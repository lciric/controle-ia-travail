"""R2 — juge par action (moniteur boîte noire de confiance, Llama-3.2-3B-Instruct ; Llama-3.1-8B-Instruct en bras
secondaire descriptif) sur les actions d'un run de P3 (GO-2026-11-01-13 ; format fixé par conv-audit, n° 328).

Lecture sans génération (P-003, `bases/scores_jetons.py`) : le juge reçoit l'invite gelée (fichier scellé de trois blocs
cités « > » : consigne système du bras spécialisé, consigne système du bras générique, message utilisateur à deux champs
`{questions}` et `{action}`), puis la seule ouverture de sa réponse (réponse imposée vide). On lit les log-probabilités
des jetons « Yes » et « No » à la première position de la réponse ; score = P(Yes) renormalisée sur {Yes, No}
(`environnements.juges.probabilite_oui`) ; masse = P(Yes) + P(No) avant renormalisation, consignée (anomalie si elle est
sous `masse_min`, jamais remplacée : une action en anomalie garde son score renormalisé, et le drapeau `anomalie` la
signale à l'analyse, qui la rapporte à part).

Contexte vu par le juge, gelé : l'énoncé de la tâche (questions de recherche) et le texte de l'action seule ; ni la
consigne privée, ni l'indication, ni les actions précédentes de l'épisode.

Sortie alignée sur `scores-p3.npz` (mêmes quatre tableaux d'identité, même ordre) : `score`, `logprob_oui`,
`logprob_non`, `masse` (bras spécialisé, bras principal), les mêmes suffixés `_generique`, `jetons_contexte`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import signal
import sys
import time
from pathlib import Path

import numpy as np

from ..environnements.juges import probabilite_oui
from ..environnements.pilote_a import charger_taches, jetons_jouet, jetons_oui_non, logits_derniere_position
from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat
from ..scellement import sceller, verifier
from .alignement_v1 import CLES_IDENTITE, charger_identite, charger_textes_alignes, empreinte_identite

COMMANDE = "python -m controle_ia.runs_nuit.juge_actions_v1"
CLES = ("juge", "mode", "chemin_invite", "invite_sha256", "chemin_textes", "textes_sha256", "chemin_scores",
        "scores_sha256", "chemin_taches", "taches_sha256", "identite_sha256", "lot", "masse_min", "fils", "nom_sortie")
CONFIG_CITEE = "Configuration du juge {} (empreinte canonique) : `{}`"
BRAS = ("specialise", "generique")
CONTEXTE = "énoncé de la tâche et texte de l'action seule (ni consigne privée, ni indication, ni actions précédentes)"


def empreinte_config(config: dict) -> str:
    return hashlib.sha256(config_canonique(config)).hexdigest()


def charger_invite_juge(chemin, sha_attendue: str | None) -> dict:
    """Trois blocs cités : système spécialisé, système générique, message utilisateur (`{questions}`, `{action}`)."""
    from ..premier_test_ia.conditions import blocs_cites

    sha = verifier(chemin)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"{chemin} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    blocs = blocs_cites(Path(chemin).read_text(encoding="utf-8"))
    if len(blocs) != 3 or any(not b for b in blocs):
        raise GardeArret(f"{chemin} : trois blocs cités attendus (système spécialisé, système générique, utilisateur), "
                         f"{len(blocs)} trouvés")
    utilisateur = blocs[2].replace("\\n", "\n")
    if utilisateur.count("{questions}") != 1 or utilisateur.count("{action}") != 1:
        raise GardeArret("message utilisateur du juge : un champ {questions} et un champ {action} exigés")
    return {"sha256": sha, "specialise": blocs[0], "generique": blocs[1], "utilisateur": utilisateur}


def demandes(lignes: list[dict], taches: dict, invite: dict, bras: str) -> list[dict]:
    sortie = []
    for i, x in enumerate(lignes):
        u = invite["utilisateur"].replace("{questions}", taches[x["tache"]]["questions"].strip()) \
                                 .replace("{action}", x["texte"].strip() or "(empty action)")
        sortie.append({"cle": i, "systeme": invite[bras], "utilisateur": u})
    return sortie


def noter(modele, fmt, ds: list[dict], oui: int, non: int, lot: int, masse_min: float) -> dict:
    from ..bases.scores_jetons import contexte_impose

    n = len(ds)
    t = {"score": np.full(n, np.nan), "logprob_oui": np.full(n, np.nan), "logprob_non": np.full(n, np.nan),
         "masse": np.full(n, np.nan), "jetons_contexte": np.zeros(n, dtype=np.int64)}
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    ordre = sorted(range(n), key=lambda i: len(ds[i]["utilisateur"]))        # lots de longueurs voisines
    for k in range(0, n, lot):
        exiger_sans_signal(f"juge, lot {k // lot}")
        morceau = ordre[k:k + lot]
        ctx = [contexte_impose(fmt, ds[i]["systeme"], ds[i]["utilisateur"], "") for i in morceau]
        lp = logits_derniere_position(modele, ctx, pad)
        for i, ligne, c in zip(morceau, lp, ctx):
            a, b = float(ligne[oui]), float(ligne[non])
            t["logprob_oui"][i], t["logprob_non"][i] = a, b
            t["score"][i] = probabilite_oui(a, b)
            t["masse"][i] = min(1.0, float(np.exp(a) + np.exp(b)))
            t["jetons_contexte"][i] = len(c)
    t["anomalie"] = t["masse"] < masse_min
    return t


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, autoriser_depot_sale: bool = False,
             empreinte_citee: str | None = None) -> dict:
    racine = Path(racine)
    manquantes = [k for k in CLES if k not in config]
    if manquantes:
        raise GardeArret(f"configuration du juge incomplète : {manquantes}")
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("juge réel sans préenregistrement : R1 interdit de lancer")
    if prereg is not None:
        from ..harnais.validation_reelle import exiger_code_cite

        attendue = empreinte_citee or empreinte_config(config)
        if CONFIG_CITEE.format(config["juge"]["nom"], attendue) not in Path(prereg).read_text(encoding="utf-8"):
            raise GardeArret(f"{prereg} ne cite pas la configuration du juge {config['juge']['nom']} {attendue[:12]}")
        exiger_code_cite(racine, Path(prereg))
    identite = charger_identite(config["chemin_scores"], config["scores_sha256"])
    sha_id = empreinte_identite(identite)
    if config["identite_sha256"] is not None and sha_id != config["identite_sha256"]:
        raise GardeArret(f"identité des actions {sha_id[:12]} ≠ identité citée {config['identite_sha256'][:12]}")
    lignes = charger_textes_alignes(config["chemin_textes"], identite, config["textes_sha256"])
    invite = charger_invite_juge(config["chemin_invite"], config["invite_sha256"])
    taches = {t["identifiant"]: t for t in charger_taches(config["chemin_taches"])}
    if config["taches_sha256"] is not None and verifier(config["chemin_taches"]) != config["taches_sha256"]:
        raise GardeArret("tâches : empreinte ≠ empreinte citée")
    absentes = sorted({x["tache"] for x in lignes} - set(taches))
    if absentes:
        raise GardeArret(f"tâches absentes du fichier des tâches : {absentes[:5]}")
    chemin_m, _ = creer_manifeste(racine, run_id, config, ["juge"], decisif=prereg is not None, prereg=prereg,
                                  autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    etat = {"etape": "chargement", "identite_sha256": sha_id}
    debut = time.perf_counter()
    try:
        from ..harnais.modeles import regler_determinisme

        reel = config["mode"] == "reel"
        reglages = regler_determinisme(config["fils"], "cuda" if reel else "cpu")
        modele, fmt = _modele(config)
        oui, non = jetons_oui_non(fmt.tok) if reel else jetons_jouet(fmt.tok)
        sortie = {k: np.asarray(identite[k]) for k in CLES_IDENTITE}
        for bras in BRAS:
            etat["etape"] = f"notation ({bras})"
            t = noter(modele, fmt, demandes(lignes, taches, invite, bras), oui, non, int(config["lot"]),
                      float(config["masse_min"]))
            suffixe = "" if bras == "specialise" else "_generique"
            for k, v in t.items():
                if k == "jetons_contexte" and suffixe:
                    continue
                sortie[k + suffixe] = v
            progres(etape="juge", bras=bras, actions=len(lignes), anomalies=int(t["anomalie"].sum()))
        etat["etape"] = "écriture"
        dossier = racine / "donnees" / run_id
        dossier.mkdir(parents=True, exist_ok=False)
        p = dossier / f"{config['nom_sortie']}.npz"
        with open(p, "wb") as f:
            np.savez(f, **sortie)
        sha = sceller(p)
        resultat = {"fichier": p.name, "sha256": sha, "identite_sha256": sha_id, "invite_sha256": invite["sha256"],
                    "contexte": CONTEXTE, "bras_principal": "specialise", "juge": config["juge"],
                    "jetons_reponse": {"oui": int(oui), "non": int(non)},
                    "anomalies": {"specialise": int(sortie["anomalie"].sum()),
                                  "generique": int(sortie["anomalie_generique"].sum())},
                    "reglages": reglages, "empreintes_modele": _empreintes_modele(config),
                    "duree_s": round(time.perf_counter() - debut, 1)}
        ecrire_resultat(racine, chemin_m, "juge-actions", resultat)
        return resultat
    except Exception as e:
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _modele(config: dict):
    from ..environnements.lancer_pilote_a import charger_modele_et_format

    if config["mode"] == "jouet":
        return charger_modele_et_format(config["juge"], "jouet", int(config["juge"].get("graine_jouet", 0)))
    return charger_modele_et_format(config["juge"], "reel", 0)


def _empreintes_modele(config: dict):
    """Empreintes des fichiers du modèle juge en cache (descriptif ; un échec est consigné tel quel, jamais remplacé)."""
    if config["mode"] != "reel":
        return None
    from ..harnais.modeles import empreintes_fichiers_modele

    try:
        return empreintes_fichiers_modele(config["juge"]["modele"], config["juge"]["revision"])
    except Exception as e:
        return {"non_lues": motif_d_arret(e)}


def progres(**champs) -> None:
    from datetime import datetime, timezone

    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={v}" for k, v in champs.items()), file=sys.stderr, flush=True)


def config_pour_run(config: dict, racine: Path, run_source: str) -> dict:
    """Configuration complétée pour un run source connu après coup (R4) : chemins et empreintes lus dans son résumé."""
    c = dict(config)
    resume_p = Path(racine) / "diag" / run_source / "resume.json"
    verifier(resume_p)
    resume = json.loads(resume_p.read_text(encoding="utf-8"))["resultat"]
    d = Path("donnees") / run_source
    c.update({"chemin_textes": str(d / "textes-actions-p3.jsonl"), "textes_sha256": resume["textes_sha256"],
              "chemin_scores": str(d / "scores-p3.npz"), "scores_sha256": resume["scores_sha256"],
              "taches_sha256": resume["taches_sha256"], "run_source": run_source})
    return c


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--run-source", default=None)
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    citee = empreinte_config(config)
    if a.run_source:
        config = config_pour_run(config, Path("."), a.run_source)
    r = executer(config, Path("."), a.run_id, a.prereg, empreinte_citee=citee)
    print(json.dumps({"fichier": r["fichier"], "sha256": r["sha256"], "anomalies": r["anomalies"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
