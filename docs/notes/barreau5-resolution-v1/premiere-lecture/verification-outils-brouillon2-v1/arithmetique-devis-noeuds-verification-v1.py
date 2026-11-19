"""Verification de l'arithmetique du devis brouillon 2 et des noeuds v2 (barreau 5, premiere lecture), ecrite a neuf par le
verificateur (Claude Opus 5.5). Processeur seul ; aucune donnee du programme. Entrees : les nombres du devis brouillon 2
(prix, debit, postes, volumes), recopies a la main ; rien n'est importe d'un autre outil.
Usage : python3 -B arithmetique-devis-noeuds-verification-v1.py <sortie .json>
"""
import json
import sys

P_BAS, P_HAUT, P_PIRE = 1.0889, 1.30, 1.40         # USD de l'heure (devis, « Sources des nombres »)
STOCK, RESEAU_MAX, RESEAU_MIN = 0.08, 0.05, 0.004  # stockage USD/h ; reseau USD/Go (bas : 0,1 USD pour ~25 Go)
DESC_BAS, DESC_HAUT = 0.4, 1.0                     # descente du modele et des donnees, USD
POSTES_BAS = dict(mise_en_place=1.0, essais=0.3, identite=0.05, relectures=0.45, equivalence=0.05, notation=0.15, poussee=0.10)
POSTES_HAUT = dict(mise_en_place=1.0, essais=0.3, identite=0.05, relectures=0.80, equivalence=0.05, notation=0.50, poussee=0.10)
DEPOT_BAS, DEPOT_HAUT = 0.15, 0.60
GO_SERIE = 1_058_424_128 / 576 * 640 / 1e9         # Go par serie de 640 actions (note 04 du socle, recopie du devis)
PASSES_TOTAL = 1920

o = {}
hb, hh = sum(POSTES_BAS.values()), sum(POSTES_HAUT.values())
o["heures_sans_depot"] = [round(hb, 2), round(hh, 2)]
o["heures_avec_depot"] = [round(hb + DEPOT_BAS, 2), round(hh + DEPOT_HAUT, 2)]
o["attendu_sans_depot_USD"] = [round(hb * P_BAS + STOCK * (hb + 1) + DESC_BAS, 3), round(hh * P_HAUT + STOCK * (hh + 1) + DESC_HAUT, 3)]
vol = 21 * GO_SERIE
o["attendu_avec_depot_USD"] = [round((hb + DEPOT_BAS) * P_BAS + STOCK * (hb + DEPOT_BAS + 1) + DESC_BAS + vol * RESEAU_MIN, 3),
                               round((hh + DEPOT_HAUT) * P_HAUT + STOCK * (hh + DEPOT_HAUT + 1) + DESC_HAUT + vol * RESEAU_MAX, 3)]
h_pire = 2 * (hh + DEPOT_HAUT)
o["pire_heures"] = round(h_pire, 2)
o["pire_tout_garde_USD"] = round(h_pire * P_PIRE + STOCK * (h_pire + 1) + DESC_HAUT + vol * RESEAU_MAX, 3)
o["pire_sans_depot_USD"] = round(2 * hh * P_PIRE + STOCK * (2 * hh + 1) + DESC_HAUT, 3)
quart = 0.25 * (P_PIRE + STOCK)
o["quart_d_heure_au_prix_pire_USD"] = round(quart, 4)
o["volumes_Go"] = dict(par_serie=round(GO_SERIE, 4), bloc_A_13=round(13 * GO_SERIE, 2), A_B_16=round(16 * GO_SERIE, 2),
                       A_B_C_19=round(19 * GO_SERIE, 2), tout_21=round(vol, 2), vingt=round(20 * GO_SERIE, 2),
                       dix_sept=round(17 * GO_SERIE, 2))
o["passes"] = dict(series=21 * 64, total=21 * 64 + 576, heures_de_passe_pure=round((21 * 64 + 576) * 0.45 / 3600, 3))

# Bloc A seul au pire cas (hote deux fois plus lent), part p de la notation : meme modele que le devis et la contre-lecture
PASSES_A = 13 * 64 + 5 * 64        # treize series du bloc A et mesure d'intensite (nu et quatre doses) du saboteur


def bloc_A(part, doses=4):
    """Cout du bloc A au pire cas si l'on ne joue que `doses` doses (les doses retirees emportent leurs trois series,
    leur part de notation et leurs 64 passes d'intensite ; HN, la mise en place et la poussee restent)."""
    retirees = 4 - doses
    passes = PASSES_A - retirees * (3 * 64 + 64)
    notation = part * (1 - 0.25 * retirees)
    h = 2 * (POSTES_HAUT["mise_en_place"] + POSTES_HAUT["essais"] + POSTES_HAUT["identite"]
             + POSTES_HAUT["relectures"] * passes / PASSES_TOTAL + POSTES_HAUT["equivalence"] + POSTES_HAUT["notation"] * notation
             + POSTES_HAUT["poussee"])
    return h, h * P_PIRE + STOCK * (h + 1) + DESC_HAUT


for part in (0.7, 1.0):
    h, usd = bloc_A(part)
    o[f"bloc_A_pire_part_{part}"] = dict(heures=round(h, 3), USD=round(usd, 4),
                                         marge_sous_8_5_moins_quart=round(8.5 - quart - usd, 4),
                                         marge_sous_9_moins_quart=round(9.0 - quart - usd, 4))
h3, usd3 = bloc_A(1.0, doses=3)
o["bloc_A_pire_part_1.0_sans_la_dose_0.75"] = dict(heures=round(h3, 3), USD=round(usd3, 4),
                                                   marge_sous_8_5_moins_quart=round(8.5 - quart - usd3, 4),
                                                   economie_d_une_dose_USD=round(bloc_A(1.0)[1] - usd3, 4))
# Garde par serie : avant la derniere dose jouee (0,75), cumul + cout projete de la dose + poussee = cout total du bloc A
seuil = 8.5 - quart
o["garde_par_serie_modele"] = dict(
    seuil_8_5_moins_quart=round(seuil, 4),
    avant_dose_0_25_cumul_plus_projection=round(bloc_A(1.0, doses=3)[1], 4),
    dose_0_25_jouee=bloc_A(1.0, doses=3)[1] <= seuil,
    avant_dose_0_75_cumul_plus_projection=round(bloc_A(1.0)[1], 4),
    dose_0_75_jouee=bloc_A(1.0)[1] <= seuil)
o["option_b_coupure_9"] = dict(somme_8_42_plus_quart=round(bloc_A(1.0)[1] + quart, 4), tient_sous_9=bloc_A(1.0)[1] + quart <= 9.0,
                               surcout_maximal_USD=0.5)
texte = json.dumps(o, indent=1, ensure_ascii=False)
print(texte)
open(sys.argv[1], "w", encoding="utf-8").write(texte + "\n")
