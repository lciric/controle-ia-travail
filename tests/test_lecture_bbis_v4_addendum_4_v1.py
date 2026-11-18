"""Épreuves (R5) du module de lecture neuf `lecture_v4` de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), écrit
sous le quatrième addendum d'écart (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md`, § 6.2). **Tout est jouet** : registres et
dépôts git fabriqués dans le dossier temporaire de l'essai. Aucun essai ne lit le registre propre réel, l'histoire réelle du dépôt,
une sortie de la course ni un fichier de résultat ; les seuls fichiers du dépôt lus sont du code (`lecture_v3.py`, `lecture_v4.py`)
et le texte de l'addendum (comparaison des valeurs de la constante).

1. Différentiel : `lecture_v4.py` = `lecture_v3.py` + les couples déclarés (`COUPLES`), égalité exacte ; chaque couple nomme la
   différence du § 6.1 (D1 à D6) qui le fonde.
2. La version 3 est conservée : les cas de l'essai d'ordre du second addendum rejoués sur la version 4, sans exception.
3. Cas sain de l'exception : dépôt jouet qui reproduit l'histoire F4 à F8 ; règle « quatrième addendum », cinq points conformes.
4. Artefacts de l'exception, (a) à (l), chacun refusé ; une commande git en échec n'est jamais un passage.
5. Lecture réelle verrouillée : valeurs de la constante, signatures, exception passée par `lire`.
6. De bout en bout, en mode jouet : cas sain (clé `ordre_propre` dans le fichier de lecture), artefacts (issue I0, « garde
   refusée (…) », aucune entrée ouverte).
7. (Suite existante `tests/test_t07bbis_*` : jouée à part, aucun fichier existant n'est modifié.)
"""
from __future__ import annotations

import hashlib
import inspect
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from controle_ia.t07bbis import lecture_v3 as lv3
from controle_ia.t07bbis import lecture_v4 as lv4

RACINE = Path(__file__).resolve().parents[1]
V3, V4 = "src/controle_ia/t07bbis/lecture_v3.py", "src/controle_ia/t07bbis/lecture_v4.py"
V3_SHA256 = "c9a478437f32465418dfafdadbd7823f88853a9c17f77a0e59cc4ccb5ccff6ec"
ADDENDUM = "prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md"
ADDENDUM_SHA256 = "5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4"

# ---------------------------------------------------------------------------------------------------------- 1. différentiel
# (différence du § 6.1, ancien, nouveau, nombre d'occurrences exigé dans la version 3) : ce sont les couples mêmes qui ont
# produit `lecture_v4.py` depuis `lecture_v3.py` ; l'essai refait le fichier et exige l'égalité exacte.
COUPLES = [
    ("D1",
     r'''lue au registre propre (`lire_lignes`, `exiger_ordre_propre`) ; les v1 et v2 restent (R12).

Sections : (1)''',
     r'''lue au registre propre (`lire_lignes`, `exiger_ordre_propre`) ; les v1 et v2 restent (R12).

v4 : la v3, modifiée par le **quatrième addendum d'écart** (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md`, empreinte scellée
`5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4`, § 6.1) et par lui seul : (D2) constante
`EXCEPTION_ORDRE_ADDENDUM_4` (les trois lignes du registre propre, les trois commits et le chemin du registre que la preuve
épingle) ; (D3) fonction neuve `preuve_entree_conjointe` (points (P1) à (P5) de QA-1, commandes git en lecture) ; (D4)
`exiger_ordre_propre(lignes, racine=None, exception=None)` : pour le seul couple (`GO-BBIS`, `CODE-BBIS` qui fait foi), l'égalité à
la seconde ne vaut pas refus si les trois lignes sont celles de l'exception et si la preuve passe ; (D5) dans `lire`, la règle qui
a servi est écrite sous `ordre_propre` (lecture réelle : la constante et elle seule) ; (D6) nom du module dans `ecrire_lecture` et
dans le docstring de `main`. Les v1 à v3 restent (R12).

Sections : (1)''', 1),
    ("D2",
     r'''REMPLACABLES_PROPRES = ("CODE-BBIS",)
''',
     r'''REMPLACABLES_PROPRES = ("CODE-BBIS",)
EXCEPTION_ORDRE_ADDENDUM_4 = {
    "registre_propre": "registres/t07-etape-b-bis-v1.md",
    "code_bbis_remplace": {"date": "2026-11-16T12:57:27Z", "chemin": "registres/t07-etape-b-bis/code-bbis-v1.json",
                           "sha256": "ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469"},
    "code_bbis": {"date": "2026-11-17T11:05:29Z", "chemin": "registres/t07-etape-b-bis/code-bbis-v2.json",
                  "sha256": "4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb"},
    "go_bbis": {"date": "2026-11-17T11:05:29Z", "chemin": "registres/t07-etape-b-bis/go-bbis-v2.txt",
                "sha256": "33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62"},
    "commit_entree_conjointe": "c098fb512d999e1dbf7cef5fba6430ff8b1a8fb5",
    "commit_remise_premiere_fiche": "06c8832819af344d01c184222833c5a42e8ac901",
    "commit_course": "438a9c5257bdc4fa65f25c42cc89753a049b4586",
}
''', 1),
    ("D3 et D4",
     r'''def exiger_ordre_propre(lignes: dict) -> None:
    """Ordre du plan, point 2 ; second addendum : une ligne `CODE-BBIS` remplacée se lit SCELLEMENT-BBIS < CODE-BBIS (première)
    < GO-BBIS < CODE-BBIS (remplacement) < SCORES-BBIS."""
    lignes, chaine = dict(lignes), list(ORDRE_PROPRE)
    if "CODE-BBIS" in lignes and "remplace" in lignes["CODE-BBIS"]:
        lignes["CODE-BBIS (première)"] = lignes["CODE-BBIS"]["remplace"]
        chaine = ["SCELLEMENT-BBIS", "CODE-BBIS (première)", "GO-BBIS", "CODE-BBIS", "SCORES-BBIS"]
    for a, b in zip(chaine, chaine[1:]):
        if a in lignes and b in lignes and not lignes[a]["instant"] < lignes[b]["instant"]:
            raise RefusLecture(f"ligne {a} ({lignes[a]['date']}) pas strictement antérieure à {b} ({lignes[b]['date']})")
''',
     r'''def preuve_entree_conjointe(racine: Path, exception: dict) -> dict:
    """Preuve d'entrée conjointe du quatrième addendum (QA-1, points (P1) à (P5)), relevée dans le dépôt de `racine` par des
    commandes git en lecture (`cat-file -e`, `rev-list --parents -n 1`, `show <commit>:<chemin>`, `ls-tree`, `merge-base
    --is-ancestor`) ; les empreintes des contenus lus par `git show` sont recalculées. Rend, pour chaque point, « conforme » avec
    les identifiants relevés. Un point en défaut, un objet absent, un code de retour inattendu : `RefusLecture` avec le point et
    le motif ; aucun repli (R5). `merge-base --is-ancestor` : code 0, ancêtre ; code 1, refus « non ancêtre » ; tout autre code,
    refus « échec de git »."""
    import hashlib
    import re
    hexa = re.compile(r"[0-9a-f]{40}")

    def refus(point: str, motif: str) -> RefusLecture:
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

    def seul_parent(point: str, c) -> str:
        exiger_commit(point, c)
        x = git(point, "rev-list", "--parents", "-n", "1", c).stdout.decode("utf-8", "replace").split()
        if len(x) != 2 or x[0] != c or not hexa.fullmatch(x[1]):
            raise refus(point, f"commit {c[:12]} : {max(len(x) - 1, 0)} parent(s) relevé(s), un seul exigé")
        return x[1]

    def texte(point: str, c: str, chemin: str) -> str:
        try:
            return git(point, "show", f"{c}:{chemin}").stdout.decode("utf-8")
        except UnicodeDecodeError:
            raise refus(point, f"{chemin} au commit {c[:12]} : contenu illisible") from None

    def present(point: str, c: str, chemin: str) -> bool:
        s = git(point, "ls-tree", "--full-tree", c, "--", chemin).stdout.decode("utf-8", "replace").splitlines()
        if not s:
            return False
        if len(s) != 1 or s[0].split()[1:2] != ["blob"]:
            raise refus(point, f"{chemin} dans l'arbre du commit {c[:12]} : un fichier, et un seul, attendu")
        return True

    def empreinte_lue(point: str, c: str, chemin: str) -> str:
        return hashlib.sha256(git(point, "show", f"{c}:{chemin}").stdout).hexdigest()

    def exiger_ancetre(point: str, a: str, b: str, quoi: str) -> None:
        if git(point, "merge-base", "--is-ancestor", a, b, codes=(0, 1)).returncode == 1:
            raise refus(point, f"{quoi} : non ancêtre")

    cle = lambda l: [x.strip() for x in l.strip().strip("|").split("|")][0]
    try:
        registre = exception["registre_propre"]
        code, go, premiere = (exception[k] for k in ("code_bbis", "go_bbis", "code_bbis_remplace"))
        c_conj, c_remise, c_course = (exception[k] for k in ("commit_entree_conjointe", "commit_remise_premiere_fiche",
                                                             "commit_course"))
        l_code, l_go, l_premiere = (f"| {k} | {x['date']} | {x['chemin']} | {x['sha256']} |"
                                    for k, x in (("CODE-BBIS", code), ("GO-BBIS", go), ("CODE-BBIS", premiere)))
        chemins = [registre, code["chemin"], go["chemin"], premiere["chemin"]]
    except (KeyError, TypeError) as e:
        raise RefusLecture(f"preuve d'entrée conjointe : exception mal formée ({e!r})") from None
    if any(not isinstance(x, str) or not x or x.startswith(("/", "-")) or ".." in Path(x).parts for x in chemins):
        raise RefusLecture("preuve d'entrée conjointe : exception mal formée (chemin)")
    # (P1) le commit de l'entrée conjointe existe et a un seul parent
    parent = seul_parent("P1", c_conj)
    # (P2) au commit, les deux lignes, une fois chacune et à l'octet ; au parent, aucune ligne de clé CODE-BBIS ni GO-BBIS
    au_commit = texte("P2", c_conj, registre).split("\n")
    for nom, l in (("CODE-BBIS", l_code), ("GO-BBIS", l_go)):
        if au_commit.count(l) != 1:
            raise refus("P2", f"au commit {c_conj[:12]}, le registre propre porte {au_commit.count(l)} fois la ligne {nom} de "
                              "l'exception, une fois exigée")
    deja = sorted({cle(l) for l in texte("P2", parent, registre).splitlines()} & {"CODE-BBIS", "GO-BBIS"})
    if deja:
        raise refus("P2", f"au parent {parent[:12]}, le registre propre porte déjà une ligne de clé {deja}")
    # (P3) le fichier de l'accord est dans l'arbre du parent, à l'empreinte de sa ligne ; la fiche remplaçante n'y est pas ;
    # elle est dans l'arbre du commit, à l'empreinte de sa ligne
    if not present("P3", parent, go["chemin"]):
        raise refus("P3", f"{go['chemin']} absent de l'arbre du parent {parent[:12]}")
    if empreinte_lue("P3", parent, go["chemin"]) != go["sha256"]:
        raise refus("P3", f"{go['chemin']} au parent {parent[:12]} : empreinte autre que celle de la ligne GO-BBIS")
    if present("P3", parent, code["chemin"]):
        raise refus("P3", f"{code['chemin']} déjà présent dans l'arbre du parent {parent[:12]}")
    if not present("P3", c_conj, code["chemin"]):
        raise refus("P3", f"{code['chemin']} absent de l'arbre du commit {c_conj[:12]}")
    if empreinte_lue("P3", c_conj, code["chemin"]) != code["sha256"]:
        raise refus("P3", f"{code['chemin']} au commit {c_conj[:12]} : empreinte autre que celle de la ligne CODE-BBIS")
    # (P4) le commit de la remise de la première fiche existe, a un seul parent, descend de l'entrée conjointe ; il porte une
    # fois, à l'octet, la ligne de la première fiche ; à son parent, aucune ligne ne cite la première fiche
    parent_remise = seul_parent("P4", c_remise)
    exiger_ancetre("P4", c_conj, c_remise, f"commit de l'entrée conjointe {c_conj[:12]} et commit de la remise {c_remise[:12]}")
    a_la_remise = texte("P4", c_remise, registre).split("\n")
    if a_la_remise.count(l_premiere) != 1:
        raise refus("P4", f"au commit {c_remise[:12]}, le registre propre porte {a_la_remise.count(l_premiere)} fois la ligne de "
                          "la première fiche de l'exception, une fois exigée")
    if any(premiere["chemin"] in l for l in texte("P4", parent_remise, registre).splitlines()):
        raise refus("P4", f"au parent {parent_remise[:12]}, le registre propre cite déjà {premiere['chemin']}")
    # (P5) la remise précède le commit de la course, qui est un ancêtre de la tête de l'arbre de lecture (ou cette tête)
    exiger_commit("P5", c_course)
    exiger_ancetre("P5", c_remise, c_course, f"commit de la remise {c_remise[:12]} et commit de la course {c_course[:12]}")
    tete = git("P5", "rev-list", "--parents", "-n", "1", "HEAD").stdout.decode("utf-8", "replace").split()[:1]
    if len(tete) != 1 or not hexa.fullmatch(tete[0]):
        raise refus("P5", "tête de l'arbre de lecture illisible")
    exiger_ancetre("P5", c_course, tete[0], f"commit de la course {c_course[:12]} et tête {tete[0][:12]}")
    return {"P1": {"etat": "conforme", "commit": c_conj, "parent": parent},
            "P2": {"etat": "conforme", "commit": c_conj, "parent": parent, "registre": registre},
            "P3": {"etat": "conforme", "commit": c_conj, "parent": parent, "accord": go["chemin"], "accord_sha256": go["sha256"],
                   "fiche": code["chemin"], "fiche_sha256": code["sha256"]},
            "P4": {"etat": "conforme", "commit": c_remise, "parent": parent_remise, "descend_de": c_conj},
            "P5": {"etat": "conforme", "commit_remise": c_remise, "commit_course": c_course, "tete": tete[0]}}


def exiger_ordre_propre(lignes: dict, racine: Path | None = None, exception: dict | None = None) -> dict:
    """Ordre du plan, point 2 ; second addendum : une ligne `CODE-BBIS` remplacée se lit SCELLEMENT-BBIS < CODE-BBIS (première)
    < GO-BBIS < CODE-BBIS (remplacement) < SCORES-BBIS. Quatrième addendum (QA-1) : pour le seul couple (`GO-BBIS`, `CODE-BBIS`
    qui fait foi), quand la comparaison stricte échoue, si `racine` et `exception` sont donnés, si les deux dates écrites sont
    égales et si les triplets (date, chemin, empreinte) de `GO-BBIS`, de `CODE-BBIS` et de la ligne remplacée sont ceux de
    `exception`, la preuve d'entrée conjointe est jouée ; si elle passe, ce couple est tenu pour ordonné et la boucle continue.
    Rend `{"regle": "stricte"}`, ou `{"regle": "quatrième addendum", "preuve": …}`. Tout autre échec : refus de la v3, mot pour
    mot, suivi, quand la preuve a été tentée, de son motif. Sans `racine` ni `exception`, la fonction est la v3."""
    lignes, chaine = dict(lignes), list(ORDRE_PROPRE)
    if "CODE-BBIS" in lignes and "remplace" in lignes["CODE-BBIS"]:
        lignes["CODE-BBIS (première)"] = lignes["CODE-BBIS"]["remplace"]
        chaine = ["SCELLEMENT-BBIS", "CODE-BBIS (première)", "GO-BBIS", "CODE-BBIS", "SCORES-BBIS"]
    preuve = None
    for a, b in zip(chaine, chaine[1:]):
        if a in lignes and b in lignes and not lignes[a]["instant"] < lignes[b]["instant"]:
            refus = f"ligne {a} ({lignes[a]['date']}) pas strictement antérieure à {b} ({lignes[b]['date']})"
            triplet = lambda x: (x["date"], x["chemin"], x["sha256"])
            try:
                ouverte = ((a, b) == ("GO-BBIS", "CODE-BBIS") and racine is not None and exception is not None
                           and lignes[a]["date"] == lignes[b]["date"] and lignes[a]["instant"] == lignes[b]["instant"]
                           and all(triplet(lignes[k]) == triplet(exception[e]) for k, e in
                                   (("GO-BBIS", "go_bbis"), ("CODE-BBIS", "code_bbis"),
                                    ("CODE-BBIS (première)", "code_bbis_remplace"))))
            except (KeyError, TypeError):
                ouverte = False
            if not ouverte:
                raise RefusLecture(refus)
            try:
                preuve = preuve_entree_conjointe(racine, exception)
            except RefusLecture as e:
                raise RefusLecture(f"{refus} ; preuve d'entrée conjointe du quatrième addendum refusée : {e}") from None
    return {"regle": "stricte"} if preuve is None else {"regle": "quatrième addendum", "preuve": preuve}
''', 1),
    ("D5",
     r'''        exiger_ordre_propre(propres)
''',
     r'''        res["ordre_propre"] = exiger_ordre_propre(propres, racine,
                                                  EXCEPTION_ORDRE_ADDENDUM_4 if reel else essai.get("exception_ordre"))
''', 1),
    ("D6",
     r'''commande="python -m controle_ia.t07bbis.lecture_v3")''',
     r'''commande="python -m controle_ia.t07bbis.lecture_v4")''', 1),
    ("D6",
     r'''PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v3 --racine''',
     r'''PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v4 --racine''', 1),
]


def appliquer(texte: str, couples) -> str:
    for _, ancien, nouveau, n in couples:
        assert texte.count(ancien) == n, (ancien[:70], texte.count(ancien), n)
        texte = texte.replace(ancien, nouveau)
    return texte


def test_1_la_version_4_est_la_version_3_plus_les_differences_declarees_et_rien_d_autre():
    v3 = (RACINE / V3).read_bytes()
    assert hashlib.sha256(v3).hexdigest() == V3_SHA256                                      # la version 3, à l'octet
    assert (RACINE / V4).read_text(encoding="utf-8") == appliquer(v3.decode("utf-8"), COUPLES)
    assert {d for d, *_ in COUPLES} == {"D1", "D2", "D3 et D4", "D5", "D6"}
    assert ADDENDUM_SHA256 in COUPLES[0][2]                                                  # D1 nomme l'empreinte scellée
    # rien d'autre : mêmes noms publics, plus la constante et la fonction neuves
    assert set(lv4.__all__) - set(lv3.__all__) == {"EXCEPTION_ORDRE_ADDENDUM_4", "preuve_entree_conjointe"}
    assert set(lv3.__all__) - set(lv4.__all__) == set()
    # aucun mode « garde seule » (§ 6.5) : mêmes options de ligne de commande que la version 3
    assert inspect.getsource(lv4.main).replace("lecture_v4", "lecture_v3") == inspect.getsource(lv3.main)


# ------------------------------------------------------------------------------------------- 2. la version 3 est conservée

def _t(date: str) -> int:
    return int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def _l(cle, date, chemin="registres/x.json", sha="a" * 64):
    return f"| {cle} | {date} | {chemin} | {sha} |\n"


def _registre(tmp_path, *lignes):
    p = tmp_path / f"registre-{len(list(tmp_path.glob('registre-*.md')))}.md"
    p.write_text("# essai\n\n" + "".join(lignes), encoding="utf-8")
    return p


BASE = [_l("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z"), _l("CODE-BBIS", "2026-11-16T12:57:51Z", "registres/c1.json"),
        _l("GO-BBIS", "2026-11-16T12:58:51Z")]


def _issue(module, f, *a, **k):
    """(« passe », valeur) ou (« refus », message) : pour comparer les deux versions."""
    try:
        return "passe", f(*a, **k)
    except module.RefusLecture as e:
        return "refus", str(e)


CAS_V3 = {
    "remplacée une fois": (*BASE, _l("CODE-BBIS", "2026-11-17T09:00:00Z", "registres/c2.json", "b" * 64)),
    "trois lignes": (*BASE, _l("CODE-BBIS", "2026-11-17T09:00:00Z"), _l("CODE-BBIS", "2026-11-17T10:00:00Z")),
    "seconde non postérieure": (*BASE, _l("CODE-BBIS", "2026-11-16T12:57:51Z")),
    "accord en double": (*BASE, _l("GO-BBIS", "2026-11-17T09:00:00Z")),
    "remplacement avant l'accord": (BASE[0], BASE[1], _l("CODE-BBIS", "2026-11-16T12:58:00Z"), BASE[2]),
    "remplacement à la seconde de l'accord": (*BASE, _l("CODE-BBIS", "2026-11-16T12:58:51Z", "registres/c2.json", "b" * 64)),
    "scores avant le remplacement": (*BASE, _l("SCORES-BBIS", "2026-11-17T08:00:00Z"), _l("CODE-BBIS", "2026-11-17T09:00:00Z")),
    "scores à la seconde du remplacement": (*BASE, _l("CODE-BBIS", "2026-11-17T09:00:00Z"),
                                            _l("SCORES-BBIS", "2026-11-17T09:00:00Z")),
    "scellement à la seconde de la première fiche": (_l("SCELLEMENT-BBIS", "2026-11-16T12:57:51Z"), BASE[1], BASE[2]),
    "sans remplacement": tuple(BASE),
    "sans remplacement, accord avant la fiche": (BASE[0], _l("CODE-BBIS", "2026-11-16T12:59:00Z"), BASE[2]),
    "chaîne entière stricte": (*BASE, _l("CODE-BBIS", "2026-11-17T09:00:00Z"), _l("SCORES-BBIS", "2026-11-18T09:00:00Z")),
}
REFUS_ATTENDUS_V3 = {"trois lignes": "en double", "seconde non postérieure": "pas strictement postérieure",
                     "accord en double": "en double",
                     "remplacement avant l'accord": "GO-BBIS .* pas strictement antérieure à CODE-BBIS",
                     "remplacement à la seconde de l'accord": "GO-BBIS .* pas strictement antérieure à CODE-BBIS",
                     "scores avant le remplacement": "pas strictement antérieure à SCORES-BBIS",
                     "scores à la seconde du remplacement": "pas strictement antérieure à SCORES-BBIS",
                     "scellement à la seconde de la première fiche": "SCELLEMENT-BBIS .* pas strictement antérieure",
                     "sans remplacement, accord avant la fiche": "CODE-BBIS .* pas strictement antérieure à GO-BBIS"}


@pytest.mark.parametrize("cas", sorted(CAS_V3))
def test_2_sans_exception_memes_passages_memes_refus_memes_messages_que_la_version_3(tmp_path, cas):
    import re
    p = _registre(tmp_path, *CAS_V3[cas])
    lus = {}
    for m in (lv3, lv4):
        lus[m] = _issue(m, m.lire_lignes, p, m.CLES_PROPRES, (), propre=True, remplacables=m.REMPLACABLES_PROPRES)
    assert lus[lv3] == lus[lv4]                                                 # `lire_lignes` : inchangée
    if lus[lv3][0] == "refus":
        assert re.search(REFUS_ATTENDUS_V3[cas], lus[lv3][1])
        return
    lignes = lus[lv4][1]
    i3 = _issue(lv3, lv3.exiger_ordre_propre, lignes)
    for i4 in (_issue(lv4, lv4.exiger_ordre_propre, lignes),                    # sans racine ni exception : la version 3
               _issue(lv4, lv4.exiger_ordre_propre, lignes, tmp_path, None),    # racine seule : la version 3
               _issue(lv4, lv4.exiger_ordre_propre, lignes, None, dict(lv4.EXCEPTION_ORDRE_ADDENDUM_4))):   # exception seule
        assert i4[0] == i3[0]
        if i3[0] == "refus":
            assert i4[1] == i3[1] and re.search(REFUS_ATTENDUS_V3[cas], i4[1])   # mot pour mot
        else:
            assert cas not in REFUS_ATTENDUS_V3 and i4[1] == {"regle": "stricte"}


def test_2_sans_le_droit_de_remplacer_refus_comme_la_version_3(tmp_path):
    p = _registre(tmp_path, *CAS_V3["remplacée une fois"])
    a, b = (_issue(m, m.lire_lignes, p, m.CLES_PROPRES, ("CODE-BBIS",), propre=True) for m in (lv3, lv4))
    assert a == b and a[0] == "refus" and "en double" in a[1]
    r = lv4.lire_lignes(p, lv4.CLES_PROPRES, ("CODE-BBIS",), propre=True, remplacables=lv4.REMPLACABLES_PROPRES)
    assert r["CODE-BBIS"]["chemin"] == "registres/c2.json" and r["CODE-BBIS"]["remplace"]["chemin"] == "registres/c1.json"


# ----------------------------------------------------------------------------------- dépôt git jouet : l'histoire F4 à F8

REG_JOUET = "registres/propre-jouet.md"
F1, F2, GO = "registres/jouet/code-jouet-v1.json", "registres/jouet/code-jouet-v2.json", "registres/jouet/go-jouet-v2.txt"
SC, D1, T, SCORES = "2026-10-01T08:00:00Z", "2026-10-02T09:10:11Z", "2026-10-03T10:20:30Z", "2026-10-04T12:00:00Z"
TXT = {GO: "accord de calcul jouet\n", F1: '{"fiche": "première, jouet"}\n', F2: '{"fiche": "remplaçante, jouet"}\n'}
SHA = {k: hashlib.sha256(v.encode("utf-8")).hexdigest() for k, v in TXT.items()}
VARIANTES_GIT = {  # artefact du § 6.2, point 4 : (lettre, point de la preuve qui refuse, motif attendu)
    "deux-commits-accord-puis-fiche": ("c", "P2", "porte déjà une ligne de clé"),
    "deux-commits-fiche-puis-accord": ("c", "P2", "porte déjà une ligne de clé"),
    "premiere-fiche-inscrite-avant": ("d", "P2", "porte déjà une ligne de clé"),
    "accord-absent-au-parent": ("e", "P3", "absent de l'arbre du parent"),
    "accord-autre-empreinte-au-parent": ("e", "P3", "empreinte autre que celle de la ligne GO-BBIS"),
    "fiche-deja-au-parent": ("f", "P3", "déjà présent dans l'arbre du parent"),
    "deux-parents": ("g", "P1", "2 parent\\(s\\) relevé\\(s\\), un seul exigé"),
    "premiere-absente-au-commit": ("h", "P4", "porte 0 fois la ligne de la première fiche"),
    "premiere-deja-au-parent": ("h", "P4", "cite déjà"),
    "premiere-autre-texte": ("h", "P4", "porte 0 fois la ligne de la première fiche"),
    "remise-sur-une-autre-lignee": ("P4", "P4", "non ancêtre"),
    "remise-non-ancetre-course": ("i", "P5", "non ancêtre"),
    "course-non-ancetre-tete": ("j", "P5", "non ancêtre"),
}


def _git(d: Path, *args) -> str:
    r = subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} : {r.stderr.strip()}")
    return r.stdout.strip()


def _depot(d: Path) -> Path:
    d.mkdir(parents=True, exist_ok=True)
    _git(d, "init", "-q", "-b", "main")
    for k, v in (("user.email", "essai@example.invalid"), ("user.name", "essai"), ("commit.gpgsign", "false")):
        _git(d, "config", k, v)
    return d


def _commit(d: Path, message: str) -> str:
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "--allow-empty", "-m", message)
    return _git(d, "rev-parse", "HEAD")


def _poser(d: Path, rel: str, texte: str) -> None:
    p = d / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")


def histoire(d: Path, v: str | None = None, reg: str = REG_JOUET, sc: str = SC, d1: str = D1, t: str = T,
             t_code: str | None = None, scores: str = SCORES, lignes_tete=None, apres_tete=None) -> SimpleNamespace:
    """Dépôt jouet qui reproduit F4 à F8 : (c0) registre à deux lignes et fichier de l'accord ; (conjoint) un commit à un seul
    parent ajoute ensemble, à la même seconde, la ligne de la fiche remplaçante et celle de l'accord, et la fiche ; (remise) un
    commit insère la ligne de la première fiche ; (course) un commit « de la course » ; (scores) un commit ajoute la ligne des
    scores. `v` : un artefact de `VARIANTES_GIT`. Rend la racine, l'exception jouet aux valeurs de ce dépôt et les commits.
    `lignes_tete` / `apres_tete` (bout en bout) : lignes de tête du registre, et geste joué avant le dernier commit."""
    _depot(d)
    l_sc, l_abs = lignes_tete or (_l("SCELLEMENT-BBIS", sc, "prereg/texte-jouet.md"),
                                  _l("ABSENCE-B-BBIS", sc, "registres/jouet/absence.json", "b" * 64))
    l_prem, l_go = _l("CODE-BBIS", d1, F1, SHA[F1]), _l("GO-BBIS", t, GO, SHA[GO])
    l_code = _l("CODE-BBIS", t_code or t, F2, SHA[F2])
    registre = lambda *ls: _poser(d, reg, "# registre propre jouet\n\n" + "".join(ls))
    tete = [l_sc, l_abs] + ([l_prem] if v == "premiere-fiche-inscrite-avant" else [])
    registre(*tete)
    if v == "premiere-fiche-inscrite-avant":
        _poser(d, F1, TXT[F1])
    if v != "accord-absent-au-parent":
        _poser(d, GO, "un autre accord\n" if v == "accord-autre-empreinte-au-parent" else TXT[GO])
    if v == "fiche-deja-au-parent":
        _poser(d, F2, TXT[F2])
    c0 = _commit(d, "c0 : scellement, constat d'absence, fichier de l'accord")
    c_cote = None
    if v == "remise-sur-une-autre-lignee":
        _git(d, "checkout", "-q", "-b", "cote")
        registre(*tete, l_prem)
        _poser(d, F1, TXT[F1])
        c_cote = _commit(d, "remise sur une autre lignée")
        _git(d, "checkout", "-q", "main")
    if v == "deux-commits-accord-puis-fiche":
        registre(*tete, l_go)
        _commit(d, "accord seul")
    if v == "deux-commits-fiche-puis-accord":
        registre(*tete, l_code)
        _poser(d, F2, TXT[F2])
        _commit(d, "fiche seule")
    if v == "deux-parents":
        _git(d, "checkout", "-q", "-b", "cote")
        _commit(d, "côté")
        _git(d, "checkout", "-q", "main")
        _commit(d, "avance")
        _git(d, "merge", "-q", "--no-ff", "--no-commit", "cote")
    registre(*tete, l_code, l_go)
    _poser(d, GO, TXT[GO])
    _poser(d, F2, TXT[F2])
    c_conj = _commit(d, "entrée conjointe : fiche remplaçante et accord, même seconde")
    c_remise = _commit(d, "commit vide avant la remise") if v == "premiere-absente-au-commit" else None
    if v != "premiere-fiche-inscrite-avant":
        autre = _l("CODE-BBIS", d1[:-3] + "59Z", F1, SHA[F1])
        registre(l_sc, l_abs, autre if v == "premiere-autre-texte" else l_prem, l_code, l_go)
        _poser(d, F1, TXT[F1])
    c = _commit(d, "remise de la première fiche (insertion)")
    c_remise = c_remise or c
    if v == "premiere-autre-texte":
        registre(l_sc, l_abs, l_prem, l_code, l_go)
        _commit(d, "ligne de la première fiche réécrite")
    if v == "premiere-deja-au-parent":
        c_remise = _commit(d, "commit vide après la remise")
    if v == "remise-sur-une-autre-lignee":
        c_remise = c_cote
    if v == "course-non-ancetre-tete":
        _git(d, "checkout", "-q", "-b", "a-part")
        c_course = _commit(d, "commit de la course, à part")
        _git(d, "checkout", "-q", "main")
        _commit(d, "suite sans la course")
    else:
        c_course = _commit(d, "commit de la course")
    if v == "remise-non-ancetre-course":
        c_course = c0
    if apres_tete is not None:
        apres_tete()
    registre(l_sc, l_abs, l_prem, l_code, l_go, _l("SCORES-BBIS", scores, *(apres_tete.scores if apres_tete else
                                                                           ("diag/jouet/sondes.json", "c" * 64))))
    c_scores = _commit(d, "ligne des scores")
    exception = {"registre_propre": reg,
                 "code_bbis_remplace": {"date": d1, "chemin": F1, "sha256": SHA[F1]},
                 "code_bbis": {"date": t_code or t, "chemin": F2, "sha256": SHA[F2]},
                 "go_bbis": {"date": t, "chemin": GO, "sha256": SHA[GO]},
                 "commit_entree_conjointe": c_conj, "commit_remise_premiere_fiche": c_remise, "commit_course": c_course}
    return SimpleNamespace(racine=d, exception=exception, reg=reg, c0=c0, c_conj=c_conj, c_remise=c_remise, c_course=c_course,
                           c_scores=c_scores)


def _lignes(h) -> dict:
    return lv4.lire_lignes(h.racine / h.reg, lv4.CLES_PROPRES, (), propre=True, remplacables=lv4.REMPLACABLES_PROPRES)


def _refus_v3(a, da, b, db) -> str:
    return f"ligne {a} ({da}) pas strictement antérieure à {b} ({db})"


REFUS_GO_CODE = _refus_v3("GO-BBIS", T, "CODE-BBIS", T)


@pytest.fixture
def espion(monkeypatch):
    """Compte les appels de la preuve (la vraie est jouée)."""
    appels, vraie = [], lv4.preuve_entree_conjointe

    def preuve(racine, exception):
        appels.append((racine, exception))
        return vraie(racine, exception)

    monkeypatch.setattr(lv4, "preuve_entree_conjointe", preuve)
    return appels


@pytest.fixture(scope="module")
def sain(tmp_path_factory):
    return histoire(tmp_path_factory.mktemp("histoire-saine") / "depot")


# --------------------------------------------------------------------------------------------- 3. cas sain de l'exception

def test_3_cas_sain_regle_quatrieme_addendum_cinq_points_conformes(sain, espion):
    lignes = _lignes(sain)
    assert lignes["GO-BBIS"]["date"] == lignes["CODE-BBIS"]["date"] == T                      # même seconde
    with pytest.raises(lv3.RefusLecture) as e3:                                              # la version 3 refuse ce registre
        lv3.exiger_ordre_propre(lignes)
    assert str(e3.value) == REFUS_GO_CODE
    r = lv4.exiger_ordre_propre(lignes, sain.racine, sain.exception)
    assert r["regle"] == "quatrième addendum" and len(espion) == 1
    p = r["preuve"]
    assert sorted(p) == ["P1", "P2", "P3", "P4", "P5"] and all(x["etat"] == "conforme" for x in p.values())
    assert p["P1"]["commit"] == sain.c_conj and p["P1"]["parent"] == sain.c0
    assert p["P4"]["commit"] == sain.c_remise and p["P4"]["parent"] == sain.c_conj
    assert p["P5"] == {"etat": "conforme", "commit_remise": sain.c_remise, "commit_course": sain.c_course,
                       "tete": sain.c_scores}
    json.dumps(r)                                                                            # écrivable dans le fichier de lecture
    assert lv4.preuve_entree_conjointe(sain.racine, sain.exception) == p                     # la preuve seule, même relevé


def test_3_la_tete_peut_etre_le_commit_de_la_course(tmp_path):
    h = histoire(tmp_path / "depot")
    _git(h.racine, "checkout", "-q", "--detach", h.c_course)                                 # registre sans la ligne des scores
    r = lv4.exiger_ordre_propre(_lignes(h), h.racine, h.exception)
    assert r["regle"] == "quatrième addendum" and r["preuve"]["P5"]["tete"] == h.c_course


def test_3_arbre_de_travail_separe_a_histoire_complete(tmp_path):
    h = histoire(tmp_path / "depot")
    arbre = tmp_path / "arbre-de-lecture"
    _git(h.racine, "worktree", "add", "-q", "--detach", str(arbre), h.c_scores)
    h2 = SimpleNamespace(racine=arbre, reg=h.reg)
    assert lv4.exiger_ordre_propre(_lignes(h2), arbre, h.exception)["regle"] == "quatrième addendum"


# ----------------------------------------------------------------------------------------- 4. artefacts de l'exception

def _exception_modifiee(exc: dict, ligne: str, champ: str) -> dict:
    autre = {"date": "2026-10-03T10:20:31Z", "chemin": "registres/jouet/un-autre-fichier.json", "sha256": "d" * 64}
    return {**exc, ligne: {**exc[ligne], champ: autre[champ]}}


@pytest.mark.parametrize("ligne", ["go_bbis", "code_bbis", "code_bbis_remplace"])
@pytest.mark.parametrize("champ", ["date", "chemin", "sha256"])
def test_4a_meme_seconde_mais_une_ligne_autre_que_celle_de_l_exception_refus_de_la_version_3(sain, espion, ligne, champ):
    with pytest.raises(lv4.RefusLecture) as e:
        lv4.exiger_ordre_propre(_lignes(sain), sain.racine, _exception_modifiee(sain.exception, ligne, champ))
    assert str(e.value) == REFUS_GO_CODE and espion == []                    # mot pour mot ; la preuve n'est pas tentée


def test_4a_une_autre_seconde_commune_que_celle_de_l_exception(tmp_path, sain, espion):
    autre = "2026-10-03T10:20:31Z"
    h = histoire(tmp_path / "depot", t=autre)                                # registre : les deux lignes à une autre seconde
    with pytest.raises(lv4.RefusLecture) as e:
        lv4.exiger_ordre_propre(_lignes(h), h.racine, sain.exception)        # exception : la seconde T
    assert str(e.value) == _refus_v3("GO-BBIS", autre, "CODE-BBIS", autre) and espion == []


@pytest.mark.parametrize("exception", [{}, {"go_bbis": None}, "exception", 7])
def test_4a_exception_mal_formee_refus_de_la_version_3(sain, espion, exception):
    with pytest.raises(lv4.RefusLecture) as e:
        lv4.exiger_ordre_propre(_lignes(sain), sain.racine, exception)
    assert str(e.value) == REFUS_GO_CODE and espion == []


def test_4b_fiche_remplacante_une_seconde_avant_l_accord(tmp_path, espion):
    avant = "2026-10-03T10:20:29Z"
    h = histoire(tmp_path / "depot", t_code=avant)                           # l'exception jouet porte ces mêmes lignes
    with pytest.raises(lv4.RefusLecture) as e:
        lv4.exiger_ordre_propre(_lignes(h), h.racine, h.exception)
    assert str(e.value) == _refus_v3("GO-BBIS", T, "CODE-BBIS", avant) and espion == []


@pytest.mark.parametrize("v", sorted(VARIANTES_GIT))
def test_4c_a_4j_histoire_autre_que_celle_de_l_addendum_refus_motive(tmp_path, espion, v):
    import re
    _lettre, point, motif = VARIANTES_GIT[v]
    h = histoire(tmp_path / "depot", v)
    lignes = _lignes(h)
    assert lignes == _lignes(histoire(tmp_path / "temoin"))                  # le registre lu est celui du cas sain, à l'octet
    with pytest.raises(lv4.RefusLecture) as e:
        lv4.exiger_ordre_propre(lignes, h.racine, h.exception)
    prefixe = f"{REFUS_GO_CODE} ; preuve d'entrée conjointe du quatrième addendum refusée : preuve d'entrée conjointe, " \
              f"point ({point}) : "
    assert str(e.value).startswith(prefixe) and re.search(motif, str(e.value)[len(prefixe):]), str(e.value)
    assert len(espion) == 1                                                   # la preuve a été tentée, elle a refusé
    with pytest.raises(lv4.RefusLecture, match=re.escape(f"point ({point})")):
        lv4.preuve_entree_conjointe(h.racine, h.exception)


@pytest.mark.parametrize("cle,point", [("commit_entree_conjointe", "P1"), ("commit_remise_premiere_fiche", "P4"),
                                       ("commit_course", "P5")])
@pytest.mark.parametrize("valeur", ["0123456789abcdef0123456789abcdef01234567", "HEAD", "--all", "c098fb5", None])
def test_4k_commit_nomme_absent_ou_mal_forme(sain, cle, point, valeur):
    with pytest.raises(lv4.RefusLecture) as e:
        lv4.exiger_ordre_propre(_lignes(sain), sain.racine, {**sain.exception, cle: valeur})
    assert str(e.value).startswith(REFUS_GO_CODE + " ; preuve d'entrée conjointe du quatrième addendum refusée : ")
    assert f"point ({point})" in str(e.value)
    assert ("absent du dépôt" in str(e.value)) == (valeur is not None and len(valeur) == 40)
    assert ("40 caractères hexadécimaux attendus" in str(e.value)) == (valeur is None or len(valeur) != 40)


def test_4k_depot_superficiel(tmp_path, sain):
    clone = tmp_path / "clone-superficiel"
    _git(tmp_path, "clone", "-q", "--depth", "1", sain.racine.as_uri(), str(clone))
    assert _git(clone, "rev-parse", "HEAD") == sain.c_scores and _git(clone, "rev-list", "--count", "HEAD") == "1"
    h = SimpleNamespace(racine=clone, reg=sain.reg)
    assert _lignes(h) == _lignes(sain)
    with pytest.raises(lv4.RefusLecture, match=r"point \(P1\) : commit .* absent du dépôt"):
        lv4.exiger_ordre_propre(_lignes(h), clone, sain.exception)


def test_4k_une_commande_git_en_echec_n_est_jamais_un_passage(tmp_path, sain, monkeypatch):
    lignes = _lignes(sain)
    hors = tmp_path / "pas-un-depot"
    hors.mkdir()
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))            # ne remonte vers aucun dépôt
    with pytest.raises(lv4.RefusLecture, match=r"point \(P1\)"):
        lv4.exiger_ordre_propre(lignes, hors, sain.exception)
    monkeypatch.delenv("GIT_CEILING_DIRECTORIES")
    vrai = subprocess.run

    def echec_de(sous_commande, code):
        def run(cmd, **k):
            r = vrai(cmd, **k)
            return subprocess.CompletedProcess(cmd, code, r.stdout, b"panne") if sous_commande in cmd else r
        return run

    for sous_commande, code, motif in (("merge-base", 128, "échec de git"), ("merge-base", 2, "échec de git"),
                                       ("merge-base", 1, "non ancêtre"), ("show", 128, "échec de git"),
                                       ("ls-tree", 1, "échec de git"), ("rev-list", 129, "échec de git"),
                                       ("cat-file", 1, "absent du dépôt")):
        monkeypatch.setattr(lv4.subprocess, "run", echec_de(sous_commande, code))
        with pytest.raises(lv4.RefusLecture, match=motif):
            lv4.exiger_ordre_propre(lignes, sain.racine, sain.exception)

    def absent(cmd, **k):
        raise FileNotFoundError("git")

    monkeypatch.setattr(lv4.subprocess, "run", absent)
    with pytest.raises(lv4.RefusLecture, match="échec de git"):
        lv4.exiger_ordre_propre(lignes, sain.racine, sain.exception)
    monkeypatch.setattr(lv4.subprocess, "run", vrai)
    assert lv4.exiger_ordre_propre(lignes, sain.racine, sain.exception)["regle"] == "quatrième addendum"


@pytest.mark.parametrize("scores", [T, "2026-10-03T10:20:29Z"])
def test_4l_scores_egaux_ou_inverses_avec_le_cas_sain_de_l_exception(tmp_path, espion, scores):
    h = histoire(tmp_path / "depot", scores=scores)
    lignes = _lignes(h)
    assert lv4.preuve_entree_conjointe(h.racine, h.exception)["P5"]["etat"] == "conforme"    # la preuve passe
    espion.clear()
    with pytest.raises(lv4.RefusLecture) as e:
        lv4.exiger_ordre_propre(lignes, h.racine, h.exception)
    assert str(e.value) == _refus_v3("CODE-BBIS", T, "SCORES-BBIS", scores)                  # refus de la version 3, mot pour mot
    assert len(espion) == 1                                                                  # après la preuve : la boucle continue


def test_4l_scellement_a_la_seconde_de_la_premiere_fiche_avec_le_cas_sain_de_l_exception(tmp_path, espion):
    h = histoire(tmp_path / "depot", sc=D1)
    assert lv4.preuve_entree_conjointe(h.racine, h.exception)["P1"]["etat"] == "conforme"
    espion.clear()
    with pytest.raises(lv4.RefusLecture) as e:
        lv4.exiger_ordre_propre(_lignes(h), h.racine, h.exception)
    assert str(e.value) == _refus_v3("SCELLEMENT-BBIS", D1, "CODE-BBIS (première)", D1) and espion == []


# ------------------------------------------------------------------------------------------ 5. lecture réelle verrouillée

def test_5_la_constante_porte_les_valeurs_de_QA_1_a_l_octet():
    attendu = {  # valeurs recopiées du quatrième addendum (F1, QA-1, F4)
        "registre_propre": "registres/t07-etape-b-bis-v1.md",
        "code_bbis_remplace": {"date": "2026-11-16T12:57:27Z", "chemin": "registres/t07-etape-b-bis/code-bbis-v1.json",
                               "sha256": "ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469"},
        "code_bbis": {"date": "2026-11-17T11:05:29Z", "chemin": "registres/t07-etape-b-bis/code-bbis-v2.json",
                      "sha256": "4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb"},
        "go_bbis": {"date": "2026-11-17T11:05:29Z", "chemin": "registres/t07-etape-b-bis/go-bbis-v2.txt",
                    "sha256": "33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62"},
        "commit_entree_conjointe": "c098fb512d999e1dbf7cef5fba6430ff8b1a8fb5",
        "commit_remise_premiere_fiche": "06c8832819af344d01c184222833c5a42e8ac901",
        "commit_course": "438a9c5257bdc4fa65f25c42cc89753a049b4586"}
    assert lv4.EXCEPTION_ORDRE_ADDENDUM_4 == attendu
    from controle_ia.t07bbis.registre_bbis_v1 import REGISTRE_PROPRE
    assert attendu["registre_propre"] == REGISTRE_PROPRE
    # les mêmes valeurs, relevées dans le texte scellé de l'addendum (texte de spécification, non un registre)
    octets = (RACINE / ADDENDUM).read_bytes()
    assert hashlib.sha256(octets).hexdigest() == ADDENDUM_SHA256
    texte = octets.decode("utf-8")
    e = lv4.EXCEPTION_ORDRE_ADDENDUM_4
    for cle, nom in (("CODE-BBIS", "code_bbis_remplace"), ("CODE-BBIS", "code_bbis"), ("GO-BBIS", "go_bbis")):
        x = e[nom]
        assert texte.count(f"| {cle} | {x['date']} | {x['chemin']} | {x['sha256']} |\n") == 1          # lignes de F1
        assert f"datée {x['date']} qui cite `{x['chemin']}` à l'empreinte {x['sha256']}" in texte        # bloc de QA-1
    for point, nom in (("(P1) le commit", "commit_entree_conjointe"), ("(P4) le commit", "commit_remise_premiere_fiche"),
                       ("ancêtre du commit de la course", "commit_course")):
        assert f"{point} `{e[nom]}`" in texte


def test_5_aucun_parametre_ne_remplace_la_constante_en_lecture_reelle():
    assert inspect.signature(lv4.lire) == inspect.signature(lv3.lire)
    assert inspect.signature(lv4.main) == inspect.signature(lv3.main)
    assert inspect.signature(lv4.ecrire_lecture) == inspect.signature(lv3.ecrire_lecture)
    source = (RACINE / V4).read_text(encoding="utf-8")
    assert source.count("EXCEPTION_ORDRE_ADDENDUM_4") == 3          # docstring (D1), définition (D2), un seul usage, dans `lire` (D5)
    assert source.count("EXCEPTION_ORDRE_ADDENDUM_4 = {") == 1
    assert source.count("EXCEPTION_ORDRE_ADDENDUM_4 if reel else essai.get(\"exception_ordre\")") == 1
    assert source.count("exception_ordre") == 1 and source.count("exiger_ordre_propre(") == 3   # D1, définition, `lire`
    assert "exception" not in inspect.getsource(lv4.main) and "exception" not in inspect.getsource(lv4.ecrire_lecture)
    v3 = (RACINE / V3).read_text(encoding="utf-8")
    for acces in ("os.environ", "getenv", "argparse", "add_argument", "sys.argv"):
        assert source.count(acces) == v3.count(acces)               # ni variable d'environnement ni option de plus


@pytest.mark.parametrize("essai,attendue", [(None, "constante"), ({}, None), ({"n_tirages": 3}, None),
                                            ({"exception_ordre": {"jouet": 1}}, {"jouet": 1})])
def test_5_lire_passe_la_constante_en_lecture_reelle_et_l_exception_de_l_essai_en_mode_jouet(tmp_path, monkeypatch, essai,
                                                                                               attendue):
    """Registre jouet (lignes rendues par un espion) ; la garde d'ordre est remplacée par un espion qui relève ses arguments et
    refuse : rien d'autre n'est lu."""
    vus = []
    ligne = {"date": "2026-10-01T08:00:00Z", "instant": 1, "chemin": "x", "sha256": "a" * 64}
    monkeypatch.delenv("BBIS_INSTANCE", raising=False)
    monkeypatch.setenv("EXCEPTION_ORDRE_ADDENDUM_4", "autre")                # une variable d'environnement n'y change rien
    monkeypatch.setattr(lv4, "lire_lignes", lambda *a, **k: {"SCELLEMENT-BBIS": dict(ligne)})
    monkeypatch.setattr(lv4, "verifier_lignes", lambda *a, **k: None)

    def espion(*a, **k):
        vus.append((a, k))
        raise lv4.RefusLecture("espion de l'essai")

    monkeypatch.setattr(lv4, "exiger_ordre_propre", espion)
    res = lv4.lire(tmp_path, "run-7b-jouet", "run-bbis-jouet", 2, essai=essai)
    assert res["issue"] == lv4.issue_complete({}, {}, None, motif_i0="garde refusée (espion de l'essai)")
    assert res["garde"] == {"refus": "espion de l'essai"} and "ordre_propre" not in res and "entrees_lues" not in res
    (a, k), = vus
    assert k == {} and len(a) == 3 and a[1] == tmp_path
    if attendue == "constante":
        assert a[2] is lv4.EXCEPTION_ORDRE_ADDENDUM_4 and res["essai"] is False
    else:
        assert a[2] == attendue and res["essai"] is True


# ------------------------------------------------------------------------------------- 6. de bout en bout, en mode jouet

@pytest.fixture(scope="module")
def course(tmp_path_factory):
    """Course jouet de T0.6, marche jouet de B bis, puis registres jouets dont l'histoire git reproduit F4 à F8 (forme de
    `test_F…` du second addendum). Aucune donnée réelle."""
    import aide_t07bbis_jouet_v1 as aide
    from controle_ia.scellement import empreinte, sceller
    from controle_ia.t07bbis import commun_v1 as cm
    from controle_ia.t07bbis import marche_v4
    from controle_ia.t07bbis import registre_bbis_v2 as rb2
    if not aide.disponible():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    run_b, entropie = "20261118-090000-bbis-jouet", 2 ** 100 + 11
    d = aide.course_jouet(tmp_path_factory.mktemp("depot-bbis-lecture-v4"))
    _git(d, "config", "commit.gpgsign", "false")
    r = marche_v4.marche(d, aide.RUN, run_b, entropie, d.parent / f"{d.name}-travail", "cpu",
                         essai={"epoques": 15, "n_plis_internes": 3, "n_directions": 12, "n_reetiquetages": 3, "n_controle": 6,
                                "n_chemin": 3})
    assert r.get("scores_ecrits"), r
    v = d / "docs" / "verdicts" / "verdict-p3bis-jouet.md"
    v.parent.mkdir(parents=True)
    v.write_text("verdict jouet\n", encoding="utf-8")
    sha_issue = aide.sceller_json(d, "docs/verdicts/issue-p3bis-jouet.json",
                                  {"issue": "vu", "ligne": 5, "verdict": "docs/verdicts/verdict-p3bis-jouet.md",
                                   "verdict_sha256": empreinte(v)})
    sha_m = (d / "runs" / aide.RUN / "manifeste.json.sha256").read_text(encoding="utf-8").split()[0]
    (d / "registres").mkdir(exist_ok=True)
    (d / rb2.REGISTRE_PARTAGE).write_text(
        "# registre jouet\n\n" + _l("RUN-CONFIRMATION-T06", "2026-09-12T05:00:00Z", f"runs/{aide.RUN}/manifeste.json", sha_m)
        + _l("VERDICT-P3BIS", "2026-09-13T05:00:00Z", "docs/verdicts/issue-p3bis-jouet.json", sha_issue), encoding="utf-8")
    absence = "registres/t07-etape-b-bis/ABSENCE-B-BBIS-jouet-v1.json"
    sha_abs = aide.sceller_json(d, absence, {"absents": True})
    fiche = lambda e: {"commit": "c" * 40, "fichiers": {"src/x.py": "a" * 64}, "entropie": str(e),
                       "epreuve_niveau": {"chemin": "e.json", "sha256": "b" * 64, "niveau_decisif_retenu": 0.99},
                       "niveau_decisif": 0.99}
    octets = lambda x: json.dumps(x, ensure_ascii=False, indent=1) + "\n"
    avant = dict(TXT), dict(SHA)
    TXT.update({F1: octets(fiche(2 ** 100 + 99)), F2: octets(fiche(entropie))})        # fiches lisibles par la lecture
    SHA.update({k: hashlib.sha256(x.encode("utf-8")).hexdigest() for k, x in TXT.items()})

    def compagnons():                                                                   # sceaux des fichiers cités
        for k in (F1, F2, GO):
            assert sceller(d / k) == SHA[k]

    compagnons.scores = (r["sondes_bbis"], r["sondes_bbis_sha256"])
    try:
        h = histoire(d, reg=rb2.REGISTRE_PROPRE, apres_tete=compagnons,
                     lignes_tete=(_l("SCELLEMENT-BBIS", SC, cm.TEXTE, cm.TEXTE_SHA256), _l("ABSENCE-B-BBIS", SC, absence, sha_abs)))
    finally:
        TXT.clear(), TXT.update(avant[0]), SHA.clear(), SHA.update(avant[1])
    return SimpleNamespace(h=h, d=d, run_7b=aide.RUN, run_b=run_b, entropie=entropie,
                           essai={"n_directions": 12, "n_nul": 3, "n_tirages": 60})


def test_6_de_bout_en_bout_cas_sain_la_garde_passe_et_le_fichier_de_lecture_porte_ordre_propre(course):
    c = course
    res = lv4.lire(c.d, c.run_7b, c.run_b, _t("2026-11-19T09:00:00Z"), essai={**c.essai, "exception_ordre": c.h.exception})
    assert "garde" not in res, res.get("garde")
    assert res["ordre_propre"]["regle"] == "quatrième addendum"
    assert all(res["ordre_propre"]["preuve"][p]["etat"] == "conforme" for p in ("P1", "P2", "P3", "P4", "P5"))
    assert res["lignes"]["propres"]["CODE-BBIS"]["chemin"] == F2 and res["lignes"]["propres"]["CODE-BBIS"]["remplace"]["chemin"] == F1
    assert res["cellules"] and all(x.get("etat") is not None for x in res["cellules"].values())   # la lecture jouet se déroule
    assert not any("R-ORDRE" in x for x in res["reserves"])                    # la réserve R-ORDRE n'est pas écrite par le module
    chemin = lv4.ecrire_lecture(c.d, "20261119-090000-lecture-bbis-jouet", res, c.entropie, reel=False)
    doc = json.loads(chemin.read_text(encoding="utf-8"))
    assert chemin.name == "lecture-bbis.json" and doc["resultat"]["ordre_propre"] == res["ordre_propre"]
    manifeste = json.loads((c.d / "runs" / "20261119-090000-lecture-bbis-jouet" / "manifeste.json").read_text(encoding="utf-8"))
    assert "python -m controle_ia.t07bbis.lecture_v4" in json.dumps(manifeste)             # D6


@pytest.mark.parametrize("artefact", ["sans exception", "commit absent", "course non ancêtre", "ligne autre"])
def test_6_de_bout_en_bout_artefact_issue_I0_garde_refusee_aucune_entree_ouverte(course, monkeypatch, artefact):
    c = course
    exception = {"sans exception": None,
                 "commit absent": {**c.h.exception, "commit_entree_conjointe": "0123456789abcdef0123456789abcdef01234567"},
                 "course non ancêtre": {**c.h.exception, "commit_course": c.h.c0},
                 "ligne autre": _exception_modifiee(c.h.exception, "go_bbis", "sha256")}[artefact]

    def interdit(self, rel):
        raise AssertionError(f"entrée ouverte malgré le refus de la garde : {rel}")

    monkeypatch.setattr(lv4.GardeEntrees, "exiger", interdit)
    essai = dict(c.essai) if exception is None else {**c.essai, "exception_ordre": exception}
    res = lv4.lire(c.d, c.run_7b, c.run_b, _t("2026-11-19T09:00:00Z"), essai=essai)       # un refus, jamais un arrêt du programme
    assert res["garde"]["refus"].startswith(REFUS_GO_CODE)
    assert ("preuve d'entrée conjointe du quatrième addendum refusée" in res["garde"]["refus"]) == (
        artefact in ("commit absent", "course non ancêtre"))
    assert res["issue"] == lv4.issue_complete({}, {}, None, motif_i0=f"garde refusée ({res['garde']['refus']})")
    assert "I0" in json.dumps(res["issue"], ensure_ascii=False) and "garde refusée (" in json.dumps(res["issue"], ensure_ascii=False)
    assert "Étape B bis non lue : garde refusée (" in json.dumps(res["issue"], ensure_ascii=False)
    for cle in ("ordre_propre", "entrees_lues", "cellules", "lignes", "p3bis", "anteriorite"):
        assert cle not in res
