"""Course de T0.8 (plan d'analyse, points 2 à 4) : épisodes honnêtes d'étalonnage, puis lectures des juges.

Mode réel : sur une carte, sous GO, **jamais lancé ici** (aucune instance n'est créée par ce code ; la création, la
minuterie et le plafond appartiennent à la session mère). Mode jouet : même chaîne, mêmes gardes, sur processeur,
données factices, agent scripté (`fabrique_jouet_v1.AgentScripte`) et juges jouets (`juges_v1.juge_jouet`).

1. Contrôle des entrées (liste blanche, empreintes) ; en mode réel, avant le manifeste : les sept marqueurs, les valeurs
   gelées (réglages de 7b compris), l'agent de 7b et les juges du texte (modèle, révision, gabarit, ouverture), les
   entrées rattachées au texte et aux marqueurs (empreinte consignée exigée, tâches et consignes du texte, fichiers de
   7b aux empreintes de `EMPREINTES_ENTREES_7B`, run de 7b égal à `RUN_7B`), le texte scellé passé portant les valeurs
   des marqueurs, le code au commit cité, la copie de l'instance sans fichier interdit
   (`entrees_v1.exiger_instance_sans_interdits`).
2. Étalonnage : 5 épisodes honnêtes par tâche d'évaluation (320), condition `honnete`, N = 1, T = 10, lots de 8,
   400 jetons au plus par action, température 1,0, modèle et gabarit de 7b (chargés hors ligne), contrôle du format de
   l'agent ; graines neuves, clés `etalonnage/tache/<identifiant>/e<k>` ; aucune activation lue (pas de garde
   d'équivalence en ligne : échantillon vide, déclaré) ; mesures de chaque action par les mêmes fonctions que la chaîne
   de 7b ; textes et identifiants générés gardés. Gardes de doublon : graines d'action d'un épisode d'étalonnage égales
   à celles d'un épisode de 7b, ou première action identique au texte de l'épisode H de 7b de la même tâche (tâche lue
   dans le plan d'étalonnage, jamais découpée dans l'identifiant de l'épisode ; une tâche sans première action H
   arrête) : arrêt.
3. Juges (l'un après l'autre) : en une passe sur toutes les actions des neuf conditions et de l'étalonnage ; avec
   raisonnement sur H, `S25` à `S100`, T100 et l'étalonnage ; graine par lecture, clé
   `juge/<juge>/raisonnement/<clé d'action>` ; une action non appliquée n'est pas lue (statut `regle`) ; une demande ne
   porte que `cle`, `systeme`, `utilisateur` (la condition reste à la course, pour ranger les lectures).
4. Lignes de progression (sortie d'erreur, heure relevée par la machine) : une par lot d'étalonnage, une par tranche de
   dix lots de chaque lecture de juge (liste d'arrêt, l. 235 ; CLT8C-11).
5. Sorties scellées sous `donnees/<run>/`, résultat `diag/<run>/course-t08.json` (fichiers et empreintes, comptes).
"""
from __future__ import annotations

import gc
import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

from ..environnements.invites import charger_invite
from ..environnements.pilote_a import charger_taches, graines_des_actions, tache_de
from ..gardes import GardeArret
from ..harnais.run_harnais_factice import graine_entiere
from ..harnais.validation_reelle import CHEMINS_GELES, exiger_code_importe_sous, noyau
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, lire_manifeste
from ..premier_test_ia.conditions import charger_consignes, environnement, mesures_action
from ..scellement import sceller
from ..t06 import test_croise as tc
from ..t06.cout import cout_action
from ..t06.lanceur import progres, tableaux_des_mesures
from . import configuration_v1 as cf
from . import entrees_v1 as en
from . import juges_v1 as jv
from . import rendu_juges_v1 as rj

COMMANDE = "python -m controle_ia.t08.course_v1"
FICHIERS = ("mesures_etalonnage", "textes_etalonnage", "lectures_J8_une_passe", "lectures_J8_raisonnement",
            "lectures_J3_une_passe", "lectures_J3_raisonnement")


def exiger_code_au_commit(racine: Path, commit: str) -> None:
    """Le code exécuté est celui du commit cité par `COMMIT_CODE_T08` (arbre gelé, mêmes chemins que T0.6)."""
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit, "HEAD", "--", *CHEMINS_GELES],
                       capture_output=True, text=True)
    if r.returncode == 1:
        raise GardeArret(f"code modifié depuis le commit cité {commit[:12]} (COMMIT_CODE_T08)")
    if r.returncode != 0:
        raise GardeArret(f"comparaison au commit cité {commit[:12]} impossible : {r.stderr.strip()}")


def cle_etalonnage(tache: str, k: int) -> str:
    return f"etalonnage/tache/{tache}/e{k}"


def cle_juge(juge: str, cle_action: str) -> str:
    return f"juge/{juge}/raisonnement/{cle_action}"


def cles_graines_course(taches: list[str], cles_raisonnement: list[str], mode: str) -> list[str]:
    cles = [cle_etalonnage(t, k) for t in taches for k in range(cf.EPISODES_ETALONNAGE_PAR_TACHE)]
    cles += [cle_juge(j, c) for j in cf.JUGES for c in cles_raisonnement]
    if mode == "jouet":
        cles += ["jouet/juge/J8", "jouet/juge/J3"]
    return cles


def plan_etalonnage(taches: list[dict]) -> list[tuple]:
    return [(f"{cf.ETALONNAGE}/{t['identifiant']}/e{k}", t, k) for t in taches
            for k in range(cf.EPISODES_ETALONNAGE_PAR_TACHE)]


def ligne_mesures(cle: str, episode: str, tache: str, pas: int, texte: str, ids: list[int], jetons_notes: int) -> dict:
    """Mêmes champs que `mesures-t06.npz` (chaîne de 7b) : coût par le lecteur neuf, formes du champ, mentions."""
    m = mesures_action(texte)
    return {"cle": cle, "episode": episode, "phase": cf.ETALONNAGE, "condition": cf.HONNETE, "tache": tache,
            "pas": int(pas), "jetons": len(ids), "jetons_notes": int(jetons_notes), **cout_action(texte),
            "mention": bool(m["mention_texte_prive"]), "mention_etendue": tc.mention_etendue(texte), "adaptateur": None,
            "dose": 0.0}


def exiger_sans_doublon(graines_et: dict, graines_7b: dict, textes_et: dict, premieres_h: dict, tache_de: dict) -> dict:
    """`graines_et[épisode]` : graines des actions d'un épisode d'étalonnage ; `graines_7b[tâche]` : celles des épisodes
    de 7b de la tâche ; `textes_et[épisode]` : texte de la première action ; `premieres_h[tâche]` : celui de l'épisode H
    de 7b ; `tache_de[épisode]` : tâche de l'épisode d'étalonnage, **prise dans le plan d'étalonnage** (aucune découpe
    de l'identifiant ; CLT8C-07). Arrêt : doublon ; épisode d'étalonnage sans première action, ou absent du plan ;
    tâche d'étalonnage sans première action H de 7b (la garde ne peut pas rester sans objet)."""
    vus_7b = {tuple(sorted(v.items())) for v in graines_7b.values()}
    for e, g in graines_et.items():
        if tuple(sorted(g.items())) in vus_7b:
            raise GardeArret(f"graines de l'épisode d'étalonnage {e} égales à celles d'un épisode de 7b : arrêt (doublon)")
    discordants = sorted(set(textes_et) ^ set(tache_de))
    if discordants:
        raise GardeArret(f"épisodes d'étalonnage du plan et premières actions discordants ({discordants[:3]}) : arrêt")
    sans_h = sorted({tache_de[e] for e in textes_et} - set(premieres_h))
    if sans_h:
        raise GardeArret(f"tâche(s) d'étalonnage sans première action de l'épisode H de 7b ({len(sans_h)} : {sans_h[:3]}) : "
                         "garde de doublon sans objet : arrêt")
    for e, t in textes_et.items():
        if t == premieres_h[tache_de[e]]:
            raise GardeArret(f"première action de {e} identique à celle de l'épisode H de 7b de la même tâche : arrêt")
    return {"episodes_controles": len(textes_et), "taches_controlees": len(set(tache_de.values())), "doublons": 0}


def _ecrire_npz(chemin: Path, tableaux: dict) -> str:
    """npz écrit à l'octet près reproductible (date des entrées fixée), lisible par `numpy.load`."""
    import io
    import zipfile

    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    with zipfile.ZipFile(chemin, "w", compression=zipfile.ZIP_STORED) as z:
        for k in sorted(tableaux):
            b = io.BytesIO()
            np.lib.format.write_array(b, np.asanyarray(tableaux[k]), allow_pickle=False)
            info = zipfile.ZipInfo(f"{k}.npy", date_time=(1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o600 << 16
            z.writestr(info, b.getvalue())
    return sceller(chemin)


def _ecrire_jsonl(chemin: Path, lignes: list[dict]) -> str:
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    with open(chemin, "w", encoding="utf-8") as f:
        for x in lignes:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    return sceller(chemin)


def _lots(n: int, lot: int) -> int:
    return -(-n // lot)


def jouer_etalonnage_reel(config: dict, taches: list[dict], g: dict, consignes: dict, guide: str) -> tuple:
    """Machine de calcul seulement : modèle de 7b (spécification contrôlée avant tout chargement, CLT8C-06), chargé hors
    ligne (cache local seulement, CLT8C-13), gabarit daté, contrôle du format, lots de 8, graines neuves ; une ligne de
    progression par lot (CLT8C-11)."""
    cf.exiger_spec_agent(config["agent"])
    from ..environnements.lancer_pilote_a import charger_modele_et_format
    from ..harnais.episode import jouer_episodes
    from ..premier_test_ia.run import controler_format_agent

    modele, fmt = charger_modele_et_format(config["agent"], "reel", 0, hors_ligne=True)
    format_agent = controler_format_agent(fmt, config["agent"], "reel")
    plan = plan_etalonnage(taches)
    lignes, textes, graines_et = [], [], {}
    index = {t["identifiant"]: k for k, t in enumerate(taches)}
    prevus = _lots(len(plan), config["lot"])
    with noyau(config["noyau_attention"]):
        for n_lot, debut in enumerate(range(0, len(plan), config["lot"]), start=1):
            morceau = plan[debut:debut + config["lot"]]
            envs = [environnement("honnete", tache_de(t), config["T"], guide, consignes) for _, t, _ in morceau]
            graines = [graines_des_actions(generateur(g[cle_etalonnage(t["identifiant"], k)]), 1, config["T"])
                       for _, t, k in morceau]
            res = jouer_episodes(modele, fmt, envs, [e for e, _, _ in morceau], 1, config["T"], graines, config["couches"],
                                 config["max_nouveaux"], config["temperature"], (), config["tolerance_equivalence"])
            for (ep, _acts, _rap), (e, t, k), gr in zip(res, morceau, graines):
                graines_et[e] = gr
                for a in ep.actions_dans_l_ordre():
                    fin = a.fin - 1 if a.ids and a.ids[-1] in fmt.fins else a.fin
                    cle = f"{cf.ETALONNAGE}__t{index[t['identifiant']]:03d}__e{k}__p{a.pas}"
                    lignes.append(ligne_mesures(cle, e, t["identifiant"], a.pas, a.texte, a.ids, max(0, fin - a.debut)))
                    textes.append({"cle": cle, "episode": e, "condition": cf.HONNETE, "tache": t["identifiant"],
                                   "pas": a.pas, "texte": a.texte, "ids": [int(x) for x in a.ids]})
            progres(etape="etalonnage", lot=f"{n_lot}/{prevus}", actions=len(lignes))
    del modele
    gc.collect()
    return lignes, textes, graines_et, {"format_agent": format_agent}


def jouer_etalonnage_jouet(config: dict, taches: list[dict], g: dict) -> tuple:
    from .fabrique_jouet_v1 import AgentScripte

    agent = AgentScripte()
    plan = plan_etalonnage(taches)
    index = {t["identifiant"]: k for k, t in enumerate(taches)}
    lignes, textes, graines_et = [], [], {}
    lot = int(config.get("lot", cf.VALEURS_GELEES_COURSE["lot"]))
    prevus = _lots(len(plan), lot)
    for n, (e, t, k) in enumerate(plan, start=1):
        gen = generateur(g[cle_etalonnage(t["identifiant"], k)])
        gr = graines_des_actions(gen, 1, config["T"])
        graines_et[e] = gr
        for pas, (texte, ids) in enumerate(agent.episode(cf.HONNETE, t["identifiant"], gr, config["T"])):
            cle = f"{cf.ETALONNAGE}__t{index[t['identifiant']]:03d}__e{k}__p{pas}"
            lignes.append(ligne_mesures(cle, e, t["identifiant"], pas, texte, ids, len(ids)))
            textes.append({"cle": cle, "episode": e, "condition": cf.HONNETE, "tache": t["identifiant"], "pas": pas,
                           "texte": texte, "ids": ids})
        if n % lot == 0 or n == len(plan):
            progres(etape="etalonnage", lot=f"{_lots(n, lot)}/{prevus}", actions=len(lignes))
    return lignes, textes, graines_et, {"agent": "scripté (jouet, factice)"}


def demandes(textes_par_episode: dict, taches_juge: dict, T: int, systeme: str) -> dict:
    """Épisode → demandes (ou non lus) dans l'ordre des pas."""
    sortie = {}
    for e, acts in sorted(textes_par_episode.items()):
        sortie[e] = rj.demandes_de_l_episode(taches_juge[acts[0]["tache"]], acts, T, systeme)
    return sortie


def demande_juge(x: dict) -> dict:
    """Ce qui va au juge : `cle`, `systeme`, `utilisateur`, rien d'autre (CLT8C-15)."""
    return {k: x[k] for k in jv.CLES_DEMANDE}


def lire_juge(juge, dem: dict, conditions: tuple, condition_de: dict, lecture: str, config: dict, g: dict) -> list[dict]:
    """Lecture d'un (juge, mode de lecture) : les demandes ne portent que `cle`, `systeme`, `utilisateur` ; l'épisode et
    la condition restent ici, pour ranger les lectures (CLT8C-15) ; une ligne de progression par tranche de dix lots."""
    lot = int(config["lot_juge"])
    a_lire, rangement, lignes = [], [], []
    for e in sorted(dem):
        c = condition_de[e]
        if c not in conditions:
            continue
        for x in dem[e]:
            if "non_lu" in x:
                lignes.append({"cle": x["cle"], "episode": e, "condition": c, "statut": "regle", "score": None,
                               "masse": None, "motif": x["non_lu"], "detail": x.get("motif")})
            else:
                a_lire.append(demande_juge(x))
                rangement.append((x["cle"], e, c))

    def suivi(fait, prevu):
        progres(etape="juge", juge=juge.nom, lecture=lecture, lots=f"{fait}/{prevu}")

    if lecture == "une_passe":
        lues = jv.lire_une_passe(juge, a_lire, lot, progres=suivi)
    else:
        graines = {x["cle"]: graine_entiere(g[cle_juge(juge.nom, x["cle"])]) for x in a_lire}
        lues = jv.lire_avec_raisonnement(juge, a_lire, lot, graines, int(config["max_jetons_raisonnement"]),
                                         float(config["temperature_juge"]), progres=suivi)
    if len(lues) != len(rangement):
        raise GardeArret("nombre de lectures ≠ nombre de demandes")
    for (cle, e, c), l in zip(rangement, lues):
        if cle != l["cle"]:
            raise GardeArret("ordre des lectures rompu")
        lignes.append({**{k: v for k, v in l.items()}, "episode": e, "condition": c,
                       "statut": "anomalie" if l["anomalie"] else "lu"})
    return sorted(lignes, key=lambda r: r["cle"])


ENTREES_COURSE_REQUISES = ("taches", "textes_7b", "episodes_7b", "manifeste_7b", "invite", "consignes")


def exiger_course_reelle(config: dict, prereg) -> dict:
    """Mode réel, avant toute lecture d'entrée et tout manifeste : marqueurs, valeurs gelées, agent de 7b, juges du
    texte, entrées rattachées au texte et aux marqueurs, texte scellé passé portant les valeurs des marqueurs."""
    marqueurs = cf.exiger_marqueurs(config.get("marqueurs"))
    cf.exiger_valeurs_gelees(config, cf.VALEURS_GELEES_COURSE)
    if prereg is None:
        raise GardeArret("course réelle sans préenregistrement scellé : R1 interdit de lancer")
    cf.exiger_spec_agent(config.get("agent"))
    for nom in cf.JUGES:
        jv.exiger_spec_reelle(nom, (config.get("juges") or {}).get(nom))
    cf.exiger_entrees_reelles(config["entrees"], marqueurs, ENTREES_COURSE_REQUISES)
    texte = cf.exiger_marqueurs_au_texte(prereg, marqueurs)
    return {"marqueurs": marqueurs, "texte": texte}


def executer_course(config: dict, racine, run_id: str, prereg: str | None = None,
                    autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    mode = cf.exiger_mode(config)
    entropie = config.get("entropie")
    if mode == "reel":
        reel = exiger_course_reelle(config, prereg)
        marqueurs = reel["marqueurs"]
        exiger_code_importe_sous(racine)
        exiger_code_au_commit(racine, marqueurs["COMMIT_CODE_T08"])
        instance = en.exiger_instance_sans_interdits(racine)
        entropie = marqueurs["ENTROPIE_T08"]
    else:
        instance = None
    lb = en.ListeBlanche(racine, config["entrees"])
    taches = charger_taches(lb.chemin("taches"))
    ids_taches = [t["identifiant"] for t in taches]
    textes_7b = lb.lire_jsonl("textes_7b")
    epi = en.projeter_episodes_t06(lb.lire_json("episodes_7b"))
    if en.verifier(lb.chemin("textes_7b")) != epi["textes_sha256"]:
        raise GardeArret("textes-actions-t06.jsonl : empreinte ≠ celle de episodes-t06.json")
    man7b = en.lire_manifeste_7b(lb, "manifeste_7b", ids_taches)
    systeme = lb.chemin("invite").read_text(encoding="utf-8")
    if mode == "reel":
        if man7b["run_id"] != marqueurs["RUN_7B"]["run_id"] or man7b["sha256"] != marqueurs["RUN_7B"]["manifeste_sha256"]:
            raise GardeArret("manifeste de 7b ≠ RUN_7B (identifiant ou empreinte) : arrêt")
        lb.chemin("consignes")                 # empreinte contrôlée avant le manifeste (consignes du texte)
    par_ep_7b = {}
    for t in textes_7b:
        par_ep_7b.setdefault(t["episode"], []).append(t)
    condition_de = {e: v[0]["condition"] for e, v in par_ep_7b.items()}
    cles_r = sorted(t["cle"] for t in textes_7b if t["condition"] in cf.CONDITIONS_RAISONNEMENT)
    cles_r += sorted(f"{cf.ETALONNAGE}__t{i:03d}__e{k}__p{p}" for i in range(len(taches))
                     for k in range(cf.EPISODES_ETALONNAGE_PAR_TACHE) for p in range(config["T"]))
    chemin_m, m = creer_manifeste(racine, run_id, config, cles_graines_course(ids_taches, cles_r, mode),
                                  entropie=entropie, decisif=mode == "reel", prereg=prereg,
                                  autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    g = m["graines"]
    from ..harnais.modeles import regler_determinisme

    reglages = regler_determinisme(int(config["fils"]), "cuda" if mode == "reel" else "cpu")
    debut = time.perf_counter()
    dossier = racine / "donnees" / run_id
    dossier.mkdir(parents=True, exist_ok=False)
    progres(etape="course-debut", run=run_id, mode=mode)
    if mode == "reel":
        consignes = charger_consignes(lb.chemin("consignes"), cf.CONSIGNES_P3_SHA256)
        lignes, textes_et, graines_et, info = jouer_etalonnage_reel(config, taches, g, consignes,
                                                                    charger_invite("H1-classification"))
    else:
        lignes, textes_et, graines_et, info = jouer_etalonnage_jouet(config, taches, g)
    premieres_et = {t["episode"]: t["texte"] for t in textes_et if int(t["pas"]) == 0}
    premieres_h = {t["tache"]: t["texte"] for t in textes_7b if t["condition"] == cf.HONNETE and int(t["pas"]) == 0}
    graines_7b = {k.split("/", 1)[1]: graines_des_actions(generateur(v), 1, config["T"])
                  for k, v in man7b["graines"].items() if k.startswith("tache/")}
    tache_de_l_episode = {e: t["identifiant"] for e, t, _ in plan_etalonnage(taches)}
    doublons = exiger_sans_doublon(graines_et, graines_7b, premieres_et, premieres_h, tache_de_l_episode)
    fichiers = {}
    p = dossier / "mesures-etalonnage-t08.npz"
    fichiers["mesures_etalonnage"] = {"chemin": str(p.relative_to(racine)), "sha256": _ecrire_npz(p, tableaux_des_mesures(lignes))}
    p = dossier / "textes-etalonnage-t08.jsonl"
    fichiers["textes_etalonnage"] = {"chemin": str(p.relative_to(racine)), "sha256": _ecrire_jsonl(p, textes_et)}
    taches_juge = {t["identifiant"]: rj.projeter_tache(t) for t in taches}
    par_ep = dict(par_ep_7b)
    for t in textes_et:
        par_ep.setdefault(t["episode"], []).append(t)
        condition_de[t["episode"]] = cf.ETALONNAGE
    dem = demandes(par_ep, taches_juge, config["T"], systeme)
    juges_info = {}
    for nom in cf.JUGES:
        if mode == "reel":
            juge = jv.charger_juge_reel(nom, config["juges"][nom], hors_ligne=True)
        else:
            vocab = [systeme] + [t["texte"] for t in textes_7b[:2000]] + [rj.EN_TETE_QUESTIONS, ">>> LATEST CHANGE (added) <<<",
                                                                          ">>> LATEST CHANGE (revised) <<< CURRENT SET after turn of"]
            vocab += [t["questions"] for t in taches]
            juge = jv.juge_jouet(nom, graine_entiere(g[f"jouet/juge/{nom}"]), vocab)
        juges_info[nom] = {"revision": juge.revision, "mode": juge.mode}
        for lecture, conds in (("une_passe", cf.CONDITIONS_7B + (cf.ETALONNAGE,)),
                               ("raisonnement", cf.CONDITIONS_RAISONNEMENT + (cf.ETALONNAGE,))):
            rows = lire_juge(juge, dem, conds, condition_de, lecture, config, g)
            p = dossier / f"lectures-{nom}-{lecture}-t08.jsonl"
            fichiers[f"lectures_{nom}_{lecture}"] = {"chemin": str(p.relative_to(racine)), "sha256": _ecrire_jsonl(p, rows)}
        del juge
        gc.collect()
    resultat = {"fichiers": fichiers, "manifeste_7b_sha256": man7b["sha256"], "run_7b": man7b["run_id"],
                "doublons": doublons, "instance": instance, "juges": juges_info, "etalonnage": info,
                "reglages": {k: v for k, v in reglages.items() if k not in ("torch", "numpy")},
                "comptes": {"episodes_etalonnage": len(premieres_et), "actions_etalonnage": len(lignes),
                            "demandes": sum(len(v) for v in dem.values())},
                "marqueurs": "remplis" if mode == "reel" else "absents (mode jouet)", "mode": mode}
    chemin = ecrire_resultat(racine, chemin_m, "course-t08", resultat)
    lire_manifeste(chemin_m)
    progres(etape="course-fin", run=run_id)
    return {"manifeste": str(chemin_m), "course": str(chemin), "duree_s": round(time.perf_counter() - debut, 1)}


def _main(argv: list[str]) -> int:
    import argparse

    from ..scellement import verifier

    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    print(json.dumps(executer_course(config, Path("."), a.run_id, a.prereg), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
