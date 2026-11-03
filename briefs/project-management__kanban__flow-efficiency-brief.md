# Content Brief: Flow Efficiency

URL (unchanged): `/project-management/kanban/flow-efficiency/`
Brief date: 4 November 2026

## Primary Keyword

flow efficiency

(Page angle: flow efficiency for Kanban and delivery teams, with the formula, worked calculations, a measurement method and improvement levers. "flow efficiency formula" and "how to calculate flow efficiency" are the main supporting phrases.)

## Secondary Keywords

- what is flow efficiency
- flow efficiency formula
- how to calculate flow efficiency
- flow efficiency example / flow efficiency calculation example
- flow efficiency in Kanban / Kanban flow efficiency
- flow efficiency vs resource efficiency (resource utilisation)
- flow efficiency vs cycle time / lead time
- what is a good flow efficiency / flow efficiency benchmark
- how to measure flow efficiency (active and wait states, Kanban board)
- how to improve flow efficiency
- touch time vs wait time / active time vs wait time
- process cycle efficiency (Lean Six Sigma term) / value-added time ratio
- flow efficiency in value stream mapping
- flow efficiency and Little's Law / WIP limits
- efficiency paradox / efficiency matrix (This Is Lean)
- flow efficiency chart / flow efficiency in Jira
- flow efficiency template
- limitations of flow efficiency

## Search Intent

Informational with a strong "how to" layer. Searchers want the definition and formula first, then a worked calculation, then practical guidance on measuring it from a board and raising it. A secondary group (Lean/Six Sigma students, delivery leads) wants the conceptual contrast with resource efficiency and an honest answer to "what is a good number?".

## Target Audience

- Kanban, Scrum and DevOps teams starting to use flow metrics
- Delivery leads, Agile coaches and team leads who report on flow
- Project and programme managers looking for why work takes so long
- Operations, marketing and service teams running request workflows
- Lean / Six Sigma practitioners and students (process cycle efficiency)

## SERP Research (WebSearch, 4 November 2026)

Queries: "flow efficiency", "how to calculate flow efficiency kanban example", "flow efficiency vs resource efficiency Modig Åhlström This is Lean", "David Anderson flow efficiency 40% very good".

Top results: Swarmia help docs, Businessmap (Kanban analytics: flow efficiency), Nimblework blog, FourWeekMBA, ASOS tech blog (Nick Brown, "The many flaws of flow efficiency", 2023), Kodus and minware metric docs, Allstacks, ClickUp blog, Scrum.org forum, ProKanban blog, Kanban Zone, Nave (flow efficiency chart and blog), Gemba Academy, TechTarget, Kanban Tool (advanced Kanban metrics).

Pages fetched for structure (wording not reused):

1. **Businessmap (flow efficiency)**: H2s What is flow efficiency, How to measure it, then product tools (flow efficiency chart, process efficiency widget). Formula = value-added time ÷ lead time × 100; non-value-added = wait + blocked time; one example (1 day active in 5 = 20%). No benchmarks, no FAQ.
2. **Nimblework blog**: sections Introducing the metric, Calculating, Visualising wait, What is normal, Improving. Quotes ~15% as "normal" and >40% as "good", attributed second-hand to David J. Anderson via a blog. No numeric example.
3. **ASOS tech blog (Nick Brown, 2023), The many flaws of flow efficiency**: criticisms: no wait states gives 100%; start/stop times unmeasurable; blocked time in active states ignored; comparisons between items meaningless; averages hide outliers. Found no study validating commonly quoted typical values (5–15%, 40% "very good" are anecdotal). Follow-up post from the same author ("Our survey says…") reported team-level averages across 63 teams in his organisation's own data: average 35%, range 9% to 68%.

Also checked: summary of Modig and Åhlström, *This Is Lean: Resolving the Efficiency Paradox* (2012): flow efficiency vs resource efficiency and the efficiency matrix (efficient islands, efficient ocean, wasteland, perfect state). Kanban Guide 2025 edition (ProKanban.org) lists WIP, throughput, work item age and cycle time as its required measures; it does not mention flow efficiency, so present flow efficiency as a supporting metric (consistent with our Kanban metrics guide).

Common H2s: what is flow efficiency; formula/how to calculate; how to measure; what is a good flow efficiency; how to improve; flow vs resource efficiency.

People Also Ask / related questions:

- What is flow efficiency?
- How do you calculate flow efficiency?
- What is a good flow efficiency percentage?
- What is the difference between flow efficiency and resource efficiency?
- How do you improve flow efficiency?
- Is flow efficiency the same as process cycle efficiency?
- What is touch time vs wait time?
- Should blocked time count as active time?
- Is flow efficiency a Kanban metric?
- Does flow efficiency use cycle time or lead time?
- What is the efficiency paradox?

Content gaps we can fill:

- **A full worked calculation from card timestamps** (stage by stage, active vs waiting vs blocked) rather than a one-line example.
- **Team-level calculation showing aggregate vs average-of-percentages** and why the method choice matters.
- **Step-by-step measurement method** with a board design table that labels each column active or waiting, plus policies for what counts as active.
- **Honest "what is good" section** that explains figures are anecdotal, cites the one public data set we found, and recommends trend-based targets.
- **Flow vs resource efficiency** with the efficiency matrix and a simple queueing table showing how waiting grows as utilisation approaches 100%.
- **Before/after improvement example using Little's Law** (WIP cut, same active time, flow efficiency doubles).
- **Limitations and gaming risks**, and common mistakes.

## SEO Title

**Flow Efficiency: Formula, Examples and How to Improve It** (55 characters)

## Meta Description

Flow efficiency explained: the formula, worked examples, how to measure active and wait time on a Kanban board, what a good figure is and how to improve it. (155 characters)

## Target Length

3,600–4,000 words (sections + FAQ).

---

# Outline

## H1: Flow Efficiency: Formula, Examples and How to Improve It

Intro: define flow efficiency in the first sentence (share of an item's time in process spent actively worked on); state the usual finding (waiting dominates); say what the guide covers.

## H2: What is flow efficiency?
- 40–60 word definition paragraph.
- Plain-language framing: "watch the baton, not the runners" (flow unit vs resource).
- Origins: Lean; value-added ratio / process cycle efficiency in Lean Six Sigma; Modig and Åhlström 2012 popularised flow vs resource efficiency; used in Kanban as a supporting flow metric (not one of the Kanban Guide's four required measures).

## H2: The flow efficiency formula
- Formula and the terms (active/touch time, wait time, blocked time, total time).
- Table: term, meaning, examples.
- H3: Cycle time or lead time as the denominator (state which; both valid; be consistent).
- H3: Item-level vs aggregate flow efficiency (sum of active ÷ sum of total vs average of item percentages).

## H2: Worked example: calculating flow efficiency for one item
- Illustrative card history table by column with dates, days, active/wait/blocked classification.
- Step-by-step calculation: cycle-time basis and lead-time basis.
- What the numbers tell you (where the longest waits are).

## H2: Worked example: flow efficiency for a team
- Five completed items table; aggregate vs simple average; interpretation; look at the distribution.

## H2: Flow efficiency vs resource efficiency
- Definitions; why they conflict; efficiency matrix table (four states).
- Queueing table: utilisation vs relative waiting (simple M/M/1 model, ρ/(1−ρ)), labelled as a simplified model.
- Implication: slack at non-constraints is deliberate.

## H2: Flow efficiency vs cycle time, lead time and other metrics
- Comparison table (metric, measures, question, how flow efficiency relates).

## H2: What is a good flow efficiency?
- No validated benchmark; commonly quoted ranges are anecdotal (attribute to Kanban community/Anderson, flagged as anecdotal).
- One public data set: 63 teams, average 35%, range 9–68% (ASOS internal data, 2023, one organisation).
- Recommend baseline + trend + distribution; target the longest waits.

## H2: How to measure flow efficiency step by step
- Numbered steps (agree boundaries, split columns, write active policy, track blocked, capture timestamps, calculate, review distribution, review regularly).
- H3: Designing a board that shows waiting (table: column, active or waiting, notes).
- H3: Measuring without a digital tool (sampling, dot stamps, spreadsheet).
- H3: Flow efficiency in a value stream map.

## H2: Why flow efficiency is often low
- Table: cause, what you see on the board, typical fix.

## H2: How to improve flow efficiency
- H3s: limit WIP; shrink queues before reviews and approvals; reduce handoffs and dependencies; make work smaller; fix recurring blockers; swarm on old items; pace intake to the constraint.

## H2: Worked example: improving a team's flow efficiency
- Illustrative before/after with Little's Law (WIP 24 → 12, throughput 6/week, cycle time 4 → 2 weeks, active 3 days constant, 15% → 30%), plus review-queue policy.
- Before/after table.

## H2: Limitations of flow efficiency
- Measurement precision, states model, blocked time, averages, not for comparing teams, gaming, not a people metric.

## H2: Common flow efficiency mistakes
- 8 bullets.

## H2: Tools and templates for tracking flow efficiency
- Wrike custom statuses and dashboards (our #1), Jira CFD and control charts, dedicated Kanban analytics tools; Kanban board template, workflow template, root cause analysis template.

## Internal links (planned)
/project-management/kanban/kanban-metrics/, /project-management/kanban/cycle-time/, /project-management/kanban/cycle-time-vs-lead-time/, /project-management/kanban/throughput/, /project-management/kanban/wip-limits/, /project-management/kanban/cumulative-flow-diagram/, /project-management/kanban/wip-aging-chart/, /project-management/kanban/blocker-clustering/, /project-management/kanban/value-stream-mapping/, /project-management/kanban/theory-of-constraints/, /project-management/kanban/kanban-boards/, /project-management/kanban/lean-kanban/, /project-management/kanban/pull-system-vs-push-system/, /project-management/agile/agile-swarming/, /project-management/agile/user-stories/, /project-management/lean-project-management/, /project-management/capacity-planning/, /templates/kanban-board-template/, /templates/workflow-template/, /templates/root-cause-analysis-template/, /project-management-tools/wrike/, /project-management-tools/jira/ (22 links)

## FAQs (from PAA and related searches)
1. What is flow efficiency?
2. How do you calculate flow efficiency?
3. What is a good flow efficiency?
4. Is flow efficiency the same as resource utilisation?
5. What is the difference between flow efficiency and cycle time?
6. Should blocked time count as active time?
7. Is flow efficiency an official Kanban metric?
8. What is the difference between flow efficiency and process cycle efficiency?
9. How do you improve flow efficiency?
10. Can you compare flow efficiency between teams?
11. Does value stream mapping measure flow efficiency?

(Cycle time vs lead time as denominator and "is high flow efficiency always good" are answered in the body.)

## Writer notes
- Label all worked examples as illustrative. Do not present quoted "typical" percentages as research; attribute and flag them as anecdotal.
- Keep Little's Law and definitions consistent with our cycle time, throughput and cycle time vs lead time guides.
- Paraphrase Modig and Åhlström; do not quote.
- British spelling.
