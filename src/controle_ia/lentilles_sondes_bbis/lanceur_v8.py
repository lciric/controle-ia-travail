"""Lanceur de la lecture des sondes de l'étape B bis par la lentille publique (texte scellé, « Plan d'analyse »,
points 4 à 6 et 10), sous une horloge de 8 h.

Sous-commandes :
- `montage` (point 4, puis garde de la fonction de lecture du point 5) : ne touche aucune sonde ; permis avant `VERDICT-BBIS` ;
- `recuperer` : clone partiel sans contenus, puis E-1, E-2 et leurs compagnons seuls ; refusé avant `VERDICT-BBIS` ;
- `calcul` (point 6, puis nettoyage du point 10) : refusé avant `VERDICT-BBIS` ; écrit des fichiers **fermés** ;
- `phrases` : rend les phrases gelées à partir des tables (étape du lecteur, après `VERDICT-BBIS` scellée).
Sorties (« Données gardées et plan de stockage ») sous le dossier de sortie : `diag/<run>/montage-lentilles-bbis.json`,
`diag/<run>/tables-lentilles-bbis.json`, `donnees/<run>/lectures-lentilles-bbis-NNN.npz` (morceaux de moins de 95 Mo),
`runs/<run>/manifeste.json`, chacun avec son compagnon `.sha256`. Le lanceur n'inscrit aucune ligne de registre et ne pousse
rien : il rend les lignes proposées. Les `Reglages` par défaut sont ceux du texte ; seuls les essais les remplacent.

Version 2 (après la contre-lecture `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-code-lentille-publique-v1.md`,
`679eb7232eed0c154743348102cccd40c05b8f38b1f730eeb21b24f171af155d`) : fiche du code vérifiée par le code (A) ; versement avant
tout nettoyage et à l'arrêt (C) ; noms des tableaux retirés de la sortie de la ligne de commande (D) ; essai hors ligne du
tokeniseur juste après la pose du cache ; fiche fermée des entrées ; manifeste qui cite le rapport du montage ; note explicite
pour les pôles « intermédiaires ». Aucune ligne de calcul n'est changée depuis `lanceur_v1`. Emploie `entrees_v2` (B).

Version 3 : seule différence avec `lanceur_v2`, les statistiques sont celles de `statistiques_v2` (concentration et part des
directions nulles calculées sans elles-mêmes : écart au texte scellé décidé par le directeur, porté par l'addendum
`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`, en rédaction quand ce module est écrit). Les tables
et le manifeste le disent (`statistique_des_directions_nulles`). **Préparé, non définitif** : à accorder à l'addendum scellé,
bornes de calibration comprises (`audits_v1` inchangé d'ici là), avant la ligne `CODE-LENTILLES-BBIS`.

Version 4 : le code de l'addendum de concentration **scellé**
(`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
`7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`). Depuis `lanceur_v3` :
- EC-4 (couple C1) : la ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` est exigée avant toute requête ou ouverture (`entrees_v3`) ;
  la fiche du code porte le chemin et l'empreinte de l'addendum (champ `addendum_concentration` : `chemin`, `sha256`), comparés
  à la ligne ; le rapport du montage, les tables et le manifeste citent l'addendum à côté du texte ; la sous-commande
  `recuperer` vérifie aussi la fiche du code ;
- EC-1, EC-2, EC-6 : statistiques de `statistiques_v3` (directions nulles jugées sans elles-mêmes ; garde d'égalité au
  vingtième rang, option 3 : direction lue : arrêt nommé ; direction nulle : marquée, p_bas et p_haut, arrêt nommé si un
  libellé en dépend ; témoin : compté) ; au montage, compte des paires de jetons gardés de même ligne de sortie, sans arrêt ;
- EC-3 : la loi des bornes de calibration est dite « de référence, approchée » dans les tables ; `audits_v1` est inchangé
  (addendum, § 4 : aucun `audits_v2` n'est demandé) : le mot « exacte » de sa docstring se lit « de référence, approchée » ;
- remarque non bloquante de la vérification de la version 2 du code, reprise : le rapport du montage est exigé au départ du
  calcul (absent : rien ne part), et le manifeste le cite toujours.

Version 5 : messages d'arrêt cloisonnés (mot de Lazar, GO-2026-11-20-56 ; nœud 1 de la contre-lecture
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-premiere-passe-addendum-v1.md`,
`7954d0fc54320d76ed63a634893063425683806dfb327acec1443e1ed6a96fd4`). Seule différence avec `lanceur_v4` : quand le calcul
s'arrête sur une égalité au vingtième rang d'une direction lue (`EgaliteDirectionLue`, EC-6, étage (i)) ou sur une égalité d'une
direction nulle décisive pour un libellé (`EgaliteNulleDecisive`, étage (ii)), le message entier que l'addendum exige est écrit
dans le seul fichier d'arrêt, `versement/<run>/calcul-interrompu/arret.json` (champ `motif`) ; la sortie d'erreur ne porte que
le nom de l'arrêt et le chemin de ce fichier, la sortie standard rien. Le tri se fait ici (`ARRETS_CLOISONNES`,
`verser_arret_cloisonne`, `ligne_d_arret_cloisonne`) ; `statistiques_v3` est inchangé. Les autres arrêts gardent leur sortie.
Aucune ligne de calcul n'est changée depuis `lanceur_v4`.

Version 6 : correction 1 de la contre-lecture du lanceur version 5
(`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-lanceur-v5-messages-arret-v1.md`,
`d821cf66698537c8649a3b55ffebdf13b321abfd066bbde1d9df1af6aa82be9b`). Seule différence avec `lanceur_v5` : une interruption du
clavier qui tombe pendant le traitement d'un arrêt cloisonné n'en porte plus le message dans sa trace. `principal` ne fait
dans son bloc `except` que retenir l'arrêt, et calcule et affiche la ligne après ; `calculer` relève sans enchaînement toute
interruption levée pendant le tri et le versement ; `verser_arret_cloisonne` tient tout son corps sous la même coupure. Les
mots fixes de la ligne affichée sont inchangés, et tenus par des constantes. Aucune ligne de calcul n'est changée.

Version 7 : garde du fichier d'arrêt déjà présent (mot de Lazar, GO-2026-11-21-06 ; nœud 2 de la contre-lecture `d821cf66…`).
Seule différence avec `lanceur_v6` : au départ de la sous-commande `calcul`, avant toute lecture de registre, toute requête,
tout chargement et tout calcul, `exiger_aucun_fichier_d_arret` arrête si un `arret.json` existe déjà au chemin où l'arrêt de
cette course serait écrit (`<sortie>/versement/<run>/calcul-interrompu/arret.json`) : la règle de non-réécriture (R12) y
ferait perdre le message d'un second arrêt. Rien n'est écrit, rien n'est supprimé. Ce n'est pas un arrêt cloisonné : son
message ne porte que le chemin et sort comme celui des autres arrêts. Les mots fixes de la ligne affichée sont gardés tels
quels. Aucune ligne de calcul n'est changée.

Version 8 : correctif de la pagination de l'arbre du corpus (mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-pagination-corpus-v1.md`, `c0c07faa…`).
Seule différence avec `lanceur_v7` : au montage, les cibles des essais d'un octet du corpus des jetons gardés viennent de
`corpus_pagine_v1.cibles_corpus`, qui suit les pages de l'arbre d'un jeu de données jusqu'à la première qui porte un fichier
de données, et non plus de `montage_v1.cibles_corpus`, qui n'en lit que la première page ; `corpus_pagine_v1` entre dans la
liste des modules dont la fiche du code porte l'empreinte. Aucune ligne de calcul n'est changée.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch

from .. import manifeste as mf
from ..scellement import sceller, verifier
from . import audits_v1 as au
from . import constantes_v1 as K
from . import corpus_pagine_v1 as cp
from . import entrees_v3 as en
from . import lecture_v1 as le
from . import montage_v1 as mo
from . import nuls_v1 as nu
from . import phrases_v1 as ph
from . import statistiques_v3 as st
from .constantes_v1 import Arret, Refus

MARQUE = "dossier-de-la-lecture-des-sondes-par-lentilles.txt"
_RE_RUN = re.compile(r"^[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}$")
MODULES = ("__init__", "constantes_v1", "entrees_v2", "entrees_v3", "montage_v1", "lecture_v1", "nuls_v1", "statistiques_v1",
           "statistiques_v2", "statistiques_v3", "audits_v1", "phrases_v1", "corpus_pagine_v1", "lanceur_v8")
ADDENDUM = {"chemin": en.ADDENDUM, "sha256": en.EMPREINTE_ADDENDUM}
CHAMP_ADDENDUM_DE_LA_FICHE = "addendum_concentration"


@dataclass
class Reglages:
    """Valeurs du texte (défauts). Les essais sur jouets en remplacent certaines ; la ligne de commande n'en expose aucune."""
    largeur: int = K.LARGEUR
    couches: tuple = K.COUCHES
    couches_lentille: tuple = K.COUCHES_LENTILLE
    couche_cible: int = K.COUCHE_CIBLE_LENTILLE
    depot_llama: str = K.DEPOT_LLAMA
    revision_llama: str = K.REVISION_LLAMA
    poids: dict = field(default_factory=lambda: dict(K.POIDS_LLAMA))
    petits: dict = field(default_factory=lambda: dict(K.PETITS_LLAMA))
    sha256_tokeniseur: str = K.SHA256_TOKENISEUR
    depot_lentille: str = K.DEPOT_LENTILLE
    revision_lentille: str = K.REVISION_LENTILLE
    fichier_lentille: str = K.FICHIER_LENTILLE
    taille_lentille: int = K.TAILLE_LENTILLE
    sha256_lentille: str = K.SHA256_LENTILLE
    pointeur_lentille: str = K.POINTEUR_LENTILLE
    licences_lentille: dict = field(default_factory=lambda: dict(K.LICENCES_LENTILLE))
    url_voisin: str = K.URL_VOISIN
    commit_voisin: str = K.COMMIT_VOISIN
    correctifs: tuple = K.CORRECTIFS
    copie_readout: str = K.COPIE_READOUT
    sha256_copie_readout: str = K.SHA256_COPIE_READOUT
    n_jetons: int = K.N_JETONS_GARDES
    sha256_jetons: str = K.SHA256_JETONS_GARDES
    m: int = K.M_NUL
    n_temoins_isotrope: int = K.N_TEMOINS_ISOTROPE
    n_temoins_par_vecteur: int = K.N_TEMOINS_PAR_VECTEUR
    n_colonnes_garde: int = K.N_COLONNES_GARDE
    disque_depart: int = K.DISQUE_DEPART_OCTETS
    disque_calcul: int = K.DISQUE_CALCUL_OCTETS


# --- gardes de procédure -----------------------------------------------------------------------------------------------------------------
class Horloge:
    """Durée cumulée de la session de calcul (montage et calcul), tenue dans le dossier de travail ; au-delà de 8 h : arrêt."""

    def __init__(self, travail: Path, limite_s: float = K.HORLOGE_S, maintenant=time.monotonic):
        self.fichier, self.limite, self.maintenant = Path(travail) / "horloge.json", float(limite_s), maintenant
        self.cumul = float(json.loads(self.fichier.read_text())["cumul_s"]) if self.fichier.is_file() else 0.0
        self.depart = maintenant()

    def ecoule(self) -> float:
        return self.cumul + (self.maintenant() - self.depart)

    def controler(self, etape: str = "") -> None:
        self.consigner()
        if self.ecoule() > self.limite:
            raise Arret(f"durée cumulée de la session de calcul au-delà de {self.limite / 3600:g} h ({etape}) : arrêt ; versement "
                        "de ce qui existe ; compte rendu")

    def consigner(self) -> None:
        if self.fichier.parent.is_dir():
            self.fichier.write_text(json.dumps({"cumul_s": self.ecoule()}))


def exiger_disque(dossier: Path, minimum: int, quand: str, mesure=shutil.disk_usage) -> int:
    """Moins de 6 Go libres au départ, ou moins de 1 Go pendant le calcul : arrêt, sans rien supprimer."""
    libre = int(mesure(str(dossier)).free)
    if libre < int(minimum):
        raise Arret(f"espace disque : {libre / 1e9:.2f} Go libres {quand}, {minimum / 1e9:g} Go exigés : arrêt, sans rien supprimer "
                    "hors du dossier de cette chaîne ; compte rendu")
    return libre


def ligne_registre(cle: str, chemin: str, sha256: str, heure: str | None = None) -> str:
    """Ligne du registre propre, au format du texte ; seules les clés de ce texte sont permises."""
    if cle not in K.CLES_PROPRES:
        raise Refus(f"clé {cle!r} : hors des clés de ce texte")
    heure = heure or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"| {cle} | {heure} | {chemin} | {sha256} |"


def inscrire_ligne(registre: str | Path, cle: str, chemin: str, sha256: str, heure: str | None = None) -> str:
    """Ajoute une ligne au registre propre (jamais réécrit). Une clé de ce texte dans `registres/scellements-v1.md` : refus."""
    registre = Path(registre)
    if registre.name == K.REGISTRE_INTERDIT:
        raise Refus(f"clé de ce texte dans registres/{K.REGISTRE_INTERDIT} : arrêt de l'écriture (la garde de T0.7 y refuse toute "
                    "clé inconnue)")
    if registre.name != Path(K.REGISTRE_PROPRE).name or not registre.is_file():
        raise Refus(f"{registre.name} : seul le registre propre de ce texte reçoit ses lignes")
    ligne = ligne_registre(cle, chemin, sha256, heure)
    with open(registre, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    return ligne


def empreintes_du_code() -> dict:
    ici = Path(__file__).resolve().parent
    return {f"{m}.py": mo.sha256_fichier(ici / f"{m}.py") for m in MODULES}


CHEMIN_PAQUET = "src/controle_ia/lentilles_sondes_bbis"


def exiger_fiche_code(racine_depot: Path, registre_propre: Path) -> dict:
    """Liste d'arrêt : « code non cité par `CODE-LENTILLES-BBIS` » : rien ne part. La fiche citée par la ligne a la forme des
    fiches `CODE-` du registre (`commit`, `fichiers`, `essais`, `contre_lecture` {chemin, sha256}) ; son empreinte égale celle
    de la ligne, et l'empreinte de chaque module de ce paquet égale celle que la fiche porte sous `fichiers`.
    Addendum, EC-4 : la fiche porte le chemin et l'empreinte de l'addendum scellé (`addendum_concentration` {chemin,
    sha256}) ; le code les compare à la ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS`, qui doit être seule et inscrite avant
    `CODE-LENTILLES-BBIS` et `ENTREES-LENTILLES-BBIS` ; sinon rien ne part. Appelée avant toute requête ou ouverture."""
    ligne_code = en.exiger_registre_propre(registre_propre)["CODE-LENTILLES-BBIS"]
    p = Path(racine_depot) / str(ligne_code.chemin)
    if not p.is_file() or mo.sha256_fichier(p) != ligne_code.sha256:
        raise Refus("fiche citée par CODE-LENTILLES-BBIS absente ou d'une autre empreinte que la ligne : rien ne part")
    try:
        fiche = json.loads(p.read_text(encoding="utf-8"))
        fichiers, essais, commit = fiche["fichiers"], fiche["essais"], str(fiche["commit"])
        lecture = fiche["contre_lecture"]
        forme = isinstance(fichiers, dict) and isinstance(essais, dict) and bool(lecture["chemin"]) and bool(lecture["sha256"])
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError):
        forme = False
    if not forme:
        raise Refus("fiche CODE-LENTILLES-BBIS d'une autre forme que les fiches CODE- du registre : rien ne part")
    porte = fiche.get(CHAMP_ADDENDUM_DE_LA_FICHE)
    if not isinstance(porte, dict) or not isinstance(porte.get("chemin"), str) or not isinstance(porte.get("sha256"), str):
        raise Refus("fiche CODE-LENTILLES-BBIS sans le chemin et l'empreinte de l'addendum de concentration scellé : rien ne part")
    ligne_addendum = en.exiger_addendum(registre_propre, porte["chemin"], porte["sha256"])
    ici = Path(__file__).resolve().parent
    for m in MODULES:
        nom = f"{CHEMIN_PAQUET}/{m}.py"
        if fichiers.get(nom) != mo.sha256_fichier(ici / f"{m}.py"):
            raise Refus(f"{nom} : empreinte absente de la fiche CODE-LENTILLES-BBIS ou différente : rien ne part")
    return {"fiche": str(ligne_code.chemin), "sha256": ligne_code.sha256, "commit_de_la_fiche": commit,
            "addendum": {"chemin": ligne_addendum.chemin, "sha256": ligne_addendum.sha256,
                         "heure_de_la_ligne": ligne_addendum.heure}}


def _commit(racine_depot: Path) -> str | None:
    r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=racine_depot, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def _ecrire_ferme(chemin: Path, contenu: dict) -> str:
    """Fichier JSON écrit une seule fois (R12) et scellé ; rend son empreinte."""
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(json.dumps(contenu, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
    return sceller(chemin)


def ecrire_morceaux(tableaux: dict[str, np.ndarray], prefixe: Path, limite: int = K.LIMITE_MORCEAU) -> list[dict]:
    """Archives `numpy` non compressées, numérotées, de moins de `limite` octets, chacune scellée."""
    prefixe.parent.mkdir(parents=True, exist_ok=True)
    marge = 2048
    lots, courant, taille = [], {}, 0
    for nom in sorted(tableaux):
        a = np.ascontiguousarray(tableaux[nom])
        if a.nbytes + marge >= limite:
            raise Arret(f"tableau {nom} trop grand pour un morceau de moins de {limite} octets")
        if courant and taille + a.nbytes + marge >= limite:
            lots.append(courant)
            courant, taille = {}, 0
        courant[nom] = a
        taille += a.nbytes + marge
    if courant:
        lots.append(courant)
    sortie = []
    for i, lot in enumerate(lots):
        chemin = Path(f"{prefixe}-{i:03d}.npz")
        if chemin.exists():
            raise Arret(f"{chemin} existe déjà (R12)")
        np.savez(chemin, **lot)
        if chemin.stat().st_size >= limite:
            raise Arret(f"{chemin.name} : morceau de {chemin.stat().st_size} octets, au-delà de la limite")
        sortie.append({"fichier": chemin.name, "sha256": sceller(chemin), "tableaux": sorted(lot)})
    return sortie


# Parties du dossier de travail jamais copiées (licence de Llama et de la lentille ; corpus non versé : « Données gardées ») ;
# elles sont inventoriées (nom, taille, SHA-256), jamais lues autrement.
NON_COPIES = ("tenseurs", "lentille", "hf", "lentille-publique.pt", "voisin")


def verser_travail(travail: Path, sortie: Path, run: str, moment: str) -> dict:
    """Règle « récupérer ce qui est récupérable » (mot de Lazar, 19 novembre 2026), avant toute suppression et à tout arrêt :
    inventaire de chaque fichier du dossier de travail (chemin relatif, taille, SHA-256) ; copie des fichiers hors des
    parties `NON_COPIES` (journaux des scripts du voisin, jetons gardés, état du montage, horloge, marque) et du correctif
    effectivement appliqué au voisin (`git diff`) ; le tout dans `<sortie>/versement/<run>/travail-<moment>/`, chaque fichier
    scellé, inventaire fermé et scellé. Rend {chemin, sha256} de l'inventaire."""
    travail, sortie = Path(travail), Path(sortie)
    dest = sortie / "versement" / run / f"travail-{moment}"
    if dest.exists():
        raise Arret(f"{dest} existe déjà (R12)")
    dest.mkdir(parents=True)
    inventaire, copies = [], []
    for f in sorted(travail.rglob("*")):
        if f.is_symlink() or not f.is_file():
            continue
        rel = f.relative_to(travail)
        inventaire.append({"chemin": str(rel), "taille": f.stat().st_size, "sha256": mo.sha256_fichier(f)})
        if rel.parts[0] not in NON_COPIES:
            cible = dest / "fichiers" / rel
            cible.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, cible)
            if mo.sha256_fichier(cible) != inventaire[-1]["sha256"]:
                raise Arret(f"versement : copie de {rel} différente de l'original : rien n'est supprimé")
            sceller(cible)
            copies.append(str(rel))
    voisin = travail / "voisin"
    if (voisin / ".git").exists():
        r = subprocess.run(["git", "diff"], cwd=voisin, capture_output=True)
        if r.returncode == 0:
            (dest / "voisin-correctifs-appliques.diff").write_bytes(r.stdout)
            sceller(dest / "voisin-correctifs-appliques.diff")
            copies.append("voisin : git diff")
    sha = _ecrire_ferme(dest / "inventaire.json", {"run": run, "moment": moment, "travail": str(travail),
                                                   "non_copies": list(NON_COPIES), "fichiers": inventaire, "copies": copies})
    return {"chemin": str((dest / "inventaire.json").relative_to(sortie)), "sha256": sha}


def nettoyer(travail: Path, sortie: Path, run: str) -> dict:
    """Plan, point 10 : verse ce qui est récupérable (`verser_travail`), vérifie le versement, puis supprime le dossier de
    travail de cette chaîne, par son chemin, et rien d'autre."""
    travail = Path(travail)
    if not (travail / MARQUE).is_file():
        raise Arret(f"{travail} ne porte pas la marque du dossier de cette chaîne : rien n'est supprimé")
    versement = verser_travail(travail, sortie, run, "fin")
    verifier(Path(sortie) / versement["chemin"])
    shutil.rmtree(travail)
    return versement


def _memoire() -> int | None:
    try:
        return int(os.sysconf("SC_PAGE_SIZE")) * int(os.sysconf("SC_PHYS_PAGES"))
    except (ValueError, OSError, AttributeError):
        return None


def _versions() -> dict:
    from importlib import metadata
    v = {"python": sys.version.split()[0]}
    for b in ("torch", "numpy", "transformers", "tokenizers", "huggingface_hub", "datasets", "safetensors", "pyarrow", "requests"):
        try:
            v[b] = metadata.version(b)
        except metadata.PackageNotFoundError:
            v[b] = "absent"
    return v


@dataclass
class Contexte:
    travail: Path
    sortie: Path
    run: str
    racine_depot: Path
    registre_propre: Path
    reglages: Reglages = field(default_factory=Reglages)
    transport: object | None = None
    env: dict | None = None
    maintenant: object = time.monotonic
    mesure_disque: object = shutil.disk_usage
    python: str = sys.executable

    def __post_init__(self):
        self.travail, self.sortie, self.racine_depot = Path(self.travail), Path(self.sortie), Path(self.racine_depot)
        if not _RE_RUN.match(self.run):
            raise Arret(f"identifiant de course {self.run!r} : format AAAAMMJJ-HHMMSS-nom attendu")
        t, s = self.travail.resolve(), self.sortie.resolve()
        if t == s or t in s.parents or s in t.parents:
            raise Arret("dossier de sortie et dossier de travail emboîtés : le nettoyage effacerait des sorties ; rien ne part")


# --- montage (plan, points 4 et 5) -------------------------------------------------------------------------------------------------------
def monter(ctx: Contexte) -> dict:
    """Montage au processeur, puis garde de la fonction de lecture. Ne touche aucune sonde. Rend le rapport de montage, écrit
    aussi dans `diag/<run>/montage-lentilles-bbis.json` (jamais la clé)."""
    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, ctx.registre_propre)
    mo.exiger_sans_debogage(ctx.env)
    cle = mo.lire_cle(ctx.env)
    if ctx.travail.exists():
        raise Arret(f"{ctx.travail} existe déjà : le dossier de travail de cette chaîne est neuf (R12)")
    ctx.travail.parent.mkdir(parents=True, exist_ok=True)
    libre = exiger_disque(ctx.travail.parent, r.disque_depart, "au départ", ctx.mesure_disque)
    ctx.travail.mkdir()
    (ctx.travail / MARQUE).write_text("Dossier de travail de la lecture des sondes de l'étape B bis par la lentille publique.\n")
    horloge = Horloge(ctx.travail, maintenant=ctx.maintenant)
    hf_home = ctx.travail / "hf"
    transport = ctx.transport if ctx.transport is not None else mo.TransportRequests()
    rapport = {"run": ctx.run, "texte": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE}, "addendum": dict(ADDENDUM),
               "versions": _versions(),
               "code": {"commit": _commit(ctx.racine_depot), "empreintes": empreintes_du_code(), "fiche_code": fiche_code},
               "machine": {"fils": os.cpu_count(), "octets_libres_au_depart": libre, "octets_de_memoire": _memoire()}}

    # réseau, avant tout flux long : un octet par hôte et par sorte de fichier
    premier_poids = sorted(r.poids)[0]
    cibles = [mo.Cible("lentille publique", mo.url_fichier(r.depot_lentille, r.revision_lentille, r.fichier_lentille)),
              mo.Cible("fichier de poids à porte", mo.url_fichier(r.depot_llama, r.revision_llama, premier_poids), avec_cle=True),
              mo.Cible("dépôt du code voisin", r.url_voisin + "/info/refs?service=git-upload-pack", sorte="en-tête")]
    rapport["essais_un_octet"] = mo.essais_un_octet(transport, cle, cibles)

    # code voisin : commit, comparaison de readout.py, correctifs
    voisin = ctx.travail / "voisin"
    rapport["voisin"] = {"commit": mo.cloner_voisin(voisin, r.url_voisin, r.commit_voisin)}
    readout = voisin / "neuron_lens" / "readout.py"
    rapport["voisin"]["readout"] = mo.comparer_readout(readout, ctx.racine_depot / r.copie_readout, r.sha256_copie_readout)
    rapport["voisin"]["fichiers_corriges"] = mo.appliquer_correctifs(voisin, ctx.racine_depot, r.correctifs)
    rapport["essais_un_octet"] += mo.essais_un_octet(transport, cle, cp.cibles_corpus(voisin, transport))
    horloge.controler("essais d'un octet")

    # petits fichiers de Llama, entiers, vérifiés ; tokeniseur posé dans le cache à la révision épinglée
    petits = {}
    for nom, (taille, ident) in sorted(r.petits.items()):
        petits[nom] = mo.telecharger_petit(transport, mo.url_fichier(r.depot_llama, r.revision_llama, nom), nom, taille, ident, cle)
    if "tokenizer.json" in petits and hashlib.sha256(petits["tokenizer.json"]).hexdigest() != r.sha256_tokeniseur:
        raise Arret("SHA-256 du tokeniseur différent de celui du texte : arrêt ; message à la mère")
    mo.poser_cache_tokeniseur(hf_home, {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA},
                              r.depot_llama, r.revision_llama)
    rapport["petits_fichiers"] = {n: {"taille": len(c), "identifiant_git": mo.identifiant_git(c)} for n, c in petits.items()}
    essayer_tokeniseur_du_cache(ctx, voisin, hf_home)
    rapport["essai_du_tokeniseur_hors_ligne"] = {"tenu": True, "journal": "journal-essai-tokeniseur.txt"}

    # poids : pointeurs vérifiés, lecture en flux, seuls les tenseurs gardés sur disque
    voulus = ("lm_head.weight", "model.norm.weight") + tuple(f"model.layers.{c}.mlp.down_proj.weight" for c in r.couches)
    par_fichier = mo.tenseurs_par_fichier(petits[K.INDEX_LLAMA], voulus)
    interface = mo.sha256_par_interface(transport, r.depot_llama, r.revision_llama, cle, tuple(par_fichier))
    tenseurs, poids = {}, {}
    for fichier, noms in par_fichier.items():
        if fichier not in r.poids:
            raise Arret(f"fichier de poids {fichier} absent de la table du texte : arrêt ; message à la mère")
        sha, taille = interface[fichier]
        mo.exiger_pointeur(fichier, sha, taille, r.poids[fichier][1], r.poids[fichier][0])
        exiger_disque(ctx.travail, r.disque_calcul, "pendant le montage", ctx.mesure_disque)
        tenseurs |= mo.lire_poids_en_flux(transport, mo.url_fichier(r.depot_llama, r.revision_llama, fichier), cle, noms,
                                          ctx.travail / "tenseurs", taille, sha)
        poids[fichier] = {"taille": taille, "sha256": sha, "identifiant_git_du_pointeur": r.poids[fichier][1], "tenseurs": list(noms)}
        horloge.controler(f"poids {fichier}")
    rapport["poids"] = poids

    # lentille publique : licences, pointeur, flux sur disque, contrôles ; seules les matrices des couches lues sont gardées
    licences = {}
    for chemin, (taille, ident) in sorted(r.licences_lentille.items()):
        c = mo.telecharger_petit(transport, mo.url_fichier(r.depot_lentille, r.revision_lentille, chemin), chemin, taille, ident)
        licences[chemin] = {"taille": len(c), "identifiant_git": mo.identifiant_git(c)}
    mo.exiger_pointeur("lentille publique", r.sha256_lentille, r.taille_lentille, r.pointeur_lentille, r.taille_lentille)
    fichier_lentille = ctx.travail / "lentille-publique.pt"
    mo.telecharger_en_fichier(transport, mo.url_fichier(r.depot_lentille, r.revision_lentille, r.fichier_lentille),
                              fichier_lentille, r.taille_lentille, r.sha256_lentille)
    mo.exiger_fichier_lentille(fichier_lentille, r.taille_lentille, r.sha256_lentille)
    controle, matrices = mo.controler_lentille(fichier_lentille, r.largeur, r.couches_lentille, r.couches, r.couche_cible)
    (ctx.travail / "lentille").mkdir()
    for l, m in matrices.items():
        np.save(ctx.travail / "lentille" / f"J-{l}.npy", m)
    del matrices
    fichier_lentille.unlink()
    rapport["lentille_publique"] = {"depot": r.depot_lentille, "revision": r.revision_lentille, "fichier": r.fichier_lentille,
                                    "taille": r.taille_lentille, "sha256": r.sha256_lentille, "licences": licences, **controle}
    horloge.controler("lentille publique")

    # jetons gardés
    jetons = mo.calculer_jetons_gardes(voisin, hf_home, ctx.travail, ctx.python, ctx.env)
    rapport["jetons_gardes"] = mo.exiger_jetons_gardes(jetons["ids"], r.n_jetons, r.sha256_jetons)
    horloge.controler("jetons gardés")

    etat = {"tenseurs": tenseurs, "empreintes_matrices": controle["empreintes_matrices_gardees"],
            "readout": str(readout.relative_to(ctx.travail)), "point_de_capture": controle["provenance"].get("capture_point")}
    (ctx.travail / "etat-montage.json").write_text(json.dumps(etat, indent=1, sort_keys=True))

    # garde de la fonction de lecture (plan, point 5) : chaque couche lue, chaque lentille
    charge = charger_montage(ctx)
    # addendum, EC-6 (couple H2) : paires de jetons gardés de même ligne de sortie, comptées et écrites, sans arrêt
    rapport["lignes_de_sortie_egales"] = st.paires_de_lignes_egales(_np(charge.wu))
    graines = nu.Graines()
    rapport["garde_fonction_lecture"] = jouer_garde_lecture(charge, graines, r)
    rapport["graines"] = {k: str(v) for k, v in sorted(graines.derivees.items())}
    horloge.controler("garde de la fonction de lecture")

    rapport["gardes"] = {"toutes_tenues": True, "liste": [
        "clé présente et non vide", "aucun mode de débogage", "espace disque au départ", "essais d'un octet", "commit du voisin",
        "readout.py égal à la copie versée", "empreintes des correctifs", "petits fichiers (taille, identifiant git)",
        "fiche du code citée par CODE-LENTILLES-BBIS", "ligne ADDENDUM-CONCENTRATION-LENTILLES-BBIS égale à la fiche du code",
        "tokeniseur lu du cache par le voisin, hors ligne et sans clé",
        "pointeurs des poids", "SHA-256 des flux de poids", "licences de la lentille", "taille et SHA-256 de la lentille",
        "disposition, provenance et 31 matrices de la lentille", "jetons gardés (nombre, empreinte)",
        "garde de la fonction de lecture"]}
    rapport["duree_cumulee_s"] = horloge.ecoule()
    chemin = ctx.sortie / "diag" / ctx.run / "montage-lentilles-bbis.json"
    sha = _ecrire_ferme(chemin, rapport)
    mo.aucune_occurrence([ctx.travail, ctx.sortie], cle)
    horloge.consigner()
    return {"chemin": str(chemin), "sha256": sha,
            "ligne_proposee": ligne_registre("MONTAGE-LENTILLES-BBIS", f"diag/{ctx.run}/montage-lentilles-bbis.json", sha)}


SCRIPT_TOKENISEUR = ("from neuron_lens import catalog\n"
                     "tok = catalog.tokenizer(catalog.MODEL)\n"
                     "assert isinstance(tok.decode([0]), str)\n")


def essayer_tokeniseur_du_cache(ctx: Contexte, voisin: Path, hf_home: Path) -> None:
    """Juste après la pose du cache, avant tout flux long : un processus enfant **hors ligne et sans clé** charge le tokeniseur
    par le catalogue du voisin et décode un jeton. Un échec ici évite de le découvrir après les flux de poids (contre-lecture,
    § 6) : arrêt ; nœud."""
    try:
        mo.jouer_script([ctx.python, "-c", SCRIPT_TOKENISEUR], voisin, mo.environnement_enfant(voisin, hf_home, True, ctx.env),
                        ctx.travail / "journal-essai-tokeniseur.txt")
    except Arret:
        raise Arret("le code voisin ne lit pas le tokeniseur du cache posé, hors ligne et sans clé (journal-essai-tokeniseur.txt) : "
                    "arrêt avant tout flux long ; nœud") from None


@dataclass
class Charge:
    """Ce que le calcul lit du dossier de travail monté."""
    wu: torch.Tensor
    gamma: torch.Tensor
    ids_gardes: np.ndarray
    chaines: list
    publique: le.LentillePublique
    lire_voisin: object
    etat: dict
    travail: Path

    def w_down(self, couche: int) -> torch.Tensor:
        d = self.etat["tenseurs"][f"model.layers.{int(couche)}.mlp.down_proj.weight"]
        return torch.from_numpy(mo.charger_tenseur(self.travail / "tenseurs", d))


def charger_montage(ctx: Contexte) -> Charge:
    """Recharge le montage ; lentille publique absente : arrêt (jamais de lecture par la seule lentille des logits)."""
    r = ctx.reglages
    chemin_etat = ctx.travail / "etat-montage.json"
    if not chemin_etat.is_file():
        raise Arret("montage absent du dossier de travail : rien ne part")
    etat = json.loads(chemin_etat.read_text())
    matrices = {}
    for c in r.couches:
        p = ctx.travail / "lentille" / f"J-{c}.npy"
        if not p.is_file():
            raise Arret("lentille publique absente : arrêt ; message à la mère ; jamais remplacée par une autre lentille ; la "
                        "lecture par la seule lentille des logits n'est pas rendue")
        matrices[int(c)] = np.load(p, allow_pickle=False)
    publique = le.LentillePublique(matrices, {int(k): v for k, v in etat["empreintes_matrices"].items()})
    jetons = json.loads((ctx.travail / "jetons-gardes.json").read_text(encoding="utf-8"))
    mo.exiger_jetons_gardes(jetons["ids"], r.n_jetons, r.sha256_jetons)
    ids = np.asarray(jetons["ids"], dtype=np.int64)
    dossier = ctx.travail / "tenseurs"
    wu = torch.from_numpy(mo.charger_tenseur(dossier, etat["tenseurs"]["lm_head.weight"], lignes=ids))
    gamma = torch.from_numpy(mo.charger_tenseur(dossier, etat["tenseurs"]["model.norm.weight"]))
    if wu.shape != (len(ids), r.largeur) or gamma.shape != (r.largeur,):
        raise Arret("formes de lm_head.weight ou de model.norm.weight inattendues : arrêt")
    return Charge(wu, gamma, ids, list(jetons["chaines"]), publique, mo.charger_read_voisin(ctx.travail / etat["readout"]),
                  etat, ctx.travail)


def jouer_garde_lecture(charge: Charge, graines: nu.Graines, r: Reglages) -> list[dict]:
    """Plan, point 5 : à chaque couche lue et pour chaque lentille, cas sain et artefact ; un échec : arrêt avant tout calcul."""
    sortie = []
    couches = sorted(r.couches)
    for i, couche in enumerate(couches):
        w_down = charge.w_down(couche)
        colonnes = w_down[:, torch.as_tensor(nu.colonnes_garde(graines, couche, w_down.shape[1], r.n_colonnes_garde))]
        j_sain, _, _ = charge.publique.matrice(couche)
        j_suivante, _, _ = charge.publique.matrice(couches[(i + 1) % len(couches)])      # ordre 7 → 15 → 23 → 7
        sortie.append(le.garde_fonction_lecture(charge.lire_voisin, colonnes, charge.gamma, charge.wu, j_sain, j_suivante,
                                                K.LENTILLE_PUBLIQUE, couche))
        permutation = le.matrice_permutation(nu.permutation_garde_logits(graines, couche, r.largeur))
        sortie.append(le.garde_fonction_lecture(charge.lire_voisin, colonnes, charge.gamma, charge.wu, None, permutation,
                                                K.LENTILLE_LOGITS, couche))
    return sortie


# --- calcul (plan, point 6) ----------------------------------------------------------------------------------------------------------------
def _echappe(chaine: str) -> str:
    return json.dumps(chaine, ensure_ascii=True)[1:-1]


def _np(t: torch.Tensor) -> np.ndarray:
    return t.detach().cpu().numpy()


class _Couche:
    """Calcul d'une couche : lectures, nuls, témoins, garde du rapport à ε, pôles, témoin de couche."""

    def __init__(self, couche: int, vecteurs: list, charge: Charge, graines: nu.Graines, r: Reglages, masques: dict,
                 tableaux: dict, horloge: Horloge, controle_disque):
        self.couche, self.vecteurs, self.charge, self.graines, self.r = int(couche), vecteurs, charge, graines, r
        self.masques, self.tableaux, self.horloge, self.controle_disque = masques, tableaux, horloge, controle_disque
        self.rho: dict[str, list[float]] = {l: [] for l in K.LENTILLES}
        self.p_temoins: dict[tuple[str, str], list[np.ndarray]] = {}
        # garde d'égalité au vingtième rang (EC-6) : comptes par (lentille, nul), écrits dans les tables
        self.egalites: dict[tuple[str, str], dict] = {}
        self.matrices = {l: le.jacobienne_de(l, self.couche, charge.publique) for l in K.LENTILLES}
        self.w_down = charge.w_down(self.couche)

    def _lire(self, v, lentille: str) -> tuple[torch.Tensor, np.ndarray]:
        scores, rho = le.lire(v, self.matrices[lentille][0], self.charge.gamma, self.charge.wu)
        self.rho[lentille].append(float(rho.min()))
        return scores, rho

    def _compter(self, lentille: str, nul: str, resume: st.ResumeNul | None = None, temoins: torch.Tensor | None = None) -> None:
        """EC-6, étages (ii) et (iii) : directions nulles marquées et témoins à égalité au vingtième rang, par (lentille, nul)."""
        c = self.egalites.setdefault((lentille, nul), {"directions_nulles": 0, "directions_nulles_marquees": 0, "temoins": 0,
                                                       "temoins_a_egalite_au_vingtieme_rang": 0, "garde_sans_objet": False})
        if resume is not None:
            c["directions_nulles"] += resume.m
            c["directions_nulles_marquees"] += resume.n_marquees
            c["garde_sans_objet"] = bool(c["garde_sans_objet"] or resume.garde_sans_objet)
        if temoins is not None:
            e = st.egalites_temoins(temoins)
            c["temoins"] += e["temoins"]
            c["temoins_a_egalite_au_vingtieme_rang"] += e["a_egalite_au_vingtieme_rang"]
            c["garde_sans_objet"] = bool(c["garde_sans_objet"] or e["garde_sans_objet"])

    def _range_resume(self, prefixe: str, resume: st.ResumeNul) -> None:
        self.tableaux[f"nul__{prefixe}__moyenne"] = _np(resume.moyenne)
        self.tableaux[f"nul__{prefixe}__ecart_type"] = _np(resume.ecart_type)
        self.tableaux[f"nul__{prefixe}__quantile_0_99"] = _np(resume.quantile)
        self.tableaux[f"directions_nulles__{prefixe}__concentration"] = _np(resume.concentration)
        self.tableaux[f"directions_nulles__{prefixe}__marquee"] = _np(resume.marquee)
        self.tableaux[f"directions_nulles__{prefixe}__part_min"] = _np(resume.part_min)
        self.tableaux[f"directions_nulles__{prefixe}__part_max"] = _np(resume.part_max)
        for nom in resume.familles_min:
            self.tableaux[f"directions_nulles__{prefixe}__famille_{nom}_min"] = _np(resume.familles_min[nom])
            self.tableaux[f"directions_nulles__{prefixe}__famille_{nom}_max"] = _np(resume.familles_max[nom])

    def _signes(self, a: torch.Tensor, nuls: dict, contexte: dict) -> dict:
        return {"+": st.lecture_signe(a, nuls, self.masques, self.charge.ids_gardes, contexte=contexte | {"signe": "+"}),
                "-": st.lecture_signe(-a, nuls, self.masques, self.charge.ids_gardes, contexte=contexte | {"signe": "-"})}

    def calculer(self) -> tuple[dict, list[dict]]:
        r, c, d = self.r, self.couche, self.r.largeur
        u_iso = torch.from_numpy(nu.nul_isotrope(self.graines, c, d, r.m))
        t_iso = torch.from_numpy(nu.temoins_isotropes(self.graines, c, d, r.n_temoins_isotrope))
        iso = {}
        for lentille in K.LENTILLES:
            a_iso, _ = self._lire(u_iso, lentille)
            resume = st.resumer_nul(a_iso, self.masques)
            self._range_resume(f"couche{c}__{lentille}__{K.NUL_ISOTROPE}", resume)
            s_t, _ = self._lire(t_iso, lentille)
            self._compter(lentille, K.NUL_ISOTROPE, resume, s_t)
            p = st.p_temoins(s_t, resume)
            self.tableaux[f"temoins__couche{c}__{lentille}__{K.NUL_ISOTROPE}__p"] = p
            self.p_temoins[(lentille, K.NUL_ISOTROPE)] = [p]
            iso[lentille] = (a_iso, resume)
        directions = []
        for sonde, nom_v, v_np in self.vecteurs:
            self.horloge.controler(f"couche {c}, {sonde.cle}/{nom_v}")
            self.controle_disque()
            ident = f"{sonde.cellule}__{sonde.pli}__{sonde.role}__{nom_v}"
            v = torch.from_numpy(np.asarray(v_np, dtype=np.float32))
            u_s_np = nu.nul_signes(self.graines, v_np, sonde.cellule, sonde.pli, sonde.role, nom_v, r.m)
            u_s = torch.from_numpy(u_s_np)
            t_s = torch.from_numpy(nu.temoins_signes(self.graines, v_np, c, sonde.cellule, sonde.pli, sonde.role, nom_v,
                                                     r.n_temoins_par_vecteur))
            ligne = {"sonde": sonde.cle, "cellule": sonde.cellule, "pli": sonde.pli, "role": sonde.role, "vecteur": nom_v,
                     "couche": c, "non_calculable": None, "norme": float(np.linalg.norm(np.asarray(v_np, np.float64))),
                     "lectures": {}, "_v": v_np, "_ident": ident}
            ou = {"cellule": sonde.cellule, "pli": sonde.pli, "role": sonde.role, "vecteur": nom_v, "couche": c}
            ligne["_ou"] = ou
            for lentille in K.LENTILLES:
                a, rho = self._lire(v, lentille)
                a = a[:, 0]
                a_s, _ = self._lire(u_s, lentille)
                resume_s = st.resumer_nul(a_s, self.masques)
                self._range_resume(f"{ident}__{lentille}__{K.NUL_SIGNES}", resume_s)
                s_t, _ = self._lire(t_s, lentille)
                self._compter(lentille, K.NUL_SIGNES, resume_s, s_t)
                p = st.p_temoins(s_t, resume_s)
                self.tableaux[f"temoins__{ident}__{lentille}__{K.NUL_SIGNES}__p"] = p
                self.p_temoins.setdefault((lentille, K.NUL_SIGNES), []).append(p)
                self.tableaux[f"scores__{ident}__{lentille}"] = _np(a)
                _, indice, empreinte = self.matrices[lentille]
                ligne["lectures"][lentille] = {
                    "indice_matrice": indice, "empreinte_matrice": empreinte, "rapport_epsilon": float(rho[0]),
                    "signes": self._signes(a, {K.NUL_ISOTROPE: iso[lentille], K.NUL_SIGNES: (a_s, resume_s)},
                                           ou | {"lentille": lentille}), "_a": a}
                del a_s, s_t
            ligne["poles"] = self._poles(v, {K.NUL_ISOTROPE: u_iso, K.NUL_SIGNES: u_s}, ou)
            ligne["lectures"][K.LENTILLE_PUBLIQUE]["temoin_de_couche"] = self._temoin_de_couche(v, ligne, ident)
            directions.append(ligne)
            del u_s, t_s
        # garde du rapport à ε, par (couche, lentille) ; repli pour les deux lentilles de la couche
        minima = {l: (min(x) if x else None) for l, x in self.rho.items()}
        tenue = all(le.independance_tenue(m) for m in minima.values() if m is not None)
        if not tenue:
            self._repli(directions)
        resume_couche = {"lentilles": {}, "independance_a_la_norme_tenue": bool(tenue), "repli_nuls_par_direction": not tenue,
                         "directions": len(directions)}
        for lentille in K.LENTILLES:
            _, indice, empreinte = self.matrices[lentille]
            cal = {nul: au.calibration(p, r.m) for (l, nul), p in sorted(self.p_temoins.items()) if l == lentille and p}
            minimum = min(self.rho[lentille]) if self.rho[lentille] else None
            resume_couche["lentilles"][lentille] = {
                "indice_matrice": indice, "empreinte_matrice": empreinte, "rapport_epsilon_minimal": minimum,
                "independance_tenue": None if minimum is None else le.independance_tenue(minimum), "calibration": cal,
                "egalites_au_vingtieme_rang": {nul: dict(e) for (l, nul), e in sorted(self.egalites.items()) if l == lentille}}
        return resume_couche, directions

    def _poles(self, v: torch.Tensor, nuls: dict, ou: dict) -> dict:
        """Les deux listes de dix des pôles entrent sous l'arrêt de la direction lue (EC-6, étage (i), couple G3) : les dix
        pôles par cosinus (`st.poles_alignes`) et les dix premiers jetons de la lecture de chaque pôle."""
        pa = st.poles_alignes(v, self.w_down, nuls, contexte=ou | {"signe": "+", "lentille": "sans objet (cosinus)"})
        j_pub = self.matrices[K.LENTILLE_PUBLIQUE][0]
        for p in pa["poles"]:
            colonne = self.w_down[:, p["neurone"]] * (1.0 if p["signe"] == "+" else -1.0)
            scores, _ = le.lire(colonne, j_pub, self.charge.gamma, self.charge.wu)
            haut = st.exiger_sans_egalite(scores[:, 0], K.K_JETONS_POLE,
                                          st.LISTE_JETONS_POLE.format(neurone=p["neurone"], signe=p["signe"]),
                                          self.charge.ids_gardes, ou | {"signe": "+", "lentille": K.LENTILLE_PUBLIQUE})
            rangs = haut["rangs"].tolist()
            p["lecture_publique"] = {"ids": [int(self.charge.ids_gardes[i]) for i in rangs],
                                     "chaines_echappees": [_echappe(self.charge.chaines[i]) for i in rangs]}
        maxima = pa.pop("maxima_nuls")
        return pa | {"_maxima": maxima}

    def _temoin_de_couche(self, v: torch.Tensor, ligne: dict, ident: str) -> dict:
        """Lentille publique seulement : jetons communs entre la lecture de v à sa couche et à chacune des deux autres."""
        a = ligne["lectures"][K.LENTILLE_PUBLIQUE]["_a"]
        sortie = {}
        for autre in sorted(self.r.couches):
            if autre == self.couche:
                continue
            j, _, _ = self.charge.publique.matrice(autre)
            b, _ = le.lire(v, j, self.charge.gamma, self.charge.wu)
            b = b[:, 0]
            self.tableaux[f"scores_temoin_de_couche__{ident}__c{autre}"] = _np(b)
            sortie[str(autre)] = {}
            for s, f in (("+", 1.0), ("-", -1.0)):          # listes du témoin de couche : EC-6, étage (i)
                ou = ligne["_ou"] | {"signe": s, "lentille": K.LENTILLE_PUBLIQUE}
                ici = st.exiger_sans_egalite(f * a, K.K_JETONS, st.LISTE_TEMOIN_DE_COUCHE.format(couche=self.couche),
                                             self.charge.ids_gardes, ou)
                la_bas = st.exiger_sans_egalite(f * b, K.K_JETONS, st.LISTE_TEMOIN_DE_COUCHE.format(couche=autre),
                                                self.charge.ids_gardes, ou)
                sortie[str(autre)][s] = st.jetons_communs(ici["rangs"].tolist(), la_bas["rangs"].tolist())
        return sortie

    def _repli(self, directions: list[dict]) -> None:
        """Indépendance à la norme non tenue : pour les deux lentilles de la couche, nul isotrope refait par vecteur, à la
        norme de v ; 200 témoins par vecteur ; les lectures faites avec le nul partagé restent en table, « remplacées »."""
        r, c = self.r, self.couche
        for ligne in directions:
            v_np = ligne["_v"]
            arg = (ligne["cellule"], ligne["pli"], ligne["role"], ligne["vecteur"])
            self.horloge.controler(f"couche {c}, repli {ligne['sonde']}/{ligne['vecteur']}")
            u_d = torch.from_numpy(nu.nul_isotrope_par_direction(self.graines, v_np, *arg, r.m))
            t_d = torch.from_numpy(nu.temoins_isotropes_par_direction(self.graines, v_np, c, *arg, r.n_temoins_par_vecteur))
            for lentille in K.LENTILLES:
                a_d, _ = self._lire(u_d, lentille)
                resume = st.resumer_nul(a_d, self.masques)
                self._range_resume(f"{ligne['_ident']}__{lentille}__{K.NUL_ISOTROPE_PAR_DIRECTION}", resume)
                s_t, _ = self._lire(t_d, lentille)
                self._compter(lentille, K.NUL_ISOTROPE_PAR_DIRECTION, resume, s_t)
                p = st.p_temoins(s_t, resume)
                self.tableaux[f"temoins__{ligne['_ident']}__{lentille}__{K.NUL_ISOTROPE_PAR_DIRECTION}__p"] = p
                self.p_temoins.setdefault((lentille, K.NUL_ISOTROPE_PAR_DIRECTION), []).append(p)
                lecture = ligne["lectures"][lentille]
                neuf = self._signes(lecture["_a"], {K.NUL_ISOTROPE_PAR_DIRECTION: (a_d, resume)},
                                    ligne["_ou"] | {"lentille": lentille})
                for s in ("+", "-"):
                    lecture["signes"][s]["nuls"][K.NUL_ISOTROPE]["remplacee"] = True
                    lecture["signes"][s]["nuls"][K.NUL_ISOTROPE_PAR_DIRECTION] = neuf[s]["nuls"][K.NUL_ISOTROPE_PAR_DIRECTION]
                del a_d, s_t
            v = torch.from_numpy(np.asarray(v_np, dtype=np.float32))
            pa = st.poles_alignes(v, self.w_down, {K.NUL_ISOTROPE_PAR_DIRECTION: u_d},
                                  contexte=ligne["_ou"] | {"signe": "+", "lentille": "sans objet (cosinus)"})
            poles = ligne["poles"]
            poles["p"][K.NUL_ISOTROPE + "_remplacee"] = poles["p"].pop(K.NUL_ISOTROPE)
            poles["p"][K.NUL_ISOTROPE_PAR_DIRECTION] = pa["p"][K.NUL_ISOTROPE_PAR_DIRECTION]
            poles["_maxima"][K.NUL_ISOTROPE_PAR_DIRECTION] = pa["maxima_nuls"][K.NUL_ISOTROPE_PAR_DIRECTION]
            for p_ancien, p_neuf in zip(poles["poles"], pa["poles"]):
                p_ancien["rang_parmi_maxima_nuls"] |= p_neuf["rang_parmi_maxima_nuls"]


def _nul_isotrope_en_vigueur(repli: bool) -> str:
    return K.NUL_ISOTROPE_PAR_DIRECTION if repli else K.NUL_ISOTROPE


def _etiqueter(directions: list[dict], couches: dict, chaines: list, ids_gardes: np.ndarray) -> list[dict]:
    """Libellés (« Seuil ») de chaque lecture, de sa part au-dessus du nul, de ses familles et de ses pôles ; une calibration
    hors de ses bornes rend « non calculables » les tables de cette couche, de cette lentille et de ce nul. Rend les lignes
    de lecture pour les déclencheurs d'audit. Addendum, EC-6, étage (ii) : le libellé de la part et celui de chaque famille
    sont calculés avec p_bas sous les deux nuls puis avec p_haut sous les deux nuls ; égaux : le libellé est celui-là ;
    différents : arrêt nommé, avant toute écriture de table. La concentration n'emploie aucune liste de premiers."""
    rang_de = {int(i): n for n, i in enumerate(ids_gardes.tolist())}
    lignes = []
    for d in directions:
        info = couches[str(d["couche"])]
        nul_iso = _nul_isotrope_en_vigueur(info["repli_nuls_par_direction"])
        for lentille, lecture in d["lectures"].items():
            cal = info["lentilles"][lentille]["calibration"]
            hors = [nul for nul in (nul_iso, K.NUL_SIGNES) if not cal[nul]["tenue"]]
            for signe, t in lecture["signes"].items():
                t["premiers_par_score"]["chaines_echappees"] = [_echappe(chaines[rang_de[i]]) for i in t["premiers_par_score"]["ids"]]
                for nul_table in t["nuls"].values():
                    if "premiers_par_z" in nul_table:
                        nul_table["premiers_par_z"]["chaines_echappees"] = [_echappe(chaines[rang_de[i]])
                                                                          for i in nul_table["premiers_par_z"]["ids"]]
                for nul in hors:
                    t["nuls"][nul] = {"non_calculable": au.MOTIF_CALIBRATION}
                if hors:
                    t |= {"libelle": None, "libelle_part": None, "non_calculable": au.MOTIF_CALIBRATION, "nul_isotrope_en_vigueur": nul_iso}
                    for f in t["familles"].values():
                        f["sur_representee"] = None
                else:
                    i, s = t["nuls"][nul_iso], t["nuls"][K.NUL_SIGNES]
                    ou = d["_ou"] | {"signe": signe, "lentille": lentille}
                    marquees = (i["directions_nulles_marquees"], s["directions_nulles_marquees"])
                    t |= {"libelle": st.libelle(i["p_concentration"], s["p_concentration"]),
                          "libelle_part": st.libelle_sous_departage(st.libelle, "part au-dessus du nul", {
                              "isotrope": (nul_iso, i["p_part_bas"], i["p_part_haut"], marquees[0]),
                              "signes": (K.NUL_SIGNES, s["p_part_bas"], s["p_part_haut"], marquees[1])}, ou),
                          "nul_isotrope_en_vigueur": nul_iso}
                    for nom, f in t["familles"].items():
                        fi, fs = i["familles"][nom], s["familles"][nom]
                        f["sur_representee"] = st.libelle_sous_departage(st.sur_representee, f"compte de la famille {nom}", {
                            "isotrope": (nul_iso, fi["p_bas"], fi["p_haut"], marquees[0]),
                            "signes": (K.NUL_SIGNES, fs["p_bas"], fs["p_haut"], marquees[1])}, ou)
                lignes.append({"sonde": d["sonde"], "role": d["role"], "vecteur": d["vecteur"], "signe": signe, "couche": d["couche"],
                               "lentille": lentille, "libelle": t["libelle"], "ids": t["premiers_par_score"]["ids"]})
        p = d["poles"]["p"]
        d["poles"]["libelle"] = st.libelle(p[nul_iso], p[K.NUL_SIGNES])
        d["poles"]["nul_isotrope_en_vigueur"] = nul_iso
        d["accord_lentilles"] = {s: st.jetons_communs(d["lectures"][K.LENTILLE_PUBLIQUE]["signes"][s]["premiers_par_score"]["ids"],
                                                      d["lectures"][K.LENTILLE_LOGITS]["signes"][s]["premiers_par_score"]["ids"])
                                 for s in ("+", "-")}
    return lignes


def _comparaisons(directions: list[dict]) -> list[dict]:
    """Comparaisons appariées, descriptives (« Métrique », point 8)."""
    par_cle = {(d["cellule"], d["pli"], d["role"], d["vecteur"]): d for d in directions}
    paires = []
    for cellule in K.CELLULES:
        for pli in K.PLIS:
            for v in ("w", "q"):
                paires.append(("sonde-lecteur", (cellule, pli, "sonde", v), (cellule, pli, "enc", v)))
        for role in K.ROLES:
            for v in ("w", "q"):
                paires.append(("plis", (cellule, "e0", role, v), (cellule, "e1", role, v)))
    for pli in K.PLIS:
        for role in K.ROLES:
            for v in ("w", "q"):
                for i, a in enumerate(K.CELLULES_DOSES):
                    for b in K.CELLULES_DOSES[i + 1:]:
                        paires.append(("doses", (a, pli, role, v), (b, pli, role, v)))
    sortie = []
    for sorte, a, b in paires:
        if a not in par_cle or b not in par_cle:
            continue
        da, db = par_cle[a], par_cle[b]
        ligne = {"type": sorte, "a": "/".join(a), "b": "/".join(b), "couche_a": da["couche"], "couche_b": db["couche"]}
        if da["couche"] != db["couche"]:
            ligne |= {"cosinus": None, "sans_objet": "couches différentes : sans objet"}
        else:
            ligne["cosinus"] = st.cosinus(da["_v"], db["_v"])
            ligne["jetons_communs"] = {
                lentille: {s: st.jetons_communs(da["lectures"][lentille]["signes"][s]["premiers_par_score"]["ids"],
                                                db["lectures"][lentille]["signes"][s]["premiers_par_score"]["ids"])
                           for s in ("+", "-")} for lentille in K.LENTILLES}
        sortie.append(ligne)
    return sortie


def _comptes(directions: list[dict]) -> dict:
    """Comptes de libellés, chacun avec son attendu par le seul hasard (« Seuil »), et nombre total de lectures."""
    lectures = [t for d in directions for l in d["lectures"].values() for t in l["signes"].values()]
    n = len(lectures)

    def compte(cle: str) -> dict:
        c: dict = {}
        for t in lectures:
            c[str(t[cle])] = c.get(str(t[cle]), 0) + 1
        return c
    sur = sum(1 for t in lectures for f in t["familles"].values() if f.get("sur_representee"))
    poles: dict = {}
    for d in directions:
        poles[d["poles"]["libelle"]] = poles.get(d["poles"]["libelle"], 0) + 1
    return {"nombre_total_de_lectures": n,
            "concentration": {"comptes": compte("libelle"), "attendu_par_hasard_au_plus": n * K.P_ISO_CONCENTREE},
            "part_au_dessus_du_nul": {"comptes": compte("libelle_part"), "attendu_par_hasard_au_plus": n * K.P_ISO_CONCENTREE},
            "poles": {"comptes": poles, "nombre": len(directions), "attendu_par_hasard_au_plus": len(directions) * K.P_ISO_CONCENTREE},
            "familles_sur_representees": {"compte": sur, "attendu_par_hasard_au_plus": n * 2 * K.P_FAMILLE}}


def _audit(entrees: en.Entrees, directions: list[dict], couches: dict, charge: Charge, graines: nu.Graines, etat: dict) -> dict:
    """Audit de symétrie, joué dans la session du calcul. Issue écrite en réserve ; aucune table ne change."""
    empreintes = all(en.empreinte_sonde(s.famille, s.nom, s.couche, s.agregation, s.w, s.b, s.q) == s.empreinte
                     for s in entrees.sondes if s.lue)
    choisies = []
    if directions:
        ordre = graines.rng(nu.cle_essai("audit-chemin-independant")).permutation(len(directions))[:2]
        for i in sorted(int(x) for x in ordre):
            d = directions[i]
            j = charge.publique.matrices[d["couche"]].astype(np.float64)
            relue = au.relire_par_chemin_independant(d["_v"], j, _np(charge.gamma), _np(charge.wu))
            lue = _np(d["lectures"][K.LENTILLE_PUBLIQUE]["_a"])
            oppose, _ = le.lire(-torch.from_numpy(np.asarray(d["_v"], np.float32)), charge.publique.matrice(d["couche"])[0],
                                charge.gamma, charge.wu)
            garde = st.premiers_gardes(torch.from_numpy(relue["scores"]), K.K_JETONS)
            choisies.append({"direction": f"{d['sonde']}/{d['vecteur']}", **au.comparer_relecture(lue, relue),
                             "egalite_au_vingtieme_rang_de_la_relecture_en_double_precision": garde["egalite"],
                             "imparite_ecart_maximal": float(np.max(np.abs(_np(oppose[:, 0]) + lue)))})
    return {"contenu": list(au.CONTENU_AUDIT),
            "empreintes_des_tableaux_lus_egales_a_E2": bool(empreintes),
            "couches": [{"direction": f"{d['sonde']}/{d['vecteur']}", "couche_de_la_sonde": d["couche"],
                         "indice_de_la_matrice": d["lectures"][K.LENTILLE_PUBLIQUE]["indice_matrice"],
                         "empreinte_de_la_matrice": d["lectures"][K.LENTILLE_PUBLIQUE]["empreinte_matrice"]} for d in directions],
            "convention_du_harnais": "couche ℓ = sortie du bloc ℓ, indice depuis 0, avant la normalisation finale",
            "point_de_capture_de_la_lentille": etat.get("point_de_capture"),
            "conventions_de_signe": "signe + : vers la classe positive ; a(−v) = −a(v), écart mesuré sur les directions relues",
            "decodage": {"jetons_gardes": int(charge.ids_gardes.size), "chaines": len(charge.chaines)},
            "rapport_epsilon_minimal": {c: {l: v["rapport_epsilon_minimal"] for l, v in info["lentilles"].items()}
                                        for c, info in couches.items()},
            "directions_relues_par_un_chemin_independant": choisies,
            "issue": "écrite en réserve ; aucune table ne change"}


def _retirer_prives(objet):
    if isinstance(objet, dict):
        return {k: _retirer_prives(v) for k, v in objet.items() if not str(k).startswith("_")}
    if isinstance(objet, list):
        return [_retirer_prives(x) for x in objet]
    return objet


# Arrêts cloisonnés (version 5) : le message entier ne va que dans `arret.json` ; la ligne de commande n'en affiche que le nom.
# (classe, nom affiché) : le nom affiché est un code fixe, égal au nom de la classe.
ARRETS_CLOISONNES = ((st.EgaliteDirectionLue, "EgaliteDirectionLue"), (st.EgaliteNulleDecisive, "EgaliteNulleDecisive"))


def nom_d_arret_cloisonne(arret: BaseException) -> str | None:
    """Nom affiché d'un arrêt cloisonné ; `None` pour tout autre arrêt (sa sortie est celle de `lanceur_v4`)."""
    for classe, nom in ARRETS_CLOISONNES:
        if isinstance(arret, classe):
            return nom
    return None


def verser_arret_cloisonne(ctx: Contexte, arret: Arret, tableaux: dict, parti: bool) -> None:
    """Versement à l'arrêt d'un arrêt cloisonné. Le message entier (`str(arret)`) est écrit dans le seul `arret.json`, champ
    `motif` ; il n'entre dans aucune autre exception ni aucune impression. Ne lève aucune exception de la classe `Exception` :
    un échec du versement (R12, disque, copie) est écrit dans `arret.json` (`versement_en_echec`) quand ce fichier peut
    l'être, et noté sur l'arrêt (`versement_en_echec`, `fichier_d_arret`), que la ligne de commande lit. Un arrêt cloisonné
    levé avant le départ du calcul (aucun chemin du code n'y mène ; défense) écrit quand même son `arret.json`, sans rien
    verser du dossier de travail."""
    try:                                    # version 6 : rien de cette fonction n'est hors de la coupure, première ligne comprise
        arret.fichier_d_arret, arret.versement_en_echec = None, False
        dest = ctx.sortie / "versement" / ctx.run / "calcul-interrompu"
        try:
            contenu = {"run": ctx.run, "motif": str(arret), "morceaux": [], "travail": None}
            try:
                if parti:
                    contenu["morceaux"] = ecrire_morceaux(tableaux, dest / "lectures-interrompues-non-lues") if tableaux else []
                    contenu["travail"] = verser_travail(ctx.travail, ctx.sortie, ctx.run, "arret")
                else:
                    contenu["avant_le_depart_du_calcul"] = True
            except Exception as e:
                arret.versement_en_echec = True
                contenu["versement_en_echec"] = f"{type(e).__name__} : {e}"
            _ecrire_ferme(dest / "arret.json", contenu)
            arret.fichier_d_arret = dest / "arret.json"
        except Exception:
            pass                            # `arret.json` non écrit (il existe déjà, R12, ou le disque refuse) : `fichier_d_arret` reste vide
    except BaseException as e:              # interruption pendant le versement : sa trace ne porte pas le message de l'arrêt
        raise e from None


# Mots fixes de la ligne affichée pour un arrêt cloisonné (inchangés depuis la version 5). Pour n'afficher que le nom de
# l'arrêt, une seule constante change : `LIGNE_ARRET_CLOISONNE = "{nom}"` (nœud posé au directeur ; non tranché ici).
LIGNE_ARRET_CLOISONNE = "ARRÊT : {nom} ; {fichier}{echec}"
MOTS_FICHIER_D_ARRET_ECRIT = "fichier d'arrêt : {chemin}"
MOTS_FICHIER_D_ARRET_NON_ECRIT = "fichier d'arrêt non écrit"
MOTS_VERSEMENT_EN_ECHEC = " ; versement à l'arrêt en échec : rien n'est supprimé"


def ligne_d_arret_cloisonne(arret: Arret) -> str:
    """La seule ligne que la ligne de commande affiche pour un arrêt cloisonné : des mots fixes, le nom de l'arrêt et le
    chemin du fichier d'arrêt (une existence). Jamais le message : ni identifiant de jeton, ni valeur, ni borne de valeur p,
    ni nom de statistique."""
    fichier = getattr(arret, "fichier_d_arret", None)
    return LIGNE_ARRET_CLOISONNE.format(
        nom=nom_d_arret_cloisonne(arret),
        fichier=MOTS_FICHIER_D_ARRET_ECRIT.format(chemin=fichier) if fichier is not None else MOTS_FICHIER_D_ARRET_NON_ECRIT,
        echec=MOTS_VERSEMENT_EN_ECHEC if getattr(arret, "versement_en_echec", False) else "")


def chemin_du_fichier_d_arret(ctx: Contexte) -> Path:
    """Le chemin où l'arrêt d'une course est écrit par l'enveloppe du calcul."""
    return ctx.sortie / "versement" / ctx.run / "calcul-interrompu" / "arret.json"


def exiger_aucun_fichier_d_arret(ctx: Contexte) -> None:
    """Garde de la version 7 (GO-2026-11-21-06) : un `arret.json` existe déjà au chemin où l'arrêt de cette course serait
    écrit : rien ne part. Rien n'est écrit, rien n'est supprimé. Sans elle, un second arrêt dans le même dossier de sortie ne
    pourrait pas écrire son message (R12 : on n'écrase pas). Arrêt ordinaire, non cloisonné : son message ne porte que le chemin."""
    fichier = chemin_du_fichier_d_arret(ctx)
    if fichier.exists() or fichier.is_symlink():
        raise Arret(f"un fichier d'arrêt existe déjà pour cette course ({fichier}) : rien ne part ; rien n'est écrit, rien n'est "
                    "supprimé")


def calculer(ctx: Contexte, racine_entrees: Path, registre_bbis: Path, nettoyage: bool = True) -> dict:
    """Enveloppe du calcul : à tout arrêt après le départ du calcul, ce qui existe est versé (dossier de travail inventorié et
    ses fichiers hors licence copiés ; tableaux déjà calculés écrits, fermés, scellés, marqués « interrompus, non lus »), rien
    n'est supprimé, puis l'arrêt est relevé tel quel. Un arrêt cloisonné (`ARRETS_CLOISONNES`) est versé par
    `verser_arret_cloisonne`, puis relevé tel quel, pour l'appelant Python ; son message ne sort que dans `arret.json`.
    Version 7 : avant tout, la garde du fichier d'arrêt déjà présent (`exiger_aucun_fichier_d_arret`), hors de l'enveloppe."""
    exiger_aucun_fichier_d_arret(ctx)
    tableaux: dict[str, np.ndarray] = {}
    etat = {"parti": False}
    try:
        return _calculer(ctx, racine_entrees, registre_bbis, nettoyage, tableaux, etat)
    except Arret as arret:
        try:                                # version 6 : le tri et le versement sous la coupure de l'enchaînement
            cloisonne = nom_d_arret_cloisonne(arret) is not None
            if cloisonne:
                verser_arret_cloisonne(ctx, arret, tableaux, etat["parti"])
        except BaseException as e:          # interruption entre l'arrêt et son relevé : sa trace ne porte pas le message
            raise e from None
        if cloisonne:
            raise
        if not etat["parti"]:
            raise                       # refus avant le départ (registres, verdict, dossier monté) : rien n'est versé
        dest = ctx.sortie / "versement" / ctx.run / "calcul-interrompu"
        try:
            morceaux = ecrire_morceaux(tableaux, dest / "lectures-interrompues-non-lues") if tableaux else []
            _ecrire_ferme(dest / "arret.json", {"run": ctx.run, "motif": str(arret), "morceaux": morceaux,
                                                "travail": verser_travail(ctx.travail, ctx.sortie, ctx.run, "arret")})
        except Arret as e:
            raise Arret(f"{arret} ; versement à l'arrêt en échec ({e}) : rien n'est supprimé") from None
        raise


def _calculer(ctx: Contexte, racine_entrees: Path, registre_bbis: Path, nettoyage: bool, tableaux: dict, etat: dict) -> dict:
    """Plan, point 6 : lectures, nuls, statistiques, pôles, comparaisons, calibration, déclencheurs et audits ; tout est écrit
    dans des fichiers fermés ; puis nettoyage (point 10). Refusé avant `VERDICT-BBIS`."""
    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, ctx.registre_propre)
    en.exiger_scores_et_verdict(registre_bbis)
    if not (ctx.travail / MARQUE).is_file():
        raise Arret("dossier de travail monté absent : rien ne part")
    rapport_montage = ctx.sortie / "diag" / ctx.run / "montage-lentilles-bbis.json"
    if not rapport_montage.is_file():
        raise Arret("rapport du montage absent du dossier de sortie : le manifeste ne pourrait le citer ; rien ne part")
    etat["parti"] = True
    horloge = Horloge(ctx.travail, maintenant=ctx.maintenant)
    horloge.controler("départ du calcul")

    def controle_disque() -> None:
        exiger_disque(ctx.travail, r.disque_calcul, "pendant le calcul", ctx.mesure_disque)
    controle_disque()
    for chemin in (ctx.sortie / "diag" / ctx.run / "tables-lentilles-bbis.json", ctx.sortie / "runs" / ctx.run / "manifeste.json",
                   ctx.sortie / "diag" / ctx.run / "entrees-lentilles-bbis.json"):
        if chemin.exists():
            raise Arret(f"{chemin} existe déjà (R12)")
    charge = charger_montage(ctx)
    entrees = en.ouvrir_entrees(racine_entrees, registre_bbis, ctx.registre_propre, r.largeur)
    graines = nu.Graines()
    masques = st.masques_familles(charge.chaines)
    tableaux["ids_gardes"] = charge.ids_gardes
    sondes_table, par_couche, non_calculables = [], {}, []
    for s in entrees.sondes:
        sondes_table.append({"cle": s.cle, "cellule": s.cellule, "pli": s.pli, "role": s.role, "lue": s.lue,
                             "motif": None if s.lue else f"non lue : {s.motif}", "famille": s.famille, "couche": s.couche,
                             "agregation": s.agregation, "empreinte": s.empreinte, "nom_en_clair": ph.nom_sonde(s.cellule, s.pli, s.role, "w")})
        for nom_v, v in s.vecteurs().items():
            motif = st.vecteur_calculable(v)
            if motif:
                non_calculables.append({"sonde": s.cle, "cellule": s.cellule, "pli": s.pli, "role": s.role, "vecteur": nom_v,
                                        "couche": s.couche, "non_calculable": motif})
            else:
                par_couche.setdefault(s.couche, []).append((s, nom_v, v))
    couches, directions = {}, []
    for couche in sorted(par_couche):
        calcul = _Couche(couche, par_couche[couche], charge, graines, r, masques, tableaux, horloge, controle_disque)
        couches[str(couche)], d = calcul.calculer()
        for ligne in d:
            for nom, m in ligne["poles"]["_maxima"].items():
                tableaux[f"poles__{ligne['_ident']}__maxima__{nom}"] = _np(m)
        directions += d
        horloge.controler(f"couche {couche}")
    lignes = _etiqueter(directions, couches, charge.chaines, charge.ids_gardes)
    comparaisons = _comparaisons(directions)
    declencheurs = au.declencheurs(lignes, [c for c in comparaisons if c.get("cosinus") is not None])
    audit = _audit(entrees, directions, couches, charge, graines, charge.etat) if declencheurs["audit_a_jouer"] else None
    non_tenues = [(int(c), l) for c, info in couches.items() for l, v in info["lentilles"].items()
                  if info["repli_nuls_par_direction"] and v["independance_tenue"] is False]
    morceaux = ecrire_morceaux(tableaux, ctx.sortie / "donnees" / ctx.run / "lectures-lentilles-bbis")
    tables = {
        "run": ctx.run, "texte": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE}, "addendum": dict(ADDENDUM),
        "entrees": {"course": entrees.course.run, "e1_sha256": entrees.sha256_e1, "e2_sha256": entrees.sha256_e2,
                    "empreinte_de_l_extrait_de_la_liste_blanche": entrees.empreinte_extrait, "extrait": entrees.extrait,
                    "entrees_decodees": list(entrees.entrees_decodees), "entrees_jamais_decodees": list(entrees.entrees_non_decodees)},
        "sondes": sondes_table, "couches": couches, "directions": _retirer_prives(directions) + non_calculables,
        "comparaisons": comparaisons, "comptes_de_libelles": _comptes(directions),
        "egalites_au_vingtieme_rang": _egalites(couches),
        "independance_a_la_norme_non_tenue": [{"couche": c, "lentille": l} for c, l in sorted(non_tenues)],
        "declencheurs_d_audit": declencheurs, "audit": audit,
        "lecture_cote_entree": f"non lue : {ph.MOTIF_SANS_LENTILLE_ENTREE}",
        "fichiers_des_lectures": morceaux, "duree_cumulee_s": horloge.ecoule(),
        "conventions": {"ecart_type": "population (diviseur M)", "quantile": "0,99, interpolation linéaire",
                        "rang_empirique": "1 + nombre de scores nuls du même jeton strictement plus grands",
                        "p": "(1 + #{j : statistique(u_j) ≥ statistique(v)}) / (M + 1)", "m": r.m,
                        "statistique_des_directions_nulles": STATISTIQUE_NULLE,
                        "comparaison_des_concentrations": COMPARAISON_CONCENTRATIONS,
                        "garde_d_egalite_au_vingtieme_rang": GARDE_EGALITE, "loi_des_bornes_de_calibration": LOI_CALIBRATION}}
    sha_tables = _ecrire_ferme(ctx.sortie / "diag" / ctx.run / "tables-lentilles-bbis.json", tables)
    chemins = en.chemins_permis(entrees.course.run)
    sha_entrees = _ecrire_ferme(ctx.sortie / "diag" / ctx.run / "entrees-lentilles-bbis.json", {
        "run": ctx.run, "course": entrees.course.run, "e1": {"chemin": chemins["e1"], "sha256": entrees.sha256_e1},
        "e2": {"chemin": chemins["e2"], "sha256": entrees.sha256_e2},
        "empreinte_de_l_extrait_de_la_liste_blanche": entrees.empreinte_extrait})
    montage = {"chemin": f"diag/{ctx.run}/montage-lentilles-bbis.json", "sha256": verifier(rapport_montage)}
    config = {"texte": K.EMPREINTE_TEXTE, "addendum": en.EMPREINTE_ADDENDUM, "m": r.m, "n_temoins_isotrope": r.n_temoins_isotrope,
              "n_temoins_par_vecteur": r.n_temoins_par_vecteur, "couches": list(r.couches), "largeur": r.largeur,
              "epsilon": K.EPSILON, "course_bbis": entrees.course.run, "statistique_des_directions_nulles": STATISTIQUE_NULLE}
    manifeste = {"run_id": ctx.run, "cree_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "commit": _commit(ctx.racine_depot), "code": empreintes_du_code(), "fiche_code": fiche_code, "config": config,
                 "rapport_du_montage": montage, "entrees_sha256": sha_entrees,
                 "config_sha256": hashlib.sha256(mf.config_canonique(config)).hexdigest(), "versions": _versions(),
                 "graines": {cle: {"entropie": str(graines.entropie), "spawn_key": [str(e)]} for cle, e in sorted(graines.derivees.items())},
                 "preenregistrement": {"chemin": K.TEXTE, "sha256": K.EMPREINTE_TEXTE}, "addendum": dict(ADDENDUM),
                 "tables_sha256": sha_tables}
    sha_manifeste = _ecrire_ferme(ctx.sortie / "runs" / ctx.run / "manifeste.json", manifeste)
    cle = (ctx.env if ctx.env is not None else os.environ).get(K.NOM_CLE)
    if cle and str(cle).strip():
        mo.aucune_occurrence([ctx.sortie, ctx.travail], mo.Cle(str(cle).strip()))
    horloge.consigner()
    versement = nettoyer(ctx.travail, ctx.sortie, ctx.run) if nettoyage else None
    return {"versement_du_travail": versement, "tables": {"chemin": f"diag/{ctx.run}/tables-lentilles-bbis.json", "sha256": sha_tables},
            "manifeste": {"chemin": f"runs/{ctx.run}/manifeste.json", "sha256": sha_manifeste}, "morceaux": morceaux,
            "lignes_proposees": [
                ligne_registre("ENTREES-LENTILLES-BBIS", f"diag/{ctx.run}/entrees-lentilles-bbis.json", sha_entrees),
                ligne_registre("TABLES-LENTILLES-BBIS", f"diag/{ctx.run}/tables-lentilles-bbis.json", sha_tables)],
            "empreinte_extrait": entrees.empreinte_extrait, "e1_sha256": entrees.sha256_e1}


STATISTIQUE_NULLE = ("concentration et part de chaque direction nulle calculées sans elle-même (moyenne, écart type et quantile 0,99 des "
                     "M − 1 autres) ; moyenne, écart type et quantile des M directions pour la direction lue et les témoins ; "
                     "familles inchangées (addendum de concentration scellé, EC-1 et EC-2)")
COMPARAISON_CONCENTRATIONS = ("C(u_j) calculé en double précision, rendu en simple précision comme C(v) ; comparaison C(u_j) ≥ C(v) "
                              "en simple précision ; une égalité compte contre v (addendum, EC-1)")
GARDE_EGALITE = ("égalité au vingtième rang : vingtième et vingt-et-unième valeurs égales, par égalité exacte, en simple précision ; "
                 "direction lue : arrêt nommé ; direction nulle : marquée, p_bas et p_haut, la valeur p écrite est p_haut, attendu "
                 "d'une famille sur les seules directions non marquées, arrêt nommé si le libellé diffère entre les deux bornes ; "
                 "témoin : compté (addendum, EC-6, option 3)")
LOI_CALIBRATION = ("loi de référence du compte : bêta-binomiale (n ; 100 ; M − 99) par jeu, somme de lois indépendantes pour des "
                   "jeux mis en commun ; approchée, non exacte (addendum, EC-3 et § 7) ; bornes de valeurs inchangées")


def _egalites(couches: dict) -> dict:
    """Garde d'égalité au vingtième rang, comptes d'ensemble : directions nulles marquées et témoins à égalité, par (couche,
    lentille, nul) dans `couches`, et leurs totaux ; aucune égalité d'une direction lue n'a été rencontrée (sinon arrêt)."""
    marquees = sum(e["directions_nulles_marquees"] for info in couches.values() for l in info["lentilles"].values()
                   for e in l["egalites_au_vingtieme_rang"].values())
    temoins = sum(e["temoins_a_egalite_au_vingtieme_rang"] for info in couches.values() for l in info["lentilles"].values()
                  for e in l["egalites_au_vingtieme_rang"].values())
    sans_objet = any(e["garde_sans_objet"] for info in couches.values() for l in info["lentilles"].values()
                     for e in l["egalites_au_vingtieme_rang"].values())
    return {"directions_lues_a_egalite": 0, "directions_nulles_marquees": marquees, "temoins_a_egalite": temoins,
            "garde_sans_objet": sans_objet, "note": st.SANS_OBJET if sans_objet else None,
            "detail": "couches/<couche>/lentilles/<lentille>/egalites_au_vingtieme_rang"}
NOTE_POLES_INTERMEDIAIRES = "pôles intermédiaires : aucune phrase gelée ; valeurs en table"


# --- phrases (étape du lecteur) ----------------------------------------------------------------------------------------------------------
def rendre_phrases(tables: dict) -> dict:
    """Phrases gelées rendues mécaniquement à partir des tables fermées."""
    non_tenues = [(x["couche"], x["lentille"]) for x in tables["independance_a_la_norme_non_tenue"]]
    sortie = {"tete": ph.phrase_de_tete(non_tenues), "directions": [], "comparaisons": [], "non_lues": [],
              "lecture_cote_entree": ph.phrase_non_lue(ph.MOTIF_SANS_LENTILLE_ENTREE)}
    for s in tables["sondes"]:
        if not s["lue"]:
            sortie["non_lues"].append({"sonde": s["cle"], "phrase": ph.phrase_non_lue(s["motif"].removeprefix("non lue : "))})
    for d in tables["directions"]:
        nom = ph.nom_sonde(d["cellule"], d["pli"], d["role"], d["vecteur"])
        if d.get("non_calculable"):
            sortie["non_lues"].append({"sonde": f"{d['sonde']}/{d['vecteur']}", "phrase": ph.phrase_non_lue(d["non_calculable"])})
            continue
        for lentille, lecture in d["lectures"].items():
            for signe, t in lecture["signes"].items():
                ligne = {"sonde": d["sonde"], "vecteur": d["vecteur"], "lentille": lentille, "signe": signe, "phrases": []}
                if t["libelle"] is None:
                    ligne["phrases"].append(ph.phrase_non_lue(t["non_calculable"]))
                else:
                    i, s = t["nuls"][t["nul_isotrope_en_vigueur"]], t["nuls"][K.NUL_SIGNES]
                    ligne["phrases"].append(ph.phrase_direction(lentille, nom, d["couche"], signe, t["libelle"], i["concentration"],
                                                                i["p_concentration"], s["p_concentration"],
                                                                t["premiers_par_score"]["chaines_echappees"]))
                    for famille, f in t["familles"].items():
                        ligne["phrases"].append(ph.phrase_famille(famille, f["n"], i["familles"][famille]["attendu"],
                                                                  i["familles"][famille]["p"], s["familles"][famille]["p"],
                                                                  f["sur_representee"]))
                sortie["directions"].append(ligne)
        p = d["poles"]
        poles = p["poles"]
        phrase = ph.phrase_poles(p["libelle"], poles, p["p"][p["nul_isotrope_en_vigueur"]], p["p"][K.NUL_SIGNES],
                                 [x["lecture_publique"]["chaines_echappees"] for x in poles])
        ligne = {"sonde": d["sonde"], "vecteur": d["vecteur"], "poles": True, "libelle": p["libelle"],
                 "phrases": [phrase] if phrase else []}
        if phrase is None:
            ligne["note"] = NOTE_POLES_INTERMEDIAIRES
        sortie["directions"].append(ligne)
    for c in tables["comparaisons"]:
        a, b = c["a"].split("/"), c["b"].split("/")
        communs = None if c["cosinus"] is None else c["jetons_communs"][K.LENTILLE_PUBLIQUE]["+"]
        sortie["comparaisons"].append({"type": c["type"], "a": c["a"], "b": c["b"],
                                       "phrase": ph.phrase_comparaison(ph.nom_sonde(*a), ph.nom_sonde(*b), c["cosinus"], communs)})
    return sortie


# --- ligne de commande -------------------------------------------------------------------------------------------------------------------
def principal(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Lecture des sondes de l'étape B bis par la lentille publique (texte scellé v1 et "
                                            "son addendum de concentration scellé)")
    sp = p.add_subparsers(dest="commande", required=True)
    for nom in ("montage", "calcul"):
        s = sp.add_parser(nom)
        s.add_argument("--travail", required=True, type=Path)
        s.add_argument("--sortie", required=True, type=Path)
        s.add_argument("--run", required=True)
        s.add_argument("--depot", type=Path, default=Path("."))
        s.add_argument("--registre-propre", required=True, type=Path)
        if nom == "calcul":
            s.add_argument("--entrees", required=True, type=Path)
            s.add_argument("--registre-bbis", required=True, type=Path)
    s = sp.add_parser("recuperer")
    s.add_argument("--url", required=True)
    s.add_argument("--entrees", required=True, type=Path)
    s.add_argument("--registre-bbis", required=True, type=Path)
    s.add_argument("--registre-propre", required=True, type=Path)
    s.add_argument("--depot", type=Path, default=Path("."))
    s = sp.add_parser("phrases")
    s.add_argument("--tables", required=True, type=Path)
    s.add_argument("--sortie", required=True, type=Path)
    a = p.parse_args(argv)
    arret = None
    try:
        if a.commande == "recuperer":
            exiger_fiche_code(a.depot, a.registre_propre)       # code cité et clé de l'addendum, avant toute requête
            en.recuperer_entrees(a.url, a.entrees, a.registre_bbis, a.registre_propre)
            rendu = {"entrees": str(a.entrees)}
        elif a.commande == "phrases":
            verifier(a.tables)
            rendu = {"sha256": _ecrire_ferme(a.sortie, rendre_phrases(json.loads(a.tables.read_text(encoding="utf-8"))))}
        else:
            ctx = Contexte(a.travail, a.sortie, a.run, a.depot, a.registre_propre)
            rendu = monter(ctx) if a.commande == "montage" else calculer(ctx, a.entrees, a.registre_bbis)
            if a.commande == "calcul":   # cloisonnement : l'opérateur ne voit que fichiers et empreintes, jamais les noms des tableaux
                rendu["morceaux"] = [{"fichier": m["fichier"], "sha256": m["sha256"]} for m in rendu["morceaux"]]
    except Arret as e:
        arret = e                           # version 6 : rien d'autre dans ce bloc ; hors de lui, aucun arrêt n'est « en cours »
    if arret is not None:
        print(f"ARRÊT : {arret}" if nom_d_arret_cloisonne(arret) is None else ligne_d_arret_cloisonne(arret), file=sys.stderr)
        return 3
    print(json.dumps(rendu, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
