CRM Customization - Lead Source Tracking

Overview : 

This module enhances Odoo's CRM functionality by:

Adding a "Source" field in the Quick Create Lead Form to track where leads originate.

Providing insights into lead acquisition channels for better marketing and sales analysis.


Features : 

✅ Source Field in Quick Create Form.

1 ] The source_id field is now visible in the quick creation form for leads.

2 ] Users can select or enter how the lead was acquired (e.g., Website, Social Media, Referral, etc.).

✅ Improved Lead Source Tracking.

1 ] Helps sales teams understand which marketing channels generate the most leads.

2 ] Enables filtering and reporting based on lead sources.

✅ User-Friendly Placeholder

1] The field includes a placeholder ("How did you hear about us?") for better UX.

Installation :

1 ] Clone or download the module into your Odoo addons directory.

2 ] Install the module via:

Odoo Apps (go to Apps → Update Apps List, then search for crm_lead_source_tracking)

Command Line:

bash
odoo-bin -i crm_lead_source_tracking --db <your_database> --http-port <port>

3 ] Restart Odoo to apply changes.

Project folder structure : custom_addons/
└── crm_lead_source/
    ├── __init__.py
    ├── __manifest__.py
    ├── hooks.py                          # Optional, only if needed
    │
    ├── models/
    │   ├── __init__.py
    │   ├── crm_lead.py                   # Python logic for `crm.lead` extension
    │   └── lead_generation_wizard.py     # Wizard class (if used)
    │
    ├── views/
    │   ├── crm_lead_views.xml            # Main Form, Kanban, Tree view customization
    │   ├── crm_lead_filter.xml           # Search view
    │   ├── lead_generation_wizard_view.xml  # Wizard view (if any)
    │
    ├── security/
    │   └── ir.model.access.csv           # Required for model access rights
    │
    ├── static/                           # Optional, for JS/CSS
    │   └── description/
    │       └── icon.png                  # Icon for the app (optional)
    │
    └── README.md                         # Module description (optional but recommended)

Configuration : 
Define Lead Sources.
1 ] Go to CRM → Configuration → Lead Sources to add or modify sources (e.g., "Google Ads", "Facebook", "Referral").

Use in CRM
1 ] When creating a new lead, select the appropriate Source from the dropdown.

Usage :

1. Creating a Lead with Source
Open CRM → Click "Create" (or use the quick-create form).
Fill in lead details and select a source (e.g., "Website Form").

2. Reporting & Analysis
Go to CRM → Reporting → Leads by Source to see which channels perform best.
Filter leads in the list view by Source for targeted follow-ups.

Dependencies :
Odoo CRM module (default in Odoo CE/EE).

Future Enhancements :
🔹 Automated Source Detection (e.g., UTM tracking from website forms).
🔹 Integration with Marketing Automation (e.g., linking sources to campaigns).

📌 Developed by Gaurav kapade
📅 Version: 1.0


