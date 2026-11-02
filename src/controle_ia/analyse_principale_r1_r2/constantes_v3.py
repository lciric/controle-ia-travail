"""Constantes gelées du mode « R2 seul » (code v3) : lecture complémentaire des juges de R2 quand le rejeu R1 s'est arrêté
(n° 247 de session-depot : `verdict_fidelite` « echec », rien de R1 versé). N'existe que sur le mot de Lazar (option (c)
du nœud R-1103) : c'est un écart assumé au texte du fournisseur (« rejeu non validé : rien n'est lu », l. 180).

Toutes les valeurs communes (taux, quantile, plis, tirages, niveau, classes, traits de T, règle C, juges, masse) restent
dans `constantes_v1`, lu par `calcul_v1` et `entrees_v1` ; ce module ne porte que ce qui est propre au mode R2 seul.
L'empreinte citée couvre les deux.
"""
from __future__ import annotations

import hashlib
import sys

from . import constantes_v1 as K1

VERSION = "analyse-r2-seul-v1 (code v3)"
COMMANDE = "python -m controle_ia.analyse_principale_r1_r2.lecture_v3"
NOM_SORTIE = "analyse-r2-seul-v1"
FORMAT_FICHE = "fiche-reception-r2-seul-v1"
BRAS = ("J3s", "J3g", "J8s", "G", "G_enjeux", "C", "T")
COMPARAISONS_PRINCIPALES = (("J3s", "G"), ("J3s", "T"))          # Bonferroni : deux comparaisons, 97,5 %
COMPARAISONS_SECONDAIRES = (("J8s", "G"), ("J8s", "T"))
COMPARAISONS_DESCRIPTIVES = (("J3g", "G"), ("J3s", "J3g"), ("J8s", "J3s"), ("T", "G"), ("C", "G"), ("J3s", "C"),
                             ("J3s", "G_enjeux"), ("T", "C"))
BRAS_CONTROLE = "J3s"                  # contrôles « mention » et « témoin » lus au seuil du juge 3B spécialisé
VERDICTS_ARRET = {"echec": "rejeu_en_echec", "non conforme": "rejeu_non_conforme"}   # verdict de l'arret.json → motif
MOTIFS_J8_NUL = ("non_livre",)
COMMANDE_REJEU = "python -m controle_ia.runs_nuit.rejeu_activations_v1"   # commande du rejeu (commit 29bd8e2e)
CLES_GRAINES = ("plis", "tirages")
REGLE_ENTROPIE = "128 premiers bits de l'empreinte sha256 du préenregistrement « R2 seul » scellé"

NOMS_GELES = ("VERSION", "COMMANDE", "NOM_SORTIE", "FORMAT_FICHE", "BRAS", "COMPARAISONS_PRINCIPALES",
              "COMPARAISONS_SECONDAIRES", "COMPARAISONS_DESCRIPTIVES", "BRAS_CONTROLE", "VERDICTS_ARRET", "MOTIFS_J8_NUL", "COMMANDE_REJEU",
              "CLES_GRAINES", "REGLE_ENTROPIE")


def constantes_courantes() -> dict:
    m = sys.modules[__name__]

    def simple(v):
        if isinstance(v, (tuple, list)):
            return [simple(x) for x in v]
        if isinstance(v, dict):
            return {str(k): simple(x) for k, x in v.items()}
        return v
    return {"v1": K1.constantes_courantes(), "v3": {n: simple(getattr(m, n)) for n in NOMS_GELES}}


def empreinte_constantes() -> str:
    from ..manifeste import config_canonique

    return hashlib.sha256(config_canonique(constantes_courantes())).hexdigest()


def entropie_de(sha_prereg: str) -> int:
    """Racine des graines (R9) : les 128 premiers bits de l'empreinte du préenregistrement « R2 seul » scellé."""
    return int.from_bytes(bytes.fromhex(sha_prereg)[:16], "big")
