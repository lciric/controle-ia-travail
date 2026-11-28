"""Affiche les champs de règles changés de la configuration brouillon 4 (statut, stabilite_rang, constat_nu.pilote,
constat_nu.gardes, etape2.loi_nette.lecture_rho_sur_r), masqués s'ils recoupent sur 12 caractères un texte sensible
(vivier, témoins, consignes, fentes, insertion, contenus neutres, paragraphes de bras, textes du constat nu) — v1.
Usage : python3 -B -I voir_regles_b4_v1.py B4"""
import sys, json
c = json.load(open(sys.argv[1], encoding="utf-8"))
def chaines(o):
    if isinstance(o, dict):
        for v in o.values(): yield from chaines(v)
    elif isinstance(o, list):
        for v in o: yield from chaines(v)
    elif isinstance(o, str):
        yield o
sens = []
for k in ("vivier", "temoins_sham", "consignes", "fentes", "insertion", "contenus_neutres", "agent_bras"):
    sens += list(chaines(c[k]))
cn = c["constat_nu"]
for k, v in cn.items():
    if k not in ("pilote", "gardes", "decision", "statut", "lecture", "repli_si_refus"):
        sens += [s for s in chaines(v) if len(s) >= 12 and ("{" in s or k.startswith("insertion") or k.startswith("texte"))]
grams = set()
for s in sens:
    for i in range(len(s) - 11):
        grams.add(s[i:i+12])
def montrer(nom, v):
    s = json.dumps(v, ensure_ascii=False)
    hit = any(s[i:i+12] in grams for i in range(len(s) - 11))
    print(f"## {nom} : " + ("[MASQUÉ : recoupe un texte sensible]" if hit else s))
print("clés de constat_nu :", list(cn))
print("clés de stabilite_rang :", list(c["stabilite_rang"]))
montrer("statut", c["statut"])
for k, v in c["stabilite_rang"].items():
    montrer("stabilite_rang." + k, v)
for k in ("pilote", "gardes", "decision"):
    if k in cn: montrer("constat_nu." + k, cn[k])
montrer("etape2.loi_nette.lecture_rho_sur_r", c["etape2"]["loi_nette"]["lecture_rho_sur_r"])
montrer("agent_bras.decision_bras_usurpation", c["agent_bras"].get("decision_bras_usurpation"))
