"""Essais de la relance du rejeu (jeton à grain fin, repli, poussée témoin, garde des 30 caractères) — R5."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from controle_ia import relance_rejeu_jeton_v1 as J
from controle_ia import rejeu_activations_voie_a_v2 as R

A40 = "ghp_" + "a" * 36
B40 = "github_pat_" + "b" * 40


def test_garde_jetons():
    assert J.garde_jetons({J.JETON_PRINCIPAL: B40, J.JETON_REPLI: A40}) == {"GH_TOKEN_A": B40, "GH_TOKEN_B": A40}
    for env in ({J.JETON_PRINCIPAL: "x" * 14, J.JETON_REPLI: A40}, {J.JETON_PRINCIPAL: A40, J.JETON_REPLI: A40},
                {J.JETON_REPLI: A40}, {J.JETON_PRINCIPAL: B40, J.JETON_REPLI: "a b" + "c" * 40}):
        with pytest.raises(R.Refus):
            J.garde_jetons(env)


def test_script_forme():
    s = J.script_de_demarrage("c" * 40, "docs/o.json", "d" * 64)
    assert A40 not in s and B40 not in s
    i_secours, i_clone = s.index("minuterie-secours"), s.index("clone -q")
    i_temoin, i_amorce = s.index(J.BRANCHE_TEMOIN), s.index("rejeu_activations_voie_a_v2.py machine")
    assert i_secours < i_clone < i_temoin < i_amorce
    assert s.index("unset GH_TOKEN_A GH_TOKEN_B") < i_amorce and "method='DELETE'" in s


def lancer_script(tmp_path, depot_url, env_jetons, preparer=None):
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=tmp_path / "source", capture_output=True,
                            text=True).stdout.strip() if (tmp_path / "source").exists() else "c" * 40
    s = J.script_de_demarrage(commit, "docs/o.json", "d" * 64)
    corps = s[s.index("A='!f()"):]
    corps = corps[:corps.index("python3 -I -B /root/depot/src")] + \
        "echo AMORCE GH=${GH_TOKEN:+present} A=${GH_TOKEN_A:+present} B=${GH_TOKEN_B:+present}"
    corps = corps.replace("/root", str(tmp_path / "racine")).replace("sleep infinity", "true")
    corps = corps.replace(corps[corps.index("for k in 1 2 3 4 5; do python3"):corps.index("; done; true")],
                          "for k in 1; do echo DESTRUCTION_DEMANDEE")
    (tmp_path / "racine").mkdir(exist_ok=True)
    if preparer:
        preparer(tmp_path / "racine")
    env = {"PATH": os.environ["PATH"], "HOME": str(tmp_path), "DEPOT_URL": str(depot_url), "GIT_TERMINAL_PROMPT": "0",
           "GIT_CONFIG_GLOBAL": str(tmp_path / "gitconfig"), **env_jetons}
    (tmp_path / "gitconfig").write_text("[user]\n\tname = e\n\temail = e@x\n")
    r = subprocess.run(["bash", "-c", "set -u; " + corps], env=env, capture_output=True, text=True, timeout=120)
    return r.stdout + r.stderr, commit


@pytest.fixture
def depot(tmp_path):
    src = tmp_path / "source"
    src.mkdir()
    for a in (["init", "-q"], ["-c", "user.name=e", "-c", "user.email=e@x", "commit", "-q", "--allow-empty", "-m", "a"]):
        subprocess.run(["git", *a], cwd=src, check=True)
    nu = tmp_path / "distant.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(src), str(nu)], check=True)
    return nu


def test_script_sain_jeton_principal(tmp_path, depot):
    sortie, commit = lancer_script(tmp_path, depot, {"GH_TOKEN_A": B40, "GH_TOKEN_B": A40})
    assert A40 not in sortie and B40 not in sortie
    assert "JETON A : clonage et poussée témoin réussis" in sortie
    assert "AMORCE GH=present A= B=" in sortie and "DESTRUCTION" not in sortie
    r = subprocess.run(["git", "ls-remote", str(depot), f"refs/heads/{J.BRANCHE_TEMOIN}"], capture_output=True, text=True)
    assert r.stdout.split()[0] == commit
    assert (tmp_path / "racine/jeton-choisi.txt").read_text().strip() == "A"


def test_script_repli_sur_le_second_jeton(tmp_path, depot):
    sortie, _ = lancer_script(tmp_path, depot, {"GH_TOKEN_A": "", "GH_TOKEN_B": A40})
    assert "JETON B : clonage et poussée témoin réussis" in sortie and "AMORCE GH=present" in sortie


def test_script_deux_jetons_refuses_detruit_sans_amorce(tmp_path, depot):
    sortie, _ = lancer_script(tmp_path, tmp_path / "inexistant.git", {"GH_TOKEN_A": B40, "GH_TOKEN_B": A40})
    assert A40 not in sortie and B40 not in sortie
    assert "JETON A : refusé" in sortie and "JETON B : refusé" in sortie and "JETONS REFUSÉS" in sortie
    assert "DESTRUCTION_DEMANDEE" in sortie and "AMORCE" not in sortie


def test_script_redemarrage_reprend_le_jeton_sans_recloner(tmp_path, depot):
    def preparer(racine):
        (racine / "depot/.git").mkdir(parents=True)
        (racine / "jeton-choisi.txt").write_text("B\n")
    sortie, _ = lancer_script(tmp_path, tmp_path / "inexistant.git", {"GH_TOKEN_A": B40, "GH_TOKEN_B": A40}, preparer)
    assert "REDÉMARRAGE : jeton B repris" in sortie and "AMORCE GH=present" in sortie and "clonage" not in sortie


def test_lire_reponse():
    assert J.lire_reponse('{\n  "success": true,\n  "new_contract": 123\n}\n')["new_contract"] == 123
    assert J.lire_reponse('bruit\n{"success": true, "new_contract": 7}\n')["new_contract"] == 7
    assert J.lire_reponse("rien de lisible") is None


def test_creation_porte_les_deux_jetons_et_pas_gh_token(tmp_path):
    outil = tmp_path / "outil.py"
    trace = tmp_path / "argv.json"
    outil.write_text("import json, sys\n"
                     f"json.dump(sys.argv, open({str(trace)!r}, 'w'))\n"
                     "print('{\\n  \"success\": true,\\n  \"new_contract\": 424242\\n}')\n")
    exe = tmp_path / "vastai"
    exe.write_text(f"#!/bin/sh\nexec {sys.executable} {outil} \"$@\"\n")
    exe.chmod(0o755)
    c = J.ClientCreation("cle-factice-1234", str(exe), {"GH_TOKEN_A": B40, "GH_TOKEN_B": A40})
    corps = {"image": "img", "disk": 100, "label": R.ETIQUETTE, "script": "echo x",
             "env": {"GH_TOKEN": B40, "HF_TOKEN": "hf_" + "h" * 30, "GO_ID": "GO-2026-11-24-13"}}
    assert c.creer(1, corps, {"GH_TOKEN": B40}) == 424242
    env = json.loads(trace.read_text())[json.loads(trace.read_text()).index("--env") + 1]
    assert f"-e GH_TOKEN_A={B40}" in env and f"-e GH_TOKEN_B={A40}" in env and "-e GH_TOKEN=" not in env


def test_script_premier_jeton_refuse_a_la_poussee_puis_second_reussit(tmp_path, depot):
    crochet = depot / "hooks/pre-receive"
    compteur = tmp_path / "poussees.txt"
    crochet.write_text(f"#!/bin/sh\nn=$(cat {compteur} 2>/dev/null || echo 0); echo $((n+1)) > {compteur}\n"
                       "[ \"$n\" = 0 ] && exit 1\nexit 0\n")
    crochet.chmod(0o755)
    sortie, _ = lancer_script(tmp_path, depot, {"GH_TOKEN_A": B40, "GH_TOKEN_B": A40})
    assert A40 not in sortie and B40 not in sortie
    assert "JETON A : refusé" in sortie and "JETON B : clonage et poussée témoin réussis" in sortie
    assert "AMORCE GH=present A= B=" in sortie and (tmp_path / "racine/jeton-choisi.txt").read_text().strip() == "B"


def test_script_redemarrage_lettre_illisible_ne_reprend_rien(tmp_path, depot):
    def preparer(racine):
        (racine / "depot/.git").mkdir(parents=True)
        (racine / "jeton-choisi.txt").write_text("A; touch /tmp/x\n")
    sortie, _ = lancer_script(tmp_path, depot, {"GH_TOKEN_A": B40, "GH_TOKEN_B": A40}, preparer)
    assert "lettre de jeton illisible" in sortie and "REDÉMARRAGE : jeton" not in sortie


def test_code_de_destruction_compile():
    import re
    s = J.script_de_demarrage("c" * 40, "docs/o.json", "d" * 64)
    codes = re.findall(r'python3 -I -B -c "([^"]*DELETE[^"]*)"', s)
    assert len(codes) == 2                       # minuterie de secours (v2) et destruction sur refus des jetons
    for c in codes:
        compile(c, "<destruction>", "exec")
