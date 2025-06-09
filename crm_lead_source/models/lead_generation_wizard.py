from odoo import models, fields, api

class LeadGenerationWizard(models.TransientModel):
    _name = 'lead.generation.wizard'
    _description = 'Lead Generation Wizard'

    number_of_leads = fields.Integer(string="How many leads would you like?", required=True)
    country_id = fields.Many2one('res.country', string="Country")
    state_id = fields.Many2one('res.country.state', string="State")
    industry_id = fields.Many2one('res.partner.industry', string="Industry")
    size_filter = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ], string="Filter on Size")
    source = fields.Selection([
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('website', 'Website'),
        ('event', 'Event'),
        ('other', 'Other'),
    ], string="Lead Source")
    sales_team_id = fields.Many2one('crm.team', string="Sales Team")
    user_id = fields.Many2one('res.users', string="Salesperson")
    tag_ids = fields.Many2many('crm.tag', string="Default Tags")

    def action_generate_leads(self):
        """Generate leads based on the wizard inputs."""
        leads = []
        for i in range(self.number_of_leads):
            lead_vals = {
                'name': f"Auto Generated Lead {i + 1}",
                'country_id': self.country_id.id if self.country_id else False,
                'state_id': self.state_id.id if self.state_id else False,
                'industry_id': self.industry_id.id if self.industry_id else False,
                'lead_source': self.source,
                'team_id': self.sales_team_id.id if self.sales_team_id else False,
                'user_id': self.user_id.id if self.user_id else False,
                'tag_ids': [(6, 0, self.tag_ids.ids)] if self.tag_ids else False,
            }
            lead = self.env['crm.lead'].create(lead_vals)
            leads.append(lead)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Generated Leads',
            'res_model': 'crm.lead',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', [lead.id for lead in leads])],
            'target': 'current',
        }
