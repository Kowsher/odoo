# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class ir_actions_server(models.Model):
    _inherit = 'ir.actions.server'

    is_workflow = fields.Boolean(string='Is Workflow Server Action')