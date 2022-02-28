# -*- coding: utf-8 -*-
{
    'name': 'Forecast Widget - Customization for Odoo',
    'version': '0.1',
    'author': 'Amondi Media d.o.o.',
    'website': 'https://amondi-media.com',
    'description': """
                    Change color or Forecast Widget. When Available qty is less than 0, change color to red, when Available qty is greater than 0, change color to green, when Available qty is less than 5 and greater than 0, change color to yellow.

    """,
    'summary': """
                    Change color of Forecast Widget according to Available qty.
    """,
    'depends': [
        'account', 'sale_stock',
    ],
    'data': [

    ],
    'qweb': [
        'static/src/xml/forecast_widget.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}