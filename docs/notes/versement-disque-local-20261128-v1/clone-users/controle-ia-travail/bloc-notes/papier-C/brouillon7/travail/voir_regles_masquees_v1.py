"""Affiche des champs de règles nommés de la configuration, masqués s'ils recoupent un texte sensible — v1.
Rédacteur neuf du brouillon 7. Un champ est affiché seulement s'il ne partage aucune sous-chaîne de 12 caractères avec
le vivier, les témoins, les fentes, les consignes, les contenus neutres, les paragraphes de bras ou le gabarit du constat
nu (remplis ou non). Usage : python3 -B -I voir_regles_masquees_v1.py CONFIG chemin.pointe ..."""
import json, sys
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
def remplir(t, f):
    for k, v in f.items():
        t = t.replace("{" + k + "}", v)
    return t
sens = []
def tous_textes(o):
    if isinstance(o, dict):
        for v in o.values(): yield from tous_textes(v)
    elif isinstance(o, list):
        for v in o: yield from tous_textes(v)
    elif isinstance(o, str):
        yield o
for cle in ("vivier", "temoins_sham", "fentes", "consignes", "contenus_neutres"):
    sens += list(tous_textes(cfg[cle]))
for k in ("plaidoyer", "usurpation", "place"):
    sens.append(cfg["agent_bras"][k])
sens.append(cfg["constat_nu"]["gabarit"])
for c in ("A", "B"):
    f = cfg["fentes"][c]
    sens += [remplir(t, f) for t in tous_textes(cfg["vivier"])] + [remplir(t, f) for t in cfg["temoins_sham"]]
    sens.append(remplir(cfg["constat_nu"]["gabarit"], f))
grams = set()
for s in sens:
    for i in range(max(0, len(s) - 11)):
        grams.add(s[i:i + 12])
for chemin in sys.argv[2:]:
    o = cfg
    for p in chemin.split("."):
        o = o[p]
    t = json.dumps(o, ensure_ascii=False)
    touche = any(t[i:i + 12] in grams for i in range(max(0, len(t) - 11)))
    print(chemin, ":", "[masqué : recoupe un texte sensible]" if touche else t)
