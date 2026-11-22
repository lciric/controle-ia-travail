"""Épreuve de forme de la lecture commune des cinq moniteurs du bras A, version 10 (demande 17 de la relance ; refaite
après la correction 2 de la contre-lecture habilitée de la version 9, 517fecb3…) : une sortie par cas de la table des
cinq cas (A à E), **sur des scores construits à la main**, sans moniteur, sans épisode réel, sans modèle ; plus une
sortie du cas A dont une valeur p haute est arrondie à quatre décimales, pour éprouver le refus de l'analyse. 2 000
permutations, 2 000 tirages, échange par paire, fichier par unité en rangs.

Forme d'une vraie livraison : le fichier par unité porte les cinq moniteurs, l'agrégateur à l'unité de l'épisode ; les
exclusions, les comptes des lectures et la preuve d'ordre sont faits par les fonctions du module (`unites_avec_scores`,
`episodes_agreges`, `comptes_des_lectures`, journal des ouvertures, table des identifiants tirée et engagée). Ce qui est
construit, et déclaré : seize tâches factices, huit épisodes de deux actions par tâche et par condition ; des scores tirés
d'une loi normale décalée aux doses ; le juge ne lit qu'une action sur deux ; les deux moniteurs appris sont lus par la
fonction du module qui lit un moniteur sur des scores, sur les scores du moniteur boîte noire, puis rangés sous leurs noms
(lignes du fichier par unité comprises) ; les états des lectures produites sont construits. Au cas C, 30 permutations
perdues sur 2 000 sont **injectées** (la fonction d'aire est remplacée, dans ce script seulement, pour les 30 premières
permutations de chaque lecture). La sortie arrondie est écrite hors du module (sa garde la refuse) et scellée.

    PYTHONPATH=src python -B scripts/bras_a_v2_habilite_epreuve_de_forme_v10_v1.py <racine> <dossier neuf>
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
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v11 as A
from controle_ia.scellement import sceller

ENTROPIE_EPREUVE = 20261120
N_PERM = N_TIRAGES = 2000
PAIRE = A.PERMUTATION_PAR_PAIRE
TACHES = [f"tache-forme-{i:02d}" for i in range(16)]
PAS = 2


def _actions(garder) -> list[dict]:
    return [{"cle": f"{c}__{t}__e{e}__p{p}", "condition": c, "tache": t, "episode": e, "pas": p}
            for t in TACHES for c in A.ROLES_LUS for e in range(8) for p in range(PAS) if garder(t, c)]


def main(racine: Path, sortie: Path) -> None:
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà : on n'écrase jamais (R12)")
    _, M = A.charger_piece_source(racine)
    graines = manifeste.graines(A.cles_des_graines(), ENTROPIE_EPREUVE)
    plis = A.plis_communs(M, TACHES, graines)
    pli = {k: [t for t in TACHES if plis[t] == k] for k in (0, 1)}
    travail = Path(tempfile.mkdtemp(prefix="epreuve-de-forme-v11-"))
    rng = np.random.default_rng(ENTROPIE_EPREUVE)
    jeux = {
        "A": lambda t, c: True,
        "B": lambda t, c: c == A.HONNETE or t in pli[1],                                     # une classe manque
        "C": lambda t, c: True,                                                              # pertes injectées
        "D": lambda t, c: t in pli[0][:2] + pli[1][:2] and (c == A.HONNETE or t in (pli[0][0], pli[1][0])),
        "E": lambda t, c: t in (pli[0][0], pli[1][0]),
    }
    vraie_aire = A._aire
    rendu = {}
    for cas, garder in jeux.items():
        dossier = travail / cas
        registre = dossier / "registre-factice.md"
        dossier.mkdir()
        registre.write_text("| clé | date | chemin | sha256 |\n|---|---|---|---|\n"
                            f"| {A.CLE_TABLE_B} | 2026-12-01T09:00:00Z | factice | {'b' * 64} |\n"
                            f"| {A.CLE_ISSUE_DE_LA_BASE} | 2026-12-01T10:00:00Z | factice | {'a' * 64} |\n",
                            encoding="utf-8")
        actions = _actions(garder)
        scores_bn = {a["cle"]: float(rng.normal(1.0 if a["condition"] != A.HONNETE else 0.0, 1.0)) for a in actions}
        scores_juge = {a["cle"]: s for i, (a, s) in enumerate(zip(actions, scores_bn.values())) if i % 2 == 0}
        # table des identifiants opaques tirée et engagée ; productions des deux moniteurs à modèle de langue
        contenu = A.tirer_la_table_opaque([a["cle"] for a in actions])
        table = contenu["table"]
        engagement = A.ecrire_la_table_opaque(dossier / "table", contenu)["engagement"]
        opaque = {v: k for k, v in table.items()}
        produites = {}
        for m, scores in ((A.BOITE_NOIRE, scores_bn), (A.JUGE, scores_juge)):
            lectures = [{"cle": k, "score": scores[table[k]], "balise": A.ETATS_BALISE[i % 5],
                         "jointure": A.JOINTURES[i % 3], "masse_faible": i % 11 == 0}
                        for i, k in enumerate(sorted(opaque[c] for c in scores))]
            produites[m] = lectures
            A.ecrire_la_production(dossier / "production", m, lectures, registre, engagement, racine=racine)
        for m in A.MONITEURS:
            prod = None
            if m in A.A_SCORES:
                prod = dossier / "production" / f"manifeste-production-{A.SOURCE_DES_SCORES[m]}.json"
            A.inscrire_ouverture(registre, m, prod)
        unites_bn, exclues_bn = A.unites_avec_scores(actions, scores_bn)
        unites_juge, exclues_juge = A.unites_avec_scores(actions, scores_juge)
        episodes, comptes_agregateur = A.episodes_agreges(actions, scores_bn, "moyenne")
        collecte, lectures = [], {}
        for dose in A.DOSES:
            lectures[dose] = {}
            for m in A.MONITEURS:
                nom_lu, unites = {A.AGREGATEUR: (A.AGREGATEUR, episodes), A.JUGE: (A.JUGE, unites_juge)}.get(
                    m, (A.BOITE_NOIRE, unites_bn))
                if cas == "C":
                    appels = [0]

                    def aire_injectee(M_, scores, pp, y=None, _appels=appels):
                        if y is not None:
                            _appels[0] += 1
                            if _appels[0] <= 30:
                                raise A.NonCalculable("permutation perdue (injectée par l'épreuve)")
                        return vraie_aire(M_, scores, pp, y)

                    A._aire = aire_injectee
                lignes = []
                try:
                    r = A.lire_scores_fixes(nom_lu, M, unites, dose, plis, graines, registre, lignes, PAIRE, N_PERM,
                                            N_TIRAGES)
                finally:
                    A._aire = vraie_aire
                if A.cas_de_la_lecture(r) != cas:
                    raise GardeArret(f"épreuve : lecture de {m} au cas {A.cas_de_la_lecture(r)}, {cas} attendu")
                lectures[dose][m] = {**r, "moniteur": m}
                collecte += [{**x, "moniteur": m} for x in lignes]
        autres = A.autres_statistiques(M, actions, scores_bn, "moyenne", plis, registre)
        par_unite = A.ecrire_les_scores(sortie / f"unites-cas-{cas.lower()}", collecte, registre, "rang")
        s = A.assembler_la_sortie(
            plis, lectures, {m: {n: v for n, (_, v) in A.PROGRAMMES_DE_PRODUCTION.items()} for m in A.PRODUCTEURS},
            PAIRE, N_PERM, N_TIRAGES, autres,
            {A.BOITE_NOIRE: exclues_bn, A.JUGE: exclues_juge, A.AGREGATEUR: comptes_agregateur},
            {**{m: A.exiger_ouverture(registre, m) for m in A.MONITEURS}, "engagement_de_la_table": engagement},
            par_unite, {m: A.comptes_des_lectures(produites[m], table, actions) for m in A.PRODUCTEURS})
        e = A.ecrire_la_sortie(sortie / f"cas-{cas.lower()}", s)
        rendu[cas] = (sortie / f"cas-{cas.lower()}" / A.FICHIER_SORTIE, e["sha256"], s, par_unite)
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
    rendu["artefact"] = (chemin, sceller(chemin), s, rendu["A"][3])
    for cas, (chemin, sha, s, par_unite) in rendu.items():
        formes = {c: sorted({type(v).__name__ for v in s[c].values()}) for c in ("agregateur_somme_sans_etat",
                                                                                 "agregateur_maximum_sans_etat")}
        lignes = [json.loads(l) for l in (sortie / f"unites-cas-{(cas if cas != 'artefact' else 'A').lower()}"
                                          / par_unite["fichier"]).read_text(encoding="utf-8").splitlines()]
        moniteurs = sorted({l["moniteur"] for l in lignes})
        print(f"{cas}\t{chemin.relative_to(racine) if chemin.is_relative_to(racine) else chemin}\t{sha}\t{formes}\t"
              f"{len(lignes)} lignes, {len(moniteurs)} moniteurs, agrégateur sans pas : "
              f"{all(l['pas'] is None for l in lignes if l['moniteur'] == A.AGREGATEUR)}")


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
