# -*- coding: utf-8 -*-
##########################################################
###                 Disclaimer                         ###
##########################################################
### NKSOft      ###
                    ###
##########################################################

{
    'name': 'NKSoft Workflow',
    'version': '1.0',
    'sequence': '10',
    'category': 'Extra Tools',
    'author': 'NKSoft',
    'website': 'http://nksoft.com/',
    'summary': 'Dynamic Workflow',
    'images': [
        'static/description/banner.png',
    ],
    'description': """
Dynamic Workflow Builder
========================
* You can build dynamic workflow for any model.
""",
    'data': [
        'templates/webclient_templates.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'wizards/views/odoo_workflow_refuse_wizard_view.xml',
        'wizards/views/odoo_workflow_update_wizard_view.xml',
        'views/odoo_workflow_view.xml',
        'views/ir_actions_server_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
