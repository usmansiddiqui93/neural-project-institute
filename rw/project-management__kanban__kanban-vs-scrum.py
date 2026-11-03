from core import S, L, OL, T, TIP, H3

URL = "/project-management/kanban/kanban-vs-scrum/"

RW = dict(
    title="Kanban vs Scrum: Key Differences, Examples and How to Choose",
    desc="Kanban vs Scrum compared: cadence, roles, planning, WIP limits and metrics, the same team run both ways, a scoring checklist and how to switch.",
    intro=(
        "Kanban vs Scrum is a choice between continuous flow and fixed Sprints: Kanban manages a steady stream of "
        "work by visualising it and limiting work in progress, while Scrum delivers in Sprints of one month or less "
        "with three defined accountabilities and five events. Neither is better in general. This guide compares them "
        "point by point, runs the same team both ways with real numbers, and gives you a checklist for choosing and "
        "step-by-step guidance for switching."
    ),
    takeaways=[
        "Kanban is a flow strategy: visualise the workflow, limit work in progress (WIP) and improve flow. Scrum is a framework of fixed-length Sprints with a Product Owner, a Scrum Master and Developers.",
        "Scrum commits to a Sprint Goal and protects it during the Sprint. Kanban makes no batch commitment, so the team can re-prioritise anything not yet started at any time.",
        "Scrum limits work through the Sprint Backlog; Kanban limits it with explicit WIP limits on each column or on the whole board.",
        "Scrum teams often track velocity and burndown; Kanban teams track throughput, cycle time, work item age and cumulative flow.",
        "Choose Kanban for unpredictable, mixed-size or service work; choose Scrum for a dedicated team building a product under uncertainty.",
        "You can combine them: many Scrum teams add WIP limits and flow metrics, and the hybrid known as Scrumban sits between the two.",
    ],
    sections=[
        S("Kanban vs Scrum: what is the difference?",
          "**The main difference between Kanban and Scrum is how they organise time.** Scrum divides work into "
          "fixed-length Sprints, each with a goal, planning, a review and a retrospective, and defines three "
          "accountabilities. Kanban has no Sprints and no required roles: work flows continuously "
          "across a board, and WIP limits control how much is in progress.",
          "Both are Agile in spirit, draw on Lean thinking and rely on transparency and frequent inspection, which "
          "is why teams often mix them. The differences matter most when work is interrupted, when priorities "
          "change daily, or when stakeholders want a fixed rhythm of reviews.",
        ),
        S("Kanban at a glance",
          "Kanban began in Toyota's production system and was adapted for knowledge work in the 2000s. Two sources "
          "define it today:",
          L(
            "**The Kanban Guide (Edition 2025.5)** describes Kanban as a strategy for optimising the flow of value. It has three practices (define and visualise the workflow, actively manage items in the workflow, improve the workflow) and four flow measures: WIP, throughput, work item age and cycle time.",
            "**The Kanban Method from Kanban University** starts with what you do now, respects current roles and adds six general practices, such as making policies explicit and implementing feedback loops, plus a set of optional meetings called cadences.",
          ),
          "Neither requires new job titles or iterations. Our guides to "
          "[what Kanban is](/project-management/kanban/what-is-kanban/) and the "
          "[Kanban principles and practices](/project-management/kanban/kanban-principles/) cover each element.",
        ),
        S("Scrum at a glance",
          "Scrum is defined by the 2020 Scrum Guide, which is still the current version. A Scrum Team of typically "
          "ten or fewer people delivers a usable Increment in each Sprint of one month or less. The framework has:",
          L(
            "**Three accountabilities:** the Product Owner, who maximises value and orders the Product Backlog; the Scrum Master, who establishes Scrum and helps the team improve; and the Developers, who create the Increment.",
            "**Five events:** the Sprint, Sprint Planning, the Daily Scrum, the Sprint Review and the Sprint Retrospective.",
            "**Three artifacts, each with a commitment:** the Product Backlog (Product Goal), the Sprint Backlog (Sprint Goal) and the Increment (Definition of Done).",
          ),
          "Story points, velocity and burndown charts are common Scrum practices, but the Scrum Guide does not "
          "require them. See [what Scrum is](/project-management/scrum/what-is-scrum/) and "
          "[Scrum team roles](/project-management/scrum/scrum-team-roles/) for the detail.",
        ),
        S("Kanban vs Scrum comparison table",
          T(["Aspect", "Kanban", "Scrum"],
            ["Type", "Flow strategy or method applied to your existing process", "Framework with defined events, accountabilities and artifacts"],
            ["Defining guide", "Kanban Guide (2025.5); Kanban Method from Kanban University", "Scrum Guide (2020)"],
            ["Cadence", "Continuous flow; meetings on a cadence that suits the team", "Fixed-length Sprints of one month or less"],
            ["Roles", "None required; some organisations add a Service Request Manager and Service Delivery Manager", "Product Owner, Scrum Master, Developers"],
            ["Planning", "Replenishment when capacity frees up or on a regular schedule", "Sprint Planning at the start of every Sprint"],
            ["Commitment", "Service level expectation for each item; no batch commitment", "Sprint Goal for the Sprint"],
            ["Change", "Anything not yet started can be re-prioritised at any time", "Sprint Goal is protected; scope can be renegotiated with the Product Owner"],
            ["Limiting WIP", "Explicit WIP limits per column, lane or board", "Implicit, through the size of the Sprint Backlog"],
            ["Estimation", "Optional; many teams right-size items instead", "Optional, though many teams use story points"],
            ["Board", "Persistent; items flow across it indefinitely", "Usually reset or re-scoped each Sprint"],
            ["Typical metrics", "Throughput, cycle time, work item age, WIP, cumulative flow", "Velocity, Sprint burndown or burnup, Sprint Goal success"],
            ["Forecasting", "From throughput and cycle time history, often with Monte Carlo", "From average velocity across recent Sprints"],
            ["Delivery", "Whenever an item is ready", "At least one usable Increment per Sprint; release can happen any time"],
            ["Team", "Can be shared specialists or a whole service", "Dedicated, cross-functional, self-managing"],
            ["Best for", "Support, operations, maintenance, marketing and other variable work", "New product development under uncertainty"],
          ),
        ),
        S("What Kanban and Scrum have in common",
          "The two approaches share more than many comparisons suggest. Both:",
          L(
            "**Make work visible**, usually on a board, so problems surface early.",
            "**Use pull**: people take new work when they have capacity.",
            "**Limit work in progress**, explicitly in Kanban and through the Sprint Backlog in Scrum.",
            "**Rely on empiricism**: decisions follow what the team observes, not a detailed long-range plan.",
            "**Build in improvement** through retrospectives, reviews and feedback loops.",
            "**Favour small batches and frequent delivery** to reduce risk and speed up feedback.",
          ),
        ),
        S("The key differences explained",
          H3("Cadence: Sprints versus continuous flow"),
          "Scrum's Sprint is a container for all other events, commonly one or two weeks long, so the team plans, "
          "reviews and improves on a predictable rhythm. Kanban has no container: items enter and leave one at a "
          "time, and the team sets separate rhythms for replenishing, reviewing and improving.",
          H3("Roles and accountabilities"),
          "Scrum establishes three accountabilities from day one, which usually means appointing a Product Owner "
          "and a Scrum Master. Kanban keeps existing roles. Some mature Kanban systems name a Service Request "
          "Manager and a Service Delivery Manager, but neither is required.",
          H3("Planning and commitment"),
          "In [Sprint Planning](/project-management/scrum/sprint-planning/), the Scrum Team agrees a Sprint Goal and "
          "selects items from the [Product Backlog](/project-management/scrum/product-backlog/) that it forecasts it "
          "can complete. Kanban replaces this with replenishment: when the Ready column runs low, the team or its "
          "requesters choose the next items. The commitment is per item, often expressed as a service level "
          "expectation such as 85% of items finished within eight working days.",
          H3("How each handles change"),
          "During a Scrum Sprint, no changes are made that would endanger the Sprint Goal, although scope can be "
          "clarified and renegotiated with the Product Owner as the team learns. New ideas go into the Product "
          "Backlog for a future Sprint. In Kanban, anything not yet started can be re-ordered at any time, and an "
          "urgent item can enter an expedite lane straight away.",
          H3("How work in progress is limited"),
          "Scrum limits work by limiting what goes into the Sprint. Within the Sprint, nothing stops five Developers "
          "starting eight items. Kanban sets explicit [WIP limits](/project-management/kanban/wip-limits/), for "
          "example a maximum of three items in Testing. When a column is full, people help finish existing work "
          "instead of starting more.",
          H3("Meetings and cadences"),
          "Kanban is sometimes described as having no meetings. That is not accurate: the Kanban Method describes "
          "seven cadences, but none is mandatory and their frequency is up to you.",
          T(["Purpose", "Scrum event", "Kanban cadence (Kanban Method)"],
            ["Daily coordination", "Daily Scrum, 15 minutes", "Kanban meeting, daily, about 15 minutes"],
            ["Choosing work", "Sprint Planning, up to 8 hours for a one-month Sprint", "Replenishment meeting, often weekly or when Ready runs low"],
            ["Reviewing results", "Sprint Review, up to 4 hours for a one-month Sprint", "Service delivery review and delivery planning meeting"],
            ["Improving the process", "Sprint Retrospective, up to 3 hours for a one-month Sprint", "Operations review, risk review and team retrospectives"],
            ["Direction", "Product Goal, managed by the Product Owner", "Strategy review, often quarterly"],
          ),
          "Our guides to [Kanban ceremonies](/project-management/kanban/kanban-ceremonies/) and "
          "[Scrum ceremonies](/project-management/scrum/scrum-ceremonies/) give agendas and timings.",
        ),
        S("Kanban board vs Scrum board",
          "Both boards show cards in columns, so they can look identical. The rules behind them differ:",
          T(["Feature", "Kanban board", "Scrum board"],
            ["Scope", "All work flowing through the team's process", "The Sprint Backlog for the current Sprint"],
            ["Lifespan", "Persistent", "Cleared or re-scoped at the end of each Sprint"],
            ["Columns", "Every real step, such as Ready, Build, Review, Test, Done", "Often simpler: To do, In progress, Done"],
            ["WIP limits", "Shown on each column or lane", "Uncommon, though allowed"],
            ["Swimlanes", "Often used for classes of service, such as Expedite", "Often used per user story"],
            ["Ownership", "The team, with explicit policies", "The Developers"],
          ),
          "Our guides to "
          "[Kanban boards](/project-management/kanban/kanban-boards/) and "
          "[Scrum boards](/project-management/scrum/scrum-boards/) show more layouts, and the free "
          "[Kanban board template](/templates/kanban-board-template/) gives you WIP limits ready to edit.",
        ),
        S("Worked example: one team, run both ways",
          "To see the differences in practice, follow one team through both approaches. **This example is "
          "illustrative; the team and figures are invented to show the mechanics.**",
          "A seven-person team builds and supports a customer billing portal. It has a Product Owner, a Scrum "
          "Master and five Developers. Most work is planned feature development, but customers also raise urgent "
          "production issues, on average three or four every two weeks.",
          H3("The Scrum version"),
          "The team runs two-week Sprints (ten working days). Its velocity over the last four Sprints was 27, 31, 24 "
          "and 30 points, an average of 28. Here is Sprint 14:",
          T(["Day", "What happens"],
            ["1", "Sprint Planning: Sprint Goal is \"Customers can update their billing details online\". The team selects 10 items totalling 29 points."],
            ["3", "Urgent production issue 1 arrives. Two Developers spend most of a day fixing it."],
            ["6", "Urgent issue 2 arrives and takes another developer-day and a half."],
            ["7", "The Developers and Product Owner renegotiate scope: two items (6 points) not needed for the Sprint Goal go back to the Product Backlog."],
            ["8", "Urgent issue 3 arrives and is fixed the same day."],
            ["10", "Sprint Review: 8 items (23 points) are Done and the Sprint Goal is met. At the Retrospective, the team agrees to reserve capacity for unplanned work."],
          ),
          "Scrum worked as designed: the goal was protected and scope flexed. The cost is noise: velocity swings "
          "with interruptions, forecasts get less reliable and the team renegotiates every Sprint.",
          H3("The Kanban version"),
          "The same team drops Sprints and sets up a board with WIP limits: Ready (6), Build (4), Review (2), Test "
          "(3) and Done, plus an Expedite lane limited to one item. It holds a daily Kanban meeting, a weekly "
          "replenishment meeting with the product lead, and a service delivery review and retrospective every two "
          "weeks.",
          "Urgent issues go straight into the Expedite lane and are pulled by the next free Developer. Planned work "
          "continues; nobody has to renegotiate a batch. Over eight weeks, the team finishes 4, 6, 5, 3, 5, 7, 4 and "
          "6 planned items per week (an average throughput of 5), plus the urgent fixes. Planned items take 5 "
          "working days on average from start to finish, and 85% finish within 8 working days, which becomes the "
          "team's service level expectation.",
          H3("What the comparison shows"),
          L(
            "**Delivery speed is similar**: about ten planned items every two weeks either way. Neither approach makes a team faster by itself.",
            "**Kanban absorbs interruptions with less overhead**, because there is no Sprint commitment to protect.",
            "**Scrum gives a clearer goal and a fixed review rhythm**, which stakeholders of a new feature often value.",
            "**The work decides.** If interruptions grew to half the team's capacity, Kanban would fit better; if they disappeared, Scrum would lose little.",
          ),
        ),
        S("Kanban vs Scrum metrics compared",
          "Scrum and Kanban answer the same questions with different measures:",
          T(["Question", "Typical Scrum measure", "Typical Kanban measure"],
            ["How much do we finish?", "Velocity (points per Sprint)", "Throughput (items per week)"],
            ["How long does an item take?", "Rarely measured directly", "Cycle time and its percentiles"],
            ["Is anything stuck?", "Sprint burndown flattening", "Work item age and a WIP aging chart"],
            ["Is work piling up?", "Unfinished items at Sprint end", "Widening bands on a cumulative flow diagram"],
            ["What can we promise?", "Sprint Goal", "Service level expectation"],
          ),
          "Read more in our guides to [Scrum velocity](/project-management/scrum/scrum-velocity/), "
          "[throughput](/project-management/kanban/throughput/), [cycle time](/project-management/kanban/cycle-time/) "
          "and the [cumulative flow diagram](/project-management/kanban/cumulative-flow-diagram/).",
          H3("Forecasting the same backlog both ways"),
          "Using the illustrative team above, suppose 30 planned items remain for the billing release, estimated at "
          "84 story points.",
          OL(
            "**Scrum forecast.** Divide the points by average velocity: 84 / 28 = 3 Sprints, or about six weeks. Using the slowest and fastest recent Sprints (24 and 31 points) gives a range of 2.7 to 3.5 Sprints, so plan for three to four Sprints.",
            "**Kanban forecast.** Divide the items by average weekly throughput: 30 / 5 = 6 weeks. If every week were as slow as the slowest week (3 items), it would take 10 weeks; as fast as the fastest (7 items), just over 4 weeks.",
            "**Narrow the range.** Instead of best and worst cases, Kanban teams usually run a Monte Carlo simulation that samples past weekly throughput thousands of times and reports a date for each confidence level, such as 85%. Our [Kanban planning guide](/project-management/kanban/kanban-planning/) walks through it.",
            "**Communicate a range, not a date**, and update it every week or Sprint as new data arrives.",
          ),
          H3("Little's Law: the link between WIP and speed"),
          "Little's Law says that, in a stable system, average cycle time equals average WIP divided by average "
          "throughput. The Kanban team above finishes about one planned item per working day with about five in "
          "progress, so items take about five working days. If WIP drifted up to ten without any faster finishing, "
          "cycle time would double to about ten days. That is why Kanban limits WIP, and why Scrum teams that add "
          "WIP limits often see items finish sooner. Our [Kanban metrics guide](/project-management/kanban/kanban-metrics/) "
          "covers the other measures.",
        ),
        S("When to choose Kanban",
          "Kanban tends to fit when:",
          L(
            "Work arrives unpredictably and often needs starting within days, as in IT support, operations or maintenance.",
            "Priorities change daily and a two-week commitment would be broken repeatedly.",
            "Items vary greatly in size, from an hour to several weeks.",
            "The team is made up of shared specialists who also serve other teams.",
            "You want to improve an existing process gradually without new roles or a reorganisation.",
            "Customers care about how quickly a request will be finished, which a service level expectation answers directly.",
          ),
        ),
        S("When to choose Scrum",
          "Scrum tends to fit when:",
          L(
            "A dedicated, cross-functional team is building a new product or major feature.",
            "There is real uncertainty about what to build, so regular inspection with stakeholders is valuable.",
            "Most work can be planned a week or two ahead without constant interruption.",
            "Someone can act as Product Owner and make ordering decisions.",
            "The team and stakeholders benefit from a fixed rhythm of planning, review and reflection.",
            "The organisation wants a common, well-documented framework with widely recognised training.",
          ),
        ),
        S("How to choose: an eight-question checklist",
          "Answer each question honestly, based on how work really arrives, and note which approach each answer points to.",
          T(["Question", "Points to Kanban if", "Points to Scrum if"],
            ["1. Does more than about a quarter of your work arrive unplanned and need starting within days?", "Yes", "No"],
            ["2. Can one person act as Product Owner and order all the work?", "No", "Yes"],
            ["3. Is the team dedicated and cross-functional?", "No, shared specialists", "Yes"],
            ["4. Do stakeholders want a fixed rhythm of reviews of working results?", "No", "Yes"],
            ["5. Do items vary widely in size, from hours to weeks?", "Yes", "No"],
            ["6. Do you want to change the current process gradually, without new roles?", "Yes", "No"],
            ["7. Is the work new product development with high uncertainty?", "No", "Yes"],
            ["8. Do customers expect a service level, such as fixes within five days?", "Yes", "No"],
          ),
          "**Reading your score:** six or more answers on one side give a clear choice. A five-three split is a "
          "lean, so start with that approach and borrow the practices you need from the other. A four-four split "
          "usually means a hybrid will serve you well.",
          "**Worked scores (illustrative).** An IT service desk answers every question on the Kanban side: eight "
          "to Kanban, a clear choice. A mobile app team answers on the Scrum side for everything except question 5, "
          "because its items vary a lot: seven to Scrum, so it starts with Scrum and adds rules for splitting large "
          "items.",
          TIP("Re-run the checklist every six months: after a first release, product work often shifts towards support."),
        ),
        S("Kanban vs Scrum by type of team",
          T(["Team", "Usual starting point", "Why"],
            ["Software product team", "Scrum", "Uncertain requirements and stakeholders who want to inspect working software each Sprint"],
            ["Platform, DevOps or SRE team", "Kanban", "High share of unplanned requests and incidents"],
            ["IT service desk", "Kanban", "Continuous flow of tickets with service levels"],
            ["Marketing team", "Either", "Kanban for always-on content; Scrum for campaign launches with a fixed review rhythm"],
            ["Creative or design agency", "Kanban", "Mixed client requests of very different sizes"],
            ["Operations, finance or HR", "Kanban", "Recurring processes that improve gradually"],
            ["Individual or very small team", "Kanban", "Lightweight, with no roles to fill"],
          ),
        ),
        S("How to switch from Scrum to Kanban",
          "Teams usually switch when unplanned work keeps breaking Sprint commitments. Change in steps:",
          OL(
            "**Agree why you are switching.** Name the problem at a Retrospective, such as \"we miss most Sprint Goals because of urgent work\", so you can check later whether Kanban fixed it.",
            "**Map your real workflow.** Replace To do, In progress and Done with the steps work actually goes through, such as Ready, Build, Review, Test and Done.",
            "**Set starting WIP limits**, roughly the number of people working in each column, and add an Expedite lane limited to one item.",
            "**Replace Sprint Planning with replenishment.** Decide when Ready is refilled (weekly, or when it falls below a set number) and who chooses.",
            "**Keep a review and a retrospective** with stakeholders and the team every two to four weeks.",
            "**Start measuring flow.** Record start and finish dates on each card to track throughput, cycle time and work item age.",
            "**Agree what happens to Scrum roles.** The Product Owner often keeps ordering work and the Scrum Master often coaches flow; nobody needs a new title.",
            "**Review after six to eight weeks**, comparing cycle time, throughput and interruptions with your Sprint data.",
          ),
          "If you would rather keep Sprints while you test Kanban practices, a staged hybrid such as Scrumban is a "
          "gentler route, covered under using Kanban and Scrum together below.",
        ),
        S("How to move from Kanban to Scrum",
          "Teams move the other way when they start a new product, need clearer goals, or want a regular demo for "
          "stakeholders.",
          OL(
            "**Confirm the team can be dedicated.** Scrum works best when most members spend most of their time on one product.",
            "**Name the accountabilities.** Choose a Product Owner who can order the backlog and a Scrum Master who will help the team adopt Scrum.",
            "**Turn the board backlog into a Product Backlog** with a Product Goal, and refine the top items until they are small enough for a Sprint.",
            "**Choose a Sprint length**, usually one or two weeks for a first attempt, and agree a Definition of Done.",
            "**Run the first Sprint Planning**, using your Kanban throughput to forecast how many items to select.",
            "**Keep useful Kanban habits**, such as WIP limits and an Expedite lane, as long as they support the Sprint Goal.",
            "**Inspect after three Sprints** at the Retrospective and adjust the Sprint length or practices.",
          ),
          "Our free [sprint planning template](/templates/sprint-planning-template/) and "
          "[product backlog template](/templates/product-backlog-template/) help you set up the first Sprint.",
        ),
        S("Using Kanban and Scrum together",
          "You do not have to choose one exclusively. There are two common ways to combine them:",
          L(
            "**Scrum with Kanban practices.** Scrum.org's Kanban Guide for Scrum Teams (2021 edition) adds flow practices such as WIP limits, work item age and service level expectations to Scrum without changing any Scrum rules. The team keeps Sprints, accountabilities and events.",
            "**Scrumban.** A hybrid that keeps some of Scrum's structure, such as regular planning and retrospectives, but replaces the fixed Sprint commitment with Kanban's continuous pull and WIP limits. It was originally described as a way for Scrum teams to move towards Kanban.",
          ),
          "The first is still Scrum; the second is a different way of working. Read our guide to "
          "[Kanban vs Scrumban](/project-management/kanban/kanban-vs-scrumban/) for how the hybrid works and how to set it up.",
        ),
        S("Tools for Kanban and Scrum teams",
          "Most work management tools support both approaches. The question is how far each goes:",
          L(
            "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool (9.4/10), gives every plan a board view built on custom statuses, so you can model a Kanban workflow quickly, alongside Gantt charts, dashboards and request forms. It suits organisations running Kanban and Scrum-style work across several departments.",
            "**[Jira](/project-management-tools/jira/)** has the deepest dedicated Scrum and Kanban support for software teams, including backlogs, Sprints, WIP limits, cumulative flow diagrams and control charts. Its free plan covers up to 10 users.",
            "**[ClickUp](/project-management-tools/clickup/)** combines Sprints, sprint points and burndown with per-column WIP limits on its board view, which suits teams mixing both approaches on a budget.",
          ),
          "Whatever the tool, agree the workflow and policies first, then configure the software to match.",
        ),
        S("Common mistakes when choosing between Kanban and Scrum",
          L(
            "**Choosing Kanban to avoid discipline.** Kanban without WIP limits, explicit policies and regular reviews is just a to-do list on a wall.",
            "**Choosing Scrum for a support queue.** If most work is unplanned, Sprint Goals will be broken repeatedly and the team will lose faith in planning.",
            "**Dropping retrospectives when moving to Kanban.** Improvement is a core Kanban practice; keep a regular cadence for it.",
            "**Comparing velocity with throughput.** Points and item counts measure different things, so you cannot compare a Scrum team's velocity with a Kanban team's throughput.",
            "**Switching without a baseline.** Record cycle time, throughput or Sprint Goal success before you change, or you will not know whether the change helped.",
            "**Treating the choice as permanent.** Teams and work change. Revisit the decision when the mix of planned and unplanned work shifts.",
          ),
        ),
    ],
    faq=[
        ("What is the main difference between Kanban and Scrum?",
         "Scrum organises work into fixed-length Sprints of one month or less, with a Sprint Goal, three accountabilities and five events. Kanban manages a continuous flow of work with WIP limits, no required roles and no iterations."),
        ("Which is better, Kanban or Scrum?",
         "Neither is better in general. Kanban suits continuous, unpredictable or mixed-size work such as support and operations. Scrum suits a dedicated team building a product where regular inspection with stakeholders adds value. Use the checklist above to decide for your team."),
        ("Is Kanban agile?",
         "Yes. Kanban is widely used as an Agile approach because it delivers in small batches, responds to change and improves continuously. It also draws heavily on Lean thinking."),
        ("Does Kanban have sprints?",
         "No. Kanban has no Sprints or other fixed iterations. Work is pulled continuously, and planning, review and improvement meetings run on whatever cadence the team chooses."),
        ("Does Kanban need a Scrum Master or Product Owner?",
         "No. Kanban requires no new roles. Some organisations add a Service Request Manager to order incoming work and a Service Delivery Manager to look after flow, and teams moving from Scrum often keep their Product Owner in a similar ordering role."),
        ("Is Kanban easier to learn than Scrum?",
         "Kanban is usually easier to start because it begins with your current process and adds no roles, though doing it well still takes discipline. Scrum asks for more change on day one but gives a clearer structure."),
        ("Can a Scrum team use a Kanban board?",
         "Yes. Many Scrum teams show their Sprint Backlog on a board with Kanban-style columns and WIP limits. As long as the team keeps its Sprints, accountabilities and events, it is still doing Scrum."),
        ("What does Kanban use instead of velocity?",
         "Kanban teams measure throughput (items finished per week), cycle time, work item age and WIP, and use a cumulative flow diagram to spot bottlenecks. Throughput history also supports forecasting."),
        ("Do Kanban teams estimate work?",
         "Estimation is optional. Many Kanban teams skip story points, split work into items of roughly similar size and forecast from throughput and cycle time."),
        ("Can you change priorities mid-Sprint in Scrum?",
         "The Product Backlog can be re-ordered at any time, but changes to the current Sprint should not endanger the Sprint Goal. Scope can be clarified and renegotiated with the Product Owner. If the Sprint Goal becomes obsolete, only the Product Owner can cancel the Sprint."),
        ("Is Jira Kanban or Scrum?",
         "Jira supports both. You can create a Scrum board with a backlog and Sprints, or a Kanban board with continuous flow and WIP limits, and its reports cover velocity and burndown as well as cumulative flow and cycle time."),
        ("Which is better for small teams?",
         "Both can work. Individuals and very small teams often prefer Kanban because it needs no roles or fixed events. A small dedicated product team can run Scrum well if one person can act as Product Owner."),
        ("How long does it take to switch from Scrum to Kanban?",
         "A team can set up a Kanban board and WIP limits in a day, but give the new system six to eight weeks, long enough to collect flow data and tune the WIP limits, before judging it."),
    ],
)
