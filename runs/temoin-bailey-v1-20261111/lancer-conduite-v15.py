"""v15 — RUN DE CONFIRMATION au régime complet (R12 ; v1 à v14 restent telles quelles ; addendum 7 du témoin de Bailey,
`prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md`, `554a74d0…`).

Conduite normale de `lanceur_v21` (mise en place, contrôle du juge, pilote, règle, run principal, relance du texte dans la
conduite), sur un poste neuf : aucune instance antérieure (D compte de zéro), B = 85 USD (manifeste v7), GO `GO-2026-11-17-07`,
garde de durée de tour du pilote à 1 800 s (addendum 7, § 2.3), aucune `relance_seule`. Elle ne diffère de la conduite
v13 que par cela, et par ses gardes d'entrée, jouées avant l'écriture du PID et avant toute création : addendum 7 scellé
à l'empreinte attendue ; ligne de GO qui cite cette empreinte entière ; manifeste v7 scellé, B = 85, GO et commit du code attendus ; plafond de
durée exactement 1 800 s. Sortie, bilan et PID neufs (`sortie-conduite-v15`, `bilan-lancement-v15.json`,
`lancement-v15.pid`). Elle ne lit aucune note.

Usage, détaché, depuis la racine du dépôt, sous `GO_ID=GO-2026-11-17-07`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v15.py --offre <id> --image <image>
"""
import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path

from controle_ia import scellement
from controle_ia.temoin_bailey import conventions_v3 as cv
from controle_ia.temoin_bailey import lanceur_v21 as L

DEPOT = Path("/home/user/controle-ia-travail")
BASE = DEPOT / "runs" / "temoin-bailey-v1-20261111"
GO_ID = "GO-2026-11-17-07"
ADDENDUM_7 = DEPOT / "prereg" / "temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md"
EMPREINTE_ADDENDUM_7 = "554a74d07c848c493c485f5f7c37d26dc419e7da381ee4180235adb76edd7f3e"
MANIFESTE = BASE / "manifeste-local-v7.json"
COMMIT_CODE = "a904aa391cdcf2650b747fe64e48caa0ec8c5849"  # addendum 7, § 4
B_ATTENDU = 85.0
T_MAX_PILOTE_S = 1800.0  # addendum 7, § 2.3
DISQUE_GO = 110  # disque demandé à Vast (Go)
ANTERIEURES: list = []  # poste neuf (addendum 7, § 2.2) : D compte de zéro


class FournisseurVastReprises(L.FournisseurVast):
    """Comme en v9 : `envoyer_fichier` retenté (`scp` en échec : 3 essais, 20 s d'écart) ; le dernier échec sort tel quel."""

    def envoyer_fichier(self, ident, local, distant):
        for n in range(3):
            try:
                return super().envoyer_fichier(ident, local, distant)
            except Exception:
                if n == 2:
                    raise
                time.sleep(20)


def gardes_d_entree(texte_go: str) -> None:
    """Avant l'écriture du PID et toute création ; lève `SystemExit` (rien ne tourne, aucune dépense)."""
    scellement.verifier(ADDENDUM_7)
    if cv.sha_fichier(ADDENDUM_7) != EMPREINTE_ADDENDUM_7:
        raise SystemExit("addendum 7 : empreinte différente de celle attendue : rien ne tourne")
    go = L.ligne_go(texte_go, GO_ID)
    if EMPREINTE_ADDENDUM_7 not in go["objet"]:
        raise SystemExit("la ligne de GO ne cite pas l'empreinte de l'addendum 7 : rien ne tourne")
    scellement.verifier(MANIFESTE)
    man = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    if float(man["B"]) != B_ATTENDU or man["go_id"] != GO_ID or man["commit_code"] != COMMIT_CODE:
        raise SystemExit("manifeste v7 : B, GO ou commit du code différents de ceux de l'addendum 7 : rien ne tourne")
    if T_MAX_PILOTE_S != 1800.0 or ANTERIEURES:
        raise SystemExit("plafond de durée du pilote différent de 1 800 s, ou instances antérieures : rien ne tourne")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--offre", required=True)
    p.add_argument("--image", required=True)
    a = p.parse_args()
    if os.environ.get("GO_ID") != GO_ID or os.environ.get("DEPOT_URL") != L.DEPOT_URL:
        print("GO_ID ou DEPOT_URL absent ou différent : rien ne tourne", file=sys.stderr)
        return 2
    manquants = [o for o in ("vastai", "ssh", "scp") if shutil.which(o) is None]
    if manquants:
        print(f"outils introuvables dans le PATH : {manquants} : rien ne tourne", file=sys.stderr)
        return 2
    texte_go = L.texte_go_main(DEPOT)
    gardes_d_entree(texte_go)
    pidf = BASE / "lancement-v15.pid"
    sortie = BASE / "sortie-conduite-v15"  # chemin absolu, le même pour `reprendre` (A-1)
    trace = BASE / "bilan-lancement-v15.json"
    if pidf.exists() or trace.exists():
        print("PID ou bilan de lancement déjà présent (R12) : rien ne tourne", file=sys.stderr)
        return 2
    pidf.write_text(f"{os.getpid()}\n", encoding="utf-8")
    conduite = L.Conduite(fournisseur=FournisseurVastReprises(), manifeste_local=MANIFESTE, sortie=sortie, go_id=GO_ID,
                          texte_go=texte_go, offre=str(a.offre), image=a.image, depot_local=DEPOT,
                          instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO, t_max_pilote_s=T_MAX_PILOTE_S)
    if conduite.relance_seule is not None or conduite.t_max_pilote_s != 1800.0:
        print("conduite mal construite : rien ne tourne", file=sys.stderr)
        return 2
    debut = time.time()
    try:
        bilan = conduite.conduire()
        issue = {"bilan": bilan}
    except Exception as err:  # la conduite a déjà fait `_finir` ; on consigne l'erreur sans valeur de note
        issue = {"erreur": f"{type(err).__name__}: {err}"[:500]}
    issue.update({"offre": a.offre, "image": a.image, "debut": debut, "fin": time.time(), "pid": os.getpid()})
    trace.write_text(json.dumps(issue, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                     encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
