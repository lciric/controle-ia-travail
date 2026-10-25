"""Devis attendu (non opposable) du second pilote : une course = organisme v5.1 de Gemini, deux générations, question à
g001. Entrées : le journal des appels de g000 du premier pilote (longueurs d'entrée réelles des appels de tâche, Fable),
les prix du collisionneur lus par le noyau (`appels.modele_de`), la règle de réservation du noyau
(`cv.cout_pire_cas` : caractères / 3 jetons d'entrée + max_tokens en sortie). La sortie par appel est inconnue (réflexion
comprise) : le devis est donné pour plusieurs hypothèses ; aucune n'est une prédiction.

Usage : python -I devis_attendu_pilote2_v1.py RACINE_CODE JOURNAL_G000 SORTIE.json
"""
import json, statistics, sys, pathlib

racine, journal, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
sys.path.insert(0, str(racine))
from essaim_m3.noyau import appels  # noqa: E402

PRIX = {e: list(appels.modele_de(e)["prix"]) for e in ("CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5", "GEMINI_ARGON")}
lignes = [json.loads(l) for l in journal.read_text(encoding="utf-8").splitlines() if l.strip()]
taches = [l for l in lignes if l.get("role") == "monoculture_analytique" and (l.get("usage") or {}).get("entree", 0) > 0]
entree_moy = statistics.mean(l["usage"]["entree"] for l in taches)
entree_med = statistics.median(l["usage"]["entree"] for l in taches)

PLAFOND_GEN, PLAFOND_COURSE, MAX_TOK = 30.0, 60.0, 8192
N_TACHES_G0 = 1 + 1 + 2 + 120   # formulation de moisson + induction + 2 vérifications + 120 tâches (Fable)
N_TACHES_G1 = 1 + 2 + 120       # induction + 2 vérifications + 120 tâches (pas de moisson des tâches quand la question est posée)
# question à g001 : formulation de moisson (Fable) + 5 castes (Fable, Opus, Argon, Fable, arbitre Opus) au plus,
# préfixe documentaire ≈ 3 000 jetons d'entrée (8 notices + 3 extraits, bornes du code de l'organisme)
QUESTION = [("CLAUDE_FABLE_5_1", 1500), ("CLAUDE_FABLE_5_1", 4500), ("CLAUDE_OPUS_5_5", 4500), ("GEMINI_ARGON", 4500),
            ("CLAUDE_FABLE_5_1", 4500), ("CLAUDE_OPUS_5_5", 9000)]

def cout(espece, e, s):
    p = PRIX[espece]
    return e / 1e6 * p[0] + s / 1e6 * p[1]

hypotheses = []
for s in (500, 1000, 2000, 3000, 4000, 6000, 8192):
    tache = cout("CLAUDE_FABLE_5_1", entree_moy, s)
    g0 = N_TACHES_G0 * tache
    g1_taches = N_TACHES_G1 * tache
    q = sum(cout(esp, e, min(s * 2, MAX_TOK)) for esp, e in QUESTION)  # la question écrit plus long qu'une tâche : 2 s, borné
    hypotheses.append({"sortie_par_appel_de_tache": s, "usd_par_appel_de_tache": round(tache, 4),
                       "usd_g000": round(g0, 2), "usd_g001_taches": round(g1_taches, 2), "usd_question": round(q, 2),
                       "usd_course": round(g0 + g1_taches + q, 2),
                       "plafond_generation_atteint_g000": g0 > PLAFOND_GEN,
                       "question_servie_sous_le_plafond_g001": None})
# seuil : la question part après les 123 appels de tâche de g001 ; elle exige que dépense + en vol + pire cas du
# premier appel de la question reste sous 30 USD ; pire cas d'un appel Fable à 8 192 jetons (entrée ≈ 1 500 jetons) :
pire_fable = 1500 / 1e6 * PRIX["CLAUDE_FABLE_5_1"][0] + MAX_TOK / 1e6 * PRIX["CLAUDE_FABLE_5_1"][1]
reserve_question = sum(cout(esp, e, MAX_TOK) for esp, e in QUESTION)  # toute la question au pire cas
for en_vol in (1, 8):
    # dépense des tâches de g001 qui laisse passer toute la question au pire cas, avec `en_vol` − 1 appels de tâche encore en vol
    marge = PLAFOND_GEN - reserve_question - (en_vol - 1) * pire_fable
    s_max = (marge / N_TACHES_G1 - entree_moy / 1e6 * PRIX["CLAUDE_FABLE_5_1"][0]) / (PRIX["CLAUDE_FABLE_5_1"][1] / 1e6)
    for h in hypotheses:
        h.setdefault("question_entiere_au_pire_cas", {})[f"{en_vol}_en_vol"] = h["sortie_par_appel_de_tache"] <= s_max
    hypotheses_seuil = {"en_vol": en_vol, "sortie_max_par_appel_de_tache": int(s_max)}
    print(json.dumps(hypotheses_seuil))
    globals().setdefault("seuils", []).append(hypotheses_seuil)
for h in hypotheses:
    h.pop("question_servie_sous_le_plafond_g001", None)

resultat = {"version": "devis-attendu-pilote2-v1", "non_opposable": True,
            "journal_source": str(journal.name), "n_appels_de_tache_lus": len(taches),
            "entree_moyenne_jetons": round(entree_moy), "entree_mediane_jetons": round(entree_med),
            "prix_usd_par_million": PRIX, "plafond_generation_usd": PLAFOND_GEN, "plafond_course_usd": PLAFOND_COURSE,
            "max_tokens_appel": MAX_TOK, "appels_g000": N_TACHES_G0, "appels_g001_taches": N_TACHES_G1,
            "question": [{"espece": e, "entree_jetons": n} for e, n in QUESTION],
            "pire_cas_appel_fable_8192_usd": round(pire_fable, 4), "question_au_pire_cas_usd": round(reserve_question, 2),
            "seuils_question": seuils, "hypotheses": hypotheses,
            "pire_cas_deux_courses_usd": 2 * PLAFOND_COURSE}
sortie.write_text(json.dumps(resultat, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: resultat[k] for k in ("entree_moyenne_jetons", "question_au_pire_cas_usd", "seuils_question")}, ensure_ascii=False))
for h in hypotheses: print(h["sortie_par_appel_de_tache"], h["usd_course"], h["usd_g000"], h["usd_g001_taches"], h["usd_question"], h["question_entiere_au_pire_cas"])
