"""B2 — la couche statistique : la même mécanique au grain de la loi et de la tentative, sans fichier, vectorisée sur les
sources d'un tirage (ou d'un lot de sources).

Une tentative est appariée à une loi vraie, à une loi fausse ou à rien. La classe d'issue (« tient » ou non) est tirée une fois
par loi engagée et par monde — pour les lois plantées, sur la graine du monde, commune aux bras, comme sur la couche mécanique
où un même engagement sur une même tranche rend le même verdict ; pour une loi non plantée (distincte à chaque tentative), sur
la graine d'échantillonnage. Seul l'échec de l'expérimentateur se tire par tentative (B5). Les fréquences viennent du fichier
scellé de la couche mécanique (M12). Le criblage du lecteur : passage d'une composition qui est une loi dépendante du monde
(tiré sur la graine du monde) et faux passage des autres compositions (sur la graine d'échantillonnage).

Équivalences de distribution employées (écrites ici, éprouvées par la garde S8) : comptes multinomiaux pour le choix uniforme
des lois ; loi hypergéométrique pour les K paires examinées parmi P ; tirage d'un sous-ensemble uniforme par clés aléatoires.
"""

import numpy as np

from .constantes import (APPELS_PAR_GENERATION, DOMAINES_A_LOI_CIBLE, DOMAINES_A_LOI_SOURCE, GENERATIONS_COURSE_SOURCE,
                         MONDES_CIBLES_D_EVOLUTION, P_FAUSSE_BASE, PROBA_DEUX_TENTATIVES, REPERE_LECTURE)
from .cout import cout_lecture_par_appel, retrait_v1, retrait_v2_vectorise
from .mondes import PAIRES_DE_LA_SOURCE, nombre_de_dependantes
from .proposeurs import p_vraie, part_generaliste

PAIRE_A = np.array([p for p, q in PAIRES_DE_LA_SOURCE])
PAIRE_B = np.array([q for p, q in PAIRES_DE_LA_SOURCE])
CLES_FREQUENCES = ("p_tient_vraie", "p_tient_fausse", "p_tient_non_plantee", "p_passage_vraie", "p_faux_passage")


def _verifier_frequences(f):
    if sorted(f) != sorted(CLES_FREQUENCES) or not all(0.0 <= float(f[k]) <= 1.0 for k in CLES_FREQUENCES):
        raise ValueError(f"fréquences de la couche mécanique mal formées : {f}")


class Mondes:
    """Tout ce que la graine du monde fixe pour S sources : classes des lois plantées et passages des compositions vraies."""

    def __init__(self, rng, S, dose, f):
        d = nombre_de_dependantes(dose)
        self.S, self.d = S, d
        self.tient_src_v = rng.random((S, DOMAINES_A_LOI_SOURCE)) < f["p_tient_vraie"]
        self.tient_src_f = rng.random((S, DOMAINES_A_LOI_SOURCE)) < f["p_tient_fausse"]
        perm = np.argsort(rng.random((S, len(PAIRES_DE_LA_SOURCE))), axis=1)
        self.paires, self.tient_v, self.tient_f, self.passage = [], [], [], []
        for w in range(MONDES_CIBLES_D_EVOLUTION + 1):
            self.paires.append(perm[:, w * d:(w + 1) * d])
            self.tient_v.append(rng.random((S, DOMAINES_A_LOI_CIBLE)) < f["p_tient_vraie"])  # d premières : dépendantes
            self.tient_f.append(rng.random((S, DOMAINES_A_LOI_CIBLE)) < f["p_tient_fausse"])
            self.passage.append(rng.random((S, d)) < f["p_passage_vraie"])


def _appels(rng, S, n_servi, paie, repere, regle):
    lecture = np.where(paie & (n_servi > 0), cout_lecture_par_appel(n_servi, repere), 0.0)
    if regle == "v1":
        par = retrait_v1(lecture)
        return par.sum(axis=1), np.zeros(S)
    perm = np.argsort(rng.random((S, APPELS_PAR_GENERATION)), axis=1)
    _, par, reliquat = retrait_v2_vectorise(perm, lecture)
    return par.sum(axis=1), reliquat


def _choisir_parmi(rng, disponibles, nombre):
    """Un sous-ensemble uniforme de `nombre` colonnes parmi les colonnes vraies de `disponibles` (S × m), par ligne."""
    cles = np.where(disponibles, rng.random(disponibles.shape), np.inf)
    rang = np.argsort(np.argsort(cles, axis=1), axis=1)
    return disponibles & (rang < np.asarray(nombre)[:, None])


def _hypergeometrique(rng, bons, mauvais, n):
    bons, mauvais, n = (np.asarray(x, dtype=np.int64) for x in (bons, mauvais, n))
    out = np.zeros_like(n)
    ok = (n > 0) & (bons > 0)
    if ok.any():
        out[ok] = rng.hypergeometric(bons[ok], mauvais[ok], n[ok])
    return out


def _lois_engagees(rng, comptes, tient, taux):
    """Pour chaque loi engagée c fois : tentatives non échouées ~ B(c, 1 − taux). Rend (gardée, entrées gardées, tenue au moins
    une fois) par loi."""
    non_echouees = rng.binomial(comptes, 1.0 - taux)
    gardee = tient & (non_echouees > 0)
    return gardee, np.where(tient, non_echouees, 0), gardee


class Registre:
    """Ce que la couche statistique garde d'un registre, par source."""

    def __init__(self, S):
        self.n = np.zeros(S, dtype=np.int64)
        self.n_gardees = np.zeros(S, dtype=np.int64)
        self.gardee_v = np.zeros((S, DOMAINES_A_LOI_SOURCE), dtype=bool)
        self.gardee_f = np.zeros((S, DOMAINES_A_LOI_SOURCE), dtype=bool)
        self.gardee_np = np.zeros(S, dtype=np.int64)
        self.engagee_v = np.zeros((S, DOMAINES_A_LOI_SOURCE), dtype=bool)
        self.engagee_f = np.zeros((S, DOMAINES_A_LOI_SOURCE), dtype=bool)
        self.engagee_np = np.zeros(S, dtype=np.int64)
        self.entrees_v = np.zeros(S, dtype=np.int64)
        self.gardees_v = np.zeros(S, dtype=np.int64)


def _base(rng, prop, n, n_servi, n_classes, propre, m_vraies):
    S = len(n)
    pv = p_vraie(prop, n_servi, propre)
    n_t = rng.binomial(n, pv)
    n_f = rng.binomial(n - n_t, np.minimum(1.0, P_FAUSSE_BASE / (1.0 - pv)))
    n_np = n - n_t - n_f
    g = part_generaliste(prop, n_classes)
    if prop["gamma"]:
        dep = rng.binomial(n_np, g)
        vers_v = rng.binomial(dep, 0.5)
        n_t, n_f, n_np = n_t + vers_v, n_f + dep - vers_v, n_np - dep
    cv = rng.multinomial(n_t, np.full(m_vraies, 1.0 / m_vraies)) if m_vraies else np.zeros((S, 0), dtype=np.int64)
    return cv, n_f, n_np


def course_source(rng, prop, mondes, f, taux, repere=REPERE_LECTURE, regle="v2"):
    """Trois générations du monde source, registre né vide servi et payé comme au bras 2."""
    S = mondes.S
    r = Registre(S)
    propre = np.zeros(S, dtype=bool)
    for _ in range(GENERATIONS_COURSE_SOURCE):
        appels, _ = _appels(rng, S, r.n, prop["paie"], repere, regle)
        n = appels + rng.binomial(appels, PROBA_DEUX_TENTATIVES)
        if prop["copieur"]:
            copie = r.n > 0
        else:
            copie = np.zeros(S, dtype=bool)
        cv, n_f, n_np = _base(rng, prop, np.where(copie, 0, n), r.n, r.n, propre, DOMAINES_A_LOI_SOURCE)
        n_np = np.where(copie, n, n_np)
        cf = rng.multinomial(n_f, np.full(DOMAINES_A_LOI_SOURCE, 1.0 / DOMAINES_A_LOI_SOURCE))
        gv, ev, _ = _lois_engagees(rng, cv, mondes.tient_src_v, taux)
        gf, ef, _ = _lois_engagees(rng, cf, mondes.tient_src_f, taux)
        g_np = rng.binomial(n_np, f["p_tient_non_plantee"] * (1.0 - taux))
        r.n += n
        r.gardee_v |= gv
        r.gardee_f |= gf
        r.gardee_np += g_np
        r.engagee_v |= cv > 0
        r.engagee_f |= cf > 0
        r.engagee_np += n_np
        r.n_gardees += ev.sum(axis=1) + ef.sum(axis=1) + g_np
        r.entrees_v += cv.sum(axis=1)
        r.gardees_v += ev.sum(axis=1)
        propre |= (gv.any(axis=1) | gf.any(axis=1) | (g_np > 0))
    return r


def _paires(n):
    return n * (n - 1) // 2


def jouer_bras(rng, prop, mondes, f, taux, bras, source, source_etrangere=None, tailles_etrangeres=None, repere=REPERE_LECTURE,
               regle="v2", repli=False, rng_k=None, faute=None):
    """Un bras (« 1 », « 2 », « 3 », « 4a », « 4b ») sur trois mondes cibles et le monde final. Rend un dictionnaire de
    tableaux (S,) : M1, D, I, fausses_tenues, tailles servies par génération, reliquat."""
    S, d = mondes.S, mondes.d
    rng_k = rng if rng_k is None else rng_k
    n_propre = np.zeros(S, dtype=np.int64)
    propre = np.zeros(S, dtype=bool)
    tailles, reliquat = [], np.zeros(S)
    out = {}
    for w in range(MONDES_CIBLES_D_EVOLUTION + 1):
        finale = w == MONDES_CIBLES_D_EVOLUTION
        if bras == "1":
            n_servi = np.zeros(S, dtype=np.int64)
        elif bras == "2":
            n_servi = n_propre.copy()
        elif bras == "3":
            n_servi = source.n + n_propre
        elif bras == "4a":
            n_servi = source_etrangere.n + n_propre
        elif bras == "4b":
            n_servi = tailles_etrangeres[w]
        else:
            raise ValueError(bras)
        tailles.append(n_servi.copy())
        appels, rel = _appels(rng, S, n_servi, prop["paie"], repere, regle)
        reliquat += rel
        n = appels + rng.binomial(appels, PROBA_DEUX_TENTATIVES)
        n_classes = np.zeros(S, dtype=np.int64) if repli else n_servi
        propre_servi = propre if bras in ("2", "3", "4a") else np.zeros(S, dtype=bool)
        # compositions du lecteur réglé pour l'héritage
        dep_eng = np.zeros((S, d), dtype=bool)
        n_comp = np.zeros(S, dtype=np.int64)
        if prop["K"] and bras in ("3", "4a"):
            src = source if bras == "3" else source_etrangere
            gv = src.engagee_v if repli else src.gardee_v
            gf = src.engagee_f if repli else src.gardee_f
            gnp = src.engagee_np if repli else src.gardee_np
            nt = gv.sum(axis=1)
            nl = nt + gf.sum(axis=1) + gnp
            P = _paires(nl)
            if bras == "3" and d:
                p = mondes.paires[w]
                dispo = np.take_along_axis(gv, PAIRE_A[p], axis=1) & np.take_along_axis(gv, PAIRE_B[p], axis=1)
            else:
                dispo = np.zeros((S, d), dtype=bool)
            K = prop["K"]
            k = np.floor(K).astype(np.int64) + (rng_k.random(S) < K - np.floor(K))
            m = np.minimum(k, P)
            touches = _hypergeometrique(rng, dispo.sum(axis=1), P - dispo.sum(axis=1), m)
            examinees = _choisir_parmi(rng, dispo, touches) if d else dispo
            passent = examinees & mondes.passage[w]
            n_vp = passent.sum(axis=1)
            n_fp = rng.binomial(np.maximum(2 * m - touches, 0), f["p_faux_passage"])
            plafond = n // 2
            trop = (n_vp + n_fp) > plafond
            n_vp_eng = np.where(trop, _hypergeometrique(rng, n_vp, n_fp, np.where(trop, plafond, 0)), n_vp)
            n_fp_eng = np.where(trop, plafond - n_vp_eng, n_fp)
            dep_eng = _choisir_parmi(rng, passent, n_vp_eng) if d else passent
            n_comp = n_vp_eng + n_fp_eng
        else:
            n_fp_eng = np.zeros(S, dtype=np.int64)
        reste = n - n_comp
        copie = np.full(S, bool(prop["copieur"])) & (n_servi > 0)
        cv, n_f, n_np = _base(rng, prop, np.where(copie, 0, reste), n_servi, n_classes, propre_servi,
                              DOMAINES_A_LOI_CIBLE - d)
        n_np = np.where(copie, reste, n_np) + n_fp_eng
        cf = rng.multinomial(n_f, np.full(DOMAINES_A_LOI_CIBLE, 1.0 / DOMAINES_A_LOI_CIBLE))
        comptes_v = np.concatenate([dep_eng.astype(np.int64), cv], axis=1)
        gv_, _, tenue_v = _lois_engagees(rng, comptes_v, mondes.tient_v[w], taux)
        gf_, _, tenue_f = _lois_engagees(rng, cf, mondes.tient_f[w], taux)
        g_np = rng.binomial(n_np, f["p_tient_non_plantee"] * (1.0 - taux))
        if finale:
            engagees_v = comptes_v > 0
            if faute == "loi-de-la-source-recopiee":
                engagees_v[:, -1] &= ~source.engagee_v[:, 0]  # la loi recopiée de la source est exclue pour tous les bras
            out["D"] = engagees_v[:, :d].sum(axis=1)
            out["I"] = engagees_v[:, d:].sum(axis=1)
            out["M1"] = out["D"] + out["I"]
            out["fausses_tenues"] = ((cf > 0) & tenue_f).sum(axis=1)
        else:
            n_propre += n
            propre |= gv_.any(axis=1) | gf_.any(axis=1) | (g_np > 0)
    out["tailles_servies"] = np.stack(tailles, axis=1)
    out["reliquat"] = reliquat
    return out


def enrichissement(source):
    """M7 : part des entrées de la source gardées ; facteur d'enrichissement au grain des entrées et des paires."""
    with np.errstate(divide="ignore", invalid="ignore"):
        part_gardees = source.n_gardees / source.n
        gardees_v = source.gardees_v / source.n_gardees
        toutes_v = source.entrees_v / source.n
        fe_entrees = gardees_v / toutes_v
        nt_g, nl_g = source.gardee_v.sum(axis=1), source.gardee_v.sum(axis=1) + source.gardee_f.sum(axis=1) + source.gardee_np
        nt_e, nl_e = source.engagee_v.sum(axis=1), source.engagee_v.sum(axis=1) + source.engagee_f.sum(axis=1) + source.engagee_np
        fe_paires = (_paires(nt_g) / _paires(nl_g)) / (_paires(nt_e) / _paires(nl_e))
    return {"part_des_entrees_gardees": part_gardees, "facteur_entrees": fe_entrees, "facteur_paires": fe_paires}


def simuler(graines_bras, rng_monde, rng_source, prop, dose, taux, f, S, bras=("1", "2", "3"), repere=REPERE_LECTURE,
            regle="v2", repli=False, faute=None):
    """Une épreuve simulée sur S sources (un tirage, ou un lot d'étalonnage). `graines_bras` : {clé de bras : générateur}
    (clé « 2 », « 2-j1 »…, le bras étant le premier caractère avant « - »). Rend {"bras": {clé: sorties}, "source": registre}."""
    _verifier_frequences(f)
    mondes = Mondes(rng_monde, S, dose, f)
    src = course_source(rng_source, prop, mondes, f, taux, repere, regle)
    etrangere = None
    roul = (np.arange(S) + 1) % S

    def etranger(r):
        e = Registre(S)
        for k, v in vars(r).items():
            setattr(e, k, v[roul])
        return e

    sorties = {}
    ordre = sorted(graines_bras, key=lambda c: (c.split("-")[0] == "4b", c))
    for cle in ordre:
        b = cle.split("-")[0]
        if b == "4a" and etrangere is None:
            etrangere = etranger(src)
        tailles = None
        if b == "4b":
            ref = sorties.get("2") or next(v for k, v in sorties.items() if k.split("-")[0] == "2")
            tailles = [ref["tailles_servies"][:, w][roul] for w in range(MONDES_CIBLES_D_EVOLUTION + 1)]
        sorties[cle] = jouer_bras(graines_bras[cle], prop, mondes, f, taux, b, src, etrangere, tailles, repere, regle, repli,
                                  faute=faute)
    return {"bras": sorties, "source": src, "mondes": mondes}
