"""Prépare la répétition jouet du script d'instance du rejeu à graine (VG-09), sans réseau ni carte : un dépôt git
local nu qui tient lieu de dépôt distant, dont le premier commit porte l'arbre gelé du commit du code courant
(`CHEMINS_GELES` : code, tests, scripts, dépendances ; égalité vérifiée entrée par entrée) sans les dossiers
documentaires lourds (hors de l'arbre gelé : `docs/` sauf les invites et les procédures que lit le code, `registres/`,
`livrables/`, `brouillons/`, `papiers/`, `traces/`), plus un P3 jouet joué par le vrai code de P3
(`premier_test_ia.run`, modèle minuscule du harnais), une table de tokenisation v2 jouet (épisodes hors de portée cités
« non résolus »), une configuration de la résolution à graine en mode « jouet » et un préenregistrement jouet scellés,
qui citent le commit du code, l'entropie, l'empreinte canonique de la configuration, « Tests attendus » et le chemin de
la configuration sous ses deux libellés (cœur, lot fidèle). Une seule configuration pour le cœur et le lot (clés du lot
comprises) ; `--non-tentes-coeur K` (défaut 1) épisodes « hors de portée » sont laissés non tentés par le cœur (clé
`repetition_non_tentes`, mode jouet seulement, refusée en mode réel) pour que l'étape du lot ait une cible et tourne.
Rien n'est écrit dans l'arbre de travail du dépôt source.

    PYTHONPATH=src:tests python scripts/preparer_repetition_r1_resolution_graine_v1.py --source . \\
        --dossier DOSSIER --tests-attendus N [--non-tentes-coeur K] [--sans-sceau-table] [--sans-citation-lot]

Écrit DOSSIER/distant.git (dépôt nu) et affiche « COMMIT=<commit à lancer> » et « DEPOT_URL=<chemin> ».
`--sans-sceau-table` : artefact (R5) — la table jouet est versée sans son sceau ; le script d'instance doit s'arrêter
avant l'installation. `--sans-citation-lot` : artefact (R5) — le préenregistrement jouet ne cite pas la configuration
sous le libellé du lot fidèle ; le script d'instance doit s'arrêter avant l'installation."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

RUN_P3 = "20261101-210000-p3-jouet"


def git(racine, *args) -> str:
    return subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True, text=True).stdout.strip()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--tests-attendus", required=True, type=int)
    ap.add_argument("--sans-sceau-table", action="store_true")
    ap.add_argument("--sans-citation-lot", action="store_true")
    ap.add_argument("--non-tentes-coeur", type=int, default=1)
    a = ap.parse_args(argv)
    source, dossier = Path(a.source).resolve(), Path(a.dossier).resolve()
    if dossier.exists():
        raise SystemExit(f"{dossier} existe déjà (R12)")
    dossier.mkdir(parents=True)
    prep = dossier / "preparation"
    prep.mkdir()
    code = git(source, "rev-parse", "HEAD")
    lourds = ("docs", "registres", "livrables", "brouillons", "papiers", "traces")
    gardes_docs = ("docs/sources/invites-2606.07054-v1", "docs/sources/invites-2606.08892-v1", "docs/procedures")
    hauts = [x.split("\t", 1)[1] for x in git(source, "ls-tree", code).splitlines()]
    archive = subprocess.run(["git", "-C", str(source), "archive", "--format=tar", code, "--",
                              *[h for h in hauts if h not in lourds], *gardes_docs],
                             check=True, capture_output=True).stdout
    subprocess.run(["tar", "-x", "-C", str(prep)], input=archive, check=True)
    git(prep, "init", "-q", "-b", "prep/repetition")
    git(prep, "config", "user.email", "repetition@example.invalid")
    git(prep, "config", "user.name", "repetition jouet")
    git(prep, "add", "-A")
    git(prep, "add", "-f", ".")
    git(prep, "commit", "-q", "-m", f"répétition : arbre gelé du commit {code}")
    sys.path[:0] = [str(prep / "src")]
    from controle_ia.harnais.validation_reelle import CHEMINS_GELES as geles

    exclus = tuple(x[len(":(exclude)"):] for x in geles if x.startswith(":(exclude)"))

    def gele(racine, rev):
        return [x for x in git(racine, "ls-tree", "-r", rev).splitlines()
                if not any(x.split("\t", 1)[1] == e or x.split("\t", 1)[1].startswith(e + "/") for e in exclus)]

    if gele(source, code) != gele(prep, "HEAD") or not gele(prep, "HEAD"):
        raise SystemExit("arbre gelé du dépôt de répétition ≠ arbre gelé du commit du code")
    sys.path[:0] = [str(prep / "tests")]

    from controle_ia.premier_test_ia import run as rp
    from controle_ia.runs_nuit import resolution_graine_lot_v1 as rl
    from controle_ia.runs_nuit import resolution_graine_v1 as rg
    from controle_ia.scellement import sceller
    from test_premier_test_ia_run import _config, _taches
    from test_runs_nuit_v2 import _table

    # P3 jouet, joué par le vrai code de P3, entropie fixée comme dans les essais (deux classes en validation)
    vraie = rp.creer_manifeste
    rp.creer_manifeste = lambda *x, entropie=None, **k: vraie(*x, entropie=20261017 if entropie is None else entropie, **k)
    pieces = prep / "donnees" / "repetition"
    pieces.mkdir(parents=True)
    f = _taches(pieces)
    git(prep, "add", "-A")
    git(prep, "add", "-f", "donnees")
    git(prep, "commit", "-q", "-m", "répétition : tâches jouet")
    c = _config(pieces)
    rp.executer(c, prep, RUN_P3, None, str(f), autoriser_depot_sale=True)
    rp.creer_manifeste = vraie
    fiches = prep / "diag" / RUN_P3 / "episodes-p3.json"
    t0 = dossier / "table0.json"
    _table(prep, f, c, fiches, t0)
    rel = lambda p: str(Path(p).resolve().relative_to(prep))  # noqa: E731
    d = prep / "donnees" / RUN_P3
    config = {"agent": {"nom": "agent-jouet"}, "mode": "jouet", "T": c["T"], "run_source": RUN_P3,
              "chemin_textes": rel(d / "textes-actions-p3.jsonl"), "textes_sha256": None,
              "chemin_scores": rel(d / "scores-p3.npz"), "scores_sha256": None, "identite_sha256": None,
              "chemin_fiches": rel(fiches), "fiches_sha256": None, "chemin_taches": rel(f), "taches_sha256": None,
              "chemin_consignes": rel(c["chemin_consignes"]), "consignes_sha256": c["consignes_sha256"],
              "chemin_manifeste_p3": f"runs/{RUN_P3}/manifeste.json", "manifeste_p3_sha256": None,
              "chemin_table_tokenisation": "prereg/R1-table-tokenisation-repetition.json",
              "table_tokenisation_sha256": None, "episodes_resolution": [], "temperature": c["temperature"],
              "max_nouveaux": c["max_nouveaux"], "noyau_attention": "math", "fils": 1, "hors_ligne": True,
              "fils_tirages": 2, "episodes_d_avance": 1, "seuil_ecart": 0.5, "quasi_egalites_max": 4,
              "bascules_max": 2, "combinaisons_max": 10, "combinaisons_max_validation": 10, "balayages_max": 8,
              "seuil_validation": 0, "duree_max_s": 600, "duree_max_episode_s": 120,
              "regle_validation": {"accord_moyen_min": 0.95, "accord_episode_min": 0.9, "accord_informatif_min": 0.9,
                                   "pas_informatifs_min": 1},
              # lot fidèle : même configuration que le cœur, clés du lot en plus
              "episodes_resolution_lot": [], "combinaisons_max_lot": 10, "duree_max_episode_lot_s": 120,
              "duree_max_lot_s": 600, "seuil_lecture_lot": 0.99}
    # classement sur la table jouet : épisodes hors de portée → « non résolus » de la table v2 jouet, à résoudre
    shutil.copy(t0, prep / config["chemin_table_tokenisation"])
    sceller(prep / config["chemin_table_tokenisation"])
    from controle_ia.environnements.lancer_pilote_a import charger_modele_et_format
    from controle_ia.harnais.run_harnais_factice import graine_entiere

    p0 = rg.charger_pieces({**config, "chemin_table_tokenisation": str(t0)}, prep)
    _, fmt = charger_modele_et_format(config["agent"], "jouet", graine_entiere(p0.manifeste_p3["graines"]["modele-jouet"]))
    cl = rg.classer(p0, fmt, int(c["T"]))
    connus = [e for e, x in cl.items() if x["identique_base"] or (x["entree"] and x["entree"]["methode"] != "non_resolu")]
    autres = [e for e in cl if e not in connus]
    table = json.loads(t0.read_text(encoding="utf-8"))
    table["episodes"] += [{"episode": e, "methode": "non_resolu", "trajectoire_p3": p0.fiches[e]["trajectoire"],
                           "fins": {}, "paires": [], "essais": {}} for e in autres]
    table["comptes"]["non_resolu"] = table["comptes"].get("non_resolu", 0) + len(autres)
    tp = prep / config["chemin_table_tokenisation"]
    Path(f"{tp}.sha256").unlink()
    tp.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if not a.sans_sceau_table:
        sceller(tp)
    if not connus or len(autres) <= a.non_tentes_coeur or a.non_tentes_coeur < 0:
        raise SystemExit(f"P3 jouet : {len(connus)} connus, {len(autres)} hors de portée ; {a.non_tentes_coeur} à laisser "
                         "au lot (il en faut au moins un résolu par le cœur)")
    # contrôle croisé (un épisode connu) en tête, puis les « hors de portée » ; les K premiers laissés au lot
    config.update(episodes_resolution=connus[:1] + autres, seuil_validation=len(connus),
                  **{rg.CLE_REPETITION: autres[:a.non_tentes_coeur]})
    rl.exiger_config(config)
    git(prep, "add", "-A")
    git(prep, "add", "-f", "donnees")
    git(prep, "commit", "-q", "-m", "répétition : P3 jouet et table jouet")
    code_cite = git(prep, "rev-parse", "HEAD")
    chemin_conf = prep / "prereg" / "R1-graine-config-repetition.json"
    chemin_conf.write_text(json.dumps(config, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(chemin_conf)
    h = "0123456789abcdef" * 4
    texte = "\n".join([
        "# Préenregistrement jouet (répétition du script d'instance du rejeu à graine)", "",
        f"- Commit du code d'analyse : `{code_cite}`",
        f"- Chemin de la configuration de la résolution à graine : `{chemin_conf.relative_to(prep)}`",
        f"- Configuration de la résolution à graine (empreinte canonique) : `{rg.empreinte_config(config)}`",
        *([] if a.sans_citation_lot else [f"- {rl.CONFIG_CITEE.format(rg.empreinte_config(config))}"]),
        "- Entropie : `20261102`", f"- Tests attendus : `{a.tests_attendus}`", "",
        *[f"## {s}\n\nRépétition jouet, sans valeur de preuve.\n" for s in
          ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
           "Critères de lecture gelés", "Liste d'arrêt")],
        "## Contre-lecture", "", f"Répétition jouet : brouillon `{h}`, rapport `{h[::-1]}`.", ""])
    chemin_p = prep / "prereg" / "R1-addendum-repetition.md"
    chemin_p.write_text(texte, encoding="utf-8")
    from controle_ia.prereg import sceller_prereg

    sceller_prereg(chemin_p)
    git(prep, "add", "-A")
    git(prep, "commit", "-q", "-m", "répétition : préenregistrement et configuration jouets")
    commit = git(prep, "rev-parse", "HEAD")
    distant = dossier / "distant.git"
    subprocess.run(["git", "clone", "-q", "--bare", f"file://{prep}", str(distant)], check=True)
    shutil.rmtree(prep)
    t0.unlink()
    Path(f"{t0}.sha256").unlink()
    print(f"COMMIT={commit}")
    print(f"DEPOT_URL={distant}")
    print(f"PREREG={chemin_p.relative_to(prep)}")
    print(f"EPISODES validation={len(connus)} resolution={len(config['episodes_resolution'])} "
          f"laisses_au_lot={len(config[rg.CLE_REPETITION])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
