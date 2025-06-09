from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    lead_source = fields.Selection(
        selection=[
            ('facebook', 'Facebook'),
            ('instagram', 'Instagram'),
            ('website', 'Website'),
            ('event', 'Event'),
            ('other', 'Other')
        ],
        string='Lead Source',
        readonly=True,
        default='other',
        compute='_compute_lead_source',
        store=True
    )

    @api.depends('email_from')
    def _compute_lead_source(self):
        for lead in self:
            email = (lead.email_from or '').lower()
            if 'facebook' in email:
                lead.lead_source = 'facebook'
            elif 'instagram' in email:
                lead.lead_source = 'instagram'
            elif 'website' in email:
                lead.lead_source = 'website'
            elif 'event' in email:
                lead.lead_source = 'event'
            else:
                lead.lead_source = 'other'