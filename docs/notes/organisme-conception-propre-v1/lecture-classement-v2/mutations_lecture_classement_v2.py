#!/usr/bin/env python3
"""Banc de mutations de l'outil du lecteur et du programme de classement — course « conception propre » — v2.

v2 : mutants de la v1 (adaptés aux lignes changées) ; les neuf mutations survivantes de la contre-lecture (R-2627),
reconstituées d'après leur description ; mutants des corrections M1, M2, M3 et de la variante détachée de L5.

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
OUTIL, CLASSER = "outil_lecteur_conception_propre_v2.py", "classer_conception_propre_v2.py"
ESSAIS = ICI / "essais_lecture_classement_v2.py"

MUTANTS = [
    # vérification mot pour mot (§ 4.5)
    ("citation non vérifiée", OUTIL, 'if any(f in espaces(t) for f in formes for t in textes):', 'if True:'),
    ("espaces non normalisés", OUTIL, 'return re.sub(r"\\s+", " ", s).strip()', 'return s'),
    ("passage cherché dans la fiche entière jointe (à cheval sur deux champs)", OUTIL,
     'if any(f in espaces(t) for f in formes for t in textes):', 'if p in espaces(" ".join(textes)):'),
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
    ("CL : L4 jugée sur R7 seul", CLASSER, 'L4 = {"tient": k_R7["tient"] and k_N["tient"]', 'L4 = {"tient": k_R7["tient"]'),
    ("CL : κ au seuil strict", CLASSER, 'tient, jugee = kappa >= Fraction(L4_KAPPA_MIN)', 'tient, jugee = kappa > Fraction(L4_KAPPA_MIN)'),
    ("κ en flottants (0,4 calculé 0,3999…)", CLASSER,
     'kappa = None if pe == 1 else (po - pe) / (1 - pe)',
     'kappa = None if pe == 1 else Fraction((float(po) - float(pe)) / (1 - float(pe)))'),
    ("L4 sans repli sur l'accord brut", CLASSER, 'constante = pa in (0, 1) or pb in (0, 1)',
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
    ("E5 au seuil 0,9", CLASSER, 'E5_PART = Fraction(4, 5)', 'E5_PART = Fraction(9, 10)'),
    ("CL : E5 au seuil large", CLASSER, '(Fraction(len(occupees), len(passees)) > E5_PART)',
     '(Fraction(len(occupees), len(passees)) >= E5_PART)'),
    ("CL : comparaisons descriptives unilatérales", CLASSER, 'enfants[k], permutations, bilateral=True)',
     'enfants[k], permutations, bilateral=False)'),
    ("CL : audit exigeant les quatre signes", CLASSER, 'audit["declenche"] = any(audit.values())',
     'audit["declenche"] = all(audit.values())'),
    ("CL : catalogue cherché dans toutes les entrées", OUTIL, '[sans_gras(cat[brut][CELLULE_MECANISME])])',
     '[sans_gras(t) for e in cat.values() for t in e])'),
    ("CL : occupation sans passage de la fiche", OUTIL, 'if ok_f and ok_c:', 'if ok_c:'),
    ("CL : typographie du passage tolérée", OUTIL, 'p = espaces(passage)\n', 'p = espaces(normaliser_typographie(passage))\n'),
    ("CL : étiquette hors lot gardée", OUTIL,
     '            anomalies.append({"genre": "etiquette_hors_lot", "detail": str(et)[:40]})\n            continue\n',
     '            anomalies.append({"genre": "etiquette_hors_lot", "detail": str(et)[:40]})\n'),
    # M1
    ("M1 : longueur minimale retirée", OUTIL, '    if court(p):  # passage vide compris\n', '    if False:\n'),
    ("M1 : seuil de 20 abaissé à 4", OUTIL, 'LONGUEUR_MIN_PASSAGE = 20 ', 'LONGUEUR_MIN_PASSAGE = 4 '),
    ("M1 : catalogue lu dans toute la ligne Ck", OUTIL, '[sans_gras(cat[brut][CELLULE_MECANISME])])',
     '[sans_gras(t) for t in cat[brut]])'),
    ("M1 : catalogue lu dans la cellule du nom", OUTIL, 'CELLULE_MECANISME = 2 ', 'CELLULE_MECANISME = 1 '),
    # M2
    ("M2 : lot illisible non bloquant", OUTIL, 'ANOMALIES_BLOQUANTES = ("reponse_illisible", "fin_non_stop",',
     'ANOMALIES_BLOQUANTES = ("fin_non_stop",'),
    ("M2 : fin non stop non bloquante", OUTIL, 'ANOMALIES_BLOQUANTES = ("reponse_illisible", "fin_non_stop",',
     'ANOMALIES_BLOQUANTES = ("reponse_illisible",'),
    ("M2 : entrée manquante non bloquante", OUTIL, '"entree_manquante", "entree_en_double")', '"entree_en_double")'),
    ("M2 : lisibilité sans la complétude", CLASSER, 'lisible = complete and L1["tient"]', 'lisible = L1["tient"]'),
    ("M2 : verdict muet sur l'illisible", CLASSER, '    elif not complete:\n', '    elif False:\n'),
    # M3
    ("M3 : chemin non contrôlé", OUTIL, '            or parties[-1] != NOM_COPIE_FICHES):', '            or False):'),
    ("M3 : dossier de run non contrôlé", OUTIL, 'or not re.fullmatch(MOTIF_RUN, parties[len(attendu)])', 'or False'),
    ("M3 : lien symbolique admis", OUTIL, 'if p.is_symlink() or any(', 'if False and any('),
    ("M3 : code de fin ignoré", OUTIL, 'if not isinstance(fin, dict) or fin.get("code") != 0:', 'if not isinstance(fin, dict):'),
    ("M3 : empreinte du manifeste de fin ignorée", OUTIL,
     'if (fin.get("pour_l_attestation") or {}).get("fiches_validees_sha256") != sha:', 'if False:'),
    ("M3 : forme des éléments non vérifiée", OUTIL, '    verifier_forme_fiches_validees(fiches)\n', ''),
    ("M3 : pile sans fiche réelle admise", OUTIL, 'if not any(p["origine"] == "reelle" for p in pile["fiches"]):', 'if False:'),
    ("M3 : provenance non revérifiée au classement", CLASSER,
     'if prov["sha256"] != man["fiches_validees"]["sha256"] or prov["run"]', 'if False and prov["run"]'),
    # variante
    ("variante active par défaut", CLASSER, 'def classement(dossier_envois, racine=O.RACINE_DEFAUT, permutations=PERMUTATIONS, designation="L5",',
     'def classement(dossier_envois, racine=O.RACINE_DEFAUT, permutations=PERMUTATIONS, designation="detachee-v1",'),
    ("variante sans mot de Lazar", CLASSER, 'if designation != "L5" and not (isinstance(decision, str)', 'if False and not (isinstance(decision, str)'),
    ("variante au seuil large", CLASSER, 'if score_C(retenu[i]) > max_h]', 'if score_C(retenu[i]) >= max_h]'),
    ("variante sans lisibilité", CLASSER, 'if score_C(retenu[i]) > max_h] if lisible else []', 'if score_C(retenu[i]) > max_h]'),
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
