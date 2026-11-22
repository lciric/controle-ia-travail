"""Brique A — magasin d'activations gardées, version 1 (consigne du développeur des sondes v2, § 2, brique A).

Une **série** est la lecture d'un jeu de textes par un jeu de poids. Elle vit dans un dossier :

    <dossier>/manifeste.json        identifiants (série, poids qui lisent, source des textes), couches, règle de choix
                                    des actions gardées, nombre d'actions, largeur, empreinte de chaque fichier ;
                                    scellé par son compagnon `manifeste.json.sha256` (R6)
    <dossier>/actions.jsonl         une ligne par action : clé, tâche, épisode, rang du pas, graine, position du champ
                                    révélateur (ou null), valeur déclarée dans ce champ (ou null), nombre de jetons
    <dossier>/c15/<clé>.npy         jetons notés à la couche décisive, demi-précision, forme (jetons, largeur) —
                                    convention de clés de `t06.lanceur_v2.ActivationsDemi` (`c<couche>/<clé>.npy`)
    <dossier>/avant_champ/c<k>/<clé>.npy
                                    jeton qui précède le champ révélateur, couches 7, 15 et 23, forme (largeur,),
                                    demi-précision ; présent si et seulement si l'action a un champ révélateur

Le lecteur relit en simple précision et vérifie, à chaque lecture, l'empreinte du fichier contre le manifeste. Toute
comparaison entre séries passe par `intersection_cles` (intersection des clés, effectifs rapportés). Gardes (R5) : clé
manquante, clé en double, empreinte fausse, forme inattendue, fichier non déclaré, valeur hors de la demi-précision.

Adaptateur : `serie_depuis_activations_demi` range dans une série un dossier écrit par `ActivationsDemi` (qui ne porte
ni empreinte ni métadonnées), avec les métadonnées fournies par l'appelant ; les empreintes des fichiers sources sont
consignées au manifeste. Le module ne lit pas `lanceur_v2` (qui importe torch) : il en reprend la convention de clés.
L'adaptateur pour les activations gardées du test sur les adaptateurs jumeaux s'écrira plus tard, d'après une
description de format fournie par la mère.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import empreinte, sceller, verifier

FORMAT = "magasin-activations-gardees-v1"
COUCHE_DECISIVE = 15
COUCHES_AVANT_CHAMP = (7, 15, 23)
FLOAT16_MAX = float(np.finfo(np.float16).max)
_CLE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,199}$")
CHAMPS_ACTION = ("cle", "tache", "episode", "pas", "graine", "position_champ", "valeur_declaree", "n_jetons")
REGLES = ("toutes", "part")


@dataclass(frozen=True)
class Action:
    """Métadonnées d'une action gardée. `position_champ` : indice, dans le texte de l'action, du premier jeton du champ
    révélateur (None s'il n'y en a pas) ; `valeur_declaree` : valeur écrite dans ce champ (None sans champ)."""
    cle: str
    tache: str
    episode: str
    pas: int
    graine: int | None
    position_champ: int | None
    valeur_declaree: float | None
    n_jetons: int

    def verifier(self) -> None:
        if not isinstance(self.cle, str) or not _CLE.match(self.cle):
            raise GardeArret(f"clé {self.cle!r} : lettres, chiffres, « . », « _ », « - », 200 signes au plus")
        if not isinstance(self.tache, str) or not self.tache:
            raise GardeArret(f"action {self.cle} : tâche vide")
        if not isinstance(self.episode, str) or not self.episode:
            raise GardeArret(f"action {self.cle} : épisode vide")
        for nom in ("pas", "graine", "n_jetons"):
            v = getattr(self, nom)
            if nom == "graine" and v is None:  # graine inconnue du format source (barreau 5) : écrite null
                continue
            if not isinstance(v, int) or isinstance(v, bool) or v < 0:
                raise GardeArret(f"action {self.cle} : {nom} entier positif ou nul attendu, reçu {v!r}")
        if self.n_jetons < 1:
            raise GardeArret(f"action {self.cle} : au moins un jeton noté")
        if (self.position_champ is None) != (self.valeur_declaree is None):
            raise GardeArret(f"action {self.cle} : position du champ et valeur déclarée vont ensemble")
        if self.position_champ is not None:
            p = self.position_champ
            if not isinstance(p, int) or isinstance(p, bool) or p < 1:
                raise GardeArret(f"action {self.cle} : position du champ ≥ 1 attendue (un jeton doit le précéder)")
            v = self.valeur_declaree
            if not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(float(v)):
                raise GardeArret(f"action {self.cle} : valeur déclarée finie attendue")

    @property
    def a_un_champ(self) -> bool:
        return self.position_champ is not None

    @classmethod
    def depuis_dict(cls, d: dict) -> "Action":
        if set(d) != set(CHAMPS_ACTION):
            raise GardeArret(f"ligne d'action : champs {sorted(d)} au lieu de {sorted(CHAMPS_ACTION)}")
        v = d["valeur_declaree"]
        a = cls(d["cle"], d["tache"], d["episode"], d["pas"], d["graine"], d["position_champ"],
                None if v is None else float(v), d["n_jetons"])
        a.verifier()
        return a


def _verifier_poids(poids: dict) -> dict:
    """Identifiant des poids qui lisent : {"type": "nu"} ; {"type": "adaptateur", "empreinte_adaptateur": hex64,
    "dose": nombre} ; ou {"type": "adaptateur_nomme", "nom": texte, "dose": nombre ou null} quand l'empreinte n'est
    pas connue du lecteur (noms opaques du barreau 5). Champs supplémentaires refusés."""
    if not isinstance(poids, dict) or poids.get("type") not in ("nu", "adaptateur", "adaptateur_nomme"):
        raise GardeArret(f"poids {poids!r} : type « nu », « adaptateur » ou « adaptateur_nomme » attendu")
    if poids["type"] == "nu":
        if set(poids) != {"type"}:
            raise GardeArret("poids nus : aucun autre champ")
        return dict(poids)
    if poids["type"] == "adaptateur_nomme":
        if set(poids) != {"type", "nom", "dose"} or not isinstance(poids["nom"], str) or not _CLE.match(poids["nom"]):
            raise GardeArret("poids d'adaptateur nommé : champs type, nom (identifiant), dose attendus")
        d = poids["dose"]
        if d is not None and (not isinstance(d, (int, float)) or isinstance(d, bool) or not math.isfinite(float(d))):
            raise GardeArret("dose : nombre fini ou null attendu")
        return dict(poids)
    if set(poids) != {"type", "empreinte_adaptateur", "dose"}:
        raise GardeArret("poids d'adaptateur : champs type, empreinte_adaptateur, dose attendus")
    if not isinstance(poids["empreinte_adaptateur"], str) or not re.fullmatch(r"[0-9a-f]{64}",
                                                                             poids["empreinte_adaptateur"]):
        raise GardeArret("empreinte de l'adaptateur : 64 chiffres hexadécimaux")
    d = poids["dose"]
    if not isinstance(d, (int, float)) or isinstance(d, bool) or not math.isfinite(float(d)):
        raise GardeArret("dose : nombre fini attendu")
    return dict(poids)


def _verifier_regle(regle: dict) -> dict:
    """Règle de choix des actions gardées : {"type": "toutes"} ou {"type": "part", "part": description déclarée,
    "cles": [liste des clés gardées]}."""
    if not isinstance(regle, dict) or regle.get("type") not in REGLES:
        raise GardeArret(f"règle {regle!r} : type « toutes » ou « part » attendu")
    if regle["type"] == "toutes":
        if set(regle) != {"type"}:
            raise GardeArret("règle « toutes » : aucun autre champ")
        return dict(regle)
    if set(regle) != {"type", "part", "cles"}:
        raise GardeArret("règle « part » : champs type, part, cles attendus")
    if not isinstance(regle["part"], str) or not regle["part"].strip():
        raise GardeArret("règle « part » : la part déclarée est un texte non vide (par exemple « une_sur_dix »)")
    cles = regle["cles"]
    if not isinstance(cles, list) or not cles or len(set(cles)) != len(cles):
        raise GardeArret("règle « part » : liste de clés non vide et sans doublon")
    return {"type": "part", "part": regle["part"], "cles": sorted(cles)}


MODES_CHEMIN = ("origine", "relu à texte imposé")


def verifier_chemin(chemin: dict) -> dict:
    """Chemin de calcul (erratum 1, § 1) : {"programme": identifiant et version du programme de lecture,
    "precision": texte, "mode": « origine » ou « relu à texte imposé », "gabarit": gabarit de conversation}."""
    if not isinstance(chemin, dict) or set(chemin) != {"programme", "precision", "mode", "gabarit"}:
        raise GardeArret("chemin de calcul : champs programme, precision, mode, gabarit attendus")
    for k in ("programme", "precision", "gabarit"):
        if not isinstance(chemin[k], str) or not chemin[k].strip():
            raise GardeArret(f"chemin de calcul : {k} texte non vide")
    if chemin["mode"] not in MODES_CHEMIN:
        raise GardeArret(f"chemin de calcul : mode {chemin['mode']!r} hors de {MODES_CHEMIN}")
    return dict(chemin)


def _en_demi(a, forme_attendue: tuple, ou: str) -> np.ndarray:
    a = np.asarray(a)
    if a.shape != forme_attendue:
        raise GardeArret(f"{ou} : forme {a.shape} au lieu de {forme_attendue}")
    a = a.astype(np.float64)
    if not np.all(np.isfinite(a)) or float(np.abs(a).max(initial=0.0)) > FLOAT16_MAX:
        raise GardeArret(f"{ou} : activation non finie ou hors de la demi-précision : aucun arrondi silencieux")
    return np.ascontiguousarray(a.astype(np.float16))


def _chemin_jetons(cle: str) -> str:
    return f"c{COUCHE_DECISIVE}/{cle}.npy"


def _chemin_avant_champ(cle: str, couche: int) -> str:
    return f"avant_champ/c{int(couche)}/{cle}.npy"


class EcrivainSerie:
    """Écrit une série neuve. Le dossier ne doit pas exister (R12). `clore()` écrit `actions.jsonl` et le manifeste,
    puis scelle le manifeste ; une série non close n'a pas de manifeste et ne se lit pas."""

    def __init__(self, dossier, identifiant_serie: str, poids: dict, source_textes: str, regle: dict, largeur: int,
                 chemin_de_calcul: dict):
        self.chemin_de_calcul = verifier_chemin(chemin_de_calcul)
        self.dossier = Path(dossier)
        if self.dossier.exists():
            raise GardeArret(f"{self.dossier} existe déjà : R12 interdit d'écraser une série")
        if not isinstance(identifiant_serie, str) or not _CLE.match(identifiant_serie):
            raise GardeArret(f"identifiant de série {identifiant_serie!r} invalide")
        if not isinstance(source_textes, str) or not source_textes.strip():
            raise GardeArret("source des textes : identifiant non vide attendu")
        if not isinstance(largeur, int) or isinstance(largeur, bool) or largeur < 1:
            raise GardeArret("largeur : entier ≥ 1 attendu")
        self.identifiant, self.poids = identifiant_serie, _verifier_poids(poids)
        self.source, self.regle, self.largeur = source_textes, _verifier_regle(regle), largeur
        self.actions: list[Action] = []
        self._cles: set[str] = set()
        self.fichiers: dict[str, str] = {}
        self.clos = False
        self.dossier.mkdir(parents=True)
        (self.dossier / f"c{COUCHE_DECISIVE}").mkdir()
        for c in COUCHES_AVANT_CHAMP:
            (self.dossier / "avant_champ" / f"c{c}").mkdir(parents=True)

    def _ecrire(self, rel: str, a: np.ndarray) -> None:
        chemin = self.dossier / rel
        if chemin.exists():
            raise GardeArret(f"{chemin} existe déjà (R12)")
        with open(chemin, "wb") as f:
            np.save(f, a, allow_pickle=False)
        self.fichiers[rel] = empreinte(chemin)

    def ajouter(self, action: Action, jetons, avant_champ: dict | None = None) -> None:
        if self.clos:
            raise GardeArret("série close : aucun ajout")
        action.verifier()
        if action.cle in self._cles:
            raise GardeArret(f"clé en double : {action.cle}")
        j = _en_demi(jetons, (action.n_jetons, self.largeur), f"action {action.cle}, jetons de la couche "
                                                               f"{COUCHE_DECISIVE}")
        if action.a_un_champ:
            if not isinstance(avant_champ, dict) or set(avant_champ) != set(COUCHES_AVANT_CHAMP):
                raise GardeArret(f"action {action.cle} : jeton d'avant le champ attendu aux couches "
                                 f"{COUCHES_AVANT_CHAMP} exactement")
            vecteurs = {c: _en_demi(avant_champ[c], (self.largeur,), f"action {action.cle}, avant le champ, "
                                                                     f"couche {c}") for c in COUCHES_AVANT_CHAMP}
        elif avant_champ is not None:
            raise GardeArret(f"action {action.cle} : jeton d'avant le champ donné sans champ révélateur")
        self._ecrire(_chemin_jetons(action.cle), j)
        if action.a_un_champ:
            for c in COUCHES_AVANT_CHAMP:
                self._ecrire(_chemin_avant_champ(action.cle, c), vecteurs[c])
        self.actions.append(action)
        self._cles.add(action.cle)

    def clore(self, provenance: dict | None = None) -> Path:
        if self.clos:
            raise GardeArret("série déjà close")
        if not self.actions:
            raise GardeArret("série vide")
        if self.regle["type"] == "part" and sorted(self._cles) != self.regle["cles"]:
            manque = sorted(set(self.regle["cles"]) - self._cles)
            hors = sorted(self._cles - set(self.regle["cles"]))
            raise GardeArret(f"règle « part » : clés déclarées ≠ clés écrites (manquent {manque[:5]}…, "
                             f"hors liste {hors[:5]}…)")
        lignes = "".join(json.dumps(asdict(a), ensure_ascii=False, sort_keys=True) + "\n" for a in self.actions)
        (self.dossier / "actions.jsonl").write_text(lignes, encoding="utf-8")
        manifeste = {
            "format": FORMAT,
            "identifiant_serie": self.identifiant,
            "poids": self.poids,
            "source_textes": self.source,
            "chemin_de_calcul": self.chemin_de_calcul,
            "couches": {"decisive": COUCHE_DECISIVE, "avant_champ": list(COUCHES_AVANT_CHAMP)},
            "precision_disque": "float16",
            "largeur": self.largeur,
            "regle": self.regle,
            "n_actions": len(self.actions),
            "n_actions_avec_champ": sum(a.a_un_champ for a in self.actions),
            "actions_sha256": empreinte(self.dossier / "actions.jsonl"),
            "fichiers": dict(sorted(self.fichiers.items())),
            "provenance": provenance,
        }
        chemin = self.dossier / "manifeste.json"
        chemin.write_text(json.dumps(manifeste, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        sceller(chemin)
        self.clos = True
        return chemin


class Serie:
    """Lecteur d'une série close. À l'ouverture : manifeste vérifié contre son compagnon, `actions.jsonl` contre le
    manifeste, aucune clé en double, chaque fichier déclaré présent, aucun fichier non déclaré. À chaque lecture :
    empreinte du fichier vérifiée, forme et précision contrôlées, relecture en simple précision.
    `verifier_tout=True` vérifie en plus toutes les empreintes à l'ouverture."""

    def __init__(self, dossier, verifier_tout: bool = False):
        self.dossier = Path(dossier)
        chemin = self.dossier / "manifeste.json"
        self.manifeste_sha256 = verifier(chemin)
        m = json.loads(chemin.read_text(encoding="utf-8"))
        if m.get("format") != FORMAT:
            raise GardeArret(f"{chemin} : format {m.get('format')!r} au lieu de {FORMAT!r}")
        if m["couches"] != {"decisive": COUCHE_DECISIVE, "avant_champ": list(COUCHES_AVANT_CHAMP)}:
            raise GardeArret(f"{chemin} : couches {m['couches']} inattendues")
        self.manifeste = m
        self.largeur = int(m["largeur"])
        self.regle = _verifier_regle(m["regle"])
        _verifier_poids(m["poids"])
        if "chemin_de_calcul" not in m:
            raise GardeArret(f"{chemin} : chemin de calcul absent (erratum 1, § 1)")
        self.chemin_de_calcul = verifier_chemin(m["chemin_de_calcul"])
        ja = self.dossier / "actions.jsonl"
        if not ja.is_file() or empreinte(ja) != m["actions_sha256"]:
            raise GardeArret(f"{ja} : absent ou empreinte différente du manifeste")
        self.actions: dict[str, Action] = {}
        self.ordre: list[str] = []
        for i, ligne in enumerate(ja.read_text(encoding="utf-8").splitlines()):
            a = Action.depuis_dict(json.loads(ligne))
            if a.cle in self.actions:
                raise GardeArret(f"{ja} : clé en double {a.cle} (ligne {i + 1})")
            self.actions[a.cle] = a
            self.ordre.append(a.cle)
        if len(self.ordre) != m["n_actions"]:
            raise GardeArret(f"{ja} : {len(self.ordre)} actions au lieu de {m['n_actions']}")
        if self.regle["type"] == "part" and sorted(self.ordre) != self.regle["cles"]:
            raise GardeArret("règle « part » : clés de actions.jsonl ≠ clés déclarées")
        attendus = set()
        for a in self.actions.values():
            attendus.add(_chemin_jetons(a.cle))
            if a.a_un_champ:
                attendus.update(_chemin_avant_champ(a.cle, c) for c in COUCHES_AVANT_CHAMP)
        declares = set(m["fichiers"])
        if attendus != declares:
            raise GardeArret(f"manifeste : fichiers déclarés ≠ fichiers attendus par actions.jsonl "
                             f"({len(declares - attendus)} en trop, {len(attendus - declares)} manquants)")
        presents = {str(p.relative_to(self.dossier)) for p in self.dossier.rglob("*.npy")}
        if presents - declares:
            raise GardeArret(f"fichier non déclaré dans la série : {sorted(presents - declares)[:3]}")
        if declares - presents:
            raise GardeArret(f"fichier déclaré absent du disque : {sorted(declares - presents)[:3]}")
        if verifier_tout:
            self.verifier_empreintes()

    @property
    def identifiant(self) -> str:
        return self.manifeste["identifiant_serie"]

    @property
    def cles(self) -> list[str]:
        return list(self.ordre)

    def verifier_empreintes(self) -> int:
        for rel, sha in self.manifeste["fichiers"].items():
            if empreinte(self.dossier / rel) != sha:
                raise GardeArret(f"{self.dossier / rel} : empreinte fausse")
        return len(self.manifeste["fichiers"])

    def _action(self, cle: str) -> Action:
        if cle not in self.actions:
            raise GardeArret(f"série {self.identifiant} : clé manquante {cle!r}")
        return self.actions[cle]

    def _charger(self, rel: str, forme: tuple) -> np.ndarray:
        chemin = self.dossier / rel
        attendue = self.manifeste["fichiers"][rel]
        with open(chemin, "rb") as f:
            octets = f.read()
        if hashlib.sha256(octets).hexdigest() != attendue:
            raise GardeArret(f"{chemin} : empreinte fausse")
        with open(chemin, "rb") as f:
            a = np.load(f, allow_pickle=False)
        if a.dtype != np.float16 or a.shape != forme:
            raise GardeArret(f"{chemin} : {a.dtype} {a.shape} au lieu de float16 {forme}")
        return a.astype(np.float32)

    def jetons(self, cle: str) -> np.ndarray:
        """Jetons notés de l'action à la couche décisive, (jetons, largeur), simple précision."""
        a = self._action(cle)
        return self._charger(_chemin_jetons(cle), (a.n_jetons, self.largeur))

    def avant_champ(self, cle: str, couche: int) -> np.ndarray:
        """Jeton d'avant le champ révélateur à la couche donnée (7, 15 ou 23), (largeur,), simple précision."""
        a = self._action(cle)
        if int(couche) not in COUCHES_AVANT_CHAMP:
            raise GardeArret(f"couche {couche} : avant le champ, seulement {COUCHES_AVANT_CHAMP}")
        if not a.a_un_champ:
            raise GardeArret(f"action {cle} : pas de champ révélateur")
        return self._charger(_chemin_avant_champ(cle, couche), (self.largeur,))


def intersection_cles(*series: Serie) -> tuple[list[str], dict]:
    """Clés communes à toutes les séries (triées), et effectifs : par série, total et clés absentes de l'intersection.
    Gardes : séries de chemins de calcul différents (erratum 1, § 1 ; voir `diagnostic_intersection_chemins_melanges`) ;
    une même clé portant des métadonnées de texte différentes (tâche, épisode, pas, position du champ, nombre de
    jetons) d'une série à l'autre — elle ne désigne pas la même action."""
    chemins = {json.dumps(s.chemin_de_calcul, sort_keys=True, ensure_ascii=False) for s in series}
    if len(chemins) > 1:
        raise GardeArret(f"comparaison de séries de chemins de calcul différents : {sorted(chemins)}")
    return _intersection(*series)


def diagnostic_intersection_chemins_melanges(*series: Serie) -> tuple[list[str], dict]:
    """DIAGNOSTIC SEULEMENT : intersection permise entre chemins de calcul différents ; le mélange est écrit dans
    les effectifs rendus (`melange_de_chemins`), à recopier dans toute sortie."""
    cles, eff = _intersection(*series)
    eff["melange_de_chemins"] = {s.identifiant: s.chemin_de_calcul for s in series}
    return cles, eff


def _intersection(*series: Serie) -> tuple[list[str], dict]:
    if len(series) < 2:
        raise GardeArret("intersection : au moins deux séries")
    ids = [s.identifiant for s in series]
    if len(set(ids)) != len(ids):
        raise GardeArret(f"intersection : séries de même identifiant {ids}")
    communes = set(series[0].actions)
    for s in series[1:]:
        communes &= set(s.actions)
    communes = sorted(communes)
    for cle in communes:
        ref = series[0].actions[cle]
        for s in series[1:]:
            a = s.actions[cle]
            for champ in ("tache", "episode", "pas", "position_champ", "n_jetons"):
                if getattr(a, champ) != getattr(ref, champ):
                    raise GardeArret(f"clé {cle} : {champ} diffère entre {series[0].identifiant} et {s.identifiant}")
    effectifs = {"communes": len(communes),
                 "par_serie": {s.identifiant: {"total": len(s.actions), "hors_intersection": len(s.actions) -
                                               len(communes)} for s in series}}
    return communes, effectifs


def serie_depuis_activations_demi(dossier_demi, lignes: list[dict], dossier_sortie, identifiant_serie: str,
                                  poids: dict, source_textes: str, regle: dict, chemin_de_calcul: dict) -> Path:
    """Range dans une série neuve un dossier écrit par `ActivationsDemi` (`<dossier_demi>/c<couche>/<clé>.npy`,
    demi-précision, (jetons, largeur)).

    `lignes` : une par action, champs de `Action` sauf `n_jetons` (lu du fichier), plus `indice_avant_champ` : indice,
    dans le segment de jetons notés, du jeton qui précède le champ révélateur (None sans champ). Le jeton d'avant le
    champ est pris à cet indice aux couches 7, 15 et 23, qui doivent alors exister dans le dossier source. Les empreintes
    des fichiers sources lus sont consignées au manifeste (`provenance`)."""
    dossier_demi = Path(dossier_demi)
    source_c = dossier_demi / f"c{COUCHE_DECISIVE}"
    if not source_c.is_dir():
        raise GardeArret(f"{source_c} : couche décisive absente du dossier ActivationsDemi")
    largeur = None
    sources: dict[str, str] = {}

    def lire(couche, cle):
        chemin = dossier_demi / f"c{couche}" / f"{cle}.npy"
        if not chemin.is_file():
            raise GardeArret(f"{chemin} : absent")
        with open(chemin, "rb") as f:
            a = np.load(f, allow_pickle=False)
        if a.dtype != np.float16 or a.ndim != 2 or a.shape[0] < 1:
            raise GardeArret(f"{chemin} : float16 (jetons, largeur) attendu, reçu {a.dtype} {a.shape}")
        sources[f"c{couche}/{cle}.npy"] = empreinte(chemin)
        return a

    vus: set[str] = set()
    preparees = []
    for l in lignes:
        attendus = (set(CHAMPS_ACTION) - {"n_jetons"}) | {"indice_avant_champ"}
        if set(l) != attendus:
            raise GardeArret(f"ligne {l.get('cle')!r} : champs {sorted(l)} au lieu de {sorted(attendus)}")
        if l["cle"] in vus:
            raise GardeArret(f"clé en double : {l['cle']}")
        vus.add(l["cle"])
        j = lire(COUCHE_DECISIVE, l["cle"])
        if largeur is None:
            largeur = int(j.shape[1])
        elif j.shape[1] != largeur:
            raise GardeArret(f"action {l['cle']} : largeur {j.shape[1]} au lieu de {largeur}")
        a = Action(l["cle"], l["tache"], l["episode"], l["pas"], l["graine"], l["position_champ"],
                   l["valeur_declaree"], int(j.shape[0]))
        a.verifier()
        i = l["indice_avant_champ"]
        if a.a_un_champ != (i is not None):
            raise GardeArret(f"action {a.cle} : indice d'avant le champ et champ révélateur vont ensemble")
        avant = None
        if i is not None:
            avant = {}
            for c in COUCHES_AVANT_CHAMP:
                seg = j if c == COUCHE_DECISIVE else lire(c, a.cle)
                if seg.shape[1] != largeur:
                    raise GardeArret(f"action {a.cle}, couche {c} : largeur {seg.shape[1]} au lieu de {largeur}")
                if not isinstance(i, int) or isinstance(i, bool) or not 0 <= i < seg.shape[0]:
                    raise GardeArret(f"action {a.cle} : indice d'avant le champ {i!r} hors du segment "
                                     f"({seg.shape[0]} jetons, couche {c})")
                avant[c] = seg[i]
        preparees.append((a, j, avant))
    if not preparees:
        raise GardeArret("aucune ligne")
    ecrivain = EcrivainSerie(dossier_sortie, identifiant_serie, poids, source_textes, regle, largeur, chemin_de_calcul)
    for a, j, avant in preparees:
        ecrivain.ajouter(a, j, avant)
    return ecrivain.clore({"adaptateur": "ActivationsDemi", "dossier_source": str(dossier_demi),
                           "empreintes_sources": dict(sorted(sources.items()))})


# ------------------------------------------------------------------------------------------- adaptateur du barreau 5

_CHEMIN_B5 = re.compile(r"^activations/([A-Za-z0-9_-]+)/c(7|15|23)/([A-Za-z0-9._-]+)__p([0-9]{1,3})\.npy$")


def series_depuis_barreau5(dossier_run, dossier_sortie, chemin_de_calcul: dict, poids_par_serie: dict | None = None,
                           source_par_serie: dict | None = None) -> dict:
    """Adaptateur du format des activations gardées par la relecture décisive du barreau 5 (pièce
    `format-activations-gardees-relecture-b5f-v1.md`, b8539886…) :
    `<dossier_run>/activations/<série>/c<7|15|23>/<tâche>__p<pas>.npy` (float16, (jetons notés, largeur)),
    `inventaire-activations.json` et `garde-activations.json` (scellés). Règle « une_sur_dix » : couche 15 seule, même
    liste de clés dans toutes les séries `nu` et adaptateurs (appariées) ; les séries `propre-*` portent leurs propres
    clés. Aucun jeton d'avant le champ, aucune étiquette de paire, graine inconnue (null).

    Range chaque série gardée dans une série du magasin, `<dossier_sortie>/<série>`. Gardes : inventaire et liste de
    garde vérifiés contre leurs compagnons ; chemin hors de la liste blanche ; fichier gardé absent de l'inventaire ou
    d'empreinte différente ; couche autre que 15 sous « une_sur_dix » ; séries `nu` et adaptateurs de clés différentes ;
    tableau non float16 ou de forme inattendue. `poids_par_serie` : {série : poids} (défaut : `nu` → nu, sinon
    adaptateur nommé de dose inconnue) ; `source_par_serie` : {série : source des textes} (défaut : « honnetes-communs »,
    ou « propres-<série> » pour `propre-*`). Rend {série : chemin du manifeste}."""
    dossier_run = Path(dossier_run)
    inv_chemin, garde_chemin = dossier_run / "inventaire-activations.json", dossier_run / "garde-activations.json"
    verifier(inv_chemin)
    verifier(garde_chemin)
    inventaire = {f["chemin"]: f for f in json.loads(inv_chemin.read_text(encoding="utf-8"))["fichiers"]}
    garde = json.loads(garde_chemin.read_text(encoding="utf-8"))
    if garde.get("regle") != "une_sur_dix":
        raise GardeArret(f"règle de garde {garde.get('regle')!r} : seule « une_sur_dix » est prévue par cet adaptateur")
    par_serie: dict = {}
    for rel in garde["fichiers"]:
        m = _CHEMIN_B5.match(rel)
        if not m:
            raise GardeArret(f"chemin hors de la liste blanche : {rel!r}")
        serie, couche, tache, pas = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
        if couche != COUCHE_DECISIVE:
            raise GardeArret(f"{rel} : couche {couche} sous « une_sur_dix » (couche 15 seule)")
        if rel not in inventaire:
            raise GardeArret(f"{rel} : absent de l'inventaire")
        chemin = dossier_run / rel
        if not chemin.is_file() or empreinte(chemin) != inventaire[rel]["sha256"]:
            raise GardeArret(f"{rel} : absent ou empreinte différente de l'inventaire")
        cle = f"{tache}__p{pas}"
        if cle in par_serie.setdefault(serie, {}):
            raise GardeArret(f"clé en double : {serie}/{cle}")
        par_serie[serie][cle] = (tache, pas, chemin)
    if "nu" not in par_serie:
        raise GardeArret("série « nu » absente de la garde")
    cles_nu = sorted(par_serie["nu"])
    for serie, d in par_serie.items():
        if not serie.startswith("propre-") and sorted(d) != cles_nu:
            raise GardeArret(f"série {serie} : clés différentes de celles de « nu » (appariement rompu)")
    sortie = {}
    for serie in sorted(par_serie):
        poids = (poids_par_serie or {}).get(serie) or ({"type": "nu"} if serie == "nu" else
                                                        {"type": "adaptateur_nomme", "nom": serie, "dose": None})
        source = (source_par_serie or {}).get(serie) or (f"propres-{serie}" if serie.startswith("propre-")
                                                          else "honnetes-communs")
        cles = sorted(par_serie[serie])
        largeur = None
        tableaux = []
        for cle in cles:
            tache, pas, chemin = par_serie[serie][cle]
            with open(chemin, "rb") as f:
                a = np.load(f, allow_pickle=False)
            if a.dtype != np.float16 or a.ndim != 2 or a.shape[0] < 1:
                raise GardeArret(f"{chemin} : float16 (jetons, largeur) attendu, reçu {a.dtype} {a.shape}")
            if largeur is None:
                largeur = int(a.shape[1])
            elif a.shape[1] != largeur:
                raise GardeArret(f"{chemin} : largeur {a.shape[1]} au lieu de {largeur}")
            tableaux.append((Action(cle, tache, tache, pas, None, None, None, int(a.shape[0])), a))
        e = EcrivainSerie(Path(dossier_sortie) / serie, serie, poids, source,
                          {"type": "part", "part": "une_sur_dix", "cles": cles}, largeur, chemin_de_calcul)
        for act, a in tableaux:
            e.ajouter(act, a)
        sortie[serie] = e.clore({"adaptateur": "barreau5-une_sur_dix", "dossier_source": str(dossier_run),
                                 "inventaire_sha256": empreinte(inv_chemin), "garde_sha256": empreinte(garde_chemin)})
    return sortie
