#!/usr/bin/env python3
"""Amorce du rejeu des activations internes du saboteur à budget, voie (A) — v1 (exécutante v8, GO-2026-11-24-06).

Devis : `docs/notes/rejeu-activations-saboteur-voie-a-v1/devis-passe-activations-saboteur-voie-a-v2.md` (9a4a794c…) ;
3,01 USD attendus, plafond 11,00 USD ; coupure externe tout compris 10,00 USD déclenchée à 9,60 USD ; horloge 4,5 h ;
borne horaire interne de la passe (P9) 7,00 USD. Ce module n'ouvre jamais le code de la passe (côté moniteurs,
`controle_ia.barreau8_moniteurs.passe_recalcul_v5`) : il le lance par la ligne de commande de sa notice d'emploi
(`docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v6.md`) et n'en relève que le code de retour, des
noms, des tailles et des empreintes. Il n'ouvre aucun fichier de scores ni d'activité (`scores-par-action-`,
`scores-par-jeton-`, `activite-brute-`) : il les copie et les empreinte, rien d'autre.

Un seul fichier, bibliothèque standard seulement : il tourne dans la session qui pilote et sur la machine louée, avant
toute installation (`python3 -I -B <ce fichier> <commande>`).

Côté pilote (session) :
- `offres` : filtre bloquant du devis, § 2.3, sur la réponse brute de la recherche d'offres ; choix A100 SXM4 80 Go, repli
  A100 PCIe 80 Go ; aucun choix, aucune création.
- `creer` : garde de l'accord (crochet `.claude/hooks/garde_calcul.py` appelé tel quel, plafond exact 11,00 USD), mot de
  feu exact, ordre de lancement scellé, crédit, aucune machine déjà à l'étiquette ; création par l'outil `vastai` (secrets
  dans les arguments d'un sous-processus, jamais affichés) ; fiche de création écrite (identifiant, heure, prix).
- `surveiller` : garde externe (R10) : horloge 4,5 h depuis la demande de création, dépense tout compris (estimée et lue
  au crédit, la plus haute des deux) coupée à 9,60 USD ; coupure = destruction par l'identifiant, relue deux fois.
- `rapatrier` : clone séparé de la branche de versement, commit attendu, inventaire scellé, chaque fichier à sa taille et à
  son empreinte, chaque compagnon `.sha256` tenu, aucun fichier de trop : attestation `RAPATRIEMENT_VERIFIE=oui|non`.
- `detruire` : par l'identifiant de la fiche de création seulement (R10) ; jamais une intouchable ; étiquette exacte ;
  rapatriement attesté, ou coupure nommée ; absence relue deux fois.
- `inventaire` : instances du compte, champs filtrés (jamais l'environnement des machines).

Côté machine (`machine`, lancé par le script de démarrage) :
minuterie détachée armée en premier (coupe la passe par son PID à l'échéance moins la marge, puis détruit la machine par
son identifiant à l'échéance) ; ordre de lancement lu à son empreinte ; branche de versement neuve exigée ; préparation ;
tirage et assemblage des entrées, vérifiés par leurs compagnons ; garde d'écriture (sonde écrite, relue, retirée ; place
libre) ; vérification des entrées et essai à blanc de la passe (code 0 exigés ; le rapport de l'essai doit nommer les trois
archives d'activité brute, sinon REFUS DE DÉPART) ; arbre propre ; passe (sans aucun secret dans son environnement) ;
garde « activations écrites » ; versement de tout ce qui est récupérable, inventaire scellé, poussé par lots, relu à
distance ; arrêt de la machine (état « stopped »). Un redémarrage du conteneur ne relance rien.

Mode jouet (`--jouet`) : aucune location, aucun réseau ; Vast simulé par un fichier, dépôts locaux, commandes fournies par
l'essai ; mêmes gardes, mêmes chemins de code.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from contextlib import redirect_stderr
from pathlib import Path

VERSION = "rejeu-activations-voie-a-v1"
GO_ATTENDU = "GO-2026-11-24-06"
FEU_ATTENDU = "feu, additif 2 scellé"
PLAFOND_USD = 11.00            # ligne d'accord GO-2026-11-24-06
COUPURE_USD = 10.00            # coupure externe tout compris (devis § 3.4)
DECLENCHEMENT_USD = 9.60       # coupure moins un quart d'heure au pire tarif horaire (0,40 USD)
P9_HORAIRE_MAX_USD = 7.00      # borne passée à la passe (--depense-max-usd), nette de réseau
DUREE_MAX_H = 4.5              # horloge dure, depuis la demande de création
MARGE_VERSEMENT_S = 1800       # la minuterie de la machine coupe la passe 30 min avant l'échéance, pour verser
RESEAU_FORFAIT_USD = 1.5625 + 0.08  # forfait entrant observé + 2 Go sortants à 0,04 USD/Go (devis § 3.3)
PERIODE_SURVEILLANCE_S = 60
ETIQUETTE = "rejeu-activations-voie-a-v1"
IMAGE = "python:3.11-bookworm"  # image de la course de la voie (A)
DISQUE_GO = 100
DEPOT_PRIVE = "https://github.com/lciric/controle-ia-travail.git"  # jamais lciric/controle-ia (copie expurgée publique)
BRANCHE_VERSEMENT = "donnees/passe-activations-voie-a-v1"
API_VAST = "https://console.vast.ai/api/v0"
INTOUCHABLES = frozenset({58936096, 58936099, 58936100, 60988826, 62096662})
SECRETS = ("GH_TOKEN", "HF_TOKEN", "CONTAINER_API_KEY", "VAST_API_KEY")
MOTIFS_PRIVES = ("iib", "ii-b", "consigne-privee", "extrait_cote_moniteurs")  # refusés par la passe dans --sortie, --run-id
PREFIXES_NON_OUVERTS = ("scores-par-action-", "scores-par-jeton-", "activite-brute-")
LOT_POUSSEE_OCTETS = 400_000_000
PLACE_MIN_OCTETS = 3_100_000_000 + 2_000_000_000  # P9 de la passe + livraison entière (marge)
SONDE_ECRITURE_OCTETS = 64_000_000

# Filtre bloquant du devis, § 2.3 (cartes : A100 SXM4 80 Go, repli A100 PCIe 80 Go)
CARTES = ("A100 SXM4", "A100 PCIE")
FILTRE = {
    "dph_total_max": 1.35,            # USD/h
    "storage_cost_max": 0.40,         # USD/Go/mois
    "inet_down_cost_max": 0.04,       # USD/Go
    "inet_up_cost_max": 0.04,         # USD/Go
    "reliability2_min": 0.97,
    "cpu_ram_min_mo": 64_000,
    "cpu_cores_effective_min": 12,
    "gpu_ram_min_mo": 79_000,
    "disk_space_min_go": DISQUE_GO,
    "cuda_max_good_min": 13.0,        # requirements-gpu.txt : roue torch pour CUDA 13.0
}

PLACEHOLDERS = {"CLONE", "CACHE_MODELE", "SORTIE_VERIF", "SORTIE_ESSAI", "SORTIE_PASSE", "RUN_ID_VERIF", "RUN_ID_ESSAI",
                "RUN_ID_PASSE", "DEBUT_LOCATION", "DEBUT_COMMANDE", "IDENTIFIANT_INSTANCE", "PRIX_HORAIRE_USD", "PYTHON"}
A_FIXER = "A_FIXER"
LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2,3})\s*\|")
MONTANT = re.compile(r"^\s*(\d+(?:[.,]\d+)?)\s*USD\b")
RE_SHA = re.compile(r"[0-9a-f]{64}")
RE_COMMIT = re.compile(r"[0-9a-f]{40}")


class Refus(Exception):
    """Une garde n'est pas tenue : on s'arrête, on écrit la cause ; jamais de repli silencieux (R5)."""


# --- Outils communs -----------------------------------------------------------------------------------------------------


def maintenant() -> float:
    return time.time()


def iso(t: float) -> str:
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def ecrire_compagnon(chemin: Path) -> str:
    s = sha256_fichier(chemin)
    Path(str(chemin) + ".sha256").write_text(f"{s}  {chemin.name}\n", encoding="utf-8")
    return s


def compagnon_tenu(compagnon: Path) -> tuple[bool, str]:
    """Forme de `sha256sum -c` : chaque ligne « <empreinte>  <nom> », le nom relatif au dossier du compagnon."""
    try:
        lignes = [x for x in compagnon.read_text(encoding="utf-8").splitlines() if x.strip()]
    except (OSError, UnicodeDecodeError) as e:
        return False, f"{compagnon.name} illisible ({type(e).__name__})"
    if not lignes:
        return False, f"{compagnon.name} vide"
    for ligne in lignes:
        m = re.fullmatch(r"([0-9a-f]{64}) [ *](.+)", ligne)
        if not m:
            return False, f"{compagnon.name} mal formé"
        cible = compagnon.parent / m.group(2)
        if not cible.is_file():
            return False, f"{compagnon.name} : {m.group(2)} absent"
        if sha256_fichier(cible) != m.group(1):
            return False, f"{compagnon.name} : empreinte de {m.group(2)} différente"
    return True, "tenu"


class Journal:
    """Journal daté, valeurs des secrets masquées avant toute écriture ou impression."""

    def __init__(self, chemin: Path, secrets: dict[str, str], echo: bool = True):
        self.chemin, self.echo = Path(chemin), echo
        self.secrets = {k: v for k, v in secrets.items() if v and len(v) >= 6}
        self.chemin.parent.mkdir(parents=True, exist_ok=True)

    def masquer(self, texte: str) -> str:
        for nom, v in self.secrets.items():
            texte = texte.replace(v, f"[{nom} masquée]")
        return texte

    def ecrire(self, texte: str) -> None:
        ligne = self.masquer(f"{iso(maintenant())} {texte}")
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(ligne + "\n")
        if self.echo:
            print(ligne, flush=True)


def lancer(cmd, cwd=None, env=None, delai=900, sortie=None) -> int:
    """Commande sans shell ; sortie et erreurs vers un fichier (jamais à l'écran) ; code de retour, 124 au délai."""
    try:
        if sortie is None:
            r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, timeout=delai)
            return r.returncode
        with open(sortie, "ab") as f:
            r = subprocess.run(cmd, cwd=cwd, env=env, stdout=f, stderr=subprocess.STDOUT, timeout=delai)
        return r.returncode
    except subprocess.TimeoutExpired:
        return 124
    except OSError:
        return 127


def env_git(gh_token: str) -> dict:
    return {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.environ.get("HOME", "/root"), "GH_TOKEN": gh_token,
            "GIT_TERMINAL_PROMPT": "0", "LANG": "C.UTF-8"}


AIDE_GIT = ["-c", 'credential.helper=!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f']


def git(args: list[str], cwd=None, gh_token="", delai=1800) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", *AIDE_GIT, *args], cwd=cwd, env=env_git(gh_token), capture_output=True,
                              timeout=delai)
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(["git", *args], 124, b"", b"delai")


# --- Accord (garde du dépôt appelée telle quelle) -------------------------------------------------------------------------


def charger_garde(chemin_garde: Path, chemin_registre: Path):
    spec = importlib.util.spec_from_file_location("garde_calcul_rejeu", chemin_garde)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.REGISTRE_GO = Path(chemin_registre)
    return mod


def verifier_go(chemin_registre: Path, chemin_garde: Path, go_id: str, aujourd_hui: dt.date) -> dict:
    """Accord de calcul valide selon le crochet du dépôt (type « calcul », Lazar, validité, révocation), plafond exact."""
    if go_id != GO_ATTENDU:
        raise Refus(f"accord {go_id} : le devis v2 et l'ordre nomment {GO_ATTENDU}, aucun autre")
    garde = charger_garde(chemin_garde, chemin_registre)
    tampon = io.StringIO()
    try:
        with redirect_stderr(tampon):
            garde.decider(f"GO_ID={go_id} vastai create instance 0", aujourd_hui)
    except SystemExit as e:
        if e.code not in (0, None):
            raise Refus(f"crochet du dépôt : {tampon.getvalue().strip()}") from None
    lignes = []
    for ligne in Path(chemin_registre).read_text(encoding="utf-8").splitlines():
        m = LIGNE_GO.match(ligne)
        if m and m.group(1) == go_id:
            lignes.append([c.strip() for c in ligne.strip().strip("|").split("|")])
    if not lignes:
        raise Refus(f"{go_id} absent du registre")
    for cellules in lignes:
        m = MONTANT.match(cellules[4])
        if not m or abs(float(m.group(1).replace(",", ".")) - PLAFOND_USD) > 1e-9:
            raise Refus(f"{go_id} : plafond « {cellules[4]} » au lieu de exactement {PLAFOND_USD:.2f} USD")
    return {"go": go_id, "lignes": len(lignes), "registre_sha256": sha256_fichier(Path(chemin_registre))}


# --- Offres (filtre bloquant, devis § 2.3) ------------------------------------------------------------------------------


def _nombre(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def motifs_offre(o: dict) -> list[str]:
    """Liste des bornes non tenues (vide : offre conforme). Champ absent ou non numérique = borne non tenue."""
    f, m = FILTRE, []
    if o.get("gpu_name") not in CARTES:
        m.append(f"carte {o.get('gpu_name')!r} hors de {CARTES}")
    if o.get("num_gpus") != 1:
        m.append(f"num_gpus {o.get('num_gpus')!r} ≠ 1")
    if o.get("verification") != "verified":
        m.append("offre non vérifiée")
    if o.get("is_bid") is not False:
        m.append("offre interruptible ou type inconnu (à la demande exigée)")
    bornes = (("gpu_ram", ">=", f["gpu_ram_min_mo"]), ("dph_total", "<=", f["dph_total_max"]),
              ("storage_cost", "<=", f["storage_cost_max"]), ("inet_down_cost", "<=", f["inet_down_cost_max"]),
              ("inet_up_cost", "<=", f["inet_up_cost_max"]), ("reliability2", ">=", f["reliability2_min"]),
              ("cpu_ram", ">=", f["cpu_ram_min_mo"]), ("cpu_cores_effective", ">=", f["cpu_cores_effective_min"]),
              ("disk_space", ">=", f["disk_space_min_go"]), ("cuda_max_good", ">=", f["cuda_max_good_min"]))
    for champ, sens, borne in bornes:
        v = o.get(champ)
        if not _nombre(v) or (sens == "<=" and not (0 <= v <= borne)) or (sens == ">=" and v < borne):
            m.append(f"{champ} = {v!r} (borne {sens} {borne})")
    return m


def prix_horaire_total(o: dict) -> float:
    """Carte + stockage de 100 Go à l'heure (stockage USD/Go/mois × 100 / 720) ; majoration prudente (8 Go déjà comptés)."""
    return float(o["dph_total"]) + float(o["storage_cost"]) * DISQUE_GO / 720.0


def choisir_offre(offres: list[dict]) -> dict:
    """La moins chère des A100 SXM4 80 Go conformes ; à défaut, la moins chère des A100 PCIe 80 Go conformes ; sinon refus."""
    conformes = [o for o in offres if isinstance(o, dict) and not motifs_offre(o)]
    for carte in CARTES:
        c = sorted((o for o in conformes if o["gpu_name"] == carte), key=lambda o: (prix_horaire_total(o), o.get("id")))
        if c:
            return c[0]
    raise Refus(f"aucune offre ne passe le filtre bloquant du devis § 2.3 ({len(offres)} offre(s) vue(s)) : rien ne se crée")


# --- Décision de la surveillance externe (R10) -----------------------------------------------------------------------------


def decision_surveillance(creation_demandee: float, t: float, prix_h: float, credit_avant: float | None,
                          credit_maintenant: float | None) -> dict:
    """POURSUIVRE ou COUPER (horloge, dépense). Dépense tout compris = max(estimée, lue au crédit)."""
    if not (_nombre(prix_h) and prix_h > 0):
        return {"decision": "COUPER", "raison": f"prix horaire illisible {prix_h!r}", "depense": None, "heures": None}
    heures = max(0.0, (t - creation_demandee) / 3600.0)
    estimee = heures * prix_h + RESEAU_FORFAIT_USD
    lue = None
    if _nombre(credit_avant) and _nombre(credit_maintenant):
        lue = max(0.0, credit_avant - credit_maintenant)
    depense = max(estimee, lue) if lue is not None else estimee
    d = {"heures": round(heures, 4), "depense_estimee": round(estimee, 4), "depense_lue": None if lue is None else
         round(lue, 4), "depense": round(depense, 4)}
    if heures >= DUREE_MAX_H:
        return {**d, "decision": "COUPER", "raison": f"horloge {heures:.3f} h ≥ {DUREE_MAX_H} h"}
    if depense >= DECLENCHEMENT_USD:
        return {**d, "decision": "COUPER", "raison": f"dépense {depense:.2f} USD ≥ {DECLENCHEMENT_USD:.2f} USD"}
    return {**d, "decision": "POURSUIVRE", "raison": ""}


# --- Clients de Vast -----------------------------------------------------------------------------------------------------


def champs_filtres(instance: dict) -> dict:
    """Inventaire sans fuite : jamais `extra_env`, `onstart`, ni rien qui porte l'environnement de la machine."""
    garder = ("id", "label", "actual_status", "cur_state", "intended_status", "dph_total", "gpu_name", "start_date",
              "etat")
    return {k: instance.get(k) for k in garder if k in instance}


class ClientVastRest:
    """Interface REST de Vast (clé du compte côté session, clé d'instance côté machine) ; la clé n'est jamais affichée."""

    def __init__(self, cle: str):
        if not cle:
            raise Refus("clé de l'interface de Vast absente")
        self._cle = cle

    def _requete(self, methode: str, chemin: str, corps: dict | None = None) -> dict:
        donnees = None if corps is None else json.dumps(corps).encode("utf-8")
        r = urllib.request.Request(f"{API_VAST}{chemin}", data=donnees, method=methode,
                                   headers={"Authorization": f"Bearer {self._cle}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(r, timeout=60) as rep:
                return json.loads(rep.read().decode("utf-8") or "{}")
        except urllib.error.HTTPError as e:
            raise Refus(f"Vast {methode} {chemin} : HTTP {e.code}") from None
        except (urllib.error.URLError, OSError, ValueError) as e:
            raise Refus(f"Vast {methode} {chemin} : {type(e).__name__}") from None

    def instances(self) -> list[dict]:
        return self._requete("GET", "/instances/").get("instances", [])

    def credit(self) -> float | None:
        v = self._requete("GET", "/users/current/").get("credit")
        return float(v) if _nombre(v) else None

    def detruire(self, ident: int) -> None:
        self._requete("DELETE", f"/instances/{int(ident)}/")

    def arreter(self, ident: int) -> None:
        self._requete("PUT", f"/instances/{int(ident)}/", {"state": "stopped"})


class ClientVastCli(ClientVastRest):
    """Côté session : création par l'outil `vastai` (forme éprouvée des amorces du dépôt), le reste par REST."""

    def __init__(self, cle: str, outil: str):
        super().__init__(cle)
        self.outil = outil

    def creer(self, offre_id: int, corps: dict, secrets: dict[str, str]) -> int:
        env = " ".join(f"-e {k}={v}" for k, v in corps["env"].items())
        if any(c.isspace() or c in "\"'" for v in corps["env"].values() for c in v):
            raise Refus("valeur d'environnement avec espace ou guillemet : refus (forme -e K=V)")
        args = [self.outil, "create", "instance", str(int(offre_id)), "--raw", "--image", corps["image"], "--disk",
                str(corps["disk"]), "--cancel-unavail", "--label", corps["label"], "--env", env, "--entrypoint", "bash",
                "--args", "-c", corps["script"]]
        try:
            r = subprocess.run(args, capture_output=True, timeout=300,
                               env={**os.environ, "VAST_API_KEY": self._cle})
        except subprocess.TimeoutExpired:
            raise Refus("création : délai dépassé ; vérifier par l'inventaire avant toute nouvelle location") from None
        texte = (r.stdout + r.stderr).decode("utf-8", "replace")
        for nom, v in secrets.items():
            if v:
                texte = texte.replace(v, f"[{nom} masquée]")
        if r.returncode != 0:
            raise Refus(f"création : code {r.returncode} : {texte[-300:]}")
        rep = None
        for ligne in reversed(texte.strip().splitlines()):
            try:
                rep = json.loads(ligne)
                break
            except ValueError:
                continue
        if not isinstance(rep, dict) or not rep.get("success") or not isinstance(rep.get("new_contract"), int):
            raise Refus("réponse de création illisible ou refusée : vérifier par l'inventaire avant toute nouvelle location")
        return rep["new_contract"]


class ClientVastJouet:
    """Vast simulé dans un fichier JSON (mode jouet) : aucune location, aucun réseau. Garde les gestes, jamais de valeur."""

    def __init__(self, chemin: Path, credit: float = 20.0):
        self.chemin = Path(chemin)
        if not self.chemin.exists():
            self._ecrire({"instances": [], "gestes": [], "credit": credit})

    def _lire(self):
        return json.loads(self.chemin.read_text())

    def _ecrire(self, e):
        tmp = self.chemin.with_suffix(".tmp")
        tmp.write_text(json.dumps(e, ensure_ascii=False, indent=1))
        os.replace(tmp, self.chemin)

    def ajouter(self, ident: int, label: str, statut: str = "running") -> None:
        e = self._lire()
        e["instances"].append({"id": ident, "label": label, "actual_status": statut})
        self._ecrire(e)

    def creer(self, offre_id, corps, secrets=None):
        e = self._lire()
        ident = 90000000 + len(e["gestes"]) + 1
        e["instances"].append({"id": ident, "label": corps.get("label"), "actual_status": "running",
                               "env": sorted(corps.get("env", {}))})
        e["gestes"].append(["creer", ident, offre_id])
        self._ecrire(e)
        return ident

    def instances(self):
        return self._lire()["instances"]

    def credit(self):
        return self._lire().get("credit")

    def detruire(self, ident):
        e = self._lire()
        e["gestes"].append(["detruire", int(ident)])
        e["instances"] = [i for i in e["instances"] if i["id"] != int(ident)]
        self._ecrire(e)

    def arreter(self, ident):
        e = self._lire()
        e["gestes"].append(["arreter", int(ident)])
        for i in e["instances"]:
            if i["id"] == int(ident):
                i["actual_status"] = "stopped"
        self._ecrire(e)


# --- Destruction par l'identifiant (R10) ---------------------------------------------------------------------------------

RAISONS_DESTRUCTION = ("rapatriement-verifie", "coupure-horloge", "coupure-depense", "refus-depart", "machine-arretee-en-echec")


def detruire(client, ident: int, fiche: dict, raison: str, attestation: Path | None, journal: Journal,
             attente_s: float = 10.0) -> dict:
    """Détruit la seule machine de la fiche de création, par son identifiant ; refuse tout le reste. Absence relue deux fois."""
    if raison not in RAISONS_DESTRUCTION:
        raise Refus(f"raison {raison!r} hors de la liste fermée {RAISONS_DESTRUCTION}")
    if not isinstance(ident, int) or isinstance(ident, bool):
        raise Refus("identifiant non entier")
    if ident in INTOUCHABLES:
        raise Refus(f"instance {ident} intouchable : aucun geste")
    if fiche.get("identifiant") != ident:
        raise Refus(f"instance {ident} absente de la fiche de création ({fiche.get('identifiant')!r}) : pas la mienne")
    if raison == "rapatriement-verifie":
        if attestation is None or not attestation.is_file():
            raise Refus("rapatriement non attesté : aucune destruction (sauf coupure nommée)")
        texte = attestation.read_text(encoding="utf-8")
        if "RAPATRIEMENT_VERIFIE=oui" not in texte.splitlines() or f"instance={ident}" not in texte.splitlines():
            raise Refus("attestation sans « RAPATRIEMENT_VERIFIE=oui » ni « instance=<id> » : aucune destruction")
    avant = [champs_filtres(i) for i in client.instances()]
    moi = [i for i in avant if i.get("id") == ident]
    if not moi:
        journal.ecrire(f"destruction : instance {ident} déjà absente de l'inventaire (rien à faire)")
        return {"identifiant": ident, "etat": "absente", "relectures": 0}
    if moi[0].get("label") != fiche.get("etiquette"):
        raise Refus(f"étiquette {moi[0].get('label')!r} ≠ {fiche.get('etiquette')!r} : aucun geste")
    autres_avant = sorted(i["id"] for i in avant if i.get("id") != ident)
    journal.ecrire(f"destruction demandée de l'instance {ident} (raison : {raison})")
    client.detruire(ident)
    relectures = 0
    for k in range(6):
        if k:
            time.sleep(attente_s)
        apres = [champs_filtres(i) for i in client.instances()]
        present = any(i.get("id") == ident for i in apres)
        autres = sorted(i["id"] for i in apres if i.get("id") != ident)
        journal.ecrire(f"relecture {k + 1}/6 : instance {ident} {'présente' if present else 'absente'} ; "
                       f"autres instances {'inchangées' if set(autres) >= set(autres_avant) else 'MANQUANTES'}")
        if not present:
            relectures += 1
            if relectures >= 2:
                return {"identifiant": ident, "etat": "detruite", "relectures": relectures}
        else:
            relectures = 0
    raise Refus(f"instance {ident} encore présente après six relectures : ALARME, vérifier à la main")


# --- Ordre de lancement (scellé, rempli par le côté moniteurs et la mère après l'additif 2) ---------------------------


def _placeholders(texte: str) -> set[str]:
    return set(re.findall(r"\{([A-Z_]+)\}", texte))


def _valeur_option(argv: list[str], option: str) -> str | None:
    if argv.count(option) > 1:
        raise Refus(f"option {option} répétée")
    if option in argv:
        i = argv.index(option)
        return argv[i + 1] if i + 1 < len(argv) else None
    return None


def lire_ordre(chemin: Path, sha_attendu: str) -> dict:
    """Ordre de lancement à son empreinte ; forme fermée ; aucune valeur « A_FIXER » ; bornes du devis tenues."""
    if not RE_SHA.fullmatch(sha_attendu or ""):
        raise Refus("empreinte de l'ordre : 64 caractères hexadécimaux exigés")
    lu = sha256_fichier(chemin)
    if lu != sha_attendu:
        raise Refus(f"empreinte de l'ordre {lu} ≠ {sha_attendu}")
    brut = chemin.read_text(encoding="utf-8")
    if A_FIXER in brut:
        raise Refus("ordre encore à remplir (valeur « A_FIXER ») : rien ne part")

    def sans_doublon(paires):
        d = {}
        for k, v in paires:
            if k in d:
                raise Refus(f"clé répétée {k!r} dans l'ordre")
            d[k] = v
        return d

    o = json.loads(brut, object_pairs_hook=sans_doublon)
    cles = {"version", "go", "branche_versement", "preparation", "tirages", "verifier_entrees", "essai_a_blanc", "passe",
            "livraison_attendue"}
    if set(o) != cles:
        raise Refus(f"clés de l'ordre {sorted(o)} ≠ {sorted(cles)}")
    if o["version"] != "ordre-rejeu-activations-voie-a-v1" or o["go"] != GO_ATTENDU:
        raise Refus("version ou accord de l'ordre inattendus")
    if not o["branche_versement"].startswith("donnees/") or not re.fullmatch(r"[a-z0-9/._-]+", o["branche_versement"]):
        raise Refus("branche de versement : « donnees/… » exigée (branche isolée, jamais main)")
    commandes = [*(p["argv"] for p in o["preparation"]), o["verifier_entrees"]["argv"], o["essai_a_blanc"]["argv"],
                 o["passe"]["argv"]]
    for argv in commandes:
        if not isinstance(argv, list) or not argv or not all(isinstance(a, str) for a in argv):
            raise Refus("chaque commande est une liste non vide de chaînes (aucun shell)")
        inconnus = set().union(*(_placeholders(a) for a in argv)) - PLACEHOLDERS
        if inconnus:
            raise Refus(f"marques inconnues dans une commande : {sorted(inconnus)}")
    for p in [*o["preparation"], o["verifier_entrees"], o["essai_a_blanc"], o["passe"]]:
        if not (_nombre(p.get("delai_s")) and 0 < p["delai_s"] <= DUREE_MAX_H * 3600):
            raise Refus("délai de commande absent ou au-delà de l'horloge")
    passe = o["passe"]["argv"]
    attendues = {"--sortie": "{SORTIE_PASSE}", "--run-id": "{RUN_ID_PASSE}", "--debut-location": "{DEBUT_LOCATION}",
                 "--identifiant-instance": "{IDENTIFIANT_INSTANCE}", "--prix-horaire-usd": "{PRIX_HORAIRE_USD}",
                 "--appareil": "cuda"}
    for opt, val in attendues.items():
        if _valeur_option(passe, opt) != val:
            raise Refus(f"passe : {opt} doit valoir {val}")
    if "passe" not in passe:
        raise Refus("passe : action « passe » absente")
    try:
        dep = float(_valeur_option(passe, "--depense-max-usd"))
        duree = float(_valeur_option(passe, "--duree-max-heures"))
    except (TypeError, ValueError):
        raise Refus("passe : --depense-max-usd et --duree-max-heures numériques exigés") from None
    if not (0 < dep <= P9_HORAIRE_MAX_USD) or not (0 < duree <= DUREE_MAX_H):
        raise Refus(f"passe : bornes P9 {dep} USD / {duree} h au-delà de {P9_HORAIRE_MAX_USD} USD / {DUREE_MAX_H} h")
    for nom, argv, sortie, run in (("vérification", o["verifier_entrees"]["argv"], "{SORTIE_VERIF}", "{RUN_ID_VERIF}"),
                                   ("essai à blanc", o["essai_a_blanc"]["argv"], "{SORTIE_ESSAI}", "{RUN_ID_ESSAI}")):
        if _valeur_option(argv, "--sortie") != sortie or _valeur_option(argv, "--run-id") != run:
            raise Refus(f"{nom} : --sortie {sortie} et --run-id {run} exigés")
        if _valeur_option(argv, "--debut-location") != "{DEBUT_COMMANDE}":
            raise Refus(f"{nom} : --debut-location {{DEBUT_COMMANDE}} exigé (heure du lancement de la commande)")
    if not isinstance(o["essai_a_blanc"].get("rapport"), str) or "/" in o["essai_a_blanc"]["rapport"]:
        raise Refus("essai à blanc : nom du rapport exigé")
    la = o["livraison_attendue"]
    if set(la) != {"sous_dossier", "archives", "fichiers"}:
        raise Refus("livraison attendue : clés sous_dossier, archives, fichiers exigées")
    for c in ("c7", "c15", "c23"):
        if not any(a.startswith(f"activite-brute-{c}-") and a.endswith(".npz") for a in la["archives"]):
            raise Refus(f"livraison attendue : archive d'activité brute de la couche {c} absente de la liste")
    for t in o["tirages"]:
        if set(t) != {"branche", "fichiers", "assembler", "verifier"}:
            raise Refus("tirage : clés branche, fichiers, assembler, verifier exigées")
        for p in [*t["fichiers"], *t["verifier"], *(a["cible"] for a in t["assembler"])]:
            if p.startswith("/") or ".." in Path(p).parts:
                raise Refus(f"tirage : chemin {p!r} hors du dépôt")
    return o


def remplir(argv: list[str], valeurs: dict[str, str]) -> list[str]:
    out = []
    for a in argv:
        for k in _placeholders(a):
            if k not in valeurs:
                raise Refus(f"marque {k} sans valeur")
            a = a.replace("{" + k + "}", valeurs[k])
        out.append(a)
    return out


# --- Gardes de la machine ------------------------------------------------------------------------------------------------


def garde_ecriture(dossier: Path, place_min: int = PLACE_MIN_OCTETS, taille_sonde: int = SONDE_ECRITURE_OCTETS) -> list[str]:
    """Sonde écrite, synchronisée, relue à son empreinte, retirée ; place libre. Liste des motifs (vide : tenue)."""
    motifs = []
    try:
        dossier.mkdir(parents=True, exist_ok=True)
        sonde = dossier / ".sonde-ecriture-rejeu"
        bloc = hashlib.sha256(b"sonde").digest() * (1 << 15)  # 1 Mo
        h = hashlib.sha256()
        with open(sonde, "wb") as f:
            ecrit = 0
            while ecrit < taille_sonde:
                b = bloc[: min(len(bloc), taille_sonde - ecrit)]
                f.write(b)
                h.update(b)
                ecrit += len(b)
            f.flush()
            os.fsync(f.fileno())
        if sonde.stat().st_size != taille_sonde or sha256_fichier(sonde) != h.hexdigest():
            motifs.append("sonde d'écriture relue différente")
        sonde.unlink()
    except OSError as e:
        motifs.append(f"écriture impossible dans {dossier} ({type(e).__name__})")
        return motifs
    libre = shutil.disk_usage(dossier).free
    if libre < place_min:
        motifs.append(f"place libre {libre} octets < {place_min}")
    return motifs


def _chaines(x):
    if isinstance(x, dict):
        for k, v in x.items():
            yield str(k)
            yield from _chaines(v)
    elif isinstance(x, list):
        for v in x:
            yield from _chaines(v)
    elif isinstance(x, str):
        yield x


def garde_rapport_essai(rapport: Path, archives: list[str]) -> list[str]:
    """Le rapport de l'essai à blanc (aucun score) existe, son compagnon tient, et il nomme chaque archive d'activité brute."""
    if not rapport.is_file():
        return [f"rapport de l'essai à blanc absent ({rapport.name})"]
    comp = Path(str(rapport) + ".sha256")
    if comp.is_file():
        ok, m = compagnon_tenu(comp)
        if not ok:
            return [f"rapport de l'essai à blanc : {m}"]
    try:
        contenu = json.loads(rapport.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return [f"rapport de l'essai à blanc illisible ({type(e).__name__})"]
    vues = " ".join(_chaines(contenu))
    return [f"l'essai à blanc n'a pas écrit {a}" for a in archives if a.startswith("activite-brute-") and a not in vues]


def garde_activations(sortie: Path, code: int, attendu: dict) -> list[str]:
    """Livraison complète et activations écrites : noms, tailles, compagnons ; aucun fichier de scores ouvert. Vide : tenue."""
    motifs = []
    if code != 0:
        motifs.append(f"passe sortie en code {code}")
    liv = sortie / attendu["sous_dossier"]
    if (liv / "trace-arret-passe-barreau8-v1.json").exists() or (sortie / "trace-arret-passe-barreau8-v1.json").exists():
        motifs.append("trace d'arrêt présente")
    if not liv.is_dir():
        return motifs + [f"dossier de livraison {attendu['sous_dossier']} absent"]
    for a in attendu["archives"]:
        desc = liv / f"{a}.morceaux.json"
        if not desc.is_file():
            motifs.append(f"{a} : description des morceaux absente")
            continue
        ok, m = compagnon_tenu(Path(str(desc) + ".sha256")) if Path(str(desc) + ".sha256").is_file() else (False,
                                                                                                         "compagnon absent")
        if not ok:
            motifs.append(f"{a}.morceaux.json : {m}")
            continue
        try:  # la description ne porte que des noms, des tailles et des empreintes (notice v6)
            d = json.loads(desc.read_text(encoding="utf-8"))
            morceaux = d["morceaux"]
            total = int(d["taille"])
        except (OSError, ValueError, KeyError, TypeError) as e:
            motifs.append(f"{a}.morceaux.json illisible ({type(e).__name__})")
            continue
        if not morceaux or total <= 0:
            motifs.append(f"{a} : aucun morceau, taille {total}")
            continue
        somme = 0
        for mc in morceaux:
            f = liv / str(mc.get("nom", ""))
            if not f.is_file() or not str(mc.get("nom", "")).startswith(a + ".morceau-"):
                motifs.append(f"{a} : morceau {mc.get('nom')!r} absent")
                continue
            if f.stat().st_size != mc.get("taille"):
                motifs.append(f"{a} : morceau {f.name} de taille différente")
            c = Path(str(f) + ".sha256")
            ok, m = compagnon_tenu(c) if c.is_file() else (False, "compagnon absent")
            if not ok:
                motifs.append(f"{a} : {m}")
            somme += f.stat().st_size
        if somme != total:
            motifs.append(f"{a} : somme des morceaux {somme} ≠ {total}")
    for nom in attendu["fichiers"]:
        f = liv / nom
        c = Path(str(f) + ".sha256")
        if not f.is_file():
            motifs.append(f"{nom} absent")
        elif not c.is_file():
            motifs.append(f"{nom} : compagnon absent")
        else:
            ok, m = compagnon_tenu(c)
            if not ok:
                motifs.append(m)
    return motifs


def arbre_propre(clone: Path) -> list[str]:
    r = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=clone, capture_output=True)
    if r.returncode != 0:
        return ["git status impossible"]
    sales = [x for x in r.stdout.decode("utf-8", "replace").splitlines() if x.strip()]
    return [f"arbre de travail non propre ({len(sales)} entrée(s))"] if sales else []


def secret_dans(fichier: Path, secrets: dict[str, str]) -> bool:
    valeurs = [v.encode() for v in secrets.values() if v and len(v) >= 6]
    if not valeurs:
        return False
    with open(fichier, "rb") as f:
        reste = b""
        for bloc in iter(lambda: f.read(1 << 20), b""):
            fen = reste + bloc
            if any(v in fen for v in valeurs):
                return True
            reste = fen[-max(len(v) for v in valeurs):]
    return False


# --- Machine -------------------------------------------------------------------------------------------------------------


class Machine:
    """Partie machine. Toutes les valeurs qui diffèrent entre la vraie machine et le jouet passent par `reglages`."""

    def __init__(self, reglages: dict):
        self.r = reglages
        self.travail = Path(reglages["travail"])
        self.travail.mkdir(parents=True, exist_ok=True)
        self.clone = Path(reglages["clone"])
        self.secrets = {k: os.environ.get(k, "") for k in SECRETS}
        self.j = Journal(self.travail / "journal-machine.txt", self.secrets, echo=not reglages.get("jouet"))
        self.collecte = self.travail / "collecte"
        self.journaux = self.collecte / "journaux-commandes"
        self.journaux.mkdir(parents=True, exist_ok=True)
        self.ident = reglages["identifiant_instance"]
        self.etat = "EN COURS"

    # client de la machine elle-même (clé d'instance, jamais affichée) ou jouet
    def client(self):
        if self.r.get("vast_jouet"):
            return ClientVastJouet(Path(self.r["vast_jouet"]))
        return ClientVastRest(os.environ.get("CONTAINER_API_KEY", ""))

    def env_sans_secret(self) -> dict:
        env = {k: v for k, v in os.environ.items() if k not in SECRETS and not k.startswith("CONTAINER_")}
        env.update({"PYTHONPATH": "src", "HF_HUB_OFFLINE": "1",  # forme de la notice : PYTHONPATH=src, depuis la racine "TRANSFORMERS_OFFLINE": "1",
                    "PYTHONDONTWRITEBYTECODE": "1"})
        return env

    def armer_minuterie(self) -> int:
        cmd = [sys.executable, "-I", "-B", str(Path(__file__).resolve()), "minuterie", "--travail", str(self.travail),
               "--echeance", str(self.r["echeance_utc_s"]), "--marge-s", str(self.r["marge_s"]),
               "--identifiant", str(self.ident), "--pas-s", str(self.r.get("pas_minuterie_s", 5))]
        if self.r.get("vast_jouet"):
            cmd += ["--vast-jouet", str(self.r["vast_jouet"])]
        p = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                             start_new_session=True, env={**os.environ})
        (self.travail / "minuterie.pid").write_text(f"{p.pid}\n")
        self.j.ecrire(f"minuterie armée : PID {p.pid}, coupure de la passe à {iso(self.r['echeance_utc_s'] - self.r['marge_s'])}, "
                      f"destruction par l'identifiant {self.ident} à {iso(self.r['echeance_utc_s'])}")
        return p.pid

    def commande(self, nom: str, argv: list[str], delai: float, env: dict, cwd: Path) -> int:
        self.j.ecrire(f"{nom} : lancée")
        code = lancer(argv, cwd=cwd, env=env, delai=delai, sortie=self.journaux / f"{nom}.txt")
        self.j.ecrire(f"{nom} : code {code}")
        return code

    def tirer(self, t: dict) -> list[str]:
        """Entrées d'une branche du dépôt : `git fetch` à refspec explicite, `git show` vers le chemin, assemblage, compagnons."""
        br = t["branche"]
        r = git(["fetch", "-q", "origin", f"+refs/heads/{br}:refs/remotes/origin/{br}"], cwd=self.clone,
                gh_token=self.secrets["GH_TOKEN"])
        if r.returncode != 0:
            return [f"tirage de {br} : fetch code {r.returncode}"]
        for p in t["fichiers"]:
            dest = self.clone / p
            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "wb") as f:
                q = subprocess.run(["git", "show", f"refs/remotes/origin/{br}:{p}"], cwd=self.clone, stdout=f,
                                   stderr=subprocess.DEVNULL)
            if q.returncode != 0:
                return [f"tirage de {br} : {p} absent"]
        for a in t["assembler"]:
            cible = self.clone / a["cible"]
            with open(cible, "wb") as f:
                for m in a["morceaux"]:
                    with open(self.clone / m, "rb") as g:
                        shutil.copyfileobj(g, f)
        motifs = []
        for c in t["verifier"]:
            ok, m = compagnon_tenu(self.clone / c)
            if not ok:
                motifs.append(f"tirage de {br} : {m}")
        return motifs

    def verser(self, motif: str) -> str | None:
        """Tout ce qui est récupérable, inventaire scellé, branche neuve, poussée par lots, relue à distance. Une fois seulement."""
        verrou = self.travail / "versement.verrou"
        try:
            fd = os.open(verrou, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f"{os.getpid()} {motif}\n".encode())
            os.close(fd)
        except FileExistsError:
            self.j.ecrire(f"versement déjà engagé (verrou) : rien de plus ({motif})")
            return None
        ordre = self.r.get("ordre") or {"branche_versement": f"{BRANCHE_VERSEMENT}-ordre-refuse-{int(maintenant())}"}
        racine_v = self.travail / "versement-git"
        if racine_v.exists():
            shutil.rmtree(racine_v)  # dossier de travail du versement seulement (jamais une sortie de la passe)
        dest = racine_v / "versement" / self.r["etiquette_course"]
        dest.mkdir(parents=True)
        # 1. ce qui est récupérable : sorties des trois commandes de la passe, runs/ et diag/ de leurs noms, journaux
        sources = []  # (liste de sources possibles, cible) : copiées si présentes ; « absent » si aucune ne l'est
        for cle, nom in (("SORTIE_VERIF", "sortie-verification"), ("SORTIE_ESSAI", "sortie-essai-a-blanc"),
                         ("SORTIE_PASSE", "sortie-passe")):
            sources.append(([Path(self.r["valeurs"][cle])], dest / nom))
        for cle in ("RUN_ID_VERIF", "RUN_ID_ESSAI", "RUN_ID_PASSE"):
            rid = self.r["valeurs"][cle]
            for base in ("runs", "diag"):
                sources.append(([self.clone / base / rid, self.collecte / base / rid], dest / base / rid))
        sources.append(([self.journaux], dest / "journaux-commandes"))
        manquants = []
        for srcs, cible in sources:
            presentes = [s for s in srcs if s.is_dir()]
            for src in presentes:
                shutil.copytree(src, cible, dirs_exist_ok=True, symlinks=False)
            if not presentes:
                manquants.append(str(cible.relative_to(dest)))
        self.j.ecrire(f"versement ({motif}) : chemins absents (non produits) : {sorted(set(manquants))}")
        shutil.copy2(self.j.chemin, dest / "journal-machine.txt")
        # 2. garde des secrets à 0 (les fichiers de scores et d'activité ne sont jamais ouverts : la passe n'a vu aucun secret)
        retires = []
        for f in sorted(p for p in dest.rglob("*") if p.is_file()):
            if f.name.startswith(PREFIXES_NON_OUVERTS):
                continue
            if secret_dans(f, self.secrets):
                f.unlink()
                retires.append(str(f.relative_to(dest)))
        if retires:
            self.j.ecrire(f"ALARME : {len(retires)} fichier(s) portant un secret retirés du versement : {retires}")
            shutil.copy2(self.j.chemin, dest / "journal-machine.txt")
        # 3. inventaire scellé : noms, tailles, empreintes (aucun contenu lu au-delà du hachage)
        fichiers = sorted(p for p in dest.rglob("*") if p.is_file())
        inv = {"version": VERSION, "motif": motif, "etat": self.etat, "instance": self.ident,
               "fichiers": [{"chemin": str(p.relative_to(dest)), "taille": p.stat().st_size, "sha256": sha256_fichier(p)}
                            for p in fichiers]}
        p_inv = dest / "inventaire-versement-v1.json"
        p_inv.write_text(json.dumps(inv, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        ecrire_compagnon(p_inv)
        # 4. branche neuve, lots, poussée, relecture distante
        gh = self.secrets["GH_TOKEN"]
        br = ordre["branche_versement"]
        for args in (["init", "-q"], ["checkout", "-q", "--orphan", br], ["config", "user.name", "executante-rejeu"],
                     ["config", "user.email", "executante-rejeu@invalid"], ["remote", "add", "origin", self.r["depot_url"]]):
            if git(args, cwd=racine_v, gh_token=gh).returncode != 0:
                self.j.ecrire(f"VERSEMENT IMPOSSIBLE : git {args[0]}")
                return None
        tous = sorted(p for p in (racine_v / "versement").rglob("*") if p.is_file())
        tous = [p for p in tous if p.name not in ("inventaire-versement-v1.json", "inventaire-versement-v1.json.sha256")] + \
               [p_inv, Path(str(p_inv) + ".sha256")]
        lots, lot, taille = [], [], 0
        for p in tous:
            s = p.stat().st_size
            if lot and taille + s > LOT_POUSSEE_OCTETS:
                lots.append(lot)
                lot, taille = [], 0
            lot.append(p)
            taille += s
        if lot:
            lots.append(lot)
        for k, lot in enumerate(lots, 1):
            rel = [str(p.relative_to(racine_v)) for p in lot]
            if git(["add", "-f", "--", *rel], cwd=racine_v, gh_token=gh).returncode != 0 or \
                    git(["commit", "-q", "-m", f"Rejeu des activations voie (A) : versement {k}/{len(lots)} ({motif})"],
                        cwd=racine_v, gh_token=gh).returncode != 0:
                self.j.ecrire(f"VERSEMENT IMPOSSIBLE : commit du lot {k}")
                return None
            pousse = False
            for essai in range(5):
                if git(["push", "-q", "origin", f"HEAD:refs/heads/{br}"], cwd=racine_v, gh_token=gh).returncode == 0:
                    pousse = True
                    break
                time.sleep(self.r.get("attente_poussee_s", 2) * (2 ** essai))
            if not pousse:
                self.j.ecrire(f"VERSEMENT IMPOSSIBLE : poussée du lot {k} refusée après cinq essais")
                return None
        tete = git(["rev-parse", "HEAD"], cwd=racine_v).stdout.decode().strip()
        r = git(["ls-remote", "origin", f"refs/heads/{br}"], cwd=racine_v, gh_token=gh)
        distant = r.stdout.decode().split()[0] if r.returncode == 0 and r.stdout.strip() else ""
        if distant != tete:
            self.j.ecrire(f"VERSEMENT NON VÉRIFIÉ : tête distante {distant or 'absente'} ≠ {tete}")
            return None
        self.j.ecrire(f"VERSEMENT POUSSÉ commit={tete} branche={br} fichiers={len(inv['fichiers'])} "
                      f"inventaire={sha256_fichier(p_inv)} lots={len(lots)}")
        return tete

    def arreter_machine(self, motif: str) -> None:
        try:
            self.client().arreter(self.ident)
            self.j.ecrire(f"ARRÊT DEMANDÉ (état « stopped ») : {motif}")
        except Refus as e:
            self.j.ecrire(f"ALARME : arrêt de la machine refusé ({e}) ; la minuterie et la surveillance externe restent")

    def finir(self, etat: str, motif: str) -> int:
        self.etat = etat
        self.j.ecrire(f"ÉTAT {etat} : {motif}")
        commit = self.verser(etat)
        self.j.ecrire(f"FIN etat={etat} versement={'oui commit=' + commit if commit else 'NON'}")
        if not self.r.get("ne_pas_arreter"):
            self.arreter_machine(etat)
        return 0 if etat == "LIVRAISON VERSÉE" and commit else 1

    def executer(self) -> int:
        r, j = self.r, self.j
        # 0. un redémarrage du conteneur ne relance rien
        compteur = self.travail / "demarrages.txt"
        n = int(compteur.read_text().strip() or 0) if compteur.is_file() else 0
        compteur.write_text(f"{n + 1}\n")
        if n >= 1:
            j.ecrire(f"REDÉMARRAGE {n + 1} : rien n'est relancé ; versement de l'état tel quel")
            return self.finir("INTERROMPUE (redémarrage)", "redémarrage du conteneur")
        # 1. minuterie en tout premier
        self.armer_minuterie()
        try:
            ordre = lire_ordre(Path(r["ordre_chemin"]), r["ordre_sha256"])
        except (Refus, OSError, ValueError, KeyError, TypeError) as e:
            return self.finir("REFUS DE DÉPART", f"ordre : {e}")
        self.r["ordre"] = ordre
        br = ordre["branche_versement"]
        q = git(["ls-remote", r["depot_url"], f"refs/heads/{br}"], gh_token=self.secrets["GH_TOKEN"])
        if q.returncode != 0 or q.stdout.strip():
            self.r["ordre"] = {**ordre, "branche_versement": br + "-refus-" + str(int(maintenant()))}
            return self.finir("REFUS DE DÉPART", f"branche de versement {br} déjà présente ou illisible (R12 : nom neuf)")
        v = r["valeurs"]
        env_prep = {**os.environ, "HF_TOKEN": self.secrets["HF_TOKEN"]}
        # 2. préparation, tirages
        for p in ordre["preparation"]:  # la préparation voit HF_TOKEN (téléchargement du modèle) ; la passe ne voit aucun secret
            if self.commande(f"preparation-{p['nom']}", remplir(p["argv"], v), p["delai_s"], env_prep, self.clone) != 0:
                return self.finir("REFUS DE DÉPART", f"préparation {p['nom']} en échec")
        for t in ordre["tirages"]:
            motifs = self.tirer(t)
            if motifs:
                return self.finir("REFUS DE DÉPART", "; ".join(motifs))
        if self.coupe():
            return self.finir("COUPURE À L'ÉCHÉANCE", "avant la vérification des entrées")
        # 3. garde d'écriture et place libre, puis vérification des entrées et essai à blanc
        motifs = garde_ecriture(Path(v["SORTIE_PASSE"]).parent, r.get("place_min", PLACE_MIN_OCTETS),
                                r.get("taille_sonde", SONDE_ECRITURE_OCTETS))
        if motifs:
            return self.finir("REFUS DE DÉPART", "garde d'écriture : " + "; ".join(motifs))
        env_passe = self.env_sans_secret()
        v["DEBUT_COMMANDE"] = iso(maintenant() - 1)
        if self.commande("verifier-entrees", remplir(ordre["verifier_entrees"]["argv"], v),
                         ordre["verifier_entrees"]["delai_s"], env_passe, self.clone) != 0:
            return self.finir("REFUS DE DÉPART", "vérification des entrées en échec")
        v["DEBUT_COMMANDE"] = iso(maintenant() - 1)
        if self.commande("essai-a-blanc", remplir(ordre["essai_a_blanc"]["argv"], v), ordre["essai_a_blanc"]["delai_s"],
                         env_passe, self.clone) != 0:
            return self.finir("REFUS DE DÉPART", "essai à blanc en échec")
        motifs = garde_rapport_essai(Path(v["SORTIE_ESSAI"]) / ordre["essai_a_blanc"]["rapport"],
                                     ordre["livraison_attendue"]["archives"])
        if motifs:
            return self.finir("REFUS DE DÉPART", "les activations ne s'écrivent pas : " + "; ".join(motifs))
        # runs/ et diag/ de l'essai et de la vérification déplacés hors du dépôt (rien n'est supprimé), puis arbre propre
        for cle in ("RUN_ID_VERIF", "RUN_ID_ESSAI"):
            for base in ("runs", "diag"):
                src = self.clone / base / v[cle]
                if src.exists():
                    (self.collecte / base).mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), str(self.collecte / base / v[cle]))
        motifs = arbre_propre(self.clone)
        if motifs:
            return self.finir("REFUS DE DÉPART", "; ".join(motifs))
        if self.coupe():
            return self.finir("COUPURE À L'ÉCHÉANCE", "avant la passe")
        # 4. passe, sans secret dans son environnement ; PID consigné pour la minuterie
        j.ecrire("passe : lancée")
        with open(self.journaux / "passe.txt", "ab") as f:
            p = subprocess.Popen(remplir(ordre["passe"]["argv"], v), cwd=self.clone, env=env_passe, stdout=f,
                                 stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            (self.travail / "passe.pid").write_text(f"{p.pid}\n")
            try:
                code = p.wait(timeout=ordre["passe"]["delai_s"])
            except subprocess.TimeoutExpired:
                os.kill(p.pid, signal.SIGTERM)
                try:
                    code = p.wait(timeout=60)
                except subprocess.TimeoutExpired:
                    os.kill(p.pid, signal.SIGKILL)
                    code = p.wait()
                j.ecrire(f"passe : délai de l'ordre dépassé, arrêtée par son PID {p.pid}")
        j.ecrire(f"passe : code {code}")
        # 5. garde « activations écrites »
        motifs = garde_activations(Path(v["SORTIE_PASSE"]), code, ordre["livraison_attendue"])
        if self.coupe():
            return self.finir("COUPURE À L'ÉCHÉANCE", f"passe arrêtée par la minuterie (code {code})")
        if motifs:
            return self.finir("ACTIVATIONS NON ÉCRITES" if code == 0 else "PASSE ARRÊTÉE", "; ".join(motifs))
        return self.finir("LIVRAISON VERSÉE", "livraison complète, activations des couches 7, 15 et 23 écrites")

    def coupe(self) -> bool:
        return (self.travail / "coupure-echeance").exists()


def minuterie(travail: Path, echeance: float, marge_s: float, ident: int, pas_s: float, client) -> int:
    """Processus détaché : à l'échéance moins la marge, coupe la passe par son PID ; à l'échéance, détruit la machine."""
    j = Journal(travail / "minuterie.txt", {}, echo=False)
    j.ecrire(f"minuterie {os.getpid()} : coupure à {iso(echeance - marge_s)}, destruction à {iso(echeance)}, instance {ident}")
    coupee = False
    while maintenant() < echeance:
        if not coupee and maintenant() >= echeance - marge_s:
            (travail / "coupure-echeance").write_text(iso(maintenant()) + "\n")
            coupee = True
            pid_f = travail / "passe.pid"
            if pid_f.is_file():
                pid = int(pid_f.read_text().strip())
                try:
                    os.kill(pid, signal.SIGTERM)
                    j.ecrire(f"COUPURE : passe signalée par son PID {pid} (SIGTERM)")
                    fin_attente = maintenant() + 60
                    while maintenant() < fin_attente:
                        time.sleep(0.5)
                        os.kill(pid, 0)
                    os.kill(pid, signal.SIGKILL)
                    j.ecrire(f"COUPURE : passe {pid} encore vivante, SIGKILL par son PID")
                except ProcessLookupError:
                    j.ecrire(f"COUPURE : passe {pid} finie")
            else:
                j.ecrire("COUPURE : passe non lancée")
        time.sleep(pas_s)
    j.ecrire(f"ÉCHÉANCE : destruction de l'instance {ident} par son identifiant")
    for essai in range(10):
        try:
            client.detruire(ident)
            j.ecrire(f"destruction demandée (essai {essai + 1}) : réponse reçue")
            return 0
        except Refus as e:
            j.ecrire(f"destruction refusée (essai {essai + 1}) : {e}")
            time.sleep(min(30, pas_s * 6))
    j.ecrire("ALARME : destruction non obtenue par la minuterie ; la surveillance externe reste")
    return 4


# --- Partie session : création, surveillance, rapatriement -----------------------------------------------------------------


def script_de_demarrage(commit: str, ordre_rel: str, ordre_sha: str) -> str:
    """Processus principal du conteneur : clone au commit de lancement, puis la partie machine de ce module (au premier plan)."""
    if not RE_COMMIT.fullmatch(commit) or not RE_SHA.fullmatch(ordre_sha):
        raise Refus("commit (40) et empreinte de l'ordre (64) en hexadécimal exigés")
    if not re.fullmatch(r"[A-Za-z0-9/._-]+", ordre_rel) or ".." in ordre_rel:
        raise Refus("chemin de l'ordre : caractères simples, relatif au dépôt")
    return ("set -u; cd /root; "
            "if [ ! -d /root/depot/.git ]; then "
            "A='!f() { echo username=x-access-token; echo \"password=${GH_TOKEN}\"; }; f'; "
            "git -c credential.helper=\"$A\" clone -q \"$DEPOT_URL\" /root/depot && "
            f"git -C /root/depot checkout -q --detach {commit}; fi; "
            "python3 -I -B /root/depot/src/controle_ia/rejeu_activations_voie_a_v1.py machine "
            f"--clone /root/depot --travail /root/rejeu --ordre /root/depot/{ordre_rel} --ordre-sha256 {ordre_sha} "
            "2>&1 | tee -a /root/rejeu-amorce.log; sleep infinity")


def creer(a, client=None, aujourd_hui=None) -> int:
    t = Path(a.fiche)
    j = Journal(Path(str(t) + ".journal"), {k: os.environ.get(k, "") for k in SECRETS})
    try:
        if t.exists():
            raise Refus(f"fiche {t} déjà présente : une création par fiche (R12)")
        if a.feu != FEU_ATTENDU:
            raise Refus(f"mot de feu {a.feu!r} ≠ « {FEU_ATTENDU} » : rien ne se crée")
        if os.environ.get("GO_ID") != a.go:
            raise Refus("GO_ID de l'environnement absent ou différent de l'accord cité")
        g = verifier_go(Path(a.registre), Path(a.garde), a.go, aujourd_hui or dt.datetime.now(dt.timezone.utc).date())
        j.ecrire(f"accord {g['go']} accepté par le crochet du dépôt ; plafond {PLAFOND_USD:.2f} USD ; registre {g['registre_sha256']}")
        lire_ordre(Path(a.ordre), a.ordre_sha256)
        j.ecrire(f"ordre {a.ordre} à son empreinte {a.ordre_sha256}")
        offres = json.loads(Path(a.offres).read_text(encoding="utf-8"))
        offres = offres.get("offers", offres) if isinstance(offres, dict) else offres
        o = choisir_offre(offres)
        prix_h = prix_horaire_total(o)
        j.ecrire(f"offre {o['id']} retenue ({o['gpu_name']}, {o['dph_total']:.4f} USD/h, stockage {o['storage_cost']:.3f} "
                 f"USD/Go/mois, total {prix_h:.4f} USD/h)")
        client = client or ClientVastCli(os.environ.get("VAST_API_KEY", ""), a.outil)
        a_moi = [i for i in client.instances() if i.get("label") == ETIQUETTE]
        if a_moi:
            raise Refus(f"une instance porte déjà l'étiquette {ETIQUETTE} ({[i.get('id') for i in a_moi]}) : aucune autre")
        credit = client.credit()
        if not _nombre(credit) or credit < PLAFOND_USD:
            raise Refus(f"crédit {credit!r} USD < plafond {PLAFOND_USD:.2f} USD")
        secrets = {k: os.environ.get(k, "") for k in ("GH_TOKEN", "HF_TOKEN")}
        if not all(secrets.values()):
            raise Refus("GH_TOKEN ou HF_TOKEN absent de l'environnement")
        demande = maintenant()
        echeance = int(demande + DUREE_MAX_H * 3600)
        env = {"DEPOT_URL": DEPOT_PRIVE, "GO_ID": a.go, "ECHEANCE_UTC_S": str(echeance), "CREATION_DEMANDEE_UTC": iso(demande),
               "PRIX_HORAIRE_USD": f"{prix_h:.6f}", **secrets}
        b64 = base64.b64encode(script_de_demarrage(a.commit, a.ordre_rel, a.ordre_sha256).encode()).decode("ascii")
        corps = {"image": IMAGE, "disk": DISQUE_GO, "label": ETIQUETTE, "env": env,
                 "script": f"echo {b64} | base64 -d > /root/demarrage-rejeu.sh && bash /root/demarrage-rejeu.sh"}
        if a.verifier_seulement:
            j.ecrire("vérification seulement : rien créé (variables : " + ", ".join(sorted(env)) + ")")
            return 0
        ident = client.creer(o["id"], corps, secrets)
        fiche = {"identifiant": ident, "etiquette": ETIQUETTE, "offre": o["id"], "carte": o["gpu_name"],
                 "creation_demandee_utc": iso(demande), "creation_demandee_s": demande, "echeance_utc_s": echeance,
                 "prix_horaire_usd": prix_h, "credit_avant": credit, "go": a.go, "commit": a.commit,
                 "ordre_sha256": a.ordre_sha256}
        t.write_text(json.dumps(fiche, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        j.ecrire(f"MACHINE CRÉÉE : identifiant {ident} ; échéance {iso(echeance)} ; fiche {t}")
        return 0
    except (Refus, OSError, ValueError, KeyError, TypeError) as e:
        j.ecrire(f"REFUS : {e}")
        return 2


def surveiller(fiche: dict, client, journal: Journal, periode_s: float = PERIODE_SURVEILLANCE_S,
               tours_max: int | None = None, attente_destruction_s: float = 10.0) -> dict:
    """Boucle externe (R10) : POURSUIVRE ou COUPER ; coupure = destruction par l'identifiant ; fin quand l'instance est absente."""
    ident, tours = fiche["identifiant"], 0
    while tours_max is None or tours < tours_max:
        tours += 1
        try:
            inst = [champs_filtres(i) for i in client.instances() if i.get("id") == ident]
            credit = client.credit()
        except Refus as e:
            journal.ecrire(f"relevé impossible ({e}) ; nouvel essai")
            time.sleep(periode_s)
            continue
        if not inst:
            journal.ecrire(f"instance {ident} absente : surveillance finie")
            return {"fin": "absente", "tours": tours}
        d = decision_surveillance(fiche["creation_demandee_s"], maintenant(), fiche["prix_horaire_usd"],
                                  fiche.get("credit_avant"), credit)
        journal.ecrire(f"{d['decision']} statut={inst[0].get('actual_status')} heures={d['heures']} "
                       f"depense={d['depense']} (estimée {d.get('depense_estimee')}, lue {d.get('depense_lue')}) {d['raison']}")
        if d["decision"] == "COUPER":
            raison = "coupure-horloge" if "horloge" in d["raison"] else "coupure-depense"
            r = detruire(client, ident, fiche, raison, None, journal, attente_destruction_s)
            return {"fin": "coupee", "raison": d["raison"], "destruction": r, "tours": tours}
        time.sleep(periode_s)
    return {"fin": "tours", "tours": tours}


def rapatrier(depot_url: str, branche: str, dossier: Path, commit_attendu: str | None, ident: int,
              journal: Journal, gh_token: str = "") -> dict:
    """Clone séparé de la branche ; commit ; inventaire scellé ; chaque fichier à sa taille et à son empreinte ; compagnons ;
    aucun fichier de trop. Aucun fichier de scores n'est ouvert au-delà du hachage. Écrit l'attestation."""
    if dossier.exists():
        raise Refus(f"dossier de rapatriement {dossier} déjà présent (dossier neuf exigé)")
    r = git(["clone", "-q", "--single-branch", "--branch", branche, depot_url, str(dossier)], gh_token=gh_token)
    motifs, n_ok, n = [], 0, 0
    if r.returncode != 0:
        motifs.append(f"clone de {branche} : code {r.returncode}")
        tete = ""
    else:
        tete = git(["rev-parse", "HEAD"], cwd=dossier).stdout.decode().strip()
        if commit_attendu and tete != commit_attendu:
            motifs.append(f"commit distant {tete} ≠ commit annoncé {commit_attendu}")
        invs = sorted(dossier.glob("versement/*/inventaire-versement-v1.json"))
        if len(invs) != 1:
            motifs.append(f"{len(invs)} inventaire(s) au lieu d'un")
        else:
            p_inv = invs[0]
            base = p_inv.parent
            ok, m = compagnon_tenu(Path(str(p_inv) + ".sha256"))
            if not ok:
                motifs.append(f"inventaire : {m}")
            inv = json.loads(p_inv.read_text(encoding="utf-8"))
            if inv.get("instance") != ident:
                motifs.append(f"inventaire de l'instance {inv.get('instance')!r}, pas {ident}")
            attendus = {e["chemin"]: e for e in inv["fichiers"]}
            n = len(attendus)
            for chemin, e in sorted(attendus.items()):
                f = base / chemin
                if not f.is_file():
                    motifs.append(f"{chemin} absent")
                elif f.stat().st_size != e["taille"] or sha256_fichier(f) != e["sha256"]:
                    motifs.append(f"{chemin} : taille ou empreinte différente")
                else:
                    n_ok += 1
            presents = {str(p.relative_to(base)) for p in base.rglob("*") if p.is_file()}
            de_trop = presents - set(attendus) - {"inventaire-versement-v1.json", "inventaire-versement-v1.json.sha256"}
            hors = {str(p.relative_to(dossier)) for p in dossier.rglob("*") if p.is_file() and ".git" not in p.parts
                    and base not in p.parents}
            if de_trop or hors:
                motifs.append(f"fichiers hors inventaire : {sorted(de_trop | hors)[:5]}")
            for c in sorted(base.rglob("*.sha256")):
                ok, m = compagnon_tenu(c)
                if not ok:
                    motifs.append(f"compagnon {c.relative_to(base)} : {m}")
    verifie = not motifs
    att = dossier.parent / f"attestation-rapatriement-{ident}.txt"
    att.write_text("\n".join([f"RAPATRIEMENT_VERIFIE={'oui' if verifie else 'non'}", f"instance={ident}",
                              f"branche={branche}", f"commit={tete}", f"fichiers={n_ok}/{n}", f"heure={iso(maintenant())}",
                              *[f"motif={m}" for m in motifs[:50]]]) + "\n", encoding="utf-8")
    journal.ecrire(f"rapatriement : {'VÉRIFIÉ' if verifie else 'NON VÉRIFIÉ'} ; commit {tete} ; {n_ok}/{n} fichiers ; "
                   f"{len(motifs)} motif(s)")
    return {"verifie": verifie, "commit": tete, "fichiers": f"{n_ok}/{n}", "motifs": motifs, "attestation": str(att)}


# --- Ligne de commande ---------------------------------------------------------------------------------------------------


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    s = p.add_subparsers(dest="cmd", required=True)
    c = s.add_parser("offres")
    c.add_argument("--offres", required=True)
    c = s.add_parser("creer")
    for k in ("--fiche", "--feu", "--go", "--registre", "--garde", "--ordre", "--ordre-rel", "--ordre-sha256", "--offres",
              "--commit"):
        c.add_argument(k, required=True)
    c.add_argument("--outil", default="vastai")
    c.add_argument("--verifier-seulement", action="store_true")
    c.add_argument("--jouet")
    c = s.add_parser("surveiller")
    c.add_argument("--fiche", required=True)
    c.add_argument("--periode-s", type=float, default=PERIODE_SURVEILLANCE_S)
    c.add_argument("--jouet")
    c = s.add_parser("rapatrier")
    for k in ("--fiche", "--branche", "--dossier"):
        c.add_argument(k, required=True)
    c.add_argument("--depot-url", default=DEPOT_PRIVE)
    c.add_argument("--commit-attendu")
    c = s.add_parser("detruire")
    c.add_argument("--fiche", required=True)
    c.add_argument("--identifiant", type=int, required=True)
    c.add_argument("--raison", required=True, choices=RAISONS_DESTRUCTION)
    c.add_argument("--attestation")
    c.add_argument("--jouet")
    c = s.add_parser("inventaire")
    c = s.add_parser("machine")
    for k in ("--clone", "--travail", "--ordre", "--ordre-sha256"):
        c.add_argument(k, required=True)
    c = s.add_parser("minuterie")
    c.add_argument("--travail", required=True)
    c.add_argument("--echeance", type=float, required=True)
    c.add_argument("--marge-s", type=float, required=True)
    c.add_argument("--identifiant", type=int, required=True)
    c.add_argument("--pas-s", type=float, default=5)
    c.add_argument("--vast-jouet")
    a = p.parse_args(argv)

    def client_session(jouet):
        return ClientVastJouet(Path(jouet)) if jouet else ClientVastRest(os.environ.get("VAST_API_KEY", ""))

    try:
        if a.cmd == "offres":
            d = json.loads(Path(a.offres).read_text(encoding="utf-8"))
            offres = d.get("offers", d) if isinstance(d, dict) else d
            for o in offres:
                m = motifs_offre(o)
                print(f"{o.get('id')} {o.get('gpu_name')} {'CONFORME' if not m else 'REJETÉE : ' + '; '.join(m)}")
            o = choisir_offre(offres)
            print(f"CHOIX {o['id']} {o['gpu_name']} {prix_horaire_total(o):.4f} USD/h")
            return 0
        if a.cmd == "creer":
            return creer(a, ClientVastJouet(Path(a.jouet)) if a.jouet else None)
        if a.cmd in ("surveiller", "detruire", "rapatrier"):
            fiche = json.loads(Path(a.fiche).read_text(encoding="utf-8"))
            j = Journal(Path(a.fiche).with_suffix(f".{a.cmd}.txt"), {k: os.environ.get(k, "") for k in SECRETS})
            if a.cmd == "surveiller":
                r = surveiller(fiche, client_session(a.jouet), j, a.periode_s)
            elif a.cmd == "detruire":
                r = detruire(client_session(a.jouet), a.identifiant, fiche, a.raison,
                             Path(a.attestation) if a.attestation else None, j)
            else:
                r = rapatrier(a.depot_url, a.branche, Path(a.dossier), a.commit_attendu, fiche["identifiant"], j,
                              os.environ.get("GH_TOKEN", ""))
                print(json.dumps({k: r[k] for k in ("verifie", "commit", "fichiers")}, ensure_ascii=False))
                return 0 if r["verifie"] else 1
            print(json.dumps(r, ensure_ascii=False))
            return 0
        if a.cmd == "inventaire":
            for i in ClientVastRest(os.environ.get("VAST_API_KEY", "")).instances():
                print(json.dumps(champs_filtres(i), ensure_ascii=False))
            return 0
        if a.cmd == "minuterie":
            client = ClientVastJouet(Path(a.vast_jouet)) if a.vast_jouet else \
                ClientVastRest(os.environ.get("CONTAINER_API_KEY", ""))
            return minuterie(Path(a.travail), a.echeance, a.marge_s, a.identifiant, a.pas_s, client)
        if a.cmd == "machine":
            ident = os.environ.get("CONTAINER_ID", "")
            if not ident.isdigit():
                print("REFUS : identifiant d'instance illisible (CONTAINER_ID)")
                return 3
            ech = int(os.environ["ECHEANCE_UTC_S"])
            stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
            valeurs = {"CLONE": a.clone, "CACHE_MODELE": "/root/cache-modele", "PYTHON": f"{a.clone}/.venv/bin/python",
                       "SORTIE_VERIF": f"/root/sorties/{stamp}-verification", "SORTIE_ESSAI": f"/root/sorties/{stamp}-essai",
                       "SORTIE_PASSE": f"/root/sorties/{stamp}-passe", "RUN_ID_VERIF": f"{stamp}-verification-barreau8",
                       "RUN_ID_ESSAI": f"{stamp}-essai-a-blanc-barreau8", "RUN_ID_PASSE": f"{stamp}-passe-barreau8",
                       "DEBUT_LOCATION": os.environ["CREATION_DEMANDEE_UTC"], "IDENTIFIANT_INSTANCE": ident,
                       "PRIX_HORAIRE_USD": os.environ["PRIX_HORAIRE_USD"]}
            m = Machine({"travail": a.travail, "clone": a.clone, "ordre_chemin": a.ordre, "ordre_sha256": a.ordre_sha256,
                         "identifiant_instance": int(ident), "echeance_utc_s": ech, "marge_s": MARGE_VERSEMENT_S,
                         "depot_url": os.environ.get("DEPOT_URL", DEPOT_PRIVE), "valeurs": valeurs,
                         "etiquette_course": stamp + "-rejeu-activations-voie-a"})
            return m.executer()
    except (Refus, OSError, ValueError, KeyError) as e:
        print(f"REFUS : {e}")
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
