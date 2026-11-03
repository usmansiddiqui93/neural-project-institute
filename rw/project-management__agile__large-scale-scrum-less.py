from core import S, L, OL, T, TIP, H3

URL = "/project-management/agile/large-scale-scrum-less/"

RW = dict(
    title="Large-Scale Scrum (LeSS): Rules, Roles and Examples",
    desc="Large-Scale Scrum (LeSS) explained: rules, 10 principles, roles, events, LeSS Huge, a worked example, adoption steps and LeSS vs SAFe and Nexus.",
    intro=(
        "Large-Scale Scrum (LeSS) is a framework for applying Scrum to many teams that work together on one "
        "product, with one Product Owner, one Product Backlog and one shared Sprint. Created by Craig Larman and "
        "Bas Vodde, it adds as little extra structure as possible and asks the organisation to change instead. "
        "This guide explains the rules, the ten principles, the roles and events, LeSS Huge, a worked Sprint "
        "example and how to adopt it."
    ),
    takeaways=[
        "LeSS is Scrum applied to many teams on one product: one Product Owner, one Product Backlog, one Definition of Done and one Sprint ending in one integrated increment.",
        "Basic LeSS is for two to eight teams; LeSS Huge, for more than eight, adds requirement areas of four to eight teams, each with an Area Product Owner.",
        "Teams are long-lived, cross-functional feature teams that deliver whole customer features, not component teams that own one layer.",
        "LeSS adds only a few events to Scrum: a shared Sprint Planning One, multi-team refinement, one product-level Sprint Review and an Overall Retrospective.",
        "Compared with SAFe, LeSS has far fewer roles and layers but demands deeper organisational change, such as removing functional reporting lines.",
        "Adopt it deep and narrow: one product group at a time, with education first and volunteers wherever possible.",
    ],
    sections=[
        S(
            "What is Large-Scale Scrum (LeSS)?",
            "**Large-Scale Scrum (LeSS)** is a lightweight framework for scaling Scrum to many teams that build one "
            "product together. All teams share one Product Owner, one Product Backlog, one Definition of Done and "
            "one Sprint, and deliver one integrated product increment. Instead of adding roles and layers, LeSS "
            "changes the organisation around the product.",
            "LeSS grew out of practical work by **Craig Larman and Bas Vodde**, who began collaborating on scaling "
            "Scrum in 2005 when clients asked for help with large, multi-site and offshore development. Their ideas "
            "are set out in three books: *Scaling Lean & Agile Development* (2008), *Practices for Scaling Lean & "
            "Agile Development* (2010) and *Large-Scale Scrum: More with LeSS*, which acts as a primer for the "
            "series. The official site, less.works, lists adoptions in organisations such as Ericsson, Nokia "
            "Networks, UBS, Cisco and bwin.party, most of them with around five teams in one or two locations.",
            "The central idea is that **large-scale Scrum is still Scrum**. It is not team-level Scrum with a "
            "management layer on top. If you know "
            "[what Scrum is](/project-management/scrum/what-is-scrum/), you already know most of LeSS; the "
            "difference lies in how many teams share each element and how the organisation is structured around them.",
            H3("The building blocks of LeSS"),
            "LeSS is published as four layers, from firm to optional:",
            T(
                ["Layer", "What it contains", "How binding it is"],
                ["Principles", "Ten ideas, such as whole-product focus and systems thinking, used to decide anything the rules do not cover", "The foundation for every decision"],
                ["Rules", "A short set of rules that define the LeSS and LeSS Huge structures (current version dated November 2024)", "Required: this is what makes it LeSS"],
                ["Guides", "Practical advice on applying the rules, such as how to run Sprint Planning One or adopt LeSS", "Recommended: try them"],
                ["Experiments", "Many situational ideas from the books that worked, or failed, somewhere", "Optional: use them to learn"],
            ),
        ),
        S(
            "LeSS rules: the \"one of everything\" structure",
            "Most of the LeSS rules can be summarised as **one of everything at product level**, with teams doing "
            "the work inside that frame. The table compares the main rules with a single-team Scrum setup.",
            T(
                ["Element", "One-team Scrum", "LeSS (2–8 teams)"],
                ["Product", "One product", "One product, defined broadly and from the customer's point of view"],
                ["Product Owner", "One", "One, for the whole product"],
                ["Product Backlog", "One", "One, shared by all teams"],
                ["Definition of Done", "One", "One common DoD; each team may make it stronger but not weaker"],
                ["Sprint", "One", "One product-level Sprint; all teams start and end together"],
                ["Increment", "One", "One integrated, potentially shippable increment"],
                ["Teams", "One Scrum Team", "Two to eight self-managing, cross-functional, long-lived feature teams"],
                ["Scrum Master", "One per team", "A dedicated, full-time Scrum Master for one to three teams"],
                ["Sprint Backlog and Daily Scrum", "One", "One per team"],
                ["Managers", "Not defined", "Optional; their focus moves to improving the product development system"],
            ),
            "LeSS also asks you to set up the **full structure for the product group from the start**, rather than "
            "piloting parts of it, and sets a long-term goal of a shippable product every Sprint or more often.",
            H3("One product, defined broadly"),
            "The product definition decides who is in the product group and what goes into the single "
            "[Product Backlog](/project-management/scrum/product-backlog/). LeSS recommends a broad, customer-centric "
            "definition: \"online banking\" rather than \"the payments API\". Narrow, component-based definitions "
            "recreate the hand-offs LeSS is designed to remove.",
            H3("One Definition of Done and undone work"),
            "All teams work to one [Definition of Done](/project-management/agile/definition-of-done/). LeSS "
            "contrasts it with a **perfect Definition of Done** that covers everything needed to put the product in "
            "customers' hands. The gap between the two is planned **undone work**, such as a separate release or "
            "performance test. Undone work hides risk and delay, so the aim is to expand the Definition of Done "
            "Sprint by Sprint until none is left.",
        ),
        S(
            "The 10 LeSS principles",
            "The principles are what you use when the rules are silent. less.works lists ten:",
            T(
                ["Principle", "What it means in practice"],
                ["Large-Scale Scrum is Scrum", "Keep Scrum's purpose, elements and empiricism at any size; do not invent a new process"],
                ["Empirical process control", "Shape the product, the process and the organisation through frequent inspection and adaptation"],
                ["Transparency", "Base decisions on done items, short cycles, shared definitions and a culture where problems can be raised safely"],
                ["More with less", "Get more learning, ownership and value with fewer roles, artifacts, special groups and processes"],
                ["Whole-product focus", "One backlog, one Product Owner, one increment and one Sprint, however many teams there are"],
                ["Customer-centric", "Judge value and waste from the paying customer's point of view and shorten the customer's wait"],
                ["Continuous improvement towards perfection", "Run small, bold improvement experiments every Sprint towards an ideal of perfect delivery"],
                ["Systems thinking", "Optimise the whole flow from concept to cash, not individual teams or people"],
                ["Lean thinking", "Managers as teachers who go and see the real work, stop and fix problems, and respect people"],
                ["Queuing theory", "Use what is known about queues to manage work in progress, batch size and variability"],
            ),
            "Lean thinking and queuing theory explain why LeSS avoids component teams, which create queues between "
            "teams, and prefers small items. See [WIP limits](/project-management/kanban/wip-limits/) for the idea in practice.",
        ),
        S(
            "LeSS roles",
            "LeSS has the same three Scrum accountabilities as one-team Scrum. It adds only one role, the Area "
            "Product Owner, and only in LeSS Huge.",
            H3("Product Owner"),
            "With up to eight teams, the [Product Owner](/project-management/scrum/scrum-product-owner/) cannot "
            "write and explain every item personally. LeSS does not solve this with proxies. Instead, the Product "
            "Owner focuses on prioritisation and the overall direction, and the teams **clarify items directly "
            "with customers, users and stakeholders**. All prioritisation still goes through the Product Owner, and "
            "only the Product Owner gives work to the teams.",
            H3("Teams: feature teams, not component teams"),
            "LeSS is built on **feature teams**: stable, cross-functional, cross-component teams that can take a "
            "customer-centric item from the backlog and finish it. Most organisations start with component teams "
            "or functional groups, so this is usually the biggest structural change.",
            T(
                ["", "Feature team", "Component team"],
                ["Owns", "Customer features end to end", "One technical layer or component"],
                ["Backlog items", "Customer-centric features", "Technical tasks split from a feature"],
                ["Hand-offs per feature", "Few or none", "Several teams, with queues between them"],
                ["Coordination", "Mostly in code and through shared practices", "Mostly through plans, managers and integration phases"],
                ["Learning", "Broad, across the product", "Deep but narrow"],
                ["Risk", "Code quality across components needs active care", "Late integration and delayed customer feedback"],
            ),
            "Feature teams need enough collective skill to finish items, not individuals who know everything. Our "
            "guide to [Agile team structures](/project-management/agile/agile-team-structures/) compares the models.",
            H3("Scrum Master"),
            "In LeSS, the [Scrum Master](/project-management/agile/scrum-master-role/) is a dedicated, full-time "
            "role that serves one to three teams. The focus shifts from a single team towards the whole system: "
            "the Product Owner, cross-team coordination, engineering practices and organisational policies that "
            "get in the way.",
            H3("Managers"),
            "Managers are optional. Where they exist, they stop directing daily work and act as teachers and "
            "capability builders who go and see the work and remove systemic impediments. LeSS also recommends "
            "**removing project managers from the teams**, because the Product Owner and teams share that work.",
        ),
        S(
            "LeSS events step by step",
            "Every LeSS Sprint follows the same pattern. Here is the order of events in one Sprint:",
            OL(
                "**Sprint Planning One (all teams).** The Product Owner and the teams, or representatives of each team, meet together. The Product Owner presents the top items; the teams decide which team takes which items, clear up open questions and agree a Sprint Goal if they use one. A popular format is to lay the item cards on a table and let teams pick.",
                "**Sprint Planning Two (per team).** Each team plans how it will deliver its items and creates its own Sprint Backlog. When teams are working on closely related items, they hold a **multi-team Sprint Planning Two** in the same room, each still planning separately but able to discuss shared design and agree who does what.",
                "**Daily Scrum (per team).** Each team holds its own [Daily Scrum](/project-management/scrum/daily-scrum/). Teams can send an observer to another team's Daily Scrum when their work overlaps.",
                "**Coordination during the Sprint.** Teams coordinate directly and informally, mainly through code and conversation, rather than through a central coordinator. See the next section.",
                "**Product Backlog Refinement (preferably multi-team).** An optional, short overall refinement identifies which teams will probably build which items; detailed [backlog refinement](/project-management/scrum/backlog-refinement/) then happens per team or, often better, with two or more teams together.",
                "**Sprint Review (one for the product).** The Product Owner, members of all teams and relevant customers, users and stakeholders inspect the integrated increment. LeSS suggests a **bazaar** or science-fair format: each team staffs an area of a large room and stakeholders move between them.",
                "**Team Retrospectives.** Each team holds its own [Sprint Retrospective](/project-management/scrum/sprint-retrospective/).",
                "**Overall Retrospective.** After the team retrospectives, the Product Owner, the Scrum Masters, rotating team representatives and any managers meet to improve the whole system. The maximum length is 45 minutes per week of Sprint.",
            ),
            "Our guide to [Sprint Planning](/project-management/scrum/sprint-planning/) covers the single-team "
            "version in detail, and the [sprint planning template](/templates/sprint-planning-template/) works for "
            "each team's Sprint Planning Two.",
        ),
        S(
            "How teams coordinate in LeSS",
            "LeSS deliberately avoids coordination roles and status meetings between teams. It prefers decentralised, "
            "informal techniques, with teams responsible for coordinating with each other. less.works names several:",
            L(
                "**Just talk.** Developers on different teams talk directly when they need to, in person or in chat, without going through a manager or Scrum Master.",
                "**Communicate in code.** Teams integrate their work continuously into one shared codebase, so conflicts show up within hours rather than at the end of the Sprint. This depends on solid [continuous integration and delivery](/project-management/kanban/continuous-delivery/).",
                "**Travellers.** An expert in a specialist area joins different teams for a Sprint or two at a time to do real work with them and spread the knowledge.",
                "**Open Space.** A self-organised meeting where anyone can raise a topic, used for larger cross-team questions.",
                "**Communities.** Communities of practice around a component, a skill or a topic, such as test automation or user experience, that cut across teams.",
                "**Multi-team events.** Multi-team refinement and multi-team Sprint Planning Two are themselves major coordination tools.",
            ),
            "LeSS does not require a [Scrum of Scrums](/project-management/scrum/scrum-of-scrums/); if your teams "
            "find one useful, keep it short and run by the teams themselves.",
        ),
        S(
            "Worked example: one Sprint in a five-team LeSS product",
            "This example is **illustrative**: the company, teams and items are invented to show how the rules work "
            "in practice. An insurer runs one product, its customer claims platform, with five feature teams "
            "(Amber, Birch, Cedar, Delta and Elm), one Product Owner, two Scrum Masters and a two-week Sprint. All "
            "teams work in one shared codebase.",
            H3("Step 1: before the Sprint"),
            "In the previous Sprint, a short overall refinement suggested which teams would probably take the next "
            "items, and Amber and Birch refined the new photo-upload feature together.",
            H3("Step 2: Sprint Planning One"),
            "The Product Owner presents the top of the Product Backlog. Using the cards-on-the-table format, the "
            "teams agree the following split and a product-level Sprint Goal: \"Customers can submit a motor claim "
            "with photos from their phone.\"",
            T(
                ["Team", "Items taken", "Why this team"],
                ["Amber", "Photo upload in the claim form; photo compression", "Refined the feature last Sprint"],
                ["Birch", "Photo review screen for claim handlers", "Same feature as Amber; holds multi-team Sprint Planning Two with Amber"],
                ["Cedar", "Claim status notifications by text message", "Worked on notifications before"],
                ["Delta", "Fix for duplicate claim references; accessibility improvements", "Volunteered to learn the reference service"],
                ["Elm", "First slice of fraud-check integration", "Has the strongest knowledge of the partner API"],
            ),
            H3("Step 3: during the Sprint"),
            L(
                "Amber and Birch hold a multi-team Sprint Planning Two in one room, agree the shared photo data model and pair across teams on the first day.",
                "All teams integrate into the main branch several times a day, so a clash between Cedar's notification change and Delta's reference fix shows up on day 3 and is fixed by the two developers involved.",
            ),
            H3("Step 4: Sprint Review and retrospectives"),
            "The Sprint Review is a bazaar: five stations in one room, with claim handlers, a customer panel and "
            "the head of claims moving between them. They try the full photo journey end to end on a phone. The "
            "Product Owner then reorders the backlog based on the feedback.",
            "Each team then holds its retrospective. In the Overall Retrospective, the Product Owner, both Scrum "
            "Masters, one rotating member from each team and the head of engineering look at a system problem "
            "that three teams raised: the separate security review, which sits outside the Definition of Done and "
            "delays every release by about a week. They agree an experiment: a security specialist will work as a "
            "traveller with two teams next Sprint, with the aim of moving security review into the Definition of Done.",
            "Notice what is not in the example: no team-level Product Owners, no integration team, no release "
            "train and no project manager assigning work. That is what \"more with less\" looks like.",
        ),
        S(
            "LeSS Huge: more than eight teams",
            "When a product needs more than eight teams, one Product Owner can no longer keep the whole backlog in "
            "view. LeSS Huge solves this by dividing the product into **requirement areas** while keeping one "
            "product, one Product Backlog and one Sprint. Eight is an empirical limit, not "
            "a magic number, and LeSS Huge adds overhead, so do not use it for smaller groups.",
            T(
                ["Element", "Basic LeSS", "LeSS Huge"],
                ["Number of teams", "Two to eight", "More than eight"],
                ["Product Owner", "One", "One overall Product Owner, plus an Area Product Owner per requirement area"],
                ["Backlog", "One Product Backlog", "One Product Backlog; each item belongs to exactly one requirement area, viewed through an Area Product Backlog"],
                ["Team grouping", "None", "Requirement areas of four to eight teams each"],
                ["Sprint", "One product-level Sprint", "Still one product-level Sprint and one integrated product"],
                ["Product Owner coordination", "Not needed", "Product Owner and Area Product Owners form a Product Owner Team and synchronise before Sprint Planning and after the Sprint Review"],
            ),
            "A **requirement area** groups strongly related customer requirements, such as \"payments\" or "
            "\"onboarding\", not technical components. Teams specialise in one area for a long time, and the "
            "overall Product Owner decides how many teams work in each area, moving teams only when another area "
            "offers more value.",
            H3("Worked sizing example"),
            "This sizing is **illustrative**. A retail bank's mobile banking product has grown to 20 feature teams. "
            "The Product Owner and Area Product Owners group the backlog by customer area:",
            T(
                ["Requirement area", "Share of backlog value", "Teams", "Area Product Owner"],
                ["Everyday banking (accounts, cards, payments)", "About 40%", "8", "One"],
                ["Lending and mortgages", "About 35%", "7", "One"],
                ["Onboarding and identity", "About 25%", "5", "One"],
                ["Total", "100%", "20", "Three, plus the overall Product Owner"],
            ),
            "Every area has between four and eight teams, so the split fits the rules. Teams can move between areas "
            "as value shifts, but because they have specialised, each move costs learning time.",
            "LeSS Huge is adopted **incrementally**, often one requirement area at a time, and the less.works rules "
            "note that this can take months or years.",
        ),
        S(
            "LeSS vs SAFe vs Nexus vs Scrum@Scale",
            "LeSS is one of several ways to scale Scrum. The four best known compare as follows:",
            T(
                ["", "LeSS", "SAFe", "Nexus", "Scrum@Scale"],
                ["Philosophy", "Scrum scaled with minimal additions; change the organisation", "Comprehensive framework covering team, programme and portfolio", "Light exoskeleton around Scrum focused on integration", "Modular, scale-free networks of teams"],
                ["Typical size", "2–8 teams; LeSS Huge beyond", "Agile Release Trains of typically 50–125 people, up to portfolios", "About 3–9 Scrum Teams", "Any size, repeated in groups of 4–5 teams"],
                ["Product Owner", "One for the product (plus Area POs in LeSS Huge)", "Product Owners per team plus Product Management", "One Product Owner for the Nexus", "Product Owner per team plus Chief Product Owners"],
                ["New roles", "Very few", "Many (for example Release Train Engineer, Solution and Portfolio roles)", "Nexus Integration Team", "Scrum of Scrums Master, Executive Action Team, MetaScrum"],
                ["Organisational change", "Deep: feature teams, fewer managers, no functional silos", "Fits around existing structures", "Moderate", "Moderate to deep, led by executives"],
                ["Best for", "One product, leaders willing to simplify the organisation", "Large enterprises that want a detailed blueprint and portfolio governance", "Several teams on one product that need integration focus", "Organisations scaling Scrum across many products and leadership"],
            ),
            H3("How to choose"),
            L(
                "**Choose LeSS** if you have one product, your teams already run Scrum well and leaders are willing to restructure around feature teams.",
                "**Choose SAFe** if you need a documented model for many trains and portfolios, with roles and events that fit around existing governance. See our [SAFe guide](/project-management/agile/scaled-agile-framework-safe/) and [Agile Release Train](/project-management/agile/agile-release-train/) guide.",
                "**Choose Nexus** if you have three to nine teams and your biggest problem is integrating their work each Sprint.",
                "**Choose Scrum@Scale** if you want a modular approach that extends into executive leadership across several products.",
            ),
            "Whichever you choose, scale only when one team genuinely cannot deliver the product. See our guide to "
            "[Scrum at scale](/project-management/scrum/scrum-at-scale/) for the Scrum@Scale framework in detail.",
        ),
        S(
            "How to adopt LeSS step by step",
            "less.works sets out three principles for adoption:",
            L(
                "**Deep and narrow over broad and shallow.** Make LeSS work well in one product group before spreading it.",
                "**Top-down and bottom-up.** Leaders change structures and fund education; teams shape the details.",
                "**Use volunteering.** Let informed people volunteer for the first product and teams.",
            ),
            "Combining those principles with the LeSS getting-started guide gives a practical sequence:",
            OL(
                "**Educate everyone.** Give the whole product group several days of Scrum and LeSS training, then coaching. Explain why each rule exists.",
                "**Define the product.** Agree a broad, customer-centric definition. This sets the scope of the adoption and which people join.",
                "**Define done.** Agree the first common Definition of Done and list the undone work that remains outside it.",
                "**Form feature teams.** Let people self-design long-lived, cross-functional teams. People leave their functional departments and stop reporting to their old functional managers.",
                "**Make the Product Owner the only source of work.** All requests from managers, sales and other departments go through the Product Owner.",
                "**Remove project managers from the teams**, and agree new roles for functional managers as capability builders.",
                "**Create one Product Backlog** and run initial refinement with all teams. A [product backlog template](/templates/product-backlog-template/) helps if you are starting from scattered lists.",
                "**Start the first Sprint** with the full LeSS structure: Sprint Planning One, Sprint Planning Two, Daily Scrums, one Sprint Review and an Overall Retrospective.",
                "**Inspect and adapt the system.** Use the Overall Retrospective to strengthen the Definition of Done and remove organisational impediments.",
            ),
            "LeSS adoption is an organisational change, so it benefits from the same care as any "
            "[Agile transformation](/project-management/agile/agile-transformation/): clear reasons, visible "
            "leadership support and patience while productivity dips and recovers.",
        ),
        S(
            "Common LeSS mistakes",
            L(
                "**Scaling before Scrum works.** If one team cannot deliver a done increment each Sprint, eight teams will not either.",
                "**Renaming component teams as feature teams.** If every item still passes through three teams, nothing has changed.",
                "**Adding a Product Owner per team.** Team-level \"Product Owners\" who only pass on requirements recreate the proxy layer LeSS removes. Let teams talk to customers directly.",
                "**Running separate Sprints.** Staggered or different-length Sprints break the single integrated increment.",
                "**Letting teams weaken the Definition of Done.** Teams may only strengthen it. Undone work should shrink over time, not grow.",
                "**Creating requirement areas too early.** Requirement areas with one or two teams each are a common novice error; Basic LeSS does not use them at all.",
                "**Appointing a central coordinator.** A cross-team manager who allocates work undermines team self-management and the Product Owner's role.",
                "**Skipping the Overall Retrospective.** Without it, system-level problems, such as external sign-offs or tooling, are never tackled.",
                "**Reviewing slides instead of the product.** The Sprint Review should inspect working, integrated software with real stakeholders.",
                "**Ignoring engineering practices.** Without continuous integration and test automation, communicating in code does not work.",
            ),
        ),
        S(
            "Tools for running LeSS",
            "LeSS needs very little tooling: a single Product Backlog that every team can see, a Sprint Backlog per "
            "team and a way to integrate code continuously. Co-located teams can simply keep their Sprint Backlogs on "
            "physical boards. When you do use software, check that it can show **one product backlog across many "
            "teams**, rather than forcing a separate backlog per team.",
            L(
                "**[Jira](/project-management-tools/jira/)** is the most common choice for software teams. Every plan supports backlogs, sprints and boards, and Premium and Enterprise add Plans for cross-team planning, capacity and dependencies.",
                "**[Wrike](/project-management-tools/wrike/)**, our top-rated tool, suits LeSS groups that also need portfolio views, dashboards and request intake across departments, for example when non-software teams join the product group.",
            ),
            "See our comparison of [Scrum software tools](/project-management/scrum/scrum-software-tools/) for more "
            "options. The [sprint retrospective template](/templates/sprint-retrospective-template/) works for both "
            "team retrospectives and the Overall Retrospective.",
        ),
        S(
            "LeSS training and certification",
            "LeSS certifications are issued by **The LeSS Company B.V.** and delivered by licensed LeSS trainers. "
            "Scrum Alliance lists the courses in its catalogue, and attending them counts towards the Scrum "
            "Education Units needed to renew Scrum Alliance certifications.",
            T(
                ["Course", "Typical length", "Who it is for"],
                ["Certified LeSS Basics (CLB)", "One day", "Anyone involved in a LeSS adoption who needs an overview"],
                ["Certified LeSS Practitioner (CLP)", "Three days in person (a longer online provisional version also exists)", "Scrum Masters, Product Owners, managers and team members adopting LeSS"],
                ["Certified LeSS for Executives (CLE)", "Several days", "Senior leaders and managers supporting a LeSS adoption"],
            ),
            "Lengths vary by trainer. No certification is required to use LeSS; the rules and guides are free on less.works.",
            "Read our guide to [Scrum certification and training](/project-management/scrum/scrum-certification-and-training/) "
            "to compare LeSS courses with PSM, CSM and other options.",
        ),
    ],
    faq=[
        ("What is LeSS in Agile?",
         "Large-Scale Scrum, a framework for applying Scrum to many teams working on one product, with one Product "
         "Owner, one Product Backlog, one Definition of Done and one shared Sprint."),
        ("Who created LeSS?",
         "Craig Larman and Bas Vodde, who began working together on scaling Scrum in 2005, based on their work with "
         "large, multi-site product development groups."),
        ("How many teams can use LeSS?",
         "Basic LeSS is designed for two to eight teams. Above eight teams, LeSS Huge applies, with requirement areas "
         "of four to eight teams each."),
        ("What is LeSS Huge?",
         "The version of LeSS for more than eight teams. It divides the product into requirement areas, each with an "
         "Area Product Owner and four to eight teams, while keeping one Product Backlog and one Sprint."),
        ("Does LeSS have a Scrum Master?",
         "Yes. Each Scrum Master is a dedicated, full-time role serving one to three teams, with a focus on the "
         "whole system as well as the teams."),
        ("What are feature teams in LeSS?",
         "Long-lived, cross-functional and cross-component teams that deliver complete customer features end to end, "
         "rather than component teams that each own one technical layer."),
        ("What is Sprint Planning One and Two in LeSS?",
         "In Sprint Planning One, the Product Owner and all teams (or their representatives) decide which team takes "
         "which items. In Sprint Planning Two, each team, or several related teams together, plans how to do its work."),
        ("What is an Overall Retrospective?",
         "A retrospective held after the team retrospectives, in which the Product Owner, Scrum Masters, team "
         "representatives and any managers improve the whole system. It lasts at most 45 minutes per week of Sprint."),
        ("What is the difference between LeSS and SAFe?",
         "LeSS adds very few roles and events to Scrum and asks the organisation to restructure around feature teams. "
         "SAFe is a comprehensive framework with additional roles, events and portfolio layers that fits around "
         "existing structures."),
        ("What is the difference between LeSS and Nexus?",
         "Both scale Scrum for one product with one Product Owner and Product Backlog. Nexus, for about three to "
         "nine teams, adds a Nexus Integration Team; LeSS has no integration team and relies on feature teams and "
         "continuous integration."),
        ("Can LeSS work outside software?",
         "Yes, in principle, for any product built by several teams, and less.works lists adoptions in telecoms, "
         "banking and trading as well as software companies. Most published experience comes from software and systems products."),
        ("Is there a LeSS certification?",
         "Yes. The LeSS Company issues Certified LeSS Basics, Certified LeSS Practitioner and Certified LeSS for "
         "Executives, delivered by licensed trainers. Certification is not required to use LeSS."),
    ],
)
