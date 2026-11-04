# Content Brief: Cycle Time vs Lead Time

URL (unchanged): `/project-management/kanban/cycle-time-vs-lead-time/`
Brief date: 4 November 2026

## Primary Keyword

cycle time vs lead time

(Page angle: the comparison page in our Kanban cluster. The standalone [cycle time](/project-management/kanban/cycle-time/) guide owns "what is cycle time", percentiles and SLEs; this page owns the difference, where each clock starts and stops, how to calculate both from the same card dates, what the gap between them tells you and which one to report to whom.)

## Secondary Keywords

- lead time vs cycle time
- difference between lead time and cycle time
- cycle time and lead time in Kanban / Kanban lead time
- how to calculate lead time and cycle time / lead time formula / cycle time formula
- lead time and cycle time example
- is lead time always longer than cycle time
- commitment point / customer lead time vs system lead time
- lead time vs cycle time vs takt time
- lead time vs cycle time vs throughput
- lead time vs cycle time in Jira / Azure DevOps
- lead time for changes (DORA) vs cycle time
- lead time vs cycle time in manufacturing
- Little's Law lead time cycle time
- how to reduce lead time / how to reduce cycle time
- lead time vs cycle time agile / Scrum
- work item age vs cycle time
- lead time and cycle time template / spreadsheet

## Search Intent

Informational and comparison. Searchers know both terms exist and want a clean, quotable difference first (featured-snippet style), then a worked example and a calculation they can reproduce. A second group (Kanban practitioners, delivery leads, DevOps engineers) wants to know why different sources define the terms differently (Kanban Method vs Kanban Guide vs DORA vs manufacturing) and which number to show to customers. A third group is students and exam candidates (PMI-ACP, Kanban certifications) wanting a precise, defensible definition.

## Target Audience

- Kanban and Scrum teams starting to measure flow
- Delivery leads, Agile coaches, service delivery managers and team leads who report on flow
- IT service, operations and marketing teams running request queues
- DevOps engineers who meet "lead time" in DORA metrics
- Project managers and PMI-ACP / Kanban certification candidates
- Operations and Lean students who know the manufacturing meanings

## SERP Research (WebSearch, 4 November 2026)

Queries: "cycle time vs lead time", "lead time vs cycle time kanban example calculate", "lead time vs cycle time vs takt time vs throughput time difference", plus primary-source checks on the Kanban Guide, Kanban University glossary, DORA and Azure DevOps.

Top results: Wrike blog, Inbound Logistics, IT Revolution, actiTIME, Kodus, EngageBay, Fabrico (manufacturing), DataMyte, PM Study Circle, StarAgile ("19 differences"), Nave, Kanban Zone, Kissflow, Atlassian Community, Lucid template, Kanban Tool, Businessmap, Agile Academy; takt-time comparison pages from UMass bootcamp, SoftwareConnect, Traqq, Everhour, GreyCampus.

Pages fetched for structure (wording not reused):

1. **Nave (lead time vs cycle time in Kanban)**: H2s on defining the commitment point first, what lead time is, what cycle time is, key differences, how to calculate lead time, tips to improve. Lead time starts at commitment, not at request. Calendar example, histogram example. No FAQ, no formulas beyond "lead time = cycle time + not-yet-started period", no customer vs team reporting guidance.
2. **IT Revolution**: definition sections, comparison, management implications, a list of optimisation practices (VSM, DORA, Little's Law mention). No numbers, no formulas, inconsistent cycle time end point, DORA lead time mentioned but not defined.
3. **Kanban Zone**: what is lead time, how to calculate it, what is cycle time (manufacturing then Kanban), calculating cycle time (single item and batch), lead and cycle time on a Kanban board (To Do → Done vs In Progress → Done). Formulas only as images. No worked dataset, no FAQ.

Primary sources checked:
- **Kanban Guide v2025.5 (kanbanguides.org, May 2025; Coleman, Vacanti and others)**: four flow measures WIP, throughput, work item age, cycle time. Cycle time = "elapsed time between when a work item started and when a work item finished". **The term "lead time" does not appear.** SLE = forecast from started to finished, based on historical cycle time.
- **Kanban University glossary and article (7 April 2023)**: lead time is generic, from point A to point B in the workflow. **Customer lead time** = time between receiving the customer's request and delivering on it (changed in 2023; it used to start at the commitment point). **System lead time** = commitment point to the first unbounded (no WIP limit) column. Commitment point = where the decision is made to start delivering a work item.
- **DORA (via UK Home Office engineering standards)**: change lead time = time for a code commit or change to be successfully deployed to production. Four metrics: change lead time, deployment frequency, change fail percentage, failed deployment recovery time.
- **Microsoft Learn, Azure DevOps Lead Time and Cycle Time widgets**: lead time = created → Completed; cycle time = first enters In Progress → Completed; reopened items keep the original start; scatter charts with moving average and standard deviation band.
- Our live [cycle time](/project-management/kanban/cycle-time/) guide uses finish − start + 1 in calendar days, nearest-rank percentiles and Little's Law (1961). Keep consistent.

Common H2s across results: what is lead time; what is cycle time; key differences (often a table); how to calculate each; lead and cycle time on a Kanban board; why they matter; how to reduce; sometimes takt time.

People Also Ask / related questions:
- What is the difference between lead time and cycle time?
- Is lead time always longer than cycle time?
- How do you calculate lead time and cycle time?
- What is lead time in Kanban?
- What is the difference between lead time, cycle time and takt time?
- Is cycle time part of lead time?
- Which is more important, lead time or cycle time?
- What is lead time for changes in DORA?
- What is a commitment point?
- How do you reduce lead time?
- What is the difference between cycle time and throughput?
- Can lead time and cycle time be the same?

Content gaps we can fill:
- **A source-by-source definitions table** (Kanban Guide, Kanban University customer/system lead time, DORA, Azure DevOps, manufacturing). No top result explains why definitions conflict.
- **A board diagram in words**: the five clock points (request, commitment, start, finish, delivery) and which measure spans which.
- **A reproducible calculation** using the same +1, calendar-day convention as our cycle time guide.
- **A ten-item worked dataset** with request, start and finish dates, medians, 85th percentiles and the share of lead time spent waiting before work starts.
- **"What the gap tells you" diagnostic table** (four patterns and the action for each).
- **Little's Law applied to both boundaries** with an illustrative before/after showing lead time halving without anyone working faster.
- **Who should see which number** (customers, team, management, service desk) and how to phrase a customer-facing forecast.
- **Tool notes** (Jira control chart, Azure DevOps widget definitions, Wrike request intake and custom statuses, spreadsheet).

## SEO Title

**Cycle Time vs Lead Time: Differences, Formulas, Examples** (55 characters)

## Meta Description

Cycle time vs lead time explained: where each starts and stops, how to calculate both, worked Kanban examples, Little's Law and which one to report. (148 characters)

## Target Length

3,700–4,000 words (sections + FAQ).

---

# Outline

## H1: Cycle Time vs Lead Time: Differences, Formulas, Examples

Intro: answer directly in sentence one (lead time = request to delivery, the customer's wait; cycle time = start to finish, the team's process; cycle time sits inside lead time). Say what the guide covers.

## H2: What is the difference between cycle time and lead time?
- 40–60 word definition paragraph.
- Equation: lead time = waiting before work starts + cycle time (+ any wait after finish before delivery).
- Comparison table: starts, ends, includes backlog wait, whose experience, question it answers, who mainly controls it, typical use.

## H2: Where the clock starts and stops on a Kanban board
- The five points: request logged, commitment point, work started, work finished, delivered. Table of which measure spans which.
- H3: Why definitions differ between sources (table: Kanban Guide, Kanban University customer lead time / system lead time, DORA change lead time, Azure DevOps, manufacturing).
- H3: Write your definitions down as a policy (example policy wording).

## H2: How to calculate lead time and cycle time
- Formulas with the +1 convention; calendar days; step-by-step numbered process; spreadsheet column set-up.
- H3: Averages, medians and percentiles (short; link to cycle time guide).

## H2: Worked example: one request from start to finish
- Illustrative dated timeline table; step-by-step calculation; what the customer experienced vs what the team did.

## H2: Worked example: ten finished items
- Table of 10 items (requested, started, finished, wait before start, cycle time, lead time).
- Medians, 85th percentiles, averages; share of lead time spent waiting; reading the result.

## H2: What the gap between lead time and cycle time tells you
- Diagnostic table: four patterns, likely cause, action.

## H2: Lead time, cycle time and Little's Law
- Formula for each boundary; illustrative worked example (queue 20, WIP 6, throughput 4/week); before/after table cutting the queue; assumptions and the "options are not a queue" caveat.

## H2: Cycle time vs lead time vs other flow measures
- Table: lead time, cycle time, work item age, throughput, WIP, takt time, DORA change lead time, touch time / flow efficiency, scheduling "lead".

## H2: Which one should you report, and to whom?
- Table by audience; how to turn lead time history into a customer-facing forecast (steps); link to SLA and forecasting guides.

## H2: How to reduce lead time
- H3s: shorten and prune the queue; replenish little and often; decide faster at the commitment point; remove waits after "done"; use classes of service carefully.

## H2: How to reduce cycle time
- Short list with links (WIP limits, split work, faster reviews, blockers, swarm on aged items, automation). Link to cycle time guide.

## H2: Measuring lead time and cycle time in project management tools
- Jira control chart, Azure DevOps widget definitions, Wrike request intake and custom statuses (our #1), ClickUp dashboards, spreadsheet + Kanban board template / work request template.

## H2: Common mistakes when comparing cycle time and lead time
- 8–10 bullets.

## Internal links (planned)
/project-management/kanban/cycle-time/, /project-management/kanban/throughput/, /project-management/kanban/wip-limits/, /project-management/kanban/kanban-metrics/, /project-management/kanban/flow-efficiency/, /project-management/kanban/cumulative-flow-diagram/, /project-management/kanban/wip-aging-chart/, /project-management/kanban/kanban-boards/, /project-management/kanban/kanban-cards/, /project-management/kanban/kanban-planning/, /project-management/kanban/pull-system-vs-push-system/, /project-management/kanban/value-stream-mapping/, /project-management/kanban/lean-manufacturing/, /project-management/kanban/devops/, /project-management/kanban/continuous-delivery/, /project-management/kanban/kanban-ceremonies/, /project-management/monte-carlo-simulation/, /project-management/project-forecasting/, /project-management/service-level-agreement-sla/, /project-management/leads-and-lags/, /project-management/scrum/backlog-refinement/, /project-management/agile/user-stories/, /project-management-tools/wrike/, /project-management-tools/jira/, /project-management-tools/clickup/, /templates/kanban-board-template/, /templates/work-request-template/

## FAQs (from PAA and related searches)
1. What is the difference between cycle time and lead time?
2. Is lead time always longer than cycle time?
3. Can lead time and cycle time be the same?
4. How do you calculate lead time and cycle time?
5. What is lead time in Kanban?
6. What is the commitment point?
7. Which is more important, lead time or cycle time?
8. What is the difference between lead time, cycle time and takt time?
9. Is DORA lead time for changes the same as cycle time?
10. How do lead time and cycle time relate to throughput?
11. Should I use calendar days or working days?
12. Does a "lead" in project scheduling relate to lead time?
13. Does Little's Law apply to lead time as well as cycle time?
14. What is the difference between lead time and work item age?

## Writer notes
- Use the same conventions as our cycle time guide: calendar days, finish − start + 1, nearest-rank percentiles. The old page used delivery − request without the +1 (its example gave 13 and 4 days); the rewrite switches to +1 and says so.
- The Kanban Guide does not define lead time; do not imply it does. Attribute customer and system lead time to Kanban University (2023 change).
- Label all worked examples as illustrative. No invented benchmarks.
- Tool claims only from our review pages and vendor docs checked above. Be positive about every tool.
- British spelling.
