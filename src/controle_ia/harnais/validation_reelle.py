"""Validation du harnais sur modèle réel (T0.4 ; porte G0, critère 1), et sa répétition sur modèle jouet.

Sur la machine de calcul, après GO (jamais sans) :
    PYTHONPATH=src python -m controle_ia.harnais.validation_reelle --revision <commit> --prereg <préenregistrement>
    PYTHONPATH=src python -m controle_ia.harnais.validation_reelle --revision <commit> --prereg <…> --rejeu-de <run A>
Répétition sur processeur, modèle jouet, non décisive :
    PYTHONPATH=src python -m controle_ia.harnais.validation_reelle --repetition-jouet [--rejeu-de <run A>]

Phases, dans un seul processus :
0. format : garde de format (transcription incrémentale = gabarit complet du tokeniseur) ;
1. logique, simple précision : épisodes courts en lots, toutes les actions dans l'échantillon
   d'équivalence ; tolérance 1e-4 ; contrôle négatif décalé d'un jeton ;
2. production, demi-précision : épisodes en lots ; équivalence et contrôle négatif sur les épisodes
   d'échantillon (tolérance de production) ; politique de stockage (codage bfloat16-bits) ; relecture
   du disque ; rejeu du premier lot dans le processus ; débit et stockage mesurés ;
3. débit : génération seule, sans arrêt anticipé, pour plusieurs tailles de lot.
Le rejeu dans un second processus est un second lancement à la même entropie (`--rejeu-de`) : il rejoue
tout et compare ses empreintes à celles du premier, au bit près (comparaison scellée).

Les gros tableaux (npz) vont dans `donnees/<run>/` (hors git, scellés sur place) ; leurs empreintes sont
dans les résultats scellés de `diag/<run>/`. Toute garde qui arrête le run laisse un `arret.json` scellé,
puis l'arrêt se propage : aucun repli silencieux (R5).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import torch

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, lire_manifeste, verifier_resultat
from . import politique as P
from .activations import couches_par_defaut
from .episode import (EnvironnementJouet, empreinte_episode, empreinte_tableaux, generer_lot, jouer_episodes)
from .formats import FormatChat, verifier_format
from .modeles import (charger_modele, empreinte_poids, exiger_modele_autorise, fins_du_modele, modele_jouet,
                      regler_determinisme, tokeniseur_caracteres_chat)
from .stockage import estimer

COMMIT_CITE = re.compile(r"Commit du code d'analyse : `([0-9a-f]{40})`")

SONDES = [{"nom": f"lineaire-{a}-{c}", "couche": c, "agregation": a}
          for c in ("precoce", "mediane", "tardive") for a in ("max", "attention")]

CONFIG_REELLE = {
    "objet": "validation du harnais sur modèle réel (T0.4 ; porte G0, critère 1) ; aucune mesure de fond",
    "modele": "meta-llama/Llama-3.1-8B-Instruct", "attention": "sdpa", "appareil": "cuda", "fils": 1,
    "variables_gabarit": {"date_string": "26 Jul 2024"},
    "format": {"consigne": "Tu es l'agent 0. Propose une étape d'expérience, en une phrase.",
               "observations": ["Pas 0. Journal : ", "Pas 1. Journal : 0@0: Mesurer la température.",
                                "Pas 2. Journal : 0@1: Répéter la mesure."],
               "reponses": ["Je propose de mesurer la température.", "Je répète la mesure.",
                            "Je compare les deux mesures."]},
    "logique": {"dtype": "float32", "episodes": 2, "N": 2, "T": 3, "max_nouveaux": 64, "taille_lot": 2,
                "temperature": 1.0, "tolerance": 1e-4},
    "production": {"dtype": "bfloat16", "episodes": 16, "N": 2, "T": 10, "max_nouveaux": 256, "taille_lot": 8,
                   "temperature": 1.0, "tolerance": 0.1, "episodes_equivalence": [0, 1],
                   "lots_rejeu_en_processus": [0]},
    "debit": {"tailles_lot": [1, 8, 32], "longueur_contexte": 2048, "max_nouveaux": 128},
    "politique": {"episodes_par_jeton": [0, 1], "vecteurs_par_action": ["max"], "sondes": SONDES},
    "projection": {"episodes": 2000},
    "limite_s": 3 * 3600,
}

CONFIG_REPETITION = dict(
    CONFIG_REELLE,
    objet="répétition de la validation sur modèle jouet à poids aléatoires (processeur) ; non décisive",
    modele="jouet", appareil="cpu",
    modele_jouet={"couches": 4, "largeur": 32, "tetes": 4, "tetes_cle_valeur": 2, "intermediaire": 64},
    logique=dict(CONFIG_REELLE["logique"], episodes=2, N=2, T=2, max_nouveaux=12, taille_lot=2),
    production=dict(CONFIG_REELLE["production"], episodes=4, N=2, T=3, max_nouveaux=16, taille_lot=2),
    debit={"tailles_lot": [1, 2, 4], "longueur_contexte": 48, "max_nouveaux": 8},
    limite_s=900,
)


# ---------------------------------------------------------------- configuration et graines

def valider_config(config: dict, revision: str | None) -> None:
    if config["modele"] != "jouet":
        exiger_modele_autorise(config["modele"], revision)
    for phase in ("logique", "production"):
        c = config[phase]
        if min(c["episodes"], c["N"], c["T"], c["max_nouveaux"], c["taille_lot"]) < 1:
            raise GardeArret(f"{phase} : tailles ≥ 1 attendues")
        if not c["tolerance"] > 0:
            raise GardeArret(f"{phase} : tolérance {c['tolerance']} ≤ 0")
    if config["logique"]["dtype"] != "float32":
        raise GardeArret("la phase de logique se fait en simple précision")
    prod = config["production"]
    if not set(prod["episodes_equivalence"]) <= set(range(prod["episodes"])):
        raise GardeArret(f"épisodes d'équivalence {prod['episodes_equivalence']} hors de la production")
    n_lots = -(-prod["episodes"] // prod["taille_lot"])
    if not set(prod["lots_rejeu_en_processus"]) <= set(range(n_lots)):
        raise GardeArret(f"lots de rejeu {prod['lots_rejeu_en_processus']} hors de [0, {n_lots}[")
    n_couches = config.get("modele_jouet", {}).get("couches", 32)
    P.valider_politique(config["politique"], n_couches, prod["episodes"])
    if max(config["debit"]["tailles_lot"]) > prod["episodes"] * prod["N"]:
        raise GardeArret("débit : plus de lignes que de transcriptions de production")


def taches(config: dict) -> list[str]:
    t = ["modele-jouet"] if config["modele"] == "jouet" else []
    t += [f"sonde-{d['nom']}" for d in config["politique"]["sondes"]]
    for phase in ("logique", "production"):
        c = config[phase]
        t += [f"{phase}/episode-{k}/action-{i}-{p}" for k in range(c["episodes"]) for p in range(c["T"])
              for i in range(c["N"])]
    t += [f"debit/ligne-{r}" for r in range(max(config["debit"]["tailles_lot"]))]
    return t


def graine_entiere(graine: dict) -> int:
    return int(generateur(graine).integers(0, 2 ** 63 - 1))


# ---------------------------------------------------------------- gardes de lancement

def exiger_code_cite(racine: Path, prereg: Path) -> str:
    """Garde : `src` et `tests` au lancement sont ceux du commit cité par le préenregistrement."""
    m = COMMIT_CITE.search(prereg.read_text(encoding="utf-8"))
    if not m:
        raise GardeArret(f"{prereg} ne cite pas le commit du code d'analyse (40 caractères hexadécimaux)")
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", m.group(1), "HEAD", "--", "src", "tests"],
                       capture_output=True, text=True)
    if r.returncode == 1:
        raise GardeArret(f"code ou tests modifiés depuis le commit cité {m.group(1)[:12]}")
    if r.returncode != 0:
        raise GardeArret(f"comparaison au commit cité {m.group(1)[:12]} impossible : {r.stderr.strip()}")
    return m.group(1)


def exiger_code_importe_sous(racine: Path) -> None:
    import controle_ia

    if (racine / "src").resolve() not in Path(controle_ia.__file__).resolve().parents:
        raise GardeArret("code importé hors de la racine du dépôt : lancer depuis la racine")


# ---------------------------------------------------------------- modèle, format, épisodes

def charger(config: dict, revision: str | None, dtype: str, graines: dict):
    if config["modele"] == "jouet":
        tok = tokeniseur_caracteres_chat()
        m = modele_jouet(graine_entiere(graines["modele-jouet"]), len(tok), **config["modele_jouet"])
        return m.to(getattr(torch, dtype)).eval(), tok
    return charger_modele(config["modele"], revision, dtype, config["appareil"], config["attention"])


def format_du_modele(modele, tok, variables: dict) -> FormatChat:
    """Format de conversation ; jetons d'arrêt = ceux du modèle plus le jeton qui ferme un tour du gabarit."""
    fmt = FormatChat(tok, variables=variables)
    debut = ("x", "y")
    fmt.fins = fins_du_modele(modele, tok) | {fmt._pieces(debut)["cloture"][0]}
    return fmt


def jouer_phase(modele, fmt, c: dict, graines: dict, phase: str, couches: list[int], episodes_equivalence,
                lots=None, chrono=None) -> tuple[list, list]:
    """Joue les épisodes d'une phase par lots consécutifs (plan de lots fixé par la configuration)."""
    E, B = c["episodes"], c["taille_lot"]
    plan = [list(range(j, min(j + B, E))) for j in range(0, E, B)]
    sorties = []
    for j, lot in enumerate(plan):
        if lots is not None and j not in lots:
            continue
        g = [{(i, p): graine_entiere(graines[f"{phase}/episode-{k}/action-{i}-{p}"])
              for p in range(c["T"]) for i in range(c["N"])} for k in lot]
        echantillon = {(b, i, p) for b, k in enumerate(lot) if k in episodes_equivalence
                       for p in range(c["T"]) for i in range(c["N"])}
        sorties += jouer_episodes(modele, fmt, EnvironnementJouet(), [f"episode-{k}" for k in lot], c["N"], c["T"], g,
                                  couches, c["max_nouveaux"], c["temperature"], echantillon, c["tolerance"],
                                  chrono=chrono)
    return sorties, plan


def bilan_equivalence(sorties) -> dict:
    ecarts = [e for _, _, r in sorties for d in r["ecarts"].values() for e in d.values()]
    decales = [e for _, _, r in sorties for d in r["controle_negatif_decalage_1"].values() for e in d.values()]
    nuls = sum(p["nuls"] for _, _, r in sorties for d in r["profils"].values() for p in d.values())
    jetons = sum(p["jetons"] for _, _, r in sorties for d in r["profils"].values() for p in d.values())
    return {"actions": sum(len(r["ecarts"]) for _, _, r in sorties), "ecart_max": max(ecarts) if ecarts else None,
            "decale_min": min(decales) if decales else None, "ecarts_nuls": nuls, "jetons_compares": jetons}


def debit(chrono: dict) -> dict:
    g, p = chrono.get("generation_s", 0.0), chrono.get("passe_unique_s", 0.0)
    return {**chrono, "jetons_generes_par_s": chrono.get("jetons_generes", 0) / g if g > 0 else None,
            "jetons_passe_unique_par_s": chrono.get("jetons_passe_unique", 0) / p if p > 0 else None}


def memoire_max_go() -> float | None:
    if not torch.cuda.is_available():
        return None
    return round(torch.cuda.max_memory_allocated() / 1e9, 3)


def liberer() -> None:
    """Après `del modele` chez l'appelant : rend la mémoire du processeur graphique, remet le pic à zéro."""
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()


# ---------------------------------------------------------------- run

def executer(racine: str | Path, run_id: str, revision: str | None = None, entropie: int | None = None,
             config: dict | None = None, prereg: str | Path | None = None, rejeu_de: str | None = None,
             verifier_import: bool = True) -> dict:
    """`verifier_import=False` n'est permis qu'aux tests sur mini-dépôt ; la ligne de commande l'active toujours."""
    racine = Path(racine)
    config = config or CONFIG_REELLE
    depart = time.perf_counter()
    decisif = config["modele"] != "jouet"
    if decisif and prereg is None:
        raise GardeArret("validation sur modèle réel sans préenregistrement scellé : R1 interdit de lancer")
    valider_config(config, revision)
    if verifier_import:
        exiger_code_importe_sous(racine)
    commit_cite = exiger_code_cite(racine, Path(prereg)) if prereg is not None else None
    if rejeu_de is not None:
        m_a, _ = lire_manifeste(racine / "runs" / rejeu_de / "manifeste.json")
        entropie_a = int(next(iter(m_a["graines"].values()))["entropie"])
        if entropie is not None and entropie != entropie_a:
            raise GardeArret(f"rejeu de {rejeu_de} : entropie {entropie} ≠ {entropie_a}")
        entropie = entropie_a
    config = dict(config, revision=revision)
    chemin_m, m = creer_manifeste(racine, run_id, config, taches(config), entropie=entropie, decisif=decisif,
                                  prereg=prereg, commande="python -m controle_ia.harnais.validation_reelle")
    donnees = racine / "donnees" / run_id
    resume: dict = {"commit_cite": commit_cite}
    phase = "reglages"

    def temps():
        if time.perf_counter() - depart > config["limite_s"]:
            raise GardeArret(f"limite de durée de {config['limite_s']} s dépassée avant la phase {phase}")

    try:
        resume["reglages"] = regler_determinisme(config["fils"], config["appareil"])
        graines = m["graines"]

        phase = "logique"
        temps()
        modele, tok = charger(config, revision, "float32", graines)
        fmt = format_du_modele(modele, tok, config["variables_gabarit"])
        resume["format"] = {"fins": sorted(fmt.fins), **verifier_format(fmt, **config["format"])}
        couches = couches_par_defaut(modele.config.num_hidden_layers)
        chrono: dict = {}
        sorties, plan = jouer_phase(modele, fmt, config["logique"], graines, "logique", couches,
                                    range(config["logique"]["episodes"]), chrono=chrono)
        resume["logique"] = {"plan_lots": plan, "equivalence": bilan_equivalence(sorties), "debit": debit(chrono),
                             "memoire_max_go": memoire_max_go(),
                             "episodes": [{"episode": ep.identifiant, "empreintes": empreinte_episode(ep, acts),
                                           "equivalence": eq} for ep, acts, eq in sorties]}
        del modele, sorties
        liberer()

        phase = "production"
        temps()
        prod = config["production"]
        modele, tok = charger(config, revision, prod["dtype"], graines)
        fmt = format_du_modele(modele, tok, config["variables_gabarit"])
        largeur = modele.config.hidden_size
        codage = "bfloat16-bits" if prod["dtype"] == "bfloat16" else "float32"
        sondes = P.construire_sondes(config["politique"], couches, largeur, graines)
        chrono = {}
        sorties, plan = jouer_phase(modele, fmt, prod, graines, "production", couches, prod["episodes_equivalence"],
                                    chrono=chrono)

        def empreintes(ep, acts):
            v, s = P.calculer_en_ligne(config["politique"], ep, acts, couches, sondes)
            return {**empreinte_episode(ep, acts), "vecteurs": empreinte_tableaux(v), "scores": empreinte_tableaux(s)}, v, s

        episodes, octets_par_jeton, jetons_par_episode = [], [], []
        for k, (ep, acts, eq) in enumerate(sorties):
            par_jeton = k in config["politique"]["episodes_par_jeton"]
            emp, v, s = empreintes(ep, acts)
            ecrire_resultat(racine, chemin_m, f"production-{ep.identifiant}-trajectoire", ep.en_dict())
            npz = P.ecrire_tableaux(donnees / f"production-{ep.identifiant}-tableaux.npz",
                                    acts if par_jeton else None, v, s, codage)
            P.relire_et_controler(npz, config["politique"], ep, couches, sondes, v, s, par_jeton, codage)
            jetons = sum(len(tr.ids) for tr in ep.transcriptions)
            jetons_par_episode.append(jetons)
            if par_jeton:
                octets_par_jeton.append(sum(P.coder(a, codage).nbytes for pc in acts.values() for a in pc.values())
                                        / (jetons * len(couches)))
            episodes.append({"episode": ep.identifiant, "par_jeton_conserve": par_jeton, "empreintes": emp,
                             "equivalence": eq, "tableaux": str(npz.relative_to(racine)),
                             "tableaux_sha256": npz.with_name(npz.name + ".sha256").read_text().split()[0],
                             "tableaux_octets": npz.stat().st_size, "jetons": jetons})
        rejeu = []
        for j in prod["lots_rejeu_en_processus"]:
            refaits, _ = jouer_phase(modele, fmt, prod, graines, "production", couches, prod["episodes_equivalence"],
                                     lots=[j])
            for (ep, acts, _), k in zip(refaits, plan[j]):
                rejeu.append({"episode": ep.identifiant, "identique": empreintes(ep, acts)[0] == episodes[k]["empreintes"]})
        moyenne_jetons = sum(jetons_par_episode) / len(jetons_par_episode)
        actions = prod["N"] * prod["T"]
        par_episode_s = (chrono.get("generation_s", 0.0) + chrono.get("passe_unique_s", 0.0)) / prod["episodes"]
        stockage = {"codage": codage, "octets_par_jeton_et_couche": octets_par_jeton,
                    "octets_par_valeur": octets_par_jeton[0] / largeur if octets_par_jeton else None,
                    "jetons_par_episode_moyen": moyenne_jetons,
                    "projection": estimer(config["projection"]["episodes"], max(1, round(moyenne_jetons)), actions,
                                          len(couches), largeur, 2 if codage == "bfloat16-bits" else 4)}
        resume["production"] = {"plan_lots": plan, "couches": couches, "largeur": largeur,
                                "projection_heures": {"episodes": config["projection"]["episodes"],
                                                      "taille_lot": prod["taille_lot"],
                                                      "heures": par_episode_s * config["projection"]["episodes"] / 3600},
                                "empreinte_poids": empreinte_poids(modele), "equivalence": bilan_equivalence(sorties),
                                "rejeu_en_processus": rejeu, "debit": debit(chrono), "stockage": stockage,
                                "sondes": [{"nom": x.nom, "couche": x.couche, "agregation": x.agregation,
                                            "empreinte": x.empreinte()} for x in sondes],
                                "episodes": episodes, "memoire_max_go": memoire_max_go()}

        phase = "debit"
        temps()
        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
        cd = config["debit"]
        transcriptions = [tr.ids[:cd["longueur_contexte"]] for ep, _, _ in sorties for tr in ep.transcriptions]
        mesures = []
        for B in cd["tailles_lot"]:
            graines_lot = [graine_entiere(graines[f"debit/ligne-{r}"]) for r in range(B)]
            t0 = time.perf_counter()
            nouveaux, _ = generer_lot(modele, transcriptions[:B], cd["max_nouveaux"], 1.0, graines_lot, set(),
                                      fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins))
            duree = time.perf_counter() - t0
            n = sum(len(x) for x in nouveaux)
            mesures.append({"taille_lot": B, "jetons_generes": n, "duree_s": duree, "jetons_par_s": n / duree,
                            "contexte_moyen": sum(len(c) for c in transcriptions[:B]) / B})
        resume["debit"] = {"mesures": mesures, "memoire_max_go": memoire_max_go()}
        del modele
        liberer()
        resume["lecture"] = lire(resume, config)
        resume["duree_s"] = time.perf_counter() - depart
    except Exception as e:          # garde ou panne (mémoire, noyau non déterministe…) : consignée, puis propagée
        ecrire_resultat(racine, chemin_m, "arret", {"phase": phase, "motif": f"{type(e).__name__}: {e}",
                                                     "partiel": resume, "duree_s": time.perf_counter() - depart})
        raise
    chemin_r = ecrire_resultat(racine, chemin_m, "resume", resume)
    verifier_resultat(racine, chemin_r)
    sortie = {"manifeste": str(chemin_m), "resume": str(chemin_r), "lecture": resume["lecture"]}
    if rejeu_de is not None:
        sortie["comparaison"] = comparer_runs(racine, rejeu_de, run_id)
    return sortie


# ---------------------------------------------------------------- lecture et comparaison

def lire(resume: dict, config: dict) -> dict:
    """Lecture gelée des prédictions mesurables dans un seul processus (le rejeu entre processus est lu par
    `comparer_runs`). Issues : « conforme », « contraire » ; l'audit de symétrie se déclenche si aucun
    écart d'équivalence n'est non nul en demi-précision (trop beau, R4)."""
    lo, pr = resume["logique"]["equivalence"], resume["production"]["equivalence"]
    tl, tp = config["logique"]["tolerance"], config["production"]["tolerance"]

    def etat(ok):
        return "conforme" if ok else "contraire"
    lecture = {
        "format": etat(resume["format"].get("verifie") is True),
        "logique_equivalence": etat(lo["ecart_max"] is not None and lo["ecart_max"] <= tl),
        "logique_controle_negatif": etat(lo["decale_min"] is not None and lo["decale_min"] > tl),
        "production_equivalence": etat(pr["ecart_max"] is not None and pr["ecart_max"] <= tp),
        "production_controle_negatif": etat(pr["decale_min"] is not None and pr["decale_min"] > tp),
        "rejeu_en_processus": etat(bool(resume["production"]["rejeu_en_processus"])
                                   and all(r["identique"] for r in resume["production"]["rejeu_en_processus"])),
    }
    lecture["audit_symetrie"] = ("déclenché : aucun écart non nul en demi-précision"
                                 if config["production"]["dtype"] != "float32" and pr["ecarts_nuls"] == pr["jetons_compares"]
                                 else "non déclenché")
    return lecture


def comparer_runs(racine: str | Path, run_a: str, run_b: str) -> dict:
    """Rejeu entre processus : mêmes configuration, graines et code ; empreintes identiques au bit près, phase par
    phase et épisode par épisode. Résultat scellé dans `diag/<run_b>/`, rattaché au manifeste de B."""
    racine = Path(racine)
    m_a, _ = lire_manifeste(racine / "runs" / run_a / "manifeste.json")
    m_b, _ = lire_manifeste(racine / "runs" / run_b / "manifeste.json")
    if m_a["config_sha256"] != m_b["config_sha256"]:
        raise GardeArret(f"{run_a} et {run_b} : configurations différentes, rejeu sans objet")
    if m_a["graines"] != m_b["graines"]:
        raise GardeArret(f"{run_a} et {run_b} : graines différentes, rejeu sans objet")
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", m_a["commit"], m_b["commit"], "--", "src", "tests"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeArret(f"{run_a} et {run_b} : code ou tests différents entre {m_a['commit'][:12]} et {m_b['commit'][:12]}")
    a = verifier_resultat(racine, racine / "diag" / run_a / "resume.json")["resultat"]
    b = verifier_resultat(racine, racine / "diag" / run_b / "resume.json")["resultat"]
    differences = []
    for phase in ("logique", "production"):
        ea = {e["episode"]: e["empreintes"] for e in a[phase]["episodes"]}
        eb = {e["episode"]: e["empreintes"] for e in b[phase]["episodes"]}
        if set(ea) != set(eb):
            differences.append({"phase": phase, "motif": "épisodes différents"})
            continue
        for ep in sorted(ea):
            for cle in sorted(set(ea[ep]) | set(eb[ep])):
                if ea[ep].get(cle) != eb[ep].get(cle):
                    differences.append({"phase": phase, "episode": ep, "empreinte": cle})
    if a["production"]["empreinte_poids"] != b["production"]["empreinte_poids"]:
        differences.append({"phase": "production", "motif": "poids différents"})
    corps = {"run_a": run_a, "run_b": run_b, "identique": not differences, "differences": differences,
             "lecture": "conforme" if not differences else "contraire"}
    ecrire_resultat(racine, racine / "runs" / run_b / "manifeste.json", f"comparaison-{run_a}", corps)
    return corps


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--racine", default=".")
    a.add_argument("--run-id", default=None)
    a.add_argument("--revision", default=None)
    a.add_argument("--prereg", default=None)
    a.add_argument("--entropie", type=int, default=None)
    a.add_argument("--rejeu-de", default=None)
    a.add_argument("--repetition-jouet", action="store_true")
    args = a.parse_args(argv)
    config = CONFIG_REPETITION if args.repetition_jouet else CONFIG_REELLE
    suffixe = "repetition-jouet" if args.repetition_jouet else "validation-reelle"
    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + suffixe
    sortie = executer(args.racine, run_id, args.revision, args.entropie, config, args.prereg, args.rejeu_de)
    print(json.dumps(sortie, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
