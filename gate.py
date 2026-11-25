"""Publication gate (framework §34-35): only pages whose independent review says PUBLISH, score >= 90 and all gates true may go live.
Usage: python3 gate.py <rw name> [...]   exits 1 if any page fails."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
ok = True
for n in sys.argv[1:]:
    p = os.path.join(HERE, "briefs", n + "-review.json")
    try:
        r = json.load(open(p))
    except Exception as e:
        print(f"BLOCKED {n}: no valid review ({e.__class__.__name__})"); ok = False; continue
    total = r.get("scores", {}).get("total", 0)
    bad = [k for k, v in r.get("gates", {}).items() if v is not True]
    if r.get("status") != "PUBLISH" or not r.get("publication_eligible") or total < 90 or bad or not r.get("gates"):
        print(f"BLOCKED {n}: status={r.get('status')} score={total} failed_gates={bad}"); ok = False
    else:
        print(f"PASS {n}: score {total}")
sys.exit(0 if ok else 1)
