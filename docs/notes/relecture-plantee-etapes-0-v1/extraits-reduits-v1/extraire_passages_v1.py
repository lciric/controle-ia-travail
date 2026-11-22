"""Extrait daté de passages d'un fichier (plages de lignes), avec source et empreinte. Bibliothèque standard seule.
Usage : python3 extraire_passages_v1.py SOURCE SORTIE_NEUVE DEBUT-FIN [DEBUT-FIN …]   (lignes numérotées dès 1)"""
import datetime, hashlib, sys
src, sortie, plages = sys.argv[1], sys.argv[2], sys.argv[3:]
o = open(src, "rb").read(); lignes = o.decode("utf-8").splitlines()
heure = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
out = [f"# Extrait de passages : {src.split('/')[-1]}", "",
       f"- Fait le {heure} par `extraire_passages_v1.py`.",
       f"- Source : `{src}`, sha256 {hashlib.sha256(o).hexdigest()}, {len(lignes)} lignes.",
       f"- Plages de lignes reprises telles quelles : {', '.join(plages)}. Chaque ligne est précédée de son numéro.", ""]
for p in plages:
    a, b = (int(x) for x in p.split("-"))
    out.append(f"## Lignes {a} à {b}")
    out += [f"{i:5d}  {lignes[i-1]}" for i in range(a, b + 1)]
    out.append("")
open(sortie, "x", encoding="utf-8").write("\n".join(out) + "\n")
