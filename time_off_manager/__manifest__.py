# -*- coding: utf-8 -*-
{
    'name': "Time Off Manager",

    'summary': """
        Submit requests for time off, to be approved by your superiors
        """,

    'description': """
        This module is meant to be used by employees to request time off
        from their superiors. The superiors can then review such requests
        and then decide to approve them or not.

        Additionally, the employee's calendar should keep track of 
        approved requests so the timespan of this time off is registered.
    """,

    'author': "Marcos Chamosa Rodriguez",
    'license': "",
    'website': "https://github.com/A21MarcosCR1/A21MarcosCR1_SXE_MODULO",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '14.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
