# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo 17 Accounting',
    'version': '17.01',
    'category': 'Accounting',
    'summary': 'Reportes contables, Manejo de activos y presupuesto, Pagos recurrentes, '
               'Fechas de cierre, Año fiscal, Tablero contabildiad, Reportes financieros, '
               'Seguimiento de clientes, Conciliación bancaria',
    'description': 'Reportes contables, Manejo de activos y presupuesto, Pagos recurrentes, '
               'Fechas de cierre, Año fiscal, Tablero contabildiad, Reportes financieros, '
               'Seguimiento de clientes, Conciliación bancaria',
    'sequence': '1',
    'website': 'https://odoo.itadmin.com.mx',
    'author': 'IT Admin',
    'license': 'LGPL-3',
    'support': 'soporte@itadmin.com.mx',
    'depends': [
        'mx_credit_limit',
        'om_account_asset',
        'om_account_budget',
        'om_fiscal_year',
        'om_recurring_payments',
        'account_reconcile_oca',
        'om_account_followup',
        'stock_accounting',
        'dynamic_accounts_report',
    ],
    'data': [
        'security/group.xml',
        'views/menu.xml',
        'views/settings.xml',
        'views/account_group.xml',
        'views/account_tag.xml',
        'views/res_partner.xml',
        'views/account_bank_statement.xml',
        'views/payment_method.xml',
        'views/reconciliation.xml',
        'views/account_journal.xml',
        'views/ledger_menu.xml',
    ],
    'application': True,
    'images': ['static/description/banner.gif'],
}

