from frappe import _

def get_data():
    return [
        {
            "label": _("Sales"),
            "icon": "fa fa-money",
            "items": [
                {
                    "type": "doctype",
                    "name": "Lead",
                    "description": _("Potential customers."),
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Opportunity",
                    "description": _("Potential business opportunities."),
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Contact",
                    "description": _("Contact details of customers."),
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Company",
                    "description": _("Company information."),
                    "onboard": 1,
                },
            ]
        },
        {
            "label": _("Activities"),
            "icon": "fa fa-calendar",
            "items": [
                {
                    "type": "doctype",
                    "name": "Activity",
                    "description": _("Calls, meetings, emails, etc."),
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Note",
                    "description": _("Notes and comments."),
                },
                {
                    "type": "doctype",
                    "name": "Document",
                    "description": _("Attachments and files."),
                },
            ]
        },
        {
            "label": _("Setup"),
            "icon": "fa fa-cog",
            "items": [
                {
                    "type": "doctype",
                    "name": "Lead Source",
                    "description": _("Sources of leads."),
                },
                {
                    "type": "doctype",
                    "name": "Industry",
                    "description": _("Industry categories."),
                },
                {
                    "type": "doctype",
                    "name": "Opportunity Stage",
                    "description": _("Stages in the sales pipeline."),
                },
                {
                    "type": "doctype",
                    "name": "Tag",
                    "description": _("Tags for categorization."),
                },
            ]
        },
        {
            "label": _("Reports"),
            "icon": "fa fa-list",
            "items": [
                {
                    "type": "report",
                    "name": "Lead Analysis",
                    "doctype": "Lead",
                    "is_query_report": True,
                },
                {
                    "type": "report",
                    "name": "Sales Pipeline",
                    "doctype": "Opportunity",
                    "is_query_report": True,
                },
                {
                    "type": "report",
                    "name": "Activity Summary",
                    "doctype": "Activity",
                    "is_query_report": True,
                },
            ]
        }
    ]
