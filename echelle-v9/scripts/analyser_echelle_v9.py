#!/usr/bin/env python3
"""Analyse v8 de la comparaison d'échelle 8B contre 70B (lignée « session-depot », 27 octobre 2026 ; préenregistrement
`prereg/test-echelle-conscience-eval-v10.md`, qui fait foi en cas de désaccord). Déclinée de `analyser_echelle_v7.py`
sous un nom nouveau (R12) après la contre-lecture n° 7 (CLT-01, CLT-02, CLT-05) : la cohérence des deux sens ne ferme
la classe de cl6 qu'en son centre ; deux réserves obligatoires s'ajoutent donc à « positif », « inverse » et « nul »,
sans paramètre tiré des mesures : l'intervalle de e(m) exclut zéro pour un modèle ; le rapport des Ec des deux sens
d'un modèle, ou son inverse, dépasse 1,15 (bande symétrique en logarithme, fixée sur un essai exploratoire synthétique,
avant toute mesure : la bande [0,8 ; 1,25] d'abord envisagée laissait dans la bande environ la moitié des valeurs
d'un modèle sous un contexte d'un jeu plus fort d'un tiers, que le rapport mesuré tire vers 1). Le rapport des Ec est rapporté, avec son intervalle ; un « désaccord » né de la seule
cohérence se nomme à part, « désaccord des deux sens (cohérence) ». Lectures inchangées sinon. Depuis la v7
(contre-lecture n° 6) : « positif », « inverse » et « nul » ne sont communs aux deux sens que si chaque modèle garde
le même λ d'un sens à l'autre, à δ près, en estimation ponctuelle (cohérence des deux sens, CLU-01). Depuis la v6
(contre-lecture n° 5) : la fuite de signe inverse se lit modèle par modèle, et n'est prononcée que si le même modèle
la tient dans les deux sens (CLV-01) ; conditions manquantes de chaque issue tenue dans un seul sens (CLV-07). Calcul
des mesures inchangé depuis la v5. Processeur seulement.

Deux sens d'ajustement, chacun croisé sur les moitiés de contenus E1 et E2, **lus par les mêmes règles** :
  a→b  direction apprise sur le jeu de cadrages a, mesurée sur les paraphrases b ;
  b→a  direction apprise sur b, mesurée sur a.
  Une poussée du format sur la signature propre aux cadrages d'un jeu déplace λ dans un sens seulement, dans un signe
  ou dans l'autre ; une fuite du concept le déplace dans les deux. Aucune issue n'est donc prononcée sur un sens seul.
Pour chaque modèle (petit = 8B, grand = 70B), à une couche L* choisie sur le pli S, et pour chaque sens :
  ĉ   différence des moyennes eval − reel du jeu d'apprentissage (les deux formats, paires à format constant), normée ;
      projections sur le jeu de mesure de l'autre moitié, centrées dans chaque moitié (invariance par translation) ;
  Ec  moyenne sur les formats de [s̄(eval) − s̄(reel)] ; Ef  moyenne sur les contextes de [s̄(qcm) − s̄(prose)] ;
  λ   indice de fuite du format = Ef / Ec ;
  A_ctx_fixe  aire (eval contre reel) à format égal, directions apprises une fois et tenues fixes dans le bootstrap
              (certification) ; A_ctx (directions réapprises), A_conf (cellules en conflit), A_conf_T1, rapportées ;
  ν   témoin de permutation : dix partitions équilibrées des six paires d'apprentissage, d_σ = moyenne du groupe 1 −
      moyenne du groupe 2, orthogonalisée par rapport à ĉ (CLY-02), ν = moyenne des |Ef le long de d_σ| / |Ec| ;
  points seuls (CLY-07) : λ mesuré sur le jeu d'apprentissage de l'autre moitié, rapport de transfert, Ec par format.
Cohérence des deux sens (CLU-01), par modèle m : écart entre les sens e(m) = λ_a→b(m) − λ_b→a(m), même couche L*,
en point ; intervalle sur les mêmes tirages, rapporté. Avec d l'écart vrai d'échelle de la fuite du concept et la
poussée d'un seul jeu à chaque taille (classe de cl6), e(m) vaut, au bruit près, le Δλ du sens que la signature de m
déplace **moins d** ; si le contexte du jeu b vaut k fois celui du jeu a, e(m) gagne de plus λ(m)·(1/k − 1) (CLT-01,
CLT-02). Sous d = 0 et k = 1 (centre de la classe), dès que « positif » tient dans les deux sens, |e(m)| dépasse δ ;
autour de ce centre, la cohérence ne borne qu'à δ, par modèle et par sens, la part de l'écart portée par un modèle
différent dans chaque sens : d'où les deux réserves de la v8.
Rapport des Ec (CLT-01), par modèle : Ec_a→b(m) / Ec_b→a(m), en point (intervalle rapporté) ; il estime k, la force
du contexte du jeu b (mesuré en a→b) relativement à celle du jeu a (mesuré en b→a).
Contrastes, par sens : Δλ = λ(petit) − λ(grand) ; spécificité = Δλ − (ν(petit) − ν(grand)) ; pour la fuite de signe
inverse, spécificité de signe inverse d'un modèle = −λ − ν (CLW-02) ; ΔA_ctx_fixe et ΔA_conf ; sac de mots appris sur
le jeu d'apprentissage et appliqué au jeu de mesure (CLW-07).
Intervalles : bootstrap apparié (mêmes tirages pour les deux modèles et les deux sens) sur les contenus (dans chaque
moitié) et sur les paires (dans chaque jeu, au moins deux paires distinctes par jeu, rejets comptés), 2 000 tirages,
percentiles 2,5 et 97,5 ; directions réapprises à chaque tirage (sauf A_ctx_fixe) ; L* fixe.
Couche L* (CLW-07) : sur le pli S, la plus petite des deux aires A_ctx (a→b et b→a), arrondie au millième, maximale ;
à égalité, le plus petit des deux d' le plus grand ; puis la plus basse. λ aux quatre profondeurs appariées, dans les
deux sens, en points.
Graines : `numpy.random.SeedSequence(ENTROPIE)` (R9).

Lecture mécanique (`lire`, δ = 0,25), en deux étapes (CLW-01, CLV-01).
  1. Chaque sens s certifié pour les deux modèles (borne basse de A_ctx_fixe_s ≥ 0,70) rend l'**ensemble** des issues
     dont toutes les conditions tiennent, dans l'ordre de lecture, en cinq étapes :
       1  fuite de signe inverse (petit)   borne haute de λ_s(petit) < −δ ;
          fuite de signe inverse (grand)   borne haute de λ_s(grand) < −δ ;
       2  positif   P(s) : borne basse de Δλ_s > δ, borne basse de λ_s(petit) > δ, borne basse de λ_s(grand) > −δ,
                    borne haute de λ_s(grand) < 1 ;
       3  inverse   I(s) : borne haute de Δλ_s < −δ, borne basse de λ_s(grand) > δ, borne basse de λ_s(petit) > −δ,
                    borne haute de λ_s(petit) < 1 ;
       4  pas de fuite   les deux intervalles de λ_s inclus dans [−δ ; δ] ;
       5  nul       intervalle de Δλ_s inclus dans [−δ ; δ].
     Les deux fuites de signe inverse forment la même étape : aucune ne passe avant l'autre. Un sens non certifié rend
     son échec : non certifiable (aucun modèle) ou certification asymétrique (grand seulement | petit seulement).
  2. Combinaison ; une issue est « commune » si elle tient dans les deux sens (pour la fuite de signe inverse : le même
     modèle sous −δ dans les deux sens ; pour « positif », « inverse » et « nul » : de plus, cohérence des deux sens,
     |e(m)| ≤ δ en point pour chacun des deux modèles, CLU-01) :
     aucun sens certifié                → l'échec commun s'il est le même dans les deux sens, sinon non certifiable ;
     les deux sens certifiés, une issue commune au moins → la **première étape qui porte une issue commune** ; à
          l'étape 1 : « fuite de signe inverse (petit) », « (grand) », ou « (petit et grand) » si les deux sont communes ;
          réserve obligatoire pour chaque issue tenue dans un seul sens et placée avant cette étape ou dans la même ;
          réserves propres à l'issue (CLW-02, CLT-01), restreintes aux modèles prononcés pour la fuite de signe
          inverse :
            « fuite non spécifique » : positif, borne basse de la spécificité ≤ 0 dans un sens au moins ; inverse,
              borne haute ≥ 0 ; fuite de signe inverse, borne basse de −λ − ν ≤ 0 dans un sens au moins, pour un
              modèle prononcé (la réserve le nomme) ;
            « profondeur », dans un sens au moins, trois des quatre profondeurs appariées contredisent l'issue :
              positif et inverse, Δλ de signe contraire ; fuite de signe inverse, λ > 0 pour un modèle prononcé (la
              réserve le nomme) ; pas de fuite, |λ| > δ pour un modèle ; nul, |Δλ| > δ ;
            « λ change d'un sens à l'autre » (positif, inverse, nul) : l'intervalle de e(m) exclut zéro, pour un
              modèle (la réserve le nomme) ;
            « jeux de force de contexte inégale » (positif, inverse, nul) : pour un modèle (nommé), le rapport des Ec
              des deux sens, en point, ou son inverse, dépasse 1,15, ou n'est pas défini (un Ec ≤ 0) ;
     aucune issue commune, chaque sens en tient une  → « désaccord des deux sens (cohérence) » si une issue au moins
          est tenue dans les deux sens sans la cohérence (« positif », « inverse » ou « nul ») ; sinon « désaccord des
          deux sens » (issues différentes, dont la fuite de signe inverse tenue par un modèle dans un sens et par
          l'autre dans l'autre sens) ;
     aucune issue commune, un seul sens en tient   → « X non confirmé (sens de l'autre) », X la première étape tenue ;
          un sens non certifié ne tient aucune issue ;
     aucun                              → indécis.
     « X non confirmé », les deux désaccords, « indécis » et les échecs de certification ne portent aucune
     réserve. Pour chaque issue tenue dans un seul sens, ce qui lui manque dans l'autre sens est rapporté, chiffré
     (CLV-07) ; pour chaque issue tenue dans les deux sens sans la cohérence, l'écart de chaque modèle qui la rompt
     (CLU-01). Une telle issue ne précède jamais l'étape prononcée : « positif » et « inverse » excluent toute autre
     issue d'un sens, et « nul » est la dernière étape ; elle ne porte donc pas de réserve.

Usage (décisif) :    python -I -B analyser_echelle_v9.py STIMULI PETIT GRAND ENTROPIE SORTIE --commit-attendu COMMIT
Usage (répétition) : python -I -B analyser_echelle_v9.py STIMULI PETIT GRAND ENTROPIE SORTIE --repetition
Mode décisif (CLY-06, CLW-04) : commit des scripts égal à COMMIT, arbre des scripts propre, numpy 2.4.6, modèles
attendus, et mesure faite par `mesurer_echelle_v9.py` de cet arbre (nom et empreinte relus dans chaque manifeste).
Codes : 0 analyse écrite ; 1 arrêt (liste d'arrêt) ; 2 usage ou sortie déjà présente.
"""
import hashlib
import itertools
import json
import pathlib
import platform
import re
import subprocess
import sys

import numpy as np

SEUILS = {"certification_A_ctx": 0.70, "delta": 0.25, "lambda_max": 1.0,
          "rapport_Ec_max": 1.15}         # max(q, 1/q) au plus, q = Ec_a→b / Ec_b→a ; fixé avant toute mesure (CLT-01)
ATTENDUS = {
    "petit": {"modele": "meta-llama/Llama-3.1-8B-Instruct", "revision": "0e9e39f249a16976918f6564b8830bc894c89659",
              "couches": [8, 12, 16, 20], "dimension": 4096},
    "grand": {"modele": "meta-llama/Llama-3.1-70B-Instruct", "revision": "1605565b47bb9346c5515c34102e054115b4f98b",
              "couches": [20, 30, 40, 50], "dimension": 8192},
}
NUMPY_ATTENDU = "2.4.6"
SCRIPT_MESURE = "mesurer_echelle_v9.py"     # mode décisif : nom et empreinte relus dans chaque manifeste (CLW-04)
N_BOOT = 2000
FORMATS = ("qcm", "prose")
CLASSES = ("eval", "reel")
N_PAIRES = 6
SENS = {"ab": ("a", "b"), "ba": ("b", "a")}
PARTITIONS = [tuple(1.0 if j in g else -1.0 for j in range(N_PAIRES))
              for g in itertools.combinations(range(N_PAIRES), 3) if 0 in g]
SANS_INTERVALLE = ("lambda_app", "transfert", "Ec_qcm", "Ec_prose", "dprime")


class Arret(Exception):
    pass


def empreinte(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def verifier_compagnon(f):
    f = pathlib.Path(f)
    c = f.parent / (f.name + ".sha256")
    if not f.is_file():
        raise Arret(f"{f.name} : fichier absent")
    if not c.is_file():
        raise Arret(f"{f.name} : compagnon d'empreinte absent")
    if empreinte(f) != c.read_text(encoding="utf-8").split()[0]:
        raise Arret(f"{f.name} : empreinte ≠ compagnon")


def auroc_pondere(pos, wpos, neg, wneg):
    """Aire de Mann–Whitney pondérée (poids entiers = tirage avec remise) ; ex aequo comptés pour moitié."""
    m_pos, m_neg = wpos > 0, wneg > 0
    pos, wpos, neg, wneg = pos[m_pos], wpos[m_pos], neg[m_neg], wneg[m_neg]
    tp, tn = wpos.sum(), wneg.sum()
    if tp <= 0 or tn <= 0:
        raise Arret("aire : une classe vide")
    ordre = np.argsort(neg, kind="mergesort")
    neg_s, wneg_s = neg[ordre], wneg[ordre]
    cum = np.concatenate([[0.0], np.cumsum(wneg_s)])
    bas = np.searchsorted(neg_s, pos, side="left")
    haut = np.searchsorted(neg_s, pos, side="right")
    gagnes = cum[bas] + 0.5 * (cum[haut] - cum[bas])
    return float((wpos * gagnes).sum() / (tp * tn))


def charger_stimuli(chemin):
    doc = json.loads(pathlib.Path(chemin).read_text(encoding="utf-8"))
    if doc.get("version") != "echelle-v2":
        raise Arret("stimuli : version echelle-v2 attendue")
    st = doc["stimuli"]
    tab = {k: np.array([s[k] for s in st]) for k in ("contenu", "pli", "jeu", "paire", "classe", "format")}
    tab["id"] = [s["id"] for s in st]
    tab["texte"] = [s["messages"][-1]["content"] for s in st]
    return doc, tab


def charger_modele(dossier, tab, sha_stimuli, attendu, repetition):
    """Gardes d'identité et d'intégrité, puis activations en float32."""
    dossier = pathlib.Path(dossier)
    verifier_compagnon(dossier / "manifeste-mesure.json")
    m = json.loads((dossier / "manifeste-mesure.json").read_text(encoding="utf-8"))
    verifier_compagnon(dossier / "ids.json")
    if m["sha256_sorties"].get("ids.json") != empreinte(dossier / "ids.json"):
        raise Arret(f"{dossier.name}/ids.json : empreinte ≠ manifeste")
    ids = json.loads((dossier / "ids.json").read_text(encoding="utf-8"))
    if ids != tab["id"]:
        raise Arret(f"{dossier.name} : ordre des identifiants ≠ stimuli")
    if m.get("sha256_stimuli") != sha_stimuli:
        raise Arret(f"{dossier.name} : mesuré sur d'autres stimuli que ceux analysés")
    if m.get("limite") is not None:
        raise Arret(f"{dossier.name} : mesure limitée (essai), pas une mesure complète")
    if not repetition:
        for k in ("modele", "revision", "couches", "dimension"):
            if m.get(k) != attendu[k]:
                raise Arret(f"{dossier.name} : {k} = {m.get(k)} ≠ {attendu[k]} attendu")
        if m.get("type_nombre") != "bfloat16":
            raise Arret(f"{dossier.name} : type {m.get('type_nombre')} ≠ bfloat16")
        if m.get("script") != SCRIPT_MESURE:
            raise Arret(f"{dossier.name} : mesuré par {m.get('script')} ≠ {SCRIPT_MESURE}")
        if m.get("sha256_script") != empreinte(pathlib.Path(__file__).resolve().parent / SCRIPT_MESURE):
            raise Arret(f"{dossier.name} : empreinte du script de mesure ≠ celle de {SCRIPT_MESURE} de cet arbre")
    X = {}
    for c in m["couches"]:
        f = dossier / f"activations-L{c}.npy"
        verifier_compagnon(f)
        if m["sha256_sorties"].get(f.name) != empreinte(f):
            raise Arret(f"{f.name} : empreinte ≠ manifeste")
        a = np.load(f).astype(np.float32)
        if a.shape != (len(ids), m["dimension"]):
            raise Arret(f"{f.name} : forme {a.shape} inattendue")
        if not np.all(np.isfinite(a)):
            raise Arret(f"{f.name} : valeur non finie")
        X[c] = a
    return m, X


class Plan:
    """Index des lignes par (moitié, jeu, paire, classe, format) et poids d'un tirage."""

    def __init__(self, tab):
        self.t = tab
        self.n = len(tab["id"])
        self.decalage = {"a": 0, "b": N_PAIRES}
        self.indice_paire = np.array([self.decalage[j] + p for j, p in zip(tab["jeu"], tab["paire"])])

    def poids(self, wc, wp):
        return wc[self.t["contenu"]] * np.concatenate([wp["a"], wp["b"]])[self.indice_paire]

    def masque(self, contenus, jeu, classe=None, fmt=None, paire=None):
        m = np.isin(self.t["contenu"], contenus) & (self.t["jeu"] == jeu)
        if classe is not None:
            m &= self.t["classe"] == classe
        if fmt is not None:
            m &= self.t["format"] == fmt
        if paire is not None:
            m &= self.t["paire"] == paire
        return m


def moyenne(X, w, m):
    ww = w * m
    s = ww.sum()
    if s <= 0:
        raise Arret("moyenne sur un ensemble vide")
    idx = np.flatnonzero(ww)
    return (ww[idx] @ X[idx]) / s


def normer(d):
    n = np.linalg.norm(d)
    if not np.isfinite(n) or n == 0:
        raise Arret("direction nulle ou non finie")
    return d / n


def differences_paires(plan, X, w, app, jeu):
    """Pour chaque paire j du jeu d'apprentissage (moitié app) : D_j = moyenne(eval) − moyenne(reel), et son poids."""
    D, p = [], []
    for j in range(N_PAIRES):
        m1, m0 = plan.masque(app, jeu, "eval", paire=j), plan.masque(app, jeu, "reel", paire=j)
        poids = float((w * m1).sum())
        if poids <= 0:
            D.append(None)
            p.append(0.0)
        else:
            D.append(moyenne(X, w, m1) - moyenne(X, w, m0))
            p.append(poids)
    return D, np.array(p)


def direction_contexte(plan, X, w, app, jeu):
    D, p = differences_paires(plan, X, w, app, jeu)
    if p.sum() <= 0:
        raise Arret("aucune paire d'apprentissage")
    return normer(sum(pj * Dj for pj, Dj in zip(p, D) if Dj is not None) / p.sum()), D, p


def stats_projections(plan, s, w, mesure):
    t = plan.t

    def cellule(classe, fmt):
        m = mesure & (t["classe"] == classe) & (t["format"] == fmt)
        return s[m], w[m]

    def wm(classe, fmt):
        v, ww = cellule(classe, fmt)
        return float((ww @ v) / ww.sum())

    ec_f = {f: wm("eval", f) - wm("reel", f) for f in FORMATS}
    ec = float(np.mean(list(ec_f.values())))
    ef = float(np.mean([wm(k, "qcm") - wm(k, "prose") for k in CLASSES]))
    a_ctx = float(np.mean([auroc_pondere(*cellule("eval", f), *cellule("reel", f)) for f in FORMATS]))
    a_conf = auroc_pondere(*cellule("eval", "prose"), *cellule("reel", "qcm"))
    variances = []
    for k in CLASSES:
        for f in FORMATS:
            v, ww = cellule(k, f)
            mu = (ww @ v) / ww.sum()
            variances.append(float((ww @ (v - mu) ** 2) / ww.sum()))
    dprime = ec / np.sqrt(np.mean(variances)) if np.mean(variances) > 0 else float("nan")
    return {"Ec": ec, "Ef": ef, "Ec_qcm": ec_f["qcm"], "Ec_prose": ec_f["prose"], "A_ctx": a_ctx, "A_conf": a_conf,
            "dprime": float(dprime)}


def effet_format(plan, s, w, mesure):
    t, out = plan.t, []
    for k in CLASSES:
        moy = {}
        for f in FORMATS:
            m = mesure & (t["classe"] == k) & (t["format"] == f)
            moy[f] = float(((w * m) @ np.nan_to_num(s)) / (w * m).sum())
        out.append(moy["qcm"] - moy["prose"])
    return float(np.mean(out))


def centrer(s, w, m):
    ww = w * m
    s[m] = s[m] - float((ww[m] @ s[m]) / ww[m].sum())


def mesures_couche(plan, X, w, moities, sens="ab", directions_fixes=None):
    """Toutes les mesures d'une couche, pour un sens et un jeu de poids (ajustement croisé sur deux moitiés)."""
    jeu_app, jeu_mes = SENS[sens]
    n = plan.n
    s, s_app, s_t1, s_fixe = (np.full(n, np.nan) for _ in range(4))
    s_perm = np.full((len(PARTITIONS), n), np.nan)
    mesure, mesure_app = np.zeros(n, dtype=bool), np.zeros(n, dtype=bool)
    perm_valide = np.ones(len(PARTITIONS), dtype=bool)
    for k, (app, mes) in enumerate(((moities[0], moities[1]), (moities[1], moities[0]))):
        c, D, p = direction_contexte(plan, X, w, app, jeu_app)
        t1 = normer(moyenne(X, w, plan.masque(app, jeu_app, "eval", "qcm"))
                    - moyenne(X, w, plan.masque(app, jeu_app, "reel", "prose")))
        mm, ma = plan.masque(mes, jeu_mes), plan.masque(mes, jeu_app)
        s[mm], s_app[ma], s_t1[mm] = X[mm] @ c, X[ma] @ c, X[mm] @ t1
        for v, m in ((s, mm), (s_app, ma), (s_t1, mm)):
            centrer(v, w, m)
        if directions_fixes is not None:
            s_fixe[mm] = X[mm] @ directions_fixes[k]
            centrer(s_fixe, w, mm)
        for i, sigma in enumerate(PARTITIONS):
            plus = [j for j in range(N_PAIRES) if sigma[j] > 0 and p[j] > 0]
            moins = [j for j in range(N_PAIRES) if sigma[j] < 0 and p[j] > 0]
            if not plus or not moins:
                perm_valide[i] = False
                continue
            g = sum(p[j] * D[j] for j in plus) / sum(p[j] for j in plus) \
                - sum(p[j] * D[j] for j in moins) / sum(p[j] for j in moins)
            g = g - (g @ c) * c                                       # orthogonalisée par rapport à ĉ (CLY-02)
            s_perm[i, mm] = X[mm] @ normer(g)
            centrer(s_perm[i], w, mm)
        mesure |= mm
        mesure_app |= ma
    r = stats_projections(plan, s, w, mesure)
    if r["Ec"] == 0:
        raise Arret("effet du contexte nul")
    r["lambda"] = r["Ef"] / r["Ec"]
    ra = stats_projections(plan, s_app, w, mesure_app)
    r["lambda_app"] = ra["Ef"] / ra["Ec"] if ra["Ec"] != 0 else float("nan")
    r["transfert"] = r["Ec"] / ra["Ec"] if ra["Ec"] != 0 else float("nan")
    r["A_conf_T1"] = stats_projections(plan, s_t1, w, mesure)["A_conf"]
    if directions_fixes is not None:
        r["A_ctx_fixe"] = stats_projections(plan, s_fixe, w, mesure)["A_ctx"]
    efs = [effet_format(plan, s_perm[i], w, mesure) for i in range(len(PARTITIONS)) if perm_valide[i]]
    if not efs:
        raise Arret("témoin de permutation : aucune partition valide")
    r["nu"] = float(np.mean(np.abs(efs)) / abs(r["Ec"]))
    return r


def directions_apprises(plan, X, moities, sens):
    w = np.ones(plan.n)
    return [direction_contexte(plan, X, w, app, SENS[sens][0])[0] for app in (moities[0], moities[1])]


def choisir_couche(plan, X, s_moities):
    """Sur le pli S, dans les deux sens (CLW-07) : la plus petite des deux aires A_ctx, arrondie au millième, maximale ;
    à égalité, le plus petit des deux d' le plus grand ; puis la plus basse."""
    w = np.ones(plan.n)
    notes, par_sens = {}, {}
    for c in sorted(X):
        r = {s: mesures_couche(plan, X[c], w, s_moities, s) for s in SENS}
        notes[c] = (round(min(r[s]["A_ctx"] for s in SENS), 3), min(r[s]["dprime"] for s in SENS))
        par_sens[str(c)] = {s: {"A_ctx": round(r[s]["A_ctx"], 3), "dprime": r[s]["dprime"]} for s in SENS}
    meilleure = max(sorted(notes), key=lambda c: (notes[c][0], notes[c][1], -c))
    return meilleure, {str(c): {"A_ctx_min": v[0], "dprime_min": v[1], "par_sens": par_sens[str(c)]}
                       for c, v in notes.items()}


def sac(textes, vocab=None):
    mots = [re.findall(r"[a-z]+", t.lower()) for t in textes]
    if vocab is None:
        vocab = sorted({m for ms in mots for m in ms})
    ix = {m: k for k, m in enumerate(vocab)}
    M = np.zeros((len(textes), len(vocab)))
    for i, ms in enumerate(mots):
        for m in ms:
            if m in ix:
                M[i, ix[m]] += 1
    return np.log1p(M), vocab


def logistique(X, y, c=1.0, iterations=3000, pas=0.1):
    n, d = X.shape
    w, b = np.zeros(d), 0.0
    for _ in range(iterations):
        p = 1.0 / (1.0 + np.exp(-np.clip(X @ w + b, -30, 30)))
        g = p - y
        w -= pas * (X.T @ g / n + w / (c * n))
        b -= pas * g.mean()
    return w, b


def scores_sac(plan, moities, sens="ab"):
    """Sac de mots appris sur les textes du jeu d'apprentissage d'une moitié, appliqué au jeu de mesure de l'autre ;
    scores bruts ; dans le sens a→b ou b→a (CLW-07)."""
    t = plan.t
    jeu_app, jeu_mes = SENS[sens]
    s = np.full(plan.n, np.nan)
    for app, mes in ((moities[0], moities[1]), (moities[1], moities[0])):
        ma = plan.masque(app, jeu_app)
        Xa, vocab = sac([x for x, k in zip(t["texte"], ma) if k])
        w, b = logistique(Xa, (t["classe"][ma] == "eval").astype(float))
        mb = plan.masque(mes, jeu_mes)
        Xb, _ = sac([x for x, k in zip(t["texte"], mb) if k], vocab)
        s[mb] = Xb @ w + b
    return s


def aire_sac(plan, s_brut, w, moities, sens="ab"):
    s = s_brut.copy()
    for mes in moities:
        centrer(s, w, plan.masque(mes, SENS[sens][1]))
    return stats_projections(plan, s, w, ~np.isnan(s))["A_ctx"]


def tirer(rng, moities, compteur):
    """Contenus avec remise dans chaque moitié ; paires avec remise dans chaque jeu, sous la condition d'au moins deux
    paires distinctes par jeu (sinon le témoin de permutation n'est pas défini) ; chaque rejet est compté."""
    wc = np.zeros(64)
    for moitie in moities:
        np.add.at(wc, rng.choice(moitie, size=len(moitie), replace=True), 1.0)
    wp = {}
    for jeu in ("a", "b"):
        while True:
            w = np.bincount(rng.integers(0, N_PAIRES, size=N_PAIRES), minlength=N_PAIRES).astype(float)
            if (w > 0).sum() >= 2:
                break
            compteur[jeu] += 1
        wp[jeu] = w
    return wc, wp


def intervalle(v):
    v = np.asarray(v, dtype=float)
    if v.size == 0 or not np.all(np.isfinite(v)):
        raise Arret("tirage de bootstrap non fini")
    return [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))]


CERTIFICATION = ("non certifiable", "certification asymétrique (grand seulement)",
                 "certification asymétrique (petit seulement)")
FSI = {"petit": "fuite de signe inverse (petit)", "grand": "fuite de signe inverse (grand)"}
FSI_DEUX = "fuite de signe inverse (petit et grand)"
ISSUES = (FSI["petit"], FSI["grand"], "positif", "inverse", "pas de fuite", "nul")   # dans l'ordre de lecture d'un sens
ETAPE = {FSI["petit"]: 1, FSI["grand"]: 1, "positif": 2, "inverse": 3, "pas de fuite": 4, "nul": 5}   # CLV-01
NOM_SENS = {"ab": "a→b", "ba": "b→a"}


def certification(r, s):
    return {k: r[k][s]["A_ctx_fixe_ic"][0] >= SEUILS["certification_A_ctx"] for k in ("petit", "grand")}


def conditions(r, s):
    """Conditions de chaque issue dans le sens s : listes de (énoncé chiffré, tenue)."""
    S, d = SEUILS, SEUILS["delta"]
    lp, lg, dl = r["petit"][s]["lambda_ic"], r["grand"][s]["lambda_ic"], r["delta_lambda_ic"][s]
    n = NOM_SENS[s]

    def ic(v):
        return f"[{v[0]:.3f} ; {v[1]:.3f}]"

    return {
        FSI["petit"]: [(f"borne haute de λ_{n}(petit) {lp[1]:.3f} < −δ", lp[1] < -d)],          # CLV-01
        FSI["grand"]: [(f"borne haute de λ_{n}(grand) {lg[1]:.3f} < −δ", lg[1] < -d)],
        "positif": [(f"borne basse de Δλ_{n} {dl[0]:.3f} > δ", dl[0] > d),
                    (f"borne basse de λ_{n}(petit) {lp[0]:.3f} > δ", lp[0] > d),
                    (f"borne basse de λ_{n}(grand) {lg[0]:.3f} > −δ", lg[0] > -d),
                    (f"borne haute de λ_{n}(grand) {lg[1]:.3f} < 1", lg[1] < S["lambda_max"])],
        "inverse": [(f"borne haute de Δλ_{n} {dl[1]:.3f} < −δ", dl[1] < -d),
                    (f"borne basse de λ_{n}(grand) {lg[0]:.3f} > δ", lg[0] > d),
                    (f"borne basse de λ_{n}(petit) {lp[0]:.3f} > −δ", lp[0] > -d),
                    (f"borne haute de λ_{n}(petit) {lp[1]:.3f} < 1", lp[1] < S["lambda_max"])],
        "pas de fuite": [(f"λ_{n}(petit) {ic(lp)} dans [−δ ; δ]", -d <= lp[0] and lp[1] <= d),
                         (f"λ_{n}(grand) {ic(lg)} dans [−δ ; δ]", -d <= lg[0] and lg[1] <= d)],
        "nul": [(f"Δλ_{n} {ic(dl)} dans [−δ ; δ]", -d <= dl[0] and dl[1] <= d)],
    }


COHERENCE = ("positif", "inverse", "nul")       # issues qui comparent les deux modèles (CLU-01, CLT-01)
DESACCORD = "désaccord des deux sens"
DESACCORD_COHERENCE = "désaccord des deux sens (cohérence)"     # issue tenue dans les deux sens sans la cohérence


def coherence(r):
    """Cohérence des deux sens (CLU-01) : pour chaque modèle, l'écart ponctuel e(m) = λ_a→b(m) − λ_b→a(m), à la couche
    L*, vérifie |e(m)| ≤ δ ; son intervalle (mêmes tirages) est rapporté avec lui. Liste de (énoncé chiffré, tenue)."""
    d = SEUILS["delta"]
    out = []
    for k in ("petit", "grand"):
        e, ic = r["ecart_sens"][k], r["ecart_sens_ic"][k]
        out.append((f"cohérence des deux sens du {k} : |λ_a→b − λ_b→a| = |{e:.3f}| ≤ δ (intervalle "
                    f"[{ic[0]:.3f} ; {ic[1]:.3f}])", abs(e) <= d))
    return out


def echec_certification(r, s):
    """Échec de certification du sens s, ou None si les deux modèles y sont certifiés."""
    c = certification(r, s)
    if not c["petit"] and not c["grand"]:
        return "non certifiable"
    if not c["petit"]:
        return "certification asymétrique (grand seulement)"
    if not c["grand"]:
        return "certification asymétrique (petit seulement)"
    return None


def issues_tenues(r, s):
    """Issues dont toutes les conditions tiennent dans le sens s, dans l'ordre de lecture (CLW-01) : « nul » peut tenir
    avec « pas de fuite » ou avec une fuite de signe inverse, et les deux fuites de signe inverse ensemble ;
    « positif » et « inverse » excluent toute autre issue."""
    cond = conditions(r, s)
    return [x for x in ISSUES if all(tenue for _, tenue in cond[x])]


def premiere_etape(issues):
    """Nom de la première étape de l'ordre de lecture parmi `issues` : les deux fuites de signe inverse de l'étape 1 se
    nomment ensemble, « fuite de signe inverse (petit et grand) » (CLV-01)."""
    e = min(ETAPE[x] for x in issues)
    etape = [x for x in ISSUES if x in issues and ETAPE[x] == e]
    return FSI_DEUX if len(etape) == 2 else etape[0]


def membres(issue):
    """Issues d'un sens que recouvre un nom prononcé."""
    return (FSI["petit"], FSI["grand"]) if issue == FSI_DEUX else (issue,)


def lire_sens(r, s):
    """Lecture d'un seul sens, rapportée : son échec de certification, sinon sa première étape tenue, sinon indécis."""
    e = echec_certification(r, s)
    if e:
        return e
    tenues = issues_tenues(r, s)
    return premiere_etape(tenues) if tenues else "indécis"


def manquantes(r, s, issue):
    """Ce qui manque à l'issue dans le sens s : certification, puis conditions qui ne tiennent pas (CLZ-02)."""
    out = [f"certification {NOM_SENS[s]} du {k} : borne basse de A_ctx_fixe {r[k][s]['A_ctx_fixe_ic'][0]:.3f} < "
           f"{SEUILS['certification_A_ctx']}" for k, ok in certification(r, s).items() if not ok]
    return out + [enonce for enonce, tenue in conditions(r, s)[issue] if not tenue]


NON_SPECIFIQUE = "fuite non spécifique : l'effet ne dépasse pas celui du témoin de permutation"
CHANGE_DE_SENS = ("le λ du {m} change d'un sens à l'autre : λ_a→b − λ_b→a = {e:.3f}, intervalle [{b:.3f} ; {h:.3f}], "
                  "qui exclut zéro : l'écart d'échelle peut être porté en partie par des modèles différents dans les "
                  "deux sens (CLT-01)")
CONTEXTE_INEGAL = ("jeux de force de contexte inégale ({m}) : Ec_a→b / Ec_b→a = {q}, hors de [1/1,15 ; 1,15] : la "
                   "cohérence des deux sens et λ ne se comparent plus d'un sens à l'autre (CLT-01, CLT-02)")
PROFONDEUR = {
    "positif": "profondeur : dans un sens au moins, trois des quatre Δλ aux profondeurs appariées ont le signe contraire",
    "inverse": "profondeur : dans un sens au moins, trois des quatre Δλ aux profondeurs appariées ont le signe contraire",
    FSI["petit"]: "profondeur : dans un sens au moins, λ(petit) est positif à trois des quatre profondeurs appariées",
    FSI["grand"]: "profondeur : dans un sens au moins, λ(grand) est positif à trois des quatre profondeurs appariées",
    "pas de fuite": "profondeur : dans un sens au moins, |λ| dépasse δ à trois des quatre profondeurs appariées pour un "
                    "modèle",
    "nul": "profondeur : dans un sens au moins, |Δλ| dépasse δ à trois des quatre profondeurs appariées",
}


def rapport_hors_bande(q):
    """Rapport des Ec hors de [1/1,15 ; 1,15] (max(q, 1/q) > 1,15), ou non défini (None : un Ec ≤ 0)."""
    return q is None or max(q, 1 / q) > SEUILS["rapport_Ec_max"]


def reserves(r, issue):
    """Réserves propres au nom prononcé (CLW-02, CLT-01) : spécificité, profondeur, puis, pour « positif », « inverse »
    et « nul », λ qui change d'un sens à l'autre et jeux de force de contexte inégale, modèle par modèle ; pour la fuite
    de signe inverse, restreintes aux modèles prononcés, qui sont sous −δ dans les deux sens (CLV-01)."""
    out = []
    sp = r["specificite_ic"]
    if issue == "positif" and min(sp["ab"][0], sp["ba"][0]) <= 0:
        out.append(NON_SPECIFIQUE)
    if issue == "inverse" and max(sp["ab"][1], sp["ba"][1]) >= 0:
        out.append(NON_SPECIFIQUE)
    for k in ("petit", "grand"):
        if FSI[k] in membres(issue) and any(r["specificite_signe_inverse_ic"][k][s][0] <= 0 for s in SENS):
            out.append(f"{NON_SPECIFIQUE} ({k})")
    for x in membres(issue):
        if any(r["profondeur_contraire"][x].values()):
            out.append(PROFONDEUR[x])
    if issue in COHERENCE:                                                     # CLT-01
        for k in ("petit", "grand"):
            b, h = r["ecart_sens_ic"][k]
            if b > 0 or h < 0:
                out.append(CHANGE_DE_SENS.format(m=k, e=r["ecart_sens"][k], b=b, h=h))
        for k in ("petit", "grand"):
            q = r["rapport_Ec"][k]
            if rapport_hors_bande(q):
                out.append(CONTEXTE_INEGAL.format(m=k, q="non défini (un Ec ≤ 0)" if q is None else f"{q:.3f}"))
    return out


def lire(r):
    """Lecture mécanique (CLZ-01, CLW-01, CLV-01, CLU-01) : chaque sens rend l'ensemble des issues qu'il tient ; on
    prononce la première étape de l'ordre de lecture qui porte une issue commune (tenue dans les deux sens, et, pour
    « positif », « inverse » et « nul », sous la cohérence des deux sens). Rend (lecture, réserves, détail)."""
    echec = {s: echec_certification(r, s) for s in SENS}
    tenues = {s: ([] if echec[s] else issues_tenues(r, s)) for s in SENS}
    coh = coherence(r)
    detail = {"lecture_par_sens": {NOM_SENS[s]: lire_sens(r, s) for s in SENS},
              "issues_tenues_par_sens": {NOM_SENS[s]: tenues[s] for s in SENS}, "conditions_manquantes": {},
              "coherence_des_sens": [{"condition": enonce, "tenue": tenue} for enonce, tenue in coh]}
    if echec["ab"] and echec["ba"]:
        return (echec["ab"] if echec["ab"] == echec["ba"] else "non certifiable"), [], detail
    rompue = [enonce for enonce, tenue in coh if not tenue]
    deux = [x for x in ISSUES if x in tenues["ab"] and x in tenues["ba"]]             # tenues dans les deux sens
    incoherentes = [x for x in deux if x in COHERENCE and rompue]                     # sans la cohérence (CLU-01)
    communes = [x for x in deux if x not in incoherentes]
    seules = [(s, x) for s in SENS for x in tenues[s] if x not in deux]             # tenues dans un seul sens
    for s, x in seules:                                                             # ce qui leur manque (CLV-07)
        autre = "ba" if s == "ab" else "ab"
        detail["conditions_manquantes"][f"{x} ({NOM_SENS[s]}), dans le sens {NOM_SENS[autre]}"] = \
            manquantes(r, autre, x)
    for x in incoherentes:                                                          # ce qui leur manque (CLU-01)
        detail["conditions_manquantes"][f"{x} (a→b et b→a), cohérence des deux sens"] = rompue
    if communes:
        issue = premiere_etape(communes)
        etape = ETAPE[membres(issue)[0]]
        return issue, reserves(r, issue) + [f"{x} lu dans le seul sens {NOM_SENS[s]} (non confirmé)"
                                            for s, x in seules if ETAPE[x] <= etape], detail
    if tenues["ab"] and tenues["ba"]:
        return (DESACCORD_COHERENCE if incoherentes else DESACCORD), [], detail
    for s in SENS:
        if tenues[s]:
            return f"{premiere_etape(tenues[s])} non confirmé (sens {NOM_SENS['ba' if s == 'ab' else 'ab']})", [], detail
    return "indécis", [], detail


def etat_scripts():
    try:
        ici = pathlib.Path(__file__).resolve().parent
        c = subprocess.run(["git", "-C", str(ici), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=10)
        st = subprocess.run(["git", "-C", str(ici), "status", "--porcelain", "--", ".."], capture_output=True, text=True,
                            timeout=10)
        return (c.stdout.strip() or None), (st.returncode == 0 and st.stdout.strip() == "")
    except Exception:
        return None, None


def principal(argv):
    repetition = "--repetition" in argv
    argv = [a for a in argv if a != "--repetition"]
    commit_attendu = None
    if "--commit-attendu" in argv:
        i = argv.index("--commit-attendu")
        commit_attendu = argv[i + 1] if i + 1 < len(argv) else ""
        argv = argv[:i] + argv[i + 2:]
    if len(argv) != 5 or (not repetition and not commit_attendu):
        print("usage : analyser_echelle_v9.py STIMULI PETIT GRAND ENTROPIE SORTIE (--commit-attendu C | --repetition)",
              file=sys.stderr)
        return 2
    stimuli, d_petit, d_grand, entropie, sortie = argv
    sortie = pathlib.Path(sortie)
    if sortie.exists():
        print(f"{sortie} existe déjà (R12)", file=sys.stderr)
        return 2
    commit, propre = etat_scripts()
    try:
        if not repetition:
            if commit != commit_attendu:
                raise Arret(f"commit des scripts {commit} ≠ {commit_attendu} attendu")
            if propre is not True:
                raise Arret("arbre des scripts non propre")
            if np.__version__ != NUMPY_ATTENDU:
                raise Arret(f"numpy {np.__version__} ≠ {NUMPY_ATTENDU}")
        doc, tab = charger_stimuli(stimuli)
        sha_stim = empreinte(stimuli)
        plan = Plan(tab)
        modeles = {nom: charger_modele(d, tab, sha_stim, ATTENDUS[nom], repetition)
                   for nom, d in (("petit", d_petit), ("grand", d_grand))}
        mp, mg = modeles["petit"][0], modeles["grand"][0]
        if mp.get("rendu_premier") != mg.get("rendu_premier"):
            raise Arret("gabarit de dialogue différent entre les deux modèles")
        if mp.get("dernier_jeton") != mg.get("dernier_jeton"):
            raise Arret("dernier jeton différent entre les deux modèles")
        if int(tab["contenu"].max()) + 1 != 64:
            raise Arret("64 contenus attendus")
        plis = {p: np.unique(tab["contenu"][tab["pli"] == p]) for p in ("S1", "S2", "E1", "E2")}
        s_moities, e_moities = (plis["S1"], plis["S2"]), (plis["E1"], plis["E2"])
        if min(len(v) for v in plis.values()) < 4:
            raise Arret("plis trop petits")
        res = {}
        uns = np.ones(plan.n)
        for nom, (m, X) in modeles.items():
            L, choix = choisir_couche(plan, X, s_moities)
            profondeurs = {s: {str(c): mesures_couche(plan, X[c], uns, e_moities, s)["lambda"] for c in sorted(X)}
                           for s in SENS}
            res[nom] = {"modele": m["modele"], "revision": m["revision"], "couche": L, "choix_couche": choix,
                        "couches": m["couches"], "lambda_par_couche": profondeurs, "XL": X[L],
                        "fixes": {s: directions_apprises(plan, X[L], e_moities, s) for s in SENS}}

        def un_tirage(wc, wp):
            w = plan.poids(wc, wp)
            return {nom: {s: mesures_couche(plan, res[nom]["XL"], w, e_moities, s, res[nom]["fixes"][s]) for s in SENS}
                    for nom in ("petit", "grand")}

        uns_c, uns_p = np.ones(64), {j: np.ones(N_PAIRES) for j in ("a", "b")}
        point = un_tirage(uns_c, uns_p)
        rng = np.random.default_rng(np.random.SeedSequence(int(entropie)).spawn(2)[0])
        rejets = {"a": 0, "b": 0}
        tirages = [un_tirage(*tirer(rng, e_moities, rejets)) for _ in range(N_BOOT)]
        s_sac = {s: scores_sac(plan, e_moities, s) for s in SENS}                 # dans les deux sens (CLW-07)
        rng_sac = np.random.default_rng(np.random.SeedSequence(int(entropie)).spawn(2)[1])
        rejets_sac = {"a": 0, "b": 0}
        sac_point = {s: aire_sac(plan, s_sac[s], plan.poids(uns_c, uns_p), e_moities, s) for s in SENS}
        sac_tir = {s: [] for s in SENS}
        for _ in range(N_BOOT):
            w_sac = plan.poids(*tirer(rng_sac, e_moities, rejets_sac))      # mêmes tirages pour les deux sens
            for s in SENS:
                sac_tir[s].append(aire_sac(plan, s_sac[s], w_sac, e_moities, s))
        r = {"delta_lambda": {}, "delta_lambda_ic": {}, "specificite": {}, "specificite_ic": {}}
        for nom in ("petit", "grand"):
            r[nom] = {k: res[nom][k] for k in ("modele", "revision", "couche", "choix_couche", "couches",
                                                "lambda_par_couche")}
            for s in SENS:
                r[nom][s] = {}
                for k, v in point[nom][s].items():
                    r[nom][s][k] = v
                    if k not in SANS_INTERVALLE:
                        r[nom][s][k + "_ic"] = intervalle([t[nom][s][k] for t in tirages])
            r[nom]["marge_sur_sac"] = {s: point[nom][s]["A_ctx_fixe"] - sac_point[s] for s in SENS}
        for s in SENS:
            r["delta_lambda"][s] = point["petit"][s]["lambda"] - point["grand"][s]["lambda"]
            r["delta_lambda_ic"][s] = intervalle([t["petit"][s]["lambda"] - t["grand"][s]["lambda"] for t in tirages])
            spec = lambda t, s=s: (t["petit"][s]["lambda"] - t["grand"][s]["lambda"]) - (t["petit"][s]["nu"] - t["grand"][s]["nu"])
            r["specificite"][s] = spec(point)
            r["specificite_ic"][s] = intervalle([spec(t) for t in tirages])
        for k in ("A_ctx_fixe", "A_conf"):                                    # dans les deux sens (CLW-07)
            r["delta_" + k] = {s: point["grand"][s][k] - point["petit"][s][k] for s in SENS}
            r["delta_" + k + "_ic"] = {s: intervalle([t["grand"][s][k] - t["petit"][s][k] for t in tirages])
                                      for s in SENS}
        r["ecart_sens"], r["ecart_sens_ic"] = {}, {}          # λ_a→b(m) − λ_b→a(m), mêmes tirages (CLU-01)
        for nom in ("petit", "grand"):
            r["ecart_sens"][nom] = point[nom]["ab"]["lambda"] - point[nom]["ba"]["lambda"]
            r["ecart_sens_ic"][nom] = intervalle([t[nom]["ab"]["lambda"] - t[nom]["ba"]["lambda"] for t in tirages])
        r["rapport_Ec"], r["rapport_Ec_ic"] = {}, {}          # Ec_a→b(m) / Ec_b→a(m) : estime k (CLT-01, CLT-02)
        for nom in ("petit", "grand"):
            ab, ba = point[nom]["ab"]["Ec"], point[nom]["ba"]["Ec"]
            r["rapport_Ec"][nom] = ab / ba if ab > 0 and ba > 0 else None
            r["rapport_Ec_ic"][nom] = intervalle([t[nom]["ab"]["Ec"] / t[nom]["ba"]["Ec"] for t in tirages])
        r["specificite_signe_inverse"], r["specificite_signe_inverse_ic"] = {}, {}   # −λ − ν (CLW-02)
        for nom in ("petit", "grand"):
            r["specificite_signe_inverse"][nom] = {s: -point[nom][s]["lambda"] - point[nom][s]["nu"] for s in SENS}
            r["specificite_signe_inverse_ic"][nom] = {
                s: intervalle([-t[nom][s]["lambda"] - t[nom][s]["nu"] for t in tirages]) for s in SENS}
        d = SEUILS["delta"]
        couples = list(zip(sorted(res["petit"]["couches"]), sorted(res["grand"]["couches"])))
        r["delta_lambda_par_profondeur"], r["profondeur_contraire"] = {}, {x: {} for x in ISSUES}
        for s in SENS:                                    # dans les deux sens, pour chaque issue (CLZ-11, CLW-02)
            lp = [res["petit"]["lambda_par_couche"][s][str(cp)] for cp, _ in couples]
            lg = [res["grand"]["lambda_par_couche"][s][str(cg)] for _, cg in couples]
            dl = [a - b for a, b in zip(lp, lg)]
            r["delta_lambda_par_profondeur"][s] = dl
            quatre = len(couples) == 4
            signe = np.sign(r["delta_lambda"][s])
            contraire = bool(quatre and sum(np.sign(x) == -signe != 0 for x in dl) >= 3)
            r["profondeur_contraire"]["positif"][s] = contraire
            r["profondeur_contraire"]["inverse"][s] = contraire
            r["profondeur_contraire"]["nul"][s] = bool(quatre and sum(abs(x) > d for x in dl) >= 3)
            r["profondeur_contraire"]["pas de fuite"][s] = bool(
                quatre and any(sum(abs(x) > d for x in l) >= 3 for l in (lp, lg)))
            for nom, l in (("petit", lp), ("grand", lg)):          # modèle par modèle ; lu s'il est prononcé (CLV-01)
                r["profondeur_contraire"][FSI[nom]][s] = bool(quatre and sum(x > 0 for x in l) >= 3)
        r["sac_de_mots"] = {s: {"A_ctx": sac_point[s], "A_ctx_ic": intervalle(sac_tir[s])} for s in SENS}
        lecture, reserves_lues, detail = lire(r)
    except Arret as e:
        print(f"arrêt : {e}", file=sys.stderr)
        return 1
    if repetition:
        lecture = f"répétition, non décisive ({lecture})"
    sortie.mkdir(parents=True)
    out = {"version": "analyse-echelle-v9", "repetition": repetition, "stimuli": pathlib.Path(stimuli).name,
           "sha256_stimuli": sha_stim, "resultats": {"petit": str(d_petit), "grand": str(d_grand)},
           "manifestes_sha256": {k: empreinte(pathlib.Path(d) / "manifeste-mesure.json")
                                 for k, d in (("petit", d_petit), ("grand", d_grand))},
           "entropie": int(entropie), "n_boot": N_BOOT, "seuils": SEUILS, "partitions": len(PARTITIONS),
           "tirages_paires_rejetes": rejets, "tirages_paires_rejetes_sac": rejets_sac,
           "script": pathlib.Path(__file__).name, "sha256_script": empreinte(__file__), "commit_scripts": commit,
           "commit_attendu": commit_attendu, "arbre_scripts_propre": propre, "python": platform.python_version(),
           "numpy": np.__version__, **r, "lecture": lecture, "reserves": reserves_lues, **detail}
    f = sortie / "analyse-echelle-v9.json"
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (sortie / (f.name + ".sha256")).write_text(f"{empreinte(f)}  {f.name}\n", encoding="utf-8")
    print(json.dumps({"lecture": lecture, "reserves": reserves_lues, **detail}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
