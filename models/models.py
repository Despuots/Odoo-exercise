# -*- coding: utf-8 -*-

from odoo import models, fields


class Documents(models.Model):
    _name = 'documents.documents'
    _description = 'documents.documents'

    name = fields.Char(string="Pavadinimas")
    description = fields.Text(string="Aprašymas")
    company_id = fields.Many2one('res.company', string="Kompanija")




