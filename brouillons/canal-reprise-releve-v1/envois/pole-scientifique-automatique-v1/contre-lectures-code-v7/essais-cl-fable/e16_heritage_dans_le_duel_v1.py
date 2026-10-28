"""E16 : le bras de référence « mécanique » du duel des proposeurs (fonctions `preparer_monde` et `course_reference` du
script du duel, version lue : instantané v9), trois générations sur des mondes de la grammaire v2. Le chercheur mécanique
est déterministe sur la partie de développement : il repropose les mêmes lois à chaque génération ; une loi éliminée
revient comme redite et hérite de son log W, éprouvée sur les mêmes lignes d'épreuve (pas de tranches). On compte, dans
les journaux, les gardes « héritage » et les promotions qui n'existent que par l'héritage.

Usage : python -I -B e16_heritage_dans_le_duel_v1.py COPIE_DU_CODE DOSSIER_NEUF GRAINE1,GRAINE2,...
"""
import json
import os
import sys

COPIE, DOSSIER, GRAINES = sys.argv[1], sys.argv[2], [int(g) for g in sys.argv[3].split(",")]
sys.path.insert(0, COPIE)
sys.path.insert(0, os.path.join(COPIE, "demonstrations"))
sys.path.insert(0, os.path.join(COPIE, "exemples"))
os.makedirs(DOSSIER, exist_ok=False)
import duel_proposeurs_v7 as duel  # noqa: E402

bilan = {}
for graine in GRAINES:
    monde_dossier = os.path.join(DOSSIER, f"monde-{graine}")
    chemin_banque, chemin_pop, chemin_tem, verite = duel.preparer_monde(monde_dossier, graine)
    course = os.path.join(DOSSIER, f"course-mecanique-{graine}")
    duel.course_reference("mecanique", graine, course, chemin_banque, chemin_pop, chemin_tem)
    gardes_heritage, promues_par_heritage, promues = 0, [], []
    for nom in sorted(os.listdir(os.path.join(course, "journal"))):
        if not nom.endswith(".json"):
            continue
        with open(os.path.join(course, "journal", nom), encoding="utf-8") as f:
            j = json.load(f)
        gardes_heritage += sum(1 for g in j["gardes_de_redite"].values() if "héritage" in (g.get("motif") or ""))
        for ident, issue in j["fiches"].items():
            pari = issue.get("pari") or {}
            if issue.get("verdict_final") == "survit" and not issue.get("temoin"):
                promues.append(ident)
                h = pari.get("heritage")
                if h and not h.get("promue_sans_heritage"):
                    promues_par_heritage.append({"fiche": ident, "generation": j["generation"], "cumul": round(h["cumul"], 3),
                                                 "log_w_max": round(pari["log_richesse_max"], 3),
                                                 "moniteur": None})
    bilan[graine] = {"gardes_heritage": gardes_heritage, "promues_reelles": promues,
                     "promues_par_le_seul_heritage": promues_par_heritage, "lecture_duel": duel.lire_course(course, verite)}
with open(os.path.join(DOSSIER, "e16-resultat-v1.json"), "w", encoding="utf-8") as f:
    json.dump(bilan, f, ensure_ascii=False, indent=1)
print(json.dumps(bilan, ensure_ascii=False, indent=1))
