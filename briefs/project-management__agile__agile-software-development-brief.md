# Brief: /project-management/agile/agile-software-development/

## Inventory and duplicate check
- Live page (published 25 Sep 2026, ~600 words): development cycle list, practice table, short DevOps paragraph, best-practice list, FAQ. Keep: the practice set (TDD, CI, CD, pairing, review, refactoring, trunk-based development), small stories, DoD with automated tests, feature flags, blameless reviews. Fix: DevOps paragraph lists DORA's old four metrics ("time to restore service"); the cycle implies release happens after the Sprint Review (the 2020 Scrum Guide says the Sprint Review is never a gate to releasing value); "TDD leads to fewer defects" stated as fact; pair programming described as "two developers share one task" only.
- Parent cluster: /project-management/agile/ (Agile guide). Prerequisites: Agile Manifesto, what is Scrum, user stories.
- Overlapping intent / pages to link rather than repeat:
  - /project-management/agile/agile-development-life-cycle/ (phases, gym-booking example) — life-cycle intent; this page is about engineering practice.
  - /project-management/kanban/continuous-delivery/ (pipeline, CI vs CD vs deployment, monthly-release-window flow-efficiency example) — do not repeat its example.
  - /project-management/kanban/devops/ (DORA five metrics, deployment-log worked example) — reuse only definitions, link for the calculation.
  - /project-management/agile/types-of-agile-methodologies/ (XP paragraph), /project-management/scrum/scrum-technical-debt/, /project-management/agile/definition-of-done/, /project-management/agile/agile-metrics-and-kpis/.
- Differentiation: the page explains how the engineering practices fit together from story to production, what the frameworks do and do not require, and gives an original calculation (test-suite shape vs CI feedback time) not found on any site page.

## Keywords
- Primary: agile software development
- Secondary: agile software development practices, agile engineering practices, extreme programming practices, test-driven development, continuous integration, trunk-based development, test automation pyramid, pair programming, code review, refactoring, continuous delivery, feature flags, definition of done software, technical debt, DORA metrics, agile vs devops, agile software development process, agile software development example, AI coding assistants agile
- Intent: methodology / how-to (how Agile software development works day to day), secondary definition.
- Level: beginner to intermediate. Audience: PMs, Scrum Masters, Product Owners, developers new to Agile teams, students.

## SERP findings and gaps
- Atlassian (/agile/software-development): developer-focused practices, branch-per-task PRs, CI, DoD; names metrics (incl. outdated "mean time to recovery") without definitions; no worked example, no limitations, vendor promotion.
- Microsoft Learn (What is Agile development?): backlog refinement, CI/CD, technical debt; no TDD, pyramid, trunk-based development, metrics or examples.
- Wikipedia: history and methods list.
- Gaps to fill: what Scrum vs XP vs Kanban require; quantitative reason the test pyramid enables CI; current DORA five metrics; when Agile software development is harder; AI assistant limits; PM role.

## SEO
- Title/H1: Agile Software Development: Practices, Process and Examples
- Meta: How Agile software development works: the flow from story to production, XP practices, test pyramid and CI worked example, DORA metrics and pitfalls.

## Outline
1. What is Agile software development? (definition, Manifesto, principles 3, 7, 9; what it is not)
2. How a change flows from backlog to production (OL; table)
3. Core engineering practices (table) — H3: TDD; CI and trunk-based development; code review and pair programming; refactoring and simple design; test automation and the pyramid; continuous delivery and feature flags
4. Scrum, XP and Kanban in software teams (table; what each requires)
5. Worked example: test-suite shape and CI feedback time (illustrative)
6. A Definition of Done for a software team, and technical debt
7. Measuring Agile software delivery (DORA five metrics, flow, quality, outcomes)
8. Agile and DevOps
9. AI coding assistants in an Agile team
10. When Agile software development is harder
11. Common mistakes
12. What the project manager does
FAQ (8)

## Planned worked example
Illustrative customer self-service portal, five developers, story US-01 (password reset) from our user story template. Test durations assumed (0.02 s unit, 1.5 s integration, 40 s end-to-end). Compare "ice-cream cone" (300/150/250) vs pyramid (2,400/200/25) suites; commit stage and parallel acceptance stage; daily pipeline load with 10 merges/day. Verified in Python.

## Sources
- Agile Manifesto principles (agilemanifesto.org/principles.html) — inspected
- Scrum Guide 2020 (scrumguides.org) — inspected
- DORA metrics guide (dora.dev/guides/dora-metrics/, updated 5 Jan 2026) — inspected
- DORA trunk-based development and test automation capabilities — inspected
- Fowler, Continuous Integration (18 Jan 2024) — inspected
- Fowler, Test Pyramid bliki (2012) and Vocke, Practical Test Pyramid (2018) — inspected
- Hodgson, Feature Toggles (2017) — inspected
- Beck, Extreme Programming Explained (1999; 2nd ed. with Andres, 2004) — publisher pages inspected
- DORA 2025 State of AI-assisted Software Development (research.google abstract) — inspected
