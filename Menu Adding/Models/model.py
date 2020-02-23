from odoo import models, fields


class StudentRecord(models.Model):
    _name = "menu.add"


    name = fields.Char(string='Name of Child', required=True)
    parent_id = fields.Many2one("menu.add", "Parent Menu", select=True)
    child_id = fields.One2many('menu.add', 'parent_id', string='Child')
