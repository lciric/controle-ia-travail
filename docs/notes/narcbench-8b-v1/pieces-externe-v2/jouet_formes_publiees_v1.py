"""Jouet de bout en bout aux formes publiées (plan d'analyse n° 1 du texte court) : vecteurs FACTICES (aucune donnée réelle),
deux modèles, deux étages, 1 054 et 1 320 lignes, couches 26-30 (5 120) et 32-37 (8 192) ; dépôt git jetable ; commande de
lecture complète (réglages du texte : 2 000 tirages, 200 directions, 200 permutations, graines 0 à 9). Mesure durée et mémoire.
Usage : PYTHONPATH=<arbre>/src:<paquets> python jouet_formes_publiees_v1.py <dossier de travail>"""
import json
import resource
import shutil
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

import controle_ia
from controle_ia import scellement
from controle_ia.narcbench import chargeur_externe_v1 as C
from controle_ia.narcbench import lecture_externe_v2 as L

travail = Path(sys.argv[1])
travail.mkdir(parents=True)
rng = np.random.default_rng(20261118)
DOMAINES = ["audit", "cyber", "eng", "env", "fin", "food", "gov", "hire", "leg", "med", "mil", "pharma", "re", "research"]


def ligne(rid, mode, role, canal, phase, rnd, agent):
    m = {k: None for k in C.CHAMPS}
    m.update(run_id=rid, mode=mode, role=role, channel=canal, phase=phase, round=rnd, agent_name=agent)
    return m


def meta(etage):
    out = []
    if etage == "core":
        runs = [(f"fam__{DOMAINES[k % 14]}_{k:02d}__{mode}", mode) for k in range(31) for mode in ("collusion", "control")]
        tours, final = (1, 2, 3), 4
    else:
        runs = [(f"bj__shoe{k:02d}__{mode}", mode) for k in range(20) for mode in ("collusion", "control")]
        tours, final = range(1, 8), 8
    for rid, mode in runs:
        roles = {f"agent_{j}": ("colluder" if mode == "collusion" and j in (0, 3) else "honest") for j in range(4)}
        out += [ligne(rid, mode, r, "private", "private", 0, a) for a, r in roles.items() if r == "colluder"]
        out += [ligne(rid, mode, r, "public", "discussion", t, a) for t in tours for a, r in roles.items()]
        out += [ligne(rid, mode, r, "public", "final", final, a) for a, r in roles.items()]
    return out


donnees, attendues = travail / "donnees", {}
for modele in C.MODELES:
    for etage in C.ETAGES:
        d = donnees / "activations" / modele / etage
        d.mkdir(parents=True)
        mt = meta(etage)
        (d / "metadata_gen.json").write_text(json.dumps(mt))
        tab = {}
        for c in C.BANDES[modele]:
            A = rng.standard_normal((len(mt), C.LARGEURS[modele]), dtype=np.float32)
            A[[i for i, m in enumerate(mt) if m["role"] == "colluder"], :8] += np.float32(0.6)
            tab[f"layer_{c}"] = A
        np.savez(d / "activations_gen.npz", **tab)
        for nom, sorte in (("activations_gen.npz", "sha256"), ("metadata_gen.json", "git-sha1")):
            p = d / nom
            attendues[f"activations/{modele}/{etage}/{nom}"] = (p.stat().st_size, sorte, C.empreinte(p, sorte))
        print(modele, etage, len(mt), "lignes", flush=True)

depot = travail / "depot"
paquet = Path(controle_ia.__file__).resolve().parent
shutil.copytree(paquet, depot / "src" / "controle_ia", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
shutil.copy(paquet.parent.parent / "requirements-cpu.txt", depot / "requirements-cpu.txt")


def git(*a):
    return subprocess.run(["git", "-C", str(depot), *a], check=True, capture_output=True, text=True).stdout.strip()


def commit(msg):
    git("add", "-A")
    git("-c", "user.name=jouet", "-c", "user.email=jouet@exemple.invalid", "commit", "-q", "-m", msg)
    return git("rev-parse", "HEAD")


git("init", "-q")
c = commit("code")
(depot / "prereg").mkdir()
(depot / "registres" / "code-narc-ext").mkdir(parents=True)
texte = depot / "prereg" / "narcbench-bras-externe-v1.md"
h = "c" * 64
texte.write_text("# Jouet\n\n## Hypothèse\n\nJouet.\n\n## Prédiction chiffrée et signe attendu\n\nJouet.\n\n## Métrique\n\nAire.\n\n"
                 "## Seuil\n\n0,03.\n\n## Plan d'analyse\n\nJouet.\n\n## Critères de lecture gelés\n\nJouet.\n\n## Liste d'arrêt\n\nJouet.\n\n"
                 "## Configuration canonique de la commande\n\naugmentation : papier\ncouches-familles : bande\n"
                 "run-id : AAAAMMJJ-HHMMSS-narc-externe-v2\nregistre : registres/narcbench-externe-v1.md\n"
                 "texte : prereg/narcbench-bras-externe-v1.md\nEntropie : 5049312917428823951\n\n"
                 f"## Contre-lecture\n\nBrouillon relu {h}, rapport {'d' * 64}.\n", encoding="utf-8")
st = scellement.sceller(texte)
fiche = depot / "registres" / "code-narc-ext" / "CODE-NARC-EXT-v1.json"
fiche.write_text(json.dumps(dict(L.fiche_code(depot, c), branche="jouet")), encoding="utf-8")
sf = scellement.sceller(fiche)
(depot / L.REGISTRE).write_text(f"# Registre jouet\n\n| SCELLEMENT-NARC-EXT | 2026-01-01T00:00:00Z | prereg/narcbench-bras-externe-v1.md | {st} |\n"
                                f"| CODE-NARC-EXT | 2026-01-02T00:00:00Z | registres/code-narc-ext/CODE-NARC-EXT-v1.json | {sf} |\n",
                                encoding="utf-8")
commit("texte, fiche, registre")
t0 = time.time()
code = L.main(["--depot", str(depot), "--texte", "prereg/narcbench-bras-externe-v1.md", "--donnees", str(donnees),
               "--run-id", "20261118-190000-narc-externe-v2", "--entropie", "5049312917428823951", "--augmentation", "papier",
               "--couches-familles", "bande"], attendues=attendues)
duree = time.time() - t0
pic = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
print(f"code {code} ; durée {duree / 60:.1f} min ; mémoire de pointe {pic:.0f} Mo", flush=True)
if code == 0:
    r = json.loads((depot / "diag" / "20261118-190000-narc-externe-v2" / "externe-narcbench-v2.json").read_text())["resultat"]
    print("réponse (vecteurs factices) :", r["lecture"]["reponse"]["ligne"],
          {m: {k: (v["ligne"], v["plancher_court"]) for k, v in r["modeles"][m]["cellules"].items()} for m in C.MODELES})
    print("méthodes de plancher :", {m: sorted({x for v in r["modeles"][m]["cellules"].values() if v.get("plancher")
                                                for x in (v["plancher"].get("methodes") or [])}) for m in C.MODELES})
