# -*- coding: utf-8 -*-
# Copyright 2018 Vignesh @ Annadurai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Animated Lock Unlock SO from tree Alertify message",

    'summary': """
        Lock / unlock SO from Tree itself, Only works for version 11, ANIMATED LOCK/UNLOCK screen with NEW NOTIFIED MESSAGES
      """,
    'author': " Vignesh ",
    'website': "viki2.odoo.com",
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'category': 'Sale',
    'version': '11.0.0.1',
    'depends': ['base', 'sale',
                ],
     'images': ['images/main_screenshot.png'],
    'data': [
        'views/sale_views.xml',
        'views/custom_scripts.xml',
    ],
    'demo': [
    ],
}
