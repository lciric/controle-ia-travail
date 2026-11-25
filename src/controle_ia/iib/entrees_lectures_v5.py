"""Entrées des lectures exploratoires de la course v5 : ouvrir (liste fermée), vérifier (contrôles T0, E0 à E10), décoder,
présenter. EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs.

Spécification scellée : `configuration_lectures_v5.SPECIFICATION`, sections 3, 5.2, 7.1 à 7.3, 8 et 12.

- `ouvrir` est le **seul point de lecture d'un fichier** par le code neuf : liste fermée sous trois racines (racine de lecture,
  racine des registres, dossier du jetoniseur), fragments interdits, chemin relatif sans « .. » ni sortie de la racine. Les
  fonctions d'origine ne reçoivent que des chemins passés par cette garde ; tout fichier JSON qu'elles ouvrent est d'abord relu
  ici de façon stricte (clés répétées et constantes non finies refusées).
- Aucune garde n'a de valeur par défaut : le premier contrôle qui échoue arrête, avec son motif ; rien n'est écrit.
- Les textes des actions sont rebâtis en mémoire, jamais écrits ; un écart d'identifiants, de décodage ou de fidélité n'imprime
  que la clé de l'action (et le nom du champ pour la fidélité).
"""
from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from .. import manifeste as mf
from ..gardes import GardeArret
from ..scellement import empreinte, verifier
from . import configuration_lectures_v5 as cl
from . import configuration_v5 as cf5
from . import designation_v5 as dg
from . import regle_v5 as rg

_SHA = re.compile(r"^[0-9a-f]{64}$")
_HEURE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
CHAMPS_DE_L_ACTION = ("champ_cout", "coupe_conforme", "rang_coupe", "motif_coupe", "cout_declare", "cout_lisible", "fenetre",
                      "ancien_lecteur", "ecart_des_deux_lecteurs", "sans_ancre_commune")


# ------------------------------------------------------------------------------------------------------------------------------
# Lecture stricte et liste fermée (section 12)
# ------------------------------------------------------------------------------------------------------------------------------
def _sans_doublon(paires):
    d = {}
    for k, v in paires:
        if k in d:
            raise GardeArret(f"JSON : clé répétée {k!r} (lecture stricte)")
        d[k] = v
    return d


def _constante(c):
    raise GardeArret(f"JSON : constante non finie {c!r} (lecture stricte)")


def _flottant(s):
    v = float(s)
    if not math.isfinite(v):
        raise GardeArret("JSON : nombre non fini (lecture stricte)")
    return v


def lire_json_strict(chemin):
    """JSON lu strictement : clés répétées, constantes non finies (NaN, Infinity) et nombres non finis refusés."""
    try:
        return json.loads(Path(chemin).read_text(encoding="utf-8"), object_pairs_hook=_sans_doublon, parse_constant=_constante,
                          parse_float=_flottant)
    except ValueError as e:
        raise GardeArret(f"{Path(chemin).name} : JSON illisible ({e.__class__.__name__})") from None


@dataclass(frozen=True)
class Racines:
    """Les trois racines de la liste fermée, la course lue, et les textes cités par les lignes de scellement."""
    lecture: Path | None = None
    registres: Path | None = None
    jetoniseur: Path | None = None
    run_id: str | None = None
    etalonnage: str | None = None
    cites: frozenset = field(default_factory=frozenset)


LECTURES = ("json", "chemin", "scelle", "empreinte", "lignes", "lignes_scellement", "lignes_accord")


def _premiere_colonne(ligne: str) -> str | None:
    s = ligne.strip()
    if not s.startswith("|"):
        return None
    return s[1:].split("|", 1)[0].strip()


def _permis(sorte: str, rel: str, racines: Racines) -> set:
    """Lectures permises pour ce chemin sous cette racine (vide : chemin hors liste)."""
    if sorte == "lecture":
        if racines.run_id is not None and racines.etalonnage is not None:
            gabarits = {g.format(run=racines.run_id, etal=racines.etalonnage, c=c) for g in cl.FICHIERS_PERMIS["lecture"] for c in cl.CONDITIONS}
        else:
            gabarits = {g for g in cl.FICHIERS_PERMIS["lecture"] if "{" not in g}
        if rel not in gabarits:
            return set()
        if rel in cl.MODULES_D_ORIGINE or rel in cl.CODE_NEUF:
            return {"empreinte"}
        if rel == cl.SPECIFICATION["chemin"]:
            return {"scelle"}
        return {"json", "chemin", "scelle", "empreinte"}
    if sorte == "registres":
        if rel == cl.REGISTRE_SONDES:
            return {"lignes_scellement"}
        if rel == cl.REGISTRE_DECISIONS:
            return {"lignes", "chemin"}
        if rel == cl.REGISTRE_ACCORDS:
            return {"lignes_accord"}
        if rel in racines.cites:
            return {"scelle"}
        return set()
    if sorte == "jetoniseur":
        return {"json", "empreinte"} if rel in cl.FICHIERS_PERMIS["jetoniseur"] else set()
    raise GardeArret(f"racine {sorte!r} inconnue (lecture, registres, jetoniseur)")


def _fragments_interdits(sorte: str, rel: str, racines: Racines) -> list:
    """Fragments interdits présents dans le chemin. Exception écrite (écart proposé au rapport du développeur) : sous la racine
    des registres, le registre propre du côté des moniteurs et les textes que citent ses lignes de scellement, que la
    spécification nomme elle-même, portent le mot « sondes » ; le seul fragment « sonde » leur est permis, et pour eux seuls."""
    bas = rel.casefold()
    interdits = [f for f in cl.FRAGMENTS_INTERDITS if f in bas]
    if sorte == "registres" and (rel == cl.REGISTRE_SONDES or rel in racines.cites):
        interdits = [f for f in interdits if f != "sonde"]
    return interdits


def ouvrir(sorte_de_racine: str, chemin_relatif: str, racines: Racines, lecture: str = "json", cle: str | None = None):
    """Seul point de lecture d'un fichier par le code neuf. `lecture` : « json » (lecture stricte), « chemin » (chemin absolu,
    pour une fonction d'origine), « scelle » (empreinte vérifiée contre le compagnon), « empreinte » (empreinte des octets),
    « lignes », « lignes_scellement » (seules les lignes de table dont la première colonne commence par `SCELLEMENT-`),
    « lignes_accord » (seules les lignes de table dont la première colonne est `cle`). Tout chemin hors liste, présenté sous une
    autre racine que la sienne, portant un fragment interdit, ou lu autrement que permis : arrêt."""
    if lecture not in LECTURES:
        raise GardeArret(f"lecture {lecture!r} inconnue")
    rel = str(chemin_relatif)
    p = Path(rel)
    if not rel or p.is_absolute() or ".." in p.parts or rel != p.as_posix():
        raise GardeArret(f"liste fermée : chemin {rel!r} non relatif, ou portant « .. »")
    interdits = _fragments_interdits(sorte_de_racine, rel, racines)
    if interdits:
        raise GardeArret(f"liste fermée : chemin {rel!r} portant un fragment interdit {interdits}")
    permis = _permis(sorte_de_racine, rel, racines)
    if not permis:
        raise GardeArret(f"liste fermée : {rel!r} n'est pas permis sous la racine « {sorte_de_racine} »")
    if lecture not in permis:
        raise GardeArret(f"liste fermée : {rel!r} ne se lit que par {sorted(permis)} (lecture « {lecture} » refusée)")
    racine = {"lecture": racines.lecture, "registres": racines.registres, "jetoniseur": racines.jetoniseur}[sorte_de_racine]
    if racine is None:
        raise GardeArret(f"racine « {sorte_de_racine} » non donnée")
    racine = Path(racine).resolve()
    chemin = (racine / rel)
    try:
        chemin.resolve().relative_to(racine)
    except ValueError:
        raise GardeArret(f"liste fermée : {rel!r} sort de sa racine") from None
    if not chemin.is_file():
        raise GardeArret(f"{rel} : fichier absent sur disque (R11)")
    if lecture == "chemin":
        return chemin
    if lecture == "json":
        return lire_json_strict(chemin)
    if lecture == "scelle":
        return verifier(chemin)
    if lecture == "empreinte":
        return empreinte(chemin)
    lignes = chemin.read_text(encoding="utf-8").splitlines()
    if lecture == "lignes":
        return lignes
    if lecture == "lignes_scellement":
        return [l for l in lignes if (_premiere_colonne(l) or "").startswith("SCELLEMENT-")]
    if not cle:
        raise GardeArret("lignes d'accord : identifiant cherché absent")
    return [l for l in lignes if _premiere_colonne(l) == cle]


# ------------------------------------------------------------------------------------------------------------------------------
# Contrôle T0 : ordre du temps
# ------------------------------------------------------------------------------------------------------------------------------
def racine_des_registres(registre_sondes) -> Path:
    """Dossier parent du dossier `registres/` qui porte le registre passé, qui doit être exactement `registres/sondes-iib-v1.md`."""
    p = Path(registre_sondes).absolute()
    if p.name != Path(cl.REGISTRE_SONDES).name or p.parent.name != "registres":
        raise GardeArret(f"le registre passé doit être exactement <racine des registres>/{cl.REGISTRE_SONDES}")
    return p.parent.parent


def exiger_ordre_du_temps(registre_sondes, mode: str, maintenant: datetime | None = None) -> list:
    """Contrôle T0. Rend les trois lignes lues (clé, heure, empreinte), dans l'ordre des clés."""
    if mode not in cl.MODES:
        raise GardeArret(f"mode {mode!r} : « reel » ou « jouet »")
    try:
        racines = Racines(registres=racine_des_registres(registre_sondes))
        lignes = ouvrir("registres", cl.REGISTRE_SONDES, racines, lecture="lignes_scellement")
        lues = {}
        for l in lignes:
            s = l.strip()
            if not s.endswith("|"):
                raise GardeArret("ligne de scellement mal formée (quatre colonnes attendues)")
            col = [c.strip() for c in s[1:-1].split("|")]
            if col[0] not in cl.SCELLEMENTS_SONDES:
                raise GardeArret(f"ligne de scellement d'une clé inconnue {col[0]!r}")
            if len(col) != 4:
                raise GardeArret(f"{col[0]} : quatre colonnes attendues (clé, heure, chemin, empreinte)")
            if col[0] in lues:
                raise GardeArret(f"{col[0]} : plus d'une ligne au registre propre")
            lues[col[0]] = col
        maintenant = datetime.now(timezone.utc) if maintenant is None else maintenant
        sortie, avant = [], None
        for cle_t0, attendue in cl.SCELLEMENTS_SONDES.items():
            if cle_t0 not in lues:
                raise GardeArret(f"{cle_t0} : ligne absente du registre propre")
            _, heure, chemin, sha = lues[cle_t0]
            if not _HEURE.match(heure):
                raise GardeArret(f"{cle_t0} : heure illisible (AAAA-MM-JJTHH:MM:SSZ)")
            try:
                h = datetime.strptime(heure, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            except ValueError:
                raise GardeArret(f"{cle_t0} : heure illisible (AAAA-MM-JJTHH:MM:SSZ)") from None
            if h > maintenant:
                raise GardeArret(f"{cle_t0} : heure future")
            if avant is not None and not h > avant:
                raise GardeArret(f"{cle_t0} : heures non croissantes dans l'ordre des trois scellements")
            avant = h
            if not _SHA.match(sha):
                raise GardeArret(f"{cle_t0} : empreinte illisible (64 caractères)")
            if not chemin or Path(chemin).is_absolute() or ".." in Path(chemin).parts:
                raise GardeArret(f"{cle_t0} : chemin cité non relatif ou portant « .. »")
            vue = ouvrir("registres", chemin, replace(racines, cites=frozenset({chemin})), lecture="scelle")
            if vue != sha:
                raise GardeArret(f"{cle_t0} : le texte cité n'a pas l'empreinte de sa ligne")
            if mode == "reel" and sha != attendue:
                raise GardeArret(f"{cle_t0} : empreinte ≠ celle de la spécification (section 5.1)")
            sortie.append({"cle": cle_t0, "heure": heure, "empreinte": sha})
        return sortie
    except GardeArret as e:
        raise GardeArret(f"{cl.MOTIF_T0} : {e}") from e


# ------------------------------------------------------------------------------------------------------------------------------
# Chargement : contrôles E0 à E10 (section 3)
# ------------------------------------------------------------------------------------------------------------------------------
def _entier(v) -> bool:
    return isinstance(v, int) and not isinstance(v, bool)


def exiger_entropie_et_prefixe(config_run: dict, manifeste_run: dict, manifeste_course: dict, mode: str) -> tuple[int, str]:
    """Contrôle E7 ; rend (entropie, préfixe)."""
    e = config_run.get("entropie")
    if not _entier(e) or e < 0:
        raise GardeArret("E7 : config.entropie du manifeste du run n'est pas un entier positif ou nul")
    g = manifeste_run.get("graines")
    if not isinstance(g, dict) or len(g) != 1:
        raise GardeArret("E7 : une seule graine attendue au manifeste du run")
    (cle_g, graine), = g.items()
    for quoi, s in (("manifeste de la course", manifeste_course.get("entropie")),
                    ("graine du manifeste du run", graine.get("entropie") if isinstance(graine, dict) else None)):
        if not isinstance(s, str):
            raise GardeArret(f"E7 : entropie du {quoi} : chaîne attendue")
        try:
            canon = str(int(s))
        except ValueError:
            raise GardeArret(f"E7 : entropie du {quoi} illisible") from None
        if canon != s or int(s) != e:
            raise GardeArret(f"E7 : entropie du {quoi} non canonique ou ≠ config.entropie du manifeste du run")
    prefixe = dg.prefixe_de_la_course(config_run)
    if manifeste_course.get("prefixe_graines") != prefixe or (manifeste_course.get("config") or {}).get("prefixe_graines") != prefixe:
        raise GardeArret("E7 : préfixe des graines de la course ≠ prefixe_de_la_course(configuration du run)")
    if cle_g != prefixe + "iib/v5/manifeste":
        raise GardeArret("E7 : clé de la graine du manifeste du run ≠ préfixe de la course suivi de iib/v5/manifeste")
    if mode == "reel" and prefixe != cl.PREFIXE_REEL:
        raise GardeArret(f"E7 : en mode réel, le préfixe de la course doit être exactement {cl.PREFIXE_REEL!r}")
    return e, prefixe


def _trier_episode(lignes: list, quoi: str, actions: int) -> list:
    for l in lignes:
        if not _entier(l.get("pas")):
            raise GardeArret(f"{quoi} : pas non entier")
    triees = sorted(lignes, key=lambda l: l["pas"])
    if [l["pas"] for l in triees] != list(range(actions)):
        raise GardeArret(f"{quoi} : {len(lignes)} lignes, pas 0 à {actions - 1} une fois chacun attendus")
    return triees


def _exiger_lignes_oracle(lignes, quoi: str) -> None:
    if not isinstance(lignes, list) or not lignes:
        raise GardeArret(f"{quoi} : liste de lignes non vide attendue")
    for l in lignes:
        if not isinstance(l, dict) or set(l) != rg.CLES_ORACLE:
            en_plus = sorted(set(l) - rg.CLES_ORACLE) if isinstance(l, dict) else "?"
            raise GardeArret(f"{quoi} : ligne hors des clés de l'oracle (en plus : {en_plus})")
        if l["schema"] != cf5.SCHEMA_ORACLE:
            raise GardeArret(f"{quoi} : schéma {l['schema']!r} ≠ {cf5.SCHEMA_ORACLE!r}")
        if l["oracle"] not in cf5.ORACLES:
            raise GardeArret(f"{quoi} : oracle ni N ni P")
        if not isinstance(l["episode"], str) or not l["episode"]:
            raise GardeArret(f"{quoi} : épisode illisible")


def exiger_chemin_de_la_designation(cite, rel_d: str) -> None:
    """E5 : le chemin de la désignation cité par la configuration est relatif, sans « .. », et vaut `diag/ETAL/designation-iib-v5.json`."""
    chemin = cite.get("chemin") if isinstance(cite, dict) else None
    if not isinstance(chemin, str) or Path(chemin).is_absolute() or ".." in Path(chemin).parts or chemin != rel_d:
        raise GardeArret("E5 : chemin de la désignation cité non relatif, portant « .. », ou autre que celui de l'étalonnage")


def exiger_oracle_concordant(oracle, cite: dict, res: dict, evaluation: dict, course: dict, fichiers_eval: dict) -> None:
    """E5 : l'oracle désigné (N ou P) est le même partout où la course l'écrit, et la course du maître cite la même désignation."""
    if oracle not in cf5.ORACLES:
        raise GardeArret("E5 : oracle désigné ni N ni P")
    conf = (course.get("configuration_de_course") or {}).get("oracle_de_la_regle") or {}
    valeurs = [res.get("oracle_de_la_regle"), evaluation.get("oracle_de_la_regle"), course.get("oracle_de_la_regle"), conf.get("valeur")]
    valeurs += [fichiers_eval[c].get("oracle_de_la_regle") for c in cl.CONDITIONS]
    if any(v != oracle for v in valeurs):
        raise GardeArret("E5 : oracle désigné discordant")
    if conf.get("designation") != cite:
        raise GardeArret("E5 : oracle désigné discordant (désignation citée par la course du maître)")


def exiger_branches(branches, sha_vu: str, cite: dict) -> None:
    """E6 : résultat des conditions de départ scellé à l'empreinte que cite la désignation, de schéma `branches-iib-v5`,
    `non_calculable` nul."""
    if sha_vu != cite.get("sha256"):
        raise GardeArret("E6 : résultat des conditions de départ d'une autre empreinte que celle de la désignation")
    if not isinstance(branches, dict) or branches.get("schema") != cf5.SCHEMA_BRANCHES or branches.get("non_calculable") is not None:
        raise GardeArret("E6 : résultat des conditions de départ : schéma faux ou non calculable")


def exiger_lignes_de_l_evaluation(fichiers_eval: dict, lignes_evaluation, config: dict) -> tuple[dict, list]:
    """E8 (section 3.1). Rend (oracle → condition → tâche → lignes triées par pas, tâches)."""
    ev_ = (config.get("distillation_evaluation") or {}).get("evaluation") or {}
    if list(ev_.get("conditions") or []) != list(cl.CONDITIONS):
        raise GardeArret(f"E8 : conditions de l'évaluation ≠ {cl.CONDITIONS}")
    n_taches, n_actions = ev_.get("taches"), (config.get("organisme") or {}).get("actions")
    if not _entier(n_taches) or not _entier(n_actions):
        raise GardeArret("E8 : nombre de tâches ou d'actions illisible")
    par = {o: {} for o in cf5.ORACLES}
    taches = None
    index_fichiers = {}
    for c in cl.CONDITIONS:
        f = fichiers_eval[c]
        if f.get("condition") != c:
            raise GardeArret(f"E8 : condition du fichier de {c} discordante")
        _exiger_lignes_oracle(f.get("lignes"), f"E8 ({c})")
        groupes = {o: {} for o in cf5.ORACLES}
        for l in f["lignes"]:
            if l["phase"] != f"evaluation-{c}":
                raise GardeArret(f"E8 ({c}) : ligne d'une autre phase")
            if not _entier(l["pas"]):
                raise GardeArret(f"E8 ({c}) : pas non entier")
            cle = (l["oracle"], l["phase"], l["episode"], l["pas"])
            if cle in index_fichiers:
                raise GardeArret(f"E8 ({c}) : ligne en double")
            index_fichiers[cle] = l
            groupes[l["oracle"]].setdefault(l["episode"], []).append(l)
        for o in cf5.ORACLES:
            if len(groupes[o]) != n_taches:
                raise GardeArret(f"E8 ({c}, {o}) : {len(groupes[o])} épisodes, {n_taches} attendus")
            for t, v in groupes[o].items():
                triees = _trier_episode(v, f"E8 ({c}, {o}, {t})", n_actions)
                rg.exiger_sorties_oracle(triees, o)
                groupes[o][t] = triees
            if taches is None:
                taches = set(groupes[o])
            elif set(groupes[o]) != taches:
                raise GardeArret(f"E8 ({c}, {o}) : ensemble des tâches différent")
            par[o][c] = groupes[o]
        for t in taches:
            for a, b in zip(groupes["N"][t], groupes["P"][t]):
                for k in CHAMPS_DE_L_ACTION:
                    if a[k] != b[k]:
                        raise GardeArret(f"E8 ({c}) : champ {k} différent entre les deux oracles")
    if len(taches) % 2:
        raise GardeArret("E8 : nombre impair de tâches")
    _exiger_lignes_oracle(lignes_evaluation, "E8 (évaluation)")
    index_ev = {}
    for l in lignes_evaluation:
        if not isinstance(l["phase"], str):
            raise GardeArret("E8 (évaluation) : phase non textuelle")
        if not _entier(l["pas"]):
            raise GardeArret("E8 (évaluation) : pas non entier")
        cle = (l["oracle"], l["phase"], l["episode"], l["pas"])
        if cle in index_ev:
            raise GardeArret("E8 : ligne en double dans le fichier de l'évaluation")
        index_ev[cle] = l
    if index_ev != index_fichiers:
        raise GardeArret("E8 : lignes des quatre fichiers par condition ≠ lignes du fichier de l'évaluation")
    return par, sorted(taches)


def exiger_episodes_du_maitre(lignes_m, course: dict, acceptes_du_resume, config: dict, oracle: str) -> dict:
    """E9 (section 3.2). Rend épisode → lignes triées par pas."""
    n_actions = (config.get("organisme") or {}).get("actions")
    _exiger_lignes_oracle(lignes_m, "E9")
    maitre = {}
    for l in lignes_m:
        if l["oracle"] != oracle or l["phase"] != "maitre":
            raise GardeArret("E9 : ligne du maître d'un autre oracle ou d'une autre phase")
        maitre.setdefault(l["episode"], []).append(l)
    for e in maitre:
        maitre[e] = _trier_episode(maitre[e], f"E9 ({e})", n_actions)
    decisions = course.get("decisions")
    if not isinstance(decisions, list) or any(not isinstance(d, dict) for d in decisions):
        raise GardeArret("E9 : décisions illisibles")
    noms = [d.get("episode") for d in decisions]
    if len(set(noms)) != len(noms) or set(noms) != set(maitre):
        raise GardeArret("E9 : épisodes des lignes ≠ épisodes des décisions")
    regle = cf5.regle_de(config, oracle)
    for d in decisions:
        r = rg.accepter(maitre[d["episode"]], regle, oracle)
        if not isinstance(d.get("accepte"), bool) or (r["accepte"], r["bornables"], r["total"]) != (d["accepte"], d.get("bornables"), d.get("total")):
            raise GardeArret("E9 : décision recalculée ≠ décision écrite")
    n_acc = sum(1 for d in decisions if d["accepte"])
    if n_acc != course.get("acceptes") or n_acc != acceptes_du_resume or course.get("arret") is not None:
        raise GardeArret("E9 : nombre d'acceptés discordant, ou arrêt de la course non nul")
    return maitre


def exiger_controle_premier_cout(cpc) -> dict:
    """Précontrôle de `controle_premier_cout` de `evaluation-iib-v5.json` avant création du manifeste."""
    if not isinstance(cpc, dict):
        raise GardeArret("E8 : controle_premier_cout absent ou illisible dans evaluation-iib-v5.json")
    for c in cl.CONDITIONS:
        bloc = cpc.get(c)
        if not isinstance(bloc, dict) or any(k not in bloc for k in ("phrase", "validite", "alerte")):
            raise GardeArret(f"E8 : controle_premier_cout incomplet pour la condition {c}")
    return cpc


def _egal_types_stricts(a, b) -> bool:
    """Égalité stricte valeur et type (refuse `1 == True == 1.0`)."""
    if type(a) is not type(b):
        return False
    if isinstance(a, list):
        return len(a) == len(b) and all(_egal_types_stricts(x, y) for x, y in zip(a, b))
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(_egal_types_stricts(a[k], b[k]) for k in a)
    return a == b


def charger(racine, run_id: str, etalonnage: str, avec_identifiants: bool = False, mode: str = "reel") -> dict:
    """Contrôles E0 à E9 (E10, forme des identifiants, si `avec_identifiants`) ; rend les entrées vérifiées. `mode` : celui que
    déclare l'appelant (réel par défaut ; jouet pour les essais seulement), exigé égal à celui de la configuration de la course."""
    if mode not in cl.MODES:
        raise GardeArret(f"mode {mode!r} : « reel » ou « jouet »")
    racine = Path(racine).resolve()
    if mode == "reel" and racine != cl.racine_du_code().resolve():
        raise GardeArret("mode réel : la racine de lecture doit être la racine du code qui tourne (section 2)")
    # E0
    if not isinstance(run_id, str) or not mf._RUN_ID.match(run_id):
        raise GardeArret("E0 : nom de la course hors de la forme d'un nom de lancement")
    if not isinstance(etalonnage, str) or not mf._RUN_ID.match(etalonnage):
        raise GardeArret("E2 : nom de l'étalonnage hors de la forme d'un nom de lancement")
    R = Racines(lecture=racine, run_id=run_id, etalonnage=etalonnage)
    D = f"diag/{etalonnage}/"
    empreintes: dict = {}

    def lire(rel):
        x = ouvrir("lecture", rel, R, lecture="json")
        empreintes[rel] = ouvrir("lecture", rel, R, lecture="empreinte")
        return x

    rel_m = f"runs/{run_id}/manifeste.json"
    lire(rel_m)
    manifeste_run, _ = mf.lire_manifeste(ouvrir("lecture", rel_m, R, lecture="chemin"))
    if manifeste_run.get("run_id") != run_id:
        raise GardeArret("E0 : run_id du manifeste ≠ nom de la course passé")
    config_run = manifeste_run["config"]
    if not isinstance(config_run, dict) or config_run.get("mode") != mode:
        raise GardeArret(f"mode de la course ≠ mode déclaré par l'appelant ({mode})")
    # E1
    rel_r = f"diag/{run_id}/resume.json"
    corps = lire(rel_r)
    if not isinstance(corps, dict) or corps.get("run_id") != run_id:
        raise GardeArret("E1 : le résumé ne nomme pas la course passée")
    corps = mf.verifier_resultat(racine, ouvrir("lecture", rel_r, R, lecture="chemin"))
    res = corps["resultat"]
    if res.get("phase") != "course" or res.get("arret") is not None or res.get("reste") is not None \
            or res.get("aucune_activation") is not True or res.get("avertissement") != cf5.AVERTISSEMENT:
        raise GardeArret("E1 : résumé de la course : phase, arrêt, reste, aucune_activation ou avertissement non conformes")
    # E2
    if res.get("etalonnage") != etalonnage:
        raise GardeArret("E2 : étalonnage du résumé ≠ argument --etalonnage")
    emp = res.get("empreintes")
    if not isinstance(emp, dict):
        raise GardeArret("E3 : empreintes du résumé illisibles")

    def sortie(nom, cle=None):                                       # E3
        cle = nom if cle is None else cle
        rel = D + nom
        if cle not in emp:
            raise GardeArret(f"E3 : {nom} absent du résumé scellé")
        x = lire(rel)
        if ouvrir("lecture", rel, R, lecture="scelle") != emp[cle]:
            raise GardeArret(f"E3 : {nom} : empreinte ≠ celle du résumé")
        return x

    manifeste_course = sortie("manifeste-course-iib-v5.json", "manifeste")
    config = manifeste_course.get("config") if isinstance(manifeste_course, dict) else None
    if not isinstance(config, dict):
        raise GardeArret("E4 : configuration du manifeste de la course illisible")
    # E4
    rel_d = D + "designation-iib-v5.json"
    designation = lire(rel_d)
    attendue = dg.configuration_de_course(config_run, racine, rel_d)
    if config != attendue:
        raise GardeArret("E4 : configuration de la course ≠ configuration_de_course(configuration du run)")
    if res.get("configuration_sha256") != manifeste_run.get("config_sha256"):
        raise GardeArret("E4 : configuration_sha256 du résumé ≠ config_sha256 du manifeste du run")
    if config.get("mode") != mode:
        raise GardeArret(f"mode de la configuration de la course ≠ mode déclaré ({mode})")
    # E5
    cite = (config.get("oracle_de_la_regle") or {}).get("designation") or {}
    exiger_chemin_de_la_designation(cite, rel_d)
    ouvrir("lecture", cite["chemin"], R, lecture="json")
    oracle = cf5.exiger_oracle_de_la_regle(config, racine)
    evaluation = sortie("evaluation-iib-v5.json")
    course = sortie("course-maitre-iib-v5.json")
    oracle_course = sortie("oracle-course-iib-v5.json")
    fichiers_eval = {c: sortie(f"evaluation/oracles-evaluation-{c}.json") for c in cl.CONDITIONS}
    exiger_oracle_concordant(oracle, cite, res, evaluation, course, fichiers_eval)
    # E6
    b = designation.get("branches") if isinstance(designation, dict) else None
    if not isinstance(b, dict) or not isinstance(b.get("nom"), str):
        raise GardeArret("E6 : résultat des conditions de départ non cité par la désignation")
    rel_b = D + b["nom"]
    branches = lire(rel_b)
    exiger_branches(branches, ouvrir("lecture", rel_b, R, lecture="scelle"), b)
    # E7
    entropie, prefixe = exiger_entropie_et_prefixe(config_run, manifeste_run, manifeste_course, mode)
    # E8
    par, taches = exiger_lignes_de_l_evaluation(fichiers_eval, evaluation.get("lignes"), config)
    controle_premier_cout = exiger_controle_premier_cout(evaluation.get("controle_premier_cout"))
    # E9
    maitre = exiger_episodes_du_maitre(oracle_course.get("lignes"), course, res.get("acceptes"), config, oracle)
    decisions = course["decisions"]
    n_actions = config["organisme"]["actions"]
    sortie_ = {"mode": mode, "racine": racine, "racines": R, "run_id": run_id, "etalonnage": etalonnage, "config": config,
               "config_run": config_run, "manifeste_run": manifeste_run, "manifeste_course": manifeste_course, "resume": res,
               "oracle": oracle, "autre": "P" if oracle == "N" else "N", "entropie": entropie, "prefixe": prefixe,
               "evaluation": par, "taches": sorted(taches), "maitre": maitre, "decisions": decisions,
               "designation": designation, "designation_citee": dict(cite), "branches": branches,
               "branches_citees": {"chemin": rel_b, "sha256": b.get("sha256")},
               "controle_premier_cout": controle_premier_cout, "rapportes": evaluation.get("rapportes"),
               "n_actions": n_actions, "empreintes": empreintes, "ids": None}
    if avec_identifiants:
        sortie_["ids"] = _charger_identifiants(lire, D, sortie_)
    return sortie_


def _charger_identifiants(lire, D: str, entrees: dict) -> dict:
    """E10, forme des fichiers d'identifiants (section 7.2) ; les contrôles qui demandent le vocabulaire et les fins
    (`exiger_identifiants`) jouent après le chargement du jetoniseur. Rend clé d'épisode → dix listes d'identifiants."""
    emp = entrees["resume"]["empreintes"]
    reunion = {}
    for c in cl.CONDITIONS:
        nom = f"evaluation/ids-evaluation-{c}.json"
        if nom not in emp:
            raise GardeArret(f"E3 : {nom} absent du résumé scellé")
        f = lire(D + nom)
        if ouvrir("lecture", D + nom, entrees["racines"], lecture="scelle") != emp[nom]:
            raise GardeArret(f"E3 : {nom} : empreinte ≠ celle du résumé")
        if not isinstance(f, dict) or set(f) != {"avertissement", "condition", "ids"}:
            raise GardeArret(f"E10 : {nom} : clés avertissement, condition, ids attendues, et elles seules")
        if f["avertissement"] != cf5.AVERTISSEMENT or f["condition"] != c:
            raise GardeArret(f"E10 : {nom} : avertissement ou condition non conformes")
        ids = f["ids"]
        if not isinstance(ids, dict) or list(ids) != sorted(ids):
            raise GardeArret(f"E10 : {nom} : clés des identifiants non rangées dans l'ordre du tri des chaînes")
        taches = set()
        for k in ids:
            phase, barre, ep = k.partition("/")
            if not barre or not ep or phase != f"evaluation-{c}":
                raise GardeArret(f"E10 : {nom} : clé d'épisode {k!r} hors forme")
            taches.add(ep)
        if taches != set(entrees["taches"]):
            raise GardeArret(f"E10 : {nom} : tâches ≠ tâches des lignes de l'évaluation")
        for k, v in ids.items():
            if k in reunion:
                raise GardeArret(f"E10 : clé {k!r} dans deux tranches")
            reunion[k] = v
    nom = "ids-actions-evaluation-iib-v5.json"
    if nom not in emp:
        raise GardeArret(f"E3 : {nom} absent du résumé scellé")
    f = lire(D + nom)
    if ouvrir("lecture", D + nom, entrees["racines"], lecture="scelle") != emp[nom]:
        raise GardeArret(f"E3 : {nom} : empreinte ≠ celle du résumé")
    if not isinstance(f, dict) or set(f) != {"avertissement", "ids"} or f["avertissement"] != cf5.AVERTISSEMENT:
        raise GardeArret(f"E10 : {nom} : clés avertissement et ids attendues, et elles seules ; avertissement exact")
    ens = f["ids"]
    if not isinstance(ens, dict) or list(ens) != sorted(ens):
        raise GardeArret(f"E10 : {nom} : clés non rangées dans l'ordre du tri des chaînes")
    if set(ens) != set(reunion):
        raise GardeArret("E10 : réunion des tranches ≠ clés du fichier d'ensemble")
    for k in ens:
        if not _egal_types_stricts(ens[k], reunion[k]):
            raise GardeArret(f"E10 : tranche différente du fichier d'ensemble à la clé {k}")
    for k, v in reunion.items():
        if not isinstance(v, list) or len(v) != entrees["n_actions"] or any(not isinstance(a, list) for a in v):
            raise GardeArret(f"identifiants hors forme à l'action {k}")
    return reunion


def exiger_identifiants(entrees: dict, V: int, fins, max_nouveaux: int) -> None:
    """Section 7.2, actions : entiers JSON de 0 à V − 1, action non vide, au plus `max_nouveaux` identifiants, une action plus
    courte finit par un jeton de fin, aucun jeton de fin ailleurs qu'en dernière position. Écart : la clé seule est dite."""
    fins = set(fins)
    for k, actions in entrees["ids"].items():
        for p, ids in enumerate(actions):
            cle = f"{k}#{p}"
            ok = bool(ids) and len(ids) <= max_nouveaux and all(_entier(i) and 0 <= i < V for i in ids)
            ok = ok and (len(ids) == max_nouveaux or ids[-1] in fins) and not any(i in fins for i in ids[:-1])
            if not ok:
                raise GardeArret(f"identifiants hors forme à l'action {cle}")


# ------------------------------------------------------------------------------------------------------------------------------
# Excès du maître, graines, ordre canonique, présentation
# ------------------------------------------------------------------------------------------------------------------------------
def exces_du_maitre(entrees: dict) -> dict:
    """Excès moyen par action comptée (bornable) des épisodes acceptés du maître, et de tous ses épisodes (section 4, point 5 ;
    nœud N-1), sous l'oracle désigné, après le contrôle E9."""
    acc = {d["episode"] for d in entrees["decisions"] if d["accepte"]}
    e_acc = [l["exces"] for e, v in entrees["maitre"].items() if e in acc for l in v if l["bornable"]]
    e_tous = [l["exces"] for v in entrees["maitre"].values() for l in v if l["bornable"]]
    gr = entrees["branches"]["oracles"][entrees["oracle"]]["grandeurs"]
    return {"episodes": len(entrees["maitre"]), "acceptes": len(acc), "actions_bornables_des_acceptes": len(e_acc),
            "exces_moyen_par_action_des_acceptes": float(np.mean(e_acc)) if e_acc else None,
            "actions_bornables_de_tous_les_episodes": len(e_tous),
            "exces_moyen_par_action_de_tous_les_episodes": float(np.mean(e_tous)) if e_tous else None,
            "exces_moyen_honnete_de_l_etalonnage": gr.get("exces_moyen_honnete")}


def graines_de_lecture(entropie: int, prefixe: str, cles) -> dict:
    """Clé (sans préfixe) → graine dérivée sous le nom préfixé, par `manifeste.graines` (dérivation de la course)."""
    g = mf.graines([prefixe + c for c in cles], entropie)
    return {c: g[prefixe + c] for c in cles}


def alias(graines: dict, table: dict) -> dict:
    """Nom lu par le module d'origine → graine de la clé de lecture que la table lui associe."""
    return {origine: graines[bloc] for origine, bloc in table.items()}


def exiger_aucune_collision(noms: list, entrees: dict) -> None:
    """Aucun nom de graine d'une lecture n'est une clé de `graines` du manifeste de la course ni de celui du run."""
    for quoi, m in (("manifeste de la course", entrees["manifeste_course"]), ("manifeste du run", entrees["manifeste_run"])):
        communs = set(noms) & set(m.get("graines") or {})
        if communs:
            raise GardeArret(f"graines : nom {sorted(communs)[0]!r} déjà présent parmi les graines du {quoi}")


def lignes_ordonnees(entrees: dict, oracle: str) -> list:
    """Lignes de l'évaluation de cet oracle dans l'ordre canonique : conditions (H, B50, B100, TJ100), tâches dans l'ordre du
    tri des chaînes, pas de 0 à 9."""
    return [l for c in cl.CONDITIONS for t in sorted(entrees["evaluation"][oracle][c]) for l in entrees["evaluation"][oracle][c][t]]


def presenter(lignes: list, variante: str | None = None) -> dict:
    """La correspondance entre une ligne v5 et une action du module d'origine (section 5.2), et elle seule."""
    if variante not in (None, "sans_ancre", "ancien_lecteur"):
        raise GardeArret(f"variante {variante!r} inconnue")
    sortie = []
    for l in lignes:
        if variante == "sans_ancre" and l["sans_ancre_commune"]:
            continue
        a = {"phase": l["phase"], "episode": l["episode"], "pas": l["pas"], "bornable": l["bornable"], "contexte": "reecrit",
             "e": l["exces"], "cout_declare": l["cout_declare"], "cout_lisible": l["cout_lisible"],
             "formes": dict(l["fenetre"]["formes"]) if l["fenetre"] is not None else {}}
        if variante == "ancien_lecteur":
            a["cout_declare"], a["cout_lisible"] = l["ancien_lecteur"], l["ancien_lecteur"] is not None
        sortie.append(a)
    return {"actions": sortie}


# ------------------------------------------------------------------------------------------------------------------------------
# Jetoniseur, décodage, fidélité (sections 7.1 à 7.3)
# ------------------------------------------------------------------------------------------------------------------------------
def charger_jetoniseur(dossier, entrees: dict, essais: dict | None = None) -> dict:
    """Mode réel : dossier à quatre fichiers aux empreintes de référence, versions égales à celles du manifeste du run,
    réglage de nettoyage lu, vocabulaire par `config.json`, fins attendues ; toute injection refusée. Mode jouet : jetoniseur,
    fins et réglage de nettoyage passés par l'essai (`essais = {"jetoniseur", "fins", "nettoyage"}`)."""
    mode, config = entrees["mode"], entrees["config"]
    if mode == "jouet":
        if not isinstance(essais, dict) or set(essais) != {"jetoniseur", "fins", "nettoyage"} or not isinstance(essais["nettoyage"], bool):
            raise GardeArret("mode jouet : jetoniseur d'essai attendu ({jetoniseur, fins, nettoyage booléen})")
        tok = essais["jetoniseur"]
        return {"tok": tok, "V": len(tok), "fins": frozenset(int(f) for f in essais["fins"]), "nettoyage": essais["nettoyage"],
                "rapport": {"modele": "jouet", "revision": None, "fichiers": None, "versions": None,
                            "controles": "sans objet en mode jouet (jetoniseur passé par l'essai)"}}
    if essais is not None:
        raise GardeArret("mode réel : injection d'un jetoniseur refusée")
    if config["agent"].get("modele") != cl.JETONISEUR["modele"] or config["agent"].get("revision") != cl.JETONISEUR["revision"]:
        raise GardeArret("jetoniseur : modèle ou révision de l'agent ≠ révision figée de la section 7.1")
    d = Path(dossier)
    if not d.is_dir():
        raise GardeArret("jetoniseur : dossier absent")
    entrees_dossier = sorted(p.name for p in d.iterdir())
    if entrees_dossier != sorted(cl.JETONISEUR["fichiers"]) or any(not (d / n).is_file() for n in entrees_dossier):
        raise GardeArret("jetoniseur : le dossier doit porter exactement les quatre fichiers de référence, et rien d'autre")
    R = Racines(jetoniseur=d)
    fichiers = {}
    for n, attendue in cl.JETONISEUR["fichiers"].items():
        sha = ouvrir("jetoniseur", n, R, lecture="empreinte")
        if sha != attendue:
            raise GardeArret(f"jetoniseur : {n} d'une autre empreinte que la référence")
        fichiers[n] = sha
    versions_run = entrees["manifeste_run"].get("versions") or {}
    import importlib
    from importlib import metadata

    versions = {}
    for b in cl.BIBLIOTHEQUES_DE_JETONISATION:
        if b not in versions_run:
            raise GardeArret(f"jetoniseur : version de {b} absente du manifeste du run (défaut de réglage, non un résultat)")
        try:
            module = importlib.import_module(b)
            chargee, installee = str(module.__version__), metadata.version(b)
        except (ImportError, metadata.PackageNotFoundError):
            raise GardeArret(f"jetoniseur : {b} non chargeable (défaut de réglage, non un résultat)") from None
        if chargee != versions_run[b] or installee != versions_run[b]:
            raise GardeArret(f"jetoniseur : version de {b} ≠ celle du manifeste du run (défaut de réglage, non un résultat)")
        versions[b] = chargee
    reglage = ouvrir("jetoniseur", "tokenizer_config.json", R, lecture="json").get("clean_up_tokenization_spaces")
    if not isinstance(reglage, bool):
        raise GardeArret("jetoniseur : clean_up_tokenization_spaces absent ou non booléen")
    V = ouvrir("jetoniseur", "config.json", R, lecture="json").get("vocab_size")
    if not _entier(V) or V <= 0:
        raise GardeArret("jetoniseur : vocab_size de config.json illisible")
    eos = ouvrir("jetoniseur", "generation_config.json", R, lecture="json").get("eos_token_id")
    eos = [eos] if _entier(eos) else eos
    if not isinstance(eos, list) or not eos or not all(_entier(x) for x in eos):
        raise GardeArret("jetoniseur : eos_token_id de generation_config.json illisible")
    from transformers import AutoTokenizer

    from ..harnais.formats import FormatChat

    tok = AutoTokenizer.from_pretrained(str(d), local_files_only=True)
    if len(tok) != V:
        raise GardeArret("jetoniseur : len(tok) ≠ vocab_size de config.json")
    cloture = FormatChat(tok, variables=config["modele"]["variables_gabarit"])._pieces(("x", "y"))["cloture"][0]
    fins = frozenset(int(x) for x in eos) | {int(tok.eos_token_id), int(cloture)}
    if fins != frozenset(cl.JETONISEUR["fins"]):
        raise GardeArret("jetoniseur : fins d'action ≠ {128001, 128008, 128009}")
    return {"tok": tok, "V": V, "fins": fins, "nettoyage": reglage,
            "rapport": {"modele": cl.JETONISEUR["modele"], "revision": cl.JETONISEUR["revision"], "fichiers": fichiers,
                        "versions": versions, "source": cl.JETONISEUR["source"], "controles": "empreintes, versions, vocabulaire, fins"}}


def decoder(jet: dict, ids: list, cle: str) -> str:
    """Les deux décodages de la section 7.3, point 1 ; s'ils diffèrent : arrêt (clé seule)."""
    tok = jet["tok"]
    texte = tok.decode(ids, skip_special_tokens=True, clean_up_tokenization_spaces=jet["nettoyage"])
    par_defaut = tok.decode(ids, skip_special_tokens=True)
    if texte != par_defaut:
        raise GardeArret(f"décodage : les deux décodages diffèrent à l'action {cle}")
    return texte


def exiger_fidelite_du_decodage(jet: dict, entrees: dict) -> dict:
    """Pour chaque action, dans l'ordre canonique : décodage, nombre de jetons, garde de fidélité (section 7.3). Rend
    (condition, tâche, pas) → {texte, jetons, ids}. Écart : la clé de l'action et le nom du champ seuls sont dits."""
    from ..t06.cout import cout_action, cout_lisible
    from .lecture_cout_v5 import lire_action_v5

    fenetre = int(entrees["config"]["oracle"]["fenetre"])
    sortie = {}
    for l in lignes_ordonnees(entrees, entrees["oracle"]):
        c, t, p = l["phase"][len("evaluation-"):], l["episode"], l["pas"]
        cle = f"{l['phase']}/{t}#{p}"
        ids = entrees["ids"][f"{l['phase']}/{t}"][p]
        texte = decoder(jet, ids, cle)
        lu = lire_action_v5(jet["tok"], ids, jet["fins"], fenetre)
        egaux = (("champ_cout", lu["coupe"]["champ_cout"]), ("coupe_conforme", lu["coupe"]["conforme"]), ("rang_coupe", lu["coupe"]["rang"]),
                 ("motif_coupe", lu["coupe"]["motif"]), ("cout_declare", lu["cout_declare"]), ("cout_lisible", lu["cout_lisible"]),
                 ("fenetre", lu["fenetre"]), ("ancien_lecteur", lu["ancien_lecteur"]),
                 ("ecart_des_deux_lecteurs", lu["ecart_des_deux_lecteurs"]))
        for nom, v in egaux:
            if v != l[nom] or isinstance(v, bool) != isinstance(l[nom], bool) or (v is None) != (l[nom] is None):
                raise GardeArret(f"fidélité du décodage : action {cle}, champ {nom}")
        piece = cout_action(texte)["cout"]
        if (cout_lisible(piece) and piece != l["ancien_lecteur"]) or (not cout_lisible(piece) and l["ancien_lecteur"] is not None):
            raise GardeArret(f"fidélité du décodage : action {cle}, champ cout_action")
        sortie[(c, t, p)] = {"texte": texte, "jetons": len(ids), "ids": ids}
    return sortie


def fiches_et_textes(decodes: dict, entrees: dict) -> tuple[list, dict]:
    """`textes` (phase, épisode, pas, texte) et fiches d'épisodes `{"fiches": […]}` que lit le module d'origine."""
    textes, fiches = [], []
    for c in cl.CONDITIONS:
        for t in entrees["taches"]:
            phase = f"evaluation-{c}"
            jetons = []
            for p in range(entrees["n_actions"]):
                d = decodes[(c, t, p)]
                textes.append({"phase": phase, "episode": t, "pas": p, "texte": d["texte"]})
                jetons.append(d["jetons"])
            fiches.append({"uid": f"{phase}/{t}", "phase": phase, "actions": entrees["n_actions"], "jetons": jetons})
    return textes, {"fiches": fiches}
