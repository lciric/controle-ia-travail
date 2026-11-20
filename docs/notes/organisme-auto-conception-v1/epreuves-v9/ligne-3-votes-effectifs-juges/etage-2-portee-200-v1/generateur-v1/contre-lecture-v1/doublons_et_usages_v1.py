"""Contre-lecteur, modèle S : doublons de contenu et réemploi des fragments dans une composition sur les fragments factices
(racine des essais). Aucune ouverture du fichier des cartes."""
import json
import sys
from collections import Counter

sys.path.insert(0, "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-generateur-etage-2/copie-G")
import generer_temoins_ligne_3_v1 as G

FR = "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-generateur-etage-2/copie-G/fragments-exemple-essais-v1.json"
conf = G.lire_configuration()
fr, _ = G.charger_fragments(FR, G.sha256_fichier(FR), conf["etiquettes_interdites_fixes"])
banque, journal = G.composer(fr, G.Contexte("essais"), G.ITEMS, conf["etiquettes_interdites_fixes"])
contenus = Counter(json.dumps(t["contenu"], sort_keys=True, ensure_ascii=False) for t in banque)
doublons = sum(1 for v in contenus.values() if v > 1)
# paires de témoins partageant quatre fragments sur cinq au moins
partages = Counter()
for i in range(len(journal)):
    for j in range(i + 1, len(journal)):
        fi, fj = journal[i]["fragments"], journal[j]["fragments"]
        partages[sum(fi[c] == fj[c] for c in G.CATEGORIES)] += 1
usages = Counter(fid for j in journal for fid in j["fragments"].values())
n_frag = {c: len(fr["conformes"][c]) for c in G.CATEGORIES}
n_frag["fautifs"] = len(fr["fautifs"])
print(json.dumps({"doublons_de_contenu": doublons, "paires_par_nombre_de_fragments_communs": dict(sorted(partages.items())),
                  "fragments_par_categorie": n_frag, "usage_max": max(usages.values()), "usage_median": sorted(usages.values())[len(usages) // 2]},
                 ensure_ascii=False, indent=1))
