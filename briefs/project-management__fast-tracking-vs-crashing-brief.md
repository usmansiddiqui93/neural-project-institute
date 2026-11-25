# Brief: /project-management/fast-tracking-vs-crashing/

## Inventory and duplicate check
- Live page (~700 words): comparison table, crash cost slope, office-move crashing example (network partly undocumented: C and E durations missing), fast-tracking example with an off-by-one start day ("FS-2 ... starts day 5 instead of day 7"), how-to-choose list, FAQ. Keep: comparison dimensions, crash-slope logic, "crash cheapest critical activity first", discretionary dependencies, painting-a-room tip idea.
- Parent: /project-management/schedule-compression/ (rewritten; website relaunch example: 8 activities, 58→52 days, least-cost duration, three-option comparison). Do NOT reuse that example. Stay consistent with it: same definitions, crash cost slope formula, Brooks quotation, "Fast tracking only on discretionary dependencies", PMBOK 6th edition attribution, $ currency. It describes this page as having "the six-activity network" and "a second worked example": keep a six-activity network.
- Other overlaps: /project-management/leads-and-lags/ (office fit-out network — avoid office scenarios), /project-management/task-dependencies/ (mandatory/discretionary), /project-management/critical-path-method/, /project-management/float-and-slack/, /project-management/resource-leveling/, /project-management/monte-carlo-simulation/ (merge bias), /project-management/contingency-plan/ (EMV).
- Differentiation (information gain): a risk-adjusted comparison (expected monetary value of fast-tracking rework vs certain crash cost), break-even rework probability, and a structured decision guide. Schedule-compression covers indirect-cost/least-cost duration; this page links rather than repeats.

## Keywords
- Primary: fast tracking vs crashing
- Secondary: crashing vs fast tracking, schedule compression techniques, crash cost slope, crashing in project management, fast tracking in project management, fast tracking example, crashing example, crash point, discretionary dependency, lead time scheduling, rework risk, expected monetary value rework, which is better crashing or fast tracking, PMP fast tracking crashing, critical path compression, overlapping activities
- Intent: comparison (plus worked example/formula). Level: intermediate. Audience: PMs, schedulers, PMP candidates.

## SERP findings
- Asana, ClickUp, Monday, Miro, Wrike blogs: qualitative cost-vs-risk tables, generic examples; no quantified risk, no expected value, no decision threshold (Asana fetched).
- PMI library: Toste-Karayan (2005) congress paper on managing crashed and fast-tracked projects (rework, communication, testing time).
- Gap: nobody quantifies fast-tracking risk against crashing cost, or shows break-even probability; few explain that both techniques share effects (float consumption, more critical paths, resource peaks).

## SEO
- Title/H1: Fast Tracking vs Crashing: Differences and Worked Example
- Meta: Fast tracking vs crashing compared: definitions, crash cost slope, a worked example with risk-adjusted cost, break-even rework probability and how to choose.

## Outline
1. Fast tracking vs crashing: the difference (PMI Lexicon definitions; 40–60 word answer)
2. Side-by-side comparison (table incl. shared effects)
3. How fast tracking works (dependency types, leads/SS, phase overlap, two questions for safe overlap, evidence)
4. How crashing works (crash cost slope with variables/units, crash point, assumptions, divisible work)
5. Worked example: ICT suite refurbishment before term (network, crash-only, fast-track-only, mixed)
6. Comparing the options on risk-adjusted cost (EMV, worst case, break-even probability, interpretation, limitations)
7. How to choose (decision table and rules)
8. Effects both techniques share
9. Recording and approving the decision
10. Common mistakes
FAQ (9)

## Worked example (illustrative, verified in Python)
Six activities A–F, durations 3/4/3/5/2/2; paths A-B-D-F 14 days, A-C-E-F 10. Target 11 days; temporary ICT room hire $2,500/day late. Crash slopes A $3,000, B $2,000, C $1,000 (non-critical), D $1,500 (max 2). Crash-only 11 days for $5,000; fast-track lead 3 on B→D (installation from day 5) with 40% chance of $4,000 rework + 2 days; mixed = crash D 1 day ($1,500) + lead 2 with 15% chance of $2,000 + 1 day. EMV and break-even.

## Sources
PMI Lexicon of Project Management Terms v4.0 (2024); Krishnan, Eppinger & Whitney (1997) Management Science abstract; Toste-Karayan (2005) PMI Global Congress paper; consistency with site pages (schedule compression, task dependencies, leads and lags).
