"""Formes du champ COST (chiffres remplacés par 9) et mots interdits de PREDICTION les plus fréquents, par condition."""
import collections, json, re, subprocess, sys
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.environnements.propositions import lire_action
from sondage_validateur_v2 import INTERDITS_PREDICTION, DEPOT, REF, RACINE, lire
blocs = subprocess.run(["git", "-C", DEPOT, "ls-tree", "--name-only", REF, RACINE + "/"], capture_output=True, check=True, text=True).stdout.split()
formes = {c: collections.Counter() for c in ("honnete", "consigne_neutre", "gonfle_5")}
mots = {c: collections.Counter() for c in formes}
n = collections.Counter()
for bloc in blocs:
    textes = {d["cle"]: d["texte"] for d in lire(f"{bloc}/textes.jsonl")}
    for d in lire(f"{bloc}/mesures.jsonl"):
        c = d["condition"]
        if c not in formes:
            continue
        a = lire_action(textes[d["cle"]])
        n[c] += 1
        cout = a.champs.get("COST")
        f = "<absent>" if cout is None else re.sub(r"\d", "9", cout.strip().splitlines()[0])[:40]
        f = re.sub(r"9+", "9", f)
        formes[c][f] += 1
        for m in set(x.group(0).lower() for x in INTERDITS_PREDICTION.finditer(a.champs.get("PREDICTION", ""))):
            mots[c][re.sub(r"\d+", "9", m)] += 1
for c in formes:
    print(c, n[c]); print("  formes COST :", formes[c].most_common(9)); print("  interdits PREDICTION :", mots[c].most_common(14))
