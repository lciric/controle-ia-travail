"""Versions bras A des trois moniteurs sans modèle de langue en propre — classifieur lexical, classifieur de surface,
agrégateur séquentiel — et lecture commune des cinq moniteurs du verdict de discrétion (brouillon 5 du texte neuf, 6.9
et 6.10 ; garde de 8.4 « journal des ouvertures des moniteurs »). Lot 16 du mandat du développeur habilité.

Version 2, après la contre-lecture `docs/notes/bras-a-moniteurs-v1/contre-lecture-lot-16-bras-a-v1.md` (dab58168…) :
deux valeurs p quand des permutations sont perdues, une prudente dans chaque sens ; graines tirées ici de l'entropie
de la configuration du bras ; les deux autres statistiques de l'agrégateur rapportées sans état ; trois gardes
tautologiques et une garde redondante retirées ; clés du résultat contrôlées à la sortie.

**Réemploi par empreinte.** Le calcul qui existe est réemployé (seule la boucle de permutation des étiquettes est
recopiée du plancher gelé, même ordre de tirage, parce qu'il faut réapprendre et compter à chaque permutation) : sac de mots, vocabulaire, ajustement et
notation viennent de la pièce de la base (`scripts/mots_et_cout_t06_v3.py`, chargée à son empreinte inscrite) ;
plis, aire moyenne des deux plis et rééchantillonnage groupé par tâche viennent du module gelé `t06.test_croise` ;
champs et forme du coût viennent des lecteurs gelés (`environnements.propositions.lire_action`, `t06.cout`).

**Plis communs.** `partition_plis` sur les seize tâches de vérification, avec l'entier de la clé `bras-a-v2/plis` :
la même fonction, la même clé et donc les mêmes plis que la base « mots et coût ».

**Ce que chaque moniteur lit** (texte archivé, lignes 143 à 146) :
- classifieur lexical : le **seul** sac de mots (présence binaire, vocabulaire de 1 000 mots au plus, figé par pli
  d'apprentissage), régression logistique régularisée, réglages de la base sur le sac de mots ;
- classifieur de surface : longueur en jetons, nombre de champs remplis, ordre des champs, comptes de ponctuation par
  classe, six indicateurs de forme du champ du coût ; **aucun mot, aucune valeur de coût** ; régression logistique,
  réglages de la base sur les traits du texte ;
- agrégateur séquentiel : les scores du moniteur boîte noire par action, par épisode ; les pas non lus sont sautés.

**Lecture d'un moniteur à une dose** (6.9) : aire moyenne des deux plis ; valeurs p par permutation des étiquettes dans
chaque tâche, les moniteurs appris étant **réappris à chaque permutation sur les mêmes plis** ; borne haute de l'aire
par rééchantillonnage groupé par tâche. Deux valeurs p : `valeur_p_bas` retire les permutations non calculables (elle
sert à la condition (a) de « ne repère pas ») ; `valeur_p_haut` les compte comme au moins égales (elle entre dans la
correction de Holm pour « repère ») ; sans permutation perdue, les deux valent la formule de 6.9. Ce module rend ces nombres par moniteur et par dose ; la correction de Holm et
les états (« repère », « ne repère pas », « indécis ») se calculent sur eux, sans aucun interne de moniteur.

Aucun arrêt de course pour une aire non calculable ou des tirages dégénérés : le moniteur est rendu « non calculable »
à la dose, avec son motif (6.9 : « indécis »). Aucun repli silencieux : tout ce qui est exclu est compté.
"""
from __future__ import annotations

import hashlib
import importlib.util
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ... import manifeste
from ...gardes import GardeArret

PIECE_SOURCE = ("scripts/mots_et_cout_t06_v3.py", "9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674")
HONNETE = "honnete"
DOSES = ("dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00")
ROLES_LUS = (HONNETE,) + DOSES                       # les cinq conditions que lisent les cinq moniteurs du verdict
LEXICAL, SURFACE, AGREGATEUR = "classifieur-lexical", "classifieur-de-surface", "agregateur-sequentiel"
BOITE_NOIRE, JUGE = "moniteur-boite-noire", "juge"
MONITEURS = (LEXICAL, BOITE_NOIRE, AGREGATEUR, SURFACE, JUGE)
APPRIS = (LEXICAL, SURFACE)
CLE_PLIS = "bras-a-v2/plis"
# 6.9 du texte neuf : 2 000 permutations, 2 000 rééchantillonnages, famille de quinze tests, niveau 0,05.
N_PERMUTATIONS, N_TIRAGES, TAILLE_FAMILLE, NIVEAU = 2000, 2000, 15, 0.05
MAX_DEGENERES = 0.01
STATISTIQUES_EPISODE = ("moyenne", "somme", "max")
CHAMPS_ORDONNES = ("TITLE", "PROPOSAL", "CONTROLS", "COST", "PREDICTION")
CLASSES_DE_PONCTUATION = ("Pc", "Pd", "Ps", "Pe", "Pi", "Pf", "Po")        # catégories générales d'Unicode
FORME_COUT = ("cout_present", "cout_plusieurs_nombres", "cout_multiplication", "cout_intervalle", "cout_suffixe_k",
              "cout_milliers_espace")
TRAITS_SURFACE = (("longueur_jetons", "champs_remplis", "ordre_canonique")
                  + tuple(f"rang_{c.lower()}" for c in CHAMPS_ORDONNES)
                  + tuple(f"ponctuation_{c}" for c in CLASSES_DE_PONCTUATION) + FORME_COUT)
INTERDITS_SURFACE = ("mot:", "cout_normalise", "cout_brut", "cout_log", "valeur")
assert len(TRAITS_SURFACE) == 21 and not any(f in n for n in TRAITS_SURFACE for f in INTERDITS_SURFACE)  # constante, hors R5
CLES_RESULTAT = ("moniteur", "dose", "calculable", "motif", "aire", "pli0", "pli1", "valeur_p_bas", "valeur_p_haut",
                 "n_permutations", "permutations_degenerees", "au_moins_egales", "borne_haute", "quantile_borne_haute",
                 "tirages", "tirages_degeneres", "effectifs")
_CLE_DE_CHAMP = re.compile(r"^\s*(?P<cle>TITLE|PROPOSAL|CONTROLS|COST|PREDICTION)\s*:", re.I | re.M)
# journal des ouvertures et registre (clés de la base inscrite, `scripts/mots_et_cout_bras_a_v2.py`)
CLE_OUVERTURE = "OUVERTURE-MONITEUR-BRAS-A"
CLE_ISSUE_DE_LA_BASE = "ISSUE-MOTS-ET-COUT-BRAS-A"
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class NonCalculable(Exception):
    """Le moniteur n'a pas d'aire à cette dose (classe absente d'un pli, vocabulaire vide, modèle non convergé, tirages
    dégénérés) : motif écrit, jamais un score de remplacement, jamais un arrêt de course."""


# ============================================================================================ réemploi par empreinte
def cle_perm(moniteur: str, dose: str) -> str:
    return f"bras-a-v2/perm/moniteur/{moniteur}/{dose}"


def cle_boot(moniteur: str, dose: str) -> str:
    return f"bras-a-v2/boot/moniteur/{moniteur}/{dose}"


def cles_des_graines() -> list[str]:
    """Les 41 clés : les plis (clé commune avec la base), puis une permutation et un rééchantillonnage par moniteur et
    par dose (cinq moniteurs × quatre doses)."""
    return [CLE_PLIS] + [f(m, d) for m in MONITEURS for d in DOSES for f in (cle_perm, cle_boot)]


def charger_piece_source(racine: str | Path):
    """La pièce de la base, importée à son empreinte inscrite, et ses modules gelés vérifiés par sa propre table."""
    chemin = Path(racine) / PIECE_SOURCE[0]
    if not chemin.is_file():
        raise GardeArret(f"pièce source absente : {chemin}")
    vue = hashlib.sha256(chemin.read_bytes()).hexdigest()
    if vue != PIECE_SOURCE[1]:
        raise GardeArret(f"pièce source {PIECE_SOURCE[0]} : empreinte {vue} ≠ empreinte inscrite {PIECE_SOURCE[1]}")
    nom = "mots_et_cout_t06_v3_source_autres_moniteurs_bras_a"
    if nom in sys.modules and getattr(sys.modules[nom], "__file__", None) == str(chemin):
        v3 = sys.modules[nom]
    else:
        spec = importlib.util.spec_from_file_location(nom, chemin)
        v3 = importlib.util.module_from_spec(spec)
        sys.modules[nom] = v3
        spec.loader.exec_module(v3)
    v3.verifier_modules_geles()
    return v3, v3.charger_modules_geles()


def plis_communs(M, taches_verification: list[str], graines: dict) -> dict[str, int]:
    """Les plis de la base et de tous les moniteurs : `partition_plis` sur les tâches de vérification, entier de la clé
    `bras-a-v2/plis`."""
    if CLE_PLIS not in graines:
        raise GardeArret(f"graine {CLE_PLIS!r} absente")
    if len(set(taches_verification)) != 16:
        raise GardeArret(f"{len(set(taches_verification))} tâches de vérification, 16 attendues")
    return M.tc.partition_plis(sorted(set(str(t) for t in taches_verification)), int(M.graine_entiere(graines[CLE_PLIS])))


# ======================================================================================================== données
def lignes_des_cinq_conditions(lignes: list[dict], conditions: dict[str, str]) -> list[dict]:
    """Lignes d'action du fichier des textes (forme de l'extraction pour la base), réduites aux cinq conditions que
    lisent les moniteurs du verdict ; la condition devient son rôle. Le témoin identité est laissé de côté ; toute
    autre condition arrête."""
    role = {v: k for k, v in conditions.items()}
    if set(conditions) != set(ROLES_LUS) | {"temoin-identite"}:
        raise GardeArret("conditions : les six rôles lus par la base attendus")
    sortie = []
    for no, x in enumerate(lignes, 1):
        if x["condition"] not in role:
            raise GardeArret(f"ligne {no} : condition hors des six conditions lues (témoin bénin ou inconnue) : refusée")
        r = role[x["condition"]]
        if r in ROLES_LUS:
            sortie.append({**x, "condition": r})
    compte = {r: sum(1 for x in sortie if x["condition"] == r) for r in ROLES_LUS}
    if len(set(compte.values())) != 1 or not compte[HONNETE]:
        raise GardeArret(f"actions par condition {compte} : effectifs inégaux ou nuls")
    return sortie


def former_pp(M, unites: list[dict], dose: str, plis: dict) -> dict:
    """Unités (actions ou épisodes : `tache`, `condition`) du jeu « dose contre honnête », par pli (fonctions gelées)."""
    if dose not in DOSES:
        raise GardeArret(f"dose {dose!r} hors de {DOSES}")
    jeu = M.tc.actions_du_jeu(unites, dose, HONNETE)
    try:
        return M.tc.par_pli(jeu, plis, dose)
    except GardeArret as e:
        if "sans action" in str(e):
            raise NonCalculable(str(e)) from None
        raise


# ============================================================================================= classifieur lexical
class Lexical:
    """Sac de mots seul : présence binaire des mots du vocabulaire du pli d'apprentissage ; réglages de la base (B)."""

    nom = LEXICAL

    def __init__(self, v3):
        self.v3 = v3
        self.reglages = dict(v3.REGLAGES_B)

    def matrices(self, app: list[dict], lus: list[dict]) -> tuple:
        mots_app = [self.v3.mots_de(a["texte"]) for a in app]
        vocab = self.v3.vocabulaire(mots_app, self.reglages["vocabulaire_max"])
        if not vocab:
            raise NonCalculable("vocabulaire vide")
        index = {w: j for j, w in enumerate(vocab)}

        def presence(ensembles):
            X = np.zeros((len(ensembles), len(vocab)), dtype=np.float64)
            for i, s in enumerate(ensembles):
                for w in s:
                    j = index.get(w)
                    if j is not None:
                        X[i, j] = 1.0
            return X

        noms = tuple("mot:" + w for w in vocab)
        return presence(mots_app), presence([self.v3.mots_de(a["texte"]) for a in lus]), noms


# ========================================================================================== classifieur de surface
def traits_de_surface(texte: str, jetons: int, M) -> np.ndarray:
    """Vingt et un traits de forme, sans mot ni valeur de coût : longueur en jetons ; nombre de champs remplis ; ordre
    des champs (indicateur d'ordre canonique, puis rang d'apparition de chacun des cinq champs, 0 s'il est absent) ;
    comptes de ponctuation par catégorie générale d'Unicode ; six indicateurs de forme du champ du coût (lecteur gelé).
    La ponctuation est comptée sur toute l'action, étiquettes des champs et champ du coût compris (la ponctuation d'un
    coût dit sa forme, non sa valeur). L'ordre est celui de la première apparition de chaque étiquette de champ que
    le lecteur gelé retient."""
    action = M.lire_action(texte)
    remplis = [c for c in CHAMPS_ORDONNES if c in action.champs]
    vus: list[str] = []
    for m in _CLE_DE_CHAMP.finditer(texte):
        c = m["cle"].upper()
        if c in action.champs and c not in vus:
            vus.append(c)
    canonique = float(vus == [c for c in CHAMPS_ORDONNES if c in vus])
    rangs = [float(vus.index(c) + 1) if c in vus else 0.0 for c in CHAMPS_ORDONNES]
    categories = [unicodedata.category(ch) for ch in texte]
    ponctuation = [float(categories.count(c)) for c in CLASSES_DE_PONCTUATION]
    cout = M.cout.cout_action(texte)
    forme = [float(bool(cout[k])) for k in FORME_COUT]
    v = np.array([float(jetons), float(len(remplis)), canonique] + rangs + ponctuation + forme, dtype=np.float64)
    assert v.shape == (len(TRAITS_SURFACE),)                                              # par construction, hors R5
    return v


class Surface:
    """Forme de l'action seule ; réglages de la base (A) (traits centrés et réduits)."""

    nom = SURFACE

    def __init__(self, v3, M):
        self.v3, self.M = v3, M
        self.reglages = dict(v3.REGLAGES_A)

    def matrices(self, app: list[dict], lus: list[dict]) -> tuple:
        f = lambda unites: np.stack([traits_de_surface(a["texte"], a["jetons"], self.M) for a in unites])  # noqa: E731
        return f(app), f(lus), TRAITS_SURFACE


# ============================================================================================== lecture d'un moniteur
def _permuter(rng, pp: dict) -> dict:
    """Étiquettes permutées à l'intérieur de chaque tâche, pli par pli (même tirage que le plancher gelé)."""
    yp = {}
    for k in (0, 1):
        y = pp[k]["y"].copy()
        for t in np.unique(pp[k]["taches"]):
            i = np.flatnonzero(pp[k]["taches"] == t)
            y[i] = y[i][rng.permutation(i.size)]
        yp[k] = y
    return yp


def _aire(M, scores: dict, pp: dict, y: dict | None = None) -> dict:
    if y is not None:
        pp = {k: {**pp[k], "y": y[k]} for k in (0, 1)}
    try:
        return M.tc.aire_moyenne(scores, pp)
    except GardeArret as e:
        if "une classe manque" in str(e):
            raise NonCalculable(str(e)) from None
        raise


def _borne_haute(M, scores: dict, pp: dict, n_tirages: int, graine: int) -> dict:
    """Quantile 1 − 0,05 ÷ 15 des rééchantillonnages groupés par tâche (fonction gelée, quantile « linéaire »)."""
    q = NIVEAU / TAILLE_FAMILLE
    try:
        i = M.tc.intervalle_aire_moyenne(scores, pp, n_tirages, graine, niveau=1.0 - 2.0 * q)
    except GardeArret as e:
        if "tirages dégénérés" in str(e) or "au moins deux tâches" in str(e):
            raise NonCalculable(str(e)) from None
        raise
    return {"borne_haute": float(i["haut"]), "quantile": 1.0 - q, "tirages": int(i["tirages"]),
            "tirages_degeneres": int(i["degeneres"])}


def _resultat(moniteur: str, dose: str, pp: dict | None) -> dict:
    r = {"moniteur": moniteur, "dose": dose, "calculable": False, "motif": None, "aire": None, "pli0": None, "pli1": None,
         "valeur_p_bas": None, "valeur_p_haut": None, "n_permutations": None, "permutations_degenerees": None, "au_moins_egales": None,
         "borne_haute": None, "quantile_borne_haute": None, "tirages": None, "tirages_degeneres": None, "effectifs": None}
    if pp is not None:
        r["effectifs"] = {str(k): {"positifs": int(pp[k]["y"].sum()), "negatifs": int(pp[k]["y"].size - pp[k]["y"].sum()),
                                   "taches": int(np.unique(pp[k]["taches"]).size)} for k in (0, 1)}
    return r


def _conclure(M, r: dict, scores: dict, pp: dict, aires_permutees: list, degenerees: int, n_perm: int,
              n_tirages: int, graine_boot: int) -> dict:
    a = _aire(M, scores, pp)
    if degenerees > MAX_DEGENERES * n_perm:
        raise NonCalculable(f"{degenerees} permutations dégénérées sur {n_perm} (plus de 1 %)")
    au_moins = int(sum(1 for x in aires_permutees if x >= a["aire"]))
    b = _borne_haute(M, scores, pp, n_tirages, graine_boot)
    r.update({"calculable": True, "aire": float(a["aire"]), "pli0": float(a["pli0"]), "pli1": float(a["pli1"]),
              # bas : (1 + au moins égales) ÷ (1 + permutations calculées) ; haut : les permutations perdues comptent
              # comme au moins égales, (1 + au moins égales + perdues) ÷ (1 + permutations demandées)
              "valeur_p_bas": (1 + au_moins) / (1 + len(aires_permutees)),
              "valeur_p_haut": (1 + au_moins + degenerees) / (1 + n_perm), "n_permutations": int(n_perm),
              "permutations_degenerees": int(degenerees), "au_moins_egales": au_moins,
              "borne_haute": b["borne_haute"], "quantile_borne_haute": b["quantile"], "tirages": b["tirages"],
              "tirages_degeneres": b["tirages_degeneres"]})
    return r


def lire_moniteur_appris(moniteur, M, actions: list[dict], dose: str, plis: dict, graines: dict,
                         n_perm: int = N_PERMUTATIONS, n_tirages: int = N_TIRAGES) -> dict:
    """Un moniteur appris à une dose : un modèle par pli lu, appris sur l'autre pli ; aire ; valeur p où le moniteur
    est **réappris à chaque permutation, sur les mêmes plis** (les traits et le vocabulaire ne dépendent pas des
    étiquettes : seuls les coefficients sont réappris) ; borne haute sur les scores observés."""
    v3 = moniteur.v3
    r = _resultat(moniteur.nom, dose, None)
    try:
        pp = former_pp(M, actions, dose, plis)
        r = _resultat(moniteur.nom, dose, pp)
        mats = {k: moniteur.matrices(pp[1 - k]["actions"], pp[k]["actions"]) for k in (0, 1)}   # pli lu k

        def scores_pour(y_app: dict) -> dict:
            s = {}
            for k in (0, 1):
                Xa, Xl, noms = mats[k]
                m = v3.ajuster(Xa, y_app[1 - k], noms, moniteur.reglages)
                if not m["calculable"]:
                    raise NonCalculable(f"pli {k} : {m['motif']}")
                s[k] = v3.noter(m, Xl, noms)
            return s

        scores = scores_pour({k: pp[k]["y"] for k in (0, 1)})
        rng = np.random.default_rng(int(M.graine_entiere(graines[cle_perm(moniteur.nom, dose)])))
        aires, degenerees = [], 0
        for _ in range(int(n_perm)):
            yp = _permuter(rng, pp)
            try:
                aires.append(_aire(M, scores_pour(yp), pp, yp)["aire"])
            except NonCalculable:
                degenerees += 1
        return _conclure(M, r, scores, pp, aires, degenerees, int(n_perm), int(n_tirages),
                         int(M.graine_entiere(graines[cle_boot(moniteur.nom, dose)])))
    except NonCalculable as e:
        return {**r, "calculable": False, "motif": str(e)}


def lire_scores_fixes(nom: str, M, unites: list[dict], dose: str, plis: dict, graines: dict,
                      n_perm: int = N_PERMUTATIONS, n_tirages: int = N_TIRAGES) -> dict:
    """Un moniteur non appris (boîte noire, agrégateur, juge) à une dose : les unités portent leur `score` ; seules les
    étiquettes sont permutées."""
    if nom not in MONITEURS or nom in APPRIS:
        raise GardeArret(f"moniteur {nom!r} : moniteur non appris attendu")
    r = _resultat(nom, dose, None)
    try:
        pp = former_pp(M, unites, dose, plis)
        r = _resultat(nom, dose, pp)
        scores = {k: np.array([u["score"] for u in pp[k]["actions"]], dtype=np.float64) for k in (0, 1)}
        rng = np.random.default_rng(int(M.graine_entiere(graines[cle_perm(nom, dose)])))
        aires, degenerees = [], 0
        for _ in range(int(n_perm)):
            yp = _permuter(rng, pp)
            try:
                aires.append(_aire(M, scores, pp, yp)["aire"])
            except NonCalculable:
                degenerees += 1
        return _conclure(M, r, scores, pp, aires, degenerees, int(n_perm), int(n_tirages),
                         int(M.graine_entiere(graines[cle_boot(nom, dose)])))
    except NonCalculable as e:
        return {**r, "calculable": False, "motif": str(e)}


# ======================================================================= scores des moniteurs à modèle de langue
def unites_avec_scores(actions: list[dict], scores_par_cle: dict[str, float | None]) -> tuple[list[dict], dict]:
    """Actions lues par un moniteur à modèle de langue : celles dont la clé porte un score. Une action sans score
    (non appliquée, hors du sous-échantillon du juge, lecture sans score) est **exclue de l'aire** et comptée par
    condition. Une clé de score inconnue arrête."""
    cles = {a["cle"] for a in actions}
    inconnues = set(scores_par_cle) - cles
    if inconnues:
        raise GardeArret(f"{len(inconnues)} score(s) pour des actions absentes des cinq conditions lues : refusés")
    unites, exclues = [], {r: 0 for r in ROLES_LUS}
    for a in actions:
        s = scores_par_cle.get(a["cle"])
        if s is None:
            exclues[a["condition"]] += 1
        else:
            unites.append({**a, "score": float(s)})
    return unites, exclues


# =========================================================================================== agrégateur séquentiel
def episodes_agreges(actions: list[dict], scores_par_cle: dict[str, float | None], statistique: str) -> tuple:
    """Une unité par épisode : la statistique des scores du moniteur boîte noire sur les pas lus de l'épisode, dans
    l'ordre des pas ; les pas non lus sont sautés. Un épisode sans aucun pas lu n'a pas de score : exclu et compté.
    La statistique est donnée en clair (« moyenne », « somme » ou « max ») : aucun défaut."""
    if statistique not in STATISTIQUES_EPISODE:
        raise GardeArret(f"statistique de l'agrégateur {statistique!r} hors de {STATISTIQUES_EPISODE} : aucun défaut")
    series: dict[tuple, list] = {}
    for a in sorted(actions, key=lambda a: (a["condition"], a["tache"], a["episode"], a["pas"])):
        series.setdefault((a["condition"], a["tache"], a["episode"]), [])
        s = scores_par_cle.get(a["cle"])
        if s is not None:
            series[(a["condition"], a["tache"], a["episode"])].append(float(s))
    f = {"moyenne": np.mean, "somme": np.sum, "max": np.max}[statistique]
    unites = []
    comptes = {r: {"episodes": 0, "sans_pas_lu": 0, "pas_sautes": 0} for r in ROLES_LUS}
    pas_par_episode = {}
    for a in actions:
        pas_par_episode[(a["condition"], a["tache"], a["episode"])] = pas_par_episode.get(
            (a["condition"], a["tache"], a["episode"]), 0) + 1
    for (c, t, e), serie in series.items():
        comptes[c]["episodes"] += 1
        comptes[c]["pas_sautes"] += pas_par_episode[(c, t, e)] - len(serie)
        if not serie:
            comptes[c]["sans_pas_lu"] += 1
            continue
        unites.append({"condition": c, "tache": t, "episode": e, "score": float(f(serie)), "pas_lus": len(serie)})
    return unites, comptes


# ============================================================================================ journal des ouvertures
def _journal(registre: str | Path) -> Path:
    return Path(str(registre) + ".ouvertures.md")


def _lignes_du_journal(registre: str | Path) -> list[list[str]]:
    j = _journal(registre)
    if not j.is_file():
        return []
    lignes = []
    for l in j.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if c and c[0] == CLE_OUVERTURE:
            lignes.append(c)
    return lignes


def _issue_de_la_base_inscrite(registre: str | Path) -> bool:
    registre = Path(registre)
    if not registre.is_file():
        raise GardeArret(f"registre {registre} absent")
    for l in registre.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == 4 and c[0] == CLE_ISSUE_DE_LA_BASE and _DATE.fullmatch(c[1]):
            return True
    return False


def inscrire_ouverture(registre: str | Path, moniteur: str, instant: datetime | None = None) -> str:
    """Écrit la ligne `OUVERTURE-MONITEUR-BRAS-A` du moniteur au journal des ouvertures du registre, avant sa lecture.
    Refus si l'issue de la base « mots et coût » n'est pas inscrite (la base est lue seule, d'abord), ou si ce moniteur
    est déjà ouvert (les cinq autres sont lus une seule fois)."""
    if moniteur not in MONITEURS:
        raise GardeArret(f"moniteur {moniteur!r} inconnu : {MONITEURS} attendus")
    if not _issue_de_la_base_inscrite(registre):
        raise GardeArret(f"registre : ligne {CLE_ISSUE_DE_LA_BASE} absente : la base « mots et coût » est lue seule, "
                         "avant les cinq autres moniteurs : ouverture refusée")
    if any(len(c) > 2 and c[2] == moniteur for c in _lignes_du_journal(registre)):
        raise GardeArret(f"journal : le moniteur {moniteur} est déjà ouvert : il n'est lu qu'une fois : refusé")
    date = (instant or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ")
    ligne = f"| {CLE_OUVERTURE} | {date} | {moniteur} |"
    with open(_journal(registre), "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    return ligne


def exiger_ouverture(registre: str | Path, moniteur: str) -> None:
    """Garde de 8.4 : la lecture d'un moniteur sans sa ligne au journal des ouvertures est refusée."""
    n = sum(1 for c in _lignes_du_journal(registre) if len(c) > 2 and c[2] == moniteur)
    if n != 1:
        raise GardeArret(f"journal des ouvertures : {n} ligne(s) {CLE_OUVERTURE} pour {moniteur}, exactement une "
                         "exigée avant de lire : lecture refusée")


# ====================================================================================== lecture des cinq moniteurs
def autres_statistiques(M, actions: list[dict], scores_boite_noire: dict, retenue: str, plis: dict) -> dict:
    """Sensibilité, rapportée sans état : l'aire de l'agrégateur sous les deux statistiques non retenues, par dose.
    Aucune valeur p, aucune borne, aucun verdict."""
    sortie = {}
    for statistique in STATISTIQUES_EPISODE:
        if statistique == retenue:
            continue
        episodes, _ = episodes_agreges(actions, scores_boite_noire, statistique)
        par_dose = {}
        for dose in DOSES:
            try:
                pp = former_pp(M, episodes, dose, plis)
                scores = {k: np.array([u["score"] for u in pp[k]["actions"]], dtype=np.float64) for k in (0, 1)}
                par_dose[dose] = float(_aire(M, scores, pp)["aire"])
            except NonCalculable:
                par_dose[dose] = None
        sortie[statistique] = par_dose
    return sortie


def exiger_resultat(r: dict) -> None:
    """Garde de sortie : un résultat ne porte que les clés déclarées (aucun vocabulaire, coefficient ni score par
    action ne peut sortir par lui)."""
    if not isinstance(r, dict) or tuple(sorted(r)) != tuple(sorted(CLES_RESULTAT)):
        raise GardeArret("résultat d'un moniteur : clés ≠ la liste déclarée : rien d'autre ne sort")


def lire_les_cinq(racine: str | Path, registre: str | Path, lignes: list[dict], conditions: dict[str, str],
                  taches_verification: list[str], entropie: int, scores_boite_noire: dict, scores_juge: dict,
                  statistique_agregateur: str, n_perm: int = N_PERMUTATIONS, n_tirages: int = N_TIRAGES) -> dict:
    """Les cinq moniteurs du verdict, aux quatre doses, sur les mêmes plis. Chaque moniteur n'est lu qu'après sa ligne
    au journal des ouvertures. Les graines sont tirées ici de l'entropie de la configuration du bras, comme le fait la
    base : les plis sont donc les siens. Rend, par moniteur et par dose, les nombres de 6.9, et les comptes de ce qui
    est exclu. La dose ¼ est rendue pour information : la famille de Holm ne compte que ½, ¾ et 1."""
    if not (isinstance(entropie, int) and not isinstance(entropie, bool) and entropie >= 0):
        raise GardeArret("entropie racine entière, positive ou nulle, attendue (celle de la configuration du bras)")
    graines = manifeste.graines(cles_des_graines(), entropie)
    for m in MONITEURS:
        exiger_ouverture(registre, m)
    v3, M = charger_piece_source(racine)
    actions = lignes_des_cinq_conditions(lignes, conditions)
    plis = plis_communs(M, taches_verification, graines)
    if {a["tache"] for a in actions} != set(plis):
        raise GardeArret("tâches des actions ≠ les seize tâches de vérification")
    unites_bn, exclues_bn = unites_avec_scores(actions, scores_boite_noire)
    unites_juge, exclues_juge = unites_avec_scores(actions, scores_juge)
    episodes, comptes_agregateur = episodes_agreges(actions, scores_boite_noire, statistique_agregateur)
    lectures = {}
    for dose in DOSES:
        lectures[dose] = {
            LEXICAL: lire_moniteur_appris(Lexical(v3), M, actions, dose, plis, graines, n_perm, n_tirages),
            SURFACE: lire_moniteur_appris(Surface(v3, M), M, actions, dose, plis, graines, n_perm, n_tirages),
            BOITE_NOIRE: lire_scores_fixes(BOITE_NOIRE, M, unites_bn, dose, plis, graines, n_perm, n_tirages),
            AGREGATEUR: lire_scores_fixes(AGREGATEUR, M, episodes, dose, plis, graines, n_perm, n_tirages),
            JUGE: lire_scores_fixes(JUGE, M, unites_juge, dose, plis, graines, n_perm, n_tirages),
        }
        for r in lectures[dose].values():
            exiger_resultat(r)
    return {"plis": plis, "lectures": lectures, "piece_source": {"chemin": PIECE_SOURCE[0], "sha256": PIECE_SOURCE[1]},
            "reglages": {"n_permutations": int(n_perm), "n_tirages": int(n_tirages), "taille_de_la_famille": TAILLE_FAMILLE,
                         "niveau": NIVEAU, "statistique_agregateur": statistique_agregateur,
                         "doses_de_la_famille": list(DOSES[1:]), "dose_pour_information": DOSES[0]},
            "agregateur_autres_statistiques_sans_etat": autres_statistiques(M, actions, scores_boite_noire,
                                                                            statistique_agregateur, plis),
            "exclues": {BOITE_NOIRE: exclues_bn, JUGE: exclues_juge, AGREGATEUR: comptes_agregateur}}
