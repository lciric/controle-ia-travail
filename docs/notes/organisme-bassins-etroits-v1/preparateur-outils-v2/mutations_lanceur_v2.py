#!/usr/bin/env python3
"""Contre-lecture du lanceur `lancer_course_ideation_bassins_etroits_v1.py` — outil de mutations des gardes (version 2, adaptée par le préparateur de l'outil 3 du contre-lecteur, 6fdac21d…), suite des
essais rejouée sur chaque mutant.

Outil du contre-lecteur (Claude Fable 5.2) adapté au lanceur v2 par le préparateur (Claude Opus 5.5), 13 novembre 2026 : mêmes douze mutants (textes de la v2), plus dix sur les gardes neuves. Aucun modèle, aucun réseau. Le dépôt n'est pas touché :
chaque mutant est une copie du lanceur écrite dans le dossier de travail (`<travail>/<nom>/scripts/…`), et la suite des
essais est une copie de `tests/test_lancer_course_ideation_bassins_etroits_v1.py` où trois lignes seulement changent :
`RACINE` (fixée au dépôt réel, pour le registre et les pièces réels), `SCRIPT` (le mutant), et `lc.DEPOT = RACINE` après le
chargement (pour que `Reglages.production()` vise le dépôt réel comme dans la suite d'origine). Le cas « base » (aucune
mutation) doit rendre tous les essais passés : c'est le contrôle de l'outil.

Usage : <python avec pytest> -B mutations_lanceur_v1.py DOSSIER_DE_TRAVAIL_NEUF
Un seul processus d'essais à la fois. Sortie : un objet JSON (par mutant : tué ou survivant, essais en échec).
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
NOM = "lancer_course_ideation_bassins_etroits_v2"
LANCEUR = DEPOT / "scripts" / f"{NOM}.py"
ESSAIS = DEPOT / "tests" / f"test_{NOM}.py"

# (nom, garde visée, texte d'origine — une seule occurrence exigée —, texte muté)
MUTATIONS = [
    ('base', "aucune (contrôle de l'outil)", None, None),
    ('M1-cumul-sans-plafond-suivant', 'garde de cumul : plafond suivant non compté', '    if deja + plafond_suivant > borne + 1e-9:', '    if deja > borne + 1e-9:'),
    ('M2-depense-illisible-comptee-zero', 'manifeste de fin illisible compté 0', '            return PLAFOND_COURSE_USD, "manifeste de fin illisible : plafond entier compté"', '            return 0.0, "manifeste de fin illisible : plafond entier compté"'),
    ('M3-relance-apres-depense', "relance d'une course après dépense", '        if total > SEUIL_SANS_DEPENSE_USD or x["fin"] is None or x["fin"].get("code") is None:', '        if x["fin"] is None or x["fin"].get("code") is None:'),
    ('M4-generation-suivante-sans-bras', 'génération g+1 sans bras de g', '    prec = [x for x in runs if x["generation"] == g - 1 and bras_reussi(x)]', '    prec = [x for x in runs if x["generation"] == g - 1 and course_reussie(x)]'),
    ('M5-argument-non-ferme', 'arguments en plus admis', '    if len(argv) != 1 or argv[0] not in GENERATIONS:', '    if len(argv) < 1 or argv[0] not in GENERATIONS:'),
    ('M6-tentatives-de-course-non-bornees', 'trois tentatives de course', '    if len(parties) >= MAX_TENTATIVES:', '    if len(parties) >= 30:'),
    ('M7-borne-du-cumul-egale-au-go', 'borne 60 cède au plafond du GO', '    borne = min(TOTAL_LIGNE_USD, plafond_go)', '    borne = plafond_go'),
    ('M8-attestation-sans-consigne-du-juge', 'consigne en attente non exigée', '    if JUGE_EXTERNE[0] not in attendues or a["consignes_en_attente_sha256"].get(JUGE_EXTERNE[0]) != attendues[JUGE_EXTERNE[0]]:', '    if False:'),
    ('M9-bras-non-bornes', 'trois bras', '    if len(run["bras"]) >= MAX_TENTATIVES:', '    if len(run["bras"]) >= 30:'),
    ('M10-bras-reussi-sans-manifeste-du-bras', 'manifeste du bras non exigé', '                and _lire_json_si_scelle(run["sortie"] / "manifeste-bras-rapporte.json") is not None)', '                )'),
    ('M11-classement-illisible-transmis', 'classement illisible transmis', '    if not isinstance(classement, dict) or classement.get("lisible_L2_L4") is not True:', '    if not isinstance(classement, dict):'),
    ('M12-plancher-du-controle-court-non-garde', 'plancher du contrôle court', ' or r.controle_bras_usd < g["plancher_controle_court"]:', ':'),
    ('N1-controle-externe-interrompu-zero', 'M1 : dossier de contrôle externe sans tentative', '        if m and (controle / nom).is_dir() and m.group(1) not in scellees:', '        if m and not m.group(2) and (controle / nom).is_dir() and m.group(1) not in scellees:'),
    ('N2-mort-sans-fin-compte-zero', 'M7 : processus mort sans fin propre compté 0', '        return PLAFOND_COURSE_USD, "processus mort sans fin propre, ou en marche : plafond entier compté"', '        return 0.0, "processus mort sans fin propre, ou en marche : plafond entier compté"'),
    ('N3-bras-relance-apres-paiement', 'M3 : bras relancé après paiement', '    if t["rapporte"] or t["payees"] or t["refus_taille"]:', '    if t["rapporte"]:'),
    ('N4-doublons-ignores', 'M4 : doublons des juges ignorés', '        if any((ident, p) in paires for p in prises):', '        if False:'),
    ('N5-en-marche-ignore', 'M7 : processus en marche ignoré', '    if en_marche:', '    if False:'),
    ('N6-confirmation-non-exigee', 'M5 : confirmation non exigée', '    if not lire_scelle(conf).decode("utf-8", errors="replace").strip():', '    if False:'),
    ('N7-relecture-recoupement-non-exigee', 'M8 : relecture du recoupement non exigée', '    a = lire_json_scelle(r.depot / RELECTURE_RECOUPEMENT)', '    a = {"lecteur": "x", "lu_le": "x", "recoupement_sha256": h, "niveau_methode_aucune_recette_aucun_secret": True, "temoin_vrai_absent": True}'),
    ('N8-temoin-vrai-non-garde', 'M9 : témoin vrai présent admis', '    if att["temoin_vrai_absent_des_fiches_validees"] is not True:', '    if False:'),
    ('N9-revocation-mal-formee-ignoree', 'm1 : ligne mal formée ignorée', '            if len(cellules) != 8:\n                raise Refus', '            if False:\n                raise Refus'),
    ('N10-liste-blanche-sans-sceau', 'B1 : compagnon non vérifié', '    lue = lire_json_scelle(chemin)\n    attendue', '    lue = json.loads(chemin.read_text(encoding="utf-8"))\n    attendue'),
]


def main():
    travail = Path(sys.argv[1]).resolve()
    if travail.exists():
        raise SystemExit("le dossier de travail doit être neuf")
    travail.mkdir(parents=True)
    source = LANCEUR.read_text(encoding="utf-8")
    essais = ESSAIS.read_text(encoding="utf-8")
    l_racine = "RACINE = Path(__file__).resolve().parents[1]\n"
    l_script = f'SCRIPT = RACINE / "scripts" / "{NOM}.py"\n'
    l_charge = "_spec.loader.exec_module(lc)\n"
    for l in (l_racine, l_script, l_charge):
        assert essais.count(l) == 1, l
    resultats = []
    for nom, garde, avant, apres in MUTATIONS:
        d = travail / nom
        (d / "scripts").mkdir(parents=True)
        (d / "tests").mkdir()
        mutant = source
        if avant is not None:
            if source.count(avant) != 1:
                raise SystemExit(f"{nom} : {source.count(avant)} occurrence(s) du texte d'origine (une exigée)")
            mutant = source.replace(avant, apres)
        chemin_mutant = d / "scripts" / f"{NOM}.py"
        chemin_mutant.write_text(mutant, encoding="utf-8")
        t = essais.replace(l_racine, f'RACINE = Path("{DEPOT}")\n').replace(
            l_script, f'SCRIPT = Path("{chemin_mutant}")\n').replace(l_charge, l_charge + "lc.DEPOT = RACINE\n")
        chemin_essais = d / "tests" / f"test_{NOM}.py"
        chemin_essais.write_text(t, encoding="utf-8")
        env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(d), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
        p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp", str(d / "pt"),
                            "-rf", "--tb=no", str(chemin_essais)], cwd=str(d), env=env, capture_output=True, text=True,
                           timeout=600)
        bilan = [x for x in p.stdout.splitlines() if re.search(r"\d+ (passed|failed)", x)]
        echecs = sorted(re.sub(r"^FAILED \S+::", "", x).split(" - ")[0] for x in p.stdout.splitlines() if x.startswith("FAILED "))
        resultats.append({"mutant": nom, "garde": garde, "avant": avant, "apres": apres, "code_pytest": p.returncode,
                          "bilan": bilan[-1].strip() if bilan else p.stdout[-300:], "essais_en_echec": echecs,
                          "issue": ("contrôle : tous passés" if avant is None and p.returncode == 0 else
                                    "CONTRÔLE EN ÉCHEC" if avant is None else "tué" if echecs else "SURVIVANT")})
        print(json.dumps(resultats[-1], ensure_ascii=False), file=sys.stderr, flush=True)
    print(json.dumps({"lanceur": str(LANCEUR), "essais": str(ESSAIS), "mutants": resultats,
                      "tues": sum(1 for r in resultats if r["issue"] == "tué"),
                      "survivants": [r["mutant"] for r in resultats if r["issue"] == "SURVIVANT"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
