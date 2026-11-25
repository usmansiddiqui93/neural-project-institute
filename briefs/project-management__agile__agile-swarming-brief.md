# Content brief: Agile swarming

URL (unchanged): `/project-management/agile/agile-swarming/`
Brief date: 25 November 2026 (framework V1.0, writer brief v2)

## Inventory and duplicate check (framework §30)
- Live page (published 17 September 2026, about 1,000 words incl. boilerplate): short definition, why it works, when to swarm, how to start, pairing/swarming/mobbing table, three pitfalls, 12 FAQs. Content is broadly accurate and is kept, but thin: no source for the practice, no mechanism beyond "reduces WIP", no worked example, no decision rules on when not to swarm or how many people to use, and "Mobbing: the whole team" vs "Swarming: several people" is presented as a hard rule. PMAI box names Sprintcraft (kept; no course mention in body).
- Parent cluster: `/project-management/agile/` (Agile practices); also strongly tied to the Kanban flow cluster.
- Prerequisites: `/project-management/agile/what-is-an-agile-team/`, `/project-management/scrum/sprint-backlog/`, `/project-management/kanban/wip-limits/`.
- Related: `/project-management/scrum/scrum-techniques/` (has a 1-paragraph swarming entry and a pair/mob entry; link, do not repeat), `/project-management/kanban/flow-efficiency/` ("swarm on the oldest items"), `/project-management/kanban/theory-of-constraints/` (swarming exploits the constraint), `/project-management/kanban/wip-limits/` (holds the Little's Law derivation; reuse the formula, do not repeat its example), `/project-management/kanban/kanban-swimlanes/` (expedite lane), `/project-management/agile/agile-operations-it/` (incident swarming), `/project-management/agile/how-to-manage-agile-teams/`, `/project-management/agile/agile-team-structures/` (T-shaped composition).
- Overlap: no other URL targets "agile swarming". Glossaries define it in one line. scrum-techniques covers it in one paragraph and links here. Keep this page as the canonical, deep treatment.
- Templates verified by reading their pages: `/templates/kanban-board-template/` (Board tab: Backlog, To do WIP 5, In progress WIP 3, Review WIP 2, Done; Cards tab: Card, Owner, Class of service, Column, Started, Finished, Cycle time (days), Blocked?), `/templates/skills-matrix-template/` (people × skills, 0–4 scale), `/templates/sprint-planning-template/` (Sprint plan + Capacity tab with focus factor).

## Primary keyword
agile swarming

## Secondary keywords
swarming in agile; what is swarming in scrum; swarming vs mobbing; swarming vs pair programming; mob programming; ensemble programming; when to swarm; swarming kanban; swarming WIP limits; story swarming; incident swarming; intelligent swarming; swarming benefits; swarming disadvantages; how many people should swarm; remote swarming; one-piece continuous flow; walk the board

## Search intent and level
Primary: definition + how-to (what is swarming, when and how to do it). Secondary: comparison (swarming vs pairing/mobbing) and troubleshooting (why it does not stick). Learning level: beginner to intermediate. Audience: Scrum Masters, Developers, team leads, Kanban practitioners, project managers coaching delivery teams, students.

## SERP findings (WebSearch 25 Nov 2026: "agile swarming what is swarming scrum team"; Scrum patterns; Intelligent Swarming)
Top results: Wrike blog (2021, updated 2026), TechTarget (Hoffman, Dec 2020), Nulab/Backlog, InfoQ (Linders, Feb 2013), Agile Academy dictionary, Medium posts.
Fetched: Wrike (definition, IT-failure example, pros/cons; no comparison with mobbing, no numbers), TechTarget (practices, pairing/mobbing contrast; no metrics or worked example), InfoQ 2013 (quotes from D'Amico, Bernstein, Derkatch).
Gaps: no source for where swarming comes from; no explanation via Little's Law; nobody shows the cost side (coordination loss, lower throughput when items are not split well); no decision rule for swarm size; "intelligent swarming" (support) and incident swarming conflated or ignored; no measurement guidance.

## SEO
- Title/H1: Agile Swarming: What It Is, When to Swarm and How (49 chars)
- Meta: Agile swarming explained: how it works, when to swarm and when not to, swarming vs pairing and mobbing, a worked Sprint example and common mistakes. (149 chars)

## Outline
- H2 What is agile swarming? (definition; origin: Scrum Patterns ¶25; what the Scrum Guide and Kanban Guide do and do not say)
- H2 Why swarming works (Little's Law; Sprint risk; handoffs; knowledge spread) + table of mechanisms
- H2 Swarming vs pairing, mobbing and intelligent swarming (table incl. incident swarming)
- H2 When to swarm and when not to (decision table)
- H2 How to swarm, step by step (OL) / H3 How many people should swarm on one item / H3 A Daily Scrum that encourages swarming
- H2 Worked example: the same Sprint planned three ways (illustrative; formula D = E ÷ s(k); table; 30% overrun; handoff variant; interpretation; limitations)
- H2 Swarming in Kanban
- H2 Swarming with remote and hybrid teams
- H2 How to tell whether swarming is helping (metrics table)
- H2 Who does what (Developers, Scrum Master, Product Owner, managers)
- H2 Common swarming mistakes
- FAQ (8–10)

## Planned worked example and calculations
Illustrative team of six Developers, two-week (10 working-day) Sprint, six Sprint Backlog items of 8 person-days each. Policies: one item per person; three swarms of two; two swarms of three. Assumed speed-up s(1)=1, s(2)=1.8, s(3)=2.4 (stated as assumptions). Compute item duration, completion days, average cycle time, items Done by day 5 and day 10, throughput and a Little's Law cross-check; then a uniform 30% overrun (10.4 person-days). Variant: solo items wait 1.5 days for review/test. All verified in Python.

## Internal links (planned)
/project-management/agile/what-is-an-agile-team/, /project-management/agile/agile-team-structures/, /project-management/scrum/sprint-backlog/, /project-management/scrum/daily-scrum/, /project-management/scrum/sprint-planning/, /project-management/agile/definition-of-done/, /project-management/kanban/wip-limits/, /project-management/kanban/cycle-time/, /project-management/kanban/throughput/, /project-management/kanban/wip-aging-chart/, /project-management/kanban/flow-efficiency/, /project-management/kanban/theory-of-constraints/, /project-management/kanban/kanban-swimlanes/, /project-management/kanban/kanban-boards/, /project-management/scrum/scrum-techniques/, /project-management/agile/agile-operations-it/, /project-management/agile/how-to-manage-agile-teams/, /project-management/scrum/sprint-retrospective/, /project-management/agile/scrum-master-role/, /templates/kanban-board-template/, /templates/skills-matrix-template/

## FAQs
What is swarming in Agile? Is swarming part of Scrum? Swarming vs mobbing? Swarming vs pair programming? How many people should swarm? Does swarming reduce productivity? When should a team not swarm? Does swarming work remotely? What is intelligent swarming? How do WIP limits relate to swarming?

## Sources to cite
- Schwaber & Sutherland, The Scrum Guide (November 2020) — inspected.
- Coleman & Vacanti, The Kanban Guide, edition 2025.5 (May 2025) — inspected (PDF).
- Scrum Patterns Group, patlet ¶25 "Swarming: One-Piece Continuous Flow" (scrumplop.org); A Scrum Book (Sutherland & Coplien, Pragmatic Bookshelf, 2019) — patlet inspected; book chapter only partially visible.
- Woody Zuill, Mob Programming: A Whole Team Approach, Agile2014 experience report (Agile Alliance) — inspected.
- Consortium for Service Innovation, Intelligent Swarming — inspected.
- Linders, How Swarming Helps Agile Teams to Deliver, InfoQ (28 Feb 2013) — inspected.
- Little's Law: as already presented on /project-management/kanban/wip-limits/ (Little 1961; original not re-inspected).
