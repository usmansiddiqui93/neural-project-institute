from core import S, L, OL, T, TIP, H3

URL = "/project-management/kanban/kanban-boards/"

RW = dict(
    title="Kanban Board: What It Is, Examples and How to Build One",
    desc="What is a Kanban board? Learn its parts, see examples for software, marketing and IT, and build your own step by step with WIP limits and policies.",
    intro=(
        "A Kanban board is a visual display of your workflow, with columns for each stage, cards for each work item "
        "and limits on how much work can be in progress at once. It shows at a glance what is being worked on, where "
        "work is waiting and where it is stuck. This guide explains every part of a board, gives examples for "
        "different teams and walks you through designing your own, with a fully worked example."
    ),
    takeaways=[
        "A Kanban board makes your real workflow visible: columns for stages, cards for work items, WIP limits, commitment and delivery points, and explicit policies.",
        "The Kanban Guide calls the board the visualisation of your Definition of Workflow and sets no required layout, so design it from how work actually flows, including waiting stages.",
        "WIP limits are what turn a board into a flow-management system: work is pulled when there is capacity rather than pushed onto people.",
        "A board gives you four flow measures for free: work in progress, throughput, work item age and cycle time.",
        "Run the board daily by walking it from right to left and focusing on blocked and ageing items, and review its design regularly.",
        "Any good tool can host a board; Wrike, monday.com, Asana, ClickUp, Jira, Trello and Microsoft Planner all offer board views, or start with our free template.",
    ],
    sections=[
        S(
            "What is a Kanban board?",
            "A **Kanban board** is a visual tool for managing the flow of work. Each column represents a stage in your "
            "process, each card represents one work item, and limits on work in progress (WIP) stop any stage taking on "
            "more than it can finish. The board makes progress, queues, bottlenecks and blockers visible to everyone.",
            "The word kanban is Japanese for a signboard or visual signal. The idea grew out of the Toyota Production "
            "System under industrial engineer Taiichi Ohno, where cards signalled when to replenish parts. In the "
            "2000s, David J. Anderson adapted it to knowledge work, first with a software team at Microsoft and later "
            "at Corbis. Our guide to [what Kanban is](/project-management/kanban/what-is-kanban/) covers the history "
            "and the wider method.",
            "The Kanban Guide (edition 2025.5, by John Coleman and Daniel Vacanti) describes the board as the "
            "visualisation of a team's **Definition of Workflow**: the shared agreement about what work items are, "
            "where they start and finish, the states in between, how WIP is controlled, the policies that apply and "
            "the service level the team expects. It deliberately sets no required layout. That is good news: your board "
            "should look like your process, not like someone else's template.",
        ),
        S(
            "Parts of a Kanban board",
            "David J. Anderson's widely quoted list has five components: visual signals (cards), columns, WIP limits, a "
            "commitment point and a delivery point. Most working boards add policies, swimlanes and blocker markers.",
            T(
                ["Element", "What it is", "Practical tip"],
                ["[Cards](/project-management/kanban/kanban-cards/)", "One card per work item, showing title, owner, type and key dates", "Keep items small enough to move every few days"],
                ["Columns", "The stages work passes through, left to right", "Model the real process, including queues and hand-offs"],
                ["[WIP limits](/project-management/kanban/wip-limits/)", "The maximum number of items allowed in a column or group of columns", "Write the number in the column header where everyone can see it"],
                ["Backlog or options", "Requests and ideas not yet committed to", "Keep it short and ordered; it is not a to-do list"],
                ["Commitment point", "The line where the team agrees to do an item and the clock starts", "Usually between Ready and the first active column"],
                ["Delivery point", "Where the item reaches the customer and the clock stops", "Define it as value delivered, not just work finished"],
                ["Policies", "Short rules for entering and leaving each column", "Write them on the board, beneath the column names"],
                ["[Swimlanes](/project-management/kanban/kanban-swimlanes/)", "Optional horizontal rows for classes of service or work types", "Add only if they change how people act"],
                ["Blocker markers", "A sticker, flag or tag showing an item cannot progress", "Record why and since when, so you can analyse patterns later"],
                ["Done", "Finished work, kept briefly for review", "Clear it at a regular interval so the board stays readable"],
            ),
            H3("Upstream and downstream"),
            "Many boards have two zones. **Upstream**, to the left of the commitment point, holds options: ideas and "
            "requests the team might do, which can still be dropped. **Downstream**, to the right, holds commitments the "
            "team will finish, governed by WIP limits. Separating the two stops the board turning into a wish list and "
            "makes delivery times measurable. See [Kanban planning](/project-management/kanban/kanban-planning/) for "
            "how replenishment moves work across the line.",
            H3("Doing and done sub-columns"),
            "A column such as Develop can be split into **doing** and **done**. Items in done are finished at that stage "
            "and waiting to be pulled by the next one. This shows queues that would otherwise be invisible, and queues "
            "are often where most of the delay hides.",
        ),
        S(
            "How a Kanban board works",
            "Kanban is a **pull system**. Instead of a manager pushing tasks onto people, team members pull the next "
            "item when they have capacity, and WIP limits make that capacity explicit. Our guide to "
            "[pull vs push systems](/project-management/kanban/pull-system-vs-push-system/) explains why this reduces "
            "overload and multitasking.",
            "Here is one card's journey across a simple software board with the columns Options, Ready, Develop, "
            "Review, Test and Done:",
            OL(
                "A stakeholder adds a request to **Options**. It is a possibility, not a promise.",
                "At the weekly replenishment meeting the team selects it and moves it to **Ready**, which has a limit of 5. "
                "It is now ordered and fully described.",
                "When a developer finishes an item and Develop drops below its limit of 4, they pull the top card from "
                "Ready. This is the **commitment point**, and the cycle-time clock starts.",
                "When coding is finished, the card moves to **Develop: done**, signalling it is ready for review.",
                "A reviewer with capacity pulls it into **Review**. A question for the product owner blocks it for a day, "
                "so the card gets a red blocker marker with the reason.",
                "Once unblocked and reviewed, it is pulled into **Test**, then into **Done** when it is released. That is "
                "the **delivery point**, and the clock stops.",
            ),
            "At no point did anyone assign the work. The board, the order of Ready and the limits did the coordinating.",
        ),
        S(
            "Types of Kanban boards",
            T(
                ["Type", "Typical columns", "Best for"],
                ["Simple three-column board", "To do, Doing, Done", "Getting started, small teams, personal Kanban"],
                ["Team workflow board", "Options, Ready, several active stages with doing and done, Done", "Most delivery teams"],
                ["Upstream or discovery board", "Ideas, Researching, Shaping, Ready for delivery", "Product and design teams deciding what to build"],
                ["Portfolio or project board", "Proposed, Approved, In delivery, Releasing, Benefits review", "PMOs and leaders tracking projects or epics, not tasks"],
                ["Service desk board", "New, Triage, In progress, Waiting on customer, Resolved", "IT support, HR and facilities requests"],
            ),
            H3("Physical vs digital boards"),
            T(
                ["", "Physical board", "Digital board"],
                ["Best for", "Co-located teams", "Remote, hybrid or multi-site teams"],
                ["Strengths", "Highly visible, quick to change, encourages conversation", "Automatic history, flow metrics, integrations and remote access"],
                ["Weaknesses", "No automatic data; hard to share across sites", "Easy to ignore if nobody displays it; tool limits can shape the process"],
                ["Tip", "Photograph it weekly to keep a record", "Show it on a screen at the daily meeting"],
            ),
            "Many teams start on a whiteboard to experiment with the design, then move to software once the columns "
            "and policies have settled. Kanban boards are part of the wider practice of "
            "visual management.",
        ),
        S(
            "Kanban board examples",
            "These are starting points to adapt, not prescriptions. WIP limits depend on team size; the figures assume "
            "a team of about five and are illustrative.",
            T(
                ["Team", "Columns", "Starting WIP ideas", "Example policy"],
                ["Software", "Options, Ready, Develop (doing / done), Review, Test, Deploy, Done", "Ready 5, Develop 4, Review 2, Test 3", "Nothing enters Review without passing automated tests"],
                ["Marketing", "Requests, Brief, Create (doing / done), Review, Scheduled, Live", "Brief 3, Create 6, Review 3", "No brief without audience, channel and deadline"],
                ["IT support", "New, Triage, In progress, Waiting on customer, Resolved", "In progress 2 per person", "Triage within 4 working hours"],
                ["HR recruitment", "Role approved, Sourcing, Screening, Interviews, Offer, Hired", "Interviews 6 roles", "Hiring manager feedback within 2 days of interview"],
                ["Product discovery", "Ideas, Researching, Testing, Decided, Ready for delivery", "Researching 3, Testing 2", "Each idea has a hypothesis before research starts"],
                ["Construction design approvals", "Drafting, Internal check, Client review, Revisions, Approved", "Client review 5", "Chase client after 5 working days"],
                ["Legal", "Intake, Assessment, Drafting, Negotiation, Signed", "Drafting 2 per lawyer", "Urgent matters use the expedite lane, limit 1"],
                ["Personal", "To do, Doing, Done", "Doing 3", "Finish before starting something new"],
            ),
            "Our free [Kanban board template](/templates/kanban-board-template/) gives you a ready-made board with "
            "columns, WIP limits and card details in Google Sheets, Excel and PDF.",
        ),
        S(
            "How to create a Kanban board, step by step",
            "This process works for a whiteboard or a tool. Involve the whole team: a board designed by one person "
            "rarely reflects how work really flows.",
            OL(
                "**Define your work items.** Agree what a card represents, such as a feature, a campaign asset or a "
                "support ticket, and roughly how large it should be.",
                "**Trace real work.** Take two or three recently finished items and walk through how each actually moved "
                "from request to delivery, including every wait and hand-off. A "
                "value stream map helps on complex processes.",
                "**Turn stages into columns.** Create one column per real stage, including waiting stages such as "
                "\"Ready for test\" or \"Waiting on client\". Merge stages that never hold work for long.",
                "**Split busy stages into doing and done** so queues between stages become visible.",
                "**Mark the commitment and delivery points.** Decide where the clock starts and stops.",
                "**Put current work on the board.** Add a card for everything genuinely in progress today. The count is "
                "often a surprise.",
                "**Set WIP limits.** Start a little below today's WIP in each active stage, or around one to one and a "
                "half items per person working that stage.",
                "**Write policies.** One or two lines per column on what must be true for a card to enter or leave it. "
                "A [workflow template](/templates/workflow-template/) helps you document them.",
                "**Add swimlanes only if needed**, for example an expedite lane with a limit of one.",
                "**Agree how you will run it:** a short daily meeting, a replenishment rhythm and a monthly review of "
                "the board design itself.",
            ),
            TIP("Resist designing the ideal process. Map how work flows today, then improve it in small steps. Kanban starts with what you do now."),
        ),
        S(
            "Kanban board policies with examples",
            "Policies are the rules of the board. The Kanban Guide lists them as part of the minimum Definition of "
            "Workflow, and Kanban University's general practices include making policies explicit. Without them, "
            "people interpret column names differently and the board stops meaning the same thing to everyone. Keep each "
            "policy to a line or two, write it on the board and change it only by team agreement.",
            T(
                ["Policy type", "Example", "Why it helps"],
                ["Entry criteria", "A card enters Ready only with a description, an owner for questions and acceptance criteria", "Stops half-understood work being started"],
                ["Exit criteria", "A card leaves Develop only when code is merged and unit tests pass", "Makes done at each stage unambiguous"],
                ["Pull order", "Pull the oldest item in the column to the left unless an expedite item is waiting", "Prevents favourites jumping the queue"],
                ["WIP breach", "If a limit must be exceeded, say so at the next daily meeting and record why", "Keeps exceptions visible and rare"],
                ["Blockers", "Mark a blocked card within an hour; escalate if blocked for more than 2 days", "Turns hidden waits into visible problems"],
                ["Expedite", "Only the service owner can add an expedite card; maximum one at a time", "Protects the system from everything becoming urgent"],
                ["Service level expectation", "85% of items finish within 10 days of the commitment point", "Gives stakeholders a realistic answer to when will it be done"],
            ),
            "The service level expectation is a forecast, not a promise: the Kanban Guide describes it as a time period "
            "plus a probability, based on historical cycle times once you have them.",
        ),
        S(
            "Worked example: designing a marketing team's board",
            "This illustrative example uses an invented team and figures to show the design process and the arithmetic.",
            "A six-person in-house marketing team produces campaign assets: emails, landing pages, social posts and "
            "short videos. Stakeholders complain that nothing arrives on time, yet everyone feels overloaded. The team "
            "lead traces five recent assets and finds that most of their elapsed time was spent waiting: for briefs to "
            "be clarified, for reviewers and for sign-off.",
            H3("Step 1: count today's work"),
            T(
                ["Stage", "Items in progress today", "People who work this stage"],
                ["Brief", "4", "1 (team lead)"],
                ["Create", "12", "4 (writers and designers)"],
                ["Waiting for review", "7", "None: a queue"],
                ["Review", "4", "2 (team lead and brand manager)"],
                ["**Total committed WIP**", "**27**", ""],
            ),
            "Over the last eight weeks the team finished an average of 9 items a week. Little's Law (average cycle time "
            "= average WIP ÷ average throughput) gives 27 ÷ 9, an average of about **3 weeks** from commitment to approval.",
            H3("Step 2: design the board"),
            T(
                ["Column", "WIP limit", "Policy to enter or leave"],
                ["Requests (options)", "None", "Anyone can add; reviewed weekly"],
                ["Ready", "5", "Brief template complete: audience, channel, deadline, assets"],
                ["Brief", "3", "Commitment point: the card enters here only when the team lead pulls it"],
                ["Create: doing", "7", "Owner named on the card; swarm rather than start a new item when blocked"],
                ["Create: done", "4", "Self-checked against the brand checklist"],
                ["Review", "6", "Reviewer responds within 1 working day"],
                ["Scheduled", "None", "Delivery point: approved and booked into the content calendar"],
                ["Live", "None", "Cleared every Friday"],
            ),
            "The new limits cap committed WIP at 3 + 7 + 4 + 6 = **20 items**, a cut of about a quarter. The team "
            "deliberately avoided halving WIP overnight, which tends to stall work and lose goodwill. If throughput "
            "holds at about 9 a week, average cycle time should move towards 20 ÷ 9, or a little over **2 weeks**.",
            H3("Step 3: run it and review"),
            L(
                "When Review is full, writers stop starting new work and help clear review, for example by peer-checking "
                "against the brand checklist.",
                "Blocked cards get a red marker with the reason and date; the team reviews blocker patterns monthly using "
                "blocker clustering.",
                "After four weeks, the team compares cycle time and throughput with the baseline and decides whether to "
                "tighten limits further.",
            ),
            "Little's Law describes averages in a reasonably stable system, so treat the forecast as a direction of "
            "travel rather than a promise. Our [content calendar template](/templates/content-calendar-template/) "
            "pairs well with the Scheduled column.",
        ),
        S(
            "Kanban board metrics",
            "A well-run board produces flow data as a by-product. The Kanban Guide names four measures every Kanban "
            "system should track.",
            T(
                ["Measure", "Definition", "How the board shows it", "Our guide"],
                ["Work in progress", "Items started but not finished", "Count of cards between the commitment and delivery points", "[WIP limits](/project-management/kanban/wip-limits/)"],
                ["Throughput", "Items finished per unit of time", "Cards reaching the delivery point each week", "[Kanban metrics](/project-management/kanban/kanban-metrics/)"],
                ["Work item age", "Time since an unfinished item started", "Days since each in-progress card crossed the commitment point", "[WIP aging chart](/project-management/kanban/wip-aging-chart/)"],
                ["Cycle time", "Time from start to finish for completed items", "Days from commitment point to delivery point", "[Cycle time](/project-management/kanban/cycle-time/)"],
            ),
            "Two charts make these measures easy to read. A [cumulative flow diagram](/project-management/kanban/cumulative-flow-diagram/) "
            "shows the number of items in each column over time; widening bands reveal growing queues. An aging chart "
            "plots each in-progress item by column and age, so you can rescue items before they become late. For the "
            "full set, see our guide to [Kanban metrics](/project-management/kanban/kanban-metrics/).",
        ),
        S(
            "Running your Kanban board day to day",
            "A board only works if it reflects reality and people act on it. Most teams settle on a small set of "
            "routines, which our guide to [Kanban ceremonies](/project-management/kanban/kanban-ceremonies/) covers in detail.",
            L(
                "**Daily Kanban meeting (about 15 minutes):** walk the board from right to left, starting with items "
                "closest to delivery. Ask what is blocked, what is ageing and what can be finished today, rather than "
                "going round each person.",
                "**Update as work happens:** move a card when its state changes, not just before the meeting.",
                "**Handle blockers visibly:** mark them, name an owner for the unblocking action and escalate if one is "
                "older than an agreed threshold.",
                "**Replenish on a rhythm:** refill Ready weekly or when it falls below a trigger level, ordered by value "
                "and urgency.",
                "**Review the board design monthly:** are columns, limits and policies still right? Change one thing at "
                "a time and watch the effect.",
            ),
            "The team that does the work owns the board. Anyone can view it, but changes to columns, limits or "
            "policies should be agreed together.",
        ),
        S(
            "Kanban board vs Scrum board and other tools",
            T(
                ["", "Kanban board", "Scrum board"],
                ["Timebox", "Continuous flow, no sprints", "Reset each sprint"],
                ["What it holds", "All work in the system, from options to delivery", "Only the Sprint Backlog"],
                ["How work is limited", "WIP limits per column or stage", "The amount forecast at sprint planning"],
                ["Changes mid-cycle", "New items can enter whenever capacity frees up", "Sprint scope is protected; the Sprint Goal should not change"],
                ["Main measures", "Cycle time, throughput, work item age", "Velocity, sprint burndown"],
                ["Roles", "None required", "Product Owner, Scrum Master, Developers"],
            ),
            "Many Scrum teams add WIP limits and flow measures to their sprint board. See "
            "[Kanban vs Scrum](/project-management/kanban/kanban-vs-scrum/) and our guide to "
            "[Scrum boards](/project-management/scrum/scrum-boards/) for more.",
            H3("Kanban board vs to-do list and Gantt chart"),
            "A to-do list records tasks but says nothing about stages, queues or capacity. A Kanban board adds the flow: "
            "where each item is, where work waits and how much is in progress. A [Gantt chart](/project-management/gantt-chart/) "
            "answers a different question: when planned activities should happen and how they depend on each other. "
            "Projects with fixed dates and dependencies often use both: a Gantt chart for the plan and a board for the "
            "day-to-day flow of tasks.",
        ),
        S(
            "Kanban board software and templates",
            "Every major project management tool now offers a board view. The differences are in WIP limits, swimlanes, "
            "flow metrics and how the board connects to the rest of your work. Check current plan details before you buy.",
            T(
                ["Tool", "Kanban board features (from our reviews)"],
                ["[Wrike](/project-management-tools/wrike/)", "Board view with custom statuses on every plan, including Free; swimlanes and columns can be grouped by custom fields; dashboards from the Team plan"],
                ["[monday.com](/project-management-tools/monday/)", "Kanban view of any board alongside table, timeline, Gantt and calendar views; Free plan for up to 2 seats"],
                ["[Asana](/project-management-tools/asana/)", "Board view where tasks move between columns; swimlanes on paid plans since July 2025"],
                ["[ClickUp](/project-management-tools/clickup/)", "Board view on Free Forever, with WIP limits per column that flag full columns"],
                ["[Jira](/project-management-tools/jira/)", "Kanban boards with column WIP limits, swimlanes by assignee, epic or priority, and quick filters; free for up to 10 users"],
                ["[Trello](/project-management-tools/trello/)", "The simplest, purest digital Kanban board; no native WIP limits or swimlanes on the base board"],
                ["[Microsoft Planner](/project-management-tools/microsoft-planner/)", "Board view with buckets as columns, included in Microsoft 365"],
            ),
            "[Wrike](/project-management-tools/wrike/), our top-ranked tool, suits teams that want a board for each "
            "team plus cross-project dashboards and custom-field swimlanes. ClickUp and Jira are strong if you want "
            "built-in WIP limits, and Trello is the quickest way to get a simple board running. Compare them in our "
            "[project management tools comparison](/project-management-tools/compare/).",
        ),
        S(
            "Common Kanban board mistakes",
            L(
                "**Designing the ideal process instead of the real one.** The board then hides the waits and hand-offs "
                "you most need to see.",
                "**No WIP limits.** Without them, a Kanban board is a to-do list with columns.",
                "**Too many columns.** If people cannot read the board in a few seconds, merge stages. Most boards need "
                "between four and eight active columns.",
                "**Cards that are too big.** Items that sit in one column for weeks hide progress; split them.",
                "**No commitment point.** Without one, you cannot measure cycle time or protect the team from overload.",
                "**Ignoring blocked and ageing items.** The oldest card on the board is usually the most important one "
                "to discuss.",
                "**A stale board.** If the board is not updated, nobody trusts it, and people go back to asking for status.",
                "**Using swimlanes per person.** They encourage silos and discourage helping each other; show owners on cards instead.",
            ),
            "Read our [guide to WIP limits](/project-management/kanban/wip-limits/) next to set limits that change how "
            "your board behaves.",
        ),
    ],
    faq=[
        ("What is a Kanban board?",
         "A Kanban board is a visual display of work, with columns for each stage of the workflow, cards for each work "
         "item and limits on work in progress. It shows what is in progress, where work is waiting and where it is stuck."),
        ("What are the parts of a Kanban board?",
         "Cards, columns, WIP limits, a commitment point and a delivery point are the core. Most boards also have "
         "written policies for each column, blocker markers and sometimes swimlanes."),
        ("What are the basic columns on a Kanban board?",
         "The simplest board has To do, Doing and Done. Most teams expand this to match their real process, for example "
         "Options, Ready, Develop, Review, Test and Done."),
        ("How many columns should a Kanban board have?",
         "As few as needed to show the real stages, usually four to eight. Add a column when work genuinely waits or "
         "changes hands there; merge columns that never hold work for long."),
        ("What is the difference between a Kanban board and a Scrum board?",
         "A Scrum board holds only the Sprint Backlog and is reset each sprint. A Kanban board shows continuous flow, "
         "has no sprints and uses WIP limits per column to control how much work is in progress."),
        ("How do you set WIP limits on a Kanban board?",
         "Count today's work in each active stage and set limits a little below it, or around one to one and a half "
         "items per person in that stage. Write them in the column headers and adjust after a few weeks."),
        ("Should I add waiting columns to a Kanban board?",
         "Yes. Queue columns such as Ready for test, or doing and done sub-columns, show where work is waiting, which is "
         "often where most delay hides."),
        ("Physical or digital Kanban board: which is better?",
         "Physical boards are quick to start and very visible for co-located teams. Digital boards suit remote and "
         "hybrid teams and collect flow metrics automatically. Many teams prototype on a whiteboard, then move to a tool."),
        ("Can you make a Kanban board in Excel or Google Sheets?",
         "Yes, for small teams or to try the idea. Our free Kanban board template works in Google Sheets and Excel, "
         "with columns, WIP limits and card details. Dedicated tools are easier once you want metrics or automation."),
        ("Who owns the Kanban board?",
         "The team that does the work owns it and keeps it up to date. Anyone can view it, and changes to its design or "
         "policies should be agreed together."),
        ("How often should you update a Kanban board?",
         "As work happens, so the board always shows the true state. At the least, the team checks and corrects it at "
         "the daily Kanban meeting."),
        ("Do Kanban boards work for remote teams?",
         "Yes. A digital board becomes the shared view of work for a distributed team. Keep policies on the board, "
         "update cards in real time and walk the board together on a video call each day."),
        ("What tools can you use for a Kanban board?",
         "A whiteboard and sticky notes work well. Digital options include Wrike, monday.com, Asana, ClickUp, Jira, "
         "Trello and Microsoft Planner, all of which offer board views, some on free plans."),
    ],
)
