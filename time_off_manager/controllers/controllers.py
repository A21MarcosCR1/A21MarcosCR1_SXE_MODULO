# -*- coding: utf-8 -*-
from odoo import http


class time_off_manager(http.Controller):
    @http.route('/time_off_manager/time_off_manager/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/time_off_manager/time_off_manager/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('time_off_manager.listing', {
            'root': '/time_off_manager/time_off_manager',
            'objects': http.request.env['time_off_manager.time_off_manager'].search([]),
        })
    @http.route('/time_off_manager/time_off_manager/objects/<model("time_off_manager.time_off_manager"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('time_off_manager.object', {
            'object': obj
        })