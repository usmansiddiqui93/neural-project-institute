"""Text measurements for a rewrite file (framework section 32). Descriptive diagnostics only, never AI-detection scores.
Usage: python3 stats.py <rw name> [--json]"""
import sys, os, re, json, math, importlib.util
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
SITE = "/home/claude/neural-project-institute"
FORMULAIC = ["in today's fast-paced", "fast-paced business environment", "rapidly evolving world", "increasingly competitive landscape",
             "effective project management is crucial", "it is important to note", "it's important to note", "let's delve", "delve",
             "game-changer", "game changer", "unlock the full potential", "unlock the power", "seamlessly integrate", "navigate the complexities",
             "pave the way", "in conclusion", "dive into", "not the right fit", "by implementing these strategies", "this helps ensure"]
WATCH = ["effective project management", "successful project delivery", "project managers should", "it is important to", "this helps ensure"]
STOP = set("the a an and or of to in on for with by is are be as at that this it its from was were will can may not your you their they".split())


def load(name):
    spec = importlib.util.spec_from_file_location("x", os.path.join(HERE, "rw", name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.URL, m.RW


def plain(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return t.replace("**", "")


def paragraphs(R):
    """Prose paragraphs only (strings and list items), tables excluded from sentence statistics."""
    paras, all_text = [], []
    def walk(b):
        if isinstance(b, str): paras.append(plain(b)); all_text.append(plain(b))
        elif isinstance(b, tuple):
            k, v = b
            if k in ("ul", "ol"): [ (paras.append(plain(i)), all_text.append(plain(i))) for i in v ]
            elif k == "table": all_text.append(" ".join(plain(str(c)) for c in v["head"] + sum(v["rows"], [])))
            elif k in ("tip", "h3"): all_text.append(plain(v)); (paras.append(plain(v)) if k == "tip" else None)
    paras.append(plain(R.get("intro", ""))); all_text.append(plain(R.get("intro", "")))
    for t in R.get("takeaways", []): all_text.append(plain(t))
    for s in R["sections"]:
        all_text.append(plain(s["h"] or ""))
        for b in s["blocks"]: walk(b)
    for q, a in R["faq"]:
        paras.append(plain(a)); all_text.append(plain(q) + " " + plain(a))
    return [p for p in paras if p.strip()], " ".join(all_text)


def tokens(t):
    return re.findall(r"[a-z0-9]+(?:['’-][a-z0-9]+)*", t.lower())


def ngram_rep(toks, n):
    grams = [tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)]
    if not grams: return 0.0, []
    c = Counter(grams)
    rep = sum(v for v in c.values() if v > 1) / len(grams)
    top = [(" ".join(g), v) for g, v in c.most_common(8) if v > 1 and not set(g) <= STOP]
    return round(rep, 4), top


def mattr(toks, w=100):
    if len(toks) < w: return round(len(set(toks)) / max(1, len(toks)), 4)
    vals = [len(set(toks[i:i + w])) / w for i in range(len(toks) - w + 1)]
    return round(sum(vals) / len(vals), 4)


def site_vectors(exclude):
    """Term-frequency vectors of every other live English guide (main article text only)."""
    vecs = {}
    for root, dirs, files in os.walk(SITE):
        rel = root[len(SITE):]
        if rel.split("/")[1:2] and rel.split("/")[1] in ("de", "es", "fr", "it", "ja", "ru", "zh", ".git", "assets"): dirs[:] = []; continue
        if not rel.startswith("/project-management/") or "index.html" not in files: continue
        u = rel + "/"
        if u == exclude: continue
        s = open(os.path.join(root, "index.html"), encoding="utf-8").read()
        if 'http-equiv="refresh"' in s: continue
        a = s.find('<div class="abody">'); b = s.find('<section id="faq">')
        body = re.sub(r"<[^>]+>", " ", s[a:b] if a > 0 else s)
        vecs[u] = Counter(t for t in tokens(body) if t not in STOP and len(t) > 2)
    return vecs


def cosine(a, b, idf):
    num = sum(a[t] * b[t] * idf.get(t, 0) ** 2 for t in a if t in b)
    na = math.sqrt(sum((v * idf.get(t, 0)) ** 2 for t, v in a.items()))
    nb = math.sqrt(sum((v * idf.get(t, 0)) ** 2 for t, v in b.items()))
    return num / (na * nb) if na and nb else 0.0


def measure(name):
    url, R = load(name)
    paras, text = paragraphs(R)
    toks = tokens(text)
    counts = Counter(toks); n = len(toks)
    H = -sum(v / n * math.log2(v / n) for v in counts.values()) if n else 0
    sents = [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9£$])", " ".join(paras)) if len(tokens(s)) > 0]
    sl = [len(tokens(s)) for s in sents]
    mean = sum(sl) / len(sl) if sl else 0
    sd = math.sqrt(sum((x - mean) ** 2 for x in sl) / len(sl)) if sl else 0
    pl = [len(tokens(p)) for p in paras]
    pm = sum(pl) / len(pl) if pl else 0
    psd = math.sqrt(sum((x - pm) ** 2 for x in pl) / len(pl)) if pl else 0
    openers = Counter(" ".join(tokens(s)[:2]) for s in sents)
    low = text.lower()
    # similarity to other guides
    vecs = site_vectors(url)
    me = Counter(t for t in toks if t not in STOP and len(t) > 2)
    df = Counter(); [df.update(set(v)) for v in vecs.values()]; df.update(set(me))
    N = len(vecs) + 1
    idf = {t: math.log(N / (1 + d)) + 1 for t, d in df.items()}
    sims = sorted(((round(cosine(me, v, idf), 3), u) for u, v in vecs.items()), reverse=True)[:5]
    return {
        "url": url,
        "word_count": n,
        "unique_words": len(counts),
        "type_token_ratio": round(len(counts) / n, 4) if n else None,
        "mattr_100": mattr(toks),
        "shannon_word_entropy_bits": round(H, 3),
        "normalised_entropy": round(H / math.log2(len(counts)), 4) if len(counts) > 1 else None,
        "sentences": len(sl),
        "avg_sentence_length": round(mean, 2),
        "sentence_length_sd": round(sd, 2),
        "sentence_length_cv": round(sd / mean, 3) if mean else None,
        "paragraph_length_mean": round(pm, 1), "paragraph_length_sd": round(psd, 1),
        "bigram_repetition_rate": ngram_rep(toks, 2)[0],
        "trigram_repetition_rate": ngram_rep(toks, 3)[0],
        "top_repeated_4grams": ngram_rep(toks, 4)[1],
        "most_common_sentence_openers": [(o, c) for o, c in openers.most_common(5) if c > 2],
        "formulaic_phrases_found": [p for p in FORMULAIC if p in low],
        "watch_phrases_counts": {p: low.count(p) for p in WATCH if low.count(p)},
        "most_similar_existing_guides": sims,
        "note": "Descriptive editorial diagnostics only. No AI-detection probability is calculated.",
    }


if __name__ == "__main__":
    for a in sys.argv[1:]:
        if a == "--json": continue
        r = measure(a[:-3] if a.endswith(".py") else a)
        print(json.dumps(r, ensure_ascii=False, indent=1))
