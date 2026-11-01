"""Lanceur du préenregistrement hors échantillon de la simulation d'essaim — v1.

    PYTHONPATH=src python -m controle_ia.simulation_essaim.run_essaim_hors_echantillon_v1 \\
        --prereg prereg/essaim-hors-echantillon-v1.md --grille prereg/essaim-hors-echantillon-grille-v1.json

    Réplication gelée (cellules statistiques contraires) : … --replication-de <run_id principal>

Gardes de v1 réutilisées sans modification : préenregistrement scellé et conforme, grille scellée et citée, commit
cité identique à HEAD sur src/, tests/ et la grille, code importé sous src/, règle de la graine
(`run_essaim.entropie_depuis_prereg` : 128 premiers bits du sha256 du préenregistrement scellé). Garde de run
unique propre (nom de simulation `essaim-hors-echantillon-v1`, distinct de v1). Toutes les tâches portent le
préfixe de leur famille (S/, Q/, P/, calib/, p0/, equivalence/) ; la graine racine diffère de celle de v1 (autre
texte), donc les flux sont disjoints de tous ceux déjà utilisés.
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
from . import blocs_hors_echantillon_v1 as BH
from . import lecture_hors_echantillon_v1 as LEC
from .loi_p3_v1 import empreinte_fichier
from .run_essaim import EQUIVALENCE_TOLERANCE, entropie_depuis_prereg

SIMULATION = "essaim-hors-echantillon-v1"
LANCEUR = "controle_ia.simulation_essaim.run_essaim_hors_echantillon_v1"
FAMILLES = ("S", "Q", "P")


def taches(grille: dict) -> list[str]:
    t = []
    for cfg in grille["S"]:
        t += [f"calib/{cfg}", f"p0/{cfg}", f"equivalence/{cfg}"] + [f"S/{cfg}/{s['nom']}" for s in grille["S"][cfg]]
    gq = grille["Q"]
    for cfg in gq["configs"]:
        for x in gq["lois"]:
            p = f"Q/{cfg}/{x['nom']}"
            t += [f"{p}/calib", f"{p}/p0"] + [f"{p}/{a}" for a in x["arrangements"]]
    gp = grille["P"]
    for s in gp["sondes"]:
        p = f"P/{s}"
        t += [f"{p}/calib", f"{p}/p0"] + [f"{p}/{a['nom']}" for a in gp["arrangements"]]
        t += [f"{p}/conforme/{l}" for l in range(int(gp["conforme"]["L"]))]
    return t


def exiger_run_unique(racine: Path, sha_prereg: str, replication_de: str | None) -> None:
    for chemin in sorted((racine / "runs").glob("*/manifeste.json")):
        try:
            m = json.loads(chemin.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            raise GardeArret(f"manifeste illisible {chemin} : {e}") from None
        cfg, p = m.get("config") or {}, m.get("preenregistrement") or {}
        if not (m.get("decisif") and cfg.get("simulation") == SIMULATION and p.get("sha256") == sha_prereg):
            continue
        if replication_de is None and cfg.get("replication_de") is None:
            raise GardeArret(f"un run décisif existe déjà pour ce préenregistrement : {m.get('run_id')}")
        if replication_de is not None and cfg.get("replication_de") == replication_de:
            raise GardeArret(f"la réplication de {replication_de} existe déjà : {m.get('run_id')}")


def exiger_donnees_p3(racine: Path, grille: dict) -> str:
    d = grille["P"]["donnees"]
    p = racine / d["chemin"]
    if not p.is_file():
        raise GardeArret(f"données P3 absentes : {p}")
    sha = empreinte_fichier(p)
    if sha != d["sha256"]:
        raise GardeArret(f"données P3 : empreinte {sha} ≠ {d['sha256']} (liste d'arrêt)")
    return sha


def tableau_md(lecture: dict, programme: list[dict], titre: str) -> str:
    l = [f"# {titre}", "", LEC.PHRASE_PORTEE, "",
         f"Lecture mécanique (`{LEC.VERSION}`), intervalles exacts de Clopper-Pearson de niveau 1 − {lecture['gamma']:g}.",
         "", "| prédiction | statut | verdict | cellules | conformes | contraires | à répliquer | à auditer |",
         "|---|---|---|---|---|---|---|---|"]
    for k, x in lecture["predictions"].items():
        l.append(f"| {k} | {x['statut']} | {x['verdict']} | {x['n_cellules']} | {x['n_conformes']} | "
                 f"{x['n_contraires']} | {len(x['a_repliquer'])} | {len(x['a_auditer'])} |")
    a = lecture["audit_symetrie"]
    l += ["", f"Audit de symétrie (R4), bornes {a['bornes']} : formes closes {a['formes_closes']['variance_z']:.3f} sur "
          f"{a['formes_closes']['n']} ; égalités {a['egalites']['variance_z']:.3f} sur {a['egalites']['n']} ; "
          f"déclenché : {a['audit_declenche']}.", "", "## Énoncés", "", "| énoncé | lecture | exigées |", "|---|---|---|"]
    for e in programme:
        l.append(f"| {e['enonce']} | {e['lecture']} | {', '.join(e['exiges'])} |")
    return "\n".join(l) + "\n"


def executer(racine, prereg, grille_chemin, run_id: str, replication_de: str | None = None,
             limite_s: float = 6 * 3600, verifier_import: bool = True) -> dict:
    racine, prereg, grille_chemin = Path(racine), Path(prereg), Path(grille_chemin)
    if verifier_import:
        exiger_code_importe_sous(racine)
    sha_prereg = exiger_prereg_scelle(prereg)
    grille, sha_grille = charger_grille(racine, grille_chemin, prereg)
    commit_cite = exiger_code_cite(racine, prereg, grille_chemin)
    exiger_run_unique(racine, sha_prereg, replication_de)
    sha_p3 = exiger_donnees_p3(racine, grille)
    entropie = entropie_depuis_prereg(sha_prereg)
    principale, familles = None, list(FAMILLES)
    if replication_de:
        corps = verifier_resultat(racine, racine / "diag" / replication_de / "lecture.json")
        principale = corps["resultat"]["lecture"]
        preds = {k.split(".")[0] for k, x in principale["predictions"].items() if x["a_repliquer"]}
        familles = sorted({b for p in preds for b in LEC.BLOCS_DE.get(p, ())})
        if not familles:
            raise GardeArret("rien à répliquer dans la lecture principale")
    ts = taches(grille)
    config = {"simulation": SIMULATION, "lanceur": LANCEUR, "lecture": LEC.VERSION, "grille": grille,
              "grille_sha256": sha_grille, "donnees_p3_sha256": sha_p3, "familles": familles,
              "replication_de": replication_de, "commit_cite": commit_cite,
              "regle_graine": "entropie = int(sha256(préenregistrement scellé)[:32], 16)", "entropie": str(entropie)}
    chemin_m, m = creer_manifeste(racine, run_id, config, ts + [x + "/replication" for x in ts], entropie=entropie,
                                  decisif=True, prereg=prereg, commande=f"python -m {LANCEUR} " + " ".join(sys.argv[1:]))
    ctx = B.Contexte(grille, m["graines"], suffixe="/replication" if replication_de else "",
                     facteur_R=int(grille["replication"]["facteur_R"]) if replication_de else 1)
    debut, journal = time.monotonic(), {}

    def chrono(nom):
        journal[nom] = round(time.monotonic() - debut, 1)
        if journal[nom] > limite_s:
            raise GardeArret(f"durée {journal[nom]} s > limite {limite_s} s (liste d'arrêt)")

    if "S" in familles:
        eq = {cfg: B.equivalence(ctx, cfg, int(grille["tailles"]["equivalence"])) for cfg in grille["S"]}
        ecrire_resultat(racine, chemin_m, "equivalence", eq)
        ecarts = [(c, s, e) for c, x in eq.items() for s, e in x["ecart_relatif_max"].items()
                  if not e <= EQUIVALENCE_TOLERANCE]
        if ecarts:
            raise GardeArret(f"garde d'équivalence (liste d'arrêt) : {ecarts}")
        chrono("equivalence")
    resultats = {}
    for f in familles:
        resultats[f] = BH.bloc_S(ctx) if f == "S" else BH.bloc_Q(ctx) if f == "Q" else BH.bloc_P(ctx, racine)
        ecrire_resultat(racine, chemin_m, f"bloc-{f}", resultats[f])
        chrono(f)
    lec = LEC.lire(resultats, grille)
    sortie = {"lecture": lec, "journal_s": journal, "portee": LEC.PHRASE_PORTEE}
    finale = LEC.fusionner(principale, lec) if principale is not None else lec
    if principale is not None:
        sortie["lecture_finale"] = finale
    sortie["enonces"] = LEC.enonces(finale)
    chemin_l = ecrire_resultat(racine, chemin_m, "lecture", sortie)
    ecrire_md(chemin_l.with_suffix(".md"), tableau_md(finale, sortie["enonces"],
                                                      f"Lecture gelée — essaim hors échantillon, run {run_id}"))
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
    suffixe = "essaim-ho-replication" if args.replication_de else "essaim-ho"
    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + suffixe
    print(json.dumps(executer(args.racine, args.prereg, args.grille, run_id, args.replication_de),
                     indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
