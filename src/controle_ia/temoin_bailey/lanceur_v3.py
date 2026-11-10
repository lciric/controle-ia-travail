"""Lanceur local (orchestration de l'instance louée) — témoin « attaque publiée reproduite » (Bailey et collègues), v3.

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : règle du nombre de tours (B, R,
D, c), liste d'arrêt, pilote et reprise, relance, transfert et comparaison des empreintes avant destruction, conditions
de lancement 2 et 8. La v3 applique la relecture en différentiel du code v2
(`relecture-differentiel-code-condition6-v2-bailey-v1.md`, `4f079ece…`) et trois corrections de la session :
- correction 1 (N-1, N-2) : la conduite décide sur l'état de l'exécution (`code_retour` de l'enfant, cause d'arrêt,
  gardes tombées, tours complets), par `lecture_v3.issue_pilote` et `lecture_v3.relance_permise`, jamais sur le code
  de `ssh` : « sonde orientée » au pilote → arrêt sans reprise ; dépense ou échéance → arrêt sans reprise ; relance du
  run principal sur erreur ou garde de démarrage avant 20 tours complets, jamais après « sonde orientée » ;
- correction 2 (N-3) : champ obligatoire `instances_anterieures` (lues dans `registres/depenses.md`), versées au
  `Poste` avant la création ; leur B doit égaler celui du manifeste ;
- correction 3 (N-4) : rapatriement dans son propre `try`, puis destruction dans tous les cas ; un `scp` en échec est
  un écart de transfert, jamais une exception qui sort ; le veilleur de secours est un **processus séparé**
  (`python -m controle_ia.temoin_bailey.lanceur_v3 veilleur …`, nouvelle session), qui survit à la conduite et lit
  l'état du poste dans `poste-v3.json` ;
- correction 5 (N-5) : arrêt nominal à `échéance − marge_transfert_s` sur l'instance ; secours au plus tard à
  l'échéance (`delai_secours_s ≤ 0`) ; `verifier_echeance` exige `échéance ≥ création + (B − marge_secours)/c h +
  marge_transfert` ;
- correction 7 (N-8) : après une comparaison d'empreintes égale, chaque fichier transféré est scellé
  (`controle_ia.scellement.sceller`, compagnon `.sha256`) ;
- correction 10 (N-11, A-7) : chaque ajout au manifeste produit un manifeste local versionné, sans écrasement
  (`manifeste-v3-mise-en-place.json`, `…-regle.json`, `…-relance.json`), envoyé sur l'instance et scellé ;
- correction 11 (N-12) : les fichiers d'état passent par `transferer` ; le bilan garde les dictionnaires d'empreintes ;
- corrections 12 et S-3 (N-13, P-9) : ni `git clone` du dépôt privé, ni jeton sur une ligne de commande : une archive
  `git archive <commit>`, empreintée, est envoyée par `scp` et vérifiée sur l'instance ; le jeton des modèles à accès
  contrôlé (variable `HF_TOKEN` du poste local, jamais imprimée) est écrit dans un fichier temporaire local (droits
  600), envoyé par `scp`, puis effacé localement ; l'amorce l'efface de l'instance à sa sortie ;
- correction 13 (N-14) : dépense et échéance vérifiées avant chaque commande, et bornes de sondage ;
- P-f : les commandes longues tournent détachées sur l'instance (`setsid nohup`), sondées par de courtes sessions
  `ssh` : une coupure du poste local ne tue pas l'exécution ; arrêt d'une commande par son PID (R10) ;
- P-3 : refus d'un GO visé par une ligne de révocation ;
- S-1 : `verifier_go` lit B dans la cellule d'objet (« B = 75 » de GO-2026-11-10-10, enveloppe de 120 USD), exige
  qu'il égale le B du manifeste et que l'objet cite `fb6c2f34` et `f9c8c66e` ; le plafond de la ligne doit couvrir B ;
- S-2 : `lire_versions_figees` lit `versions-figees-temoin-bailey-v1.json` (`e21bccf6…`, Python 3.11).
Ce module ne lit aucune note. Lectures de lignes scellées faites ici (liste :
`docs/notes/reproduction-attaque-publiee-v1/lectures-a-acter-addendum-condition6-v1.md`) : « B − 2 » lu comme arrêt
du run sur l'instance, transfert, puis destruction, seuil de secours B − 0,5 USD, secours au plus tard à l'échéance
(actés par Lazar, `registres/passations/2026-11-10-1240-decision-lazar-noeud5-lecture-b2.md`, `2f3e8e3a…`) ; valeur
de la marge de transfert (3 600 s) et lecture de B dans la ligne de GO : à acter.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import signal
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

from .. import scellement
from ..gardes import GardeArret
from . import analyse_v3 as an
from . import conventions_v3 as cv
from .lecture_v3 import ETAPES, MANIFESTES, issue_pilote, relance_permise

DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"  # cité dans l'ordre de lancement (condition 8)
CACHE_HF = "/root/hf"
JETON_DISTANT = "/root/.cache/huggingface/token"
ARCHIVE_DISTANTE = "/root/travail.tar.gz"
ETATS_DISTANTS = "/root/etats"
EMPREINTE_PREREG = "fb6c2f34"
EMPREINTE_DEVIS = "f9c8c66e"
MARGE_SECOURS_USD = 0.5
MARGE_TRANSFERT_S = 3600.0


class Fournisseur:
    def creer(self, offre: str, image: str, disque_go: int) -> str: ...
    def taux_horaire(self, ident: str) -> float: ...
    def detruire(self, ident: str) -> None: ...
    def executer(self, ident: str, commande: str, delai_s: float | None = None) -> tuple[int, str]: ...
    def rapatrier_fichier(self, ident: str, distant: str, local: Path) -> None: ...
    def envoyer_fichier(self, ident: str, local: Path, distant: str) -> None: ...


class FournisseurVast(Fournisseur):
    """Commande `vastai` (la clé est lue par la commande ; ce module ne la lit ni ne l'imprime). Aucune variable
    d'environnement n'est passée à la création (le jeton passe par un fichier, S-3)."""

    def _vast(self, *args: str) -> str:
        return subprocess.run(["vastai", *args], check=True, capture_output=True, text=True).stdout

    def creer(self, offre, image, disque_go):
        args = ["create", "instance", offre, "--image", image, "--disk", str(disque_go), "--ssh", "--direct", "--raw"]
        return str(json.loads(self._vast(*args))["new_contract"])

    def taux_horaire(self, ident):
        return float(json.loads(self._vast("show", "instance", ident, "--raw"))["dph_total"])

    def detruire(self, ident):
        self._vast("destroy", "instance", ident)

    def _ssh(self, ident) -> tuple[str, str]:
        m = re.match(r"ssh://([^@]+)@([^:]+):(\d+)", self._vast("ssh-url", ident).strip())
        if not m:
            raise GardeArret("adresse de l'instance illisible")
        return f"{m.group(1)}@{m.group(2)}", m.group(3)

    def executer(self, ident, commande, delai_s=None):
        hote, port = self._ssh(ident)
        p = subprocess.run(["ssh", "-o", "StrictHostKeyChecking=accept-new", "-p", port, hote, commande],
                           capture_output=True, text=True, timeout=delai_s)
        return p.returncode, p.stdout

    def rapatrier_fichier(self, ident, distant, local):
        hote, port = self._ssh(ident)
        local.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["scp", "-P", port, f"{hote}:{distant}", str(local)], check=True, capture_output=True)

    def envoyer_fichier(self, ident, local, distant):
        hote, port = self._ssh(ident)
        subprocess.run(["scp", "-P", port, str(local), f"{hote}:{distant}"], check=True, capture_output=True)


class FournisseurFichier(Fournisseur):
    """Pour l'épreuve du veilleur sur processeur : une destruction est une ligne écrite dans un fichier."""

    def __init__(self, chemin: str):
        self.chemin = Path(chemin)

    def detruire(self, ident):
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(f"{ident}\n")


def fournisseur_depuis(spec: str) -> Fournisseur:
    if spec == "vast":
        return FournisseurVast()
    if spec.startswith("fichier:"):
        return FournisseurFichier(spec[len("fichier:"):])
    raise GardeArret("fournisseur inconnu")


# --- conditions de lancement ------------------------------------------------------------------------------------------

def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def ligne_go(texte_go: str, go_id: str) -> dict:
    """Colonnes de `registres/go.md` : id, accordé le, type, périmètre (objet), plafond, échéance, accordé par,
    référence."""
    for ligne in texte_go.splitlines():
        cellules = _cellules(ligne)
        if cellules and cellules[0] == go_id:
            if len(cellules) < 6:
                raise GardeArret("condition 2 : ligne de GO incomplète")
            return {"id": go_id, "type": cellules[2], "objet": cellules[3], "plafond": cellules[4],
                    "echeance": cellules[5]}
    raise GardeArret("condition 2 : ligne de GO absente de registres/go.md")


def _nombre(texte: str) -> float:
    return float(texte.replace(",", "."))


def b_de_l_objet(objet: str) -> float:
    """S-1 : B lu dans la cellule d'objet, sous la forme qui le fixe, entre parenthèses : « (B = 75, garde d'horloge à
    B − 2) » dans GO-2026-11-10-10. La même cellule cite aussi « le passage de Bailey à B = 120 » comme **hors
    enveloppe, retour à Lazar** : cette mention, hors parenthèse, ne fixe pas B (lecture à acter). Une seule valeur
    entre parenthèses admise."""
    valeurs = {_nombre(x) for x in re.findall(r"\(\s*B\s*=\s*(\d+(?:[.,]\d+)?)", objet)}
    if len(valeurs) != 1:
        raise GardeArret("condition 2 : la ligne de GO ne fixe pas B (« (B = … ») de façon unique")
    return valeurs.pop()


def verifier_go(go: dict, b: float, empreinte_prereg: str = EMPREINTE_PREREG,
                empreinte_devis: str = EMPREINTE_DEVIS) -> None:
    """Condition 2 : type « calcul » ; l'objet cite le texte scellé et le devis v4, et fixe B (« B = … »), égal au B
    du manifeste ; le plafond de la ligne (premier nombre de sa cellule, en USD) couvre B."""
    if go["type"].lower() != "calcul":
        raise GardeArret("condition 2 : la ligne de GO n'est pas de type « calcul »")
    if empreinte_prereg not in go["objet"]:
        raise GardeArret("condition 2 : la ligne de GO ne cite pas le préenregistrement scellé")
    if empreinte_devis not in go["objet"]:
        raise GardeArret("condition 2 : la ligne de GO ne cite pas le devis v4")
    if b_de_l_objet(go["objet"]) != float(b):
        raise GardeArret("condition 2 : B de la ligne de GO différent du B du manifeste")
    nombres = re.findall(r"\d+(?:[.,]\d+)?", go["plafond"])
    if not nombres or _nombre(nombres[0]) < float(b):
        raise GardeArret("condition 2 : plafond de la ligne de GO inférieur à B")


def verifier_non_revoque(texte_go: str, go_id: str) -> None:
    """P-3 : aucune ligne de type « révocation » ne vise le GO cité."""
    for ligne in texte_go.splitlines():
        c = _cellules(ligne)
        if len(c) >= 4 and c[0] != go_id and c[2].lower() in ("révocation", "revocation") and go_id in ligne:
            raise GardeArret("condition 2 : le GO cité est révoqué")


def echeance_epoch(echeance: str) -> float:
    """« AAAA-MM-JJ » : lue comme la fin de ce jour, 23:59:59 UTC (lecture déclarée, P-3) ; « AAAA-MM-JJTHH:MMZ » :
    l'instant dit."""
    import calendar
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2}))?", echeance)
    if not m:
        raise GardeArret("condition 2 : échéance du GO illisible")
    a, mo, j = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if m.group(4):
        return calendar.timegm((a, mo, j, int(m.group(4)), int(m.group(5)), 0))
    return calendar.timegm((a, mo, j, 23, 59, 59))


def verifier_echeance(echeance: float, creation: float, b: float, c: float,
                      marge_secours: float = MARGE_SECOURS_USD, marge_transfert_s: float = MARGE_TRANSFERT_S) -> None:
    """Correction 5 : le texte exige `échéance ≥ création + (B − 2)/c h` ; la dépense pouvant courir jusqu'au seuil de
    secours, on exige plus : `échéance ≥ création + (B − marge_secours)/c h + marge_transfert`."""
    if echeance < creation + (float(b) - float(marge_secours)) / float(c) * 3600 + float(marge_transfert_s):
        raise GardeArret("condition 2 : échéance du GO antérieure à la création + (B − marge de secours)/c heures "
                         "+ marge de transfert")


# --- manifeste (A-7, S-2) --------------------------------------------------------------------------------------------

def chemin_snapshot(depot: str, revision: str) -> str:
    return f"{CACHE_HF}/models--{depot.replace('/', '--')}/snapshots/{revision}"


def lire_versions_figees(chemin, empreinte: str = cv.VERSIONS_FIGEES_SHA256) -> dict:
    """S-2 : versions figées, vérifiées par leur empreinte ; Python 3.11 ; paquets exigés présents ; strong_reject au
    commit du texte."""
    p = Path(chemin)
    if not p.is_file() or cv.sha_fichier(p) != empreinte:
        raise GardeArret("versions figées : fichier absent ou empreinte différente")
    v = json.loads(p.read_text(encoding="utf-8"))
    if v.get("python") != cv.PYTHON:
        raise GardeArret("versions figées : Python différent de 3.11")
    for paquet in cv.VERSIONS_EXIGEES:
        if paquet not in v.get("versions", {}):
            raise GardeArret(f"versions figées : {paquet} absent")
    if list(v.get("git", {}).get("strong_reject", [None, None]))[1] != cv.JUGE_COMMIT_PAQUET:
        raise GardeArret("versions figées : commit de strong_reject différent du texte")
    return v


def ecrire_manifeste(chemin: Path, *, versions: dict, git: dict, python: str, revision_modele: str,
                     revision_adaptateur: str, revision_base: str, commit_code: str, b: float, go_id: str,
                     versions_figees: dict | None = None) -> dict:
    """Manifeste (R9) fixé avant la création de l'instance. N'écrase jamais un fichier existant (R12)."""
    chemin = Path(chemin)
    if chemin.exists():
        raise GardeArret("manifeste déjà présent : une nouvelle version prend un nouveau nom (R12)")
    g = an.graines()
    m = {"version": 3, "commit_code": commit_code, "commit_public": cv.COMMIT_PUBLIC, "arbre_public": cv.ARBRE_PUBLIC,
         "go_id": go_id, "B": b, "python": python, "versions": versions, "git": git, "cache_hf": CACHE_HF,
         "versions_figees": versions_figees,
         "modele": cv.MODELE, "revision_modele": revision_modele,
         "chemin_modele": chemin_snapshot(cv.MODELE, revision_modele),
         "juge": {"adaptateur": cv.JUGE, "revision_adaptateur": revision_adaptateur, "base": cv.JUGE_BASE,
                  "revision_base": revision_base, "dtype": "torch.bfloat16"},
         "graines": {"racine": an.RACINE_GRAINES, "pilote": g["pilote"], "principal": g["principal"],
                     "cle_reechantillonnage": list(an.CLE_REECHANTILLONNAGE)}}
    an.garde_graines(m["graines"])
    chemin.write_text(json.dumps(m, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return m


def manifeste_depuis_versions_figees(chemin: Path, chemin_versions, *, commit_code: str, b: float,
                                     go_id: str) -> dict:
    """Manifeste écrit depuis les versions figées (S-2) : versions, commits, Python et révisions relevées."""
    v = lire_versions_figees(chemin_versions)
    rev = v["revisions_hugging_face_relevees_le_2026-11-10"]
    return ecrire_manifeste(chemin, versions=v["versions"], git=v["git"], python=v["python"],
                            revision_modele=rev[cv.MODELE], revision_adaptateur=rev[cv.JUGE],
                            revision_base=rev[cv.JUGE_BASE], commit_code=commit_code, b=b, go_id=go_id,
                            versions_figees={"chemin": cv.VERSIONS_FIGEES, "sha256": cv.sha_fichier(chemin_versions)})


# --- dépense du poste -------------------------------------------------------------------------------------------------

@dataclass
class Poste:
    """D : chaque instance comptée à son taux réel × heures de sa création à sa destruction (ou à maintenant), toutes
    instances du poste comprises (texte l. 252-254)."""
    b: float
    instances: list[dict] = field(default_factory=list)

    def ajouter(self, ident: str, c: float, creation: float) -> None:
        self.instances.append({"id": ident, "c": c, "creation": creation, "destruction": None})

    def detruite(self, ident: str, quand: float) -> None:
        for i in self.instances:
            if i["id"] == ident and i["destruction"] is None:
                i["destruction"] = quand

    def depense(self, maintenant: float | None = None) -> float:
        maintenant = time.time() if maintenant is None else maintenant
        return sum(float(i["c"]) * ((i["destruction"] or maintenant) - float(i["creation"])) / 3600
                   for i in self.instances)

    def d_avant(self, ident: str, maintenant: float | None = None) -> float:
        maintenant = time.time() if maintenant is None else maintenant
        return sum(float(i["c"]) * ((i["destruction"] or maintenant) - float(i["creation"])) / 3600
                   for i in self.instances if i["id"] != ident)

    def ecrire(self, chemin: Path) -> None:
        tmp = Path(str(chemin) + ".tmp")
        tmp.write_text(json.dumps({"b": self.b, "instances": self.instances}, sort_keys=True), encoding="utf-8")
        os.replace(tmp, chemin)

    @classmethod
    def lire(cls, chemin: Path) -> "Poste":
        d = json.loads(Path(chemin).read_text(encoding="utf-8"))
        return cls(b=float(d["b"]), instances=list(d["instances"]))


def instances_du_poste(anterieures: list[dict], b: float) -> list[dict]:
    """Correction 2 : chaque instance antérieure (lue dans `registres/depenses.md`) porte id, c, création, destruction
    et le B en vigueur à sa création ; tous égaux au B du manifeste (B fixé à la création de la première instance)."""
    out = []
    for i in anterieures:
        for cle in ("id", "c", "creation", "destruction", "B"):
            if cle not in i:
                raise GardeArret(f"instance antérieure : champ « {cle} » absent")
        if i["destruction"] is None:
            raise GardeArret("instance antérieure non détruite")
        if float(i["B"]) != float(b):
            raise GardeArret("B différent de celui de la première instance du poste")
        out.append({k: i[k] for k in ("id", "c", "creation", "destruction")})
    return out


class Veilleur:
    """Secours (B-5, correction 3) : détruit l'instance par son identifiant (R10), sans transfert, à
    `B − marge_secours` ou à `échéance + delai_secours_s` (`delai_secours_s ≤ 0`, correction 5). L'arrêt nominal à
    B − 2 se fait sur l'instance, puis transfert, puis destruction par la conduite. Lit l'état du poste dans un fichier
    à chaque passage : tourne dans un processus séparé (`main(["veilleur", …])`), qui survit à la conduite."""

    def __init__(self, fournisseur: Fournisseur, poste_fichier: Path, instance: str, echeance: float, journal: Path,
                 marge_secours: float = MARGE_SECOURS_USD, delai_secours_s: float = 0.0, periode_s: float = 30.0,
                 horloge=time.time, attendre=time.sleep):
        if float(delai_secours_s) > 0:
            raise GardeArret("veilleur : délai de secours positif refusé (destruction au plus tard à l'échéance)")
        self.f, self.poste_fichier, self.instance = fournisseur, Path(poste_fichier), instance
        self.echeance, self.journal = float(echeance), Path(journal)
        self.marge, self.delai, self.periode = float(marge_secours), float(delai_secours_s), float(periode_s)
        self.horloge, self.attendre = horloge, attendre
        self.cause: str | None = None

    def _poste(self) -> Poste:
        return Poste.lire(self.poste_fichier)

    def deja_detruite(self) -> bool:
        return any(i["id"] == self.instance and i["destruction"] is not None for i in self._poste().instances)

    def verifier(self) -> str | None:
        maintenant = self.horloge()
        poste = self._poste()
        if poste.depense(maintenant) >= poste.b - self.marge:
            return "dépense (seuil de secours)"
        if maintenant >= self.echeance + self.delai:
            return "échéance du GO (secours)"
        return None

    def boucle(self, passages: int | None = None) -> str | None:
        n = 0
        while passages is None or n < passages:
            n += 1
            if self.deja_detruite():
                return None
            cause = self.verifier()
            if cause:
                self.cause = cause
                self.f.detruire(self.instance)
                poste = self._poste()
                poste.detruite(self.instance, self.horloge())
                poste.ecrire(self.poste_fichier)
                with open(self.journal, "a", encoding="utf-8") as j:
                    j.write(json.dumps({"arret": cause, "instance": self.instance, "t": self.horloge()},
                                       ensure_ascii=False) + "\n")
                return cause
            self.attendre(self.periode)
        return None


def lancer_veilleur_processus(poste_fichier: Path, ident: str, echeance: float, journal: Path,
                              fournisseur: str = "vast", periode_s: float = 30.0,
                              marge_secours: float = MARGE_SECOURS_USD) -> int:
    """Processus séparé, nouvelle session (survit à la conduite et à la coupure de son terminal). Rend son PID."""
    cmd = [sys.executable, "-m", "controle_ia.temoin_bailey.lanceur_v3", "veilleur", "--poste", str(poste_fichier),
           "--instance", str(ident), "--echeance", repr(float(echeance)), "--journal", str(journal),
           "--fournisseur", fournisseur, "--periode", repr(float(periode_s)), "--marge", repr(float(marge_secours))]
    p = subprocess.Popen(cmd, start_new_session=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL)
    return p.pid


def arreter_veilleur(pid: int) -> None:
    """R10 : par PID."""
    try:
        os.kill(int(pid), signal.SIGTERM)
    except ProcessLookupError:
        pass


# --- amorce et commandes distantes ------------------------------------------------------------------------------------

def fabriquer_archive(depot: Path, commit: str, dossier: Path) -> tuple[Path, str]:
    """Correction 12 : archive `git archive` du commit du code (dépôt privé : rien n'est cloné sur l'instance)."""
    dossier.mkdir(parents=True, exist_ok=True)
    sortie = dossier / f"travail-{commit[:12]}.tar.gz"
    try:
        subprocess.run(["git", "-C", str(depot), "archive", "--format=tar.gz", "-o", str(sortie), commit],
                       check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise GardeArret("archive du code : commit introuvable ou dépôt illisible") from None
    return sortie, cv.sha_fichier(sortie)


def script_amorce(manifeste: dict, sha_archive: str) -> str:
    """Archive du code vérifiée par son empreinte puis dépliée ; dépôt public à son commit (jamais copié dans le dépôt
    de travail) ; Python 3.11 ; versions et commits du manifeste ; modèle, adaptateur du juge et base à leurs
    révisions, `refs/main` posé sur chacune (B-4). Le jeton est lu dans un fichier envoyé par `scp`, effacé à la sortie
    du script, quelle qu'elle soit."""
    v = manifeste["versions"]
    paquets = " ".join(shlex.quote(f"{p}=={x}") for p, x in sorted(v.items()) if p not in manifeste["git"])
    git = " ".join(shlex.quote(f"{p} @ git+{u}@{c}") for p, (u, c) in sorted(manifeste["git"].items()))
    echec = lambda cause: ("{ echo ETAT " + shlex.quote(json.dumps({"commande": "amorce", "finie": False,
                                                                    "cause": cause}, ensure_ascii=False))
                           + "; exit 3; }")
    py = "python" + str(manifeste["python"])
    lignes = ["set -euo pipefail", f"trap 'rm -f {JETON_DISTANT}' EXIT", "cd /root",
              f"echo {shlex.quote(sha_archive + '  ' + ARCHIVE_DISTANTE)} | sha256sum -c --quiet - || "
              + echec("empreinte de l'archive du code"),
              f"mkdir -p /root/travail && tar -xzf {ARCHIVE_DISTANTE} -C /root/travail",
              f"git init -q public && git -C public fetch -q --depth=1 {cv.DEPOT_PUBLIC} {cv.COMMIT_PUBLIC}"
              " && git -C public checkout -q FETCH_HEAD",
              f"command -v {py} > /dev/null || " + echec("Python " + str(manifeste["python"]) + " absent"),
              f"{py} -m venv /root/venv && . /root/venv/bin/activate",
              f"pip install -q {paquets}" + (f" {git}" if git else ""),
              f"pip install -q --no-deps -e /root/public/{cv.SOUS_DOSSIER}",
              f"export HF_HUB_CACHE={CACHE_HF}",
              f"test -s {JETON_DISTANT} || " + echec("jeton absent")]
    for depot, rev in ((cv.MODELE, manifeste["revision_modele"]),
                       (cv.JUGE, manifeste["juge"]["revision_adaptateur"]),
                       (cv.JUGE_BASE, manifeste["juge"]["revision_base"])):
        refs = f"{CACHE_HF}/models--{depot.replace('/', '--')}/refs"
        lignes += [f"huggingface-cli download {depot} --revision {shlex.quote(rev)} --quiet > /dev/null",
                   f"mkdir -p {refs} && printf %s {shlex.quote(rev)} > {refs}/main"]
    lignes.append(f"rm -f {JETON_DISTANT}")
    lignes.append("echo ETAT " + shlex.quote(json.dumps({"commande": "amorce", "finie": True})))
    return "\n".join(lignes) + "\n"


def commande_instance(sous_commande: str, **opts) -> str:
    morceaux = [f". /root/venv/bin/activate && cd /root/travail && PYTHONPATH=src HF_HUB_OFFLINE=1 HF_HUB_CACHE={CACHE_HF}",
                "python -m controle_ia.temoin_bailey.instance_v3", sous_commande]
    for k, v in opts.items():
        morceaux += [f"--{k.replace('_', '-')}", shlex.quote(str(v))]
    return " ".join(morceaux)


def commande_detachee(nom: str, commande: str) -> str:
    """P-f : la commande tourne détachée (nouvelle session) ; sa sortie reste sur l'instance ; seules la dernière ligne
    `ETAT` et une ligne `CODE n` sont écrites dans `<nom>.fin`, lu par `commande_sondage`. PID dans `<nom>.pid`."""
    d = ETATS_DISTANTS
    interne = (f"{commande} > {d}/{nom}.log 2>&1; c=$?; "
               f"{{ grep '^ETAT ' {d}/{nom}.log | tail -n 1; echo \"CODE $c\"; }} > {d}/{nom}.tmp; "
               f"mv {d}/{nom}.tmp {d}/{nom}.fin")
    return (f"mkdir -p {d} && setsid nohup bash -c {shlex.quote(interne)} > /dev/null 2>&1 < /dev/null & "
            f"echo $! > {d}/{nom}.pid")


def commande_sondage(nom: str) -> str:
    return f"cat {ETATS_DISTANTS}/{nom}.fin 2>/dev/null; true"


def commande_arret(nom: str) -> str:
    """R10 : arrêt du groupe de processus de la commande par son PID (identifiant), jamais par motif."""
    return f"kill -TERM -- -$(cat {ETATS_DISTANTS}/{nom}.pid) 2>/dev/null; true"


def lire_etat(sortie: str) -> dict:
    """Seule la ligne `ETAT {…}` revient au poste local (A-9) ; le reste de la sortie est ignoré."""
    for ligne in reversed(sortie.splitlines()):
        if ligne.startswith("ETAT "):
            return json.loads(ligne[5:])
    raise GardeArret("commande distante sans ligne d'état")


def lire_code(sortie: str) -> int | None:
    for ligne in reversed(sortie.splitlines()):
        if ligne.startswith("CODE "):
            return int(ligne[5:].strip())
    return None


def normaliser_execution(etat_: dict | None, code: int | None, phase: str) -> dict:
    """État d'une exécution tel que la liste d'arrêt le lit. Une garde levée par la commande avant l'enfant (dossier
    neuf, configuration effective) ou une commande sans ligne d'état devient une exécution en échec, sans tour."""
    if etat_ is not None and "code_retour" in etat_:
        return etat_
    message = (etat_ or {}).get("garde_tombee") or "commande distante sans ligne d'état"
    return {"commande": "executer", "phase": phase, "code_retour": code if code not in (None, 0) else 1,
            "cause_arret": "garde de démarrage" if "configuration effective" in message else None,
            "gardes_tombees": [message], "tours_marques": 0, "tours_complets": 0, "durees": {},
            "configuration_effective": "non décidée", "message": message}


def transferer(fournisseur: Fournisseur, ident: str, distant: str, local: Path, empreintes_instance: dict,
               erreurs: list | None = None) -> list[dict]:
    """Fichier par fichier, la seule liste fermée (B-6) ; un transfert, puis au plus un nouveau si une empreinte
    diffère. Un `scp` en échec est un écart (fichier absent du transfert), consigné dans `erreurs`, jamais une
    exception qui sort (correction 3). Rend les empreintes de chaque essai."""
    if not set(empreintes_instance) <= set(cv.SORTANTS):
        raise GardeArret("transfert : fichier hors de la liste fermée")
    essais = []
    for n in range(2):
        cible = local / f"transfert-{n + 1}"
        for rel in empreintes_instance:
            try:
                fournisseur.rapatrier_fichier(ident, f"{distant}/{rel}", cible / rel)
            except Exception as err:  # écart de transfert, consigné
                if erreurs is not None:
                    erreurs.append({"essai": n + 1, "fichier": rel, "erreur": type(err).__name__})
        obtenues = {rel: cv.sha_fichier(cible / rel) for rel in empreintes_instance if (cible / rel).is_file()}
        essais.append(obtenues)
        if obtenues == empreintes_instance:
            break
    return essais


def ordre_de_lancement(go_id: str, b: float, c: float, commit_code: str) -> dict:
    """Condition 8 : l'ordre cite le GO, B, le taux relevé et DEPOT_URL."""
    return {"GO_ID": go_id, "B": b, "c": c, "DEPOT_URL": DEPOT_URL, "commit_code": commit_code,
            "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def envoyer_jeton(fournisseur: Fournisseur, ident: str, variable: str = "HF_TOKEN") -> None:
    """S-3 : jeton lu dans l'environnement du poste local (jamais imprimé), écrit dans un fichier temporaire local de
    droits 600, envoyé par `scp`, puis effacé localement ; jamais sur une ligne de commande."""
    valeur = os.environ.get(variable)
    if not valeur:
        raise GardeArret(f"jeton d'accès absent de l'environnement local ({variable})")
    fd, chemin = tempfile.mkstemp(prefix="jeton-")
    try:
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(valeur)
        fournisseur.executer(ident, f"mkdir -p {Path(JETON_DISTANT).parent} && chmod 700 {Path(JETON_DISTANT).parent}")
        fournisseur.envoyer_fichier(ident, Path(chemin), JETON_DISTANT)
        fournisseur.executer(ident, f"chmod 600 {JETON_DISTANT}")
    finally:
        Path(chemin).unlink(missing_ok=True)


# --- conduite (A-8) ---------------------------------------------------------------------------------------------------

class _Arret(Exception):
    """Arrêt de la liste d'arrêt décidé par la conduite (dépense, échéance) : consigné au bilan."""


@dataclass
class Conduite:
    """Déroulé complet d'un poste sur une instance. `sortie` : dossier local neuf (bilan, manifestes versionnés,
    transferts scellés, journal des étapes `conduite-v3.jsonl`, état du poste `poste-v3.json`)."""
    fournisseur: Fournisseur
    manifeste_local: Path
    sortie: Path
    go_id: str
    texte_go: str
    offre: str
    image: str
    depot_local: Path
    instances_anterieures: list[dict]
    disque_go: int = 200
    horloge: object = time.time
    attendre: object = time.sleep
    periode_sondage_s: float = 60.0
    marge_secours: float = MARGE_SECOURS_USD
    marge_transfert_s: float = MARGE_TRANSFERT_S
    fournisseur_veilleur: str = "vast"
    lancer_veilleur: object = lancer_veilleur_processus
    arreter_veilleur: object = arreter_veilleur

    def _etape(self, objet: dict) -> None:
        with open(self.sortie / "conduite-v3.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({**objet, "t": self.horloge()}, ensure_ascii=False, sort_keys=True, default=str) + "\n")

    # bornes : dépense du poste à B − 2, échéance moins la marge de transfert
    def _borne(self) -> float:
        maintenant = self.horloge()
        reste = (self.b - 2 - self.poste.depense(maintenant)) / self.c * 3600
        return min(maintenant + reste, self.echeance - self.marge_transfert_s)

    def _avant(self, quoi: str) -> None:
        maintenant = self.horloge()
        if self.poste.depense(maintenant) >= self.b - 2:
            raise _Arret(f"dépense du poste ≥ B − 2 avant « {quoi} »")
        if maintenant >= self.echeance - self.marge_transfert_s:
            raise _Arret(f"échéance du GO (moins la marge de transfert) avant « {quoi} »")

    def _cmd(self, nom: str, commande: str, executer: bool = False) -> tuple[dict | None, int | None]:
        """Lance `commande` détachée sous le nom `nom`, puis la sonde jusqu'à sa fin ou jusqu'à la borne ; à la borne,
        arrêt par PID et `_Arret`. Pour une exécution, l'instance s'arrête elle-même (B − 2, échéance moins la marge) ;
        la borne locale est alors l'échéance moins la moitié de la marge."""
        self._avant(nom)
        self.lances.append(nom)
        self.fournisseur.executer(self.ident, commande_detachee(nom, commande), 120)
        borne = self.echeance - self.marge_transfert_s / 2 if executer else self._borne()
        while True:
            _code, sortie = self.fournisseur.executer(self.ident, commande_sondage(nom), 120)
            code = lire_code(sortie)
            if code is not None:
                try:
                    e = lire_etat(sortie)
                except GardeArret:
                    e = None
                self._etape({"commande": nom, "code": code, "etat": e})
                return e, code
            if self.horloge() >= borne:
                self.fournisseur.executer(self.ident, commande_arret(nom), 120)
                raise _Arret(f"borne de dépense ou d'échéance atteinte pendant « {nom} » : arrêt par PID")
            self.attendre(self.periode_sondage_s)

    def _manifeste(self, nom: str, contenu: dict) -> str:
        """Correction 10 : manifeste versionné, écrit localement sans écrasement, scellé, envoyé sur l'instance."""
        local = self.sortie / MANIFESTES[nom]
        if local.exists():
            raise GardeArret("manifeste versionné déjà présent (R12)")
        local.write_text(json.dumps(contenu, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        scellement.sceller(local)
        distant = f"/root/{MANIFESTES[nom]}"
        self.fournisseur.envoyer_fichier(self.ident, local, distant)
        return distant

    def _depense(self) -> str:
        return json.dumps({"d_avant": self.poste.d_avant(self.ident, self.horloge()), "c": self.c,
                           "creation": self.creation, "b": self.b})

    def _executer(self, phase: str, manifeste: str) -> dict:
        e, code = self._cmd(phase, commande_instance(
            "executer", travail=f"/root/x/{phase}", phase=phase, depense=self._depense(), echeance_go=self.echeance,
            marge_transfert=self.marge_transfert_s, manifeste=manifeste, clone="/root/public"), executer=True)
        return normaliser_execution(e, code, phase)

    def conduire(self) -> dict:
        man = json.loads(Path(self.manifeste_local).read_text(encoding="utf-8"))
        self.b = float(man["B"])
        anterieures = instances_du_poste(self.instances_anterieures, self.b)
        go = ligne_go(self.texte_go, self.go_id)
        verifier_go(go, self.b)
        verifier_non_revoque(self.texte_go, self.go_id)
        self.echeance = echeance_epoch(go["echeance"])
        if os.environ.get("GO_ID") != self.go_id:
            raise GardeArret("condition 2 : GO_ID absent ou différent de la ligne citée")
        if not os.environ.get("HF_TOKEN"):
            raise GardeArret("jeton d'accès absent de l'environnement local (HF_TOKEN)")
        if self.sortie.exists() and any(self.sortie.iterdir()):
            raise GardeArret("dossier de sortie de la conduite non neuf")
        self.sortie.mkdir(parents=True, exist_ok=True)
        archive, sha_archive = fabriquer_archive(Path(self.depot_local), man["commit_code"], self.sortie / "archive")
        self.poste = Poste(b=self.b, instances=anterieures)
        if self.poste.depense(self.horloge()) >= self.b - 2:
            raise GardeArret("dépense du poste ≥ B − 2 avant la création : rien ne tourne")
        self.ident = self.fournisseur.creer(self.offre, self.image, self.disque_go)
        self.creation = self.horloge()
        self.c = self.fournisseur.taux_horaire(self.ident)
        self.poste.ajouter(self.ident, self.c, self.creation)
        poste_fichier = self.sortie / "poste-v3.json"
        self.poste.ecrire(poste_fichier)
        self.lances: list[str] = []
        self._etape({"instance": self.ident, "creee": self.creation, "c": self.c, "archive_sha256": sha_archive,
                     "ordre": ordre_de_lancement(self.go_id, self.b, self.c, man["commit_code"])})
        pid_veilleur = self.lancer_veilleur(poste_fichier, self.ident, self.echeance, self.sortie / "arrets-v3.jsonl",
                                            self.fournisseur_veilleur)
        bilan = {"instance": self.ident, "d_avant_creation": self.poste.d_avant(self.ident, self.creation),
                 "archive_sha256": sha_archive}
        try:
            verifier_echeance(self.echeance, self.creation, self.b, self.c, self.marge_secours, self.marge_transfert_s)
            self._avant("amorce")
            self.fournisseur.envoyer_fichier(self.ident, archive, ARCHIVE_DISTANTE)
            amorce = self.sortie / "amorce-v3.sh"
            amorce.write_text(script_amorce(man, sha_archive), encoding="utf-8")
            self.fournisseur.envoyer_fichier(self.ident, amorce, "/root/amorce-v3.sh")
            envoyer_jeton(self.fournisseur, self.ident)
            e, _ = self._cmd("amorce", "bash /root/amorce-v3.sh")
            bilan["amorce"] = e
            if not e or e.get("finie") is not True:
                bilan["arret"] = "amorce non finie : rien ne tourne ; consigner"
                return bilan
            self.fournisseur.envoyer_fichier(self.ident, Path(self.manifeste_local), "/root/manifeste-v3.json")
            if Path(self.manifeste_local).resolve() != (self.sortie / MANIFESTES["initial"]).resolve():
                (self.sortie / MANIFESTES["initial"]).write_bytes(Path(self.manifeste_local).read_bytes())
                scellement.sceller(self.sortie / MANIFESTES["initial"])
            clone = "/root/public"
            dep = lambda: dict(depense=self._depense())
            mep, _ = self._cmd("mise-en-place", commande_instance(
                "mise-en-place", travail="/root/x/mise-en-place", manifeste="/root/manifeste-v3.json",
                clone=clone, echeance_go=self.echeance, marge_transfert=self.marge_transfert_s, **dep()))
            bilan["mise_en_place"] = mep
            if not mep or "garde_tombee" in mep or "pas_par_tour" not in mep:
                bilan["arret"] = "garde de mise en place tombée : pas de run, pas de verdict ; consigner"
                return bilan
            man = {**man, "pas_par_tour": mep["pas_par_tour"], "longueur_suffixe": mep["longueur_suffixe"],
                   "ecart_10": mep["ecart_10"]}
            m_mep = self._manifeste("mise-en-place", man)
            juge, _ = self._cmd("controle-juge", commande_instance(
                "controle-juge", travail="/root/x/controle-juge", manifeste=m_mep, clone=clone,
                mise_en_place="/root/x/mise-en-place", echeance_go=self.echeance,
                marge_transfert=self.marge_transfert_s, **dep()))
            bilan["controle_juge"] = juge
            if not juge or "garde_tombee" in juge or juge.get("etats", {}).get("tenus") is not True:
                bilan["arret"] = "garde du juge ou contrôle du juge hors seuil : arrêt avant le pilote ; nœud"
                return bilan
            pilotes = []
            for phase in ("pilote", "pilote-reprise"):
                r = self._executer(phase, m_mep)
                pilotes.append(r)
                issue = issue_pilote(r)
                if issue == "finie":
                    break
                if issue == "sonde orientée":
                    bilan["pilote"] = pilotes
                    bilan["arret"] = "non interprétable (sonde orientée au pilote) ; pas de run principal"
                    return bilan
                if issue == "arrêt":
                    bilan["pilote"] = pilotes
                    bilan["arret"] = "pilote arrêté (dépense ou échéance du GO) : pas de run principal ; nœud"
                    return bilan
            else:
                bilan["pilote"] = pilotes
                bilan["arret"] = "seconde chute du pilote : pas de run principal, pas de verdict ; nœud"
                return bilan
            bilan["pilote"] = pilotes
            fixe_t = next(p for p in pilotes if "0" in p.get("durees", {}) and "1" in p.get("durees", {}))
            regle, _ = self._cmd("regle", commande_instance(
                "regle-tours", travail="/root/x/regle", manifeste=m_mep, pilote=f"/root/x/{fixe_t['phase']}", **dep()))
            bilan["regle"] = regle
            if not regle or "K" not in regle:
                bilan["arret"] = "règle du nombre de tours non calculée : arrêt ; nœud"
                return bilan
            if regle["K"] < 20:
                bilan["arret"] = "K < 20 après le pilote : arrêt, devis révisé à Lazar"
                return bilan
            man = {**man, "regle_tours": {k: regle[k] for k in ("B", "R", "D", "c", "t", "H_heures", "K")}}
            m_regle = self._manifeste("regle", man)
            principal = self._executer("principal", m_regle)
            bilan["principal"] = [principal]
            if relance_permise(principal):
                d = self.poste.depense(self.horloge())
                k2 = an.nombre_de_tours(self.b, round(d, 4), self.c, regle["t"])["K"]
                if k2 < 20:
                    bilan["arret"] = "relance impossible (K < 20) : pas de verdict ; nœud"
                    return bilan
                man = {**man, "regle_tours": {**man["regle_tours"], "K": k2, "D": round(d, 4), "relance": True,
                                              "premiere_execution": man["regle_tours"]}}
                m_relance = self._manifeste("relance", man)
                bilan["principal"].append(self._executer("principal-relance", m_relance))
            return bilan
        except _Arret as arret:
            bilan["arret"] = str(arret)
            return bilan
        except Exception as err:
            bilan["erreur"] = f"{type(err).__name__}: {err}"[:300]
            raise
        finally:
            try:
                self._rapatrier(bilan)
            except Exception as err:  # consigné ; la destruction suit dans tous les cas
                bilan["rapatriement_erreur"] = f"{type(err).__name__}: {err}"[:300]
            detruite = False
            try:
                self.fournisseur.detruire(self.ident)  # R10, par identifiant
                detruite = True
            except Exception as err:  # le veilleur, processus séparé, reste actif
                bilan["destruction_erreur"] = f"{type(err).__name__}: {err}"[:300]
            if detruite:
                self.poste.detruite(self.ident, self.horloge())
                self.poste.ecrire(poste_fichier)
                self.arreter_veilleur(pid_veilleur)
            bilan["detruite"] = detruite
            bilan["depense"] = self.poste.depense(self.horloge())
            self._etape({"instance": self.ident, "detruite": detruite, "depense": bilan["depense"]})
            sortie_bilan = self.sortie / "bilan-conduite-v3.json"
            sortie_bilan.write_text(json.dumps(bilan, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                                    encoding="utf-8")
            scellement.sceller(sortie_bilan)

    def _rapatrier(self, bilan: dict) -> None:
        """Avant destruction : empreintes sur l'instance, transfert des journaux et des fichiers d'état de chaque
        étape lancée, comparaison, second transfert au plus, scellement après égalité (corrections 7 et 11)."""
        transferts = {}
        dossiers = {"mise-en-place": "mise-en-place", "controle-juge": "controle-juge", "regle": "regle",
                    "pilote": "pilote", "pilote-reprise": "pilote-reprise", "principal": "principal",
                    "principal-relance": "principal-relance"}
        for etape in ETAPES:
            if etape not in self.lances:
                continue
            distant = f"/root/x/{dossiers[etape]}"
            local = self.sortie / etape
            res = {"erreurs": []}
            transferts[etape] = res
            try:
                _c, sortie = self.fournisseur.executer(self.ident, commande_instance("empreintes", travail=distant), 600)
                lire_etat(sortie)
                self.fournisseur.rapatrier_fichier(self.ident, f"{distant}/{cv.EMPREINTES_INSTANCE}",
                                                   local / cv.EMPREINTES_INSTANCE)
                emp = json.loads((local / cv.EMPREINTES_INSTANCE).read_text(encoding="utf-8"))
            except Exception as err:  # étape sans empreintes : consignée, les autres continuent
                res["erreurs"].append({"etape": "empreintes", "erreur": f"{type(err).__name__}: {err}"[:200]})
                continue
            essais = transferer(self.fournisseur, self.ident, distant, local, emp, res["erreurs"])
            res.update({"empreintes_instance": emp, "essais": essais, "foi": None})
            for n, obtenues in enumerate(essais, start=1):
                if obtenues == emp:
                    res["foi"] = f"transfert-{n}"
                    scellement.sceller(local / cv.EMPREINTES_INSTANCE)
                    for rel in emp:
                        scellement.sceller(local / f"transfert-{n}" / rel)
                    break
        bilan["transferts"] = transferts


# --- point d'entrée du veilleur ---------------------------------------------------------------------------------------

def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=["veilleur"])
    p.add_argument("--poste", required=True)
    p.add_argument("--instance", required=True)
    p.add_argument("--echeance", type=float, required=True)
    p.add_argument("--journal", required=True)
    p.add_argument("--fournisseur", default="vast")
    p.add_argument("--periode", type=float, default=30.0)
    p.add_argument("--marge", type=float, default=MARGE_SECOURS_USD)
    a = p.parse_args(argv)
    v = Veilleur(fournisseur_depuis(a.fournisseur), Path(a.poste), a.instance, a.echeance, Path(a.journal),
                 marge_secours=a.marge, periode_s=a.periode)
    v.boucle()
    return 0


if __name__ == "__main__":
    sys.exit(main())
