{
    'name': 'CRM Custom Features',
    'version': '1.1',
    'summary': 'Custom modifications for CRM leads with permanent view changes',
    'description': """
        Implements two features with permanent view modifications:
        1. Automatic lead source detection from email domain
        2. Moves source field above expected revenue in lead form
        3. Ensures changes persist through upgrades/updates
    """,
    'category': 'CRM',
    'author': 'Gaurav',
    'website': 'https://www.yourcompany.com',
    'depends': ['crm'],
    'data': [
    'security/ir.model.access.csv',
    'views/crm_lead_views.xml',
    'views/crm_lead_filter.xml',
    'views/lead_generation_wizard_view.xml' 
    ],
    'post_init_hook': '_post_install_override',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'crm_custom_features/static/src/css/crm_style.css',
        ],
    }
}