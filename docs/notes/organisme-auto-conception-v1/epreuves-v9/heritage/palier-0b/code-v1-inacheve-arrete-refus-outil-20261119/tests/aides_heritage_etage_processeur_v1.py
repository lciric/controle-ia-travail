"""Aides communes aux essais de l'étage sur processeur du palier 0b (pas un essai). Les chemins viennent de variables
d'environnement, passées en argument du lancement ; une variable absente fait échouer l'essai qui en a besoin (aucun repli
silencieux, règle R5) :
- HERITAGE_COPIE_ORGANISME : dossier `orchestrator/` d'une copie du code de l'organisme ;
- HERITAGE_DEPOT : racine du dépôt de travail (pièces du palier 0a et calcul des ordres de grandeur v2)."""

import json
import os

import pytest

DOSSIER_HERITAGE = os.path.join("docs", "notes", "organisme-auto-conception-v1", "epreuves-v9", "heritage")


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
