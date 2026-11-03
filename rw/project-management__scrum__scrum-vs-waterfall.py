from core import S, L, OL, T, TIP, H3

URL = "/project-management/scrum/scrum-vs-waterfall/"

RW = dict(
    title="Scrum vs Waterfall: Differences, Examples and How to Choose",
    desc="Scrum vs Waterfall compared: planning, roles, change, testing and risk, the same project run both ways, a scoring tool for choosing and hybrid options.",
    intro=(
        "Scrum vs Waterfall comes down to when you plan and when you deliver: Waterfall plans the whole project up "
        "front and delivers the result at the end, while Scrum plans in short Sprints and delivers a usable Increment "
        "every Sprint. Neither is better in general; each fits a different kind of work. This guide compares them "
        "point by point, runs the same project both ways and gives you a simple way to choose, combine or switch."
    ),
    takeaways=[
        "Waterfall is a predictive approach: fix the scope, plan it in detail, then build and test in sequence. Scrum is an adaptive framework: fix the Sprint length and team, and let scope evolve through feedback.",
        "In Waterfall, users usually see the working result near the end. In Scrum, stakeholders inspect a usable Increment at every Sprint Review.",
        "Waterfall handles change through formal change requests; Scrum handles it by re-ordering the Product Backlog between Sprints.",
        "Waterfall suits stable requirements, physical or contract-driven work and heavy regulation. Scrum suits uncertain, complex work where early feedback is valuable.",
        "Hybrids are common: Waterfall-style governance and milestones with Scrum teams delivering inside them.",
        "When moving from Waterfall to Scrum, turn the remaining requirements into a Product Backlog and map existing roles to the three Scrum accountabilities.",
    ],
    sections=[
        S("Scrum vs Waterfall: what is the difference?",
          "**The difference between Scrum and Waterfall is how they deal with uncertainty.** Waterfall assumes the "
          "requirements can be known up front, so it plans everything first and completes each phase in sequence. "
          "Scrum assumes you will learn as you go, so it delivers in Sprints of one month or less and adapts the plan "
          "after each one.",
          "PMI describes these as **predictive** and **adaptive** approaches, and a mix of the two as **hybrid**. "
          "Waterfall is the classic predictive life cycle. Scrum is the most widely used adaptive framework, defined "
          "by the 2020 Scrum Guide. Strictly, you are comparing a life cycle model with a framework, but in practice "
          "both answer the same question: how should this project be planned and delivered?",
        ),
        S("Waterfall in brief",
          "In Waterfall, a project moves through fixed phases, typically requirements, design, implementation, "
          "verification, deployment and maintenance. Each phase produces approved deliverables that feed the next, and "
          "a phase gate at the end of each one decides whether the project continues. Scope, schedule and cost are "
          "planned in detail, saved as a [project baseline](/project-management/project-baseline/) and controlled "
          "through formal [change control](/project-management/change-control/).",
          "A project manager usually plans and directs the work, specialists hand work from one phase to the next, "
          "and progress is shown on a [Gantt chart](/project-management/gantt-chart/) against the baseline.",
          "See our full guide to [Waterfall project management](/project-management/waterfall-project-management/) for the phases, gates, a worked example and its pros and cons.",
        ),
        S("Scrum in brief",
          "Scrum is a lightweight framework in which a small, cross-functional Scrum Team, typically ten or fewer "
          "people, delivers value in fixed-length Sprints of one month or less. It has three accountabilities "
          "(Product Owner, Scrum Master and Developers), five events (the Sprint, Sprint Planning, Daily Scrum, Sprint "
          "Review and Sprint Retrospective) and three artifacts (Product Backlog, Sprint Backlog and Increment).",
          "The Product Owner orders the [Product Backlog](/project-management/scrum/product-backlog/) to maximise "
          "value. Each Sprint, the team selects work towards a Sprint Goal, builds a usable Increment that meets the "
          "[Definition of Done](/project-management/agile/definition-of-done/), shows it to stakeholders at the "
          "[Sprint Review](/project-management/scrum/sprint-review/) and improves its own way of working at the "
          "Retrospective. Our guide to [what Scrum is](/project-management/scrum/what-is-scrum/) covers each element "
          "in detail.",
        ),
        S("Scrum vs Waterfall comparison table",
          T(["Aspect", "Waterfall", "Scrum"],
            ["Approach", "Predictive, sequential", "Adaptive, iterative and incremental"],
            ["Planning", "Detailed plan up front, baselined", "Product Goal plus detailed planning each Sprint"],
            ["What is fixed", "Scope; time and cost are estimated from it", "Sprint length and team; scope varies"],
            ["Requirements", "Specification signed off early", "Product Backlog that evolves"],
            ["Delivery", "One release at the end, or a few large ones", "A usable Increment every Sprint"],
            ["Roles", "Project manager, analysts, designers, developers, testers", "Product Owner, Scrum Master, Developers"],
            ["Decision-making", "Project manager and sponsor, through gates", "Product Owner decides what; Developers decide how"],
            ["Change", "Formal change requests and impact assessment", "Re-order the Product Backlog; applies from the next Sprint"],
            ["Testing", "A separate phase after build", "Within every Sprint, to meet the Definition of Done"],
            ["Risk", "Many risks surface late, in integration and testing", "Surfaces early through frequent integration and feedback"],
            ["Stakeholder involvement", "Heavy at the start and at gates", "At every Sprint Review and through the Product Owner"],
            ["Documentation", "Comprehensive, created phase by phase", "Just enough; backlog and Increments are the main record"],
            ["Progress measure", "Planned vs actual, milestones, earned value", "Working Increments, Sprint Goals, burndown and velocity"],
            ["Typical contract", "Fixed price against a specification", "Time and materials, or fixed budget with flexible scope"],
            ["Typical fit", "Construction, infrastructure, regulated rollouts", "Software, digital products, new services"],
          ),
        ),
        S("Pros and cons of Scrum and Waterfall",
          "Each approach's strengths are the mirror image of the other's weaknesses.",
          T(["", "Waterfall", "Scrum"],
            ["Main advantages", "Predictable scope, dates and budget when requirements are stable; clear phases and milestones; thorough documentation for audits and handovers; fits fixed-price contracts; less demand on stakeholders' time", "Early and frequent delivery of value; problems and misunderstandings found within weeks; change absorbed cheaply; quality built in every Sprint; motivated, self-managing teams"],
            ["Main disadvantages", "Late feedback from users; costly change after sign-off; risks found late in testing; no value until the end; assumes requirements can be known early", "Less up-front certainty about final scope and date; needs an empowered Product Owner and regular stakeholder time; harder to fit fixed-price contracts; relies on a dedicated, cross-functional team"],
            ["Biggest risk", "Delivering exactly what was specified, on time, and finding it is not what users need", "Delivering a stream of Increments without a clear Product Goal, so the product drifts"],
            ["How to reduce it", "Prototypes, design walkthroughs with users, phased releases", "A clear Product Goal, an ordered backlog and real stakeholders at every Sprint Review"],
          ),
          "Many of Waterfall's weaknesses come from running a single pass with no feedback, and many of Scrum's come "
          "from adopting the events without the discipline behind them. Both work well when they are applied to the "
          "kind of work they were designed for.",
        ),
        S("The key differences explained",
          H3("Planning"),
          "Waterfall front-loads planning. Before the build starts you have a work breakdown structure, a schedule "
          "with dependencies and a cost estimate. Scrum spreads planning across the project: a long-term Product Goal, "
          "an ordered backlog refined continuously, and detailed planning only for the next Sprint. Scrum still plans; "
          "it just plans at the last responsible moment. See our guide to "
          "[the role of the project plan in Agile](/project-management/agile/role-of-the-project-plan-in-agile/).",
          H3("Scope, time and cost"),
          "Waterfall fixes scope and estimates time and cost from it. Scrum turns this around: the team and Sprint "
          "length fix the cost and cadence, and scope is what flexes, with the most valuable items done first. If the "
          "money or time runs out, a Scrum project stops with the most valuable features already delivered; a "
          "Waterfall project that runs out may have nothing usable yet.",
          H3("Delivery and value"),
          "Waterfall delivers value once, at the end. Scrum requires a usable Increment every Sprint, which can be "
          "released early to some or all users. Early releases bring earlier benefits and real feedback, but only if "
          "the product can be used in parts.",
          H3("Roles and decision-making"),
          "Waterfall usually has a project manager who plans, assigns and controls work, with specialists working "
          "phase by phase. The Scrum Guide has no project manager role. The "
          "[three Scrum accountabilities](/project-management/scrum/scrum-team-roles/) split that job: the Product "
          "Owner decides what to build and in what order, the Developers decide how and manage their own work, and the "
          "Scrum Master improves the team's effectiveness.",
          H3("Handling change"),
          "In Waterfall, a change after sign-off goes through a change request, an impact assessment and a decision "
          "by the change authority, because it may ripple through design, build and test. In Scrum, new ideas go into "
          "the Product Backlog and the Product Owner re-orders it; the change takes effect from the next Sprint. "
          "Scrum does not make change free. It makes it cheaper by keeping the unbuilt part of the plan light.",
          H3("Testing and quality"),
          "Waterfall tests in a dedicated phase after the build, so defects and misunderstood "
          "requirements are often found late. In Scrum, work is not done "
          "until it meets the Definition of Done, which normally includes testing, so quality is built in every "
          "Sprint. Waterfall testing time is also the first thing squeezed when earlier phases overrun.",
          H3("Risk"),
          "Waterfall reduces risk through analysis, design reviews and contingency. Scrum reduces it through short "
          "feedback loops: technical risks surface when the team integrates working software every Sprint, and "
          "product risks surface when stakeholders inspect the Increment.",
          H3("Documentation and reporting"),
          "Waterfall produces requirements specifications, design documents, test plans and status reports at each "
          "phase. Scrum favours just enough documentation, with the Product Backlog, Increment and Sprint Review as "
          "the main sources of truth. Regulated Scrum teams still produce the documents auditors need, often as part "
          "of the Definition of Done.",
        ),
        S("Scrum vs Agile vs Waterfall",
          "These three terms are often compared as if they were equals, but they are not the same kind of thing.",
          L(
            "**Agile** is a mindset and set of values and principles, set out in the 2001 Agile Manifesto.",
            "**Scrum** is one specific framework for working in an Agile way. Kanban, Extreme Programming and others are alternatives.",
            "**Waterfall** is a predictive life cycle, the opposite end of the spectrum from Agile.",
          ),
          "So Scrum vs Waterfall compares a specific Agile framework with a predictive approach. For the broader "
          "comparison see [Agile vs Waterfall](/project-management/agile/agile-vs-waterfall/); for how Scrum relates to "
          "Agile, see [Agile vs Scrum](/project-management/agile/agile-vs-scrum/); and if you are considering a "
          "flow-based option, our Kanban guides compare it with both.",
        ),
        S("Worked example: the same project run both ways",
          "The following example is **illustrative**: the organisation, durations and figures are invented to show "
          "how the two approaches behave on the same project.",
          "A housing association with 8,000 tenants wants an online portal where tenants can report repairs, pay rent "
          "and update their details. The budget allows a team of seven for about six months. Tenants have never had "
          "online services before, so nobody is sure which features they will use most.",
          H3("Run as Waterfall"),
          T(["Phase", "Weeks", "What happens"],
            ["Requirements", "1 to 5", "Workshops with housing officers; 140 requirements signed off"],
            ["Design", "6 to 9", "Screen designs, integration design for the housing and payments systems"],
            ["Build", "10 to 19", "All three features built in parallel"],
            ["Test", "20 to 23", "System testing, then user acceptance testing with 20 tenants"],
            ["Deploy", "24 to 26", "Launch to all tenants"],
          ),
          "In week 16, housing officers ask for tenants to be able to upload photos with repair reports, because "
          "contractors keep arriving without the right parts. The project manager raises a change request. The impact "
          "assessment shows changes to the signed-off design, the build and the test scripts, adding about three "
          "weeks. The change board approves it and moves the launch to week 29. In UAT, tenants find the rent payment "
          "journey confusing; fixing it adds another two weeks.",
          H3("Run as Scrum"),
          T(["Sprints (2 weeks each)", "Sprint Goal", "What is released"],
            ["1 to 3", "Tenants can report a repair online", "Repairs reporting, released to a pilot of 300 tenants after Sprint 3"],
            ["4 to 6", "Tenants can pay rent online", "Rent payment, released to the pilot; feedback reshapes the journey in Sprint 6"],
            ["7 to 8", "Repair reports include photos", "Photo upload, added to the backlog after pilot feedback and ordered first"],
            ["9 to 11", "All tenants can use the portal", "Wider release, accessibility fixes, update-details feature"],
            ["12", "Improve based on live use", "Highest-value fixes from live data"],
          ),
          "The photo request arrives in Sprint 6 from pilot users and housing officers. The Product Owner orders it "
          "above \"update your details\", which tenants have rarely asked for. Nothing already built has to change. At "
          "the end of six months, update-details is simpler than first planned, which the sponsor accepts because "
          "repairs and rent were working months earlier.",
          H3("Comparing the outcomes"),
          T(["Measure", "Waterfall", "Scrum"],
            ["First tenant use", "Week 26 (moved to week 31 after changes)", "Week 7 (pilot)"],
            ["Photo upload change", "Change request, three-week delay", "Re-ordered in the backlog, no rework"],
            ["Usability problems found", "In UAT, near the end", "In the pilot, Sprint 5"],
            ["What flexed", "Time and cost", "Scope of a low-value feature"],
            ["Up-front certainty", "High: dates and scope agreed early", "Lower: scope agreed Sprint by Sprint"],
          ),
          "Scrum fits this project because the value is uncertain and the portal is useful in parts. Change the "
          "facts, though, and the answer changes: a fixed-price contract with a regulator-approved specification, or "
          "an office move with a hard lease date, would favour Waterfall.",
        ),
        S("When Waterfall is the better choice",
          L(
            "**Requirements are stable and well understood**, for example a payroll system dictated by legislation.",
            "**The output only has value when complete**: a bridge, a data centre move or an office relocation.",
            "**Late change is very expensive**, because work is physical or manufacturing tooling is involved.",
            "**Contracts or regulation require approved stages**, such as fixed-price public procurement or validated systems.",
            "**The team has delivered similar projects many times** and the method is proven.",
            "**Stakeholders are only available at key points**, not every few weeks.",
          ),
        ),
        S("When Scrum is the better choice",
          L(
            "**The solution is uncertain** and needs discovery, such as a new digital product or service.",
            "**The product is useful in increments**, so early releases bring early value and feedback.",
            "**Users and stakeholders can give regular feedback** at Sprint Reviews.",
            "**Speed to market matters** more than delivering everything at once.",
            "**Technology is new or changing**, so technical risk is best reduced by building and integrating early.",
            "**A small, cross-functional, stable team** can be dedicated to the work.",
          ),
        ),
        S("How to choose between Scrum and Waterfall",
          "Use these steps for a new project, or at a phase boundary on an existing one.",
          OL(
            "**Describe the end result.** Write one paragraph on what will exist when the project is finished and who will use it.",
            "**List the fixed constraints.** Note hard dates, fixed budgets, contracts, regulatory approvals and physical dependencies.",
            "**Score the project.** Rate each factor in the table below from 1 to 5.",
            "**Look for splits.** Different parts of the project may score differently, for example hardware versus software.",
            "**Check the organisation.** Can you provide a Product Owner with authority, a dedicated team and stakeholders for Sprint Reviews? If not, Scrum will struggle until you can.",
            "**Decide and record why.** Note the approach and reasons in the [project charter](/project-management/project-charter/) so it can be revisited.",
          ),
          T(["Factor", "1 (leans Waterfall)", "5 (leans Scrum)"],
            ["Requirement clarity", "Fully known and stable", "Unclear or likely to change"],
            ["Value in parts", "Only useful when complete", "Useful in small increments"],
            ["Cost of late change", "Very high", "Low"],
            ["Contract", "Fixed price, fixed specification", "Time and materials or flexible scope"],
            ["Regulation", "Formal stage approvals required", "Lighter documentation acceptable"],
            ["Stakeholder availability", "Only at milestones", "Every few weeks"],
            ["Technology", "Mature and well understood", "New or experimental"],
            ["Team set-up", "Specialists shared across projects", "Dedicated, cross-functional team"],
          ),
          "Add up the eight scores. As a rule of thumb, **8 to 18** points to Waterfall, **19 to 29** to a hybrid and "
          "**30 to 40** to Scrum. These bands are a starting point for discussion, not a formula. The tenant portal "
          "above scored 5, 5, 4, 3, 3, 4, 3 and 4, a total of 31, which supports using Scrum. A fixed-date office move "
          "might score 1, 1, 1, 2, 2, 2, 1 and 2, a total of 12.",
        ),
        S("Hybrid approaches: combining Scrum and Waterfall",
          "Many organisations combine the two rather than choose. The most common patterns are:",
          T(["Pattern", "How it works", "Works well when"],
            ["Scrum inside phase gates", "Funding, milestones and gates are predictive; delivery between gates runs in Sprints", "Governance needs gates but the solution needs feedback"],
            ["Water-scrum-fall", "Requirements and funding up front, build in Sprints, then a formal release and deployment phase", "Release processes or operations teams are not yet Agile"],
            ["Split by workstream", "Hardware, construction or procurement run as Waterfall; software runs as Scrum", "Some parts are physical and some are digital"],
            ["Predictive programme, Scrum projects", "The programme plan sets major dates; each team uses Scrum", "Large change programmes with several teams"],
          ),
          "To make a hybrid work, agree where the boundary sits, which dates are fixed and which scope can flex, and "
          "how Sprint progress rolls up into milestone reporting. Use [release planning](/project-management/agile/agile-release-planning/) "
          "to connect Sprints to milestones. The risk is getting the worst of both: heavy up-front specifications "
          "that remove Scrum's flexibility, plus Sprints that never release. Methods such as "
          "[PRINCE2](/project-management/prince2/) explicitly support Agile delivery within management stages.",
        ),
        S("How to move from Waterfall to Scrum, step by step",
          "You can switch at any point, but a phase boundary, often after design, is the easiest place.",
          OL(
            "**Agree why you are switching.** Name the problem Scrum should solve, such as late feedback or frequent change.",
            "**Appoint a Product Owner.** Choose one person with the authority to order the work and access to stakeholders, often the business lead or senior analyst.",
            "**Form the Scrum Team.** Bring designers, developers and testers into one team of ten or fewer, and choose a Scrum Master.",
            "**Convert remaining requirements into a Product Backlog.** Rewrite open requirements as backlog items with acceptance criteria. Our [product backlog template](/templates/product-backlog-template/) helps.",
            "**Order the backlog by value and risk.** Put high-value and high-risk items first.",
            "**Write a Definition of Done.** Include testing, documentation and any regulatory evidence previously produced in later phases.",
            "**Agree Sprint length and run the first Sprint.** Two weeks is common. Keep the Sprint Review open to the sponsors who used to attend gates.",
            "**Reconnect governance.** Agree with the sponsor how Sprint Reviews and release plans replace or feed phase-gate reporting.",
            "**Inspect and adapt the transition.** Use the first few Retrospectives to fix what is not working.",
          ),
          TIP("Do not convert a signed-off specification into a backlog and treat it as fixed. The point of switching "
              "is that the Product Owner can re-order, split and drop items as you learn."),
          "Read our guide on [how to implement Agile](/project-management/agile/how-to-implement-agile/) for the wider organisational changes.",
        ),
        S("Mapping Waterfall roles and documents to Scrum",
          "The Scrum Guide does not say what happens to existing job titles; organisations decide. These mappings are "
          "common starting points, not rules.",
          T(["Waterfall role", "Common move in Scrum"],
            ["Project manager", "Product Owner, Scrum Master, or a delivery or programme role outside the team handling budgets, contracts and reporting"],
            ["Business analyst", "Developer focused on refinement, or supports the Product Owner"],
            ["Designers, developers, testers", "Developers in one cross-functional Scrum Team"],
            ["Test manager", "Developer with a quality focus; shapes the Definition of Done"],
            ["Sponsor and steering group", "Key stakeholders at Sprint Reviews; set the Product Goal and budget"],
          ),
          T(["Waterfall document", "Scrum equivalent"],
            ["Requirements specification", "Product Backlog with acceptance criteria"],
            ["Project plan and Gantt chart", "Product Goal, release plan and Sprint Backlog"],
            ["Change request", "New or re-ordered Product Backlog item"],
            ["Status report", "Sprint Review, burndown and release forecast"],
            ["Test plan and sign-off", "Definition of Done and acceptance criteria"],
            ["Lessons learned", "Sprint Retrospective, every Sprint"],
          ),
        ),
        S("Common mistakes when comparing or switching",
          L(
            "**Choosing by fashion.** Picking Scrum because it is popular, or Waterfall because it is familiar, ignores the project's actual characteristics.",
            "**Assuming Scrum means no planning.** Scrum plans continuously; teams without a Product Goal or ordered backlog are just busy.",
            "**Assuming Waterfall means no feedback.** Prototypes, design walkthroughs and phased releases bring feedback into predictive projects.",
            "**Mini-waterfalls inside Sprints.** Design in Sprint 1, build in Sprint 2, test in Sprint 3 is not Scrum. Each Sprint must produce a done Increment.",
            "**No real Product Owner.** A committee or a proxy without authority slows every decision.",
            "**Fixing scope, time and cost in a Scrum project.** If everything is fixed, Scrum loses its main lever. Agree what can flex.",
            "**Letting scope creep into Waterfall.** Informal additions accumulate into delays; route every change through change control.",
            "**Keeping both sets of paperwork.** Teams that produce Waterfall reports and Scrum artifacts get the overhead of both. Agree which reports Scrum artifacts replace.",
          ),
        ),
        S("Tools for Scrum, Waterfall and hybrid projects",
          "Waterfall projects need strong Gantt charts, dependencies and baselines; Scrum teams need backlogs, boards "
          "and Sprint planning. Hybrid teams need both in one place.",
          L(
            "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool, includes interactive Gantt charts with dependencies, the critical path and baselines from the Team plan, plus Kanban boards on every plan, so a phase plan and team boards can sit together. That makes it a strong option for hybrid portfolios and PMOs.",
            "**[Jira](/project-management-tools/jira/)** is the most complete Agile tool for software teams that we review, with backlogs, sprints, story points and boards. It has no classic Gantt chart with critical path and baselines, so pair it with a planning tool for Waterfall work.",
            "**[Smartsheet](/project-management-tools/smartsheet/)** combines a spreadsheet grid with Gantt charts and dependencies, which suits plan-driven teams.",
            "**[monday.com](/project-management-tools/monday/)**, **[ClickUp](/project-management-tools/clickup/)** and **Asana** all offer timeline or Gantt views alongside boards, and suit teams running both kinds of work.",
            "**Templates.** Start with our [Gantt chart template](/templates/gantt-chart-template/) for Waterfall work and our [Sprint planning template](/templates/sprint-planning-template/) for Scrum.",
          ),
          "See our comparison of [Scrum software tools](/project-management/scrum/scrum-software-tools/) for more options.",
        ),
    ],
    faq=[
        ("What is the main difference between Scrum and Waterfall?",
         "Waterfall completes requirements, design, build and test in sequence and delivers at the end. Scrum delivers "
         "a usable Increment every Sprint and adapts the plan based on feedback."),
        ("Which is better, Scrum or Waterfall?",
         "It depends on the work. Scrum suits uncertain, changing requirements and products that are useful in parts; "
         "Waterfall suits stable, well-understood work, physical builds and regulated projects needing staged approvals."),
        ("Which is faster, Scrum or Waterfall?",
         "Scrum usually delivers usable results much sooner because it releases in increments. Total duration depends "
         "on scope and team, and Scrum often finishes by trimming low-value scope rather than building everything."),
        ("Which is cheaper, Scrum or Waterfall?",
         "Neither automatically. Scrum can reduce waste by stopping low-value work early and finding problems sooner; "
         "Waterfall can be efficient when requirements are stable. Total cost depends on scope, team and context."),
        ("Is Scrum the same as Agile?",
         "No. Agile is a set of values and principles; Scrum is one framework for applying them. Kanban and Extreme "
         "Programming are other Agile approaches."),
        ("What is the difference between a Sprint and a Waterfall phase?",
         "A Sprint is a fixed time-box of one month or less that produces a usable Increment and includes all the work "
         "needed, from refinement to testing. A Waterfall phase covers one type of work, such as design, and ends when "
         "its deliverables are approved."),
        ("Is there a project manager in Scrum?",
         "The Scrum Guide has no project manager role. Its responsibilities are shared between the Product Owner, "
         "Developers and Scrum Master. Many organisations keep a delivery or programme role outside the team for "
         "budgets, contracts and reporting."),
        ("How is testing different in Scrum and Waterfall?",
         "In Waterfall, testing is usually a separate late phase. In Scrum, testing happens within every Sprint so each "
         "Increment meets the Definition of Done."),
        ("How does documentation differ in Scrum and Waterfall?",
         "Waterfall relies on detailed documents created phase by phase. Scrum favours just enough documentation, with "
         "the Product Backlog and working Increments as the main sources of truth."),
        ("How are changes handled in Scrum vs Waterfall?",
         "Waterfall handles changes through formal change requests and impact assessment. Scrum handles them by "
         "re-ordering the Product Backlog, so changes take effect from the next Sprint."),
        ("Can Scrum and Waterfall be combined?",
         "Yes. Common hybrids use predictive governance, budgets and milestones with Scrum teams delivering inside "
         "them, or run hardware and construction as Waterfall and software as Scrum."),
        ("Can a project switch from Waterfall to Scrum midway?",
         "Yes. It works best at a phase boundary: appoint a Product Owner, form a cross-functional team, turn the "
         "remaining requirements into a Product Backlog and agree how Sprint Reviews feed governance."),
        ("Is Scrum or Waterfall better for construction projects?",
         "Physical construction usually follows a predictive approach because the build sequence is fixed and late "
         "change is expensive. Scrum ideas can still help in design, fit-out planning and internal work."),
    ],
)
