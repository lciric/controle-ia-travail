"""Compare les relevés v4 et v5 de invariance_v1.py, cas par cas. Usage : python -I comparer_invariance_v1.py DOSSIER_RES"""
import json, sys
from pathlib import Path
res = Path(sys.argv[1])
for cas in "ABCD":
    a = json.loads((res / f"v4-{cas}.json").read_text(encoding="utf-8"))
    b = json.loads((res / f"v5-{cas}.json").read_text(encoding="utf-8"))
    ja, jb = a["journal"], b["journal"]
    meme_appels = ja["appeler"] == jb["appeler"]
    premier_ecart = next((i for i, (x, y) in enumerate(zip(ja["appeler"], jb["appeler"])) if x != y), None)
    print(f"== cas {cas} : appels v4 {len(ja['appeler'])}, v5 {len(jb['appeler'])} ; suite identique (espèce, empreinte de la consigne, jetons, rôle) : {meme_appels}"
          + ("" if meme_appels else f" ; premier écart à l'appel n° {premier_ecart}"))
    if not meme_appels and premier_ecart is not None:
        print("   v4 :", ja["appeler"][premier_ecart]); print("   v5 :", jb["appeler"][premier_ecart])
    elif not meme_appels:
        print("   appels en plus (v5) :", [x["role"] for x in jb["appeler"][len(ja["appeler"]):]])
    print(f"   rechercher v4 {len(ja['rechercher'])} / v5 {len(jb['rechercher'])} ; telecharger v4 {len(ja['telecharger'])} / v5 {len(jb['telecharger'])} ; budget() v4 {ja['budget']} / v5 {jb['budget']} ; especes() v4 {ja['especes']} / v5 {jb['especes']}")
    fa, fb = a["fichiers"], b["fichiers"]
    for f in sorted(set(fa) | set(fb)):
        if fa.get(f) != fb.get(f):
            print(f"   fichier différent : {f} (v4 {'absent' if f not in fa else fa[f][:12]}, v5 {'absent' if f not in fb else fb[f][:12]})")
    ka, kb = set(a["cles_bilan"] or []), set(b["cles_bilan"] or [])
    if ka != kb:
        print(f"   clés du bilan : en plus en v5 {sorted(kb - ka)}, en moins {sorted(ka - kb)}")
