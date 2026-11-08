"""Build /llms.txt (index of every English page) and /llms-full.txt (full text of every English page).
Usage: python3 gen_llms.py   (reads and writes /home/claude/neural-project-institute)"""
import os, re, html
from bs4 import BeautifulSoup, NavigableString, Tag

SITE = "/home/claude/neural-project-institute"
BASE = "https://neuralprojectinstitute.com"
LANGS = ("de", "es", "fr", "it", "ja", "ru", "zh")
SKIP_TOP = {"unsubscribe", "verify", "assets", "fonts"}
DROP = "script, style, noscript, svg, form, button, nav, footer, .crumbs, .ctabox, .pn, .share, .tplcallout, .readnext, img, picture, video, iframe, .bwho, .bimg, aside.toc, .dlbox, figcaption, .tplthumb, .eyebrow, .pmai-box, .sharebar"


def pages():
    out = []
    for root, dirs, files in os.walk(SITE):
        rel = root[len(SITE):].strip("/")
        top = rel.split("/")[0] if rel else ""
        if top.startswith(".") or top in LANGS or top in SKIP_TOP:
            dirs[:] = []; continue
        if "index.html" not in files: continue
        s = open(os.path.join(root, "index.html"), encoding="utf-8").read()
        if 'http-equiv="refresh"' in s: continue
        if re.search(r'<meta name="robots" content="[^"]*noindex', s): continue
        out.append(("/" + rel + "/" if rel else "/", s))
    return out


def meta(s):
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    t = html.unescape(t.group(1)).split(" | Neural Project Institute")[0].strip() if t else ""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    h1 = html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else t
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    return (t if h1.startswith("Plan it") else (h1 or t)), html.unescape(d.group(1)) if d else ""


def text(el):
    out = []
    for c in el.children:
        if isinstance(c, NavigableString): out.append(str(c))
        elif isinstance(c, Tag):
            inner = text(c)
            if c.name in ("strong", "b"): out.append(f"**{inner.strip()}**" if inner.strip() else "")
            elif c.name in ("em", "i"): out.append(f"*{inner.strip()}*" if inner.strip() else "")
            elif c.name == "a" and c.get("href", "").startswith("/"): out.append(f"[{inner.strip()}]({BASE}{c['href']})")
            elif c.name == "br": out.append(" ")
            else: out.append(inner)
    return re.sub(r"\s+", " ", "".join(out))


def md(el, lines):
    for c in el.children:
        if not isinstance(c, Tag):
            t = str(c).strip()
            if t: lines.append(re.sub(r"\s+", " ", t))
            continue
        n = c.name
        if n in ("h1", "h2", "h3", "h4"):
            lines.append("\n" + "#" * (int(n[1]) + 1) + " " + text(c).strip())
        elif n == "p":
            t = text(c).strip()
            if t: lines.append(t)
        elif n in ("ul", "ol"):
            for i, li in enumerate(c.find_all("li", recursive=False), 1):
                t = text(li).strip()
                if t: lines.append(("%d. " % i if n == "ol" else "- ") + t)
        elif n == "table":
            rows = []
            for tr in c.find_all("tr"):
                cells = [text(td).strip().replace("|", "/") for td in tr.find_all(["th", "td"])]
                if cells: rows.append(cells)
            if rows:
                w = max(len(r) for r in rows)
                rows = [r + [""] * (w - len(r)) for r in rows]
                lines.append("| " + " | ".join(rows[0]) + " |")
                lines.append("|" + " --- |" * w)
                for r in rows[1:]: lines.append("| " + " | ".join(r) + " |")
        elif n == "details":
            q = c.find("summary")
            qt = text(q).strip() if q else ""
            if q: q.extract()
            lines.append(f"\n**Q: {qt}**")
            sub = []; md(c, sub); lines.append(" ".join(x.strip() for x in sub if x.strip()))
        else:
            md(c, lines)


def body(s):
    soup = BeautifulSoup(s, "html.parser")
    main = soup.find("main") or soup.body
    if main is None: return ""
    for x in main.select(DROP): x.decompose()
    lines = []; md(main, lines)
    out, prev = [], None
    for l in lines:
        l = l.rstrip()
        if not l or l == prev: continue
        out.append(l); prev = l
    return "\n".join(out)


def section(u):
    if u == "/": return "Home"
    if u.startswith("/project-management-tools/"):
        if "-vs-" in u: return "Tool comparisons"
        if u.endswith("-alternatives/"): return "Tool alternatives"
        return "Project management software reviews"
    if u.startswith("/templates/"): return "Free templates"
    if u.startswith("/project-management/agile/"): return "Agile guides"
    if u.startswith("/project-management/scrum/"): return "Scrum guides"
    if u.startswith("/project-management/kanban/"): return "Kanban guides"
    if u.startswith("/project-management/industries/"): return "Industry guides"
    if u.startswith("/project-management/"): return "Project management guides"
    if u.startswith("/reviews/"): return "Learner reviews"
    return "About and policies"


ORDER = ["Home", "Project management guides", "Agile guides", "Scrum guides", "Kanban guides", "Industry guides",
         "Free templates", "Project management software reviews", "Tool comparisons", "Tool alternatives",
         "Learner reviews", "About and policies"]

INTRO = """# Neural Project Institute

> Neural Project Institute (neuralprojectinstitute.com) is an independent project management education site. It publishes free, in-depth guides on project management, Agile, Scrum and Kanban; free Excel, Google Sheets and PDF templates; independent reviews and comparisons of project management software; and the PMAI (Project Management Artificial Intelligence) certification. Contact: support@neuralprojectinstitute.com.

Guides are written in British English, cite primary sources (PMI, the Scrum Guide 2020, the Kanban Guide, vendor documentation) and label worked examples as illustrative. Most pages are also available in German, Spanish, French, Italian, Japanese, Russian and Chinese under /de/, /es/, /fr/, /it/, /ja/, /ru/ and /zh/. The full text of every English page is in [llms-full.txt](https://neuralprojectinstitute.com/llms-full.txt).
"""


def main():
    ps = sorted(pages(), key=lambda x: x[0])
    groups = {k: [] for k in ORDER}
    full = [INTRO.replace("The full text of every English page is in [llms-full.txt](https://neuralprojectinstitute.com/llms-full.txt).", "This file contains the full text of every English page; the index is in [llms.txt](https://neuralprojectinstitute.com/llms.txt)."), ""]
    for u, s in ps:
        t, d = meta(s)
        groups[section(u)].append((u, t, d))
    idx = [INTRO]
    for k in ORDER:
        if not groups[k]: continue
        idx.append(f"\n## {k}\n")
        for u, t, d in groups[k]:
            idx.append(f"- [{t}]({BASE}{u})" + (f": {d}" if d else ""))
    open(SITE + "/llms.txt", "w", encoding="utf-8").write("\n".join(idx) + "\n")
    pages_by_url = dict(ps)
    for k in ORDER:
        for u, t, d in groups[k]:
            full.append(f"\n\n---\n\n# {t}\n\nURL: {BASE}{u}\nSection: {k}\n" + (f"Summary: {d}\n" if d else "") + "\n" + body(pages_by_url[u]))
    open(SITE + "/llms-full.txt", "w", encoding="utf-8").write("\n".join(full) + "\n")
    print(len(ps), "pages")


if __name__ == "__main__":
    main()
