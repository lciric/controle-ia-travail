"""Banc des essais du lot 5 v3 du véhicule NA-1 : monte un banc, y joue les essais, écrit le journal.

`python -B jouer_banc_lot_5_v3.py ORCHESTRATOR_BASE BANC JOURNAL.txt [--doublures DOSSIER]`

- `ORCHESTRATOR_BASE` : une copie du dossier `orchestrator` de l'orchestrateur (lue seulement) ; elle est copiée en
  `BANC/orchestrator` (`BANC` ne doit pas exister : R12).
- Les cinq modules du lot 5 v1 y sont posés depuis le paquet v1, **chacun vérifié contre l'empreinte du manifeste v1**
  (déjà posés : vérifiés à cette empreinte, ou refus).
- `--doublures` : les modules des lots 1 à 3 manquent à la base ; ils sont remplacés par les **doublures d'essai** du
  dossier donné, déclarées comme telles dans leur en-tête. Sans `--doublures`, la base doit déjà les porter (application
  réelle des lots 2 v5 et 3 v3), chaque dépendance du manifeste v1 à son empreinte, sinon refus : c'est le rejeu que la
  vérification doit faire.
- Le paquet v3 (modules et essais) est posé ; une cible déjà présente fait refuser (R12).
Aucun réseau, aucune clé.
"""

import hashlib
import json
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
LOT5_V1 = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/lot-5-vehicule-na-v1"
V1_POLE = ("lecteur_fiches_na_v1.py", "contrat_fiche_na_v1.py", "portier_na_v1.py", "registre_na_v1.py",
           "verifier_registre_servi_na_v1.py")
DOUBLURES = ("identifiants_na_v1.py", "tirage_na_v4.py", "requete_na_v3.py", "journal_na_v3.py")
PAQUET_V3 = ("orchestrator/pole/registre_na_v3.py", "orchestrator/pole/verifier_registre_servi_na_v3.py",
             "orchestrator/pole/portier_na_v3.py", "orchestrator/essais/aides_na_lot5_v3.py",
             "orchestrator/essais/test_na_lot5_v3_registre.py", "orchestrator/essais/mutations_na_lot5_v3.py")
ESSAIS = ("essais/test_na_lot5_v3_registre.py",)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def poser(source, cible):
    if os.path.exists(cible):
        raise SystemExit(f"refus : cible déjà présente ({os.path.basename(cible)}) (R12)")
    shutil.copyfile(source, cible)


def monter(base, banc, doublures):
    if os.path.exists(banc):
        raise SystemExit("refus : banc existant (R12)")
    with open(os.path.join(LOT5_V1, "manifeste-paquet-vehicule-na-lot-5-v1.json"), encoding="utf-8") as f:
        m = json.load(f)
    manif = {e["chemin"]: e for e in m["fichiers_du_paquet"]}
    orch = os.path.join(banc, "orchestrator")
    shutil.copytree(base, orch, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
    if not doublures:  # base réelle : les dépendances du lot 5 v1 à leur empreinte (manifeste v1)
        for e in m["dependances_lot_2_v5_et_lot_3_v3"] + m["fichiers_existants_lus"]:
            cible = os.path.join(banc, e["chemin"])
            if not os.path.isfile(cible) or sha(cible) != e["sha256"]:
                raise SystemExit(f"refus : dépendance absente ou d'une autre empreinte ({e['chemin']})")
    for nom in V1_POLE:
        e = manif["orchestrator/pole/" + nom]
        src, cible = os.path.join(LOT5_V1, e["chemin_paquet"]), os.path.join(orch, "pole", nom)
        if sha(src) != e["sha256"]:
            raise SystemExit(f"refus : module du lot 5 v1 altéré ({nom})")
        if os.path.exists(cible):  # lot 5 v1 déjà posé : à son empreinte, ou refus
            if sha(cible) != e["sha256"]:
                raise SystemExit(f"refus : module du lot 5 v1 posé à une autre empreinte ({nom})")
            continue
        poser(src, cible)
    if doublures:
        for nom in DOUBLURES:
            poser(os.path.join(doublures, nom), os.path.join(orch, "pole", nom))
    for rel in PAQUET_V3:
        poser(os.path.join(ICI, "paquet", rel), os.path.join(banc, rel))
    return orch


def main(argv):
    doublures = None
    if "--doublures" in argv:
        i = argv.index("--doublures")
        doublures = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    base, banc, journal = argv
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    orch = monter(base, banc, doublures)
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-rA", "-p", "no:cacheprovider", *ESSAIS],
                       cwd=orch, env=env, capture_output=True, text=True)
    with open(journal, "x", encoding="utf-8") as f:
        f.write(f"banc : {'doublures d’essai des lots 1 à 3 (déclarées)' if doublures else 'base réelle'}\n")
        f.write(r.stdout)
        f.write(r.stderr)
    lignes = [l for l in r.stdout.splitlines() if l.strip()]
    print(lignes[-1] if lignes else r.stderr[-2000:])
    return r.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
