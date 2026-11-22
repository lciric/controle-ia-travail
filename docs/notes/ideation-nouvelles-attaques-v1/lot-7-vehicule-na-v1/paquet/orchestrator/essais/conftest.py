"""Les essais du lot 7 importent `pole` depuis le paquet (dossier parent) ; ils n'ont besoin d'aucun autre lot."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
