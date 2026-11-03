from core import S, L, OL, T, TIP, H3

URL = "/project-management/pert-chart/"

RW = dict(
    title="PERT Chart: Formula, Steps and Worked Example",
    desc="What a PERT chart is and how to make one: the PERT formula, steps, a full worked example with probability, PERT vs CPM and Gantt, and common pitfalls.",
    intro=(
        "A PERT chart is a network diagram that maps a project's activities and dependencies using the Program "
        "Evaluation and Review Technique, in which each activity gets three duration estimates (optimistic, most "
        "likely and pessimistic). From those you calculate an expected duration, find the critical path and "
        "estimate the probability of finishing by a given date. This guide gives the formulas, the steps and a "
        "complete worked example."
    ),
    takeaways=[
        "PERT expected duration = (O + 4M + P) / 6; standard deviation = (P - O) / 6; variance = SD squared.",
        "Draw the network, run a forward and backward pass on the expected durations, and the zero-float chain is the critical path.",
        "Add variances, not standard deviations, along the critical path, then use z = (deadline - expected finish) / path SD for the probability.",
        "Classic PERT ignores near-critical paths, so it tends to be optimistic where paths merge; check important dates with Monte Carlo simulation.",
        "Use PERT for new or uncertain work and to set schedule contingency; single-point estimates are fine for routine tasks.",
    ],
    sections=[
        S(
            "What is a PERT chart?",
            "A **PERT chart** is a network diagram of a project's activities, the dependencies between them and "
            "their estimated durations, built using the Program Evaluation and Review Technique. Each activity has "
            "three estimates, which PERT combines into an expected duration and a measure of uncertainty, so the "
            "chart shows the likely finish date and how confident you can be in it.",
            "The term is used in two slightly different ways. The **PERT chart** is the picture: boxes or circles "
            "joined by arrows. The **PERT estimate** or PERT analysis is the arithmetic behind it. Most practical "
            "uses combine both, and the chart is a type of "
            "[project network diagram](/project-management/project-network-diagram/).",
            "PERT charts come in two notations:",
            T(
                ["", "Activity on node (AON)", "Activity on arrow (AOA)"],
                ["Activities shown as", "Boxes (nodes)", "Arrows"],
                ["Nodes represent", "The activities themselves", "Events: points in time when activities start or finish"],
                ["Dummy activities", "Not needed", "Sometimes needed to show logic correctly"],
                ["Where you see it", "Modern scheduling software and most textbooks", "Original PERT, exam questions and some engineering fields"],
            ),
            "The original PERT used activity on arrow, with numbered events. Today most people draw activity on "
            "node because it is easier to read and to build in software. The worked example below shows the same "
            "network both ways.",
            H3("How to read a PERT chart node"),
            "On an activity-on-node PERT chart, each box usually carries six numbers around the activity name. "
            "The top row shows the **early start, expected duration and early finish**; the bottom row shows the "
            "**late start, total float and late finish**. Some charts add the standard deviation under the "
            "duration. Read the chart from left to right: arrows show which activities must finish first, the "
            "boxes with zero float form the critical path (often drawn in red or bold), and the last box's early "
            "finish is the expected project duration.",
        ),
        S(
            "A short history of PERT",
            "PERT was developed in 1958 for the US Navy's Polaris submarine missile programme by the Navy's Special "
            "Projects Office, working with Lockheed and the consultancy Booz Allen Hamilton. It was first called "
            "Program Evaluation Research Task and was renamed by 1959. The aim was to coordinate thousands of "
            "contractors on a programme where nobody could estimate durations precisely.",
            "At about the same time, DuPont developed the [critical path method](/project-management/critical-path-method/) "
            "(CPM) for plant maintenance and construction. CPM used a single duration per activity and focused on "
            "time-cost trade-offs; PERT focused on uncertainty. The two ideas merged so thoroughly that many people "
            "now say \"PERT/CPM\" and use the terms almost interchangeably.",
        ),
        S(
            "PERT chart symbols and terms",
            T(
                ["Term", "Meaning"],
                ["Activity (task)", "Work that takes time and uses resources, such as \"build front end\""],
                ["Event", "A point in time that marks the start or finish of activities; uses no time or resources (AOA charts)"],
                ["Milestone", "A significant event, such as \"testing complete\"; see [project milestones](/project-management/project-milestones/)"],
                ["Dependency", "A logical link: one activity must finish before another starts; see [task dependencies](/project-management/task-dependencies/)"],
                ["Dummy activity", "A dashed arrow with zero duration, used in AOA charts to show a dependency without adding work"],
                ["Optimistic (O)", "The shortest realistic duration if things go well"],
                ["Most likely (M)", "The duration you expect under normal conditions"],
                ["Pessimistic (P)", "The longest realistic duration if things go badly, excluding catastrophes"],
                ["Expected time (TE or E)", "The weighted average of O, M and P"],
                ["Critical path", "The longest path through the network; it sets the shortest possible project duration"],
                ["Slack or float", "How long an activity or event can slip without delaying the project; see [float and slack](/project-management/float-and-slack/)"],
            ),
        ),
        S(
            "The PERT formulas",
            T(
                ["Measure", "Formula", "What it tells you"],
                ["Expected duration (E)", "(O + 4M + P) / 6", "The duration to plan with"],
                ["Standard deviation (SD)", "(P - O) / 6", "How uncertain one activity is"],
                ["Variance", "SD squared", "Uncertainty in a form you can add up"],
                ["Path expected duration", "Sum of E along the path", "The expected length of a path"],
                ["Path SD", "Square root of the sum of variances along the path", "How uncertain the whole path is"],
                ["z-score", "(Deadline - path expected duration) / path SD", "Look up z in a normal table to get the probability"],
            ),
            "**Quick example.** A design task is estimated at O = 4 days, M = 6 days and P = 14 days. "
            "E = (4 + 24 + 14) / 6 = 42 / 6 = **7 days**, and SD = (14 - 4) / 6 = **1.67 days**. The expected "
            "duration is longer than the most likely value because the pessimistic tail is long, which is exactly "
            "the effect PERT is designed to capture.",
            H3("Why the most likely value is weighted by 4"),
            "PERT assumes each activity's duration follows a beta distribution, which can be skewed, unlike a "
            "normal curve. The (O + 4M + P) / 6 formula is a simple approximation of that distribution's mean, "
            "and (P - O) / 6 assumes the range covers roughly six standard deviations. Both are approximations, "
            "not laws. A simpler alternative is the triangular average, (O + M + P) / 3, which gives more weight "
            "to the extremes; our guides to [cost estimation](/project-management/cost-estimation/) and "
            "[effort estimation](/project-management/effort-estimation/) compare the two.",
        ),
        S(
            "How to get good three-point estimates",
            "PERT is only as good as its inputs. Three-point estimates go wrong in predictable ways, so plan how you "
            "collect them.",
            L(
                "**Ask the people who will do the work,** ideally two or three of them, and discuss differences "
                "rather than averaging them away.",
                "**Ask for the extremes first.** Asking \"what is the worst realistic case?\" before \"what is "
                "most likely?\" reduces anchoring on a single number.",
                "**Define the pessimistic case clearly.** It should cover things that plausibly go wrong (rework, "
                "a key person off sick, a slow supplier), not disasters, which belong in the "
                "[risk register](/templates/risk-register-template/).",
                "**Use history where you have it.** Actual durations from similar past activities are better than "
                "memory; [expert judgment](/project-management/expert-judgment/) fills the gaps.",
                "**Record assumptions** with each estimate so you can revisit them when conditions change.",
                "**Challenge narrow ranges.** If O, M and P are almost identical on new work, the team may be "
                "underestimating uncertainty.",
            ),
        ),
        S(
            "How to make a PERT chart step by step",
            OL(
                "**List the activities.** Start from your [work breakdown structure](/project-management/work-breakdown-structure/) "
                "and break work packages into activities small enough to estimate.",
                "**Identify dependencies.** For each activity, record which activities must finish before it can start.",
                "**Collect three estimates.** Ask the people doing the work for O, M and P. Ask for the pessimistic "
                "case explicitly; do not just pad the most likely figure.",
                "**Calculate E, SD and variance** for every activity.",
                "**Draw the network.** Use boxes and arrows (AON) or events and arrows (AOA), working left to right "
                "from start to finish.",
                "**Run the forward and backward pass** using E as the duration to find early and late dates and "
                "float. Our [forward and backward pass](/project-management/forward-and-backward-pass/) guide shows the working.",
                "**Mark the critical path:** the chain of activities with zero total float.",
                "**Calculate the probability** of meeting the deadline from the critical path's variance.",
                "**Check near-critical paths** and, for important commitments, run a simulation.",
                "**Set contingency and baseline the schedule,** then update estimates as work progresses.",
            ),
        ),
        S(
            "Worked example: launching a customer portal",
            "This illustrative example follows a small project team launching a customer self-service portal. "
            "Durations are in working days and use the day-0 convention: the first activity starts at time 0, and "
            "a successor's early start equals its predecessor's early finish.",
            H3("Step 1: activities and three-point estimates"),
            T(
                ["ID", "Activity", "Predecessors", "O", "M", "P"],
                ["A", "Gather requirements", "None", "4", "5", "12"],
                ["B", "Design user experience", "A", "3", "6", "9"],
                ["C", "Set up hosting infrastructure", "A", "5", "8", "17"],
                ["D", "Build front end", "B", "8", "10", "18"],
                ["E", "Build back end and integrations", "A", "10", "16", "22"],
                ["F", "Integration testing", "C, D, E", "4", "6", "14"],
                ["G", "User acceptance testing", "F", "3", "4", "11"],
                ["H", "Prepare training and support", "B", "5", "7", "15"],
                ["I", "Go-live", "G, H", "1", "2", "3"],
            ),
            H3("Step 2: expected durations and variances"),
            T(
                ["ID", "Working for E", "E", "SD", "Variance"],
                ["A", "(4 + 20 + 12) / 6", "6", "1.33", "1.78"],
                ["B", "(3 + 24 + 9) / 6", "6", "1.00", "1.00"],
                ["C", "(5 + 32 + 17) / 6", "9", "2.00", "4.00"],
                ["D", "(8 + 40 + 18) / 6", "11", "1.67", "2.78"],
                ["E", "(10 + 64 + 22) / 6", "16", "2.00", "4.00"],
                ["F", "(4 + 24 + 14) / 6", "7", "1.67", "2.78"],
                ["G", "(3 + 16 + 11) / 6", "5", "1.33", "1.78"],
                ["H", "(5 + 28 + 15) / 6", "8", "1.67", "2.78"],
                ["I", "(1 + 8 + 3) / 6", "2", "0.33", "0.11"],
            ),
            H3("Step 3: forward and backward pass"),
            "The forward pass takes the largest early finish at merge points (F waits for C, D and E). The "
            "backward pass starts from the project finish of 37 and takes the smallest late start at burst points "
            "(A feeds B, C and E).",
            T(
                ["ID", "E", "ES", "EF", "LS", "LF", "Total float"],
                ["A", "6", "0", "6", "0", "6", "0"],
                ["B", "6", "6", "12", "6", "12", "0"],
                ["C", "9", "6", "15", "14", "23", "8"],
                ["D", "11", "12", "23", "12", "23", "0"],
                ["E", "16", "6", "22", "7", "23", "1"],
                ["F", "7", "23", "30", "23", "30", "0"],
                ["G", "5", "30", "35", "30", "35", "0"],
                ["H", "8", "12", "20", "27", "35", "15"],
                ["I", "2", "35", "37", "35", "37", "0"],
            ),
            H3("Step 4: find the critical path"),
            T(
                ["Path", "Expected duration", "Path variance", "Path SD"],
                ["A-B-D-F-G-I (critical)", "37", "10.22", "3.20"],
                ["A-E-F-G-I", "36", "10.44", "3.23"],
                ["A-C-F-G-I", "29", "10.44", "3.23"],
                ["A-B-H-I", "22", "5.67", "2.38"],
            ),
            "The critical path is **A-B-D-F-G-I**, with an expected duration of **37 working days**. Notice the "
            "back-end path, A-E-F-G-I: it is only one day shorter and slightly more uncertain. Keep an eye on "
            "it; it matters in the probability calculation.",
            H3("Step 5: the same network as an activity-on-arrow chart"),
            "In the original PERT style, activities are arrows between numbered events. C and E both start at "
            "event 2 and both must finish before F, which would draw two arrows between the same pair of events. "
            "To keep each activity unique, C ends at its own event 4, and a **dummy** (zero duration) links "
            "event 4 to event 5.",
            T(
                ["Event", "Meaning", "Earliest time (TE)", "Latest time (TL)", "Event slack"],
                ["1", "Project start", "0", "0", "0"],
                ["2", "A complete", "6", "6", "0"],
                ["3", "B complete", "12", "12", "0"],
                ["4", "C complete", "15", "23", "8"],
                ["5", "C, D and E complete (dummy 4 to 5)", "23", "23", "0"],
                ["6", "F complete", "30", "30", "0"],
                ["7", "G and H complete", "35", "35", "0"],
                ["8", "Go-live complete", "37", "37", "0"],
            ),
            "The arrows are A (1 to 2), B (2 to 3), C (2 to 4), E (2 to 5), D (3 to 5), H (3 to 7), F (5 to 6), "
            "G (6 to 7) and I (7 to 8). The zero-slack events trace the same critical path.",
        ),
        S(
            "Probability of meeting a deadline",
            "Suppose the sponsor wants the portal live within **40 working days**. PERT treats the critical path's "
            "total duration as roughly normally distributed, so:",
            OL(
                "Path expected duration = 37 days.",
                "Path variance = 1.78 + 1.00 + 2.78 + 2.78 + 1.78 + 0.11 = 10.22, so path SD = square root of 10.22 = 3.20 days.",
                "z = (40 - 37) / 3.20 = 0.94.",
                "From a normal table, z = 0.94 gives a probability of about **83%**.",
            ),
            T(
                ["Deadline (days)", "z", "PERT probability"],
                ["36", "-0.31", "38%"],
                ["37", "0.00", "50%"],
                ["38", "0.31", "62%"],
                ["40", "0.94", "83%"],
                ["42", "1.56", "94%"],
            ),
            "You can also work backwards from the confidence the sponsor wants: deadline = expected duration + "
            "z x path SD. Using z = 0.84 for 80%, 1.28 for 90% and 1.645 for 95% gives about **39.7, 41.1 and "
            "42.3 days**.",
            TIP(
                "Never add standard deviations along a path. Add the variances, then take the square root. Adding "
                "SDs here would give 7.33 days instead of 3.20 and make the project look far riskier than PERT "
                "predicts."
            ),
        ),
        S(
            "Merge bias: why PERT can be optimistic",
            "Classic PERT looks only at the critical path. But F cannot start until C, D **and** E have all "
            "finished. If the back end (E) runs late while the front end (D) runs to time, the back-end path "
            "becomes critical. Because that path is only one day shorter, this happens often. The effect is "
            "called **merge bias**, and it always pushes the real finish later than PERT predicts.",
            "To show the size of the effect, we ran a [Monte Carlo simulation](/project-management/monte-carlo-simulation/) "
            "of this illustrative network: 200,000 runs, each drawing every activity's duration from a beta-PERT "
            "distribution built from the same O, M and P.",
            T(
                ["Measure", "Classic PERT", "Monte Carlo simulation"],
                ["Mean finish", "37.0 days", "37.8 days"],
                ["Chance of finishing within 38 days", "62%", "54%"],
                ["Chance of finishing within 40 days", "83%", "76%"],
                ["Chance of finishing within 42 days", "94%", "90%"],
                ["80% confidence date", "39.7 days", "40.4 days"],
                ["90% confidence date", "41.1 days", "41.9 days"],
            ),
            "In the simulation, the back end rather than the front end set the start of integration testing in "
            "about 38% of runs. The lesson is not that PERT is wrong, but that it is a first approximation. When "
            "near-critical paths merge, treat PERT's probabilities as an upper bound, and simulate before you make "
            "a firm commitment.",
            H3("What-if: reducing back-end uncertainty"),
            "Suppose the team runs a short technical spike on the riskiest integration in week one and re-estimates "
            "the back end (E) at O = 10, M = 14 and P = 18 days. E falls to 14 days and its float rises to 3. "
            "Classic PERT shows **no change** at all, because E is not on the critical path. The simulation tells a "
            "different story:",
            T(
                ["Measure (simulation)", "Before the spike", "After the spike"],
                ["Mean finish", "37.8 days", "37.1 days"],
                ["Chance of finishing within 40 days", "76%", "81%"],
                ["90% confidence date", "41.9 days", "41.4 days"],
            ),
            "Reducing uncertainty on a near-critical path can be worth as much as shortening the critical path "
            "itself, and only a method that looks beyond the single critical path will show it. A "
            "[sensitivity analysis](/project-management/sensitivity-analysis/) helps you find which activities "
            "to work on first.",
        ),
        S(
            "Turning PERT results into a schedule commitment",
            "The point of PERT is a date you can defend. Using the example:",
            L(
                "**Planning target:** 37 days, the expected duration, for the team's working schedule.",
                "**Commitment to the sponsor:** the sponsor asked for 90% confidence. The simulation gives 41.9 "
                "days, so the project manager commits to **42 working days**.",
                "**Schedule contingency:** the 5-day gap between 37 and 42 is held as a single buffer at the end of "
                "the project, owned by the project manager, rather than spread as padding across activities.",
                "**Risk focus:** E and C have the largest variances. Splitting the back-end build or starting "
                "infrastructure earlier reduces uncertainty more than squeezing the most likely estimates.",
            ),
            "This end-of-project buffer is the same idea that [critical chain project management](/project-management/critical-chain-project-management/) "
            "formalises. Record the buffer and its triggers in your [contingency plan](/project-management/contingency-plan/), "
            "and if the committed date is still too late, see [schedule compression](/project-management/schedule-compression/) "
            "for fast tracking and crashing options.",
        ),
        S(
            "PERT vs CPM vs Gantt chart",
            T(
                ["", "PERT chart", "CPM", "[Gantt chart](/project-management/gantt-chart/)"],
                ["Main purpose", "Model duration uncertainty", "Find the critical path and float", "Show the schedule on a calendar"],
                ["Duration estimates", "Three per activity", "One per activity", "One per task"],
                ["Shows dependencies", "Yes, clearly", "Yes", "Yes, as links between bars"],
                ["Shows calendar dates", "Not usually", "As calculated dates", "Yes"],
                ["Key output", "Expected duration and probability", "Early and late dates, float", "Timeline for tracking progress"],
                ["Best for", "New or uncertain work, setting contingency", "Repeatable work with reliable estimates", "Communicating and tracking the plan"],
            ),
            "In practice the three are used together: PERT to estimate, CPM logic to calculate dates and float, and "
            "a Gantt chart to communicate and track the plan. Read our guide to the "
            "[critical path method](/project-management/critical-path-method/) for the single-estimate version of the calculation.",
        ),
        S(
            "Advantages and disadvantages of PERT charts",
            T(
                ["Advantages", "Disadvantages"],
                ["Makes uncertainty visible instead of hiding it in padded estimates", "Three estimates per activity take more effort to collect"],
                ["Gives a probability for a deadline, not just a single date", "Assumes activity durations are independent, which is rarely fully true"],
                ["Shows dependencies and the critical path clearly", "Ignores near-critical paths, so it is optimistic where paths merge"],
                ["Supports what-if analysis on risky activities", "Large networks become hard to draw and maintain by hand"],
                ["Helps justify schedule contingency to sponsors", "Estimates are only as good as the people giving them"],
            ),
        ),
        S(
            "When to use a PERT chart",
            L(
                "**Use it** for new, one-off or research-heavy work where durations are genuinely uncertain: "
                "software launches, R&D, first-of-a-kind engineering, complex events.",
                "**Use it** when a sponsor asks how confident you are in a date, or when you need to size a buffer.",
                "**Use it selectively** on larger projects: three-point estimates for the critical and near-critical "
                "activities, single estimates for routine work.",
                "**Skip it** for small, familiar projects where the team has done the work many times; a simple "
                "[project schedule](/project-management/project-scheduling/) is enough.",
            ),
            "In Agile teams, full PERT networks are rare because work is planned in short iterations. Three-point "
            "thinking still helps for release forecasting alongside "
            "[story point estimation](/project-management/agile/agile-estimation-story-points/).",
        ),
        S(
            "PERT charts in project management software",
            "Most mainstream work management tools do not have dedicated PERT fields, but they handle the network, "
            "dependencies and critical path, and you can add the three estimates yourself.",
            L(
                "**[Wrike](/project-management-tools/wrike/)** (our top-rated tool) supports all four dependency "
                "types with lead and lag, the critical path, float and baselines in its Gantt chart. Add custom "
                "fields for O, M and P, then use E as the task duration.",
                "**[Smartsheet](/project-management-tools/smartsheet/)** is spreadsheet-based, so a formula column "
                "can calculate E and SD next to each task, with dependencies and the critical path in the Gantt view.",
                "**[ClickUp](/project-management-tools/clickup/)** offers Gantt charts with dependencies, the critical "
                "path, slack and baselines on paid plans.",
                "**[Microsoft Planner](/project-management-tools/microsoft-planner/)** premium plans cover scheduled "
                "projects with dependencies, and Plan 3 adds baselines and the critical path.",
            ),
            "For learning or one-off analysis, a spreadsheet is often the quickest option. Our free "
            "[critical path template](/templates/critical-path-template/) handles durations, predecessors, early "
            "and late dates and float, and you can add O, M and P columns in front of the duration. For a "
            "calendar view, use the [project schedule template](/templates/project-schedule-template/).",
        ),
        S(
            "Common PERT mistakes",
            L(
                "**Padding the most likely estimate.** M should be the realistic central case; the pessimistic "
                "estimate is where the bad news belongs.",
                "**Adding standard deviations.** Add variances along a path, then take the square root.",
                "**Ignoring near-critical paths.** A path a day or two shorter can drive the finish; check it or simulate.",
                "**Treating the expected duration as a promise.** E is roughly a 50% date. Commit to a higher "
                "confidence date and hold the difference as contingency.",
                "**Using very wide ranges without asking why.** If P is many times O, the activity is poorly "
                "understood. Break it down or investigate before relying on any number.",
                "**Never updating the chart.** Re-estimate remaining work as you learn; the uncertainty should "
                "shrink as the project progresses.",
            ),
        ),
    ],
    faq=[
        ("What does PERT stand for?",
         "Program Evaluation and Review Technique. It was developed in 1958 for the US Navy's Polaris programme."),
        ("What is a PERT chart used for?",
         "To plan projects with uncertain durations: it shows activities and dependencies, finds the critical path "
         "and estimates the probability of meeting a deadline."),
        ("What is the PERT formula?",
         "Expected duration = (optimistic + 4 x most likely + pessimistic) / 6. For O = 4, M = 6 and P = 14 days, "
         "the PERT estimate is 7 days."),
        ("How do you calculate PERT standard deviation?",
         "(Pessimistic - optimistic) / 6 for one activity. For a path, add the activities' variances (SD squared) "
         "and take the square root."),
        ("Why is the most likely value multiplied by 4 in PERT?",
         "The formula approximates the mean of a beta distribution, in which the most likely value carries most of "
         "the weight while the optimistic and pessimistic values allow for skew."),
        ("How do you calculate the probability of completing a project with PERT?",
         "Calculate z = (deadline - expected duration of the critical path) / path standard deviation, then look up z "
         "in a normal distribution table. A z of 1 gives about 84%."),
        ("Is a PERT chart the same as a network diagram?",
         "A PERT chart is a type of network diagram. What makes it PERT is the use of three-point estimates and "
         "probability analysis."),
        ("What is a dummy activity in a PERT chart?",
         "A zero-duration arrow used in activity-on-arrow charts to show a dependency, or to stop two activities "
         "sharing the same start and end events. It uses no time or resources."),
        ("What is the difference between a PERT chart and a Gantt chart?",
         "A PERT chart shows the logic and uncertainty of the network; a Gantt chart shows tasks as bars on a "
         "calendar for scheduling and tracking. Many teams use both."),
        ("What is the difference between PERT and CPM?",
         "PERT uses three estimates per activity to model uncertainty and probability; CPM uses one estimate and "
         "focuses on the critical path, float and time-cost trade-offs."),
        ("Can PERT be used in Agile?",
         "Not usually as a full network, but three-point estimates are useful for release forecasts and for "
         "communicating uncertainty to stakeholders."),
        ("Who invented PERT?",
         "The US Navy's Special Projects Office developed it in 1958 with Lockheed and Booz Allen Hamilton, to "
         "manage the Polaris missile programme."),
        ("Is PERT on the PMP exam?",
         "Three-point estimating and network calculations are common PMP study topics. See our "
         "[PMP certification guide](/project-management/pmp-certification/) for the current exam content."),
    ],
)
