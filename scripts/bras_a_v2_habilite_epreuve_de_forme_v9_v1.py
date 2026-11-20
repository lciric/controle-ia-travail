"""Épreuve de forme de la lecture commune des cinq moniteurs du bras A, version 9 (demande 17 de la relance) : une
sortie par cas de la table des cinq cas (A à E), **sur des scores construits à la main**, sans moniteur, sans épisode
réel, sans modèle ; plus une sortie du cas A dont une valeur p est volontairement arrondie, pour éprouver le refus de
l'analyse. 2 000 permutations et 2 000 tirages, échange par paire, fichier par unité en rangs.

Construction (aucun interne de moniteur) : seize tâches factices, huit épisodes d'une action par tâche et par
condition ; la lecture d'un moniteur à une dose est faite par la fonction du module qui lit un moniteur sur des scores
(`lire_scores_fixes`), puis rangée sous les cinq noms de moniteurs ; les autres champs de la sortie (agrégateur,
exclusions, comptes) portent des nombres construits ; la sortie est assemblée et écrite par le module
(`assembler_la_sortie`, `ecrire_la_sortie`), donc passée par sa garde de forme. Seul le cas C est forcé : les
permutations perdues y sont **injectées** (30 sur 2 000 : la fonction d'aire est remplacée, dans ce script seulement,
pour les 30 premières permutations), parce qu'un moniteur lu sur des scores ne perd aucune permutation sous l'échange
par paire. La sortie arrondie est écrite hors du module (sa garde la refuse) et scellée.

    PYTHONPATH=src python -B scripts/bras_a_v2_habilite_epreuve_de_forme_v9_v1.py <racine> <dossier neuf>
"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path

import numpy as np

from controle_ia import manifeste
from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v9 as A
from controle_ia.scellement import sceller

ENTROPIE_EPREUVE = 20261120
N_PERM = N_TIRAGES = 2000
PAIRE = A.PERMUTATION_PAR_PAIRE
TACHES = [f"tache-forme-{i:02d}" for i in range(16)]


def _registre(dossier: Path, racine: Path) -> Path:
    r = dossier / "registre-factice.md"
    r.write_text("| clé | date | chemin | sha256 |\n|---|---|---|---|\n"
                 f"| {A.CLE_TABLE_B} | 2026-12-01T09:00:00Z | factice | {'b' * 64} |\n"
                 f"| {A.CLE_ISSUE_DE_LA_BASE} | 2026-12-01T10:00:00Z | factice | {'a' * 64} |\n", encoding="utf-8")
    lecture = {"cle": "0" * 16, "score": 0.5, "balise": A.ETATS_BALISE[0], "jointure": A.JOINTURES[0],
               "masse_faible": False}
    manifestes = {m: A.ecrire_la_production(dossier / "production", m, [lecture], r, "0" * 64, racine=racine)["manifeste"]
                  for m in A.PRODUCTEURS}
    for m in A.MONITEURS:
        A.inscrire_ouverture(r, m, manifestes[A.SOURCE_DES_SCORES[m]] if m in A.A_SCORES else None)
    return r


def _unites(rng, garder) -> list[dict]:
    unites = []
    for t in TACHES:
        for condition in A.ROLES_LUS:
            for e in range(8):
                if garder(t, condition):
                    s = float(rng.normal(1.0 if condition != A.HONNETE else 0.0, 1.0))
                    unites.append({"cle": f"{condition}__{t}__e{e}__p0", "condition": condition, "tache": t,
                                   "episode": e, "pas": 0, "score": s})
    return unites


def main(racine: Path, sortie: Path) -> None:
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà : on n'écrase jamais (R12)")
    _, M = A.charger_piece_source(racine)
    graines = manifeste.graines(A.cles_des_graines(), ENTROPIE_EPREUVE)
    plis = A.plis_communs(M, TACHES, graines)
    pli = {k: [t for t in TACHES if plis[t] == k] for k in (0, 1)}
    travail = Path(tempfile.mkdtemp(prefix="epreuve-de-forme-v9-"))
    registre = _registre(travail, racine)
    rng = np.random.default_rng(ENTROPIE_EPREUVE)
    jeux = {
        "A": _unites(rng, lambda t, c: True),
        "B": _unites(rng, lambda t, c: c == A.HONNETE or t in pli[1]),                       # une classe manque
        "C": _unites(rng, lambda t, c: True),                                                # pertes injectées
        "D": _unites(rng, lambda t, c: t in pli[0][:2] + pli[1][:2] and (c == A.HONNETE or t in (pli[0][0], pli[1][0]))),
        "E": _unites(rng, lambda t, c: t in (pli[0][0], pli[1][0])),
    }
    vraie_aire = A._aire
    rendu = {}
    for cas, unites in jeux.items():
        collecte, lectures = [], {}
        for dose in A.DOSES:
            if cas == "C":
                appels = [0]

                def aire_injectee(M_, scores, pp, y=None):
                    if y is not None:
                        appels[0] += 1
                        if appels[0] <= 30:
                            raise A.NonCalculable("permutation perdue (injectée par l'épreuve)")
                    return vraie_aire(M_, scores, pp, y)

                A._aire = aire_injectee
            try:
                r = A.lire_scores_fixes(A.JUGE, M, unites, dose, plis, graines, registre, collecte, PAIRE, N_PERM,
                                        N_TIRAGES)
            finally:
                A._aire = vraie_aire
            if A.cas_de_la_lecture(r) != cas:
                raise GardeArret(f"épreuve : la lecture construite pour le cas {cas} tombe au cas {A.cas_de_la_lecture(r)}")
            lectures[dose] = {m: {**r, "moniteur": m} for m in A.MONITEURS}
        autres = {s: {d: 0.5 + 0.01 * i for i, d in enumerate(A.DOSES)} for s in A.STATISTIQUES_RAPPORTEES}
        exclues = {A.BOITE_NOIRE: {c: 0 for c in A.ROLES_LUS}, A.JUGE: {c: 0 for c in A.ROLES_LUS},
                   A.AGREGATEUR: {c: {"episodes": 128, "sans_pas_lu": 0, "pas_sautes": 0} for c in A.ROLES_LUS}}
        preuve = {**{m: A.exiger_ouverture(registre, m) for m in A.MONITEURS}, "engagement_de_la_table": "0" * 64}
        unites_dir = sortie / f"unites-cas-{cas.lower()}"
        par_unite = A.ecrire_les_scores(unites_dir, collecte, registre, "rang")
        comptes = {m: {c: {"lectures": 0} for c in A.ROLES_LUS} for m in A.PRODUCTEURS}
        programmes = {m: {n: s for n, (_, s) in A.PROGRAMMES_DE_PRODUCTION.items()} for m in A.PRODUCTEURS}
        s = A.assembler_la_sortie(plis, lectures, programmes, PAIRE, N_PERM, N_TIRAGES, autres, exclues, preuve,
                                  par_unite, comptes)
        e = A.ecrire_la_sortie(sortie / f"cas-{cas.lower()}", s)
        rendu[cas] = (sortie / f"cas-{cas.lower()}" / A.FICHIER_SORTIE, e["sha256"], s)
    # artefact : la sortie du cas A, une valeur p haute arrondie à quatre décimales, écrite hors du module
    s = copy.deepcopy(rendu["A"][2])
    x = s["lectures"]["dose-0.50"][A.JUGE]
    arrondie = round(x["valeur_p_haut"], 4)
    if arrondie == x["valeur_p_haut"]:
        raise GardeArret("épreuve : l'arrondi ne change pas la valeur p choisie")
    x["valeur_p_haut"] = arrondie
    try:
        A.exiger_sortie(s)
    except GardeArret:
        pass
    else:
        raise GardeArret("épreuve : la garde du module accepte la valeur p arrondie")
    chemin = sortie / "artefact-cas-a-valeur-p-arrondie" / A.FICHIER_SORTIE
    chemin.parent.mkdir(parents=True)
    chemin.write_text(json.dumps(s, ensure_ascii=False, indent=1, allow_nan=False) + "\n", encoding="utf-8")
    rendu["artefact"] = (chemin, sceller(chemin), s)
    for cas, (chemin, sha, s) in rendu.items():
        formes = {c: sorted({type(v).__name__ for v in s[c].values()}) for c in ("agregateur_somme_sans_etat",
                                                                                 "agregateur_maximum_sans_etat")}
        print(f"{cas}\t{chemin.relative_to(racine) if chemin.is_relative_to(racine) else chemin}\t{sha}\t{formes}")


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
