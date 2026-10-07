"""Revalidation courte de l'équivalence sur le domaine du pilote (T0.5).

P-007 retenue par Lazar, lue comme le plan (a) plus une revalidation courte avant le pilote (R-085) ; remarque CL-3 de
la contre-lecture 1 du pilote. Préenregistrement : `prereg/T0.5-revalidation-equivalence-pilote-v1.md`.

Deux bras de noyau d'attention (« defaut », « math ») jouent les mêmes épisodes : agent honnête, tâches d'entraînement
de l'extraction scellée (jamais une tâche d'évaluation du pilote), mêmes graines, demi-précision, garde d'équivalence
différée. Tout est consigné, puis la lecture gelée s'applique (`lire_bras`, `choisir_noyau`). Pour chaque bras :
- Rk-1 : maximum, sur les actions échantillonnées et les couches, du 99e centile par action ≤ la tolérance ;
- Rk-2 : contrôle négatif de la production (règle de T0.4 v3 : 95 % des actions comparables, au moins 10) ;
- Rk-3 : repère de précision (passe unique en demi-précision au noyau du bras, contre passe unique en simple précision
  au noyau « math ») : deux fois son 99e centile ≤ la tolérance, à chaque couche ;
- Rk-4 : rejeu du lot 0 dans le processus : empreintes identiques ;
- Rk-5 : domaine couvert : assez d'actions comparées, une action remplie à gauche, et le plus long contexte comparé
  atteint une part fixée du plus long contexte joué dans le bras (mêmes réglages que le pilote : son domaine).
Règle gelée : « defaut » s'il est conforme ; sinon « math » s'il est conforme ; sinon nœud (aucun noyau retenu).

Garde restreinte à la zone générée (descriptive, lecture gelée) : le 99e centile de l'action entière ne voit pas un
écart confiné à moins d'environ 1 % de ses positions (limite déclarée de T0.4 v3) ; aux contextes longs du pilote, ce
cas peut être fréquent. Chaque bras mesure donc aussi le 99e centile de la seule zone générée et son contrôle négatif
(maximum de l'écart décalé dans la zone générée). Si aucun bras n'est conforme, et qu'un bras ne manque que le contrôle
négatif de l'action entière alors que sa garde restreinte est conforme, le nœud porte une proposition prête : passer la
garde du pilote à la zone générée (décision de Lazar : la garde validée change).

Mode « jouet » : modèle jouet sur processeur, mêmes chaînes et mêmes gardes (tests et répétitions).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import signal
import sys
import time
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.activations import ecarts_par_jeton, passe_unique
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import (ENTROPIE_CITEE, exiger_code_cite, exiger_code_importe_sous,
                                         exiger_memoire_carte, noyau)
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat, generateur
from ..scellement import verifier
from .lancer_pilote_a import charger_modele_et_format
from .pilote_a import CLES_CONFIG, charger_taches, exiger_config, jouer_pilote

BRAS = ("defaut", "math")
CLES_REVALIDATION = CLES_CONFIG + ("agent", "mode", "fils", "bras", "nombre_taches", "episodes_repere",
                                   "actions_min_comparees", "part_min_contexte_couvert", "memoire_carte_min_gio",
                                   "duree_max_s")
CONFIG_CITEE = re.compile(r"Configuration de la revalidation \(empreinte canonique\) : `([0-9a-f]{64})`")
TACHES_CITEES = re.compile(r"Tâches d'entraînement : `([0-9a-f]{64})`")
COMMANDE = "python -m controle_ia.environnements.revalider_pilote_a"


def _sha_fichier(chemin) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def exiger_config_revalidation(config: dict) -> None:
    exiger_config(config, CLES_REVALIDATION)
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    if list(config["bras"]) != list(BRAS):
        raise GardeArret(f"bras {config['bras']!r} : {list(BRAS)} attendus, dans cet ordre (règle de choix)")
    if config["statistique_equivalence"] != "q99" or config["episodes_par_tache"] != 1:
        raise GardeArret("revalidation : 99e centile (garde de production de T0.4 v3) et un épisode par tâche")
    if not all(0 <= k < config["nombre_taches"] for k in config["episodes_repere"]):
        raise GardeArret("épisodes du repère hors du plan")


def taches_d_entrainement(chemin_entrainement, chemin_evaluation, n: int) -> list[dict]:
    """Les `n` premières tâches d'entraînement de l'extraction scellée ; arrêt si l'une est aussi une tâche
    d'évaluation, ou s'il en manque (R1 : aucune tâche du pilote n'est jouée avant son préenregistrement)."""
    entrainement = charger_taches(chemin_entrainement)
    evaluation = {t["identifiant"] for t in charger_taches(chemin_evaluation)}
    communes = sorted({t["identifiant"] for t in entrainement} & evaluation)
    if communes:
        raise GardeArret(f"tâches d'entraînement aussi tâches d'évaluation : {communes}")
    if len(entrainement) < n:
        raise GardeArret(f"{len(entrainement)} tâches d'entraînement, {n} attendues")
    return entrainement[:n]


def exiger_citations(prereg: Path, config: dict, sha_taches: str) -> int:
    """La configuration (empreinte canonique), les tâches et l'entropie sont celles que cite le préenregistrement."""
    texte = Path(prereg).read_text(encoding="utf-8")
    c, t, e = CONFIG_CITEE.search(texte), TACHES_CITEES.search(texte), ENTROPIE_CITEE.search(texte)
    if not (c and t and e):
        raise GardeArret(f"{prereg} ne cite pas la configuration, les tâches ou l'entropie de la revalidation")
    if hashlib.sha256(config_canonique(config)).hexdigest() != c.group(1):
        raise GardeArret("configuration ≠ configuration citée")
    if sha_taches != t.group(1):
        raise GardeArret(f"tâches {sha_taches[:12]} ≠ tâches citées {t.group(1)[:12]}")
    return int(e.group(1))


def _infini_si_nan(x) -> float:
    return float("inf") if x is None or x != x else float(x)


def domaine_et_garde(fiches: list[dict]) -> dict:
    """Grandeur de la garde (Rk-1) et domaine couvert (Rk-5), sur les actions échantillonnées de tous les épisodes."""
    q99, maxima, contextes, remplies, comparees = [], [], [], 0, 0
    joues = [int(a["debut"]) for f in fiches for a in f["actions"]]
    for f in fiches:
        eq = f["equivalence"]
        for cle, par_couche in eq["ecarts_q99"].items():
            comparees += 1
            q99 += [_infini_si_nan(v) for v in par_couche.values()]
            maxima += [_infini_si_nan(v) for v in eq["ecarts"][cle].values()]
            contextes.append(int(eq["longueurs_contexte"][cle]))
            remplies += int(eq["lignes"][cle]["remplissage"] > 0)
    return {"actions_comparees": comparees, "q99_max": max(q99) if q99 else None,
            "ecart_max": max(maxima) if maxima else None,
            "contexte_max": max(contextes, default=0), "contexte_max_joue": max(joues, default=0),
            "actions_remplies": remplies}


def garde_zone_generee(fiches: list[dict], tolerance: float, positions_min: int) -> dict:
    """Garde restreinte à la zone générée : 99e centile des écarts de la seule zone générée (par action et par
    couche) et contrôle négatif sur le maximum de l'écart décalé de cette zone ; part des actions comparées dont la
    zone générée compte moins de 1 % des positions (là où la garde de l'action entière est aveugle par construction)."""
    q99g, parts, comparables, passent = [], [], 0, 0
    for f in fiches:
        eq = f["equivalence"]
        for cle in eq["ecarts_q99"]:
            n = eq["positions_capturees"][cle]
            parts.append((n - eq["longueurs_contexte"][cle]) / n if n else 0.0)
            for prof in eq["profils"][cle].values():
                if prof["generee"]["jetons"]:
                    q99g.append(_infini_si_nan(prof["generee"]["q99"]))
            zone = eq["controle_negatif_zone_generee"].get(cle)
            if zone is None or min(v["positions"] for v in zone.values()) < positions_min:
                continue
            comparables += 1
            if min(float("-inf") if v["max"] != v["max"] else v["max"] for v in zone.values()) > tolerance:
                passent += 1
    return {"q99_generee_max": max(q99g) if q99g else None, "comparables": comparables, "passent": passent,
            "fraction": passent / comparables if comparables else None,
            "part_zone_generee_sous_1pc": sum(x < 0.01 for x in parts) / len(parts) if parts else None}


def lire_bras(mesures: dict, controle_negatif: dict, repere: dict | None, rejeu_identique: bool | None,
              config: dict, panne: str | None = None, zone_generee: dict | None = None) -> dict:
    """Lecture gelée d'un bras (Rk-1 à Rk-5). Un bras en panne (mémoire) ou dont une mesure manque est non conforme."""
    tol = config["tolerance_equivalence"]
    if panne is not None:
        return {"conforme": False, "panne": panne}
    r1 = mesures["q99_max"] is not None and mesures["q99_max"] <= tol
    r2 = controle_negatif["lecture"]
    r3 = repere is not None and all(2 * _infini_si_nan(v["q99"]) <= tol for v in repere.values())
    r4 = bool(rejeu_identique)
    r5 = (mesures["actions_comparees"] >= config["actions_min_comparees"] and mesures["actions_remplies"] > 0
          and mesures["contexte_max"] >= config["part_min_contexte_couvert"] * mesures["contexte_max_joue"])
    # R4 (symétrie) : un bras dont tous les écarts sont exactement nuls, génération et passe unique confondues au bit
    # près partout, est trop propre : réserve et audit, sans effet sur la conformité (T0.4 v3, P9)
    lecture = {"R1_garde_saine": r1, "R2_controle_negatif": r2, "R3_seuil_fonde": r3, "R4_rejeu": r4,
               "R5_domaine_couvert": r5, "conforme": bool(r1 and r2 == "conforme" and r3 and r4 and r5),
               "audit_R4_ecarts_tous_nuls": mesures["ecart_max"] == 0}
    if zone_generee is not None:
        zg = zone_generee
        g1 = zg["q99_generee_max"] is not None and zg["q99_generee_max"] <= tol
        g2 = (zg["comparables"] >= config["actions_min_controle_negatif"]
              and zg["fraction"] >= config["fraction_min_controle_negatif"])
        lecture["garde_zone_generee_conforme"] = bool(g1 and g2)
        # seul manque : le contrôle négatif de l'action entière ; la garde restreinte est conforme
        lecture["aveugle_action_entiere_seulement"] = bool(r1 and r2 != "conforme" and r3 and r4 and r5 and g1 and g2)
    return lecture


def choisir_noyau(lectures: dict) -> str | None:
    """Règle gelée : le premier bras conforme, dans l'ordre (« defaut », puis « math ») ; None : nœud."""
    for b in BRAS:
        if lectures.get(b, {}).get("conforme"):
            return b
    return None


def statistiques_repere(bas: dict, ref: dict, couches) -> dict:
    """Écart par jeton entre activations de demi-précision (`bas`) et de référence (`ref`), mêmes transcriptions."""
    sortie = {}
    for c in couches:
        e = np.concatenate([ecarts_par_jeton(bas[k][c], ref[k][c]) for k in sorted(ref)])
        sortie[str(c)] = {"jetons": int(e.size), "q50": float(np.quantile(e, 0.5)), "q99": float(np.quantile(e, 0.99)),
                          "max": float(e.max())}
    return sortie


def _activations(modele, transcriptions: dict, couches) -> dict:
    return {k: {c: a.astype(np.float32) for c, a in passe_unique(modele, ids, couches).items()}
            for k, ids in transcriptions.items()}


def _empreintes_rejeu(fiches: list[dict]) -> dict:
    return {f["episode"]: {"empreintes": f["empreintes"], "captures": f["equivalence"].get("empreintes_capture")}
            for f in fiches}


def _modele_reference(config: dict, graine_jouet: int):
    """Modèle de référence du repère : simple précision (le même modèle jouet, ou la révision figée du 8B)."""
    if config["mode"] == "jouet":  # poids arrondis en demi-précision puis convertis sans perte, comme ceux du 8B
        m, _ = charger_modele_et_format(config["agent"], "jouet", graine_jouet)
        return m.to(torch.bfloat16).to(torch.float32).eval()
    from ..harnais.modeles import charger_modele

    m, _ = charger_modele(config["agent"]["modele"], config["agent"]["revision"], "float32", "cuda", "sdpa")
    return m


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_entrainement: str,
             chemin_evaluation: str, autoriser_depot_sale: bool = False, entropie_essai: int | None = None) -> dict:
    """`entropie_essai` : entropie fixée d'une répétition sans préenregistrement (tests) ; refusée avec un
    préenregistrement, qui cite la sienne."""
    racine = Path(racine)
    exiger_config_revalidation(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("revalidation réelle sans préenregistrement : R1 interdit de lancer")
    if prereg is not None and entropie_essai is not None:
        raise GardeArret("entropie d'essai refusée avec un préenregistrement : seule l'entropie citée vaut")
    verifier(chemin_entrainement)
    verifier(chemin_evaluation)
    sha_taches = _sha_fichier(chemin_entrainement)
    entropie = entropie_essai
    if prereg is not None:
        exiger_code_cite(racine, Path(prereg))
        exiger_code_importe_sous(racine)
        entropie = exiger_citations(Path(prereg), config, sha_taches)
    taches = taches_d_entrainement(chemin_entrainement, chemin_evaluation, config["nombre_taches"])
    plan = [(f"{t['identifiant']}/e0", t) for t in taches]
    ids_episodes = [e for e, _ in plan]
    config_m = dict(config, taches_entrainement=chemin_entrainement, taches_entrainement_sha256=sha_taches,
                    taches_evaluation=chemin_evaluation, taches_evaluation_sha256=_sha_fichier(chemin_evaluation))
    chemin_m, manifeste = creer_manifeste(racine, run_id, config_m, ids_episodes + ["modele-jouet"], entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale,
                                          commande=f"{COMMANDE} --run-id {run_id}")
    etat = {"etape": "mise en place"}
    debut = time.perf_counter()
    try:
        return _executer_apres_manifeste(config, racine, chemin_m, manifeste, plan, ids_episodes, etat)
    except Exception as e:          # garde, panne, signal TERM : consigné, puis propagé
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": f"{type(e).__name__}: {e}",
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        raise


def _executer_apres_manifeste(config, racine, chemin_m, manifeste, plan, ids_episodes, etat) -> dict:
    g = manifeste["graines"]
    from ..harnais.modeles import regler_determinisme

    reel = config["mode"] == "reel"
    reglages = regler_determinisme(config["fils"], "cuda" if reel else "cpu")
    if reel:
        exiger_memoire_carte(config["memoire_carte_min_gio"])
    graine_jouet = graine_entiere(g["modele-jouet"])
    modele, fmt = charger_modele_et_format(config["agent"], config["mode"], graine_jouet)
    if not reel:
        modele = modele.to(torch.bfloat16).eval()
    echeance = time.perf_counter() + float(config["duree_max_s"])
    repere_de = {ids_episodes[k] for k in config["episodes_repere"]}
    resultats, transcriptions, acts_bas = {}, {}, {}
    for bras in config["bras"]:
        etat["etape"] = f"bras {bras}"
        r = {"noyau": bras}
        try:
            if reel:
                torch.cuda.reset_peak_memory_stats()
            chrono: dict = {}
            debut = time.perf_counter()
            with noyau(bras):
                fiches, _, cn = jouer_pilote(modele, fmt, plan, {e: generateur(g[e]) for e in ids_episodes}, config,
                                             garder_vecteurs=False, echeance=echeance, garde="differee",
                                             exiger_controle_negatif=False, chrono=chrono, transcriptions_de=repere_de)
                r["duree_s"] = time.perf_counter() - debut
                lot0 = plan[:config["lot"]]
                rejeu, _, _ = jouer_pilote(modele, fmt, lot0, {e: generateur(g[e]) for e, _ in lot0}, config,
                                           garder_vecteurs=False, echeance=echeance, garde="differee",
                                           exiger_controle_negatif=False)
                kept = {f"{bras}|{f['episode']}|{tr['agent']}": tr["ids"] for f in fiches
                        for tr in f.get("transcriptions", [])}
                acts_bas[bras] = _activations(modele, kept, config["couches"])
            transcriptions.update(kept)
            premier = {e: v for e, v in _empreintes_rejeu(fiches).items() if e in dict(lot0)}
            r.update({"fiches": fiches, "controle_negatif": cn, "chrono": chrono,
                      "mesures": domaine_et_garde(fiches),
                      "rejeu_identique": _empreintes_rejeu(rejeu) == premier,
                      "memoire_pic_go": (torch.cuda.max_memory_allocated() / 1e9) if reel else None})
        except torch.cuda.OutOfMemoryError as exc:  # panne de mémoire signalée : consignée, bras non concluant
            r["panne"] = f"mémoire : {exc}"[:500]
        resultats[bras] = r
    del modele
    if reel:
        torch.cuda.empty_cache()
    etat["etape"] = "repère de précision"
    reference = _modele_reference(config, graine_jouet)
    with noyau("math"):
        acts_ref = _activations(reference, transcriptions, config["couches"])
    lectures = {}
    for bras, r in resultats.items():
        if "panne" in r:
            lectures[bras] = lire_bras({}, {}, None, None, config, panne=r["panne"])
            continue
        ref = {k: v for k, v in acts_ref.items() if k.startswith(f"{bras}|")}
        r["repere"] = statistiques_repere(acts_bas[bras], ref, config["couches"])
        r["zone_generee"] = garde_zone_generee(r["fiches"], config["tolerance_equivalence"],
                                               config["positions_min_controle_negatif"])
        lectures[bras] = lire_bras(r["mesures"], r["controle_negatif"], r["repere"], r["rejeu_identique"], config,
                                   zone_generee=r["zone_generee"])
    noyau_retenu = choisir_noyau(lectures)
    proposition = None
    if noyau_retenu is None:
        prets = [b for b in BRAS if lectures.get(b, {}).get("aveugle_action_entiere_seulement")]
        if prets:
            proposition = {"garde": "zone générée", "noyau": prets[0]}
    resume = {"lectures": lectures, "noyau_retenu": noyau_retenu, "noeud": noyau_retenu is None,
              "proposition_au_noeud": proposition, "reglages": reglages,
              "bras": {b: {k: v for k, v in r.items() if k != "fiches"} for b, r in resultats.items()}}
    ecrire_resultat(racine, chemin_m, "episodes", {b: r.get("fiches", []) for b, r in resultats.items()})
    ecrire_resultat(racine, chemin_m, "resume", resume)
    return resume


def _signal_term(signum, frame):
    raise GardeArret("signal TERM reçu (délai externe du run ou plafond de l'amorce) : arrêt consigné")


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--entrainement", required=True)
    ap.add_argument("--evaluation", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg")
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, _signal_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    resume = executer(config, Path("."), a.run_id, a.prereg, a.entrainement, a.evaluation)
    print(json.dumps({"noyau_retenu": resume["noyau_retenu"], "lectures": resume["lectures"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
