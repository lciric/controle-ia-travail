"""Épreuve par retrait des gardes du lanceur v2 et de la garde neuve de la préparation v3 : chaque retrait, joué seul,
doit faire échouer les essais ciblés. Le fichier est remis à l'identique après chaque retrait ; son empreinte est
vérifiée à la fin. Version 2 du script : les 46 retraits de la v1, trois récrits pour le texte de la v2, plus les
retraits de la contre-lecture (C8, partie 6) et ceux des gardes neuves de C1 à C11 et des deux décisions de la mère.

    python -B epreuve_retraits_lanceur_v2.py <copie de travail> <interpréteur> <relevé>
"""
import hashlib
import subprocess
import sys
from pathlib import Path

COPIE, PY, RELEVE = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
LANCEUR = "src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v2.py"
PREP = "src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py"
T_L = "tests/test_bras_a_v2_habilite_lanceur_discretion_v2.py"
T_P = "tests/test_bras_a_v2_habilite_preparation_des_lectures_v3.py"

R = [
    ("poser : nom final pris", LANCEUR, T_L, 'if final.exists():\n        raise GardeArret(f"{final.name} existe déjà',
     'if False:\n        raise GardeArret(f"{final.name} existe déjà'),
    ("poser : compagnon seul d'un autre fichier", LANCEUR, T_L,
     "if not (src.is_file() and final_c.read_text", "if False and not (src.is_file() and final_c.read_text"),
    ("poser : provisoire non scellé", LANCEUR, T_L, "        _scelle(src)\n        os.rename(src_c, final_c)",
     "        os.rename(src_c, final_c)"),
    ("registre : format de ligne", LANCEUR, T_L,
     'if not (_SHA.fullmatch(sha) and chemin and "|" not in chemin and "\\n" not in chemin):', "if False:"),
    ("registre : clé unique", LANCEUR, T_L, "if unique and lignes_du_registre(registre, cle, absent_permis=creer):", "if False:"),
    ("configuration : clés fermées", LANCEUR, T_L, "if not isinstance(c, dict) or tuple(c) != CLES_CONFIG:",
     "if not isinstance(c, dict):"),
    ("configuration : valeurs nulles", LANCEUR, T_L, "    if nulles:\n", "    if False:\n"),
    ("configuration : version et mode", LANCEUR, T_L,
     'if c["version"] != VERSION or c["mode"] not in MODES or (cli and c["mode"] != "reel"):', "if False:"),
    ("configuration : texte scellé", LANCEUR, T_L, '    _fichier_cite(c["texte_scelle"], "texte scellé")\n', ""),
    ("configuration : ligne d'accord", LANCEUR, T_L, 'if not (isinstance(c["go_de_lazar"], str) and re.fullmatch(',
     'if False and not (isinstance(c["go_de_lazar"], str) and re.fullmatch('),
    ("configuration : commit du registre figé", LANCEUR, T_L, 'and _COMMIT.fullmatch(f["commit"])):', "):"),
    ("configuration : modules fermés", LANCEUR, T_L,
     'if not (isinstance(c["modules"], dict) and set(c["modules"]) == set(MODULES_APPELES.values())',
     'if False and not (isinstance(c["modules"], dict) and set(c["modules"]) == set(MODULES_APPELES.values())'),
    ("configuration : échange par paire", LANCEUR, T_L, 'if c["permutation"] != A.PERMUTATION_PAR_PAIRE:', "if False:"),
    ("configuration : forme rang", LANCEUR, T_L, 'if c["forme_du_fichier_par_unite"] != "rang":', "if False:"),
    ("configuration : statistique", LANCEUR, T_L, 'if c["statistique_agregateur"] not in A.STATISTIQUES_EPISODE:',
     "if False:"),
    ("configuration : entiers", LANCEUR, T_L,
     'if not (isinstance(c[k], int) and not isinstance(c[k], bool) and c[k] >= 1):', "if False:"),
    ("configuration : 2 000 en mode réel", LANCEUR, T_L, 'if c["mode"] == "reel" and (c["n_permutations"]',
     'if False and (c["n_permutations"]'),
    ("configuration : dossiers", LANCEUR, T_L, "if not (isinstance(d, dict) and tuple(d) == DOSSIERS):",
     "if not isinstance(d, dict):"),
    ("configuration : chemin relatif", LANCEUR, T_L,
     'if not (isinstance(x, str) and x and not x.startswith("/") and ".." not in Path(x).parts):', "if False:"),
    ("configuration : chargement", LANCEUR, T_L,
     'if not (isinstance(g, dict) and tuple(g) == CLES_CHARGEMENT and g["dtype"] in ("bfloat16", "float32")',
     'if False and not (isinstance(g, dict) and tuple(g) == CLES_CHARGEMENT and g["dtype"] in ("bfloat16", "float32")'),
    ("configuration : jetons de fin", LANCEUR, T_L,
     "if not (fins_a_relever and fins is None) and not (isinstance(fins, list) and fins and all(",
     "if False and not (isinstance(fins, list) and fins and all("),
    ("dossiers disjoints", LANCEUR, T_L, "if d1 == d2 or d1 in d2.parents or d2 in d1.parents:", "if False:"),
    ("modules : empreinte", LANCEUR, T_L, 'if vue != cfg["modules"][chemin]:', "if False:"),
    ("modules : absent", LANCEUR, T_L, 'if not p.is_file():\n            raise GardeArret(f"module appelé',
     'if False:\n            raise GardeArret(f"module appelé'),
    ("modules : importé ailleurs", LANCEUR, T_L,
     "if Path(module.__file__).resolve() != (racine / MODULES_APPELES[nom]).resolve():", "if False:"),
    ("modules : entrée importée ailleurs", LANCEUR, T_L,
     'Path(entree.__file__).resolve() != (racine / MODULES_APPELES["entree"]).resolve():', "False:"),
    ("extraire : ligne CONFIG déjà là", LANCEUR, T_L, "if lignes_du_registre(registre, CLE_CONFIG_BRAS):", "if False:"),
    ("extraire : sorties déjà là", LANCEUR, T_L, 'if any((d["extraction"] / n).exists() for n in',
     'if False and any((d["extraction"] / n).exists() for n in'),
    ("base : code de sortie", LANCEUR, T_L, "if r.returncode != 0:", "if False:"),
    ("aucune reprise après une ouverture", LANCEUR, T_L, "    if ouverts:\n", "    if False:\n"),
    ("comptes de positions", LANCEUR, T_L, "if not comptes or any(n != attendu for n in comptes.values()):", "if False:"),
    ("table : entropie admise", LANCEUR, T_L, 'if int(contenu["entropie_propre"]) != entropie_de_la_table:', "if False:"),
    ("table : une ligne d'engagement", LANCEUR, T_L,
     'if len(lignes) != 1:\n        raise GardeArret(f"registre : {len(lignes)} lignes',
     'if False:\n        raise GardeArret(f"registre : {len(lignes)} lignes'),
    ("table : ligne d'un autre fichier", LANCEUR, T_L, 'if _relatif(racine, chemin) != lignes[0]["chemin"]:', "if False:"),
    ("préparation : bilan et demandes", LANCEUR, T_L,
     'if json.loads(bil.read_text(encoding="utf-8"))["demandes_sha256"] != _sha(dem):', "if False:"),
    ("production : déjà inscrite", LANCEUR, T_L,
     "if lignes_du_registre(registre_du_bras, CLE_MANIFESTE[moniteur], absent_permis=True):\n        raise",
     "if False:\n        raise"),
    ("production : ordre des identifiants", LANCEUR, T_L,
     'if [s["cle"] for s in sorties] != [d["cle"] for d in morceaux[i]]:\n                    raise GardeArret(f"production',
     'if False:\n                    raise GardeArret(f"production'),
    ("production : morceau d'un autre lot", LANCEUR, T_L,
     'if [x["cle"] for x in lignes] != [d["cle"] for d in morceau]:', "if False:"),
    ("production : garde avant le premier appel", LANCEUR, T_L,
     "        A.exiger_production_permise(registre)              # garde", "        pass  # garde"),
    ("morceaux : fichier inattendu", LANCEUR, T_L, "if not m or int(m[1]) >= n:", "if False:"),
    ("morceaux : compagnon", LANCEUR, T_L, "        _scelle(p)\n        presents[int(m[1])] = p",
     "        presents[int(m[1])] = p"),
    ("discrétion : dossiers peuplés", LANCEUR, T_L,
     "if d[nom].is_dir() and any(p.name != PROVISOIRE for p in d[nom].iterdir()):", "if False:"),
    ("discrétion : extraction et bras", LANCEUR, T_L,
     '    if conf_base["entropie"] != entropie_du_bras or \\\n            conf_base["base_mots_et_cout"]["textes"]["sha256"] != _sha(d["extraction"] / X.FICHIER_TEXTES):',
     "    if False:"),
    ("discrétion : garde de production à l'étape 1", LANCEUR, T_L,
     "    A.exiger_production_permise(registre)\n    exiger_aucune_ouverture(registre)",
     "    exiger_aucune_ouverture(registre)"),
    ("discrétion : appel de la garde d'ouverture", LANCEUR, T_L,
     "    exiger_aucune_ouverture(registre)\n    A.charger_piece_source", "    A.charger_piece_source"),
    # --- C8 : retraits de la contre-lecture, au texte de la v2
    ("tâches : identifiant en double", LANCEUR, T_L, 'if t.get("identifiant") in q:', "if False:"),
    ("tâches : énoncé absent", LANCEUR, T_L, '    if manquantes:\n        raise GardeArret(f"tâches',
     '    if False:\n        raise GardeArret(f"tâches'),
    ("tâches : fichier à l'empreinte de la configuration", LANCEUR, T_L, '    _scelle(p, cfg["taches"]["sha256"])\n', ""),
    ("registre absent", LANCEUR, T_L, '        raise GardeArret(f"registre {registre.name} absent")',
     "        return []"),
    ("fichier scellé : empreinte attendue", LANCEUR, T_L, "if attendu is not None and vue != attendu:", "if False:"),
    ("reprise : table à l'empreinte engagée", LANCEUR, T_L, '    _scelle(chemin, lignes[0]["sha256"])\n', ""),
    ("reprise : demandes et bilan scellés", LANCEUR, T_L, "            _scelle(dem)\n            _scelle(bil)\n", ""),
    ("reprise : manifeste inscrit à son empreinte", LANCEUR, T_L, '            _scelle(chemin, inscrites[0]["sha256"])\n', ""),
    ("discrétion : configuration du bras à son empreinte", LANCEUR, T_L,
     '    _scelle(racine / cfg["configuration_du_bras"]["chemin"], cfg["configuration_du_bras"]["sha256"])\n    entropie_du_bras',
     "    entropie_du_bras"),
    ("discrétion : textes scellés", LANCEUR, T_L, '    _scelle(d["extraction"] / X.FICHIER_TEXTES)\n    ligne_config',
     "    ligne_config"),
    ("production : forme de la ligne produite", LANCEUR, T_L, "    A.exiger_ligne_de_production(x)\n", ""),
    # --- gardes neuves de la v2
    ("C3 : pièce source à l'étape 1", LANCEUR, T_L, "    A.charger_piece_source(racine)          # pièce source",
     "    pass  # pièce source"),
    ("C4 : ligne de configuration de la base", LANCEUR, T_L,
     'if len(ligne_config) != 1 or ligne_config[0]["chemin"] != _relatif(racine, d["extraction"] / X.FICHIER_CONFIG):',
     "if False:"),
    ("C4 : configuration à l'empreinte de la ligne", LANCEUR, T_L,
     '_scelle(d["extraction"] / X.FICHIER_CONFIG, ligne_config[0]["sha256"])', '_scelle(d["extraction"] / X.FICHIER_CONFIG)'),
    ("C7 : énoncé bordé de blancs", LANCEUR, T_L, "    if bordees:\n", "    if False:\n"),
    ("C11 : fichiers vérifiés avant l'import", LANCEUR, T_L,
     "    programmes = verifier_les_fichiers(racine, cfg)                # avant tout import du module d'entrée (C11)\n"
     "    entree = entree if entree is not None else charger_le_module_d_entree()\n",
     "    entree = entree if entree is not None else charger_le_module_d_entree()\n"
     "    programmes = verifier_les_fichiers(racine, cfg)\n"),
    ("C6 : relevé seul admet des jetons de fin nuls", LANCEUR, T_L,
     'if v is None and not (fins_a_relever and k == "fins_moniteur_boite_noire")]', "if v is None]"),
    ("registres : trois fichiers distincts", LANCEUR, T_L,
     '    if len({Path(c[k]).as_posix() for k in ("registre", "registre_du_bras", "registre_des_accords")}) != 3:',
     "    if False:"),
    ("lecture complète : champs fermés", LANCEUR, T_L,
     "if not isinstance(s, dict) or tuple(s) != CHAMPS_LECTURE_COMPLETE:", "if not isinstance(s, dict):"),
    ("lecture complète : identifiants générés", LANCEUR, T_L, 'if not (isinstance(s["ids_generes"], list) and all(',
     'if False and not (isinstance(s["ids_generes"], list) and all('),
    ("lecture complète : nombres finis", LANCEUR, T_L,
     "        if not (s[k] is None or (isinstance(s[k], float) and np.isfinite(s[k]))):", "        if False:"),
    ("reprise : lecture complète d'un autre lot", LANCEUR, T_L,
     'if [s["cle"] for s in sorties] != [d["cle"] for d in morceaux[i]]:\n                    raise GardeArret(f"lecture complète {i}',
     'if False:\n                    raise GardeArret(f"lecture complète {i}'),
    ("reprise : lecture complète scellée", LANCEUR, T_L, "                _scelle(dossier_c / nom_c)\n", ""),
    ("reprise : relevé inscrit à chaque relance", LANCEUR, T_L,
     "        ecrire_le_releve_de_reprise(racine, d, registre_du_bras, demandes, manifeste)", "        pass"),
    ("préparation v3 : bilan à cinq comptes", PREP, T_P,
     "if set(bilan) != set(ROLES_LUS) or any(not isinstance(b, dict) or tuple(b) != CLES_DU_BILAN for b in bilan.values()):",
     "if set(bilan) != set(ROLES_LUS):"),
]


def verifier_les_textes():
    """Chaque texte de retrait apparaît exactement une fois dans son fichier."""
    for nom, fichier, _, ancien, _ in R:
        n = (COPIE / fichier).read_text(encoding="utf-8").count(ancien)
        if n != 1:
            print(f"{n} : {nom}")
    print(f"{len(R)} retraits listés")


def main():
    if len(sys.argv) > 4 and sys.argv[4] == "--verifier":
        verifier_les_textes()
        return
    if len(sys.argv) > 4:                   # rejeu des seuls retraits nommés (seconde passe, après correction d'essais)
        R[:] = [r for r in R if r[0] in sys.argv[4:]]
    lignes = ["| retrait | fichier | essais | mord |", "|---|---|---|---|"]
    origines = {f: (COPIE / f).read_bytes() for f in {r[1] for r in R}}
    empreintes = {f: hashlib.sha256(b).hexdigest() for f, b in origines.items()}
    mordent = 0
    for nom, fichier, essais, ancien, neuf in R:
        texte = origines[fichier].decode("utf-8")
        if texte.count(ancien) != 1:
            lignes.append(f"| {nom} | {Path(fichier).name} | — | texte du retrait introuvable ({texte.count(ancien)}) |")
            continue
        (COPIE / fichier).write_text(texte.replace(ancien, neuf), encoding="utf-8")
        try:
            r = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", essais], cwd=COPIE,
                               env={"PYTHONPATH": "src", "PATH": "/usr/bin:/bin"}, capture_output=True, text=True)
        finally:
            (COPIE / fichier).write_bytes(origines[fichier])
        mord = r.returncode != 0
        mordent += mord
        fin = (r.stdout.strip().splitlines() or ["?"])[-1]
        lignes.append(f"| {nom} | {Path(fichier).name} | {Path(essais).name} | {'oui' if mord else 'NON'} — {fin} |")
    for f, e in empreintes.items():
        assert hashlib.sha256((COPIE / f).read_bytes()).hexdigest() == e, f
    lignes.append("")
    lignes.append(f"{mordent} retraits mordent sur {len(R)} listés ; fichiers remis à l'identique : "
                  + " ; ".join(f"{Path(f).name} {e}" for f, e in sorted(empreintes.items())))
    RELEVE.write_text("\n".join(lignes) + "\n", encoding="utf-8")


main()
