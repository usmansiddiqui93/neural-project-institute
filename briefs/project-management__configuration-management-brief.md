# Brief: /project-management/configuration-management/

Prepared 25 November 2026 under RW_BRIEF.md v2 and FRAMEWORK.md V1.0.

## Inventory and duplicate check (§30)
- Live page (2 Oct 2026, ~1,150 words): accurate outline. Keeps: four core activities plus planning, key terms table, register example, CM vs change control with CR-04 SSO, tips, FAQs (PRINCE2, software-only, responsibility). Weaknesses: no sources, no standards comparison, no audit types, no worked impact analysis or audit, no Agile/DevOps treatment, a "Configuration register template" heading although no such template exists on the site (fix: describe it as an example register, and point to real templates).
- Parent cluster: risk, quality and control; sits beside /project-management/change-control/, /project-management/change-management-vs-change-control/, /project-management/project-integration-management/, /project-management/project-baseline/.
- Overlap handling:
  - change-control owns the change request process and authority levels: link, do not repeat. Its CR-04 SSO example stays there; our example uses a new change (CR-07).
  - change-management-vs-change-control already says CM "makes sure the approved version of each item is the one everyone uses": we expand, not repeat.
  - project-baseline (rewritten in the same session) owns scope/schedule/cost baselines; this page covers configuration baselines (functional, allocated, product) and links back. Both pages share the illustrative housing association repairs system scenario and CR-07 so learners can follow one change through both disciplines; calculations differ.
  - kanban/devops and kanban/continuous-delivery own pipelines: link only.
- Templates read: change-request-template (change log + form; expert adds revision history), project-deliverables-template (ID, Deliverable, Description, Type, Owner, Due date, Acceptance criteria, Approver, Status; no version/location columns), business-requirements-document-template (requirement IDs, traceability, "baseline the approved BRD"). No configuration register template exists: do not imply one.

## Search intent
Primary: definition/methodology ("what is configuration management in project management"), with how-to sub-intent (activities, register, audit).

## Keywords
- Primary: configuration management in project management
- Secondary (17): configuration management; configuration item; configuration item record; configuration baseline; configuration management plan; configuration identification; configuration control; configuration status accounting; configuration audit; functional configuration audit; physical configuration audit; configuration management vs change control; version control vs configuration management; configuration control board; ISO 10007; configuration management in Agile; product status account.

## Audience and level
Intermediate: project managers, PMO staff and project support, engineers and BAs moving into PM, PRINCE2/PMP learners.

## SERP findings (WebSearch 25 Nov 2026; Wrike guide and DoF NI guidance opened)
- Wrike guide: five steps, car example, one-line Agile note. Gaps: no register fields, no metrics, no roles, no CM plan contents, no audit procedure.
- DoF NI guidance (updated Oct 2024): practical rules (single updater, check-out/check-in, roles).
- APM "what is configuration management": five activities, definition attributed to APM BoK 8th edition.
- Gaps we fill: cross-standard comparison table; CM vs change control vs version control vs ITIL service configuration management; configuration baselines vs project baselines; calculated worked example (status account, impact trace, release audit, traceability coverage); tailoring by project type; Agile/DevOps mechanisms.

## SEO
- Title (≤60): Configuration Management in Project Management Explained (54)
- Meta: see record.

## Outline
1. What is configuration management? (40–60 word definition; ISO 10007 and APM wording; what it is not)
2. Why projects need it (concrete failure modes)
3. Key terms (table)
4. The five activities (comparison table across ISO 10007:2017, APM, PMI Practice Standard 2007, NASA SE Handbook; H3 per activity)
5. Configuration audits: functional and physical
6. Configuration baselines versus project baselines
7. CM vs change control vs version control vs IT service configuration management (table)
8. Worked example: one change through the configuration (register excerpt, impact trace, status account, pre-release audit, traceability)
9. Who does configuration management
10. CM in Agile and DevOps
11. Scaling CM to the project (tailoring table)
12. Common mistakes; FAQs

## Internal links (planned, all in en_urls.txt)
change-control, change-management-vs-change-control, project-baseline, project-integration-management, project-management-plan, project-quality-management, project-requirements, work-breakdown-structure, project-deliverables, issue-log, project-closure, prince2, kanban/devops, kanban/continuous-delivery, agile/definition-of-done, scrum/increment-in-scrum, industries/engineering-project-management, industries/construction-project-management, project-management-office-pmo, lessons-learned; templates: change-request-template, project-deliverables-template, business-requirements-document-template.

## Worked example (illustrative)
Housing association repairs system replacement; CR-07 mobile app for repair operatives. Register of 46 CIs: status account 28/5/6/7 with percentages; CR-07 touches 6 existing CIs and creates 2 new (48 total); release R1.0 audit of 21 CIs, 19 match (90.5%); requirement trace 62/64 (96.9%). All verified in Python.

## Sources
- ISO 10007:2017 catalogue page (iso.org) and BSI preview (ANSI webstore): edition 3, confirmed 2023, revision under development; clause structure; definitions.
- APM "What is configuration management?" (apm.org.uk).
- PMI Lexicon v4.0 (2024): configuration management system, change control, CCB.
- PMI Practice Standard for Project Configuration Management (2007): O'Reilly listing (chapter structure only).
- NASA Systems Engineering Handbook 6.5: five elements, functional/allocated/product baselines.
- MIL-HDBK-61A section 8 (product-lifecycle-management.com mirror): FCA and PCA wording; DAU Adaptive Acquisition Framework PCA page.
- DoF NI programme and project configuration management guidance.
- SEBoK Configuration Management: CCB composition, pitfalls.
- Semantic Versioning 2.0.0 (semver.org).
- Knowledge Train PRINCE2 7 summaries (secondary).
