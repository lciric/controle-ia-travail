#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rejoue le programme de vérification v3 sur les 39 sorties factices du vérificateur S.

Les noms des sorties sont lus dans son fichier de résultats de la v1 (premier mot des lignes
qui commencent par « sortie- ») ; chaque sortie est ouverte par son chemin complet, sans
lister aucun dossier. Le fichier rendu ne porte que des noms de fichiers, des codes de sortie,
des verdicts et des codes de fautes, d'écarts et d'observations : aucun texte des sorties.

Usage : python3 -I -B rejouer_sorties_de_s_v3.py DOSSIER_DES_SORTIES RESULTATS_V1 PROGRAMME MOTIFS DOSSIER_RAPPORTS RESULTATS_V3

Développeur du programme de vérification de la sortie des mondes, modèle O.
"""

import json
import subprocess
import sys
from pathlib import Path


def principal(argv):
    if len(argv) != 6:
        print("usage : DOSSIER_DES_SORTIES RESULTATS_V1 PROGRAMME MOTIFS DOSSIER_RAPPORTS RESULTATS_V3", file=sys.stderr)
        return 3
    dossier, resultats_v1, programme, motifs, rapports, sortie = (Path(a) for a in argv)
    if sortie.exists() or rapports.exists():
        print("erreur : sortie existante, on n'écrase jamais", file=sys.stderr)
        return 3
    rapports.mkdir()
    noms = [ligne.split()[0] for ligne in resultats_v1.read_text(encoding="utf-8").splitlines() if ligne.startswith("sortie-")]
    lignes = []
    for nom in noms:
        rapport = rapports / (nom + ".rapport-v3.json")
        r = subprocess.run([sys.executable, "-I", "-B", str(programme), str(dossier / nom), str(rapport), "--motifs", str(motifs)],
                           capture_output=True, text=True, timeout=300)
        if not rapport.exists():
            lignes.append("%-58s exit=%d sans_rapport" % (nom, r.returncode))
            continue
        rap = json.loads(rapport.read_text(encoding="utf-8"))
        fautes = sorted({f["code"] for p in rap["points"].values() for f in p["fautes"]})
        points = "".join(p["verdict"][0] for _, p in sorted(rap["points"].items()))
        ecartes = [(e["monde"], e["raisons"]) for e in rap["ecartes"]]
        obs = sorted({o["code"] for o in rap["observations"]})
        lignes.append("%-58s exit=%d ens=%s pts=%s\n    fautes=%s\n    ecartes=%s obs=%s"
                      % (nom, r.returncode, rap["verdict_d_ensemble"], points, fautes, ecartes, obs))
    with open(sortie, "x", encoding="utf-8") as fh:
        fh.write("\n".join(lignes) + "\n")
    print("%d sorties rejouées" % len(noms))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
