"""Complément de `nos_lentilles_v1` pour le lanceur de la seconde passe v2 : la pièce citée par la ligne
`NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` ne nomme la lentille que par **une seule** ligne « Lentille nommée : … ».

Correction non bloquante N5 de la contre-lecture du code de la seconde passe
(`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-seconde-passe-v1.md`, `0c90e0f6…`) :
`nos_lentilles_v1.lentilles_nommees_par_le_noeud` cherche la forme « Lentille nommée : R », « Lentille nommée : S » ou
« Lentilles nommées : R et S » sur **toutes** les lignes de la pièce et réunit ce qu'elle trouve ; une citation de cette forme
ailleurs dans la pièce (un exemple, un rappel d'une autre pièce) ouvrirait donc la lecture d'une lentille que le mot de Lazar ne
nomme pas. Ici, une pièce qui porte plus d'une ligne de cette forme arrête : la forme est mal comprise.

`nos_lentilles_v1` n'est pas réécrit (R12) et reste appelé tel quel pour tout le reste. Ce module n'ajoute que :
- `lignes_qui_nomment` : les lignes de la forme, dans une pièce ;
- `exiger_une_seule_ligne_qui_nomme` : pour chaque ligne du registre que `nos_lentilles_v1` retient (postérieure, par la place et
  par l'heure, à toute ligne d'avertissement), la pièce citée porte au plus une ligne de la forme ; sinon arrêt ;
- `condition_de_lecture` : celle de `nos_lentilles_v1`, suivie de cette exigence **quand la condition a consulté la pièce**
  (une de nos lentilles au deuxième palier en ajustement seul ou en seconde course incomplète, parvenue jusqu'à la règle du nœud
  N12). Dans les autres cas la pièce n'est pas lue, comme avant.

Ce qui ne change pas : une pièce **sans aucune** ligne de la forme ne nomme aucune lentille, et la lentille reste « non lue »
(sens sévère du nœud N-dev-3, tenu par la contre-lecture) ; plusieurs lignes du registre, chacune citant une pièce d'une seule
ligne de la forme, se réunissent comme avant. Le texte décide, le code suit.
"""
from __future__ import annotations

from pathlib import Path

from . import constantes_v2 as K2
from . import nos_lentilles_v1 as nl
from .constantes_v1 import FormeMalComprise

MESSAGE_PLUSIEURS_LIGNES = ("pièce citée par {cle} ({chemin}) : {n} lignes de la forme « Lentille nommée : … » ; une seule est "
                            "attendue (une citation de cette forme ailleurs dans la pièce ouvrirait la lecture) : arrêt avant tout "
                            "calcul ; nœud (la forme est mal comprise)")


def lignes_qui_nomment(texte: str) -> list[str]:
    """Les lignes de la pièce qui ont la forme lue par `nos_lentilles_v1` (« Lentille nommée : R », « Lentille nommée : S »,
    « Lentilles nommées : R et S »), dans l'ordre de la pièce ; ce que chacune nomme (« R », « S » ou « R et S »)."""
    return [m.group(1) for m in nl.FORME_LENTILLE_NOMMEE.finditer(texte)]


def exiger_une_seule_ligne_qui_nomme(racine_depot: str | Path, etat: nl.EtatRegistre) -> dict:
    """Pour chaque ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` retenue par `nos_lentilles_v1` (même filtre : place et
    heure strictement postérieures à toute ligne d'avertissement), la pièce citée porte au plus une ligne de la forme ; plus
    d'une : arrêt, forme mal comprise. Rend `{chemin de la pièce : ce que sa ligne nomme, ou None}`."""
    avertissements = etat.presentes(K2.CLE_AVERTISSEMENT)
    releve: dict = {}
    if not avertissements:
        return releve
    place_a = max(p for p, _ in avertissements)
    heure_a = max(l.heure for _, l in avertissements)
    for place, ligne in etat.presentes(K2.CLE_NOEUD_AJUSTEMENT_SEUL):
        if not (place > place_a and ligne.heure > heure_a):
            continue
        nommees = lignes_qui_nomment(nl.lire_piece(racine_depot, ligne, K2.CLE_NOEUD_AJUSTEMENT_SEUL).decode("utf-8"))
        if len(nommees) > 1:
            raise FormeMalComprise(MESSAGE_PLUSIEURS_LIGNES.format(cle=K2.CLE_NOEUD_AJUSTEMENT_SEUL, chemin=ligne.chemin,
                                                                   n=len(nommees)))
        releve[str(ligne.chemin)] = nommees[0] if nommees else None
    return releve


def a_consulte_la_piece_du_noeud(conditions: dict) -> bool:
    """Vrai si `nos_lentilles_v1.condition_de_lecture` est parvenue, pour une lentille au moins, à la règle du nœud N12 (elle
    seule lit la pièce) : la lentille en sort lue avec la phrase « sans mesure à elle », ou non lue « sans mesure propre »."""
    for lettre in K2.NOS_LENTILLES:
        cond = conditions[lettre]
        if cond.phrase_sans_mesure or cond.motif == nl.NON_LUE.format(lettre=lettre, motif=nl.MOTIF_SANS_MESURE_PROPRE):
            return True
    return False


def condition_de_lecture(fiche: dict, etat: nl.EtatRegistre, racine_depot: str | Path) -> dict:
    """La condition de lecture de `nos_lentilles_v1`, telle quelle ; puis, si elle a consulté la pièce du nœud N12, l'exigence
    d'une seule ligne « Lentille nommée : … » par pièce. Rend ce que `nos_lentilles_v1.condition_de_lecture` rend."""
    conditions = nl.condition_de_lecture(fiche, etat, racine_depot)
    if a_consulte_la_piece_du_noeud(conditions):
        exiger_une_seule_ligne_qui_nomme(racine_depot, etat)
    return conditions
