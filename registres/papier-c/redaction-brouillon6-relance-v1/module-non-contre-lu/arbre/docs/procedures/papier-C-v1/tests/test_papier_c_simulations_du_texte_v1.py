"""Essais du module que le texte r1 écrit lui-même (R5), sur données simulées : loi nette du témoin et contrôles de
l'artefact (point 8 bis, lignes 733 à 748) ; règle conjointe de C-P1 ; statistiques de rang aux trois lectures ; niveau
réel des queues des intervalles BCa (point 11, lignes 768 à 774).

Tailles. Les nombres d'essais sont ceux du texte (200, 300, 1 000) ; le texte ne fixe pas le nombre de tirages par
essai : `TIRAGES` = 1 000. Les seuils sont ceux du texte, appliqués tels quels ; les graines sont fixées d'avance, une
par essai, et n'ont pas été choisies sur une issue. Durée : environ neuf minutes sur un processeur. Une première passe
à effectifs réduits (150 et 300 essais) a donné deux taux à la limite de leur seuil (0,100 pour un seuil « au-dessus
de 0,10 » ; 0,053 pour un seuil de 0,05) : aux nombres d'essais du texte, les sept essais passent (journal du module).
Pour un tour rapide des autres essais, `PAPIER_C_SANS_SIMULATIONS=1` saute ce fichier, et le dit (essais comptés
« sautés », jamais « passés »). Point ouvert PO-37 : modèles S5 et S6 de la contre-lecture de méthode non fournis.
"""
import os

import numpy as np
import pytest

from papier_c_lois_v1 import loi_nette
from papier_c_rangs_v1 import TOUTES_LES_LECTURES, c_p3a_lecture, c_p3b_lecture
from papier_c_reechantillonnage_v1 import (clopper_pearson, comptes_par_grappes, effectif_efficace, holm, intervalle_bca,
                                           p_inferieur, p_superieur, poids_jackknife)
from papier_c_sondes_v1 import gain_d_ecart, taux_d_alarme
from simulation_papier_c_v1 import FAMILLES, appariement, corpus_A, corpus_B, juge

pytestmark = pytest.mark.skipif(os.environ.get("PAPIER_C_SANS_SIMULATIONS") == "1",
                                reason="simulations du texte sautées à la demande (PAPIER_C_SANS_SIMULATIONS=1)")
TIRAGES = 1000
UN = lambda n: np.ones((1, n))


def _delta(j, f):
    return j["familles"][f]["v"] - np.stack([j["temoins"][t] for t in j["familles"][f]["temoins"]])


def _temoins(j):
    return np.stack([j["temoins"][t] for t in sorted(j["temoins"])])


def _lois(j, P, v_etoile, lecture):
    W = _temoins(j)
    return [loi_nette(P, j["v0"], _delta(j, f), W, v_etoile, lecture) for f in FAMILLES]


def test_sans_attaque_part_des_familles_positives_au_plus_0_05(cfg):
    """Sans attaque (interaction d'écart type 0,4 ; 60 tâches ; 200 essais) : part des familles déclarées positives
    ≤ 0,05 (Holm sur les cinq familles du juge, seuil 0,025)."""
    rng = np.random.default_rng(20261119_1)
    paires, essais, positives = appariement(cfg), 200, []
    for _ in range(essais):
        A = corpus_A(rng, 60)
        P = comptes_par_grappes(A["grappes"], TIRAGES, rng)
        for _j in range(3):
            j = juge(rng, A, 0.4, 0.4, 0.0, np.zeros((5, 3)), 1.0, paires)
            p = [p_superieur(l["G"], 0.0) for l in _lois(j, P, 0.0, "calibree")]
            positives += [x <= 0.025 for x in holm(p)]
    part = float(np.mean(positives))
    print(f"\n[sans attaque] essais {essais}, tirages {TIRAGES} : part des familles positives {part:.4f}")
    assert part <= 0.05


def test_lambda_egal_un_mediane_calibree_et_artefact_sans_calibrage(cfg):
    """Avec λ = 1 et g = 0,10, à interaction 0,4 et 0,6, médiane de λ̂ dans [0,9 ; 1,1] ; la même loi sans calibrage,
    à 0,6, hors de [0,9 ; 1,1] (contrôle de l'artefact). 200 essais, 60 tâches."""
    rng = np.random.default_rng(20261119_2)
    paires, essais = appariement(cfg), 200
    gains = 0.10 * np.ones((5, 1)) * np.array([0.5, 1.0, 1.5])[None, :]
    medianes = {}
    for sig in (0.4, 0.6):
        cal, brut = [], []
        for _ in range(essais):
            A = corpus_A(rng, 60)
            for _j in range(3):
                j = juge(rng, A, sig, sig, 0.0, gains, 1.0, paires)
                cal += [float(l["lam"][0]) for l in _lois(j, UN(120), 0.0, "calibree")]
                brut += [float(l["lam"][0]) for l in _lois(j, UN(120), 0.0, "sans_calibrage")]
        medianes[sig] = (float(np.median(cal)), float(np.median(brut)))
    print(f"\n[λ = 1] médianes (calibrée, sans calibrage) : {medianes}")
    assert 0.9 <= medianes[0.4][0] <= 1.1 and 0.9 <= medianes[0.6][0] <= 1.1
    assert not 0.9 <= medianes[0.6][1] <= 1.1                              # sans calibrage : l'artefact se voit


def _regle_conjointe(cfg, rng, s0, sig, kap, g, lam, T, essais):
    paires = appariement(cfg)
    gains = g * np.ones((5, 1)) * np.array([0.5, 1.0, 1.5])[None, :]
    r = {(l, d): [] for l in ("cal", "brut", "conj") for d in ("cible", "moy")}
    for _ in range(essais):
        A = corpus_A(rng, T)
        P = comptes_par_grappes(A["grappes"], TIRAGES, rng)
        for _j in range(3):
            j = juge(rng, A, s0, sig, kap, gains, lam, paires)
            cal, brut = _lois(j, P, 0.0, "calibree"), _lois(j, P, 0.0, "sans_calibrage")
            for a, b in zip(cal, brut):                                    # par couple juge × famille, sans Holm
                cc, cb = p_superieur(a["lam"], 0.5) <= 0.025, p_superieur(b["lam"], 0.5) <= 0.025
                mc, mb = p_inferieur(a["lam"], 0.5) <= 0.025, p_inferieur(b["lam"], 0.5) <= 0.025
                for cle, v in ((("cal", "cible"), cc), (("brut", "cible"), cb), (("conj", "cible"), cc and cb),
                               (("cal", "moy"), mc), (("brut", "moy"), mb), (("conj", "moy"), mc and mb)):
                    r[cle].append(v)
    return {k: float(np.mean(v)) for k, v in r.items()}


@pytest.mark.parametrize("nom, s0, sig, kap", [("erreur d'insertion sur v0", 0.4, 0.4, 0.0),
                                               ("v0 exact et compression 0,16", 0.0, 0.4, 0.16)])
def test_regle_conjointe_a_la_frontiere(cfg, nom, s0, sig, kap):
    """Règle conjointe de C-P1, à la frontière λ = 0,5, g = 0,10, 45 tâches, 300 essais, sous les deux modèles :
    « vers la cible » et « vers la moyenne » au plus 0,05 chacun (taux par couple juge × famille, sans Holm)."""
    essais = 300
    r = _regle_conjointe(cfg, np.random.default_rng(20261119_3 + int(100 * kap)), s0, sig, kap, 0.10, 0.5, 45, essais)
    print(f"\n[frontière, {nom}] essais {essais} : {r}")
    assert r[("conj", "cible")] <= 0.05 and r[("conj", "moy")] <= 0.05


def test_controles_de_l_artefact_de_la_regle_conjointe(cfg):
    """Contrôles de l'artefact, 60 tâches, g = 0,20, 300 essais, à la frontière λ = 0,5 : sous le modèle v₀ exact et
    compression κ = 0,16, la lecture calibrée seule donne « vers la moyenne » au-dessus de 0,10 ; sous le modèle erreur
    sur v₀ d'écart type 0,6, la lecture sans calibrage seule donne « vers la cible » au-dessus de 0,08 ; la règle
    conjointe reste au plus 0,05 dans les deux."""
    essais = 300
    d = _regle_conjointe(cfg, np.random.default_rng(20261119_5), 0.0, 0.4, 0.16, 0.20, 0.5, 60, essais)
    s = _regle_conjointe(cfg, np.random.default_rng(20261119_6), 0.6, 0.6, 0.0, 0.20, 0.5, 60, essais)
    print(f"\n[artefact] essais {essais} ; compression : {d} ; erreur sur v0 : {s}")
    assert d[("cal", "moy")] > 0.10 and s[("brut", "cible")] > 0.08
    assert max(d[("conj", "cible")], d[("conj", "moy")], s[("conj", "cible")], s[("conj", "moy")]) <= 0.05


def test_statistiques_de_rang_trois_lectures_et_artefact_a_deux_lectures(cfg):
    """Statistiques de rang, trois lectures : juges aux modèles d'erreur différents (erreur sur v₀ d'écart type 0,6 ;
    erreur 0,4 et compression 0,08 ; compression 0,16), même gain vrai g = 0,20, k = 5, 60 tâches, 1 000 essais :
    C-P3a et C-P3b « établie » au plus 0,06 chacun ; aux deux premières lectures seules, au-dessus de 0,10."""
    rng = np.random.default_rng(20261119_7)
    essais = 1000
    paires = appariement(cfg, (1, 4, 8, 12, 16))
    gains = 0.20 * np.ones((5, 1)) * np.array([0.5, 0.75, 1.0, 1.25, 1.5])[None, :]
    modeles = [(0.6, 0.6, 0.0), (0.4, 0.4, 0.08), (0.0, 0.4, 0.16)]
    compte = {"a3": 0, "a2": 0, "b3": 0, "b2": 0}
    for _ in range(essais):
        A, Bc = corpus_A(rng, 60), corpus_B(rng)
        PA, PB = comptes_par_grappes(A["grappes"], TIRAGES, rng), comptes_par_grappes(Bc["grappes"], TIRAGES, rng)
        JA = [juge(rng, A, s0, sig, kap, gains, 1.0, paires) for s0, sig, kap in modeles]
        JB = [juge(rng, Bc, s0, sig, kap, gains, 1.0, paires) for s0, sig, kap in modeles]
        a, b = [], []
        for lecture in TOUTES_LES_LECTURES:
            def G(juges, P, v_etoile):
                return np.moveaxis(np.array([[l["G"] for l in _lois(j, P, v_etoile, lecture)] for j in juges]), 0, 1)
            GA, GAb = G(JA, UN(120), 0.0)[:, :, 0], np.moveaxis(G(JA, PA, 0.0), -1, 0)
            GB, GBb = G(JB, UN(30), 9.0)[:, :, 0], np.moveaxis(G(JB, PB, 9.0), -1, 0)
            a.append(c_p3a_lecture(GA, GAb)["conclut"])
            b.append(c_p3b_lecture(GA, GAb, GB, GBb)["conclut"])
        compte["a3"] += all(a)
        compte["a2"] += all(a[:2])
        compte["b3"] += all(b)
        compte["b2"] += all(b[:2])
    taux = {k: v / essais for k, v in compte.items()}
    print(f"\n[rang] essais {essais} : {taux}")
    assert taux["a3"] <= 0.06 and taux["b3"] <= 0.06
    assert taux["a2"] > 0.10 and taux["b2"] > 0.10                         # contrôle de l'artefact


def mesure_des_queues_bca(graine: int = 20261119_8, essais: int = 1000, taches: int = 30, tirages: int = TIRAGES) -> dict:
    """Niveau réel des queues à 2,5 % et 1,25 % des bornes de la réfutation de C-P2 (borne haute de Ḡ net), de C-P4
    (gain d'écart brut, champs seuls, deux côtés) et de C-P5 (borne par rééchantillonnage des tâches), 30 tâches, 1 000
    essais. Modèles simulés par ces essais (ceux de la contre-lecture de méthode, S5 et S6, ne sont pas dans les pièces
    reçues : point ouvert PO-37). Rend les taux de dépassement de chaque queue."""
    rng = np.random.default_rng(graine)
    gains = 0.10 * np.ones((5, 1)) * np.array([0.5, 1.0, 1.5])[None, :]
    paires = {f: [1, 8, 16] for f in FAMILLES}
    hors = {(s, q): 0 for s in ("C-P2", "C-P4", "C-P5") for q in ("2,5 % haute", "2,5 % basse", "1,25 % haute", "1,25 % basse")}
    vrai_taux = 0.93
    for _ in range(essais):
        A = corpus_A(rng, taches)
        g = A["grappes"]
        P, J = comptes_par_grappes(g, tirages, rng), poids_jackknife(g)
        j = juge(rng, A, 0.4, 0.4, 0.0, gains, 1.0, paires)
        f = FAMILLES[0]
        W, D = _temoins(j), _delta(j, f)
        stat = lambda Q: loi_nette(Q, j["v0"], D, W, 0.0)["G"]
        cellules = {"H": rng.normal(2, 0.5, taches)}
        cellules["S"] = cellules["H"] + 2.0 + rng.normal(0, 0.5, taches)
        SP = (cellules["S"] - 0.2 + rng.normal(0, 0.5, taches))[None, :]             # gain vrai 0,10
        PT, JT = P[:, ::2], J[:, ::2]
        gain = lambda Q: gain_d_ecart(Q, cellules["H"], cellules["S"], cellules["H"][None, :], SP)["G_brut"]
        tt, to = np.repeat(np.arange(taches), 8), np.repeat(np.arange(taches), 6)
        temoins = rng.normal(1.0, 0.8, tt.size)
        seuil_fixe = 1.0 + 0.8 * 1.6449
        p_t = np.clip(vrai_taux + rng.normal(0, 0.04, taches), 0, 1)                # détection variable par tâche
        ordres = np.where(rng.random(to.size) < p_t[to], seuil_fixe + 3.0, seuil_fixe - 3.0)
        alarme = lambda Q: taux_d_alarme(Q, temoins, tt, ordres, to)["taux"]
        for nom, s, P_, J_, vrai in (("C-P2", stat, P, J, 0.10), ("C-P4", gain, PT, JT, 0.10), ("C-P5", alarme, PT, JT, None)):
            obs, tir, jack = float(s(np.ones((1, P_.shape[1])))[0]), s(P_), s(J_)
            if vrai is None:
                vrai = float(np.mean(p_t))
            for niveau, q in ((0.95, "2,5 %"), (0.975, "1,25 %")):
                ic = intervalle_bca(obs, tir, jack, niveau)
                hors[(nom, f"{q} haute")] += vrai > ic["haut"]
                hors[(nom, f"{q} basse")] += vrai < ic["bas"]
    return {k: v / essais for k, v in hors.items()}


def test_niveau_reel_des_queues_du_bca():
    """Point 11 : niveau réel des queues à 2,5 % et 1,25 % au plus le double du nominal ; sinon l'effectif minimal
    passe à 90 contenus (45 tâches). L'issue de cet essai est l'entrée `test_bca_reussi` de la dérivation : un échec
    ici n'est pas un défaut du code, il commande la liste d'effectifs {90, 120}."""
    essais = 1000
    taux = mesure_des_queues_bca(essais=essais)
    print(f"\n[queues du BCa] essais {essais} : " + " ; ".join(f"{s} {q} : {v:.4f}" for (s, q), v in taux.items()))
    # bornes de la réfutation : borne haute pour C-P2 ; les deux côtés pour C-P4 et C-P5
    for (stat, queue), v in taux.items():
        if stat == "C-P2" and "basse" in queue:
            continue
        assert v <= 2 * (0.025 if queue.startswith("2,5") else 0.0125), (stat, queue, v)
