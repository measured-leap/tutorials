{
    'name': 'Estate',
    'category': 'Estate',
    'version': '1.0',
    'summary': 'Real estate advertisement module',
    'description': 'This module is a basic real estate listing system.',
    'author': 'measured-leap',
    'website': 'https://github.com/measured-leap/tutorials/tree/estate-module/estate',
    'license': 'LGPL-3',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'actions/estate_property_action.xml',
        'menus/estate_menus.xml'
    ]
}
