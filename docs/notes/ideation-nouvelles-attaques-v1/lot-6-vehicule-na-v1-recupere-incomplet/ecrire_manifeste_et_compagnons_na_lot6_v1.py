"""Véhicule NA-1, lot 6 — écrit le manifeste du paquet, puis les compagnons `.sha256` et la table d'empreintes du dossier.

    python -I -B ecrire_manifeste_et_compagnons_na_lot6_v1.py manifeste ORCHESTRATEUR_A41B7B50 DOSSIER_LOTS
    python -I -B ecrire_manifeste_et_compagnons_na_lot6_v1.py compagnons

`ORCHESTRATEUR_A41B7B50` : le dossier `orchestrator` d'une copie de l'orchestrateur au commit de base (lu seulement) ;
`DOSSIER_LOTS` : le dossier qui porte les dossiers des lots 2 v5, 3 v3, 4 v1 et 5 v1 (lus seulement). Le manifeste de la
v68 est lu dans `pieces-origin-main/v68/`. Rien n'est écrasé (R12), sauf les compagnons, réécrits à chaque passe.
"""

import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
VERSION = "manifeste-paquet-vehicule-na-lot-6-v1"
MANIFESTE = os.path.join(ICI, "manifeste-paquet-vehicule-na-lot-6-v1.json")
TABLE = os.path.join(ICI, "table-empreintes-dossier-na-lot-6-v1.txt")
FICHIERS_DU_PAQUET = (
    "orchestrator/pole/configuration_course_na_v1.py",
    "orchestrator/pole/course_na_v1.py",
    "orchestrator/pole/simulation_na_v1.py",
    "orchestrator/demonstrations/lancer_orchestrateur_na_v1.py",
    "orchestrator/demonstrations/ecrire_configuration_course_essai_na_v1.py",
    "orchestrator/essais/configuration_essai_na_lot6_v1.py",
    "orchestrator/essais/aides_na_lot6_v1.py",
    "orchestrator/essais/test_na_lot6_v1_course.py",
    "orchestrator/essais/test_na_lot6_v1_arrets.py",
    "orchestrator/essais/mutations_na_lot6_v1.py",
)
MANIFESTES_DES_LOTS = (
    "lot-2-vehicule-na-v5/manifeste-paquet-vehicule-na-lot-2-v5.json",
    "lot-3-vehicule-na-v3/manifeste-paquet-vehicule-na-lot-3-v3.json",
    "lot-4-vehicule-na-v1/manifeste-paquet-vehicule-na-lot-4-v1.json",
    "lot-5-vehicule-na-v1/manifeste-paquet-vehicule-na-lot-5-v1.json",
)
MANIFESTE_V68 = os.path.join(ICI, "pieces-origin-main", "v68", "manifeste-paquet-orchestrateur-v68-v1.json")
EXISTANTS_LUS = (
    "pole/__init__.py", "pole/noyau_v54.py", "pole/noyau_v55.py", "pole/noyau_v56.py", "pole/course2_v53.py",
    "pole/course2_v54.py", "pole/course2_v55.py", "pole/course2_v56.py", "pole/budget_v53.py", "pole/budget_v56.py",
    "pole/suivi_roles_v54.py", "pole/juges_croises_v53.py", "pole/memoire_v53.py", "pole/adaptateurs.py",
    "pole/adaptateurs_v56.py", "pole/adaptateur_kimi_v53.py", "pole/configuration_v53.py", "pole/outils.py",
    "pole/graines_v53.py", "demonstrations/ideation_v8.py", "essais/aides_v53.py", "essais/aides_v56.py",
    "essais/conftest.py",
)
# Fichiers du dossier hors de la table : la base, la copie de travail, les copies tirées de `origin/main`, les dossiers
# temporaires des essais (aucun n'est un dépôt ; aucun ne contient la liste réelle des motifs).
HORS_TABLE = ("base", "travail", "pieces-origin-main", "tmp-essais", "application")


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def manifeste(orchestrateur, dossier_lots):
    if os.path.exists(MANIFESTE):
        raise SystemExit("manifeste existant : jamais écrasé (R12)")
    deps = []
    for rel in MANIFESTES_DES_LOTS:
        with open(os.path.join(dossier_lots, rel), encoding="utf-8") as f:
            m = json.load(f)
        for e in m["fichiers_du_paquet"]:
            if e["chemin"].startswith("orchestrator/pole/") or e["chemin"].startswith("orchestrator/essais/"):
                deps.append({"chemin": e["chemin"], "sha256": e["sha256"], "lot": m["version"]})
    with open(MANIFESTE_V68, encoding="utf-8") as f:
        m68 = json.load(f)
    for e in m68["fichiers_du_paquet"]:
        deps.append({"chemin": e["chemin"], "sha256": e["sha256"], "lot": m68["version"]})
    objet = {
        "version": VERSION,
        "commit_base_orchestrateur": "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb",
        "fichiers_du_paquet": [{"chemin": c, "chemin_paquet": "paquet/" + c, "sha256": sha(os.path.join(ICI, "paquet", c))}
                               for c in FICHIERS_DU_PAQUET],
        "dependances_lots_2_a_5_et_v68": deps,
        "fichiers_existants_lus": [{"chemin": "orchestrator/" + c, "sha256": sha(os.path.join(orchestrateur, c))}
                                   for c in EXISTANTS_LUS],
        "fichiers_existants_modifies": [],
        "regle": "fichiers neufs seulement (R12) ; aucun fichier existant de l'orchestrateur ni des lots 2 à 5 n'est modifié",
    }
    with open(MANIFESTE, "x", encoding="utf-8") as f:
        json.dump(objet, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(json.dumps({"manifeste": os.path.basename(MANIFESTE), "sha256": sha(MANIFESTE), "fichiers": len(FICHIERS_DU_PAQUET),
                      "dependances": len(deps)}, ensure_ascii=False))


def compagnons():
    lignes = []
    for racine, dossiers, fichiers in os.walk(ICI):
        rel_racine = os.path.relpath(racine, ICI)
        if rel_racine == ".":
            dossiers[:] = sorted(d for d in dossiers if d not in HORS_TABLE)
        else:
            dossiers[:] = sorted(d for d in dossiers if d != "__pycache__")
        for f in sorted(fichiers):
            rel = os.path.normpath(os.path.join(rel_racine, f))
            if f.endswith(".sha256") or rel == os.path.basename(TABLE):
                continue
            chemin = os.path.join(ICI, rel)
            s = sha(chemin)
            with open(chemin + ".sha256", "w", encoding="utf-8") as g:
                g.write(f"{s}  {f}\n")
            lignes.append(f"{s}  {rel}")
    with open(TABLE, "w", encoding="utf-8") as g:
        g.write("\n".join(lignes) + "\n")
    with open(TABLE + ".sha256", "w", encoding="utf-8") as g:
        g.write(f"{sha(TABLE)}  {os.path.basename(TABLE)}\n")
    print(json.dumps({"table": os.path.basename(TABLE), "sha256": sha(TABLE), "fichiers": len(lignes)}, ensure_ascii=False))


if __name__ == "__main__":
    if sys.argv[1:2] == ["manifeste"] and len(sys.argv) == 4:
        manifeste(sys.argv[2], sys.argv[3])
    elif sys.argv[1:] == ["compagnons"]:
        compagnons()
    else:
        raise SystemExit(__doc__)
