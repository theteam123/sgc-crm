# SGC CRM

Customer Relationship Management for SGC

## Overview

SGC CRM is a comprehensive customer relationship management system built on the Frappe framework. It provides tools for managing leads, opportunities, contacts, companies, and activities to streamline your sales process.

## Features

- **Lead Management**: Track and manage potential customers
- **Opportunity Management**: Monitor sales opportunities through various stages
- **Contact Management**: Maintain detailed contact information
- **Company Management**: Store comprehensive company information
- **Activity Tracking**: Log calls, meetings, emails, and other interactions
- **Document Management**: Store and organize files related to leads and opportunities
- **Notes**: Keep detailed notes on interactions and important information
- **Tagging System**: Categorize and organize records with tags

## Installation

### Prerequisites

- Frappe Bench environment
- ERPNext (recommended)

### Steps

1. Navigate to your bench folder
   ```
   cd frappe-bench
   ```

2. Get the app from GitHub
   ```
   bench get-app sgc_crm https://github.com/sgc/sgc_crm
   ```

3. Install the app on your site
   ```
   bench --site your-site.local install-app sgc_crm
   ```

4. Migrate the database
   ```
   bench --site your-site.local migrate
   ```

## Configuration

After installation, you can configure the CRM by:

1. Setting up Lead Sources
2. Configuring Industry categories
3. Defining Opportunity Stages
4. Creating Tags for categorization

## Usage

Access the CRM from the desk by clicking on the SGC CRM module icon. From there, you can:

- Create and manage leads
- Convert leads to opportunities
- Track opportunities through the sales pipeline
- Manage contacts and companies
- Log activities and schedule follow-ups
- Attach documents and files
- Add notes and tags

## License

MIT
