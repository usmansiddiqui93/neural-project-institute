from core import S, L, OL, T, TIP, H3

URL = "/project-management/communication-plan/"

RW = dict(
    title="Project Communication Plan: How to Write One (With Examples)",
    desc="How to write a project communication plan: what to include, 8 steps, a column-by-column template, filled-in examples, escalation rules and common mistakes.",
    intro=(
        "A project communication plan is a short document that sets out who needs information about your project, what "
        "they need, why, how and when they will get it, and who is responsible for sending it. This guide shows you what "
        "to include, how to write one in eight steps, a column-by-column template and two filled-in examples you can adapt."
    ),
    takeaways=[
        "A communication plan answers six questions for every audience: who, what, why, how, when and who sends it.",
        "Build it from your stakeholder analysis and RACI matrix, grouping people with similar information needs.",
        "The core of most plans is a communication matrix: one row per communication item, kept to a page or a sheet.",
        "Every plan needs a feedback route and escalation thresholds, so urgent issues do not wait for the next routine report.",
        "Assign an owner to every item, not just the project manager, and put recurring items in calendars as soon as the plan is agreed.",
        "Review the plan at each phase or whenever stakeholders change; a plan written once and never updated soon stops being followed.",
    ],
    sections=[
        S(
            "What is a project communication plan?",
            "A **project communication plan** is a document that lists each regular and planned communication on a "
            "project, with its audience, purpose, content, method, frequency and owner, plus how people give feedback and "
            "how urgent issues are escalated. It turns good intentions about keeping people informed into a schedule "
            "everyone can see and follow.",
            "The project manager usually drafts it during planning, once stakeholders have been identified, and agrees it "
            "with the sponsor. On a small project it can be a single table. On a large change programme it is a short "
            "document with a matrix, a calendar, escalation rules and key messages.",
            "The plan is one output of [project communication management](/project-management/project-communication-management/), "
            "which also covers delivering communication and checking that it works. This guide is about writing the "
            "document itself.",
            H3("Communication plan vs related documents"),
            "Several documents deal with communication, and the names are often used interchangeably. The table "
            "shows how they differ.",
            T(
                ["Document", "What it covers", "Relationship to the communication plan"],
                ["Communication plan (communication matrix)", "Who receives what, how, when and from whom", "The working schedule this guide explains"],
                ["Communications management plan", "PMI term for the wider plan: approach, rules, technology, constraints and the matrix", "A component of the [project management plan](/project-management/project-management-plan/); the communication plan is usually its core"],
                ["Stakeholder engagement plan", "How you will involve and influence each stakeholder group", "Sets the goals that the communication plan delivers"],
                ["PRINCE2 communication management approach", "How communication with stakeholders inside and outside the project will work", "The [PRINCE2](/project-management/prince2/) equivalent, part of the project initiation documentation"],
                ["RACI matrix", "Who is Responsible, Accountable, Consulted and Informed for each deliverable", "Its C and I columns are a starting list of audiences"],
            ),
            "On most projects you do not need all of these as separate documents. One communication plan with a matrix, "
            "a few rules and an escalation section usually covers them.",
        ),
        S(
            "Why a communication plan matters",
            "Communication problems rarely come from a lack of effort. They come from assumptions: the sponsor assumed "
            "they would hear about a slipping milestone, the team assumed the sponsor already knew, and the people affected "
            "by the change assumed nobody would tell them anything. A written plan replaces those assumptions with "
            "agreements. It helps you:",
            L(
                "**Set expectations early**, so stakeholders know when and how they will hear from you.",
                "**Make sure nobody is forgotten**, especially end users and people affected by the change.",
                "**Share the work of communicating**, because named owners deliver items, not just the project manager.",
                "**Get decisions on time**, by timing updates just before the decisions they support.",
                "**Escalate fast**, because thresholds and routes are agreed before anything goes wrong.",
            ),
            "Signs you need one now: the same questions arrive repeatedly, stakeholders hear news from the grapevine "
            "before the project, or meetings keep being called to share information that could have been a report.",
        ),
        S(
            "What to include in a communication plan",
            "Whatever the format, a complete plan covers the components below. On a small project several can be a "
            "single line.",
            T(
                ["Component", "Question it answers", "Example"],
                ["Communication objectives", "What must communication achieve on this project?", "Every manager can brief their team on move dates two weeks before each wave"],
                ["Audiences", "Who needs information, grouped by need?", "Sponsor, steering committee, project team, suppliers, line managers, all staff"],
                ["Information needs", "What does each audience need, and what do we need from them?", "Directors: exceptions, risks and decisions needed"],
                ["Key messages", "What must each audience understand and remember?", "No one loses desk space; teams sit together"],
                ["Communication items", "Which reports, meetings and updates will we run?", "Monthly steering report, weekly supplier review"],
                ["Method and channel", "How is each item delivered?", "Meeting plus one-page report; intranet page"],
                ["Frequency and timing", "How often, and on which day or milestone?", "Monthly, five working days before the steering meeting"],
                ["Owner", "Who prepares and sends it?", "Facilities lead"],
                ["Feedback route", "How do recipients ask questions or respond?", "Shared mailbox answered within two working days"],
                ["Escalation path", "How do urgent issues reach a decision-maker?", "Milestone delay over 5 days: sponsor within 24 hours"],
                ["Storage and conventions", "Where do documents live; which templates apply?", "Project site; status report template v2"],
                ["Review schedule", "When will the plan be updated?", "At each phase gate and when stakeholders change"],
            ),
            "Free template: our [communication plan template](/templates/communication-plan-template/) has columns for "
            "audience, information, channel, frequency, owner and feedback, in beginner, advanced and expert versions.",
        ),
        S(
            "How to write a communication plan in 8 steps",
            "This process takes an hour or two on a small project and a short workshop on a large one.",
            OL(
                "**Set communication objectives** linked to the project's goals.",
                "**Identify and group your audiences** from the stakeholder register and RACI matrix.",
                "**Define information needs and key messages** for each group.",
                "**Choose methods, frequency and timing** for each communication item.",
                "**Assign an owner** to every item.",
                "**Agree feedback routes and escalation rules.**",
                "**Review the draft with the sponsor and key stakeholders, then publish it.**",
                "**Schedule the items and review the plan** at each phase or when stakeholders change.",
            ),
            H3("Step 1: Set communication objectives"),
            "Start from the [project charter](/project-management/project-charter/) and ask what communication must "
            "achieve for the project to succeed. Good objectives are specific and observable, for example: \"the "
            "steering committee receives decision papers at least five working days before each meeting\" or \"every "
            "affected employee knows their move date four weeks in advance\". Two to four objectives are enough.",
            H3("Step 2: Identify and group your audiences"),
            "List everyone affected by or able to influence the project, using your stakeholder register. Then group "
            "people with similar needs, so the plan has 5-10 rows rather than 40. A power/interest grid from "
            "[stakeholder management](/project-management/project-stakeholder-management/) gives a sensible starting "
            "approach for each group:",
            T(
                ["Group on the grid", "Typical members", "Communication approach"],
                ["High power, high interest", "Sponsor, steering committee, key client contacts", "Manage closely: regular two-way meetings, early warning, decision papers"],
                ["High power, low interest", "Senior executives, finance, legal", "Keep satisfied: short summaries, exception reports, involve at key decisions"],
                ["Low power, high interest", "End users, affected staff, team members", "Keep informed: regular updates, FAQs, briefings, clear feedback route"],
                ["Low power, low interest", "Wider organisation, peripheral suppliers", "Monitor: occasional general updates, information available on request"],
            ),
            "Check the Consulted and Informed columns of your [RACI matrix](/project-management/raci-matrix/) for "
            "anyone missing. People most often forgotten are line managers of affected staff, support teams who will "
            "inherit the result, and external regulators or auditors.",
            H3("Step 3: Define information needs and key messages"),
            "For each group, write down what they need to know, what they need to do and what you need from them. "
            "Ask them where you can. Useful questions: which decisions do you make and when; how much detail do you "
            "want; how do you prefer to receive updates; and what happens if you hear about a problem late? Then "
            "draft the two or three key messages each group must understand (see the section on key messages below).",
            H3("Step 4: Choose methods, frequency and timing"),
            "Match the method to the purpose. Use interactive methods (meetings, calls, workshops) for decisions and "
            "sensitive news, push methods (reports, emails) for information people must receive, and pull methods "
            "(intranet pages, dashboards) for reference material. Our "
            "[communication management guide](/project-management/project-communication-management/) explains these "
            "methods in detail.",
            "Set frequency from the audience's decision cycle, not from habit. A monthly steering committee needs its "
            "report a few days before the meeting, not on the first of the month. Event-driven items, such as "
            "briefings before each [milestone](/project-management/project-milestones/), are often more useful than "
            "fixed intervals.",
            H3("Step 5: Assign an owner to every item"),
            "Name a person or role for each row. The project manager should own steering reports and sponsor meetings, "
            "but workstream leads, change leads, internal communications teams and supplier managers are often better "
            "placed to deliver other items. An item without an owner will not happen.",
            H3("Step 6: Agree feedback routes and escalation rules"),
            "For every item, decide how recipients respond: questions in the meeting, a shared mailbox, a comments "
            "thread or a survey. Then set escalation thresholds and response times, as described in the escalation "
            "section below.",
            H3("Steps 7 and 8: Agree, publish, schedule and review"),
            "Walk the sponsor and key stakeholders through the draft; they will often spot a missing audience or an "
            "unrealistic frequency. Publish the plan where the team can find it, send calendar invitations for every "
            "recurring item the same week, and set review dates at each phase gate.",
        ),
        S(
            "Communication plan template",
            "Most plans are a matrix with one row per communication item. Use the column guide below, then copy the "
            "blank row into a spreadsheet or your project tool.",
            T(
                ["Column", "What to write", "Tip"],
                ["Communication item", "The name of the report, meeting or update", "Use the name people will see in calendar invites"],
                ["Audience", "The group that receives it", "Use groups, not long lists of names"],
                ["Purpose", "Inform, consult, decide, approve or prepare", "If you cannot state a purpose, drop the item"],
                ["Content", "The information included", "Name the template, such as the status report"],
                ["Method", "Meeting, email, report, dashboard, intranet, call", "Interactive for decisions and bad news"],
                ["Frequency or timing", "Daily, weekly, monthly or trigger", "Tie to decision dates and milestones"],
                ["Owner", "Name or role", "Spread ownership across the team"],
                ["Feedback route", "How the audience responds", "Include a response time"],
            ),
            T(
                ["Communication", "Audience", "Purpose", "Content", "Method", "Frequency", "Owner", "Feedback route"],
                ["[Name of item]", "[Who receives it]", "[Inform / consult / decide]", "[Key information]", "[Meeting / email / report / dashboard]", "[Daily / weekly / monthly / milestone]", "[Name or role]", "[How to respond]"],
            ),
            "Recurring meetings in the plan need a standard agenda and record; our "
            "[meeting agenda template](/templates/meeting-agenda-template/) and "
            "[RACI matrix template](/templates/raci-matrix-template/) pair well with the communication plan.",
        ),
        S(
            "Communication plan example: office relocation",
            "This example is illustrative. A company is moving 250 staff from two buildings into a new office over six "
            "months, in three move waves. The project has a sponsor (the chief operating officer), a steering committee "
            "of directors, a project team of eight, a fit-out contractor, an IT supplier and 25 line managers.",
            T(
                ["Communication", "Audience", "Purpose", "Content", "Method", "Frequency", "Owner", "Feedback route"],
                ["Kick-off meeting", "Sponsor, project team, facilities, IT, HR", "Align on goals and roles", "Charter, scope, milestones, RACI", "Workshop", "Once, week 1", "Project manager", "Q&A in session"],
                ["Sponsor one-to-one", "Sponsor", "Early warning and decisions", "Top risks, issues, decisions needed", "Meeting", "Weekly, 30 minutes", "Project manager", "Actions in meeting notes"],
                ["Steering committee update", "Sponsor and directors", "Decide and approve", "RAG status, budget, risks, decisions needed", "Meeting plus one-page report", "Monthly; report sent 5 working days before", "Project manager", "Decisions recorded in minutes"],
                ["Team stand-up", "Project team", "Coordinate daily work", "Progress, blockers, next tasks", "15-minute call", "Daily", "Project coordinator", "Raise in call or team chat"],
                ["Supplier progress review", "Fit-out contractor, IT supplier", "Track deliverables", "Progress against schedule, issues, snags", "On-site meeting", "Weekly", "Facilities lead", "Issue log"],
                ["Manager briefing pack", "Line managers", "Equip managers to brief teams", "Key messages, FAQs, wave dates, floor plans", "Email pack plus 30-minute call", "4 weeks before each wave", "Change lead", "Briefing call Q&A"],
                ["Staff newsletter", "All staff", "Inform and prepare", "Move dates, what to pack, new facilities", "Email and intranet", "Fortnightly; weekly in the final month", "Internal comms", "Shared mailbox, reply in 2 working days"],
                ["Move information page", "All staff", "Reference", "Wave plan, FAQ, floor plans, contacts", "Intranet page", "Updated weekly", "Project coordinator", "Comment form"],
                ["Post-move survey", "Moved staff", "Gather feedback", "Satisfaction, issues, suggestions", "Online form", "Once, 2 weeks after each wave", "Project coordinator", "Results shared in newsletter"],
            ),
            "The plan also contains three rules: decisions are recorded in the decision log within one working day; all "
            "risks and issues live in one [RAID log](/project-management/raid-log/); and any issue that threatens a move "
            "date goes to the sponsor the same day by phone, then in writing.",
            H3("The communication calendar for each move wave"),
            "A matrix shows what happens regularly. For milestone-driven projects, add a calendar counting back from "
            "each key date, so nothing is sent too late or all at once.",
            T(
                ["When", "Communication", "Audience", "Owner"],
                ["Move date minus 6 weeks", "Wave confirmed at steering committee; go/no-go criteria agreed", "Steering committee", "Project manager"],
                ["Minus 4 weeks", "Manager briefing pack and call", "Line managers in the wave", "Change lead"],
                ["Minus 3 weeks", "Managers brief their teams; move page updated with seating plans", "Staff in the wave", "Line managers"],
                ["Minus 2 weeks", "Packing instructions and crates delivered", "Staff in the wave", "Facilities lead"],
                ["Minus 1 week", "Reminder email with day-by-day checklist; IT readiness confirmed", "Staff in the wave; IT supplier", "Internal comms; IT lead"],
                ["Move day", "Welcome message, help desk location and hours", "Moved staff", "Project coordinator"],
                ["Plus 2 weeks", "Post-move survey; results to the steering committee", "Moved staff; steering committee", "Project coordinator"],
            ),
        ),
        S(
            "Communication plan example: Agile product team",
            "Agile teams already have much of their communication built into their events, so their plan is shorter. "
            "This illustrative example is for a Scrum team of seven building a customer portal in two-week sprints, "
            "with a product owner, a business sponsor and a customer service department that will use the portal.",
            T(
                ["Communication", "Audience", "Method", "Frequency", "Owner"],
                ["Daily Scrum", "Developers", "15-minute meeting", "Daily", "Developers"],
                ["Sprint review", "Team, sponsor, customer service leads", "Demonstration and discussion", "End of each sprint", "Product owner"],
                ["Product backlog and roadmap", "Anyone interested", "Shared board and roadmap page (pull)", "Updated continuously", "Product owner"],
                ["Sponsor update", "Business sponsor", "Short written update plus 30-minute call", "Every sprint", "Product owner"],
                ["Release notes", "Customer service staff", "Email and knowledge base article", "Each release", "Product owner with service lead"],
                ["Dependency check-in", "Teams that own connected systems", "Meeting", "Fortnightly", "Scrum master"],
            ),
            "The [sprint review](/project-management/scrum/sprint-review/) does much of the work a status report would "
            "do on a predictive project. The plan exists mainly to cover people outside the team: the sponsor, the "
            "users and the teams the product depends on. See our guide to "
            "[agile meetings and ceremonies](/project-management/agile/agile-meetings-and-ceremonies/) for how each "
            "event works.",
        ),
        S(
            "Escalation rules and thresholds",
            "Routine reports are too slow for urgent problems. The escalation section of your plan states, in advance, "
            "which issues skip the normal rhythm, who they go to and how quickly. Agree thresholds with the sponsor and "
            "align them with your [project governance](/project-management/project-governance/). The thresholds below "
            "are illustrative.",
            T(
                ["Level", "Example trigger", "Escalate to", "Method", "Within"],
                ["1: Team", "Task blocked for more than 2 days", "Project manager", "Team chat or stand-up", "Same day"],
                ["2: Project", "Milestone forecast to slip by up to 5 working days, or a new high risk", "Sponsor", "Call, then written note", "24 hours"],
                ["3: Governance", "Milestone slip over 5 days, budget variance over the agreed tolerance, or a safety or legal issue", "Steering committee via sponsor", "Exception report and extraordinary meeting if needed", "2 working days"],
            ),
            "Record every escalated item in the [issue log](/project-management/issue-log/) with its owner and the "
            "decision taken, so the routine reports stay consistent with what was escalated.",
        ),
        S(
            "Writing key messages",
            "Key messages are the few points each audience must understand and remember. Writing them down keeps "
            "everyone who communicates on the project saying the same thing. A simple message map works well:",
            OL(
                "Write one **core message** in a single sentence, in the audience's language.",
                "Add **three supporting points** that explain or justify it.",
                "Add **evidence or detail** for each point: a date, fact or example.",
                "Note **what you want the audience to do** next.",
            ),
            "Illustrative example for staff in the office relocation:",
            T(
                ["Element", "Content"],
                ["Core message", "Your team is moving together to the new office in May, and your working arrangements stay the same."],
                ["Supporting point 1", "Teams keep their current desk-to-person ratio and sit together."],
                ["Supporting point 2", "The new office has more meeting rooms and quiet space."],
                ["Supporting point 3", "IT equipment is moved and tested for you before your first day."],
                ["Action", "Read the move page and pack your crate by the Thursday before your move."],
            ),
            "Check key messages with the sponsor before use, and update them when facts change. Out-of-date messages "
            "repeated by line managers do more damage than no message at all.",
        ),
        S(
            "Tailoring the plan to your project",
            "The structure of a communication plan stays the same, but the emphasis changes with the project.",
            T(
                ["Project type", "What to emphasise"],
                ["Small internal project", "One-page matrix, a weekly update and a clear escalation line. Avoid over-engineering"],
                ["Organisational change (relocation, restructure, new system)", "Affected staff, line manager briefings, key messages, calendars around each go-live, feedback routes. See [change management vs change control](/project-management/change-management-vs-change-control/)"],
                ["Agile product development", "Stakeholders outside the team, sprint reviews, roadmap visibility, release notes"],
                ["Client or agency project", "Single point of contact on each side, approval turnaround times, change request route, what counts as formal instruction"],
                ["Remote or global team", "Time zones, written decisions, recorded meetings, plain language. See [remote project management](/project-management/industries/remote-project-management/)"],
                ["Regulated or safety-critical project", "Formal records, mandatory notifications, approval sign-offs and document control"],
            ),
        ),
        S(
            "Putting the plan into action",
            "A plan only works if it becomes part of the project's rhythm. In the first week after approval:",
            L(
                "Present the plan at the kick-off meeting so everyone knows what to expect and where to find things.",
                "Send calendar invitations for every recurring meeting and report deadline.",
                "Create the templates the plan names, such as the [project status report](/project-management/project-status-report/), and store them in one place.",
                "Tell each owner which items they own and when the first one is due.",
            ),
            "Revisit the plan at each phase gate, when a stakeholder joins or leaves, after a major change in scope or "
            "risk, and whenever you see warning signs such as repeated questions or poor meeting attendance. Plan "
            "communication for the end of the project as well: handover, [project closure](/project-management/project-closure/) "
            "and a [lessons learned](/project-management/lessons-learned/) session.",
            "Read our guide to [project communication management](/project-management/project-communication-management/) for how to measure whether your communication is working and fix it when it is not.",
        ),
        S(
            "Tools for building and running a communication plan",
            "A spreadsheet is enough to write the plan. Running it is easier in the tools your team already uses, so "
            "updates, comments and decisions sit next to the work:",
            L(
                "[Wrike](/project-management-tools/wrike/), our top-rated project management tool, keeps comments and "
                "approvals on tasks, offers shareable dashboards on paid plans and includes AI features that summarise "
                "long comment threads and help draft status updates.",
                "[Asana](/project-management-tools/asana/) includes status updates, which suit regular sponsor and "
                "steering reports.",
                "[monday.com](/project-management-tools/monday/) combines forms, boards and dashboards, useful for "
                "collecting questions and showing status at a glance.",
                "[Microsoft Planner](/project-management-tools/microsoft-planner/) connects each plan to a Microsoft 365 "
                "group, with shared files and an optional Teams channel, which suits organisations already on Microsoft 365.",
            ),
            "Whichever you choose, keep one source of truth for status and decisions, and link to it from every message.",
        ),
        S(
            "Common communication plan mistakes",
            L(
                "**Writing it once and never updating it.** Stakeholders, risks and phases change; the plan must too.",
                "**Listing the project manager as owner of everything.** Share the work and the plan becomes realistic.",
                "**Forgetting end users and affected staff.** They are often the largest audience and the one that decides whether the change sticks.",
                "**Too many items.** If people receive five updates a week, they read none. Merge or drop items without a clear purpose.",
                "**Relying on email for important or sensitive messages.** Bad news and decisions need a conversation.",
                "**No feedback route.** Communication that only flows one way misses early warnings.",
                "**Vague escalation.** Without thresholds and response times, urgent issues wait for the next monthly report.",
                "**Timing updates to the calendar, not to decisions.** A report that arrives after the meeting is wasted effort.",
            ),
            TIP("Keep the plan to one page or one sheet where you can. If it needs scrolling, it probably contains "
                "items nobody will deliver."),
        ),
    ],
    faq=[
        ("What is a communication plan in project management?",
         "A document that defines who receives project information, what they receive, why, how, how often and who "
         "provides it, together with feedback routes and escalation rules."),
        ("What are the key elements of a communication plan?",
         "Objectives, audiences, information needs, key messages, communication items, method, frequency, owner, "
         "feedback route, escalation path, storage conventions and a review schedule."),
        ("Who creates the communication plan?",
         "The project manager usually drafts it, with input from the sponsor, team leads, change or internal "
         "communications specialists and key stakeholders, and the sponsor agrees it."),
        ("When should the communication plan be created?",
         "During planning, once stakeholders have been identified, and before regular reporting starts. Update it "
         "throughout the project."),
        ("What is a communication matrix?",
         "A table that lists each communication item with its audience, purpose, content, method, frequency, owner and "
         "feedback route. It is the core of most communication plans."),
        ("How long should a communication plan be?",
         "As short as it can be. For most projects a one-page matrix plus a few rules on storage and escalation is "
         "enough; large change programmes add a calendar and key messages."),
        ("Is a communication plan the same as a stakeholder engagement plan?",
         "No, but they overlap. The engagement plan sets out how to involve and influence stakeholders; the "
         "communication plan sets out the information flows that support it."),
        ("What is the difference between a communication plan and a communications management plan?",
         "In PMI terms the communications management plan is the wider document, covering approach, rules and "
         "technology, and it is part of the project management plan. The communication plan or matrix is its working "
         "schedule. On most projects one document does both jobs."),
        ("Do Agile projects need a communication plan?",
         "Agile events such as the daily Scrum and sprint review are built-in communication, so the plan is lighter. "
         "It is still useful for sponsors, users and dependent teams outside the core team."),
        ("How often should a communication plan be reviewed?",
         "At each phase gate or major milestone, and whenever stakeholders, risks or priorities change significantly."),
        ("What should a communication plan include for escalation?",
         "Clear thresholds, who to escalate to at each level, the method and expected response times, so urgent issues "
         "do not wait for the next routine report."),
        ("What should you do if stakeholders do not follow the plan?",
         "Ask why. Usually the frequency, format or channel does not suit them. Agree a change with them, update the "
         "plan and, if it affects decisions, involve the sponsor."),
        ("What tools can I use to create a communication plan?",
         "A spreadsheet or our free [communication plan template](/templates/communication-plan-template/) is enough "
         "to write it. Project management tools such as Wrike, Asana, monday.com or Microsoft Planner help you run it."),
    ],
)
