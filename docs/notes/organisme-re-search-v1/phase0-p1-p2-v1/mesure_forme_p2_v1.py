"""Mesure de la répétition des formes de lois et référence tirée au hasard dans la grammaire — P2, phase 0, v1 (modèle I).
Fichier neuf (R12).

Mesure (figée) : la règle M2 de l'analyse de nos journaux (`analyse_journaux_re_search_v1.py`, `mesures_s1`) — une carte
« répète une forme déjà proposée » si sa forme figure parmi les cartes d'une génération antérieure, ou plus haut dans la
liste du même proposeur à la même génération (ordre des identifiants) ; les cartes de l'autre proposeur à la même
génération sont simultanées, pas antérieures. Part = cartes qui répètent / cartes. Forme principale : toutes les feuilles
numériques masquées (`cle_forme`) ; sensibilité A-3 : entiers gardés (`cle_forme_entiers`).

Écart A-1 (contre-lecture) : la part est rapportée avec et sans les cartes softmax (hors softmax = cartes non softmax qui
répètent une forme / cartes non softmax ; une carte non softmax ne peut répéter qu'une forme non softmax).

Référence : les mêmes emplacements (génération, proposeur, identifiant) que les cartes observées, chaque loi remplacée par
une loi tirée dans la grammaire fermée (`mondes_reponses_p1p2_v1.tirer_loi`), même règle de répétition ; loi de tirage R1
(principale), R2 (types de racine aux fréquences observées) ; référence hors softmax (emplacements non softmax, racine
uniforme sur les cinq autres types). Variante séquentielle (suite de n tirages sans structure) rapportée.

M4 (suites des attaques de Goodhart, description seulement) : règle de `m4_cellule` de l'analyse ; référence : mêmes
longueurs de suites, lois tirées selon R1.
"""
from __future__ import annotations

import numpy as np

from mondes_reponses_p1p2_v1 import TYPES, Refus, cle_forme, cle_forme_entiers, tirer_loi

VERSION = "mesure-forme-p2-v1"
SEUIL_QUART = 0.25


def trier_cartes(cartes):
    return sorted(cartes, key=lambda c: (c["generation"], c["proposeur"], c["identifiant"]))


def repetitions_m2(cartes, cle=cle_forme):
    """Liste de booléens (dans l'ordre trié) : la carte répète-t-elle une forme déjà proposée (règle M2) ?"""
    cartes = trier_cartes(cartes)
    formes = [cle(c["loi"]) for c in cartes]
    sortie = []
    for i, c in enumerate(cartes):
        anterieures = {formes[j] for j, x in enumerate(cartes)
                       if x["generation"] < c["generation"]
                       or (x["generation"] == c["generation"] and x["proposeur"] == c["proposeur"]
                           and x["identifiant"] < c["identifiant"])}
        sortie.append(formes[i] in anterieures)
    return sortie


def part_m2(cartes, cle=cle_forme):
    rep = repetitions_m2(cartes, cle)
    return sum(rep) / len(rep)


def part_hors_softmax(cartes, cle=cle_forme):
    cartes = trier_cartes(cartes)
    rep = repetitions_m2(cartes, cle)
    hs = [r for r, c in zip(rep, cartes) if c["loi"]["type"] != "softmax"]
    return (sum(hs) / len(hs)) if hs else float("nan"), sum(hs), len(hs)


def mesure_observee(cartes):
    cartes = trier_cartes(cartes)
    rep = repetitions_m2(cartes)
    hs, k_hs, n_hs = part_hors_softmax(cartes)
    hs_e, k_hs_e, _ = part_hors_softmax(cartes, cle_forme_entiers)
    types = [c["loi"]["type"] for c in cartes]
    return {"cartes": len(cartes), "repetent": int(sum(rep)), "part": sum(rep) / len(rep),
            "part_entiers_gardes": part_m2(cartes, cle_forme_entiers),
            "hors_softmax": {"cartes": n_hs, "repetent": int(k_hs), "part": hs,
                             "part_entiers_gardes": hs_e, "repetent_entiers_gardes": int(k_hs_e)},
            "repetitions_par_type": {t: int(sum(r for r, x in zip(rep, types) if x == t)) for t in sorted(set(types))},
            "cartes_par_type": {t: types.count(t) for t in sorted(set(types))},
            "formes_distinctes": len({cle_forme(c["loi"]) for c in cartes}),
            "detail": [{"carte": c["identifiant"], "type": c["loi"]["type"], "repete_une_forme": bool(r)}
                       for c, r in zip(cartes, rep)]}


def _cartes_tirees(emplacements, rng, types_racine=None, poids_racine=None):
    return [{"generation": e["generation"], "proposeur": e["proposeur"], "identifiant": e["identifiant"],
             "loi": tirer_loi(rng, 0, types_racine, poids_racine)} for e in emplacements]


def reference_m2(cartes, rng, tirages, loi_tirage="R1"):
    """Parts de la référence (tableau de `tirages` valeurs, forme principale et entiers gardés) aux emplacements des
    cartes. R1 : types uniformes ; R2 : types de racine aux fréquences observées dans les cartes ; HS : emplacements non
    softmax seulement, racine uniforme sur les cinq autres types ; SEQ : suite de n tirages R1, part = 1 − formes
    distinctes / n."""
    cartes = trier_cartes(cartes)
    if loi_tirage == "R1":
        emplacements, tr, pr = cartes, None, None
    elif loi_tirage == "R2":
        types = [c["loi"]["type"] for c in cartes]
        inconnus = sorted(set(types) - set(TYPES))
        if inconnus:
            raise Refus(f"types de carte hors grammaire : {inconnus}")
        tr = sorted(set(types))
        pr = [types.count(t) / len(types) for t in tr]
        emplacements = cartes
    elif loi_tirage == "HS":
        emplacements = [c for c in cartes if c["loi"]["type"] != "softmax"]
        tr, pr = [t for t in TYPES if t != "softmax"], None
    elif loi_tirage == "SEQ":
        n = len(cartes)
        parts, parts_e = np.empty(tirages), np.empty(tirages)
        for b in range(tirages):
            lois = [tirer_loi(rng) for _ in range(n)]
            parts[b] = 1 - len({cle_forme(x) for x in lois}) / n
            parts_e[b] = 1 - len({cle_forme_entiers(x) for x in lois}) / n
        return parts, parts_e
    else:
        raise Refus(f"loi de tirage inconnue : {loi_tirage!r}")
    parts, parts_e = np.empty(tirages), np.empty(tirages)
    for b in range(tirages):
        tirees = _cartes_tirees(emplacements, rng, tr, pr)
        parts[b] = part_m2(tirees)
        parts_e[b] = part_m2(tirees, cle_forme_entiers)
    return parts, parts_e


def resume_reference(parts, observee):
    q = np.quantile(parts, [0.025, 0.5, 0.975], method="inverted_cdf")
    return {"mediane": float(q[1]), "quantiles_2_5_et_97_5": [float(q[0]), float(q[2])], "moyenne": float(np.mean(parts)),
            "part_des_tirages_au_moins_egale_a_l_observee": float(np.mean(parts >= observee - 1e-12)),
            "observee": float(observee)}


# --- quota (option iii, rejeu hors ligne, conditions de la mère R-3186, P2 a) -----------------------------------------
# Fixé à l'écriture du préenregistrement, sans lire l'oracle ni aucun verdict, ni les 23 cartes : q = 2 laisse à chaque
# proposeur, à chaque génération, une carte et un raffinement d'une même forme ; plage de sensibilité gelée {1, 2, 3}.
QUOTA_PRINCIPAL = 2
QUOTA_PLAGE_SENSIBILITE = (1, 2, 3)
CHAMPS_LUS_PAR_LE_QUOTA = ("generation", "proposeur", "identifiant", "loi")


def projeter_pour_le_quota(cartes):
    """Ne garde de chaque carte que les champs que le quota a le droit de lire : ni `promue`, ni `retenue`, ni `verdict`,
    ni `gardien`, ni aucun champ d'oracle n'atteint le rejeu."""
    sortie = []
    for c in cartes:
        manquants = [k for k in CHAMPS_LUS_PAR_LE_QUOTA if k not in c]
        if manquants:
            raise Refus(f"carte sans champ {manquants} : rejeu du quota refusé")
        sortie.append({k: c[k] for k in CHAMPS_LUS_PAR_LE_QUOTA})
    return sortie


def rejeu_quota(cartes, q, cle=cle_forme):
    """Cartes qu'un quota de q cartes d'une même forme par proposeur et par génération refuserait (au-delà de la q-ième,
    dans l'ordre des identifiants). Seuls les champs de `CHAMPS_LUS_PAR_LE_QUOTA` sont lus (projection d'abord) ; q doit
    appartenir à la plage gelée. Aucune vérité : combien de cartes seraient refusées, rien de plus."""
    if not (isinstance(q, int) and not isinstance(q, bool) and q in QUOTA_PLAGE_SENSIBILITE):
        raise Refus(f"quota hors de la plage gelée {QUOTA_PLAGE_SENSIBILITE} : {q!r}")
    vues = trier_cartes(projeter_pour_le_quota(cartes))
    comptes, refusees = {}, []
    for c in vues:
        k = (c["generation"], c["proposeur"], cle(c["loi"]))
        comptes[k] = comptes.get(k, 0) + 1
        if comptes[k] > q:
            refusees.append(c["identifiant"])
    hs = {c["identifiant"] for c in vues if c["loi"]["type"] != "softmax"}
    return {"quota": q, "principal": q == QUOTA_PRINCIPAL, "cartes": len(vues), "refusees": len(refusees),
            "identifiants": refusees, "refusees_hors_softmax": sum(1 for i in refusees if i in hs),
            "cartes_hors_softmax": len(hs)}


# --- aucune nouveauté (conditions de la mère R-3186, P2 d) --------------------------------------------------------------
MENTION_AUCUNE_NOUVEAUTE = ("Aucune nouveauté n'est attribuée à une forme du seul fait qu'elle est absente de l'archive ou "
                            "des cartes antérieures : « ne répète pas » veut dire seulement « forme non vue plus tôt au "
                            "sens de la règle M2 », jamais « nouvelle », « originale » ni « découverte ».")


# --- M4 (suites des attaques, description seulement) --------------------------------------------------------------------
def part_m4(suites, cle=cle_forme):
    props = rep = 0
    for s in suites:
        vues = set()
        for t in s["tentatives"]:
            if t.get("loi") is None:
                continue
            f = cle(t["loi"])
            props += 1
            rep += int(f in vues)
            vues.add(f)
    return (rep / props if props else float("nan")), rep, props


def reference_m4(suites, rng, tirages):
    longueurs = [sum(1 for t in s["tentatives"] if t.get("loi") is not None) for s in suites]
    parts = np.empty(tirages)
    total = sum(longueurs)
    for b in range(tirages):
        rep = 0
        for n in longueurs:
            vues = set()
            for _ in range(n):
                f = cle_forme(tirer_loi(rng))
                rep += int(f in vues)
                vues.add(f)
        parts[b] = rep / total if total else float("nan")
    return parts
