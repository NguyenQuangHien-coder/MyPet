# -*- coding: utf-8 -*-
{
    'name': "MyPet (+)",
    'summary': """My pet plus""",
    'description': """Managing pet information""",
    'author': "ShiroNeko",
    'website': "https://shironeko.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'mypet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_plus_views.xml',
        'views/product_pet_views.xml',
        'views/my_pet_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}