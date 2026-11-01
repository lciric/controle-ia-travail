"""Lanceur du préenregistrement hors échantillon — v2 (corrections de la contre-lecture 1 : C1, C5, C6, C9 ; R3).

    <racine du dépôt principal>/.venv/bin/python -m controle_ia.simulation_essaim.run_essaim_hors_echantillon_v2 \\
        --prereg prereg/essaim-hors-echantillon-v1.md --grille prereg/essaim-hors-echantillon-grille-v1.json
    (avec PYTHONPATH=src, depuis la racine de l'arbre de travail séparé)

    Réplication gelée (cellules statistiques contraires) : … --replication-de <run_id principal>

Différences avec `run_essaim_hors_echantillon_v1` (inchangé, qui n'est pas la commande citée) :
- lecture `lecture_hors_echantillon_v2` (HS.3 exacte, HP.4 bilatérale, scores séparés, « trop beau ») ; la lecture
  finale après réplication est annotée de nouveau ; `lecture.md` porte la phrase de portée puis les trois scores en tête ;
- descriptif de la position des maxima (R3, `blocs_hors_echantillon_v2.bloc_maxima`, run principal seulement) ;
- journal git (`git log` et `git reflog` de l'arbre, sans tri) consigné dans `diag/<run_id>/journal-git.json` (C5).
Même nom de simulation que v1 (`essaim-hors-echantillon-v1`) : la garde de run unique est commune aux deux lanceurs.
Gardes réutilisées de v1 sans modification : `exiger_run_unique`, `exiger_donnees_p3`, `taches`, et celles de
`simulation_t03.run_t03` et `run_essaim`.
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
from . import blocs_hors_echantillon_v2 as BH2
from . import lecture_hors_echantillon_v2 as LEC
from .run_essaim import EQUIVALENCE_TOLERANCE, entropie_depuis_prereg
from .run_essaim_hors_echantillon_v1 import FAMILLES, SIMULATION, exiger_donnees_p3, exiger_run_unique
from .run_essaim_hors_echantillon_v1 import taches as taches_v1

LANCEUR = "controle_ia.simulation_essaim.run_essaim_hors_echantillon_v2"


def taches(grille: dict) -> list[str]:
    return taches_v1(grille) + BH2.taches_maxima(grille)


def journal_git(racine: Path) -> dict:
    sortie = {}
    for nom, args in (("log", ["log", "--format=%H %cI %s", "-n", "40"]), ("reflog", ["reflog", "--date=iso", "-n", "80"]),
                      ("statut", ["status", "--porcelain", "--untracked-files=all"])):
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
          f"sur {a['formes_closes']['n']} ; égalités {a['egalites']['variance_z']:.3f} sur {a['egalites']['n']}.", "",
          "## Énoncés", "", "| énoncé | lecture | exigées |", "|---|---|---|"]
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
    ecrire_resultat(racine, chemin_m, "journal-git", journal_git(racine))
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
        ecrire_resultat(racine, chemin_m, "descriptif-maxima", BH2.bloc_maxima(ctx, racine))
        chrono("descriptif-maxima")
    lec = LEC.lire(resultats, grille)
    sortie = {"lecture": lec, "journal_s": journal, "portee": LEC.PHRASE_PORTEE}
    finale = LEC.annoter(LEC.fusionner(principale, lec)) if principale is not None else lec
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
