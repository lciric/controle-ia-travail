"""Applique les couples V-01 à V-14 du rapport de vérification à la note d'interface v1, dans l'ordre, puis les ajouts
déclarés de l'exécutante (en-tête v2, phrase de l'empreinte git, section « Livraison »). Chaque « avant » doit être présent
une seule fois au moment de son application ; sinon arrêt.
Usage : python appliquer_couples_interface_v2.py <rapport> <note-v1> <ajouts.json> <sortie-v2>
"""
import hashlib
import json
import re
import sys

rapport, note_v1, ajouts_f, sortie = sys.argv[1:5]
r = open(rapport, encoding="utf-8").read()
t = open(note_v1, encoding="utf-8").read()
assert hashlib.sha256(t.encode()).hexdigest() == "4fddb6c616de813f040353fc26fb2465aba101020222d08e904447bffa90b8db"
assert hashlib.sha256(r.encode()).hexdigest() == "ae5c03531564b0a4f9c0606b03db9e56661cb6babdee56ea6cecb1444482beef"
sections = re.split(r"^### (V-\d\d) — .*$", r.split("## 3. Exactitude")[0], flags=re.M)
couples = []
for i in range(1, len(sections), 2):
    nom, corps = sections[i], sections[i + 1]
    blocs = re.findall(r"^~~~~\n(.*?)\n~~~~$", corps, flags=re.S | re.M)
    if len(blocs) != 2:
        raise SystemExit(f"{nom} : {len(blocs)} blocs lus (2 attendus)")
    couples.append((nom, blocs[0], blocs[1]))
noms = [c[0] for c in couples]
if noms != [f"V-{k:02d}" for k in range(1, 15)]:
    raise SystemExit(f"couples lus : {noms}")
for nom, avant, apres in couples:
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"{nom} : « avant » présent {n} fois")
    t = t.replace(avant, apres)
    print(f"{nom} appliqué")
for k, (avant, apres) in enumerate(json.load(open(ajouts_f, encoding="utf-8"))):
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"ajout {k + 1} : « avant » présent {n} fois")
    t = t.replace(avant, apres)
    print(f"ajout {k + 1} appliqué")
open(sortie, "w", encoding="utf-8").write(t)
