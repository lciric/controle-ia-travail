#!/usr/bin/env python3
"""Programme de classement de la relecture exploratoire — course « conception propre » — v3.2 (règle v2).

v3.2 (14 novembre 2026, à partir de 12:25 UTC, `date -u`) = v3.1 (`../../lecture-classement-v3-1/`, `f9ef3695…`, gardée,
R12), pour la **relecture exploratoire** sous la règle corrigée `../regle-v2.md` (R-2726). **Rien n'est désigné** : la
relecture rend un rang exploratoire, jamais une désignation au sens de la conception (§ 4.6) ; le verdict E2 scellé de la
première lecture reste tel quel. Changements, et seulement eux (différentiel entier : `differentiel-classer-v3-1-v3-2.diff`) :

- il charge `outil_lecteur_conception_propre_v3_2.py` et lit et écrit les noms en `-v3-2` ;
- **portes** : R2 et R3 seulement (R7 sort des portes, règle v2, § 2) ; **S v2 = R1 + R4 + R5 + R6 + R7** ; C v2 = 1[portes
  et N = aucune] × (1 + S v2), de 0 à 6 ;
- **L3 v2** : le vrai et le jumeau passent R2 et R3 (retenues), restent neufs, et reçoivent chacun R7 = 1 prouvé dans au
  moins une des deux lectures ;
- **L5 v2** sur C v2 (même test, même graine) ; **séparation** (séquence fixe) : si L5 v2 rejette, test de R7 seul
  (`SeedSequence(2026111404)`) → « séparation réelle » ou « séparation de forme » ; sinon « pas de séparation » (le second
  test est calculé et rapporté, jamais lu) ;
- **aucune désignation** : la variante « détachée » de la v3.1 est retirée (sans objet) ; rang exploratoire des neuves, rang
  restreint aux fiches de R7 retenu = 1, témoin à score permuté : information ;
- descriptifs déclarés d'avance (règle v2, § 7) : R7 du hasard selon que sa chaîne implique ou non le signe prédit (champ
  `chaine` de la pièce épinglée des idées au hasard) ; **relecture contre première lecture** (accord des valeurs retenues,
  critère par critère, avec `classement-v3-1.json` épinglé) ; **règle v2 appliquée aux valeurs retenues de la première
  lecture** (statut, rang, recouvrement des deux et des cinq premières) ;
- issues renommées (E2 v2, E3 v2, E4 v2, E5) ; signes d'audit de propreté inchangés (R4 du programme).

De la v3.1 (inchangé) : vérification mot pour mot des deux lectures par l'outil (anomalies bloquantes → lecture incomplète,
E2), valeurs retenues (R = 1 si les deux lectures donnent 1 prouvé ; N = aucune si les deux donnent aucune), nouveauté,
ordre (S décroissant, coût `processeur` avant `depense`, départage enfant 2), témoin à score permuté (enfant 3), L1, L2, L4,
test par permutation (100 000, tranches de 10 000, entiers), huit comparaisons descriptives et Holm, κ en fractions exactes,
exactitude du lecteur sur les témoins (valeurs « non fixées » exclues), comptes par proposeur (N-058), refus d'une racine
autre que celle du dossier d'envois, provenance des fiches revérifiée. **N'appelle aucun modèle.** Ne lit jamais les notes
du juge de l'organisme (conception, § 4.8).

    python3 -I -B classer_conception_propre_v3_2.py --envois DOSSIER_ENVOIS --sortie DOSSIER_SORTIE

Sortie (dossier neuf ou vide, rien n'est écrasé) : `lecture-verifiee-L1-v3-2.json`, `lecture-verifiee-L2-v3-2.json`,
`classement-v3-2.json`, `classement-v3-2.md`, scellés.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
import sys
from pathlib import Path

import numpy as np

VERSION = "classer-conception-propre-v3-2"
ICI = Path(__file__).resolve().parent
NOM_OUTIL = "outil_lecteur_conception_propre_v3_2.py"


def _charger_outil():
    spec = importlib.util.spec_from_file_location("outil_lecteur_cp_v3_2", ICI / NOM_OUTIL)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


O = _charger_outil()
CRITERES = O.CRITERES
ENTROPIE_TEST = 2026111303            # § 4.3 et § 6 de la conception : test L5 (inchangé)
ENTROPIE_SEPARATION = 2026111404      # règle v2, § 6.7 : R7 seul, après L5 v2
PERMUTATIONS = 100_000
SEUIL_P = 0.05
TAILLE_TRANCHE = 10_000
COUT_RANG = {"processeur": 0, "depense": 1}
PORTES = ("R2", "R3")                  # règle v2 : R7 n'est plus une porte
L1_MIN_PUBLIEES = 5
L4_KAPPA_MIN, L4_ACCORD_MIN = 0.4, 0.8
E5_PART = Fraction(4, 5)
PREMIERE_CLASSEMENT = (f"{O.DOSSIER}/lecture-g1-v3-1/classement/classement-v3-1.json",
                       "6ee04e1b41639ce12b64bf27f4514f3427c173c6ef3ceb5bcf3ace65c1b19b62")
PRECISIONS = [
    "Passage « mot pour mot » (inchangé depuis la v2) : comparé, espaces normalisés seulement, à chaque chaîne de la fiche "
    "servie prise isolément ; au moins 20 caractères hors espaces ; un passage de plus de 200 caractères n'est pas refusé, "
    "il est compté ; un passage recopié avec les échappements JSON de la vue servie est accepté ; catalogue : cellule « "
    "Mécanisme central » seule, marques ** retirées.",
    "Valeur rendue autre que l'entier 0 ou 1 : comptée 0. Anomalie bloquante de l'outil (réponse illisible, fin autre que "
    "stop, entrée manquante ou en double, clé de critère manquante, modèle servi autre, refus du lecteur, réponse absente "
    "après un arrêt, écart d'envoi, réponse non analysée, palier servi autre) : lecture « incomplète », E2 v2 ; aucune "
    "relecture.",
    "Règle v2 : portes R2 et R3 ; S v2 = R1 + R4 + R5 + R6 + R7 ; C v2 = 1[portes et N = aucune] × (1 + S v2), de 0 à 6.",
    "L3 v2 : « R7 = 1 prouvé dans au moins une lecture » lu sur les valeurs comptées après la preuve (§ 4.5) de chaque "
    "lecture ; portes et N sur les valeurs retenues des deux lectures.",
    "Valeurs « lues » de L1, L2, L4 et de l'exactitude du lecteur : valeurs comptées après la preuve de chaque lecture ; L3 "
    "(portes et N), le rang, C et L5 : valeurs retenues des deux lectures. Exactitude : les valeurs attendues « non "
    "fixées » (null) sont exclues.",
    "L4 (inchangé) : dès qu'une des deux lectures est constante sur la pile, on juge l'accord brut (≥ 0,8) ; sinon κ ≥ 0,4, "
    "calculé en fractions exactes.",
    "L5 v2 : valeur p = (1 + #{permutations dont la statistique ≥ l'observée}) / (1 + 100 000) ; statistique comparée en "
    "entiers ; permutations par argsort de tirages uniformes, tranches de 10 000, générateur "
    "numpy.random.default_rng(SeedSequence(2026111303)).",
    "Séparation (séquence fixe) : test de R7 retenu seul, réelles contre hasard, même méthode, générateur "
    "default_rng(SeedSequence(2026111404)) ; toujours calculé ; lu seulement si L5 v2 rejette.",
    "Huit comparaisons descriptives (R1 à R7 retenus, et N = aucune) : bilatérales, 100 000 permutations chacune, "
    "SeedSequence(2026111303).spawn(8)[k] ; Holm sur les huit.",
    "Départage : rang dans default_rng(enfant 2).permutation(n) des fiches réelles admissibles prises dans l'ordre du "
    "fichier ; témoin à score permuté : la fiche i reçoit le vecteur (R1…R7, N, coût) de la fiche perm[i], "
    "perm = default_rng(enfant 3).permutation(n).",
    "Relecture contre première lecture : fiches réelles communes aux deux piles (même identifiant), valeurs retenues ; "
    "κ ou accord brut par la même fonction que L4 ; N lu « occupée ou non ». Règle v2 appliquée aux valeurs retenues de la "
    "première lecture : mêmes fonctions de classement, même départage. Aucun de ces descriptifs ne change le rang ni le "
    "verdict.",
    "Audit de propreté (R4 du programme) : déclenché si lisible et L5 v2 rejetée, si κ = 1 sur R7 et sur N, si toutes les "
    "publiées sont reconnues, ou si aucune idée au hasard ne passe les portes.",
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
    return vec["R1"] + vec["R4"] + vec["R5"] + vec["R6"] + vec["R7"]


def score_C(vec: dict) -> int:
    return (1 + score_S(vec)) if (not portes_manquantes(vec) and vec["N"] == "aucune") else 0


def classer(ids: list, vec_de: dict, cout_de: dict, departage: dict) -> dict:
    """Statut de chaque fiche et rang exploratoire des neuves (règle v2, § 6)."""
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


def separation(rejet_L5: bool, R7_reel: list, R7_hasard: list, permutations=PERMUTATIONS) -> dict:
    """Règle v2, § 6.7 : séquence fixe. Le test de R7 seul est toujours calculé, et lu seulement si L5 v2 rejette."""
    t = test_permutation(R7_reel, R7_hasard, np.random.SeedSequence(ENTROPIE_SEPARATION), permutations)
    if not rejet_L5:
        issue = "pas de séparation"
    elif t["p"] is not None and t["p"] <= SEUIL_P:
        issue = "séparation réelle"
    else:
        issue = "séparation de forme"
    return {"issue": issue, "test_R7_seul": t, "lu": bool(rejet_L5)}


# --- descriptifs déclarés d'avance ---------------------------------------------------------------------------------------

def chaines_du_hasard(racine) -> dict:
    """Sens de la chaîne causale de chaque idée au hasard (pièce épinglée de l'outil ; jamais servi au lecteur)."""
    texte, _ = O.lire_piece(racine, "temoins_hasard")
    return {t["code"]: bool(t["chaine"]["coherente_avec_le_signe"]) for t in json.loads(texte)["temoins"]}


def retenu_premiere_lecture(racine) -> dict:
    rel, attendue = PREMIERE_CLASSEMENT
    p = Path(racine) / rel
    if not p.is_file():
        raise O.Refus(f"classement de la première lecture absent : {rel}")
    h = O.sha256_fichier(p)
    if h != attendue:
        raise O.Refus(f"classement de la première lecture : empreinte {h[:12]}… ≠ épinglée {attendue[:12]}…")
    return json.loads(p.read_text(encoding="utf-8"))["retenu"]


def relecture_contre_premiere(reelles: list, retenu: dict, retenu_1: dict) -> dict:
    communes = [i for i in reelles if i in retenu_1]
    if not communes:
        return {"fiches_communes": 0}
    par = {}
    for c in list(CRITERES) + ["N"]:
        f = (lambda v: int(v["N"] != "aucune")) if c == "N" else (lambda v, c=c: int(v[c]))
        a, b = [f(retenu_1[i]) for i in communes], [f(retenu[i]) for i in communes]
        par[c if c != "N" else "N_occupee"] = {**kappa_accord(a, b), "premiere_1": sum(a), "relecture_1": sum(b)}
    return {"fiches_communes": len(communes), "par_critere": par}


def regle_v2_sur_premiere(reelles: list, retenu_1: dict, cout_de: dict, departage: dict, ordre_v2: list) -> dict:
    communes = [i for i in reelles if i in retenu_1]
    if not communes:
        return {"fiches_communes": 0}
    cl = classer(communes, retenu_1, cout_de, departage)
    return {"fiches_communes": len(communes), "ordre_neuves": cl["ordre_neuves"],
            "statut": {i: cl["statut"][i]["statut"] for i in communes},
            "deux_premieres_communes_avec_la_relecture": len(set(cl["ordre_neuves"][:2]) & set(ordre_v2[:2])),
            "cinq_premieres_communes_avec_la_relecture": len(set(cl["ordre_neuves"][:5]) & set(ordre_v2[:5]))}


# --- programme -------------------------------------------------------------------------------------------------------------

def classement(dossier_envois, racine=O.RACINE_DEFAUT, permutations=PERMUTATIONS) -> tuple[dict, dict]:
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
    rang_R7 = [i for i in cl["ordre_neuves"] if retenu[i]["R7"] == 1]

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
    L3_detail = {i: {"portes_manquantes": portes_manquantes(retenu[i]), "N": retenu[i]["N"],
                     "R7_prouve_par": [L for L in O.LECTURES if v[L][i]["R7"]["compte"] == 1]} for i in vj}
    L3 = {"tient": len(vj) == 2 and all(not d["portes_manquantes"] and d["N"] == "aucune" and d["R7_prouve_par"]
                                        for d in L3_detail.values()),
          "par_temoin": L3_detail, "regle": "v2 : portes R2, R3 retenues ; N retenue aucune ; R7 = 1 prouvé dans au moins "
                                            "une lecture"}
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
          "moyenne_hasard": float(np.mean(C_hasard)) if C_hasard else None, "prediction": "signe positif",
          "statut": "exploratoire (règle v2)"}
    sep = separation(L5["rejet"], [retenu[i]["R7"] for i in reelles], [retenu[i]["R7"] for i in hasard], permutations)
    # lecture incomplète
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

    # descriptifs déclarés d'avance
    coherence = chaines_du_hasard(racine)
    hasard_R7 = {"chaine_coherente": {i: retenu[i]["R7"] for i in hasard if coherence.get(i) is True},
                 "chaine_contraire": {i: retenu[i]["R7"] for i in hasard if coherence.get(i) is False}}
    retenu_1 = retenu_premiere_lecture(racine)
    contre_premiere = relecture_contre_premiere(reelles, retenu, retenu_1)
    regle_v2_premiere = regle_v2_sur_premiere(reelles, retenu_1, cout_de, departage, cl["ordre_neuves"])

    # issues (aucune désignation)
    passees = [i for i in reelles if cl["statut"][i]["statut"] in ("neuve", "occupee")]
    occupees = [i for i in passees if cl["statut"][i]["statut"] == "occupee"]
    echecs = {"E1": not reelles, "E2_v2": not lisible, "E2_v2_lecture_incomplete": not complete,
              "E3_v2": not L5["rejet"], "E4_v2": len(cl["ordre_neuves"]) < 2,
              "E5": (Fraction(len(occupees), len(passees)) > E5_PART) if passees else False}
    hasard_passes = [i for i in hasard if not portes_manquantes(retenu[i])]
    audit = {"lisibilite_parfaite": bool(lisible and L5["rejet"]),
             "kappa_1": bool(k_R7["kappa"] == 1 and k_N["kappa"] == 1),
             "toutes_publiees_reconnues": n_reconnues == len(publiees),
             "aucune_idee_au_hasard_passee": not hasard_passes}
    audit["declenche"] = any(audit.values())

    # exactitude du lecteur sur les témoins (valeurs non fixées exclues)
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
        d = par_auteur.setdefault(a, {"admissibles": 0, "passees": 0, "neuves": 0, "hors_question": 0})
        d["admissibles"] += 1
        d["passees"] += cl["statut"][i]["statut"] in ("neuve", "occupee")
        d["neuves"] += cl["statut"][i]["statut"] == "neuve"
    for h in env["pile"]["hors_question"]:
        d = par_auteur.setdefault(h.get("auteur") or "inconnu", {"admissibles": 0, "passees": 0, "neuves": 0,
                                                                 "hors_question": 0})
        d["hors_question"] += 1

    if not reelles:
        verdict = "E1 : aucune fiche réelle admissible ; rien à classer"
    elif not complete:
        an = "; ".join(f"{L} lot {a['lot']} : {a['genre']}" for L in O.LECTURES for a in bloquantes[L])
        verdict = (f"E2 v2 : lecture illisible ou incomplète ({an}) ; {len(lecture_complete['reelles_touchees'])} fiche(s) "
                   f"réelle(s) et {len(lecture_complete['temoins_touches'])} témoin(s) touchés ; rang exploratoire non "
                   "lisible ; aucune relecture prévue")
    elif not lisible:
        verdict = ("E2 v2 : classement exploratoire non lisible (" + ", ".join(
            n for n, x in (("L1", L1), ("L2", L2), ("L3 v2", L3), ("L4", L4)) if not x["tient"])
                   + f") ; {sep['issue']} (L5 v2 : p = {t5['p']:.5f}) ; rang rapporté avec cette mention")
    else:
        verdict = (f"classement exploratoire lisible ; {sep['issue']} (L5 v2 : p = {t5['p']:.5f})"
                   + (f" ; R7 seul : p = {sep['test_R7_seul']['p']:.5f}" if L5["rejet"] else ""))
    verdict += " ; exploratoire : aucune idée désignée (règle v2)"
    res = {
        "version": VERSION, "outil_version": O.VERSION, "regle": "regle-v2.md (exploratoire, R-2726)",
        "programmes_sha256": {"classer": O.sha256_fichier(__file__), "outil": O.sha256_fichier(ICI / NOM_OUTIL)},
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__},
        "fiches_validees": prov,
        "envois": {"manifeste_sha256": O.sha256_fichier(Path(dossier_envois) / O.MANIFESTE),
                   "reponses": {L: lectures[L]["reponses"] for L in O.LECTURES}},
        "graines": {"ordres": O.ENTROPIE_ORDRES, "test": ENTROPIE_TEST, "separation": ENTROPIE_SEPARATION,
                    "permutations": permutations},
        "precisions": PRECISIONS,
        "verdict": verdict, "lisible": lisible, "lecture_complete": lecture_complete, "designees": [],
        "separation": sep,
        "rang_exploratoire": {"ordre_neuves": cl["ordre_neuves"], "deux_premieres": cl["deux_premieres"],
                              "restreint_a_R7_retenu_1": rang_R7, "statut": cl["statut"], "departage": departage,
                              "hors_question": env["pile"]["hors_question"],
                              "note": "exploratoire : ne désigne rien au sens de la conception, § 4.6"},
        "temoin_score_permute": {**tp, "communes_avec_deux_premieres": len(set(tp["deux_premieres"]) &
                                                                           set(cl["deux_premieres"]))},
        "L1": L1, "L2": L2, "L3": L3, "L4": L4, "L5": L5, "descriptif_holm": desc,
        "hasard_R7_selon_la_chaine": hasard_R7,
        "relecture_contre_premiere_lecture": contre_premiere,
        "regle_v2_sur_la_premiere_lecture": regle_v2_premiere,
        "echecs": echecs, "audit_proprete": audit, "exactitude_lecteur": exactitude,
        "non_prouves": {L: lectures[L]["non_prouves"] for L in O.LECTURES},
        "passages_courts_refuses": {L: lectures[L]["passages_courts_refuses"] for L in O.LECTURES},
        "passages_au_dela_de_200": {L: lectures[L]["passages_au_dela_de_200"] for L in O.LECTURES},
        "anomalies": {L: lectures[L]["anomalies"] for L in O.LECTURES},
        "retenu": retenu, "comptes_par_proposeur": par_auteur,
        "juge_de_l_organisme": "non ouvert (conception, § 4.8)",
    }
    return res, lectures


def resume_md(r: dict) -> str:
    sep = r["separation"]
    l = ["# Classement exploratoire de la relecture — course « conception propre » — v3.2 (règle v2)\n",
         f"Programme `{r['version']}` (`{r['programmes_sha256']['classer'][:12]}…`), outil "
         f"`{r['programmes_sha256']['outil'][:12]}…` ; envois `{r['envois']['manifeste_sha256'][:12]}…`. "
         "**Exploratoire** (R-2726) : aucune idée désignée ; le verdict E2 de la première lecture reste tel quel.\n",
         f"**Verdict** : {r['verdict']}.\n",
         f"- Lecture complète : {r['lecture_complete']['complete']} ; anomalies bloquantes : "
         + ("; ".join(f"{L} lot {a['lot']} {a['genre']}" for L in ('L1', 'L2') for a in r['lecture_complete']['anomalies'][L])
            or "aucune")
         + f" ; fiches réelles touchées : {len(r['lecture_complete']['reelles_touchees'])}, témoins touchés : "
         f"{len(r['lecture_complete']['temoins_touches'])}.",
         "- Passages courts refusés, par lecture : "
         + " ; ".join(f"{L} : {sum(r['passages_courts_refuses'][L].values())}" for L in ('L1', 'L2'))
         + " ; passages au-delà de 200 caractères : "
         + " ; ".join(f"{L} : {r['passages_au_dela_de_200'][L]}" for L in ('L1', 'L2')) + ".",
         f"- Rang exploratoire (deux premières, information) : {', '.join(r['rang_exploratoire']['deux_premieres']) or 'aucune'} ; "
         f"neuves : {len(r['rang_exploratoire']['ordre_neuves'])} ; restreint à R7 retenu = 1 : "
         f"{len(r['rang_exploratoire']['restreint_a_R7_retenu_1'])}.",
         f"- Témoin à score permuté : {', '.join(r['temoin_score_permute']['deux_premieres']) or 'aucune'}.",
         f"- L1 {'tient' if r['L1']['tient'] else 'manque'} ({r['L1']['reconnues']}/{r['L1']['sur']}) ; "
         f"L2 {'tient' if r['L2']['tient'] else 'manque'} ; L3 v2 {'tient' if r['L3']['tient'] else 'manque'} ; "
         f"L4 {'tient' if r['L4']['tient'] else 'manque'} (R7 : {r['L4']['R7']['jugee_sur']}, κ = "
         f"{r['L4']['R7']['kappa']}, accord {r['L4']['R7']['accord_brut']:.3f} ; N : {r['L4']['N']['jugee_sur']}, κ = "
         f"{r['L4']['N']['kappa']}, accord {r['L4']['N']['accord_brut']:.3f}).",
         f"- L5 v2 : p = {r['L5']['test']['p']}, moyennes C v2 réelles {r['L5']['moyenne_reelles']} contre hasard "
         f"{r['L5']['moyenne_hasard']} ; rejet : {r['L5']['rejet']}. Séparation : **{sep['issue']}** (R7 seul : p = "
         f"{sep['test_R7_seul']['p']}, lu : {sep['lu']}).",
         f"- Hasard, R7 retenu selon la chaîne : cohérente {r['hasard_R7_selon_la_chaine']['chaine_coherente']} ; "
         f"contraire {r['hasard_R7_selon_la_chaine']['chaine_contraire']}.",
         f"- Relecture contre première lecture : {r['relecture_contre_premiere_lecture'].get('fiches_communes')} fiches "
         "communes" + "".join(f" ; {c} κ = {d['kappa']}, accord {d['accord_brut']:.3f}"
                               for c, d in r['relecture_contre_premiere_lecture'].get('par_critere', {}).items()) + ".",
         f"- Règle v2 sur la première lecture : deux premières communes avec la relecture : "
         f"{r['regle_v2_sur_la_premiere_lecture'].get('deux_premieres_communes_avec_la_relecture')} ; cinq premières : "
         f"{r['regle_v2_sur_la_premiere_lecture'].get('cinq_premieres_communes_avec_la_relecture')}.",
         f"- Issues : {', '.join(k for k, x in r['echecs'].items() if x) or 'aucune'} ; audit de propreté déclenché : "
         f"{r['audit_proprete']['declenche']}.",
         "\n| Comparaison descriptive | différence | p brute | p Holm |\n|---|---|---|---|"]
    for d in r["descriptif_holm"]:
        l.append(f"| {d['critere']} | {d['difference']} | {d['p_brute']} | {d.get('p_holm')} |")
    l.append("\nNotes du juge de l'organisme : non ouvertes (conception, § 4.8).\n")
    return "\n".join(l) + "\n"


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--envois", required=True)
    a.add_argument("--sortie", required=True)
    a.add_argument("--racine", default=str(O.RACINE_DEFAUT))
    args = a.parse_args(argv)
    sortie = Path(args.sortie)
    try:
        if sortie.exists() and any(sortie.iterdir()):
            raise O.Refus(f"{sortie} existe et n'est pas vide : on n'écrase jamais (R12)")
        r, lectures = classement(args.envois, args.racine)
        sortie.mkdir(parents=True, exist_ok=True)
        for L in O.LECTURES:
            O.ecrire_scelle(sortie / f"lecture-verifiee-{L}-{O.SUFFIXE}.json", O.json_texte(lectures[L]))
        h = O.ecrire_scelle(sortie / f"classement-{O.SUFFIXE}.json", O.json_texte(r))
        O.ecrire_scelle(sortie / f"classement-{O.SUFFIXE}.md", resume_md(r))
        print(json.dumps({"verdict": r["verdict"], "separation": r["separation"]["issue"], "designees": [],
                          "classement_sha256": h}, ensure_ascii=False))
    except O.Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
