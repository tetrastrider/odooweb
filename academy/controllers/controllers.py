# -*- coding: utf-8 -*-
from odoo import http
#from odoo.http import request
from odoo.addons.web.controllers import main
from odoo import SUPERUSER_ID
# class Academy(http.Controller):
class Academy(main.Home):
    @http.route('/',type="http", auth='public',website=True)
    def index(self, **kw):
    	Products = http.request.env['modelo.clientes'].sudo()
    	return http.request.render('academy.index',{'products':Products.search([]),})    	

    @http.route('/contacto',type="http", auth='public',website=True)
    def contacto(self, **kw):
    	return http.request.render('academy.contacto')    	

    @http.route('/acerca',type="http", auth='public',website=True)
    def acerca(self, **kw):
    	return http.request.render('academy.acerca')

    @http.route('/horario',type="http", auth='public',website=True)
    def horario(self, **kw):
    	return http.request.render('academy.horario')    	

    @http.route('/servicios',type="http", auth='public',website=True)
    def servicios(self, **kw):
    	return http.request.render('academy.servicios')

    @http.route('/noticias',type="http", auth='public',website=True)
    def noticias(self, **kw):
    	return http.request.render('academy.noticias')
#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })