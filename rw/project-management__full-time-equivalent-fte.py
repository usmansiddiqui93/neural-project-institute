from core import S, L, OL, T, TIP, H3

URL = "/project-management/full-time-equivalent-fte/"

RW = dict(
    title="Full-Time Equivalent (FTE): Meaning, Formula and Examples",
    desc="Full-time equivalent (FTE) explained: the formula, conversion tables, worked examples for teams and projects, FTE vs headcount and common mistakes.",
    intro=(
        "A full-time equivalent (FTE) is a unit that expresses how much working time a person, team or piece of work "
        "represents compared with one full-time employee: 1.0 FTE is one full-time schedule, and someone working half "
        "that schedule is 0.5 FTE. This guide gives you the FTE formula, a conversion table, four worked examples and a "
        "step-by-step method for using FTE to staff, cost and track a project."
    ),
    takeaways=[
        "FTE = hours worked or planned / full-time hours for the same period.",
        "Always state your full-time basis (for example 37.5 or 40 hours a week), because the same hours give different FTE figures under different bases.",
        "Contracted FTE is what someone is paid for; allocated FTE is what your project gets. Plan against productive hours, not the full contract.",
        "To staff a project, divide the estimated effort hours by the productive hours one FTE supplies in that period.",
        "FTE measures capacity; headcount counts people. Five part-time people can be fewer than four FTE.",
        "FTE converts directly into cost: FTE x hours per FTE x hourly rate.",
    ],
    sections=[
        S(
            "What is a full-time equivalent (FTE)?",
            "A **full-time equivalent (FTE)** is a standard unit of working time equal to one person working a full-time "
            "schedule for a given period. Part-time or shared work is expressed as a fraction of that unit, so a person on "
            "20 hours in a 40-hour organisation is 0.5 FTE. FTE measures time and capacity, not the number of people.",
            "Because it converts every working pattern into the same unit, FTE lets you add up and compare effort that "
            "would otherwise be hard to compare: a full-time developer, a part-time analyst on three days a week, a "
            "designer shared with two other projects and a contractor booked for 15 hours a week can all be expressed in "
            "FTE and summed.",
            "FTE turns up in two main places:",
            L(
                "**HR and finance**, where it describes the size of the workforce, drives salary budgets and is used in "
                "some legal and reporting tests.",
                "**Project and resource management**, where it describes how much capacity a project needs (demand), how "
                "much is available (supply) and what that capacity costs. This guide concentrates on the project use, which "
                "most HR-focused explanations skip.",
            ),
            "FTE is also used as a noun for a role: \"we need two more FTEs\" means two full-time people's worth of time, "
            "which could be filled by two full-time hires, four people at 0.5 FTE, or a mix.",
        ),
        S(
            "The FTE formula",
            "The basic formula is the same whatever period you use:",
            TIP("**FTE = hours worked (or planned) / hours in a full-time schedule for the same period**"),
            "The only things that change are the period and the full-time hours that go with it.",
            T(
                ["Version", "Formula", "Example (40-hour basis)"],
                ["Weekly", "Hours per week / standard weekly hours", "30 / 40 = 0.75 FTE"],
                ["Monthly", "Hours in the month / standard monthly hours", "120 / 160 = 0.75 FTE (using four 40-hour weeks)"],
                ["Annual", "Hours in the year / standard annual hours", "1,560 / 2,080 = 0.75 FTE"],
                ["Project period", "Total effort hours / (standard weekly hours x weeks in the period)", "600 / (40 x 20) = 0.75 FTE"],
                ["Team or organisation", "Sum of everyone's hours / standard hours for one person", "1,000 weekly hours / 40 = 25 FTE"],
            ),
            H3("Choosing the full-time basis"),
            "The organisation, not the formula, defines what full time means. Common bases are 35, 37.5 and 40 hours a "
            "week. In the UK there is no legal number of hours that makes someone full time; the government's nidirect "
            "guidance says a full-time worker usually works 35 hours or more a week. Many US organisations use 40 hours, "
            "which gives the familiar annual figure of 40 x 52 = **2,080 hours**. A 37.5-hour week gives 37.5 x 52 = "
            "**1,950 hours**.",
            "Pick the basis your organisation uses for contracts and write it next to every FTE figure, for example "
            "\"2.5 FTE (37.5-hour basis)\". The same 30 hours a week is 0.86 FTE on a 35-hour basis, 0.80 on 37.5 hours and "
            "0.75 on 40 hours, so an unstated basis is the most common source of FTE confusion between teams, countries "
            "and suppliers.",
            H3("Converting FTE back to hours"),
            "Reverse the formula when you need hours, for example to book people or estimate cost:",
            TIP("**Hours = FTE x full-time hours for the period**"),
            "0.6 FTE on a 37.5-hour basis is 0.6 x 37.5 = 22.5 hours a week. 2.5 FTE for 12 weeks on a 40-hour basis is "
            "2.5 x 40 x 12 = 1,200 hours.",
        ),
        S(
            "FTE conversion table",
            "Use this table to convert weekly hours into FTE under the three most common full-time bases. Values are "
            "rounded to two decimal places.",
            T(
                ["Hours per week", "35-hour basis", "37.5-hour basis", "40-hour basis"],
                ["8 (one day)", "0.23", "0.21", "0.20"],
                ["15", "0.43", "0.40", "0.38"],
                ["16 (two days)", "0.46", "0.43", "0.40"],
                ["20", "0.57", "0.53", "0.50"],
                ["22.5", "0.64", "0.60", "0.56"],
                ["24 (three days)", "0.69", "0.64", "0.60"],
                ["28", "0.80", "0.75", "0.70"],
                ["30", "0.86", "0.80", "0.75"],
                ["32 (four days)", "0.91", "0.85", "0.80"],
                ["35", "1.00", "0.93", "0.88"],
                ["37.5", "1.07", "1.00", "0.94"],
                ["40", "1.14", "1.07", "1.00"],
            ),
            "Figures above 1.0 mean someone is working more than the organisation's full-time schedule. That is "
            "possible in a calculation, but a plan that relies on it is a warning sign, as explained under common mistakes.",
        ),
        S(
            "How to calculate FTE step by step",
            "Whether you are sizing a team, a department or a project, the method is the same.",
            OL(
                "**Confirm the full-time basis.** Find the standard weekly hours in your organisation's contracts, such as 37.5 hours.",
                "**Choose the period.** Week, month, year or the project period. Use the same period for the hours and for the full-time standard.",
                "**Work out full-time hours for that period.** For example 37.5 x 52 = 1,950 hours a year, or 40 x 10 = 400 hours for a 10-week phase.",
                "**Collect the hours.** For an existing team use contracted, timesheet or payroll hours. For a project use estimated effort hours from your estimates.",
                "**Add the hours together** for everyone or everything you want to measure.",
                "**Divide** the total hours by the full-time hours for the period.",
                "**Round sensibly.** Two decimal places for people (0.75), one decimal place for plans (2.5 FTE). Spurious precision such as 3.137 FTE implies certainty you do not have.",
                "**Record the basis and the source** next to the result, for example \"4.25 FTE, 37.5-hour basis, 2026 payroll hours\".",
            ),
        ),
        S(
            "Worked example 1: FTE of a mixed team",
            "This is an illustrative example. Full time in this organisation is 40 hours a week.",
            T(
                ["Person", "Hours per week", "FTE"],
                ["Project manager", "40", "1.0"],
                ["Developer 1", "40", "1.0"],
                ["Developer 2", "40", "1.0"],
                ["Analyst (part time)", "24", "0.6"],
                ["Designer (shared with another team)", "16", "0.4"],
                ["**Total**", "**160**", "**4.0**"],
            ),
            "Five people provide 4.0 FTE, because 160 / 40 = 4.0. Headcount is 5, but the capacity is that of four "
            "full-time people. If you estimated the work assuming five full-time people, the plan would be 25% short "
            "before a single task started.",
        ),
        S(
            "Worked example 2: annual FTE with joiners, part-timers and contractors",
            "Annual FTE is useful for budgets and year-end reporting, and it handles people who were only present for part "
            "of the year. In this illustrative example the organisation uses a 37.5-hour week, so one FTE year is "
            "37.5 x 52 = 1,950 hours.",
            T(
                ["Who", "Pattern", "Hours in the year"],
                ["3 full-time staff", "37.5 hours x 52 weeks each", "5,850"],
                ["1 part-time analyst", "22.5 hours x 52 weeks", "1,170"],
                ["1 joiner", "37.5 hours x 26 weeks (joined mid-year)", "975"],
                ["1 contractor", "15 hours x 20 weeks", "300"],
                ["**Total**", "", "**8,295**"],
            ),
            "Annual FTE = 8,295 / 1,950 = **4.25 FTE**, from a headcount of six people. Whether the contractor is "
            "included depends on why you are counting: include them when you measure the capacity the team actually "
            "used or the cost of delivery, and exclude them when you report employee FTE to HR or finance. Say which you did.",
        ),
        S(
            "Worked example 3: converting project effort into FTE",
            "This is the calculation project managers use most. Suppose an illustrative project needs 1,200 hours of "
            "development effort over 10 weeks, and the organisation's standard week is 40 hours.",
            OL(
                "Hours one FTE supplies in 10 weeks: 40 x 10 = 400 hours.",
                "Nominal FTE needed: 1,200 / 400 = 3.0 FTE.",
                "Adjust for productive time. If about 80% of a developer's hours go on project work once meetings, "
                "support and admin are taken out, each FTE supplies 400 x 0.8 = 320 project hours.",
                "FTE to staff against: 1,200 / 320 = **3.75 FTE**.",
            ),
            "The second figure is the one to request. Planning with 3.0 FTE would leave the team 240 hours short, which is "
            "three weeks of one developer's productive time. The 80% figure is an assumption; use your own timesheet data "
            "where you have it, and record the assumption in the plan.",
            "See our guide to [effort estimation](/project-management/effort-estimation/) for how the 1,200 hours might be estimated.",
            H3("Building an FTE profile by month"),
            "Real projects rarely need a flat level of effort. Converting estimated hours per role per month into FTE "
            "gives you a profile you can compare with what each team can supply. In this illustrative six-month website "
            "project, one FTE month is taken as 160 hours (four 40-hour weeks) for simplicity.",
            T(
                ["Role", "Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"],
                ["Project manager", "0.5", "0.5", "0.5", "0.5", "0.5", "0.5"],
                ["Designer", "1.0", "1.5", "0.5", "0", "0", "0"],
                ["Developers", "0", "2.0", "3.0", "3.0", "2.0", "0.5"],
                ["Tester", "0", "0", "0.5", "1.0", "1.5", "0.5"],
                ["**Total FTE**", "**1.5**", "**4.0**", "**4.5**", "**4.5**", "**4.0**", "**1.5**"],
            ),
            "Each cell is hours divided by 160; for example 480 developer hours in month 3 is 3.0 FTE. The profile shows "
            "at a glance that the project peaks at 4.5 FTE in months 3 and 4, that design needs 1.5 FTE in month 2 (so one "
            "designer is not enough that month), and that testing ramps up as development winds down. Build the hours "
            "from your [work breakdown structure](/project-management/work-breakdown-structure/) and "
            "[project schedule](/project-management/project-scheduling/), and record the profile in a "
            "[project schedule template](/templates/project-schedule-template/) or resource plan.",
        ),
        S(
            "Worked example 4: turning FTE into project cost",
            "FTE converts directly into labour cost, which is why it is so useful for "
            "[cost estimation](/project-management/cost-estimation/). The formula is:",
            TIP("**Labour cost = FTE x hours per FTE in the period x hourly rate**"),
            "Using example 3, 3.75 developer FTE for 10 weeks at 40 hours, with an illustrative fully loaded rate of $90 "
            "an hour: 3.75 x 40 x 10 x $90 = **$135,000**. A fully loaded rate includes salary plus on-costs such as "
            "employer taxes, pension and overheads; ask finance which rate to use, because salary alone understates cost.",
            "Most teams have several rates, so build the estimate by role:",
            T(
                ["Role", "FTE", "Hours (10 weeks x 40)", "Rate (illustrative)", "Cost"],
                ["Project manager", "0.5", "200", "$95", "$19,000"],
                ["Developers", "3.75", "1,500", "$90", "$135,000"],
                ["Tester", "1.0", "400", "$70", "$28,000"],
                ["**Total**", "**5.25**", "**2,100**", "", "**$182,000**"],
            ),
            "The total labour cost then feeds your [project budget](/project-management/project-budget/) and "
            "[budget at completion](/project-management/budget-at-completion/). Our "
            "[project cost estimate template](/templates/project-cost-estimate-template/) and "
            "[budget template](/templates/budget-template/) have the columns to do this by role.",
            "See our guide to the [project budget](/project-management/project-budget/) for how labour, contingency and reserves fit together.",
        ),
        S(
            "Contracted, available and allocated FTE",
            "Most FTE mistakes in projects come from mixing up three different figures. Keep them separate in your plans.",
            T(
                ["Term", "What it means", "Example"],
                ["Contracted FTE", "The working time someone is employed and paid for", "Priya is contracted for 32 of 40 hours: 0.8 FTE"],
                ["Available (productive) FTE", "Contracted time minus leave, public holidays, training, admin and meetings", "About 0.55 FTE after leave and overheads (assumptions below)"],
                ["Allocated FTE", "The share assigned to a specific project or activity", "0.5 FTE to Project A, 0.2 FTE to Project B"],
            ),
            H3("How many productive hours is 1 FTE?"),
            "On a 40-hour basis, one FTE year is 2,080 hours, but nobody works all of them on a project. This illustrative "
            "calculation shows why. Substitute your organisation's own leave entitlement and figures.",
            T(
                ["Step", "Hours", "Running total"],
                ["Contracted hours (40 x 52)", "2,080", "2,080"],
                ["Less annual leave (assume 25 days x 8 hours)", "-200", "1,880"],
                ["Less public holidays (assume 8 days)", "-64", "1,816"],
                ["Less sickness and training allowance (assume 5 days)", "-40", "1,776"],
                ["Available hours", "", "1,776"],
                ["Less meetings, admin and support (assume 20%)", "-355", "1,421"],
                ["**Productive project hours per FTE**", "", "**about 1,421**"],
            ),
            "Under these assumptions one FTE supplies about 1,421 project hours a year, roughly 68% of the contracted "
            "2,080. Planning against 2,080 would overstate capacity by almost half.",
            H3("Allocation example"),
            "Priya (0.8 FTE contracted) is allocated 0.5 FTE to Project A, 0.2 FTE to Project B and 0.1 FTE to team duties, "
            "which adds up to her 0.8. If Project C now asks for 0.5 FTE of her time, her total allocation becomes 1.3 FTE "
            "against a 0.8 FTE contract. Showing contracted and allocated FTE side by side in the resource plan makes "
            "that over-allocation visible before it becomes overtime or missed dates. Our guides to "
            "[resource allocation](/project-management/resource-allocation/) and "
            "[resource levelling](/project-management/resource-leveling/) explain how to resolve it.",
        ),
        S(
            "FTE vs headcount",
            "FTE and headcount both describe the size of a team, but they answer different questions.",
            T(
                ["", "FTE", "Headcount"],
                ["Measures", "Working time supplied", "Number of people"],
                ["Part-time worker on 20 of 40 hours", "0.5", "1"],
                ["Two job-sharers covering one role", "1.0", "2"],
                ["Can be fractional?", "Yes", "No"],
                ["Useful for", "Capacity, effort, cost and budget planning", "HR records, licences, equipment, desk space, onboarding, management span"],
                ["Main risk if used alone", "Hides the overhead of many part-time or shared people", "Overstates capacity when many people are part time"],
            ),
            H3("When to use each"),
            L(
                "Use **FTE** for anything driven by working time: estimating, staffing requests, budgets, capacity and "
                "utilisation reporting.",
                "Use **headcount** for anything driven by the number of people: software seats, laptops, onboarding, "
                "communication and team size.",
                "Report **both** when they differ a lot. A team of 12 people providing 7.5 FTE has more coordination "
                "overhead than a team of 8 full-time people providing 8.0 FTE, even though the FTE figures are similar.",
            ),
        ),
        S(
            "How project managers use FTE",
            "FTE gives project managers a common language with resource managers, finance and the "
            "[PMO](/project-management/project-management-office-pmo/). Typical uses include:",
            L(
                "**Resource plans:** each role with the FTE needed per period, for example \"2.0 FTE developers, months 2 to 5\". "
                "See [project resources](/project-management/project-resources/) for what a resource plan contains.",
                "**Capacity planning:** comparing the FTE a team can supply with the FTE projects demand.",
                "**Estimating:** converting effort hours into team size and duration, and checking whether a deadline is realistic.",
                "**Budgeting:** converting FTE into labour cost for the [cost management plan](/project-management/cost-management-plan/).",
                "**Staffing requests and business cases:** asking for \"1.5 FTE business analyst for six months\" is clearer than asking for \"some BA help\".",
                "**Tracking:** comparing planned FTE with actual FTE from timesheets in the [project status report](/project-management/project-status-report/).",
            ),
            H3("Portfolio example: FTE supply vs demand"),
            "In this illustrative example, a delivery team has six full-time people and two people at 0.6 FTE on a "
            "40-hour basis, so contracted capacity is 6 + 1.2 = **7.2 FTE**. After leave, training and team overheads, "
            "the team leader assumes 85% is available for project work: 7.2 x 0.85 = **6.1 FTE** (rounded).",
            T(
                ["Demand next quarter", "FTE"],
                ["Project A (in delivery)", "3.0"],
                ["Project B (starting)", "2.5"],
                ["Project C (proposed)", "1.0"],
                ["**Total demand**", "**6.5**"],
                ["**Available supply**", "**6.1**"],
                ["**Gap**", "**-0.4**"],
            ),
            "The team is about 0.4 FTE short, or roughly 16 hours a week on a 40-hour basis. Expressing the gap in FTE "
            "turns a vague sense of being busy into a decision the sponsor can make: delay Project C, bring in a "
            "contractor for 0.4 FTE, reduce scope, or accept a later finish. This kind of comparison is the core of "
            "[managing multiple projects](/project-management/managing-multiple-projects/).",
            "See our guide to [capacity planning](/project-management/capacity-planning/) for a full supply-and-demand method.",
        ),
        S(
            "FTE in HR and employment rules",
            "In project planning, FTE is simply a unit of capacity. In HR it can also have legal or contractual "
            "meaning, and the definitions differ from country to country, so check with HR or legal advisers before "
            "using an FTE figure for anything other than planning.",
            L(
                "**United States (Affordable Care Act):** the IRS treats a full-time employee as someone averaging at "
                "least 30 hours of service a week, or 130 hours in a calendar month. For the applicable large employer "
                "test, you add the monthly hours of employees who are not full time, counting no more than 120 hours per "
                "person, and divide by 120 to get full-time equivalent employees. An employer with 50 or more full-time "
                "plus full-time equivalent employees on average in the previous year is an applicable large employer.",
                "**United Kingdom:** there is no legal definition of full-time hours; the government's nidirect guidance "
                "says full-time workers usually work 35 hours or more a week, and employers set their own standard.",
                "**Elsewhere:** standard working weeks and statutory rules vary, so international projects should agree "
                "one planning basis and convert local hours into it.",
            ),
            TIP("A legal FTE test (such as the US 30-hour rule) and your planning basis (such as 40 hours) can give different "
                "figures for the same person. Keep them apart: use the legal test only for compliance and your contracted "
                "standard for project plans."),
        ),
        S(
            "Tracking FTE in templates and software",
            "For a single project, a spreadsheet works well: list each person or role, their contracted FTE, their "
            "allocated FTE per week or month and the resulting hours. Our [skills matrix template](/templates/skills-matrix-template/) "
            "helps you see who has the skills a role needs before you allocate FTE to them, and the "
            "[project schedule template](/templates/project-schedule-template/) holds dates and owners.",
            "Once you run several projects with shared people, spreadsheets become hard to keep consistent, and "
            "[project management software](/project-management/project-management-software/) with workload views helps:",
            L(
                "[Wrike](/project-management-tools/wrike/) (our top-rated tool) shows team workload and capacity, "
                "accounts for working hours, non-working days and holidays, and supports time tracking. Advanced, "
                "role-based resource and capacity planning is part of its Pinnacle plan, which suits PMOs and "
                "professional services firms that plan in FTE across a portfolio.",
                "[monday.com](/project-management-tools/monday/) offers workload views on its Pro plan, which is often "
                "enough for basic capacity planning in small and mid-sized teams.",
                "[Asana](/project-management-tools/asana/) includes workload on its Advanced plan, alongside portfolios "
                "and goals for cross-team work.",
                "[Smartsheet](/project-management-tools/smartsheet/) provides workload tracking on Business and above, "
                "with a Resource Management add-on for capacity planning, time tracking and project budgets.",
            ),
            "Whichever tool you use, set each person's working hours and leave correctly first. Workload views are only "
            "as accurate as the capacity behind them.",
        ),
        S(
            "Common FTE mistakes",
            L(
                "**Not stating the full-time basis.** 2.0 FTE on a 35-hour basis is 70 hours a week; on a 40-hour basis it is 80.",
                "**Treating 1.0 FTE as 40 productive project hours.** Leave, meetings, support and admin reduce it, often to two-thirds or less.",
                "**Allocating one person to several projects at 1.0 FTE each.** Add up every allocation per person and compare it with their contracted FTE.",
                "**Mixing contracted and allocated FTE** in the same column, so nobody can tell what the project actually gets.",
                "**Assuming FTE is interchangeable.** Two 0.5 FTE people rarely deliver the same as one 1.0 FTE person; handovers and context switching cost time, and skills differ.",
                "**Splitting people into many small fractions.** Someone on five projects at 0.2 FTE each loses time to switching between them. Prefer fewer, larger allocations.",
                "**Planning above 1.0 FTE.** It may balance the spreadsheet, but it relies on overtime and increases burnout and quality risk.",
                "**Using salary instead of a fully loaded rate** when converting FTE into cost.",
                "**Never comparing plan with actuals.** Check planned FTE against timesheet hours each month and adjust future estimates.",
            ),
            TIP("In every resource plan, show contracted FTE, allocated FTE and the difference for each person. The difference "
                "shows what they owe to other work and is the quickest way to spot over-allocation."),
            "See our guide to [resource allocation](/project-management/resource-allocation/) for how to assign people once you know the FTE you need.",
        ),
    ],
    faq=[
        ("What does FTE stand for?",
         "FTE stands for full-time equivalent: a unit that expresses working time relative to one full-time employee. "
         "1.0 FTE is one full-time schedule."),
        ("How do you calculate FTE?",
         "Divide the hours worked or planned by the hours in a full-time schedule for the same period. For example, 30 "
         "hours in a 40-hour week is 30 / 40 = 0.75 FTE."),
        ("How many hours is 1 FTE per year?",
         "It depends on the organisation's full-time standard. On a 40-hour week it is 40 x 52 = 2,080 hours; on 37.5 "
         "hours it is 1,950 hours. Productive project hours are lower once leave, holidays and overheads are removed."),
        ("What is 0.5 FTE?",
         "Half of a full-time schedule: 20 hours a week when full time is 40 hours, or 18.75 hours when full time is 37.5 hours."),
        ("What is 0.8 FTE?",
         "Four-fifths of a full-time schedule, usually four days a week. That is 32 hours on a 40-hour basis or 30 hours "
         "on a 37.5-hour basis."),
        ("What is the difference between FTE and headcount?",
         "Headcount counts people; FTE measures the working time they provide. Two half-time people are a headcount of 2 "
         "but 1.0 FTE."),
        ("How do you convert project hours to FTE?",
         "Divide total effort hours by the hours one FTE supplies in the project period. 1,200 hours over 10 weeks at 40 "
         "hours a week is 1,200 / 400 = 3.0 FTE, or 3.75 FTE if only 80% of each person's time is productive project time."),
        ("Can FTE be more than 1 for one person?",
         "In a calculation it can, if someone regularly works more than the standard week. In a plan, allocating anyone "
         "above 1.0 FTE is a warning sign of overtime, burnout and quality risk."),
        ("Is 37.5 hours a week 1 FTE?",
         "It is if the organisation defines full time as 37.5 hours. FTE is always relative to the organisation's own standard."),
        ("Do contractors count in FTE?",
         "For project capacity and cost, yes: include their hours, because they supply working time. For employee FTE "
         "reported by HR or finance they are usually excluded. State which approach you used."),
        ("Does overtime count towards FTE?",
         "If you measure actual capacity used, overtime hours count and can push FTE above contracted levels. For planning, "
         "base FTE on standard hours and treat overtime as a risk response, not as capacity."),
        ("Does 1 FTE mean 100% project time?",
         "No. 1 FTE means a full-time schedule. The share actually spent on the project is usually lower once leave, "
         "meetings, support and other duties are counted."),
        ("How is FTE used in resource plans?",
         "Resource plans list each role with the FTE needed per period, such as 2.0 FTE developers in months 2 to 6, so "
         "they can be compared with available capacity and costed. See our guide to "
         "[project resources](/project-management/project-resources/)."),
    ],
)
