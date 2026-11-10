"""Lanceur local (orchestration de l'instance louée) — témoin « attaque publiée reproduite » (Bailey et collègues), v8.

La v8 emploie `instance_v8` et `lecture_v8` (décision de Lazar du 10 novembre 2026, points A-1 et A-2 de
`relecture-lignes-touchees-code-condition6-v7-bailey-v1.md`, `5831e98c…`) : `INSTANCE_MODULE`, `CHEMINS_ARCHIVE` et le
module du veilleur sont ceux de la v8. A-2 : une exécution du pilote dont l'issue est « ligne de garde coupée »
(`lecture_v8.issue_pilote` : dernière ligne coupée dans un journal de gardes, garde inconnue) **arrête** la conduite :
pas de reprise, pas de run principal ; le bilan dit « pas de run principal ; ligne de garde coupée au pilote (garde
inconnue) ; nœud » et porte les exécutions du pilote (`pilote`, avec leurs gardes tombées et lignes coupées). Une
exécution morte dont `tours` est relu reçoit les gardes tombées de la ligne `ETAT` (ligne coupée nommée comprise).
Rien d'autre ne change.

Docstring de la v7 :

La v7 emploie `instance_v7` et `lecture_v7` (relecture des lignes touchées v5 → v6, `a46dc4fb…`, C-1 à C-4) :
`INSTANCE_MODULE`, `CHEMINS_ARCHIVE` et le module du veilleur sont ceux de la v7 ; la ligne `ETAT` de `tours` porte
les lignes coupées ignorées sur l'instance (`lignes_tronquees_ignorees`), reportées dans l'exécution rendue au bilan
(exécution morte) et dans `etats_reconstitues` (C-2). Rien d'autre ne change.

Docstring de la v6 :

La v6 corrige M-1 de la relecture des lignes touchées v5 (`22879993…`) : une exécution morte est inscrite dans
`arretees` (cause « coupure de l'hôte ») dès qu'elle est vue morte, pour que la reconstitution de son état soit
retentée avant les empreintes si la première tentative échoue ; et emploie `instance_v6` et `lecture_v6` (M-2).

La v5 reprend la v4 (`lanceur_v4.py`, docstring ci-dessous) et applique la relecture des lignes touchées v3 → v4
(`relecture-lignes-touchees-code-condition6-v4-bailey-v1.md`, `ff6c76c7…`) :
- C8 (N-1) : toute exécution qui n'a pas écrit son état en reçoit un **sur l'instance, avant les empreintes**, par
  `instance_v5 tours --ecrire-etat` (jamais d'écrasement ; « reconstitué » ; code non nul ; cause) : sur une exécution
  morte (cause « coupure de l'hôte », après l'arrêt du groupe, C10), et dans `_finir` pour toute exécution que la
  conduite a arrêtée par PID (cause « dépense » au seuil local, « échéance du GO » à la borne d'échéance, « instance
  injoignable », ou « arrêt par la conduite » sur une autre sortie) ; la lecture (`lecture_v5`) lit alors le run
  tronqué sur K′ et la relance complète ;
- C9 (N-2) : destruction en échec → un veilleur à échéance 0 est **toujours** lancé, puis l'ancien est arrêté s'il
  est vu vivant (sinon gardé, alerte) ;
- C10 (N-3) : sur `MORT` (meneur mort sans `.fin`), le groupe de la commande est arrêté par son PID avant `tours` et
  avant toute relance ; l'arrêt attend la fin du groupe (TERM, attente bornée, puis KILL) ;
- C11 (N-5) : étiquette unique par conduite à la création (`--label`) ; si `creer` lève, inventaire filtré sur cette
  seule étiquette, destruction de ces seuls identifiants ; sinon alerte au bilan (« création incertaine : inventaire
  R10 manuel ») ; l'étiquette est écrite à l'ordre de lancement ;
- N-4 : le lancement détaché écrit, avec le PID, son identité (`boot_id` et heure de départ, champ 22 de
  `/proc/<pid>/stat`) dans `<nom>.debut` ; « vivant » exige la même identité ; l'arrêt par PID ne vise le groupe que si
  le meneur a cette identité ou n'existe plus (un PID réemployé n'est jamais signalé) ;
- remarque (R10) : le veilleur local est suivi par son objet `Popen` ; un veilleur déjà récolté n'est jamais signalé ;
  `processus_vivant` ne récolte plus un PID inconnu.
Noms des fichiers de la conduite en v5 (`conduite-v5.jsonl`, `poste-v5.json`, `arrets-v5.jsonl`,
`bilan-conduite-v5.json`, `amorce-v5.sh`). Lectures : liste
`docs/notes/reproduction-attaque-publiee-v1/lectures-a-acter-addendum-condition6-v3.md`.

Docstring de la v4 :

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : règle du nombre de tours (B, R,
D, c), liste d'arrêt, pilote et reprise, relance, transfert et comparaison des empreintes avant destruction, conditions
de lancement 2 et 8. La v4 reprend la v3 (`lanceur_v3.py`, dont la docstring dit les corrections 1 à 18 du rapport
`4f079ece…`) et applique la relecture en différentiel du code v3
(`relecture-differentiel-code-condition6-v3-bailey-v1.md`, `a2107244…`), corrections C1 à C7 :
- C1 (D-1) : le `try … finally` qui rapatrie puis détruit s'ouvre **aussitôt après** `creer` : relevé du taux,
  écriture du poste, journal des étapes et lancement du veilleur sont dedans ; si le taux n'a pu être lu, l'instance
  est détruite quand même (sa dépense est alors signalée au bilan, à relever dans `registres/depenses.md`) ; la
  destruction est retentée (`ESSAIS_DESTRUCTION`), et si elle échoue sans veilleur vivant, un veilleur est lancé avec
  une échéance immédiate, qui retente la destruction à chaque période ;
- C2 (D-2, D-7) : `Veilleur.boucle` met chaque passage dans un `try` ; toute erreur est écrite à son journal ; la
  destruction est retentée à chaque période jusqu'à réussir ; poste illisible → dernier poste lu, ou, s'il n'y en a
  aucun, destruction ; le veilleur écrit un battement (`<journal>.battement`) à chaque passage et sa sortie d'erreur
  dans `<journal>.err`. La conduite vérifie qu'il vit (PID vivant et non zombie, battement frais,
  `verifier_veilleur`) avant toute commande et à chaque sondage ; mort → une relance du veilleur, sinon arrêt et
  destruction. `marge_secours` et la période du veilleur lui sont passées ;
- C3 (D-3) : `FournisseurVast.executer` rattrape `TimeoutExpired` et l'échec de `vastai ssh-url` (code 255) ; la
  conduite tolère les sondages en échec jusqu'à `SONDAGES_EN_ECHEC_MAX` consécutifs **ou** `DUREE_SANS_SONDAGE_MAX_S`
  sans sondage réussi (instance tenue pour injoignable : arrêt) ; sur toute sortie anormale, la commande en cours est
  arrêtée par son PID **avant** le rapatriement ;
- C4 (D-4) : chaque sondage vérifie que le PID de la commande vit (`kill -0`) ; mort sans `.fin` → état
  « commande distante sans ligne d'état (coupure de l'hôte) », normalisé, tours complets relus sur l'instance
  (`instance_v4 tours`, sans note) : relance selon la liste ; la borne locale d'une exécution est le premier de
  `échéance − marge/2` et de l'instant où D atteint `B − SEUIL_LOCAL_USD` (1 USD, entre B − 2 et B − 0,5 ; valeur à
  acter) ; le lancement détaché rend `LANCE <pid>` après avoir vérifié `<nom>.pid` ; sinon un nouvel essai
  (idempotent : rien n'est relancé si la commande vit ou a fini), puis arrêt ;
- C5 (D-5) : attente de l'instance prête (état « running » de `vastai show instance`, puis `ssh … true` accepté),
  bornée (`DELAI_PRETE_S`), comptée dans D ; `ssh` et `scp` avec `StrictHostKeyChecking=accept-new` et `BatchMode` ;
- C6 (D-6) : l'archive envoyée ne contient que les fichiers de `src/` dont l'instance a besoin (`CHEMINS_ARCHIVE`,
  fermeture des imports vérifiée par l'essai) ; rien de `docs/`, `donnees/`, `diag/`, `registres/` ni du reste de
  `src/` ne part sur l'hôte loué ;
- C7 (D-8) : `instance_v4 regle-tours` met K et la garde au même `ETAT` ; « K < 20 après le pilote : arrêt, devis
  révisé à Lazar » est atteignable ;
- lecture 7 (section 3) : l'échéance « AAAA-MM-JJ » est lue comme la fin du jour à Paris (22:59:59 UTC en
  hiver), lecture prudente, fuseau à acter ;
- P-i : la ligne de GO est lue sur `origin/main` (`texte_go_main`, `git show origin/main:registres/go.md`, après un
  `git fetch origin main` explicite de l'appelant) ; la conduite refuse un texte de GO différent de celui-là.
Ce module ne lit aucune note. Lectures de lignes scellées faites ici : liste
`docs/notes/reproduction-attaque-publiee-v1/lectures-a-acter-addendum-condition6-v2.md`.
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
import uuid
from dataclasses import dataclass, field
from pathlib import Path

from .. import scellement
from ..gardes import GardeArret
from . import analyse_v3 as an
from . import conventions_v3 as cv
from .lecture_v8 import ETAPES, ISSUE_LIGNE_COUPEE, MANIFESTES, issue_pilote, relance_permise

DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"  # cité dans l'ordre de lancement (condition 8)
CACHE_HF = "/root/hf"
JETON_DISTANT = "/root/.cache/huggingface/token"
ARCHIVE_DISTANTE = "/root/travail.tar.gz"
ETATS_DISTANTS = "/root/etats"
EMPREINTE_PREREG = "fb6c2f34"
EMPREINTE_DEVIS = "f9c8c66e"
MARGE_SECOURS_USD = 0.5
MARGE_TRANSFERT_S = 3600.0
SEUIL_LOCAL_USD = 1.0  # C4 : arrêt local d'une exécution à D ≥ B − 1 (entre B − 2 et B − 0,5) ; valeur à acter
SONDAGES_EN_ECHEC_MAX = 30  # C3 : sondages consécutifs en échec tolérés …
DUREE_SANS_SONDAGE_MAX_S = 3600.0  # … ou durée sans sondage réussi, avant de tenir l'instance pour injoignable
DELAI_PRETE_S = 1800.0  # C5 : attente bornée de l'instance prête
ESSAIS_DESTRUCTION = 3  # C1 : essais de destruction par la conduite avant de s'en remettre au veilleur
INSTANCE_MODULE = "controle_ia.temoin_bailey.instance_v8"
EXECUTIONS = ("pilote", "pilote-reprise", "principal", "principal-relance")
PREFIXE_ETIQUETTE = "temoin-bailey-c6-"  # C11 : étiquette unique par conduite (`--label`)
# C6 : seuls fichiers envoyés sur l'instance (fermeture des imports de `instance_v8`, vérifiée par l'essai)
CHEMINS_ARCHIVE = ("src/controle_ia/__init__.py", "src/controle_ia/gardes.py", "src/controle_ia/scellement.py",
                   "src/controle_ia/temoin_bailey/__init__.py", "src/controle_ia/temoin_bailey/analyse_v3.py",
                   "src/controle_ia/temoin_bailey/conventions_v3.py", "src/controle_ia/temoin_bailey/execution_v3.py",
                   "src/controle_ia/temoin_bailey/journaliseur_v3.py", "src/controle_ia/temoin_bailey/lecture_v8.py",
                   "src/controle_ia/temoin_bailey/instance_v8.py")


class Fournisseur:
    def creer(self, offre: str, image: str, disque_go: int, etiquette: str | None = None) -> str: ...
    def inventaire(self, etiquette: str) -> list[str]: ...  # C11 : identifiants portant cette seule étiquette
    def taux_horaire(self, ident: str) -> float: ...
    def statut(self, ident: str) -> str | None: ...
    def detruire(self, ident: str) -> None: ...
    def executer(self, ident: str, commande: str, delai_s: float | None = None) -> tuple[int, str]: ...
    def rapatrier_fichier(self, ident: str, distant: str, local: Path) -> None: ...
    def envoyer_fichier(self, ident: str, local: Path, distant: str) -> None: ...


OPTIONS_SSH = ("-o", "StrictHostKeyChecking=accept-new", "-o", "BatchMode=yes", "-o", "ConnectTimeout=30")


class FournisseurVast(Fournisseur):
    """Commande `vastai` (la clé est lue par la commande ; ce module ne la lit ni ne l'imprime). Aucune variable
    d'environnement n'est passée à la création (le jeton passe par un fichier, S-3). C3 : `executer` ne lève jamais
    sur une coupure (adresse illisible, `vastai ssh-url` en échec, délai dépassé) : il rend le code 255. C5 : `ssh` et
    `scp` acceptent une clé d'hôte neuve et ne posent aucune question (`BatchMode`)."""

    def _vast(self, *args: str) -> str:
        return subprocess.run(["vastai", *args], check=True, capture_output=True, text=True, timeout=120).stdout

    def creer(self, offre, image, disque_go, etiquette=None):
        args = ["create", "instance", offre, "--image", image, "--disk", str(disque_go), "--ssh", "--direct", "--raw"]
        if etiquette:
            args += ["--label", etiquette]  # C11
        return str(json.loads(self._vast(*args))["new_contract"])

    def inventaire(self, etiquette):
        """C11 : identifiants des instances du compte dont l'étiquette est exactement `etiquette` (aucune autre)."""
        return [str(i["id"]) for i in json.loads(self._vast("show", "instances", "--raw"))
                if str(i.get("label") or "") == etiquette]

    def taux_horaire(self, ident):
        return float(json.loads(self._vast("show", "instance", ident, "--raw"))["dph_total"])

    def statut(self, ident):
        return json.loads(self._vast("show", "instance", ident, "--raw")).get("actual_status")

    def detruire(self, ident):
        self._vast("destroy", "instance", ident)

    def _ssh(self, ident) -> tuple[str, str]:
        m = re.match(r"ssh://([^@]+)@([^:]+):(\d+)", self._vast("ssh-url", ident).strip())
        if not m:
            raise GardeArret("adresse de l'instance illisible")
        return f"{m.group(1)}@{m.group(2)}", m.group(3)

    def executer(self, ident, commande, delai_s=None):
        try:
            hote, port = self._ssh(ident)
            p = subprocess.run(["ssh", *OPTIONS_SSH, "-p", port, hote, commande], capture_output=True, text=True,
                               timeout=delai_s)
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, GardeArret, OSError):
            return 255, ""
        return p.returncode, p.stdout

    def rapatrier_fichier(self, ident, distant, local):
        hote, port = self._ssh(ident)
        local.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["scp", *OPTIONS_SSH, "-P", port, f"{hote}:{distant}", str(local)], check=True,
                       capture_output=True, timeout=3600)

    def envoyer_fichier(self, ident, local, distant):
        hote, port = self._ssh(ident)
        subprocess.run(["scp", *OPTIONS_SSH, "-P", port, str(local), f"{hote}:{distant}"], check=True,
                       capture_output=True, timeout=3600)


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


def texte_go_main(depot: Path, ref: str = "origin/main") -> str:
    """P-i : le registre des GO fait foi sur `main` ; il est lu par `git show origin/main:registres/go.md`, jamais
    dans la branche de travail (la ligne GO-2026-11-10-10 n'y est pas). Aucune requête réseau ici : l'appelant fait
    d'abord `git fetch origin main` (refspec explicite)."""
    try:
        return subprocess.run(["git", "-C", str(depot), "show", f"{ref}:registres/go.md"], check=True,
                              capture_output=True, text=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise GardeArret("condition 2 : registres/go.md illisible sur origin/main") from None


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


FUSEAU_ECHEANCE = "Europe/Paris"  # lecture 7 (section 3 du rapport `a2107244…`) : lecture prudente, à acter


def echeance_epoch(echeance: str, fuseau: str = FUSEAU_ECHEANCE) -> float:
    """« AAAA-MM-JJ » : lue comme la fin de ce jour **à Paris** (23:59:59, heure de Paris : 22:59:59 UTC en hiver),
    lecture prudente de la liste v2 (lecture 7 : la v3 lisait 23:59:59 UTC, une heure au-delà de la fin du jour à
    Paris) ; fuseau à acter par Lazar ; « AAAA-MM-JJTHH:MMZ » : l'instant dit, en UTC. Fuseau introuvable : arrêt
    (aucun repli silencieux)."""
    import calendar
    import datetime
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2}))?", echeance)
    if not m:
        raise GardeArret("condition 2 : échéance du GO illisible")
    a, mo, j = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if m.group(4):
        return calendar.timegm((a, mo, j, int(m.group(4)), int(m.group(5)), 0))
    try:
        from zoneinfo import ZoneInfo
        tz = ZoneInfo(fuseau)
    except Exception:
        raise GardeArret(f"condition 2 : fuseau de l'échéance introuvable ({fuseau})") from None
    return datetime.datetime(a, mo, j, 23, 59, 59, tzinfo=tz).timestamp()


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
    à chaque passage : tourne dans un processus séparé (`main(["veilleur", …])`), qui survit à la conduite.
    C2 : chaque passage est dans un `try` ; une erreur (poste illisible, destruction refusée) est écrite au journal et
    le passage suivant recommence, jusqu'à ce que la destruction réussisse ; poste illisible → dernier poste lu, ou,
    s'il n'y en a aucun, destruction (cause « poste illisible (secours) ») ; un battement est écrit à chaque passage."""

    def __init__(self, fournisseur: Fournisseur, poste_fichier: Path, instance: str, echeance: float, journal: Path,
                 marge_secours: float = MARGE_SECOURS_USD, delai_secours_s: float = 0.0, periode_s: float = 30.0,
                 horloge=time.time, attendre=time.sleep, battement: Path | None = None):
        if float(delai_secours_s) > 0:
            raise GardeArret("veilleur : délai de secours positif refusé (destruction au plus tard à l'échéance)")
        self.f, self.poste_fichier, self.instance = fournisseur, Path(poste_fichier), instance
        self.echeance, self.journal = float(echeance), Path(journal)
        self.marge, self.delai, self.periode = float(marge_secours), float(delai_secours_s), float(periode_s)
        self.horloge, self.attendre = horloge, attendre
        self.battement = Path(battement) if battement is not None else Path(str(self.journal) + ".battement")
        self.cause: str | None = None
        self.dernier_poste: Poste | None = None

    def _noter(self, objet: dict) -> None:
        try:
            with open(self.journal, "a", encoding="utf-8") as j:
                j.write(json.dumps({**objet, "instance": self.instance, "t": self.horloge()}, ensure_ascii=False)
                        + "\n")
        except OSError:
            pass

    def _battre(self) -> None:
        try:
            tmp = Path(str(self.battement) + ".tmp")
            tmp.write_text(json.dumps({"t": time.time(), "pid": os.getpid()}), encoding="utf-8")
            os.replace(tmp, self.battement)
        except OSError:
            pass

    def _poste(self) -> Poste | None:
        """Poste lu au fichier ; illisible → dernier poste lu (erreur notée), ou `None` s'il n'y en a aucun."""
        try:
            self.dernier_poste = Poste.lire(self.poste_fichier)
        except Exception as err:
            self._noter({"erreur": f"poste illisible : {type(err).__name__}"})
        return self.dernier_poste

    def deja_detruite(self) -> bool:
        poste = self._poste()
        return poste is not None and any(i["id"] == self.instance and i["destruction"] is not None
                                         for i in poste.instances)

    def verifier(self, poste: Poste | None = None) -> str | None:
        maintenant = self.horloge()
        poste = self._poste() if poste is None else poste
        if poste is None:
            return "poste illisible (secours)"
        if poste.depense(maintenant) >= poste.b - self.marge:
            return "dépense (seuil de secours)"
        if maintenant >= self.echeance + self.delai:
            return "échéance du GO (secours)"
        return None

    def _passage(self) -> str | None:
        poste = self._poste()
        if poste is not None and any(i["id"] == self.instance and i["destruction"] is not None
                                     for i in poste.instances):
            return "déjà détruite"
        cause = self.verifier(poste)
        if not cause:
            return None
        self.cause = cause
        self.f.detruire(self.instance)  # une exception ici : notée, retentée au passage suivant
        self._noter({"arret": cause})
        try:
            poste = Poste.lire(self.poste_fichier)
            poste.detruite(self.instance, self.horloge())
            poste.ecrire(self.poste_fichier)
        except Exception as err:
            self._noter({"erreur": f"poste non mis à jour après destruction : {type(err).__name__}"})
        return cause

    def boucle(self, passages: int | None = None) -> str | None:
        n = 0
        while passages is None or n < passages:
            n += 1
            self._battre()
            try:
                cause = self._passage()
                if cause == "déjà détruite":
                    return None
                if cause:
                    return cause
            except Exception as err:  # C2 : jamais de sortie sur une erreur ; retenté à la période suivante
                self._noter({"erreur": f"{type(err).__name__}: {err}"[:300], "cause_visee": self.cause})
            self.attendre(self.periode)
        return None


def lancer_veilleur_processus(poste_fichier: Path, ident: str, echeance: float, journal: Path,
                              fournisseur: str = "vast", periode_s: float = 30.0,
                              marge_secours: float = MARGE_SECOURS_USD) -> int:
    """Processus séparé, nouvelle session (survit à la conduite et à la coupure de son terminal). Rend son PID. Sa
    sortie d'erreur va dans `<journal>.err` ; son battement dans `<journal>.battement` (C2)."""
    cmd = [sys.executable, "-m", "controle_ia.temoin_bailey.lanceur_v8", "veilleur", "--poste", str(poste_fichier),
           "--instance", str(ident), "--echeance", repr(float(echeance)), "--journal", str(journal),
           "--fournisseur", fournisseur, "--periode", repr(float(periode_s)), "--marge", repr(float(marge_secours))]
    with open(str(journal) + ".err", "ab") as err:
        p = subprocess.Popen(cmd, start_new_session=True, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                             stderr=err)
    _VEILLEURS[p.pid] = p
    return p.pid


_VEILLEURS: dict[int, subprocess.Popen] = {}  # remarque R10 (v5) : veilleurs lancés par ce processus, par PID


def processus_vivant(pid: int) -> bool:
    """Vivant et non zombie. Un veilleur lancé par ce processus est suivi par son `Popen` (récolté par `poll`, qui le
    sait ensuite fini) ; un autre PID n'est jamais récolté ici (v5) : son état est lu dans `/proc`."""
    p = _VEILLEURS.get(int(pid))
    if p is not None:
        return p.poll() is None
    statut = Path(f"/proc/{int(pid)}/status")
    try:
        for ligne in statut.read_text().splitlines():
            if ligne.startswith("State:"):
                return "Z" not in ligne.split()[1]
    except OSError:
        pass
    try:
        os.kill(int(pid), 0)
    except (ProcessLookupError, PermissionError):
        return False
    return True


def verifier_veilleur(pid: int | None, journal: Path, delai_s: float = 20.0, fraicheur_s: float = 180.0) -> bool:
    """C2 : le veilleur vit (PID vivant, non zombie) et a écrit un battement depuis moins de `fraicheur_s`. Attend au
    plus `delai_s` le premier battement."""
    if pid is None:
        return False
    battement = Path(str(journal) + ".battement")
    fin = time.time() + float(delai_s)
    while True:
        if not processus_vivant(pid):
            return False
        try:
            t = float(json.loads(battement.read_text(encoding="utf-8"))["t"])
            if time.time() - t <= float(fraicheur_s):
                return True
        except (OSError, ValueError, KeyError):
            pass
        if time.time() >= fin:
            return False
        time.sleep(0.2)


def arreter_veilleur(pid: int) -> None:
    """R10 : par PID. v5 : un veilleur lancé par ce processus est signalé par son `Popen`, qui ne signale jamais un
    processus déjà récolté (PID peut-être réemployé)."""
    p = _VEILLEURS.get(int(pid))
    if p is not None:
        p.send_signal(signal.SIGTERM)  # sans effet si `poll` l'a déjà récolté
        return
    try:
        os.kill(int(pid), signal.SIGTERM)
    except ProcessLookupError:
        pass


# --- amorce et commandes distantes ------------------------------------------------------------------------------------

def fabriquer_archive(depot: Path, commit: str, dossier: Path,
                      chemins: tuple[str, ...] = CHEMINS_ARCHIVE) -> tuple[Path, str]:
    """Correction 12 et C6 : archive `git archive` du commit du code, **limitée aux fichiers de `src/` dont l'instance
    a besoin** (`CHEMINS_ARCHIVE`) ; dépôt privé : rien n'est cloné sur l'instance ; aucun fichier de `docs/`,
    `donnees/`, `diag/`, `registres/`, ni le reste de `src/`, ne part sur l'hôte loué."""
    if not chemins or any(not c.startswith("src/") or ".." in c for c in chemins):
        raise GardeArret("archive du code : chemins hors de src/")
    dossier.mkdir(parents=True, exist_ok=True)
    sortie = dossier / f"travail-{commit[:12]}.tar.gz"
    try:
        subprocess.run(["git", "-C", str(depot), "archive", "--format=tar.gz", "-o", str(sortie), commit, "--",
                        *chemins], check=True, capture_output=True)
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
                f"python -m {INSTANCE_MODULE}", sous_commande]
    for k, v in opts.items():
        if v is True:  # v5 : option sans valeur (`--ecrire-etat`)
            morceaux.append(f"--{k.replace('_', '-')}")
        else:
            morceaux += [f"--{k.replace('_', '-')}", shlex.quote(str(v))]
    return " ".join(morceaux)


def _identite(p: str) -> str:
    """N-4 : identité d'un PID (expression shell `p`) : `boot_id` du noyau et heure de départ du processus (champ 22 de
    `/proc/<pid>/stat`, compté après le nom entre parenthèses, d'où le champ 20 une fois le nom retiré)."""
    return (f"$(cat /proc/sys/kernel/random/boot_id 2>/dev/null) "
            f"$(sed 's/^.*) //' /proc/{p}/stat 2>/dev/null | cut -d' ' -f20)")


def _meme_identite(p: str, debut: str) -> str:
    return f"[ \"{_identite(p)}\" = \"$(cat {debut} 2>/dev/null)\" ]"


def _pid_vit(pid: str, debut: str) -> str:
    """Test shell : le PID lu dans `pid` vit, n'est pas un zombie (`kill -0` réussit sur un zombie, d'où `/proc`) et
    a l'identité écrite à son lancement dans `debut` (N-4 : un PID réemployé n'est pas « vivant »)."""
    return (f"{{ [ -s {pid} ] && [ -s {debut} ] && kill -0 $(cat {pid}) 2>/dev/null && "
            f"! grep -qs '^State:[[:space:]]*Z' /proc/$(cat {pid})/status && "
            f"{_meme_identite(f'$(cat {pid})', debut)}; }}")


def commande_detachee(nom: str, commande: str) -> str:
    """P-f : la commande tourne détachée (nouvelle session) ; sa sortie reste sur l'instance ; seules la dernière ligne
    `ETAT` et une ligne `CODE n` sont écrites dans `<nom>.fin`, lu par `commande_sondage`. PID dans `<nom>.pid`.
    C4 : la commande rend `LANCE <pid>` une fois `<nom>.pid` écrit ; elle est idempotente : si `<nom>.fin` existe ou si
    le PID vit déjà, rien n'est relancé (un second essai de lancement ne double jamais une exécution)."""
    d = ETATS_DISTANTS
    interne = (f"( {commande} ) > {d}/{nom}.log 2>&1; c=$?; "  # sous-shell : un `exit` n'empêche pas `.fin`
               f"{{ grep '^ETAT ' {d}/{nom}.log | tail -n 1; echo \"CODE $c\"; }} > {d}/{nom}.tmp; "
               f"mv {d}/{nom}.tmp {d}/{nom}.fin")
    pid, fin, debut = f"{d}/{nom}.pid", f"{d}/{nom}.fin", f"{d}/{nom}.debut"
    return (f"mkdir -p {d} && if [ -e {fin} ] || {_pid_vit(pid, debut)}; then :; "
            f"else setsid nohup bash -c {shlex.quote(interne)} > /dev/null 2>&1 < /dev/null & "
            f"p=$!; echo \"{_identite('$p')}\" > {debut}; echo $p > {pid}; fi; "  # N-4 : identité avant le PID
            f"test -s {pid} && echo \"LANCE $(cat {pid})\"")


def lancement_verifie(sortie: str) -> bool:
    return any(re.fullmatch(r"LANCE \d+", l.strip()) for l in sortie.splitlines())


def commande_sondage(nom: str) -> str:
    """C4 : `.fin` s'il existe ; sinon `VIVANT` si le PID vit (`kill -0`, et non zombie), sinon `.fin` relu (fin entre les deux
    lectures), sinon `MORT` (processus disparu sans écrire son état : coupure de l'hôte)."""
    d = ETATS_DISTANTS
    pid, fin, debut = f"{d}/{nom}.pid", f"{d}/{nom}.fin", f"{d}/{nom}.debut"
    return (f"if [ -e {fin} ]; then cat {fin}; elif {_pid_vit(pid, debut)}; then "
            f"echo VIVANT; elif [ -e {fin} ]; then cat {fin}; else echo MORT; fi")


def lire_sondage(code: int | None, sortie: str) -> str:
    """« fin » (ligne `CODE`), « vivant », « mort », ou « échec » (sondage illisible : `ssh` en échec, rien rendu)."""
    if lire_code(sortie) is not None:
        return "fin"
    lignes = [l.strip() for l in sortie.splitlines() if l.strip()]
    if code == 0 and lignes and lignes[-1] == "VIVANT":
        return "vivant"
    if code == 0 and lignes and lignes[-1] == "MORT":
        return "mort"
    return "échec"


def commande_arret(nom: str, attente_s: float = 10.0) -> str:
    """R10 : arrêt du groupe de processus de la commande par son PID (identifiant), jamais par motif. v5 : le groupe
    n'est visé que si son meneur a l'identité écrite au lancement (N-4) ou n'existe plus (le numéro reste alors tenu
    par le groupe, qui ne peut être que celui de la commande) ; TERM, attente bornée de la fin du groupe, puis KILL
    (C10 : plus aucun membre du groupe après l'arrêt)."""
    d = ETATS_DISTANTS
    pid, debut = f"{d}/{nom}.pid", f"{d}/{nom}.debut"
    tours = max(1, int(float(attente_s) / 0.5))
    return (f"p=$(cat {pid} 2>/dev/null); if [ -n \"$p\" ] && {{ [ ! -e /proc/$p ] || "
            f"{_meme_identite('$p', debut)}; }}; then kill -TERM -- -$p 2>/dev/null; i=0; "
            f"while [ $i -lt {tours} ] && kill -0 -- -$p 2>/dev/null; do sleep 0.5; i=$((i+1)); done; "
            f"kill -0 -- -$p 2>/dev/null && kill -KILL -- -$p 2>/dev/null; fi; true")


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


MORT_SANS_ETAT = "commande distante sans ligne d'état (coupure de l'hôte)"


def normaliser_execution(etat_: dict | None, code: int | None, phase: str,
                         message_defaut: str = "commande distante sans ligne d'état") -> dict:
    """État d'une exécution tel que la liste d'arrêt le lit. Une garde levée par la commande avant l'enfant (dossier
    neuf, configuration effective) ou une commande sans ligne d'état devient une exécution en échec, sans tour. C4 :
    une exécution morte sans `.fin` porte `MORT_SANS_ETAT` ; ses tours complets sont relus par la conduite."""
    if etat_ is not None and "code_retour" in etat_:
        return etat_
    message = (etat_ or {}).get("garde_tombee") or message_defaut
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


def ordre_de_lancement(go_id: str, b: float, c: float, commit_code: str, etiquette: str | None = None) -> dict:
    """Condition 8 : l'ordre cite le GO, B, le taux relevé et DEPOT_URL ; v5 : et l'étiquette de l'instance (C11,
    inventaire R10)."""
    return {"GO_ID": go_id, "B": b, "c": c, "DEPOT_URL": DEPOT_URL, "commit_code": commit_code,
            "etiquette": etiquette, "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


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
    """Arrêt de la liste d'arrêt décidé par la conduite (dépense, échéance, instance injoignable, veilleur mort) :
    consigné au bilan."""


@dataclass
class Conduite:
    """Déroulé complet d'un poste sur une instance. `sortie` : dossier local neuf (bilan, manifestes versionnés,
    transferts scellés, journal des étapes `conduite-v5.jsonl`, état du poste `poste-v5.json`, journal du veilleur
    `arrets-v5.jsonl`). `texte_go` : `registres/go.md` de `origin/main` (`texte_go_main`, P-i), vérifié ici."""
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
    seuil_local_usd: float = SEUIL_LOCAL_USD
    sondages_en_echec_max: int = SONDAGES_EN_ECHEC_MAX
    duree_sans_sondage_max_s: float = DUREE_SANS_SONDAGE_MAX_S
    delai_prete_s: float = DELAI_PRETE_S
    periode_prete_s: float = 15.0
    periode_veilleur_s: float = 30.0
    fournisseur_veilleur: str = "vast"
    lancer_veilleur: object = lancer_veilleur_processus
    arreter_veilleur: object = arreter_veilleur
    veilleur_vivant: object = None  # (pid, journal) -> bool ; défaut : `verifier_veilleur`

    def _etape(self, objet: dict) -> None:
        with open(self.sortie / "conduite-v5.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({**objet, "t": self.horloge()}, ensure_ascii=False, sort_keys=True, default=str) + "\n")

    # --- veilleur (C2) ---
    def _lancer_veilleur(self, echeance: float | None = None) -> None:
        self.pid_veilleur = self.lancer_veilleur(self.poste_fichier, self.ident,
                                                 self.echeance if echeance is None else echeance, self.journal_arrets,
                                                 self.fournisseur_veilleur, self.periode_veilleur_s,
                                                 self.marge_secours)

    def _veilleur_ok(self) -> bool:
        if self.veilleur_vivant is not None:
            return bool(self.veilleur_vivant(self.pid_veilleur, self.journal_arrets))
        return verifier_veilleur(self.pid_veilleur, self.journal_arrets,
                                 fraicheur_s=max(180.0, 4 * float(self.periode_veilleur_s)))

    def _garde_veilleur(self) -> None:
        """C2 : veilleur vivant, sinon une relance ; mort après la relance → arrêt (transfert, destruction)."""
        if self._veilleur_ok():
            return
        self._etape({"veilleur": "non vivant", "pid": self.pid_veilleur})
        if self.pid_veilleur is not None:
            self.arreter_veilleur(self.pid_veilleur)
        self._lancer_veilleur()
        if not self._veilleur_ok():
            raise _Arret("veilleur de secours non vivant, relance comprise : arrêt avant toute autre commande")
        self._etape({"veilleur": "relancé", "pid": self.pid_veilleur})

    # bornes : dépense du poste à B − 2, échéance moins la marge de transfert
    def _borne(self) -> float:
        maintenant = self.horloge()
        reste = (self.b - 2 - self.poste.depense(maintenant)) / self.c * 3600
        return min(maintenant + reste, self.echeance - self.marge_transfert_s)

    def _avant(self, quoi: str) -> None:
        self._garde_veilleur()
        maintenant = self.horloge()
        if self.poste.depense(maintenant) >= self.b - 2:
            raise _Arret(f"dépense du poste ≥ B − 2 avant « {quoi} »")
        if maintenant >= self.echeance - self.marge_transfert_s:
            raise _Arret(f"échéance du GO (moins la marge de transfert) avant « {quoi} »")

    def _relever_taux(self) -> float:
        """C1 : dans le `try` ; trois essais (l'instance peut charger encore) ; l'erreur du dernier sort."""
        for n in range(3):
            try:
                return float(self.fournisseur.taux_horaire(self.ident))
            except Exception:
                if n == 2:
                    raise
                self.attendre(self.periode_prete_s)
        raise AssertionError  # jamais atteint

    def _attendre_prete(self) -> None:
        """C5 : état « running » puis `ssh … true` accepté, borné par `delai_prete_s` ; la dépense court (D)."""
        debut = self.horloge()
        while True:
            self._avant("attente de l'instance prête")
            try:
                statut = self.fournisseur.statut(self.ident)
            except Exception:
                statut = None
            if statut == "running":
                try:
                    code, _ = self.fournisseur.executer(self.ident, "true", 60)
                except Exception:
                    code = None
                if code == 0:
                    self._etape({"instance_prete": True, "attente_s": self.horloge() - debut})
                    return
            if self.horloge() - debut >= self.delai_prete_s:
                raise _Arret("instance non prête dans le délai (état « running » et ssh) : arrêt et destruction")
            self.attendre(self.periode_prete_s)

    def _arreter_en_cours(self, cause: str = "arrêt par la conduite") -> None:
        """R10 et C3 : la commande en cours est arrêtée par son PID ; erreur consignée, jamais levée. v5 (C8) : la
        cause est notée (`arretees`), pour l'état reconstitué de l'exécution avant les empreintes."""
        nom, self.en_cours = self.en_cours, None
        if nom is None:
            return
        self.arretees.setdefault(nom, cause)
        self._arreter_groupe(nom)

    def _arreter_groupe(self, nom: str) -> None:
        try:
            code, _ = self.fournisseur.executer(self.ident, commande_arret(nom), 120)
            self._etape({"commande": nom, "arret_par_pid": code})
        except Exception as err:
            self._etape({"commande": nom, "arret_par_pid": f"{type(err).__name__}"})

    def _lancer(self, nom: str, commande: str) -> None:
        """C4 : lancement détaché vérifié (`LANCE <pid>`) ; un second essai (idempotent), puis arrêt."""
        for essai in (1, 2):
            try:
                code, sortie = self.fournisseur.executer(self.ident, commande_detachee(nom, commande), 120)
            except Exception:
                code, sortie = None, ""
            if code == 0 and lancement_verifie(sortie):
                return
            self._etape({"commande": nom, "lancement": "non vérifié", "essai": essai, "code": code})
            if essai == 1:
                self.attendre(self.periode_sondage_s)
        raise _Arret(f"lancement de « {nom} » non vérifié après deux essais : arrêt")

    def _cmd(self, nom: str, commande: str, executer: bool = False) -> tuple[dict | None, int | None, str]:
        """Lance `commande` détachée sous le nom `nom`, puis la sonde jusqu'à sa fin, sa mort, ou une borne. Rend
        (état, code, issue), issue « fin » ou « mort » (C4). Sondages en échec tolérés (C3) jusqu'à
        `sondages_en_echec_max` consécutifs ou `duree_sans_sondage_max_s` sans réussite : instance injoignable, arrêt.
        Bornes : hors exécution, B − 2 et échéance − marge ; pour une exécution (qui s'arrête elle-même à B − 2 et à
        échéance − marge), échéance − marge/2 et le seuil local `B − seuil_local_usd` (C4)."""
        self._avant(nom)
        self.lances.append(nom)
        self.en_cours = nom
        self._lancer(nom, commande)
        echecs, dernier_ok = 0, self.horloge()
        while True:
            try:
                code, sortie = self.fournisseur.executer(self.ident, commande_sondage(nom), 120)
            except Exception:  # C3 : un sondage qui lève est un sondage en échec
                code, sortie = None, ""
            issue = lire_sondage(code, sortie)
            maintenant = self.horloge()
            if issue == "fin":
                try:
                    e = lire_etat(sortie)
                except (GardeArret, ValueError):
                    e = None
                c = lire_code(sortie)
                self.en_cours = None
                self._etape({"commande": nom, "code": c, "etat": e})
                return e, c, "fin"
            if issue == "mort":
                self.en_cours = None
                self._etape({"commande": nom, "issue": MORT_SANS_ETAT})
                self._arreter_groupe(nom)  # C10 : un membre du groupe peut vivre encore ; avant `tours` et la relance
                return None, None, "mort"
            if issue == "vivant":
                echecs, dernier_ok = 0, maintenant
            else:
                echecs += 1
                self._etape({"commande": nom, "sondage": "échec", "consecutifs": echecs})
                if echecs >= self.sondages_en_echec_max or maintenant - dernier_ok >= self.duree_sans_sondage_max_s:
                    self._arreter_en_cours("instance injoignable")
                    raise _Arret(f"instance injoignable pendant « {nom} » ({echecs} sondages consécutifs en échec) : "
                                 "arrêt par PID tenté, transfert tenté, destruction ; nœud")
            if executer:
                if maintenant >= self.echeance - self.marge_transfert_s / 2:
                    self._arreter_en_cours("échéance du GO")
                    raise _Arret(f"borne d'échéance (échéance du GO moins la moitié de la marge de transfert) "
                                 f"atteinte pendant « {nom} » : arrêt par PID")
                if self.poste.depense(maintenant) >= self.b - self.seuil_local_usd:
                    self._arreter_en_cours("dépense")
                    raise _Arret(f"seuil local de dépense (D ≥ B − {self.seuil_local_usd:g} USD) atteint pendant "
                                 f"« {nom} » : arrêt par PID")
            elif maintenant >= self._borne():
                self._arreter_en_cours("dépense" if self.poste.depense(maintenant) >= self.b - 2 else "échéance du GO")
                raise _Arret(f"borne de dépense ou d'échéance atteinte pendant « {nom} » : arrêt par PID")
            self._garde_veilleur()
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

    def _tours_relus(self, phase: str, cause: str = "coupure de l'hôte") -> dict | None:
        """C4 et C8 : exécution sans état : sur l'instance, l'état absent est écrit (« reconstitué », jamais
        d'écrasement, `cause`), et les tours complets et gardes tombées sont relus, sans note."""
        try:
            _code, sortie = self.fournisseur.executer(self.ident, commande_instance(
                "tours", travail=f"/root/x/{phase}", ecrire_etat=True, phase=phase,
                manifeste=self.manifestes_phase[phase], cause=cause), 600)
            t = lire_etat(sortie)
            r = {"tours_complets": int(t["tours_complets"]), "gardes_tombees": list(t.get("gardes_tombees", [])),
                 "journal_absent": t.get("journal_absent"), "etat_execution": t.get("etat_execution"),
                 "lignes_tronquees_ignorees": list(t.get("lignes_tronquees_ignorees") or [])}
            self._etape({"commande": phase, "etat_reconstitue": r, "cause": cause})
            return r
        except Exception as err:
            self._etape({"commande": phase, "etat_reconstitue": f"échec : {type(err).__name__}", "cause": cause})
            return None

    def _executer(self, phase: str, manifeste: str) -> dict:
        self.manifestes_phase[phase] = manifeste
        e, code, issue = self._cmd(phase, commande_instance(
            "executer", travail=f"/root/x/{phase}", phase=phase, depense=self._depense(), echeance_go=self.echeance,
            marge_transfert=self.marge_transfert_s, manifeste=manifeste, clone="/root/public"), executer=True)
        if issue == "mort":
            r = normaliser_execution(None, None, phase, MORT_SANS_ETAT)
            t = self._tours_relus(phase, "coupure de l'hôte")
            if t is None:
                # M-1 : la reconstitution a échoué ; elle est retentée avant les empreintes (`_finir`)
                self.arretees.setdefault(phase, "coupure de l'hôte")
                r["tours_complets"] = None  # inconnu : aucune relance (la liste exige < 20 tours complets)
            else:
                r["tours_complets"] = t["tours_complets"]
                r["journal_absent"] = t["journal_absent"]
                r["etat_execution"] = t["etat_execution"]
                r["lignes_tronquees_ignorees"] = t["lignes_tronquees_ignorees"]  # v7 (C-2)
                r["gardes_tombees"] += [g for g in t["gardes_tombees"] if g not in r["gardes_tombees"]]
            return r
        return normaliser_execution(e, code, phase)

    def conduire(self) -> dict:
        man = json.loads(Path(self.manifeste_local).read_text(encoding="utf-8"))
        self.b = float(man["B"])
        anterieures = instances_du_poste(self.instances_anterieures, self.b)
        if self.texte_go != texte_go_main(Path(self.depot_local)):
            raise GardeArret("condition 2 (P-i) : le texte de GO passé n'est pas registres/go.md de origin/main")
        go = ligne_go(self.texte_go, self.go_id)
        verifier_go(go, self.b)
        verifier_non_revoque(self.texte_go, self.go_id)
        self.echeance = echeance_epoch(go["echeance"])
        if not float(self.marge_secours) < float(self.seuil_local_usd) < 2:
            raise GardeArret("seuil local de dépense hors de ]B − 2, B − marge de secours[ (C4)")
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
        self.lances: list[str] = []
        self.en_cours: str | None = None
        self.pid_veilleur: int | None = None
        self.c: float | None = None
        self.poste_fichier = self.sortie / "poste-v5.json"
        self.journal_arrets = self.sortie / "arrets-v5.jsonl"
        self.arretees: dict[str, str] = {}
        self.manifestes_phase: dict[str, str] = {}
        self.etiquette = PREFIXE_ETIQUETTE + uuid.uuid4().hex[:16]  # C11 : unique par conduite
        try:
            self.ident = self.fournisseur.creer(self.offre, self.image, self.disque_go, self.etiquette)
        except Exception as err:  # C11 : l'instance peut exister quand même
            self._creation_incertaine(err, sha_archive)
            raise
        self.creation = self.horloge()
        bilan = {"instance": self.ident, "etiquette": self.etiquette, "archive_sha256": sha_archive}
        try:  # C1 : ouvert aussitôt après la création
            self._etape({"instance": self.ident, "creee": self.creation})
            self.c = self._relever_taux()
            self.poste.ajouter(self.ident, self.c, self.creation)
            self.poste.ecrire(self.poste_fichier)
            bilan["d_avant_creation"] = self.poste.d_avant(self.ident, self.creation)
            self._etape({"instance": self.ident, "c": self.c, "archive_sha256": sha_archive,
                         "ordre": ordre_de_lancement(self.go_id, self.b, self.c, man["commit_code"],
                                                     self.etiquette)})
            self._lancer_veilleur()
            self._garde_veilleur()
            verifier_echeance(self.echeance, self.creation, self.b, self.c, self.marge_secours, self.marge_transfert_s)
            self._attendre_prete()
            self._avant("amorce")
            self.fournisseur.envoyer_fichier(self.ident, archive, ARCHIVE_DISTANTE)
            amorce = self.sortie / "amorce-v5.sh"
            amorce.write_text(script_amorce(man, sha_archive), encoding="utf-8")
            self.fournisseur.envoyer_fichier(self.ident, amorce, "/root/amorce-v5.sh")
            envoyer_jeton(self.fournisseur, self.ident)
            e, _, _ = self._cmd("amorce", "bash /root/amorce-v5.sh")
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
            mep, _, _ = self._cmd("mise-en-place", commande_instance(
                "mise-en-place", travail="/root/x/mise-en-place", manifeste="/root/manifeste-v3.json",
                clone=clone, echeance_go=self.echeance, marge_transfert=self.marge_transfert_s, **dep()))
            bilan["mise_en_place"] = mep
            if not mep or "garde_tombee" in mep or "pas_par_tour" not in mep:
                bilan["arret"] = "garde de mise en place tombée : pas de run, pas de verdict ; consigner"
                return bilan
            man = {**man, "pas_par_tour": mep["pas_par_tour"], "longueur_suffixe": mep["longueur_suffixe"],
                   "ecart_10": mep["ecart_10"]}
            m_mep = self._manifeste("mise-en-place", man)
            juge, _, _ = self._cmd("controle-juge", commande_instance(
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
                if issue == ISSUE_LIGNE_COUPEE:  # v8 (A-2) : garde inconnue ; jamais de reprise
                    bilan["pilote"] = pilotes
                    bilan["arret"] = ("pas de run principal ; ligne de garde coupée au pilote (garde inconnue) ; "
                                      "nœud")
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
            regle, _, _ = self._cmd("regle", commande_instance(
                "regle-tours", travail="/root/x/regle", manifeste=m_mep, pilote=f"/root/x/{fixe_t['phase']}", **dep()))
            bilan["regle"] = regle
            if not regle or "K" not in regle:
                bilan["arret"] = "règle du nombre de tours non calculée : arrêt ; nœud"
                return bilan
            if regle["K"] < 20:  # C7 : atteignable (K et la garde au même `ETAT`)
                bilan["arret"] = "K < 20 après le pilote : arrêt, devis révisé à Lazar"
                return bilan
            man = {**man, "regle_tours": {k: regle[k] for k in ("B", "R", "D", "c", "t", "H_heures", "K")}}
            m_regle = self._manifeste("regle", man)
            principal = self._executer("principal", m_regle)
            bilan["principal"] = [principal]
            if principal.get("tours_complets") is None:
                bilan["arret"] = ("exécution principale morte sans état, tours complets illisibles : pas de relance "
                                  "(la liste l'exige sous 20 tours complets) ; nœud")
                return bilan
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
            self._finir(bilan)

    def _finir(self, bilan: dict) -> None:
        """Dans tous les cas : arrêt par PID de la commande en cours (C3), rapatriement, destruction retentée (C1) ;
        destruction en échec sans veilleur vivant → veilleur à échéance immédiate, qui la retente à chaque période."""
        self._arreter_en_cours()
        for nom, cause in self.arretees.items():  # C8 : état reconstitué avant les empreintes
            if nom in EXECUTIONS and nom in self.manifestes_phase:
                bilan.setdefault("etats_reconstitues", {})[nom] = self._tours_relus(nom, cause)
        try:
            self._rapatrier(bilan)
        except Exception as err:  # consigné ; la destruction suit dans tous les cas
            bilan["rapatriement_erreur"] = f"{type(err).__name__}: {err}"[:300]
        detruite, erreurs = False, []
        for n in range(ESSAIS_DESTRUCTION):
            try:
                self.fournisseur.detruire(self.ident)  # R10, par identifiant
                detruite = True
                break
            except Exception as err:
                erreurs.append(f"{type(err).__name__}: {err}"[:300])
                if n < ESSAIS_DESTRUCTION - 1:
                    self.attendre(self.periode_prete_s)
        if erreurs:
            bilan["destruction_erreur"] = erreurs[-1]
            bilan["destruction_essais_en_echec"] = len(erreurs)
        if detruite:
            if self.c is not None:
                self.poste.detruite(self.ident, self.horloge())
                self.poste.ecrire(self.poste_fichier)
            if self.pid_veilleur is not None:
                self.arreter_veilleur(self.pid_veilleur)
        else:  # C9 : toujours un veilleur à échéance 0 (destruction retentée à chaque période), puis l'ancien arrêté
            ancien = self.pid_veilleur
            try:
                self._lancer_veilleur(echeance=0.0)
                bilan["veilleur_de_destruction"] = self.pid_veilleur
                try:
                    neuf_vivant = self._veilleur_ok()
                except Exception:
                    neuf_vivant = False
                if neuf_vivant and ancien is not None and ancien != self.pid_veilleur:
                    self.arreter_veilleur(ancien)
                elif not neuf_vivant:
                    bilan["alerte"] = ("instance non détruite ; veilleur de destruction non vu vivant (l'ancien veilleur "
                                       "est gardé) : vérifier, et arrêt manuel par identifiant (R10)")
            except Exception as err:
                self.pid_veilleur = ancien
                bilan["alerte"] = (f"instance non détruite et aucun veilleur de destruction ({type(err).__name__}) : "
                                   "arrêt manuel par identifiant (R10)")
        if self.c is None:
            bilan["taux_illisible"] = ("dépense de cette instance non comptée (taux illisible) : à relever dans "
                                       "registres/depenses.md")
        bilan["detruite"] = detruite
        bilan["depense"] = self.poste.depense(self.horloge())
        self._etape({"instance": self.ident, "detruite": detruite, "depense": bilan["depense"]})
        sortie_bilan = self.sortie / "bilan-conduite-v5.json"
        sortie_bilan.write_text(json.dumps(bilan, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                                encoding="utf-8")
        scellement.sceller(sortie_bilan)

    def _creation_incertaine(self, err: Exception, sha_archive: str) -> None:
        """C11 (N-5) : `creer` a levé ; l'instance peut exister. Inventaire filtré sur la seule étiquette de cette
        conduite, destruction de ces seuls identifiants (R10) ; sinon alerte au bilan. Bilan écrit et scellé."""
        bilan = {"instance": None, "etiquette": self.etiquette, "archive_sha256": sha_archive,
                 "creation_erreur": f"{type(err).__name__}: {err}"[:300], "detruite": False, "detruites": []}
        try:
            idents = [str(i) for i in self.fournisseur.inventaire(self.etiquette)]
        except Exception as e2:
            idents = None
            bilan["inventaire_erreur"] = f"{type(e2).__name__}"
        bilan["inventaire"] = idents
        echecs = []
        for ident in idents or []:
            for n in range(ESSAIS_DESTRUCTION):
                try:
                    self.fournisseur.detruire(ident)  # R10, par identifiant, étiquette de cette conduite seulement
                    bilan["detruites"].append(ident)
                    break
                except Exception as e3:
                    if n == ESSAIS_DESTRUCTION - 1:
                        echecs.append({"id": ident, "erreur": type(e3).__name__})
                    else:
                        self.attendre(self.periode_prete_s)
        bilan["detruite"] = bool(bilan["detruites"]) and not echecs
        if echecs:
            bilan["destruction_erreur"] = echecs
        if not bilan["detruite"]:
            bilan["alerte"] = (f"création incertaine : inventaire R10 manuel (étiquette « {self.etiquette} »)")
        if bilan["detruites"]:
            bilan["taux_illisible"] = ("dépense de l'instance créée sans réponse non comptée : à relever dans "
                                       "registres/depenses.md")
        self._etape({"creation_incertaine": bilan})
        sortie_bilan = self.sortie / "bilan-conduite-v5.json"
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
    p.add_argument("--battement")  # défaut : <journal>.battement (C2)
    a = p.parse_args(argv)
    v = Veilleur(fournisseur_depuis(a.fournisseur), Path(a.poste), a.instance, a.echeance, Path(a.journal),
                 marge_secours=a.marge, periode_s=a.periode, battement=a.battement)
    v.boucle()
    return 0


if __name__ == "__main__":
    sys.exit(main())
