#!/usr/bin/env python3
"""
Product Import Script for Odoo Hardware Store
Imports and normalizes product catalog with duplicate control and quality validation.

Usage:
    python3 scripts/import_products.py data/product_template.csv [--output output.json] [--validate-only]
"""

import csv
import json
import sys
import argparse
import re
from typing import Dict, List, Tuple
from collections import defaultdict


class ProductValidator:
    """Validates product data quality"""
    
    REQUIRED_FIELDS = ['sku', 'name', 'category', 'price', 'stock', 'status']
    VALID_STATUSES = ['active', 'inactive', 'discontinued']
    MIN_PRICE = 0
    MAX_NAME_LENGTH = 200
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_product(self, product: Dict, line_num: int) -> bool:
        """Validate a single product record"""
        is_valid = True
        
        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if not product.get(field) or str(product[field]).strip() == '':
                self.errors.append(f"Line {line_num}: Missing required field '{field}'")
                is_valid = False
        
        # Validate SKU format (alphanumeric with optional dashes/underscores)
        sku = product.get('sku', '')
        if sku and not re.match(r'^[A-Z0-9_-]+$', sku.upper()):
            self.errors.append(f"Line {line_num}: Invalid SKU format '{sku}'. Use only letters, numbers, dashes, and underscores.")
            is_valid = False
        
        # Validate price
        try:
            price = float(product.get('price', 0))
            if price < self.MIN_PRICE:
                self.errors.append(f"Line {line_num}: Price must be >= {self.MIN_PRICE}")
                is_valid = False
        except (ValueError, TypeError):
            self.errors.append(f"Line {line_num}: Invalid price value '{product.get('price')}'")
            is_valid = False
        
        # Validate stock
        try:
            stock = int(product.get('stock', 0))
            if stock < 0:
                self.warnings.append(f"Line {line_num}: Negative stock value {stock}")
        except (ValueError, TypeError):
            self.errors.append(f"Line {line_num}: Invalid stock value '{product.get('stock')}'")
            is_valid = False
        
        # Validate status
        status = product.get('status', '').lower()
        if status and status not in self.VALID_STATUSES:
            self.errors.append(f"Line {line_num}: Invalid status '{status}'. Must be one of: {', '.join(self.VALID_STATUSES)}")
            is_valid = False
        
        # Validate name length
        name = product.get('name', '')
        if len(name) > self.MAX_NAME_LENGTH:
            self.warnings.append(f"Line {line_num}: Product name exceeds {self.MAX_NAME_LENGTH} characters")
        
        # Check for image URL
        if not product.get('image_url'):
            self.warnings.append(f"Line {line_num}: Missing image URL for product '{product.get('name')}'")
        
        return is_valid
    
    def get_report(self) -> str:
        """Generate validation report"""
        report = []
        if self.errors:
            report.append(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                report.append(f"  - {error}")
        
        if self.warnings:
            report.append(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                report.append(f"  - {warning}")
        
        return '\n'.join(report)


class ProductImporter:
    """Imports and normalizes product data"""
    
    def __init__(self):
        self.validator = ProductValidator()
        self.products = []
        self.duplicates = defaultdict(list)
    
    def normalize_product(self, product: Dict) -> Dict:
        """Normalize product data (assumes validation has already passed)"""
        normalized = {}
        
        # Normalize SKU (uppercase, trim)
        normalized['sku'] = product.get('sku', '').strip().upper()
        
        # Trim and title case name
        normalized['name'] = product.get('name', '').strip()
        
        # Normalize category and subcategory
        normalized['category'] = product.get('category', '').strip()
        normalized['subcategory'] = product.get('subcategory', '').strip()
        
        # Normalize brand
        normalized['brand'] = product.get('brand', '').strip()
        
        # Format price (validation ensures this is valid)
        normalized['price'] = float(product.get('price', 0))
        
        # Format stock (validation ensures this is valid)
        normalized['stock'] = int(product.get('stock', 0))
        
        # Normalize unit
        normalized['unit'] = product.get('unit', 'unidad').strip().lower()
        
        # Trim descriptions
        normalized['short_description'] = product.get('short_description', '').strip()
        normalized['long_description'] = product.get('long_description', '').strip()
        
        # Normalize image URL
        normalized['image_url'] = product.get('image_url', '').strip()
        
        # Normalize status
        normalized['status'] = product.get('status', 'active').strip().lower()
        
        return normalized
    
    def detect_duplicates(self, products_with_lines: List[Tuple[Dict, int]]) -> Dict[str, List[int]]:
        """Detect duplicate products by SKU with accurate line numbers"""
        sku_map = defaultdict(list)
        
        for product, line_num in products_with_lines:
            sku = product.get('sku', '')
            if sku:
                sku_map[sku].append(line_num)
        
        # Filter only duplicates
        duplicates = {sku: lines for sku, lines in sku_map.items() if len(lines) > 1}
        return duplicates
    
    def import_from_csv(self, file_path: str) -> Tuple[List[Dict], bool]:
        """Import products from CSV file"""
        products = []
        products_with_lines = []  # Track products with their line numbers
        line_num = 1  # Start at 1 for header
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    line_num += 1
                    
                    # Validate product
                    if not self.validator.validate_product(row, line_num):
                        continue
                    
                    # Normalize and add to list
                    normalized = self.normalize_product(row)
                    products.append(normalized)
                    products_with_lines.append((normalized, line_num))
        
        except FileNotFoundError:
            print(f"❌ Error: File '{file_path}' not found")
            return [], False
        except Exception as e:
            print(f"❌ Error reading file: {str(e)}")
            return [], False
        
        # Detect duplicates using line numbers
        duplicates = self.detect_duplicates(products_with_lines)
        
        if duplicates:
            print(f"\n❌ DUPLICATE SKUs DETECTED:")
            for sku, lines in duplicates.items():
                print(f"  - SKU '{sku}' found on lines: {', '.join(map(str, lines))}")
            print("\n⚠️  Please resolve duplicates before importing.")
            return products, False
        
        self.products = products
        return products, True
    
    def export_to_json(self, output_path: str):
        """Export normalized products to JSON"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.products, f, indent=2, ensure_ascii=False)
            print(f"✅ Products exported to '{output_path}'")
        except Exception as e:
            print(f"❌ Error exporting to JSON: {str(e)}")
    
    def print_summary(self):
        """Print import summary"""
        print(f"\n{'='*60}")
        print(f"📦 PRODUCT IMPORT SUMMARY")
        print(f"{'='*60}")
        print(f"Total products imported: {len(self.products)}")
        
        # Count by category
        categories = defaultdict(int)
        for product in self.products:
            categories[product['category']] += 1
        
        print(f"\nProducts by category:")
        for category, count in sorted(categories.items()):
            print(f"  - {category}: {count}")
        
        # Count by status
        statuses = defaultdict(int)
        for product in self.products:
            statuses[product['status']] += 1
        
        print(f"\nProducts by status:")
        for status, count in sorted(statuses.items()):
            print(f"  - {status}: {count}")
        
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Import and normalize product catalog for Odoo'
    )
    parser.add_argument(
        'input_file',
        help='Input CSV file path'
    )
    parser.add_argument(
        '--output', '-o',
        default='data/products_normalized.json',
        help='Output JSON file path (default: data/products_normalized.json)'
    )
    parser.add_argument(
        '--validate-only', '-v',
        action='store_true',
        help='Only validate without creating output file'
    )
    
    args = parser.parse_args()
    
    print(f"\n{'='*60}")
    print(f"🔧 ODOO PRODUCT IMPORTER")
    print(f"{'='*60}\n")
    print(f"Input file: {args.input_file}")
    
    # Import and validate
    importer = ProductImporter()
    products, is_valid = importer.import_from_csv(args.input_file)
    
    # Print validation report
    report = importer.validator.get_report()
    if report:
        print(report)
    
    # Check if validation passed
    if not is_valid:
        print("\n❌ Import failed due to validation errors.")
        sys.exit(1)
    
    if args.validate_only:
        print("\n✅ Validation passed!")
        importer.print_summary()
        sys.exit(0)
    
    # Export to JSON
    if products:
        importer.export_to_json(args.output)
        importer.print_summary()
        print("✅ Import completed successfully!")
    else:
        print("\n⚠️  No products to import.")
        sys.exit(1)


if __name__ == '__main__':
    main()
