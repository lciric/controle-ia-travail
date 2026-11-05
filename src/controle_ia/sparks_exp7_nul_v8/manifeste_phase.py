"""Manifeste de chaque phase de SPARKS-EXP7-NUL, v8 (répétition v7 : la fabrication s'arrêtait à la création du manifeste).

Comme R1 v4 (`prereg/R1-addendum-relance-v4.md`), le texte qui gouverne le run, cité comme `preenregistrement` du
manifeste et vérifié par `controle_ia.prereg.exiger_prereg_scelle` (sceau, huit sections, deux empreintes à la
« Contre-lecture »), est **l'addendum scellé** (`prereg/SPARKS-EXP7-NUL-addendum-1.md`). Le texte parent
(`prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md`, scellé le 4 novembre, inchangeable : R1, R12) reste cité dans la
configuration (`texte_parent`) et n'est vérifié que par son seul sceau, contre l'empreinte gelée `SHA_PREREG`. Les
graines restent dérivées de cette empreinte (`plan.entropie_prereg()`), comme en v1 à v7.

Refus (`GardeArret`, code 2), sans repli : texte parent altéré ou non scellé ; addendum absent (le texte parent seul ne
gouverne pas) ; addendum non conforme ou non scellé ; addendum qui ne cite pas le commit du code en entier ; addendum
factice de répétition (`addendum_factice.MARQUE`) hors du mode jouet.

    python -m controle_ia.sparks_exp7_nul_v8.manifeste_phase RUN_ID DEPART HTTP PHASE COMMIT_CODE LOTS MODE
"""
from __future__ import annotations

import sys
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste
from ..scellement import verifier
from ..sparks_exp7_nul_v3 import plan
from .addendum_factice import MARQUE


def verifier_texte_parent(racine: Path) -> str:
    sha = verifier(racine / plan.CHEMIN_PREREG)
    if sha != plan.SHA_PREREG:
        raise GardeArret(f"{plan.CHEMIN_PREREG} : empreinte {sha[:12]}… ≠ empreinte gelée {plan.SHA_PREREG[:12]}…")
    return sha


def verifier_addendum(racine: Path, commit_code: str, mode: str) -> tuple[Path, bool]:
    p = racine / plan.CHEMIN_ADDENDUM
    if not p.is_file():
        raise GardeArret(f"{plan.CHEMIN_ADDENDUM} absent : le texte parent seul ne gouverne pas le run (sa section "
                         "« Contre-lecture » ne porte pas les deux empreintes ; R1, R2)")
    t = p.read_text(encoding="utf-8")
    factice = MARQUE in t
    if factice and mode != "jouet":
        raise GardeArret(f"{plan.CHEMIN_ADDENDUM} : addendum factice de répétition hors du mode jouet (MODE={mode})")
    if commit_code not in t:
        raise GardeArret(f"{plan.CHEMIN_ADDENDUM} : le commit du code {commit_code[:12]} n'y est pas cité en entier")
    return p, factice


def creer(racine: str | Path, run_id: str, depart: str, http: str, phase: str, commit_code: str, lots: str, mode: str,
          commande: str | None = None) -> tuple[Path, dict]:
    racine = Path(racine)
    if mode not in ("reel", "jouet"):
        raise GardeArret(f"MODE={mode} : reel ou jouet attendu")
    sha_parent = verifier_texte_parent(racine)
    addendum, factice = verifier_addendum(racine, commit_code, mode)
    pl = plan.construire_plan()
    taches = sorted({f"ordre-{m.ident}" for m in plan.modeles_a_entrainer(pl, avec_reserve=True)}
                    | {f"partage-{c.ident}" for c in pl.values() if c.groupe != "ancre"} | set(plan.TACHES_NEUVES))
    cfg = {"etude": "SPARKS-EXP7-NUL", "addendum": plan.CHEMIN_ADDENDUM, "commit_code": commit_code, "phase": phase,
           "modele_depart": depart, "acces_http": http, "go": plan.GO_ID, "plafond_usd": plan.PLAFOND_USD,
           "lots_causal": lots, "hyper": "recette des auteurs (HYPER_AUTEURS)", "mode": mode,
           "texte_parent": {"chemin": plan.CHEMIN_PREREG, "sha256": sha_parent}, "addendum_factice": factice}
    return creer_manifeste(racine, run_id, cfg, taches, entropie=plan.entropie_prereg(), decisif=True,
                           prereg=addendum, commande=commande)


def main(argv: list[str]) -> int:
    if len(argv) != 7:
        print("usage : manifeste_phase RUN_ID DEPART HTTP PHASE COMMIT_CODE LOTS MODE", file=sys.stderr)
        return 2
    try:
        c, m = creer(Path("."), *argv, commande="manifeste_phase " + " ".join(argv))
    except GardeArret as err:
        print(f"MANIFESTE REFUSÉ : {err}", file=sys.stderr)
        return 2
    print(f"MANIFESTE CRÉÉ : {c} ; préenregistrement {m['preenregistrement']['chemin']} "
          f"({m['preenregistrement']['sha256'][:12]}…) ; texte parent {m['config']['texte_parent']['sha256'][:12]}…"
          + (" ; ADDENDUM FACTICE (jouet)" if m["config"]["addendum_factice"] else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
