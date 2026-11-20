"""Passage de mutations v2 du code de lecture du barreau 5 (développeur du code de lecture, 20 novembre 2026) : ce qui est
neuf dans la v2 (amorce de l'instance de lecture, commande de création, destruction, ligne SCORES-B5F, activations gardées,
gardes resserrées des entrées et des adaptateurs existants : A01 à A13, S01 à S12) ; les huit mutations du contre-lecteur
(C1 à C8, rejouées telles quelles après les essais ajoutés) ; chaque correction de la contre-lecture v2 défaite (K01 à
K16). Même méthode que `mutations-code-lecture-v1.py` (corrigée après
son premier passage nul) : copie de travail unique ; témoins sans mutation exigés verts avant tout compte ; « attrapée » si
pytest rend le code 1 ; chaque « avant » paraît une fois exactement dans le fichier d'origine, sinon « introuvable ».

Usage : python -B mutations-code-lecture-v2.py COPIE BASETEMP [IDENTIFIANTS…]  — imprime le bilan en JSON.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[6]
R, AM = "src/controle_ia/barreau5_familles/relecture_v1.py", "scripts/amorce_b5f_lecture_v1.sh"
L, S = "src/controle_ia/barreau5_familles/lecture_v1.py", "src/controle_ia/barreau5_familles/sondes_v1.py"
EA, EE, ELA, ER = ("tests/test_amorce_b5f_lecture_v1.py", "tests/test_amorce_b5f_lecture_entiere_v1.py",
                   "tests/test_lancer_b5f_lecture_v1.py", "tests/test_barreau5_familles_relecture_v1.py")
EL, ES = "tests/test_barreau5_familles_lecture_v1.py", "tests/test_barreau5_familles_sondes_v1.py"
RAPIDE = "not bout_en_bout and not produits_ecrits and not deplacement_moyen"
A_COPIER = ["src", "tests/conftest.py", EA, EE, ELA, ER, "tests/test_barreau5_familles_lecture_v1.py",
            "tests/test_barreau5_familles_sondes_v1.py", AM, "scripts/lancer_b5f_lecture_v1.sh",
            "prereg/T0.6-organismes-config-7b-v1.json", "prereg/T0.6-organismes-config-7b-v1.json.sha256",
            "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md", "pyproject.toml", ".gitignore",
            ".gitattributes", "requirements-gpu.txt", "requirements-cpu.txt", "requirements-donnees.txt",
            ".claude/hooks/garde_calcul.py", "docs/sources/invites-2606.08892-v1"]

MUTATIONS = [
    # --- amorce ---
    ("A01", AM, "entrées : un seul commit non exigé", '[ "$tous" = "$ajoutes" ] && [ -z "$autres" ] ||', "true ||", [EA]),
    ("A02", AM, "entrées : référence à la branche de la formation tolérée",
     "[ -z \"$(git -C \"$1\" for-each-ref --format='%(refname)' | grep 'barreau5-familles-jumelles-v1-formation')\" ] \\",
     "true \\", [EA]),
    ("A03", AM, "entrées : fichier hors du dossier toléré",
     '[ -z "$(cd "$1" && find . -path ./.git -prune -o -type f -print | grep -v "^\\./$DOSSIER_ENTREES/")" ] \\', "true \\",
     [EA]),
    ("A04", AM, "activations admises par la voie ordinaire", '"^donnees/$r/poids/[a-zA-Z0-9-]+-pli[01]\\\\.json(\\\\.sha256)?\\$" \\',
     '"^donnees/$r/poids/[a-zA-Z0-9-]+-pli[01]\\\\.json(\\\\.sha256)?\\$" "^donnees/$r/activations/" \\', [EA]),
    ("A05", AM, "activations en un seul lot", '[ $((taille + o)) -gt "$LOT_OCTETS" ]', "[ $((taille + o)) -gt 999999999999 ]",
     [EA]),
    ("A06", AM, "témoin sans les activations versées", '[ -s "$SORTIES_PROUVEES" ] && [ -f "$ACTIVATIONS_VERSEES" ]; then',
     '[ -s "$SORTIES_PROUVEES" ]; then', [EA]),
    ("A07", AM, "témoin sans la marche menée au bout", 'if [ -f "$MARCHE_FINIE" ] && [ -s "$SORTIES_PROUVEES" ]',
     'if [ -s "$SORTIES_PROUVEES" ]', [EA]),
    ("A08", AM, "preuve sans les activations gardées",
     'for f in $(sorties_fermees; [ -f "$T/activations-gardees.txt" ] && cat "$T/activations-gardees.txt"); do',
     "for f in $(sorties_fermees); do", [EA]),
    ("A09", AM, "minuterie : destruction sans preuve", '    if [ -s "$TEMOIN" ]; then', "    if true; then", [EA]),
    ("A10", AM, "commit des entrées non exigé (plan décisif)",
     "printf '%s' \"$ENTREES_COMMIT\" | LC_ALL=C grep -qxE '[0-9a-f]{40}' ||", "true ||", [EA]),
    ("A11", AM, "texte scellé non comparé", '[ "$PREREG" = "$TEXTE_B5F" ] ||', "true ||", [EA]),
    ("A12", AM, "chemins d'adaptateurs existants hors du dépôt admis",
     'case "/$c/" in */../*|/docs/*|/diag/*|/runs/*|*b5f-formation*)', 'case "/$c/" in /jamais/*)', [EA]),
    ("A13", AM, "entrées non vérifiées dans le déroulé (seul l'essai à blanc entier le voit)",
     '    verifier_entrees "$E" || arret', "    true || arret", [(EE, "deux_commits")]),
    # --- relecture_v1, côté session ---
    ("S01", R, "offre : disque de 150 Go pour toute pièce", '("disk_space", p["disque_go"], ">=")', '("disk_space", 150, ">=")',
     [ELA]),
    ("S02", R, "commande : registre de la marche non lu",
     '    reg = exiger_registre_de_relecture(_montrer(racine, commit, en.REGISTRE_PROPRE).decode("utf-8"), config, maintenant)',
     '    reg = {"commit_lecture": commit, "engagement": None}', [ELA]),
    ("S03", R, "commande : code du commit non comparé", '    exiger_code_du_commit(racine, reg["commit_lecture"], commit)',
     "    pass", [ELA]),
    ("S04", R, "commande : commit des entrées hors de leur branche admis",
     'if r.returncode != 0 or f"origin/{BRANCHE_ENTREES}" not in r.stdout.split():', "if False:", [ELA]),
    ("S05", R, "commande : adaptateur existant absent du commit admis",
     "                          capture_output=True).returncode != 0:", "                          capture_output=True).returncode != 0 and False:",
     [ELA]),
    ("S06", R, "destruction : étiquette non comparée", 'if len(trouvees) != 1 or trouvees[0].get("label") != p["etiquette"]:',
     "if len(trouvees) != 1:", [ELA]),
    ("S07", R, "ligne SCORES-B5F : taille et empreinte non comparées",
     'if len(b) != f["octets"] or hashlib_sha256(b) != f["sha256"]:', "if False:", [ELA]),
    ("S08", R, "ligne SCORES-B5F : commit non versé admis",
     "    if r.returncode != 0 or not r.stdout.strip():\n        raise GardeArret(f\"commit {commit[:12]} sur aucune branche distante",
     "    if False:\n        raise GardeArret(f\"commit {commit[:12]} sur aucune branche distante", [ELA]),
    ("S09", R, "activations gardées : chemin hors de la liste blanche admis",
     'if _SORTIE.fullmatch(str(c)) is None or not str(c).startswith("activations/"):', "if False:", [ELA]),
    ("S10", R, "entrées : métadonnées admises", 'if not isinstance(entete, dict) or "__metadata__" in entete:',
     "if not isinstance(entete, dict):", [(ER, RAPIDE)]),
    ("S11", R, "entrées : noms opaques non contigus admis", 'if sorted(tenus) != [f"X-{k:02d}" for k in range(1, len(tenus) + 1)]:',
     "if False:", [(ER, RAPIDE)]),
    ("S12", R, "adaptateur existant sans empreinte admis",
     'if not isinstance(x.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", x["sha256"]):', "if False:",
     [(ER, RAPIDE)]),
    # --- les huit mutations du contre-lecteur (`mutations-contre-lecture-v1.py`), rejouées après les essais ajoutés ---
    ("C1", L, "probabilité rapportée de « séparé » prise sur la somme des rangs positifs",
     "float(probabilite_au_plus(K, w_moins))", "float(probabilite_au_plus(K, w_plus))", [EL]),
    ("C2", L, "issue E sans que la séparation apprise soit établie",
     'if sep is not None and sep["etablie"] and E3["K"] > 0 and all(', 'if sep is not None and E3["K"] > 0 and all(', [EL]),
    ("C3", L, "issue E sans valeur absolue", 'all(abs(v) < SEUIL_EMPREINTE * sep["delta_app"]',
     'all(v < SEUIL_EMPREINTE * sep["delta_app"]', [EL]),
    ("C4", L, "épreuve à vérité plantée non exigée avant les scores",
     'for a in ("ENGAGEMENT-B5F", "EPREUVE-B5F", "GO-LECTURE-B5F", "CODE-LECTURE-B5F"):',
     'for a in ("ENGAGEMENT-B5F", "GO-LECTURE-B5F", "CODE-LECTURE-B5F"):', [EL]),
    ("C5", L, "table reçue non comparée à OUVERTURE-B5F", '_exiger(en.empreinte_table(table) == reg["ouverture"]["table"],',
     "_exiger(True,", [EL]),
    ("C6", L, "E2b : rapport des poussées inversé", "c = math.sqrt(rj / rs)", "c = math.sqrt(rs / rj)", [EL]),
    ("C7", L, "M1 et M3 : tâches de l'un des membres (réunion)", "communes = set.intersection(*jouees)",
     "communes = set.union(*jouees)", [EL]),
    ("C8", S, "la sonde d'un pli note les actions de l'autre pli",
     "series = noter(appris[(d.nom, k)], d, lecteur, cles, plis[k])",
     "series = noter(appris[(d.nom, k)], d, lecteur, cles, plis[1 - k])", [ES]),
    # --- corrections de la contre-lecture v2 : chaque correction défaite une à une ---
    ("K01", L, "M-1 défait : sondes lues sous « non interprétable »", 'lu = bool(manip["etablie"])', "lu = True", [EL]),
    ("K02", L, "M-2 défait : famille sans sur-saboteur dans M1",
     ' and "sur_saboteur" in fam[f] and m[f][haut]["m"] is not None', ' and m[f][haut]["m"] is not None', [EL]),
    ("K03", L, "M-3 défait : compagnon orphelin admis", '_exiger(vise in listes or vise == "inventaire.json",',
     "_exiger(True,", [EL]),
    ("K04", L, "M-3 défait : compagnon non vérifié", "        verifier(arbre / vise)\n        compagnons += 1",
     "        compagnons += 1", [EL]),
    ("K05", L, "m-1 défait : « au plus » au niveau de l'issue",
     'au_plus = "0,025" if (ep and ep["E3"]["niveau"] == "95") else "0,005"',
     'au_plus = "0,025" if niveau == "95" else "0,005"', [EL]),
    ("K06", L, "m-1 défait : niveau absent de la phrase",
     """        sortie["issue"] = f"{sortie['issue'][:-1]} (au niveau de 95 %)."\n""", "", [EL]),
    ("K07", S, "m-3 défait : l'écart mesuré relevé tel quel",
     """        raise GardeArret(f"contrôle carte-processeur de la sonde {nom}, pli {pli} : écart au-dessus de la tolérance "
                         "(point 9) : arrêt (erreur de chaîne ; l'écart n'est pas écrit)") from None""", "        raise",
     [ES]),
    ("K08", R, "m-5 défait dans « verifier »",
     '    arbre = exiger_arbre_extrait_propre(racine, commit, reg["engagement"], chemins)\n', "    arbre = {}\n", [ELA]),
    ("K09", R, "m-5 défait dans la commande de création",
     '    exiger_arbre_extrait_propre(racine, commit, reg["engagement"], [x["chemin"] for x in existants])\n', "", [ELA]),
    ("K10", R, "m-5 : tout le commit tenu pour extrait", "    import fnmatch\n    for x in motifs:",
     "    import fnmatch\n    return True\n    for x in motifs:", [ELA]),
    ("K11", L, "m-4 défait : motif sans « niveau non atteignable »",
     '        manque = [e if not manip[e]["non_atteignable"] else', "        manque = [e if True else", [EL]),
    ("K12", L, "M-4 : relance ignorée dans la marche à lire", '    suffixe = "-x1" if relance and n in relance else ""',
     '    suffixe = ""', [EL]),
    ("K13", L, "M-4 : ligne d'évaluation d'une autre copie admise",
     '        _exiger(y.get("famille") == copie and y.get("membre") == x["membre"],',
     '        _exiger(y.get("membre") == x["membre"],', [EL]),
    ("K14", L, "M-4 : résultat de la formation « absente » admis",
     '_exiger(r.get("statut") == "formée" and r.get("nom_forme") == copie,', '_exiger(r.get("nom_forme") == copie,', [EL]),
    ("K15", L, "M-4 : fichier non suivi sous src admis", "u.returncode == 0 and not u.stdout.strip(),", "u.returncode == 0,",
     [EL]),
    ("K16", R, "M-4 : marche qui ne descend pas du code admise",
     '    if a.returncode != 0:\n        raise GardeArret("le commit de la marche ne descend pas du commit de CODE-LECTURE-B5F")',
     '    if False:\n        raise GardeArret("le commit de la marche ne descend pas du commit de CODE-LECTURE-B5F")', [ELA]),
]


def copier(copie: Path) -> None:
    if copie.exists():
        raise SystemExit(f"{copie} existe déjà : une seule copie de travail, neuve")
    for rel in A_COPIER:
        s, d = DEPOT / rel, copie / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)


def jouer(copie: Path, base: Path, nom: str, essais) -> dict:
    cibles = []
    for e in essais:
        cibles += [e[0], "-k", e[1]] if isinstance(e, tuple) else [e]
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(copie / "src"), "TMPDIR": "/dev/shm",
           "PYTHONDONTWRITEBYTECODE": "1", "HOME": os.environ.get("HOME", "/root")}
    debut = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", "--basetemp",
                        str(base / nom), *cibles], cwd=str(copie), env=env, capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip() and not x.startswith("PROGRES")]
    echec = [x for x in lignes if x.startswith(("FAILED", "ERROR"))]
    return {"code": r.returncode, "duree_s": round(time.time() - debut, 1), "fin": lignes[-1] if lignes else "",
            "premier_echec": echec[0] if echec else None}


def main(argv: list[str]) -> int:
    copie, base = Path(argv[0]), Path(argv[1])
    choix = set(argv[2:])
    copier(copie)
    base.mkdir(parents=True, exist_ok=False)
    bilan = {"temoins": {}, "mutations": []}
    for nom, essais in {"EA": [EA], "ELA": [ELA], "ER": [(ER, RAPIDE)], "EE": [(EE, "deux_commits")], "EL": [EL],
                        "ES": [ES]}.items():
        bilan["temoins"][nom] = jouer(copie, base, f"temoin-{nom}", essais)
        print(f"témoin {nom} : code {bilan['temoins'][nom]['code']} ({bilan['temoins'][nom]['fin']})", file=sys.stderr,
              flush=True)
    if any(t["code"] != 0 for t in bilan["temoins"].values()):
        print(json.dumps(bilan, ensure_ascii=False, indent=1))
        raise SystemExit("un témoin sans mutation échoue : aucun compte de mutations")
    for mid, fichier, quoi, avant, apres, essais in MUTATIONS:
        if choix and mid not in choix:
            continue
        origine = (DEPOT / fichier).read_text(encoding="utf-8")
        x = {"id": mid, "fichier": fichier, "defaut": quoi}
        if origine.count(avant) != 1:
            x.update({"etat": "introuvable", "occurrences": origine.count(avant)})
            bilan["mutations"].append(x)
            print(f"{mid} introuvable ({x['occurrences']})", file=sys.stderr, flush=True)
            continue
        cible = copie / fichier
        cible.write_text(origine.replace(avant, apres), encoding="utf-8")
        try:
            r = jouer(copie, base, mid, essais)
        finally:
            cible.write_text(origine, encoding="utf-8")
        etat = "attrapée" if r["code"] == 1 else ("MANQUÉE" if r["code"] == 0 else f"erreur de l'outil (code {r['code']})")
        x.update({"etat": etat, **r})
        bilan["mutations"].append(x)
        print(f"{mid} {etat} ({r['duree_s']} s)", file=sys.stderr, flush=True)
    joues = [m for m in bilan["mutations"] if m["etat"] in ("attrapée", "MANQUÉE")]
    bilan["compte"] = {"jouees": len(joues), "attrapees": sum(m["etat"] == "attrapée" for m in joues),
                       "manquees": [m["id"] for m in joues if m["etat"] == "MANQUÉE"],
                       "erreurs_de_l_outil": [m["id"] for m in bilan["mutations"] if m["etat"].startswith("erreur")],
                       "introuvables": [m["id"] for m in bilan["mutations"] if m["etat"] == "introuvable"]}
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
