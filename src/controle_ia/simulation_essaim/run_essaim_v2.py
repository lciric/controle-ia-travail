"""Simulation d'essaim — lanceur v2 : celui de v1 (`run_essaim.py`, inchangé), avec la lecture v2.

    PYTHONPATH=src python -m controle_ia.simulation_essaim.run_essaim_v2 \\
        --prereg prereg/essaim-simulation-v1.md --grille prereg/essaim-grille-v1.json

    Réplication gelée (cellules statistiques contraires) :
        … --replication-de <run_id principal>

Différences avec v1, toutes dans la lecture (contre-lecture 1, C7) : `lecture_v2` (statut de chaque prédiction,
table E en 9 lignes, appui exploratoire, phrase de portée) et un `lecture.md` qui porte la phrase de portée en
tête, une colonne « statut » et une colonne « appui exploratoire ». Calibrage, blocs, gardes, graines, tâches et
critères sont ceux de v1, importés sans modification.

Graine racine (règle écrite au préenregistrement, `run_essaim.entropie_depuis_prereg`) : 128 premiers bits du
sha256 du préenregistrement scellé. Elle est une fonction du texte final : calculable dès que ce texte est figé ;
aucun calcul n'est fait avec elle avant le run décisif.

Run unique : la garde `run_essaim.exiger_run_unique` est partagée (même nom de simulation « essaim-v1 ») : un run
décisif principal, par le lanceur v1 ou v2, pour une empreinte de préenregistrement, bloque tout autre.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, verifier_resultat
from ..prereg import exiger_prereg_scelle
from ..simulation_t03.run_t03 import charger_grille, ecrire_md, exiger_code_cite, exiger_code_importe_sous
from . import blocs as B
from . import lecture_v2 as LEC
from .run_essaim import (EQUIVALENCE_TOLERANCE, SIMULATION, configs_des_blocs, entropie_depuis_prereg,
                         exiger_run_unique, taches)

LANCEUR = "controle_ia.simulation_essaim.run_essaim_v2"


def tableau_md(lecture: dict, programme: list[dict], titre: str) -> str:
    lignes = [f"# {titre}", "", LEC.PHRASE_PORTEE, "",
              "Lecture mécanique des critères gelés (`controle_ia.simulation_essaim.lecture`, statuts et table E par "
              f"`controle_ia.simulation_essaim.lecture_v2`), intervalles exacts de Clopper-Pearson de niveau "
              f"1 − {lecture['gamma']:g}.", "",
              "| prédiction | statut | verdict | cellules | conformes | contraires | à répliquer | à auditer |",
              "|---|---|---|---|---|---|---|---|"]
    for k, x in lecture["predictions"].items():
        lignes.append(f"| {k} | {x.get('statut', LEC.statut(k))} | {x['verdict']} | {x['n_cellules']} | "
                      f"{x['n_conformes']} | {x['n_contraires']} | {len(x.get('a_repliquer', []))} | "
                      f"{len(x.get('a_auditer', []))} |")
    a = lecture["audit_symetrie"]
    lignes += ["", f"Audit de symétrie (R4), bornes {a['bornes']} : formes closes, variance des écarts réduits "
               f"{a['formes_closes']['variance_z']:.3f} sur {a['formes_closes']['n']} ; égalités, "
               f"{a['egalites']['variance_z']:.3f} sur {a['egalites']['n']} ; déclenché : {a['audit_declenche']}.", "",
               "## Énoncés (table E)", "",
               "| énoncé | lecture | exigées | complémentaires | appui exploratoire |", "|---|---|---|---|---|"]
    for ligne in programme:
        lignes.append(f"| {ligne['enonce']} | {ligne['lecture']} | {', '.join(ligne['exiges'])} | "
                      f"{', '.join(ligne['complementaires']) or '—'} | "
                      f"{', '.join(ligne['appui_exploratoire']) or '—'} |")
    return "\n".join(lignes) + "\n"


def executer(racine: str | Path, prereg: str | Path, grille_chemin: str | Path, run_id: str,
             blocs: list[str] | None = None, replication_de: str | None = None, limite_s: float = 6 * 3600,
             verifier_import: bool = True) -> dict:
    """Identique à `run_essaim.executer` sauf la lecture (v2) et son rendu. `blocs` n'est jamais accepté de
    l'extérieur ; `verifier_import=False` n'est permis qu'aux tests sur mini-dépôt."""
    racine, prereg, grille_chemin = Path(racine), Path(prereg), Path(grille_chemin)
    if blocs is not None:
        raise GardeArret("les blocs ne se choisissent pas : run principal complet, réplication déterminée par la lecture")
    if verifier_import:
        exiger_code_importe_sous(racine)
    sha_prereg = exiger_prereg_scelle(prereg)
    grille, sha_grille = charger_grille(racine, grille_chemin, prereg)
    commit_cite = exiger_code_cite(racine, prereg, grille_chemin)
    exiger_run_unique(racine, sha_prereg, replication_de)
    entropie = entropie_depuis_prereg(sha_prereg)
    principale = None
    if replication_de:
        corps = verifier_resultat(racine, racine / "diag" / replication_de / "lecture.json")
        principale = corps["resultat"]["lecture"]
        preds = {k for k, x in principale["predictions"].items() if x["a_repliquer"]}
        blocs = sorted({b for p, bs in LEC.BLOCS_DE.items() if any(k.split(".")[0] == p for k in preds) for b in bs})
        if not blocs:
            raise GardeArret("rien à répliquer dans la lecture principale")
    blocs = blocs or list(B.BLOCS)
    ts = taches(grille)
    commande = f"python -m {LANCEUR} " + " ".join(sys.argv[1:])
    config = {"simulation": SIMULATION, "lanceur": LANCEUR, "lecture": LEC.VERSION, "grille": grille,
              "grille_sha256": sha_grille, "blocs": blocs, "replication_de": replication_de, "commit_cite": commit_cite,
              "regle_graine": "entropie = int(sha256(préenregistrement scellé)[:32], 16)", "entropie": str(entropie)}
    chemin_m, m = creer_manifeste(racine, run_id, config, ts + [x + "/replication" for x in ts], entropie=entropie,
                                  decisif=True, prereg=prereg, commande=commande)
    ctx = B.Contexte(grille, m["graines"], suffixe="/replication" if replication_de else "",
                     facteur_R=int(grille["replication"]["facteur_R"]) if replication_de else 1)
    debut = time.monotonic()
    journal = {}

    def chrono(nom):
        journal[nom] = round(time.monotonic() - debut, 1)
        if journal[nom] > limite_s:
            raise GardeArret(f"durée {journal[nom]} s > limite {limite_s} s (liste d'arrêt)")

    cfgs = configs_des_blocs(grille, blocs)
    calib = {cfg: B.calibrer(ctx, cfg) for cfg in cfgs}
    ecrire_resultat(racine, chemin_m, "calibrage", {"configs": calib})
    chrono("calibrage")
    manques = [x for cfg in cfgs for x in B.garde_p0(calib[cfg], ctx.alpha, ctx.gamma)]
    if manques:
        raise GardeArret("garde de calibrage sous P₀ (liste d'arrêt) : " + " ; ".join(manques))
    eq = {cfg: B.equivalence(ctx, cfg, int(grille["tailles"]["equivalence"])) for cfg in cfgs}
    ecrire_resultat(racine, chemin_m, "equivalence", eq)
    chrono("equivalence")
    ecarts = [(cfg, s, e) for cfg, x in eq.items() for s, e in x["ecart_relatif_max"].items()
              if not e <= EQUIVALENCE_TOLERANCE]
    if ecarts:
        raise GardeArret(f"garde d'équivalence (liste d'arrêt) : {ecarts}")
    resultats = {"calibrage": calib}
    for b in blocs:
        resultats[b] = B.BLOCS[b](ctx)
        ecrire_resultat(racine, chemin_m, f"bloc-{b}", resultats[b])
        chrono(b)
    lec = LEC.lire(resultats, grille)
    sortie = {"lecture": lec, "journal_s": journal, "portee": LEC.PHRASE_PORTEE, "lecture_version": LEC.VERSION}
    if principale is not None:
        finale = LEC.fusionner(principale, lec)
        sortie["lecture_finale"] = finale
        sortie["programme"] = LEC.enonces_du_programme(finale)
    else:
        sortie["programme"] = LEC.enonces_du_programme(lec)
    chemin_l = ecrire_resultat(racine, chemin_m, "lecture", sortie)
    ecrire_md(chemin_l.with_suffix(".md"), tableau_md(sortie.get("lecture_finale", lec), sortie["programme"],
                                                      f"Lecture gelée — simulation d'essaim, run {run_id}"))
    return {"run_id": run_id, "manifeste": str(chemin_m), "lecture": str(chemin_l), "journal_s": journal,
            "entropie": str(entropie)}


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--racine", default=".")
    a.add_argument("--prereg", required=True)
    a.add_argument("--grille", required=True)
    a.add_argument("--run-id", default=None)
    a.add_argument("--replication-de", default=None)
    args = a.parse_args(argv)
    suffixe = "essaim-replication" if args.replication_de else "essaim"
    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + suffixe
    print(json.dumps(executer(args.racine, args.prereg, args.grille, run_id, None, args.replication_de),
                     indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
