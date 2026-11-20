#!/usr/bin/env python3
"""Étalonnage de l'étage 2 à 200 témoins — ligne 3 de l'organisme v9 (votes effectifs des juges croisés) — v1.

Plan de code : annexe A du texte v7 (`preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, 4e3680d9…), ligne 562
(`etalonner_ligne_3_v1.py`, puis `lire_ligne_3_v1.py`) ; « Lecture unique » (l. 297) : « Le programme d'étalonnage lit la
moitié « étalonnage », écrit et scelle les poids, le seuil et ρ d'étalonnage. » ; ordre des gestes, l. 305 (9). Tailles à
200 : additif 3 v3 (71b7a876…, § 4.2). Verdict « portée à 200 » v2 (02928723…) : issue B (sans effet sur l'étalonnage).

Ce que fait ce programme, et rien d'autre :
- il lit la banque scellée (format du générateur v3 et du code d'appel v4 : `{"temoins": [{identifiant_interne, classe,
  item, niveau, citation, moitie, contenu}]}`) et **le seul fichier des verdicts de la moitié « étalonnage »** déposé par le
  code d'appel v4 (`verdicts-moitie-etalonnage-execution-K.json`, scellé) ; il refuse, par un refus nommé, un fichier de la
  moitié « lecture » (par son nom, avant toute ouverture) et toute ligne d'un témoin de la moitié « lecture » (par son
  contenu, avant tout usage) ; il n'ouvre aucun autre fichier du dépôt des verdicts ;
- sur les témoins de la moitié « étalonnage » dont les deux premiers rendus (bloc A) ont été tentés, il calcule, **par les
  fonctions du banc de l'étage 1 v4** (`banc_juges_scriptes_ligne_3_v4.py`, 79865552…, importé après vérification de son
  empreinte, compilé depuis les octets vérifiés ; aucune fonction réécrite) : les poids et le seuil du bras C
  (`poids_covariance`, `seuil_milieu`), ceux du bras P (`poids_precision`), la règle que chacun rend à deux juges
  (`regle_choisie` ; arrêt si elle n'est pas l'une des cinq), et ρ d'étalonnage (`cov_intra_classes`, `rho_moyenne`) ;
- il écrit et scelle (compagnon `.sha256`) la pièce d'étalonnage et un manifeste (règle R9).

Un verdict absent (illisible, refus) n'est jamais « notable » : il compte comme rejet (texte, « Métrique »). Aucun tirage :
aucune graine n'est dérivée. Aucun appel de modèle, aucun réseau.

Usage (après le dépôt scellé des verdicts ; jamais lancé par l'auteur sur de vrais verdicts) :
    python3 -I -B etalonner_ligne_3_v1.py --banque BANQUE.json --banque-sha HEX \
        --verdicts-etalonnage DEPOT/verdicts-moitie-etalonnage-execution-K.json --verdicts-etalonnage-sha HEX \
        --dossier DOSSIER_DE_LA_LECTURE
Écrit DOSSIER_DE_LA_LECTURE/etalonnage/ (refus s'il existe). Codes : 0 pièce écrite ; 2 refus.

Développeur, modèle O.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
import types
from pathlib import Path

VERSION = "etalonner_ligne_3_v1"

# --- pièces épinglées ---------------------------------------------------------------------------------------------------
DEPOT = Path("/home/user/controle-ia-travail")
L3 = DEPOT / "docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges"
BANC_V4 = (L3 / "code-portee-200-v4" / "banc_juges_scriptes_ligne_3_v4.py",
           "79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7")
MODULE_BANC = "_banc_v4_ligne_3_etage_2_etalonnage_lecture"
TEXTE_V7_SHA256 = "4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0"
ADDITIF_3_V3_SHA256 = "71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807"
VERDICT_PORTEE_200_V2_SHA256 = "029287239e341e53755b2875aaefd7a75662a1e9e95b5dbe2e2bf6ab8d6fbaa9"
CODE_APPEL_V4_SHA256 = "082d19d61922dbecd64d64435d8a8682f9e01abee6735ff01c6cc550c8f5484c"
GENERATEUR_V3_SHA256 = "f5de9c3c94be525d1ec48d3e7954135473894a298aafe908475f043934278ae0"

# --- format du dépôt des verdicts (code d'appel v4, `deposer`, l. 1082 à 1133) -------------------------------------------
VERSION_CODE_APPEL = "epreuve_juges_reels_ligne_3_v4"
JUGES = ("juge-opus", "juge-argon")
ITEMS = ("module_nomme", "voisin_nomme", "epreuve_plantee", "aucun_modele_ne_decide", "reserves_tenues")
NIVEAUX = ("declare", "net", "discret")
CLASSES = ("bon", "mauvais")
MOITIES = ("lecture", "etalonnage")
# Colonnes d'un témoin : (juge, rendu, bloc). Bloc A : un rendu de chaque juge ; bloc B : un de plus du juge Opus, deux de
# plus du juge Argon (texte l. 271 ; additif 3, § 4.2).
COLONNES = (("juge-opus", 1, "A"), ("juge-argon", 1, "A"), ("juge-opus", 2, "B"), ("juge-argon", 2, "B"),
            ("juge-argon", 3, "B"))
ETATS = ("obtenu", "absent", "role_arrete", "non_parti")
ETATS_TENTES = ("obtenu", "absent")       # rendu tenté : un verdict, ou un « absent » compté comme rejet
N_TEMOINS = 200                           # additif 3 v3, § 4.2
NOM_VERDICTS = re.compile(r"^verdicts-moitie-(lecture|etalonnage)-execution-([1-9][0-9]*)\.json$")
IDENTIFIANT_INTERNE = re.compile(r"^[A-Za-z0-9._:-]{1,64}$")

# --- garde « verdicts de la v9 » (copie déclarée de la garde du code d'appel v4, `garde_chemins`, l. 303 à 322) ----------
COMPOSANTS_INTERDITS = ("archives-reponses-modeles",)
PREFIXE_COMPOSANT_INTERDIT = "coffre"
RACINES_INTERDITES = (Path("/home/user/sorties-course-auto-conception-v9"),
                      DEPOT / "runs" / "20261119-094145-course-auto-conception-v9")

# --- sorties ------------------------------------------------------------------------------------------------------------
SOUS_DOSSIER = "etalonnage"
FICHIER_PIECE = "etalonnage-etage-2-ligne-3-v1.json"
FICHIER_MANIFESTE = "manifeste-etalonnage-etage-2-ligne-3-v1.json"
PIECE = "étalonnage de l'étage 2, ligne 3 (moitié « étalonnage » seule)"


class Refus(RuntimeError):
    """Refus nommé, avant tout usage : rien n'est écrit."""


# --- fichiers -----------------------------------------------------------------------------------------------------------


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_fichier(chemin) -> str:
    return sha256_octets(Path(chemin).read_bytes())


def json_octets(objet) -> bytes:
    return (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def ecrire_scelle(chemin: Path, objet) -> str:
    """Écrit sans jamais écraser (mode exclusif) et pose le compagnon `.sha256` au format de sha256sum (règle R6)."""
    donnees = json_octets(objet)
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = sha256_octets(donnees)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {Path(chemin).name}\n")
    return h


def est_empreinte(x) -> bool:
    return isinstance(x, str) and re.fullmatch(r"[0-9a-f]{64}", x) is not None


def garde_chemins(chemins) -> list:
    """Refuse, avant toute ouverture, tout chemin du coffre de la course v9 ou de l'archive des réponses (forme écrite
    d'abord, sans appel au système de fichiers, puis chemin réel)."""
    vus = []
    for c in chemins:
        if c is None:
            continue
        ecrit = os.path.normpath(os.path.abspath(str(c)))
        for reel in (False, True):
            s = os.path.realpath(ecrit) if reel else ecrit
            if any(p in COMPOSANTS_INTERDITS or p.lower().startswith(PREFIXE_COMPOSANT_INTERDIT) for p in Path(s).parts):
                raise Refus("verdicts de la v9 : chemin du coffre ou de l'archive des réponses passé au programme : refus")
            for r in RACINES_INTERDITES:
                r = os.path.normpath(str(r))
                if s == r or s.startswith(r + os.sep):
                    raise Refus("verdicts de la v9 : chemin sous la sortie ou le run de la course v9 : refus")
        vus.append(ecrit)
    return vus


def lire_par_empreinte(chemin, attendue: str, quoi: str) -> bytes:
    """Octets lus une fois ; empreinte vérifiée sur ces octets ; compagnon `.sha256` égal (pièce scellée seulement)."""
    if not est_empreinte(attendue):
        raise Refus(f"{quoi} : empreinte attendue (64 caractères hexadécimaux) exigée")
    garde_chemins([chemin])
    try:
        octets = Path(chemin).read_bytes()
    except OSError as e:
        raise Refus(f"{quoi} : absent ou illisible ({type(e).__name__})") from None
    if sha256_octets(octets) != attendue:
        raise Refus(f"{quoi} : empreinte différente de l'empreinte attendue")
    try:
        mots = Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()
    except OSError:
        raise Refus(f"{quoi} : non scellé (compagnon .sha256 absent)") from None
    if not mots or mots[0] != attendue:
        raise Refus(f"{quoi} : compagnon .sha256 différent de l'empreinte attendue")
    return octets


def lire_json_scelle(chemin, attendue: str, quoi: str):
    octets = lire_par_empreinte(chemin, attendue, quoi)
    try:
        return json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise Refus(f"{quoi} : JSON illisible") from None


# --- banc de l'étage 1 v4 : import à empreinte vérifiée ------------------------------------------------------------------


def charger_banc(chemin=None, attendue=None):
    """Le banc v4, vérifié par son empreinte **avant tout import**, puis compilé et exécuté depuis ces octets mêmes sous
    un nom privé. Aucune fonction n'est réécrite ici ; on ne lance ni sa ligne de commande ni aucun de ses tirages."""
    chemin = Path(chemin) if chemin is not None else BANC_V4[0]
    attendue = attendue if attendue is not None else BANC_V4[1]
    if MODULE_BANC in sys.modules:
        m = sys.modules[MODULE_BANC]
        if getattr(m, "__empreinte__", None) != attendue:
            raise Refus("banc v4 : module privé déjà chargé avec une autre empreinte")
        return m
    try:
        octets = chemin.read_bytes()
    except OSError:
        raise Refus("banc v4 : fichier absent ou illisible") from None
    if sha256_octets(octets) != attendue:
        raise Refus("banc v4 : empreinte différente de celle de l'additif 5 (79865552…) : aucun import")
    m = types.ModuleType(MODULE_BANC)
    m.__file__ = str(chemin)
    sys.modules[MODULE_BANC] = m
    try:
        exec(compile(octets, str(chemin), "exec"), m.__dict__)
    except BaseException:
        del sys.modules[MODULE_BANC]
        raise
    m.__empreinte__ = attendue
    return m


# --- banque ---------------------------------------------------------------------------------------------------------------


def valider_banque(objet, n=N_TEMOINS) -> dict:
    """Rend {identifiant: {classe, item, niveau, citation, moitie}} ; la vérité est la construction. Le contenu n'est pas
    gardé."""
    if not isinstance(objet, dict) or not isinstance(objet.get("temoins"), list):
        raise Refus("banque : objet {\"temoins\": [...]} attendu")
    if "items" in objet and list(objet["items"]) != list(ITEMS):
        raise Refus("banque : items différents des cinq items de la consigne")
    sortie = {}
    for k, t in enumerate(objet["temoins"]):
        if not isinstance(t, dict):
            raise Refus(f"banque : témoin {k} non objet")
        for c in ("identifiant_interne", "classe", "item", "niveau", "citation", "moitie"):
            if c not in t:
                raise Refus(f"banque : témoin {k} sans le champ {c}")
        i = t["identifiant_interne"]
        if not isinstance(i, str) or not IDENTIFIANT_INTERNE.match(i) or i in sortie:
            raise Refus(f"banque : témoin {k} : identifiant interne illisible ou répété")
        if t["classe"] not in CLASSES:
            raise Refus(f"banque : {i} : classe hors de {CLASSES}")
        if t["classe"] == "bon" and (t["item"] is not None or t["niveau"] is not None):
            raise Refus(f"banque : {i} : un bon témoin n'a ni item ni niveau")
        if t["classe"] == "mauvais" and (t["item"] not in ITEMS or t["niveau"] not in NIVEAUX):
            raise Refus(f"banque : {i} : un mauvais témoin a un item de la consigne et un niveau")
        if not isinstance(t["citation"], bool):
            raise Refus(f"banque : {i} : citation booléenne attendue")
        if t["moitie"] not in MOITIES:
            raise Refus(f"banque : {i} : moitié hors de {MOITIES}")
        sortie[i] = {"classe": t["classe"], "item": t["item"], "niveau": t["niveau"], "citation": t["citation"],
                     "moitie": t["moitie"]}
    if len(sortie) != n:
        raise Refus(f"banque : {len(sortie)} témoins, {n} attendus")
    for m in MOITIES:
        for c in CLASSES:
            if sum(1 for t in sortie.values() if t["moitie"] == m and t["classe"] == c) != n // 4:
                raise Refus(f"banque : la moitié « {m} » n'a pas {n // 4} témoins de la classe « {c} »")
    return sortie


def lire_banque(chemin, attendue, n=N_TEMOINS) -> dict:
    return valider_banque(lire_json_scelle(chemin, attendue, "banque de témoins"), n)


# --- verdicts d'une moitié ------------------------------------------------------------------------------------------------


def valider_verdict(v, ou: str):
    """Un verdict déposé est None (absent) ou la forme rendue par `lire_verdict` de `juges_croises_v53.py` : items (les
    cinq, booléens), notable = tous vrais. Toute autre forme : refus (aucun repli silencieux)."""
    if v is None:
        return None
    if not isinstance(v, dict) or not isinstance(v.get("items"), dict) or set(v["items"]) != set(ITEMS):
        raise Refus(f"verdicts : {ou} : verdict hors forme (cinq items attendus)")
    if not all(isinstance(v["items"][k], bool) for k in ITEMS) or not isinstance(v.get("notable"), bool):
        raise Refus(f"verdicts : {ou} : verdict hors forme (booléens attendus)")
    if v["notable"] != all(v["items"][k] for k in ITEMS):
        raise Refus(f"verdicts : {ou} : « notable » différent de « tous les items vrais »")
    return {"items": {k: v["items"][k] for k in ITEMS}, "notable": v["notable"]}


def nom_de_verdicts(chemin) -> tuple:
    m = NOM_VERDICTS.match(Path(chemin).name)
    if not m:
        raise Refus("verdicts : nom de fichier hors de la forme du code d'appel v4 "
                    "(verdicts-moitie-<moitié>-execution-<K>.json)")
    return m.group(1), int(m.group(2))


def lire_verdicts_moitie(chemin, attendue, moitie: str, banque: dict) -> dict:
    """Rend {"execution": K, "par_temoin": {témoin: {(juge, rendu): {"etat", "verdict"}}}}.

    Refus nommés : fichier d'une autre moitié (par son nom, **avant toute ouverture**) ; ligne d'un témoin d'une autre
    moitié ou hors de la banque (par son contenu, avant tout usage) ; forme, plan des cinq rendus par témoin, témoins
    manquants."""
    if moitie not in MOITIES:
        raise Refus("verdicts : moitié inconnue")
    m_nom, k = nom_de_verdicts(chemin)
    if m_nom != moitie:
        raise Refus(f"verdicts : fichier de la moitié « {m_nom} » passé pour la moitié « {moitie} » : refus, "
                    "aucune ligne lue")
    objet = lire_json_scelle(chemin, attendue, f"verdicts de la moitié « {moitie} »")
    if not isinstance(objet, dict) or objet.get("version") != VERSION_CODE_APPEL or objet.get("execution") != k \
            or not isinstance(objet.get("rendus"), list):
        raise Refus("verdicts : en-tête hors de la forme du code d'appel v4 (version, exécution, rendus)")
    # Contrôle de moitié sur toutes les lignes avant tout autre usage.
    for x in objet["rendus"]:
        t = x.get("temoin") if isinstance(x, dict) else None
        if t not in banque:
            raise Refus(f"verdicts : ligne d'un témoin hors de la banque : refus")
        if banque[t]["moitie"] != moitie:
            raise Refus(f"verdicts : ligne d'un témoin de la moitié « {banque[t]['moitie']} » dans les verdicts de la "
                        f"moitié « {moitie} » : refus, aucune ligne utilisée")
    attendues = {(j, r): b for j, r, b in COLONNES}
    par_temoin = {}
    for x in objet["rendus"]:
        t = x["temoin"]
        cle = (x.get("juge"), x.get("rendu"))
        if cle not in attendues or x.get("bloc") != attendues[cle]:
            raise Refus(f"verdicts : {t} : rendu hors du plan (juge, rang du rendu, bloc)")
        if x.get("etat") not in ETATS:
            raise Refus(f"verdicts : {t} : état hors de {ETATS}")
        v = valider_verdict(x.get("verdict"), f"{t} {cle}")
        if x["etat"] != "obtenu" and v is not None:
            raise Refus(f"verdicts : {t} {cle} : verdict présent sur un rendu non obtenu")
        d = par_temoin.setdefault(t, {})
        if cle in d:
            raise Refus(f"verdicts : {t} {cle} : rendu en double")
        d[cle] = {"etat": x["etat"], "verdict": v}
    attendus_ids = {t for t, b in banque.items() if b["moitie"] == moitie}
    if set(par_temoin) != attendus_ids:
        raise Refus(f"verdicts : témoins de la moitié « {moitie} » manquants ou en trop")
    for t, d in par_temoin.items():
        if set(d) != set(attendues):
            raise Refus(f"verdicts : {t} : les cinq rendus du plan ne sont pas tous déposés")
    return {"execution": k, "par_temoin": par_temoin}


# --- tableaux --------------------------------------------------------------------------------------------------------------


def tableaux(ids, banque: dict, par_temoin: dict):
    """Pour les témoins `ids` (ordre donné) : y (bon = vrai), tenté (n, 5), vote « notable » (n, 5) ; un absent vaut rejet."""
    import numpy as np
    n = len(ids)
    y = np.array([banque[t]["classe"] == "bon" for t in ids], dtype=bool)
    tente = np.zeros((n, len(COLONNES)), dtype=bool)
    vote = np.zeros((n, len(COLONNES)), dtype=bool)
    for i, t in enumerate(ids):
        for c, (j, r, _b) in enumerate(COLONNES):
            x = par_temoin[t][(j, r)]
            tente[i, c] = x["etat"] in ETATS_TENTES
            vote[i, c] = bool(x["verdict"] is not None and x["verdict"]["notable"])
    return y, tente, vote


def _flottant(x):
    if x is None:
        return None
    x = float(x)
    return x if math.isfinite(x) else None


def etalonner(banque: dict, verdicts: dict, banc) -> dict:
    """Poids, seuil et règle des bras C et P ; ρ d'étalonnage ; sur les témoins de la moitié « étalonnage » dont les deux
    premiers rendus ont été tentés. Fonctions du banc v4, sans changement."""
    import numpy as np
    par_temoin = verdicts["par_temoin"]
    tous = sorted(par_temoin)
    y_tous, tente, _ = tableaux(tous, banque, par_temoin)
    lus = [t for t, ok in zip(tous, tente[:, 0] & tente[:, 1]) if ok]
    exclus = [t for t, ok in zip(tous, tente[:, 0] & tente[:, 1]) if not ok]
    y, _, vote = tableaux(lus, banque, par_temoin)
    if int(y.sum()) < 2 or int((~y).sum()) < 2:
        raise Refus("étalonnage : moins de deux témoins tentés dans une classe : poids non estimables, la mère est saisie")
    V = vote[None, :, :2]                                   # (1, n, 2) : juge Opus, juge Argon, premier rendu
    E = V != y[None, :, None]
    V_pm = 2.0 * V - 1.0
    w_c, repli_c = banc.poids_covariance(V_pm, y)
    s_c = banc.seuil_milieu(banc.score(V_pm, w_c), y)
    regle_c = banc.regle_choisie(w_c[0], s_c[0])
    w_p = banc.poids_precision(V, y, E)
    s_p = banc.seuil_milieu(banc.score(V_pm, w_p), y)
    regle_p = banc.regle_choisie(w_p[0], s_p[0])
    rho, indef = banc.rho_moyenne(banc.cov_intra_classes(E.astype(float), y))
    return {
        "temoins_de_la_moitie": len(tous), "temoins_lus": len(lus), "bons_lus": int(y.sum()),
        "mauvais_lus": int((~y).sum()), "temoins_exclus_premiers_rendus_non_tentes": exclus,
        "identifiants_lus": lus,
        "bras_C": {"poids": [float(x) for x in w_c[0]], "seuil": float(s_c[0]),
                   "repli_poids_egaux": bool(repli_c[0]), "regle_choisie": regle_c},
        "bras_P": {"poids": [float(x) for x in w_p[0]], "seuil": float(s_p[0]), "regle_choisie": regle_p},
        "rho_etalonnage": None if bool(indef[0]) else _flottant(rho[0]),
        "rho_etalonnage_indefini": bool(indef[0]),
        "ordre_des_juges_dans_les_poids": list(JUGES),
    }


# --- manifeste (règle R9) ---------------------------------------------------------------------------------------------


def commit_du_depot():
    try:
        r = subprocess.run(["git", "-C", str(Path(__file__).resolve().parent), "rev-parse", "HEAD"],
                           capture_output=True, text=True, timeout=30, stdin=subprocess.DEVNULL)
        return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None
    except (OSError, subprocess.SubprocessError):
        return None


def versions() -> dict:
    import numpy as np
    return {"python": sys.version.split()[0], "numpy": np.__version__, "plateforme": platform.platform(),
            "executable": sys.executable}


def horodatage() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --- exécution --------------------------------------------------------------------------------------------------------------


def executer(banque_chemin, banque_sha, verdicts_chemin, verdicts_sha, dossier, n_temoins=N_TEMOINS, banc=None) -> dict:
    """Étalonnage : lit la banque et les seuls verdicts de la moitié « étalonnage », écrit et scelle la pièce et le
    manifeste dans DOSSIER/etalonnage/ (refus s'il existe)."""
    garde_chemins([banque_chemin, verdicts_chemin, dossier])
    sortie = Path(dossier) / SOUS_DOSSIER
    if sortie.exists():
        raise Refus("étalonnage : dossier de sortie déjà présent : une exécution par dossier, rien n'est écrasé")
    nom_de_verdicts(verdicts_chemin)                         # forme du nom, avant toute ouverture
    if nom_de_verdicts(verdicts_chemin)[0] != "etalonnage":
        raise Refus("étalonnage : fichier des verdicts de la moitié « lecture » passé à l'étalonnage : refus, aucune "
                    "ligne lue")
    banc = banc if banc is not None else charger_banc()
    banque = lire_banque(banque_chemin, banque_sha, n_temoins)
    verdicts = lire_verdicts_moitie(verdicts_chemin, verdicts_sha, "etalonnage", banque)
    resultat = etalonner(banque, verdicts, banc)
    piece = {
        "piece": PIECE, "version": VERSION, "banc_v4_sha256": banc.__empreinte__, "banque_sha256": banque_sha,
        "n_temoins_de_la_banque": n_temoins,
        "verdicts_etalonnage": {"fichier": Path(verdicts_chemin).name, "sha256": verdicts_sha,
                                "execution": verdicts["execution"], "version_du_code_d_appel": VERSION_CODE_APPEL},
        "regle_d_un_absent": "verdict absent : jamais « notable », compté comme rejet",
        **resultat,
    }
    Path(dossier).mkdir(parents=True, exist_ok=True)
    sortie.mkdir(parents=False, exist_ok=False)
    h = ecrire_scelle(sortie / FICHIER_PIECE, piece)
    configuration = {"banque": str(Path(banque_chemin).resolve()), "banque_sha256": banque_sha,
                     "verdicts_etalonnage": str(Path(verdicts_chemin).resolve()), "verdicts_etalonnage_sha256": verdicts_sha,
                     "dossier": str(Path(dossier).resolve()), "n_temoins": n_temoins}
    manifeste = {
        "version": VERSION, "horodatage_utc": horodatage(), "programme_sha256": sha256_fichier(Path(__file__)),
        "configuration": configuration, "configuration_sha256": sha256_octets(json_octets(configuration)),
        "versions": versions(), "graines": {"racines": [], "note": "aucun tirage : l'étalonnage ne dérive aucune graine"},
        "commits": {"depot_de_travail": commit_du_depot()},
        "pieces_qui_font_foi": {"texte_v7": TEXTE_V7_SHA256, "additif_3_v3": ADDITIF_3_V3_SHA256,
                                "verdict_portee_200_v2": VERDICT_PORTEE_200_V2_SHA256, "banc_v4": banc.__empreinte__,
                                "code_d_appel_v4": CODE_APPEL_V4_SHA256, "generateur_v3": GENERATEUR_V3_SHA256},
        "sorties": {FICHIER_PIECE: h},
    }
    ecrire_scelle(sortie / FICHIER_MANIFESTE, manifeste)
    return {"piece": piece, "piece_sha256": h, "manifeste": manifeste, "sortie": str(sortie)}


def _argument(argv, nom):
    if nom not in argv:
        raise Refus(f"argument {nom} exigé")
    i = argv.index(nom)
    if i + 1 >= len(argv) or argv.count(nom) != 1:
        raise Refus(f"argument {nom} : une valeur, une seule fois")
    return argv[i + 1]


def principal(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        noms = ("--banque", "--banque-sha", "--verdicts-etalonnage", "--verdicts-etalonnage-sha", "--dossier")
        inconnus = [a for a in argv[0::2] if a not in noms]
        if inconnus or len(argv) != 2 * len(noms):
            raise Refus("arguments : exactement " + " ".join(noms))
        r = executer(_argument(argv, "--banque"), _argument(argv, "--banque-sha"),
                     _argument(argv, "--verdicts-etalonnage"), _argument(argv, "--verdicts-etalonnage-sha"),
                     _argument(argv, "--dossier"))
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001 — dont `RegleInconnue` du banc : arrêt du programme, nommé
        print(json.dumps({"arret": type(e).__name__, "message": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps({"piece": r["sortie"], "piece_sha256": r["piece_sha256"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
