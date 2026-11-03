from core import S, L, OL, T, TIP, H3

URL = "/project-management/project-network-diagram/"

RW = dict(
    title="Project Network Diagram: Types, Examples and How to Draw",
    desc="Project network diagram explained: AON vs AOA, node notation, dummy activities, a step-by-step method and fully worked examples with the critical path.",
    intro=(
        "A project network diagram is a picture of a project's activities and the dependencies between them, "
        "drawn as boxes or circles joined by arrows from start to finish. It shows the logical order of the work, "
        "and it is the basis for the forward and backward pass, float and the critical path. This guide explains "
        "the two types, the notation, how to draw one step by step and three fully worked examples."
    ),
    takeaways=[
        "A network diagram shows the logic of a schedule: which activities depend on which, and which can run in parallel.",
        "Activity on node (AON), also called the precedence diagramming method, is the modern standard and supports all four dependency types.",
        "Activity on arrow (AOA) puts activities on the arrows, allows only finish-to-start links and sometimes needs dummy activities.",
        "Each AON node can show ES, duration and EF on top and LS, total float and LF underneath, so the critical path is visible at a glance.",
        "Burst points spread work into parallel paths; merge points are where delays combine and deserve the closest watching.",
        "Check the logic before you trust the dates: one start, one finish, no loops and no activities without a predecessor or successor.",
    ],
    sections=[
        S(
            "What is a project network diagram?",
            "A **project network diagram** is a graphical representation of the activities in a project and the "
            "logical relationships between them. Activities are shown as nodes or arrows, dependencies as connecting "
            "arrows, and the whole diagram flows from a single start to a single finish. It is used to check logic, "
            "calculate dates and float, and find the critical path.",
            "You may also see it called an **activity network diagram**, a **logic diagram** or a **precedence "
            "diagram**. The PMBOK Guide 6th edition called it the **project schedule network diagram** and made it "
            "the main output of sequencing activities. Later editions are organised around principles and "
            "performance domains rather than processes, but the technique itself has not changed.",
            H3("Where it fits in planning"),
            "A network diagram sits between breaking down the work and setting dates:",
            OL(
                "Break the scope into deliverables with a [work breakdown structure](/project-management/work-breakdown-structure/).",
                "Turn the lowest-level work packages into [activities](/project-management/project-tasks-and-activities/).",
                "Sequence the activities with [task dependencies](/project-management/task-dependencies/): this is where the network diagram is drawn.",
                "Estimate a duration for each activity.",
                "Run the [forward and backward pass](/project-management/forward-and-backward-pass/) on the network to get dates, [float](/project-management/float-and-slack/) and the critical path.",
                "Show the result on a [Gantt chart](/project-management/gantt-chart/) and save a [baseline](/project-management/project-baseline/).",
            ),
            "The diagram shows **logic**, not calendar time. A long box does not mean a long activity, and two "
            "nodes side by side do not have to happen at the same time. For dates against a calendar, you need the "
            "Gantt chart; for the reasons behind those dates, you need the network.",
            "Network diagrams date from the late 1950s, when the critical path method was developed for DuPont and "
            "PERT for the US Navy. Both originally drew activities on arrows. The activity-on-node approach, "
            "published by John Fondahl in the early 1960s, became the basis for the precedence diagramming method "
            "used by almost all scheduling software today.",
        ),
        S(
            "Network diagram notation and components",
            T(
                ["Component", "What it is", "How it is drawn (AON)"],
                ["Activity", "A piece of work with a duration", "A box (node) with an ID and name"],
                ["Dependency", "A logical link between two activities", "An arrow from predecessor to successor"],
                ["Start and finish nodes", "Single entry and exit points for the network", "Zero-duration nodes or milestones at each end"],
                ["Milestone", "A significant point with zero duration", "A node with duration 0, often a diamond"],
                ["Path", "Any continuous chain of activities from start to finish", "Follow the arrows"],
                ["Critical path", "The longest path; it sets the project duration and has the lowest float", "Bold or red arrows and nodes"],
                ["Burst point", "An activity with two or more successors", "One node with several outgoing arrows"],
                ["Merge point", "An activity with two or more predecessors", "One node with several incoming arrows"],
                ["Lead or lag", "An overlap or delay on a link", "A label on the arrow, such as FS+3 or SS-2"],
                ["Dummy activity", "A zero-duration link used only in AOA diagrams", "A dashed arrow"],
            ),
            "Our guide to [predecessors and successors](/project-management/predecessors-and-successors/) explains "
            "the terms used on each side of an arrow, and [project milestones](/project-management/project-milestones/) "
            "covers how to choose them.",
            H3("The AON node box"),
            "On an activity-on-node diagram, each box usually holds seven values once the forward and backward pass "
            "are done. A common layout is:",
            T(
                ["Position", "Left", "Centre", "Right"],
                ["Top row", "Early start (ES)", "Duration", "Early finish (EF)"],
                ["Middle", "", "Activity ID and name", ""],
                ["Bottom row", "Late start (LS)", "Total float (TF)", "Late finish (LF)"],
            ),
            "For example, activity C in the worked example below reads **ES 3 | 2 | EF 5** on top, **C Book "
            "removal firm** in the middle and **LS 7 | TF 4 | LF 9** underneath. Layouts vary between textbooks and "
            "tools, so always include a key on the diagram.",
        ),
        S(
            "Types of network diagram: AON vs AOA",
            T(
                ["", "Activity on node (AON)", "Activity on arrow (AOA)"],
                ["Activities shown as", "Boxes (nodes)", "Arrows"],
                ["Nodes represent", "Activities", "Events: the start or end of activities"],
                ["Dependency types", "FS, SS, FF and SF, with leads and lags", "Finish-to-start only"],
                ["Dummy activities", "Never needed", "Sometimes needed to show logic correctly"],
                ["Also called", "Precedence diagramming method (PDM)", "Arrow diagramming method (ADM)"],
                ["Where you see it", "All modern scheduling tools; PMP exam questions", "Older textbooks, some PERT and university courses"],
            ),
            H3("Activity on node (precedence diagramming method)"),
            "In AON, every activity is a node and every arrow is a dependency. Because the logic sits on the arrows, "
            "you can show all four dependency types and label any lead or lag. Adding an activity or a link never "
            "needs extra dummy arrows, which makes AON easier to draw, read and change. This guide uses AON unless "
            "it says otherwise.",
            H3("Activity on arrow (arrow diagramming method)"),
            "In AOA, each activity is an arrow running between two numbered circles called **events** or nodes. An "
            "event is the moment when all arrows entering it are complete and those leaving it can start. Two rules "
            "apply: events are numbered so that every arrow runs from a lower to a higher number, and no two "
            "activities may share the same start and end event. Event times are usually written in the circles: "
            "earliest event time and latest event time.",
            H3("Dummy activities"),
            "A dummy is a dashed arrow with zero duration and no resources. It is needed in AOA in two situations: "
            "to show a dependency that cannot be drawn with real activities alone, and to stop two activities "
            "sharing the same pair of events. **Illustrative example:**",
            T(
                ["Activity", "Duration (days)", "Predecessors"],
                ["P", "2", "-"],
                ["Q", "3", "-"],
                ["R", "4", "P, Q"],
                ["S", "1", "Q"],
            ),
            "R needs both P and Q, but S needs only Q. In AOA, draw P from event 1 to event 2 and Q from event 1 to "
            "event 3. R leaves event 2, so it would wait only for P. Add a **dummy from event 3 to event 2**: now "
            "event 2 is not reached until Q is also done, so R waits for both, while S leaves event 3 and waits "
            "only for Q. R and S both end at event 4. In AON none of this is needed: you simply draw arrows "
            "P→R, Q→R and Q→S.",
            H3("Related diagrams"),
            L(
                "**PERT chart:** a network diagram, usually AOA in its original form, that uses three-point duration estimates. See our [PERT chart guide](/project-management/pert-chart/).",
                "**Time-scaled network diagram:** nodes or arrows placed against a time axis, so the diagram shows both logic and timing. It is close to a Gantt chart with links.",
            ),
        ),
        S(
            "Showing dependency types and lags on the diagram",
            "In AON, the default arrow means finish-to-start with no lag. Anything else should be labelled on the "
            "arrow, and the arrow should leave and enter the side of the box the link refers to (the start is the "
            "left edge, the finish the right edge).",
            T(
                ["Link", "Meaning", "How to draw and label", "Example"],
                ["Finish-to-start (FS)", "Successor starts after predecessor finishes", "Right edge to left edge; no label needed", "Pack boxes, then move"],
                ["FS with lag", "Delay after the finish", "Right to left, labelled FS+3", "Pour concrete, wait 3 days to cure, then build"],
                ["Start-to-start (SS)", "Successor starts after predecessor starts", "Left edge to left edge, labelled SS or SS+2", "Start electrics 2 days after partitions start"],
                ["Finish-to-finish (FF)", "Successor finishes after predecessor finishes", "Right edge to right edge, labelled FF or FF+1", "Finish electrics a day after partitions finish"],
                ["Start-to-finish (SF)", "Successor finishes after predecessor starts", "Left edge to right edge, labelled SF", "Old system runs until the new one starts"],
                ["FS with lead", "Overlap before the finish", "Right to left, labelled FS-2", "Start testing 2 days before the build ends"],
            ),
            "Most networks are almost entirely finish-to-start, and quality checks expect that (see below). Use SS "
            "and FF where the work genuinely overlaps, and record why. Our guide to [leads and lags](/project-management/leads-and-lags/) "
            "covers when each is justified, and the [forward and backward pass](/project-management/forward-and-backward-pass/) "
            "guide works through an office fit-out network with SS, FF and lag links.",
        ),
        S(
            "How to draw a project network diagram step by step",
            OL(
                "**List the activities.** Take them from the lowest level of the WBS. Each should have an ID, a short verb-noun name and a clear finish. Our [work breakdown structure template](/templates/work-breakdown-structure-template/) helps if you are starting from scratch.",
                "**Record the predecessors** of each activity in a table. Ask \"what must be finished before this can start?\" rather than \"what comes next?\", and note any SS, FF or SF links, leads and lags.",
                "**Add a Start node** on the left. Every activity with no predecessor connects to it.",
                "**Place activities in columns** from left to right. An activity goes in the column after the latest of its predecessors, so the diagram reads in time order.",
                "**Draw an arrow for every dependency**, labelling any link that is not a plain finish-to-start.",
                "**Add a Finish node** on the right. Every activity with no successor connects to it.",
                "**Check the logic**: one start, one finish, no loops, no dangling activities and no redundant links (if A→B→C exists, a direct A→C arrow adds nothing).",
                "**Add durations** to each node.",
                "**Run the forward pass** to fill in ES and EF, then the **backward pass** for LS and LF, and calculate total float.",
                "**Highlight the critical path**: the chain of activities with zero (or the lowest) total float.",
                "**Review the diagram with the team** who will do the work. They will spot missing links and impossible sequences faster than anyone.",
            ),
            TIP("Draw the first version with sticky notes, one per activity. Moving notes is quicker than "
                "redrawing, and it gets the team involved in the logic."),
            "Free template: the [critical path template](/templates/critical-path-template/) records activities, "
            "durations and predecessors and calculates early and late dates and float, so you can check your "
            "diagram against it.",
        ),
        S(
            "Worked example 1: a six-activity office move",
            "This illustrative network is the same six-activity network used in our "
            "[forward and backward pass](/project-management/forward-and-backward-pass/) and "
            "[float and slack](/project-management/float-and-slack/) guides, so you can follow the same numbers "
            "across all three. Here the activities are named for a small office move. Durations are in working "
            "days and all links are finish-to-start.",
            H3("Step 1: activity list"),
            T(
                ["ID", "Activity", "Duration (days)", "Predecessors"],
                ["A", "Agree move plan and layout", "3", "-"],
                ["B", "Fit out new office", "4", "A"],
                ["C", "Book removal firm", "2", "A"],
                ["D", "Install IT and network", "5", "B"],
                ["E", "Pack and label", "3", "C"],
                ["F", "Move and unpack", "2", "D, E"],
            ),
            H3("Step 2: place the nodes and draw the arrows"),
            T(
                ["Column", "Nodes", "Arrows leaving this column"],
                ["0", "Start", "Start → A"],
                ["1", "A", "A → B, A → C (A is a burst point)"],
                ["2", "B, C", "B → D, C → E"],
                ["3", "D, E", "D → F, E → F"],
                ["4", "F (a merge point)", "F → Finish"],
                ["5", "Finish", "-"],
            ),
            "Put B and D on the top row and C and E on the bottom row, so that the two parallel paths are easy to "
            "see and no arrows cross.",
            H3("Step 3: list the paths"),
            "For a small network, listing every path from start to finish is a quick way to find the critical path "
            "before doing any date calculations:",
            T(
                ["Path", "Durations", "Length", "Path float"],
                ["A-B-D-F", "3 + 4 + 5 + 2", "14 days", "0 (critical)"],
                ["A-C-E-F", "3 + 2 + 3 + 2", "10 days", "14 - 10 = 4"],
            ),
            H3("Step 4: fill in the nodes"),
            "The forward and backward pass (day-0 convention) give these node values:",
            T(
                ["Node", "ES", "Duration", "EF", "LS", "Total float", "LF", "Free float"],
                ["A Agree move plan", "0", "3", "3", "0", "0", "3", "0"],
                ["B Fit out new office", "3", "4", "7", "3", "0", "7", "0"],
                ["C Book removal firm", "3", "2", "5", "7", "4", "9", "0"],
                ["D Install IT and network", "7", "5", "12", "7", "0", "12", "0"],
                ["E Pack and label", "5", "3", "8", "9", "4", "12", "4"],
                ["F Move and unpack", "12", "2", "14", "12", "0", "14", "0"],
            ),
            H3("Step 5: read the diagram"),
            L(
                "**Critical path: A-B-D-F, 14 days.** Highlight these four nodes and their arrows. Any delay to them delays the move.",
                "**C and E share 4 days of float.** C has no free float, so a slip in C pushes E later; E has 4 days of free float because F cannot start until day 12.",
                "**A is a burst point.** A late move plan delays both paths at once.",
                "**F is a merge point.** It needs both the IT installation and the packing. If either path slips beyond its float, the move slips.",
            ),
            H3("Step 6: the same network as activity on arrow"),
            "Drawn as AOA, the six activities become arrows between six events. No dummy is needed because no two "
            "activities share the same pair of events and every dependency can be drawn directly.",
            T(
                ["Arrow", "From event", "To event", "Duration"],
                ["A", "1", "2", "3"],
                ["B", "2", "3", "4"],
                ["C", "2", "4", "2"],
                ["D", "3", "5", "5"],
                ["E", "4", "5", "3"],
                ["F", "5", "6", "2"],
            ),
            "The earliest and latest event times are: event 1, 0 and 0; event 2, 3 and 3; event 3, 7 and 7; event 4, "
            "5 and 9; event 5, 12 and 12; event 6, 14 and 14. Events with equal earliest and latest times lie on "
            "the critical path, and the gap of 4 at event 4 is the float on the C-E path. See our "
            "[forward and backward pass](/project-management/forward-and-backward-pass/) guide for every step of the "
            "calculation.",
        ),
        S(
            "Worked example 2: a nine-activity website relaunch",
            "This illustrative example uses the website relaunch network from our "
            "[float and slack](/project-management/float-and-slack/) guide. It has three parallel paths, two merge "
            "points and a near-critical path.",
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
            H3("Drawing it"),
            L(
                "**Column 1:** A, a burst point with three successors (B, C and F).",
                "**Column 2:** B, C and F, stacked so that the design path is on top, content in the middle and back end at the bottom.",
                "**Column 3:** E (after B) and D (after C). F has no successor until H, so its arrow runs across to column 5.",
                "**Column 4:** G, a merge point for D and E.",
                "**Column 5:** H, a merge point for G and F.",
                "**Column 6:** I, then Finish.",
            ),
            H3("Paths and float"),
            T(
                ["Path", "Durations", "Length", "Path float"],
                ["A-B-E-G-H-I", "4 + 6 + 8 + 3 + 5 + 1", "27 days", "0 (critical)"],
                ["A-C-D-G-H-I", "4 + 7 + 2 + 3 + 5 + 1", "22 days", "5"],
                ["A-F-H-I", "4 + 10 + 5 + 1", "20 days", "7"],
            ),
            "The critical path runs through design and front-end build. The content path is **near-critical** with "
            "5 days of float: in the float guide, a 6-day slip in content writing switches the critical path to "
            "A-C-D-G-H-I and moves the launch to day 28. Mark it in a second colour on the diagram.",
            "The two merge points, G and H, are where most schedule risk collects. If you want to recover time, "
            "the diagram also shows where not to look: shortening back-end integration (F) cannot bring the launch "
            "forward, because it has 7 days of float. See [schedule compression](/project-management/schedule-compression/) "
            "for how to choose which critical activities to shorten.",
        ),
        S(
            "How to read a network diagram",
            "Once the diagram is drawn and the nodes are filled in, look for five things:",
            OL(
                "**The critical path.** The chain of zero-float activities sets the end date. Focus management attention here.",
                "**Near-critical paths.** Paths with only a few days of float can become critical after one bad week. Many teams set a threshold, such as 5 or 10 days, and track these paths as closely as the critical path.",
                "**Merge points.** When several paths join, the activity can only start when the latest one finishes. The more paths that merge, the more likely at least one is late, an effect often called merge bias. Consider a buffer or earlier start for the paths that feed big merge points.",
                "**Burst points.** A delay in a burst activity hits every path that leaves it. Protect them with clear ownership and early starts.",
                "**Parallel work and resources.** Activities side by side in the same column can run at the same time, but only if people are available. If the same person is needed on both, you will have to [level resources](/project-management/resource-leveling/), which can change the critical path.",
            ),
            "For a schedule with significant uncertainty, a [Monte Carlo simulation](/project-management/monte-carlo-simulation/) "
            "on the same network shows how often each path ends up critical, which is a better guide to risk than a "
            "single set of float values.",
        ),
        S(
            "Network diagram vs Gantt chart, PERT chart and WBS",
            T(
                ["", "Network diagram", "Gantt chart", "PERT chart", "WBS"],
                ["Shows", "Logic and flow of activities", "Activities as bars against a calendar", "Logic with three-point time estimates", "Hierarchy of deliverables and work"],
                ["Time scale", "None (unless time-scaled)", "Yes", "None", "None"],
                ["Dependencies", "Central", "Shown as links between bars", "Central", "Not shown"],
                ["Best for", "Building and checking logic, finding the critical path", "Communicating dates and tracking progress", "Estimating duration under uncertainty", "Defining scope"],
                ["Weakness", "Hard to read with hundreds of activities", "Logic is harder to check", "More estimating effort", "Says nothing about sequence"],
            ),
            "In practice you use them together: the WBS defines the work, the network sets the logic and the Gantt "
            "chart communicates the dates. Read our guide to [project scheduling](/project-management/project-scheduling/) to see how the pieces fit "
            "together.",
        ),
        S(
            "Checking the logic: schedule quality tests",
            "A network diagram is only as good as its logic. Missing or wrong links produce wrong dates and "
            "misleading float. Several of the checks in the DCMA 14-point schedule assessment, widely used on US "
            "defence and government projects, test the logic directly:",
            T(
                ["Check", "What it looks for", "Threshold"],
                ["Logic", "Incomplete activities missing a predecessor or successor", "No more than 5%"],
                ["Leads", "Links with negative lag", "None (0%)"],
                ["Lags", "Links with positive lag", "No more than 5% of links"],
                ["Relationship types", "Share of finish-to-start links", "At least 90%"],
                ["Hard constraints", "Activities with fixed dates instead of logic", "No more than 5%"],
                ["High float", "Incomplete activities with total float above 44 working days", "Flagged for review"],
            ),
            "You do not need to work on a government contract to use these checks. They catch the most common "
            "problems in any network:",
            L(
                "**Loops:** A depends on B, which depends on A. Scheduling tools reject them, but they appear on hand-drawn diagrams.",
                "**Dangling activities:** an activity with no successor gets its late dates from the project finish, so its float looks far larger than it really is.",
                "**Constraints instead of links:** a fixed date overrides the logic and hides the real driver.",
                "**Too many leads and lags:** each one is an assumption that is easy to forget and hard to update.",
            ),
            "Our guide to [float and slack](/project-management/float-and-slack/) explains how unusually high float "
            "usually points to missing logic.",
        ),
        S(
            "Network diagrams in software",
            "Most scheduling tools build the network from the dependencies you enter, so you rarely draw a large "
            "diagram by hand.",
            L(
                "**Microsoft Project** (desktop) has a dedicated Network Diagram view under View > Network Diagram. Format > Layout controls box arrangement and spacing, Format > Box Styles controls what each box shows, and link labels can display the dependency type and any lead or lag.",
                "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool, shows dependencies and the critical path on its interactive Gantt charts from the Team plan upwards, with all four dependency types, lead and lag time, float and baselines.",
                "**[ClickUp](/project-management-tools/clickup/)** Gantt charts support all four dependency types and show the critical path and slack time.",
                "**[Smartsheet](/project-management-tools/smartsheet/)** lets you set dependencies between rows and identify the critical path on its Gantt chart, which suits date-driven projects.",
                "**[Microsoft Planner](/project-management-tools/microsoft-planner/)** premium plans include dependencies, and Plan 3 adds baselines and the critical path.",
            ),
            "Many tools show the logic as links on the Gantt chart rather than as a separate network view; filter "
            "it to the critical and near-critical paths when checking a new schedule. The "
            "[project schedule template](/templates/project-schedule-template/) is a simple starting point if you "
            "work in a spreadsheet.",
        ),
        S(
            "Common network diagram mistakes",
            L(
                "**Drawing the sequence you expect rather than the logic.** Only link activities that genuinely depend on each other; everything else can run in parallel.",
                "**Several start or finish points.** Connect every open start to a Start node and every open end to a Finish node.",
                "**Missing links.** An activity with no successor shows false float and can hide the real critical path.",
                "**Redundant links.** If A→B→C exists, a direct A→C arrow clutters the diagram without adding logic.",
                "**Unlabelled SS, FF or lag links.** Anyone reading the diagram will assume finish-to-start.",
                "**Mixing AON and AOA** in one diagram, or using dummies on an AON diagram.",
                "**Activities that are too large.** A three-month activity hides the dependencies inside it. Break it down until links are clear.",
                "**Using hammocks or summaries as logic.** Link the detailed activities, not summary bars; see our guide to [hammock activities](/project-management/hammock-activity/).",
                "**Not updating the diagram.** When durations, links or deadlines change, recalculate. The critical path can switch.",
            ),
            "Read our guide to the [critical path method](/project-management/critical-path-method/) to see how the "
            "network diagram fits into the full scheduling process.",
        ),
    ],
    faq=[
        ("What is a project network diagram?",
         "A diagram of a project's activities and the dependencies between them, drawn as nodes and arrows from a "
         "single start to a single finish. It shows the logical sequence of the work and is used to find the "
         "critical path."),
        ("What are the two main types of network diagram?",
         "Activity on node (AON), also called the precedence diagramming method, and activity on arrow (AOA), also "
         "called the arrow diagramming method."),
        ("What is the difference between AON and AOA?",
         "In AON, activities are boxes and arrows are dependencies, and all four dependency types can be shown. In "
         "AOA, activities are arrows, nodes are events, only finish-to-start links are possible and dummy "
         "activities are sometimes needed."),
        ("What is the precedence diagramming method?",
         "Another name for activity-on-node diagramming, in which activities are nodes linked by arrows that can "
         "be finish-to-start, start-to-start, finish-to-finish or start-to-finish, with leads and lags."),
        ("What is a dummy activity?",
         "A zero-duration arrow used in activity-on-arrow diagrams to show a dependency that real activities cannot "
         "show, or to stop two activities sharing the same start and end events. AON diagrams never need them."),
        ("What information goes in a network diagram node?",
         "At minimum an ID, name and duration. After the forward and backward pass, nodes usually also show early "
         "start, early finish, late start, late finish and total float."),
        ("What are merge and burst activities?",
         "A merge activity has two or more predecessors, such as F in our office move example. A burst activity has "
         "two or more successors, such as A. Merge points are where delays combine."),
        ("How do you find the critical path on a network diagram?",
         "List every path and add up its durations, or run a forward and backward pass. The longest path, whose "
         "activities have zero total float, is the critical path."),
        ("Is a PERT chart a network diagram?",
         "Yes. A PERT chart is a network diagram that uses three-point duration estimates to allow for "
         "uncertainty."),
        ("What is the difference between a network diagram and a Gantt chart?",
         "A network diagram shows the logic and flow of activities; a Gantt chart shows activities as bars against a "
         "calendar. Most tools build both from the same data."),
        ("Can you draw a network diagram in Excel?",
         "Yes, for small networks, using shapes and connectors, and a spreadsheet can calculate the dates and float. "
         "For larger projects, a scheduling tool that draws the logic automatically is quicker and less error-prone."),
        ("How do you create a network diagram in Microsoft Project?",
         "In Project desktop, enter tasks, durations and predecessors, then choose View > Network Diagram. Use "
         "Format > Layout and Box Styles to arrange the boxes and choose what they display."),
        ("Do I still need a network diagram if my software draws a Gantt chart?",
         "You may not need to draw one by hand, but reviewing the network logic, or the Gantt chart filtered to the "
         "critical path, is still the best way to catch missing links before you commit to dates."),
    ],
)
