# Content brief: Agile team structures

URL (unchanged): `/project-management/agile/agile-team-structures/`
Brief date: 25 November 2026 (framework V1.0, writer brief v2)

## Inventory and duplicate check (framework §30)
- Live page (published 7 September 2026, about 1,400 words incl. boilerplate): "what makes a team Agile" list, structure table (feature, component, generalist, specialist, hybrid T-shaped, platform), roles table, 7-step design list, a short online-retailer example (four component teams of six → three journey-aligned feature teams plus a platform team of six), structures-at-scale list, 11 FAQs. Accurate but thin; the example has no numbers to show why the change helps. Kept and extended; the retailer scenario is preserved and quantified. PMAI box names Sprintcraft (kept; no course mention in body).
- Parent cluster: `/project-management/agile/` (Agile roles and teams).
- Prerequisite: `/project-management/agile/what-is-an-agile-team/` — this is the single-team guide (characteristics, roles, who decides what, size table with n(n−1)/2, feature vs component in one paragraph, Team Topologies types in a list, teams of teams in one paragraph, build-a-team steps, insurer worked example with a skills matrix). **Do not repeat** the size table, roles table, build-a-team steps or skills-matrix example; link to them.
- Sibling: `/project-management/agile/squads-tribes-chapters-guilds/` — the Spotify model in depth (chapter-lead load formula, 61-person reorganisation). **Do not repeat**; mention the chapter option in one row and link.
- Differentiation: this page is about **organisation design across teams**: where to draw team boundaries, team composition patterns, interaction modes between teams, line-management options, multi-team structures, and how to choose and test a structure with a dependency count. Intent: "agile team structure(s)", "types of agile teams", "how to structure agile teams", "feature vs component teams".
- Related / advanced: LeSS, SAFe, Agile Release Train, Scrum@Scale, Scrum of Scrums, Agile transformation, Agile PMO, how to manage Agile teams, value stream mapping, Agile project manager, Scrum team roles, agile swarming (T-shaped skills enable swarming).
- Templates verified by reading their pages: `/templates/skills-matrix-template/` (people × skills, 0–4 scale, key-person risk), `/templates/raci-matrix-template/` (tasks × roles, one A per row), `/templates/communication-plan-template/` (exists; listed on live page).

## Primary keyword
agile team structure

## Secondary keywords
agile team structures; types of agile teams; how to structure agile teams; feature teams vs component teams; stream-aligned team; platform team; enabling team; complicated subsystem team; team topologies interaction modes; T-shaped team; generalising specialist; cross-functional team structure; Conway's law; inverse Conway manoeuvre; agile organisational structure; agile team reporting structure; scaling agile team structures; team cognitive load; dependency between agile teams

## Search intent and level
Primary: methodology/how-to (which structures exist and how to choose one). Secondary: comparison (feature vs component; team types). Learning level: intermediate. Audience: delivery and engineering managers, Agile coaches, project and programme managers moving to product teams, PMO and HR leads, Scrum Masters, students.

## SERP findings (WebSearch 25 Nov 2026: "agile team structures types feature component team how to choose"; Team Topologies; LeSS feature teams; Conway's law)
Top results: Mountain Goat Software "Agile team structure" (updated 31 July 2026), PMI Disciplined Agile "How do we organize a large agile team?", TechTarget "common types of Agile teams", LeSS "Feature Teams", Xebia "5 ways to organize agile teams", Atlassian/others.
Fetched: Mountain Goat (prefer feature teams; component teams sparingly with six conditions; "20% on five teams"; primary team clear; do not reorganise constantly), Disciplined Agile (component, feature, functional, internal open source; can be combined), LeSS (feature team definition and characteristics; component-team disadvantages; hybrid caution), Team Topologies key concepts, Fowler bliki on Team Topologies (2019 book; cognitive load) and Conway's law (1968 quote; inverse Conway manoeuvre coined by LeRoy and Simons 2010), SAFe "Features and Components" (most teams stream-aligned; 1–3 complicated-subsystem teams per ART; 2–3 enabling teams across enterprise; updated 17 April 2023).
Gaps: almost no page shows how to **test** a candidate structure against real upcoming work; line-management options are rarely covered; interaction modes seldom connected to choosing structure; no worked numbers.

## SEO
- Title/H1: Agile Team Structures: Types, Examples and How to Choose (56 chars)
- Meta: Agile team structures compared: feature, component, platform and enabling teams, how teams interact, reporting lines, scaling, and a worked redesign. (152 chars)

## Outline
- H2 What is an Agile team structure? (definition; three design decisions)
- H2 Why team structure matters (Conway's law; dependencies and queues; cognitive load; stability)
- H2 Ways to draw team boundaries (table) / H3 Feature teams and component teams / H3 How SAFe applies the four team types
- H2 Team composition: generalists, specialists and T-shaped people (H3 Shared specialists)
- H2 How teams work with each other (interaction modes table)
- H2 Line management and reporting lines (table)
- H2 Structures for several teams on one product (table: multiple Scrum Teams, LeSS, LeSS Huge, SAFe ART, Scrum@Scale, Spotify)
- H2 How to choose a structure (decision table)
- H2 How to design your team structure, step by step
- H2 Worked example: redesigning an online retailer's teams (illustrative; dependency count; composition; handoff wait; interpretation; limitations)
- H2 Changing structure without losing momentum
- H2 How to tell whether your structure is working (metrics)
- H2 Common team-structure mistakes
- FAQ (10)

## Planned worked example and calculations
Keep live scenario: 24 people in four component teams of six (web front end, mobile, checkout services, database) → three journey-aligned feature teams (Browse, Buy, Account) of six plus a platform team of six. Take ten upcoming features, mark components each touches; count teams per feature, single-team features, handoffs (teams − 1), and expected waiting at an assumed 5 working days per handoff. Check demand per journey and component; allocate the 24 people by skill and confirm totals. All verified in Python.

## Internal links (planned)
/project-management/agile/what-is-an-agile-team/, /project-management/agile/squads-tribes-chapters-guilds/, /project-management/scrum/scrum-team-roles/, /project-management/kanban/value-stream-mapping/, /project-management/agile/large-scale-scrum-less/, /project-management/agile/agile-release-train/, /project-management/agile/scaled-agile-framework-safe/, /project-management/scrum/scrum-at-scale/, /project-management/scrum/scrum-of-scrums/, /project-management/agile/agile-project-manager/, /project-management/agile/how-to-manage-agile-teams/, /project-management/agile/agile-transformation/, /project-management/agile/agile-swarming/, /project-management/kanban/devops/, /project-management/kanban/cycle-time/, /project-management/agile/agile-metrics-and-kpis/, /project-management/scrum/product-backlog/, /project-management/scrum/scrum-product-owner/, /templates/skills-matrix-template/, /templates/raci-matrix-template/

## FAQs
What is the best Agile team structure? What are the main types of Agile teams? Feature teams or component teams? What is a stream-aligned team? What is a platform team? What is Conway's law? Who do Agile team members report to? Does an Agile team structure need a project manager? How often should you change team structure? How many teams before you need a scaling framework?

## Sources to cite
- Schwaber & Sutherland, The Scrum Guide (November 2020) — inspected.
- Team Topologies key concepts (teamtopologies.com) — inspected; Fowler, "Team Topologies" bliki (25 July 2023) — inspected.
- Fowler, "Conway's Law" bliki (20 Oct 2022) quoting Conway (Datamation, 1968) — inspected (original paper not inspected).
- LeSS, "Feature Teams" (less.works) — inspected.
- PMI Disciplined Agile, "How do we organize a large agile team?" — inspected.
- SAFe, "Features and Components" (updated 17 April 2023) — inspected.
- Mountain Goat Software, "Agile Team Structure" (updated 31 July 2026) — inspected.
