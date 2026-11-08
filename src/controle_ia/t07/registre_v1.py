"""Lignes de registre de T0.7 (brouillon 8, section « Lignes de registre », CLT7B-02, CLT7B-03) et garde d'ouverture, v1.

Registre : **`registres/scellements-v1.md`** (chemin fixé par le brouillon 8 ; créé à la première ligne, jamais réécrit : on y
ajoute des lignes). Format exact, celui de `scripts/controle_lecture_t06_v1.py` (`lire_registre`, branche
`origin/prep/t06-candidat8-v1`, sha256 `ba2ba5cfe7484e7e30bb74e44420b46c9939dd5613bbb961b9725c3d46343c07`) : une ligne de table
Markdown à quatre cellules,

    | CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin/relatif/depuis/la/racine | sha256 (64 caractères hexadécimaux) |

date en UTC au format strict (motif `DATE`), chemin relatif sans « .. », **empreinte du fichier entier cité, égale à son compagnon
`.sha256`** (`sceau_conforme`). Aucune ligne ne porte l'empreinte d'une ligne d'un autre fichier : une ligne de GO cite un **extrait
scellé** (`registres/go-extraits/<CLÉ>-v1.md`, la ligne du GO recopiée à l'octet, avec compagnon), et le module vérifie que l'extrait
est une ligne de `registres/go.md` (texte UTF-8 exact, `extrait_est_une_ligne_de`).

`lire_registre_t07(registre, cles_exigees, cles_permises)` : écrite sur le modèle de `controle_lecture_t06_v1.lire_registre` (mêmes
motifs `DATE` et `SHA`, mêmes textes de refus), essayée contre lui sur les clés communes (`SCELLEMENT-T07`, `SCELLEMENT-P3BIS`) avec
égalité des refus (`tests/test_t07_lecture_v1.py`). Refus (`RefusRegistre`, une `GardeArret` ; code 2 en ligne de commande, rien
ouvert) : registre absent ; ligne exigée absente ; ligne en double ; mal formée ; **clé ni exigée ni permise** (toute ligne de
table dont la première cellule a la forme d'une clé de registre, `CLE`) ; puis, dans `verifier_lignes` : date non **strictement
antérieure** à l'instant d'ouverture ; fichier cité absent, empreinte différente, compagnon absent ou différent. Rend, par clé,
(instant, date, chemin, sha). Chaque ouverture est journalisée dans `<registre>.ouvertures.md`.
"""
from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret

SHA = re.compile(r"[0-9a-f]{64}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
CLE = re.compile(r"[A-Z0-9]+(?:-[A-Z0-9]+)+")           # forme d'une clé de registre (SCELLEMENT-T07, GO-ETAPE-A-T07, …)
FORMAT_DATE = "%Y-%m-%dT%H:%M:%SZ"
REGISTRE_DEFAUT = "registres/scellements-v1.md"
DOSSIER_GO, FICHIER_GO = "registres/go-extraits", "registres/go.md"

SCELLEMENT_T07, SCELLEMENT_P3BIS, VERDICT_P3BIS = "SCELLEMENT-T07", "SCELLEMENT-P3BIS", "VERDICT-P3BIS"
RUN_CONFIRMATION_T06 = "RUN-CONFIRMATION-T06"
SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC, SCELLEMENT_JEUX_JA = ("SCELLEMENT-JEUX-T07-JD", "SCELLEMENT-JEUX-T07-JC",
                                                             "SCELLEMENT-JEUX-T07-JA")
SCELLEMENT_CONCEPTS_T07 = "SCELLEMENT-CONCEPTS-T07"
GO_ETAPE_A_T07, GO_LECTURE_T07 = "GO-ETAPE-A-T07", "GO-LECTURE-T07"
SCORES_T07, SONDES_T07 = "SCORES-T07", "SONDES-T07"
ISSUE_MOTS_ET_COUT_T06 = "ISSUE-MOTS-ET-COUT-T06"
CODE_T07 = "CODE-T07"
LIGNES_GO = (GO_ETAPE_A_T07, GO_LECTURE_T07)
CLES_CONNUES = (SCELLEMENT_T07, SCELLEMENT_P3BIS, VERDICT_P3BIS, RUN_CONFIRMATION_T06, SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC,
                SCELLEMENT_JEUX_JA, SCELLEMENT_CONCEPTS_T07, GO_ETAPE_A_T07, GO_LECTURE_T07, SCORES_T07, SONDES_T07,
                ISSUE_MOTS_ET_COUT_T06, CODE_T07)

# Clés par étape (brouillon 8, « Clés par étape »). Étape A : `GO-ETAPE-A-T07` (étape annexe) ou `GO-LECTURE-T07` (variante B) —
# l'une des deux est exigée, vérifié par `lecture_v1.ouvrir` ; `CODE-T07` exigée seulement si DS-3 bis est accordée (configuration).
# Les clés des autres étapes et de T0.6 sont permises (présentes dans le même registre), jamais lues ici.
EXIGEES_ETAPE_A = (RUN_CONFIRMATION_T06, SCELLEMENT_CONCEPTS_T07)
PERMISES_ETAPE_A = (SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC, SCELLEMENT_JEUX_JA, GO_ETAPE_A_T07, GO_LECTURE_T07, CODE_T07,
                    SCELLEMENT_T07, SCELLEMENT_P3BIS, VERDICT_P3BIS, SCORES_T07, SONDES_T07, ISSUE_MOTS_ET_COUT_T06)
# Étape B : les lignes de P3-bis sont lues par la grille (P = « absente » → L0a) ; `ISSUE-MOTS-ET-COUT-T06` est exigée depuis N-063
# (le filtre des doses en a besoin) ; la règle d'antériorité `SCORES-T07`, `SONDES-T07` < `VERDICT-P3BIS` est tenue par `exiger_anteriorite`.
EXIGEES_ETAPE_B = (RUN_CONFIRMATION_T06, SCORES_T07, SONDES_T07, ISSUE_MOTS_ET_COUT_T06)
PERMISES_ETAPE_B = (SCELLEMENT_P3BIS, VERDICT_P3BIS, SCELLEMENT_JEUX_JD, SCELLEMENT_JEUX_JC, SCELLEMENT_JEUX_JA,
                    SCELLEMENT_CONCEPTS_T07, GO_ETAPE_A_T07, GO_LECTURE_T07, CODE_T07, SCELLEMENT_T07)


class RefusRegistre(GardeArret):
    """Refus de la garde d'ouverture : aucune ouverture, motif écrit (code 2 en ligne de commande)."""


def sha256_de(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def instant_utc(date: str) -> int:
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


def lire_registre_t07(registre: Path, cles_exigees, cles_permises=()) -> dict:
    """Lignes du registre, clé → (instant, date, chemin, sha). Contrôles de forme de `controle_lecture_t06_v1.lire_registre`
    (`ba2ba5cf…`, mêmes textes de refus) ; une exigée absente refuse ; une permise absente n'est pas rendue ; une clé de registre
    ni exigée ni permise refuse."""
    registre = Path(registre)
    exigees, permises = tuple(cles_exigees), tuple(cles_permises)
    if set(exigees) & set(permises):
        raise RefusRegistre(f"clés à la fois exigées et permises : {sorted(set(exigees) & set(permises))}")
    if not registre.is_file():
        raise RefusRegistre(f"registre {registre} absent")
    trouvees: dict = {k: [] for k in exigees + permises}
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if not cellules or not cellules[0]:
            continue
        if cellules[0] in trouvees:
            trouvees[cellules[0]].append(cellules)
        elif CLE.fullmatch(cellules[0]) and len(cellules) == 4 and DATE.fullmatch(cellules[1]):
            raise RefusRegistre(f"registre : ligne {cellules[0]} ni exigée ni permise à cette étape")
    sortie = {}
    for k, lignes in trouvees.items():
        if len(lignes) == 0 and k in permises:
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
            instant = int(datetime.strptime(date, FORMAT_DATE).replace(tzinfo=timezone.utc).timestamp())
        except ValueError:
            raise RefusRegistre(f"registre : ligne {k} : date {date!r} impossible") from None
        sortie[k] = (instant, date, chemin, sha)
    return sortie


def extrait_est_une_ligne_de(extrait: Path, fichier: Path) -> str:
    """L'extrait scellé (une seule ligne non vide, recopiée à l'octet) est une ligne du fichier (texte UTF-8 exact) ; rend la ligne."""
    extrait, fichier = Path(extrait), Path(fichier)
    lignes = [l for l in extrait.read_text(encoding="utf-8").split("\n") if l.strip()]
    if len(lignes) != 1:
        raise RefusRegistre(f"{extrait} : une seule ligne non vide attendue, {len(lignes)} trouvée(s)")
    if not fichier.is_file():
        raise RefusRegistre(f"{fichier} absent")
    if lignes[0] not in fichier.read_text(encoding="utf-8").split("\n"):
        raise RefusRegistre(f"{extrait} : l'extrait n'est pas une ligne de {fichier} (texte UTF-8 exact)")
    return lignes[0]


def verifier_lignes(lignes: dict, racine: Path, instant: int) -> dict:
    """Pour chaque ligne lue : antériorité stricte à `instant` et sceau du fichier cité ; pour une ligne de GO, l'extrait scellé
    doit en plus être une ligne de `registres/go.md`. Rend clé → {date, chemin, sha256, instant, …}."""
    racine = Path(racine)
    sortie = {}
    for k, (t, date, chemin, sha) in lignes.items():
        if not t < int(instant):
            raise RefusRegistre(f"registre : ligne {k} datée {date}, pas strictement antérieure à l'ouverture ({date_utc(instant)})")
        sceau_conforme(racine / chemin, sha)
        sortie[k] = {"date": date, "instant": t, "chemin": chemin, "sha256": sha, "verifie": "fichier et compagnon .sha256"}
        if k in LIGNES_GO:
            sortie[k]["ligne_go"] = extrait_est_une_ligne_de(racine / chemin, racine / FICHIER_GO)
            sortie[k]["verifie"] += f" ; extrait égal à une ligne de {FICHIER_GO}"
    return sortie


def exiger_anteriorite(lignes: dict, avant: tuple, apres: str) -> None:
    """Chaque clé de `avant` strictement antérieure à `apres` (CLT7B-03 : `SCORES-T07`, `SONDES-T07` < `VERDICT-P3BIS`)."""
    if apres not in lignes:
        return
    for k in avant:
        if k not in lignes:
            raise RefusRegistre(f"registre : ligne {k} absente, exigée avant {apres}")
        if not lignes[k]["instant"] < lignes[apres]["instant"]:
            raise RefusRegistre(f"registre : ligne {k} ({lignes[k]['date']}) pas strictement antérieure à {apres} ({lignes[apres]['date']})")


def garde_ouverture(registre: Path, racine: Path, exigees, permises, instant: int) -> dict:
    lignes = lire_registre_t07(registre, exigees, permises)
    verifiees = verifier_lignes(lignes, racine, instant)
    return {"registre": str(registre), "registre_sha256": sha256_de(registre), "instant": date_utc(instant),
            "exigees": list(exigees), "permises_presentes": [k for k in permises if k in verifiees],
            "permises_absentes": [k for k in permises if k not in verifiees], "lignes": verifiees}


def journaliser_ouverture(registre: Path, instant: int, quoi: str, empreinte_objet: str) -> Path:
    journal = Path(str(registre) + ".ouvertures.md")
    with open(journal, "a", encoding="utf-8") as f:
        f.write(f"| OUVERTURE-T07 | {date_utc(instant)} | {quoi} | {empreinte_objet} | registre {sha256_de(registre)} |\n")
    return journal


def ecrire_ligne(cle: str, date: str, chemin: str, sha: str) -> str:
    """Une ligne au format exact."""
    if not CLE.fullmatch(cle) or not DATE.fullmatch(date) or not SHA.fullmatch(sha):
        raise RefusRegistre(f"ligne {cle} : clé, date ou empreinte hors format")
    return f"| {cle} | {date} | {chemin} | {sha} |"


def ajouter_ligne(registre: Path, cle: str, instant: int, chemin: str, sha: str) -> str:
    """Ajoute une ligne au registre (créé à la première ligne, jamais réécrit) ; refuse si la clé y est déjà."""
    registre = Path(registre)
    ligne = ecrire_ligne(cle, date_utc(instant), chemin, sha)
    if registre.is_file():
        for l in registre.read_text(encoding="utf-8").splitlines():
            cellules = [c.strip() for c in l.strip().strip("|").split("|")]
            if cellules and cellules[0] == cle:
                raise RefusRegistre(f"registre : ligne {cle} déjà présente, jamais réécrite")
    else:
        registre.parent.mkdir(parents=True, exist_ok=True)
        registre.write_text("# Registre des scellements (T0.6, T0.7, P3-bis) — lignes ajoutées, jamais réécrites\n\n", encoding="utf-8")
    with open(registre, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    return ligne


__all__ = ["RefusRegistre", "lire_registre_t07", "verifier_lignes", "garde_ouverture", "journaliser_ouverture", "sceau_conforme",
           "sha256_de", "extrait_est_une_ligne_de", "exiger_anteriorite", "ecrire_ligne", "ajouter_ligne", "instant_utc", "date_utc",
           "EXIGEES_ETAPE_A", "PERMISES_ETAPE_A", "EXIGEES_ETAPE_B", "PERMISES_ETAPE_B", "REGISTRE_DEFAUT", "CLES_CONNUES"]
