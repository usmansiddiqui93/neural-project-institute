"""Build /llms.txt (index of every English page) and /llms-full.txt (full text of every English page).
Usage: python3 gen_llms.py   (reads and writes /home/claude/neural-project-institute)"""
import os, re, html
from bs4 import BeautifulSoup, NavigableString, Tag

SITE = "/home/claude/neural-project-institute"
BASE = "https://neuralprojectinstitute.com"
LANGS = ("de", "es", "fr", "it", "ja", "ru", "zh")
SKIP_TOP = {"unsubscribe", "verify", "assets", "fonts"}
DROP = "script, style, noscript, svg, form, button, nav, footer, .crumbs, .ctabox, .pn, .share, .tplcallout, .readnext, img, picture, video, iframe, .bwho, .bimg, aside.toc, .dlbox, figcaption, .tplthumb, .eyebrow, .pmai-box, .sharebar"


def pages(lang=None):
    out = []
    start = SITE + ("/" + lang if lang else "")
    for root, dirs, files in os.walk(start):
        rel = root[len(SITE):].strip("/")
        top = rel.split("/")[0] if rel else ""
        if top.startswith(".") or (lang is None and top in LANGS) or top in SKIP_TOP:
            dirs[:] = []; continue
        if "index.html" not in files: continue
        s = open(os.path.join(root, "index.html"), encoding="utf-8").read()
        if 'http-equiv="refresh"' in s: continue
        if re.search(r'<meta name="robots" content="[^"]*noindex', s): continue
        out.append(("/" + rel + "/" if rel else "/", s))
    return out


def meta(s):
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    t = re.split(r"\s*\|\s*Neural Project Institute", html.unescape(t.group(1)))[0].strip() if t else ""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    h1 = html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else t
    d = re.search(r'<meta name="description" content="([^"]*)"', s) or re.search(r'<meta content="([^"]*)" name="description"', s)
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

Translated editions: [Deutsch](https://neuralprojectinstitute.com/de/llms.txt), [Español](https://neuralprojectinstitute.com/es/llms.txt), [Français](https://neuralprojectinstitute.com/fr/llms.txt), [Italiano](https://neuralprojectinstitute.com/it/llms.txt), [日本語](https://neuralprojectinstitute.com/ja/llms.txt), [Русский](https://neuralprojectinstitute.com/ru/llms.txt), [中文](https://neuralprojectinstitute.com/zh/llms.txt).
"""


def main_en():
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




# ---------- translated sites ----------
L10N = {
 "de": ("Deutsch", "Neural Project Institute (neuralprojectinstitute.com) ist eine unabhängige Bildungsseite zum Projektmanagement. Sie veröffentlicht kostenlose, ausführliche Leitfäden zu Projektmanagement, Agile, Scrum und Kanban, kostenlose Vorlagen für Excel, Google Sheets und PDF, unabhängige Tests und Vergleiche von Projektmanagement-Software sowie die PMAI-Zertifizierung (Project Management Artificial Intelligence). Kontakt: support@neuralprojectinstitute.com.",
        "Diese Datei listet die deutschsprachigen Seiten. Die englische Originalfassung steht unter", "Der vollständige Text aller deutschen Seiten steht in", "Diese Datei enthält den vollständigen Text aller deutschen Seiten; das Verzeichnis steht in",
        ["Startseite","Projektmanagement-Leitfäden","Agile-Leitfäden","Scrum-Leitfäden","Kanban-Leitfäden","Branchenleitfäden","Kostenlose Vorlagen","Tests von Projektmanagement-Software","Tool-Vergleiche","Tool-Alternativen","Bewertungen von Lernenden","Über uns und Richtlinien"]),
 "es": ("Español", "Neural Project Institute (neuralprojectinstitute.com) es un sitio independiente de formación en gestión de proyectos. Publica guías gratuitas y detalladas sobre gestión de proyectos, Agile, Scrum y Kanban; plantillas gratuitas para Excel, Google Sheets y PDF; análisis y comparativas independientes de software de gestión de proyectos; y la certificación PMAI (Project Management Artificial Intelligence). Contacto: support@neuralprojectinstitute.com.",
        "Este archivo enumera las páginas en español. La versión original en inglés está en", "El texto completo de todas las páginas en español está en", "Este archivo contiene el texto completo de todas las páginas en español; el índice está en",
        ["Inicio","Guías de gestión de proyectos","Guías de Agile","Guías de Scrum","Guías de Kanban","Guías por sector","Plantillas gratuitas","Análisis de software de gestión de proyectos","Comparativas de herramientas","Alternativas a herramientas","Opiniones de alumnos","Sobre nosotros y políticas"]),
 "fr": ("Français", "Neural Project Institute (neuralprojectinstitute.com) est un site indépendant de formation à la gestion de projet. Il publie des guides gratuits et détaillés sur la gestion de projet, Agile, Scrum et Kanban, des modèles gratuits pour Excel, Google Sheets et PDF, des tests et comparatifs indépendants de logiciels de gestion de projet, ainsi que la certification PMAI (Project Management Artificial Intelligence). Contact : support@neuralprojectinstitute.com.",
        "Ce fichier répertorie les pages en français. La version originale en anglais se trouve sur", "Le texte intégral de toutes les pages en français se trouve dans", "Ce fichier contient le texte intégral de toutes les pages en français ; l'index se trouve dans",
        ["Accueil","Guides de gestion de projet","Guides Agile","Guides Scrum","Guides Kanban","Guides par secteur","Modèles gratuits","Tests de logiciels de gestion de projet","Comparatifs d'outils","Alternatives aux outils","Avis des apprenants","À propos et politiques"]),
 "it": ("Italiano", "Neural Project Institute (neuralprojectinstitute.com) è un sito indipendente di formazione sul project management. Pubblica guide gratuite e approfondite su project management, Agile, Scrum e Kanban, modelli gratuiti per Excel, Google Sheets e PDF, recensioni e confronti indipendenti di software di project management e la certificazione PMAI (Project Management Artificial Intelligence). Contatto: support@neuralprojectinstitute.com.",
        "Questo file elenca le pagine in italiano. La versione originale in inglese si trova su", "Il testo completo di tutte le pagine in italiano si trova in", "Questo file contiene il testo completo di tutte le pagine in italiano; l'indice si trova in",
        ["Home","Guide al project management","Guide Agile","Guide Scrum","Guide Kanban","Guide per settore","Modelli gratuiti","Recensioni di software di project management","Confronti tra strumenti","Alternative agli strumenti","Recensioni degli studenti","Chi siamo e informative"]),
 "ja": ("日本語", "Neural Project Institute（neuralprojectinstitute.com）は、プロジェクト管理を学ぶための独立系教育サイトです。プロジェクト管理、アジャイル、スクラム、かんばんに関する無料の詳しいガイド、Excel・Google スプレッドシート・PDF 用の無料テンプレート、プロジェクト管理ソフトウェアの独立したレビューと比較、そして PMAI（Project Management Artificial Intelligence）認定を提供しています。お問い合わせ：support@neuralprojectinstitute.com。",
        "このファイルは日本語ページの一覧です。英語の原文は次の場所にあります：", "日本語ページの全文は次のファイルにあります：", "このファイルには日本語ページの全文が含まれています。一覧は次のファイルにあります：",
        ["ホーム","プロジェクト管理ガイド","アジャイルガイド","スクラムガイド","かんばんガイド","業界別ガイド","無料テンプレート","プロジェクト管理ソフトウェアのレビュー","ツール比較","ツールの代替","受講者のレビュー","当サイトについて・ポリシー"]),
 "ru": ("Русский", "Neural Project Institute (neuralprojectinstitute.com) — независимый образовательный сайт по управлению проектами. Здесь публикуются бесплатные подробные руководства по управлению проектами, Agile, Scrum и Kanban, бесплатные шаблоны для Excel, Google Таблиц и PDF, независимые обзоры и сравнения программ для управления проектами, а также сертификация PMAI (Project Management Artificial Intelligence). Контакты: support@neuralprojectinstitute.com.",
        "В этом файле перечислены страницы на русском языке. Оригинал на английском:", "Полный текст всех страниц на русском языке находится в", "Этот файл содержит полный текст всех страниц на русском языке; список страниц находится в",
        ["Главная","Руководства по управлению проектами","Руководства по Agile","Руководства по Scrum","Руководства по Kanban","Отраслевые руководства","Бесплатные шаблоны","Обзоры программ для управления проектами","Сравнения инструментов","Альтернативы инструментам","Отзывы слушателей","О нас и правила"]),
 "zh": ("中文", "Neural Project Institute（neuralprojectinstitute.com）是一个独立的项目管理教育网站，免费提供项目管理、敏捷、Scrum 和看板的详细指南，适用于 Excel、Google 表格和 PDF 的免费模板，项目管理软件的独立评测与对比，以及 PMAI（Project Management Artificial Intelligence）认证。联系邮箱：support@neuralprojectinstitute.com。",
        "本文件列出了中文页面。英文原版位于", "所有中文页面的全文位于", "本文件包含所有中文页面的全文；页面索引位于",
        ["首页","项目管理指南","敏捷指南","Scrum 指南","看板指南","行业指南","免费模板","项目管理软件评测","工具对比","工具替代方案","学员评价","关于我们与政策"]),
}


def en_of(s):
    m = re.search(r'hreflang="en" href="https://neuralprojectinstitute\.com([^"]+)"', s)
    return m.group(1) if m else None


def main_lang(lang):
    name, about, l_orig, l_full, l_idx, secnames = L10N[lang]
    names = dict(zip(ORDER, secnames))
    ps = sorted(pages(lang), key=lambda x: x[0])
    groups = {k: [] for k in ORDER}
    for u, s in ps:
        e = en_of(s)
        k = section(e) if e else ("Home" if u == f"/{lang}/" else "About and policies")
        t, d = meta(s)
        groups[k].append((u, t, d))
    head = f"# Neural Project Institute ({name})\n\n> {about}\n\n"
    idx = [head + f"{l_orig} {BASE}/llms.txt. {l_full} [{lang}/llms-full.txt]({BASE}/{lang}/llms-full.txt).\n"]
    full = [head + f"{l_idx} [{lang}/llms.txt]({BASE}/{lang}/llms.txt).\n"]
    byurl = dict(ps)
    for k in ORDER:
        if not groups[k]: continue
        idx.append(f"\n## {names[k]}\n")
        for u, t, d in groups[k]:
            idx.append(f"- [{t}]({BASE}{u})" + (f": {d}" if d else ""))
            full.append(f"\n\n---\n\n# {t}\n\nURL: {BASE}{u}\n" + (f"{d}\n" if d else "") + "\n" + body(byurl[u]))
    open(f"{SITE}/{lang}/llms.txt", "w", encoding="utf-8").write("\n".join(idx) + "\n")
    open(f"{SITE}/{lang}/llms-full.txt", "w", encoding="utf-8").write("\n".join(full) + "\n")
    return len(ps)


def main():
    main_en()
    for lang in LANGS:
        print(lang, main_lang(lang), "pages")


if __name__ == "__main__":
    main()
