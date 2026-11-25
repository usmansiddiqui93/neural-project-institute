# Brief: /project-management/project-baseline/

Prepared 25 November 2026 under RW_BRIEF.md v2 and FRAMEWORK.md V1.0.

## Inventory and duplicate check (§30)
- Live page (21 Sep 2026, ~780 words): accurate but thin. Keeps: three baselines table, PMB link to EVM, set/use/re-baseline outline, MR outside the cost baseline, Agile answer, tool FAQ. Fix: tool FAQ names Smartsheet (our Smartsheet review page does not mention baselines) and says "Microsoft Planner premium plans" (our Planner review says baselines are on Plan 3 only).
- Parent cluster: project planning and control (/project-management/project-management-plan/, /project-management/project-integration-management/).
- Overlapping intent / pages to link rather than repeat:
  - /project-management/project-management-plan/ has a short "Baselines" table (same three rows). Our page is the deep dive; link from there is already present.
  - /project-management/change-control/ owns the change process and authority levels. Do not repeat; link.
  - /project-management/project-budget/ owns the budget build-up layers (contingency, cost baseline, MR). We show the same layers only as part of a different scenario and link.
  - /project-management/cost-control/ has "When to change the cost baseline" (one paragraph). We go deeper on re-baselining types; link.
  - /project-management/earned-value-management/ and /project-management/s-curve/ use a $200,000/8-month example; /project-management/schedule-variance/ uses a $400,000 CRM. /project-management/cost-management-plan/ already uses a "warehouse system rollout" ($1.2M), so we switched away from a first-draft warehouse scenario. Our scenario is new: an illustrative £ housing association repairs management system replacement. No reuse of their numbers.
  - /project-management/configuration-management/ (rewritten in the same session) uses the same repairs-system scenario and change CR-07, deliberately, so the two pages connect; different calculations and focus.
- Templates checked (pages read): change-request-template (change log 12 columns + 12-field form; expert version adds revision history tab), project-schedule-template (tip "Baseline the schedule once approved"; no baseline columns), project-cost-estimate-template (states approved estimate becomes cost baseline; contingency inside, MR outside), budget-template (planned vs actual, variance), project-plan-template ("Review and baseline" step), work-breakdown-structure-template. No dedicated baseline template exists: do not imply one.

## Search intent
Primary: definition ("what is a project baseline"), with how-to (setting and re-baselining) and worked-example sub-intents. Answer in the intro.

## Keywords
- Primary: project baseline
- Secondary (16): what is a project baseline; baseline in project management; scope baseline; schedule baseline; cost baseline; performance measurement baseline; PMB; re-baselining; rebaseline vs replan; baseline vs forecast; management reserve and cost baseline; contingency reserve; baseline execution index (BEI); over target baseline; baseline in MS Project / Gantt baseline; baseline in Agile; how to set a project baseline; baseline change log.

## Audience and level
Intermediate: project managers and coordinators who know a schedule and budget, PMP/CAPM candidates, PMO analysts.

## SERP findings (WebSearch 25 Nov 2026; Atlassian and PMI library result opened)
- Atlassian "project baseline" page: scope/schedule/cost elements, Confluence/Jira example, benefits. Gaps: no numbers, no PMB vs budget, no re-baselining governance, no EVM link.
- Vendor blogs (Asana, ClickUp) similar: definitions and benefits, little governance.
- Gaps we fill: budget layers with a reserve calculation; baseline vs current plan vs forecast vs target table; re-baselining vs replanning (with US DoD/GAO terms OTB/OTS); what a quiet re-baseline does to SV/CV (calculated); BEI as a schedule-baseline check (calculated); baseline log with versions; contingency drawdown vs management-reserve release; Agile equivalents.

## SEO
- Title (≤60): What Is a Project Baseline? Scope, Schedule and Cost (51)
- Meta (≤155): see record.

## Outline
1. What is a project baseline? (definition 40–60 words; PMI Lexicon wording; what it is not)
2. The three baselines and the performance measurement baseline (table; PMI vs PMBOK 6 components; EVMS PMB note)
3. Baseline, current plan, forecast and target (comparison table)
4. How reserves relate to the cost baseline (contingency inside, MR outside; convention note)
5. How to set a project baseline (OL steps with entry criteria)
6. Worked example: baselining a repairs system replacement (H3: build-up; schedule baseline; month-3 status; BEI)
7. Changing a baseline: approved change, replanning and re-baselining (H3: what counts as a baseline change; replan vs re-baseline; OTB/OTS; quiet re-baseline table; baseline log v1.0–v1.2)
8. Baselines in Agile and hybrid projects
9. Baselines in PRINCE2
10. Baselines in scheduling tools (MS Project 11 baselines; tools per our review pages)
11. Common mistakes
12. FAQs

## Internal links (planned, all in en_urls.txt)
project-management-plan, project-scope, work-breakdown-structure, project-scheduling, critical-path-method, cost-estimation, project-budget, cost-management-plan, earned-value-management, schedule-variance, cost-variance, cost-performance-index, estimate-at-completion, s-curve, change-control, configuration-management, cost-control, scope-creep, risk-register, contingency-plan, gantt-chart, project-milestones, integrated-master-plan, agile/agile-release-planning, prince2, project-forecasting; templates: change-request-template, project-schedule-template, project-cost-estimate-template.

## Worked examples (illustrative, one scenario)
Repairs system replacement: five work packages £290k time-phased over six months (Jan–Jun 2027); contingency from two risks by expected value (0.40×£50k + 0.25×£40k = £30k); cost baseline £320k; MR 5% = £16k; project budget £336k. Month-3 status PV £115k / EV £106k / AC £121k → SV, CV, SPI, CPI, SV%, CV%. BEI 21/24. CR-07 mobile app for repair operatives (+£24k, +2 weeks). Contingency transfer £10k. MR release £8k (single sign-on incompatibility). All verified in Python.

## Sources to cite / inspect
- PMI Lexicon of Project Management Terms v4.0 (2024) — opened (Colorado College copy).
- US DoD EVM definitions (acq.osd.mil) — opened: PMB, MR, UB, CBB, OTB, OTS, internal replanning, formal reprogramming, BEI.
- GAO Cost Estimating and Assessment Guide: Overtarget baselines and schedules (gaoinnovations.gov) — opened.
- Microsoft Support "Set and save a baseline" — opened (11 baseline sets, Project Online/Server page).
- Elecosoft Powerproject BEI help page — opened (suggested 1.00 pass / 0.95 fail boundaries).
- Knowledge Train PRINCE2 7 glossary and management products pages — opened (secondary; official PeopleCert manual not accessed).
- Our tool review pages for Wrike, ClickUp, Microsoft Planner, monday.com baseline support.
