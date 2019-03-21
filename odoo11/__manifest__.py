# -*- coding: utf-8 -*-
{
'name': "Modulo odoo 11",
'sumary': """
mi modulo de odoo11
""",
'description': """
Probando modulo odoo11 y con clases
""",
'author': "Soluciones 4G",
'website': "http:www.soluciones4g.com",

'category': 'pruebas',
'version': '1.0',

'depends': [
'base',
],

'data':[
'views/academy_view.xml',
'security/ir.model.access.csv',

],

'installable':True,
'auto_install':False,

}