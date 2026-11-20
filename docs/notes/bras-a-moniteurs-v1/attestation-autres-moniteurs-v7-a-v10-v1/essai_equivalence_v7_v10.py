"""Essai d'équivalence des calculs des versions 7 et 10 du module des autres moniteurs du bras A (demande 24 a).

Mêmes entrées construites à la main (aucun moniteur réel, aucun épisode réel), mêmes plis, mêmes graines, permutation
« libre par épisode » (la seule de la version 7) : chaque nombre que les deux versions rendent toutes deux doit être
égal au bit près. Trois moniteurs lus : un moniteur lu sur des scores (fonction de la boîte noire, de l'agrégateur et
du juge), le classifieur lexical et le classifieur de surface (réappris à chaque permutation). Deux jeux : un jeu où
tout est calculable (cas A) et un jeu où l'intervalle manque faute de tâches (cas E de la version 10), pour montrer
qu'au cas E la version 10 rend les mêmes aire et valeurs p que la version 7 calcule avant de lever l'arrêt.

    PYTHONPATH=src python -B <ce fichier> <racine du dépôt> <relevé à écrire>
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import numpy as np

from controle_ia import manifeste
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v7 as A7
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v10 as A10

ENTROPIE = 20261120
TACHES = [f"tache-equivalence-{i:02d}" for i in range(16)]
N_PERM, N_TIRAGES = 300, 300
COMMUNS = ("aire", "pli0", "pli1", "valeur_p_bas", "valeur_p_haut", "valeur_p_pour_la_famille", "au_moins_egales",
           "n_permutations", "permutations_degenerees", "borne_haute", "quantile_borne_haute", "tirages",
           "tirages_degeneres", "effectifs")
ACTION = "ACTION: ADD\nTITLE: t {k}\nPROPOSAL: body {mot} {k}\nCONTROLS: c{k}\nCOST: {cout} GPU-hours\nPREDICTION: p{k}"


def _actions(garder, rng) -> list[dict]:
    sortie = []
    for t in TACHES:
        for c in A10.ROLES_LUS:
            if not garder(t, c):
                continue
            for e in range(8):
                for p in range(3):
                    mot = "alpha" if c == A10.HONNETE or rng.random() < 0.6 else "beta"
                    texte = ACTION.format(k=p, mot=mot, cout=int(rng.integers(1, 90)))
                    sortie.append({"cle": f"{c}__{t}__e{e}__p{p}", "condition": c, "tache": t, "episode": e, "pas": p,
                                   "texte": texte, "jetons": len(texte) // 4,
                                   "score": float(rng.normal(0.4 if c != A10.HONNETE else 0.0, 1.0))})
    return sortie


def main(racine: Path, releve: Path) -> None:
    v3, M = A10.charger_piece_source(racine)
    graines = manifeste.graines(A10.cles_des_graines(), ENTROPIE)
    plis = A10.plis_communs(M, TACHES, graines)
    pli = {k: [t for t in TACHES if plis[t] == k] for k in (0, 1)}
    jeux = {"tout calculable": lambda t, c: True,
            "intervalle impossible faute de tâches": lambda t, c: t in (pli[0][0], pli[1][0])}
    lignes = ["| jeu | moniteur | dose | cas (v10) | motif v7 | nombres communs égaux au bit près |", "|---|---|---|---|---|---|"]
    tout = True
    for nom_jeu, garder in jeux.items():
        actions = _actions(garder, np.random.default_rng(ENTROPIE))
        dossier = Path(tempfile.mkdtemp(prefix="equivalence-v7-v10-"))
        registre = dossier / "registre-factice.md"
        registre.write_text(f"| {A10.CLE_ISSUE_DE_LA_BASE} | 2026-12-01T10:00:00Z | factice | {'a' * 64} |\n",
                            encoding="utf-8")
        with open(str(registre) + ".ouvertures.md", "w", encoding="utf-8") as f:
            for m in A10.MONITEURS:
                f.write(f"| {A10.CLE_OUVERTURE} | 2026-12-01T11:00:00Z | {m} |\n")
        for dose in ("dose-0.50", "dose-1.00"):
            lus = {
                "lu sur des scores": (
                    A7.lire_scores_fixes(A7.BOITE_NOIRE, M, actions, dose, plis, graines, registre, [], N_PERM, N_TIRAGES),
                    A10.lire_scores_fixes(A10.BOITE_NOIRE, M, actions, dose, plis, graines, registre, [],
                                          A10.PERMUTATION_LIBRE, N_PERM, N_TIRAGES)),
                "classifieur lexical": (
                    A7.lire_moniteur_appris(A7.Lexical(v3), M, actions, dose, plis, graines, registre, [], N_PERM, N_TIRAGES),
                    A10.lire_moniteur_appris(A10.Lexical(v3), M, actions, dose, plis, graines, registre, [],
                                             A10.PERMUTATION_LIBRE, N_PERM, N_TIRAGES)),
                "classifieur de surface": (
                    A7.lire_moniteur_appris(A7.Surface(v3, M), M, actions, dose, plis, graines, registre, [], N_PERM,
                                            N_TIRAGES),
                    A10.lire_moniteur_appris(A10.Surface(v3, M), M, actions, dose, plis, graines, registre, [],
                                             A10.PERMUTATION_LIBRE, N_PERM, N_TIRAGES)),
            }
            for moniteur, (r7, r10) in lus.items():
                A10.exiger_forme_du_cas(r10)
                cas = A10.cas_de_la_lecture(r10)
                communs = [k for k in COMMUNS if r7[k] is not None and r10[k] is not None]
                egaux = all(r7[k] == r10[k] for k in communs)
                # au cas E, la version 7 lève l'arrêt et ne rend pas l'aire ni les valeurs p : la v10 les rend
                if cas == "E":
                    egaux = egaux and r7["aire"] is None and r10["aire"] is not None
                tout = tout and egaux and r7["motif"] == (r10["motif"] if cas == "A" else r7["motif"])
                lignes.append(f"| {nom_jeu} | {moniteur} | {dose} | {cas} | {r7['motif'] or '—'} | "
                              f"{'oui' if egaux else 'NON'} ({len(communs)} nombres) |")
    lignes += ["", f"Verdict de l'essai : {'aucun nombre commun ne diffère' if tout else 'UNE DIFFÉRENCE'} ; "
               f"{N_PERM} permutations, {N_TIRAGES} tirages, permutation « {A10.PERMUTATION_LIBRE} »."]
    releve.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("\n".join(lignes))


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
