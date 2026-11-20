"""Ordres de grandeur du redacteur pour le preenregistrement du palier 0b (v2).
Calcul analytique seul : aucun tirage, aucune simulation, aucun resultat de l etage.
Bibliotheque standard et numpy. Sortie JSON sur la sortie standard.
Reprend tous les champs de la v1 (memes valeurs) et ajoute :
- la regle corrigee de C1 et de C4 (correction 3 de la contre-lecture) ;
- le seuil chiffre de << beaucoup plus de sources >> (devis v5, section 9, noeud 4) ;
- deux comptes de paires employes par la correction 2."""
import json, math
from statistics import NormalDist
import numpy as np


class Binomiale:
    def __init__(self, n):
        self.n = n
        logfact = np.concatenate(([0.0], np.cumsum(np.log(np.arange(1, n + 1, dtype=np.float64)))))
        self.indices = np.arange(0, n + 1, dtype=np.float64)
        self.logcomb = logfact[n] - logfact - logfact[::-1]

    def pmf(self, p):
        return np.exp(self.logcomb + self.indices * math.log(p) + (self.n - self.indices) * math.log1p(-p))

    def cdf(self, k, p):
        """P(X <= k), X binomiale (n, p), 0 < p < 1."""
        return float(min(1.0, self.pmf(p)[: k + 1].sum()))

    def queue_haute(self, k, p):
        """P(X >= k)."""
        return float(min(1.0, self.pmf(p)[k:].sum()))

    def clopper_pearson(self, k, niveau=0.95):
        a = (1.0 - niveau) / 2.0
        if k == 0:
            bas = 0.0
        else:
            lo, hi = 1e-12, 1.0 - 1e-12
            for _ in range(60):
                m = (lo + hi) / 2.0
                if 1.0 - self.cdf(k - 1, m) < a: lo = m
                else: hi = m
            bas = (lo + hi) / 2.0
        if k == self.n:
            haut = 1.0
        else:
            lo, hi = 1e-12, 1.0 - 1e-12
            for _ in range(60):
                m = (lo + hi) / 2.0
                if self.cdf(k, m) > a: lo = m
                else: hi = m
            haut = (lo + hi) / 2.0
        return [round(bas, 5), round(haut, 5)]


def sources_approx_normale(delta, alpha_bilateral, puissance=0.8):
    z = NormalDist()
    brut = (z.inv_cdf(1 - alpha_bilateral / 2) + z.inv_cdf(puissance)) ** 2 / delta ** 2
    return {"taille_reduite": delta, "alpha_bilateral": alpha_bilateral,
            "n_test_de_student_approx": round(brut, 2),
            "n_rangs_signes_approx_efficacite_3_sur_pi": round(brut / (3 / math.pi), 2)}


N = 10000
B = Binomiale(N)
s = {"version": 2, "tirages_par_case": N, "intervalles_a_95_pour_cent": {},
     "sources_par_approximation_normale": []}

# --- champs de la v1, inchanges ---
for k in (400, 450, 500, 550, 600, 7800, 7900, 8000, 8100):
    s["intervalles_a_95_pour_cent"][str(k)] = B.clopper_pearson(k)
lo, hi = 0, N
while hi - lo > 1:
    m = (lo + hi) // 2
    if B.clopper_pearson(m)[1] <= 0.06: lo = m
    else: hi = m
s["plus_grand_compte_dont_la_borne_haute_est_au_plus_0_06"] = lo
lo, hi = 0, N
while hi - lo > 1:
    m = (lo + hi) // 2
    if B.clopper_pearson(m)[0] >= 0.79: hi = m
    else: lo = m
s["plus_petit_compte_dont_la_borne_basse_est_au_moins_0_79"] = hi
for d in (0.5, 0.75, 1.0, 1.5):
    for a in (0.025, 0.05):
        s["sources_par_approximation_normale"].append(sources_approx_normale(d, a))
ref = sources_approx_normale(0.5, 0.025)["n_rangs_signes_approx_efficacite_3_sur_pi"]
s["sources_a_taille_0_5_majorees_par_une_part_nulle_de_0_15"] = round(ref / 0.85, 2)

# --- ajout 1 : regle corrigee de C1 et de C4 ---
# Etape 1 : une case est retiree si son compte depasse 500 sur 10 000.
# Etape 2 : sur 100 000 tirages neufs, echec si la borne basse de l intervalle exact
# bilateral de niveau 1 - 0,05/K depasse 0,05, c est-a-dire si P(X >= k | 0,05) < 0,05/(2K).
NC = 100000
BC = Binomiale(NC)
regle = {"tirages_de_confirmation": NC, "seuil_de_retrait_sur_10000": 500,
         "cases_de_C1": 12 * 2 * 3, "cases_de_C4": 12 * 2 * 3, "par_nombre_de_cases": {}}
pmf_005 = BC.pmf(0.05)
queue_005 = np.cumsum(pmf_005[::-1])[::-1]  # queue_005[k] = P(X >= k | 0,05)
for K in (24, 72, 96, 144):
    a = 0.05 / (2 * K)
    kmin = int(np.argmax(queue_005 < a))
    lignes = []
    for p in (0.046, 0.049, 0.05, 0.052, 0.053, 0.055, 0.058):
        retrait = 1.0 - B.cdf(500, p)
        echec_si_retiree = BC.queue_haute(kmin, p)
        lignes.append({"niveau_vrai": p,
                       "probabilite_de_retrait": round(retrait, 4),
                       "probabilite_d_echec_de_la_case": round(retrait * echec_si_retiree, 4)})
    regle["par_nombre_de_cases"][str(K)] = {
        "plus_petit_compte_de_confirmation_qui_fait_echouer": kmin,
        "taux_de_confirmation_correspondant": round(kmin / NC, 5),
        "par_niveau_vrai": lignes,
        "majorant_du_risque_d_echec_a_tort_sur_K_cases_au_niveau_vrai_0_05":
            round(K * lignes[2]["probabilite_d_echec_de_la_case"], 4)}
s["regle_corrigee_de_C1_et_de_C4"] = regle

# --- ajout 2 : seuil chiffre de << beaucoup plus de sources >> ---
GRILLE = [10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48]
NOMBRES_DU_SEUL_CONTRASTE = [6, 7, 8, 9] + GRILLE
ECART_MINIMAL = 8
RAPPORT_MINIMAL = 1.5
COUT_D_UNE_SOURCE_USD = 880  # devis v5, section 7, composition A, dose non nulle
table = []
for n1 in NOMBRES_DU_SEUL_CONTRASTE:
    candidats = [n2 for n2 in GRILLE if n2 - n1 >= ECART_MINIMAL and n2 >= RAPPORT_MINIMAL * n1]
    n2 = candidats[0] if candidats else None
    table.append({"n_du_seul_contraste_de_l_heritage": n1,
                  "plus_petit_n_des_deux_contrastes_qui_remplit_la_condition": n2,
                  "condition_remplie_si_les_deux_contrastes_ne_sont_pas_atteints_jusqu_a_48":
                      bool(48 + 1 - n1 >= ECART_MINIMAL and 48 + 1 >= RAPPORT_MINIMAL * n1) if n2 is None else True,
                  "surcout_minimal_usd_composition_A": None if n2 is None else (n2 - n1) * COUT_D_UNE_SOURCE_USD})
un = sources_approx_normale(1.0, 0.05)["n_rangs_signes_approx_efficacite_3_sur_pi"]
deux = sources_approx_normale(1.0, 0.025)["n_rangs_signes_approx_efficacite_3_sur_pi"]
s["seuil_de_beaucoup_plus_de_sources"] = {
    "ecart_minimal_en_sources": ECART_MINIMAL, "rapport_minimal": RAPPORT_MINIMAL,
    "cout_d_une_source_a_dose_non_nulle_usd": COUT_D_UNE_SOURCE_USD,
    "ecart_minimal_en_usd": ECART_MINIMAL * COUT_D_UNE_SOURCE_USD,
    "economie_deja_pesee_par_le_devis_usd": 6 * COUT_D_UNE_SOURCE_USD,
    "prix_attendu_de_la_procedure_de_holm_par_approximation_normale_a_la_taille_1": {
        "sources_au_seuil_0_05": un, "sources_au_seuil_0_025": deux,
        "ecart": round(deux - un, 2), "rapport": round(deux / un, 3)},
    "table": table}

# --- ajout 3 : comptes de paires de la correction 2 ---
s["paires"] = {"paires_de_huit_lois": math.comb(8, 2),
               "paires_de_282_entrees": math.comb(282, 2),
               "rapport": round(math.comb(282, 2) / math.comb(8, 2), 1)}

print(json.dumps(s, indent=1, sort_keys=True))
