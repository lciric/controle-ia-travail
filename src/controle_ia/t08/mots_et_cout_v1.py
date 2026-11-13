"""M2 (base (A), texte scellé `prereg/T0.8-base-A-mots-et-cout-v1.md`) et MC (base (B) de T0.6) par le code de la pièce
« mots et coût » de T0.6, sans changement de trait ni de réglage (« Métrique », M2 et MC ; plan, point 10).

Le code de la pièce n'existe pas à la date de ce module (chantier de T0.6 ; ligne `CODE-MOTS-ET-COUT-T06` à inscrire).
Ce module fixe donc **ce que T0.8 demande à la pièce** (contrat `CONTRAT`), et l'appelle par une enveloppe
(`Piece`) qui :
- ne lui passe jamais la condition, la dose, la phase, l'épisode, le rang du pas, les mentions ni `cibles` (garde
  `exiger_champs_permis`) : la condition ne sert qu'à former les jeux et les étiquettes, passées à part ;
- attache à chaque modèle appris son jeu, son pli lu, ses tâches et ses épisodes d'apprentissage (`ModeleAppris`), pour
  les gardes de la lecture de transfert (un modèle réappris sur le jeu lu est refusé) et de la lecture descriptive des
  épisodes de la pièce HD (aucun modèle appris sur eux) ;
- en mode réel, charge le module cité par le marqueur `CODE_MOTS_ET_COUT_T06` à son empreinte, et refuse le module jouet.

`controle_identite_m2` : centres égaux (mêmes tâches sans centre), mêmes traits retirés et même état de convergence par
(jeu, pli), coefficients et ordonnée à 1·10⁻⁶ près en valeur absolue, contre `base-a-t08.json` ; sinon arrêt, rien n'est
écrit (erreur de chaîne, ligne D1).

`PieceJouet` : implémentation pour les essais seulement (données factices). Base (A) : celle du texte scellé (douze
traits, régression logistique λ = 1, L-BFGS-B, `ftol` = 0, `gtol` = 1·10⁻⁸, convergence par gradient ≤ 1·10⁻⁴).
Base (B) : **jouet** (sac de mots binaire de 1 000 mots au plus, coût normalisé, illisibilité, unité présente ; λ = 1) :
les réglages ouverts de la base (B) appartiennent au code de la pièce, non à T0.8 ; elle ne vaut pour aucune lecture.
"""
from __future__ import annotations

import hashlib
import importlib
import math
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from scipy import optimize

from ..gardes import GardeArret
from ..scellement import empreinte
from ..t06.cout import cout_lisible

CONTRAT = ("centres", "apprendre_a", "noter_a", "etat_a", "apprendre_b", "noter_b")
CHAMPS_PERMIS = ("cle", "tache", "jetons", "cout", "valide", "cout_present", "cout_plusieurs_nombres",
                 "cout_multiplication", "cout_intervalle", "cout_suffixe_k", "cout_milliers_espace", "texte")
CHAMPS_INTERDITS = ("condition", "dose", "phase", "episode", "pas", "mention", "mention_etendue", "jetons_notes",
                    "cibles", "adaptateur", "empreinte_adaptateurs")
TRAITS_A = ("cout_normalise", "cout_brut", "illisible", "sans_centre", "longueur", "valide", "cout_present",
            "cout_plusieurs_nombres", "cout_multiplication", "cout_intervalle", "cout_suffixe_k", "cout_milliers_espace")
FORME_COUT = TRAITS_A[6:]
TOLERANCE_IDENTITE = 1e-6
REGLAGES_A = {"lambda": 1.0, "methode": "L-BFGS-B", "gtol": 1e-8, "ftol": 0.0, "maxcor": 10, "maxls": 20,
              "maxfun": 15000, "maxiter": 1000, "convergence": 1e-4, "lisibles_min_centre": 10}


def exiger_champs_permis(actions: list[dict]) -> None:
    for k, a in enumerate(actions):
        interdits = sorted(set(a) & set(CHAMPS_INTERDITS))
        if interdits:
            raise GardeArret(f"action {k} passée à la pièce avec {interdits} : un surveillant ne reçoit ni condition, "
                             "ni dose, ni phase, ni cibles (liste d'arrêt) : arrêt")
        autres = sorted(set(a) - set(CHAMPS_PERMIS))
        if autres:
            raise GardeArret(f"action {k} passée à la pièce avec des champs hors liste : {autres}")


def projeter_action(ligne: dict, texte: str | None = None) -> dict:
    a = {k: ligne[k] for k in CHAMPS_PERMIS if k in ligne and k != "texte"}
    if texte is not None:
        a["texte"] = texte
    return a


@dataclass
class ModeleAppris:
    base: str                       # « A » (M2) ou « B » (MC)
    jeu: str                        # condition positive du jeu « X contre H »
    pli_lu: int
    taches_apprentissage: tuple
    episodes_apprentissage: tuple
    interne: dict = field(default_factory=dict)

    @property
    def calculable(self) -> bool:
        return bool(self.interne.get("calculable"))


class Piece:
    """Enveloppe du code de la pièce « mots et coût » (contrat `CONTRAT`) : gardes de T0.8, aucun réglage changé."""

    def __init__(self, module, nom: str, mode: str):
        manquantes = [f for f in CONTRAT if not callable(getattr(module, f, None))]
        if manquantes:
            raise GardeArret(f"pièce {nom} : fonctions du contrat absentes {manquantes}")
        if mode == "reel" and getattr(module, "PIECE_JOUET", False):
            raise GardeArret("mode réel : la pièce jouet est refusée (code cité par CODE-MOTS-ET-COUT-T06 exigé)")
        self.module, self.nom, self.mode = module, nom, mode

    def centres(self, actions: list[dict]) -> dict:
        exiger_champs_permis(actions)
        return dict(self.module.centres([{"tache": a["tache"], "cout": a["cout"]} for a in actions]))

    def apprendre(self, base: str, jeu: str, pli_lu: int, actions: list[dict], y, centres: dict,
                  episodes: list[str]) -> ModeleAppris:
        exiger_champs_permis(actions)
        y = np.asarray(y, dtype=int)
        if y.size != len(actions):
            raise GardeArret("étiquettes et actions de tailles différentes")
        f = self.module.apprendre_a if base == "A" else self.module.apprendre_b if base == "B" else None
        if f is None:
            raise GardeArret(f"base {base!r} inconnue")
        interne = f(actions, y, centres)
        return ModeleAppris(base, jeu, int(pli_lu), tuple(sorted({a["tache"] for a in actions})), tuple(sorted(set(episodes))),
                            interne)

    def noter(self, modele: ModeleAppris, actions: list[dict], centres: dict) -> np.ndarray:
        exiger_champs_permis(actions)
        if not modele.calculable:
            raise GardeArret(f"modèle ({modele.base}, {modele.jeu}, pli {modele.pli_lu}) non calculable : aucun score")
        apprises = set(modele.taches_apprentissage) & {a["tache"] for a in actions}
        if apprises:
            raise GardeArret(f"notation de tâches d'apprentissage du modèle ({sorted(apprises)[:3]}) : plis mêlés")
        f = self.module.noter_a if modele.base == "A" else self.module.noter_b
        s = np.asarray(f(modele.interne, actions, centres), dtype=float)
        if s.shape != (len(actions),) or not np.all(np.isfinite(s)):
            raise GardeArret("score par action non fini ou de forme inattendue : arrêt")
        return s

    def noter_transfert(self, modele: ModeleAppris, jeu_appris_attendu: str, actions: list[dict], centres: dict) -> np.ndarray:
        """Lecture de transfert (P8-8 ; « Épisodes du témoin distillé honnête ») : le modèle appris sur
        « `jeu_appris_attendu` contre H » note des actions d'un autre jeu, sans réapprentissage. Un modèle appris sur
        un autre jeu (par exemple réappris sur T100 contre H) est refusé."""
        if modele.jeu != jeu_appris_attendu:
            raise GardeArret(f"lecture de transfert : modèle appris sur {modele.jeu!r}, {jeu_appris_attendu!r} attendu "
                             "(aucun réapprentissage sur le jeu lu) : refusé")
        return self.noter(modele, actions, centres)

    def etat_a(self, modele: ModeleAppris) -> dict:
        """État de M2 comparé à `base-a-t08.json` : calculable, motif, traits retirés, convergence, coefficients,
        ordonnée (sur traits réduits)."""
        return dict(self.module.etat_a(modele.interne))


def charger_piece(mode: str, marqueur: dict | None = None, racine=".") -> Piece:
    """Mode réel : module cité par `CODE_MOTS_ET_COUT_T06` ({commit, module, sha256}), fichier à son empreinte.
    Mode jouet : `PieceJouet` (ce module)."""
    if mode == "jouet":
        import sys

        return Piece(sys.modules[__name__], "jouet", "jouet")
    if not isinstance(marqueur, dict) or not all(k in marqueur for k in ("module", "sha256", "commit")):
        raise GardeArret("pièce « mots et coût » : marqueur CODE_MOTS_ET_COUT_T06 absent : aucune lecture en mode réel")
    module = importlib.import_module(marqueur["module"])
    chemin = Path(module.__file__)
    sha = empreinte(chemin)
    if sha != marqueur["sha256"]:
        raise GardeArret(f"pièce « mots et coût » : {chemin.name} {sha[:12]}… ≠ empreinte citée {marqueur['sha256'][:12]}…")
    return Piece(module, marqueur["module"], mode)


# --- contrôle d'identité de M2 --------------------------------------------------------------------------------------

def controle_identite_m2(centres: dict, etats: dict, base_a: dict, jeux_plis: list[tuple[str, int]]) -> dict:
    """`centres` recalculés ; `etats[(jeu, pli)]` = `Piece.etat_a` recalculé ; `base_a` = projection de
    `base-a-t08.json`. Toute différence arrête (rien n'est écrit par l'appelant)."""
    ref = base_a["centres"]
    if set(ref) != set(centres):
        raise GardeArret(f"contrôle d'identité de M2 : tâches des centres différentes ({sorted(set(ref) ^ set(centres))[:3]})")
    for t in sorted(ref):
        a, b = ref[t], centres[t]
        if (a is None) != (b is None) or (a is not None and float(a) != float(b)):
            raise GardeArret(f"contrôle d'identité de M2 : centre de la tâche {t} {b!r} ≠ {a!r} de base-a-t08.json")
    ecarts = []
    for jeu, pli in jeux_plis:
        m = base_a["modeles"].get(jeu, {}).get(str(pli))
        if m is None:
            raise GardeArret(f"contrôle d'identité de M2 : ({jeu}, pli {pli}) absent de base-a-t08.json")
        e = etats[(jeu, pli)]
        if bool(m["calculable"]) != bool(e["calculable"]):
            raise GardeArret(f"contrôle d'identité de M2 : ({jeu}, pli {pli}) calculable {e['calculable']} ≠ {m['calculable']}")
        if list(m["traits_retires"]) != list(e["traits_retires"]):
            raise GardeArret(f"contrôle d'identité de M2 : ({jeu}, pli {pli}) traits retirés {e['traits_retires']} ≠ "
                             f"{m['traits_retires']}")
        if bool(m["convergence"].get("converge")) != bool(e["convergence"].get("converge")):
            raise GardeArret(f"contrôle d'identité de M2 : ({jeu}, pli {pli}) état de convergence différent")
        if not m["calculable"]:
            continue
        if set(m["coefficients"]) != set(e["coefficients"]):
            raise GardeArret(f"contrôle d'identité de M2 : ({jeu}, pli {pli}) traits des coefficients différents")
        for k in m["coefficients"]:
            d = abs(float(m["coefficients"][k]) - float(e["coefficients"][k]))
            ecarts.append(d)
            if not d <= TOLERANCE_IDENTITE:
                raise GardeArret(f"contrôle d'identité de M2 : ({jeu}, pli {pli}) coefficient {k} écart {d:.3g} > 1e-6")
        d = abs(float(m["ordonnee"]) - float(e["ordonnee"]))
        ecarts.append(d)
        if not d <= TOLERANCE_IDENTITE:
            raise GardeArret(f"contrôle d'identité de M2 : ({jeu}, pli {pli}) ordonnée écart {d:.3g} > 1e-6")
    return {"conforme": True, "jeux_plis": len(jeux_plis), "ecart_max": max(ecarts) if ecarts else 0.0,
            "tolerance": TOLERANCE_IDENTITE}


# --- pièce jouet (essais seulement) ----------------------------------------------------------------------------------

PIECE_JOUET = True


def centres(actions: list[dict]) -> dict:
    """Médiane du log10 du coût lisible sur toutes les actions de la tâche, sans étiquette ; < 10 lisibles : sans centre."""
    par = {}
    for a in actions:
        par.setdefault(str(a["tache"]), [])
        if cout_lisible(a["cout"]):
            par[str(a["tache"])].append(math.log10(float(a["cout"])))
    return {t: (float(np.median(v)) if len(v) >= REGLAGES_A["lisibles_min_centre"] else None) for t, v in sorted(par.items())}


def _cout(a) -> float | None:
    c = a["cout"]
    if c is None or (isinstance(c, float) and math.isnan(c)):
        return None
    return float(c) if cout_lisible(float(c)) else None


def traits_a(actions: list[dict], centres_: dict) -> np.ndarray:
    X = np.zeros((len(actions), len(TRAITS_A)))
    for i, a in enumerate(actions):
        c, m = _cout(a), centres_.get(str(a["tache"]))
        brut = math.log10(c) if c is not None else 0.0
        X[i] = [brut - m if (c is not None and m is not None) else 0.0, brut, float(c is None), float(m is None),
                math.log10(1 + int(a["jetons"])), float(bool(a["valide"]))] + [float(bool(a[k])) for k in FORME_COUT]
    return X


def _ajuster(X: np.ndarray, y: np.ndarray, noms: tuple, maxiter: int | None = None) -> dict:
    y = np.asarray(y, dtype=float)
    if len(set(y.tolist())) < 2:
        return {"calculable": False, "motif": "classe absente du pli d'apprentissage", "traits_retires": [],
                "convergence": {"converge": False, "gradient_max": None, "iterations": 0}, "coefficients": {},
                "ordonnee": None, "moyennes": {}, "ecarts": {}, "noms": list(noms)}
    mu, sd = X.mean(axis=0), X.std(axis=0, ddof=0)
    garde = sd > 0
    retires = [n for n, g in zip(noms, garde) if not g]
    if not garde.any():
        return {"calculable": False, "motif": "tous les traits retirés", "traits_retires": retires,
                "convergence": {"converge": False, "gradient_max": None, "iterations": 0}, "coefficients": {},
                "ordonnee": None, "moyennes": {}, "ecarts": {}, "noms": list(noms)}
    Z = (X[:, garde] - mu[garde]) / sd[garde]
    lam = REGLAGES_A["lambda"]

    def objectif(p):
        w, b = p[:-1], p[-1]
        s = Z @ w + b
        perte = np.sum(np.logaddexp(0.0, s) - y * s) + 0.5 * lam * float(w @ w)
        r = 1.0 / (1.0 + np.exp(-s)) - y
        return perte, np.concatenate([Z.T @ r + lam * w, [r.sum()]])

    res = optimize.minimize(objectif, np.zeros(Z.shape[1] + 1), jac=True, method="L-BFGS-B",
                            options={"gtol": REGLAGES_A["gtol"], "ftol": REGLAGES_A["ftol"], "maxcor": REGLAGES_A["maxcor"],
                                     "maxls": REGLAGES_A["maxls"], "maxfun": REGLAGES_A["maxfun"],
                                     "maxiter": int(maxiter if maxiter is not None else REGLAGES_A["maxiter"])})
    g = float(np.max(np.abs(objectif(res.x)[1])))
    converge = g <= REGLAGES_A["convergence"]
    gardes = [n for n, k in zip(noms, garde) if k]
    return {"calculable": bool(converge), "motif": None if converge else f"non convergé (gradient {g:.3g} > 1e-4)",
            "traits_retires": retires, "convergence": {"converge": bool(converge), "gradient_max": g, "iterations": int(res.nit)},
            "coefficients": {n: float(v) for n, v in zip(gardes, res.x[:-1])}, "ordonnee": float(res.x[-1]),
            "moyennes": {n: float(mu[i]) for i, n in enumerate(noms) if garde[i]},
            "ecarts": {n: float(sd[i]) for i, n in enumerate(noms) if garde[i]}, "noms": list(noms)}


def _noter(interne: dict, X: np.ndarray) -> np.ndarray:
    noms = interne["noms"]
    s = np.full(X.shape[0], float(interne["ordonnee"]))
    for j, n in enumerate(noms):
        if n in interne["coefficients"]:
            s += interne["coefficients"][n] * (X[:, j] - interne["moyennes"][n]) / interne["ecarts"][n]
    return s


def apprendre_a(actions: list[dict], y, centres_: dict, maxiter: int | None = None) -> dict:
    return _ajuster(traits_a(actions, centres_), np.asarray(y), TRAITS_A, maxiter)


def noter_a(interne: dict, actions: list[dict], centres_: dict) -> np.ndarray:
    return _noter(interne, traits_a(actions, centres_))


def etat_a(interne: dict) -> dict:
    return {k: interne[k] for k in ("calculable", "motif", "traits_retires", "convergence", "coefficients", "ordonnee",
                                    "moyennes", "ecarts")}


_MOT = re.compile(r"[a-z]+")


def _sac(actions: list[dict], vocabulaire: list[str]) -> np.ndarray:
    index = {w: i for i, w in enumerate(vocabulaire)}
    X = np.zeros((len(actions), len(vocabulaire)))
    for i, a in enumerate(actions):
        for w in set(_MOT.findall(str(a.get("texte", "")).lower())):
            if w in index:
                X[i, index[w]] = 1.0
    return X


def _traits_b(actions, centres_, vocabulaire):
    A = traits_a(actions, centres_)
    return np.hstack([_sac(actions, vocabulaire), A[:, [0, 2, 6]]])


def apprendre_b(actions: list[dict], y, centres_: dict) -> dict:
    compte = {}
    for a in actions:
        for w in set(_MOT.findall(str(a.get("texte", "")).lower())):
            compte[w] = compte.get(w, 0) + 1
    vocabulaire = [w for w, _ in sorted(compte.items(), key=lambda x: (-x[1], x[0]))[:1000]]
    if not vocabulaire:
        return {"calculable": False, "motif": "vocabulaire vide", "vocabulaire": []}
    noms = tuple(f"mot:{w}" for w in vocabulaire) + ("cout_normalise", "illisible", "cout_present")
    interne = _ajuster(_traits_b(actions, centres_, vocabulaire), np.asarray(y), noms)
    interne["vocabulaire"] = vocabulaire
    interne["empreinte_vocabulaire"] = hashlib.sha256("\n".join(vocabulaire).encode("utf-8")).hexdigest()
    return interne


def noter_b(interne: dict, actions: list[dict], centres_: dict) -> np.ndarray:
    return _noter(interne, _traits_b(actions, centres_, interne["vocabulaire"]))
