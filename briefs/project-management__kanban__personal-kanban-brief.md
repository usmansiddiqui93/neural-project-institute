# Content brief: Personal Kanban

URL (unchanged): `/project-management/kanban/personal-kanban/`
Brief date: 25 November 2026

## Inventory and duplicate check (framework §30)
- Live page: short (3-minute read): two rules, basic setup, useful additions, why it works, making it stick, 11 FAQs. Accurate; kept (two rules, Backlog/Doing/Done, WIP 2–3, weekly review, Waiting/Today columns, recurring tasks, students, families) and expanded. PMAI box names Wayfinder (kept; no course mention in body). Page also carries an inline to-do list template box and a templates box (to-do list, priority list, Kanban board).
- Parent cluster: `/project-management/kanban/` (Kanban basics).
- Prerequisites: `/project-management/kanban/what-is-kanban/`.
- Related: WIP limits, Kanban boards, Kanban cards, Kanban principles, pull vs push, cycle time, WIP aging chart, Kanban ceremonies, Kanban vs Scrum, managing multiple projects.
- Overlap: kanban-boards (team board design; one table row on a personal board; has a "Kanban board vs to-do list" section), wip-limits (Little's Law for teams), what-is-kanban. No other page targets "personal kanban". Differentiate by: individual WIP counting (incl. Waiting), personal board layouts for PMs and students, evidence-based limit adjustment table, a personal Little's Law and SLE example, weekly review, comparison with Eisenhower/GTD/time blocking (not repeated from kanban-boards). Link rather than repeat team Little's Law material.
- stats.py similarity after drafting: kanban-boards 0.568, what-is-kanban 0.563, wip-limits 0.557, agile-workflow 0.473, kanban-vs-agile 0.452. Moderate, driven by shared Kanban vocabulary; headings, examples and intent differ.
- Templates verified by reading their pages: `/templates/kanban-board-template/` (Board: Backlog, To do WIP 5, In progress WIP 3, Review WIP 2, Done; Cards: owner, class of service, column, started, finished, cycle time, blocked), `/templates/to-do-list-template/` (Done?, Task, Category, Priority, Due date, Estimated time, Status, Notes; weekly planner), `/templates/priority-list-template/` (importance and urgency 1–5, score, quadrant Do now/Schedule/Delegate/Drop).

## Primary keyword
personal kanban

## Secondary keywords
personal kanban board; personal kanban rules; two rules of personal kanban; personal kanban WIP limit; personal kanban columns; personal kanban example; personal kanban for project managers; personal kanban for students; personal kanban vs to-do list; personal kanban app; how to set up a personal kanban board; personal kanban weekly review; personal kanban Jim Benson; kanban for personal productivity; limit work in progress; visualise your work; Little's Law personal

## Search intent and level
How-to (set up and use a personal board), with definition intent first. Learning level: beginner. Audience: project coordinators and managers, knowledge workers, students, people new to Kanban.

## SERP findings (WebSearch 25 Nov 2026: "personal kanban"; "Personal Kanban Jim Benson ... two rules")
Top results: Wrike Kanban guide and blog, Smartsheet, Kanban Tool, Pluralsight, ProjectManager, Shortform book summary, Zenkit, Any.do, personalkanban.com primer, Lean Enterprise Institute (Lean Post), Nimblework, SessionLab, University of Washington HR.
Fetched and inspected: personalkanban.com "Building your first Personal Kanban" primer (Backlog/Doing/Done; whiteboard; arbitrary starting WIP such as no more than 5; pull); Lean Post (Drickhamer, 19 Nov 2015) on the book (two rules, Benson's origins, Shingo award, invisible knowledge work).
Gaps: competitors rarely explain what counts as WIP for an individual (waiting work), give no evidence-based way to adjust the limit, no numbers (Little's Law, percentiles) applied to a personal board, and little on project-manager-specific layouts.

## SEO
- Title/H1: Personal Kanban: The Two Rules, Board Setup and Examples (55 chars)
- Meta: Personal Kanban explained: the two rules, how to set up your board and WIP limit step by step, a worked Little's Law example, and how to make it stick. (151 chars)

## Outline
H2 What is personal Kanban? · H2 The two rules (H3 visualise; H3 limit WIP, Kanban Guide WIP definition) · H2 Why personal Kanban works (task switching per APA; Little's Law; visible problems) · H2 How to set up a personal Kanban board step by step (7 steps) · H2 Personal Kanban board examples (layout table; H3 project manager; H3 students) · H2 How to choose and adjust your WIP limit (evidence table) · H2 Worked example: measuring a personal board with Little's Law (illustrative; 4 steps incl. 85th percentile SLE and work item age) · H2 The weekly review · H2 Personal Kanban vs to-do lists and other methods · H2 Personal Kanban for teams and families · H2 Tools for personal Kanban · H2 Common personal Kanban mistakes · FAQ (12)

## Worked example and calculations
Illustrative project coordinator, 10 working days: average WIP 9, throughput 12 ÷ 10 = 1.2/day → cycle time 7.5 working days; after limits average WIP 4 → 3.3 working days (≈56% shorter) at unchanged throughput. Cycle-time sample of 20 cards → nearest-rank 85th percentile = 6 working days. All verified with Python.

## Internal links (planned)
/project-management/kanban/what-is-kanban/, /project-management/kanban/, /project-management/kanban/wip-limits/, /project-management/kanban/kanban-boards/, /project-management/kanban/kanban-cards/, /project-management/managing-multiple-projects/, /project-management/kanban/wip-aging-chart/, /project-management/kanban/cycle-time/, /project-management/kanban/kanban-ceremonies/, /templates/to-do-list-template/, /templates/priority-list-template/, /project-management/kanban/kanban-principles/, /project-management/kanban/kanban-vs-scrum/, /templates/kanban-board-template/, /project-management-tools/trello/, /project-management-tools/notion/, /project-management-tools/microsoft-planner/, /project-management/kanban/pull-system-vs-push-system/

## FAQs
What is personal Kanban? Two rules? Good WIP limit? Columns? vs to-do list? Do waiting tasks count? Review frequency? Recurring tasks? Best app? Students? Procrastination? Same as the Kanban Method?

## Sources to cite
- Benson, J. and DeMaria Barry, T. (2011) Personal Kanban: Mapping Work | Navigating Life — book not inspected; facts taken from the Lean Post article and the site's existing page.
- Drickhamer, D. (19 Nov 2015) Lean Enterprise Institute, "Personal Kanban: You can't manage what you can't see" — inspected.
- personalkanban.com primer "Building your first Personal Kanban" — inspected (author/date not shown).
- Coleman, J. and Vacanti, D. The Kanban Guide, edition 2025.5 (1 May 2025) — inspected (definition, WIP, four measures, SLE).
- American Psychological Association, "Multitasking: switching costs" (2006) — inspected (Rubinstein, Meyer and Evans 2001 findings).
- Little's Law: as presented on the site's WIP limits guide (Little 1961).

## Writer notes
No official personal WIP limit exists; present numbers as starting hypotheses. Do not use the APA page's "40 percent" remark (an attributed remark, not a measured result). Tool claims match review pages (Trello 7.8 best for simple Kanban boards, free plan up to 10 collaborators per Workspace; Notion 8.0; Planner basic included in Microsoft 365). Wrike not forced into a personal-productivity context.
