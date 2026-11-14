#!/usr/bin/env python3
"""Banc de mutations de l'outil du lecteur et du programme de classement — course « conception propre » — v3.1.

v3.1 : les mutants du banc v3 (cinq adaptés aux lignes changées : pièce épinglée, deux anomalies bloquantes, plafond à la
préparation, chaîne du journal ; « exception de transport non masquée » retiré, remplacé par « message d'exception de
transport écrit », B1), plus les mutants des corrections de la v3.1 : B1 (clé), B2 (redirections), M1 (réponses hors journal),
C6 (un seul dossier), M3, M4, écarts d'envoi bloquants, palier et prix lus, revalidation du manifeste, bilan, racine du
classement.

Chaque mutant est une copie des deux programmes, dans un dossier temporaire hors du dépôt, où une seule chaîne est
remplacée (elle doit apparaître exactement une fois) ; les essais (`essais_lecture_classement_v3_1.py`) sont joués
contre lui (`LC_MODULES`). Un mutant est tué si les essais échouent. La base (sans mutation) doit passer.

Hors réseau, par construction : chaque passe tourne sous `unshare -n` (espace de noms réseau vide ; les essais du
transport réel montent la seule boucle locale), environnement réduit à PATH, LANG, LC_ALL, TZ, TMPDIR, HOME (aucune
clé, aucun mandataire). Trois passes en parallèle.

    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B mutations_lecture_classement_v3_1.py SORTIE.json
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
OUTIL, CLASSER = "outil_lecteur_conception_propre_v3_1.py", "classer_conception_propre_v3_1.py"
ESSAIS = ICI / "essais_lecture_classement_v3_1.py"

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
    ("réponse non scellée acceptée", OUTIL, '    verifier_sceau(chemin)\n    nom = Path(chemin).name', '    nom = Path(chemin).name'),
    # préparation, aveugle, graines, garde
    ("auteur servi au lecteur", OUTIL, 'vue, retires = {}, [k for k', 'vue, retires = {"auteur": fiche.get("auteur", "")}, [k for k'),
    ("ordre des clés non canonique (trahit l'origine)", OUTIL, 'return normaliser_objet(vue), sorted(retires)',
     'return normaliser_objet({k: vue[k] for k in sorted(vue)} if "identifiant_auteur" in fiche else vue), sorted(retires)'),
    ("typographie non normalisée", OUTIL, 'return normaliser_objet(vue), sorted(retires)', 'return vue, sorted(retires)'),
    ("même ordre pour les deux lectures", OUTIL, 'default_rng(e[i]).permutation(n)', 'default_rng(e[0]).permutation(n)'),
    ("graine des ordres changée", OUTIL, 'ENTROPIE_ORDRES = 2026111302', 'ENTROPIE_ORDRES = 2026111301'),
    ("lots de 15 (taille de l'échec de R-2658)", OUTIL, 'TAILLE_LOT = 5\n', 'TAILLE_LOT = 15\n'),
    ("garde du nombre d'appels retirée", OUTIL, 'if appels > MAX_APPELS:', 'if False:'),
    ("attestation non vérifiée", OUTIL, '    att = verifier_attestation(attestation_chemin, sha_fiches)\n',
     '    att = json.loads(Path(attestation_chemin).read_text(encoding="utf-8"))\n'),
    ("attestation : drapeau d'envoi ignoré", OUTIL,
     'or a["envoi_au_lecteur_externe_permis"] is not True:', 'or False:'),
    ("admissibilité : deux leviers admis", OUTIL, 'if len(lev) != 1:', 'if len(lev) < 1:'),
    ("admissibilité : nature « rien » admise", OUTIL, 'NATURES_ADMISES = ("modification", "ajout")',
     'NATURES_ADMISES = ("modification", "ajout", "rien")'),
    ("pièce épinglée non vérifiée", OUTIL, '    if h != attendue:\n        raise Refus(f"pièce {nom}', '    if False:\n        raise Refus(f"pièce {nom}'),
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
     '            anomalies.append({"genre": "etiquette_hors_lot", "detail": str(et)[:40], "etiquettes": []})\n            continue\n',
     '            anomalies.append({"genre": "etiquette_hors_lot", "detail": str(et)[:40], "etiquettes": []})\n'),
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
    ("M2 : entrée manquante non bloquante", OUTIL, '"entree_manquante", "entree_en_double",\n', '"entree_en_double",\n'),
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
    # v3 : anomalies bloquantes neuves (C1, réponse absente, modèle servi, refus)
    ("C1 : clé manquante non bloquante", OUTIL, '"cle_de_critere_manquante", "reponse_absente",', '"reponse_absente",'),
    ("C1 : manque non détecté", OUTIL, '            if manque:  # C1', '            if False:  # C1'),
    ("C1 : R4 exempté", OUTIL, 'return [c for c in CLES_ENTREE if', 'return [c for c in CLES_ENTREE if c != "R4" and'),
    ("C1 : valeur nulle acceptée", OUTIL, 'and e[c].get("valeur") is not None)]', ')]'),
    ("réponse absente non bloquante", OUTIL, '"reponse_absente", "modele_servi_different",', '"modele_servi_different",'),
    ("réponse absente acceptée sans arrêt consigné", OUTIL,
     '            if not arret:\n                raise Refus(f"réponse attendue absente',
     '            if False:\n                raise Refus(f"réponse attendue absente'),
    ("vérification : modèle servi non bloquant", OUTIL, '"modele_servi_different", "refus_du_lecteur",\n',
     '"refus_du_lecteur",\n'),
    ("vérification : refus du lecteur non bloquant", OUTIL, '"modele_servi_different", "refus_du_lecteur",\n',
     '"modele_servi_different",\n'),
    ("vérification : modèle par préfixe", OUTIL, '    if r.get("model") != MODELE_LECTEUR:\n        an.append(',
     '    if not str(r.get("model")).startswith(MODELE_LECTEUR[:5]):\n        an.append('),
    ("vérification : contenu lu malgré le modèle", OUTIL,
     'if any(g in ("modele_servi_different", "refus_du_lecteur") for g, _ in an) or not isinstance(contenu, str):',
     'if not isinstance(contenu, str):'),
    ("vérification : anomalie d'envoi non rapportée", OUTIL, '        if ev and ev.get("anomalies"):', '        if False:'),
    # v3 : corps de la requête, lecteur, point d'entrée
    ("effort non transmis", OUTIL, '"reasoning_effort": effort, "store": False}', '"store": False}'),
    ("store omis", OUTIL, '"reasoning_effort": effort, "store": False}', '"reasoning_effort": effort}'),
    ("max_tokens au lieu de max_completion_tokens", OUTIL, '"max_completion_tokens": MAX_SORTIE, "reasoning_effort": effort, "store"',
     '"max_tokens": MAX_SORTIE, "reasoning_effort": effort, "store"'),
    ("point d'entrée Responses", OUTIL, 'URL_AMONT = "https://api.openai.com/v1/chat/completions"',
     'URL_AMONT = "https://api.openai.com/v1/responses"'),
    ("modèle du lecteur changé", OUTIL, 'MODELE_LECTEUR = "gpt-6-astra"', 'MODELE_LECTEUR = "kimi-k3.1-pro"'),
    ("plafond de sortie abaissé", OUTIL, 'MAX_SORTIE = 32768 ', 'MAX_SORTIE = 16384 '),
    ("effort « max » admis", OUTIL, 'EFFORTS = ("low", "medium", "high")', 'EFFORTS = ("low", "medium", "high", "max")'),
    # v3 : analyse d'une réponse à l'envoi
    ("envoi : modèle servi non vérifié", OUTIL, '    if r["modele_servi"] != MODELE_LECTEUR:\n        r["anomalies"].append(',
     '    if False:\n        r["anomalies"].append('),
    ("envoi : modèle servi par préfixe", OUTIL, '    if r["modele_servi"] != MODELE_LECTEUR:\n        r["anomalies"].append(',
     '    if not str(r["modele_servi"]).startswith(MODELE_LECTEUR):\n        r["anomalies"].append('),
    ("envoi : fin non stop ignorée", OUTIL, '    if r["finish_reason"] != "stop":\n        r["anomalies"].append("fin_non_stop")',
     '    if False:\n        r["anomalies"].append("fin_non_stop")'),
    ("envoi : refus du lecteur ignoré", OUTIL, '    if msg.get("refusal"):\n        r["anomalies"].append("refus_du_lecteur")',
     '    if False:\n        r["anomalies"].append("refus_du_lecteur")'),
    ("envoi : usage absent compté zéro", OUTIL, '        r["anomalies"].append("usage_absent")\n',
     '        r["anomalies"].append("usage_absent")\n        r["cout_usd"] = 0.0\n'),
    ("envoi : usage absent sans anomalie", OUTIL, '        r["anomalies"].append("usage_absent")\n', '        pass\n'),
    ("envoi : usage incohérent accepté", OUTIL, '    elif probleme:\n', '    elif False:\n'),
    ("envoi : coût au-dessus du pire cas accepté", OUTIL, 'if cout > pire_cas + 1e-12:', 'if False:'),
    ("envoi : statut 429 gardé comme réponse", OUTIL, '    if statut != 200:\n', '    if statut not in (200, 429):\n'),
    ("envoi : pas d'arrêt à la première anomalie", OUTIL,
     """            issue, detail = "anomalie", f"{e['envoi']} : {', '.join(a['anomalies'])}"\n            break\n""",
     """            issue, detail = "anomalie", f"{e['envoi']} : {', '.join(a['anomalies'])}"\n"""),
    # v3 : coût lu
    ("coût : cache au prix d'entrée", OUTIL, '+ min(cache, p) * prix["cache"]', '+ min(cache, p) * prix["entree"]'),
    ("coût : raisonnement compté deux fois", OUTIL, '+ c * prix["sortie"]', '+ (c + raison) * prix["sortie"]'),
    ("coût : excédent de total ignoré", OUTIL, '+ exces * haut', '+ 0'),
    ("coût : sortie au-delà du plafond admise", OUTIL, '    elif c > MAX_SORTIE:\n', '    elif False:\n'),
    # v3 : garde de dépense et d'appels
    ("garde : plafond retiré à l'envoi", OUTIL, 'if j["depense_usd"] + pire > plafond + 1e-12:', 'if False:'),
    ("garde : plafond sans la dépense passée", OUTIL, 'if j["depense_usd"] + pire > plafond + 1e-12:',
     'if pire > plafond + 1e-12:'),
    ("garde : pire cas sans la sortie", OUTIL, ' + MAX_SORTIE * prix["sortie"] / 1e6', ''),
    ("garde : pire cas d'entrée sans la marge", OUTIL, 'return (octets + OCTETS_MARGE) * prix', 'return (octets) * prix'),
    ("garde : nombre d'appels non contrôlé à l'envoi", OUTIL, 'if j["appels"] >= appels_max:', 'if False:'),
    ("garde : MAX_APPELS relevé à 20", OUTIL, 'MAX_APPELS = 18 ', 'MAX_APPELS = 20 '),
    ("garde : plafond absolu retiré", OUTIL, 'if plafond_usd > disponible + 1e-9:', 'if False:'),
    ("garde : plafond sous un seul appel admis", OUTIL, 'if plus_gros > plafond_usd:', 'if False:'),
    ("garde : prix nul admis", OUTIL, 'or v <= 0:', 'or v < 0:'),
    ("garde : effort non contrôlé", OUTIL, '    if effort not in EFFORTS:\n        raise', '    if False:\n        raise'),
    # v3 : journal de dépense et reprise
    ("journal : coûts clos non sommés", OUTIL, '            etat["depense_usd"] += ev["cout_usd"]\n', ''),
    ("journal : appel sans clôture non compté", OUTIL, '        etat["depense_usd"] += ev["pire_cas_usd"]\n', ''),
    ("journal : chaîne non vérifiée", OUTIL,
     'if not isinstance(ev, dict) or ev.get("n") != i + 1 or ev.get("precedent") != etat["dernier_sha256"]:',
     'if not isinstance(ev, dict):'),
    ("reprise après anomalie ou arrêt permise", OUTIL, 'if j["anomalies"] or j["arret"]:', 'if False:'),
    ("reprise après appel sans clôture permise", OUTIL, '    if j["en_vol"]:\n        raise Refus(f"appel sans clôture',
     '    if False:\n        raise Refus(f"appel sans clôture'),
    ("cohérence réponses-journal non contrôlée", OUTIL, '    controler_coherence(dossier, man, j)\n    if j["en_vol"]:',
     '    if j["en_vol"]:'),
    ("envois d'une autre version admis", OUTIL, '    if man.get("version") != VERSION:\n', '    if False:\n'),
    # v3 : clé et corps d'erreur
    ("clé non retirée de l'environnement", OUTIL, 'cle = os.environ.pop(VARIABLE_CLE, None)', 'cle = os.environ.get(VARIABLE_CLE)'),
    ("corps d'erreur écrit", OUTIL, '"corps_octets": len(rep) if rep is not None else None,',
     '"corps_octets": len(rep) if rep is not None else None, "corps": rep.decode("utf-8", "replace") if rep else None,'),
    ("clé absente : envoi quand même", OUTIL, '    if not cle:\n        raise Refus(f"{VARIABLE_CLE} absente',
     '    if False:\n        raise Refus(f"{VARIABLE_CLE} absente'),
    ("transport réel : adresse non contrôlée", OUTIL, '    if url != URL_AMONT:\n        raise Refus("adresse',
     '    if False:\n        raise Refus("adresse'),
    # v3.1 : B1, la clé
    ("B1 : clé hors ASCII imprimable admise", OUTIL, '    if not MOTIF_CLE.fullmatch(cle):\n        raise Refus(',
     '    if False:\n        raise Refus('),
    ("B1 : motif de clé admettant les fins de ligne", OUTIL, r'MOTIF_CLE = re.compile(r"[\x21-\x7e]{1,512}")',
     r'MOTIF_CLE = re.compile(r"[\s\S]{1,512}")'),
    ("B1 : réponse non expurgée", OUTIL, '            brut, expurgee = expurger(rep, cle)\n',
     '            brut, expurgee = rep, False\n'),
    ("B1 : journal non expurgé", OUTIL, '    if cle:\n        ligne, _ = expurger(ligne, cle)',
     '    if False:\n        ligne, _ = expurger(ligne, cle)'),
    ("B1 : anomalie cle_dans_la_reponse omise", OUTIL, '        if expurgee:\n            a["anomalies"].append("cle_dans_la_reponse")',
     '        if False:\n            a["anomalies"].append("cle_dans_la_reponse")'),
    ("B1 : formes échappées omises", OUTIL,
     r'formes = {cle, j, cle.replace("/", "\\/"), j.replace("/", "\\/"), urllib.parse.quote(cle, safe=""), repr(cle)[1:-1]}',
     'formes = {cle}'),
    ("B1 : message d'exception de transport écrit", OUTIL, 'statut, rep, cause = None, None, type(ex).__name__',
     'statut, rep, cause = None, None, f"{type(ex).__name__}: {ex}"'),
    # v3.1 : B2, redirections
    ("B2 : redirections suivies (gestionnaire par défaut)", OUTIL,
     'build_opener(SansRedirection, urllib.request.HTTPSHandler', 'build_opener(urllib.request.HTTPSHandler'),
    ("B2 : redirect_request rend la requête suivante", OUTIL,
     '    def redirect_request(self, req, fp, code, msg, headers, newurl):\n        return None',
     '    def redirect_request(self, req, fp, code, msg, headers, newurl):\n'
     '        return urllib.request.HTTPRedirectHandler.redirect_request(self, req, fp, code, msg, headers, newurl)'),
    ("B2 : adresse finale non contrôlée", OUTIL, '            if r.geturl() != url:\n', '            if False:\n'),
    ("B2 : 3xx non nommé", OUTIL, '        if 300 <= statut < 400:\n            r["anomalies"].append("redirection_refusee")',
     '        if False:\n            r["anomalies"].append("redirection_refusee")'),
    # v3.1 : M1, réponses hors journal
    ("M1 : vérification sans confrontation journal-dossier", OUTIL,
     '    controler_coherence(dossier, env["manifeste"], journal)  # M1', '    pass  # M1'),
    ("M1 : fichiers nommés au journal non vérifiés", OUTIL,
     '    for nom, h in refs.items():\n        if not (Path(dossier) / nom).exists() or verifier_sceau(Path(dossier) / nom) != h:',
     '    for nom, h in refs.items():\n        if False:'),
    ("M1 : fichier étranger non détecté", OUTIL, '            if (Path(dossier) / nom).exists() and nom not in refs:\n',
     '            if False:\n'),
    # v3.1 : M2, C6
    ("C6 : chemin du dossier non contrôlé à la préparation", OUTIL,
     '    if sortie.resolve() != (racine.resolve() / DOSSIER_ENVOIS_REL):\n', '    if False:\n'),
    ("C6 : unicité non vérifiée", OUTIL, '    if trouves != voulus:\n', '    if False:\n'),
    ("C6 : racine du dossier non contrôlée", OUTIL, '    if d.parts[-len(parties):] != parties:\n', '    if False:\n'),
    ("C6 : dépense antérieure ignorée à la préparation", OUTIL,
     'disponible = PLAFOND_ABSOLU_USD - depense_anterieure_usd', 'disponible = PLAFOND_ABSOLU_USD'),
    ("C6 : dépense antérieure ignorée à l'envoi", OUTIL, 'plafond > PLAFOND_ABSOLU_USD - anterieure + 1e-9',
     'plafond > PLAFOND_ABSOLU_USD + 1e-9'),
    # v3.1 : M3
    ("M3 : réponse 200 non écrite brute", OUTIL,
     '        if statut == 200 and rep is not None and len(rep) <= TAILLE_MAX_REPONSE:\n', '        if False:\n'),
    ("M3 : réception non consignée", OUTIL, '            ajouter_journal(dossier, j, {"evenement": "recu",',
     '            (lambda *a: None)(dossier, j, {"evenement": "recu",'),
    ("M3 : filet de l'analyse retiré", OUTIL, '        except Exception as ex:  # filet déclaré',
     '        except ZeroDivisionError as ex:  # filet déclaré'),
    ("M3 : détails d'usage non contrôlés", OUTIL,
     '    if (ptd is not None and not isinstance(ptd, dict)) or (ctd is not None and not isinstance(ctd, dict)):\n',
     '    if False:\n'),
    ("M3 : message non contrôlé (envoi)", OUTIL,
     '    msg = c0.get("message") if isinstance(c0.get("message"), dict) else {}\n    texte',
     '    msg = c0.get("message") or {}\n    texte'),
    ("M3 : erreur non contrôlée", OUTIL, '        err = err if isinstance(err, dict) else {}\n', ''),
    # v3.1 : M4
    ("M4 : total sous la somme admis", OUTIL, '    elif total < p + c:\n', '    elif False:\n'),
    ("M4 : plancher d'entrée retiré", OUTIL, '    elif p < plancher_entree:\n', '    elif False:\n'),
    ("M4 : plancher de sortie visible retiré", OUTIL, '    elif c - raison < plancher_visible:\n', '    elif False:\n'),
    ("M4 : plancher de sortie sans le « au moins 1 »", OUTIL,
     'plancher_visible = -(-octets_contenu // PLANCHER_OCTETS_PAR_JETON)',
     'plancher_visible = octets_contenu // PLANCHER_OCTETS_PAR_JETON'),
    ("M4 : plancher à 64 octets par jeton", OUTIL, 'PLANCHER_OCTETS_PAR_JETON = 16 ', 'PLANCHER_OCTETS_PAR_JETON = 64 '),
    # v3.1 : M5, écarts d'envoi bloquants
    ("anomalie d'envoi non bloquante", OUTIL, '"anomalie_d_envoi", "reponse_non_analysee", "palier_servi_different")',
     '"reponse_non_analysee", "palier_servi_different")'),
    ("réponse non analysée non bloquante", OUTIL, '"anomalie_d_envoi", "reponse_non_analysee", "palier_servi_different")',
     '"anomalie_d_envoi", "palier_servi_different")'),
    ("anomalie d'envoi sans les fiches du lot", OUTIL,
     '                           "etiquettes": list(lot)})\n        if not (Path(dossier) / nom).exists():',
     '                           "etiquettes": []})\n        if not (Path(dossier) / nom).exists():'),
    # v3.1 : palier
    ("palier : service_tier non transmis", OUTIL, '    if SERVICE_TIER[palier] is not None:\n        c["service_tier"]',
     '    if False:\n        c["service_tier"]'),
    ("palier : palier servi non vérifié à l'envoi", OUTIL,
     '    if (o.get("service_tier") not in PALIERS_SERVIS_ADMIS[palier]\n', '    if (False\n'),
    ("palier : palier servi non vérifié à la vérification", OUTIL,
     '    if r.get("service_tier") not in PALIERS_SERVIS_ADMIS.get(palier, ()):\n', '    if False:\n'),
    ("palier : flex admet « default »", OUTIL, '"flex": ("flex",)}', '"flex": ("flex", "default")}'),
    ("palier : standard admet « priority »", OUTIL, '"standard": (None, "default", "standard")',
     '"standard": (None, "default", "standard", "priority")'),
    ("prix : sortie flex fausse", OUTIL, '"flex": {"entree": 5.0, "cache": 0.5, "sortie": 25.0}}',
     '"flex": {"entree": 5.0, "cache": 0.5, "sortie": 50.0}}'),
    ("prix : cache standard au prix d'entrée", OUTIL, '"standard": {"entree": 10.0, "cache": 1.0,',
     '"standard": {"entree": 10.0, "cache": 10.0,'),
    ("prix : ligne source non vérifiée", OUTIL, '    if LIGNES_SOURCE_PRIX[palier] not in p.read_text(encoding="utf-8"):\n',
     '    if False:\n'),
    ("prix : empreinte de la pièce des prix non vérifiée", OUTIL,
     '    if h != attendue:\n        raise Refus(f"pièce des prix', '    if False:\n        raise Refus(f"pièce des prix'),
    # v3.1 : revalidation du manifeste à l'envoi (D6, D7, m1)
    ("manifeste : prix non revérifiés à l'envoi", OUTIL, '    if prix != {**PRIX_LUS[palier], "source": SOURCE_PRIX}:\n',
     '    if False:\n'),
    ("manifeste : plafond non revérifié à l'envoi", OUTIL,
     '    if not nombre_fini(plafond) or plafond <= 0 or plafond > PLAFOND_ABSOLU_USD - anterieure + 1e-9:\n',
     '    if False:\n'),
    ("manifeste : nombre d'appels non revérifié", OUTIL,
     '    if type(appels_max) is not int or appels_max > MAX_APPELS or appels_max != len(envois):\n', '    if False:\n'),
    ("manifeste : lecteur non revérifié", OUTIL,
     '    if effort not in EFFORTS or lecteur != lecteur_attendu(effort, palier):\n', '    if effort not in EFFORTS:\n'),
    ("manifeste : octets ou pire cas non revérifiés", OUTIL,
     '        if len(corps) != e.get("octets") or e.get("pire_cas_usd") != round(pire_cas_usd(len(corps), prix), 6):\n',
     '        if False:\n'),
    ("manifeste : clés du corps non revérifiées", OUTIL,
     '        if (not isinstance(c, dict) or set(c) != attendu or c["model"] != MODELE_LECTEUR\n',
     '        if (not isinstance(c, dict) or c["model"] != MODELE_LECTEUR\n'),
    ("manifeste : ordre non revérifié", OUTIL,
     '    if man.get("ordre_d_envoi") != [e.get("envoi") for e in envois if isinstance(e, dict)] or not envois:\n',
     '    if not envois:\n'),
    ("manifeste : palier non revérifié", OUTIL, '    if palier not in PALIERS:\n        raise Refus(f"manifeste',
     '    if False:\n        raise Refus(f"manifeste'),
    ("manifeste non revalidé du tout", OUTIL, '    prix, plafond, appels_max, palier = valider_manifeste(man, dossier)\n',
     '    prix, plafond, appels_max, palier = (man["garde_depense"]["prix_usd_par_million"], '
     'man["garde_depense"]["plafond_usd"], man["garde_depense"]["appels_max"], man["palier"])\n'),
    # v3.1 : bilan et classement
    ("bilan : prêt sans toutes les clôtures", OUTIL, '"pret_pour_verifier": (len(j["clos"]) == attendus and',
     '"pret_pour_verifier": (True and'),
    ("classement : racine non contrôlée", CLASSER, '    if O.racine_du_dossier(dossier_envois) != Path(racine).resolve():\n',
     '    if False:\n'),
    ("vérification en ligne de commande : racine non contrôlée", OUTIL,
     '            if racine_du_dossier(args.envois) != Path(args.racine).resolve():\n', '            if False:\n'),
]


def jouer(dossier: Path, delai=900) -> tuple[bool, str]:
    env = {k: v for k, v in os.environ.items() if k in ("PATH", "LANG", "LC_ALL", "TZ", "HOME")}
    env.update({"LC_MODULES": str(dossier), "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(dossier.parents[3])})
    c = subprocess.run(["unshare", "-n", sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                        "--basetemp", str(dossier.parents[3] / "pytest"), str(ESSAIS)],
                       capture_output=True, text=True, env=env, timeout=delai, cwd=str(ICI.parents[3]))
    lignes = c.stdout.strip().splitlines() or [""]
    echec = next((l for l in lignes if l.startswith("FAILED") or l.startswith("ERROR")), "")
    return c.returncode == 0, lignes[-1] + (" | " + echec[:160] if echec else "")


def un_mutant(tmp: Path, base: Path, k: int, mutant) -> dict:
    nom, fichier, ancien, nouveau = mutant
    d = tmp / f"m{k:03d}" / "docs" / "notes" / "o" / "lecture-classement-v3-1"
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
    with tempfile.TemporaryDirectory(prefix="mut-lc-v3-1-") as tmp:
        tmp = Path(tmp)
        base = tmp / "base" / "docs" / "notes" / "o" / "lecture-classement-v3-1"
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
    res = {"banc": "mutations-lecture-classement-v3-1", "debut_utc": debut,
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
