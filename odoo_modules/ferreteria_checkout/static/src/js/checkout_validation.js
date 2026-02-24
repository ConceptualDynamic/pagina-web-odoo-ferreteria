/** @odoo-module **/

import publicWidget from 'web.public.widget';
import { _t } from 'web.core';

publicWidget.registry.FerreteriaCheckoutValidation = publicWidget.Widget.extend({
    selector: '.oe_website_sale',
    events: {
        'change input[name="partner_vat"]': '_onVatChange',
        'change select[name="customer_type"]': '_onCustomerTypeChange',
        'click #apply_coupon_btn': '_onApplyCoupon',
        'submit #o_payment_form': '_onSubmitPayment',
    },

    /**
     * Validate VAT/ID number format
     */
    _onVatChange: function (ev) {
        const $input = $(ev.currentTarget);
        const vat = $input.val().trim();
        
        if (vat && !this._validateVat(vat)) {
            $input.addClass('is-invalid');
            this._showError($input, 'Formato de documento inválido (6-10 dígitos)');
        } else {
            $input.removeClass('is-invalid');
            this._hideError($input);
        }
    },

    /**
     * Validate VAT format
     */
    _validateVat: function (vat) {
        return /^[0-9]{6,10}$/.test(vat);
    },

    /**
     * Handle customer type change
     */
    _onCustomerTypeChange: function (ev) {
        const customerType = $(ev.currentTarget).val();
        const $vatInput = $('input[name="partner_vat"]');
        
        if (customerType === 'company') {
            $vatInput.attr('placeholder', 'NIT de la empresa');
        } else {
            $vatInput.attr('placeholder', 'Número de cédula');
        }
    },

    /**
     * Apply coupon code
     */
    _onApplyCoupon: function (ev) {
        ev.preventDefault();
        const couponCode = $('#coupon_code_input').val().trim();
        const $messageDiv = $('#coupon_message');
        const $button = $(ev.currentTarget);
        
        if (!couponCode) {
            this._showCouponMessage('Por favor ingresa un código de cupón', 'warning');
            return;
        }
        
        $button.prop('disabled', true).text('Aplicando...');
        
        this._rpc({
            route: '/shop/apply_coupon',
            params: {
                coupon_code: couponCode,
            },
        }).then((result) => {
            if (result.success) {
                this._showCouponMessage(result.message, 'success');
                // Reload page to update totals
                window.location.reload();
            } else {
                this._showCouponMessage(result.message, 'danger');
            }
        }).catch((error) => {
            this._showCouponMessage('Error al aplicar cupón. Intenta nuevamente.', 'danger');
        }).finally(() => {
            $button.prop('disabled', false).text('Aplicar');
        });
    },

    /**
     * Show coupon message
     */
    _showCouponMessage: function (message, type) {
        const $messageDiv = $('#coupon_message');
        const $alert = $('<div class="alert"></div>')
            .addClass('alert-' + type)
            .text(message);  // Use .text() to prevent XSS
        $messageDiv.html($alert);
    },

    /**
     * Validate form before payment submission
     */
    _onSubmitPayment: function (ev) {
        const $form = $(ev.currentTarget);
        let isValid = true;
        
        // Validate VAT
        const $vatInput = $('input[name="partner_vat"]');
        if ($vatInput.length && !this._validateVat($vatInput.val())) {
            isValid = false;
            this._showError($vatInput, 'Por favor ingresa un número de documento válido');
        }
        
        // Validate required fields
        $form.find('[required]').each((index, field) => {
            const $field = $(field);
            const value = $field.val();
            if (!value || value.trim() === '') {
                isValid = false;
                this._showError($field, 'Este campo es obligatorio');
            }
        });
        
        if (!isValid) {
            ev.preventDefault();
            this._showGlobalError('Por favor completa todos los campos requeridos correctamente');
        }
    },

    /**
     * Show error message for a field
     */
    _showError: function ($field, message) {
        $field.addClass('is-invalid');
        let $feedback = $field.next('.invalid-feedback');
        if ($feedback.length === 0) {
            $feedback = $('<div class="invalid-feedback"></div>');
            $field.after($feedback);
        }
        $feedback.text(message);
    },

    /**
     * Hide error message for a field
     */
    _hideError: function ($field) {
        $field.removeClass('is-invalid');
        $field.next('.invalid-feedback').remove();
    },

    /**
     * Show global error message
     */
    _showGlobalError: function (message) {
        const $alert = $('<div class="alert alert-danger alert-dismissible fade show" role="alert"></div>')
            .text(message);
        const $closeButton = $('<button type="button" class="close" data-dismiss="alert" aria-label="Close"></button>')
            .append('<span aria-hidden="true">&times;</span>');
        $alert.append($closeButton);
        $('#o_payment_form').prepend($alert);
        $('html, body').animate({ scrollTop: 0 }, 300);
    },
});

export default publicWidget.registry.FerreteriaCheckoutValidation;
