"""Témoin-jumeau de (ii-b), v1 : réécriture de la valeur entière du champ COST (décision M4 de la mère ; conception 2.2 point 1,
5.2, section 10, `iib/temoin_jumeau_v1.py`). Fonction partagée avec le contexte réécrit de l'oracle (`oracle_v1`).

`reecrire_valeur_cout(tok, ids, texte, rang_coupe, texte_nombre)` : dans une action dont la coupe est conforme (`rang_coupe` :
rang du premier jeton qui suit `COST:`, rendu par `oracle_v1.coupe_du_prefixe`), **toute la valeur** du champ COST — du premier
jeton qui suit `COST:` jusqu'à la clé suivante (ligne ACTION comprise, comme `lire_action`) ou à la fin de l'action — est
remplacée par une espace et `texte_nombre` (le texte du nombre de la médiane basse tel que le jumeau l'a écrit) ; les espaces
de fin de la valeur, saut de ligne final compris, sont gardés. Si la clé est ouverte en gras et fermée après les deux-points
(« **COST:** »), les marques de fermeture qui suivent la coupe appartiennent à la clé, non à la valeur : elles restent (sans
elles, `lire_action` ne lirait plus le champ). Seuls les jetons qui portent la valeur sont retokenisés ; ceux d'avant et
d'après sont collés tels quels ; un jeton qui chevauche la valeur et ce qui la suit (« )\\n ») est retokenisé avec elle
(compté : `chevauchement`). Si le collage ne redonne pas le texte attendu au décodage, la retokenisation est élargie à la fin de
l'action (comptée : `elargie`) ; si l'élargie échoue aussi, arrêt. Rend les identifiants et le texte neufs.

`transcription_temoin_jumeau(fmt, env_honnete, actions_reecrites)` : la transcription du témoin-jumeau est la transcription
honnête (`t06.distillation_transcription.transcription_honnete`) autour des actions réécrites : c'est le contexte réécrit de
l'oracle.
"""
from __future__ import annotations

import re

from ..gardes import GardeArret
from ..premier_test_ia.conditions import _CLE_BRUTE
from ..t06 import distillation_transcription as dt

_FERMETURE = re.compile(r"[*_]{1,3}")


def _longueurs(tok, ids: list[int]) -> list[int]:
    """longueurs[k] = longueur du décodage cumulé des k premiers jetons (décodage cumulé, comme `bornes_champs`)."""
    return [0] + [len(tok.decode(ids[:k + 1], skip_special_tokens=True)) for k in range(len(ids))]


def _ids(tok, texte: str) -> list[int]:
    return list(tok(texte, add_special_tokens=False)["input_ids"])


def bornes_de_la_valeur(texte: str, p_coupe: int) -> tuple[int, int, int]:
    """(début de la valeur, fin du cœur de la valeur, fin de la valeur) en caractères, la coupe étant à `p_coupe`."""
    cle = None
    for m in _CLE_BRUTE.finditer(texte):
        if m["cle"].upper() == "COST" and m.end() <= p_coupe:
            cle = m
    if cle is None:
        raise GardeArret("réécriture : aucune clé COST avant la coupe")
    v0 = p_coupe
    if cle["gras"] and not cle["gras_avant"]:
        f = _FERMETURE.match(texte, v0)
        if f is not None:
            v0 = f.end()
    v_fin = next((m.start() for m in _CLE_BRUTE.finditer(texte) if m.start() >= v0), len(texte))
    coeur_fin = v0 + len(texte[v0:v_fin].rstrip())
    return v0, coeur_fin, v_fin


def reecrire_valeur_cout(tok, ids: list[int], texte: str, rang_coupe: int, texte_nombre: str) -> dict:
    if not texte_nombre or not texte_nombre.strip() or "\n" in texte_nombre:
        raise GardeArret(f"réécriture : texte du nombre illisible {texte_nombre!r}")
    lg = _longueurs(tok, ids)
    if tok.decode(ids, skip_special_tokens=True) != texte:
        raise GardeArret("réécriture : le décodage des identifiants ne rend pas le texte de l'action")
    if not 0 < rang_coupe <= len(ids):
        raise GardeArret(f"réécriture : rang de coupe {rang_coupe} hors de l'action ({len(ids)} jetons)")
    v0, coeur_fin, _ = bornes_de_la_valeur(texte, lg[rang_coupe])
    neuf_texte = texte[:v0] + " " + texte_nombre.strip() + texte[coeur_fin:]
    s = max(k for k in range(rang_coupe, len(ids) + 1) if lg[k] <= v0)
    e = min(k for k in range(s, len(ids) + 1) if lg[k] >= coeur_fin)
    segment = texte[lg[s]:v0] + " " + texte_nombre.strip() + texte[coeur_fin:lg[e]]
    neuf = list(ids[:s]) + _ids(tok, segment) + list(ids[e:])
    elargie = False
    if tok.decode(neuf, skip_special_tokens=True) != neuf_texte:
        fin_texte = min(k for k in range(len(ids) + 1) if lg[k] >= len(texte))
        neuf = list(ids[:s]) + _ids(tok, neuf_texte[lg[s]:]) + list(ids[fin_texte:])
        elargie = True
        if tok.decode(neuf, skip_special_tokens=True) != neuf_texte:
            raise GardeArret("réécriture : le texte réécrit ne se retrouve pas au décodage, même retokenisé jusqu'à la fin de l'action")
    return {"ids": neuf, "texte": neuf_texte, "jetons_remplaces": e - s, "jetons_neufs": len(neuf) - s - (len(ids) - e) if not elargie else None,
            "chevauchement": lg[s] < v0 or lg[e] > coeur_fin, "elargie": elargie}


def transcription_temoin_jumeau(fmt, env_honnete, actions_reecrites: list[list[int]]):
    """Identifiants et empans de la transcription du témoin-jumeau (contexte honnête, actions réécrites)."""
    return dt.transcription_honnete(fmt, env_honnete, actions_reecrites)
