#!/usr/bin/env python3
"""Configuration réelle de la course de T0.8 — programme qui l'écrit à partir du texte scellé (consigne de la chaîne de
lancement, `722ceb5e…`, tenue en v3 `6f52c4db…` ; texte au brouillon 15 `8d68b7a0…`, § 3.2). v1.

La configuration ne peut être finie qu'après le scellement du texte (commit du code, entropie) : ce programme l'écrit alors,
**à partir du texte scellé et des marqueurs que le scellement a remplis, jamais d'ailleurs** :

- valeurs gelées de la course, agent de 7b et juges : les constantes du code de T0.8 (`configuration_v1.VALEURS_GELEES_COURSE`,
  `SPEC_AGENT_7B`, `SPEC_JUGES`), que le code exige déjà égales au texte (`exiger_valeurs_gelees`, `exiger_spec_agent`,
  `exiger_spec_juge`) ;
- les sept marqueurs (`--marqueurs`, fichier JSON écrit par le programme de scellement, une clé par marqueur) : forme contrôlée
  par `exiger_marqueurs`, présence de leurs valeurs dans le texte scellé par `exiger_marqueurs_au_texte` ;
- les entrées de la course (`course_v1.ENTREES_COURSE_REQUISES`) : tâches, consignes et invite dérivée aux chemins et
  empreintes du texte (`configuration_v1.ENTREES_CONSTANTES`) ; textes, épisodes et manifeste de 7b aux chemins du run
  `RUN_7B` (plan d'analyse, point 1) et aux empreintes de `EMPREINTES_ENTREES_7B` ;
- la section `lancement`, lue par la chaîne et jamais par la course : bornes de l'offre (section « Machine » : chaque valeur
  n'est écrite que si sa phrase figure telle quelle dans le texte scellé, `PHRASES_MACHINE`), plafond cumulé (marqueur `GO_T08`,
  phrase « 120 USD » du texte), seuil du compte rendu (40 USD, phrase du texte), lignes de GO admises (l'identifiant du marqueur
  `GO_T08` et les prolongations que le texte cite, `--go-admis`, chacune citée telle quelle par le texte), aucune carte de relance
  (aucune H200, section « Machine ») ; fin de validité et calendrier ne sont pas écrits ici : la chaîne les lit au registre des GO
  le jour de la création.

Contrôle final : `course_v1.exiger_course_reelle(config, texte)` (marqueurs, valeurs gelées, agent, juges, entrées rattachées au
texte, texte scellé portant les marqueurs) ; puis écriture (refus d'écraser, R12) et compagnon `.sha256` (R6).

    PYTHONPATH=src python3 -B scripts/ecrire_configuration_course_t08_v1.py --texte prereg/T0.8-bases-boite-noire-v0-v1.md \
        --marqueurs <marqueurs.json> --go-admis GO-2026-11-10-12,GO-2026-11-22-79 --sortie prereg/T0.8-configuration-course-v1.json

Codes : 0 écrit (empreinte sur la sortie standard) ; 1 arrêt (rien d'écrit) ; 2 usage.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
if str(RACINE / "src") not in sys.path:
    sys.path.insert(0, str(RACINE / "src"))

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.scellement import sceller, verifier  # noqa: E402
from controle_ia.t08 import configuration_v1 as cf  # noqa: E402

VERSION = "ecrire_configuration_course_t08_v1"
# section « Machine, devis et dépense » du texte : phrase exigée telle quelle (après retrait du gras « ** ») → valeur écrite
PHRASES_MACHINE = {
    "une carte A100 SXM4 80 Go": ("carte", {"nom": "A100 SXM4 80 Go", "nom_offre": "A100 SXM4", "memoire_carte_min_mo": 80000}),
    "au plus 1,30 USD de l'heure": ("prix_max_usd_h", 1.3),
    "au moins 8 cœurs effectifs": ("coeurs_effectifs_min", 8),
    "64 Go de mémoire vive": ("memoire_vive_min_mo", 64000),
    "100 Go de disque": ("disque_min_go", 100),
    "stockage au plus 0,08 USD de l'heure": ("stockage_max_usd_h", 0.08),
    "téléchargement au plus 0,05 USD par Go": ("telechargement_max_usd_go", 0.05),
    "téléchargement ≤ 40 Go": ("telechargement_go_prevu", 40),
    "aucune relance automatique sur H200": ("relance", None),
}
PHRASE_PLAFOND = "120 USD cumulés"
PHRASE_COMPTE_RENDU = "compte rendu à 40 USD"
COMPTE_RENDU_USD = 40
ETIQUETTE = "t08-v1"
_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")


def _plat(texte: str) -> str:
    return re.sub(r"\s+", " ", texte.replace("**", ""))


def entrees_course(marqueurs: dict) -> dict:
    run = marqueurs["RUN_7B"]["run_id"]
    emp = marqueurs["EMPREINTES_ENTREES_7B"]
    e = {n: {"chemin": c, "sha256": s, "phase": "course"} for n, (c, s) in cf.ENTREES_CONSTANTES.items()
         if n in ("taches", "consignes", "invite")}
    e["textes_7b"] = {"chemin": f"donnees/{run}/textes-actions-t06.jsonl", "sha256": emp["textes-actions-t06.jsonl"],
                      "phase": "course"}
    e["episodes_7b"] = {"chemin": f"diag/{run}/episodes-t06.json", "sha256": emp["episodes-t06.json"], "phase": "course"}
    e["manifeste_7b"] = {"chemin": f"runs/{run}/manifeste.json", "sha256": emp["manifeste.json"], "phase": "course"}
    return dict(sorted(e.items()))


def lancement(texte: str, marqueurs: dict, go_admis: list[str]) -> dict:
    plat = _plat(texte)
    manquantes = [p for p in PHRASES_MACHINE if p not in plat]
    for p in (PHRASE_PLAFOND, PHRASE_COMPTE_RENDU):
        if p not in plat:
            manquantes.append(p)
    if manquantes:
        raise GardeArret(f"phrases de la section « Machine » absentes du texte scellé : {manquantes} : aucune valeur inventée")
    offre, carte = {}, None
    for _, (cle, v) in PHRASES_MACHINE.items():
        if cle == "carte":
            carte = dict(v)
        elif cle == "prix_max_usd_h":
            carte_prix = v
        elif cle != "relance":
            offre[cle] = v
    carte["prix_max_usd_h"] = carte_prix
    offre["etiquette"] = ETIQUETTE
    go = marqueurs["GO_T08"]
    if go["plafond_usd"] != 120:
        raise GardeArret(f"GO_T08.plafond_usd {go['plafond_usd']} ≠ 120 USD du texte (« {PHRASE_PLAFOND} »)")
    if not go_admis or go_admis[0] != go["id"]:
        raise GardeArret(f"lignes de GO admises {go_admis} : la première doit être celle du marqueur GO_T08 ({go['id']})")
    for g in go_admis:
        if not _GO.match(g) or not cf._tel_quel(texte, g):
            raise GardeArret(f"ligne de GO {g!r} illisible ou non citée telle quelle par le texte scellé")
    if len(set(go_admis)) != len(go_admis):
        raise GardeArret("ligne de GO admise en double")
    return {"go_origine": go["id"], "go_admis": list(go_admis), "plafond_usd": go["plafond_usd"],
            "compte_rendu_usd": COMPTE_RENDU_USD, "carte": {"course": carte}, "offre": dict(sorted(offre.items())),
            "relance": "aucune (aucune carte H200 sans un mot de Lazar ; section « Machine »)"}


def construire(texte_chemin: Path, marqueurs: dict, go_admis: list[str]) -> dict:
    from controle_ia.t08.course_v1 import exiger_course_reelle

    mq = cf.exiger_marqueurs(marqueurs)
    if set(mq) != set(cf.MARQUEURS):
        raise GardeArret(f"marqueurs {sorted(set(mq) - set(cf.MARQUEURS))} hors de la liste du texte")
    verifier(texte_chemin)
    texte = Path(texte_chemin).read_text(encoding="utf-8")
    if re.search(r"<<[A-Z0-9_]+>>", texte):
        raise GardeArret("texte scellé portant encore un marqueur « <<…>> » : non scellable, aucune configuration")
    config = {"mode": "reel", "objet": "course de T0.8 (épisodes honnêtes d'étalonnage, juges J8 et J3)",
              "version_programme": VERSION, **cf.VALEURS_GELEES_COURSE, "agent": dict(cf.SPEC_AGENT_7B),
              "juges": json.loads(json.dumps(cf.SPEC_JUGES)), "entrees": entrees_course(mq), "marqueurs": mq,
              "lancement": lancement(texte, mq, go_admis)}
    exiger_course_reelle(config, str(texte_chemin))
    return config


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="ecrire_configuration_course_t08_v1.py")
    ap.add_argument("--texte", required=True)
    ap.add_argument("--marqueurs", required=True)
    ap.add_argument("--go-admis", required=True, help="identifiants séparés par des virgules ; le premier est GO_T08")
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args(argv)
    sortie = Path(a.sortie)
    try:
        if sortie.exists() or Path(str(sortie) + ".sha256").exists():
            raise GardeArret(f"{sortie} existe déjà : nouvelle version = nouveau nom (R12)")
        marqueurs = json.loads(Path(a.marqueurs).read_text(encoding="utf-8"))
        config = construire(Path(a.texte), marqueurs, [g.strip() for g in a.go_admis.split(",") if g.strip()])
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(json.dumps(config, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        sha = sceller(sortie)
    except (GardeArret, json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"ARRÊT ({VERSION}) : {type(e).__name__} : {e}", file=sys.stderr)
        return 1
    print(json.dumps({"version": VERSION, "sortie": str(sortie), "sha256": sha}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
