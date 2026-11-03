from core import S, L, OL, T, TIP, H3

URL = "/project-management/project-management-office-pmo/"

RW = dict(
    title="Project Management Office (PMO): Types, Roles and Setup",
    desc="A project management office (PMO) sets standards and supports projects. Learn PMO types, services, roles, KPIs and a step-by-step plan to set one up.",
    intro=(
        "A project management office (PMO) is a team or function that sets the standards for how projects are run "
        "and supports, monitors or directly manages them, so that an organisation delivers its projects more "
        "consistently and can see all of them in one place. This guide explains the types and levels of PMO, the "
        "services and roles inside one, how to set a PMO up step by step, and how to prove it is worth the cost."
    ),
    takeaways=[
        "A PMO standardises, supports and oversees project delivery across a department or a whole organisation.",
        "Supportive, controlling and directive PMOs differ in how much authority they hold over projects.",
        "PMOs also differ by level: project or programme office, departmental PMO, enterprise PMO and centre of excellence.",
        "Start with a short list of services that solve a real problem, prove their value, then expand.",
        "Measure the PMO by delivery outcomes, such as forecast accuracy and benefits, not by the number of reports it collects.",
        "Most PMO failures come from adding bureaucracy without giving project managers anything useful back.",
    ],
    sections=[
        S(
            "What is a project management office (PMO)?",
            "A **project management office (PMO)** is a team or organisational function that defines how projects "
            "are managed and supports, monitors or directly runs them. It provides common methods, templates, "
            "reporting, governance and expertise, so projects are delivered more consistently and leaders can see "
            "the health of all project work in one place.",
            "The letters PMO can also stand for a **programme management office** (supporting one large programme) "
            "or a **portfolio management office** (supporting decisions about which projects to fund). The functions "
            "overlap, and many organisations simply call all of them \"the PMO\". The differences are covered in "
            "the levels section below and in our guide to "
            "[programme vs project vs portfolio management](/project-management/program-vs-project-vs-portfolio-management/).",
            "PMOs are common in medium and large organisations. CIO.com, citing PM Solutions' 2022 State of the PMO "
            "research, reports that nearly three-quarters of midsize and large companies have one. The "
            "[PMBOK Guide](/project-management/pmbok-guide/) 8th edition, published by PMI in November 2025, includes "
            "an appendix on project management offices that covers PMO types, models, structure and maturity, and "
            "describes the PMO moving from a process-focused unit that standardises methods and tools towards a "
            "partner tailored to the organisation's strategy.",
        ),
        S(
            "What does a PMO do?",
            "What a PMO does depends on the problem it was set up to solve, but most PMO services fall into eight "
            "areas. Few PMOs offer all of them, and a new PMO should not try to.",
            T(
                ["Service area", "Typical activities", "What good looks like"],
                ["Governance", "Stage gates, approval workflows, assurance reviews, decision logs", "Decisions are made at the right level, quickly, with clear criteria. See [project governance](/project-management/project-governance/)"],
                ["Standards and methods", "Lifecycle, templates, tailoring rules, guidance", "A light, documented method that teams actually follow"],
                ["Reporting", "Status reports, portfolio dashboards, RAG ratings, executive packs", "One version of the truth, produced from live data, not retyped"],
                ["Portfolio support", "Intake, prioritisation, business case review, roadmap", "Leaders can see what is running, what is queued and why"],
                ["Resources and capacity", "Capacity plans, allocation across projects, conflict resolution", "Clashes for key people spotted weeks before they cause delays"],
                ["Capability", "Training, coaching, onboarding, community of practice", "Project managers improve and new starters ramp up quickly"],
                ["Tools", "Administering the project management platform, templates, integrations", "Data is entered once and reused for every report"],
                ["Knowledge", "Lessons learned, estimating data, risk libraries", "Lessons from one project change how the next one is planned"],
            ),
            H3("A typical month in a PMO"),
            "To make this concrete, here is what an illustrative month looks like for a three-person PMO supporting "
            "around 30 projects:",
            T(
                ["Week", "Main activities"],
                ["Week 1", "Collect status updates, check data quality, publish the portfolio dashboard, flag projects with red or worsening ratings"],
                ["Week 2", "Portfolio review meeting with executives; prepare decision papers for new requests and change requests; update the capacity plan"],
                ["Week 3", "Stage gate reviews for projects reaching a decision point; coaching sessions; one assurance health check"],
                ["Week 4", "Lessons learned workshop for a closing project; improve one template or process; plan next month's priorities"],
            ),
            "The PMO also answers ad hoc questions, maintains the "
            "[RAID log](/project-management/raid-log/) for cross-project risks and dependencies, and keeps the tool "
            "configuration tidy.",
        ),
        S(
            "Types of PMO: supportive, controlling and directive",
            "The best-known classification groups PMOs by how much control they have over projects. It was "
            "popularised by earlier editions of the PMBOK Guide and remains the standard answer in exams and job "
            "interviews.",
            T(
                ["", "Supportive", "Controlling", "Directive"],
                ["Level of control", "Low", "Medium", "High"],
                ["Main role", "Advise and provide resources", "Set standards and check compliance", "Manage projects directly"],
                ["Who project managers report to", "Their business unit", "Their business unit, with PMO oversight", "The PMO"],
                ["Typical services", "Templates, training, lessons learned, coaching", "Mandatory methods, reviews, reporting, stage gates", "Staffing, running and closing projects"],
                ["Best for", "Organisations with capable teams that want consistency without central control", "Regulated or high-risk work, or organisations with uneven delivery", "Strategic, high-value portfolios where central accountability is needed"],
                ["Main risk", "Being ignored because nothing is required", "Being seen as bureaucracy", "Cost, and becoming a bottleneck"],
            ),
            H3("Supportive PMO"),
            "A supportive PMO acts as a consultant and library. It offers templates, training, expertise and lessons "
            "from previous projects, but does not insist that anyone use them. It works well where project managers "
            "are experienced and the main problem is inconsistency, or as a first step in an organisation wary of "
            "central control. Its weakness is that its influence depends entirely on being useful.",
            H3("Controlling PMO"),
            "A controlling PMO requires compliance. Projects must use agreed methods, templates and tools, submit "
            "regular reports and pass reviews or stage gates. It suits regulated industries, organisations with "
            "repeated delivery problems and portfolios where executives need reliable data. To avoid becoming pure "
            "overhead, a controlling PMO should tailor its rules to project size and risk.",
            H3("Directive PMO"),
            "A directive PMO manages projects itself. Project managers are employed by, or report to, the PMO and are "
            "assigned to projects as needed. This gives the most consistency and the clearest accountability, and "
            "suits organisations where projects are the main way strategy is delivered. It is also the most "
            "expensive model and needs strong leadership to avoid becoming a bottleneck.",
            H3("How to choose the right type"),
            "Answer these questions honestly before you decide:",
            OL(
                "**What problem are we solving?** Poor visibility usually needs a reporting-led supportive or controlling PMO; repeated failure of strategic projects may need a directive one.",
                "**How mature is project delivery today?** Teams with little experience need more support and more structure.",
                "**How much regulation or risk is involved?** Audit, safety and financial controls push towards a controlling model.",
                "**What will executives actually back?** A directive PMO without visible executive support will fail.",
                "**What can we afford?** Each step up in control adds people and process.",
            ),
            "Many PMOs are hybrids: directive for a handful of strategic projects, controlling for large ones and "
            "supportive for everything else.",
        ),
        S(
            "PMO levels and structures",
            "A second way to classify PMOs is by the scope of work they cover. An organisation can have several of "
            "these at once.",
            T(
                ["Level", "Scope", "Typical focus", "Lifespan"],
                ["Project office", "One large project", "Planning, scheduling, reporting, document control", "Temporary"],
                ["Programme office", "One programme of related projects", "Dependencies, benefits, programme reporting", "Temporary"],
                ["Departmental PMO", "All projects in a function, such as IT, engineering or marketing", "Standards, reporting and resourcing for that function", "Permanent"],
                ["Enterprise PMO (EPMO)", "All projects across the organisation", "Strategic alignment, portfolio decisions, enterprise reporting", "Permanent"],
                ["Portfolio office", "The investment portfolio", "Prioritisation, funding, capacity, benefits tracking", "Permanent"],
                ["Centre of excellence", "Methods and capability across all levels", "Standards, training, tools, continuous improvement", "Permanent"],
            ),
            "The P3O (Portfolio, Programme and Project Offices) guidance, now owned by the PeopleCert group, uses a "
            "similar model: portfolio, programme and project offices, supported by a centre of excellence that owns "
            "standards and capability.",
            H3("Centralised, federated and virtual PMOs"),
            T(
                ["Structure", "How it works", "Strengths", "Watch out for"],
                ["Centralised", "One PMO serves the whole organisation", "Consistency, one data set, economies of scale", "Distance from the front line"],
                ["Federated (hub and spoke)", "A central PMO sets standards; departmental PMOs apply them locally", "Local knowledge with common reporting", "Duplicated effort and local variations"],
                ["Virtual", "PMO roles are part-time duties held by people in delivery teams", "Low cost, close to the work", "Work slips when delivery is busy"],
            ),
            "Organisations that deliver mainly through Agile teams often reshape the PMO around flow, outcomes and "
            "portfolio funding rather than project plans. See our guides to the "
            "[Agile PMO](/project-management/agile/agile-pmo/) and "
            "[Agile portfolio management](/project-management/agile/agile-portfolio-management/).",
        ),
        S(
            "PMO roles and responsibilities",
            "Job titles vary, but most PMOs are built from the roles below. A small PMO may combine several of them "
            "in one person.",
            T(
                ["Role", "Typical responsibilities", "Useful background"],
                ["Head of PMO or PMO director", "Sets the PMO's direction, reports to executives, owns the PMO's value and budget", "Senior delivery or programme management, stakeholder skills"],
                ["PMO manager", "Runs PMO services day to day, manages PMO staff, improves processes", "Project management, process design"],
                ["Portfolio manager", "Runs intake and prioritisation, balances the portfolio against capacity and strategy", "Business analysis, finance, strategy"],
                ["PMO analyst", "Collects and checks data, builds dashboards and reports, supports governance", "Data and spreadsheet skills, attention to detail"],
                ["Planner or scheduler", "Builds and maintains integrated schedules, critical path and dependency analysis", "Scheduling tools and techniques"],
                ["PMO coordinator or support officer", "Administration, document control, meeting support, onboarding", "Organisation and communication; a common entry role"],
                ["Project and programme managers", "In a directive PMO, deliver projects and report to the PMO", "Delivery experience and certification"],
            ),
            "The PMO coordinator role overlaps with the [project coordinator](/project-management/project-coordinator/) "
            "role, and many people move between them.",
            H3("How big should a PMO be?"),
            "There is no reliable universal ratio of PMO staff to projects; it depends on the services offered and "
            "how much is automated. Size the PMO from its service catalogue instead: estimate the hours each service "
            "needs per month, add time for improvement work and convert to people using "
            "full-time equivalents (FTE). A reporting-only PMO with "
            "good tooling can be very lean; a directive PMO that employs the project managers is much larger.",
        ),
        S(
            "PMO vs project manager vs programme manager",
            T(
                ["", "Project manager", "Programme manager", "PMO"],
                ["Focus", "One project", "A group of related projects and their combined benefits", "Many projects, and how they are run"],
                ["Main question", "How do we deliver this project?", "How do these projects together deliver the benefits?", "How do we deliver all our projects well, and can we see them?"],
                ["Authority", "Over the project team and plan", "Over the programme and its projects", "From advisory to directive, depending on type"],
                ["Lifespan", "Temporary", "Temporary, often several years", "Usually permanent"],
                ["Typical outputs", "Plan, schedule, status report, deliverables", "Roadmap, benefits plan, programme reports", "Standards, dashboards, governance, capacity plans"],
            ),
            "Read our comparison of [project manager vs programme manager](/project-management/project-manager-vs-program-manager/) for a closer look at the first two roles.",
        ),
        S(
            "How to set up a PMO step by step",
            OL(
                "**Define the problem.** Interview executives, sponsors and project managers. Write down the two or three problems the PMO must solve, such as \"we cannot see which projects are late\" or \"the same specialists are booked on four projects at once\".",
                "**Find a sponsor.** A senior executive must own the PMO, defend its mandate and attend its key forums. Without one, a PMO cannot enforce anything.",
                "**Agree the type, level and scope.** Decide whether the PMO is supportive, controlling or directive, which projects it covers, and which it does not. Many start with projects above a size or risk threshold.",
                "**Design a short service catalogue.** Choose three to five services that address the problems from step 1. Write what each service provides, who it is for and how often.",
                "**Write a PMO charter.** Record purpose, scope, services, authority, roles, funding and success measures, and have the sponsor approve it. Our [project charter template](/templates/project-charter-template/) is a good starting structure.",
                "**Set minimum standards.** Agree a light lifecycle, a one-page [status report](/project-management/project-status-report/), a risk register format and a change control route. Scale them by project size so small projects are not overloaded.",
                "**Choose one shared tool.** Put all in-scope projects in one platform so data is entered once. See [how to choose project management software](/project-management/how-to-choose-project-management-software/).",
                "**Set the reporting and governance rhythm.** Fix dates for status updates, the portfolio review and stage gates, and publish them for the year.",
                "**Pilot with friendly projects.** Test templates and reports with two or three willing project managers, then fix what does not work.",
                "**Roll out and support.** Train project managers, offer drop-in help and show them what they get back.",
                "**Measure and publish results.** Track the KPIs agreed in the charter and report them to the sponsor every quarter.",
                "**Expand deliberately.** Add services only when the current ones run well and there is demand.",
            ),
            H3("A 90-day plan for a new PMO"),
            T(
                ["Period", "Goals", "Outputs"],
                ["Days 1-30: understand", "Interview stakeholders, list all projects, assess current practice", "Project inventory, problem statement, draft charter"],
                ["Days 31-60: design and pilot", "Agree services, standards and tool; pilot reporting", "Approved charter, status template, first draft dashboard"],
                ["Days 61-90: launch", "Roll out to all in-scope projects; first portfolio review", "Live dashboard, governance calendar, first quick wins reported"],
            ),
            H3("What to include in a PMO charter"),
            L(
                "Purpose and the problems the PMO will solve",
                "Sponsor and reporting line",
                "Type (supportive, controlling or directive) and scope: which projects, departments and thresholds",
                "Service catalogue with service levels, such as \"dashboard published by the fifth working day\"",
                "Authority: what the PMO can require, approve or stop",
                "Roles, staffing and budget",
                "Success measures and how often they are reported",
                "Review date for the charter itself",
            ),
            TIP("Write the charter in the language of the problem, not of process. \"Executives will see the status of "
                "every project over £100,000 on one page by the fifth working day of each month\" wins more support "
                "than \"implement portfolio reporting standards\"."),
        ),
        S(
            "Worked example: a new PMO in a 40-project organisation",
            "This example is illustrative. A professional services firm runs about 40 internal and client projects "
            "at any time. There is no shared tool, status reports arrive in five different formats, and the "
            "leadership team learns about problems only when a client complains.",
            H3("Quarter 1: visibility"),
            L(
                "The operations director sponsors a two-person supportive PMO: a PMO manager and a PMO analyst.",
                "The charter names two problems: no single view of project health, and specialists double-booked across projects.",
                "The PMO builds a project inventory (it finds 46 projects, not 40) and introduces a one-page status template with RAG ratings, forecast finish date and top three risks.",
                "All projects move into one work management platform; the analyst builds a portfolio dashboard from live data.",
                "The first monthly portfolio review takes place in week 10.",
            ),
            H3("Quarter 2: capacity and decisions"),
            L(
                "A simple [capacity planning](/project-management/capacity-planning/) sheet shows that two senior engineers are allocated at about 180% of their time over the next eight weeks.",
                "The leadership team delays one internal project by six weeks to free them, and records the decision.",
                "Two projects with overlapping scope are merged into one.",
                "A light stage gate is introduced for new projects above an agreed budget, using a short [business case template](/templates/business-case-template/).",
            ),
            H3("Results after two quarters"),
            T(
                ["Measure", "Start", "After 6 months"],
                ["Projects with a current status report", "Unknown (no central list)", "All 46"],
                ["Time to produce the executive portfolio pack", "About 3 days of manual collation", "Half a day, mostly review"],
                ["Resource conflicts identified in advance", "None tracked", "7, of which 5 resolved before they caused delay"],
                ["Projects stopped or merged after review", "0", "3"],
            ),
            "The figures are illustrative, but the pattern is typical: the first wins come from simply seeing all "
            "the work in one place. Only after that does the PMO earn the authority to introduce stage gates and "
            "move towards a controlling model for larger projects.",
        ),
        S(
            "PMO KPIs and how to measure value",
            "A PMO costs money, so it must show what it returns. Choose a few measures linked to the problems in "
            "the charter, set a baseline and report the trend.",
            T(
                ["KPI", "How to measure it", "Why it matters"],
                ["On-time delivery", "% of projects finishing within an agreed tolerance of the baselined date", "The most visible sign of delivery reliability"],
                ["Forecast accuracy", "Gap between forecast and actual finish dates or costs", "Shows whether reports can be trusted"],
                ["Schedule and cost performance", "SPI and CPI from [earned value management](/project-management/earned-value-management/)", "Objective view of progress against plan"],
                ["Benefits realised", "Benefits achieved vs the business case", "Links projects to business value"],
                ["Portfolio alignment", "% of spend on projects linked to a strategic objective", "Shows the PMO is steering, not just counting"],
                ["Decision speed", "Days from request to approval or rejection", "Slow governance is a common complaint"],
                ["Resource conflicts resolved early", "Number of clashes flagged and resolved before causing delay", "Direct evidence of preventive value"],
                ["Stakeholder satisfaction", "Short survey of executives and project managers", "Captures whether the PMO is seen as useful"],
            ),
            "Avoid vanity measures such as the number of templates published or reports collected: they show "
            "activity, not value.",
        ),
        S(
            "PMO maturity: from administrator to strategic partner",
            "PMOs usually grow through recognisable stages. Several PMO maturity models exist, and the PMBOK Guide 8th "
            "edition appendix on PMOs discusses maturity models; the simplified view below is a practical summary "
            "rather than any one official model.",
            T(
                ["Stage", "What the PMO does", "Typical evidence", "Next step"],
                ["1. Administrative", "Collects reports and maintains templates", "Status reports exist but are inconsistent", "Standardise reporting and data"],
                ["2. Standardising", "Sets common methods and reporting", "One status format, one tool, regular portfolio review", "Add governance and capacity planning"],
                ["3. Controlling", "Runs governance, stage gates and assurance", "Decisions documented; struggling projects spotted early", "Link projects to strategy and benefits"],
                ["4. Portfolio-driven", "Supports prioritisation and funding decisions", "Projects stopped or reprioritised based on data", "Track benefits and improve continuously"],
                ["5. Strategic partner", "Shapes strategy execution with leadership", "PMO leader part of planning and investment forums", "Sustain, adapt to new ways of working"],
            ),
            "Do not try to jump stages. A PMO that introduces portfolio prioritisation before it has reliable "
            "project data will base decisions on guesses.",
        ),
        S(
            "Why PMOs fail and how to avoid it",
            T(
                ["Failure mode", "What it looks like", "How to avoid it"],
                ["Bureaucracy without value", "Project managers fill in forms and get nothing back", "Give something back for every request: help with risks, resources or escalations"],
                ["No executive sponsor", "Rules are ignored with no consequence", "Secure a named sponsor before launch and involve them in portfolio reviews"],
                ["Unclear purpose", "The PMO tries to do everything at once", "Limit the service catalogue to the problems in the charter"],
                ["One-size-fits-all process", "Small projects buried in paperwork", "Tailor standards by project size, risk and delivery approach"],
                ["Reporting the past", "Reports explain what went wrong last month", "Report forecasts, trends and decisions needed"],
                ["Tool before process", "An expensive platform nobody uses consistently", "Agree the minimum data and process first, then configure the tool"],
                ["Not measuring itself", "The PMO cannot answer \"what have you done for us?\"", "Baseline KPIs at launch and report quarterly"],
            ),
            "Most of these share one root cause: the PMO was set up to control rather than to help. Effective PMOs "
            "behave like a service, with project managers as their main customers.",
        ),
        S(
            "PMO tools and software",
            "A PMO needs one place where project data lives, so reports can be generated rather than assembled by "
            "hand. Most PMOs use a work or portfolio management platform plus a reporting tool. Options from our "
            "reviews:",
            L(
                "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool (9.4/10), combines projects, request "
                "intake, workflows, resource planning and dashboards that pull data from across projects; its top "
                "plans add deeper portfolio, financial and resource analysis aimed at PMO-level insight.",
                "**[Smartsheet](/project-management-tools/smartsheet/)** offers a spreadsheet-style grid with Gantt "
                "charts, dependencies and roll-up reporting, and its scheduling depth is a key reason PMOs choose it.",
                "**[monday.com](/project-management-tools/monday/)** is easy to adopt, with dashboards across boards and "
                "prebuilt AI agents for PMO tasks such as project intake, status reporting and portfolio health; "
                "portfolio and resource management arrive on the Pro and Enterprise plans.",
                "**[Asana](/project-management-tools/asana/)** connects projects to portfolios and goals on its "
                "Advanced plan, which suits organisations coordinating work across many teams.",
                "**[Microsoft Planner](/project-management-tools/microsoft-planner/)** Plan 3 adds portfolios, "
                "baselines and the critical path for organisations already on Microsoft 365.",
            ),
            "Compare them side by side on our [tool comparison page](/project-management-tools/compare/). If you "
            "are not ready for a platform, start with a shared spreadsheet based on our "
            "[project tracker template](/templates/project-tracker-template/) and "
            "[RAID log template](/templates/raid-log-template/).",
        ),
        S(
            "PMO careers and certification",
            "PMO work suits people who like organisation, data and seeing the bigger picture. A common path is PMO "
            "coordinator or support officer, then PMO analyst, then PMO manager or portfolio manager. Many PMO leaders "
            "also have project or programme management experience.",
            T(
                ["Certification", "Body", "Relevance to PMO work"],
                ["PMI Project Management Office Certified Professional (PMI-PMOCP)", "PMI", "Dedicated PMO credential. Requires a secondary degree, 3 years of project-related experience in the last 8 years or a current PMP, and 10 hours of PMO education; the exam has 120 questions in 165 minutes"],
                ["P3O Foundation and Practitioner", "PeopleCert", "Designing and running portfolio, programme and project offices, popular in the UK"],
                ["[PMP](/project-management/pmp-certification/)", "PMI", "Broad project management credential, often expected for PMO manager roles"],
            ),
            "The PMI-PMOCP builds on the PMO-CP certification that PMI acquired from the PMO Global Alliance in 2023. "
            "Check the current requirements on PMI's site before you apply. For a wider view of the options, see our "
            "guide to [project management certification](/project-management/project-management-certification/).",
            "Read our guide to [managing multiple projects](/project-management/managing-multiple-projects/) for the techniques PMO staff and project managers use to keep a portfolio on track.",
        ),
    ],
    faq=[
        ("What is a PMO in project management?",
         "A project management office: a team or function that sets standards for how projects are run and supports, "
         "monitors or directly manages them across a department or organisation."),
        ("What does PMO stand for?",
         "Usually project management office. It can also mean programme management office or portfolio management "
         "office, depending on what the office supports."),
        ("What are the three types of PMO?",
         "Supportive (low control: templates, training and advice), controlling (medium control: required methods, "
         "reporting and reviews) and directive (high control: the PMO manages projects directly)."),
        ("What does a PMO do day to day?",
         "Collects and checks project data, publishes dashboards, supports portfolio and stage gate reviews, resolves "
         "resource conflicts, coaches project managers and maintains templates and tools."),
        ("What is the difference between a PMO and a project manager?",
         "A project manager delivers one project. A PMO supports and oversees many projects, sets common standards "
         "and gives leaders a consolidated view."),
        ("What is an enterprise PMO?",
         "An enterprise PMO (EPMO) works at organisation level. It links projects to strategy, supports portfolio "
         "decisions and provides enterprise-wide reporting and standards."),
        ("How many people does a PMO need?",
         "It depends on its services. Estimate the effort for each service in your catalogue and convert it to FTE; "
         "a reporting-focused PMO with good tooling can start with one or two people."),
        ("How long does it take to set up a PMO?",
         "A basic PMO with reporting and a governance rhythm can be running in about three months. Reaching a "
         "mature, portfolio-driven PMO usually takes a few years."),
        ("What are good PMO KPIs?",
         "On-time delivery, forecast accuracy, schedule and cost performance, benefits realised, portfolio "
         "alignment, decision speed, resource conflicts resolved early and stakeholder satisfaction."),
        ("Why do PMOs fail?",
         "Mostly through adding bureaucracy without value, lacking executive sponsorship, trying to do too much at "
         "once and failing to measure and show their own value."),
        ("Does an Agile organisation need a PMO?",
         "Many still have one, reshaped as an Agile PMO or value management office that supports portfolio "
         "funding, flow, dependencies and outcomes rather than detailed plans."),
        ("Is there a PMO certification?",
         "Yes. PMI offers the PMI Project Management Office Certified Professional (PMI-PMOCP), and PeopleCert offers "
         "P3O Foundation and Practitioner. The PMP is also common among PMO managers."),
        ("Is a PMO the same as a portfolio office?",
         "Not quite. A portfolio office focuses on choosing and balancing the investments; a PMO focuses on how "
         "projects are delivered. In practice many PMOs do both."),
    ],
)
