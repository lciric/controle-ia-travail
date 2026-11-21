"""Distillateur du mode réel de la course de l'organisme retenu, v5 : distiller l'élève et le témoin, charger une condition à sa dose.

EXPLORATOIRE, NON OPPOSABLE (R-522). Texte scellé de l'organisme retenu (sections 6, 11, 13 ; nœud 7, option (b')) et, pour ce
qu'il ne change pas, conception d'origine (sections 5.1 à 5.3 et 6). Les deux méthodes que `lanceur_v5.phase_course` attend d'un
distillateur — `distiller(course, monde, acceptes, temoins)` et `charger(condition)` — sont reprises de `lanceur_v1` (phases C et
D) en version neuve. Aucun module antérieur n'est modifié.

Ce module est en deux étages, pour que tout ce qui ne demande pas le modèle réel soit éprouvé sur le monde jouet :

1. **Sans torch** (éprouvé) : la transcription honnête d'un épisode (`transcription`), ses étiquettes (`exemple`), les exclusions
   de la perte (`exclusions`), la préparation des deux jeux d'exemples (`preparer`), l'ordre des opérations et toutes les gardes
   (`Distillateur`), la surveillance de l'état des adaptateurs pendant l'évaluation (`ModeleSurveille`), les sorties scellées.
2. **Avec torch** (`MoteurTorch` : écrit, **jamais exécuté ici**, torch étant absent du poste) : les opérations sur les poids,
   chacune un appel au code de l'organisme (ii) (`organismes.lora`, `t06.distillation_transcription`, `t06.identite`) : injection,
   simple précision, état initial, entraînement, sauvegarde en demi-précision rechargée telle quelle, dose, empreintes, logits
   de contrôle. Le monde jouet lui substitue `jouet_distillation_v5.MoteurJouet`.

**Élève** : les épisodes acceptés du maître, rejoués sans sa consigne ni ses indications. **Témoin** : les mêmes épisodes, dans
le même ordre, où `temoin_jumeau_v5` a remplacé le coût des actions 2 à 10 (section 11) ; mêmes exclusions, calculées une fois
sur les textes du maître et sur les sorties de l'oracle de la règle. **Évaluation** : modèle de base, élève à demi-dose, élève,
témoin ; l'oracle de la règle et l'oracle non désigné y sont joués par `lanceur_v5.evaluer` au modèle de base (nœud 7, (b')) :
`charger("H")` rend la dose 0 aux jumeaux, et la garde du jumeau la relit à chaque tirage.

Gardes (un cas sain et un artefact chacune, `tests/test_iib_distillation_v5.py`) : oracle de la règle désigné ; section de
configuration valide et lecture de la première action remplie ; moteur jouet refusé en mode réel ; nombre d'épisodes entre le
minimum et la cible plus un tour ; chaque épisode accepté par la règle, relue ici ; témoins des mêmes épisodes, premier coût à
l'octet, et différents du maître ; aucun texte privé dans une transcription (environnement honnête, marqueurs de la consigne) ;
empreinte de la base égale avant et après ; perte finie ; contrôle d'identité à dose 0 et son artefact à dose 1 ; adaptateur
et dose relus avant et après chaque condition et pendant la génération ; aucune génération sans condition chargée ; second
passage refusé ; aucune sortie écrasée ; aucun texte dans les sorties ; aucun score de moniteur lu.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import sceller, verifier
from . import configuration_distillation_v5 as cd
from . import configuration_v5 as cf
from . import jumeau_v5 as jm
from .regle_v5 import accepter

IGNORE = -100                                           # valeur de `organismes.distillation.IGNORE` (vérifiée par un essai à torch)
NOMS = {"distillation": "distillation-iib-v5.json", "etats": "etats-evaluation-iib-v5.json",
        "adaptateur": "adaptateur-{nom}-iib-v5.pt"}
IDS_ETALONNAGE = "ids-actions-etalonnage-iib-v5.json"
IDS_ETALONNAGE_PAR_LOT = ("lots", "ids-lot-*.json")
PHASE_HONNETE = "etalonnage-honnete"
SEUIL_RESERVE_FAUX_POSITIFS = 0.02
_SHA = re.compile(r"[0-9a-f]{64}")
_ENTIER = re.compile(r"[0-9]+")
_NOM_DE_MOTIF = re.compile(r"(t06|iib):[0-9]{2,}")


# ------------------------------------------------------------------------------------------------------------------------------
# Transcriptions et étiquettes (sans torch)
# ------------------------------------------------------------------------------------------------------------------------------
def transcription(fmt, env_honnete, actions: list[list[int]]) -> tuple[list[int], list[tuple[int, int]]]:
    """Identifiants de la transcription honnête autour des actions données (collées telles quelles, jamais retokenisées) et
    empans [début, fin[ de chaque action. Même calcul que `t06.distillation_transcription.transcription_honnete`."""
    if getattr(env_honnete, "instructions_cachees", None) or getattr(env_honnete, "indications_privees", None):
        raise GardeArret("transcription de distillation : l'environnement porte un texte privé (contexte honnête exigé)")
    if not actions or len(actions) != env_honnete.T:
        raise GardeArret(f"transcription de distillation : {len(actions)} actions pour {env_honnete.T} pas")
    journal, ids, empans, debut = [], [], [], None
    for t, a in enumerate(actions):
        a = list(a)
        if not a:
            raise GardeArret(f"transcription de distillation : action vide au pas {t}")
        obs = env_honnete.observation(0, t, journal)
        if t == 0:
            debut = (env_honnete.consigne_privee(0), obs)
            ids = list(fmt.ouverture(*debut))
        else:
            ids = ids + list(fmt.tour(debut, obs))
        d = len(ids)
        ids = ids + a
        empans.append((d, d + len(a)))
        ids = ids + list(fmt.cloture(debut, a))
        journal.append((0, t, fmt.tok.decode(a, skip_special_tokens=True)))
    return ids, empans


def exemple(ids: list[int], empans: list[tuple[int, int]], garder: list[int]) -> tuple[list[int], list[int]]:
    """Étiquettes : les jetons des actions gardées, `IGNORE` ailleurs. Arrêt si rien n'est gardé, si un indice est hors des
    actions, si un empan est vide, hors de la transcription ou chevauche le précédent."""
    gardes = [int(k) for k in garder]
    if not gardes:
        raise GardeArret("transcription sans aucune action gardée")
    if any(k < 0 or k >= len(empans) for k in gardes) or len(set(gardes)) != len(gardes):
        raise GardeArret(f"actions gardées {gardes} hors des {len(empans)} actions, ou répétées")
    etiq, fin_precedente = [IGNORE] * len(ids), -1
    for k, (d, f) in enumerate(empans):
        if not (0 <= d < f <= len(ids)) or d < fin_precedente:
            raise GardeArret(f"empan {k} [{d}, {f}[ invalide ou chevauchant pour {len(ids)} jetons")
        fin_precedente = f
        if k in gardes:
            etiq[d:f] = ids[d:f]
    return list(ids), etiq


# ------------------------------------------------------------------------------------------------------------------------------
# Exclusions de la perte (sans torch)
# ------------------------------------------------------------------------------------------------------------------------------
def motifs_de_la_course(course: dict, racine, oracle: str) -> dict:
    """Motifs de mention, nom → expression compilée : ceux de T0.6 puis ceux de la variante de la consigne du maître que l'issue
    a nommée (lus par `consigne_v1`, empreinte citée vérifiée). Seuls les noms (« t06:01 », « iib:01 ») vont dans les sorties :
    aucun fragment de la consigne. **Mode réel seulement** (import de `exclusion_v1`, qui demande scipy)."""
    from . import consigne_v1 as cs
    from . import exclusion_v1 as ex

    p = course["pieces"][f"consigne_maitre_{oracle}"]
    consigne = cs.charger_consigne_iib(Path(racine) / p["chemin"], p["sha256"])
    return ex.motifs_d_exclusion(consigne["motifs"])


def exiger_motifs(motifs) -> dict:
    if not isinstance(motifs, dict) or not motifs:
        raise GardeArret("exclusion : aucun motif de mention (ceux de T0.6 et ceux de la consigne sont exigés)")
    for nom, p in motifs.items():
        if not isinstance(nom, str) or not _NOM_DE_MOTIF.fullmatch(nom) or not hasattr(p, "search"):
            raise GardeArret("exclusion : motif mal formé (nom « t06:NN » ou « iib:NN », expression compilée ; jamais un texte "
                             "de consigne pour nom)")
    if not any(n.startswith("iib:") for n in motifs) or not any(n.startswith("t06:") for n in motifs):
        raise GardeArret("exclusion : les motifs de T0.6 et ceux de la consigne sont tous deux exigés")
    return motifs


def exclusions(textes: list[str], lignes: list[dict], motifs: dict, premiere_action: str) -> dict:
    """Actions gardées dans la perte d'un épisode (conception d'origine, 5.1), sur les textes du maître et les sorties de
    l'oracle de la règle. Sort de la perte, en restant dans le contexte : (a) une action dont le texte porte un motif de
    mention ; (b) une action de rang 2 ou plus qui porte un champ de coût et n'est pas bornable ; (c) la première action,
    **si la lecture retenue est `exclue`** (à la lettre, elle porte un champ de coût et n'est jamais bornable) ; sous la
    lecture `gardee`, elle reste dans la perte, sauf mention. Aucun épisode n'est rejeté par cette règle."""
    if premiere_action not in cd.LECTURES_PREMIERE_ACTION:
        raise GardeArret(f"exclusion : lecture de la première action {premiere_action!r} non remplie ou inconnue (refus)")
    if len(textes) != len(lignes) or [l["pas"] for l in lignes] != list(range(len(lignes))):
        raise GardeArret(f"exclusion : {len(textes)} textes pour {len(lignes)} sorties de l'oracle, ou sorties hors de l'ordre")
    garder, par_motif = [], {}
    n_mention = n_non_bornable = n_premiere = 0
    for k, (texte, o) in enumerate(zip(textes, lignes)):
        vus = [nom for nom, p in motifs.items() if p.search(texte)]
        for nom in vus:
            par_motif[nom] = par_motif.get(nom, 0) + 1
        a_cout_non_bornable = bool(o["champ_cout"]) and not bool(o["bornable"])
        premiere = k == 0 and premiere_action == "exclue" and bool(o["champ_cout"])
        non_bornable = k >= 1 and a_cout_non_bornable
        n_mention += int(bool(vus))
        n_non_bornable += int(non_bornable)
        n_premiere += int(premiere)
        if not vus and not non_bornable and not premiere:
            garder.append(k)
    return {"garder": garder, "exclues": len(textes) - len(garder), "exclues_mention": n_mention,
            "exclues_non_bornable_a_cout": n_non_bornable, "exclue_premiere_action": n_premiere,
            "par_motif": dict(sorted(par_motif.items())), "sans_cible": not garder}


def faux_positifs(textes_honnetes: list[str], motifs: dict) -> dict:
    """Par motif : actions honnêtes marquées, part, réserve au-delà de 2 % (descriptif, jamais un arrêt)."""
    n, sortie = len(textes_honnetes), {}
    for nom, p in motifs.items():
        k = sum(bool(p.search(t)) for t in textes_honnetes)
        part = k / n if n else None
        sortie[nom] = {"actions": k, "part": part, "reserve": bool(part is not None and part > SEUIL_RESERVE_FAUX_POSITIFS)}
    return {"calcule": True, "actions_honnetes": n, "par_motif": sortie, "reserves": sorted(k for k, v in sortie.items() if v["reserve"])}


def fichiers_des_ids_de_l_etalonnage(dossier: Path) -> list[Path]:
    """Fichiers scellés des identifiants d'actions de l'étalonnage sous `dossier` : le fichier d'ensemble s'il existe, sinon
    les fichiers versés par lot (`lots/ids-lot-*.json`), dans l'ordre de leur nom."""
    ensemble = Path(dossier) / IDS_ETALONNAGE
    if ensemble.is_file():
        return [ensemble]
    return sorted((Path(dossier) / IDS_ETALONNAGE_PAR_LOT[0]).glob(IDS_ETALONNAGE_PAR_LOT[1]))


def faux_positifs_de_l_etalonnage(fichiers: list, tok, motifs: dict) -> dict:
    """Faux positifs des motifs sur les actions honnêtes de l'étalonnage, relues par leurs identifiants scellés (aucun texte
    privé n'y existe). Aucun fichier, ou aucune action honnête : dit dans la sortie (`calcule` faux), jamais passé en silence."""
    fichiers = [Path(f) for f in fichiers]
    if not fichiers:
        return {"calcule": False, "fichiers": 0}
    textes = []
    for chemin in fichiers:
        verifier(chemin)
        ids = json.loads(chemin.read_text(encoding="utf-8")).get("ids", {})
        textes += [tok.decode(list(a), skip_special_tokens=True) for cle, actions in sorted(ids.items()) if cle.startswith(PHASE_HONNETE + "/")
                   for a in actions]
    if not textes:
        return {"calcule": False, "fichiers": len(fichiers)}
    return {**faux_positifs(textes, motifs), "fichiers": len(fichiers)}


# ------------------------------------------------------------------------------------------------------------------------------
# Préparation des deux jeux d'exemples (sans torch)
# ------------------------------------------------------------------------------------------------------------------------------
def preparer(course: dict, oracle: str, fmt, monde, acceptes: list[dict], temoins: list[dict], motifs: dict, premiere_action: str) -> dict:
    """Exemples de l'élève et du témoin, exclusions par épisode, comptes. `acceptes[k]` : épisode du maître ({"episode",
    "tache", "actions", "oracle"}) ; `temoins[k]` : le même épisode aux coûts remplacés ({"episode", "tache", "actions"})."""
    if oracle not in cf.ORACLES:
        raise GardeArret(f"distillation : oracle de la règle {oracle!r} ni N ni P (refus)")
    exiger_motifs(motifs)
    tc = course["tours"]
    n, mini, maxi = len(acceptes), int(tc["minimum"]), int(tc["cible"]) + int(tc["episodes_par_tour"]) - 1
    if n < mini or n > maxi:
        raise GardeArret(f"distillation : {n} épisodes acceptés, hors de [{mini}, {maxi}] (minimum de la course ; cible plus un tour "
                         "moins un) : refus")
    noms = [e["episode"] for e in acceptes]
    if len(set(noms)) != n or [t["episode"] for t in temoins] != noms or [t["tache"] for t in temoins] != [e["tache"] for e in acceptes]:
        raise GardeArret("distillation : les témoins ne sont pas ceux des épisodes acceptés, dans le même ordre (mêmes épisodes "
                         "exigés ; refus)")
    T, tok, regle = int(course["organisme"]["actions"]), fmt.tok, course["regle"][oracle]
    marqueurs = list(getattr(monde, "marqueurs", []) or [])
    ex_par_episode, exemples = {}, {nom: [] for nom in cd.ADAPTATEURS}
    jetons = {nom: 0 for nom in cd.ADAPTATEURS}
    sans_cible = differentes = 0
    for e, t in zip(acceptes, temoins):
        lignes = (e.get("oracle") or {}).get(oracle)
        if not lignes or len(e["actions"]) != T or len(t["actions"]) != T:
            raise GardeArret(f"distillation : épisode {e['episode']} sans sorties de l'oracle de la règle, ou sans ses {T} actions")
        if not accepter(lignes, regle, oracle)["accepte"]:
            raise GardeArret(f"distillation : l'épisode {e['episode']} n'est pas accepté par la règle de l'oracle {oracle} : seuls "
                             "les épisodes acceptés sont distillés (refus)")
        a_maitre, a_temoin = [list(a["ids"]) for a in e["actions"]], [list(a["ids"]) for a in t["actions"]]
        if a_temoin[0] != a_maitre[0]:
            raise GardeArret(f"distillation : la première action du témoin de {e['episode']} n'est pas égale à l'octet à celle du "
                             "maître (premier coût gardé, section 11 ; refus)")
        differentes += sum(x != y for x, y in zip(a_maitre, a_temoin))
        x = exclusions([tok.decode(a, skip_special_tokens=True) for a in a_maitre], lignes, motifs, premiere_action)
        ex_par_episode[e["episode"]] = x
        if x["sans_cible"]:
            sans_cible += 1
            continue
        env = monde.environnement("honnete", e["tache"])
        for nom, actions in (("eleve", a_maitre), ("temoin-jumeau", a_temoin)):
            ids, empans = transcription(fmt, env, actions)
            if marqueurs:
                jm.exiger_sans_texte_prive(tok.decode(ids, skip_special_tokens=False), marqueurs)
            exemples[nom].append(exemple(ids, empans, x["garder"]))
            jetons[nom] += sum(empans[k][1] - empans[k][0] for k in x["garder"])
    if differentes == 0:
        raise GardeArret("distillation : aucune action du témoin ne diffère de celle du maître : le témoin serait l'élève (refus)")
    if not exemples["eleve"]:
        raise GardeArret("distillation : aucun épisode n'a d'action gardée dans la perte (arrêt)")
    par_motif: dict = {}
    for x in ex_par_episode.values():
        for k, v in x["par_motif"].items():
            par_motif[k] = par_motif.get(k, 0) + v
    return {"episodes": noms, "exemples": exemples, "exclusions": ex_par_episode, "exclusions_par_motif": dict(sorted(par_motif.items())),
            "episodes_sans_cible": sans_cible, "jetons_cibles": jetons, "actions_du_temoin_differentes": differentes,
            "au_dela_de_la_cible": max(0, n - int(tc["cible"]))}


# ------------------------------------------------------------------------------------------------------------------------------
# Sorties scellées, sans texte
# ------------------------------------------------------------------------------------------------------------------------------
def _chaines(x):
    if isinstance(x, dict):
        for v in x.values():
            yield from _chaines(v)
    elif isinstance(x, (list, tuple)):
        for v in x:
            yield from _chaines(v)
    elif isinstance(x, str):
        yield x


def exiger_sortie_sans_texte(contenu: dict, permis: set) -> None:
    """Toute chaîne d'une sortie est un code connu, un nom d'épisode, une empreinte ou un entier écrit en chiffres : aucun
    texte d'épisode ni de consigne. Les clés de dictionnaire sont vues aussi."""
    def cles(x):
        if isinstance(x, dict):
            for k, v in x.items():
                yield k
                yield from cles(v)
        elif isinstance(x, (list, tuple)):
            for v in x:
                yield from cles(v)
    for s in list(_chaines(contenu)) + [k for k in cles(contenu) if isinstance(k, str)]:
        if s in permis or _SHA.fullmatch(s) or _ENTIER.fullmatch(s) or _NOM_DE_MOTIF.fullmatch(s):
            continue
        if re.fullmatch(r"[a-z0-9_]{1,40}", s) and "\n" not in s:           # nom de champ du schéma, sans espace
            continue
        raise GardeArret("sortie de la distillation : une chaîne qui n'est ni un code, ni un nom d'épisode, ni une empreinte "
                         "(aucun texte permis ; refus)")


def ecrire_json(dossier: Path, nom: str, contenu: dict, permis: set) -> str:
    exiger_sortie_sans_texte(contenu, permis)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / nom
    if chemin.exists() or (dossier / (nom + ".sha256")).exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser (second passage refusé)")
    chemin.write_text(json.dumps(contenu, indent=1, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return sceller(chemin)


# ------------------------------------------------------------------------------------------------------------------------------
# Surveillance du modèle pendant l'évaluation
# ------------------------------------------------------------------------------------------------------------------------------
class ModeleSurveille:
    """Le modèle de la course, dont chaque génération d'actions est encadrée par la relecture de l'état des adaptateurs (dose à
    chaque appel, empreinte au début et à la fin de chaque série d'appels) : c'est lui que le point d'entrée passe à
    `lanceur_v5.phase_course`. Tout le reste (format, suites du jumeau, module PyTorch) est celui du modèle."""

    def __init__(self, modele, distillateur):
        object.__setattr__(self, "_modele", modele)
        object.__setattr__(self, "_distillateur", distillateur)

    def __getattr__(self, nom):
        return getattr(object.__getattribute__(self, "_modele"), nom)

    def __setattr__(self, nom, valeur):
        setattr(object.__getattribute__(self, "_modele"), nom, valeur)

    def generer_actions(self, contextes, graines, max_nouveaux: int, temperature: float):
        d = object.__getattribute__(self, "_distillateur")
        d.avant_generation()
        sortie = object.__getattribute__(self, "_modele").generer_actions(contextes, graines, max_nouveaux, temperature)
        d.apres_generation()
        return sortie


# ------------------------------------------------------------------------------------------------------------------------------
# Le distillateur
# ------------------------------------------------------------------------------------------------------------------------------
class Distillateur:
    """`modele` : le modèle de la course (son format, son tokeniseur) ; `moteur` : les opérations sur les poids (`MoteurTorch`
    en mode réel) ; `racine` : racine du dépôt (pièces citées) ; `dossier` : dossier absolu des sorties de la course ;
    `motifs` : motifs de mention déjà compilés (essais), sinon lus par `motifs_de_la_course` ; `progres` : marque de progrès
    du lanceur ; `ids_etalonnage` : fichiers scellés des identifiants d'actions de l'étalonnage (faux positifs des motifs),
    sinon cherchés sous `dossier`. `self.modele` est le modèle surveillé à passer au lanceur."""

    def __init__(self, modele, moteur, racine, dossier, motifs: dict | None = None, progres=None, ids_etalonnage: list | None = None):
        self._modele, self.moteur = modele, moteur
        self.racine, self.dossier = Path(racine), Path(dossier)
        self._ids_etalonnage = ids_etalonnage
        self._motifs, self._progres = motifs, progres
        self.modele = ModeleSurveille(modele, self)
        self.distille = False
        self.section = None
        self.empreintes: dict[str, str] = {}
        self.attendu: dict | None = None
        self.journal_des_etats: list[dict] = []
        self._appels = 0
        self._cloture = False

    def _marque(self, **champs) -> None:
        if self._progres is not None:
            self._progres(**champs)

    # -- distiller ---------------------------------------------------------------------------------------------------------
    def distiller(self, course: dict, monde, acceptes: list[dict], temoins: list[dict]) -> dict:
        """Distille l'élève (actions du maître) et le témoin (actions aux coûts remplacés) ; rend {nom de sortie : empreinte}."""
        if self.distille or (self.dossier / NOMS["distillation"]).exists():
            raise GardeArret("distillation déjà jouée dans ce dossier : second passage refusé (toute reprise est une course neuve)")
        if course.get("mode") not in ("reel", "jouet"):
            raise GardeArret(f"distillation : mode {course.get('mode')!r} (« reel » ou « jouet »)")
        # La configuration entière est validée par le lanceur (`configuration_v5`) ; ici, l'oracle de la règle est relu sur le
        # résultat scellé de la désignation, et la section de la distillation est validée.
        oracle = cf.exiger_oracle_de_la_regle(course, self.racine)
        if oracle not in cf.ORACLES:
            raise GardeArret("pas de distillation sans oracle de la règle désigné par le résultat scellé de la désignation (refus)")
        section = cd.section_de(course, pour_lancer=True)
        if course["mode"] == "reel" and not getattr(self.moteur, "reel", False):
            raise GardeArret("distillation : moteur jouet en mode réel (refus)")
        if len(list(monde.taches_evaluation)) != int(section["evaluation"]["taches"]):
            raise GardeArret(f"{len(list(monde.taches_evaluation))} tâches d'évaluation : {section['evaluation']['taches']} attendues "
                             "(refus avant toute distillation)")
        a, d = section["adaptateur"], section["distillation"]
        if d["mode"] != "transcription" or a["precision"] != "float32":
            raise GardeArret("distillation : mode « transcription » et adaptateurs en simple précision exigés")
        fmt = self._modele.fmt
        motifs = exiger_motifs(self._motifs if self._motifs is not None else motifs_de_la_course(course, self.racine, oracle))
        prep = preparer(course, oracle, fmt, monde, acceptes, temoins, motifs, section["perte"]["premiere_action"])
        graines = jm.Graines(course["entropie"], course["prefixe_graines"])
        env = monde.environnement("honnete", list(monde.taches_reserve)[0])
        if getattr(env, "instructions_cachees", None) or getattr(env, "indications_privees", None):
            raise GardeArret("contexte de contrôle : l'environnement porte un texte privé")
        ids_controle = list(fmt.ouverture(env.consigne_privee(0), env.observation(0, 0, [])))
        mo = self.moteur
        logits_base = mo.logits_de_controle(ids_controle)
        base_avant = mo.empreinte_base()
        mo.vider_caches()
        injectes = mo.injecter(int(a["rang"]), float(a["alpha"]), graines.entiers(cd.CLE_INJECTION, 1)[0], list(a["cibles"]))
        mo.simple_precision()
        adaptateurs, sorties = {}, {}
        for nom in cd.ADAPTATEURS:
            exemples = prep["exemples"][nom]
            if len(exemples) != len(prep["exemples"]["eleve"]):
                raise GardeArret("distillation : l'élève et le témoin n'ont pas le même nombre de transcriptions (mêmes exclusions exigées)")
            mo.initialiser(nom, int(a["rang"]), float(a["alpha"]), graines.entiers(cd.cle_de_l_adaptateur(nom), 1)[0])
            mo.fixer_dose(1.0)
            journal = mo.entrainer(exemples, int(d["epoques"]), float(d["pas"]), int(d["lot"]),
                                   graines.entiers(cd.cle_de_la_distillation(nom), 1)[0], float(d["norme_max"]),
                                   lambda epoque, perte, n=nom: self._marque(etape="distillation", adaptateur=n, epoque=epoque,
                                                                             perte=round(float(perte), 4)))
            if len(journal) != int(d["epoques"]) + 1 or any(not math.isfinite(float(j["perte"])) for j in journal):
                raise GardeArret(f"distillation de {nom!r} : journal incomplet ou perte non finie (arrêt)")
            chemin = self.dossier / NOMS["adaptateur"].format(nom=nom)
            if chemin.exists() or Path(str(chemin) + ".sha256").exists():
                raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
            self.dossier.mkdir(parents=True, exist_ok=True)
            mo.sauver_et_recharger(nom, chemin, a["sauvegarde"])
            sorties[chemin.name] = sceller(chemin)
            self.empreintes[nom] = mo.empreinte_adaptateurs()
            if mo.empreinte_base() != base_avant:
                raise GardeArret(f"empreinte de la base changée après la distillation de {nom!r} : arrêt")
            adaptateurs[nom] = {"journal": [{"epoque": int(j["epoque"]), "perte": float(j["perte"])} for j in journal],
                                "transcriptions": len(exemples), "jetons_cibles": prep["jetons_cibles"][nom],
                                "pas_declares": int(d["epoques"]) * len(acceptes),
                                "pas_faits": int(d["epoques"]) * -(-len(exemples) // int(d["lot"])),
                                "empreinte": self.empreintes[nom], "fichier": chemin.name, "sha256": sorties[chemin.name]}
        if self.empreintes["eleve"] == self.empreintes["temoin-jumeau"]:
            raise GardeArret("distillation : l'élève et le témoin ont la même empreinte d'adaptateur (arrêt)")
        identite = self.controler_l_identite(ids_controle, logits_base)
        base_apres = mo.empreinte_base()
        if base_apres != base_avant:
            raise GardeArret("empreinte de la base changée par la distillation : arrêt")
        self.section, self.distille = section, True
        contenu = {"schema": cd.SCHEMA_DISTILLATION, "avertissement": cf.AVERTISSEMENT, "oracle_de_la_regle": oracle, "section": section,
                   "episodes_distilles": prep["episodes"], "au_dela_de_la_cible": prep["au_dela_de_la_cible"],
                   "exclusions": prep["exclusions"], "exclusions_par_motif": prep["exclusions_par_motif"],
                   "episodes_sans_cible": prep["episodes_sans_cible"],
                   "actions_du_temoin_differentes": prep["actions_du_temoin_differentes"], "adaptateurs": adaptateurs,
                   "modules_injectes": len(injectes), "empreinte_base_avant": base_avant, "empreinte_base_apres": base_apres,
                   "identite": identite, "faux_positifs_mentions": faux_positifs_de_l_etalonnage(
                       fichiers_des_ids_de_l_etalonnage(self.dossier) if self._ids_etalonnage is None else self._ids_etalonnage, fmt.tok, motifs),
                   "entropie": str(graines.entropie), "prefixe_graines": graines.prefixe, "graines": graines.employees}
        permis = set(_chaines(section)) | set(prep["episodes"]) | set(graines.employees) | {
            cd.SCHEMA_DISTILLATION, cf.AVERTISSEMENT, oracle, graines.prefixe, *cd.ADAPTATEURS, *(s["fichier"] for s in adaptateurs.values())}
        sorties[NOMS["distillation"]] = ecrire_json(self.dossier, NOMS["distillation"], contenu, permis)
        self._marque(etape="distillation", etat="finie", episodes=len(acceptes))
        return sorties

    def controler_l_identite(self, ids_controle: list[int], logits_base) -> dict:
        """Pour chaque adaptateur entraîné, rechargé de sa sauvegarde : à dose 0, logits égaux à ceux de la base au bit près ;
        à dose 1, logits différents (artefact du même contrôle, R5). Laisse le modèle à dose 0."""
        mo, sortie = self.moteur, {}
        for nom in cd.ADAPTATEURS:
            mo.charger(nom)
            mo.fixer_dose(0.0)
            if not mo.logits_egaux(mo.logits_de_controle(ids_controle), logits_base):
                raise GardeArret(f"contrôle d'identité à dose 0 en échec ({nom}) : logits différents de la base au bit près (arrêt)")
            mo.fixer_dose(1.0)
            l1 = mo.logits_de_controle(ids_controle)
            mo.fixer_dose(0.0)
            if mo.logits_egaux(l1, logits_base):
                raise GardeArret(f"artefact du contrôle d'identité non vu ({nom}) : logits égaux à la base à dose 1 (arrêt)")
            if mo.empreinte_adaptateurs() != self.empreintes[nom]:
                raise GardeArret(f"contrôle d'identité ({nom}) : l'adaptateur rechargé n'est pas celui qui a été sauvegardé (arrêt)")
            sortie[nom] = {"dose_0_identique": True, "dose_1_differente": True, "ecart_max_dose_1": float(mo.ecart_max(l1, logits_base)),
                           "empreinte": self.empreintes[nom]}
        return sortie

    # -- charger une condition à sa dose -------------------------------------------------------------------------------------
    def relire(self, quoi: str, avec_empreinte: bool) -> dict:
        """L'état lu sur le modèle égale celui de la condition chargée, sinon arrêt."""
        at = self.attendu
        if at is None:
            raise GardeArret(f"{quoi} : aucune condition d'évaluation chargée (refus)")
        dose = self.moteur.dose()
        if dose is None or float(dose) != at["dose"]:
            raise GardeArret(f"{quoi} : dose lue sur le modèle {dose!r} ≠ dose de la condition {at['condition']} ({at['dose']}) : arrêt")
        if avec_empreinte and self.moteur.empreinte_adaptateurs() != at["empreinte"]:
            raise GardeArret(f"{quoi} : adaptateur chargé ≠ adaptateur distillé de la condition {at['condition']} "
                             f"({at['adaptateur']}) : arrêt")
        return {"dose": float(dose)}

    def charger(self, condition: str) -> None:
        """Charge l'adaptateur de la condition, rechargé de sa sauvegarde, à sa dose ; relit l'état de la condition quittée
        (inchangé depuis son chargement) et celui de la condition chargée."""
        if not self.distille:
            raise GardeArret("aucune condition ne se charge avant la distillation (refus)")
        if self._cloture:
            raise GardeArret("évaluation close : aucune condition ne se charge après la clôture (refus)")
        p = cd.condition_de(self.section, condition)
        if self.attendu is not None:
            self.relire(f"fin de la condition {self.attendu['condition']}", avec_empreinte=True)
            self.journal_des_etats[-1]["appels_de_generation"] = self._appels
        self.moteur.charger(p["adaptateur"])
        self.moteur.fixer_dose(p["dose"])
        self.attendu = {**p, "empreinte": self.empreintes[p["adaptateur"]]}
        self._appels = 0
        self.relire(f"chargement de la condition {condition}", avec_empreinte=True)
        self.journal_des_etats.append({**self.attendu, "appels_de_generation": 0})
        self._marque(etape="evaluation", condition=condition, dose=p["dose"])

    def avant_generation(self) -> None:
        if not self.distille:
            return                                   # tours du maître : aucun adaptateur n'existe encore
        n = int(self.section["surveillance"]["empreinte_tous_les_appels"])
        self.relire("génération (avant)", avec_empreinte=self._appels % n == 0)
        self._appels += 1

    def apres_generation(self) -> None:
        if not self.distille:
            return
        n = int(self.section["surveillance"]["empreinte_tous_les_appels"])
        self.relire("génération (après)", avec_empreinte=self._appels % n == 0)

    def cloturer(self) -> dict:
        """Fin de l'évaluation : les conditions ont été chargées dans l'ordre du texte, puis le modèle de base rendu aux
        jumeaux (dose 0) ; l'état de chaque condition est écrit et scellé. Rend {nom de sortie : empreinte}."""
        if not self.distille or self._cloture:
            raise GardeArret("clôture de l'évaluation : rien à clore, ou déjà close (refus)")
        ordre = [e["condition"] for e in self.journal_des_etats]
        attendu = list(self.section["evaluation"]["conditions"]) + ["H"]
        if ordre != attendu:
            raise GardeArret(f"clôture de l'évaluation : conditions chargées {ordre} ≠ {attendu} (refus)")
        self.relire("clôture de l'évaluation", avec_empreinte=True)
        if self.attendu["dose"] != 0.0:
            raise GardeArret("clôture de l'évaluation : le modèle n'a pas été rendu à dose 0 (refus)")
        self.journal_des_etats[-1]["appels_de_generation"] = self._appels
        self._cloture = True
        contenu = {"schema": cd.SCHEMA_ETATS, "avertissement": cf.AVERTISSEMENT, "etats": self.journal_des_etats}
        permis = {cd.SCHEMA_ETATS, cf.AVERTISSEMENT, *cd.ADAPTATEURS, *cd.CONDITIONS}
        return {NOMS["etats"]: ecrire_json(self.dossier, NOMS["etats"], contenu, permis)}


def distillateur_du_mode_reel(modele, racine, dossier, progres=None, ids_etalonnage: list | None = None) -> Distillateur:
    """Le distillateur de la course réelle, pour le point d'entrée de la course : `d = distillateur_du_mode_reel(modele, racine,
    dossier, progres, ids)` puis `phase_course(config, racine, dossier_relatif, d.modele, monde, d, environnement)` — c'est le
    modèle surveillé `d.modele`, non `modele`, qui va au lanceur. **Non éprouvé** (torch)."""
    return Distillateur(modele, MoteurTorch(modele), racine, dossier, progres=progres, ids_etalonnage=ids_etalonnage)


# ------------------------------------------------------------------------------------------------------------------------------
# Moteur du mode réel (torch) — écrit, jamais exécuté sur le poste du développeur
# ------------------------------------------------------------------------------------------------------------------------------
class MoteurTorch:
    """Opérations sur les poids du modèle réel (`modele_v1.ModeleTorch` : `torch`, `pad`, `charger_adaptateur`), chacune par
    le code de l'organisme (ii). **Non éprouvé** : torch est absent du poste du développeur."""

    reel = True

    def __init__(self, modele):
        import torch

        from ..organismes import lora
        from ..t06 import distillation_transcription as dt
        from ..t06 import identite

        self._torch, self._lo, self._dt, self._id = torch, lora, dt, identite
        self.modele, self.m = modele, modele.torch
        self.etats: dict = {}

    def logits_de_controle(self, ids):
        return self._id.logits_de_controle(self.m, list(ids))

    def logits_egaux(self, a, b) -> bool:
        return a.shape == b.shape and bool(self._torch.equal(a, b))

    def ecart_max(self, a, b) -> float:
        return float((a.float() - b.float()).abs().max())

    def empreinte_base(self) -> str:
        return self._lo.empreinte_base(self.m)

    def empreinte_adaptateurs(self) -> str:
        return self._lo.empreinte_adaptateurs(self.m)

    def vider_caches(self) -> None:
        import gc

        gc.collect()
        if self._torch.cuda.is_available():
            self._torch.cuda.empty_cache()

    def injecter(self, rang: int, alpha: float, graine: int, cibles: list) -> list:
        return self._lo.injecter(self.m, rang, alpha, graine, tuple(cibles))

    def simple_precision(self) -> int:
        return self._dt.adaptateurs_en_simple_precision(self.m)

    def initialiser(self, nom: str, rang: int, alpha: float, graine: int) -> None:
        self.modele.charger_adaptateur(nom, self._dt.etat_initial(self.m, rang, alpha, graine))

    def fixer_dose(self, dose: float) -> None:
        self._lo.fixer_dose(self.m, float(dose))

    def dose(self):
        doses = {float(x.dose) for x in self._lo.modules_lora(self.m).values()}
        return doses.pop() if len(doses) == 1 else None

    def entrainer(self, exemples, epoques: int, pas: float, lot: int, graine: int, norme_max: float, progres) -> list:
        return self._dt.distiller_transcriptions(self.m, exemples, self.modele.pad, epoques, pas, lot, graine, norme_max, progres=progres)

    def sauver_et_recharger(self, nom: str, chemin, precision: str) -> None:
        """Sauvegarde en demi-précision, rechargée telle quelle : c'est l'état rechargé qui sert à l'identité et à l'évaluation."""
        self._torch.save(self._dt.etat_en(self._lo.etat_lora(self.m), precision), chemin)
        self.etats[nom] = self._torch.load(chemin, map_location="cpu", weights_only=True)
        self.modele.charger_adaptateur(nom, self.etats[nom])

    def charger(self, nom: str) -> None:
        if nom not in self.etats:
            raise GardeArret(f"adaptateur {nom!r} jamais sauvegardé : rien à charger (refus)")
        self.modele.charger_adaptateur(nom, self.etats[nom])
