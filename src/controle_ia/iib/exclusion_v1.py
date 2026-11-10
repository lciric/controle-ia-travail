"""Actions hors de la perte de distillation de (ii-b) (conception 5.1 ; exception déclarée à « le texte n'est pas filtré »
de P-066, qui vise le choix des épisodes). Règle mécanique fixée avant tout tirage, identique pour l'élève et le
témoin-jumeau ; l'action exclue reste dans le contexte des suivantes ; un épisode n'est jamais rejeté par cette règle (il
est accepté ou non par la seule règle d'acceptation) ; un épisode dont toutes les actions sont exclues n'a aucune cible et
ne contribue à aucune perte (compté).

Motifs d'exclusion, comptés par motif :
- `t06:<phrase>` : `t06.test_croise.MENTIONS_ETENDUES` (motifs de T0.6), la phrase trouvée en minuscules ;
- `iib:<motif>` : les motifs de la consigne scellée de (ii-b) (`consigne_v1`), un compte par motif ;
- `non_bornable_a_champ_cout` : action qui porte un champ COST et n'est pas bornable selon l'oracle (R1 ne la borne pas) ;
- `reecriture_impossible` : action qui a une estimation honnête mais dont la valeur n'a pas pu être réécrite (le nombre du
  maître resterait dans le témoin-jumeau) — ajout du développeur, déclaré, lu sur l'oracle seul.
"""
from __future__ import annotations

from ..gardes import GardeArret
from ..t06.test_croise import MENTIONS_ETENDUES
from .consigne_v1 import compiler_motifs


def motifs_de_l_action(texte: str, motifs_iib) -> list[str]:
    trouves = [f"t06:{m.group(0).lower()}" for m in MENTIONS_ETENDUES.finditer(texte)]
    trouves += [f"iib:{nom}" for nom, rx in motifs_iib if rx.search(texte)]
    return sorted(set(trouves))


def actions_gardees(textes: list[str], lignes_oracle: list[dict], motifs: list[str]) -> dict:
    if len(textes) != len(lignes_oracle):
        raise GardeArret(f"exclusion : {len(textes)} textes pour {len(lignes_oracle)} lignes d'oracle")
    rx = compiler_motifs(motifs)
    gardees, comptes, par_action = [], {}, []
    for k, (texte, l) in enumerate(zip(textes, lignes_oracle)):
        raisons = motifs_de_l_action(texte, rx)
        if l["porte_cout"] and not l["bornable"]:
            raisons.append("non_bornable_a_champ_cout")
        if l["a_estimation"] and not l["reecrite"]:
            raisons.append("reecriture_impossible")
        for r in raisons:
            comptes[r] = comptes.get(r, 0) + 1
        par_action.append(raisons)
        if not raisons:
            gardees.append(k)
    return {"gardees": gardees, "comptes": comptes, "raisons": par_action}


def faux_positifs(textes_honnetes: list[str], motifs: list[str], seuil_reserve: float = 0.02) -> dict:
    """Taux de correspondance de chaque motif de (ii-b) sur des actions honnêtes (aucun texte privé n'y existe : toute
    correspondance est un faux positif) ; au-delà de 2 % pour un motif : réserve écrite (pas un arrêt)."""
    n = len(textes_honnetes)
    taux = {nom: (sum(bool(r.search(t)) for t in textes_honnetes) / n if n else None) for nom, r in compiler_motifs(motifs)}
    return {"actions": n, "taux": taux, "reserves": sorted(m for m, v in taux.items() if v is not None and v > seuil_reserve)}
