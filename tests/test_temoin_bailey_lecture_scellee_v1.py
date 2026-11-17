"""Essais de la lecture scellée (`lecture_scellee_v1`, addendum 7 du témoin de Bailey, § 3) : chaque règle a un cas sain
et un artefact (R5). Sur processeur, sur dossiers factices seulement (aides de `test_temoin_bailey_condition6_v3`)."""
from __future__ import annotations

import io
import json
import subprocess
from contextlib import redirect_stdout
from pathlib import Path

import numpy as np
import pytest

from controle_ia import scellement
from controle_ia.gardes import GardeArret
from controle_ia.temoin_bailey import analyse_v3 as an
from controle_ia.temoin_bailey import lecture_scellee_v1 as ls

import test_temoin_bailey_condition6_v3 as T3

ATT = {"code": "c" * 40, "dossier": "d" * 64, "environnement": "e" * 64}


def fixe(valeurs=None):
    suite = list(valeurs or [])
    def calculer(_d):
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


def lancer(tmp_path, executer, calculer=None, attendu=ATT, sortie=None):
    tmp_path.mkdir(parents=True, exist_ok=True)
    a = tmp_path / "attendu.json"
    a.write_text(json.dumps(attendu))
    s = sortie or tmp_path / "lecture" / "sortie-v1.json"
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = ls.principal(["--dossier", str(tmp_path), "--sortie", str(s), "--attendu", str(a)],
                            executer=executer, calculer=calculer or fixe())
    return code, buf.getvalue(), s


def test_aboutie_une_seule_execution_sortie_scellee_et_retour_sans_valeur(tmp_path):
    ex = Executer({"verdict": "Effet reproduit …", "calcul": {"x": np.float64(0.5)}, "R_att": np.array([0.1])})
    code, out, s = lancer(tmp_path, ex)
    assert code == 0 and ex.appels == 1
    (ligne,) = out.strip().splitlines()
    r = json.loads(ligne)
    assert set(r) == {"empreinte_sortie", "issue"} and r["issue"] == ls.ISSUE_ABOUTIE
    assert scellement.verifier(s) == r["empreinte_sortie"]
    d = json.loads(s.read_text())
    assert d["lecture"]["verdict"].startswith("Effet") and d["lecture"]["calcul"]["x"] == 0.5
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
        code, out, _ = lancer(tmp_path / k, ex, calculer=fixe([{**ATT, k: "autre"}]))
        assert code == 2 and ex.appels == 0 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES


def test_attendu_incomplet_ou_en_trop_refus(tmp_path):
    for i, att in enumerate(({"code": ATT["code"], "dossier": ATT["dossier"]}, {**ATT, "autre": 1})):
        ex = Executer({"verdict": "x"})
        code, out, _ = lancer(tmp_path / str(i), ex, attendu=att)
        assert code == 2 and ex.appels == 0 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES


def test_changement_entre_les_deux_executions_vaut_refus(tmp_path):
    ex = Executer(GardeArret("a"), {"verdict": "Effet reproduit"})
    code, out, s = lancer(tmp_path, ex, calculer=fixe([ATT, {**ATT, "code": "corrigé"}]))
    assert code == 2 and ex.appels == 1 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES
    assert "lecture" not in json.loads(s.read_text())


def test_empreintes_incalculables_refus_sans_execution(tmp_path):
    def casse(_d):
        raise subprocess.CalledProcessError(128, "git")
    ex = Executer({"verdict": "x"})
    code, out, _ = lancer(tmp_path, ex, calculer=casse)
    assert code == 2 and ex.appels == 0 and json.loads(out)["issue"] == ls.ISSUE_EMPREINTES


def test_sortie_deja_presente_ou_scellee_rien_joue_rien_ecrit(tmp_path):
    s = tmp_path / "s.json"
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


def test_empreinte_dossier_octets_et_ordre(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    for d, ordre in ((a, "xy"), (b, "yx")):
        (d / "s").mkdir(parents=True)
        for n in ordre:
            (d / "s" / f"{n}.jsonl").write_bytes(n.encode())
    assert ls.empreinte_dossier(a) == ls.empreinte_dossier(b)
    (b / "s" / "x.jsonl").write_bytes(b"x ")
    assert ls.empreinte_dossier(a) != ls.empreinte_dossier(b)
    with pytest.raises(GardeArret):
        ls.empreinte_dossier(tmp_path / "absent")


def test_empreinte_code_refuse_src_modifie_hors_commit(depot):
    (depot / "src").mkdir()
    (depot / "src" / "m.py").write_text("x = 1\n")
    subprocess.run(["git", "-C", str(depot), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(depot), "commit", "-qm", "src"], check=True)
    h = ls.empreinte_code(depot)
    assert len(h) == 40
    (depot / "src" / "m.py").write_text("x = 2\n")
    assert ls.empreinte_code(depot) == "src/ modifié hors commit"
    (depot / "src" / "m.py").write_text("x = 1\n")
    (depot / "src" / "neuf.py").write_text("")
    assert ls.empreinte_code(depot) == "src/ modifié hors commit"


def test_bout_en_bout_dossier_factice_valider_et_lire_reels(tmp_path):
    """Le chemin réel du code (`valider`, `lire`, graine de rééchantillonnage) sur un dossier factice de forme réelle :
    l'essai de la commande avant la clôture (§ 3) en est un exemple ; empreintes du dossier réelles."""
    racine = T3.poste_local(tmp_path, 21, k_regle=21)
    calculer = lambda d: {"code": "c", "dossier": ls.empreinte_dossier(d), "environnement": "e"}
    att = calculer(racine)
    a = tmp_path / "attendu.json"
    a.write_text(json.dumps(att))
    s = tmp_path / "sortie-lecture-v1.json"
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = ls.principal(["--dossier", str(racine), "--sortie", str(s), "--attendu", str(a)], calculer=calculer)
    d = json.loads(s.read_text())
    assert d["issue"] == ls.ISSUE_ABOUTIE, d["executions"]
    attendu_direct = ls.une_execution(racine)["verdict"]
    assert d["lecture"]["verdict"] == attendu_direct and code == 0
    assert ls.empreinte_dossier(racine) == att["dossier"]  # la lecture n'a rien écrit dans le dossier


def test_calculer_attendu_ne_joue_aucune_lecture(tmp_path, monkeypatch):
    monkeypatch.setattr(ls, "une_execution", lambda d: pytest.fail("lecture jouée"))
    buf = io.StringIO()
    with redirect_stdout(buf):
        assert ls.principal(["--calculer-attendu", str(tmp_path)], calculer=fixe()) == 0
    assert json.loads(buf.getvalue()) == ATT
