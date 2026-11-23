"""Essai écrit de la veille corrigée (veille-v2.sh), mot de la mère R-5117 : cas sain, coupure, artefact des octets
(413696 et 12058624, relevés sur l'instance 62094971 : cumul ≈ 0,2 USD, aucun arrêt), anomalie (aucun arrêt automatique).
Témoin : la veille v1 fautive, sur l'artefact des octets, rend « COUPURE » (c'est l'erreur du 23 novembre à 04:35:03Z).
Joué : python3 -I essai-veille-cumul-v1.py (depuis ce dossier). Code 0 si tout est conforme."""
import json, re, subprocess, sys, tempfile, time
from pathlib import Path

ICI = Path(__file__).resolve().parent


def bloc(script: str) -> str:
    s = (ICI / script).read_text(encoding="utf-8")
    m = re.search(r'R=\$\(python3 -I - "\$P/veille/liste-\$H\.json" "\$ID" "\$COUP" <<\'PY\'\n(.*?)\nPY\n', s, re.S)
    assert m, f"bloc de calcul introuvable dans {script}"
    return m.group(1)


def jouer(script: str, liste: list, coupure: float) -> str:
    with tempfile.TemporaryDirectory() as t:
        p, q = Path(t) / "l.json", Path(t) / "c.py"
        p.write_text(json.dumps(liste)); q.write_text(bloc(script))
        return subprocess.run([sys.executable, "-I", str(q), str(p), "62094971", str(coupure)], capture_output=True,
                              text=True, check=True).stdout.strip()


def inst(heures, up, down, dph=1.1533333333333333):
    return [{"id": 62094971, "actual_status": "running", "dph_total": dph, "start_date": time.time() - heures * 3600,
             "inet_up_billed": up, "inet_down_billed": down, "inet_up_cost": 0.0390625, "inet_down_cost": 0.026041666666666668}]


cas = [  # (nom, script, liste, coupure, attendu : verdict, cumul min, cumul max)
    ("sain, 1 h, rien d'échangé", "veille-v2.sh", inst(1, 0, 0), 14, "ok", 1.15, 1.16),
    ("artefact des octets (62094971, 04:35Z)", "veille-v2.sh", inst(10.87 / 60, 413696, 12058624), 14, "ok", 0.19, 0.22),
    ("coupure, 12 h", "veille-v2.sh", inst(12, 0, 0), 14, "COUPURE", 13.8, 13.9),
    ("anomalie, 12 To facturés", "veille-v2.sh", inst(0.02, 4e5, 1.2e13), 14, "ANOMALIE", 0, 1e9),
    ("témoin : veille v1 fautive sur l'artefact", "veille-v1-fautive.sh", inst(10.87 / 60, 413696, 12058624), 14, "COUPURE", 0, 1e9),
]
rouge = 0
for nom, script, liste, coup, verdict, a, b in cas:
    etat, cumul, v = jouer(script, liste, coup).split()
    ok = v == verdict and a <= float(cumul) <= b
    rouge += not ok
    print(f"{'OK ' if ok else 'ROUGE'} {nom} : cumul {cumul}, verdict {v} (attendu {verdict}, cumul dans [{a} ; {b}])")
sys.exit(1 if rouge else 0)
