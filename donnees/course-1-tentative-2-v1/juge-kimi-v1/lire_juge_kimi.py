"""Lecture complémentaire : notes de Kimi (consigne d'Argon, anonymisation d'Argon) lues par les fonctions de la v52, puis
comparées à Opus 5.5 et Argon. Usage : python3 lire_juge_kimi.py SORTIE_COMMANDE.jsonl SORTIE.json"""
import json, statistics, sys
sys.path.insert(0, "/root/ideation-v1/orchestrateur-v52/arbre")
from pole.outils import extraire_bloc_json
from pole.ideation_v2 import valider_notes, CRITERES, PORTE_ELIGIBILITE
R = "/root/ideation-v1/sortie-juges-course-v2/"
cle = json.load(open(R + "noyau/cles-anonymisation-par-juge.json"))["argon-juge"]
derniere = open(sys.argv[1], encoding="utf-8").read().strip().splitlines()[-1]
texte = json.loads(derniere)["texte"]
notes, doubles = valider_notes(extraire_bloc_json(texte, "notes"), list(cle.keys()))
kimi = {cle[i]: n for i, n in notes.items()}
anciens = json.load(open(R + "notes-par-juge.json"))
temoins = {t["fiche"]["identifiant_auteur"] if "identifiant_auteur" in t["fiche"] else None: t
           for t in json.load(open("/root/ideation-v1/temoins/temoins-ideation-tiers-v1.json"))["temoins"]}
tot = lambda n: sum(n["criteres"][k] for k in CRITERES)
juges = {"kimi-juge": kimi, **anciens}
res = {"doublons_kimi": [[cle[a] for a in d] for d in doubles], "moyennes_par_auteur": {}, "temoins": {}, "fiches": {}}
for j, nj in juges.items():
    par = {}
    for ident, n in nj.items():
        a = ident.split("-")[0]
        par.setdefault(a, []).append(tot(n))
    res["moyennes_par_auteur"][j] = {a: round(statistics.mean(v), 3) for a, v in par.items()}
for ident in kimi:
    if ident.startswith("temoin"):
        res["temoins"][ident] = {j: (tot(juges[j][ident]), max(juges[j][ident]["criteres"]["avantage"], juges[j][ident]["criteres"]["originalite"]) >= PORTE_ELIGIBILITE) for j in juges if ident in juges[j]}
    else:
        res["fiches"][ident] = {j: tot(juges[j][ident]) for j in juges}
json.dump(res, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: res[k] for k in ("moyennes_par_auteur", "temoins", "doublons_kimi")}, ensure_ascii=False))
