# -*- coding: utf-8 -*-

{
    'name': 'Límite de crédito',
    'version': '19.1.0',
    'category': 'Accounting',
    'summary': """ Credit Limit """,
    'author': 'IT Admin',
    'company': 'IT Admin',
    'maintainer': 'IT Admin',
    'website': "https://www.itadmin.com.mx",
    'depends': ['account', 'sale',],
    'data': [
        'views/res_config_view.xml',
        'views/credit_limit_view.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
}

