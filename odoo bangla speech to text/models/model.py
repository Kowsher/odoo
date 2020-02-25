from odoo import models, fields, api
import BanglaSpeechRecognition as bsr



class StudentRecord(models.Model):
    _name = "test.model"

    file = fields.Selection([ ('Yes', 'Speak now'),('No', 'Speaking mode is not enabled'),],'Type', default='No')
    name = fields.Html(string='Name of model', required=True)


    @api.onchange('file')
    def Bangla_STT(self):
        if self.file == "Yes":
            if self.name:
                self.name = self.name + " " + bsr.STT_Bangla()
            else:
                self.name = bsr.STT_Bangla()
        self.file = 'No'







