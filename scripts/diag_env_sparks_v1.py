"""Tir de diagnostic d'environnement SPARKS, v1 — gardes du lanceur, hors du code scellé. Bibliothèque standard seule ;
le contrôle du GO reprend `sparks_exp7_nul_v9/tir.py` (périmètre « SPARKS » et « tir », auteur, plafond ≤ 5 USD, validité,
révocation) avec une **durée de 40 minutes** (le tir de diagnostic installe `requirements-gpu.txt` et joue les cinq
fichiers d'essais : plus long que les 20 à 30 minutes d'un tir de la minuterie), même formule de devis.

    python3 -I -B diag_env_sparks_v1.py liste DEPOT COMMIT        → la différence 78671d93..COMMIT est exactement les fichiers du diagnostic
                                                                   (quatre fichiers de code et d'essais et leurs compagnons ; ajouts sous docs/ ignorés)
    python3 -I -B diag_env_sparks_v1.py go GO_MD GO_ID PRIX_CARTE PRIX_STOCKAGE [AAAA-MM-JJ]   → ECHEANCE_UTC_S= DEVIS_USD= PLAFOND_USD=
"""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

CODE_SCELLE = "78671d9362c82a3ef02312bcf80c076a19069d42"          # code v12 : le diagnostic ne le touche pas
FICHIERS = ("scripts/amorce_diag_env_sparks_v1.sh", "scripts/diag_env_sparks_v1.py", "scripts/lancer_diag_env_sparks_v1.sh",
            "tests/test_sparks_diag_env_v1.py")                  # chacun avec son compagnon .sha256 : liste close, 8 fichiers
AJOUTS_IGNORES = ("docs/",)   # procédures et notes ajoutées sur la branche (l'ordre à la fille 6) : jamais exécutées sur la machine,
#                               hors de la liste close (décision de la mère, 5 novembre 2026, 20:03 UTC) ; une modification y reste un refus
MINUTES = 40
RELANCE_MIN, MARGE_MIN, STOCKAGE_EN_PLUS_MIN = 15, 10, 60

_T9 = Path(__file__).resolve().parents[1] / "src" / "controle_ia" / "sparks_exp7_nul_v9" / "tir.py"
_s = importlib.util.spec_from_file_location("tir_v9_pour_diag", _T9)
t9 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(t9)
GardeTir = t9.GardeTir


def verifier_liste(depot: Path, commit: str) -> int:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise GardeTir("commit du diagnostic : 40 chiffres hexadécimaux attendus")
    if subprocess.run(["git", "-C", str(depot), "merge-base", "--is-ancestor", CODE_SCELLE, commit]).returncode != 0:
        raise GardeTir(f"{commit[:12]} ne descend pas du code scellé {CODE_SCELLE[:12]}")
    r = subprocess.run(["git", "-C", str(depot), "diff", "--name-status", "--no-renames", f"{CODE_SCELLE}..{commit}"],
                       capture_output=True, text=True, check=True)
    diff = [l.split("\t") for l in r.stdout.splitlines() if l.strip()]
    mauvais = [d for d in diff if d[0] != "A"]
    if mauvais:
        raise GardeTir(f"le diagnostic modifie ou supprime un fichier du code scellé : {mauvais[:3]}")
    attendus = {f for f in FICHIERS} | {f + ".sha256" for f in FICHIERS}
    changes = {d[-1] for d in diff if not d[-1].startswith(AJOUTS_IGNORES)}
    if changes != attendus:
        raise GardeTir(f"différence ≠ fichiers du diagnostic : hors liste {sorted(changes - attendus)[:4]}, absents {sorted(attendus - changes)[:4]}")
    return len(changes)


def devis(prix_carte: float, prix_stockage: float, minutes: int = MINUTES) -> float:
    if prix_carte <= 0 or prix_stockage < 0:
        raise GardeTir("prix illisibles")
    return prix_carte * (minutes + RELANCE_MIN + MARGE_MIN) / 60 + prix_stockage * (minutes + STOCKAGE_EN_PLUS_MIN) / 60


def preparer(chemin_go: Path, go_id: str, prix_carte: float, prix_stockage: float, aujourd_hui: date | None = None,
             maintenant_s: int | None = None) -> dict:
    t9.verifier_perimetre(chemin_go, go_id)
    plafond = t9.t5.verifier_go_tir(chemin_go, go_id, aujourd_hui)
    d = devis(prix_carte, prix_stockage)
    if d > plafond:
        raise GardeTir(f"devis du diagnostic {d:.2f} USD > plafond {plafond:g} USD de {go_id}")
    now = int(time.time()) if maintenant_s is None else maintenant_s
    return {"plafond_usd": plafond, "devis_usd": round(d, 4), "echeance_utc_s": now + MINUTES * 60}


def main(argv: list[str]) -> int:
    try:
        if argv[0] == "liste":
            n = verifier_liste(Path(argv[1]), argv[2])
            print(f"DIAGNOSTIC HORS DU CODE SCELLÉ : {n} fichiers neufs sur {CODE_SCELLE[:12]}, aucun fichier modifié")
        elif argv[0] == "go":
            j = date.fromisoformat(argv[5]) if len(argv) > 5 else None
            r = preparer(Path(argv[1]), argv[2], float(argv[3]), float(argv[4]), j)
            print(f"ECHEANCE_UTC_S={r['echeance_utc_s']} DEVIS_USD={r['devis_usd']} PLAFOND_USD={r['plafond_usd']:g} MINUTES={MINUTES}")
        else:
            raise IndexError
    except (GardeTir, IndexError, ValueError, subprocess.CalledProcessError) as err:
        print(f"DIAGNOSTIC REFUSÉ : {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
