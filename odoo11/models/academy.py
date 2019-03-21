 #-*- coding:utf-8 -*-
from odoo import fields
from odoo import models

class academy(models.Model): #
	_name = 'academy.main_data'
	_description ="academy"
	
	name =fields.Char(
		string="nombre de la academia",
		required=True,
		index=True,
		)
	clave = fields.Integer( 
		string="clave",
		required=True,
		)
	grado=fields.Char( 
		string="grado",
		)
	director=fields.Char(
		string="director",
		)
	informacion_adicional=fields.Text(
		string="informacio_adicional",
		)
	foto=fields.Binary(
		string="foto",
		help="agrega una foto",
		)
	description=fields.Char(
		string="description",
		)