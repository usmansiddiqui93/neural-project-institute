from core import S, L, OL, T, TIP, H3

URL = "/project-management/pmbok-guide/"

RW = dict(
    title="PMBOK Guide 8th Edition: Principles, Domains and Processes",
    desc="The PMBOK Guide 8th edition explained: 6 principles, 7 performance domains, 5 focus areas, 40 processes, what changed and how it links to the PMP.",
    intro=(
        "The PMBOK Guide (A Guide to the Project Management Body of Knowledge) is the Project Management "
        "Institute's standard and guide to good practice in project management, and its current edition is the "
        "eighth, published in November 2025. It combines six principles, seven performance domains and 40 "
        "processes grouped into five focus areas. This guide explains the full structure, what changed from the "
        "6th and 7th editions, and how the book relates to the PMP exam."
    ),
    takeaways=[
        "The PMBOK Guide 8th edition (November 2025) is the current edition; it replaces the 7th edition published in 2021.",
        "It has six principles, seven performance domains (governance, scope, schedule, finance, stakeholders, resources, risk) and five focus areas containing 40 processes.",
        "The 8th edition brings back process guidance that the 7th removed, but presents it as non-prescriptive guidance you tailor, not steps you must follow.",
        "New appendices cover project management offices, artificial intelligence and procurement.",
        "The PMP exam is built on PMI's July 2026 exam content outline, not on the PMBOK Guide alone; use the book as a reference alongside it.",
        "PMBOK is a standard, not a methodology: pair it with a way of working such as predictive, Agile, hybrid or PRINCE2.",
    ],
    sections=[
        S(
            "What is the PMBOK Guide?",
            "The **PMBOK Guide** is the Project Management Institute's foundational publication on project "
            "management. It sets out the principles, performance domains, processes and vocabulary that PMI "
            "regards as good practice for most projects, most of the time. It is a standard and reference, not a "
            "step-by-step methodology, so you tailor it to each project.",
            "PMBOK stands for **Project Management Body of Knowledge**. The body of knowledge itself is the whole "
            "collection of practice in the profession; the Guide is PMI's summary of the generally recognised "
            "part of it. The book is published by [PMI, the Project Management Institute](/project-management/what-is-pmi/), "
            "and it is the best-known reference behind PMI's certifications.",
            "Since the 7th edition, one volume contains two documents:",
            L(
                "**The Standard for Project Management**, the formal standard: what a project is, how projects "
                "create value, the six principles and project life cycles.",
                "**The PMBOK Guide** itself: the seven performance domains and their processes, tailoring, and "
                "reference chapters on inputs, outputs, tools and techniques, plus appendices.",
            ),
            "What it is not: it is not a method that tells you which meeting to hold on which day. Methods such as "
            "[PRINCE2](/project-management/prince2/), Scrum or your organisation's own lifecycle supply that detail. "
            "Think of the PMBOK Guide as the map of what a well-run project must cover, and the method as the route "
            "you choose.",
        ),
        S(
            "The PMBOK Guide 8th edition at a glance",
            T(
                ["Item", "PMBOK Guide 8th edition"],
                ["Full title", "A Guide to the Project Management Body of Knowledge (PMBOK Guide), Eighth Edition, and The Standard for Project Management"],
                ["Publisher", "Project Management Institute (PMI)"],
                ["Published", "November 2025 (digital); the print edition became widely available from January 2026"],
                ["Length", "408 pages, according to PMI"],
                ["Principles", "6"],
                ["Performance domains", "7: governance, scope, schedule, finance, stakeholders, resources, risk"],
                ["Focus areas", "5: initiating, planning, executing, monitoring and controlling, closing"],
                ["Processes", "40, presented as non-prescriptive guidance"],
                ["Appendices", "Contributors, project management offices, artificial intelligence, procurement, evolution of the guide"],
                ["Access", "Free digital copy for PMI members; on sale to non-members through PMI and booksellers"],
            ),
            "PMI describes the update as refreshing key terms and concepts, consolidating the principles, "
            "reintroducing the old process groups as focus areas and bringing technical \"how to\" guidance back "
            "into the performance domains. In short, it keeps the principle-based thinking of the 7th edition and "
            "restores much of the practical structure that readers of the 6th edition missed.",
        ),
        S(
            "Inside The Standard for Project Management",
            "The Standard is the shorter, more formal half of the book. Its four chapters set the foundations that "
            "the rest of the Guide builds on.",
            T(
                ["Chapter", "What it covers"],
                ["1. Introduction", "Purpose of the Standard, key terms, characteristics of a project, how organisational and project governance connect, and how portfolios, programmes, projects and operations relate"],
                ["2. A System for Value Delivery", "How projects create value, how to assess project success, the project environment (enterprise environmental factors, organisational process assets, structures), product management and project roles"],
                ["3. Project Management Principles", "The project management mindset and the six principles, each with its impact, the principle in action and the performance domains it connects to"],
                ["4. Project Life Cycles", "Phases, predictive, adaptive and hybrid development approaches, how to choose one, delivery cadence, and the five focus areas"],
            ),
            "Two ideas from the Standard run through everything else. Projects exist to deliver **value**, judged "
            "by benefits as well as time and cost. And the **development approach** is a choice: predictive, as in "
            "[waterfall project management](/project-management/waterfall-project-management/), adaptive, as in "
            "[Agile project management](/project-management/agile/what-is-agile-project-management/), or a hybrid.",
        ),
        S(
            "The six project management principles",
            "The 7th edition had twelve principles. The 8th consolidates them into six, which describe the mindset "
            "behind good project management rather than the mechanics. The titles below are the chapter headings in "
            "the Standard; some summaries shorten them (for example \"embed quality\" or \"lead accountably\").",
            T(
                ["Principle", "What it means", "What it looks like on a project"],
                ["Adopt a holistic view", "See the project as a system of interacting parts inside a wider organisation", "Checking how a scope change affects cost, risk, people and other projects before approving it"],
                ["Focus on value", "Judge work by the benefits it delivers, not only by outputs", "Re-testing the business case at each phase gate and stopping work that no longer pays back"],
                ["Embed quality into processes and deliverables", "Build quality into how work is done, not just inspect it at the end", "Agreeing acceptance criteria before work starts and reviewing early drafts"],
                ["Be an accountable leader", "Take ownership of outcomes and lead with integrity, whatever your formal role", "Owning a missed milestone openly and setting out the recovery plan"],
                ["Integrate sustainability within all project areas", "Weigh environmental, social and economic effects in decisions", "Including energy use, supplier practices or long-term running costs in option appraisal"],
                ["Build an empowered culture", "Create a team and stakeholder environment where people can collaborate and decide", "Delegating decisions to the people closest to the work, with clear boundaries"],
            ),
            "Sustainability is the most visible new emphasis; the rest will feel familiar from the 7th edition. Our guide to "
            "[project management principles](/project-management/project-management-principles/) explains the "
            "wider set of principles in plain English.",
        ),
        S(
            "The seven performance domains",
            "A performance domain is a group of related activities that are critical to delivering project "
            "outcomes. In the 8th edition the domains are practical subject areas again, much closer to the old "
            "knowledge areas than the 7th edition's more abstract domains. Each domain chapter covers key "
            "concepts, its processes, tailoring considerations, interactions with other domains and how to check "
            "results.",
            T(
                ["Domain", "What it covers", "Processes", "Closest 6th-edition knowledge areas"],
                ["Governance", "Oversight, decision-making, integrated planning, sourcing strategy, quality assurance, knowledge, change and closure", "9", "Integration; parts of quality and procurement"],
                ["Scope", "Requirements, scope definition, the scope structure (such as a WBS), validation and control", "6", "Scope"],
                ["Schedule", "Planning, developing and controlling the schedule, whichever approach you use", "3", "Schedule"],
                ["Finance", "Cost estimates, budget, funding, reserves and financial control", "4", "Cost"],
                ["Stakeholders", "Identifying and engaging stakeholders, and planning and managing communications", "7", "Stakeholder; communications"],
                ["Resources", "People and physical resources: planning, estimating, acquiring, leading the team and control", "5", "Resource"],
                ["Risk", "Threats and opportunities: planning, identification, analysis, responses and monitoring", "6", "Risk"],
            ),
            "Notice what has gone as a separate heading: communications now sits inside stakeholders, quality is "
            "both a principle and a governance process, and procurement is a governance process plus a full "
            "appendix. Integration has become governance, which is broader: it covers how decisions are made and "
            "who makes them, not only how plans fit together. See our guide to "
            "[project governance](/project-management/project-governance/) for how this works in practice.",
        ),
        S(
            "The five focus areas and 40 processes",
            H3("What the focus areas are"),
            "The focus areas reuse the names of the old process groups: **initiating, planning, executing, "
            "monitoring and controlling, and closing**. They describe the type of management attention a project "
            "needs at a given moment. They are not phases: on a multi-phase project you initiate, plan, execute, "
            "monitor and close within every phase, and monitoring and controlling runs throughout. On an adaptive "
            "project the same cycle repeats inside each iteration.",
            H3("The 40 processes by domain and focus area"),
            "The table places each process by domain and focus area. Process names follow published summaries of "
            "the guide; the allocation to focus areas is our reading of the names, so check the guide itself if you "
            "need the exact wording.",
            T(
                ["Domain", "Initiating", "Planning", "Executing", "Monitoring and controlling", "Closing"],
                ["Governance", "Initiate Project or Phase", "Integrate and Align Project Plans; Plan Sourcing Strategy", "Manage Project Execution; Manage Quality Assurance; Manage Project Knowledge", "Monitor and Control Project Performance; Assess and Implement Changes", "Close Project or Phase"],
                ["Scope", "", "Plan Scope Management; Elicit and Analyze Requirements; Define Scope; Develop Scope Structure", "", "Validate Scope; Monitor and Control Scope", ""],
                ["Schedule", "", "Plan Schedule Management; Develop Schedule", "", "Monitor and Control Schedule", ""],
                ["Finance", "", "Plan Financial Management; Estimate Costs; Develop Budget", "", "Monitor and Control Finances", ""],
                ["Stakeholders", "Identify Stakeholders", "Plan Stakeholder Engagement; Plan Communications Management", "Manage Stakeholder Engagement; Manage Communications", "Monitor Stakeholder Engagement; Monitor Communications", ""],
                ["Resources", "", "Plan Resource Management; Estimate Resources", "Acquire Resources; Lead the Team", "Monitor and Control Resources", ""],
                ["Risk", "", "Plan Risk Management; Identify Risks; Perform Risk Analysis; Plan Risk Responses", "Implement Risk Responses", "Monitor Risks", ""],
                ["**Total**", "**2**", "**19**", "**8**", "**10**", "**1**"],
            ),
            "Planning holds almost half of the processes, as it did in the 6th edition, which reflects the number "
            "of subjects that need thinking through, not the share of time planning should take. Compared with the "
            "6th edition's 49 processes, several have been merged: schedule work now has three processes instead "
            "of six, and qualitative and quantitative risk analysis have become one Perform Risk Analysis process. "
            "Our guide to [project management processes](/project-management/project-management-processes/) "
            "shows the classic 49-process matrix if you need to compare the two.",
            TIP(
                "Treat the 40 processes as a checklist of decisions, not a list of documents. A two-month internal "
                "project might cover Plan Risk Management, Identify Risks and Plan Risk Responses in one hour-long "
                "workshop and a [risk register template](/templates/risk-register-template/)."
            ),
        ),
        S(
            "Tailoring, inputs and outputs, tools and techniques",
            "Three further chapters turn the domains into something you can use.",
            L(
                "**Tailoring (chapter 3)** explains why to tailor, what to tailor (life cycle and development "
                "approach, processes, and engagement) and a four-step tailoring process: select the initial "
                "development approach, tailor for the organisation, tailor for the project, and implement ongoing "
                "improvement. It also covers tailoring each performance domain and diagnostics for spotting "
                "where tailoring is needed.",
                "**Inputs and outputs (chapter 4)** describes the documents and artefacts that processes use and "
                "produce, such as the charter, plans, registers and logs.",
                "**Tools and techniques (chapter 5)** describes the methods used to carry out the processes, from "
                "estimating and analysis techniques to meetings and data representation.",
            ),
            "This is a middle path between the 6th edition, which attached inputs, tools and techniques and outputs "
            "(ITTOs) to every process, and the 7th, which replaced them with a looser section on models, methods "
            "and artefacts.",
        ),
        S(
            "The appendices: PMOs, AI and procurement",
            "The appendices are where much of the genuinely new material sits.",
            T(
                ["Appendix", "Topic", "What it covers"],
                ["X1", "Contributors and reviewers", "The people who developed and reviewed the edition"],
                ["X2", "Project management offices", "The PMO value proposition, customer centricity, PMO types, models and structures, and PMO maturity models"],
                ["X3", "Artificial intelligence", "AI in the project context, strategies for AI adoption, the state of the market, common use cases, and responsible use and ethical concerns"],
                ["X4", "Procurement", "Buyer and seller roles, make-or-buy decisions, procurement strategy, bid documents, source selection, contract types and claims"],
                ["X5", "Evolution of the PMBOK Guide", "The evidence base and research behind the edition, the changes it makes, its sources and how the principles were refined"],
            ),
            "The PMO appendix reflects a shift PMI describes from PMOs that enforce process to PMOs that act as "
            "customer-focused partners delivering value. If you run or are setting up one, read it with our guide "
            "to the [project management office (PMO)](/project-management/project-management-office-pmo/). The "
            "procurement appendix restores much of the contract material that was a full knowledge area in the 6th "
            "edition; our guide to [project procurement management](/project-management/project-procurement-management/) "
            "covers the same ground step by step.",
        ),
        S(
            "What changed: 6th vs 7th vs 8th edition",
            "Many study guides, courses and job adverts still refer to older editions, so it helps to know how "
            "they line up.",
            T(
                ["", "6th edition (2017)", "7th edition (2021)", "8th edition (November 2025)"],
                ["Organised around", "Processes", "Principles and outcomes", "Principles, domains and non-prescriptive processes"],
                ["Principles", "None as a list", "12", "6"],
                ["Main structure", "10 knowledge areas, 5 process groups", "8 performance domains", "7 performance domains, 5 focus areas"],
                ["Processes", "49, each with ITTOs", "Removed from the guide (moved to Process Groups: A Practice Guide, 2022)", "40, as guidance"],
                ["Approaches", "Mainly predictive, with Agile considerations", "Predictive, adaptive and hybrid", "Predictive, adaptive and hybrid"],
                ["Notable additions", "Agile content per knowledge area; Agile Practice Guide published alongside", "Value delivery system, tailoring, models, methods and artefacts", "Sustainability principle, governance and finance domains, appendices on PMOs, AI and procurement"],
            ),
            H3("From the 7th to the 8th edition"),
            L(
                "**Fewer principles:** twelve became six, with sustainability added as a principle of its own.",
                "**Different domains:** the 7th edition's domains (stakeholders, team, development approach and "
                "life cycle, planning, project work, delivery, measurement, uncertainty) gave way to seven "
                "subject-based domains.",
                "**Processes are back:** 40 processes within five focus areas, after the 7th edition removed "
                "process detail from the guide.",
                "**More practical content:** domain chapters include processes, tailoring and checks, and the "
                "reference chapters restore inputs, outputs, tools and techniques.",
                "**New topics:** PMOs, artificial intelligence and procurement get dedicated appendices.",
            ),
            H3("Where the ten knowledge areas went"),
            T(
                ["6th-edition knowledge area", "Where it sits in the 8th edition"],
                ["[Integration](/project-management/project-integration-management/)", "Governance domain (planning, execution, knowledge, change and closure processes)"],
                ["[Scope](/project-management/project-scope/)", "Scope domain"],
                ["[Schedule](/project-management/project-scheduling/)", "Schedule domain"],
                ["[Cost](/project-management/project-cost-management/)", "Finance domain"],
                ["[Quality](/project-management/project-quality-management/)", "Principle (embed quality) and Manage Quality Assurance in governance"],
                ["[Resource](/project-management/project-resources/)", "Resources domain"],
                ["Communications", "Stakeholders domain"],
                ["[Risk](/project-management/project-risk-management/)", "Risk domain"],
                ["Procurement", "Plan Sourcing Strategy in governance, plus Appendix X4"],
                ["[Stakeholder](/project-management/project-stakeholder-management/)", "Stakeholders domain"],
            ),
        ),
        S(
            "PMBOK Guide editions history",
            "The body of knowledge grew out of a 1983 PMI report on ethics, standards and accreditation, and PMI "
            "dates the body of knowledge itself to 1987. The first edition of the Guide followed in 1996.",
            T(
                ["Year", "Edition", "What changed"],
                ["1996", "1st edition", "First publication as A Guide to the Project Management Body of Knowledge"],
                ["2000", "2nd edition", "Updated to reflect growth in practice"],
                ["2004", "3rd edition", "Inclusion standard moved from \"generally accepted\" to \"generally recognised as good practice\""],
                ["2008", "4th edition", "Refinements to processes and terminology"],
                ["2013", "5th edition", "Stakeholder management added as the tenth knowledge area"],
                ["2017", "6th edition", "49 processes; Agile considerations added to each knowledge area"],
                ["2021", "7th edition", "Twelve principles and eight performance domains replace process groups and knowledge areas"],
                ["November 2025", "8th edition", "Six principles, seven domains, five focus areas and 40 processes; appendices on PMOs, AI and procurement"],
            ),
            "PMI also publishes companion titles. The most relevant are *Process Groups: A Practice Guide* (2022), "
            "which preserved the 49-process model after the 7th edition, and the *Agile Practice Guide*. Our guide "
            "to [what PMI is](/project-management/what-is-pmi/) lists PMI's other standards.",
        ),
        S(
            "The PMBOK Guide and the PMP exam",
            "The most common question about the PMBOK Guide is whether you need it to pass the "
            "[PMP certification](/project-management/pmp-certification/). The short answer: it is a key reference, "
            "but it is not the syllabus. PMI builds the exam from its **Examination Content Outline (ECO)**, and "
            "the current outline took effect in July 2026.",
            T(
                ["", "PMBOK Guide 8th edition", "PMP exam (from July 2026)"],
                ["What it is", "A standard and guide to good practice", "A test of how you would act in realistic situations"],
                ["Structure", "6 principles, 7 domains, 5 focus areas, 40 processes", "3 domains: People 33%, Process 41%, Business Environment 26%"],
                ["Approaches", "Predictive, adaptive and hybrid", "Predictive, Agile and hybrid scenarios across all domains"],
                ["Role in study", "Background, vocabulary and concepts", "Defines what you are tested on"],
            ),
            "The 8th edition fits the new exam well: its governance, finance and sustainability material overlaps "
            "with the much larger Business Environment domain, and its stakeholder and resources domains support "
            "People questions. But the exam rewards judgement, so reading the Guide cover to cover is far less "
            "useful than practising scenario questions.",
            H3("How to study the PMBOK Guide for the PMP"),
            OL(
                "Download the current PMP Examination Content Outline from pmi.org and read it first.",
                "Check eligibility: 35 contact hours or an active CAPM, plus three, four or five years of experience "
                "within the last 10 years depending on your education (two with a GAC-accredited degree).",
                "Book training from a PMI Authorized Training Partner if you need live hours: from 1 December 2026 "
                "only approved providers count. See our guide to [35 contact hours for the PMP](/project-management/35-contact-hours-pmp/).",
                "Read the Standard's principles and life cycle chapters and the seven domain chapters; skim the "
                "reference chapters and appendices.",
                "Map each ECO task to the domains and processes that support it, and note any gaps your course covers.",
                "Spend most of your time on full-length, timed practice exams built on the 2026 outline.",
            ),
            "If you are earlier in your career, the [CAPM certification](/project-management/capm-certification/) "
            "tests foundational knowledge and is a common first step.",
        ),
        S(
            "Worked example: applying PMBOK 8 to a project",
            "This illustrative example shows how the principles, domains and focus areas work together on one "
            "project. The organisation and figures are invented.",
            "A regional insurer is replacing its customer relationship management (CRM) system. The project has a "
            "budget of £300,000, six months to go-live and about 85 users in sales and customer service. The "
            "project manager chooses a **hybrid approach**: a predictive plan for the contract, data migration and "
            "cut-over, and two-week iterations for configuring screens and workflows with users.",
            H3("Step 1: apply the principles"),
            L(
                "**Holistic view:** the CRM touches billing and the call-centre telephony, so both teams join the "
                "design reviews.",
                "**Value:** success is defined as cutting average call handling time and giving sales a single "
                "customer view, not just \"system live by 30 June\".",
                "**Quality:** acceptance criteria for each workflow are agreed before configuration starts.",
                "**Sustainability:** the option appraisal compares hosting energy use and the supplier's support "
                "commitments alongside price.",
            ),
            H3("Step 2: work through the domains"),
            T(
                ["Domain", "Key question", "What the project manager did"],
                ["Governance", "Who decides, and how do changes get approved?", "Signed [project charter](/templates/project-charter-template/), steering group every four weeks, change threshold of £10,000 or two weeks"],
                ["Scope", "What exactly is in and out?", "Requirements workshops, scope statement, WBS for migration and cut-over, product backlog for configuration"],
                ["Schedule", "When will it be done?", "Milestone plan for the predictive work, iteration calendar for configuration"],
                ["Finance", "What will it cost and how is it funded?", "Budget with a 10% contingency reserve held by the sponsor"],
                ["Stakeholders", "Who is affected and how will we engage them?", "Stakeholder map, fortnightly demos, communications plan for go-live"],
                ["Resources", "Who and what do we need?", "Two super-users seconded from each department, supplier consultants for eight weeks"],
                ["Risk", "What could go wrong or better?", "Risk register; top threat is poor data quality, so a trial migration is scheduled in month two"],
            ),
            H3("Step 3: tailor the processes by focus area"),
            T(
                ["Focus area", "Processes used in full", "Processes kept light"],
                ["Initiating", "Initiate Project or Phase; Identify Stakeholders", "None"],
                ["Planning", "Plan Sourcing Strategy; Develop Budget; Identify Risks; Plan Risk Responses", "Plan Schedule Management (one page); Plan Communications Management (folded into the stakeholder plan)"],
                ["Executing", "Manage Project Execution; Lead the Team; Implement Risk Responses", "Manage Project Knowledge (a shared lessons log)"],
                ["Monitoring and controlling", "Assess and Implement Changes; Monitor and Control Finances; Validate Scope", "Monitor Communications (checked at steering group)"],
                ["Closing", "Close Project or Phase, including supplier contract closure and lessons learned", "None"],
            ),
            "The result covers every domain without 40 documents. Work management platforms such as [Wrike](/project-management-tools/wrike/) can hold the "
            "predictive milestones and the iteration boards in one place, with dependencies and dashboards for the "
            "steering group.",
        ),
        S(
            "How to use the PMBOK Guide step by step",
            "Whether or not you are studying for an exam, the Guide is most useful as a checklist and shared "
            "vocabulary. A practical routine:",
            OL(
                "**Choose the development approach** using the Standard's life cycle chapter: predictive, adaptive or hybrid.",
                "**Check what is mandatory** in your organisation: governance gates, PMO standards, contract or regulatory requirements.",
                "**Walk the seven domains** and write down, for each, the key decisions this project needs.",
                "**Pick the processes** from the 40 that each decision needs, and decide how formal each one should be.",
                "**Record your tailoring** in the project management plan so the sponsor and team know what to expect.",
                "**Use the principles as a test** at each phase gate: are we still delivering value, leading accountably and building quality in?",
                "**Review and adjust** the process set when risk, size or stakeholders change.",
            ),
            "Read our overview of [project management methodologies](/project-management/project-management-methodologies/) "
            "to choose the way of working that sits on top of the PMBOK Guide.",
        ),
        S(
            "PMBOK, PRINCE2 and Agile",
            "The PMBOK Guide is often compared with methods, but it does a different job. PRINCE2 is a "
            "process-based method that tells you how to direct and manage a project in stages; Scrum is an Agile "
            "framework for delivering in short iterations; the PMBOK Guide describes what a well-run project must "
            "address, whatever method you use. Many organisations use PRINCE2 or an Agile framework as the method "
            "and the PMBOK Guide as the wider body of knowledge. See our guide to "
            "[PMBOK vs PRINCE2](/project-management/pmbok-vs-prince2/) for a detailed comparison.",
        ),
        S(
            "How to get the PMBOK Guide",
            "PMI members can download a free digital copy of the PMBOK Guide and PMI's other standards as a "
            "membership benefit, and PMIstandards+ offers searchable online access. Non-members can buy print or "
            "digital copies from PMI's store and major booksellers, and translations are available in several "
            "languages. Check that you are buying the eighth edition: listings for the 6th and 7th editions are "
            "still common.",
        ),
        S(
            "Common mistakes with the PMBOK Guide",
            L(
                "**Studying from an old edition only.** The 6th edition's 49 processes and the 7th edition's "
                "domains are both out of date. Use the 8th edition with materials built on the 2026 exam outline.",
                "**Treating it as a methodology.** It tells you what to cover, not how to run your Monday stand-up. "
                "You still need to choose and tailor an approach.",
                "**Running every process.** The 40 processes are options. Using all of them on a small project "
                "wastes time and frustrates the team.",
                "**Confusing focus areas with phases.** Initiating, planning, executing, monitoring and controlling, "
                "and closing repeat within each phase or iteration.",
                "**Memorising instead of applying.** Exams and real projects both reward judgement. Practise using "
                "the domains on a real or illustrative project.",
            ),
        ),
    ],
    faq=[
        ("What does PMBOK stand for?",
         "Project Management Body of Knowledge. The full title of PMI's book is A Guide to the Project Management "
         "Body of Knowledge (PMBOK Guide)."),
        ("What is the latest edition of the PMBOK Guide?",
         "The eighth edition, published by PMI in November 2025. It replaced the seventh edition from 2021."),
        ("What are the six principles in PMBOK 8?",
         "Adopt a holistic view; focus on value; embed quality into processes and deliverables; be an accountable "
         "leader; integrate sustainability within all project areas; and build an empowered culture."),
        ("What are the seven performance domains in the PMBOK Guide 8th edition?",
         "Governance, scope, schedule, finance, stakeholders, resources and risk."),
        ("How many processes are in the PMBOK Guide 8th edition?",
         "40, presented as non-prescriptive guidance and grouped into five focus areas: initiating, planning, "
         "executing, monitoring and controlling, and closing. Planning holds 19 of them."),
        ("Are the process groups back in PMBOK 8?",
         "In effect, yes. The five process groups return as five focus areas with the same names, after the 7th "
         "edition removed process detail from the guide."),
        ("What happened to the ten knowledge areas?",
         "They were replaced by seven performance domains. Most map directly; integration became governance, "
         "communications moved into stakeholders, cost became finance, and quality and procurement are covered by "
         "governance processes, a principle and an appendix."),
        ("Is PMBOK a methodology?",
         "No. It is a standard and guide to good practice. Methodologies such as PRINCE2 or Scrum describe how to do "
         "the work; the PMBOK Guide describes what good practice covers."),
        ("Is the PMP exam based on the PMBOK Guide 8th edition?",
         "The exam is based on PMI's Examination Content Outline, updated in July 2026. The PMBOK Guide is one of "
         "several references, so study it alongside the outline and scenario-based practice questions."),
        ("Is the PMBOK Guide free?",
         "PMI members get a free digital copy as a membership benefit. Non-members usually buy it from PMI or a "
         "bookseller."),
        ("Does the PMBOK Guide cover Agile?",
         "Yes. The 8th edition covers predictive, adaptive and hybrid approaches and includes tailoring guidance for "
         "each. PMI also publishes a separate Agile Practice Guide."),
        ("What is the difference between PMBOK and PMP?",
         "PMBOK is the body of knowledge and PMI's guide to it; the PMP is a certification awarded by PMI to people who "
         "meet the experience and training requirements and pass the exam."),
        ("Is the PMBOK Guide used outside the US?",
         "Yes. It is used worldwide, particularly in the Americas, the Middle East and Asia. In the UK it is often used "
         "alongside PRINCE2 or the APM Body of Knowledge."),
    ],
)
