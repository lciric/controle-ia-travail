"""Appel de la pièce inscrite « mots et coût » par la lecture (2) de (ii-b), v1. EXPLORATOIRE, NON OPPOSABLE (R-522).

Décision de Lazar (GO-2026-11-18-56, point 4), recommandation (A) du relevé `docs/notes/barreau8-iib-v1/
releve-code-des-deux-bases-v1.md` : les deux bases textuelles de la lecture (2) — le prédicteur sur les traits du texte (base (A))
et la base « mots et coût » (base (B)) — sont calculées par **la pièce inscrite**, `scripts/mots_et_cout_t06_v3.py`, par les six
fonctions de son contrat (`centres`, `apprendre_a`, `noter_a`, `etat_a`, `apprendre_b`, `noter_b`). Ce module ne recopie aucune
fonction de la pièce et ne touche aucun de ses réglages (solveur, pénalité, découpage des mots, vocabulaire, seuil des centres) :
il la charge, la garde et lui passe des actions.

Gardes de ce module (chacune avec un essai sain et un artefact, `tests/test_iib_lectures_v1.py`, section du portage) :
- la pièce est chargée **par son chemin**, et seulement si l'empreinte du fichier est celle de l'inscription (`PIECE_SHA256`) ;
  fichier absent ou empreinte différente : arrêt (R11), rien n'est calculé ;
- les six fonctions du contrat existent ;
- les modules gelés dont dépend la pièce sont à leurs empreintes (`verifier_modules_geles` de la pièce, appelée ici parce que la
  pièce ne l'applique qu'à sa propre exécution) ;
- fils de calcul fixés à 1 en mode réel (les trois variables de la pièce), sinon refus avant tout calcul ; en mode jouet, l'état
  des trois variables est seulement rapporté ;
- champs des actions : la pièce ne reçoit que la tâche, le coût, le nombre de jetons, la validité, les six formes du champ du
  coût et le texte ; toute autre clé (condition, dose, phase, épisode, pas…) : arrêt ;
- plis mêlés : une tâche présente à la fois à l'apprentissage et à la notation d'un même modèle : arrêt ;
- lecture de transfert : un modèle ne note que le jeu (paire de conditions) sur lequel il a appris ; un modèle appris sur un jeu
  et présenté à la notation d'un autre jeu, des actions lues d'une condition hors du jeu, ou un modèle que ce chargeur n'a pas
  appris : arrêt (la lecture de la diffusion n'a aucun jeu de transfert ; la garde refuse s'il s'en présente un) ;
- état d'une unité de lecture : rendu par la fonction d'état inscrite de la pièce (`etat_dose` : base décisive = plus haute aire,
  la base (A) à égalité ; « non calculable » si l'une des deux bases ne se calcule pas ; seuil d'aire et plancher de la pièce),
  jamais par une règle de ce paquet ; les lectures passées à cette fonction sont exigées entières et finies ;
- centres : calculés une seule fois par la pièce, passés tels quels ; une tâche sans entrée de centre : arrêt (garde de la pièce).
Un arrêt de la pièce (`ArretPiece`) ou d'une garde de ce module est un **arrêt de la lecture** (`ArretBaseTextuelle`), jamais un
état « non calculable ». Un modèle que la pièce déclare elle-même non calculable (classe absente, traits tous constants,
vocabulaire vide, non convergé au point rendu) est rendu tel quel, avec son motif : c'est la lecture qui en fait l'état « non
calculable ». Aucun repli : ce module n'a aucune autre méthode d'ajustement.

Aucun aléa (départ du solveur à zéro, dans la pièce) : aucune graine n'est tirée ici (R9 : les graines de la lecture restent les
clés `iib/lecture-2/…` du manifeste de la course). Aucune activation, aucune sonde ; aucune moyenne ni médiane sur des jetons (la
seule médiane est celle de la pièce : le centre d'une tâche, sur les coûts lisibles des actions).
"""
from __future__ import annotations

import hashlib
import importlib.util
import os
import sys
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..t06.cout import cout_action

PIECE_CHEMIN = "scripts/mots_et_cout_t06_v3.py"
PIECE_SHA256 = "9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674"
PIECE_INSCRIPTION = "CODE-MOTS-ET-COUT-T06 (commit da06bb57610f840152e4e9a8c449b036577cc582)"
CONTRAT = ("centres", "apprendre_a", "noter_a", "etat_a", "apprendre_b", "noter_b")
FONCTION_D_ETAT = "etat_dose"                                   # règle de lecture inscrite : état d'une unité (deux bases)
CLES_LECTURE = ("aire", "bas", "haut", "quantile_plancher")       # ce que la lecture passe à la fonction d'état, par base
FILS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")
BASES = ("a", "b")
_NOM_MODULE = "controle_ia_piece_mots_et_cout_t06_v3_"            # suivi des douze premiers caractères de l'empreinte chargée
_CACHE: dict = {}


class ArretBaseTextuelle(GardeArret):
    """Arrêt de la lecture : garde de ce module ou arrêt de la pièce. Jamais converti en « non calculable »."""


def racine_du_code() -> Path:
    """Racine du dépôt qui porte ce module (`src/controle_ia/iib/` → trois niveaux plus haut)."""
    return Path(__file__).resolve().parents[3]


def _sha256(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def exiger_fils(mode: str, environnement: dict | None = None) -> dict:
    """Fils de calcul : en mode réel, les trois variables valent « 1 » (reproductibilité des sommes, règle de la pièce), sinon
    refus avant tout calcul. Rend l'état lu des trois variables (rapporté dans la sortie de la lecture)."""
    env = os.environ if environnement is None else environnement
    fils = {k: env.get(k) for k in FILS}
    if mode == "reel" and any(v != "1" for v in fils.values()):
        raise ArretBaseTextuelle(f"mode réel : fils de calcul non fixés à 1 ({fils}) : poser {', '.join(FILS)} à 1 avant de lancer "
                                 "la lecture (reproductibilité des sommes, règle de la pièce inscrite)")
    if mode not in ("reel", "jouet"):
        raise ArretBaseTextuelle(f"mode {mode!r} inconnu (reel ou jouet)")
    return fils


def charger_piece(racine=None, sha256: str = PIECE_SHA256, chemin: str = PIECE_CHEMIN, table_geles: dict | None = None):
    """Charge la pièce inscrite par son chemin, après contrôle de son empreinte ; vérifie le contrat et les modules gelés.
    Rend (module de la pièce, fiche {chemin, sha256, inscription, modules_geles}). `table_geles` : essais seulement."""
    racine = racine_du_code() if racine is None else Path(racine)
    fichier = (racine / chemin).resolve()
    if not fichier.is_file():
        raise ArretBaseTextuelle(f"pièce inscrite absente sur disque : {fichier} (R11) : aucune base textuelle n'est calculée")
    sha = _sha256(fichier)
    if sha != sha256:
        raise ArretBaseTextuelle(f"pièce {chemin} : empreinte {sha[:12]}… ≠ empreinte inscrite {sha256[:12]}… (R11) : "
                                 "aucune base textuelle n'est calculée")
    cle = (str(fichier), sha)
    if cle not in _CACHE:
        nom = _NOM_MODULE + sha[:12]
        spec = importlib.util.spec_from_file_location(nom, fichier)
        module = importlib.util.module_from_spec(spec)
        ancien, sys.dont_write_bytecode = sys.dont_write_bytecode, True       # rien d'écrit à côté de la pièce
        sys.modules[nom] = module
        try:
            spec.loader.exec_module(module)
        except BaseException:
            sys.modules.pop(nom, None)
            raise
        finally:
            sys.dont_write_bytecode = ancien
        _CACHE[cle] = module
    piece = _CACHE[cle]
    manquantes = [n for n in CONTRAT + (FONCTION_D_ETAT, "verifier_modules_geles", "ArretPiece") if not callable(getattr(piece, n, None))]
    if manquantes:
        raise ArretBaseTextuelle(f"pièce {chemin} : fonction(s) du contrat absente(s) : {manquantes}")
    try:
        geles = piece.verifier_modules_geles(table=table_geles)
    except piece.ArretPiece as e:
        raise ArretBaseTextuelle(f"pièce inscrite : {e}") from e
    return piece, {"chemin": chemin, "sha256": sha, "inscription": PIECE_INSCRIPTION, "modules_geles": geles}


def champs_permis(piece) -> tuple:
    """Clés d'une action passée à la pièce : ses colonnes d'entrée de la base (A), et le texte pour la base (B)."""
    return tuple(piece.ENTREES_A) + ("texte",)


def action_pour_la_piece(tache: str, texte: str, jetons: int) -> dict:
    """Une action sous la forme que lit le contrat de la pièce : coût, validité et six formes du champ du coût lus sur le texte
    par le lecteur gelé `t06.cout.cout_action` (celui des deux chaînes d'origine) ; `jetons` : nombre d'identifiants générés,
    compté par la course."""
    if isinstance(jetons, bool) or not isinstance(jetons, (int, np.integer)) or int(jetons) < 0:
        raise ArretBaseTextuelle(f"nombre de jetons générés {jetons!r} : entier positif ou nul attendu")
    return {"tache": str(tache), "jetons": int(jetons), "texte": str(texte), **cout_action(str(texte))}


def exiger_champs(actions: list, piece) -> None:
    """Chaque action passée à la pièce porte exactement les champs permis ; un champ interdit par la pièce (condition, dose,
    phase, épisode, clé, pas, mentions…) ou tout autre champ : arrêt. La pièce ignore les clés en trop (`_colonnes_actions`) :
    cette garde est donc celle de l'appelant."""
    permis = set(champs_permis(piece))
    for k, a in enumerate(actions):
        cles = set(a)
        interdits = sorted(cles & set(piece.INTERDITES_ENTREE))
        if interdits:
            raise ArretBaseTextuelle(f"action {k} : champ(s) interdit(s) {interdits} passé(s) à la pièce : arrêt")
        if cles != permis:
            raise ArretBaseTextuelle(f"action {k} : champs {sorted(cles)} ≠ champs permis {sorted(permis)} : arrêt")


def exiger_plis_disjoints(apprentissage: list, lues: list) -> None:
    """Aucune tâche à la fois à l'apprentissage et à la notation d'un même modèle (plis mêlés) : sinon arrêt."""
    communes = sorted({a["tache"] for a in apprentissage} & {a["tache"] for a in lues})
    if communes:
        raise ArretBaseTextuelle(f"plis mêlés : {len(communes)} tâche(s) à la fois à l'apprentissage et à la notation "
                                 f"(première : {communes[0]!r}) : arrêt")


def exiger_aucun_transfert(jeu_appris, jeu_lu, conditions_lues) -> None:
    """Lecture de transfert : le jeu noté est celui sur lequel le modèle a appris, et les actions lues sont de ses seules
    conditions ; sinon arrêt. `jeu_appris` : `None` si le modèle n'a pas été appris par ce chargeur."""
    if jeu_appris is None:
        raise ArretBaseTextuelle("lecture de transfert : modèle d'origine inconnue (il n'a pas été appris par ce chargeur) : arrêt")
    if tuple(jeu_lu) != tuple(jeu_appris):
        raise ArretBaseTextuelle(f"lecture de transfert : modèle appris sur le jeu {tuple(jeu_appris)} présenté à la notation "
                                 f"du jeu {tuple(jeu_lu)} : aucun jeu de transfert n'est permis : arrêt")
    hors = sorted(set(conditions_lues) - set(jeu_appris))
    if hors:
        raise ArretBaseTextuelle(f"lecture de transfert : actions lues de condition(s) {hors} hors du jeu appris "
                                 f"{tuple(jeu_appris)} : arrêt")


def exiger_jeu(jeu) -> tuple:
    if not (isinstance(jeu, (tuple, list)) and len(jeu) == 2 and all(isinstance(c, str) and c for c in jeu) and jeu[0] != jeu[1]):
        raise ArretBaseTextuelle(f"jeu {jeu!r} : une paire (positifs, négatifs) de deux conditions distinctes est attendue")
    return tuple(jeu)


class Bases:
    """Les deux bases textuelles, par les fonctions du contrat de la pièce inscrite, sous les gardes de ce module."""

    def __init__(self, mode: str, racine=None, sha256: str = PIECE_SHA256, table_geles: dict | None = None,
                 environnement: dict | None = None):
        self.fils = exiger_fils(mode, environnement)
        if mode == "reel" and (sha256 != PIECE_SHA256 or table_geles is not None):
            raise ArretBaseTextuelle("mode réel : options d'essai (empreinte de la pièce, table des modules gelés) refusées")
        self.piece, self.fiche = charger_piece(racine, sha256, table_geles=table_geles)
        self.mode = mode
        self._jeu_des_modeles: dict = {}                          # id du modèle → (modèle, jeu appris) : garde de transfert

    def rapport(self) -> dict:
        """Ce que la sortie de la lecture consigne : pièce, modules gelés, fils, réglages lus dans la pièce, versions."""
        import scipy
        p = self.piece
        return {"piece": self.fiche, "contrat": list(CONTRAT), "fils_de_calcul": self.fils, "mode": self.mode,
                "reglages_de_la_piece": {"base_a": dict(p.REGLAGES_A), "base_b": dict(p.REGLAGES_B),
                                         "lisibles_min_centre": p.LISIBLES_MIN_CENTRE, "traits_a": list(p.TRAITS_A)},
                "versions": {"numpy": np.__version__, "scipy": scipy.__version__}}

    def _appeler(self, nom: str, *args, **kwargs):
        try:
            return getattr(self.piece, nom)(*args, **kwargs)
        except self.piece.ArretPiece as e:
            raise ArretBaseTextuelle(f"pièce inscrite ({nom}) : {e}") from e

    def centres(self, actions: list) -> dict:
        """Centres de tâche, une seule fois, sur les actions données (sans étiquette), par la pièce."""
        exiger_champs(actions, self.piece)
        return self._appeler("centres", actions)

    def apprendre(self, base: str, actions: list, y, centres: dict, maxiter: int | None = None, *, jeu) -> dict:
        """Modèle de la base (« a » ou « b ») sur les seules actions d'apprentissage du jeu `jeu` (positifs, négatifs), que la
        garde de transfert retient pour ce modèle. `maxiter` : essais seulement (le contrat de la pièce l'offre) ; refusé en
        mode réel."""
        jeu = exiger_jeu(jeu)
        if base not in BASES:
            raise ArretBaseTextuelle(f"base {base!r} inconnue ({BASES})")
        if maxiter is not None and self.mode == "reel":
            raise ArretBaseTextuelle("mode réel : option d'essai maxiter refusée (réglage de la pièce)")
        exiger_champs(actions, self.piece)
        y = np.asarray(y)
        if y.shape != (len(actions),):
            raise ArretBaseTextuelle(f"{len(actions)} actions d'apprentissage, étiquettes de forme {y.shape}")
        modele = self._appeler(f"apprendre_{base}", actions, y, centres, maxiter)
        self._jeu_des_modeles[id(modele)] = (modele, jeu)
        return modele

    def noter(self, base: str, modele: dict, actions: list, centres: dict, apprentissage: list | None = None, *, jeu,
              conditions) -> np.ndarray:
        """Scores des actions lues par un modèle calculable. `apprentissage` : les actions qui ont appris ce modèle, pour la
        garde des plis mêlés (omis seulement pour noter les actions d'apprentissage elles-mêmes, seuil du taux à 1 %). `jeu` :
        le jeu noté ; `conditions` : la condition de chaque action lue (jamais passée à la pièce) ; garde de transfert."""
        connu = self._jeu_des_modeles.get(id(modele))
        exiger_aucun_transfert(connu[1] if connu is not None and connu[0] is modele else None, exiger_jeu(jeu), conditions)
        if len(conditions) != len(actions):
            raise ArretBaseTextuelle(f"{len(actions)} actions lues, {len(conditions)} conditions")
        if base not in BASES:
            raise ArretBaseTextuelle(f"base {base!r} inconnue ({BASES})")
        if not modele.get("calculable"):
            raise ArretBaseTextuelle(f"modèle non calculable ({modele.get('motif')}) : aucun score n'est demandé à la pièce")
        exiger_champs(actions, self.piece)
        if apprentissage is not None:
            exiger_plis_disjoints(apprentissage, actions)
        s = np.asarray(self._appeler(f"noter_{base}", modele, actions, centres), dtype=np.float64)
        if s.shape != (len(actions),) or not np.all(np.isfinite(s)):
            raise ArretBaseTextuelle(f"scores de la pièce de forme {s.shape} ou non finis pour {len(actions)} actions")
        return s

    def lecture_pour_l_etat(self, jeu_rendu: dict) -> dict:
        """Lecture d'une base sur une unité, sous la forme que lit la fonction d'état de la pièce : `calculable`, et, si elle se
        calcule, aire moyenne, bornes de l'intervalle et quantile du plancher, exigés présents et finis (sinon arrêt)."""
        if jeu_rendu.get("etat") == "non calculable":
            return {"calculable": False, "motif": jeu_rendu.get("motif")}
        try:
            v = {"aire": jeu_rendu["aire"]["aire"], "bas": jeu_rendu["intervalle"]["bas"], "haut": jeu_rendu["intervalle"]["haut"],
                 "quantile_plancher": jeu_rendu["plancher"]["quantile"]}
        except (KeyError, TypeError) as e:
            raise ArretBaseTextuelle(f"lecture d'une base incomplète pour la fonction d'état de la pièce ({e!r}) : arrêt") from e
        for k in CLES_LECTURE:
            if isinstance(v[k], bool) or not isinstance(v[k], (int, float)) or not np.isfinite(v[k]):
                raise ArretBaseTextuelle(f"lecture d'une base : {k} = {v[k]!r} n'est pas un nombre fini : arrêt")
        return {"calculable": True, "aire": float(v["aire"]), "bas": float(v["bas"]), "haut": float(v["haut"]),
                "plancher": {"quantile": float(v["quantile_plancher"])}}

    def etat_unite(self, base_a: dict, base_b: dict, permutations: int) -> dict:
        """État d'une unité de lecture, par la fonction d'état inscrite de la pièce (`etat_dose`), telle quelle : `base_a` et
        `base_b` sont les jeux rendus par la lecture pour la base (A) et la base (B) sur la même unité. Aucune règle d'état
        n'est appliquée ici. Rend le dictionnaire de la pièce (état, base décisive sous les noms de la pièce, aires, bornes)."""
        ra, rb = self.lecture_pour_l_etat(base_a), self.lecture_pour_l_etat(base_b)
        r = self._appeler(FONCTION_D_ETAT, ra, rb, None, int(permutations))
        if r.get("etat") not in ("réussit", "échoue", "non calculable"):
            raise ArretBaseTextuelle(f"fonction d'état de la pièce : état {r.get('etat')!r} inattendu : arrêt")
        return r
