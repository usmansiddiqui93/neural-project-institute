from core import S, L, OL, T, TIP, H3

URL = "/project-management/work-package/"

RW = dict(
    title="Work Package in Project Management: Examples & How-To",
    desc="What a work package in project management is, what to include, the 8/80 rule, work package vs task and activity, a worked example and step-by-step guide.",
    intro=(
        "A work package in project management is the lowest level of the work breakdown structure (WBS): a defined "
        "piece of work, with a clear output, that is small enough to estimate reliably, assign to one owner and track "
        "to completion. Work packages are where scope turns into estimates, budgets, schedules and accountability. "
        "This guide explains what to include, how to size and create work packages, how they differ from tasks and "
        "activities, and walks through a complete worked example."
    ),
    takeaways=[
        "A work package is the lowest level of the WBS, where cost and duration are estimated and managed.",
        "It describes an output (a noun, such as \"quote request form\"); the activities and tasks inside it describe the work (verbs).",
        "Every work package needs one owner, a clear deliverable, acceptance criteria, estimates, dates and dependencies.",
        "Use the 8/80 rule and the reporting-period rule as guides to size, not as fixed standards.",
        "Work packages roll up into control accounts and the project budget, and break down into schedule activities.",
        "In PRINCE2, a work package is also the formal instruction the project manager gives a team manager to deliver specific products.",
    ],
    sections=[
        S(
            "What is a work package in project management?",
            "A **work package** is the work defined at the lowest level of a work breakdown structure, for which cost "
            "and duration are estimated and managed. It produces a specific, verifiable output, has a single "
            "accountable owner and is small enough to plan and control, yet large enough to be worth tracking as a "
            "unit.",
            "Think of a work package as a small, self-contained project inside your project. It has its own scope "
            "(what it delivers), its own estimates (effort, duration and cost), its own owner and its own definition "
            "of done. Once it is approved, the owner and their team can get on with the work, and the project manager "
            "tracks it as one line in the plan.",
            "Work packages matter because almost everything in project control is built on them:",
            L(
                "**Estimating.** Bottom-up estimates are made at work package level and added up to the project total.",
                "**Scheduling.** Each work package is broken into activities, which are sequenced and scheduled.",
                "**Budgeting.** Work package costs roll up into control accounts and the [project budget](/project-management/project-budget/).",
                "**Accountability.** Each package has one named owner, which removes doubt about who is responsible.",
                "**Progress tracking.** Status, percent complete and earned value are measured package by package.",
            ),
        ),
        S(
            "Where work packages sit in the WBS",
            "A [work breakdown structure](/project-management/work-breakdown-structure/) breaks the total project "
            "scope into progressively smaller deliverables. The bottom of each branch is a work package. Under the "
            "**100% rule**, the work packages together must cover all of the project's scope, including project "
            "management work, and nothing outside it.",
            T(
                ["Level", "What it represents", "Example (website project)"],
                ["1. Project", "The total scope", "New customer website"],
                ["2. Major deliverable", "A main output or phase", "5 Build"],
                ["3. Control account (optional)", "A management point where scope, budget and schedule are integrated and reported", "5 Build, owned by the development lead"],
                ["4. Work package", "The lowest WBS element, estimated, owned and tracked", "5.3 Quote request form"],
                ["Below the WBS: activities", "Scheduled work needed to produce the work package", "Build CRM integration"],
                ["Below the WBS: tasks", "Smaller personal steps inside an activity", "Map form fields to CRM fields"],
            ),
            "Each work package has a WBS code (such as 5.3) that ties it to its parent and appears in the schedule, "
            "budget, timesheets and reports. The detail for each package is recorded in the **WBS dictionary**, which "
            "is essentially a collection of work package descriptions.",
            H3("Control accounts and planning packages"),
            "On larger projects, particularly those using earned value, work packages are grouped under **control "
            "accounts**. A control account is a management point, usually owned by a control account manager, where "
            "scope, budget, actual cost and schedule are integrated and compared. Each work package belongs to exactly "
            "one control account.",
            "A **planning package** is a placeholder below a control account for work whose scope is known but not yet "
            "detailed. It has a budget but no detailed activities. As the work gets closer, the planning package is "
            "converted into one or more work packages. This is the essence of **rolling wave planning**: plan the near "
            "term in detail and the far term at a higher level.",
        ),
        S(
            "Work package vs task, activity and deliverable",
            "These terms are often used loosely, and project management tools call almost everything a \"task\". The "
            "distinctions are still useful, especially for planning and exams.",
            T(
                ["Term", "What it is", "Named as", "Typical size", "Example"],
                ["Deliverable", "A product, result or capability the project must produce", "Noun", "Weeks to months", "Website build"],
                ["Work package", "The lowest WBS element, with an owner, estimates and acceptance criteria", "Noun", "Roughly 8 to 80 hours of effort", "Quote request form"],
                ["Activity", "A scheduled piece of work needed to complete a work package", "Verb + noun", "Hours to days", "Build CRM integration"],
                ["Task", "A smaller step within an activity, often personal", "Verb + noun", "Minutes to hours", "Test field validation in Safari"],
                ["Milestone", "A significant point or event with zero duration", "Event", "Zero duration", "Form approved for launch"],
            ),
            "The simplest rule: **work packages describe what is produced; activities and tasks describe how it is "
            "produced.** If a WBS element starts with a verb (\"design\", \"build\", \"test\"), it is probably an "
            "activity that belongs inside a work package. For more on the lower levels, see our guide to "
            "[project tasks and activities](/project-management/project-tasks-and-activities/).",
            "A work package is not always the same as a deliverable either. A large deliverable may be split into "
            "several work packages, while a small deliverable may be a single work package. See our guide to "
            "[project deliverables](/project-management/project-deliverables/).",
        ),
        S(
            "What a work package includes",
            "A work package description (also called a work package statement or WBS dictionary entry) records "
            "everything someone needs to understand, estimate, deliver and accept the work. Scale it to the project: a "
            "small internal project may need only the first eight fields; a contract or earned value project will "
            "need all of them.",
            T(
                ["Field", "What to write", "Why it matters"],
                ["ID and name", "WBS code and a short noun phrase", "Links the package to the WBS, schedule and budget"],
                ["Description and scope", "What is included and, just as important, what is excluded", "Prevents gaps, overlaps and [scope creep](/project-management/scope-creep/)"],
                ["Deliverable", "The specific output", "Makes completion visible"],
                ["Acceptance criteria", "Measurable conditions for \"done\" and who accepts", "Avoids arguments at the end"],
                ["Owner", "One named person", "Single point of accountability"],
                ["Resources", "People, roles, equipment and materials", "Feeds resource planning and costing"],
                ["Effort and duration", "Hours of work and elapsed time", "Effort drives cost; duration drives the schedule"],
                ["Cost estimate", "Labour, materials and other costs", "Rolls up to the control account and budget"],
                ["Start and finish dates", "Planned dates from the schedule", "Sets expectations and supports tracking"],
                ["Dependencies", "Predecessors, successors and external inputs", "Feeds the network diagram and [critical path](/project-management/critical-path-method/)"],
                ["Assumptions and constraints", "What the estimate depends on", "Explains variances later"],
                ["Risks", "Key risks specific to this package", "Feeds the risk register"],
                ["Progress method and reporting", "How progress is measured and how often it is reported", "Consistent status and earned value"],
                ["Approval", "Who approved the package and when", "Shows that the work is authorised"],
            ),
            "You do not need to build this from scratch. Our free [work package template](/templates/work-package-template/) "
            "includes these fields, and the [WBS template](/templates/work-breakdown-structure-template/) holds the "
            "structure the packages sit in.",
        ),
        S(
            "How big should a work package be?",
            "There is no formal standard for work package size. The right size is the one that lets you estimate "
            "accurately, assign clearly and see progress early, without creating more administration than the work "
            "is worth. Four rules of thumb help.",
            T(
                ["Rule of thumb", "What it says", "Why"],
                ["8/80 rule", "Between about 8 and 80 hours of effort", "Smaller packages add overhead; larger ones are hard to estimate and hide problems"],
                ["Reporting-period rule", "No longer than one or two reporting periods", "Problems show up in the next status report, not months later"],
                ["Single-owner rule", "One person can be accountable for it", "If two managers own it, it is probably two work packages"],
                ["Measurable-output rule", "Completion can be verified objectively", "\"Done\" should not be a matter of opinion"],
            ),
            "Treat these as guides, not laws. The 8/80 rule comes from practitioner experience rather than from a "
            "standards body, and large engineering or construction projects often have much bigger packages that are "
            "still well controlled. The real test is: **can you estimate it, assign it and track it?** If yes, stop "
            "decomposing.",
            T(
                ["Signs a work package is too big", "Signs a work package is too small"],
                ["Estimates vary wildly between estimators", "There are hundreds of packages to track"],
                ["It spans several months or several teams", "Reporting takes longer than the work"],
                ["Status stays at \"in progress\" for many periods", "Packages are really individual tasks"],
                ["It has several unrelated outputs", "The WBS has been decomposed to the level of to-do lists"],
            ),
        ),
        S(
            "How to create work packages step by step",
            OL(
                "**Start from an agreed scope.** Work from an approved scope statement and requirements. Work packages cannot be better than the [project scope](/project-management/project-scope/) they come from.",
                "**Decompose the deliverables.** Break each major deliverable into smaller components until each branch reaches a piece of work that passes the sizing tests above. Name each element as a noun.",
                "**Check the 100% rule.** Confirm the children of every element add up to all of its work, with no gaps or overlaps. Include project management, testing, training and handover packages.",
                "**Assign an owner to each package.** Choose the person who will be accountable for delivery, and agree it with them and their line manager. A [RACI matrix](/project-management/raci-matrix/) helps where several roles are involved.",
                "**Write the work package description.** Fill in the fields from the table above, starting with the description, exclusions, deliverable and acceptance criteria.",
                "**Estimate with the people doing the work.** Ask the owner and team to estimate effort, duration and cost. Bottom-up [effort estimation](/project-management/effort-estimation/) at this level is usually the most accurate method. Our [project cost estimate template](/templates/project-cost-estimate-template/) turns effort into cost.",
                "**Identify activities and dependencies.** Break each package into activities, link them with dependencies and feed them into the [project schedule](/project-management/project-scheduling/).",
                "**Review and approve.** Review packages with owners and the sponsor, resolve gaps, then include them in the scope, schedule and cost [baselines](/project-management/project-baseline/).",
                "**Authorise and track.** Release each package when it is due to start, then track progress, cost and issues against its baseline.",
            ),
            TIP(
                "Write the exclusions as carefully as the inclusions. \"Excludes content writing and translation\" in "
                "a build work package prevents one of the most common arguments at acceptance."
            ),
        ),
        S(
            "Work package example: a website build",
            "This example is **illustrative**: the project, rates and figures are invented to show how one work "
            "package is defined, broken down and rolled up.",
            "A company is replacing its customer website. The WBS has six major deliverables: 1 Project management, "
            "2 Discovery, 3 Design, 4 Content, 5 Build and 6 Launch. The development lead owns deliverable 5 Build, "
            "which is managed as a control account and broken into four work packages.",
            H3("Step 1: decompose the deliverable"),
            T(
                ["WBS code", "Work package", "Owner", "Effort", "Cost"],
                ["5.1", "Page templates", "Front-end developer", "72 hours", "£4,680"],
                ["5.2", "CMS configuration", "Back-end developer", "40 hours", "£2,600"],
                ["5.3", "Quote request form", "Back-end developer", "56 hours", "£3,430"],
                ["5.4", "Analytics and tracking", "Front-end developer", "20 hours", "£1,300"],
                ["5 Build (control account)", "", "Development lead", "188 hours", "£12,010"],
            ),
            "Every package sits within the 8/80 range, each has one owner, and the four packages together cover all "
            "of the build work. Content writing is in deliverable 4, so it is excluded here.",
            H3("Step 2: write the work package description"),
            T(
                ["Field", "5.3 Quote request form"],
                ["Description", "An online form on the Contact and Product pages that lets visitors request a quote and sends each request to the CRM"],
                ["Excludes", "Form copy (supplied by 4 Content), CRM licence changes, email nurture sequences"],
                ["Deliverable", "Working form in the live environment, connected to the CRM"],
                ["Acceptance criteria", "Submissions create a CRM lead within 1 minute; required-field validation works; form meets the agreed accessibility standard; spam protection blocks automated test submissions; accepted by the sales operations manager"],
                ["Owner", "Back-end developer"],
                ["Resources", "Business analyst 6 h, back-end developer 40 h, tester 10 h, CRM sandbox account"],
                ["Effort and duration", "56 hours over 10 working days"],
                ["Cost", "£3,430 (analyst at £55/h, developer at £65/h, tester at £50/h)"],
                ["Dependencies", "Starts after 3.2 Form design is approved and 5.2 CMS configuration is complete; 6.1 Launch testing depends on it"],
                ["Assumptions", "CRM API access is available by day 1; field list does not change after activity A1"],
                ["Risks", "CRM API rate limits; late changes to form fields from sales"],
                ["Progress method", "Weighted milestones: fields agreed 10%, form built 40%, integration working 70%, tested 90%, accepted 100%"],
            ),
            H3("Step 3: break the work package into activities"),
            T(
                ["ID", "Activity", "Role", "Effort", "Predecessor"],
                ["A1", "Confirm form fields and validation rules", "Business analyst", "6 h", "None"],
                ["A2", "Build front-end form", "Developer", "16 h", "A1"],
                ["A3", "Build CRM integration", "Developer", "14 h", "A1"],
                ["A4", "Add spam protection and accessibility fixes", "Developer", "6 h", "A2"],
                ["A5", "Test form, integration and accessibility", "Tester", "10 h", "A3, A4"],
                ["A6", "Fix defects and obtain acceptance", "Developer", "4 h", "A5"],
            ),
            "The activities add up to 56 hours: 6 for the analyst, 40 for the developer and 10 for the tester. The "
            "cost works out as 6 × £55 + 40 × £65 + 10 × £50 = £330 + £2,600 + £500 = £3,430. These activities, not "
            "the work package itself, go into the Gantt chart with their dependencies.",
            H3("Step 4: track progress"),
            "At the end of week one, A1 and A2 are complete and A3 is half done. Under the weighted milestone rule, "
            "the package has reached \"fields agreed\" and \"form built\", so it is reported as 40% complete, giving an "
            "earned value of 40% × £3,430 = £1,372. If actual cost to date is £1,600, the package is slightly over "
            "budget for the work done, which the owner explains in the weekly [project status report](/project-management/project-status-report/).",
        ),
        S(
            "Work package examples by industry",
            T(
                ["Industry", "Deliverable", "Example work packages"],
                ["Software", "Mobile app release", "Login and account screens; payment integration; push notifications; app store submission"],
                ["Construction", "Office fit-out", "Partition walls, level 2; electrical first fix; data cabling; ceilings and lighting"],
                ["Marketing", "Product launch campaign", "Launch video; landing page; paid social campaign set-up; press kit"],
                ["Events", "Annual conference", "Venue contract; speaker programme; registration system; on-site signage"],
                ["Manufacturing", "New production line", "Equipment specification; conveyor installation; safety validation; operator training"],
                ["Research", "Clinical study set-up", "Protocol document; ethics submission; site selection; data management plan"],
                ["HR and change", "New HR system", "Data migration; manager training; policy updates; payroll interface"],
            ),
            "Notice that every example is a noun describing an output. Each would then get its own owner, estimates "
            "and acceptance criteria.",
        ),
        S(
            "Work packages in PRINCE2",
            "In [PRINCE2](/project-management/prince2/), the term has a slightly different, more formal meaning. A "
            "PRINCE2 work package is a set of information and instructions that the project manager uses to hand over "
            "responsibility for delivering one or more products to a team manager or team member. It is both a "
            "description of the work and an **authorisation** to do it.",
            "The project manager authorises work packages as part of controlling a stage. The team manager accepts, "
            "executes and delivers them in the managing product delivery process, then reports progress through "
            "checkpoint reports. A PRINCE2 work package typically contains:",
            L(
                "A description of the work and the products to be delivered, with their product descriptions",
                "Techniques, processes or standards to be used",
                "Agreed tolerances, such as time, cost and scope",
                "Constraints, interfaces and dependencies",
                "Reporting arrangements, such as how often checkpoint reports are produced",
                "Quality requirements and who carries out quality checks",
                "The date it was agreed between the project manager and team manager",
            ),
            "The two meanings fit together well: a PRINCE2 work package can cover one or several WBS work packages, "
            "and in both cases the point is clear, agreed, controllable chunks of work with a named person accountable "
            "for delivery.",
        ),
        S(
            "Tracking work packages and earned value",
            "Because each work package has its own budget and dates, it is the natural unit for measuring progress. "
            "The key is to agree, before work starts, how progress will be credited, so that \"percent complete\" "
            "means something.",
            T(
                ["Progress method", "How it works", "Best for"],
                ["0/100", "No credit until the package is finished", "Very short packages, under one reporting period"],
                ["50/50", "50% credit at start, 50% at finish", "Packages spanning about two reporting periods"],
                ["Weighted milestones", "Credit at defined, verifiable points", "Longer packages with clear intermediate outputs"],
                ["Units complete", "Credit by quantity delivered (metres laid, pages built)", "Repetitive work with countable outputs"],
                ["Physical percent complete", "Owner's assessment against defined criteria", "Work without natural milestones; needs clear rules"],
            ),
            "Rolled up to control accounts, these figures give planned value, earned value and actual cost for the "
            "whole project. See our guide to [earned value management](/project-management/earned-value-management/) "
            "for the formulas and how to read the results.",
        ),
        S(
            "Benefits of work packages",
            L(
                "**More accurate estimates.** Small, well-defined pieces of work are easier to estimate than whole deliverables, and errors partly cancel out when added up.",
                "**Clear accountability.** One owner per package means nobody has to ask who is responsible.",
                "**Easier delegation.** A good description lets the owner and team work with little supervision.",
                "**Earlier warning of problems.** Packages that fit a reporting period show slippage within weeks.",
                "**Better cost control.** Actual costs can be collected and compared package by package.",
                "**Stronger scope control.** Inclusions and exclusions make it obvious when a request is new scope.",
                "**Reuse.** Well-written packages become templates for similar future projects.",
            ),
        ),
        S(
            "Common work package mistakes",
            T(
                ["Mistake", "Consequence", "Fix"],
                ["Naming packages as activities (\"Build form\")", "The WBS turns into a to-do list and outputs are unclear", "Name packages as nouns; put verbs in the activity list"],
                ["Shared or unclear ownership", "Work falls between people", "Assign one accountable owner per package"],
                ["No acceptance criteria", "Disputes over whether the work is done", "Write measurable criteria and name who accepts"],
                ["Estimating without the team", "Optimistic, unowned estimates", "Have the people doing the work estimate it"],
                ["Missing project management, testing or training packages", "The budget and schedule are understated", "Apply the 100% rule to the whole scope"],
                ["Packages far too large", "Problems hide until late", "Split by output, phase or location to fit a reporting period"],
                ["Decomposing far-off work too early", "Wasted effort and false precision", "Use planning packages and rolling wave planning"],
                ["Changing packages without change control", "The baseline loses meaning", "Route changes through [change control](/project-management/change-control/)"],
            ),
        ),
        S(
            "Managing work packages in project management software",
            "Most tools do not have a field called \"work package\", but they all let you represent one. The usual "
            "pattern is to make each work package a parent item with its own owner, dates and custom fields, and to "
            "add the activities as child tasks.",
            L(
                "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool, maps well to a formal WBS: deliverables as projects or folders, work packages as parent tasks with custom fields for WBS code, budget and acceptance criteria, and activities as subtasks on an interactive Gantt chart with dependencies and baselines.",
                "**[monday.com](/project-management-tools/monday/)** works well when each work package is a group or an item, with subitems for activities and columns for owner, timeline, budget and status.",
                "**[Asana](/project-management-tools/asana/)** can represent work packages as sections or parent tasks within a project, with subtasks, dependencies and custom fields.",
                "**[ClickUp](/project-management-tools/clickup/)** lets you use lists or parent tasks for work packages, with subtasks, custom fields and Gantt views.",
                "**[Smartsheet](/project-management-tools/smartsheet/)** uses indented parent rows, so a WBS with work packages and activities looks much like the spreadsheet many planners already use.",
            ),
            "Whatever the tool, keep the WBS code in a field so that schedule, cost and status reports can be grouped "
            "by work package.",
        ),
    ],
    faq=[
        ("What is a work package in simple terms?",
         "A small, clearly defined chunk of project work with one owner, a specific output, estimates and acceptance "
         "criteria. It is the lowest level of the work breakdown structure."),
        ("What is an example of a work package?",
         "\"Quote request form\" on a website project, \"electrical first fix\" on an office fit-out or \"press kit\" on a "
         "product launch. Each produces a defined output that can be estimated, owned and accepted."),
        ("What is the difference between a work package and a task?",
         "A work package describes an output at the lowest level of the WBS. Tasks and activities are the steps needed to "
         "produce it. One work package usually contains several activities, and each activity may contain several tasks."),
        ("What is the difference between a work package and an activity?",
         "Work packages belong to the WBS and are named as nouns; activities belong to the schedule and are named as "
         "verbs. Activities are created by breaking down work packages."),
        ("What is the 8/80 rule?",
         "A rule of thumb that a work package should take between about 8 and 80 hours of effort. It is a guide to the "
         "right level of detail, not a formal standard."),
        ("Who is responsible for a work package?",
         "One named owner is accountable for delivering it, even if several people do the work. On larger projects, the "
         "owner reports to a control account manager or the project manager."),
        ("What should a work package include?",
         "At minimum an ID, name, description and exclusions, deliverable, acceptance criteria, owner, resources, effort, "
         "duration, cost, dates and dependencies. Larger projects add assumptions, risks, progress method and approval."),
        ("What is a control account?",
         "A management point in the WBS where scope, budget, actual cost and schedule are integrated and compared for "
         "earned value. Each control account contains one or more work packages, and each work package belongs to "
         "exactly one control account."),
        ("What is the difference between a planning package and a work package?",
         "A planning package is a budgeted placeholder for future work whose scope is known but not yet detailed. It is "
         "converted into work packages, with activities and estimates, as the work gets closer."),
        ("What is a work package in PRINCE2?",
         "A set of information and instructions that the project manager uses to authorise a team manager or team member "
         "to deliver one or more products, including tolerances, quality requirements and reporting arrangements."),
        ("How many work packages should a project have?",
         "As many as needed to cover 100% of the scope at a level you can estimate, assign and track. A small project "
         "might have 10 to 20; a large programme can have hundreds."),
        ("Is a work package the same as a deliverable?",
         "Not always. A work package always produces an output, but a large deliverable may be split into several work "
         "packages, and some outputs, such as a test report, exist mainly to support other deliverables."),
        ("What is the difference between a work package and a WBS dictionary?",
         "The work package is the piece of work itself. The WBS dictionary is the document that describes every WBS "
         "element, including each work package's scope, owner, estimates and acceptance criteria."),
    ],
)
