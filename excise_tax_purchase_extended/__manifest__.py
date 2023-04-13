# -*- coding: utf-8 -*-
{
    'name': "Purchase Excise Tax",

    'summary': """
        This module add excise tax amount in purchase order line.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sarath",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_extended_view.xml',
        'views/account_move_extended_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
