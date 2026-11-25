# Content Brief: What Is DevOps?

URL (unchanged): `/project-management/kanban/devops/`
Brief date: 25 November 2026
Writer brief: RW_BRIEF.md v2 / FRAMEWORK.md V1.0

## Why this page is being rewritten
The live page (published 19 September 2026, about 1,000 words including FAQs) is accurate on origins, CALMS and the Three Ways, but it lists DORA's **old four metrics** ("time to restore service") in the body, a takeaway and an FAQ. FOLLOWUPS.md flags this. DORA's current model (dora.dev, guide last updated 5 January 2026) has **five** software delivery metrics in two groups. The site's Agile metrics guide, continuous delivery guide, Agile IT operations guide and software project management guide already use the five-metric model; this page must match them. The live page is also thin: no definition block, no explanation of how the practices connect, no worked example, no limitations, no guidance for project managers.

Keep from the live page: origins (Debois, DevOpsDays Ghent 2009), CALMS table, Three Ways, practice list, blameless reviews, FAQ themes (role vs culture, DevOps vs Agile, DevOps vs continuous delivery, DevOps engineer, CALMS meaning).

## Primary keyword
what is DevOps

## Secondary keywords (16)
- DevOps meaning / DevOps definition
- DORA metrics / five DORA metrics
- failed deployment recovery time
- deployment rework rate
- change lead time, change fail rate, deployment frequency
- CALMS framework DevOps
- Three Ways of DevOps
- DevOps principles
- DevOps practices
- DevOps vs Agile
- DevOps vs SRE (site reliability engineering)
- DevSecOps
- platform engineering
- DevOps and Kanban
- DevOps change approval / change advisory board
- DevOps for project managers

## Search intent
Primarily **definition** ("what is DevOps"), with a strong secondary **methodology** intent (principles, practices, how it is measured). A third group searches specifically for "DORA metrics" and lands here from the FAQ; they need the current five metrics with dates. Answer the definition in the intro and in a 40–60 word definition block directly under the first H2.

## Learning level and audience
Beginner to intermediate. Project managers, delivery leads, Scrum Masters and Kanban practitioners who work alongside software and operations teams; PM students; IT managers. Readers are not assumed to be engineers, so technical practices are explained by what they achieve.

## SERP findings (WebSearch "what is DevOps", 25 Nov 2026)
Top results: AWS, Microsoft Azure, Red Hat, Atlassian, GitHub, GitLab, IBM, Cisco, Wikipedia, Coursera, CMU SEI. Fetched for structure (wording not reused):
1. **AWS "What is DevOps?"**: definition, how it works, six benefits, adoption, then one H2 per practice (CI, CD, microservices, IaC, monitoring, collaboration), tools. No DORA metrics, no history, no limitations, no worked example; AWS-centric tooling.
2. **Red Hat "What is DevOps?"**: definition, culture, DevOps engineer, practices (CI/CD, IaC, microservices, platform engineering), adoption challenges, containers/Kubernetes, DevSecOps, product promotion. No DORA, no CALMS, no Three Ways, no history.
3. **Wikipedia "DevOps"**: history timeline (DevOpsDays 2009, State of DevOps 2012, DORA metric changes 2023/2024, 2025 archetypes), Bass/Weber/Zhu definition.
4. **Atlassian CALMS page**: credits CALMS to Jez Humble, no date.

Gaps we fill: current five DORA metrics with the 2023 and 2024 changes and a calculated example that shows counting rules (which deployment counts as a failure, which as rework); how the practices map to the Three Ways; DevOps vs Agile vs SRE vs platform engineering vs ITIL in one table; what changes for project managers (change approval evidence from DORA 2019, release planning, risk); limitations and when DevOps practices are constrained; 2025 DORA finding on AI as an amplifier; connection to Kanban flow.

## Duplicate / cannibalisation check (llms.txt + stats.py)
Overlapping pages and how we differentiate:
- `/project-management/kanban/continuous-delivery/`: owns CI vs CD vs continuous deployment, pipeline, release strategies, the "monthly release window" worked example and the DORA-to-Kanban mapping table. We link to it and do **not** repeat the release-window example or the mapping table.
- `/project-management/agile/agile-metrics-and-kpis/`: owns the DORA table with a 40-deployment change-fail/rework example. We keep the same five names, groups and dates, and use a **different** example (20-deployment log with lead time percentiles, recovery time median vs mean, and counting rules).
- `/project-management/industries/software-project-management/`: also has a 40-deployment DORA example; ours differs.
- `/project-management/agile/agile-operations-it/`: owns Kanban for ops teams, ITIL change enablement, error budgets, SRE details. Link, do not repeat.
- `/project-management/kanban/value-stream-mapping/`, `/lean-kanban/`, `/wip-limits/`, `/visual-management/`: linked for the Lean side.
Consistency facts: five metrics; MTTR renamed failed deployment recovery time in 2023; deployment rework rate added in 2024; throughput = change lead time, deployment frequency, failed deployment recovery time; instability = change fail rate, deployment rework rate. Note for follow-up: `/project-management/agile/agile-software-development/` still lists four metrics (outside this task; not edited).

## SEO title (H1)
What Is DevOps? Principles, Practices and DORA Metrics (53 chars)

## Meta description
DevOps explained: what it is, where it came from, CALMS and the Three Ways, core practices, the five DORA metrics with a worked example, and what PMs do. (≈153 chars)

## Outline
- H2 What is DevOps? (definition block; what it is not: not a job title only, not a toolset, not a framework with a rulebook)
  - H3 The problem DevOps set out to solve (conflicting incentives, hand-offs)
- H2 Where DevOps came from (2008 Agile conference / Debois; Velocity 2009 talk not claimed; DevOpsDays 30–31 Oct 2009 Ghent; Three Ways 2012; Phoenix Project 2013; State of DevOps reports; DORA; Accelerate 2018)
- H2 DevOps principles: CALMS and the Three Ways (CALMS table; Three Ways table with practices that implement each)
- H2 Core DevOps practices (table: practice, what it does, which Way it serves; link CI/CD guide)
- H2 How DevOps fits with Agile, Lean, Kanban, SRE and ITIL (comparison table)
  - H3 DevOps and Kanban
  - H3 DevSecOps and platform engineering
- H2 How DevOps performance is measured: the five DORA metrics (table, history 2014→2015→2023→2024, reliability not a delivery metric, speed and stability move together, pitfalls)
- H2 Worked example: calculating DORA metrics from a deployment log (illustrative; counting rules; median vs mean; P85; decision)
- H2 How to start a DevOps improvement (DORA's improvement loop, adapted)
- H2 What DevOps changes for project managers (change approval: DORA 2019 finding; release planning; risk; reporting)
- H2 AI and DevOps: what the 2025 DORA research found
- H2 Limitations and when DevOps is harder to apply
- H2 Common DevOps mistakes
- FAQ (10–12)

## Planned internal links (all in en_urls.txt)
Kanban hub, continuous delivery, value stream mapping, lean kanban, WIP limits, visual management, cycle time vs lead time, kanban metrics, flow efficiency, theory of constraints, Agile metrics and KPIs, Agile IT operations, Agile software development, Agile manifesto, software project management, change control, sprint retrospective, lessons learned, SLA, templates: kanban board, release plan, root cause analysis, change request.

## FAQs
Is DevOps a role or a culture? What is DevOps in simple terms? When did DevOps start? What does CALMS stand for? What are the DORA metrics? Why did DORA replace time to restore service? What are the Three Ways? Is DevOps part of Agile? DevOps vs continuous delivery? DevOps vs SRE? What does a DevOps engineer do? What is a blameless post-incident review?

## Worked example
Illustrative: a team running one customer-facing service logs 20 production deployments in four weeks (20 working days). Compute deployment frequency, change lead time median and nearest-rank 85th percentile, change fail rate, deployment rework rate, failed deployment recovery time (median vs mean). Interpret and choose one constraint to improve (code review waiting). All numbers verified in Python (see record).

## Sources to cite / inspected
- dora.dev, "DORA's software delivery performance metrics" guide (last updated 5 Jan 2026) — inspected.
- dora.dev, Nathen Harvey, "A history of DORA's software delivery metrics" (2 Jan 2026) — inspected.
- dora.dev research index (latest report 2025; no 2026 report listed) — inspected.
- dora.dev capabilities: streamlining change approval (2019 finding; updated 30 Oct 2025), working in small batches, capability list — inspected.
- Google Cloud blog, "Announcing the 2025 DORA report" (23 Sep 2025) — inspected.
- Gene Kim, "The Three Ways: The Principles Underpinning DevOps", IT Revolution (22 Aug 2012) — inspected.
- Patrick Debois, DevOpsDays '09 announcement (Google Groups, 22 Jul 2009; event 30–31 Oct 2009, Ghent) — inspected.
- Google SRE Workbook, "How SRE Relates to DevOps" — inspected.
- Atlassian CALMS page (credits Jez Humble) — inspected; DWP Digital blog (25 Mar 2019) on CALMS — inspected.
- AWS and Red Hat "What is DevOps" pages — inspected for SERP structure only.
