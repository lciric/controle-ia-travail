"""Contrôle d'ouverture de la lecture des sondes de T0.6 (décision de Lazar R-1654 : T0.6 ne cite plus les empreintes de T0.7 ni de
P3-bis ; « les états des sondes ne sont lus qu'après le scellement de T0.7 et de P3-bis, empreintes inscrites au registre avant toute
lecture »). Bibliothèque standard seule ; aucun réseau, aucune clé ; ne lit jamais le contenu du résultat des sondes (empreinte et
sceau seulement).

Registre : un fichier Markdown portant exactement une ligne de chaque forme (colonnes séparées par « | »)

    | SCELLEMENT-T07 | AAAA-MM-JJTHH:MM:SSZ | chemin/du/preenregistrement-T0.7.md | sha256 |
    | SCELLEMENT-P3BIS | AAAA-MM-JJTHH:MM:SSZ | chemin/du/preenregistrement-P3-bis.md | sha256 |

Le contrôle refuse (code 2, motif sur la sortie, aucune ouverture) si : le registre manque ; une des deux lignes manque, est en double
ou est mal formée (date non UTC, empreinte qui n'a pas 64 caractères hexadécimaux, chemin absolu ou sortant) ; le fichier cité manque,
ou son empreinte n'est pas celle de la ligne ; son compagnon `.sha256` manque ou ne dit pas la même empreinte ; la date d'une ligne n'est
pas **strictement antérieure** à l'instant d'ouverture ; le résultat des sondes manque ou son compagnon `.sha256` est absent ou faux.
Sinon (code 0) : imprime « OUVERTURE AUTORISÉE » et ajoute une ligne au journal d'ouvertures (`<registre>.ouvertures.md` : instant,
empreinte du résultat, empreinte du registre) : l'antériorité des inscriptions sur chaque ouverture se relit dans ce journal.

    python3 -I -B controle_lecture_t06_v1.py REGISTRE RESULTAT_SONDES [RACINE] [INSTANT_UTC_S]

RACINE (défaut : parent du dossier du registre) : racine des chemins cités ; INSTANT_UTC_S : instant d'ouverture (défaut : maintenant ;
n'existe que pour les essais).
"""
from __future__ import annotations

import hashlib
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

LIGNES = ("SCELLEMENT-T07", "SCELLEMENT-P3BIS")
SHA = re.compile(r"[0-9a-f]{64}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")


class Refus(Exception):
    pass


def sha256_de(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def sceau_conforme(chemin: Path, attendu: str | None = None) -> str:
    """Empreinte du fichier, après vérification de son compagnon `.sha256` (première colonne) ; `attendu` : empreinte exigée."""
    if not chemin.is_file():
        raise Refus(f"{chemin} absent")
    sha = sha256_de(chemin)
    comp = Path(str(chemin) + ".sha256")
    if not comp.is_file():
        raise Refus(f"{chemin} : compagnon .sha256 absent")
    lu = (comp.read_text(encoding="utf-8").split() or [""])[0]
    if lu != sha:
        raise Refus(f"{chemin} : compagnon .sha256 ({lu[:12]}…) ≠ empreinte du fichier ({sha[:12]}…)")
    if attendu is not None and sha != attendu:
        raise Refus(f"{chemin} : empreinte {sha[:12]}… ≠ celle du registre ({attendu[:12]}…)")
    return sha


def lire_registre(registre: Path) -> dict:
    if not registre.is_file():
        raise Refus(f"registre {registre} absent")
    trouvees: dict = {k: [] for k in LIGNES}
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if cellules and cellules[0] in trouvees:
            trouvees[cellules[0]].append(cellules)
    sortie = {}
    for k, lignes in trouvees.items():
        if len(lignes) != 1:
            raise Refus(f"registre : {len(lignes)} ligne(s) {k}, exactement une attendue")
        c = lignes[0]
        if len(c) != 4:
            raise Refus(f"registre : ligne {k} mal formée ({len(c)} colonnes, 4 attendues)")
        _, date, chemin, sha = c
        if not DATE.fullmatch(date):
            raise Refus(f"registre : ligne {k} : date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
        if not SHA.fullmatch(sha):
            raise Refus(f"registre : ligne {k} : empreinte {sha!r} (64 caractères hexadécimaux attendus)")
        if not chemin or chemin.startswith("/") or ".." in Path(chemin).parts:
            raise Refus(f"registre : ligne {k} : chemin {chemin!r} (relatif à la racine, sans « .. » attendu)")
        try:
            instant = int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())
        except ValueError:
            raise Refus(f"registre : ligne {k} : date {date!r} impossible") from None
        sortie[k] = (instant, date, chemin, sha)
    return sortie


def controler(registre: Path, resultat: Path, racine: Path, instant=None) -> str:
    maintenant = int(time.time()) if instant is None else int(instant)
    lignes = lire_registre(registre)
    for k, (t, date, chemin, sha) in lignes.items():
        if not t < maintenant:
            raise Refus(f"registre : ligne {k} datée {date}, pas strictement antérieure à l'ouverture ({datetime.fromtimestamp(maintenant, timezone.utc):%Y-%m-%dT%H:%M:%SZ})")
        sceau_conforme(racine / chemin, sha)
    sha_res = sceau_conforme(resultat)
    journal = Path(str(registre) + ".ouvertures.md")
    with open(journal, "a", encoding="utf-8") as f:
        f.write(f"| OUVERTURE-SONDES-T06 | {datetime.fromtimestamp(maintenant, timezone.utc):%Y-%m-%dT%H:%M:%SZ} | {resultat.name} | {sha_res} | registre {sha256_de(registre)} |\n")
    return "OUVERTURE AUTORISÉE : " + " ; ".join(f"{k} {d} {c} {s[:12]}…" for k, (_, d, c, s) in lignes.items()) + f" ; résultat {resultat.name} {sha_res[:12]}…"


def main(argv: list) -> int:
    if not 2 <= len(argv) <= 4:
        print("usage : REGISTRE RESULTAT_SONDES [RACINE] [INSTANT_UTC_S]", file=sys.stderr)
        return 2
    registre, resultat = Path(argv[0]), Path(argv[1])
    racine = Path(argv[2]) if len(argv) > 2 and argv[2] else registre.resolve().parent.parent
    try:
        print(controler(registre, resultat, racine, int(argv[3]) if len(argv) == 4 else None))
    except Refus as e:
        print(f"REFUS : {e}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
