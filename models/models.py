# -*- coding: utf-8 -*-

from odoo import models, fields


class Documents(models.Model):
    _name = 'documents.documents'
    _description = 'documents.documents'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    company_id = fields.Many2one('res.company', string="Company")
    document_date = fields.Date(default=fields.Datetime.now)




