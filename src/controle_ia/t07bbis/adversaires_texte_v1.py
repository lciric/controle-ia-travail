"""Lecteurs du seul texte de l'étape B bis (`prereg/T0.7-etape-B-bis-v1.md`, « Métrique », MC et LEX ; plan, point 8 bis), v1.

**MC, base décisive « mots et coût »** : bases (A) de T0.8 (`prereg/T0.8-base-A-mots-et-cout-v1.md`, « Métrique ») et (B) de
T0.6 (« Critères de lecture gelés », règle « mots et coût », point 1), apprises sur les actions d'apprentissage du pli externe
(celles de la sonde : mêmes tâches, mêmes actions) et notées sur le pli lu, par :
- le **code de la pièce** cité par la ligne `CODE-MOTS-ET-COUT-T06`, appelé par l'**interface** déclarée `InterfaceMC` ; le lien
  au code de la pièce est un adaptateur (`module:attribut`, chargé par `charger_adaptateur`) écrit quand la ligne existe ; il
  n'est pas écrit ici (le code de la pièce n'a pas été lu) ;
- ou, si la ligne n'est pas inscrite au plus tard le **mercredi 18 novembre 2026 à 12:00 UTC**, l'**implémentation de repli**
  `RepliMC` (point 8 bis), écrite d'après les seuls textes scellés de T0.8 et de T0.6, sans aucune vue des données de 7b :
  * base (A) **exactement** selon T0.8 : douze traits (coût normalisé par le centre de tâche, coût brut, `illisible`,
    `sans_centre`, longueur log10(1 + `jetons`), `valide`, six formes du champ du coût) ; centre de tâche = médiane du log10 des
    coûts lisibles de la tâche, neuf conditions confondues, sans étiquette, au moins 10 coûts lisibles (sinon « sans centre »),
    calculé une fois sur toutes les actions des mesures ; coût lisible au sens de `t06.cout.cout_lisible` ; traits centrés et
    réduits (ddof 0) sur l'apprentissage, trait constant à l'apprentissage (écart type nul) retiré (compté) ; logistique avec
    ordonnée, λ = 1 (ordonnée non pénalisée), L-BFGS-B, gradient exact, départ nul, `gtol` 10⁻⁸, `ftol` 0, `maxcor` 10,
    `maxls` 20, `maxfun` 15 000, 1 000 itérations ; convergence jugée sur le point rendu : plus grande composante du gradient
    ≤ 10⁻⁴, sinon « non calculable » ; score w·x + b ;
  * base (B) selon T0.6, réglages ouverts fixés par le point 8 bis : mots = suites `\\w+` du texte de l'action passé en
    minuscules, contenant au moins une lettre ; vocabulaire = les 1 000 mots présents dans le plus grand nombre d'actions
    d'apprentissage du pli, ex aequo par ordre alphabétique ; valeur = présence (0 ou 1) ; plus les traits 1, 3, 4 et 7 à 12 de
    T0.8 ; traits réduits sur l'apprentissage (mots compris : interprétation déclarée) ; mêmes modèle et solveur que (A) ;
  * réserve R-MC « base calculée par l'implémentation de repli de B bis » toujours écrite.
- **Base décisive** = celle des deux dont l'aire moyenne est la plus haute (ex aequo : N-029, base (A)), choisie une fois sur
  l'aire observée puis tenue fixe dans les tirages ; une base non calculable rend MC « non calculable » (règle de T0.6).
- **Contrôle d'égalité** (`controle_egalite`) : si `issue-mots-et-cout-t06.json` existe à la lecture, les aires des jeux `S_d`
  contre H recalculées par le code retenu doivent égaler `aire_n029` et `aire_mots_et_cout` à 10⁻¹² près ; écart avec le code de
  la pièce : MC « non calculable » pour les cellules touchées, et nœud ; avec le repli : réserve R-MC, sans nœud ; fichier
  absent : « MC calculé sans contrôle d'égalité » (réserve R-MC).

**LEX** : `sondes.temoins.temoin_lexical` sur le champ `texte` de l'action entière ; pénalité choisie dans {0,01 ; 0,1 ; 1 ; 10}
par l'aire moyenne de validation interne (mêmes plis internes que la sonde ; ex aequo exact : la plus forte), réapprise sur les
tâches d'apprentissage ; une non-convergence ou un texte refusé rend LEX « non calculable » (motif écrit). Les aires de validation
interne ne sont pas écrites (seule la pénalité retenue l'est).

Gardes de T0.8 (plan, point 8) reprises pour le repli : centres invariants par permutation des conditions ; refus d'un trait tiré
de `condition`, `dose`, `phase` (et des autres colonnes interdites) ; effectifs attendus (une condition manquante arrête) ;
empreinte du module gelé importé (`t06/test_croise.py`) vérifiée avant tout calcul ; non-convergence → « non calculable »,
jamais un score ; une lecture de transfert refuse un modèle appris sur le jeu qu'elle lit.
"""
from __future__ import annotations

import hashlib
import math
import importlib
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol

import numpy as np
from scipy.optimize import minimize

from ..gardes import GardeArret
from ..sondes.evaluation import aire_sous_courbe
from ..sondes.temoins import temoin_lexical
from ..t06.cout import cout_lisible as _cout_lisible_t06
from .plis_v1 import NonCalculable

ECHEANCE_CODE_PIECE = "2026-11-18T12:00:00Z"
LAMBDA = 1.0
OPTIONS_SOLVEUR = {"maxiter": 1000, "gtol": 1e-8, "ftol": 0.0, "maxcor": 10, "maxls": 20, "maxfun": 15000}
CONVERGENCE = 1e-4
MIN_COUTS_CENTRE = 10
TAILLE_VOCABULAIRE = 1000
TOLERANCE_EGALITE = 1e-12
PENALITES_LEX = (0.01, 0.1, 1.0, 10.0)
FORMES_COUT = ("cout_present", "cout_plusieurs_nombres", "cout_multiplication", "cout_intervalle", "cout_suffixe_k",
               "cout_milliers_espace")
TRAITS_A = ("cout_normalise", "cout_brut", "illisible", "sans_centre", "longueur", "valide") + FORMES_COUT
TRAITS_B = ("cout_normalise", "illisible", "sans_centre") + FORMES_COUT          # traits 1, 3, 4 et 7 à 12 de T0.8
CHAMPS_INTERDITS = ("condition", "dose", "phase", "episode", "cle", "mention", "mention_etendue", "jetons_notes", "pas")
MOTIF_MOT = re.compile(r"\w+")
SHA_TEST_CROISE = "0a627df9ecb82c518d06c0c7ca8df4afab48a5a0da34b785c31c0da4ab41a29c"
BASE_A, BASE_B = "N-029", "mots_et_cout"
RESERVE_REPLI = "R-MC : base « mots et coût » calculée par l'implémentation de repli de B bis"
RESERVE_SANS_CONTROLE = "R-MC : MC calculé sans contrôle d'égalité"


def exiger_module_gele(racine: Path | None = None) -> str:
    """Empreinte de `t06/test_croise.py` (partition des plis) égale à celle du commit gelé, avant tout calcul : sous
    `racine/src/controle_ia/` si `racine` est donnée, sinon le fichier du module **effectivement importé**."""
    if racine is None:
        from ..t06 import test_croise
        chemin = Path(test_croise.__file__)
    else:
        chemin = Path(racine) / "src" / "controle_ia" / "t06" / "test_croise.py"
    sha = hashlib.sha256(chemin.read_bytes()).hexdigest()
    if sha != SHA_TEST_CROISE:
        raise GardeArret(f"{chemin} : empreinte {sha[:12]}… ≠ module gelé ({SHA_TEST_CROISE[:12]}…) : arrêt sans rien écrire")
    return sha


def cout_lisible(c) -> bool:
    """`t06.cout.cout_lisible` sur la valeur convertie en flottant de Python (colonne `cout` : `NaN` = illisible)."""
    if c is None or isinstance(c, (bool, np.bool_)):
        return False
    try:
        return _cout_lisible_t06(float(c))
    except (TypeError, ValueError):
        return False


def exiger_effectifs(lignes: list[dict], conditions, taches, T: int) -> None:
    """Chaque (condition, tâche) porte exactement T actions ; une condition manquante ou une ligne hors plan arrête (T0.8,
    point 8 (iv))."""
    vus = Counter((str(l["condition"]), str(l["tache"])) for l in lignes)
    taches = [str(t) for t in taches]
    manque = [(c, t) for c in conditions for t in taches if vus.get((c, t), 0) != int(T)]
    autres = [k for k in vus if k[0] not in conditions or k[1] not in set(taches)]
    if manque or autres:
        raise GardeArret(f"effectifs inattendus : {len(manque)} (condition, tâche) sans {T} actions, {len(autres)} hors plan "
                         f"(premiers : {(manque + autres)[:3]})")


def centres_de_tache(lignes: list[dict]) -> dict:
    """m_j = médiane du log10 des coûts lisibles de la tâche, toutes conditions confondues, **sans étiquette** ; moins de 10 coûts
    lisibles : tâche sans centre (None)."""
    par_tache: dict = {}
    for l in lignes:
        par_tache.setdefault(str(l["tache"]), [])
        if cout_lisible(l["cout"]):
            par_tache[str(l["tache"])].append(math.log10(float(l["cout"])))
    return {t: (float(np.median(v)) if len(v) >= MIN_COUTS_CENTRE else None) for t, v in sorted(par_tache.items())}


def exiger_champs_permis(champs) -> None:
    interdits = sorted(set(champs) & set(CHAMPS_INTERDITS))
    if interdits:
        raise GardeArret(f"matrice de traits tirée de colonnes interdites {interdits} (T0.8, « Les douze traits ») : refus")


def traits(lignes: list[dict], centres: dict, noms=TRAITS_A) -> np.ndarray:
    """Matrice des traits nommés (codage déclaré de T0.8 : valeurs mises à 0 toujours accompagnées de leur indicateur) ; un nom de
    colonne interdite (`condition`, `dose`, `phase`, …) ou inconnu est refusé."""
    exiger_champs_permis(noms)
    inconnus = [n for n in noms if n not in TRAITS_A]
    if inconnus:
        raise GardeArret(f"traits inconnus {inconnus} : refus")
    X = np.empty((len(lignes), len(noms)))
    for i, l in enumerate(lignes):
        c, m = l["cout"], centres.get(str(l["tache"]))
        lis = cout_lisible(c)
        v = {"cout_normalise": (math.log10(float(c)) - m) if (lis and m is not None) else 0.0,
             "cout_brut": math.log10(float(c)) if lis else 0.0, "illisible": 0.0 if lis else 1.0,
             "sans_centre": 1.0 if m is None else 0.0, "longueur": math.log10(1.0 + int(l["jetons"])),
             "valide": 1.0 if bool(l["valide"]) else 0.0}
        for f in FORMES_COUT:
            v[f] = 1.0 if bool(l[f]) else 0.0
        X[i] = [v[n] for n in noms]
    return X


def mots(texte: str) -> set[str]:
    return {m for m in MOTIF_MOT.findall(texte.lower()) if any(ch.isalpha() for ch in m)}


def vocabulaire(textes) -> tuple[str, ...]:
    df = Counter(w for t in textes for w in mots(t))
    return tuple(w for w, _ in sorted(df.items(), key=lambda kv: (-kv[1], kv[0]))[:TAILLE_VOCABULAIRE])


def presence(textes, vocab) -> np.ndarray:
    index = {w: j for j, w in enumerate(vocab)}
    X = np.zeros((len(textes), len(vocab)))
    for i, t in enumerate(textes):
        for w in mots(t):
            j = index.get(w)
            if j is not None:
                X[i, j] = 1.0
    return X


def ajuster_logistique(X: np.ndarray, y: np.ndarray, lam: float = LAMBDA, options: dict | None = None) -> dict:
    """Σ pertes logistiques + (λ/2)‖w‖², ordonnée non pénalisée ; L-BFGS-B depuis zéro ; convergence jugée sur le point rendu."""
    y = np.asarray(y, dtype=np.float64)

    def objectif(theta):
        w, b = theta[:-1], theta[-1]
        z = X @ w + b
        p = np.exp(-np.logaddexp(0.0, -z))
        r = p - y
        return float(np.sum(np.logaddexp(0.0, z) - y * z) + 0.5 * lam * w @ w), np.concatenate([X.T @ r + lam * w, [r.sum()]])

    res = minimize(objectif, np.zeros(X.shape[1] + 1), jac=True, method="L-BFGS-B", options=dict(options or OPTIONS_SOLVEUR))
    g = objectif(res.x)[1]
    gmax = float(np.max(np.abs(g)))
    return {"theta": res.x, "converge": bool(np.all(np.isfinite(res.x)) and gmax <= CONVERGENCE), "gradient_max": gmax,
            "iterations": int(res.nit)}


@dataclass(frozen=True)
class ModeleBase:
    base: str
    jeu: str                      # jeu d'apprentissage (« S100 contre honnete ») : une lecture de transfert le vérifie
    colonnes: tuple
    mu: np.ndarray
    s: np.ndarray
    w: np.ndarray
    b: float
    vocab: tuple
    retires: int
    iterations: int
    gradient_max: float


class InterfaceMC(Protocol):
    """Interface déclarée du code de la pièce « mots et coût » (liée par l'adaptateur de la ligne `CODE-MOTS-ET-COUT-T06`).
    `lignes` : une ligne de `mesures-t06.npz` par action (champs de T0.8) plus `texte` (champ de `textes-actions-t06.jsonl`) ;
    `y` : 1 pour les positifs du jeu ; `centres` : rendu par `centres` sur toutes les actions des mesures ; `jeu` : nom du jeu
    d'apprentissage ; `apprendre` lève `NonCalculable` (motif) si la base ne se calcule pas ; `noter` rend un score par ligne."""
    nom: str

    def centres(self, lignes: list[dict]) -> dict: ...

    def apprendre(self, base: str, lignes: list[dict], y, centres: dict, jeu: str): ...

    def noter(self, modele, lignes: list[dict], centres: dict, jeu_lu: str) -> np.ndarray: ...


class RepliMC:
    """Implémentation de repli de MC (point 8 bis ; docstring du module)."""
    nom = "repli-bbis-v1"

    def __init__(self, options: dict | None = None):
        self.options = dict(options or OPTIONS_SOLVEUR)

    def centres(self, lignes: list[dict]) -> dict:
        return centres_de_tache(lignes)

    def _matrice(self, base: str, lignes: list[dict], centres: dict, vocab: tuple) -> np.ndarray:
        if base == BASE_A:
            return traits(lignes, centres, TRAITS_A)
        if base == BASE_B:
            return np.hstack([presence([l["texte"] for l in lignes], vocab), traits(lignes, centres, TRAITS_B)])
        raise GardeArret(f"base {base!r} inconnue")

    def apprendre(self, base: str, lignes: list[dict], y, centres: dict, jeu: str) -> ModeleBase:
        y = np.asarray(y)
        if y.shape != (len(lignes),) or len(set(y.tolist())) < 2:
            raise NonCalculable(f"base {base} ({jeu}) : une classe absente de l'apprentissage")
        vocab = ()
        if base == BASE_B:
            vocab = vocabulaire([l["texte"] for l in lignes])
            if not vocab:
                raise NonCalculable(f"base {base} ({jeu}) : vocabulaire vide")
        X = self._matrice(base, lignes, centres, vocab)
        garde = X.max(axis=0) > X.min(axis=0)                       # trait constant à l'apprentissage : écart type nul
        if not garde.any():
            raise NonCalculable(f"base {base} ({jeu}) : tous les traits retirés (écart type nul)")
        mu, s = X[:, garde].mean(axis=0), X[:, garde].std(axis=0)
        Z = (X[:, garde] - mu) / s
        r = ajuster_logistique(Z, y, LAMBDA, self.options)
        if not r["converge"]:
            raise NonCalculable(f"base {base} ({jeu}) : non convergée (gradient {r['gradient_max']:.2e} > {CONVERGENCE:g})")
        return ModeleBase(base, jeu, tuple(np.flatnonzero(garde).tolist()), mu, s, r["theta"][:-1].copy(),
                          float(r["theta"][-1]), vocab, int((~garde).sum()), r["iterations"], r["gradient_max"])

    def noter(self, modele: ModeleBase, lignes: list[dict], centres: dict, jeu_lu: str) -> np.ndarray:
        X = self._matrice(modele.base, lignes, centres, modele.vocab)[:, list(modele.colonnes)]
        s = ((X - modele.mu) / modele.s) @ modele.w + modele.b
        if not np.all(np.isfinite(s)):
            raise GardeArret(f"base {modele.base} : score non fini : arrêt")
        return s


def noter_transfert(interface, modele, lignes: list[dict], centres: dict, jeu_lu: str) -> np.ndarray:
    """Lecture de transfert : le modèle n'est pas réappris sur le jeu lu ; un modèle appris sur ce jeu est refusé."""
    if getattr(modele, "jeu", None) == jeu_lu:
        raise GardeArret(f"lecture de transfert : modèle appris sur le jeu lu ({jeu_lu}) : refus (T0.8, point 8 (vi))")
    return interface.noter(modele, lignes, centres, jeu_lu)


def charger_adaptateur(spec: str, racine: Path | None = None):
    """Adaptateur du code de la pièce, `module:attribut` (l'attribut est une classe ou une fabrique, appelée sans argument, ou
    avec `racine=` quand la racine du dépôt lu est donnée) ; il doit porter `nom`, `centres`, `apprendre` et `noter`
    (interface `InterfaceMC`), sinon refus. Lien de la pièce scellée : `controle_ia.t07bbis.lien_mots_et_cout_v1:AdaptateurPieceMC`."""
    if not isinstance(spec, str) or spec.count(":") != 1:
        raise GardeArret(f"adaptateur {spec!r} : forme module:attribut attendue")
    module, attribut = spec.split(":")
    fabrique = getattr(importlib.import_module(module), attribut)
    obj = fabrique() if racine is None else fabrique(racine=racine)
    manque = [m for m in ("nom", "centres", "apprendre", "noter") if not hasattr(obj, m)]
    if manque:
        raise GardeArret(f"adaptateur {spec} : {manque} absents de l'interface InterfaceMC : refus")
    return obj


def _instant(date: str) -> int:
    return int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def interface_retenue(lignes_registre: dict, adaptateur=None, echeance: str = ECHEANCE_CODE_PIECE) -> dict:
    """Code de la pièce si la ligne `CODE-MOTS-ET-COUT-T06` est inscrite au plus tard à l'échéance (un adaptateur lié est alors
    exigé : sinon arrêt et nœud, jamais un passage au repli) ; sinon l'implémentation de repli (réserve R-MC, sans nœud)."""
    ligne = lignes_registre.get("CODE-MOTS-ET-COUT-T06")
    if ligne is not None and int(ligne["instant"]) <= _instant(echeance):
        if adaptateur is None:
            raise GardeArret("ligne CODE-MOTS-ET-COUT-T06 inscrite avant l'échéance, mais aucun adaptateur de la pièce n'est lié "
                             "à l'interface InterfaceMC : nœud (MC ne passe pas au repli quand la ligne existe)")
        return {"interface": adaptateur, "source": "piece", "reserves": [], "ligne": dict(ligne)}
    motif = "absente" if ligne is None else f"inscrite après l'échéance ({ligne.get('date')})"
    return {"interface": RepliMC(), "source": "repli", "reserves": [RESERVE_REPLI],
            "ligne": None if ligne is None else dict(ligne), "motif_repli": f"ligne CODE-MOTS-ET-COUT-T06 {motif}"}


def decisive(aire_a, aire_b) -> str:
    """Base décisive : aire moyenne la plus haute ; ex aequo : N-029 (base (A)), convention de la pièce."""
    return BASE_B if aire_b > aire_a else BASE_A


def controle_egalite(aires_recalculees: dict, issue: dict | None, source: str) -> dict:
    """`aires_recalculees` : dose (`S25` …) → (aire de (A), aire de (B)) ; `issue` : contenu de `issue-mots-et-cout-t06.json`, ou
    None. Rend {statut, ecarts, reserves, noeud, non_calculables} (docstring du module)."""
    if issue is None:
        return {"statut": "sans contrôle d'égalité", "ecarts": {}, "reserves": [RESERVE_SANS_CONTROLE], "noeud": False,
                "non_calculables": []}
    ecarts, fautes = {}, []
    doses_issue = issue.get("doses") if isinstance(issue, dict) else None
    for dose, (aa, ab) in aires_recalculees.items():
        d = (doses_issue or {}).get(dose) or {}
        ref_a, ref_b = d.get("aire_n029"), d.get("aire_mots_et_cout")
        if ref_a is None or ref_b is None:
            fautes.append(dose)
            ecarts[dose] = None
            continue
        e = max(abs(float(aa) - float(ref_a)), abs(float(ab) - float(ref_b)))
        ecarts[dose] = e
        if not e <= TOLERANCE_EGALITE:
            fautes.append(dose)
    if not fautes:
        return {"statut": "égalité vérifiée", "ecarts": ecarts, "reserves": [], "noeud": False, "non_calculables": []}
    if source == "piece":
        return {"statut": "écart", "ecarts": ecarts, "reserves": [], "noeud": True, "non_calculables": fautes}
    return {"statut": "écart (repli)", "ecarts": ecarts, "noeud": False, "non_calculables": [],
            "reserves": [f"R-MC : aires du repli ≠ issue-mots-et-cout-t06.json aux doses {fautes}"]}


# ------------------------------------------------------------------------------------------------------------------- LEX

def lex_pli(textes_app, y_app, taches_app, plis_internes: list, textes_lus: dict, nom: str) -> dict:
    """LEX d'un pli externe : pénalité choisie par l'aire moyenne de validation interne (tâches d'apprentissage seulement), puis
    témoin réappris sur toutes les tâches d'apprentissage et noté sur les textes lus (`textes_lus` : groupe → textes)."""
    textes_app, y_app = list(textes_app), np.asarray(y_app)
    taches_app = np.asarray([str(t) for t in taches_app])
    toutes = set(taches_app.tolist())
    for p in plis_internes:
        if not set(map(str, p)) <= toutes:
            raise GardeArret("LEX : pli interne hors des tâches d'apprentissage : refus")
    aires = {}
    try:
        for pen in PENALITES_LEX:
            a = []
            for p in plis_internes:
                v = np.isin(taches_app, list(map(str, p)))
                t = temoin_lexical(nom, [x for x, k in zip(textes_app, ~v) if k], y_app[~v], pen)
                a.append(aire_sous_courbe(t.scores([x for x, k in zip(textes_app, v) if k]), y_app[v]))
            aires[pen] = float(sum(a) / len(a))
        meilleure = max(aires.values())
        penalite = max(p for p, a in aires.items() if a == meilleure)
        final = temoin_lexical(nom, textes_app, y_app, penalite)
        scores = {k: final.scores(list(v)) for k, v in textes_lus.items()}
    except GardeArret as e:
        raise NonCalculable(f"LEX : {e}") from None
    return {"penalite": penalite, "empreinte": final.empreinte(), "scores": scores}


__all__ = ["RepliMC", "InterfaceMC", "ModeleBase", "interface_retenue", "charger_adaptateur", "noter_transfert", "decisive",
           "controle_egalite", "centres_de_tache", "traits", "vocabulaire", "presence", "ajuster_logistique", "cout_lisible",
           "exiger_effectifs", "exiger_champs_permis", "exiger_module_gele", "lex_pli", "BASE_A", "BASE_B", "RESERVE_REPLI",
           "RESERVE_SANS_CONTROLE", "ECHEANCE_CODE_PIECE", "TRAITS_A", "TRAITS_B", "PENALITES_LEX"]
