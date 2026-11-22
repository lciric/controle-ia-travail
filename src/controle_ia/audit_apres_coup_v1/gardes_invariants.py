"""Les gardes des quatre invariants (rang 8 ; section 6). Fonctions pures du journal et des rejeux appariés.

| Invariant | Garde |
| Audit après coup | l'horloge de U_i est postérieure à la fin ; l'oracle lit une copie de même empreinte que
  l'enregistrement ; la vue de l'agent est identique à l'octet sur deux rejeux appariés, pièce forcée « audité » et
  « non audité », jusqu'au premier instant d'alarme des deux rejeux |
| Plancher indépendant du score | toute ligne porte π_i ≥ π_min > 0, consignée ; les tirages de source « plancher »
  sont invariants par permutation des scores |
| Part selon l'enjeu | l'enjeu est écrit avant le début ; la part vaut β·s_i/s̄ au bit près ; des enjeux égaux sont
  déclarés tels |
| Aucun retour à l'agent | jusqu'au plus tôt des instants d'alarme du rejeu d'origine et du rejeu permuté, la vue de
  l'agent est invariante à l'octet par permutation des verdicts et des scores |

La quatrième garde applique la lettre en vigueur : aucune correction observable par l'agent avant l'alarme. Aucun bras
« correction tirée au hasard » n'est écrit. Ces gardes réfutent ; elles n'attestent pas : un canal hors journal leur
échappe.
"""
from __future__ import annotations

from typing import Callable

import numpy as np

from ..gardes import GardeArret
from .alerte import alerte_signature
from .graines import empreinte_octets, generateur_auxiliaire
from .journal import Journal
from .regle_audit import ETIQUETTE_SANS_PLANCHER, RegleAudit
from .simulateur import Resultat, simuler

INFINI = np.iinfo(np.int64).max


# ------------------------------------------------------------------------------------------------
# Vue de l'agent et canaux de retour (les canaux ne servent qu'aux artefacts)
# ------------------------------------------------------------------------------------------------
def vues_agent(res: Resultat, canal_retour: Callable[[Resultat], list[str]] | None = None) -> list[bytes]:
    """Ce que l'agent voit au début de chaque épisode : son rang, son enjeu, sa lisibilité ; plus, pour un artefact,
    ce qu'un canal de retour lui montrerait. Le harnais simulé n'a, par défaut, aucun canal de retour."""
    e = res.journal.colonne("episode")
    s = res.journal.colonne("enjeu")
    lis = res.verite.lisibilite
    extra = canal_retour(res) if canal_retour is not None else [""] * len(e)
    return [f"{int(i)}|{float(si)!r}|{float(li)!r}|{x}".encode() for i, si, li, x in zip(e, s, lis, extra)]


def canal_latence_selon_piece(res: Resultat) -> list[str]:
    """Artefact : un champ de latence qui dépend de la pièce (l'épisode suivant un audit démarre plus tard)."""
    a = res.journal.colonne("audite")
    return ["latence=1"] + [f"latence={2 if x else 1}" for x in a[:-1]]


def canal_relance_sur_audit(res: Resultat) -> list[str]:
    """Artefact : une relance de l'agent déclenchée par chaque verdict « sain » déjà lisible (correction observable
    avant l'alarme)."""
    hd = res.journal.colonne("h_debut")
    v = res.journal.colonne("v_verdict")
    hv = res.journal.colonne("v_h_verdict")
    hs = np.sort(hv[v == 0])
    k = np.searchsorted(hs, hd, side="left")
    return [f"relances={int(x)}" for x in k]


# ------------------------------------------------------------------------------------------------
# Rejeux appariés
# ------------------------------------------------------------------------------------------------
def rejeu_piece_forcee(monde, regle, oracle, tache: int, n: int, audite: bool) -> Resultat:
    """Rejeu apparié où la pièce est forcée : U_i = 0 (audité) ou U_i juste sous 1 (non audité, sauf π_i = 1)."""
    valeur = 0.0 if audite else np.nextafter(1.0, 0.0)

    def t(u):
        u["piece"] = np.full_like(u["piece"], valeur)
        return u

    return simuler(monde, regle, oracle, tache, n, transformer_uniformes=t)


def rejeu_permute(monde, regle, oracle, tache: int, n: int, cle_permutation: int,
                  canaux: tuple[str, ...] = ("score", "oracle"), **kw) -> Resultat:
    """Rejeu où les uniformes des canaux nommés (scores, verdicts) sont permutés entre épisodes ; les autres canaux,
    dont la pièce, restent identiques à l'octet."""
    perm = generateur_auxiliaire(monde.entropie, monde.identifiant, tache, cle_permutation).permutation(n)

    def t(u):
        for c in canaux:
            u[c] = u[c][perm]
        return u

    return simuler(monde, regle, oracle, tache, n, transformer_uniformes=t, **kw)


def instant_alarme(res: Resultat) -> int:
    h = alerte_signature(res.journal)
    return INFINI if h is None else h


# ------------------------------------------------------------------------------------------------
# Gardes
# ------------------------------------------------------------------------------------------------
def garde_vues_identiques(vues_a: list[bytes], vues_b: list[bytes], h_debut: np.ndarray, limite: int, nom: str) -> int:
    """Compare à l'octet les vues des épisodes commencés avant `limite` ; rend le nombre d'épisodes comparés."""
    n = int(np.sum(np.asarray(h_debut) < limite))
    if len(vues_a) < n or len(vues_b) < n:
        raise GardeArret(f"{nom} : rejeux de longueurs insuffisantes")
    for i in range(n):
        if vues_a[i] != vues_b[i]:
            raise GardeArret(f"{nom} : la vue de l'agent diffère à l'épisode {i} avant l'alarme")
    return n


def garde_audit_apres_coup(journal: Journal) -> None:
    if np.any(journal.colonne("h_piece") <= journal.colonne("h_fin")):
        raise GardeArret("audit après coup : un uniforme de la pièce tiré avant la fin de l'épisode")


def garde_copie_oracle(empreintes_enregistrement: list[str], empreintes_lues: list[str]) -> None:
    if len(empreintes_enregistrement) != len(empreintes_lues):
        raise GardeArret("audit après coup : l'oracle n'a pas lu une copie par épisode audité")
    for i, (a, b) in enumerate(zip(empreintes_enregistrement, empreintes_lues)):
        if a != b:
            raise GardeArret(f"audit après coup : l'oracle lit une copie d'empreinte différente (rang {i})")


def empreintes_enregistrements(res: Resultat) -> list[str]:
    """Empreinte de l'enregistrement de chaque épisode audité (ce que l'agent a produit : ici rang, enjeu, lisibilité
    et dommage planté)."""
    a = np.flatnonzero(res.journal.colonne("audite"))
    s = res.journal.colonne("enjeu")
    return [empreinte_octets(f"{i}|{s[i]!r}|{res.verite.lisibilite[i]!r}|{int(res.verite.dommage[i])}".encode())
            for i in a]


def garde_pieces_appariees(monde, regle, oracle, tache: int, n: int,
                           canal_retour: Callable | None = None) -> int:
    r1 = rejeu_piece_forcee(monde, regle, oracle, tache, n, audite=True)
    r0 = rejeu_piece_forcee(monde, regle, oracle, tache, n, audite=False)
    for r in (r0, r1):
        garde_audit_apres_coup(r.journal)
    limite = min(instant_alarme(r0), instant_alarme(r1))
    return garde_vues_identiques(vues_agent(r1, canal_retour), vues_agent(r0, canal_retour),
                                 r1.journal.colonne("h_debut"), limite, "audit après coup (pièce appariée)")


def garde_plancher(journal: Journal, regle: RegleAudit) -> None:
    pi = journal.colonne("pi")
    pl = journal.colonne("part_plancher")
    if np.any(~np.isfinite(pi)):
        raise GardeArret("plancher : probabilité manquante")
    if regle.sans_plancher:
        if journal.etiquette != ETIQUETTE_SANS_PLANCHER:
            raise GardeArret("plancher : un journal `sans_plancher` doit porter l'étiquette « sans plancher : aucune borne »")
        return
    if not (regle.pi_min > 0):
        raise GardeArret("plancher : π_min > 0 exigé")
    if np.any(pl != regle.pi_min):
        raise GardeArret("plancher : la part du plancher n'est pas π_min sur toute ligne (plancher fonction du score ?)")
    if np.any(pi < regle.pi_min):
        raise GardeArret("plancher : une ligne porte π_i < π_min")


def garde_plancher_permutation(res_origine: Resultat, res_permute: Resultat) -> None:
    a = (res_origine.journal.colonne("source") == 1)
    b = (res_permute.journal.colonne("source") == 1)
    if np.packbits(a).tobytes() != np.packbits(b).tobytes():
        raise GardeArret("plancher : les tirages de source « plancher » changent quand on permute les scores")


def garde_enjeu(journal: Journal, regle: RegleAudit, enjeux_egaux_declares: bool, enjeux_egaux_loi: bool) -> None:
    if np.any(journal.colonne("h_enjeu") >= journal.colonne("h_debut")):
        raise GardeArret("part selon l'enjeu : enjeu écrit ou modifié après le début de l'épisode")
    attendu = regle.beta * journal.colonne("enjeu") / regle.s_bar
    if not np.array_equal(journal.colonne("part_enjeu"), attendu):
        raise GardeArret("part selon l'enjeu : la part ne vaut pas β·s_i/s̄ au bit près")
    if enjeux_egaux_declares != enjeux_egaux_loi:
        raise GardeArret("part selon l'enjeu : des enjeux égaux doivent être déclarés tels (et seulement eux)")


def garde_aucun_retour(monde, regle, oracle, tache: int, n: int, cle_permutation: int,
                       canal_retour: Callable | None = None) -> int:
    r = simuler(monde, regle, oracle, tache, n)
    rp = rejeu_permute(monde, regle, oracle, tache, n, cle_permutation)
    limite = min(instant_alarme(r), instant_alarme(rp))
    return garde_vues_identiques(vues_agent(r, canal_retour), vues_agent(rp, canal_retour),
                                 r.journal.colonne("h_debut"), limite, "aucun retour à l'agent")
