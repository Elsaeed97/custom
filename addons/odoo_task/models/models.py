# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Digizilla(models.Model):
    _name = 'digizilla.model'
    _description = 'Digizilla Model'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    country = fields.Char(string='Country')
    joining_date = fields.Date(string='Joining Date')
    tags = fields.Many2many('digizilla.tag', string='Tags')
    customers = fields.Many2many('res.partner', string='Customers')
    company = fields.Many2one('res.company', string='Company', required=True)
    notes = fields.Text(string='Notes')
    comments = fields.Char(string='Comments')
    log_messages = fields.Text(string='Messages and Logger', readonly=True)

    @api.model
    def create(self, vals):
        message = "New record created: {}".format(vals)
        vals['log_messages'] = message
        return super(Digizilla, self).create(vals)

    def write(self, vals):
        message = "Record updated. Changes: {}".format(vals)
        vals['log_messages'] = message
        return super(Digizilla, self).write(vals)

    @api.model
    def action_save_and_log_changes(self):
        print("Form data saved and changes logged")


class DigizillaReport(models.AbstractModel):
    _name = 'report.digizilla'
    _description = 'Digizilla Report'

    def generate_report(self, docs):
        return self.env['report'].render('odoo_task.report_digizilla', {'docs': docs})
