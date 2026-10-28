"""Lanceur d'un bras du dossier « bras d'attaque » de conv-audit (bras-attaque-v1), par la lignée session-depot.

Une instance neuve = un appel unique à un modèle (sans outils, sans réseau côté modèle, sans mémoire), qui reçoit le brief
de son bras et les seuls fichiers de la liste blanche préparée dans `<bras>/entrees/` (empreintes relues avant l'envoi
contre `<bras>/ENTREES-v1.txt`). Sa réponse est écrite telle quelle, puis découpée en fichiers selon les balises demandées.
Rien de la réponse n'est affiché : on ne rapporte que la fin de l'appel, la catégorie d'un refus, l'usage et le coût
(quarantaine : session-depot scelle sans lire). Un refus est consigné tel quel, jamais relancé ni reformulé.

    ANTHROPIC_API_KEY=… python -I -B lancer_bras_v1.py BRAS MODELE SORTIE_NEUVE PLAFOND_USD

Codes : 0 réponse complète ; 3 refus consigné ; 4 réponse tronquée ou sans balises ; 2 arrêt avant l'appel.
"""
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

PRIX = {"claude-fable-5-1": (10.0, 50.0), "claude-opus-5-5": (4.0, 20.0)}   # USD par million (entrée, sortie)
MAX_SORTIE = 32000
SORTIES = {"A": ["mode-tenu-a-l-ecart-v1.md", "MANIFESTE.md"], "B": None}    # B : recette-NN.md (au plus 8) + MANIFESTE.md
BALISE = re.compile(r"^=== FICHIER : ([A-Za-z0-9._-]+) ===\n(.*?)^=== FIN DU FICHIER ===$", re.S | re.M)


def maintenant():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def h(b):
    return hashlib.sha256(b).hexdigest()


def main(bras, modele, sortie, plafond):
    ici = Path(__file__).resolve().parent
    d = ici / bras
    sortie = Path(sortie)
    if bras not in SORTIES or modele not in PRIX:
        sys.exit(f"bras {bras!r} ou modèle {modele!r} inconnu")
    if sortie.exists():
        print(f"{sortie} existe déjà (R12)"); return 2
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("clé absente : rien n'est lancé"); return 2
    entrees = []