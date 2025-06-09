from odoo import api, SUPERUSER_ID

def _post_install_override(cr, registry):
    """Force the custom view to stay permanent"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.ui.view']._force_views_override(
        env.ref('crm_custom_features.crm_lead_view_form_custom')
    )