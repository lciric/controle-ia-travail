"""B7, M9 — l'étalonnage des réglages, sur des graines d'étalonnage (jamais celles des tirages décisifs ; étape 6).

Pour chaque proposeur réglable, chaque dose et chaque taille réduite visée, le réglage est trouvé par dichotomie sur des graines
communes, sur 200 000 sources d'étalonnage, chaque continuation y étant jouée avec sa jumelle (même source, même bras, même
suite de mondes ; graines d'échantillonnage seules différentes), jusqu'à ce que la taille réduite estimée soit à 0,02 près de la
cible : contraste de l'héritage pour K, φ et γ (à dose nulle pour φ et γ) ; contraste de la tenue pour τ. Une cible est
atteignable si la taille au réglage maximal l'atteint ; sinon elle est écrite « non atteignable ». La taille réduite est l'écart
moyen du contraste divisé par l'écart-type des différences de M1 entre jumelles, tous bras réunis (racine de la moyenne des carrés
des écarts-types par bras). Les proposeurs sans réglage sont joués de même, pour leur seul écart-type entre jumelles.

Garde 22 : étalonner n'est pas lire un critère. Pendant l'étalonnage, le verrou du test est levé (tout appel au test lève), et
la sortie n'a que des écarts moyens, des écarts-types et des réglages (`CLES_PERMISES`) ; tout autre champ arrête.

Code v4, note D8 (B7, version 7) : un écart-type entre jumelles nul ou non fini, ou une taille réduite non finie, arrête
l'étalonnage (`ArretEtalonnage`, avec sa cause) ; ce n'est pas « non atteignable », qui se dit d'une taille que le réglage maximal
n'atteint pas. Le contrôle porte sur l'écart-type réuni (celui qui divise l'écart moyen et qui est gelé), à chaque évaluation de
la dichotomie comme pour les proposeurs sans réglage.
"""

import contextlib
import hashlib
import json
import math
import os

import numpy as np

from . import rangs_signes as RS
from .constantes import LOT_DE_SOURCES, PAS_DICHOTOMIE_MAX, REPERE_LECTURE, TOLERANCE_ETALONNAGE
from .statistique import bras_de, simuler

CLES_PERMISES = {"proposeur", "dose", "taux", "contraste", "cible", "reglage", "nom_du_reglage", "taille_estimee",
                 "ecart_moyen", "ecart_type_jumelles", "ecart_type_jumelles_par_bras", "atteignable", "pas", "sources",
                 "repere", "retrait", "repli", "ecarts_moyens_par_bras", "statut"}
PLAGES = {"K": (0.0, 256.0), "tau": (0.0, 4.0), "phi": (0.0, 4.0), "gamma": (0.0, 1.0)}
CONTRASTE_DU_REGLAGE = {"K": "heritage", "tau": "tenue", "phi": "heritage", "gamma": "heritage"}


class ArretEtalonnage(RuntimeError):
    pass


@contextlib.contextmanager
def verrou():
    """Garde 22 : tout appel au test des rangs signés lève pendant l'étalonnage."""
    avant = RS.VERROU_ETALONNAGE["leve"]
    RS.VERROU_ETALONNAGE["leve"] = True
    try:
        yield
    finally:
        RS.VERROU_ETALONNAGE["leve"] = avant


def verifier_sortie(sortie):
    """Garde 22 : la sortie de l'étalonnage n'a que des écarts moyens, des écarts-types et des réglages."""
    lignes = sortie if isinstance(sortie, list) else [sortie]
    for l in lignes:
        hors = sorted(set(l) - CLES_PERMISES)
        if hors:
            raise ArretEtalonnage(f"garde 22 : champ hors de l'étalonnage dans la sortie : {hors} : arrêt")
    return True


def jumelles(graines, couche, base, prop, dose, taux, f, S, bras, repere=REPERE_LECTURE, regle="v2", repli=False,
             lot=LOT_DE_SOURCES):
    """Sommes sur S sources (en lots) : M1 par bras et par jumelle. Rend (moyennes de M1 par bras, écart-type des différences
    entre jumelles par bras). Les graines ne dépendent que de `base` et du numéro de lot : elles sont communes à tous les
    réglages (dichotomie sur graines communes)."""
    sommes = {b: 0.0 for b in bras}
    diff2, diff1 = {b: 0.0 for b in bras}, {b: 0.0 for b in bras}
    fait = 0
    k = 0
    while fait < S:
        n = min(lot, S - fait)
        cles = {}
        for b in bras:
            for j in (0, 1):
                cles[b if j == 0 else f"{b}-j1"] = graines.g(couche=couche, **base, lot=k, bras=b, jumelle=j, role="echantillonnage")
        r = simuler(cles, graines.g(couche=couche, **base, lot=k, role="monde"), graines.g(couche=couche, **base, lot=k,
                    role="source"), prop, dose, taux, f, n, repere, regle, repli)
        for b in bras:
            a, c = r["bras"][b]["M1"].astype(float), r["bras"][f"{b}-j1"]["M1"].astype(float)
            sommes[b] += float((a + c).sum()) / 2.0
            d = a - c
            diff1[b] += float(d.sum())
            diff2[b] += float((d * d).sum())
        fait += n
        k += 1
    moy = {b: sommes[b] / S for b in bras}
    sd = {b: math.sqrt(max(0.0, (diff2[b] - diff1[b] ** 2 / S) / (S - 1))) for b in bras}
    return moy, sd


def ecart_type_reuni(sd_par_bras):
    v = list(sd_par_bras.values())
    return math.sqrt(sum(x * x for x in v) / len(v))


def taille(moy, sd, contraste):
    s = ecart_type_reuni(sd)
    e = (moy["3"] - moy["2"]) if contraste == "heritage" else (moy["2"] - moy["1"])
    return e, (e / s if s > 0 else float("nan")), s


def exiger_ecart_type_et_taille_finis(ecart_type, taille_reduite=None, cas=""):
    """Note D8 (code v4) : arrêt de l'étalonnage si l'écart-type entre jumelles réuni est nul ou non fini, ou si la taille
    réduite est non finie ; jamais « non atteignable », jamais une case rangée en silence."""
    if not (math.isfinite(ecart_type) and ecart_type > 0.0):
        raise ArretEtalonnage(f"note D8 : écart-type entre jumelles nul ou non fini ({ecart_type!r}) {cas}: arrêt de "
                              "l'étalonnage (ce n'est pas « non atteignable »)")
    if taille_reduite is not None and not math.isfinite(taille_reduite):
        raise ArretEtalonnage(f"note D8 : taille réduite non finie ({taille_reduite!r}) {cas}: arrêt de l'étalonnage (ce "
                              "n'est pas « non atteignable »)")
    return True


def _bras(dose, contraste):
    return ("2", "3") if (dose == 0.0 and contraste == "heritage") else ("1", "2", "3")


def etalonner(graines, couche, nom, fabrique, nom_du_reglage, dose, cible, f, S, taux=0.25, base_en_plus=None):
    """Dichotomie sur le réglage `nom_du_reglage` (fabrique(x) → configuration du proposeur) ; graines communes. Rend une ligne
    de sortie (écarts, écarts-types, réglage, atteignable)."""
    contraste = CONTRASTE_DU_REGLAGE[nom_du_reglage]
    bras = _bras(dose, contraste)
    base = dict(famille="etalonnage", proposeur=nom, dose=dose, taux=taux, **(base_en_plus or {}))
    bas, haut = PLAGES[nom_du_reglage]
    with verrou():
        def evaluer(x):
            moy, sd = jumelles(graines, couche, base, fabrique(x), dose, taux, f, S, bras)
            e, t, s = taille(moy, sd, contraste)
            exiger_ecart_type_et_taille_finis(s, t, f"({nom}, dose {dose}, cible {cible}, réglage {x!r}) ")
            return e, t, s, sd, moy

        e, t, s, sd, moy = evaluer(haut)
        ligne = {"proposeur": nom, "dose": dose, "taux": taux, "contraste": contraste, "cible": cible,
                 "nom_du_reglage": nom_du_reglage, "sources": S}
        if not (t >= cible - TOLERANCE_ETALONNAGE):
            ligne.update(reglage=haut, taille_estimee=t, ecart_moyen=e, ecart_type_jumelles=s, ecart_type_jumelles_par_bras=sd,
                         ecarts_moyens_par_bras=moy, atteignable=False, pas=1, statut="non atteignable")
            verifier_sortie(ligne)
            return ligne
        x = haut
        pas = 1
        if abs(t - cible) > TOLERANCE_ETALONNAGE:
            lo, hi = bas, haut
            for pas in range(2, PAS_DICHOTOMIE_MAX + 2):
                x = (lo + hi) / 2.0
                e, t, s, sd, moy = evaluer(x)
                if abs(t - cible) <= TOLERANCE_ETALONNAGE:
                    break
                if t < cible:
                    lo = x
                else:
                    hi = x
        statut = "atteint" if abs(t - cible) <= TOLERANCE_ETALONNAGE else "non convergé"
        ligne.update(reglage=x, taille_estimee=t, ecart_moyen=e, ecart_type_jumelles=s, ecart_type_jumelles_par_bras=sd,
                     ecarts_moyens_par_bras=moy, atteignable=True, pas=pas, statut=statut)
    verifier_sortie(ligne)
    return ligne


def ecart_type_sans_reglage(graines, couche, nom, prop, dose, taux, f, S, bras, repere=REPERE_LECTURE, regle="v2", repli=False,
                            base_en_plus=None):
    """Écart-type entre jumelles d'un proposeur sans réglage (ou à réglage fixé), par bras et réuni."""
    base = dict(famille="etalonnage-jumelles", proposeur=nom, dose=dose, taux=taux, retrait=regle, repere=repere,
                **(base_en_plus or {}))
    with verrou():
        moy, sd = jumelles(graines, couche, base, prop, dose, taux, f, S, bras, repere, regle, repli)
    exiger_ecart_type_et_taille_finis(ecart_type_reuni(sd), None, f"({nom}, dose {dose}, taux {taux}) ")
    ligne = {"proposeur": nom, "dose": dose, "taux": taux, "repere": repere, "retrait": regle, "repli": repli, "sources": S,
             "ecart_type_jumelles": ecart_type_reuni(sd), "ecart_type_jumelles_par_bras": sd, "ecarts_moyens_par_bras": moy}
    verifier_sortie(ligne)
    return ligne


def geler_reglages(chemin, lignes, configuration):
    """Écrit le fichier des réglages et son compagnon `.sha256`, après la garde 22 ; jamais d'écrasement."""
    verifier_sortie(lignes)
    octets = (json.dumps({"reglages": lignes, "configuration": configuration}, ensure_ascii=False, sort_keys=True, indent=1)
              + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    sha = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="ascii") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def taille_realisee(ecart_moyen_decisif, ecart_type_gele):
    """M9 : la taille réalisée d'une case décisive est son écart moyen divisé par l'écart-type entre jumelles gelé."""
    return ecart_moyen_decisif / ecart_type_gele


def taille_tenue(realisee, cible, tolerance=0.05):
    """Liste d'arrêt, point 6 : une case dont la taille réalisée s'écarte de plus de 0,05 de sa cible est « taille non tenue »."""
    return abs(realisee - cible) <= tolerance + 1e-12
