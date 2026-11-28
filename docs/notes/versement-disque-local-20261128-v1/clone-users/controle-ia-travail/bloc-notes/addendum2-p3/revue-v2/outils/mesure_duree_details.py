"""Détails de la durée (point D) sur le dépôt jouet construit par `mesure_duree_revue.py` : processus qui n'importe que
le module (durée murale vue de l'extérieur, et durée des imports vue de l'intérieur), fonction pure seule (10 000
tirages) dans ce processus. Tables synthétiques seulement.

Usage : python mesure_duree_details.py <dossier du gabarit> <journal JSON>
"""
import importlib.util
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import garde_r1_v2  # noqa: F401

from controle_ia.manifeste import graines
from controle_ia.premier_test_ia import lecture as lp

RUN, LEC = "20261020-100000-p3-jouet-taille-reelle", "20261020-110000-lecture-jouet"


def processus_imports(d: Path) -> dict:
    env = {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    env.pop("REVUE_JOURNAL_R1", None)
    code = ("import time; t=time.perf_counter(); import importlib.util as u; "
            "s=u.spec_from_file_location('m', 'docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py'); "
            "m=u.module_from_spec(s); s.loader.exec_module(m); print(time.perf_counter()-t)")
    debut = time.perf_counter()
    r = subprocess.run([sys.executable, "-B", "-c", code], cwd=d, env=env, capture_output=True, text=True, timeout=600)
    return {"mural_s": round(time.perf_counter() - debut, 3), "interieur_s": round(float(r.stdout.split()[-1]), 3)}


def main():
    d, journal = Path(sys.argv[1]), Path(sys.argv[2])
    imports = [processus_imports(d) for _ in range(4)]
    spec = importlib.util.spec_from_file_location("av_jouet", d / "docs/procedures/P3-addendum2-v1/audit_verdict_p3_v1.py")
    av = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(av)
    assert av.TIRAGES == 10_000 and av.RUN_SOURCE == RUN
    source = lp.charger_source(d, RUN)
    lecture = json.loads((d / "diag" / LEC / "lecture-p3.json").read_text(encoding="utf-8"))["resultat"]
    gr = graines(av.cles_addendum2(), av.ENTROPIE_P3)
    pures = []
    for _ in range(4):
        debut = time.perf_counter()
        sortie = av.analyser_addendum2(source, lecture, gr)
        pures.append(round(time.perf_counter() - debut, 3))
    res = {"processus_d_imports": imports, "fonction_pure_s": pures,
           "fonction_pure_controles": sortie["nombre_de_controles"]["ecrits"], "charge_1min": os.getloadavg()[0]}
    journal.write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
