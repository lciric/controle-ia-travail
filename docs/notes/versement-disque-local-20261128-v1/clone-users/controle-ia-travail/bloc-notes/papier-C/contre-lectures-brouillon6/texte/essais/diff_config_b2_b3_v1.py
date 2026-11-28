"""Compare les configurations brouillon 2 et brouillon 3 chemin par chemin ; affiche seulement les chemins
ajoutés, retirés ou changés (jamais les valeurs)."""
import json, sys
a = json.load(open(sys.argv[1], encoding="utf-8")); b = json.load(open(sys.argv[2], encoding="utf-8"))
def plat(x, p="$"):
    if isinstance(x, dict):
        out = {}
        for k, v in x.items(): out.update(plat(v, f"{p}.{k}"))
        return out
    if isinstance(x, list) and x and all(isinstance(e, dict) for e in x):
        out = {}
        for i, v in enumerate(x): out.update(plat(v, f"{p}[{i}]"))
        return out
    return {p: json.dumps(x, ensure_ascii=False, sort_keys=True)}
fa, fb = plat(a), plat(b)
print("retirés :", sorted(set(fa) - set(fb)))
print("ajoutés :", sorted(set(fb) - set(fa)))
print("changés :", sorted(k for k in set(fa) & set(fb) if fa[k] != fb[k]))
for cle in ["vivier", "temoins_sham", "consignes", "fentes", "contenus_neutres", "insertion", "gardes_lexicales",
            "juges", "agent", "echelle", "raisonne", "graines"]:
    print(cle, "égal" if a.get(cle) == b.get(cle) else "DIFFÉRENT")
print("agent_bras sans décision égal :", {k: v for k, v in a["agent_bras"].items() if k != "decision_bras_usurpation"} == {k: v for k, v in b["agent_bras"].items() if k != "decision_bras_usurpation"})
print("longueurs égales :", all(a["controle_redaction"][k] == b["controle_redaction"][k] for k in a["controle_redaction"]))
