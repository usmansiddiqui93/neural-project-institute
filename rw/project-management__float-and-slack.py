from core import S, L, OL, T, TIP, H3

URL = "/project-management/float-and-slack/"

RW = dict(
    title="Float and Slack in Project Management: Types and Formulas",
    desc="Float and slack in project management explained: total, free, project and negative float, formulas, a step-by-step worked example and how to manage float.",
    intro=(
        "Float in project management, also called slack, is the amount of time an activity can be delayed without "
        "delaying something else: its successors (free float) or the project finish date (total float). Activities "
        "with zero total float form the critical path. This guide gives the formulas for every type of float, two "
        "fully worked examples and practical rules for managing float on a live schedule."
    ),
    takeaways=[
        "Float and slack mean the same thing: how long an activity can slip before it causes a delay.",
        "Total float = LS - ES (or LF - EF) and protects the project finish; free float = earliest ES of successors - EF and protects the next activity.",
        "Float is shared along a path, so using it early leaves less for activities later on the same path.",
        "Negative float means the schedule cannot meet a required date; its size is the time you must recover.",
        "Unusually high float usually signals missing logic, not genuine flexibility.",
        "Agree who owns float before the project starts; contracts and standards take different positions.",
    ],
    sections=[
        S(
            "What is float in project management?",
            "**Float**, or **slack**, is the amount of time a schedule activity can be delayed without delaying "
            "either the early start of its successors (free float) or the project finish date (total float). It is "
            "calculated from the network of activities, durations and dependencies. Activities with zero total float "
            "are critical: any delay to them delays the project.",
            "Three points follow from that definition:",
            L(
                "**Float is calculated, not entered.** It comes out of the "
                "[forward and backward pass](/project-management/forward-and-backward-pass/) once you have activities, "
                "durations and [task dependencies](/project-management/task-dependencies/). If the logic is wrong, the "
                "float is wrong.",
                "**Float belongs to a path, not just an activity.** Two activities in a chain often show the same total "
                "float because they share it. Use it on the first and the second has less.",
                "**Float changes every time the schedule is updated.** Progress, delays, new dependencies and changed "
                "deadlines all move it.",
            ),
            "Float is what tells you where you have room to manoeuvre and where you have none. It is the basis of the "
            "[critical path method](/project-management/critical-path-method/), resource levelling and most schedule "
            "recovery decisions.",
        ),
        S(
            "Float vs slack: is there a difference?",
            "No. In scheduling, float and slack are interchangeable terms for the same calculation. The choice of word "
            "is mostly a matter of tradition and software:",
            T(
                ["Where you see it", "Term usually used"],
                ["PMI publications and PMP exam material", "Float (total float, free float)"],
                ["PERT literature", "Slack"],
                ["Microsoft Project", "Slack (Total Slack and Free Slack fields)"],
                ["Construction and engineering planning tools", "Float"],
                ["Some Gantt chart tools, such as ClickUp", "Slack time"],
            ),
            "Do not confuse schedule slack with the general idea of spare capacity, or with the Slack messaging app. "
            "Slack in this guide always means scheduling float.",
        ),
        S(
            "Types of float",
            T(
                ["Type", "What it measures", "Formula"],
                ["Total float", "How long an activity can slip without delaying the project finish (or a constraint)", "LS - ES, or LF - EF"],
                ["Free float", "How long an activity can slip without delaying the early start of any successor", "Earliest ES of successors - EF"],
                ["Project float", "How much the whole project can slip before missing an imposed deadline", "Required finish - calculated early finish"],
                ["Negative float", "How far the schedule is behind a required date or constraint", "Total float below zero"],
                ["Independent float", "Slip available even if predecessors finish late and successors start early", "Earliest ES of successors - latest LF of predecessors - duration (if positive)"],
                ["Interfering float", "The part of total float that, if used, takes float away from successors", "Total float - free float"],
            ),
            H3("Total float"),
            "Total float is the figure most people mean when they say \"float\". It is measured against the project "
            "finish, or against a date constraint if one applies. Zero total float marks the critical path. Total "
            "float is shared by all activities on the same chain of non-critical work.",
            H3("Free float"),
            "Free float is more local. It tells you how long an activity can slip before the next team or activity is "
            "affected. Only the last activity in a chain of non-critical work usually has free float; the earlier ones "
            "pass any slip straight to their successors. Free float is always less than or equal to total float.",
            H3("Project float"),
            "Project float compares the calculated finish with an imposed deadline from the sponsor, customer or "
            "contract. If the network finishes on day 27 and the contract requires day 30, the project has 3 days of "
            "project float. Some planners call this terminal float, particularly in construction contracts.",
            H3("Independent and interfering float"),
            "These two are mainly used in exam questions and detailed schedule analysis. **Independent float** is the "
            "most conservative measure: the slip an activity can absorb even in the worst case, when its predecessors "
            "finish as late as possible and its successors need to start as early as possible. **Interfering float** "
            "is the part of total float that is not free float, so using it interferes with the float of later "
            "activities.",
        ),
        S(
            "Float formulas at a glance",
            T(
                ["Measure", "Formula", "Notes"],
                ["Early finish", "EF = ES + duration", "Forward pass"],
                ["Early start", "ES = largest EF of all predecessors", "Add any lag; subtract any lead"],
                ["Late start", "LS = LF - duration", "Backward pass"],
                ["Late finish", "LF = smallest LS of all successors", "Allow for lags on the links"],
                ["Total float", "TF = LS - ES = LF - EF", "Both give the same answer"],
                ["Free float", "FF = min(ES of successors) - EF", "Subtract any lag on the link"],
                ["Interfering float", "IF = TF - FF", ""],
                ["Project float", "Required finish - project EF", "Negative if the deadline is earlier"],
            ),
            "This guide uses the day-0 convention: the first activity starts at 0 and each successor starts at its "
            "predecessor's early finish. Some textbooks use a day-1 convention where ES = previous EF + 1. The float "
            "values and the critical path are the same either way, so stick to one convention throughout. If your "
            "network uses [leads and lags](/project-management/leads-and-lags/), include them in every calculation: a "
            "3-day lag on a link reduces the free float of the predecessor by 3 days.",
        ),
        S(
            "How to calculate float step by step",
            OL(
                "**List the activities** with durations and predecessors. A [work breakdown structure](/project-management/work-breakdown-structure/) is the usual source.",
                "**Draw the network** so every activity, except the start and finish, has at least one predecessor and one successor. See our guide to the [project network diagram](/project-management/project-network-diagram/).",
                "**Forward pass.** Work from left to right: ES = largest EF of predecessors, EF = ES + duration. The largest EF is the project duration.",
                "**Backward pass.** Work from right to left: LF of the last activity = project finish (or the required date), LS = LF - duration, and LF of other activities = smallest LS of successors.",
                "**Total float** for each activity: LS - ES.",
                "**Free float** for each activity: earliest ES of its successors - its EF.",
                "**Identify the critical path**: the chain of activities with zero total float (or the lowest float, if it is negative).",
                "**Sanity-check the results.** Look for activities with surprisingly high float; they often have a missing successor.",
            ),
            "Free template: the [critical path template](/templates/critical-path-template/) calculates early and late "
            "dates, float and the critical path for you, in Google Sheets, Excel and PDF.",
        ),
        S(
            "Worked example 1: the six-activity network",
            "This illustrative network is the same one used in our [forward and backward pass](/project-management/forward-and-backward-pass/) "
            "guide, so you can follow the calculation from start to finish.",
            T(
                ["Activity", "Duration (days)", "Predecessors"],
                ["A", "3", "-"],
                ["B", "4", "A"],
                ["C", "2", "A"],
                ["D", "5", "B"],
                ["E", "3", "C"],
                ["F", "2", "D, E"],
            ),
            "The forward and backward passes give these dates and floats:",
            T(
                ["Activity", "ES", "EF", "LS", "LF", "Total float", "Free float", "Interfering float"],
                ["A", "0", "3", "0", "3", "0", "0", "0"],
                ["B", "3", "7", "3", "7", "0", "0", "0"],
                ["C", "3", "5", "7", "9", "4", "0", "4"],
                ["D", "7", "12", "7", "12", "0", "0", "0"],
                ["E", "5", "8", "9", "12", "4", "4", "0"],
                ["F", "12", "14", "12", "14", "0", "0", "0"],
            ),
            L(
                "**Critical path:** A-B-D-F, 14 days. Every activity on it has zero total float.",
                "**C:** total float 7 - 3 = 4 days. Free float = ES of E (5) - EF of C (5) = 0, so any slip in C pushes E.",
                "**E:** total float 9 - 5 = 4 days. Free float = ES of F (12) - EF of E (8) = 4 days.",
                "**Shared float:** the 4 days belong to the path C-E. If C slips 3 days, E has only 1 day left.",
                "**Independent float** of C = ES of E (5) - LF of A (3) - 2 = 0, and of E = ES of F (12) - LF of C (9) - 3 = 0.",
                "**Project float:** if the sponsor requires completion by day 16, project float is 16 - 14 = 2 days. If the deadline is day 12, the critical activities have -2 days of float.",
            ),
            "See our guide to the [forward and backward pass](/project-management/forward-and-backward-pass/) for each step of the date calculation.",
        ),
        S(
            "Worked example 2: a website relaunch",
            "This larger illustrative example shows how float behaves when things change. A marketing team is "
            "relaunching its website. Durations are in working days.",
            T(
                ["ID", "Activity", "Duration", "Predecessors"],
                ["A", "Requirements and kick-off", "4", "-"],
                ["B", "Visual design", "6", "A"],
                ["C", "Content writing", "7", "A"],
                ["D", "Content sign-off", "2", "C"],
                ["E", "Front-end build", "8", "B"],
                ["F", "Back-end integration", "10", "A"],
                ["G", "Content load", "3", "D, E"],
                ["H", "Testing", "5", "F, G"],
                ["I", "Launch", "1", "H"],
            ),
            H3("Step 1: calculate dates and float"),
            T(
                ["ID", "ES", "EF", "LS", "LF", "Total float", "Free float"],
                ["A", "0", "4", "0", "4", "0", "0"],
                ["B", "4", "10", "4", "10", "0", "0"],
                ["C", "4", "11", "9", "16", "5", "0"],
                ["D", "11", "13", "16", "18", "5", "5"],
                ["E", "10", "18", "10", "18", "0", "0"],
                ["F", "4", "14", "11", "21", "7", "7"],
                ["G", "18", "21", "18", "21", "0", "0"],
                ["H", "21", "26", "21", "26", "0", "0"],
                ["I", "26", "27", "26", "27", "0", "0"],
            ),
            "The critical path is A-B-E-G-H-I (4 + 6 + 8 + 3 + 5 + 1 = 27 days). The content path C-D shares 5 days "
            "of float, and back-end integration (F) has 7 days, all of it free float. If the sponsor's launch date is "
            "day 30, the project has 3 days of project float.",
            H3("Step 2: content writing slips 3 days"),
            "The copywriter is ill and C takes 10 days instead of 7. C now finishes on day 14 and D on day 16. G "
            "cannot start until E finishes on day 18 anyway, so the launch date does not move. But the C-D path now "
            "has only 2 days of float left, and D's free float has dropped from 5 to 2. Tell the content team: one "
            "more slip of 3 days and the launch moves.",
            H3("Step 3: content writing slips 6 days"),
            "Suppose instead C takes 13 days. It finishes on day 17, D on day 19, and G cannot start until day 19. "
            "The project now finishes on day 28, one day later than planned. The critical path has switched to "
            "A-C-D-G-H-I, and the old critical activities B and E now have 1 day of float. This is why near-critical "
            "paths need watching: a path with 5 days of float can become critical after a single bad week.",
            H3("Step 4: the deadline moves to day 25"),
            "Back to the original plan. Marketing brings the launch forward to day 25 to coincide with an event. Run "
            "the backward pass from day 25 instead of day 27 and every float value falls by 2:",
            T(
                ["Path", "Total float before", "Total float with day-25 deadline"],
                ["A-B-E-G-H-I", "0", "-2"],
                ["C-D", "5", "3"],
                ["F", "7", "5"],
            ),
            "The -2 tells you exactly how much time must be recovered on the critical path.",
            H3("Step 5: recover the time and recheck float"),
            "The team adds a second front-end developer and crashes E from 8 days to 6. Recalculating:",
            L(
                "E now finishes on day 16, G runs from 16 to 19, H from 19 to 24 and I from 24 to 25. The launch meets day 25.",
                "The critical path is still A-B-E-G-H-I, now with zero float.",
                "The C-D path keeps 3 days of float, and F's float has dropped from 7 to 5 days.",
            ),
            "Notice that the recovery used up float elsewhere in the network. Every compression decision should be "
            "followed by a fresh float check, because a parallel path may now be close to critical. See our guide to "
            "[fast tracking vs crashing](/project-management/fast-tracking-vs-crashing/) for the two main recovery techniques and their costs.",
        ),
        S(
            "Negative float: what it means and how to fix it",
            "Negative float appears when the calculated dates are later than a required date or constraint. It is not "
            "an error in the maths: it is the schedule telling you that the plan, as it stands, cannot meet the date. "
            "The size of the negative number is the time you must recover on that path.",
            "Common causes:",
            L(
                "A deadline or \"finish no later than\" constraint earlier than the network can achieve.",
                "Delays on critical activities that have not been offset.",
                "Added scope or new dependencies after the baseline was set.",
                "Over-optimistic durations that are now being corrected with actual progress.",
            ),
            T(
                ["Response", "How it removes negative float", "Trade-off"],
                ["Crashing", "Adds resources to shorten critical activities", "Higher cost; not every task can be shortened"],
                ["Fast tracking", "Overlaps activities that were planned in sequence", "More rework risk"],
                ["Reducing scope", "Removes or defers work on the critical path", "Needs sponsor and customer agreement"],
                ["Changing logic", "Removes dependencies that were preferences, not necessities", "Only valid if the original logic was unnecessary"],
                ["Moving the date", "Agrees a new deadline", "Requires formal [change control](/project-management/change-control/)"],
            ),
            "See [schedule compression](/project-management/schedule-compression/) for a step-by-step method for "
            "choosing between these options. Never hide negative float by deleting links or adding constraints; it "
            "only postpones the conversation.",
        ),
        S(
            "Float and the critical path",
            "The critical path is the longest path through the network, and in a schedule without date constraints its "
            "activities have zero total float. In practice there are a few complications:",
            L(
                "**Constraints and deadlines** can give the critical path negative float, or leave it with positive "
                "float if the deadline is later than the calculated finish. The critical path is then the path with the "
                "lowest float.",
                "**Different calendars** (for example a 5-day calendar for most work and a 7-day calendar for curing) "
                "can make float values on the same path look uneven.",
                "**Near-critical paths** have a small amount of float. Many teams set a threshold, such as 5 or 10 days, "
                "and monitor every path below it as closely as the critical path itself.",
                "**Several critical paths** can exist at once, which makes the schedule riskier: a delay on any of them "
                "delays the project.",
            ),
            "For a schedule with significant uncertainty, a [Monte Carlo simulation](/project-management/monte-carlo-simulation/) "
            "shows how often each activity ends up on the critical path, which is a better guide to risk than a single "
            "float value. The [critical chain](/project-management/critical-chain-project-management/) approach goes "
            "further and replaces activity float with managed buffers.",
        ),
        S(
            "How to manage float on a live project",
            OL(
                "**Recalculate float after every schedule update.** Float from last month's plan is out of date as soon as progress is entered.",
                "**Use free float first.** When you need to delay an activity, choose one with free float, because nobody else is affected.",
                "**Use float to level resources.** [Resource levelling](/project-management/resource-leveling/) moves non-critical work within its float to smooth peaks in demand without moving the end date.",
                "**Protect shared float.** When an early activity in a chain uses float, tell the owners of later activities how much is left.",
                "**Watch near-critical paths.** Report paths below your threshold alongside the critical path.",
                "**Do not treat float as a buffer for estimates.** If an estimate is uncertain, fix the estimate or add an explicit contingency activity or buffer, so the risk is visible.",
                "**Report trends, not just values.** Float that shrinks every week is an early warning even if it is still positive. Compare with the [project baseline](/project-management/project-baseline/).",
            ),
            TIP("A simple float report works well in steering meetings: critical path end date, project float against "
                "the deadline, the three paths with the least float, and how each of those numbers has moved since the "
                "last report."),
        ),
        S(
            "Who owns float?",
            "When a delay uses up float, someone has benefited from it. If the contract or project rules say nothing, "
            "the person who uses it first effectively takes it, which can lead to disputes. Positions vary:",
            T(
                ["Source", "Position on float ownership"],
                ["Common project practice", "Float is a shared project resource, managed by the project manager for the benefit of the project"],
                ["SCL Delay and Disruption Protocol (2nd edition, UK)", "Unless the contract says otherwise, float is not for the exclusive use or benefit of either the employer or the contractor"],
                ["NEC4 contracts", "Extensions of time are assessed against planned completion, so terminal float between planned completion and the completion date is protected, which is why it is often said to belong to the contractor"],
                ["JCT and FIDIC contracts", "Do not expressly define float or its ownership; float generally has to be used up before an extension of time can be claimed"],
            ),
            "The contract positions above follow a 2026 summary by law firm Herbert Smith Freehills Kramer; always "
            "check the exact terms of your own contract and take advice on disputes. Inside an organisation, the "
            "practical answer is to agree the rule at the start, record it in the schedule management plan and make "
            "sure team leads know they cannot spend float without telling the project manager. This matters most in "
            "[construction project management](/project-management/industries/construction-project-management/), "
            "where float often decides who pays for a delay.",
        ),
        S(
            "Checking float as a schedule quality test",
            "Float values are a quick health check on the schedule itself. Two widely used references:",
            L(
                "**GAO Schedule Assessment Guide.** Its best practice on ensuring reasonable total float warns that "
                "unreasonably high total float on an activity or path suggests that schedule logic may be missing or "
                "invalid, and that incomplete logic, unrealistic durations and unstatused work all distort float. It "
                "also expects managers on both the customer and contractor side to manage total float actively as "
                "work is completed.",
                "**DCMA 14-point assessment.** Its high float check flags incomplete activities with total float "
                "greater than 44 working days, with a benchmark that they should not exceed 5% of incomplete "
                "activities. Its negative float check has a threshold of zero: every activity with negative float "
                "should have an explanation and a corrective plan.",
            ),
            "You do not need to work on a government contract to use these tests. Filter your schedule for activities "
            "with very high float and check each one has a real successor; it takes minutes and catches most logic "
            "gaps.",
        ),
        S(
            "Float in scheduling software",
            "You rarely calculate float by hand on a real project. Most scheduling tools do it automatically once "
            "dependencies are in place:",
            L(
                "**Microsoft Project** calls it slack. Switch to the Detail Gantt view and the Schedule table to see "
                "the Free Slack and Total Slack fields. A task with zero slack is critical by default, and you can "
                "change that threshold with the option \"Tasks are critical if slack is less than or equal to\".",
                "**[Wrike](/project-management-tools/wrike/)** (our top-rated tool) shows the critical path and float "
                "in its interactive [Gantt charts](/project-management/gantt-chart/), from the Team plan upwards, "
                "together with all four dependency types, lead and lag time and baselines.",
                "**[ClickUp](/project-management-tools/clickup/)** Gantt charts show the critical path and slack time, "
                "with automatic rescheduling of downstream tasks when a date moves.",
                "**[Microsoft Planner](/project-management-tools/microsoft-planner/)** premium plans include "
                "dependencies, and Plan 3 adds baselines and the critical path.",
                "**Spreadsheets** work for small networks. Our [project schedule template](/templates/project-schedule-template/) "
                "and [Gantt chart template](/templates/gantt-chart-template/) are good starting points.",
            ),
        ),
        S(
            "Common mistakes with float",
            L(
                "**Treating float as spare time.** It is shared along a path and disappears quickly once used.",
                "**Trusting high float without checking logic.** Missing successors inflate float; an activity with 60 "
                "days of float usually has a missing link, not 60 days of freedom.",
                "**Hiding float with constraints.** \"Must start on\" dates and other hard constraints distort float. "
                "Use logic wherever you can.",
                "**Reporting only total float.** Free float shows the immediate impact on the next team.",
                "**Letting teams consume float silently.** Agree who can use float and require a heads-up when they do.",
                "**Ignoring float when assigning people.** A low-priority task with float can take a resource needed "
                "on the critical path.",
                "**Mixing day conventions.** Combining day-0 and day-1 calculations creates off-by-one errors.",
                "**Forgetting lags.** A lag on a link reduces the free float of the predecessor.",
            ),
            "Read our guide to the [critical path method](/project-management/critical-path-method/) to see how float fits into the full scheduling process.",
        ),
    ],
    faq=[
        ("What is float in project management?",
         "The amount of time an activity can be delayed without delaying its successors (free float) or the project "
         "finish date (total float). It is also called slack."),
        ("Is slack the same as float?",
         "Yes. The terms are interchangeable. Slack is more common in PERT literature and Microsoft Project; float is "
         "more common in PMI material and construction planning."),
        ("How do you calculate total float?",
         "Total float = late start - early start, or late finish - early finish. Both give the same answer."),
        ("How do you calculate free float?",
         "Free float = the earliest early start of the activity's successors minus its own early finish, after "
         "allowing for any lags on the links."),
        ("What does zero float mean?",
         "The activity is on the critical path, so any delay to it delays the project finish, unless time is recovered later."),
        ("What is negative float?",
         "Float below zero. It shows that the schedule cannot meet a required date or constraint, and by how much. It "
         "needs recovery through crashing, fast tracking, scope changes or a new agreed date."),
        ("Can free float be greater than total float?",
         "No. Free float is always less than or equal to total float."),
        ("What is project float?",
         "The difference between the project's calculated finish and an imposed deadline. A network finishing on day "
         "27 with a deadline of day 30 has 3 days of project float."),
        ("What is the difference between total float and free float?",
         "Total float protects the project finish date; free float protects the next activity. An activity can have "
         "total float but no free float when it shares float with later activities on the same path."),
        ("Who owns float in a project?",
         "It depends on the contract. Many organisations treat float as a shared project resource. In the UK, the SCL "
         "Delay and Disruption Protocol says float is not for the exclusive benefit of either party unless the "
         "contract says otherwise."),
        ("Does float change during a project?",
         "Yes. As activities finish early or late, or as logic and deadlines change, float is recalculated and can "
         "grow, shrink or become negative."),
        ("What is a good amount of float?",
         "There is no single figure. Low float means risk, and very high float often means missing logic. The DCMA "
         "14-point assessment flags activities with more than 44 working days of total float."),
        ("What is interfering float?",
         "Total float minus free float. It is the part of an activity's float that, if used, reduces the float "
         "available to activities later on the same path."),
    ],
)
