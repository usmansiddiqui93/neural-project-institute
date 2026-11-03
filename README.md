# NPI static rewrite tooling (branch `npi-tools`)

The original Python site generator was lost in a workspace reset (late Oct 2026). Until it is restored, English guide pages are rewritten directly in the static site (`main` branch).

## Recover after a reset
    git clone <repo> neural-project-institute            # main = the live site
    git clone -b npi-tools <repo> npi                     # this branch, cloned to /home/claude/npi
    pip install beautifulsoup4 --break-system-packages    # only needed for queue building

## Daily run
1. Next pages: guides in `queue.json` ("listed" first, then "other") whose live page has no "Last updated" line.
2. Agents follow `RW_BRIEF.md`, writing `briefs/<name>-brief.md` and `rw/<name>.py` (2 pages per agent, 5 agents).
3. Publish each finished batch: `./publish.sh "message" <rw names>` (checks, renders into the live HTML, refreshes cards/sitemap, pushes `main`, then backs up this branch).

## Notes
- `render.py` edits pages as text (never re-serialises with BeautifulSoup, which breaks SVG `viewBox`).
- Only guide pages (/project-management/...) are supported. Templates and tool pages need extra work.
- Translations are not updated by this tooling: translated pages keep their previous content.
