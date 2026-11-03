from core import S, L, OL, T, TIP, H3

URL = "/project-management/kanban/kanban-vs-scrumban/"

RW = dict(
    title="Kanban vs Scrumban: Differences, Examples and When to Use Each",
    desc="Kanban vs Scrumban explained: what Scrumban takes from Scrum, how its planning trigger and board work, a worked example, and when to choose each.",
    intro=(
        "Kanban vs Scrumban comes down to how much structure you add to flow: Kanban improves your existing "
        "process with a visual board and WIP limits, and needs no roles or iterations, while Scrumban is a hybrid "
        "that keeps parts of Scrum, such as regular planning, reviews and retrospectives, on top of Kanban's "
        "continuous pull. Scrumban is most useful for Scrum teams whose Sprints keep being disrupted by unplanned "
        "work. This guide explains how Scrumban works, how to set it up step by step, and how to choose."
    ),
    takeaways=[
        "Kanban is a flow method you apply to your current process. Scrumban is a hybrid that adds Scrum-style planning, reviews, retrospectives and often Scrum roles to Kanban flow.",
        "Scrumban replaces the fixed Sprint commitment with planning on demand: the team plans when the Ready column falls to a set trigger point.",
        "Both use WIP limits, pull and flow metrics. The difference is whether Scrum's structure stays in place.",
        "Scrumban was popularised by Corey Ladas in 2009 as a way for Scrum teams to move towards Kanban. It has no official guide.",
        "Choose Scrumban when a Scrum team faces mixed planned and unplanned work; choose Kanban if you do not use Scrum today or your work is almost entirely unplanned.",
    ],
    sections=[
        S("Kanban vs Scrumban: what is the difference?",
          "**The difference between Kanban and Scrumban is where you start and what you keep.** Kanban starts with "
          "your current process and adds a visual board, WIP limits and flow metrics, with no required roles or "
          "iterations. Scrumban usually starts with Scrum and swaps the Sprint commitment for Kanban's continuous "
          "pull, while keeping regular planning, reviews and retrospectives.",
          "In practice, the two can look alike: both use a board with WIP limits and both pull work as capacity "
          "frees up. What sets Scrumban apart is the Scrum scaffolding it keeps. If your team has a Product Owner, "
          "a Scrum Master, a fortnightly review and a planning trigger, it is running Scrumban. If it has none of "
          "those and simply manages flow, it is running Kanban.",
        ),
        S("What is Scrumban?",
          "Scrumban is a hybrid Agile approach that combines Scrum's structure with Kanban's flow. The name was "
          "popularised by Corey Ladas, whose 2009 book *Scrumban: Essays on Kanban Systems for Lean Software "
          "Development* described it as a way for Scrum teams to evolve towards a Kanban system step by step.",
          "Many teams now treat Scrumban as a destination rather than a stepping stone. They like Scrum's rhythm of "
          "planning and reflection but find fixed Sprint commitments a poor fit for work that arrives "
          "unpredictably.",
          "There is no official Scrumban guide in the way the [Scrum Guide](/project-management/scrum/what-is-scrum/) "
          "defines Scrum or the Kanban Guide defines [Kanban](/project-management/kanban/what-is-kanban/). Some "
          "consultancies and tool vendors publish their own Scrumban guides, but each team shapes its own version. "
          "That flexibility is useful, but it also means you need to write down your rules so everyone knows which "
          "parts of Scrum still apply.",
        ),
        S("What Scrumban takes from Scrum and from Kanban",
          T(["Element", "From Scrum", "From Kanban", "Typical Scrumban practice"],
            ["Work selection", "Planning meeting", "Pull when capacity frees up", "Plan on demand when Ready hits a trigger point"],
            ["Time box", "Sprint", "None", "Optional iteration used for rhythm, not commitment"],
            ["Limiting work", "Sprint Backlog size", "Explicit WIP limits", "WIP limits per column"],
            ["Board", "Sprint board", "Persistent board with policies", "Persistent board; not reset each iteration"],
            ["Roles", "Product Owner, Scrum Master, Developers", "None required", "Often kept, especially the Product Owner"],
            ["Daily coordination", "Daily Scrum", "Kanban meeting", "Daily stand-up focused on the board"],
            ["Improvement", "Sprint Retrospective", "Feedback loops and reviews", "Regular retrospective, often every two weeks"],
            ["Stakeholder feedback", "Sprint Review", "Service delivery review", "Regular review of finished work"],
            ["Metrics", "Velocity, burndown", "Throughput, cycle time, work item age", "Mostly flow metrics"],
            ["Estimation", "Often story points", "Optional; right-sizing", "Often reduced or dropped over time"],
          ),
        ),
        S("Kanban vs Scrumban comparison table",
          T(["Aspect", "Kanban", "Scrumban"],
            ["Starting point", "Your current process, whatever it is", "Usually an existing Scrum team"],
            ["Defining source", "Kanban Guide (2025.5) and Kanban University's Kanban Method", "No official guide; Ladas (2009) and team practice"],
            ["Iterations", "None", "Optional, for planning and review rhythm"],
            ["Commitment", "Per item, often a service level expectation", "No Sprint commitment; per-item expectations"],
            ["Planning", "Replenishment as capacity frees up or on a schedule", "Planning on demand, triggered by the Ready column"],
            ["Roles", "None required; optional Service Request Manager and Service Delivery Manager", "Often keeps the Product Owner and Scrum Master"],
            ["Meetings", "Optional cadences chosen by the team", "Usually keeps stand-up, planning, review and retrospective"],
            ["WIP limits", "Core practice", "Core practice"],
            ["Board", "Persistent", "Persistent"],
            ["Estimation", "Optional", "Often keeps story points at first, then drops them"],
            ["Metrics", "Throughput, cycle time, work item age, WIP", "The same, sometimes alongside velocity during transition"],
            ["Change", "Anything not started can be re-prioritised", "Anything not started can be re-prioritised"],
            ["Learning curve", "Low to start; discipline needed to sustain", "Moderate; the team must agree which Scrum rules remain"],
            ["Best for", "Service, support, operations and any team improving its current process", "Scrum teams with a mix of planned and unplanned work"],
          ),
          "The rows that differ are the ones about structure: starting point, iterations, roles, meetings and "
          "planning. The rows about flow are identical, because Scrumban takes its flow mechanics directly from "
          "Kanban.",
        ),
        S("Scrum vs Kanban vs Scrumban at a glance",
          "If you are also considering plain Scrum, this summary places all three side by side:",
          T(["", "Scrum", "Scrumban", "Kanban"],
            ["Cadence", "Fixed Sprints of one month or less", "Optional iterations; continuous flow", "Continuous flow"],
            ["Commitment", "Sprint Goal", "None per batch", "None per batch"],
            ["Planning", "Every Sprint", "On demand", "Replenishment"],
            ["Roles", "Three accountabilities", "Usually kept", "None required"],
            ["WIP limits", "Not required", "Yes", "Yes"],
            ["Main metrics", "Velocity, burndown", "Flow metrics", "Flow metrics"],
          ),
          "See our guide to [Kanban vs Scrum](/project-management/kanban/kanban-vs-scrum/) for a full comparison of "
          "the two parent approaches, with the same team run both ways and a checklist for choosing.",
        ),
        S("How Scrumban works",
          H3("The board and WIP limits"),
          "A Scrumban board is persistent: items move across it continuously and the board is never cleared at the "
          "end of an iteration. Each in-progress column has a [WIP limit](/project-management/kanban/wip-limits/), "
          "and many teams add [swimlanes](/project-management/kanban/kanban-swimlanes/) to separate planned work, "
          "unplanned requests and genuine emergencies.",
          H3("Planning on demand"),
          "Instead of planning a fixed batch at the start of each Sprint, the team keeps a Ready column with a "
          "minimum level, the planning trigger. When Ready drops to that level, the Product Owner and team hold a "
          "short planning session to refill it. Planning happens as often as the team consumes work, not on a fixed "
          "calendar. This is the main mechanism that turns a Scrum team into a [pull system](/project-management/kanban/pull-system-vs-push-system/).",
          H3("Iterations: optional, for rhythm not commitment"),
          "Some Scrumban teams keep two-week iterations so that reviews, retrospectives and reporting happen on a "
          "familiar schedule. The difference from Scrum is that nobody commits to finishing a batch by the end of "
          "the iteration, and unfinished work simply continues. Other teams drop iterations entirely and schedule "
          "each meeting on its own cadence.",
          H3("Meetings"),
          "Most Scrumban teams keep four meetings: a daily stand-up that walks the board from right to left, an "
          "on-demand planning session, a regular review with stakeholders and a regular "
          "[retrospective](/project-management/scrum/sprint-retrospective/). Many also hold "
          "[backlog refinement](/project-management/scrum/backlog-refinement/) so items reaching Ready are small "
          "and clear.",
          H3("Roles"),
          "Scrumban does not mandate roles. Teams moving from Scrum usually keep a Product Owner to order the "
          "backlog and decide what enters Ready. The Scrum Master often becomes a flow coach, watching WIP limits, "
          "blockers and ageing items. Over time, some teams drop the titles and share these responsibilities.",
          H3("Long-range planning: buckets, feature freeze and triage"),
          "Because there is no Sprint plan, Scrumban teams need another way to see further ahead. Three practices "
          "appear in many Scrumban descriptions, though none is formally required:",
          L(
            "**Bucket planning:** ideas sit in time-horizon buckets, such as one year, six months and three months, and move closer as they become concrete enough to plan.",
            "**Feature freeze:** close to a fixed deadline, the team stops adding new features to the release and only finishes what is in progress.",
            "**Triage:** straight after a feature freeze, the team decides which unfinished items will make the deadline and which go back to the backlog.",
          ),
        ),
        S("How to calculate a Scrumban planning trigger",
          "The planning trigger, sometimes called the order point, is the number of items left in Ready that "
          "prompts the next planning session. Set it too low and the team runs out of work; set it too high and "
          "you are back to planning large batches.",
          OL(
            "**Measure throughput.** Count how many items the team finishes per working day on average over the last six to eight weeks. See our guide to [throughput](/project-management/kanban/throughput/).",
            "**Measure planning lead time.** Note how many working days it takes, from deciding to plan, to get new items refined and agreed, including finding time with the Product Owner.",
            "**Multiply the two.** Throughput per day times planning lead time gives the number of items the team will consume while planning is being arranged.",
            "**Add a small safety margin** of one or two items to cover busy weeks.",
            "**Set the Ready limit** above the trigger, so each planning session adds a sensible batch, often about a week's work.",
            "**Write the policy on the board**, for example \"When Ready falls to 4, the Product Owner books planning within two days\".",
            "**Review the trigger monthly.** If Ready empties often, raise it; if planning feels too frequent, raise the Ready limit instead.",
          ),
          H3("Worked example"),
          "**Illustrative figures.** A team finishes 10 items every two weeks, which is 1 item per working day. "
          "Arranging and holding a planning session takes up to 2 working days. Adding a safety margin of 2 gives "
          "a trigger of (1 x 2) + 2 = **4 items**. The team sets the Ready limit at **8**, so each planning session "
          "adds about four items, roughly every four working days.",
          T(["Input", "Value", "Result"],
            ["Throughput", "1 item per working day", ""],
            ["Planning lead time", "2 working days", "2 items consumed while waiting"],
            ["Safety margin", "2 items", ""],
            ["Planning trigger", "", "4 items in Ready"],
            ["Ready limit", "", "8 items"],
            ["Planning frequency", "", "About every 4 working days, adding about 4 items"],
          ),
          "See our [Kanban planning guide](/project-management/kanban/kanban-planning/) for forecasting further "
          "ahead, such as when a whole feature will be finished.",
        ),
        S("Example Scrumban board",
          "Here is an illustrative board for a seven-person team that builds features and handles support "
          "requests:",
          T(["Column", "WIP limit", "Policy for moving in"],
            ["Backlog", "None", "Ordered by the Product Owner; large items split during refinement"],
            ["Ready", "8 (plan at 4)", "Small enough to finish within 7 working days; acceptance criteria agreed"],
            ["In progress", "5", "A person has capacity and nothing is waiting in Review"],
            ["Review", "2", "Code complete, tests written, ready for a peer"],
            ["Test", "3", "Peer review passed"],
            ["Done", "None", "Meets the Definition of Done"],
          ),
          "The team also splits the In progress limit across swimlanes to protect planned work:",
          L(
            "**Expedite lane (limit 1):** production incidents only. Any free person pulls it immediately.",
            "**Requests lane (limit 2):** unplanned support and small changes, about 40% of capacity.",
            "**Features lane (limit 3):** planned backlog items, about 60% of capacity.",
          ),
          "Each column's policy works like a mini [Definition of Done](/project-management/agile/definition-of-done/). "
          "Our free [Kanban board template](/templates/kanban-board-template/) has WIP limits and columns you can "
          "adapt to this layout, and the [workflow template](/templates/workflow-template/) helps you map the steps "
          "first.",
        ),
        S("Worked example: moving a Scrum team to Scrumban",
          "**This example is illustrative; the team and figures are invented to show a typical transition.**",
          "A seven-person platform team runs two-week Sprints. About 40% of the items it finishes are unplanned: "
          "bug fixes, access requests and small changes from other teams. It has missed the Sprint Goal in four of "
          "its last six Sprints, and Sprint Planning has become a negotiation about how much capacity to hold back. "
          "The team decides to move to Scrumban in three stages, reviewing each at a retrospective.",
          T(["Stage", "What changes", "What stays from Scrum", "What to watch"],
            ["1. Weeks 1 to 4", "Map the real workflow on the board; add WIP limits and an Expedite lane", "Sprints, Sprint Goal, all events, story points", "Blocked items and columns that hit their limit"],
            ["2. Weeks 5 to 10", "Replace the Sprint commitment with a planning trigger (plan at 4, Ready limit 8); add Requests and Features lanes", "Two-week review and retrospective; Product Owner and Scrum Master", "Whether Ready ever runs empty; how often planning happens"],
            ["3. Week 11 onwards", "Drop story points; forecast from throughput; publish a service level expectation", "Review, retrospective, daily stand-up", "Cycle time percentiles and work item age"],
          ),
          "By stage 3, the team has a clear picture of its flow. Planned items take a median of four working days "
          "and 85% finish within seven, so the team publishes \"85% of items within seven working days\" as its "
          "service level expectation. Planning sessions are shorter because they cover a few items at a time, and "
          "urgent work no longer breaks a commitment.",
          "The team keeps the fortnightly review and retrospective because stakeholders value the rhythm. If it "
          "later decided to drop the Scrum roles and fixed meetings too, it would effectively be running Kanban.",
          TIP("Change one thing per stage and keep it for at least two weeks before judging it. Changing WIP "
              "limits, planning and estimation all at once makes it impossible to tell what helped."),
        ),
        S("Scrumban beyond software: a marketing example",
          "Scrumban is not limited to development teams. **This example is illustrative.**",
          "A five-person content marketing team plans campaign content a quarter ahead but also receives a steady "
          "stream of requests from sales, such as case studies, slide updates and event copy. Under two-week "
          "Sprints, sales requests either waited up to a fortnight or broke the Sprint plan.",
          "The team moves to Scrumban. The head of content keeps the Product Owner role and orders both campaign "
          "work and sales requests in one backlog. The board runs Ready (limit 6, plan at 3), Drafting (3), Design "
          "(2), Approval (2) and Published. The team finishes about six pieces a week, a little over one per working "
          "day, and planning takes a day to arrange, so a trigger of 3 leaves a safety margin of almost two items.",
          "Within a few weeks, the Approval column is often full while writers wait. The WIP limit has exposed the "
          "real bottleneck. At the retrospective, the team and its approvers agree a policy of reviewing within two "
          "working days, and flow improves. The team keeps a fortnightly review with sales and a monthly "
          "retrospective, the Scrum rhythm it valued, without the batch commitment. Our guide to "
          "[Agile marketing](/project-management/agile/agile-marketing/) covers more patterns for marketing teams.",
        ),
        S("How to set up Scrumban step by step",
          OL(
            "**Agree the problem you want to solve**, such as missed Sprint Goals or too much time spent planning, so you can measure whether Scrumban helps.",
            "**Map your actual workflow** as columns, from Backlog through Ready and each working step to Done.",
            "**Write a policy for each column** describing what must be true before an item moves in.",
            "**Set starting WIP limits**, roughly the number of people who work in each column, and tune them after two or three weeks.",
            "**Add swimlanes** for urgent and unplanned work, and decide how much capacity each lane gets.",
            "**Calculate a planning trigger and Ready limit** using your throughput and planning lead time.",
            "**Choose your meeting cadence**: daily stand-up, on-demand planning, and a review and retrospective every two to four weeks.",
            "**Decide which Scrum roles stay** and write down who orders the backlog and who looks after flow.",
            "**Track flow from day one**: record start and finish dates for throughput, [cycle time and lead time](/project-management/kanban/cycle-time-vs-lead-time/), and use a [WIP aging chart](/project-management/kanban/wip-aging-chart/) to spot stuck items.",
            "**Inspect and adapt at each retrospective**, changing one policy at a time.",
          ),
          "Our [sprint retrospective template](/templates/sprint-retrospective-template/) works just as well for "
          "Scrumban retrospectives.",
        ),
        S("Is it Kanban or Scrumban? A quick test",
          "The line between the two is blurry, partly because Kanban is not meeting-free: Kanban University's "
          "Kanban Method describes seven cadences, from a daily meeting to a quarterly strategy review (see "
          "[Kanban ceremonies](/project-management/kanban/kanban-ceremonies/)). So a Kanban team that holds a "
          "fortnightly review is still doing Kanban. Use this test instead:",
          T(["If your team...", "It is probably running"],
            ["Started from its existing process with no Scrum in place", "Kanban"],
            ["Started from Scrum and kept a Product Owner and Scrum Master", "Scrumban"],
            ["Keeps iterations, even without a Sprint commitment", "Scrumban"],
            ["Plans when Ready hits a trigger and uses Scrum names for its meetings", "Scrumban"],
            ["Has a Sprint Goal and commits to a batch each Sprint", "Scrum, perhaps with Kanban practices"],
            ["Has no WIP limits", "Neither, yet; add WIP limits first"],
          ),
          "The label matters less than clarity. Write down your rules so new team members and stakeholders know "
          "how work enters, flows and is reviewed.",
        ),
        S("Kanban vs Scrumban: which should you choose?",
          T(["Your situation", "Usual choice", "Why"],
            ["You run Scrum and unplanned work keeps breaking Sprint Goals", "Scrumban", "Keeps the rhythm the team knows while removing the batch commitment"],
            ["You run Scrum and want to move to Kanban without a big-bang change", "Scrumban, then Kanban", "Scrumban was designed as this stepping stone"],
            ["You do not use Scrum today", "Kanban", "Start with your current process; no need to adopt Scrum first"],
            ["Almost all work is unplanned, such as a service desk", "Kanban", "There is little planned work for Scrum structure to organise"],
            ["Stakeholders want a fixed review rhythm but work is mixed", "Scrumban", "Regular reviews with continuous flow"],
            ["You want minimal process change and no new titles", "Kanban", "Kanban respects current roles"],
            ["A Kanban team lacks focus and planning discipline", "Scrumban, or add Kanban cadences", "A regular planning and review rhythm adds structure"],
          ),
          "IT operations and platform teams often sit on the boundary. Our guide to "
          "[Agile in IT operations](/project-management/agile/agile-operations-it/) covers how such teams balance "
          "planned and unplanned work.",
        ),
        S("Pros and cons of Kanban and Scrumban",
          T(["", "Kanban", "Scrumban"],
            ["Pros", "Starts immediately with the current process; no new roles; handles unpredictable work well; strong flow metrics", "Familiar to Scrum teams; keeps a regular review and reflection rhythm; absorbs unplanned work better than Sprints; a gradual route to flow"],
            ["Cons", "Can drift without discipline; no built-in planning rhythm unless you add cadences; less guidance on product goals", "No official guide, so rules vary; risk of keeping Scrum's overhead without its focus; harder to explain to stakeholders used to Sprint commitments"],
            ["Watch out for", "Boards without WIP limits or policies", "A hybrid that is really Scrum with broken commitments"],
          ),
        ),
        S("Moving on from Scrumban to Kanban",
          "Because Scrumban began as a bridge, some teams eventually move on to pure Kanban. Signs you are ready "
          "include stable WIP limits, a reliable service level expectation and meetings that would happen anyway "
          "without Scrum names. To complete the move:",
          OL(
            "Drop any remaining iterations and schedule each meeting on its own cadence.",
            "Replace the Product Owner's planning role with replenishment, ordered by whoever owns demand.",
            "Turn the Scrum Master role into shared responsibility for flow, or a Service Delivery Manager if your organisation uses one.",
            "Keep the retrospective and stakeholder review; improvement and feedback remain core Kanban practices.",
          ),
          "Read our guide to [Kanban principles and practices](/project-management/kanban/kanban-principles/) for "
          "what your team will rely on once the Scrum scaffolding is gone.",
        ),
        S("Tools that support Scrumban",
          "Scrumban needs a board with WIP limits, swimlanes and, ideally, flow reports. Most mainstream tools "
          "handle it:",
          L(
            "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool (9.4/10), builds boards from custom statuses on every plan, and adds dashboards, request forms for unplanned work and automation, which suits Scrumban teams that take requests from several departments.",
            "**[Jira](/project-management-tools/jira/)** offers both Scrum and Kanban boards with WIP limits, swimlanes, cumulative flow diagrams and control charts, so software teams can move from one to the other in the same tool.",
            "**[ClickUp](/project-management-tools/clickup/)** combines Sprints with per-column WIP limits on its board view, useful for teams keeping optional iterations alongside flow.",
          ),
        ),
        S("Common Scrumban mistakes",
          L(
            "**Dropping WIP limits.** Without them, Scrumban is just Scrum without commitments.",
            "**Keeping every Scrum meeting at full length.** On-demand planning should be short; if planning still takes half a day, the trigger or Ready limit is wrong.",
            "**Never writing the rules down.** With no official guide, unwritten rules cause confusion about what still applies.",
            "**Letting the Expedite lane fill up.** If everything is urgent, nothing is. Keep its limit at one and define what qualifies.",
            "**Measuring only velocity.** Once there is no Sprint commitment, velocity loses meaning; switch to throughput and cycle time.",
            "**Changing too much at once.** Move in stages, as in the worked example, so you can see what helps.",
            "**Using Scrumban to avoid hard conversations.** If a team keeps missing goals because of poor refinement, a new label will not fix it.",
          ),
        ),
    ],
    faq=[
        ("What is the difference between Kanban and Scrumban?",
         "Kanban is a flow method applied to your existing process, with WIP limits and no required roles or iterations. Scrumban is a hybrid that keeps parts of Scrum, such as roles, regular planning, reviews and retrospectives, while replacing the Sprint commitment with Kanban's continuous pull and WIP limits."),
        ("Is Scrumban better than Kanban?",
         "Neither is better in general. Scrumban suits Scrum teams that want a gradual move to flow or need a regular review rhythm with mixed work. Kanban suits teams that do not use Scrum, or whose work is almost entirely unplanned."),
        ("Who created Scrumban?",
         "The term was popularised by Corey Ladas, whose 2009 book Scrumban: Essays on Kanban Systems for Lean Software Development described it as a way for Scrum teams to move towards Kanban."),
        ("Does Scrumban have sprints?",
         "Not in the Scrum sense. Some Scrumban teams keep fixed iterations to time their reviews and retrospectives, but they do not commit to finishing a batch of work by the end of each one. Others drop iterations entirely."),
        ("Does Scrumban have roles?",
         "Scrumban does not require any roles. Teams moving from Scrum often keep a Product Owner to order the backlog and a Scrum Master to coach flow, while others share these responsibilities across the team."),
        ("What meetings does Scrumban use?",
         "Most Scrumban teams hold a daily stand-up, planning on demand when the Ready column hits its trigger, a regular review with stakeholders and a regular retrospective. Many also run backlog refinement."),
        ("Does Scrumban use story points?",
         "It can, but many teams drop them over time. Once work is pulled continuously, throughput and cycle time give more useful forecasts, and teams split items to a similar size instead of estimating each one. See our guide to [story points](/project-management/scrum/scrum-story-points/)."),
        ("Is there an official Scrumban guide?",
         "No. Scrum has the Scrum Guide and Kanban has the Kanban Guide and Kanban University's materials, but Scrumban has no single official definition. Some consultancies and vendors publish their own guides."),
        ("How do you plan work in Scrumban?",
         "Scrumban uses planning on demand. The team sets a minimum number of items for the Ready column, and when Ready falls to that trigger, the Product Owner and team hold a short session to refill it."),
        ("Is Scrumban agile?",
         "Yes. Scrumban combines two widely used Agile approaches and keeps their emphasis on small batches, frequent feedback and continuous improvement."),
        ("Can a Kanban team move to Scrumban?",
         "It can, but it rarely needs to. A Kanban team that wants more structure can usually add Kanban cadences, such as a replenishment meeting and a service delivery review, without adopting Scrum roles."),
        ("Does Scrumban use WIP limits?",
         "Yes. WIP limits are one of the main elements Scrumban takes from Kanban, and without them it is not really Scrumban."),
        ("How long does it take to move from Scrum to Scrumban?",
         "A staged move usually takes two to three months: a few weeks to add WIP limits while keeping Sprints, a few more to switch to planning on demand, and then time to collect enough flow data to drop estimation and set a service level expectation."),
        ("Which teams use Scrumban?",
         "Scrumban is common in software maintenance, platform and DevOps teams, and in marketing or product teams that combine planned projects with a steady stream of requests."),
    ],
)
