from core import S, L, OL, T, TIP, H3

URL = "/project-management/scrum/scrum-principles-and-values/"

RW = dict(
    title="Scrum Principles and Values: Pillars, Values and Examples",
    desc="Scrum principles and values explained: the three pillars and five values from the Scrum Guide, real examples, a team workshop and how to live them.",
    intro=(
        "Scrum principles and values are the three pillars of empiricism (transparency, inspection and adaptation) "
        "and the five Scrum values (commitment, focus, openness, respect and courage) set out in the 2020 Scrum Guide. "
        "The pillars describe how a Scrum Team learns its way through complex work; the values describe how people "
        "need to behave for that learning to work. This guide explains each one, shows what they look like in real "
        "teams and gives you a step-by-step way to build them into your own."
    ),
    takeaways=[
        "Scrum is founded on empiricism and lean thinking. Its three pillars are transparency, inspection and adaptation; each one depends on the one before it.",
        "The five Scrum values are commitment, focus, openness, respect and courage. They were added to the Scrum Guide in 2016 and remain in the 2020 version.",
        "The values are what make the pillars work: without openness and courage, information stays hidden and inspection is based on a false picture.",
        "Commitment in Scrum means commitment to goals and to each other, not a promise to finish every item in the Sprint Backlog.",
        "Lists of \"six Scrum principles\" (such as self-organisation and time-boxing) come from training bodies, not from the Scrum Guide itself.",
        "Values are built through behaviour, not posters: agree what each one looks like, write working agreements and inspect them in the Sprint Retrospective.",
    ],
    sections=[
        S("What are Scrum principles and values?",
          "**Scrum principles and values are the theory and behaviours that hold the Scrum framework together.** The "
          "principles are the three pillars of empiricism (transparency, inspection and adaptation) that let a team "
          "learn from experience. The values are commitment, focus, openness, respect and courage, the behaviours that "
          "make those pillars work in a real team.",
          "The [Scrum Guide](/project-management/scrum/what-is-scrum/), written by Ken Schwaber and Jeff Sutherland and "
          "last updated in November 2020, does not use a heading called \"principles\". It says Scrum is founded on "
          "**empiricism** (knowledge comes from experience and decisions are based on what is observed) and **lean "
          "thinking** (reduce waste and focus on the essentials). It then describes three pillars that make empiricism "
          "work and five values that people need to live. When people talk about \"Scrum principles\", they almost "
          "always mean those pillars. The table shows which elements are official and which come from elsewhere.",
          T(["Element", "What it includes", "Source", "Status"],
            ["Scrum theory", "Empiricism and lean thinking", "2020 Scrum Guide", "Official"],
            ["Three pillars", "Transparency, inspection, adaptation", "2020 Scrum Guide", "Official"],
            ["Five values", "Commitment, focus, openness, respect, courage", "Scrum Guide since 2016", "Official"],
            ["Self-managing teams", "The team decides who does what, when and how", "2020 Scrum Guide", "Official (replaced \"self-organising\" in 2020)"],
            ["Six Scrum principles", "Empirical process control, self-organisation, collaboration, value-based prioritisation, time-boxing, iterative development", "SBOK Guide (SCRUMstudy)", "Not part of the Scrum Guide, but consistent with it"],
            ["Agile values and principles", "Four values and twelve principles", "Agile Manifesto (2001)", "Wider Agile context, not Scrum-specific"],
          ),
        ),
        S("How pillars, values and the framework fit together",
          "It helps to think of Scrum in four layers, each resting on the one below:",
          OL(
            "**Values** shape behaviour: whether people speak up, focus and support each other.",
            "**Pillars** depend on that behaviour: work is only transparent if people are open.",
            "**Events and artifacts** give the pillars structure: the [Scrum events](/project-management/scrum/scrum-ceremonies/) are the points to inspect and adapt, and the [Scrum artifacts](/project-management/scrum/scrum-artifacts/) make the work visible.",
            "**Outcomes** follow: valuable Increments, problems found early and a team that improves every Sprint.",
          ),
          "The Scrum Guide says that when the values are embodied by the Scrum Team and the people they work with, the "
          "pillars come to life and build trust. Teams that copy the events but skip the values get meetings that "
          "change nothing.",
          TIP("If your Sprint Review never changes the Product Backlog and your Retrospective never changes how you "
              "work, the pillars are not working. Look at the values first."),
        ),
        S("The three pillars of Scrum",
          "The three pillars are a chain. The Scrum Guide puts it plainly: transparency enables inspection, and "
          "inspection enables adaptation. Inspection without transparency is misleading and wasteful; inspection "
          "without adaptation is pointless.",
          H3("Transparency"),
          "Transparency means the process and the work are visible to the people doing the work and the people "
          "receiving it. Important decisions are based on the state of the three artifacts, so if those artifacts are "
          "incomplete or misleading, decisions carry more risk. In practice transparency looks like a Product Backlog "
          "anyone can read, a [Sprint Backlog](/project-management/scrum/sprint-backlog/) and "
          "[Scrum board](/project-management/scrum/scrum-boards/) that show the real state of work, and a shared "
          "[Definition of Done](/project-management/agile/definition-of-done/) so \"done\" means the same thing to "
          "everyone.",
          "**Warning signs:** items marked done that still need testing, a separate \"real\" plan kept outside the "
          "backlog, or status reports that differ from what the board shows.",
          H3("Inspection"),
          "Inspection means frequently and diligently examining the Scrum artifacts and progress towards the agreed "
          "goals to spot problems early. It is not an audit by outsiders; the Scrum Team inspects its own work, often "
          "together with stakeholders. Scrum's events provide a regular rhythm for it, so inspection does not depend on "
          "someone remembering to ask.",
          "**Warning signs:** Daily Scrums that are status reports to one person, Sprint Reviews that are slide shows "
          "rather than a look at the working Increment, or retrospectives where nobody mentions the real problem.",
          H3("Adaptation"),
          "Adaptation means adjusting the process or the product as soon as possible when inspection shows something "
          "has drifted outside acceptable limits. The Scrum Guide notes that adaptation becomes harder when the people "
          "involved are not empowered or self-managing, which is why Scrum gives the team authority over how it works.",
          "**Warning signs:** the same retrospective actions every Sprint, a backlog order that never changes after "
          "stakeholder feedback, or a plan that cannot change without approval from outside the team.",
        ),
        S("Where the pillars appear in Scrum events and artifacts",
          "Every Scrum event is a formal opportunity to inspect and adapt something. The Sprint itself is the "
          "container for the other four.",
          T(["Event", "Inspect", "Adapt"],
            ["[Sprint Planning](/project-management/scrum/sprint-planning/)", "Product Backlog, Product Goal, past performance and capacity", "The Sprint Goal and Sprint Backlog"],
            ["[Daily Scrum](/project-management/scrum/daily-scrum/)", "Progress towards the Sprint Goal", "The plan for the next working day; the Sprint Backlog"],
            ["[Sprint Review](/project-management/scrum/sprint-review/)", "The Increment and the outcome of the Sprint, with stakeholders", "The Product Backlog and, if needed, the Product Goal"],
            ["[Sprint Retrospective](/project-management/scrum/sprint-retrospective/)", "How the Sprint went: people, interactions, processes, tools, Definition of Done", "Ways of working; improvements added to the next Sprint"],
          ),
          "The three artifacts provide the transparency that inspection depends on, and each has a commitment that "
          "gives it a clear focus: the [Product Backlog](/project-management/scrum/product-backlog/) has the Product "
          "Goal, the Sprint Backlog has the Sprint Goal and the Increment has the Definition of Done. Our "
          "[product backlog template](/templates/product-backlog-template/) and "
          "[Sprint planning template](/templates/sprint-planning-template/) keep both visible.",
          "See our guide to [empiricism in Scrum](/project-management/scrum/empiricism-in-scrum/) for the theory "
          "behind the pillars and four more worked examples.",
        ),
        S("The five Scrum values explained",
          "The Scrum Guide says that successful use of Scrum depends on people becoming more proficient in living five "
          "values. Here is what each one means, what it looks like and how it is commonly misread.",
          H3("Commitment"),
          "The Scrum Team commits to achieving its goals and to supporting each other. The goals are the Product Goal "
          "and the Sprint Goal, and the Definition of Done is a commitment about quality.",
          L(
            "**In practice:** the team works together towards the Sprint Goal, swarms on blocked items and keeps its working agreements.",
            "**Example:** a Developer who finishes early helps a colleague test a story that is at risk, rather than pulling new work into the Sprint.",
            "**Misreading:** treating commitment as a promise to complete every item in the Sprint Backlog regardless of what is learned. The Scrum Guide treats the selected work as a forecast and makes the Sprint Goal the commitment.",
          ),
          H3("Focus"),
          "The team's primary focus is on the work of the Sprint so that it makes the best possible progress towards "
          "its goals.",
          L(
            "**In practice:** limit work in progress, finish before starting, protect the Sprint from unplanned requests and route new ideas to the Product Owner.",
            "**Example:** a stakeholder asks a Developer directly for a quick change. The Developer thanks them and takes it to the Product Owner, who decides whether it goes into the Product Backlog.",
            "**Misreading:** focus as tunnel vision, where the team ignores stakeholder feedback or important information until the Sprint ends.",
          ),
          H3("Openness"),
          "The Scrum Team and its stakeholders are open about the work and the challenges. Openness is the value most "
          "directly behind transparency.",
          L(
            "**In practice:** raise risks and blockers as soon as they appear, show unfinished work honestly, say \"I don't know\" and stay open to other people's ideas.",
            "**Example:** at the Daily Scrum a Developer says a third-party API is returning errors and the story may not be finished, three days before the Sprint Review rather than during it.",
            "**Misreading:** openness only within the team. The Guide extends it to stakeholders, so the Sprint Review should show what is genuinely done and what is not.",
          ),
          H3("Respect"),
          "Scrum Team members respect each other to be capable, independent people, and are respected as such by the "
          "people they work with.",
          L(
            "**In practice:** trust Developers to decide how to do the work, assume good intent, listen to different views and respect the Product Owner's decisions about order and value.",
            "**Example:** a manager who wants a feature sooner talks to the Product Owner rather than reassigning tasks inside the team.",
            "**Misreading:** respect as avoiding disagreement. Respectful teams disagree openly about ideas while staying respectful of the people.",
          ),
          H3("Courage"),
          "Scrum Team members have the courage to do the right thing and to work on tough problems.",
          L(
            "**In practice:** say no to work that would break the Definition of Done, challenge unrealistic expectations, admit mistakes and raise uncomfortable topics in the Retrospective.",
            "**Example:** the Product Owner tells a senior stakeholder that the release date holds but two features will move to the next Sprint, instead of letting the team cut testing.",
            "**Misreading:** courage as heroics, such as working through the night to hide a problem. That trades the team's sustainability for short-term appearances.",
          ),
        ),
        S("How the values make the pillars work",
          "Each value supports one or more pillars. When a value is missing, you can usually see which pillar breaks "
          "first.",
          T(["Value", "Main pillar it supports", "What breaks without it"],
            ["Openness", "Transparency", "Problems stay hidden, so inspection looks at a false picture"],
            ["Courage", "Transparency and adaptation", "People see the problem but do not raise it or act on it"],
            ["Focus", "Inspection", "Work is scattered, so there is little finished to inspect"],
            ["Commitment", "Adaptation", "Changes agreed in events are not followed through"],
            ["Respect", "All three", "People stop sharing honest information because they expect blame"],
          ),
          "The common thread is **trust**: a team that trusts its leaders tells them the truth early; a team that "
          "expects blame tells them what they want to hear.",
        ),
        S("Scrum values in everyday behaviour",
          "The table turns the values into behaviour you can observe and discuss.",
          T(["Value", "Looks like", "Does not look like"],
            ["Commitment", "Working together towards the Sprint Goal", "Committing to unrealistic scope to please others"],
            ["Focus", "Finishing Sprint work before starting new tasks", "Constant context switching between projects"],
            ["Openness", "Raising a risk at the Daily Scrum", "Hiding a problem until the Sprint Review"],
            ["Respect", "Letting Developers decide how to do the work", "Assigning tasks over their heads"],
            ["Respect", "Disagreeing about ideas, not people", "Blaming individuals in the Retrospective"],
            ["Courage", "Telling stakeholders a feature is not ready", "Releasing work that does not meet the Definition of Done"],
            ["Courage", "Admitting a mistake and proposing a fix", "Covering up an error to protect your reputation"],
          ),
        ),
        S("Scrum values by accountability",
          "Everyone in and around the [Scrum Team](/project-management/scrum/scrum-team-roles/) lives the same five "
          "values, but they show up differently depending on the accountability.",
          T(["Who", "What living the values looks like"],
            ["[Product Owner](/project-management/scrum/scrum-product-owner/)", "Keeps the Product Backlog transparent and ordered; explains the reasons behind priorities (openness); says no to low-value requests (courage); respects the Developers' estimates and choices about how to build"],
            ["[Scrum Master](/project-management/agile/scrum-master-role/)", "Models the values rather than enforcing them; makes impediments visible; protects the team's focus; coaches the organisation when behaviour outside the team undermines the values"],
            ["Developers", "Commit to the Sprint Goal and the Definition of Done; raise risks early; help each other; hold each other accountable as professionals"],
            ["Managers and stakeholders", "Respect the team's self-management; bring requests through the Product Owner; respond to bad news with help, not blame; attend the Sprint Review and give honest feedback"],
          ),
          "The Scrum Master is accountable for the Scrum Team's effectiveness, so fostering the values is part of the "
          "role, but that does not mean policing them. A Scrum Master models them and removes the conditions, such as "
          "blame or overload, that make them hard to live. Our guide to "
          "[servant leadership in Scrum](/project-management/scrum/servant-leadership-in-scrum/) covers this style in more depth.",
          TIP("Managers have a big influence on openness and courage. If bad news is punished even once, teams learn "
              "to hide it. Thank people for raising problems early, especially when the news is unwelcome."),
        ),
        S("Worked example: one Sprint with and without the values",
          "The following example is **illustrative**: the team, product and dates are invented to show how the "
          "values and pillars affect a real Sprint.",
          "A seven-person team is building a booking feature for a dentists' appointment app. The Sprint is two weeks "
          "long and the Sprint Goal is: \"Patients can book and cancel an appointment online.\" On day three, a "
          "Developer finds that the practice-management system the app connects to rejects cancellations made less "
          "than 24 hours ahead.",
          H3("Version A: the values are weak"),
          L(
            "**Day 3:** the Developer assumes they can find a workaround and says nothing at the Daily Scrum (no openness).",
            "**Days 4 to 8:** two Developers start extra stories to look busy while the problem is unresolved (no focus). A manager asks one of them to fix an unrelated bug, which they do quietly (no respect for the Product Owner's ordering).",
            "**Day 9:** the workaround fails. To protect the Sprint Review, the team marks cancellation as done without the edge-case tests (no courage, no commitment to the Definition of Done).",
            "**Sprint Review:** stakeholders see a working demo and approve a release. Two weeks after go-live, patients start receiving cancellation errors.",
          ),
          H3("Version B: the values are strong"),
          L(
            "**Day 3:** the Developer raises the issue at the Daily Scrum. The team updates the board so the risk is visible (openness, transparency).",
            "**Day 3, afternoon:** the Product Owner checks with the practice manager and confirms the 24-hour rule is intentional (inspection).",
            "**Day 4:** the Product Owner and Developers renegotiate the Sprint scope: the app will block late cancellations and show the practice's phone number instead (adaptation, commitment to the goal rather than the original plan).",
            "**Days 4 to 9:** the team swarms on the remaining work; the manager is asked to raise the unrelated bug with the Product Owner (focus, respect).",
            "**Sprint Review:** the team shows exactly what is done. Stakeholders ask for clearer wording on the error message, which goes to the top of the backlog (openness, inspection, adaptation).",
          ),
          T(["Measure", "Version A", "Version B"],
            ["When the problem became visible", "After release", "Day 3 of the Sprint"],
            ["Sprint Goal met", "Apparently, but not really", "Yes, with an agreed change to scope"],
            ["Definition of Done", "Broken", "Kept"],
            ["Stakeholder trust after the Sprint", "Falls once defects appear", "Rises because there were no surprises"],
          ),
          "The events and artifacts were identical in both versions; only the behaviour differed.",
        ),
        S("How to embed Scrum values in your team, step by step",
          "Values cannot be installed, but they can be made explicit, practised and inspected like anything else in "
          "Scrum.",
          OL(
            "**Explain the why.** Link each value to the pillar it supports and to a problem the team has actually had.",
            "**Define observable behaviours.** For each value, list two or three things you would see if it were present and absent. The behaviour table above is a starting point.",
            "**Turn them into working agreements.** Pick five to eight specific agreements, such as \"we raise blockers at the Daily Scrum, even if we think we can solve them\" or \"nobody marks an item done until it meets the Definition of Done\".",
            "**Make them visible.** Put the working agreements next to the Scrum board or in the team's shared space. Visibility is transparency applied to the team's own process.",
            "**Agree how outsiders interact with the team.** Share with managers and stakeholders how to bring requests (through the Product Owner) and how to respond to bad news. Many value problems start outside the team.",
            "**Model them from the top.** The Product Owner, Scrum Master and managers go first: admit their own mistakes, share uncomfortable information and respect the team's decisions.",
            "**Inspect them in the Retrospective.** Every few Sprints, use a values exercise (see the self-assessment below) and pick one improvement. Our [Sprint Retrospective template](/templates/sprint-retrospective-template/) has space for this, and our list of [retrospective games](/project-management/scrum/sprint-retrospective-games/) offers more formats.",
            "**Recognise the behaviour.** When someone raises a risk early or pushes back on a broken Definition of Done, say so publicly. What gets recognised gets repeated.",
            "**Adapt the agreements.** Remove agreements that the team now follows naturally and add new ones as the context changes, such as new team members or a new stakeholder group.",
          ),
        ),
        S("A 90-minute Scrum values workshop",
          "If you want a ready-made session for steps 1 to 4, this agenda works for teams of up to about ten people, "
          "in person or remote.",
          T(["Time", "Activity", "Output"],
            ["0 to 10 min", "Check-in: each person names a time a team they were in worked really well, and why", "Shared language about good teamwork"],
            ["10 to 20 min", "Short explanation of the pillars and five values and how they connect", "Common understanding"],
            ["20 to 45 min", "Small groups take one or two values each and list \"looks like\" and \"does not look like\" behaviours from their own work", "Behaviour lists for all five values"],
            ["45 to 60 min", "Each group presents; the whole team adds or challenges", "Agreed behaviours"],
            ["60 to 75 min", "Dot-vote the behaviours most worth working on and turn the top five to eight into working agreements", "Draft working agreements"],
            ["75 to 85 min", "Agree how the agreements will be displayed, shared with stakeholders and reviewed", "Visibility and review plan"],
            ["85 to 90 min", "Close: one word each on how they feel about the agreements", "Quick read of buy-in"],
          ),
          "Keep the output to one page the team will actually use.",
        ),
        S("Scrum values self-assessment",
          "Use these questions in a Retrospective. Ask each person to score each value from 1 (rarely true) to 5 "
          "(almost always true), anonymously if trust is still low, then discuss the lowest score and the biggest "
          "spread of opinion.",
          T(["Value", "Question", "Healthy signal"],
            ["Commitment", "Do we pursue the Sprint Goal together, even when it means helping outside our speciality?", "Items are swarmed; few items sit half-finished at Sprint end"],
            ["Focus", "Do we finish what we start before taking on more?", "Low work in progress; unplanned requests go through the Product Owner"],
            ["Openness", "Would anyone here raise a problem on the day they found it?", "Blockers appear on the board within a day"],
            ["Respect", "Do we trust each other's judgement and challenge ideas, not people?", "Disagreement happens in the open and is resolved"],
            ["Courage", "Have we said no to anything this Sprint that would have hurt quality or the goal?", "The Definition of Done holds under pressure"],
          ),
          "Track the trend over several Sprints, and never use the scores to compare teams or individuals; that would "
          "undermine the openness you are trying to build.",
        ),
        S("Other principles often taught with Scrum",
          "Because the Scrum Guide is short, training bodies and authors have published their own lists of Scrum "
          "principles. The best known is the six principles in the SBOK Guide from SCRUMstudy. They are consistent "
          "with the Scrum Guide but are not part of its official text, so exam questions on the Scrum Guide will not "
          "use them.",
          T(["Principle (SBOK)", "Closest Scrum Guide equivalent"],
            ["Empirical process control", "Empiricism and the three pillars"],
            ["Self-organisation", "Self-managing Scrum Teams"],
            ["Collaboration", "Cross-functional teams working together and with stakeholders"],
            ["Value-based prioritisation", "The Product Owner ordering the Product Backlog to maximise value"],
            ["Time-boxing", "Fixed-length Sprints and maximum durations for each event"],
            ["Iterative development", "Delivering a usable Increment every Sprint"],
          ),
          H3("Self-managing versus self-organising"),
          "Earlier versions of the Scrum Guide described Development Teams as self-organising. The 2020 Guide uses "
          "**self-managing**, meaning the Scrum Team decides internally who does what, when and how.",
          H3("Lean thinking"),
          "The 2020 Guide added lean thinking alongside empiricism: reducing waste and focusing on the essentials. In "
          "practice that means small batches, finishing work and removing anything that does not add value. Our "
          "comparison of [Scrum vs Lean](/project-management/scrum/scrum-vs-lean/) explains how the two ideas fit.",
          H3("Scrum values compared with other Agile values"),
          "The [Agile Manifesto](/project-management/agile/agile-manifesto-values-and-principles/) has four values and "
          "twelve principles that apply to all Agile approaches. Extreme Programming (XP) has its own values: "
          "communication, simplicity, feedback, courage and respect, so courage and respect appear in both. The Scrum "
          "values are the Scrum-specific expression of the broader [Agile mindset](/project-management/agile/agile-mindset/).",
        ),
        S("Common mistakes with Scrum principles and values",
          L(
            "**Values as wall posters.** Printing the five values without agreeing what they mean in behaviour changes nothing. Define observable behaviours.",
            "**Reading commitment as a scope promise.** Treating the Sprint Backlog as a contract leads to overtime, cut corners and hidden problems. Commit to the Sprint Goal and the Definition of Done.",
            "**Using velocity as a target.** Pressuring teams to raise [velocity](/project-management/scrum/scrum-velocity/) encourages inflated estimates and destroys transparency.",
            "**Openness inside the team only.** If the Sprint Review hides unfinished work from stakeholders, transparency fails at the point where it matters most.",
            "**Confusing respect with politeness.** Avoiding difficult conversations to keep the peace lets problems grow. Respect allows honest disagreement.",
            "**Blaming people for bad news.** One reaction like this teaches the team to stay quiet. Respond to problems with questions and help.",
            "**Leaving managers out.** Many value problems, such as interrupting the team or reassigning work, come from outside the Scrum Team. Include managers and stakeholders in the conversation.",
            "**Mixing up official and unofficial principles.** For a Scrum Guide-based exam, learn the pillars and values from the Guide, not from SBOK-style lists. Our guide to [Scrum certification and training](/project-management/scrum/scrum-certification-and-training/) compares the main options.",
          ),
          "Read our [guide to the Scrum team roles](/project-management/scrum/scrum-team-roles/) to see how each accountability supports the values.",
        ),
    ],
    faq=[
        ("What are the 5 Scrum values?",
         "Commitment, focus, openness, respect and courage. The Scrum Team commits to its goals and to supporting each "
         "other, focuses on the work of the Sprint, is open about the work and its challenges, respects each other as "
         "capable people and has the courage to do the right thing and work on tough problems."),
        ("What are the three pillars of Scrum?",
         "Transparency, inspection and adaptation. Together they make empiricism work: the work is made visible, it is "
         "inspected frequently, and the product or process is adjusted as soon as something drifts off course."),
        ("What are the principles of Scrum?",
         "The Scrum Guide says Scrum is founded on empiricism and lean thinking, supported by the three pillars of "
         "transparency, inspection and adaptation. Some training bodies, such as SCRUMstudy's SBOK Guide, add a list of "
         "six principles, but those are not part of the official Scrum Guide."),
        ("Why are the Scrum values important?",
         "Because empiricism only works with honest information. Without openness, courage and respect, people hide "
         "problems, inspection is based on a false picture and adaptation comes too late. The values build the trust "
         "that makes the pillars work."),
        ("When were the Scrum values added to the Scrum Guide?",
         "The five values were added in an update announced in July 2016 and remain in the current 2020 Scrum Guide. "
         "They were discussed in Scrum writing well before that."),
        ("Who is responsible for the Scrum values?",
         "Everyone on the Scrum Team lives the values, and the Guide extends them to the people the team works with. "
         "The Scrum Master helps the team and organisation understand and apply them, mainly by modelling them and "
         "removing obstacles, not by enforcing them."),
        ("Which Scrum value is the most important?",
         "The Scrum Guide does not rank them. In practice, openness and courage often need the most attention because "
         "they decide whether problems surface early."),
        ("Is self-organisation a Scrum principle?",
         "Not in the current Scrum Guide's wording. The 2020 Guide describes Scrum Teams as self-managing, meaning they "
         "decide who does what, when and how. Self-organisation appears as a principle in some training frameworks and "
         "in earlier versions of the Guide."),
        ("What does commitment mean in Scrum?",
         "Commitment to achieving the team's goals and to supporting each other. It does not mean promising to finish "
         "every Sprint Backlog item; those items are a forecast. Each artifact also has a commitment: the Product Goal, "
         "the Sprint Goal and the Definition of Done."),
        ("How do Scrum values relate to the Agile Manifesto?",
         "Both put people, collaboration and responding to change at the centre. The Manifesto applies to all Agile "
         "approaches; the Scrum values describe the behaviours that make Scrum work."),
        ("How can a team practise the Scrum values?",
         "Agree what each value looks like in behaviour, turn the most important behaviours into working agreements, "
         "make them visible and inspect them in the Sprint Retrospective."),
        ("What happens if a team ignores the Scrum values?",
         "Events and artifacts become rituals. Information gets hidden, trust drops and problems are discovered late. "
         "Teams often keep the meetings but lose the benefits."),
    ],
)
