# Content Brief: WIP Limits in Kanban

URL (unchanged): `/project-management/kanban/wip-limits/`
Brief date: 4 November 2026

## Primary Keyword

WIP limits

(Page angle: a practical, numbers-first guide to setting, enforcing and tuning WIP limits on a Kanban board, for project managers and delivery teams. "Kanban WIP limits" and "how to set WIP limits" are the main supporting phrases.)

## Secondary Keywords

- what is a WIP limit / WIP limit meaning
- Kanban WIP limits
- how to set WIP limits / how to calculate WIP limits
- WIP limit example
- WIP limits and Little's Law
- types of WIP limits (per column, per person, per swimlane, CONWIP)
- CONWIP / constant work in progress
- WIP limit per person / personal WIP limit
- what happens when a WIP limit is reached
- WIP limits too high / too low
- WIP limits for blocked items
- WIP limits in Scrum / Scrumban WIP limits
- WIP limits in Jira / Azure Boards
- why limit work in progress / benefits of WIP limits
- stop starting, start finishing
- WIP limit template / Kanban board template with WIP limits
- WIP limits vs capacity

## Search Intent

Informational with a strong "how to" layer. Most searchers already know what a Kanban board is and want (a) a short definition, (b) a way to pick their first numbers and (c) what to do when a column fills up. A second group (Scrum and project teams, students) wants the theory: why WIP limits shorten delivery time (Little's Law). The page should answer the definition in the first sentence and then go further than competitors with a fully worked board example, a numerical Little's Law example, a multitasking example and a tuning table.

## Target Audience

- Kanban and Scrum teams (software, IT operations, marketing, creative, service desks)
- Project managers and delivery leads introducing Kanban practices
- Team leads whose people are juggling too many tasks at once
- Students and certification candidates (PMI-ACP, Kanban, PMAI) who need clear definitions

## SERP Research (WebSearch, 4 November 2026)

Top results for "WIP limits kanban": Adobe (Workfront) blog, GitScrum docs, Miro (two pages), Businessmap (ex-Kanbanize) "What is WIP", Superthread docs, GeeksforGeeks, AWS Builder post, Medium, LaunchNotes, Shortcut help, Microsoft Azure Boards docs, Kanban Tool, ClickUp blog, FourWeekMBA, DORA capability page, Scrum.org forum, Atlassian, Lucid, Planview. For "how to set WIP limits example": Superthread, Azure Boards docs, Rework, Scrum.org, Kanban Tool help, GitScrum, Uplevel, Welsh Government digital services course.

Pages fetched for structure (wording not reused):

1. **Atlassian (WIP limits)**: what they are; why they matter; using limits on agile teams (team decision after watching averages, limit below team size to leave room for pairing/review); anti-patterns (raising limits, hiding idleness, adding people); four goals (consistent task size, map limits to skills, reduce idleness, sustainable pace). No formula, no Little's Law worked example, no FAQ.
2. **Businessmap (What is WIP)**: definition; why use limits; how to set up (reviews, accept change, analyse flow, don't exceed); five ways to apply (per person, per team, CONWIP, activity-based, upstream); benefits; "WIP paradox" (too high vs too low); starting point of team size plus one. Vendor case studies, no FAQ.
3. **Rework (WIP limits with examples)**: Little's Law with a numeric example; five steps (capacity, current WIP, set slightly below, treat as conversation trigger, review every two weeks); a per-column reference table; mistakes (ignoring limits, same number everywhere, lowering too fast, forgetting blocked items).
4. **DORA (WIP limits capability)**: implementation (make work visible, limit per column, pull when space frees, don't raise limits when people are idle); pitfalls (invisible work, limits too high, relaxing when idle); measuring lead time and its variability; DORA research states that WIP limits help drive improvements in software delivery performance, especially when combined with visual displays and monitoring feedback.

Primary sources checked:
- **The Kanban Guide** (John Coleman and Daniel Vacanti, edition 2025.5, May 2025): WIP is "the number of work items started but not finished"; Kanban system members must explicitly control WIP between started and finished; four flow measures are WIP, throughput, work item age and cycle time. The guide talks about "controlling WIP" rather than prescribing column limits.
- **Kanban University glossary**: a WIP limit is a policy that constrains the amount of work allowed in a given part of the Kanban system.
- **Little's Law**: John D. C. Little, "A Proof for the Queuing Formula: L = λW", Operations Research, vol. 9, no. 3 (1961), pp. 383–387.

Common H2s across the SERP: what are WIP limits; why limit WIP / benefits; how to set WIP limits; types of WIP limits; what to do when the limit is reached; common mistakes; WIP limits in a tool.

People Also Ask / related questions:
- What is a good WIP limit?
- How do you calculate a WIP limit?
- What happens when a WIP limit is reached?
- Can a team break a WIP limit?
- Should blocked items count towards the WIP limit?
- Should the Done column have a WIP limit?
- Do WIP limits slow teams down?
- What is CONWIP?
- Can you set WIP limits per person?
- Does Scrum use WIP limits?
- What is the difference between a WIP limit and capacity?

Content gaps we can fill:
- A complete worked example: one illustrative board, current counts, people per stage, chosen limits and the reasoning for each.
- A numeric Little's Law example plus its assumptions (most pages give the formula without caveats).
- A multitasking example showing why finishing sequentially improves average completion time.
- A tuning table: symptom, likely cause, change to the limit.
- How to treat blocked items, expedite work, waiting ("Done") sub-columns and the Ready column.
- How to introduce limits to a sceptical team and stakeholders.
- WIP limits in Scrum and Scrumban, and in common tools, kept fair to every tool.

## SEO Title

WIP Limits in Kanban: How to Set Them, With Examples (52 characters)

## Meta Description

WIP limits explained: what they are, why they work (Little's Law), how to set your first limits step by step, worked board examples and common mistakes. (153 characters)

## Target Length

3,600–4,000 words (sections plus FAQ). Upper end of the 2,500–4,000 range at the owner's request.

# Outline

## H1: WIP Limits in Kanban: How to Set Them, With Examples

Intro: define WIP limit in the first sentence; say it is the practice that turns a board into a pull system; preview the worked examples.

## H2: What is a WIP limit?
- 40–60 word definition (snippet).
- WIP = started but not finished (Kanban Guide 2025.5); WIP limit = a policy (Kanban University glossary).
- Where limits are shown (column header), and that they create a pull signal.
- Link: what is Kanban, Kanban boards, pull vs push.

## H2: Why WIP limits work
- H3 Little's Law: formula, source, numeric example (24 items, 6/week → 4 weeks; 12 items → 2 weeks), assumptions table.
- H3 Less task switching: multitasking worked example (three 5-day jobs in parallel vs in sequence).
- H3 Bottlenecks become visible: link theory of constraints.
- H3 Other benefits: quality, predictability, sustainable pace. Attribute DORA finding.

## H2: Types of WIP limits
- Table: per column, per column group (CONWIP for a stage), per person, per swimlane/class of service, per work type, whole system CONWIP, upstream (Ready) limit.
- Note on which to start with.

## H2: How to set WIP limits step by step
- OL of 7 steps: define start/finish points; count today's WIP; note people per stage; choose starting limits (current minus a bit, or 1–1.5 per person); decide policies (blocked, expedite, breach); make visible; review after 2–4 weeks.
- TIP about avoiding a dramatic cut.

## H2: Worked example: setting limits on a team board
- Illustrative 6-person marketing/software team; table with column, people, current WIP, starting limit, reasoning.
- Doing/Done sub-columns explanation.
- Results after four weeks table (illustrative) and what the team changed.

## H2: What to do when a column hits its limit
- OL right-to-left process: look downstream, unblock, swarm, pair, help with review, improve, don't pull.
- H3 Blocked items; H3 Expedite and breaches (record them).

## H2: Tuning WIP limits over time
- Table: symptom → likely meaning → change.
- When to lower, when to raise; one change at a time; use CFD, cycle time, WIP aging.

## H2: Introducing WIP limits to a team and stakeholders
- Conversation points, start with an experiment, explain idle time, stakeholder side (replenishment).

## H2: WIP limits in Scrum, Scrumban and personal Kanban
- Sprint backlog as implicit limit; in-sprint column limits; Scrumban; personal Kanban (Jim Benson's personal Kanban emphasises limiting WIP).

## H2: Setting WIP limits in project management tools
- Tool-neutral: Jira column constraints, Azure Boards, ClickUp per review page; Trello via Power-Ups; in other tools put the number in the column name and track counts on a dashboard. Wrike for cross-team visibility. Link to tool reviews and Kanban board template.

## H2: Common WIP limit mistakes
- Bulleted list with fixes.

## FAQ (12–14)
1. What is a good WIP limit?
2. How do you calculate a WIP limit?
3. What does WIP stand for?
4. What happens when a WIP limit is reached?
5. Can a team break a WIP limit?
6. Should blocked items count towards the WIP limit?
7. Should the Done column have a WIP limit?
8. Do WIP limits slow teams down?
9. What is CONWIP?
10. Can you set WIP limits per person?
11. Does Scrum use WIP limits?
12. What is the difference between a WIP limit and capacity?
13. How often should you change WIP limits?

## Internal links (planned)

/project-management/kanban/what-is-kanban/, /project-management/kanban/kanban-boards/, /project-management/kanban/pull-system-vs-push-system/, /project-management/kanban/cycle-time/, /project-management/kanban/throughput/, /project-management/kanban/theory-of-constraints/, /project-management/kanban/kanban-swimlanes/, /project-management/agile/agile-swarming/, /project-management/kanban/cumulative-flow-diagram/, /project-management/kanban/wip-aging-chart/, /project-management/kanban/kanban-metrics/, /project-management/kanban/kanban-planning/, /project-management/kanban/kanban-ceremonies/, /project-management/kanban/personal-kanban/, /project-management/kanban/kanban-vs-scrumban/, /project-management/agile/what-is-a-sprint/, /project-management/kanban/flow-efficiency/, /project-management/kanban/kanban-principles/, /project-management-tools/jira/, /project-management-tools/clickup/, /project-management-tools/trello/, /project-management-tools/wrike/, /templates/kanban-board-template/, /templates/workflow-template/, /project-management/kanban/blocker-clustering/.

## Writer notes
- British spelling, second person, short paragraphs.
- Label all numerical scenarios as illustrative.
- No invented statistics or case studies; attribute the DORA finding to DORA.
- Do not claim specific tools lack WIP limits unless our review pages say so (Trello's review says it has none natively; ClickUp's review says it supports per-column limits).
