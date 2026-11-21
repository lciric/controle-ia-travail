"""Montage de la seconde passe : `montage_v1` plus `model.embed_tokens.weight`, seuils d'espace de la seconde passe, garde par
les noms des variables d'environnement, appel de `nos_lentilles_v1`.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`), « Plan d'analyse », point 4, « Montage de la seconde
passe » ; « Entrées » (poids, nos lentilles, points 1 à 5) ; « Liste d'arrêt », lignes de la v2. Le texte décide, le code suit.
Tout ce que `montage_v1` fait reste dans `montage_v1`, appelé tel quel (R12) ; ce module n'ajoute que ce que la v2 ajoute.

**Corpus des jetons gardés** (nœud du développeur, N-dev-1) : `montage_v1.cibles_corpus` ne lit que la première page de
l'arbre paginé d'un jeu de données ; il n'est pas réemployé tel quel. `cibles_du_corpus` est le point de branchement : il
prend la fonction qu'on lui donne, sinon celle du module `corpus_pagine_v1` (écrit ailleurs) s'il est présent ; sinon arrêt.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np

from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import montage_v1 as mo
from . import nos_lentilles_v1 as nl
from .constantes_v1 import Arret

TENSEURS_GARDES_V2 = K.TENSEURS_GARDES + (K2.TENSEUR_PLONGEMENTS,)
NOM_CLE_PERMISE = K.NOM_CLE


# --- garde par les noms des variables d'environnement -------------------------------------------------------------------------------------
def exiger_noms_des_variables(env=None) -> list[str]:
    """Le lanceur relève les **noms** (jamais les valeurs) des variables d'environnement ; un nom qui contient `TOKEN` et `HF`
    ou `HUGGING`, autre que `HF_TOKEN` : arrêt, nœud (une seconde clé de la plateforme de modèles n'a rien à faire dans cette
    session ; elle n'est ni lue, ni employée). Rend les noms qui ressemblent à une clé de la plateforme (au plus `HF_TOKEN`)."""
    noms = list((os.environ if env is None else env).keys())            # les noms seuls : aucune valeur n'est lue
    suspects = sorted(n for n in noms if "TOKEN" in n.upper() and ("HF" in n.upper() or "HUGGING" in n.upper()))
    en_trop = [n for n in suspects if n != NOM_CLE_PERMISE]
    if en_trop:
        raise Arret(f"variable d'environnement d'un nom de clé de la plateforme de modèles autre que {NOM_CLE_PERMISE} "
                    f"({', '.join(en_trop)}) : arrêt ; nœud ; elle n'est ni lue, ni employée")
    return suspects


# --- plongements ---------------------------------------------------------------------------------------------------------------------------
def exiger_plongements_dans_l_index(index: bytes) -> None:
    """`model.embed_tokens.weight` absent de l'index : arrêt avant tout calcul."""
    try:
        carte = json.loads(index.decode("utf-8"))["weight_map"]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError):
        raise Arret("index des poids illisible : arrêt avant tout calcul") from None
    if K2.TENSEUR_PLONGEMENTS not in carte:
        raise Arret(f"{K2.TENSEUR_PLONGEMENTS} absent de l'index : arrêt avant tout calcul")


def exiger_forme_des_plongements(description: dict, forme: tuple = K2.FORME_PLONGEMENTS) -> None:
    """`model.embed_tokens.weight` d'une autre forme que celle du texte (128 256 × 4 096) : arrêt avant tout calcul."""
    if tuple(description.get("shape", ())) != tuple(forme):
        raise Arret(f"{K2.TENSEUR_PLONGEMENTS} d'une autre forme que {forme[0]} × {forme[1]} ({description.get('shape')}) : arrêt "
                    "avant tout calcul")


def cle_tie_word_embeddings(config: bytes):
    """Clé `tie_word_embeddings` de `config.json`, relevée et rapportée ; le tenseur lu est celui de l'index, quel que soit
    son lien avec `lm_head.weight`."""
    try:
        return json.loads(config.decode("utf-8")).get("tie_word_embeddings")
    except (UnicodeDecodeError, json.JSONDecodeError, AttributeError):
        return None


# --- corpus des jetons gardés : point de branchement --------------------------------------------------------------------------------------
def cibles_du_corpus(voisin: Path, transport, fonction=None) -> list:
    """Cibles de l'essai d'un octet d'un fichier de chaque jeu de données du corpus. Jamais `montage_v1.cibles_corpus` tel
    quel (il ne lit que la première page de l'arbre paginé). Sans fonction donnée ni module `corpus_pagine_v1` : arrêt."""
    if fonction is not None:
        return fonction(voisin, transport)
    try:
        from . import corpus_pagine_v1 as cp           # écrit par un autre développeur ; absent tant qu'il n'est pas poussé
    except ImportError:
        raise Arret("cibles du corpus des jetons gardés : la lecture paginée de l'arbre (`corpus_pagine_v1`) n'est pas "
                    "branchée ; celle de `montage_v1` ne lit que la première page : rien ne part ; nœud") from None
    if not hasattr(cp, "cibles_corpus"):
        raise Arret("cibles du corpus des jetons gardés : `corpus_pagine_v1` ne porte pas la fonction attendue "
                    "(`cibles_corpus`) : rien ne part ; nœud")
    return cp.cibles_corpus(voisin, transport)


# --- nos lentilles ----------------------------------------------------------------------------------------------------------------------------
def cibles_de_nos_lentilles(fiche: dict, conditions: dict) -> list:
    """L'essai d'un octet porte aussi sur chacun de nos fichiers lus, avec la clé, à la révision de la fiche."""
    return [nl.cible_un_octet(l, fiche["lentilles"][l]) for l in K2.NOS_LENTILLES if conditions[l].lue]


def attendu_de(lettre: str, reglages_lentilles: dict, chemin_piece_meta_s: Path | None, sha256_piece_meta_s: str) -> nl.Attendu:
    """Ce que le texte attend du fichier d'une lentille : pour notre R, la `meta` de la table de « Entrées » ; pour notre S,
    le champ `meta` lu par le code dans la pièce du 18 novembre, sur son empreinte."""
    base = dict(reglages_lentilles[lettre])
    if base.get("meta") is None:
        if lettre == "R":
            base["meta"] = dict(K2.META_R)
        else:
            if chemin_piece_meta_s is None:
                raise Arret("pièce du 18 novembre de notre S non désignée : arrêt ; nœud")
            base["meta"] = nl.meta_attendue_de_s(chemin_piece_meta_s, sha256_piece_meta_s)
    return nl.Attendu(lettre=lettre, **base)


def monter_une_lentille(transport, cle, lettre: str, l: dict, palier: int, attendu: nl.Attendu, dossier: Path) -> tuple[dict, dict]:
    """Points 3 et 4 de « Entrées » pour une lentille lue : lecture en flux à la révision de la fiche, SHA-256 et taille
    calculés sur le flux et comparés à la fiche (et, au premier palier, à l'empreinte du 18 novembre) ; `meta` et état
    comparés à la table. Rend (description de l'extraction, contrôle de `meta` et de l'état)."""
    url = mo.url_fichier(l["depot"], l["revision"], l["chemin"])
    description = nl.lire_ajustement_en_flux(transport, url, cle, attendu, dossier, int(l["taille"]), l["sha256_relecture"],
                                             K2.EMPREINTE_18_NOVEMBRE[lettre] if palier == 1 else None)
    return description, nl.controler_meta_et_etat(description, attendu)


def matrices_publiques(dossier_lentille: Path, couches) -> dict:
    """Matrices gardées de la lentille publique, en simple précision (pour le contrôle « notre R distincte de la publique »)."""
    return {int(c): np.load(Path(dossier_lentille) / f"J-{c}.npy", allow_pickle=False).astype(np.float32) for c in couches}
