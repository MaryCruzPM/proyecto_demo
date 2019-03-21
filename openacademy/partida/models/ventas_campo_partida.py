# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class ventas_campo_partida(models.Model):
	"""docstring for ClassName"""
	_inherit='sale.order.line'

	
	
	partida = fields.Integer()