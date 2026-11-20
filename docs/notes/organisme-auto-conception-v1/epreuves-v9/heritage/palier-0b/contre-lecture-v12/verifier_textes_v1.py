"""Les textes « Ancien : » et « Neuf : » de ma pièce sont-ils égaux, dans l'ordre, à ceux de mes jeux ? Et chaque ancien
figure-t-il une seule fois dans la v12 ? Lecture seule. Arguments : pièce, jeu des corrections, jeu non exigé, v12, sortie."""
import json
import sys

piece, jeu_c, jeu_ne, v12, sortie = sys.argv[1:6]
anciens, neufs = [], []
for ligne in open(piece, encoding="utf-8").read().split("\n"):
    for tete, liste in (("  - Ancien : `", anciens), ("  - Neuf : `", neufs)):
        if ligne.startswith(tete):
            assert ligne.endswith("`"), ligne[:80]
            liste.append(ligne[len(tete):-1])
jeu = json.load(open(jeu_c, encoding="utf-8")) + json.load(open(jeu_ne, encoding="utf-8"))
texte = open(v12, encoding="utf-8").read()
out = [f"textes dans la pièce : {len(anciens)} anciens, {len(neufs)} neufs ; dans les jeux : {len(jeu)}"]
for k, r in enumerate(jeu, 1):
    a_ok = k <= len(anciens) and anciens[k - 1] == r["ancien"]
    n_ok = k <= len(neufs) and neufs[k - 1] == r["neuf"]
    out.append(f"{k} : ancien égal {a_ok} ; neuf égal {n_ok} ; ancien dans la v12 {texte.count(r['ancien'])} fois")
out.append(f"tout égal : {len(anciens) == len(neufs) == len(jeu) and all(a == r['ancien'] and n == r['neuf'] for a, n, r in zip(anciens, neufs, jeu))}")
open(sortie, "w", encoding="utf-8").write("\n".join(out) + "\n")
