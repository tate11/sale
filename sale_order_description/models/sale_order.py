# -*- coding: utf-8 -*-
from openerp import models, fields


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    description = fields.Text("Description",
                              help='Internal notes')
