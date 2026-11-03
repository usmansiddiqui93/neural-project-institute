from core import S, L, OL, T, TIP, H3

URL = "/project-management/agile/agile-pmo/"

RW = dict(
    title="Agile PMO: Roles, Services and How to Build One",
    desc="An Agile PMO enables value delivery instead of policing projects. Learn its services, roles, metrics, governance and how to transform a traditional PMO.",
    intro=(
        "An Agile PMO is a project, programme or portfolio management office that helps Agile teams deliver value "
        "by coordinating portfolio decisions, lightweight governance, flow metrics and coaching, rather than by "
        "enforcing detailed plans and stage gates. This guide explains how it differs from a traditional PMO, the "
        "services and roles inside one, how it works in SAFe, and a step-by-step plan to transform the PMO you "
        "already have."
    ),
    takeaways=[
        "An Agile PMO exists to help value flow from strategy to customers; it coordinates and enables rather than polices.",
        "Its core services are portfolio prioritisation, Lean funding and guardrails, dependency management, flow and outcome metrics, and coaching.",
        "Stage gates and RAG reports give way to regular reviews of working product, forecasts and outcome data.",
        "In SAFe the same function is called a value management office (VMO) and facilitates Lean Portfolio Management.",
        "Transform gradually: agree a new purpose, pilot with a few teams, replace one control at a time and measure the result.",
        "The biggest mistake is renaming the PMO without changing what it asks teams to do.",
    ],
    sections=[
        S(
            "What is an Agile PMO?",
            "An **Agile PMO** is a project, programme or portfolio management office redesigned for organisations "
            "that deliver through Agile teams. Instead of approving detailed plans and chasing status reports, it "
            "helps leaders choose and fund the right work, keeps governance light, connects teams that depend on "
            "each other, and measures flow and outcomes.",
            "You will also see it called an **Agile programme management office (APMO)**, a **Lean PMO**, a "
            "**portfolio office** or, in the Scaled Agile Framework, a **value management office (VMO)**. The names "
            "differ, but the shift is the same: from controlling projects to enabling the flow of value.",
            "If you are new to PMOs in general, start with our guide to the "
            "[project management office (PMO)](/project-management/project-management-office-pmo/), which covers "
            "the supportive, controlling and directive types, PMO levels and how to set one up. The "
            "[PMBOK Guide](/project-management/pmbok-guide/) 8th edition, published by PMI in November 2025, has an "
            "appendix on PMOs and describes the PMO moving from a process-focused unit towards a partner tailored to "
            "strategy, which is close to what an Agile PMO aims to be.",
            H3("What an Agile PMO is not"),
            L(
                "**Not a team that runs sprints.** Scrum Teams manage their own work; the Agile PMO works at portfolio and cross-team level.",
                "**Not a reporting factory.** It does not ask teams to retype data that already lives in their tools.",
                "**Not a rename.** A PMO that keeps every old template and gate but adds \"Agile\" to its name has not changed.",
            ),
        ),
        S(
            "Agile PMO vs traditional PMO",
            "The table below sets out the main differences. Most real PMOs sit somewhere between the two columns, "
            "and the direction of travel matters more than the label.",
            T(
                ["Aspect", "Traditional PMO", "Agile PMO"],
                ["Purpose", "Control and compliance of projects", "Enabling value delivery across the portfolio"],
                ["Unit of work", "Temporary projects", "Long-lived products, value streams and epics"],
                ["Planning", "Detailed plans approved up front", "Rolling roadmaps and quarterly planning, detail added just in time"],
                ["Funding", "Budget approved per project", "Funding for teams or value streams, steered by guardrails"],
                ["Governance", "Stage gates and sign-offs", "Lightweight guardrails and regular reviews of working results"],
                ["Reporting", "Status reports and RAG ratings", "Live dashboards, flow metrics, forecasts and outcomes"],
                ["Change", "Formal change control to protect the baseline", "Reprioritising the backlog is normal and cheap"],
                ["Relationship with teams", "Oversight and audit", "Service, facilitation and coaching"],
                ["Measure of success", "On time, on budget, to scope", "Outcomes achieved, flow predictability and customer value"],
            ),
            H3("What stays the same"),
            "An Agile PMO still answers the same executive questions: are we doing the right work, will it be ready "
            "when needed and is money well spent? What changes is **how** the answers are produced: from working "
            "product and live data rather than plans and opinions.",
        ),
        S(
            "Why an Agile organisation still needs a PMO",
            "Agile frameworks such as Scrum describe how a team works. They say little about how 20 or 200 teams share "
            "a budget, agree priorities or coordinate a release. Those gaps appear quickly when an organisation scales "
            "Agile but leaves the old PMO untouched:",
            L(
                "**Dual reporting.** Teams update their board for the sprint and then fill in a separate status template for the PMO.",
                "**Project funding fights team stability.** Each new project needs a business case and a new team, so stable Agile teams are broken up.",
                "**Invisible dependencies.** Teams plan independently and discover late that they need something from each other.",
                "**Too much work in progress.** Every request is approved, nothing is stopped, and lead times grow.",
            ),
            "An Agile PMO solves these portfolio problems so that teams can stay focused on delivery. It is often the "
            "function that makes an [Agile transformation](/project-management/agile/agile-transformation/) stick "
            "beyond the first few pilot teams.",
            H3("When you may not need one"),
            "A single product with two or three teams usually manages without a formal PMO: the Product Owner and Scrum "
            "Master cover coordination. "
            "The case for an Agile PMO grows with the number of teams, shared budgets and regulatory requirements.",
        ),
        S(
            "Agile PMO services and responsibilities",
            "An Agile PMO is easiest to design as a short catalogue of services. Pick the ones that solve your current "
            "problems; few PMOs offer all of them.",
            T(
                ["Service", "What the Agile PMO does", "What good looks like"],
                ["Portfolio flow and prioritisation", "Runs intake, maintains the portfolio Kanban, prepares prioritisation data such as cost of delay", "New ideas are triaged within weeks; work in progress at portfolio level is limited"],
                ["Funding and guardrails", "Supports budgeting for teams or value streams and tracks spend against guardrails", "Funding decisions take days, not months, and the spend mix matches strategy"],
                ["Lean governance", "Designs lightweight decision points and reviews based on working results", "Decisions happen at the lowest sensible level with a clear audit trail"],
                ["Capacity", "Keeps a view of team capacity and demand across the portfolio", "Leaders can see what the teams can absorb before they commit"],
                ["Dependencies and release calendar", "Facilitates cross-team planning and keeps one release and dependency view", "Blocking dependencies are spotted at planning, not in the last sprint"],
                ["Metrics and reporting", "Publishes flow and outcome metrics generated from team tools", "One live dashboard, no retyped reports"],
                ["Capability and coaching", "Trains and coaches teams, leaders and PMO staff; runs communities of practice", "Practices improve and new teams ramp up quickly"],
                ["Tools and data", "Configures shared tools and agrees minimum data standards", "Data entered once, consistent fields across teams"],
                ["Risk and compliance", "Maps regulatory controls onto Agile practices; keeps a cross-team RAID view", "Auditors get evidence from normal work, not extra paperwork"],
                ["Event facilitation", "Organises portfolio reviews, quarterly planning and cross-team retrospectives", "Events start on time, have clear outputs and decisions are recorded"],
            ),
            "Several of these services are covered in more depth in our guides to "
            "[Agile portfolio management](/project-management/agile/agile-portfolio-management/), "
            "[Agile capacity planning](/project-management/agile/agile-capacity-planning/) and the "
            "[RAID log](/project-management/raid-log/).",
        ),
        S(
            "Supportive, controlling and directive PMOs in an Agile setting",
            "The classic PMO types still apply, but each looks different once teams work in an Agile way. Use the "
            "table to decide which model you are moving towards.",
            T(
                ["PMO type", "Traditional version", "Agile version", "Main risk in an Agile setting"],
                ["Supportive", "Templates, training, lessons learned", "Coaching, communities of practice, shared tool set-up, metrics help", "Teams ignore it if the help is not practical"],
                ["Controlling", "Mandatory methods, reports and gates", "A small set of non-negotiable guardrails, such as Definition of Done, security checks and funding limits", "Guardrails grow back into a full stage-gate process"],
                ["Directive", "PMO employs and assigns project managers", "PMO hosts delivery leads or Release Train Engineers who serve groups of teams", "Command and control returns under a new name"],
            ),
            "Most Agile PMOs end up as a **supportive PMO with a few firm guardrails**: teams choose how they work, but "
            "everyone follows the same minimum rules for funding, quality, security and data. That combination keeps "
            "autonomy high without losing the control that regulators and finance teams need.",
        ),
        S(
            "Agile PMO structure and roles",
            "Job titles vary widely. The roles below are the building blocks; a small Agile PMO may combine three or "
            "four of them in one person.",
            T(
                ["Role", "Typical responsibilities", "Useful background"],
                ["Head of Agile PMO or VMO lead", "Owns the PMO's purpose and services, works with portfolio leaders, champions lean governance", "Senior delivery or portfolio leadership, change management"],
                ["Portfolio manager", "Runs intake and the portfolio Kanban, prepares prioritisation and funding decisions", "Portfolio management, finance, business analysis"],
                ["Portfolio or data analyst", "Builds dashboards, maintains data standards, analyses flow metrics", "Data skills, Jira or work management tools, reporting"],
                ["Agile coach", "Coaches teams and leaders, trains PMO staff, improves practices", "Scrum, Kanban, facilitation, coaching"],
                ["Release Train Engineer or delivery lead", "Facilitates cross-team planning and events, removes impediments across teams", "Scrum Master or programme experience"],
                ["PMO coordinator", "Organises events, keeps the calendar, supports onboarding", "Organisation and communication; a common entry role"],
            ),
            "The [Agile project manager](/project-management/agile/agile-project-manager/) and "
            "[Scrum Master](/project-management/agile/scrum-master-role/) roles sit mainly in or beside the teams, "
            "but many people move into Agile PMO roles from both.",
            H3("Where the Agile PMO sits"),
            "Smaller portfolios usually have one **central** Agile PMO. Larger organisations prefer **hub and "
            "spoke**: a small central team owns guardrails, metrics and tools, while people in each product area "
            "or release train apply them. Mature organisations may go further and **embed** most PMO roles in the "
            "value streams.",
            "A centre of excellence focuses on methods and coaching, while an Agile PMO also covers portfolio, "
            "funding and governance; many organisations combine them under one leader.",
        ),
        S(
            "The Agile PMO in SAFe: the value management office",
            "The [Scaled Agile Framework (SAFe)](/project-management/agile/scaled-agile-framework-safe/) gives the "
            "Agile PMO a specific name and job. SAFe describes the **value management office (VMO)** as the function "
            "responsible for facilitating Lean Portfolio Management and fostering operational excellence and lean "
            "governance. SAFe notes that VMOs often emerge from existing PMOs, and earlier SAFe material called the "
            "same function the Agile PMO or APMO.",
            "SAFe separates two complementary functions: the **Lean-Agile Center of Excellence (LACE)** leads and coaches the transformation as a whole, "
            "while the **VMO** focuses on the portfolio activities that connect strategy to delivery.",
            H3("Portfolio events the VMO supports"),
            T(
                ["Event", "Typical frequency", "Purpose", "VMO contribution"],
                ["Portfolio Sync", "Typically monthly", "Review epic progress, flow and dependencies; make portfolio decisions", "Keeps the portfolio Kanban and metrics current, tracks actions, filters the agenda"],
                ["Strategic Portfolio Review", "Typically quarterly", "Check strategy, investment mix and portfolio performance", "Prepares data on outcomes, spend and capacity"],
                ["Participatory Budgeting", "Typically twice a year", "Stakeholders allocate budget across value streams together", "Prepares options and the business context, records the result"],
            ),
            H3("Lean budget guardrails"),
            "SAFe defines Lean budget guardrails as the policies and practices for budgeting, spending and governance "
            "for a portfolio. It lists four:",
            OL(
                "**Guiding investments by horizon**, so spending is balanced across current, emerging and future solutions.",
                "**Applying capacity allocation**, so new features, maintenance and technical work each get a planned share.",
                "**Approving significant initiatives**, so large epics above an agreed threshold get portfolio approval.",
                "**Continuous Business Owner engagement**, so business stakeholders stay involved in reviews and planning.",
            ),
            "The VMO also supports [Agile release trains](/project-management/agile/agile-release-train/) and their "
            "[PI planning](/project-management/agile/pi-planning/) events. You do not need SAFe to use these ideas: "
            "guardrails, a portfolio Kanban and a regular portfolio sync work in any scaled Agile setting.",
        ),
        S(
            "Lean governance: replacing stage gates",
            "Governance does not disappear in an Agile organisation; it moves closer to the work and relies on "
            "evidence from working product. The table translates the controls a traditional PMO runs into their "
            "Agile equivalents. Our guide to [project governance](/project-management/project-governance/) covers "
            "the underlying principles.",
            T(
                ["Traditional control", "Agile equivalent", "What the Agile PMO checks"],
                ["Full business case before any work", "Lean business case for each epic with a hypothesis and an MVP", "The hypothesis is measurable and the MVP is small enough to test quickly"],
                ["Stage gate sign-off", "Regular review of working product at sprint or system demos", "Increments are reviewed by stakeholders, and decisions to continue, pivot or stop are recorded"],
                ["Baseline and change control", "Backlog reprioritisation by the Product Owner within guardrails", "Large changes to scope, cost or direction go to the portfolio sync"],
                ["Project budget approval", "Funding for teams or value streams, reviewed periodically", "Spend stays within guardrails and matches priorities"],
                ["RAG status report", "Live flow metrics, forecasts and outcome data", "Forecasts are based on actual throughput, not optimism"],
                ["Quality gate at the end", "Definition of Done, automated tests and security checks on every increment", "The Definition of Done is applied consistently across teams"],
            ),
            H3("Satisfying audit and compliance"),
            "Regulated organisations often worry that Agile governance will fail an audit. Auditors need evidence "
            "that controls exist and operate, not specific documents. List the controls you must meet, map each "
            "one to an Agile practice (such as pull request approvals or the Definition of Done), agree what tool "
            "evidence will be accepted, and pilot the mapping with one team before scaling it.",
        ),
        S(
            "Agile PMO metrics and reporting",
            "An Agile PMO reports on flow, outcomes and quality, using data generated by the teams' tools. Choose a "
            "few measures, explain them clearly and show trends rather than single numbers.",
            T(
                ["Metric", "What it measures", "How the Agile PMO uses it"],
                ["[Throughput](/project-management/kanban/throughput/)", "Items finished per week or sprint", "Forecasting how much the portfolio can deliver"],
                ["[Cycle time](/project-management/kanban/cycle-time/)", "Time from start to finish for an item", "Spotting slow stages and setting realistic expectations"],
                ["Epic lead time", "Time from an epic's approval to its release", "Showing how quickly strategy turns into delivered value"],
                ["Portfolio WIP", "Number of epics in progress at once", "Limiting parallel work so things finish"],
                ["Plan predictability", "Planned vs delivered objectives each quarter", "Building trust in forecasts without demanding certainty"],
                ["Outcome measures", "Progress on OKRs or business results such as adoption or cost", "Checking that delivery changes something that matters"],
                ["Quality", "Escaped defects, incidents, change failure rate", "Making sure speed is not bought with rework"],
                ["Investment mix", "Spend by value stream, horizon or work type", "Checking that spend follows strategy and guardrails"],
            ),
            TIP("Never compare velocity between teams or use it as a performance target. Story points are relative "
                "to each team, so a velocity league table only teaches teams to inflate their estimates."),
            H3("What an Agile portfolio report looks like"),
            "A one-page portfolio report, generated from live data, typically contains:",
            L(
                "**Outcomes:** progress on the quarter's objectives or OKRs, with a short commentary.",
                "**Flow:** throughput and cycle time trends, plus epics in progress against the WIP limit.",
                "**Forecasts:** for each major epic or release, a date or scope range based on actual throughput.",
                "**Risks and dependencies:** the top cross-team blockers and who owns them.",
                "**Decisions needed:** what the portfolio leaders must decide at the next sync.",
            ),
            "It replaces, rather than adds to, the traditional [project status report](/project-management/project-status-report/). "
            "For a wider list of measures, see our guide to [Agile metrics and KPIs](/project-management/agile/agile-metrics-and-kpis/).",
        ),
        S(
            "How to transform a traditional PMO into an Agile PMO",
            "Transforming a PMO is itself a change programme, so run it in an Agile way: small steps, visible results, "
            "regular feedback.",
            OL(
                "**Agree a new purpose with leadership.** Write one sentence, such as \"help the organisation deliver the most valuable work, predictably, with the least overhead\", and have the sponsor endorse it.",
                "**Map the current PMO.** List every report, template, gate and meeting the PMO runs, who uses each one and how long it takes teams to produce.",
                "**Ask the customers.** Interview executives, Product Owners and team members about what helps them and what gets in the way.",
                "**Choose a pilot area.** Pick one product area or group of three to five willing teams.",
                "**Agree minimum guardrails.** Decide the few non-negotiables: funding limits, Definition of Done, security and data rules.",
                "**Replace one control at a time.** For example, swap the monthly status template for a live dashboard built from team tools.",
                "**Set up a portfolio Kanban.** Visualise epics from idea to done, add WIP limits and agree how items are prioritised.",
                "**Start a portfolio cadence.** Run a monthly portfolio sync and a quarterly planning and review event.",
                "**Retrain and redeploy PMO staff.** Train them in Agile, Lean, flow metrics and facilitation; some will become portfolio analysts or coaches.",
                "**Agree the governance mapping with audit.** Document how existing controls are met by Agile practices.",
                "**Measure and publish results.** Track a few before-and-after measures such as reporting effort, decision time and epic lead time.",
                "**Expand in waves.** Add the next group of teams only when the pilot works, and retire old processes as you go.",
            ),
            H3("A 90-day plan"),
            T(
                ["Period", "Goals", "Outputs"],
                ["Days 1-30: understand", "Map current services, interview customers, agree purpose and pilot", "PMO service inventory, problem list, one-sentence purpose, pilot teams chosen"],
                ["Days 31-60: pilot", "Live dashboard, portfolio Kanban, first portfolio sync", "Dashboard replacing one report, visible portfolio WIP, first decisions recorded"],
                ["Days 61-90: learn and plan", "Review the pilot, agree guardrails with finance and audit, plan the next wave", "Guardrail document, governance mapping, results shared with the sponsor"],
            ),
            "If the wider organisation is also changing, align this plan with the "
            "[how to implement Agile](/project-management/agile/how-to-implement-agile/) roadmap rather than running "
            "a separate initiative.",
        ),
        S(
            "Worked example: an Agile PMO for 12 teams",
            "This example is illustrative. A financial services firm has 12 Scrum Teams building customer and internal "
            "products. The PMO is a five-person controlling PMO built for waterfall projects. Teams complain that they "
            "spend hours each month on status templates, and executives complain that they still cannot tell what "
            "will ship this quarter.",
            H3("Quarter 1: stop the double reporting"),
            L(
                "The head of PMO and the CTO agree a new purpose: help the teams deliver the highest-value work with the least overhead.",
                "The PMO lists 14 recurring reports and templates. Six are used by nobody and are retired at once.",
                "Four pilot teams move to a live dashboard built from their work management tool; the monthly status template is dropped for them.",
                "A portfolio Kanban shows 31 epics in progress across the 12 teams, far more than the teams can finish in a quarter.",
            ),
            H3("Quarter 2: limit work in progress and plan together"),
            L(
                "Portfolio leaders agree a WIP limit of 15 epics. Ten epics are paused and three are stopped.",
                "The first joint quarterly planning event brings all 12 teams together and surfaces 22 cross-team dependencies.",
                "Internal audit agrees a mapping of change-control requirements onto pull request approvals and the Definition of Done.",
            ),
            H3("Results after two quarters"),
            T(
                ["Measure", "Start", "After 6 months"],
                ["Recurring PMO reports and templates", "14", "5, all generated from tools"],
                ["Team time spent on status reporting", "About 4 hours per team per month", "Under 1 hour, mostly review"],
                ["Epics in progress", "31", "15 (at the WIP limit)"],
                ["Median epic lead time", "About 9 months", "About 5 months"],
                ["Quarterly objectives delivered as planned", "Not measured", "About 75%"],
            ),
            "The figures are illustrative, but the pattern is common: the quickest gains come from removing unused "
            "reports and limiting work in progress, not from new processes. The PMO's influence grew because teams "
            "could see it saving them time.",
        ),
        S(
            "Common Agile PMO mistakes",
            T(
                ["Mistake", "What it looks like", "How to avoid it"],
                ["Renaming without changing", "The \"Agile PMO\" still asks for Gantt charts, gates and RAG reports", "Retire at least one old control for every new practice"],
                ["Dual reporting", "Teams update their board and a separate PMO template", "Generate every report from the tools teams already use"],
                ["Velocity league tables", "Teams ranked by story points per sprint", "Use throughput and cycle time trends for forecasting, never for ranking"],
                ["No limit on portfolio WIP", "Everything is approved and nothing finishes", "Set a WIP limit for epics and stop work when it is reached"],
                ["Guardrails that grow into gates", "Each incident adds a new mandatory check", "Review guardrails every quarter and remove the ones that add no value"],
            ),
        ),
        S(
            "Agile PMO tools and templates",
            "An Agile PMO needs one place where portfolio data lives, ideally the same tool the teams use day to day, "
            "so reports are generated rather than assembled. Options from our reviews:",
            L(
                "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool (9.4/10), combines boards, request "
                "intake, workflows, resource planning and cross-project dashboards, and its top plans add deeper "
                "portfolio, financial and resource analysis for PMO-level insight. It suits Agile PMOs that oversee a "
                "mix of Agile and non-Agile work across departments.",
                "**[Jira](/project-management-tools/jira/)** is the natural choice where software teams already work "
                "in it; its Premium and Enterprise plans add Plans (previously Advanced Roadmaps) for cross-team "
                "planning, dependencies and capacity.",
                "**[monday.com](/project-management-tools/monday/)** is easy to adopt and offers dashboards across "
                "boards, with portfolio and resource management on its higher plans.",
                "**[Asana](/project-management-tools/asana/)** links projects to portfolios and goals on its Advanced "
                "plan, which helps when the PMO reports progress against OKRs.",
                "**ClickUp** and **Smartsheet** are also worth comparing: ClickUp for sprints, goals and dashboards in "
                "one low-cost workspace, Smartsheet for spreadsheet-style portfolio reporting.",
            ),
            "See all of them side by side on our [tool comparison page](/project-management-tools/compare/). If you "
            "are starting without a platform, our [product roadmap template](/templates/product-roadmap-template/) "
            "gives a simple portfolio roadmap and the [RAID log template](/templates/raid-log-template/) covers "
            "cross-team risks and dependencies.",
        ),
        S(
            "Agile PMO skills, careers and certification",
            "Agile PMO work rewards a different mix of skills from traditional PMO work. Templates and compliance "
            "checking matter less; data, facilitation and portfolio thinking matter more.",
            L(
                "**Portfolio management:** prioritisation, cost of delay, funding models and investment mix.",
                "**Data and flow metrics:** throughput, cycle time, forecasting and dashboard design.",
                "**Facilitation:** running planning events, portfolio reviews and cross-team retrospectives.",
                "**Stakeholder and change skills:** working with finance, audit and executives to change long-standing processes.",
            ),
            "Relevant credentials include PMI's PMO credential (PMI-PMOCP), Agile certifications such as PMI-ACP or "
            "Scrum certifications, SAFe's Lean Portfolio Management training for SAFe organisations, and P3O for "
            "PMO design. Requirements change, so check each awarding body's site before you apply.",
            "Read our guide on [how to learn Agile and get certified](/project-management/agile/how-to-learn-agile-and-get-certified/) to compare the main Agile credentials and plan your next step.",
        ),
    ],
    faq=[
        ("What is an Agile PMO?",
         "A project, programme or portfolio management office redesigned for Agile delivery. It coordinates "
         "portfolio decisions, Lean funding, lightweight governance, flow metrics and coaching rather than enforcing "
         "detailed plans and stage gates."),
        ("What is the difference between a PMO and an Agile PMO?",
         "A traditional PMO controls projects through plans, stage gates and status reports. An Agile PMO enables "
         "long-lived teams through roadmaps, guardrails, live dashboards and regular reviews of working product."),
        ("Does Agile need a PMO?",
         "Not always. A small product with a few teams can coordinate without one. Larger organisations with shared "
         "budgets, many teams and regulatory requirements usually benefit from an Agile PMO or similar portfolio "
         "function."),
        ("What is the role of the PMO in Scrum?",
         "Scrum does not define a PMO. In Scrum organisations, the PMO typically supports portfolio prioritisation, "
         "funding, cross-team dependencies, metrics and coaching, while Scrum Teams manage their own work."),
        ("What does a value management office (VMO) do?",
         "In SAFe, the VMO facilitates Lean Portfolio Management and fosters operational excellence and lean "
         "governance. It supports portfolio events, keeps the portfolio Kanban and metrics current and often evolves "
         "from an existing PMO."),
        ("What is an APMO?",
         "An Agile programme management office: another name for an Agile PMO. Earlier SAFe material used the term; "
         "current SAFe guidance describes the value management office (VMO) instead."),
        ("What metrics should an Agile PMO track?",
         "Throughput, cycle time, epic lead time, portfolio work in progress, plan predictability, outcome measures "
         "such as OKR progress, quality and investment mix. Avoid comparing velocity between teams."),
        ("How do you transform a traditional PMO into an Agile PMO?",
         "Agree a new purpose, map current reports and gates, pilot with a few willing teams, replace one control at a "
         "time with a lighter Agile equivalent, retrain PMO staff, agree the approach with audit and expand in waves."),
        ("What roles are in an Agile PMO?",
         "Typically a head of Agile PMO or VMO lead, portfolio managers, portfolio or data analysts, Agile coaches, "
         "delivery leads or Release Train Engineers, a tools administrator and coordinators."),
        ("What is lean governance?",
         "Governance that relies on lightweight guardrails, decentralised decisions and evidence from working product, "
         "instead of detailed up-front approval and stage gates."),
        ("Is an Agile PMO the same as a centre of excellence?",
         "Not exactly. A centre of excellence focuses on methods and coaching; an Agile PMO also covers portfolio "
         "decisions, funding, governance and reporting. Many organisations combine the two."),
        ("How long does it take to build an Agile PMO?",
         "A pilot with a live dashboard, portfolio Kanban and portfolio cadence can run within about three months. "
         "Changing funding and governance across a whole organisation usually takes a year or more."),
    ],
)
