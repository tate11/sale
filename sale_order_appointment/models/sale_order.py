# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class SaleOrder(models.Model):
    
    # 1. Private attributes
    _inherit = 'sale.order'

    # 2. Fields declaration
    discount_code = fields.Char("Discount code")
    appointment_date = fields.Datetime("Scheduled date")
    appointment_date_end = fields.Datetime("Scheduled date end")
    appointment_cancel_url = fields.Char("Cancel url")
    appointment_existing_customer = fields.Boolean("Existing customer")

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
