# -*- coding: utf-8 -*-

{
    'name': 'Material',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Registration of materials to be sell',
    'description': """
        Registration of materials to be sell
        Long description of module's purpose
    """,
    'author': "Imam Nawawi",
    'website': "https://www.yourdomaincompany.com",
    'data': [
        'security/ir.model.access.csv',
        'views/material.xml',
        'views/templates.xml',
    ],
    'depends': ['base'],
    'installable': True,
    'application': True,
    'demo': [
        'demo/demo.xml',
    ]
}
