from core import S, L, OL, T, TIP, H3

URL = "/project-management/capacity-planning/"

RW = dict(
    title="Capacity Planning in Project Management: Steps and Example",
    desc="Capacity planning in project management explained: formulas, step-by-step process, worked examples, lead/lag/match strategies, tools and common mistakes.",
    intro=(
        "Capacity planning in project management is the process of comparing the work your projects and day-to-day "
        "operations will demand with the productive time and skills your people can actually supply, so you can spot "
        "shortfalls before they delay delivery. This guide gives you the formulas, a step-by-step process, three worked "
        "examples and the decisions to make when demand and capacity do not match."
    ),
    takeaways=[
        "Capacity planning compares demand (hours of work needed) with productive capacity (hours people can really give) for a team, skill or portfolio over a set period.",
        "Productive capacity = people x hours x weeks, minus leave and holidays, multiplied by a productive-time factor for meetings, admin and support.",
        "Plan by skill or role, not by headcount: a surplus of testers does not cancel out a shortage of developers.",
        "Include business-as-usual work and weight pipeline projects by their likelihood, or the plan will look better than reality.",
        "Do not plan to 100%. Keep a buffer, often 10-15% of productive capacity, for urgent work and estimating error.",
        "Review the plan on a fixed cadence: monthly for portfolios, every sprint or fortnight for teams.",
    ],
    sections=[
        S(
            "What is capacity planning in project management?",
            "**Capacity planning** is the process of estimating how much productive work a team, department or "
            "organisation can deliver in a period, comparing it with the work requested, and acting on the difference. "
            "It answers one question before work starts: do we have enough of the right people, at the right time, to "
            "deliver what we have promised?",
            "It works on two sides of a balance:",
            L(
                "**Supply (capacity):** the hours of productive time available, by person, role or skill, after leave, "
                "holidays and non-project work are taken out.",
                "**Demand:** the hours of work required by approved projects, likely future projects and the "
                "business-as-usual work that never goes away.",
            ),
            "It looks weeks, months or years ahead and works with teams, roles and portfolios rather than individual "
            "tasks. Typical questions: can we start this project next month, which skill runs out first, and do we need "
            "to hire, contract or say no? Once capacity planning confirms the work fits, [resource allocation](/project-management/resource-allocation/) assigns named people to specific "
            "tasks and [project scheduling](/project-management/project-scheduling/) sets the dates.",
        ),
        S(
            "Capacity, demand, allocation and utilisation",
            "These terms are often used loosely. Agreeing what each one means is the first step to a capacity plan "
            "people trust.",
            T(
                ["Term", "Meaning", "Example"],
                ["Gross capacity", "Total contracted hours for the period", "5 people x 40 hours x 4 weeks = 800 hours"],
                ["Availability", "Gross capacity minus leave, public holidays and training", "800 - 40 hours of leave = 760 hours"],
                ["Productive capacity", "The part of available time that can go on planned work, after meetings, admin and support", "760 x 80% = 608 hours"],
                ["Demand", "Hours of work requested by projects and business-as-usual activity", "680 hours across two projects and routine requests"],
                ["Allocation", "Which work is assigned to which person or team", "Ana: 24 hours a week on Project A"],
                ["Utilisation", "Allocated or demanded hours divided by capacity, as a percentage", "680 / 608 = 112%"],
                ["Capacity gap", "Demand minus productive capacity; positive means a shortfall", "680 - 608 = 72 hours short"],
            ),
            H3("Capacity planning vs resource planning vs resource allocation"),
            "The three activities overlap and the names vary between organisations, but the distinction below is the "
            "most useful in practice.",
            T(
                ["", "Capacity planning", "Resource planning", "Resource allocation"],
                ["Main question", "Do we have enough of each skill for all the work we want to do?", "What resources does this project need, and when?", "Who exactly does which task?"],
                ["Scope", "Team, department or portfolio", "One project or programme", "One project or team"],
                ["Horizon", "Months to years", "Life of the project", "Days to weeks"],
                ["Unit", "Hours or FTE by role or skill", "Roles, people, equipment, materials", "Named people and hours per task"],
                ["Typical owner", "PMO, resource manager, functional heads", "Project manager", "Project manager or team lead"],
                ["Output", "Gap analysis and decisions: start, delay, hire, cut", "Resource plan and requirements", "Assignments in the schedule"],
            ),
            "When individual people are overloaded inside an approved plan, the fix is "
            "[resource levelling](/project-management/resource-leveling/), which moves tasks within float or extends the "
            "schedule. Capacity planning works one level up and decides how much work should enter the system in the "
            "first place. For a wider view of people, equipment and materials, see our guide to "
            "[project resources](/project-management/project-resources/).",
            H3("Capacity planning and Agile teams"),
            "Agile teams turn the problem round: the team is fixed, so they ask how much work fits into its capacity "
            "each sprint, using availability and past velocity. Portfolio-level planning still decides which teams work "
            "on which initiatives. See our guide to [agile capacity planning](/project-management/agile/agile-capacity-planning/) for the sprint-level formula.",
        ),
        S(
            "Why capacity planning matters",
            "Most organisations approve projects one at a time, each with a plausible plan. Trouble starts when those "
            "plans all draw on the same specialists in the same months. Capacity planning helps you:",
            L(
                "**Set realistic dates**, checked against the hours actually available.",
                "**Protect people from overload**, which shows up as long hours, then mistakes and resignations.",
                "**Find skill shortages early**, while there is time to recruit, train or contract.",
                "**Make portfolio decisions on evidence**: what can start now and what must wait.",
                "**Reduce multitasking and budget accurately**, since capacity converts directly into cost.",
            ),
            "Skipping it rarely causes a single dramatic failure. Instead, projects all run a little late and shared "
            "experts become bottlenecks. Our guide to [managing multiple projects](/project-management/managing-multiple-projects/) covers the day-to-day side.",
        ),
        S(
            "Strategic, tactical and operational capacity planning",
            "Capacity planning happens at three levels. Each has a different horizon, level of detail and owner, and "
            "they should feed each other.",
            T(
                ["Level", "Horizon", "Unit of planning", "Typical decisions", "Usual owner"],
                ["Strategic", "1-3 years", "FTE by role or capability", "Hiring plans, new teams, outsourcing, building a capability", "Leadership, HR, portfolio board"],
                ["Tactical", "1-12 months, usually a quarter", "Hours or FTE by skill, per month", "Which projects start, sequencing, contractors, training", "PMO, resource managers"],
                ["Operational", "1-6 weeks", "Hours by person, per week or sprint", "Who works on what, rebalancing, short-term overtime", "Project managers, team leads"],
            ),
            "This guide concentrates on the tactical level, but the same method scales up and down.",
        ),
        S(
            "Capacity planning formulas",
            "You need only a handful of formulas. Use the same period (week, month or quarter) for every figure in the "
            "calculation.",
            T(
                ["Measure", "Formula"],
                ["Gross capacity", "Number of people x contracted hours per week x weeks in the period"],
                ["Available capacity", "Gross capacity - (leave + public holidays + planned training)"],
                ["Productive capacity", "Available capacity x productive-time factor"],
                ["Total demand", "Committed project hours + business-as-usual hours + (pipeline hours x probability)"],
                ["Capacity gap", "Total demand - productive capacity"],
                ["Utilisation", "Total demand / productive capacity x 100"],
                ["Gap in FTE", "Capacity gap / productive hours one FTE supplies in the period"],
            ),
            TIP("**Productive capacity = (people x hours x weeks - leave and holidays) x productive-time factor.** "
                "Compare demand with this figure, never with contracted hours."),
            "Calculate separately for each role that matters; decisions are made skill by skill. Converting gaps into "
            "[full-time equivalents (FTE)](/project-management/full-time-equivalent-fte/) makes them easier to discuss: "
            "\"1.3 developers short\" is clearer than \"378 hours short\".",
        ),
        S(
            "How to do capacity planning step by step",
            "This process works for a single team or a whole portfolio. The first cycle takes longest; after that it is "
            "a regular update.",
            OL(
                "**Set the scope and horizon**, for example one department for the next quarter in monthly buckets.",
                "**Define the roles or skills to plan**, such as developers, testers and analysts. A "
                "[skills matrix](/templates/skills-matrix-template/) shows who can cover more than one role.",
                "**Calculate gross capacity** by role from actual contracts, so part-timers count at their real hours.",
                "**Subtract known absence**: leave, public holidays, training and long-term absence.",
                "**Apply a productive-time factor**, derived from timesheets where you have them.",
                "**Collect demand from every source**, by role and month: committed projects, business-as-usual and "
                "weighted pipeline projects.",
                "**Compare demand with capacity** and flag every role and period above your target utilisation.",
                "**Decide how to close gaps** and record the decision and who made it.",
                "**Publish a one-page view** for project managers, functional heads and the portfolio board, with assumptions.",
                "**Review on a fixed cadence** and compare planned with actual utilisation to improve your factors.",
            ),
            H3("Estimating demand"),
            "Demand is where most capacity plans go wrong, because it is easy to count projects and forget everything "
            "else. Build it from four sources:",
            T(
                ["Demand source", "How to estimate it", "Common trap"],
                ["Committed projects", "Remaining effort by role and month from each project's estimate or schedule", "Using the original estimate instead of the remaining work"],
                ["Pipeline projects", "Rough effort by role x probability of approval", "Leaving them out until they are approved, then discovering there is no room"],
                ["Business-as-usual", "Average hours from the last 3-6 months of timesheets or ticket data", "Assuming it is zero because it is not in a project plan"],
                ["Support and incidents", "Historical average plus a margin for peaks", "Ignoring on-call rotas and release support"],
            ),
            "Remaining effort should come from the people closest to the work; see "
            "[effort estimation](/project-management/effort-estimation/) for three-point and bottom-up techniques.",
            H3("Choosing a productive-time factor"),
            "Meetings, email, admin, line management, support and context switching all take a share of contracted "
            "time. The best source for your factor is your own timesheets: hours booked to planned work divided by hours "
            "available over a few months. Without data, many teams start around 70-80% for specialists and lower for "
            "leads and managers, then adjust. Treat these as starting assumptions, not benchmarks.",
        ),
        S(
            "Worked example 1: one month for a team of five",
            "This is an illustrative example. A design team has five people working 40-hour weeks. The month has four "
            "working weeks. Planned leave totals 40 hours, and timesheets show about 20% of time goes on meetings, admin "
            "and support, so the productive-time factor is 80%.",
            T(
                ["Step", "Calculation", "Hours"],
                ["Gross capacity", "5 people x 40 h x 4 weeks", "800"],
                ["Less leave", "800 - 40", "760"],
                ["Productive capacity", "760 x 80%", "608"],
            ),
            T(
                ["Demand source", "Hours"],
                ["Project A (website redesign)", "320"],
                ["Project B (brand refresh)", "240"],
                ["Business-as-usual requests", "120"],
                ["**Total demand**", "**680**"],
            ),
            "Demand of 680 hours exceeds productive capacity of 608 hours by **72 hours**, so utilisation is "
            "680 / 608 = 112%, roughly 12% over. Expressed in FTE, one designer supplies 160 x 80% = 128 productive hours "
            "a month, so the gap is 72 / 128 = **0.56 FTE**.",
            "The team lead takes three options to the head of marketing:",
            L(
                "Move 72 hours of Project B into next month, delaying the brand refresh by about two weeks.",
                "Bring in a freelance designer for about two weeks to cover the shortfall.",
                "Pause lower-priority business-as-usual requests for the month, with an agreed list of what waits.",
            ),
            "Without the numbers the team would simply have worked late and missed some dates. With them, the business "
            "chooses the trade-off.",
        ),
        S(
            "Worked example 2: a quarterly skill-based capacity plan",
            "This example is also illustrative. A PMO is planning the next quarter for an IT delivery team of 11 "
            "people: 6 developers, 3 testers and 2 business analysts. The quarter has 12 working weeks after public "
            "holidays, the standard week is 37.5 hours, and each person averages 1.5 weeks of planned leave, leaving "
            "10.5 available weeks each. Timesheets give different productive-time factors by role.",
            H3("Step 1: productive capacity by role"),
            T(
                ["Role", "People", "Available hours (people x 37.5 x 10.5)", "Productive factor", "Productive capacity"],
                ["Developers", "6", "2,362.5", "75%", "1,772"],
                ["Testers", "3", "1,181.3", "80%", "945"],
                ["Business analysts", "2", "787.5", "70%", "551"],
                ["**Total**", "**11**", "**4,331.3**", "", "**3,268**"],
            ),
            H3("Step 2: demand by role"),
            "Two projects are approved. A third, Project Gamma, is in the pipeline and the portfolio board puts its "
            "chance of approval at 60%, so its hours are weighted by 0.6.",
            T(
                ["Demand source", "Developers", "Testers", "Business analysts"],
                ["Project Alpha (CRM upgrade, committed)", "900", "300", "150"],
                ["Project Beta (mobile app, committed)", "700", "250", "200"],
                ["Business-as-usual and support", "250", "100", "50"],
                ["Project Gamma (500 / 200 / 150 hours x 60%)", "300", "120", "90"],
                ["**Total demand**", "**2,150**", "**770**", "**490**"],
            ),
            H3("Step 3: compare and calculate the gaps"),
            T(
                ["Role", "Productive capacity", "Demand", "Gap (hours)", "Utilisation"],
                ["Developers", "1,772", "2,150", "378 short", "121%"],
                ["Testers", "945", "770", "175 spare", "81%"],
                ["Business analysts", "551", "490", "61 spare", "89%"],
                ["**Whole team**", "**3,268**", "**3,410**", "**142 short**", "**104%**"],
            ),
            "Looked at as a whole, the team is only 4% over capacity, which might pass as \"tight but manageable\". By "
            "role, developers are 21% over while testers have spare time. One developer supplies 37.5 x 10.5 x 75% = "
            "about 295 productive hours a quarter, so the developer gap is 378 / 295 = **1.3 FTE**. Even without Project "
            "Gamma, developers would be 78 hours short (about 0.26 FTE), so the shortage is real and not just a "
            "pipeline risk.",
            "This is why planning by headcount fails: \"11 people, 104% loaded\" invites \"work a bit harder\", while "
            "\"1.3 developers short from week one\" invites a decision.",
        ),
        S(
            "What to do when demand exceeds capacity",
            "You have a limited set of levers, each with a cost. The right mix depends on priorities, budget and how "
            "long the gap lasts.",
            T(
                ["Option", "How it works", "Best when", "Trade-off"],
                ["Reprioritise", "Stop, pause or defer lower-value work", "The portfolio has more ideas than capacity, which is common", "Someone's project waits; needs a clear decision-maker"],
                ["Reschedule", "Move the start or phases to a period with spare capacity", "Dates are flexible or the peak is short", "Benefits arrive later"],
                ["Reduce scope", "Cut or postpone lower-priority features", "Some requirements are nice to have", "Less delivered in this release"],
                ["Rebalance skills", "Move work to roles with spare time or cross-trained staff", "Skills overlap, for example testers automating tests", "Lower productivity at first; needs training"],
                ["Contractors or partners", "Buy capacity for a fixed period", "The gap is temporary and the skill is available in the market", "Day rates, onboarding time, knowledge leaving at the end"],
                ["Hire", "Add permanent capacity", "The gap is lasting and strategic", "Recruitment lead time; ongoing cost"],
                ["Overtime", "Ask people to work extra hours", "Short, genuine peaks only", "Fatigue, errors and attrition if it becomes normal"],
            ),
            "Inside individual projects, [resource levelling](/project-management/resource-leveling/) and techniques "
            "from [schedule compression](/project-management/schedule-compression/) help once the portfolio decision "
            "has been made. Watch for [scope creep](/project-management/scope-creep/): unmanaged additions quietly "
            "increase demand after the capacity plan has been agreed.",
            H3("Worked example 3: closing the developer gap"),
            "Continuing the illustrative example, the PMO models the options for the 378-hour developer shortfall.",
            T(
                ["Option", "Effect on developers", "Cost or consequence"],
                ["A. Defer Project Gamma's start to next quarter", "Demand falls by 300 hours", "Gamma's benefits arrive about three months later"],
                ["B. Testers take on 80 hours of test-automation scripting estimated as developer work", "Demand falls by 80 hours", "Uses tester surplus; small learning curve"],
                ["C. Contract developer at 0.5 FTE for 10 weeks", "Capacity rises by about 159 hours (187.5 hours x 85% productive)", "Contractor cost for 10 weeks"],
                ["D. Cut 120 hours of lower-priority Beta features", "Demand falls by 120 hours", "Features move to a later release"],
                ["E. Two hours' overtime a week for all developers", "Capacity rises by about 126 hours", "Unsustainable over a quarter; not recommended"],
            ),
            "Options A and B together remove 380 hours, bringing developer demand to 1,770 hours against 1,772 hours of "
            "capacity. On paper the gap is closed, but utilisation is 100%, with nothing left for urgent defects or "
            "estimating error. The portfolio board therefore also approves option C. Developer capacity becomes about "
            "1,931 hours against 1,770 hours of demand, a utilisation of about **92%**, leaving roughly 160 hours of "
            "buffer. Option D is held in reserve if Gamma is approved early.",
            TIP("Closing the gap to exactly zero is not the goal. Aim for a plan that leaves a buffer, because real work "
                "always contains surprises."),
        ),
        S(
            "What to do with surplus capacity",
            "In example 2 the testers had about 175 spare hours. Decide how to use spare capacity rather than letting it "
            "fill with low-value work:",
            L(
                "**Pull forward** approved work waiting on that skill, or absorb work from a constrained role.",
                "**Invest in improvement**: automation, documentation or technical debt that frees capacity later.",
                "**Train and cross-skill**, using a [training plan](/templates/training-plan-template/).",
                "**Lend capacity** to another team, or reduce contractor use.",
            ),
            "A surplus that persists for several cycles suggests the skill mix no longer matches the work.",
        ),
        S(
            "Capacity planning strategies: lead, lag and match",
            "When demand is growing, there are three classic strategies for adding capacity. They come from operations "
            "management but apply equally to project teams.",
            T(
                ["Strategy", "What it means", "When to use it", "Main risk"],
                ["Lead", "Add capacity before demand arrives", "Growth is near certain and delay is costly, for example a signed programme of work", "Paying for idle capacity if demand does not appear"],
                ["Lag", "Add capacity only once demand is confirmed", "Budgets are tight or demand is uncertain", "Overload and delays while you recruit"],
                ["Match", "Add capacity in small steps as demand grows", "Most project organisations; balances cost and risk", "Needs frequent reviews to time each step"],
                ["Fixed-team (Agile)", "Keep stable teams and prioritise work into their capacity", "Product teams with continuous demand", "Low-priority work may wait a long time"],
            ),
            "Many organisations combine them: a permanent core for steady demand, contractors for confirmed peaks and "
            "early recruitment for strategic skills.",
        ),
        S(
            "Utilisation targets and buffers",
            "It is tempting to plan everyone at 100% of productive capacity. In practice, a fully loaded team has no "
            "room to absorb urgent work, estimating error or sickness, so queues form and every item waits longer. The "
            "same idea underpins [WIP limits](/project-management/kanban/wip-limits/) in Kanban and the shared buffers "
            "in [critical chain project management](/project-management/critical-chain-project-management/).",
            L(
                "Keep a buffer of unallocated productive capacity, often 10-15%, and protect it.",
                "Plan shared specialists more lightly than generalists, because they are pulled in many directions.",
                "In agencies, keep planned project utilisation separate from billable utilisation.",
                "Watch the trend: planned at 90% but running at 110% every month means your estimates or factors are wrong.",
            ),
            "There is no universal correct rate. Set a target per role and compare it with actuals each cycle.",
        ),
        S(
            "Who owns capacity planning and how often to review it",
            "Capacity planning works when ownership is clear and everyone knows when the numbers will be refreshed.",
            T(
                ["Role", "Responsibility"],
                ["Portfolio board or sponsor", "Makes the priority calls when demand exceeds capacity"],
                ["PMO or resource manager", "Owns the capacity model, consolidates demand, runs the review and reports gaps"],
                ["Functional or line managers", "Provide capacity by role: headcount, leave, skills, recruitment plans"],
                ["Project managers", "Provide remaining demand by role and month, and flag changes early"],
                ["Team leads", "Keep operational allocation and actual utilisation up to date"],
                ["Finance and HR", "Turn gaps into budgets, hiring plans and contractor approvals"],
            ),
            "In many organisations the [project management office](/project-management/project-management-office-pmo/) "
            "is the natural owner because it already sees the whole portfolio. Decisions about which projects to start "
            "belong to portfolio management; see [program vs project vs portfolio management](/project-management/program-vs-project-vs-portfolio-management/) for how the levels fit together.",
            T(
                ["Plan level", "Typical review cadence"],
                ["Strategic", "Annually, refreshed quarterly"],
                ["Tactical (portfolio)", "Monthly"],
                ["Operational (team)", "Weekly, fortnightly or every sprint"],
                ["Any level", "Immediately after a major change: a large project approved, cancelled or re-scoped, or a key person leaving"],
            ),
            "Comparing forecast with actual at each review improves your factors, estimates and "
            "[project forecasting](/project-management/project-forecasting/).",
        ),
        S(
            "Capacity planning tools and templates",
            "A spreadsheet is enough for one team or a small portfolio: a tab for capacity by role, a tab for demand "
            "by project and a summary of gaps and utilisation. Keep demand aligned with each project's "
            "[project schedule template](/templates/project-schedule-template/) or "
            "[project tracker](/templates/project-tracker-template/).",
            "Once several projects share people, [project management software](/project-management/project-management-software/) "
            "saves manual consolidation. Workload features often sit on higher plans:",
            L(
                "[Wrike](/project-management-tools/wrike/), our top-rated tool, shows team workload and capacity, "
                "accounts for working hours and holidays, and includes time tracking. Advanced resource and capacity "
                "planning, including role-based planning, is among its Pinnacle capabilities, which suits PMOs.",
                "[monday.com](/project-management-tools/monday/) has a visual workload view on Pro, with resource management on Enterprise.",
                "[Asana](/project-management-tools/asana/) includes workload, portfolios and time tracking on Advanced.",
                "[Smartsheet](/project-management-tools/smartsheet/) has workload tracking on Business and above, plus a "
                "Resource Management add-on.",
                "[Jira](/project-management-tools/jira/) Premium adds Plans for cross-team roadmaps and capacity.",
            ),
            "Whatever the tool, the inputs matter most: honest remaining estimates, real leave data and an "
            "evidence-based productive-time factor.",
        ),
        S(
            "Common capacity planning mistakes",
            L(
                "**Counting contracted hours as capacity.** Plans built on 40 productive hours a week are short before they start.",
                "**Planning by headcount instead of skill.** Totals hide the bottleneck role, as example 2 shows.",
                "**Ignoring business-as-usual and support.** Routine work is real demand even if no project plan lists it.",
                "**Leaving out the pipeline.** Unapproved projects become approved projects; weight them by probability.",
                "**Using original estimates instead of remaining work.** Late projects need more hours than their plans say.",
                "**Planning to 100%.** There is no room for surprises, so planned work slips when they arrive.",
                "**Treating it as a one-off exercise.** An unreviewed plan is out of date within weeks.",
                "**Hiding the gap.** Absorbing shortfalls with overtime protects today's dates at the expense of next quarter's.",
            ),
            "Read our guide to [resource allocation](/project-management/resource-allocation/) for the next step: turning an approved capacity plan into named assignments.",
        ),
    ],
    faq=[
        ("What is capacity planning in project management?",
         "It is the process of comparing the work demanded by projects and day-to-day operations with the productive "
         "time and skills available, for a team or portfolio over a set period, so that gaps can be fixed before they "
         "delay delivery."),
        ("How do you calculate capacity for capacity planning?",
         "Multiply the number of people by their contracted hours and the weeks in the period, subtract leave, holidays "
         "and training, then multiply by a productive-time factor, such as 75-80%, to allow for meetings, admin and "
         "support. Do this separately for each role or skill."),
        ("What is an example of capacity planning?",
         "Five designers have 800 contracted hours in a month; after leave and an 80% productive factor that is 608 "
         "hours. Demand is 680 hours, so the team is 72 hours (0.56 FTE) short and must defer work, add a freelancer "
         "or pause requests."),
        ("What is the difference between capacity planning and resource planning?",
         "Capacity planning compares total supply with total demand across a team or portfolio, usually by role and "
         "over months. Resource planning works out what one project needs, and resource allocation assigns named "
         "people to specific tasks."),
        ("What is a good utilisation rate in capacity planning?",
         "There is no single correct figure. Many teams plan productive capacity at roughly 85-90% so that a buffer of "
         "10-15% remains for urgent work and estimating error. Set targets per role and compare them with actuals."),
        ("What are the three capacity planning strategies?",
         "Lead adds capacity before demand arrives, lag waits until demand is confirmed, and match adds capacity in "
         "small steps as demand grows. Agile organisations often use a fourth approach: fixed teams with work "
         "prioritised into their capacity."),
        ("What is the difference between capacity and availability?",
         "Availability is the time someone is at work and not on leave. Capacity, in the productive sense, is the part "
         "of that available time that can go on planned work once meetings, admin and support are taken out."),
        ("How often should capacity plans be updated?",
         "Monthly is common for portfolio plans, weekly or every sprint for team plans, and annually with quarterly "
         "refreshes for strategic workforce plans. Update immediately after a major change in projects or people."),
        ("Who is responsible for capacity planning?",
         "Usually the PMO or a resource manager owns the model, line managers supply capacity, project managers supply "
         "demand, and a portfolio board or sponsor makes the priority decisions when demand exceeds capacity."),
        ("How do you include projects that are not yet approved?",
         "Estimate their effort by role and multiply it by the probability of approval. A 500-hour project with a 60% "
         "chance adds 300 hours of weighted demand. Replace the weighted figure with the full estimate once it is approved."),
        ("How does capacity planning work in Agile?",
         "Agile teams estimate how much work fits each sprint from team availability, a focus factor and past velocity, "
         "then commit only to that. See our [agile capacity planning](/project-management/agile/agile-capacity-planning/) guide for the formula."),
        ("What tools are used for capacity planning?",
         "Spreadsheets work for small teams. Larger portfolios use the workload and resource features of tools such "
         "as Wrike, monday.com, Asana, Smartsheet or Jira, which often sit on higher-tier plans or add-ons."),
        ("How does FTE relate to capacity planning?",
         "FTE expresses capacity and demand in full-time-person units, which makes gaps easy to communicate, for "
         "example \"1.3 developers short next quarter\". See our guide to [full-time equivalent](/project-management/full-time-equivalent-fte/)."),
    ],
)
