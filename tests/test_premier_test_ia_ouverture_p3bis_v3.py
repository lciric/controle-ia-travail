"""Ouverture v3 de P3-bis (`premier_test_ia.ouverture_p3bis_v3`) : copie exacte de la v2 hors de l'en-tête, de la commande de
la lecture complémentaire (`lecture_p3bis_v2`, règle (a') décisive, R-2296, R-2320) et du nom du programme. Essais :
comparaison ligne à ligne des deux fichiers ; chaque fonction et classe de même source dans les deux modules, hors des deux
changées ; commandes des lectures ; chaîne fermée de bout en bout en mode décisif (runs à 800 directions, vraie garde
d'import), cas sain et artefact (run à 200 directions : la lecture complémentaire s'arrête sur sa garde, code 1).

Les fabriques du texte scellé factice et du run décisif sont recopiées de
`tests/test_premier_test_ia_lecture_p3bis_gardes_v1.py` (`_prereg`, `_monter_decisif`), sur l'essai de fermeture v3."""
import difflib
import hashlib
import importlib.util
import inspect
import json
import shutil
import subprocess
from pathlib import Path

from conftest import committer
from controle_ia.manifeste import config_canonique
from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob2
from controle_ia.premier_test_ia import ouverture_p3bis_v3 as ob3
from controle_ia.prereg import SECTIONS
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("essai_fermeture_p3bis_v3", RACINE / "scripts" / "essai_fermeture_p3bis_v3.py")
ev3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev3)

RUN = "20261120-120000-p3bis-reel"
LECTURE, LC = "20261120-130000-p3bis-lecture", "20261120-130100-p3bis-lecture-complementaire"
ENTROPIE = 4242
PREREG = "prereg/P3-bis-temoin-positif-v1.md"
CONFIG = {"mode": "reel", "max_nouveaux": 64}
MODULE = RACINE / "src" / "controle_ia" / "premier_test_ia"
RETIREES = ['"""Fermeture et ouverture des sorties de P3-bis (témoin positif planté), v2.',
            '             [sys.executable, "-m", "controle_ia.premier_test_ia.lecture_p3bis_v1", "--run-source", run, "--lecture",',
            '    ap = argparse.ArgumentParser(prog="python -m controle_ia.premier_test_ia.ouverture_p3bis_v2")']
AJOUTEES_HORS_EN_TETE = [
    '             [sys.executable, "-m", "controle_ia.premier_test_ia.lecture_p3bis_v2", "--run-source", run, "--lecture",',
    '    ap = argparse.ArgumentParser(prog="python -m controle_ia.premier_test_ia.ouverture_p3bis_v3")']


def _git(d, *args):
    return subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, text=True).stdout.strip()


def test_v3_egale_a_v2_hors_des_lignes_declarees():
    a = (MODULE / "ouverture_p3bis_v2.py").read_text(encoding="utf-8").splitlines()
    b = (MODULE / "ouverture_p3bis_v3.py").read_text(encoding="utf-8").splitlines()
    retirees = [x[2:] for x in difflib.ndiff(a, b) if x.startswith("- ")]
    ajoutees = [x[2:] for x in difflib.ndiff(a, b) if x.startswith("+ ")]
    assert retirees == RETIREES
    en_tete = ajoutees[:8]
    assert en_tete[0].startswith('"""Fermeture et ouverture des sorties de P3-bis (témoin positif planté), v3 :')
    assert en_tete[-1] == "Fermeture et ouverture des sorties de P3-bis (témoin positif planté), v2."
    assert ajoutees[8:] == AJOUTEES_HORS_EN_TETE
    assert len(b) == len(a) + 7
    # artefact : une ligne de plus ailleurs serait vue
    c = list(b)
    c.insert(500, "    pass")
    assert [x[2:] for x in difflib.ndiff(a, c) if x.startswith("+ ")][8:] != AJOUTEES_HORS_EN_TETE


def test_fonctions_et_classes_de_meme_source_hors_des_deux_changees():
    changees = {"commandes_des_lectures", "_main"}
    noms = [n for n, o in vars(ob2).items() if (inspect.isfunction(o) or inspect.isclass(o)) and o.__module__ == ob2.__name__]
    assert len(noms) > 60 and changees <= set(noms)
    for n in noms:
        x, y = inspect.getsource(getattr(ob2, n)), inspect.getsource(getattr(ob3, n))
        if n in changees:
            assert x != y
        else:
            assert x == y, n
            assert getattr(ob3, n).__module__ == ob3.__name__                       # défini dans v3 : rien n'est importé de v2
    for k, v in vars(ob2).items():                                                  # constantes égales
        if k.isupper():
            assert getattr(ob3, k) == v, k


def test_commandes_des_lectures():
    c2 = ob2.commandes_des_lectures("R", "RL", "RLC", "p.md", 7)
    c3 = ob3.commandes_des_lectures("R", "RL", "RLC", "p.md", 7)
    assert c3[0] == c2[0] and c3[1][:2] == c2[1][:2]
    assert c3[1][2][2] == "controle_ia.premier_test_ia.lecture_p3bis_v2" and c2[1][2][2] == "controle_ia.premier_test_ia.lecture_p3bis_v1"
    assert c3[1][2][:2] + c3[1][2][3:] == c2[1][2][:2] + c2[1][2][3:]


# ------------------------------------------------------------------------------------------------- chaîne fermée décisive
def _prereg(depot: Path, commit: str, config: dict) -> Path:
    p = depot / PREREG
    p.parent.mkdir(parents=True, exist_ok=True)
    corps = ["# P3-bis factice (essai de bout en bout décisif)", "", f"- Commit du code d'analyse : `{commit}`",
             f"- Configuration de P3 (empreinte canonique) : `{hashlib.sha256(config_canonique(config)).hexdigest()}`",
             f"- Entropie : `{ENTROPIE}`", ""]
    for s in SECTIONS[:-1]:
        corps += [f"## {s}", "", f"contenu {s}", ""]
    corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
    p.write_text("\n".join(corps), encoding="utf-8")
    sceller(p)
    return p


def _clone_ferme(tmp_path, monkeypatch, n_plancher: int = 800) -> tuple[Path, str]:
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))
    depot = ev3.depot_vide(tmp_path / "instance")
    shutil.copytree(RACINE / "src" / "controle_ia", depot / "src" / "controle_ia",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    gi = depot / ".gitignore"
    gi.write_text(gi.read_text(encoding="utf-8") + "donnees/\n__pycache__/\n", encoding="utf-8")
    committer(depot)
    commit = _git(depot, "rev-parse", "HEAD")
    p = _prereg(depot, commit, CONFIG)
    committer(depot)
    monkeypatch.setattr(ev3, "N_PLANCHER", n_plancher)
    ev3.fabriquer_run(depot, RUN, "vu", ev3.graine("vu"), config=CONFIG, decisif=True, prereg=str(p), entropie=ENTROPIE)
    ob3.fermer_run(depot, RUN)
    _git(depot, "add", "-A")
    _git(depot, "commit", "-qm", "run et second paquet")
    ob3.exiger_aucun_clair(depot, RUN)
    clone = tmp_path / "clone-ferme"
    subprocess.run(["git", "clone", "-q", str(depot), str(clone)], check=True, capture_output=True)
    monkeypatch.setenv("PYTHONPATH", str(clone / "src"))                                         # code importé du clone
    monkeypatch.setenv("PYTHONDONTWRITEBYTECODE", "1")
    return clone, commit


def test_chaine_fermee_de_bout_en_bout_en_mode_decisif_v3(tmp_path, monkeypatch):
    clone, commit = _clone_ferme(tmp_path, monkeypatch)
    sortie = []
    code = ob3.lectures_fermees(clone, RUN, LECTURE, LC, prereg=PREREG, entropie=ENTROPIE, imprimer=sortie.append)
    assert code == 0, sortie
    assert sortie[:4] == ["code dépliage du second paquet : 0", "code lecture de P3 : 0", "code lecture complémentaire : 0",
                          "code mise en paquet : 0"] and len(sortie) == 5
    _, archive = ob3.relire_paquet_lectures((clone / ob3.dossier_ferme(RUN) / ob3.PAQUET_LECTURES).read_bytes(), ENTROPIE)
    f = dict(ob3.membres_de(archive))
    for lecture, commande in ((LECTURE, "python -m controle_ia.premier_test_ia.lecture"),
                              (LC, "python -m controle_ia.premier_test_ia.lecture_p3bis_v2")):
        m = json.loads(f[f"runs/{lecture}/manifeste.json"])
        assert m["decisif"] is True and m["preenregistrement"]["chemin"] == PREREG and m["depot_propre"] is True
        assert m["commande"] == commande
    l3bis = json.loads(f[f"diag/{LC}/lecture-p3bis.json"])["resultat"]
    assert l3bis["lien_au_preenregistrement"] == {"commit_cite": commit, "entropie": ENTROPIE}
    assert l3bis["issue_mecanique"] == {"issue": "vu", "ligne": 4}
    assert l3bis["etat_decisif"]["lecture"]["n_plancher"] == 800 and l3bis["regle_ancienne_200"]["lecture"]["n_plancher"] == 200
    assert json.loads(f[f"diag/{LECTURE}/lecture-p3.json"])["resultat"]["n_plancher"][ev3.P_T] == 800
    assert f[f"{ob3.ESPACE_DEFAUT}/lecture-p3bis.sortie"] == b"" and f[f"{ob3.ESPACE_DEFAUT}/lecture-p3bis.erreurs"] == b""
    statut = _git(clone, "status", "--porcelain", "--untracked-files=all", "--ignored")
    assert sorted(x[3:] for x in statut.splitlines()) == sorted([f"{ob3.dossier_ferme(RUN)}/{ob3.PAQUET_LECTURES}",
                                                                 f"{ob3.dossier_ferme(RUN)}/{ob3.PAQUET_LECTURES}.sha256"])


def test_chaine_fermee_artefact_run_a_200_directions(tmp_path, monkeypatch):
    clone, _ = _clone_ferme(tmp_path, monkeypatch, n_plancher=200)
    sortie = []
    code = ob3.lectures_fermees(clone, RUN, LECTURE, LC, prereg=PREREG, entropie=ENTROPIE, imprimer=sortie.append)
    assert code == 1
    assert sortie[:3] == ["code dépliage du second paquet : 0", "code lecture de P3 : 0", "code lecture complémentaire : 1"]
    _, archive = ob3.relire_paquet_lectures((clone / ob3.dossier_ferme(RUN) / ob3.PAQUET_LECTURES).read_bytes(), ENTROPIE)
    f = dict(ob3.membres_de(archive))
    assert f[f"{ob3.ESPACE_DEFAUT}/lecture-p3bis.sortie"] == b""
    assert f[f"{ob3.ESPACE_DEFAUT}/lecture-p3bis.erreurs"].decode("utf-8").startswith("ARRÊT : plancher de")
    assert not any(x.startswith(f"runs/{LC}/") for x in f)                                       # aucun run laissé par la garde
