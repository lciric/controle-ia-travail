"""Aides communes aux essais de l'étage sur processeur du palier 0b (pas un essai). Les chemins viennent de variables
d'environnement passées au lancement ; une variable absente fait échouer l'essai qui en a besoin (aucun repli silencieux,
règle R5) :
- HERITAGE_COPIE_ORGANISME : dossier `orchestrator/` d'une copie du code de l'organisme (commit 94bfd92) ;
- HERITAGE_DEPOT : racine du dépôt de travail (pièces du palier 0a et calcul des ordres de grandeur v2).
Toutes les graines des essais sont de la couche « essai »."""

import json
import os

import pytest

from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import proposeurs as P
from controle_ia.heritage_etage_processeur_v1.constantes import CLES_FREQUENCES

DOSSIER_HERITAGE = os.path.join("docs", "notes", "organisme-auto-conception-v1", "epreuves-v9", "heritage")

# Fréquences d'essai (ordre de grandeur vu sur des graines « essai » ; jamais un fichier gelé de l'étape 5)
FREQUENCES_D_ESSAI = {"p_tient_vraie_source": 1.0, "p_tient_vraie_cible": 1.0, "p_tient_fausse": 0.15,
                      "p_tient_non_plantee_base": 0.02, "p_tient_non_plantee_composition": 0.8,
                      "p_tient_non_plantee_copie": 0.05, "p_passage_vraie": 1.0, "p_faux_passage": 0.4}
assert sorted(FREQUENCES_D_ESSAI) == sorted(CLES_FREQUENCES)


def chemin_env(nom):
    v = os.environ.get(nom)
    if not v or not os.path.isdir(v):
        pytest.fail(f"variable d'environnement {nom} absente ou dossier introuvable : l'essai ne se joue pas sans elle (R5)")
    return v


def depot(*morceaux):
    return os.path.join(chemin_env("HERITAGE_DEPOT"), DOSSIER_HERITAGE, *morceaux)


def lire_json(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def copie_organisme():
    return chemin_env("HERITAGE_COPIE_ORGANISME")


def graines():
    return GR.Graines()


def prop(nom, **kw):
    return P.configuration(nom, **kw)
