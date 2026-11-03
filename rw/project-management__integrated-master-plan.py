from core import S, L, OL, T, TIP, H3

URL = "/project-management/integrated-master-plan/"

RW = dict(
    title="Integrated Master Plan (IMP): IMS, Structure and Example",
    desc="Integrated master plan (IMP) explained: events, accomplishments and criteria, IMP vs IMS, numbering, a step-by-step method and a worked example.",
    intro=(
        "An integrated master plan (IMP) is an event-based plan that defines a programme's major events, the "
        "accomplishments each event needs and the criteria that prove each accomplishment is complete. Its "
        "time-based companion, the integrated master schedule (IMS), adds the detailed tasks, durations and logic. "
        "This guide explains how both work, how to write and number an IMP, and walks through a worked example from "
        "plan to schedule."
    ),
    takeaways=[
        "An IMP has three levels: events, accomplishments and criteria. It describes what \"done\" looks like, not when each task happens.",
        "The IMS adds a fourth level, tasks, with durations, dependencies and dates, so it can show the critical path.",
        "On US defence contracts the approved IMP generally becomes part of the contract; the IMS usually does not, because its dates change.",
        "IMP items are written in the past tense (\"Design review completed\"); IMS tasks start with an action verb (\"Develop\", \"Test\").",
        "The IMP and IMS trace to the work breakdown structure, the statement of work and earned value control accounts.",
        "The event-based idea is useful on any large, multi-team project, even without a formal IMP.",
    ],
    sections=[
        S(
            "What is an integrated master plan?",
            "An **integrated master plan (IMP)** is an event-based, hierarchical plan made up of programme events, "
            "the accomplishments that must be achieved by each event, and the criteria that provide objective "
            "evidence each accomplishment is complete. It answers \"what does done look like at each review?\" and "
            "forms the framework for the integrated master schedule.",
            "The IMP is deliberately not a schedule. It contains no task durations or dependencies, and any dates in "
            "it are usually for information only. That is its strength: it fixes the logic of progress (you cannot "
            "hold the critical design review until the detailed design is finished and its evidence exists) "
            "independently of the dates, which will move.",
            "Three ideas sum it up:",
            L(
                "**Event-driven, not calendar-driven.** A review happens when its entry criteria are met, not because "
                "a date has arrived.",
                "**Evidence-based.** Each accomplishment has measurable criteria, such as an approved document or a "
                "passed test, rather than a percentage complete.",
                "**Integrated.** It brings engineering, manufacturing, test, logistics and management work into one "
                "plan, traced to the [work breakdown structure](/project-management/work-breakdown-structure/) and "
                "contract requirements.",
            ),
        ),
        S(
            "Where IMPs are used and the guidance behind them",
            "The IMP and IMS come from US Department of Defense (DoD) acquisition, where they are used on major "
            "development and production contracts, often alongside earned value management. They also appear on "
            "other government, aerospace and large engineering programmes, especially those with several "
            "contractors.",
            "The current reference is the *Integrated Master Plan and Integrated Master Schedule Preparation and Use "
            "Guide* published by the Office of the Under Secretary of Defense for Research and Engineering "
            "(OUSD(R&E)) in May 2023, with Change 1 dated 1 October 2024. It replaced the DoD guide of October 2005, "
            "which many older articles still cite. This page follows the 2023 guide; if your contract names a "
            "specific version or customer guidance, that takes precedence.",
            TIP("\"Integrated master plan\" is also used by city and regional governments for long-term public works "
                "plans (water, wastewater, transport). Those are strategic infrastructure plans, not the "
                "event-based programme plan described here."),
            "If you work in the public sector, see our guide to "
            "[government project management](/project-management/industries/government-project-management/) for "
            "the wider context of contracts, oversight and reporting.",
        ),
        S(
            "The three levels of an IMP",
            T(
                ["Level", "What it is", "Example"],
                ["Event", "A programme assessment point at the end of significant activities, usually a major review or decision", "Critical design review (CDR) completed"],
                ["Accomplishment", "A result that must be achieved before or at the event, showing progress", "Software design completed"],
                ["Criteria", "Definitive, measurable evidence that the accomplishment is complete", "Software design description baselined"],
            ),
            "Older guidance and many contracts call accomplishments **significant accomplishments (SAs)** and "
            "criteria **accomplishment criteria (ACs)**. The 2023 guide uses the shorter names; the meaning is the "
            "same.",
            H3("Events"),
            "Events are the big checkpoints: design reviews, test readiness reviews, production readiness reviews, "
            "first deliveries and acceptance. An event is achieved only when all its accomplishments are complete. "
            "There is no required number of events; choose the points where the customer and contractor genuinely "
            "need to assess progress and decide whether to proceed. These are often the programme's key "
            "[project milestones](/project-management/project-milestones/).",
            H3("Accomplishments"),
            "Accomplishments describe the state the programme must reach for the event to succeed: a design "
            "finished, a test facility ready, a supplier qualified, risks assessed. The guide says an event normally "
            "has two or more accomplishments. Accomplishments often cut across teams, which is what makes the plan "
            "integrated.",
            H3("Criteria"),
            "Criteria are the proof. Each one should be a yes/no test that an independent reviewer could check: a "
            "document approved, an analysis delivered, a test passed. The guide says there are generally at least "
            "two criteria per accomplishment, though one may be enough. Criteria can be:",
            L(
                "**Entry criteria:** what must be ready before a review, test or demonstration can start.",
                "**Exit criteria:** what shows the event itself has succeeded, such as review actions closed.",
            ),
        ),
        S(
            "IMP numbering and wording rules",
            "A consistent numbering scheme lets every IMS task trace back to the criterion, accomplishment and event "
            "it supports. The 2023 guide's examples use a hierarchical alphanumeric scheme:",
            T(
                ["Level", "Format", "Example ID", "Example name"],
                ["Event", "Letter", "C", "Critical design review completed"],
                ["Accomplishment", "Event letter + two digits", "C02", "Software design completed"],
                ["Criterion", "Accomplishment + lower-case letter", "C02a", "Software design description baselined"],
                ["IMS task", "Criterion + two digits", "C02a01", "Develop software architecture"],
            ),
            "Some programmes use separators (C.02.a); either way, keep one scheme across the whole programme, give "
            "each sub-plan a unique sequence and let the scheduling tool generate the numbers where possible.",
            H3("How to word IMP items and IMS tasks"),
            "The guide sets a simple grammar. IMP items describe a finished state, so they use **past participles**: "
            "completed, approved, conducted, delivered. IMS tasks describe work, so they **start with an imperative "
            "verb**: develop, perform, test, deliver. Define each verb once in an **Event and Action Dictionary** so "
            "that \"approved\" or \"verified\" means the same thing to everyone.",
            T(
                ["Item", "Weak wording", "Better wording"],
                ["Event", "CDR", "Critical design review completed"],
                ["Accomplishment", "Work on hardware design", "Detailed hardware design completed"],
                ["Criterion", "Thermal analysis 90% done", "Thermal analysis report approved by chief engineer"],
                ["IMS task", "Thermal analysis", "Perform thermal analysis of display unit"],
            ),
        ),
        S(
            "IMP vs IMS",
            "The IMP and IMS are two views of the same plan. The IMP is the top-down, event-based framework; the IMS "
            "is the bottom-up, time-based schedule that shows how and when the work behind each criterion gets done.",
            T(
                ["", "Integrated master plan (IMP)", "Integrated master schedule (IMS)"],
                ["Basis", "Events and the evidence needed for them", "Tasks with durations and dependencies"],
                ["Levels", "Events, accomplishments, criteria", "The same three, plus tasks (and often work packages)"],
                ["Question answered", "What must be achieved, and how will we prove it?", "When will it happen, and what drives the date?"],
                ["Dates", "None, or for information only", "Calculated from logic; baselined and updated"],
                ["Contract status (DoD)", "Generally part of the contract once approved", "Usually a data deliverable, not contractually binding"],
                ["Changes", "Rarely; through contract change", "Every status update"],
                ["Main users", "Programme leadership, customer, contract managers", "Planners, control account managers, team leads"],
            ),
            "In the IMS, every event, accomplishment and criterion appears as a milestone, worded exactly as in the "
            "IMP. Tasks sit beneath the criteria, linked by finish-to-start logic, so the schedule shows which "
            "criterion is late and which event it threatens. Read our guide to "
            "[project scheduling](/project-management/project-scheduling/) for the general scheduling process.",
        ),
        S(
            "How the IMP and IMS connect to the WBS, SOW and EVM",
            "Traceability is what makes the IMP \"integrated\". Each element links to the documents that define and "
            "measure the work:",
            T(
                ["Document", "What it defines", "How it links to the IMP/IMS"],
                ["Statement of work (SOW)", "The work the contractor must do", "Every SOW task should be covered by at least one IMS task"],
                ["Work breakdown structure (WBS)", "The product-oriented breakdown of the deliverables", "Accomplishments, criteria and tasks carry WBS codes; WBS is the foundation of both"],
                ["Organisation breakdown structure (OBS)", "Who is responsible", "Assigns each task and control account to a team"],
                ["Control accounts and work packages", "Where budget and progress are managed", "IMS tasks roll up to work packages and control accounts"],
                ["Earned value management (EVM)", "Cost and schedule performance", "The IMS provides the time-phasing and status for earned value"],
                ["Risk register", "Threats and opportunities", "Risk responses appear as IMS tasks; risks are reviewed at events"],
            ),
            "The WBS and IMP give two complementary views: the WBS shows **what** is being produced, the IMP shows "
            "**how maturity is proven** over time. Work packages are where they meet; see our guide to the "
            "[work package](/project-management/work-package/) and the "
            "[statement of work](/project-management/statement-of-work/).",
            "See our guide to [earned value management](/project-management/earned-value-management/) for how "
            "the IMS time-phasing feeds cost and schedule performance indices.",
        ),
        S(
            "What an IMP document contains",
            "The 2023 guide describes four main parts:",
            OL(
                "**Introduction:** a short programme description, assumptions and ground rules, the Event and Action "
                "Dictionary, the programme organisation and reference documents.",
                "**IMP table:** the numbering scheme, event descriptions and the full hierarchy of events, "
                "accomplishments and criteria, usually as a table.",
                "**Narratives:** brief descriptions of key processes, such as systems engineering, risk management "
                "or configuration management, where the customer needs them.",
                "**Glossary:** terms and abbreviations.",
            ),
            "Because the approved IMP generally becomes contractual, the guide advises keeping narratives concise: "
            "anything written there can bind the contractor and reduce flexibility. Put detailed process "
            "descriptions in management plans that can be updated without a contract change.",
        ),
        S(
            "How to create an integrated master plan step by step",
            "The guide's steps for an IMP fit inside a wider sequence that ends with a baselined IMS. In practice:",
            OL(
                "**Read the requirements.** Start from the statement of work or statement of objectives, the "
                "contract data requirements and any customer IMP guidance.",
                "**Build or adopt the WBS.** Agree the product-oriented "
                "[work breakdown structure](/project-management/work-breakdown-structure/) first; the IMP will be "
                "coded to it.",
                "**Select the events.** Choose the major reviews and decision points, usually from the programme's "
                "life cycle (requirements, preliminary design, critical design, test readiness, production, delivery).",
                "**Define accomplishments for each event.** Ask each team what must be true for the event to "
                "succeed. Aim for two or more per event, covering every discipline involved.",
                "**Write criteria for each accomplishment.** Make each one measurable and evidence-based; include "
                "entry criteria for reviews and exit criteria where needed.",
                "**Write the introduction, dictionary and any narratives.** Define every action verb you use.",
                "**Apply the numbering scheme** and check every item has a WBS code and an owner.",
                "**Iterate with the IMS.** As teams build tasks beneath each criterion, gaps and overlaps appear. "
                "Adjust the IMP until every SOW requirement traces to a task and every task traces to a criterion.",
                "**Review and approve.** The customer reviews the IMP, often as part of proposal evaluation, and the "
                "agreed version is incorporated into the contract.",
            ),
            TIP("Write accomplishments with the people who will do the work. An IMP drafted by planners alone tends "
                "to describe documents rather than the engineering maturity that the customer actually needs to see."),
        ),
        S(
            "Worked example: IMP for an avionics display upgrade",
            "This illustrative example follows a contractor upgrading the cockpit display units on a fleet of "
            "transport aircraft. The programme has five events:",
            T(
                ["ID", "Event"],
                ["A", "System requirements review completed"],
                ["B", "Preliminary design review completed"],
                ["C", "Critical design review completed"],
                ["D", "Test readiness review completed"],
                ["E", "First production units delivered"],
            ),
            H3("Event C in detail"),
            "Here is the IMP for event C, showing four accomplishments and their criteria:",
            T(
                ["ID", "IMP item", "WBS"],
                ["C", "**Critical design review completed**", "1.0"],
                ["C01", "Detailed hardware design completed", "1.1"],
                ["C01a", "Circuit card assembly drawings released", "1.1.2"],
                ["C01b", "Thermal analysis report approved", "1.1.3"],
                ["C02", "Software design completed", "1.2"],
                ["C02a", "Software design description baselined", "1.2.1"],
                ["C02b", "Interface control documents signed", "1.2.2"],
                ["C03", "Verification planning completed", "1.4"],
                ["C03a", "System test plan approved", "1.4.1"],
                ["C03b", "Test equipment requirements defined", "1.4.2"],
                ["C04", "Programme risks and estimates updated", "1.6"],
                ["C04a", "Risk register updated with design risks", "1.6.3"],
                ["C04b", "Estimate to complete updated and reviewed", "1.6.1"],
            ),
            "Notice that the accomplishments span hardware, software, test and management. Event C cannot be "
            "declared complete because the hardware team is ready; all four accomplishments, and all eight criteria, "
            "must be met.",
            H3("From IMP to IMS: tasks under accomplishment C02"),
            "The software team now plans the tasks behind C02. Durations are in working days and day 0 is the day "
            "after event B completes.",
            T(
                ["ID", "Task or milestone", "Duration", "Predecessor", "Start", "Finish"],
                ["C02a01", "Develop software architecture", "15", "B", "0", "15"],
                ["C02a02", "Draft software design description", "20", "C02a01", "15", "35"],
                ["C02a03", "Conduct software design peer review", "5", "C02a02", "35", "40"],
                ["C02a04", "Incorporate comments and baseline design description", "5", "C02a03", "40", "45"],
                ["C02a", "Software design description baselined (milestone)", "0", "C02a04", "45", "45"],
                ["C02b01", "Draft interface control documents", "20", "C02a01", "15", "35"],
                ["C02b02", "Hold interface working group with hardware team", "3", "C02b01", "35", "38"],
                ["C02b03", "Obtain interface control document signatures", "5", "C02b02", "38", "43"],
                ["C02b", "Interface control documents signed (milestone)", "0", "C02b03", "43", "43"],
                ["C02", "Software design completed (milestone)", "0", "C02a, C02b", "45", "45"],
            ),
            "Working through the result:",
            L(
                "Accomplishment C02 is achieved on day 45, driven by the design description path "
                "(C02a01, C02a02, C02a03, C02a04).",
                "The interface path finishes on day 43, so it has 2 days of "
                "[float](/project-management/float-and-slack/) relative to C02.",
                "Every task is under 44 days, so none would be flagged as a long-duration task in a DCMA-style check.",
                "If the peer review (C02a03) slips by 3 days, C02 moves to day 48, and the planner can see "
                "immediately that event C is threatened, not just a software task.",
            ),
            "The same pattern repeats for every criterion. Once all tasks are linked, the IMS calculates the date "
            "for event C and the [critical path](/project-management/critical-path-method/) through the whole "
            "programme.",
        ),
        S(
            "Building the IMS from the IMP",
            "The 2023 guide sets out the IMS steps: determine objectives from the SOW, create the WBS, develop the "
            "IMP, define the OBS, then develop the IMS by defining tasks, resources and milestones, building and "
            "validating the network logic, setting the baseline, identifying the critical path and planning status "
            "reporting. The scheduling practices it recommends are the same ones that make any schedule reliable:",
            T(
                ["Practice", "Guidance"],
                ["Relationships", "Prefer finish-to-start; use finish-to-finish sparingly; never use start-to-finish"],
                ["Leads", "Avoid leads (negative lags); see our guide to [leads and lags](/project-management/leads-and-lags/)"],
                ["Constraints", "Hard constraints are highly discouraged; document any constraint other than as soon as possible"],
                ["Durations", "Review tasks longer than 44 days, which DCMA treats as long-duration, and break them down where practical"],
                ["Critical path", "Only one critical path at a time; validate tool-generated paths for gaps caused by lags, constraints or calendars"],
                ["Dates", "IMS dates are forecasts, not due dates; events happen when their criteria are met"],
                ["Analysis", "Support filtering by WBS, team or control account, and allow what-if analysis without changing the master schedule"],
            ),
            "Every task needs at least one predecessor and one successor, using sound "
            "[task dependencies](/project-management/task-dependencies/). Once the logic is validated, set the "
            "[project baseline](/project-management/project-baseline/) and change it only through formal "
            "[change control](/project-management/change-control/).",
        ),
        S(
            "Tracking progress with the IMP and IMS",
            "During delivery the two documents do different jobs:",
            L(
                "**Event reviews use the IMP.** At each event the customer checks every criterion. If the evidence "
                "is not there, the event is not complete, whatever the schedule says.",
                "**Status updates use the IMS.** Teams report actual starts, finishes and remaining durations, and "
                "the IMS recalculates forecast dates, float and the critical path.",
                "**Earned value uses both.** The IMS time-phases the budget; completed criteria provide objective "
                "evidence for earned value claims.",
                "**Schedule risk analysis uses the IMS.** Adding three-point durations lets you run a "
                "[Monte Carlo simulation](/project-management/monte-carlo-simulation/) to estimate the confidence of "
                "meeting each event. The guide warns that without accurate logic, the critical path and any "
                "statistical analysis are suspect.",
            ),
            "On US defence contracts, IMS data is usually delivered under the Integrated Program Management Data and "
            "Analysis Report (IPMDAR) data item, DI-MGMT-81861. According to Humphreys & Associates, this superseded "
            "the stand-alone IMS data item, DI-MGMT-81650. Check your contract data requirements list for the exact "
            "version and format required. Risks found at reviews feed your wider "
            "[project risk management](/project-management/project-risk-management/) process.",
        ),
        S(
            "Using an IMP outside defence",
            "You do not need a government contract to benefit from event-based planning. On any large project with "
            "several teams or suppliers, a light version of the IMP gives sponsors a clear answer to \"how will we "
            "know we are ready?\". This illustrative example is for a hospital replacing its patient records system:",
            T(
                ["ID", "Event, accomplishment or criterion"],
                ["A", "Design approved"],
                ["A01", "Clinical workflows agreed"],
                ["A01a", "Workflow designs signed off by clinical leads for all wards in scope"],
                ["A02", "Data migration approach agreed"],
                ["A02a", "Migration test 1 completed with reconciliation report approved"],
                ["B", "Go-live readiness confirmed"],
                ["B01", "Staff trained"],
                ["B01a", "Training completion at or above the agreed threshold for every ward"],
                ["B02", "Cutover rehearsed"],
                ["B02a", "Full dress rehearsal completed and rollback timed"],
            ),
            "Use the events as stage gates in your [project roadmap](/project-management/project-roadmap/) and the "
            "criteria as go/no-go checklists. The tasks can live in an ordinary schedule; the free "
            "[project schedule template](/templates/project-schedule-template/) and "
            "[work breakdown structure template](/templates/work-breakdown-structure-template/) are enough for a "
            "first version.",
            H3("Software for IMP-style planning"),
            "Formal defence IMSs are normally built in dedicated scheduling software and delivered in the format "
            "the contract specifies. For lighter use, a work management tool with proper scheduling works well. "
            "[Wrike](/project-management-tools/wrike/), our top-rated tool, is a strong option for multi-team, "
            "date-driven programmes: its Gantt charts (from the Team plan) support all four dependency types, the "
            "critical path, float and baselines, and milestones can carry the IMP numbering in their names. "
            "[Smartsheet](/project-management-tools/smartsheet/) offers dependencies and the critical path on a "
            "familiar grid, and [Microsoft Planner](/project-management-tools/microsoft-planner/) Plan 3 adds "
            "baselines and the critical path for teams already using Microsoft 365.",
        ),
        S(
            "Who does what on an IMP and IMS",
            "Because the IMP and IMS span the whole programme, responsibilities need to be clear from the start. A "
            "typical split on a large contract looks like this:",
            T(
                ["Role", "Responsibilities"],
                ["Customer programme office", "Sets requirements and IMP guidance, evaluates the IMP in the proposal, approves it and runs event reviews"],
                ["Contractor programme manager", "Owns the IMP, agrees events with the customer and decides when the programme is ready for each event"],
                ["Integrated product team (IPT) leads", "Write the accomplishments and criteria for their area and plan the tasks beneath them"],
                ["Planners and schedulers", "Maintain numbering, build and validate the IMS logic, run critical path and schedule risk analysis"],
                ["Control account managers", "Link IMS tasks to work packages and budgets, and report earned value"],
                ["Systems engineering lead", "Checks that events and criteria reflect real technical maturity and trace to requirements"],
            ),
            "This is a programme-level way of working. If you are unsure where project management ends and programme "
            "management begins, see our comparison of "
            "[programme, project and portfolio management](/project-management/program-vs-project-vs-portfolio-management/). "
            "Our guide to [engineering project management](/project-management/industries/engineering-project-management/) "
            "covers the design review cycle that most IMP events are built around.",
        ),
        S(
            "IMP review checklist",
            "Before you submit an IMP, or approve one as the customer, work through these checks:",
            OL(
                "**Coverage:** every SOW requirement and WBS element is covered by at least one criterion.",
                "**Events:** each event is a real decision point, with two or more accomplishments spanning the "
                "disciplines involved.",
                "**Criteria:** each criterion is a yes/no test with named evidence (a document, approval, test result "
                "or delivery) and is not expressed as a percentage.",
                "**Wording:** IMP items use past participles, every verb is defined in the Event and Action "
                "Dictionary, and the IMS milestones repeat the IMP wording exactly.",
                "**Numbering:** IDs follow one scheme, are unique and carry WBS codes.",
                "**Dates:** any dates in the IMP are marked as information only.",
                "**Narratives:** process narratives are short and do not commit the contractor to more than the "
                "contract requires.",
                "**Schedule link:** every criterion has tasks beneath it in the IMS, and the IMS logic produces a "
                "credible date for every event.",
            ),
        ),
        S(
            "Benefits and limitations",
            T(
                ["Benefits", "Limitations"],
                ["Defines progress by evidence, not by elapsed time or percentage complete", "Takes significant effort to build and maintain on large programmes"],
                ["Gives customer and contractor a shared, contractual view of what each event requires", "Contractual status makes changes slow; over-detailed IMPs reduce flexibility"],
                ["Integrates all disciplines, so no team can declare an event complete alone", "Can become a documentation exercise if criteria describe paperwork rather than maturity"],
                ["Traces every task to a requirement and every requirement to a task", "Needs disciplined numbering and tooling to keep traceability intact"],
                ["Provides a solid structure for earned value and schedule risk analysis", "Adds little value on small or single-team projects"],
            ),
        ),
        S(
            "Common IMP and IMS mistakes",
            L(
                "**Treating the IMP as a schedule.** Putting firm dates in the IMP invites contract changes every time "
                "the schedule moves. Keep dates in the IMS.",
                "**Vague criteria.** \"Design 90% complete\" cannot be verified. Use approvals, releases, test results "
                "and signed documents.",
                "**Activity-based accomplishments.** \"Work on software\" describes effort, not a result. Write the "
                "state you will reach.",
                "**Broken traceability.** Tasks with no criterion, or SOW requirements with no task, mean the plan "
                "is incomplete.",
                "**Inconsistent wording.** IMS milestones must match IMP wording exactly, or reviewers cannot trace "
                "them.",
                "**Poor schedule logic.** Missing links, hard constraints and leads distort float and the critical "
                "path.",
                "**Over-long narratives.** Detailed process text in a contractual document limits how you can improve "
                "the process later.",
                "**Declaring events on date.** Holding a review because the date arrived, with criteria unmet, "
                "defeats the purpose of event-based planning.",
            ),
            "Read our guide to the [critical path method](/project-management/critical-path-method/) to check that "
            "the IMS logic behind your events is sound.",
        ),
    ],
    faq=[
        ("What is an integrated master plan (IMP)?",
         "An event-based plan made up of programme events, the accomplishments needed for each event and the "
         "criteria that prove each accomplishment is complete. It provides the framework for the integrated master "
         "schedule."),
        ("What is an integrated master schedule (IMS)?",
         "A networked, time-based schedule that adds detailed tasks, durations and dependencies beneath the IMP's "
         "events, accomplishments and criteria, so forecast dates and the critical path can be calculated."),
        ("What is the difference between an IMP and an IMS?",
         "The IMP defines what must be achieved and how it will be proven; the IMS shows how and when the work will "
         "be done. The IMP rarely changes, while the IMS is updated at every status cycle."),
        ("What are the three elements of an IMP?",
         "Events, accomplishments (formerly called significant accomplishments) and criteria (formerly called "
         "accomplishment criteria)."),
        ("Is the IMP a contractual document?",
         "On US defence contracts, the approved contractor IMP generally becomes part of the contract. The IMS is "
         "usually delivered as data and is not contractually binding, because its dates change."),
        ("Does an IMP include dates?",
         "Usually not, or only for information. Dates, durations and logic belong in the IMS."),
        ("How is an IMP numbered?",
         "Typically hierarchically: events use a letter (C), accomplishments add two digits (C02), criteria add a "
         "lower-case letter (C02a) and IMS tasks add two more digits (C02a01)."),
        ("How should IMP items be worded?",
         "IMP items use past participles to describe a finished state, such as \"Design review completed\". IMS "
         "tasks start with an imperative verb, such as \"Develop\" or \"Test\"."),
        ("How does the IMP relate to the WBS?",
         "The WBS is the foundation. IMP items and IMS tasks carry WBS codes, and IMS tasks roll up to work "
         "packages and control accounts."),
        ("Who prepares the IMP and IMS?",
         "Usually the contractor, often as part of the proposal, with the customer reviewing and approving the IMP "
         "before it is incorporated into the contract."),
        ("Is the IMS used for earned value management?",
         "Yes. The IMS time-phases the work and budget, and completed criteria provide objective evidence for "
         "earned value."),
        ("Which guide covers IMP and IMS preparation?",
         "The OUSD(R&E) Integrated Master Plan and Integrated Master Schedule Preparation and Use Guide, May 2023, "
         "with Change 1 dated 1 October 2024. It replaced the 2005 DoD guide."),
        ("Can I use an IMP on a non-defence project?",
         "Yes, in a lighter form. Event-based milestones with evidence-based criteria work well on any large, "
         "multi-team project, even without the full contractual apparatus."),
    ],
)
