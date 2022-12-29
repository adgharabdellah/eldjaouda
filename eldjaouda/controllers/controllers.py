# -*- coding: utf-8 -*-
# from odoo import http


# class Eldjaouda(http.Controller):
#     @http.route('/eldjaouda/eldjaouda', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eldjaouda/eldjaouda/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eldjaouda.listing', {
#             'root': '/eldjaouda/eldjaouda',
#             'objects': http.request.env['eldjaouda.eldjaouda'].search([]),
#         })

#     @http.route('/eldjaouda/eldjaouda/objects/<model("eldjaouda.eldjaouda"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eldjaouda.object', {
#             'object': obj
#         })
