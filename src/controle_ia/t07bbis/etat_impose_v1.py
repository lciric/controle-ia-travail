"""Relecture forcée à **état d'adaptateur imposé** et à **environnement imposé** (`prereg/T0.7-etape-B-bis-v1.md`, plan,
point 3 ; « Code neuf », premier point), v1 — module neuf, **partagé avec la pièce R** du texte de validité de l'adaptateur
(`prereg/validite-adaptateur-v1.md`, « Métrique », séries R1 à R7 : code seulement ; B bis ne lit jamais ses données, ses
scores ni sa lecture). Le module prévu par ce texte (`validite_adaptateur/relecture_v1.py`) n'existe pas au 2026-11-14 :
B bis l'écrit ici sous un nom neuf (R12), et la pièce R peut l'importer.

Réutilisé **sans modification** : `t07.repli_recalcul_v1` (lecture des textes, `charger_adaptateurs`, empan noté `_empan`),
la chaîne de T0.6 appelée telle quelle (`environnements.lancer_pilote_a.charger_modele_et_format`, `conversation_de_controle`,
`harnais.modeles.regler_determinisme`, `t06.identite` (`logits_de_controle`, `controle_identite`, `exiger_etat_de_phase`),
`t06.lanceur.charger_taches_t06`, `premier_test_ia.conditions` (`environnement`, `charger_consignes`),
`environnements.pilote_a.tache_de`, `environnements.invites.charger_invite`, `harnais.episode.Action`,
`harnais.activations.passe_unique`, `organismes.lora`).

- `charger` : comme `repli_recalcul_v1.recalculer` (points 1 et 2 de son en-tête) : manifeste de 7b, modèle et format,
  logits de contrôle **avant** l'injection, injection et chargement de chaque adaptateur à son sceau, empreinte égale à celle
  de `distillation-t06.json`, **contrôle d'identité à dose 0** (logits égaux au bit près à la base) **et artefact à dose 1**.
- `imposer_etat` : état « modèle nu » (adaptateur saboteur chargé, dose 0 : la base au bit près), ou adaptateur saboteur à la
  dose d, ou témoin à la dose 1 ; **à chaque série**, dose lue sur chaque module égale à la dose imposée et empreinte des
  adaptateurs chargés égale à celle de `distillation-t06.json` (`exiger_etat_de_phase`), sinon arrêt.
- `rejouer_episode` : la conversation reconstruite **comme `repli_recalcul_v1.rejouer`** (ouverture au pas 0, puis tour, clôture
  après chaque action ; observation de l'environnement **imposé** ; journal des textes décodés) ; texte décodé des
  identifiants égal à `texte`, clé reconstruite égale à la clé de la chaîne, sinon arrêt ; une passe unique par épisode ;
  empan noté `[début, _fin_notee[`.
- `relire_serie` : une série (J_d, J_instruit, A_d, A_T ; `commun_v1.series_imposees`) écrite en demi-précision
  (`t06.lanceur_v2.ActivationsDemi`, dossier absent exigé, R12).
- `eprouver_chemin` (constat M4) : 8 épisodes de H tirés par graine (`bbis/chemin-impose`) relus à l'état « modèle nu » égaux
  au bit près à leur série O (cas sain), et relus à l'état `S100` différents (artefact) ; 8 épisodes de `S100` relus à l'état
  `S100` imposé et 8 de `T100` à l'état `T100` imposé, égaux au bit près à leur série O ; un écart : arrêt.

**Éprouvé en mode jouet seulement** (modèle jouet par caractères du harnais) ; en mode réel, le chemin est le même avec le
modèle de la révision figée, en « cuda », hors ligne : jamais lancé ici.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from ..gardes import GardeArret, exiger_sans_signal
from ..t07 import repli_recalcul_v1 as rr
from .commun_v1 import H, T100, nom_dose


def charger(racine: Path, run_t06: str) -> dict:
    """Modèle, format, adaptateurs chargés et contrôlés (docstring du module)."""
    from ..environnements.lancer_pilote_a import charger_modele_et_format, conversation_de_controle
    from ..harnais.modeles import regler_determinisme
    from ..harnais.run_harnais_factice import graine_entiere
    from ..manifeste import lire_manifeste, verifier_resultat
    from ..t06.identite import controle_identite, logits_de_controle
    from ..t07.lecture_v1 import lire_episodes_t06
    racine = Path(racine)
    m6, sha_m6 = lire_manifeste(racine / "runs" / run_t06 / "manifeste.json")
    config, g = m6["config"], m6["graines"]
    ep = lire_episodes_t06(racine, run_t06)
    textes = rr.lire_textes_par_episode(racine / "donnees" / run_t06 / Path(str(ep["resultat"]["textes"])).name)
    dist = verifier_resultat(racine, racine / "diag" / run_t06 / "distillation-t06.json")["resultat"]
    mode = config["mode"]
    regler_determinisme(config["fils"], "cuda" if mode == "reel" else "cpu")
    modele, fmt = charger_modele_et_format(config["agent"], mode, graine_entiere(g["modele-jouet"]), hors_ligne=(mode == "reel"))
    consigne_c, observations_c, _ = conversation_de_controle("agent", None)
    ids_controle = fmt.ouverture(consigne_c, observations_c[0])
    logits_base = logits_de_controle(modele, ids_controle)
    etats, empreintes = rr.charger_adaptateurs(modele, racine, dist, config, g)
    identite = controle_identite(modele, ids_controle, logits_base, etats)
    return {"racine": racine, "run": run_t06, "modele": modele, "fmt": fmt, "config": config, "graines_7b": g,
            "etats": etats, "empreintes": empreintes, "identite": identite, "textes": textes,
            "manifeste_7b": {"chemin": f"runs/{run_t06}/manifeste.json", "sha256": sha_m6}}


def imposer_etat(ch: dict, adaptateur: str | None, dose: float) -> dict:
    """Impose l'état ; vérifie la dose lue sur chaque module et l'empreinte des adaptateurs chargés (sinon arrêt)."""
    from ..organismes import lora as lo
    from ..t06.identite import exiger_etat_de_phase
    ad = adaptateur or "saboteur"
    if adaptateur is None and float(dose) != 0.0:
        raise GardeArret("modèle nu : dose 0 exigée")
    lo.charger_etat(ch["modele"], ch["etats"][ad])
    lo.fixer_dose(ch["modele"], float(dose))
    e = exiger_etat_de_phase(ch["modele"], float(dose), ch["empreintes"][ad], f"état imposé ({ad}, dose {dose})")
    return {"adaptateur": ad, "dose": float(dose), "empreinte": e["empreinte"], "modules": e["modules"]}


def _taches(ch: dict) -> list:
    from ..t06.lanceur import charger_taches_t06
    return charger_taches_t06(ch["config"], ch["racine"])["evaluation"]


def rejouer_episode(ch: dict, condition_textes: str, environnement: str, tache: dict, index: int) -> list:
    """Rejeu en forçage d'un épisode (textes de `condition_textes`, environnement `environnement`) ; rend [(clé, {couche :
    activations de l'empan noté})]. Même reconstruction que `repli_recalcul_v1.rejouer`."""
    from ..environnements.invites import charger_invite
    from ..environnements.pilote_a import tache_de
    from ..harnais.activations import passe_unique
    from ..harnais.episode import Action
    from ..premier_test_ia.conditions import charger_consignes, environnement as env_de
    config, fmt = ch["config"], ch["fmt"]
    T = int(config["T"])
    ecrites = ch["textes"].get((condition_textes, tache["identifiant"]))
    if ecrites is None or sorted(ecrites) != list(range(T)):
        raise GardeArret(f"état imposé : épisode {condition_textes}/{tache['identifiant']} : actions écrites "
                         f"{sorted(ecrites or {})}, pas 0 à {T - 1} attendus")
    guide = charger_invite("H1-classification")
    consignes = charger_consignes(Path(ch["racine"]) / config["chemin_consignes"], config["consignes_sha256"])
    env = env_de(environnement, tache_de(tache), T, guide, consignes)
    couches = [int(c) for c in config["couches"]]
    ids, journal, debut, actions = [], [], None, []
    for pas in range(T):
        rec = ecrites[pas]
        obs = env.observation(0, pas, journal)
        if pas == 0:
            debut = (env.consigne_privee(0), obs)
            ctx = fmt.ouverture(*debut)
        else:
            ctx = ids + fmt.tour(debut, obs)
        nv = [int(x) for x in rec["ids"]]
        texte = fmt.tok.decode(nv, skip_special_tokens=True)
        if texte != rec["texte"]:
            raise GardeArret(f"état imposé : action {rec['cle']} : texte décodé des identifiants ≠ texte écrit par la chaîne")
        cle = f"{condition_textes}__t{index:03d}__p{pas}"
        if cle != rec["cle"]:
            raise GardeArret(f"état imposé : clé reconstruite {cle} ≠ clé écrite {rec['cle']}")
        actions.append((cle, Action(0, pas, len(ctx), len(ctx) + len(nv), nv, texte)))
        ids = ctx + nv + fmt.cloture(debut, nv)
        journal.append((0, pas, texte))
    acts = passe_unique(ch["modele"], ids, couches)
    sortie = []
    for cle, a in actions:
        d, f = rr._empan(a, fmt)
        if f > d:
            sortie.append((cle, {k: acts[k][d:f] for k in couches}))
    return sortie


def relire_serie(ch: dict, serie: dict, ecrire, identifiants=None) -> dict:
    """Une série à état et environnement imposés ; `ecrire(clé, {couche : tableau})` ; `identifiants` : tâches retenues (toutes
    par défaut). Rend {serie, etat, episodes, actions} (aucun score)."""
    from ..organismes import lora as lo
    etat = imposer_etat(ch, serie["adaptateur"], serie["dose"])
    taches = _taches(ch)
    index = {t["identifiant"]: k for k, t in enumerate(taches)}
    episodes = actions = 0
    for t in taches:
        if identifiants is not None and t["identifiant"] not in identifiants:
            continue
        exiger_sans_signal(f"la relecture {serie['serie']}/{t['identifiant']}")
        for cle, segs in rejouer_episode(ch, serie["textes"], serie["environnement"], t, index[t["identifiant"]]):
            ecrire(cle, segs)
            actions += 1
        episodes += 1
    imposer_etat(ch, serie["adaptateur"], serie["dose"])          # état inchangé pendant la série (contrôle de fin)
    lo.fixer_dose(ch["modele"], 0.0)
    return {"serie": serie["serie"], "etat": etat, "episodes": episodes, "actions": actions}


def _demi(a) -> np.ndarray:
    """Passage en demi-précision comme `t06.lanceur_v2.ActivationsDemi.ecrire`."""
    return np.ascontiguousarray(np.asarray(a, dtype=np.float32).astype(np.float16))


def _comparer(ch: dict, dossier_o: Path, condition: str, environnement: str, adaptateur, dose, identifiants) -> dict:
    """Relecture en mémoire d'épisodes, comparée au bit près aux fichiers de leur série O (demi-précision)."""
    taches = _taches(ch)
    index = {t["identifiant"]: k for k, t in enumerate(taches)}
    imposer_etat(ch, adaptateur, dose)
    egales = differentes = 0
    for t in taches:
        if t["identifiant"] not in identifiants:
            continue
        for cle, segs in rejouer_episode(ch, condition, environnement, t, index[t["identifiant"]]):
            for k, a in segs.items():
                o = np.load(Path(dossier_o) / f"c{k}" / f"{cle}.npy")
                n = _demi(a)
                if o.dtype == n.dtype and o.shape == n.shape and np.array_equal(o.view(np.uint16), n.view(np.uint16)):
                    egales += 1
                else:
                    differentes += 1
    from ..organismes import lora as lo
    lo.fixer_dose(ch["modele"], 0.0)
    return {"egales": egales, "differentes": differentes}


def eprouver_chemin(ch: dict, dossier_o: Path, rng, n: int = 8) -> dict:
    """Chemin de l'état imposé éprouvé sur la marche (constat M4) : trois cas sains égaux au bit près à la série O, un artefact
    différent ; un écart : arrêt (TE et ART comparent une série du chemin ancien à une série du chemin neuf)."""
    ids = [t["identifiant"] for t in _taches(ch)]
    choisir = lambda: sorted(ids[int(i)] for i in rng.choice(len(ids), size=min(int(n), len(ids)), replace=False))
    t_h, t_s, t_t = choisir(), choisir(), choisir()
    s100 = nom_dose(1.0)
    cas = {"H sous le modèle nu": _comparer(ch, dossier_o, H, H, None, 0.0, t_h),
           f"{s100} sous {s100}": _comparer(ch, dossier_o, s100, H, "saboteur", 1.0, t_s),
           f"{T100} sous {T100}": _comparer(ch, dossier_o, T100, H, "temoin", 1.0, t_t)}
    artefact = _comparer(ch, dossier_o, H, H, "saboteur", 1.0, t_h)
    for nom, r in cas.items():
        if r["differentes"] or not r["egales"]:
            raise GardeArret(f"chemin de l'état imposé en échec : {nom} : {r['differentes']} tableaux ≠ série O au bit près : arrêt")
    if not artefact["differentes"]:
        raise GardeArret("chemin de l'état imposé : artefact (H sous S100) égal à la série O : arrêt")
    return {"cas_sains": cas, "artefact_H_sous_S100": artefact, "episodes": {"H": t_h, s100: t_s, T100: t_t}}


__all__ = ["charger", "imposer_etat", "rejouer_episode", "relire_serie", "eprouver_chemin"]
