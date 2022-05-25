# -*- coding: utf-8 -*-


from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'wizard.wizard'

    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)

    def find_by_date(self):
        sorted_documents = []
        sort_documents = self.env['documents.documents'].search([('document_date', '>=', self.date_start),
                                                                 ('document_date', '<=', self.date_end)])

        for document in sort_documents:
            sorted_documents.append({
                'name': document.name,
                'description': document.description,
                'company': document.company_id.name,
                'document_date': document.document_date
            })

        data = {
            'vals': sorted_documents
        }

        return self.env.ref('documents.sorted_documents_report').report_action(self, data=data)


