# Content Brief: PERT Chart

URL (unchanged): `/project-management/pert-chart/`
Brief date: 4 November 2026

## Primary Keyword

PERT chart

## Secondary Keywords

- what is a PERT chart
- PERT chart example
- how to make a PERT chart / PERT chart steps
- PERT formula ((O + 4M + P) / 6)
- PERT estimate / three-point estimate
- PERT standard deviation and variance
- PERT probability of completion / PERT z-score
- PERT critical path
- PERT chart vs Gantt chart
- PERT vs CPM
- PERT chart template
- activity on arrow vs activity on node (PERT diagram)
- dummy activity in PERT
- PERT advantages and disadvantages
- PERT merge bias
- PERT stands for (Program Evaluation and Review Technique)
- PERT chart in project management software

## Search Intent

Mixed informational and how-to. Beginners want a definition and a picture of what the chart looks like; students and exam candidates want the formulas and a worked example including probability; practitioners want to know when PERT is worth the effort, how it compares with CPM and Gantt charts, and how to do it in their tools.

## Target Audience

- Students and PMP, CAPM and PMAI learners practising three-point estimating and network calculations
- Project managers and planners on uncertain projects (IT, R&D, engineering, events)
- Team leads asked to give a delivery date "with confidence"

## Recommended Length

3,600–4,000 words (sections + FAQ), upper end of the house range at the site owner's request.

## SERP Research (searched 4 November 2026)

Queries: "PERT chart", "PERT chart example how to calculate probability of completing project critical path".

Top-ranking pages (sample): TechTarget (two definitions), Lucidchart, Adobe, Coursera, G2, Toggl, ProjectManager.com, Creately, educative.io, CareerFoundry, fourweekmba, Smartsheet "PERT 101", Wikipedia, university PDFs and the R `critpath` package vignette for the probability query.

Structure observed (WebFetched TechTarget, Lucidchart, critpath vignette, Wikipedia):
- **TechTarget:** how a PERT chart works (events, arrows, dummy activities, slack, critical path), how to create one (four steps, expected-time formula), when to use, advantages, disadvantages, PERT vs Gantt. No standard deviation or probability.
- **Lucidchart:** symbols and terms, how to make a chart, PERT analysis with SD, CPM, PERT formula, PERT vs Gantt, PERT vs CPM, diagram examples. Single-activity expected-time example; no probability.
- **critpath vignette:** nine-activity AOA network, expected completion 31 days, SD 1.49, normal approximation for the chance of meeting a deadline. Does not discuss merge bias.
- **Wikipedia:** history (1958, US Navy Special Projects Office with Lockheed and Booz Allen Hamilton for Polaris; first called Program Evaluation Research Task), terminology, AOA vs AON, formulas, pros and cons, uncertainty criticisms.

Common H2s: what is a PERT chart; symbols/terms; how to create; formula; example; PERT vs Gantt; PERT vs CPM; advantages/disadvantages; templates.

People Also Ask style questions:
- What is a PERT chart used for?
- What does PERT stand for?
- How do you calculate PERT?
- What is the difference between PERT and a Gantt chart?
- What is the difference between PERT and CPM?
- How do you calculate the probability of completing a project in PERT?
- Why is the most likely estimate multiplied by 4?
- What is a dummy activity?
- Is a PERT chart the same as a network diagram?
- What are the disadvantages of PERT?
- Is PERT used in Agile?

Content gaps we can fill:
- **One complete worked example** from three-point estimates to expected durations, forward and backward pass, critical path, path variance, probability of a deadline and confidence dates (most pages stop at the expected-time formula).
- **The same network drawn both ways**: activity-on-node table and activity-on-arrow event table with a real dummy activity and event slack.
- **Merge bias shown with numbers**: our 200,000-run Monte Carlo of the same illustrative network gives 76% for a 40-day deadline against PERT's 83%, because a near-critical path drives the finish in about 38% of runs.
- **Turning PERT into a commitment**: P80/P90 dates and schedule contingency.
- **Software**: how to hold O, M and P in tools without native PERT fields (custom fields and formulas), linked to our tool reviews.

## SEO Title

PERT Chart: Formula, Steps and Worked Example (44 characters)

## Meta Description

What a PERT chart is and how to make one: the PERT formula, step-by-step method, a full worked example with probability, PERT vs CPM and Gantt, and pitfalls. (153 characters)

## Outline

**Intro:** a PERT chart is a network diagram used with the Program Evaluation and Review Technique; three estimates per activity give an expected duration and a probability of meeting a date.

### H2: What is a PERT chart?
- 40–60 word definition; PERT chart vs PERT estimate; AON vs AOA.

### H2: A short history of PERT
### H2: PERT chart symbols and terms (table)
### H2: The PERT formulas
- Table; single-activity example (O 4, M 6, P 14 = 7 days); why weight 4; triangular alternative.

### H2: How to make a PERT chart step by step
### H2: Worked example: launching a customer portal (illustrative)
- H3 Activities and three-point estimates; H3 Expected durations and variances; H3 Forward and backward pass; H3 The critical path; H3 The same network as an activity-on-arrow chart (events, dummy, event slack).

### H2: Probability of meeting a deadline
- z formula, step list, deadline table, confidence dates; short z table.

### H2: Merge bias: why PERT can be optimistic
- Monte Carlo comparison table; what to do.

### H2: Turning PERT results into a schedule commitment
### H2: PERT vs CPM vs Gantt chart (table)
### H2: Advantages and disadvantages of PERT charts
### H2: When to use a PERT chart
### H2: PERT charts in project management software
### H2: Common PERT mistakes

Internal links planned: critical-path-method, forward-and-backward-pass, float-and-slack, project-network-diagram, task-dependencies, gantt-chart, monte-carlo-simulation, cost-estimation, effort-estimation, project-scheduling, work-breakdown-structure, contingency-plan, critical-chain-project-management, schedule-compression, project-milestones, agile/agile-estimation-story-points, pmp-certification, sensitivity-analysis, tools (wrike, smartsheet, clickup, microsoft-planner), templates (critical-path-template, project-schedule-template, gantt-chart-template).

## FAQs (13)
1. What does PERT stand for?
2. What is a PERT chart used for?
3. What is the PERT formula?
4. How do you calculate PERT standard deviation?
5. Why is the most likely value multiplied by 4?
6. How do you calculate the probability of completing a project with PERT?
7. Is a PERT chart the same as a network diagram?
8. What is a dummy activity in a PERT chart?
9. What is the difference between a PERT chart and a Gantt chart?
10. What is the difference between PERT and CPM?
11. Can PERT be used in Agile?
12. Who invented PERT?
13. Is PERT on the PMP exam?

## Consistency rules
- Day-0 convention, same formulas as `/project-management/forward-and-backward-pass/` and `/project-management/float-and-slack/`.
- Worked example numbers computed with a script: critical path A-B-D-F-G-I = 37 days, path variance 10.22, SD 3.20; near-critical A-E-F-G-I = 36 days; 40-day deadline z = 0.94, 82.6%; P80 39.7, P90 41.1, P95 42.3; Monte Carlo (beta-PERT, 200,000 runs, illustrative) mean 37.8, P(40) 76.1%, P80 40.4, P90 41.9.
- History: 1958, US Navy Special Projects Office with Lockheed and Booz Allen Hamilton, Polaris programme (Wikipedia; widely cited).
