"""Essai 01 : `charger_textes` lit le fichier des textes par `str.splitlines()`. Le run l'écrit par
`run._ecrire_textes` (json.dumps, ensure_ascii=False, une ligne par action, fin de ligne « \\n »). Un texte d'action qui
contient U+2028, U+2029 ou U+0085 est écrit tel quel (json ne les échappe pas avec ensure_ascii=False) ; splitlines()
coupe la ligne en deux. Question : que fait l'addendum ? (GardeArret attendue au mieux ; repli ou exception brute ?)"""
import json
import shutil
import tempfile
from pathlib import Path

import commun  # noqa: F401
from commun import ICI, cp

from controle_ia.premier_test_ia.run import _ecrire_textes

base = Path(tempfile.mkdtemp(prefix="essai01-", dir=ICI))
try:
    for nom, car in (("U+2028", " "), ("U+2029", " "), ("U+0085", "\u0085"), ("témoin sain", "")):
        d = base / nom.replace("+", "").replace(" ", "-")
        d.mkdir()
        textes = [{"episode": "honnete/t0/e0", "condition": "honnete", "tache": "t0", "pas": 0,
                   "texte": f"ACTION: ADD\nTITLE: A{car}B\nPROPOSAL: p\nCOST: 40"},
                  {"episode": "honnete/t0/e0", "condition": "honnete", "tache": "t0", "pas": 1,
                   "texte": "ACTION: ADD\nTITLE: C\nPROPOSAL: p\nCOST: 50"}]
        sha = _ecrire_textes(d / "textes-actions-p3.jsonl", textes)       # écrivain du run, code gelé
        source = {"episodes-p3": {"textes": "textes-actions-p3.jsonl", "textes_sha256": sha}}
        brut = (d / "textes-actions-p3.jsonl").read_bytes()
        par_n = [json.loads(x) for x in brut.decode("utf-8").split("\n") if x]
        try:
            lus = cp.charger_textes(d, source)
            print(f"{nom:12s} : charger_textes rend {len(lus)} textes (écrits : 2 ; lus par split('\\n') : {len(par_n)}) ;"
                  f" égaux aux écrits : {lus == textes}")
        except Exception as e:  # noqa: BLE001
            print(f"{nom:12s} : charger_textes lève {type(e).__module__}.{type(e).__name__} "
                  f"(GardeArret : {isinstance(e, cp.GardeArret)}) ; lecture par split('\\n') : {len(par_n)} textes, "
                  f"égaux aux écrits : {par_n == textes}")
finally:
    shutil.rmtree(base)
