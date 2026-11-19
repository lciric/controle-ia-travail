#!/usr/bin/env python3
"""Enveloppe de conservation des réponses brutes — version 1 (course d'auto-conception, lanceur v9, additif v2i).

Règle de Lazar (R-3661) : « il faut TOUJOURS récupérer ce qui est récupérable ». Cette enveloppe est mise par le lanceur v9
(`envelopper_commandes`) devant chaque commande externe de la course (Argon proposeur et juge, Carbon synchrone, la commande
d'Astra), à l'intérieur de la garde de crédit v5 :

    python3 -I -B garde_credit_relais_v5.py DOSSIER_DES_ARRETS ETIQUETTE -- \
        python3 -I -B enveloppe_conservation_reponses_v1.py DOSSIER_DE_CONSERVATION ETIQUETTE -- COMMANDE ARGS…

Elle ne change rien au réglage de la commande enveloppée (les enveloppes épinglées d'Argon et de Carbon et la commande d'Astra
restent exactement celles que le lanceur contrôle) : elle passe l'entrée standard (la consigne) à la commande, avec
l'environnement tel quel, attend sa fin, puis, **avant de rendre la réponse**, écrit dans DOSSIER_DE_CONSERVATION (tenu par le
lanceur : il le crée, hors des dossiers de sessions ; l'enveloppe ne le crée jamais) une copie **octet pour octet** :
- de la sortie standard de la commande (la réponse brute rendue : la ligne JSON `{"texte", "cout_usd", "modele_servi", …}`) ;
- de sa sortie d'erreur ;
- de ses en-têtes techniques (JSON : étiquette, rôle `ROLE_POLE`, modèle demandé `MODELE_DEMANDE_POLE`, plafond
  `PLAFOND_SESSION_USD`, lot, numéro d'appel, horodatage, durée, code de sortie, tailles et empreintes SHA-256 de la consigne,
  de la sortie et de la sortie d'erreur, commande lancée — aucune valeur de clé : l'environnement n'est jamais recopié).

Nommage : un dossier par appel, réservé de façon exclusive (`ETIQUETTE-appel-NNNN`, `mkdir` atomique : deux appels
simultanés ne prennent jamais le même numéro), et dedans
`ETIQUETTE-appel-NNNN-lot-LL-HORODATAGE-reponse.bin`, `…-erreur.bin`, `…-entetes.json` (lot lu dans la consigne :
« Lot k sur n du catalogue » ; « sans-lot » pour un juge). Écriture atomique : fichier temporaire du même dossier, `fsync`,
lien dur vers le nom final (jamais d'écrasement), retrait du temporaire, `fsync` du dossier ; les en-têtes sont écrits en
dernier (leur présence dit l'appel complet).

Aucun repli silencieux (R5) :
- dossier de conservation absent, pas un dossier ou non inscriptible : **refus avant tout appel** (code 2, ligne JSON
  `{"texte": "", "cout_usd": 1e-06, "erreur": …}` : rien n'est lancé, rien n'est dépensé) ;
- écriture impossible après l'appel : **l'appel est arrêté** — la réponse n'est pas rendue ; code 9 ; la dernière ligne de la
  sortie standard porte le coût que la commande a déclaré (`cout_usd`, s'il est lisible : la dépense est comptée par
  l'orchestrateur) et l'erreur ; si le coût n'est pas lisible, rien n'est imprimé sur la sortie standard et l'orchestrateur
  compte le plafond de session (`cout_inconnu`).
Sinon : la sortie standard et la sortie d'erreur de la commande sont rendues telles quelles, et son code.

Bibliothèque standard seulement. Aucun appel réseau par elle-même.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time

VERSION = "enveloppe_conservation_reponses_v1"
CODE_REFUS = 2
CODE_ECRITURE_IMPOSSIBLE = 9
MOTIF_LOT = re.compile(rb"Lot (\d{1,3}) sur (\d{1,3}) du catalogue")
ETIQUETTE_PERMISE = re.compile(r"^[a-z][a-z0-9_-]{0,31}$")
VARIABLES_LUES = ("ROLE_POLE", "MODELE_DEMANDE_POLE", "PLAFOND_SESSION_USD")
MAX_APPELS = 100000


class EcritureImpossible(OSError):
    """Écriture de conservation impossible : l'appel est arrêté."""


def _ligne(objet: dict) -> bytes:
    return (json.dumps(objet, ensure_ascii=False) + "\n").encode("utf-8")


def refuser(motif: str) -> int:
    sys.stdout.buffer.write(_ligne({"texte": "", "cout_usd": 1e-06, "erreur": f"{VERSION} : {motif}"}))
    sys.stdout.flush()
    return CODE_REFUS


def lot_de(consigne: bytes) -> str:
    m = MOTIF_LOT.search(consigne)
    return f"{int(m.group(1)):02d}" if m else "sans-lot"


def cout_declare(sortie: bytes):
    """Le `cout_usd` de la dernière ligne JSON non vide de la sortie (contrat de la commande externe), s'il est fini et > 0."""
    lignes = [l for l in sortie.decode("utf-8", "replace").splitlines() if l.strip()]
    try:
        o = json.loads(lignes[-1]) if lignes else None
    except ValueError:
        return None
    c = o.get("cout_usd") if isinstance(o, dict) else None
    if isinstance(c, bool) or not isinstance(c, (int, float)) or not math.isfinite(c) or c <= 0:
        return None
    return float(c)


def reserver_appel(dossier: str, etiquette: str) -> tuple:
    """Réserve `ETIQUETTE-appel-NNNN` par `mkdir` exclusif ; rend (numéro, chemin)."""
    for n in range(1, MAX_APPELS):
        d = os.path.join(dossier, f"{etiquette}-appel-{n:04d}")
        try:
            os.mkdir(d, 0o700)
            return n, d
        except FileExistsError:
            continue
    raise EcritureImpossible(f"aucun numéro d'appel libre sous {dossier}")


def _fsync_dossier(dossier: str) -> None:
    fd = os.open(dossier, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def ecrire_atomique(dossier: str, nom: str, donnees: bytes) -> str:
    """Temporaire du même dossier, fsync, lien dur vers le nom final (jamais d'écrasement), retrait du temporaire."""
    final = os.path.join(dossier, nom)
    tmp = os.path.join(dossier, f".{nom}.{os.getpid()}.tmp")
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        vue = memoryview(donnees)
        while vue:
            k = os.write(fd, vue)
            vue = vue[k:]
        os.fsync(fd)
    finally:
        os.close(fd)
    try:
        os.link(tmp, final)
    finally:
        os.unlink(tmp)
    _fsync_dossier(dossier)
    with open(final, "rb") as f:
        if hashlib.sha256(f.read()).hexdigest() != hashlib.sha256(donnees).hexdigest():
            raise EcritureImpossible(f"{final} relu d'une autre empreinte")
    return final


def conserver(dossier: str, etiquette: str, commande: list, consigne: bytes, p, debut: _dt.datetime, duree_s: float) -> dict:
    n, d = reserver_appel(dossier, etiquette)
    lot = lot_de(consigne)
    horo = debut.strftime("%Y%m%dT%H%M%S%fZ")
    base = f"{etiquette}-appel-{n:04d}-lot-{lot}-{horo}"
    f_rep = ecrire_atomique(d, base + "-reponse.bin", p.stdout)
    f_err = ecrire_atomique(d, base + "-erreur.bin", p.stderr)
    entetes = {"version": VERSION, "etiquette": etiquette, "appel": n, "lot": lot, "horodatage_debut_utc": debut.isoformat(),
               "duree_s": round(duree_s, 3), "code_commande": p.returncode,
               "environnement_lu": {v: os.environ.get(v) for v in VARIABLES_LUES},
               "commande": list(commande),
               "consigne": {"octets": len(consigne), "sha256": hashlib.sha256(consigne).hexdigest()},
               "reponse": {"fichier": os.path.basename(f_rep), "octets": len(p.stdout), "sha256": hashlib.sha256(p.stdout).hexdigest()},
               "erreur": {"fichier": os.path.basename(f_err), "octets": len(p.stderr), "sha256": hashlib.sha256(p.stderr).hexdigest()},
               "cout_declare_usd": cout_declare(p.stdout)}
    f_ent = ecrire_atomique(d, base + "-entetes.json", (json.dumps(entetes, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
    return {"dossier": d, "reponse": f_rep, "erreur": f_err, "entetes": f_ent}


def principal(argv: list) -> int:
    if len(argv) < 4 or argv[2] != "--":
        return refuser("usage DOSSIER_DE_CONSERVATION ETIQUETTE -- COMMANDE ARGS…")
    dossier, etiquette, commande = argv[0], argv[1], argv[3:]
    if not ETIQUETTE_PERMISE.match(etiquette):
        return refuser(f"étiquette {etiquette!r} non admise ([a-z][a-z0-9_-]*)")
    if not os.path.isabs(dossier) or not os.path.isdir(dossier) or os.path.islink(dossier):
        return refuser(f"dossier de conservation {dossier!r} absent, relatif, lien ou pas un dossier (il est tenu par le lanceur) : "
                       "rien n'est lancé")
    if not os.access(dossier, os.W_OK | os.X_OK):
        return refuser(f"dossier de conservation {dossier!r} non inscriptible : rien n'est lancé")
    consigne = sys.stdin.buffer.read()
    debut = _dt.datetime.now(_dt.timezone.utc)
    t0 = time.monotonic()
    p = subprocess.run(commande, input=consigne, capture_output=True)
    duree = time.monotonic() - t0
    try:
        conserver(dossier, etiquette, commande, consigne, p, debut, duree)
    except Exception as e:  # noqa: BLE001 — toute erreur d'écriture arrête l'appel, jamais en silence
        message = f"{VERSION} : conservation impossible ({type(e).__name__} : {e}) — appel arrêté, réponse non rendue"
        sys.stderr.buffer.write((message + "\n").encode("utf-8"))
        sys.stderr.flush()
        c = cout_declare(p.stdout)
        if c is not None:
            sys.stdout.buffer.write(_ligne({"texte": "", "cout_usd": c, "erreur": message}))
            sys.stdout.flush()
        return CODE_ECRITURE_IMPOSSIBLE
    sys.stdout.buffer.write(p.stdout)
    sys.stdout.flush()
    sys.stderr.buffer.write(p.stderr)
    sys.stderr.flush()
    return p.returncode if p.returncode >= 0 else 128 - p.returncode   # commande tuée par un signal : 128 + numéro


if __name__ == "__main__":
    raise SystemExit(principal(sys.argv[1:]))
