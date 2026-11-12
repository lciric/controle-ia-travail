"""Création liée au devis, garde-fous de destruction hors du processus de la session (A13, R10) — essai Lean, v7.

v7 (R-2415, liste de Lazar après le premier essai, rapport `rapport-poste-local-d1a-v1.md`). Copie de `minuterie_v6.py`
(inchangé, R12), avec seulement :
- **source SSH en réseau** (accordé par Lazar) : `acces-creer` et `acces-couper` prennent `--prefixe-poste P` (32 par défaut,
  24 au plus large ; tout autre préfixe est refusé) ; la source des règles est le réseau `IP_POSTE/P`. Règle sortante de
  coupure inchangée.
- **`adresses-sortie`** : mesure préalable (section 0) du nombre d'adresses par lesquelles le poste sort, par un service qui
  renvoie l'adresse vue ; ne rend que des comptes et le préfixe conseillé (32 si une seule adresse, celle du poste ; 24 si
  toutes sont dans le /24 du poste) ; code 1 si une adresse sort du /24 ou si rien n'a répondu. Jamais une adresse écrite.
- **`garde-poste`** contrôle aussi le /24 du poste (toute adresse `a.b.c.x` du même /24).
- `MODULE`, `FORMAT` et les messages portent `minuterie_v7`.

Texte de la v6 :
Création liée au devis, garde-fous de destruction hors du processus de la session (A13, R10) — essai Lean, v6.

Contre-lecture courte des points machine de la v5 (`897b7438…`, décision R-2333). La v5 reste telle quelle (R12). Montage :
le serveur est loué depuis l'ordinateur de Lazar par une session locale ; la mère, dans le nuage, a l'interface de Hetzner.
Corrections v6 :
- CLC5-01 : le contrôle de survie ne conclut « morte » que par `Popen.poll()` du processus lancé, ou après des lectures
  négatives répétées jusqu'au délai (120 s) ; jamais sur une seule lecture de `/proc/PID/cmdline` vide (course de l'`exec`).
- CLC5-03 : une seconde préparation, ou une création avec un autre fichier `rattrapage-machine-d1a-*` dans le dossier versé,
  est refusée, même sans journal des créations.
- CLC5-07 : aucune donnée du poste de Lazar dans un fichier versé ou poussé. Ni son adresse IPv4 (le fichier d'accès ne la
  porte plus ; elle ne passe qu'en argument, en mémoire), ni le commentaire de sa clé publique, ni ses chemins (sorties en
  chemins relatifs au clone, messages et traces masqués). `garde-poste` refuse un index git qui porte l'adresse du poste,
  son dossier personnel ou le chemin du clone ; `verifier-coupure` masque les adresses des règles.
- CLC5-06 : essais neufs pour m01, m09, m10, m11 et m15 de la contre-lecture.
- Notes : `acces-couper` relit le nom du pare-feu ; `fichier_pousse` lit la branche distante par `git ls-remote` ; la mère
  donne l'empreinte du fichier de rattrapage qu'elle a lu (`--empreinte-mere`, comparée avant tout appel) ; clé SSH et
  pare-feu pris dans le fichier d'accès poussé ; trois tâches de la mère (rappel dans sa session à H, sessions neuves à
  H + 30 min et H + 24 h), messages autosuffisants avec les formes `curl` ; ligne « en tâche jusqu'à » pour
  `registres/etat.md` ; `detruire` et `inventaire` bornés en temps en ligne de commande (code 5) ; `adresse-serveur` en
  lecture seule.
Codes de sortie : 0 fait ; 1 arrêt ; 2 usage ; 3 destruction refusée durablement (à la main, par l'identifiant) ; 4 rattrapage
à refaire ; 5 panne passagère plus longue que la borne (refaire dans 15 minutes, puis prévenir Lazar).
"""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import os
import re
import subprocess
import sys
import time
import traceback
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from controle_ia.gardes import GardeArret

from . import garde_go_v1
from .hetzner_v5 import (ETIQUETTE_CREATION, NOM_MACHINE, TYPES_PERMIS, ClientHetzner5, CreationRefusee, ErreurHetzner,
                         RefusDurable, creation_du_serveur, lieu_du_serveur, regles_coupure, regles_installation,
                         type_du_serveur, verifier_coupure_nuage)
from .minuterie_v1 import ECHEANCES_H, PLAFONDS_MACHINE, Machine, cout_cumule, decider
from .minuterie_v2 import verifier_devis
from .minuterie_v4 import (TAUX_USD_EUR_RETENU, _ajouter_journal_creations, _pause, cout_journal,  # noqa: F401
                           deja_depense_go, ecrire_rattrapage, machines_anterieures, taux_retenu)

MODULE = "controle_ia.lean_essai.minuterie_v7"
FORMAT = "minuterie_v7"
DOSSIER_RELATIF = Path("docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1")
NOM_JOURNAL_CREATIONS = "journal-creations-machines-v1.jsonl"
PAS_LONGS = {"d1a": "D-1a"}
API = "https://api.hetzner.cloud/v1"
MARGE_TACHE_H = 1.0              # échéance de la minuterie au plus tard une heure avant la première tâche de la mère
ECART_LIMITE_TACHE_H = 2.0       # première tâche de la mère au moins deux heures après l'heure limite de création
TACHE_MERE_MAX_H = 47.0          # première tâche de la mère au plus 47 heures après la préparation (R-2323)
DECALAGES_TACHES_H = (0.0, 0.5, 24.0)   # rappel dans la session mère ; sessions neuves à + 30 min et + 24 h (CLC5-02)
RAPPEL_LAZAR_H = 1.0             # rappel personnel de Lazar, console de Hetzner (CLC5-02)
ECHEANCE_MIN_H = 1.0
FENETRE_RATTRAPAGE_S = 600.0
PAS_RATTRAPAGE_S = 30.0
REFUS_DURABLES_MAX = 3
DELAI_SURVIE_S = 120.0           # note 4 de la contre-lecture v5 : 60 s portés à 120 s
PAS_SURVIE_S = 1.0
FRAICHEUR_GARDE_S = 300.0
DUREE_MAX_COMMANDE_S = 480.0     # `detruire`, `inventaire` en ligne de commande : sous la limite d'une commande de premier plan
CODE_REFUS, CODE_DESTRUCTION_REFUSEE, CODE_RATTRAPAGE, CODE_PANNE = 1, 3, 4, 5
RE_JETON = re.compile(r"^[0-9a-f]{32}$")
ADRESSE_DOCUMENTATION = "192.0.2.1/32"
PREFIXE_POSTE_MIN = 24           # source SSH au plus large : le /24 du poste (accord de Lazar, R-2415)
SERVICE_ADRESSE = "https://api.ipify.org"
ESSAIS_ADRESSE = 16


def source_poste(ip_poste: str, prefixe: int = 32) -> str:
    """Source SSH des règles : le réseau `IP_POSTE/prefixe`, 24 ≤ prefixe ≤ 32 ; rien de plus large."""
    try:
        ipaddress.IPv4Address(ip_poste)
    except ValueError:
        raise GardeArret("adresse du poste : une adresse IPv4 seule attendue") from None
    if isinstance(prefixe, bool) or not isinstance(prefixe, int) or not PREFIXE_POSTE_MIN <= prefixe <= 32:
        raise GardeArret(f"préfixe du poste {prefixe!r} refusé : entre {PREFIXE_POSTE_MIN} et 32")
    return str(ipaddress.IPv4Network(f"{ip_poste}/{prefixe}", strict=False))


def regles_installation_reseau(source: str) -> list[dict]:
    """Comme `hetzner_v1.regles_installation`, la source étant un réseau déjà contrôlé par `source_poste`."""
    reseau = ipaddress.IPv4Network(source)
    if reseau.prefixlen < PREFIXE_POSTE_MIN:
        raise GardeArret(f"source {reseau.prefixlen} plus large que /{PREFIXE_POSTE_MIN} : refusée")
    return [{"direction": "in", "protocol": "tcp", "port": "22", "source_ips": [str(reseau)],
             "description": "SSH depuis le seul poste"}]


def regles_coupure_reseau(source: str) -> list[dict]:
    return regles_installation_reseau(source) + [
        {"direction": "out", "protocol": "icmp", "destination_ips": [ADRESSE_DOCUMENTATION],
         "description": "seule règle sortante : bascule la sortie en refus implicite"}]


def _lire_adresse_vue(service: str) -> str:
    import urllib.request
    with urllib.request.urlopen(service, timeout=15) as r:   # noqa: S310 — service fixé dans le code ou par la consigne
        return r.read(64).decode("ascii", errors="replace").strip()


def adresses_sortie(ip_poste: str, essais: int = ESSAIS_ADRESSE, lire=None, service: str = SERVICE_ADRESSE) -> dict:
    """Section 0 : par combien d'adresses le poste sort-il ? Ne rend que des comptes et le préfixe conseillé, jamais une
    adresse (CLC5-07). Code 1 (préfixe `None`) si rien n'a répondu ou si une adresse sort du /24 du poste."""
    reseau = ipaddress.IPv4Network(source_poste(ip_poste, PREFIXE_POSTE_MIN))
    lire = lire or (lambda: _lire_adresse_vue(service))
    vues, echecs, illisibles = set(), 0, 0
    for _ in range(int(essais)):
        try:
            brut = lire()
        except Exception:  # noqa: BLE001 — un échec du service compte, il ne tranche pas
            echecs += 1
            continue
        try:
            vues.add(ipaddress.IPv4Address(brut))
        except ValueError:
            illisibles += 1
    hors = sum(1 for v in vues if v not in reseau)
    if not vues or hors:
        prefixe = None
    elif vues == {ipaddress.IPv4Address(ip_poste)}:
        prefixe = 32
    else:
        prefixe = PREFIXE_POSTE_MIN
    return {"essais": int(essais), "reponses": int(essais) - echecs - illisibles, "echecs": echecs, "illisibles": illisibles,
            "adresses_distinctes": len(vues), "ip_poste_vue": ipaddress.IPv4Address(ip_poste) in vues,
            "hors_du_24_du_poste": hors, "prefixe_conseille": prefixe}


class DestructionRefusee(GardeArret):
    """Refus durable de l'API (401, 403) : la destruction ne se fera pas par ce jeton ; à la main, par l'identifiant."""


class RattrapageARefaire(GardeArret):
    """Création incertaine et rien trouvé : un serveur est peut-être allumé ; `detruire --pas d1a` maintenant et plus tard."""


class PannePassagere(GardeArret):
    """Panne passagère de l'interface plus longue que la borne d'une commande : refaire dans 15 minutes, puis prévenir Lazar."""


def dormir_borne(dormir, duree_max_s: float):
    """Pauses cumulées bornées : au-delà, `PannePassagere` (code 5), plutôt qu'une commande coupée sans code par l'outil."""
    cumul = [0.0]

    def borne(s: float) -> None:
        if cumul[0] + s > duree_max_s:
            raise PannePassagere(f"panne passagère de l'interface depuis plus de {duree_max_s:.0f} s : refaire la commande dans "
                                 "15 minutes, puis prévenir Lazar")
        cumul[0] += s
        dormir(s)
    return borne


def _relatif(chemin, racine) -> str:
    """Chemin relatif à la racine du clone : jamais un chemin du poste dans une sortie (CLC5-07)."""
    try:
        return str(Path(chemin).resolve().relative_to(Path(racine).resolve()))
    except ValueError:
        return f"<hors du clone>/{Path(chemin).name}"


def masquer_texte(texte: str, racine) -> str:
    """Chemin du clone et dossier personnel remplacés dans un message ou une trace (CLC5-07)."""
    for brut, marque in ((str(Path(racine).resolve()), "<clone>"), (str(Path.home()), "~")):
        if len(brut) > 1:
            texte = texte.replace(brut, marque)
    return texte


def masquer_regles(regles) -> list[dict]:
    """Règles d'un pare-feu sans les adresses du poste : seule reste l'adresse de documentation de la règle de coupure."""
    sortie = []
    for r in regles or []:
        r = dict(r)
        for cle in ("source_ips", "destination_ips"):
            if cle in r:
                r[cle] = [x if x == ADRESSE_DOCUMENTATION else "<adresse masquée>" for x in (r[cle] or [])]
        sortie.append(r)
    return sortie


def maintenant_utc() -> datetime:
    return datetime.now(timezone.utc)


# ---- dépôt (CLC4-03) ---------------------------------------------------------------------------------------------------------

def racine_depot(depot=None) -> Path:
    """`--depot` s'il est donné, sinon la racine de l'arbre qui porte ce module (src/controle_ia/lean_essai/…)."""
    return Path(depot).resolve() if depot else Path(__file__).resolve().parents[3]


def chemins_depot(racine: Path, exiger: bool = True) -> dict:
    racine = Path(racine)
    verse = racine / DOSSIER_RELATIF
    c = {"racine": racine, "go": racine / "registres" / "go.md", "depenses": racine / "registres" / "depenses.md",
         "verse": verse, "creations": verse / NOM_JOURNAL_CREATIONS}
    if exiger and not (c["go"].is_file() and c["depenses"].is_file()):
        raise GardeArret("dépôt introuvable (registres/go.md ou registres/depenses.md absent) : donner --depot "
                         "RACINE_DU_CLONE")   # sans chemin du poste dans le message (CLC5-07)
    return c


# ---- journaux ----------------------------------------------------------------------------------------------------------------

def _ecrire(journal, entree: dict) -> None:
    """Au mieux : une écriture en échec (disque plein, journal fermé) part sur la sortie d'erreur et ne lève jamais."""
    if journal is None:
        return
    texte = json.dumps({"heure": maintenant_utc().isoformat(timespec="seconds"), **entree}, ensure_ascii=False, default=str)
    try:
        journal.write(texte + "\n")
        journal.flush()
    except (OSError, ValueError) as e:
        try:
            sys.stderr.write(f"journal en échec ({type(e).__name__}) : {texte}\n")
        except (OSError, ValueError):
            pass


def _signaler(journal, entree: dict) -> None:
    """Échecs et refus : au journal s'il y en a un, sinon sur la sortie d'erreur (CLC4-05 : plus de boucle muette)."""
    if journal is not None:
        _ecrire(journal, entree)
        return
    try:
        sys.stderr.write(json.dumps({"heure": maintenant_utc().isoformat(timespec="seconds"), **entree}, ensure_ascii=False,
                                    default=str) + "\n")
    except (OSError, ValueError):
        pass


def fabrique_solder(journal_creations: Path, horloge=maintenant_utc, go_id: str | None = None, jeton: str | None = None):
    """CLC4-07 : après une destruction confirmée, ligne `destruction_confirmee` au journal des créations (GO et jeton donnés,
    ou lus sur les étiquettes du serveur). Au mieux : jamais d'exception, rien si le dossier versé n'existe pas."""
    def solder(ident: int, etiquettes: dict | None) -> None:
        etiquettes = etiquettes or {}
        etiquette, go = jeton or etiquettes.get(ETIQUETTE_CREATION), go_id or etiquettes.get("go")
        if not etiquette or not go:
            return
        if not Path(journal_creations).parent.is_dir():
            _signaler(None, {"solde": "non écrit (dossier versé absent)", "identifiant": ident})
            return
        _ajouter_journal_creations(Path(journal_creations), {"go": go, "etiquette": etiquette, "destruction_confirmee": True,
                                                             "identifiant": int(ident), "heure": horloge().isoformat()})
    return solder


# ---- destruction (R10, CLC4-05, CLC4-06) -------------------------------------------------------------------------------------

def _lire_avec_retentatives(fonction, journal, dormir, essais_max, quoi: str, refus_max: int = REFUS_DURABLES_MAX):
    essai = refus = 0
    while True:
        essai += 1
        try:
            return fonction()
        except RefusDurable as e:
            refus += 1
            _signaler(journal, {quoi: "refus durable", "essai": essai, "erreur": str(e)[:200]})
            if refus >= refus_max:
                raise DestructionRefusee(f"{quoi} refusée durablement ({e}) : ce jeton ne peut rien retrouver ni détruire ; "
                                         "détruire à la main par l'identifiant (console de Hetzner, projet de l'essai)") \
                    from None
        except GardeArret:
            raise
        except Exception as e:  # noqa: BLE001 — retentée, écrite
            _signaler(journal, {quoi: "échec", "essai": essai, "erreur": type(e).__name__})
            if essais_max is not None and essai >= essais_max:
                raise GardeArret(f"{quoi} en échec après {essai} essais") from None
        dormir(_pause(essai, 300.0))


def detruire_par_identifiant(client, ident: int, nom: str = NOM_MACHINE, journal=None, dormir=time.sleep,
                             pause_max_s: float = 300.0, essais_max: int | None = None, refus_max: int = REFUS_DURABLES_MAX,
                             solder=None) -> dict:
    """Par l'identifiant (R10), après contrôle du nom ; échecs passagers retentés sans fin ; refus durables bornés."""
    essai = refus = 0
    etiquettes = None
    while True:
        essai += 1
        try:
            if etiquettes is None:
                lu = client.serveur(ident)
                etiquettes = dict((lu or {}).get("labels") or {})
            etat = client.supprimer_serveur(ident, nom)
            if client.absence_confirmee(ident):
                _ecrire(journal, {"destruction": "confirmée", "identifiant": ident, "essai": essai, "etat": etat})
                if solder is not None:
                    try:
                        solder(ident, etiquettes)
                    except Exception as e:  # noqa: BLE001 — le solde ne défait jamais une destruction
                        _signaler(journal, {"solde": "échec", "erreur": type(e).__name__})
                return {"detruit": True, "etat": etat, "essais": essai, "identifiant": ident}
            raise RuntimeError("serveur encore présent après la demande de suppression")
        except RefusDurable as e:
            refus += 1
            _signaler(journal, {"destruction": "refus durable", "identifiant": ident, "essai": essai, "erreur": str(e)[:200]})
            if refus >= refus_max:
                raise DestructionRefusee(
                    f"suppression du serveur {ident} refusée durablement ({refus} refus ; {e}). Le serveur est peut-être "
                    f"ENCORE ALLUMÉ : le détruire à la main par son identifiant {ident} (console de Hetzner, projet de "
                    "l'essai, ou jeton en lecture et écriture), puis vérifier l'absence par deux lectures") from None
        except GardeArret as e:
            _signaler(journal, {"destruction": "refusée", "identifiant": ident, "motif": str(e)[:200]})
            raise
        except Exception as e:  # noqa: BLE001 — retentée, écrite
            _signaler(journal, {"destruction": "échec", "identifiant": ident, "essai": essai,
                                "erreur": f"{type(e).__name__}: {str(e)[:200]}"})
            if essais_max is not None and essai >= essais_max:
                raise GardeArret(f"destruction de {ident} non confirmée après {essai} essais (borne des essais seulement)") \
                    from None
        dormir(_pause(essai, pause_max_s))


def _detruire_trouves(client, trouves, journal, dormir, essais_max, solder=None, refus_max: int = REFUS_DURABLES_MAX):
    """CLC4-06 : chaque serveur du bon nom est détruit par son identifiant ; ceux d'un autre nom sont rendus, jamais touchés."""
    bons = [(i, n) for i, n in trouves if n == NOM_MACHINE]
    autres = [(i, n) for i, n in trouves if n != NOM_MACHINE]
    if autres:
        _signaler(journal, {"serveurs_d_un_autre_nom": autres, "touches": False})
    detruits = [detruire_par_identifiant(client, i, NOM_MACHINE, journal, dormir, essais_max=essais_max, refus_max=refus_max,
                                         solder=solder) for i, _ in bons]   # nom fixe : le contrôle du nom ne dépend pas du tri
    return detruits, autres


def _arret_autres(detruits, autres) -> GardeArret:
    return GardeArret(f"{len(detruits)} serveur(s) {NOM_MACHINE!r} détruit(s) ; serveur(s) étiqueté(s) d'un autre nom {autres} "
                      "NON touché(s) (R10) : à voir à la main avec Lazar ; ne jamais renommer un serveur de l'essai")


def rattraper_par_etiquette(client, jeton: str, journal=None, dormir=time.sleep, essais_max: int | None = None,
                            fenetre_s: float = FENETRE_RATTRAPAGE_S, pas_s: float = PAS_RATTRAPAGE_S, solder=None,
                            refus_max: int = REFUS_DURABLES_MAX) -> list[dict]:
    """Recherches répétées par l'étiquette unique sur une fenêtre ; tout serveur du bon nom trouvé est détruit."""
    detruits, autres_vus, ecoule = [], set(), 0.0
    while True:
        trouves = _lire_avec_retentatives(lambda: client.chercher_par_etiquette(jeton), journal, dormir, essais_max,
                                          "recherche_etiquette", refus_max)
        _ecrire(journal, {"recherche_etiquette": "faite", "etiquette": jeton, "trouves": trouves, "ecoule_s": ecoule})
        d, autres = _detruire_trouves(client, trouves, journal, dormir, essais_max, solder, refus_max)
        detruits += d
        autres_vus |= set(autres)
        if ecoule >= fenetre_s:
            break
        dormir(pas_s)
        ecoule += pas_s
    if autres_vus:
        raise _arret_autres(detruits, sorted(autres_vus))
    if not detruits:
        raise RattrapageARefaire(f"rien trouvé pendant {fenetre_s / 60:.0f} minutes : rattrapage par l'étiquette {jeton} à "
                                 "refaire (`detruire --pas d1a` maintenant, puis 15 minutes plus tard) ; journal non soldé")
    return detruits


def detruire_pas(client, pas: str = "d1a", journal=None, dormir=time.sleep, essais_max: int | None = None, solder=None,
                 refus_max: int = REFUS_DURABLES_MAX) -> dict:
    """Par les étiquettes fixes et par le nom, sans jeton ni journal ; inventaire de contrôle à la fin."""
    par_etiquettes = _lire_avec_retentatives(lambda: client.chercher_par_etiquettes_fixes(pas), journal, dormir, essais_max,
                                             "recherche_etiquettes_fixes", refus_max)
    par_nom = [(i, n) for i, n in _lire_avec_retentatives(client.inventaire, journal, dormir, essais_max, "inventaire",
                                                          refus_max) if n == NOM_MACHINE]
    trouves = sorted(set(par_etiquettes) | set(par_nom))
    detruits, autres = _detruire_trouves(client, trouves, journal, dormir, essais_max, solder, refus_max)
    restants = [i for i, n in _lire_avec_retentatives(client.inventaire, journal, dormir, essais_max, "inventaire", refus_max)
                if n == NOM_MACHINE]
    if restants:
        raise GardeArret(f"serveurs {restants} encore présents après destruction : relancer `detruire --pas {pas}`")
    if autres:
        raise _arret_autres(detruits, autres)
    return {"trouves": trouves, "detruits": detruits, "message": "aucun serveur de l'essai" if not trouves else ""}


def inventaire_essai(client, pas: str = "d1a", journal=None, dormir=time.sleep, refus_max: int = REFUS_DURABLES_MAX) -> dict:
    """Lecture seule : serveurs de l'essai (étiquettes fixes et nom) et adresses IP primaires attribuées à aucun serveur."""
    par_etiquettes = _lire_avec_retentatives(lambda: client.chercher_par_etiquettes_fixes(pas), journal, dormir, None,
                                             "recherche_etiquettes_fixes", refus_max)
    par_nom = [(i, n) for i, n in _lire_avec_retentatives(client.inventaire, journal, dormir, None, "inventaire", refus_max)
               if n == NOM_MACHINE]
    serveurs = sorted(set(par_etiquettes) | set(par_nom))
    ips = _lire_avec_retentatives(client.ips_primaires_libres, journal, dormir, None, "ips_primaires", refus_max)
    return {"serveurs_de_l_essai": serveurs, "ips_primaires_non_attribuees": ips,
            "message": "aucun serveur de l'essai" if not serveurs else f"{len(serveurs)} serveur(s) de l'essai"}


# ---- veille (CLC4-01) --------------------------------------------------------------------------------------------------------

def veiller(m: Machine, client, horloge=maintenant_utc, dormir=time.sleep, pas_s: float = 60.0, journal=None,
            tours_max: int | None = None, essais_max: int | None = None, refus_max: int = REFUS_DURABLES_MAX,
            solder=None) -> dict:
    tours = 0
    while True:
        maintenant = horloge()
        detruire, motif = decider(m, maintenant)
        _ecrire(journal, {"identifiant": m.identifiant, "detruire": detruire, "motif": motif})
        if detruire:
            r = detruire_par_identifiant(client, m.identifiant, m.nom, journal, dormir, essais_max=essais_max,
                                         refus_max=refus_max, solder=solder)
            r.update({"motif": motif, "cout_cumule_usd": cout_cumule(m, maintenant)})
            return r
        try:
            if client.absence_confirmee(m.identifiant):
                _ecrire(journal, {"identifiant": m.identifiant, "absence": "confirmée par deux lectures"})
                if solder is not None:
                    solder(m.identifiant, {})
                return {"detruit": False, "absent": True, "motif": "serveur absent (détruit par une autre commande)"}
        except GardeArret:
            raise
        except Exception as e:  # noqa: BLE001 — la minuterie ne meurt pas d'une lecture
            _ecrire(journal, {"identifiant": m.identifiant, "lecture": "échec", "erreur": f"{type(e).__name__}"})
        tours += 1
        if tours_max is not None and tours >= tours_max:
            return {"detruit": False, "motif": motif}
        dormir(pas_s)


def demarrer_et_veiller(client, *, identifiant: int, pas: str, depuis: datetime, echeance_h: float | None = None,
                        taux_declare: float | None = None, deja: float = 0.0, lieu: str | None = None,
                        prix_usd_h: float | None = None, journal=None, solder=None, horloge=maintenant_utc,
                        dormir=time.sleep, pas_s: float = 60.0, tours_max: int | None = None,
                        refus_max: int = REFUS_DURABLES_MAX) -> dict:
    """Démarrage sous retentatives, borné par l'échéance ; replis explicites ; seul le refus de nom (R10) arrête."""
    pas_long = PAS_LONGS[pas]
    echeance_h = ECHEANCES_H[pas_long] if echeance_h is None else float(echeance_h)
    if not 0 < echeance_h <= ECHEANCES_H[pas_long]:
        raise GardeArret("échéance plus longue que celle du pas, ou non positive")
    if depuis.tzinfo is None:
        raise GardeArret("--depuis sans fuseau : UTC exigé")
    taux = taux_retenu(taux_declare)
    fin = depuis + timedelta(hours=echeance_h)
    s, prix_api, essai, refus = None, None, 0, 0
    while True:
        essai += 1
        try:
            s = client.serveur(identifiant)
            if s is None:
                if client.absence_confirmee(identifiant):
                    _ecrire(journal, {"demarrage": "serveur absent (deux lectures)", "identifiant": identifiant})
                    if solder is not None:
                        solder(identifiant, {})
                    return {"detruit": False, "absent": True, "motif": "serveur absent au démarrage"}
                raise ErreurHetzner("lectures contradictoires : 404, puis présent à l'inventaire")
            if s.get("name") != NOM_MACHINE:
                _signaler(journal, {"demarrage": "refus de nom", "identifiant": identifiant, "nom": s.get("name")})
                raise GardeArret(f"serveur {identifiant} nommé {s.get('name')!r} : la minuterie ne garde que {NOM_MACHINE!r} "
                                 "(R10)")
            lieu_lu, _source = lieu_du_serveur(s)
            type_lu = type_du_serveur(s)
            if type_lu and (lieu_lu or lieu):
                try:
                    prix_api = client.prix_horaire_eur(type_lu, lieu_lu or lieu)["total"] * taux
                except GardeArret as e:   # prix introuvable ou devise : repli explicite, jamais la mort
                    _signaler(journal, {"demarrage": "prix illisible (repli)", "motif": str(e)[:200]})
            break
        except RefusDurable as e:
            refus += 1
            _signaler(journal, {"demarrage": "refus durable", "essai": essai, "erreur": str(e)[:200]})
            if refus >= refus_max:
                raise DestructionRefusee(f"lecture du serveur {identifiant} refusée durablement ({e}) : la minuterie ne peut "
                                         f"ni lire ni détruire ; détruire à la main par l'identifiant {identifiant}") from None
        except GardeArret:
            raise
        except Exception as e:  # noqa: BLE001 — démarrage retenté
            _signaler(journal, {"demarrage": "échec", "essai": essai, "erreur": f"{type(e).__name__}: {str(e)[:120]}"})
            if horloge() >= fin:
                _signaler(journal, {"demarrage": "échéance passée sans lecture : destruction par identifiant"})
                s = None
                break
        dormir(_pause(essai, 300.0))
    cree_a = creation_du_serveur(s)
    depuis_retenu = min(depuis, cree_a) if cree_a is not None else depuis
    lieu_lu, source = lieu_du_serveur(s)
    candidats = [p for p in (prix_usd_h, prix_api) if p]
    reste = PLAFONDS_MACHINE[pas_long] - deja
    try:
        if candidats:
            prix = max(candidats)
            verifier_devis(prix, pas_long, deja)
        else:
            prix = reste / ECHEANCES_H[pas_long]   # pire cas admis par le devis : tenu par construction
            _signaler(journal, {"demarrage": "prix inconnu : pire cas admis par le devis", "prix_usd_h": prix})
        m = Machine(identifiant, NOM_MACHINE, depuis_retenu, prix, reste, echeance_h)
    except GardeArret as e:
        _signaler(journal, {"demarrage": "devis non tenu : destruction immédiate", "motif": str(e)[:200]})
        r = detruire_par_identifiant(client, identifiant, NOM_MACHINE, journal, dormir, refus_max=refus_max, solder=solder)
        r["motif"] = f"devis non tenu au démarrage ({e})"
        return r
    _ecrire(journal, {"demarrage": "fait", "identifiant": identifiant, "lieu": lieu_lu or lieu, "source_lieu":
                      source if lieu_lu else ("--lieu" if lieu else "aucune"), "prix_usd_h": prix,
                      "depuis": depuis_retenu.isoformat(), "echeance": (depuis_retenu + timedelta(hours=echeance_h)).isoformat(),
                      "plafond_usd": reste})
    return veiller(m, client, horloge=horloge, dormir=dormir, pas_s=pas_s, journal=journal, tours_max=tours_max,
                   refus_max=refus_max, solder=solder)


# ---- minuterie détachée et son contrôle (CLC4-01, CLC4-03) -------------------------------------------------------------------

def lancer_minuterie_detachee(*, identifiant: int, pas: str, depuis: datetime, echeance_h: float, taux: float, deja: float,
                              jeton: str, go_id: str, lieu: str, prix_usd_h: float, dossier: Path, racine: Path,
                              popen=subprocess.Popen) -> dict:
    """`veiller` dans une session à elle (sans terminal), PID écrit dans un fichier versé ; tout est passé en arguments. L'objet
    `Popen` est rendu sous `_processus` (jamais imprimé), pour un contrôle de survie sans course (CLC5-01)."""
    base = f"minuterie-{pas}-{jeton[:12]}"
    journal, sortie, fichier_pid = (dossier / f"{base}-journal-v1.jsonl", dossier / f"{base}-sortie-v1.log",
                                    dossier / f"{base}-pid-v1.txt")
    existants = [p.name for p in (journal, sortie, fichier_pid) if p.exists()]
    if existants:
        raise GardeArret(f"fichiers de minuterie déjà présents {existants} (R12) : jeton réutilisé")
    argv = [sys.executable, "-B", "-m", MODULE, "veiller", "--identifiant", str(identifiant), "--pas", pas,
            "--depuis", depuis.isoformat(), "--echeance-h", repr(float(echeance_h)), "--taux-usd-eur", repr(float(taux)),
            "--deja-depense-usd", repr(float(deja)), "--lieu", lieu, "--prix-usd-h", repr(float(prix_usd_h)),
            "--go", go_id, "--etiquette", jeton, "--journal", str(journal), "--depot", str(racine)]
    env = dict(os.environ, PYTHONPATH=str(Path(__file__).resolve().parents[2]))
    dossier.mkdir(parents=True, exist_ok=True)
    with open(sortie, "xb") as s:
        p = popen(argv, stdin=subprocess.DEVNULL, stdout=s, stderr=s, start_new_session=True, env=env, cwd=str(racine))
    fichier_pid.write_text(f"{p.pid} {identifiant} {jeton}\n", encoding="utf-8")
    return {"pid": p.pid, "fichier_pid": str(fichier_pid), "journal": str(journal), "sortie": str(sortie), "argv": argv,
            "_processus": p}


def lignes_garder(chemin) -> list[dict]:
    try:
        texte = Path(chemin).read_text(encoding="utf-8")
    except OSError:
        return []
    sortie = []
    for x in texte.splitlines():
        try:
            e = json.loads(x)
        except ValueError:
            continue
        if isinstance(e, dict) and e.get("detruire") is False and str(e.get("motif", "")).startswith("garder"):
            sortie.append(e)
    return sortie


def _existe(pid: int) -> str:
    try:
        os.kill(pid, 0)   # signal 0 : contrôle d'existence, rien n'est envoyé
    except ProcessLookupError:
        return "absent"
    except PermissionError:
        return "autre utilisateur"
    return "présent"


def _ps(pid: int, executer=subprocess.run) -> str:
    r = executer(["ps", "-ww", "-p", str(pid), "-o", "command="], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def _est_la_minuterie(arguments: list[str], identifiant: str) -> bool:
    if MODULE not in arguments or "veiller" not in arguments:
        return False
    return any(a == "--identifiant" and b == identifiant for a, b in zip(arguments, arguments[1:]))


def _heure_ou_rien(x) -> datetime | None:
    try:
        d = datetime.fromisoformat(str(x).replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo is not None else None


def verifier_minuterie(fichier_pid: Path, racine_proc: Path = Path("/proc"), existe=_existe, ps=_ps,
                       journal_minuterie: Path | None = None, horloge=maintenant_utc,
                       fraicheur_s: float = FRAICHEUR_GARDE_S) -> dict:
    """Par le PID (R10) : `/proc/PID/cmdline` sous Linux ; `kill -0 PID` et `ps -ww -p PID -o command=` ailleurs (macOS).
    Avec `journal_minuterie` : la dernière ligne « garder » doit dater de moins de `fraicheur_s`. Lecture unique : à l'opérateur
    de refaire deux minutes plus tard avant de conclure ; jamais de relance d'une minuterie (note 5)."""
    pid_texte, identifiant, _jeton = Path(fichier_pid).read_text(encoding="utf-8").split()
    pid = int(pid_texte)
    if (Path(racine_proc) / "self").exists():
        methode = "/proc"
        try:
            arguments = [x.decode("utf-8", "replace") for x in (Path(racine_proc) / str(pid) / "cmdline").read_bytes()
                         .split(b"\0") if x]
        except OSError:
            arguments = None
    else:
        methode = "kill -0 et ps -p"
        etat = existe(pid)
        arguments = None if etat == "absent" else (ps(pid).split() if etat == "présent" else [])
    if arguments is None:
        res = {"vivante": False, "motif": "processus absent : détruire le serveur par son identifiant (jamais de relance de "
                                          "la minuterie)"}
    elif not _est_la_minuterie(arguments, identifiant):
        res = {"vivante": False, "motif": "le PID désigne un autre processus : détruire le serveur par son identifiant (jamais "
                                          "de relance)"}
    else:
        res = {"vivante": True, "motif": ""}
    res.update(pid=pid, methode=methode, conforme=res["vivante"])
    if journal_minuterie is not None and res["vivante"]:
        gardes = lignes_garder(journal_minuterie)
        derniere = _heure_ou_rien(gardes[-1].get("heure")) if gardes else None
        res["derniere_garde"] = derniere.isoformat() if derniere else None
        if derniere is None or (horloge() - derniere).total_seconds() > fraicheur_s:
            res.update(conforme=False, motif=f"minuterie muette (aucune ligne « garder » depuis {fraicheur_s:.0f} s) : refaire "
                                              "dans 2 minutes, puis détruire le serveur par son identifiant (jamais de relance)")
    return res


def attendre_minuterie(minuterie: dict, *, dormir=time.sleep, verifier=verifier_minuterie, delai_s: float = DELAI_SURVIE_S,
                       pas_s: float = PAS_SURVIE_S, processus=None) -> dict:
    """CLC5-01 : « armée » dès qu'elle vit et a écrit une ligne « garder ». « Morte » seulement si le processus lancé est fini
    (`processus.poll()`, sans course), ou si aucune lecture de son PID ne l'a vue vivante jusqu'au délai ; jamais sur une seule
    lecture négative (juste après l'`exec`, `/proc/PID/cmdline` peut se lire vide quelques millisecondes)."""
    ecoule, vue, negatives, motif = 0.0, False, 0, ""
    while True:
        if processus is not None:
            code = processus.poll()
            if code is not None:
                return {"vivante": False, "garder": False, "motif": f"processus fini (code {code})",
                        "lectures_negatives": negatives}
            vivante = True
        else:
            etat = verifier(Path(minuterie["fichier_pid"]))
            vivante = bool(etat["vivante"])
            if not vivante:
                negatives += 1
                motif = etat["motif"]
        vue = vue or vivante
        if vivante and lignes_garder(minuterie["journal"]):
            return {"vivante": True, "garder": True, "motif": "", "lectures_negatives": negatives}
        if ecoule >= delai_s:
            if not vue:
                return {"vivante": False, "garder": False, "motif": f"jamais vue vivante en {delai_s:.0f} s ({motif})",
                        "lectures_negatives": negatives}
            return {"vivante": vivante, "garder": False, "motif": f"aucune ligne « garder » en {delai_s:.0f} s",
                    "lectures_negatives": negatives}
        dormir(pas_s)
        ecoule += pas_s


# ---- préparation, poussée, accès (CLC4-02) -----------------------------------------------------------------------------------

def _heure(x) -> datetime:
    d = _heure_ou_rien(x)
    if d is None:
        raise GardeArret(f"heure illisible ou sans fuseau {x!r} : ISO 8601 avec fuseau (UTC) exigé")
    return d


def _utc(d: datetime) -> str:
    return d.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def message_tache_mere(prep: dict, rang: int) -> str:
    """Message autosuffisant d'une tâche de la mère (CLC5-02, note 7) : la tâche 1 est un rappel dans la session mère ; les
    tâches 2 et 3 ouvrent une session neuve, qui n'a pas d'autre mémoire que ce texte."""
    jeton, pas = prep["etiquette"], prep["pas"]
    au_plus_tard = _utc(prep["heure_tache_mere"] - timedelta(hours=MARGE_TACHE_H))
    tete = {1: "tâche 1 sur 3, rappel dans la session mère, armée AVANT la création",
            2: "tâche 2 sur 3, en session neuve : tu n'as pas d'autre mémoire que ce message",
            3: "tâche 3 sur 3, en session neuve, 24 heures après la première : tu n'as pas d'autre mémoire que ce message"}[rang]
    return (f"Essai Lean D-1a, garde-fou de la mère, {tete} (R-2323, R-2333). Le serveur {NOM_MACHINE!r} (étiquettes "
            f"essai=lean, pas={pas}, creation={jeton}) a pu être créé depuis l'ordinateur de Lazar ; sa minuterie locale le "
            f"détruit au plus tard à {au_plus_tard}. Fais seulement ceci, par ton propre jeton (HCLOUD_TOKEN lu par son nom, "
            "jamais affiché ni écrit ; des réponses, n'afficher que les identifiants et les noms) : "
            f"(0) API={API} ; lire() {{ printf 'Authorization: Bearer %s\\n' \"$HCLOUD_TOKEN\" | curl -sS --max-time 30 "
            "-H @- \"$@\"; } ; "
            f"(1) lire \"$API/servers?label_selector=essai%3Dlean%2Cpas%3D{pas}\" et lire \"$API/servers?name={NOM_MACHINE}\" ; "
            "(2) pour chaque serveur trouvé : lire \"$API/servers/<identifiant>\" et, seulement si son nom est exactement "
            f"{NOM_MACHINE!r}, lire -X DELETE \"$API/servers/<identifiant>\" ; "
            "ne jamais toucher un serveur d'un autre nom (le signaler à Lazar) ; "
            "(3) constater l'absence par deux lectures (le serveur rend 404, et son identifiant manque aux deux listes), puis "
            "relire les deux listes une minute plus tard ; "
            "(4) erreur passagère (délai, 429, 5xx) : réessayer trois fois en 15 minutes, puis prévenir Lazar ; "
            "si une suppression rend 401 ou 403 : s'arrêter et demander à Lazar de détruire à la main par l'identifiant "
            "(console de Hetzner) ; "
            "(5) inscrire dans registres/arrets.md l'identifiant, l'heure et le motif « tâche de la mère », ou « aucun serveur "
            "de l'essai », et clore la ligne « en tâche jusqu'à » de registres/etat.md ; "
            "(6) prévenir Lazar, et la session mère si tu es une session neuve. Ne jamais recréer de serveur.")


def ligne_etat_mere(prep: dict) -> str:
    """CLC5-04 : ligne que la mère inscrit dans `registres/etat.md` à l'armement, pour que la routine de reprise (R-2322) ne
    détruise pas un serveur au travail ; au-delà de l'heure, ou sans la ligne, la routine le détruit."""
    au_plus_tard = _utc(prep["heure_tache_mere"] - timedelta(hours=MARGE_TACHE_H))
    rappel = _utc(prep["heure_tache_mere"] + timedelta(hours=RAPPEL_LAZAR_H))
    return (f"Serveur `{NOM_MACHINE}` (essai Lean D-1a, {prep['go']}, étiquette `creation={prep['etiquette']}`) en tâche "
            f"jusqu'à {au_plus_tard} au plus tard ; au-delà, ou si cette ligne manque, le détruire par son identifiant après "
            "contrôle du nom (R10). Tâches de destruction de la mère : <identifiants des trois tâches>. Rappel de Lazar : "
            f"{rappel}.")


def preparer(*, go_id: str, chemins: dict, heure_limite_creation: datetime, heure_tache_mere: datetime, pas: str = "d1a",
             horloge=maintenant_utc, jeton: str | None = None) -> dict:
    """Avant toute création : fichier de rattrapage neuf (R12) à committer et pousser, que la mère lit pour s'armer. Une seule
    préparation par dossier versé (CLC5-03)."""
    maintenant = horloge()
    garde_go_v1.autoriser_creation_machine(go_id, chemins["go"], maintenant.date())
    autres = sorted(p.name for p in Path(chemins["verse"]).glob(f"rattrapage-machine-{pas}-*-v1.json"))
    if autres:
        raise GardeArret(f"une préparation existe déjà ({', '.join(autres)}) : une seule préparation et une seule création "
                         f"sous {go_id} ; une seconde passe par une consigne neuve de la mère")
    anterieures = machines_anterieures(chemins["depenses"], chemins["creations"], go_id)
    if anterieures:
        raise GardeArret(f"seconde machine sous {go_id} refusée sans exception : {anterieures} ; une seconde machine passe par "
                         "une consigne neuve de la mère")
    if heure_limite_creation.tzinfo is None or heure_tache_mere.tzinfo is None:
        raise GardeArret("heures sans fuseau : UTC exigé")
    if heure_limite_creation <= maintenant:
        raise GardeArret("heure limite de création déjà passée")
    if heure_tache_mere < heure_limite_creation + timedelta(hours=ECART_LIMITE_TACHE_H):
        raise GardeArret(f"tâche de la mère moins de {ECART_LIMITE_TACHE_H:.0f} heures après l'heure limite de création")
    if heure_tache_mere > maintenant + timedelta(hours=TACHE_MERE_MAX_H):
        raise GardeArret(f"tâche de la mère plus de {TACHE_MERE_MAX_H:.0f} heures après maintenant")
    jeton = jeton or uuid.uuid4().hex
    commande = f"PYTHONPATH=src python3 -B -m {MODULE}"
    prep = {"format": FORMAT, "pas": pas, "go": go_id, "nom": NOM_MACHINE, "etiquette": jeton,
            "etiquettes_fixes": {"essai": "lean", "pas": pas}, "heure_preparation": maintenant,
            "heure_limite_creation": heure_limite_creation, "heure_tache_mere": heure_tache_mere,
            "echeance_au_plus_tard": heure_tache_mere - timedelta(hours=MARGE_TACHE_H),
            "rappel_lazar": heure_tache_mere + timedelta(hours=RAPPEL_LAZAR_H)}
    modes = ("rappel dans la session mère (send_later)", "tâche programmée qui ouvre une session neuve",
             "tâche programmée qui ouvre une session neuve")
    prep["taches_mere"] = [{"rang": i + 1, "heure": heure_tache_mere + timedelta(hours=d), "mode": modes[i],
                            "message": message_tache_mere(prep, i + 1)} for i, d in enumerate(DECALAGES_TACHES_H)]
    prep["ligne_etat_mere"] = ligne_etat_mere(prep)
    prep["commandes_poste"] = {"par_pas": f"{commande} detruire --pas {pas} --journal <fichier neuf>",
                               "par_etiquette": f"{commande} detruire --etiquette {jeton} --journal <fichier neuf>",
                               "par_identifiant": f"{commande} detruire --identifiant <N> --journal <fichier neuf>"}
    chemin = ecrire_rattrapage(chemins["verse"], json.loads(json.dumps(prep, default=lambda d: d.isoformat())))
    return {"rattrapage": chemin.name, "etiquette": jeton,
            "taches_mere": [t["heure"].isoformat() for t in prep["taches_mere"]],
            "suite": "committer et pousser ce fichier sur la branche du poste ; la mère le lit, prouve le même projet, s'arme, "
                     "et rend « armée » avec son empreinte (sha256) ; aucune création avant"}


def lire_rattrapage(chemin, go_id: str | None = None) -> dict:
    chemin = Path(chemin)
    try:
        r = json.loads(chemin.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise GardeArret(f"fichier de rattrapage {chemin.name} illisible ({type(e).__name__})") from None
    if not isinstance(r, dict) or r.get("format") != FORMAT:
        raise GardeArret(f"{chemin.name} n'est pas un fichier écrit par `minuterie_v7 preparer`")
    jeton = r.get("etiquette")
    if not isinstance(jeton, str) or not RE_JETON.match(jeton) or r.get("pas") not in PAS_LONGS:
        raise GardeArret(f"{chemin.name} : jeton ou pas mal formé")
    if chemin.name != f"rattrapage-machine-{r['pas']}-{jeton[:12]}-v1.json" or r.get("nom") != NOM_MACHINE:
        raise GardeArret(f"{chemin.name} : nom du fichier, jeton ou nom du serveur incohérents")
    if go_id is not None and r.get("go") != go_id:
        raise GardeArret(f"{chemin.name} porte le GO {r.get('go')!r}, {go_id} cité")
    for k in ("heure_limite_creation", "heure_tache_mere"):
        r[k] = _heure(r.get(k))
    return r


def fichier_pousse(racine: Path, chemin: Path, executer=subprocess.run) -> tuple[bool, str]:
    """Le fichier est suivi par git, égal à HEAD, et le dernier commit qui le porte est contenu dans la branche **distante**,
    lue par `git ls-remote` sur l'amont de la branche courante (note 2 : une référence de suivi écrite à la main ne suffit
    plus)."""
    try:
        rel = str(Path(chemin).resolve().relative_to(Path(racine).resolve()))
    except ValueError:
        return False, "fichier hors du dépôt"

    def git(*args):
        return executer(["git", "-C", str(racine), *args], capture_output=True, text=True, timeout=60)
    try:
        if git("ls-files", "--error-unmatch", "--", rel).returncode != 0:
            return False, "fichier non suivi par git (git add, commit, push)"
        if git("diff", "--quiet", "HEAD", "--", rel).returncode != 0:
            return False, "fichier modifié depuis le dernier commit"
        commit = git("log", "-1", "--format=%H", "--", rel).stdout.strip()
        amont = git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}").stdout.strip()
        if not commit or "/" not in amont:
            return False, "branche sans amont (pousser avec `git push -u`)"
        distant, branche = amont.split("/", 1)
        lu = git("ls-remote", "--exit-code", distant, f"refs/heads/{branche}")
        tete = lu.stdout.split()[0] if lu.returncode == 0 and lu.stdout.split() else ""
        if not tete:
            return False, f"branche {branche} absente du dépôt distant (lu par git ls-remote)"
        if git("merge-base", "--is-ancestor", commit, tete).returncode != 0:
            return False, (f"commit {commit[:12]} absent de la branche distante (lu par git ls-remote) : pousser ; si la tête "
                           "distante est inconnue ici, `git fetch`")
    except (OSError, subprocess.SubprocessError) as e:
        return False, f"git inutilisable ({type(e).__name__})"
    return True, f"commit {commit[:12]} contenu dans {amont} (lu par git ls-remote)"


def _chemin_acces(prep: dict, dossier: Path) -> Path:
    return Path(dossier) / f"acces-machine-{prep['pas']}-{prep['etiquette'][:12]}-v1.json"


def lire_acces(prep: dict, dossier: Path) -> dict:
    chemin = _chemin_acces(prep, dossier)
    try:
        d = json.loads(chemin.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise GardeArret(f"fichier d'accès {chemin.name} illisible ({type(e).__name__})") from None
    if not isinstance(d, dict) or d.get("etiquette") != prep["etiquette"]:
        raise GardeArret(f"{chemin.name} : fichier d'accès d'un autre jeton")
    return d


def creer_acces(client, prep: dict, cle_publique: str, ip_poste: str, dossier: Path, horloge=maintenant_utc,
                prefixe: int = 32) -> dict:
    """Clé SSH et pare-feu (règles d'installation : SSH depuis le seul poste), étiquetés au jeton ; identifiants dans un fichier
    neuf. CLC5-07 : ce fichier ne porte ni l'adresse du poste ni les règles, et la clé part sans son commentaire (souvent
    « utilisateur@machine »)."""
    texte = cle_publique.strip()
    if "PRIVATE" in texte.upper() or "\n" in texte or not texte.startswith(("ssh-", "ecdsa-")):
        raise GardeArret("clé publique SSH d'une seule ligne attendue (ssh-… ou ecdsa-…) ; jamais une clé privée")
    morceaux = texte.split()
    if len(morceaux) < 2:
        raise GardeArret("clé publique SSH incomplète : type et matière attendus")
    try:
        ipaddress.IPv4Address(ip_poste)
    except ValueError:
        raise GardeArret("adresse du poste : une adresse IPv4 seule attendue") from None
    source = source_poste(ip_poste, prefixe)
    chemin = _chemin_acces(prep, dossier)
    if chemin.exists():
        raise GardeArret(f"{chemin.name} existe déjà (R12)")
    etiquettes = {"essai": "lean", "pas": prep["pas"], "go": prep["go"], ETIQUETTE_CREATION: prep["etiquette"]}
    nom = f"{NOM_MACHINE}-{prep['etiquette'][:12]}"
    cle = client.creer_cle_ssh_etiquetee(nom, " ".join(morceaux[:2]), etiquettes)
    try:
        pare_feu = client.creer_pare_feu_etiquete(nom, regles_installation_reseau(source), etiquettes)
    except Exception:
        client.supprimer_cle_ssh(cle["id"])   # aucun objet orphelin
        raise
    entree = {"format": FORMAT, "etiquette": prep["etiquette"], "pas": prep["pas"], "nom": nom, "cle_ssh": cle,
              "pare_feu": pare_feu, "etiquettes": etiquettes, "heure": horloge().isoformat()}
    Path(dossier).mkdir(parents=True, exist_ok=True)
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(json.dumps(entree, ensure_ascii=False, indent=1) + "\n")
    return {"acces": chemin.name, **entree}


def couper_acces(client, prep: dict, dossier: Path, ip_poste: str, prefixe: int = 32) -> dict:
    """Règles de coupure sur le pare-feu du fichier d'accès, après relecture de son nom (note 1) ; rien de l'adresse du poste
    dans ce qui est rendu (CLC5-07)."""
    try:
        ipaddress.IPv4Address(ip_poste)
    except ValueError:
        raise GardeArret("adresse du poste : une adresse IPv4 seule attendue") from None
    acces = lire_acces(prep, dossier)
    ident = int(acces["pare_feu"]["id"])
    lu = client.lire_pare_feu(ident)
    if lu.get("name") != acces["nom"]:
        raise GardeArret(f"pare-feu {ident} nommé {lu.get('name')!r}, {acces['nom']!r} attendu : aucune règle posée")
    regles = regles_coupure_reseau(source_poste(ip_poste, prefixe))
    client.poser_regles(ident, regles)
    return {"pare_feu": ident, "regles_posees": len(regles),
            "suite": f"python3 -B -m {MODULE} verifier-coupure --serveur <N> --pare-feu {ident} --journal <J>"}


def _lire_ou_rien(client, chemin: str, cle: str) -> dict | None:
    statut, d = client.transport("GET", chemin, None)
    if statut == 404:
        return None
    if statut != 200 or not isinstance(d, dict) or not isinstance(d.get(cle), dict):
        raise ErreurHetzner(f"GET {chemin} : statut {statut}")
    return d[cle]


def supprimer_acces(client, prep: dict, dossier: Path) -> dict:
    """Après la destruction du serveur : pare-feu et clé SSH supprimés par leurs identifiants, après contrôle de leur nom."""
    acces = lire_acces(prep, dossier)
    if client.chercher_par_etiquette(prep["etiquette"]) or any(n == NOM_MACHINE for _, n in client.inventaire()):
        raise GardeArret("un serveur de l'essai existe encore : le détruire d'abord (un pare-feu appliqué ne se supprime pas)")
    fait = {}
    for quoi, chemin, cle, supprimer in (("pare_feu", f"/firewalls/{int(acces['pare_feu']['id'])}", "firewall",
                                          client.supprimer_pare_feu),
                                         ("cle_ssh", f"/ssh_keys/{int(acces['cle_ssh']['id'])}", "ssh_key",
                                          client.supprimer_cle_ssh)):
        objet = _lire_ou_rien(client, chemin, cle)
        if objet is None:
            fait[quoi] = "absent"
            continue
        if objet.get("name") != acces["nom"]:
            raise GardeArret(f"{chemin} nommé {objet.get('name')!r}, {acces['nom']!r} attendu : rien d'autre n'est touché")
        supprimer(int(objet["id"]))
        fait[quoi] = "supprimé"
    return fait


# ---- création (CLC4-01, CLC4-02, CLC4-07) ------------------------------------------------------------------------------------

def creer_et_armer(client, *, go_id: str, chemins: dict, rattrapage: Path, empreinte_mere: str, type_serveur: str, image: str,
                   lieu: str, taux_declare: float | None = None, deja_declare: float | None = None, horloge=maintenant_utc,
                   dormir=time.sleep, journal=None, essais_max: int | None = None, lancer=lancer_minuterie_detachee,
                   controler=None, verifier_pousse=fichier_pousse, fenetre_s: float = FENETRE_RATTRAPAGE_S) -> dict:
    if type_serveur not in TYPES_PERMIS:
        raise GardeArret(f"type {type_serveur!r} hors de la liste du devis {TYPES_PERMIS}")
    rattrapage = Path(rattrapage)
    prep = lire_rattrapage(rattrapage, go_id)
    pas, pas_long, jeton = prep["pas"], PAS_LONGS[prep["pas"]], prep["etiquette"]
    empreinte = hashlib.sha256(rattrapage.read_bytes()).hexdigest()
    if str(empreinte_mere).strip().lower() != empreinte:
        raise GardeArret("empreinte du fichier de rattrapage différente de celle que la mère a lue (mot « armée ») : ne pas "
                         "créer ; refaire L3 et M1")
    autres = sorted(p.name for p in Path(chemins["verse"]).glob(f"rattrapage-machine-{pas}-*-v1.json")
                    if p.name != rattrapage.name)
    if autres:
        raise GardeArret(f"autre préparation dans le dossier versé ({', '.join(autres)}) : seconde machine refusée sans exception "
                         f"sous {go_id}, même sans journal des créations (CLC5-03)")
    if horloge() > prep["heure_limite_creation"]:
        raise GardeArret(f"heure limite de création passée ({_utc(prep['heure_limite_creation'])}) : ne pas créer, rendre la "
                         "main à Lazar")
    acces = lire_acces(prep, chemins["verse"])
    for fichier in (rattrapage, _chemin_acces(prep, chemins["verse"])):
        pousse, motif = verifier_pousse(chemins["racine"], fichier)
        if not pousse:
            raise GardeArret(f"{fichier.name} non poussé ({motif}) : le committer et le pousser avant toute création")
    jour = horloge().date()
    garde_go_v1.autoriser_creation_machine(go_id, chemins["go"], jour)
    anterieures = machines_anterieures(chemins["depenses"], chemins["creations"], go_id)
    if anterieures:
        raise GardeArret(f"seconde machine sous {go_id} refusée sans exception : {anterieures} ; une seconde machine passe par "
                         "une consigne neuve de la mère")
    taux = taux_retenu(taux_declare)
    deja = deja_depense_go(chemins["depenses"], go_id, chemins["creations"], deja_declare, horloge())
    prix = client.prix_horaire_eur(type_serveur, lieu)
    prix_usd = prix["total"] * taux
    verifier_devis(prix_usd, pas_long, deja["retenu"])
    intention = horloge()
    limite = prep["heure_tache_mere"] - timedelta(hours=MARGE_TACHE_H)
    if (limite - intention).total_seconds() / 3600.0 < ECHEANCE_MIN_H:
        raise GardeArret("moins d'une heure avant l'échéance imposée par la tâche de la mère : ne pas créer")
    cles_ssh, pare_feux = [int(acces["cle_ssh"]["id"])], [int(acces["pare_feu"]["id"])]   # note 3 : objets du fichier poussé
    entree = {"go": go_id, "intention": True, "etiquette": jeton, "heure_intention": intention.isoformat(),
              "type": type_serveur, "lieu": lieu, "prix_eur_h": prix, "taux_usd_eur": taux, "prix_usd_h": prix_usd,
              "deja_depense": deja, "pas": pas_long, "rattrapage": rattrapage.name, "empreinte_rattrapage": empreinte,
              "cle_ssh": cles_ssh[0], "pare_feu": pare_feux[0], "echeance_au_plus_tard": limite.isoformat()}
    _ajouter_journal_creations(chemins["creations"], entree, exige=True)   # intention exigée AVANT l'appel
    _ecrire(journal, entree)
    solder = fabrique_solder(chemins["creations"], horloge, go_id, jeton)
    try:
        reponse = client.creer_serveur_etiquete(go_id, chemins["go"], jour, type_serveur, image, lieu, cles_ssh, pare_feux,
                                                jeton)
        serveur = reponse["server"]
        ident = int(serveur["id"])
    except GardeArret:
        raise
    except CreationRefusee as e:
        trouves = _lire_avec_retentatives(lambda: client.chercher_par_etiquette(jeton), journal, dormir, essais_max,
                                          "recherche_de_controle")
        if trouves:   # note 1 de la v4 : refus annoncé, serveur pourtant là
            detruits, autres = _detruire_trouves(client, trouves, journal, dormir, essais_max, solder)
            if autres:
                raise _arret_autres(detruits, autres)
            raise GardeArret(f"création refusée par l'API ({e}) mais {len(detruits)} serveur(s) de l'étiquette trouvé(s) et "
                             "détruit(s) par identifiant") from None
        _ajouter_journal_creations(chemins["creations"], {"go": go_id, "etiquette": jeton, "aucune_creation": True,
                                                          "heure": horloge().isoformat(), "motif": str(e)[:200]})
        raise GardeArret(f"création refusée par l'API, aucun serveur créé (recherche de contrôle vide) : {e}") from None
    except Exception as e:  # noqa: BLE001 — réponse perdue ou illisible
        _ecrire(journal, {"creation": "incertaine", "etiquette": jeton, "erreur": f"{type(e).__name__}"})
        detruits = rattraper_par_etiquette(client, jeton, journal, dormir, essais_max, fenetre_s=fenetre_s, solder=solder)
        raise GardeArret(f"création incertaine ({type(e).__name__}) : {len(detruits)} serveur(s) de l'étiquette détruit(s) "
                         "par identifiant") from None
    cree_a = creation_du_serveur(serveur)   # illisible ⇒ l'intention, plus tôt, suffit (jamais d'arrêt ici)
    depuis = min(intention, cree_a) if cree_a is not None else intention
    echeance = min(depuis + timedelta(hours=ECHEANCES_H[pas_long]), limite)
    echeance_h = (echeance - depuis).total_seconds() / 3600.0
    _ajouter_journal_creations(chemins["creations"], {"go": go_id, "creation": True, "etiquette": jeton, "identifiant": ident,
                                                      "created": serveur.get("created"), "depuis": depuis.isoformat(),
                                                      "echeance": echeance.isoformat()})
    controler = controler or (lambda mi, dormir: attendre_minuterie(mi, dormir=dormir, processus=mi.get("_processus")))
    try:
        minuterie = lancer(identifiant=ident, pas=pas, depuis=depuis, echeance_h=echeance_h, taux=taux, deja=deja["retenu"],
                           jeton=jeton, go_id=go_id, lieu=lieu, prix_usd_h=prix_usd, dossier=chemins["verse"],
                           racine=chemins["racine"])
        survie = controler(minuterie, dormir)
        if not (survie["vivante"] and survie["garder"]):
            raise GardeArret(f"minuterie morte ou muette au démarrage ({survie['motif']})")
    except Exception as e:  # noqa: BLE001 — pas de serveur sans minuterie vivante
        detruire_par_identifiant(client, ident, NOM_MACHINE, journal, dormir, essais_max=essais_max, solder=solder)
        raise GardeArret(f"minuterie non armée ({type(e).__name__}: {str(e)[:200]}) : serveur {ident} détruit par son "
                         "identifiant") from None
    public = {"pid": minuterie.get("pid")}
    public.update({k: _relatif(minuterie[k], chemins["racine"]) for k in ("fichier_pid", "journal", "sortie")
                   if k in minuterie})
    return {"identifiant": ident, "depuis": depuis.isoformat(), "echeance": echeance.isoformat(), "echeance_h": echeance_h,
            "minuterie": public, "survie": survie, "rattrapage": rattrapage.name, "empreinte_rattrapage": empreinte,
            "taches_mere": [t.get("heure") for t in prep.get("taches_mere", [])],
            "suite": "verifier-minuterie avec --journal-minuterie dans la minute ; garde-poste puis poussée du journal des "
                     "créations, du fichier PID, du journal et de la sortie de la minuterie ; donner à Lazar l'identifiant, "
                     "l'échéance et le PID"}


def adresse_serveur(client, ident: int) -> dict:
    """Lecture seule : adresse IPv4 publique du serveur de l'essai, pour SSH ; à ne verser nulle part."""
    s = client.serveur(int(ident))
    if s is None:
        raise GardeArret(f"serveur {ident} absent")
    if s.get("name") != NOM_MACHINE:
        raise GardeArret(f"serveur {ident} nommé {s.get('name')!r} : seul {NOM_MACHINE!r} est lu (R10)")
    ip = ((s.get("public_net") or {}).get("ipv4") or {}).get("ip")
    if not isinstance(ip, str) or not ip:
        raise GardeArret(f"adresse IPv4 publique du serveur {ident} illisible")
    return {"identifiant": int(ident), "ipv4": ip, "note": "adresse du serveur loué, pour SSH ; à ne verser nulle part"}


def donnees_du_poste(ip_poste: str, racine) -> dict:
    """CLC5-07 : motifs de ce qui ne doit jamais être versé ni poussé depuis le poste (son adresse IPv4, son dossier
    personnel, le chemin du clone). Seule leur nature est jamais rendue, jamais leur valeur."""
    try:
        ipaddress.IPv4Address(ip_poste)
    except ValueError:
        raise GardeArret("adresse du poste : une adresse IPv4 seule attendue") from None
    motifs = {"adresse IPv4 du poste": re.compile(r"(?<![\d.])" + re.escape(ip_poste) + r"(?![\d])")}
    trois = ip_poste.rsplit(".", 1)[0]
    motifs["réseau /24 du poste"] = re.compile(r"(?<![\d.])" + re.escape(trois) + r"\.\d{1,3}(?![\d])")
    for nature, brut in (("dossier personnel", str(Path.home())), ("chemin du clone", str(Path(racine).resolve()))):
        if len(brut) >= 6 and brut not in ("/root", "/home"):
            motifs[nature] = re.compile(re.escape(brut))
    return motifs


def garde_poste(textes: dict, motifs: dict) -> list[list[str]]:
    """[texte, nature] pour chaque texte qui porte une donnée du poste ; vide si rien."""
    return [[nom, nature] for nom, t in textes.items() for nature, m in motifs.items() if m.search(t)]


# ---- ligne de commande -------------------------------------------------------------------------------------------------------

def _sans_detache(argv: list[str]) -> list[str]:
    sortie, sauter = [], False
    for x in argv:
        if sauter:
            sauter = False
        elif x == "--sortie":
            sauter = True
        elif x != "--detache" and not x.startswith("--sortie="):
            sortie.append(x)
    return sortie


def lancer_detache(argv: list[str], sortie, racine: Path, popen=subprocess.Popen) -> dict:
    """CLC4-04 : la commande tourne dans une session à elle (aucun outil ne la coupe au milieu du rattrapage), sorties dans un
    fichier neuf (R12) ; ce qui est rendu ne porte aucun chemin du poste (CLC5-07)."""
    sortie = Path(sortie)
    if sortie.exists():
        raise GardeArret(f"{sortie.name} existe déjà (R12) : nom neuf exigé")
    cmd = [sys.executable, "-B", "-m", MODULE, *_sans_detache(argv)]
    env = dict(os.environ, PYTHONPATH=str(Path(__file__).resolve().parents[2]))
    sortie.parent.mkdir(parents=True, exist_ok=True)
    with open(sortie, "xb") as f:
        p = popen(cmd, stdin=subprocess.DEVNULL, stdout=f, stderr=subprocess.STDOUT, start_new_session=True, env=env,
                  cwd=str(racine))
    return {"pid": p.pid, "sortie": _relatif(sortie, racine),
            "suite": "attendre la fin du processus (kill -0 PID), puis lire la sortie ; toute fin anormale : detruire --pas d1a "
                     "tout de suite, puis 15 minutes plus tard"}


def construire_analyseur() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Création liée au devis, garde-fous de destruction (A13), v7", allow_abbrev=False)
    sous = ap.add_subparsers(dest="action", required=True)

    def sp(nom):
        p = sous.add_parser(nom, allow_abbrev=False)
        p.add_argument("--depot", help="racine du clone (par défaut : déduite de l'emplacement du module)")
        return p
    p = sp("preparer")
    p.add_argument("--go", required=True)
    p.add_argument("--heure-limite-creation", required=True)
    p.add_argument("--heure-tache-mere", required=True)
    p.add_argument("--pas", choices=sorted(PAS_LONGS), default="d1a")
    for nom in ("acces-creer", "acces-couper", "acces-supprimer"):
        p = sp(nom)
        p.add_argument("--rattrapage", required=True)
        if nom != "acces-supprimer":
            p.add_argument("--ip-poste", required=True, help="en mémoire seulement : jamais écrite dans un fichier versé")
            p.add_argument("--prefixe-poste", type=int, default=32,
                           help=f"source SSH IP_POSTE/P, {PREFIXE_POSTE_MIN} ≤ P ≤ 32 (mesuré par adresses-sortie)")
        if nom == "acces-creer":
            p.add_argument("--cle-publique", required=True, help="fichier .pub (jamais la clé privée)")
    c = sp("creer-et-armer")
    c.add_argument("--go", required=True)
    c.add_argument("--rattrapage", required=True)
    c.add_argument("--empreinte-mere", required=True, help="sha256 du fichier de rattrapage lu par la mère (mot « armée »)")
    c.add_argument("--type", required=True)
    c.add_argument("--image", default="ubuntu-24.04")
    c.add_argument("--lieu", required=True)
    c.add_argument("--taux-usd-eur", type=float, help="ne peut que relever le taux fixé dans le code (1,25)")
    c.add_argument("--deja-depense-usd", type=float)
    c.add_argument("--journal", required=True)
    c.add_argument("--detache", action="store_true")
    c.add_argument("--sortie")
    v = sp("veiller")
    v.add_argument("--identifiant", type=int, required=True)
    v.add_argument("--pas", choices=sorted(PAS_LONGS), default="d1a")
    v.add_argument("--depuis", required=True, help="heure ISO de l'intention ; la création lue, si plus tôt, la remplace")
    v.add_argument("--echeance-h", type=float, help="plus courte que celle du pas, jamais plus longue")
    v.add_argument("--taux-usd-eur", type=float)
    v.add_argument("--deja-depense-usd", type=float, default=0.0)
    v.add_argument("--lieu")
    v.add_argument("--prix-usd-h", type=float)
    v.add_argument("--go")
    v.add_argument("--etiquette")
    v.add_argument("--journal", required=True)
    d = sp("detruire")
    g = d.add_mutually_exclusive_group(required=True)
    g.add_argument("--identifiant", type=int)
    g.add_argument("--etiquette")
    g.add_argument("--pas", choices=sorted(PAS_LONGS))
    d.add_argument("--journal")
    d.add_argument("--duree-max-s", type=float, default=DUREE_MAX_COMMANDE_S)
    k = sp("verifier-coupure")
    k.add_argument("--serveur", type=int, required=True)
    k.add_argument("--pare-feu", type=int, required=True)
    k.add_argument("--journal", required=True)
    i = sp("inventaire")
    i.add_argument("--pas", choices=sorted(PAS_LONGS), default="d1a")
    i.add_argument("--duree-max-s", type=float, default=DUREE_MAX_COMMANDE_S)
    r = sp("adresse-serveur")
    r.add_argument("--identifiant", type=int, required=True)
    q = sp("garde-poste")
    q.add_argument("--ip-poste", required=True, help="en mémoire seulement")
    q.add_argument("--fichier", action="append", help="fichiers à lire ; par défaut, l'index git (git diff --cached)")
    e = sp("adresses-sortie")
    e.add_argument("--ip-poste", required=True, help="en mémoire seulement")
    e.add_argument("--essais", type=int, default=ESSAIS_ADRESSE)
    e.add_argument("--service", default=SERVICE_ADRESSE, help="service qui renvoie l'adresse vue, en texte")
    w = sp("verifier-minuterie")
    w.add_argument("--fichier-pid", required=True)
    w.add_argument("--journal-minuterie")
    return ap


def _executer(a, argv, client, dormir, horloge, popen, controler, verifier_pousse):
    racine = racine_depot(a.depot)
    if a.action == "verifier-minuterie":
        res = verifier_minuterie(Path(a.fichier_pid), horloge=horloge,
                                 journal_minuterie=Path(a.journal_minuterie) if a.journal_minuterie else None)
        print(json.dumps(res, ensure_ascii=False))
        return 0 if res["conforme"] else 1
    if a.action == "adresses-sortie":
        res = adresses_sortie(a.ip_poste, a.essais, service=a.service)
        print(json.dumps(res, ensure_ascii=False))
        return 0 if res["prefixe_conseille"] is not None else 1
    if a.action == "garde-poste":
        motifs = donnees_du_poste(a.ip_poste, racine)
        if a.fichier:
            textes = {Path(f).name: Path(f).read_text(encoding="utf-8", errors="replace") for f in a.fichier}
        else:
            lu = subprocess.run(["git", "-C", str(racine), "diff", "--cached", "--no-color"], capture_output=True, text=True,
                                timeout=60)
            if lu.returncode != 0:
                raise GardeArret("lecture de l'index git impossible (git diff --cached)")
            textes = {"index git (git diff --cached)": lu.stdout}
        trouves = garde_poste(textes, motifs)
        print(json.dumps({"conforme": not trouves, "trouves": trouves, "controles": sorted(motifs)}, ensure_ascii=False))
        return 0 if not trouves else 1
    if a.action == "creer-et-armer" and a.detache:
        if not a.sortie:
            raise GardeArret("--detache exige --sortie FICHIER (nom neuf)")
        print(json.dumps(lancer_detache(argv, a.sortie, racine, popen), ensure_ascii=False))
        return 0
    client = client or ClientHetzner5()
    j = open(a.journal, "a", encoding="utf-8") if getattr(a, "journal", None) else None
    try:
        if a.action == "preparer":
            res = preparer(go_id=a.go, chemins=chemins_depot(racine), heure_limite_creation=_heure(a.heure_limite_creation),
                           heure_tache_mere=_heure(a.heure_tache_mere), pas=a.pas, horloge=horloge)
        elif a.action.startswith("acces-"):
            c = chemins_depot(racine)
            prep = lire_rattrapage(a.rattrapage)
            if a.action == "acces-creer":
                res = creer_acces(client, prep, Path(a.cle_publique).read_text(encoding="utf-8"), a.ip_poste, c["verse"],
                                  horloge, prefixe=a.prefixe_poste)
            elif a.action == "acces-couper":
                res = couper_acces(client, prep, c["verse"], a.ip_poste, prefixe=a.prefixe_poste)
            else:
                res = supprimer_acces(client, prep, c["verse"])
        elif a.action == "creer-et-armer":
            res = creer_et_armer(client, go_id=a.go, chemins=chemins_depot(racine), rattrapage=Path(a.rattrapage),
                                 empreinte_mere=a.empreinte_mere, type_serveur=a.type, image=a.image, lieu=a.lieu,
                                 taux_declare=a.taux_usd_eur, deja_declare=a.deja_depense_usd, journal=j, dormir=dormir,
                                 horloge=horloge, controler=controler, verifier_pousse=verifier_pousse or fichier_pousse)
        elif a.action == "veiller":
            c = chemins_depot(racine, exiger=False)
            solder = fabrique_solder(c["creations"], horloge, a.go, a.etiquette) if (a.go and a.etiquette) else None
            res = demarrer_et_veiller(client, identifiant=a.identifiant, pas=a.pas, depuis=_heure(a.depuis),
                                      echeance_h=a.echeance_h, taux_declare=a.taux_usd_eur, deja=a.deja_depense_usd,
                                      lieu=a.lieu, prix_usd_h=a.prix_usd_h, journal=j, solder=solder, horloge=horloge,
                                      dormir=dormir)
        elif a.action == "inventaire":
            res = inventaire_essai(client, a.pas, j, dormir_borne(dormir, a.duree_max_s))
        elif a.action == "adresse-serveur":
            res = adresse_serveur(client, a.identifiant)
        elif a.action == "detruire":
            borne = dormir_borne(dormir, a.duree_max_s)
            solder = fabrique_solder(chemins_depot(racine, exiger=False)["creations"], horloge)
            if a.identifiant is not None:
                res = detruire_par_identifiant(client, a.identifiant, NOM_MACHINE, j, borne, solder=solder)
            elif a.etiquette is not None:
                res = {"detruits": rattraper_par_etiquette(client, a.etiquette, j, borne, fenetre_s=0.0, solder=solder)}
            else:
                res = detruire_pas(client, a.pas, j, borne, solder=solder)
        else:
            res = verifier_coupure_nuage(client, a.pare_feu, a.serveur)
            res["regles"] = masquer_regles(res.get("regles"))   # CLC5-07 : aucune adresse du poste au journal
            _ecrire(j, {"verification_coupure": res})
        _ecrire(j, {"resultat": res})
    except GardeArret as e:
        _ecrire(j, {"arret": type(e).__name__, "motif": masquer_texte(str(e), racine)[:400]})
        raise
    finally:
        if j is not None:
            j.close()
    print(json.dumps(res, ensure_ascii=False, default=str))
    return 0


def main(argv=None, client=None, dormir=time.sleep, horloge=maintenant_utc, popen=subprocess.Popen, controler=None,
         verifier_pousse=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    a = construire_analyseur().parse_args(argv)
    racine = racine_depot(a.depot)
    try:
        return _executer(a, argv, client, dormir, horloge, popen, controler, verifier_pousse)
    except DestructionRefusee as e:
        sys.stderr.write(f"DESTRUCTION REFUSÉE DURABLEMENT (code {CODE_DESTRUCTION_REFUSEE}) : {masquer_texte(str(e), racine)}\n")
        return CODE_DESTRUCTION_REFUSEE
    except RattrapageARefaire as e:
        sys.stderr.write(f"RATTRAPAGE À REFAIRE (code {CODE_RATTRAPAGE}) : {masquer_texte(str(e), racine)}\n")
        return CODE_RATTRAPAGE
    except PannePassagere as e:
        sys.stderr.write(f"PANNE PASSAGÈRE (code {CODE_PANNE}) : {masquer_texte(str(e), racine)}\n")
        return CODE_PANNE
    except GardeArret as e:
        sys.stderr.write(f"ARRÊT (code {CODE_REFUS}) : {masquer_texte(str(e), racine)}\n")
        return CODE_REFUS
    except Exception:  # noqa: BLE001 — trace écrite, chemins du poste masqués (CLC5-07)
        sys.stderr.write("ERREUR INATTENDUE (code 1) :\n" + masquer_texte(traceback.format_exc(), racine))
        return CODE_REFUS


if __name__ == "__main__":
    sys.exit(main())
