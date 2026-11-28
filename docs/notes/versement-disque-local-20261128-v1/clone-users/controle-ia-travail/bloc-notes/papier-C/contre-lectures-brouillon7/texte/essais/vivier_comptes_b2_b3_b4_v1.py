"""Vivier par comptes (familles, entrées, longueurs min/max) et empreintes courtes des champs figés des configurations
brouillons 4, 3 et 2 du papier C ; aucun texte affiché — v1. Usage : python3 -B -I vivier_comptes_b2_b3_b4_v1.py B4 B3 B2"""
import sys, json, hashlib
cs=[json.load(open(p,encoding='utf-8')) for p in sys.argv[1:]]
h=lambda v: hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()[:12]
c=cs[0]
v=c["vivier"]
print("vivier : type", type(v).__name__, "; familles", len(v) if hasattr(v,'__len__') else None)
if isinstance(v,dict):
    for k,x in v.items():
        n=len(x) if isinstance(x,(list,dict)) else None
        print(f"  {k}: {n} entrées ; longueurs (caractères) min/max {min(len(json.dumps(e,ensure_ascii=False)) for e in (x if isinstance(x,list) else x.values()))}/{max(len(json.dumps(e,ensure_ascii=False)) for e in (x if isinstance(x,list) else x.values()))}")
t=c["temoins_sham"]; print("témoins :", type(t).__name__, len(t))
for k in ("vivier","temoins_sham","regle_temoins","fentes","insertion","consignes","contenus_neutres","gardes_lexicales","controle_redaction","graines","juges","echelle","pilote","derivation","partage_taches","agent","raisonne","confidentialite"):
    print(f"{k:20s} b4 {h(cs[0][k])} b3 {h(cs[1][k])} b2 {h(cs[2][k]) if k in cs[2] else '—'}")
