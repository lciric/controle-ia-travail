"""R1 relancé sur la table de tokenisation version 4 (relance v4 de R1 ; addendum `prereg/R1-addendum-relance-v4.md`).

Version 4 du rejeu, sous un nom nouveau (R12) : `rejeu_activations_v3.py`, cité par l'addendum v3, n'est pas modifié ;
la v2 et la v1 non plus. Tout ce qui n'est pas nommé ici est la v3 (et, par elle, la v2 et la v1) : gardes de la
configuration, configuration citée, parent cité, commit du code cité, tolérance de fidélité, contrôle de fidélité,
contrôle négatif (`rejeu_activations_v3.controle_negatif`, importé tel quel : il applique déjà les formes anciennes et
« identifiants »), règle de repli, couches, agrégats, passe unique, définition de `fidele`, sorties (mêmes fichiers,
mêmes tableaux, mêmes noms, mêmes formes), verdicts. Ce que la v4 change, et rien d'autre (chaque écart marqué `# v4`) :

- **Table version 4** (`resolution_graine_lot_v2.charger_table_v4` : version 4, formes de la v3, aucun doublon, sceau) ;
  une table de version 1, 2 ou 3 est refusée, sa version dans le motif. **Empreinte de la table** : soit citée (64
  hexadécimaux), soit la valeur `TABLE_EN_SESSION` (« construite-en-session ») : la table v4 est construite dans la même
  session que le rejeu, son empreinte ne peut pas être citée d'avance (écart déclaré par l'addendum v4) ; elle est alors
  lue au chemin cité, scellée, et **revérifiée tout entière par l'oracle de P3 au chargement** (comme en v3), puis son
  empreinte est écrite au résultat (`tokenisation.table_sha256`).
- **Règle A étendue** (`classer_episodes_v4`) : la table doit couvrir **exactement** les épisodes dont la trajectoire de
  base diffère de P3 : les signalés (conformes en longueur, trajectoire différente : règle de la v3) **et** les non
  entièrement conformes en longueur ; arrêt « echec » si un manque ou un en trop. Chaque correction (les deux
  ensembles) est appliquée et revérifiée par l'empreinte de P3 ; un épisode corrigé devient « trajectoire identique »,
  toutes ses actions conformes et en contexte exact.
- **Règle B inchangée** pour les signalés (entrées `non_resolu` parmi les conformes en longueur, au plus
  `seuil_non_conformes`). Les entrées `non_resolu` parmi les non conformes en longueur (cibles v4 non retrouvées) sont
  **déclarées** (`episodes_non_retrouves_v4`) et gardent exactement le traitement de la v3 (préfixe conforme en
  `contexte_conforme`, actions jugées par la tolérance) : elles ne comptent pas dans la règle B, qui ne les a jamais
  comptées.
- **Sortie** (`rejeu-activations.json`, clé `tokenisation`) : `version_table` = 4, `addendum` = l'addendum v4,
  `non_conformes`, `episodes_non_retrouves_v4`, `actions_non_retrouvees_v4`, `table_empreinte_citee` (vrai ou faux) ;
  méthodes de résolution comme en v3.
"""
from __future__ import annotations

import argparse
import json
import re
import signal
import sys
import time
from pathlib import Path

import numpy as np

from ..environnements.invites import charger_invite
from ..environnements.pilote_a import charger_taches, tache_de
from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.activations import agreger, passe_unique
from ..manifeste import creer_manifeste, ecrire_resultat, generateur
from ..scellement import sceller, verifier
from ..sondes.familles import SondeMahalanobis
from . import rejeu_activations_v2 as v2
from . import resolution_graine_v1 as rg
from . import resolution_tokenisation_v1 as rt
from .alignement_v1 import CLES_IDENTITE, charger_identite, charger_textes_alignes, empreinte_identite
from .resolution_tokenisation_v1 import table_des_octets

v1 = v2.v1
from . import rejeu_activations_v3 as v3
from . import resolution_graine_lot_v2 as rv

COMMANDE = "python -m controle_ia.runs_nuit.rejeu_activations_v4"
ADDENDUM = "prereg/R1-addendum-relance-v4.md"
TABLE_EN_SESSION = "construite-en-session"
CLES = v2.CLES
CONFIG_CITEE = v2.CONFIG_CITEE
empreinte_config = v2.empreinte_config
progres = v2.progres
VERSION_TABLE = rv.VERSION_TABLE_V4
CORRIGEES = rg.CORRIGEES_V3
appliquer_entree = rg.appliquer_entree_v3
METHODES_RESOLUTION = ("v1", "v2", "identifiants", "aucune")
EMPREINTE_HEX = re.compile(r"^[0-9a-f]{64}$")


methode_resolution = v3.methode_resolution
controle_negatif = v3.controle_negatif


def exiger_config(config: dict) -> None:
    """Gardes de la v2 (et de la v1), puis : empreinte de la table obligatoire dans tous les modes, 64 hexadécimaux ou
    `TABLE_EN_SESSION` (table construite dans la session, revérifiée par l'oracle de P3 au chargement)."""        # v4
    v2.exiger_config(config)
    sha = config["table_tokenisation_sha256"]
    if sha != TABLE_EN_SESSION and (not isinstance(sha, str) or not EMPREINTE_HEX.fullmatch(sha)):
        raise GardeArret("table_tokenisation_sha256 : empreinte sha256 de la table version 4 (64 hexadécimaux) ou "
                         f"« {TABLE_EN_SESSION} », obligatoire, dans tous les modes")


def charger_table(chemin, sha_attendue: str) -> dict:
    """Table version 4 scellée (`resolution_graine_lot_v2.charger_table_v4`) ; empreinte citée vérifiée, sauf
    `TABLE_EN_SESSION` ; une table de version 1, 2 ou 3 est refusée, sa version dans le motif."""                  # v4
    if sha_attendue != TABLE_EN_SESSION and (not isinstance(sha_attendue, str)
                                             or not EMPREINTE_HEX.fullmatch(sha_attendue)):
        raise GardeArret("table de tokenisation : empreinte citée absente")
    return rv.charger_table_v4(chemin, None if sha_attendue == TABLE_EN_SESSION else sha_attendue)


def classer_episodes_v4(signales: list[str], non_conformes: list[str], table: dict,
                        seuil: int) -> tuple[dict, list[str], list[str]]:
    """Règle A étendue : la table couvre exactement `signales` ∪ `non_conformes` (épisodes à trajectoire de base
    différente de P3) ; rend ({épisode : entrée à appliquer}, non résolus de la règle B (parmi les signalés), non
    retrouvés v4 (parmi les non conformes)). Arrêt si un manque, un en trop, un épisode dans les deux ensembles, ou si les
    non résolus de la règle B dépassent `seuil` (message de la v3)."""                                              # v4
    if set(signales) & set(non_conformes):
        raise GardeArret("épisode à la fois signalé et non conforme en longueur : classement incohérent")
    par_ep = {e["episode"]: e for e in table["episodes"]}
    attendus = list(signales) + list(non_conformes)
    manquants = [e for e in attendus if e not in par_ep]
    en_trop = sorted(set(par_ep) - set(attendus))
    if manquants or en_trop:
        raise GardeArret(f"table de tokenisation non conforme au run : manquants {manquants[:3]} ({len(manquants)}), "
                         f"en trop {en_trop[:3]} ({len(en_trop)})")
    corriger = {e: par_ep[e] for e in attendus if par_ep[e]["methode"] != "non_resolu"}
    non_resolus = [e for e in signales if par_ep[e]["methode"] == "non_resolu"]
    non_retrouves = [e for e in non_conformes if par_ep[e]["methode"] == "non_resolu"]
    if len(non_resolus) > int(seuil):
        raise GardeArret(f"{len(non_resolus)} épisode(s) conformes en longueur restés différents de P3 après la table "
                         f"(au-delà du seuil de {seuil}) : {non_resolus[:3]} : reconstruction non fidèle, rien n'est versé")
    return corriger, non_resolus, non_retrouves


def verifier_table_au_chargement(table: dict, fmt, lignes: list, par_episode: dict, jetons: list, jetons_notes: list,
                                 fiches: dict, taches: dict, consignes, guide: str, T: int) -> int:
    """Revérification de toute la table par l'empreinte de P3 (voir le module) ; rend le nombre de corrections
    vérifiées. Arrêt, avec la raison, sinon."""
    from ..premier_test_ia.conditions import environnement

    if table.get("version") != VERSION_TABLE:
        raise GardeArret(f"table de tokenisation : version {table.get('version')!r} ≠ {VERSION_TABLE}")
    for ent in table["episodes"]:
        e = ent["episode"]
        if e not in par_episode:
            raise GardeArret(f"table de tokenisation : épisode {e} absent du run source")
        if e not in fiches:
            raise GardeArret(f"table de tokenisation : épisode {e} absent des fiches de P3")
        if ent.get("trajectoire_p3") != fiches[e]["trajectoire"]:
            raise GardeArret(f"table de tokenisation : {e} : empreinte de P3 citée par l'entrée "
                             f"({str(ent.get('trajectoire_p3'))[:12]}) ≠ fiches de P3 : table d'un autre run ou falsifiée")

    def contexte(e):
        rs = par_episode[e]
        x0 = lignes[rs[0]]
        env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
        return env, [lignes[r] for r in rs], [jetons[r] for r in rs], [jetons_notes[r] for r in rs], T

    n = rg.verifier_entrees_v3(table["episodes"], fmt, contexte, fiches)
    comptes = table.get("comptes") or {}
    attendu = comptes.get("identiques_apres_table", 0) - comptes.get("identiques_base", 0)
    if n != attendu:
        raise GardeArret(f"table de tokenisation : {n} correction(s) vérifiée(s) ≠ {attendu} selon les comptes de la table")
    return n


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, autoriser_depot_sale: bool = False,
             entropie_essai: int | None = None) -> dict:
    """Copie de `rejeu_activations_v3.executer` ; écarts de la v3 marqués `# v3`, de la v4 `# v4` : table version 4
    (empreinte citée ou construite en session), commande du manifeste."""
    racine = Path(racine)
    exiger_config(config)                                                                              # v3
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("rejeu réel sans préenregistrement : R1 interdit de lancer")
    entropie = entropie_essai
    if config["chemin_prereg_parent"]:
        sha = verifier(racine / config["chemin_prereg_parent"])
        if config["prereg_parent_sha256"] is not None and sha != config["prereg_parent_sha256"]:
            raise GardeArret(f"préenregistrement parent {config['chemin_prereg_parent']} : empreinte {sha[:12]} ≠ "
                             f"empreinte citée {config['prereg_parent_sha256'][:12]}")
    if prereg is not None:
        from ..harnais.validation_reelle import ENTROPIE_CITEE, exiger_code_cite

        texte = Path(prereg).read_text(encoding="utf-8")
        attendue = empreinte_config(config)
        if CONFIG_CITEE.format(attendue) not in texte:
            raise GardeArret(f"{prereg} ne cite pas la configuration du rejeu {attendue[:12]}")
        if config["chemin_prereg_parent"] and config["prereg_parent_sha256"] \
                and config["prereg_parent_sha256"] not in texte:
            raise GardeArret(f"{prereg} ne cite pas l'empreinte du préenregistrement parent")
        e = ENTROPIE_CITEE.search(texte)
        if not e:
            raise GardeArret(f"{prereg} ne cite pas l'entropie")
        entropie = int(e.group(1))
        exiger_code_cite(racine, Path(prereg))
    identite = charger_identite(config["chemin_scores"], config["scores_sha256"])
    sha_id = empreinte_identite(identite)
    if config["identite_sha256"] is not None and sha_id != config["identite_sha256"]:
        raise GardeArret(f"identité des actions {sha_id[:12]} ≠ identité citée {config['identite_sha256'][:12]}")
    lignes = charger_textes_alignes(config["chemin_textes"], identite, config["textes_sha256"])
    table = charger_table(config["chemin_table_tokenisation"], config["table_tokenisation_sha256"])     # v3
    for k in ("textes_sha256", "fiches_sha256", "scores_sha256"):
        if config[k] is not None and table.get(k) != config[k]:
            raise GardeArret(f"table de tokenisation calculée sur d'autres pièces ({k} : {str(table.get(k))[:12]})")
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, ["fidelite", "modele-jouet-inutilise"],
                                          entropie=entropie, decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)        # v3
    etat = {"etape": "chargement", "identite_sha256": sha_id}
    debut = time.perf_counter()
    try:
        return _executer(config, racine, run_id, chemin_m, manifeste, identite, lignes, table, etat, debut)
    except Exception as e:
        # verdict au format du n° 330 : « non conforme » si le contrôle de fidélité, le contrôle négatif ou la règle B
        # (non résolus au-delà du seuil) a échoué, « echec » pour tout autre arrêt (table falsifiée comprise)
        etat["verdict_fidelite"] = ("non conforme" if (etat.get("fidelite_echantillon") or {}).get("lecture") == "contraire"
                                    or (etat.get("controle_negatif") or {}).get("lecture") == "non discriminant"
                                    or etat.get("regle_b") == "au-delà du seuil"
                                    else "echec")
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "verdict_fidelite": etat["verdict_fidelite"],
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _executer(config, racine, run_id, chemin_m, manifeste, identite, lignes, table, etat, debut) -> dict:
    """Copie de `rejeu_activations_v3._executer` ; écarts de la v4 marqués `# v4` : règle A étendue aux non conformes
    en longueur (`classer_episodes_v4`), non retrouvés déclarés, clés ajoutées à la sortie."""
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import noyau
    from ..premier_test_ia.conditions import charger_consignes, environnement
    from ..premier_test_ia.figees import lire_sondes
    from ..premier_test_ia.notation import Notation

    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    reglages = regler_determinisme(config["fils"], appareil)
    taches = {t["identifiant"]: t for t in charger_taches(config["chemin_taches"])}
    if config["taches_sha256"] is not None and verifier(config["chemin_taches"]) != config["taches_sha256"]:
        raise GardeArret("tâches : empreinte ≠ empreinte citée")
    consignes = charger_consignes(config["chemin_consignes"], config["consignes_sha256"])
    sondes, _, sha_sondes = lire_sondes(config["chemin_sondes_legeres"], config["sondes_legeres_sha256"])
    sondes = [s for s in sondes if not isinstance(s, SondeMahalanobis) and int(s.couche) in config["couches"]]
    noms_src = [str(x) for x in identite["noms_sondes"].tolist()]
    index = {n: k for k, n in enumerate(noms_src)}
    sondes = [s for s in sondes if s.nom in index]
    if not sondes:
        raise GardeArret("aucune sonde légère commune au fichier des scores : contrôle de fidélité impossible")
    notation = Notation(sondes, appareil)
    noms = [s.nom for s in sondes]
    guide = charger_invite("H1-classification")
    modele, fmt = v1._modele(config, racine)
    T, couches = int(config["T"]), [int(c) for c in config["couches"]]
    n = len(lignes)
    par_episode: dict[str, list[int]] = {}
    for i, x in enumerate(lignes):
        par_episode.setdefault(x["episode"], []).append(i)
    for e, rs in par_episode.items():
        if len(rs) != T or rs != list(range(rs[0], rs[0] + T)):
            raise GardeArret(f"épisode {e} : {len(rs)} actions non contiguës ({T} attendues)")
    jetons = [int(x) for x in identite["jetons"]]
    jetons_notes = [int(x) for x in identite["jetons_notes"]]
    # v3 : fiches chargées avant la reconstruction, table revérifiée par l'empreinte de P3 avant tout calcul
    fiches = v1.charger_fiches(config["chemin_fiches"], config["fiches_sha256"]) if config["chemin_fiches"] else None
    if fiches is None:
        raise GardeArret("fiches de P3 absentes : les règles A et B de l'addendum les exigent")
    etat["etape"] = "vérification de la table"                                                                 # v3
    etat["corrections_verifiees_au_chargement"] = verifier_table_au_chargement(                               # v3
        table, fmt, lignes, par_episode, jetons, jetons_notes, fiches, taches, consignes, guide, T)
    progres(etape="verification_table", version=VERSION_TABLE, entrees=len(table["episodes"]),
            corrections_verifiees=etat["corrections_verifiees_au_chargement"])                                 # v3
    etat["etape"] = "rejeu"
    conforme = np.zeros(n, dtype=bool)
    contexte_conforme = np.zeros(n, dtype=bool)
    recs, envs = {}, {}
    for e, rs in par_episode.items():           # reconstruction de tous les épisodes, sur processeur, avant la carte
        x0 = lignes[rs[0]]
        envs[e] = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
        recs[e] = v1.reconstruire_episode(fmt, envs[e], T, [lignes[r] for r in rs], [jetons[r] for r in rs],
                                          [jetons_notes[r] for r in rs])
        tous = True
        for r, a in zip(rs, recs[e]["actions"]):
            conforme[r] = a["conforme"]
            tous = tous and a["conforme"]
            contexte_conforme[r] = tous
    traj = np.zeros(n, dtype=bool)
    episodes_h = {}
    for e, rs in par_episode.items():
        episodes_h[e] = v1.episode_harnais(e, T, recs[e])
        if e not in fiches:
            raise GardeArret(f"épisode {e} absent des fiches du run source")
        traj[rs] = v1.empreinte_trajectoire(episodes_h[e]) == fiches[e]["trajectoire"]
    etat["trajectoires_identiques_base"] = int(traj.sum()) // T
    signales = [e for e, rs in par_episode.items() if conforme[rs].all() and not traj[rs].all()]
    non_conformes = [e for e, rs in par_episode.items() if not conforme[rs].all()]                          # v4
    if any(traj[par_episode[e]].all() for e in non_conformes):                                            # v4
        raise GardeArret("épisode non conforme en longueur à trajectoire de base identique : incohérent")
    etat["episodes_conformes_longueur"] = sum(1 for rs in par_episode.values() if conforme[rs].all())
    # règles A et B : la table couvre exactement les signalés ; non résolus au plus `seuil_non_conformes`
    try:
        corrections, non_resolus, non_retrouves = classer_episodes_v4(signales, non_conformes, table,       # v4
                                                                      int(config["seuil_non_conformes"]))
    except GardeArret as g:
        if "au-delà du seuil" in str(g):
            etat["regle_b"] = "au-delà du seuil"
        raise
    etat["regle_b"] = "dans le seuil"
    etat["episodes_non_resolus"] = non_resolus
    etat["episodes_non_retrouves_v4"] = non_retrouves                                                         # v4
    octets = table_des_octets(fmt.tok)[0] if any(c.get("paires") for c in corrections.values()) else None
    for e, ent in corrections.items():
        rs = par_episode[e]
        rec = appliquer_entree(fmt, envs[e], T, [lignes[r] for r in rs], [jetons[r] for r in rs],
                               [jetons_notes[r] for r in rs], ent, octets)                                     # v3
        ep = v1.episode_harnais(e, T, rec)
        if v1.empreinte_trajectoire(ep) != fiches[e]["trajectoire"]:
            raise GardeArret(f"table de tokenisation : la correction de {e} ({ent['methode']}) ne redonne pas "
                             f"l'empreinte de trajectoire de P3 : table falsifiée ou non applicable, rien n'est versé")
        recs[e], episodes_h[e] = rec, ep
        traj[rs] = True
        for r, a in zip(rs, rec["actions"]):
            conforme[r] = a["conforme"]
            contexte_conforme[r] = True
    non_resolu = np.zeros(n, dtype=bool)
    for e in non_resolus:
        non_resolu[par_episode[e]] = True
    contexte_conforme &= ~non_resolu
    par_methode = {m: sum(1 for c in corrections.values() if c["methode"] == m) for m in CORRIGEES}           # v3
    etat["episodes_fin_resolue"] = par_methode["fins"]
    # v3 : méthode de résolution par épisode (v1, v2, identifiants, aucune) et méthode de table
    par_table = {x["episode"]: x["methode"] for x in table["episodes"]}
    methodes = {e: {"methode_resolution": methode_resolution(par_table.get(e)), "methode_table": par_table.get(e)}
                for e in par_episode}
    par_resolution = {m: sum(1 for x in methodes.values() if x["methode_resolution"] == m) for m in METHODES_RESOLUTION}
    etat["par_methode_resolution"] = par_resolution
    etat["trajectoires_identiques"] = int(traj.sum()) // T
    etat["conformes_longueur"] = int(conforme.sum())
    etat["contextes_conformes"] = int(contexte_conforme.sum())
    progres(etape="reconstruction", conformes=int(conforme.sum()), contextes_conformes=int(contexte_conforme.sum()),
            trajectoires_identiques=etat["trajectoires_identiques"], corrections=len(corrections),
            non_resolus=len(non_resolus), non_retrouves=len(non_retrouves), actions=n)                       # v4
    eligibles = traj & (np.asarray(jetons_notes) > 0)
    echantillon = v1.tirer_echantillon(identite, eligibles, int(config["n_fidelite_par_condition"]),
                                       generateur(manifeste["graines"]["fidelite"]))
    ep_echantillon = list(dict.fromkeys(lignes[r]["episode"] for r in echantillon))
    ordre = ep_echantillon + [e for e in par_episode if e not in set(ep_echantillon)]
    d = len(couches)
    largeur = None
    moyenne = maximum = hors_cout = None
    jetons_empan = np.zeros(n, dtype=np.int64)
    ecart = np.full(n, np.nan)
    tol = float(config["tolerance_fidelite"])
    source = np.asarray(identite["scores"], dtype=np.float64)
    tour_echantillon, verdict_echantillon, verdict_negatif, repli = len(ep_echantillon), None, None, False
    activ_ident = np.zeros(n, dtype=bool)
    with noyau(config["noyau_attention"]):
        for k_ep, e in enumerate(ordre):
            exiger_sans_signal(f"rejeu, épisode {k_ep}")
            rs = par_episode[e]
            rec = recs.pop(e)
            acts = passe_unique(modele, rec["ids"], couches)
            from ..harnais.episode import empreinte_episode

            activ_ident[rs] = empreinte_episode(episodes_h[e], {0: acts})["activations"] == fiches[e]["activations"]
            if largeur is None:
                largeur = acts[couches[0]].shape[1]
                moyenne = np.full((n, d, largeur), np.nan, dtype=np.float16)
                maximum = np.full((n, d, largeur), np.nan, dtype=np.float16)
                hors_cout = np.full((n, d, largeur), np.nan, dtype=np.float16)
            for r, a in zip(rs, rec["actions"]):
                jetons_empan[r] = a["fin"] - a["debut"]
                if a["fin"] <= a["debut"]:
                    continue
                for j, c in enumerate(couches):
                    maximum[r, j] = v1._f16(agreger(acts[c], a["debut"], a["fin"], "max"), f"maximum, ligne {r}")
                    moyenne[r, j] = v1._f16(v1.moyenne_diagnostic_n026(acts[c], a["debut"], a["fin"]),
                                            f"moyenne, ligne {r}")
                    hc = v1.bornes_hors_cout(a["bornes"], a["fin"] - a["debut"])
                    if hc is None:
                        hors_cout[r, j] = maximum[r, j]
                    else:
                        garde = [p for p in range(a["debut"], a["fin"]) if not (hc[0] <= p - a["debut"] < hc[1])]
                        if garde:
                            hors_cout[r, j] = v1._f16(acts[c][garde].max(axis=0), f"hors coût, ligne {r}")
                seg = {c: acts[c][a["debut"]:a["fin"]] for c in notation.couches}
                if np.all(np.isfinite(source[r, [index[m] for m in noms]])):
                    ecart[r] = v1.ecart_relatif(notation.noter(seg), source[r], noms, index)
            if k_ep + 1 == tour_echantillon:
                fautes = [r for r in echantillon if not (conforme[r] and np.isfinite(ecart[r]) and ecart[r] <= tol)]
                verdict_echantillon = {"rangs": echantillon, "ecarts": [float(ecart[r]) for r in echantillon],
                                       "conformes": [bool(conforme[r]) for r in echantillon], "fautes": fautes,
                                       "tolerance": tol, "lecture": "conforme" if not fautes else "contraire"}
                etat["fidelite_echantillon"] = verdict_echantillon
                progres(etape="fidelite", lecture=verdict_echantillon["lecture"], fautes=len(fautes),
                        ecart_max=f"{np.nanmax([ecart[r] for r in echantillon]):.3e}")
                if fautes:
                    raise GardeArret(f"contrôle de fidélité contraire sur {len(fautes)} action(s) de l'échantillon "
                                     f"({fautes[:5]}) : le rejeu n'est pas le calcul de P3, rien n'est versé")
                verdict_negatif = controle_negatif(modele, fmt, notation, noms, index, source, echantillon, lignes,
                                                   par_episode, taches, consignes, guide, T, couches, jetons,
                                                   jetons_notes, tol, int(config["controle_negatif_min"]),
                                                   corrections, octets)                                        # v3
                etat["controle_negatif"] = verdict_negatif
                progres(etape="controle_negatif", lecture=verdict_negatif["lecture"],
                        hors_tolerance=f"{verdict_negatif['hors_tolerance']}/{len(echantillon)}")
                repli = verdict_negatif["lecture"] != "discriminant"
            if (k_ep + 1) % 20 == 0:
                progres(etape="rejeu", episodes=f"{k_ep + 1}/{len(ordre)}")
    notees = np.isfinite(ecart)
    # fidèle (v1, inchangé) : notée, conforme en longueur, scores à la tolérance ; les actions des épisodes non résolus
    # (règle B) sont jugées comme toute action hors contexte exact, par la tolérance
    fidele = notees & conforme & (np.nan_to_num(ecart, nan=np.inf) <= tol)
    if repli:
        fidele &= traj
    etat["etape"] = "écriture"
    dossier = racine / "donnees" / run_id
    dossier.mkdir(parents=True, exist_ok=False)
    ident = {k: np.asarray(identite[k]) for k in CLES_IDENTITE}
    commun = {**ident, "jetons_empan": np.asarray(identite["jetons_notes"], dtype=np.int64),
              "jetons_empan_rejeu": jetons_empan, "couches": np.array(couches, dtype=np.int64),
              "conforme_longueur": conforme, "contexte_conforme": contexte_conforme, "ecart_fidelite": ecart, "fidele": fidele,
              "trajectoire_identique": traj, "activations_identiques": activ_ident}
    fichiers = {}
    nom = config["nom_sortie"]
    for p, tableaux in ((dossier / f"{nom}.npz", {"moyenne": moyenne}), (dossier / f"{nom}-maximum.npz", {"maximum": maximum})):
        with open(p, "wb") as f:
            np.savez_compressed(f, **tableaux, **commun)
        fichiers[p.name] = sceller(p)
    p = dossier / f"{nom}-complement-hors-cout.npz"
    with open(p, "wb") as f:
        np.savez_compressed(f, maximum_hors_cout=hors_cout, **commun)
    fichiers[p.name] = sceller(p)
    trop_lourds = {n: (dossier / n).stat().st_size for n in fichiers if (dossier / n).stat().st_size > 95_000_000}
    p_r5 = float(fidele.sum() / notees.sum()) if notees.any() else None
    resultat = {"fichiers_au_dessus_de_95_mo": trop_lourds, "verdict_fidelite": "conforme", "regle_repli_appliquee": bool(repli),
                "lecture": "réserve (repli : fidèle restreint aux trajectoires identiques)" if repli else "principale",
                "textes_sha256": verifier(config["chemin_textes"]),
                "fichiers": fichiers, "identite_sha256": etat["identite_sha256"], "regle_empan": v1.REGLE_EMPAN,
                "contexte": v1.CONTEXTE, "couches": couches, "agregats": {"maximum": "production (harnais)",
                                                                          "moyenne": "diagnostic seulement (N-026)",
                                                                          "maximum_hors_cout": "contrôle, hors champ COST"},
                "fidelite_echantillon": verdict_echantillon, "controle_negatif": verdict_negatif,
                "empreintes_p3": {"episodes": len(par_episode), "trajectoires_identiques": etat["trajectoires_identiques"],
                                  "activations_identiques_au_bit": int(activ_ident.sum()) // T},
                "fidelite_toutes": {"notees": int(notees.sum()), "fideles": int(fidele.sum()),
                                    "conformes_longueur": int(conforme.sum()),
                                    "contextes_conformes": int(contexte_conforme.sum()), "actions": n,
                                    "fideles_parmi_contextes_conformes": int((fidele & contexte_conforme).sum()),
                                    "notees_contextes_conformes": int((notees & contexte_conforme).sum()),
                                    "egalite_exacte": int((ecart == 0).sum()),
                                    "ecart_max": float(np.nanmax(ecart)) if notees.any() else None,
                                    "ecart_mediane": float(np.nanmedian(ecart)) if notees.any() else None},
                "tokenisation": {"addendum": ADDENDUM,                                                         # v3
                                 "version_table": VERSION_TABLE,                                               # v3
                                 "table_sha256": verifier(config["chemin_table_tokenisation"]),
                                 "corrections_verifiees_au_chargement": etat["corrections_verifiees_au_chargement"],  # v3
                                 "trajectoires_identiques_base": etat["trajectoires_identiques_base"],
                                 "signales": len(signales), "corrections_par_methode": par_methode,
                                 "non_conformes": len(non_conformes),                                          # v4
                                 "episodes_non_retrouves_v4": non_retrouves,                                   # v4
                                 "actions_non_retrouvees_v4": int(sum(len(par_episode[e]) for e in non_retrouves)),  # v4
                                 "table_empreinte_citee": config["table_tokenisation_sha256"] != TABLE_EN_SESSION,  # v4
                                 "methodes_resolution": methodes,                                              # v3
                                 "par_methode_resolution": par_resolution,                                     # v3
                                 "episodes_non_resolus": non_resolus,
                                 "actions_non_resolues": int(non_resolu.sum()),
                                 "fideles_parmi_non_resolues": int((fidele & non_resolu).sum()),
                                 "seuil_non_conformes": int(config["seuil_non_conformes"]),
                                 "part_fideles_parmi_notees": p_r5,
                                 "p_r5_au_moins_90_pour_cent": None if p_r5 is None else bool(p_r5 >= 0.9)},
                "sondes_fidelite": noms, "sondes_legeres_sha256": sha_sondes, "reglages": reglages,
                "modele": config["agent"], "empreintes_modele": v1._empreintes_modele(config),
                "duree_s": round(time.perf_counter() - debut, 1)}
    ecrire_resultat(racine, chemin_m, "rejeu-activations", resultat)
    progres(etape="fin", fideles=int(fidele.sum()), notees=int(notees.sum()))
    return resultat


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    resultat = executer(config, Path("."), a.run_id, a.prereg)
    t = resultat["tokenisation"]
    print(json.dumps({"fichiers": resultat["fichiers"], "fidelite": resultat["fidelite_toutes"],
                      "tokenisation": {k: v for k, v in t.items() if k != "methodes_resolution"}},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
