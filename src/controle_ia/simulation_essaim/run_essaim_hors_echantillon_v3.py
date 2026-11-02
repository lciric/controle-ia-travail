"""Lanceur du préenregistrement hors échantillon — v3, **la commande citée** (contre-lecture 2 : M2, M9 ; Ra, Rb, Rc).

    PYTHONPATH=src <racine du dépôt principal>/.venv/bin/python -m controle_ia.simulation_essaim.run_essaim_hors_echantillon_v3 \\
        --prereg prereg/essaim-hors-echantillon-v1.md --grille prereg/essaim-hors-echantillon-grille-v1.json
    (depuis la racine de l'arbre de travail séparé)

    Réplication gelée (cellules statistiques contraires) : … --replication-de <run_id principal>

Différences avec `run_essaim_hors_echantillon_v2` (inchangé, non cité) :
- lecture `lecture_hors_echantillon_v3` (M3, M4) ; dans une réplication, la lecture des familles rejouées est
  `lire_partielle` (sans scores ni « trop beau », marquée `partielle` ; Rc) et seule la lecture finale fusionnée est
  annotée ;
- descriptif des maxima `blocs_hors_echantillon_v3` (référence iid aux mêmes (K, T), ex aequo départagés ; M2) ;
- Ra : la puissance exacte des 12 cellules S est certifiée aux seuils exacts **avant le manifeste**, donc avant tout
  tirage ; une erreur certifiée > 10⁻⁶ arrête le run sans rien écrire ;
- Rb : le journal git ajoute `git worktree list --porcelain` et `git fsck --unreachable --no-reflogs` ;
- M9 : une réplication n'est acceptée que d'un run principal lancé par ce lanceur (`exiger_principal_v3`). Le lanceur v1
  (et le v2) ne doit pas être lancé sur ce texte ; il ne peut pas en être empêché sans modifier son code (R12) : la
  garde de run unique, commune (même nom de simulation), empêche seulement un second run après lui.
Gardes réutilisées sans modification : `run_essaim_hors_echantillon_v1` (run unique, données P3, tâches), `run_t03`,
`run_essaim`.
"""
from __future__ import annotations

import argparse
import json
import subprocess
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
from . import blocs_hors_echantillon_v3 as BH3
from . import bornes_synchro_v2 as BS2
from . import calibrage as cal
from . import lecture_hors_echantillon_v3 as LEC
from .lecture_hors_echantillon_v2 import ERREUR_MAX_EXACTE
from .run_essaim import EQUIVALENCE_TOLERANCE, entropie_depuis_prereg
from .run_essaim_hors_echantillon_v1 import FAMILLES, SIMULATION, exiger_donnees_p3, exiger_run_unique
from .run_essaim_hors_echantillon_v1 import taches as taches_v1

LANCEUR = "controle_ia.simulation_essaim.run_essaim_hors_echantillon_v3"


def taches(grille: dict) -> list[str]:
    return taches_v1(grille) + BH3.taches_maxima(grille)


def certifier_puissances_S(grille: dict) -> dict:
    """Ra : puissance exacte de `coelev_comptage` aux seuils exacts de S, avant tout tirage."""
    sortie = {}
    q, a = float(grille["q"]), float(grille["alpha"])
    for cfg, specs in grille["S"].items():
        K, T = int(grille["configs"][cfg]["K"]), int(grille["configs"][cfg]["T"])
        seuil = cal.seuils_exacts(K, T, q, a)["coelev_comptage"]
        for s in specs:
            v, e = BS2.puissance_exacte(K, T, int(s["m"]), q, seuil)
            if not e <= ERREUR_MAX_EXACTE:
                raise GardeArret(f"S/{cfg}/{s['nom']} : erreur certifiée {e} > {ERREUR_MAX_EXACTE}, avant tout tirage "
                                 "(liste d'arrêt)")
            sortie[f"S/{cfg}/{s['nom']}"] = {"puissance": v, "erreur_certifiee": e, "seuil": list(seuil)}
    return sortie


def exiger_principal_v3(racine: Path, run_id: str) -> None:
    """M9 : on ne réplique qu'un run principal lancé par ce lanceur."""
    chemin = racine / "runs" / run_id / "manifeste.json"
    try:
        m = json.loads(chemin.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise GardeArret(f"manifeste du run principal {run_id} illisible : {e}") from None
    if (m.get("config") or {}).get("lanceur") != LANCEUR:
        raise GardeArret(f"le run principal {run_id} n'a pas été lancé par {LANCEUR} : réplication refusée")


def journal_git(racine: Path) -> dict:
    sortie = {}
    for nom, args in (("log", ["log", "--format=%H %cI %s", "-n", "40"]), ("reflog", ["reflog", "--date=iso", "-n", "80"]),
                      ("statut", ["status", "--porcelain", "--untracked-files=all"]),
                      ("arbres", ["worktree", "list", "--porcelain"]),
                      ("inaccessibles", ["fsck", "--unreachable", "--no-reflogs"])):
        r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True, text=True)
        sortie[nom] = r.stdout.splitlines() if r.returncode == 0 else [f"erreur : {r.stderr.strip()}"]
    return sortie


def tableau_md(lecture: dict, programme: list[dict], titre: str) -> str:
    l = [f"# {titre}", "", LEC.PHRASE_PORTEE, ""] + LEC.scores_md(lecture) + [
        f"Lecture mécanique (`{LEC.VERSION}`), intervalles exacts de Clopper-Pearson de niveau 1 − {lecture['gamma']:g}.",
        "", "| prédiction | nature | statut | verdict | cellules | conformes | contraires | à répliquer | à auditer |",
        "|---|---|---|---|---|---|---|---|---|"]
    for k, x in lecture["predictions"].items():
        l.append(f"| {k} | {x['nature']} | {x['statut']} | {x['verdict']} | {x['n_cellules']} | {x['n_conformes']} | "
                 f"{x['n_contraires']} | {len(x.get('a_repliquer', []))} | {len(x.get('a_auditer', []))} |")
    a = lecture["audit_symetrie"]
    l += ["", f"Variances des écarts réduits, bornes {a['bornes']} : formes closes {a['formes_closes']['variance_z']:.3f} "
          f"sur {a['formes_closes']['n']} ; égalités {a['egalites']['variance_z']:.3f} sur {a['egalites']['n']}. "
          "`audit_declenche` ne compte que ces variances et « trop beau » ; réfutations, violations et arrêts déclenchent "
          "leur audit par la table des issues.", "", "## Énoncés", "", "| énoncé | lecture | exigées |", "|---|---|---|"]
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
        exiger_principal_v3(racine, replication_de)
        corps = verifier_resultat(racine, racine / "diag" / replication_de / "lecture.json")
        principale = corps["resultat"]["lecture"]
        preds = {k.split(".")[0] for k, x in principale["predictions"].items() if x["a_repliquer"]}
        familles = sorted({b for p in preds for b in LEC.BLOCS_DE.get(p, ())})
        if not familles:
            raise GardeArret("rien à répliquer dans la lecture principale")
    certifiees = certifier_puissances_S(grille) if "S" in familles else {}
    ts = taches(grille)
    config = {"simulation": SIMULATION, "lanceur": LANCEUR, "lecture": LEC.VERSION, "grille": grille,
              "grille_sha256": sha_grille, "donnees_p3_sha256": sha_p3, "familles": familles,
              "replication_de": replication_de, "commit_cite": commit_cite,
              "regle_graine": "entropie = int(sha256(préenregistrement scellé)[:32], 16)", "entropie": str(entropie)}
    chemin_m, m = creer_manifeste(racine, run_id, config, ts + [x + "/replication" for x in ts], entropie=entropie,
                                  decisif=True, prereg=prereg, commande=f"python -m {LANCEUR} " + " ".join(sys.argv[1:]))
    ecrire_resultat(racine, chemin_m, "journal-git", journal_git(racine))
    if certifiees:
        ecrire_resultat(racine, chemin_m, "puissances-exactes-S", certifiees)
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
    if replication_de is None:
        ecrire_resultat(racine, chemin_m, "descriptif-maxima", BH3.bloc_maxima(ctx, racine))
        chrono("descriptif-maxima")
        lec = LEC.lire(resultats, grille)
        finale = lec
    else:
        lec = LEC.lire_partielle(resultats, grille)
        finale = LEC.annoter(LEC.fusionner(principale, lec))
    sortie = {"lecture": lec, "journal_s": journal, "portee": LEC.PHRASE_PORTEE}
    if principale is not None:
        sortie["lecture_finale"] = finale
    sortie["scores"] = finale["scores"]
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
