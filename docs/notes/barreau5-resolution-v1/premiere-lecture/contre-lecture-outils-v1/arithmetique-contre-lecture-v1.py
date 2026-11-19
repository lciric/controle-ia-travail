"""Contre-lecture du brouillon 1 « validite de l'adaptateur pour les sondes apprises sur la tache » : arithmetique refaite.

Processeur seul. Aucun fichier de scores ouvert. Entrees : les seules aires scellees du verdict de l'etape B bis
(docs/verdicts/verdict-T0.7-etape-B-bis-v1.md, 1561399a..., par. 3.1 et 3.6 ; bornes de l'adaptateur seul recopiees
de la note 02 du socle, ligne VA-5a) ; les nombres du brouillon de devis (prix, debit, postes), recopies.
Rien n'est importe du script du redacteur : formules ecrites a neuf.
"""
import json
import math
import sys
from statistics import NormalDist

N = NormalDist()
R2 = math.sqrt(2.0)


def d_de(a):          # ecart des moyennes en ecarts types, deux normales de meme variance
    return R2 * N.inv_cdf(a)


def a_de(d):
    return N.cdf(d / R2)


AIRES = {  # D : SA/HN ; TE : SA/SN ; ART : HA/HN ; MU : SN/HN ; ART_b, ART_h : bornes a 95 % (note 02)
    "0.25": dict(D=0.9357, TE=0.9436, ART=0.9252, MU=0.4955, ART_b=0.9046, ART_h=0.9449),
    "0.5": dict(D=0.9854, TE=0.9532, ART=0.9822, MU=0.5706, ART_b=0.9732, ART_h=0.9903),
    "0.75": dict(D=0.9990, TE=0.9967, ART=0.9942, MU=0.6871, ART_b=0.9906, ART_h=0.9973),
    "1": dict(D=0.9994, TE=0.9885, ART=0.9986, MU=0.8793, ART_b=0.9976, ART_h=0.9995),
}
TE_PLIS = {"0.25": (0.9607, 0.9265), "0.5": (0.9980, 0.9084), "0.75": (0.9958, 0.9977), "1": (0.9899, 0.9871)}
# (note 02 du socle, annexe 11.1, champ TE.aires_plis) : l'interaction du texte est la moyenne des deux plis, chacun reduit
# par son propre ecart type ; la prevision par l'aire moyenne n'est pas la moyenne des probits par pli.
out = {"bloc_A_prevision": {}}
for dose, v in AIRES.items():
    out.setdefault("bloc_A2_voie1_probit_moyen_des_plis_de_TE", {})[dose] = round(
        sum(d_de(a) for a in TE_PLIS[dose]) / 2 - d_de(v["ART"]), 3)
    # identite : (SA-SN) - (HA-HN) ; voie 2 : (SA-HN) - (SN-HN) - (HA-HN)
    v1 = d_de(v["TE"]) - d_de(v["ART"])
    v2 = d_de(v["D"]) - d_de(v["MU"]) - d_de(v["ART"])
    # bande de la voie 1 avec les seules bornes scellees de l'adaptateur seul (les autres aires prises sans incertitude)
    v1_b = (d_de(v["TE"]) - d_de(v["ART_h"]), d_de(v["TE"]) - d_de(v["ART_b"]))
    v2_b = (d_de(v["D"]) - d_de(v["MU"]) - d_de(v["ART_h"]), d_de(v["D"]) - d_de(v["MU"]) - d_de(v["ART_b"]))
    # contraste SA contre HA : d(SA,HA) = d(SA,SN) + d(SN,HN) - d(HA,HN) = d(SA,HN) - d(HA,HN)
    c1 = a_de(d_de(v["TE"]) + d_de(v["MU"]) - d_de(v["ART"]))
    c2 = a_de(d_de(v["D"]) - d_de(v["ART"]))
    out["bloc_A_prevision"][dose] = {
        "voie1": round(v1, 3), "voie2": round(v2, 3),
        "bande_voie1_bornes_ART": [round(x, 3) for x in v1_b],
        "bande_voie2_bornes_ART": [round(x, 3) for x in v2_b],
        "bande_reunie": [round(min(v1_b + v2_b), 3), round(max(v1_b + v2_b), 3)],
        "aire_SA_HA_voie1": round(c1, 4), "aire_SA_HA_voie2": round(c2, 4),
        "difference_aires_moins_MU": [round(c1 - v["MU"], 4), round(c2 - v["MU"], 4)],
        "coherence_dD_contre_dTE_plus_dMU": [round(d_de(v["D"]), 3), round(d_de(v["TE"]) + d_de(v["MU"]), 3)],
    }

# ------------------------------------------------------------------ bloc B : famille
out["bloc_B_famille"] = {
    "attendu_8_tests_99_deux_sens": 8 * 0.01,
    "proba_au_moins_une_independance": round(1 - 0.99 ** 8, 4),
    "borne_de_Bonferroni": 0.08,
    "niveau_corrige_5_pour_cent_sur_8": round(1 - 0.05 / 8, 5),
    "attendu_12_tests": 12 * 0.01,
    # taux simules par le redacteur (sorties versees) : critere double 0,0065 max par sens ; Delta-tau seul 0,0093 max
    "attendu_au_pire_simule_interaction_critere_double_plus_tendance_intervalle":
        round(4 * 2 * 0.0065 + 4 * (0.0093 + 0.0093), 3),
}

# ------------------------------------------------------------------ bloc C : epreuve, regle E2 (symetrie a 0,05)
# Probabilite qu'un code symetrique echoue a E2 par le seul hasard : |p+ - p-| > 0,05, n doses par monde, independantes.
e2 = {}
for n in (1000, 2000, 4000):
    for p in (0.5, 0.65, 0.8, 0.9, 0.95):
        sd = math.sqrt(2 * p * (1 - p) / n)
        e2[f"n{n}_p{p}"] = round(2 * (1 - N.cdf(0.05 / sd)), 4)
out["bloc_C_E2_fausse_alarme_par_comparaison"] = e2

# ------------------------------------------------------------------ bloc D : devis refait
P_BAS, P_HAUT, P_PIRE, STOCK, RES = 1.0889, 1.30, 1.40, 0.08, 0.05
bas = [1.0, 0.3, 0.05, 0.45, 0.05, 0.15, 0.10]
haut = [1.0, 0.3, 0.05, 0.80, 0.05, 0.50, 0.10]
hb, hh = sum(bas), sum(haut)
go_serie = 1_058_424_128 / 576 / 1e9 * 640
tot_go = 21 * go_serie
dev = {
    "heures": [round(hb, 2), round(hh, 2)],
    "attendu_sans_depot": [round(hb * P_BAS + STOCK * (hb + 1) + 0.4, 2), round(hh * P_HAUT + STOCK * (hh + 1) + 1.0, 2)],
    "attendu_avec_depot": [round((hb + .15) * P_BAS + STOCK * (hb + 1.15) + 0.4 + tot_go * 0.004, 2),
                           round((hh + .6) * P_HAUT + STOCK * (hh + 1.6) + 1.0 + tot_go * RES, 2)],
    "pire_tout": round(2 * (hh + .6) * P_PIRE + STOCK * (2 * (hh + .6) + 1) + 1.0 + tot_go * RES, 2),
    "quart_heure_pire": round(0.25 * (P_PIRE + STOCK), 3),
    "volume_21_series_Go": round(tot_go, 2), "volume_20_series_Go": round(20 * go_serie, 2),
    "volume_17_series_Go": round(17 * go_serie, 2),
}
# bloc A seul au pire cas, selon la part de la notation qui revient au bloc A (le redacteur prend 0,7)
passes_A = 13 * 64 + 5 * 64
for part in (0.7, 0.85, 0.95, 1.0):
    h = 2 * (1.0 + 0.3 + 0.05 + 0.80 * passes_A / 1920 + 0.05 + 0.50 * part + 0.10)
    usd = h * P_PIRE + STOCK * (h + 1) + 1.0
    dev[f"bloc_A_pire_part_notation_{part}"] = {"heures": round(h, 2), "USD": round(usd, 2),
                                                 "marge_sous_8_5_apres_quart_heure": round(8.5 - usd - 0.25 * (P_PIRE + STOCK), 2)}
# part de la notation du bloc A : directions notees sur le bloc A seulement (800 par sonde, 8 sondes, 4 cases de 64 episodes)
# contre sondes et jumelles sur toutes les series
dir_A = 8 * 800 * 4 * 64
sondes_tout = (13 * 64) * 2 + (8 * 64) * 2 * 8          # bloc A : sonde et jumelle de la dose ; HN et blocs B-D : 8 sondes x 2
dev["part_directions_dans_les_notations_ordre_de_grandeur"] = round(dir_A / (dir_A + sondes_tout), 4)
out["bloc_D_devis"] = dev

texte = json.dumps(out, indent=1, ensure_ascii=False)
print(texte)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write(texte + "\n")
