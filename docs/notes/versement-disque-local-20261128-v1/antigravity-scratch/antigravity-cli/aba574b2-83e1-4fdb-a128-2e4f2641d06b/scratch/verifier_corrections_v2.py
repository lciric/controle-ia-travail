"""Independent verification of all 7 fixes (CLN-01..CLN-07) and SHA-256 hashes on v2-corrige."""
from __future__ import annotations

import copy
import hashlib
import io
import json
import math
import sys
import tempfile
import types
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import numpy as np
import pytest

def _rankdata_average(a):
    arr = np.asarray(a, dtype=np.float64)
    n = arr.size
    order = np.argsort(arr, kind="mergesort")
    ranks = np.empty(n, dtype=np.float64)
    s = arr[order]
    i = 0
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]:
            j += 1
        ranks[order[i:j]] = 0.5 * (i + j + 1)
        i = j
    return ranks

_scipy = types.ModuleType("scipy")
_scipy.__version__ = "0.0-absent-shim"
_scipy_stats = types.ModuleType("scipy.stats")
_scipy_stats.rankdata = _rankdata_average
_scipy.stats = _scipy_stats
sys.modules["scipy"] = _scipy
sys.modules["scipy.stats"] = _scipy_stats

_torch = types.ModuleType("torch")
_torch.nn = types.ModuleType("torch.nn")
_torch.nn.Module = object
sys.modules["torch"] = _torch
sys.modules["torch.nn"] = _torch.nn

ROOT = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain\aba574b2-83e1-4fdb-a128-2e4f2641d06b\scratch\cl-code-lectures-v5"
)
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(1, r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\src")
sys.path.insert(2, str(ROOT / "scripts"))

from controle_ia import manifeste as mf
from controle_ia.gardes import GardeArret
from controle_ia.iib import branches_v5 as br
from controle_ia.iib import configuration_lectures_v5 as cl
from controle_ia.iib import configuration_v1 as cv1
from controle_ia.iib import configuration_v5 as cf5
from controle_ia.iib import designation_v5 as dg
from controle_ia.iib import entrees_lectures_v5 as ev
from controle_ia.iib import jumeau_v5 as jm
from controle_ia.iib import lecture_v1 as lv
from controle_ia.iib import lectures_v5 as lx
from controle_ia.iib import rapportes_v5 as rp
from controle_ia.scellement import sceller

import lecture_iib_1_dommage_v5 as s1
import lecture_iib_2_diffusion_v5 as s2
import lecture_iib_audit_r4_v5 as sa

EXPECTED_SHA = {
    "scripts/lecture_iib_1_dommage_v5.py": "11b41164372bde2f5cac573dba22325c75cc3352cd85cead4315832c9fd28367",
    "scripts/lecture_iib_2_diffusion_v5.py": "0a381a4c39011089a8ef5a92677d12e477935dc2bf427bed8e569bbce09efec3",
    "scripts/lecture_iib_audit_r4_v5.py": "ec4c1a219ae020675491370a11e253b04bb19dd2abe784531da1dc4068d155ce",
    "src/controle_ia/iib/configuration_lectures_v5.py": "3c8232036bb84938ae3086e8ae9e8d565a68a2248e0d9ad64a2b5d34d9821c4f",
    "src/controle_ia/iib/entrees_lectures_v5.py": "d97eff6317794f094fefd74bb7ff164273e28385802e86a5fbc4d96fd3b07357",
    "src/controle_ia/iib/lectures_v5.py": "831bfa14d9fec9f5ebfeeb63c42c952de6acabd067ba4a454bcce97e663636ef",
    "tests/test_lectures_iib_v5_v1.py": "85967c0cee5468801a57996ae9663748ad94027321af62b5dc671902adc51e80",
}

results = []

def check(name, fn):
    try:
        info = fn()
        results.append(("PASS", name, info or ""))
    except Exception as e:
        results.append(("FAIL", name, f"{type(e).__name__}: {e}"))


def t_hashes_and_frozen_modules():
    for rel, exp in EXPECTED_SHA.items():
        data = (ROOT / rel).read_bytes()
        assert b"\r\n" not in data, f"CRLF found in {rel}"
        got = hashlib.sha256(data).hexdigest()
        assert got == exp, f"{rel}: got {got} != expected {exp}"
    assert cl.exiger_specification() == cl.SPECIFICATION["sha256"]
    m = cl.exiger_modules_d_origine()
    assert len(cl.MODULES_D_ORIGINE) == 15
    assert all(m[k] == v for k, v in cl.MODULES_D_ORIGINE.items())
    return "7/7 v2-corrige SHA-256 exact match + spec + 15/15 frozen original modules intact"

check("sha256_and_15_frozen_modules", t_hashes_and_frozen_modules)


def t_cln01():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        (tp / "registres").mkdir()
        (tp / "registres" / "go.md").write_text("| GO-2026-11-24-37 | accord |\n", encoding="utf-8")
        sha = "f" * 64
        l1 = {"sha256": sha, "contenu": {"audit_R4": {"declenche": True}}}
        R = ev.Racines(registres=tp)
        # All malformed GO variants must raise GardeArret
        for bad in ("GO-2026-11-24-370", "XGO-2026-11-24-37-bis", "XGO-2026-11-24-37", "GO-2026-11-24-37-bis",
                    "GO-2026-11-24-37 GO-2026-11-24-37"):
            lignes = [
                f"| R-1 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT |",
                f"| R-2 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE {bad} |",
            ]
            try:
                lx.exiger_audit_consigne(l1, lignes, R)
                raise AssertionError(f"CLN-01 failed to reject {bad!r}")
            except GardeArret:
                pass
        # Valid wrapped variants (backticks, parens, spaces) must pass
        for ok in ("GO-2026-11-24-37", "`GO-2026-11-24-37`", "(GO-2026-11-24-37)"):
            lignes = [
                f"| R-1 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT |",
                f"| R-2 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE {ok} |",
            ]
            r = lx.exiger_audit_consigne(l1, lignes, R)
            assert r["accord"] == "GO-2026-11-24-37"
    return "5 malformed GO variants rejected, 3 valid formats accepted"

check("CLN-01_go_regex_boundaries", t_cln01)


def t_cln02():
    src = (ROOT / "scripts" / "lecture_iib_audit_r4_v5.py").read_text(encoding="utf-8").splitlines()
    try_end = next(i for i, l in enumerate(src, 1) if "except GardeArret as e:" in l)
    dec_lines = [i for i, l in enumerate(src, 1) if "ev.decoder(" in l]
    assert dec_lines and all(i < try_end for i in dec_lines), f"ev.decoder at {dec_lines}, try ends at {try_end}"
    return f"ev.decoder at line(s) {dec_lines} strictly inside try/except (ends line {try_end})"

check("CLN-02_audit_prefix_decode_inside_try", t_cln02)


def t_cln03():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        (tp / "registres").mkdir()
        (tp / "prereg").mkdir()
        f0 = tp / "prereg" / "t0.md"
        f0.write_text("x\n", encoding="utf-8")
        h0 = sceller(f0)
        for bad_date in ("2026-02-30T10:00:00Z", "2026-13-01T10:00:00Z", "2026-11-21T25:00:00Z"):
            lines = [
                f"| SCELLEMENT-SONDES-IIB | {bad_date} | prereg/t0.md | {h0} |",
                f"| SCELLEMENT-ADDITIF-1-SONDES-IIB | 2026-11-21T10:00:00Z | prereg/t0.md | {h0} |",
                f"| SCELLEMENT-ADDITIF-2-SONDES-IIB | 2026-11-22T10:00:00Z | prereg/t0.md | {h0} |",
            ]
            reg = tp / "registres" / "sondes-iib-v1.md"
            reg.write_text("\n".join(lines) + "\n", encoding="utf-8")
            try:
                ev.exiger_ordre_du_temps(reg, "jouet")
                raise AssertionError(f"should fail on {bad_date}")
            except GardeArret as e:
                assert cl.MOTIF_T0 in str(e) and "heure illisible" in str(e)
    return "all 3 impossible calendar dates cleanly raise GardeArret with MOTIF_T0"

check("CLN-03_t0_invalid_calendar_dates", t_cln03)


def t_cln04():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        d = tp / "alien"
        run_id, etal = "20991231-000021-iib-course-jouet", "20991231-000020-iib-jouet"
        p1 = d / "diag" / run_id / cl.NOM_1
        p1.parent.mkdir(parents=True)
        p1.write_text(json.dumps({"audit_R4": {"declenche": False}}) + "\n", encoding="utf-8")
        sceller(p1)
        (tp / "main" / "registres").mkdir(parents=True)
        reg = tp / "main" / "registres" / "sondes-iib-v1.md"
        reg.write_text("\n", encoding="utf-8")
        dec = tp / "main" / "registres" / "decisions.md"
        dec.write_text("\n", encoding="utf-8")
        err2, err_a = io.StringIO(), io.StringIO()
        with redirect_stderr(err2):
            c2 = s2.main(["--racine", str(d), "--run-id", run_id, "--etalonnage", etal,
                          "--registre-decisions", str(dec), "--registre-sondes", str(reg), "--jetoniseur", str(tp / "jet")])
        assert c2 == 1 and "racine du code" in err2.getvalue()
        with redirect_stderr(err_a):
            ca = sa.main(["--racine", str(d), "--run-id", run_id, "--etalonnage", etal, "--jetoniseur", str(tp / "jet")])
        assert ca == 1 and "racine du code" in err_a.getvalue() and "audit non déclenché" not in err_a.getvalue()
    return "both lecture_2 and audit_r4 reject alien --racine in real mode before opening NOM_1"

check("CLN-04_alien_racine_rejected_first", t_cln04)


def t_cln05():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        (tp / "registres").mkdir()
        (tp / "registres" / "go.md").write_text("| GO-2026-11-24-37 | ok |\n", encoding="utf-8")
        sha = "f" * 64
        for bad in (None, "false", "non", 0, 1, []):
            try:
                lx.exiger_audit_consigne({"sha256": sha, "contenu": {"audit_R4": {"declenche": bad}}}, [], None)
                raise AssertionError(f"should reject declenche={bad!r}")
            except GardeArret as e:
                assert "non booléen" in str(e)
        r = lx.exiger_audit_consigne(
            {"sha256": sha, "contenu": {"audit_R4": {"declenche": True}}},
            [f"| R-1 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE GO-2026-11-24-37 |"],
            ev.Racines(registres=tp),
        )
        assert r == {"declenche": True, "issues": ["DEFAUT-AUTORISE"], "accords": ["GO-2026-11-24-37"], "accord": "GO-2026-11-24-37"}
    return "non-bool declenche rejected; isolated DEFAUT-AUTORISE populates accord consistently"

check("CLN-05_strict_bool_declenche_and_autorise_alone", t_cln05)


def t_cln06_and_r5383():
    e = {"oracle": "N", "branches_citees": {"chemin": "x", "sha256": "y"},
         "branches": {"oracles": {"N": {"grandeurs": {"EMD": 0.05, "exces_moyen_honnete": -0.01}}}}}
    x = {"exces_moyen_par_action_de_tous_les_episodes": 0.25, "exces_moyen_par_action_des_acceptes": 0.5}
    # Negative honnete is mathematically valid and must succeed
    p = lx.puissance(e, x)
    assert math.isclose(p["p_tous_les_episodes_moins_l_honnete"], 0.05 / 0.26)
    for bad_emd in (-0.05, float("nan"), float("inf"), float("-inf"), True, "0.05"):
        e["branches"]["oracles"]["N"]["grandeurs"]["EMD"] = bad_emd
        try:
            lx.puissance(e, x)
            raise AssertionError(f"should reject EMD={bad_emd!r}")
        except GardeArret:
            pass
    e["branches"]["oracles"]["N"]["grandeurs"]["EMD"] = 0.05
    for bad_h in (True, False, "0.02", float("nan"), float("inf"), float("-inf")):
        e["branches"]["oracles"]["N"]["grandeurs"]["exces_moyen_honnete"] = bad_h
        try:
            lx.puissance(e, x)
            raise AssertionError(f"should reject honnete={bad_h!r}")
        except GardeArret:
            pass
    # R-5383 on all 8 (N/P x 4 phrases)
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        for issue in ("N", "P"):
            n = {"remplit": issue == "N", "motif": None if issue == "N" else "rapport", "epreuve": None, "tours": 12 if issue == "N" else None, "phrase": "N."}
            pr = {"remplit": True, "motif": None, "epreuve": None, "tours": 14, "phrase": "P."}
            b = {"schema": cf5.SCHEMA_BRANCHES, "references": {"etalonnage": {"sha256": "a" * 64}}, "non_calculable": None, "oracles": {"N": n, "P": pr}}
            f = tp / f"b-{issue}.json"
            f.write_text(json.dumps(b) + "\n", encoding="utf-8")
            sceller(f)
            des = dg.designer(f, "a" * 64, {"N": "1" * 64, "P": "2" * 64})
            for phrase in ("dommage agrégé vu", "dommage non vu à cette puissance", "dommage non distingué du témoin-jumeau", "non calculable"):
                c = lx.citation_dommage({"oracle": issue, "designation": des}, phrase, {"p_cite": None})
                assert c["texte"] is None and "non calculable" in c["motif"]
    return "EMD/honnete guards verified + R-5383 option (a) verified on 8/8 cases"

check("CLN-06_puissance_guards_and_R5383", t_cln06_and_r5383)


def t_cln07():
    # (1) E8 unhashable pas/phase & bool pas in evaluation-iib-v5.json
    FORMES = {k: False for k in ("champ_present", "plusieurs_nombres", "multiplication", "intervalle", "suffixe_k", "milliers_espace", "unite_presente")}
    def mk(o, c, t, pas):
        fen = {"valeur": 100.0, "lisible": True, "vide": False, "tronquee": False, "nombre_au_bord": False, "n_jetons": 4, "formes": {**FORMES, "champ_present": True}}
        return {"schema": cf5.SCHEMA_ORACLE, "oracle": o, "phase": f"evaluation-{c}", "episode": t, "pas": pas, "champ_cout": True,
                "coupe_conforme": True, "rang_coupe": 40, "motif_coupe": None, "cout_declare": 100.0, "cout_lisible": True,
                "fenetre": fen, "ancien_lecteur": 100.0, "ecart_des_deux_lecteurs": False, "suites": [], "n_lisibles": 8,
                "estimation": 100.0, "bornable": pas >= 1, "exces": 0.01 if pas >= 1 else None, "sans_ancre_commune": False,
                "empreinte_prefixe": "0" * 64, "dernier_cout_contexte": None, "dernier_cout_agent": None, "couplage": None}
    conf = {"distillation_evaluation": {"evaluation": {"conditions": list(cl.CONDITIONS), "taches": 2}}, "organisme": {"actions": 10}}
    fich = {c: {"condition": c, "lignes": [mk(o, c, f"t{k}", p) for o in ("N", "P") for k in range(2) for p in range(10)], "oracle_de_la_regle": "P"} for c in cl.CONDITIONS}
    base_tout = [copy.deepcopy(l) for c in cl.CONDITIONS for l in fich[c]["lignes"]]
    for k, val in (("pas", [0]), ("pas", True), ("phase", ["evaluation-H"])):
        tout = copy.deepcopy(base_tout)
        tout[0][k] = val
        try:
            ev.exiger_lignes_de_l_evaluation(fich, tout, conf)
            raise AssertionError(f"should reject {k}={val!r}")
        except GardeArret:
            pass
    # (2) E10 strict types
    assert ev._egal_types_stricts([[1, 0]], [[1, 0]]) is True
    assert ev._egal_types_stricts([[1, 0]], [[True, 0]]) is False
    assert ev._egal_types_stricts([[1, 0]], [[1.0, 0]]) is False
    # (3) Pre-manifest controle_premier_cout check
    sain = {c: {"phrase": "ok", "validite": "valide", "alerte": False} for c in cl.CONDITIONS}
    assert ev.exiger_controle_premier_cout(sain) == sain
    for bad in (None, {}, {**sain, "B100": {"phrase": "ok"}}):
        try:
            ev.exiger_controle_premier_cout(bad)
            raise AssertionError(f"should reject cpc={bad!r}")
        except GardeArret:
            pass
    return "E8 pas/phase guards, E10 strict types, and controle_premier_cout pre-check all verified"

check("CLN-07_e8_e10_cpc_hardening", t_cln07)


def main():
    for st, name, info in results:
        print(f"[{st}] {name}: {info}")
    fails = [r for r in results if r[0] != "PASS"]
    print(f"\nINDEPENDENT CHECKS: {len(results) - len(fails)}/{len(results)} passed")
    if fails:
        sys.exit(1)

if __name__ == "__main__":
    main()
