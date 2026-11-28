"""Affiche les champs de règles changés de la configuration brouillon 4, chaque caractère couvert par un 12-gramme
commun avec un texte sensible (vivier, témoins, consignes, fentes, insertion, contenus neutres, paragraphes de bras,
gabarit et fentes du constat nu) remplacé par « ▒ » — v2 (la v1 masquait le champ entier, et comptait des champs de
règles comme sensibles). Usage : python3 -B -I voir_regles_b4_v2.py B4"""
import sys, json
c = json.load(open(sys.argv[1], encoding="utf-8"))
def chaines(o):
    if isinstance(o, dict):
        for v in o.values(): yield from chaines(v)
    elif isinstance(o, list):
        for v in o: yield from chaines(v)
    elif isinstance(o, str): yield o
sens = []
for k in ("vivier", "temoins_sham", "consignes", "fentes", "insertion", "contenus_neutres"):
    sens += list(chaines(c[k]))
for k, v in c["agent_bras"].items():
    if not k.startswith("decision"):
        sens += list(chaines(v))
for k in ("gabarit", "fentes"):
    sens += list(chaines(c["constat_nu"][k]))
g = set()
for s in sens:
    for i in range(len(s) - 11): g.add(s[i:i+12])
def masque(s):
    m = [False] * len(s)
    for i in range(len(s) - 11):
        if s[i:i+12] in g:
            for j in range(i, i + 12): m[j] = True
    return "".join("▒" if m[i] else ch for i, ch in enumerate(s)), sum(m)
champs = {"statut": c["statut"], **{"stabilite_rang." + k: v for k, v in c["stabilite_rang"].items()},
          **{"constat_nu." + k: c["constat_nu"][k] for k in ("pilote", "gardes", "decision", "lectures", "verdict", "temoin_indice", "place")},
          "agent_bras.decision_bras_usurpation": c["agent_bras"].get("decision_bras_usurpation"),
          "etape2.loi_nette.lecture_rho_sur_r": c["etape2"]["loi_nette"]["lecture_rho_sur_r"]}
print("clés de agent_bras :", list(c["agent_bras"]))
for n, v in champs.items():
    s, k = masque(json.dumps(v, ensure_ascii=False))
    print(f"## {n} ({k} caractères masqués) : {s}")
