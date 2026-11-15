"""Essai à blanc de l'ENVIRONNEMENT EXACT des essais de B0 de la tranche B-α (variables, fichiers, chemins) — v1.

Demande de la mère après la première course (2026-11-15, instance 60770175 : B0 en échec, `NEURON_LENS_ORIG` absent) : voir sur
processeur ce défaut-là et ses voisins. Sur un clone du dépôt réduit, sans réseau ni modèle, **sans exécuter le code voisin** :
1. joue le **vrai** `preparer` du lanceur (empreintes, manifeste, copie d'origine, `git apply` des quatre correctifs) ;
2. joue le **vrai** `etape_b0` du lanceur, l'exécuteur des essais remplacé par un enregistreur (aucun pytest lancé) et la lecture des
   lentilles par un faux ; consigne, pour chaque essai, l'environnement et le dossier de travail qu'il recevrait ;
3. contrôle, pour chacun des quatre essais de B0 : (a) chaque variable que le fichier lit (`os.environ.get("…")`, `os.environ["…"]`)
   ou que son usage écrit (`NOM=… python -m pytest`) est présente ; (b) toute variable qui nomme un chemin pointe vers un fichier ou un
   dossier existant ; (c) chaque empreinte sha256 écrite dans le fichier est celle d'un fichier de l'arbre préparé (code voisin corrigé,
   copie d'origine) ou d'un fichier de l'arbre réduit, sinon elle est listée « hors du conteneur » avec son nom de constante (fichiers
   téléchargés sur la machine : poids, lentilles) — jamais une erreur muette ; (d) `NEURON_LENS_MODEL` vaut le modèle de B-α et
   `HF_HUB_OFFLINE` vaut 1 ; aucun secret.
R5 : `--lanceur-artefact <module>` rejoue l'étape 2 avec un autre lanceur (par exemple `b_alpha_lancer_v1`) sur l'arbre déjà préparé :
il doit être pris en défaut.

Usage : `python scripts/essai_environnement_b0_v1.py <clone du dépôt réduit> [--lanceur b_alpha_lancer_v2] [--lanceur-artefact
b_alpha_lancer_v1 --source <dépôt source>]` ; code 0 : conforme ; 1 : écart.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import re
import sys
from pathlib import Path

_LU = re.compile(r'os\.environ(?:\.get)?\(\s*"([A-Z_][A-Z0-9_]*)"|os\.environ\[\s*"([A-Z_][A-Z0-9_]*)"\s*\]')
_USAGE = re.compile(r"((?:[A-Z_][A-Z0-9_]*=\S+\s+)+)python -m pytest")
_HEX = re.compile(r'([A-Z_][A-Z0-9_]*)\s*=\s*"([0-9a-f]{64})"|"([0-9a-f]{64})"')


def variables_exigees(texte: str) -> set[str]:
    out = {a or b for a, b in _LU.findall(texte)}
    for bloc in _USAGE.findall(texte):
        out |= {x.split("=")[0] for x in bloc.split()}
    return out


def empreintes_ecrites(texte: str) -> list[tuple[str, str]]:
    return [(nom or "(sans nom)", h1 or h2) for nom, h1, h2 in _HEX.findall(texte)]


def empreintes_locales(*racines: Path) -> dict[str, str]:
    out = {}
    for r in racines:
        for p in r.rglob("*"):
            if p.is_file() and ".git" not in p.parts and p.stat().st_size < 200 * 1024 * 1024:
                out.setdefault(hashlib.sha256(p.read_bytes()).hexdigest(), str(p.relative_to(r)))
    return out


def enregistrer_b0(lanceur, ctx) -> list[dict]:
    vus = []

    def ex(cmd, cwd, env, journal, timeout_s):
        vus.append({"cmd": [str(c) for c in cmd], "cwd": str(cwd), "env": dict(env)})
        return {"code": 0, "duree_s": 0.0, "fin": ["7 passed in 0.1s"]}
    ctx.executer = ex
    faux = lambda v, s: {"arrets": [], "defauts": [], "autres_cles": "[]", "sortie": "faux"}
    lanceur.etape_b0(ctx, lire_lentille=faux)
    return vus


def controler(depot: Path, appels: list[dict], essais, modele: str) -> tuple[list[str], list[str]]:
    ecarts, hors = [], []
    locales = empreintes_locales(depot / "voisin" / "neuron-lens", depot / "originaux", depot / "docs", depot / "src")
    for e in essais:
        fichier = depot / "docs/notes/neuron-lens-v1/correctifs" / e
        a = [x for x in appels if any(c.endswith(e) for c in x["cmd"])]
        if len(a) != 1:
            ecarts.append(f"{e} : {len(a)} appel(s) (attendu 1)")
            continue
        env, texte = a[0]["env"], fichier.read_text(encoding="utf-8")
        for v in sorted(variables_exigees(texte)):
            if v not in env:
                ecarts.append(f"{e} : variable {v} absente")
            elif v in ("NEURON_LENS_ROOT", "NEURON_LENS_ORIG") and not Path(env[v]).exists():
                ecarts.append(f"{e} : {v} = {env[v]} n'existe pas")
        if env.get("NEURON_LENS_MODEL") != modele:
            ecarts.append(f"{e} : NEURON_LENS_MODEL = {env.get('NEURON_LENS_MODEL')}")
        if env.get("HF_HUB_OFFLINE") != "1":
            ecarts.append(f"{e} : HF_HUB_OFFLINE absent")
        for k in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "GH_TOKEN"):
            if k in env:
                ecarts.append(f"{e} : secret {k} présent")
        ecrites = empreintes_ecrites(texte)
        for nom, h in ecrites:
            if h not in locales:
                hors.append(f"{e} : {nom} {h[:12]}… hors du conteneur")
        print(f"  {e} : empreintes écrites {len(ecrites)}, résolues dans l'arbre préparé "
              f"{sum(h in locales for _, h in ecrites)} ({', '.join(f'{n}→{locales[h]}' for n, h in ecrites if h in locales)})")
    return ecarts, hors


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("depot", type=Path)
    p.add_argument("--lanceur", default="b_alpha_lancer_v2")
    p.add_argument("--lanceur-artefact")
    p.add_argument("--source", type=Path)
    a = p.parse_args(argv)
    depot = a.depot.resolve()
    sys.path.insert(0, str(depot / "src"))
    os.environ |= {"GO_ID": "GO-2026-11-14-06", "NEURON_LENS_MODEL": "meta-llama/Llama-3.1-8B-Instruct",
                   "HF_HOME": str(depot.parent / "hf"), "HF_HUB_OFFLINE": "1"}
    for k in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "GH_TOKEN"):
        os.environ.pop(k, None)
    bl = importlib.import_module(f"controle_ia.neuron_lens.{a.lanceur}")
    ctx = bl.Contexte(depot, "20261120-100000-neuron-lens-b-alpha", depot.parent / "hf")
    bl.jouer(ctx, "preparer")
    print(f"preparer reel : fait ({ctx.resultat('preparer').name}) ; copie d'origine : "
          f"{getattr(ctx, 'original_06', Path('?')).exists() if hasattr(ctx, 'original_06') else 'sans objet'}")
    appels = enregistrer_b0(bl, ctx)
    ecarts, hors = controler(depot, appels, bl.p2.ESSAIS_B0, bl.LLAMA)
    for e in bl.p2.ESSAIS_B0:
        x = next(x for x in appels if any(c.endswith(e) for c in x["cmd"]))
        env = {k: v for k, v in x["env"].items() if k.startswith(("NEURON_LENS", "HF_HUB_OFFLINE", "PYTHONPATH"))}
        print(f"  {e} : cwd={Path(x['cwd']).relative_to(depot)} ; {json.dumps({k: str(v).replace(str(depot), '<depot>') for k, v in sorted(env.items())}, ensure_ascii=False)}")
    for h in hors:
        print(f"  hors du conteneur (attendu sur la machine) : {h}")
    for e in ecarts:
        print(f"  ÉCART : {e}")
    print(f"CONTROLE de l'environnement de B0 ({a.lanceur}) : {'conforme, 0 écart' if not ecarts else f'{len(ecarts)} écart(s)'}")
    code = 1 if ecarts else 0
    if a.lanceur_artefact:
        sys.path.insert(0, str(a.source.resolve() / "src"))
        for m in [k for k in sys.modules if k.startswith("controle_ia")]:
            del sys.modules[m]
        art = importlib.import_module(f"controle_ia.neuron_lens.{a.lanceur_artefact}")
        actx = art.Contexte(depot, ctx.run_id, ctx.hf_home)
        ea, _ = controler(depot, enregistrer_b0(art, actx), art.p2.ESSAIS_B0, art.LLAMA)
        for e in ea:
            print(f"  artefact {a.lanceur_artefact} : {e}")
        print(f"ARTEFACT {a.lanceur_artefact} : {'pris en défaut' if ea else 'NON pris en défaut'} ({len(ea)} écart(s))")
        if not ea:
            code = 1
    return code


if __name__ == "__main__":
    sys.exit(main())
