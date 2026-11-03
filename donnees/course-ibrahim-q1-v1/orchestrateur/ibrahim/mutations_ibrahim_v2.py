#!/usr/bin/env python3
"""Contre-épreuve par mutations des gardes de la course Ibrahim Q1 (R4) — v2 (sous-agent de session-depot, 3 novembre 2026).
(v2 = mutations_ibrahim_v1.py, gardé, R12, appliqué aux essais v2 et au lanceur shell v2, plus M10 : max_appels v1 rendu à la
configuration cinq espèces v2, contre-lecture CLI-01. Lignes héritées :)
(Kit Ibrahim Q1, v1, dérivé par substitution de noms du kit Kirchner Q2 v2 — branche outils/course-kirchner-q2-v1, 53e1f738 — par un sous-agent de session-depot, 3 novembre 2026 ; les mentions de versions et de kits antérieurs ci-dessous sont héritées.)
(Kit Ibrahim Q1, v1, dérivé à l'octet près des substitutions de nom du kit Heimersheim — branche outils/course-heimersheim-v1 — par un sous-agent de session-depot, 3 novembre 2026 ; les mentions de versions antérieures ci-dessous sont celles du kit Heimersheim.)

Copie, dans un dossier temporaire, l'arbre minimal du dépôt (`donnees/course-ibrahim-q1-v1/orchestrateur/`, les commandes
A1-bis, la garde du dépôt) ; vérifie que les essais passent sur la copie intacte ; puis, pour chaque mutation (une garde
neutralisée, remplacement textuel qui doit apparaître une seule fois), refait une copie neuve, applique la mutation et exige
qu'au moins un essai échoue. Le dépôt lui-même n'est jamais modifié.

  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHON -I -B mutations_ibrahim_v2.py
Code : 0 si chaque mutation fait échouer au moins un essai et si la copie intacte passe ; 3 sinon.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ICI))))
ARBRE = ("donnees/course-ibrahim-q1-v1/orchestrateur", "docs/notes/ideation-organisme-v1/commandes-a1-bis-v1", ".claude/hooks")
FICHIERS = ("docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py",
            "docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py.sha256")
K = "donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/"
MUTATIONS = (
    ("M1 relais Kimi au-dessus de 5 USD accepté", K + "course_ibrahim_v1.py",
     'elif f in PLAFOND_RELAIS_MAX and r["plafond_usd"] > PLAFOND_RELAIS_MAX[f]:', 'elif False:'),
    ("M2 plafond de session sous le pire cas accepté", K + "course_ibrahim_v1.py",
     "if not float(ps.get(r, 0)) > pire:", "if False:"),
    ("M3 Argon accepté hors de la variante cinq espèces", K + "course_ibrahim_v1.py",
     'if v != "cinq_especes" and ("argon" in four', 'if False and ("argon" in four'),
    ("M4 modèle Claude non permis transmis", K + "commande_claude_ibrahim_v1.py",
     "if demande not in MODELES_PERMIS:", "if demande is None:"),
    ("M5 GO_ID différent de l'identifiant attendu accepté", K + "lancer_course_ibrahim_v1.py",
     'if env.get("GO_ID") != attendu:', "if False:"),
    ("M6 pièce exigée non gelée acceptée", K + "lancer_course_ibrahim_v1.py",
     "    if manquent:\n        raise LancementRefuse(\"pièces non gelées", "    if False:\n        raise LancementRefuse(\"pièces non gelées"),
    ("M7 canari accepté par la garde anti-fuite", K + "trace_agregee_course_ibrahim_v1.py",
     "can = sorted(c for c in canaris if c and c in plat)", "can = []"),
    ("M8 registre des GO de répétition accepté au lancement réel", K + "lancer-course-ibrahim-v2.sh",
     '[ -z "${REGISTRE_GO:-}${CONFIGURATION_REPETITION:-}" ] ||', "true ||"),
    ("M9 étiquette interdite dans une consigne de juge acceptée", K + "course_ibrahim_v1.py",
     "        trouvees = trouver(t, interdites, mode)\n", "        trouvees = []\n"),
    ("M10 marge d'appels v1 (203) rendue au relais Claude à cinq espèces", K + "configuration-course-ibrahim-q1-v2-cinq-especes.json",
     '"max_appels": 301', '"max_appels": 203'),
)


def copie(dest):
    for r in ARBRE:
        src = os.path.join(DEPOT, r)
        shutil.copytree(src, os.path.join(dest, r), ignore=shutil.ignore_patterns("__pycache__"))
    for r in FICHIERS:
        os.makedirs(os.path.dirname(os.path.join(dest, r)), exist_ok=True)
        shutil.copy2(os.path.join(DEPOT, r), os.path.join(dest, r))


def essais(dest):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PYTHONDONTWRITEBYTECODE": "1", "HOME": dest}
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                        os.path.join(dest, K, "test_course_ibrahim_v2.py")], env=env, capture_output=True, text=True, cwd=dest)
    m = re.search(r"(\d+) failed", r.stdout)
    return r.returncode, int(m.group(1)) if m else 0, r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]


def principal():
    bilan = True
    with tempfile.TemporaryDirectory(prefix="mutations-kirchner-") as t:
        d0 = os.path.join(t, "intacte")
        copie(d0)
        code, n, fin = essais(d0)
        print(f"copie intacte : code {code} ({fin})")
        bilan &= code == 0
        for nom, fichier, avant, apres in MUTATIONS:
            d = os.path.join(t, nom.split()[0])
            copie(d)
            p = os.path.join(d, fichier)
            s = open(p, encoding="utf-8").read()
            if s.count(avant) != 1:
                print(f"{nom} : motif à muter trouvé {s.count(avant)} fois (1 exigée) : ÉCHEC")
                bilan = False
                continue
            open(p, "w", encoding="utf-8").write(s.replace(avant, apres))
            code, n, fin = essais(d)
            ok = code != 0 and n >= 1
            bilan &= ok
            print(f"{nom} : {'conforme' if ok else 'ÉCHEC'} — {n} essai(s) en échec ({fin})")
    print("bilan :", "chaque mutation fait échouer au moins un essai" if bilan else "ÉCART")
    return 0 if bilan else 3


if __name__ == "__main__":
    sys.exit(principal())
