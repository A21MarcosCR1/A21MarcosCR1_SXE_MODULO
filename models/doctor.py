from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = 'mail.thread'
    _description = 'Doctor Records'
    _rec_name = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        string="Gender", required=True, tracking=True)
    specialty = fields.Selection([
        ('family doctor', 'Family doctor'),
        ('neurologist', 'Neurologist'),
        ('nephrologist', 'Nephrologist'),
        ('dermatologist', 'Dermatologist'),
        ('psychiatrist', 'Psychiatrist'),
        ('cardiologist', 'Cardiologist'),
        ('oncologist', 'Oncologist'),
        ('gynecologist', 'Gynecologist'),
        ('endocrinologist', 'Endocrinologist')
    ], string='Medical specialty', required=True, tracking=True)
    is_surgeon = fields.Boolean(string='Surgeon', required=True, tracking=True)
    ref = fields.Char(string="Reference", default=lambda self: _('ID'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.doctor')
        return super(HospitalDoctor, self).create(vals_list)

    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res
