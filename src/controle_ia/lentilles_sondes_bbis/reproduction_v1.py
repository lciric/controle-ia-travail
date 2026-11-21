"""Reproduction de la première passe par la seconde : ouverture des tables fermées de la première passe sur l'empreinte de
leur ligne de registre ; comparaison, par programme, des lectures de la lentille publique et de la lentille des logits.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`), « Plan d'analyse », point 11 ; « Métrique », point 6
(« Lien avec la première passe ») et point 10 (dernier alinéa) ; « Liste d'arrêt », lignes de la v2. Le texte décide.

- Les tables de la première passe sont ouvertes **par le programme**, jamais par une personne, **sur leur empreinte**, égale
  à celle de la ligne `TABLES-LENTILLES-BBIS` ; une autre empreinte : arrêt (R11). Le code ne les ouvre qu'après
  `SCELLEMENT-LENTILLES-BBIS-V2` ou `ABANDON-LENTILLES-BBIS-V2`.
- Empreinte de E-1 ou de E-2 différente entre les deux passes : arrêt (R11).
- Comparé, par lecture (direction, signe, lentille publique ou des logits) : le libellé et les vingt premiers jetons ; et
  l'écart maximal des scores, en valeur relative. Égalité : rapportée. Différence : **réserve écrite, sans arrêt** ; pour une
  direction dont le libellé de la lentille publique diffère d'une passe à l'autre, les comparaisons entre lentilles sont « non
  calculables » et l'audit de symétrie de la seconde passe est joué.
- Première passe **jamais lancée** (ni ligne des entrées ni ligne des tables) : la seconde la remplace pour la lentille
  publique, et c'est écrit. Première passe **lancée et non achevée** : elle n'est pas remplacée ; rien n'est comparé.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import nos_lentilles_v1 as nl
from .constantes_v1 import Arret

LENTILLES_REPRODUITES = (K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS)
ETAT_FAITE = "faite"
ETAT_NON_FAITE = "non faite : première passe lancée et non achevée"
ETAT_REMPLACEE = "sans objet : première passe jamais lancée ; la seconde passe la remplace"


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def ouvrir_tables_premiere_passe(racine: str | Path, registre_propre: str | Path, etat: nl.EtatRegistre) -> dict:
    """Tables fermées de la première passe, lues sous `racine` au chemin de la ligne `TABLES-LENTILLES-BBIS`, sur l'empreinte
    de cette ligne. Avant `SCELLEMENT-LENTILLES-BBIS-V2` ou `ABANDON-LENTILLES-BBIS-V2` : refus. Autre empreinte, ou fichier
    absent : arrêt (R11) ; nœud."""
    nl.exiger_ouverture_permise_des_tables(registre_propre)
    if etat.premiere_passe != nl.PREMIERE_PASSE_ACHEVEE:
        raise Arret("tables de la première passe : aucune ligne TABLES-LENTILLES-BBIS ; rien n'est ouvert")
    ligne = etat.derniere(K2.CLE_TABLES_V1)
    chemin = Path(racine) / ligne.chemin
    if not chemin.is_file():
        raise Arret(f"tables de la première passe absentes sur disque ({ligne.chemin}) : arrêt (R11) ; nœud")
    octets = chemin.read_bytes()
    if _sha(octets) != ligne.sha256:
        raise Arret("tables de la première passe d'une autre empreinte que celle de la ligne TABLES-LENTILLES-BBIS : arrêt "
                    "(R11) ; nœud")
    try:
        tables = json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Arret("tables de la première passe illisibles : arrêt (R11) ; nœud") from None
    tables["_ligne"] = {"chemin": ligne.chemin, "sha256": ligne.sha256}
    return tables


def exiger_memes_entrees(tables_premiere_passe: dict, sha256_e1: str, sha256_e2: str) -> dict:
    """Empreinte de E-1 ou de E-2 différente entre les deux passes : arrêt (R11)."""
    entrees = tables_premiere_passe.get("entrees") or {}
    if entrees.get("e1_sha256") != sha256_e1 or entrees.get("e2_sha256") != sha256_e2:
        raise Arret("empreinte de E-1 ou de E-2 différente entre les deux passes : arrêt (R11)")
    return {"e1_sha256": sha256_e1, "e2_sha256": sha256_e2, "egales_entre_les_deux_passes": True}


def scores_premiere_passe(racine: str | Path, tables_premiere_passe: dict) -> dict:
    """Scores de tous les jetons gardés par vecteur et lentille, lus dans les archives fermées de la première passe, chacune
    sur l'empreinte que portent ses tables ; autre empreinte ou fichier absent : arrêt (R11). Seuls les tableaux `scores__…`
    sont décodés."""
    dossier = (Path(racine) / tables_premiere_passe["_ligne"]["chemin"]).parent
    donnees = Path(racine) / "donnees" / dossier.name
    scores = {}
    for morceau in tables_premiere_passe.get("fichiers_des_lectures", []):
        chemin = donnees / morceau["fichier"]
        if not chemin.is_file() or _sha(chemin.read_bytes()) != morceau["sha256"]:
            raise Arret(f"archive de lectures de la première passe absente ou d'une autre empreinte ({morceau['fichier']}) : "
                        "arrêt (R11)")
        with np.load(chemin, allow_pickle=False) as archive:
            for nom in morceau["tableaux"]:
                if nom.startswith("scores__") and not nom.startswith("scores_temoin_de_couche__"):
                    scores[nom] = archive[nom]
    return scores


def _lectures(tables: dict) -> dict:
    """(sonde, vecteur, lentille, signe) → (libellé, vingt premiers identifiants), pour les deux lentilles reproduites."""
    sortie = {}
    for d in tables.get("directions", []):
        for lentille in LENTILLES_REPRODUITES:
            lecture = (d.get("lectures") or {}).get(lentille)
            if lecture is None:
                continue
            for signe, t in lecture["signes"].items():
                sortie[(d["sonde"], d["vecteur"], lentille, signe)] = (t.get("libelle"), [int(i) for i in t["premiers_par_score"]["ids"]])
    return sortie


def comparer(tables_premiere_passe: dict, tables_seconde_passe: dict, scores_un: dict | None = None,
             scores_deux: dict | None = None) -> dict:
    """Compare, par lecture, les libellés et les vingt premiers jetons (mêmes identifiants) de la lentille publique et de la
    lentille des logits d'une passe à l'autre ; rapporte aussi si l'ordre des vingt est le même, et l'écart maximal des
    scores en valeur relative (`scores_*` : nom du tableau `scores__<direction>__<lentille>` → scores). Ne lève aucun arrêt
    sur une différence : c'est une réserve."""
    un, deux = _lectures(tables_premiere_passe), _lectures(tables_seconde_passe)
    seulement = sorted("/".join(k) for k in set(un) ^ set(deux))
    differentes, publique_differente, ordre_different = [], set(), 0
    for cle in sorted(set(un) & set(deux)):
        (lib1, ids1), (lib2, ids2) = un[cle], deux[cle]
        libelle, jetons = lib1 != lib2, set(ids1) != set(ids2)
        ordre_different += int(not jetons and ids1 != ids2)
        if libelle or jetons:
            differentes.append({"lecture": "/".join(cle), "libelle_different": libelle, "jetons_differents": jetons,
                                "libelle_premiere_passe": lib1, "libelle_seconde_passe": lib2})
        if libelle and cle[2] == K.LENTILLE_PUBLIQUE:
            publique_differente.add((cle[0], cle[1], cle[3]))
    ecart = None
    if scores_un is not None and scores_deux is not None:
        ecart = 0.0
        for nom in sorted(set(scores_un) & set(scores_deux)):
            a, b = np.asarray(scores_un[nom], np.float64), np.asarray(scores_deux[nom], np.float64)
            if a.shape != b.shape:
                raise Arret(f"reproduction : scores de formes différentes d'une passe à l'autre ({nom}) : arrêt (R11)")
            echelle = float(np.max(np.abs(a)))
            ecart = max(ecart, float(np.max(np.abs(a - b)) / echelle) if echelle > 0 else float(np.max(np.abs(b))))
    return {"etat": ETAT_FAITE, "lectures_comparees": len(set(un) & set(deux)), "nombre_de_lectures_differentes": len(differentes),
            "lectures_differentes": differentes, "lectures_d_une_seule_passe": seulement,
            "lectures_aux_memes_jetons_dans_un_autre_ordre": ordre_different,
            "ecart_relatif_maximal_des_scores": ecart,
            "directions_au_libelle_de_la_lentille_publique_different": sorted("/".join(k) for k in publique_differente),
            "audit_de_symetrie_a_jouer": bool(differentes or seulement), "issue": "réserve écrite, sans arrêt"}


def libelle_public_different(reproduction: dict, sonde: str, vecteur: str, signe: str) -> bool:
    """Vrai si le libellé de la lentille publique de cette direction diffère d'une passe à l'autre : ses comparaisons entre
    lentilles sont alors « non calculables »."""
    return f"{sonde}/{vecteur}/{signe}" in reproduction.get("directions_au_libelle_de_la_lentille_publique_different", [])


def sans_comparaison(premiere_passe: str) -> dict:
    """Ce que la reproduction rend quand rien n'est comparé : première passe jamais lancée (la seconde la remplace pour la
    lentille publique, et c'est écrit), ou lancée et non achevée (elle n'est **pas** remplacée ; aucune phrase gelée de la
    lentille publique ni de la lentille des logits n'est écrite par la seconde passe)."""
    if premiere_passe == nl.PREMIERE_PASSE_JAMAIS_LANCEE:
        return {"etat": ETAT_REMPLACEE, "phrases_de_la_lentille_publique_et_des_logits_ecrites": True,
                "nombre_de_lectures_differentes": None, "audit_de_symetrie_a_jouer": False,
                "directions_au_libelle_de_la_lentille_publique_different": []}
    if premiere_passe == nl.PREMIERE_PASSE_NON_ACHEVEE:
        return {"etat": ETAT_NON_FAITE, "phrases_de_la_lentille_publique_et_des_logits_ecrites": False,
                "nombre_de_lectures_differentes": None, "audit_de_symetrie_a_jouer": False,
                "directions_au_libelle_de_la_lentille_publique_different": []}
    raise Arret(f"reproduction : état de la première passe inconnu ({premiere_passe!r})")
