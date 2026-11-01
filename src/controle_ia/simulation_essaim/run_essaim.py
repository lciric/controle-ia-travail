"""Simulation d'essaim — lancement de bout en bout sous préenregistrement scellé (R1, R9).

    PYTHONPATH=src python -m controle_ia.simulation_essaim.run_essaim \\
        --prereg prereg/essaim-simulation-v1.md --grille prereg/essaim-grille-v1.json

    Réplication gelée (cellules statistiques contraires) :
        … --replication-de <run_id principal>

Graine racine (règle écrite au préenregistrement) : entropie = entier formé par les 128 premiers bits du
sha256 du préenregistrement scellé (ses 32 premiers caractères hexadécimaux). Elle n'est connue qu'au
scellement, donc après la contre-lecture ; toute version nouvelle du préenregistrement la change.
Chaque tâche reçoit sa graine par `manifeste.graines` (clé de dérivation : 64 premiers bits de sha256(nom)).

Chaîne : grille scellée et citée par le préenregistrement → commit cité identique sur src/, tests/ et la
grille → run décisif unique pour ce préenregistrement → manifeste décisif → calibrage sous la loi de
référence et gardes → garde d'équivalence → blocs C, M, HE3 → lecture gelée → résultats scellés dans
diag/<run_id>/. Toute garde qui échoue arrête le run (liste d'arrêt).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, verifier_resultat
from ..prereg import exiger_prereg_scelle
from ..simulation_t03.run_t03 import charger_grille, ecrire_md, exiger_code_cite, exiger_code_importe_sous
from . import blocs as B
from . import lecture as LEC

EQUIVALENCE_TOLERANCE = 1e-9
SIMULATION = "essaim-v1"


def tableau_md(lecture: dict, programme: list[dict], titre: str) -> str:
    lignes = [f"# {titre}", "", "Lecture mécanique des critères gelés (`controle_ia.simulation_essaim.lecture`), "
              f"intervalles exacts de Clopper-Pearson de niveau 1 − {lecture['gamma']:g}.", "",
              "| prédiction | verdict | cellules | conformes | contraires | à répliquer | à auditer |",
              "|---|---|---|---|---|---|---|"]
    for k, x in lecture["predictions"].items():
        lignes.append(f"| {k} | {x['verdict']} | {x['n_cellules']} | {x['n_conformes']} | {x['n_contraires']} | "
                      f"{len(x.get('a_repliquer', []))} | {len(x.get('a_auditer', []))} |")
    a = lecture["audit_symetrie"]
    lignes += ["", f"Audit de symétrie (R4), bornes {a['bornes']} : formes closes, variance des écarts réduits "
               f"{a['formes_closes']['variance_z']:.3f} sur {a['formes_closes']['n']} ; égalités, "
               f"{a['egalites']['variance_z']:.3f} sur {a['egalites']['n']} ; déclenché : {a['audit_declenche']}.", "",
               "## Énoncés (table E)", "", "| énoncé | lecture | exigées | complémentaires |", "|---|---|---|---|"]
    for ligne in programme:
        lignes.append(f"| {ligne['enonce']} | {ligne['lecture']} | {', '.join(ligne['exiges'])} | "
                      f"{', '.join(ligne['complementaires']) or '—'} |")
    return "\n".join(lignes) + "\n"


def entropie_depuis_prereg(sha256_prereg: str) -> int:
    """Règle de la graine racine : 128 premiers bits de l'empreinte du préenregistrement scellé."""
    if not re.fullmatch(r"[0-9a-f]{64}", sha256_prereg or ""):
        raise GardeArret(f"empreinte de préenregistrement {sha256_prereg!r} : 64 caractères hexadécimaux attendus")
    return int(sha256_prereg[:32], 16)


def taches(grille: dict) -> list[str]:
    """Toutes les tâches à graine du run, dans l'ordre de leur usage par les blocs."""
    t = []
    for cfg in grille["configs"]:
        t += [f"calib/{cfg}", f"p0/{cfg}", f"equivalence/{cfg}"]
    for cfg, specs in grille["C"].items():
        t += [f"C/{cfg}/{s['nom']}" for s in specs]
    for cfg, specs in grille["M"].items():
        t += [f"M/{cfg}/{s['nom']}" for s in specs]
    g3 = grille["HE3"]
    for cfg in g3["configs"]:
        for x in g3["lois"]:
            t.append(f"HE3/{cfg}/{x['nom']}/fa")
            t += [f"HE3/{cfg}/{x['nom']}/conforme/{l}" for l in range(int(g3["conforme"]["L"]))]
    g6 = grille["HE6"]
    for cfg in g6["configs"]:
        for x in g6["lois"]:
            cle = f"HE6/{cfg}/{x['nom']}"
            t += [f"{cle}/calib", f"{cle}/p0"] + [f"{cle}/{s['nom']}" for s in g6["arrangements"]]
    return t


def configs_des_blocs(grille: dict, blocs: list[str]) -> list[str]:
    voulues = set()
    if "C" in blocs:
        voulues |= set(grille["C"])
    if "M" in blocs:
        voulues |= set(grille["M"])
    if "HE3" in blocs:
        voulues |= set(grille["HE3"]["configs"])
    if "HE6" in blocs:
        voulues |= set(grille["HE6"]["configs"])
    return [c for c in grille["configs"] if c in voulues]


def exiger_run_unique(racine: Path, sha_prereg: str, replication_de: str | None) -> None:
    """Un seul run décisif principal par préenregistrement, une seule réplication par run principal."""
    for chemin in sorted((racine / "runs").glob("*/manifeste.json")):
        try:
            m = json.loads(chemin.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            raise GardeArret(f"manifeste illisible {chemin} : {e}") from None
        cfg = m.get("config") or {}
        p = m.get("preenregistrement") or {}
        if not (m.get("decisif") and cfg.get("simulation") == SIMULATION and p.get("sha256") == sha_prereg):
            continue
        if replication_de is None and cfg.get("replication_de") is None:
            raise GardeArret(f"un run décisif existe déjà pour ce préenregistrement : {m.get('run_id')}")
        if replication_de is not None and cfg.get("replication_de") == replication_de:
            raise GardeArret(f"la réplication de {replication_de} existe déjà : {m.get('run_id')}")


def executer(racine: str | Path, prereg: str | Path, grille_chemin: str | Path, run_id: str,
             blocs: list[str] | None = None, replication_de: str | None = None, limite_s: float = 6 * 3600,
             verifier_import: bool = True) -> dict:
    """`blocs` n'est jamais accepté de l'extérieur : run principal complet ; en réplication, les blocs sont
    déterminés par la lecture principale. `verifier_import=False` n'est permis qu'aux tests sur mini-dépôt."""
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
    commande = "python -m controle_ia.simulation_essaim.run_essaim " + " ".join(sys.argv[1:])
    config = {"simulation": SIMULATION, "grille": grille, "grille_sha256": sha_grille, "blocs": blocs,
              "replication_de": replication_de, "commit_cite": commit_cite,
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
    sortie = {"lecture": lec, "journal_s": journal}
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
