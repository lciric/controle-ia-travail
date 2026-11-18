# -*- coding: utf-8 -*-
"""Lecture 09 de la veille sur l'exploration d'idées (v1) — recalcul indépendant.

Relit, en mémoire et sans rien extraire sur disque, l'archive des journaux de
lancements publiée par les auteurs de « Lineage Is Memory » (arXiv 2610.41157)
et recalcule :
  1. les moyennes par cellule de la table 2A (gpt-4.1-mini, sept tâches) ;
  2. l'effet principal de l'héritage du parent (moyenne « parent » moins « graine »
     sur les quatre affichages du premier lot) et deux intervalles par rééchantillonnage :
     strates fixes (lancements dans chaque cellule) et deux niveaux (tâches, puis lancements) ;
  3. la précision « à tout instant » sur le jeu de recherche de la table 5C
     (cinq tâches hors plafond, pas 1, 2, 4 et 7) ;
  4. la note de la graine telle que les journaux la consignent, à comparer
     à la colonne « Seed Score » de la table 1 du document (p. 5).

N'exécute aucun code des auteurs. À lancer avec `python3 -I`.
Usage : python3 -I recalcul_journaux_publies.py CHEMIN/runs.tar.gz

Archive attendue : `results/runs.tar.gz` du dépôt github.com/shangliy/lineage-is-memory
au commit 66141bbe0b7f9f5abbc4714a78cba32b9774c557, 8106831 octets,
SHA-256 131b0f763b06410ec2f1f43520d411c623a8ed7dea641beec9b1244e4e8e0589.
Les graines des rééchantillonnages sont fixées ci-dessous (R9 : un seul flux, graine 20261118).
"""
import collections
import hashlib
import json
import sys
import tarfile

import numpy as np

ATTENDU = "131b0f763b06410ec2f1f43520d411c623a8ed7dea641beec9b1244e4e8e0589"
TACHES7 = ["labels", "dates", "routing", "replies", "scone", "duration", "size"]
TACHES5 = ["labels", "routing", "replies", "duration", "size"]
AFFICHAGES = ["first", "diverse", "minibatch", "cluster"]


def moyenne(valeurs):
    return sum(valeurs) / len(valeurs)


def main(chemin):
    with open(chemin, "rb") as flux:
        empreinte = hashlib.sha256(flux.read()).hexdigest()
    print("empreinte de l'archive :", empreinte, "(attendue)" if empreinte == ATTENDU else "(INATTENDUE)")
    archive = tarfile.open(chemin)

    def charger(nom):
        return json.load(archive.extractfile(nom))

    # --- 1. Table 2A -------------------------------------------------------
    cellules = collections.defaultdict(list)
    lancements = collections.defaultdict(list)
    for tache in ["labels", "dates", "routing", "replies", "scone"]:
        for ligne in charger("paper/gpt41mini/%s/summary.json" % tache):
            cellules[(tache, ligne["key"])].append(ligne["holdout_best"])
            lancements[(tache, ligne["key"])].append(ligne)
    for ligne in charger("paper/gpt41mini/code/summary.json"):
        cellules[(ligne["task"], ligne["key"])].append(ligne["holdout_best"])
        lancements[(ligne["task"], ligne["key"])].append(ligne)
    for tache in ["labels", "dates", "routing", "replies", "scone"]:
        for ligne in charger("paper/gpt41mini_clustergold/%s/summary.json" % tache):
            cellules[(tache, ligne["key"])].append(ligne["holdout_best"])
            lancements[(tache, ligne["key"])].append(ligne)
    for ligne in charger("paper/gpt41mini_clustergold/code/summary.json"):
        cellules[(ligne["task"], ligne["key"])].append(ligne["holdout_best"])
        lancements[(ligne["task"], ligne["key"])].append(ligne)

    cles = sorted({cle for (_, cle) in cellules})
    print("\n1. Précision tenue à l'écart du meilleur candidat, moyennes par cellule (gpt-4.1-mini)")
    print("%-26s" % "cellule" + "".join("%9s" % t for t in TACHES7) + "    moy7  n")
    for cle in cles:
        rang = [moyenne(cellules[(t, cle)]) for t in TACHES7]
        tailles = sorted({len(cellules[(t, cle)]) for t in TACHES7})
        print("%-26s" % cle + "".join("%9.3f" % v for v in rang) + "  %6.3f  %s" % (moyenne(rang), tailles))

    # --- 2. Effet de l'héritage -------------------------------------------
    def effet(table, taches):
        return moyenne([
            moyenne(table[(t, "parent-full-" + a)]) - moyenne(table[(t, "seed-full-" + a)])
            for t in taches for a in AFFICHAGES
        ])

    print("\n2. Effet principal de l'héritage (parent moins graine, quatre affichages du premier lot)")
    print("sept tâches : %+.4f" % effet(cellules, TACHES7))
    for tache in TACHES7:
        print("   %-9s %+.3f" % (tache, effet(cellules, [tache])))

    generateur = np.random.default_rng(np.random.SeedSequence(20261118))
    utiles = {cle: np.array(v) for cle, v in cellules.items() if cle[1].split("-")[-1] in AFFICHAGES}

    def retirer():
        return {cle: list(generateur.choice(v, size=len(v), replace=True)) for cle, v in utiles.items()}

    tirages = sorted(effet(retirer(), TACHES7) for _ in range(4000))
    print("intervalle à 95 %%, strates fixes (lancements seuls) : [%+.3f, %+.3f]" % (tirages[100], tirages[3899]))
    tirages = []
    for _ in range(4000):
        taches = list(generateur.choice(TACHES7, size=len(TACHES7), replace=True))
        tirages.append(effet(retirer(), taches))
    tirages.sort()
    print("intervalle à 95 %%, deux niveaux (tâches puis lancements) : [%+.3f, %+.3f]" % (tirages[100], tirages[3899]))

    # --- 3. Table 5C --------------------------------------------------------
    def a_tout_instant(lancement, pas):
        notes = [candidat["score"] for candidat in lancement["candidates"]]
        return max(notes[: pas + 1])

    print("\n3. Précision à tout instant sur le jeu de recherche, cinq tâches hors plafond")
    print("%-26s" % "cellule" + "".join("%8s" % ("t=%d" % p) for p in [0, 1, 2, 4, 7]))
    for cle in ["seed-full-first", "seed-full-clustergold", "parent-full-first", "parent-full-clustergold"]:
        rang = [
            moyenne([moyenne([a_tout_instant(l, pas) for l in lancements[(t, cle)]]) for t in TACHES5])
            for pas in [0, 1, 2, 4, 7]
        ]
        print("%-26s" % cle + "".join("%8.3f" % v for v in rang))

    # --- 4. Notes de la graine dans les journaux ---------------------------
    print("\n4. Note du premier candidat consigné (son texte est la graine) et champ holdout_seed,")
    print("   comptés sur les 90 lancements par tâche du premier lot (gpt-4.1-mini)")
    for tache in TACHES7:
        recherche = collections.Counter()
        ecart = collections.Counter()
        for (t, cle), liste in lancements.items():
            if t != tache or cle.endswith("clustergold"):
                continue
            for l in liste:
                recherche[round(l["candidates"][0]["score"], 4)] += 1
                ecart[round(l["holdout_seed"], 4)] += 1
        print("   %-9s recherche %s | tenu à l'écart %s" % (tache, dict(recherche), dict(ecart)))

    premier = lancements[("labels", "parent-full-first")][0]["candidates"][0]["text"]
    print("   texte du premier candidat consigné, tâche labels :", repr(premier))


if __name__ == "__main__":
    main(sys.argv[1])
