# -*- coding: utf-8 -*-
# from odoo import http


# class OdooTask(http.Controller):
#     @http.route('/odoo_task/odoo_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_task/odoo_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_task.listing', {
#             'root': '/odoo_task/odoo_task',
#             'objects': http.request.env['odoo_task.odoo_task'].search([]),
#         })

#     @http.route('/odoo_task/odoo_task/objects/<model("odoo_task.odoo_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_task.object', {
#             'object': obj
#         })

