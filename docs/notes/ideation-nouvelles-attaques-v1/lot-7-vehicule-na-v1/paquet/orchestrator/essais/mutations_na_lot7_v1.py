"""Mutations du lot 7 (manière de la v68 et des lots 2 à 6) : chaque garde retirée ou faussée, sur une copie
temporaire du paquet, doit faire échouer les essais. Une mutation dont le texte cherché n'est pas présent exactement une
fois est « invalide » (jamais comptée tuée). Témoins : T0 (aucune mutation) doit passer ; T1 (commentaire seul) doit
survivre.

Usage : python mutations_na_lot7_v1.py --paquet <dossier paquet/orchestrator> --journal <fichier .json>
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

P, E, Q, R, C = ("pole/mesures_na_v1.py", "pole/export_na_v1.py", "pole/quarantaine_na_v1.py",
                 "pole/requetes_anteriorite_na_v1.py", "pole/commun_na_lot7_v1.py")

MUTATIONS = [
    ("T0", None, None, None),
    ("T1", P, 'VERSION = "mesures-na-v1"', 'VERSION = "mesures-na-v1"  # témoin inerte'),
    # arrêt n° 15
    ("M15-01", P, 'if os.path.exists(os.path.join(sortie, NOM_TEMOIN_LECTURE)):\n        raise ArretMesureNA15("seconde lecture des mesures")',
     'if False:\n        raise ArretMesureNA15("seconde lecture des mesures")'),
    ("M15-02", P, "        if n != 3:\n            raise ArretMesureNA15", "        if n not in (2, 3):\n            raise ArretMesureNA15"),
    ("M15-03", P, "or nom == NOM_ARRET_NON_NOMME:", "or False:"),
    ("M15-04", P, "    attestation = lire_attestation(chemin_attestation, empreinte_attestation)\n",
     "    attestation = lire_attestation(chemin_attestation, None)\n"),
    ("M15-05", C, '    if not os.path.isfile(chemin + ".sha256"):\n        raise ScelleRefuse',
     '    if False:\n        raise ScelleRefuse'),
    ("M15-06", P, "    _consigner_lecture(sortie, entrees)\n    registres = lire_registres(sortie, n)\n    mesures = calculer(",
     "    registres = lire_registres(sortie, n)\n    mesures = calculer("),
    ("M15-07", P, 'raise ArretMesureNA15("la clôture de la course est absente ou illisible")',
     'cloture = {"generations_completes": 3, "arret": None}'),
    ("M15-08", P, '        raise ArretMesureNA15(f"bilan de course absent ou non scellé ({e})") from None',
     '        bilan = {"arret": cloture.get("arret"), "generations": [0] * cloture["generations_completes"]}'),
    # course arrêtée
    ("CA-01", P, "        if n < 2:\n            L[\"M1\"]", "        if n < 1:\n            L[\"M1\"]"),
    ("CA-02", P, "    registres = lire_registres(sortie, n)\n", "    registres = lire_registres(sortie, n + (etat[\"arret\"] is not None))\n"),
    ("CA-03", P, '        titre = f"course arrêtée par {nom}"', '        titre = "course complète, trois générations"'),
    # registre et tentatives
    ("RG-01", P, "    if set(l) - set(CHAMPS_REGISTRE):\n", "    if False:\n"),
    ("RG-02", P, '    if l.get("type_ligne") not in TYPES_LIGNE:', '    if False:'),
    ("RG-03", P, '        if t is None or t["classe_issue"] != FICHES_RENDUES:', '        if t is None:'),
    ("RG-04", P, '            if cle in index:\n                raise', '            if False:\n                raise'),
    ("RG-05", P, '        if "classe" in l or "identifiant" in l:', '        if False:'),
    ("RG-06", P, '        if l.get("raison_arret") == SANS_REPONSE and l.get("modele_servi") is not None:',
     '        if False:'),
    # valeurs
    ("VA-01", P, 'return (0, 1, 2) if lecture == "scellée" else (0,)', 'return (0, 1, 2)'),
    ("VA-02", P, "                    if fil in registre_servi:", "                    if fil not in FILIATION_AUCUNE:"),
    ("VA-03", P, '        if t0["classe_issue"] != REPLI_SERVI:\n            raise', '        if False:\n            raise'),
    ("VA-04", P, '    if der["rang"] == 2 and der["raison_arret"] == RAISON_REFUS:\n        return ARRET_1',
     '    if der["raison_arret"] == RAISON_REFUS:\n        return der["classe_issue"]'),
    ("VA-05", P, '    servies = [t for t in chaine[1:] if t["raison_arret"] not in (RAISON_REFUS, SANS_REPONSE)]',
     '    servies = [t for t in chaine[1:] if t["raison_arret"] != RAISON_REFUS]'),
    ("VA-06", P, "        if t[\"rang\"] == 0:\n            par_role[t[\"espece\"]] += t[\"cout\"]",
     "        if True:\n            par_role[t[\"espece\"]] += t[\"cout\"]"),
    ("VA-07", P, '    if set(attestation) != set(passees):', '    if not set(attestation) <= set(passees):'),
    ("VA-08", P, '    if len(lues) > BORNE_LECTURE_ANTERIORITE:', '    if len(lues) > 1000:'),
    ("VA-09", P, '        if coffre.get("rendues") != rendues or', '        if'),
    ("VA-10", P, 'and ls.get("lignes_tentative") != len(registre_servi):', 'and False:'),
    ("VA-11", P, '"aucune_case_de_la_famille_tenue_a_l_ecart": all(axes_des_cases[c][0] != famille_tenue for c in servies)}',
     '"aucune_case_de_la_famille_tenue_a_l_ecart": True}'),
    ("VA-12", P, '                k = "autre, à nommer" if ax[0] == AXE_AUTRE else "autres cases"',
     '                k = "autres cases"'),
    ("VA-13", P, '            if t["espece"] not in especes_des_roles:\n                raise',
     '            if False:\n                raise'),
    # M4 sans cumul par clé
    ("CL-01", P, "        if ev == EVENEMENT_CUMUL:\n            continue",
     "        if ev == EVENEMENT_CUMUL:\n            generations.setdefault(\"cumul\", []).append(l)\n            continue"),
    ("CL-02", E, '        m4[g] = {"cout_par_role_usd": d["cout_par_role_usd"],',
     '        m4[g] = {"cout_par_role_usd": dict(d["cout_par_role_usd"], **d["replis"]),'),
    # export (n° 17)
    ("EX-01", E, '        hors = set(v) - set(t)\n        if hors:', '        hors = set(v) - set(t)\n        if False:'),
    ("EX-02", E, '        if type(v) is not str or v not in t[1]:', '        if type(v) is not str:'),
    ("EX-03", E, '                ok = k in permis[0]', '                ok = True'),
    ("EX-04", E, '                ok = k in permis[1]', '                ok = True'),
    ("EX-05", E, '        if type(v) is not int or v < 0:\n            _refus(chemin, "compte attendu")',
     '        if False:\n            _refus(chemin, "compte attendu")'),
    ("EX-06", E, '        if type(v) is not str or not _HEX64.match(v):', '        if type(v) is not str:'),
    ("EX-07", E, 'or v["numerateur"] > v["denominateur"]:', ':'),
    ("EX-08", E, '        if type(v) is not bool:', '        if False:'),
    ("EX-09", E, '    if not all(type(i) is str and re.fullmatch(r"[a-z0-9_-]{1,40}", i) for i in ids | roles):',
     '    if False:'),
    ("EX-10", E, '        "parentes_distinctes": L["M2"]["parentes_distinctes"], "part_vers_la_plus_citee": L["M2"]["part_vers_la_plus_citee"]}',
     '        "parentes_distinctes": L["M2"]["parentes_distinctes"], "part_vers_la_plus_citee": L["M2"]["part_vers_la_plus_citee"], "parentes": L["M2"]["parentes"]}'),
    # quarantaine : branche orpheline
    ("BO-01", Q, "    orpheline = not avec_m and not avec_liees", "    orpheline = not avec_m"),
    ("BO-03", Q, '        if sous_commande not in SOUS_COMMANDES_GIT:', '        if False:'),
    ("BO-04", Q, '    if code == 1 and not sortie.strip():\n        return ()', '    if True:\n        return ()'),
    ("BO-05", Q, "    if not constat.orpheline:\n        raise", "    if False:\n        raise"),
    # quarantaine : journal des lectures
    ("JL-01", Q, "    if role not in lecteurs:\n        journal.ajouter", "    if False:\n        journal.ajouter"),
    ("JL-02", Q, '''    journal.ajouter({"evenement": "ouverture", "role": role, "heure": _heure(horloge), "commit": commit,
                     "empreintes": list(empreintes)})
    return ouvrir()''', '''    r = ouvrir()
    journal.ajouter({"evenement": "ouverture", "role": role, "heure": _heure(horloge), "commit": commit,
                     "empreintes": list(empreintes)})
    return r'''),
    ("JL-03", Q, '                     and l["heure"] <= lc["heure"] for l in ouvertures)', '                     for l in ouvertures)'),
    ("JL-04", Q, '        if lc["role"] not in lecteurs:\n            hors.append(i)\n            continue',
     '        if False:\n            hors.append(i)\n            continue'),
    ("JL-05", Q, "        objet = cm.lire_json_scelle(chemin, empreinte_attendue)", "        objet = cm.lire_json_scelle(chemin)"),
    ("JL-06", Q, '        journal.ajouter({"evenement": "refus", "role": role, "heure": _heure(horloge), "commit": commit,\n'
                 '                         "empreintes": list(empreintes), "cause": "lecteur absent de la liste nominative"})\n',
     ''),
    ("RE-01", Q, "        n = (1 if cm.sha256_octets(o) in cible else 0) + sum(", "        n = 0 + sum("),
    # classe (i)
    ("RQ-01", R, '    if tr is A_REMPLIR:\n        raise ParametreGeleNonRempli', '    if tr is A_REMPLIR:\n        tr = {}\n    if False:\n        raise ParametreGeleNonRempli'),
    ("RQ-02", R, '    if manquantes:\n        raise', '    if False:\n        raise'),
    ("RQ-03", R, '    if parametres.valeur_passe_x is A_REMPLIR:\n        raise', '    if False:\n        raise'),
    ("RQ-04", R, '    if len(parts) != 4 or not all(_chaine(p) for p in parts):', '    if len(parts) < 4:'),
    ("RQ-05", R, '    for v in valeurs:\n        for m in mots:', '    for m in mots:\n        for v in valeurs:'),
    ("RQ-06", R, '    o = cm.lire_json_scelle(chemin, empreinte_attendue)', '    o = cm.lire_json_scelle(chemin)'),
    ("RQ-07", R, '    cases = [chaines_classe_i(l, parametres, LANGUES) for l in lignes_de_case]',
     '    cases = [dict(chaines_classe_i(l, parametres, ("fr",)), en=[]) for l in lignes_de_case]'),
    # commun : ajout seul
    ("AS-01", C, '                or _ligne_canonique(ligne) != brute:', '                :'),
    ("AS-02", C, '    if exiger_sceau and not os.path.exists(compagnon):', '    if False:'),
    ("AS-03", C, '    if os.path.exists(chemin) or os.path.exists(chemin + ".sha256"):\n        raise ScelleRefuse',
     '    if False:\n        raise ScelleRefuse'),
]


def jouer(paquet, mutation, python):
    nom, fichier, avant, apres = mutation
    with tempfile.TemporaryDirectory() as tmp:
        copie = os.path.join(tmp, "orchestrator")
        shutil.copytree(paquet, copie, ignore=shutil.ignore_patterns("__pycache__", "*.sha256", ".pytest_cache"))
        if fichier is not None:
            chemin = os.path.join(copie, fichier)
            with open(chemin, encoding="utf-8") as f:
                texte = f.read()
            if texte.count(avant) != 1:
                return {"mutation": nom, "fichier": fichier, "issue": "invalide", "occurrences": texte.count(avant)}
            with open(chemin, "w", encoding="utf-8") as f:
                f.write(texte.replace(avant, apres))
        p = subprocess.run([python, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "essais"], cwd=copie,
                           capture_output=True, text=True, timeout=600)
        derniere = (p.stdout.strip().splitlines() or [""])[-1]
        return {"mutation": nom, "fichier": fichier, "issue": "survit" if p.returncode == 0 else "tuée",
                "code": p.returncode, "resume": derniere[:200]}


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--paquet", required=True)
    a.add_argument("--journal", required=True)
    o = a.parse_args(argv)
    if os.path.exists(o.journal):
        print("journal existant : jamais écrasé (R12)")
        return 2
    rendu = [jouer(o.paquet, m, sys.executable) for m in MUTATIONS]
    vraies = [r for r in rendu if r["mutation"] not in ("T0", "T1")]
    bilan = {"jouees": len(vraies), "tuees": sum(r["issue"] == "tuée" for r in vraies),
             "survivantes": [r["mutation"] for r in vraies if r["issue"] == "survit"],
             "invalides": [r["mutation"] for r in vraies if r["issue"] == "invalide"],
             "temoin_T0": rendu[0]["issue"], "temoin_T1": rendu[1]["issue"]}
    with open(o.journal, "x", encoding="utf-8") as f:
        json.dump({"bilan": bilan, "mutations": rendu}, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(bilan, ensure_ascii=False))
    ok = bilan["temoin_T0"] == "survit" and bilan["temoin_T1"] == "survit" and not bilan["survivantes"] \
        and not bilan["invalides"]
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
