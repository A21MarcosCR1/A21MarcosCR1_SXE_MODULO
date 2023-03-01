# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import re


class TimeOffRequest(models.Model):
    _name = 'time.off.request'
    _description = 'Time off request'

    employee_id = fields.Many2one('employee.model', 'Your ID', required = True)
    reason_for_time_off = fields.Char("Explain your reasons: ", required = True)
    date_begin = fields.Date('Starting date', required=True)
    date_end = fields.Date('End date', required = True)

    def _date_is_valid(self):
        return self.date_end >= self.date_begin
    
    def _id_is_valid(self):
        return  re.search(r'[0-9]{8}[A-Z]', self.employee_id)
    
    def validate_request(self):
        if not self._date_is_valid:
            raise UserError('The passed dates are not valid!')
        if not self._id_is_valid(self):
            raise UserError('That id is not valid')
