# Brief: Monte Carlo simulation in project management

- URL (unchanged): /project-management/monte-carlo-simulation/
- Prepared: 25 November 2026
- Article type: technique guide (methodology + worked example + formula)
- Learning level: intermediate (assumes the reader knows three-point estimates and the critical path)
- Audience: project managers, planners and project controls staff, PMOs, risk managers, sponsors who receive P50/P80 forecasts, certification candidates studying quantitative risk analysis

## Primary keyword
monte carlo simulation project management

## Secondary keywords (16)
monte carlo simulation in project management; monte carlo analysis project management; monte carlo schedule risk analysis; quantitative risk analysis monte carlo; P50 P80 P90 project; P80 estimate; schedule contingency monte carlo; cost contingency monte carlo; monte carlo simulation excel project; triangular distribution project estimate; beta PERT distribution; criticality index; tornado chart monte carlo; merge bias; joint confidence level (JCL); monte carlo iterations how many; monte carlo vs PERT

## Search intent
Primary: methodology / worked example ("what is it and how do I do it"). Secondary: formula (Excel sampling formula), interpretation (what P80 means), comparison (vs PERT, EMV, sensitivity analysis). Answer "what it is and what it tells you" in the intro and the first 60 words of the first H2.

## Content inventory and duplicate check (framework §30)
- Live page (1 Oct 2026, ~900 words): accurate but thin. Keep: definition, P50/P80 framing, three-task example idea, mistakes list (narrow ranges, correlation, poor logic, false precision, one-off runs), FAQ themes. Its example (three sequential tasks) cannot show merge bias, risk events or cost; it will be replaced by a richer, fully re-verified scenario.
- Parent cluster: /project-management/project-risk-management/ (quantitative risk analysis step links here). Sibling hub for forecasting: /project-management/project-forecasting/.
- Overlap to avoid:
  - /project-management/pert-chart/ already contains a merge-bias Monte Carlo comparison on its portal network. Do not repeat; link to it and use a different network.
  - /project-management/kanban/kanban-planning/ and /kanban/throughput/ contain a throughput Monte Carlo worked example (40 items, 10 weeks of history). Do not repeat; give a short section and link.
  - /project-management/sensitivity-analysis/ covers tornado charts and one-at-a-time analysis. Here: only probabilistic sensitivity (rank correlation) from the simulation; link out.
  - /project-management/contingency-plan/ and /project-risk-management/ size reserves with EMV. Here: confidence-level sizing; link to them for EMV.
- This page is the site's only dedicated Monte Carlo page; several pages link to it as the deep reference, so it must be the most complete treatment. No cannibalisation risk once differentiated as above.
- stats.py similarity run after drafting (see record).

## SERP findings and gaps (searched 25 Nov 2026)
Top results: PMI learning library papers (Kandaswamy 2001 basics tutorial; Barreras 2011 cost estimating), vendor blogs (ClickUp, monday.com, Minitab), course notes.
- monday.com: broad, PMP-oriented, many P50/P80 figures, but no correlation explanation, no merge bias, no discrete risk events, inconsistent iteration guidance, no spreadsheet formulas, no criticality index.
- Minitab: simple three-phase software example and deadline probability; omits distributions, correlation, risk events, P80, criticality, sensitivity.
- PMI papers: good on inputs, correlation matrix, pre/post-mitigation models (Barreras) and path convergence/criticality (Kandaswamy), but dated and not a single worked end-to-end example.
Gaps we can fill: one consistent schedule + cost model with merging paths and discrete risks; a traced single iteration; decomposition of why the deterministic date is optimistic; criticality and rank-correlation drivers; a mitigation decision tested in the model; joint cost-and-schedule confidence; quantified effect of distribution choice, correlation and iteration count; exact Excel inverse-triangular formula.

## SEO
- SEO title / H1 (60 chars): Monte Carlo Simulation in Project Management: Worked Example
- Meta description (<=155): see record.

## Outline
H2 What is Monte Carlo simulation in project management? (40-60 word definition; question it answers; deterministic vs probabilistic; origin; place in quantitative risk analysis)
H2 Why single-point plans are usually optimistic (skew, merge bias, risk events, correlation)
H2 What a Monte Carlo model needs (H3 model; H3 ranges and distributions table; H3 risk events; H3 correlation)
H2 How to run a Monte Carlo simulation, step by step (OL)
H2 Worked example: refurbishing a training centre (illustrative) (H3 inputs; H3 one iteration; H3 schedule results; H3 cost results; H3 why the 42-day plan is unlikely; H3 drivers; H3 mitigation decision; H3 joint confidence)
H2 How to read Monte Carlo outputs (table; choosing a confidence level; GAO/NASA examples)
H2 How assumptions change the answer (distribution, correlation, iterations)
H2 Monte Carlo simulation in Excel (formulas, steps, limits)
H2 Monte Carlo versus PERT, EMV and sensitivity analysis (table + decision rules)
H2 Monte Carlo forecasting in Agile and Kanban (short, link out)
H2 When to use it and when not to
H2 Common mistakes
H2 Further learning (read-next)
FAQ (8-10)

## Planned internal links
project-risk-management, project-risk, risk-register, contingency-plan, pert-chart, critical-path-method, project-network-diagram, float-and-slack, task-dependencies, sensitivity-analysis, project-forecasting, s-curve, cost-estimation, effort-estimation, expert-judgment, project-budget, project-baseline, critical-chain-project-management, schedule-compression, earned-value-management, kanban/kanban-planning, kanban/throughput; templates: risk-register-template, project-cost-estimate-template, critical-path-template, project-schedule-template.

## Templates (verified by reading the pages)
- Risk register template: probability, impact, score (1-25), response, owner, review date, status. Supplies the candidate risk events; it does not run a simulation.
- Project cost estimate template: quantity x rate lines, estimate type dropdown including three-point, contingency %. Supplies cost lines; no simulation.
- Critical path template: activity, duration, predecessors, ES/EF/LS/LF, total float. Supplies the network logic; no simulation.
Say plainly that none of the site templates runs a Monte Carlo simulation.

## Worked examples (all illustrative, verified with Python, numpy 2.5.3 / scipy 1.18.1)
One scenario throughout: refurbishment of a training centre with five activities (A design and approvals; B manufacture and delivery of equipment; C site works; D installation and commissioning after B and C; E testing and handover), two discrete risks (R1 supplier misses factory slot, R2 asbestos found), direct cost ranges, £2,000 per working day time-related cost. 100,000 iterations, seed 1. Plus: traced iterations, mitigation option, distribution comparison, correlation comparison, iteration convergence, classic PERT comparison.

## FAQs
What is it; what does P80 mean; how many iterations; which distribution; P50 vs P80 for budgets; can it be done in Excel; why later than the plan; criticality index; does correlation matter; Agile use; limitations.

## Sources to cite / inspect
- GAO, Schedule Assessment Guide (GAO-16-89G, Dec 2015), schedule risk analysis section (gaoinnovations.gov) - inspected.
- NASA JCL FAQ (12 Oct 2009) - inspected; 70% JCL budgeting, 50% funding minimum, NPD 1000.5.
- Barreras, PMI Global Congress 2011, Monte Carlo simulation in cost estimating - inspected.
- Kandaswamy, PMI 2001, basics of Monte Carlo simulation - inspected.
- LANL, birth of the Monte Carlo method - inspected.
