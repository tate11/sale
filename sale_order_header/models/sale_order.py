# -*- coding: utf-8 -*-
from openerp import fields, models, api, _


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        # Handling for when invoicing the invoiceable lines
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['header_text'] = self.header_text
        return invoice_vals

    header_text = fields.Char('Header', help='Header or title of the Sale')
