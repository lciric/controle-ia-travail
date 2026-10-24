"""Devis de la v6 recalculé avec `cout_pire_cas` du collisionneur (213b52ef…) et la consigne d'amorçage du noyau
(`contrat.prompt_amorcage`, mission `MISSION-v1.md`, budget de la v6). Les six exemples d'amorçage sont les six
premières tâches de `train` de la banque scellée (absente ici) : on borne leur longueur par le maximum du résumé
(20 071 caractères) ; la longueur réelle est à mesurer sur la banque."""
import json, pathlib, sys
sys.path.insert(0, "/srv/copie/essaim-m3-refonte-v1")
from essaim_m3.noyau import contrat, taches
from essaim_m3.noyau.appels import cv
mission = pathlib.Path("/srv/copie/essaim-m3-refonte-v1/MISSION-v1.md").read_text(encoding="utf-8")
budget = {"appels_max": 160, "usd_max": 37, "temps_max_s": 1800}
fixe = len(contrat.prompt_amorcage(mission, taches.ETIQUETTES, budget, []))
par_exemple_hors_texte = len(contrat.prompt_amorcage(mission, taches.ETIQUETTES, budget, [{"id": "cd-lot1-L1-01-H", "famille": "controle-delegation", "verite": "honnete", "texte": ""}])) - fixe
M = cv.MODELES
def pire(lettre, caracteres):
    m = M[lettre]
    return cv.cout_pire_cas(m["prix"], caracteres, m["max"])
cas = {"v6_implicite_30000": 30000, "sans_exemple": fixe, "exemples_max_6x20071": fixe + 6 * (20071 + par_exemple_hors_texte)}
amorcage = {k: {l: round(pire(l, c), 3) for l in "ABC"} | {"total_3_especes": round(sum(pire(l, c) for l in "ABC"), 3), "caracteres": c} for k, c in cas.items()}
# lignes du devis de la v6
conception = 5 * 8 * 10; generations = 5 * 3 * 37; gelee = 5 * 3 * 37
defense_v6, defense_code = 15.1, 37.0
def une_graine(amorc, defense):
    return amorc + conception + generations + gelee + 12 * defense
rep = 3.3 + 2 * 2 * 10 + 2 * 37
r = {"caracteres_consigne_sans_exemple": fixe, "caracteres_par_exemple_hors_texte": par_exemple_hors_texte, "amorcage": amorcage,
     "lignes_v6": {"course_adaptative": round(6.3 + conception + generations, 1), "course_gelee": gelee, "confrontation": round(12 * defense_v6, 1),
                   "une_graine": round(une_graine(6.3, defense_v6), 1), "repetition": round(rep, 1), "total": round(2 * une_graine(6.3, defense_v6) + rep, 1)},
     "avec_le_budget_de_defense_du_code_37": {"confrontation": 12 * defense_code, "une_graine": round(une_graine(6.3, defense_code), 1),
                   "total": round(2 * une_graine(6.3, defense_code) + rep, 1)},
     "avec_amorcage_borne_haute": {"une_graine": round(une_graine(amorcage["exemples_max_6x20071"]["total_3_especes"], defense_code), 1),
                   "total": round(2 * une_graine(amorcage["exemples_max_6x20071"]["total_3_especes"], defense_code) + rep, 1)},
     "pire_cas_appel_160_sur_37_usd": round(37 / 160, 4), "pire_cas_appel_fable_texte_max": round(cv.cout_pire_cas(M["A"]["prix"], 20071 + 2000, 4096), 4),
     "moisson_recherches_max": {"une_graine": 5 * 8 * 30 + 5 * 3 * 30 + 5 * 3 * 30, "repetition": 2 * (2 + 1) * 30, "total": 2 * (5 * 8 * 30 + 5 * 3 * 30 + 5 * 3 * 30) + 2 * (2 + 1) * 30}}
print(json.dumps(r, ensure_ascii=False, indent=1))
pathlib.Path("/srv/sorties/calcul-devis.json").write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
