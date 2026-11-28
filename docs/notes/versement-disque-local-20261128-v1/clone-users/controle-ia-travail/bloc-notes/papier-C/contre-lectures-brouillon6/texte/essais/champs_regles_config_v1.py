"""Affiche les seuls champs de règles de la configuration (jamais vivier, témoins, consignes, fentes, contenus,
paragraphes de bras, gabarit du constat nu, listes des gardes). Masque tout champ qui contiendrait un morceau
de 12 caractères ou plus d'un texte de formulation, de témoin, de fente ou de consigne."""
import json, sys
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
sensibles = []
for fam in cfg["vivier"].values():
    sensibles += fam
sensibles += cfg["temoins_sham"]
for c in ("A", "B"):
    sensibles += [v for v in cfg["fentes"][c].values()]
def chaines(x):
    if isinstance(x, str): yield x
    elif isinstance(x, list):
        for e in x: yield from chaines(e)
    elif isinstance(x, dict):
        for e in x.values(): yield from chaines(e)
sensibles += list(chaines(cfg["consignes"])) + list(chaines(cfg["contenus_neutres"]))
sensibles += [cfg["agent_bras"]["plaidoyer"], cfg["agent_bras"]["usurpation"], cfg["constat_nu"]["gabarit"]]
morceaux = set()
for s in sensibles:
    for i in range(0, max(1, len(s) - 11)):
        m = s[i:i+12]
        if len(m) == 12: morceaux.add(m)
def sur(s):
    return not any(s[i:i+12] in morceaux for i in range(0, max(1, len(s) - 11)))
champs = ["statut", ("stabilite_rang",), ("agent_bras", "decision_bras_usurpation"), ("agent_bras", "place"),
          ("constat_nu", "decision"), ("constat_nu", "place"), ("constat_nu", "temoin"), ("constat_nu", "lectures"),
          ("constat_nu", "verdict"), ("constat_nu", "pilote"), ("constat_nu", "gardes"), ("constat_nu", "temoin_indice"),
          ("graines", "cles"), ("derivation", "demi_largeur_lambda"), ("partage_taches", "tirage_etape2"),
          ("partage_taches", "tirage_raisonne"), ("partage_taches", "cle"), ("etape2",), ("regle_temoins",),
          ("gardes_lexicales", "regle"), ("pilote", "borne_lancement"), "version"]
def get(chemin):
    x = cfg
    for k in ([chemin] if isinstance(chemin, str) else chemin): x = x[k]
    return x
def montre(chemin, x):
    if isinstance(x, dict):
        for k, v in x.items(): montre(f"{chemin}.{k}", v)
    elif isinstance(x, list):
        for i, v in enumerate(x): montre(f"{chemin}[{i}]", v)
    elif isinstance(x, str):
        print(f"{chemin} = {x if sur(x) else '[MASQUÉ : recoupe un texte sensible]'}")
    else:
        print(f"{chemin} = {x!r}")
for c in champs:
    nom = c if isinstance(c, str) else ".".join(c)
    montre("$." + nom, get(c))
