"""Contre-lecteur, modèle S : les différentiels v2 -> v3 refaits égalent ceux du développeur, hors les deux lignes d'en-tête."""
import json

B = "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-generateur-etage-2/"
D = "/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/generateur-v3/"
sortie = {}
for nom, mien, leur in (("programme", "diff-programme-v2-v3-refait-v1.diff", "differentiel-programme-v2-v3.diff"),
                        ("essais", "diff-essais-v2-v3-refait-v1.diff", "differentiel-essais-v2-v3.diff")):
    a = open(B + mien, encoding="utf-8").read().splitlines()[2:]
    b = open(D + leur, encoding="utf-8").read().splitlines()[2:]
    sortie[nom] = {"corps_identique": a == b, "lignes": [len(a), len(b)]}
print(json.dumps(sortie))
