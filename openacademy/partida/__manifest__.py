# -*- coding: utf-8 -*-
{
    'name': "partida odoo11 ventas",

    'summary': """Ejercicios
    """,

    'description': """
        Modulos para ventas 
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'purchase',
        'sale',
        'sale_management',
        'contacts',
        'stock',

    ],

    # always loaded
	'data': [
	'views/ventas_partida.xml',
       
    ],
	'demo':[

	],
    'installable':True,
}
