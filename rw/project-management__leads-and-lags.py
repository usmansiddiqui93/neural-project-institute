from core import S, L, OL, T, TIP, H3

URL = "/project-management/leads-and-lags/"

RW = dict(
    title="Leads and Lags in Project Management: Guide with Examples",
    desc="Leads and lags in project management explained: lead vs lag, notation, date formulas, worked examples, critical path effects and scheduling rules.",
    intro=(
        "Leads and lags in project management are adjustments to the link between two dependent activities: a lag "
        "adds a deliberate wait before the successor can start or finish, and a lead lets the successor start early so "
        "the two activities overlap. This guide explains the notation, the date formulas for every dependency type, "
        "worked examples with the critical path, and the rules experienced schedulers follow."
    ),
    takeaways=[
        "A lag adds waiting time to a dependency (FS+3d); a lead overlaps activities and is entered as a negative lag (FS-2d).",
        "Lags are not activities: no one works during them and they use no resources, but they still add time to any path they sit on.",
        "Leads shorten the schedule but are a form of fast tracking, so they add rework risk.",
        "Never use a lag to hide real work, supplier lead time or contingency; model those as activities or buffers.",
        "State whether each lag is in working days or calendar days and record why it exists.",
        "Schedule quality checks such as the DCMA 14-point assessment aim for no leads and lags on no more than 5% of links.",
    ],
    sections=[
        S(
            "What are leads and lags?",
            "**Leads and lags** are time adjustments applied to a dependency between a predecessor and a successor "
            "activity. A **lag** delays the successor, for example waiting three days for concrete to cure before "
            "building walls. A **lead** advances the successor so it starts before the predecessor finishes, for example "
            "starting testing two days before development ends.",
            "PMI's glossary describes them in the same way: a lag is the amount of time a successor activity is delayed "
            "with respect to its predecessor, and a lead is the amount of time a successor can be advanced. In other "
            "words, they modify a logical relationship rather than add new work.",
            "Three points follow from that definition:",
            L(
                "**A lag is not an activity.** Nobody is assigned to it, it has no cost and it uses no resources. It is "
                "pure waiting time built into the link.",
                "**A lead is a negative lag.** Most scheduling tools have only one field, usually called Lag, and you "
                "enter a lead as a negative value, such as -2 days.",
                "**Both only exist on a dependency.** You cannot add a lead or lag to an activity on its own. If the "
                "links are wrong, the leads and lags will be too, so start with sound "
                "[task dependencies](/project-management/task-dependencies/).",
            ),
            "See our guide to [predecessors and successors](/project-management/predecessors-and-successors/) for how activities are linked before you add leads or lags.",
        ),
        S(
            "Lead vs lag at a glance",
            T(
                ["", "Lag", "Lead"],
                ["What it does", "Adds waiting time between linked activities", "Overlaps linked activities"],
                ["Notation", "Positive value, e.g. FS+3d", "Negative value, e.g. FS-2d (a negative lag)"],
                ["Typical reasons", "Curing, drying, settling, notice or consultation periods, mandatory waiting times", "Starting work on partial output to save time"],
                ["Effect on the path", "Lengthens it", "Shortens it"],
                ["Uses resources?", "No", "No (but the overlapped work does)"],
                ["Risk", "Low, if the wait is genuine", "Higher: the successor starts on incomplete inputs and may need rework"],
                ["Related technique", "Physical or contractual constraints", "Fast tracking"],
            ),
            "A simple way to remember the difference: a lag is a gap on the [Gantt chart](/project-management/gantt-chart/), "
            "and a lead is an overlap.",
        ),
        S(
            "Leads and lags vs similar terms",
            "The words lead and lag are used in several other ways, and some articles mix them up. In scheduling they "
            "have the narrow meaning above. This table separates them from terms they are often confused with.",
            T(
                ["Term", "What it means", "How it differs from a schedule lead or lag"],
                ["Float (slack)", "How long an activity can slip without delaying a successor or the project", "Float is calculated from the network; a lag is an input you put into it. See [float and slack](/project-management/float-and-slack/)."],
                ["Lead time (supply chain, Lean)", "Time from order or request to delivery", "A duration of a process, not an overlap. Supplier lead time should be modelled as an activity, not a lag."],
                ["Leading and lagging indicators", "Metrics that predict (leading) or confirm (lagging) performance", "Performance measurement, unrelated to dependencies."],
                ["Buffer or contingency", "Time reserved to absorb risk", "A buffer is managed and consumed deliberately; hiding it in a lag makes it invisible. See [critical chain](/project-management/critical-chain-project-management/)."],
                ["Duration", "Working time an activity takes", "Duration belongs to an activity and uses resources; lag belongs to a link and does not."],
                ["Constraint (e.g. start no earlier than)", "A fixed date imposed on an activity", "Use a constraint, not a lag, when an external date drives the start."],
            ),
        ),
        S(
            "Notation and the four dependency types",
            "Leads and lags can be applied to any of the four dependency types. Schedulers usually write them as the link "
            "type followed by the lead or lag, for example FS+3d or SS-1d. Tools often show the predecessor's ID first, "
            "such as 4FS+3d.",
            T(
                ["Dependency", "Meaning", "Lag example", "Lead example"],
                ["Finish-to-start (FS)", "B starts after A finishes", "FS+3d: walls start 3 days after the slab is poured (curing)", "FS-2d: testing starts 2 days before development finishes"],
                ["Start-to-start (SS)", "B starts after A starts", "SS+2d: cable laying starts 2 days after trench digging starts", "SS-1d: set-up starts 1 day before training starts (rare; usually remodelled)"],
                ["Finish-to-finish (FF)", "B finishes after A finishes", "FF+1d: documentation finishes 1 day after the software is finished", "FF-1d: a review finishes 1 day before the drafting finishes"],
                ["Start-to-finish (SF)", "B finishes after A starts", "SF+1d: old system support ends 1 day after the new system goes live", "Rarely used"],
            ),
            "Some tools also accept leads and lags as a **percentage of the predecessor's duration**. Microsoft's own "
            "guidance for Project gives -50% on a finish-to-start link as the way to start the second task when the first "
            "is half complete. Percentage lags adjust automatically if the predecessor's duration changes, which can be "
            "useful but also makes the logic harder to read.",
            "The link types themselves, and when to use each, are covered in our guide to [task dependencies](/project-management/task-dependencies/).",
        ),
        S(
            "How to calculate dates with leads and lags",
            "In a forward pass you calculate each activity's early start (ES) and early finish (EF). Leads and lags slot "
            "into the standard rules as an extra term. In these formulas a lead is simply a negative lag.",
            T(
                ["Link from A to B", "Forward pass rule", "Then"],
                ["FS + lag", "ES(B) = EF(A) + lag", "EF(B) = ES(B) + duration(B)"],
                ["SS + lag", "ES(B) = ES(A) + lag", "EF(B) = ES(B) + duration(B)"],
                ["FF + lag", "EF(B) = EF(A) + lag", "ES(B) = EF(B) - duration(B)"],
                ["SF + lag", "EF(B) = ES(A) + lag", "ES(B) = EF(B) - duration(B)"],
            ),
            "If B has several predecessors, work out the date each link requires and take the **latest**. The backward "
            "pass mirrors these rules: for an FS link, the late finish of A = late start of B - lag, and so on. Our guide "
            "to the [forward and backward pass](/project-management/forward-and-backward-pass/) covers the full method.",
            H3("Mini calculations"),
            "Dates in this guide are counted as elapsed working days from the project start: an activity that starts at "
            "day 0 and lasts 10 days finishes at day 10, and a successor with no lag can start at day 10. Take activity A "
            "(10 days, day 0 to day 10) and a successor B lasting 4 days:",
            T(
                ["Link", "B starts", "B finishes", "Effect"],
                ["FS (no lag)", "Day 10", "Day 14", "Baseline"],
                ["FS+2d", "Day 12", "Day 16", "2-day gap"],
                ["FS-2d (lead)", "Day 8", "Day 12", "2-day overlap"],
                ["SS+3d", "Day 3", "Day 7", "B runs alongside A"],
                ["FF+1d", "Day 7", "Day 11", "B finishes 1 day after A"],
            ),
        ),
        S(
            "Worked example: a lag (curing concrete)",
            "In this illustrative example, A **Pour concrete slab** takes 2 days. B **Build walls** takes 5 days and, "
            "according to the project's (hypothetical) specification, cannot start until the slab has cured for 3 days.",
            T(
                ["Activity", "Link", "Start", "Finish"],
                ["A Pour slab", "-", "Day 0", "Day 2"],
                ["B Build walls", "FS+3d from A", "Day 5", "Day 10"],
            ),
            "The total is 2 + 3 + 5 = 10 days. Nobody works during days 2 to 5 and the lag carries no cost, but it still "
            "sits on the path. If this path is critical, every day of lag is a day on the project end date.",
            H3("Working days or calendar days?"),
            "Curing continues over a weekend; most crews do not work one. That is why many tools let you specify a lag in "
            "elapsed (calendar) time as well as working time. Suppose the slab is finished at the end of a Wednesday on a "
            "Monday-to-Friday calendar:",
            T(
                ["Lag type", "Lag runs over", "Walls can start"],
                ["3 working days", "Thursday, Friday, Monday", "Tuesday"],
                ["3 calendar (elapsed) days", "Thursday, Friday, Saturday", "Monday (next working day)"],
            ),
            "Using the correct unit saves one working day here. The wrong unit either wastes time or, worse, schedules "
            "work before a physical process is complete. Always write the unit next to the lag, for example FS+3ed "
            "(elapsed days) or FS+3d (working days), and agree with the engineer or supplier which one the requirement means.",
        ),
        S(
            "Worked example: a lead (development and testing)",
            "In this illustrative example, C **Develop module** takes 10 days and D **Test module** takes 6 days. The "
            "testers agree they can start on features that are already finished 2 days before development ends.",
            T(
                ["Link", "D starts", "D finishes", "Time saved"],
                ["FS (no lead)", "Day 10", "Day 16", "-"],
                ["FS-2d (lead)", "Day 8", "Day 14", "2 days"],
            ),
            "Using the lead saves 2 days, but testing now starts on an incomplete module. If a late change in development "
            "affects features already tested, some testing must be repeated. Before agreeing a lead, ask what the "
            "successor needs to start, whether that partial output will really exist on the day, and what rework would "
            "cost if it changes.",
            "There are often clearer ways to model the same overlap. FS-2d on a 10-day predecessor gives the same start "
            "date as SS+8d. Better still, split development into two deliverables (for example features 1 to 4 and "
            "features 5 to 6) and link testing of the first batch to the first deliverable with a plain FS link. The "
            "schedule then shows exactly what testing depends on.",
        ),
        S(
            "Worked example: leads and lags in a network and the critical path",
            "This illustrative office fit-out shows how several leads and lags interact and how they affect the "
            "[critical path](/project-management/critical-path-method/) and float.",
            T(
                ["ID", "Activity", "Duration", "Predecessors"],
                ["A", "Strip out and survey", "4 days", "-"],
                ["B", "Install partitions", "6 days", "A (FS)"],
                ["C", "Plaster walls", "5 days", "B (SS+2d), B (FF+1d)"],
                ["D", "Paint", "3 days", "C (FS+2d drying lag)"],
                ["E", "Furniture made and delivered (supplier)", "10 days", "A (FS)"],
                ["F", "Install furniture", "2 days", "D (FS), E (FS)"],
            ),
            "Plastering can start 2 days after partitions start (SS+2d), because the first rooms are ready, but cannot "
            "finish until 1 day after the last partition is in (FF+1d). Paint needs 2 days of drying time after plastering (FS+2d).",
            H3("Forward and backward pass"),
            T(
                ["Activity", "ES", "EF", "LS", "LF", "Total float"],
                ["A", "0", "4", "0", "4", "0"],
                ["B", "4", "10", "4", "10", "0"],
                ["C", "6", "11", "6", "11", "0"],
                ["D", "13", "16", "13", "16", "0"],
                ["E", "4", "14", "6", "16", "2"],
                ["F", "16", "18", "16", "18", "0"],
            ),
            "How the dates were worked out:",
            OL(
                "C: the SS+2d link gives ES = 4 + 2 = 6, so EF = 6 + 5 = 11. The FF+1d link requires EF of at least 10 + 1 = 11, which is met.",
                "D: FS+2d gives ES = 11 + 2 = 13, EF = 16.",
                "E: FS from A gives ES = 4, EF = 14.",
                "F: two predecessors require day 16 (D) and day 14 (E); take the later, so ES = 16 and the project finishes on day 18.",
                "Backward pass: F's late start of 16 gives D and E a late finish of 16. C's late finish is D's late start minus the lag: 13 - 2 = 11. E has 16 - 14 = 2 days of float.",
            ),
            "The critical path is **A-B-C-D-F**, and it includes the SS+2d overlap and the 2-day drying lag. E has 2 "
            "days of float.",
            H3("What-if analysis"),
            T(
                ["Change", "New finish", "Why"],
                ["Drying lag increases from 2 to 3 days", "Day 19 (+1)", "The lag is on the critical path, so it adds directly to the end date"],
                ["Plastering waits for partitions to finish (plain FS, no overlap)", "Day 22 (+4)", "C runs day 10 to 15, D day 17 to 20, F day 20 to 22"],
                ["Supplier needs a 1-day order confirmation period before starting E (FS+1d)", "Day 18 (no change)", "E now finishes on day 15; its float falls from 2 days to 1"],
            ),
            "The example shows the two rules that matter most: a lag on the critical path moves the end date day for day, "
            "and an overlap (a lead, or an SS link with a positive lag) is often what makes a deadline achievable. Our "
            "[critical path template](/templates/critical-path-template/) lets you practise this calculation.",
            "See our guide to the [critical path method](/project-management/critical-path-method/) for the full forward and backward pass procedure.",
        ),
        S(
            "How to apply leads and lags step by step",
            OL(
                "**Build the logic first.** Identify every activity and link them with the right dependency types, with no leads or lags yet. Draw a [project network diagram](/project-management/project-network-diagram/) if the logic is complex.",
                "**Look for genuine waiting time.** Curing, drying, settling, statutory notice or consultation periods, regulator response times. These are lag candidates.",
                "**Check whether the wait is really work.** If someone does something during it (a supplier manufactures, a reviewer reviews), create an activity instead, so it can be resourced and tracked.",
                "**Look for safe overlaps.** Where a successor can start on partial output, decide whether a lead, an SS link with a positive lag, or splitting the predecessor models it most clearly.",
                "**Agree the value and unit** with the person who knows: the engineer, supplier or team lead. Decide on working or calendar days.",
                "**Enter the lead or lag** on the link in your scheduling tool and check the resulting dates on the Gantt chart.",
                "**Document the reason** in the activity notes or schedule basis document, for example \"FS+7ed: minimum 7-day consultation period\".",
                "**Recalculate and check the critical path.** Note which leads and lags are on it, because they drive the end date.",
                "**Review them at every update.** Leads and lags are static; when actual progress differs from the plan, check they still make sense.",
            ),
        ),
        S(
            "Entering leads and lags in scheduling software",
            "Most scheduling tools handle leads and lags in a similar way.",
            L(
                "**Microsoft Project:** open the task's Task Information box, go to the Predecessors tab and type a value "
                "in the Lag column. Microsoft's guidance is to enter a positive number or percentage for lag (such as 2d) "
                "and a negative number or percentage for lead (such as -50%).",
                "**[Wrike](/project-management-tools/wrike/):** its interactive Gantt charts, available from the Team plan "
                "upwards, support all four dependency types with lead and lag time, reschedule successors automatically "
                "when a predecessor moves, and show the critical path, float and baselines. That combination makes it a "
                "good fit for teams who schedule with real dependency logic rather than simple task lists.",
                "**[Microsoft Planner](/project-management-tools/microsoft-planner/):** premium plans include timeline "
                "(Gantt) views and dependencies, and Planner and Project Plan 3 adds the critical path and the Project "
                "desktop application for full scheduling.",
                "**Spreadsheets:** you can model lags with formulas (start = predecessor finish + lag), as in our "
                "[project schedule template](/templates/project-schedule-template/) and "
                "[Gantt chart template](/templates/gantt-chart-template/), but there is no automatic critical path, so "
                "check the logic by hand.",
            ),
            "Our guide to [Gantt chart software](/project-management/gantt-chart-software/) compares dependency and "
            "scheduling features across tools.",
            TIP("Check how your tool treats lag units. Some default to working days on the task's calendar, and some let you "
                "enter elapsed days with a different suffix. A 7-day lag can mean 7 or 9 calendar days depending on the setting."),
        ),
        S(
            "Good practice rules for leads and lags",
            "Leads and lags are easy to misuse, which is why formal schedule assessments look at them closely. Two widely "
            "used references in project controls are the US Government Accountability Office (GAO) Schedule Assessment "
            "Guide and the DCMA 14-point schedule assessment.",
            H3("GAO guidance on lags"),
            L(
                "Each lag should be justified by a real reason outside the schedule, and that reason documented.",
                "Lags should not represent work. Because a lag uses no resources, effort belongs in an activity.",
                "Procurement and work by external parties should be shown as activities, not lags.",
                "A lag should not be used to force a fixed start date; use a date constraint such as start no earlier than instead.",
                "A lag should not be used as a risk buffer, because it stays in the schedule even after the risk it was meant to cover has passed.",
                "Misused lags can distort float and the critical path.",
            ),
            H3("GAO guidance on leads"),
            L(
                "Leads should generally be avoided: a lead implies that a future event dictates the timing of an earlier one.",
                "A lead longer than its successor can produce out-of-sequence logic, where the successor finishes before its predecessor.",
                "Leads are static, so schedules that rely on them need more manual updating and become less reliable as management tools.",
                "Instead, use a start-to-start link with a positive lag, or split the predecessor into smaller activities linked finish-to-start.",
            ),
            H3("DCMA 14-point thresholds"),
            "The DCMA 14-point assessment, as described in schedule analysis tools that implement it, sets two simple "
            "targets: **no leads** (negative lags) at all, because they distort total float, and **lags on no more than 5% "
            "of relationships**. Even if your project is not subject to these checks, they are useful benchmarks for a "
            "schedule review.",
            "See our guide to [float and slack](/project-management/float-and-slack/) to understand why distorted float misleads decisions.",
        ),
        S(
            "Leads, lags and schedule compression",
            "When a project is running late, removing lags and adding leads are among the first options people look at. "
            "They belong to two different categories:",
            L(
                "**Adding a lead** (or converting FS links into overlapping SS links) is a form of "
                "[fast tracking](/project-management/fast-tracking-vs-crashing/): doing in parallel what was planned in "
                "sequence. It costs little up front but increases rework risk.",
                "**Removing or shortening a lag** is only valid if the lag was not genuine in the first place, or if you can "
                "change the underlying condition, for example using a faster-curing material or agreeing a shorter "
                "review period with a regulator. Simply deleting a curing lag does not make concrete cure faster.",
                "**Crashing**, adding resources to shorten activities, does not change leads or lags at all, because they use no resources.",
            ),
            "Only compress activities and links on the critical path; shortening a lag on a path with float saves nothing. "
            "Our guide to [schedule compression](/project-management/schedule-compression/) walks through the options "
            "in order of cost and risk.",
            "See our guide to [fast tracking vs crashing](/project-management/fast-tracking-vs-crashing/) to choose between the two techniques.",
        ),
        S(
            "Leads and lags in the PMBOK Guide and exams",
            "Earlier, process-based editions of the [PMBOK Guide](/project-management/pmbok-guide/), such as the 6th "
            "edition, listed leads and lags as a tool and technique in the Sequence Activities and Develop Schedule "
            "processes. The current 8th edition, published in November 2025, is organised around 6 principles and 7 "
            "performance domains rather than detailed processes, but leads and lags remain standard scheduling "
            "vocabulary.",
            "For the [PMP certification](/project-management/pmp-certification/), whose exam content outline was updated "
            "in July 2026, scheduling questions sit mainly in the Process domain (41% of the exam). Expect to:",
            L(
                "Tell a lead from a lag and recognise that a lead is a negative lag.",
                "Calculate early and late dates on a network that includes lags.",
                "Distinguish lag (an input) from float (a calculated result).",
                "Recognise that applying a lead is fast tracking and carries rework risk.",
            ),
            "Our [project time management](/project-management/project-time-management/) guide puts leads and lags in the "
            "wider context of planning, estimating and controlling the schedule.",
        ),
        S(
            "Common mistakes with leads and lags",
            L(
                "**Using lags to represent work**, such as a supplier's manufacturing time or a client's review. Model it "
                "as an activity so it can be owned, tracked and reported.",
                "**Hiding contingency inside lags.** The buffer becomes invisible and is never released. Use a visible "
                "buffer or a [contingency plan](/project-management/contingency-plan/) instead.",
                "**Using a lag to hit a date.** If a start is fixed by an external date, use a date constraint or a "
                "[milestone](/project-management/project-milestones/).",
                "**Large leads** that make the logic hard to follow or produce out-of-sequence results. Split the predecessor instead.",
                "**Forgetting the unit.** Working days and calendar days give different dates, especially around weekends and holidays.",
                "**Not documenting the reason.** Six months later nobody remembers why there is a 10-day gap, and it is either "
                "wrongly removed or wrongly kept.",
                "**Ignoring leads and lags in progress updates.** A lead assumes partial output will exist by a certain date; "
                "if the predecessor is late, the lead may no longer be valid.",
                "**Confusing lag with float**, for example \"using up\" lag as if it were spare time. Lag is a requirement; float is flexibility.",
                "**Changing leads and lags after baselining without change control**, which makes "
                "[schedule variance](/project-management/schedule-variance/) against the "
                "[project baseline](/project-management/project-baseline/) meaningless.",
            ),
            TIP("Add a notes column to your schedule and write the reason and unit for every lead and lag, for example "
                "\"FS+3ed: slab curing per structural engineer\". It takes seconds and makes every later review faster."),
        ),
    ],
    faq=[
        ("What is a lag in project management?",
         "A lag is a planned delay between a predecessor and its successor, such as FS+3 days to let concrete cure. It "
         "is waiting time on the link, not work."),
        ("What is a lead in project management?",
         "A lead is the amount of time a successor can start before its predecessor finishes, so the two overlap. It is "
         "usually written as a negative lag, such as FS-2 days."),
        ("Is a lead the same as a negative lag?",
         "Yes. Most scheduling tools have a single Lag field and record a lead as a negative value."),
        ("Do lags use resources?",
         "No. A lag is waiting time with no resources or cost. If people or suppliers do something during that time, "
         "create an activity instead."),
        ("Are leads and lags on the critical path?",
         "They can be. A lag on a critical link adds directly to the project duration, and a lead on a critical link "
         "shortens it. Leads and lags on paths with float do not change the end date until the float is used up."),
        ("When should I use a lead?",
         "When the successor can safely start on partial output from the predecessor, usually to shorten the schedule. "
         "Check the rework risk first, and consider splitting the predecessor instead."),
        ("What is an example of lag time?",
         "Waiting 3 days after pouring concrete before building on it, waiting for paint or plaster to dry, or waiting "
         "for a statutory consultation period to close after sending a notice."),
        ("Is lag the same as float?",
         "No. Lag is a planned delay you put into a link; [float](/project-management/float-and-slack/) is flexibility "
         "calculated from the schedule. A lag can reduce the float of other activities."),
        ("Is lead time the same as a lead?",
         "No. In supply chains and Lean, lead time is the time from order or request to delivery. A schedule lead is an "
         "overlap between two linked activities."),
        ("Can lags be in calendar days?",
         "Yes. Many tools let you specify elapsed (calendar) days for lags such as drying or curing, which continue over "
         "weekends and holidays."),
        ("Do leads increase risk?",
         "Usually, yes. The successor starts with incomplete information and may need rework if the predecessor's output changes."),
        ("How do you add lead or lag time in MS Project?",
         "Open Task Information for the successor, go to the Predecessors tab and type a value in the Lag column: a "
         "positive number or percentage for lag, or a negative number or percentage for lead."),
        ("How many lags are acceptable in a schedule?",
         "There is no universal rule, but the DCMA 14-point assessment uses a benchmark of lags on no more than 5% of "
         "relationships and no leads at all. Every lag should have a documented reason."),
    ],
)
