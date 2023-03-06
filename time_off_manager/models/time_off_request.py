# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TimeOffRequest(models.Model):
    _name = 'time.off.request'
    _description = 'Time off request form'

    employee_id = fields.Many2one('hr.employee', string = 'Employee ID', required = True)
    reason_for_time_off = fields.Char("Explain your reasons: ", required = True)
    date_begin = fields.Date('Starting date', required=True)
    date_end = fields.Date('End date', required = True)

    def date_is_valid(self):
        return self.date_end >= self.date_begin
    
    
    @api.model
    def create(self, vals):
        if self.employee_id in vals:
            employee = self.env['hr.employee'].browse(vals['employee_id']) 
            raise ValidationError('Invalid employee ID!')
        elif not self.date_is_valid():
            raise ValidationError('Invalid date configuration!')
        return super(TimeOffRequest, self).create(vals)