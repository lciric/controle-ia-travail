"""Lire un coût sur la fenêtre commune, v5 (texte scellé de l'organisme retenu, section 3.2 points 2 et 4 ; section 13).

Une seule fonction, `lire_fenetre`, lit la fenêtre du coût déclaré d'une action (ses jetons après la coupe) et une suite du
jumeau : les 16 premiers jetons, arrêtés à la fin de tour, décodés, coupés au premier saut de ligne ; premier nombre par le
lecteur du coût de T0.6 (`t06.cout.lire_cout`) ; lisible si fini et strictement positif. **Nombre au bord** : si la fenêtre
atteint sa limite sans saut de ligne ni fin de tour et que seuls des caractères pouvant prolonger le nombre (chiffres, espaces,
virgule, point, « k ») le séparent de la fin, elle est illisible.

`coupe_du_prefixe` : coupe juste après « COST: », **fonction du seul préfixe** : le plus petit rang r dont le décodage des r
premiers jetons finit par la première clé COST de l'action (espaces et tabulations permis après les deux-points). La valeur qui
suit n'entre pas dans la décision : « COST: » suivi aussitôt de la clé suivante a une coupe conforme et une fenêtre illisible.

`lire_action_v5` : coupe, fenêtre du coût déclaré, valeur de l'ancien lecteur du champ entier (`t06.cout.cout_action`) et
`ecart_des_deux_lecteurs`. Aucun texte n'est rendu : seulement des valeurs, des booléens et des codes de motif.
"""
from __future__ import annotations

import re

from ..gardes import GardeArret
from ..t06.cout import NOMBRE, cout_action, cout_lisible, lire_cout

FENETRE = 16
FORMES = ("champ_present", "plusieurs_nombres", "multiplication", "intervalle", "suffixe_k", "milliers_espace", "unite_presente")
CLES_LECTURE = frozenset({"valeur", "lisible", "vide", "tronquee", "nombre_au_bord", "n_jetons", "formes"})
MOTIFS_COUPE = ("champ_absent", "decodage_infidele", "chevauchement_cle_valeur")
_CLE_COST = re.compile(r"(?:^|\n)[ \t]*[*_]{0,3}COST[*_]{0,3}[ \t]*:", re.I)
_FIN_DE_CLE = re.compile(r"(?:^|\n)[ \t]*[*_]{0,3}COST[*_]{0,3}[ \t]*:[ \t]*\Z", re.I)
_PROLONGE = frozenset("0123456789 \t  ,.kK")
_UNITE = re.compile(r"[ \t  ]*-?[ \t  ]*[A-Za-zµ]")


def lire_fenetre(tok, ids, fins=frozenset(), limite: int = FENETRE) -> dict:
    """Lecture d'une fenêtre de jetons (fin d'action après la coupe, ou suite du jumeau) ; même fonction pour les deux."""
    ids = list(ids)
    garde = ids[:limite]
    fin_de_tour = False
    for i, j in enumerate(garde):
        if j in fins:
            garde, fin_de_tour = garde[:i], True
            break
    texte = tok.decode(garde, skip_special_tokens=True)
    saut = "\n" in texte
    ligne = texte.split("\n", 1)[0]
    tronquee = len(ids) >= limite and not fin_de_tour and not saut
    lu = lire_cout(ligne)
    m = NOMBRE.search(ligne)
    au_bord = bool(tronquee and m is not None and all(c in _PROLONGE for c in ligne[m.end():]))
    valeur = lu["cout"]
    lisible = bool(cout_lisible(valeur) and not au_bord)
    return {"valeur": float(valeur) if lisible else None, "lisible": lisible, "vide": not ligne.strip(" \t*_"),
            "tronquee": bool(tronquee), "nombre_au_bord": au_bord, "n_jetons": len(garde),
            "formes": {"champ_present": bool(ligne.strip(" \t*_")), "plusieurs_nombres": bool(lu["cout_plusieurs_nombres"]),
                       "multiplication": bool(lu["cout_multiplication"]), "intervalle": bool(lu["cout_intervalle"]),
                       "suffixe_k": bool(lu["cout_suffixe_k"]), "milliers_espace": bool(lu["cout_milliers_espace"]),
                       "unite_presente": bool(m is not None and _UNITE.match(ligne, m.end()))}}


def coupe_du_prefixe(tok, ids) -> dict:
    """Coupe du préfixe d'action juste après la première clé COST ; `champ_cout` : la clé est présente dans l'action."""
    ids = list(ids)
    texte = tok.decode(ids, skip_special_tokens=True)
    cle = _CLE_COST.search(texte)
    if cle is None:
        return {"champ_cout": False, "conforme": False, "rang": None, "motif": "champ_absent"}
    for r in range(1, len(ids) + 1):
        d = tok.decode(ids[:r], skip_special_tokens=True)
        if len(d) < cle.end():
            continue
        if d != texte[:len(d)]:
            return {"champ_cout": True, "conforme": False, "rang": None, "motif": "decodage_infidele"}
        if _FIN_DE_CLE.search(d) and len(d.rstrip(" \t")) == cle.end():
            return {"champ_cout": True, "conforme": True, "rang": r, "motif": None}
        return {"champ_cout": True, "conforme": False, "rang": None, "motif": "chevauchement_cle_valeur"}
    return {"champ_cout": True, "conforme": False, "rang": None, "motif": "decodage_infidele"}


def lire_action_v5(tok, ids, fins=frozenset(), limite: int = FENETRE) -> dict:
    """Coupe (sur le seul préfixe), fenêtre du coût déclaré, ancien lecteur du champ entier, écart des deux lecteurs."""
    ids = list(ids)
    coupe = coupe_du_prefixe(tok, ids)
    fenetre = lire_fenetre(tok, ids[coupe["rang"]:], fins, limite) if coupe["conforme"] else None
    ancien = cout_action(tok.decode(ids, skip_special_tokens=True))["cout"]
    ancien = float(ancien) if cout_lisible(ancien) else None
    neuf = fenetre["valeur"] if fenetre is not None else None
    return {"coupe": coupe, "fenetre": fenetre, "cout_declare": neuf, "cout_lisible": neuf is not None,
            "ancien_lecteur": ancien, "ecart_des_deux_lecteurs": ancien != neuf}


def exiger_lecture(l) -> None:
    """Forme exacte d'une lecture (fenêtre ou suite) : sinon arrêt (aucun texte, aucune clé de plus)."""
    if not isinstance(l, dict) or set(l) != CLES_LECTURE or set(l["formes"]) != set(FORMES):
        raise GardeArret("lecture de fenêtre hors du schéma (clés ou formes)")
    if l["lisible"] != (l["valeur"] is not None) or any(not isinstance(v, bool) for v in l["formes"].values()):
        raise GardeArret("lecture de fenêtre incohérente (valeur, lisibilité ou formes)")
