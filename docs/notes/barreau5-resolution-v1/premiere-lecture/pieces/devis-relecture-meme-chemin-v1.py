"""Arithmetique du brouillon de devis de la relecture des quatre cases par un meme chemin de calcul (brouillon 1).

Aucune donnee du programme n'est ouverte. Sources des nombres (recopies, cites dans le devis) :
- debit : 0,45 s par passe d'episode ; prix A100 SXM4 80 Go : 1,0889 a 1,30 USD de l'heure, pire 1,40 ; stockage au plus
  0,08 USD de l'heure ; reseau au plus 0,05 USD par Go (prereg/validite-adaptateur-v1.md, « Calcul et depense » ;
  brouillons/T0.7-etape-B-bis-v1/devis-etape-b-bis-v3.md) ;
- postes de mise en place, d'essais, de garde et de poussee : ceux du devis scelle de la relecture a texte constant
  (prereg/validite-adaptateur-v1.md, lignes « R : ... ») ;
- volume des activations : sous-ensemble pousse par la course de confirmation, 576 actions, couche 15, par jeton,
  1 058 424 128 octets (note 04 du socle).
"""
import json
import sys

DEBIT_S = 0.45
PRIX_BAS, PRIX_HAUT, PRIX_PIRE = 1.0889, 1.30, 1.40
STOCKAGE_H = 0.08
RESEAU_GO = 0.05
QUART_PIRE = 0.25 * (PRIX_PIRE + STOCKAGE_H)

# ---------------------------------------------------------------------------------------------------------------- series
BLOCS = {  # nom : (nombre de series, role)
    "A, quatre cases du saboteur (honnete sous le modele nu ; par dose : saboteur sous adaptateur, honnete sous adaptateur, saboteur sous modele nu)": 13,
    "B, quatre cases du temoin a la dose 1 (honnete sous temoin ; temoin sous temoin ; temoin sous modele nu)": 3,
    "C, temoin aux doses 0,5 ; 0,25 ; 0,75 sur les textes honnetes": 3,
    "D, consigne (temoin instruit ; saboteur instruit), etats d'origine": 2,
}
EPISODES = 64
n_series = sum(BLOCS.values())
passes_series = n_series * EPISODES
passes_divergence = EPISODES * (1 + 8)        # par episode honnete : modele nu, puis huit etats (saboteur et temoin, quatre doses)
passes = passes_series + passes_divergence

# ----------------------------------------------------------------------------------------------------------- activations
OCTETS_SOUS_ENSEMBLE, ACTIONS_SOUS_ENSEMBLE = 1_058_424_128, 576
go_par_action = OCTETS_SOUS_ENSEMBLE / ACTIONS_SOUS_ENSEMBLE / 1e9
go_par_serie = go_par_action * 640
vol = {"par_serie_Go": round(go_par_serie, 3)}
cumul = 0
for nom, n in BLOCS.items():
    cumul += n
    vol[f"cumul_jusqu_au_bloc_{nom[0]}_Go"] = round(cumul * go_par_serie, 1)
vol["vecteurs_moyens_par_action_trois_couches_demi_precision_Mo"] = round(n_series * 3 * 640 * 4096 * 2 / 1e6, 0)
vol["sous_ensemble_apparie_une_action_sur_dix_Go"] = round(n_series * go_par_serie / 10, 2)
vol["sous_ensemble_apparie_une_action_sur_cinq_Go"] = round(n_series * go_par_serie / 5, 2)
total_go = n_series * go_par_serie

# ------------------------------------------------------------------------------------------------------------------ postes
# (bas, haut) en heures de carte
postes = {
    "mise en place (image, modele, depot, donnees de la course de confirmation, sondes, directions, poids des jumelles)": (1.0, 1.0),
    "essais cibles sur l'instance (jouet, identite, chemin, garde de la moyenne)": (0.3, 0.3),
    "controles d'identite (deux adaptateurs)": (0.05, 0.05),
    f"relectures et mesure d'intensite ({passes} passes ; ecriture des activations de la couche 15)": (0.45, 0.80),
    "garde d'equivalence des series a l'etat d'origine": (0.05, 0.05),
    "notation (sondes, jumelles, 800 directions par sonde sur le bloc A ; avec et sans le champ du cout)": (0.15, 0.50),
    "ecriture des scores fermes, sceaux, poussee des scores": (0.10, 0.10),
}
depot = (0.15, 0.60)   # depot des activations par jeton (25 Go), en plus
h_bas = sum(v[0] for v in postes.values())
h_haut = sum(v[1] for v in postes.values())


def usd(h, prix, go_descente, go_envoi, prix_reseau, h_hors_marche=1.0):
    return h * prix + STOCKAGE_H * (h + h_hors_marche) + (go_descente + go_envoi) * prix_reseau


s = {
    "series": n_series, "passes_des_series": passes_series, "passes_de_la_divergence": passes_divergence, "passes": passes,
    "heure_de_passe_pure": round(passes * DEBIT_S / 3600, 3),
    "volumes": vol,
    "postes_heures": {k: list(v) for k, v in postes.items()},
    "depot_des_activations_heures": list(depot),
    "heures_sans_depot_des_activations": [round(h_bas, 2), round(h_haut, 2)],
    "heures_avec_depot_des_activations": [round(h_bas + depot[0], 2), round(h_haut + depot[1], 2)],
}
# attendu : descente 20 a 40 Go facturee de 0,4 a 1,0 USD (forme du devis scelle : « telechargement <= 1 »)
att_sans = (h_bas * PRIX_BAS + STOCKAGE_H * (h_bas + 1.0) + 0.4, h_haut * PRIX_HAUT + STOCKAGE_H * (h_haut + 1.0) + 1.0)
att_avec = ((h_bas + depot[0]) * PRIX_BAS + STOCKAGE_H * (h_bas + depot[0] + 1.0) + 0.4 + total_go * 0.004,
            (h_haut + depot[1]) * PRIX_HAUT + STOCKAGE_H * (h_haut + depot[1] + 1.0) + 1.0 + total_go * RESEAU_GO)
s["attendu_USD_sans_depot_des_activations_par_jeton"] = [round(x, 2) for x in att_sans]
s["attendu_USD_avec_depot_des_activations_par_jeton"] = [round(x, 2) for x in att_avec]
# pire cas : hote deux fois plus lent, prix pire, reseau au plus cher
h_pire = 2 * (h_haut + depot[1])
s["pire_cas_heures"] = round(h_pire, 2)
s["pire_cas_USD_tout_garde"] = round(h_pire * PRIX_PIRE + STOCKAGE_H * (h_pire + 1.0) + 40 * RESEAU_GO * 0.5 + total_go * RESEAU_GO, 2)
h_pire_sans = 2 * h_haut
s["pire_cas_USD_sans_depot_des_activations_par_jeton"] = round(h_pire_sans * PRIX_PIRE + STOCKAGE_H * (h_pire_sans + 1.0) + 1.0, 2)
# ce que la coupure de 8,5 USD garantit au pire cas : bloc A seul, scores pousses
part_A = BLOCS[next(iter(BLOCS))] * EPISODES / passes
h_A_pire = 2 * (1.0 + 0.3 + 0.05 + 0.80 * (13 * 64 + 5 * 64) / passes + 0.05 + 0.50 * 0.7 + 0.10)
s["pire_cas_bloc_A_seul_heures"] = round(h_A_pire, 2)
s["pire_cas_bloc_A_seul_USD"] = round(h_A_pire * PRIX_PIRE + STOCKAGE_H * (h_A_pire + 1.0) + 1.0, 2)
s["quart_d_heure_au_prix_pire_USD"] = round(QUART_PIRE, 2)
s["coupure_USD"] = 8.5
s["marge_sous_la_coupure_au_pire_cas_bloc_A_USD"] = round(8.5 - QUART_PIRE - s["pire_cas_bloc_A_seul_USD"], 2)
# cout mensuel d'un volume loue pour 25 Go (ordre de grandeur, a verifier au devis final)
s["volume_loue_ordre_de_grandeur_EUR_par_mois_a_0.05_EUR_par_Go"] = round(total_go * 0.05, 2)
s["fichiers_de_moins_de_2_Go_pour_tout_garder"] = int(-(-total_go // 1.9))

texte = json.dumps(s, indent=1, ensure_ascii=False)
print(texte)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write(texte + "\n")
