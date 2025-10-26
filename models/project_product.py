from odoo import api, fields, models, _


class ProjectProject(models.Model):
    _inherit = 'project.project'

    allowed_product_ids = fields.Many2many(
        'product.product',
        'project_product_rel',
        'project_id',
        'product_id',
        string='Allowed Products',
        help='Products that can be transferred for this project'
    )

    transfer_request_count = fields.Integer(
        string='Transfer Requests',
        compute='_compute_transfer_request_count'
    )

    @api.depends('allowed_product_ids')
    def _compute_transfer_request_count(self):
        for project in self:
            project.transfer_request_count = self.env['transfer.request'].search_count([
                ('project_id', '=', project.id)
            ])

    def action_view_transfer_requests(self):
        """Open transfer requests related to this project"""
        self.ensure_one()
        return {
            'name': _('Transfer Requests'),
            'type': 'ir.actions.act_window',
            'res_model': 'transfer.request',
            'view_mode': 'tree,form',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id}
        }


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def open_product_form(self):
        """Open the product form view for this specific product"""
        self.ensure_one()
        return {
            'name': _('Product'),
            'type': 'ir.actions.act_window',
            'res_model': 'product.product',
            'res_id': self.id,
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'current',
        }
