"""Banc de mutations de la relance v4 de R1, version 2 (`banc_mutations_r1_v4_v1.py` non modifié) : module de la réparation
`resolution_graine_lot_v3` et ses essais, garde de chaîne (I1), mesure de l'indépendance (I5), gardes de dépense et
surveillance (I2, I3), et les gardes que la contre-lecture R2 (M6) trouvait sans mutation ; mutations lancées en
parallèle (`TACHES`, défaut 3), chacune dans sa copie. Processeur, sans réseau ni modèle téléchargé : chaque mutation est appliquée
à une **copie** du code (dossier temporaire ; l'arbre de travail n'est jamais touché), puis les essais qui la visent
sont lancés ; une mutation « tuée » fait échouer au moins un essai, une mutation « survivante » est rapportée telle
quelle (R4 : aucune n'est retirée après coup). Sortie : une ligne par mutation, puis le compte.

    nice -n 10 python -I -B scripts/banc_mutations_r1_v4_v2.py RACINE_DU_DEPOT DOSSIER_DE_TRAVAIL_VIDE PYTHON [M06,M07]

Quatrième argument facultatif : identifiants des mutations à rejouer seules (séparés par des virgules), cas sain compris.
"""
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

LOT = "src/controle_ia/runs_nuit/resolution_graine_lot_v3.py"
LOT2 = "src/controle_ia/runs_nuit/resolution_graine_lot_v2.py"
REJEU = "src/controle_ia/runs_nuit/rejeu_activations_v4.py"
CHAINE = "src/controle_ia/runs_nuit/chaine_table_v4_v1.py"
GARDE = "src/controle_ia/runs_nuit/garde_depense_v4_v1.py"
E_LOT = "tests/test_resolution_graine_lot_v3.py"
E_LOT2 = "tests/test_resolution_graine_lot_v2.py"     # essais du chargeur v4 de la v2 (le rejeu v4 revérifie la
#                                                       version de son côté : garde double, une mutation seule y survit)
E_REJEU = "tests/test_rejeu_activations_v4.py"
E_CHAINE = "tests/test_chaine_table_v4_v1.py"
E_GARDE = "tests/test_garde_depense_v4_v1.py"

# (identifiant, fichier, texte exact, remplacement, essais) — chaque texte doit apparaître exactement une fois
MUTATIONS = [
    ("M01 témoin : captures ignorées", LOT, "and not differentes and not en_trop and forme):",
     "and forme):", [E_LOT]),
    ("M02 témoin : forme ignorée", LOT, "and not differentes and not en_trop and forme):",
     "and not differentes and not en_trop):", [E_LOT]),
    ("M03 témoin : accord à 0,99 au lieu de 1", LOT, 'elif (m["accord"] == 1.0 and',
     'elif (m["accord"] >= 0.99 and', [E_LOT]),
    ("M04 voie : non exact → passe forcée (règle de la v2)", LOT, "VOIE_SI_NON_EXACT = VOIE_LOT ",
     "VOIE_SI_NON_EXACT = VOIE_PASSE ", [E_LOT]),
    ("M05 ligne approchée : fin interne gardée", LOT, "notes = [int(remplissage) if x in fins else x for x in notes][:int(jn)]",
     "notes = notes[:int(jn)]", [E_LOT]),
    ("M06 cible en échec : remplissage de P3 (une fin chez Llama 3) au lieu d'un jeton ordinaire", LOT,
     "j = int(fins_defaut[r]) if (c.a_fin and pas == c.n - 1) else int(remplissage)",
     "j = int(fins_defaut[r]) if (c.a_fin and pas == c.n - 1) else int(min(fins))", [E_LOT]),
    ("M07 lot : arrêt dès que les cibles sont finies (forme tronquée)", LOT,
     "            if not any(actives) or pas == max_nouveaux - 1:\n                break\n            masque = torch.cat",
     "            if not any(actives) or pas == max_nouveaux - 1 or (choix and not any(actives[r] for r in choix)):\n"
     "                break\n            masque = torch.cat", [E_LOT]),
    ("M08 lot : contrôle du texte décodé retiré", LOT,
     "if fmt.tok.decode(nv, skip_special_tokens=True) != lignes[b].textes[t]:",
     "if False:", [E_LOT]),
    ("M09 table v4 : revérification par l'empreinte retirée", LOT,
     "            if empreinte_trajectoire(episode_harnais(e, T, rec)) != traj:\n                raise GardeArret(f\"{e} : les identifiants de la réparation",
     "            if False:\n                raise GardeArret(f\"{e} : les identifiants de la réparation", [E_LOT]),
    ("M10 cibles : entrées de la table v3 comprises", LOT,
     "if not c[\"identique_base\"] and e not in dans_v3]", "if not c[\"identique_base\"]]", [E_LOT]),
    ("M11 échantillon d'équivalence non recalculé", LOT, "        if attendues != sorted(actions):",
     "        if False:", [E_LOT]),
    ("M12 rejeu v4 : non retrouvés comptés dans la règle B", REJEU,
     "    non_resolus = [e for e in signales if par_ep[e][\"methode\"] == \"non_resolu\"]",
     "    non_resolus = [e for e in attendus if par_ep[e][\"methode\"] == \"non_resolu\"]", [E_REJEU]),
    ("M13 rejeu v4 : toute empreinte de table admise", REJEU,
     "if sha != TABLE_EN_SESSION and (not isinstance(sha, str) or not EMPREINTE_HEX.fullmatch(sha)):",
     "if not sha:", [E_REJEU]),
    ("M14 rejeu v4 : non conformes hors de la règle A", REJEU,
     "    attendus = list(signales) + list(non_conformes)", "    attendus = list(signales)", [E_REJEU]),
    ("M15 rejeu v4 : empreinte citée ignorée", REJEU,
     "return rv.charger_table_v4(chemin, None if sha_attendue == TABLE_EN_SESSION else sha_attendue)",
     "return rv.charger_table_v4(chemin, None)", [E_REJEU]),
    # ---- v2 du banc : I1 (garde de chaîne)
    ("M16 chaîne : retrouvée rétrogradée admise", CHAINE, "    if ident != retrouvees:", "    if False:", [E_CHAINE]),
    ("M17 chaîne : sceau du résultat non comparé", CHAINE,
     '    if table.get("resultat_reparation_sha256") != sha_r:', "    if False:", [E_CHAINE]),
    ("M18 chaîne : identifiants des entrées non comparés", CHAINE,
     '            if not 0 <= int(a["pas"]) < len(ids) or [int(y) for y in a["p3"]] != ids[int(a["pas"])]:',
     "            if False:", [E_CHAINE]),
    ("M19 chaîne : entrées de la table v3 non comparées", CHAINE, '    if hors != list(table_v3["episodes"]):',
     "    if False:", [E_CHAINE]),
    ("M20 chaîne : entrée sans le sceau du résultat admise", CHAINE,
     '        if (ent.get("resolution_graine") or {}).get("resultat_sha256") != sha_r:', "        if False:", [E_CHAINE]),
    ("M21 réception : recalcul non comparé à l'octet", CHAINE,
     "    if octets_de_table(table) != Path(chemin_table).read_bytes():", "    if False:", [E_CHAINE]),
    ("M22 chaîne : réparation arrêtée admise", CHAINE,
     '    if (racine / "diag" / corps["run_id"] / "arret.json").exists():', "    if False:", [E_CHAINE]),
    # ---- I5 (indépendance des lignes)
    ("M23 I5 : réserve d'indépendance sans condition sur « après »", LOT,
     '                                         and apres["propre"] is False),', "                                         ),",
     [E_LOT]),
    ("M24 I5 : dernier échec au lieu du premier", LOT, "    t_e = pas_echec[0] if pas_echec else None",
     "    t_e = pas_echec[-1] if pas_echec else None", [E_LOT]),
    ("M25 I5 : réserve « exact » même avec une cible en échec", LOT,
     '            "reserve_lecture_exact": bool(not en_echec and tout["propre"] is False)}',
     '            "reserve_lecture_exact": bool(tout["propre"] is False)}', [E_LOT]),
    # ---- arbitrage M7 : la passe forcée seule n'est plus une voie
    ("M26 réparation : voie autre que le lot admise", LOT, "    if voie != VOIE_LOT:                     ",
     "    if False:                     ", [E_LOT]),
    # ---- I2 et I3 (dépense, surveillance)
    ("M27 dépense : destruction à 60 USD au lieu de 57", GARDE, "DESTRUCTION_USD = 57.0", "DESTRUCTION_USD = 60.0",
     [E_GARDE]),
    ("M28 dépense : identifiant non entier admis", GARDE, 'if not re.fullmatch(r"[1-9][0-9]{0,11}", s):',
     'if not s:', [E_GARDE]),
    ("M29 dépense : instance absente du listing détruite quand même", GARDE,
     "    if ident not in {exiger_identifiant(x) for x in instances_listees}:\n        return {\"action\": \"absente\", \"alerte\": False, \"identifiant\": ident, \"commande\": None,\n                \"motif\"",
     "    if False:\n        return {\"action\": \"absente\", \"alerte\": False, \"identifiant\": ident, \"commande\": None,\n                \"motif\"",
     [E_GARDE]),
    ("M30 filtre : champ lecture= gardé", GARDE,
     'CHAMPS_PERMIS = ("etape", "episodes", "lot", "cibles", "lots", "version")',
     'CHAMPS_PERMIS = ("etape", "episodes", "lot", "cibles", "lots", "version", "lecture")', [E_GARDE]),
    ("M31 surveillance : délai non vérifié", GARDE, '            voir("delai", m.group(1), str(att["delai"]))',
     "            pass", [E_GARDE]),
    ("M32 dépense : fin de l'amorce ignorée", GARDE, "    if fin_amorce:\n", "    if False:\n", [E_GARDE]),
    # ---- M6 de la contre-lecture : gardes du module sans mutation dans la v1 du banc
    ("M33 R3 : exécution unique non vérifiée", LOT,
     '        if m.get("commande") == commande and m.get("config_sha256") == sha:', "        if False:", [E_LOT]),
    ("M34 comptes attendus non vérifiés", LOT, "        if config[k] is not None and int(config[k]) != attendu:",
     "        if False:", [E_LOT]),
    ("M35 témoin arrêté admis", LOT, '    if (Path(racine) / "diag" / corps["run_id"] / "arret.json").exists():\n        raise GardeArret(f"témoin',
     '    if False:\n        raise GardeArret(f"témoin', [E_LOT]),
    ("M36 rejeu v4 : entrée en trop admise", REJEU, "    en_trop = sorted(set(par_ep) - set(attendus))",
     "    en_trop = []", [E_REJEU]),
    ("M37 chargeur v4 (v2, celui du rejeu) : version non vérifiée", LOT2,
     '    if t.get("version") != VERSION_TABLE_V4:', "    if False:", [E_REJEU, E_LOT2]),
]


def copier(racine: Path, dest: Path) -> None:
    # v2 : sous `donnees/`, les seules pièces des essais jouets (aucune pièce de P3, aucun score n'est copié) ; sous
    # `docs/sources`, aucun PDF (place disque : trois copies en parallèle ; aucun essai visé ne lit un PDF)
    for d in ("src", "tests", "docs/sources", "donnees/T0.7-faits-repe-v1", "donnees/T0.7-models-under-pressure-v1"):
        shutil.copytree(racine / d, dest / d, ignore=shutil.ignore_patterns("__pycache__", "*.pdf"))
    shutil.copy2(racine / "pyproject.toml", dest / "pyproject.toml")


def main(racine: str, travail: str, python: str, seules: str = "") -> int:
    racine, travail = Path(racine).resolve(), Path(travail).resolve()
    if travail.exists() and any(travail.iterdir()):
        print(f"{travail} non vide : arrêt (R12)")
        return 2
    travail.mkdir(parents=True, exist_ok=True)
    # cas sain du banc (R5) : copie non mutée, tous les essais visés passent ; sinon le banc est faux (environnement de la
    # copie incomplet : une erreur d'installation passerait pour une mutation tuée)
    d = travail / "m00-sain"
    copier(racine, d)
    essais_sains = sorted({e for m in MUTATIONS for e in m[4]})
    r = subprocess.run([python, "-I", "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *essais_sains], cwd=d,
                       capture_output=True, text=True)
    derniere = (r.stdout.strip().splitlines() or [""])[-1]
    print(f"M00 copie non mutée (cas sain) : {derniere}", flush=True)
    if r.returncode != 0 or " error" in derniere or "skipped" in derniere:
        print("banc faux : la copie non mutée ne passe pas tous ses essais ; arrêt")
        return 2
    shutil.rmtree(d)
    choisies = {x.strip() for x in seules.split(",") if x.strip()}
    retenues = [(k, m) for k, m in enumerate(MUTATIONS) if not choisies or m[0].split()[0] in choisies]
    # chaque texte à muter vérifié unique avant toute exécution (banc faux sinon)
    for k, (nom, fichier, avant, apres, essais) in retenues:
        n = (racine / fichier).read_text(encoding="utf-8").count(avant)
        if n != 1:
            print(f"{nom} : texte à muter trouvé {n} fois : banc faux, arrêt")
            return 2

    def jouer(km):
        k, (nom, fichier, avant, apres, essais) = km
        d = travail / f"m{k + 1:02d}"
        copier(racine, d)
        p = d / fichier
        p.write_text(p.read_text(encoding="utf-8").replace(avant, apres), encoding="utf-8")
        t0 = time.time()
        r = subprocess.run([python, "-I", "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", *essais],
                           cwd=d, capture_output=True, text=True)
        derniere = (r.stdout.strip().splitlines() or [""])[-1]
        # tuée : au moins un essai **en échec** (une erreur d'installation n'en est pas une : le cas sain l'a exclue)
        tuee = r.returncode != 0 and " failed" in derniere
        shutil.rmtree(d)
        return nom, tuee, f"{derniere} ; {time.time() - t0:.0f} s"

    tuees = 0
    with ThreadPoolExecutor(max_workers=int(os.environ.get("TACHES", "3"))) as ex:
        for nom, tuee, detail in ex.map(jouer, retenues):
            tuees += tuee
            print(f"{nom} : {'tuée' if tuee else 'SURVIVANTE'} ({detail})", flush=True)
    print(f"bilan : {tuees} tuées sur {len(retenues)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:5]))
