"""R1 relancé — rejeu des actions stockées de P3 (addendum `prereg/R1-addendum-relance-v1.md`, GO-2026-11-01-13).

Version 2 du rejeu, sous un nom nouveau (R12) : `rejeu_activations_v1.py`, cité par le préenregistrement scellé
`prereg/R1-R2-rejeu-p3-v1.md`, n'est pas modifié ; ses fonctions sont importées telles quelles (reconstruction,
empreintes, échantillon, écart, agrégats, conversion en float16). Seule la garde CLC-03 change, selon l'addendum :

- **Règle A (table de tokenisation)** : la table des corrections (`resolution_tokenisation_v1`), calculée sur
  processeur avant la carte et scellée, est citée par la configuration (`chemin_table_tokenisation`,
  `table_tokenisation_sha256`). Elle doit couvrir **exactement** les épisodes conformes en longueur à trajectoire
  différente de la reconstruction de base (dans les deux sens) ; chaque correction est appliquée
  (`appliquer_entree`, gardes : mêmes octets, même longueur, même texte) et doit redonner **exactement** l'empreinte de
  trajectoire de P3, sinon arrêt (table falsifiée ou non applicable). La recherche des jetons de fin, faite à la volée
  par la v1, passe dans la table (même ordre, même fonction).
- **Règle B (non résolus)** : un épisode de la table « non résolu » est classé **non conforme** au lieu d'arrêter la
  course : ses actions ont `fidele` = faux et `contexte_conforme` = faux (hors contexte exact, non éligibles) ;
  `conforme_longueur` garde la mesure par action. Arrêt si ces épisodes dépassent `seuil_non_conformes` (10).

Tout le reste est la v1 : contrôle de fidélité, contrôle négatif (appliqué aux identifiants corrigés pour les épisodes
corrigés), règle de repli, sorties (mêmes fichiers, mêmes tableaux, mêmes noms, mêmes formes), verdict « conforme » du
run quand la course va au bout. Le résultat du run ajoute des clés descriptives (`tokenisation`), sans en retirer.
"""
from __future__ import annotations

import argparse
import json
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
from . import rejeu_activations_v1 as v1
from .alignement_v1 import CLES_IDENTITE, charger_identite, charger_textes_alignes, empreinte_identite
from .resolution_tokenisation_v1 import appliquer_entree, charger_table, classer_episodes, table_des_octets

COMMANDE = "python -m controle_ia.runs_nuit.rejeu_activations_v2"
CLES = v1.CLES + ("chemin_table_tokenisation", "table_tokenisation_sha256", "seuil_non_conformes",
                  "chemin_prereg_parent", "prereg_parent_sha256")
CONFIG_CITEE = v1.CONFIG_CITEE
empreinte_config = v1.empreinte_config
progres = v1.progres


def exiger_config(config: dict) -> None:
    manquantes = [k for k in CLES if k not in config]
    if manquantes:
        raise GardeArret(f"configuration du rejeu incomplète : {manquantes}")
    v1.exiger_config(config)
    s = config["seuil_non_conformes"]
    if isinstance(s, bool) or not isinstance(s, int) or s < 0:
        raise GardeArret(f"seuil_non_conformes {s!r} : entier positif ou nul attendu")
    if not config["chemin_table_tokenisation"]:
        raise GardeArret("table de tokenisation absente : la règle A l'exige")
    if config["mode"] == "reel":
        for k in ("table_tokenisation_sha256", "chemin_prereg_parent", "prereg_parent_sha256", "chemin_fiches",
                  "fiches_sha256"):
            if not config[k]:
                raise GardeArret(f"mode réel : {k} obligatoire")


def controle_negatif(modele, fmt, notation, noms, index, source, echantillon, lignes, par_episode, taches, consignes,
                     guide, T, couches, jetons, jetons_notes, tol, minimum, corrections: dict, octets) -> dict:
    """Contrôle négatif de la v1 (CLC-01, mêmes règles), à ceci près que les épisodes corrigés par la table sont
    reconstruits sous la consigne fausse **avec leurs identifiants corrigés** (mêmes paires, mêmes jetons de fin) : seule
    la consigne diffère du contexte exact."""
    from ..premier_test_ia.conditions import environnement

    consigne_seule, decale = [], []
    for r in echantillon:
        e = lignes[r]["episode"]
        rs = par_episode[e]
        x0 = lignes[rs[0]]
        faux = "saboteur" if x0["condition"] == "honnete" else "honnete"
        env = environnement(faux, tache_de(taches[x0["tache"]]), T, guide, consignes)
        L, J, JN = [lignes[q] for q in rs], [jetons[q] for q in rs], [jetons_notes[q] for q in rs]
        rec = (appliquer_entree(fmt, env, T, L, J, JN, corrections[e], octets) if e in corrections
               else v1.reconstruire_episode(fmt, env, T, L, J, JN))
        a = rec["actions"][rs.index(r)]
        acts = passe_unique(modele, rec["ids"], notation.couches)
        seg = {c: acts[c][a["debut"]:a["fin"]] for c in notation.couches}
        consigne_seule.append(v1.ecart_relatif(notation.noter(seg), source[r], noms, index))
        n_pos = acts[notation.couches[0]].shape[0]
        d1, f1 = a["debut"] + 1, min(a["fin"] + 1, n_pos)
        seg = {c: acts[c][d1:f1] for c in notation.couches}
        decale.append(v1.ecart_relatif(notation.noter(seg), source[r], noms, index))
    if not all(np.isfinite(x) for x in consigne_seule):
        raise GardeArret("contrôle négatif : écart non fini sous consigne fausse (score non fini) : echec")
    hors = int(sum(1 for x in consigne_seule if x > tol))
    return {"rangs": echantillon, "ecarts_consigne_fausse": [float(x) for x in consigne_seule],
            "ecarts_empan_decale_descriptif": [float(x) for x in decale], "hors_tolerance": hors,
            "minimum": minimum, "tolerance": tol, "lecture": "discriminant" if hors >= minimum else "non discriminant"}


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, autoriser_depot_sale: bool = False,
             entropie_essai: int | None = None) -> dict:
    racine = Path(racine)
    exiger_config(config)
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
    table = charger_table(config["chemin_table_tokenisation"], config["table_tokenisation_sha256"])
    for k in ("textes_sha256", "fiches_sha256", "scores_sha256"):
        if config[k] is not None and table.get(k) != config[k]:
            raise GardeArret(f"table de tokenisation calculée sur d'autres pièces ({k} : {str(table.get(k))[:12]})")
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, ["fidelite", "modele-jouet-inutilise"],
                                          entropie=entropie, decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
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
    etat["etape"] = "rejeu"
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
    fiches = v1.charger_fiches(config["chemin_fiches"], config["fiches_sha256"]) if config["chemin_fiches"] else None
    if fiches is None:
        raise GardeArret("fiches de P3 absentes : les règles A et B de l'addendum les exigent")
    traj = np.zeros(n, dtype=bool)
    episodes_h = {}
    for e, rs in par_episode.items():
        episodes_h[e] = v1.episode_harnais(e, T, recs[e])
        if e not in fiches:
            raise GardeArret(f"épisode {e} absent des fiches du run source")
        traj[rs] = v1.empreinte_trajectoire(episodes_h[e]) == fiches[e]["trajectoire"]
    etat["trajectoires_identiques_base"] = int(traj.sum()) // T
    signales = [e for e, rs in par_episode.items() if conforme[rs].all() and not traj[rs].all()]
    etat["episodes_conformes_longueur"] = sum(1 for rs in par_episode.values() if conforme[rs].all())
    # règles A et B : la table couvre exactement les signalés ; non résolus au plus `seuil_non_conformes`
    try:
        corrections, non_resolus = classer_episodes(signales, table, int(config["seuil_non_conformes"]))
    except GardeArret as g:
        if "au-delà du seuil" in str(g):
            etat["regle_b"] = "au-delà du seuil"
        raise
    etat["regle_b"] = "dans le seuil"
    etat["episodes_non_conformes"] = non_resolus
    octets = table_des_octets(fmt.tok)[0] if any(c.get("paires") for c in corrections.values()) else None
    for e, ent in corrections.items():
        rs = par_episode[e]
        rec = appliquer_entree(fmt, envs[e], T, [lignes[r] for r in rs], [jetons[r] for r in rs],
                               [jetons_notes[r] for r in rs], ent, octets)
        ep = v1.episode_harnais(e, T, rec)
        if v1.empreinte_trajectoire(ep) != fiches[e]["trajectoire"]:
            raise GardeArret(f"table de tokenisation : la correction de {e} ({ent['methode']}) ne redonne pas "
                             f"l'empreinte de trajectoire de P3 : table falsifiée ou non applicable, rien n'est versé")
        recs[e], episodes_h[e] = rec, ep
        traj[rs] = True
        for r, a in zip(rs, rec["actions"]):
            conforme[r] = a["conforme"]
            contexte_conforme[r] = True
    non_conforme_b = np.zeros(n, dtype=bool)
    for e in non_resolus:
        non_conforme_b[par_episode[e]] = True
    contexte_conforme &= ~non_conforme_b
    par_methode = {m: sum(1 for c in corrections.values() if c["methode"] == m) for m in ("fins", "une_paire", "deux_paires")}
    etat["episodes_fin_resolue"] = par_methode["fins"]
    etat["trajectoires_identiques"] = int(traj.sum()) // T
    etat["conformes_longueur"] = int(conforme.sum())
    etat["contextes_conformes"] = int(contexte_conforme.sum())
    progres(etape="reconstruction", conformes=int(conforme.sum()), contextes_conformes=int(contexte_conforme.sum()),
            trajectoires_identiques=etat["trajectoires_identiques"], corrections=len(corrections),
            non_conformes=len(non_resolus), actions=n)
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
                                                   corrections, octets)
                etat["controle_negatif"] = verdict_negatif
                progres(etape="controle_negatif", lecture=verdict_negatif["lecture"],
                        hors_tolerance=f"{verdict_negatif['hors_tolerance']}/{len(echantillon)}")
                repli = verdict_negatif["lecture"] != "discriminant"
            if (k_ep + 1) % 20 == 0:
                progres(etape="rejeu", episodes=f"{k_ep + 1}/{len(ordre)}")
    notees = np.isfinite(ecart)
    # fidèle (v1) : notée, conforme en longueur, scores à la tolérance ; règle B : jamais pour un épisode non conforme
    fidele = notees & conforme & (np.nan_to_num(ecart, nan=np.inf) <= tol) & ~non_conforme_b
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
                "tokenisation": {"addendum": "prereg/R1-addendum-relance-v1.md",
                                 "table_sha256": verifier(config["chemin_table_tokenisation"]),
                                 "trajectoires_identiques_base": etat["trajectoires_identiques_base"],
                                 "signales": len(signales), "corrections_par_methode": par_methode,
                                 "episodes_non_conformes": non_resolus,
                                 "actions_non_conformes": int(non_conforme_b.sum()),
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
    print(json.dumps({"fichiers": resultat["fichiers"], "fidelite": resultat["fidelite_toutes"],
                      "tokenisation": resultat["tokenisation"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
