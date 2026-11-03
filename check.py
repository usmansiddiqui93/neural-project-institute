"""Validate rewrite files. Usage: python3 check.py <rw name> [...]"""
import sys, os, re, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
SITE = "/home/claude/neural-project-institute"


def link_ok(u):
    u = u.split("#")[0].split("?")[0]
    if not u.startswith("/") or u == "/": return True
    return os.path.exists(SITE + u + ("index.html" if u.endswith("/") else ""))


def check(name):
    f = os.path.join(HERE, "rw", name + ".py")
    spec = importlib.util.spec_from_file_location("x", f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    u, R = m.URL, m.RW; errs, warn = [], []
    expect = u.strip("/").replace("/", "__")
    if expect != name: errs.append(f"file name should be {expect}.py")
    if not os.path.exists(SITE + u + "index.html"): errs.append(f"URL {u} does not exist on the site")
    for n in ["title", "desc", "intro", "takeaways", "sections", "faq"]:
        if not R.get(n): errs.append(f"missing {n}")
    if len(R.get("title", "")) > 62: warn.append(f"title {len(R['title'])} chars (aim <= 60)")
    if len(R.get("desc", "")) > 158: warn.append(f"desc {len(R['desc'])} chars (aim <= 155)")
    text, widgets = [], []
    def walk(x):
        if isinstance(x, str): text.append(x)
        elif isinstance(x, dict): [walk(v) for v in x.values()]
        elif isinstance(x, (list, tuple)):
            if len(x) == 2 and x[0] == "widget": widgets.append(x[1])
            else: [walk(v) for v in x]
    walk(R.get("sections", [])); walk([R.get("intro", "")] + list(R.get("takeaways", []))); walk(R.get("faq", []))
    if widgets: errs.append(f"widgets are not supported on static pages: {widgets}")
    blob = "\n".join(text)
    if re.search(r"<[a-z][^>]*>", blob): errs.append("raw HTML found; use **bold** and [text](/url/) only")
    links = re.findall(r"\]\(([^)]+)\)", blob)
    broken = sorted({l for l in links if not link_ok(l)})
    if broken: errs.append(f"broken internal links: {broken}")
    internal = {l.split('#')[0] for l in links if l.startswith("/")}
    hs = [s["h"] for s in R.get("sections", []) if s["h"]]
    if len(hs) != len(set(hs)): errs.append("duplicate section headings")
    words = len(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", blob).split())
    for bad in ["delve", "dive into", "fast-paced world", "game changer", "game-changer", "unlock the power", "not the right fit"]:
        if bad in blob.lower(): warn.append(f"avoid phrase: {bad}")
    print(f"{name} {u}\n  words~{words} sections={len(hs)} faq={len(R.get('faq', []))} internal_links={len(internal)}")
    for e in errs: print("  ERROR", e)
    for w in warn: print("  warn", w)
    return not errs


if __name__ == "__main__":
    ok = all([check(a[:-3] if a.endswith(".py") else a) for a in sys.argv[1:]])
    sys.exit(0 if ok else 1)
