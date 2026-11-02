"""Champs de lecture calculés par le code (sortie scellée, clé « lecture »), imprimés tels quels."""
import json
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
L = R["lecture"]
print("issues", json.dumps(L["issues"], ensure_ascii=False))
for w, m in L["mondes"].items():
    print("=" * 30, w)
    for k, v in m.items():
        if k == "taux":
            for kk, vv in v.items():
                print("  taux", kk, json.dumps(vv))
        else:
            print(" ", k, json.dumps(v, ensure_ascii=False))
print("audit_A2 :", len(R["audit_A2"]))
for r in R["audit_A2"]:
    print("  ", json.dumps(r, ensure_ascii=False))
