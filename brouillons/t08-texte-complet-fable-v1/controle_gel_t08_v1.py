"""Contrôle du gel du texte de T0.8 : une seule écriture, employée par le programme du brouillon 12, par le programme de
scellement (version 2) et par leurs essais.

Règle du texte (« Gel vérifiable ») : hors des marqueurs remplis, des déclarations de vue et des corrections de renvoi,
toute différence dans les sections « Hypothèse » à « Liste d'arrêt » avec le brouillon gelé est un écart, nœud de Lazar.

Ce que le contrôle exige, et arrête sinon (constat B-1 de la contre-lecture 8) :
  (1) le brouillon 4 (ligne GEL-T08) et le brouillon 10 (candidat du compte 4) ont leurs empreintes épinglées ;
  (2) la plage gelée du brouillon 10, une fois retirée la phrase T5-19, est égale à l'octet à celle du brouillon 4 ; la
      phrase T5-19 du brouillon 10 a l'empreinte épinglée (celle que couvre le mot de Lazar, R-2657) ;
  (3) la plage gelée du texte contrôlé, une fois remis le nom de chaque marqueur à la place de sa valeur, est égale à
      l'octet à celle du brouillon 10 : la phrase T5-19 y est donc épinglée dans son texte et à sa place.
Une phrase T5-19 réécrite, déplacée, doublée ou retirée est arrêtée par (3).
"""
from __future__ import annotations

import hashlib
from pathlib import Path

B4 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md")
B10 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon10.md")
SHA_B4 = "7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5"
SHA_B10 = "fb004b96bf7fd70d6fe4f1938cba8bcd1afa9a3261135b5ddea336a9e0c68ba1"
SHA_T5_19 = "906b82d6c063eb60cc0c6179d43fdbcbe0dbc434e430ac6026837fd0ae06cde4"
DEBUT_T5_19 = "   - de la course de T0.8 elle-même, pour la lecture seulement"
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
SECTION_APRES_GEL = "Machine, devis et dépense"


class ArretGel(SystemExit):
    """Arrêt du contrôle du gel : rien ne doit être écrit par l'appelant."""


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def lire_epingle(chemin: Path, attendu: str, racine: Path = Path(".")) -> str:
    octets = (racine / chemin).read_bytes()
    if sha(octets) != attendu:
        raise ArretGel(f"ARRÊT : {chemin} : empreinte {sha(octets)} ≠ {attendu} épinglée (R11)")
    return octets.decode("utf-8")


def plage_gelee(lignes: list[str]) -> tuple[int, int]:
    debuts = [i for i, l in enumerate(lignes) if l.strip() == "## Hypothèse"]
    fins = [i for i, l in enumerate(lignes) if l.strip() == "## " + SECTION_APRES_GEL]
    if len(debuts) != 1 or len(fins) != 1 or fins[0] <= debuts[0]:
        raise ArretGel("ARRÊT : bornes des sections gelées introuvables ou en double")
    titres = tuple(l[3:].strip() for l in lignes[debuts[0]:fins[0]] if l.startswith("## "))
    if titres != GELEES:
        raise ArretGel(f"ARRÊT : sections gelées inattendues : {titres}")
    return debuts[0], fins[0]


def controler_gel(texte: str, valeurs: dict[str, str], racine: Path = Path(".")) -> dict:
    """`valeurs` : nom de marqueur → valeur écrite dans les sections gelées du texte contrôlé (une occurrence chacune)."""
    l4 = lire_epingle(B4, SHA_B4, racine).split("\n")
    l10 = lire_epingle(B10, SHA_B10, racine).split("\n")
    d4, f4 = plage_gelee(l4)
    d10, f10 = plage_gelee(l10)
    gel4, gel10 = l4[d4:f4], l10[d10:f10]
    # (2) brouillon 10 contre brouillon 4 : seule la phrase T5-19 s'ajoute, et c'est celle que couvre le mot de Lazar
    t5 = [i for i, x in enumerate(gel10) if x.startswith(DEBUT_T5_19)]
    if len(t5) != 1:
        raise ArretGel(f"ARRÊT : phrase T5-19 : {len(t5)} occurrence(s) dans la plage gelée du brouillon 10")
    if sha(gel10[t5[0]].encode("utf-8")) != SHA_T5_19:
        raise ArretGel("ARRÊT : phrase T5-19 du brouillon 10 ≠ empreinte épinglée")
    if gel10[:t5[0]] + gel10[t5[0] + 1:] != gel4:
        raise ArretGel("ARRÊT : plage gelée du brouillon 10 ≠ celle du brouillon 4 hors la phrase T5-19")
    # (3) texte contrôlé contre brouillon 10, noms des marqueurs remis
    l = texte.split("\n")
    d, f = plage_gelee(l)
    ramene = "\n".join(l[d:f])
    for nom, valeur in valeurs.items():
        if not valeur or ramene.count(valeur) != 1:
            raise ArretGel(f"ARRÊT : valeur du marqueur {nom} : {ramene.count(valeur) if valeur else 0} occurrence(s) dans "
                           "les sections gelées, une seule attendue")
        ramene = ramene.replace(valeur, f"`<<{nom}>>`")
    if ramene != "\n".join(gel10):
        a, b = gel10, ramene.split("\n")
        premier = next((k for k, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        raise ArretGel("ARRÊT : SECTIONS GELÉES ≠ brouillon 10 (donc ≠ brouillon 4 hors la phrase T5-19), noms des marqueurs "
                       f"remis : première ligne en écart, la {premier + 1}e de la plage ({len(a)} lignes attendues, {len(b)} "
                       "trouvées) : écart, nœud de Lazar ; rien n'est écrit")
    return {"plage_b4": (d4 + 1, f4), "plage_b10": (d10 + 1, f10), "plage_texte": (d + 1, f),
            "sha_plage_b4": sha("\n".join(gel4).encode("utf-8")), "sha_plage_b10": sha("\n".join(gel10).encode("utf-8")),
            "sha_plage_texte": sha("\n".join(l[d:f]).encode("utf-8")), "ligne_t5_19_b10": gel10[t5[0]],
            "rang_t5_19": t5[0] + 1, "marqueurs_remis": dict(valeurs)}


def histoire_t5_19(racine: Path = Path(".")) -> list[dict]:
    """La phrase T5-19 dans chaque brouillon où elle existe (5 à 12) : empreinte de la ligne, et de sa partie de fond
    (avant la parenthèse de statut). Lecture de textes seulement."""
    sortie = []
    for k in range(5, 13):
        chemin = racine / f"brouillons/T0.8-bases-boite-noire-v0-v1-brouillon{k}.md"
        if not chemin.exists():
            continue
        lignes = [x for x in chemin.read_text(encoding="utf-8").split("\n") if x.startswith(DEBUT_T5_19)]
        if len(lignes) != 1:
            sortie.append({"brouillon": k, "occurrences": len(lignes)})
            continue
        ligne = lignes[0]
        j = ligne.find(" (phrase ajoutée au brouillon 5")
        fond = ligne[:j] if j > 0 else ligne
        sortie.append({"brouillon": k, "occurrences": 1, "sha_ligne": sha(ligne.encode("utf-8")),
                       "sha_fond": sha(fond.encode("utf-8"))})
    return sortie
