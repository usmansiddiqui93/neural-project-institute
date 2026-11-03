"""Apply a rewrite file to the live English page (string surgery, keeps the page shell untouched).
Usage: python3 render.py <rw name> [<rw name> ...]   (names in rw/ without .py)"""
import sys, os, re, json, html, importlib.util, datetime

SITE = "/home/claude/neural-project-institute"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
TODAY = datetime.date.today()
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
CAL_SVG = '<svg width="15" height="15" viewBox="0 0 16 16" aria-hidden="true"><rect x="1.5" y="2.5" width="13" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M1.5 6.5h13M5 1v3M11 1v3" stroke="currentColor" stroke-width="1.4"/></svg>'


def load(name):
    f = os.path.join(HERE, "rw", name + ".py")
    spec = importlib.util.spec_from_file_location("rw_" + name.replace("-", "_"), f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.URL, m.RW


def slug(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t).lower().replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:80] or "section"


def inline(t):
    t = html.escape(t, quote=True)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    return t


def plain(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return t.replace("**", "")


def page_label(url):
    f = SITE + url + "index.html"
    if not os.path.exists(f): return None
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<li aria-current="page">([^<]+)</li>', s)
    return html.unescape(m.group(1)) if m else None


READNEXT = re.compile(r"(?:^|(?<=[.!?] ))((?:See|Read)\b[^.!?]*?\[([^\]]+)\]\((/[^)\s]+)\)[^.!?]*[.!?])\s*$")


def para(t):
    out = f"<p>{inline(t)}</p>"
    m = READNEXT.search(t)
    if m:
        url = m.group(3)
        label = page_label(url) or m.group(2)
        label = label[:1].upper() + label[1:]
        out += (f'\n<aside class="readnext"><span class="rn-eye">Read next</span><div class="rn-links">'
                f'<a href="{url}"><b>{html.escape(label)}</b><i aria-hidden="true">→</i></a></div></aside>')
    return out


def block(b, used_ids):
    if isinstance(b, str):
        return para(b)
    kind, val = b
    if kind == "ul":
        return "<ul>" + "".join(f"<li>{inline(i)}</li>" for i in val) + "</ul>"
    if kind == "ol":
        return "<ol>" + "".join(f"<li>{inline(i)}</li>" for i in val) + "</ol>"
    if kind == "table":
        head = "".join(f"<th>{inline(h)}</th>" for h in val["head"])
        rows = "".join("<tr>" + "".join(f"<td>{inline(str(c))}</td>" for c in r) + "</tr>" for r in val["rows"])
        return f'<div class="tw"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    if kind == "tip":
        return f'<aside class="tip"><span>Tip</span><p>{inline(val)}</p></aside>'
    if kind == "h3":
        i = slug(val)
        while i in used_ids: i += "-2"
        used_ids.add(i)
        return f'<h3 id="{i}">{inline(val)}</h3>'
    if kind == "widget":
        raise ValueError(f"widget {val!r} not supported for static pages")
    raise ValueError(kind)


def words(R):
    out = []
    def walk(x):
        if isinstance(x, str): out.append(plain(x))
        elif isinstance(x, dict): [walk(v) for v in x.values()]
        elif isinstance(x, (list, tuple)): [walk(v) for v in x]
    walk([R.get("intro", ""), R.get("takeaways", []), R["sections"], R["faq"]])
    return len(" ".join(out).split())


def sub1(pattern, repl, s, what, flags=re.S):
    new, n = re.subn(pattern, lambda m: repl, s, count=1, flags=flags)
    if n != 1: raise RuntimeError(f"could not find {what}")
    return new


def apply(name, date=None):
    url, R = load(name)
    date = date or TODAY
    f = SITE + url + "index.html"
    s = open(f, encoding="utf-8").read()
    title, desc = R["title"], R["desc"]
    brand = " | Neural Project Institute"
    wc = words(R)
    mins = max(1, round(wc / 220))

    # head
    s = sub1(r"<title>.*?</title>", f"<title>{html.escape(title, quote=False)}{brand}</title>", s, "title")
    s = sub1(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(desc)}">', s, "description")
    s = sub1(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{html.escape(title + brand)}">', s, "og:title")
    s = sub1(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{html.escape(desc)}">', s, "og:description")

    # JSON-LD
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    data = json.loads(m.group(1))
    graph = data.get("@graph", [data])
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in R["faq"]]}
    newg, had_faq = [], False
    for g in graph:
        if g.get("@type") == "Article":
            g["headline"] = title; g["description"] = desc; g["dateModified"] = date.isoformat(); g["wordCount"] = wc
        if g.get("@type") == "FAQPage":
            g = faq_ld; had_faq = True
        newg.append(g)
    if not had_faq: newg.append(faq_ld)
    if "@graph" in data: data["@graph"] = newg
    else: data = newg[0]
    s = s[:m.start(1)] + json.dumps(data, ensure_ascii=False) + s[m.end(1):]

    # header
    s = re.sub(r"<h1>.*?</h1>", f"<h1>{html.escape(title, quote=False)}</h1>", s, count=1, flags=re.S)
    s = sub1(r'<p class="lead">.*?</p>', f'<p class="lead">{inline(R["intro"])}</p>', s, "lead")
    dt = f'<time datetime="{date.isoformat()}">{date.day} {MONTHS[date.month-1]} {date.year}</time>'
    if "Last updated <time" in s:
        s = re.sub(r'Last updated <time datetime="[^"]*">[^<]*</time>', "Last updated " + dt, s, count=1)
    else:
        s, n = re.subn(r'(<ul class="bmeta"><li>.*?</li>)', lambda mm: mm.group(1) + f"<li>{CAL_SVG}<span>Last updated {dt}</span></li>", s, count=1, flags=re.S)
        if n != 1: raise RuntimeError("byline")
    s = re.sub(r"<span>\d+ min read</span>", f"<span>{mins} min read</span>", s, count=1)

    # takeaways
    tk = "".join(f"<li>{inline(t)}</li>" for t in R.get("takeaways", []))
    s = sub1(r'<section id="key-takeaways" class="takeaways top">.*?</section>',
             f'<section id="key-takeaways" class="takeaways top"><h2>Key takeaways</h2><ul>{tk}</ul></section>', s, "takeaways")

    # body sections
    used = set()
    secs, toc = [], ['<li><a href="#key-takeaways">Key takeaways</a></li>']
    for sec in R["sections"]:
        body = "".join(block(b, used) for b in sec["blocks"])
        if sec["h"]:
            i = slug(sec["h"])
            while i in used: i += "-2"
            used.add(i)
            secs.append(f'<section id="{i}"><h2>{inline(sec["h"])}</h2>{body}</section>')
            toc.append(f'<li><a href="#{i}">{html.escape(plain(sec["h"]))}</a></li>')
        else:
            secs.append(f"<section>{body}</section>")
    a0 = s.index('<div class="abody">') + len('<div class="abody">')
    tail_start = None
    for marker in ('<section id="free-templates">', '<section id="faq">'):
        k = s.find(marker, a0)
        if k != -1: tail_start = k; break
    if tail_start is None: raise RuntimeError("no free-templates/faq section")
    old_body = s[a0:tail_start]
    callout = re.search(r'<aside class="tplcallout">.*?</aside>', old_body, re.S)
    if callout and len(secs) > 2:
        secs.insert(2, callout.group(0))
    s = s[:a0] + "\n" + "\n".join(secs) + "\n" + s[tail_start:]
    if '<section id="free-templates">' in s:
        toc.append('<li><a href="#free-templates">Free templates</a></li>')
    toc.append('<li><a href="#faq">Frequently asked questions</a></li>')
    s = sub1(r'<nav aria-label="Table of contents"><ol>.*?</ol></nav>', f'<nav aria-label="Table of contents"><ol>{"".join(toc)}</ol></nav>', s, "toc")

    # FAQ
    faq = "".join(f"<details class='faq'><summary>{inline(q)}</summary><p>{inline(a)}</p></details>" for q, a in R["faq"])
    s = sub1(r'<section id="faq">.*?</section>', f'<section id="faq"><h2>Frequently asked questions</h2>{faq}</section>', s, "faq")

    open(f, "w", encoding="utf-8").write(s)
    return url, title, desc, wc


def update_cards(url, old_title, old_desc, title, desc):
    """Refresh this page's title/description on English cards and prev/next links site-wide."""
    langs = ("/de/", "/es/", "/fr/", "/it/", "/ja/", "/ru/", "/zh/")
    n = 0
    for root, _, files in os.walk(SITE):
        rel = root[len(SITE):] + "/"
        if rel.startswith("/.git") or any(rel.startswith(l) for l in langs): continue
        if "index.html" not in files: continue
        p = os.path.join(root, "index.html"); s = open(p, encoding="utf-8").read()
        if f'href="{url}"' not in s: continue
        s2 = s
        if old_title and old_title != title:
            s2 = re.sub(r'(<a class="card" href="%s">(?:(?!</a>).)*?<b>)%s(</b>)' % (re.escape(url), re.escape(html.escape(old_title, quote=False))), lambda m: m.group(1) + html.escape(title, quote=False) + m.group(2), s2, flags=re.S)
            s2 = re.sub(r'(href="%s"><small>(?:Previous|Next)</small>)%s(</a>)' % (re.escape(url), re.escape(html.escape(old_title, quote=False))), lambda m: m.group(1) + html.escape(title, quote=False) + m.group(2), s2)
        if old_desc and old_desc != desc:
            s2 = re.sub(r'(<a class="card" href="%s">(?:(?!</a>).)*?<span>)%s(</span>)' % (re.escape(url), re.escape(html.escape(old_desc, quote=False))), lambda m: m.group(1) + html.escape(desc, quote=False) + m.group(2), s2, flags=re.S)
        if s2 != s:
            open(p, "w", encoding="utf-8").write(s2); n += 1
    return n


def sitemap(url, date):
    p = SITE + "/sitemap.xml"; s = open(p, encoding="utf-8").read()
    loc = "https://neuralprojectinstitute.com" + url
    s = re.sub(r"(<loc>%s</loc><lastmod>)[^<]*(</lastmod>)" % re.escape(loc), lambda m: m.group(1) + date.isoformat() + m.group(2), s)
    open(p, "w", encoding="utf-8").write(s)


def old_meta(url):
    s = open(SITE + url + "index.html", encoding="utf-8").read()
    t = re.search(r"<h1>(.*?)</h1>", s, re.S).group(1)
    d = re.search(r'<meta name="description" content="([^"]*)">', s).group(1)
    return html.unescape(t), html.unescape(d)


if __name__ == "__main__":
    for name in sys.argv[1:]:
        url, _ = load(name)
        ot, od = old_meta(url)
        url, t, d, wc = apply(name)
        n = update_cards(url, ot, od, t, d)
        sitemap(url, TODAY)
        print(f"{url}: {wc} words, cards updated on {n} pages")
