from core import S, L, OL, T, TIP, H3

URL = "/project-management/forward-and-backward-pass/"

RW = dict(
    title="Forward and Backward Pass: Step-by-Step Worked Example",
    desc="Forward and backward pass explained step by step: formulas, day 0 vs day 1, a full worked example, lags, SS and FF links, deadlines and negative float.",
    intro=(
        "The forward and backward pass are the two calculations at the heart of the "
        "[critical path method](/project-management/critical-path-method/): the forward pass works from start to "
        "finish to find each activity's earliest start and finish dates, and the backward pass works from finish to "
        "start to find the latest dates. The gap between the two is the float, and activities with zero float form "
        "the critical path. This guide gives the formulas, three fully worked examples and a checklist for "
        "checking your answer."
    ),
    takeaways=[
        "Forward pass: EF = ES + duration, and at a merge point take the largest EF of the predecessors.",
        "Backward pass: LS = LF - duration, and at a burst point take the smallest LS of the successors.",
        "Total float = LS - ES = LF - EF; activities with zero total float form the critical path.",
        "Day 0 and day 1 conventions give different dates but the same float and critical path; never mix them.",
        "Start the backward pass from a required date, not the calculated finish, to reveal project float or negative float.",
        "Lags and SS, FF or SF links change the formulas: always apply the lag to the date the link refers to.",
    ],
    sections=[
        S(
            "What is the forward and backward pass?",
            "The **forward pass** is a calculation that moves through a project network from the first activity to "
            "the last, finding each activity's early start (ES) and early finish (EF). The **backward pass** moves "
            "from the last activity to the first, finding each activity's late finish (LF) and late start (LS). "
            "Together they give the project duration, the float of every activity and the critical path.",
            "Both passes need the same inputs: a list of activities, a duration for each and the "
            "[task dependencies](/project-management/task-dependencies/) between them. The terms you will meet:",
            T(
                ["Term", "Abbreviation", "Meaning"],
                ["Early start", "ES", "The earliest an activity can start, once its predecessors allow it"],
                ["Early finish", "EF", "The earliest it can finish: ES + duration"],
                ["Late finish", "LF", "The latest it can finish without delaying the project finish (or a required date)"],
                ["Late start", "LS", "The latest it can start without delaying the project: LF - duration"],
                ["Total float", "TF", "How long it can slip without delaying the project: LS - ES"],
                ["Free float", "FF", "How long it can slip without delaying any successor"],
                ["Merge point", "", "An activity with two or more predecessors; matters in the forward pass"],
                ["Burst point", "", "An activity with two or more successors; matters in the backward pass"],
            ),
            "On an activity-on-node diagram, each box usually shows ES, duration and EF along the top and LS, total "
            "float and LF along the bottom. Our guide to the "
            "[project network diagram](/project-management/project-network-diagram/) shows the layout.",
        ),
        S(
            "Forward and backward pass formulas",
            "This guide uses the **day-0 convention**: the first activity starts at time 0, and a successor starts "
            "at the same number as its predecessor's finish. Read the numbers as the end of a day: EF 3 means the end of "
            "day 3, so a successor with ES 3 starts on day 4.",
            T(
                ["Pass", "Formula", "Rule when there are several links"],
                ["Forward", "EF = ES + duration", "ES = the **largest** EF of all predecessors (plus any lag)"],
                ["Backward", "LS = LF - duration", "LF = the **smallest** LS of all successors (minus any lag)"],
                ["Float", "Total float = LS - ES = LF - EF", "Free float = smallest ES of successors - EF"],
                ["Start and end", "ES of the first activity = 0", "LF of the last activity = project EF, or a required finish date"],
            ),
            "An activity cannot start until **all** its predecessors have finished, so the latest one controls it. "
            "And it must finish in time for **every** successor, so the one needed earliest controls it.",
        ),
        S(
            "Day 0 vs day 1 convention",
            "Many textbooks, exam courses and the US GAO Schedule Assessment Guide use a **day-1 convention** "
            "instead, where the first activity starts on day 1 and both start and finish dates refer to whole "
            "working days. The formulas change slightly:",
            T(
                ["", "Day-0 convention", "Day-1 convention"],
                ["First activity ES", "0", "1"],
                ["Early finish", "EF = ES + duration", "EF = ES + duration - 1"],
                ["Successor's ES (FS link)", "ES = predecessor EF", "ES = predecessor EF + 1"],
                ["Late start", "LS = LF - duration", "LS = LF - duration + 1"],
                ["Predecessor's LF (FS link)", "LF = successor LS", "LF = successor LS - 1"],
                ["Total float", "LS - ES", "LS - ES (same result)"],
            ),
            "Under day 1, every ES and LS is one higher than under day 0, while EF and LF stay the same. Float and "
            "the critical path do not change. Day 0 is quicker for hand calculation; day 1 maps more naturally "
            "onto a calendar, because \"starts on day 4\" means the fourth working day. Pick one and use it "
            "consistently: mixing them is the most common source of off-by-one errors.",
        ),
        S(
            "How to do a forward pass step by step",
            OL(
                "**Prepare the inputs.** List every activity with its duration and predecessors. A [work breakdown structure](/project-management/work-breakdown-structure/) is the usual source of the activity list, and your estimates give the durations.",
                "**Order the activities** so that every activity comes after all its predecessors. Drawing the network first makes this easy.",
                "**Set the first activity's ES to 0** (or 1 under the day-1 convention). If there are several start activities, each starts at 0 unless a constraint says otherwise.",
                "**Calculate EF = ES + duration** for that activity.",
                "**Move to the next activity.** If it has one predecessor, its ES is that predecessor's EF. If it has several (a merge point), its ES is the **largest** of their EFs. Add any lag on the link.",
                "**Repeat** until every activity has an ES and EF.",
                "**Read the project duration.** It is the largest EF in the network, normally the EF of the last activity.",
            ),
        ),
        S(
            "How to do a backward pass step by step",
            OL(
                "**Choose the finish point.** Set the LF of the last activity (or activities) to the project EF from the forward pass, or to a required finish date if one has been imposed.",
                "**Calculate LS = LF - duration** for that activity.",
                "**Move backwards to its predecessors.** If an activity has one successor, its LF is that successor's LS. If it has several (a burst point), its LF is the **smallest** of their LSs. Subtract any lag on the link.",
                "**Repeat** until you reach the first activity.",
                "**Check the start.** If you started from the calculated finish, the first activity's LS should be 0. If it is positive or negative, you either used a required date or made an error.",
                "**Calculate float** for every activity: total float = LS - ES, free float = smallest ES of successors - EF.",
                "**Identify the critical path**: the chain of activities with zero total float (or the lowest float, if a required date has been used).",
            ),
        ),
        S(
            "Worked example: the six-activity network",
            "This illustrative network is the same one used in our [float and slack](/project-management/float-and-slack/) "
            "guide, so you can follow the numbers from one guide to the other. Durations are in working days and all "
            "links are finish-to-start with no lag.",
            T(
                ["Activity", "Duration (days)", "Predecessors"],
                ["A", "3", "-"],
                ["B", "4", "A"],
                ["C", "2", "A"],
                ["D", "5", "B"],
                ["E", "3", "C"],
                ["F", "2", "D, E"],
            ),
            H3("Step 1: forward pass"),
            T(
                ["Activity", "Predecessor EFs", "ES", "Working", "EF"],
                ["A", "None (start)", "0", "0 + 3", "3"],
                ["B", "A = 3", "3", "3 + 4", "7"],
                ["C", "A = 3", "3", "3 + 2", "5"],
                ["D", "B = 7", "7", "7 + 5", "12"],
                ["E", "C = 5", "5", "5 + 3", "8"],
                ["F", "D = 12, E = 8: take the largest", "12", "12 + 2", "14"],
            ),
            "F is a merge point: it cannot start until both D and E are finished, so it waits for D on day 12. The "
            "project duration is **14 days**.",
            H3("Step 2: backward pass"),
            T(
                ["Activity", "Successor LSs", "LF", "Working", "LS"],
                ["F", "None (finish)", "14", "14 - 2", "12"],
                ["E", "F = 12", "12", "12 - 3", "9"],
                ["D", "F = 12", "12", "12 - 5", "7"],
                ["C", "E = 9", "9", "9 - 2", "7"],
                ["B", "D = 7", "7", "7 - 4", "3"],
                ["A", "B = 3, C = 7: take the smallest", "3", "3 - 3", "0"],
            ),
            "A is a burst point: it must finish in time for B, which is needed on day 3, even though C could wait "
            "until day 7. A's LS comes out as 0, which confirms the arithmetic.",
            H3("Step 3: float and the critical path"),
            T(
                ["Activity", "ES", "EF", "LS", "LF", "Total float", "Free float"],
                ["A", "0", "3", "0", "3", "0", "0"],
                ["B", "3", "7", "3", "7", "0", "0"],
                ["C", "3", "5", "7", "9", "4", "0"],
                ["D", "7", "12", "7", "12", "0", "0"],
                ["E", "5", "8", "9", "12", "4", "4"],
                ["F", "12", "14", "12", "14", "0", "0"],
            ),
            L(
                "**Critical path: A-B-D-F**, 14 days. Every activity on it has ES = LS and EF = LF.",
                "**C** has 4 days of total float (7 - 3) but no free float (ES of E 5 - EF of C 5 = 0): any slip in C pushes E later.",
                "**E** has 4 days of total float (9 - 5) and 4 days of free float (ES of F 12 - EF of E 8), because F does not need it until day 12.",
                "**The 4 days are shared** by C and E. If C uses 3 of them, E has only 1 left.",
            ),
            H3("Step 4: the same network under the day-1 convention"),
            T(
                ["Activity", "ES", "EF", "LS", "LF", "Total float"],
                ["A", "1", "3", "1", "3", "0"],
                ["B", "4", "7", "4", "7", "0"],
                ["C", "4", "5", "8", "9", "4"],
                ["D", "8", "12", "8", "12", "0"],
                ["E", "6", "8", "10", "12", "4"],
                ["F", "13", "14", "13", "14", "0"],
            ),
            "Every start is one day later, every finish is identical, and the float is unchanged.",
            H3("Step 5: check your answer"),
            L(
                "The first activity's LS is 0 (day 0) or 1 (day 1) when the backward pass starts from the calculated finish.",
                "The last activity's EF equals its LF.",
                "Every critical activity has ES = LS and EF = LF.",
                "No activity has free float greater than its total float.",
                "The critical path length equals the sum of its durations (3 + 4 + 5 + 2 = 14).",
            ),
            "Free template: the [critical path template](/templates/critical-path-template/) does these calculations "
            "for you in Google Sheets or Excel.",
        ),
        S(
            "Backward pass from a required finish date",
            "So far the backward pass started from the calculated finish (day 14). In practice a sponsor, customer "
            "or contract often sets a required date. Start the backward pass from that date instead, and every late "
            "date moves by the difference.",
            H3("Required finish on day 16"),
            "Set LF of F = 16 and repeat the backward pass. Every LS and LF rises by 2:",
            T(
                ["Activity", "ES", "LS", "LF", "Total float"],
                ["A", "0", "2", "5", "2"],
                ["B", "3", "5", "9", "2"],
                ["C", "3", "9", "11", "6"],
                ["D", "7", "9", "14", "2"],
                ["E", "5", "11", "14", "6"],
                ["F", "12", "14", "16", "2"],
            ),
            "The critical path is still A-B-D-F, but it now has 2 days of float: the project float between the "
            "calculated finish (14) and the required date (16). The critical path is now the path with the "
            "**lowest** float, not zero float.",
            H3("Required finish on day 12"),
            "Now set LF of F = 12, two days earlier than the network can achieve:",
            T(
                ["Activity", "ES", "LS", "LF", "Total float"],
                ["A", "0", "-2", "1", "-2"],
                ["B", "3", "1", "5", "-2"],
                ["C", "3", "5", "7", "2"],
                ["D", "7", "5", "10", "-2"],
                ["E", "5", "7", "10", "2"],
                ["F", "12", "10", "12", "-2"],
            ),
            "A late start of -2 means A should have started two days before the project began, which is "
            "impossible. The negative float is not a mistake: it tells you that the plan, as it stands, misses the "
            "date by 2 days, and that the time must be recovered on A-B-D-F. The C-E path still has 2 days of "
            "float, so shortening C or E would not help.",
            "To recover the 2 days you can crash a critical activity, overlap activities, reduce scope or agree a "
            "new date. See our guide to [schedule compression](/project-management/schedule-compression/) for a "
            "step-by-step method.",
        ),
        S(
            "Forward and backward pass with leads and lags",
            "A **lag** is a delay added to a link; a **lead** is an overlap, written as a negative lag. Both enter "
            "the calculation on the link itself, not on the activity duration. For a finish-to-start link:",
            L(
                "**Forward pass:** ES of successor = EF of predecessor + lag (a lead is a negative lag).",
                "**Backward pass:** LF of predecessor = LS of successor - lag.",
                "**Free float:** ES of successor - lag - EF of predecessor.",
            ),
            H3("Example: a 3-day lag between E and F"),
            "Suppose E is pouring a concrete base and F cannot start until it has cured for 3 days (E to F, FS+3). "
            "In the forward pass, E's link now gives F an ES of 8 + 3 = 11. D still gives 12, so F starts on 12 "
            "and the project still takes 14 days. In the backward pass, E's LF = LS of F (12) - 3 = 9.",
            T(
                ["Activity", "ES", "EF", "LS", "LF", "Total float without lag", "Total float with lag"],
                ["C", "3", "5", "4", "6", "4", "1"],
                ["E", "5", "8", "6", "9", "4", "1"],
            ),
            "The critical path is unchanged, but the lag has used 3 of the 4 days of float on C-E.",
            H3("Example: a 2-day lead between D and F"),
            "Now suppose F can start 2 days before D finishes (D to F, FS-2). F's ES = max(12 - 2, 8) = 10, so F "
            "finishes on day 12 and the project shortens from 14 to 12 days. A-B-D-F is still critical, and C-E's "
            "float falls from 4 to 2. Using leads in this way is the basis of "
            "[fast tracking](/project-management/fast-tracking-vs-crashing/), and it carries rework risk.",
            "Read our guide to [leads and lags](/project-management/leads-and-lags/) for when each is justified and how to record them.",
        ),
        S(
            "SS, FF and SF relationships",
            "Finish-to-start is the most common link, but networks built with the precedence diagramming method can "
            "use all four types. The rule is always the same: apply the lag to the date the link refers to.",
            T(
                ["Link", "Forward pass (successor)", "Backward pass (predecessor)"],
                ["Finish-to-start (FS)", "ES ≥ EF of predecessor + lag", "LF ≤ LS of successor - lag"],
                ["Start-to-start (SS)", "ES ≥ ES of predecessor + lag", "LS ≤ LS of successor - lag, then LF = LS + duration"],
                ["Finish-to-finish (FF)", "EF ≥ EF of predecessor + lag, then ES = EF - duration", "LF ≤ LF of successor - lag"],
                ["Start-to-finish (SF)", "EF ≥ ES of predecessor + lag, then ES = EF - duration", "LS ≤ LF of successor - lag, then LF = LS + duration"],
            ),
            "When an activity has several incoming links, work out the date each link implies and take the latest "
            "(forward pass). When it has several outgoing links, work out each implied late date and take the "
            "earliest (backward pass). The link that sets the date is called the **driving** relationship.",
            H3("Worked example: an office fit-out"),
            "This illustrative network for an office fit-out uses an SS link, an FF link and an FS link with a "
            "drying lag. Durations are in working days.",
            T(
                ["ID", "Activity", "Duration", "Links from predecessors"],
                ["A", "Strip-out", "4", "-"],
                ["B", "Build partition walls", "6", "A (FS)"],
                ["C", "Electrical first fix", "3", "B (SS+2) and B (FF+1)"],
                ["D", "Plastering", "4", "B (FS), C (FS)"],
                ["E", "Painting", "3", "D (FS+2, drying)"],
                ["F", "Order and deliver furniture", "10", "A (FS)"],
                ["G", "Install furniture", "2", "E (FS), F (FS)"],
                ["H", "Handover", "1", "G (FS)"],
            ),
            "The electricians can start 2 days after the partitions start (SS+2), but cannot finish until a day "
            "after the partitions are complete (FF+1).",
            "**Forward pass:**",
            L(
                "A: ES 0, EF 4. B: ES 4, EF 10. F: ES 4, EF 14.",
                "C: the SS+2 link gives ES ≥ 4 + 2 = 6. The FF+1 link gives EF ≥ 10 + 1 = 11, so ES ≥ 11 - 3 = 8. Take the later: **ES 8, EF 11**. The FF link is driving.",
                "D: predecessors B (EF 10) and C (EF 11), so ES 11, EF 15.",
                "E: ES = 15 + 2 = 17, EF 20.",
                "G: predecessors E (EF 20) and F (EF 14), so ES 20, EF 22.",
                "H: ES 22, EF 23. The project takes **23 days**.",
            ),
            "**Backward pass:**",
            L(
                "H: LF 23, LS 22. G: LF 22, LS 20.",
                "E: LF 20, LS 17. F: LF 20, LS 10.",
                "D: LF = LS of E - 2 = 15, LS 11.",
                "C: LF = LS of D = 11, LS 8.",
                "B has three outgoing links. To D (FS): LF ≤ 11. To C (SS+2): LS ≤ 8 - 2 = 6, so LF ≤ 12. To C (FF+1): LF ≤ 11 - 1 = 10. Take the earliest: **LF 10, LS 4**.",
                "A: successors B (LS 4) and F (LS 10), so LF 4, LS 0.",
            ),
            T(
                ["ID", "ES", "EF", "LS", "LF", "Total float", "Free float"],
                ["A", "0", "4", "0", "4", "0", "0"],
                ["B", "4", "10", "4", "10", "0", "0"],
                ["C", "8", "11", "8", "11", "0", "0"],
                ["D", "11", "15", "11", "15", "0", "0"],
                ["E", "17", "20", "17", "20", "0", "0"],
                ["F", "4", "14", "10", "20", "6", "6"],
                ["G", "20", "22", "20", "22", "0", "0"],
                ["H", "22", "23", "22", "23", "0", "0"],
            ),
            "The critical path is A-B-C-D-E-G-H, and it runs through the FF link and the drying lag. Furniture (F) "
            "has 6 days of float. **What if the supplier quotes 17 days instead of 10?** F would finish on day 21, "
            "G would start on 21 and the project would take 24 days. The critical path would switch to A-F-G-H, "
            "and the fit-out work (B, C, D and E) would gain 1 day of float.",
        ),
        S(
            "Forward pass vs backward pass",
            T(
                ["", "Forward pass", "Backward pass"],
                ["Direction", "Start to finish", "Finish to start"],
                ["Calculates", "Early start and early finish", "Late finish and late start"],
                ["Starting value", "ES of first activity = 0 (or 1)", "LF of last activity = project EF or a required date"],
                ["Rule at junctions", "Largest EF at a merge point", "Smallest LS at a burst point"],
                ["Answers", "How soon can we finish?", "How late can each activity be without delaying the finish?"],
            ),
        ),
        S(
            "Real-world complications",
            "Textbook networks have one start, one finish and only finish-to-start links. Real schedules add a few "
            "complications that change how the passes behave:",
            L(
                "**Date constraints.** A \"start no earlier than\" constraint can push an ES later in the forward "
                "pass; a \"finish no later than\" constraint can pull an LF earlier in the backward pass and create "
                "negative float. Use logic wherever you can and keep constraints to genuine external dates.",
                "**Calendars.** Software counts working time on each activity's calendar, so a 5-day activity that "
                "spans a weekend or holiday takes longer in calendar days. Activities on different calendars, such "
                "as a 7-day calendar for curing, can make float look uneven along a path.",
                "**Open ends.** An activity with no successor gets its LF from the project finish, which gives it "
                "inflated float. Every activity except the last should have a successor.",
                "**Progress.** Once work has started, the forward pass for remaining work begins from the status "
                "(data) date rather than day 0, using actual dates for completed work and remaining durations for "
                "work in progress.",
                "**Uncertain durations.** The passes treat every duration as fixed. For a range of outcomes, use "
                "three-point estimates with a [PERT chart](/project-management/pert-chart/) or a "
                "[Monte Carlo simulation](/project-management/monte-carlo-simulation/).",
                "**Resources.** The passes assume unlimited resources; "
                "[resource levelling](/project-management/resource-leveling/) can move work and change the critical path.",
            ),
        ),
        S(
            "Forward and backward pass in scheduling software",
            "Scheduling software recalculates both passes every time a date, duration or link changes. Knowing the "
            "method lets you check and explain the output.",
            L(
                "**Microsoft Project** runs both passes automatically and shows the results as Early Start, Early "
                "Finish, Late Start, Late Finish, Free Slack and Total Slack fields. You can schedule from the project "
                "start date (the usual forward approach) or from a finish date.",
                "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool, highlights the critical path in "
                "its interactive [Gantt charts](/project-management/gantt-chart/) from the Team plan upwards, with all "
                "four dependency types and lead and lag time.",
                "**[ClickUp](/project-management-tools/clickup/)** Gantt charts support all four dependency types and "
                "show the critical path and slack time, rescheduling downstream tasks automatically.",
                "**[Smartsheet](/project-management-tools/smartsheet/)** combines a grid with Gantt dependencies and "
                "can identify the critical path, which suits date-driven projects.",
                "**Spreadsheets** work for small networks. Our [project schedule template](/templates/project-schedule-template/) "
                "and [Gantt chart template](/templates/gantt-chart-template/) are good starting points.",
            ),
            "Whatever the tool, save a [project baseline](/project-management/project-baseline/) once the schedule "
            "is approved, so you can compare later passes against it.",
        ),
        S(
            "Common mistakes",
            L(
                "**Taking the smallest EF at a merge point** in the forward pass. Always take the largest.",
                "**Taking the largest LS at a burst point** in the backward pass. Always take the smallest.",
                "**Mixing day-0 and day-1 formulas** in the same calculation.",
                "**Forgetting lags**, or applying an SS or FF lag to the wrong date.",
                "**Starting the backward pass from the wrong date.** Use the calculated finish or the required date, and say which.",
                "**Reading the critical path off durations alone.** In networks with lags, constraints or SS and FF links, the longest-looking chain of durations may not be critical; trust the float.",
                "**Not recalculating after a change.** A new duration, link or deadline can switch the critical path.",
            ),
            "Read our guide to the [critical path method](/project-management/critical-path-method/) to see how the passes fit into the full scheduling process.",
        ),
    ],
    faq=[
        ("What is a forward pass in project management?",
         "A calculation from the start of the network to the end that finds each activity's early start and early "
         "finish, and so the shortest possible project duration."),
        ("What is a backward pass?",
         "A calculation from the end of the network to the start that finds each activity's late finish and late "
         "start, which shows how much each activity can slip."),
        ("Why take the largest EF in a forward pass?",
         "Because an activity cannot start until all its predecessors have finished, so the latest-finishing one "
         "controls its start."),
        ("Why take the smallest LS in a backward pass?",
         "Because an activity must finish in time for every successor, so the successor needed earliest controls "
         "its late finish."),
        ("Should the forward pass start at day 0 or day 1?",
         "Either, if you are consistent. Day 0 is simpler for hand calculation; day 1 matches calendar days more "
         "naturally. Float and the critical path are the same either way."),
        ("How do you calculate float from the forward and backward pass?",
         "Total float = LS - ES, or LF - EF. Free float = the smallest ES of the activity's successors minus its own "
         "EF, allowing for any lag."),
        ("Which comes first, the forward or backward pass?",
         "The forward pass, because the backward pass normally starts from the project finish it calculates. The "
         "exception is when you start the backward pass from an imposed date."),
        ("What if the required finish date is earlier than the forward pass finish?",
         "Start the backward pass from the required date. Critical activities will show negative float equal to the "
         "time that must be recovered."),
        ("Do I need to do the forward and backward pass by hand?",
         "Scheduling software does it automatically, but working a small network by hand helps you understand and "
         "check the results, and it is a common exam topic."),
        ("Is the forward and backward pass on the PMP exam?",
         "Network calculations such as float and the critical path are commonly covered in PMP preparation. See our "
         "[PMP certification guide](/project-management/pmp-certification/) for the current exam content."),
        ("Is this the same as the forward and backward pass in neural networks?",
         "No. In machine learning the terms describe computing a network's output and its gradients. In project "
         "management they are schedule calculations."),
    ],
)
