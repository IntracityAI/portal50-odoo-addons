# Portal50 - Odoo Multitenant Addons

Portal50 is a multi-tenant business operating platform built on:
- Odoo Enterprise (ERP core)
- Portal50 custom addons
- Portal frontend (Squarespace + custom portal)
- Sage50 Accounting Bridge

This repository contains all custom Odoo addons used for Portal50.

## 📁 Repository Structure

addons/
  Independent Odoo addon modules.
  Each business feature = one addon.

docs/
  Business requirements, flowcharts, API docs.

scripts/
  Helper scripts for installation, backups, and deployment.

## 🧩 Development Rules

1. One feature = One Odoo addon.
2. No mixing of functions across addon modules.
3. External developers MUST submit Pull Requests.
4. All code MUST pass installation test.
5. All addons MUST contain:
   - __manifest__.py
   - models/
   - controllers/ (if needed)
   - views/
   - security/ir.model.access.csv

## 🛠️ Branch Strategy

main    = stable production  
dev     = active development  
feature/* = outsourced tasks  

## 📝 How to Work with External Developers (Outsourcing)

1. Each task is posted as a GitHub Issue.
2. Developer forks repository.
3. Developer submits PR to branch feature/task-id.
4. Owner reviews.
5. Approved PR → merged to dev.
6. All modules are tested before going to main.

---
