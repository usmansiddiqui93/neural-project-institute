# Content Brief: WIP Aging Chart

URL (unchanged): `/project-management/kanban/wip-aging-chart/`
Brief date: 25 November 2026
Writer brief: RW_BRIEF.md v2 / FRAMEWORK.md V1.0

## Why this page is being rewritten
The live page (published 14 September 2026, about 1,000 words including FAQs) is accurate but thin: one paragraph on what the chart shows, four reading rules, four meeting actions and 11 short FAQs. It has no worked example, no calculation of work item age or percentiles, no explanation of total age vs time in stage, no per-stage ("pace") reading, no build instructions, and no limitations. Keep: the leading-indicator framing, 50th/85th percentile reading rules, oldest-first daily review, "old dots in early stages", the SLE link, FAQ themes.

## Primary keyword
WIP aging chart

Spelling note: the chart is widely known by its American name ("aging chart", "Aging Work in Progress chart" in ActionableAgile, "Aging WIP" in Businessmap) and the URL uses it. The H1 and chart name keep "aging"; running prose uses British "ageing" for the verb and adjective.

## Secondary keywords (15)
- aging work in progress chart / aging WIP chart
- work item age
- work item age Kanban
- how to read a WIP aging chart
- work item aging chart (Vacanti)
- WIP aging chart percentiles / 85th percentile line
- pace percentiles
- service level expectation (SLE)
- work item age vs cycle time
- leading indicator Kanban
- WIP aging chart Excel / build in a spreadsheet
- total WIP age
- daily Kanban meeting ageing work
- Kanban flow metrics
- stuck work / stale work items

## Search intent
How-to (read and use the chart) with a definition answer first. Searchers are Kanban and Scrum practitioners who have seen the chart in a tool, or heard of work item age from the Kanban Guide, and want to know how to read the dots and lines and what to do about old items. A smaller group wants to build one without a specialist tool.

## Learning level and audience
Intermediate. Kanban team members, Scrum Masters, delivery leads, project managers using flow metrics, certification candidates. Assumes the reader knows what a Kanban board and cycle time are (linked prerequisites).

## SERP findings (WebSearch "aging work in progress chart kanban how to read", 25 Nov 2026)
Results: 55 Degrees / ActionableAgile documentation (two versions), Businessmap knowledge base and blog, Scrum.org blogs (John Coleman 2024, Julia Wester 2020), Atlassian community app articles, Rework, Microsoft and Jira CFD docs (not aging).
Fetched (wording not reused):
1. **ActionableAgile "Aging Work in Progress" docs (updated 11 Dec 2025, archived)**: X = workflow stages, Y = cumulative age since first checked stage; done percentile lines from completed items; per-column **pace percentile** colour bands from ages at which past items left each column; needs at least 10 completed items; stalled alert; aging replay.
2. **Businessmap "Aging WIP"**: Y axis = days in **current stage**, not total age; pace percentiles mentioned without method; no numbers, no build steps.
3. **Scrum.org, Julia Wester (6 Feb 2020)**: two daily habits (limit WIP, watch age); dots by stage and age with scatterplot percentile lines.
4. **Scrum.org, John Coleman (4 Jan 2024)**: compare relative age; same age in an earlier column is relatively older; unblock first; cancel items on hold; avoid moving items backwards.

Gaps we fill: a full numerical example (30 finished items, nine items in progress, ages calculated, percentile bands calculated by nearest rank), the conditional probability of still meeting the SLE given current age, total age vs time-in-stage explained, per-stage pace computed in the example, spreadsheet build using the site's own Kanban board template columns, interpretation patterns table, limitations.

## Primary sources
- **The Kanban Guide**, John Coleman and Daniel Vacanti, edition 2025.5 (1 May 2025): Work Item Age = elapsed time between when a work item started and the current date; four mandatory flow metrics; SLE = period of elapsed time plus a probability, based on historical cycle time; "ensuring work items do not age unnecessarily, using the SLE as a reference" is part of actively managing items; the guide prescribes no specific chart.
- **Daniel S. Vacanti, Actionable Agile Metrics for Predictability, 10th Anniversary Edition (2025)**, Leanpub sample: chapters 6 "The Work Item Aging Chart" and 7 "Leveraging the Aging Chart for Predictability"; Age = current date − start date + 1 (inclusive, never zero). Only the sample (TOC and early chapters) was inspected.

## Duplicate / cannibalisation check
- `/project-management/kanban/cycle-time/` has a short "work item age" subsection with a three-item table and its own 20-item dataset (85th percentile 11 days). We link to it for cycle time and percentiles and use a **different** dataset (30 items, SLE 14 days).
- `/project-management/kanban/kanban-metrics/` lists work item age as one of four metrics; we link.
- `/project-management/kanban/kanban-planning/` owns SLE calculation; we link and only apply it.
- `/project-management/kanban/blocker-clustering/`, `/kanban-ceremonies/`, `/cumulative-flow-diagram/`, `/wip-limits/`, `/throughput/`: linked for follow-on actions.
Conventions kept consistent with the site: calendar days, age = today − start date + 1, nearest-rank percentiles, 20–30 items before publishing an SLE.

## SEO title (H1)
WIP Aging Chart: How to Read and Use It, With Examples (54 chars)

## Meta description
How to read a WIP aging chart: work item age, percentile lines, per-stage pace, a worked example with SLE risk, daily actions and how to build one in Excel. (≈153 chars)

## Outline
- H2 What is a WIP aging chart? (definition block; leading vs lagging)
- H2 Work item age: the measure behind the chart (definition, formula, convention, total age vs time in stage)
- H2 Anatomy of the chart (axes, dots, percentile lines, pace bands, SLE line)
- H2 Worked example: reading one team's chart (illustrative; history, percentiles, ages, overall vs per-stage reading, conditional probability, actions, Little's Law check)
- H2 Patterns to look for and what they mean (table)
- H2 Using the chart in the daily Kanban meeting (steps)
- H2 How to build a WIP aging chart in a spreadsheet (steps with formulas)
- H2 WIP aging chart vs other Kanban charts (table)
- H2 Limitations
- H2 Common mistakes
- FAQ (10–12)

## Planned internal links
Kanban hub, what is Kanban, kanban metrics, cycle time, cycle time vs lead time, kanban planning, WIP limits, kanban ceremonies, blocker clustering, cumulative flow diagram, throughput, kanban boards, kanban cards, kanban swimlanes, flow efficiency, daily scrum, monte carlo simulation, templates: kanban board template.

## FAQs
What is a WIP aging chart? What is work item age? How is work item age calculated? How do you read the percentile lines? Aging chart vs cycle time scatterplot? Why is age a leading indicator? What should a team do about an ageing item? Total age or time in stage? How much history do you need? Does Scrum use it? How often to review? Which tools produce one?

## Worked example
Illustrative website development team: 30 finished items (cycle times listed), nearest-rank P50 8, P70 10, P85 14, P95 21 days; SLE 85% within 14 days; nine items in progress on Wednesday 25 November 2026 with start dates; ages; share of past items that took longer; conditional probability of meeting the SLE; per-stage 85th percentile exit ages (Analysis 3, Development 8, Review 11, Testing 14); actions; Little's Law check (5 items/week, WIP 9 → about 12.6 days average cycle time if throughput holds). All numbers verified in Python (record).

## Sources to cite
Kanban Guide 2025.5 (inspected); Vacanti AAMFP 10th anniversary sample (inspected, partial); ActionableAgile Aging WIP docs (inspected); Businessmap Aging WIP article (inspected); Wester 2020 and Coleman 2024 Scrum.org posts (inspected).
