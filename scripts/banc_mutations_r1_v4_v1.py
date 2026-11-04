"""Banc de mutations de la relance v4 de R1 (processeur, sans réseau ni modèle téléchargé) : chaque mutation est appliquée
à une **copie** du code (dossier temporaire ; l'arbre de travail n'est jamais touché), puis les essais qui la visent
sont lancés ; une mutation « tuée » fait échouer au moins un essai, une mutation « survivante » est rapportée telle
quelle (R4 : aucune n'est retirée après coup). Sortie : une ligne par mutation, puis le compte.

    nice -n 10 python -I -B scripts/banc_mutations_r1_v4_v1.py RACINE_DU_DEPOT DOSSIER_DE_TRAVAIL_VIDE PYTHON [M06,M07]

Quatrième argument facultatif : identifiants des mutations à rejouer seules (séparés par des virgules), cas sain compris.
"""
import shutil
import subprocess
import sys
import time
from pathlib import Path

LOT = "src/controle_ia/runs_nuit/resolution_graine_lot_v2.py"
REJEU = "src/controle_ia/runs_nuit/rejeu_activations_v4.py"
E_LOT = "tests/test_resolution_graine_lot_v2.py"
E_REJEU = "tests/test_rejeu_activations_v4.py"

# (identifiant, fichier, texte exact, remplacement, essais) — chaque texte doit apparaître exactement une fois
MUTATIONS = [
    ("M01 témoin : captures ignorées", LOT, "and not differentes and not en_trop and forme):",
     "and forme):", [E_LOT]),
    ("M02 témoin : forme ignorée", LOT, "and not differentes and not en_trop and forme):",
     "and not differentes and not en_trop):", [E_LOT]),
    ("M03 témoin : accord à 0,99 au lieu de 1", LOT, 'elif (m["accord"] == 1.0 and',
     'elif (m["accord"] >= 0.99 and', [E_LOT]),
    ("M04 voie : non exact → lot fidèle", LOT, "VOIE_SI_NON_EXACT = VOIE_PASSE ", "VOIE_SI_NON_EXACT = VOIE_LOT ",
     [E_LOT]),
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
]


def copier(racine: Path, dest: Path) -> None:
    for d in ("src", "tests", "docs/sources", "donnees"):
        shutil.copytree(racine / d, dest / d, ignore=shutil.ignore_patterns("__pycache__"))
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
    tuees = 0
    choisies = {x.strip() for x in seules.split(",") if x.strip()}
    for k, (nom, fichier, avant, apres, essais) in enumerate(MUTATIONS):
        if choisies and nom.split()[0] not in choisies:
            continue
        d = travail / f"m{k + 1:02d}"
        copier(racine, d)
        p = d / fichier
        s = p.read_text(encoding="utf-8")
        if s.count(avant) != 1:
            print(f"{nom} : texte à muter trouvé {s.count(avant)} fois : banc faux, arrêt")
            return 2
        p.write_text(s.replace(avant, apres), encoding="utf-8")
        t0 = time.time()
        r = subprocess.run([python, "-I", "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", *essais],
                           cwd=d, capture_output=True, text=True)
        derniere = (r.stdout.strip().splitlines() or [""])[-1]
        # tuée : au moins un essai **en échec** (une erreur d'installation n'en est pas une : le cas sain l'a exclue)
        tuee = r.returncode != 0 and " failed" in derniere
        tuees += tuee
        print(f"{nom} : {'tuée' if tuee else 'SURVIVANTE'} ({derniere} ; {time.time() - t0:.0f} s)", flush=True)
        shutil.rmtree(d)
    print(f"bilan : {tuees} tuées sur {len(choisies) if choisies else len(MUTATIONS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:5]))
