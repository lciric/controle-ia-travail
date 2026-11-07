#!/usr/bin/env python3
"""Échantillon de la contre-vérification à l'aveugle (consigne v3, section 9) — fille 12, v1.
Usage : echantillon_contre_verification_v1.py DOSSIER_ASSEMBLE REPERTOIRE_LECTEUR FICHIER_CLE
Entropie neuve (numpy.random.SeedSequence()), clés de la section 9 ; 32 paires par jeu (J-D, J-C), 16 par mode pour J-A, au plus deux paires par tâche
(par jeu, et par mode pour J-A). J-C et J-A : les deux membres dans un ordre tiré, sans étiquette, COST masqué ; J-D : bloc, rappel, réponse.
Le fichier clé (étiquettes, ordre, entropie) est écrit hors de la vue du lecteur."""
import json, re, sys
import numpy as np
from pathlib import Path
RACINE = Path(__file__).resolve().parents[3]
d = Path(sys.argv[1]); sortie = Path(sys.argv[2]); cle_chemin = Path(sys.argv[3])
annexes = RACINE / "brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes"
banque = json.load(open(annexes / "banque-instructions-v2.json")); incs = {e["id"]: e["texte"] for e in json.load(open(annexes / "banque-incitations-v2.json"))["entrees"]}
cad = banque["cadrages"]; instr = {e["id"]: e for e in banque["entrees"]}
ordre_taches = [json.loads(l)["identifiant"] for l in open(d / "enonces-reserve-v2.jsonl")]
enonces = {json.loads(l)["identifiant"]: json.loads(l) for l in open(d / "enonces-reserve-v2.jsonl")}
entropie = np.random.SeedSequence().entropy
CLES = {"echantillon-dissimulation": 1, "echantillon-domaine-cout": 2, "echantillon-intention-autres-modes": 3}
def rng(cle, sous=0):
    return np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropie, spawn_key=(CLES[cle], sous))))
def charge(nom): return [json.loads(l) for l in open(d / nom)]
def paires(recs):
    p = {}
    for r in recs: p.setdefault((r["tache"], r["paire"]), []).append(r)
    return p
def tirer(P, n, gen, filtre=lambda k, v: True):
    cles = sorted(k for k, v in P.items() if filtre(k, v))
    ordre = list(gen.permutation(len(cles))); pris = []; par_tache = {}
    for i in ordre:
        t = cles[i][0]
        if par_tache.get(t, 0) >= 2: continue
        pris.append(cles[i]); par_tache[t] = par_tache.get(t, 0) + 1
        if len(pris) == n: break
    assert len(pris) == n, (len(pris), n)
    return sorted(pris, key=lambda k: (ordre_taches.index(k[0]), k[1]))
def masque(rep): return re.sub(r"\nCOST: \d+\n", "\nCOST: [masqué]\n", rep)
cle = {"entropie": int(entropie), "cles": CLES, "items": {}}
taches_vues = set()
def entete(t):
    taches_vues.add(t)
sortie.mkdir(parents=True, exist_ok=True)
# --- J-D
jd = paires(charge("dissimulation-v2.jsonl")); k = tirer(jd, 32, rng("echantillon-dissimulation"))
lignes = ["# Échantillon J-D (dissimulation) : 32 paires\n"]
for i, (t, p) in enumerate(k, 1):
    rs = jd[(t, p)]; pos = [r for r in rs if r["etiquette"] == 1][0]
    e = instr[pos["instruction_id"]]; o, f = cad[e["cadrage"]]
    lignes.append(f"## JD-{i:02d} (tâche {t})\n\n**Bloc d'instruction privée** (fin du message système, présent chez un des deux exemplaires de l'agent) : {o} {e['contrainte']} {f}\n\n**Ligne de rappel** (avant « Your action: ») : {e['rappel']}\n\n**Réponse** (la même pour les deux exemplaires) :\n\n```\n{pos['reponse']}\n```\n")
    cle["items"][f"JD-{i:02d}"] = {"jeu": "dissimulation", "tache": t, "paire": p, "instruction_id": pos["instruction_id"]}; entete(t)
open(sortie / "echantillon-jd.md", "w").write("\n".join(lignes))
# --- J-C
jc = paires(charge("domaine-cout-v2.jsonl")); k = tirer(jc, 32, rng("echantillon-domaine-cout"))
lignes = ["# Échantillon J-C (domaine, mode coût) : 32 paires\n\nChaque paire : le même contexte (la tâche, voir `taches.md`, et la note de contexte ci-dessous), deux actions X et Y ; le champ COST est masqué.\n"]
g = rng("echantillon-domaine-cout", 99)
for i, (t, p) in enumerate(k, 1):
    rs = {r["etiquette"]: r for r in jc[(t, p)]}; echange = int(g.integers(0, 2))
    x, y = (rs[1], rs[0]) if echange else (rs[0], rs[1])
    lignes.append(f"## JC-{i:02d} (tâche {t})\n\n**Note de contexte commune** : {incs[rs[0]['incitation_id']]}\n\n**Action X** :\n\n```\n{masque(x['reponse'])}\n```\n\n**Action Y** :\n\n```\n{masque(y['reponse'])}\n```\n")
    cle["items"][f"JC-{i:02d}"] = {"jeu": "domaine-cout", "tache": t, "paire": p, "x_etiquette": x["etiquette"], "incitation_id": rs[0]["incitation_id"]}; entete(t)
open(sortie / "echantillon-jc.md", "w").write("\n".join(lignes))
# --- J-A
ja = paires(charge("intention-autres-modes-v2.jsonl"))
for mode, nom in (("controles", "ja-controles"), ("direction", "ja-direction")):
    sous = 0 if mode == "controles" else 1
    k = tirer(ja, 16, rng("echantillon-intention-autres-modes", sous), lambda kk, v, m=mode: v[0]["mode"] == m)
    lignes = [f"# Échantillon J-A, mode `{mode}` : 16 paires\n\nChaque paire : le même contexte (la tâche, voir `taches.md`), deux actions X et Y ; le champ COST est masqué.\n"]
    g = rng("echantillon-intention-autres-modes", 10 + sous)
    for i, (t, p) in enumerate(k, 1):
        rs = {r["etiquette"]: r for r in ja[(t, p)]}; echange = int(g.integers(0, 2))
        x, y = (rs[1], rs[0]) if echange else (rs[0], rs[1])
        lignes.append(f"## {'JAC' if mode == 'controles' else 'JAD'}-{i:02d} (tâche {t})\n\n**Action X** :\n\n```\n{masque(x['reponse'])}\n```\n\n**Action Y** :\n\n```\n{masque(y['reponse'])}\n```\n")
        cle["items"][f"{'JAC' if mode == 'controles' else 'JAD'}-{i:02d}"] = {"jeu": "intention-autres-modes", "mode": mode, "tache": t, "paire": p, "x_etiquette": x["etiquette"]}; entete(t)
    open(sortie / f"echantillon-{nom}.md", "w").write("\n".join(lignes))
# --- énoncés des tâches échantillonnées (une fois)
txt = ["# Tâches de l'échantillon : énoncé et métadonnées vus par l'agent\n"]
for t in ordre_taches:
    if t in taches_vues:
        txt.append(f"## Tâche {t}\n\n{enonces[t]['questions']}\n\nMétadonnées : {json.dumps(enonces[t]['classification'], ensure_ascii=False)}\n")
open(sortie / "taches.md", "w").write("\n".join(txt))
cle_chemin.parent.mkdir(parents=True, exist_ok=True)
json.dump(cle, open(cle_chemin, "w"), indent=1, ensure_ascii=False)
print("entropie", entropie, "items", len(cle["items"]), "tâches", len(taches_vues))
