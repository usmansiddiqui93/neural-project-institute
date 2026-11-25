from core import S, L, OL, T, TIP, H3

URL = "/project-management/monte-carlo-simulation/"

RW = dict(
    title="Monte Carlo Simulation in Project Management: Worked Example",
    desc="Monte Carlo simulation explained: turn three-point estimates and risks into P50 and P80 dates and costs, with a worked example, Excel formulas and limits.",
    intro=(
        "Monte Carlo simulation in project management recalculates a schedule or cost model thousands of times, "
        "each time drawing random values from the estimate ranges and risks you supply, and reports how likely "
        "each finish date or final cost is. Instead of one date, you get statements such as \"50% likely by day 50, "
        "80% likely by day 56\". This guide explains the mechanism, the inputs, a fully worked example with "
        "merging paths, risk events and cost, and how to turn the results into contingency and decisions."
    ),
    takeaways=[
        "A Monte Carlo simulation answers \"how confident can we be in this date or budget?\", which a single-point schedule cannot.",
        "Plans built from most-likely estimates are usually optimistic: skewed ranges, merging paths and risk events all push the real outcome later and higher.",
        "In our illustrative example, a 42-day plan had about a 5% chance of being met; the P80 was 55.3 working days and the P80 cost £475,500.",
        "P80 for the date and P80 for the cost are not met together 80% of the time; in the example both were met in only 72% of runs.",
        "The answer depends heavily on the ranges, the distribution shape and correlation, so document every assumption and rerun the model as the project changes.",
    ],
    sections=[
        S(
            "What is Monte Carlo simulation in project management?",
            "**Monte Carlo simulation** is a quantitative risk analysis technique that runs a project schedule or cost "
            "model many times, each time sampling every uncertain duration, cost and risk event from a probability "
            "distribution. The collected results form a distribution of possible outcomes, from which you read the "
            "probability of meeting a date or budget, such as P50 or P80.",
            "A normal schedule is **deterministic**: one duration per activity produces one finish date. A Monte Carlo "
            "model is **probabilistic**: each activity carries a range, so the finish date becomes a range too, with a "
            "probability attached to every point in it. The technique does not make the project more predictable. It "
            "makes the existing uncertainty visible, so the sponsor can choose how much confidence to buy with schedule "
            "and cost contingency.",
            "The method itself comes from physics. Stanislaw Ulam conceived it at Los Alamos in 1946, John von Neumann "
            "and Nicholas Metropolis developed it, and Metropolis named it after the gambling resort of Monte Carlo, a "
            "nod to the method's reliance on chance. In project management it sits within quantitative risk analysis, the stage of "
            "[project risk management](/project-management/project-risk-management/) that puts numbers on the combined "
            "effect of risks on the objectives.",
            T(
                ["Question", "Deterministic schedule", "Monte Carlo simulation"],
                ["When will we finish?", "One date, for example day 42", "A range, for example 50% by day 49.5, 80% by day 55.3"],
                ["How likely is the planned date?", "Cannot say", "A probability, for example about 5%"],
                ["Which activities drive the date?", "The critical path only", "Criticality index and sensitivity for every activity and risk"],
                ["How much contingency do we need?", "A habitual percentage", "The gap between the plan and a chosen confidence level"],
            ),
        ),
        S(
            "Why single-point plans are usually optimistic",
            "Four effects make a plan built from most-likely estimates finish earlier on paper than it does in reality. "
            "A simulation captures all four at once, which is its main advantage over adding up estimates by hand.",
            L(
                "**Skewed ranges.** Most activities can overrun by more than they can underrun. A task estimated at 20 "
                "days might take 16 at best and 30 at worst. The mean of that range is higher than 20, so a chain of such "
                "activities finishes later on average than the sum of the most-likely values.",
                "**Merge bias.** Where two or more paths join, the successor waits for the latest of them. Any path that "
                "runs late delays the merge point, while an early path cannot pull it forward. The more near-critical "
                "paths merge, the larger the effect. Our [PERT chart guide](/project-management/pert-chart/) shows it on a "
                "separate network.",
                "**Discrete risk events.** A risk that may or may not happen, such as a supplier missing a production slot, "
                "is absent from the most-likely plan. In a simulation it occurs in the share of runs matching its "
                "probability.",
                "**Correlation.** When one cause, such as an under-resourced contractor, slows several activities at once, "
                "overruns cluster instead of cancelling out. Ignoring correlation makes the range of outcomes look "
                "narrower than it is.",
            ),
            "The worked example below separates these effects so you can see how much each contributes.",
        ),
        S(
            "What a Monte Carlo model needs",
            H3("A model with sound logic"),
            "For a schedule, the model is a logic-linked network: activities, durations and "
            "[dependencies](/project-management/task-dependencies/), with as few hard date constraints as possible. "
            "Each iteration repeats the forward pass with new durations, so missing links or constraints that override "
            "logic produce meaningless results. GAO's schedule assessment guidance makes the same point: the schedule "
            "must contain complete and correct logic before a schedule risk analysis can be trusted. Build and check the "
            "network first with a [project network diagram](/project-management/project-network-diagram/) and the "
            "[critical path method](/project-management/critical-path-method/).",
            "For cost, the model is usually the cost estimate by work package, with time-related costs (site "
            "management, hired equipment, the project team) linked to the simulated duration. That link matters: a "
            "late finish costs money, and a cost model that ignores duration understates cost risk.",
            H3("Ranges and probability distributions"),
            "Each uncertain input needs a range and a shape. Ranges usually come from three-point estimates "
            "(optimistic, most likely and pessimistic) produced through [effort estimation](/project-management/effort-estimation/), "
            "[cost estimation](/project-management/cost-estimation/) and [expert judgment](/project-management/expert-judgment/), "
            "or better, from historical records of similar work.",
            T(
                ["Distribution", "Inputs", "Mean", "When to use it"],
                ["Triangular", "Min a, most likely m, max b", "(a + m + b) / 3", "Default when you have only three-point estimates; gives relatively heavy tails"],
                ["Beta-PERT", "Min a, most likely m, max b", "(a + 4m + b) / 6", "Experts are confident in the most likely value; tails are thinner than triangular"],
                ["Uniform", "Min and max", "(a + b) / 2", "Any value in the range is equally plausible and there is no most likely value"],
                ["Discrete (yes/no)", "Probability p and an impact", "p x mean impact", "Risk events that either happen or do not"],
                ["Lognormal or empirical", "Fitted to historical data", "From the data", "You have enough completed-activity actuals to fit or resample"],
            ),
            "Distribution choice is not a technicality. In the example below, switching every activity duration from "
            "triangular to beta-PERT moved the P80 finish by almost three working days.",
            H3("Risk events from the risk register"),
            "Discrete risks come from the [risk register](/project-management/risk-register/); our guide to "
            "[project risk](/project-management/project-risk/) covers how to identify and describe them. For each one you need a "
            "probability of occurrence, the activity or cost line it affects, and an impact range if it occurs. Model a "
            "risk either as a separate event or inside an activity's range, never both, or it will be counted twice.",
            H3("Correlation between inputs"),
            "Where a common cause links inputs, enter a correlation coefficient, usually between 0 and 1. Typical "
            "candidates are activities performed by the same contractor, cost lines priced from the same rate "
            "assumption, and tasks that depend on the same immature design. PMI's 2011 Global Congress paper on cost "
            "estimating by Barreras recommends recording correlations in a matrix and agreeing them with the functional "
            "leads.",
        ),
        S(
            "How to run a Monte Carlo simulation, step by step",
            OL(
                "**Define the question.** For example: \"How likely are we to finish by 30 June and within £450,000, and "
                "what contingency do we need for 80% confidence?\"",
                "**Build or clean the model.** Check schedule logic, remove unnecessary constraints and link time-related "
                "costs to duration. A summary network is often enough if it keeps the key hand-offs and merge points.",
                "**Collect ranges.** Hold short estimating interviews for each significant activity and cost line. Ask for "
                "the pessimistic value first and challenge narrow ranges; people are usually over-confident.",
                "**Choose distributions.** Use historical data where you have it, otherwise triangular or beta-PERT, and "
                "record the reason.",
                "**Add risk events.** Map the top risks from the register to the activities and cost lines they affect, "
                "with probabilities and impact ranges.",
                "**Set correlations.** Identify common causes and enter coefficients for the inputs they affect.",
                "**Run enough iterations.** Several thousand is typical; check that repeated runs give stable percentiles.",
                "**Read the results.** Histogram, cumulative S-curve, P-values, criticality index and sensitivity ranking.",
                "**Decide and act.** Set the commitment and contingency, test risk responses in the model, and record "
                "the confidence levels in the [project baseline](/project-management/project-baseline/) documents.",
                "**Repeat.** Rerun at each major stage gate or when scope, logic or the risk profile changes.",
            ),
            TIP(
                "Keep a short assumptions log next to the model: the source of each range, each distribution choice, "
                "each correlation and the number of iterations. Without it, nobody can challenge or reproduce the P80."
            ),
        ),
        S(
            "Worked example: refurbishing a training centre",
            "This scenario is **illustrative**: invented to show the technique, not drawn from a real project. A team is "
            "refurbishing a training centre and installing new simulation equipment. All durations are in working days "
            "and costs in thousands of pounds (£k). Every figure below was calculated in Python with 100,000 iterations "
            "and a fixed random seed; your own runs will differ slightly in the last decimal place.",
            H3("The model and its inputs"),
            T(
                ["Activity", "Predecessors", "Duration O / M / P (days)", "Direct cost O / M / P (£k)"],
                ["A: Design and approvals", "None", "8 / 10 / 16", "30 / 35 / 45"],
                ["B: Manufacture and delivery of equipment", "A", "16 / 20 / 30", "182 / 190 / 205"],
                ["C: Site works", "A", "12 / 15 / 22", "72 / 80 / 100"],
                ["D: Installation and commissioning", "B and C", "6 / 8 / 14", "25 / 30 / 45"],
                ["E: Testing and handover", "D", "3 / 4 / 7", "8 / 10 / 15"],
            ),
            "Time-related costs (site management, hired plant and the project team) run at **£2,000 per working day** "
            "for the whole duration. Two risks from the register are modelled as discrete events:",
            T(
                ["Risk", "Probability", "Affects", "Impact if it occurs"],
                ["R1: Equipment supplier misses its factory slot", "25%", "B", "+5 / 10 / 15 days"],
                ["R2: Asbestos found during site works", "15%", "C", "+5 / 8 / 15 days and £18k removal cost"],
            ),
            "The deterministic plan uses the most-likely values. Path A-B-D-E takes 10 + 20 + 8 + 4 = **42 days** and "
            "is critical. Path A-C-D-E takes 37 days, so C has 5 days of [total float](/project-management/float-and-slack/). "
            "The deterministic budget is £345k of direct cost plus 42 x £2k = £84k of time-related cost, a total of "
            "**£429k**. Every duration, cost line and risk impact was sampled from a triangular distribution, and all "
            "inputs were treated as independent.",
            H3("What one iteration does"),
            "Each iteration draws a value for every input, applies any risks that occur, and repeats the forward pass. "
            "Three sample iterations from the simulation:",
            T(
                ["Iteration", "A", "B (+R1)", "C (+R2)", "D", "E", "Finish = A + max(B, C) + D + E"],
                ["1", "11.8", "26.2 (R1 no)", "18.0 + 11.5 = 29.5 (R2 yes)", "7.9", "4.1", "11.8 + 29.5 + 7.9 + 4.1 = 53.3"],
                ["2", "12.9", "21.4 (R1 no)", "15.0 (R2 no)", "8.1", "4.0", "12.9 + 21.4 + 8.1 + 4.0 = 46.4"],
                ["3", "11.4", "29.2 + 10.6 = 39.8 (R1 yes)", "18.2 (R2 no)", "9.7", "6.6", "11.4 + 39.8 + 9.7 + 6.6 = 67.5"],
            ),
            "In iteration 1 the asbestos risk occurs and the non-critical site works path (C) drives the finish, even "
            "though it had 5 days of float in the plan. In iteration 3 the supplier risk occurs and the finish lands "
            "25.5 working days after the plan. After 100,000 such iterations, the finish dates form the distribution below.",
            H3("Schedule results"),
            T(
                ["Measure", "Finish (working days)"],
                ["Deterministic plan", "42.0"],
                ["Probability of finishing in 42 days or less", "About 5% (4.7%)"],
                ["P10", "43.5"],
                ["P50 (median)", "49.5"],
                ["Mean", "50.3"],
                ["P80", "55.3"],
                ["P90", "58.5"],
                ["Range across all iterations", "About 35 to 75 (the extremes vary between runs)"],
            ),
            "The plan's 42 days is roughly a **P5 date**: it would be met in about one run in twenty. A sponsor who "
            "wants 80% confidence needs to plan for about 56 working days, which means holding about 13 to 14 working "
            "days of schedule contingency (55.3 - 42 = 13.3) as a visible buffer before handover, not spread across "
            "activities.",
            H3("Cost results"),
            T(
                ["Measure", "Total cost (£k)"],
                ["Deterministic budget", "429.0"],
                ["Probability of costing £429k or less", "About 1%"],
                ["P50", "459.0"],
                ["Mean", "460.7"],
                ["P80", "475.5"],
                ["P90", "484.2"],
            ),
            "At P80, the cost contingency is £475.5k - £429k = **£46.5k**, or about 10.8% of the deterministic "
            "estimate. At P50 it would be £30.0k. Note how strongly cost follows the schedule: the rank correlation "
            "between finish date and total cost across iterations is 0.75, because every extra day adds £2,000 of "
            "time-related cost.",
            H3("Why the 42-day plan is so unlikely"),
            "Running the model with and without parts of the uncertainty separates the four effects described earlier:",
            T(
                ["Step", "Mean finish (days)", "Change"],
                ["Deterministic plan (most likely values)", "42.0", ""],
                ["Means of the triangular ranges on path A-B-D-E", "47.3", "+5.3 from skewed ranges"],
                ["Simulation without risk events (adds merge with path C)", "47.4", "+0.1 from merge bias"],
                ["Full simulation with R1 and R2", "50.3", "+2.9 from risk events"],
            ),
            "Skew is the largest effect here: each range has its tail on the overrun side, and the means "
            "(11.3, 22.0, 9.3 and 4.7 days on the critical path) sum to 47.3, not 42. Merge bias is small because path "
            "C has 5 days of float and becomes critical mainly when R2 occurs. On a network with several near-critical "
            "paths, merge bias would be much larger. The risk contribution is close to what "
            "[expected monetary value](/project-management/project-risk-management/) would suggest for R1 alone "
            "(25% x 10 days = 2.5 days), because B is almost always critical.",
            H3("Which inputs drive the result"),
            "Two outputs show where to focus management attention. The **criticality index** is the share of iterations "
            "in which an activity lies on the critical path. The **sensitivity ranking** here uses Spearman rank "
            "correlation between each input and the finish date: the closer to 1, the more that input moves the result.",
            T(
                ["Input", "Criticality index", "Rank correlation with finish"],
                ["R1 supplier slot (occurs or not)", "Not applicable", "0.66"],
                ["B base duration", "87%", "0.45"],
                ["A duration", "100%", "0.29"],
                ["D duration", "100%", "0.29"],
                ["R2 asbestos (occurs or not)", "Not applicable", "0.21"],
                ["E duration", "100%", "0.15"],
                ["C base duration", "13%", "0.05"],
            ),
            "The supplier risk is the single biggest driver of the finish date, ahead of any activity's own estimating "
            "uncertainty. Activities A, D and E are always critical because every path passes through them, yet they "
            "drive less of the spread because their ranges are narrower. Criticality and sensitivity answer different "
            "questions, which is why tools report both. For one-at-a-time testing and tornado charts, see our guide "
            "to [sensitivity analysis](/project-management/sensitivity-analysis/).",
            H3("Testing a risk response in the model"),
            "The supplier offers a reserved factory slot for £6,000, which the team judges would cut R1's probability "
            "from 25% to 5%. Rerunning the model with that response:",
            T(
                ["Measure", "Without response", "With reserved slot", "Change"],
                ["P50 finish (days)", "49.5", "48.1", "-1.4"],
                ["P80 finish (days)", "55.3", "52.1", "-3.2"],
                ["P90 finish (days)", "58.5", "54.4", "-4.1"],
                ["Mean cost (£k)", "460.7", "463.0", "+2.3"],
                ["P80 cost (£k)", "475.5", "475.8", "+0.3"],
            ),
            "The response buys about three working days at the P80 level for almost no change in P80 cost: the £6,000 "
            "is largely offset by fewer days of time-related cost in the bad outcomes. On the mean, it costs about "
            "£2,300 more. If the handover date matters, for example because training courses are already booked, the "
            "response is good value. If only cost matters, it is roughly neutral. This is the kind of decision a "
            "simulation supports and a single-point plan cannot.",
            H3("Meeting the date and the budget together"),
            "The P80 date (55.3 days) and P80 cost (£475.5k) were **both** met in only **72%** of iterations, not 80%. "
            "Some runs finish on time but over budget and others the reverse. To reach about 80% joint confidence in "
            "this model, both targets had to move to roughly their 88th percentiles (57.8 days and £482.1k, met together "
            "in 82% of runs). NASA calls this measure the **joint cost and schedule confidence level (JCL)**; its "
            "2009 JCL guidance asks projects to be budgeted at a 70% JCL unless the decision authority approves "
            "otherwise.",
            "See [project forecasting](/project-management/project-forecasting/) for how a simulation sits alongside "
            "[earned value management](/project-management/earned-value-management/) and earned schedule forecasts once "
            "the project is under way.",
        ),
        S(
            "How to read Monte Carlo outputs",
            T(
                ["Output", "What it shows", "How to use it"],
                ["Histogram", "How often each finish date or cost occurred", "Spot skew, long tails and double peaks (often a large risk event)"],
                ["Cumulative S-curve", "Probability of finishing on or before each date or cost", "Read P-values; compare against the plan and the deadline"],
                ["P-value (P50, P80, P90)", "The value not exceeded in that share of iterations", "Set commitments and size contingency"],
                ["Criticality index", "Share of iterations in which an activity is critical", "Watch near-critical activities the deterministic plan ignores"],
                ["Sensitivity ranking or tornado", "Which inputs move the result most", "Target risk responses and better estimates"],
                ["Cost-schedule scatter", "Each iteration's finish and cost together", "Read joint confidence; check that cost and time are linked"],
            ),
            "The cumulative chart of outcomes is a probability S-curve and is a different chart from the cost "
            "[S-curve](/project-management/s-curve/) used to track planned and earned value over time, although both "
            "share the shape.",
            H3("Choosing a confidence level"),
            "No standard mandates one percentile for every project. The choice reflects how costly a miss is and who "
            "carries the risk. Some reference points:",
            L(
                "**P50** is the median: as likely to be beaten as missed. It suits internal targets and portfolio "
                "totals, where overruns on some projects offset savings on others.",
                "**P80** is a common basis for external commitments and contingency. Barreras's PMI paper notes P80 as "
                "commonly used for total project cost and P90 when management reserve is included.",
                "**GAO's Schedule Assessment Guide** gives the example of an organisation adopting a completion "
                "date with a 70% probability, chosen according to its risk tolerance.",
                "**NASA** budgets projects at a 70% joint cost and schedule confidence level and funds them at no less "
                "than 50%, according to its 2009 JCL guidance.",
            ),
            "A common arrangement is to set the baseline at the deterministic or P50 value and hold the difference to "
            "the chosen percentile as contingency reserve, with management reserve above that for unidentified risks. "
            "How the reserves are owned and released is covered in our guides to the "
            "[contingency plan](/project-management/contingency-plan/) and the [project budget](/project-management/project-budget/).",
            TIP(
                "Report P-values with their assumptions: \"80% confident of handover by day 56, assuming the supplier "
                "risk is unmitigated and durations are independent.\" A bare number invites false precision."
            ),
        ),
        S(
            "How assumptions change the answer",
            "The same project can produce noticeably different P80s depending on modelling choices. Testing the main "
            "choices on the example shows how much each one matters.",
            H3("Distribution shape"),
            T(
                ["Measure (with risks)", "Triangular", "Beta-PERT"],
                ["Mean finish (days)", "50.3", "47.7"],
                ["P50 finish (days)", "49.5", "46.7"],
                ["P80 finish (days)", "55.3", "52.4"],
                ["Probability of meeting 42 days", "4.7%", "13.9%"],
                ["P80 cost (£k)", "475.5", "469.9"],
            ),
            "Only the five activity durations were switched; cost lines and risk impacts stayed triangular, so the cost "
            "change comes entirely from the shorter durations. Beta-PERT concentrates more probability near the most "
            "likely value, so it gives earlier dates from the same three numbers. Neither is right in general. Use triangular when the experts' most likely value is "
            "itself uncertain, beta-PERT when it is well supported, and historical data when you have it.",
            H3("Correlation"),
            "A second run gave all five activity durations a pairwise correlation of 0.5, representing a common cause "
            "such as one main contractor's productivity. Both columns come from that run (seeded separately), so the "
            "first column differs from the headline results by at most 0.1 days.",
            T(
                ["Measure (with risks)", "Independent (0.0)", "Correlated (0.5)"],
                ["Mean finish (days)", "50.3", "50.3"],
                ["Standard deviation (days)", "5.8", "7.2"],
                ["P10 (days)", "43.4", "41.3"],
                ["P80 (days)", "55.2", "56.4"],
                ["P90 (days)", "58.5", "60.0"],
            ),
            "Correlation leaves the mean almost unchanged but widens the spread in both directions. The upper percentiles "
            "used for commitments move later, so ignoring a real common cause makes the P80 look safer than it is.",
            H3("Number of iterations"),
            "Each run of the full model was repeated 100 times with different random seeds to see how much the P80 "
            "finish moved from run to run:",
            T(
                ["Iterations per run", "Lowest P80 (days)", "Highest P80 (days)", "Standard deviation (days)"],
                ["100", "52.9", "57.7", "1.06"],
                ["1,000", "54.5", "56.1", "0.35"],
                ["10,000", "55.1", "55.6", "0.11"],
                ["100,000", "55.23", "55.38", "0.03"],
            ),
            "A few thousand iterations are usually enough for decisions. More "
            "iterations reduce sampling noise only; they do nothing to correct wrong ranges or missing risks. For a "
            "probability such as \"80% likely\", the sampling error is roughly the square root of p(1 - p) / n: about "
            "1.3 percentage points at 1,000 iterations and 0.4 points at 10,000.",
        ),
        S(
            "Monte Carlo simulation in Excel",
            "A spreadsheet can run a simple simulation with no add-in by using one row per iteration. To sample a "
            "triangular distribution, generate a uniform random number U with RAND() and apply the inverse of the "
            "triangular cumulative distribution:",
            L(
                "**a** = optimistic (minimum) value, **m** = most likely value, **b** = pessimistic (maximum) value, all in "
                "the same unit (working days or £).",
                "**U** = a uniform random number between 0 and 1, held in its own cell.",
                "If U < (m - a) / (b - a): **x = a + SQRT(U x (b - a) x (m - a))**",
                "Otherwise: **x = b - SQRT((1 - U) x (b - a) x (b - m))**",
            ),
            "In Excel, with U in cell F2: =IF(F2<(m-a)/(b-a), a+SQRT(F2*(b-a)*(m-a)), b-SQRT((1-F2)*(b-a)*(b-m))). "
            "For activity B (a = 16, m = 20, b = 30), the switch point is (20 - 16) / (30 - 16) = 0.286. With U = 0.5, "
            "x = 30 - SQRT(0.5 x 14 x 10) = 30 - 8.37 = **21.6 days**, which is the median of that distribution. With "
            "U = 0.2, x = 16 + SQRT(0.2 x 14 x 4) = **19.3 days**.",
            OL(
                "Put each activity's sampled duration in its own column, each with its own RAND() cell.",
                "Model each risk event as =IF(RAND()<p, impact, 0), where the impact is itself a sampled value.",
                "Calculate the finish for the row from the network logic, for example =A + MAX(B_total, C_total) + D + E.",
                "Copy the row down 10,000 rows.",
                "Read percentiles with =PERCENTILE.INC(finish_range, 0.8) and probabilities with "
                "=COUNTIF(finish_range, \"<=42\")/COUNT(finish_range).",
                "Copy and paste the results as values before you report them, because RAND() recalculates on every edit.",
            ),
            TIP(
                "Never write RAND() twice inside one sampling formula. Each call returns a different number, so the "
                "IF test and the result would use different values of U and the distribution would be wrong."
            ),
            "Spreadsheets work for small networks and cost models. They become impractical when the logic has many "
            "merge points, lags or calendars, because you must rewrite the forward pass as formulas. For real "
            "schedules, use a schedule risk analysis tool that reads the plan directly. The "
            "[critical path template](/templates/critical-path-template/) and "
            "[project cost estimate template](/templates/project-cost-estimate-template/) on this site provide the "
            "network logic and cost lines you would feed into such a model; neither template runs a simulation itself.",
        ),
        S(
            "Monte Carlo versus PERT, EMV and sensitivity analysis",
            T(
                ["Technique", "What it varies", "Output", "Main limitation"],
                ["Classic PERT", "Durations on the critical path only", "Expected duration and a normal-approximation probability", "Ignores merge bias, risk events and correlation"],
                ["Expected monetary value (EMV)", "Each risk's probability and impact", "One average value per risk or in total", "No range; one large risk can exceed the total"],
                ["Sensitivity analysis", "One input at a time, or a few scenarios", "Swing in the result per input", "Says how much, not how likely"],
                ["Monte Carlo simulation", "All inputs and risks together", "Full distribution of dates and costs", "Only as good as the ranges, logic and correlations"],
            ),
            "On the example network, classic PERT along A-B-D-E gives an expected duration of 10.67 + 21.00 + 8.67 + "
            "4.33 = 44.67 days, a path variance of 9.44 and a standard deviation of 3.07 days, so z = (42 - 44.67) / "
            "3.07 = -0.87 and a 19% chance of meeting 42 days. The full simulation gave about 5%, because it also "
            "includes the risk events, the path through C and the heavier tails of the triangular distribution. "
            "PERT is a useful first estimate; Monte Carlo is the check before a firm commitment.",
            "Read our [PERT chart guide](/project-management/pert-chart/) for the PERT formulas and a worked "
            "probability calculation.",
        ),
        S(
            "Monte Carlo forecasting in Agile and Kanban",
            "Teams using flow-based or iterative delivery often run a different kind of Monte Carlo simulation. Instead "
            "of activity ranges, it resamples the team's own history: weekly throughput, or Sprint velocity, drawn at "
            "random week by week until the remaining backlog is finished. It needs no task estimates and answers "
            "\"when will these 40 items be done?\" or \"how many items by this date?\" with a probability.",
            "The same cautions apply. The history must come from a reasonably stable system, scope growth must be "
            "modelled or the forecast will be early, and the forecast needs updating as new data arrives. The "
            "mechanics and a worked throughput example are in our guide to [Kanban planning](/project-management/kanban/kanban-planning/), "
            "and [throughput in Kanban](/project-management/kanban/throughput/) explains how to measure the input data.",
        ),
        S(
            "When to use Monte Carlo simulation, and when not to",
            T(
                ["Use it when", "Simpler methods are enough when"],
                ["A date or budget commitment carries contractual, regulatory or reputational consequences", "The project is small, short and similar to past work"],
                ["The network has several near-critical paths that merge", "One clear critical path dominates and has little uncertainty"],
                ["Several significant risk events could affect the same objectives", "Risks are few and independent; EMV gives a sufficient reserve"],
                ["You need to size contingency at a stated confidence level", "Contingency is set by policy and the stakes are low"],
                ["You want to compare risk responses quantitatively", "No credible ranges can be obtained, so results would be guesswork"],
            ),
            "The technique assumes the model's logic reflects how the work will really be done, that the ranges capture "
            "the plausible spread, and that the identified risks and correlations are the important ones. It cannot "
            "predict unknown-unknowns, organisational change or a decision to re-plan, and it does not replace "
            "[schedule compression](/project-management/schedule-compression/) or other responses; it shows whether they "
            "are needed. Where resources, not logic, limit the schedule, consider combining it with "
            "[critical chain project management](/project-management/critical-chain-project-management/) buffers.",
        ),
        S(
            "Common mistakes",
            L(
                "**Ranges that are too narrow.** A pessimistic value that is only 10% above the most likely value is rarely "
                "realistic. Ask \"what would have to go wrong for this to take twice as long?\" and use historical overruns.",
                "**Double counting risks.** If a risk is already inside an activity's pessimistic estimate, do not also "
                "add it as an event.",
                "**Ignoring correlation.** Independent sampling lets overruns and underruns cancel, which narrows the "
                "spread and makes P80 too early.",
                "**Simulating a broken schedule.** Missing logic, hard constraints and open ends make every iteration "
                "wrong in the same way.",
                "**Separating cost from time.** If time-related costs are not linked to duration, the cost model misses "
                "the most common reason for cost overruns.",
                "**Adding P80s.** Percentiles do not add. In the example, the P80s of A, B, D and E (without risk events) sum to "
                "54.0 days, but the P80 of their combined duration is 50.7 days. Simulate the whole model, and read joint "
                "confidence separately when cost and date must both be met.",
                "**Reporting false precision.** \"55.27 days\" implies accuracy the inputs cannot support. Round to the "
                "nearest day or week and state the assumptions.",
                "**Running it once.** A simulation from the business case says little about the project six months later. "
                "Rerun it with actual progress and the current [risk register](/templates/risk-register-template/).",
            ),
        ),
    ],
    faq=[
        ("What is Monte Carlo simulation in project management?",
         "A quantitative risk analysis technique that recalculates a schedule or cost model thousands of times using "
         "random values from estimate ranges and risk events, to show the probability of meeting a date or budget."),
        ("What does P80 mean in a Monte Carlo simulation?",
         "P80 is the value that was not exceeded in 80% of iterations. A P80 finish of day 55 means the model "
         "finished on or before day 55 in 80% of runs, given its assumptions."),
        ("How many iterations does a Monte Carlo simulation need?",
         "Usually a few thousand to 10,000. In our example, the P80 had a run-to-run standard deviation of about 0.35 "
         "days at 1,000 iterations and about 0.1 days at 10,000. More iterations reduce sampling noise but cannot fix poor inputs."),
        ("Which distribution should I use for three-point estimates?",
         "Triangular is a common default and gives heavier tails; beta-PERT weights the most likely value more and "
         "gives earlier dates. Use historical data where you have it and record the choice, because it changes the result."),
        ("Should the budget be set at P50 or P80?",
         "It depends on the cost of a miss and who carries the risk. P50 suits internal targets and portfolio totals; "
         "P80 is common for external commitments, with the difference from the base estimate held as contingency reserve."),
        ("Can I run a Monte Carlo simulation in Excel?",
         "Yes, for small models. Sample each input with RAND() and the inverse triangular formula, put one iteration "
         "per row, and read results with PERCENTILE.INC and COUNTIF. Large schedules need a dedicated tool."),
        ("What is the criticality index?",
         "The percentage of iterations in which an activity lies on the critical path. An activity off the "
         "deterministic critical path can still have a high criticality index if its path is near-critical or risky."),
        ("Does correlation matter in Monte Carlo simulation?",
         "Yes. Correlation between inputs that share a cause widens the spread of results. In our example a pairwise "
         "correlation of 0.5 moved the P80 finish about 1.2 days later and the P90 about 1.5 days later."),
        ("What are the limitations of Monte Carlo simulation?",
         "Results depend entirely on the model's logic, ranges, distributions, risks and correlations. Narrow ranges or "
         "missing risks give confident-looking but optimistic answers, and the model cannot foresee unidentified risks."),
    ],
)
