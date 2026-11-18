"""Épreuves (R5) du module de lecture final `lecture_v5` de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), écrit
sous le complément au quatrième addendum d'écart (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, § 6). **Tout
est jouet** : registres, arbres et dépôts git fabriqués dans le dossier temporaire de l'essai. Aucun essai ne lit le registre
propre réel, l'histoire réelle du dépôt, une sortie de la course ni un fichier de résultat ; les seuls fichiers du dépôt lus sont
du code (`lecture_v4.py`, `lecture_v5.py`) et le texte scellé du préenregistrement, recopié dans l'arbre jouet (comme
`tests/aide_t07bbis_jouet_v1.py`).

**Environnement fixé par les essais** : chaque essai retire de son environnement toute variable `GIT_*` (la machine en pose) et
`BBIS_INSTANCE`, et pose un dossier personnel vide ; les commandes git qui fabriquent les dépôts jouets reçoivent un
environnement écrit ici (`ENV_GIT`), sans rien d'hérité que le chemin de recherche.

**Comment `main` est joué en mode jouet** : `main` n'a aucun paramètre qui fasse passer `lire` en mode jouet (c'est la
propriété verrouillée). Les essais jouent donc le vrai `main`, et remplacent le seul nom `lire` du module par un passeur qui
appelle le vrai `lire` avec `essai=…` (tirages réduits, exception d'ordre du dépôt jouet). Tout le reste de `main` est réel.

1. Cas sains de la septième différence (un par motif de mise en place) : I0, nature « mise en place », preuve conforme, pièce
   scellée, journal sans ligne, code 3 ; puis panne corrigée, relance sous un nom neuf : la lecture jouet se déroule.
2. Artefacts de la preuve d'aucune ouverture (O1, O2, O3).
3. Refus de fond, chacun sans relance possible.
4. Arrêt après ouverture : ligne du seuil imprimée, code 2, aucune pièce.
5. R12 : relance sous le nom du run refusé, refus.
6. Différentiel version 4 → version 5.
7. Garde des variables d'environnement de git (huitième différence).
"""
from __future__ import annotations

import hashlib
import inspect
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t07bbis import lecture_v4 as lv4
from controle_ia.t07bbis import lecture_v5 as lv5

RACINE = Path(__file__).resolve().parents[1]
V4, V5 = "src/controle_ia/t07bbis/lecture_v4.py", "src/controle_ia/t07bbis/lecture_v5.py"
V4_SHA256 = "9bfca6269e34bb2a2ccd9b35c43c2af7b69e67b8bee45eab223cbd0a1c85f7ca"
COMPLEMENT_SHA256 = "12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419"
SEUIL = "BBIS LECTURE ENTREES OUVERTES"

# ---------------------------------------------------------------------------------------------------------- 6. différentiel
# (différence du § 6 du complément, ancien, nouveau, nombre d'occurrences exigé dans la version 4) : ce sont les couples mêmes
# qui ont produit `lecture_v5.py` depuis `lecture_v4.py` ; l'essai refait le fichier et exige l'égalité exacte.
COUPLES = [
    ("nom du module",
     r'''dans le docstring de `main`. Les v1 à v3 restent (R12).

Sections : (1)''',
     r'''dans le docstring de `main`. Les v1 à v3 restent (R12).

v5 : la v4, modifiée par le **complément au quatrième addendum d'écart**
(`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, empreinte scellée
`12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419`, § 6) et par lui seul : (D7) suite d'un refus de la garde né
d'un pur défaut de mise en place — classe `RefusMiseEnPlace`, levée aux seuls endroits des motifs (M1) à (M3) ; nature du refus
et preuve d'aucune ouverture (`preuve_aucune_ouverture`, points (O1) à (O3)) écrites par `lire` ; ligne
`BBIS LECTURE ENTREES OUVERTES` imprimée juste avant la première ouverture d'une entrée ; dans `main`, pièce
`preuve-aucune-ouverture-bbis` scellée, aucune ligne au journal des ouvertures, ligne `BBIS LECTURE NON CONSOMMEE`, code de
sortie 3 ; (D8) `exiger_environnement_git_propre` : refus, sans nettoyage, si une variable d'environnement `GIT_*` est posée, en
première instruction de `main` et de `lire` en lecture réelle ; nom du module dans `ecrire_lecture` et dans les docstrings. Les
v1 à v4 restent (R12) ; la v4 n'est ni rattachée ni jouée pour la lecture.

Sections : (1)''', 1),
    ("D7 (a)",
     r'''class RefusLecture(GardeArret):
    """Refus de la garde d'ouverture : rien n'est lu (I0, motif écrit)."""
''',
     r'''class RefusLecture(GardeArret):
    """Refus de la garde d'ouverture : rien n'est lu (I0, motif écrit)."""


class RefusMiseEnPlace(RefusLecture):
    """Refus de la garde d'ouverture né d'un pur défaut de mise en place de l'arbre de lecture (complément au quatrième
    addendum, motifs (M1) à (M3)) : fichier cité ou compagnon absent du disque, registre absent du disque, dépôt superficiel,
    commit nommé absent d'un dépôt superficiel, code de retour inattendu d'une commande git. Rendu en I0 comme tout refus."""
''', 1),
    ("D8",
     r'''        raise GardeArret("lecture de B bis demandée sur l'instance (BBIS_INSTANCE posée) : refus ; aucune aire, aucun état ni "
                         "résumé de score n'est calculé sur l'instance")
''',
     r'''        raise GardeArret("lecture de B bis demandée sur l'instance (BBIS_INSTANCE posée) : refus ; aucune aire, aucun état ni "
                         "résumé de score n'est calculé sur l'instance")


def exiger_environnement_git_propre() -> None:
    """Complément au quatrième addendum, D8 : si l'environnement du processus porte une variable dont le nom commence par
    `GIT_`, refus (jamais un nettoyage : aucune variable n'est retirée ni changée) ; le refus nomme ces variables par leur nom
    seulement, jamais une valeur."""
    posees = sorted(k for k in os.environ if k.startswith("GIT_"))
    if posees:
        raise GardeArret(f"variable(s) d'environnement de git posée(s) ({', '.join(posees)}) : refus ; la lecture de B bis ne "
                         "lance aucune commande git sous une variable GIT_* (complément au quatrième addendum, D8)")
''', 1),
    ("D7 (a)",
     r'''        raise RefusLecture(f"registre {registre} absent")''',
     r'''        raise RefusMiseEnPlace(f"registre {registre} absent")''', 1),
    ("D7 (a)",
     r'''    fautes = []
    for k, x in lignes.items():
        try:
            if not x["instant"] < int(instant):
                raise RefusLecture(f"ligne {k} datée {x['date']}, pas strictement antérieure à l'ouverture")
            rg.sceau_conforme(Path(racine) / x["chemin"], x["sha256"])
        except GardeArret as e:
            fautes.append(str(e))
    if fautes:
        raise RefusLecture(" ; ".join(fautes))
''',
     r'''    fautes, de_fond = [], False
    for k, x in lignes.items():
        try:
            if not x["instant"] < int(instant):
                raise RefusLecture(f"ligne {k} datée {x['date']}, pas strictement antérieure à l'ouverture")
            cite = Path(racine) / x["chemin"]
            if not cite.is_file():                                   # (M1) relevé avant `sceau_conforme` : fichier non extrait
                raise RefusMiseEnPlace(f"{cite} absent")
            if not Path(str(cite) + ".sha256").is_file():            # (M1) compagnon non extrait
                raise RefusMiseEnPlace(f"{cite} : compagnon .sha256 absent")
            rg.sceau_conforme(cite, x["sha256"])
        except GardeArret as e:
            fautes.append(str(e))
            de_fond = de_fond or not isinstance(e, RefusMiseEnPlace)
    if fautes:
        raise (RefusLecture if de_fond else RefusMiseEnPlace)(" ; ".join(fautes))
''', 1),
    ("D7 (a)",
     r'''    def refus(point: str, motif: str) -> RefusLecture:
        return RefusLecture(f"preuve d'entrée conjointe, point ({point}) : {motif}")

    def git(point: str, *args, codes=(0,)):
        try:
            r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True)
        except OSError as e:
            raise refus(point, f"git {' '.join(args[:2])} : échec de git ({e})") from None
        if r.returncode not in codes:
            raise refus(point, f"git {' '.join(args[:2])} : échec de git (code {r.returncode} ; "
                               f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})")
        return r

    def exiger_commit(point: str, c) -> None:
        if not isinstance(c, str) or not hexa.fullmatch(c):
            raise refus(point, f"identifiant de commit {c!r} : 40 caractères hexadécimaux attendus")
        r = git(point, "cat-file", "-e", f"{c}^{{commit}}", codes=tuple(range(256)))
        if r.returncode != 0:
            raise refus(point, f"commit {c[:12]} absent du dépôt ou illisible (code {r.returncode} ; "
                               f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})")
''',
     r'''    def refus(point: str, motif: str, classe=RefusLecture) -> RefusLecture:
        return classe(f"preuve d'entrée conjointe, point ({point}) : {motif}")

    def git(point: str, *args, codes=(0,)):
        try:
            r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True)
        except OSError as e:
            raise refus(point, f"git {' '.join(args[:2])} : échec de git ({e})", RefusMiseEnPlace) from None
        if r.returncode not in codes:
            raise refus(point, f"git {' '.join(args[:2])} : échec de git (code {r.returncode} ; "
                               f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})", RefusMiseEnPlace)
        return r

    def exiger_commit(point: str, c) -> None:
        if not isinstance(c, str) or not hexa.fullmatch(c):
            raise refus(point, f"identifiant de commit {c!r} : 40 caractères hexadécimaux attendus")
        r = git(point, "cat-file", "-e", f"{c}^{{commit}}", codes=tuple(range(256)))
        if r.returncode != 0:
            superficiel = git(point, "rev-parse", "--is-shallow-repository").stdout.decode("utf-8", "replace").strip() == "true"
            raise refus(point, f"commit {c[:12]} absent du dépôt{' superficiel' if superficiel else ''} ou illisible (code "
                               f"{r.returncode} ; {r.stderr.decode('utf-8', 'replace').strip()[:200]})",
                        RefusMiseEnPlace if superficiel else RefusLecture)
''', 1),
    ("D7 (a)",
     r'''                raise RefusLecture(f"{refus} ; preuve d'entrée conjointe du quatrième addendum refusée : {e}") from None''',
     r'''                raise type(e)(f"{refus} ; preuve d'entrée conjointe du quatrième addendum refusée : {e}") from None''', 1),
    ("D7 (a)",
     r'''        raise RefusLecture(f"git {' '.join(args[:2])} : échec ({r.stderr.strip()[:200]})")''',
     r'''        raise RefusMiseEnPlace(f"git {' '.join(args[:2])} : échec ({r.stderr.strip()[:200]})")''', 1),
    ("D7 (a)",
     r'''    sinon refus et nœud (liste d'arrêt, première ligne)."""
    ajout = _git(''',
     r'''    sinon refus et nœud (liste d'arrêt, première ligne)."""
    superficiel = _git(racine, "rev-parse", "--is-shallow-repository").strip()
    if superficiel != "false":
        raise RefusMiseEnPlace("dépôt superficiel : histoire git incomplète, antériorité de l'étape B non vérifiable"
                               if superficiel == "true" else "git rev-parse --is-shallow-repository : sortie inattendue")
    ajout = _git(''', 1),
    ("D7 (b)",
     r'''

def lire(racine: Path, run_7b: str, run_bbis: str, instant: int, adaptateur_mc=None, essai: dict | None = None,
''',
     r'''

def preuve_aucune_ouverture(racine: Path, garde_entrees, passee: bool) -> dict:
    """Preuve d'aucune ouverture (complément au quatrième addendum) : (O1) la liste blanche des entrées n'a pas été construite
    (`garde_entrees` absent) ou sa liste `lus` est vide ; (O2) la ligne `BBIS LECTURE ENTREES OUVERTES` n'a pas été imprimée
    (`passee` faux) ; (O3) le journal des ouvertures est absent du disque, ou présent sans aucune ligne `OUVERTURE-BBIS` (nombre
    de lignes et empreinte relevés). Rend `conforme` vrai ou faux avec les relevés ; ne lève rien pour un point en défaut."""
    import hashlib
    from .registre_bbis_v1 import REGISTRE_PROPRE
    rel = REGISTRE_PROPRE + ".ouvertures.md"
    journal = Path(racine) / rel
    lus = None if garde_entrees is None else list(garde_entrees.lus)
    o1 = {"conforme": not lus, "liste_blanche_construite": garde_entrees is not None, "entrees_ouvertes": len(lus or [])}
    o2 = {"conforme": not passee, "ligne_du_seuil_imprimee": bool(passee)}
    if journal.is_file():
        try:
            octets = journal.read_bytes()
            lignes = octets.decode("utf-8", "replace").splitlines()
            n = sum("OUVERTURE-BBIS" in l for l in lignes)
            o3 = {"conforme": n == 0, "journal": rel, "etat": "présent", "lignes": len(lignes), "lignes_ouverture": n,
                  "sha256": hashlib.sha256(octets).hexdigest()}
        except OSError as e:
            o3 = {"conforme": False, "journal": rel, "etat": f"illisible ({type(e).__name__})"}
    elif journal.exists() or journal.is_symlink():
        o3 = {"conforme": False, "journal": rel, "etat": "présent, ni fichier ni absent"}
    else:
        o3 = {"conforme": True, "journal": rel, "etat": "absent du disque"}
    return {"conforme": bool(o1["conforme"] and o2["conforme"] and o3["conforme"]), "O1": o1, "O2": o2, "O3": o3}


def lire(racine: Path, run_7b: str, run_bbis: str, instant: int, adaptateur_mc=None, essai: dict | None = None,
''', 1),
    ("D8",
     r'''`n_directions`, `n_nul`, `n_tirages` ; jamais en lecture réelle."""
    from ..harnais.run_harnais_factice import graine_entiere
''',
     r'''`n_directions`, `n_nul`, `n_tirages` ; jamais en lecture réelle."""
    if essai is None:
        exiger_environnement_git_propre()
    from ..harnais.run_harnais_factice import graine_entiere
''', 1),
    ("D7 (b)",
     r'''           "instant_ouverture": rg.date_utc(instant), "essai": not reel, "section_D": SECTION_D}
    try:
''',
     r'''           "instant_ouverture": rg.date_utc(instant), "essai": not reel, "section_D": SECTION_D}
    garde, passee = None, False
    try:
''', 1),
    ("D7 (c)",
     r'''        garde = GardeEntrees(racine, entrees_autorisees(run_7b, run_bbis, partagees, propres), run_7a)
        p3 = issue_p3bis(''',
     r'''        garde = GardeEntrees(racine, entrees_autorisees(run_7b, run_bbis, partagees, propres), run_7a)
        passee = True
        print("BBIS LECTURE ENTREES OUVERTES", flush=True)
        p3 = issue_p3bis(''', 1),
    ("D7 (b)",
     r'''        res["garde"] = {"refus": str(e)}
''',
     r'''        res["garde"] = {"refus": str(e), "nature": "mise en place" if isinstance(e, RefusMiseEnPlace) else "fond"}
        if res["garde"]["nature"] == "mise en place":
            res["garde"]["aucune_ouverture"] = preuve_aucune_ouverture(racine, garde, passee)
''', 1),
    ("nom du module",
     r'''commande="python -m controle_ia.t07bbis.lecture_v4")''',
     r'''commande="python -m controle_ia.t07bbis.lecture_v5")''', 1),
    ("nom du module",
     r'''PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v4 --racine''',
     r'''PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v5 --racine''', 1),
    ("D8",
     r'''(`adaptateur_retenu` ; fils de calcul à 1 exigés), sinon implémentation de repli."""
    import time
''',
     r'''(`adaptateur_retenu` ; fils de calcul à 1 exigés), sinon implémentation de repli."""
    try:
        exiger_environnement_git_propre()
    except GardeArret as e:
        print(f"BBIS LECTURE ARRET : {e}")
        return 2
    import time
''', 1),
    ("D7 (d)",
     r'''        chemin = ecrire_lecture(racine, a.run_lecture, r, entropie)
''',
     r'''        chemin = ecrire_lecture(racine, a.run_lecture, r, entropie)
        refus = r.get("garde") or {}
        if refus.get("nature") == "mise en place" and (refus.get("aucune_ouverture") or {}).get("conforme") is True:
            from ..manifeste import ecrire_resultat
            piece = ecrire_resultat(racine, racine / "runs" / a.run_lecture / "manifeste.json", "preuve-aucune-ouverture-bbis",
                                    {"motif": refus["refus"], "nature": refus["nature"],
                                     "aucune_ouverture": refus["aucune_ouverture"],
                                     "fichier_de_lecture": str(chemin.relative_to(racine)),
                                     "fichier_de_lecture_sha256": empreinte(chemin)})
            print(f"BBIS LECTURE NON CONSOMMEE {chemin.relative_to(racine)} {empreinte(chemin)} {piece.relative_to(racine)} "
                  f"{empreinte(piece)}")
            return 3
''', 1),
]


def appliquer(texte: str, couples) -> str:
    for _, ancien, nouveau, n in couples:
        assert texte.count(ancien) == n, (ancien[:70], texte.count(ancien), n)
        texte = texte.replace(ancien, nouveau)
    return texte


def test_6_la_version_5_est_la_version_4_plus_D7_D8_et_le_nom_du_module_et_rien_d_autre():
    v4 = (RACINE / V4).read_bytes()
    assert hashlib.sha256(v4).hexdigest() == V4_SHA256                                       # la version 4, à l'octet, intacte
    assert (RACINE / V5).read_text(encoding="utf-8") == appliquer(v4.decode("utf-8"), COUPLES)
    assert {d for d, *_ in COUPLES} == {"nom du module", "D7 (a)", "D7 (b)", "D7 (c)", "D7 (d)", "D8"}
    assert COMPLEMENT_SHA256 in COUPLES[0][2]                                                 # l'en-tête nomme l'empreinte scellée
    assert set(lv5.__all__) - set(lv4.__all__) == {"RefusMiseEnPlace", "preuve_aucune_ouverture",
                                                   "exiger_environnement_git_propre"}
    assert set(lv4.__all__) - set(lv5.__all__) == set()
    assert lv5.EXCEPTION_ORDRE_ADDENDUM_4 == lv4.EXCEPTION_ORDRE_ADDENDUM_4                   # la constante de D2, inchangée
    assert issubclass(lv5.RefusMiseEnPlace, lv5.RefusLecture) and issubclass(lv5.RefusLecture, GardeArret)


def test_6_aucun_parametre_ne_declare_une_nature_ne_saute_la_preuve_ni_ne_tait_la_ligne_du_seuil():
    for nom in ("lire", "main", "ecrire_lecture", "exiger_ordre_propre", "preuve_entree_conjointe", "lire_lignes",
                "verifier_lignes", "anteriorite_etape_b"):
        assert inspect.signature(getattr(lv5, nom)) == inspect.signature(getattr(lv4, nom)), nom
    assert list(inspect.signature(lv5.exiger_environnement_git_propre).parameters) == []
    source, v4 = (RACINE / V5).read_text(encoding="utf-8"), (RACINE / V4).read_text(encoding="utf-8")
    for acces in ("getenv", "argparse", "add_argument", "sys.argv"):
        assert source.count(acces) == v4.count(acces)                 # aucune option de ligne de commande de plus
    assert source.count("os.environ") == v4.count("os.environ") + 1   # la seule lecture de plus : les noms des variables GIT_*
    assert source.count('print("BBIS LECTURE ENTREES OUVERTES", flush=True)') == 1
    assert source.count("essai.get(") == v4.count("essai.get(")       # aucune clé d'essai de plus
    assert source.count("exiger_environnement_git_propre()") == 3     # définition, `lire` (lecture réelle), `main`


# -------------------------------------------------------------------------------------- environnement fixé par les essais

@pytest.fixture(autouse=True)
def environnement(monkeypatch, tmp_path_factory):
    """Aucun essai ne dépend de l'environnement hérité : variables `GIT_*` et `BBIS_INSTANCE` retirées, dossier personnel vide."""
    for k in [k for k in os.environ if k.startswith("GIT_")] + ["BBIS_INSTANCE"]:
        monkeypatch.delenv(k, raising=False)
    maison = tmp_path_factory.mktemp("maison")
    monkeypatch.setenv("HOME", str(maison))
    monkeypatch.setenv("XDG_CONFIG_HOME", str(maison / "config"))


def _env_git(date: str | None = None) -> dict:
    """Environnement, écrit ici, des commandes git qui fabriquent les dépôts jouets."""
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
           "GIT_CONFIG_GLOBAL": os.devnull, "GIT_AUTHOR_NAME": "essai", "GIT_AUTHOR_EMAIL": "essai@example.invalid",
           "GIT_COMMITTER_NAME": "essai", "GIT_COMMITTER_EMAIL": "essai@example.invalid", "LC_ALL": "C"}
    if date:
        env.update({"GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date})
    return env


def _git(d: Path, *args, date: str | None = None) -> str:
    r = subprocess.run(["git", "-c", "protocol.file.allow=always", "-C", str(d), *args], capture_output=True, text=True,
                       env=_env_git(date))
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} : {r.stderr.strip()}")
    return r.stdout.strip()


def _commit(d: Path, message: str, date: str | None = None) -> str:
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "--allow-empty", "-m", message, date=date)
    return _git(d, "rev-parse", "HEAD")


def _sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def _poser(d: Path, rel: str, texte: str, sceau: bool = True) -> str:
    """Écrit le fichier et, sauf demande contraire, son compagnon `.sha256` ; rend l'empreinte."""
    p = d / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    if sceau:
        Path(str(p) + ".sha256").write_text(f"{_sha(texte)}  {p.name}\n", encoding="utf-8")
    return _sha(texte)


def _l(cle, date, chemin, sha):
    return f"| {cle} | {date} | {chemin} | {sha} |\n"


# ------------------------------------------------------------------------------------- arbres jouets : registres et histoire

DOSSIER = "registres/t07-etape-b-bis"
F1, F2, GO = f"{DOSSIER}/code-bbis-jouet-v1.json", f"{DOSSIER}/code-bbis-jouet-v2.json", f"{DOSSIER}/go-bbis-jouet-v2.txt"
ABSENCE = f"{DOSSIER}/ABSENCE-B-BBIS-jouet-v1.json"
ISSUE, VERDICT = "docs/verdicts/issue-p3bis-jouet.json", "docs/verdicts/verdict-p3bis-jouet.md"
SC, D1, T, SCORES = "2026-10-01T08:00:00Z", "2026-10-02T09:10:11Z", "2026-10-03T10:20:30Z", "2026-10-04T12:00:00Z"
RUN_7B, RUN_B = "20261010-070000-t06-jouet", "20261018-090000-bbis-jouet"
ESSAI = {"n_directions": 12, "n_nul": 3, "n_tirages": 60}


def _fiche(entropie: int) -> str:
    return json.dumps({"commit": "c" * 40, "fichiers": {"src/x.py": "a" * 64}, "entropie": str(entropie),
                       "epreuve_niveau": {"chemin": "e.json", "sha256": "b" * 64, "niveau_decisif_retenu": 0.99},
                       "niveau_decisif": 0.99}, ensure_ascii=False, indent=1) + "\n"


def base_legere(d: Path) -> SimpleNamespace:
    """Arbre jouet sans course : texte scellé du préenregistrement recopié, manifeste et fichier de sondes fabriqués (jamais
    lus : les essais qui s'en servent s'arrêtent à la garde ou juste après)."""
    from controle_ia.t07bbis import commun_v1 as cm
    d.mkdir(parents=True, exist_ok=True)
    _git(d, "init", "-q", "-b", "main")
    (d / "prereg").mkdir()
    for nom in (Path(cm.TEXTE).name, Path(cm.TEXTE).name + ".sha256"):
        shutil.copy(RACINE / "prereg" / nom, d / "prereg" / nom)
    sha_m = _poser(d, f"runs/{RUN_7B}/manifeste.json", '{"jouet": "manifeste"}\n')
    sha_s = _poser(d, f"diag/{RUN_B}/sondes-bbis.json", '{"jouet": "sondes"}\n')
    _commit(d, "jouet", date="2026-09-01T00:00:00Z")
    return SimpleNamespace(d=d, run_7b=RUN_7B, run_b=RUN_B, sha_manifeste=sha_m, scores=(f"diag/{RUN_B}/sondes-bbis.json", sha_s),
                           entropie=2 ** 100 + 11)


def registres(base: SimpleNamespace, v: str | None = None, scores: str = SCORES, issue: str = "vu",
              verdict: str = VERDICT, avant_c0=None) -> SimpleNamespace:
    """Registres jouets de l'arbre `base.d`, dont l'histoire git reproduit F4 à F8 du quatrième addendum : (c0) registre propre à
    deux lignes, registre partagé, fichier de l'accord ; (conjoint) un commit à un seul parent ajoute ensemble, à la même seconde,
    la ligne de la fiche remplaçante et celle de l'accord, et la fiche ; (remise) insertion de la ligne de la première fiche ;
    (course) ; (scores). `v` = « fiche-deja-au-parent » : la fiche remplaçante est déjà dans l'arbre du parent (preuve d'entrée
    conjointe en défaut par contenu). Rend l'exception jouet aux valeurs de ce dépôt et les commits."""
    from controle_ia.t07bbis import commun_v1 as cm
    from controle_ia.t07bbis.registre_bbis_v1 import REGISTRE_PARTAGE, REGISTRE_PROPRE
    d = base.d
    if avant_c0 is not None:
        avant_c0(d)
    txt = {GO: "accord de calcul jouet\n", F1: _fiche(2 ** 100 + 99), F2: _fiche(base.entropie)}
    sha = {k: _sha(x) for k, x in txt.items()}
    (d / VERDICT).parent.mkdir(parents=True, exist_ok=True)
    (d / verdict).write_text("verdict jouet\n", encoding="utf-8")
    sha_issue = _poser(d, ISSUE, json.dumps({"issue": issue, "ligne": 5 if issue == "vu" else 3, "verdict": verdict,
                                             "verdict_sha256": _sha("verdict jouet\n")}) + "\n")
    _poser(d, REGISTRE_PARTAGE, "# registre partagé jouet\n\n"
           + _l("RUN-CONFIRMATION-T06", "2026-09-12T05:00:00Z", f"runs/{base.run_7b}/manifeste.json", base.sha_manifeste)
           + _l("VERDICT-P3BIS", "2026-09-13T05:00:00Z", ISSUE, sha_issue), sceau=False)
    sha_abs = _poser(d, ABSENCE, '{"absents": true}\n')
    l_sc, l_abs = _l("SCELLEMENT-BBIS", SC, cm.TEXTE, cm.TEXTE_SHA256), _l("ABSENCE-B-BBIS", SC, ABSENCE, sha_abs)
    l_prem, l_code, l_go = _l("CODE-BBIS", D1, F1, sha[F1]), _l("CODE-BBIS", T, F2, sha[F2]), _l("GO-BBIS", T, GO, sha[GO])
    registre = lambda *ls: _poser(d, REGISTRE_PROPRE, "# registre propre jouet\n\n" + "".join(ls), sceau=False)
    registre(l_sc, l_abs)
    _poser(d, GO, txt[GO])
    if v == "fiche-deja-au-parent":
        _poser(d, F2, txt[F2])
    c0 = _commit(d, "c0 : scellement, constat d'absence, fichier de l'accord")
    registre(l_sc, l_abs, l_code, l_go)
    _poser(d, F2, txt[F2])
    c_conj = _commit(d, "entrée conjointe : fiche remplaçante et accord, même seconde")
    registre(l_sc, l_abs, l_prem, l_code, l_go)
    _poser(d, F1, txt[F1])
    c_remise = _commit(d, "remise de la première fiche (insertion)")
    c_course = _commit(d, "commit de la course")
    registre(l_sc, l_abs, l_prem, l_code, l_go, _l("SCORES-BBIS", scores, *base.scores))
    c_scores = _commit(d, "ligne des scores")
    exception = {"registre_propre": REGISTRE_PROPRE,
                 "code_bbis_remplace": {"date": D1, "chemin": F1, "sha256": sha[F1]},
                 "code_bbis": {"date": T, "chemin": F2, "sha256": sha[F2]},
                 "go_bbis": {"date": T, "chemin": GO, "sha256": sha[GO]},
                 "commit_entree_conjointe": c_conj, "commit_remise_premiere_fiche": c_remise, "commit_course": c_course}
    return SimpleNamespace(d=d, run_7b=base.run_7b, run_b=base.run_b, entropie=base.entropie, exception=exception, txt=txt,
                           c0=c0, c_conj=c_conj, c_remise=c_remise, c_course=c_course, c_scores=c_scores,
                           propre=REGISTRE_PROPRE, journal=REGISTRE_PROPRE + ".ouvertures.md")


@pytest.fixture
def leger(tmp_path):
    return registres(base_legere(tmp_path / "arbre"))


def ailleurs(h: SimpleNamespace, d: Path) -> SimpleNamespace:
    """Le même arbre jouet, vu depuis un autre dossier (copie ou clone)."""
    return SimpleNamespace(**{**vars(h), "d": d})


def copie(h: SimpleNamespace, d: Path) -> SimpleNamespace:
    shutil.copytree(h.d, d, symlinks=True)
    return ailleurs(h, d)


def clone_superficiel(h: SimpleNamespace, d: Path, profondeur: int) -> SimpleNamespace:
    _git(d.parent, "clone", "-q", "--depth", str(profondeur), h.d.as_uri(), str(d))
    assert _git(d, "rev-parse", "--is-shallow-repository") == "true" and _git(d, "rev-parse", "HEAD") == h.c_scores
    assert _git(d, "status", "--porcelain") == ""
    return ailleurs(h, d)


def completer(h: SimpleNamespace) -> None:
    """Correction de la panne « histoire incomplète » : l'histoire complète est récupérée ; aucun fichier ne change."""
    _git(h.d, "fetch", "-q", "--unshallow")
    assert _git(h.d, "rev-parse", "--is-shallow-repository") == "false"


VRAI_LIRE = lv5.lire


def lancer(monkeypatch, capsys, h: SimpleNamespace, run_lecture: str, exception="celle du dépôt jouet"):
    """Le vrai `main` de la version 5 sur l'arbre jouet ; seul `lire` reçoit `essai=…` par un passeur. Rend le code de sortie
    et les lignes imprimées."""
    exc = h.exception if exception == "celle du dépôt jouet" else exception
    essai = dict(ESSAI) if exc is None else {**ESSAI, "exception_ordre": exc}

    def lire_en_mode_jouet(racine, run_7b, run_bbis, instant, adaptateur_mc=None):
        return VRAI_LIRE(racine, run_7b, run_bbis, instant, adaptateur_mc, essai=essai)

    monkeypatch.setattr(lv5, "lire", lire_en_mode_jouet)
    capsys.readouterr()
    code = lv5.main(["--racine", str(h.d), "--run-7b", h.run_7b, "--run-bbis", h.run_b, "--run-lecture", run_lecture])
    return code, capsys.readouterr().out.splitlines()


def lignes_du_journal(h) -> list[str]:
    p = h.d / h.journal
    return p.read_text(encoding="utf-8").splitlines() if p.is_file() else []


def fichiers(d: Path) -> dict:
    """Tous les fichiers de l'arbre hors du dossier de git, avec leur empreinte : pour constater « rien d'écrit »."""
    return {str(p.relative_to(d)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(d.rglob("*")) if p.is_file() and ".git" not in p.relative_to(d).parts}


def resultat(h, run_lecture: str, nom: str = "lecture-bbis") -> dict:
    from controle_ia.manifeste import verifier_resultat
    return verifier_resultat(h.d, h.d / "diag" / run_lecture / f"{nom}.json")["resultat"]     # sceau et rattachement vérifiés


def exiger_non_consommee(h, run_lecture: str, code: int, sortie: list[str], motif: str) -> dict:
    """Suite d'un refus de pure mise en place dont la preuve passe : I0, nature, preuve, pièce scellée, journal sans ligne,
    ligne imprimée, code 3. Rend les empreintes des deux fichiers gardés."""
    from controle_ia.scellement import empreinte
    assert code == 3, sortie
    assert SEUIL not in sortie and len(sortie) == 1                             # aucune ouverture, une seule ligne imprimée
    lecture, piece = (f"diag/{run_lecture}/lecture-bbis.json", f"diag/{run_lecture}/preuve-aucune-ouverture-bbis.json")
    assert sortie[0] == f"BBIS LECTURE NON CONSOMMEE {lecture} {empreinte(h.d / lecture)} {piece} {empreinte(h.d / piece)}"
    res = resultat(h, run_lecture)
    g = res["garde"]
    assert g["nature"] == "mise en place" and motif in g["refus"], g["refus"]
    assert res["issue"] == lv5.issue_complete({}, {}, None, motif_i0=f"garde refusée ({g['refus']})")   # phrase gelée de I0
    assert "Étape B bis non lue : garde refusée (" in json.dumps(res["issue"], ensure_ascii=False)
    p = g["aucune_ouverture"]
    assert p["conforme"] is True and all(p[o]["conforme"] is True for o in ("O1", "O2", "O3"))
    assert p["O1"]["entrees_ouvertes"] == 0 and p["O2"]["ligne_du_seuil_imprimee"] is False
    assert p["O3"]["etat"] == "absent du disque"
    for cle in ("entrees_lues", "cellules", "lignes", "p3bis"):
        assert cle not in res
    doc = resultat(h, run_lecture, "preuve-aucune-ouverture-bbis")
    assert doc == {"motif": g["refus"], "nature": "mise en place", "aucune_ouverture": p, "fichier_de_lecture": lecture,
                   "fichier_de_lecture_sha256": empreinte(h.d / lecture)}
    assert lignes_du_journal(h) == [] and not (h.d / h.journal).exists()        # aucune ligne au journal des ouvertures
    return {lecture: empreinte(h.d / lecture), piece: empreinte(h.d / piece)}


def exiger_comme_la_version_3(h, run_lecture: str, code: int, sortie: list[str], n_journal: int = 1) -> dict:
    """Suite de la version 3 : fichier de lecture écrit, ligne au journal, `BBIS LECTURE ECRITE`, code 0, aucune pièce."""
    from controle_ia.scellement import empreinte
    lecture = f"diag/{run_lecture}/lecture-bbis.json"
    assert code == 0, sortie
    assert sortie[-1] == f"BBIS LECTURE ECRITE {lecture} {empreinte(h.d / lecture)}"
    assert not any(l.startswith("BBIS LECTURE NON CONSOMMEE") for l in sortie)
    assert not (h.d / "diag" / run_lecture / "preuve-aucune-ouverture-bbis.json").exists()   # pas de pièce « non consommée »
    j = lignes_du_journal(h)
    assert len(j) == n_journal and j[-1].startswith("| OUVERTURE-BBIS | ") and j[-1].endswith(
        f" | lecture B bis ({run_lecture}) | {empreinte(h.d / lecture)} |")
    return resultat(h, run_lecture)


# ----------------------------------------------------- 1. cas sains : un par motif de mise en place, puis relance

@pytest.fixture(scope="module")
def course(tmp_path_factory):
    """Course jouet de T0.6 et marche jouet de B bis (forme de `test_F…` du second addendum), puis registres jouets à l'histoire
    F4 à F8. Les commandes git de l'aide héritent de l'environnement : il est fixé ici le temps de la fabrication."""
    import aide_t07bbis_jouet_v1 as aide
    from controle_ia.t07bbis import marche_v4
    if not aide.disponible():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    run_b, entropie = "20261018-090000-bbis-jouet", 2 ** 100 + 11
    with pytest.MonkeyPatch.context() as mp:
        for k in [k for k in os.environ if k.startswith("GIT_")] + ["BBIS_INSTANCE"]:
            mp.delenv(k, raising=False)
        for k, x in _env_git().items():
            if k.startswith("GIT_"):
                mp.setenv(k, x)
        d = aide.course_jouet(tmp_path_factory.mktemp("course-lecture-v5") / "depot")
        r = marche_v4.marche(d, aide.RUN, run_b, entropie, d.parent / f"{d.name}-travail", "cpu",
                             essai={"epoques": 15, "n_plis_internes": 3, "n_directions": 12, "n_reetiquetages": 3,
                                    "n_controle": 6, "n_chemin": 3})
    assert r.get("scores_ecrits"), r
    sha_m = (d / "runs" / aide.RUN / "manifeste.json.sha256").read_text(encoding="utf-8").split()[0]
    base = SimpleNamespace(d=d, run_7b=aide.RUN, run_b=run_b, sha_manifeste=sha_m, entropie=entropie,
                           scores=(r["sondes_bbis"], r["sondes_bbis_sha256"]))
    h = registres(base)
    assert _git(d, "status", "--porcelain") == ""
    return h


def _retirer(h, rel: str) -> None:
    _git(h.d, "rm", "-q", "--", rel)
    _commit(h.d, f"panne : {rel} non extrait")


PANNES = {
    "fichier cité absent": dict(clone=None, casser=lambda h: _retirer(h, GO), motif=f"{GO} absent",
                                corriger=lambda h: _poser(h.d, GO, h.txt[GO], sceau=False)),
    "compagnon absent": dict(clone=None, casser=lambda h: _retirer(h, GO + ".sha256"), motif=f"{GO} : compagnon .sha256 absent",
                             corriger=lambda h: _poser(h.d, GO, h.txt[GO])),
    # histoire coupée sous le commit c0 : les trois commits nommés et leurs parents sont là, la preuve d'entrée conjointe passe,
    # le relevé du dépôt superficiel refuse
    "dépôt superficiel": dict(clone=5, casser=lambda h: None, motif="dépôt superficiel : histoire git incomplète",
                              corriger=completer),
    "commit nommé absent d'un dépôt superficiel": dict(clone=1, casser=lambda h: None,
                                                       motif="absent du dépôt superficiel ou illisible", corriger=completer),
}


@pytest.mark.parametrize("panne", sorted(PANNES))
def test_1_cas_sain_refus_de_pure_mise_en_place_non_consomme_puis_relance(course, tmp_path, monkeypatch, capsys, panne):
    from controle_ia.scellement import empreinte
    p = PANNES[panne]
    h = copie(course, tmp_path / "origine")
    if p["clone"] is not None:
        assert int(_git(h.d, "rev-list", "--count", "HEAD")) == 6                  # jouet, c0, conjoint, remise, course, scores
        h = clone_superficiel(h, tmp_path / "arbre-de-lecture", p["clone"])
    p["casser"](h)
    assert _git(h.d, "status", "--porcelain") == ""
    run = "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, h, run)
    gardes = exiger_non_consommee(h, run, code, sortie, p["motif"])
    if panne == "commit nommé absent d'un dépôt superficiel":
        assert "point (P1)" in resultat(h, run)["garde"]["refus"]
    # la suite : fichiers du refus gardés et commités, panne corrigée sur l'arbre jouet, relance sous un nom de run neuf
    _commit(h.d, "fichier de lecture du refus, pièce de preuve et manifeste gardés")
    p["corriger"](h)
    _commit(h.d, "panne corrigée")
    assert _git(h.d, "status", "--porcelain") == ""
    code, sortie = lancer(monkeypatch, capsys, h, run + "-relance1")
    res = exiger_comme_la_version_3(h, run + "-relance1", code, sortie)
    assert sortie.count(SEUIL) == 1 and sortie.index(SEUIL) < len(sortie) - 1      # le seuil, puis la ligne du fichier écrit
    assert "garde" not in res and res["ordre_propre"]["regle"] == "quatrième addendum"   # la garde passe
    assert res["cellules"] and all(x.get("etat") is not None for x in res["cellules"].values())   # la lecture jouet se déroule
    assert not any("R-RELANCE" in x or "R-ORDRE" in x for x in res["reserves"])    # réserves portées par le verdict, non le module
    assert {k: empreinte(h.d / k) for k in gardes} == gardes                       # le premier fichier et sa preuve : intacts
    resultat(h, run), resultat(h, run, "preuve-aucune-ouverture-bbis")             # sceaux et rattachements toujours conformes


def test_1_le_registre_absent_du_disque_est_un_motif_de_mise_en_place(tmp_path):
    with pytest.raises(lv5.RefusMiseEnPlace, match="registre .* absent"):          # (M2)
        lv5.lire_lignes(tmp_path / "registre-absent.md", lv5.CLES_PROPRES, (), propre=True)
    with pytest.raises(lv4.RefusLecture) as e4:
        lv4.lire_lignes(tmp_path / "registre-absent.md", lv4.CLES_PROPRES, (), propre=True)
    with pytest.raises(lv5.RefusLecture) as e5:
        lv5.lire_lignes(tmp_path / "registre-absent.md", lv5.CLES_PROPRES, (), propre=True)
    assert str(e4.value) == str(e5.value)                                          # même message que la version 4


def test_1_une_commande_git_au_code_inattendu_est_un_motif_de_mise_en_place(leger, tmp_path, monkeypatch):
    hors = tmp_path / "pas-un-depot"
    hors.mkdir()
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))                    # ne remonte vers aucun dépôt
    with pytest.raises(lv5.RefusMiseEnPlace, match="échec"):
        lv5.anteriorite_etape_b(hors, leger.propre)
    with pytest.raises(lv5.RefusMiseEnPlace, match="échec de git"):
        lv5.preuve_entree_conjointe(hors, leger.exception)
    monkeypatch.delenv("GIT_CEILING_DIRECTORIES")
    lignes = lv5.lire_lignes(leger.d / leger.propre, lv5.CLES_PROPRES, (), propre=True, remplacables=lv5.REMPLACABLES_PROPRES)
    vrai = subprocess.run

    def echec_de(sous_commande, code):
        def run(cmd, **k):
            r = vrai(cmd, **k)
            vide = "" if k.get("text") else b""
            return subprocess.CompletedProcess(cmd, code, r.stdout, vide) if sous_commande in cmd else r
        return run

    for sous_commande, code in (("merge-base", 128), ("merge-base", 2), ("show", 128), ("ls-tree", 1), ("rev-list", 129)):
        monkeypatch.setattr(subprocess, "run", echec_de(sous_commande, code))
        with pytest.raises(lv5.RefusMiseEnPlace, match="échec de git"):            # la nature traverse la fonction d'ordre
            lv5.exiger_ordre_propre(lignes, leger.d, leger.exception)
    monkeypatch.setattr(subprocess, "run", echec_de("merge-base", 1))               # « non ancêtre » : de fond
    with pytest.raises(lv5.RefusLecture, match="non ancêtre") as e:
        lv5.exiger_ordre_propre(lignes, leger.d, leger.exception)
    assert not isinstance(e.value, lv5.RefusMiseEnPlace)
    monkeypatch.setattr(subprocess, "run", echec_de("log", 128))
    with pytest.raises(lv5.RefusMiseEnPlace, match="git log"):
        lv5.anteriorite_etape_b(leger.d, leger.propre)

    def absent(cmd, **k):
        raise FileNotFoundError("git")

    monkeypatch.setattr(subprocess, "run", absent)
    with pytest.raises(lv5.RefusMiseEnPlace, match="échec de git"):
        lv5.preuve_entree_conjointe(leger.d, leger.exception)
    monkeypatch.setattr(subprocess, "run", vrai)
    assert lv5.exiger_ordre_propre(lignes, leger.d, leger.exception)["regle"] == "quatrième addendum"
    assert lv5.anteriorite_etape_b(leger.d, leger.propre)["commit_scellement"] == leger.c0


def test_1_cas_sain_sans_panne_la_garde_passe_et_aucune_nature_n_est_ecrite(leger, monkeypatch, capsys):
    """Arbre sain : la garde passe ; la lecture est arrêtée juste après elle par un espion (l'arbre léger n'a pas de données)."""
    from controle_ia.t07bbis import adversaires_texte_v1 as ad

    class Fin(Exception):
        pass

    def fin():
        raise Fin()

    monkeypatch.setattr(ad, "exiger_module_gele", fin)
    with pytest.raises(Fin):
        VRAI_LIRE(leger.d, leger.run_7b, leger.run_b, _t("2026-11-19T09:00:00Z"),
                  essai={**ESSAI, "exception_ordre": leger.exception})
    assert capsys.readouterr().out.splitlines() == [SEUIL]


def _t(date: str) -> int:
    return int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


# ------------------------------------------------------------------- 2. artefacts de la preuve d'aucune ouverture

def test_2_O3_journal_portant_deja_une_ligne_d_ouverture(leger, monkeypatch, capsys):
    _retirer(leger, GO)
    (leger.d / leger.journal).write_text("| OUVERTURE-BBIS | 2026-10-05T00:00:00Z | lecture B bis (antérieure) | " + "e" * 64
                                         + " |\n", encoding="utf-8")
    _commit(leger.d, "journal portant déjà une ligne")
    run = "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, leger, run)
    res = exiger_comme_la_version_3(leger, run, code, sortie, n_journal=2)        # ligne écrite au journal, code 0
    g = res["garde"]
    assert g["nature"] == "mise en place" and g["aucune_ouverture"]["conforme"] is False
    assert [o for o in ("O1", "O2", "O3") if not g["aucune_ouverture"][o]["conforme"]] == ["O3"]
    assert g["aucune_ouverture"]["O3"]["lignes_ouverture"] == 1 and g["aucune_ouverture"]["O3"]["lignes"] == 1
    assert SEUIL not in sortie


def test_2_O1_et_O2_refus_de_mise_en_place_leve_apres_la_premiere_ouverture(leger, monkeypatch, capsys):
    """Artefact fabriqué : un refus de mise en place levé après le seuil (le code n'en lève aucun à cet endroit) ; la preuve le
    voit par la liste `lus` et par la ligne imprimée, et la lecture est consommée."""
    def panne(chemin_issue, garde):
        raise lv5.RefusMiseEnPlace("panne simulée après la première ouverture")

    monkeypatch.setattr(lv5, "issue_p3bis", panne)
    run = "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, leger, run)
    res = exiger_comme_la_version_3(leger, run, code, sortie)
    p = res["garde"]["aucune_ouverture"]
    assert res["garde"]["nature"] == "mise en place" and p["conforme"] is False
    assert [o for o in ("O1", "O2", "O3") if not p[o]["conforme"]] == ["O1", "O2"]
    assert p["O1"] == {"conforme": False, "liste_blanche_construite": True, "entrees_ouvertes": 1}
    assert p["O2"] == {"conforme": False, "ligne_du_seuil_imprimee": True}
    assert sortie[0] == SEUIL


def test_2_la_preuve_point_par_point_sans_rien_lever(tmp_path):
    from controle_ia.t07bbis.registre_bbis_v1 import REGISTRE_PROPRE
    journal = tmp_path / (REGISTRE_PROPRE + ".ouvertures.md")
    vide, ouverte = lv5.GardeEntrees(tmp_path, {"a"}), lv5.GardeEntrees(tmp_path, {"a"})
    ouverte.exiger("a")
    sain = lv5.preuve_aucune_ouverture(tmp_path, None, False)                     # liste blanche non construite, journal absent
    assert sain["conforme"] is True and sain["O1"]["liste_blanche_construite"] is False
    assert lv5.preuve_aucune_ouverture(tmp_path, vide, False)["conforme"] is True   # construite, liste `lus` vide
    o1 = lv5.preuve_aucune_ouverture(tmp_path, ouverte, False)                    # (O1) liste `lus` non vide
    assert o1["conforme"] is False and [o1[o]["conforme"] for o in ("O1", "O2", "O3")] == [False, True, True]
    o2 = lv5.preuve_aucune_ouverture(tmp_path, vide, True)                        # (O2) ligne du seuil imprimée
    assert o2["conforme"] is False and [o2[o]["conforme"] for o in ("O1", "O2", "O3")] == [True, False, True]
    journal.parent.mkdir(parents=True)
    journal.write_text("# journal des ouvertures\n", encoding="utf-8")            # présent, sans ligne d'ouverture : conforme
    o3 = lv5.preuve_aucune_ouverture(tmp_path, None, False)
    assert o3["conforme"] is True and o3["O3"]["lignes"] == 1 and o3["O3"]["lignes_ouverture"] == 0
    assert o3["O3"]["sha256"] == hashlib.sha256(journal.read_bytes()).hexdigest()
    journal.write_text("# journal\n| OUVERTURE-BBIS | 2026-10-05T00:00:00Z | x | y |\n", encoding="utf-8")
    o3 = lv5.preuve_aucune_ouverture(tmp_path, None, False)                       # (O3) une ligne d'ouverture
    assert o3["conforme"] is False and [o3[o]["conforme"] for o in ("O1", "O2", "O3")] == [True, True, False]
    journal.unlink()
    journal.mkdir()                                                               # ni fichier ni absent : non conforme
    assert lv5.preuve_aucune_ouverture(tmp_path, None, False)["O3"]["conforme"] is False
    json.dumps(o3)


# ------------------------------------------------------------------------------ 3. refus de fond : sans relance possible

def _fond_empreinte(h):
    _poser(h.d, GO, "un autre accord\n")                      # fichier et compagnon d'accord entre eux, autres que le registre
    _commit(h.d, "accord d'une autre empreinte")


def _fond_compagnon(h):
    Path(str(h.d / GO) + ".sha256").write_text("f" * 64 + f"  {Path(GO).name}\n", encoding="utf-8")
    _commit(h.d, "compagnon différent du fichier")


def _fond_inscrite(h):
    with open(h.d / h.propre, "a", encoding="utf-8") as f:
        f.write(_l("LECTURE-BBIS", "2026-10-05T00:00:00Z", "diag/x/lecture-bbis.json", "a" * 64))
    _commit(h.d, "lecture déjà inscrite")


def _fond_mele(h):
    _git(h.d, "rm", "-q", "--", GO)                                                # motif de mise en place…
    Path(str(h.d / ABSENCE) + ".sha256").write_text("f" * 64 + f"  {Path(ABSENCE).name}\n", encoding="utf-8")   # … et de fond
    _commit(h.d, "fichier absent et compagnon différent")


def _etape_b_avant(d):
    _poser(d, "diag/20260901-000000-t07-jouet/lecture-t07.json", "{}\n", sceau=False)
    _commit(d, "étape B jouée avant le scellement de B bis", date="2026-09-02T00:00:00Z")


FONDS = {  # nom : (montage de l'arbre, geste, exception passée, motif attendu)
    "empreinte d'un fichier cité différente de celle du registre": ({}, _fond_empreinte, "dépôt", "≠ celle du registre"),
    "compagnon différent du fichier": ({}, _fond_compagnon, "dépôt", "compagnon .sha256 .* ≠ empreinte du fichier"),
    "ordre inversé hors l'exception": ({"scores": "2026-10-03T10:20:29Z"}, None, "dépôt",
                                       "CODE-BBIS .* pas strictement antérieure à SCORES-BBIS"),
    "égalité à la seconde sans l'exception": ({}, None, None, "GO-BBIS .* pas strictement antérieure à CODE-BBIS"),
    "preuve d'entrée conjointe en défaut par contenu": ({"v": "fiche-deja-au-parent"}, None, "dépôt",
                                                        r"point \(P3\) : .* déjà présent dans l'arbre du parent"),
    "étape B antérieure au scellement": ({"avant_c0": _etape_b_avant}, None, "dépôt", "étape B exécutée avant le scellement"),
    "lecture déjà inscrite": ({}, _fond_inscrite, "dépôt", "déjà inscrite"),
    "refus mêlant mise en place et fond": ({}, _fond_mele, "dépôt", "≠ empreinte du fichier.*absent"),
    "commit nommé absent d'un dépôt non superficiel": ({}, None, "commit absent", r"point \(P1\) : commit .* absent du dépôt ou"),
}


@pytest.mark.parametrize("fond", sorted(FONDS))
def test_3_refus_de_fond_nature_fond_ligne_au_journal_code_0_sans_relance(tmp_path, monkeypatch, capsys, fond):
    import re
    montage, geste, exc, motif = FONDS[fond]
    h = registres(base_legere(tmp_path / "arbre"), **montage)
    if geste is not None:
        geste(h)
    exception = {"dépôt": h.exception, None: None,
                 "commit absent": {**h.exception, "commit_entree_conjointe": "0123456789abcdef0123456789abcdef01234567"}}[exc]
    assert _git(h.d, "status", "--porcelain") == "" and _git(h.d, "rev-parse", "--is-shallow-repository") == "false"
    run = "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, h, run, exception=exception)
    res = exiger_comme_la_version_3(h, run, code, sortie)                          # ligne au journal, code 0, aucune pièce
    g = res["garde"]
    assert g["nature"] == "fond" and "aucune_ouverture" not in g and re.search(motif, g["refus"]), g["refus"]
    assert res["issue"] == lv5.issue_complete({}, {}, None, motif_i0=f"garde refusée ({g['refus']})")
    assert SEUIL not in sortie and len(sortie) == 1
    # sans relance possible : la lecture a laissé sa ligne au journal ; une relance, même la panne « corrigée », n'est jamais
    # rendue « non consommée »
    _commit(h.d, "fichiers du refus de fond")
    code, sortie = lancer(monkeypatch, capsys, h, run + "-relance1", exception=exception)
    assert code == 0 and not any(l.startswith("BBIS LECTURE NON CONSOMMEE") for l in sortie)
    assert len(lignes_du_journal(h)) == 2


def test_3_issue_de_l_epreuve_du_signal_plante_autre_que_vu(tmp_path, monkeypatch, capsys):
    h = registres(base_legere(tmp_path / "arbre"), issue="non vu")
    run = "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, h, run)
    res = exiger_comme_la_version_3(h, run, code, sortie)                          # ligne au journal, code 0, aucune pièce
    assert sortie[0] == SEUIL                                                      # une entrée a été ouverte
    assert res["p3bis"]["P"] == "non vu" and res["entrees_lues"] == sorted([ISSUE, VERDICT])
    assert (res.get("garde") or {}).get("nature") != "mise en place"               # la suite est celle de la version 3
    assert res["issue"] == lv5.issue_complete({}, {}, None, motif_i0=lv5.PHRASE_NON_LU_P3BIS)


def test_3_les_motifs_de_fond_de_la_verification_des_lignes_ne_sont_jamais_de_mise_en_place(leger):
    lignes = lv5.lire_lignes(leger.d / leger.propre, lv5.CLES_PROPRES, (), propre=True, remplacables=lv5.REMPLACABLES_PROPRES)
    lv5.verifier_lignes(leger.d, lignes, _t("2026-11-19T09:00:00Z"))               # cas sain
    with pytest.raises(lv5.RefusLecture, match="pas strictement antérieure à l'ouverture") as e:
        lv5.verifier_lignes(leger.d, lignes, _t(SC))                               # ligne non antérieure à l'ouverture : fond
    assert not isinstance(e.value, lv5.RefusMiseEnPlace)
    (leger.d / GO).unlink()
    with pytest.raises(lv5.RefusMiseEnPlace) as e:                                 # un seul motif, de mise en place
        lv5.verifier_lignes(leger.d, lignes, _t("2026-11-19T09:00:00Z"))
    with pytest.raises(lv4.RefusLecture) as e4:
        lv4.verifier_lignes(leger.d, lignes, _t("2026-11-19T09:00:00Z"))
    assert str(e.value) == str(e4.value) == f"{leger.d / GO} absent"               # même message que la version 4
    (leger.d / (ABSENCE + ".sha256")).unlink()
    with pytest.raises(lv5.RefusMiseEnPlace) as e:                                 # deux motifs, tous deux de mise en place
        lv5.verifier_lignes(leger.d, lignes, _t("2026-11-19T09:00:00Z"))
    with pytest.raises(lv4.RefusLecture) as e4:
        lv4.verifier_lignes(leger.d, lignes, _t("2026-11-19T09:00:00Z"))
    assert str(e.value) == str(e4.value) and "compagnon .sha256 absent" in str(e.value)
    with pytest.raises(lv5.RefusLecture) as e:                                     # mêlés à un motif de fond : de fond
        lv5.verifier_lignes(leger.d, lignes, _t(SCORES))
    assert not isinstance(e.value, lv5.RefusMiseEnPlace) and "absent" in str(e.value)


# -------------------------------------------------------------------------------------------- 4. arrêt après ouverture

def exiger_arret_apres_ouverture(h, run, code, sortie, avant: dict):
    assert code == 2 and sortie[0] == SEUIL and sortie[-1].startswith("BBIS LECTURE ARRET : ") and len(sortie) == 2
    assert fichiers(h.d) == avant                                                  # rien d'écrit : ni fichier, ni pièce, ni journal
    assert not (h.d / "runs" / run).exists() and not (h.d / "diag" / run).exists() and lignes_du_journal(h) == []


def test_4_garde_d_arret_levee_dans_le_bloc_de_la_garde_apres_la_premiere_ouverture(tmp_path, monkeypatch, capsys):
    """Le fichier d'issue de l'épreuve du signal planté cite un verdict de la liste « Jamais » : arrêt de `GardeEntrees.exiger`,
    dans le bloc de la garde, après la première ouverture."""
    h = registres(base_legere(tmp_path / "arbre"), verdict="docs/verdicts/etiqueteur-jouet.md")
    avant, run = fichiers(h.d), "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, h, run)
    exiger_arret_apres_ouverture(h, run, code, sortie, avant)
    assert "liste « Jamais »" in sortie[-1]


def test_4_garde_d_arret_levee_apres_le_bloc_de_la_garde(leger, monkeypatch, capsys):
    from controle_ia.t07bbis import adversaires_texte_v1 as ad

    def arret():
        raise GardeArret("module gelé d'une autre empreinte (jouet) : arrêt")

    monkeypatch.setattr(ad, "exiger_module_gele", arret)
    avant, run = fichiers(leger.d), "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, leger, run)
    exiger_arret_apres_ouverture(leger, run, code, sortie, avant)


def test_4_la_ligne_du_seuil_est_imprimee_avant_la_premiere_ouverture_et_jamais_sans_elle(leger, monkeypatch, capsys):
    ordre, vraie = [], lv5.GardeEntrees.exiger

    def exiger(self, rel):
        ordre.append(("ouverture", rel, capsys.readouterr().out))                  # ce qui a été imprimé avant cette ouverture
        return vraie(self, rel)

    monkeypatch.setattr(lv5.GardeEntrees, "exiger", exiger)
    from controle_ia.t07bbis import adversaires_texte_v1 as ad
    monkeypatch.setattr(ad, "exiger_module_gele", lambda: (_ for _ in ()).throw(GardeArret("fin de l'essai")))
    with pytest.raises(GardeArret):
        VRAI_LIRE(leger.d, leger.run_7b, leger.run_b, _t("2026-11-19T09:00:00Z"),
                  essai={**ESSAI, "exception_ordre": leger.exception})
    assert ordre and ordre[0] == ("ouverture", ISSUE, SEUIL + "\n")                # imprimée juste avant la première ouverture
    assert all(x[2] == "" for x in ordre[1:])                                      # une seule fois
    ordre.clear()
    (leger.d / GO).unlink()                                                        # refus avant le seuil : jamais imprimée
    res = VRAI_LIRE(leger.d, leger.run_7b, leger.run_b, _t("2026-11-19T09:00:00Z"),
                    essai={**ESSAI, "exception_ordre": leger.exception})
    assert res["garde"]["nature"] == "mise en place" and ordre == [] and SEUIL not in capsys.readouterr().out


# ----------------------------------------------------------------------------------------------------------- 5. R12

def test_5_relance_sous_le_nom_du_run_refuse_refus(leger, monkeypatch, capsys):
    from controle_ia.scellement import empreinte
    _retirer(leger, GO)
    run = "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, leger, run)
    gardes = exiger_non_consommee(leger, run, code, sortie, f"{GO} absent")
    _commit(leger.d, "fichiers du refus gardés")
    avant = fichiers(leger.d)
    code, sortie = lancer(monkeypatch, capsys, leger, run)                         # le même nom de run
    assert code == 2 and sortie[-1].startswith("BBIS LECTURE ARRET : ") and "existe déjà" in sortie[-1]
    assert fichiers(leger.d) == avant and {k: empreinte(leger.d / k) for k in gardes} == gardes   # rien d'écrasé


# --------------------------------------------------------------- 7. garde des variables d'environnement de git (D8)

@pytest.fixture
def aucun_processus(monkeypatch):
    """Tout lancement de processus est relevé et refusé."""
    lances = []

    def interdit(*a, **k):
        lances.append(a)
        raise AssertionError(f"processus lancé : {a}")

    for nom in ("run", "Popen", "call", "check_call", "check_output"):
        monkeypatch.setattr(subprocess, nom, interdit)
    monkeypatch.setattr(os, "system", interdit)
    return lances


def test_7_cas_sain_aucune_variable_de_git_la_fonction_passe(monkeypatch):
    assert not [k for k in os.environ if k.startswith("GIT_")]                     # environnement fixé par l'essai
    assert lv5.exiger_environnement_git_propre() is None
    for nom in ("GITHUB_TOKEN", "GITLAB_TOKEN", "MON_GIT_DIR", "git_dir", "GIT"):  # un autre nom ne refuse pas
        monkeypatch.setenv(nom, "valeur-a-ne-pas-ecrire")
        assert lv5.exiger_environnement_git_propre() is None


@pytest.mark.parametrize("variables", [("GIT_DIR",), ("GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0"),
                                       ("GIT_WORK_TREE", "GIT_INDEX_FILE"), ("GIT_",)])
def test_7_artefact_une_variable_de_git_posee_main_s_arrete_sans_commande_git_sans_rien_ecrire(leger, monkeypatch, capsys,
                                                                                              aucun_processus, variables):
    secret = "/chemin/secret/a-ne-jamais-ecrire"
    for k in variables:
        monkeypatch.setenv(k, secret)
    avant, env = fichiers(leger.d), dict(os.environ)
    run = "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, leger, run)
    assert code == 2 and len(sortie) == 1 and sortie[0].startswith("BBIS LECTURE ARRET : ")
    assert all(k in sortie[0] for k in variables) and secret not in sortie[0]      # le nom, jamais la valeur
    assert aucun_processus == [] and fichiers(leger.d) == avant                    # aucune commande git, rien d'écrit
    assert dict(os.environ) == env                                                 # aucun nettoyage : rien n'est retiré ni changé
    capsys.readouterr()
    assert lv5.main([]) == 2 and capsys.readouterr().out.startswith("BBIS LECTURE ARRET : ")   # avant la ligne de commande même
    with pytest.raises(GardeArret) as e:
        lv5.exiger_environnement_git_propre()
    assert not isinstance(e.value, lv5.RefusLecture) and secret not in str(e.value)


def test_7_meme_refus_par_lire_en_lecture_reelle_et_pas_en_mode_jouet(leger, monkeypatch, aucun_processus):
    monkeypatch.setenv("GIT_DIR", "/chemin/secret/a-ne-jamais-ecrire")
    monkeypatch.setattr(lv5, "lire_lignes", lambda *a, **k: (_ for _ in ()).throw(AssertionError("registre lu")))
    with pytest.raises(GardeArret, match="GIT_DIR") as e:                          # lecture réelle (`essai` absent) : refus
        VRAI_LIRE(leger.d, leger.run_7b, leger.run_b, _t("2026-11-19T09:00:00Z"))
    assert not isinstance(e.value, lv5.RefusLecture) and "secret" not in str(e.value) and aucun_processus == []
    with pytest.raises(AssertionError, match="registre lu"):                       # mode jouet : la garde ne joue pas
        VRAI_LIRE(leger.d, leger.run_7b, leger.run_b, _t("2026-11-19T09:00:00Z"), essai={})


def test_7_la_garde_est_la_premiere_instruction_de_main_et_de_lire_en_lecture_reelle(leger, monkeypatch, capsys):
    appels = []

    class Fin(GardeArret):
        pass

    def espion():
        appels.append("garde des variables de git")
        raise Fin("espion de l'essai")

    monkeypatch.setattr(lv5, "exiger_environnement_git_propre", espion)
    monkeypatch.setattr(lv5, "exiger_processeur", lambda: appels.append("processeur"))
    monkeypatch.setattr(lv5, "adaptateur_retenu", lambda *a, **k: appels.append("adaptateur"))
    assert lv5.main(["--option-inconnue"]) == 2 and appels == ["garde des variables de git"]   # avant la ligne de commande
    assert capsys.readouterr().out == "BBIS LECTURE ARRET : espion de l'essai\n"
    appels.clear()
    with pytest.raises(Fin):
        VRAI_LIRE(leger.d, leger.run_7b, leger.run_b, _t("2026-11-19T09:00:00Z"))
    assert appels == ["garde des variables de git"]
    source = inspect.getsource(lv5.main)
    assert source.index("exiger_environnement_git_propre()") < source.index("import time") < source.index("adaptateur_retenu(")
    source = inspect.getsource(VRAI_LIRE)
    assert source.index("exiger_environnement_git_propre()") < source.index("from ..harnais") < source.index("exiger_processeur()")


def test_7_cas_sain_une_variable_d_un_autre_nom_ne_refuse_pas_la_lecture(leger, monkeypatch, capsys):
    monkeypatch.setenv("GITHUB_TOKEN", "valeur-a-ne-pas-ecrire")
    _retirer(leger, GO)
    run = "20261119-090000-lecture-bbis-jouet"
    code, sortie = lancer(monkeypatch, capsys, leger, run)                         # `main` part, la garde d'ouverture est jouée
    exiger_non_consommee(leger, run, code, sortie, f"{GO} absent")
    assert "valeur-a-ne-pas-ecrire" not in json.dumps(resultat(leger, run), ensure_ascii=False)
