# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MaterialType(models.Model):
    _name = 'material.type'
    _description = 'Material Type'
    _order = 'id'

    name = fields.Char('Name', required=True)
    note = fields.Html(string='Note')


class Supplier(models.Model):
    _name = 'supplier.supplier'
    _description = 'Supplier'
    _order = 'id'

    name = fields.Char('Name', required=True)
    phone = fields.Char('Phone', required=True)
    address = fields.Char('Address', required=True)


class Material(models.Model):
    _name = 'material.material'
    _description = 'Material'
    _order = 'id'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    type_id = fields.Many2one('material.type', 'Type', required=True)
    buy_price = fields.Float('Buy Price', required=True)
    supplier_id = fields.Many2one('material.supplier', 'Supplier', required=True)
    
    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("Buy price cannot less than 100!")
