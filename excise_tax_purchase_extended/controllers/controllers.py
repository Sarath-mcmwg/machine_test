# -*- coding: utf-8 -*-
# from odoo import http


# class ExciseTaxPurchaseExtended(http.Controller):
#     @http.route('/excise_tax_purchase_extended/excise_tax_purchase_extended', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/excise_tax_purchase_extended/excise_tax_purchase_extended/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('excise_tax_purchase_extended.listing', {
#             'root': '/excise_tax_purchase_extended/excise_tax_purchase_extended',
#             'objects': http.request.env['excise_tax_purchase_extended.excise_tax_purchase_extended'].search([]),
#         })

#     @http.route('/excise_tax_purchase_extended/excise_tax_purchase_extended/objects/<model("excise_tax_purchase_extended.excise_tax_purchase_extended"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('excise_tax_purchase_extended.object', {
#             'object': obj
#         })
