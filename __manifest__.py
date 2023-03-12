{
    'name': 'Hospital Management System',
    'author': 'Marcos Chamosa Rodríguez',
    'website': 'https://github.com/A21MarcosCR1/modulo_hospital',
    'summary': 'A simple module to manage doctors and patients in a hospital'
               ', as well as the appointments they can have between them and'
               ' the result of them.',
    'category': 'Administration',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/sequence_doctor.xml',
        'data/sequence_appointment.xml',
        'views/menu.xml',
        'views/appointment.xml',
        'views/patient.xml',
        'views/doctor.xml'
    ],

    'demo': ['data/demo_doctors.xml',
             'data/demo_patient.xml']
}
