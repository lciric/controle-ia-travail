#!/usr/bin/env python3
"""Épreuve des témoins du juge — course d'auto-conception de l'organisme d'idéation, version 5 (tentative neuve, additif v2e).

Version 5 (R12 ; la v4, `scripts/epreuve_temoins_auto_conception_v4.py`, `04f62b8c…`, reste en place, scellée ; son épreuve
réelle du 18 novembre 2026, « réussie », 1,204591 USD, rapport `course-v2/epreuve-temoins-reelle-auto-conception-v4.json`,
`980e8888…`, ne vaut que pour la course v4). La course v4 est close (code 2, étape « proposition » non mesurée pour cause
technique, 44,780492 USD) ; mot de Lazar « 2a » : tentative **neuve** après le diagnostic, correction ciblée de Carbon. Le
préenregistrement exige une épreuve réelle **du jour**, aux empreintes du lanceur qui part (`empreintes.lanceur`) : le rapport
v4 cite le lanceur v4 et le 18 novembre ; une épreuve neuve est donc exigée le jour de la tentative. Ce que la v5 change, et
rien d'autre :
1. chemins neufs (`course-v3/`) : déclaration des relais de l'épreuve `declaration-relais-epreuve-temoins-auto-conception-v5.json`,
   rapport `epreuve-temoins-reelle-auto-conception-v5.json` (le programme refuse de partir s'il existe déjà : une épreuve par
   tentative) ; lanceur **v5** ;
2. la décision de reprise unique de la v4 (`GO-2026-11-18-36`, échue) et le retranchement de la tentative v3 ne s'appliquent
   plus : l'épreuve part sous la **ligne de GO neuve de l'épreuve** nommée par la pièce de départ v2e (`go_epreuve` ; le lanceur
   v5 refuse les lignes consommées par la course v4 : `GO-2026-11-18-20`, `-21`, `-36`), plafond **5 USD** entier ;
3. **mot de reprise** exigé avant tout appel : la ligne de GO de la course neuve (`tentative_neuve.mot_de_reprise` de la pièce,
   égale à `go_course`) au registre lu au commit de `main`, type « calcul », accordée par Lazar, plafond 90 USD, périmètre qui
   dit « auto-conception » et « tentative neuve » (`verifier_mot_de_reprise` du lanceur v5) : pas d'épreuve sans tentative
   accordée ;
4. tentatives précédentes rapportées à côté, jamais masquées (`tentatives_precedentes`) : la v3 (`1e11376f…`, « échouée »,
   causes techniques, 0,132289 USD) et la v4 (`980e8888…`, « réussie », 1,204591 USD), verdicts et classes bruts compris ;
   elles ne comptent pas dans le verdict de la v5.
Inchangés à l'octet : `lire_epreuve`, `verite`, `jouer`, `servir`, `controles_statiques`, le mode hors ligne, les juges factices,
la sonde du bac, la borne du relais d'Argon (2 × 11 + 2 = 24), la requalification des manques techniques (`qualifier_verdict`) ;
témoins v2, consignes, configuration, 33 appels, ordre des appels, juges et aiguilleur.

Texte de la v4 :

Épreuve des témoins du juge — course d'auto-conception de l'organisme d'idéation, version 4 (correctif v2d).

Version 4 (R12 ; la v3, `scripts/epreuve_temoins_auto_conception_v3.py`, `0c72dd87…`, reste en place, scellée) — épreuve
réelle v3 jouée le 18 novembre 2026 à 16:11Z (rapport scellé `course-v2/epreuve-temoins-reelle-auto-conception-v3.json`,
`1e11376f…`, verdict écrit « échouée », 0,132289 USD ; sortie d'erreur versée `course-v2/epreuve-reelle-v3-2026-11-18-v1/`).
Deux causes **techniques**, aucune réponse de juge Claude rendue :
(1) le bac à sable du kit n'était pas installé (bwrap, socat) : l'aiguilleur et le juge Claude ont refusé de démarrer
    (« sandbox required but unavailable ») ; le v3 ne sondait pas le bac avant les appels (le lanceur, lui, le fait) ;
(2) chaque jugement d'Argon coûte **deux** appels au relais Gemini (`countTokens` puis `generateContent` : `commande_argon_v3d.py`,
    `--compter-jetons` actif par défaut ; le relais `relais_gemini_v2.py` compte les deux actions dans `--max-appels`) ; le
    relais de l'épreuve était borné à 15 pour 11 témoins (22 appels de relais) : t08 à t11 refusés par le relais (429).
Correction (mot de Lazar « go (a), lance les deux correctifs », 18 novembre 2026 ; additif
`course-v2/additif-preenregistrement-course-auto-conception-v2d.md`), **avant tout appel et avant la transmission des plafonds** :
1. **sonde du bac à sable** par la commande de l'orchestrateur épinglé (`etat_bac_a_sable_detaille`, par `sonder_bac_a_sable` du
   lanceur v4, même exigence : `actif` et `proc_neuf` vrais) ; sinon refus, code 2, rien dépensé (`exiger_bac_a_sable`) ;
2. **borne du relais d'Argon** : `--max-appels` lu par PID (arguments) et par `/relais/etat` ≥ 2 × (appels d'Argon du plan) +
   marge 2 (`appels_relais_gemini_requis` du lanceur v4 : 2 × 11 + 2 = 24 pour l'épreuve) ; sinon refus, code 2
   (`verifier_procedure_relais` du lanceur v4, puis `verifier_borne_argon`, qui relit l'état) ;
3. **manques techniques** : chaque appel dont l'adaptateur rend le statut « erreur » (appel parti mais échoué : bac, refus du
   relais, réseau, délai) ou qui n'est pas parti est consigné (`incidents_techniques`) ; si **tous** les manques de la lecture
   gelée sont de cette sorte, le verdict écrit est « non conclue » et non « échouée » (`qualifier_verdict`) — comme `motif_arret`
   le fait déjà ; un verdict de juge lu et faux (ou une réponse lue illisible, un refus du modèle, un budget ou des tours
   épuisés) reste un échec, et « échouée » demeure dès qu'il en existe un. **`lire_epreuve` est identique à l'octet** ; la
   requalification ne peut jamais rendre « réussie » ;
4. chemins neufs : rapport `course-v2/epreuve-temoins-reelle-auto-conception-v4.json` (le programme refuse de partir s'il existe
   déjà : **une reprise unique**), déclaration `course-v2/declaration-relais-epreuve-temoins-auto-conception-v4.json`, lanceur v4 ;
5. décision de Lazar `GO-2026-11-18-36` (type « décision », registre lu au commit de `main`, échéance le 18 novembre 2026) :
   la ligne doit y figurer, sinon refus ; **plafond inchangé, 5 USD au total, tentative v3 comprise** : la dépense de la
   tentative v3, lue dans son rapport scellé (empreinte épinglée `1e11376f…`, 0,132289 USD), est retranchée ; la reprise
   n'appelle que tant que le cumul plus le plafond de session de l'appel suivant tient sous 5 − 0,132289 = 4,867711 USD, et
   c'est ce budget (au centime inférieur, 4,86 USD) qui est transmis aux portes ; les 7 verdicts d'Argon de la tentative v3 ne
   comptent pas dans le verdict (ils sont rapportés à part, `tentative_precedente`).
Rien d'autre ne change : témoins, consignes, configuration, matière, lecture gelée, plafond 5 USD, 33 appels, ordre des appels,
juges et aiguilleur, mode hors ligne.

Texte de la v3 :

Épreuve des témoins du juge — course d'auto-conception de l'organisme d'idéation, version 3 (correctif v2c).

Version 3 (R12 ; la v2, `scripts/epreuve_temoins_auto_conception_v2.py`, `19d03876…`, reste en place, scellée) — défaut
constaté en réel le 18 novembre 2026, avant tout appel (0 USD ; sortie d'erreur versée :
`course-v2/epreuve-reelle-arret-avant-appel-2026-11-18-v1/epreuve-reelle.stderr.txt`) : `reel()` remettait aux adaptateurs
réels de l'orchestrateur (`adaptateurs_reels_v56`) les chemins interdits en lecture `[base des sessions, sortie/"sortie"]`
mais passait `sortie/"appels"` comme dossier des agents ; la garde de `construire_options` (`pole/adaptateurs.py`) refusait
donc le premier appel du kit (« le dossier de l'agent doit être sous un chemin interdit en lecture (sinon la fiche voisine
reste lisible) »). Le mode hors ligne n'emploie pas les adaptateurs réels et ne l'a pas vu. Correction (mot de Lazar
« go (a), lance les deux correctifs », 18 novembre 2026 ; additif `course-v2/additif-preenregistrement-course-auto-
conception-v2c.md`) :
1. les dossiers d'appel sont **sous la sortie interdite en lecture** remise aux adaptateurs : `sortie/"sortie"/"appels"/
   <étiquette>/<témoin>` (chemin réel, `dossier_des_appels`) ; un juge ne lit ni la fiche voisine ni le dossier d'un autre
   rôle (tous sous `sortie/"sortie"`, interdit ; seul son dossier est rouvert) ;
2. **garde avant tout appel et avant la transmission des plafonds** (`preparer_appels`, `verifier_dossiers_d_appel`) : pour
   chaque rôle servi par le kit, `construire_options` de l'orchestrateur épinglé (fonction pure, aucun appel) est jouée sur le
   dossier exact de chaque appel du plan, avec la liste interdite de l'adaptateur ; chaque autre dossier du plan doit y être
   interdit et non rouvert ; un refus arrête l'épreuve (code 2) sans rien dépenser ; rôles des commandes externes : sans
   objet (aucun bac du kit ; consigne sur l'entrée standard, aucun outil), dit au rapport ;
3. chemins neufs : déclaration des relais de l'épreuve `declaration-relais-epreuve-temoins-auto-conception-v3.json` (l'ancienne,
   scellée, porte des PID morts), rapport `epreuve-temoins-reelle-auto-conception-v3.json`, lanceur v3.
Rien d'autre ne change : témoins, consignes, configuration, lecture gelée `lire_epreuve`, plafond 5 USD, 33 appels, ordre
des appels, juges et aiguilleur, mode hors ligne.

Texte de la v2 :

Épreuve des témoins du juge — course d'auto-conception de l'organisme d'idéation, version 2.

Version 2 (R12 ; la v1, `scripts/epreuve_temoins_auto_conception_v1.py`, `5e354e7d…`, reste en place) — contre-lecture de la
v1 par le modèle K : témoins v2 (constat 2) ; l'épreuve hors ligne éprouve aussi la **longueur du seul champ lu par chaque
item** (règle de seuil par champ, et un juge factice qui la suit) et dit sa limite (constat 4) : elle éprouve un plancher de
lecture de forme, jamais le pouvoir de discrimination d'un juge sur des défauts non déclarés ; le rapport réel garde les
**verdicts et classes bruts**, pour que le lanceur recalcule le verdict (constat 11).

Texte de la v1 :

Épreuve des témoins du juge — course d'auto-conception de l'organisme d'idéation, version 1.

Leçon des courses passées (R-3221, R-3229, R-3234 ; course v7 des organismes discrets finie en code 4, témoins échoués chez
un juge) : des témoins mal écrits rendent une course illisible ; ils s'éprouvent **avant** toute course, et rien ne part sans
cette épreuve réussie. Les témoins (`temoins-juge-auto-conception-v1.json`) sont des cartes de conception plantées, bonnes et
mauvaises, de classe connue par construction, écrites à la lettre de la consigne du juge.

Deux modes, la même lecture (`lire_epreuve`) :

- `--hors-ligne SORTIE_NEUVE [--matiere MATIERE.md]` : aucun appel. Les témoins sont servis par les **vraies** fonctions de
  service de l'orchestrateur épinglé (`fiches_v54.entree_une_fiche`, garde A4 comprise ; lecture par `lire_verdict` et
  `lire_classe`) à des juges factices : un juge parfait (rend la vérité plantée), des juges au hasard (graines dérivées par
  `numpy.random.SeedSequence`, R9), un juge biaisé vers la longueur, un juge indulgent, un juge sévère ; un aiguilleur
  parfait et un aiguilleur artefact. Il montre que les témoins **séparent** le juge parfait des autres, qu'aucune règle de
  seuil sur la longueur ne les classe, que leurs champs tiennent dans les bornes de la consigne, que chaque identifiant du
  catalogue qu'ils citent existe dans la matière servie, et qu'aucun titre de témoin n'apparaît dans la consigne servie.
- `--reel` (session d'exécution seulement, jamais lancé ici) : les juges et l'aiguilleur **de la configuration de la course**,
  par les relais déclarés pour l'épreuve (`declaration-relais-epreuve-temoins-auto-conception-v1.json`, scellée), sous la
  ligne de GO de l'épreuve (pièce de départ de la mère), plafond 5 USD ; écrit, scellé, le rapport que le lanceur de la course
  exige (`course-v1/epreuve-temoins-reelle-auto-conception-v1.json`). **Règle écrite d'avance** : un témoin manqué par un juge
  ou par l'aiguilleur → verdict « échouée » → aucune course, et aucune retouche des témoins sans version neuve (R12) et mot de
  la mère. Plafond atteint, refus pour crédit ou réponse illisible → « non conclue » → aucune course.

Codes : 0 épreuve écrite (lire le verdict) ; 2 refus avant tout appel.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import importlib.util
import json
import os
import re
import statistics
import sys
import tempfile
from pathlib import Path

VERSION = "epreuve_temoins_auto_conception_v5"
DEPOT = Path(__file__).resolve().parents[1]
COURSE_V1 = "docs/notes/organisme-auto-conception-v1/course-v1"
COURSE = "docs/notes/organisme-auto-conception-v1/course-v2"
COURSE_V3 = "docs/notes/organisme-auto-conception-v1/course-v3"                                       # v5 : dossier neuf
TEMOINS = DEPOT / COURSE / "temoins-juge-auto-conception-v2.json"
CONSIGNE_JUGE = DEPOT / COURSE_V1 / "consigne-juge-auto-conception-v1.md"
CONSIGNE_AIGUILLEUR = DEPOT / COURSE_V1 / "consigne-aiguilleur-auto-conception-v1.md"
CONSIGNE_PROPOSEUR = DEPOT / COURSE / "consigne-proposeur-auto-conception-v2.md"
CONFIGURATION = DEPOT / COURSE / "configuration-course-auto-conception-v2.json"
DECLARATION_EPREUVE = DEPOT / COURSE_V3 / "declaration-relais-epreuve-temoins-auto-conception-v5.json"  # v5 : chemin neuf
RAPPORT_REEL = DEPOT / COURSE_V3 / "epreuve-temoins-reelle-auto-conception-v5.json"                       # v5 : chemin neuf
# v4 : tentative précédente (scellée), citée par le rapport ; ses verdicts sont rapportés à côté de ceux de la reprise
RAPPORT_TENTATIVE_V3 = DEPOT / COURSE / "epreuve-temoins-reelle-auto-conception-v3.json"
# v5 : épreuve v4 (« réussie » le 18 novembre, pour la course v4), rapportée à côté, jamais comptée dans le verdict de la v5
RAPPORT_TENTATIVE_V4 = DEPOT / COURSE / "epreuve-temoins-reelle-auto-conception-v4.json"
SHA_TENTATIVE_V4 = "980e888898c180b347d526d75bdc41d531ec26943c043a96e44c24c0853337be"
LANCEUR = DEPOT / "scripts" / "lancer_course_auto_conception_v5.py"                                     # v5 : lanceur v5
# v4 : statut d'adaptateur tenu pour une cause technique (appel parti mais échoué : bac, relais, réseau, délai) ; « refus »
# (refus ou changement de modèle), « budget_depasse », « tours_epuises » et une réponse « ok » illisible restent des échecs.
STATUTS_TECHNIQUES = ("erreur",)
# v4 : décision de reprise de Lazar et tentative v3 (dépense retranchée du plafond de 5 USD au total)
GO_REPRISE = "GO-2026-11-18-36"
SHA_TENTATIVE_V3 = "1e11376fe1255d281212bac086f25d143ab8c86f520dd16f3207ad95d40d02cf"
MOTIF_NON_PARTI = "appel non parti (arrêt de l'épreuve avant cet appel)"
PLAFOND_EPREUVE_USD = 5.0
ETAPE = "epreuve-temoins"
RACINE_GRAINES = 2026111833
# Champ lu par chaque item dont un champ porte seul la lecture (constat 4).
CHAMP_LU = {"module_nomme": "module_change", "voisin_nomme": "plus_proche_voisin", "epreuve_plantee": "epreuve_monde_plante"}
N_JUGES_AU_HASARD = 2000
BORNE_CHAMP, BORNE_CARTE = 1200, 9000
ID_CATALOGUE = re.compile(r"(?<![\w-])([a-zéèêôûàç-]+) n° (\d+)", re.I)


# --- outils -----------------------------------------------------------------------------------------------------------------


def sha256_fichier(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def ecrire_scelle(chemin: Path, objet) -> str:
    donnees = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {Path(chemin).name}\n")
    return h


def charger_orchestrateur(racine: Path) -> dict:
    """Fonctions de service et de lecture de l'orchestrateur épinglé (aucune réécriture ici)."""
    racine = str(racine)
    if racine not in sys.path:
        sys.path.insert(0, racine)
    from pole import fiches_v54, juges_croises_v53, aiguilleur_v53  # noqa: E402
    return {"entree_une_fiche": fiches_v54.entree_une_fiche, "lire_verdict": juges_croises_v53.lire_verdict,
            "lire_classe": aiguilleur_v53.lire_classe, "racine": racine}


def charger_lanceur():
    spec = importlib.util.spec_from_file_location("lancer_course_auto_conception_v5", LANCEUR)
    m = importlib.util.module_from_spec(spec)
    sys.modules["lancer_course_auto_conception_v5"] = m
    spec.loader.exec_module(m)
    return m


def orchestrateur_present(candidats) -> Path:
    presents = [Path(o) for o in candidats if (Path(o) / "pole" / "fiches_v54.py").is_file()]
    if len(presents) != 1:
        raise SystemExit(f"orchestrateur : {len(presents)} copie(s) trouvée(s) (une exigée)")
    return presents[0]


# --- service et lecture -------------------------------------------------------------------------------------------------------


def identifiant_servi(etiquette: str, ident: str) -> str:
    return "F" + hashlib.sha256(f"epreuve-temoins|{etiquette}|{ident}".encode("utf-8")).hexdigest()[:5]


def servir(o: dict, consigne: str, temoin: dict, interdites: list, ident_servi: str | None) -> str:
    return o["entree_une_fiche"](consigne, {"contenu": temoin["contenu"]}, interdites, "mot_entier", ident_servi)


def verite(temoin: dict, items: list) -> dict:
    """Items attendus par construction : tous vrais pour un bon témoin ; l'item planté faux pour un mauvais (les autres items
    d'un mauvais témoin ne sont jamais lus comme critère)."""
    return {k: not (temoin["classe"] == "mauvais" and k == temoin["item_plante"]) for k in items}


def lire_epreuve(verdicts: dict, classes_aiguilleur: dict, temoins: dict, items: list) -> dict:
    """`verdicts` {juge: {id: verdict lu ou None}} ; `classes_aiguilleur` {id: classe lue ou None}. Règle gelée :
    un juge réussit si chaque bon témoin est notable (cinq items vrais) et si chaque mauvais témoin a son item planté faux ;
    l'aiguilleur réussit si chaque bon témoin est `niveau_methode` et si aucun témoin n'est `concret` ; une réponse illisible
    est un échec. Verdict : « réussie » si tous réussissent, « échouée » sinon."""
    par_juge = {}
    for juge, v in sorted(verdicts.items()):
        manques = []
        for tid, t in sorted(temoins.items()):
            lu = v.get(tid)
            if lu is None:
                manques.append({"temoin": tid, "motif": "verdict illisible ou absent"})
            elif t["classe"] == "bon" and not lu["notable"]:
                manques.append({"temoin": tid, "motif": "bon témoin non notable",
                                "items_faux": sorted(k for k in items if not lu["items"][k])})
            elif t["classe"] == "mauvais" and lu["items"][t["item_plante"]]:
                manques.append({"temoin": tid, "motif": f"item planté {t['item_plante']} rendu vrai"})
        par_juge[juge] = {"reussi": not manques, "manques": manques}
    manques_a = []
    for tid, t in sorted(temoins.items()):
        c = classes_aiguilleur.get(tid)
        if c is None:
            manques_a.append({"temoin": tid, "motif": "classe illisible ou absente"})
        elif c == "concret" or (t["classe"] == "bon" and c != "niveau_methode"):
            manques_a.append({"temoin": tid, "motif": f"classe {c}"})
    tous = all(x["reussi"] for x in par_juge.values()) and not manques_a and bool(par_juge)
    return {"verdict": "réussie" if tous else "échouée", "par_juge": par_juge,
            "aiguilleur": {"reussi": not manques_a, "manques": manques_a}}


# --- juges factices (hors ligne) ----------------------------------------------------------------------------------------------


class Reponse:
    def __init__(self, texte: str, modele: str):
        self.statut, self.texte_brut, self.texte_final, self.cout_declare_usd, self.modele_servi = "ok", texte, texte, 0.0, modele


def fiche_servie(consigne: str) -> dict:
    corps = consigne.rsplit("## La fiche\n```json\n", 1)[1].rsplit("\n```", 1)[0]
    d = json.loads(corps)
    d.pop("identifiant", None)
    return d


class JugeFactice:
    """`genre` : parfait | hasard | longueur | indulgent | severe. Le juge parfait reconnaît le témoin par son contenu et rend la
    vérité plantée ; le juge à la longueur rend tout vrai si la fiche servie est plus longue que la médiane des témoins, tout
    faux sinon."""

    def __init__(self, genre: str, temoins: dict, items: list, graine=None, mediane: float | None = None):
        self.genre, self.temoins, self.items, self.mediane = genre, temoins, items, mediane
        self.medianes_champ = {k: statistics.median(len(t["contenu"][c]) for t in temoins.values()) for k, c in CHAMP_LU.items()}
        if genre == "hasard":
            import numpy as np
            self.rng = np.random.default_rng(graine)

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        f = fiche_servie(consigne)
        if self.genre == "parfait":
            t = next(t for t in self.temoins.values() if t["contenu"] == f)
            items = verite(t, self.items)
        elif self.genre == "hasard":
            items = {k: bool(self.rng.integers(0, 2)) for k in self.items}
        elif self.genre == "longueur":
            long_ = len(json.dumps(f, ensure_ascii=False, indent=1)) > self.mediane
            items = {k: long_ for k in self.items}
        elif self.genre == "champ":  # v2 : chaque item vrai si son champ lu est plus long que la médiane de ce champ
            items = {k: (len(f[CHAMP_LU[k]]) > self.medianes_champ[k]) if k in CHAMP_LU else True for k in self.items}
        else:
            items = {k: self.genre == "indulgent" for k in self.items}
        return Reponse("```json\n" + json.dumps({"items": items, "note": "factice"}) + "\n```", modele or "factice")


class AiguilleurFactice:
    def __init__(self, classe: str):
        self.classe = classe

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        fiche_servie(consigne)
        return Reponse('```json\n{"classe": "%s", "categorie": "factice"}\n```' % self.classe, modele or "factice")


def jouer(o: dict, adaptateur, etiquette: str, modele: str, consigne: str, temoins: dict, items: list, interdites: list,
          dossier: Path, plafond_session: float, juge: bool = True) -> tuple:
    """Rend ({id: lu}, coût, modèles servis). Un appel par témoin, session neuve, identifiant opaque propre au juge."""
    lus, cout, servis = {}, 0.0, set()
    for tid in sorted(temoins):
        entree = servir(o, consigne, temoins[tid], interdites, identifiant_servi(etiquette, tid) if juge else None)
        d = dossier / etiquette / tid
        d.mkdir(parents=True, exist_ok=True)
        r = adaptateur.lancer("juge_ideation", entree, str(d), plafond_session, 1, modele=modele)
        cout += float(r.cout_declare_usd or 0.0)
        if r.statut == "ok" and r.modele_servi:
            servis.add(r.modele_servi)
        texte = r.texte_brut or r.texte_final if r.statut == "ok" else None
        lus[tid] = (o["lire_verdict"](texte, items) if juge else o["lire_classe"](texte)[0]) if texte else None
    return lus, cout, sorted(servis)


# --- contrôles des témoins eux-mêmes ------------------------------------------------------------------------------------------


def controles_statiques(temoins: dict, items: list, consigne_proposeur: str, matiere: bytes | None) -> dict:
    longueurs = {tid: len(json.dumps(t["contenu"], ensure_ascii=False, indent=1)) for tid, t in temoins.items()}
    bornes = {tid: max(len(v) for v in t["contenu"].values()) <= BORNE_CHAMP and longueurs[tid] <= BORNE_CARTE
              for tid, t in temoins.items()}
    # aucune règle de seuil sur la longueur ne classe tous les témoins (dans un sens ou dans l'autre)
    bons = {tid for tid, t in temoins.items() if t["classe"] == "bon"}
    erreurs_min = len(temoins)
    for s in sorted(set(longueurs.values())) + [0]:
        for sens in (1, -1):
            e = sum((sens * (longueurs[t] - s) > 0) != (t in bons) for t in temoins)
            erreurs_min = min(erreurs_min, e)
    par_champ = {}
    for item, champ in CHAMP_LU.items():
        sous = {tid: len(t["contenu"][champ]) for tid, t in temoins.items() if t["classe"] == "bon" or t["item_plante"] == item}
        bons_i = {tid for tid in sous if temoins[tid]["classe"] == "bon"}
        e_min = len(sous)
        for s_ in sorted(set(sous.values())) + [0]:
            for sens in (1, -1):
                e_min = min(e_min, sum((sens * (sous[t] - s_) > 0) != (t in bons_i) for t in sous))
        par_champ[item] = {"champ": champ, "longueurs": sous, "erreurs_min": e_min}
    champs = {tid: sorted(t["contenu"]) for tid, t in temoins.items()}
    titres_dans_la_consigne = sorted(tid for tid, t in temoins.items() if t["contenu"]["titre"].lower() in consigne_proposeur.lower())
    sortie = {"longueurs": longueurs, "bornes_tenues": all(bornes.values()), "bornes_par_temoin": bornes,
              "regle_de_seuil_sur_la_longueur_erreurs_min": erreurs_min,
              "regle_de_seuil_sur_le_champ_lu": par_champ,
              "regle_de_seuil_sur_le_champ_lu_erreurs_min": min(x["erreurs_min"] for x in par_champ.values()),
              "champs_identiques": len({tuple(v) for v in champs.values()}) == 1,
              "titres_de_temoin_dans_la_consigne_servie": titres_dans_la_consigne,
              "classes": {"bon": len(bons), "mauvais": len(temoins) - len(bons)},
              "items_plantes": sorted({t["item_plante"] for t in temoins.values() if t["item_plante"]}),
              "items_plantes_tous_couverts": sorted({t["item_plante"] for t in temoins.values() if t["item_plante"]}) == sorted(items)}
    if matiere is not None:
        texte = matiere.decode("utf-8")
        regroupements = set(re.findall(r"^\*\*([a-zéèêôûàç-]+ n° \d+) — ", texte, flags=re.M))
        cites, absents = {}, []
        for tid, t in temoins.items():
            ids = sorted(set(f"{a.lower()} n° {b}" for a, b in ID_CATALOGUE.findall(t["contenu"]["plus_proche_voisin"] + " "
                                                                             + t["contenu"]["ce_qui_distingue"])))
            cites[tid] = ids
            absents += [f"{tid}:{i}" for i in ids if i not in regroupements]
        sortie.update(matiere_sha256=hashlib.sha256(matiere).hexdigest(), identifiants_cites=cites,
                      identifiants_absents_de_la_matiere=absents)
    return sortie


# --- hors ligne -----------------------------------------------------------------------------------------------------------------


def hors_ligne(sortie: Path, matiere: Path | None, orchestrateur: Path) -> dict:
    import numpy as np
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    sortie.mkdir(parents=True)
    o = charger_orchestrateur(orchestrateur)
    conf = json.loads(CONFIGURATION.read_text(encoding="utf-8"))
    brut = json.loads(TEMOINS.read_text(encoding="utf-8"))
    items = list(conf["items_juge"])
    if brut["items"] != items:
        raise SystemExit("témoins : items différents de ceux de la configuration")
    temoins = {t["id"]: t for t in brut["temoins"]}
    interdites = list(conf["etiquettes_interdites_fixes"])
    cj, ca = CONSIGNE_JUGE.read_text(encoding="utf-8"), CONSIGNE_AIGUILLEUR.read_text(encoding="utf-8")
    statiques = controles_statiques(temoins, items, CONSIGNE_PROPOSEUR.read_text(encoding="utf-8"),
                                    matiere.read_bytes() if matiere else None)
    mediane = statistics.median(statiques["longueurs"].values())
    appels = sortie / "appels"
    ss = np.random.SeedSequence(RACINE_GRAINES)
    graines = ss.spawn(N_JUGES_AU_HASARD)
    juges = {"parfait": JugeFactice("parfait", temoins, items), "longueur": JugeFactice("longueur", temoins, items, mediane=mediane),
             "indulgent": JugeFactice("indulgent", temoins, items), "severe": JugeFactice("severe", temoins, items),
             "champ": JugeFactice("champ", temoins, items)}
    lectures = {}
    for nom, j in juges.items():
        lus, _, _ = jouer(o, j, nom, "factice", cj, temoins, items, interdites, appels, 0.6)
        a, _, _ = jouer(o, AiguilleurFactice("niveau_methode"), "aiguilleur", "factice", ca, temoins, items, interdites, appels / nom, 0.25, juge=False)
        lectures[nom] = lire_epreuve({nom: lus}, a, temoins, items)
    reussites_hasard = 0
    for k, g in enumerate(graines):
        lus, _, _ = jouer(o, JugeFactice("hasard", temoins, items, graine=g), f"hasard-{k}", "factice", cj, temoins, items,
                          interdites, appels / "hasard", 0.6) if k < 3 else (None, None, None)
        if lus is None:  # au-delà des trois premiers, sans écrire de dossier : même tirage, lecture directe
            rng = np.random.default_rng(g)
            lus = {}
            for tid in sorted(temoins):
                its = {kk: bool(rng.integers(0, 2)) for kk in items}
                lus[tid] = {"items": its, "notable": all(its.values()), "x": sum(its.values()) / len(items)}
        a = {tid: "niveau_methode" for tid in temoins}
        reussites_hasard += lire_epreuve({"h": lus}, a, temoins, items)["verdict"] == "réussie"
    a_art, _, _ = jouer(o, AiguilleurFactice("concret"), "aiguilleur-artefact", "factice", ca, temoins, items, interdites, appels, 0.25,
                        juge=False)
    lus_parfait, _, _ = jouer(o, juges["parfait"], "parfait-bis", "factice", cj, temoins, items, interdites, appels, 0.6)
    artefact_aiguilleur = lire_epreuve({"parfait": lus_parfait}, a_art, temoins, items)
    n_bons = statiques["classes"]["bon"]
    n_mauvais = statiques["classes"]["mauvais"]
    p_hasard = (0.5 ** len(items)) ** n_bons * 0.5 ** n_mauvais
    separe = (lectures["parfait"]["verdict"] == "réussie" and all(lectures[n]["verdict"] == "échouée" for n in ("longueur", "indulgent", "severe", "champ"))
              and reussites_hasard == 0 and artefact_aiguilleur["verdict"] == "échouée")
    temoins_conformes = (statiques["bornes_tenues"] and statiques["regle_de_seuil_sur_la_longueur_erreurs_min"] >= 1
                         and statiques["regle_de_seuil_sur_le_champ_lu_erreurs_min"] >= 1
                         and statiques["champs_identiques"] and not statiques["titres_de_temoin_dans_la_consigne_servie"]
                         and statiques["items_plantes_tous_couverts"]
                         and not statiques.get("identifiants_absents_de_la_matiere", []))
    rapport = {"version": VERSION, "moteur": "hors_ligne (juges factices, aucun appel)",
               "empreintes": {"temoins": sha256_fichier(TEMOINS), "consigne_juge": sha256_fichier(CONSIGNE_JUGE),
                              "consigne_aiguilleur": sha256_fichier(CONSIGNE_AIGUILLEUR), "programme": sha256_fichier(Path(__file__)),
                              "configuration": sha256_fichier(CONFIGURATION), "consigne_proposeur": sha256_fichier(CONSIGNE_PROPOSEUR)},
               "orchestrateur": str(orchestrateur), "graines": {"racine": RACINE_GRAINES, "juges_au_hasard": N_JUGES_AU_HASARD,
                                                               "regle": "numpy.random.SeedSequence(racine).spawn(n)"},
               "controles_statiques": statiques, "lectures": lectures, "juges_au_hasard_reussis": reussites_hasard,
               "probabilite_exacte_qu_un_juge_au_hasard_reussisse": p_hasard,
               "artefact_aiguilleur_tout_concret": artefact_aiguilleur["verdict"],
               "mediane_des_longueurs": mediane,
               "limite": ("plancher de lecture de forme seulement : chaque mauvais témoin déclare son défaut en toutes lettres ; "
                          "le juge ne voit pas le catalogue ; l'épreuve ne mesure pas le pouvoir de discrimination d'un juge sur des "
                          "défauts non déclarés, ni l'existence d'un identifiant (constat 4)"),
               "conclusion": {"temoins_separent_le_juge_parfait": separe, "temoins_conformes": temoins_conformes,
                              "verdict": "témoins éprouvés hors ligne" if (separe and temoins_conformes) else "témoins à reprendre"}}
    h = ecrire_scelle(sortie / "epreuve-temoins-hors-ligne.json", rapport)
    print(json.dumps({"rapport": str(sortie / "epreuve-temoins-hors-ligne.json"), "sha256": h, **rapport["conclusion"],
                      "juges_au_hasard_reussis": reussites_hasard}, ensure_ascii=False))
    return rapport


# --- v3 : dossiers d'appel sous un chemin interdit en lecture, garde avant tout appel ---------------------------------------------


def dossier_des_appels(sortie: Path) -> Path:
    """v3 : racine des dossiers d'appel = `sortie/"sortie"/"appels"`, sous la sortie interdite en lecture remise aux
    adaptateurs réels (chemin réel, comme `adaptateurs_reels_v56` le calcule pour sa liste interdite)."""
    return Path(os.path.realpath(os.path.abspath(str(sortie / "sortie")))) / "appels"


def _sous(chemin: str, racine: str) -> bool:
    chemin, racine = os.path.realpath(chemin), os.path.realpath(racine)
    return chemin == racine or chemin.startswith(racine.rstrip(os.sep) + os.sep)


def verifier_dossiers_d_appel(adaptateurs: dict, plan: list, temoins: dict, appels: Path, refus=RuntimeError) -> dict:
    """v3, garde avant tout appel (aucun appel, aucune écriture) : pour chaque rôle du plan servi par un adaptateur du kit
    (`AdaptateurClaudeSDK`), `construire_options` de l'orchestrateur épinglé est jouée sur le dossier exact de chaque appel
    (`appels/<étiquette>/<témoin>`, comme `jouer`), avec la liste interdite de l'adaptateur et le rôle que `jouer` passe ;
    puis chaque **autre** dossier du plan (fiche voisine, autre rôle) doit être sous un chemin de `denyRead` et hors de
    `allowRead`. Tout écart lève `refus`. Rôles des autres adaptateurs : « sans objet » (aucun bac du kit). Rend le contrôle."""
    from pole.adaptateurs import AdaptateurClaudeSDK, construire_options
    tous = {(e, tid): os.path.abspath(str(appels / e / tid)) for e, _r, _c, _p, _j in plan for tid in sorted(temoins)}
    controle = {}
    for etiquette, role, _consigne, plafond_session, _juge in plan:
        ad = adaptateurs[role["fournisseur"]]
        if not isinstance(ad, AdaptateurClaudeSDK):
            controle[etiquette] = {"fournisseur": role["fournisseur"], "adaptateur": type(ad).__name__,
                                   "controle": "sans objet : aucun bac du kit (commande externe : dossier courant seulement, consigne "
                                               "sur l'entrée standard, aucun outil de lecture)"}
            continue
        refus_lus = None
        for tid in sorted(temoins):
            d = tous[(etiquette, tid)]
            try:
                o = construire_options(d, float(plafond_session), 1, url_relais=ad.url_relais, modele=role["modele"],
                                       role="juge_ideation", interdire_lecture=ad.interdire_lecture)
            except ValueError as e:
                raise refus(f"dossier d'appel {etiquette}/{tid} refusé par la garde de l'orchestrateur avant tout appel : {e}") from None
            fs = o["sandbox"]["filesystem"]
            if [os.path.normpath(x) for x in fs["allowRead"]] != [os.path.normpath(d)]:
                raise refus(f"dossier d'appel {etiquette}/{tid} : lecture rouverte ailleurs que sur son seul dossier ({fs['allowRead']})")
            lisibles = sorted(f"{e}/{t}" for (e, t), autre in tous.items() if autre != d and (
                not any(_sous(autre, x) for x in fs["denyRead"]) or any(_sous(autre, x) for x in fs["allowRead"])))
            if lisibles:
                raise refus(f"dossier d'appel {etiquette}/{tid} : dossiers voisins lisibles {lisibles[:5]}")
            refus_lus = list(fs["denyRead"])
        controle[etiquette] = {"fournisseur": role["fournisseur"], "adaptateur": type(ad).__name__, "dossiers": len(temoins),
                               "deny_read": refus_lus, "voisins_interdits": len(tous) - 1,
                               "controle": "construire_options jouée sur chaque dossier d'appel : acceptée ; voisins interdits"}
    return controle


def preparer_appels(v8, fournisseurs: dict, sortie: Path, base_sessions: str, plan: list, temoins: dict,
                    refus=RuntimeError) -> tuple:
    """v3 : adaptateurs réels et portes de l'orchestrateur épinglé (`adaptateurs_reels_v56`, liste interdite
    `[base des sessions, sortie/"sortie"]`), racine des dossiers d'appel **sous** `sortie/"sortie"`, puis la garde
    `verifier_dossiers_d_appel`. Aucun appel, aucune transmission de plafond. Rend (adaptateurs, portes, appels, contrôle)."""
    adaptateurs, portes = v8.adaptateurs_reels_v56({"fournisseurs": fournisseurs}, str(sortie / "sortie"), base_sessions)
    appels = dossier_des_appels(sortie)
    controle = verifier_dossiers_d_appel(adaptateurs, plan, temoins, appels, refus)
    return adaptateurs, portes, appels, controle


# --- v4 : sonde du bac, borne du relais d'Argon, manques techniques -------------------------------------------------------------


def exiger_bac_a_sable(L, r, orchestrateur: Path, env: dict) -> dict:
    """v4 (1) : sonde le bac à sable comme le lanceur (`sonder_bac_a_sable` : `etat_bac_a_sable_detaille` de l'orchestrateur
    épinglé, sous-processus `-I -B`), puis exige ici, quel que soit le réglage `r.exiger_bac_a_sable`, `actif` et `proc_neuf`
    vrais. Aucun appel à un fournisseur ; refus (`L.Refus`) sinon."""
    etat = L.sonder_bac_a_sable(r, Path(orchestrateur), env)
    if not (etat.get("actif") is True and etat.get("proc_neuf") is True):
        raise L.Refus("bac à sable inactif ou sans /proc neuf (sonde de l'orchestrateur) : aucun appel — " + str(etat.get("motif")))
    return etat


def environnement_de_sonde(environ) -> dict:
    """Environnement de la sonde : noms permis seulement (aucun nom de clé ; `reel()` a déjà refusé tout nom de clé)."""
    return {n: environ[n] for n in ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR", "HOME") if n in environ}


def verifier_borne_argon(procedure: dict, requis: int, refus=RuntimeError) -> dict:
    """v4 (2) : relit, dans le contrôle des relais rendu par `verifier_procedure_relais`, la borne du relais d'Argon lue par PID
    (`--max-appels`) et par `/relais/etat` (`max_appels`) ; chacune doit valoir au moins `requis` (= 2 × appels d'Argon du plan
    + marge) et l'état doit être neuf (0 appel). Rend {max_appels_args, max_appels_etat, requis}."""
    a = ((procedure or {}).get("relais_vivants") or {}).get("argon") or {}
    args, etat = a.get("max_appels"), (a.get("etat") or {})
    lu_etat = etat.get("max_appels")
    for nom, v in (("arguments (--max-appels)", args), ("état (/relais/etat)", lu_etat)):
        if isinstance(v, bool) or not isinstance(v, int):
            raise refus(f"relais argon : borne illisible dans les {nom} ({v!r}) — aucun appel")
        if v < requis:
            raise refus(f"relais argon : borne {v} dans les {nom} < {requis} appels de relais requis (2 par jugement d'Argon : "
                        "countTokens puis generateContent, plus la marge) — aucun appel")
    if etat.get("appels") != 0:
        raise refus(f"relais argon : relais non neuf ({etat.get('appels')!r} appel(s) déjà comptés) — aucun appel")
    return {"max_appels_args": args, "max_appels_etat": lu_etat, "requis": requis}


def _motif_court(erreur, L=None) -> str:
    texte = str(erreur or "")[:240]
    if L is not None:
        texte = L.MOTIF_VALEUR_DE_CLE.sub("[valeur masquée]", texte)
    return texte


def jouer_avec_incidents(o: dict, adaptateur, etiquette: str, modele: str, consigne: str, temoins: dict, items: list,
                         interdites: list, dossier: Path, plafond_session: float, juge: bool = True, L=None) -> tuple:
    """v4 : `jouer` (inchangée, à l'octet) plus le statut de chaque appel. Rend ({id: lu}, coût, modèles servis,
    {id: statut}, {id: {statut, erreur}} pour les appels au statut technique (`STATUTS_TECHNIQUES`)). Mêmes appels, même ordre,
    même dossier, même lecture que `jouer`."""
    lus, cout, servis, statuts, incidents = {}, 0.0, set(), {}, {}
    for tid in sorted(temoins):
        entree = servir(o, consigne, temoins[tid], interdites, identifiant_servi(etiquette, tid) if juge else None)
        d = dossier / etiquette / tid
        d.mkdir(parents=True, exist_ok=True)
        r = adaptateur.lancer("juge_ideation", entree, str(d), plafond_session, 1, modele=modele)
        cout += float(r.cout_declare_usd or 0.0)
        if r.statut == "ok" and r.modele_servi:
            servis.add(r.modele_servi)
        texte = r.texte_brut or r.texte_final if r.statut == "ok" else None
        lus[tid] = (o["lire_verdict"](texte, items) if juge else o["lire_classe"](texte)[0]) if texte else None
        statuts[tid] = str(r.statut)
        if r.statut in STATUTS_TECHNIQUES:
            incidents[tid] = {"statut": str(r.statut), "erreur": _motif_court(getattr(r, "erreur", None), L)}
    return lus, cout, sorted(servis), statuts, incidents


def manques_par_sorte(lecture: dict, incidents: dict) -> dict:
    """Partage les manques de la lecture gelée : « techniques » (réponse absente ET appel au statut technique ou non parti,
    consigné dans `incidents` {rôle: {témoin: …}}) ; « autres » (tout le reste : verdict lu et faux, réponse lue illisible,
    refus du modèle, budget ou tours épuisés)."""
    techniques, autres = [], []
    roles = [(j, x["manques"]) for j, x in sorted((lecture.get("par_juge") or {}).items())] + \
        [("aiguilleur", (lecture.get("aiguilleur") or {}).get("manques") or [])]
    for role, manques in roles:
        for m in manques:
            absent = m.get("motif") in ("verdict illisible ou absent", "classe illisible ou absente")
            if absent and m.get("temoin") in ((incidents or {}).get(role) or {}):
                techniques.append(f"{role}/{m['temoin']}")
            else:
                autres.append(f"{role}/{m['temoin']}")
    return {"techniques": techniques, "autres": autres}


def qualifier_verdict(lecture: dict, incidents: dict, motif_arret, changes: list, juges_complets: bool) -> str:
    """v4 (3) : verdict écrit. Règles du v3 d'abord (arrêt, version servie changée, juge manquant → « non conclue ») ; puis,
    si la lecture gelée rend « échouée » et que **tous** ses manques sont techniques → « non conclue ». Ne rend jamais
    « réussie » si `lire_epreuve` ne l'a pas rendu."""
    if motif_arret or changes or not juges_complets:
        return "non conclue"
    v = lecture["verdict"]
    if v == "échouée":
        sortes = manques_par_sorte(lecture, incidents)
        if sortes["techniques"] and not sortes["autres"]:
            return "non conclue"
    return v


def refuser_si_rapport_existe(refus=RuntimeError) -> None:
    """v5 : une seule épreuve à ce chemin (tentative neuve) — refus avant tout s'il existe déjà (ou son compagnon)."""
    if RAPPORT_REEL.exists() or Path(str(RAPPORT_REEL) + ".sha256").exists():
        raise refus(f"{RAPPORT_REEL} existe déjà : l'épreuve v5 a déjà été jouée (R12 : version neuve et mot de la mère)")


def verifier_mot_de_reprise(texte_registre: str, aujourd_hui, refus=RuntimeError) -> dict:
    """v4 : la décision de reprise (`GO-2026-11-18-36`) figure au registre des GO lu au commit de `main` : une seule ligne,
    type « décision », accordée par Lazar, période de validité couvrant aujourd'hui, périmètre qui dit « reprise » et
    « témoins ». Rend {id, accorde, echeance, ligne_sha256}."""
    lignes = [l for l in texte_registre.splitlines() if re.match(r"^\|\s*" + re.escape(GO_REPRISE) + r"\s*\|", l)]
    if len(lignes) != 1:
        raise refus(f"{GO_REPRISE} : {len(lignes)} ligne(s) au registre (une exigée) — aucune reprise sans la décision de Lazar")
    c = [x.strip() for x in lignes[0].strip().strip("|").split("|")]
    if len(c) != 8:
        raise refus(f"{GO_REPRISE} : ligne mal formée ({len(c)} colonnes, 8 attendues)")
    ident, accorde, typ, perimetre, _plafond, echeance, par, _ref = c
    if typ != "décision" or par != "Lazar":
        raise refus(f"{GO_REPRISE} : type {typ!r} et accordé par {par!r} (« décision », Lazar exigés)")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise refus(f"{GO_REPRISE} : dates illisibles") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise refus(f"{GO_REPRISE} hors de sa période ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui}) — aucune reprise")
    p = perimetre.lower()
    if "reprise" not in p or "témoins" not in p:
        raise refus(f"{GO_REPRISE} : périmètre sans « reprise » ni « témoins » — ce n'est pas la décision attendue")
    return {"id": ident, "accorde": accorde, "echeance": echeance,
            "ligne_sha256": hashlib.sha256("|".join(c).encode("utf-8")).hexdigest()}


def depense_tentative_v3(refus=RuntimeError) -> float:
    """v4 : dépense de la tentative v3, lue dans son rapport scellé à l'empreinte épinglée (jamais une valeur écrite à la main)."""
    if not RAPPORT_TENTATIVE_V3.is_file() or sha256_fichier(RAPPORT_TENTATIVE_V3) != SHA_TENTATIVE_V3:
        raise refus(f"rapport de la tentative v3 absent ou d'une autre empreinte que {SHA_TENTATIVE_V3}")
    compagnon = Path(str(RAPPORT_TENTATIVE_V3) + ".sha256")
    if not compagnon.is_file() or compagnon.read_text(encoding="utf-8").split()[0] != SHA_TENTATIVE_V3:
        raise refus("rapport de la tentative v3 non scellé")
    v = json.loads(RAPPORT_TENTATIVE_V3.read_text(encoding="utf-8")).get("cout_usd")
    if isinstance(v, bool) or not isinstance(v, (int, float)) or v < 0:
        raise refus(f"dépense de la tentative v3 illisible ({v!r})")
    return float(v)


def budget_de_la_reprise(plafond_total: float, depense_anterieure: float, refus=RuntimeError) -> float:
    """v4 : budget de la reprise = plafond total (5 USD, inchangé) − dépense de la tentative v3 ; > 0 exigé."""
    b = round(float(plafond_total) - float(depense_anterieure), 6)
    if b <= 0:
        raise refus(f"plafond de l'épreuve ({plafond_total} USD au total) déjà dépensé par la tentative v3")
    return b


def tentative_precedente() -> dict:
    """La tentative v3 (scellée) : chemin, empreinte, verdict écrit, coût, et ses verdicts bruts du juge Argon, rapportés à
    côté de ceux de la reprise (jamais masqués)."""
    if not RAPPORT_TENTATIVE_V3.is_file():
        return {"chemin": str(RAPPORT_TENTATIVE_V3), "present": False}
    o = json.loads(RAPPORT_TENTATIVE_V3.read_text(encoding="utf-8"))
    return {"chemin": str(RAPPORT_TENTATIVE_V3), "present": True, "sha256": sha256_fichier(RAPPORT_TENTATIVE_V3),
            "verdict_ecrit": o.get("verdict"), "cout_usd": o.get("cout_usd"), "verdicts": o.get("verdicts"),
            "classes": o.get("classes")}


# --- v5 : tentative neuve (les fonctions de reprise de la v4 ci-dessus sont gardées à l'octet, sans emploi par `reel`) ------------


def _resume_tentative(chemin: Path, sha_epingle: str) -> dict:
    """Une tentative précédente, scellée : chemin, empreinte (vérifiée contre l'épinglée), verdict écrit, coût, ligne de GO,
    horodatage, verdicts et classes bruts. Absente ou d'une autre empreinte : dit tel quel (jamais un repli silencieux)."""
    if not chemin.is_file():
        return {"chemin": str(chemin), "present": False}
    lu = sha256_fichier(chemin)
    if lu != sha_epingle:
        return {"chemin": str(chemin), "present": True, "sha256": lu, "sha256_epingle": sha_epingle, "conforme": False}
    o = json.loads(chemin.read_text(encoding="utf-8"))
    return {"chemin": str(chemin), "present": True, "sha256": lu, "conforme": True, "verdict_ecrit": o.get("verdict"),
            "cout_usd": o.get("cout_usd"), "go": (o.get("go") or {}).get("id"), "horodatage_utc": o.get("horodatage_utc"),
            "verdicts": o.get("verdicts"), "classes": o.get("classes")}


def tentatives_precedentes() -> list:
    """v5 : les épreuves réelles v3 et v4, rapportées à côté de celle-ci (elles ne comptent pas dans son verdict)."""
    return [dict(_resume_tentative(RAPPORT_TENTATIVE_V3, SHA_TENTATIVE_V3), version="v3"),
            dict(_resume_tentative(RAPPORT_TENTATIVE_V4, SHA_TENTATIVE_V4), version="v4")]


# --- réel (session d'exécution seulement) ---------------------------------------------------------------------------------------


def reel() -> dict:
    """Jamais lancé par l'auteur. Ordre : environnement sans nom de clé ; pièce de départ ; ligne de GO de l'épreuve
    (lue au commit de main) ; pièces épinglées par le lanceur (ce programme compris) ; orchestrateur épinglé ; déclaration des
    relais de l'épreuve (Claude et Argon seulement) ; relais vivants par PID et porte à blanc ; v3 : adaptateurs réels et garde
    des dossiers d'appel (`preparer_appels`, avant la transmission des plafonds) ; puis les appels, sous le plafond de 5 USD
    (chaque appel n'est lancé que si le cumul plus son plafond de session tient dessous)."""
    L = charger_lanceur()
    presents = sorted(n for n in os.environ if n in L.NOMS_DE_CLE or L.MOTIF_NOM_DE_CLE.search(n))
    if presents:
        raise L.Refus(f"variables de clé dans l'environnement de l'épreuve ({presents}) : la clé reste dans son relais")
    refuser_si_rapport_existe(L.Refus)                                       # v5 : une seule épreuve à ce chemin
    r = L.Reglages.production()
    r.declaration = DECLARATION_EPREUVE
    aujourd_hui = _dt.datetime.now(_dt.timezone.utc).date()
    depart = L.verifier_piece_de_depart(r)                                   # v5 : lignes consommées par la v4 refusées
    registre = L.lire_registre(r)
    go = L.verifier_go(registre["texte"], aujourd_hui, depart["go_epreuve"], PLAFOND_EPREUVE_USD, ("temoins",))
    # v5 : mot de reprise (ligne de GO de la course neuve, « tentative neuve ») ; plafond de 5 USD entier, ligne neuve
    mot_de_reprise = L.verifier_mot_de_reprise(registre["texte"], aujourd_hui, depart)
    depense_v3 = 0.0                                                         # v5 : ligne neuve, rien n'y a été dépensé
    budget = PLAFOND_EPREUVE_USD
    pieces = L.verifier_pieces(r)
    if pieces["epreuve_temoins"]["sha256"] != sha256_fichier(Path(__file__)):
        raise L.Refus("ce programme n'est pas celui que le lanceur épingle")
    orch = L.verifier_orchestrateur(r)
    # v4 (1) : bac à sable sondé avant tout appel, toute porte et toute transmission de plafond
    bac = exiger_bac_a_sable(L, r, Path(orch["chemin"]), environnement_de_sonde(os.environ))
    fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
    decl_brute, decl_sha = L.lire_json_scelle(DECLARATION_EPREUVE, "déclaration des relais de l'épreuve")
    if sorted(decl_brute.get("fournisseurs") or {}) != ["argon", "claude"]:
        raise L.Refus("déclaration de l'épreuve : claude et argon seulement (juges et aiguilleur de la configuration)")
    decl = L.verifier_declaration(decl_brute, fixe, depart)
    n_argon = len(json.loads(TEMOINS.read_text(encoding="utf-8"))["temoins"]) * sum(1 for j in fixe["juges"] if j["fournisseur"] == "argon")
    # v4 (2) : deux appels de relais par jugement d'Argon (countTokens puis generateContent), plus la marge
    requis_argon = L.appels_relais_gemini_requis(n_argon)
    procedure = L.verifier_procedure_relais(r, decl, pieces, fixe, requis_argon, plafond_ligne=PLAFOND_EPREUVE_USD)
    borne_argon = verifier_borne_argon(procedure, requis_argon, L.Refus)
    portes_a_blanc = L.porte_a_blanc(decl)
    sortie = Path(tempfile.mkdtemp(prefix="epreuve-temoins-auto-conception-"))
    arrets = sortie / "arrets-credit"
    arrets.mkdir()
    decl = L.envelopper_commandes(decl, sys.executable, Path(pieces["garde_credit"]["absolu"]), arrets)
    o = charger_orchestrateur(Path(orch["chemin"]))
    spec = importlib.util.spec_from_file_location("ideation_v8_pour_epreuve", Path(orch["chemin"]) / L.LANCEUR_ORCHESTRATEUR)
    v8 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v8)
    brut = json.loads(TEMOINS.read_text(encoding="utf-8"))
    items, temoins = list(fixe["items_juge"]), {t["id"]: t for t in brut["temoins"]}
    interdites = list(fixe["etiquettes_interdites_fixes"])
    ps = fixe["plafonds_session"]
    cj, ca = Path(pieces["consigne_juge"]["absolu"]).read_text(encoding="utf-8"), Path(pieces["consigne_aiguilleur"]["absolu"]).read_text(encoding="utf-8")
    cumul, verdicts, servis, motif_arret = 0.0, {}, {}, None
    statuts, incidents = {}, {}                                              # v4
    plan = [("aiguilleur", fixe["aiguilleur"], ca, float(ps["aiguilleur"]), False)] + \
        [(j["etiquette"], j, cj, float(ps["juge"]), True) for j in fixe["juges"]]
    base_sessions = tempfile.mkdtemp(prefix="pole-sessions-epreuve-")
    # v3 : dossiers d'appel sous la sortie interdite en lecture, garde avant tout appel et avant la transmission des plafonds
    adaptateurs, portes, appels, dossiers_d_appel = preparer_appels(v8, decl["fournisseurs"], sortie, base_sessions, plan, temoins,
                                                                    refus=L.Refus)
    accuses = {nom: p.transmettre(ETAPE, budget) for nom, p in sorted(portes.items())}         # v4 : budget de la reprise
    classes = {}
    for etiquette, role, consigne, plafond_session, juge in plan:
        lus = {}
        for tid in sorted(temoins):
            if cumul + plafond_session > budget + 1e-9:                     # v5 : 5 USD, ligne neuve
                motif_arret = (f"plafond de l'épreuve ({PLAFOND_EPREUVE_USD} USD, ligne {depart['go_epreuve']}) : appel suivant "
                               "non lancé")
                break
            if any(x.name.startswith("arret-credit-") for x in arrets.iterdir()):
                motif_arret = "refus pour crédit d'un relais au solde illisible"
                break
            un, c, s, st, inc = jouer_avec_incidents(o, adaptateurs[role["fournisseur"]], etiquette, role["modele"], consigne,
                                                    {tid: temoins[tid]}, items, interdites, appels, plafond_session, juge=juge,
                                                    L=L)
            cumul += c
            lus.update(un)
            servis.setdefault(etiquette, set()).update(s)
            statuts.setdefault(etiquette, {}).update(st)
            if inc:
                incidents.setdefault(etiquette, {}).update(inc)
        if juge:
            verdicts[etiquette] = lus
        else:
            classes = lus
        if motif_arret:
            break
    lecture = lire_epreuve(verdicts, classes, temoins, items)
    changes = sorted(e for e, s in servis.items() if len(s) > 1)
    # v4 (3) : appels non partis = manques techniques ; verdict qualifié sans toucher à la lecture gelée
    for etiquette, _role, _c, _p, _j in plan:
        for tid in sorted(temoins):
            if tid not in statuts.get(etiquette, {}):
                incidents.setdefault(etiquette, {})[tid] = {"statut": "non parti", "erreur": MOTIF_NON_PARTI}
    verdict_lecture_gelee = lecture["verdict"]
    lecture["verdict"] = qualifier_verdict(lecture, incidents, motif_arret, changes, len(verdicts) == len(fixe["juges"]))
    rapport = {"version": VERSION, "moteur": "reel", "verdict": lecture["verdict"], "lecture": lecture, "motif_arret": motif_arret,
               "verdicts": verdicts, "classes": classes,
               "verdict_lecture_gelee": verdict_lecture_gelee, "statuts_par_appel": statuts, "incidents_techniques": incidents,
               "manques_par_sorte": manques_par_sorte(lecture, incidents), "bac_a_sable": bac, "borne_relais_argon": borne_argon,
               "tentatives_precedentes": tentatives_precedentes(), "mot_de_reprise": mot_de_reprise,
               "plafond_total_usd": PLAFOND_EPREUVE_USD, "depense_anterieure_sous_la_ligne_usd": depense_v3,
               "budget_epreuve_usd": budget,
               "modeles_servis": {e: sorted(s) for e, s in servis.items()}, "version_servie_changee": changes,
               "horodatage_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(), "go": go,
               "registre": {"commit": registre["commit"], "sha256": registre["sha256"]},
               "piece_de_depart": {"chemin": depart["chemin"], "sha256": depart["sha256"]},
               "empreintes": {"temoins": pieces["temoins"]["sha256"], "consigne_juge": pieces["consigne_juge"]["sha256"],
                              "consigne_aiguilleur": pieces["consigne_aiguilleur"]["sha256"], "programme": sha256_fichier(Path(__file__)),
                              "lanceur": sha256_fichier(LANCEUR), "orchestrateur_commit": orch["commit"]},
               "juges": [[j["etiquette"], j["modele"]] for j in fixe["juges"]],
               "aiguilleur": [fixe["aiguilleur"]["etiquette"], fixe["aiguilleur"]["modele"]],
               "declaration": {"chemin": str(DECLARATION_EPREUVE), "sha256": decl_sha}, "procedure": procedure,
               "porte_a_blanc": portes_a_blanc, "accuses_de_plafond": accuses, "cout_usd": round(cumul, 6),
               "plafond_usd": PLAFOND_EPREUVE_USD, "sortie_hors_depot": str(sortie),
               "dossiers_d_appel": {"racine": str(appels), "controle_avant_appel": dossiers_d_appel}}
    h = ecrire_scelle(RAPPORT_REEL, rapport)
    print(json.dumps({"rapport": str(RAPPORT_REEL), "sha256": h, "verdict": rapport["verdict"], "cout_usd": rapport["cout_usd"]},
                     ensure_ascii=False))
    return rapport


def principal(argv: list | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) in (2, 4) and argv[0] == "--hors-ligne" and (len(argv) == 2 or argv[2] == "--matiere"):
        L = charger_lanceur()
        hors_ligne(Path(argv[1]).resolve(), Path(argv[3]).resolve() if len(argv) == 4 else None,
                   orchestrateur_present(L.ORCHESTRATEURS_CANDIDATS))
        return 0
    if argv == ["--reel"]:
        L = charger_lanceur()
        try:
            reel()
        except L.Refus as e:
            print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
            return 2
        return 0
    print("usage : --hors-ligne SORTIE_NEUVE [--matiere MATIERE.md] | --reel", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(principal())
