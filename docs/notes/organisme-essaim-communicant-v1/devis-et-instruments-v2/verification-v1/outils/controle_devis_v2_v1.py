"""Contrôles du devis v2 : rapports pire v2 / pire v1, décomposition du pire haut 10/50 contre P3 du relecteur, lignes de
provenance. Usage : controle_devis_v2_v1.py CALCUL_V1.json CALCUL_V2.json"""
import json, sys

v1 = json.load(open(sys.argv[1], encoding="utf-8"))
v2 = json.load(open(sys.argv[2], encoding="utf-8"))
rap = []
for r in ("bas", "attendu", "haut"):
    for e in sorted(v2["resume_usd"][r]):
        x = v2["resume_usd"][r][e]["pire"] / v1["resume_usd"][r][e]["pire"]
        rap.append(x)
        print(f"rapport pire v2/v1 {r:8s} {e:10s} {x:.3f}")
print("rapport min / max :", round(min(rap), 3), round(max(rap), 3))
d = v2["devis_par_espece"]["astra"]["haut"]["par_ligne"]
somme = {}
for l, v in d.items():
    for k, u in v["pire_postes"].items():
        somme[k] = somme.get(k, 0) + u
print("pire haut astra, postes :", {k: round(u, 2) for k, u in somme.items()})
s = sum(somme.values())
print("somme sans marges :", round(s, 2), "| x1,1 x1,05 :", round(s * 1.1 * 1.05, 2), "| sortie :", v2["resume_usd"]["haut"]["astra"]["pire"])
print("P3 relecteur (236 448) = tests + proposeurs + aiguilleur cartes + messages au tarif ; écart dû à :",
      "messages au plafond", round(somme["messages"] - 1440 * (3000 * 10 + 400 * 50) / 1e6, 2),
      "| aiguillage des objets", round(somme["aiguilleur_objets_de_controle"], 2), "| marges x1,155")
for k, v in v2["provenance_des_nombres"].items():
    print("provenance", k, {kk: (vv if kk != "sha256" else vv[:8]) for kk, vv in v.items() if kk in ("piece", "sha256", "ligne", "valeur")})
print("supposes :", json.dumps(v2["supposes"], ensure_ascii=False))
