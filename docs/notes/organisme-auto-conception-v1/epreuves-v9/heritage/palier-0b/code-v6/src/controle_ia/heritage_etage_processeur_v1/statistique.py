"""B2 — la couche statistique : la même mécanique au grain de la loi et de la tentative, sans fichier, vectorisée sur les
sources d'un tirage (ou d'un lot de sources).

Une tentative est appariée à une loi vraie, à une loi fausse ou à rien. La classe d'issue (« tient » ou non) est tirée une fois
par loi engagée et par monde — pour les lois plantées, sur la graine du monde, commune aux bras, comme sur la couche mécanique
où un même engagement sur une même tranche rend le même verdict ; la fréquence d'une loi vraie est celle de la strate de son
monde (monde source ou monde cible, version 5) ; une loi non plantée est tenue pour distincte à chaque tentative et prend la
fréquence de son origine (recherche de base, composition passée au criblage, copie ; version 4). Seul l'échec de
l'expérimentateur se tire par tentative (B5). Le criblage du lecteur : passage d'une composition qui est une loi dépendante du
monde (tiré sur la graine du monde) et faux passage des autres compositions (sur la graine d'échantillonnage).

Une strate vide dont la couche a besoin arrête (liste d'arrêt, point 4) : `_f` lève, jamais de repli.

Équivalences de loi employées (annexe F, acceptées sans entrer au texte ; éprouvées par la garde S8) : comptes multinomiaux pour
le choix uniforme des lois ; loi hypergéométrique pour les paires examinées et pour le plafond des compositions engagées ;
sous-ensemble uniforme par clés aléatoires.
"""

import numpy as np

from .constantes import (APPELS_PAR_GENERATION, CLES_FREQUENCES, DOMAINES_A_LOI_CIBLE, DOMAINES_A_LOI_SOURCE,
                         GENERATIONS_COURSE_SOURCE, MONDES_CIBLES_D_EVOLUTION, P_FAUSSE_BASE, PROBA_DEUX_TENTATIVES,
                         REPERE_LECTURE)
from .cout import cout_lecture_par_appel, retrait_v1, retrait_v2_vectorise
from .frequences import ArretFrequences, exiger_strates, strates_requises
from .mondes import PAIRES_DE_LA_SOURCE, nombre_de_dependantes
from .proposeurs import p_vraie, part_generaliste

PAIRE_A = np.array([p for p, q in PAIRES_DE_LA_SOURCE])
PAIRE_B = np.array([q for p, q in PAIRES_DE_LA_SOURCE])


def _f(f, cle):
    v = f[cle]
    if v is None:
        raise ArretFrequences(f"strate de M12 vide employée par la couche statistique : {cle} : arrêt (liste d'arrêt, point 4)")
    return float(v)


class Mondes:
    """Tout ce que la graine du monde fixe pour S sources : classes des lois plantées et passages des compositions vraies.

    `passage_requis` (code v3, C3) : vrai si `frequences.strates_requises` exige `p_passage_vraie` pour le proposeur, la dose et
    les bras joués (un lecteur aux bras 3 ou 4a, à dose non nulle). Sinon la fréquence n'est pas lue : les tirages du
    générateur sont faits de même (le flux de la graine du monde ne change pas) et les passages valent None ; les employer
    arrête (`jouer_bras`), jamais de repli."""

    def __init__(self, rng, S, dose, f, passage_requis):
        d = nombre_de_dependantes(dose)
        self.S, self.d = S, d
        self.tient_src_v = rng.random((S, DOMAINES_A_LOI_SOURCE)) < _f(f, "p_tient_vraie_source")
        self.tient_src_f = rng.random((S, DOMAINES_A_LOI_SOURCE)) < _f(f, "p_tient_fausse")
        perm = np.argsort(rng.random((S, len(PAIRES_DE_LA_SOURCE))), axis=1)
        self.paires, self.tient_v, self.tient_f, self.passage = [], [], [], []
        for w in range(MONDES_CIBLES_D_EVOLUTION + 1):
            self.paires.append(perm[:, w * d:(w + 1) * d])
            self.tient_v.append(rng.random((S, DOMAINES_A_LOI_CIBLE)) < _f(f, "p_tient_vraie_cible"))  # d premières : dépendantes
            self.tient_f.append(rng.random((S, DOMAINES_A_LOI_CIBLE)) < _f(f, "p_tient_fausse"))
            u = rng.random((S, d))
            if not d:
                self.passage.append(u < 0.0)
            elif passage_requis:
                self.passage.append(u < _f(f, "p_passage_vraie"))
            else:
                self.passage.append(None)


def _appels(rng, S, n_servi, paie, repere, regle):
    lecture = np.where(paie & (n_servi > 0), cout_lecture_par_appel(n_servi, repere), 0.0)
    if regle == "v1":
        return retrait_v1(lecture).sum(axis=1), np.zeros(S)
    perm = np.argsort(rng.random((S, APPELS_PAR_GENERATION)), axis=1)
    _, par, reliquat = retrait_v2_vectorise(perm, lecture)
    return par.sum(axis=1), reliquat


def _choisir_parmi(rng, disponibles, nombre):
    """Un sous-ensemble uniforme de `nombre` colonnes parmi les colonnes vraies de `disponibles` (S × m), par ligne."""
    if disponibles.shape[1] == 0:
        return disponibles.copy()
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


def _binomiale(rng, n, p):
    n = np.asarray(n, dtype=np.int64)
    if not np.any(n > 0):
        return np.zeros_like(n)
    return rng.binomial(n, p)


def _lois_engagees(rng, comptes, tient, taux):
    """Pour chaque loi engagée c fois : tentatives non échouées ~ B(c, 1 − taux). Rend (gardée, entrées gardées) par loi."""
    non_echouees = rng.binomial(comptes, 1.0 - taux)
    gardee = tient & (non_echouees > 0)
    return gardee, np.where(tient, non_echouees, 0)


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

    def roule(self, roul):
        e = Registre(len(roul))
        for k, v in vars(self).items():
            setattr(e, k, v[roul])
        return e


def _base(rng, prop, n, n_servi, n_classes, propre, m_vraies):
    S = len(n)
    pv = p_vraie(prop, n_servi, propre)
    n_t = rng.binomial(n, pv)
    n_f = rng.binomial(n - n_t, np.minimum(1.0, P_FAUSSE_BASE / (1.0 - pv)))
    n_np = n - n_t - n_f
    if prop["gamma"]:
        g = part_generaliste(prop, n_classes)
        dep = rng.binomial(n_np, g)
        vers_v = rng.binomial(dep, 0.5)
        n_t, n_f, n_np = n_t + vers_v, n_f + dep - vers_v, n_np - dep
    cv = rng.multinomial(n_t, np.full(m_vraies, 1.0 / m_vraies)) if m_vraies else np.zeros((S, 0), dtype=np.int64)
    return cv, n_f, n_np


def course_source(rng, prop, mondes, f, taux, repere=REPERE_LECTURE, regle="v2", repli=False):
    """Trois générations du monde source, registre né vide servi et payé comme au bras 2 ; aucune entrée héritée."""
    S = mondes.S
    r = Registre(S)
    propre = np.zeros(S, dtype=bool)
    for _ in range(GENERATIONS_COURSE_SOURCE):
        appels, _ = _appels(rng, S, r.n, prop["paie"], repere, regle)
        n = appels + rng.binomial(appels, PROBA_DEUX_TENTATIVES)
        copie = (r.n > 0) if prop["copieur"] else np.zeros(S, dtype=bool)
        n_classes = np.zeros(S, dtype=np.int64) if repli else r.n
        cv, n_f, n_np = _base(rng, prop, np.where(copie, 0, n), r.n, n_classes, propre, DOMAINES_A_LOI_SOURCE)
        n_copie = np.where(copie, n, 0)
        cf = rng.multinomial(n_f, np.full(DOMAINES_A_LOI_SOURCE, 1.0 / DOMAINES_A_LOI_SOURCE))
        gv, ev = _lois_engagees(rng, cv, mondes.tient_src_v, taux)
        gf, ef = _lois_engagees(rng, cf, mondes.tient_src_f, taux)
        g_np = _binomiale(rng, n_np, _f(f, "p_tient_non_plantee_base") * (1.0 - taux))
        g_cp = _binomiale(rng, n_copie, _f(f, "p_tient_non_plantee_copie") * (1.0 - taux)) if prop["copieur"] else 0 * n_copie
        r.n += n
        r.gardee_v |= gv
        r.gardee_f |= gf
        r.gardee_np += g_np + g_cp
        r.engagee_v |= cv > 0
        r.engagee_f |= cf > 0
        r.engagee_np += n_np + n_copie
        r.n_gardees += ev.sum(axis=1) + ef.sum(axis=1) + g_np + g_cp
        r.entrees_v += cv.sum(axis=1)
        r.gardees_v += ev.sum(axis=1)
        propre |= gv.any(axis=1) | gf.any(axis=1) | (g_np + g_cp > 0)
    return r


def _paires(n):
    return n * (n - 1) // 2


def jouer_bras(rng, prop, mondes, f, taux, bras, source, source_etrangere=None, tailles_etrangeres=None, repere=REPERE_LECTURE,
               regle="v2", repli=False):
    """Un bras (« 1 », « 2 », « 3 », « 4a », « 4b ») sur trois mondes cibles et le monde final. Rend un dictionnaire de
    tableaux (S,) : M1, D, I, fausses_tenues, fausses_engagees, vraies_tenues, tailles servies par génération, reliquat."""
    S, d = mondes.S, mondes.d
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
            n_servi = np.asarray(tailles_etrangeres[w], dtype=np.int64)
        else:
            raise ValueError(bras)
        tailles.append(n_servi.copy())
        appels, rel = _appels(rng, S, n_servi, prop["paie"], repere, regle)
        reliquat += rel
        n = appels + rng.binomial(appels, PROBA_DEUX_TENTATIVES)
        n_classes = np.zeros(S, dtype=np.int64) if repli else n_servi
        propre_servi = propre if bras in ("2", "3", "4a") else np.zeros(S, dtype=bool)
        dep_eng = np.zeros((S, d), dtype=bool)
        n_comp = np.zeros(S, dtype=np.int64)
        n_fp_eng = np.zeros(S, dtype=np.int64)
        if prop["K"] and bras in ("3", "4a"):
            src = source if bras == "3" else source_etrangere
            gv = src.engagee_v if repli else src.gardee_v
            gf = src.engagee_f if repli else src.gardee_f
            gnp = src.engagee_np if repli else src.gardee_np
            nl = gv.sum(axis=1) + gf.sum(axis=1) + gnp
            P = _paires(nl)
            if bras == "3" and d:
                p = mondes.paires[w]
                dispo = np.take_along_axis(gv, PAIRE_A[p], axis=1) & np.take_along_axis(gv, PAIRE_B[p], axis=1)
            else:
                dispo = np.zeros((S, d), dtype=bool)
            K = prop["K"]
            k = int(np.floor(K)) + (rng.random(S) < K - np.floor(K))
            m = np.minimum(k, P)
            touches = _hypergeometrique(rng, dispo.sum(axis=1), P - dispo.sum(axis=1), m)
            examinees = _choisir_parmi(rng, dispo, touches)
            if mondes.passage[w] is None:
                raise ArretFrequences("passages des compositions vraies non tirés (p_passage_vraie non requise) mais employés "
                                      f"au bras {bras} : arrêt (liste d'arrêt, point 4)")
            passent = examinees & mondes.passage[w]
            n_vp = passent.sum(axis=1)
            n_fp = _binomiale(rng, np.maximum(2 * m - touches, 0), _f(f, "p_faux_passage"))
            plafond = n // 2
            trop = (n_vp + n_fp) > plafond
            n_vp_eng = np.where(trop, _hypergeometrique(rng, n_vp, n_fp, np.where(trop, plafond, 0)), n_vp)
            n_fp_eng = np.where(trop, plafond - n_vp_eng, n_fp)
            dep_eng = _choisir_parmi(rng, passent, n_vp_eng)
            n_comp = n_vp_eng + n_fp_eng
        reste = n - n_comp
        copie = np.full(S, bool(prop["copieur"])) & (n_servi > 0)
        cv, n_f, n_np = _base(rng, prop, np.where(copie, 0, reste), n_servi, n_classes, propre_servi, DOMAINES_A_LOI_CIBLE - d)
        n_copie = np.where(copie, reste, 0)
        cf = rng.multinomial(n_f, np.full(DOMAINES_A_LOI_CIBLE, 1.0 / DOMAINES_A_LOI_CIBLE))
        comptes_v = np.concatenate([dep_eng.astype(np.int64), cv], axis=1)
        gv_, _ = _lois_engagees(rng, comptes_v, mondes.tient_v[w], taux)
        gf_, _ = _lois_engagees(rng, cf, mondes.tient_f[w], taux)
        g_np = _binomiale(rng, n_np, _f(f, "p_tient_non_plantee_base") * (1.0 - taux))
        g_cmp = _binomiale(rng, n_fp_eng, _f(f, "p_tient_non_plantee_composition") * (1.0 - taux)) if prop["K"] else 0 * n_np
        g_cp = _binomiale(rng, n_copie, _f(f, "p_tient_non_plantee_copie") * (1.0 - taux)) if prop["copieur"] else 0 * n_np
        if finale:
            engagees_v = comptes_v > 0
            out["D"] = engagees_v[:, :d].sum(axis=1)
            out["I"] = engagees_v[:, d:].sum(axis=1)
            out["M1"] = out["D"] + out["I"]
            out["fausses_tenues"] = gf_.sum(axis=1)
            out["fausses_engagees"] = (cf > 0).sum(axis=1)
            out["vraies_tenues"] = gv_.sum(axis=1)
        else:
            n_propre += n
            propre |= gv_.any(axis=1) | gf_.any(axis=1) | (g_np + g_cmp + g_cp > 0)
    out["tailles_servies"] = np.stack(tailles, axis=1)
    out["reliquat"] = reliquat
    return out


def enrichissement(source):
    """M7 : part des entrées de la source gardées ; facteur d'enrichissement au grain des entrées et des paires."""
    with np.errstate(divide="ignore", invalid="ignore"):
        part_gardees = source.n_gardees / source.n
        fe_entrees = (source.gardees_v / source.n_gardees) / (source.entrees_v / source.n)
        nt_g = source.gardee_v.sum(axis=1)
        nl_g = nt_g + source.gardee_f.sum(axis=1) + source.gardee_np
        nt_e = source.engagee_v.sum(axis=1)
        nl_e = nt_e + source.engagee_f.sum(axis=1) + source.engagee_np
        fe_paires = (_paires(nt_g) / _paires(nl_g)) / (_paires(nt_e) / _paires(nl_e))
    return {"part_des_entrees_gardees": part_gardees, "facteur_entrees": fe_entrees, "facteur_paires": fe_paires}


def bras_de(cle):
    return cle.split("-")[0]


def roulement(S, taille_tirage=None):
    """La source étrangère de chaque source : la suivante du même tirage, la première pour la dernière (B7 bis)."""
    t = S if taille_tirage is None else int(taille_tirage)
    if S % t:
        raise ValueError("le nombre de sources d'un lot doit être un multiple de la taille du tirage")
    i = np.arange(S)
    return (i // t) * t + (i % t + 1) % t


def simuler(graines_bras, rng_monde, rng_source, prop, dose, taux, f, S, repere=REPERE_LECTURE, regle="v2", repli=False,
            taille_tirage=None):
    """Une épreuve simulée sur S sources (un tirage, ou un lot de sources). `graines_bras` : {clé de bras : générateur}
    (clé « 2 », « 2-j1 »… : le bras est ce qui précède « - »). La source étrangère d'une source est la suivante du même tirage
    (`taille_tirage` sources consécutives ; tout le lot par défaut). Rend {"bras": {clé: sorties}, "source": registre,
    "mondes": mondes}."""
    bras = sorted({bras_de(c) for c in graines_bras})
    exiger_strates(f, prop, dose, bras)
    if sorted(f) != sorted(CLES_FREQUENCES):
        raise ArretFrequences("fréquences mal formées")
    mondes = Mondes(rng_monde, S, dose, f, "p_passage_vraie" in strates_requises(prop, dose, bras))
    src = course_source(rng_source, prop, mondes, f, taux, repere, regle, repli)
    roul = roulement(S, taille_tirage)
    etrangere = src.roule(roul) if "4a" in bras else None
    sorties = {}
    ordre = sorted(graines_bras, key=lambda c: (bras_de(c) == "4b", c))
    for cle in ordre:
        b = bras_de(cle)
        tailles = None
        if b == "4b":
            ref = sorties.get("2") or next((v for k, v in sorties.items() if bras_de(k) == "2"), None)
            if ref is None:
                raise ValueError("bras 4b sans bras 2 joué : la source étrangère n'a pas de registre tenu")
            tailles = [ref["tailles_servies"][:, w][roul] for w in range(MONDES_CIBLES_D_EVOLUTION + 1)]
        sorties[cle] = jouer_bras(graines_bras[cle], prop, mondes, f, taux, b, src, etrangere, tailles, repere, regle, repli)
    return {"bras": sorties, "source": src, "mondes": mondes}
