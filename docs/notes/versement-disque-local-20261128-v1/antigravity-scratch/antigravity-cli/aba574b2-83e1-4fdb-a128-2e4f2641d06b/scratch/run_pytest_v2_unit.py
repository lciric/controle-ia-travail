"""Run all standalone unit tests of v2-corrige test_lectures_iib_v5_v1.py in sandbox (zero file edits)."""
import os
import shutil
import sys
import types
from pathlib import Path
import numpy as np
import pytest

os.link = shutil.copy2

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

EXCLUDED_FIXTURES = {"monde", "copie", "lu", "dossier_jetoniseur"}

class _FilterPlugin:
    def pytest_collection_modifyitems(self, session, config, items):
        total = len(items)
        kept, deselected = [], []
        for it in items:
            fnames = set(getattr(it, "fixturenames", ()))
            if (fnames & EXCLUDED_FIXTURES) or it.name == "test_fils_de_calcul":
                deselected.append(it)
            else:
                kept.append(it)
        print(f"\nCOLLECTED_TOTAL={total} STANDALONE_KEPT={len(kept)} DESELECTED_ENV={len(deselected)}")
        config.hook.pytest_deselected(items=deselected)
        items[:] = kept

sys.exit(pytest.main(["-q", "--tb=short", str(ROOT / "tests" / "test_lectures_iib_v5_v1.py")], plugins=[_FilterPlugin()]))
