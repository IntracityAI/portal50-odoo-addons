# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Portal50TestModel(models.Model):
    _name = 'portal50.test.model'
    _description = 'Portal50 Test Model'
    _order = 'name'

    name = fields.Char(string='Name', required=True, index=True)
    description = fields.Text(string='Description')

