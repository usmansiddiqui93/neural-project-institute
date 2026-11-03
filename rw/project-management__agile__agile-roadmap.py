from core import S, L, OL, T, TIP, H3

URL = "/project-management/agile/agile-roadmap/"

RW = dict(
    title="Agile Roadmap: Formats, Example and How to Build One",
    desc="An Agile roadmap shows the outcomes a team is working towards over time. Learn the main formats, see a worked example and follow 9 steps to build your own.",
    intro=(
        "An Agile roadmap is a high-level, regularly updated plan that shows the goals and outcomes a product or "
        "team is working towards, ordered by priority over broad time horizons rather than fixed dates. This guide "
        "explains how it differs from a traditional plan and a release plan, compares the main formats, walks "
        "through a worked example and gives you nine steps to build and maintain your own."
    ),
    takeaways=[
        "An Agile roadmap communicates direction and priorities; the backlog and release plan hold the detail.",
        "Good roadmaps are built around outcomes and problems to solve, not lists of features with dates.",
        "Now-Next-Later, outcome-based and theme-based timelines are the most common formats.",
        "Detail and confidence should fall the further out an item sits; show genuine deadlines, avoid invented ones.",
        "Roadmap items become epics, epics become user stories, and stories are planned into releases and sprints.",
        "Review the roadmap on a fixed cadence, usually monthly or quarterly, and after any major learning.",
    ],
    sections=[
        S(
            "What is an Agile roadmap?",
            "An **Agile roadmap** is a short, visual plan that shows where a product or team is heading and why. It "
            "lists the goals, problems or outcomes the team will work on, in priority order, across broad time "
            "horizons such as now, next and later or the coming quarters. It is reviewed and updated as the team "
            "learns.",
            "The term usually means an **Agile product roadmap**, owned by a Product Owner or product manager. The same "
            "idea is used for Agile project roadmaps in non-software teams, and for **portfolio roadmaps** that "
            "combine several products. What makes any of them Agile is the approach: outcomes before outputs, honest "
            "uncertainty, and frequent revision.",
            H3("Why use an Agile roadmap?"),
            L(
                "**Alignment:** everyone can see how today's work connects to strategy.",
                "**Better conversations:** stakeholders discuss goals and trade-offs instead of arguing over feature dates.",
                "**Focus:** a short list of priorities makes it easier to say no to everything else.",
                "**Honest expectations:** confidence levels show what is committed and what is still being explored.",
                "**Context for the team:** developers understand why items matter, which leads to better solutions.",
            ),
            "Product Owners and [Agile product managers](/project-management/agile/agile-product-manager/) "
            "typically spend much of their stakeholder time on these conversations.",
            H3("Is a roadmap part of Scrum?"),
            "No. The 2020 Scrum Guide defines three artifacts (Product Backlog, Sprint Backlog and Increment) and "
            "does not mention a roadmap. It does introduce the **Product Goal**, a long-term objective that the "
            "Product Backlog works towards, and makes the Product Owner accountable for the Product Backlog. Many "
            "Scrum Teams use a roadmap to show the sequence of goals between today and that Product Goal. See our "
            "guides to the [Product Owner](/project-management/scrum/scrum-product-owner/) and the "
            "[product backlog](/project-management/scrum/product-backlog/).",
        ),
        S(
            "Agile roadmap vs traditional roadmap",
            T(
                ["Aspect", "Traditional roadmap or plan", "Agile roadmap"],
                ["Focus", "Features, tasks and deliverables", "Goals, outcomes and problems to solve"],
                ["Time", "Exact dates for everything", "Broad horizons; dates only where genuinely fixed"],
                ["Detail", "Even across the whole plan", "Detailed near term, broad further out"],
                ["Change", "Formally re-baselined", "Expected and reviewed on a cadence"],
                ["Measure of success", "Delivered on the planned date", "Outcome achieved, such as higher retention"],
                ["Audience", "Mainly the delivery team and sponsor", "Leadership, stakeholders, customers and the team"],
                ["Link to delivery", "Usually a separate Gantt chart", "Items flow into epics, the backlog and releases"],
            ),
            "A traditional roadmap is not wrong: it suits projects with fixed scope, contracts and dependencies, "
            "which our guide to the [project roadmap](/project-management/project-roadmap/) covers. Many hybrid "
            "teams combine both, using fixed milestones for external commitments and an Agile roadmap for "
            "everything else. Our guide to the "
            "[role of the project plan in Agile](/project-management/agile/role-of-the-project-plan-in-agile/) "
            "explains how the two fit together.",
        ),
        S(
            "Where the roadmap fits: from vision to sprint",
            "Agile planning works in levels. Each one adds detail over a shorter horizon, and the roadmap sits in the "
            "middle, linking strategy to the backlog.",
            T(
                ["Level", "Question it answers", "Typical horizon", "Usual owner"],
                ["Product vision", "Why does the product exist and who is it for?", "Several years", "Product leadership"],
                ["Strategy and goals", "Which goals, such as OKRs, matter most now?", "One year", "Product leadership with the Product Owner"],
                ["Agile roadmap", "Which outcomes will we pursue, in what order?", "Six to eighteen months", "Product Owner or product manager"],
                ["Release plan", "What will ship in the next few releases?", "One to six months", "Product Owner with the team"],
                ["Product backlog", "What exactly is next, in what order?", "Ongoing", "Product Owner"],
                ["Sprint backlog", "What will we do this sprint?", "One to four weeks", "Developers"],
            ),
            "The roadmap answers \"where and why\"; the [release plan](/project-management/agile/agile-release-planning/) "
            "answers \"what and roughly when\"; the backlog and [sprint planning](/project-management/scrum/sprint-planning/) "
            "answer \"exactly what next\". Keeping these apart is what stops the roadmap turning into a Gantt chart.",
        ),
        S(
            "What to include in an Agile roadmap",
            L(
                "**Vision or Product Goal** at the top, so every item can be traced back to it.",
                "**Goals or outcomes**, each with a measure, such as \"increase trial-to-paid conversion\".",
                "**Initiatives or themes**: the problems or opportunities the team will tackle to reach each goal.",
                "**Time horizons**: now, next and later, or quarters, with detail falling as you go further out.",
                "**Status or confidence** for each item, so readers know what is committed and what is exploratory.",
                "**Key dependencies and genuine deadlines**, such as regulatory dates or a trade show.",
                "**Owner and last-updated date**, so people know whom to ask and whether it is current.",
            ),
            H3("What to leave out"),
            "Individual user stories, task assignments, story point estimates and exact dates for work more than a "
            "release or two away. They belong in the backlog and release plan. A roadmap that tries to hold them "
            "becomes out of date within weeks and stops being trusted.",
        ),
        S(
            "Types of Agile roadmap",
            "Choose the format that fits your audience and the amount of certainty you have. Many teams keep one "
            "underlying roadmap and show it in two formats.",
            T(
                ["Format", "How it is laid out", "Best for", "Watch out for"],
                ["Now-Next-Later", "Three columns by priority and certainty, no dates", "Products with high uncertainty; teams moving away from date-driven plans", "Stakeholders who need dates may push back"],
                ["Outcome-based (goal-oriented)", "Each item is a measurable goal with initiatives beneath it", "Empowered teams and leadership using OKRs", "Goals that are too vague to measure"],
                ["Theme-based timeline", "Quarters or months with broad themes", "Organisations that need some time structure for budgeting and sales", "Themes quietly turning into fixed feature commitments"],
                ["Feature or epic timeline", "Epics on a timeline, often in a tool", "Near-term delivery coordination for one or a few teams", "False precision further out"],
                ["Portfolio roadmap", "Several products or teams in swimlanes", "Leaders coordinating across teams", "Too much detail for an executive audience"],
            ),
            H3("Now-Next-Later roadmap"),
            "Popularised by Janna Bastow, co-founder of ProdPad, the Now-Next-Later roadmap replaces dates with three "
            "columns. **Now** holds work in progress or about to start and is the most detailed. **Next** holds what "
            "comes after that, shaped but not yet refined. **Later** holds problems and opportunities you intend to "
            "explore, described broadly. Items move left as they become clearer and closer, and can be removed if "
            "priorities change.",
            H3("Outcome-based and GO roadmaps"),
            "An outcome-based roadmap lists goals such as \"reduce time to first value for new customers\" instead "
            "of features. Teams are then free to find the best solution. A well-known version is Roman Pichler's "
            "goal-oriented (GO) product roadmap, which has five elements for each period: date, name, goal, "
            "features and metrics. Our [OKR template](/templates/okr-template/) pairs well with this format.",
            H3("Theme-based timeline"),
            "A theme-based timeline keeps quarters or months along the top but places broad themes, such as "
            "\"self-service onboarding\", rather than features in each period. It gives finance and sales a sense "
            "of timing while leaving the detail open.",
        ),
        S(
            "How to create an Agile roadmap in 9 steps",
            OL(
                "**Start from the vision and strategy.** Write the product vision and the Product Goal in a sentence each. If leadership has set OKRs or strategic goals, list them; every roadmap item must support one.",
                "**Gather inputs.** Collect customer feedback, analytics, sales and support themes, technical debt, regulatory changes and stakeholder requests. Group them into problems rather than feature requests.",
                "**Choose three to five goals for the coming period.** Express each as an outcome with a measure and a target, such as \"raise 30-day retention from 40% to 50%\".",
                "**Identify initiatives for each goal.** For each goal, list the problems or bets that could move the measure. Keep them broad; these are candidate [epics](/project-management/agile/agile-epics/), not stories.",
                "**Prioritise.** Score the initiatives with a simple method such as RICE or cost of delay (see below), and agree the order with key stakeholders.",
                "**Place items on time horizons.** Put the top-priority, best-understood items in Now, the next ones in Next and the rest in Later. Check that Now fits the team's real capacity.",
                "**Mark dependencies, deadlines and confidence.** Note any genuine external dates, dependencies on other teams and a confidence level for each item.",
                "**Review with the team and stakeholders.** Walk through the draft with developers for feasibility and with stakeholders for value. Record what you decided not to do and why.",
                "**Publish, connect and maintain.** Share it in one place, link each Now item to its epic in the backlog, and set a review date.",
            ),
            TIP("Keep the first version small enough to fit on one screen or slide. If it does not fit, you are "
                "either including too much detail or trying to do too much at once."),
            H3("Running a roadmap workshop"),
            "Steps 3 to 8 are easiest in a single half-day workshop with the Product Owner, two or three developers "
            "and the main stakeholders. An illustrative agenda:",
            T(
                ["Time", "Activity", "Output"],
                ["30 min", "Recap vision, strategy and last period's results", "Shared context and lessons"],
                ["45 min", "Review grouped inputs and agree three to five goals with measures", "Draft goals"],
                ["45 min", "Brainstorm initiatives per goal, then cluster and name them", "Candidate initiatives"],
                ["45 min", "Score initiatives and place them on Now, Next and Later", "Draft roadmap"],
                ["30 min", "Check capacity, dependencies and deadlines; agree what is out", "Reviewed roadmap and a \"not doing\" list"],
                ["15 min", "Agree owners, how it will be shared and the next review date", "Actions and review date"],
            ),
        ),
        S(
            "Agile roadmap example",
            "This example is illustrative. A team of eight builds a project management app for small agencies. The "
            "vision is \"help small agencies deliver client work on time without spreadsheets\". Leadership's goals "
            "for the year are growth in paying customers and lower churn.",
            T(
                ["Horizon", "Goal and measure", "Initiatives", "Confidence"],
                ["Now (this quarter)", "Improve trial-to-paid conversion from 8% to 11%", "Guided onboarding with sample project; import from spreadsheets", "High: discovery done, epics refined"],
                ["Now (this quarter)", "Reduce support tickets about invoicing by 30%", "Redesign invoice set-up; in-app help", "High"],
                ["Next (next 3-6 months)", "Raise 90-day retention for teams of 5+ users", "Client portal for approvals; workload view", "Medium: problem validated, solutions open"],
                ["Next (next 3-6 months)", "Enter the accounting integration market", "Integration with one major accounting tool", "Medium: depends on partner API access"],
                ["Later (6-12 months)", "Grow average account size", "Advanced reporting; resource planning", "Low: exploring"],
                ["Later (6-12 months)", "Meet enterprise security requirements", "Single sign-on; audit log", "Low: waiting on customer research"],
            ),
            "Notice what the roadmap does not show: individual stories, estimates or sprint dates. It also lists a "
            "dependency (partner API access) and is honest that Later items may change.",
            H3("From roadmap item to sprint"),
            "Here is how the first Now item flows into delivery:",
            OL(
                "**Roadmap item:** improve trial-to-paid conversion with guided onboarding.",
                "**Epic:** \"Guided onboarding\", with a hypothesis: if new users create a sample project in their first session, more will convert.",
                "**User stories:** for example, \"As a new trial user, I want a sample client project created for me so I can see how the app works.\" See our guide to [user stories](/project-management/agile/user-stories/).",
                "**Release plan:** the team's forecast shows the minimum version of the epic fitting in the next two sprints, with spreadsheet import following in the release after.",
                "**Sprints:** stories are pulled into sprint planning in priority order.",
                "**Measure:** after release, the Product Owner checks conversion and updates the roadmap.",
            ),
            H3("Example for a non-software team"),
            "Agile roadmaps work outside software too. An illustrative Now-Next-Later roadmap for an in-house "
            "marketing team:",
            T(
                ["Horizon", "Goal and measure", "Initiatives"],
                ["Now", "Increase qualified leads from the website by 20%", "Rewrite three landing pages; launch a comparison guide"],
                ["Next", "Shorten the sales cycle for mid-sized clients", "Case study series; webinar programme"],
                ["Later", "Build awareness in a new region", "Local partner events; translated content"],
            ),
            "Our guide to [epics vs stories vs tasks](/project-management/agile/epics-vs-stories-vs-tasks/) explains "
            "each level of this breakdown. You can build the same structure in our "
            "[product roadmap template](/templates/product-roadmap-template/) and "
            "[product backlog template](/templates/product-backlog-template/).",
        ),
        S(
            "How to prioritise roadmap items",
            "Prioritisation decides what goes in Now. Use a simple, transparent method so stakeholders can see why "
            "one item beats another.",
            T(
                ["Method", "How it works", "Best for"],
                ["RICE", "Reach x Impact x Confidence / Effort", "Product teams comparing many ideas with some data"],
                ["Cost of delay / WSJF", "Value lost by waiting, divided by job size", "Portfolios and scaled Agile; time-sensitive work"],
                ["Value vs effort", "Plot items on a two-by-two grid", "Quick workshops with stakeholders"],
                ["MoSCoW", "Must, Should, Could, Won't have", "Fixed-date releases with negotiable scope"],
            ),
            H3("Worked example: RICE scores"),
            "Continuing the illustrative example, the team scores four candidate initiatives. Reach is users affected "
            "per quarter, impact is on a scale from 0.25 (minimal) to 3 (massive), confidence is a percentage and "
            "effort is in person-months.",
            T(
                ["Initiative", "Reach", "Impact", "Confidence", "Effort", "RICE score"],
                ["Guided onboarding", "2,000", "2", "80%", "2", "1,600"],
                ["Spreadsheet import", "1,200", "1", "80%", "1", "960"],
                ["Client portal", "600", "2", "50%", "3", "200"],
                ["Advanced reporting", "300", "1", "50%", "4", "38"],
            ),
            "Guided onboarding and spreadsheet import go to Now; the client portal goes to Next while the team "
            "raises confidence through discovery. Treat scores as an input to a conversation, not a final answer: "
            "strategic or regulatory work may still jump the queue.",
        ),
        S(
            "Dates, deadlines and confidence",
            "Stakeholders will ask \"when?\". An Agile roadmap can answer honestly without committing to dates the "
            "team cannot know.",
            T(
                ["Horizon", "What to show", "Confidence"],
                ["Now", "A target release or month, based on the team's forecast", "High"],
                ["Next", "A quarter or a range, such as \"Q2-Q3\"", "Medium"],
                ["Later", "No date, or a half-year at most", "Low"],
            ),
            L(
                "**Show genuine deadlines.** Regulatory dates, contract milestones and events are real constraints. Mark them clearly as [milestones](/project-management/project-milestones/).",
                "**Forecast from data.** Base near-term dates on the team's actual [throughput](/project-management/kanban/throughput/) or velocity, and give a range.",
                "**Separate forecasts from commitments.** Label which items are committed and which are forecasts; only a few should be commitments.",
                "**Update dates openly.** When a forecast moves, say so and explain why. Hidden slips destroy trust faster than visible ones.",
            ),
            H3("Worked example: forecasting a Now item"),
            "Continuing the illustrative example, the guided onboarding epic has been split into 24 stories. Over the "
            "last eight two-week sprints, the team finished between 6 and 9 stories per sprint, with roughly half "
            "of its capacity going to this epic and half to other work. That gives 3 to 4.5 onboarding stories per "
            "sprint, so the epic needs about 6 to 8 sprints, or 12 to 16 weeks. The roadmap therefore shows "
            "\"Now: target end of Q2, high confidence for the core flow\", and the Product Owner agrees with "
            "stakeholders which stories form the minimum version if the lower end of the range applies. Our guide to "
            "[Agile release planning](/project-management/agile/agile-release-planning/) covers this kind of "
            "forecast in more detail.",
        ),
        S(
            "Presenting the roadmap to different audiences",
            "One roadmap, several views. Keep a single source and tailor the level of detail.",
            T(
                ["Audience", "What they need", "Suggested view"],
                ["Executives", "Link to strategy, outcomes, investment and risk", "Outcome-based, one page, by quarter or Now-Next-Later"],
                ["Sales and customer success", "What is coming and roughly when, what to avoid promising", "Theme-based, with clear confidence labels"],
                ["Delivery team", "Priorities, context and what comes next", "Now-Next-Later linked to epics in the backlog"],
                ["Customers or the public", "Direction and problems being solved", "High-level themes, usually without dates"],
                ["Other teams", "Dependencies and timing that affect them", "Epic timeline with dependencies marked"],
            ),
            "Our guide to [project stakeholder management](/project-management/project-stakeholder-management/) "
            "covers how to map audiences and their interests.",
        ),
        S(
            "Keeping the roadmap up to date",
            "An Agile roadmap is only useful if it is current. Agree a cadence and stick to it:",
            L(
                "**Every sprint or fortnight:** the Product Owner checks Now items against progress and moves anything finished.",
                "**Monthly:** review Next and Later with key stakeholders; add, remove or reorder items.",
                "**Quarterly:** revisit goals and measures, usually alongside quarterly business or OKR planning.",
            ),
            "Also review it whenever something important changes: a major customer insight, a competitor move, a "
            "failed experiment or a change in budget. Frequent small updates are a sign of learning; a roadmap that "
            "has not changed in six months is a warning sign.",
        ),
        S(
            "Agile roadmaps across multiple teams",
            "When several teams work on one product or portfolio, each team keeps its own roadmap and a combined "
            "view shows how they connect.",
            L(
                "**Shared goals:** all team roadmaps trace back to the same product or portfolio goals.",
                "**Dependency view:** a portfolio roadmap shows where one team's Next depends on another team's Now.",
                "**Joint planning:** teams align roadmaps at a regular event; in SAFe this is [PI planning](/project-management/agile/pi-planning/).",
                "**One tool:** linking team epics in one tool lets the combined roadmap update itself.",
            ),
            "Portfolio-level roadmaps are usually maintained by portfolio leaders with support from an "
            "[Agile PMO](/project-management/agile/agile-pmo/). See our guide to "
            "[Agile portfolio management](/project-management/agile/agile-portfolio-management/) for how "
            "priorities and funding are set at that level.",
        ),
        S(
            "Agile roadmap checklist",
            "Before you share a roadmap, check that it passes these tests:",
            L(
                "Every item traces back to the vision or a stated goal.",
                "Each goal has a measure and a target, not just a name.",
                "Now fits the team's real capacity, including support and maintenance work.",
                "Detail and confidence fall from Now to Later.",
                "Genuine deadlines and cross-team dependencies are marked.",
                "Each Now item links to an epic in the backlog.",
                "It fits on one page or screen for its main audience.",
                "It shows an owner, a last-updated date and the next review date.",
            ),
        ),
        S(
            "Common Agile roadmap mistakes",
            T(
                ["Mistake", "What it looks like", "How to fix it"],
                ["Feature list with dates", "Every item is a feature with a delivery date", "Rewrite items as outcomes; keep dates for genuine deadlines"],
                ["Too much detail", "Stories and tasks on the roadmap", "Move detail into the backlog; keep the roadmap to one page"],
                ["Never updated", "The roadmap still shows last quarter's plan", "Set a monthly review and show a last-updated date"],
                ["Overloaded Now column", "Ten things \"in progress\" for one team", "Check Now against capacity and limit work in progress"],
                ["Built alone", "The Product Owner presents a finished roadmap", "Involve developers and stakeholders before publishing"],
                ["No link to delivery", "Roadmap and backlog drift apart", "Link every Now item to an epic in the backlog"],
                ["Treated as a promise", "Sales commits Later items to customers", "Label confidence and agree what can be shared externally"],
            ),
        ),
        S(
            "Agile roadmap tools and templates",
            "A slide or whiteboard is enough to start. Once the roadmap needs to stay linked to the backlog, a work "
            "management tool saves a lot of manual updating. Options from our reviews:",
            L(
                "**[Jira](/project-management-tools/jira/)** includes a timeline view on every plan that shows epics "
                "and their child work, which works well as a single-team Agile roadmap. Premium and Enterprise add "
                "Plans (previously Advanced Roadmaps) for cross-team roadmaps, dependencies and capacity.",
                "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool (9.4/10), combines Gantt and "
                "board views, request intake and cross-project dashboards, which suits roadmaps that span product, "
                "marketing and operations teams.",
                "**[Asana](/project-management-tools/asana/)** links projects to goals and portfolios on its Advanced "
                "plan, a natural fit for outcome-based roadmaps tied to OKRs.",
                "**[monday.com](/project-management-tools/monday/)** sells monday dev, a separate product for sprints, "
                "roadmaps and bug tracking, alongside its work management boards.",
                "**ClickUp** and **Notion** are flexible options for smaller product teams: ClickUp combines sprints, "
                "goals and timelines, and Notion's timeline view is often used as a lightweight product roadmap.",
            ),
            "Compare them on our [tool comparison page](/project-management-tools/compare/).",
            "See our free [product roadmap template](/templates/product-roadmap-template/), with themes, initiatives, quarters, owners and status, and pair it with the [release plan template](/templates/release-plan-template/) for the next level of detail.",
        ),
    ],
    faq=[
        ("What is an Agile roadmap?",
         "A high-level, regularly updated plan showing the goals and outcomes a product or team is working towards, "
         "in priority order over broad time horizons rather than exact dates."),
        ("What should an Agile roadmap include?",
         "The vision or Product Goal, three to five measurable goals, the initiatives that support them, time "
         "horizons, confidence levels, genuine deadlines and dependencies, and an owner and last-updated date."),
        ("What is a Now-Next-Later roadmap?",
         "A format with three columns: what the team is working on now, what comes next and what it plans to explore "
         "later. It replaces dates with priority and is honest about uncertainty further out."),
        ("What is an outcome-based roadmap?",
         "A roadmap where each item is a measurable goal, such as reducing onboarding time, rather than a feature. It "
         "leaves the team free to find the best solution."),
        ("What is the difference between a roadmap and a release plan?",
         "A roadmap shows goals and priorities over six to eighteen months. A release plan forecasts which backlog "
         "items will ship in the next few releases, usually one to six months ahead."),
        ("What is the difference between a roadmap and a product backlog?",
         "The roadmap is a high-level view of goals and initiatives. The product backlog is the detailed, ordered list "
         "of items, such as user stories, that the team will work on."),
        ("Is a roadmap part of Scrum?",
         "No. The 2020 Scrum Guide has three artifacts and no roadmap, but it includes the Product Goal. Many Scrum "
         "Teams use a roadmap to show the steps towards that goal."),
        ("Who owns the Agile roadmap?",
         "Usually the Product Owner or product manager, with input from leadership, customers, stakeholders and the "
         "development team."),
        ("Can an Agile roadmap have dates?",
         "Yes, for near-term items and genuine external deadlines. Further out, use quarters, ranges or no dates at "
         "all, and label the confidence of each item."),
        ("What is a theme in an Agile roadmap?",
         "A broad area of focus, such as self-service onboarding, that groups related initiatives. Themes give a "
         "sense of direction and timing without committing to specific features."),
        ("How far ahead should an Agile roadmap go?",
         "Commonly six to eighteen months, with detail and confidence decreasing the further out it goes."),
        ("How often should you update an Agile roadmap?",
         "Check Now items every sprint, review the wider roadmap monthly and revisit goals quarterly, plus after any "
         "major learning or change in strategy."),
        ("What is the difference between an Agile roadmap and a project roadmap?",
         "A project roadmap usually shows phases and milestones for a project with defined scope and end date. An "
         "Agile roadmap focuses on outcomes for an ongoing product and changes as the team learns."),
        ("What tools can I use for an Agile roadmap?",
         "A slide, whiteboard or spreadsheet template is enough to start. Tools such as Jira, Wrike, Asana, monday dev, "
         "ClickUp and Notion offer roadmap or timeline views linked to the backlog."),
    ],
)
