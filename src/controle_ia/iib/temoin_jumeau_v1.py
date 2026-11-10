"""Champ COST d'une action : occurrence, coupe du préfixe, réécriture de toute la valeur (conception 2.2 points 1 et 2,
5.2 ; décision M4 de la mère). Fonction partagée par le contexte réécrit de l'oracle et par le témoin-jumeau.

- `occurrence_cout` : première occurrence non vide du champ COST dans le texte brut de l'action, par la même règle que
  `premier_test_ia.conditions.bornes_champs` (une occurrence vide est sautée ; la ligne ACTION termine la valeur) ; rend le
  début de la clé et la fin de la valeur (début de la clé suivante, ou fin de l'action).
- `coupe_prefixe` : plus petit rang r, à partir du jeton qui porte le premier caractère de la clé, tel que le décodage de
  `ids[:r]`, nettoyé du gras (`*`, `_`) et des espaces finales, finit par « COST: » (espaces permises avant les deux-points,
  casse indifférente) ; None si aucune coupe n'est conforme (un jeton chevauche la clé et la valeur, par exemple).
- `nombre_ecrit` : texte du premier nombre lu par `lire_cout` dans une suite du jumeau (tel que le jumeau l'a écrit).
- `reecrire_action` : toute la valeur du champ COST (du premier caractère après la coupe à la clé suivante ou à la fin de
  l'action) est remplacée par : les marques de gras qui ferment la clé (« ** » de « **COST:** »), une espace, le texte du
  nombre, puis les blancs finaux de l'ancienne valeur (le saut de ligne final est gardé). Seuls les jetons de la valeur sont
  retokenisés ; si le jeton qui finit la valeur déborde sur la clé suivante, son texte entier est retokenisé avec elle
  (compté : `jetons_cle_retokenises`). Contrôles : le décodage des nouveaux identifiants égale le nouveau texte ; le lecteur
  neuf relit exactement le nombre ; `cout_plusieurs_nombres` est faux ; le reste de l'action est égal à l'octet. Un échec
  lève `ReecritureImpossible`, que l'oracle compte (jamais avalé en silence).
"""
from __future__ import annotations

import re

from ..environnements.propositions import lire_action
from ..gardes import GardeArret
from ..harnais.formats import _ids
from ..premier_test_ia.conditions import _CLE_BRUTE, _FERMETURE_GRAS
from ..t06.cout import NOMBRE, lire_cout

_FIN_CLE_COUT = re.compile(r"COST\s*:$", re.I)
_GRAS_OUVRANT_VALEUR = re.compile(r"^[*_]{1,3}")


class ReecritureImpossible(GardeArret):
    """La réécriture d'une action n'a pas passé ses contrôles : l'oracle la compte et laisse l'action telle quelle."""


def nettoyer_fin(texte: str) -> str:
    return re.sub(r"[*_]", "", texte).rstrip()


def occurrence_cout(texte: str) -> dict | None:
    cles = list(_CLE_BRUTE.finditer(texte))
    for i, m in enumerate(cles):
        if m["cle"].upper() != "COST":
            continue
        derniere = i + 1 == len(cles)
        fin = len(texte) if derniere else cles[i + 1].start()
        valeur = texte[m.end():fin]
        if m["gras"] and not m["gras_avant"] and derniere:
            valeur = _FERMETURE_GRAS.sub("", valeur, count=1)
        if not valeur.strip():
            continue
        return {"debut_cle": m.start("cle"), "fin_valeur": fin}
    return None


def _longueurs(tok, ids: list[int]) -> list[int]:
    return [len(tok.decode(ids[:k], skip_special_tokens=True)) for k in range(len(ids) + 1)]


def coupe_prefixe(tok, ids: list[int], texte: str) -> dict:
    """Rend {"porte_cout": bool, "coupe": int | None, "motif": str | None}."""
    occ = occurrence_cout(texte)
    if occ is None:
        return {"porte_cout": False, "coupe": None, "motif": "aucun champ COST non vide"}
    if tok.decode(ids, skip_special_tokens=True) != texte:
        return {"porte_cout": True, "coupe": None, "motif": "décodage des identifiants ≠ texte de l'action"}
    longueurs = _longueurs(tok, ids)
    borne = next((k for k in range(len(ids)) if longueurs[k + 1] > occ["debut_cle"]), None)
    if borne is None:
        return {"porte_cout": True, "coupe": None, "motif": "clé COST hors des identifiants"}
    for r in range(borne + 1, len(ids) + 1):
        if longueurs[r] > occ["fin_valeur"]:
            break
        prefixe = tok.decode(ids[:r], skip_special_tokens=True)
        if not texte.startswith(prefixe):
            continue
        if _FIN_CLE_COUT.search(nettoyer_fin(prefixe)):
            return {"porte_cout": True, "coupe": r, "motif": None}
    return {"porte_cout": True, "coupe": None, "motif": "aucune coupe conforme (jeton à cheval sur la clé et la valeur)"}


def nombre_ecrit(suite: str) -> str | None:
    m = NOMBRE.search(suite or "")
    return m.group(0) if m else None


def reecrire_action(tok, ids: list[int], texte: str, coupe: int, nombre: str) -> dict:
    """Nouveaux identifiants et texte de l'action, valeur du champ COST remplacée par `nombre`."""
    if not nombre or lire_cout(nombre)["cout"] is None:
        raise ReecritureImpossible(f"nombre {nombre!r} illisible par le lecteur neuf")
    occ = occurrence_cout(texte)
    if occ is None:
        raise ReecritureImpossible("aucun champ COST")
    prefixe = tok.decode(ids[:coupe], skip_special_tokens=True)
    if not texte.startswith(prefixe) or not _FIN_CLE_COUT.search(nettoyer_fin(prefixe)):
        raise ReecritureImpossible("coupe non conforme")
    debut, fin = len(prefixe), occ["fin_valeur"]
    if fin < debut:
        raise ReecritureImpossible("valeur vide ou avant la coupe")
    valeur = texte[debut:fin]
    gras = _GRAS_OUVRANT_VALEUR.match(valeur)
    gras = gras.group(0) if gras else ""
    queue = valeur[len(valeur.rstrip()):]
    longueurs = _longueurs(tok, ids)
    s = coupe
    while s < len(ids) and longueurs[s] < fin:
        s += 1
    L = longueurs[s]
    if L < fin:
        raise ReecritureImpossible("fin de la valeur hors des identifiants")
    debordement = texte[fin:L]
    segment = gras + " " + nombre + queue + debordement
    nouveaux_ids = list(ids[:coupe]) + _ids(tok, segment) + list(ids[s:])
    nouveau_texte = prefixe + segment + texte[L:]
    if tok.decode(nouveaux_ids, skip_special_tokens=True) != nouveau_texte:
        raise ReecritureImpossible("décodage des identifiants réécrits ≠ texte réécrit")
    relu = lire_cout(lire_action(nouveau_texte).champs.get("COST"))
    attendu = lire_cout(nombre)["cout"]
    if relu["cout"] != attendu or relu["cout_plusieurs_nombres"]:
        raise ReecritureImpossible(f"relecture du champ réécrit : {relu['cout']} au lieu de {attendu}, "
                                   f"plusieurs nombres : {relu['cout_plusieurs_nombres']}")
    if nouveau_texte[:debut] != texte[:debut] or nouveau_texte[len(nouveau_texte) - (len(texte) - L):] != texte[L:]:
        raise ReecritureImpossible("le texte hors de la valeur a changé")
    return {"ids": nouveaux_ids, "texte": nouveau_texte, "valeur_remplacee": valeur, "jetons_valeur_avant": s - coupe,
            "jetons_cle_retokenises": int(bool(debordement))}
