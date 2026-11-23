"""Essais (R5) du programme de la branche d'entrée de T0.8 (`scripts/construire_branche_entree_t08_v1.py`) : cas sain et
artefacts — empreinte fausse, fichier interdit glissé dans la liste, branche déjà là, commit de 7b non cité, empreinte absente
du texte, branche relevée altérée. Dépôt jetable, données factices."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

import aide_t08_chaine_v1 as A

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("branche_t08", RACINE / "scripts" / "construire_branche_entree_t08_v1.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def _args(fx, ct, quoi="construire", **plus):
    a = [quoi, "--depot", str(fx["depot"]), "--commit-7b", fx["c7b"], "--commit-code", fx["ccode"], "--commit-texte", ct,
         "--texte", A.CH_TEXTE, "--config", A.CH_CONFIG]
    for k, v in plus.items():
        a += [f"--{k}", v]
    return a


@pytest.fixture
def fx(tmp_path):
    return A.depot_factice(tmp_path / "depot")


def test_cas_sain_liste_exacte_orpheline_sans_interdit(fx, capsys):
    ct = A.commit_texte(fx)
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 0
    r = json.loads(capsys.readouterr().out)
    attendus = sorted([*A.CH.values(), *A.GUIDE, A.CH_TEXTE, A.CH_CONFIG])
    attendus = sorted(attendus + [x + ".sha256" for x in attendus])
    assert sorted(r["fichiers"]) == attendus and r["nombre"] == 20
    d = fx["depot"]
    assert A.git(d, "rev-list", "--count", "entree/t08-essai") == "1"
    assert A.git(d, "rev-list", "--parents", "-n", "1", "entree/t08-essai").split() == [r["commit"]]
    objets = A.git(d, "rev-list", "--objects", "entree/t08-essai")
    assert "lecture-sondes" not in objets and "resume.json" not in objets and "mesures-t06.npz" not in objets
    for c in A.CH.values():                    # copie à l'octet : même blob que la source
        src = fx["c7b"] if c.startswith(("donnees/2026111", "diag/", "runs/")) else fx["ccode"]
        assert A.git(d, "rev-parse", f"entree/t08-essai:{c}") == A.git(d, "rev-parse", f"{src}:{c}")
    # la vérification seule, sur la référence écrite, rend la même liste
    assert B.main(_args(fx, ct, "verifier", ref="entree/t08-essai")) == 0


def test_artefact_empreinte_fausse_dans_la_configuration(fx, capsys):
    c = A.config_factice(fx)
    c["entrees"]["textes_7b"]["sha256"] = "f" * 64
    c["marqueurs"]["EMPREINTES_ENTREES_7B"]["textes-actions-t06.jsonl"] = "f" * 64
    ct = A.commit_texte(fx, c, A.texte_factice(fx) + ("f" * 64 + "\n").encode())
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 1
    assert "R11" in capsys.readouterr().err
    assert A.git(fx["depot"], "branch", "--list", "entree/t08-essai") == ""      # rien d'écrit


def test_artefact_fichier_altere_contre_son_compagnon(fx, capsys):
    d = fx["depot"]
    A.git(d, "checkout", "-q", "calcul/t06-confirmation-7b-factice")
    (d / A.CH["episodes_7b"]).write_bytes(b'{"altere": 1}\n')                  # compagnon gardé : écart
    A.git(d, "commit", "-qam", "altération")
    fx = {**fx, "c7b": A.git(d, "rev-parse", "HEAD")}
    ct = A.commit_texte(fx)
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 1
    assert "compagnon" in capsys.readouterr().err


def test_artefact_fichier_interdit_glisse_dans_la_liste(fx, capsys):
    c = A.config_factice(fx)
    c["entrees"]["episodes_7b"]["chemin"] = f"diag/{A.RUN_7B}/lecture-sondes-t06.json"
    ct = A.commit_texte(fx, c)
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 1
    err = capsys.readouterr().err
    assert "lecture-sondes" in err or "ne se termine pas" in err
    for nom in ("lecture-sondes-t06.json", "resume.json", "distillation-t06.json", "activations-001.npz", "adaptateur-hd.pt",
                "base-a-t08.json"):
        assert B.nom_interdit(f"diag/x/{nom}"), nom
    with pytest.raises(B.Arret):
        B.montrer(fx["depot"], fx["c7b"], f"diag/{A.RUN_7B}/lecture-sondes-t06.json")


def test_artefact_entree_hors_course_ajoutee(fx, capsys):
    c = A.config_factice(fx)
    c["entrees"]["mesures_7b"] = {"chemin": f"donnees/{A.RUN_7B}/mesures-t06.npz", "sha256": "1" * 64, "phase": "course"}
    ct = A.commit_texte(fx, c)
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 1
    assert "entrées de la course" in capsys.readouterr().err


def test_artefact_branche_deja_la(fx, capsys):
    ct = A.commit_texte(fx)
    A.git(fx["depot"], "branch", "entree/t08-essai", fx["ccode"])
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 1
    assert "existe déjà" in capsys.readouterr().err
    assert A.git(fx["depot"], "rev-parse", "entree/t08-essai") == fx["ccode"]      # inchangée


def test_artefact_commit_7b_non_cite_et_empreinte_absente_du_texte(fx, capsys):
    ct = A.commit_texte(fx, texte=b"texte sans la tete de 7b\n")
    assert B.main(_args(fx, ct, branche="entree/t08-a")) == 1
    assert "non cité" in capsys.readouterr().err
    ct = A.commit_texte(fx, texte=A.texte_factice(fx, sans=("episodes-t06.json",)), branche="main-factice-2")
    assert B.main(_args(fx, ct, branche="entree/t08-b")) == 1
    assert "absente du texte" in capsys.readouterr().err


def test_artefact_branche_relevee_alteree(fx, capsys):
    ct = A.commit_texte(fx)
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 0
    capsys.readouterr()
    d = fx["depot"]
    A.git(d, "checkout", "-q", "entree/t08-essai")
    (d / f"diag/{A.RUN_7B}/resume.json").parent.mkdir(parents=True, exist_ok=True)
    (d / f"diag/{A.RUN_7B}/resume.json").write_text("{}\n")
    A.git(d, "add", "-f", ".")
    A.git(d, "commit", "-qm", "ajout interdit")
    assert B.main(_args(fx, ct, "verifier", ref="entree/t08-essai")) == 1
    assert "parent" in capsys.readouterr().err
    # même ajout sur un commit orphelin (sans parent) : la liste exacte arrête
    A.git(d, "checkout", "-q", "--orphan", "entree/t08-orpheline")
    A.git(d, "commit", "-qm", "orpheline avec un fichier de trop")
    assert B.main(_args(fx, ct, "verifier", ref="entree/t08-orpheline")) == 1
    assert "liste blanche" in capsys.readouterr().err


def test_verification_seule_sans_la_branche_de_7b(fx, capsys):
    """Le lanceur vérifie la branche relevée sans la branche de 7b : sources lues dans la branche d'entrée, commit de 7b et du
    code pris dans son message ; artefacts : message altéré (commit du code autre que COMMIT_CODE_T08), autre texte."""
    c = A.config_factice(fx)
    c["marqueurs"]["COMMIT_CODE_T08"] = fx["ccode"]
    ct = A.commit_texte(fx, c)
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 0
    capsys.readouterr()
    v = ["verifier", "--depot", str(fx["depot"]), "--commit-texte", ct, "--texte", A.CH_TEXTE, "--config", A.CH_CONFIG,
         "--ref", "entree/t08-essai"]
    assert B.main(v) == 0
    assert json.loads(capsys.readouterr().out)["nombre"] == 20
    # message altéré : même arbre, commit du code consigné autre
    d = fx["depot"]
    arbre = A.git(d, "rev-parse", "entree/t08-essai^{tree}")
    msg = A.git(d, "log", "-1", "--format=%B", "entree/t08-essai").replace(fx["ccode"], fx["c7b"])
    faux = A.git(d, "commit-tree", arbre, entree=msg.encode())
    A.git(d, "branch", "entree/t08-faux", faux)
    assert B.main(v[:-1] + ["entree/t08-faux"]) == 1
    assert "COMMIT_CODE_T08" in capsys.readouterr().err
    # autre commit du texte que celui consigné
    ct2 = A.commit_texte(fx, c, branche="main-factice-autre")
    assert B.main(["verifier", "--depot", str(d), "--commit-texte", ct2, "--texte", A.CH_TEXTE, "--config", A.CH_CONFIG,
                   "--ref", "entree/t08-essai"]) == 1
    assert "commit du texte consigné" in capsys.readouterr().err


def test_artefact_commit_du_code_autre_que_celui_de_la_configuration(fx, capsys):
    """Contre-lecture m-1 : `construire` exige `--commit-code` égal à COMMIT_CODE_T08 de la configuration."""
    c = A.config_factice(fx)
    c["marqueurs"]["COMMIT_CODE_T08"] = fx["c7b"]
    ct = A.commit_texte(fx, c)
    assert B.main(_args(fx, ct, branche="entree/t08-essai")) == 1
    assert "COMMIT_CODE_T08" in capsys.readouterr().err
    assert A.git(fx["depot"], "branch", "--list", "entree/t08-essai") == ""
