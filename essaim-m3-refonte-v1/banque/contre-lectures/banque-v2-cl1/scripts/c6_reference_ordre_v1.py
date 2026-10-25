"""Contre-lecture banque v2 — c6 : la référence de surface dépend-elle de l'ordre du fichier ?

LISEZMOI-v4 garde l'ordre v1 « pour que la référence de surface, calculée dans l'ordre du fichier, reste identique ».
On calcule `essaim_m3.banque.reference_traits_texte` (code du dépôt, importé en lecture) sur la v2, sur une copie dont
chaque part est triée par identifiant v2 (correction naturelle), et sur trois copies dont chaque part est mélangée au
hasard (SeedSequence(2026102506)). Copies écrites sous /var/tmp/contre-lecture-banque-v2-v1/artefacts/.
Usage : python3 -I c6_reference_ordre_v1.py RACINE_CODE BANQUE_V2 DOSSIER_SORTIE
"""
import hashlib
import json
import pathlib
import sys

import numpy as np


def main(racine, pv2, sortie):
    sys.path.insert(0, str(racine))
    from essaim_m3.banque import reference_traits_texte
    sortie = pathlib.Path(sortie) / "artefacts"
    b = json.loads(pathlib.Path(pv2).read_text(encoding="utf-8"))
    ref0 = reference_traits_texte(pathlib.Path(pv2))["par_famille"]
    print("v2 telle quelle :", json.dumps(ref0, ensure_ascii=False))
    variantes = {"triee-par-id-v2": {p: sorted(b[p], key=lambda t: t["id"]) for p in ("train", "test", "test_final")}}
    rng = np.random.default_rng(np.random.SeedSequence(2026102506))
    for k in range(3):
        variantes[f"melangee-{k + 1}"] = {p: [b[p][int(i)] for i in rng.permutation(len(b[p]))] for p in ("train", "test", "test_final")}
    for nom, parts in variantes.items():
        c = dict(parts, manifeste=b["manifeste"])
        f = sortie / f"reference-ordre-{nom}-v1.json"
        if f.exists():
            sys.exit(f"{f} existe déjà (R12)")
        f.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        h = hashlib.sha256(f.read_bytes()).hexdigest()
        f.with_name(f.name + ".sha256").write_text(f"{h}  {f.name}\n", encoding="utf-8")
        ref = reference_traits_texte(f)["par_famille"]
        motif = "".join(("H" if t["verite"] == "honnete" else "S") if t["famille"] == "controle-delegation"
                        else ("e" if t["verite"] == "evaluation" else "u") for t in parts["test"])
        print(f"{nom} ({h[:12]}…) : référence identique à la v2 : {ref == ref0} ; test dans l'ordre du fichier : {motif}")
        if ref != ref0:
            print("   ", json.dumps(ref, ensure_ascii=False))


if __name__ == "__main__":
    main(*sys.argv[1:4])
