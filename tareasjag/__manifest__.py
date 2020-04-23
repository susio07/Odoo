# -*- coding: utf-8 -*-
{
    'name': "tareasjag",

    'summary': """
        Módulo realizado por jag, SGE Curso 19-20""",

    'description': """
        Este módulo nos permitirá gestionar tareas
    """,

    'author': "Javier Álvarez",
    'website': "http://www.javierSL.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    
    'installable': True,
    'auto_install': False,
}