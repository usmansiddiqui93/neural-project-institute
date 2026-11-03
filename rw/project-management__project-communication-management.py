from core import S, L, OL, T, TIP, H3

URL = "/project-management/project-communication-management/"

RW = dict(
    title="Project Communication Management: Processes and Examples",
    desc="Project communication management explained: the three processes, push, pull and interactive methods, the channels formula, a worked example and steps.",
    intro=(
        "Project communication management is the work of making sure the right people get the right project "
        "information, in the right format and at the right time, and that they understand it and act on it. It has "
        "three parts: planning communication, delivering it and monitoring whether it works. This guide explains each "
        "process, the methods and formulas you need, and a full worked example you can adapt."
    ),
    takeaways=[
        "Communication management has three processes: plan communications management, manage communications and monitor communications.",
        "In the PMBOK Guide 8th edition the three communication processes sit inside the Stakeholders performance domain, according to published summaries.",
        "Match the method to the message: interactive for decisions and sensitive topics, push for things people must receive, pull for reference material.",
        "Communication channels grow quickly with team size: n(n - 1) / 2, so 10 people have 45 channels and 12 people have 66.",
        "Sending is not communicating. Build in feedback, measure whether messages land and adjust the plan.",
        "Keep one source of truth for status, decisions and documents so people are not chasing information across tools.",
    ],
    sections=[
        S(
            "What is project communication management?",
            "**Project communication management** is the set of processes a project uses to plan, create, distribute, "
            "store and monitor project information. Its aim is simple: every stakeholder gets the information they "
            "need, in a form they can use, when they need it, and the project team can confirm that messages have been "
            "understood and acted on.",
            "In practice it covers all the information that flows around a project: status reports, steering "
            "committee papers, meeting notes, change decisions, risk escalations, team updates, supplier "
            "correspondence and announcements to end users. It covers formal and informal communication, and people "
            "inside and outside the organisation.",
            "Two related documents are often confused:",
            L(
                "**The communication management plan** is the part of the "
                "[project management plan](/project-management/project-management-plan/) that sets the rules: "
                "audiences, information needs, methods, frequency, owners, escalation routes, templates, storage and "
                "how the plan will be reviewed.",
                "**The communication plan** (or communication matrix) is the working schedule that comes out of it: a "
                "table of who receives what, how, when and from whom. On smaller projects the two are usually one "
                "short document.",
            ),
            "The project manager sits at the centre of this flow. You will often see the claim that project managers "
            "spend 90% of their time communicating; it is widely repeated, but we could not trace it to a solid study, "
            "so treat it as a figure of speech. What is clear is that most project management work, from running "
            "meetings to negotiating scope and reporting to the sponsor, is communication.",
            "See our step-by-step guide to writing a [communication plan](/project-management/communication-plan/) for the document itself.",
        ),
        S(
            "Why communication management matters",
            "Many project problems that look technical start as communication problems. A sponsor is surprised by a "
            "delay the team knew about for weeks. A supplier delivers to the old specification because a change "
            "decision never reached them. Scope is disputed because an agreement was never recorded.",
            "Good communication management prevents these failures. It:",
            L(
                "Keeps stakeholders informed and engaged, so support does not quietly fade.",
                "Gets decisions made on time, because the people who decide have what they need in a form they can act on.",
                "Reduces misunderstanding about scope, priorities and responsibilities.",
                "Makes risks and issues visible while they are still cheap to fix.",
                "Creates a record of decisions and agreements that protects everyone when memories differ.",
            ),
            "The best-known evidence comes from PMI's Pulse of the Profession in-depth report on communications, "
            "published in May 2013. It found that US$135 million was at risk for every US$1 billion spent on "
            "projects, and that 56% of that amount (US$75 million) was at risk because of ineffective communications. "
            "The same report found that one in five projects was unsuccessful because of ineffective communications, "
            "and that 55% of project managers agreed effective communication with all stakeholders was the most "
            "critical success factor. The data is more than a decade old, so treat it as an indication, not a current measure.",
        ),
        S(
            "The three communication management processes",
            "The PMBOK Guide sixth edition defines Project Communications Management as one of ten knowledge areas, "
            "with three processes. They form a cycle that repeats throughout the project: you plan, you deliver, you "
            "check, and you feed what you learn back into the plan.",
            T(
                ["Process", "Key question", "Main inputs", "Main outputs"],
                ["Plan communications management", "Who needs what information, why, when, how and from whom?", "Project charter, stakeholder register, organisational standards", "Communication management plan"],
                ["Manage communications", "Are we creating, sending and storing information as planned?", "Communication plan, work performance reports, issue and change logs", "Project communications (reports, presentations, notes), updated records"],
                ["Monitor communications", "Is communication working, and what should change?", "Communications sent, feedback, stakeholder engagement", "Work performance information, change requests, plan updates"],
            ),
            H3("Plan communications management"),
            "Planning starts from your stakeholder analysis. For each person or group you work out their information "
            "needs, how much detail they want, how they prefer to receive it, how often, and who on the team is "
            "responsible. You also set the rules that apply to everyone: where documents live, which template a status "
            "report uses, how quickly urgent issues are escalated, and any constraints such as confidentiality, "
            "language or time zones. Planning happens early, but it is revisited at every phase.",
            H3("Manage communications"),
            "This is the delivery process: writing and sending reports, running meetings, publishing updates, "
            "answering questions and storing records so people can find them later. Managing communications is not "
            "only about pushing information out. It includes choosing words carefully, checking understanding during "
            "conversations and making sure the record of decisions is complete.",
            H3("Monitor communications"),
            "Monitoring checks whether communication is achieving its purpose. Are decisions being made on time? Are "
            "people asking the same questions repeatedly? Are stakeholders surprised by things that were reported? "
            "When the answer shows a gap, you adjust the plan: a different method, a different frequency, a different "
            "messenger or a different level of detail.",
        ),
        S(
            "Communication management in PMBOK 7 and PMBOK 8",
            "If you are studying for an exam or working with an organisation that follows PMI standards, it helps to "
            "know how the topic has moved between editions of the [PMBOK Guide](/project-management/pmbok-guide/).",
            T(
                ["Edition", "Structure", "Where communication sits"],
                ["6th edition (2017)", "Ten knowledge areas, five process groups", "Its own knowledge area, Project Communications Management, with three processes"],
                ["7th edition (2021)", "Twelve principles, eight performance domains, no processes", "No separate area; communication runs through the Stakeholders and Team performance domains"],
                ["8th edition (November 2025)", "Six principles, seven performance domains, processes reintroduced in a non-prescriptive form", "Inside the Stakeholders performance domain, alongside the stakeholder engagement processes"],
            ),
            "According to published summaries of the 8th edition, the Stakeholders performance domain contains seven "
            "processes: identify stakeholders, plan stakeholder engagement, plan communications management, manage "
            "stakeholder engagement, manage communications, monitor stakeholder engagement and monitor communications. "
            "The practical message is that communication is treated as one of the main tools of "
            "[stakeholder management](/project-management/project-stakeholder-management/), not as a separate "
            "discipline.",
        ),
        S(
            "Communication methods: interactive, push and pull",
            "The PMBOK Guide groups communication methods into three types. Choosing the right one for each message "
            "is one of the simplest ways to improve communication on a project.",
            T(
                ["Method", "How it works", "Examples", "Best for", "Watch out for"],
                ["Interactive", "Two-way, real-time exchange between two or more people", "Meetings, phone and video calls, workshops, instant messaging conversations", "Decisions, complex or sensitive topics, conflict, building relationships", "Costly in people's time; decisions need recording afterwards"],
                ["Push", "Sent to specific recipients, who do not have to ask for it", "Emails, status reports, memos, newsletters, notifications", "Information people must receive, such as decisions, deadlines and warnings", "Sending does not prove it was read or understood"],
                ["Pull", "Stored centrally for people to access when they choose", "Intranet pages, shared drives, project dashboards, knowledge bases, recorded briefings", "Reference material, large audiences, detail some people want and others do not", "People may never look; needs signposting"],
            ),
            H3("Which method for which message?"),
            "Use this rule of thumb when you are unsure:",
            T(
                ["Message", "Recommended method", "Why"],
                ["A decision is needed from the sponsor", "Interactive, followed by a short written record (push)", "Discussion surfaces concerns; the record prevents later disputes"],
                ["Weekly progress", "Push (status report) plus pull (live dashboard)", "Regular rhythm for those who must know; detail for those who want it"],
                ["Bad news, such as a missed milestone", "Interactive first, then push", "People should hear bad news from you directly, with options"],
                ["Policy, process or training material", "Pull, announced by push", "Large audience, used when needed"],
                ["Changes affecting end users", "Push and interactive briefings through line managers", "People trust messages from their own manager"],
            ),
        ),
        S(
            "Types of project communication",
            "Beyond the three methods, it is useful to think about the type of communication, because each has its "
            "own expectations about tone, formality and record-keeping.",
            T(
                ["Type", "Description", "Examples"],
                ["Formal", "Structured, planned and usually recorded", "Steering committee papers, contracts, change requests, sign-offs"],
                ["Informal", "Unplanned, conversational", "Corridor chats, quick calls, chat messages"],
                ["Written", "Permanent and easy to share", "Reports, emails, meeting notes, documentation"],
                ["Verbal", "Faster, with tone and immediate feedback", "Stand-ups, presentations, phone calls"],
                ["Internal", "Within the project or organisation", "Team updates, briefings to department heads"],
                ["External", "With customers, suppliers, regulators or the public", "Supplier progress meetings, client reports, press statements"],
            ),
            "A useful habit is to **follow informal communication with a formal record when it matters**. If a "
            "decision is agreed in a hallway conversation, send a two-line note confirming it, and log it in the "
            "decision or [issue log](/project-management/issue-log/).",
        ),
        S(
            "The sender-receiver communication model",
            "The basic communication model in project management texts describes how a message travels from one "
            "person to another, and where it can go wrong.",
            OL(
                "**Encode.** The sender turns an idea into words, numbers or images.",
                "**Transmit.** The message is sent through a channel: email, meeting, report, call.",
                "**Decode.** The receiver interprets the message, through their own knowledge and assumptions.",
                "**Acknowledge.** The receiver confirms they have received it. This is not the same as agreeing or understanding.",
                "**Feedback.** The receiver responds, showing whether the meaning came across as intended.",
            ),
            "Anything that distorts the message along the way is called **noise**: jargon, a poor connection, a "
            "distracted reader, cultural differences, or a 40-page report when the reader wanted one page. The "
            "interactive version of the model stresses the last two steps: communication is only complete when the "
            "sender has checked that the receiver understood.",
        ),
        S(
            "Communication channels formula",
            "Every pair of people on a project is a potential communication channel. The number of channels grows "
            "much faster than the number of people, which is why communication gets harder as projects grow.",
            "The formula is **n(n - 1) / 2**, where n is the number of people (including the project manager).",
            T(
                ["People (n)", "Calculation", "Channels"],
                ["5", "5 x 4 / 2", "10"],
                ["8", "8 x 7 / 2", "28"],
                ["10", "10 x 9 / 2", "45"],
                ["12", "12 x 11 / 2", "66"],
                ["20", "20 x 19 / 2", "190"],
            ),
            H3("Worked example: channels added"),
            "Exam questions often ask how many channels are **added** when people join. Calculate both totals and "
            "subtract:",
            OL(
                "A team has 10 people: 10 x 9 / 2 = 45 channels.",
                "Two people join, so n = 12: 12 x 11 / 2 = 66 channels.",
                "Channels added = 66 - 45 = 21.",
            ),
            "Read the question carefully: \"a project manager and 9 team members\" means n = 10.",
            "The number is not a target. Its practical lesson is that you cannot rely on everyone talking to everyone. "
            "As teams grow you need structure: clear roles (a [RACI matrix](/project-management/raci-matrix/) helps), "
            "a predictable meeting rhythm, team leads who pass information on, and one place where status and "
            "decisions are published.",
        ),
        S(
            "How to manage project communication step by step",
            "This process works for most projects, whether you follow a predictive, agile or hybrid approach. On a "
            "small project it can take an hour; on a large programme it is a workshop and a formal document.",
            OL(
                "**Identify stakeholders.** Start from the [project charter](/project-management/project-charter/) "
                "and list everyone affected or able to influence the project. Record them in a stakeholder register.",
                "**Analyse their information needs.** For each group, ask what decisions they make, what they need to "
                "know to make them, how much detail they want and how they prefer to receive it.",
                "**Set communication objectives.** Decide what each communication must achieve: inform, consult, gain "
                "approval, build support or prompt action. The objective drives the method.",
                "**Choose methods, frequency and owners.** Match interactive, push or pull to each message, set a "
                "rhythm and name the person responsible for every item.",
                "**Agree rules and escalation routes.** Decide where documents live, which templates to use, response "
                "times for questions, and how issues move up to the sponsor or "
                "[governance](/project-management/project-governance/) board.",
                "**Write the plan and agree it with the sponsor.** Keep it short. A one-page matrix plus a few rules "
                "is usually enough.",
                "**Deliver consistently.** Send reports on the agreed day, using the same format each time, so people "
                "know where to look and can spot changes quickly.",
                "**Monitor and adjust.** Gather feedback, watch the indicators in the measurement section below and "
                "update the plan at each phase or when stakeholders change.",
            ),
            H3("Questions to ask in a communication requirements analysis"),
            L(
                "What decisions does this person or group make, and when?",
                "What happens if they find out late?",
                "How much detail do they want: headline, summary or full data?",
                "Which format do they actually read: email, dashboard, meeting, phone call?",
                "Who do they trust to deliver bad news?",
            ),
            "Free template: our [communication plan template](/templates/communication-plan-template/) has columns "
            "for audience, information, method, frequency, owner and feedback, and comes in beginner, advanced and "
            "expert versions. Pair it with the [RACI matrix template](/templates/raci-matrix-template/) to show who is "
            "informed and who is consulted.",
        ),
        S(
            "Worked example: communication management on an ERP rollout",
            "This example is illustrative. A 9-month ERP rollout has a steering committee, 4 department heads, a "
            "12-person project team, an external implementation partner and 600 end users across two sites.",
            H3("Step 1: the communication matrix"),
            T(
                ["Audience", "What they need", "Method", "Frequency", "Owner"],
                ["Steering committee", "Progress against milestones, top risks, decisions needed", "Meeting plus one-page RAG report (push)", "Monthly, plus by exception", "Project manager"],
                ["Sponsor", "Early warning, decisions, political issues", "One-to-one (interactive)", "Weekly, 30 minutes", "Project manager"],
                ["Department heads", "Impact on their teams, readiness actions, training dates", "Briefing call (interactive) and action list (push)", "Fortnightly", "Change lead"],
                ["Project team", "Tasks, blockers, priorities", "Stand-up and task board (interactive and pull)", "Daily", "Workstream leads"],
                ["Implementation partner", "Deliverables, issues, acceptance status", "Joint progress meeting (interactive), shared RAID log (pull)", "Weekly", "Project manager"],
                ["End users", "What is changing, when, what they must do, training", "Newsletter (push), intranet page (pull), team briefings", "Monthly, weekly in the last 6 weeks", "Change lead"],
            ),
            H3("Step 2: rules and escalation"),
            L(
                "All decisions are recorded in the decision log within one working day of being made.",
                "Status, risks and issues live in one [RAID log](/project-management/raid-log/) in the project tool; email attachments are not the record.",
                "Red issues are escalated to the sponsor the same day by phone, then in writing.",
                "Questions from department heads receive a reply within two working days, even if the reply is \"we are checking\".",
            ),
            H3("Step 3: monitor and adjust"),
            "Three months in, the project manager reviews the indicators. Newsletter open rates are low, the service "
            "desk is already fielding questions about go-live, and a readiness survey shows that only a minority of "
            "end users can say what is changing for them.",
            T(
                ["Signal", "Diagnosis", "Change to the plan"],
                ["Newsletter rarely opened", "Wrong channel for end users; email overload", "Department heads deliver a 5-minute briefing in existing team meetings, using a script and FAQ from the project"],
                ["Repeated questions to the service desk", "Information exists but is hard to find", "Single intranet page with a search-friendly FAQ, linked from every message"],
                ["Steering committee asks for more detail on data migration", "One-page report too thin for the highest risk", "Add a monthly data migration annex with trend charts"],
                ["Partner surprised by a scope decision", "Decision log not shared with partner", "Give the partner read access to the decision log and add a weekly decisions summary"],
            ),
            "The next readiness survey shows a clear improvement, and repeated service desk questions fall. That is "
            "the monitor process doing its job: the plan changed because the evidence showed it was not working.",
        ),
        S(
            "Status reports, meetings and escalation",
            "Most project communication runs through three routines. Getting them right covers a large share of what "
            "stakeholders need.",
            H3("Status reports"),
            "A good [project status report](/project-management/project-status-report/) is short and leads with what "
            "the reader must know or do. A reliable structure:",
            OL(
                "**Overall status** (RAG) and a one-sentence summary.",
                "**Decisions or help needed**, with a date by which they are needed.",
                "**Progress since last report** against milestones, not a list of activities.",
                "**Top risks and issues**, with owner and next action.",
                "**Forecast**: are the end date and budget still achievable?",
                "**Next period**: the main things that will happen.",
            ),
            H3("Meetings"),
            "Meetings are the most expensive communication method, so each one needs a clear purpose, an "
            "agenda and a record. Use a [meeting agenda template](/templates/meeting-agenda-template/) and capture "
            "decisions and actions with a [meeting notes template](/templates/meeting-notes-template/). On agile "
            "teams, the regular events described in our guide to [agile meetings and ceremonies](/project-management/agile/agile-meetings-and-ceremonies/) "
            "replace many traditional status meetings; the [daily scrum](/project-management/scrum/daily-scrum/), for "
            "example, is for the developers to inspect progress and adapt their plan, not a report to a manager.",
            H3("Escalation"),
            T(
                ["Level", "Who decides", "Typical trigger", "Response time"],
                ["1. Team", "Workstream lead", "Task blocked, small slip within float", "Same day"],
                ["2. Project", "Project manager", "Milestone at risk, cross-team conflict", "Within 2 working days"],
                ["3. Sponsor", "Sponsor", "Tolerance breach on time, cost or scope", "Within 1 week, or same day if urgent"],
                ["4. Governance board", "Steering committee", "Change to business case, major scope change", "Next meeting or extraordinary session"],
            ),
            "Write your tolerances into the plan so everyone knows when an issue must move up a level. Changes to "
            "baselines should follow your [change control](/project-management/change-control/) process, and the "
            "decision should be communicated to everyone affected.",
        ),
        S(
            "How to measure whether communication is working",
            "The monitor process needs evidence, not impressions. Pick a handful of indicators that fit your project "
            "and review them at each phase gate or monthly.",
            T(
                ["Indicator", "What it tells you", "How to collect it"],
                ["Decision turnaround", "Whether decision makers get what they need in time", "Days from request to decision in the decision log"],
                ["Repeated questions", "Whether information is clear and easy to find", "Service desk tickets, inbox, FAQ page searches"],
                ["Surprises", "Whether bad news travels early", "Count of issues stakeholders say they heard about late"],
                ["Attendance and engagement", "Whether meetings and briefings are valued", "Attendance, questions asked, actions completed on time"],
                ["Stakeholder feedback", "Whether people feel informed", "Short pulse survey: two or three questions each phase"],
                ["Readiness", "Whether end users understand what is changing", "Readiness survey or quiz before go-live"],
            ),
            TIP("Keep the feedback survey short. Two questions work well: \"How well informed do you feel about the "
                "project?\" (1 to 5) and \"What one thing would make our communication more useful to you?\""),
        ),
        S(
            "Communication barriers and how to overcome them",
            T(
                ["Barrier", "What it looks like", "How to reduce it"],
                ["Information overload", "People stop reading updates; important messages are missed", "Fewer, shorter messages; put the action in the subject line; use dashboards for detail"],
                ["Jargon and acronyms", "Business users nod along but do not understand", "Plain language; a project glossary; test messages on someone outside the team"],
                ["Distance and time zones", "Delays, people left out of decisions", "Agreed core hours, written decision records, recorded briefings; see [remote project management](/project-management/industries/remote-project-management/)"],
                ["Language and culture", "Silence mistaken for agreement; directness mistaken for rudeness", "Check understanding explicitly; written follow-ups; agree team norms"],
                ["Tool sprawl", "Decisions spread across email, chat and documents", "Agree one source of truth for status and decisions; define what each channel is for"],
                ["Unclear ownership", "Everyone assumes someone else told the supplier", "Name an owner for each communication in the plan"],
            ),
            "Many of these are skills as much as processes. Our guide to [project management skills](/project-management/project-management-skills/) "
            "covers listening, writing and negotiation in more depth.",
        ),
        S(
            "Tools for project communication",
            "Tools do not fix communication on their own, but good [project management software](/project-management/project-management-software/) "
            "keeps conversations attached to the work and status in one place. Agree what each tool is for before the project starts.",
            L(
                "[Wrike](/project-management-tools/wrike/) (our top-rated tool) keeps comments, @mentions, approvals "
                "and files on each task, offers dashboards across projects and includes AI comment summaries. Agree "
                "notification habits early, as reviewers mention notification volume.",
                "[monday.com](/project-management-tools/monday/) gives every item an updates thread with comments, "
                "@mentions and files, plus dashboards and guest access, and is quick for teams to pick up.",
                "[Asana](/project-management-tools/asana/) lets project owners publish status updates, and its "
                "portfolios give leaders one view of the health of many projects.",
                "[Microsoft Planner](/project-management-tools/microsoft-planner/) lives inside Teams and Outlook, which "
                "suits organisations that already communicate there.",
            ),
        ),
        S(
            "Common mistakes in project communication",
            L(
                "**One message for everyone.** Executives need decisions and exceptions; teams need detail. Tailor "
                "the same facts for each audience.",
                "**Reporting activity, not outcomes.** \"We held six workshops\" says little. Say what has changed, "
                "what is at risk and what you need.",
                "**Hiding or softening bad news.** Raise problems early, with options and a recommendation. Late bad "
                "news damages trust far more than early bad news.",
                "**No feedback loop.** Sending is not communicating. Check understanding and measure whether messages land.",
                "**Too many channels.** Decisions in chat, documents in email and status in a spreadsheet leave "
                "everyone hunting. Agree one source of truth.",
                "**Plan written once and forgotten.** Stakeholders change between phases. Review the plan at every "
                "phase gate and when key people change.",
                "**Forgetting the end.** At closure, tell people what was delivered, thank contributors and share "
                "[lessons learned](/project-management/lessons-learned/), including lessons about communication.",
            ),
            "Read our guide to [project stakeholder management](/project-management/project-stakeholder-management/) to connect your communication plan with how you engage each group.",
        ),
    ],
    faq=[
        ("What is project communication management?",
         "It is the planning, delivery and monitoring of project information so that stakeholders receive what they "
         "need, when they need it, in a useful format, and understand it."),
        ("What are the three processes of project communication management?",
         "Plan communications management, manage communications and monitor communications. They come from the PMBOK "
         "Guide sixth edition and, according to published summaries, also appear in the 8th edition's Stakeholders "
         "performance domain."),
        ("What is the difference between a communication plan and a communication management plan?",
         "The communication management plan sets the approach and rules: audiences, methods, owners, escalation and "
         "storage. The communication plan, or matrix, is the working schedule of who receives what, how and when. "
         "Small projects often combine them."),
        ("How do you calculate communication channels?",
         "Use n(n - 1) / 2, where n is the number of people. A team of 8 has 8 x 7 / 2 = 28 channels. To find "
         "channels added when people join, calculate both totals and subtract."),
        ("What is the difference between push and pull communication?",
         "Push communication is sent to specific recipients, such as an email or status report. Pull communication is "
         "stored centrally for people to access when they need it, such as an intranet page or dashboard."),
        ("What is interactive communication?",
         "Real-time, two-way exchange such as meetings, calls and workshops. It is best for decisions and for complex "
         "or sensitive topics, and should be followed by a written record of what was agreed."),
        ("How much of a project manager's time is spent communicating?",
         "A large share. The often-quoted figure of 90% could not be traced to a solid study, but most project "
         "management work, including meetings, reporting, negotiating and coordinating, is communication."),
        ("What should a communication management plan include?",
         "Stakeholder groups and their information needs, the information to be shared, methods, frequency, owners, "
         "escalation routes and timescales, templates, where information is stored, constraints such as "
         "confidentiality, and how the plan will be reviewed."),
        ("How do I write a good project status report?",
         "Keep it short and lead with overall status and any decisions needed. Then cover progress against milestones, "
         "top risks and issues, the forecast and what happens next, using the same format every time."),
        ("What are common communication barriers in projects?",
         "Information overload, jargon, time zones and distance, language and cultural differences, unclear "
         "ownership, too many tools and a culture where bad news is delayed."),
        ("How do you monitor project communication?",
         "Track a few indicators, such as decision turnaround, repeated questions, surprises and short survey scores, "
         "ask for feedback, and adjust the plan when the evidence shows something is not working."),
        ("Where is communications management in the PMBOK Guide 8th edition?",
         "There is no separate knowledge area. Published summaries place plan, manage and monitor communications in "
         "the Stakeholders performance domain, one of the edition's seven performance domains."),
        ("What is the role of the kick-off meeting in communication?",
         "It sets a shared starting point. The kick-off should explain the project purpose, objectives, scope, key "
         "milestones, roles and how the team will communicate, so everyone starts with the same understanding."),
    ],
)
