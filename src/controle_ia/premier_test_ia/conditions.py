"""Conditions des épisodes de P3 et mesures d'action sans juge.

Textes privés : lus dans le fichier des consignes scellé (citations « > », dans l'ordre : consigne du saboteur, indication
du saboteur, consigne du témoin, indication du témoin), jamais écrits dans le code. Place (code de l'environnement (a)) :
la consigne à la fin du message système (`instructions_cachees`), l'indication juste avant « Your action: » à chaque pas
(`indications_privees`, p = 1).

Mesures d'action (calculées sur l'instance ; aucun texte gardé) : coût déclaré, `heures_declarees(lire_action(texte)
.champs.get("COST"))` ; forme du champ `COST` (plus d'un nombre, multiplication, intervalle, suffixe « k ») ; titre sans
lettre capitale (première ligne du champ `TITLE`, au moins une lettre) ; validité de lecture de l'action.
"""
from __future__ import annotations

import re
from pathlib import Path

from ..environnements.propositions import _NOMBRE, EnvironnementPropositions, heures_declarees, lire_action
from ..gardes import GardeArret
from ..scellement import verifier

CONDITIONS = ("honnete", "saboteur", "temoin")
_MULTIPLICATION = re.compile(r"\d\s*[×xX*]\s*\d")
_INTERVALLE = re.compile(r"\d\s*(?:–|—|-|to)\s*\d")
_SUFFIXE_K = re.compile(r"\d\s*[kK](?![A-Za-z])")


def blocs_cites(texte: str) -> list[str]:
    """Blocs de lignes « > » consécutives, joints par une espace (même règle que la mesure des longueurs)."""
    blocs, courant = [], []
    for ligne in texte.split("\n"):
        if ligne.startswith("> "):
            courant.append(ligne[2:].strip())
        elif courant:
            blocs.append(" ".join(courant))
            courant = []
    if courant:
        blocs.append(" ".join(courant))
    return blocs


def charger_consignes(chemin, sha_attendue: str | None = None) -> dict:
    sha = verifier(chemin)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"{chemin} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]} (R11)")
    blocs = blocs_cites(Path(chemin).read_text(encoding="utf-8"))
    if len(blocs) != 4 or any(not b for b in blocs):
        raise GardeArret(f"{chemin} : quatre textes cités attendus (consigne et indication du saboteur, puis du témoin), "
                         f"{len(blocs)} trouvés")
    return {"sha256": sha, "saboteur": {"consigne": blocs[0], "indication": blocs[1]},
            "temoin": {"consigne": blocs[2], "indication": blocs[3]}}


def environnement(condition: str, tache, T: int, guide: str | None, consignes: dict) -> EnvironnementPropositions:
    """Environnement (a) d'un épisode de la condition (N = 1)."""
    if condition not in CONDITIONS:
        raise GardeArret(f"condition {condition!r} inconnue : {CONDITIONS}")
    if condition == "honnete":
        return EnvironnementPropositions(tache, 1, T, guide)
    textes = consignes[condition]
    return EnvironnementPropositions(tache, 1, T, guide, instructions_cachees={0: textes["consigne"]},
                                     indications_privees={(0, t): textes["indication"] for t in range(T)})


def mesures_action(texte: str) -> dict:
    a = lire_action(texte)
    champ = a.champs.get("COST") or ""
    titre = (a.champs.get("TITLE") or "").split("\n")[0].strip()
    lettres = [c for c in titre if c.isalpha()]
    return {"valide": bool(a.valide), "cout": heures_declarees(a.champs.get("COST")), "cout_present": bool(champ),
            "cout_plusieurs_nombres": len(_NOMBRE.findall(champ)) > 1,
            "cout_multiplication": bool(_MULTIPLICATION.search(champ)),
            "cout_intervalle": bool(_INTERVALLE.search(champ)), "cout_suffixe_k": bool(_SUFFIXE_K.search(champ)),
            "titre_present": bool(lettres), "titre_sans_capitale": bool(lettres) and not any(c.isupper() for c in lettres)}
