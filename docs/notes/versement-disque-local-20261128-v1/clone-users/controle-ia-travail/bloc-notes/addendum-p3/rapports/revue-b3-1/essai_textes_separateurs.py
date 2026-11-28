"""Essai : un texte d'action qui contient U+2028, U+2029 ou U+0085, écrit comme `run._ecrire_textes` (json.dumps,
ensure_ascii=False, une ligne par action), puis relu par `complements_p3_v1.charger_textes`."""
import hashlib
import json
import sys
from pathlib import Path

import complements_p3_v1 as cp

ICI = Path(__file__).resolve().parent / "jouet-textes"
ICI.mkdir(exist_ok=True)
for nom, car in (("ligne_normale", ""), ("U+2028", " "), ("U+2029", " "), ("U+0085", "\u0085"),
                 ("U+000B", "\u000b")):
    textes = [{"episode": "honnete/t0/e0", "condition": "honnete", "tache": "t0", "pas": 0,
               "texte": f"ACTION: ADD\nTITLE: a{car}b\nPROPOSAL: p\nCONTROLS: c\nCOST: 40\nPREDICTION: q"},
              {"episode": "honnete/t0/e0", "condition": "honnete", "tache": "t0", "pas": 1,
               "texte": "ACTION: ADD\nTITLE: c\nPROPOSAL: p\nCONTROLS: c\nCOST: 50\nPREDICTION: q"}]
    chemin = ICI / f"textes-{nom}.jsonl"
    with open(chemin, "w", encoding="utf-8") as f:                    # comme `run._ecrire_textes`
        for x in textes:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    sha = hashlib.sha256(chemin.read_bytes()).hexdigest()
    source = {"episodes-p3": {"textes": chemin.name, "textes_sha256": sha}}
    try:
        lus = cp.charger_textes(ICI, source)
        print(f"{nom:13s} : {len(lus)} textes relus, égaux à l'écrit : {lus == textes}")
    except Exception as e:                                             # noqa: BLE001
        print(f"{nom:13s} : {type(e).__module__}.{type(e).__name__} : {str(e)[:90]}")
print("lignes physiques selon split('\\n') pour U+2028 :",
      len((ICI / "textes-U+2028.jsonl").read_bytes().decode("utf-8").split("\n")) - 1,
      "; selon splitlines() :", len((ICI / "textes-U+2028.jsonl").read_bytes().decode("utf-8").splitlines()))
