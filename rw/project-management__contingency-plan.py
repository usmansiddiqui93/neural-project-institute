from core import S, L, OL, T, TIP, H3

URL = "/project-management/contingency-plan/"

RW = dict(
    title="Contingency Plan in Project Management: Steps and Examples",
    desc="Contingency plan in project management explained: triggers, a free template, a 9-step method, worked examples and how to size the contingency reserve.",
    intro=(
        "A contingency plan in project management is a pre-agreed set of actions the team will take if a specific "
        "risk occurs, activated by a clear trigger and funded in advance. Because the decisions are made calmly "
        "beforehand, people can act within minutes instead of improvising under pressure. This guide shows you how "
        "to write one step by step, with a template, two fully worked examples and a method for sizing the "
        "contingency reserve."
    ),
    takeaways=[
        "A contingency plan is a response prepared in advance for one identified risk, used only if that risk occurs.",
        "Every plan needs a measurable trigger, a named decision maker, ordered actions with owners, a reserve, a fallback and a stand-down rule.",
        "Mitigation acts before a risk occurs; a contingency plan acts when it occurs; a fallback plan acts if the contingency plan fails.",
        "Write plans for high-impact or time-critical risks, not for every line in the risk register.",
        "Contingency reserve sits inside the cost baseline for identified risks; management reserve sits outside it for unknown ones.",
        "Rehearse critical plans and record how each activated plan performed in lessons learned.",
    ],
    sections=[
        S(
            "What is a contingency plan in project management?",
            "A **contingency plan** is a documented set of actions that a project will carry out only if a specific, "
            "identified risk occurs. It names the trigger that activates it, who decides, what each person does, the "
            "time and money set aside, and what happens if the plan itself fails. It is prepared and approved before "
            "it is needed.",
            "Five features separate a real contingency plan from a vague intention to \"deal with it if it happens\":",
            L(
                "**It is tied to one risk.** Each plan responds to a named entry in the "
                "[risk register](/project-management/risk-register/), not to bad luck in general.",
                "**It has a trigger.** An observable condition, such as a date, a measurement or an event, tells you "
                "the plan is now live.",
                "**It is pre-approved.** The sponsor or governance body agrees the actions and spending in advance, "
                "so nobody waits for sign-off on the day.",
                "**It is owned.** One person monitors the trigger and one person (often the same) leads the response.",
                "**It is funded.** The time and money it needs are covered by the contingency reserve.",
            ),
            "In PMI terminology, these are **contingent response strategies**: responses designed for use only if "
            "certain events occur (the term used in the PMBOK Guide 6th edition). They deal with known-unknowns, "
            "risks you have identified but cannot be sure will happen. Contingency plans are one part of wider "
            "[project risk management](/project-management/project-risk-management/), which also covers identifying, "
            "analysing and reducing risks before they occur.",
        ),
        S(
            "Contingency plan vs mitigation, fallback plan and workaround",
            "These terms are often mixed up, including in exam questions. The difference is timing: when the "
            "response is used and whether it was planned.",
            T(
                ["Response", "When it is used", "Planned in advance?", "Example"],
                ["Mitigation", "Before the risk occurs, to reduce its probability or impact", "Yes", "Run a load test eight weeks before go-live"],
                ["Contingency plan", "When a trigger shows the risk is occurring", "Yes", "If response times exceed 3 seconds under load, add two application servers"],
                ["Fallback plan", "When the contingency plan does not work", "Yes", "Roll back to the old system and process orders manually"],
                ["Workaround", "When an unplanned problem occurs, or a risk with no plan", "No", "Staff re-key orders by hand while the fault is investigated"],
                ["Business continuity plan", "When the organisation's operations are disrupted", "Yes, at organisation level", "Move the call centre to a second site after a building fire"],
            ),
            H3("Contingency plan vs mitigation"),
            "Mitigation is proactive: you spend effort now to make a risk less likely or less damaging. A contingency "
            "plan is reactive but prepared: you spend nothing (or very little) unless the trigger fires. Many risks "
            "need both. You might mitigate a supplier risk by approving a second supplier, and still hold a "
            "contingency plan for switching volume to that supplier if the first one misses a delivery.",
            H3("Contingency plan vs fallback plan"),
            "A fallback plan exists because contingency plans can fail too: the marquee company is fully booked, or "
            "the rollback script errors. Write one where failure of the contingency would be serious.",
            H3("Contingency plan vs workaround"),
            "A workaround is improvised for a problem nobody planned for. If you keep needing the same one, the "
            "underlying risk belongs in the register with a proper plan. Once a risk has occurred, track it in the "
            "[issue log](/project-management/issue-log/).",
            H3("Contingency plan vs business continuity plan"),
            "A business continuity plan keeps the whole organisation running through a disruption such as a fire, "
            "cyber attack or loss of a key site; ISO 22301 is the international standard for business continuity "
            "management systems. A project contingency plan is narrower: it protects one project's objectives against "
            "one identified risk.",
        ),
        S(
            "When does a risk need a contingency plan?",
            "Not every risk deserves a plan; plans for low risks bury the important ones. Use these rules:",
            T(
                ["Situation", "Contingency plan?", "Reason"],
                ["High score (for example 15+ on a 5x5 matrix) after mitigation", "Yes", "Residual exposure is still serious"],
                ["Accepted risk with a severe impact", "Yes", "Acceptance without a plan is hope, not a response"],
                ["Low probability but catastrophic impact (safety, legal, go-live failure)", "Yes", "Scores understate these risks"],
                ["Time-critical risk where hours matter (events, cutovers, launches)", "Yes", "No time to decide on the day"],
                ["Medium risk with good mitigation in place", "Optional: a short note is enough", "Proportionate effort"],
                ["Low risk", "No", "Monitor at review; write a workaround if it occurs"],
            ),
            "The score bands above are an example; use the thresholds from your own risk management plan. Look at the "
            "[residual risk](/project-management/residual-risk/), not the inherent risk: a contingency plan covers what "
            "is left after mitigation. If you are unsure how to score risks consistently, see our guide to "
            "[project risk](/project-management/project-risk/).",
        ),
        S(
            "What a contingency plan contains",
            "A good contingency plan fits on one page. People use it under pressure, so it must be quick to read and "
            "unambiguous. Use these fields as your template:",
            T(
                ["Field", "What to write"],
                ["Risk ID and title", "Link to the risk register entry"],
                ["Plan owner", "Who monitors the trigger and keeps the plan current"],
                ["Decision maker", "Who confirms activation, plus a named deputy"],
                ["Warning sign", "An early signal that puts the team on alert"],
                ["Activation trigger", "The measurable condition that activates the plan, with a decision deadline"],
                ["Actions", "Numbered steps, each with an owner and a deadline"],
                ["Resources and reserve", "People, budget and time pre-approved, with the spending limit"],
                ["Communication", "Who is told, in what order, through which channel"],
                ["Fallback plan", "What to do if the contingency fails"],
                ["Stand-down rule", "How and when the plan is closed"],
            ),
            "Keep the plan with the risk it supports. A small project can hold contingency plans as extra columns in "
            "the free [risk register template](/templates/risk-register-template/), or in a "
            "[RAID log template](/templates/raid-log-template/) that also tracks assumptions, issues and dependencies. "
            "Larger projects usually keep a short plan document per major risk and link to it from the register.",
        ),
        S(
            "How to write a contingency plan in 9 steps",
            OL(
                "**Select the risks.** Filter your register for the risks that meet the criteria above. On most "
                "projects that is a handful, not dozens.",
                "**Describe the scenario.** For each risk, write what it looks like when it happens: what fails, "
                "when, and what the first effects are.",
                "**Set the trigger and decision deadline.** Choose an observable threshold and the latest time a "
                "decision can be made while the response will still work. Add an earlier warning sign if one exists.",
                "**List the actions in order.** Write each action as a verb with an owner and a deadline: who does "
                "what, by when. Put the actions that buy time first.",
                "**Estimate cost and time.** Price each action, including any cancellation fees, overtime or "
                "expedited delivery. Estimate the schedule effect and check it against "
                "[float](/project-management/float-and-slack/) on the affected path.",
                "**Agree the reserve and authority.** Agree with the sponsor how much contingency reserve the plan "
                "may draw on and who can authorise it. Record the limit in the plan.",
                "**Plan communication.** List who must be told when the plan activates, in what order and by which "
                "channel, using your [communication plan](/project-management/communication-plan/).",
                "**Write the fallback and stand-down rules.** Decide what happens if the response fails and how you "
                "will know the plan is finished.",
                "**Approve, store and rehearse.** Get formal approval, store the plan where the team can reach it at "
                "any hour (including offline if needed) and rehearse the critical ones.",
            ),
            TIP("Write the actions so that someone who has never seen the plan could carry them out. The person who "
                "wrote it may be on leave on the day it is needed."),
            "Assign responsibilities with a [RACI matrix](/project-management/raci-matrix/) if several teams are "
            "involved, so there is no doubt about who decides and who acts.",
        ),
        S(
            "How to write good triggers",
            "The trigger is the most important line in the plan, and the one most often written badly. A weak trigger "
            "leads to late activation, arguments about whether the plan applies, or false alarms.",
            T(
                ["Weak trigger", "Strong trigger", "Why it is better"],
                ["If the supplier is late", "If the supplier misses the 12 March sample date by more than 2 working days", "Specific date and tolerance"],
                ["If performance is poor", "If p95 page response time exceeds 3 seconds for 15 minutes under test load", "Measurable, with a duration to avoid noise"],
                ["If a key person leaves", "If the lead engineer gives notice or is absent for more than 5 consecutive working days", "Observable event and threshold"],
                ["If it rains", "If the forecast at 08:00 two days before shows more than a 60% chance of rain", "Named source, time and threshold"],
                ["If the budget is under pressure", "If the cost performance index falls below 0.90 for two consecutive months", "Uses an existing metric"],
            ),
            H3("Warning signs and activation triggers"),
            "Many risks give you notice. Use two levels: a **warning sign** that puts the plan owner on alert and "
            "starts low-cost preparation (checking supplier availability, briefing the team), and an **activation "
            "trigger** that starts the full plan. This avoids both late reactions and expensive false starts.",
            H3("Decision deadlines"),
            "Some responses only work if they start early enough. A replacement marquee needs 48 hours; a rollback "
            "must start before the old system's data becomes out of date. Work backwards from the response lead time "
            "to set a decision deadline, and write it into the trigger: \"if X by 08:00 on Thursday\".",
        ),
        S(
            "Worked example 1: outdoor product launch",
            "This illustrative example shows a complete plan for a risk on an outdoor launch event for 300 guests. "
            "The risk register rates heavy rain as probability 3 (possible) and impact 5 (severe) on a 5x5 matrix, a "
            "score of 15. Mitigation has already been done: a marquee supplier has been pre-booked on a provisional "
            "basis, with a £2,000 cancellation fee if the marquee is not used.",
            T(
                ["Field", "Content"],
                ["Risk", "R-07: Because the launch is outdoors, heavy rain could force cancellation or a poor guest experience, damaging press coverage."],
                ["Owner / decision maker", "Events lead owns the plan; project manager decides (deputy: marketing director)."],
                ["Warning sign", "Five days before: Met Office forecast shows more than a 40% chance of rain. Events lead confirms marquee and crew availability."],
                ["Activation trigger", "08:00 two days before: forecast shows more than a 60% chance of rain. Decision by 10:00 the same day."],
                ["Actions", "1. Events lead confirms marquee with supplier by 10:30. 2. Venue manager approves revised layout by 12:00. 3. Communications lead updates the invitation page and emails guests by 15:00. 4. Catering lead confirms covered serving area by 16:00. 5. Health and safety lead checks marquee sign-off on arrival."],
                ["Reserve", "£6,500 marquee hire plus £800 extra crew, from contingency reserve. Authority: project manager up to £8,000."],
                ["Communication", "Guests (email), press contacts (phone), venue and suppliers (phone, then written confirmation)."],
                ["Fallback", "If the marquee is unavailable or fails its safety check: move to the indoor conference room with a reduced guest list of 150, prioritising press and key customers."],
                ["Stand-down", "Plan closes after the event. Record actual cost, guest feedback and decision timing in lessons learned."],
            ),
            H3("How the plan runs"),
            OL(
                "**Monday (five days out):** the forecast shows a 45% chance of rain. Warning sign reached. The events "
                "lead confirms the marquee and crew are still available. No spend yet.",
                "**Wednesday 08:00 (two days out):** forecast at 70%. Trigger reached. The events lead calls the "
                "project manager, who confirms activation at 08:40.",
                "**Wednesday 08:45 to 16:00:** actions 1 to 4 completed in order. The project manager logs the "
                "activation in the issue log and records a reserve drawdown of £7,300.",
                "**Friday:** the event goes ahead in the marquee. The plan is stood down that evening.",
            ),
            "The plan costs £2,000 if it is not needed (the cancellation fee, a mitigation cost) and £7,300 if it "
            "is, far less than cancelling the event. For more on planning events, see our guide to "
            "[event project management](/project-management/industries/event-project-management/).",
        ),
        S(
            "Worked example 2: system go-live with a rollback plan",
            "Technology cutovers are classic contingency planning territory: the risk is clear, the window is short "
            "and a wrong call is expensive. In this illustrative example, a distribution company is replacing its "
            "order management system over a weekend. The old system is switched off at 18:00 on Friday, data is "
            "migrated overnight and the new system must be ready for the warehouse at 06:00 on Monday.",
            T(
                ["Field", "Content"],
                ["Risk", "R-12: Because data migration is complex, migrated order and stock data may be incomplete or wrong, stopping warehouse operations on Monday."],
                ["Go/no-go checkpoint", "Sunday 12:00: cutover lead presents results to the steering group."],
                ["Activation trigger", "At the checkpoint, any of: stock balance reconciliation variance above 0.5%; fewer than 95% of critical test scripts passed; any open severity 1 defect."],
                ["Decision maker", "Sponsor (operations director), advised by the cutover lead and IT service owner."],
                ["Actions if triggered", "1. Freeze the new system (IT lead, 12:15). 2. Run the tested rollback script to restore the old system from the Friday 18:00 snapshot (database lead, by 16:00). 3. Run smoke tests on the old system (test lead, by 18:00). 4. Notify warehouse, customer service and key customers (communications lead, by 19:00). 5. Rebook the cutover for a later weekend through change control (project manager)."],
                ["Reserve", "Rollback team on standby all weekend (£4,200 overtime, pre-approved). Schedule: a second cutover weekend four weeks later is already held in the plan."],
                ["Fallback", "If the rollback fails: restore from the Friday 20:00 full backup and run manual order processing on Monday using printed pick lists, which have been rehearsed with the warehouse team."],
                ["Stand-down", "If go-live succeeds, the plan closes after five days of stable operation. If triggered, it closes once the old system is confirmed live."],
            ),
            "The plan works because the go/no-go criteria were agreed weeks earlier, the 12:00 decision deadline "
            "leaves time for the rollback to finish before Monday, and the rollback was rehearsed, so the team knows "
            "how long it takes.",
            "Treat the rescheduled cutover as a formal change: raise it through "
            "[change control](/project-management/change-control/) using a "
            "[change request template](/templates/change-request-template/) so the baseline, budget and stakeholders "
            "are updated together. Our guide to [IT project management](/project-management/industries/it-project-management/) "
            "covers cutover planning in more depth.",
        ),
        S(
            "More contingency plan examples",
            "Short, illustrative plans for common risks. Add owners, deadlines and costs from your own project.",
            T(
                ["Project", "Risk", "Trigger", "Contingency actions", "Fallback"],
                ["Construction", "Steel delivery delay", "Supplier misses the fabrication milestone by 5 working days", "Resequence the groundworks; book a crane for later dates; approve overtime for erection", "Source standard sections from a stockist and accept design substitution"],
                ["Software", "Third-party API not ready", "Provider misses the sandbox release date", "Release behind a feature toggle with a mock service; ship other features first", "Descope the integration to the next release"],
                ["Any project", "Loss of a key specialist", "Notice given or absence beyond 5 working days", "Bring in the named backup; activate the contractor framework call-off", "Reschedule dependent work and use float"],
            ),
        ),
        S(
            "Contingency reserve: funding your plans",
            "A contingency plan without money or time behind it is a wish. The **contingency reserve** is the budget "
            "and schedule allowance for identified risks, held inside the cost and schedule baselines. It differs from "
            "**management reserve**, which covers unknown risks and sits outside the baseline.",
            T(
                ["", "Contingency reserve", "Management reserve"],
                ["Covers", "Identified risks (known-unknowns)", "Unidentified risks (unknown-unknowns)"],
                ["Part of the cost baseline?", "Yes", "No; it is part of the overall project budget"],
                ["Who controls it", "Usually the project manager, within agreed limits", "Usually the sponsor or governance body"],
                ["How it is sized", "From risk analysis: expected monetary value or simulation", "Often a percentage set by organisational policy"],
                ["How it is used", "Drawn down when a contingency plan activates", "Released through change control, which changes the baseline"],
            ),
            "See our guide to the [project budget](/project-management/project-budget/) for how both reserves fit "
            "into the overall budget and the [project baseline](/project-management/project-baseline/).",
            H3("Worked example: sizing the reserve with expected monetary value"),
            "Expected monetary value (EMV) is probability multiplied by impact. For an illustrative product launch "
            "programme with four risks that each have a contingency plan:",
            T(
                ["Risk", "Probability", "Cost if the plan is used", "EMV"],
                ["Rain on launch day", "25%", "£7,300", "£1,825"],
                ["Rollback at system cutover", "15%", "£18,000", "£2,700"],
                ["Late delivery of display stands", "30%", "£12,000", "£3,600"],
                ["Loss of key specialist", "20%", "£9,500", "£1,900"],
                ["**Total**", "", "£46,800", "**£10,025**"],
            ),
            "An EMV-based contingency reserve of around £10,000 works as a **pool**: you would not expect all four "
            "risks to occur, so the pool covers the likely total. Two cautions apply:",
            L(
                "If a single large risk occurs, its plan may cost more than the whole pool (the rollback alone is "
                "£18,000). For high-impact risks, check that the sponsor will fund the full plan cost, from management "
                "reserve if necessary, and record that agreement in the plan.",
                "EMV is a simple average. For larger projects, a [Monte Carlo simulation](/project-management/monte-carlo-simulation/) "
                "gives a range of outcomes and lets you set the reserve at a chosen confidence level, such as P80.",
            ),
            H3("Schedule contingency"),
            "Time works the same way. Hold schedule contingency as a visible buffer before key milestones rather than "
            "padding every task, and check how much [float](/project-management/float-and-slack/) the affected path "
            "already has. If a plan's actions would push the critical path, note which "
            "[schedule compression](/project-management/schedule-compression/) options you would use to recover.",
            "Log every drawdown against the risk it served, release the share for risks that close without "
            "occurring, and report the remaining reserve alongside the top risks.",
        ),
        S(
            "Activating and standing down a contingency plan",
            "When a trigger fires, follow a short, repeatable routine:",
            OL(
                "**Confirm the trigger.** The plan owner checks the data and contacts the decision maker. If the "
                "decision maker is unavailable, the named deputy decides.",
                "**Decide and record** the decision, time and reason, including any decision not to activate.",
                "**Execute the actions** in order; each owner confirms completion.",
                "**Log it.** Move the risk to the issue log as an occurred risk, record the reserve drawdown and note "
                "any new risks the response creates (secondary risks).",
                "**Communicate** to the people listed in the plan, then update the "
                "[project status report](/project-management/project-status-report/).",
                "**Watch for failure.** Agree in advance what would show the contingency is not working, and switch "
                "to the fallback plan if it happens.",
                "**Stand down.** Close the plan when the stand-down condition is met, confirm the final cost and "
                "schedule effect, and update the baseline through change control if needed.",
                "**Learn.** Record what worked and what did not in [lessons learned](/project-management/lessons-learned/): "
                "was the trigger early enough, were the actions in the right order, was the reserve right?",
            ),
        ),
        S(
            "Testing and reviewing contingency plans",
            "An untested plan is an assumption. Match the testing effort to the stakes: desk-check every plan at "
            "each risk review (contacts, costs, lead times), hold a tabletop walkthrough for plans that involve "
            "several teams, and physically rehearse technical responses such as rollbacks, data restores and "
            "failovers, ideally in a full dress rehearsal before a go-live.",
            "Review each plan whenever its risk is reviewed or something changes, such as a new supplier, a moved "
            "date or a new person in a key role, and check the contact details every time.",
        ),
        S(
            "Contingency planning in agile projects",
            "Agile teams handle many risks by working in short cycles and delivering the riskiest work early, but "
            "contingency plans still matter for risks that short cycles cannot absorb, such as release dates, "
            "regulatory deadlines, vendor dependencies and production incidents.",
            L(
                "**Release planning:** agree in [agile release planning](/project-management/agile/agile-release-planning/) "
                "which features would be dropped first if a date is at risk. That ranked list is your contingency plan "
                "for schedule risk.",
                "**Feature toggles:** release unfinished or risky features switched off, so the contingency is simply "
                "to keep them off.",
                "**Retrospectives:** discuss risks that nearly occurred and decide whether they need a plan.",
            ),
        ),
        S(
            "Tools for managing contingency plans",
            "Most teams start with a spreadsheet: a risk register with extra columns for the trigger, plan owner, "
            "actions summary and fallback, plus a link to the full plan. That works well for small projects.",
            "As projects grow, a work management tool puts risk items next to the schedule they affect. [Wrike](/project-management-tools/wrike/), our top-rated tool, "
            "suits date-driven projects well: its Gantt charts (from the Team plan) show dependencies, the critical "
            "path, float and baselines, so you can see what a triggered plan would do to the schedule. "
            "[monday.com](/project-management-tools/monday/) makes it easy to build a risk board with custom columns "
            "and dashboards, and [Smartsheet](/project-management-tools/smartsheet/) suits teams that like a "
            "spreadsheet-style register linked to a Gantt chart.",
            "Whichever tool you use, keep critical plans available offline as well. If the contingency is \"the "
            "system is down\", the plan should not live only in that system.",
        ),
        S(
            "Common contingency planning mistakes",
            L(
                "**Vague triggers.** \"If the supplier is late\" invites debate. Use a date, a number or an event.",
                "**No decision maker.** Plans stall while people look for authority. Name a deputy too.",
                "**No money behind the plan.** If the reserve has not been agreed, the first hour is spent asking for "
                "budget.",
                "**Confusing mitigation with contingency.** \"Monitor the supplier\" is neither; it is part of "
                "managing the risk. A contingency plan is what you do when monitoring shows trouble.",
                "**No fallback for critical risks.** Contingency plans fail too, especially under pressure.",
                "**Never testing.** The rollback that has never been run is the one that fails.",
                "**Not learning.** Each activation is evidence about your risk estimates. Feed it back.",
            ),
            "Read our guide to the [risk register](/project-management/risk-register/) to see how contingency plans "
            "fit alongside probability, impact, owners and review dates.",
        ),
    ],
    faq=[
        ("What is a contingency plan in project management?",
         "A documented set of actions, prepared and approved in advance, that the project carries out only if a "
         "specific identified risk occurs, activated by a trigger and funded from the contingency reserve."),
        ("What is an example of a contingency plan?",
         "For an outdoor event: if the forecast two days before shows more than a 60% chance of rain, confirm a "
         "pre-booked marquee, update the layout and email guests, funded from a pre-approved reserve, with an indoor "
         "venue as the fallback."),
        ("What is the difference between a contingency plan and a fallback plan?",
         "The contingency plan is used when a risk occurs. The fallback plan is used if the contingency plan itself "
         "does not work."),
        ("What is the difference between mitigation and a contingency plan?",
         "Mitigation acts before a risk occurs to reduce its probability or impact. A contingency plan is prepared in "
         "advance but only carried out if the risk occurs."),
        ("What is the difference between a workaround and a contingency plan?",
         "A contingency plan is prepared in advance for an identified risk. A workaround is an unplanned response to a "
         "problem that was not anticipated or had no plan."),
        ("What is a trigger in a contingency plan?",
         "A specific, observable condition, such as a missed date, a measurement crossing a threshold or an event, "
         "that signals the plan should be activated. Good triggers include a decision deadline."),
        ("Does every risk need a contingency plan?",
         "No. Write plans for high-scoring residual risks, accepted risks with severe impacts, low-probability "
         "catastrophic risks and time-critical risks. Monitor the rest."),
        ("Who approves a contingency plan?",
         "Usually the sponsor or governance body approves plans for major risks, together with the reserve the "
         "project manager may use, so the plan can be activated without further sign-off."),
        ("How much contingency reserve should a project have?",
         "There is no universal percentage. Base it on your analysed risks, for example the total expected monetary "
         "value of risks with contingency plans, or a Monte Carlo simulation at a chosen confidence level."),
        ("What is the difference between contingency reserve and management reserve?",
         "Contingency reserve covers identified risks and is part of the cost baseline. Management reserve covers "
         "unidentified risks, sits outside the baseline and is usually controlled by the sponsor."),
        ("Is a contingency plan the same as a business continuity plan?",
         "No. A business continuity plan keeps the whole organisation operating through a disruption. A project "
         "contingency plan protects one project's objectives against one identified risk."),
        ("Should contingency plans be tested?",
         "Yes, in proportion to the stakes: desk-check every plan, walk through multi-team plans and rehearse "
         "technical responses such as rollbacks before go-live."),
    ],
)
