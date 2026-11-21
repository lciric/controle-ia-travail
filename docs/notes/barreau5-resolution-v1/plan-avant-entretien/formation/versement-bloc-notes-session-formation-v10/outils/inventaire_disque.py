"""python -I inventaire_disque.py N RUN DOSSIER_DISQUES ARBRE_COURSE SORTIE.tsv : inventaire d'un disque arrêté (noms et
tailles par `du -ab`, rien lu), comparé à la branche de sortie de l'instance (taille au commit de tête)."""
import re, subprocess, sys
from pathlib import Path
n, run, dd, arbre, sortie = sys.argv[1:6]
T = "/root/b5f-formation-v1/"
lignes = []
for k in (2, 3, 4, 5):
    for l in Path(dd, f"disque-{n}-{k}.txt").read_text(encoding="utf-8").splitlines():
        m = re.match(r"(\d+)\t(.*)$", l)
        if not m: continue
        p = m.group(2); i = p.find(T)
        if i < 0: continue
        lignes.append((p[i + len(T):], int(m.group(1))))
br = f"origin/donnees/barreau5-familles-jumelles-v1-formation-instance-{n}"
arbre_br = {}
for l in subprocess.run(["git", "-C", arbre, "ls-tree", "-r", "-l", br], capture_output=True, text=True, check=True).stdout.splitlines():
    meta, chemin = l.split("\t", 1); arbre_br[chemin] = int(meta.split()[3]) if meta.split()[3] != "-" else -1
tete = subprocess.run(["git", "-C", arbre, "rev-parse", br], capture_output=True, text=True, check=True).stdout.strip()
with open(sortie, "x", encoding="utf-8") as f:
    f.write(f"# inventaire du disque de l'instance {n} (run {run}), par `du -ab` du loueur ; branche {br[7:]} @ {tete}\n")
    f.write("chemin_sur_le_disque\toctets\tsur_la_branche\n")
    nf = nv = 0
    for c, t in sorted(lignes):
        rel = c[len("depot/"):] if c.startswith("depot/") else None
        if rel is not None and rel in arbre_br:
            etat = "même taille" if arbre_br[rel] == t else f"taille différente ({arbre_br[rel]})"
        else:
            etat = "absent" if rel is not None else "hors dépôt (traces)"
        f.write(f"{c}\t{t}\t{etat}\n")
print(n, "entrées", len(lignes))
