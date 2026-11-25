# Research and content brief: Agile in IT operations

- URL (unchanged): /project-management/agile/agile-operations-it/
- Brief date: 25 November 2026 (v2 framework; replaces the 8 November 2026 v1 brief, whose research is re-checked below)
- Article type: methodology guide with a how-to layer and a worked example
- Learning level: intermediate (assumes basic Agile and Kanban vocabulary; links to prerequisites)
- Language: en-GB

## Primary keyword
Agile IT operations

## Secondary keywords (17)
Agile in IT operations; Agile operations; AgileOps; Kanban for IT operations; Scrum vs Kanban for operations teams; Agile operations vs DevOps; Agile and ITIL; Agile ITSM; unplanned work in operations; interrupt-driven team; reserved capacity for unplanned work; classes of service for IT operations; DORA metrics; failed deployment recovery time; error budget; toil reduction; blameless post-incident review.

## Search intent
Primary: methodology / how-to ("how do I make an ops team work in an Agile way?"). Secondary: definition (what is AgileOps), comparison (Agile ops vs DevOps vs ITIL). The definition must appear in the first H2; the practical answer (Kanban + reserved capacity + explicit interrupt policy + automation, coexisting with ITSM) must be clear in the intro.

## Audience
Infrastructure, platform, network, database, service desk and security operations leads; IT managers asked to "go Agile"; Scrum Masters, delivery leads and project managers supporting ops teams; ITSM practitioners combining ITIL with Agile and DevOps.

## Inventory and duplicate check (framework §30)
- Live page (about 1,250 words incl. FAQ): accurate core ideas (work-type table, Kanban, reserved capacity, stand-ups, metrics table, mistakes, 11 FAQs). Problems: worked example uses unlabelled invented numbers; metrics use pre-2023 DORA names ("time to restore service"); "30–40% reserved capacity" stated without basis; no ITIL detail; no SRE; no calculations.
- Parent cluster: Agile guide (/project-management/agile/). Siblings: is-agile-only-for-software (broad, non-software use), how-to-implement-agile (organisation-wide rollout), agile-transformation.
- Overlaps: /project-management/kanban/kanban-swimlanes/ (classes of service, expedite lane rules: link, do not repeat the table); /project-management/kanban/wip-limits/ (Little's Law, how to set limits: link, use only a short Little's Law check); /project-management/kanban/devops/ (DevOps definition, CALMS; note that page still lists four DORA metrics with "time to restore service"; flagged as an unresolved site consistency issue, not edited); /project-management/kanban/kanban-ceremonies/ (cadences); /project-management/service-level-agreement-sla/ (SLA metrics, response/resolution time); /project-management/industries/it-project-management/ (IT projects, not operations).
- Differentiation: this page owns the operations-team view: work mix, interrupt policy, reserved capacity calculation, ITSM practice mapping, change enablement, SRE error budgets and toil, and a single consistent illustrative scenario.
- stats.py similarity results recorded in the record JSON after drafting.

## SERP findings (searched 25 November 2026; v1 SERP notes from 8 November re-used for context)
Results: InfoWorld (Sacolick, "3 steps to applying agile methodologies in IT operations", March 2020), DZone, Broadcom "Agile operations and the three ways", Wrike Agile guide, Atlassian Team Playbook "Agile for IT teams", McKinsey "Transforming IT infrastructure organizations using agile", PMI Disciplined Agile IT operations process blade, Budibase, Apress *Hands-On Guide to AgileOps*, HCLTech, Lucid.
Fetched: InfoWorld (mission/charter, product ownership, user stories, Kanban for small initiatives, tool integration; no metrics, no worked example, ITIL only in passing); Atlassian playbook (about 550 words of plays: stand-ups, retros, capacity planning, dependency mapping; no metrics, no ITIL); PMI Disciplined Agile IT operations practices (goals: run solutions, manage infrastructure, manage configurations, evolve infrastructure, mitigate disasters, govern IT operations).
Gaps we fill: no competitor sizes reserved capacity from data, maps ITSM practices to Agile mechanics, uses the current five DORA metrics, explains error budgets with arithmetic, or gives a labelled worked example with consistent numbers.

## Fact checks (primary sources)
- DORA (dora.dev/guides/dora-metrics/, updated 5 January 2026; history page): five software delivery metrics: change lead time, deployment frequency, failed deployment recovery time (throughput); change fail rate, deployment rework rate (instability). MTTR/time to restore was redefined as failed deployment recovery time in 2023; deployment rework rate added 2024; reliability is treated as operational performance, not a delivery metric.
- Google SRE book (sre.google): error budget = 1 − SLO, releases halted when exhausted (Embracing Risk); toil definition (manual, repetitive, automatable, tactical, no enduring value, scales linearly) and the 50% cap on operational work (Eliminating Toil).
- ITIL: PeopleCert "ITIL (Version 5) explained": phased release, ITIL 4 remains available; Global Knowledge FAQ: no ITIL 4 retirement date announced, at least 12 months of parallel running. ITSM.tools: ITIL 4 change enablement, standard/normal/emergency changes, change authority incl. peer review and automated pipeline approvals; "change control" was the original ITIL 4 Foundation term. AWS whitepaper quotes the ITIL 4 purpose of change enablement.
- Agile Manifesto values used for the translation table (agilemanifesto.org; already established on site).
- Site facts: Wrike #1 (9.4) with request forms and automation; Jira #6 (8.6); Jira Service Management is a separate service-desk product (per our Jira review).

## SEO
- Title (H1/SEO, 55 chars): Agile IT Operations: Kanban, ITIL and DevOps in Practice
- Meta description (≤155): Agile IT operations explained: run incidents, requests and improvements with Kanban, reserved capacity, ITIL and DevOps, with a worked example and metrics.

## Outline
- H2 What is Agile in IT operations? (40–60 word definition; scope; AgileOps; what it is not)
- H2 Why operations work needs a different kind of Agile (work-type table; why sprint commitments break)
- H2 Agile values translated for an operations team (table)
- H2 Kanban, Scrum or Scrumban for an operations team? (decision table by unplanned share)
- H2 Core practices for Agile operations teams (H3: one board; interrupt policy and classes of service; WIP limits; reserved capacity from data; cadences; automation and toil; blameless post-incident reviews)
- H2 Agile alongside ITIL and IT service management (practice mapping table; change enablement)
- H2 Agile operations, DevOps and SRE (error budget with calculation)
- H2 How to introduce Agile in an operations team, step by step (10 steps with timings)
- H2 Worked example: an infrastructure team moves to Kanban (illustrative; capacity, Little's Law, automation payback, results, interpretation)
- H2 Metrics for Agile IT operations (flow, DORA five, service)
- H2 Roles in an Agile operations team
- H2 Tools and templates
- H2 When Agile operations practices are unsuitable or limited
- H2 Common mistakes (table)
- FAQ (11)

## Worked examples planned (one consistent illustrative scenario)
Six-person infrastructure team, 32 focus hours each per week (192 h). Eight weeks of unplanned effort: 78, 92, 85, 101, 88, 95, 70, 99 h → mean 88.5 h (46.1%); 50% reservation (96 h) covers 6 of 8 weeks. Little's Law: standard requests WIP 36, throughput 22.5/week → 1.6 weeks (8 working days); WIP 18 → 0.8 weeks (4 days). Automation of environment builds: 14/month × (3 − 0.25) h = 38.5 h/month saved; 60 h build → 1.56 months payback. Error budget: 99.9% monthly SLO over 30 days = 43.2 minutes; 25-minute incident uses 57.9%. Change fail rate 6/80 = 7.5%. Illustrative outcome after three months: unplanned mean 72 h (37.5%).

## Internal links planned
Kanban: what-is-kanban, kanban-boards, kanban-swimlanes, wip-limits, kanban-ceremonies, kanban-vs-scrum, kanban-vs-scrumban, cycle-time, throughput, kanban-metrics, devops, continuous-delivery, value-stream-mapping. Agile: agile-manifesto-values-and-principles, is-agile-only-for-software, how-to-implement-agile, agile-metrics-and-kpis, agile-capacity-planning. Scrum: sprint-retrospective, scrum-product-owner. Other: service-level-agreement-sla, change-management-vs-change-control. Templates: work-request-template, kanban-board-template, root-cause-analysis-template. Tools: wrike, jira, wrike-vs-jira.

## FAQs
What is Agile in IT operations? What is AgileOps? Is Scrum or Kanban better for IT operations? Can operations teams run sprints? How do Agile ops teams handle incidents? How much capacity should an ops team reserve? Can Agile and ITIL work together? Agile operations vs DevOps? What metrics? Do ops teams need a product owner? How long does it take?

## Sources to cite / record
dora.dev metrics and history; sre.google Embracing Risk and Eliminating Toil; peoplecert.org ITIL (Version 5) explained; Global Knowledge ITIL 5 FAQ; itsm.tools change enablement; AWS change enablement in ITIL 4; pmi.org Disciplined Agile IT operations; agilemanifesto.org (site-established).

## Course
Sprintcraft: Agile and Scrum Practitioner is on the page's PMAI box; no body mention planned.
