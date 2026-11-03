"""Essais du lanceur shell v2 de la course Heimersheim (délai 12 h), hors réseau (sous-agent de session-depot, 3 novembre 2026).

La v2 = la v1 (essayée par `test_course_heimersheim_v1.py`, 30 essais, et par neuf mutations) dont seul change le délai de la
course : on vérifie que les lignes qui diffèrent sont exactement les lignes déclarées, puis on rejoue sur la v2 les refus
d'avant tout relais (cas sain : la v1 et la v2 refusent les mêmes artefacts).

  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PYTHON -B -m pytest -q -p no:cacheprovider test_course_heimersheim_v2.py
"""

import difflib
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ICI))))
V1, V2 = (os.path.join(ICI, f"lancer-course-heimersheim-v{n}.sh") for n in (1, 2))
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PYTHONDONTWRITEBYTECODE": "1", "GO_ID": "GO-2026-11-03-98",
       "PY_RELAIS_CLAUDE": sys.executable}
CONF = "configuration-course-heimersheim-v1-avec-kimi.json"


def test_v2_ne_change_que_le_delai_et_les_lignes_declarees():
    a = open(V1, encoding="utf-8").read().splitlines()
    b = open(V2, encoding="utf-8").read().splitlines()
    changees = [l[1:] for l in difflib.unified_diff(a, b, lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
    code = [l for l in changees if not l.lstrip().startswith("#")]
    assert sorted(code) == sorted([
        '  "${E[@]}" HOME="$RA" GO_ID="$GO_ID" timeout -k 120 21600 "$PY" -I -B lancer_course_heimersheim_v1.py lancer \\',
        '  "${E[@]}" HOME="$RA" GO_ID="$GO_ID" timeout -k 120 43200 "$PY" -I -B lancer_course_heimersheim_v1.py lancer \\',
        'ecrire_json_scelle(sys.argv[1], {"version": "lanceur-shell-course-heimersheim-v1", "mode": "$MODE", "go": "$GO_ID",',
        'ecrire_json_scelle(sys.argv[1], {"version": "lanceur-shell-course-heimersheim-v2", "mode": "$MODE", "go": "$GO_ID",'])


def shell(script, *args, **env):
    return subprocess.run(["bash", script] + list(args), env=dict(ENV, **env), capture_output=True, text=True, timeout=60)


def test_v2_refus_avant_tout_relais(tmp_path):
    for script in (V1, V2):
        r = shell(script, "lancer", "GO-2026-11-03-97", CONF, str(tmp_path / "run"), "p", "c")
        assert r.returncode == 2 and "ne court que sous" in r.stderr and not (tmp_path / "run").exists()
        r = shell(script, "lancer", "GO-2026-11-03-98", CONF, str(tmp_path / "run"), "p", "c", REGISTRE_GO="/x")
        assert r.returncode == 2 and "permis qu'en répétition" in r.stderr
        dedans = os.path.join(DEPOT, "run-essai-interdit")
        r = shell(script, "repeter", "GO-2026-11-03-98", CONF, dedans, "p", "c", SSL_CERT_FILE="/nulle-part/ca.pem")
        assert r.returncode == 2 and not os.path.exists(dedans)
