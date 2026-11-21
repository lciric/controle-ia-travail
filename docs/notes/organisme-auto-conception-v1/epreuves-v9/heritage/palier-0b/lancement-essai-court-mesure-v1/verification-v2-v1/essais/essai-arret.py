"""Essai de la colonne « fichier d'arrêt » : parcourir() sur un arbre factice (profondeurs variées, noms voisins, dossier, lien)."""
import importlib.util
import os
import sys

gardien_chemin, racine = sys.argv[1:3]
spec = importlib.util.spec_from_file_location("gardien", gardien_chemin)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

def toucher(rel):
    c = os.path.join(racine, rel)
    os.makedirs(os.path.dirname(c), exist_ok=True)
    with open(c, "w") as fh:
        fh.write("x")

toucher("etape-3/manifeste.json")
toucher("etape-4/darret.txt")            # nom voisin : ne commence pas par arret
toucher("etape-4/Arret.txt")             # casse : ne compte pas (à la lettre)
toucher("etape-4/a/b/c/d/e/arret-profond.txt")  # profondeur 6 : compte
os.makedirs(os.path.join(racine, "etape-5/arretdossier"), exist_ok=True)  # dossier : compte (écart 2 du rapport)
os.symlink("/nonexistent", os.path.join(racine, "arret-lien-brise"))   # lien brisé nommé arret... : doit compter sans planter
app, alloc, nf, arrets = g.parcourir(racine)
print("arrets rendus :", arrets)
attendu = ["etape-4/a/b/c/d/e/arret-profond.txt", "etape-5/arretdossier"]
print("attendu (fichiers) :", attendu[:1], "; dossier tolérable :", attendu[1:])
