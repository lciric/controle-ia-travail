from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\wt-dr-v3")


def read_lf(rel: str) -> str:
    data = (ROOT / rel).read_bytes()
    assert b"\r" not in data, f"CR found in source {rel}"
    return data.decode("utf-8")


def write_lf_and_sha(rel: str, text: str) -> str:
    assert "\r" not in text, f"CR found in output {rel}"
    if not text.endswith("\n"):
        text += "\n"
    p = ROOT / rel
    raw = text.encode("utf-8")
    p.write_bytes(raw)
    sha = hashlib.sha256(raw).hexdigest()
    Path(str(p) + ".sha256").write_bytes(f"{sha}  {p.name}\n".encode("utf-8"))
    return sha


def replace_once(src: str, old: str, new: str, label: str) -> str:
    n = src.count(old)
    assert n == 1, f"{label}: expected 1 occurrence of {old!r}, got {n}"
    return src.replace(old, new, 1)


tc4_sha = hashlib.sha256((ROOT / "scripts/tests-cibles-dose-reponse-v4.txt").read_bytes()).hexdigest()
assert tc4_sha == "2766a9b022d4e9db45dd0c85d224473409b4cacb20aad9a1c3fd81166c449d55"

a3 = read_lf("scripts/amorce_instance_dose_reponse_v3.sh")
a4 = replace_once(
    a3,
    "#!/usr/bin/env bash\n# [v3 (mot de Lazar GO-2026-11-24-31",
    "#!/usr/bin/env bash\n"
    "# [v4 (écart matériel minimal autorisé par Lazar : GO-2026-11-25-01, R-5397) ; nom neuf, R12 : la v3 reste telle quelle.\n"
    "# Changent seulement : les gardes avant calcul (`controles_v3` : `stockage_max_usd_h` relevé de `0.08` à `0.10` USD/h),\n"
    "# la course jouée (`controle_ia.dose_reponse.course_v3`), la liste d'essais figée (`scripts/tests-cibles-dose-reponse-v4.txt`,\n"
    "# empreinte et compte écrits en dur) et la ligne de démarrage « AMORCE DR v4 » ; rien d'autre.]\n"
    "# [v3 (mot de Lazar GO-2026-11-24-31",
    "amorce_v4 header",
)
a4 = replace_once(a4, "AMORCE DR v3 DEMARRAGE", "AMORCE DR v4 DEMARRAGE", "amorce_v4 banner")
a4 = replace_once(a4, 'journal "début dose-réponse v3 :', 'journal "début dose-réponse v4 :', "amorce_v4 journal")
a4 = replace_once(
    a4,
    "from controle_ia.dose_reponse import controles_v2 as ct",
    "from controle_ia.dose_reponse import controles_v3 as ct",
    "amorce_v4 ct",
)
a4 = replace_once(
    a4,
    'LISTE_TESTS="scripts/tests-cibles-dose-reponse-v3.txt"; LISTE_SHA256="4d99cacc52a8695498d4fb4a498653dc5e5f14ef4d0203b937ca08c3c943134f"; ATTENDUS="58"; FICHIERS_TESTS=""',
    f'LISTE_TESTS="scripts/tests-cibles-dose-reponse-v4.txt"; LISTE_SHA256="{tc4_sha}"; ATTENDUS="60"; FICHIERS_TESTS=""',
    "amorce_v4 liste tests",
)
a4 = replace_once(
    a4,
    "python -m controle_ia.dose_reponse.course_v2",
    "python -m controle_ia.dose_reponse.course_v3",
    "amorce_v4 course_v3",
)
sha_a4 = write_lf_and_sha("scripts/amorce_instance_dose_reponse_v4.sh", a4)
print("amorce_instance_dose_reponse_v4.sh", sha_a4)
