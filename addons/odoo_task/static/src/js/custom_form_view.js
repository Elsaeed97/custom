odoo.define('odoo_task.custom_form_view', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        /**
         * @override
         */
        renderButtons: function ($node) {
            this._super.apply(this, arguments);

            // Hide the create button
            this.$buttons.find('.o_form_button_create').hide();
        },
    });
});
