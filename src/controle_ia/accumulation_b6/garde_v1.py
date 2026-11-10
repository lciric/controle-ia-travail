"""Registre propre, journal propre, garde d'ouverture et aiguillage du barreau 6 (`ACCB6`), v1.

Texte joué : `brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-brouillon2.md` (`9f070e31…`), « Plan d'analyse »,
points 1 à 3, « Lignes de registre », « Liste d'arrêt ».

- **Registre propre** `registres/accumulation-b6-v1.md` (clés `SCELLEMENT-ACCB6`, `CODE-ACCB6`, `LECTURE-ACCB6`), journal propre
  `registres/accumulation-b6-v1.md.ouvertures.md` (lignes `OUVERTURE-ACCB6`, `REFUS-ACCB6`) ; **jamais** `registres/scellements-v1.md`
  ni son journal : ce module n'y écrit rien, il y lit `RUN-CONFIRMATION-T06`, `SCORES-T07`, `SONDES-T07`, `VERDICT-P3BIS` et, dans le
  journal de T0.7, la première ligne `OUVERTURE-T07` dont la troisième cellule commence par `scores-t07/`.
- **Garde d'ouverture** (`garde`) : clés exigées, chacune exactement une fois, de forme conforme (format de `registre_v1`, appelé tel
  quel pour le registre propre), sceau vérifié (`registre_v1.verifier_lignes`), strictement antérieure à l'ouverture ; fichier
  `lecture-t07.json` présent et scellé (`manifeste.verifier_resultat`) ; `arret-etape-b.json` présent → refus, nœud ;
  `lecture-accb6.json` déjà présent sous `diag/` → refus (lecture unique, R12) ; `SCELLEMENT-ACCB6` strictement avant
  `SCORES-T07` (sinon refus, nœud) ; clé de ce texte (marque `ACCB6`) présente dans `registres/scellements-v1.md` → refus (liste
  d'arrêt : la mère retire la ligne). Tous les motifs sont relevés, puis rendus ensemble (une ligne `REFUS-ACCB6` au journal propre,
  `RefusAccb6`, code 2) ; sinon une ligne `OUVERTURE-ACCB6`. Réserve R-B6-TARD (scellement non strictement antérieur à
  `RUN-CONFIRMATION-T06`) relevée ici ; R-B6-CODE après l'aiguillage (`reserve_code`).
- **Aiguillage** (`aiguiller`), avant toute ouverture de E1, la première ligne qui s'applique : G-1 (`scores_ouverts` faux, recoupé
  avec `issue_critere_3` ∈ {R11-arret, R12-invalide, L0a, L0b, L0c, L1}), G-2 (`scores_ii_ouverts` faux, recoupé avec `issue_critere_3`
  ∈ {L7b, L7c} ou L1b avec `entrees.Q` ∈ {non_calculable, incoherent}), G-3 (`entrees.A`, recoupé avec `table_A.A`, ∈ {A1b, A2,
  A3}), G-4 sinon. Champ absent ou recoupement en désaccord : refus, code 2, nœud.
"""
from __future__ import annotations

import json
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import verifier_resultat
from ..scellement import verifier
from ..t07 import criteres_v1 as cr
from ..t07 import registre_v1 as rg

REGISTRE_PROPRE = "registres/accumulation-b6-v1.md"
JOURNAL_PROPRE = REGISTRE_PROPRE + ".ouvertures.md"
REGISTRE_PARTAGE = rg.REGISTRE_DEFAUT                              # registres/scellements-v1.md : lu, jamais écrit
JOURNAL_PARTAGE = REGISTRE_PARTAGE + ".ouvertures.md"              # lu, jamais écrit
MARQUE = "ACCB6"
SCELLEMENT_ACCB6, CODE_ACCB6, LECTURE_ACCB6 = "SCELLEMENT-ACCB6", "CODE-ACCB6", "LECTURE-ACCB6"
OUVERTURE_ACCB6, REFUS_ACCB6 = "OUVERTURE-ACCB6", "REFUS-ACCB6"
PREREG = "prereg/accumulation-barreau6-v1.md"
EXIGEES_PROPRE = (SCELLEMENT_ACCB6, CODE_ACCB6)
REFUSEES_PROPRE = {LECTURE_ACCB6: "ligne LECTURE-ACCB6 déjà inscrite : la lecture est unique (R12) : refus"}
EXIGEES_PARTAGE = (rg.RUN_CONFIRMATION_T06, rg.SCORES_T07, rg.SONDES_T07, rg.VERDICT_P3BIS)
RUN_7A = "20261109-070232-t06-reel"                                 # course exploratoire 7a : jamais lue
FICHIER_SCORES, FICHIER_SONDES, FICHIER_NOTATION = "scores-actions-t07.npz", "sondes-t07.json", "notation-t07.json"
FICHIER_LECTURE_T07, FICHIER_ARRET_B = "lecture-t07.json", "arret-etape-b.json"
FICHIER_MESURES = "mesures-t06.npz"
NOM_LECTURE, NOM_ARRET = "lecture-accb6", "arret-accb6"
FICHIER_LECTURE, FICHIER_ARRET = NOM_LECTURE + ".json", NOM_ARRET + ".json"

ISSUES_G1 = ("R11-arret", "R12-invalide", "L0a", "L0b", "L0c", "L1")
ISSUES_G2 = ("L7b", "L7c")
Q_FERMANTS = ("non_calculable", "incoherent")                      # chaînes exactes de `criteres_v1.Q`
A_G3 = ("A1b", "A2", "A3")
CHAMPS_E4 = ("scores_ouverts", "scores_ii_ouverts", "issue_critere_3", "entrees", "table_A", "fuites", "doses",
             "conditions_retirees", "jeux", "jeux_hors_jugement", "reserves_identifiees", "sondes_lues", "niveau_applique")
DOSES = cr.DOSES


class RefusAccb6(GardeArret):
    """Refus avant le manifeste (garde, aiguillage, entrées de T0.7 lues avant E1) : rien d'écrit hors du journal propre, code 2."""


# ------------------------------------------------------------------------------------------------------------- journal propre
def _cellules(ligne: str) -> list:
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def _empreinte_registre(racine: Path) -> str:
    p = Path(racine) / REGISTRE_PROPRE
    return rg.sha256_de(p) if p.is_file() else "absent"


def journaliser(racine: Path, cle: str, instant: int, quoi: str, detail: str) -> Path | None:
    """Ligne `| CLÉ | date | quoi | détail | registre <sha256> |` au journal propre ; rien si son dossier n'existe pas."""
    if cle not in (OUVERTURE_ACCB6, REFUS_ACCB6):
        raise GardeArret(f"clé de journal {cle!r} : {OUVERTURE_ACCB6} ou {REFUS_ACCB6} seulement")
    journal = Path(racine) / JOURNAL_PROPRE
    if journal.resolve() == (Path(racine) / JOURNAL_PARTAGE).resolve():
        raise GardeArret("journal de T0.7 : ce module n'y écrit jamais")
    if not journal.parent.is_dir():
        return None
    propre = " ".join(str(detail).replace("|", "¦").split())
    with open(journal, "a", encoding="utf-8") as f:
        f.write(f"| {cle} | {rg.date_utc(instant)} | {quoi} | {propre} | registre {_empreinte_registre(racine)} |\n")
    return journal


def inscrire_lecture(racine: Path, instant: int, chemin: str, sha: str) -> str:
    """Ligne `LECTURE-ACCB6` au registre propre (jamais au registre partagé)."""
    registre = Path(racine) / REGISTRE_PROPRE
    if registre.resolve() == (Path(racine) / REGISTRE_PARTAGE).resolve():
        raise GardeArret("registre partagé de T0.7 : aucune clé de ce texte n'y est écrite")
    if not registre.is_file():
        raise GardeArret(f"{registre} absent : la ligne LECTURE-ACCB6 n'est jamais écrite ailleurs")
    return rg.ajouter_ligne(registre, LECTURE_ACCB6, instant, chemin, sha)


# ------------------------------------------------------------------------------------------------------------ registre partagé
def lire_registre_partage(registre: Path) -> dict:
    """Les quatre clés exigées de `registres/scellements-v1.md`, chacune exactement une fois, de forme conforme (mêmes contrôles et
    mêmes textes que `registre_v1.lire_registre_detail`) ; toute autre clé est ignorée (ce n'est pas le registre de ce texte), sauf
    une clé de ce texte (marque `ACCB6`) → refus. Rend clé → (instant, date, chemin, sha)."""
    registre = Path(registre)
    if not registre.is_file():
        raise rg.RefusRegistre(f"registre {registre} absent")
    trouvees: dict = {k: [] for k in EXIGEES_PARTAGE}
    fautes = []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        c = _cellules(ligne)
        if not c or not c[0]:
            continue
        if c[0] in trouvees:
            trouvees[c[0]].append(c)
        elif MARQUE in c[0].split("-"):
            fautes.append(f"registre partagé : ligne {c[0]} : clé de ce texte (marque {MARQUE}) écrite dans {REGISTRE_PARTAGE} : arrêt "
                          "de l'écriture ; la mère retire la ligne et le déclare")
    sortie = {}
    for k, lignes in trouvees.items():
        if len(lignes) != 1:
            fautes.append(f"registre : {len(lignes)} ligne(s) {k}, exactement une attendue")
            continue
        c = lignes[0]
        if len(c) != 4:
            fautes.append(f"registre : ligne {k} mal formée ({len(c)} colonnes, 4 attendues)")
            continue
        _, date, chemin, sha = c
        if not rg.DATE.fullmatch(date):
            fautes.append(f"registre : ligne {k} : date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
            continue
        if not rg.SHA.fullmatch(sha):
            fautes.append(f"registre : ligne {k} : empreinte {sha!r} (64 caractères hexadécimaux attendus)")
            continue
        if not chemin or chemin.startswith("/") or ".." in Path(chemin).parts:
            fautes.append(f"registre : ligne {k} : chemin {chemin!r} (relatif à la racine, sans « .. » attendu)")
            continue
        try:
            instant = rg.instant_utc(date)
        except rg.RefusRegistre:
            fautes.append(f"registre : ligne {k} : date {date!r} impossible")
            continue
        sortie[k] = (instant, date, chemin, sha)
    if fautes:
        e = rg.RefusRegistre(" ; ".join(fautes))
        e.partiel = sortie
        raise e
    return sortie


def lire_fichier_code(chemin: Path) -> dict:
    """Fichier cité par `CODE-ACCB6` : `{commit, fichiers : {chemin : sha256}, entropie}` (« Lignes de registre ») ; entropie de
    128 bits (entier, 0 < e < 2¹²⁸). Toute autre forme → refus."""
    try:
        d = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise rg.RefusRegistre(f"CODE-ACCB6 : fichier {chemin} illisible ({type(e).__name__})") from None
    if not isinstance(d, dict) or set(d) != {"commit", "fichiers", "entropie"}:
        raise rg.RefusRegistre("CODE-ACCB6 : forme {commit, fichiers, entropie} attendue (clés exactement)")
    if not isinstance(d["commit"], str) or not (len(d["commit"]) == 40 and all(x in "0123456789abcdef" for x in d["commit"])):
        raise rg.RefusRegistre(f"CODE-ACCB6 : commit {d['commit']!r} : 40 caractères hexadécimaux attendus")
    if not isinstance(d["fichiers"], dict) or not d["fichiers"] or not all(
            isinstance(p, str) and p and isinstance(s, str) and rg.SHA.fullmatch(s) for p, s in d["fichiers"].items()):
        raise rg.RefusRegistre("CODE-ACCB6 : fichiers {chemin : sha256} non vide attendu")
    e = d["entropie"]
    if isinstance(e, bool) or not isinstance(e, int) or not 0 < e < 2 ** 128:
        raise rg.RefusRegistre(f"CODE-ACCB6 : entropie {e!r} : entier de 128 bits attendu (0 < e < 2^128)")
    return d


def _run_de(chemin: str, debut: str, nom: str, cle: str) -> str:
    p = Path(chemin)
    if len(p.parts) != 3 or p.parts[0] != debut or p.name != nom:
        raise rg.RefusRegistre(f"ligne {cle} : chemin {chemin!r}, `{debut}/<run>/{nom}` attendu")
    return p.parts[1]


# -------------------------------------------------------------------------------------------------------------------- garde
def garde(racine: Path, instant: int) -> dict:
    """Garde d'ouverture (docstring du module). Rend les lignes vérifiées, les runs, l'entropie, le fichier de code et la réserve
    R-B6-TARD ; refus → ligne `REFUS-ACCB6` et `RefusAccb6` (tous les motifs)."""
    racine = Path(racine)
    motifs: list = []

    def tenter(f, *args):
        try:
            return f(*args)
        except GardeArret as e:
            motifs.append(str(e))
            return getattr(e, "partiel", None)
        except (OSError, ValueError, KeyError, TypeError) as e:          # fichier illisible : motif écrit, jamais un passage
            motifs.append(f"{getattr(f, '__name__', f)} : fichier illisible ({type(e).__name__}: {e})")
            return None

    # registre propre (lecteur de T0.7 appelé tel quel : clés exigées, refusées, toute autre clé refusée par sa règle (4))
    lu = tenter(rg.lire_registre_detail, racine / REGISTRE_PROPRE, EXIGEES_PROPRE, (), REFUSEES_PROPRE, ())
    propre = (lu[0] if isinstance(lu, tuple) else lu) or {}
    v_propre = tenter(rg.verifier_lignes, propre, racine, instant) if propre else {}
    v_propre = v_propre or {}
    code = None
    if SCELLEMENT_ACCB6 in v_propre and v_propre[SCELLEMENT_ACCB6]["chemin"] != PREREG:
        motifs.append(f"ligne SCELLEMENT-ACCB6 : chemin {v_propre[SCELLEMENT_ACCB6]['chemin']!r} ≠ {PREREG!r}")
    if CODE_ACCB6 in v_propre:
        code = tenter(lire_fichier_code, racine / v_propre[CODE_ACCB6]["chemin"])
    # registre partagé (lu, jamais écrit)
    partage = tenter(lire_registre_partage, racine / REGISTRE_PARTAGE) or {}
    v_part = tenter(rg.verifier_lignes, partage, racine, instant) if partage else {}
    v_part = v_part or {}
    run_7b = run_t07 = None
    if rg.RUN_CONFIRMATION_T06 in v_part:
        run_7b = tenter(_run_de, v_part[rg.RUN_CONFIRMATION_T06]["chemin"], "runs", "manifeste.json", rg.RUN_CONFIRMATION_T06)
        if run_7b == RUN_7A:
            motifs.append(f"RUN-CONFIRMATION-T06 désigne la course exploratoire 7a ({RUN_7A}) : lecture invalide, nœud")
            run_7b = None
    runs = {}
    for k, debut, nom in ((rg.SCORES_T07, "donnees", FICHIER_SCORES), (rg.SONDES_T07, "diag", FICHIER_SONDES)):
        if k in v_part:
            r = tenter(_run_de, v_part[k]["chemin"], debut, nom, k)
            if r:
                runs[k] = r
    if len(runs) == 2:
        if runs[rg.SCORES_T07] != runs[rg.SONDES_T07]:
            motifs.append(f"SCORES-T07 ({runs[rg.SCORES_T07]}) et SONDES-T07 ({runs[rg.SONDES_T07]}) : runs de T0.7 différents")
        else:
            run_t07 = runs[rg.SCORES_T07]
    # ordre : SCELLEMENT-ACCB6 strictement avant SCORES-T07
    if SCELLEMENT_ACCB6 in v_propre and rg.SCORES_T07 in v_part:
        if not v_propre[SCELLEMENT_ACCB6]["instant"] < v_part[rg.SCORES_T07]["instant"]:
            motifs.append(f"SCELLEMENT-ACCB6 ({v_propre[SCELLEMENT_ACCB6]['date']}) non strictement antérieure à SCORES-T07 "
                          f"({v_part[rg.SCORES_T07]['date']}) : refus de la lecture, nœud")
    # fichiers de l'étape B de T0.7 et lecture unique
    if run_t07 is not None:
        dossier = racine / "diag" / run_t07
        e4 = dossier / FICHIER_LECTURE_T07
        if not e4.is_file():
            motifs.append(f"diag/{run_t07}/{FICHIER_LECTURE_T07} absent : lecture après celle de T0.7 seulement (attente)")
        else:
            tenter(verifier_resultat, racine, e4)
        if (dossier / FICHIER_ARRET_B).exists():
            motifs.append(f"diag/{run_t07}/{FICHIER_ARRET_B} présent : refus, nœud")
    deja = sorted(str(p.relative_to(racine)) for p in (racine / "diag").glob(f"*/{FICHIER_LECTURE}")) if (racine / "diag").is_dir() else []
    if deja:
        motifs.append(f"{deja[0]} déjà présent : la lecture est unique (R12) : refus")
    if motifs:
        journaliser(racine, REFUS_ACCB6, instant, f"lecture/{run_t07 or '?'}", "clés ou fichiers manquants ou fautifs : " + " ; ".join(motifs))
        raise RefusAccb6(" ; ".join(motifs))
    reserves = []
    if not v_propre[SCELLEMENT_ACCB6]["instant"] < v_part[rg.RUN_CONFIRMATION_T06]["instant"]:
        reserves.append({"id": "R-B6-TARD", "vise": "toute la lecture",
                         "motif": f"SCELLEMENT-ACCB6 ({v_propre[SCELLEMENT_ACCB6]['date']}) non strictement antérieure à "
                                  f"RUN-CONFIRMATION-T06 ({v_part[rg.RUN_CONFIRMATION_T06]['date']}) ; déclarer ce que les auteurs ont "
                                  "vu de 7b"})
    journaliser(racine, OUVERTURE_ACCB6, instant, f"lecture/{run_t07}", f"garde passée ; registre partagé "
                f"{rg.sha256_de(racine / REGISTRE_PARTAGE)}")
    return {"instant": rg.date_utc(instant), "lignes_propres": v_propre, "lignes_partagees": v_part, "run_7b": run_7b,
            "run_t07": run_t07, "code": code, "entropie": int(code["entropie"]), "reserves": reserves}


def premiere_ouverture_scores_t07(racine: Path) -> int | None:
    """Instant de la première ligne `OUVERTURE-T07` dont la troisième cellule commence par `scores-t07/` au journal de T0.7 (lu,
    jamais écrit), ou None."""
    journal = Path(racine) / JOURNAL_PARTAGE
    if not journal.is_file():
        return None
    for ligne in journal.read_text(encoding="utf-8").splitlines():
        c = _cellules(ligne)
        if len(c) >= 3 and c[0] == "OUVERTURE-T07" and c[2].startswith("scores-t07/"):
            return rg.instant_utc(c[1])
    return None


def reserve_code(racine: Path, g: dict, aiguillage: str) -> dict | None:
    """R-B6-CODE : `CODE-ACCB6` non strictement antérieure à la première ouverture des scores par T0.7 (lecture permise, réserve
    gelée). Sous G-1, T0.7 n'a pas ouvert ses scores : sans objet. Scores ouverts mais aucune ligne d'ouverture au journal de T0.7 :
    antériorité non vérifiable, réserve écrite (déclaré)."""
    if aiguillage == "G-1":
        return None
    t_code = g["lignes_propres"][CODE_ACCB6]
    premiere = premiere_ouverture_scores_t07(racine)
    condition = ("permise seulement si l'auteur et le contre-lecteur du code n'ont vu ni lecture-t07.json ni aucune issue de T0.7 ou "
                 "de P3-bis (sinon : lecture invalide, version neuve)")
    if premiere is None:
        return {"id": "R-B6-CODE", "vise": "toute la lecture", "condition": condition,
                "motif": "antériorité de CODE-ACCB6 non vérifiable : aucune ligne OUVERTURE-T07 « scores-t07/ » au journal de T0.7"}
    if not t_code["instant"] < premiere:
        return {"id": "R-B6-CODE", "vise": "toute la lecture", "condition": condition,
                "motif": f"CODE-ACCB6 ({t_code['date']}) non strictement antérieure à la première ouverture des scores par T0.7 "
                         f"({rg.date_utc(premiere)})"}
    return None


# --------------------------------------------------------------------------------------------------------------- aiguillage
def lire_e4(racine: Path, run_t07: str) -> dict:
    """`diag/<run-t07>/lecture-t07.json` (scellé, rattaché au manifeste de T0.7) : son `resultat`, champs du texte exigés."""
    corps = verifier_resultat(racine, Path(racine) / "diag" / run_t07 / FICHIER_LECTURE_T07)
    r = corps.get("resultat") if isinstance(corps, dict) else None
    if not isinstance(r, dict):
        raise GardeArret("lecture-t07.json : resultat absent : refus, nœud")
    absents = [k for k in CHAMPS_E4 if k not in r]
    if absents:
        raise GardeArret(f"lecture-t07.json : champs absents {absents} : refus, nœud")
    return r


def aiguiller(r: dict) -> dict:
    """Aiguillage G-1 à G-4 (« Plan d'analyse », point 3), la première ligne qui s'applique ; champ absent ou recoupement en
    désaccord → `GardeArret` (refus, code 2, nœud). Recoupement déclaré en plus des trois du texte : `conditions_retirees` vide quand
    `scores_ii_ouverts` est vrai, égal aux quatre doses quand il est faux (sous `scores_ouverts`)."""
    absents = [k for k in CHAMPS_E4 if k not in r]
    if absents:
        raise GardeArret(f"lecture-t07.json : champs absents {absents} : refus, nœud")
    so, sio, issue = r["scores_ouverts"], r["scores_ii_ouverts"], r["issue_critere_3"]
    if not isinstance(so, bool) or not isinstance(sio, bool):
        raise GardeArret(f"scores_ouverts {so!r}, scores_ii_ouverts {sio!r} : booléens attendus : refus, nœud")
    if issue not in cr.ORDRE:
        raise GardeArret(f"issue_critere_3 {issue!r} hors de {cr.ORDRE} : refus, nœud")
    entrees, table = r["entrees"], r["table_A"]
    if not isinstance(entrees, dict) or "A" not in entrees or "Q" not in entrees:
        raise GardeArret("lecture-t07.json : entrees.A ou entrees.Q absent : refus, nœud")
    if not isinstance(table, dict) or "A" not in table:
        raise GardeArret("lecture-t07.json : table_A.A absent : refus, nœud")
    a, q, a_table = entrees["A"], entrees["Q"], table["A"]
    sortie = {"scores_ouverts": so, "scores_ii_ouverts": sio, "issue_critere_3": issue, "A": a, "Q": q, "table_A": a_table,
              "conditions_retirees": r["conditions_retirees"]}
    # G-1
    if not so:
        if sio:
            raise GardeArret("scores_ii_ouverts vrai sous scores_ouverts faux : recoupement en désaccord : refus, nœud")
        if issue not in ISSUES_G1:
            raise GardeArret(f"scores_ouverts faux mais issue {issue} ∉ {ISSUES_G1} : recoupement en désaccord : refus, nœud")
        return {**sortie, "ligne": "G-1"}
    if issue in ISSUES_G1:
        raise GardeArret(f"scores_ouverts vrai mais issue {issue} ∈ {ISSUES_G1} : recoupement en désaccord : refus, nœud")
    retirees = r["conditions_retirees"]
    if not isinstance(retirees, list):
        raise GardeArret(f"conditions_retirees {retirees!r} : liste attendue sous scores_ouverts : refus, nœud")
    # G-2
    ferme_ii = issue in ISSUES_G2 or (issue == "L1b" and q in Q_FERMANTS)
    if not sio:
        if not ferme_ii:
            raise GardeArret(f"scores_ii_ouverts faux mais issue {issue} (Q = {q}) ni L7b, ni L7c, ni L1b sous Q ∈ {Q_FERMANTS} : "
                             "recoupement en désaccord : refus, nœud")
        if sorted(retirees) != sorted(DOSES):
            raise GardeArret(f"scores_ii_ouverts faux mais conditions_retirees {retirees} ≠ {list(DOSES)} : recoupement en désaccord : "
                             "refus, nœud")
        return {**sortie, "ligne": "G-2"}
    if ferme_ii:
        raise GardeArret(f"scores_ii_ouverts vrai mais issue {issue} (Q = {q}) les ferme : recoupement en désaccord : refus, nœud")
    if retirees:
        raise GardeArret(f"scores_ii_ouverts vrai mais conditions_retirees {retirees} non vide : recoupement en désaccord : refus, nœud")
    # G-3
    if a != a_table:
        raise GardeArret(f"entrees.A {a!r} ≠ table_A.A {a_table!r} : recoupement en désaccord : refus, nœud")
    if a not in cr.A:
        raise GardeArret(f"entrees.A {a!r} hors de {cr.A} : refus, nœud")
    if a in A_G3:
        return {**sortie, "ligne": "G-3"}
    return {**sortie, "ligne": "G-4"}


def verifier_fichier(chemin: Path) -> str:
    """Fichier exigé hors registre (E2b, E3) : présent et égal à son compagnon `.sha256` (R11) ; sinon refus."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise RefusAccb6(f"{chemin} absent (fichier exigé)")
    return verifier(chemin)


__all__ = ["RefusAccb6", "garde", "aiguiller", "lire_e4", "reserve_code", "journaliser", "inscrire_lecture", "lire_registre_partage",
           "lire_fichier_code", "premiere_ouverture_scores_t07", "verifier_fichier", "REGISTRE_PROPRE", "JOURNAL_PROPRE",
           "REGISTRE_PARTAGE", "JOURNAL_PARTAGE", "SCELLEMENT_ACCB6", "CODE_ACCB6", "LECTURE_ACCB6", "PREREG", "MARQUE", "RUN_7A"]
