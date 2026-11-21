"""Essais du programme de vérité des dix-sept témoins imposés — v1.

Développeur du programme de vérité des témoins imposés, modèle O.

Lancer : /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider CE_FICHIER

Quatre familles d'essais :
1. pour chaque forme de règle de la grammaire du § 4.3, un cas sain dont la valeur est calculée à la main
   (le calcul est écrit en commentaire), et des artefacts refusés (règle R5) ;
2. la table : T08 au rang juste, T12 du bon côté, T07 aux deux tailles, issues des dix-sept témoins ;
3. l'accord, à 0,001 près, avec le programme de calcul de la note (`301c0f52…`), là où il calcule la même
   chose ; les valeurs de la note sont celles de sa sortie rejouée (`9b66cc78…`, voir le rapport) ;
4. les mutations : chaque garde retirée fait échouer son essai ; six mutations de calcul aussi.
"""
import math
import os
import re
import tempfile
import types
from fractions import Fraction as F

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
CHEMIN = os.path.join(ICI, "calculer_verite_temoins_imposes_v1.py")
with open(CHEMIN, encoding="utf-8") as _f:
    SOURCE = _f.read()


def charger(source=SOURCE, nom="verite_temoins"):
    mod = types.ModuleType(nom)
    mod.__file__ = CHEMIN
    exec(compile(source, CHEMIN, "exec"), mod.__dict__)
    return mod


P = charger()

N01 = {"type": "normale", "parametres": {"mu": 0, "sigma": 1}}


def normale(mu, sigma=1):
    return {"type": "normale", "parametres": {"mu": F(mu), "sigma": F(sigma)}}


def decalage(loi, delta):
    return {"type": "decalage", "parametres": {"loi": loi, "delta_en_ecarts_types": F(delta)}}


def arrondi(loi, pas):
    return {"type": "arrondi", "parametres": {"loi": loi, "pas_de_grille": F(pas)}}


def grappes(tailles, rho=F(1, 5)):
    return {"type": "effet_de_famille_plus_bruit", "parametres": {"correlation_intra": F(rho), "tailles_de_famille": tailles}}


def T(**kw):
    t = {"id": "X", "n": 200, "regle": {"type": "k_ieme_plus_grand", "k": 1},
         "garantie": "avec une confiance dite", "risque_ou_niveau": F(5, 100), "grandeur": "couverture",
         "population_de_calibration": "tous_les_honnetes",
         "portee_de_la_garantie": "tous les episodes honnetes de la tranche",
         "lois": {"calibration": N01, "lecture": N01}}
    t.update(kw)
    return t


def SEQ(**kw):
    t = {"id": "S", "n": None, "regle": {"type": "test_repete_sans_correction", "taux_nul": F(1, 5), "niveau_annonce": F(1, 100)},
         "garantie": "a tout instant", "risque_ou_niveau": F(1, 100), "grandeur": "fausse_alerte_sur_horizon",
         "population_de_calibration": "tous_les_honnetes",
         "portee_de_la_garantie": "tous les episodes honnetes de la tranche", "lois": {},
         "suite": {"taux_honnete": F(1, 5), "horizon": 300}}
    t.update(kw)
    return t


def exacte(res, cle="valeur_exacte"):
    return F(res[cle])


def phibar(z):
    return 0.5 * math.erfc(z / math.sqrt(2))


Z99 = 2.3263478740408408   # quantile normal à 99 % (tables)


# ===================================================================================================
# 1. Moteur exact : cas sains calculés à la main
# ===================================================================================================

def test_queue_binomiale_a_la_main():
    # P(Bin(3, 1/10) >= 2) = 3 × (1/10)² × (9/10) + (1/10)³ = 27/1000 + 1/1000 = 28/1000
    assert P.queue_binomiale_exacte(3, F(1, 10), 2) == F(28, 1000)
    assert P.queue_binomiale_exacte(3, F(1, 10), 0) == 1
    assert P.queue_binomiale_exacte(3, F(1, 10), 4) == 0


def test_k_ieme_plus_grand_sain():
    # n = 2, k = 1 : taux = 1 − F(max) ~ Beta(1, 2) ; P(taux <= 1/100) = 1 − (99/100)² = 199/10000
    r = P.recalculer_temoin(T(n=2))
    assert exacte(r) == F(199, 10000)
    assert r["tenue_de_la_garantie"] == "violee"
    # n = 3, k = 2 : P(Bin(3, 1/100) >= 2) = 3 (1/100)² (99/100) + (1/100)³ = 298 / 10^6
    r = P.recalculer_temoin(T(n=3, regle={"type": "k_ieme_plus_grand", "k": 2}))
    assert exacte(r) == F(298, 10 ** 6)
    # taux moyen : E[Beta(k, n − k + 1)] = k / (n + 1) = 2/4
    assert F(r["quantites"]["taux_moyen"]["valeur_exacte"]) == F(1, 2)


def test_quantile_empirique_rangs_justes():
    # ⌈n × 0,99⌉-ième plus petit = (n − ⌈n × 0,99⌉ + 1)-ième plus grand
    # 400 : ⌈396⌉ = 396 → 5 ; 200 : 198 → 3 ; 300 : 297 → 4 ; 299 : ⌈296,01⌉ = 297 → 3 ; 1000 : 990 → 11
    for n, k in ((400, 5), (200, 3), (300, 4), (299, 3), (1000, 11)):
        assert P.rang_du_quantile_empirique(n, F(99, 100)) == k
    # Le piège du plafond en flottants : il ne mord pas à 0,99 aux tailles en jeu (vérifié de 1 à 2 000),
    # mais il mord à d'autres niveaux : 200 × 0,07 vaut 14,000000000000002 en flottants, plafond 15 au lieu
    # de 14. Rang juste : 200 − 14 + 1 = 187 (et non 186).
    assert all(math.ceil(n * 0.99) == -((-n * 99) // 100) for n in (200, 299, 300, 400, 1000))
    assert math.ceil(200 * 0.07) == 15
    assert P.rang_du_quantile_empirique(200, F(7, 100)) == 187
    # n = 4, niveau 1/2 : ⌈2⌉ = 2e plus petit = 3e plus grand ; P(Bin(4, 1/100) >= 3) = 4 (1/100)³ (99/100) + (1/100)⁴
    r = P.recalculer_temoin(T(n=4, regle={"type": "quantile_empirique", "niveau": F(1, 2)}))
    assert exacte(r) == F(4 * 99 + 1, 10 ** 8)


def test_jamais_et_toujours_alerter():
    r = P.recalculer_temoin(T(regle={"type": "jamais_alerter"}))
    assert exacte(r) == 1 and F(r["quantites"]["taux_moyen"]["valeur_exacte"]) == 0
    r = P.recalculer_temoin(T(regle={"type": "toujours_alerter"}))
    assert exacte(r) == 0 and F(r["quantites"]["taux_moyen"]["valeur_exacte"]) == 1


def test_test_repete_a_la_main():
    # horizon 2, taux nul 1/2, niveau 3/10. t = 1 : p(k=1) = 1/2 ; t = 2 : p(k=2) = 1/4 < 3/10, p(k=1) = 3/4.
    # Seule l'issue (2 alertes en 2) sonne : probabilité 1/4 sous le taux vrai 1/2.
    t = SEQ(regle={"type": "test_repete_sans_correction", "taux_nul": F(1, 2), "niveau_annonce": F(3, 10)},
            risque_ou_niveau=F(3, 10), suite={"taux_honnete": F(1, 2), "horizon": 2})
    assert exacte(P.recalculer_temoin(t)) == F(1, 4)


def test_test_repete_strictement_sous_le_niveau():
    # horizon 2, taux nul 1/2, niveau 1/4 : p(2 alertes en 2) = 1/4, pas strictement sous 1/4 → ne sonne jamais.
    t = SEQ(regle={"type": "test_repete_sans_correction", "taux_nul": F(1, 2), "niveau_annonce": F(1, 4)},
            risque_ou_niveau=F(1, 4), suite={"taux_honnete": F(1, 2), "horizon": 2})
    assert exacte(P.recalculer_temoin(t)) == 0


def test_test_repete_du_bon_cote():
    # Queue droite : la valeur p est P(compte >= compte observé). Taux nul 1/5, horizon 1, niveau 1/4 :
    # p(k=1) = 1/5 < 1/4 → sonne sur une alerte ; p(k=0) = 1 → ne sonne pas sur zéro.
    # Sous le taux vrai 1/5 : 1/5. (Une queue gauche sonnerait sur zéro alerte, à 4/5.)
    t = SEQ(regle={"type": "test_repete_sans_correction", "taux_nul": F(1, 5), "niveau_annonce": F(1, 4)},
            risque_ou_niveau=F(1, 4), suite={"taux_honnete": F(1, 5), "horizon": 1})
    assert exacte(P.recalculer_temoin(t)) == F(1, 5)
    seuils = P.seuils_test_repete(F(1, 5), F(1, 100), 300)
    # à t = 300, la valeur p d'un compte de 75 (moyenne 60) : bien au-dessus de la moyenne pour sonner
    assert seuils[300] > 60


def test_pari_atteint_ou_depasse():
    # taux nul 1/2, parié 3/4 : richesse × 3/2 sur alerte, × 1/2 sinon. Horizon 2, seuil 9/4 :
    # (3/2)² = 9/4 atteint le seuil → sonne sur deux alertes ; probabilité 1/4 sous le taux vrai 1/2.
    regle = {"type": "pari_de_bernoulli", "taux_nul": F(1, 2), "taux_parie": F(3, 4), "seuil_de_richesse": F(9, 4)}
    t = SEQ(regle=regle, suite={"taux_honnete": F(1, 2), "horizon": 2})
    assert exacte(P.recalculer_temoin(t)) == F(1, 4)
    regle2 = dict(regle, seuil_de_richesse=F(9, 4) + F(1, 10 ** 9))
    assert exacte(P.recalculer_temoin(SEQ(regle=regle2, suite={"taux_honnete": F(1, 2), "horizon": 2}))) == 0


def test_seuil_fixe_sain():
    # taux vrai = P(X > 2) = Φ̄(2) = 0,0227501319… > 0,01 → couverture 0 ; P(X > 3) = 0,0013498980… → 1
    r = P.recalculer_temoin(T(regle={"type": "seuil_fixe", "valeur": 2}))
    assert exacte(r) == 0
    assert abs(r["quantites"]["taux_moyen"]["valeur"] - 0.022750131948179) < 1e-11
    r = P.recalculer_temoin(T(regle={"type": "seuil_fixe", "valeur": 3}))
    assert exacte(r) == 1
    assert abs(r["quantites"]["taux_moyen"]["valeur"] - 0.0013498980316301) < 1e-11


def test_tranche_voisine():
    # voisine de 40 épisodes, même loi : couverture 1 − (99/100)^40, taux moyen 1/41 (la base de la tranche D)
    t = T(regle={"type": "plus_grand_de_la_tranche_voisine"}, n=None,
          lois={"lecture": N01, "voisine": {"n": 40, "loi": N01}})
    r = P.recalculer_temoin(t)
    assert exacte(r) == 1 - F(99, 100) ** 40
    assert F(r["quantites"]["taux_moyen"]["valeur_exacte"]) == F(1, 41)
    # lecture décalée de 1/2 : couverture = 1 − (1 − Φ̄(z99 + 1/2))^40
    t["lois"]["lecture"] = normale(F(1, 2))
    r = P.recalculer_temoin(t)
    attendu = 1 - (1 - phibar(Z99 + 0.5)) ** 40
    assert abs(r["valeur_vraie"] - attendu) < 1e-9 and r["borne_erreur"] < 1e-9


def test_moyenne_plus_k_ecarts_types():
    # k = 0 : seuil = moyenne de l'échantillon, Z̄ ~ N(0, 1/n). Taux moyen E[Φ̄(Z̄)] = 1/2 (symétrie).
    # Couverture P(Z̄ >= z99) = Φ̄(√n z99), n = 10.
    r = P.recalculer_temoin(T(n=10, regle={"type": "moyenne_plus_k_ecarts_types", "k": 0}))
    assert abs(r["valeur_vraie"] - phibar(math.sqrt(10) * Z99)) < 1e-9
    assert abs(r["quantites"]["taux_moyen"]["valeur"] - 0.5) < 1e-9
    assert abs(r["quantites"]["taux_moyen_ecart_type_divise_par_n"]["valeur"] - 0.5) < 1e-9
    # Limite : n grand, S ≈ 1 ; taux moyen ≈ Φ̄(k / √(1 + 1/n)) (écart de l'ordre de var(S) ≈ 1/(2n))
    r = P.recalculer_temoin(T(n=2000, garantie="en moyenne", risque_ou_niveau=None, grandeur="taux_moyen",
                              regle={"type": "moyenne_plus_k_ecarts_types", "k": F(233, 100)}))
    assert abs(r["valeur_vraie"] - phibar(2.33 / math.sqrt(1 + 1 / 2000))) < 1e-4


def test_grappes_sans_correlation_et_note():
    # ρ = 0 : épisodes indépendants, couverture 1 − (99/100)^300
    r = P.recalculer_temoin(T(n=300, lois={"calibration": grappes([100] * 3, 0), "lecture": N01}))
    assert abs(r["valeur_vraie"] - float(1 - F(99, 100) ** 300)) < 1e-9


def test_lois_valeurs_a_la_main():
    # Student ν = 1 (Cauchy) : P(X > 1) = 1/2 − arctan(1)/π = 1/4
    assert abs(P.construire_loi({"type": "student", "parametres": {"nu": 1, "mu": 0, "echelle": 1}}).sf(1.0) - 0.25) < 1e-13
    # Student ν = 2 : P(X > t) = 1/2 − t / (2 √(2 + t²)) ; t = 1 : 1/2 − 1/(2√3)
    s2 = P.construire_loi({"type": "student", "parametres": {"nu": 2, "mu": 0, "echelle": 1}})
    assert abs(s2.sf(1.0) - (0.5 - 1 / (2 * math.sqrt(3)))) < 1e-13
    # Laplace : P(X > 1) = e^{-1} / 2
    assert abs(P.construire_loi({"type": "laplace", "parametres": {"mu": 0, "echelle": 1}}).sf(1.0) - math.exp(-1) / 2) < 1e-15
    # lognormale (0, 1) : P(X > e) = Φ̄(1)
    assert abs(P.construire_loi({"type": "lognormale", "parametres": {"mu": 0, "sigma": 1}}).sf(math.e) - phibar(1)) < 1e-15
    # mélange ½ N(0,1) + ½ N(2,1) : P(X > 1) = ½ Φ̄(1) + ½ Φ̄(−1) = ½
    mel = {"type": "melange", "parametres": {"poids": [F(1, 2), F(1, 2)], "composantes": [N01, normale(2)]}}
    assert abs(P.construire_loi(mel).sf(1.0) - 0.5) < 1e-15
    # somme de 2 pas N(0,1) équicorrélés à 1/2 : variance 2 + 2 × 1/2 = 3 ; P(X > √3) = Φ̄(1)
    sp = {"type": "somme_de_pas", "parametres": {"nombre_de_pas": 2, "loi_du_pas": N01, "correlation": F(1, 2), "structure": "equicorrelee"}}
    assert abs(P.construire_loi(sp).sf(math.sqrt(3)) - phibar(1)) < 1e-14
    # ar1, 3 pas, r = 1/2 : variance 3 + 2 (2 × 1/2 + 1 × 1/4) = 5,5
    sp["parametres"].update({"nombre_de_pas": 3, "structure": "ar1"})
    assert abs(P.construire_loi(sp).sf(math.sqrt(5.5)) - phibar(1)) < 1e-14
    # décalage d'un écart type de N(0, 2) : translation de 2 ; P(X > 2) = 1/2
    assert abs(P.construire_loi(decalage(normale(0, 2), 1)).sf(2.0) - 0.5) < 1e-15


def test_reseau_a_la_main():
    # X = entier le plus proche d'une N(0,1). n = 1, k = 1 : s = X1, taux = P(X > s).
    # g* = plus petit atome de taux <= 0,01 : P(X > 1) = Φ̄(1,5) = 0,0668 ; P(X > 2) = Φ̄(2,5) = 0,0062 → g* = 2.
    # Couverture = P(X1 >= 2) = Φ̄(1,5).
    loi = arrondi(N01, 1)
    r = P.recalculer_temoin(T(n=1, lois={"calibration": loi, "lecture": loi}))
    assert abs(r["valeur_vraie"] - phibar(1.5)) < 1e-12
    # Taux moyen, n = 1 : E[P(X > X')] = (1 − Σ_m P(m)²) / 2
    masses = [phibar(m - 0.5) - phibar(m + 0.5) for m in range(-12, 13)]
    attendu = (1 - sum(p * p for p in masses)) / 2
    assert abs(r["quantites"]["taux_moyen"]["valeur"] - attendu) < 1e-12
    # Avec ex æquo, l'inégalité stricte garde le taux moyen du plus grand de n sous 1/(n + 1)
    r = P.recalculer_temoin(T(n=5, lois={"calibration": loi, "lecture": loi}))
    assert r["quantites"]["taux_moyen"]["valeur"] < 1 / 6
    # lecture sur réseau (g* = 2), calibration continue N(0,1), n = 1 : couverture P(Y >= 2) = Φ̄(2)
    r = P.recalculer_temoin(T(n=1, lois={"calibration": N01, "lecture": loi}))
    assert abs(r["valeur_vraie"] - phibar(2.0)) < 1e-12
    # seuil fixe sur un atome, en rationnels exacts : P(X > 1) = P(Y > 1,5)
    r = P.recalculer_temoin(T(regle={"type": "seuil_fixe", "valeur": 1}, lois={"lecture": loi}))
    assert abs(r["quantites"]["taux_moyen"]["valeur"] - phibar(1.5)) < 1e-12


def test_chemin_flottant_contre_chemin_exact():
    # même loi écrite deux fois (décalage nul) : le chemin flottant encadré doit contenir la valeur exacte
    for n, k in ((200, 1), (300, 3), (1000, 6)):
        t = T(n=n, regle={"type": "k_ieme_plus_grand", "k": k}, lois={"calibration": N01, "lecture": decalage(N01, 0)})
        r = P.recalculer_temoin(t)
        cov = float(P.couverture_rang_exacte(n, k))
        assert abs(r["valeur_vraie"] - cov) <= r["borne_erreur"] + 1e-12
        tm = r["quantites"]["taux_moyen"]
        assert abs(tm["valeur"] - k / (n + 1)) <= tm["borne_erreur"] + 1e-12
        assert tm["borne_erreur"] < 2e-5


def test_familles_C_et_I_au_recalcul(table):
    # C : 0,95 N(0,1) + 0,05 N(2,1), la composante « qui échoue » décalée de 2.
    # T14 : calibré sur le mélange, lu sur N(2,1) : g* = 2 + z99 ; π = P_mélange(X >= g*) = 0,95 Φ̄(2 + z99) + 0,05 × 0,01
    echec = normale(2)
    melange = {"type": "melange", "parametres": {"poids": [F(19, 20), F(1, 20)], "composantes": [N01, echec]}}
    r = P.recalculer_temoin(T(id="T14", n=299, portee_de_la_garantie="conditionnelle a l'issue",
                              lois={"calibration": melange, "lecture": echec}))
    pi = 0.95 * phibar(2 + Z99) + 0.05 * 0.01
    assert abs(r["valeur_vraie"] - (1 - (1 - pi) ** 299)) < 1e-9
    assert r["issue_recalculee"] == "morte_invalide"
    pi_bas = float(table["T14"]["valeurs_de_plus"]["pi_critique_borne_basse"])
    assert pi < pi_bas
    # T15 : calibré et lu sur le mélange : exact, 1 − 0,99^299
    r = P.recalculer_temoin(T(id="T15", n=299, lois={"calibration": melange, "lecture": melange}))
    assert F(r["valeur_exacte"]) == 1 - F(99, 100) ** 299
    # T16 : calibré et lu sur la composante qui échoue : exact ; taux moyen 1/300
    r = P.recalculer_temoin(T(id="T16", n=299, population_de_calibration="honnetes_qui_echouent",
                              portee_de_la_garantie="conditionnelle a l'issue", lois={"calibration": echec, "lecture": echec}))
    assert F(r["valeur_exacte"]) == 1 - F(99, 100) ** 299
    assert F(r["quantites"]["taux_moyen"]["valeur_exacte"]) == F(1, 300)
    # I : la composante qui échoue en N(6, 1). Au quantile vrai à 99 % du mélange, le taux parmi ceux qui
    # échouent vaut 0,2 à 0,001 près (la composante qui réussit n'a presque rien au-delà) ; T17 doit tomber
    # dans l'encadrement de la table, établi sans connaître la loi.
    echec_i = normale(6)
    melange_i = {"type": "melange", "parametres": {"poids": [F(19, 20), F(1, 20)], "composantes": [N01, echec_i]}}
    q99 = P._isf_continue(P.construire_loi(melange_i), 0.01)[1]
    assert abs(phibar(q99 - 6) - 0.2) <= 0.001
    r = P.recalculer_temoin(T(id="T17", n=299, portee_de_la_garantie="conditionnelle a l'issue",
                              lois={"calibration": melange_i, "lecture": echec_i}))
    v = table["T17"]["valeurs_de_plus"]
    assert v["couverture_borne_basse_sous_condition"] - 1e-12 <= r["valeur_vraie"] <= v["couverture_borne_haute_sous_condition"]
    assert r["issue_recalculee"] == "morte_invalide"


def test_recalcul_bout_en_bout_et_comparaison():
    entree = {"version_entree": P.VERSION_ENTREE_RECALCUL, "temoins": [
        dict(T(id="A", n=299), valeur_annoncee=F(9505, 10000), issue_annoncee="tient"),
        dict(T(id="B", n=299), valeur_annoncee=F(9525, 10000)),
        T(id="C", n=None),
        dict(T(id="D", n=299, lois={"calibration": N01, "lecture": decalage(N01, F(4456, 10000))}),
             valeur_annoncee=F(5658, 10000), issue_annoncee="tient"),
    ]}
    s = P.recalculer(entree)
    assert s["temoins"]["A"]["comparaison"]["statut"] == "en_deca_de_0_001" and s["temoins"]["A"]["accord_issue"]
    assert s["temoins"]["B"]["comparaison"]["statut"] == "au_dela_de_0_001"
    assert s["temoins"]["C"]["statut"] == "refuse" and s["temoins"]["C"]["code"] == "taille_absente"
    assert s["temoins"]["D"]["comparaison"]["statut"] == "en_deca_de_0_001"
    assert s["temoins"]["D"]["issue_recalculee"] == "morte_invalide" and s["temoins"]["D"]["accord_issue"] is False
    assert s["comptes"] == {"calcules": 3, "refuses": 1, "ecarts_au_dela_de_0_001": 1,
                            "ecarts_indecis_a_la_borne": 0, "desaccords_d_issue": 1}


def test_lecture_json_en_rationnels_et_ligne_de_commande():
    with tempfile.TemporaryDirectory(dir=ICI) as d:
        entree = os.path.join(d, "entree.json")
        with open(entree, "w", encoding="utf-8") as f:
            f.write('{"version_entree": "%s", "temoins": [{"id": "Q", "n": 400, "regle": {"type": "quantile_empirique", '
                    '"niveau": 0.99}, "garantie": "avec une confiance dite", "risque_ou_niveau": 0.05, "grandeur": '
                    '"couverture", "population_de_calibration": "tous_les_honnetes", "portee_de_la_garantie": '
                    '"tous les episodes honnetes de la tranche", "lois": {"calibration": {"type": "normale", '
                    '"parametres": {"mu": 0, "sigma": 1}}, "lecture": {"type": "normale", "parametres": {"mu": 0, '
                    '"sigma": 1}}}}]}' % P.VERSION_ENTREE_RECALCUL)
        lu = P.lire_json(entree)
        assert lu["temoins"][0]["regle"]["niveau"] == F(99, 100)
        sortie = os.path.join(d, "sortie.json")
        assert P.main(["--recalculer", entree, sortie]) == 0
        res = P.lire_json(sortie)["temoins"]["Q"]
        assert res["quantites"]["rang_k_ieme_plus_grand"]["valeur"] == 5
        assert F(res["valeur_exacte"]) == P.queue_binomiale_exacte(400, F(1, 100), 5)
        assert P.main(["--recalculer", entree, sortie]) == 3          # on n'écrase jamais
        assert P.main(["--inconnu"]) == 2


# ===================================================================================================
# 2. La table des dix-sept témoins imposés
# ===================================================================================================

@pytest.fixture(scope="module")
def table():
    return P.table_des_temoins()


ISSUES_ATTENDUES = {"T01": "morte_invalide", "T02": "tient", "T03": "tient", "T04": "morte_invalide",
                    "T05": "morte_sans_gain", "T06": "morte_invalide", "T07": "morte_sans_gain",
                    "T08": "morte_invalide", "T09": "morte_invalide", "T10": "morte_invalide",
                    "T11": "morte_invalide", "T12": "morte_invalide", "T13": "tient", "T14": None,
                    "T15": "tient", "T16": "tient", "T17": "morte_invalide"}


def test_dix_sept_temoins_et_issues(table):
    assert sorted(table) == [f"T{i:02d}" for i in range(1, 18)]
    assert {i: table[i]["issue_attendue"] for i in table} == ISSUES_ATTENDUES


def test_valeurs_exactes_a_la_main(table):
    def queue(n, k):   # P(Bin(n, 1/100) >= k) = 1 − Σ_{j<k} C(n, j) (1/100)^j (99/100)^(n−j)
        return 1 - sum(math.comb(n, j) * F(1, 100) ** j * F(99, 100) ** (n - j) for j in range(k))
    assert F(table["T01"]["valeur_exacte"]) == queue(300, 3)
    assert F(table["T02"]["valeur_exacte"]) == 1 - F(99, 100) ** 299
    assert F(table["T03"]["valeur_exacte"]) == F(3, 301)
    assert F(table["T04"]["valeur_exacte"]) == queue(1000, 6)
    assert F(table["T05"]["valeur_exacte"]) == 0
    assert F(table["T06"]["valeur_exacte"]) == 1 - F(99, 100) ** 200
    assert F(table["T08"]["valeur_exacte"]) == queue(400, 5)
    assert F(table["T15"]["valeur_exacte"]) == 1 - F(99, 100) ** 299
    assert F(table["T16"]["valeur_exacte"]) == 1 - F(99, 100) ** 299
    assert F(table["T17"]["valeur_exacte"]) == 1 - (1 - F(1, 100) * F(1, 20)) ** 299


def test_T08_au_rang_juste(table):
    assert table["T08"]["valeurs_de_plus"]["rang_k_ieme_plus_grand"] == 5


def test_T07_aux_deux_tailles(table):
    t7 = table["T07"]
    assert F(t7["valeur_exacte"]) == F(1, 201) and t7["entree_de_reference"]["n"] == 200
    assert F(t7["valeurs_de_plus"]["taux_moyen_n400"]["valeur_exacte"]) == F(1, 401)
    for nom in ("aire_0_69", "aire_0_80", "aire_0_95"):
        assert F(t7["valeurs_de_plus"][f"ecart_de_puissance_a_la_base_{nom}"]["valeur_exacte"]) == 0
        assert 0 < t7["valeurs_de_plus"][f"puissance_{nom}"]["valeur"] < 1
    t5 = table["T05"]
    for nom in ("aire_0_69", "aire_0_80", "aire_0_95"):
        assert F(t5["valeurs_de_plus"][f"puissance_{nom}"]["valeur_exacte"]) == 0
        assert t5["valeurs_de_plus"][f"ecart_de_puissance_a_la_base_{nom}"]["valeur"] == pytest.approx(
            -t7["valeurs_de_plus"][f"puissance_{nom}"]["valeur"], abs=1e-12)


def test_T12_du_bon_cote_et_T13(table):
    # La note (bloc F) : 0,0770 pour le test répété, 0,0076 pour le pari ; le pari sonne 0,888 contre 0,30
    # et 0,272 sous la dérive à 0,25.
    assert abs(table["T12"]["valeur_vraie"] - 0.0770) <= 0.00005 + 1e-12
    assert abs(table["T13"]["valeur_vraie"] - 0.0076) <= 0.00005 + 1e-12
    v = table["T13"]["valeurs_de_plus"]
    assert abs(v["puissance_contre_le_saboteur_0_30"]["valeur"] - 0.888) <= 0.0005
    assert abs(v["fausse_alerte_sous_derive_0_25"]["valeur"] - 0.272) <= 0.0005


def test_lecture_D_M16(table):
    # la base, et tout témoin autre que T05 et T07, se lit sur la seule garantie
    for ident in ("T02", "T06", "T15", "T16"):
        assert table[ident]["issue_attendue"] in ("tient", "morte_invalide")
    assert P.IDS_LUS_SANS_GAIN == frozenset({"T05", "T07"})


def test_T17_encadrement_sous_condition(table):
    v = table["T17"]["valeurs_de_plus"]
    assert v["couverture_borne_basse_sous_condition"] <= table["T17"]["valeur_vraie"] <= v["couverture_borne_haute_sous_condition"] < 0.95


def test_recalcul_aux_lois_de_reference_egal_a_la_table(table):
    for t in P.temoins_imposes_en_entree():
        r = P.recalculer_temoin(t)
        assert r["valeur_vraie"] == table[t["id"]]["valeur_vraie"]
        assert r["issue_recalculee"] == table[t["id"]]["issue_attendue"]


def test_sortie_jouee_deux_fois_identique():
    with tempfile.TemporaryDirectory(dir=ICI) as d:
        a, b = os.path.join(d, "a.json"), os.path.join(d, "b.json")
        assert P.main([a]) == 0 and P.main([b]) == 0
        with open(a, "rb") as fa, open(b, "rb") as fb:
            assert fa.read() == fb.read()
        assert P.main([a]) == 3


# ===================================================================================================
# 3. Accord avec le programme de calcul de la note (sortie rejouée, valeurs imprimées)
# ===================================================================================================

def ecart_note(mesure, imprime, decimales):
    """Écart à la valeur imprimée ; tenu à 0,001 (mandat) et, plus serré, au demi-chiffre imprimé."""
    e = abs(mesure - imprime)
    assert e <= 0.001
    assert e <= 0.5 * 10 ** (-decimales) + 2e-5
    return e


NOTE_A = [(300, 3, 0.5779, 0.00997), (299, 1, 0.9505, 0.00333), (300, 1, 0.9510, 0.00332), (368, 1, 0.9752, 0.00271),
          (1000, 5, 0.9713, 0.00500), (1000, 6, 0.9339, 0.00599), (1000, 10, 0.5427, 0.00999),
          (200, 1, 0.8660, 0.00498), (200, 2, 0.5954, 0.00995), (400, 1, 0.9820, 0.00249), (400, 4, 0.5675, 0.00998)]


@pytest.mark.parametrize("n,k,cov,tm", NOTE_A)
def test_note_blocs_A_et_G(n, k, cov, tm):
    ecart_note(float(P.couverture_rang_exacte(n, k)), cov, 4)
    ecart_note(float(P.taux_moyen_rang_exact(n, k)), tm, 5)


NOTE_C = [(299, 1, (0.020, 0.057, 0.305)), (368, 1, (0.017, 0.050, 0.283)), (300, 3, (0.050, 0.122, 0.478))]


@pytest.mark.parametrize("n,k,attendus", NOTE_C)
def test_note_bloc_C_puissance(n, k, attendus):
    sab = P.saboteurs_binormaux()
    for (nom, spec), imprime in zip(sorted(sab.items()), attendus):
        r = P.recalculer_temoin(T(n=n, regle={"type": "k_ieme_plus_grand", "k": k}, lois={"calibration": N01, "lecture": N01, "saboteurs": {nom: spec}}))
        ecart_note(r["puissances"][nom]["valeur"], imprime, 3)


def test_note_bloc_D_derive():
    delta = P.decalage_qui_triple(P.Normale(0, 1))
    ecart_note(delta, 0.4456, 4)
    for n, k, imprime in ((299, 1, 0.5658), (368, 1, 0.6419), (1000, 5, 0.1500)):
        r = P.recalculer_temoin(T(n=n, regle={"type": "k_ieme_plus_grand", "k": k},
                                  lois={"calibration": N01, "lecture": decalage(N01, F(delta))}))
        ecart_note(r["valeur_vraie"], imprime, 4)


def test_note_bloc_E_grappes():
    for tailles, imprime in (([1] * 300, 0.9510), ([10] * 30, 0.9351), ([30] * 10, 0.9036), ([100] * 3, 0.8167)):
        r = P.recalculer_temoin(T(n=300, lois={"calibration": grappes(tailles), "lecture": N01}))
        ecart_note(r["valeur_vraie"], imprime, 4)


def test_note_bloc_F_deploiement():
    q = F(1, 5)
    repete = P.predicat_test_repete(q, F(1, 100), 300)
    pari = P.predicat_pari(q, F(3, 10), F(100), 300)
    ecart_note(float(P.probabilite_de_sonner(repete, q, 300)), 0.0770, 4)
    ecart_note(float(P.probabilite_de_sonner(pari, q, 300)), 0.0076, 4)
    for p, (r_rep, r_pari) in ((F(1, 4), (0.580, 0.272)), (F(3, 10), (0.976, 0.888)), (F(2, 5), (1.000, 1.000))):
        ecart_note(float(P.probabilite_de_sonner(repete, p, 300)), r_rep, 3)
        ecart_note(float(P.probabilite_de_sonner(pari, p, 300)), r_pari, 3)


# ===================================================================================================
# 4. Artefacts refusés (R5) et mutations
# ===================================================================================================

def _z99_rationnel(mod):
    bas, haut = mod._isf_continue(mod.Normale(0, 1), 0.01)
    return F(haut)


def _lecture_alpha_sur_atome(mod):
    mu = F(1.5) - _z99_rationnel(mod)
    loi = arrondi(normale(mu), 1)
    return T(n=1, lois={"calibration": loi, "lecture": loi})


V = P.VERSION_ENTREE_RECALCUL
STUDENT1 = {"type": "student", "parametres": {"nu": 1, "mu": 0, "echelle": 1}}
LAPLACE = {"type": "laplace", "parametres": {"mu": 0, "echelle": 1}}

ARTEFACTS = {
    "nombre_non_rationnel": lambda m: m.rang_du_quantile_empirique(400, 0.99),
    "entier_attendu": lambda m: m.recalculer_temoin(T(n=F(7, 2))),
    "entier_trop_petit": lambda m: m.recalculer_temoin(T(n=0)),
    "probabilite_hors_domaine": lambda m: m.recalculer_temoin(T(risque_ou_niveau=F(0))),
    "niveau_quantile_hors_domaine": lambda m: m.recalculer_temoin(T(regle={"type": "quantile_empirique", "niveau": F(1)})),
    "moyenne_indefinie": lambda m: m.construire_loi(decalage({"type": "melange", "parametres": {"poids": [F(1, 2), F(1, 2)], "composantes": [STUDENT1, N01]}}, 1)),
    "ecart_type_indefini": lambda m: m.construire_loi(decalage({"type": "student", "parametres": {"nu": 2, "mu": 0, "echelle": 1}}, 1)),
    "reseau_trop_fin": lambda m: m.construire_loi(arrondi(N01, F(1, 10 ** 7))),
    "egalite_sur_reseau": lambda m: m.recalculer_temoin(T(n=1, lois={"calibration": arrondi(N01, F(1, 2)), "lecture": arrondi(N01, 1)})),
    "forme_de_loi": lambda m: m.construire_loi({"type": "normale"}),
    "loi_hors_grammaire": lambda m: m.construire_loi({"type": "gamma", "parametres": {}}),
    "loi_hors_moteur": lambda m: m.construire_loi({"type": "couple", "parametres": {}}),
    "parametres_de_loi": lambda m: m.construire_loi({"type": "normale", "parametres": {"mu": 0}}),
    "parametre_non_positif": lambda m: m.construire_loi(normale(0, 0)),
    "melange_longueurs": lambda m: m.construire_loi({"type": "melange", "parametres": {"poids": [1], "composantes": []}}),
    "melange_somme_des_poids": lambda m: m.construire_loi({"type": "melange", "parametres": {"poids": [F(1, 2), F(1, 3)], "composantes": [N01, N01]}}),
    "melange_non_continu": lambda m: m.construire_loi({"type": "melange", "parametres": {"poids": [F(1, 2), F(1, 2)], "composantes": [arrondi(N01, 1), N01]}}),
    "somme_de_pas_non_normale": lambda m: m.construire_loi({"type": "somme_de_pas", "parametres": {"nombre_de_pas": 2, "loi_du_pas": LAPLACE, "correlation": 0, "structure": "ar1"}}),
    "structure_inconnue": lambda m: m.construire_loi({"type": "somme_de_pas", "parametres": {"nombre_de_pas": 2, "loi_du_pas": N01, "correlation": 0, "structure": "toeplitz"}}),
    "correlation_hors_domaine": lambda m: m.construire_loi({"type": "somme_de_pas", "parametres": {"nombre_de_pas": 2, "loi_du_pas": N01, "correlation": 1, "structure": "ar1"}}),
    "equicorrelation_hors_domaine": lambda m: m.construire_loi({"type": "somme_de_pas", "parametres": {"nombre_de_pas": 3, "loi_du_pas": N01, "correlation": F(-3, 5), "structure": "equicorrelee"}}),
    "correlation_intra_hors_domaine": lambda m: m.construire_loi(grappes([10], 1)),
    "tailles_de_famille": lambda m: m.construire_loi(grappes([])),
    "arrondi_non_continu": lambda m: m.construire_loi(arrondi(arrondi(N01, 1), 1)),
    "decalage_de_grappes": lambda m: m.construire_loi(decalage(grappes([10]), 1)),
    "taux_egal_a_alpha_sur_reseau": lambda m: m.recalculer_temoin(_lecture_alpha_sur_atome(m)),
    "moyenne_k_loi_non_normale": lambda m: m.recalculer_temoin(T(regle={"type": "moyenne_plus_k_ecarts_types", "k": 2}, lois={"calibration": LAPLACE, "lecture": LAPLACE})),
    "moyenne_k_saboteur_non_normal": lambda m: m.recalculer_temoin(T(regle={"type": "moyenne_plus_k_ecarts_types", "k": 2}, lois={"calibration": N01, "lecture": N01, "saboteurs": {"s": LAPLACE}})),
    "forme_de_regle": lambda m: m.recalculer_temoin(T(regle=[])),
    "regle_hors_grammaire": lambda m: m.recalculer_temoin(T(regle={"type": "mediane"})),
    "parametres_de_regle": lambda m: m.recalculer_temoin(T(regle={"type": "k_ieme_plus_grand"})),
    "k_superieur_a_n": lambda m: m.recalculer_temoin(T(n=2, regle={"type": "k_ieme_plus_grand", "k": 3})),
    "saboteurs_requis_sans_gain": lambda m: m.recalculer_temoin(T(id="T05", regle={"type": "jamais_alerter"}, garantie="en moyenne", risque_ou_niveau=None, grandeur="taux_moyen")),
    "risque_inattendu": lambda m: m.recalculer_temoin(T(garantie="en moyenne", grandeur="taux_moyen")),
    "risque_absent": lambda m: m.recalculer_temoin(T(risque_ou_niveau=None)),
    "forme_du_temoin": lambda m: m.recalculer_temoin([]),
    "cles_du_temoin": lambda m: m.recalculer_temoin(dict(T(), formule="x")),
    "garantie_hors_liste": lambda m: m.recalculer_temoin(T(garantie="toujours")),
    "grandeur_hors_liste": lambda m: m.recalculer_temoin(T(grandeur="rappel")),
    "champ_ferme_population": lambda m: m.recalculer_temoin(T(population_de_calibration="tous")),
    "cles_de_lois": lambda m: m.recalculer_temoin(T(lois={"calibration": N01, "lecture": N01, "usage": N01})),
    "garantie_incoherente": lambda m: m.recalculer_temoin(T(regle={"type": "test_repete_sans_correction", "taux_nul": F(1, 5), "niveau_annonce": F(1, 100)})),
    "garantie_incoherente_seuil": lambda m: m.recalculer_temoin(SEQ(regle={"type": "k_ieme_plus_grand", "k": 1})),
    "suite_absente": lambda m: m.recalculer_temoin({k: v for k, v in SEQ().items() if k != "suite"}),
    "taux_parie_egal_au_nul": lambda m: m.recalculer_temoin(SEQ(regle={"type": "pari_de_bernoulli", "taux_nul": F(1, 5), "taux_parie": F(1, 5), "seuil_de_richesse": 100})),
    "seuil_de_richesse_invalide": lambda m: m.recalculer_temoin(SEQ(regle={"type": "pari_de_bernoulli", "taux_nul": F(1, 5), "taux_parie": F(3, 10), "seuil_de_richesse": 1})),
    "puissance_sans_saboteur_sequentiel": lambda m: m.recalculer_temoin(SEQ(grandeur="puissance")),
    "grandeur_incoherente_sequentielle": lambda m: m.recalculer_temoin(SEQ(grandeur="couverture")),
    "taille_absente": lambda m: m.recalculer_temoin(T(n=None)),
    "loi_de_lecture_absente": lambda m: m.recalculer_temoin(T(lois={"calibration": N01})),
    "grappes_en_lecture": lambda m: m.recalculer_temoin(T(lois={"calibration": N01, "lecture": grappes([200])})),
    "grappes_en_saboteur": lambda m: m.recalculer_temoin(T(lois={"calibration": N01, "lecture": N01, "saboteurs": {"s": grappes([200])}})),
    "loi_de_calibration_absente": lambda m: m.recalculer_temoin(T(lois={"lecture": N01})),
    "voisine_absente": lambda m: m.recalculer_temoin(T(regle={"type": "plus_grand_de_la_tranche_voisine"}, lois={"lecture": N01})),
    "grappes_regle": lambda m: m.recalculer_temoin(T(n=300, regle={"type": "k_ieme_plus_grand", "k": 2}, lois={"calibration": grappes([100] * 3), "lecture": N01})),
    "grappes_taille": lambda m: m.recalculer_temoin(T(n=299, lois={"calibration": grappes([100] * 3), "lecture": N01})),
    "grappes_grandeur": lambda m: m.recalculer_temoin(T(n=300, garantie="en moyenne", risque_ou_niveau=None, grandeur="taux_moyen", lois={"calibration": grappes([100] * 3), "lecture": N01})),
    "taux_egal_a_alpha_seuil_fixe": lambda m: m.recalculer_temoin(T(regle={"type": "seuil_fixe", "valeur": _z99_rationnel(m)})),
    "moyenne_k_taille": lambda m: m.recalculer_temoin(T(n=1, regle={"type": "moyenne_plus_k_ecarts_types", "k": 1})),
    "puissance_sans_saboteur_unique": lambda m: m.recalculer_temoin(T(grandeur="puissance")),
    "grandeur_incoherente_a_seuil": lambda m: m.recalculer_temoin(T(grandeur="fausse_alerte_sur_horizon")),
    "version_entree": lambda m: m.recalculer({"version_entree": "autre", "temoins": []}),
    "identifiant_double": lambda m: m.recalculer({"version_entree": V, "temoins": [T(id="A"), T(id="A")]}),
    "sortie_existante": lambda m: m.ecrire_json({}, CHEMIN),
}

GARDES = re.findall(r"# GARDE:(\w+)", SOURCE)


def test_chaque_garde_a_son_artefact():
    assert len(GARDES) == len(set(GARDES))
    assert set(GARDES) == set(ARTEFACTS)
    for ligne in SOURCE.splitlines():
        if "# GARDE:" in ligne:
            code = ligne.rsplit("# GARDE:", 1)[1].strip()
            assert re.search(r"^\s*if .*?: raise Refus\(\"" + code + "\"", ligne), code


@pytest.mark.parametrize("code", sorted(ARTEFACTS))
def test_artefact_refuse(code):
    with pytest.raises(P.Refus) as e:
        ARTEFACTS[code](P)
    assert e.value.code == code


def _mutant_sans_garde(code):
    lignes = SOURCE.splitlines(keepends=True)
    trouve = 0
    for i, l in enumerate(lignes):
        if l.rstrip().endswith(f"# GARDE:{code}"):
            nouvelle = re.sub(r"^(\s*)if .*?: raise Refus\(", r"\1if False: raise Refus(", l, count=1)
            assert nouvelle != l
            lignes[i] = nouvelle
            trouve += 1
    assert trouve == 1
    return charger("".join(lignes), nom=f"mutant_{code}")


@pytest.mark.parametrize("code", sorted(ARTEFACTS))
def test_mutation_garde_retiree_fait_echouer_son_essai(code):
    mutant = _mutant_sans_garde(code)
    try:
        ARTEFACTS[code](mutant)
        detecte = True
    except mutant.Refus as e:
        detecte = e.code != code
    except Exception:
        detecte = True
    assert detecte, f"la garde {code} retirée, son essai passe encore"


def _verif_quantile(m):
    assert m.rang_du_quantile_empirique(400, F(99, 100)) == 5
    assert m.rang_du_quantile_empirique(200, F(7, 100)) == 187


def _verif_strict(m):
    t = SEQ(regle={"type": "test_repete_sans_correction", "taux_nul": F(1, 2), "niveau_annonce": F(1, 4)},
            risque_ou_niveau=F(1, 4), suite={"taux_honnete": F(1, 2), "horizon": 2})
    assert F(m.recalculer_temoin(t)["valeur_exacte"]) == 0


def _verif_cote(m):
    q = F(1, 5)
    assert abs(float(m.probabilite_de_sonner(m.predicat_test_repete(q, F(1, 100), 300), q, 300)) - 0.0770) <= 0.001


def _verif_pari(m):
    regle = {"type": "pari_de_bernoulli", "taux_nul": F(1, 2), "taux_parie": F(3, 4), "seuil_de_richesse": F(9, 4)}
    assert F(m.recalculer_temoin(SEQ(regle=regle, suite={"taux_honnete": F(1, 2), "horizon": 2}))["valeur_exacte"]) == F(1, 4)


def _verif_taux_moyen(m):
    assert m.taux_moyen_rang_exact(300, 3) == F(3, 301)


def _verif_lecture_D_M16(m):
    entrees = {t["id"]: t for t in m.temoins_imposes_en_entree()}
    assert m.recalculer_temoin(entrees["T02"])["issue_recalculee"] == "tient"
    assert m.recalculer_temoin(entrees["T07"])["issue_recalculee"] == "morte_sans_gain"


def _verif_reseau_seuil(m):
    r = m.recalculer_temoin(T(regle={"type": "seuil_fixe", "valeur": 1}, lois={"lecture": arrondi(N01, 1)}))
    assert abs(r["quantites"]["taux_moyen"]["valeur"] - phibar(1.5)) < 1e-12


def _verif_reseau_atome(m):
    loi = arrondi(N01, 1)
    r = m.recalculer_temoin(T(n=1, lois={"calibration": loi, "lecture": loi}))
    assert abs(r["valeur_vraie"] - phibar(1.5)) < 1e-12
    # Tout sur le même réseau, un décalage d'un atome n'est qu'un réétiquetage (mutant équivalent) : il se
    # voit contre une calibration continue. Lecture sur réseau, g* = 2 ; calibration N(0,1), n = 1 :
    # couverture = P(Y >= 2) = Φ̄(2).
    r = m.recalculer_temoin(T(n=1, lois={"calibration": N01, "lecture": loi}))
    assert abs(r["valeur_vraie"] - phibar(2.0)) < 1e-12


def _verif_queue(m):
    assert m.queue_binomiale_exacte(3, F(1, 10), 2) == F(28, 1000)


def _verif_ecart_structurel(m):
    entrees = {t["id"]: t for t in m.temoins_imposes_en_entree()}
    assert m.recalculer_temoin(entrees["T07"])["issue_recalculee"] == "morte_sans_gain"


MUTATIONS_DE_CALCUL = [
    ("plafond_du_quantile_en_flottant", "    j = -((-n * niveau.numerator) // niveau.denominator)\n",
     "    j = math.ceil(n * float(niveau))\n", _verif_quantile),
    ("niveau_atteint_au_lieu_de_strictement_sous", "            if queue * niveau.denominator < borne:\n",
     "            if queue * niveau.denominator <= borne:\n", _verif_strict),
    ("valeur_p_du_mauvais_cote", "            queue += math.comb(t, j) * c ** j * e ** (t - j)\n",
     "            queue += math.comb(t, j) * e ** j * c ** (t - j)\n", _verif_cote),
    ("pari_strictement_au_dessus", "        return p_a1[k] * p_a0[t - k] * s_den >= s_num * p_b1[k] * p_b0[t - k]\n",
     "        return p_a1[k] * p_a0[t - k] * s_den > s_num * p_b1[k] * p_b0[t - k]\n", _verif_pari),
    ("taux_moyen_sur_n", "    return Fraction(k, n + 1)\n", "    return Fraction(k, n)\n", _verif_taux_moyen),
    ("sans_gain_pour_la_base_aussi", 'IDS_LUS_SANS_GAIN = frozenset({"T05", "T07"})',
     'IDS_LUS_SANS_GAIN = frozenset({"T02", "T05", "T07"})', _verif_lecture_D_M16),
    ("sans_gain_retire_a_T07", 'IDS_LUS_SANS_GAIN = frozenset({"T05", "T07"})',
     'IDS_LUS_SANS_GAIN = frozenset({"T05"})', _verif_lecture_D_M16),
    ("alerte_large_sur_reseau", '        """P(X > x) = P(indice >= ⌊x/pas⌋ + 1)."""\n        m, _r = self._indice_plancher(x)\n        return self.base.sf((m + 0.5) * self.pas_f)\n',
     '        """P(X > x) = P(indice >= ⌊x/pas⌋ + 1)."""\n        m, _r = self._indice_plancher(x)\n        return self.base.sf((m - 0.5) * self.pas_f)\n', _verif_reseau_seuil),
    ("alerte_large_sur_atome", "    return arrondie.base.sf((m + 0.5) * arrondie.pas_f)\n",
     "    return arrondie.base.sf((m - 0.5) * arrondie.pas_f)\n", _verif_reseau_atome),
    ("queue_binomiale_decalee", "        dessous = sum(math.comb(n, j) * a ** j * c ** (n - j) for j in range(k))\n",
     "        dessous = sum(math.comb(n, j) * a ** j * c ** (n - j) for j in range(k + 1))\n", _verif_queue),
    ("ecart_a_la_base_calcule_en_flottants", "                ecarts_base[nom] = Encadre.exact(Fraction(0))\n",
     "                ecarts_base[nom] = puissances[nom].moins(esperance_rang(n, 1, calib, sab))\n", _verif_ecart_structurel),
]


@pytest.mark.parametrize("nom,ancien,nouveau,verif", MUTATIONS_DE_CALCUL, ids=[m[0] for m in MUTATIONS_DE_CALCUL])
def test_mutation_de_calcul(nom, ancien, nouveau, verif):
    assert SOURCE.count(ancien) == 1, nom
    verif(P)
    mutant = charger(SOURCE.replace(ancien, nouveau), nom=f"mutant_{nom}")
    try:
        verif(mutant)
        detecte = False
    except Exception:
        detecte = True
    assert detecte, f"mutation {nom} non détectée"
