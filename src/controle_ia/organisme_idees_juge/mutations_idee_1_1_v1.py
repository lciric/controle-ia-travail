"""Idée 1.1 — banc de mutations de l'étape 0 (préenregistrement scellé `3ffe1739…`, « Étapes », 0).

Chaque mutation est une altération du code (remplacement d'une fonction ou d'une constante, le temps d'un essai), un
détecteur et la raison attendue de sa mort. Le même détecteur, joué sans mutation, est le **cas sain** : il doit passer.
Une mutation « survit » si son détecteur passe sous elle, ou s'il échoue pour une autre raison que celle attendue.

Détecteurs : gardes de la liste d'arrêt (raison = message de la garde) ; seconde écriture indépendante (terme projeté,
règle de J9-D, part regagnée et lignes informatives, ici même) ; deux détecteurs statistiques à critères de mort écrits :
- « garde P4 retirée » : le **critère du texte** (`compter_garde_H7`) : sur 200 répétitions de H7 aux graines (97, k), le
  terme projeté sans garde promeut au moins 20 fois ; cas sain : sous gel, au plus 2 fois ;
- « certificat retiré, optimiseur à 3 pas » : au moins une promotion de J9-P sur les répétitions de Q8, Q1 et Q2 (le texte
  dit « doit faire promouvoir Q8 ou une copie » sans compte : 30 répétitions de chaque ligne, choix déclaré au rapport) ;
  cas sain : aucune promotion sur les copies Q1 et Q2 (Q8, cellule de taille, est seulement rapportée).
Graines : `(97, k)`, un k distinct par essai (`CLES`), écrit dans le fichier de l'étape 0.
"""
from __future__ import annotations

import contextlib
import copy
import traceback

import numpy as np

from ..gardes import GardeArret
from . import banc_idee_1_1_v1 as B
from . import lecture_idee_1_1_v1 as LE
from . import lois_v1 as Lv
from . import projection_bras_v1 as PB
from . import projection_commun_v1 as cm
from . import projection_methodes_v1 as me

# k des graines (97, k) des essais de l'étape 0 (liste inscrite à l'addendum) ; 1..99 réservés ici.
CLES = {"mutation_certificat": 1, "mutation_garde_acces": 2, "mutation_blocs": 3, "mutation_minimum": 4,
        "mutation_gel": 5, "mutation_w_reste": 6, "mutation_lineaire": 7, "mutation_coupures": 8, "mutation_tirages": 9,
        "mutation_avant_gel": 10, "mutation_t40": 11, "lecture_synthetique": 12, "garde_H7": 20, "garde_Hn": 21,
        "E9": 30, "ED": 31, "EP": 32, "chronometrage": 40}
N_H7 = 200
MORT_H7_SANS_GARDE, SAIN_H7_GEL = 20, 2        # critère de mort et cas sain écrits (texte, étape 0)
BLOCAGE_HN_GEL = 3                              # Hn sous gel : 3 promotions ou plus sur 200 bloquent le jeu
N_CERTIFICAT = 30


@contextlib.contextmanager
def remplacer(objet, nom, valeur):
    ancien = getattr(objet, nom)
    setattr(objet, nom, valeur)
    try:
        yield
    finally:
        setattr(objet, nom, ancien)


@contextlib.contextmanager
def aucune():
    yield


def attendre_garde(fonction, morceau: str) -> tuple[bool, str]:
    """(tuée, raison) : tuée si `fonction` lève `GardeArret` dont le message contient `morceau`."""
    try:
        fonction()
    except GardeArret as e:
        return (morceau in str(e)), f"GardeArret : {e}"
    except Exception as e:  # une autre exception n'est pas la raison attendue
        return False, f"{type(e).__name__} : {e}"
    return False, "aucune garde levée"


def _rep(V, racine, ligne: str, k: int, r: int = 0, **kw):
    return B.Repetition(V, racine, B.INDICE[ligne], 0, cle=(97, k, r), **kw)


def _jouer(V, racine, ligne, k, r=0):
    rep = _rep(V, racine, ligne, k, r)
    rep.geler()
    rep.tirer()
    return rep.evaluer()


# --- détecteurs (cas sain = détecteur sans mutation) ------------------------------------------------------------------
def det_certificat(V, racine, n=N_CERTIFICAT) -> dict:
    k = CLES["mutation_certificat"]
    comptes = {}
    for ligne in ("Q8", "Q1", "Q2"):
        comptes[ligne] = sum(bool(B.jouer_projection_seule(V, racine, B.INDICE[ligne], (97, k, B.INDICE[ligne], r))["J9-P"]["promue"])
                             for r in range(n))
    return {"comptes": comptes, "promotion": sum(comptes.values()) > 0, "copies": comptes["Q1"] + comptes["Q2"]}


def det_garde_acces(V, racine):
    k = CLES["mutation_garde_acces"]
    return attendre_garde(lambda: _jouer(V, racine, "Q1", k), "après la création du flux")


def det_blocs(V, racine):
    return attendre_garde(lambda: _jouer(V, racine, "Q1", CLES["mutation_blocs"]), "décalés")


def det_minimum(V, racine):
    return attendre_garde(lambda: _jouer(V, racine, "Q1", CLES["mutation_minimum"]), "seconde écriture")


def det_gel(V, racine):
    return attendre_garde(lambda: _jouer(V, racine, "Hs", CLES["mutation_gel"]), "bloc courant")


def det_w_reste(V, racine, n=3) -> tuple[bool, str]:
    """Carte membre de W^reste seulement (loi log-linéaire de S1 : puissance 2, inclinaison) : log W de J9-P ≤ 10⁻⁶ sous le
    code juste (W^reste borne la richesse) ; sous la mutation, le terme projeté seul la laisse monter."""
    k = CLES["mutation_w_reste"]
    pire = -np.inf
    for r in range(n):
        rep = _rep(V, racine, "Q9a", k, r)
        carte = Lv.transformee(copy.deepcopy(rep.archive["S1"]), 2.0, [0.5, -0.5, 0.0])
        rep.carte = rep.monde = rep.ligne.carte = rep.ligne.monde = carte
        rep.Mp = np.array([rep.J.sp.proba(carte, x, [], t) for t, x in enumerate(rep.plan)])
        rep.geler()
        rep.tirer()
        pire = max(pire, B.evaluer_projection_seule(rep)["J9-P"]["max"])
    return pire > 1e-6, f"log W maximal de J9-P sur une carte de W^reste : {pire!r}"


def det_lineaire(V, racine):
    return attendre_garde(lambda: _jouer(V, racine, "Q1", CLES["mutation_lineaire"]), "familles de J9-P")


def det_coupures(V, racine):
    return attendre_garde(lambda: _jouer(V, racine, "Q1", CLES["mutation_coupures"]), "coupures de l'archive")


def det_tirages(V, racine):
    return attendre_garde(lambda: _jouer(V, racine, "Q1", CLES["mutation_tirages"]), "issues différents de J9")


def det_avant_gel(V, racine):
    def f():
        rep = _rep(V, racine, "Q1", CLES["mutation_avant_gel"])
        B.ordre_du_jeu(rep)
    return attendre_garde(f, "avant le gel")


def det_t40(V, racine):
    return attendre_garde(lambda: _jouer(V, racine, "Q1", CLES["mutation_t40"]), "T₄₀")


def det_regle_j9d() -> tuple[bool, str]:
    """Seconde écriture : J9 promeut à T₈, le jumeau et la règle par membre non ⇒ J9-D promeut (réunion)."""
    lw9 = [0.0] * 7 + [B.SEUIL + 0.1]
    lw40 = [0.0] * 40
    par = {"m1": [B.SEUIL + 1.0] * 40, "m2": [0.0] * 40}
    d40, regle, dd = B.regle_j9d(lw9, lw40, par)
    ok = d40 and not regle and dd
    lw9b = [0.0] * 8
    d40b, regleb, ddb = B.regle_j9d(lw9b, lw40, {"m1": [B.SEUIL] * 40})
    ok = ok and (not d40b) and regleb and ddb
    return (not ok), f"règle de J9-D : {(d40, regle, dd, d40b, regleb, ddb)}"


# --- lecture : seconde écriture indépendante sur des données synthétiques -------------------------------------------
def donnees_synthetiques(racine: int, R: int = 300) -> dict:
    """Lignes V synthétiques (J8, J9, J9⁺, J9-P, La, Ld), paires discordantes de 0 à 60 sur R, dont des lignes au bord du
    seuil d'informativité ; J9⁺ diffère de J9 sur certaines lignes (I⁺ ≠ I)."""
    rng = B.generateur(racine, 97, CLES["lecture_synthetique"])
    d = {}
    for i, nom in enumerate(LE.V_TEXTE):
        a = (rng.random(R) < 0.5).astype(int)
        disc = int([0, 3, 9, 12, 14, 20, 30, 40, 60, 8, 11, 13, 25, 2, 16][i] * R / 1000 * 3.0)
        b = a.copy()
        idx = np.flatnonzero(a == 1)[:disc]
        b[idx] = 0
        bp = b.copy()
        bp[idx[: disc // 2]] = 1 if i % 3 == 0 else 0
        x = b.copy()
        x[idx[: max(0, disc // 2)]] = 1
        la = b.copy()
        la[idx[: max(0, (2 * disc) // 3)]] = 1
        ld = b.copy()
        ld[idx[: max(0, disc // 3)]] = 1
        d[nom] = [{"J8": {"promue": bool(a[r])}, "J9": {"promue": bool(b[r])}, "J9+": {"promue": bool(bp[r])},
                   "J9-P": {"promue": bool(x[r])}, "La": {"promue": bool(la[r])}, "Ld": {"promue": bool(ld[r])}} for r in range(R)]
    return d


def rho_independant(racine: int, d: dict, bras: list, plus: bool, B_: int, quantiles) -> dict:
    """Troisième écriture de ρ, de I et de son intervalle, en boucles simples (indépendante de la lecture gelée)."""
    from scipy.stats import beta
    lignes = list(LE.V_TEXTE)
    ref = "J9+" if plus else "J9"
    R = len(d[lignes[0]])
    A = np.array([[int(r["J8"]["promue"]) for r in d[l]] for l in lignes])
    Bm = np.array([[int(r[ref]["promue"]) for r in d[l]] for l in lignes])
    X = {x: np.array([[int(r[x]["promue"]) for r in d[l]] for l in lignes]) for x in bras}

    def I_de(a, b):
        out = []
        for k in range(len(lignes)):
            kk = int((a[k] - b[k]).sum())
            bas = 0.0 if kk == 0 else float(beta.ppf(0.05, kk, R - kk + 1))
            if bas >= 0.02:
                out.append(k)
        return out

    def rh(x, a, b, I):
        return sum((x[k] - b[k]).mean() for k in I) / sum((a[k] - b[k]).mean() for k in I)
    I = I_de(A, Bm)
    out = {"I": [lignes[k] for k in I]}
    if len(I) < 2:
        return out
    tirs = {x: [] for x in bras}
    for bb in range(B_):
        idx = B.generateur(racine, 99, bb).integers(0, R, size=(len(lignes), R))
        a = np.take_along_axis(A, idx, 1)
        b = np.take_along_axis(Bm, idx, 1)
        Ir = I_de(a, b)
        if len(Ir) < 2:
            continue
        for x in bras:
            tirs[x].append(rh(np.take_along_axis(X[x], idx, 1), a, b, Ir))
    for x in bras:
        out[x] = (rh(X[x], A, Bm, I), float(np.quantile(tirs[x], quantiles[0])), float(np.quantile(tirs[x], quantiles[1])))
    return out


def det_lecture(racine: int, B_: int = 200) -> tuple[bool, str]:
    d = donnees_synthetiques(racine)
    ecarts = []
    for plus, bras in ((False, ["J9-P", "La", "Ld"]), (True, ["J9-P"])):
        lu = LE.lire_rho(racine, d, bras, plus=plus, B_=B_)
        ind = rho_independant(racine, d, bras, plus, B_, LE.QUANTILES_PRIMAIRES)
        if lu["I"] != ind["I"]:
            ecarts.append(f"I{'⁺' if plus else ''} {lu['I']} ≠ {ind['I']}")
            continue
        if any(not l.startswith("V") for l in lu["I"]):
            ecarts.append("ligne Q dans I")
        for x in bras:
            e, lo, hi = ind[x]
            if abs(lu[x]["estimation"] - e) > 1e-12 or abs(lu[x]["bas"] - lo) > 1e-12 or abs(lu[x]["haut"] - hi) > 1e-12:
                ecarts.append(f"ρ de {x}{'⁺' if plus else ''} différent de la seconde écriture")
    return bool(ecarts), "; ".join(ecarts) or "lecture égale à la seconde écriture"


def _rho_numerateur_faux(x, a, b, I):
    return sum(float((a[k] - b[k]).mean()) for k in I) / sum(float((a[k] - b[k]).mean()) for k in I)


def _ordre_inverse(rep):
    rep.tirer()
    rep.geler()


# --- liste des mutations du texte (au moins celles-ci) -----------------------------------------------------------------
def mutations(V, racine):
    """[(nom, contexte de mutation, détecteur, raison attendue)] ; le détecteur rend (tuée, raison)."""
    tirer_orig = B.Repetition.tirer
    tirages_orig = B.Repetition.tirages_de
    processus_orig = PB.processus_j9p
    temoins_orig = B.Repetition._temoins

    def tirer_projection_apres(self):
        tirer_orig(self)
        self.Qp = np.eye(B.K)[np.asarray(self.issues)]      # projection calculée sur les issues du bloc
        self._projeter_au_gel()

    def tirer_avant_projection(self):                        # bloc tiré avant sa projection sous gel
        if self.etat != "gelee":
            raise GardeArret("état")
        self.flux_cree = True
        rng = B.generateur(self.racine, *self.cle, 1)
        self.flux = PB.FluxFrais(self._tireur(rng))
        self.proj_gel, self.Qg = {}, np.zeros((B.N, B.K))
        for b in range(PB.NB):
            self.flux.tirer_bloc(b)
            self._projeter_sous_gel(b)
        self.issues = self.flux.complet()
        self.etat = "tiree"

    def tirages_perturbes(self, quoi):
        t = tirages_orig(self, quoi)
        if quoi == "La":
            t["issues"] = [(y + 1) % B.K for y in t["issues"]]
        return t

    def processus_sans_lineaire(loge, z):
        p, n = processus_orig(loge, z)
        return p[1:], n[1:]

    def temoins_coupures_fraiches(self, rec):
        self.cA = (np.asarray(self.issues) == 0).astype(int)
        return temoins_orig(self, rec)

    def certificat_un(G, Wt, P, cells, C):
        return np.ones(cells.shape[0])

    @contextlib.contextmanager
    def certif_et_trois_pas():
        with remplacer(cm, "certificat_commun", certificat_un), remplacer(me, "IT_PROJ", 3), remplacer(me, "IT_CHAUD", 3):
            yield

    blocs_decales = [(int(a) + 1, int(e) + 1) for a, e in cm.BLOCS[:-1]] + [(176, 200)]

    return [
        ("certificat de bloc retiré, optimiseur réduit à 3 pas", certif_et_trois_pas,
         lambda: (lambda d: (d["promotion"], f"promotions {d['comptes']}"))(det_certificat(V, racine)),
         "au moins une promotion de J9-P sur Q8 ou une copie"),
        ("projection calculée sur les issues du bloc", lambda: remplacer(B.Repetition, "tirer", tirer_projection_apres),
         lambda: det_garde_acces(V, racine), "garde d'accès"),
        ("blocs décalés des instants", lambda: remplacer(cm, "BLOCS", blocs_decales), lambda: det_blocs(V, racine),
         "garde des blocs alignés"),
        ("minimum sur les familles remplacé par un maximum", lambda: remplacer(B, "terme_projete", lambda p: np.asarray(p).max(0)),
         lambda: det_minimum(V, racine), "seconde écriture du terme projeté"),
        ("projection sous gel recevant une issue du bloc courant", lambda: remplacer(B.Repetition, "tirer", tirer_avant_projection),
         lambda: det_gel(V, racine), "garde d'accès sous gel"),
        ("W^reste oublié", lambda: remplacer(B.Repetition, "_w_reste", lambda self, P9, num, exclure_log=False: [np.inf] * 8),
         lambda: det_w_reste(V, racine), "carte de W^reste promue ou log W > 10⁻⁶"),
        ("famille linéaire oubliée", lambda: remplacer(PB, "processus_j9p", processus_sans_lineaire),
         lambda: det_lineaire(V, racine), "liste des familles"),
        ("coupures de l'archive calculées sur les issues fraîches", lambda: remplacer(B.Repetition, "_temoins", temoins_coupures_fraiches),
         lambda: det_coupures(V, racine), "garde des coupures"),
        ("tirages différents d'un bras à l'autre", lambda: remplacer(B.Repetition, "tirages_de", tirages_perturbes),
         lambda: det_tirages(V, racine), "garde des mêmes issues"),
        ("issues fraîches tirées avant le gel", lambda: remplacer(B, "ordre_du_jeu", _ordre_inverse),
         lambda: det_avant_gel(V, racine), "garde de l'ordre du gel"),
        ("rejet par famille lu à un instant hors de T₄₀", lambda: remplacer(B, "T40", tuple(range(1, 201))),
         lambda: det_t40(V, racine), "garde des instants du jumeau"),
        ("J9-D sans la réunion avec J9", lambda: remplacer(B, "regle_j9d", lambda a, b_, c: (lambda t: (t[0], t[1], t[1]))(_regle_orig(a, b_, c))),
         det_regle_j9d, "seconde écriture de la règle"),
        ("seuil d'informativité choisi sur un bras neuf", lambda: remplacer(LE, "paire_informativite", lambda plus: ("J8", "J9-P")),
         lambda: det_lecture(racine), "I ≠ seconde écriture"),
        ("mauvais bras au numérateur de ρ", lambda: remplacer(LE, "rho", _rho_numerateur_faux), lambda: det_lecture(racine),
         "ρ ≠ seconde écriture"),
        ("I gardé fixe dans le rééchantillonnage", lambda: remplacer(LE, "I_FIXE", True), lambda: det_lecture(racine),
         "intervalle ≠ seconde écriture"),
        ("une ligne Q admise dans I", lambda: remplacer(LE, "V", list(LE.V)[:-1] + ["Q2"]),
         lambda: attendre_garde(lambda: LE.lire_rho(racine, {**donnees_synthetiques(racine), "Q2": donnees_synthetiques(racine)["V5(1.2)"]},
                                                    ["J9-P"], B_=20), "lignes admises dans I"), "garde des lignes V"),
        ("ρ⁺ calculé sans recalculer I⁺", lambda: remplacer(LE, "paire_informativite", lambda plus: ("J8", "J9")),
         lambda: det_lecture(racine), "I⁺ ≠ seconde écriture"),
    ]


_regle_orig = B.regle_j9d


def jouer_banc(V, racine, *, seulement=None, n_certificat=N_CERTIFICAT) -> dict:
    """Joue chaque mutation et son cas sain ; rend le rapport (aucune valeur de jeu)."""
    rapport = []
    for nom, ctx, det, raison in mutations(V, racine):
        if seulement is not None and nom not in seulement:
            continue
        if nom.startswith("certificat"):
            det = (lambda: (lambda d: (d["promotion"], f"promotions {d['comptes']}"))(det_certificat(V, racine, n_certificat)))
        try:
            sain_tue, sain_raison = det()
        except Exception as e:
            sain_tue, sain_raison = True, f"cas sain en erreur : {type(e).__name__}: {e}\n{traceback.format_exc()[-800:]}"
        if nom.startswith("certificat"):
            d = det_certificat(V, racine, n_certificat)
            sain_tue, sain_raison = d["copies"] > 0, f"cas sain : promotions {d['comptes']} (copies Q1, Q2 : 0 exigé)"
        try:
            with ctx():
                tue, raison_obtenue = det()
        except Exception as e:
            tue, raison_obtenue = False, f"détecteur en erreur sous la mutation : {type(e).__name__}: {e}"
        rapport.append({"mutation": nom, "raison_attendue": raison, "tuee": bool(tue), "raison": raison_obtenue,
                        "cas_sain_passe": not sain_tue, "cas_sain": sain_raison})
    return {"mutations": rapport, "toutes_tuees": all(r["tuee"] for r in rapport),
            "cas_sains_passes": all(r["cas_sain_passe"] for r in rapport)}


def compter_garde(V, racine, ligne: str, n: int = N_H7) -> dict:
    """Comptes de la garde P4 sur `ligne` (H7 ou Hn), graines (97, k, r) : terme projeté (toutes les familles) et famille
    linéaire seule, sans garde et sous gel."""
    k = CLES["garde_H7" if ligne == "H7" else "garde_Hn"]
    c = {"sans_garde_terme": 0, "sans_garde_lineaire": 0, "gel_terme": 0, "gel_lineaire": 0}
    for r in range(n):
        o = B.jouer_projection_seule(V, racine, B.INDICE[ligne], (97, k, r))
        c["sans_garde_terme"] += int(o["sans_garde"]["terme"])
        c["sans_garde_lineaire"] += int(o["sans_garde"]["lineaire"])
        c["gel_terme"] += int(o["gel"]["terme"])
        c["gel_lineaire"] += int(o["gel"]["lineaire"])
    c["n"] = n
    return c


def verdict_garde(h7: dict, hn: dict) -> dict:
    """Critère de mort et cas sain écrits (texte, étape 0) ; Hn : compte sans garde inscrit (non bloquant), compte sous
    gel bloquant à 3 ou plus sur 200 (lecture la plus stricte : terme sur toutes les familles **ou** famille linéaire)."""
    mort = h7["sans_garde_terme"] >= MORT_H7_SANS_GARDE
    sain = h7["gel_terme"] <= SAIN_H7_GEL
    hn_bloque = hn["gel_terme"] >= BLOCAGE_HN_GEL or hn["gel_lineaire"] >= BLOCAGE_HN_GEL
    return {"H7_mutation_tuee": mort, "H7_cas_sain_passe": sain, "Hn_gel_bloque": hn_bloque,
            "bloque_le_jeu": (not mort) or (not sain) or hn_bloque}
