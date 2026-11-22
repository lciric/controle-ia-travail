"""Programme d'enchaînement de la lecture de la discrétion, bras A des organismes discrets — version 2.

Texte qui fait foi : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md` — 13.2, ligne « programme d'enchaînement
de la lecture de la discrétion (8.7 ; brouillon 38 ; vérification du brouillon 37) » ; 8.7, garde de procédure
« versement avant lecture » ; 6.3, étapes (m) et (n) ; 6.9 ; 6.10 ; 3.5 (b) (ligne 562 : le programme de l'aire
conditionnelle « ne rend que les aires (valeur, intervalle, comptes), jamais une ligne du fichier ») ; 6.9 (ligne
873, même règle) ; conventions (constat de lancement, contrôle avant un rejeu) ; 8.4.

`enchainement_discretion_bras_a_v1.py` n'est pas modifié (R12). **Ce qui change à la version 2** (décision de la
session mère, nœud N1, option (a)) : l'étape (n) ne s'arrête plus sur la règle non écrite n° 1 de la version 1 (code
6). **Le programme de l'aire conditionnelle est reçu par la configuration scellée de l'enchaînement** (son entrée
scellée : chemin du programme et son empreinte sha256, chemin du fichier des scores par unité) ; l'enchaînement
**vérifie l'empreinte** (au départ, avant tout constat, puis de nouveau juste avant de le lancer), puis **le lance
comme une commande à part** (un processus séparé), joué depuis une copie des octets vérifiés. **Il ne nomme ni
n'ouvre le fichier des scores par unité** : le chemin vient de la configuration et est passé tel quel au programme
lancé ; l'enchaînement ne garde que ce que le programme rend — les vingt aires conditionnelles (valeur, intervalle,
comptes), repassées une à une par la garde de sortie de l'analyse, et les vingt clés tirées — et les confronte au
fichier scellé des grandeurs de l'étape (n), que le programme lancé a écrit. Programme absent, empreinte différente,
code de sortie inconnu, sortie mal formée ou portant autre chose que les aires, aires qui ne sont pas celles du
fichier des grandeurs : **arrêt explicite, versé** (garde ordinaire).

**Ce que le programme lancé doit faire** (contrat de la commande, forme de ce programme, non du texte) : arguments
`--configuration`, `--sortie`, `--fichier-des-unites` et, pour une reprise de l'étape (n), `--sortie-d-origine` ; sur
l'entrée standard, un objet JSON à quatre clés (`actions_desappariees`, `taches_de_verification`,
`entropie_de_la_configuration_du_bras`, `autres_grandeurs`) ; il lit le fichier, calcule les vingt aires, écrit et
scelle le fichier des grandeurs de l'étape (n) ; codes de sortie : 0 et une seule ligne JSON `{"aires": {dose:
{moniteur: sortie de l'aire}}, "cles": [...]}` ; 3, arrêt de la lecture consigné par l'analyse dans le dossier des
arrêts, sortie standard vide ; 4, garde ordinaire, sortie standard vide et une seule ligne sur la sortie d'erreur.
Tout autre code : rien de ses sorties n'est rendu.

Le reste est celui de la version 1 : **dans cet ordre** (une seule exécution) — configuration scellée de la
livraison, dossier de course, refus de ce que le texte n'écrit pas, entrée scellée de l'enchaînement, table A et base,
garde statique de la version 13 sur `src` et `scripts` ; versement d'ouverture ; constat de lancement (ou contrôle)
par la commande du programme du constat ; étape (m) et **versement avant tout rendu** (`EchecDuVersement`) ; étape
(n), versée ; compte rendu, qui ne porte ni le contenu du fichier de l'étape (m) ni celui des grandeurs, ni les
aires. Tout arrêt est versé avant d'être rendu ; d'une exception d'arrêt il ne tire que son constat ; une erreur
inattendue n'est rendue que par son type.

Sans réseau propre : seul le poussage git sort, vers le dépôt distant nommé par l'appelant. Aucun appel de modèle.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable, Mapping

from ..gardes import GardeArret
from ..scellement import verifier
from . import analyse_bras_a_v13 as analyse
from . import arrets_bras_a_v12 as arrets
from . import cloisonnement_bras_a_v13 as cloisonnement
from . import configuration_bras_a_v12 as conf_mod
from . import graines_bras_a_v12 as graines
from . import verdicts_bras_a_v13 as verdicts

VERSION = 2
RACINE_DU_CODE = Path(__file__).resolve().parents[3]
PAQUET = Path("src") / "controle_ia" / "organismes_discrets"
# Les modules que 13.2 nomme : analyse, verdicts et garde statique de la version 13 ; six modules de la version 12.
MODULES_JOUES = ("analyse_bras_a_v13", "verdicts_bras_a_v13", "cloisonnement_bras_a_v13", "configuration_bras_a_v12",
                 "arrets_bras_a_v12", "depots_bras_a_v12", "graines_bras_a_v12", "mesures_bras_a_v12",
                 "permutation_etiquettes_bras_a_v12")
DOSSIERS_DE_LA_GARDE_STATIQUE = ("src", "scripts")
RACINE_DE_LA_GARDE_STATIQUE = RACINE_DU_CODE          # le dépôt dont la commande fait lire `src` et `scripts`

ETAPE_M, ETAPE_N = arrets.ETAPE_M, arrets.ETAPE_N
A_JOUER_M_PUIS_N = "étape (m), puis étape (n)"
A_JOUER_N = "étape (n) seule (le fichier de l'étape (m) de cette livraison est scellé)"
A_JOUER_REPRISE_N = "reprise de l'étape (n) (le fichier de l'étape (m) est celui d'un autre rang)"

ISSUE_ABOUTIE = "étapes jouées, versées"
ISSUE_ARRET = "arrêt de la lecture de la discrétion"
ISSUE_GARDE = "garde ordinaire"
ISSUE_CONSTAT_MALSAIN = "constat de lancement malsain"
ISSUE_REGLE_NON_ECRITE = "règle que le texte n'écrit pas"
ISSUE_ERREUR = "erreur inattendue du programme"

MODE_CONSTAT, MODE_CONTROLE = "constat", "contrôle"

# Entrée de l'enchaînement (sa configuration scellée) : forme de ce programme (le texte ne la fixe pas), un objet JSON
# scellé, ces clés et elles seules. Version 2 : deux clés de plus, le programme de l'aire conditionnelle et le fichier.
CLE_DU_PROGRAMME_DE_L_AIRE = "programme_de_l_aire_conditionnelle"
CLE_DU_FICHIER = "fichier_des_unites"
CLES_DE_L_ENTREE = ("journal_de_la_table_a", "revision_refusee", "taches_gardees_lues", "renvoi_de_la_base",
                    "effectifs_de_la_base_conformes", "lignes_de_la_table_b", "etats_de_la_base", "cout_apparie",
                    "actions_desappariees", "taches_de_verification", "entropie_de_la_configuration_du_bras",
                    CLE_DU_PROGRAMME_DE_L_AIRE, CLE_DU_FICHIER)
CLES_DU_PROGRAMME_DE_L_AIRE = ("chemin", "sha256")
FORMES_DES_DOSES = tuple(analyse._forme_dose(p) for p in analyse.QUATRE_DOSES)
FORMES_DU_VERDICT = tuple(analyse._forme_dose(p) for p in analyse.DOSES_VERDICT)

# Contrat de la commande de l'aire conditionnelle.
CODE_DES_AIRES, CODE_DE_L_ARRET, CODE_DE_LA_GARDE = 0, 3, 4
CLES_DE_LA_SORTIE_DU_PROGRAMME = ("aires", "cles")
PAIRES_DE_LA_SORTIE_DE_L_AIRE = ("aires_des_plis", "intervalle")      # deux bornes : listes en JSON, couples en Python
DELAI_DU_PROGRAMME_DE_L_AIRE = 3600


class RegleNonEcrite(Exception):
    """Un cas que le texte n'écrit pas : le programme ne le tranche pas, il s'arrête et le nomme."""


class EchecDuVersement(Exception):
    """Le commit ou le poussage du dossier de course a échoué : **rien n'est rendu** (8.7). Le message ne dit que
    l'étape du versement et la commande git en défaut ; le versement est à refaire avant toute lecture."""


class ArretDeLEnchainement(Exception):
    """L'enchaînement s'est arrêté, **après le versement** de ce qu'il avait scellé. Porte `issue` et `compte_rendu`
    (ce qui se rend : aucune variable d'une lecture fautive)."""

    def __init__(self, issue: str, compte_rendu: dict):
        super().__init__(f"{issue} : {compte_rendu.get('motif_de_l_arret')}")
        self.issue, self.compte_rendu = issue, compte_rendu


# --- empreintes --------------------------------------------------------------------------------------------------------

def _sha256(chemin) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def _sous(chemin, dossier: Path) -> bool:
    p = Path(chemin).resolve()
    return p == dossier or dossier in p.parents


def _est_une_empreinte(x) -> bool:
    return isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def programmes_joues(programme_du_constat) -> dict:
    """Chemin et empreinte de chaque programme joué (manifeste de course, 8.7 : « la commande et l'empreinte de chaque
    programme joué, dont celle du module d'analyse employé, du module des verdicts et de la garde statique »). Le
    programme de l'aire conditionnelle s'y ajoute quand son empreinte a été vérifiée."""
    sortie = {nom: [str(PAQUET / f"{nom}.py"), _sha256(RACINE_DU_CODE / PAQUET / f"{nom}.py")] for nom in MODULES_JOUES}
    sortie["programme_du_constat"] = [str(programme_du_constat), _sha256(programme_du_constat)]
    sortie["enchainement"] = [str(PAQUET / Path(__file__).name), _sha256(__file__)]
    return sortie


def octets_du_programme_de_l_aire(chemin: Path, sha256_inscrit: str) -> bytes:
    """Les octets du programme de l'aire conditionnelle, **s'ils répondent à l'empreinte que la configuration scellée
    inscrit**. Programme absent, illisible, ou d'une autre empreinte : garde ordinaire (il n'est pas lancé)."""
    try:
        octets = Path(chemin).read_bytes()
    except OSError:
        raise GardeArret(f"programme de l'aire conditionnelle absent ou illisible ({chemin}) : il n'est pas lancé") from None
    if hashlib.sha256(octets).hexdigest() != sha256_inscrit:
        raise GardeArret(f"programme de l'aire conditionnelle ({chemin}) : son empreinte n'est pas celle que la "
                         f"configuration scellée inscrit ({sha256_inscrit[:16]}…) — il n'est pas lancé")
    return octets


# --- git : versement -----------------------------------------------------------------------------------------------------

def _git(racine: Path, *args: str, timeout: int = 300) -> str:
    try:
        fait = subprocess.run(["git", "-C", str(racine), *args], capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as e:
        raise EchecDuVersement(f"git {args[0]} : {type(e).__name__}") from None
    if fait.returncode != 0:
        raise EchecDuVersement(f"git {args[0]} en échec (code {fait.returncode}) : {fait.stderr.strip()[-300:]}")
    return fait.stdout


def depot_du_dossier_de_course(course: Path) -> tuple[Path, str]:
    """La racine du dépôt git qui porte le dossier de course, et le chemin du dossier relatif à elle."""
    try:
        fait = subprocess.run(["git", "-C", str(course), "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                              timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        fait = None
    if fait is None or fait.returncode != 0:
        raise GardeArret(f"dossier de course {course} : il n'est dans aucun dépôt git — il ne peut pas être versé (8.7)")
    racine = Path(fait.stdout.strip()).resolve()
    return racine, course.resolve().relative_to(racine).as_posix()


def verser(course: Path, distant: str, branche: str, etiquette: str) -> dict:
    """**Versement** (8.7) : commit du dossier de course entier — et de lui seul — puis poussage vers `distant`, sur la
    branche `branche` ; le poussage est vérifié sur le distant. Un fichier du dossier que git ignore, un reste non
    versé après le commit, un commit ou un poussage en échec : `EchecDuVersement`, sans rien rendre. Rend le commit,
    son heure, et s'il est neuf."""
    racine, rel = depot_du_dossier_de_course(course)
    etat = _git(racine, "status", "--porcelain", "--ignored", "--untracked-files=all", "--", rel)
    if any(l.startswith("!!") for l in etat.splitlines()):
        raise EchecDuVersement(f"versement « {etiquette} » : un fichier du dossier de course est ignoré par git — le "
                               "versement ne prendrait pas le dossier entier (8.7)")
    neuf = bool(etat.strip())
    if neuf:
        _git(racine, "add", "-A", "--", rel)
        _git(racine, "commit", "-q", "-m", f"Bras A, lecture de la discrétion : versement du dossier de course ({etiquette})",
             "--", rel)
    if _git(racine, "status", "--porcelain", "--ignored", "--untracked-files=all", "--", rel).strip():
        raise EchecDuVersement(f"versement « {etiquette} » : le dossier de course n'est pas entièrement versé après le commit")
    commit = _git(racine, "rev-parse", "HEAD").strip()
    heure = _git(racine, "show", "-s", "--format=%cI", "HEAD").strip()
    _git(racine, "push", "-q", distant, f"HEAD:refs/heads/{branche}")
    lu = _git(racine, "ls-remote", distant, f"refs/heads/{branche}").split()
    if not lu or lu[0] != commit:
        raise EchecDuVersement(f"versement « {etiquette} » : le distant ne porte pas le commit poussé")
    return {"etape": etiquette, "commit": commit, "heure": heure, "commit_neuf": neuf, "distant": distant, "branche": branche}


# --- entrée de l'enchaînement ------------------------------------------------------------------------------------------

def _booleen(x, nom: str) -> bool:
    if not isinstance(x, bool):
        raise GardeArret(f"entrée de l'enchaînement : `{nom}` — un booléen exigé")
    return x


def _chemin_de_l_entree(x, nom: str, dossier: Path) -> Path:
    """Un chemin écrit dans l'entrée : un texte non vide ; relatif, il se lit depuis le dossier de l'entrée."""
    if not isinstance(x, str) or not x.strip():
        raise GardeArret(f"entrée de l'enchaînement : `{nom}` — un chemin (texte non vide) exigé")
    p = Path(x)
    return (p if p.is_absolute() else dossier / p).resolve()


def lire_l_entree(chemin) -> dict:
    """L'entrée de l'enchaînement, **scellée** (compagnon vérifié), un objet JSON aux clés `CLES_DE_L_ENTREE` et à
    elles seules. Rend une table prête : doses en nombres, comptes des actions désappariées par (tâche, épisode),
    programme de l'aire conditionnelle (chemin et empreinte inscrite) et chemin du fichier, **qui n'est pas ouvert**."""
    verifier(chemin)
    try:
        o = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise GardeArret("entrée de l'enchaînement : pièce illisible") from None
    if not isinstance(o, dict) or sorted(o) != sorted(CLES_DE_L_ENTREE):
        raise GardeArret(f"entrée de l'enchaînement : exactement les clés {CLES_DE_L_ENTREE}")
    journal = o["journal_de_la_table_a"]
    if not isinstance(journal, list) or any(not isinstance(e, str) for e in journal):
        raise GardeArret("entrée de l'enchaînement : `journal_de_la_table_a` — une liste de textes")
    for nom in ("revision_refusee", "taches_gardees_lues", "effectifs_de_la_base_conformes"):
        _booleen(o[nom], nom)
    if not isinstance(o["renvoi_de_la_base"], str):
        raise GardeArret("entrée de l'enchaînement : `renvoi_de_la_base` — un texte")
    b, base, cout = o["lignes_de_la_table_b"], o["etats_de_la_base"], o["cout_apparie"]
    if not isinstance(b, dict) or sorted(b) != sorted(FORMES_DU_VERDICT) or any(x not in verdicts.ORDRE_B for x in b.values()):
        raise GardeArret(f"entrée de l'enchaînement : `lignes_de_la_table_b` — une ligne de {verdicts.ORDRE_B} à chacune des "
                         f"doses {FORMES_DU_VERDICT}")
    if not isinstance(base, dict) or sorted(base) != sorted(FORMES_DES_DOSES) or any(x not in verdicts.ETATS_BASE for x in base.values()):
        raise GardeArret(f"entrée de l'enchaînement : `etats_de_la_base` — un état de {verdicts.ETATS_BASE} à chacune des "
                         f"doses {FORMES_DES_DOSES}")
    if not isinstance(cout, dict) or sorted(cout) != sorted(FORMES_DU_VERDICT):
        raise GardeArret(f"entrée de l'enchaînement : `cout_apparie` — un booléen à chacune des doses {FORMES_DU_VERDICT}")
    for d, x in cout.items():
        _booleen(x, f"cout_apparie.{d}")
    taches = o["taches_de_verification"]
    if not isinstance(taches, list) or any(not isinstance(t, str) for t in taches):
        raise GardeArret("entrée de l'enchaînement : `taches_de_verification` — une liste de textes")
    entropie = o["entropie_de_la_configuration_du_bras"]
    if isinstance(entropie, bool) or not isinstance(entropie, int) or entropie < 0:
        raise GardeArret("entrée de l'enchaînement : `entropie_de_la_configuration_du_bras` — un entier positif ou nul")
    des = o["actions_desappariees"]
    if not isinstance(des, dict) or sorted(des) != sorted(FORMES_DES_DOSES):
        raise GardeArret(f"entrée de l'enchaînement : `actions_desappariees` — une liste à chacune des doses {FORMES_DES_DOSES}")
    par_dose = {}
    for d, triplets in des.items():
        if not isinstance(triplets, list):
            raise GardeArret(f"entrée de l'enchaînement : `actions_desappariees.{d}` — une liste de [tâche, épisode, compte]")
        comptes = {}
        for t in triplets:
            if not (isinstance(t, list) and len(t) == 3 and isinstance(t[0], str) and isinstance(t[1], int)
                    and not isinstance(t[1], bool) and isinstance(t[2], int) and not isinstance(t[2], bool)) \
                    or (t[0], t[1]) in comptes:
                raise GardeArret(f"entrée de l'enchaînement : `actions_desappariees.{d}` — [tâche, épisode, compte], un "
                                 "seul par épisode")
            comptes[(t[0], t[1])] = t[2]
        par_dose[analyse._dose_de(d)] = comptes
    dossier = Path(chemin).resolve().parent
    programme = o[CLE_DU_PROGRAMME_DE_L_AIRE]
    if not isinstance(programme, dict) or sorted(programme) != sorted(CLES_DU_PROGRAMME_DE_L_AIRE) \
            or not _est_une_empreinte(programme["sha256"]):
        raise GardeArret(f"entrée de l'enchaînement : `{CLE_DU_PROGRAMME_DE_L_AIRE}` — exactement `chemin` (un chemin) et "
                         "`sha256` (une empreinte entière, en minuscules)")
    return {"journal": journal, "revision_refusee": o["revision_refusee"], "gardees_lues": o["taches_gardees_lues"],
            "renvoi_de_la_base": o["renvoi_de_la_base"],
            "effectifs_de_la_base_conformes": o["effectifs_de_la_base_conformes"],
            "lignes_b": {analyse._dose_de(d): x for d, x in b.items()},
            "base": {analyse._dose_de(d): x for d, x in base.items()},
            "cout": {analyse._dose_de(d): x for d, x in cout.items()},
            "desappariees": par_dose, "desappariees_ecrites": des, "taches": taches, "entropie": entropie,
            "programme_de_l_aire": (_chemin_de_l_entree(programme["chemin"], f"{CLE_DU_PROGRAMME_DE_L_AIRE}.chemin", dossier),
                                    programme["sha256"]),
            "fichier": _chemin_de_l_entree(o[CLE_DU_FICHIER], CLE_DU_FICHIER, dossier),
            "sha256": _sha256(chemin)}


def exiger_etape_m_jouee(entree: Mapping) -> verdicts.ResultatA:
    """6.3 (m) et conventions : l'étape (m) n'est jouée que si aucune ligne de la table A ne s'applique, que la case
    « renvoi de la base » est vérifiée et que les effectifs de la base sont conformes ; sinon « rien ne vient après
    elle ». Garde ordinaire, avant tout constat et toute lecture."""
    resultat_a = verdicts.lire_table_a(entree["journal"], entree["revision_refusee"], entree["gardees_lues"])
    if not resultat_a.etapes_m_et_n_jouees:
        raise GardeArret(f"table A : ligne {' et '.join(resultat_a.lignes)} — les étapes (m) et (n) ne sont pas jouées, rien "
                         "ne part (7.2, règle (iii))")
    if entree["renvoi_de_la_base"] != verdicts.RENVOI_DE_LA_BASE_VERIFIE or entree["effectifs_de_la_base_conformes"] is not True:
        raise GardeArret("case « renvoi de la base » non vérifiée, ou effectifs de la base non conformes : la discrétion est "
                         "« non lue », l'étape (m) n'est pas jouée — rien ne part (6.3 (m) ; 7.4)")
    return resultat_a


# --- constat de lancement : par le programme, par sa commande ---------------------------------------------------------

def _environnement() -> dict:
    return {"PYTHONPATH": str(RACINE_DU_CODE / "src"), "PATH": "/usr/bin:/bin", "LC_ALL": "C.UTF-8"}


def jouer_le_constat(programme_du_constat: Path, configuration_scellee: Path, registre_courant, *, commit: str, date_utc: str,
                     registre_fige, ligne_de_go, mode: str) -> dict:
    """Joue le programme du constat **par sa commande** (conventions : « le constat de lancement et le contrôle d'avant un
    rejeu sont faits par le programme, jamais à la main, et cités au manifeste avec la commande et l'empreinte du
    programme »). Rend la commande, le code de sortie, la ligne à huit champs de sa sortie (sain ou malsain : c'est la
    trace d'un constat malsain) et la sortie d'erreur. Code 2 (pièces fautives) : garde ordinaire."""
    commande = [sys.executable, str(programme_du_constat), str(configuration_scellee), str(registre_courant),
                "--commit", commit, "--date-utc", date_utc]
    if registre_fige is not None:
        commande += ["--registre-fige", str(registre_fige)]
    if ligne_de_go is not None:
        commande += ["--ligne-de-go", ligne_de_go]
    if mode == MODE_CONTROLE:
        commande.append("--controle")
    fait = subprocess.run(commande, capture_output=True, text=True, timeout=600, env=_environnement(), cwd=str(RACINE_DU_CODE))
    if fait.returncode not in (0, 1):
        raise GardeArret(f"programme du constat, mode {mode} : arrêt sans constat (code {fait.returncode}) — "
                         f"{fait.stderr.strip()[-600:]}")
    lignes = fait.stdout.strip().splitlines()
    try:
        constat = json.loads(lignes[0]) if len(lignes) == 1 else None
    except json.JSONDecodeError:
        constat = None
    if not isinstance(constat, dict) or tuple(constat) != tuple(conf_mod.CHAMPS_DU_CONSTAT_DE_LANCEMENT):
        raise GardeArret(f"programme du constat, mode {mode} : sa sortie n'est pas une ligne à huit champs — refusé")
    return {"mode": mode, "commande": commande, "code": fait.returncode, "sain": fait.returncode == 0,
            "constat": constat, "sortie_d_erreur": fait.stderr.strip()}


# --- l'aire conditionnelle : par le programme que la configuration inscrit, par sa commande ----------------------------

def _sans_doublon(paires):
    cles = [k for k, _ in paires]
    if len(cles) != len(set(cles)):
        raise GardeArret("programme de l'aire conditionnelle : une clé en double dans sa sortie — refusée")
    return dict(paires)


def _constante_refusee(nom):
    raise GardeArret(f"programme de l'aire conditionnelle : `{nom}` dans sa sortie — refusé")


def aires_rendues(texte: str) -> dict:
    """La sortie standard du programme de l'aire conditionnelle, **telle qu'elle doit être et rien d'autre** : une
    seule ligne, un objet JSON à deux clés — `aires` (aux quatre doses, pour les cinq moniteurs, chaque sortie repassée
    par `exiger_sortie_de_l_aire_conditionnelle` : état, aire, aires des deux plis, intervalle, comptes, motif) et
    `cles` (les vingt clés de l'aire conditionnelle, chacune une fois). Une ligne de plus, une clé de plus ou en
    double, un champ d'un autre nom ou d'une autre forme : garde ordinaire. Rend `aires[(moniteur, dose)]`, `cles`."""
    if not isinstance(texte, str) or texte.count("\n") != 1 or not texte.endswith("\n"):
        raise GardeArret("programme de l'aire conditionnelle : sa sortie n'est pas une seule ligne — refusée")
    try:
        o = json.loads(texte, object_pairs_hook=_sans_doublon, parse_constant=_constante_refusee)
    except json.JSONDecodeError:
        raise GardeArret("programme de l'aire conditionnelle : sa sortie n'est pas du JSON — refusée") from None
    if not isinstance(o, dict) or sorted(o) != sorted(CLES_DE_LA_SORTIE_DU_PROGRAMME):
        raise GardeArret(f"programme de l'aire conditionnelle : sa sortie porte exactement {CLES_DE_LA_SORTIE_DU_PROGRAMME} "
                         "— rien d'autre que les aires (3.5 (b) ; 8.4)")
    par_dose = o["aires"]
    if not isinstance(par_dose, dict) or sorted(par_dose) != sorted(FORMES_DES_DOSES) \
            or any(not isinstance(x, dict) or sorted(x) != sorted(analyse.MONITEURS) for x in par_dose.values()):
        raise GardeArret("programme de l'aire conditionnelle : `aires` — les cinq moniteurs à chacune des quatre doses, "
                         "ni plus ni moins")
    aires = {}
    for d, par_moniteur in par_dose.items():
        for m, sortie in par_moniteur.items():
            if not isinstance(sortie, dict):
                raise GardeArret("programme de l'aire conditionnelle : une aire qui n'est pas une table — refusée")
            lue = dict(sortie)
            for champ in PAIRES_DE_LA_SORTIE_DE_L_AIRE:
                if isinstance(lue.get(champ), list):
                    lue[champ] = tuple(lue[champ])
            aires[(m, analyse._dose_de(d))] = analyse.exiger_sortie_de_l_aire_conditionnelle(lue)
    cles = o["cles"]
    if not isinstance(cles, list) or any(not isinstance(c, str) for c in cles) \
            or sorted(cles) != sorted(graines.cles_de_l_aire_conditionnelle()):
        raise GardeArret("programme de l'aire conditionnelle : `cles` — les vingt clés de l'aire conditionnelle, chacune "
                         "une fois")
    return {"aires": aires, "cles": sorted(cles)}


def _en_json(objet):
    return json.loads(json.dumps(objet, ensure_ascii=False, allow_nan=False))


def confronter_au_fichier_des_grandeurs(rendu: Mapping, autres: Mapping, sortie: Path, configuration_scellee: Path,
                                        origine) -> str:
    """Les aires rendues sont **celles du fichier scellé des grandeurs de l'étape (n)** que le programme a écrit (rejoué
    sur ses pièces par l'analyse), avec les mêmes clés et les mêmes autres grandeurs ; sinon garde ordinaire. Rend
    l'empreinte du fichier des grandeurs ; son contenu n'est pas gardé."""
    contenu, empreinte = analyse.exiger_fichier_des_grandeurs_de_l_etape_n(sortie, configuration_scellee,
                                                                           sortie_d_origine=origine)
    grandeurs = contenu["grandeurs"]
    attendues = _en_json({analyse._forme_dose(d): {m: dict(rendu["aires"][(m, d)]) for m in analyse.MONITEURS}
                          for d in analyse.QUATRE_DOSES})
    accord = (grandeurs.get("aire_conditionnelle") == attendues and grandeurs.get("cles_des_tirages") == rendu["cles"]
              and grandeurs.get("autres_grandeurs") == _en_json(autres))
    del contenu, grandeurs
    if not accord:
        raise GardeArret("programme de l'aire conditionnelle : les aires qu'il rend ne sont pas celles du fichier scellé des "
                         "grandeurs de l'étape (n) — refusé")
    return empreinte


def jouer_l_aire_conditionnelle(programme: tuple[Path, str], fichier: Path, sortie: Path, configuration_scellee: Path,
                                origine, entree: Mapping, autres: Mapping) -> dict:
    """Lance le programme de l'aire conditionnelle **comme une commande à part**, depuis une copie de ses octets
    vérifiés à l'empreinte inscrite (vérifiée ici une seconde fois). Le chemin du fichier lui est passé tel quel ;
    l'enchaînement ne l'ouvre pas. Code 0 : les aires, lues par `aires_rendues`, confrontées au fichier des grandeurs ;
    code 3 : l'arrêt consigné par l'analyse pour cette livraison, à l'étape (n), est relevé de son seul constat ; code
    4 : la ligne de sa garde ; tout autre code ou toute autre forme : garde ordinaire, rien de ses sorties n'est rendu."""
    chemin, sha256_inscrit = programme
    octets = octets_du_programme_de_l_aire(chemin, sha256_inscrit)
    if analyse.etape_n_aboutie(configuration_scellee):
        raise GardeArret("étape (n) : le fichier des grandeurs existe déjà — l'étape n'est pas rejouée (6.9 ; 8.4)")
    donnees = json.dumps({"actions_desappariees": entree["desappariees_ecrites"],
                          "taches_de_verification": entree["taches"],
                          "entropie_de_la_configuration_du_bras": entree["entropie"], "autres_grandeurs": autres},
                         ensure_ascii=False, sort_keys=True)
    arguments = ["--configuration", str(configuration_scellee), "--sortie", str(sortie), "--fichier-des-unites", str(fichier)]
    if origine is not None:
        arguments += ["--sortie-d-origine", str(origine)]
    with tempfile.TemporaryDirectory(prefix="aire-conditionnelle-") as d:
        copie = Path(d) / Path(chemin).name
        copie.write_bytes(octets)
        try:
            fait = subprocess.run([sys.executable, str(copie), *arguments], input=donnees, capture_output=True, text=True,
                                  timeout=DELAI_DU_PROGRAMME_DE_L_AIRE, env=_environnement(), cwd=str(RACINE_DU_CODE))
        except (OSError, subprocess.TimeoutExpired) as x:
            raise GardeArret(f"programme de l'aire conditionnelle : non lancé, ou hors délai ({type(x).__name__})") from None
    compte = {"commande": [sys.executable, str(chemin), *arguments], "sha256": sha256_inscrit, "code": fait.returncode}
    if fait.returncode == CODE_DES_AIRES:
        rendu = aires_rendues(fait.stdout)
        compte["sha256_du_fichier_des_grandeurs"] = confronter_au_fichier_des_grandeurs(
            rendu, autres, sortie, configuration_scellee, origine)
        compte["aires_rendues"] = len(rendu["aires"])
        del rendu
        return compte
    if fait.returncode == CODE_DE_L_ARRET and fait.stdout == "":
        consigne = analyse.arret_de_la_livraison(sortie, configuration_scellee)
        if consigne is None:
            raise GardeArret("programme de l'aire conditionnelle : arrêt annoncé (code 3), mais aucun arrêt consigné pour "
                             "cette livraison — refusé")
        constat = arrets.exiger_constat(consigne["constat"])
        if constat["etape"] != ETAPE_N:
            raise GardeArret("programme de l'aire conditionnelle : l'arrêt consigné n'est pas un arrêt de l'étape (n) — refusé")
        raise arrets.ArretDeLaLectureDeLaDiscretion(**constat)
    erreur = fait.stderr
    if fait.returncode == CODE_DE_LA_GARDE and fait.stdout == "" and erreur.count("\n") == 1 and erreur.endswith("\n") \
            and erreur.strip():
        raise GardeArret(f"programme de l'aire conditionnelle, garde ordinaire : {erreur.strip()[-600:]}")
    raise GardeArret(f"programme de l'aire conditionnelle : arrêt sans aires (code {fait.returncode}), ou sortie hors de sa "
                     "forme — rien de ses sorties n'est rendu")


# --- l'enchaînement --------------------------------------------------------------------------------------------------------

def _pieces_du_dossier_de_course(course: Path) -> dict:
    """Chaque fichier du dossier de course et son empreinte (chemin relatif au dossier de course)."""
    return {p.relative_to(course).as_posix(): _sha256(p) for p in sorted(course.rglob("*")) if p.is_file()}


def _a_jouer(configuration: Mapping) -> str:
    rang_m = analyse.exiger_un_seul_fichier_de_l_etape_m(configuration)
    if rang_m is None:
        return A_JOUER_M_PUIS_N
    return A_JOUER_N if rang_m == configuration["rang"] else A_JOUER_REPRISE_N


def _exiger_hors_du_dossier_de_course(course: Path, pieces: Mapping[str, object]) -> None:
    for nom, chemin in pieces.items():
        if chemin is not None and _sous(chemin, course):
            raise RegleNonEcrite(f"{nom} rangé(e) sous le dossier de course ({course}) : le versement de l'enchaînement la "
                                 "prendrait ; le texte n'écrit pas si le dossier de course la porte (8.7 nomme ce qu'il "
                                 "porte : configuration, constat de lancement, ouverture, dossier des arrêts, constats, "
                                 "fichier de l'étape (m))")


def enchainer(*, configuration_scellee, sortie_de_la_lecture_commune, registre_courant, commit_du_registre_courant: str,
              registre_fige, ligne_de_go, entree, sortie_d_origine, programme_du_constat, distant: str,
              branche: str, horloge: Callable[[], datetime.datetime], racine_du_code) -> dict:
    """Joue la lecture de la discrétion (module en tête). Tous les arguments sont nommés et exigés, sans valeur par
    défaut ; `registre_fige` et `ligne_de_go` valent `None` pour une première livraison ; `sortie_d_origine` n'est
    donnée que pour une reprise de l'étape (n). `horloge` rend l'heure UTC (constat, contrôle). `racine_du_code` : le
    dépôt dont la garde statique lit `src` et `scripts`. Le programme de l'aire conditionnelle et le chemin du fichier
    viennent de l'entrée scellée (version 2). Rend le compte rendu ; lève `ArretDeLEnchainement` (après versement),
    `EchecDuVersement` (rien n'est rendu), `RegleNonEcrite` ou `GardeArret` (avant tout constat : rien n'est lu)."""
    for nom, x in (("distant", distant), ("branche", branche), ("commit_du_registre_courant", commit_du_registre_courant)):
        if not isinstance(x, str) or not x.strip():
            raise GardeArret(f"enchaînement : `{nom}` exigé (un texte non vide), sans valeur par défaut")
    if (registre_fige is None) != (ligne_de_go is None):
        raise GardeArret("enchaînement : registre figé et ligne de GO vont ensemble — tous deux pour une livraison refaite, "
                         "aucun pour une première livraison")
    configuration_scellee = Path(configuration_scellee).resolve()
    configuration = conf_mod.lire_la_configuration_scellee(configuration_scellee)
    course = conf_mod.dossier_de_la_livraison(configuration).parent
    arrets_dossier = conf_mod.dossier_des_arrets(configuration)
    if not _sous(arrets_dossier, course):
        raise RegleNonEcrite(f"dossier des arrêts ({arrets_dossier}) hors du dossier de course ({course}) : 8.7 range le "
                             "dossier des arrêts dans le dossier de course ; le texte n'écrit pas ce que fait l'enchaînement "
                             "d'un dossier des arrêts rangé ailleurs")
    _exiger_hors_du_dossier_de_course(course, {
        "la sortie de la lecture commune": sortie_de_la_lecture_commune, "la sortie d'origine": sortie_d_origine,
        "l'entrée de l'enchaînement": entree, "le registre courant": registre_courant, "le registre figé": registre_fige})
    depot_du_dossier_de_course(course)
    lue = lire_l_entree(entree)
    _exiger_hors_du_dossier_de_course(course, {"le fichier des scores par unité": lue["fichier"],
                                               "le programme de l'aire conditionnelle": lue["programme_de_l_aire"][0]})
    resultat_a = exiger_etape_m_jouee(lue)
    racine_du_code = Path(racine_du_code)
    cloisonnement.exiger_garde_statique(racine_du_code, DOSSIERS_DE_LA_GARDE_STATIQUE)
    cr = {"version": VERSION, "programmes": programmes_joues(programme_du_constat),
          "garde_statique": {"racine": str(racine_du_code), "dossiers": list(DOSSIERS_DE_LA_GARDE_STATIQUE),
                             "violations": 0,
                             "chemins_elagues": cloisonnement.chemins_elagues(racine_du_code, DOSSIERS_DE_LA_GARDE_STATIQUE),
                             "listages_a_relire": cloisonnement.listages_a_relire(racine_du_code, DOSSIERS_DE_LA_GARDE_STATIQUE)},
          "dossier_de_course": str(course), "dossier_des_arrets": str(arrets_dossier),
          "configuration": {"chemin": str(configuration_scellee), "sha256": configuration["sha256"], "rang": configuration["rang"]},
          "livraison": {"chemin": str(Path(sortie_de_la_lecture_commune).resolve()), "sha256": _sha256(sortie_de_la_lecture_commune)},
          "entree": {"chemin": str(Path(entree).resolve()), "sha256": lue["sha256"]},
          "ligne_de_go": ligne_de_go, "constats": [], "versements": [], "etapes_jouees": []}
    cr["versements"].append(verser(course, distant, branche, "ouverture de l'enchaînement"))
    issue = motif = arret_constat = None
    try:
        # le programme de l'aire conditionnelle : son empreinte, avant tout constat et toute lecture
        chemin_de_l_aire, sha256_de_l_aire = lue["programme_de_l_aire"]
        octets_du_programme_de_l_aire(chemin_de_l_aire, sha256_de_l_aire)
        cr["programmes"]["programme_de_l_aire_conditionnelle"] = [str(chemin_de_l_aire), sha256_de_l_aire]
        a_jouer = _a_jouer(configuration)
        cr["a_jouer"] = a_jouer
        if sortie_d_origine is not None and a_jouer != A_JOUER_REPRISE_N:
            raise GardeArret("sortie d'origine donnée hors d'une reprise de l'étape (n) — refusé")
        _etapes(cr, configuration, configuration_scellee, course, lue, resultat_a, a_jouer,
                sortie=Path(sortie_de_la_lecture_commune), registre_courant=registre_courant,
                commit=commit_du_registre_courant, registre_fige=registre_fige, ligne_de_go=ligne_de_go,
                sortie_d_origine=sortie_d_origine, programme_du_constat=Path(programme_du_constat), distant=distant,
                branche=branche, horloge=horloge)
    except EchecDuVersement:
        raise
    except arrets.ArretDeLaLectureDeLaDiscretion as x:      # 6.9 : de l'exception levée, son constat seul
        issue, arret_constat = ISSUE_ARRET, x.constat()
    except _ConstatMalsain as x:
        issue, motif = ISSUE_CONSTAT_MALSAIN, x.args[0]
    except RegleNonEcrite as x:
        issue, motif = ISSUE_REGLE_NON_ECRITE, str(x)
    except GardeArret as x:
        issue, motif = ISSUE_GARDE, str(x)
    except Exception as x:                                  # noqa: BLE001 — son type seul : aucune variable n'en sort
        issue, motif = ISSUE_ERREUR, type(x).__name__
    if issue is None:
        cr["issue"] = ISSUE_ABOUTIE
        cr["pieces_du_dossier_de_course"] = _pieces_du_dossier_de_course(course)
        cr["compte_des_livraisons"] = analyse.compte_des_livraisons(configuration_scellee)
        return cr
    # tout arrêt est versé avant d'être rendu ; un versement en échec ne rend rien
    cr["versements"].append(verser(course, distant, branche, f"arrêt : {issue}"))
    cr.update(issue=issue, motif_de_l_arret=motif, constat_de_l_arret=arret_constat,
              pieces_du_dossier_de_course=_pieces_du_dossier_de_course(course))
    raise ArretDeLEnchainement(issue, cr)


class _ConstatMalsain(Exception):
    pass


def _date(horloge) -> str:
    t = horloge()
    if not isinstance(t, datetime.datetime) or t.tzinfo is None or t.utcoffset() != datetime.timedelta(0):
        raise GardeArret("horloge : une date en temps universel exigée")
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def _etapes(cr: dict, configuration: Mapping, configuration_scellee: Path, course: Path, lue: Mapping,
            resultat_a: verdicts.ResultatA, a_jouer: str, *, sortie: Path, registre_courant, commit: str, registre_fige,
            ligne_de_go, sortie_d_origine, programme_du_constat: Path, distant: str, branche: str, horloge) -> None:
    arrets_dossier = conf_mod.dossier_des_arrets(configuration)
    constat_present = (conf_mod.dossier_de_la_livraison(configuration) / conf_mod.NOM_DU_CONSTAT_DE_LANCEMENT).exists()
    acte_present = (arrets_dossier / analyse.NOM_DES_ACTES_DE_REPRISE.format(_sha256(sortie)[:16])).exists()
    faut_un_constat = a_jouer == A_JOUER_M_PUIS_N or (a_jouer == A_JOUER_REPRISE_N and not acte_present)
    if faut_un_constat:                              # le constat d'abord, dans la même exécution que la lecture
        c = jouer_le_constat(programme_du_constat, configuration_scellee, registre_courant, commit=commit,
                             date_utc=_date(horloge), registre_fige=registre_fige, ligne_de_go=ligne_de_go,
                             mode=MODE_CONTROLE if constat_present else MODE_CONSTAT)
        cr["constats"].append(c)
        cr["versements"].append(verser(course, distant, branche, f"{c['mode']} de lancement"))
        if not c["sain"]:
            raise _ConstatMalsain(f"{c['mode']} malsain : la lecture ne part pas — {c['sortie_d_erreur'][-600:]}")
    if a_jouer == A_JOUER_M_PUIS_N:
        resultat = analyse.regle_de_discretion(sortie, configuration_scellee, go_de_la_reprise=ligne_de_go,
                                               registre_fige=registre_fige)
        analyse.exiger_resultat_de_discretion(resultat)
        lignes_c = {p: verdicts.ligne_table_c(lue["base"][p], lue["cout"][p], resultat, p)
                    for p in analyse.DOSES_VERDICT if lue["lignes_b"][p] == "B8"}
        verdicts.ecrire_fichier_de_l_etape_m(journal=lue["journal"], revision_refusee=lue["revision_refusee"],
                                             gardees_lues=lue["gardees_lues"], renvoi_de_la_base=lue["renvoi_de_la_base"],
                                             effectifs_de_la_base_conformes=lue["effectifs_de_la_base_conformes"],
                                             resultat_de_discretion=resultat, lignes_c=lignes_c)
        del resultat, lignes_c                       # rien de l'étape (m) ne reste en mémoire pendant le versement
        # versement avant lecture (8.7) : rien de l'étape (m) n'est rendu avant que ce poussage ait réussi
        cr["versements"].append(verser(course, distant, branche, "étape (m)"))
        cr["etapes_jouees"].append(ETAPE_M)
        # après le poussage seulement : le déclencheur de 7.6, relu du fichier scellé de l'étape (m) (6.3 (m))
        contenu, _ = analyse.exiger_fichier_de_l_etape_m(sortie, configuration_scellee)
        cr["declencheur_au_moins_une_dose_en_c6"] = verdicts.declencheur_dose_en_c6(
            resultat_a, {analyse._dose_de(d): l for d, l in contenu["lignes_de_la_table_c"].items()})
        del contenu
    origine = None
    if a_jouer == A_JOUER_REPRISE_N:
        if sortie_d_origine is None:
            raise GardeArret("reprise de l'étape (n) : la sortie d'origine est exigée (6.9)")
        origine = Path(sortie_d_origine)
        analyse.ouvrir_la_reprise_de_l_etape_n(sortie, configuration_scellee, sortie_d_origine=origine,
                                               go_de_la_reprise=ligne_de_go, registre_fige=registre_fige)
        cr["versements"].append(verser(course, distant, branche, "acte de reprise de l'étape (n)"))
    # étape (n) : le programme de l'aire conditionnelle, lancé à part ; il lit le fichier et écrit le fichier des grandeurs
    autres = {"etat_de_la_base": {analyse._forme_dose(p): verdicts.etat_ecrit_de_la_base(lue["base"][p])
                                  for p in analyse.QUATRE_DOSES}}
    cr["programme_de_l_aire_conditionnelle"] = jouer_l_aire_conditionnelle(
        lue["programme_de_l_aire"], lue["fichier"], sortie, configuration_scellee, origine, lue, autres)
    cr["versements"].append(verser(course, distant, branche, "étape (n)"))
    cr["etapes_jouees"].append(ETAPE_N)


# --- commande ------------------------------------------------------------------------------------------------------------

CODES_DE_SORTIE = {ISSUE_ABOUTIE: 0, ISSUE_ARRET: 3, ISSUE_GARDE: 4, ISSUE_CONSTAT_MALSAIN: 5, ISSUE_REGLE_NON_ECRITE: 6,
                   ISSUE_ERREUR: 8}
CODE_ECHEC_DU_VERSEMENT = 7


def _horloge_du_systeme() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)


def main(argv: list[str]) -> int:
    lecteur = argparse.ArgumentParser(description="Enchaînement de la lecture de la discrétion, bras A (version 2).")
    lecteur.add_argument("--configuration", required=True)
    lecteur.add_argument("--sortie", required=True, help="sortie scellée de la lecture commune des cinq moniteurs")
    lecteur.add_argument("--registre-courant", required=True)
    lecteur.add_argument("--commit-du-registre", required=True)
    lecteur.add_argument("--registre-fige", default=None)
    lecteur.add_argument("--ligne-de-go", default=None)
    lecteur.add_argument("--entree", required=True,
                         help="entrée scellée de l'enchaînement (dont le programme de l'aire conditionnelle et le fichier)")
    lecteur.add_argument("--sortie-d-origine", default=None)
    lecteur.add_argument("--programme-du-constat", required=True)
    lecteur.add_argument("--distant", required=True)
    lecteur.add_argument("--branche", required=True)
    a = lecteur.parse_args(argv)
    try:
        cr = enchainer(configuration_scellee=a.configuration, sortie_de_la_lecture_commune=a.sortie,
                       registre_courant=a.registre_courant, commit_du_registre_courant=a.commit_du_registre,
                       registre_fige=a.registre_fige, ligne_de_go=a.ligne_de_go, entree=a.entree,
                       sortie_d_origine=a.sortie_d_origine, programme_du_constat=a.programme_du_constat,
                       distant=a.distant, branche=a.branche, horloge=_horloge_du_systeme,
                       racine_du_code=RACINE_DE_LA_GARDE_STATIQUE)
    except EchecDuVersement as e:
        print(f"VERSEMENT EN ÉCHEC — rien n'est rendu ; le versement est à refaire avant toute lecture : {e}", file=sys.stderr)
        return CODE_ECHEC_DU_VERSEMENT
    except ArretDeLEnchainement as e:
        e.compte_rendu["commande"] = ["python", "-m", __name__, *argv]
        print(json.dumps(e.compte_rendu, ensure_ascii=False, sort_keys=True))
        return CODES_DE_SORTIE[e.issue]
    except (RegleNonEcrite, GardeArret) as e:
        print(f"ARRÊT AVANT TOUT CONSTAT ({type(e).__name__}) : {e}", file=sys.stderr)
        return CODES_DE_SORTIE[ISSUE_REGLE_NON_ECRITE if isinstance(e, RegleNonEcrite) else ISSUE_GARDE]
    cr["commande"] = ["python", "-m", __name__, *argv]
    print(json.dumps(cr, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
