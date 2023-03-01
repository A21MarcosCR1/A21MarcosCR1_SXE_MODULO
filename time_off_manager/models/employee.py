from odoo import models, fields, api

class EmployeeModel(models.Model):
    _name = 'employee.model'
    _description = 'Employee\'s model'

    employee_id = fields.Char('Your ID', required = True)
    state = fields.Selection(
        [('allowed', 'Allowed'),
         ('not allowed', 'Not Allowed')
        ], 'Eligible for time off',
        default = 'allowed'
        )
    def make_allowed(self):
        self.state = 'allowed'

    def make_not_allowed(self):
        self.state = 'not allowed'
