from core import S, L, OL, T, TIP, H3

URL = "/project-management/fast-tracking-vs-crashing/"
P = "/project-management/"

RW = dict(
    title="Fast Tracking vs Crashing: Differences and Worked Example",
    desc="Fast tracking vs crashing compared: definitions, crash cost slope, a worked example with risk-adjusted cost, break-even rework probability and how to choose.",
    intro=(
        "Fast tracking and crashing are the two standard schedule compression techniques. "
        "Fast tracking shortens the schedule by overlapping activities that would normally run in sequence, so it mainly adds risk of rework; crashing shortens critical activities by adding resources, so it mainly adds cost. "
        "This guide compares them side by side and works through an example that puts the risk of fast tracking and the cost of crashing on the same scale."
    ),
    takeaways=[
        "Fast tracking overlaps sequential activities; crashing adds people, overtime, equipment or faster supply to critical activities. Neither reduces scope.",
        "Both techniques only shorten the project when applied to the critical path, and both use up float and can create new critical paths.",
        "Crashing has a visible, fairly predictable cost per day saved: the crash cost slope. Fast tracking has little direct cost but an uncertain cost of rework.",
        "Compare the two on risk-adjusted cost: the certain cost of crashing against the probability-weighted cost of rework and the delay it would cause.",
        "A blend of a small amount of crashing and a short overlap often beats either technique used alone, but the answer depends on the probabilities and on how much risk the sponsor will accept.",
    ],
    sections=[
        S(
            "Fast tracking vs crashing: the difference",
            "**Fast tracking** is a schedule compression technique in which activities or phases normally done in sequence are performed in parallel for at least part of their duration. **Crashing** shortens the schedule for the least incremental cost by adding resources to critical activities. Fast tracking trades time for risk of rework; crashing trades time for money.",
            "The definitions above follow the *PMI Lexicon of Project Management Terms* (version 4.0, 2024), which defines schedule compression itself as a technique \"used to shorten the schedule duration without reducing the project scope\". That last condition matters: dropping deliverables, accepting a later date or moving work to a later phase are legitimate responses to a deadline problem, but they are not compression.",
            "Both techniques work only on the [critical path](" + P + "critical-path-method/). Overlapping or speeding up an activity with float makes it finish earlier but does not move the project end date. For the full compression method, including indirect costs and the least-cost duration, see our guide to [schedule compression](" + P + "schedule-compression/).",
        ),
        S(
            "Side-by-side comparison",
            T(
                ["", "Fast tracking", "Crashing"],
                ["How it saves time", "Overlaps activities or phases that were planned in sequence", "Adds people, overtime, shifts, equipment or premium supply to critical activities"],
                ["Schedule change", "Changes the logic: finish-to-start link gets a lead, or becomes start-to-start", "Changes durations; the logic stays the same"],
                ["Direct cost", "Little or none at first", "Increases, usually by a known amount per day saved"],
                ["Main risk", "Rework if the earlier activity's output changes", "Lower productivity, fatigue and quality problems; extra resources not available in time"],
                ["Predictability of the saving", "Lower: the saving can be lost to rework", "Higher, within the activity's crash limit"],
                ["Works on", "Discretionary (soft) dependencies", "Work that can be divided or speeded up with more resources"],
                ["Does not work on", "Mandatory dependencies, such as curing, legal approvals or test-before-release rules", "Work limited by physics or a few experts' knowledge"],
                ["Effect on resources", "More activities run at once, so resource demand peaks", "More resources on fewer activities"],
                ["Can be reversed?", "Hard: once later work starts on early inputs, it is committed", "Usually: extra crew or overtime can be stopped"],
                ["Effect on float", "Uses up float on parallel paths; may create new critical paths", "Same"],
            ),
            "The last row is why both techniques make a schedule more fragile. Once the critical path is shorter, other paths that had float become critical or near-critical, so a small delay anywhere can move the finish date.",
        ),
        S(
            "How fast tracking works",
            "In a schedule network, fast tracking changes the relationship between two activities. A finish-to-start (FS) link becomes FS with a lead, written FS-3d for a 3-day lead, or is replaced by a start-to-start (SS) link with a lag. Our guide to [leads and lags](" + P + "leads-and-lags/) explains the notation and date arithmetic. At project level, fast tracking can also overlap whole phases, for example starting construction on early design packages while later packages are still being designed.",
            "Only **discretionary** dependencies can be overlapped. These are sequences chosen as good practice or preference, such as \"finish the full design before ordering anything\". **Mandatory** dependencies, such as \"concrete must cure before loading\" or \"the safety certificate must be issued before the building opens\", cannot be overlapped without breaking a physical, legal or contractual rule. Our guide to [task dependencies](" + P + "task-dependencies/) explains the four dependency attributes.",
            "Two practical questions decide whether an overlap is safe:",
            L(
                "**How likely is the earlier activity's output to change after the later activity starts?** Approved, stable inputs (a signed-off module design, a frozen floor plan) carry little risk; inputs still under discussion carry a lot.",
                "**How much later work would a change undo?** If a change means moving a few desks, the overlap is cheap to get wrong. If it means re-pouring foundations or rewriting interfaces, it is expensive.",
            ),
            "Research on product development supports this caution. Krishnan, Eppinger and Whitney (*Management Science*, 1997) note that overlapping interrelated activities can speed development, but without careful management can increase effort and cost and reduce quality; their framework sets out the conditions under which different kinds of overlap are appropriate rather than recommending maximum overlap.",
            TIP("Overlap by deliverable, not by calendar. \"Start installation in zones where cabling has been tested\" gives the later team a stable input; \"start installation three days early\" does not."),
        ),
        S(
            "How crashing works",
            "Crashing shortens an activity by applying more resources to it. To compare crashing options fairly, calculate the **crash cost slope**, the extra cost of each time unit saved:",
            "**Crash cost slope = (crash cost − normal cost) ÷ (normal duration − crash duration)**",
            L(
                "**Normal cost** and **crash cost** are the activity's direct costs, in currency, at its normal and fully crashed durations.",
                "**Normal duration** and **crash duration** are in the same time unit, here working days. The crash duration is the **crash point**: the shortest duration the activity can reach however many resources are added.",
                "The result is in currency per time unit, for example dollars per day saved.",
            ),
            "The formula assumes that cost rises in a straight line between the normal and crash points. In practice the first day saved is often cheap (some overtime) and the last is expensive (a second crew, premium delivery), so ask for quotes for each step where the amounts are large.",
            "Crashing suits work that can be divided among more people or speeded up with better equipment: installation, data entry, testing that can run in parallel, manufacturing with spare capacity. It suits poorly work that depends on a few people's knowledge or on a fixed physical process. New people need onboarding and coordination, which is the point of Fred Brooks's observation in *The Mythical Man-Month* (1975) that \"adding manpower to a late software project makes it later\". Crash the cheapest critical activity first, one step at a time, and recalculate the critical path after each step.",
        ),
        S(
            "Worked example: refurbishing an ICT suite before term starts",
            "This example is **illustrative**: the school, costs and probabilities are hypothetical. A school is refurbishing its ICT suite during the summer break. The contractor's schedule is 14 working days, but the pupils return in 11 working days. Each working day the suite is not ready, the school must hire a temporary mobile ICT classroom at **$2,500 per day**. The project manager needs to recover 3 days.",
            T(
                ["ID", "Activity", "Predecessors", "Normal days", "Normal cost", "Crash days", "Crash cost", "Crash cost slope"],
                ["A", "Strip out and survey", "-", "3", "$6,000", "2", "$9,000", "$3,000/day"],
                ["B", "Install and test data cabling", "A", "4", "$8,000", "3", "$10,000", "$2,000/day"],
                ["C", "Image and configure PCs off site", "A", "3", "$4,500", "2", "$5,500", "$1,000/day"],
                ["D", "Install furniture and PCs", "B", "5", "$10,000", "3", "$13,000", "$1,500/day"],
                ["E", "Deliver configured PCs", "C", "2", "$2,000", "2", "-", "Cannot crash"],
                ["F", "Test and hand over", "D, E", "2", "$4,000", "2", "-", "Cannot crash"],
            ),
            "Two paths run through the network: **A-B-D-F = 3 + 4 + 5 + 2 = 14 days** (critical) and **A-C-E-F = 3 + 3 + 2 + 2 = 10 days** (4 days of total float). C has the cheapest crash cost slope, but it is not critical, so crashing it would buy nothing. Doing nothing costs 3 days × $2,500 = **$7,500** in classroom hire.",
            H3("Option 1: crash only"),
            T(
                ["Step", "Action", "Cost of step", "Paths (A-B-D-F / A-C-E-F)", "Cumulative cost"],
                ["0", "Normal schedule", "-", "14 / 10", "$0"],
                ["1", "Crash D by 1 day (cheapest critical activity)", "$1,500", "13 / 10", "$1,500"],
                ["2", "Crash D by 1 more day (D now at its crash point)", "$1,500", "12 / 10", "$3,000"],
                ["3", "Crash B by 1 day (next cheapest)", "$2,000", "11 / 10", "$5,000"],
            ),
            "The target is met for **$5,000** of extra direct cost, with fairly little uncertainty. The other path now has only 1 day of float. A fourth day could be bought by crashing A for $3,000, which shortens both paths because A is on both, but it is not needed.",
            H3("Option 2: fast track only"),
            "Normally installation (D) starts on day 8, after all cabling is installed and tested at the end of day 7. If D starts in zones where cabling is already finished, the B→D link becomes FS with a 3-day lead (FS-3d): installation starts on **day 5**, D finishes at the end of day 9 and handover finishes at the end of **day 11**. No direct cost is added.",
            "The risk is that cabling tests in later zones fail or the cable routes change, so desks and PCs already installed must be moved. With three days of overlap, cabling in most of the room is still unfinished when installation starts. The project manager and the contractor estimate a **40% probability** of rework costing **$4,000** and adding **2 days**.",
            H3("Option 3: crash a little, fast track a little"),
            "Crash D by 1 day with a second installation crew ($1,500), and overlap B and D by only 2 days (FS-2d), installing only in zones whose cabling has passed testing. D starts on day 6, takes 4 days and finishes at the end of day 9; handover finishes at the end of day 11. Because less of the room is unfinished when installation starts, the estimated rework risk falls to a **15% probability** of **$2,000** and **1 day** of delay.",
        ),
        S(
            "Comparing the options on risk-adjusted cost",
            "Fast tracking looks free and crashing looks expensive until the risk is costed. **Expected monetary value (EMV)** puts both on the same scale:",
            "**EMV of rework = P × (rework cost + delay days × daily late cost)**",
            L(
                "**P** is the probability that rework is needed, as a decimal (0.40 for 40%).",
                "**Rework cost** is the direct cost of redoing work, in dollars.",
                "**Delay days** is the extra working days the rework adds beyond the target; **daily late cost** is $2,500 per day here.",
                "**Expected total cost** = direct compression cost + EMV of rework. **Worst case** = direct cost + full rework impact.",
            ),
            "Substituting the figures:",
            L(
                "**Crash only:** EMV of rework = $0 (no overlap). Expected total = **$5,000**; worst case $5,000.",
                "**Fast track only:** impact = $4,000 + 2 × $2,500 = $9,000; EMV = 0.40 × $9,000 = $3,600. Expected total = $0 + $3,600 = **$3,600**; worst case $9,000.",
                "**Crash and fast track:** impact = $2,000 + 1 × $2,500 = $4,500; EMV = 0.15 × $4,500 = $675. Expected total = $1,500 + $675 = **$2,175**; worst case $1,500 + $4,500 = $6,000.",
            ),
            T(
                ["Option", "Planned finish", "Direct cost", "EMV of rework", "Expected total", "Worst case", "Expected saving vs doing nothing ($7,500)"],
                ["Crash only", "Day 11", "$5,000", "$0", "$5,000", "$5,000", "$2,500"],
                ["Fast track only", "Day 11", "$0", "$3,600", "$3,600", "$9,000", "$3,900"],
                ["Crash and fast track", "Day 11", "$1,500", "$675", "$2,175", "$6,000", "$5,325"],
            ),
            H3("Break-even rework probability"),
            "Because the probabilities are judgements, test how wrong they can be before the decision changes. Fast tracking alone costs less than crashing alone in expectation while P × $9,000 < $5,000, so the **break-even probability** is $5,000 ÷ $9,000 = **0.56 (56%)**. For the blended option, $1,500 + P × $4,500 < $5,000 gives P < $3,500 ÷ $4,500 = **0.78 (78%)**.",
            H3("Interpreting the result"),
            "The blended option has the lowest expected cost, and its worst case ($6,000) is still cheaper than doing nothing. Fast tracking alone has a lower expected cost than crashing, but in the 40% case it costs $9,000 and the suite opens two days late, which is worse than doing nothing. Crashing alone is the most expensive in expectation but the only option with a certain outcome.",
            "What the project manager should do: recommend option 3 to the sponsor, with option 1 as the alternative if the school cannot accept any chance of a late start. Make the overlap conditional on a clear rule (\"install only in zones with passed cable tests\"), record the rework risk with an owner in the [risk register](" + P + "risk-register/), and monitor the A-C-E-F path, which has only 1 day of float in all three options.",
            "**Limitations.** EMV is a long-run average; on a single project you get either the full rework impact or none of it, so a sponsor with low risk tolerance may rightly prefer the certain option. The probabilities and impacts are estimates, which is why the break-even check matters. The comparison also leaves out non-monetary effects, such as pupils losing ICT lessons, and treats the crash cost as certain, although crews may be unavailable or quotes may overrun. For schedules with many uncertain activities, a [Monte Carlo simulation](" + P + "monte-carlo-simulation/) gives a fuller picture than single-point EMV.",
        ),
        S(
            "How to choose between fast tracking and crashing",
            "The two questions from the fast-tracking section, how likely the earlier output is to change and how much later work a change would undo, map directly onto the two parts of the EMV calculation: probability and impact. Crossing them gives a quick screen before any detailed costing:",
            T(
                ["", "Rework would be cheap and quick", "Rework would be expensive or long"],
                ["Earlier output approved and stable (low probability of change)", "**Fast track.** Little direct cost and little exposure", "**Fast track with a short, conditional overlap**, or blend with some crashing; cost the worst case"],
                ["Earlier output still changing (high probability of change)", "**Blend.** Crash a little so the overlap can be shorter, or overlap only the parts that are already stable", "**Crash, or do not compress.** Overlap is a poor bet; if crashing is too costly, negotiate the date or scope through change control"],
            ),
            "Crashing still has to pass its own test: the work must be divisible or genuinely faster with more resources, and the people, crews or equipment must be available on the dates needed. If neither technique passes, the gap has to be closed in another way.",
            "Three decision rules follow from the example:",
            OL(
                "Cost the risk before choosing. A fast-tracking option with no direct cost is not free if rework is likely and expensive.",
                "Look for the blend. A little crashing often lets you overlap less, which reduces both the probability and the impact of rework.",
                "Match the option to the sponsor's risk tolerance, not only to the lowest expected cost, and show the worst case alongside the expected value.",
            ),
            "The common rule of thumb \"fast track first, because it is cheaper\" holds only when the overlap is on stable inputs. Many recovery plans start with cheaper options than either technique, such as shortening approval cycles or removing waiting time; the [schedule compression](" + P + "schedule-compression/) guide lists them.",
        ),
        S(
            "Effects both techniques share",
            L(
                "**Float disappears.** Every day taken off the critical path reduces the float on other paths. In the example, A-C-E-F goes from 4 days of float to 1. Recalculate with a [forward and backward pass](" + P + "forward-and-backward-pass/) after each change and watch near-critical paths, not just the critical one.",
                "**More paths converge on the finish.** When several paths are close to critical, the chance that at least one of them slips rises. Monte Carlo simulation shows this effect, known as merge bias; a deterministic critical path does not.",
                "**Resource peaks appear.** Overlapping activities need their resources at the same time, and crashing concentrates resources on fewer activities. Check the resource histogram; if the compressed plan over-allocates people, [resource levelling](" + P + "resource-leveling/) may push dates back out.",
                "**Coordination load rises.** More parallel work means more handoffs and interfaces. Toste-Karayan's PMI Global Congress paper on managing crashed and fast-tracked projects (2005) stresses frequent, detailed communication, securing handoffs and resources in advance, and protecting time for quality testing.",
            ),
        ),
        S(
            "Recording and approving the decision",
            "Compression changes cost, risk and the schedule, so it is a decision for the sponsor, supported by the project manager's analysis. Present each option with its finish date, direct cost, expected and worst-case cost, main risks and the cost of doing nothing, as in the comparison table above.",
            OL(
                "Update the schedule with the approved leads and crashed durations in your [critical path template](/templates/critical-path-template/) or scheduling tool, and check the new critical path.",
                "Record the new risks, such as rework from overlap or crew availability for crashing, with owners and responses in the [risk register template](/templates/risk-register-template/).",
                "Raise a [change request](/templates/change-request-template/) for the extra cost and revised dates, and approve it through [change control](" + P + "change-control/).",
                "Update the [project baseline](" + P + "project-baseline/) once approved, so that later variance is measured against the compressed plan.",
            ),
            "Read our guide to [float and slack](" + P + "float-and-slack/) to understand how much flexibility remains on each path after compression.",
        ),
        S(
            "Common mistakes when fast tracking or crashing",
            L(
                "**Compressing non-critical activities** because they are cheap or easy to speed up. The finish date does not move.",
                "**Overlapping mandatory dependencies**, such as testing before code is written or occupying a building before certification.",
                "**Treating fast tracking as free.** The rework cost appears later, often in a different budget line, so nobody connects it to the decision.",
                "**Crashing with people who cannot start productive work at once.** Onboarding and coordination absorb part or all of the saving.",
                "**Using a straight-line crash cost slope for large steps** without checking real quotes.",
                "**Not recalculating after each step**, and missing a path that has become critical.",
                "**Calling a scope cut compression.** Removing deliverables is a scope change and needs approval as one.",
                "**Leaving the risk out of the comparison**, so the sponsor chooses between a priced option and an apparently free one.",
            ),
            "In Agile delivery, where sprints are fixed time-boxes, the closest equivalents are reprioritising the backlog (a scope decision) and [swarming](/project-management/agile/agile-swarming/) on the highest-priority item; adding people mid-release behaves like crashing and carries the same onboarding cost.",
        ),
    ],
    faq=[
        ("What is the difference between fast tracking and crashing?", "Fast tracking overlaps activities that were planned in sequence, so it mainly adds risk of rework. Crashing adds resources to critical activities to shorten them, so it mainly adds cost. Both shorten the schedule without reducing scope."),
        ("Which is better, crashing or fast tracking?", "Neither in general. Compare them on risk-adjusted cost: the certain cost of crashing against the probability of rework multiplied by its cost and delay. Stable inputs and cheap rework favour fast tracking; unstable inputs, expensive rework or a sponsor who needs certainty favour crashing."),
        ("Does fast tracking increase cost?", "Not directly, but rework caused by building on inputs that later change can add cost and delay. It can also add coordination effort and create resource peaks when activities run at the same time."),
        ("How do you calculate crash cost per day?", "Crash cost slope = (crash cost − normal cost) ÷ (normal duration − crash duration). For example, an activity crashed from 5 to 3 days with its cost rising from $10,000 to $13,000 costs $3,000 ÷ 2 = $1,500 per day saved."),
        ("Can you use fast tracking and crashing together?", "Yes, and it is often the best option. A small amount of crashing can let you overlap less, which lowers both the probability and the impact of rework."),
        ("Which dependencies can be fast tracked?", "Only discretionary (soft) dependencies, which reflect preference or good practice. Mandatory dependencies based on physical, legal or contractual rules cannot be overlapped."),
        ("What is the crash point of an activity?", "The shortest duration the activity can reach however many resources are added. Beyond it, extra money buys no more time."),
        ("Why should you only crash or fast track critical activities?", "Only the critical path determines the finish date. Shortening an activity with float adds to its float and leaves the finish date unchanged."),
        ("Is reducing scope a form of fast tracking or crashing?", "No. Both techniques keep scope the same. Reducing scope changes the deliverables and needs approval through change control."),
    ],
)
