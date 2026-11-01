#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Implémentation B (indépendante) de la statistique décisive — course de convergence des règles
de défense et sa réplication.

Écrite uniquement d'après « specification-statistique-decisive-v1.md » (les « § n » renvoient aux
sections de cette spécification). Elle n'importe rien du dépôt : bibliothèque standard + numpy.

Sous-commandes
  analyser           analyse un fichier de résultats au format E1 ; sortie = fichier JSON neuf,
                     jamais écrasé (sections 5 à 11 de la spécification)
  regle-d            règle D (§ 4) appliquée à un préenregistrement scellé ou à une empreinte
  comparer           compare une sortie de cette implémentation à une analyse de référence (§ 11)
  valider-originale  validation sur la course originale (§ 12) ; écrit validation-b-v1.json / .md

Codes de sortie : 0 = tout va bien ; 2 = arrêt prescrit par la spécification (empreinte fausse,
garde violée : aucune sortie) ; 3 = sortie écrite mais un arrêt de la liste d'arrêt est déclenché
(§ 10.3 « graines non neuves ») : la lecture n'est pas autorisée ; 4 = erreur d'usage (par exemple
fichier de sortie déjà existant).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import re
import sys
import time
from pathlib import Path

import numpy as np

VERSION_IMPLEMENTATION = "implementation-b-v1"

# --------------------------------------------------------------------------------------------
# § 2 — constantes (binaires64 les plus proches de l'écriture décimale)
# --------------------------------------------------------------------------------------------
N = 100                      # instances par budget
B = 20_000                   # rééchantillonnages
P = (0.003125, 0.00625, 0.0125, 0.025, 0.05, 0.95, 0.975, 0.9875, 0.99375, 0.996875)
M = 0.02                     # marge d'effet d'intérêt (S1)
S5 = 0.02                    # tolérance de non-régression sur (ii)
ALPHA = 0.01                 # taux de fausses alertes visé
DEUX_ALPHA = 2 * ALPHA       # 0,02 (le doublement est exact en binaire)
TAU = 0.05                   # seuil de taille de la réplication de HR1
Z_ETOILE = 2.497705474412374  # quantile 0,99375 de la loi normale centrée réduite
EPS = 1e-9                   # tolérance de concordance entre deux implémentations

# § 7 — seuils des contrôles de santé
SEUIL_T2_TROP_BEAU = 0.99
SEUIL_T2_EST_R3 = 0.30
SEUIL_T2_EST_XBARRE = 0.30
SEUIL_T3_POIDS_PUR = 1.0 - 1e-9
SEUIL_T3_NB = 50
SEUIL_T4_COS = 0.999
SEUIL_T4_NB = 50
SEUIL_T5 = 0.01
SEUIL_T6 = 0.001
# § 10.2 / 10.3
SEUIL_TR2 = 0.001
SEUIL_GRAINES_NEUVES = 10
# § 5.2
TOLERANCE_BORNES_01 = 1e-12

BUDGETS = (1, 2)
RACINE_COURSE_ORIGINALE = 20266201

# § 3 — empreintes des pièces de la course originale (E4)
EMPREINTE_RESULTATS_ORIGINAUX = "d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b"
EMPREINTE_ANALYSE_ORIGINALE = "18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42"

# --------------------------------------------------------------------------------------------
# § 1 — variantes, mesures, libellés
# --------------------------------------------------------------------------------------------
LAMBDA_GREC = "λ"
NOMS_VARIANTES = ("R0", "R1", "R2", "R3", "R4[moyenne," + LAMBDA_GREC + "=0.3]")
RANG = {nom: i for i, nom in enumerate(NOMS_VARIANTES)}
NOM_COURT = {"R0": "R0", "R1": "R1", "R2": "R2", "R3": "R3", NOMS_VARIANTES[4]: "R4"}
NOM_LONG = {court: long for long, court in NOM_COURT.items()}
VARIANTES_CONTRASTEES = ("R0", "R1", "R3", NOMS_VARIANTES[4])   # toutes sauf R2

# identifiant interne -> (code j, champ). « Xbarre » = X̄, exploitabilité moyenne au fil des tours.
MESURES = {
    "V": (0, "V_iii_final"),
    "ii": (1, "ii_final"),
    "X": (2, "exploitabilite_finale"),
    "Xbarre": (8, "exploitabilite_moyenne_tours"),
}
CHAMPS_MESURES = tuple(champ for (_, champ) in MESURES.values())
CHAMPS_LUS = CHAMPS_MESURES + ("V_iii_standard", "V_iii_renforce", "fpr_final")


def libelle_contraste(nom_variante: str, mesure: str) -> str:
    """Libellé d'un contraste dans les fichiers d'analyse : « <nom de k> - R2 (<champ de M>) »."""
    return f"{nom_variante} - R2 ({MESURES[mesure][1]})"


TOUS_LES_CONTRASTES = tuple((nom, mes) for mes in MESURES for nom in VARIANTES_CONTRASTEES)   # 16
# § 11 : arrêt pour discordance sur ces cinq-là (par budget) ; alerte seulement pour les 11 autres
CONTRASTES_A_ARRET = (("R3", "V"), ("R0", "V"), (NOMS_VARIANTES[4], "V"), ("R0", "ii"), ("R1", "Xbarre"))
# § 10.2 — contrastes primaires (variante, mesure, budget)
PRIMAIRES = (("R3", "V", 1), ("R3", "V", 2), ("R0", "V", 1), ("R0", "V", 2))

CLES_QUANTILES = tuple("q" + repr(p) for p in P)
IDX_B2 = (1, 8)   # [q(0,00625) ; q(0,99375)]
IDX_B8 = (0, 9)   # [q(0,003125) ; q(0,996875)]
IDX_E8 = (1, 8)   # mêmes quantiles que B2, rôle d'équivalence

# --------------------------------------------------------------------------------------------
# § 8 / § 9 / § 10 — libellés (copiés mot pour mot de la spécification)
# --------------------------------------------------------------------------------------------
A_DEGENERE = "non concluant : jeu dégénéré"
A_CONFIRMEE = "HR1 confirmée"
A_REFUTEE = "HR1 réfutée"
A_NON_DEMONTREE = "HR1 non démontrée"
EQUIVALENT = "≈"
INCERTAIN = "?"
LIBELLES_TABLE_C = {
    1: "régression avérée au-delà de la tolérance",
    2: "régression démontrée, sous la tolérance",
    3: "régression démontrée, ampleur non tranchée",
    4: "amélioration",
    5: "sans régression à S5 près",
    6: "imprécis",
}
V_SANTE = "non jugeable (santé)"
V_DEGENERE = "non jugeable (jeu dégénéré)"
V_IMPRECIS = "non jugeable (imprécis)"
V_REPLIQUEE = "répliquée"
V_HR1_SIGNE = "non répliquée (signe inversé)"
V_HR1_PETIT = "non répliquée (effet démontré inférieur à 0,05)"
V_HR0_INTERET = "non répliquée (le réentraînement l'emporte d'un effet d'intérêt)"
V_HR0_NON_NUL = "non répliquée (le réentraînement l'emporte, effet démontré non nul)"
V_NON_REPLIQUEE = "non répliquée"
V_HR3_SANS_VERDICT = "sans verdict (R4 ≈ défense figée)"
V_AUDIT_ATTENTE = "non jugeable (audit en attente)"
V_ARTEFACT = "non jugeable (artefact)"
O_CONFIRMEE = "confirmée"
O_REFUTEE = "réfutée"
O_NON_TRANCHEE = "non tranchée"
ISSUES = {
    1: "non jugeable (plomberie)",
    2: "en attente d'audit",
    3: "non jugeable (artefact)",
    4: "échec de réplication du résultat positif",
    5: "réplication réussie",
    6: "réplication partielle : le mélange tient, l'équivalence de la défense figée ne tient pas",
    7: "réplication partielle : le mélange tient, l'équivalence de la défense figée reste imprécise",
    8: "non jugeable",
}

# § 4 — règle D : ensembles interdits et six entiers des vecteurs d'essai
RACINES_INTERDITES_EXPLICITES = frozenset({20261201, 20261202, 20266201, 20266202})
PLAGE_INTERDITE = (20261000, 20269999)   # bornes incluses
VECTEURS_REGLE_D = (
    ("d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d",
     11786724493248295725, 9136419304016434890),
    ("0" * 64, 15793235383387715774, 12390638538380655177),
    ("f" * 64, 10168828190493638947, 4616211851522120706),
)
ENTIERS_DES_VECTEURS = frozenset(x for (_, a, b) in VECTEURS_REGLE_D for x in (a, b))

# § 5.5 — vecteurs d'essai du générateur (racine 20266201)
VECTEURS_GENERATEUR = (
    {"cle": (1, 203, 0, 0, 99),
     "ligne0_dix_premiers": [80, 79, 39, 86, 45, 87, 54, 22, 58, 80],
     "derniere_ligne_cinq_derniers": [56, 63, 4, 66, 85]},
    {"cle": (2, 200, 0, 0, 99),
     "ligne0_dix_premiers": [73, 34, 66, 88, 64, 92, 23, 55, 84, 31],
     "derniere_ligne_cinq_derniers": [10, 38, 20, 60, 51]},
)


class Arret(Exception):
    """Arrêt prescrit par la spécification : aucune sortie, aucun repli silencieux."""


# ============================================================================================
# Lecture exacte, empreintes (§ 3)
# ============================================================================================
def _paires_sans_doublon(paires):
    objet = {}
    for cle, valeur in paires:
        if cle in objet:
            raise Arret(f"clé dupliquée dans le JSON : {cle!r}")
        objet[cle] = valeur
    return objet


def lire_json_octets(octets: bytes, role: str):
    """Lecture exacte : décimaux lus comme binaire64 (float de Python), entiers lus exactement
    (int de Python, précision arbitraire). Une clé dupliquée est un arrêt."""
    try:
        return json.loads(octets.decode("utf-8"), object_pairs_hook=_paires_sans_doublon)
    except Arret as e:
        raise Arret(f"{role} : {e}") from None
    except (UnicodeDecodeError, ValueError) as e:
        raise Arret(f"{role} : JSON illisible ({e})") from None


def empreinte_octets(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def lire_compagnon(chemin: Path):
    """Fichier compagnon « <nom>.sha256 » : une ligne « 64 hexadécimaux minuscules, deux espaces,
    nom du fichier ». On cherche d'abord <fichier>.sha256 puis <fichier sans extension>.sha256.
    Rend (empreinte, nom inscrit, chemin du compagnon)."""
    for cand in (Path(str(chemin) + ".sha256"), chemin.with_suffix(".sha256")):
        if cand.is_file():
            texte = cand.read_text(encoding="utf-8")
            lignes = [ligne for ligne in texte.split("\n") if ligne != ""]
            if len(lignes) != 1:
                raise Arret(f"compagnon {cand.name} : une seule ligne attendue")
            m = re.fullmatch(r"([0-9a-f]{64})  (.+)", lignes[0])
            if m is None:
                raise Arret(f"compagnon {cand.name} : format « empreinte, deux espaces, nom » non respecté")
            return m.group(1), m.group(2), cand
    raise Arret(f"aucun fichier compagnon <nom>.sha256 à côté de {chemin.name}")


def lire_fichier_verifie(chemin, role: str, *, attendue: str | None = None, avertissements=None):
    """Lit les octets, vérifie l'empreinte (valeur imposée, sinon fichier compagnon), rend
    (octets, empreinte). Toute différence : arrêt."""
    chemin = Path(chemin)
    try:
        octets = chemin.read_bytes()
    except OSError as e:
        raise Arret(f"{role} : lecture impossible ({e})") from None
    sha = empreinte_octets(octets)
    if attendue is None:
        attendue, nom_inscrit, _ = lire_compagnon(chemin)
        if nom_inscrit != chemin.name and avertissements is not None:
            avertissements.append(f"{role} : le compagnon nomme « {nom_inscrit} », le fichier est « {chemin.name} »")
    if sha != attendue:
        raise Arret(f"{role} : empreinte {sha} différente de l'attendue {attendue}")
    return octets, sha


# ============================================================================================
# § 4 — règle D
# ============================================================================================
def regle_d_derivation(h_hex: str):
    """Étapes 1 à 5 : E = entier de H (base 16) ; S = SeedSequence(E) sans clé de descendance ;
    (w0, w1) = deux premiers mots uint64 de generate_state ; rho = w0, rho_t = w1. Aucune garde."""
    if not re.fullmatch(r"[0-9a-f]{64}", h_hex):
        raise Arret("règle D : H doit s'écrire en 64 chiffres hexadécimaux minuscules")
    e = int(h_hex, 16)
    mots = np.random.SeedSequence(e).generate_state(2, dtype=np.uint64)
    return int(mots[0]), int(mots[1])


def regle_d_gardes(rho: int, rho_t: int) -> None:
    """Étape 6 : rho != rho_t ; ni l'un ni l'autre dans F (quatre racines nommées + plage
    [20261000 ; 20269999]) ni parmi les six entiers des vecteurs d'essai. Sinon arrêt."""
    if rho == rho_t:
        raise Arret("règle D : rho == rho_t")
    for nom, r in (("rho", rho), ("rho_t", rho_t)):
        if r in RACINES_INTERDITES_EXPLICITES or PLAGE_INTERDITE[0] <= r <= PLAGE_INTERDITE[1]:
            raise Arret(f"règle D : {nom} = {r} appartient à l'ensemble interdit F")
        if r in ENTIERS_DES_VECTEURS:
            raise Arret(f"règle D : {nom} = {r} est un des six entiers des vecteurs d'essai")


def regle_d(h_hex: str):
    """Règle D complète (dérivation + gardes). Rend (rho, rho_t)."""
    rho, rho_t = regle_d_derivation(h_hex)
    regle_d_gardes(rho, rho_t)
    return rho, rho_t


def regle_d_depuis_octets(octets: bytes):
    """H = SHA-256 des octets exacts du préenregistrement scellé. Rend (H, rho, rho_t)."""
    h = empreinte_octets(octets)
    rho, rho_t = regle_d(h)
    return h, rho, rho_t


# ============================================================================================
# § 5.1 — sélection, ordre, gardes ; extraction des champs
# ============================================================================================
def _entier(x, nom: str) -> int:
    if isinstance(x, bool) or not isinstance(x, int):
        raise Arret(f"{nom} : entier attendu, trouvé {x!r}")
    return x


def _nombre(x, nom: str) -> float:
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise Arret(f"{nom} : nombre attendu, trouvé {x!r}")
    try:
        v = float(x)
    except OverflowError:
        raise Arret(f"{nom} : entier trop grand pour un nombre à virgule")
    if not math.isfinite(v):
        raise Arret(f"{nom} : valeur non finie")
    return v


def valider_forme_E1(e1) -> list:
    """Forme de E1 (§ 3) : objet à trois clés ; `resultat` contient `temps` et `resultats` (lu « au moins » :
    d'autres clés dans `resultat` sont ignorées) ; `resultats` : liste de 200 tâches."""
    if not isinstance(e1, dict) or set(e1) != {"run_id", "manifeste_sha256", "resultat"}:
        raise Arret("E1 : l'objet doit avoir exactement les clés run_id, manifeste_sha256, resultat")
    res = e1["resultat"]
    if not isinstance(res, dict) or not {"temps", "resultats"} <= set(res):
        raise Arret("E1 : `resultat` doit contenir `temps` et `resultats`")
    taches = res["resultats"]
    if not isinstance(taches, list) or len(taches) != 2 * N:
        raise Arret("E1 : `resultats` doit être une liste de 200 tâches")
    return taches


DELTA_DU_BUDGET = {1: 1.4, 2: 1.6}


def selectionner_taches(taches: list, avertissements: list | None = None) -> dict:
    """T_c triées par instance croissante ; gardes du § 5.1. Rend {c: [tâche, ...]} (c = 1, 2).
    Un champ `delta` incohérent avec `code_delta` (c = 1 : 1,4 ; c = 2 : 1,6) est signalé en avertissement."""
    par_budget = {c: [] for c in BUDGETS}
    delta_incoherent = set()
    for i, t in enumerate(taches):
        if not isinstance(t, dict):
            raise Arret(f"tâche {i} : objet attendu")
        for cle in ("code_delta", "instance", "delta", "racine", "racine_tenue", "config_sha256", "regles"):
            if cle not in t:
                raise Arret(f"tâche {i} : champ `{cle}` absent")
        c = _entier(t["code_delta"], f"tâche {i} code_delta")
        if c not in par_budget:
            raise Arret(f"tâche {i} : code_delta = {c} (1 ou 2 attendu)")
        _entier(t["instance"], f"tâche {i} instance")
        if t["delta"] != DELTA_DU_BUDGET[c]:
            delta_incoherent.add((c, repr(t["delta"])))
        par_budget[c].append(t)
    if delta_incoherent and avertissements is not None:
        avertissements.append("E1 : `delta` incohérent avec `code_delta` (budget, delta lu) : "
                              + ", ".join(f"({c}, {d})" for c, d in sorted(delta_incoherent)))
    for c in BUDGETS:
        par_budget[c].sort(key=lambda t: t["instance"])
        if len(par_budget[c]) != N:
            raise Arret(f"budget {c} : {len(par_budget[c])} tâches au lieu de {N}")
        if [t["instance"] for t in par_budget[c]] != list(range(N)):
            raise Arret(f"budget {c} : les instances ne sont pas exactement 0, 1, …, {N - 1} sans doublon")
        for t in par_budget[c]:
            regles = t["regles"]
            if not isinstance(regles, dict) or set(regles) != set(NOMS_VARIANTES):
                raise Arret(f"budget {c}, instance {t['instance']} : les clés de `regles` ne sont pas "
                            f"exactement les cinq noms de variantes")
            if list(regles) != list(NOMS_VARIANTES):
                raise Arret(f"budget {c}, instance {t['instance']} : ordre des variantes différent de "
                            f"R0, R1, R2, R3, R4")
    return par_budget


def extraire_donnees(taches_c: list, c: int) -> dict:
    """Champs numériques de chaque variante (tableaux numpy float64 de longueur n, dans l'ordre des
    instances), poids finaux de R3 et cosinus consécutifs de R4. Gardes du § 5.2 et de la garde de
    cohérence de V (§ 7)."""
    champs = {nom: {ch: np.empty(N) for ch in CHAMPS_LUS} for nom in NOMS_VARIANTES}
    for l, t in enumerate(taches_c):
        for nom in NOMS_VARIANTES:
            v = t["regles"][nom]
            if not isinstance(v, dict):
                raise Arret(f"budget {c}, instance {l}, {nom} : objet attendu")
            for ch in CHAMPS_LUS:
                if ch not in v:
                    raise Arret(f"budget {c}, instance {l}, {nom} : champ `{ch}` absent")
                x = _nombre(v[ch], f"budget {c}, instance {l}, {nom}.{ch}")
                if ch in CHAMPS_MESURES and not (-TOLERANCE_BORNES_01 <= x <= 1.0 + TOLERANCE_BORNES_01):
                    raise Arret(f"budget {c}, instance {l}, {nom}.{ch} = {x} hors de [0 ; 1] à 1e-12 près")
                champs[nom][ch][l] = x
            # garde de cohérence de V : V_iii_final = min(V_iii_standard, V_iii_renforce) exactement
            if champs[nom]["V_iii_final"][l] != min(champs[nom]["V_iii_standard"][l],
                                                   champs[nom]["V_iii_renforce"][l]):
                raise Arret(f"budget {c}, instance {l}, {nom} : V_iii_final ≠ min(V_iii_standard, V_iii_renforce)")
    poids_r3, cos_r4 = [], []
    for l, t in enumerate(taches_c):
        w = t["regles"]["R3"].get("poids_finaux")
        if not isinstance(w, list) or len(w) == 0:
            raise Arret(f"budget {c}, instance {l}, R3 : `poids_finaux` doit être une liste non vide")
        poids_r3.append([_nombre(x, f"budget {c}, instance {l}, R3.poids_finaux") for x in w])
        par_tour = t["regles"][NOMS_VARIANTES[4]].get("par_tour")
        cos = par_tour.get("cos_consecutif") if isinstance(par_tour, dict) else None
        if not isinstance(cos, list) or len(cos) != 8:
            raise Arret(f"budget {c}, instance {l}, R4 : `par_tour.cos_consecutif` doit contenir 8 nombres")
        cos_r4.append([_nombre(x, f"budget {c}, instance {l}, R4.cos_consecutif") for x in cos])
    return {"champs": champs, "poids_R3": poids_r3, "cos_R4": cos_r4}


# ============================================================================================
# § 5.2 à 5.7 — la statistique d'un contraste
# ============================================================================================
def code_generateur(mesure: str, nom_variante: str) -> int:
    """code = 200 + 100 × j(M) + r(k)  (§ 5.4)."""
    return 200 + 100 * MESURES[mesure][0] + RANG[nom_variante]


def generateur(rho: int, c: int, code: int) -> np.random.Generator:
    """Generator fondé sur PCG64, initialisé par SeedSequence(entropie rho, clé (c, code, 0, 0, 99))."""
    graine = np.random.SeedSequence(entropy=int(rho), spawn_key=(int(c), int(code), 0, 0, 99))
    return np.random.Generator(np.random.PCG64(graine))


def indices_reechantillonnage(rho: int, c: int, code: int) -> np.ndarray:
    """Matrice I (B lignes, n colonnes) d'entiers uniformes de {0..n-1}, un seul appel, remplie ligne
    par ligne : integers(0, n, size=(B, n)) en entiers signés 64 bits (§ 5.5)."""
    return generateur(rho, c, code).integers(0, N, size=(B, N), dtype=np.int64)


def quantile_type7(tri: np.ndarray, p: float) -> float:
    """Quantile de type 7 (Hyndman et Fan) d'un tableau déjà trié (§ 5.6)."""
    h = (len(tri) - 1) * p
    f = int(math.floor(h))
    t = h - f
    if f >= len(tri) - 1:
        return float(tri[-1])
    return float(tri[f]) + t * (float(tri[f + 1]) - float(tri[f]))


def statistique_contraste(d: np.ndarray, rho: int, c: int, code: int) -> dict:
    """Sortie d'un contraste au format du § 5.7 à partir des différences appariées d."""
    if d.shape != (N,):
        raise Arret("différences appariées : longueur ≠ n")
    est = float(np.mean(d))
    s = float(np.sqrt(np.sum((d - est) ** 2) / (N - 1)))
    zeros = int(np.count_nonzero(d == 0))
    mu = np.sum(d[indices_reechantillonnage(rho, c, code)], axis=1) / N
    tri = np.sort(mu)
    quantiles = {cle: quantile_type7(tri, p) for cle, p in zip(CLES_QUANTILES, P)}
    return {"moyenne": est, "ecart_type": s, "n": N, "quantiles": quantiles, "zeros_exacts": zeros}


def bornes_depuis_statistique(stat: dict) -> dict:
    """Intervalles B2, B8, E8 (§ 2) d'une statistique au format du § 5.7."""
    q = [stat["quantiles"][cle] for cle in CLES_QUANTILES]
    return {"B2": (q[IDX_B2[0]], q[IDX_B2[1]]),
            "B8": (q[IDX_B8[0]], q[IDX_B8[1]]),
            "E8": (q[IDX_E8[0]], q[IDX_E8[1]])}


def calculer_contrastes_budget(donnees: dict, c: int, rho: int) -> dict:
    """Les 16 contrastes d'un budget : {libellé: statistique du § 5.7}."""
    champs = donnees["champs"]
    sortie = {}
    for nom, mes in TOUS_LES_CONTRASTES:
        champ = MESURES[mes][1]
        d = champs[nom][champ] - champs["R2"][champ]
        sortie[libelle_contraste(nom, mes)] = statistique_contraste(d, rho, c, code_generateur(mes, nom))
    return sortie


# ============================================================================================
# Comparaisons à un seuil avec suivi de la « frontière numérique » (§ 8)
# ============================================================================================
def _cmp(trace: list, nom: str, x: float, op: str, seuil: float) -> bool:
    if op == ">":
        r = x > seuil
    elif op == "<":
        r = x < seuil
    elif op == ">=":
        r = x >= seuil
    elif op == "<=":
        r = x <= seuil
    else:   # pragma: no cover
        raise ValueError(op)
    trace.append((nom, x, op, seuil, bool(r)))
    return bool(r)


def _marge_et_proches(trace: list):
    marge = min((abs(x - s) for (_, x, _, s, _) in trace), default=None)
    proches = [{"quantite": nom, "valeur": x, "comparaison": f"{op} {s!r}", "ecart_au_seuil": abs(x - s)}
               for (nom, x, op, s, _) in trace if abs(x - s) <= EPS]
    return marge, proches


def _clore(trace: list, ligne: int, libelle: str, cle: str = "classe", extra: dict | None = None) -> dict:
    marge, proches = _marge_et_proches(trace)
    r = {"ligne": ligne, cle: libelle, "frontiere": bool(proches),
         "marge_min_au_seuil": marge, "comparaisons_a_la_frontiere": proches}
    if extra:
        r.update(extra)
    return r


# ============================================================================================
# § 8 — classes (la première condition vraie décide)
# ============================================================================================
def classe_table_A(par_budget: dict) -> dict:
    """Table A — Δ(R3, R2) sur V (HR1, règles de la course originale).
    par_budget[c] = {"est", "bas_B2", "haut_B2", "moyennes_V": {nom de variante: moy_c(k, V)}}."""
    trace: list = []
    degenere = {}
    for c in BUDGETS:
        pb = par_budget[c]
        degenere[c] = all([_cmp(trace, f"moy_{c}({NOM_COURT[nom]}, V)", pb["moyennes_V"][nom], "<=", DEUX_ALPHA)
                           for nom in NOMS_VARIANTES])
    detail = {str(c): {"est": par_budget[c]["est"], "bas_B2": par_budget[c]["bas_B2"],
                       "haut_B2": par_budget[c]["haut_B2"], "jeu_degenere": degenere[c]} for c in BUDGETS}
    extra = {"par_budget": detail}
    if any(degenere.values()):                                                      # ligne 1
        return _clore(trace, 1, A_DEGENERE, extra=extra)
    ok2 = {}
    for c in BUDGETS:
        a = _cmp(trace, f"est_{c}", par_budget[c]["est"], ">=", M)
        b = _cmp(trace, f"bas(B2)_{c}", par_budget[c]["bas_B2"], ">", 0.0)
        ok2[c] = a and b
    if ok2[1] and ok2[2]:                                                           # ligne 2
        return _clore(trace, 2, A_CONFIRMEE, extra=extra)
    neg = [_cmp(trace, f"haut(B2)_{c}", par_budget[c]["haut_B2"], "<", 0.0) for c in BUDGETS]
    if any(neg):                                                                    # ligne 3
        return _clore(trace, 3, A_REFUTEE, extra=extra)
    return _clore(trace, 4, A_NON_DEMONTREE, extra=extra)                           # ligne 4


def _classe_B_generique(bornes: dict, libelles: tuple) -> dict:
    bas8, haut8 = bornes["B8"]
    bas_e, haut_e = bornes["E8"]
    trace: list = []
    if _cmp(trace, "bas(B8)", bas8, ">", M):
        return _clore(trace, 1, libelles[0])
    if _cmp(trace, "haut(B8)", haut8, "<", -M):
        return _clore(trace, 2, libelles[1])
    a = _cmp(trace, "bas(E8)", bas_e, ">", -M)
    b = _cmp(trace, "haut(E8)", haut_e, "<", M)
    if a and b:
        return _clore(trace, 3, libelles[2])
    if _cmp(trace, "bas(B8)", bas8, ">", 0.0):
        return _clore(trace, 4, libelles[3])
    if _cmp(trace, "haut(B8)", haut8, "<", 0.0):
        return _clore(trace, 5, libelles[4])
    return _clore(trace, 6, libelles[5])


def classe_table_B(nom_court: str, bornes: dict) -> dict:
    """Table B — Δ(R_k, R2) sur V (signe + : R_k détecte mieux, donc est moins exploitable)."""
    k = nom_court
    return _classe_B_generique(bornes, (f"{k} > R2", f"R2 > {k}", EQUIVALENT, f"{k} ≳ R2", f"R2 ≳ {k}", INCERTAIN))


def classe_table_Bprime(nom_court: str, bornes: dict) -> dict:
    """Table B′ — D̄(R_k, R2) sur X̄ (signe + : R_k plus exploitable)."""
    k = nom_court
    return _classe_B_generique(bornes, (f"R2 > {k}", f"{k} > R2", EQUIVALENT, f"R2 ≳ {k}", f"{k} ≳ R2", INCERTAIN))


def classe_table_C(bornes: dict) -> dict:
    """Table C — Δ(R_k, R2) sur (ii), bornes B8, tolérance S5 ; on rend le numéro de ligne."""
    bas, haut = bornes["B8"]
    trace: list = []
    if _cmp(trace, "haut(B8)", haut, "<", -S5):
        return _clore(trace, 1, LIBELLES_TABLE_C[1])
    a = _cmp(trace, "haut(B8)", haut, "<", 0.0)
    b = _cmp(trace, "bas(B8)", bas, ">", -S5)
    if a and b:
        return _clore(trace, 2, LIBELLES_TABLE_C[2])
    if a:
        return _clore(trace, 3, LIBELLES_TABLE_C[3])
    if _cmp(trace, "bas(B8)", bas, ">", 0.0):
        return _clore(trace, 4, LIBELLES_TABLE_C[4])
    if _cmp(trace, "bas(B8)", bas, ">", -S5):
        return _clore(trace, 5, LIBELLES_TABLE_C[5])
    return _clore(trace, 6, LIBELLES_TABLE_C[6])


def classes_depuis_contrastes(contrastes: dict, moyennes_V: dict) -> dict:
    """Applique les tables A, B, B′, C à des contrastes au format du § 5.7.
    contrastes = {"1": {libellé: stat}, "2": {...}} ; moyennes_V = {"1": {nom de variante: moy}, ...}.
    Les moyennes de V servent seulement au prédicat « jeu dégénéré » de la table A."""
    bornes = {str(c): {(nom, mes): bornes_depuis_statistique(contrastes[str(c)][libelle_contraste(nom, mes)])
                       for nom, mes in TOUS_LES_CONTRASTES} for c in BUDGETS}
    entrees_A = {}
    for c in BUDGETS:
        stat = contrastes[str(c)][libelle_contraste("R3", "V")]
        b2 = bornes[str(c)][("R3", "V")]["B2"]
        entrees_A[c] = {"est": stat["moyenne"], "bas_B2": b2[0], "haut_B2": b2[1],
                        "moyennes_V": moyennes_V[str(c)]}
    classes = {"table_A": classe_table_A(entrees_A), "table_B": {}, "table_Bprime": {}, "table_C": {}}
    for nom in VARIANTES_CONTRASTEES:
        court = NOM_COURT[nom]
        classes["table_B"][court] = {str(c): classe_table_B(court, bornes[str(c)][(nom, "V")]) for c in BUDGETS}
        classes["table_Bprime"][court] = {str(c): classe_table_Bprime(court, bornes[str(c)][(nom, "Xbarre")])
                                          for c in BUDGETS}
        classes["table_C"][court] = {str(c): classe_table_C(bornes[str(c)][(nom, "ii")]) for c in BUDGETS}
    return classes


# ============================================================================================
# § 7 — contrôles de santé (recalculés depuis E1, par budget)
# ============================================================================================
def controles_sante_budget(donnees: dict, contrastes_c: dict) -> dict:
    """T2 à T6 pour un budget. `contrastes_c` : {libellé: stat} du même budget."""
    ch = donnees["champs"]

    def moy(nom, champ):
        return float(np.mean(ch[nom][champ]))

    moyennes_V = {nom: moy(nom, "V_iii_final") for nom in NOMS_VARIANTES}

    # T2 — trop beau, trop mauvais (bloque toutes les lectures)
    tr: list = []
    trop_beau = [_cmp(tr, f"moy({NOM_COURT[nom]}, V)", moyennes_V[nom], ">=", SEUIL_T2_TROP_BEAU)
                 for nom in NOMS_VARIANTES]
    tous_mauvais = all([_cmp(tr, f"moy({NOM_COURT[nom]}, V)", moyennes_V[nom], "<=", DEUX_ALPHA)
                        for nom in NOMS_VARIANTES])
    est_r3 = contrastes_c[libelle_contraste("R3", "V")]["moyenne"]
    r3_trop_grand = _cmp(tr, "est(R3, V)", est_r3, ">", SEUIL_T2_EST_R3)
    est_xbarre = {nom: contrastes_c[libelle_contraste(nom, "Xbarre")]["moyenne"] for nom in VARIANTES_CONTRASTEES}
    xbarre_grand = [_cmp(tr, f"|est({NOM_COURT[nom]}, Xbarre)|", abs(est_xbarre[nom]), ">", SEUIL_T2_EST_XBARRE)
                    for nom in VARIANTES_CONTRASTEES]
    marge2, proches2 = _marge_et_proches(tr)
    t2 = {"declenche": bool(any(trop_beau) or tous_mauvais or r3_trop_grand or any(xbarre_grand)),
          "une_variante_moy_V_ge_0_99": bool(any(trop_beau)),
          "cinq_variantes_moy_V_le_0_02": bool(tous_mauvais),
          "est_R3_V_gt_0_30": bool(r3_trop_grand),
          "un_abs_est_Xbarre_gt_0_30": bool(any(xbarre_grand)),
          "est_R3_V": est_r3,
          "abs_est_Xbarre": {NOM_COURT[nom]: abs(v) for nom, v in est_xbarre.items()},
          "marge_min_au_seuil": marge2, "comparaisons_a_la_frontiere": proches2}

    # T3 — mélange dégénéré (bloque HR1)
    plus_grands = [max(w) for w in donnees["poids_R3"]]
    nb_pur = sum(1 for g in plus_grands if g >= SEUIL_T3_POIDS_PUR)
    t3 = {"declenche": bool(nb_pur > SEUIL_T3_NB), "nb_taches_poids_pur": nb_pur, "seuil_nb": SEUIL_T3_NB,
          "plus_grand_poids_maximal": max(plus_grands),
          "nb_taches_a_la_frontiere": sum(1 for g in plus_grands if abs(g - SEUIL_T3_POIDS_PUR) <= EPS)}

    # T4 — régularisation dégénérée, S12 (bloque HR3 seulement)
    cos_moyens = [sum(v) / 8 for v in donnees["cos_R4"]]
    nb_cos = sum(1 for g in cos_moyens if g >= SEUIL_T4_COS)
    t4 = {"declenche": bool(nb_cos > SEUIL_T4_NB), "nb_taches_cos_moyen_ge_0_999": nb_cos, "seuil_nb": SEUIL_T4_NB,
          "nb_taches_a_la_frontiere": sum(1 for g in cos_moyens if abs(g - SEUIL_T4_COS) <= EPS)}

    # T5 — optimiseur (bloque toutes les lectures)
    tr5: list = []
    std_moins_ren = {nom: moy(nom, "V_iii_standard") - moy(nom, "V_iii_renforce") for nom in NOMS_VARIANTES}
    partie1 = [_cmp(tr5, f"moy_standard−moy_renforcé({NOM_COURT[nom]})", std_moins_ren[nom], ">", SEUIL_T5)
               for nom in NOMS_VARIANTES]
    ecart_contraste = {}
    partie2 = []
    for nom in VARIANTES_CONTRASTEES:
        a = float(np.mean(ch[nom]["V_iii_standard"] - ch["R2"]["V_iii_standard"]))
        b = float(np.mean(ch[nom]["V_iii_renforce"] - ch["R2"]["V_iii_renforce"]))
        ecart_contraste[NOM_COURT[nom]] = {"a_standard": a, "b_renforce": b, "a_moins_b": a - b}
        partie2.append(_cmp(tr5, f"|a−b|({NOM_COURT[nom]})", abs(a - b), ">", SEUIL_T5))
    marge5, proches5 = _marge_et_proches(tr5)
    t5 = {"declenche": bool(any(partie1) or any(partie2)),
          "standard_moins_renforce": {NOM_COURT[n_]: v for n_, v in std_moins_ren.items()},
          "plus_grand_standard_moins_renforce": max(std_moins_ren.values()),
          "ecart_de_contraste": ecart_contraste,
          "plus_grand_abs_ecart_de_contraste": max(abs(v["a_moins_b"]) for v in ecart_contraste.values()),
          "marge_min_au_seuil": marge5, "comparaisons_a_la_frontiere": proches5}

    # T6 — dérive des fausses alertes (bloque toutes les lectures)
    tr6: list = []
    ecarts_alpha = {nom: moy(nom, "fpr_final") - ALPHA for nom in NOMS_VARIANTES}
    deriv = [_cmp(tr6, f"|moy_fpr({NOM_COURT[nom]}) − α|", abs(ecarts_alpha[nom]), ">", SEUIL_T6)
             for nom in NOMS_VARIANTES]
    marge6, proches6 = _marge_et_proches(tr6)
    t6 = {"declenche": bool(any(deriv)),
          "moyenne_fpr_final": {NOM_COURT[nom]: moy(nom, "fpr_final") for nom in NOMS_VARIANTES},
          "plus_grand_abs_ecart_a_alpha": max(abs(v) for v in ecarts_alpha.values()),
          "marge_min_au_seuil": marge6, "comparaisons_a_la_frontiere": proches6}

    return {"moyennes_V": moyennes_V, "jeu_degenere": bool(tous_mauvais),
            "T2": t2, "T3": t3, "T4": t4, "T5": t5, "T6": t6, "garde_coherence_V": "ok"}


def etat_global_sante(sante: dict) -> dict:
    """Un contrôle est déclenché s'il l'est dans au moins un des deux budgets (voir le rapport :
    lecture retenue pour « T2, T3, T5 ou T6 déclenché »)."""
    return {t: bool(any(sante[str(c)][t]["declenche"] for c in BUDGETS)) for t in ("T2", "T3", "T4", "T5", "T6")}


# ============================================================================================
# § 9 — verdicts de la course originale (pour la validation)
# ============================================================================================
def _agrege(ligne: int, verdict: str, trace: list, classes_liees=()) -> dict:
    marge, proches = _marge_et_proches(trace)
    frontiere = bool(proches) or any(c["frontiere"] for c in classes_liees)
    return {"ligne": ligne, "verdict": verdict, "frontiere": frontiere,
            "marge_min_au_seuil": marge, "comparaisons_a_la_frontiere": proches}


def verdicts_regles_originales(classes: dict, etat: dict) -> dict:
    """HR1, HR0, HR3, HR2 selon le § 9 (contrôles T2, T3, T5, T6 supposés non déclenchés)."""
    a = classes["table_A"]
    hr1 = {"ligne": a["ligne"], "verdict": a["classe"], "frontiere": a["frontiere"]}

    cl0 = classes["table_B"]["R0"]
    lib0 = [cl0[str(c)]["classe"] for c in BUDGETS]
    if all(x == "R2 > R0" for x in lib0):
        v0 = O_CONFIRMEE
    elif any(x in ("R0 > R2", "R0 ≳ R2", EQUIVALENT) for x in lib0):
        v0 = O_REFUTEE
    else:
        v0 = O_NON_TRANCHEE
    hr0 = {"verdict": v0, "classes": lib0, "frontiere": any(cl0[str(c)]["frontiere"] for c in BUDGETS)}

    cl4 = classes["table_B"]["R4"]
    lib4 = [cl4[str(c)]["classe"] for c in BUDGETS]
    if etat["T4"]:
        v3 = V_HR3_SANS_VERDICT
    elif all(x in ("R4 > R2", "R4 ≳ R2", EQUIVALENT) for x in lib4):
        v3 = O_CONFIRMEE
    elif any(x == "R2 > R4" for x in lib4):
        v3 = O_REFUTEE
    else:
        v3 = O_NON_TRANCHEE
    hr3 = {"verdict": v3, "classes": lib4, "T4_dans_au_moins_un_budget": bool(etat["T4"]),
           "frontiere": any(cl4[str(c)]["frontiere"] for c in BUDGETS)}

    cl1 = classes["table_Bprime"]["R1"]
    lib1 = [cl1[str(c)]["classe"] for c in BUDGETS]
    if all(x == "R2 > R1" for x in lib1):
        v2 = O_CONFIRMEE
    elif any(x in ("R1 > R2", "R1 ≳ R2", EQUIVALENT) for x in lib1):
        v2 = O_REFUTEE
    else:
        v2 = O_NON_TRANCHEE
    hr2 = {"verdict": v2, "classes": lib1, "frontiere": any(cl1[str(c)]["frontiere"] for c in BUDGETS)}
    return {"HR1": hr1, "HR0": hr0, "HR3": hr3, "HR2": hr2,
            "hypothese": "contrôles T2, T3, T5, T6 supposés non déclenchés (§ 9)",
            "T2_T3_T5_T6_effectivement_non_declenches": not any(etat[t] for t in ("T2", "T3", "T5", "T6"))}


# ============================================================================================
# § 10.1 — verdicts bruts de la réplication
# ============================================================================================
def verdict_HR1_replication(etat: dict, par_budget: dict, jeu_degenere: dict) -> dict:
    """par_budget[c] = {"est", "bas_B2", "haut_B2"} du contraste (R3, V) ; jeu_degenere[c] : bool."""
    trace: list = []
    if etat["T2"] or etat["T3"] or etat["T5"] or etat["T6"]:
        return _agrege(1, V_SANTE, trace)
    if any(jeu_degenere[c] for c in BUDGETS):
        return _agrege(2, V_DEGENERE, trace)
    ok3 = {}
    for c in BUDGETS:
        a = _cmp(trace, f"est_{c}", par_budget[c]["est"], ">=", TAU)
        b = _cmp(trace, f"bas(B2)_{c}", par_budget[c]["bas_B2"], ">", 0.0)
        ok3[c] = a and b
    if ok3[1] and ok3[2]:
        return _agrege(3, V_REPLIQUEE, trace)
    if any([_cmp(trace, f"haut(B2)_{c}", par_budget[c]["haut_B2"], "<", 0.0) for c in BUDGETS]):
        return _agrege(4, V_HR1_SIGNE, trace)
    if any([_cmp(trace, f"haut(B2)_{c}", par_budget[c]["haut_B2"], "<", TAU) for c in BUDGETS]):
        return _agrege(5, V_HR1_PETIT, trace)
    return _agrege(6, V_IMPRECIS, trace)


def verdict_HR0_replication(etat: dict, kappa: dict, classes_liees=()) -> dict:
    """kappa[c] = classe de (R0, V) par la table B, au budget c."""
    k = [kappa[c] for c in BUDGETS]
    if etat["T2"] or etat["T5"] or etat["T6"]:
        return _agrege(1, V_SANTE, [], classes_liees)
    if any(x == "R2 > R0" for x in k):
        return _agrege(2, V_HR0_INTERET, [], classes_liees)
    if any(x == "R2 ≳ R0" for x in k):
        return _agrege(3, V_HR0_NON_NUL, [], classes_liees)
    if all(x in (EQUIVALENT, "R0 ≳ R2", "R0 > R2") for x in k):
        return _agrege(4, V_REPLIQUEE, [], classes_liees)
    return _agrege(5, V_IMPRECIS, [], classes_liees)


def verdict_HR3_replication(etat: dict, kappa: dict, classes_liees=()) -> dict:
    """kappa[c] = classe de (R4, V) par la table B, au budget c."""
    k = [kappa[c] for c in BUDGETS]
    if etat["T2"] or etat["T5"] or etat["T6"]:
        return _agrege(1, V_SANTE, [], classes_liees)
    if etat["T4"]:
        return _agrege(2, V_HR3_SANS_VERDICT, [], classes_liees)
    if any(x in ("R2 > R4", "R2 ≳ R4") for x in k):
        return _agrege(3, V_NON_REPLIQUEE, [], classes_liees)
    if all(x in ("R4 > R2", "R4 ≳ R2", EQUIVALENT) for x in k):
        return _agrege(4, V_REPLIQUEE, [], classes_liees)
    return _agrege(5, V_IMPRECIS, [], classes_liees)


def verdict_ii_replication(etat: dict, lignes_C: dict, classes_liees=()) -> dict:
    """lignes_C[c] = numéro de ligne de la table C pour (R0, (ii)) au budget c."""
    lg = [lignes_C[c] for c in BUDGETS]
    if etat["T2"] or etat["T5"] or etat["T6"]:
        return _agrege(1, V_SANTE, [], classes_liees)
    if all(x == 4 for x in lg):
        return _agrege(2, V_REPLIQUEE, [], classes_liees)
    if any(x in (1, 2, 3) for x in lg):
        return _agrege(3, V_HR1_SIGNE, [], classes_liees)
    return _agrege(4, V_IMPRECIS, [], classes_liees)


def verdicts_bruts_replication(classes: dict, contrastes: dict, sante: dict, etat: dict) -> dict:
    """Les cinq lignes du § 10.1 (HR1, HR0, HR3, lois tenues à l'écart (ii), HR2 recopié)."""
    par_budget = {}
    for c in BUDGETS:
        stat = contrastes[str(c)][libelle_contraste("R3", "V")]
        bas, haut = bornes_depuis_statistique(stat)["B2"]
        par_budget[c] = {"est": stat["moyenne"], "bas_B2": bas, "haut_B2": haut}
    jeu = {c: bool(sante[str(c)]["jeu_degenere"]) for c in BUDGETS}
    hr1 = verdict_HR1_replication(etat, par_budget, jeu)
    cl0, cl4, clC = classes["table_B"]["R0"], classes["table_B"]["R4"], classes["table_C"]["R0"]
    hr0 = verdict_HR0_replication(etat, {c: cl0[str(c)]["classe"] for c in BUDGETS}, list(cl0.values()))
    hr3 = verdict_HR3_replication(etat, {c: cl4[str(c)]["classe"] for c in BUDGETS}, list(cl4.values()))
    iii = verdict_ii_replication(etat, {c: clC[str(c)]["ligne"] for c in BUDGETS}, list(clC.values()))
    originaux = verdicts_regles_originales(classes, etat)
    return {"HR1": hr1, "HR0": hr0, "HR3": hr3, "lois_tenues_ii": iii,
            "HR2": {"verdict": originaux["HR2"]["verdict"], "classes": originaux["HR2"]["classes"],
                    "note": "recopié du § 9, sans verdict de réplication"},
            "kappa_R0_V": {str(c): cl0[str(c)]["classe"] for c in BUDGETS},
            "kappa_prime_R4_V": {str(c): cl4[str(c)]["classe"] for c in BUDGETS},
            "lignes_C_R0_ii": {str(c): clC[str(c)]["ligne"] for c in BUDGETS}}


# ============================================================================================
# § 10.2 — écart de réplication et déclencheurs d'audit symétriques
# ============================================================================================
def sigma_pi(s_rep: float, s_or: float) -> float:
    return math.sqrt(s_rep ** 2 / 100 + s_or ** 2 / 100)


def ecart_replication(contrastes_rep: dict, analyse_originale: dict) -> dict:
    """g, sigma, z des quatre contrastes primaires. `analyse_originale` : analyse de E4."""
    sortie = {}
    for nom, mes, c in PRIMAIRES:
        lib = libelle_contraste(nom, mes)
        rep = contrastes_rep[str(c)][lib]
        try:
            ori = analyse_originale["resultat"][str(c)]["contrastes_contre_R2"][lib]
            est_or, s_or = float(ori["moyenne"]), float(ori["ecart_type"])
        except (KeyError, TypeError) as e:
            raise Arret(f"analyse originale : contraste « {lib} » du budget {c} introuvable ({e})") from None
        g = rep["moyenne"] - est_or
        sigma = sigma_pi(rep["ecart_type"], s_or)
        z = (g / sigma) if sigma > 0 else None
        sortie[f"({NOM_COURT[nom]}, {mes}, c={c})"] = {
            "libelle": lib, "budget": c, "est_rep": rep["moyenne"], "s_rep": rep["ecart_type"],
            "est_or": est_or, "s_or": s_or, "g": g, "sigma": sigma, "z": z}
    return sortie


def declencheurs_audit(ecarts: dict, kappa_R0_V: dict, verdicts_bruts: dict) -> dict:
    tr1 = any(abs(e["g"]) > Z_ETOILE * e["sigma"] for e in ecarts.values())
    tr2 = all(abs(e["g"]) < SEUIL_TR2 for e in ecarts.values())
    tr3 = any(kappa_R0_V[str(c)] in ("R0 > R2", "R0 ≳ R2") for c in BUDGETS)
    tr4 = (verdicts_bruts["HR1"]["verdict"].startswith("non répliquée")
           or verdicts_bruts["HR0"]["verdict"].startswith("non répliquée"))
    return {"TR1_ecart_de_replication": bool(tr1), "TR2_trop_propre": bool(tr2),
            "TR3_defense_figee_plus_belle": bool(tr3), "TR4_non_replication": bool(tr4),
            "au_moins_un": bool(tr1 or tr2 or tr3 or tr4)}


def verdicts_apres_declencheurs(verdicts_bruts: dict, declencheurs: dict) -> dict:
    """Effet des déclencheurs : s'il y en a au moins un, HR1, HR0, HR3 et (ii) deviennent
    « non jugeable (audit en attente) » (HR2 n'a pas de verdict de réplication)."""
    clefs = ("HR1", "HR0", "HR3", "lois_tenues_ii")
    if declencheurs["au_moins_un"]:
        return {k: V_AUDIT_ATTENTE for k in clefs}
    return {k: verdicts_bruts[k]["verdict"] for k in clefs}


# ============================================================================================
# § 10.3 — contrôle « graines neuves »
# ============================================================================================
def comptes_graines_neuves(donnees_rep: dict, donnees_orig: dict) -> dict:
    """Pour chaque variante, nombre de tâches (c, i) où V_iii_final est égal au bit à celui de la course
    originale à la même tâche. donnees_*[c] : sorties de extraire_donnees."""
    comptes = {}
    for nom in NOMS_VARIANTES:
        total = 0
        for c in BUDGETS:
            a = np.ascontiguousarray(donnees_rep[c]["champs"][nom]["V_iii_final"]).view(np.uint64)
            b = np.ascontiguousarray(donnees_orig[c]["champs"][nom]["V_iii_final"]).view(np.uint64)
            total += int(np.count_nonzero(a == b))
        comptes[NOM_COURT[nom]] = total
    return comptes


# ============================================================================================
# § 10.4 — issue globale
# ============================================================================================
def issue_globale(hr1: str, hr0: str, *, plomberie_fausse: bool = False, arret: bool = False,
                  discordance_ab: bool = False) -> dict:
    """Première ligne vraie du § 10.4. hr1 et hr0 : textes des verdicts (bruts ou après effet des
    déclencheurs)."""
    if plomberie_fausse or arret or discordance_ab:
        ligne = 1
    elif hr1 == V_AUDIT_ATTENTE or hr0 == V_AUDIT_ATTENTE:
        ligne = 2
    elif hr1 == V_ARTEFACT or hr0 == V_ARTEFACT:
        ligne = 3
    elif hr1.startswith("non répliquée"):
        ligne = 4
    elif hr1 == V_REPLIQUEE and hr0 == V_REPLIQUEE:
        ligne = 5
    elif hr1 == V_REPLIQUEE and hr0.startswith("non répliquée"):
        ligne = 6
    elif hr1 == V_REPLIQUEE and hr0.startswith("non jugeable"):
        ligne = 7
    else:
        ligne = 8
    return {"ligne": ligne, "issue": ISSUES[ligne]}


# ============================================================================================
# Analyse complète d'un fichier E1
# ============================================================================================
def analyser_donnees(e1, rho: int, *, e4_analyse=None, e4_resultats=None, plomberie_fausse=False,
                     discordance_ab=False) -> dict:
    """Cœur de l'analyse : E1 déjà lu ; rho = racine de rééchantillonnage ; E4 optionnel (analyse et résultats
    de la course originale, déjà lus et vérifiés). Rend un dictionnaire JSON-compatible (sans la partie
    « fichiers lus » ni « meta », ajoutées par l'appelant)."""
    avertissements: list = []
    taches = valider_forme_E1(e1)
    par_budget = selectionner_taches(taches, avertissements)
    donnees = {c: extraire_donnees(par_budget[c], c) for c in BUDGETS}

    contrastes = {str(c): calculer_contrastes_budget(donnees[c], c, rho) for c in BUDGETS}
    intervalles = {str(c): {lib: {k: [float(x) for x in v] for k, v in bornes_depuis_statistique(st).items()}
                            for lib, st in contrastes[str(c)].items()} for c in BUDGETS}
    sante = {str(c): controles_sante_budget(donnees[c], contrastes[str(c)]) for c in BUDGETS}
    etat = etat_global_sante(sante)
    classes = classes_depuis_contrastes(contrastes, {str(c): sante[str(c)]["moyennes_V"] for c in BUDGETS})

    sortie = {
        "resultat": {str(c): {"contrastes_contre_R2": contrastes[str(c)]} for c in BUDGETS},
        "intervalles": intervalles,
        "sante": {**sante, "etat_global": etat},
        "classes": classes,
        "verdicts_regles_originales": verdicts_regles_originales(classes, etat),
        "verdicts_bruts_replication": verdicts_bruts_replication(classes, contrastes, sante, etat),
        "ecart_de_replication": None, "declencheurs_audit": None, "comptes_graines_neuves": None,
        "verdicts_apres_declencheurs": None, "issue_globale_brute": None,
        "issue_globale_apres_declencheurs": None, "arrets": [], "lecture_autorisee": True,
        "avertissements": avertissements,
    }
    sortie["classes_a_la_frontiere"] = _lister_frontieres(classes)

    vb = sortie["verdicts_bruts_replication"]
    arret = False
    if e4_analyse is not None:
        ecarts = ecart_replication(contrastes, e4_analyse)
        decl = declencheurs_audit(ecarts, vb["kappa_R0_V"], vb)
        va = verdicts_apres_declencheurs(vb, decl)
        sortie["ecart_de_replication"] = {"constantes": {"z_etoile": Z_ETOILE, "seuil_TR2": SEUIL_TR2},
                                          "contrastes_primaires": ecarts}
        sortie["declencheurs_audit"] = decl
        sortie["verdicts_apres_declencheurs"] = va
    if e4_resultats is not None:
        taches_or = selectionner_taches(valider_forme_E1(e4_resultats))
        donnees_or = {c: extraire_donnees(taches_or[c], c) for c in BUDGETS}
        comptes = comptes_graines_neuves(donnees, donnees_or)
        non_neuves = [v for v, n_ in comptes.items() if n_ > SEUIL_GRAINES_NEUVES]
        sortie["comptes_graines_neuves"] = {"comptes": comptes, "seuil": SEUIL_GRAINES_NEUVES,
                                            "variantes_au_dessus_du_seuil": non_neuves,
                                            "arret_graines_non_neuves": bool(non_neuves)}
        if non_neuves:
            sortie["arrets"].append("graines non neuves : " + ", ".join(f"{v}={comptes[v]}" for v in non_neuves))
            arret = True
    if e4_analyse is not None and e4_resultats is not None:
        sortie["issue_globale_brute"] = issue_globale(
            vb["HR1"]["verdict"], vb["HR0"]["verdict"], plomberie_fausse=plomberie_fausse, arret=arret,
            discordance_ab=discordance_ab)
        sortie["issue_globale_apres_declencheurs"] = issue_globale(
            sortie["verdicts_apres_declencheurs"]["HR1"], sortie["verdicts_apres_declencheurs"]["HR0"],
            plomberie_fausse=plomberie_fausse, arret=arret, discordance_ab=discordance_ab)
        sortie["indicateurs_externes"] = {"plomberie_fausse_V0": bool(plomberie_fausse),
                                          "discordance_A_B": bool(discordance_ab)}
    sortie["lecture_autorisee"] = not sortie["arrets"]
    sortie["racines_lues_dans_E1"] = {
        "racine": sorted({t["racine"] for t in taches}), "racine_tenue": sorted({t["racine_tenue"] for t in taches})}
    return sortie


def _lister_frontieres(classes: dict) -> list:
    out = []
    if classes["table_A"]["frontiere"]:
        out.append("table_A")
    for table in ("table_B", "table_Bprime", "table_C"):
        for court, par_c in classes[table].items():
            for c, cl in par_c.items():
                if cl["frontiere"]:
                    out.append(f"{table}/{court}/budget {c}")
    return out


# ============================================================================================
# Sortie JSON neuve (jamais écrasée) et analyse « de bout en bout » depuis les fichiers
# ============================================================================================
def ecrire_json_neuf(chemin, objet) -> str:
    """Écrit un fichier JSON neuf (création exclusive : jamais écrasé). Rend son empreinte."""
    chemin = Path(chemin)
    texte = json.dumps(objet, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    try:
        with open(chemin, "x", encoding="utf-8", newline="\n") as f:
            f.write(texte)
    except FileExistsError:
        raise FileExistsError(f"{chemin} existe déjà : une nouvelle version porte un nouveau nom") from None
    return empreinte_octets(texte.encode("utf-8"))


def analyser_fichiers(*, resultats, racine: int | None = None, prereg=None, manifeste=None,
                      analyse_originale=None, resultats_originaux=None, empreinte_attendue_E1=None,
                      plomberie_fausse=False, discordance_ab=False) -> dict:
    """Lit et vérifie les fichiers (§ 3), dérive ou impose la racine, puis analyse. Deux modes :
    - réplication : `prereg` + `manifeste` (+ E4 obligatoire) ; racines par la règle D ;
    - racine imposée : `racine` ; E4 facultatif (essai « contre elle-même » de la course originale)."""
    t0 = time.perf_counter()
    avertissements: list = []
    fichiers: list = []

    def noter(role, chemin, sha):
        fichiers.append({"role": role, "fichier": Path(chemin).name, "sha256": sha})

    if (prereg is None) != (manifeste is None):
        raise Arret("mode réplication : `prereg` et `manifeste` vont ensemble")
    if prereg is not None and racine is not None:
        raise Arret("racine imposée et règle D sont exclusives")
    if prereg is None and racine is None:
        raise Arret("il faut soit (prereg, manifeste), soit une racine imposée")
    if prereg is not None and (analyse_originale is None or resultats_originaux is None):
        raise Arret("mode réplication : E4 (analyse et résultats originaux) est obligatoire")

    # E1
    octets_e1, sha_e1 = _lire_E1(resultats, empreinte_attendue_E1, avertissements)
    noter("E1 résultats analysés", resultats, sha_e1)
    e1 = lire_json_octets(octets_e1, "E1")

    # E4
    e4_analyse = e4_resultats = None
    if analyse_originale is not None:
        o, sha = lire_fichier_verifie(analyse_originale, "E4 analyse originale", attendue=EMPREINTE_ANALYSE_ORIGINALE)
        e4_analyse = lire_json_octets(o, "E4 analyse originale")
        noter("E4 analyse originale", analyse_originale, sha)
    if resultats_originaux is not None:
        o, sha = lire_fichier_verifie(resultats_originaux, "E4 résultats originaux",
                                      attendue=EMPREINTE_RESULTATS_ORIGINAUX)
        e4_resultats = lire_json_octets(o, "E4 résultats originaux")
        noter("E4 résultats originaux", resultats_originaux, sha)

    # racines
    info_racines: dict
    if prereg is not None:
        octets_e3, sha_e3 = lire_fichier_verifie(prereg, "E3 préenregistrement", avertissements=avertissements)
        noter("E3 préenregistrement scellé", prereg, sha_e3)
        octets_e2, sha_e2 = lire_fichier_verifie(manifeste, "E2 manifeste", avertissements=avertissements)
        noter("E2 manifeste du run", manifeste, sha_e2)
        e2 = lire_json_octets(octets_e2, "E2")
        h, rho, rho_t = regle_d_depuis_octets(octets_e3)
        info_racines = _controle_coherence_racines(e2, e1, h, rho, rho_t, avertissements)
        h_texte = h
    else:
        rho, rho_t, h_texte = int(racine), None, None
        info_racines = {"origine": "racine imposée", "rho": str(rho), "rho_t": None}

    sortie = analyser_donnees(e1, rho, e4_analyse=e4_analyse, e4_resultats=e4_resultats,
                              plomberie_fausse=plomberie_fausse, discordance_ab=discordance_ab)
    entete = {
        "implementation": f"implementation_b.py ({VERSION_IMPLEMENTATION})",
        "specification": "specification-statistique-decisive-v1.md",
        "mode": "réplication (règle D)" if prereg is not None else "racine imposée",
        "empreinte_H": h_texte,
        "racines": info_racines,
        "racine_de_reechantillonnage": str(rho),
    }
    sortie = {**entete, **sortie, "empreintes_fichiers": fichiers,
              "avertissements": avertissements + sortie["avertissements"],
              "meta_non_deterministe": {"python": platform.python_version(), "numpy": np.__version__,
                                        "duree_calcul_s": round(time.perf_counter() - t0, 3)}}
    return sortie


def _lire_E1(chemin, empreinte_attendue, avertissements):
    """E1 : empreinte imposée en ligne de commande, sinon compagnon ; à défaut de compagnon, accepté seulement
    si c'est exactement le fichier de résultats originaux (empreinte E4 connue de la spécification)."""
    if empreinte_attendue is not None:
        return lire_fichier_verifie(chemin, "E1", attendue=empreinte_attendue, avertissements=avertissements)
    try:
        return lire_fichier_verifie(chemin, "E1", avertissements=avertissements)
    except Arret as e:
        if "aucun fichier compagnon" not in str(e):
            raise
        try:
            octets, sha = lire_fichier_verifie(chemin, "E1", attendue=EMPREINTE_RESULTATS_ORIGINAUX)
        except Arret:
            raise Arret("E1 : ni fichier compagnon <nom>.sha256, ni empreinte imposée, et ce n'est pas le fichier "
                        "des résultats originaux : empreinte non vérifiable") from None
        avertissements.append("E1 : pas de fichier compagnon ; accepté car c'est le fichier des résultats "
                              "originaux (empreinte E4 de la spécification)")
        return octets, sha


def _controle_coherence_racines(e2, e1, h, rho, rho_t, avertissements) -> dict:
    """§ 3 (E3 contre E2) et § 4 (contrôle de cohérence des racines)."""
    try:
        cfg = e2["config"]
        sha_manifeste = e2["preenregistrement"]["sha256"]
        racine_m, racine_tenue_m = cfg["racine"], cfg["racine_tenue"]
    except (KeyError, TypeError) as e:
        raise Arret(f"E2 : champ attendu absent ({e})") from None
    if sha_manifeste != h:
        raise Arret("E2 : preenregistrement.sha256 ≠ H recalculé du texte scellé")
    if cfg.get("prereg_sha256") != h:
        avertissements.append("E2 : config.prereg_sha256 ≠ H recalculé (non prescrit comme arrêt par la spécification)")
    if _entier(racine_m, "E2 config.racine") != rho or _entier(racine_tenue_m, "E2 config.racine_tenue") != rho_t:
        raise Arret("E2 : (config.racine, config.racine_tenue) ≠ (rho, rho_t) de la règle D")
    for i, t in enumerate(e1["resultat"]["resultats"]):
        if t.get("racine") != rho or t.get("racine_tenue") != rho_t:
            raise Arret(f"E1 : tâche {i} : (racine, racine_tenue) ≠ (rho, rho_t) de la règle D")
    # champs de E2 lus mais sans contrôle prescrit : consignés et confrontés à E1 en simple avertissement
    lam, ref = cfg.get("lambda"), cfg.get("reference")
    n_inst = cfg.get("config", {}).get("n_instances") if isinstance(cfg.get("config"), dict) else None
    vus = {(t["regles"][NOMS_VARIANTES[4]].get("lam"), t["regles"][NOMS_VARIANTES[4]].get("reference"))
           for t in e1["resultat"]["resultats"]}
    if vus != {(lam, ref)}:
        avertissements.append(f"E2 : (lambda, reference) = ({lam!r}, {ref!r}) ≠ valeurs de R4 dans E1 : {sorted(map(repr, vus))}")
    if n_inst != N:
        avertissements.append(f"E2 : config.config.n_instances = {n_inst!r} ≠ {N}")
    return {"origine": "règle D", "rho": str(rho), "rho_t": str(rho_t),
            "controle_coherence": "racines de E2 et des 200 tâches de E1 égales à (rho, rho_t)",
            "E2_lambda": lam, "E2_reference": ref, "E2_n_instances": n_inst}


# ============================================================================================
# § 11 — comparaison avec l'implémentation de référence A
# ============================================================================================
def lire_contrastes_A(analyse_a: dict) -> dict:
    """Contrastes d'une analyse de référence : {"1": {libellé: stat}, "2": {...}} (16 libellés par budget)."""
    sortie = {}
    for c in BUDGETS:
        try:
            tous = analyse_a["resultat"][str(c)]["contrastes_contre_R2"]
        except (KeyError, TypeError) as e:
            raise Arret(f"analyse de référence : contrastes du budget {c} absents ({e})") from None
        sortie[str(c)] = {libelle_contraste(nom, mes): tous.get(libelle_contraste(nom, mes))
                          for nom, mes in TOUS_LES_CONTRASTES}
    return sortie


def comparer_contrastes(contrastes_b: dict, contrastes_a: dict) -> dict:
    """Écarts absolus, contraste par contraste (§ 11). `niveau` : « arrêt » pour les cinq contrastes de la
    concordance exigée (par budget), « alerte » pour les onze autres."""
    detail = {}
    for c in BUDGETS:
        detail[str(c)] = {}
        for nom, mes in TOUS_LES_CONTRASTES:
            lib = libelle_contraste(nom, mes)
            sb, sa = contrastes_b[str(c)][lib], contrastes_a[str(c)][lib]
            niveau = "arrêt" if (nom, mes) in CONTRASTES_A_ARRET else "alerte"
            if sa is None:
                detail[str(c)][lib] = {"niveau": niveau, "present_dans_A": False, "ok": False}
                continue
            e_moy = abs(sb["moyenne"] - sa["moyenne"])
            e_sd = abs(sb["ecart_type"] - sa["ecart_type"])
            e_q = {cle: abs(sb["quantiles"][cle] - sa["quantiles"][cle]) for cle in CLES_QUANTILES}
            e_max = max([e_moy, e_sd, *e_q.values()])
            n_ok = bool(sb["n"] == sa["n"])
            z_ok = bool(sb["zeros_exacts"] == sa["zeros_exacts"])
            detail[str(c)][lib] = {
                "niveau": niveau, "present_dans_A": True, "ecart_moyenne": e_moy, "ecart_ecart_type": e_sd,
                "ecart_quantiles": e_q, "ecart_quantiles_max": max(e_q.values()), "ecart_max_abs": e_max,
                "n_identique": n_ok, "zeros_exacts_identiques": z_ok, "ok": bool(e_max <= EPS and n_ok and z_ok)}
    return detail


def comparer_classes(classes_b: dict, classes_a: dict) -> dict:
    """Identité des lignes et des classes, table par table (§ 11) ; une différence sur une classe marquée
    « à la frontière » (de l'un ou de l'autre côté) est signalée à part."""
    diffs, frontieres = [], []

    def un(chemin, cb, ca):
        identique = cb["ligne"] == ca["ligne"] and cb["classe"] == ca["classe"]
        front = bool(cb["frontiere"] or ca["frontiere"])
        if front:
            frontieres.append(chemin)
        if not identique:
            diffs.append({"chemin": chemin, "B": [cb["ligne"], cb["classe"]], "A": [ca["ligne"], ca["classe"]],
                          "a_la_frontiere": front,
                          "classe_retenue_pour_la_lecture": [ca["ligne"], ca["classe"]] if front else None})

    un("table_A", classes_b["table_A"], classes_a["table_A"])
    nb = 1
    for table in ("table_B", "table_Bprime", "table_C"):
        for court, par_c in classes_b[table].items():
            for c in par_c:
                un(f"{table}/{court}/budget {c}", par_c[c], classes_a[table][court][c])
                nb += 1
    strictes = [d for d in diffs if not d["a_la_frontiere"]]
    return {"nombre_de_classes_comparees": nb, "differences": diffs, "differences_hors_frontiere": strictes,
            "classes_a_la_frontiere": frontieres, "identiques": not strictes}


def comparer_verdicts(v_b: dict, v_a: dict) -> dict:
    """Verdicts identiques, sauf s'ils reposent sur une classe marquée à la frontière (on retient alors celui de A)."""
    diffs = []
    for cle in ("HR1", "HR0", "HR3", "HR2"):
        if v_b[cle]["verdict"] != v_a[cle]["verdict"]:
            front = bool(v_b[cle].get("frontiere") or v_a[cle].get("frontiere"))
            diffs.append({"verdict": cle, "B": v_b[cle]["verdict"], "A": v_a[cle]["verdict"], "a_la_frontiere": front})
    strictes = [d for d in diffs if not d["a_la_frontiere"]]
    return {"identiques": not strictes, "differences": diffs, "differences_hors_frontiere": strictes}


def z_depuis_analyses(contrastes_rep: dict, analyse_originale: dict) -> dict:
    return {k: v["z"] for k, v in ecart_replication(contrastes_rep, analyse_originale).items()}


def comparer_a_reference(sortie_b: dict, analyse_a: dict, analyse_originale: dict | None = None) -> dict:
    """Compare une sortie de cette implémentation (format de `analyser_fichiers`) à une analyse de
    référence A (même format que l'analyse de la course originale). Les classes et verdicts de A sont
    calculés « à partir des nombres de A en appliquant le texte scellé » (§ 11), avec les contrôles de santé
    recalculés depuis E1 (ils ne dépendent pas de l'analyse)."""
    contrastes_b = {c: sortie_b["resultat"][c]["contrastes_contre_R2"] for c in ("1", "2")}
    contrastes_a = lire_contrastes_A(analyse_a)
    detail = comparer_contrastes(contrastes_b, contrastes_a)
    manquants = [lib for c in detail for lib, d in detail[c].items() if not d["present_dans_A"]]
    sortie = {"tolerance": EPS, "detail_par_contraste": detail, "contrastes_absents_de_A": manquants}
    presents = [d for c in detail for d in detail[c].values() if d["present_dans_A"]]
    arrets = [d for d in presents if d["niveau"] == "arrêt"]
    alertes = [d for d in presents if d["niveau"] == "alerte"]
    sortie["ecart_maximal_absolu"] = max((d["ecart_max_abs"] for d in presents), default=None)
    sortie["ecart_maximal_absolu_contrastes_a_arret"] = max((d["ecart_max_abs"] for d in arrets), default=None)
    sortie["ecart_maximal_absolu_contrastes_a_alerte"] = max((d["ecart_max_abs"] for d in alertes), default=None)
    sortie["discordance_a_arret"] = bool(manquants) or any(not d["ok"] for d in arrets)
    sortie["alertes_de_discordance"] = [lib for c in detail for lib, d in detail[c].items()
                                       if d["niveau"] == "alerte" and d["present_dans_A"] and not d["ok"]]
    moyennes_V = {c: sortie_b["sante"][c]["moyennes_V"] for c in ("1", "2")}
    if not manquants:
        classes_a = classes_depuis_contrastes(contrastes_a, moyennes_V)
        sortie["classes"] = comparer_classes(sortie_b["classes"], classes_a)
        etat = sortie_b["sante"]["etat_global"]
        v_a = verdicts_regles_originales(classes_a, etat)
        sortie["verdicts_regles_originales"] = comparer_verdicts(sortie_b["verdicts_regles_originales"], v_a)
        vb_a = verdicts_bruts_replication(classes_a, contrastes_a, sortie_b["sante"], etat)
        diffs = []
        for k in ("HR1", "HR0", "HR3", "lois_tenues_ii"):
            vb_b = sortie_b["verdicts_bruts_replication"][k]
            if vb_a[k]["verdict"] != vb_b["verdict"]:
                front = bool(vb_a[k].get("frontiere") or vb_b.get("frontiere"))
                diffs.append({"verdict": k, "B": vb_b["verdict"], "A": vb_a[k]["verdict"], "a_la_frontiere": front})
        strictes = [d for d in diffs if not d["a_la_frontiere"]]
        sortie["verdicts_bruts_replication"] = {"identiques": not strictes, "differences": diffs,
                                                "differences_hors_frontiere": strictes}
        if analyse_originale is not None:
            z_a = z_depuis_analyses(contrastes_a, analyse_originale)
            z_b = {k: v["z"] for k, v in
                   ecart_replication(contrastes_b, analyse_originale).items()}
            ecarts_z = {k: (abs(z_a[k] - z_b[k]) if z_a[k] is not None and z_b[k] is not None else
                            (0.0 if z_a[k] is None and z_b[k] is None else math.inf)) for k in z_a}
            sortie["z_pi"] = {"A": z_a, "B": z_b, "ecart_abs": ecarts_z,
                              "ok": all(v <= EPS for v in ecarts_z.values())}
    sortie["concordance"] = bool(
        not sortie["discordance_a_arret"]
        and sortie.get("classes", {}).get("identiques", False)
        and sortie.get("verdicts_regles_originales", {}).get("identiques", False)
        and sortie.get("verdicts_bruts_replication", {}).get("identiques", False)
        and sortie.get("z_pi", {"ok": True})["ok"])
    return sortie


# ============================================================================================
# Ligne de commande
# ============================================================================================
def _imprimer_json(objet) -> None:
    sys.stdout.write(json.dumps(objet, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def _cmd_analyser(a) -> int:
    sortie_chemin = Path(a.sortie)
    if sortie_chemin.exists():
        sys.stderr.write(f"ERREUR : {sortie_chemin} existe déjà (jamais écrasé ; nouvelle version = nouveau nom)\n")
        return 4
    try:
        res = analyser_fichiers(
            resultats=a.resultats, racine=a.racine, prereg=a.prereg, manifeste=a.manifeste,
            analyse_originale=a.analyse_originale, resultats_originaux=a.resultats_originaux,
            empreinte_attendue_E1=a.empreinte_attendue, plomberie_fausse=a.plomberie_fausse,
            discordance_ab=a.discordance_ab)
    except Arret as e:
        sys.stderr.write(f"ARRÊT : {e}\n")
        return 2
    sha = ecrire_json_neuf(sortie_chemin, res)
    sys.stderr.write(f"sortie écrite : {sortie_chemin} (sha256 {sha})\n")
    if res["arrets"]:
        sys.stderr.write("ARRÊT de la liste d'arrêt : " + " ; ".join(res["arrets"]) + " — lecture non autorisée\n")
        return 3
    return 0


def _cmd_regle_d(a) -> int:
    try:
        if a.prereg:
            octets, sha = lire_fichier_verifie(a.prereg, "E3 préenregistrement")
            h = sha
        else:
            h = a.empreinte
        rho, rho_t = regle_d_derivation(h)
        try:
            regle_d_gardes(rho, rho_t)
            gardes = "ok"
        except Arret as e:
            gardes = f"ARRÊT : {e}"
    except Arret as e:
        sys.stderr.write(f"ARRÊT : {e}\n")
        return 2
    _imprimer_json({"H": h, "E_decimal": str(int(h, 16)), "rho": str(rho), "rho_t": str(rho_t), "gardes": gardes})
    return 0 if gardes == "ok" else 2


def _cmd_comparer(a) -> int:
    try:
        sortie_b = json.loads(Path(a.sortie_b).read_text(encoding="utf-8"))
        if a.empreinte_attendue_a:
            octets_a, _ = lire_fichier_verifie(a.analyse_a, "A analyse de référence", attendue=a.empreinte_attendue_a)
        else:
            octets_a = Path(a.analyse_a).read_bytes()
        analyse_a = lire_json_octets(octets_a, "A")
        ori = None
        if a.analyse_originale:
            oo, _ = lire_fichier_verifie(a.analyse_originale, "E4 analyse originale",
                                         attendue=EMPREINTE_ANALYSE_ORIGINALE)
            ori = lire_json_octets(oo, "E4 analyse originale")
        res = comparer_a_reference(sortie_b, analyse_a, ori)
    except Arret as e:
        sys.stderr.write(f"ARRÊT : {e}\n")
        return 2
    if a.sortie:
        ecrire_json_neuf(a.sortie, res)
    else:
        _imprimer_json(res)
    return 0 if res["concordance"] else 3


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="implementation_b.py", description=__doc__.split("\n\n")[0])
    sp = ap.add_subparsers(dest="commande", required=True)

    an = sp.add_parser("analyser", help="analyse un fichier de résultats E1")
    an.add_argument("--resultats", required=True, help="fichier de résultats au format E1")
    an.add_argument("--empreinte-attendue", help="empreinte attendue de E1 (sinon fichier compagnon)")
    an.add_argument("--racine", type=int, help="racine de rééchantillonnage imposée (course originale : 20266201)")
    an.add_argument("--prereg", help="E3 : préenregistrement scellé (mode réplication, règle D)")
    an.add_argument("--manifeste", help="E2 : manifeste du run (mode réplication)")
    an.add_argument("--analyse-originale", help="E4 : analyse de la course originale")
    an.add_argument("--resultats-originaux", help="E4 : résultats de la course originale")
    an.add_argument("--plomberie-fausse", action="store_true", help="V0 de la réplication faux (entrée du § 10.4)")
    an.add_argument("--discordance-ab", action="store_true", help="discordance A/B constatée (entrée du § 10.4)")
    an.add_argument("--sortie", required=True, help="fichier JSON neuf (jamais écrasé)")
    an.set_defaults(fonction=_cmd_analyser)

    rd = sp.add_parser("regle-d", help="règle D (§ 4)")
    g = rd.add_mutually_exclusive_group(required=True)
    g.add_argument("--prereg", help="préenregistrement scellé (fichier compagnon .sha256 requis)")
    g.add_argument("--empreinte", help="empreinte H en 64 hexadécimaux minuscules")
    rd.set_defaults(fonction=_cmd_regle_d)

    cp = sp.add_parser("comparer", help="compare une sortie B à une analyse de référence A (§ 11)")
    cp.add_argument("--sortie-b", required=True)
    cp.add_argument("--analyse-a", required=True)
    cp.add_argument("--empreinte-attendue-a", help="empreinte attendue de l'analyse A")
    cp.add_argument("--analyse-originale", help="E4 : analyse originale (pour comparer les z)")
    cp.add_argument("--sortie", help="fichier JSON neuf ; sinon sortie standard")
    cp.set_defaults(fonction=_cmd_comparer)

    va = sp.add_parser("valider-originale", help="validation sur la course originale (§ 12)")
    va.add_argument("--dossier", default=str(Path(__file__).resolve().parent),
                    help="dossier contenant entrees/ (par défaut : celui du module)")
    va.add_argument("--dossier-sortie", help="dossier d'écriture (par défaut : --dossier)")
    va.set_defaults(fonction=_cmd_valider)

    a = ap.parse_args(argv)
    return a.fonction(a)


# ============================================================================================
# § 12 — validation obligatoire sur la course originale
# ============================================================================================
PREFIXE_EMPREINTE_SPECIFICATION = "2a1ad6d3"
NOM_SORTIE_B = "sortie-b-originale-v1.json"
NOM_VALIDATION_JSON = "validation-b-v1.json"
NOM_VALIDATION_MD = "validation-b-v1.md"

# Classes, contrôles et verdicts annoncés par le § 12 pour la course originale (budget 1, budget 2).
ATTENDU_12 = {
    "table_A": (2, A_CONFIRMEE),
    "table_B": {"R0": (EQUIVALENT, EQUIVALENT), "R1": ("R2 ≳ R1", INCERTAIN),
                "R3": ("R3 > R2", "R3 > R2"), "R4": ("R4 ≳ R2", "R4 ≳ R2")},
    "table_Bprime": {"R0": (EQUIVALENT, EQUIVALENT), "R1": ("R2 > R1", "R2 ≳ R1"),
                     "R3": ("R3 > R2", "R3 > R2"), "R4": ("R4 ≳ R2", "R4 ≳ R2")},
    "table_C": {"R0": (4, 4), "R1": (4, 4), "R3": (1, 1), "R4": (4, 4)},
    "T3_nb_taches_poids_pur": (0, 0),
    "T4_nb_taches": (5, 2),
    "T5_plus_grand_standard_moins_renforce_arrondi_5_decimales": 0.00039,
    "T5_plus_grand_ecart_de_contraste_arrondi_5_decimales": 0.00043,
    "T6_plus_grand_ecart_a_alpha_arrondi_5_decimales": 0.00019,
    "verdicts_9": {"HR1": A_CONFIRMEE, "HR0": O_REFUTEE, "HR3": O_CONFIRMEE, "HR2": O_NON_TRANCHEE},
}


def lire_table_12(texte: str) -> list:
    """Extrait du texte de la spécification le tableau de valeurs de contrôle du § 12 (dix lignes) :
    budget, variante, mesure, moyenne, écart-type, q(0,003125), q(0,00625), q(0,99375), q(0,996875)."""
    lignes = texte.split("\n")
    debut = next((i for i, ligne in enumerate(lignes) if ligne.startswith("## 12.")), None)
    if debut is None:
        raise Arret("spécification : section 12 introuvable")
    mesures = {"V": "V", "(ii)": "ii", "X̄": "Xbarre"}
    rangees = []
    for ligne in lignes[debut:]:
        if not ligne.startswith("|"):
            continue
        cellules = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(cellules) != 8 or cellules[0] not in ("1", "2"):
            continue
        m = re.fullmatch(r"(R\d) - R2, (V|\(ii\)|X̄)", cellules[1].replace("−", "-"))
        if m is None:
            raise Arret(f"spécification : ligne de contrôle illisible : {cellules[1]!r}")
        v = [float(x.replace("−", "-")) for x in cellules[2:]]
        nom = NOMS_VARIANTES[4] if m.group(1) == "R4" else m.group(1)
        rangees.append({"budget": int(cellules[0]), "variante": nom, "mesure": mesures[m.group(2)],
                        "moyenne": v[0], "ecart_type": v[1],
                        "q0.003125": v[2], "q0.00625": v[3], "q0.99375": v[4], "q0.996875": v[5]})
    return rangees


def _vecteurs_regle_d() -> dict:
    sortie = {"vecteurs": [], "gardes_rejettent_les_six_entiers": True}
    for h, rho_att, rho_t_att in VECTEURS_REGLE_D:
        rho, rho_t = regle_d_derivation(h)
        try:
            regle_d_gardes(rho, rho_t)
            rejete = False
        except Arret:
            rejete = True
        sortie["gardes_rejettent_les_six_entiers"] &= rejete
        sortie["vecteurs"].append({"H": h, "rho": str(rho), "rho_t": str(rho_t), "rho_attendu": str(rho_att),
                                   "rho_t_attendu": str(rho_t_att), "ok": (rho, rho_t) == (rho_att, rho_t_att),
                                   "gardes_rejettent_ce_vecteur": rejete})
    h0 = VECTEURS_REGLE_D[0][0]
    rho, rho_t = regle_d_derivation(h0)
    sortie["cas_sain"] = {"H_preenregistrement_original": h0, "rho": str(rho), "rho_t": str(rho_t),
                          "differe_de_20266201_20266202": (rho, rho_t) != (20266201, 20266202)}
    sortie["ok"] = (all(v["ok"] for v in sortie["vecteurs"]) and sortie["gardes_rejettent_les_six_entiers"]
                    and sortie["cas_sain"]["differe_de_20266201_20266202"])
    return sortie


def _vecteurs_generateur() -> dict:
    sortie = {"vecteurs": []}
    for v in VECTEURS_GENERATEUR:
        c, code = v["cle"][0], v["cle"][1]
        ind = indices_reechantillonnage(RACINE_COURSE_ORIGINALE, c, code)
        d10, f5 = [int(x) for x in ind[0, :10]], [int(x) for x in ind[-1, -5:]]
        sortie["vecteurs"].append({
            "racine": RACINE_COURSE_ORIGINALE, "cle": list(v["cle"]), "forme": list(ind.shape),
            "dtype": str(ind.dtype), "ligne0_dix_premiers": d10, "attendu": v["ligne0_dix_premiers"],
            "derniere_ligne_cinq_derniers": f5, "attendu_derniere": v["derniere_ligne_cinq_derniers"],
            "ok": d10 == v["ligne0_dix_premiers"] and f5 == v["derniere_ligne_cinq_derniers"]})
    sortie["ok"] = all(v["ok"] for v in sortie["vecteurs"])
    return sortie


def _table_12(res: dict, texte_spec: str) -> dict:
    rangees = lire_table_12(texte_spec)
    detail, ecart_max = [], 0.0
    for r in rangees:
        stat = res["resultat"][str(r["budget"])]["contrastes_contre_R2"][
            libelle_contraste(r["variante"] if r["variante"] != NOMS_VARIANTES[4] else NOMS_VARIANTES[4], r["mesure"])]
        e = {"moyenne": abs(stat["moyenne"] - r["moyenne"]), "ecart_type": abs(stat["ecart_type"] - r["ecart_type"])}
        for cle in ("q0.003125", "q0.00625", "q0.99375", "q0.996875"):
            e[cle] = abs(stat["quantiles"][cle] - r[cle])
        m = max(e.values())
        ecart_max = max(ecart_max, m)
        detail.append({"budget": r["budget"], "contraste": libelle_contraste(r["variante"], r["mesure"]),
                       "ecarts": e, "ecart_max_abs": m, "ok": m <= EPS})
    return {"nombre_de_lignes_lues": len(rangees), "lignes": detail, "ecart_maximal_absolu": ecart_max,
            "ok": len(rangees) == 10 and all(d["ok"] for d in detail)}


def _attendus_12(res: dict) -> dict:
    """Confronte classes, contrôles, verdicts et auto-essai de la sortie aux valeurs écrites dans le § 12."""
    cl, sa = res["classes"], res["sante"]
    t = {}
    a = cl["table_A"]
    t["table_A"] = {"obtenu": [a["ligne"], a["classe"]], "attendu": list(ATTENDU_12["table_A"]),
                    "ok": (a["ligne"], a["classe"]) == ATTENDU_12["table_A"]}
    for table, cle_obt in (("table_B", "classe"), ("table_Bprime", "classe"), ("table_C", "ligne")):
        t[table] = {}
        for court, att in ATTENDU_12[table].items():
            obt = tuple(cl[table][court][str(c)][cle_obt] for c in BUDGETS)
            t[table][court] = {"obtenu": list(obt), "attendu": list(att), "ok": obt == att}
    ctrl = {
        "T2_non_declenche": not res["sante"]["etat_global"]["T2"],
        "T3_non_declenche": not res["sante"]["etat_global"]["T3"],
        "T3_nb_taches": [sa[str(c)]["T3"]["nb_taches_poids_pur"] for c in BUDGETS],
        "T4_non_declenche": not res["sante"]["etat_global"]["T4"],
        "T4_nb_taches": [sa[str(c)]["T4"]["nb_taches_cos_moyen_ge_0_999"] for c in BUDGETS],
        "T5_non_declenche": not res["sante"]["etat_global"]["T5"],
        "T5_plus_grand_standard_moins_renforce": max(sa[str(c)]["T5"]["plus_grand_standard_moins_renforce"] for c in BUDGETS),
        "T5_plus_grand_ecart_de_contraste": max(sa[str(c)]["T5"]["plus_grand_abs_ecart_de_contraste"] for c in BUDGETS),
        "T6_non_declenche": not res["sante"]["etat_global"]["T6"],
        "T6_plus_grand_ecart_a_alpha": max(sa[str(c)]["T6"]["plus_grand_abs_ecart_a_alpha"] for c in BUDGETS),
    }
    ctrl["ok"] = (ctrl["T2_non_declenche"] and ctrl["T3_non_declenche"] and ctrl["T4_non_declenche"]
                  and ctrl["T5_non_declenche"] and ctrl["T6_non_declenche"]
                  and tuple(ctrl["T3_nb_taches"]) == ATTENDU_12["T3_nb_taches_poids_pur"]
                  and tuple(ctrl["T4_nb_taches"]) == ATTENDU_12["T4_nb_taches"]
                  and round(ctrl["T5_plus_grand_standard_moins_renforce"], 5) == ATTENDU_12["T5_plus_grand_standard_moins_renforce_arrondi_5_decimales"]
                  and round(ctrl["T5_plus_grand_ecart_de_contraste"], 5) == ATTENDU_12["T5_plus_grand_ecart_de_contraste_arrondi_5_decimales"]
                  and round(ctrl["T6_plus_grand_ecart_a_alpha"], 5) == ATTENDU_12["T6_plus_grand_ecart_a_alpha_arrondi_5_decimales"])
    t["controles"] = ctrl
    v9 = {k: res["verdicts_regles_originales"][k]["verdict"] for k in ("HR1", "HR0", "HR3", "HR2")}
    t["verdicts_9"] = {"obtenu": v9, "attendu": ATTENDU_12["verdicts_9"], "ok": v9 == ATTENDU_12["verdicts_9"]}
    g = [e["g"] for e in res["ecart_de_replication"]["contrastes_primaires"].values()]
    comptes = res["comptes_graines_neuves"]["comptes"]
    t["auto_essai_contre_elle_meme"] = {
        "g_pi": g, "tous_nuls": all(x == 0 for x in g),
        "TR2_declenche": res["declencheurs_audit"]["TR2_trop_propre"],
        "comptes_graines_neuves": comptes, "tous_egaux_a_200": all(v == 200 for v in comptes.values()),
        "arret_graines_non_neuves": res["comptes_graines_neuves"]["arret_graines_non_neuves"],
        "ok": (all(x == 0 for x in g) and res["declencheurs_audit"]["TR2_trop_propre"]
               and all(v == 200 for v in comptes.values()) and res["comptes_graines_neuves"]["arret_graines_non_neuves"])}
    t["ok"] = (t["table_A"]["ok"] and all(v["ok"] for tb in ("table_B", "table_Bprime", "table_C") for v in t[tb].values())
               and ctrl["ok"] and t["verdicts_9"]["ok"] and t["auto_essai_contre_elle_meme"]["ok"])
    return t


def _recoupements_hors_specification(res: dict, analyse_a: dict, e1: dict) -> dict:
    """Recoupements avec des champs de l'analyse de la course qui ne font pas partie du contrat de la spécification
    (sections `variantes` et contrastes « V standard seul / renforce seul »). Informatif : sans effet sur la
    conclusion ; une absence ou une différence est consignée telle quelle."""
    par_budget = selectionner_taches(valider_forme_E1(e1))
    sortie, ecart_max, nb_comparaisons = {}, 0.0, 0
    for c in BUDGETS:
        d = extraire_donnees(par_budget[c], c)
        ch = d["champs"]
        var_a = analyse_a["resultat"][str(c)].get("variantes", {})
        lignes = {}
        for nom in NOMS_VARIANTES:
            va = var_a.get(nom)
            if va is None:
                lignes[NOM_COURT[nom]] = "absent de l'analyse de référence"
                continue
            comp = {}
            paires = {
                "V_iii_final (moyenne)": (va.get("V_iii_final"), float(np.mean(ch[nom]["V_iii_final"]))),
                "ii_final (moyenne)": (va.get("ii_final"), float(np.mean(ch[nom]["ii_final"]))),
                "exploitabilite_finale (moyenne)": (va.get("exploitabilite_finale"), float(np.mean(ch[nom]["exploitabilite_finale"]))),
                "exploitabilite_moyenne_tours (moyenne)": (va.get("exploitabilite_moyenne_tours"), float(np.mean(ch[nom]["exploitabilite_moyenne_tours"]))),
                "fpr (moyenne)": (va.get("fpr_moyen"), float(np.mean(ch[nom]["fpr_final"]))),
                "standard - renforce (moyenne)": (va.get("standard_moins_renforce"),
                                                 float(np.mean(ch[nom]["V_iii_standard"])) - float(np.mean(ch[nom]["V_iii_renforce"]))),
            }
            for lib, (x_a, x_b) in paires.items():
                if isinstance(x_a, (int, float)):
                    comp[lib] = abs(float(x_a) - x_b)
                    ecart_max = max(ecart_max, comp[lib])
                    nb_comparaisons += 1
                else:
                    comp[lib] = None
            lignes[NOM_COURT[nom]] = comp
        # cosinus consécutifs moyens par tâche de R4 (base du contrôle T4) et poids purs de R3
        cos_a = var_a.get(NOMS_VARIANTES[4], {}).get("cos_consecutif_par_tache")
        if isinstance(cos_a, list) and len(cos_a) == N:
            mes = [sum(v) / 8 for v in d["cos_R4"]]
            e = max(abs(x - y) for x, y in zip(cos_a, mes))
            lignes["R4 cos moyen par tâche (cos_consecutif_par_tache)"] = e
            ecart_max = max(ecart_max, e)
            nb_comparaisons += 1
        pur = var_a.get("R3", {}).get("poids", {}).get("part_pure")
        if isinstance(pur, (int, float)):
            lignes["R3 part de tâches à poids pur (poids.part_pure)"] = abs(float(pur) - res["sante"][str(c)]["T3"]["nb_taches_poids_pur"] / N)
            nb_comparaisons += 1
        contr_a = analyse_a["resultat"][str(c)]["contrastes_contre_R2"]
        for nom in VARIANTES_CONTRASTEES:
            ent = contr_a.get(f"{nom} - R2 (V standard seul / renforce seul)")
            if ent is None:
                continue
            ec = res["sante"][str(c)]["T5"]["ecart_de_contraste"][NOM_COURT[nom]]
            e = max(abs(ent["moyenne_standard"] - ec["a_standard"]), abs(ent["moyenne_renforce"] - ec["b_renforce"]),
                    abs(ent["ecart"] - ec["a_moins_b"]))
            lignes[f"{NOM_COURT[nom]} contraste standard seul / renforcé seul (T5, a, b, a−b)"] = e
            ecart_max = max(ecart_max, e)
            nb_comparaisons += 1
        sortie[str(c)] = lignes
    return {"nature": "hors contrat de la spécification ; informatif", "nombre_de_comparaisons": nb_comparaisons,
            "ecart_maximal_absolu": ecart_max, "par_budget": sortie}


def _plus_petites_marges(res: dict, combien: int = 6) -> list:
    cl = res["classes"]
    lignes = [("table_A", cl["table_A"]["marge_min_au_seuil"])]
    for table in ("table_B", "table_Bprime", "table_C"):
        for court, par_c in cl[table].items():
            for c, d in par_c.items():
                lignes.append((f"{table}/{court}/budget {c}", d["marge_min_au_seuil"]))
    lignes.sort(key=lambda x: x[1])
    return [{"classe": nom, "marge_min_au_seuil": m} for nom, m in lignes[:combien]]


def valider_originale(dossier, dossier_sortie) -> dict:
    """Validation obligatoire du § 12. Écrit la sortie de l'implémentation (sortie-b-originale-v1.json) et rend
    le rapport (dictionnaire) ; l'appelant écrit validation-b-v1.json et validation-b-v1.md."""
    t0 = time.perf_counter()
    dossier, dossier_sortie = Path(dossier), Path(dossier_sortie)
    entrees = dossier / "entrees"
    p_spec = entrees / "specification-statistique-decisive-v1.md"
    p_res = entrees / "resultats-regles-defense.json"
    p_ana = entrees / "analyse-regles-defense.json"

    octets_spec = p_spec.read_bytes()
    sha_spec = empreinte_octets(octets_spec)
    rapport = {"version_validation": "validation-b-v1", "implementation": f"implementation_b.py ({VERSION_IMPLEMENTATION})",
               "python": platform.python_version(), "numpy": np.__version__}
    rapport["entrees"] = {
        "specification": {"fichier": p_spec.name, "sha256": sha_spec, "prefixe_attendu": PREFIXE_EMPREINTE_SPECIFICATION,
                          "conforme": sha_spec.startswith(PREFIXE_EMPREINTE_SPECIFICATION)},
        "resultats_originaux": {"fichier": p_res.name, "sha256": empreinte_octets(p_res.read_bytes()),
                                "attendu": EMPREINTE_RESULTATS_ORIGINAUX},
        "analyse_de_reference_A": {"fichier": p_ana.name, "sha256": empreinte_octets(p_ana.read_bytes()),
                                   "attendu": EMPREINTE_ANALYSE_ORIGINALE}}
    for k in ("resultats_originaux", "analyse_de_reference_A"):
        rapport["entrees"][k]["conforme"] = rapport["entrees"][k]["sha256"] == rapport["entrees"][k]["attendu"]

    rapport["vecteurs_regle_D"] = _vecteurs_regle_d()
    rapport["vecteurs_generateur"] = _vecteurs_generateur()

    # la sortie de l'implémentation sur la course originale (racine imposée 20266201, essai contre elle-même)
    t1 = time.perf_counter()
    res = analyser_fichiers(resultats=p_res, racine=RACINE_COURSE_ORIGINALE, analyse_originale=p_ana,
                            resultats_originaux=p_res)
    duree_analyse = time.perf_counter() - t1
    chemin_b = dossier_sortie / NOM_SORTIE_B
    sha_b = ecrire_json_neuf(chemin_b, res)
    rapport["sortie_de_B"] = {"fichier": chemin_b.name, "sha256": sha_b, "racine": res["racine_de_reechantillonnage"],
                              "arrets_de_la_liste_d_arret": res["arrets"], "duree_analyse_s": round(duree_analyse, 3)}

    analyse_a = lire_json_octets(p_ana.read_bytes(), "A")
    e1 = lire_json_octets(p_res.read_bytes(), "E1")
    comparaison = comparer_a_reference(res, analyse_a, analyse_a)
    rapport["comparaison_A_B"] = comparaison
    rapport["table_de_controle_12"] = _table_12(res, octets_spec.decode("utf-8"))
    rapport["attendus_12"] = _attendus_12(res)
    rapport["plus_petites_marges_aux_seuils"] = _plus_petites_marges(res)
    rapport["classes_a_la_frontiere"] = res["classes_a_la_frontiere"]
    rapport["recoupements_hors_specification"] = _recoupements_hors_specification(res, analyse_a, e1)

    cond = {
        "entrees_conformes": all(v.get("conforme", False) for v in rapport["entrees"].values()),
        "vecteurs_regle_D": rapport["vecteurs_regle_D"]["ok"],
        "vecteurs_generateur": rapport["vecteurs_generateur"]["ok"],
        "statistiques_16x2_a_1e-9": (not comparaison["discordance_a_arret"]) and not comparaison["alertes_de_discordance"]
                                    and comparaison["ecart_maximal_absolu"] is not None
                                    and comparaison["ecart_maximal_absolu"] <= EPS,
        "table_de_controle_12": rapport["table_de_controle_12"]["ok"],
        "classes_identiques_A_B": comparaison["classes"]["identiques"],
        "verdicts_identiques_A_B": comparaison["verdicts_regles_originales"]["identiques"]
                                   and comparaison["verdicts_bruts_replication"]["identiques"],
        "z_pi_concordants": comparaison["z_pi"]["ok"],
        "classes_controles_verdicts_conformes_au_12": rapport["attendus_12"]["ok"],
    }
    cond["validation_reussie"] = all(cond.values())
    rapport["conclusion"] = cond
    rapport["duree_totale_s"] = round(time.perf_counter() - t0, 3)
    return rapport


def _e(x) -> str:
    return "0" if x == 0 else f"{x:.2e}"


def rapport_markdown(r: dict) -> str:
    """Rendu lisible du rapport de validation (le fichier JSON fait foi)."""
    c, cmp_ = r["conclusion"], r["comparaison_A_B"]
    ok = "RÉUSSIE" if c["validation_reussie"] else "ÉCHEC"
    L = []
    L.append("# Validation de l'implémentation B sur la course originale — v1\n")
    L.append(f"**Verdict : validation {ok}.** Écart maximal absolu entre ma sortie et l'analyse de référence : "
             f"**{_e(cmp_['ecart_maximal_absolu'])}** sur 32 contrastes (16 par budget, chacun : moyenne, écart-type, dix quantiles ; "
             f"exigence ≤ 1e-9). Classes et verdicts : **identiques** à ceux de la référence et à ceux écrits dans le § 12 de la spécification."
             if c["validation_reussie"] else
             f"**Verdict : validation {ok}.** Voir les conditions non remplies ci-dessous.")
    L.append("")
    L.append(f"Implémentation : `{r['implementation']}` · Python {r['python']} · numpy {r['numpy']} · "
             f"analyse en {r['sortie_de_B']['duree_analyse_s']} s (validation complète : {r['duree_totale_s']} s).\n")
    L.append("## Conditions de réussite\n")
    L.append("| Condition | Résultat |\n|---|---|")
    libs = {
        "entrees_conformes": "Empreintes des trois entrées conformes",
        "vecteurs_regle_D": "Règle D : trois vecteurs d'essai, gardes sur les six entiers, cas sain",
        "vecteurs_generateur": "Générateur : indices des deux vecteurs d'essai du § 5.5",
        "statistiques_16x2_a_1e-9": "Statistiques des 16 contrastes × 2 budgets à 1e-9 près",
        "table_de_controle_12": "Tableau de contrôle du § 12 (10 lignes lues dans la spécification)",
        "classes_identiques_A_B": "Classes (tables A, B, B′, C) identiques entre ma sortie et les nombres de la référence",
        "verdicts_identiques_A_B": "Verdicts identiques entre ma sortie et les nombres de la référence",
        "z_pi_concordants": "Écarts réduits z des quatre contrastes primaires concordants à 1e-9",
        "classes_controles_verdicts_conformes_au_12": "Classes, contrôles, verdicts et auto-essai conformes au texte du § 12",
    }
    for k, lib in libs.items():
        L.append(f"| {lib} | {'oui' if c[k] else '**NON**'} |")
    L.append("")
    L.append("## Entrées (empreintes SHA-256)\n")
    for k, v in r["entrees"].items():
        att = v.get("attendu", v.get("prefixe_attendu"))
        L.append(f"- {k} : `{v['fichier']}` — `{v['sha256']}` (attendu : `{att}…`)" if k == "specification"
                 else f"- {k} : `{v['fichier']}` — `{v['sha256']}` (attendu : identique : {v['conforme']})")
    L.append(f"- Sortie de B : `{r['sortie_de_B']['fichier']}` — `{r['sortie_de_B']['sha256']}` (racine {r['sortie_de_B']['racine']})\n")
    L.append("## Vecteurs d'essai\n")
    L.append("Règle D (§ 4) — H, ρ calculé, ρ attendu, résultat :\n")
    for v in r["vecteurs_regle_D"]["vecteurs"]:
        L.append(f"- `{v['H'][:8]}…` : ρ = {v['rho']} ; ρ_t = {v['rho_t']} → {'identiques aux attendus' if v['ok'] else '**DIFFÉRENTS**'} ; "
                 f"les gardes rejettent bien ce vecteur (interdit comme racine) : {v['gardes_rejettent_ce_vecteur']}")
    cs = r["vecteurs_regle_D"]["cas_sain"]
    L.append(f"- Cas sain : la règle D appliquée à l'empreinte du préenregistrement original rend ({cs['rho']}, {cs['rho_t']}), "
             f"différent de (20266201, 20266202) : {cs['differe_de_20266201_20266202']}.\n")
    L.append("Générateur (§ 5.5), racine 20266201 :\n")
    for v in r["vecteurs_generateur"]["vecteurs"]:
        L.append(f"- clé {tuple(v['cle'])} : forme {tuple(v['forme'])}, {v['dtype']} ; ligne 0, dix premiers = {v['ligne0_dix_premiers']} ; "
                 f"dernière ligne, cinq derniers = {v['derniere_ligne_cinq_derniers']} → {'conformes' if v['ok'] else '**DIFFÉRENTS**'}")
    L.append("")
    t12 = r["table_de_controle_12"]
    L.append(f"## Tableau de contrôle du § 12 ({t12['nombre_de_lignes_lues']} lignes lues dans le texte de la spécification)\n")
    L.append("| Budget | Contraste | Écart max. absolu (moyenne, écart-type, 4 quantiles) | Conforme |\n|---|---|---|---|")
    for d in t12["lignes"]:
        L.append(f"| {d['budget']} | {d['contraste']} | {_e(d['ecart_max_abs'])} | {'oui' if d['ok'] else '**NON**'} |")
    L.append("")
    L.append("## Concordance avec l'analyse de référence, contraste par contraste\n")
    L.append("Niveau « arrêt » : les cinq contrastes dont une discordance arrête la lecture ; « alerte » : les onze autres. "
             "Colonne « n / zéros » : nombre d'instances et nombre de différences exactement nulles, identiques à la référence.\n")
    L.append("| Budget | Contraste | Niveau | Écart max. absolu | n / zéros |\n|---|---|---|---|---|")
    for cb in ("1", "2"):
        for lib, d in cmp_["detail_par_contraste"][cb].items():
            L.append(f"| {cb} | {lib} | {d['niveau']} | {_e(d['ecart_max_abs'])} | {'oui' if d['n_identique'] and d['zeros_exacts_identiques'] else '**NON**'} |")
    L.append("")
    L.append(f"Écart maximal absolu : tous contrastes **{_e(cmp_['ecart_maximal_absolu'])}** ; "
             f"contrastes à arrêt {_e(cmp_['ecart_maximal_absolu_contrastes_a_arret'])} ; "
             f"contrastes à alerte {_e(cmp_['ecart_maximal_absolu_contrastes_a_alerte'])}. "
             f"Écarts réduits z des quatre contrastes primaires : écart A/B maximal {_e(max(cmp_['z_pi']['ecart_abs'].values()))}.\n")
    L.append("## Classes (première condition vraie ; budget 1 / budget 2)\n")
    at = r["attendus_12"]
    L.append(f"- Table A (Δ(R3, R2) sur V, détection finale) : ligne {at['table_A']['obtenu'][0]}, « {at['table_A']['obtenu'][1]} » — conforme au § 12 : {at['table_A']['ok']}")
    noms_tables = {"table_B": "Table B (détection V)", "table_Bprime": "Table B′ (exploitabilité moyenne X̄)",
                   "table_C": "Table C (détection sur les lois tenues à l'écart, ligne)"}
    for tb, nom in noms_tables.items():
        L.append(f"- {nom} :")
        for court, v in at[tb].items():
            L.append(f"  - {court} : {v['obtenu'][0]} / {v['obtenu'][1]} — conforme au § 12 : {v['ok']}")
    L.append(f"- Comparaison avec les classes calculées sur les nombres de la référence : {cmp_['classes']['nombre_de_classes_comparees']} classes comparées, "
             f"différences : {len(cmp_['classes']['differences'])} ; classes à la frontière numérique : {len(cmp_['classes']['classes_a_la_frontiere'])}.\n")
    L.append("## Contrôles de santé (budget 1 / budget 2)\n")
    ct = at["controles"]
    L.append(f"- T2 (résultat trop beau ou jeu trop mauvais) non déclenché : {ct['T2_non_declenche']}")
    L.append(f"- T3 (mélange dégénéré) non déclenché : {ct['T3_non_declenche']} ; tâches à poids pur : {ct['T3_nb_taches']}")
    L.append(f"- T4 (régularisation dégénérée) non déclenché : {ct['T4_non_declenche']} ; tâches à cosinus moyen ≥ 0,999 : {ct['T4_nb_taches']} (attendu : 5 et 2)")
    L.append(f"- T5 (écart entre les deux optimiseurs) non déclenché : {ct['T5_non_declenche']} ; plus grand écart standard − renforcé : {ct['T5_plus_grand_standard_moins_renforce']:.6f} (attendu : 0,00039) ; "
             f"plus grand écart de contraste : {ct['T5_plus_grand_ecart_de_contraste']:.6f} (attendu : 0,00043)")
    L.append(f"- T6 (dérive du taux de fausses alertes) non déclenché : {ct['T6_non_declenche']} ; plus grand écart à α : {ct['T6_plus_grand_ecart_a_alpha']:.6f} (attendu : 0,00019)\n")
    L.append("## Verdicts de la course originale (§ 9)\n")
    v9 = at["verdicts_9"]["obtenu"]
    L.append(f"- Le mélange bat l'historique (HR1) : **{v9['HR1']}**\n- Réentraîner vaut mieux que ne rien faire (HR0) : **{v9['HR0']}**\n"
             f"- La régularisation ne nuit pas (HR3) : **{v9['HR3']}**\n- Oublier coûte (HR2, descriptif) : **{v9['HR2']}**\n"
             f"- Conformes au § 12 : {at['verdicts_9']['ok']} ; identiques aux verdicts calculés sur les nombres de la référence : {cmp_['verdicts_regles_originales']['identiques']}.\n")
    ae = at["auto_essai_contre_elle_meme"]
    L.append("## Essai des gardes de la réplication « contre elle-même » (§ 12, cas artefact)\n")
    L.append(f"- g des quatre contrastes primaires : {ae['g_pi']} → tous nuls : {ae['tous_nuls']}\n"
             f"- TR2 (résultat trop propre) déclenché : {ae['TR2_declenche']}\n"
             f"- Comptes « graines neuves » : {ae['comptes_graines_neuves']} → tous égaux à 200 : {ae['tous_egaux_a_200']}\n"
             f"- Arrêt « graines non neuves » déclenché : {ae['arret_graines_non_neuves']}\n"
             f"- Conforme au § 12 : {ae['ok']}. Code de sortie de la commande `analyser` dans ce cas : 3 (sortie écrite, lecture non autorisée).\n")
    L.append("## Marges aux seuils (ce qui rend les classes robustes au calcul numérique)\n")
    L.append("Plus petite distance entre une quantité comparée et son seuil, sur les comparaisons effectivement évaluées pour chaque classe "
             "(seuil de frontière numérique : 1e-9). Les six plus petites :\n")
    for m in r["plus_petites_marges_aux_seuils"]:
        L.append(f"- {m['classe']} : {m['marge_min_au_seuil']:.3e}")
    L.append(f"\nClasses marquées à la frontière : {r['classes_a_la_frontiere'] or 'aucune'}.\n")
    rc = r["recoupements_hors_specification"]
    L.append("## Recoupements hors contrat de la spécification (informatif)\n")
    L.append(f"{rc['nombre_de_comparaisons']} comparaisons de champs de l'analyse de référence qui ne font pas partie du contrat "
             f"(moyennes par variante, écart standard − renforcé, cosinus moyens par tâche de R4, part de tâches à poids pur de R3, "
             f"contrastes « V standard seul / renforcé seul »). Écart maximal absolu : **{_e(rc['ecart_maximal_absolu'])}**.\n")
    L.append("## Ce que cette validation ne couvre pas\n")
    L.append("- Le mode réplication (règle D appliquée au texte scellé, manifeste, fichiers compagnons, concordance des racines) n'a pas de "
             "données réelles à ce stade ; il est essayé par les tests unitaires sur des pièces synthétiques (`test_implementation_b.py`).\n"
             "- Les contrôles de santé de la référence A ne sont pas dans l'analyse de la course : ils sont confrontés au texte du § 12 et aux "
             "champs voisins de l'analyse (recoupements ci-dessus), pas à des états écrits par A.\n"
             "- La concordance des écarts réduits z est établie ici sur le cas où A et B portent sur les mêmes résultats (essai contre elle-même).\n")
    return "\n".join(L) + "\n"


def valider_originale_cli(a) -> int:
    dossier = Path(a.dossier)
    dossier_sortie = Path(a.dossier_sortie) if a.dossier_sortie else dossier
    chemins = [dossier_sortie / n for n in (NOM_SORTIE_B, NOM_VALIDATION_JSON, NOM_VALIDATION_MD)]
    existants = [str(p) for p in chemins if p.exists()]
    if existants:
        sys.stderr.write("ERREUR : fichiers déjà existants (jamais écrasés ; nouvelle version = nouveau nom) : "
                         + ", ".join(existants) + "\n")
        return 4
    try:
        rapport = valider_originale(dossier, dossier_sortie)
    except Arret as e:
        sys.stderr.write(f"ARRÊT : {e}\n")
        return 2
    sha_json = ecrire_json_neuf(dossier_sortie / NOM_VALIDATION_JSON, rapport)
    md = rapport_markdown(rapport)
    with open(dossier_sortie / NOM_VALIDATION_MD, "x", encoding="utf-8", newline="\n") as f:
        f.write(md)
    sys.stderr.write(f"{NOM_VALIDATION_JSON} sha256 {sha_json}\n")
    sys.stderr.write("validation " + ("RÉUSSIE" if rapport["conclusion"]["validation_reussie"] else "ÉCHEC") + "\n")
    return 0 if rapport["conclusion"]["validation_reussie"] else 3


def _cmd_valider(a) -> int:
    return valider_originale_cli(a)


if __name__ == "__main__":
    sys.exit(main())
