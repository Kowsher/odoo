# -*- coding: utf-8 -*-

import json

from collections import OrderedDict
from openerp import http  # @UnresolvedImport
from openerp.addons.website.controllers.main import Website
from openerp.http import request  # @UnresolvedImport

FIELDS = ['id', 'parent_id', 'name']



class Main(Website):


    @http.route(['/ir_ui_menu/get_org_chart/<int:employee_id>'],
                type='http', auth="public", website=True)
    def get_org_chart(self, employee_id=0):

        Model = request.env['ir.ui.menu'].sudo()

        employee_ids = Model.browse(employee_id)
        manager = employee_ids.parent_id
        employee_ids |= manager
        employee_ids |= Model.search([('parent_id', 'child_of', employee_id)])
        data_source = self.get_chart_data_source(employee_ids)

        data = {'dataSource': data_source,
                'customize': {manager.id: {"color": "darkred"},
                              employee_id: {"color": "teal"}},
                'expandToLevel': manager and 3 or 2
                }

        return json.dumps(data)

    def get_chart_data_source(self, employee_ids):

        res = []
        for employee in employee_ids:
            employee_dict = OrderedDict()
            for field in FIELDS:
                field_value = None
                if field == "parent_id":
                    field_value = getattr(employee, field, None)
                    field_value = field_value and field_value.id or None
                elif field.endswith("id") and field != 'id':
                    field_value = getattr(employee, field, None)
                    field_value = field_value and field_value.name or ''
                else:
                    field_value = getattr(employee, field, None)

                employee_dict[field] = field_value

            res.append(employee_dict)
        return res
