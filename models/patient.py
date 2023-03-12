# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = 'mail.thread'
    _description = 'Patient Record'

    name = fields.Char(string='Name', required=True, tracking=True)
    dob = fields.Date(string="Date of birth", required=True, tracking=True)
    notes = fields.Text(string="Notes", tracking=True)
    age = fields.Integer(string='Age', compute="_calc_age", tracking=True)
    age_group = fields.Selection([
        ('baby', 'Baby'),
        ('child', 'Child'),
        ('teen', 'Teen'),
        ('adult', 'Adult'),
        ('senior', 'Senior')
    ], string="Age Group", tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        string="Gender", required=True, tracking=True)

    ref = fields.Char(string="Reference", default=lambda self: _('ID'))
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True, tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    @api.onchange('age')
    def _onchange_age(self):
        for rec in self:
            if rec.age <= 2:
                rec.age_group = 'baby'
            elif rec.age <= 11:
                rec.age_group = 'child'
            elif rec.age <= 18:
                rec.age_group = 'teen'
            elif rec.age <= 59:
                rec.age_group = 'adult'
            else:
                rec.age_group = 'senior'

    @api.depends('dob')
    def _calc_age(self):
        today = date.today()
        for rec in self:
            rec.age = relativedelta(today, rec.dob).years

    @api.constrains('dob')
    def validate_dob(self):
        for rec in self:
            if rec.dob >= date.today():
                raise ValidationError(_('Date of birth must be in the past'))

    @api.constrains('age_group', 'age')
    def validate_age_group(self):
        for rec in self:
            if rec.age_group == 'baby' and not (0 <= rec.age < 3):
                raise ValidationError(_('Babies can only be up to 2 years old'))
            elif rec.age_group == 'child' and not (3 <= rec.age < 12):
                raise ValidationError(_('Children can only be between 3 and 11 years old'))
            elif rec.age_group == 'teen' and not (12 <= rec.age < 18):
                raise ValidationError(_('Teens can only be between 12 and 17 years old'))
            elif rec.age_group == 'adult' and not (18 <= rec.age < 60):
                raise ValidationError(_('Adults can only be between 18 and 59 years old'))
            elif rec.age_group == 'senior' and rec.age < 60:
                raise ValidationError(_('Seniors can only be 60 years old or more'))
