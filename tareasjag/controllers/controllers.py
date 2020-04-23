# -*- coding: utf-8 -*-
from odoo import http

# class Tareasjag(http.Controller):
#     @http.route('/tareasjag/tareasjag/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tareasjag/tareasjag/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tareasjag.listing', {
#             'root': '/tareasjag/tareasjag',
#             'objects': http.request.env['tareasjag.tareasjag'].search([]),
#         })

#     @http.route('/tareasjag/tareasjag/objects/<model("tareasjag.tareasjag"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tareasjag.object', {
#             'object': obj
#         })