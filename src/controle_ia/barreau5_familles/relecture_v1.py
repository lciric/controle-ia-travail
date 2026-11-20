"""Relecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») sur l'instance de lecture. Texte scellé
`prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f…`), « Plan d'analyse », points 7
(deuxième tiret), 8, 9, 10, 14 et 18 ; « Métrique » (activations, intensité, déplacement moyen, produits) ; « Données
gardées » ; « Liste d'arrêt », points 1, 3, 5 à 9 et 11. Code neuf (R12), v1, écrit sans aucune donnée (modèle jouet et
fichiers fabriqués seulement) ; en mode réel, le chemin est le même avec le modèle de la configuration scellée, sur la carte :
jamais lancé ici.

Une marche, dans l'ordre du point 8 :
1. gardes avant tout manifeste : configuration (clés exactes ; recette égale à la configuration scellée en mode réel) ;
   registre propre au commit de la marche (plan décisif : `ENGAGEMENT-B5F` présente et antérieure à la marche, postérieure
   à `SORTIES-FORMATION-B5F` et à toute ligne de relance ; `CODE-LECTURE-B5F` et code au commit ; `EPREUVE-B5F` pour la même
   empreinte du programme de lecture ; `GO-LECTURE-B5F` égale à l'accord de la configuration ; ni `SCORES-B5F` ni
   `OUVERTURE-B5F`) ; **entrées de lecture** (point 7, deuxième tiret : adaptateurs tenus à l'écart sous leurs noms opaques,
   adaptateurs d'apprentissage étiquetés, épisodes d'évaluation des saboteurs d'apprentissage, et rien d'autre ; chaque
   fichier à son empreinte) ; **arbre de la session** sans table des étiquettes, sans branche de la formation, sans coût d'un
   adaptateur tenu à l'écart (liste d'arrêt, point 8) ;
2. modèle, logits d'un contexte de contrôle avant l'injection ; injection (recette), adaptateurs en simple précision, dose 0,
   modèle nu vérifié ; chaque adaptateur chargé à son empreinte (clés et formes de l'état injecté) ;
3. (a) 64 textes honnêtes communs, un par tâche d'évaluation, joués une fois sur le modèle nu (environnement honnête, graines
   `b5f/lecture/honnete/tache/<id>`) ; activations d'origine des 8 épisodes du chemin (`b5f/lecture/chemin`), en mémoire ;
   la série du modèle nu est **relue par le même chemin forcé** que les adaptateurs (dose 0) ;
4. (b) chemin éprouvé : les 8 épisodes relus à l'état « modèle nu » égaux au bit près à leur origine (cas sain) ; relus sous
   un adaptateur d'apprentissage à la dose 1, différents (artefact) ; sinon arrêt avant toute notation (point 11) ;
5. (c) chaque adaptateur, dans un ordre tiré par graine (`b5f/lecture/ordre`) : identité à dose 0 et artefact à dose 1 ;
   série nominale (trois couches) et divergence des sorties ; aucune autre série ; puis déplacement moyen δ̄ (couche 15),
   direction ĝ (saboteurs d'apprentissage), produits P de toutes les paires et poussées le long de ĝ, par
   `lecture_v1.produits_et_poussees`, sans aucune étiquette des familles tenues à l'écart ;
6. (d) épisodes d'évaluation des saboteurs d'apprentissage relus sous leur propre adaptateur (trois couches) ;
7. sondes et notation fermée (`sondes_v1`) ; fichiers fermés (arbre de lecture : inventaire, bilan, textes honnêtes, scores,
   produits, intensités ; l'empreinte de l'inventaire est le contenu de `SCORES-B5F`) ; activations selon « Données
   gardées » et la règle de garde de la configuration (trois couches ; couche 15 seule ; une action sur dix tirée par graine,
   `b5f/tirages/garde-activations`), inventaire de toutes les activations écrites.
**Aucune statistique d'adaptateur tirée d'un score de sonde n'est calculée ici, et aucune grandeur d'un adaptateur (produits,
poussées, divergences, normes) n'est imprimée ni écrite ailleurs que dans les fichiers fermés** (liste d'arrêt, point 7) : les
journaux ne portent que des étapes et des comptes.

Toutes les grandeurs sont calculées sur les activations arrondies à la demi-précision puis lues en double précision, comme
elles sont gardées : une relecture des fichiers les rend à l'identique.

Écarts déclarés au texte (rapport du développeur) : clés de graines ajoutées `b5f/lecture/injection` (sans effet : chaque
état chargé remplace A et B), `b5f/modele-jouet` (mode jouet), `b5f/sonde/controle-carte/choix` et `…/actions` ; divergence
des sorties : à chaque jeton noté, divergence de Kullback-Leibler de la loi du jeton suivant du modèle nu à celle du modèle
adapté, lue à la position de ce jeton.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch

from ..environnements.pilote_a import charger_taches, graines_des_actions, tache_de
from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.activations import ecarts_par_jeton, passe_unique
from ..harnais.episode import Action
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, graines as graines_manifeste
from ..organismes import lora as lo
from ..premier_test_ia.conditions import environnement
from ..scellement import empreinte, sceller, verifier
from ..t06 import distillation_transcription as dt
from ..t06.cout import cout_action
from ..t06.identite import controle_identite, exiger_etat_de_phase, logits_de_controle
from ..t06.lanceur import _fin_notee
from ..t06.lanceur_v2 import ActivationsDemi
from ..t07bbis.etat_impose_v1 import demi
from . import engagement_v1 as en
from . import lecture_v1 as lv
from . import sondes_v1 as sv

COMMANDE = "python -m controle_ia.barreau5_familles.relecture_v1"
CONFIG_SCELLEE = {"chemin": "prereg/T0.6-organismes-config-7b-v1.json",
                  "sha256": "b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527"}
CLES_RECETTE = ("agent", "T", "lot", "max_nouveaux", "temperature", "noyau_attention", "fils", "memoire_vive_min_go",
                "taches_evaluation", "adaptateur", "couches")
CLES_PLAN = ("mode", "plan", "entrees", "adaptateurs_repetition", "ancrages", "divergence", "garde_activations", "go_id",
             "config_scellee")
CLES_CONFIG = CLES_RECETTE + CLES_PLAN
GARDES_ACTIVATIONS = ("trois_couches", "couche_15", "une_sur_dix")
COUCHES = (7, 15, 23)
N_CHEMIN = 8
SERIE_NU = lv.SERIE_NU
ETIQUETTE = "b5f-lecture-v1"
ETIQUETTE_REPETITION = "b5f-repetition-v1"
_ENTREE_TENUE = re.compile(r"(?P<nom>X-[0-9]{2})\.safetensors")
_ENTREE_APPRENTISSAGE = re.compile(r"(?P<nom>A[1-3]-(?:jumeau|saboteur|sur_saboteur))\.safetensors")
_ENTREE_EPISODES = re.compile(r"(?P<famille>A[1-3])-saboteur-evaluation\.jsonl")
_NOM_REPETITION = re.compile(r"R[1-9]-(?:saboteur|temoin)")
_NOM_ANCRE = re.compile(r"ancre-[A-Za-z0-9-]{1,40}")
_TACHE_FICHIER = re.compile(r"[A-Za-z0-9._-]+")
_SORTIE = re.compile(r"(?:lecture/(?:inventaire\.json|bilan-relecture\.json|textes-honnetes\.jsonl|produits\.json|"
                     r"intensites\.json|scores/[a-zA-Z0-9-]+-pli[01]\.json|"
                     r"jetons/[a-zA-Z0-9-]+-pli[01]/[A-Za-z0-9_-]+\.json)(?:\.sha256)?|"
                     r"poids/[a-zA-Z0-9-]+-pli[01]\.json(?:\.sha256)?|"
                     r"activations/[A-Za-z0-9_-]+/c(?:7|15|23)/[A-Za-z0-9._-]+__p[0-9]{1,3}\.npy|"
                     r"(?:garde-activations|inventaire-activations)\.json(?:\.sha256)?)")


def progres(**champs) -> None:
    """Journal d'avancement : étapes et comptes seulement (aucune grandeur d'un adaptateur, liste d'arrêt, point 7)."""
    for k, v in champs.items():
        if isinstance(v, float):
            raise GardeArret(f"journal : nombre à virgule {k} refusé (liste d'arrêt, point 7)")
    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={v}" for k, v in champs.items()), file=sys.stderr, flush=True)


# --- configuration -----------------------------------------------------------------------------------------------------

def exiger_config_lecture(config: dict, racine: Path) -> None:
    """Clés exactes (aucune clé libre, aucune clé de score) ; plan ; règle de garde des activations ; en mode réel, recette
    égale clé par clé à la configuration scellée de la course de confirmation (empreinte vérifiée)."""
    if not isinstance(config, dict):
        raise GardeArret("configuration : objet attendu")
    manquantes = [k for k in CLES_CONFIG if k not in config]
    inconnues = sorted(k for k in config if k not in CLES_CONFIG)
    if manquantes or inconnues:
        raise GardeArret(f"configuration : clés manquantes {manquantes}, clés inconnues {inconnues} (aucune clé libre)")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    if config["plan"] not in sv.PLANS:
        raise GardeArret(f"plan {config['plan']!r} : {sv.PLANS} attendu")
    if config["garde_activations"] not in GARDES_ACTIVATIONS:
        raise GardeArret(f"garde des activations {config['garde_activations']!r} : {GARDES_ACTIVATIONS} attendu")
    if not isinstance(config["divergence"], bool):
        raise GardeArret("divergence : vrai ou faux (coupe 1 du calendrier : faux)")
    if config["config_scellee"] != CONFIG_SCELLEE:
        raise GardeArret("config_scellee : chemin et empreinte de la configuration de la course de confirmation attendus")
    if tuple(int(c) for c in config["couches"]) != COUCHES and config["mode"] == "reel":
        raise GardeArret(f"couches {config['couches']} ≠ {COUCHES} (texte, « Métrique »)")
    if config["plan"] == "decisif":
        if not config["entrees"] or config["adaptateurs_repetition"]:
            raise GardeArret("plan décisif : dossier des entrées de lecture exigé, aucun adaptateur de répétition")
    else:
        if config["entrees"] or not config["adaptateurs_repetition"] or config["ancrages"]:
            raise GardeArret("plan de répétition : quatre adaptateurs existants (chemin, empreinte), ni entrées de lecture "
                             "ni points d'ancrage")
        for x in config["adaptateurs_repetition"]:
            if not (isinstance(x, dict) and set(x) == {"nom", "chemin", "sha256"} and _NOM_REPETITION.fullmatch(x["nom"])):
                raise GardeArret("adaptateur de répétition : {nom R<k>-saboteur|R<k>-temoin, chemin, sha256} attendu")
        noms = sorted(x["nom"] for x in config["adaptateurs_repetition"])
        if len(set(noms)) != len(noms):
            raise GardeArret("adaptateurs de répétition : nom en double")
    for x in config["ancrages"]:
        if not (isinstance(x, dict) and set(x) == {"nom", "chemin", "sha256"} and _NOM_ANCRE.fullmatch(x["nom"])):
            raise GardeArret("point d'ancrage : {nom ancre-…, chemin, sha256} attendu")
    for x in list(config["adaptateurs_repetition"]) + list(config["ancrages"]):
        exiger_adaptateur_existant(x)
    if config["mode"] == "reel":
        chemin = Path(racine) / CONFIG_SCELLEE["chemin"]
        if verifier(chemin) != CONFIG_SCELLEE["sha256"]:
            raise GardeArret("configuration scellée de la course de confirmation : empreinte différente (R11)")
        scellee = json.loads(chemin.read_text(encoding="utf-8"))
        ecarts = [k for k in CLES_RECETTE if config[k] != scellee.get(k)]
        if ecarts:
            raise GardeArret(f"recette différente de la configuration scellée : {ecarts}")
        if not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", str(config["go_id"])):
            raise GardeArret("accord de calcul illisible")


_CHEMIN_EXISTANT = re.compile(r"[A-Za-z0-9._-]+(?:/[A-Za-z0-9._-]+)*\.(?:pt|safetensors)")


def exiger_adaptateur_existant(x: dict) -> None:
    """Adaptateur existant (répétition générale ou point d'ancrage, point 18), donné par la session : empreinte sha256 de
    64 signes exigée (une empreinte absente ou illisible est refusée : aucun repli sur un compagnon) ; chemin relatif au
    dépôt, sans « .. », hors de `docs/`, `diag/`, `runs/` et de toute marche de la formation de ce plan."""
    if not isinstance(x.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", x["sha256"]):
        raise GardeArret(f"adaptateur existant {x.get('nom')!r} : empreinte sha256 absente ou illisible : refus")
    c = x.get("chemin")
    if (not isinstance(c, str) or not _CHEMIN_EXISTANT.fullmatch(c) or ".." in c.split("/")
            or c.split("/")[0] in ("docs", "diag", "runs") or "b5f-formation" in c):
        raise GardeArret(f"adaptateur existant {x.get('nom')!r} : chemin {c!r} refusé")


# --- registre propre ---------------------------------------------------------------------------------------------------

def exiger_registre_de_relecture(texte: str, config: dict, creation: str) -> dict:
    """Registre au commit de la marche. Plan décisif : `ENGAGEMENT-B5F` présente, d'instant antérieur à `creation`
    (liste d'arrêt, point 9), postérieure à `SORTIES-FORMATION-B5F` et à toute ligne de relance ; `CODE-LECTURE-B5F`,
    `EPREUVE-B5F` (même empreinte du programme, postérieure), `GO-LECTURE-B5F` égale à l'accord de la configuration ; ni
    `SCORES-B5F`, ni `OUVERTURE-B5F`, ni `LECTURE-B5F`. Répétition (point 18) : `CODE-LECTURE-B5F` et l'accord de calcul de
    la formation (`GO-FORMATION-B5F`, répétition comprise). Rend l'entropie, la relance et le commit du code de lecture."""
    lignes = en.lignes_du_registre(texte)
    s = re.fullmatch(rf"(?P<texte>prereg/[A-Za-z0-9._-]+\.md) ; sha256 (?P<sha>[0-9a-f]{{64}}) ; membres-apprentissage "
                     r"[23] ; piece (?:famille|instance)", lignes.get("SCELLEMENT-B5F", {}).get("contenu", ""))
    if s is None or s["texte"] != lv.TEXTE or s["sha"] != lv.TEXTE_SHA256:
        raise GardeArret("SCELLEMENT-B5F absente, illisible, ou d'un autre texte que ce plan : refus (R1)")
    cf = re.fullmatch(r"commit ([0-9a-f]{40}) ; entropie ([0-9]+)", lignes.get("CODE-FORMATION-B5F", {}).get("contenu", ""))
    if cf is None or not 0 < int(cf.group(2)) < 2 ** 128:
        raise GardeArret("CODE-FORMATION-B5F absente ou illisible (entropie des graines de la lecture)")
    cl = re.fullmatch(r"commit (?P<commit>[0-9a-f]{40}) ; lecture sha256 (?P<lecture>[0-9a-f]{64})",
                      lignes.get("CODE-LECTURE-B5F", {}).get("contenu", ""))
    if cl is None:
        raise GardeArret("CODE-LECTURE-B5F absente ou illisible : aucune relecture avant le code figé")
    if not lv.programme_sha256() == cl["lecture"]:
        raise GardeArret("programme de lecture d'une autre empreinte que CODE-LECTURE-B5F (liste d'arrêt, point 10)")
    relance = lv.relance_du_registre(texte)
    if config["plan"] == "repetition":
        if lignes.get("GO-FORMATION-B5F", {}).get("contenu") != config["go_id"]:
            raise GardeArret("répétition : accord GO-FORMATION-B5F (répétition comprise) ≠ accord de la configuration")
        return {"entropie": int(cf.group(2)), "relance": relance, "commit_lecture": cl["commit"], "engagement": None}
    en.verifier_engagement_avant_lecture(None, creation, lignes=lignes)
    for avant in ("SORTIES-FORMATION-B5F", "GO-RELANCE-FORMATION-B5F"):
        if avant == "SORTIES-FORMATION-B5F" and avant not in lignes:
            raise GardeArret("SORTIES-FORMATION-B5F absente : versement de la formation non inscrit")
        if avant in lignes and not lignes[avant]["instant"] < lignes["ENGAGEMENT-B5F"]["instant"]:
            raise GardeArret(f"ENGAGEMENT-B5F n'est pas postérieure à {avant} : refus, nœud")
    ep = re.fullmatch(r"passee ; lecture sha256 (?P<lecture>[0-9a-f]{64}) ; rapport sha256 [0-9a-f]{64}",
                      lignes.get("EPREUVE-B5F", {}).get("contenu", ""))
    if ep is None or ep["lecture"] != cl["lecture"] or not lignes["CODE-LECTURE-B5F"]["instant"] < lignes["EPREUVE-B5F"]["instant"]:
        raise GardeArret("épreuve à vérité plantée non passée pour ce programme (EPREUVE-B5F) : aucune relecture")
    if lignes.get("GO-LECTURE-B5F", {}).get("contenu") != config["go_id"]:
        raise GardeArret("accord de lecture GO-LECTURE-B5F absent ou ≠ accord de la configuration")
    for c in ("SCORES-B5F", "OUVERTURE-B5F", "LECTURE-B5F", "VERDICT-B5F"):
        if c in lignes:
            raise GardeArret(f"{c} déjà inscrite : la relecture ne se refait pas")
    return {"entropie": int(cf.group(2)), "relance": relance, "commit_lecture": cl["commit"],
            "engagement": lignes["ENGAGEMENT-B5F"]["contenu"].split()[1]}


# --- entrées de lecture, arbre de la session ------------------------------------------------------------------------

def exiger_entrees(dossier: Path) -> dict:
    """Point 7, deuxième tiret ; liste d'arrêt, point 8 : le dossier des entrées ne porte que les adaptateurs tenus à
    l'écart sous leurs noms opaques, les adaptateurs d'apprentissage étiquetés et les épisodes d'évaluation des saboteurs
    d'apprentissage, chacun scellé ; tout autre fichier (table, coût, journal de la formation) : refus, nœud."""
    dossier = Path(dossier)
    if not dossier.is_dir():
        raise GardeArret(f"entrées de lecture {dossier} absentes")
    tenus, app, episodes = {}, {}, {}
    for p in sorted(dossier.rglob("*")):
        if p.is_symlink() or (not p.is_file() and not p.is_dir()):
            raise GardeArret(f"entrées de lecture : {p.name} ni fichier ni dossier")
        if p.is_dir():
            raise GardeArret(f"entrées de lecture : dossier {p.relative_to(dossier)} non admis")
        rel = p.relative_to(dossier).as_posix()
        if rel.endswith(".sha256"):
            continue
        for motif, cible in ((_ENTREE_TENUE, tenus), (_ENTREE_APPRENTISSAGE, app)):
            m = motif.fullmatch(rel)
            if m:
                cible[m["nom"]] = p
                break
        else:
            m = _ENTREE_EPISODES.fullmatch(rel)
            if m is None:
                raise GardeArret(f"entrées de lecture : fichier non admis {rel} (liste d'arrêt, point 8) : refus, nœud")
            episodes[m["famille"]] = p
    en.exiger_entrees_de_lecture_propres(dossier, sorted(tenus), [tuple(n.split("-", 1)) for n in sorted(app)],
                                         [(f, "saboteur") for f in sorted(episodes)])
    for p in list(tenus.values()) + list(app.values()) + list(episodes.values()):
        verifier(p)
    if not tenus or not app:
        raise GardeArret("entrées de lecture : adaptateurs tenus à l'écart et d'apprentissage exigés")
    # point 7 : noms opaques donnés dans l'ordre (X-01 à X-NN, sans trou) ; fichiers réduits aux seuls tenseurs
    if sorted(tenus) != [f"X-{k:02d}" for k in range(1, len(tenus) + 1)]:
        raise GardeArret(f"entrées de lecture : noms opaques {sorted(tenus)[:3]}… non contigus depuis X-01 : refus")
    for p in list(tenus.values()) + list(app.values()):
        exiger_tenseurs_seuls(p)
    saboteurs = {n.split("-", 1)[0] for n in app if n.endswith("-saboteur")}
    if set(episodes) != saboteurs:
        raise GardeArret(f"épisodes d'évaluation {sorted(episodes)} ≠ saboteurs d'apprentissage {sorted(saboteurs)} : la "
                         "sonde du diagnostic ne se coupe pas")
    return {"tenus": tenus, "apprentissage": app, "episodes": episodes}


def exiger_tenseurs_seuls(chemin: Path) -> list[str]:
    """Point 7 (« fichiers réduits aux seuls tenseurs ») : l'en-tête du fichier `safetensors` ne porte aucune métadonnée
    (`__metadata__`), et seulement des matrices A et B d'adaptateur. Lu sans charger les tenseurs. Rend les clés."""
    chemin = Path(chemin)
    with open(chemin, "rb") as f:
        tete = f.read(8)
        if len(tete) != 8:
            raise GardeArret(f"{chemin.name} : en-tête safetensors illisible")
        n = int.from_bytes(tete, "little")
        if not 0 < n < 100_000_000:
            raise GardeArret(f"{chemin.name} : en-tête safetensors illisible")
        try:
            entete = json.loads(f.read(n).decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            raise GardeArret(f"{chemin.name} : en-tête safetensors illisible") from None
    if not isinstance(entete, dict) or "__metadata__" in entete:
        raise GardeArret(f"{chemin.name} : métadonnées dans le fichier (seuls les tenseurs sont admis, point 7) : refus")
    cles = sorted(entete)
    if not cles or any(not k.endswith((".A", ".B")) for k in cles):
        raise GardeArret(f"{chemin.name} : autre chose que des matrices A et B d'adaptateur : refus")
    return cles


def exiger_arbre_de_lecture_propre(racine: Path, dossiers, empreinte_engagement: str | None, sorties: Path | None) -> dict:
    """Liste d'arrêt, point 8 : dans l'arbre de la session de lecture (dépôt et entrées), ni la table des étiquettes (par
    l'empreinte engagée ou par sa forme), ni une ligne de la branche de la formation qui porte une famille tenue à l'écart,
    ni une marche de formation sous `donnees/`, ni une référence git à la branche de la formation : refus, nœud. Les
    dossiers `.git`, `.venv` et les sorties de la marche ne sont pas parcourus."""
    racine = Path(racine)
    vus = 0
    exclus = {(racine / ".git").resolve(), (racine / ".venv").resolve()}
    if sorties is not None:
        exclus.add(Path(sorties).resolve())
    for base in [racine] + [Path(d) for d in dossiers]:
        for p in sorted(base.rglob("*")):
            if any(e == p.resolve() or e in p.resolve().parents for e in exclus):
                continue
            if p.is_dir() and re.fullmatch(r"[0-9]{8}-[0-9]{6}-b5f-formation-[1-7](?:-x1)?", p.name):
                raise GardeArret(f"marche de la formation présente dans l'arbre de lecture ({p}) : refus, nœud")
            if not p.is_file():
                continue
            vus += 1
            if empreinte_engagement is not None and empreinte(p) == empreinte_engagement:
                raise GardeArret(f"table des étiquettes présente dans l'arbre de lecture ({p}) : refus, nœud")
            if p.suffix in (".json", ".jsonl"):
                texte = p.read_text(encoding="utf-8", errors="replace")
                morceaux = [texte] if p.suffix == ".json" else [x for x in texte.split("\n") if x.strip()]
                for mo in morceaux:
                    try:
                        x = json.loads(mo)
                    except ValueError:
                        continue
                    if lv._ressemble_a_une_table(x):
                        raise GardeArret(f"table des étiquettes présente dans l'arbre de lecture ({p}) : refus, nœud")
                    if lv._porte_un_cout_tenu(x):
                        raise GardeArret(f"ligne de la formation d'une famille tenue à l'écart dans l'arbre de lecture "
                                         f"({p}) : refus, nœud")
    if (racine / ".git").exists():
        r = subprocess.run(["git", "-C", str(racine), "for-each-ref", "--format=%(refname)"], capture_output=True, text=True)
        if r.returncode != 0:
            raise GardeArret("références git illisibles")
        if any("barreau5-familles-jumelles-v1-formation" in x for x in r.stdout.splitlines()):
            raise GardeArret("branche de la formation présente dans le dépôt de la session de lecture : refus, nœud")
    return {"fichiers_parcourus": vus}


# --- adaptateurs ---------------------------------------------------------------------------------------------------------

def charger_etat_fichier(chemin: Path, sha256: str | None, formes: dict) -> dict:
    """État d'un adaptateur, à son empreinte (compagnon scellé, ou empreinte donnée par la configuration pour un adaptateur
    existant) : `.safetensors` (entrées de lecture) ou `.pt` (adaptateurs existants) ; seulement des matrices A et B, aux
    clés et formes de l'état injecté."""
    chemin = Path(chemin)
    if sha256 is None:
        verifier(chemin)
    elif empreinte(chemin) != sha256:
        raise GardeArret(f"{chemin} : empreinte ≠ celle citée (liste d'arrêt, point 1)")
    if chemin.suffix == ".safetensors":
        from safetensors.torch import load_file
        etat = dict(load_file(str(chemin)))
    elif chemin.suffix == ".pt":
        etat = torch.load(chemin, map_location="cpu", weights_only=True)
    else:
        raise GardeArret(f"{chemin} : format d'adaptateur inconnu")
    if (not isinstance(etat, dict) or {k: tuple(v.shape) for k, v in etat.items()} != {k: tuple(v) for k, v in formes.items()}):
        raise GardeArret(f"{chemin} : clés ou formes différentes de celles de l'état injecté")
    return etat


# --- relecture forcée ----------------------------------------------------------------------------------------------------

def rejouer(modele, fmt, env, ids_actions: list, textes: list, couches) -> tuple[list, list]:
    """Rejeu en forçage d'un épisode (même reconstruction que `harnais.episode.jouer_episodes` et
    `t07bbis.etat_impose_v1.rejouer_episode` : ouverture au pas 0, puis tour, clôture après chaque action ; observation de
    l'environnement honnête ; journal des textes décodés) ; texte décodé des identifiants égal au texte écrit, sinon arrêt ;
    une passe unique (`harnais.activations.passe_unique`) ; empan noté [début, `t06.lanceur._fin_notee`[ (même empan que la
    chaîne) ; actions d'empan vide écartées. Rend ([(pas, début, fin, {couche : activations})], identifiants)."""
    ids, journal, debut, actions = [], [], None, []
    if len(ids_actions) != env.T or len(textes) != env.T:
        raise GardeArret(f"épisode de {len(ids_actions)} actions pour {env.T} pas")
    for pas, (nv, texte) in enumerate(zip(ids_actions, textes)):
        obs = env.observation(0, pas, journal)
        if pas == 0:
            debut = (env.consigne_privee(0), obs)
            ctx = fmt.ouverture(*debut)
        else:
            ctx = ids + fmt.tour(debut, obs)
        nv = [int(x) for x in nv]
        decode = fmt.tok.decode(nv, skip_special_tokens=True)
        if decode != texte:
            raise GardeArret(f"relecture : action {pas} : texte décodé des identifiants ≠ texte écrit : arrêt")
        actions.append(Action(0, pas, len(ctx), len(ctx) + len(nv), nv, decode))
        ids = ctx + nv + fmt.cloture(debut, nv)
        journal.append((0, pas, decode))
    acts = passe_unique(modele, ids, couches)
    sortie = []
    for a in actions:
        d, f = a.debut, _fin_notee(a, fmt)
        if f > d:
            sortie.append((a.pas, d, f, {int(k): acts[int(k)][d:f] for k in couches}))
    return sortie, ids


def logits_aux_positions(modele, ids: list, positions) -> torch.Tensor:
    """Logits (simple précision) aux positions données, une passe sans cache ni crochet."""
    appareil = next(modele.parameters()).device
    with torch.no_grad():
        sortie = modele(input_ids=torch.tensor([list(ids)], device=appareil), use_cache=False)
    return sortie.logits[0, torch.as_tensor(list(positions), device=appareil)].to(torch.float32)


def divergence_par_jeton(l0: torch.Tensor, l1: torch.Tensor) -> np.ndarray:
    """KL(p_0 ‖ p_1) à chaque position : loi du jeton suivant du modèle nu (p_0) à celle du modèle adapté (p_1)."""
    lp0, lp1 = torch.log_softmax(l0, dim=-1), torch.log_softmax(l1, dim=-1)
    return (lp0.exp() * (lp0 - lp1)).sum(dim=-1).to("cpu", torch.float64).numpy()


def charger_et_controler(modele, nom: str, etat: dict, ids_controle: list, logits_base) -> dict:
    """Point 8 (c) ; liste d'arrêt, point 3 : l'adaptateur chargé à dose 0 rend les logits du contexte de contrôle égaux
    au bit près à ceux du modèle nu, et à dose 1 des logits différents (artefact), par `t06.identite.controle_identite`
    (gelé) ; puis dose 1 et état de phase vérifié (dose lue sur chaque module, empreinte des adaptateurs chargés). Rend le
    contrôle et l'empreinte ; le modèle est laissé à la dose 1."""
    lo.charger_etat(modele, etat)
    identite = controle_identite(modele, ids_controle, logits_base, {nom: lo.etat_lora(modele)})[nom]
    lo.fixer_dose(modele, 1.0)
    exiger_etat_de_phase(modele, 1.0, identite["empreinte"], f"début de la série {nom}")
    return identite


def _egaux_au_bit(a, b) -> bool:
    x, y = demi(a), demi(b)
    return x.shape == y.shape and bool(np.array_equal(x.view(np.uint16), y.view(np.uint16)))


def eprouver_chemin(modele, fmt, envs: dict, textes: dict, origine: dict, chemin_t: list, couches, temoin: str,
                    etat_temoin: dict) -> dict:
    """Point 8 (b) ; liste d'arrêt, point 11 : les épisodes du chemin relus par le chemin forcé à l'état « modèle nu »
    (dose 0) égaux au bit près, en demi-précision, aux activations d'origine (cas sain) ; relus sous l'adaptateur `temoin`
    à la dose 1, différents (artefact). Sinon arrêt avant toute notation. Laisse le modèle à la dose 0."""
    lo.fixer_dose(modele, 0.0)
    egales = differentes = 0
    for t in chemin_t:
        spans, _ = rejouer(modele, fmt, envs[t], textes[t][0], textes[t][1], couches)
        for pas, d, f, acts in spans:
            for k in couches:
                if _egaux_au_bit(origine[t][k][d:f], acts[k]):
                    egales += 1
                else:
                    differentes += 1
    if differentes or not egales:
        raise GardeArret(f"chemin de relecture en échec : {differentes} tableaux ≠ origine au bit près (cas sain) : arrêt "
                         "avant toute notation (liste d'arrêt, point 11)")
    lo.charger_etat(modele, etat_temoin)
    lo.fixer_dose(modele, 1.0)
    art = 0
    try:
        for t in chemin_t:
            spans, _ = rejouer(modele, fmt, envs[t], textes[t][0], textes[t][1], couches)
            for pas, d, f, acts in spans:
                art += sum(0 if _egaux_au_bit(origine[t][k][d:f], acts[k]) else 1 for k in couches)
    finally:
        lo.fixer_dose(modele, 0.0)
    if not art:
        raise GardeArret("chemin de relecture : artefact (sous un adaptateur, dose 1) égal à l'origine : arrêt avant toute "
                         "notation (liste d'arrêt, point 11)")
    return {"episodes": list(chemin_t), "cas_sain": {"egales": egales, "differentes": differentes},
            "artefact": {"adaptateur": temoin, "differents": art}}


def episodes_propres(chemin: Path, famille: str, relance, par_id: dict, T: int) -> dict:
    """Épisodes d'évaluation du saboteur d'une famille d'apprentissage (point 8 (d)) : chaque ligne est du saboteur de
    cette famille, de la copie lue (règle de la relance : `-x1` si l'instance est relancée, jamais l'autre copie ; retirage
    `-r1` admis), sur une tâche d'évaluation ; chaque épisode porte les pas 0 à T − 1. Rend {tâche : {pas : ligne}}."""
    par_tache = {}
    for x in lv._lire_jsonl(chemin, f"épisodes d'évaluation de {famille}"):
        if x.get("membre") != "saboteur":
            raise GardeArret(f"{chemin} : ligne d'un autre membre que le saboteur")
        if re.sub(r"(-x1)?(-r1)?$", "", str(x.get("famille", ""))) != famille:
            raise GardeArret(f"{chemin} : ligne de la famille {x.get('famille')}, {famille} attendue")
        lv.exiger_copie_lue(famille, str(x["famille"]), relance)
        if x["tache"] not in par_id:
            raise GardeArret(f"{chemin} : tâche {x['tache']} hors des tâches d'évaluation")
        par_tache.setdefault(x["tache"], {})[int(x["pas"])] = x
    for t, pas in par_tache.items():
        if sorted(pas) != list(range(T)):
            raise GardeArret(f"{chemin} : épisode {t} : pas {sorted(pas)}, 0 à {T - 1} attendus")
    if not par_tache:
        raise GardeArret(f"{chemin} : aucun épisode")
    return par_tache


def cle_fichier(cle: str) -> str:
    tache, pas = lv.decomposer_cle(cle)
    return f"{tache}__p{pas}"


class Lecteur:
    """Activations gardées en demi-précision (`activations/<série>/c<couche>/<tâche>__p<pas>.npy`), lues en double
    précision (« Métrique »)."""

    def __init__(self, dossier: Path):
        self.dossier = Path(dossier)

    def __call__(self, serie: str, couche: int, cle: str) -> np.ndarray:
        p = self.dossier / serie / f"c{int(couche)}" / f"{cle_fichier(cle)}.npy"
        a = np.load(p, allow_pickle=False)
        if a.dtype != np.float16:
            raise GardeArret(f"{p} : demi-précision attendue")
        return a.astype(np.float64)


# --- marche ------------------------------------------------------------------------------------------------------------

def charger_modele(config: dict, graine_jouet: int):
    """Mode réel : modèle et format de la configuration scellée (`charger_modele_et_format`). Mode jouet : le modèle par
    caractères du harnais, à 24 couches (largeur 32), pour que les couches 7, 15 et 23 du texte existent."""
    from ..environnements.lancer_pilote_a import charger_modele_et_format
    from ..harnais.formats import FormatChat
    from ..harnais.modeles import modele_jouet, tokeniseur_caracteres_chat
    if config["mode"] == "reel":
        return charger_modele_et_format(config["agent"], "reel", graine_jouet)
    tok = tokeniseur_caracteres_chat()
    m = modele_jouet(graine_jouet, len(tok), couches=24, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    return m, FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})


def cles_des_graines(taches_ids, definitions) -> list[str]:
    cles = [f"b5f/lecture/honnete/tache/{t}" for t in taches_ids]
    cles += ["b5f/lecture/plis", "b5f/lecture/ordre", "b5f/lecture/chemin", "b5f/lecture/injection", "b5f/modele-jouet",
             "b5f/tirages/garde-activations"]
    return cles + sv.cles_des_graines(definitions)


def _definitions_prevues(config: dict, noms: list[str]) -> list:
    return sv.plan_des_sondes(noms, config["plan"])


def executer(config: dict, racine: Path, run_id: str, prereg: str | None = None, entropie: int | None = None,
             registre_texte: str | None = None, autoriser_depot_sale: bool = False, jouer=None) -> dict:
    """Marche de lecture. Mode réel : registre propre au commit de la marche (fichier du dépôt extrait), texte scellé,
    code au commit ; aucun générateur scripté. Mode jouet : entropie donnée ; registre fabriqué facultatif (mêmes gardes,
    hors le code au commit) ; générateur scripté permis (`jouer`)."""
    racine = Path(racine)
    exiger_config_lecture(config, racine)
    creation = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reg = None
    if config["mode"] == "reel":
        if prereg is None or jouer is not None or registre_texte is not None:
            raise GardeArret("mode réel : texte scellé exigé, registre du dépôt, aucun générateur scripté (R1)")
        if str(prereg) != lv.TEXTE:
            raise GardeArret(f"texte {prereg} ≠ {lv.TEXTE}")
        reg = exiger_registre_de_relecture((racine / en.REGISTRE_PROPRE).read_text(encoding="utf-8"), config, creation)
        lv.exiger_code_de_lecture_au_commit(racine, reg["commit_lecture"])
        entropie = reg["entropie"]
    else:
        if entropie is None:
            raise GardeArret("mode jouet : entropie donnée exigée")
        if registre_texte is not None:
            reg = exiger_registre_de_relecture(registre_texte, config, creation)
            if reg["entropie"] != entropie:
                raise GardeArret("mode jouet : entropie ≠ celle du registre fabriqué")
    relance = reg["relance"] if reg else None
    taches = charger_taches(Path(racine) / config["taches_evaluation"]["chemin"])
    if verifier(Path(racine) / config["taches_evaluation"]["chemin"]) != config["taches_evaluation"]["sha256"]:
        raise GardeArret("tâches d'évaluation : empreinte différente de celle citée (R11)")
    ids_taches = [t["identifiant"] for t in taches]
    for t in ids_taches:
        if not _TACHE_FICHIER.fullmatch(str(t)):
            raise GardeArret(f"identifiant de tâche {t!r} hors de [A-Za-z0-9._-]")
    sorties = racine / "donnees" / run_id
    if config["plan"] == "decisif":
        entrees = exiger_entrees(racine / config["entrees"])
        sources = {**{n: (p, None) for n, p in entrees["tenus"].items()},
                   **{n: (p, None) for n, p in entrees["apprentissage"].items()}}
        arbre = exiger_arbre_de_lecture_propre(racine, [racine / config["entrees"]], reg["engagement"] if reg else None,
                                               sorties)
    else:
        entrees = {"tenus": {}, "apprentissage": {}, "episodes": {}}
        sources = {x["nom"]: (racine / x["chemin"], x["sha256"]) for x in config["adaptateurs_repetition"]}
        arbre = {"fichiers_parcourus": 0}
    ancres = {x["nom"]: (racine / x["chemin"], x["sha256"]) for x in config["ancrages"]}
    noms_plan = sorted(sources)
    definitions = _definitions_prevues(config, noms_plan)
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles_des_graines(ids_taches, definitions),
                                          entropie=entropie, decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    etat = {"etape": "début"}
    debut = time.perf_counter()
    try:
        return _executer(config, racine, run_id, chemin_m, manifeste, taches, entrees, sources, ancres, definitions,
                         relance, sorties, arbre, etat, debut, jouer)
    except Exception as e:
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _graine(g: dict, cle: str) -> int:
    return sv.graine_entiere(g[cle])


def _executer(config, racine, run_id, chemin_m, manifeste, taches, entrees, sources, ancres, definitions, relance,
              sorties, arbre, etat, debut, jouer) -> dict:
    from ..environnements.invites import charger_invite
    from ..environnements.lancer_pilote_a import conversation_de_controle
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import exiger_memoire_vive, noyau
    from .formation_v1 import jouer_sans_activations

    g = manifeste["graines"]
    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    couches = [int(c) for c in config["couches"]]
    c15 = 15 if 15 in couches else couches[len(couches) // 2]
    T = int(config["T"])
    etat["etape"] = "chargement"
    if reel:
        exiger_memoire_vive(config["memoire_vive_min_go"])
    reglages = regler_determinisme(config["fils"], appareil)
    modele, fmt = charger_modele(config, _graine(g, "b5f/modele-jouet"))
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    consigne_c, observations_c, _ = conversation_de_controle("agent", None)
    ids_controle = fmt.ouverture(consigne_c, observations_c[0])
    logits_base = logits_de_controle(modele, ids_controle)
    a = config["adaptateur"]
    lo.injecter(modele, a["rang"], float(a["alpha"]), _graine(g, "b5f/lecture/injection"), tuple(a["cibles"]))
    if a["precision"] == "float32":
        dt.adaptateurs_en_simple_precision(modele)
    lo.fixer_dose(modele, 0.0)
    if not torch.equal(logits_de_controle(modele, ids_controle), logits_base):
        raise GardeArret("après l'injection, à dose 0 : logits ≠ ceux du modèle nu : arrêt")
    formes = {k: tuple(v.shape) for k, v in lo.etat_lora(modele).items()}
    etats = {n: charger_etat_fichier(p, s, formes) for n, (p, s) in sorted({**sources, **ancres}.items())}
    guide = charger_invite("H1-classification")
    par_id = {t["identifiant"]: t for t in taches}
    ids_taches = [t["identifiant"] for t in taches]
    plis = lv.partition_des_plis(ids_taches, int(manifeste["graines"]["b5f/lecture/plis"]["entropie"]))
    dossier_ferme, dossier_act = sorties / "lecture", sorties / "activations"
    dossier_ferme.mkdir(parents=True, exist_ok=False)
    ecrire_resultat(racine, chemin_m, "mise-en-place", {"reglages": reglages, "adaptateurs": sorted(etats),
                                                        "sondes": [d.nom for d in definitions], "plis": plis,
                                                        "arbre": arbre, "relance": relance, "plan": config["plan"]})
    with noyau(config["noyau_attention"]):
        # (a) textes honnêtes communs, sur le modèle nu
        etat["etape"] = "textes honnêtes"
        envs = {t: environnement("honnete", tache_de(par_id[t]), T, guide, {}) for t in ids_taches}
        graines_act = {t: graines_des_actions(generateur(g[f"b5f/lecture/honnete/tache/{t}"]), 1, T) for t in ids_taches}
        episodes = {}
        for k in range(0, len(ids_taches), int(config["lot"])):
            morceau = ids_taches[k:k + int(config["lot"])]
            ev = [envs[t] for t in morceau]
            gs = [graines_act[t] for t in morceau]
            eps = (jouer(fmt, ev, [f"honnete/{t}" for t in morceau], T, gs) if jouer is not None
                   else jouer_sans_activations(modele, fmt, ev, [f"honnete/{t}" for t in morceau], T, gs,
                                               config["max_nouveaux"], config["temperature"], pad))
            for t, ep in zip(morceau, eps):
                episodes[t] = ep.transcriptions[0]
            progres(etape="textes honnetes", episodes=len(episodes))
        rng_chemin = generateur(g["b5f/lecture/chemin"])
        chemin_t = sorted(ids_taches[int(i)] for i in rng_chemin.choice(len(ids_taches), size=min(N_CHEMIN, len(ids_taches)),
                                                                           replace=False))
        origine = {t: passe_unique(modele, episodes[t].ids, couches) for t in chemin_t}
        lignes_h = []
        for t in ids_taches:
            for act in episodes[t].actions:
                lignes_h.append({"tache": t, "pas": act.pas, "texte": act.texte, "ids": [int(x) for x in act.ids],
                                 **cout_action(act.texte)})
        p_h = dossier_ferme / "textes-honnetes.jsonl"
        with open(p_h, "w", encoding="utf-8") as f:
            for x in lignes_h:
                f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
        sceller(p_h)
        textes = {t: ([list(x.ids) for x in episodes[t].actions], [x.texte for x in episodes[t].actions]) for t in ids_taches}

        def relire(serie: str, a_ecrire: bool, avec_logits: bool, reference=None):
            """Série sur les textes honnêtes communs, à l'état courant du modèle ; rend activations (demi-précision) par
            clé, et divergence par action si demandée (le modèle passe à la dose 0 pour les logits du modèle nu, puis
            revient à la dose 1)."""
            ecr = ActivationsDemi(dossier_act / serie, couches) if a_ecrire else None
            acts_serie, div = {}, {}
            for t in ids_taches:
                exiger_sans_signal(f"la relecture de {serie}/{t}")
                spans, ids = rejouer(modele, fmt, envs[t], textes[t][0], textes[t][1], couches)
                if avec_logits:
                    pos = [p for _, d, f, _ in spans for p in range(d, f)]
                    l1 = logits_aux_positions(modele, ids, pos)
                    lo.fixer_dose(modele, 0.0)
                    l0 = logits_aux_positions(modele, ids, pos)
                    lo.fixer_dose(modele, 1.0)
                    kl = divergence_par_jeton(l0, l1)
                    i = 0
                    for pas, d, f, _ in spans:
                        div[lv.cle_action(t, pas)] = float(np.mean(kl[i:i + (f - d)]))
                        i += f - d
                for pas, d, f, acts in spans:
                    cle = lv.cle_action(t, pas)
                    a16 = {k: demi(acts[k]) for k in couches}
                    if ecr is not None:
                        ecr.ecrire(cle_fichier(cle), a16)
                    acts_serie[cle] = a16
            return acts_serie, div

        # série du modèle nu, relue par le même chemin forcé (dose 0)
        etat["etape"] = "série du modèle nu"
        lo.fixer_dose(modele, 0.0)
        nu, _ = relire(SERIE_NU, True, False)
        progres(etape="serie nu", actions=len(nu))
        # (b) chemin éprouvé : cas sain (modèle nu, au bit près) et artefact (sous un adaptateur d'apprentissage)
        etat["etape"] = "chemin éprouvé"
        temoin = sorted(n for n in sources if not n.startswith("X-"))[0]
        chemin = eprouver_chemin(modele, fmt, envs, textes, origine, chemin_t, couches, temoin, etats[temoin])
        ecrire_resultat(racine, chemin_m, "chemin", chemin)
        # (c) chaque adaptateur, dans un ordre tiré par graine
        noms = sorted(etats)
        ordre = [noms[int(i)] for i in generateur(g["b5f/lecture/ordre"]).permutation(len(noms))]
        intensites, deplacements, identites = {}, {}, {}
        cles = {SERIE_NU: sorted(nu)}
        for n_ad, nom in enumerate(ordre):
            etat["etape"] = f"série {nom}"
            identite = charger_et_controler(modele, nom, etats[nom], ids_controle, logits_base)
            emp = identite["empreinte"]
            acts_serie, div = relire(nom, True, bool(config["divergence"]))
            exiger_etat_de_phase(modele, 1.0, emp, f"fin de la série {nom}")
            lo.fixer_dose(modele, 0.0)
            if sorted(acts_serie) != cles[SERIE_NU]:
                raise GardeArret(f"série {nom} : actions notées ≠ celles du modèle nu")
            normes = {k: [] for k in couches}
            somme, jetons = None, 0
            for cle in cles[SERIE_NU]:
                for k in couches:
                    x1, x0 = acts_serie[cle][k].astype(np.float64), nu[cle][k].astype(np.float64)
                    normes[k].append(float(np.mean(ecarts_par_jeton(x1, x0))))
                    if k == c15:
                        s = (x1 - x0).sum(axis=0)
                        somme = s if somme is None else somme + s
                        jetons += x1.shape[0]
            deplacements[nom] = somme / jetons
            intensites[nom] = {"divergence": float(np.median(list(div.values()))) if div else None,
                               "normes": {str(k): float(np.median(v)) for k, v in normes.items()},
                               "empreinte": emp, "identite": identite, "actions": len(cles[SERIE_NU])}
            identites[nom] = {"dose_0_identique": identite["dose_0_identique"], "dose_1_differente": identite["dose_1_differente"]}
            cles[nom] = cles[SERIE_NU]
            progres(etape="serie", adaptateur=f"{n_ad + 1}/{len(ordre)}")
        # (d) épisodes d'évaluation des saboteurs d'apprentissage, sous leur propre adaptateur
        for fam, p in sorted(entrees["episodes"].items()):
            etat["etape"] = f"série propre de {fam}"
            nom = f"{fam}-saboteur"
            par_tache = episodes_propres(p, fam, relance, par_id, T)
            emp = charger_et_controler(modele, nom, etats[nom], ids_controle, logits_base)["empreinte"]
            ecr = ActivationsDemi(dossier_act / f"propre-{nom}", couches)
            cles_p = []
            for t in sorted(par_tache, key=str):
                env = environnement("honnete", tache_de(par_id[t]), T, guide, {})
                spans, _ = rejouer(modele, fmt, env, [par_tache[t][q]["ids"] for q in range(T)],
                                   [par_tache[t][q]["texte"] for q in range(T)], couches)
                for pas, d, f, acts in spans:
                    cle = lv.cle_action(t, pas)
                    ecr.ecrire(cle_fichier(cle), {k: demi(acts[k]) for k in couches})
                    cles_p.append(cle)
            exiger_etat_de_phase(modele, 1.0, emp, f"fin de la série propre de {fam}")
            lo.fixer_dose(modele, 0.0)
            cles[f"propre-{nom}"] = cles_p
        # produits P de toutes les paires et poussées le long de ĝ (adaptateurs du plan ; ni points d'ancrage ni étiquette)
        etat["etape"] = "produits"
        dep_plan = {n: deplacements[n] for n in sources}
        if config["plan"] == "decisif":
            saboteurs = sorted(n for n in dep_plan if re.fullmatch(r"A[1-3]-saboteur", n))
        else:
            saboteurs = sorted(n for n in dep_plan if n.endswith("-saboteur"))
        prod = lv.produits_et_poussees(dep_plan, saboteurs)
        p_prod = dossier_ferme / "produits.json"
        p_prod.write_text(json.dumps({"format": lv.FORMAT_PRODUITS, "couche": c15,
                                      "deplacements": {n: [float(v) for v in d] for n, d in sorted(dep_plan.items())},
                                      "saboteurs_apprentissage": saboteurs,
                                      "direction": [float(v) for v in prod["direction"]], "produits": prod["produits"],
                                      "poussees": prod["poussees"]}, sort_keys=True), encoding="utf-8")
        sceller(p_prod)
        p_int = dossier_ferme / "intensites.json"
        p_int.write_text(json.dumps({"format": lv.FORMAT_INTENSITES, "adaptateurs": intensites}, sort_keys=True),
                         encoding="utf-8")
        sceller(p_int)
        # sondes et notation fermée
        etat["etape"] = "sondes"
        notation = sv.apprendre_et_noter(definitions, Lecteur(dossier_act), cles, plis, g, dossier_ferme,
                                         sorties / "poids", appareil)
        progres(etape="sondes", notees=len(notation["fichiers"]))
    # bilan, inventaire de l'arbre de lecture, garde des activations
    etat["etape"] = "inventaires"
    coupes = [] if config["divergence"] else ["divergence des sorties"]
    if config["plan"] == "decisif" and "comparaison" not in notation["sondes"]:
        coupes.append("sonde de comparaison")
    bilan = {"format": lv.FORMAT_BILAN, "run_id": run_id, "plan": config["plan"], "taches": ids_taches,
             "plis": [list(p) for p in plis], "adaptateurs": sorted(sources), "ancrages": sorted(ancres),
             "series": sorted(cles), "sondes": notation["sondes"], "coupes": coupes,
             "chemin": {"episodes": len(chemin_t), "cas_sain_egales": chemin["cas_sain"]["egales"]},
             "identites": identites, "statuts_des_sondes": notation["statuts"],
             "controle_carte_processeur": notation["controle_carte_processeur"],
             "textes_honnetes": {"episodes": len(ids_taches), "actions": len(lignes_h)}}
    p_bilan = dossier_ferme / "bilan-relecture.json"
    p_bilan.write_text(json.dumps(bilan, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    sceller(p_bilan)
    inventaire = lv.ecrire_inventaire(dossier_ferme, run_id)
    garde = garde_des_activations(dossier_act, sorties, config["garde_activations"], g)
    exiger_sorties_lecture_permises(sorties)
    resume = {"inventaire_sha256": inventaire, "fichiers_fermes": len(lv._fichiers(dossier_ferme)),
              "adaptateurs": len(sources), "ancrages": len(ancres), "series": len(cles),
              "sondes": notation["statuts"], "garde_activations": garde,
              "duree_s": round(time.perf_counter() - debut, 1)}
    ecrire_resultat(racine, chemin_m, "resume", resume)
    progres(etape="fin", inventaire=inventaire)
    return resume


def garde_des_activations(dossier_act: Path, sorties: Path, regle: str, g: dict) -> dict:
    """« Données gardées » : inventaire (noms, tailles, empreintes) de toutes les activations écrites, et la liste de
    celles que la règle garde : `trois_couches` (tout), `couche_15` (couche 15 de toutes les séries), `une_sur_dix` (une
    action sur dix, tirée par graine `b5f/tirages/garde-activations`, couche 15). Le reste est détruit avec l'instance, après
    cet inventaire (rien n'est supprimé ici)."""
    tous = sorted(p for p in Path(dossier_act).rglob("*.npy"))
    inv = [{"chemin": p.relative_to(sorties).as_posix(), "octets": p.stat().st_size, "sha256": empreinte(p)} for p in tous]
    if regle == "trois_couches":
        gardes = [x["chemin"] for x in inv]
    else:
        c15 = [x["chemin"] for x in inv if "/c15/" in x["chemin"]]
        if regle == "couche_15":
            gardes = c15
        else:
            noms = sorted({c.rsplit("/", 1)[1] for c in c15})
            rng = generateur(g["b5f/tirages/garde-activations"])
            choisies = {noms[int(i)] for i in rng.choice(len(noms), size=max(1, len(noms) // 10), replace=False)} if noms else set()
            gardes = [c for c in c15 if c.rsplit("/", 1)[1] in choisies]
    p_inv = Path(sorties) / "inventaire-activations.json"
    p_inv.write_text(json.dumps({"fichiers": inv}, sort_keys=True), encoding="utf-8")
    p_g = Path(sorties) / "garde-activations.json"
    p_g.write_text(json.dumps({"regle": regle, "fichiers": gardes}, sort_keys=True), encoding="utf-8")
    return {"regle": regle, "ecrites": len(inv), "gardees": len(gardes), "inventaire_sha256": sceller(p_inv),
            "liste_sha256": sceller(p_g)}


def exiger_sorties_lecture_permises(sorties: Path) -> None:
    """Liste blanche des sorties d'une marche de lecture sous `donnees/<marche>/` : arbre de lecture fermé, poids des
    sondes, activations, inventaires ; tout autre fichier : refus."""
    for p in sorted(Path(sorties).rglob("*")):
        if p.is_symlink():
            raise GardeArret(f"sortie {p} : lien refusé")
        if p.is_file():
            rel = p.relative_to(sorties).as_posix()
            if _SORTIE.fullmatch(rel) is None:
                raise GardeArret(f"sortie non admise {rel} (liste blanche de la lecture)")


def config_lecture(racine: Path, go_id: str, plan: str, entrees: str | None, divergence: bool, garde: str,
                   ancrages=(), adaptateurs_repetition=()) -> dict:
    """Configuration réelle d'une marche de lecture : recette lue dans la configuration scellée de la course de
    confirmation (empreinte vérifiée), plan, accord, entrées, coupes (divergence) et règle de garde des activations.
    Passe `exiger_config_lecture`."""
    chemin = Path(racine) / CONFIG_SCELLEE["chemin"]
    if verifier(chemin) != CONFIG_SCELLEE["sha256"]:
        raise GardeArret("configuration scellée de la course de confirmation : empreinte différente (R11)")
    scellee = json.loads(chemin.read_text(encoding="utf-8"))
    config = {k: scellee[k] for k in CLES_RECETTE}
    config.update({"mode": "reel", "plan": plan, "entrees": entrees, "adaptateurs_repetition": list(adaptateurs_repetition),
                   "ancrages": list(ancrages), "divergence": bool(divergence), "garde_activations": garde, "go_id": go_id,
                   "config_scellee": dict(CONFIG_SCELLEE)})
    exiger_config_lecture(config, racine)
    return config


def verifier_avant_creation(racine: Path, commit: str, config: dict) -> dict:
    """Côté session, avant la création de l'instance de lecture : registre propre au commit de la marche (mêmes gardes que
    la marche, instant de création = maintenant : `ENGAGEMENT-B5F` antérieure), code du commit égal à celui de
    `CODE-LECTURE-B5F`, arbre de travail de la session identique (« le jour L » : la relecture ne part jamais avant)."""
    if not re.fullmatch(r"[0-9a-f]{40}", str(commit)):
        raise GardeArret("commit (40 signes) attendu")
    vu = subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{en.REGISTRE_PROPRE}"], capture_output=True, text=True)
    if vu.returncode != 0:
        raise GardeArret(f"registre propre absent du commit {commit[:12]}")
    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reg = exiger_registre_de_relecture(vu.stdout, config, maintenant)
    lv.exiger_code_de_lecture_au_commit(racine, reg["commit_lecture"])
    a = subprocess.run(["git", "-C", str(racine), "merge-base", "--is-ancestor", reg["commit_lecture"], commit],
                       capture_output=True)
    if a.returncode != 0:
        raise GardeArret("le commit de la marche ne descend pas du commit de CODE-LECTURE-B5F")
    chemins = [x["chemin"] for x in list(config.get("ancrages") or []) + list(config.get("adaptateurs_repetition") or [])]
    arbre = exiger_arbre_extrait_propre(racine, commit, reg["engagement"], chemins)
    return {"commit": commit, "commit_lecture": reg["commit_lecture"], "relance": reg["relance"], "verifie_le": maintenant,
            "arbre_extrait": arbre}


def motifs_de_l_amorce(texte: str) -> list[str]:
    """Motifs de l'extraction partielle de l'amorce (bloc `# >>> motifs` … `# <<< motifs`, variable `MOTIFS`)."""
    m = re.search(r"# >>> motifs[^\n]*\nMOTIFS='(?P<corps>[^']*)'\n# <<< motifs", texte)
    if m is None:
        raise GardeArret("amorce : bloc des motifs d'extraction illisible")
    motifs = [x for x in m["corps"].split("\n") if x]
    if not motifs or any(not re.fullmatch(r"/[A-Za-z0-9._/*-]+", x) for x in motifs):
        raise GardeArret("amorce : motif d'extraction illisible")
    return motifs


def _extrait(chemin: str, motifs: list[str]) -> bool:
    """Un chemin du commit est-il extrait par ces motifs (extraction partielle sans cône : « /d/ » un dossier, « /f* »
    une étoile qui ne passe pas « / », « /f » un fichier ou un dossier) ?"""
    import fnmatch
    for x in motifs:
        p = x[1:]
        if p.endswith("/"):
            if chemin.startswith(p):
                return True
        elif "*" in p:
            if fnmatch.fnmatchcase(chemin, p) and chemin.count("/") == p.count("/"):
                return True
        elif chemin == p or chemin.startswith(p + "/"):
            return True
    return False


def exiger_arbre_extrait_propre(racine: Path, commit: str, engagement: str | None, existants=()) -> dict:
    """Constat m-5 de la contre-lecture : côté session, avant la création, la garde de l'arbre de la session de lecture
    (`exiger_arbre_de_lecture_propre`, liste d'arrêt, point 8) est jouée sur l'arbre que l'amorce extraira au commit de la
    marche (ses motifs, lus dans l'amorce de ce commit, et les adaptateurs existants cités), dans un dossier temporaire. La
    garde des références git reste celle de l'instance (son clone ne porte qu'une branche)."""
    import io
    import tarfile
    import tempfile

    motifs = motifs_de_l_amorce(_montrer(racine, commit, AMORCE).decode("utf-8"))
    ls = subprocess.run(["git", "-C", str(racine), "ls-tree", "-r", "-z", "--name-only", commit], capture_output=True)
    if ls.returncode != 0:
        raise GardeArret(f"arbre du commit {commit[:12]} illisible")
    tous = [x for x in ls.stdout.decode("utf-8").split("\0") if x]
    pris = sorted({c for c in tous if _extrait(c, motifs)} | {c for c in existants if c in tous})
    if not pris:
        raise GardeArret("arbre extrait vide : motifs de l'amorce sans fichier au commit")
    ar = subprocess.run(["git", "-C", str(racine), "archive", "--format=tar", commit, "--", *pris], capture_output=True)
    if ar.returncode != 0:
        raise GardeArret(f"extraction du commit {commit[:12]} impossible")
    with tempfile.TemporaryDirectory(prefix="b5f-arbre-extrait-") as t:
        base = Path(t) / "depot"
        with tarfile.open(fileobj=io.BytesIO(ar.stdout)) as tar:
            for membre in tar.getmembers():
                if not membre.isfile():
                    continue
                if membre.name.startswith("/") or ".." in Path(membre.name).parts:
                    raise GardeArret(f"extraction : chemin {membre.name!r} refusé")
                cible = base / membre.name
                cible.parent.mkdir(parents=True, exist_ok=True)
                cible.write_bytes(tar.extractfile(membre).read())
        r = exiger_arbre_de_lecture_propre(base, [], engagement, None)
    return {"motifs": len(motifs), "fichiers_extraits": len(pris), **r}


# --- côté session : instance de lecture (aucune création, aucun arrêt ici : les commandes sont imprimées) -------------

AMORCE = "scripts/amorce_b5f_lecture_v1.sh"
IMAGE = "python:3.11-bookworm"
DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"
BRANCHE_ENTREES = "donnees/barreau5-familles-jumelles-v1-entrees-de-lecture"
DOSSIER_ENTREES = "entrees-de-lecture-b5f"
ENTREES_DE_LA_MARCHE = f"../entrees/{DOSSIER_ENTREES}"
# devis, § 3 (qui fait foi) : heures de carte au plus, coupure ; disque : 300 Go pour la relecture (§ 3, ligne « Carte ») ;
# la répétition n'y a pas de disque écrit : 150 Go, comme une instance de formation (choix déclaré)
PIECES_LECTURE = {"decisif": {"etiquette": ETIQUETTE, "coupure_usd": 21.0, "heures_max": 5.42, "disque_go": 300,
                              "branche": "donnees/barreau5-familles-jumelles-v1-lecture", "suffixe": "b5f-lecture"},
                  "repetition": {"etiquette": ETIQUETTE_REPETITION, "coupure_usd": 8.0, "heures_max": 3.20, "disque_go": 150,
                                 "branche": "donnees/barreau5-familles-jumelles-v1-repetition", "suffixe": "b5f-repetition"}}
OFFRE_LECTURE = {"nom_offre": ("A100", "SXM4"), "memoire_carte_min_mo": 80000, "prix_max_usd_h": 1.30, "coeurs_min": 16,
                 "memoire_vive_min_mo": 128000, "stockage_max_usd_h": 0.08, "cuda_min": 13.0}
QUART_D_HEURE_H = 0.25
_RUN_LECTURE = re.compile(r"[0-9]{8}-[0-9]{6}-(?P<suffixe>b5f-lecture|b5f-repetition)")


def piece_lecture(plan: str) -> dict:
    if plan not in PIECES_LECTURE:
        raise GardeArret(f"plan {plan!r} : {sorted(PIECES_LECTURE)} attendu")
    return PIECES_LECTURE[plan]


def exiger_offre_lecture(offre: dict, plan: str) -> dict:
    """Bornes du devis sur une offre du loueur (champs bruts) pour la pièce du plan : A100 SXM4 80 Go, une carte, au plus
    1,30 USD de l'heure, au moins 16 cœurs et 128 Go de mémoire vive, disque de la pièce (300 Go pour la relecture),
    stockage au plus 0,08 USD de l'heure, CUDA au moins 13.0. Champ absent ou illisible : refus."""
    p = piece_lecture(plan)

    def nombre(cle):
        v = offre.get(cle)
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            raise GardeArret(f"offre : champ {cle} absent ou illisible")
        return float(v)
    nom = str(offre.get("gpu_name", ""))
    if not all(x in nom.replace("_", " ") for x in OFFRE_LECTURE["nom_offre"]):
        raise GardeArret(f"offre : carte {nom!r}, A100 SXM4 80 Go attendue")
    for cle, borne, sens in (("num_gpus", 1, "="), ("gpu_ram", OFFRE_LECTURE["memoire_carte_min_mo"], ">="),
                             ("cpu_cores_effective", OFFRE_LECTURE["coeurs_min"], ">="),
                             ("cpu_ram", OFFRE_LECTURE["memoire_vive_min_mo"], ">="), ("disk_space", p["disque_go"], ">="),
                             ("cuda_max_good", OFFRE_LECTURE["cuda_min"], ">="),
                             ("dph_total", OFFRE_LECTURE["prix_max_usd_h"], "<=")):
        v = nombre(cle)
        if (sens == "=" and v != borne) or (sens == ">=" and v < borne) or (sens == "<=" and not 0 < v <= borne):
            raise GardeArret(f"offre : {cle} = {v} hors de la borne du devis ({sens} {borne})")
    stockage_h = nombre("storage_cost") * p["disque_go"] / 730.0
    if stockage_h > OFFRE_LECTURE["stockage_max_usd_h"]:
        raise GardeArret(f"offre : stockage de {p['disque_go']} Go à {stockage_h:.3f} USD de l'heure > "
                         f"{OFFRE_LECTURE['stockage_max_usd_h']}")
    if not str(offre.get("id")).isdigit():
        raise GardeArret("offre : identifiant illisible")
    return {"id": str(offre["id"]), "prix_usd_h": nombre("dph_total")}


def echeance_arret_lecture_s(depart_s: float, plan: str, prix_usd_h: float) -> int:
    """Instant (secondes UTC) où le cumul plus un quart d'heure atteint la coupure de la pièce, au prix de l'offre, compté
    depuis l'impression de la commande ; refus si les heures laissées sont sous les heures attendues au plus du devis."""
    p = piece_lecture(plan)
    if not 0 < float(prix_usd_h) <= OFFRE_LECTURE["prix_max_usd_h"]:
        raise GardeArret("prix hors des bornes du devis")
    heures = p["coupure_usd"] / float(prix_usd_h) - QUART_D_HEURE_H
    if heures < p["heures_max"]:
        raise GardeArret(f"{heures:.2f} h avant la coupure < {p['heures_max']} h attendues au plus")
    return int(depart_s + heures * 3600)


def _montrer(racine: Path, commit: str, chemin: str) -> bytes:
    r = subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        raise GardeArret(f"{chemin} absent du commit {commit[:12]}")
    return r.stdout


def exiger_code_du_commit(racine: Path, commit_lecture: str, commit: str) -> None:
    """Le commit de la marche descend du commit de `CODE-LECTURE-B5F` et porte le même arbre gelé (`CHEMINS_GELES`)."""
    from ..harnais.validation_reelle import CHEMINS_GELES
    a = subprocess.run(["git", "-C", str(racine), "merge-base", "--is-ancestor", commit_lecture, commit], capture_output=True)
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit_lecture, commit, "--", *CHEMINS_GELES],
                       capture_output=True)
    if a.returncode != 0 or r.returncode != 0:
        raise GardeArret(f"commit de la marche {commit[:12]} : code différent de CODE-LECTURE-B5F {commit_lecture[:12]}, ou "
                         "ne descend pas de lui")


def commande_de_creation(racine: Path, plan: str, offre_json: Path, commit: str, branche: str, run_id: str, go_id: str,
                         entrees_commit: str, divergence: bool, garde: str, existants_json: Path, aujourd_hui,
                         maintenant_s: float) -> str:
    """Commande de création de l'instance de lecture (plan « decisif ») ou de la répétition générale (« repetition »), à
    jouer par la session. Refus : offre hors des bornes du devis ; commit, branche, marche ou commit des entrées illisibles ;
    registre au commit de la marche qui n'admet pas la marche (`exiger_registre_de_relecture`, instant de création :
    maintenant) ; code du commit ou de l'arbre de la session différent de `CODE-LECTURE-B5F` ; texte scellé absent du commit
    ou d'une autre empreinte ; amorce absente ; configuration refusée (adaptateurs existants sans empreinte compris), ou
    adaptateur existant absent du commit ; arbre que l'amorce extraira au commit qui porte la table, une ligne de la
    formation ou une marche de formation (`exiger_arbre_extrait_propre`) ; commit des entrées absent de leur branche
    distante (plan décisif) ; garde de calcul qui bloquerait la commande. Clés passées par leur nom ($HF_TOKEN, $GH_TOKEN) ;
    aucune valeur écrite ici."""
    import base64

    from .formation_v1 import exiger_garde_de_calcul
    p = piece_lecture(plan)
    of = exiger_offre_lecture(json.loads(Path(offre_json).read_text(encoding="utf-8")), plan)
    for nom, v in (("commit", commit), ("commit des entrées", entrees_commit)):
        if (v or nom == "commit") and not re.fullmatch(r"[0-9a-f]{40}", str(v)):
            raise GardeArret(f"{nom} (40 signes) attendu")
    if (plan == "decisif") != bool(entrees_commit):
        raise GardeArret("commit des entrées de lecture : exigé pour le plan décisif, refusé pour la répétition")
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", str(branche)):
        raise GardeArret("branche du code illisible")
    m = _RUN_LECTURE.fullmatch(str(run_id))
    if m is None or m["suffixe"] != p["suffixe"]:
        raise GardeArret(f"identifiant de marche AAAAMMJJ-HHMMSS-{p['suffixe']} attendu")
    existants = json.loads(Path(existants_json).read_text(encoding="utf-8"))
    if not isinstance(existants, list):
        raise GardeArret("adaptateurs existants : liste attendue")
    config = config_lecture(racine, go_id, plan, ENTREES_DE_LA_MARCHE if plan == "decisif" else None, divergence, garde,
                            ancrages=existants if plan == "decisif" else (),
                            adaptateurs_repetition=existants if plan == "repetition" else ())
    maintenant = datetime.fromtimestamp(maintenant_s, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reg = exiger_registre_de_relecture(_montrer(racine, commit, en.REGISTRE_PROPRE).decode("utf-8"), config, maintenant)
    exiger_code_du_commit(racine, reg["commit_lecture"], commit)
    lv.exiger_code_de_lecture_au_commit(racine, reg["commit_lecture"])
    if hashlib_sha256(_montrer(racine, commit, lv.TEXTE)) != lv.TEXTE_SHA256:
        raise GardeArret(f"texte {lv.TEXTE} : autre empreinte au commit de la marche (R1)")
    amorce = _montrer(racine, commit, AMORCE)
    for x in existants:
        if subprocess.run(["git", "-C", str(racine), "cat-file", "-e", f"{commit}:{x['chemin']}"],
                          capture_output=True).returncode != 0:
            raise GardeArret(f"adaptateur existant {x['nom']} : {x['chemin']} absent du commit de la marche")
    exiger_arbre_extrait_propre(racine, commit, reg["engagement"], [x["chemin"] for x in existants])
    if plan == "decisif":
        r = subprocess.run(["git", "-C", str(racine), "branch", "-r", "--contains", entrees_commit], capture_output=True,
                           text=True)
        if r.returncode != 0 or f"origin/{BRANCHE_ENTREES}" not in r.stdout.split():
            raise GardeArret(f"commit des entrées {entrees_commit[:12]} absent de la branche distante {BRANCHE_ENTREES}")
    arret = echeance_arret_lecture_s(maintenant_s, plan, of["prix_usd_h"])
    b64 = base64.b64encode(amorce).decode("ascii")
    ex64 = base64.b64encode(json.dumps(existants, separators=(",", ":"), sort_keys=True).encode("utf-8")).decode("ascii")
    cmd = (f"GO_ID={go_id} vastai create instance {of['id']} --raw --image {IMAGE} --disk {p['disque_go']} --cancel-unavail "
           f"--label {p['etiquette']} --env \"-e PLAN_B5F={plan} -e COMMIT={commit} -e BRANCHE_CODE={branche} "
           f"-e PREREG={lv.TEXTE} -e RUN_LECTURE={run_id} -e PRIX_USD_H={of['prix_usd_h']} -e ECHEANCE_ARRET_UTC_S={arret} "
           f"-e GO_ID={go_id} -e DEPOT_URL={DEPOT_URL} -e ENTREES_COMMIT={entrees_commit or '-'} "
           f"-e DIVERGENCE_B5F={int(bool(divergence))} -e GARDE_B5F={garde} -e EXISTANTS_B5F={ex64} "
           f"-e EXISTANTS_CHEMINS={','.join(x['chemin'] for x in existants) or '-'} "
           f"-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN\" --entrypoint bash --args -c "
           f"\"echo {b64} | base64 -d > /root/amorce_b5f_lecture_v1.sh && bash /root/amorce_b5f_lecture_v1.sh\"")
    exiger_garde_de_calcul(racine, cmd, aujourd_hui)
    return cmd


def hashlib_sha256(octets: bytes) -> str:
    import hashlib
    return hashlib.sha256(octets).hexdigest()


def commande_de_destruction(racine: Path, ident: str, plan: str, liste: Path, inventaire: Path, commit: str,
                            go_id: str) -> str:
    """Destruction par l'identifiant (R10), après preuve de l'étiquette de la pièce et du versement (chaque fichier de
    l'inventaire final au commit prouvé, commit sur une branche distante : `formation_v1.exiger_versement`, réemployé)."""
    from .formation_v1 import _instances, exiger_versement
    p = piece_lecture(plan)
    if not str(ident).isdigit():
        raise GardeArret("identifiant d'instance numérique attendu (R10)")
    trouvees = [x for x in _instances(liste) if str(x.get("id")) == str(ident)]
    if len(trouvees) != 1 or trouvees[0].get("label") != p["etiquette"]:
        raise GardeArret(f"instance {ident} absente, en double, ou d'une autre étiquette que {p['etiquette']}")
    exiger_versement(racine, inventaire, commit)
    return f"GO_ID={go_id} vastai destroy instance {ident} -y"


def ligne_scores(racine: Path, commit: str, run_id: str) -> str:
    """Contenu de la ligne `SCORES-B5F` (« commit <40> ; inventaire sha256 <64> »), après le versement prouvé : l'inventaire
    de l'arbre fermé (`donnees/<marche>/lecture/inventaire.json`) et chacun de ses fichiers (fichiers de scores par jeton
    de chaque série compris) sont au commit, à leur taille et à leur empreinte, et ce commit est sur la branche distante de
    sortie de la pièce (`PIECES_LECTURE`, selon l'identifiant de la marche ; constat v-1). Aucun fichier n'est lu au-delà
    de son empreinte."""
    if not re.fullmatch(r"[0-9a-f]{40}", str(commit)) or _RUN_LECTURE.fullmatch(str(run_id)) is None:
        raise GardeArret("commit (40 signes) et identifiant de marche de lecture attendus")
    base = f"donnees/{run_id}/lecture"
    octets = _montrer(racine, commit, f"{base}/inventaire.json")
    inv = json.loads(octets.decode("utf-8"))
    if inv.get("format") != lv.FORMAT_INVENTAIRE or not inv.get("fichiers"):
        raise GardeArret("inventaire de l'arbre fermé illisible ou vide")
    for f in inv["fichiers"]:
        b = _montrer(racine, commit, f"{base}/{f['chemin']}")
        if len(b) != f["octets"] or hashlib_sha256(b) != f["sha256"]:
            raise GardeArret(f"{f['chemin']} : taille ou empreinte au commit ≠ inventaire : versement non prouvé")
    # constat v-1 de la vérification : le commit est sur la branche de sortie de la pièce, et non sur une branche quelconque
    branche = piece_lecture("decisif" if _RUN_LECTURE.fullmatch(str(run_id))["suffixe"] == "b5f-lecture" else
                            "repetition")["branche"]
    r = subprocess.run(["git", "-C", str(racine), "branch", "-r", "--contains", commit], capture_output=True, text=True)
    if r.returncode != 0 or f"origin/{branche}" not in r.stdout.split():
        raise GardeArret(f"commit {commit[:12]} absent de la branche distante {branche} : versement non prouvé")
    return f"commit {commit} ; inventaire sha256 {hashlib_sha256(octets)}"


def activations_gardees(sorties: Path) -> list[str]:
    """Chemins (relatifs à la racine du dépôt) des activations que garde la règle de la marche, lus dans
    `garde-activations.json` (vérifié par son compagnon) : ceux que l'amorce verse ; rien d'autre."""
    sorties = Path(sorties)
    p = sorties / "garde-activations.json"
    verifier(p)
    x = json.loads(p.read_text(encoding="utf-8"))
    if x.get("regle") not in GARDES_ACTIVATIONS or not isinstance(x.get("fichiers"), list):
        raise GardeArret("garde des activations illisible")
    sortie = []
    for c in x["fichiers"]:
        if _SORTIE.fullmatch(str(c)) is None or not str(c).startswith("activations/"):
            raise GardeArret(f"garde des activations : chemin {c!r} hors de la liste blanche")
        sortie.append((sorties / c).as_posix())
    return sortie


def precharger(racine: Path) -> str:
    """Modèle de la configuration scellée au cache local (révision figée), avant la marche hors ligne."""
    from ..harnais.modeles import precharger_modele
    chemin = Path(racine) / CONFIG_SCELLEE["chemin"]
    if verifier(chemin) != CONFIG_SCELLEE["sha256"]:
        raise GardeArret("configuration scellée de la course de confirmation : empreinte différente (R11)")
    a = json.loads(chemin.read_text(encoding="utf-8"))["agent"]
    return precharger_modele(a["modele"], a["revision"])


def _session(argv: list[str]) -> int:
    from datetime import date
    if not argv:
        raise GardeArret("sous-commande attendue : config, verifier, commande, detruire, verifier-destruction, scores, "
                         "gardees, precharger")
    s, a = argv[0], argv[1:]
    if s == "config" and len(a) in (6, 7):
        racine, go_id, plan, entrees, divergence, garde = a[:6]
        if divergence not in ("0", "1"):
            raise GardeArret("DIVERGENCE : 0 ou 1")
        existants = json.loads(Path(a[6]).read_text(encoding="utf-8")) if len(a) == 7 else []
        if not isinstance(existants, list):
            raise GardeArret("adaptateurs existants : liste attendue")
        print(json.dumps(config_lecture(Path(racine), go_id, plan, entrees or None, divergence == "1", garde,
                                        ancrages=existants if plan == "decisif" else (),
                                        adaptateurs_repetition=existants if plan == "repetition" else ()),
                         ensure_ascii=False, sort_keys=True))
    elif s == "verifier" and len(a) == 3:
        racine, commit, config_f = a
        config = json.loads(Path(config_f).read_text(encoding="utf-8"))
        exiger_config_lecture(config, Path(racine))
        print(json.dumps(verifier_avant_creation(Path(racine), commit, config), ensure_ascii=False))
    elif s == "commande" and len(a) == 11:
        plan, racine, offre, commit, branche, run_id, go_id, entrees_commit, divergence, garde, existants = a
        if divergence not in ("0", "1"):
            raise GardeArret("DIVERGENCE : 0 ou 1")
        print(commande_de_creation(Path(racine), plan, Path(offre), commit, branche, run_id, go_id,
                                   "" if entrees_commit == "-" else entrees_commit, divergence == "1", garde,
                                   Path(existants), date.today(), time.time()))
    elif s == "detruire" and len(a) == 7:
        print(commande_de_destruction(Path(a[0]), a[1], a[2], Path(a[3]), Path(a[4]), a[5], a[6]))
    elif s == "verifier-destruction" and len(a) == 3:
        from .formation_v1 import absence_prouvee
        absence_prouvee(Path(a[0]), a[1], a[2])
        print(f"absence de l'instance {a[1]} prouvée")
    elif s == "scores" and len(a) == 3:
        print(ligne_scores(Path(a[0]), a[1], a[2]))
    elif s == "gardees" and len(a) == 1:
        for c in activations_gardees(Path(a[0])):
            print(c)
    elif s == "precharger" and len(a) == 1:
        print(precharger(Path(a[0])))
    else:
        raise GardeArret(f"sous-commande {s!r} ou nombre d'arguments ({len(a)}) inconnu")
    return 0


def _main(argv: list[str]) -> int:
    if argv[:1] == ["session"]:
        return _session(argv[1:])
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", required=True)
    x = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    config = json.loads(Path(x.config).read_text(encoding="utf-8"))
    r = executer(config, Path("."), x.run_id, x.prereg)
    print(json.dumps({"inventaire_sha256": r["inventaire_sha256"]}, ensure_ascii=False))
    return 0


__all__ = ["exiger_config_lecture", "exiger_registre_de_relecture", "exiger_entrees", "exiger_arbre_de_lecture_propre",
           "charger_etat_fichier", "rejouer", "divergence_par_jeton", "Lecteur", "executer", "garde_des_activations",
           "exiger_sorties_lecture_permises"]


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
