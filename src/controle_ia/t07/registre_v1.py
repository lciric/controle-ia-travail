"""Lignes de registre de T0.7 (brouillon 7, section « Lignes de registre ») et garde d'ouverture, v1.

Format exact, celui de `scripts/controle_lecture_t06_v1.py` (`lire_registre`, branche `origin/prep/t06-candidat8-v1`,
sha256 `ba2ba5cfe7484e7e30bb74e44420b46c9939dd5613bbb961b9725c3d46343c07`) : une ligne de table Markdown à quatre cellules,
**exactement une** par clé,

    | CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin/relatif/depuis/la/racine | sha256 (64 caractères hexadécimaux) |

date en UTC au format strict, chemin relatif sans « .. », empreinte égale à celle du fichier **et** à son compagnon
`.sha256`. Les contrôles de forme sont recopiés de `lire_registre` (mêmes motifs `SHA` et `DATE`, mêmes refus) ; la seule
différence est l'ensemble des clés cherchées, passé en argument (clés obligatoires et clés facultatives : une clé facultative
absente est rendue absente, jamais inventée ; en double, mal formée ou non antérieure, elle est refusée comme une obligatoire).

Refus (`RefusRegistre`, une `GardeArret` ; code 2 en ligne de commande, motif écrit, **aucune ouverture**) : registre absent ;
ligne obligatoire absente ; ligne en double ; mal formée ; fichier cité absent, empreinte différente de la ligne, compagnon
`.sha256` absent ou différent ; date non **strictement antérieure** à l'instant d'ouverture.

Exception de format déclarée : la ligne `GO-LECTURE-T07` porte le chemin de `registres/go.md` et le sha256 **de la ligne exacte
du GO cité** (texte UTF-8 de la ligne, sans son saut de ligne final), non du fichier (brouillon 7, table des lignes) ; les
registres vivants n'ont pas de compagnon `.sha256` (`scellement.DOSSIERS_SCELLES`). Sa vérification cherche donc une ligne du
fichier d'empreinte égale ; aucune → refus.
"""
from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret

SHA = re.compile(r"[0-9a-f]{64}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
FORMAT_DATE = "%Y-%m-%dT%H:%M:%SZ"

# Clés du brouillon 7 (table « Lignes de registre »).
SCELLEMENT_T07 = "SCELLEMENT-T07"
SCELLEMENT_P3BIS = "SCELLEMENT-P3BIS"
VERDICT_P3BIS = "VERDICT-P3BIS"
RUN_CONFIRMATION_T06 = "RUN-CONFIRMATION-T06"
SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC, SCELLEMENT_JEUX_JA = ("SCELLEMENT-JEUX-T07-JD", "SCELLEMENT-JEUX-T07-JC",
                                                             "SCELLEMENT-JEUX-T07-JA")
SCELLEMENT_CONCEPTS_T07 = "SCELLEMENT-CONCEPTS-T07"
GO_LECTURE_T07 = "GO-LECTURE-T07"
ISSUE_MOTS_ET_COUT_T06 = "ISSUE-MOTS-ET-COUT-T06"
CODE_T07 = "CODE-T07"
LIGNES_SHA_DE_LIGNE = (GO_LECTURE_T07,)          # empreinte d'une ligne du fichier, pas du fichier

# Étape A (notation scellée) : obligatoires et facultatives (brouillon 7, plan, point 8, étape A (1)).
OBLIGATOIRES_ETAPE_A = (RUN_CONFIRMATION_T06, SCELLEMENT_JEUX_JD, SCELLEMENT_CONCEPTS_T07, GO_LECTURE_T07)
FACULTATIVES_ETAPE_A = (SCELLEMENT_JEUX_JC, SCELLEMENT_JEUX_JA, CODE_T07, SCELLEMENT_T07)
# Étape B (lecture mécanique) : les lignes de P3-bis sont lues par L0 (absentes → L0a, jamais un refus) ; l'issue « mots et
# coût » peut manquer (qualification « en attente de T0.6 »).
OBLIGATOIRES_ETAPE_B = (RUN_CONFIRMATION_T06,)
FACULTATIVES_ETAPE_B = (SCELLEMENT_P3BIS, VERDICT_P3BIS, ISSUE_MOTS_ET_COUT_T06, SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC,
                        SCELLEMENT_JEUX_JA, SCELLEMENT_CONCEPTS_T07, GO_LECTURE_T07, CODE_T07, SCELLEMENT_T07)


class RefusRegistre(GardeArret):
    """Refus de la garde d'ouverture : aucune ouverture, motif écrit (code 2 en ligne de commande)."""


def sha256_de(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def instant_utc(date: str) -> int:
    """Secondes depuis l'époque d'une date `AAAA-MM-JJTHH:MM:SSZ` (format strict, UTC)."""
    if not DATE.fullmatch(date):
        raise RefusRegistre(f"date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
    try:
        return int(datetime.strptime(date, FORMAT_DATE).replace(tzinfo=timezone.utc).timestamp())
    except ValueError:
        raise RefusRegistre(f"date {date!r} impossible") from None


def date_utc(instant: int) -> str:
    return datetime.fromtimestamp(int(instant), timezone.utc).strftime(FORMAT_DATE)


def sceau_conforme(chemin: Path, attendu: str | None = None) -> str:
    """Empreinte du fichier, après vérification de son compagnon `.sha256` (première colonne) ; `attendu` : empreinte exigée.
    Recopie de `controle_lecture_t06_v1.sceau_conforme` (`ba2ba5cf…`), exception `RefusRegistre`."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise RefusRegistre(f"{chemin} absent")
    sha = sha256_de(chemin)
    comp = Path(str(chemin) + ".sha256")
    if not comp.is_file():
        raise RefusRegistre(f"{chemin} : compagnon .sha256 absent")
    lu = (comp.read_text(encoding="utf-8").split() or [""])[0]
    if lu != sha:
        raise RefusRegistre(f"{chemin} : compagnon .sha256 ({lu[:12]}…) ≠ empreinte du fichier ({sha[:12]}…)")
    if attendu is not None and sha != attendu:
        raise RefusRegistre(f"{chemin} : empreinte {sha[:12]}… ≠ celle du registre ({attendu[:12]}…)")
    return sha


def sha256_de_la_ligne(ligne: str) -> str:
    """Empreinte d'une ligne de texte (UTF-8, sans saut de ligne final) : format de la ligne `GO-LECTURE-T07`."""
    return hashlib.sha256(ligne.rstrip("\r\n").encode("utf-8")).hexdigest()


def ligne_d_empreinte(chemin: Path, attendu: str) -> str:
    """La ligne du fichier dont l'empreinte (`sha256_de_la_ligne`) vaut `attendu` ; aucune → refus."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise RefusRegistre(f"{chemin} absent")
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        if sha256_de_la_ligne(ligne) == attendu:
            return ligne
    raise RefusRegistre(f"{chemin} : aucune ligne d'empreinte {attendu[:12]}… (ligne du GO cité par GO-LECTURE-T07)")


def lire_registre(registre: Path, obligatoires, facultatives=()) -> dict:
    """Lignes du registre, clé → (instant, date, chemin, sha). Contrôles de forme de `controle_lecture_t06_v1.lire_registre`
    (`ba2ba5cf…`), appliqués à chaque clé cherchée ; une obligatoire absente refuse, une facultative absente n'est pas rendue."""
    registre = Path(registre)
    obligatoires, facultatives = tuple(obligatoires), tuple(facultatives)
    if set(obligatoires) & set(facultatives):
        raise RefusRegistre(f"clés à la fois obligatoires et facultatives : {sorted(set(obligatoires) & set(facultatives))}")
    if not registre.is_file():
        raise RefusRegistre(f"registre {registre} absent")
    trouvees: dict = {k: [] for k in obligatoires + facultatives}
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if cellules and cellules[0] in trouvees:
            trouvees[cellules[0]].append(cellules)
    sortie = {}
    for k, lignes in trouvees.items():
        if len(lignes) == 0 and k in facultatives:
            continue
        if len(lignes) != 1:
            raise RefusRegistre(f"registre : {len(lignes)} ligne(s) {k}, exactement une attendue")
        c = lignes[0]
        if len(c) != 4:
            raise RefusRegistre(f"registre : ligne {k} mal formée ({len(c)} colonnes, 4 attendues)")
        _, date, chemin, sha = c
        if not DATE.fullmatch(date):
            raise RefusRegistre(f"registre : ligne {k} : date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
        if not SHA.fullmatch(sha):
            raise RefusRegistre(f"registre : ligne {k} : empreinte {sha!r} (64 caractères hexadécimaux attendus)")
        if not chemin or chemin.startswith("/") or ".." in Path(chemin).parts:
            raise RefusRegistre(f"registre : ligne {k} : chemin {chemin!r} (relatif à la racine, sans « .. » attendu)")
        try:
            instant = instant_utc(date)
        except RefusRegistre:
            raise RefusRegistre(f"registre : ligne {k} : date {date!r} impossible") from None
        sortie[k] = (instant, date, chemin, sha)
    return sortie


def verifier_lignes(lignes: dict, racine: Path, instant: int) -> dict:
    """Pour chaque ligne lue : antériorité stricte à `instant` et sceau du fichier cité (ou de la ligne citée, pour
    `GO-LECTURE-T07`). Rend clé → {date, chemin, sha256, verifie}."""
    racine = Path(racine)
    sortie = {}
    for k, (t, date, chemin, sha) in lignes.items():
        if not t < int(instant):
            raise RefusRegistre(f"registre : ligne {k} datée {date}, pas strictement antérieure à l'ouverture ({date_utc(instant)})")
        if k in LIGNES_SHA_DE_LIGNE:
            ligne = ligne_d_empreinte(racine / chemin, sha)
            sortie[k] = {"date": date, "chemin": chemin, "sha256": sha, "verifie": "ligne du fichier", "ligne": ligne}
        else:
            sceau_conforme(racine / chemin, sha)
            sortie[k] = {"date": date, "chemin": chemin, "sha256": sha, "verifie": "fichier et compagnon .sha256"}
    return sortie


def garde_ouverture(registre: Path, racine: Path, obligatoires, facultatives, instant: int) -> dict:
    """Garde d'ouverture : lecture du registre, antériorité, sceaux ; rend les lignes vérifiées, l'instant et l'empreinte du
    registre. Toute faute refuse avant toute ouverture (R5 : cas sain et artefact dans les essais)."""
    lignes = lire_registre(registre, obligatoires, facultatives)
    verifiees = verifier_lignes(lignes, racine, instant)
    return {"registre": str(registre), "registre_sha256": sha256_de(registre), "instant": date_utc(instant),
            "obligatoires": list(obligatoires), "facultatives_presentes": [k for k in facultatives if k in verifiees],
            "facultatives_absentes": [k for k in facultatives if k not in verifiees], "lignes": verifiees}


def journaliser_ouverture(registre: Path, instant: int, quoi: str, empreinte_objet: str) -> Path:
    """Ajoute une ligne au journal `<registre>.ouvertures.md` (comme `controle_lecture_t06_v1.controler`)."""
    journal = Path(str(registre) + ".ouvertures.md")
    with open(journal, "a", encoding="utf-8") as f:
        f.write(f"| OUVERTURE-T07 | {date_utc(instant)} | {quoi} | {empreinte_objet} | registre {sha256_de(registre)} |\n")
    return journal


def ecrire_ligne(cle: str, date: str, chemin: str, sha: str) -> str:
    """Une ligne au format exact (pour les registres factices des essais et les écritures de la session mère)."""
    if not DATE.fullmatch(date) or not SHA.fullmatch(sha):
        raise RefusRegistre(f"ligne {cle} : date ou empreinte hors format")
    return f"| {cle} | {date} | {chemin} | {sha} |"


__all__ = ["RefusRegistre", "lire_registre", "verifier_lignes", "garde_ouverture", "journaliser_ouverture", "sceau_conforme",
           "sha256_de", "sha256_de_la_ligne", "ligne_d_empreinte", "ecrire_ligne", "instant_utc", "date_utc",
           "OBLIGATOIRES_ETAPE_A", "FACULTATIVES_ETAPE_A", "OBLIGATOIRES_ETAPE_B", "FACULTATIVES_ETAPE_B"]
