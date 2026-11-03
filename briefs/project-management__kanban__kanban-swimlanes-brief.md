# Content Brief: Kanban Swimlanes

URL (unchanged): `/project-management/kanban/kanban-swimlanes/`
Brief date: 4 November 2026

## Primary Keyword

kanban swimlanes

(Page angle: a practical design guide for teams using Kanban boards: what swimlanes are, which type to choose, how they work with classes of service and WIP limits, how to set them up step by step, and how to measure flow by lane.)

## Secondary Keywords

- what is a kanban swimlane / swimlane kanban board
- kanban swimlanes examples
- types of kanban swimlanes
- kanban swimlanes vs columns
- expedite swimlane / expedite lane
- classes of service kanban (expedite, fixed date, standard, intangible)
- kanban swimlanes WIP limits / WIP limits per swimlane
- how to set up swimlanes on a kanban board
- how many swimlanes should a kanban board have
- swimlanes by team / by person / by project / by work type / by priority
- kanban swimlanes best practices
- kanban swimlane policies
- kanban swimlanes in Jira / Trello / Asana / Wrike
- swimlane diagram vs kanban swimlane
- kanban board template with swimlanes

## Search Intent

Informational with a practical "how to set it up" layer. Most searchers already have a Kanban board and want to know whether, and how, to add horizontal lanes. They want a definition, the common lane types with examples, how many lanes to use and how WIP limits work across lanes. A smaller group is checking how a specific tool handles swimlanes. The page should define swimlanes in the first sentence, then go deeper than competitors with classes of service treated as policies (not just labels), worked WIP arithmetic across lanes, a full worked board design, step-by-step setup, flow metrics per lane, and tool notes that match our tool reviews.

## Target Audience

- Kanban and Agile teams (software, IT operations, service desks, marketing, creative)
- Team leads and delivery managers redesigning a board
- Project managers running a Kanban board for a project or programme
- Scrum teams adding Kanban practices
- Students preparing for Kanban or PMI-ACP style exams who need clear definitions

## SERP Research (WebSearch, 4 November 2026)

Top results for "kanban swimlanes": DevSamurai docs, Kanban Tool, TopLeft, Leantime, Jotform, ONES, Virto, ProjectWizards, Planview blog, Asana forum, ClickUp feature page, Businessmap (Kanbanize), Nave, Zenkit, Kanban Zone, Blue Cat Reports, Quire, TechRepublic (Trello). For "classes of service": Kanban University glossary, Kanban Zone, Scrum.org blog, Businessmap. Microsoft Learn (Azure Boards expedite swimlanes) ranks for the expedite-lane query.

Pages fetched for structure (wording not reused):

1. **Businessmap (Kanban swimlanes)**: definition; what lanes are for (procurement example with per-lane WIP limits fitting inside the column limit); types (individuals/teams/clients, repetitive tasks, classes of service with four H4s, discarded options, company-level/portfolio lanes); product section; no FAQ.
2. **Nave (Kanban swimlanes)**: definition; categories (team/individual, feature, recurring tasks, priority-based); WIP limit per lane example (column limit 6 split 3/3); Trello workaround with labels; when to implement; warning that sequential steps belong in columns, not lanes.
3. **Leantime (Kanban swimlanes)**: definition; six types (priority, team member, project, client, work type, expedite lane limited to one); five-step setup; best practices and mistakes (too many lanes, lanes for status, empty lanes); tool comparison; FAQ (what is a swimlane, Trello, how many lanes, lanes vs columns, free tools).

Also checked: Kanban University's Official Kanban Guide glossary (definitions of class of service and the expedite, fixed date, standard and intangible archetypes; boards "use horizontal swimlanes to further enhance the visualization of policies, types of work, classes of service"); Scrum.org blog on classes of service (the Kanban Guide does not require them; some practitioners prefer breaching WIP by exception over a permanent expedite lane); Microsoft Learn (Azure Boards: default lane cannot be deleted, up to 50 swimlanes, swimlane rules); Asana community announcement (swimlanes on Board view launched July 2025 on Starter, Advanced, Enterprise and Enterprise+, grouping by sections, assignees or single-select custom fields); Wrike community (Board view can group horizontal swimlanes and columns by single- or multi-select custom fields); ClickUp feature page (swimlanes on Board view). Our Jira review: swimlanes by assignee, epic or priority; our Trello review: no native swimlanes on the base board.

Common H2s: what are swimlanes; types; classes of service; WIP limits per lane; how to set up; best practices/mistakes; tool support; FAQ.

People Also Ask / related questions:

- What is a swimlane in Kanban?
- What is the difference between a swimlane and a column?
- What are the types of swimlanes?
- How many swimlanes should a Kanban board have?
- What is an expedite lane?
- What are classes of service in Kanban?
- Should each swimlane have a WIP limit?
- Should I have a swimlane per person?
- Does Trello have swimlanes? Does Jira have swimlanes?
- What is the difference between a swimlane diagram and a Kanban swimlane?
- When should you not use swimlanes?

Content gaps we can fill:

- **Classes of service as policies**: table with cost-of-delay pattern, pull policy, WIP rule and example for each class.
- **WIP arithmetic across lanes**: column limits vs lane limits vs capacity allocation, with a worked example.
- **Full worked board design** (illustrative IT team): lanes x columns layout, policies, what changed.
- **Step-by-step setup and review process**.
- **Flow metrics by lane** (cycle time per class, throughput mix, aging, CFD) with links to our metrics guides.
- **Decision table: which lane type for which problem**.
- **Disambiguation**: Kanban swimlanes vs swimlane (process) diagrams.
- **Tool notes** consistent with our reviews.

## SEO Title

**Kanban Swimlanes: Types, Examples and How to Use Them** (52 characters)

## Meta Description

Kanban swimlanes explained: the main types, classes of service, WIP limits per lane, a worked board example and step-by-step setup, plus common mistakes. (153 characters)

## Target Length

3,500–4,000 words (sections + FAQ).

---

# Outline

## H1: Kanban Swimlanes: Types, Examples and How to Use Them

Intro: define swimlanes in the first sentence; when they help; what the guide covers.

## H2: What is a Kanban swimlane?
- 40–60 word definition.
- Anatomy: columns (stages), lanes (categories), cards move left to right within a lane; default lane.
- Kanban University glossary mention.

## H2: Swimlanes vs columns
- Comparison table (what it represents, how cards move, WIP limits, example).
- Rule: sequential steps are columns, parallel streams are lanes.

## H2: Why use swimlanes (and when not to)
- Benefits list; when you do not need them.

## H2: Types of Kanban swimlanes
- Table: lane type, example lanes, best when, watch out for.
- H3s: class of service; work type; team or person; customer or project; epic or feature; priority.

## H2: Classes of service and the expedite lane
- Definitions (glossary-based); policy table; H3 expedite lane rules; H3 fixed date; intangible capacity.
- Alternative: breaching WIP by exception (attributed view).

## H2: WIP limits and swimlanes
- Column limits vs lane limits vs capacity allocation; worked arithmetic; what happens when an expedite arrives.

## H2: Worked example: redesigning a team's board with swimlanes
- Illustrative IT/product team; before problems; lane design table; policies; what to watch afterwards.

## H2: How to set up Kanban swimlanes: step by step
- Numbered steps from problem to review.

## H2: Writing swimlane policies
- Example policy statements per lane.

## H2: Kanban swimlane examples by team
- Table: team, columns, lanes, why.

## H2: Measuring flow by swimlane
- Cycle time per class, throughput mix, aging, CFD, SLE per class.

## H2: Common swimlane mistakes
- List with fixes.

## H2: Swimlanes in Kanban software
- Jira, Wrike, Asana, ClickUp, Trello, Azure Boards; template.

## H2: Kanban swimlanes vs swimlane diagrams
- Short disambiguation.

## FAQ (12–13)
- What is a Kanban swimlane? / Types? / Swimlane vs column? / How many? / Expedite? / Classes of service? / WIP per lane? / Per person? / Intangible? / Trello and Jira? / When not to use? / Swimlane diagram? / Can a card change lane?

## Internal links planned (all in en_urls.txt)

/project-management/kanban/what-is-kanban/, /project-management/kanban/kanban-boards/, /project-management/kanban/kanban-cards/, /project-management/kanban/wip-limits/, /project-management/kanban/kanban-principles/, /project-management/kanban/kanban-metrics/, /project-management/kanban/cycle-time/, /project-management/kanban/throughput/, /project-management/kanban/cumulative-flow-diagram/, /project-management/kanban/wip-aging-chart/, /project-management/kanban/kanban-ceremonies/, /project-management/kanban/blocker-clustering/, /project-management/scrum/scrum-technical-debt/, /project-management/service-level-agreement-sla/, /project-management/swimlane-diagram/, /project-management/kanban/personal-kanban/, /templates/kanban-board-template/, /templates/workflow-template/, /project-management-tools/jira/, /project-management-tools/wrike/, /project-management-tools/asana/, /project-management-tools/clickup/, /project-management-tools/trello/, /project-management-tools/compare/.
