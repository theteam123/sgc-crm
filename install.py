import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_install():
    """
    Setup basic configuration after app installation
    """
    create_default_lead_sources()
    create_default_opportunity_stages()
    create_default_industries()
    create_default_tags()
    
def create_default_lead_sources():
    """
    Create default lead sources
    """
    lead_sources = [
        {"source_name": "Website", "description": "Leads generated from the company website"},
        {"source_name": "Referral", "description": "Leads referred by existing customers or partners"},
        {"source_name": "Cold Call", "description": "Leads generated from cold calling"},
        {"source_name": "Exhibition", "description": "Leads from trade shows and exhibitions"},
        {"source_name": "Social Media", "description": "Leads from social media platforms"},
        {"source_name": "Email Campaign", "description": "Leads from email marketing campaigns"},
        {"source_name": "Google Search", "description": "Leads from organic search"},
        {"source_name": "Paid Advertising", "description": "Leads from paid advertising"}
    ]
    
    for source in lead_sources:
        if not frappe.db.exists("Lead Source", source["source_name"]):
            doc = frappe.new_doc("Lead Source")
            doc.source_name = source["source_name"]
            doc.description = source["description"]
            doc.insert(ignore_permissions=True)
    
    frappe.db.commit()

def create_default_opportunity_stages():
    """
    Create default opportunity stages
    """
    stages = [
        {"stage_name": "Qualification", "stage_order": 1, "default_probability": 10, "color": "#FFC107"},
        {"stage_name": "Needs Analysis", "stage_order": 2, "default_probability": 25, "color": "#FF9800"},
        {"stage_name": "Value Proposition", "stage_order": 3, "default_probability": 40, "color": "#FF5722"},
        {"stage_name": "Proposal", "stage_order": 4, "default_probability": 60, "color": "#8BC34A"},
        {"stage_name": "Negotiation", "stage_order": 5, "default_probability": 75, "color": "#03A9F4"},
        {"stage_name": "Closed Won", "stage_order": 6, "default_probability": 100, "color": "#4CAF50"},
        {"stage_name": "Closed Lost", "stage_order": 7, "default_probability": 0, "color": "#F44336"}
    ]
    
    for stage in stages:
        if not frappe.db.exists("Opportunity Stage", stage["stage_name"]):
            doc = frappe.new_doc("Opportunity Stage")
            doc.stage_name = stage["stage_name"]
            doc.stage_order = stage["stage_order"]
            doc.default_probability = stage["default_probability"]
            doc.color = stage["color"]
            doc.insert(ignore_permissions=True)
    
    frappe.db.commit()

def create_default_industries():
    """
    Create default industries
    """
    industries = [
        {"industry_name": "Agriculture", "description": "Farming, forestry, and related activities"},
        {"industry_name": "Manufacturing", "description": "Production of goods"},
        {"industry_name": "Construction", "description": "Building and infrastructure development"},
        {"industry_name": "Retail", "description": "Sale of goods to consumers"},
        {"industry_name": "Transportation", "description": "Movement of goods and people"},
        {"industry_name": "Information Technology", "description": "Software, hardware, and IT services"},
        {"industry_name": "Finance", "description": "Banking, insurance, and financial services"},
        {"industry_name": "Healthcare", "description": "Medical services and healthcare products"},
        {"industry_name": "Education", "description": "Schools, universities, and educational services"},
        {"industry_name": "Professional Services", "description": "Legal, accounting, consulting services"}
    ]
    
    for industry in industries:
        if not frappe.db.exists("Industry", industry["industry_name"]):
            doc = frappe.new_doc("Industry")
            doc.industry_name = industry["industry_name"]
            doc.description = industry["description"]
            doc.insert(ignore_permissions=True)
    
    frappe.db.commit()

def create_default_tags():
    """
    Create default tags
    """
    tags = [
        {"tag_name": "High Priority", "color": "#FF5722"},
        {"tag_name": "Follow Up", "color": "#2196F3"},
        {"tag_name": "New Client", "color": "#4CAF50"},
        {"tag_name": "VIP", "color": "#9C27B0"},
        {"tag_name": "Urgent", "color": "#F44336"}
    ]
    
    for tag in tags:
        if not frappe.db.exists("Tag", tag["tag_name"]):
            doc = frappe.new_doc("Tag")
            doc.tag_name = tag["tag_name"]
            doc.color = tag["color"]
            doc.insert(ignore_permissions=True)
    
    frappe.db.commit()
