"""v12 — RELANCE SEULE (R12 ; v1 à v11 restent telles quelles ; addendum 5) : relance entière de la liste d'arrêt
(texte l. 338, 371) après l'interruption du run principal de la série 3 (K′ = 8 tours complets, compte Vast sans crédit ;
reprise faite, `sortie-conduite-v11/reprise-v10-2/`). Conduite `lanceur_v18` avec `relance_seule` : amorce, auto-arrêt,
mise en place et contrôle du juge sur une instance neuve, puis, sans pilote ni règle sur l'instance, K recalculé par la
règle (même B, D du poste, c de l'instance neuve, t du pilote de la série 3) et `principal-relance`. Manifeste v6 (commit
du code v18). Instances antérieures : les sept du poste (60417353 ajoutée, destruction écrite par la reprise dans
`sortie-conduite-v11/poste-v5.json`). Gardes de ce script, avant toute création : empreintes du manifeste de la règle et
du journal des durées de la reprise ; exactement 8 lignes de durées (tours 0 à 7). Sortie, bilan et PID neufs
(`sortie-conduite-v12`, `bilan-lancement-v12.json`, `lancement-v12.pid`).

v11 (R12 ; v1 à v10 restent telles quelles) : v10 sans son défaut de syntaxe (deux ouvertures de docstring ; la v10,
scellée, n'a jamais tourné). Code, manifeste, instances antérieures : ceux de la v10. Sortie, bilan et PID neufs
(`sortie-conduite-v11`, `bilan-lancement-v11.json`, `lancement-v11.pid`).

v10 (R12 ; v1 à v9 restent telles quelles) : code v17 (`lanceur_v17`, `instance_v16`, `execution_v4` : le script public
est lancé comme programme principal par `runpy.run_path` ; addendum 4) ; manifeste v5 (au commit du code v17) ; sortie,
bilan et PID neufs (`sortie-conduite-v10`, `bilan-lancement-v10.json`, `lancement-v10.pid`) ; instance 60403564 (série 2)
ajoutée aux instances antérieures. Même fournisseur à envoi retenté que la v9.

v9 (R12 ; v1 à v8 restent telles quelles) : la conduite reçoit un fournisseur Vast dont l'envoi de fichier (`scp`)
est retenté (3 essais, 20 s d'écart) au lieu d'abandonner au premier échec : la v8 a échoué à l'envoi de l'archive du code
(code 255) le 12 novembre à 20:11Z, avant l'amorce. Le code du run (commit 91238a73) ne change pas : seule la classe
passée en paramètre (`FournisseurVastReprises`, ci-dessous) diffère. Sortie, bilan et PID neufs (`sortie-conduite-v9`,
`bilan-lancement-v9.json`, `lancement-v9.pid`) ; instance 60400450 ajoutée aux instances antérieures.

v8 (R12 ; v1 à v7 restent telles quelles) : code v16 (`lanceur_v16`, `instance_v15`, commit 91238a73 ; addendum 3,
brouillon 2) ; sortie, bilan et PID neufs (`sortie-conduite-v8`, `bilan-lancement-v8.json`, `lancement-v8.pid`) ; même
manifeste v4 (au commit du code v16), mêmes instances antérieures. La v7 (code v14) n'a jamais tourné.

v7 (R12 ; v1 à v6 restent telles quelles) : code v14 (`lanceur_v14`, `instance_v13`, commit 4821ad7e ; addendum 3) ;
sortie, bilan et PID neufs ; manifeste `manifeste-local-v4.json` (commit du code v14) ; (`sortie-conduite-v7`, `bilan-lancement-v7.json`, `lancement-v7.pid`) ; instance 60370363
(run v6, détruite par la conduite après la seconde chute du pilote) ajoutée aux instances antérieures du poste.

v6 (R12 ; v1 à v5 restent telles quelles) : disque demandé à 110 Go au lieu de la valeur par défaut du code (200 Go),
qui n'est ni dans le préenregistrement ni dans le devis (le devis chiffre 1 à 2 Go de sondes et suffixes) ; aucune A100 80 Go
louable n'offrait 200 Go le 12 novembre à 14:57Z ; mot de Lazar : « on loue ce qu'il y a now ». Sortie, bilan et PID
neufs (`sortie-conduite-v6`, `bilan-lancement-v6.json`, `lancement-v6.pid`). La conduite v5 n'a jamais tourné.

v5 (R12 ; v1 à v4 restent telles quelles) : conduite tournée sur un poste Hetzner (la session ne peut pas ouvrir de
`ssh`) ; sortie, bilan et PID neufs (`sortie-conduite-v5`, `bilan-lancement-v5.json`, `lancement-v5.pid`) ; instance
60330510 (lancement v4, détruite par la conduite) ajoutée aux instances antérieures du poste.

v4 (R12 ; v1 à v3 restent telles quelles) : sortie, bilan et PID neufs (`sortie-conduite-v4`, `bilan-lancement-v4.json`,
`lancement-v4.pid`) ; instance 60326443 (lancement v3, détruite à 08:08:49Z après l'extinction de la machine de la
session) ajoutée aux instances antérieures du poste.

v3 (R12 ; v1 et v2 restent telles quelles) : sortie et bilan neufs (`sortie-conduite-v3`, `bilan-lancement-v3.json`) ;
PID écrit par le script lui-même au démarrage (`lancement-v3.pid` ; en v2, le PID relevé était celui du parent de
`setsid`, sorti aussitôt) ; instance 60280913 (lancement v2, détruite) comptée dans les instances antérieures du poste
(B = 75, fixé à sa création ; D la compte).

v2 (R12 ; la v1 reste telle quelle) : sortie et bilan neufs (`sortie-conduite-v2`, `bilan-lancement-v2.json`) ;
refus avant toute conduite si `vastai`, `ssh` ou `scp` est introuvable dans le PATH (la v1 a échoué à la création,
`FileNotFoundError: vastai`, aucune instance créée, inventaire R10 vide pour son étiquette).

Lancement de la conduite du témoin de Bailey (addendum 2, condition 6 ; procédure de la passation
`registres/passations/2026-11-11-1624-attaquant-informe-passation-autre-compte.md`, étape 5).

Usage, détaché (`setsid nohup`), depuis la racine du dépôt, sous `GO_ID=GO-2026-11-10-10`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v12.py --offre <id> --image <image>

Ce script ne fait que construire `lanceur_v13.Conduite` avec les valeurs de la procédure et appeler `.conduire()` ;
toutes les gardes sont celles du code au commit 4988f3f4. Le bilan rendu est écrit dans `bilan-lancement-v2.json`
à côté de la sortie (jamais dans la sortie, que la conduite exige neuve). Il ne lit aucune note.
"""
import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path

from controle_ia import scellement
from controle_ia.temoin_bailey import lanceur_v18 as L

DEPOT = Path("/home/user/controle-ia-travail")
BASE = DEPOT / "runs" / "temoin-bailey-v1-20261111"
GO_ID = "GO-2026-11-10-10"


class FournisseurVastReprises(L.FournisseurVast):
    """v9 : `envoyer_fichier` retenté (`scp` en échec : 3 essais, 20 s d'écart) ; le dernier échec sort tel quel."""

    def envoyer_fichier(self, ident, local, distant):
        for n in range(3):
            try:
                return super().envoyer_fichier(ident, local, distant)
            except Exception:
                if n == 2:
                    raise
                time.sleep(20)
DISQUE_GO = 110  # v6 : disque demandé à Vast (Go)
# Lancement v2 : création relevée par la conduite (`conduite-v5.jsonl` de la sortie v2), destruction par l'identifiant
# à 2026-11-12T00:14:43Z (`registres/arrets.md`), c relevé par la conduite.
ANTERIEURES = [{"id": "60280913", "c": 1.6404444444444444, "creation": 1794441800.044329,
                "destruction": 1794442483.0, "B": 75.0},
               # Lancement v3 : création relevée par la conduite (sortie v3), destruction par l'identifiant à 08:08:49Z.
               {"id": "60326443", "c": 1.2392592592592593, "creation": 1794469718.6305506,
                "destruction": 1794470929.0, "B": 75.0},
               # Lancement v4 : création et destruction relevées par la conduite v4 (`sortie-conduite-v4/poste-v5.json`).
               {"id": "60330510", "c": 1.6071111111111112, "creation": 1794472034.7656338,
                "destruction": 1794473847.2796314, "B": 75.0},
               # Run v6 : création et destruction relevées par la conduite v6 (`sortie-conduite-v6/poste-v5.json`).
               {"id": "60370363", "c": 1.2838888888888886, "creation": 1794495776.7685294,
                "destruction": 1794497008.1361988, "B": 75.0},
               # Série 2, conduite v8 : création et destruction relevées par la conduite (`sortie-conduite-v8/poste-v5.json`).
               {"id": "60400450", "c": 1.503963388888889, "creation": 1794514214.5005274,
                "destruction": 1794514349.6833932, "B": 75.0},
               # Série 2, conduite v9 : création et destruction relevées par la conduite (`sortie-conduite-v9/poste-v5.json`).
               {"id": "60403564", "c": 1.3314444444444447, "creation": 1794516103.7767491,
                "destruction": 1794518119.5065181, "B": 75.0},
               # Série 3, conduite v11 : création relevée par la conduite, destruction écrite par la reprise v3
               # (`sortie-conduite-v11/poste-v5.json`).
               {"id": "60417353", "c": 1.342111111111111, "creation": 1794525123.5713172,
                "destruction": 1794556404.244174, "B": 75.0}]
REPRISE = BASE / "sortie-conduite-v11" / "reprise-v10-2"
TOURS_COMPLETS_PREMIERE = 8  # note `registres/passations/2026-11-13-0803-…` (`ab372ed1…`) : tours 0 à 7


def relance_seule() -> dict:
    """Règle de la première exécution (manifeste de la règle transféré par la reprise) et K′, vérifiés."""
    m = REPRISE / "manifeste-v3-regle.json"
    durees = REPRISE / "principal" / "transfert-1" / "sortie-durees-v3.jsonl"
    scellement.verifier(m)
    scellement.verifier(durees)
    lignes = [l for l in durees.read_text(encoding="utf-8").splitlines() if l.strip()]
    tours = sorted(json.loads(l)["tour"] for l in lignes)
    if tours != list(range(TOURS_COMPLETS_PREMIERE)):
        raise SystemExit(f"journal des durées : tours {tours}, attendus 0 à {TOURS_COMPLETS_PREMIERE - 1}")
    regle = json.loads(m.read_text(encoding="utf-8"))["regle_tours"]
    return {"tours_complets_premiere": TOURS_COMPLETS_PREMIERE, "regle_premiere": regle, "source": str(REPRISE)}


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
    pidf = BASE / "lancement-v12.pid"
    if pidf.exists():
        print("PID de lancement déjà présent (R12) : rien ne tourne", file=sys.stderr)
        return 2
    pidf.write_text(f"{os.getpid()}\n", encoding="utf-8")
    sortie = BASE / "sortie-conduite-v12"  # chemin absolu, le même pour `reprendre` (A-1)
    trace = BASE / "bilan-lancement-v12.json"
    if trace.exists():
        print("bilan de lancement déjà présent (R12) : rien ne tourne", file=sys.stderr)
        return 2
    conduite = L.Conduite(fournisseur=FournisseurVastReprises(), manifeste_local=BASE / "manifeste-local-v6.json",
                          sortie=sortie, go_id=GO_ID, texte_go=L.texte_go_main(DEPOT), offre=str(a.offre),
                          image=a.image, depot_local=DEPOT, instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO,
                          relance_seule=relance_seule())
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
