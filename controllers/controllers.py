# -*- coding: utf-8 -*-
# from odoo import http


# class Documents(http.Controller):
#     @http.route('/documents/documents', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/documents/documents/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('documents.listing', {
#             'root': '/documents/documents',
#             'objects': http.request.env['documents.documents'].search([]),
#         })

#     @http.route('/documents/documents/objects/<model("documents.documents"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('documents.object', {
#             'object': obj
#         })
