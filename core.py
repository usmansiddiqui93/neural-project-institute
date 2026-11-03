"""Content blocks for rewrite files (same format as the old generator).
A rewrite file defines URL = "/path/" and RW = dict(title, desc, intro, takeaways, sections, faq)."""


def S(h, *blocks):
    return {"h": h, "blocks": list(blocks)}


def L(*items):
    return ("ul", list(items))


def OL(*items):
    return ("ol", list(items))


def T(head, *rows):
    return ("table", {"head": list(head), "rows": [list(r) for r in rows]})


def TIP(text):
    return ("tip", text)


def H3(text):
    return ("h3", text)


def W(name):
    return ("widget", name)
