"""Comptes seulement : longueurs (caractères) des contextes de juge H.4, rapport caractères / jetons mesuré sur les
notations scellées. N'affiche aucun texte."""
import json, sys, statistics as st
R = sys.argv[1]
ep = json.load(open(f"{R}/diag/20261012-105125-t05-pilote-reel/episodes.json"))["resultat"]["fiches"]
tb = json.load(open(f"{R}/donnees/t05-pilote-v1/taches-pilote-60-v1.json"))
taches = tb["resultat"]["taches"] if "resultat" in tb else tb["taches"]
par_id = {t["identifiant"]: t for t in taches}
h3 = open(f"{R}/docs/sources/invites-2606.08892-v1/invites/H3.txt", encoding="utf-8").read().strip()
h4 = open(f"{R}/docs/sources/invites-2606.08892-v1/invites/H4.txt", encoding="utf-8").read().strip()
nots = json.load(open(f"{R}/diag/20261017-193648-t05-notations-reel/notations-8B-decisives.json"))["resultat"]["notations"]
ctx_tok = {n["cle"]: n["jetons_contexte"] for n in nots}
fiche = {f["episode"]: f for f in ep}
ratios, corps_len = [], []
for cle, tok in ctx_tok.items():
    _, e, p = cle.split("/", 1)[1].rsplit("/", 1)[0], cle.split("/", 1)[1].rsplit("/passe-", 1)[0], None
    f = fiche[e]
    t = par_id[f["tache"]]
    cl = t.get("classification")
    cl_len = (len("## Paper Classification (verified metadata)\n\n") + 150 + 2) if cl else 0
    corps = len("## Research Questions\n\n") + len(t["questions"].strip()) + 2 + cl_len + len("## Proposals\n\n") + len(f["bilan"]["ensemble"].strip()) + 1
    corps_len.append(corps)
    total = len(h3) + len(h4) + 2 + corps
    ratios.append(total / tok)
print("len H3", len(h3), "len H4", len(h4))
print("corps : min/med/max", min(corps_len), st.median(corps_len), max(corps_len))
print("caractères par jeton (contexte H.4) : min/med/max", round(min(ratios),3), round(st.median(ratios),3), round(max(ratios),3))
