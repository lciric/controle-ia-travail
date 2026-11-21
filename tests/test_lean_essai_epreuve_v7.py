"""Essais de l'épreuve d'isolement v7 et des attendus v6 (essai Lean D-1a ; arbitrage Fable 5.2, point 7, pas 2, 3 et 5).

Sans chaîne (toujours joués) : jugement des tentatives (motifs d'ECHEC sans valeur de preuve), cas sain vivant, statut
« épreuve morte » distinct de « non conforme » (R5 : sur un cas sain et sur un artefact), sortie de compilation bornée dans le
JSON, groupe `limites_lean`, items sondes v3 = v2 plus `.toString` seulement, attendus v6 = v5 plus les changements déclarés.
Avec la chaîne épinglée (`LEAN_ESSAI_D1A_CHAINE`, comme `test_lean_essai_verificateur_v6.py`) : les items sondes v2 ne
compilent pas, avec l'erreur `String.Slice` (cause établie) ; les items v3, compilés comme le bac les compile dans un bac à
sable de montage (`compiler_comme_bac_v1.sh`, root et `unshare` exigés, sinon sauté en le disant), rendent leurs tentatives.
"""
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest

from controle_ia.lean_essai import epreuve_isolement_v7 as E

RACINE = Path(__file__).resolve().parents[1]
ART = RACINE / "scripts" / "lean_essai_d1a_v4" / "artefacts_r5_v4"
COMPILER = RACINE / "scripts" / "lean_essai_d1a_v11" / "compiler_comme_bac_v1.sh"
CHAINE = os.environ.get("LEAN_ESSAI_D1A_CHAINE", "")
avec_chaine = pytest.mark.skipif(not CHAINE, reason="chaîne épinglée absente : LEAN_ESSAI_D1A_CHAINE non posée (essai sauté, "
                                                    "pas réussi)")
ATT5 = json.loads((ART / "attendus-v5.json").read_text(encoding="utf-8"))
ATT6 = json.loads((ART / "attendus-v6.json").read_text(encoding="utf-8"))


def ligne_lean(nom, issue, detail):
    """Une ligne de tentative telle que `lean --json` l'écrit (message d'information échappé)."""
    return json.dumps({"severity": "information", "data": f"ISOLEMENT {nom} {issue} {detail}\n"}, ensure_ascii=False)


# ---- jugement des tentatives -----------------------------------------------------------------------------------------------

def test_tentatives_lues_dans_le_json_de_lean():
    texte = "\n".join([ligne_lean("a", "ECHEC", "no such file or directory (error code: 2)\n  file: /srv"),
                       ligne_lean("b", "REUSSI", "écrit")])
    assert E.tentatives(texte) == {"a": "ECHEC", "b": "REUSSI"}
    assert E.details_tentatives(texte)["a"] == "no such file or directory (error code: 2)"


def test_echec_sans_valeur_de_preuve():
    cas = {"tentatives": {"reseau-dns": "ECHEC", "reseau-curl-ip": "ECHEC"},
           "echecs_invalides": ["could not execute external process"]}
    sain = "\n".join([ligne_lean("reseau-dns", "ECHEC", "code 1 socket.gaierror: [Errno -3]"),
                      ligne_lean("reseau-curl-ip", "ECHEC", "code 7 curl: (7) Failed to connect")])
    assert E.juger_tentatives(cas, sain) == []
    artefact = "\n".join([ligne_lean("reseau-dns", "ECHEC", "code 255 could not execute external process 'python3'"),
                          ligne_lean("reseau-curl-ip", "ECHEC", "code 7 curl: (7) Failed to connect")])
    ecarts = E.juger_tentatives(cas, artefact)
    assert len(ecarts) == 1 and "reseau-dns" in ecarts[0] and "sans valeur de preuve" in ecarts[0]


def test_sain_vivant():
    cas = {"tentatives": {"ecriture-tmp": "REUSSI", "ecriture-item": "REUSSI"}}
    assert E.sain_vivant(cas, ligne_lean("ecriture-tmp", "REUSSI", "écrit") + "\n" + ligne_lean("ecriture-item", "REUSSI", "x"))
    assert not E.sain_vivant(cas, ligne_lean("ecriture-tmp", "REUSSI", "écrit"))
    assert not E.sain_vivant(cas, "")   # sortie du troisième essai : aucune tentative


def test_extrait_sonde_borne():
    long = "x" * (E.EXTRAIT_SONDE + 10)
    ex = E.extrait_sonde({"sortie_compilation": long, "erreurs_compilation": "e" * 5000, "compilation": {"code": 1}})
    assert len(ex["sortie_compilation_extrait"]) == E.EXTRAIT_SONDE and ex["sortie_compilation_tronquee"]
    assert len(ex["erreurs_compilation_extrait"]) == E.EXTRAIT_ERREURS and ex["erreurs_compilation_tronquees"]
    assert ex["sonde_muette"] and ex["code_compilation"] == 1
    assert not E.extrait_sonde({"sortie_compilation": ligne_lean("a", "ECHEC", "x")})["sonde_muette"]


def test_statuts_genres():
    rendus = [{"genre": "isolement Lean", "ok": False}, {"genre": "isolement Lean", "ok": True},
              {"genre": "Python", "ok": True}, {"genre": "limites", "ok": False}, {"genre": "limites", "ok": True}]
    assert E.statuts_genres(rendus, {"isolement Lean": False, "Python": True}) == {
        "isolement Lean": "épreuve morte", "Python": "conforme", "limites": "non conforme"}
    assert E.statuts_genres(rendus, {"isolement Lean": True})["isolement Lean"] == "non conforme"


# ---- épreuve entière avec un bac factice -------------------------------------------------------------------------------------

def res_lean(sortie="", code=0, incident=None):
    gardes = {g: {"ok": True, "motifs": []} for g in ("G-L1", "G-L2", "G-L3", "G-L3+", "G-L4", "G-L5", "G-L6", "G-L7", "G-L8")}
    return {"verdict": {"accepte_gardes": True, "gardes": gardes, "rejeu_ok": True, "enonces_imprimes": {},
                        "impressions": {}, "axiomes": {}},
            "sortie_compilation": sortie, "erreurs_compilation": "", "compilation": {"code": code}, "noyau": {},
            "isolement": True, "incident_bac": incident, "processus_residuels": [], "dossiers_restants": []}


def res_python(stdout="", code=0, incident=None):
    return {"execution": {"code": code, "duree_murale_s": 0.1}, "stdout": stdout, "stderr": "", "isolement": True,
            "incident_bac": incident, "processus_residuels": [], "dossiers_restants": []}


def sortie_attendue(cas):
    return "\n".join(ligne_lean(n, issue, "détail") for n, issue in cas["tentatives"].items())


class BacFactice:
    """Rend, pour chaque fichier, la sortie que l'attendu exige ; `casser` dit quels fichiers rendent une sortie vide (sonde
    morte, comme au troisième essai)."""
    casser: set = set()
    attendus: dict = {}

    def __init__(self, cfg, *a, **k):
        self.cfg = cfg

    def _cas(self, source):
        for groupe, liste in self.attendus.items():
            if isinstance(liste, list):
                for c in liste:
                    if isinstance(c, dict) and (ART / c["fichier"]).read_text(encoding="utf-8") == source:
                        return groupe, c
        raise AssertionError("source inconnue")

    def verifier_lean(self, item, source, m):
        groupe, c = self._cas(source)
        if c["fichier"] in self.casser:
            return res_lean("", code=1)
        if groupe == "isolement_lean":
            return res_lean(sortie_attendue(c))
        if groupe == "limites_lean":
            return res_lean("", code=1, incident="mémoire")
        r = res_lean()
        r["verdict"]["accepte_gardes"] = c["accepte"]
        for g in c.get("echecs", []):
            r["verdict"]["gardes"][g] = {"ok": False, "motifs": ["m"]}
        if "rejeu" in c:
            r["verdict"]["rejeu_ok"] = c["rejeu"]
        for nom, morceaux in c.get("enonce_contient", {}).items():
            r["verdict"]["enonces_imprimes"][nom] = " ".join(morceaux)
        for nom, morceaux in c.get("impression_contient", {}).items():
            r["verdict"]["impressions"][nom] = " ".join(morceaux)
        for nom, ax in c.get("axiomes_contient", {}).items():
            r["verdict"]["axiomes"][nom] = ax
        r["sortie_compilation"] = " ".join(c.get("sortie_agent_contient", []))
        return r

    def executer_python(self, item, code):
        groupe, c = self._cas(code)
        if c["fichier"] in self.casser:
            return res_python("", code=1)
        out = " ".join(c.get("stdout_contient", []))
        if "tentatives" in c:
            out += "\n" + "\n".join(f"ISOLEMENT {n} {i} détail" for n, i in c["tentatives"].items())
        code_ = c.get("code", 1 if c.get("code_non_nul") else 0)
        return res_python(out, code_, c.get("incident_attendu"))


@pytest.fixture
def epreuve_factice(tmp_path, monkeypatch):
    monkeypatch.setattr(E, "LEURRE", tmp_path / "leurre" / "leurre-v1.txt")
    monkeypatch.setattr(E, "manifeste", lambda racines=None: "m")
    monkeypatch.setattr(E, "PIEGES_HOTE", ())
    monkeypatch.setattr(E.subprocess, "run", lambda *a, **k: subprocess.CompletedProcess(a, 0, "", ""))
    monkeypatch.setattr(E.X, "Bac", BacFactice)
    BacFactice.attendus = ATT6
    for n in ("items", "sorties"):
        (tmp_path / n).mkdir()
    cfg = E.X.Config(lean="/l", lean_path="/p", verificateur_sha256="x", mode="bac", racine_items=tmp_path / "items",
                     racine_sorties=tmp_path / "sorties")

    def jouer(casser=()):
        BacFactice.casser = set(casser)
        return E.epreuve(cfg, ART)
    return jouer


def test_epreuve_cas_sain_conforme(epreuve_factice):
    r = epreuve_factice()
    assert r["statut"] == "conforme" and r["conforme"], [c for c in r["cas"] if not c["ok"]]
    assert r["sains"] == {"isolement Lean": True, "Python": True}
    iso = [c for c in r["cas"] if c["genre"] == "isolement Lean"]
    assert len(iso) == 5 and all("sortie_compilation_extrait" in c and not c["sonde_muette"] for c in iso)
    assert [c["genre"] for c in r["cas"]].count("limites Lean") == 1
    assert len(r["cas"]) == 21 + 5 + 4 + 5 + 1


def test_epreuve_morte_quand_le_sain_ne_rend_rien(epreuve_factice):
    """Artefact R5 : le troisième essai rejoué (les cinq sondes Lean muettes, cas sain compris)."""
    r = epreuve_factice(casser={c["fichier"] for c in ATT6["isolement_lean"]})
    assert r["statut"] == "épreuve morte" and not r["conforme"] and r["genres_morts"] == ["isolement Lean"]
    assert r["genres"]["isolement Lean"] == "épreuve morte" and r["genres"]["Python"] == "conforme"
    assert all(c["sonde_muette"] for c in r["cas"] if c["genre"] == "isolement Lean")


def test_non_conforme_quand_le_sain_vit_et_un_artefact_echoue(epreuve_factice):
    r = epreuve_factice(casser={"iso_lecture_v3.lean"})
    assert r["statut"] == "non conforme" and r["genres"]["isolement Lean"] == "non conforme" and not r["genres_morts"]


def test_epreuve_morte_python(epreuve_factice):
    r = epreuve_factice(casser={"iso_persistance_ecrire_v1.py"})
    assert r["statut"] == "épreuve morte" and r["genres_morts"] == ["Python"]


def test_code_de_sortie_epreuve_morte(monkeypatch):
    monkeypatch.setattr(E.X, "charger_config", lambda *a, **k: None)
    for statut, conforme, code in (("épreuve morte", False, 3), ("non conforme", False, 1), ("conforme", True, 0)):
        monkeypatch.setattr(E, "epreuve", lambda cfg, art, s=statut, c=conforme: {"statut": s, "conforme": c})
        assert E.main(["epreuve"]) == code


def test_juger_limite_lean():
    cas = ATT6["limites_lean"][0]
    assert E.juger_limite_lean(cas, res_lean("", code=1, incident="mémoire")) == []
    assert E.juger_limite_lean(cas, res_lean("", code=1, incident=None))                  # pas classé « mémoire »
    assert E.juger_limite_lean(cas, res_lean(ligne_lean("x", "ECHEC", "") + "ALLOUE 1", code=1, incident="mémoire"))
    assert E.juger_limite_lean(cas, res_lean("", code=0, incident="mémoire"))


# ---- artefacts et attendus ---------------------------------------------------------------------------------------------------

def test_sondes_v3_egales_aux_v2_plus_to_string():
    for c5, c6 in zip(ATT5["isolement_lean"], ATT6["isolement_lean"]):
        v2 = (ART / c5["fichier"]).read_text(encoding="utf-8")
        v3 = (ART / c6["fichier"]).read_text(encoding="utf-8")
        l2, l3 = v2.splitlines(), v3.splitlines()
        assert l3[0] == l2[0] and l3[1].startswith("-- v3 ") and l3[2].startswith("-- `String.take`")
        corps2, corps3 = l2[1:], l3[3:]
        assert len(corps2) == len(corps3)
        for a, b in zip(corps2, corps3):
            assert re.sub(r"\(([\w.]+)\.take (\d+)\)\.toString", r"(\1.take \2)", b) == a
        assert ".take " in v3 and all(re.search(r"\.take \d+\)\.toString", x) for x in corps3 if ".take " in x)


def test_attendus_v6_changements_declares():
    assert ATT6["version"] == "attendus-v6"
    for g in ("noyau", "observations_noyau", "lean"):
        assert ATT6[g] == ATT5[g]
    assert [c["tentatives"] for c in ATT6["isolement_lean"]] == [c["tentatives"] for c in ATT5["isolement_lean"]]
    assert [c["nom"] for c in ATT6["isolement_lean"] if c.get("sain")] == [
        "persistance : écriture dans son propre espace (cas sain)"]
    assert [c["nom"] for c in ATT6["python"] if c.get("sain")] == [
        "persistance Python : écriture dans son propre espace (cas sain)"]
    assert ATT6["limites_python"][:4] == ATT5["limites_python"]
    nouveau = ATT6["limites_python"][4]
    assert nouveau["fichier"] == "limite_code137_v1.py" and nouveau["code"] == 137 and nouveau["incident_attendu"] is None
    assert ATT6["limites_lean"][0]["incident_attendu"] == "mémoire"
    for groupe in ("isolement_lean", "python", "limites_python", "limites_lean", "lean", "noyau"):
        for c in ATT6[groupe]:
            assert (ART / c["fichier"]).is_file(), c["fichier"]


def test_artefact_memoire_lean_sans_mathlib_et_temoin():
    t = (ART / "limite_memoire_lean_v1.lean").read_text(encoding="utf-8")
    assert "import" not in t and "Array.replicate 200000000" in t and "ALLOUE" in t


# ---- avec la chaîne épinglée --------------------------------------------------------------------------------------------------

def chaine():
    d = json.loads(Path(CHAINE).read_text(encoding="utf-8"))
    return d["lean"], d["lean_path"]


def bac_a_sable_possible():
    if os.geteuid() != 0 or shutil.which("unshare") is None:
        return False
    return subprocess.run(["unshare", "--mount", "--net", "true"], capture_output=True).returncode == 0



sans_bac_a_sable = pytest.mark.skipif(not bac_a_sable_possible(),
                                      reason="bac à sable de montage impossible (root et unshare exigés) : sauté")


def compiler_dans_le_bac_a_sable(fichier, tmp_path):
    """Compile comme le bac (même commande, même environnement), sans que les tentatives touchent l'hôte."""
    lean, lp = chaine()
    racine_chaine = os.path.commonpath([lean, lp.split(":")[0]])
    sortie = tmp_path / "sortie"
    sortie.mkdir()
    p = subprocess.run(["bash", str(COMPILER), racine_chaine, lean, lp, str(fichier), str(sortie)],
                       capture_output=True, text=True, timeout=300)
    return p.returncode, (sortie / "compilation.out").read_text(encoding="utf-8")


@avec_chaine
@sans_bac_a_sable
@pytest.mark.parametrize("cas", ATT5["isolement_lean"], ids=lambda c: c["fichier"])
def test_sondes_v2_ne_compilent_pas_cause(cas, tmp_path):
    """Cause établie : l'élaboration de `tenter` échoue (String.Slice), chaque `#eval` est abandonné ; code 1, aucune tentative."""
    code, out = compiler_dans_le_bac_a_sable(ART / cas["fichier"], tmp_path)
    assert code == 1
    assert "String.Slice" in out and "but is expected to have type" in out and "ISOLEMENT" not in out
    assert "depends on the 'sorry' axiom" in out


@avec_chaine
@sans_bac_a_sable
@pytest.mark.parametrize("cas", ATT6["isolement_lean"], ids=lambda c: c["fichier"])
def test_sondes_v3_rendent_leurs_tentatives(cas, tmp_path):
    code, out = compiler_dans_le_bac_a_sable(ART / cas["fichier"], tmp_path)
    assert code == 0, out[:2000]
    assert set(E.tentatives(out)) == set(cas["tentatives"])
    if cas.get("sain"):
        assert E.sain_vivant(cas, out)
