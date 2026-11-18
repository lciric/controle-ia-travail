"""Essais R5 du contrôle du code contre la ligne `CODE-ACCB6` (`src/controle_ia/accumulation_b6/code_accb6_v1.py`, R-2272) : cas sain
et artefacts, `ecrire`, appel par `lecture_v1.lire` avant tout calcul et avant le manifeste (refus, code 2). Dépôts git jetables
seulement : le paquet importé y est recopié et committé ; aucune donnée réelle, aucun appel de modèle."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from controle_ia.scellement import sceller
from controle_ia.t07 import registre_v1 as rg
from controle_ia.accumulation_b6 import code_accb6_v1 as ca
from controle_ia.accumulation_b6 import garde_v1 as gv
from controle_ia.accumulation_b6 import lecture_v1 as lv
from test_accb6_lecture_v1 import DOSSIER_PAQUET_JOUET, ENTROPIE_JOUET, T0, construire, tirages  # noqa: F401

PAQUET = Path(ca.__file__).resolve().parent


def git(depot: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(depot), *args], check=True, capture_output=True, text=True).stdout.strip()


def paquet_committe(depot: Path, sous: str = DOSSIER_PAQUET_JOUET) -> tuple[Path, str]:
    cible = depot / sous
    cible.mkdir(parents=True, exist_ok=True)
    for f in PAQUET.glob("*.py"):
        shutil.copy(f, cible / f.name)
    git(depot, "add", sous)
    git(depot, "commit", "-q", "-m", "paquet")
    return cible, git(depot, "rev-parse", "HEAD")


def fichier_code(depot: Path, contenu: dict, nom: str = "code.json") -> dict:
    p = depot / "registres" / "code-accb6" / nom
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(contenu) + "\n", encoding="utf-8")
    sceller(p)
    return {"chemin": str(p.relative_to(depot)), "date": rg.date_utc(T0)}


def ecrit(depot: Path, commit: str = "HEAD", nom: str = "code-ecrit.json") -> tuple[dict, dict]:
    p = depot / "registres" / "code-accb6" / nom
    ca.ecrire_fichier_code(depot, commit, p, entropie=ENTROPIE_JOUET)
    sceller(p)
    return {"chemin": str(p.relative_to(depot)), "date": rg.date_utc(T0)}, json.loads(p.read_text(encoding="utf-8"))


# ------------------------------------------------------------------------------------------------------------- cas sain
def test_cas_sain_et_ecrire(depot):
    """Paquet committé, fichier écrit par `ecrire` pour la tête : contrôle passé ; la liste est exactement les fichiers `*.py` du
    paquet, aux empreintes du contenu ; l'entropie donnée est écrite."""
    dossier, commit = paquet_committe(depot)
    entree, d = ecrit(depot)
    assert d["commit"] == commit and d["entropie"] == ENTROPIE_JOUET
    assert set(d["fichiers"]) == {f"{ca.PREFIXE}{f.name}" for f in PAQUET.glob("*.py")}
    assert f"{ca.PREFIXE}code_accb6_v1.py" in d["fichiers"] and f"{ca.PREFIXE}lecture_v1.py" in d["fichiers"]
    r = ca.controler_code(depot, entree, dossier)
    assert r["commit"] == commit and r["fichiers"] == len(d["fichiers"])


def test_commit_ancetre_de_la_tete_accepte(depot):
    """Commit cité ancêtre de la tête (un commit sans changement du paquet après lui) : accepté."""
    dossier, _ = paquet_committe(depot)
    entree, _ = ecrit(depot)
    (depot / "autre.txt").write_text("x\n")
    git(depot, "add", "autre.txt")
    git(depot, "commit", "-q", "-m", "autre")
    assert ca.controler_code(depot, entree, dossier)["fichiers"] > 0


def test_ecrire_gardes(depot):
    """`ecrire` : entropie tirée (128 bits) quand elle n'est pas donnée ; refuse d'écraser ; commit introuvable ; commit sans
    paquet."""
    paquet_committe(depot)
    p = depot / "c1.json"
    ca.ecrire_fichier_code(depot, "HEAD", p)
    assert 0 < json.loads(p.read_text())["entropie"] < 2 ** 128
    with pytest.raises(rg.RefusRegistre, match="R12"):
        ca.ecrire_fichier_code(depot, "HEAD", p)
    with pytest.raises(rg.RefusRegistre, match="introuvable"):
        ca.ecrire_fichier_code(depot, "0" * 40, depot / "c2.json")
    racine_commit = git(depot, "rev-list", "--max-parents=0", "HEAD")
    with pytest.raises(rg.RefusRegistre, match="aucun fichier"):
        ca.ecrire_fichier_code(depot, racine_commit, depot / "c3.json")


# ------------------------------------------------------------------------------------------------------------- artefacts
def test_fichier_du_paquet_importe_modifie(depot):
    dossier, _ = paquet_committe(depot)
    entree, _ = ecrit(depot)
    with open(dossier / "etats_v1.py", "a", encoding="utf-8") as f:
        f.write("# changé après le commit\n")
    with pytest.raises(rg.RefusRegistre, match="etats_v1.py dans le paquet importé"):
        ca.controler_code(depot, entree, dossier)


@pytest.mark.parametrize("geste", ["ajout", "retrait"])
def test_fichier_en_plus_ou_en_moins_dans_le_paquet_importe(depot, geste):
    dossier, _ = paquet_committe(depot)
    entree, _ = ecrit(depot)
    if geste == "ajout":
        (dossier / "intrus_v1.py").write_text("x = 1\n")
    else:
        (dossier / "phrases_v1.py").unlink()
    with pytest.raises(rg.RefusRegistre, match="fichiers du paquet importé ≠ liste écrite"):
        ca.controler_code(depot, entree, dossier)


def test_empreinte_ecrite_fausse(depot):
    dossier, _ = paquet_committe(depot)
    _, d = ecrit(depot)
    d["fichiers"][f"{ca.PREFIXE}garde_v1.py"] = "0" * 64
    entree = fichier_code(depot, d)
    with pytest.raises(rg.RefusRegistre, match="garde_v1.py au commit cité.*garde_v1.py dans le paquet importé"):
        ca.controler_code(depot, entree, dossier)


def test_commit_absent(depot):
    dossier, _ = paquet_committe(depot)
    _, d = ecrit(depot)
    d["commit"] = "1" * 40
    with pytest.raises(rg.RefusRegistre, match="absent du dépôt"):
        ca.controler_code(depot, fichier_code(depot, d), dossier)


def test_commit_non_ancetre_de_la_tete(depot):
    """Commit hors de l'histoire de la tête (commit orphelin du même arbre, fait par `git commit-tree`, la tête ne bouge pas) :
    refus."""
    dossier, _ = paquet_committe(depot)
    _, d = ecrit(depot)
    arbre = git(depot, "rev-parse", "HEAD^{tree}")
    orphelin = git(depot, "commit-tree", arbre, "-m", "orphelin")
    d["commit"] = orphelin
    with pytest.raises(rg.RefusRegistre, match="ni la tête"):
        ca.controler_code(depot, fichier_code(depot, d), dossier)


def test_commit_cite_d_un_autre_contenu(depot):
    """Le paquet change dans un commit postérieur : le fichier écrit pour l'ancien commit refuse le paquet importé (nouveau) ; une
    liste aux empreintes nouvelles mais citant l'ancien commit refuse le commit."""
    dossier, ancien = paquet_committe(depot)
    entree_ancien, d_ancien = ecrit(depot, nom="ancien.json")
    with open(dossier / "lecture_v1.py", "a", encoding="utf-8") as f:
        f.write("# version suivante\n")
    git(depot, "add", DOSSIER_PAQUET_JOUET)
    git(depot, "commit", "-q", "-m", "suivant")
    with pytest.raises(rg.RefusRegistre, match="lecture_v1.py dans le paquet importé"):
        ca.controler_code(depot, entree_ancien, dossier)
    _, d_neuf = ecrit(depot, nom="neuf.json")
    d_neuf["commit"] = ancien
    with pytest.raises(rg.RefusRegistre, match="lecture_v1.py au commit cité"):
        ca.controler_code(depot, fichier_code(depot, d_neuf, "melange.json"), dossier)
    assert ca.controler_code(depot, ecrit(depot, nom="neuf2.json")[0], dossier)["fichiers"] == len(d_ancien["fichiers"])


def test_chemin_liste_hors_du_paquet(depot):
    dossier, _ = paquet_committe(depot)
    _, d = ecrit(depot)
    d["fichiers"]["scripts/enumeration_etats_accb6_v1.py"] = "a" * 64
    with pytest.raises(rg.RefusRegistre, match="chemin src/controle_ia/accumulation_b6/<nom>.py"):
        ca.controler_code(depot, fichier_code(depot, d), dossier)


def test_forme_du_fichier(depot):
    dossier, _ = paquet_committe(depot)
    _, d = ecrit(depot)
    del d["entropie"]
    with pytest.raises(rg.RefusRegistre, match="forme"):
        ca.controler_code(depot, fichier_code(depot, d), dossier)


def test_paquet_hors_d_un_depot_git(depot, tmp_path_factory):
    dossier, _ = paquet_committe(depot)
    entree, _ = ecrit(depot)
    hors = tmp_path_factory.mktemp("hors") / "accumulation_b6"
    shutil.copytree(dossier, hors)
    with pytest.raises(rg.RefusRegistre, match="pas dans un dépôt git"):
        ca.controler_code(depot, entree, hors)


def test_paquet_ailleurs_dans_le_depot(depot):
    """Paquet committé hors de `src/controle_ia/accumulation_b6/` du dépôt : non vérifiable, refus."""
    paquet_committe(depot)
    entree, _ = ecrit(depot)
    ailleurs, _ = paquet_committe(depot, "autre/accumulation_b6")
    with pytest.raises(rg.RefusRegistre, match="non vérifiable"):
        ca.controler_code(depot, entree, ailleurs)


# ------------------------------------------------------------------------------------------------- appel par la lecture
def _runs_accb6(j) -> list:
    return sorted(p.name for d in ("runs", "diag") for p in (j.racine / d).glob("*accb6*"))


def test_lecture_refusee_avant_tout_calcul(depot, tirages, monkeypatch):
    """Paquet importé (copie du jouet) changé après le commit cité : `lire` refuse (code 2) avant l'aiguillage, avant le manifeste ;
    ligne `REFUS-ACCB6` au journal propre ; aucun run ; `lecture-t07.json` jamais ouvert par l'aiguillage. Cas sain : les essais de
    bout en bout (contrôle passé, rapport écrit dans le résultat)."""
    j = construire(depot)
    with open(j.racine / DOSSIER_PAQUET_JOUET / "phrases_v1.py", "a", encoding="utf-8") as f:
        f.write("# changé\n")
    lus = []
    monkeypatch.setattr(gv, "lire_e4", lambda *a, **k: lus.append(a) or {})
    with pytest.raises(gv.RefusAccb6, match="CODE-ACCB6 : empreintes différentes"):
        lv.lire(j.racine, instant=T0 + 5000, dossier_code=j.racine / DOSSIER_PAQUET_JOUET)
    assert lus == [] and _runs_accb6(j) == []
    assert (j.racine / gv.JOURNAL_PROPRE).read_text(encoding="utf-8").splitlines()[-1].startswith("| REFUS-ACCB6 |")


def test_lecture_saine_ecrit_le_controle(depot, tirages):
    j = construire(depot, aiguillage="G-1")
    r = lv.lire(j.racine, instant=T0 + 5000, dossier_code=j.racine / DOSSIER_PAQUET_JOUET)
    assert r["controle_code"]["commit"] == git(j.racine, "rev-parse", "HEAD") and r["controle_code"]["fichiers"] >= 6


def test_commande_controle_le_paquet_reellement_importe(depot, capsys):
    """La commande ne prend aucun dossier : elle contrôle le paquet importé. Le fichier du jouet cite un commit du dépôt jetable,
    étranger au dépôt du paquet importé (ou paquet hors de tout dépôt, dans une copie) : refus, code 2. Avec le paquet du jouet
    désigné comme paquet importé : code 0."""
    j = construire(depot, aiguillage="G-1")
    assert lv.main(["lire", str(j.racine)]) == lv.CODE_REFUS
    assert "CODE-ACCB6" in capsys.readouterr().err
    assert ca.main(["verifier", str(j.racine)]) == 2


def test_commande_verifier_et_ecrire(depot, monkeypatch, capsys):
    j = construire(depot, aiguillage="G-1")
    monkeypatch.setattr(ca, "dossier_du_paquet", lambda: (j.racine / DOSSIER_PAQUET_JOUET).resolve())
    assert ca.main(["verifier", str(j.racine)]) == 0
    sortie = j.racine / "registres" / "code-accb6" / "code-accb6-v2.json"
    assert ca.main(["ecrire", str(j.racine), "HEAD", str(sortie)]) == 0
    assert json.loads(sortie.read_text())["commit"] == git(j.racine, "rev-parse", "HEAD")
    assert ca.main(["ecrire", str(j.racine), "HEAD", str(sortie)]) == 2
    assert ca.main(["autre"]) == 2


def test_fichier_du_commit_absent_de_la_liste_et_du_paquet_importe(depot):
    """Le commit cité porte un fichier du paquet que la liste n'a pas (et que le paquet importé n'a plus) : refus, même si tous les
    fichiers listés sont égaux (ajout après le banc : mutation C02 survivante)."""
    dossier, _ = paquet_committe(depot)
    (dossier / "intrus_v1.py").write_text("x = 1\n")
    git(depot, "add", DOSSIER_PAQUET_JOUET)
    git(depot, "commit", "-q", "-m", "intrus")
    _, d = ecrit(depot)
    del d["fichiers"][f"{ca.PREFIXE}intrus_v1.py"]
    (dossier / "intrus_v1.py").unlink()
    with pytest.raises(rg.RefusRegistre, match="fichiers du paquet au commit cité ≠ liste écrite"):
        ca.controler_code(depot, fichier_code(depot, d), dossier)
