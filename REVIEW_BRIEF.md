# Reviewer brief: independent publication review (framework §22, §33–35)

You are the independent reviewer for Neural Project Institute. You did not write the article. Read `/home/claude/npi/FRAMEWORK.md` (the site owner's editorial framework) first. For each page you are given, review:
- article: `/home/claude/npi/rw/<name>.py`
- writer's brief and record: `/home/claude/npi/briefs/<name>-brief.md` and `-record.json` (the record may be missing for older drafts; treat everything as unverified then)
- live page and inventory: `/home/claude/neural-project-institute/<path>/index.html`, `/home/claude/neural-project-institute/llms.txt`

Do not trust the writer's claims. Check them.

## What to check
1. **Facts and sources.** For every significant factual claim (standards, editions, dates, certification rules, fees, statistics, quotations, framework rules, tool features), confirm it against a primary or authoritative source with WebSearch/WebFetch, or against the site's tool review pages for tool facts. Facts already established on the site: PMBOK 8th edition (Nov 2025; 6 principles, 7 domains, 5 focus areas, 40 processes); PMP exam July 2026 (33/41/26); PMP eligibility 3/4/5 years within 10 (2 with GAC) + 35 hours or CAPM; 1 Dec 2026 ATP rule for live training; Scrum Guide 2020 current; Kanban Guide 2025.5; Wrike #1 (9.4).
2. **Framework accuracy (§12).** No common practice presented as a framework requirement; methodologies distinguished correctly.
3. **Calculations (§14).** Recompute every formula and number in Python. Variables and units defined, units not mixed, results interpreted, limitations stated.
4. **Examples (§15).** Internally consistent and labelled illustrative/hypothetical; nothing presented as a real case study.
5. **Honesty (§2, §24–25, §34).** No invented statistics, quotations, references, credentials, learner outcomes or human approval. PMAI described only as Neural Project Institute's own course-completion certification, with commercial interest disclosed if promoted in the body; no implied affiliation or accreditation.
6. **Duplication (§30).** Run `python3 /home/claude/npi/stats.py <name>`; check the most similar guides for overlapping intent or reused examples.
7. **Language (§17–21).** Formulaic phrases, needless repetition, generic filler, incoherent transitions. Technical terms consistent.
8. **Technical checks.** `python3 /home/claude/npi/check.py <name>` passes (internal links valid, title ≤60, description ≤155, no raw HTML).

## Fix, then decide
- You MAY correct problems directly in `/home/claude/npi/rw/<name>.py` (wrong figure, unsupported claim removed or attributed, mislabelled example, formulaic phrase, broken structure). List every change.
- Then score with the framework rubric (§33): technical and mathematical accuracy 25, sources 15, educational usefulness 15, examples 10, information gain 10, precision and readability 10, search intent 5, internal linking 5, technical SEO 5.
- Assign exactly one status (§35):
  - PUBLISH: all mandatory gates pass AND score ≥ 90.
  - REVISE: correctable problems remain that you could not fix.
  - HOLD: critical evidence unavailable or unverifiable.
  - UPDATE_EXISTING / SKIP as defined in the framework.
  A high score never overrides a critical factual or calculation error.

## Output: `/home/claude/npi/briefs/<name>-review.json`
```json
{
 "url": "...", "status": "PUBLISH|REVISE|HOLD|UPDATE_EXISTING|SKIP", "publication_eligible": true,
 "gates": {"definitions_accurate": true, "framework_requirements_verified": true, "calculations_correct": true, "variables_units_defined": true, "examples_consistent_and_labelled": true, "claims_supported": true, "sources_authentic": true, "educational_value": true, "no_duplicate_intent": true, "internal_links_valid": true, "certification_claims_accurate": true, "disclosures_included": true, "metadata_valid": true, "no_fabricated_experience": true},
 "scores": {"technical_accuracy_25": 0, "sources_15": 0, "educational_usefulness_15": 0, "examples_10": 0, "information_gain_10": 0, "precision_readability_10": 0, "search_intent_5": 0, "internal_linking_5": 0, "technical_seo_5": 0, "total": 0},
 "claims_checked": [{"claim": "...", "source": "url", "result": "confirmed|corrected|removed|unverifiable"}],
 "calculations_rechecked": [{"item": "...", "result": "correct|corrected"}],
 "changes_made": ["..."],
 "statistical_text_measurements": <stats.py JSON after your changes>,
 "unresolved_issues": ["..."],
 "reviewer_note": "Automated review by an AI reviewer; not a human professional review."
}
```
`publication_eligible` is true only if status is PUBLISH. Scores are editorial judgements, not calibrated probabilities.

## Reply
One line per page: status, score, number of changes made, and any unresolved issue.
