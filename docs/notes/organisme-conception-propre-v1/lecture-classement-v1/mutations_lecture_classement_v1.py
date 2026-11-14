#!/usr/bin/env python3
"""Banc de mutations de l'outil du lecteur et du programme de classement — course « conception propre » — v1.

Chaque mutant est une copie des deux programmes, dans un dossier temporaire hors du dépôt, où une seule chaîne est
remplacée (elle doit apparaître exactement une fois) ; les essais (`essais_lecture_classement_v1.py`) sont joués contre
lui (`LC_MODULES`). Un mutant est tué si les essais échouent. La base (sans mutation) doit passer.

    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B mutations_lecture_classement_v1.py SORTIE.json
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
OUTIL, CLASSER = "outil_lecteur_conception_propre_v1.py", "classer_conception_propre_v1.py"
ESSAIS = ICI / "essais_lecture_classement_v1.py"

MUTANTS = [
    # vérification mot pour mot (§ 4.5)
    ("citation non vérifiée", OUTIL, 'if any(f in espaces(t) for f in formes for t in textes):', 'if True:'),
    ("espaces non normalisés", OUTIL, 'return re.sub(r"\\s+", " ", s).strip()', 'return s'),
    ("passage cherché dans la fiche entière jointe (à cheval sur deux champs)", OUTIL,
     'if any(f in espaces(t) for f in formes for t in textes):', 'if p in espaces(" ".join(textes)):'),
    ("passage vide accepté", OUTIL, 'if not p:\n        return False, "passage vide"', 'if False:\n        pass'),
    ("passage du catalogue non vérifié", OUTIL, 'if ok_f and ok_c:', 'if ok_f:'),
    ("valeur « 1 » en chaîne acceptée", OUTIL, 'if type(brut) is not int or brut not in (0, 1):',
     'if str(brut) not in ("0", "1"):'),
    ("R4 hors levier:juge lu au lieu de 1", OUTIL, 'if c == "R4" and not juge:', 'if False:'),
    ("entrée en double : la première retenue", OUTIL, 'elif len(entrees) > 1:', 'elif len(entrees) > 99:'),
    ("modèle servi non vérifié", OUTIL, 'if r.get("model") != MODELE_LECTEUR:', 'if False:'),
    ("réponse non scellée acceptée", OUTIL, '    verifier_sceau(chemin)\n    r = json.loads', '    r = json.loads'),
    # préparation, aveugle, graines, garde
    ("auteur servi au lecteur", OUTIL, 'vue, retires = {}, [k for k', 'vue, retires = {"auteur": fiche.get("auteur", "")}, [k for k'),
    ("ordre des clés non canonique (trahit l'origine)", OUTIL, 'return normaliser_objet(vue), sorted(retires)',
     'return normaliser_objet({k: vue[k] for k in sorted(vue)} if "identifiant_auteur" in fiche else vue), sorted(retires)'),
    ("typographie non normalisée", OUTIL, 'return normaliser_objet(vue), sorted(retires)', 'return vue, sorted(retires)'),
    ("même ordre pour les deux lectures", OUTIL, 'default_rng(e[i]).permutation(n)', 'default_rng(e[0]).permutation(n)'),
    ("graine des ordres changée", OUTIL, 'ENTROPIE_ORDRES = 2026111302', 'ENTROPIE_ORDRES = 2026111301'),
    ("lots de 25", OUTIL, 'TAILLE_LOT = 20', 'TAILLE_LOT = 25'),
    ("garde du nombre d'appels retirée", OUTIL, 'if appels > MAX_APPELS:', 'if False:'),
    ("garde de dépense retirée", OUTIL, 'if max_tok < MIN_TOKENS:', 'if False:'),
    ("attestation non vérifiée", OUTIL, '    att = verifier_attestation(attestation_chemin, sha_fiches)\n',
     '    att = json.loads(Path(attestation_chemin).read_text(encoding="utf-8"))\n'),
    ("attestation : drapeau d'envoi ignoré", OUTIL,
     'or a["envoi_au_lecteur_externe_permis"] is not True:', 'or False:'),
    ("admissibilité : deux leviers admis", OUTIL, 'if len(lev) != 1:', 'if len(lev) < 1:'),
    ("admissibilité : nature « rien » admise", OUTIL, 'NATURES_ADMISES = ("modification", "ajout")',
     'NATURES_ADMISES = ("modification", "ajout", "rien")'),
    ("pièce épinglée non vérifiée", OUTIL, 'if h != attendue:', 'if False:'),
    ("écrasement permis", OUTIL, 'if p.exists() or Path(str(p) + ".sha256").exists():', 'if False:'),
    # classement (§ 4.5 à 4.7)
    ("R retenu si une seule lecture", CLASSER, 'v1[c]["compte"] == 1 and v2[c]["compte"] == 1',
     'v1[c]["compte"] == 1 or v2[c]["compte"] == 1'),
    ("N aucune si une seule lecture le dit", CLASSER, '"aucune" if (n1 == "aucune" and n2 == "aucune")',
     '"aucune" if (n1 == "aucune" or n2 == "aucune")'),
    ("porte R7 oubliée", CLASSER, 'PORTES = ("R2", "R3", "R7")', 'PORTES = ("R2", "R3")'),
    ("S compte R2 au lieu de R6", CLASSER, 'return vec["R1"] + vec["R4"] + vec["R5"] + vec["R6"]',
     'return vec["R1"] + vec["R4"] + vec["R5"] + vec["R2"]'),
    ("coût inversé", CLASSER, 'COUT_RANG = {"processeur": 0, "depense": 1}', 'COUT_RANG = {"processeur": 1, "depense": 0}'),
    ("départage par l'enfant 3", CLASSER, 'default_rng(O.enfants_ordres()[2])', 'default_rng(O.enfants_ordres()[3])'),
    ("témoin à score non permuté", CLASSER, 'vec_p = {ids[i]: vec_de[ids[perm[i]]]', 'vec_p = {ids[i]: vec_de[ids[i]]'),
    ("désignées sans L5", CLASSER, 'if (lisible and L5["rejet"]) else []', 'if lisible else []'),
    ("désignées sans lisibilité", CLASSER, 'if (lisible and L5["rejet"]) else []', 'if L5["rejet"] else []'),
    # L1 à L5, Holm
    ("L1 à 4 publiées", CLASSER, 'L1_MIN_PUBLIEES = 5', 'L1_MIN_PUBLIEES = 4'),
    ("L1 sans l'entrée attendue", CLASSER, 'if v[L][p["id"]]["N"]["compte"] == p["entree"]]',
     'if v[L][p["id"]]["N"]["compte"] != "aucune"]'),
    ("L2 sur une seule lecture", CLASSER, 'all(d[L] == 0 for d in L2_detail.values() for L in O.LECTURES)',
     'all(d["L1"] == 0 for d in L2_detail.values())'),
    ("L3 sans la nouveauté", CLASSER, 'not d["portes_manquantes"] and d["N"] == "aucune"', 'not d["portes_manquantes"]'),
    ("L4 sans seuil de κ (−1)", CLASSER, 'L4_KAPPA_MIN, L4_ACCORD_MIN = 0.4, 0.8', 'L4_KAPPA_MIN, L4_ACCORD_MIN = -1.0, 0.8'),
    ("L4 sans repli sur l'accord brut", CLASSER, 'constante = pa in (0.0, 1.0) or pb in (0.0, 1.0)',
     'constante = kappa is None'),
    ("L5 au seuil 0,1", CLASSER, 'SEUIL_P = 0.05', 'SEUIL_P = 0.1'),
    ("L5 bilatérale", CLASSER, 't5 = test_permutation(C_reel, C_hasard, np.random.SeedSequence(ENTROPIE_TEST), permutations)',
     't5 = test_permutation(C_reel, C_hasard, np.random.SeedSequence(ENTROPIE_TEST), permutations, bilateral=True)'),
    ("L5 statistique inversée", CLASSER, 'k += int((np.abs(dd) >= abs(obs)).sum() if bilateral else (dd >= obs).sum())',
     'k += int((np.abs(dd) >= abs(obs)).sum() if bilateral else (dd <= obs).sum())'),
    ("valeur p sans le +1", CLASSER, 'return {"p": (1 + k) / (1 + permutations)', 'return {"p": k / permutations'),
    ("C sans la nouveauté", CLASSER, 'if (not portes_manquantes(vec) and vec["N"] == "aucune") else 0',
     'if not portes_manquantes(vec) else 0'),
    ("Holm remplacé par Bonferroni", CLASSER, 'courant = max(courant, min(1.0, (k - r) * p[i]))',
     'courant = min(1.0, k * p[i])'),
    ("E5 au seuil 0,9", CLASSER, 'E5_PART = 0.8', 'E5_PART = 0.9'),
]


def jouer(dossier: Path, delai=600) -> tuple[bool, str]:
    env = {k: v for k, v in os.environ.items() if k in ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR", "HOME")}
    env.update({"LC_MODULES": str(dossier), "PYTHONDONTWRITEBYTECODE": "1"})
    c = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", str(ESSAIS)],
                       capture_output=True, text=True, env=env, timeout=delai, cwd=str(ICI.parents[3]))
    derniere = (c.stdout.strip().splitlines() or [""])[-1]
    return c.returncode == 0, derniere


def main(sortie: str) -> int:
    debut = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    resultats = []
    with tempfile.TemporaryDirectory(prefix="mut-lc-v1-") as tmp:
        # même profondeur que dans le dépôt (la racine par défaut des programmes est le 4e parent) ; les essais
        # passent toujours la vraie racine du dépôt
        base = Path(tmp) / "base" / "docs" / "notes" / "o" / "lecture-classement-v1"
        base.mkdir(parents=True)
        for n in (OUTIL, CLASSER):
            shutil.copyfile(ICI / n, base / n)
        ok, ligne = jouer(base)
        if not ok:
            print("la base échoue : " + ligne, file=sys.stderr)
            return 1
        for k, (nom, fichier, ancien, nouveau) in enumerate(MUTANTS, 1):
            d = Path(tmp) / f"m{k:02d}" / "docs" / "notes" / "o" / "lecture-classement-v1"
            shutil.copytree(base, d)
            texte = (d / fichier).read_text(encoding="utf-8")
            if texte.count(ancien) != 1:
                resultats.append({"mutant": k, "nom": nom, "fichier": fichier, "statut": "inapplicable",
                                  "occurrences": texte.count(ancien)})
                continue
            (d / fichier).write_text(texte.replace(ancien, nouveau), encoding="utf-8")
            survit, ligne = jouer(d)
            resultats.append({"mutant": k, "nom": nom, "fichier": fichier,
                              "statut": "survivant" if survit else "tue", "sortie": ligne})
            print(f"{k:02d} {'SURVIT' if survit else 'tué'} — {nom}", flush=True)
    tues = sum(r["statut"] == "tue" for r in resultats)
    res = {"banc": "mutations-lecture-classement-v1", "debut_utc": debut,
           "fin_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "base": ligne_base(ok),
           "mutants": len(MUTANTS), "tues": tues,
           "survivants": [r["nom"] for r in resultats if r["statut"] == "survivant"],
           "inapplicables": [r["nom"] for r in resultats if r["statut"] == "inapplicable"], "detail": resultats}
    Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{tues} tués sur {len(MUTANTS)}")
    return 0


def ligne_base(ok):
    return "base : essais passés" if ok else "base en échec"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
