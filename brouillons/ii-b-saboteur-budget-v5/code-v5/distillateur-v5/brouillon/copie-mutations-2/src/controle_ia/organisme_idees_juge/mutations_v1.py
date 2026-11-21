"""Banc de mutations exigé par l'étape 0 du texte scellé. Chaque mutation est appliquée en mémoire (remplacement d'une
fonction du code, jamais d'un fichier), jouée sur un scénario, et doit être **tuée pour la raison attendue** : la garde
(ou la lecture) qui l'arrête doit être celle que le texte nomme. Une mutation survivante, ou tuée pour une autre raison,
dit « pas de jeu ».

Scénarios : (a) trajectoires d'essai construites (24 × 32, sans le juge) pour les règles des bras, la valeur e et e-BH ;
(b) une génération du banc, racine d'essai `RACINE_ESSAI` (jamais celle du texte), pour le gel, les flux et l'oracle ;
(c) le jeu d'essai synthétique de 20 000 générations, graines `(97, g)` de la racine du jeu, pour la mutation « valeur e
lue au maximum de la trajectoire » (réserve (a) de la Métrique).
"""
from __future__ import annotations

import hashlib
from contextlib import contextmanager
from unittest import mock

import numpy as np

from ..gardes import GardeArret
from . import banc_tirages_repartis_v1 as B
from . import execution_v1 as X
from . import juge_v1
from . import oracle_v1 as O
from . import rejeu_v1 as R
from . import synthetique_v1 as S

RACINE_ESSAI = B.racine_de(hashlib.sha256(b"banc de mutations, idee 1.2, v1 (racine d'essai, jamais celle du jeu)").hexdigest())


def trajectoires_essai(graine: int = 12) -> list[list[float]]:
    """24 trajectoires de 32 instants qui exercent chaque règle : arrêt haut à 25, arrêt bas à 50, valeur basse à 25
    puis remontée (piège de l'arrêt bas avant 50 tirages), cartes indécises qui atteignent le plafond, marches au hasard."""
    rng = np.random.default_rng(graine)
    lw = np.cumsum(rng.normal(-0.05, 0.6, (24, 32)), axis=1)
    lw[0] = 6.5 + np.arange(32) * 0.1                     # haut dès 25
    lw[1] = np.r_[-1.0, -3.5, np.linspace(-3.6, -5, 30)]  # bas à 50
    lw[2] = np.r_[-3.2, -1.0, np.linspace(-0.9, 0.5, 30)] # sous 1/20 à 25 seulement : ne doit pas s'arrêter
    lw[3] = np.r_[np.linspace(0.0, 5.0, 16), 6.3, np.linspace(6.4, 7.0, 15)]  # haut à 425
    for i in (4, 5):
        lw[i] = 0.2 * np.sin(np.arange(32))                # indécises : restent actives jusqu'au plafond
    for i in range(6, 24):
        lw[i] = np.minimum(lw[i], 2.0) - 3.5               # la plupart s'arrêtent bas tôt (budget libéré)
        lw[i, 0] = -0.5
    return [[round(float(v), 6) for v in ligne] for ligne in lw]


def evaluations_lentes() -> dict:
    """24 cartes indécises (aucun arrêt) : A épuise le budget au tour 8 ; un A qui ignore le budget le dépasse."""
    lw = [[round(0.2 * float(np.sin(k + i)), 6) for k in range(32)] for i in range(24)]
    return {i: B.EvaluationFiltree(t) for i, t in enumerate(lw)}


def evaluations_essai(graine: int = 12) -> dict:
    return {i: B.EvaluationFiltree(t) for i, t in enumerate(trajectoires_essai(graine))}


def positions_essai() -> list[int]:
    return [int(p) for p in np.random.default_rng(5).permutation(24)]


def _jouer_tous(J, evaluations=None, familles=("N",)):
    ev = evaluations or evaluations_essai()
    pos = positions_essai()
    for f in familles:
        R.rejouer_generation(J, ev, pos, RACINE_ESSAI, f, 0)


def _tuee(scenario, attendue: str) -> dict:
    try:
        scenario()
    except GardeArret as e:
        msg = str(e)
        return {"tuee": attendue in msg, "raison": msg[:300], "attendue": attendue}
    except Exception as e:  # noqa: BLE001 — une autre exception n'est pas « la raison attendue »
        return {"tuee": False, "raison": f"{type(e).__name__}: {e}"[:300], "attendue": attendue}
    return {"tuee": False, "raison": "aucun arrêt : la mutation survit", "attendue": attendue}


# --- mutants ---------------------------------------------------------------------------------------------------------
def _G_qui_lit_le_bloc_suivant(vues, positions, budget, rng=None):
    for i in R.ordre_du_tour(positions, 0):
        for _ in range(2):
            R.donner(vues[i], budget)
    while budget.reste > 0:
        c = [i for i in range(24) if not R.arretee_haut(vues[i]) and vues[i].n < R.NB]
        if not c:
            return
        j = max(c, key=lambda i: vues[i].lire(vues[i].n))  # lit l'instant que le bloc suivant révélerait
        R.donner(vues[j], budget)


def _donner_sans_budget(v, budget):
    v.reveler()


def _A_sans_budget(vues, positions, budget, rng=None):
    """A qui continue les tours tant qu'il reste des actives, sans regarder le budget restant."""
    tour = 0
    while True:
        actives = [i for i in R.ordre_du_tour(positions, tour) if R.active(vues[i]) and vues[i].n < R.NB]
        if not actives:
            return
        for i in actives:
            R.donner(vues[i], budget)
        tour += 1


def _arretee_bas_des_25(v):
    return any(x < R.SEUIL_BAS for x in v.revelees())


def _A_sans_plafond(vues, positions, budget, rng=None):
    R._tours(vues, positions, budget, 10 ** 6, 0, R.active)


def _placebo_tire_des_issues(racine, f, g):
    # stand-in d'un générateur dérivé des issues (ici : des trajectoires d'essai), au lieu de la graine (f, g, 1000)
    h = hashlib.sha256(repr(trajectoires_essai()).encode()).digest()
    return np.random.default_rng(int.from_bytes(h[:8], "big"))


def _ebh_m_apres_coup(J, revelees_par_carte):
    gardees = {f"c{i:02d}": {"verdict_final": "survit" if any(v >= R.SEUIL_PROMUE_SEULE for v in rev) else "eliminee",
                             "motif": "", "pari": {"trajectoire_log_w": list(rev)}}
               for i, rev in enumerate(revelees_par_carte)
               if not any(x < R.SEUIL_BAS for k, x in enumerate(rev) if k >= 1)}
    res = J.cycle.appliquer_multiplicite(gardees, R.ALPHA)  # m compté après coup (cartes non arrêtées bas)
    promues = sorted(int(n[1:]) for n in res["retenues"])
    log_e = {int(n[1:]): it["pari"]["multiplicite"]["log_e"] for n, it in gardees.items()}
    return promues, res["m"], log_e


def _F_lu_sur(champ):
    def jouer(J, nom, evaluations, positions, racine, f, g):
        if nom == "F":
            _ = [evaluations[i][champ] for i in range(24)]
        return VRAI_JOUER_BRAS(J, nom, evaluations, positions, racine, f, g)
    return jouer


VRAI_JOUER_BRAS = R.jouer_bras


def _pipeline_tire_avant_gel(J, gen):
    gen.preparer_engagements(J)
    gen.tirer_frais(J)
    gen.geler()
    return gen.evaluer(J)


def _preparer_avec_issues_fraiches(self, J):
    # bâtit les engagements en lisant les issues fraîches (marginale d'entraînement prise sur elles)
    ys = [self.ouvrir_flux_frais(c.indice).random(B.N_MAX) for c in self.cartes]
    for c, u in zip(self.cartes, ys):
        rng = B.generateur(self.racine, self.f, self.g, c.indice, 1)
        Zp, Gp = B.tirer_instances_np(rng, B.N_MAX)
        plan = B.instances_dicts(Zp, Gp)
        q = J.controles_pari._frequences([int(x * 3) for x in u[:100]], B.K)
        gele, _ = B.construire_engagement(J, f"m-{c.indice}", c.loi, plan, q, self.archive)
        self.engagements[c.indice] = gele
        self.plans[c.indice] = {"plan": plan, "q_ent": q}
    self.etat = "engagements"


# --- banc -------------------------------------------------------------------------------------------------------------
def banc(racine_jeu: int, generations_synthetiques: int = S.GENERATIONS, reechantillons: int = S.REECHANTILLONS) -> dict:
    """Joue chaque mutation ; rend {nom: {tuee, raison, attendue}} et le détail de l'épreuve synthétique."""
    J = juge_v1.charger()
    res = {}

    # sain d'abord : le scénario (a) passe sans mutation (sinon le banc ne prouve rien)
    _jouer_tous(J, familles=("N", "T"))

    res["la règle lit un instant non révélé"] = _tuee(
        lambda: _avec(mock.patch.dict(R.BRAS, {"G": (_G_qui_lit_le_bloc_suivant, R.BUDGET_BLOCS)}), lambda: _jouer_tous(J)),
        "instant non révélé")
    res["budget dépassé"] = _tuee(
        lambda: _avec(mock.patch.dict(R.BRAS, {"A": (_A_sans_budget, R.BUDGET_BLOCS)}), lambda: _jouer_tous(J, evaluations_lentes())),
        "tirages donnés > budget")
    res["garde du budget contournée (blocs révélés sans être comptés)"] = _tuee(
        lambda: _avec(mock.patch.object(R, "donner", _donner_sans_budget), lambda: _jouer_tous(J)), "garde du budget contournée")
    res["arrêt bas avant 50 tirages"] = _tuee(
        lambda: _avec(mock.patch.object(R, "arretee_bas", _arretee_bas_des_25), lambda: _jouer_tous(J)),
        "allocation non conforme")
    res["plafond ignoré"] = _tuee(
        lambda: _avec(mock.patch.dict(R.BRAS, {"A": (_A_sans_plafond, R.BUDGET_BLOCS)}), lambda: _jouer_tous(J)),
        "plafond de 800")
    res["hasard du placebo tiré des issues"] = _tuee(
        lambda: _avec(mock.patch.object(R, "generateur_placebo", _placebo_tire_des_issues), lambda: _jouer_tous(J)),
        "allocation non conforme")
    res["m compté après coup"] = _tuee(
        lambda: _avec(mock.patch.object(R, "promotions_ebh", _ebh_m_apres_coup), lambda: _jouer_tous(J)),
        "m compté après coup")
    for champ in ("promue", "t_promotion", "log_richesse_max", "log_richesse_arretee"):
        res[f"F lu sur le champ « {champ} » de l'évaluation à 800"] = _tuee(
            lambda c=champ: _avec(mock.patch.object(R, "jouer_bras", _F_lu_sur(c)), lambda: _jouer_tous(J)),
            f"champ « {champ} »")
    res["valeur e lue au maximum (garde de recoupement du rejeu)"] = _tuee(
        lambda: _avec(mock.patch.object(R, "log_valeur_e", S.maximum_de_la_trajectoire), lambda: _jouer_tous(J)),
        "valeur e lue par le juge")

    # scénario (b) : une génération du banc (racine d'essai)
    def gen():
        return B.Generation(RACINE_ESSAI, "T", 3)

    g_sain = gen()
    O.table_oracle(J, g_sain)                       # sain : l'oracle passe avant les issues fraîches
    g_sain.preparer_engagements(J); g_sain.geler(); g_sain.tirer_frais(J)

    def flux_partage():
        g = gen(); g.preparer_engagements(J); g.geler(); g.tirer_frais(J)
    res["flux d'issues partagé entre deux cartes"] = _tuee(
        lambda: _avec(mock.patch.object(B, "cle_flux_frais", lambda f, g, i: (f, g, 0, 2)), flux_partage), "flux d'issues fraîches partagé")
    res["issues fraîches tirées avant le gel"] = _tuee(lambda: _pipeline_tire_avant_gel(J, gen()), "avant le gel")

    def avec_issues():
        g = gen()
        _preparer_avec_issues_fraiches(g, J)
        g.geler()
    res["issues fraîches passées à la fonction qui bâtit un engagement"] = _tuee(avec_issues, "issue fraîche tirée avant le gel")

    def oracle_sur_jugees():
        g = gen(); g.preparer_engagements(J); g.geler(); g.tirer_frais(J)
        O.table_oracle(J, g)
    res["oracle calculé sur les issues jugées (après le tirage des issues fraîches)"] = _tuee(oracle_sur_jugees, "oracle demandé après")

    def oracle_echantillon_remplace():
        g = gen()
        ys = np.asarray(g_sain.issues[0] * 25, dtype=np.int64)[:B.ORACLE_N]
        g.echantillon = B.Echantillon(g.echantillon.Z, g.echantillon.G, ys, g.echantillon.cle,
                                      hashlib.sha256(ys.tobytes()).hexdigest())
        O.table_oracle(J, g)
    res["oracle calculé sur les issues jugées (échantillon remplacé)"] = _tuee(oracle_echantillon_remplace, "non tiré de sa graine")

    # scénario (c) : jeu synthétique, lecture (3)
    ep = S.epreuve_mutation_maximum(racine_jeu, generations_synthetiques, reechantillons)
    res["valeur e lue au maximum de la trajectoire (lecture (3), jeu synthétique)"] = {
        "tuee": bool(ep["mutation_tuee"]), "attendue": "borne basse de la moyenne mutée > 1",
        "raison": f"borne basse {ep['mute']['borne_basse']:.4f} (moyenne {ep['mute']['moyenne']:.4f}) ; lecture saine : "
                  f"moyenne {ep['sain']['moyenne']:.4f}, borne haute {ep['sain']['borne_haute']:.4f}"}
    return {"mutations": res, "synthetique": ep, "toutes_tuees": all(r["tuee"] for r in res.values()) and ep["sain_sous_un"],
            "racine_essai": str(RACINE_ESSAI)}


def _avec(patch, f):
    with patch:
        return f()


def exiger_toutes_tuees(rapport: dict) -> None:
    survivantes = [n for n, r in rapport["mutations"].items() if not r["tuee"]]
    if survivantes or not rapport["synthetique"]["sain_sous_un"]:
        raise GardeArret(f"mutation(s) survivante(s) ou tuée(s) pour une autre raison : {survivantes} : pas de jeu")
