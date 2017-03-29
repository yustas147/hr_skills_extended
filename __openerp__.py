# -*- coding: utf-8 -*-
{
    'name': "hr_skills_extended",

    'summary': """
        Adds 2 fields to hr_skills.hr_skill model
""",

    'description': """
        Adds 2 fields to hr_skills.hr_skill model: Percentage and Description
    """,

    'author': "Simbioz",
    'website': "http://simbioz.odooua.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_skill','hr_ext_qa'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
     #   'templates.xml',
        'views/inherited_hr_skill_views.xml',
        'views/hr_employee_skill_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
     #   'demo.xml',
    ],
}
