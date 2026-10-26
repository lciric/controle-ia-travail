"""Structure des banques v1 et v5 : noms de champs, types, comptes par part. N'imprime aucune valeur
(ni texte, ni identifiant, ni vérité). Écrit le 25 octobre 2026 (sous-agent conv-audit, étape 1 v10).
Usage : python -I structure_banques_v1.py BANQUE.json [BANQUE.json ...]"""
import collections
import hashlib
import json
import pathlib
import sys

for chemin in sys.argv[1:]:
    p = pathlib.Path(chemin)
    if p.name.endswith(("-cle.json", "-secret.json")):
        sys.exit(f"refusé : {p.name}")
    octets = p.read_bytes()
    b = json.loads(octets)
    print(f"== {p.name} sha256 {hashlib.sha256(octets).hexdigest()}")
    print("  champs de tête :", {k: type(v).__name__ for k, v in b.items()})
    for part in ("train", "test", "test_final"):
        t = b.get(part)
        if not isinstance(t, list):
            print(f"  {part} : absent ou non liste")
            continue
        champs = collections.Counter()
        for x in t:
            for k, v in x.items():
                champs[(k, type(v).__name__)] += 1
        print(f"  {part} : {len(t)} tâches ; champs {dict(champs)}")
        # comptes par famille si un champ « famille » non secret existe
        for nom in ("famille", "family"):
            if all(nom in x for x in t):
                print(f"    par {nom} :", dict(collections.Counter(str(x[nom]) for x in t)))
