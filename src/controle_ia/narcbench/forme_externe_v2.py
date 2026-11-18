"""Essai de forme des activations publiées de NARCBench, v2 (bras externe, R-2175 ; mandat du développeur v2).

**Aucun score** : ce module ne calcule ni direction, ni projection, ni aire, ni statistique d'agent ou d'épisode. Il rend des
formes, des types, des clés et des **comptes** (lignes, tours, agents, épisodes, domaines, exclusions), après la vérification
des tailles et des empreintes (`chargeur_externe_v1.verifier_fichiers`, R11). Les champs de résultat du jeu (`agent_vote`,
`target_option`, `target_majority`, `collusion_success`, `fair_option`, `label_variant`, `bp_corr`, `flagged`) ne sont **jamais
lus** ici : seule leur présence est vérifiée par le chargeur (20 champs exacts).

Ce que l'essai établit pour le texte court (rapport v1, § 6 et § 10) :
- les clés `layer_<i>` de chaque `.npz`, leur forme et leur type, lus dans l'en-tête de chaque tableau **sans charger ses
  valeurs** ; l'alignement des lignes sur les métadonnées (le code des auteurs tronque `[:n]` sans le dire : ici, égalité exigée
  par le chargeur) ;
- les comptes par (mode, rôle, canal, phase), et les tours présents par (canal, phase) : **E3** (combien de tours de
  discussion entrent dans la moyenne des auteurs) ;
- le nombre de tours de discussion publics par (épisode, agent) ;
- les effectifs de l'apprentissage par message (**E1**) : lignes publiques de discussion des épisodes de collusion, par rôle ;
- les épisodes rendus par le chargeur v1, par condition, et les exclusions comptées (agents ≠ 4, tours inégaux) ;
- les domaines (règle des auteurs sur `run_id`) et leur concordance avec le champ `scenario_domain`, le domaine vide compris
  (le code des auteurs ne le tient jamais à l'écart).

Commande (sortie JSON, jamais écrasée, R12) :
    PYTHONPATH=src python -m controle_ia.narcbench.forme_externe_v2 <racine des données> <sortie.json>
"""
from __future__ import annotations

import json
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from numpy.lib import format as npy_format

from ..gardes import GardeArret
from . import chargeur_externe_v1 as C

CHAMPS_LUS = ("run_id", "mode", "role", "channel", "phase", "round", "agent_name", "scenario_domain")


def entetes_npz(chemin: Path) -> dict:
    """{clé: {"forme", "type", "ordre_fortran"}} lus dans l'en-tête `.npy` de chaque membre, sans charger les valeurs."""
    sortie = {}
    with zipfile.ZipFile(chemin) as z:
        for nom in sorted(z.namelist()):
            if not nom.endswith(".npy"):
                raise GardeArret(f"{Path(chemin).name} : membre {nom!r} qui n'est pas un tableau .npy")
            with z.open(nom) as f:
                version = npy_format.read_magic(f)
                if version == (1, 0):
                    forme, fortran, dtype = npy_format.read_array_header_1_0(f)
                elif version == (2, 0):
                    forme, fortran, dtype = npy_format.read_array_header_2_0(f)
                else:
                    raise GardeArret(f"{Path(chemin).name}/{nom} : version d'en-tête .npy {version} non prise en charge")
            if dtype.hasobject:
                raise GardeArret(f"{Path(chemin).name}/{nom} : tableau d'objets (refusé, données non sûres)")
            sortie[nom[:-4]] = {"forme": [int(x) for x in forme], "type": str(dtype), "ordre_fortran": bool(fortran)}
    return sortie


def _comptes_metadonnees(meta: list) -> dict:
    """Comptes sur les seuls champs de structure (`CHAMPS_LUS`) ; aucun champ de résultat du jeu n'est lu."""
    par_cle = Counter((m["mode"], m["role"], m["channel"], m["phase"]) for m in meta)
    tours = defaultdict(Counter)
    for m in meta:
        tours[f"{m['channel']}/{m['phase']}"][str(m["round"])] += 1
    mode_par_run = {}
    for m in meta:
        if mode_par_run.setdefault(m["run_id"], m["mode"]) != m["mode"]:
            raise GardeArret(f"{m['run_id']} : deux modes dans un même épisode")
    runs_par_mode = defaultdict(set)
    for r, mode in mode_par_run.items():
        runs_par_mode[mode].add(r)
    # tours de discussion publics par (épisode, agent) : E3
    disc = defaultdict(list)
    for m in meta:
        if m["channel"] == "public" and m["phase"] == "discussion":
            disc[(m["run_id"], m["agent_name"])].append(m["round"])
    hist_disc = Counter(len(v) for v in disc.values())
    jeux_de_tours = Counter(tuple(sorted(str(r) for r in v)) for v in disc.values())
    # effectifs de l'apprentissage par message (E1) : collusion, public, discussion
    appr = Counter(m["role"] for m in meta
                   if m["mode"] == "collusion" and m["channel"] == "public" and m["phase"] == "discussion")
    # domaines (règle des auteurs) et concordance avec `scenario_domain`
    dom_par_run, ecarts_dom = {}, Counter()
    for m in meta:
        d = C.domaine(m["run_id"])
        dom_par_run[m["run_id"]] = d
        if m["scenario_domain"] != d:
            ecarts_dom[(d, str(m["scenario_domain"]))] += 1
    domaines = defaultdict(Counter)
    for r, d in dom_par_run.items():
        domaines[d][mode_par_run[r]] += 1
    return {
        "lignes": len(meta),
        "par_mode_role_canal_phase": {"/".join(map(str, k)): v for k, v in sorted(par_cle.items())},
        "tours_par_canal_phase": {k: dict(sorted(v.items())) for k, v in sorted(tours.items())},
        "runs_par_mode": {k: len(v) for k, v in sorted(runs_par_mode.items())},
        "discussion_publique_tours_par_agent": {str(k): v for k, v in sorted(hist_disc.items())},
        "discussion_publique_jeux_de_tours": {",".join(k): v for k, v in sorted(jeux_de_tours.items())},
        "apprentissage_par_message_lignes_par_role": dict(sorted(appr.items())),
        "domaines_runs_par_mode": {d: dict(sorted(c.items())) for d, c in sorted(domaines.items())},
        "domaine_vide_present": "" in domaines,
        "scenario_domain_different_du_domaine_des_auteurs": {f"{a} | {b}": v for (a, b), v in sorted(ecarts_dom.items())},
    }


def forme_modele_etage(racine: Path, modele: str, etage: str) -> dict:
    """Forme d'un (modèle, étage) : en-têtes du `.npz`, comptes des métadonnées, épisodes et exclusions du chargeur v1."""
    d = Path(racine) / "activations" / modele / etage
    entetes = entetes_npz(d / "activations_gen.npz")
    donnees = C.charger(racine, modele, etage)          # 20 champs, couches de la bande, float32, alignement, finitude
    meta, eps, exclus = donnees["meta"], donnees["episodes"], donnees["exclusions"]
    for cle, e in entetes.items():
        if e["forme"][0] != len(meta):
            raise GardeArret(f"{modele}/{etage}/{cle} : {e['forme'][0]} lignes pour {len(meta)} lignes de métadonnées")
    formes_ep = Counter(tuple(int(x) for x in e["acts"].shape) for e in eps)
    colludeurs = Counter((e["condition"], int(np.asarray(e["colludeurs"]).sum())) for e in eps)
    return {
        "npz": {"cles": sorted(entetes), "entetes": entetes,
                "bande_attendue": [f"layer_{c}" for c in C.BANDES[modele]],
                "bande_presente": all(f"layer_{c}" in entetes for c in C.BANDES[modele]),
                "largeur_attendue": C.LARGEURS[modele]},
        "metadonnees": _comptes_metadonnees(meta),
        "chargeur_v1": {"episodes_par_condition": dict(sorted(Counter(e["condition"] for e in eps).items())),
                        "formes_acts": {"x".join(map(str, k)): v for k, v in sorted(formes_ep.items())},
                        "colludeurs_par_condition": {f"{c}/{n}": v for (c, n), v in sorted(colludeurs.items())},
                        "exclusions": {k: sorted(v) for k, v in exclus.items()},
                        "domaines_des_episodes": dict(sorted(Counter(e["domaine"] for e in eps).items()))},
    }


def essai_de_forme(racine: Path, modeles=C.MODELES, etages=C.ETAGES, attendues: dict = C.EMPREINTES_PUBLIEES) -> dict:
    """Vérifie tailles et empreintes (arrêt au premier écart), puis rend la forme de chaque (modèle, étage). Aucun score.
    `attendues` : les empreintes publiées (défaut) ; un autre jeu ne sert qu'aux essais sur fichiers factices."""
    verif = C.verifier_fichiers(racine, attendues)
    sortie = {"objet": "essai de forme des activations publiées de NARCBench (bras externe), sans aucun score",
              "revision_jeu": C.REVISION_JEU, "racine": str(Path(racine)),
              "date_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "fichiers_verifies": verif, "champs_de_metadonnees_lus": list(CHAMPS_LUS), "formes": {}}
    for modele in modeles:
        for etage in etages:
            sortie["formes"][f"{modele}/{etage}"] = forme_modele_etage(racine, modele, etage)
    return sortie


def main(argv=None, attendues: dict | None = None) -> int:
    """`attendues` : None en usage réel (empreintes publiées) ; un autre jeu ne sert qu'aux essais sur fichiers factices."""
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) != 2:
        raise SystemExit("usage : python -m controle_ia.narcbench.forme_externe_v2 <racine des données> <sortie.json>")
    racine, sortie = Path(argv[0]), Path(argv[1])
    if sortie.exists():
        raise GardeArret(f"{sortie} existe : on n'écrase jamais (R12)")
    res = essai_de_forme(racine, attendues=C.EMPREINTES_PUBLIEES if attendues is None else attendues)
    sortie.write_text(json.dumps(res, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(sortie)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["entetes_npz", "forme_modele_etage", "essai_de_forme", "CHAMPS_LUS"]
