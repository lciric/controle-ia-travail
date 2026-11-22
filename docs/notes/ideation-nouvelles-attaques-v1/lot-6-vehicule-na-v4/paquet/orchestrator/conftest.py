# Hors paquet : met la racine de l'orchestrateur d'essai sur le chemin d'import (le vrai `pole` existe dans l'orchestrateur).
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
