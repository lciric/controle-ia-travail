"""É5 — décompte des heures de carte et des dollars du brouillon (G1), contre ses propres plafonds (65 USD et 30 h ;
40 USD et 20 h en repli) et contre le plafond accordé de la campagne (6 331 USD, GO-2026-11-05-07).
Ancres, toutes prises au dépôt (aucun prix de mémoire) :
 A1 génération par l'agent 8B : 933 actions par heure de carte (course de dose-réponse, mesuré par e5c_debit_mesure_dose_reponse.py) ;
    42,1 s et 54,6 s par épisode de dix actions (devis du brouillon 6 de G1, l. 349 : pilote de T0.5 et P3) ;
 A2 notation d'un épisode par un juge 8B : 58,2 s (même ligne, R-205) ; moniteurs boîte noire : 1 à 4 « équivalents juge 8B » ;
 A3 carte A100 80 Go : 1,00 à 1,19 USD de l'heure (registres/depenses.md, l. 613 à 639) ;
 A4 formation d'adaptateurs : plafond de 200 USD pour 39 adaptateurs (GO-2026-11-19-86), soit 5,1 USD par adaptateur au plafond.
Suppositions, déclarées : un juge de 27 milliards coûte 27,2 / 8,03 = 3,39 fois un juge de 8 milliards à service égal ;
 une action de code coûte autant qu'une action de proposition (222 jetons : favorable) ; maître des adaptateurs saboteurs :
 512 épisodes acceptés par adaptateur (64 tâches × 8, non écrit au brouillon), taux d'acceptation du rejet à trois niveaux."""
import json

PRIX = {"bas": 1.00, "central": 1.12, "haut": 1.19}
RATIO_27_SUR_8 = 27.2 / 8.03

def plan(archi):
    ev = 5 * 200 * 4                                   # épisodes d'évaluation, cinq conditions
    cal = 399 if archi == "amont" else 0
    fit = 64 * 2 * 2 if archi == "amont" else 0
    return {"episodes_evaluation": ev, "episodes_calibrage": cal, "episodes_ajustement": fit, "episodes": ev + cal + fit,
            "actions": (ev + cal + fit) * 10}

def decompte(archi, niveau):
    p = plan(archi)
    s_gen = {"bas": 36000 / 933.1, "central": 42.1, "haut": 54.6}[niveau]          # secondes par épisode
    acc = {"bas": 0.20, "central": 0.10, "haut": 0.05}[niveau]                      # acceptation du rejet (saboteurs)
    acc_hon = {"bas": 0.8, "central": 0.6, "haut": 0.4}[niveau]                     # acceptation (jumeau, témoin léger : tests publics tenus)
    juge_service = {"bas": 0.1, "central": 1.0, "haut": 1.0}[niveau]                # 0,1 : service par lots dix fois plus rapide que l'ancre
    trace_equiv = {"bas": 1, "central": 2, "haut": 4}[niveau]
    h = {}
    h["generation_des_actions_lues (agent 8B)"] = p["episodes"] * s_gen / 3600
    maitre = 2 * 512 / acc + 2 * 512 / acc_hon                                      # deux saboteurs, deux adaptateurs honnêtes
    h["episodes_du_maitre_pour_quatre_adaptateurs (rejet)"] = maitre * s_gen / 3600
    h["apprentissage_de_quatre_adaptateurs"] = 4 * 5.1 / PRIX["central"] * {"bas": 0.3, "central": 0.6, "haut": 1.0}[niveau]
    h["juge_27_milliards_par_action (analyse puis score)"] = p["episodes"] * 58.2 * RATIO_27_SUR_8 * juge_service / 3600
    h["TRACE-lite_sur_le_juge_27_milliards"] = p["episodes"] * 58.2 * RATIO_27_SUR_8 * juge_service * trace_equiv / 3600
    h["passe_de_recalcul_des_activations"] = p["episodes"] * s_gen / 3600 * 0.15
    h["quatrieme_mode_tenu_a_l_ecart (un adaptateur, 800 episodes, juges)"] = (512 / acc + 800) * s_gen / 3600 + 800 * 58.2 * RATIO_27_SUR_8 * juge_service * (1 + trace_equiv) / 3600
    total = sum(h.values())
    return {"plan": p, "heures": {k: round(v, 1) for k, v in h.items()}, "heures_total": round(total, 1),
            "usd_total": round(total * PRIX[niveau], 0), "episodes_du_maitre": round(maitre)}

sortie = {"plafonds_du_brouillon": {"amont": {"usd": 65, "heures": 30, "actions_annoncees": 46550}, "intra": {"usd": 40, "heures": 20, "actions_annoncees": 40000}},
          "plafond_accorde_campagne_usd": 6331, "texte_des_arbitrages": {"juge_27B": "~2 h GPU A100", "banque_727": "+12 min GPU", "montants_en_usd": "aucun"}}
for archi in ("amont", "intra"):
    sortie[archi] = {n: decompte(archi, n) for n in ("bas", "central", "haut")}
    pl = sortie["plafonds_du_brouillon"][archi]
    for n in ("bas", "central", "haut"):
        d = sortie[archi][n]
        d["rapport_au_plafond_heures_du_brouillon"] = round(d["heures_total"] / pl["heures"], 1)
        d["rapport_au_plafond_usd_du_brouillon"] = round(d["usd_total"] / pl["usd"], 1)
        d["part_du_plafond_accorde"] = round(d["usd_total"] / 6331, 3)
        d["generation_seule_depasse_le_plafond_d_heures"] = d["heures"]["generation_des_actions_lues (agent 8B)"] > pl["heures"]
sortie["actions_annoncees_recalculees"] = {"amont": plan("amont")["actions"], "intra": plan("intra")["actions"]}
sortie["non_comptes"] = ["construction de la banque de 727 tâches Python (énoncé, tests publics, oracle privé, solution canonique, mutants des trois modes), par une session à part : aucune ligne au brouillon ni au texte des arbitrages",
                         "conception et scellement du quatrième mode", "pilote de faisabilité de l'agent 8B", "disques et téléchargements (modèle de 27 milliards : 54 Go en bfloat16)"]
print(json.dumps(sortie, indent=1, ensure_ascii=False))
