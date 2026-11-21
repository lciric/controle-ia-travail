"""Remplacer la valeur du coût dans une action, v5 (texte scellé, section 3.3 c et d, section 10.1 ; section 13).

Sert à l'oracle à contexte réécrit, aux deux témoins, à l'épisode régénéré et à l'excès planté.

`remplacer_valeur(tok, ids, rang_coupe, suite_ids, fins)` — le texte de l'action, de la coupe jusqu'à la fin du cœur de la
valeur (jusqu'à la clé suivante, lignes comprises, espaces et sauts de ligne de fin exclus), est remplacé par le texte de la
suite (nombre, unité, multiplicateur), sans rien ajouter ni retirer en tête, ses espaces et sauts de ligne de fin retirés ; une
suite vide retire la valeur. Les espaces et sauts de ligne de fin de la valeur d'origine sont gardés ; s'il n'y en avait pas et
qu'une clé suit, un saut de ligne est inséré (`separateur_insere`). Les marques de gras fermées après les deux-points restent à
la clé : la suite prend place après elles, sauf si elle porte elle-même ces marques en tête (elle a été tirée après la coupe,
donc avant elles) — elle prend alors place à la coupe, et la clé reste fermée une seule fois (lecture déclarée au rapport).
Jetons : les identifiants de la suite sont collés tels quels ; seuls le séparateur et les morceaux de jetons à cheval sont
retokenisés. Le décodage du tout doit redonner le texte attendu (sinon retokenisation élargie à la fin de l'action, comptée ;
sinon arrêt), et la lecture de l'action réécrite doit rendre les mêmes champs que l'originale, au coût près ; sinon arrêt.

`multiplier_cout(tok, ids, rang_coupe, delta, fins)` — le premier nombre de la fenêtre du coût est multiplié par 10^δ et écrit
dans la forme de l'original (même séparateur de milliers, quatre chiffres significatifs au plus, suffixe « k » gardé) ; tout
le reste de l'action est égal à l'octet. δ = 0 : l'action est rendue telle quelle.
"""
from __future__ import annotations

import math
import re

from ..environnements.propositions import lire_action
from ..gardes import GardeArret
from ..premier_test_ia.conditions import _CLE_BRUTE
from ..t06.cout import ESPACES, NOMBRE, valeur_du_nombre
from .lecture_cout_v5 import FENETRE

_FERMETURE = re.compile(r"[*_]{1,3}")
_MARQUES_EN_TETE = re.compile(r"[ \t]*[*_]")
CHIFFRES_SIGNIFICATIFS = 4


def _longueurs(tok, ids: list[int]) -> list[int]:
    return [0] + [len(tok.decode(ids[:k + 1], skip_special_tokens=True)) for k in range(len(ids))]


def _ids(tok, texte: str) -> list[int]:
    return list(tok(texte, add_special_tokens=False)["input_ids"]) if texte else []


def bornes_de_la_valeur(texte: str, p_coupe: int) -> tuple[int, int, int]:
    """(début de la valeur après les marques de gras de la clé, fin du cœur, fin de la valeur), la coupe étant à `p_coupe`."""
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


def separateur(texte: str, coeur_fin: int, v_fin: int) -> tuple[str, bool]:
    """Espaces et sauts de ligne de fin de la valeur d'origine ; s'il n'y en a pas et qu'une clé suit, un saut de ligne inséré."""
    sep = texte[coeur_fin:v_fin]
    if not sep and v_fin < len(texte):
        return "\n", True
    return sep, False


def texte_de_suite(tok, suite_ids, fins=frozenset(), limite: int = FENETRE) -> str:
    """Texte d'une suite tel qu'il entre dans une réécriture : fenêtre, arrêt à la fin de tour, premier saut de ligne, sans fin."""
    garde = list(suite_ids)[:limite]
    for i, j in enumerate(garde):
        if j in fins:
            garde = garde[:i]
            break
    return tok.decode(garde, skip_special_tokens=True).split("\n", 1)[0].rstrip()


def exiger_memes_champs(avant: str, apres: str) -> None:
    """La lecture de l'action réécrite rend les mêmes champs que l'originale, au coût près ; sinon arrêt."""
    a, b = lire_action(avant), lire_action(apres)
    ca = {k: v for k, v in a.champs.items() if k != "COST"}
    cb = {k: v for k, v in b.champs.items() if k != "COST"}
    if ca != cb or a.operation != b.operation or a.numero != b.numero:
        raise GardeArret("réécriture : la lecture de l'action réécrite ne rend pas les mêmes champs que l'originale, au coût près (arrêt)")


def _coller(tok, ids, lg, texte, neuf_texte, debut, fin, milieu_ids, tete, queue) -> tuple[list[int], bool]:
    """Remplace les caractères [debut, fin) : jetons d'avant et d'après collés tels quels, `milieu_ids` collés tels quels,
    `tete` et `queue` retokenisés ; élargit la retokenisation à la fin de l'action si le décodage ne redonne pas le texte."""
    s = max(k for k in range(len(ids) + 1) if lg[k] <= debut)
    e = min(k for k in range(s, len(ids) + 1) if lg[k] >= fin)
    neuf = list(ids[:s]) + _ids(tok, texte[lg[s]:debut] + tete) + list(milieu_ids) + _ids(tok, queue + texte[fin:lg[e]]) + list(ids[e:])
    if tok.decode(neuf, skip_special_tokens=True) == neuf_texte:
        return neuf, False
    fin_texte = min(k for k in range(len(ids) + 1) if lg[k] >= len(texte))
    neuf = list(ids[:s]) + _ids(tok, neuf_texte[lg[s]:]) + list(ids[fin_texte:])
    if tok.decode(neuf, skip_special_tokens=True) != neuf_texte:
        raise GardeArret("réécriture : le texte réécrit ne se retrouve pas au décodage, même retokenisé jusqu'à la fin de l'action (arrêt)")
    return neuf, True


def remplacer_valeur(tok, ids, rang_coupe: int, suite_ids, fins=frozenset(), limite: int = FENETRE) -> dict:
    ids = list(ids)
    texte = tok.decode(ids, skip_special_tokens=True)
    lg = _longueurs(tok, ids)
    if isinstance(rang_coupe, bool) or not isinstance(rang_coupe, int) or not 0 < rang_coupe <= len(ids):
        raise GardeArret(f"réécriture : rang de coupe {rang_coupe!r} hors de l'action ({len(ids)} jetons)")
    p = lg[rang_coupe]
    v0, coeur_fin, v_fin = bornes_de_la_valeur(texte, p)
    suite_ids = list(suite_ids or [])
    coeur = texte_de_suite(tok, suite_ids, fins, limite)
    debut = p if (v0 > p and _MARQUES_EN_TETE.match(coeur)) else v0
    sep, insere = separateur(texte, coeur_fin, v_fin)
    neuf_texte = texte[:debut] + coeur + sep + texte[v_fin:]
    m = 0
    for k in range(1, len(suite_ids) + 1):
        d = tok.decode(suite_ids[:k], skip_special_tokens=True)
        if len(d) <= len(coeur) and coeur.startswith(d) and suite_ids[k - 1] not in fins:
            m = k
        else:
            break
    colle = tok.decode(suite_ids[:m], skip_special_tokens=True) if m else ""
    neuf, elargie = _coller(tok, ids, lg, texte, neuf_texte, debut, v_fin, suite_ids[:m], "", coeur[len(colle):] + sep)
    exiger_memes_champs(texte, neuf_texte)
    return {"ids": neuf, "texte": neuf_texte, "separateur_insere": insere, "valeur_origine_plusieurs_lignes": "\n" in texte[v0:coeur_fin],
            "jetons_de_suite_colles": m, "elargie": elargie, "a_la_coupe": debut == p and v0 > p}


def ecrire_nombre(valeur: float, original: str) -> str:
    """Écrit `valeur` dans la forme du nombre `original` : même séparateur de milliers, quatre chiffres significatifs au plus."""
    if not (math.isfinite(valeur) and valeur > 0):
        raise GardeArret(f"nombre à écrire illisible ({valeur!r})")
    e = math.floor(math.log10(valeur))
    arrondi = round(valeur, CHIFFRES_SIGNIFICATIFS - 1 - e)
    decimales = max(0, CHIFFRES_SIGNIFICATIFS - 1 - math.floor(math.log10(arrondi)))
    milliers_espace = re.search(rf"\d{ESPACES}\d{{3}}", original)
    milliers_virgule = re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", original)
    virgule_decimale = bool(not milliers_virgule and re.search(r",\d", original))
    if virgule_decimale and decimales >= 3:
        decimales = 2                                   # « 1,256 » serait relu comme un millier : deux décimales au plus
    brut = f"{arrondi:.{decimales}f}"
    entier, _, frac = brut.partition(".")
    frac = frac.rstrip("0")
    if milliers_espace or milliers_virgule:
        sep = milliers_espace.group(0)[1] if milliers_espace else ","
        groupes = []
        while len(entier) > 3:
            groupes.insert(0, entier[-3:])
            entier = entier[:-3]
        entier = sep.join([entier] + groupes)
    if not frac:
        return entier
    return entier + ("," if virgule_decimale else ".") + frac


def multiplier_cout(tok, ids, rang_coupe: int, delta: float, fins=frozenset(), limite: int = FENETRE) -> dict:
    """Multiplie par 10^δ le premier nombre de la fenêtre du coût ; rend l'action (jetons, texte) et la valeur écrite."""
    ids = list(ids)
    texte = tok.decode(ids, skip_special_tokens=True)
    if delta == 0:
        return {"ids": ids, "texte": texte, "valeur_ecrite": None, "elargie": False, "multipliee": False}
    lg = _longueurs(tok, ids)
    if isinstance(rang_coupe, bool) or not isinstance(rang_coupe, int) or not 0 < rang_coupe <= len(ids):
        raise GardeArret(f"multiplication : rang de coupe {rang_coupe!r} hors de l'action")
    p = lg[rang_coupe]
    garde = ids[rang_coupe:rang_coupe + limite]
    for i, j in enumerate(garde):
        if j in fins:
            garde = garde[:i]
            break
    ligne = tok.decode(garde, skip_special_tokens=True).split("\n", 1)[0]
    if texte[p:p + len(ligne)] != ligne:
        raise GardeArret("multiplication : la fenêtre du coût ne se retrouve pas dans le texte de l'action (arrêt)")
    m = NOMBRE.search(ligne)
    if m is None:
        raise GardeArret("multiplication : aucun nombre dans la fenêtre du coût (l'appelant ne multiplie qu'un coût lisible)")
    facteur_k = 1000.0 if m["k"] else 1.0
    cible = valeur_du_nombre(m["n"], m["k"]) * 10.0 ** float(delta)
    ecrit = ecrire_nombre(cible / facteur_k, m["n"])
    a, b = p + m.start("n"), p + m.end("n")
    neuf_texte = texte[:a] + ecrit + texte[b:]
    relu = NOMBRE.search(neuf_texte[p:].split("\n", 1)[0])
    valeur = valeur_du_nombre(relu["n"], relu["k"]) if relu is not None else None
    tolerance = 0.006 if re.search(r",\d", m["n"]) and not re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", m["n"]) else 0.00051
    if valeur is None or abs(valeur / cible - 1.0) > tolerance:
        raise GardeArret(f"multiplication : le nombre relu ({valeur!r}) n'est pas la valeur d'origine × 10^δ à l'arrondi près ({cible!r})")
    neuf, elargie = _coller(tok, ids, lg, texte, neuf_texte, a, b, [], ecrit, "")
    exiger_memes_champs(texte, neuf_texte)
    return {"ids": neuf, "texte": neuf_texte, "valeur_ecrite": float(valeur), "elargie": elargie, "multipliee": True}
