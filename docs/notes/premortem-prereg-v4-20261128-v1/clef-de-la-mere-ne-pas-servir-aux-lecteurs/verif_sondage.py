"""Contrôle du sondage : formes de la première ligne et motifs d'invalidité des actions honnêtes rejetées."""
import collections, re, subprocess, sys
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.environnements.propositions import Etat, appliquer
from sondage_validateur_v2 import DEPOT, REF, RACINE, lire, motifs_de_rejet
import copy
blocs = subprocess.run(["git", "-C", DEPOT, "ls-tree", "--name-only", REF, RACINE + "/"], capture_output=True, check=True, text=True).stdout.split()
prem = collections.Counter(); inval = collections.Counter(); seuls = collections.Counter(); n = 0
for bloc in blocs:
    textes = {d["cle"]: d["texte"] for d in lire(f"{bloc}/textes.jsonl")}
    eps = collections.defaultdict(list)
    for d in lire(f"{bloc}/mesures.jsonl"):
        if d["condition"] == "honnete":
            eps[(d["tache"], d["replique"])].append(d)
    for actions in eps.values():
        actions.sort(key=lambda d: d["pas"]); etat = Etat()
        for d in actions:
            t = textes[d["cle"]]; n += 1
            r = motifs_de_rejet(etat, d["pas"], t)
            if "2d-premiere-ligne" in r:
                l = (t.strip().splitlines() or [""])[0]
                prem[re.sub(r"\d+", "9", l)[:48]] += 1
            if r == ["1a-action-invalide"]:
                a = appliquer(copy.deepcopy(etat), 0, d["pas"], t)
                inval[re.sub(r"\d+", "9", str(a.motif))[:60]] += 1
            if len(r) == 1:
                seuls[r[0]] += 1
            appliquer(etat, 0, d["pas"], t)
print(n); print("premières lignes rejetées :", prem.most_common(8)); print("motifs d'invalidité :", inval.most_common(6)); print("rejetées pour un seul motif :", seuls.most_common())
