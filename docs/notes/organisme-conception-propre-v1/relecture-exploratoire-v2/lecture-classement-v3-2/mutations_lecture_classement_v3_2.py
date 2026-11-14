#!/usr/bin/env python3
"""Banc de mutations de l'outil du lecteur v3.2 et du classement v3.2 — sur ce qui change depuis la v3.1.

Écrit le 14 novembre 2026 (vers 12:37 UTC, `date -u`) par le préparateur de la relecture (modèle A). Reprend le
harnais du banc v3.1 (`../../lecture-classement-v3-1/mutations_lecture_classement_v3_1.py`, `182f36cf…`) ; seuls les
mutants des changements de la v3.2 sont joués (C6 à côté de la première lecture, nom de manifeste, plafond absolu, pièces
v2, règle v2 : portes, S, L3 v2, séparation, absence de désignation, descriptifs) ; les 182 mutants de la v3.1 portent sur
du code inchangé (essai `test_regle_de_lecture_inchangee_v3_1_v3_2`).

Chaque mutant est une copie des deux programmes, dans un dossier temporaire hors du dépôt (même profondeur que dans le
dépôt), où une seule chaîne est remplacée (elle doit apparaître exactement une fois) ; les essais v3.2 sont joués contre
lui (`LC_MODULES`). Tué si les essais échouent. La base doit passer. Sous `unshare -n`, environnement réduit à PATH, LANG,
LC_ALL, TZ, TMPDIR, HOME (aucune clé, aucun mandataire). Trois passes en parallèle.

    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B mutations_lecture_classement_v3_2.py SORTIE.json
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
OUTIL, CLASSER = "outil_lecteur_conception_propre_v3_2.py", "classer_conception_propre_v3_2.py"
ESSAIS = ICI / "essais_lecture_classement_v3_2.py"

MUTANTS = [
    # outil : C6 v3.2, manifeste, plafond, pièces
    ("manifeste sous l'ancien nom (vu par la v3.1)", OUTIL, 'MANIFESTE = f"manifeste-relecture-{SUFFIXE}.json"',
     'MANIFESTE = f"manifeste-envois-{SUFFIXE}.json"'),
    ("première lecture non vérifiée", OUTIL, '    verifier_premiere_lecture(racine)\n    trouves', '    trouves'),
    ("empreinte de la première lecture non contrôlée", OUTIL,
     '        if h != attendue:\n            raise Refus(f"C6 (v3.2) : première lecture',
     '        if False:\n            raise Refus(f"C6 (v3.2) : première lecture'),
    ("première lecture absente tolérée", OUTIL,
     '        if not p.is_file():\n            raise Refus(f"C6 (v3.2) : première lecture : {nom} absent',
     '        if not p.is_file():\n            continue\n            raise Refus(f"C6 (v3.2) : première lecture : {nom} absent'),
    ("relevé : dépense non contrôlée", OUTIL,
     'if (not isinstance(r, dict) or r.get("depense_comptee_usd") != DEPENSE_PREMIERE_LECTURE_USD',
     'if (not isinstance(r, dict)'),
    ("motif de la relecture non cherché", OUTIL,
     'MOTIFS_MANIFESTES = ("manifeste-envois-v3*.json", "manifeste-relecture-v3*.json")',
     'MOTIFS_MANIFESTES = ("manifeste-envois-v3*.json",)'),
    ("motif v3 non cherché", OUTIL, 'MOTIFS_MANIFESTES = ("manifeste-envois-v3*.json", "manifeste-relecture-v3*.json")',
     'MOTIFS_MANIFESTES = ("manifeste-relecture-v3*.json",)'),
    ("manifeste de la première lecture non toléré", OUTIL,
     '    voulus = sorted([(racine / PREMIERE_LECTURE["manifeste"][0]).resolve()]\n                    + (',
     '    voulus = sorted([]\n                    + ('),
    ("plafond absolu de la v3.1", OUTIL, 'PLAFOND_ABSOLU_USD = 11.65', 'PLAFOND_ABSOLU_USD = 14.20'),
    ("dossier fixe de la v3.1", OUTIL, 'DOSSIER_ENVOIS_REL = f"{DOSSIER}/lecture-g1-v3-2/envois"',
     'DOSSIER_ENVOIS_REL = f"{DOSSIER}/lecture-g1-v3-1/envois"'),
    ("témoins du lecteur v1 en entrée", OUTIL,
     '''    "temoins_lecteur": (f"{DOSSIER}/relecture-exploratoire-v2/temoins-lecteur-v2.json",
                        "bb4f903f5a7fbe2366fb631afe708dcf93632e47c459acd86afbd425b93e295e"),''',
     '''    "temoins_lecteur": (f"{DOSSIER}/temoins-lecteur-v1.json",
                        "d11efe787cd27d2acb4b912487565896e43fc7cefbc7f51aa18080f3cdf8a77e"),'''),
    ("hasard v1 en entrée", OUTIL,
     '''    "temoins_hasard": (f"{DOSSIER}/relecture-exploratoire-v2/temoins-hasard-v2.json",
                       "5cef38f6d0545acd47859e87dd3de18846035570dfd32b7644be617d641b745d"),''',
     '''    "temoins_hasard": (f"{DOSSIER}/temoins-hasard-v1.json",
                       "b5e38724cf74b61e1db47f6dbc0e8f6955a0e4419723dc0ecd627854206c539d"),'''),
    ("règle v2 non épinglée", OUTIL,
     '''    "regle": (f"{DOSSIER}/relecture-exploratoire-v2/regle-v2.md",
              "56c58b096fd546ba05b68caebcf4e57cade9c2af1ea9b091de6770cbd36f3f24"),
''', ''),
    # classement : règle v2
    ("porte R7 rétablie", CLASSER, 'PORTES = ("R2", "R3")                  # règle v2', 'PORTES = ("R2", "R3", "R7")  # règle v2'),
    ("S v2 sans R7", CLASSER, 'return vec["R1"] + vec["R4"] + vec["R5"] + vec["R6"] + vec["R7"]',
     'return vec["R1"] + vec["R4"] + vec["R5"] + vec["R6"]'),
    ("L3 v2 : R7 exigé aux deux lectures", CLASSER, 'and d["N"] == "aucune" and d["R7_prouve_par"]\n',
     'and d["N"] == "aucune" and len(d["R7_prouve_par"]) == 2\n'),
    ("L3 v2 : R7 ignoré", CLASSER, 'and d["N"] == "aucune" and d["R7_prouve_par"]\n', 'and d["N"] == "aucune"\n'),
    ("L3 v2 : N ignorée", CLASSER, 'not d["portes_manquantes"] and d["N"] == "aucune" and d["R7_prouve_par"]',
     'not d["portes_manquantes"] and d["R7_prouve_par"]'),
    ("L3 v2 : R7 rendu non prouvé compté", CLASSER, '"R7_prouve_par": [L for L in O.LECTURES if v[L][i]["R7"]["compte"] == 1]',
     '"R7_prouve_par": [L for L in O.LECTURES if v[L][i]["R7"]["brut"] == 1]'),
    ("séparation lue sans L5", CLASSER, '    if not rejet_L5:\n        issue = "pas de séparation"',
     '    if False:\n        issue = "pas de séparation"'),
    ("issues réelle et de forme inversées", CLASSER,
     '        issue = "séparation réelle"\n    else:\n        issue = "séparation de forme"',
     '        issue = "séparation de forme"\n    else:\n        issue = "séparation réelle"'),
    ("graine de la séparation égale à celle de L5", CLASSER, 'ENTROPIE_SEPARATION = 2026111404',
     'ENTROPIE_SEPARATION = 2026111303'),
    ("séparation calculée sur C au lieu de R7", CLASSER,
     'sep = separation(L5["rejet"], [retenu[i]["R7"] for i in reelles], [retenu[i]["R7"] for i in hasard], permutations)',
     'sep = separation(L5["rejet"], C_reel, C_hasard, permutations)'),
    ("désignation rétablie", CLASSER, '"lecture_complete": lecture_complete, "designees": [],',
     '"lecture_complete": lecture_complete, "designees": cl["deux_premieres"] if (lisible and L5["rejet"]) else [],'),
    ("rang restreint à R7 inversé", CLASSER, 'rang_R7 = [i for i in cl["ordre_neuves"] if retenu[i]["R7"] == 1]',
     'rang_R7 = [i for i in cl["ordre_neuves"] if retenu[i]["R7"] == 0]'),
    ("exactitude : valeurs non fixées comptées", CLASSER, '                if att is None:\n                    continue\n',
     '                if att is None:\n                    att = 0\n'),
    ("hasard : chaînes cohérentes et contraires inversées", CLASSER, 'if coherence.get(i) is True},',
     'if coherence.get(i) is False},'),
    ("classement de la première lecture non épinglé", CLASSER,
     '    if h != attendue:\n        raise O.Refus(f"classement de la première lecture',
     '    if False:\n        raise O.Refus(f"classement de la première lecture'),
    ("relecture comparée à elle-même", CLASSER,
     'a, b = [f(retenu_1[i]) for i in communes], [f(retenu[i]) for i in communes]',
     'a, b = [f(retenu[i]) for i in communes], [f(retenu[i]) for i in communes]'),
    ("règle v2 sur la première lecture : valeurs de la relecture", CLASSER,
     '    cl = classer(communes, retenu_1, cout_de, departage)', '    cl = classer(communes, {i: {**retenu_1[i], "R2": 0} for i in communes}, cout_de, departage)'),
]


def jouer(dossier: Path, delai=900) -> tuple[bool, str]:
    env = {k: v for k, v in os.environ.items() if k in ("PATH", "LANG", "LC_ALL", "TZ", "HOME")}
    env.update({"LC_MODULES": str(dossier), "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(dossier.parents[4])})
    c = subprocess.run(["unshare", "-n", sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                        "--basetemp", str(dossier.parents[4] / "pytest"), str(ESSAIS)],
                       capture_output=True, text=True, env=env, timeout=delai, cwd=str(ICI.parents[4]))
    lignes = c.stdout.strip().splitlines() or [""]
    echec = next((l for l in lignes if l.startswith("FAILED") or l.startswith("ERROR")), "")
    return c.returncode == 0, lignes[-1] + (" | " + echec[:160] if echec else "")


def un_mutant(tmp: Path, base: Path, k: int, mutant) -> dict:
    nom, fichier, ancien, nouveau = mutant
    d = tmp / f"m{k:03d}" / "docs" / "notes" / "o" / "r" / "lecture-classement-v3-2"
    shutil.copytree(base, d)
    texte = (d / fichier).read_text(encoding="utf-8")
    if texte.count(ancien) != 1:
        return {"mutant": k, "nom": nom, "fichier": fichier, "statut": "inapplicable", "occurrences": texte.count(ancien)}
    (d / fichier).write_text(texte.replace(ancien, nouveau), encoding="utf-8")
    survit, ligne = jouer(d)
    shutil.rmtree(tmp / f"m{k:03d}", ignore_errors=True)
    return {"mutant": k, "nom": nom, "fichier": fichier, "statut": "survivant" if survit else "tue", "sortie": ligne}


def main(sortie: str) -> int:
    from concurrent.futures import ThreadPoolExecutor
    debut = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with tempfile.TemporaryDirectory(prefix="mut-lc-v3-2-") as tmp:
        tmp = Path(tmp)
        base = tmp / "base" / "docs" / "notes" / "o" / "r" / "lecture-classement-v3-2"
        base.mkdir(parents=True)
        for n in (OUTIL, CLASSER):
            shutil.copyfile(ICI / n, base / n)
        ok, ligne_base = jouer(base)
        if not ok:
            print("la base échoue : " + ligne_base, file=sys.stderr)
            return 1
        with ThreadPoolExecutor(max_workers=3) as ex:
            futurs = [ex.submit(un_mutant, tmp, base, k, m) for k, m in enumerate(MUTANTS, 1)]
            resultats = []
            for f in futurs:
                r = f.result()
                resultats.append(r)
                print(f"{r['mutant']:03d} {dict(tue='tué', survivant='SURVIT', inapplicable='INAPPLICABLE')[r['statut']]}"
                      f" — {r['nom']}", flush=True)
    tues = sum(r["statut"] == "tue" for r in resultats)
    res = {"banc": "mutations-lecture-classement-v3-2", "debut_utc": debut,
           "fin_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "base": ligne_base,
           "isolement": "unshare -n ; environnement : PATH, LANG, LC_ALL, TZ, TMPDIR, HOME",
           "mutants": len(MUTANTS), "tues": tues,
           "survivants": [r["nom"] for r in resultats if r["statut"] == "survivant"],
           "inapplicables": [r["nom"] for r in resultats if r["statut"] == "inapplicable"], "detail": resultats}
    Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{tues} tués sur {len(MUTANTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
