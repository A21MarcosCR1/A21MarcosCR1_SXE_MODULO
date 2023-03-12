from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date


class PatientAppointment(models.Model):
    _name = 'patient.appointment'
    _inherit = 'mail.thread'
    _description = 'Appointment Records'
    _rec_name = 'ref'

    ref = fields.Char(string="Reference", default=lambda self: _('ID'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    date_appointment = fields.Date(string ="Date of appointment", required=True, tracking=True)
    notes_on_appointment = fields.Text(string="Diagnostic notes", tracking=True)
    prescription = fields.Text(string="Prescription", tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('patient.appointment')
        return super(PatientAppointment, self).create(vals_list)

    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.patient_id.name} - {rec.doctor_id.name}'
            res.append((rec.id, name))
        return res

    @api.constrains('date_appointment')
    def validate_appointment(self):
        today = date.today()
        for rec in self:
            if rec.date_appointment < today:
                raise ValidationError(_('Appointment must be set in the future or present day'))
