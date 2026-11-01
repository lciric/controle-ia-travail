"""Blocs de la simulation d'essaim : comptes bruts par cellule, sans aucune lecture (la lecture gelée est
dans `lecture.py`).

Graines (R9) : une tâche nommée par usage, dérivée de l'entropie racine consignée au manifeste
(`manifeste.graines`). Chaque essaim reçoit un uniforme U de départage, tiré avec ses scores ; un essaim
attaqué de classe C garde le U de l'essaim honnête dont il est issu (nombres aléatoires communs), ce qui
rend exactes les vérifications trajectorielles de T1. Les cellules d'attaque sont indépendantes entre
elles et de l'échantillon des taux sous P₀.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import stats as sstats

from ..gardes import GardeArret
from ..manifeste import generateur
from ..simulation_t03.blocs import morceaux
from ..simulation_t03.lois import tirer
from . import calibrage as cal
from . import menaces as men
from . import references as ref
from . import statistiques as S

TOL_REL = 1e-9          # tolérance relative des vérifications trajectorielles numériques (× n₀)
TOL_SEUIL = 1e-9        # écart au seuil en deçà duquel une alarme est « à égalité » (exclue des discordances)


class Contexte:
    """Grille, graines du manifeste, seuils par configuration ; aucun état caché."""

    def __init__(self, grille: dict, graines: dict, suffixe: str = "", facteur_R: int = 1):
        self.grille = grille
        self.graines = graines
        self.alpha = float(grille["alpha"])
        self.q = float(grille["q"])
        self.u = cal.seuil_par_case(self.q)
        self.fractions = tuple(float(f) for f in grille["fractions_lambda"])
        self.gamma = float(grille["lecture"]["gamma"])
        self.suffixe = suffixe
        self.facteur_R = int(facteur_R)
        self.seuils: dict[str, dict[str, tuple[float, float]]] = {}
        self._rho: dict[str, float] = {}

    def rng(self, tache: str) -> np.random.Generator:
        nom = tache + self.suffixe
        if nom not in self.graines:
            raise GardeArret(f"tâche {nom!r} absente du manifeste (R9)")
        return generateur(self.graines[nom])

    def R(self, cle: str) -> int:
        return int(self.grille["tailles"][cle]) * self.facteur_R

    def dims(self, cfg: str) -> tuple[int, int]:
        if cfg not in self.grille["configs"]:
            raise GardeArret(f"configuration {cfg!r} absente de la grille")
        c = self.grille["configs"][cfg]
        K, T = int(c["K"]), int(c["T"])
        if K < 2 or T < 2:
            raise GardeArret(f"{cfg} : K = {K}, T = {T} (K ≥ 2 et T ≥ 2 requis)")
        return K, T

    def panneau(self, cfg: str) -> dict[str, str]:
        return self.grille["configs"][cfg]["panneau"]

    def params(self, cfg: str) -> dict:
        if cfg not in self._rho:
            K, T = self.dims(cfg)
            self._rho[cfg] = cal.rho_e_pas(K, T, self.alpha)
        return {"u": self.u, "q": self.q, "fractions": self.fractions, "rho": self._rho[cfg]}

    def seuil(self, cfg: str, alarme: str) -> tuple[float, float]:
        try:
            return self.seuils[cfg][alarme]
        except KeyError:
            raise GardeArret(f"seuil {alarme!r} non calibré pour {cfg!r}") from None


def loi_reference(K: int, T: int) -> dict:
    return {"type": "iid", "marginale": "gauss", "N": K, "T": T}


def tirer_essaims(g: np.random.Generator, r: int, loi: dict) -> tuple[np.ndarray, np.ndarray]:
    """Scores (r, K, T) puis uniformes de départage (r,), dans cet ordre (R9)."""
    Y = tirer(g, r, loi)
    return Y, g.random(r)


def alarmes(valeurs: dict, U, liste, ctx: Contexte, cfg: str) -> dict[str, np.ndarray]:
    return {a: cal.alarme(valeurs[S.nom_statistique(a)], U, ctx.seuil(cfg, a)) for a in liste}


def stats_de(liste) -> list[str]:
    return list(dict.fromkeys(S.nom_statistique(a) for a in liste))


# ---------------------------------------------------------------------------------------------
# Calibrage sous la loi de référence, taux sous P₀, garde, équivalence
# ---------------------------------------------------------------------------------------------
def calibrer(ctx: Contexte, cfg: str) -> dict:
    K, T = ctx.dims(cfg)
    n0 = K * T
    pan = ctx.panneau(cfg)
    exacts = cal.seuils_exacts(K, T, ctx.q, ctx.alpha)
    seuils = {}
    for a, genre in pan.items():
        s = S.nom_statistique(a)
        if genre == "exact":
            if s not in exacts:
                raise GardeArret(f"{cfg}/{a} : pas de seuil exact pour {s!r}")
            seuils[a] = exacts[s]
        elif genre == "ville":
            if not a.endswith("_ville"):
                raise GardeArret(f"{cfg}/{a} : seuil de Ville réservé aux alarmes « _ville »")
            seuils[a] = cal.seuil_ville(ctx.alpha)
        elif genre != "mc":
            raise GardeArret(f"{cfg}/{a} : genre de seuil {genre!r} inconnu")
    a_mc = [a for a, genre in pan.items() if genre == "mc"]
    if a_mc:
        g = ctx.rng(f"calib/{cfg}")
        valeurs = {s: [] for s in stats_de(a_mc)}
        for r in morceaux(ctx.R("R_cal"), n0):
            Y, _ = tirer_essaims(g, r, loi_reference(K, T))
            v = S.calculer(Y, list(valeurs), ctx.params(cfg))
            for s in valeurs:
                valeurs[s].append(v[s])
        for a in a_mc:
            seuils[a] = cal.seuil_mc(np.concatenate(valeurs[S.nom_statistique(a)]), ctx.alpha)
    non_finis = sorted(a for a, (c, _) in seuils.items() if not math.isfinite(c))
    if non_finis:
        raise GardeArret(f"{cfg} : seuils non finis {non_finis} (liste d'arrêt)")
    ctx.seuils[cfg] = seuils
    g0 = ctx.rng(f"p0/{cfg}")
    comptes = {a: 0 for a in pan}
    R0 = 0
    for r in morceaux(ctx.R("R0"), n0):
        Y, U = tirer_essaims(g0, r, loi_reference(K, T))
        al = alarmes(S.calculer(Y, stats_de(pan), ctx.params(cfg)), U, list(pan), ctx, cfg)
        for a in pan:
            comptes[a] += int(al[a].sum())
        R0 += r
    return {"cfg": cfg, "K": K, "T": T, "seuils": {a: list(t) for a, t in seuils.items()}, "genres": dict(pan),
            "R_cal": ctx.R("R_cal") if a_mc else 0, "R0": R0, "alarmes_p0": comptes, "rho": ctx.params(cfg)["rho"]}


def garde_p0(res: dict, alpha: float, gamma: float) -> list[str]:
    """Garde de calibrage (liste d'arrêt) : renvoie les manquements, vide si tout va bien.
    - seuil exact (taille α exacte, aléatoirisée si discrète) : α dans l'intervalle exact du taux ;
    - Monte-Carlo : |p̂₀ − α| ≤ z·√(α(1 − α)(1/R₀ + 1/R_cal)), z = Φ⁻¹(1 − γ/2) ;
    - Ville : borne basse de l'intervalle exact ≤ α."""
    manques = []
    R0, Rc = res["R0"], res["R_cal"]
    z = float(sstats.norm.isf(gamma / 2))
    for a, k in res["alarmes_p0"].items():
        genre = res["genres"][a]
        bas, haut = cal.intervalle_cp(k, R0, gamma)
        p = k / R0
        if genre == "mc" and Rc <= 0:
            manques.append(f"{res['cfg']}/{a} : seuil Monte-Carlo sans échantillon de calibrage")
        elif genre == "exact" and not (bas <= alpha <= haut):
            manques.append(f"{res['cfg']}/{a} : taux sous P₀ {p:.4f}, α hors de [{bas:.4f}, {haut:.4f}] (seuil exact)")
        elif genre == "mc" and abs(p - alpha) > z * math.sqrt(alpha * (1 - alpha) * (1 / R0 + 1 / Rc)):
            manques.append(f"{res['cfg']}/{a} : taux sous P₀ {p:.4f} ≠ α (seuil Monte-Carlo)")
        elif genre == "ville" and bas > alpha:
            manques.append(f"{res['cfg']}/{a} : taux sous P₀ {p:.4f} > α (Ville)")
    return manques


def equivalence(ctx: Contexte, cfg: str, n_essaims: int) -> dict:
    """Garde : statistiques vectorisées = références scalaires, essaim par essaim (écart relatif)."""
    K, T = ctx.dims(cfg)
    stats_ = stats_de(ctx.panneau(cfg))
    Y = tirer(ctx.rng(f"equivalence/{cfg}"), n_essaims, loi_reference(K, T))
    v = S.calculer(Y, stats_, ctx.params(cfg))
    ecarts = {}
    for s in stats_:
        r = np.array([ref.reference(s, Y[i], ctx.params(cfg)) for i in range(n_essaims)])
        ecarts[s] = float(np.max(np.abs(r - v[s]) / np.maximum(1.0, np.abs(r))))
    return {"cfg": cfg, "n_essaims": n_essaims, "ecart_relatif_max": ecarts}


# ---------------------------------------------------------------------------------------------
# Classe C : réarrangements par sous-groupe (HE1, HE2, HE5)
# ---------------------------------------------------------------------------------------------
def bloc_C(ctx: Contexte) -> dict:
    sortie = []
    for cfg, specs in ctx.grille["C"].items():
        K, T = ctx.dims(cfg)
        seuils = {a: ctx.seuil(cfg, a) for a in ctx.panneau(cfg)}
        for spec in specs:
            sortie.append(cellule_C(ctx, cfg, spec, loi_reference(K, T), seuils, f"C/{cfg}/{spec['nom']}"))
    return {"cellules": sortie}


def cellule_C(ctx: Contexte, cfg: str, spec: dict, loi: dict, seuils: dict, tache: str) -> dict:
    """Une cellule de classe C : essaims honnêtes Y de la loi, X = arrangement(Y) dans le groupe annoncé (garde),
    identité trajectorielle des statistiques invariantes, alarmes de X (départage : U de Y)."""
    K, T = ctx.dims(cfg)
    n0 = K * T
    pan = list(seuils)
    stats_ = stats_de(pan)
    p = ctx.params(cfg)
    groupe = spec["groupe"]
    inv_s = [s for s in stats_ if S.invariante(s, groupe)]
    inv_a = [a for a in pan if S.invariante(S.nom_statistique(a), groupe)]
    g = ctx.rng(tache)
    res = {"cfg": cfg, "K": K, "T": T, **spec, "R": 0, "alarmes": {a: 0 for a in pan},
           "valeurs_differentes": {s: 0 for s in inv_s}, "discordances": {a: 0 for a in inv_a}, "invariantes": inv_a}
    if spec["genre"] == "synchro":
        res.update({"viol_hors_synchro": 0, "viol_valeurs_hautes": 0, "viol_compte_pas": 0, "viol_borne_coelev": 0})
    for r in morceaux(ctx.R("R"), n0):
        Y, U = tirer_essaims(g, r, loi)
        X, info = men.arranger(spec, Y, g)
        men.exiger_groupe(X, Y, groupe, tache)
        vY, vX = S.calculer(Y, stats_, p), S.calculer(X, stats_, p)
        aY = {a: cal.alarme(vY[S.nom_statistique(a)], U, seuils[a]) for a in pan}
        aX = {a: cal.alarme(vX[S.nom_statistique(a)], U, seuils[a]) for a in pan}
        for s in inv_s:
            res["valeurs_differentes"][s] += int(np.count_nonzero(vX[s] != vY[s]))
        for a in inv_a:
            res["discordances"][a] += int(np.count_nonzero(aX[a] != aY[a]))
        for a in pan:
            res["alarmes"][a] += int(aX[a].sum())
        if spec["genre"] == "synchro":
            _verifier_synchro(res, X, Y, info, ctx.u, int(spec["r"]))
        res["R"] += r
    return res


def _verifier_synchro(res: dict, X, Y, info: dict, u: float, r_pas: int) -> None:
    """Vérifications trajectorielles de la synchronisation (sémantique de l'arrangement et borne de T3)."""
    R, K, T = Y.shape
    agents, pas = info["agents"], info["pas"]
    dans = np.zeros((R, K), dtype=bool)
    np.put_along_axis(dans, agents, True, axis=1)
    res["viol_hors_synchro"] += int(np.count_nonzero((X != Y).any(axis=2) & ~dans))
    rr = np.arange(R)[:, None]
    hauts_Y = np.sort(Y, axis=2)[:, :, -r_pas:]                               # (R, K, r)
    aux_pas = np.sort(np.take_along_axis(X, np.broadcast_to(pas[:, None, :], (R, K, r_pas)), axis=2), axis=2)
    res["viol_valeurs_hautes"] += int(np.count_nonzero((aux_pas != hauts_Y).any(axis=2) & dans))
    if r_pas == 1:
        s = pas[:, 0]
        compte = (X[rr[:, 0], :, s] >= u).sum(axis=1)                         # C_s(X)
        attendu = ((Y.max(axis=2) >= u) & dans).sum(axis=1) + ((Y[rr[:, 0], :, s] >= u) & ~dans).sum(axis=1)
        res["viol_compte_pas"] += int(np.count_nonzero(compte != attendu))
        res["viol_borne_coelev"] += int(np.count_nonzero(S.coelev_comptage(X, u) < compte))


# ---------------------------------------------------------------------------------------------
# Classe M : décalages à budget fixé (HE4, cas sain, L4)
# ---------------------------------------------------------------------------------------------
L4_STATS = ("somme", "pas_moyenne", "e_pas")
L4_ALARMES = ("somme", "pas_moyenne", "e_pas_ville")


def bloc_M(ctx: Contexte) -> dict:
    sortie = []
    for cfg, specs in ctx.grille["M"].items():
        K, T = ctx.dims(cfg)
        n0 = K * T
        pan = list(ctx.panneau(cfg))
        stats_ = stats_de(pan)
        p = ctx.params(cfg)
        manquantes = [a for a in L4_ALARMES if a not in pan]
        if manquantes and any(s["genre"] == "synchro" for s in specs):
            raise GardeArret(f"{cfg} : alarmes de L4 absentes du panneau {manquantes}")
        for spec in specs:
            genre, B, m = spec["genre"], float(spec["B"]), int(spec["m"])
            g = ctx.rng(f"M/{cfg}/{spec['nom']}")
            res = {"cfg": cfg, "K": K, "T": T, **spec, "R": 0, "alarmes": {a: 0 for a in pan}}
            if genre == "synchro":
                res.update({"L4_ecart_max": {s: 0.0 for s in L4_STATS}, "L4_discordances": {a: 0 for a in L4_ALARMES},
                            "L4_tolerance": TOL_REL * n0})
            for r in morceaux(ctx.R("R"), n0):
                Y, U = tirer_essaims(g, r, loi_reference(K, T))
                if genre == "synchro":
                    s_pas = g.integers(0, T, size=r)
                    ag = men.sous_ensemble(g, r, K, m)
                    D = men.decalages("synchro", K, T, B, m, r, g, pas_impose=s_pas, agents_imposes=ag)
                else:
                    D = men.decalages(genre, K, T, B, m, r, g)
                X = Y + D
                v = S.calculer(X, stats_, p)
                al = alarmes(v, U, pan, ctx, cfg)
                for a in pan:
                    res["alarmes"][a] += int(al[a].sum())
                if genre == "synchro":
                    X1 = Y + men.decalages("synchro_un", K, T, B, 1, r, g, pas_impose=s_pas, agents_imposes=ag)
                    v1 = S.calculer(X1, list(L4_STATS), p)
                    for st in L4_STATS:
                        res["L4_ecart_max"][st] = max(res["L4_ecart_max"][st], float(np.max(np.abs(v[st] - v1[st]))))
                    for a in L4_ALARMES:
                        st = S.nom_statistique(a)
                        c = ctx.seuil(cfg, a)[0]
                        a1 = cal.alarme(v1[st], U, ctx.seuil(cfg, a))
                        egalite = (np.abs(v[st] - c) <= TOL_SEUIL * n0) | (np.abs(v1[st] - c) <= TOL_SEUIL * n0)
                        res["L4_discordances"][a] += int(np.count_nonzero((al[a] != a1) & ~egalite))
                res["R"] += r
            sortie.append(res)
    return {"cellules": sortie}


# ---------------------------------------------------------------------------------------------
# HE3 : validité hors hypothèses, Ville contre calibrage sur essaims honnêtes entiers
# ---------------------------------------------------------------------------------------------
def bloc_HE3(ctx: Contexte) -> dict:
    g3 = ctx.grille["HE3"]
    conf = g3["conforme"]
    Kc, nt, Lc = int(conf["K"]), int(conf["n_test"]), int(conf["L"])
    sortie = []
    for cfg in g3["configs"]:
        K, T = ctx.dims(cfg)
        n0 = K * T
        p = ctx.params(cfg)
        liste = g3["alarmes"]
        for x in g3["lois"]:
            loi = {**x["loi"], "N": K, "T": T}
            g = ctx.rng(f"HE3/{cfg}/{x['nom']}/fa")
            comptes = {a: 0 for a in liste}
            R = 0
            for r in morceaux(ctx.R("R"), n0):
                Y, U = tirer_essaims(g, r, loi)
                al = alarmes(S.calculer(Y, stats_de(liste), p), U, liste, ctx, cfg)
                for a in liste:
                    comptes[a] += int(al[a].sum())
                R += r
            par_tirage = {s: [] for s in conf["statistiques"]}
            for l in range(Lc):
                gc = ctx.rng(f"HE3/{cfg}/{x['nom']}/conforme/{l}")
                Yc, Uc = tirer_essaims(gc, Kc, loi)
                Yt, Ut = tirer_essaims(gc, nt, loi)
                vc = S.calculer(Yc, conf["statistiques"], p)
                vt = S.calculer(Yt, conf["statistiques"], p)
                for s in conf["statistiques"]:
                    seuil = cal.seuil_conforme(vc[s], Uc, ctx.alpha)
                    par_tirage[s].append(int(cal.alarme_conforme(vt[s], Ut, seuil).sum()))
            sortie.append({"cfg": cfg, "K": K, "T": T, "loi_nom": x["nom"], "loi": loi, "R": R, "alarmes": comptes,
                           "conforme": {"K": Kc, "n_test": nt, "L": Lc, "alarmes_par_tirage": par_tirage,
                                        "taux_theorique": cal.taux_conforme(Kc, ctx.alpha)}})
    return {"cellules": sortie}


# ---------------------------------------------------------------------------------------------
# HE6 : synchronisation sous P₀ corrélée (copies à poids partagés), seuils calibrés sur essaims entiers
# ---------------------------------------------------------------------------------------------
def bloc_HE6(ctx: Contexte) -> dict:
    """Pour chaque loi corrélée : seuils Monte-Carlo aléatoirisés sur R_cal essaims honnêtes entiers de la loi,
    taux sous P₀ sur R₀ essaims indépendants (garde de la liste d'arrêt), puis cellules de synchronisation."""
    g6 = ctx.grille["HE6"]
    liste = list(g6["alarmes"])
    calibrages, sortie = [], []
    for cfg in g6["configs"]:
        K, T = ctx.dims(cfg)
        n0 = K * T
        p = ctx.params(cfg)
        stats_ = stats_de(liste)
        for x in g6["lois"]:
            loi = {**x["loi"], "N": K, "T": T}
            cle = f"HE6/{cfg}/{x['nom']}"
            g = ctx.rng(f"{cle}/calib")
            valeurs = {s: [] for s in stats_}
            for r in morceaux(ctx.R("R_cal"), n0):
                Y, _ = tirer_essaims(g, r, loi)
                v = S.calculer(Y, stats_, p)
                for s in stats_:
                    valeurs[s].append(v[s])
            seuils = {a: cal.seuil_mc(np.concatenate(valeurs[S.nom_statistique(a)]), ctx.alpha) for a in liste}
            g0 = ctx.rng(f"{cle}/p0")
            k0, R0 = {a: 0 for a in liste}, 0
            for r in morceaux(ctx.R("R0"), n0):
                Y, U = tirer_essaims(g0, r, loi)
                v = S.calculer(Y, stats_, p)
                for a in liste:
                    k0[a] += int(cal.alarme(v[S.nom_statistique(a)], U, seuils[a]).sum())
                R0 += r
            res_cal = {"cfg": cle, "loi": loi, "seuils": {a: list(t) for a, t in seuils.items()},
                       "genres": {a: "mc" for a in liste}, "R_cal": ctx.R("R_cal"), "R0": R0, "alarmes_p0": k0}
            manques = garde_p0(res_cal, ctx.alpha, ctx.gamma)
            if manques:
                raise GardeArret("garde de calibrage HE6 sous P₀ corrélée (liste d'arrêt) : " + " ; ".join(manques))
            calibrages.append(res_cal)
            for spec in g6["arrangements"]:
                res = cellule_C(ctx, cfg, spec, loi, seuils, f"{cle}/{spec['nom']}")
                sortie.append({**res, "loi_nom": x["nom"], "loi": loi, "alarmes_p0": k0, "R0": R0})
    return {"calibrages": calibrages, "cellules": sortie}


BLOCS = {"C": bloc_C, "M": bloc_M, "HE3": bloc_HE3, "HE6": bloc_HE6}
