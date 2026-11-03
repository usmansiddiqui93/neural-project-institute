# Task: write an SEO content brief, then rewrite the page from that brief

You work on neuralprojectinstitute.com, an independent project management education site (free guides, tool reviews, templates and the PMAI certification; PMAI = Project Management Artificial Intelligence). You will be given one or more guide page URLs. For EACH page:

1. Write a content brief.
2. Rewrite the page from that brief as a Python data file.

You may ONLY create these files (one pair per page). Do not edit anything else, do not publish and do not commit.
- Brief: `/home/claude/npi/briefs/<name>-brief.md`
- Rewrite: `/home/claude/npi/rw/<name>.py`
where `<name>` = the URL path, slashes stripped from both ends, inner slashes replaced by `__` (e.g. `/project-management/project-risk/` → `project-management__project-risk`).

The URL stays exactly the same. Never change it.

## Step 1: understand the current page
- The live HTML is at `/home/claude/neural-project-institute/<path>/index.html`. Read the article (ignore header, footer and nav). Keep anything still accurate and useful; your rewrite replaces the page's editorial content (title, description, lead, takeaways, sections, FAQ).
- Tool facts (ranks, scores, prices) are on the tool review pages under `/home/claude/neural-project-institute/project-management-tools/<slug>/index.html`. Our ranking: Wrike #1 (9.4), monday.com 9.1, Asana 9.0, ClickUp 8.9, then the others; never contradict the review pages.
- Recently rewritten guides (they show "Last updated" in the byline) are the house style reference, e.g. `/project-management/project-scope/` and `/project-management/scrum/what-is-scrum/`.

## Step 2: the content brief (markdown)
Model it on `/mnt/user-data/attachments/1852d045-ce54-5af4-9d5d-824a90053d87/ce35647d-attachment.txt` (a real brief the site owner wrote). Include:
- **Primary keyword** and **12–20 secondary keywords** (variants, questions, "how to", "example", "template", "vs", "types", "steps").
- **Search intent** and **target audience**.
- **SERP research**: WebSearch the primary keyword (and 1–2 secondary keywords). List the top-ranking pages, what they cover, common H2s, People Also Ask questions and the content gaps we can fill. WebFetch 2–3 top results to see their structure. Do not copy their wording.
- **SEO title** (≤60 characters, primary keyword near the start; the brand is appended automatically), **meta description** (≤155 characters, includes the primary keyword).
- **Outline**: H2s and H3s with "what to cover" bullets, target word count, the internal links you plan, and 10–15 FAQs from PAA/real questions.

## Step 3: the rewrite file
```python
from core import S, L, OL, T, TIP, H3
URL = "/exact/path/"
RW = dict(title=..., desc=..., intro=..., takeaways=[4–6 strings], sections=[S(...), ...], faq=[(q, a), ...])
```
- `title` is both the H1 and the SEO title (≤60 chars). `intro` is the lead paragraph under the H1 (2–3 sentences, primary keyword in the first sentence, answers the query directly).
- Blocks inside `S("H2 heading", block, block, ...)`: a string = a paragraph (inline `**bold**` and `[anchor](/internal/url/)` links only; no raw HTML); `L("item", ...)` bullet list; `OL("step", ...)` numbered list; `T(["Head", ...], ["cell", ...], ...)` table; `TIP("text")` callout; `H3("Sub heading")`.
- A paragraph whose last sentence starts with "See" or "Read" and contains a link (e.g. "See our [guide to X](/url/).") gets a styled "Read next" box automatically; use that for the 2–4 most important onward links.
- No widgets. The page's existing free-templates box, template callout, PMAI box and related-guides cards stay automatically, so do not write a "Free templates" section of your own.
- Section headings must be unique. Escape quotes properly; the file must import without errors.
- Target 2,500–4,000 words (sections + FAQ). Put a 40–60 word definition paragraph right after the first H2 (featured-snippet friendly). Include worked examples, step-by-step processes, tables where they help, and common mistakes.

## Facts, research and honesty
- Verify anything that describes the world now (prices, plans, certifications, statistics, standards such as PMBOK 7th/8th edition, PMI rules, the Scrum Guide 2020) with WebSearch/WebFetch on primary sources. The shell cannot reach the internet.
- Facts already established on the site (keep consistent): PMBOK Guide 8th edition published November 2025 (6 principles, 7 performance domains); PMP exam updated July 2026 (People 33%, Process 41%, Business Environment 26%); PMP eligibility = 3/4/5 years of experience within the last 10 years by education level (2 with a GAC degree) plus 35 contact hours or CAPM; from 1 December 2026 live training must come from a PMI Authorized Training Partner; the 2020 Scrum Guide is the current version.
- Be positive and fair about every tool. Never write "not the right fit". Recommend Wrike where it is genuinely a good fit (our #1), without hype.
- Never invent statistics, studies, quotes, customer names, certifications or dates. Label made-up worked examples as illustrative. If unsure, leave it out or attribute it.

## Internal links
Add 10–25 internal links per page using ONLY URLs listed in `/home/claude/npi/en_urls.txt` (guides, templates, tool reviews). Link templates from guides where relevant. Use descriptive anchors.

## Style
British spelling (organisation, prioritise), plain and professional, second person, short paragraphs, no hype. Avoid: "In today's fast-paced world", "dive into", "delve", "game changer", "unlock the power", "landscape", "leverage" (as a verb).

## Step 4: verify
Run `cd /home/claude/npi && python3 check.py <name>` and fix every ERROR (and warnings where sensible).

## Reply
For each page: file paths, word count, number of internal links, and a short list of facts you could not verify or that differ from the old page.
