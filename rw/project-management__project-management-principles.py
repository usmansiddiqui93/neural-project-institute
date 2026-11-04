from core import S, L, OL, T, TIP, H3

URL = "/project-management/project-management-principles/"

RW = dict(
    title="Project Management Principles: The 6 PMBOK 8 Principles",
    desc="Project management principles explained: PMBOK 8's six principles with examples, where the 7th edition's 12 went, and PRINCE2 7's seven compared.",
    intro=(
        "Project management principles are the guiding ideas that shape decisions on any project, whatever method "
        "you use, and PMI's current set is the six principles in the PMBOK Guide 8th edition, published in November "
        "2025. They replace the twelve principles of the 7th edition, which many articles still present as current. "
        "This guide explains all six with examples, shows where the twelve went and compares them with the seven "
        "principles of PRINCE2 7."
    ),
    takeaways=[
        "The PMBOK Guide 8th edition (November 2025) has six principles: adopt a holistic view, focus on value, embed quality, be an accountable leader, integrate sustainability and build an empowered culture.",
        "The 7th edition (2021) had twelve principles. Their ideas have not disappeared: most were merged into the six, and tailoring and risk now sit elsewhere in the guide.",
        "PRINCE2 7 (2023) has seven principles, and a project only counts as PRINCE2 if all seven are applied; you can tailor almost everything else, but not the principles.",
        "Principles tell you what good looks like when no process covers the situation; processes tell you how to do a specific piece of work.",
        "Use principles at real decision points: kick-off, phase gates, change requests and retrospectives, not as a poster on the wall.",
        "For the PMP exam, PMI's July 2026 exam content outline defines what is tested; the principles are useful background for situational questions.",
    ],
    sections=[
        S(
            "What are project management principles?",
            "**Project management principles** are short, broadly applicable statements of how good project work should "
            "be approached. They guide behaviour and decisions rather than prescribing steps, so they apply to predictive, "
            "Agile and hybrid projects alike. In PMI's PMBOK Guide 8th edition there are six; PRINCE2 7 has seven.",
            "Principles sit above the detail of any method. A Scrum team and a PRINCE2 project board can follow very "
            "different processes and still agree that work should deliver value, that quality should be built in and "
            "that someone must own outcomes. Principles hold when your process runs out.",
            T(
                ["Term", "What it is", "Example", "Can you tailor it?"],
                ["Principle", "A guiding idea about how to behave and decide", "Focus on value", "You apply it in proportion, but you do not drop it"],
                ["Process", "A defined set of activities with inputs and outputs", "Perform integrated change control", "Yes: combine, simplify or skip as the project needs"],
                ["Practice or technique", "A specific way of doing part of the work", "Daily stand-up, earned value, RACI chart", "Yes: choose what fits"],
                ["Method or framework", "A packaged way of running projects", "PRINCE2, Scrum, Kanban", "Yes, within the method's own rules"],
            ),
            "The main principle sets you will meet come from different owners. PMI publishes the [PMBOK Guide](/project-management/pmbok-guide/); "
            "PeopleCert owns [PRINCE2](/project-management/prince2/); the [Agile Manifesto](/project-management/agile/agile-manifesto-values-and-principles/) "
            "has twelve principles of its own; Scrum rests on three pillars and five values; and the Kanban Method has its "
            "own principles and practices. This page focuses on PMI and PRINCE2 and points you to the others.",
        ),
        S(
            "The six PMBOK 8 principles at a glance",
            "The PMBOK Guide 8th edition includes *The Standard for Project Management*, and its principles chapter "
            "sets out the project management mindset and six principles. For each principle the Standard describes its "
            "impact, what the principle looks like in action and how it connects to the seven performance domains "
            "(governance, scope, schedule, finance, stakeholders, resources and risk).",
            T(
                ["#", "Principle (Standard title)", "Core idea", "The question it makes you ask"],
                ["1", "Adopt a holistic view", "A project is a system of connected parts inside a wider organisation", "What else does this decision affect?"],
                ["2", "Focus on value", "Success is judged by the benefits delivered, not only by outputs", "Is this still worth doing, and is it the most valuable thing to do next?"],
                ["3", "Embed quality into processes and deliverables", "Build quality in from the start rather than inspecting it in at the end", "How will we know it is good enough, and how do we prevent defects?"],
                ["4", "Be an accountable leader", "Own outcomes and lead with integrity, whatever your formal role", "Who owns this, and am I acting in the project's and stakeholders' best interest?"],
                ["5", "Integrate sustainability within all project areas", "Weigh environmental, social and economic effects throughout", "What does this leave behind for the organisation, community and environment?"],
                ["6", "Build an empowered culture", "Create conditions in which people collaborate, decide and recover from setbacks", "Do the people closest to the work have the information and authority to act?"],
            ),
            "Some summaries shorten the titles, for example \"embed quality\", \"integrate sustainability\" or \"lead "
            "accountably\". The meaning is the same. For the full structure of the book, including the 40 processes and "
            "five focus areas, see our [guide to the PMBOK Guide 8th edition](/project-management/pmbok-guide/).",
        ),
        S(
            "The six principles explained",
            H3("1. Adopt a holistic view"),
            "A project is not a set of independent tasks. Scope, schedule, cost, risk and people interact, and the "
            "project itself interacts with operations, other projects and the wider organisation. A holistic view means "
            "looking at those connections before you act. Commentators link it to the 7th edition's systems-thinking "
            "principle, and it also absorbs much of what the 7th edition said about complexity.",
            L(
                "**In practice:** assess every significant change for knock-on effects on cost, schedule, risk, people and "
                "neighbouring projects before approving it, using a formal [change control](/project-management/change-control/) "
                "process where the stakes justify it.",
                "**In practice:** map dependencies with other teams and suppliers early, and revisit the map at each phase.",
                "**Warning signs:** teams optimising their own work at the expense of the whole; surprises from "
                "departments nobody consulted; risks that \"belong to someone else\".",
            ),
            H3("2. Focus on value"),
            "Value is the reason the project exists. It may be financial, social, regulatory or strategic, and it can "
            "change during delivery as markets, priorities or technology move. Focusing on value means checking the "
            "business case regularly, prioritising work that delivers the most benefit soonest, and being willing to "
            "stop work that no longer pays back.",
            L(
                "**In practice:** state the expected benefits and how they will be measured in the "
                "[project charter](/project-management/project-charter/), then test them at each phase gate.",
                "**In practice:** use a [cost-benefit analysis](/project-management/cost-benefit-analysis/) when options "
                "compete, and record value assumptions so you can see when they change.",
                "**Warning signs:** reporting only on time and budget; a business case written once and never reopened; "
                "features delivered that nobody uses.",
            ),
            H3("3. Embed quality into processes and deliverables"),
            "Quality is a design decision made early, not an inspection made late. This principle covers both the "
            "deliverables (do they meet agreed acceptance criteria?) and the way the work is done (does the process "
            "prevent defects?). It also means not gold-plating: delivering what is needed, to the standard agreed, "
            "rather than everything that is possible.",
            L(
                "**In practice:** agree acceptance criteria before work starts, review early drafts and prototypes, and "
                "automate checks where you can.",
                "**In practice:** treat recurring defects as process problems; see our guide to "
                "[project quality management](/project-management/project-quality-management/).",
                "**Warning signs:** testing squeezed into the last week; rework accepted as normal; arguments at "
                "handover about what \"done\" meant.",
            ),
            H3("4. Be an accountable leader"),
            "Leadership on a project is not limited to the project manager, and it is not the same as administration. "
            "An accountable leader takes ownership of outcomes, acts with integrity and transparency, and makes sure "
            "accountability is clear across the team. Some commentators note that this principle combines the 7th "
            "edition's separate stewardship and leadership principles.",
            L(
                "**In practice:** make decision rights and accountability explicit, for example with a "
                "[RACI matrix](/project-management/raci-matrix/), and report bad news early with a recovery plan.",
                "**In practice:** model the behaviour you expect: keep commitments, admit mistakes, give credit.",
                "**Warning signs:** \"I just follow the process\"; missed milestones explained away; decisions that "
                "nobody admits to having made.",
            ),
            H3("5. Integrate sustainability within all project areas"),
            "Sustainability is the most visible new emphasis in the 8th edition. It asks you to consider what the "
            "project leaves behind: environmental effects such as energy use and waste, social effects on people and "
            "communities, and economic effects such as long-term running costs. It belongs in every area, from supplier "
            "choice and design to operations and closure, not in a separate report.",
            L(
                "**In practice:** include whole-life cost, energy and supplier practices in option appraisal and "
                "[procurement](/project-management/project-procurement-management/) criteria.",
                "**In practice:** add sustainability risks and opportunities to the risk register and track them like "
                "any other.",
                "**Warning signs:** sustainability mentioned in the charter and nowhere else; the cheapest option chosen "
                "without considering running costs or disposal.",
            ),
            H3("6. Build an empowered culture"),
            "Projects are delivered by people, and people do their best work when they trust each other, understand "
            "the goal and have the authority to act. An empowered culture covers collaboration within the team, "
            "genuine engagement with stakeholders, psychological safety and resilience when things go wrong. It "
            "carries forward much of the 7th edition's team, stakeholder and resiliency principles.",
            L(
                "**In practice:** delegate decisions to the people closest to the work, with clear boundaries and "
                "escalation routes.",
                "**In practice:** involve stakeholders early and often; our guide to "
                "[stakeholder management](/project-management/project-stakeholder-management/) shows how to plan it.",
                "**Warning signs:** every decision waits for the project manager; people hide problems; the same few "
                "voices dominate meetings.",
            ),
        ),
        S(
            "From twelve principles to six",
            "The PMBOK Guide 7th edition, published in 2021, replaced the old process groups and knowledge areas with "
            "twelve principles and eight performance domains. The twelve are still widely taught and quoted, but they are "
            "no longer PMI's current set, even though the thinking behind them is still sound.",
            "PMI describes the 8th edition as consolidating the principles. The table below lists the twelve with their "
            "7th edition titles and shows where each idea now sits. PMI has not published a simple one-to-one mapping "
            "that we could find, so the right-hand column is **our reading**, based on the 8th edition's principle "
            "titles and structure.",
            T(
                ["7th edition principle", "Short name", "Where the idea sits in the 8th edition (our reading)"],
                ["Be a diligent, respectful and caring steward", "Stewardship", "Be an accountable leader; care for the environment and society now has its own sustainability principle"],
                ["Create a collaborative project team environment", "Team", "Build an empowered culture"],
                ["Effectively engage with stakeholders", "Stakeholders", "Build an empowered culture, plus the stakeholders performance domain"],
                ["Focus on value", "Value", "Focus on value"],
                ["Recognise, evaluate and respond to system interactions", "Systems thinking", "Adopt a holistic view"],
                ["Demonstrate leadership behaviours", "Leadership", "Be an accountable leader"],
                ["Tailor based on context", "Tailoring", "A full tailoring chapter in the guide rather than a principle"],
                ["Build quality into processes and deliverables", "Quality", "Embed quality into processes and deliverables"],
                ["Navigate complexity", "Complexity", "Adopt a holistic view"],
                ["Optimise risk responses", "Risk", "The risk performance domain and its processes"],
                ["Embrace adaptability and resiliency", "Adaptability and resiliency", "Build an empowered culture, and the choice of life cycle and development approach"],
                ["Enable change to achieve the envisioned future state", "Change", "Focus on value (benefits depend on people adopting the output) and build an empowered culture"],
            ),
            H3("Why PMI consolidated the principles"),
            "Twelve principles overlapped considerably: stewardship and leadership, team and stakeholders, systems "
            "thinking and complexity all describe related behaviours. Six are easier to remember and apply. The 8th "
            "edition also moved practical material back into the book, so ideas such as tailoring and risk response, "
            "which the 7th edition could only express as principles, now have their own chapters, domains and "
            "processes.",
            TIP("If you studied the 7th edition, you do not need to unlearn anything. Group what you know under the six new headings, add sustainability, and read the 8th edition's tailoring chapter and risk domain for the material that moved."),
        ),
        S(
            "PRINCE2 7's seven principles",
            "PRINCE2 is a process-based method owned by PeopleCert. Its current edition, PRINCE2 7, was published in "
            "2023 and is built from five integrated elements: principles, people, practices, processes and the project "
            "context. The seven principles are the foundation. A project is only being run as PRINCE2 if all seven are "
            "applied; you can tailor processes, practices, roles and management products, but not the principles.",
            T(
                ["PRINCE2 7 principle", "What it means", "How it shows up"],
                ["Ensure continued business justification", "The project must remain desirable, viable and achievable throughout", "The business case is reviewed at every stage boundary; the project is closed early if it stops being worthwhile"],
                ["Learn from experience", "Seek, record and act on lessons from previous and current work", "Lessons are gathered at start-up and captured throughout, not only at closure"],
                ["Define roles, responsibilities and relationships", "Everyone knows who decides, who does and how people work together", "A project board representing business, user and supplier interests"],
                ["Manage by stages", "Plan, monitor and control the project one management stage at a time", "Detailed stage plans; authorisation to continue at each stage boundary"],
                ["Manage by exception", "Set tolerances so each level of management only escalates when they are forecast to be exceeded", "Tolerances for time, cost, quality, scope, benefits, risk and sustainability"],
                ["Focus on products", "Define and agree the outputs and their quality before doing the work", "Product descriptions with quality criteria"],
                ["Tailor to suit the project", "Adapt the method to the project's environment, size, complexity, importance, capability and risk", "Tailoring decisions recorded in the project initiation documentation"],
            ),
            "PRINCE2 7 renamed the roles principle. The 2017 edition called it \"defined roles and responsibilities\"; "
            "the 7th edition adds **relationships**, reflecting the new people element. The 7th edition also added "
            "sustainability as a performance target alongside time, cost, quality, scope, benefits and risk.",
            "See our [PRINCE2 guide](/project-management/prince2/) for the practices and processes, and our "
            "[PMBOK vs PRINCE2 comparison](/project-management/pmbok-vs-prince2/) for how the two fit together.",
        ),
        S(
            "PMBOK 8 vs PMBOK 7 vs PRINCE2 7 principles",
            "The three sets are often confused, especially in exam preparation. They differ in purpose as well as number.",
            T(
                ["", "PMBOK Guide 8th edition", "PMBOK Guide 7th edition", "PRINCE2 7"],
                ["Owner", "PMI", "PMI", "PeopleCert"],
                ["Published", "November 2025", "2021", "2023"],
                ["Number of principles", "6", "12", "7"],
                ["Status", "Current", "Superseded by the 8th edition", "Current"],
                ["Nature", "Mindset that underpins a non-prescriptive standard", "Mindset that underpins a non-prescriptive standard", "Mandatory foundations of a prescriptive method"],
                ["Must all be applied?", "Applied in proportion to the project", "Applied in proportion to the project", "Yes, all seven, or it is not PRINCE2"],
                ["Distinctive emphasis", "Sustainability, accountable leadership, empowered culture", "Stewardship, systems thinking, tailoring, change", "Business justification, stages, exception, products"],
            ),
            H3("Where the themes overlap"),
            T(
                ["Theme", "PMBOK 8 principle", "PRINCE2 7 principle"],
                ["Value and justification", "Focus on value", "Ensure continued business justification"],
                ["Accountability and roles", "Be an accountable leader", "Define roles, responsibilities and relationships"],
                ["Quality of outputs", "Embed quality into processes and deliverables", "Focus on products"],
                ["Learning and improvement", "Build an empowered culture; embed quality", "Learn from experience"],
                ["Fitting the approach to the project", "Tailoring chapter of the guide", "Tailor to suit the project"],
                ["Sustainability", "Integrate sustainability within all project areas", "Sustainability performance target and tolerance (not a principle)"],
                ["Control structure", "Governance performance domain", "Manage by stages; manage by exception"],
                ["Whole-system thinking", "Adopt a holistic view", "Implicit in the project context element"],
            ),
            "The practical lesson: if you run PRINCE2 projects, the PMBOK principles add little that conflicts and a "
            "good deal that complements, especially around leadership and culture. If you follow PMI, PRINCE2's stage "
            "and exception principles are a useful model for [project governance](/project-management/project-governance/).",
        ),
        S(
            "Other principle sets you will meet",
            "Many teams combine a project management standard with an Agile or Lean way of working. Each comes with its "
            "own principles, and they sit comfortably alongside PMI's six.",
            T(
                ["Source", "What it contains", "Our guide"],
                ["Agile Manifesto (2001)", "Four values and twelve principles for adaptive, collaborative delivery", "[Agile Manifesto values and principles](/project-management/agile/agile-manifesto-values-and-principles/)"],
                ["Scrum Guide (2020)", "Three pillars of empiricism and five Scrum values; no list called principles", "[Scrum principles and values](/project-management/scrum/scrum-principles-and-values/)"],
                ["Kanban Method", "Change management and service delivery principles plus six general practices", "[Kanban principles](/project-management/kanban/kanban-principles/)"],
                ["Lean thinking", "Value, value stream, flow, pull and continuous improvement", "[Lean project management](/project-management/lean-project-management/)"],
            ),
            "If you see a list of \"5\", \"8\" or \"10\" project management principles that matches none of these, it is "
            "usually an author's own summary of good practice. Such lists can be useful, but they are not a standard.",
        ),
        S(
            "Worked example: the six principles on one project",
            "This illustrative example shows how the principles change real decisions. The organisation, figures and "
            "outcomes are invented.",
            "A housing association plans to replace gas boilers with heat pumps in 120 homes over nine months, with a "
            "budget of £1.2 million. Tenants stay in their homes during the work. The project uses a predictive plan for "
            "procurement and installation, with short weekly cycles for scheduling visits.",
            T(
                ["Principle", "Decision point", "What the team did", "Effect"],
                ["Adopt a holistic view", "Installation plan", "Checked the plan with the repairs team, the call centre and the electricity network operator before fixing dates", "Found that 30 homes needed electrical upgrades first and resequenced them, avoiding wasted visits"],
                ["Focus on value", "Month 4 review", "Re-tested the business case against new tariff data and tenant fuel bills", "Kept the project, but moved the oldest, least efficient homes to the front of the queue"],
                ["Embed quality", "First 10 installations", "Treated them as a pilot with a checklist, photo evidence and a tenant walkthrough", "Fixed a recurring commissioning fault before it reached the remaining 110 homes"],
                ["Be an accountable leader", "Supplier delay", "The project manager told the board about a six-week delay in the week it was known, with two recovery options", "The board approved a second installer within its tolerance; trust held"],
                ["Integrate sustainability", "Procurement", "Scored bids on whole-life cost, refrigerant type, waste handling and local employment as well as price", "Chose a supplier that was not the cheapest but had lower running and disposal costs"],
                ["Build an empowered culture", "Daily scheduling", "Let installation leads rebook visits directly with tenants within agreed rules", "Fewer missed appointments and faster rebooking without waiting for the office"],
            ),
            H3("The same project through a PRINCE2 lens"),
            L(
                "**Continued business justification:** the month 4 review was a stage boundary with a formal go or "
                "stop decision.",
                "**Manage by exception:** the board set tolerances of plus or minus four weeks and 5% of cost, so the "
                "second-installer decision stayed within delegated limits.",
                "**Focus on products:** the pilot produced a product description for a \"completed installation\", with "
                "quality criteria every crew used.",
                "**Learn from experience:** lessons from another landlord's pilot shaped the checklist before work began.",
            ),
        ),
        S(
            "How to apply project management principles, step by step",
            "Principles only help if they influence decisions. This process works on predictive, Agile and hybrid projects.",
            OL(
                "**Choose your set.** Use the PMBOK 8 six as a default, add PRINCE2's seven if you run PRINCE2, and add "
                "your delivery framework's principles if you use Scrum or Kanban.",
                "**Translate each principle into a project-specific rule.** For example, \"focus on value\" might become "
                "\"no feature enters the plan without a named benefit owner\".",
                "**Build them into the charter.** Record the benefits, quality expectations, sustainability goals and "
                "decision rights in the charter; our [project charter template](/templates/project-charter-template/) "
                "has sections for each.",
                "**Make accountability visible.** Agree who decides what, using our free "
                "[RACI matrix template](/templates/raci-matrix-template/).",
                "**Use them at decision points.** At each phase gate, change request and major risk response, ask the "
                "six questions from the table above before you decide.",
                "**Keep the value case live.** Revisit the [business case template](/templates/business-case-template/) "
                "at every gate, not just at approval.",
                "**Review them in retrospectives and lessons-learned sessions.** Ask which principle was weakest this "
                "period and what you will change. Our [lessons learned template](/templates/lessons-learned-template/) "
                "gives a simple structure.",
                "**Adjust as the project changes.** When risk, size or stakeholders shift, revisit how strongly each "
                "principle needs to be applied.",
            ),
        ),
        S(
            "Principles health check",
            "Use this check at kick-off, at each phase gate or quarterly on long projects. Score each line from 1 "
            "(rarely true) to 5 (consistently true). Any score of 2 or below is worth a conversation; a total below 18 "
            "suggests the principles are not yet shaping decisions.",
            T(
                ["Principle", "Question to score", "Evidence to look for"],
                ["Adopt a holistic view", "Do we assess the knock-on effects of changes before approving them?", "Impact assessments on change requests; a dependency map that is up to date"],
                ["Focus on value", "Have we re-tested the benefits since the last gate?", "Updated business case; benefits with owners and measures"],
                ["Embed quality", "Are acceptance criteria agreed before work starts?", "Criteria on work items; falling rework over time"],
                ["Be an accountable leader", "Is it clear who owns each decision, and is bad news raised early?", "Decision log; issues raised before they become crises"],
                ["Integrate sustainability", "Do our option appraisals include environmental, social and whole-life costs?", "Sustainability criteria in procurement and design decisions"],
                ["Build an empowered culture", "Can team members make routine decisions without waiting for approval?", "Delegated authority written down; problems raised openly in meetings"],
            ),
        ),
        S(
            "Common mistakes with project management principles",
            L(
                "**Teaching the twelve as current.** The 7th edition's principles are superseded. Use the six, and "
                "explain the twelve as background.",
                "**Treating principles as a poster.** Principles that never appear in a decision, a gate review or a "
                "retrospective have no effect.",
                "**Confusing principles with processes.** Principles do not tell you which documents to produce. Use the "
                "[project management processes](/project-management/project-management-processes/) for that.",
                "**Applying everything at full strength.** A two-week internal project needs a light touch; a "
                "regulated infrastructure programme needs much more. Proportion is part of applying principles well.",
                "**Leaving sustainability to someone else.** It is now a core principle, not a corporate report.",
                "**Using accountability to blame.** Accountable leadership is about ownership and transparency, not "
                "finding someone to fault when things go wrong.",
            ),
        ),
        S(
            "Project management principles and the PMP exam",
            "The [PMP certification](/project-management/pmp-certification/) exam is built on PMI's exam content "
            "outline, which was updated in July 2026 and weights three domains: People 33%, Process 41% and Business "
            "Environment 26%. The PMBOK Guide is one of several references, not the syllabus itself.",
            "The principles still matter for the exam because many situational questions test judgement: whether you "
            "re-check value before continuing, involve the people affected, take ownership of a problem or build "
            "quality in rather than inspecting it later. If you know the six principles well, the best answer in those "
            "questions is often easier to spot. The same applies to the [CAPM](/project-management/capm-certification/) "
            "at a more foundational level. For background on the organisation behind both exams, see "
            "[what is PMI](/project-management/what-is-pmi/).",
            "Read our overview of [project management methodologies](/project-management/project-management-methodologies/) "
            "next to see how these principles sit under predictive, Agile and hybrid ways of working.",
        ),
    ],
    faq=[
        ("What are the principles of project management?",
         "They are guiding ideas that shape decisions on any project, whatever method you use. PMI's current set, in "
         "the PMBOK Guide 8th edition, has six: adopt a holistic view, focus on value, embed quality into processes and "
         "deliverables, be an accountable leader, integrate sustainability within all project areas, and build an "
         "empowered culture."),
        ("How many project management principles are there?",
         "It depends on the source. The PMBOK Guide 8th edition has six, the 7th edition had twelve, PRINCE2 7 has "
         "seven and the Agile Manifesto has twelve of its own. Lists of five, eight or ten are usually an author's own summary."),
        ("What are the six principles in PMBOK 8?",
         "Adopt a holistic view; focus on value; embed quality into processes and deliverables; be an accountable "
         "leader; integrate sustainability within all project areas; and build an empowered culture."),
        ("What were the 12 principles of project management in PMBOK 7?",
         "Stewardship, team, stakeholders, value, systems thinking, leadership, tailoring, quality, complexity, risk, "
         "adaptability and resiliency, and change. They come from the 7th edition (2021), which the 8th edition replaced "
         "in November 2025."),
        ("Are the 7th edition's 12 principles still valid?",
         "Their ideas are still sound, but they are no longer PMI's current list. Most were merged into the six "
         "principles of the 8th edition, while tailoring and risk now have their own chapter and performance domain."),
        ("Which principle is new in the PMBOK Guide 8th edition?",
         "Integrate sustainability within all project areas. The 7th edition touched on care for the environment under "
         "stewardship, but the 8th edition makes sustainability a principle in its own right."),
        ("What are the seven principles of PRINCE2 7?",
         "Ensure continued business justification, learn from experience, define roles, responsibilities and "
         "relationships, manage by stages, manage by exception, focus on products, and tailor to suit the project. "
         "All seven must be applied for a project to count as PRINCE2."),
        ("What is the difference between principles and processes?",
         "Principles are guiding ideas about how to behave and decide; processes are defined activities with inputs "
         "and outputs. You tailor processes heavily, but you keep the principles and apply them in proportion."),
        ("Can you tailor project management principles?",
         "You apply them with more or less rigour depending on the project, but you do not drop them. PRINCE2 is "
         "explicit: processes, practices and products can be tailored, the principles cannot."),
        ("Do project management principles apply to Agile projects?",
         "Yes. PMI's principles are written for predictive, adaptive and hybrid work. Agile teams usually combine them "
         "with the Agile Manifesto's principles and their framework's own values, such as the Scrum values."),
        ("What is the most important project management principle?",
         "No source ranks them, and they work as a set. If you need one starting point, focus on value is the reason "
         "the project exists, and the other principles help you deliver that value well."),
        ("Are project management principles tested on the PMP exam?",
         "Not as a list to memorise. The PMP exam follows PMI's July 2026 exam content outline, but the principles "
         "inform many situational questions about judgement, leadership and value."),
        ("Why are project management principles important?",
         "They guide decisions when no process covers the situation, let teams using different methods work to the "
         "same standards and keep attention on outcomes rather than paperwork."),
    ],
)
