# Copyright 2014 Numérigraphe
# Copyright 2016 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    """Add options to add 'Potential' quantity to 'Available to promise' only if it is needed"""
    _inherit = 'res.config.settings'


    add_potential_qty = fields.Boolean(
        string='Add Potential To Available',
        help="If set true then potential quantity is added to the " 
             "available to promise quantity")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(add_potential_qty=self.env[
            'ir.config_parameter'].sudo().get_param(
                'add_potential_qty', self.add_potential_qty)
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'add_potential_qty', self.add_potential_qty)
