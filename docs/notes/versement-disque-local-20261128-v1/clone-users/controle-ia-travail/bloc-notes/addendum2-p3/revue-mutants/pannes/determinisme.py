"""Panne P1 : déterminisme de la fonction pure `analyser_addendum2` d'un processus à l'autre.

Scénarios synthétiques des tests (copie de base, importée sans pytest), paramètres du texte (10 000 tirages, sauf
`--tirages`), graines de la liste fermée dérivées de l'entropie de P3. Imprime, par scénario, l'empreinte sha256 de la
sortie sérialisée (clés triées). Aucun fichier du dépôt de travail n'est lu en dehors du code gelé et des aides de tests.
"""
import hashlib
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "base"
sys.path.insert(0, str(BASE))
sys.dont_write_bytecode = True

import test_audit_verdict_p3_v1 as T  # noqa: E402

av = T.av
tirages = int(sys.argv[sys.argv.index("--tirages") + 1]) if "--tirages" in sys.argv else 10_000
av.TIRAGES = tirages
sortie = {"tirages": tirages, "module": str(Path(av.__file__).resolve())}
for nom in ("sain", "sans_formes", "trop_bas", "propre", "part", "b2", "non_etabli", "criteres", "temoin_illisible",
            "degenere"):
    s, lec = T._cas(nom)
    o = av.analyser_addendum2(s, lec, T.G)
    sortie[nom] = hashlib.sha256(json.dumps(o, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
print(json.dumps(sortie, ensure_ascii=False))
