    # -*- coding: utf-8 -*-
{
'name': "herencia ejemplo",
'sumary': """
mi modulo de odoo11 con inherit wit class partner
""",
'description': """
Probando modulo odoo11 y con clases y con herencia
""",
'author': "Soluciones 4G",
'website': "http:www.soluciones4g.com",

'category': 'pruebas',
'version': '1.0',

'depends': [
'base',
'contacts',
],

'data':[
#'security/ir.model.access.csv',
#'templates.xml',
#'views/openacademy.xml',
'views/partner.xml',
],

'installable':True,
'auto_install':False,

}