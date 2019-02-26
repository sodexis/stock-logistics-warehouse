# Copyright 2014 Numérigraphe SARL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    def _compute_available_quantities_dict(self):
        res = super(ProductTemplate, self)._compute_available_quantities_dict()
        add_potential_qty = self.env['ir.config_parameter'].sudo().get_param('add_potential_qty')
        for template in self.filtered('bom_ids'):
            if add_potential_qty:
                res[template.id]['immediately_usable_qty'] =\
                    template.virtual_available + res[template.id]['potential_qty']
            else:
                res[template.id]['immediately_usable_qty'] = template.virtual_available
        return res
