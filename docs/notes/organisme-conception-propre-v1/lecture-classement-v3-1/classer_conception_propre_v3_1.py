#!/usr/bin/env python3
"""Programme de classement de la règle de sélection — course « conception propre » — v3.1.

v3.1 (14 novembre 2026, à partir de 09:20 UTC, `date -u`) = v3 (`../lecture-classement-v3/`, `87643592…`, gardée, R12),
pour l'outil du lecteur v3.1 (contre-lecture `f5cc9cdb…`, R-2678). La règle ne change pas. Changements, et seulement eux
(différentiel entier : `differentiel-classer-v3-v3-1.diff`) :
- il charge `outil_lecteur_conception_propre_v3_1.py` et lit et écrit les noms en `-v3-1` ;
- il refuse une racine autre que celle du dossier d'envois (C6 : dossier fixe sous la racine) ;
- les refus et anomalies neuves de l'outil v3.1 passent par le même chemin (M1 : toute réponse sans clôture chaînée au
  journal est refusée ; écart d'envoi consigné, réponse non analysée, palier servi autre : anomalies bloquantes, E2) ;
  précision complétée en conséquence.

De la v3 : v3 (14 novembre 2026, à partir de 07:55 UTC, `date -u`) = v2 (`../lecture-classement-v2/`, `2cb65f33…`, gardée, R12),
pour l'outil du lecteur v3 (lecteur Astra, lots de 5, R-2662). La règle (§ 4.5 à 4.8, 6, 7) ne change pas. Changements, et
seulement eux (différentiel entier : `differentiel-classer-v2-v3.diff`) :
- il charge `outil_lecteur_conception_propre_v3.py` et lit les noms en `-v3` (`manifeste-envois-v3.json`,
  `reponse-<L>-lot<k>-v3.json`), écrit `lecture-verifiee-<L>-v3.json`, `classement-v3.json`, `classement-v3.md` ;
- la vérification préalable « réponse attendue absente → refus » est retirée d'ici : l'outil v3 la fait lui-même, et
  n'accepte une réponse absente que si son journal de dépense consigne un arrêt (anomalie ou plafond) ; elle devient alors
  l'anomalie bloquante `reponse_absente` (verdict E2, aucune désignation) ; sans arrêt consigné, refus comme en v2 ;
- les anomalies bloquantes de l'outil v3 (dont C1, `cle_de_critere_manquante`, `modele_servi_different`,
  `refus_du_lecteur`) passent au verdict par le même chemin que celles de la v2 ; précisions complétées en conséquence.
Les entrées de la v2 (dossier préparé par l'outil v2, réponses au format Kimi) ne sont plus lues par ce programme : elles
restent celles de `classer_conception_propre_v2.py`.

De la v2 : v2 (14 novembre 2026, à partir de 00:16 UTC, `date -u`) = v1 (`../lecture-classement-v1/`, `f91962f3…`, gardée, R12)
corrigée d'après la contre-lecture `contre-lecture-lecture-classement-v1.md` (`baabfb13…`, R-2627) :
- **M1** : preuve par passages d'au moins 20 caractères hors espaces, catalogue lu dans la seule cellule du mécanisme
  (outil v2) ; passages courts refusés comptés par critère et par lecture, au JSON et au résumé ;
- **M2** : une anomalie bloquante (réponse illisible, fin autre que `stop`, entrée manquante ou en double) rend la
  lecture **incomplète** : verdict « illisible », désignation impossible, anomalies et fiches réelles touchées citées au
  verdict et au résumé. La règle (§ 4 à 7) ne permet aucune relecture (deux lectures, six appels) : il n'y en a pas ;
- **M3** : la provenance des fiches (copie scellée du run, empreinte du manifeste de fin) est revérifiée ici ;
- essais muets de la contre-lecture couverts (κ calculé en fractions exactes : un κ de 0,4 tient) ; détail de L2 avec la
  valeur brute ; précisions A2 et A7 complétées ;
- **variante « désignation détachée de L5 »** (contre-lecture, section A1) **préparée, non active** : `--designation
  detachee-v1 --decision <R-…>` ; par défaut, la règle de la conception (`L5`). Elle ne s'applique que sur un mot de Lazar
  (nœud A1), consigné **avant** le lancement du classement : le programme ne la calcule jamais quand elle n'est pas
  demandée, pour qu'aucun résultat ne la précède.

De la v1 : écrit le 13 novembre 2026 (à partir de 23:45 UTC, `date -u`) par un développeur neuf (tâche N3 de R-2615), avant toute
course et toute lecture. Comportement fixé par `conception-course-v1.md` (be3ba97e…), § 4.5 à 4.8, 6 et 7 ; tout écart
serait un écart déclaré (les précisions prises là où le texte se tait sont listées dans `PRECISIONS` et rendues dans la
sortie). **N'appelle aucun modèle.** Ne lit jamais les notes du juge de l'organisme (§ 4.8).

    python3 -I -B classer_conception_propre_v3_1.py --envois DOSSIER_ENVOIS --sortie DOSSIER_SORTIE

Entrées (v3.1) : le dossier fixe préparé par `outil_lecteur_conception_propre_v3_1.py preparer`, où `envoyer` a scellé les
réponses `reponse-<L>-lot<k>-v3-1.json` et tenu le journal de dépense. Sortie (dossier neuf ou vide, rien n'est écrasé) :
`lecture-verifiee-L1-v3-1.json`, `lecture-verifiee-L2-v3-1.json`, `classement-v3-1.json`, `classement-v3-1.md`, scellés.

Chaîne : vérification mot pour mot des deux lectures (§ 4.5) → valeurs retenues (R = 1 si les deux lectures donnent 1
prouvé ; N = aucune si les deux donnent aucune) → portes R2, R3, R7 → nouveauté → ordre des neuves (S = R1 + R4 + R5 + R6
décroissant, coût `processeur` avant `depense`, départage tiré, enfant 2) → deux désignées, seulement si le classement est
lisible (L1 à L4) et L5 rejetée → témoin à score permuté (enfant 3) → L1 à L5 → huit comparaisons descriptives, Holm.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
from fractions import Fraction
import sys
from pathlib import Path

import numpy as np

VERSION = "classer-conception-propre-v3-1"
ICI = Path(__file__).resolve().parent


def _charger_outil():
    spec = importlib.util.spec_from_file_location("outil_lecteur_cp_v3_1", ICI / "outil_lecteur_conception_propre_v3_1.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


O = _charger_outil()
CRITERES = O.CRITERES
ENTROPIE_TEST = 2026111303            # § 4.3 et § 6 : test L5
PERMUTATIONS = 100_000
SEUIL_P = 0.05
TAILLE_TRANCHE = 10_000
COUT_RANG = {"processeur": 0, "depense": 1}
PORTES = ("R2", "R3", "R7")
L1_MIN_PUBLIEES = 5
L4_KAPPA_MIN, L4_ACCORD_MIN = 0.4, 0.8
E5_PART = Fraction(4, 5)
DESIGNATIONS = ("L5", "detachee-v1")
MOTIF_DECISION = r"(R|N)-\d+"
PRECISIONS = [
    "Passage « mot pour mot » : comparé, espaces normalisés seulement (aucune autre normalisation, typographie comprise), à "
    "chaque chaîne de la fiche servie prise isolément (un passage à cheval sur deux champs, ou qui recopie les clés JSON, "
    "n'est pas prouvé) ; M1 : au moins 20 caractères hors espaces (un signe, une étiquette de levier, un code Ck, une date "
    "ne prouvent rien ; 20 caractères font une proposition courte de quatre ou cinq mots ; la consigne borne en haut à "
    "200) ; R4 hors levier:juge n'est pas concerné (1 par programme) ; un passage de plus de 200 caractères n'est pas "
    "refusé, il est compté ; "
    "un passage recopié avec les échappements JSON de la vue servie (\\\" ou \\\\) est accepté.",
    "Passage du catalogue (M1) : cherché dans la seule cellule « Mécanisme central » de la ligne Ck (ni code, ni nom, ni "
    "source), marques ** retirées des deux côtés, au moins 20 caractères hors espaces ; passage de la fiche exigé aussi.",
    "Valeur rendue autre que l'entier 0 ou 1 (chaîne, booléen) : comptée 0. M2 : entrée manquante, en double, lot illisible "
    "ou fin autre que stop : la fiche est comptée 0 et aucune, mais la lecture est « incomplète » : verdict illisible, "
    "aucune désignation, anomalies citées au verdict et au résumé ; aucune relecture (la règle n'en prévoit pas).",
    "v3 (C1 de la relecture courte) : une entrée à laquelle manque une clé de critère (R1 à R7, N) ou sa valeur est une "
    "anomalie bloquante (cle_de_critere_manquante), R4 compris hors levier:juge (la consigne demande les huit points) ; "
    "modèle servi autre que gpt-6-astra, refus du lecteur, réponse absente après un arrêt consigné au journal de dépense : "
    "anomalies bloquantes, contenu non lu ; réponse absente sans arrêt consigné : refus.",
    "v3.1 (M1) : toute réponse lue doit avoir, au journal de dépense chaîné, sa clôture à son nom, à son empreinte et au "
    "statut 200 (sinon refus ; reçue sans clôture : anomalie bloquante reponse_non_analysee) ; tout écart d'envoi "
    "consigné pour un lot (usage, coût, statut, palier…) et un palier servi autre que celui du manifeste sont des "
    "anomalies bloquantes (E2) ; le contenu d'une réponse à fin autre que stop est lu (m3), sans effet sur le verdict.",
    "Valeurs « lues » de L1, L2, L4 et de l'exactitude du lecteur : valeurs comptées après la preuve (§ 4.5) de chaque "
    "lecture ; L3, le classement, C et L5 : valeurs retenues des deux lectures.",
    "L4 : « κ non défini (une marge constante) » lu comme : dès qu'une des deux lectures est constante sur la pile, "
    "on juge l'accord brut (≥ 0,8) ; sinon κ ≥ 0,4, calculé en fractions exactes. κ est rapporté quand son dénominateur "
    "est non nul. Lecture la plus indulgente des deux, et discontinue : une marge constante et 82 % d'accord tiennent "
    "(κ = 0) ; une marge presque constante au même accord manque ; la lecture littérale (accord brut seulement quand κ "
    "n'a pas de valeur) ferait manquer L4 dans le premier cas.",
    "L5 : valeur p = (1 + #{permutations dont la statistique ≥ l'observée}) / (1 + 100 000) ; statistique comparée en "
    "entiers (somme du groupe réel, à effectifs fixés) ; permutations par argsort de tirages uniformes, tranches de 10 000, "
    "générateur numpy.random.default_rng(SeedSequence(2026111303)).",
    "Huit comparaisons descriptives (R1 à R7 retenus, et N = aucune) : même statistique, bilatérale, 100 000 permutations "
    "chacune, générateur SeedSequence(2026111303).spawn(8)[k] ; Holm (pas à pas descendant) sur les huit.",
    "Départage : rang dans numpy.random.default_rng(enfant 2).permutation(n) des fiches réelles admissibles prises dans "
    "l'ordre du fichier ; le rang suit la fiche, pas son vecteur, dans le témoin à score permuté.",
    "Témoin à score permuté : la fiche i reçoit le vecteur (R1…R7, N, coût) de la fiche perm[i], "
    "perm = default_rng(enfant 3).permutation(n) ; calculé même quand aucune idée n'est désignée.",
    "Audit de propreté (R4 du programme) : déclenché si l'un des quatre signes du § 7 tient ; « lisibilité parfaite » est "
    "codée « lisible et L5 rejetée », donc l'audit se déclenche à chaque désignation.",
    "L2 : jugée sur les valeurs comptées après la preuve (§ 4.5) ; le détail porte aussi la valeur brute rendue : une "
    "fausse fiche acceptée par le lecteur avec une citation non prouvée passe L2, et cela se lit dans le détail.",
]


# --- valeurs retenues et classement ------------------------------------------------------------------------------------

def retenir(v1: dict, v2: dict) -> dict:
    vec = {c: int(v1[c]["compte"] == 1 and v2[c]["compte"] == 1) for c in CRITERES}
    n1, n2 = v1["N"]["compte"], v2["N"]["compte"]
    vec["N"] = "aucune" if (n1 == "aucune" and n2 == "aucune") else "+".join(sorted({n for n in (n1, n2)
                                                                                      if n != "aucune"}))
    return vec


def portes_manquantes(vec: dict) -> list[str]:
    return [c for c in PORTES if vec[c] != 1]


def score_S(vec: dict) -> int:
    return vec["R1"] + vec["R4"] + vec["R5"] + vec["R6"]


def score_C(vec: dict) -> int:
    return (1 + score_S(vec)) if (not portes_manquantes(vec) and vec["N"] == "aucune") else 0


def classer(ids: list, vec_de: dict, cout_de: dict, departage: dict) -> dict:
    """Statut de chaque fiche et ordre des neuves (§ 4.6)."""
    statut, neuves = {}, []
    for i in ids:
        v = vec_de[i]
        manque = portes_manquantes(v)
        if manque:
            statut[i] = {"statut": "ecartee", "motif": "porte(s) " + ", ".join(manque)}
        elif v["N"] != "aucune":
            statut[i] = {"statut": "occupee", "entrees": v["N"]}
        else:
            statut[i] = {"statut": "neuve", "S": score_S(v)}
            neuves.append(i)
    neuves.sort(key=lambda i: (-score_S(vec_de[i]), COUT_RANG[cout_de[i]], departage[i]))
    return {"statut": statut, "ordre_neuves": neuves, "deux_premieres": neuves[:2]}


def rangs_departage(ids: list) -> dict:
    tirage = np.random.default_rng(O.enfants_ordres()[2]).permutation(len(ids))
    return {ids[int(j)]: r for r, j in enumerate(tirage)}


def temoin_permute(ids: list, vec_de: dict, cout_de: dict, departage: dict) -> dict:
    perm = [int(x) for x in np.random.default_rng(O.enfants_ordres()[3]).permutation(len(ids))]
    vec_p = {ids[i]: vec_de[ids[perm[i]]] for i in range(len(ids))}
    cout_p = {ids[i]: cout_de[ids[perm[i]]] for i in range(len(ids))}
    r = classer(ids, vec_p, cout_p, departage)
    return {"permutation": perm, "deux_premieres": r["deux_premieres"], "ordre_neuves": r["ordre_neuves"]}


# --- statistiques --------------------------------------------------------------------------------------------------------

def kappa_accord(a: list, b: list) -> dict:
    """κ de Cohen en fractions exactes (un κ de 2/5 tient à 0,4) ; rendu en flottants."""
    n = len(a)
    if n == 0 or len(b) != n:
        raise O.Refus("κ : listes vides ou de longueurs différentes")
    po = Fraction(sum(int(x == y) for x, y in zip(a, b)), n)
    pa, pb = Fraction(sum(int(x) for x in a), n), Fraction(sum(int(y) for y in b), n)
    pe = pa * pb + (1 - pa) * (1 - pb)
    kappa = None if pe == 1 else (po - pe) / (1 - pe)
    constante = pa in (0, 1) or pb in (0, 1)
    if constante:
        tient, jugee = po >= Fraction(L4_ACCORD_MIN).limit_denominator(1000), "accord brut (une marge constante)"
    else:
        tient, jugee = kappa >= Fraction(L4_KAPPA_MIN).limit_denominator(1000), "kappa"
    return {"kappa": None if kappa is None else float(kappa), "accord_brut": float(po), "marge_constante": constante,
            "jugee_sur": jugee, "tient": bool(tient)}


def test_permutation(x: list, y: list, graine, permutations=PERMUTATIONS, bilateral=False) -> dict:
    """Différence des moyennes x − y, en entiers : d = Σx·m − Σy·n (même signe et même ordre que la différence)."""
    x, y = np.asarray(x, dtype=np.int64), np.asarray(y, dtype=np.int64)
    n, m = len(x), len(y)
    if n == 0 or m == 0:
        return {"p": None, "observee": None, "motif": "groupe vide"}
    z = np.concatenate([x, y])
    total = int(z.sum())

    def d(sx):
        return sx * m - (total - sx) * n

    obs = d(int(x.sum()))
    rng = np.random.default_rng(graine)
    k, fait = 0, 0
    while fait < permutations:
        b = min(TAILLE_TRANCHE, permutations - fait)
        idx = rng.random((b, n + m)).argsort(axis=1)
        sx = z[idx[:, :n]].sum(axis=1)
        dd = sx * m - (total - sx) * n
        k += int((np.abs(dd) >= abs(obs)).sum() if bilateral else (dd >= obs).sum())
        fait += b
    return {"p": (1 + k) / (1 + permutations), "observee": float(x.mean() - y.mean()), "depassements": k,
            "permutations": permutations, "bilateral": bilateral}


def holm(p: list) -> list:
    k = len(p)
    ordre = sorted(range(k), key=lambda i: p[i])
    adj, courant = [None] * k, 0.0
    for r, i in enumerate(ordre):
        courant = max(courant, min(1.0, (k - r) * p[i]))
        adj[i] = courant
    return adj


def designer_detachee(cl: dict, retenu: dict, C_hasard: list, lisible: bool, rejet_L5: bool, decision: str):
    """Variante de la contre-lecture (section A1), **non active par défaut** : sous L1 à L4 (et lecture complète), chacune
    des deux premières neuves est désignée si son C dépasse strictement le plus grand C des huit idées au hasard ; « séparation
    démontrée » si L5 rejette, « non démontrée » sinon ; E3 devient une mention ; E4 redevient atteignable."""
    max_h = max(C_hasard) if C_hasard else 0
    retenues = [i for i in cl["deux_premieres"] if score_C(retenu[i]) > max_h] if lisible else []
    mention = "séparation démontrée (L5 rejetée)" if rejet_L5 else "séparation non démontrée (L5 non rejetée)"
    if not lisible:
        verdict = "variante détachée : classement non lisible ; aucune idée désignée"
    elif not retenues:
        verdict = f"variante détachée : aucune des deux premières neuves ne dépasse le plus grand C des idées au hasard ({max_h}) ; {mention}"
    else:
        verdict = (f"variante détachée : {len(retenues)} idée(s) désignée(s), {mention}"
                   + (" ; E4 : désignation partielle" if len(retenues) < 2 else ""))
    return retenues, {"decision": decision, "max_C_hasard": max_h, "mention": mention, "verdict": verdict,
                      "C_deux_premieres": {i: score_C(retenu[i]) for i in cl["deux_premieres"]}}


# --- programme -------------------------------------------------------------------------------------------------------------

def classement(dossier_envois, racine=O.RACINE_DEFAUT, permutations=PERMUTATIONS, designation="L5",
               decision=None) -> tuple[dict, dict]:
    if designation not in DESIGNATIONS:
        raise O.Refus(f"règle de désignation inconnue : {designation!r}")
    if designation != "L5" and not (isinstance(decision, str) and re.fullmatch(MOTIF_DECISION, decision)):
        raise O.Refus("variante détachée de L5 : nœud de Lazar ; elle exige --decision R-… ou N-… (mot consigné)")
    if O.racine_du_dossier(dossier_envois) != Path(racine).resolve():
        raise O.Refus("racine différente de celle du dossier d'envois (C6)")
    env = O.charger_envois(dossier_envois)
    cat_texte, _ = O.lire_piece(racine, "catalogue")
    man = env["manifeste"]
    prov = O.verifier_fiches_de_run(racine, man["fiches_validees"]["chemin"])  # M3, revérifié ici
    if prov["sha256"] != man["fiches_validees"]["sha256"] or prov["run"] != man["fiches_validees"]["run"]:
        raise O.Refus("fiches validées : empreinte ou run différents de ceux du manifeste des envois")
    lectures = {L: O.verifier_lecture(dossier_envois, L, cat_texte) for L in O.LECTURES}
    pile = env["pile"]["fiches"]
    par_id = {p["id"]: p for p in pile}
    v = {L: lectures[L]["fiches"] for L in O.LECTURES}
    for L in O.LECTURES:
        if set(v[L]) != set(par_id):
            raise O.Refus(f"lecture {L} : fiches lues ≠ pile")
    retenu = {i: retenir(v["L1"][i], v["L2"][i]) for i in par_id}
    reelles = [p["id"] for p in pile if p["origine"] == "reelle"]
    hasard = [p["id"] for p in pile if p["famille"] == "hasard"]
    cout_de = {i: par_id[i]["cout"] for i in par_id}
    departage = rangs_departage(reelles)
    cl = classer(reelles, retenu, cout_de, departage)
    tp = temoin_permute(reelles, retenu, cout_de, departage)

    # L1 à L5
    publiees = [p for p in pile if p["famille"] == "publie"]
    reconnues = {p["id"]: [L for L in O.LECTURES if v[L][p["id"]]["N"]["compte"] == p["entree"]] for p in publiees}
    n_reconnues = sum(1 for x in reconnues.values() if x)
    L1 = {"tient": n_reconnues >= L1_MIN_PUBLIEES, "reconnues": n_reconnues, "sur": len(publiees),
          "par_temoin": reconnues}
    fausses = [p for p in pile if p["famille"] == "faux"]
    L2_detail = {p["id"]: {"cible": p["cible"], **{L: v[L][p["id"]][p["cible"]]["compte"] for L in O.LECTURES},
                           "brut": {L: v[L][p["id"]][p["cible"]]["brut"] for L in O.LECTURES}} for p in fausses}
    L2 = {"tient": bool(fausses) and all(d[L] == 0 for d in L2_detail.values() for L in O.LECTURES),
          "par_temoin": L2_detail}
    vj = [p["id"] for p in pile if p["famille"] in ("vrai", "jumeau")]
    L3_detail = {i: {"portes_manquantes": portes_manquantes(retenu[i]), "N": retenu[i]["N"]} for i in vj}
    L3 = {"tient": len(vj) == 2 and all(not d["portes_manquantes"] and d["N"] == "aucune" for d in L3_detail.values()),
          "par_temoin": L3_detail}
    ids_pile = [p["id"] for p in pile]
    k_R7 = kappa_accord([v["L1"][i]["R7"]["compte"] for i in ids_pile], [v["L2"][i]["R7"]["compte"] for i in ids_pile])
    k_N = kappa_accord([int(v["L1"][i]["N"]["compte"] != "aucune") for i in ids_pile],
                       [int(v["L2"][i]["N"]["compte"] != "aucune") for i in ids_pile])
    L4 = {"tient": k_R7["tient"] and k_N["tient"], "R7": k_R7, "N": k_N}
    C_reel = [score_C(retenu[i]) for i in reelles]
    C_hasard = [score_C(retenu[i]) for i in hasard]
    t5 = test_permutation(C_reel, C_hasard, np.random.SeedSequence(ENTROPIE_TEST), permutations)
    L5 = {"rejet": t5["p"] is not None and t5["p"] <= SEUIL_P, "test": t5, "C_reelles": dict(zip(reelles, C_reel)),
          "C_hasard": dict(zip(hasard, C_hasard)), "moyenne_reelles": float(np.mean(C_reel)) if C_reel else None,
          "moyenne_hasard": float(np.mean(C_hasard)) if C_hasard else None, "prediction": "signe positif"}
    # M2 : lecture incomplète
    bloquantes = {L: lectures[L]["anomalies_bloquantes"] for L in O.LECTURES}
    touchees = sorted(set(lectures["L1"]["ids_touches"]) | set(lectures["L2"]["ids_touches"]))
    complete = not touchees and not any(bloquantes.values())
    lecture_complete = {"complete": complete, "fiches_touchees": len(touchees),
                        "reelles_touchees": sorted(i for i in touchees if par_id[i]["origine"] == "reelle"),
                        "temoins_touches": sorted(i for i in touchees if par_id[i]["origine"] == "temoin"),
                        "anomalies": {L: [{k: a.get(k) for k in ("genre", "lot", "detail")} for a in bloquantes[L]]
                                      for L in O.LECTURES}}
    lisible = complete and L1["tient"] and L2["tient"] and L3["tient"] and L4["tient"]

    # comparaisons descriptives, Holm
    enfants = np.random.SeedSequence(ENTROPIE_TEST).spawn(8)
    desc = []
    for k, c in enumerate(list(CRITERES) + ["N"]):
        f = (lambda i: int(retenu[i]["N"] == "aucune")) if c == "N" else (lambda i, c=c: retenu[i][c])
        t = test_permutation([f(i) for i in reelles], [f(i) for i in hasard], enfants[k], permutations, bilateral=True)
        desc.append({"critere": c if c != "N" else "N = aucune", "p_brute": t["p"], "difference": t["observee"]})
    ps = [d["p_brute"] for d in desc]
    if all(p is not None for p in ps):
        for d, a in zip(desc, holm(ps)):
            d["p_holm"] = a

    # désignation et échecs
    variante = None
    if designation == "L5":
        designees = cl["deux_premieres"] if (lisible and L5["rejet"]) else []
    else:
        designees, variante = designer_detachee(cl, retenu, C_hasard, lisible, L5["rejet"], decision)
    passees = [i for i in reelles if cl["statut"][i]["statut"] in ("neuve", "occupee")]
    occupees = [i for i in passees if cl["statut"][i]["statut"] == "occupee"]
    echecs = {"E1": not reelles, "E2": not lisible, "E2_lecture_incomplete": not complete, "E3": not L5["rejet"],
              "E4": ((lisible and L5["rejet"] and len(cl["ordre_neuves"]) < 2) if designation == "L5"
                     else (lisible and len(designees) < 2)),
              "E5": (Fraction(len(occupees), len(passees)) > E5_PART) if passees else False}
    hasard_passes = [i for i in hasard if not portes_manquantes(retenu[i])]
    audit = {"lisibilite_parfaite": bool(lisible and L5["rejet"]),
             "kappa_1": bool(k_R7["kappa"] == 1 and k_N["kappa"] == 1),
             "toutes_publiees_reconnues": n_reconnues == len(publiees),
             "aucune_idee_au_hasard_passee": not hasard_passes}
    audit["declenche"] = any(audit.values())

    # exactitude du lecteur sur les témoins
    exactitude = {}
    for L in O.LECTURES:
        par_c = {}
        for p in pile:
            if p["origine"] != "temoin" or not p.get("attendu"):
                continue
            for c, att in p["attendu"].items():
                if att is None:
                    continue
                lu = v[L][p["id"]][c]["compte"]
                d = par_c.setdefault(c, {"justes": 0, "sur": 0, "erreurs": []})
                d["sur"] += 1
                if lu == att:
                    d["justes"] += 1
                else:
                    d["erreurs"].append({"temoin": p["id"], "attendu": att, "lu": lu})
        exactitude[L] = par_c

    # comptes par proposeur (information, N-058)
    par_auteur = {}
    for i in reelles:
        a = par_id[i]["auteur"] or "inconnu"
        d = par_auteur.setdefault(a, {"admissibles": 0, "passees": 0, "neuves": 0, "designees": 0, "hors_question": 0})
        d["admissibles"] += 1
        d["passees"] += cl["statut"][i]["statut"] in ("neuve", "occupee")
        d["neuves"] += cl["statut"][i]["statut"] == "neuve"
        d["designees"] += i in designees
    for h in env["pile"]["hors_question"]:
        d = par_auteur.setdefault(h.get("auteur") or "inconnu", {"admissibles": 0, "passees": 0, "neuves": 0,
                                                                 "designees": 0, "hors_question": 0})
        d["hors_question"] += 1

    if not reelles:
        verdict = "E1 : aucune fiche réelle admissible ; rien à classer"
    elif not complete:
        an = "; ".join(f"{L} lot {a['lot']} : {a['genre']}" for L in O.LECTURES for a in bloquantes[L])
        verdict = (f"E2 : lecture illisible ou incomplète ({an}) ; {len(lecture_complete['reelles_touchees'])} fiche(s) "
                   f"réelle(s) et {len(lecture_complete['temoins_touches'])} témoin(s) touchés ; aucune idée désignée ; "
                   "aucune relecture prévue par la règle")
    elif not lisible:
        verdict = "E2 : classement non lisible (" + ", ".join(n for n, x in (("L1", L1), ("L2", L2), ("L3", L3),
                                                                               ("L4", L4)) if not x["tient"]) + \
                  ") ; aucune idée désignée ; lecture rapportée telle quelle"
    elif designation != "L5":
        verdict = variante["verdict"]
    elif not L5["rejet"]:
        verdict = f"E3 : L5 non rejetée (p = {t5['p']:.5f}) ; aucune idée désignée ; résultat négatif rapporté"
    elif len(designees) < 2:
        verdict = f"E4 : {len(designees)} neuve(s) seulement ; désignation partielle ou nulle"
    else:
        verdict = f"lisible, L5 rejetée (p = {t5['p']:.5f}) : deux idées désignées"
    res = {
        "version": VERSION, "outil_version": O.VERSION,
        "programmes_sha256": {"classer": O.sha256_fichier(__file__),
                              "outil": O.sha256_fichier(ICI / "outil_lecteur_conception_propre_v3_1.py")},
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__},
        "fiches_validees": prov,
        "envois": {"manifeste_sha256": O.sha256_fichier(Path(dossier_envois) / O.MANIFESTE),
                   "reponses": {L: lectures[L]["reponses"] for L in O.LECTURES}},
        "graines": {"ordres": O.ENTROPIE_ORDRES, "test": ENTROPIE_TEST, "permutations": permutations},
        "precisions": PRECISIONS,
        "regle_de_designation": designation, "variante_detachee": variante,
        "verdict": verdict, "lisible": lisible, "lecture_complete": lecture_complete, "designees": designees,
        "temoin_score_permute": {**tp, "communes_avec_designees": len(set(tp["deux_premieres"]) & set(designees)),
                                 "communes_avec_deux_premieres": len(set(tp["deux_premieres"]) &
                                                                     set(cl["deux_premieres"]))},
        "classement": {"ordre_neuves": cl["ordre_neuves"], "deux_premieres": cl["deux_premieres"],
                       "statut": cl["statut"], "departage": departage,
                       "hors_question": env["pile"]["hors_question"]},
        "L1": L1, "L2": L2, "L3": L3, "L4": L4, "L5": L5, "descriptif_holm": desc,
        "echecs": echecs, "audit_proprete": audit, "exactitude_lecteur": exactitude,
        "non_prouves": {L: lectures[L]["non_prouves"] for L in O.LECTURES},
        "passages_courts_refuses": {L: lectures[L]["passages_courts_refuses"] for L in O.LECTURES},
        "passages_au_dela_de_200": {L: lectures[L]["passages_au_dela_de_200"] for L in O.LECTURES},
        "anomalies": {L: lectures[L]["anomalies"] for L in O.LECTURES},
        "retenu": retenu, "comptes_par_proposeur": par_auteur,
        "juge_de_l_organisme": "non ouvert (§ 4.8 : après le scellement de ce classement, à titre d'information)",
    }
    return res, lectures


def resume_md(r: dict) -> str:
    l = [f"# Classement de la règle de sélection — course « conception propre » — v3.1\n",
         f"Programme `{r['version']}` (`{r['programmes_sha256']['classer'][:12]}…`), outil "
         f"`{r['programmes_sha256']['outil'][:12]}…` ; envois `{r['envois']['manifeste_sha256'][:12]}…`.\n",
         f"**Verdict** : {r['verdict']}.\n",
         f"- Règle de désignation : {r['regle_de_designation']}"
         + (f" (décision {r['variante_detachee']['decision']})" if r['variante_detachee'] else " (conception, § 4.6 et 6)") + ".",
         f"- Lecture complète : {r['lecture_complete']['complete']} ; anomalies bloquantes : "
         + ("; ".join(f"{L} lot {a['lot']} {a['genre']}" for L in ('L1', 'L2') for a in r['lecture_complete']['anomalies'][L])
            or "aucune")
         + f" ; fiches réelles touchées : {len(r['lecture_complete']['reelles_touchees'])}, témoins touchés : "
         f"{len(r['lecture_complete']['temoins_touches'])}.",
         "- Passages courts refusés (moins de 20 caractères hors espaces), par lecture : "
         + " ; ".join(f"{L} : {sum(r['passages_courts_refuses'][L].values())}" for L in ('L1', 'L2'))
         + " ; passages au-delà de 200 caractères : "
         + " ; ".join(f"{L} : {r['passages_au_dela_de_200'][L]}" for L in ('L1', 'L2')) + ".",
         f"- Désignées : {', '.join(r['designees']) or 'aucune'} ; deux premières neuves : "
         f"{', '.join(r['classement']['deux_premieres']) or 'aucune'}.",
         f"- Témoin à score permuté : {', '.join(r['temoin_score_permute']['deux_premieres']) or 'aucune'} "
         f"(communes avec les désignées : {r['temoin_score_permute']['communes_avec_designees']}).",
         f"- L1 {'tient' if r['L1']['tient'] else 'manque'} ({r['L1']['reconnues']}/{r['L1']['sur']}) ; "
         f"L2 {'tient' if r['L2']['tient'] else 'manque'} ; L3 {'tient' if r['L3']['tient'] else 'manque'} ; "
         f"L4 {'tient' if r['L4']['tient'] else 'manque'} (R7 : {r['L4']['R7']['jugee_sur']}, κ = "
         f"{r['L4']['R7']['kappa']}, accord {r['L4']['R7']['accord_brut']:.3f} ; N : {r['L4']['N']['jugee_sur']}, κ = "
         f"{r['L4']['N']['kappa']}, accord {r['L4']['N']['accord_brut']:.3f}).",
         f"- L5 : p = {r['L5']['test']['p']}, moyennes C réelles {r['L5']['moyenne_reelles']} contre hasard "
         f"{r['L5']['moyenne_hasard']} ; rejet : {r['L5']['rejet']}.",
         f"- Échecs : {', '.join(k for k, x in r['echecs'].items() if x) or 'aucun'} ; audit de propreté déclenché : "
         f"{r['audit_proprete']['declenche']}.",
         "\n| Comparaison descriptive | différence | p brute | p Holm |\n|---|---|---|---|"]
    for d in r["descriptif_holm"]:
        l.append(f"| {d['critere']} | {d['difference']} | {d['p_brute']} | {d.get('p_holm')} |")
    l.append("\nNotes du juge de l'organisme : non ouvertes (§ 4.8).\n")
    return "\n".join(l) + "\n"


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--envois", required=True)
    a.add_argument("--sortie", required=True)
    a.add_argument("--racine", default=str(O.RACINE_DEFAUT))
    a.add_argument("--designation", choices=DESIGNATIONS, default="L5",
                   help="L5 (règle de la conception, défaut) ; detachee-v1 seulement sur un mot de Lazar (nœud A1)")
    a.add_argument("--decision", default=None, help="référence du mot de Lazar (R-… ou N-…), exigée par detachee-v1")
    args = a.parse_args(argv)
    sortie = Path(args.sortie)
    try:
        if sortie.exists() and any(sortie.iterdir()):
            raise O.Refus(f"{sortie} existe et n'est pas vide : on n'écrase jamais (R12)")
        r, lectures = classement(args.envois, args.racine, designation=args.designation, decision=args.decision)
        sortie.mkdir(parents=True, exist_ok=True)
        for L in O.LECTURES:
            O.ecrire_scelle(sortie / f"lecture-verifiee-{L}-{O.SUFFIXE}.json", O.json_texte(lectures[L]))
        h = O.ecrire_scelle(sortie / f"classement-{O.SUFFIXE}.json", O.json_texte(r))
        O.ecrire_scelle(sortie / f"classement-{O.SUFFIXE}.md", resume_md(r))
        print(json.dumps({"verdict": r["verdict"], "designees": r["designees"], "classement_sha256": h},
                         ensure_ascii=False))
    except O.Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
