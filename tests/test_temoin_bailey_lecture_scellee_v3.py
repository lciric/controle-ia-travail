"""Essais de la lecture scellée v3 (`lecture_scellee_v3`, ceux de la v2 rejoués, plus les artefacts de la vérification
adverse v8 en fin de fichier ;, addendum 7 du témoin de Bailey, § 3) : chaque règle a un cas
sain et un artefact (R5), dont les deux artefacts de la vérification adverse v7 (répertoire vide qui change le verdict
sans changer l'empreinte ; `src/` modifié qui passait). Sur processeur, sur dossiers factices seulement (aides de
`test_temoin_bailey_condition6_v3`) et dans des dépôts git jetables."""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
from contextlib import redirect_stdout
from pathlib import Path

import numpy as np
import pytest

from controle_ia import scellement
from controle_ia.gardes import GardeArret
from controle_ia.temoin_bailey import lecture_scellee_v3 as ls

import test_temoin_bailey_condition6_v3 as T3

PYTHON = str(Path(sys.executable))
SRC = str(Path(ls.__file__).resolve().parents[2])


@pytest.fixture(autouse=True)
def _sans_garde_de_commande(request, monkeypatch):
    """En processus, pytest ne porte ni `-B` ni `-P` : la garde de commande est éprouvée à part, en sous-processus."""
    if "garde_de_commande_reelle" not in request.keywords:
        monkeypatch.setattr(ls, "garde_commande", lambda depot=None: None)

ATT = {"commit": "a" * 40, "code": "c" * 40, "dossier": "d" * 64, "environnement": "e" * 64}


def fixe(valeurs=None):
    suite = list(valeurs or [])
    def calculer(_d, _c):
        return dict(suite.pop(0)) if suite else dict(ATT)
    return calculer


class Executer:
    def __init__(self, *issues):
        self.issues, self.appels = list(issues), 0

    def __call__(self, _d):
        self.appels += 1
        x = self.issues.pop(0)
        if isinstance(x, BaseException):
            raise x
        return x


def sortie_std(f, *a, **k):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = f(*a, **k)
    return code, buf.getvalue()


def lancer(tmp_path, executer, calculer=None, attendu=ATT, sortie=None, texte_attendu=None):
    tmp_path.mkdir(parents=True, exist_ok=True)
    a = tmp_path / "attendu.json"
    a.write_text(texte_attendu if texte_attendu is not None else json.dumps(attendu))
    s = sortie or tmp_path / "lecture" / "sortie-v1.json"
    lu = tmp_path / "dossier-lu"  # v3 : ni l'attendu ni la sortie sous le dossier lu
    lu.mkdir(exist_ok=True)
    code, out = sortie_std(ls.principal, ["--dossier", str(lu), "--sortie", str(s), "--attendu", str(a)],
                           executer=executer, calculer=calculer or fixe())
    return code, out, s


def depot_git(racine: Path) -> Path:
    def g(*args):
        subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True)
    racine.mkdir(parents=True, exist_ok=True)
    g("init", "-q", "-b", "main")
    g("config", "user.email", "t@example.invalid")
    g("config", "user.name", "t")
    (racine / "src").mkdir()
    (racine / "src" / "m.py").write_text("x = 1\n")
    g("add", "-A")
    g("commit", "-qm", "src")
    return racine


def tete(racine: Path) -> str:
    return subprocess.run(["git", "-C", str(racine), "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


# --- Règles 1 à 5 ---------------------------------------------------------------------------------------------------

def test_aboutie_une_seule_execution_sortie_scellee_et_retour_sans_valeur(tmp_path):
    ex = Executer({"verdict": "Effet reproduit …", "calcul": {"x": np.float64(0.5)}, "R_att": np.array([0.1])})
    code, out, s = lancer(tmp_path, ex)
    assert code == 0 and ex.appels == 1
    (ligne,) = out.strip().splitlines()
    r = json.loads(ligne)
    assert set(r) == {"empreinte_sortie", "issue"} and r["issue"] == ls.ISSUE_ABOUTIE
    assert scellement.verifier(s) == r["empreinte_sortie"]
    d = json.loads(s.read_text())
    assert d["version"] == "lecture_scellee_v3" and d["lecture"]["calcul"]["x"] == 0.5
    assert [e["n"] for e in d["executions"]] == [1] and d["executions"][0]["aboutie"] is True


def test_etat_pas_de_verdict_est_une_execution_qui_aboutit_jamais_rejouee(tmp_path):
    ex = Executer({"verdict": "Pas de run principal, pas de verdict (…)."}, {"verdict": "Effet reproduit"})
    code, _, s = lancer(tmp_path, ex)
    assert code == 0 and ex.appels == 1 and json.loads(s.read_text())["lecture"]["verdict"].startswith("Pas de run")


def test_refus_puis_succes_seconde_execution_retenue_premier_echec_dit(tmp_path):
    ex = Executer(GardeArret("lecture : fichier absent (x.jsonl)"), {"verdict": "Effet non reproduit"})
    code, _, s = lancer(tmp_path, ex)
    d = json.loads(s.read_text())
    assert code == 0 and ex.appels == 2 and d["issue"] == ls.ISSUE_ABOUTIE
    assert d["executions"][0]["message"] == "lecture : fichier absent (x.jsonl)" and d["executions"][1]["aboutie"]


def test_deux_refus_pas_de_troisieme_execution(tmp_path):
    ex = Executer(GardeArret("a"), GardeArret("a"), {"verdict": "jamais"})
    code, out, s = lancer(tmp_path, ex)
    assert code == 2 and ex.appels == 2 and json.loads(out)["issue"] == ls.ISSUE_REFUS
    assert "lecture" not in json.loads(s.read_text())


def test_erreur_hors_garde_message_jamais_ecrit_type_et_lieu_seulement(tmp_path):
    ex = Executer(ValueError("note 0.7342 du tour 3"), ValueError("note 0.7342 du tour 3"))
    code, out, s = lancer(tmp_path, ex)
    texte = s.read_text()
    assert code == 2 and "0.7342" not in texte and "0.7342" not in out
    e = json.loads(texte)["executions"]
    assert [x["echec"] for x in e] == ["ValueError", "ValueError"] and all(":" in x["lieu"] for x in e)


def test_empreintes_differentes_aucune_execution(tmp_path):
    for k in ATT:
        ex = Executer({"verdict": "x"})
        code, out, _ = lancer(tmp_path / k, ex, calculer=fixe([{**ATT, k: ATT[k][:-1] + "0"}]))
        assert code == 2 and ex.appels == 0 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES


@pytest.mark.parametrize("att", [
    {k: v for k, v in ATT.items() if k != "environnement"},
    {**ATT, "autre": "f" * 64},
    {**ATT, "code": "src/ modifié hors commit"},
    {**ATT, "dossier": "D" * 64},
    {**ATT, "commit": 12},
    ["liste"],
])
def test_attendu_non_conforme_refus_sans_execution_ni_calcul(tmp_path, att):
    ex = Executer({"verdict": "x"})
    calc = lambda d, c: pytest.fail("empreintes calculées sur un attendu non conforme")
    code, out, s = lancer(tmp_path, ex, calculer=calc, attendu=att)
    assert code == 2 and ex.appels == 0 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES
    assert json.loads(s.read_text())["attendu_non_conforme"] is True


def test_attendu_illisible_refus(tmp_path):
    code, out, _ = lancer(tmp_path, Executer({"verdict": "x"}), texte_attendu="{pas du json")
    assert code == 2 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES


def test_changement_entre_les_deux_executions_vaut_refus(tmp_path):
    ex = Executer(GardeArret("a"), {"verdict": "Effet reproduit"})
    code, out, s = lancer(tmp_path, ex, calculer=fixe([ATT, {**ATT, "code": "b" * 40}]))
    assert code == 2 and ex.appels == 1 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES
    assert "lecture" not in json.loads(s.read_text())


def test_empreintes_refusees_ou_incalculables_refus_sans_execution(tmp_path):
    for i, x in enumerate((GardeArret("lecture scellée : src/ modifié hors commit"),
                           subprocess.CalledProcessError(128, "git"))):
        def casse(_d, _c, x=x):
            raise x
        ex = Executer({"verdict": "x"})
        code, out, s = lancer(tmp_path / str(i), ex, calculer=casse)
        assert code == 2 and ex.appels == 0 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES
        e = json.loads(s.read_text())["executions"][0]
        assert e["echec_empreintes"] == type(x).__name__ and (("message" in e) is (i == 0))


def test_sortie_deja_presente_ou_scellee_rien_joue_rien_ecrit(tmp_path):
    s = tmp_path / "s.json"
    tmp_path.mkdir(exist_ok=True)
    s.write_text("premier")
    ex = Executer({"verdict": "x"})
    code, out, _ = lancer(tmp_path, ex, sortie=s)
    assert code == 3 and ex.appels == 0 and s.read_text() == "premier" and "R12" in out
    s2 = tmp_path / "s2.json"
    scellement.compagnon(s2).write_text("0" * 64 + "  s2.json\n")
    code, _, _ = lancer(tmp_path, Executer({"verdict": "x"}), sortie=s2)
    assert code == 3 and not s2.exists()


def test_sortie_non_serialisable_echec_mecanique(tmp_path):
    code, out, s = lancer(tmp_path, Executer({"verdict": "x", "objet": object()}))
    d = json.loads(s.read_text())
    assert code == 2 and json.loads(out)["issue"] == ls.ISSUE_REFUS and "lecture" not in d
    assert d["echec_sortie"] == "TypeError"


# --- Empreintes -----------------------------------------------------------------------------------------------------

def test_empreinte_dossier_octets_ordre_repertoires_vides_et_liens(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    for d, ordre in ((a, "xy"), (b, "yx")):
        (d / "s").mkdir(parents=True)
        for n in ordre:
            (d / "s" / f"{n}.jsonl").write_bytes(n.encode())
    assert ls.empreinte_dossier(a) == ls.empreinte_dossier(b)
    (b / "vide").mkdir()
    assert ls.empreinte_dossier(a) != ls.empreinte_dossier(b)
    (b / "vide").rmdir()
    (b / "s" / "x.jsonl").write_bytes(b"x ")
    assert ls.empreinte_dossier(a) != ls.empreinte_dossier(b)
    os.symlink(a / "s", b / "lien")
    with pytest.raises(GardeArret, match="lien symbolique"):
        ls.empreinte_dossier(b)
    os.symlink(a, tmp_path / "c")
    with pytest.raises(GardeArret):
        ls.empreinte_dossier(tmp_path / "c")
    with pytest.raises(GardeArret):
        ls.empreinte_dossier(tmp_path / "absent")


def test_artefact_v7_repertoire_vide_qui_change_le_verdict_change_l_empreinte(tmp_path):
    """Artefact de la vérification v7 : un répertoire vide `pilote-reprise/` change le verdict de `valider` ; ajouté
    après l'attendu, il donne désormais « refus : empreintes » et aucune exécution."""
    racine = T3.poste_local(tmp_path, 21, k_regle=21)
    avant = ls.une_execution(racine)["verdict"]
    calculer = lambda d, c: {**ATT, "dossier": ls.empreinte_dossier(d)}
    att = calculer(racine, None)
    (racine / "pilote-reprise").mkdir()
    assert ls.une_execution(racine)["verdict"] != avant  # le répertoire vide change bien la lecture
    code, out, _ = lancer(tmp_path / "l", Executer({"verdict": "x"}), calculer=calculer, attendu=att,
                          sortie=tmp_path / "l" / "s.json")
    assert json.loads(out)["issue"] == ls.ISSUE_EMPREINTES


def test_arbre_src_propre_refuse_modification_et_fichier_non_suivi(tmp_path):
    r = depot_git(tmp_path / "depot")
    h = ls.arbre_src_propre(r)
    assert len(h) == 40 and h == ls.arbre_src_du_commit(tete(r), r)
    (r / "src" / "m.py").write_text("x = 2\n")
    with pytest.raises(GardeArret, match="src/ modifié hors commit"):
        ls.arbre_src_propre(r)
    (r / "src" / "m.py").write_text("x = 1\n")
    (r / "src" / "sous").mkdir()
    (r / "src" / "sous" / "neuf.py").write_text("")
    with pytest.raises(GardeArret):
        ls.arbre_src_propre(r)


def test_artefact_v7_code_modifie_jamais_lu_meme_si_l_attendu_a_ete_pris_sur_un_arbre_sale(tmp_path):
    """Artefact de la vérification v7 : un attendu ne peut plus être pris sur un `src/` modifié (refus), et une lecture
    sur un `src/` modifié est un refus, quel que soit l'attendu."""
    r = depot_git(tmp_path / "depot")
    d = tmp_path / "dossier"
    d.mkdir()
    (r / "src" / "brouillon.py").write_text("")
    with pytest.raises(GardeArret):
        ls.calculer_attendu(d, tete(r), r)
    (r / "src" / "brouillon.py").unlink()
    att = ls.calculer_attendu(d, tete(r), r)
    (r / "src" / "m.py").write_text("x = 'forgé'\n")
    ex = Executer({"verdict": "VERDICT FORGÉ"})
    code, out, _ = lancer(tmp_path / "l", ex, calculer=lambda dd, c: ls.calculer_attendu(d, c, r), attendu=att,
                          sortie=tmp_path / "l" / "s.json")
    assert code == 2 and ex.appels == 0 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES


def test_calculer_attendu_refuse_un_commit_dont_l_arbre_src_differe(tmp_path):
    r = depot_git(tmp_path / "depot")
    c0 = tete(r)
    (r / "src" / "m.py").write_text("x = 3\n")
    subprocess.run(["git", "-C", str(r), "commit", "-qam", "change"], check=True)
    d = tmp_path / "dossier"
    d.mkdir()
    with pytest.raises(GardeArret, match="différent de celui du commit nommé"):
        ls.calculer_attendu(d, c0, r)
    with pytest.raises(GardeArret, match="commit non conforme"):
        ls.calculer_attendu(d, "HEAD", r)
    att = ls.calculer_attendu(d, tete(r), r)
    assert ls.attendu_conforme(att) and att["commit"] == tete(r)


def test_empreinte_environnement_stable_et_porte_l_interpreteur(monkeypatch):
    a = ls.empreinte_environnement()
    assert a == ls.empreinte_environnement()
    monkeypatch.setattr(sys, "executable", "/autre/python")
    assert ls.empreinte_environnement() != a
    monkeypatch.undo()
    monkeypatch.setattr(sys, "path", [*sys.path, "/ailleurs"])
    assert ls.empreinte_environnement() != a


def test_cli_calculer_attendu_ecrit_et_scelle_seulement_en_cas_de_succes(tmp_path):
    v = tmp_path / "attendu.json"
    lu = tmp_path / "lu"
    lu.mkdir()
    code, out = sortie_std(ls.principal, ["--calculer-attendu", str(lu), "--commit", "a" * 40, "--vers", str(v)],
                           calculer=fixe())
    assert code == 0 and json.loads(v.read_text()) == ATT and scellement.verifier(v) == json.loads(out)["empreinte_attendu"]
    code, out = sortie_std(ls.principal, ["--calculer-attendu", str(lu), "--commit", "a" * 40, "--vers", str(v)],
                           calculer=fixe())
    assert code == 3 and "R12" in out
    v2 = tmp_path / "attendu-2.json"
    def refuse(_d, _c):
        raise GardeArret("lecture scellée : src/ modifié hors commit")
    with pytest.raises(GardeArret):
        sortie_std(ls.principal, ["--calculer-attendu", str(lu), "--commit", "a" * 40, "--vers", str(v2)],
                   calculer=refuse)
    assert not v2.exists()


def test_calculer_attendu_ne_joue_aucune_lecture(tmp_path, monkeypatch):
    monkeypatch.setattr(ls, "une_execution", lambda d: pytest.fail("lecture jouée"))
    monkeypatch.setattr(ls.lc, "valider", lambda d: pytest.fail("valider joué"))
    monkeypatch.setattr(ls.lc, "lire", lambda *a: pytest.fail("lire joué"))
    r = depot_git(tmp_path / "depot")
    d = T3.poste_local(tmp_path / "f", 21, k_regle=21)
    assert ls.attendu_conforme(ls.calculer_attendu(d, tete(r), r))


# --- Contrôle (règle 6) ---------------------------------------------------------------------------------------------

def test_controler_conforme_puis_chaque_ecart(tmp_path):
    code, out, s = lancer(tmp_path, Executer({"verdict": "x"}))
    h = json.loads(out)["empreinte_sortie"]
    a = tmp_path / "attendu.json"
    lu = str(tmp_path / "dossier-lu")
    ok = lambda **k: ls.controler(k.get("s", s), k.get("a", a), k.get("d", lu), k.get("h", h))
    assert ok()
    assert not ok(h="0" * 64)
    assert not ok(d=str(tmp_path / "autre"))
    a2 = tmp_path / "attendu-autre.json"
    a2.write_text(json.dumps({**ATT, "code": "b" * 40}))
    assert not ok(a=a2)
    assert not ok(s=tmp_path / "absente.json")
    s.write_text(s.read_text().replace('"x"', '"y"'))
    assert not ok()
    code, out = sortie_std(ls.principal, ["--controler", str(s), "--attendu", str(a), "--dossier", lu,
                                          "--empreinte", h])
    assert code == 2 and json.loads(out) == {"controle": "écart"}


def test_controler_refuse_une_sortie_v2(tmp_path):
    s = tmp_path / "s.json"
    a = tmp_path / "a.json"
    a.write_text(json.dumps(ATT))
    s.write_text(json.dumps({"version": "lecture_scellee_v2", "attendu": ATT, "dossier": str(tmp_path)}))
    h = scellement.sceller(s)
    assert not ls.controler(s, a, str(tmp_path), h)


# --- Bout en bout ---------------------------------------------------------------------------------------------------

def test_bout_en_bout_dossier_factice_valider_et_lire_reels_lecture_entiere_egale(tmp_path):
    """Chemin réel du code (`valider`, `lire`, graine) sur un dossier factice de forme réelle : la lecture entière de la
    sortie est égale à `valider` + `lire` joués directement ; le dossier n'est pas modifié ; contrôle conforme."""
    racine = T3.poste_local(tmp_path, 21, k_regle=21)
    calculer = lambda d, c: {**ATT, "dossier": ls.empreinte_dossier(d)}
    att = calculer(racine, None)
    a = tmp_path / "attendu.json"
    a.write_text(json.dumps(att))
    s = tmp_path / "sortie-lecture-v1.json"
    code, out = sortie_std(ls.principal, ["--dossier", str(racine), "--sortie", str(s), "--attendu", str(a)],
                           calculer=calculer)
    d = json.loads(s.read_text())
    assert code == 0 and d["issue"] == ls.ISSUE_ABOUTIE, d["executions"]
    direct = json.loads(json.dumps(ls.une_execution(racine), default=ls._en_json))
    assert d["lecture"] == direct
    assert ls.empreinte_dossier(racine) == att["dossier"]
    assert ls.controler(s, a, str(racine), json.loads(out)["empreinte_sortie"])


# --- v3 : artefacts de la vérification adverse v8 -------------------------------------------------------------------

def test_v8_controle_conforme_avec_barre_finale_double_barre_et_point(tmp_path):
    racine = T3.poste_local(tmp_path, 21, k_regle=21)
    calculer = lambda d, c: {**ATT, "dossier": ls.empreinte_dossier(d)}
    a = tmp_path / "attendu.json"
    a.write_text(json.dumps(calculer(racine, None)))
    s = tmp_path / "sortie.json"
    code, out = sortie_std(ls.principal, ["--dossier", str(racine) + "/", "--sortie", str(s), "--attendu", str(a)],
                           calculer=calculer)
    h = json.loads(out)["empreinte_sortie"]
    assert code == 0 and json.loads(s.read_text())["dossier"] == str(racine.resolve())
    for forme in (str(racine), str(racine) + "/", str(racine.parent) + "//" + racine.name, str(racine) + "/./"):
        assert ls.controler(s, a, forme, h), forme
    assert not ls.controler(s, a, str(racine.parent), h)


def test_v8_attendu_ou_sortie_sous_le_dossier_lu_refus_sans_rien_ecrire(tmp_path):
    d = tmp_path / "d"
    d.mkdir()
    code, out = sortie_std(ls.principal, ["--calculer-attendu", str(d), "--commit", "a" * 40, "--vers",
                                          str(d / "attendu.json")], calculer=fixe())
    assert code == 3 and not (d / "attendu.json").exists() and "sous le dossier lu" in out
    a = tmp_path / "attendu.json"
    a.write_text(json.dumps(ATT))
    ex = Executer({"verdict": "x"})
    code, out = sortie_std(ls.principal, ["--dossier", str(d), "--sortie", str(d / "s.json"), "--attendu", str(a)],
                           executer=ex, calculer=fixe())
    assert code == 3 and ex.appels == 0 and not (d / "s.json").exists()
    a2 = d / "attendu.json"
    a2.write_text(json.dumps(ATT))
    code, _ = sortie_std(ls.principal, ["--dossier", str(d), "--sortie", str(tmp_path / "s.json"), "--attendu",
                                        str(a2)], executer=ex, calculer=fixe())
    assert code == 3 and ex.appels == 0 and not (tmp_path / "s.json").exists()


def test_v8_fichier_ignore_sous_src_refuse_pycache_permis(tmp_path):
    r = depot_git(tmp_path / "depot")
    (r / ".gitignore").write_text("*.so\n__pycache__/\n")
    subprocess.run(["git", "-C", str(r), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(r), "commit", "-qm", "ignore"], check=True)
    (r / "src" / "__pycache__").mkdir()
    (r / "src" / "__pycache__" / "m.cpython-311.pyc").write_bytes(b"x")
    assert len(ls.arbre_src_propre(r)) == 40
    (r / "src" / "m.so").write_bytes(b"x")
    with pytest.raises(GardeArret):
        ls.arbre_src_propre(r)


def _sous_processus(code_python, cwd, drapeaux=("-B", "-P"), prefixe=True, tmp=None):
    env = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON")}
    env["PYTHONPATH"] = SRC
    if prefixe:
        env["PYTHONPYCACHEPREFIX"] = str(tmp)
    return subprocess.run([PYTHON, *drapeaux, "-c", code_python], cwd=cwd, env=env, capture_output=True, text=True)


@pytest.mark.garde_de_commande_reelle
def test_v8_garde_de_commande_en_sous_processus(tmp_path):
    prog = "from controle_ia.temoin_bailey import lecture_scellee_v3 as ls; ls.garde_commande(); print('ok')"
    assert _sous_processus(prog, tmp_path, tmp=tmp_path / "pyc").stdout.strip() == "ok"
    for drapeaux, prefixe in ((("-B",), True), (("-P",), True), (("-B", "-P"), False)):
        r = _sous_processus(prog, tmp_path, drapeaux, prefixe, tmp=tmp_path / "pyc")
        assert r.returncode != 0 and "GardeArret" in r.stderr, (drapeaux, prefixe)
    r = _sous_processus(prog, tmp_path, tmp=Path(SRC) / "pyc-interdit")
    assert r.returncode != 0 and "sous src/" in r.stderr
    assert not (Path(SRC) / "pyc-interdit").exists() or not any((Path(SRC) / "pyc-interdit").rglob("*.pyc"))


@pytest.mark.garde_de_commande_reelle
def test_v8_empreinte_environnement_independante_du_repertoire_courant(tmp_path):
    prog = "from controle_ia.temoin_bailey import lecture_scellee_v3 as ls; print(ls.empreinte_environnement())"
    (tmp_path / "a").mkdir()
    (tmp_path / "b" / "c").mkdir(parents=True)
    h = [_sous_processus(prog, tmp_path / x, tmp=tmp_path / f"pyc-{i}").stdout.strip()
         for i, x in enumerate(("a", "b/c"))]
    assert len(h[0]) == 64 and h[0] == h[1]
