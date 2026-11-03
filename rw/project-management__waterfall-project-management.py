from core import S, L, OL, T, TIP, H3

URL = "/project-management/waterfall-project-management/"

RW = dict(
    title="Waterfall Project Management: Phases, Pros, Cons & Example",
    desc="Waterfall project management explained: the phases, deliverables and gates, a worked example, pros and cons, when to use it and how it compares with Agile.",
    intro=(
        "Waterfall project management is a sequential, plan-driven approach in which a project moves through fixed "
        "phases, such as requirements, design, build, test and deployment, with each phase finished and approved "
        "before the next begins. It works best when requirements are stable and the result only has value once it is "
        "complete. This guide covers the phases and their deliverables, how to run a waterfall project step by step, "
        "a worked example, the pros and cons and how waterfall compares with Agile."
    ),
    takeaways=[
        "Waterfall is a predictive approach: you define scope, schedule and cost up front, baseline them and control the project against that plan.",
        "Typical phases are requirements, design, implementation, verification, deployment and maintenance, separated by phase gates where sponsors approve the work.",
        "It suits stable requirements, regulated or contract-driven work, physical builds and teams repeating a familiar type of project.",
        "Its main weakness is late feedback: users see the result near the end, when changes are most expensive.",
        "Royce's 1970 paper, usually cited as the origin, actually warned against a single pass and recommended feedback between phases.",
        "Many organisations now use hybrids: waterfall governance and milestones with iterative delivery inside some phases.",
    ],
    sections=[
        S(
            "What is waterfall project management?",
            "**Waterfall project management** is a linear way of running a project in which the work flows through a "
            "series of phases in a fixed order: requirements, design, build, test, deploy and support. Each phase "
            "produces approved deliverables that become the input to the next. Scope, schedule and budget are planned "
            "in detail at the start and changes go through formal change control.",
            "PMI and the PMBOK Guide describe this style as a **predictive** approach, because you predict and commit "
            "to the outcome early, then manage the project against a baseline. Agile approaches are described as "
            "**adaptive**, and a mix of the two as **hybrid**. Waterfall is the classic, best-known form of predictive "
            "delivery.",
            "Three ideas sit at the heart of waterfall:",
            L(
                "**Sequence.** Phases follow one another. You do not start building until the design is approved, and "
                "you do not release until testing is complete.",
                "**Up-front definition.** The project requirements and "
                "project scope are agreed and signed off early, so estimates "
                "and contracts can be based on them.",
                "**Control against a plan.** A [project baseline](/project-management/project-baseline/) for scope, "
                "time and cost is set before execution, and progress is measured against it.",
            ),
            "Waterfall is still widely used in construction, engineering, manufacturing, defence, government, "
            "infrastructure and parts of regulated IT, where a design must be approved before money is spent on "
            "building it.",
        ),
        S(
            "Where the waterfall model came from",
            "The sequential model is usually traced to a 1970 paper by Winston W. Royce, \"Managing the Development of "
            "Large Software Systems\". Royce drew the familiar cascade of phases, but he did not recommend running them "
            "in a single pass. He described that version as risky and argued for feedback between phases, early "
            "prototyping, heavy documentation and doing the job twice, so that a pilot version informed the final "
            "one.",
            "Royce never used the word \"waterfall\". The label is generally traced to later writers, with a 1976 "
            "paper by Bell and Thayer often cited as an early use. The irony is that the paper most often quoted as "
            "the source of rigid waterfall was one of its first critics.",
            "Phase-by-phase delivery is older than software, however. Construction and engineering projects have long "
            "separated feasibility, design, procurement, construction and commissioning, because changing a design "
            "after concrete is poured or steel is fabricated is extremely expensive.",
        ),
        S(
            "The phases of waterfall project management",
            "Sources name and count the phases differently, from five to seven. The six below are the most common. "
            "Whatever names you use, each phase should have a clear purpose, defined deliverables and exit criteria.",
            T(
                ["Phase", "Purpose", "Key deliverables", "Typical exit criteria"],
                ["1. Requirements", "Define what the solution must do and the constraints it must meet", "Requirements specification, acceptance criteria, scope statement", "Requirements signed off by the sponsor and key users"],
                ["2. Design", "Decide how the solution will meet the requirements", "High-level and detailed design, specifications, test strategy", "Design review passed; traceability to requirements confirmed"],
                ["3. Implementation", "Build, configure, construct or manufacture the solution", "Built components, unit-tested code, constructed works", "All components complete and unit tested"],
                ["4. Verification", "Prove the solution meets the requirements", "Test plans, test results, defect log, user acceptance sign-off", "Agreed defect thresholds met; acceptance signed"],
                ["5. Deployment", "Release or hand over the solution to users", "Go-live plan, training, handover documents", "Go-live checklist complete; operations accept handover"],
                ["6. Maintenance", "Support, fix and improve after release", "Support model, warranty fixes, lessons learned", "Warranty period ends; project formally closed"],
            ),
            H3("1. Requirements"),
            "You gather and document everything the solution must do: functional requirements (features and "
            "behaviour), non-functional requirements (performance, security, accessibility) and constraints such as "
            "regulation, budget and dates. Interviews, workshops, document analysis and observation are the usual "
            "techniques. The output is a requirements specification that is precise enough to design, estimate and "
            "test against. Ambiguous requirements are the most common root cause of waterfall failures, so this phase "
            "deserves more time than teams usually give it.",
            H3("2. Design"),
            "The team turns requirements into a solution. In software this means architecture, data models, "
            "interfaces and screen designs; in construction it means drawings and specifications; in manufacturing it "
            "means engineering designs and tooling plans. Many projects split design into a high-level (outline) "
            "design and a detailed design, each with its own review. A traceability matrix links every requirement to "
            "the design element that satisfies it and, later, the test that proves it.",
            H3("3. Implementation"),
            "This is the build phase, usually the longest and most resource-intensive. Work is organised using the "
            "[work breakdown structure](/project-management/work-breakdown-structure/) into "
            "[work packages](/project-management/work-package/) with owners, estimates and dates. The project manager "
            "tracks progress against the schedule and cost baselines and reports variances.",
            H3("4. Verification"),
            "The solution is tested against the requirements: system testing, integration testing, performance and "
            "security testing and, finally, user acceptance testing (UAT). Defects are logged, prioritised and fixed. "
            "Because testing comes late, it often gets squeezed when earlier phases overrun, so protect its duration "
            "in the schedule.",
            H3("5. Deployment"),
            "The solution goes live or is handed over. Activities include data migration, cutover planning, training, "
            "communications and a go/no-go decision. In construction this is commissioning and handover; in "
            "manufacturing it is the start of production.",
            H3("6. Maintenance"),
            "After go-live the solution is supported, defects found in live use are fixed and small enhancements are "
            "made. Many projects define a warranty or hypercare period after which support transfers to business as "
            "usual and the project is formally closed.",
            TIP(
                "Do not confuse these delivery phases with the project management life cycle (initiating, planning, "
                "executing, monitoring and controlling, closing). The life cycle wraps around the delivery phases: you "
                "initiate and plan before requirements start and close after handover. See our guide to "
                "[project management phases](/project-management/project-management-phases/)."
            ),
        ),
        S(
            "Phase gates and sign-offs",
            "A **phase gate** (also called a stage gate or decision point) is a formal review at the end of a phase "
            "where the sponsor or a steering group decides whether the project should continue. Gates are what make "
            "waterfall controllable: they stop a project drifting into the next phase on the strength of unfinished or "
            "unapproved work.",
            "At each gate the decision-makers typically choose one of four outcomes:",
            T(
                ["Decision", "Meaning", "When it is used"],
                ["Go", "Approve the phase and release funding for the next one", "Exit criteria are met and the business case still holds"],
                ["Hold", "Pause until a condition is met", "A dependency, funding or approval is outstanding"],
                ["Recycle", "Rework the current phase", "Deliverables are incomplete or quality is not acceptable"],
                ["Stop", "Close the project", "The business case no longer holds or risk is too high"],
            ),
            "A simple gate checklist covers five questions: Are the phase deliverables complete and approved? Does the "
            "next phase have an updated plan, budget and resources? Are the top risks and issues understood and owned? "
            "Is the business case still valid? Are any open change requests resolved or explicitly carried forward?",
        ),
        S(
            "How to run a waterfall project step by step",
            "The steps below follow a typical waterfall project from approval to closure. Scale the documentation to "
            "the size and risk of the project: a three-month internal project needs far less than a multi-year "
            "contract.",
            OL(
                "**Initiate the project.** Write a [project charter](/project-management/project-charter/) that names the sponsor and project manager, states objectives, high-level scope, budget and key dates, and authorises the work.",
                "**Gather and sign off requirements.** Run workshops and interviews, document requirements with acceptance criteria and get formal sign-off. Agree how requirements will be changed later.",
                "**Define the scope and WBS.** Turn the requirements into a scope statement and a [work breakdown structure](/project-management/work-breakdown-structure/) that covers 100% of the work, broken down to work packages. Use our [WBS template](/templates/work-breakdown-structure-template/).",
                "**Estimate effort, duration and cost.** Estimate each work package bottom up, add contingency for known risks and build the budget.",
                "**Build the schedule.** Break work packages into activities, add task dependencies, assign resources and calculate the [critical path](/project-management/critical-path-method/). Show it on a [Gantt chart](/project-management/gantt-chart/).",
                "**Set the baselines.** Once the plan is approved, save the scope, schedule and cost baselines. Every later variance is measured against them.",
                "**Plan risk, quality and communications.** Start a risk register, define quality checks and testing, and agree who receives which reports and when.",
                "**Execute phase by phase.** Deliver each phase's work, hold reviews and pass each phase gate before starting the next. Report progress with a regular project status report.",
                "**Control changes formally.** Log every change request, assess its impact on scope, time, cost and risk, and get a decision from the change authority before acting. See [change control](/project-management/change-control/).",
                "**Test and accept.** Complete system and user acceptance testing against the signed-off requirements, fix defects and obtain formal acceptance.",
                "**Deploy and hand over.** Execute the go-live or handover plan, train users and transfer the solution to operations or the client.",
                "**Close the project.** Confirm all deliverables are accepted, release resources, close contracts, archive documents and capture lessons learned. See our guide to [project closure](/project-management/project-closure/).",
            ),
        ),
        S(
            "Waterfall project management example",
            "The following example is **illustrative**: the organisation, figures and dates are invented to show how "
            "the phases, gates and change control fit together.",
            "A 400-person organisation is replacing its payroll system. The new system must be live before the start "
            "of the next tax year, the requirements are largely dictated by payroll law and company policy, and the "
            "vendor contract is fixed price against an agreed specification. Those three facts (a fixed deadline, "
            "stable requirements and a fixed-price contract) make a waterfall approach a sensible choice.",
            T(
                ["Phase", "Planned duration", "Main deliverables", "Gate decision"],
                ["Requirements", "4 weeks", "Requirements specification (180 requirements), data migration scope, acceptance criteria", "Gate 1: Go, signed by the HR director and finance director"],
                ["Design", "5 weeks", "Configuration design, interface specifications for HR and finance systems, test strategy", "Gate 2: Recycle for one week; two interface designs incomplete, then Go"],
                ["Implementation", "10 weeks", "Configured system, built interfaces, three trial data migrations", "Gate 3: Go"],
                ["Verification", "6 weeks", "System test, two parallel payroll runs against the old system, UAT sign-off", "Gate 4: Go, with two low-priority defects accepted"],
                ["Deployment", "2 weeks", "Final migration, cutover, training for 12 payroll staff, go-live", "Go-live approved at a go/no-go meeting"],
                ["Maintenance", "8 weeks hypercare", "Defect fixes, first live payroll runs, handover to the support team", "Project closure report approved"],
            ),
            H3("Handling a change request"),
            "During verification, the finance team asks for a new monthly cost-centre report that was not in the signed-off "
            "requirements. Under waterfall, the request is not simply added to the build. The project manager logs it "
            "and runs an impact assessment:",
            L(
                "**Scope:** one new report, plus changes to two existing interfaces.",
                "**Schedule:** about 6 days of extra build and testing effort on the critical path, which would push go-live past the tax year deadline.",
                "**Cost:** a quoted vendor change of £4,800 (illustrative figure).",
                "**Risk:** retesting interfaces late in the project increases the chance of defects at go-live.",
            ),
            "The change control board decides to **defer** the report to a post-go-live enhancement, protecting the "
            "fixed deadline. The decision, the reason and the new delivery date are recorded in the change log and "
            "communicated to finance. That is waterfall working as intended: change is possible, but it is a "
            "deliberate decision with known consequences rather than scope creep.",
            H3("What the example shows"),
            L(
                "Gate 2 caught incomplete designs before they turned into build defects. Recycling one phase cost a week; finding the gaps in testing would have cost far more.",
                "Two parallel payroll runs gave the business evidence, not just assurance, that the new system produced correct results.",
            ),
        ),
        S(
            "Advantages of waterfall",
            T(
                ["Advantage", "Why it matters"],
                ["Clear structure and milestones", "Everyone knows what phase the project is in, what comes next and what \"done\" means for each phase."],
                ["Predictable scope, cost and schedule", "With stable requirements you can estimate, budget and commit to dates early, which sponsors and finance teams value."],
                ["Fits contracts and regulation", "Fixed-price contracts, public procurement and regulated industries often require approved specifications and sign-offs."],
                ["Thorough documentation", "Requirements, designs and test records support audits, handovers, staff changes and long-term maintenance."],
                ["Less demand on stakeholders' time", "Users and sponsors are heavily involved at the start and at gates, rather than continuously."],
                ["Easy to understand", "New team members and external stakeholders grasp a sequential plan quickly; it maps naturally to a Gantt chart."],
                ["Good for dependencies on physical work", "Where later work physically depends on earlier work (foundations before walls), sequencing is not optional."],
            ),
        ),
        S(
            "Disadvantages of waterfall and how to reduce them",
            T(
                ["Disadvantage", "What happens", "How to reduce it"],
                ["Late feedback", "Users see the working solution near the end, when changes are expensive", "Use prototypes, mock-ups or a pilot during design; hold design walkthroughs with real users"],
                ["Costly change", "A requirement change after design can ripple through build and test", "Invest in requirements quality; use formal change control and a contingency reserve"],
                ["Risks found late", "Integration problems and misunderstood requirements surface in testing", "Test critical integrations early; run a technical spike or proof of concept in design"],
                ["Testing gets squeezed", "Overruns in build eat into the test window", "Protect test duration on the critical path; set entry criteria for testing"],
                ["No value until the end", "Benefits arrive only after deployment", "Split large projects into phased releases, each delivering usable value"],
                ["Assumes requirements can be known", "For new products or uncertain markets, early specifications are guesses", "Choose an Agile or hybrid approach where uncertainty is high"],
            ),
            "Most of these weaknesses are not arguments against planning; they are arguments against a single pass "
            "with no feedback. That is exactly what Royce warned about in 1970.",
        ),
        S(
            "When to use waterfall (and when not to)",
            "Use the checklist below to judge whether a project leans towards waterfall, Agile or a hybrid. A project "
            "rarely ticks every box; look at where most of the answers fall.",
            T(
                ["Project characteristic", "Leans waterfall", "Leans Agile"],
                ["Requirements", "Stable, known and can be written down", "Unclear, likely to change or discovered through use"],
                ["Value", "Only useful when complete (a bridge, a payroll system)", "Useful in increments (a website, an app)"],
                ["Cost of change late on", "Very high (physical, contractual or regulatory)", "Low (software that can be released often)"],
                ["Contract", "Fixed price against a specification", "Time and materials or outcome based"],
                ["Regulation and audit", "Formal approvals and documentation required", "Lighter documentation is acceptable"],
                ["Stakeholder availability", "Limited; available at key points", "Available frequently to give feedback"],
                ["Team experience", "Has delivered similar projects before", "Doing something new"],
                ["Technology", "Mature and well understood", "New, experimental or fast-changing"],
            ),
            "Typical good fits for waterfall include construction and fit-out projects, infrastructure, equipment "
            "installation, regulated system validation, data centre moves, office relocations, events with a fixed "
            "date and repeatable implementation projects where the method is well proven.",
            "Typical poor fits are new digital products, research and innovation work, marketing experiments and any "
            "project where users cannot describe what they need until they see something working. For these, see "
            "[what is Agile project management](/project-management/agile/what-is-agile-project-management/).",
        ),
        S(
            "Waterfall vs Agile",
            "Waterfall and Agile answer the same question (how do we deliver this project?) with different "
            "assumptions about uncertainty.",
            T(
                ["Aspect", "Waterfall", "Agile"],
                ["Planning", "Detailed plan up front, baselined", "High-level plan, detailed planning each iteration"],
                ["Scope", "Fixed; time and cost estimated from it", "Flexible; time and cost often fixed, scope varies"],
                ["Delivery", "One release at the end (or a few large ones)", "Frequent small increments"],
                ["Customer involvement", "Heavy at start and at gates", "Continuous"],
                ["Change", "Controlled through formal change requests", "Expected; reprioritised in the backlog"],
                ["Testing", "A separate phase after build", "Built into every iteration"],
                ["Documentation", "Comprehensive", "Just enough"],
                ["Progress measure", "Planned vs actual against baselines, milestones, earned value", "Working increments, velocity, burndown"],
                ["Project manager role", "Plans, directs and controls against the baseline", "Often shared across product owner, Scrum Master and team"],
            ),
            "Neither is better in general. The right choice depends on the project characteristics above, and many "
            "organisations use both. For a full comparison see our guide to "
            "[Agile vs Waterfall](/project-management/agile/agile-vs-waterfall/).",
            "If you are weighing specific frameworks, we also compare [Scrum vs Waterfall](/project-management/scrum/scrum-vs-waterfall/), "
            "and our overview of "
            "[project management methodologies](/project-management/project-management-methodologies/) covers "
            "PRINCE2, Lean, Six Sigma and Critical Chain alongside them.",
        ),
        S(
            "Variations of the waterfall model",
            H3("V-model"),
            "The V-model bends the waterfall into a V. The left side descends through requirements, system design, "
            "architecture and detailed design; the bottom is coding; the right side climbs back up through unit, "
            "integration, system and acceptance testing. Each design level is paired with the test level that "
            "verifies it, and test plans are written at the same time as the design. It is common in safety-critical "
            "and regulated fields such as automotive, medical devices and defence.",
            H3("Waterfall with feedback and overlapping phases"),
            "Here phases are allowed to overlap slightly, and the team can return to the previous phase when a "
            "problem is found. Design might start on well-understood requirements while others are still being "
            "finalised. This is closer to what Royce actually recommended and to how most real waterfall projects "
            "run. The risk is rework if early decisions change, so overlaps should be managed deliberately.",
            H3("Phased or incremental waterfall"),
            "A large scope is split into several releases, each run as a mini-waterfall. A system might go live for "
            "one region first, then others; a building might be handed over floor by floor. This brings value and "
            "feedback earlier while keeping predictive control within each release. See "
            "[iterative and incremental development](/project-management/iterative-and-incremental-development/).",
            H3("Hybrid approaches"),
            "Hybrid models combine waterfall governance (a charter, budget, phase gates and milestone dates) with "
            "Agile delivery inside some phases. A common pattern, sometimes nicknamed \"water-scrum-fall\", runs "
            "requirements and funding in a predictive way, builds in Scrum sprints, then uses a formal release and "
            "deployment phase. Methods such as [PRINCE2](/project-management/prince2/) also support this: its "
            "management stages and stage boundaries give control, while delivery inside a stage can be Agile.",
        ),
        S(
            "Common waterfall mistakes",
            L(
                "**Signing off vague requirements.** \"The system should be user friendly\" cannot be designed or tested. Write requirements with measurable acceptance criteria.",
                "**Treating sign-off as a formality.** If sponsors approve documents they have not read, problems pass through the gate and resurface in testing.",
                "**Skipping the baseline.** Without a saved baseline you cannot measure variance, and status reports become opinions.",
                "**Absorbing changes informally.** Small \"while you are at it\" additions accumulate into delays. Route every change through change control.",
                "**Squeezing testing to recover the schedule.** Cutting test time moves defects into live use, where they cost more. Recover time elsewhere or agree a new date.",
                "**No user involvement between requirements and UAT.** Show designs, prototypes or demonstrations to users during design and build, even in a waterfall project.",
                "**Using waterfall for an uncertain product.** If nobody can say what good looks like, a predictive plan will be wrong. Choose a hybrid or Agile approach instead.",
            ),
        ),
        S(
            "Tools and templates for waterfall projects",
            "Waterfall projects lean heavily on scheduling, so the most useful tools are those with strong Gantt "
            "charts, dependencies, the critical path and baselines.",
            L(
                "**Templates.** For small projects a spreadsheet is enough. Start with our [Gantt chart template](/templates/gantt-chart-template/), [project schedule template](/templates/project-schedule-template/) and [project plan template](/templates/project-plan-template/), and use the [change request template](/templates/change-request-template/) to log changes.",
                "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool, includes interactive Gantt charts from the Team plan with all four dependency types, the critical path and baselines for planned-versus-actual tracking, which suits date-driven, multi-phase projects and PMOs running many of them.",
                "**[Smartsheet](/project-management-tools/smartsheet/)** combines a familiar spreadsheet grid with Gantt charts, dependencies and critical path highlighting, which many construction and enterprise planning teams find natural.",
                "**[Microsoft Planner](/project-management-tools/microsoft-planner/)** premium plans offer timelines and dependencies, with baselines and critical path on Planner and Project Plan 3, which suits organisations already standardised on Microsoft 365.",
                "**[monday.com](/project-management-tools/monday/)** and **[ClickUp](/project-management-tools/clickup/)** both offer Gantt views with dependencies and milestones, and suit teams that run waterfall and Agile work side by side.",
            ),
        ),
    ],
    faq=[
        ("What are the phases of waterfall?",
         "The most common list is requirements, design, implementation, verification (testing), deployment and "
         "maintenance. Some sources merge or rename phases, giving five or seven, but the sequence is the same."),
        ("Is waterfall outdated?",
         "No. It remains a sound choice for stable, regulated, contract-driven or physical projects, such as "
         "construction, infrastructure and system validation. It is less suitable for new products where requirements "
         "are uncertain."),
        ("Who created the waterfall model?",
         "The sequence is usually traced to Winston Royce's 1970 paper on managing large software systems. Royce warned "
         "that a single pass was risky and recommended feedback and iteration. He did not use the word \"waterfall\", "
         "which was applied by later authors."),
        ("What is the main difference between waterfall and Agile?",
         "Waterfall fixes scope up front and delivers in one sequence of phases; Agile delivers in short iterations, "
         "gathers feedback continuously and lets scope change as the team learns."),
        ("When should you use waterfall?",
         "When requirements are stable and well understood, the result only has value once complete, late changes are "
         "expensive, a contract or regulator requires approved stages, or the team has delivered similar projects "
         "before."),
        ("What is an example of a waterfall project?",
         "Constructing a building, replacing a payroll system to a fixed legal deadline, installing manufacturing "
         "equipment or relocating an office. Each has a defined end state and a natural order of phases."),
        ("What is the V-model?",
         "A variant of waterfall that pairs each design phase with a matching test phase, so acceptance tests are "
         "planned against requirements, system tests against the system design and so on. It is common in "
         "safety-critical industries."),
        ("Is waterfall the same as predictive project management?",
         "Broadly, yes. Predictive is the wider term PMI uses for approaches that define scope, schedule and cost early "
         "and control against a baseline. Waterfall is its classic form."),
        ("Can waterfall and Agile be combined?",
         "Yes. Hybrid approaches use waterfall-style governance, budgets and milestones with Agile delivery inside some "
         "phases, or run fixed-scope parts of a project predictively and uncertain parts iteratively."),
        ("Can you go back to a previous phase in waterfall?",
         "In practice, yes, though it should be a controlled decision. A gate can recycle a phase, and a change request "
         "can reopen approved requirements or designs, with the impact on time and cost assessed first."),
        ("Do waterfall projects use Gantt charts?",
         "Yes. Gantt charts are the standard way to show phases, activities, dependencies, milestones and the critical "
         "path in a waterfall schedule, and to compare actual progress with the baseline."),
        ("Is PRINCE2 a waterfall method?",
         "Not exactly. PRINCE2 is a project management method with management stages and stage boundaries that can be "
         "used with either predictive or Agile delivery. It is often used to govern waterfall projects, but it does not "
         "require them."),
        ("What documents does a waterfall project need?",
         "Typically a project charter, requirements specification, design documents, project management plan with "
         "schedule and budget baselines, risk register, change log, test plans and results, acceptance sign-offs and a "
         "closure report with lessons learned. Scale them to the project's size and risk."),
    ],
)
