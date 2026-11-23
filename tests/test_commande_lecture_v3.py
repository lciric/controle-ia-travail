"""Épreuves du code de commande de la relecture, version 3 (`controle_ia.barreau5_familles.commande_lecture_v3`,
`scripts/lancer_b5f_lecture_v3.sh`) : erratum de chaîne de la relecture décisive du barreau 5, v2 (`01298f0f…`), § 4.3
et § 6.2, et les trois précisions de sa vérification ; cas sain et artefact pour chaque garde (R5). Écrites avant le module.

Monde d'essai, sur le modèle de `tests/test_commande_lecture_v2.py` (dont les aides sont importées, déclaré) : un dépôt
jetable relié à un dépôt distant local, qui porte tout `src/` sans les listes fermées des versions 2 et 3 ; le « code » (rôle
du commit du code de lecture figé) ; le « commit v2 » (le code plus la liste fermée de la version 2) ; le « commit v3 » (le
commit v2 plus les sept fichiers de l'erratum, et rien d'autre) ; la « marche » (le code plus le registre propre, dont la
ligne de l'accord de lecture cite l'additif et le commit v2, et dont une ligne libre sous la table épingle le commit v3).
Trois arbres : l'arbre figé (à la marche), l'arbre v2 (au commit v2, pour la comparaison) et l'arbre de commande (au commit
v3). Aucun essai n'atteint le réseau, ne crée, n'arrête ni ne détruit d'instance ; aucune clé n'est lue.
"""
from __future__ import annotations

import ast
import base64
import difflib
import hashlib
import inspect
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
import unicodedata
from datetime import date
from pathlib import Path

import pytest

import test_commande_lecture_v2 as t2               # aides du monde d'essai de la version 2 (déclaré)
from controle_ia.barreau5_familles import commande_lecture_v2 as cl2
from controle_ia.barreau5_familles import commande_lecture_v3 as cl3
from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import formation_v1 as fv
from controle_ia.barreau5_familles import lecture_v1 as lv
from controle_ia.barreau5_familles import relecture_v1 as rv
from controle_ia.gardes import GardeArret

RACINE = Path(__file__).resolve().parents[1]
ERRATUM = "01298f0f73a731e6ee31e0e91b45367da75ba1bd2276ba5d041000b9f87da87b"
ERRATUM_V1 = "d4b5ff14a910b693f910906ad4c044c57b0cb6e1896e49eca641107f94812702"
ACCORD = "GO-2026-11-22-147"
SORTIE = "donnees/barreau5-familles-jumelles-v1-lecture"
FIGEE, CORRIGEE = ("54a676f35bde811e8ebcfb0f643d510c2a1a79ca6a8554d61b7a39dd8e44453f",
                   "0adb6efba0a430f11c30e01da52787ef0482e20f6d74f699dbe8d76d2d300001")
# la ligne 362 de l'amorce et la ligne ajoutée, recopiées de l'erratum (§ 3.1)
L362 = ('    git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch '
        '"$BRANCHE_ENTREES" "$DEPOT_URL" "$E" || arret "clonage des entrées de lecture" 2')
AJOUT = ('    git -C "$E" config credential.helper "$AIDE" || arret "aide d\'identification non inscrite dans le clone des '
         'entrées" 2')
SEPT = ("scripts/lancer_b5f_lecture_v3.sh", "scripts/lancer_b5f_ouverture_suffixes_v1.sh",
        "src/controle_ia/barreau5_familles/commande_lecture_v3.py", "src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py",
        "tests/test_amorce_b5f_lecture_identification_v1.py", "tests/test_commande_lecture_v3.py",
        "tests/test_ouverture_suffixes_v1.py")
MODULE_V3, LANCEUR_V3 = "src/controle_ia/barreau5_familles/commande_lecture_v3.py", "scripts/lancer_b5f_lecture_v3.sh"
MODULE_OUV = "src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py"
_g = t2._g
GO_LECTURE, GO_FORMATION, RUN_L = t2.GO_LECTURE, t2.GO_FORMATION, t2.RUN_L


def epinglage(k3, erratum=ERRATUM, accord=ACCORD, branche=SORTIE, rapport="f" * 64):
    """La ligne d'épinglage, au format exact de l'erratum (§ 4.3 (d))."""
    return (f"Erratum de chaîne de la relecture décisive (barreau 5) : erratum sha256 {erratum} ; code de commande v3 et "
            f"d'ouverture à noms suffixés v1, commit {k3}, vérifié sha256 {rapport} ; accord {accord} ; branche de sortie "
            f"{branche}")


def registre_v3(code, k2, k3, lignes=None):
    """Registre propre de la marche : table de la version 2 (citation du commit v2), puis, sous la table, une note et la
    ligne d'épinglage (ou les lignes données)."""
    sous = [epinglage(k3)] if lignes is None else list(lignes)
    return t2._registre(code, t2._citation(k2)) + "\nNote sous la table.\n" + "".join(x + "\n" for x in sous)


# --- fabrique du monde d'essai -----------------------------------------------------------------------------------------

@pytest.fixture(scope="module")
def gabarit3(tmp_path_factory):
    """Comme le gabarit de la version 2, sans les deux listes fermées sous `src/`."""
    t = tmp_path_factory.mktemp("gabarit-b5f-commande-v3")
    nu, r = t / "distant.git", t / "fige"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(nu)], check=True)
    subprocess.run(["git", "clone", "-q", str(nu), str(r)], check=True, capture_output=True)
    for a in (["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _g(r, *a)
    liste = {(RACINE / f).resolve() for f in cl2.LISTE_FERMEE + SEPT}

    def ignorer(dossier, noms):
        return [n for n in noms if n == "__pycache__" or n.endswith((".pyc", ".egg-info"))
                or (Path(dossier) / n).resolve() in liste]
    shutil.copytree(RACINE / "src", r / "src", ignore=ignorer)
    (r / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE / ".claude" / "hooks" / "garde_calcul.py", r / ".claude" / "hooks" / "garde_calcul.py")
    (r / "prereg").mkdir()
    for f in (rv.CONFIG_SCELLEE["chemin"], rv.CONFIG_SCELLEE["chemin"] + ".sha256", lv.TEXTE):
        shutil.copy(RACINE / f, r / f)
    (r / "scripts").mkdir()
    for f in (rv.AMORCE, t2.LANCEUR_V1):
        shutil.copy(RACINE / f, r / f)
    (r / ".gitignore").write_text("__pycache__/\n*.pyc\n", encoding="utf-8")
    (r / "registres").mkdir()
    (r / "registres" / "go.md").write_text("| id | accordé | type | périmètre | plafond | échéance | par | réf |\n"
                                          + t2._ligne_go(GO_LECTURE) + "\n" + t2._ligne_go(GO_FORMATION) + "\n",
                                          encoding="utf-8")
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "code")
    _g(r, "push", "-q", "origin", "main")
    e = t / "entrees-graine"
    e.mkdir()
    for a in (["init", "-q", "-b", "x"], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _g(e, *a)
    (e / rv.DOSSIER_ENTREES).mkdir()
    (e / rv.DOSSIER_ENTREES / "X-01.safetensors").write_bytes(b"x")
    _g(e, "add", "-A")
    _g(e, "commit", "-q", "-m", "entrées de lecture")
    _g(e, "push", "-q", str(nu), f"x:refs/heads/{rv.BRANCHE_ENTREES}")
    _g(r, "fetch", "-q", "origin")
    return {"t": t, "code": _g(r, "rev-parse", "HEAD"), "entrees": _g(e, "rev-parse", "HEAD")}


@pytest.fixture
def monde3(gabarit3, tmp_path):
    shutil.copytree(gabarit3["t"] / "fige", tmp_path / "fige", symlinks=True)
    for nom, corps in (("offre.json", t2.OFFRE), ("aucun.json", [])):
        (tmp_path / nom).write_text(json.dumps(corps))
    return {"t": tmp_path, "fige": tmp_path / "fige", "commande": tmp_path / "commande", "v2": tmp_path / "v2",
            "code": gabarit3["code"], "entrees": gabarit3["entrees"], "maintenant_s": time.time()}


def monter3(m, *, dans_v2=None, dans_v3=None, v3_parent=None, lignes=None, dans_marche=None):
    """Commit v2 (le code plus la liste fermée de la version 2 ; `dans_v2` retouche), commit v3 (le commit v2 plus les
    sept fichiers ; `dans_v3` retouche l'arbre, ou l'index, avant le commit ; `v3_parent` : autre parent, même arbre),
    marche (registre : citation du commit v2, épinglage du commit v3, ou `lignes(k3)` sous la table). L'arbre de commande
    reste au commit v3, l'arbre v2 au commit v2, l'arbre figé à la marche."""
    r, c = m["fige"], m["commande"]
    _g(r, "worktree", "add", "-q", "-b", "commande", str(c), m["code"])
    for f in cl2.LISTE_FERMEE:
        (c / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE / f, c / f)
    if dans_v2 is not None:
        dans_v2(c)
    _g(c, "add", "-A")
    _g(c, "commit", "-q", "-m", "commande de lecture v2")
    k2 = _g(c, "rev-parse", "HEAD")
    for f in SEPT:
        (c / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE / f, c / f)
    _g(c, "add", "-A")
    if dans_v3 is not None:
        dans_v3(c)
    _g(c, "commit", "-q", "-m", "commande de lecture v3 et ouverture à noms suffixés v1")
    k3 = _g(c, "rev-parse", "HEAD")
    if v3_parent is not None:
        k3 = _g(c, "commit-tree", f"{k3}^{{tree}}", "-p", v3_parent(m, k2), "-m", "v3 sur un autre parent")
        _g(c, "checkout", "-q", "--detach", k3)
    _g(r, "worktree", "add", "-q", "--detach", str(m["v2"]), k2)
    if dans_marche is not None:
        dans_marche(r)
    texte = registre_v3(m["code"], k2, k3, None if lignes is None else lignes(k3))
    (r / en.REGISTRE_PROPRE).write_text(texte, encoding="utf-8")
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "marche (registre)")
    m.update(k2=k2, k3=k3, marche=_g(r, "rev-parse", "HEAD"))
    return m


def _args(m, **k):
    a = {"offre_json": m["t"] / "offre.json", "commit": m["marche"], "branche": "main", "run_id": RUN_L,
         "go_id": GO_LECTURE, "entrees_commit": m["entrees"], "divergence": True, "garde": "une_sur_dix",
         "existants_json": m["t"] / "aucun.json"}
    a.update(k)
    return ("decisif", a["offre_json"], a["commit"], a["branche"], a["run_id"], a["go_id"], a["entrees_commit"],
            a["divergence"], a["garde"], a["existants_json"], date.today(), m["maintenant_s"])


def corps3(m, **k):
    return cl3.corps_recompose(m["commande"], *_args(m, **k))


def corps2(m, **k):
    return cl2.corps_recompose(m["v2"], *_args(m, **k))


def _segment(cmd):
    return re.search(r"echo (\S+) \| base64 -d > /root/amorce_b5f_lecture_v1\.sh", cmd).group(1)


# --- constantes et liste fermée (§ 4.3 (a) et (b)) ----------------------------------------------------------------------

def test_constantes_de_l_erratum():
    assert cl3.ERRATUM_SHA256 == ERRATUM and cl3.ACCORD_RELANCE == ACCORD
    assert cl3.AMORCE_FIGEE_SHA256 == FIGEE and cl3.AMORCE_CORRIGEE_SHA256 == CORRIGEE
    assert cl3.BRANCHE_SORTIE == SORTIE == rv.PIECES_LECTURE["decisif"]["branche"]
    assert tuple(cl3.LISTE_FERMEE_V3) == tuple(sorted(SEPT)) and len(set(cl3.LISTE_FERMEE_V3)) == 7
    assert not set(cl3.LISTE_FERMEE_V3) & set(cl2.LISTE_FERMEE)
    for f in SEPT:
        assert (RACINE / f).is_file(), f
    assert cl3.PAIRE_AMORCE == ((L362 + "\n").encode("utf-8"), (L362 + "\n" + AJOUT + "\n").encode("utf-8"))
    assert unicodedata.is_normalized("NFC", AJOUT) and Path(cl3.__file__).resolve() == (RACINE / MODULE_V3).resolve()


# --- l'amorce corrigée (§ 3.1, § 4.3 (c)) --------------------------------------------------------------------------------

def test_amorce_corrigee_cas_sain_une_ligne_ajoutee_apres_la_ligne_362():
    figee = (RACINE / rv.AMORCE).read_bytes()
    assert hashlib.sha256(figee).hexdigest() == FIGEE
    corrigee = cl3.amorce_corrigee(figee)
    assert hashlib.sha256(corrigee).hexdigest() == CORRIGEE and len(corrigee) == 33_536
    a, b = figee.decode("utf-8").split("\n"), corrigee.decode("utf-8").split("\n")
    assert len(b) == len(a) + 1 and b[361] == L362 and b[362] == AJOUT and b[:362] + b[363:] == a
    assert b"\r" not in corrigee and unicodedata.is_normalized("NFC", corrigee.decode("utf-8"))


@pytest.mark.parametrize("cas", ["autre_empreinte", "ancien_absent", "ancien_deux_fois", "sortie_differente"])
def test_amorce_corrigee_artefacts(cas):
    figee = (RACINE / rv.AMORCE).read_bytes()
    if cas == "autre_empreinte":
        with pytest.raises(GardeArret, match="empreinte"):
            cl3.amorce_corrigee(figee + b"\n")
        with pytest.raises(GardeArret, match="empreinte"):
            cl3.amorce_corrigee(cl3.amorce_corrigee(figee))          # l'amorce déjà corrigée n'est pas une entrée
        return
    ancien, neuf = cl3.PAIRE_AMORCE
    octets = {"ancien_absent": figee.replace(ancien, b""), "ancien_deux_fois": figee + ancien,
              "sortie_differente": figee}[cas]
    sortie = "0" * 64 if cas == "sortie_differente" else hashlib.sha256(octets.replace(ancien, neuf)).hexdigest()
    with pytest.raises(GardeArret, match="une fois et une seule|empreinte"):
        cl3.remplacer_paire(octets, hashlib.sha256(octets).hexdigest(), cl3.PAIRE_AMORCE, sortie)
    # le même appel, sur l'amorce figée et ses empreintes, est sain
    assert cl3.remplacer_paire(figee, FIGEE, cl3.PAIRE_AMORCE, CORRIGEE) == cl3.amorce_corrigee(figee)


# --- vérification (d') : la ligne d'épinglage (§ 4.3 (d), C11) ----------------------------------------------------------

def _reg(*lignes):
    return t2._registre("c" * 40, t2._citation("2" * 40)) + "".join(x + "\n" for x in lignes)


def test_d_prime_cas_sain():
    assert cl3.commit_v3_epingle(_reg(epinglage("3" * 40))) == "3" * 40
    # la ligne est ignorée du lecteur figé du registre (elle ne commence pas par « | »)
    assert en.lignes_du_registre(_reg(epinglage("3" * 40))) == en.lignes_du_registre(_reg())


@pytest.mark.parametrize("cas", ["absente", "deux_lignes", "autre_format", "espace_initiale", "espace_insecable",
                                 "tabulation", "accent_decompose", "autre_erratum", "autre_accord", "autre_branche",
                                 "barre_verticale", "fin_crlf", "commit_court"])
def test_d_prime_artefacts(cas):
    k3 = "3" * 40
    sain = epinglage(k3)
    lignes = {"absente": [], "deux_lignes": [sain, sain],
              "autre_format": [sain.replace(" ; accord", " ; accord donné")],
              "espace_initiale": [" " + sain],
              "espace_insecable": [sain.replace("(barreau 5) :", "(barreau 5) :")],
              "tabulation": [sain.replace(" ; accord ", " ;\taccord ")],
              "accent_decompose": [unicodedata.normalize("NFD", sain)],
              "autre_erratum": [epinglage(k3, erratum=ERRATUM_V1)],
              "autre_accord": [epinglage(k3, accord="GO-2026-11-22-117")],
              "autre_branche": [epinglage(k3, branche=SORTIE + "-r1")],
              "barre_verticale": ["| " + sain],
              "fin_crlf": [sain + "\r"],
              "commit_court": [epinglage("3" * 39)]}[cas]
    if cas == "accent_decompose":
        assert lignes[0] != sain
    with pytest.raises(GardeArret, match="épinglage"):
        cl3.commit_v3_epingle(_reg(*lignes))


# --- le montage complet : cas sain, différence fermée ---------------------------------------------------------------------

def test_montage_complet_cas_sain_et_les_verifications_une_a_une(monde3):
    m = monter3(monde3)
    cmd = corps3(m)
    assert cmd.startswith(f"GO_ID={GO_LECTURE} vastai create instance 654321 --raw --image python:3.11-bookworm --disk 300 ")
    assert hashlib.sha256(base64.b64decode(_segment(cmd))).hexdigest() == CORRIGEE
    texte = _g(m["fige"], "show", f"{m['marche']}:{en.REGISTRE_PROPRE}")
    assert cl3.commit_de_code_verifie(m["commande"], m["code"], texte) == (m["k2"], m["k3"])
    assert cl3.exiger_v3_issu_de_v2(m["commande"], m["k2"], m["k3"]) == sorted(SEPT)
    assert cl2.exiger_commande_issue_du_code_fige(m["commande"], m["code"], m["k2"]) == sorted(cl2.LISTE_FERMEE)


def test_difference_fermee_commande_v3_egale_a_la_v2_hors_du_segment_de_l_amorce(monde3):
    """La commande v3 (arbre v3) égale à l'octet la commande v2 jouée depuis l'arbre v2 du même monde, au même instant,
    hors du segment base64 ; décodés, les deux segments sont l'amorce figée et l'amorce corrigée, qui ne diffèrent que par
    la ligne ajoutée."""
    m = monter3(monde3)
    v2, v3 = corps2(m), corps3(m)
    s2, s3 = _segment(v2), _segment(v3)
    assert v2.replace(s2, "<amorce>").encode("utf-8") == v3.replace(s3, "<amorce>").encode("utf-8")
    a2, a3 = base64.b64decode(s2), base64.b64decode(s3)
    assert hashlib.sha256(a2).hexdigest() == FIGEE and hashlib.sha256(a3).hexdigest() == CORRIGEE
    d = [x for x in difflib.unified_diff(a2.decode().split("\n"), a3.decode().split("\n"), lineterm="", n=0)
         if x[:1] in "+-" and not x.startswith(("+++", "---"))]
    assert d == ["+" + AJOUT]


def test_difference_fermee_entre_le_corps_v2_et_le_corps_v3():
    """Ligne pour ligne, le corps v3 ne diffère du corps v2 que par deux remplacements (§ 4.3 (f))."""
    v2, v3 = t2._lignes_du_corps(cl2.corps_recompose), t2._lignes_du_corps(cl3.corps_recompose)
    blocs = [(o, [x.strip() for x in v2[i1:i2]], [x.strip() for x in v3[j1:j2]]) for o, i1, i2, j1, j2 in
             difflib.SequenceMatcher(None, v2, v3, autojunk=False).get_opcodes() if o != "equal"]
    assert blocs == [
        ("replace", ['commande = commit_de_commande(racine, plan, _montrer(racine, commit, en.REGISTRE_PROPRE).decode("utf-8"))',
                     "exiger_session_au_commit_de_commande(racine, commande)",
                     'exiger_commande_issue_du_code_fige(racine, reg["commit_lecture"], commande)'],
         ['commit_de_code_verifie(racine, reg["commit_lecture"], _montrer(racine, commit, en.REGISTRE_PROPRE).decode("utf-8"))']),
        ("replace", ["amorce = _montrer(racine, commit, AMORCE)"],
         ["amorce = amorce_corrigee(_montrer(racine, commit, AMORCE))"])]
    assert inspect.signature(cl3.corps_recompose) == inspect.signature(cl2.corps_recompose)
    assert inspect.signature(cl3.commande_de_creation_v3) == inspect.signature(rv.commande_de_creation)


def test_les_noms_du_corps_v3_sont_les_objets_des_versions_1_et_2():
    """Importés sans être copiés ; les objets privés employés (`_montrer`, `_RUN_LECTURE`) récrits à l'identique."""
    for nom in ("piece_lecture", "config_lecture", "exiger_registre_de_relecture", "exiger_code_du_commit",
                "exiger_arbre_extrait_propre", "echeance_arret_lecture_s", "hashlib_sha256", "PIECES_LECTURE",
                "AMORCE", "IMAGE", "DEPOT_URL", "BRANCHE_ENTREES", "ENTREES_DE_LA_MARCHE"):
        assert getattr(cl3, nom) is getattr(rv, nom), nom
    assert cl3.exiger_offre_lecture_v2 is cl2.exiger_offre_lecture_v2
    for nom in ("commit_de_commande_cite", "exiger_commande_issue_du_code_fige", "exiger_session_au_commit_de_commande"):
        assert getattr(cl3, nom) is getattr(cl2, nom), nom
    assert cl3.en is en and cl3.lv is lv
    assert t2._lignes_du_corps(cl3._montrer) == t2._lignes_du_corps(rv._montrer)
    assert cl3._RUN_LECTURE.pattern == rv._RUN_LECTURE.pattern and cl3._RUN_LECTURE.flags == rv._RUN_LECTURE.flags
    arbre = ast.parse((RACINE / MODULE_V3).read_text(encoding="utf-8"))
    assert not [a.name for n in ast.walk(arbre) if isinstance(n, (ast.Import, ast.ImportFrom)) for a in n.names
                if a.name.startswith("_")]
    assert not [n.attr for n in ast.walk(arbre) if isinstance(n, ast.Attribute) and n.attr.startswith("_")]


# --- (a) et (d), inchangées : artefacts de la version 2 -------------------------------------------------------------------

def test_a_marche_dont_l_arbre_gele_differe(monde3):
    m = monter3(monde3, dans_marche=lambda r: (r / "scripts" / "autre.sh").write_text("echo x\n"))
    with pytest.raises(GardeArret, match="code différent de CODE-LECTURE-B5F"):
        corps3(m)


def test_d_accord_de_lecture_sans_la_citation_de_la_v2(monde3):
    m = monter3(monde3)
    texte = t2._registre(m["code"], "session de lecture session_essai") + epinglage(m["k3"]) + "\n"
    with pytest.raises(GardeArret, match="ne cite pas, une fois et à la lettre"):
        cl3.commit_de_code_verifie(m["commande"], m["code"], texte)
    texte = t2._registre(m["code"], t2._citation(m["k2"], additif="b" * 64)) + epinglage(m["k3"]) + "\n"
    with pytest.raises(GardeArret, match="autre empreinte"):
        cl3.commit_de_code_verifie(m["commande"], m["code"], texte)


def test_d_prime_par_le_corps_ligne_absente_ou_autre_accord(monde3):
    m = monter3(monde3, lignes=lambda k3: [])
    with pytest.raises(GardeArret, match="épinglage"):
        corps3(m)


def test_d_prime_par_le_corps_epinglage_d_un_autre_commit(monde3):
    """La ligne épingle un jumeau du commit v3 (même arbre, autre message) : la session est au vrai commit v3 : refus."""
    def lignes(k3):
        return [epinglage(_g(monde3["commande"], "commit-tree", f"{k3}^{{tree}}", "-p", f"{k3}^", "-m", "jumeau"))]
    m = monter3(monde3, lignes=lignes)
    with pytest.raises(GardeArret, match="tête de la session"):
        corps3(m)


# --- (c'1) et (c'2) (C1) ---------------------------------------------------------------------------------------------------

def _symlien(c):
    p = c / SEPT[6]
    p.unlink()
    os.symlink("test_commande_lecture_v3.py", p)
    _g(c, "add", "-A")


def _sous_module(c):
    _g(c, "rm", "-q", "--cached", SEPT[6])
    (c / SEPT[6]).unlink()
    _g(c, "update-index", "--add", "--cacheinfo", f"160000,{'1' * 40},{SEPT[6]}")


@pytest.mark.parametrize("cas, motif", [
    ("v2_modifie_module", "modifié ou supprimé"), ("v2_modifie_lanceur", "modifié ou supprimé"),
    ("v2_modifie_essais", "modifié ou supprimé"), ("fige_modifie", "modifié ou supprimé"),
    ("hors_liste", "hors de la liste fermée"), ("supprime", "modifié ou supprimé"),
    ("lien", "mode"), ("sous_module", "mode"), ("sans_module_ouverture", "absent"), ("sans_lanceur_v3", "absent")])
def test_c_prime_2_le_commit_v3_n_ajoute_que_des_fichiers_de_la_liste(monde3, cas, motif):
    def retouche(c):
        if cas.startswith("v2_modifie_"):
            f = {"module": cl2.MODULE, "lanceur": cl2.LANCEUR, "essais": cl2.ESSAIS}[cas.rsplit("_", 1)[1]]
            (c / f).write_text((c / f).read_text() + "\n# retouche\n")
        elif cas == "fige_modifie":
            (c / rv.AMORCE).write_text((c / rv.AMORCE).read_text() + "\n# retouche\n")
        elif cas == "hors_liste":
            (c / "scripts" / "autre.sh").write_text("echo x\n")
        elif cas == "supprime":
            (c / t2.LANCEUR_V1).unlink()
        elif cas == "lien":
            _symlien(c)
            return
        elif cas == "sous_module":
            _sous_module(c)
            return
        elif cas == "sans_module_ouverture":
            (c / MODULE_OUV).unlink()
        elif cas == "sans_lanceur_v3":
            (c / LANCEUR_V3).unlink()
        _g(c, "add", "-A")
    m = monter3(monde3, dans_v3=retouche)
    with pytest.raises(GardeArret, match=motif):
        corps3(m)
    with pytest.raises(GardeArret, match=motif):
        cl3.exiger_v3_issu_de_v2(m["commande"], m["k2"], m["k3"])


def test_c_prime_2_commit_v3_qui_ne_descend_pas_du_commit_v2(monde3):
    """Même arbre que le commit v3, parent : le code (et non le commit v2) : refus par l'ascendance."""
    m = monter3(monde3, v3_parent=lambda m, k2: m["code"])
    with pytest.raises(GardeArret, match="ne descend pas"):
        corps3(m)


def test_c_prime_1_commit_v2_qui_modifie_le_code_fige(monde3):
    """(c'1) : la vérification (c) de la version 2, rejouée sur le commit v2 cité : un commit v2 qui modifie l'amorce est
    refusé, même si le commit v3 n'ajoute que les sept fichiers."""
    m = monter3(monde3, dans_v2=lambda c: (c / rv.AMORCE).write_text((c / rv.AMORCE).read_text() + "\n# v2 retouché\n"))
    with pytest.raises(GardeArret, match="modifié ou supprimé"):
        corps3(m)


# --- (b') -------------------------------------------------------------------------------------------------------------------

def test_b_prime_autre_tete_arbre_change_non_suivi(monde3):
    m = monter3(monde3)
    (m["commande"] / "src" / "controle_ia" / "intrus.py").write_text("x = 1\n")
    with pytest.raises(GardeArret, match="non suivi sous src"):
        corps3(m)
    (m["commande"] / "src" / "controle_ia" / "intrus.py").unlink()
    (m["commande"] / MODULE_V3).write_text((m["commande"] / MODULE_V3).read_text() + "\n# retouche\n")
    with pytest.raises(GardeArret, match="arbre de travail"):
        corps3(m)
    _g(m["commande"], "checkout", "-q", "--", MODULE_V3)
    assert corps3(m)
    with pytest.raises(GardeArret, match="tête de la session"):          # la session à l'arbre v2
        cl3.corps_recompose(m["v2"], *_args(m))


def test_b_prime_module_joue_depuis_un_autre_arbre(monde3):
    m = monter3(monde3)
    with pytest.raises(GardeArret, match="joué depuis un autre arbre"):
        cl3.commande_de_creation_v3(m["commande"], *_args(m))


# --- les autres gardes, rejouées telles quelles ----------------------------------------------------------------------------

@pytest.mark.parametrize("cas", ["disque", "prix", "carte", "stockage", "marche_autre_plan", "sans_entrees",
                                 "entrees_hors_branche", "go_autre", "commit_illisible", "branche_illisible",
                                 "existant_sans_empreinte"])
def test_les_autres_gardes_refusent_par_la_v3_comme_par_la_v2(monde3, cas):
    m = monter3(monde3)
    k = {}
    if cas in ("disque", "prix", "carte", "stockage"):
        p = m["t"] / "offre-retouchee.json"
        p.write_text(json.dumps(dict(t2.OFFRE, **{"disque": {"disk_space": 200}, "prix": {"dph_total": 1.35},
                                                  "carte": {"gpu_name": "H100 SXM"},
                                                  "stockage": {"storage_cost": 0.2921}}[cas])))
        k["offre_json"] = p
    elif cas == "marche_autre_plan":
        k["run_id"] = t2.RUN_R
    elif cas == "sans_entrees":
        k["entrees_commit"] = ""
    elif cas == "entrees_hors_branche":
        k["entrees_commit"] = m["code"]
    elif cas == "go_autre":
        k["go_id"] = GO_FORMATION
    elif cas == "commit_illisible":
        k["commit"] = "pas-un-commit"
    elif cas == "branche_illisible":
        k["branche"] = "main; echo x"
    elif cas == "existant_sans_empreinte":
        (m["t"] / "x.json").write_text(json.dumps([{**t2.EXISTANTS[0], "nom": "ancre-R1", "sha256": ""}]))
        k["existants_json"] = m["t"] / "x.json"

    def jouer(f):
        try:
            return ("rendu", f(m, **k))
        except GardeArret as e:
            return ("refus", re.sub(r"[0-9a-f]{12}", "<commit>", str(e)))
    v2, v3 = jouer(corps2), jouer(corps3)
    assert v2 == v3 and v3[0] == "refus", (v2, v3)


def test_portee_la_repetition_est_refusee(monde3):
    m = monter3(monde3)
    a = list(_args(m))
    a[0] = "repetition"
    with pytest.raises(GardeArret, match="répétition générale"):
        cl3.commande_de_creation_v3(m["commande"], *a)


# --- intégrité ---------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("module", [MODULE_V3, MODULE_OUV])
def test_aucune_substitution_dans_les_modules_neufs(module):
    source = (RACINE / module).read_text(encoding="utf-8")
    assert t2.substitutions(source) == []
    assert t2.substitutions(source + "\n\nfrom . import lecture_v1 as figee\nfigee.ouvrir = None\n") != []


def test_les_modules_figes_ne_sont_pas_alteres_par_l_import_ni_par_l_appel(monde3):
    from controle_ia.barreau5_familles import ouverture_suffixes_v1 as ov  # noqa: F401  (import des deux modules neufs)
    avant = (rv.commande_de_creation, cl2.corps_recompose, cl2.commit_de_commande_cite, lv.ouvrir, lv.preparer,
             lv.garde_d_ouverture, lv._familles_formees, en.exiger_table_coherente, dict(rv.OFFRE_LECTURE),
             cl2.LISTE_FERMEE, rv.AMORCE, dict(fv.OFFRE))
    m = monter3(monde3)
    corps3(m)
    apres = (rv.commande_de_creation, cl2.corps_recompose, cl2.commit_de_commande_cite, lv.ouvrir, lv.preparer,
             lv.garde_d_ouverture, lv._familles_formees, en.exiger_table_coherente, dict(rv.OFFRE_LECTURE),
             cl2.LISTE_FERMEE, rv.AMORCE, dict(fv.OFFRE))
    assert all(a is b or a == b for a, b in zip(avant, apres))


# --- l'amorce embarquée (C10) ---------------------------------------------------------------------------------------------

def test_amorce_embarquee_bloc_branche_rend_la_branche_de_sortie():
    texte = cl3.amorce_corrigee((RACINE / rv.AMORCE).read_bytes()).decode("utf-8")
    bloc = re.search(r"^# >>> branche\b.*?$(.*?)^# <<< branche$", texte, re.S | re.M).group(1)
    p = subprocess.run(["bash", "-c", bloc + "branche_sortie decisif"], capture_output=True, text=True, timeout=30)
    assert p.stdout.strip() == cl3.BRANCHE_SORTIE


def test_amorce_embarquee_les_51_essais_figes_de_l_amorce_sur_une_copie_jetable(tmp_path):
    """Le fichier d'essais figé de l'amorce, joué sur une copie jetable de l'arbre où l'amorce est remplacée par
    `amorce_corrigee(...)` : 51 passés exigés."""
    c = tmp_path / "copie"
    shutil.copytree(RACINE / "src", c / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.egg-info"))
    (c / "tests").mkdir()
    for f in ("conftest.py", "test_amorce_b5f_lecture_v1.py", "test_barreau5_familles_lecture_v1.py",
              "test_barreau5_familles_sondes_v1.py", "test_barreau5_familles_relecture_v1.py"):
        shutil.copy(RACINE / "tests" / f, c / "tests" / f)
    for f in ("pyproject.toml", "requirements-gpu.txt", "requirements-cpu.txt", "requirements-donnees.txt"):
        shutil.copy(RACINE / f, c / f)
    (c / "scripts").mkdir()
    (c / rv.AMORCE).write_bytes(cl3.amorce_corrigee((RACINE / rv.AMORCE).read_bytes()))
    assert hashlib.sha256((c / rv.AMORCE).read_bytes()).hexdigest() == CORRIGEE
    env = {k: v for k, v in os.environ.items() if not k.startswith("PYTEST_")}
    env.update({"PYTHONPATH": str(c / "src"), "PYTHONDONTWRITEBYTECODE": "1"})
    p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--tb=short",
                        f"--basetemp={tmp_path / 'bt'}", "tests/test_amorce_b5f_lecture_v1.py"],
                       cwd=c, env=env, capture_output=True, text=True, timeout=900)
    assert re.search(r"^51 passed", p.stdout.strip().splitlines()[-1]), p.stdout[-3000:] + p.stderr[-2000:]


# --- le lanceur v3 (§ 4.3 (g) ; C12) ----------------------------------------------------------------------------------------

def _jouer(racine, *args, env=None):
    e = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHON_B5F": sys.executable, "PYTHONDONTWRITEBYTECODE": "1"}
    e.update(env or {})
    return subprocess.run(["bash", str(Path(racine) / LANCEUR_V3), *args], capture_output=True, text=True, env=e,
                          cwd=str(racine))


def _arguments_du_lanceur(m, racine=None, plan="decisif"):
    return ["commande", plan, str(racine or m["commande"]), str(m["t"] / "offre.json"), m["marche"], "main", RUN_L,
            m["entrees"], "1", "une_sur_dix", str(m["t"] / "aucun.json")]


def test_lanceur_v3_cas_sain_imprime_l_empreinte_puis_la_commande(monde3):
    m = monter3(monde3)
    r = _jouer(m["commande"], *_arguments_du_lanceur(m), env={"GO_ID": GO_LECTURE})
    assert r.returncode == 0, r.stderr
    lignes = r.stdout.splitlines()
    assert lignes[0] == f"B5F AMORCE EMBARQUÉE : sha256 {CORRIGEE}"
    assert lignes[1].startswith("B5F COMMANDE") and lignes[2].startswith(f"GO_ID={GO_LECTURE} vastai create instance ")
    assert hashlib.sha256(base64.b64decode(_segment(lignes[2]))).hexdigest() == CORRIGEE
    assert _g(m["commande"], "status", "--porcelain") == ""


def test_lanceur_v3_refus(monde3):
    m = monter3(monde3)
    r = _jouer(m["commande"], *_arguments_du_lanceur(m))
    assert r.returncode == 2 and "GO_ID absent" in r.stderr and r.stdout == ""
    r = _jouer(m["commande"], *_arguments_du_lanceur(m, plan="repetition"), env={"GO_ID": GO_FORMATION})
    assert r.returncode == 2 and "répétition" in r.stderr and r.stdout == ""
    r = _jouer(m["commande"], *_arguments_du_lanceur(m, racine=m["fige"]), env={"GO_ID": GO_LECTURE})
    assert r.returncode == 2 and r.stdout == ""
    r = _jouer(RACINE, *_arguments_du_lanceur(m), env={"GO_ID": GO_LECTURE})
    assert r.returncode == 2 and "joué depuis un autre arbre" in r.stderr and r.stdout == ""


@pytest.mark.parametrize("segment", ["figee", "illisible", "deux"])
def test_lanceur_v3_condition_d_arret_c12_segment_qui_n_est_pas_l_amorce_corrigee(tmp_path, segment):
    """C12 : quel que soit ce que rend le module, le lanceur ne laisse sortir aucune commande dont le segment base64 décodé
    n'a pas l'empreinte `0adb6efb…` (faux interpréteur qui rend une commande de la version 2, l'amorce figée)."""
    figee = base64.b64encode((RACINE / rv.AMORCE).read_bytes()).decode()
    corrigee = base64.b64encode(cl3.amorce_corrigee((RACINE / rv.AMORCE).read_bytes())).decode()
    s = {"figee": f"echo {figee} | base64 -d > /root/amorce_b5f_lecture_v1.sh",
         "illisible": "echo !!! | base64 -d > /root/amorce_b5f_lecture_v1.sh",
         "deux": f"echo {corrigee} | base64 -d > /root/a.sh && echo {figee} | base64 -d > /root/amorce_b5f_lecture_v1.sh"}[segment]
    faux = tmp_path / "faux-python"
    faux.write_text(f"#!/usr/bin/env bash\necho 'GO_ID=GO-2026-11-24-01 vastai create instance 1 --args -c \"{s}\"'\n")
    faux.chmod(0o755)
    r = _jouer(RACINE, "commande", "decisif", *["a"] * 9, env={"GO_ID": GO_LECTURE, "PYTHON_B5F": str(faux)})
    assert r.returncode == 2 and "amorce embarquée" in r.stderr and "vastai" not in r.stdout, (r.stdout, r.stderr)
    # témoin : le même faux interpréteur, avec le segment de l'amorce corrigée, passe
    faux.write_text("#!/usr/bin/env bash\necho 'GO_ID=GO-2026-11-24-01 vastai create instance 1 --args -c \"echo "
                    f"{corrigee} | base64 -d > /root/amorce_b5f_lecture_v1.sh && bash /root/amorce_b5f_lecture_v1.sh\"'\n")
    r = _jouer(RACINE, "commande", "decisif", *["a"] * 9, env={"GO_ID": GO_LECTURE, "PYTHON_B5F": str(faux)})
    assert r.returncode == 0 and f"sha256 {CORRIGEE}" in r.stdout, r.stderr


@pytest.mark.parametrize("args", [[], ["inconnue"], ["commande"], ["config", "a", "b", "c", "d", "e"],
                                  ["verifier", "a", "b", "c"], ["marche", "a", "b", "c"], ["ouvrir"] + ["a"] * 7,
                                  ["preparer"] + ["a"] * 5, ["variante"] + ["a"] * 4, ["scores", "a", "b", "c"],
                                  ["detruire"] + ["a"] * 6, ["commande"] + ["a"] * 11])
def test_lanceur_v3_refuse_toute_autre_sous_commande(args):
    r = _jouer(RACINE, *args, env={"GO_ID": GO_LECTURE})
    assert r.returncode == 2 and "B5F REFUS" in r.stderr and r.stdout == ""


def test_texte_du_lanceur_v3_sans_commande_d_arret_de_creation_ni_de_reseau():
    texte = (RACINE / LANCEUR_V3).read_text(encoding="utf-8")
    code = "\n".join(x for x in texte.splitlines() if not x.lstrip().startswith("#"))
    arret = "k" + "ill"
    for interdit in (rf"\b{arret}\b", rf"\bp{arret}\b", r"\bp" + "grep\\b", r"vastai", r"\bcurl\b", r"\bwget\b",
                     r"\bgit\b", r"\brm\s", r"huggingface", r"barreau5_familles\.(?:re)?lecture_v1"):
        assert re.search(interdit, code) is None, interdit
    assert "set -uo pipefail" in texte and "commande_lecture_v3" in code and CORRIGEE in code
