#-*- coding:utf-8 -*-

{
    'name': 'Stock Accounting',
    'category': 'Stock',
    'author': 'IT Admin',
    'version': '17.01',
    'website': 'https://www.itadmin.com.mx',
    'summary': 'Agrega opción oculta para la contabilidad de inventario.',
    'description': """Agrega opción oculta para la contabilidad de inventario.""",
    'depends': [
        'stock', 
    ],
    'data': [
        'views/res_config_settings_view.xml',
    ],
    'application': True,
}
