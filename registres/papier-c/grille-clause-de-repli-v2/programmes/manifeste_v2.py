"""Manifeste d'un run de la grille de la clause de repli (rapport v2) : configuration et son empreinte, versions,
graines, commit (R9). Reprend config_canonique et versions de src/controle_ia/manifeste.py ; n'emploie pas
creer_manifeste, qui ecrit sous runs/ (interdit a cet agent) et derive les graines du nom des taches : les graines
consignees ici sont celles que les programmes emploient (grille_commun_v2.generateur), avec leur etat de controle.

Usage (depuis la racine du depot, PYTHONPATH=src) :
  python3 -B registres/papier-c/grille-clause-de-repli-v2/programmes/manifeste_v2.py RUN_ID SORTE SORTIE.json
  SORTE : « lot » (cases a jouer, passe 0) ou « mesure » (mesure du temps, passe 9).
"""
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.path.dirname(ICI)
sys.path.insert(0, ICI)
from grille_commun_v2 import RACINE, identifiant_case  # noqa: E402
from controle_ia.manifeste import config_canonique, versions  # noqa: E402


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def graine(programme, m, a, k, T, passe):
    cle = (programme, identifiant_case(m, a, k, T), passe)
    ss = np.random.SeedSequence(RACINE, spawn_key=cle)
    return dict(entropie=RACINE, spawn_key=list(cle), etat_controle=[int(x) for x in ss.generate_state(2)])


def main():
    run_id, sorte, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
    if os.path.exists(sortie):
        raise SystemExit(f"{sortie} existe deja (R12)")
    figees = os.path.join(DOSSIER, "sha256sums-programmes-avant-lancement-v2.txt")
    cases, graines = [], {}
    if sorte == "lot":
        for ty, prog, fich, R, B in (("c", 2, "cases_c_a_jouer_v2.txt", 8000, None),
                                     ("ab", 1, "cases_ab_a_jouer_v2.txt", 1000, 1000)):
            for ligne in open(os.path.join(DOSSIER, "entrees", fich), encoding="utf-8"):
                m, a, k, T = ligne.split()
                nom = f"{ty}_{m}_{a}_k{k}_T{T}_p0"
                cases.append(dict(nom=nom, programme=f"grille_{ty}_v2.py", modele=m, attaque=a, k=int(k), T=int(T),
                                  R=R, B=B, passe=0))
                graines[nom] = graine(prog, m, a, int(k), int(T), 0)
        commande = "bash registres/papier-c/grille-clause-de-repli-v2/programmes/lancer_v2.sh lot"
    elif sorte == "mesure":
        for ty, prog, m, a, k, T, R, B in (("c", 2, "MH", "g20", 5, 30, 400, None),
                                           ("ab", 1, "MH", "g20", 5, 30, 40, 1000),
                                           ("ab", 1, "E40", "g20", 5, 60, 40, 1000)):
            nom = f"{ty}_{m}_{a}_k{k}_T{T}_p9"
            cases.append(dict(nom=nom, programme=f"grille_{ty}_v2.py", modele=m, attaque=a, k=k, T=T, R=R, B=B,
                              passe=9))
            graines[nom] = graine(prog, m, a, k, T, 9)
        commande = "bash registres/papier-c/grille-clause-de-repli-v2/programmes/mesure_temps_v2.sh"
    else:
        raise SystemExit("sorte inconnue")
    config = dict(
        objet="grille de la clause de repli de la stabilite de rang, papier C, rapport v2 ; donnees simulees",
        texte="brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c5.md",
        texte_sha256="0747f357c30335ec7c37192be7b0d827bdcb4c6e3287c27c000c9d9ee2de723d",
        liste_finie_sha256=sha(os.path.join(DOSSIER, "entrees", "liste-finie-cases-grille-v1.md")),
        programmes_figes=os.path.relpath(figees, os.getcwd()), programmes_figes_sha256=sha(figees),
        interpreteur="/usr/local/bin/python3", processus_paralleles=4, sorte=sorte, cases=cases)
    git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout  # noqa: E731
    statut = git("status", "--porcelain", "--untracked-files=all")
    man = dict(run_id=run_id, cree_le=datetime.now(timezone.utc).isoformat(timespec="seconds"),
               commit=git("rev-parse", "HEAD").strip(), branche=git("branch", "--show-current").strip(),
               depot_propre=statut.strip() == "",
               reserves=["arbre de travail non propre : fichiers neufs de cet agent sous "
                         "registres/papier-c/grille-clause-de-repli-v2/ (aucun commit permis a cet agent)"]
               if statut.strip() else [],
               config=config, config_sha256=hashlib.sha256(config_canonique(config)).hexdigest(),
               versions=versions(), graines=graines, commande=commande)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(man, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    print(sortie, sha(sortie))


if __name__ == "__main__":
    main()
