"""Adaptateur de MC de l'étape B bis vers le **code scellé de la pièce « mots et coût »** (`prereg/T0.7-etape-B-bis-v1.md`,
« Métrique », MC : « apprises et notées par le code de la pièce « mots et coût » cité par la ligne `CODE-MOTS-ET-COUT-T06`, sans
changement »), v1 — module neuf (R12). Lien attendu par `adversaires_texte_v1.charger_adaptateur` :
`controle_ia.t07bbis.lien_mots_et_cout_v1:AdaptateurPieceMC`.

**Au chargement** (`AdaptateurPieceMC(racine)`), avant tout import du code de la pièce, et sans aucun repli :
1. la ligne `CODE-MOTS-ET-COUT-T06` de `registres/scellements-v1.md` est présente **une fois**, de forme exacte ; absente,
   en double ou mal formée → arrêt ;
2. le fichier qu'elle cite (`registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`) a l'empreinte de la ligne et son
   compagnon `.sha256` égal (`t07.registre_v1.sceau_conforme`) ; sinon arrêt ;
3. ce fichier porte `commit` (40 caractères hexadécimaux) et `fichiers` ; l'empreinte attendue du module est
   `fichiers["scripts/mots_et_cout_t06_v3.py"]` ;
4. le module lu sur le disque (`racine/scripts/mots_et_cout_t06_v3.py`) a **cette** empreinte, et le module au commit cité
   (`git show <commit>:scripts/mots_et_cout_t06_v3.py`) aussi ; sinon arrêt ;
5. le module est exécuté **depuis les octets dont l'empreinte vient d'être vérifiée** (aucune seconde lecture du disque), sous
   un nom propre ; sa version (`VERSION = 3`) et son contrat (`centres`, `apprendre_a`, `noter_a`, `apprendre_b`, `noter_b`)
   sont exigés ; ses modules gelés sont vérifiés par sa propre fonction (`verifier_modules_geles`, table de la pièce) ;
6. les fils de calcul de l'algèbre linéaire (`OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`) valent « 1 »,
   comme la pièce l'exige en mode réel (l'ordre des sommes change les coefficients au-delà de 10⁻¹², ce qui ferait refuser le
   contrôle d'égalité) ; sinon arrêt (`exiger_fils=False` pour les seuls essais).

**Interface `InterfaceMC`** (`adversaires_texte_v1`) : `centres` → `centres` de la pièce ; `apprendre(base, …)` →
`apprendre_a` (base (A), « N-029 ») ou `apprendre_b` (base (B), « mots_et_cout ») de la pièce, sans changement ; un modèle
non calculable de la pièce (classe absente, tous les traits retirés, non convergé, vocabulaire vide) lève `NonCalculable`
(motif de la pièce recopié), jamais un score ; `noter` → `noter_a` ou `noter_b`. Le modèle rendu porte `jeu` (lecture de
transfert : `noter_transfert` refuse un modèle appris sur le jeu lu). Les lignes passées sont celles de la lecture : une par
action, champs de `mesures-t06.npz` et `texte` ; la pièce n'en lit que `tache`, `cout`, `jetons`, `valide`, les six formes du
champ du coût et `texte` (contrat de T0.8, « mêmes fonctions que la pièce, mêmes réglages »).

Écarts déclarés avec l'implémentation de repli de B bis (`RepliMC`, plan, point 8 bis), qui ne sert plus quand la ligne est
inscrite avant l'échéance : base (A) identique par construction (mêmes traits, mêmes réglages ; égalité éprouvée) ; base (B)
différente en trois points (note `rapport-developpeur-adaptateur-mc-v1.md`, § 4) : mots (`[^\\W\\d_]+` contre `\\w+` avec une
lettre), échelle (aucun centrage ni réduction contre traits réduits), point (c) (« coût présent » lu sur le texte par
`lire_action` contre les six formes du champ du coût des mesures).
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import types
from pathlib import Path

from ..gardes import GardeArret
from .adversaires_texte_v1 import BASE_A, BASE_B
from .plis_v1 import NonCalculable

CLE_LIGNE = "CODE-MOTS-ET-COUT-T06"
REGISTRE = "registres/scellements-v1.md"
CHEMIN_FICHIER_LIGNE = "registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json"
MODULE_PIECE = "scripts/mots_et_cout_t06_v3.py"
VERSION_PIECE = 3
CONTRAT = ("centres", "apprendre_a", "noter_a", "apprendre_b", "noter_b", "verifier_modules_geles")
FILS_BLAS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")
NOM_MODULE = "controle_ia_t07bbis_piece_mots_et_cout_v3"


class ModeleMC:
    """Modèle d'une base rendu par la pièce, avec le jeu d'apprentissage (garde de la lecture de transfert)."""

    def __init__(self, base: str, jeu: str, interne: dict):
        self.base, self.jeu, self.interne = base, jeu, interne

    @property
    def traits_retires(self) -> list:
        return list(self.interne.get("traits_retires") or [])

    @property
    def gradient_max(self):
        return (self.interne.get("convergence") or {}).get("gradient_max")


def lire_ligne(racine: Path) -> dict:
    """La ligne `CODE-MOTS-ET-COUT-T06` du registre partagé, une fois exactement, de forme exacte ; sinon arrêt."""
    from ..t07 import registre_v1 as rg
    reg = Path(racine) / REGISTRE
    if not reg.is_file():
        raise GardeArret(f"{REGISTRE} absent : ligne {CLE_LIGNE} illisible : arrêt (aucun repli)")
    lignes = []
    for l in reg.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if c and c[0] == CLE_LIGNE:
            lignes.append(c)
    if not lignes:
        raise GardeArret(f"ligne {CLE_LIGNE} absente de {REGISTRE} : adaptateur de la pièce refusé : arrêt (aucun repli)")
    if len(lignes) != 1:
        raise GardeArret(f"{len(lignes)} lignes {CLE_LIGNE} dans {REGISTRE} : une exactement attendue : arrêt")
    c = lignes[0]
    if len(c) != 4 or not rg.DATE.fullmatch(c[1]) or not rg.SHA.fullmatch(c[3]) or c[2].startswith("/") or ".." in Path(c[2]).parts:
        raise GardeArret(f"ligne {CLE_LIGNE} mal formée : arrêt")
    return {"date": c[1], "instant": rg.instant_utc(c[1]), "chemin": c[2], "sha256": c[3]}


def lire_fichier_ligne(racine: Path, ligne: dict) -> dict:
    """Fichier cité par la ligne : empreinte de la ligne, compagnon égal ; `commit` et `fichiers` lisibles ; sinon arrêt."""
    from ..t07 import registre_v1 as rg
    if ligne["chemin"] != CHEMIN_FICHIER_LIGNE:
        raise GardeArret(f"ligne {CLE_LIGNE} : chemin {ligne['chemin']!r} ≠ {CHEMIN_FICHIER_LIGNE!r} : arrêt")
    try:
        sha = rg.sceau_conforme(Path(racine) / ligne["chemin"], ligne["sha256"])
    except GardeArret as e:
        raise GardeArret(f"fichier de la ligne {CLE_LIGNE} différent de la ligne ou de son compagnon ({e}) : arrêt") from None
    try:
        doc = json.loads((Path(racine) / ligne["chemin"]).read_text(encoding="utf-8"))
        commit, fichiers = str(doc["commit"]), dict(doc["fichiers"])
        attendu = str(fichiers[MODULE_PIECE])
    except (OSError, ValueError, KeyError, TypeError) as e:
        raise GardeArret(f"fichier de la ligne {CLE_LIGNE} illisible ({type(e).__name__}) : arrêt") from None
    if len(commit) != 40 or any(ch not in "0123456789abcdef" for ch in commit) or not rg.SHA.fullmatch(attendu):
        raise GardeArret(f"fichier de la ligne {CLE_LIGNE} : commit ou empreinte du module hors format : arrêt")
    return {"sha256": sha, "commit": commit, "module_sha256": attendu, "fichiers": fichiers}


def octets_au_commit(racine: Path, commit: str, chemin: str) -> bytes:
    r = subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        raise GardeArret(f"commit cité {commit[:12]} introuvable ou sans {chemin} dans le dépôt : arrêt")
    return r.stdout


def exiger_fils_un() -> dict:
    fils = {k: os.environ.get(k) for k in FILS_BLAS}
    if any(v != "1" for v in fils.values()):
        raise GardeArret(f"fils de calcul de l'algèbre linéaire non fixés à 1 ({fils}) : MC par la pièce refusé (sommes non "
                         "reproductibles ; poser OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1 avant l'import de "
                         "numpy)")
    return fils


def charger_piece(racine: Path, exiger_fils: bool = True) -> tuple[types.ModuleType, dict]:
    """Vérifications 1 à 6 du docstring, puis le module de la pièce exécuté depuis les octets vérifiés."""
    racine = Path(racine)
    fils = exiger_fils_un() if exiger_fils else {k: os.environ.get(k) for k in FILS_BLAS}
    ligne = lire_ligne(racine)
    fichier = lire_fichier_ligne(racine, ligne)
    chemin = racine / MODULE_PIECE
    if not chemin.is_file():
        raise GardeArret(f"{MODULE_PIECE} absent : arrêt")
    octets = chemin.read_bytes()
    sha = hashlib.sha256(octets).hexdigest()
    if sha != fichier["module_sha256"]:
        raise GardeArret(f"{MODULE_PIECE} : empreinte {sha[:12]}… ≠ fichier de la ligne {CLE_LIGNE} "
                         f"({fichier['module_sha256'][:12]}…) : arrêt (aucun repli)")
    if hashlib.sha256(octets_au_commit(racine, fichier["commit"], MODULE_PIECE)).hexdigest() != sha:
        raise GardeArret(f"{MODULE_PIECE} au commit cité {fichier['commit'][:12]} ≠ fichier de la ligne : arrêt")
    mod = types.ModuleType(NOM_MODULE)
    mod.__file__ = str(chemin)
    sys.modules[NOM_MODULE] = mod
    try:
        exec(compile(octets, str(chemin), "exec"), mod.__dict__)
    except Exception:
        sys.modules.pop(NOM_MODULE, None)
        raise
    if getattr(mod, "VERSION", None) != VERSION_PIECE or any(not callable(getattr(mod, f, None)) for f in CONTRAT):
        raise GardeArret(f"module de la pièce : version {getattr(mod, 'VERSION', None)!r} ou contrat {CONTRAT} incomplet : arrêt")
    geles = mod.verifier_modules_geles()
    return mod, {"ligne": ligne, "fichier": {k: fichier[k] for k in ("sha256", "commit", "module_sha256")},
                 "module": {"chemin": MODULE_PIECE, "sha256": sha}, "modules_geles": geles, "fils_blas": fils}


class AdaptateurPieceMC:
    """Interface `InterfaceMC` liée au code scellé de la pièce (docstring du module)."""
    nom = "piece-mots-et-cout-t06-v3"

    def __init__(self, racine: Path | None = None, exiger_fils: bool = True):
        racine = Path(racine) if racine is not None else Path(__file__).resolve().parents[3]
        self.racine = racine
        self.piece, self.provenance = charger_piece(racine, exiger_fils)

    def centres(self, lignes: list[dict]) -> dict:
        return self.piece.centres(list(lignes))

    def apprendre(self, base: str, lignes: list[dict], y, centres: dict, jeu: str) -> ModeleMC:
        if base == BASE_A:
            m = self.piece.apprendre_a(list(lignes), y, centres)
        elif base == BASE_B:
            m = self.piece.apprendre_b(list(lignes), y, centres)
        else:
            raise GardeArret(f"base {base!r} inconnue")
        if not m.get("calculable"):
            raise NonCalculable(f"base {base} ({jeu}) : {m.get('motif')} (code de la pièce)")
        return ModeleMC(base, jeu, m)

    def noter(self, modele: ModeleMC, lignes: list[dict], centres: dict, jeu_lu: str):
        if not isinstance(modele, ModeleMC):
            raise GardeArret("adaptateur de la pièce : modèle d'une autre interface : refus")
        if modele.base == BASE_A:
            return self.piece.noter_a(modele.interne, list(lignes), centres)
        return self.piece.noter_b(modele.interne, list(lignes), centres)


__all__ = ["AdaptateurPieceMC", "ModeleMC", "charger_piece", "lire_ligne", "lire_fichier_ligne", "octets_au_commit",
           "exiger_fils_un", "CLE_LIGNE", "MODULE_PIECE", "CHEMIN_FICHIER_LIGNE"]
