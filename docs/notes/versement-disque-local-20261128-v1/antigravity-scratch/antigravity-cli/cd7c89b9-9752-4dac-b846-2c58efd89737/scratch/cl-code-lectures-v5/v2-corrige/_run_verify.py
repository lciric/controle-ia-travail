"""In-memory verification harness for CLN-01..CLN-07 and autonomous unit tests."""
from __future__ import annotations

import hashlib
import json
import math
import os
import sys
import tempfile
import types
from pathlib import Path

import numpy as np

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

# Minimal in-memory adapters for unavailable optional Windows packages (scipy.stats.rankdata, torch)
if "scipy" not in sys.modules:
    scipy_mod = types.ModuleType("scipy")
    stats_mod = types.ModuleType("scipy.stats")

    def rankdata(a, method="average"):
        arr = np.asarray(a, dtype=float)
        n = len(arr)
        order = np.argsort(arr, kind="mergesort")
        s = arr[order]
        ranks = np.empty(n, dtype=float)
        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1
            r = 0.5 * (i + j) + 1.0
            ranks[order[i:j + 1]] = r
            i = j + 1
        return ranks

    stats_mod.rankdata = rankdata
    scipy_mod.stats = stats_mod
    sys.modules["scipy"] = scipy_mod
    sys.modules["scipy.stats"] = stats_mod

if "torch" not in sys.modules:
    torch_mod = types.ModuleType("torch")
    nn_mod = types.ModuleType("torch.nn")
    nn_mod.Module = object
    torch_mod.nn = nn_mod
    torch_mod.Tensor = object
    sys.modules["torch"] = torch_mod
    sys.modules["torch.nn"] = nn_mod

import pytest  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.iib import configuration_lectures_v5 as cl  # noqa: E402
from controle_ia.iib import configuration_v5 as cf5  # noqa: E402
from controle_ia.iib import entrees_lectures_v5 as ev  # noqa: E402
from controle_ia.iib import lectures_v5 as lx  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
import lecture_iib_2_diffusion_v5 as s2  # noqa: E402
import lecture_iib_audit_r4_v5 as sa  # noqa: E402


def verify_cln_reproducers():
    print("=== 1. Spec & 15 frozen modules ===")
    assert cl.exiger_specification() == cl.SPECIFICATION["sha256"]
    mods = cl.exiger_modules_d_origine()
    assert all(mods[k] == v for k, v in cl.MODULES_D_ORIGINE.items())
    print("OK spec & 15 frozen modules verified")

    print("=== 2. CLN-01..CLN-07 exact reproducers ===")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        # Setup fake registres
        (tmp / "registres").mkdir()
        (tmp / "prereg").mkdir()
        (tmp / "registres" / "go.md").write_text("| GO-2026-11-24-37 | ok |\n", encoding="utf-8")
        reg_r = ev.Racines(registres=tmp)
        l1_ok = {"sha256": "f" * 64, "contenu": {"audit_R4": {"declenche": True}}}

        # CLN-01
        for bad_go in ("GO-2026-11-24-370", "XGO-2026-11-24-37-bis", "XGO-2026-11-24-37", "GO-2026-11-24-37-bis"):
            lignes = [
                f"| R-1 | `{'f' * 64}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT |",
                f"| R-2 | `{'f' * 64}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE {bad_go} |",
            ]
            try:
                lx.exiger_audit_consigne(l1_ok, lignes, reg_r)
                raise AssertionError(f"CLN-01 failed to reject {bad_go}")
            except GardeArret:
                pass
        # Positive check with backticks/parentheses
        for good_go in ("GO-2026-11-24-37", "`GO-2026-11-24-37`", "(GO-2026-11-24-37)"):
            lignes = [
                f"| R-1 | `{'f' * 64}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT |",
                f"| R-2 | `{'f' * 64}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE {good_go} |",
            ]
            res = lx.exiger_audit_consigne(l1_ok, lignes, reg_r)
            assert res["accord"] == "GO-2026-11-24-37"
        print("OK CLN-01")

        # CLN-02 (static AST check that ev.decoder is called inside Try and before any print in lecture_iib_audit_r4_v5.py)
        import ast
        tree = ast.parse((ROOT / "scripts" / "lecture_iib_audit_r4_v5.py").read_text(encoding="utf-8"))
        main_fn = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main"][0]
        try_node = [n for n in main_fn.body if isinstance(n, ast.Try)][0]
        outside_calls = [
            ast.dump(c) for stmt in main_fn.body[main_fn.body.index(try_node) + 1:]
            for c in ast.walk(stmt) if isinstance(c, ast.Attribute) and c.attr == "decoder"
        ]
        inside_calls = [
            ast.dump(c) for stmt in try_node.body
            for c in ast.walk(stmt) if isinstance(c, ast.Attribute) and c.attr == "decoder"
        ]
        assert not outside_calls and len(inside_calls) == 1
        print("OK CLN-02 (AST + runtime test in pytest)")

        # CLN-03
        lignes_t0 = []
        for i, k in enumerate(cl.SCELLEMENTS_SONDES):
            p = tmp / "prereg" / f"sondes-{i}.md"
            p.write_text(f"t{i}\n", encoding="utf-8")
            sha = sceller(p)
            h = ["2026-11-20T10:00:00Z", "2026-02-30T10:00:00Z", "2026-11-22T10:00:00Z"][i]
            lignes_t0.append(f"| {k} | {h} | prereg/sondes-{i}.md | {sha} |")
        rs = tmp / "registres" / "sondes-iib-v1.md"
        rs.write_text("\n".join(lignes_t0) + "\n", encoding="utf-8")
        try:
            ev.exiger_ordre_du_temps(rs, "jouet")
            raise AssertionError("CLN-03 failed")
        except GardeArret as e:
            assert "heure illisible" in str(e)
        print("OK CLN-03")

        # CLN-04
        etr = tmp / "etr"
        p1 = etr / "diag" / "20991231-000021-iib-course-jouet" / cl.NOM_1
        p1.parent.mkdir(parents=True)
        p1.write_text(json.dumps({"audit_R4": {"declenche": False}}) + "\n", encoding="utf-8")
        sceller(p1)
        assert s2.main(["--racine", str(etr), "--run-id", "20991231-000021-iib-course-jouet",
                        "--etalonnage", "20991231-000020-iib-jouet",
                        "--registre-decisions", str(tmp / "registres" / "decisions.md"),
                        "--registre-sondes", str(rs), "--jetoniseur", str(tmp / "jet")]) == 1
        assert sa.main(["--racine", str(etr), "--run-id", "20991231-000021-iib-course-jouet",
                        "--etalonnage", "20991231-000020-iib-jouet",
                        "--jetoniseur", str(tmp / "jet")]) == 1
        print("OK CLN-04")

        # CLN-05
        for bad_d in (None, "false", 0, 1):
            try:
                lx.exiger_audit_consigne({"sha256": "f" * 64, "contenu": {"audit_R4": {"declenche": bad_d}}}, [], reg_r)
                raise AssertionError(f"CLN-05 failed for {bad_d!r}")
            except GardeArret:
                pass
        res_iso = lx.exiger_audit_consigne(
            l1_ok, [f"| R-2 | `{'f' * 64}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE GO-2026-11-24-37 |"], reg_r
        )
        assert res_iso["accord"] == "GO-2026-11-24-37" and res_iso["accords"] == ["GO-2026-11-24-37"]
        print("OK CLN-05")

        # CLN-06
        e_p = {"oracle": "N", "branches_citees": {"chemin": "x", "sha256": "y"},
               "branches": {"oracles": {"N": {"grandeurs": {"EMD": -0.05, "exces_moyen_honnete": 0.02}}}}}
        x_p = {"exces_moyen_par_action_de_tous_les_episodes": 0.25, "exces_moyen_par_action_des_acceptes": 0.5}
        for bad_emd in (-0.05, float("nan"), float("inf")):
            e_p["branches"]["oracles"]["N"]["grandeurs"]["EMD"] = bad_emd
            try:
                lx.puissance(e_p, x_p)
                raise AssertionError(f"CLN-06 failed for EMD={bad_emd}")
            except GardeArret:
                pass
        e_p["branches"]["oracles"]["N"]["grandeurs"]["EMD"] = 0.05
        for bad_h in (True, "0.02", float("nan")):
            e_p["branches"]["oracles"]["N"]["grandeurs"]["exces_moyen_honnete"] = bad_h
            try:
                lx.puissance(e_p, x_p)
                raise AssertionError(f"CLN-06 failed for honnete={bad_h}")
            except GardeArret:
                pass
        print("OK CLN-06")

        # CLN-07
        assert ev._egal_types_stricts([[1, 0]], [[True, 0]]) is False
        assert ev._egal_types_stricts([[1, 0]], [[1.0, 0]]) is False
        try:
            ev.exiger_controle_premier_cout(None)
            raise AssertionError("CLN-07 cpc None failed")
        except GardeArret:
            pass
        print("OK CLN-07")


def run_autonomous_pytest():
    print("=== 3. Autonomous pytest suite ===")
    # Select all tests in tests/test_lectures_iib_v5_v1.py that do not depend on `monde`, `lu`, `copie`, `dossier_jetoniseur`, or `test_fils_de_calcul`
    test_file = str(ROOT / "tests" / "test_lectures_iib_v5_v1.py")

    class Plugin:
        def pytest_collection_modifyitems(self, items):
            kept = []
            for item in items:
                fnames = set(getattr(item, "fixturenames", ()))
                if fnames & {"monde", "lu", "copie", "dossier_jetoniseur"} or item.name == "test_fils_de_calcul":
                    continue
                kept.append(item)
            items[:] = kept

    rc = pytest.main(["-v", "-p", "no:cacheprovider", f"--rootdir={ROOT}", "-o", "testpaths=tests", test_file], plugins=[Plugin()])
    if rc != 0:
        sys.exit(rc)


if __name__ == "__main__":
    os.chdir(ROOT)
    verify_cln_reproducers()
    run_autonomous_pytest()
    print("=== 4. SHA-256 of the 7 code/test files ===")
    targets = [
        "scripts/lecture_iib_1_dommage_v5.py",
        "scripts/lecture_iib_2_diffusion_v5.py",
        "scripts/lecture_iib_audit_r4_v5.py",
        "src/controle_ia/iib/configuration_lectures_v5.py",
        "src/controle_ia/iib/entrees_lectures_v5.py",
        "src/controle_ia/iib/lectures_v5.py",
        "tests/test_lectures_iib_v5_v1.py",
    ]
    for rel in targets:
        p = ROOT / rel
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        print(f"{h}  {rel}  ({p.stat().st_size} octets)")
