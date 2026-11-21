"""Lanceur d'une machine A100 du loueur pour les étapes 1 et 2a, mode exploratoire (GO-2026-11-21-44).

Ce module NE LANCE RIEN : il contrôle et IMPRIME les commandes, que la session de course joue. Toute commande de création
porte le préfixe `GO_ID=…`, et la décision de la garde de calcul du dépôt (`.claude/hooks/garde_calcul.py`, chargée
telle quelle) est rejouée sur elle : un GO absent, d'un autre type que « calcul », non accordé par Lazar, hors de sa
période ou révoqué refuse le départ. La dépense d'une machine passe toujours par un devis accordé : le prix plafond et la
coupure ne se devinent pas, ils sont donnés par la session, lus dans le devis.

Mécanismes :
- coupure de dépense : la destruction tombe au plus tard 6 h 30 après la commande, plus tôt si le plafond l'exige ; la
  marche tourne sous `timeout` jusqu'à un quart d'heure avant ; `depense` refuse dès que cumul + un quart d'heure ≥ 10 USD ;
- minuterie de destruction (dans l'amorce) : à l'heure de destruction, l'instance se détruit par son identifiant
  si le versement final est prouvé, sinon elle s'arrête (disque gardé) et écrit un signal pour la mère ;
- versement : les sorties permises sont poussées sur la branche `donnees/dopamine-exploratoire-v1` ; l'inventaire (noms,
  tailles, empreintes) de tout ce qui existe est poussé et relu ; `detruire` refuse tant que ce versement n'est pas prouvé
  au commit nommé, atteignable depuis la branche distante ;
- arrêt par l'identifiant seulement (R10) : identifiant numérique, étiquette de ce plan, absence prouvée par la liste.

Horloge (devis de l'étape 1, § 5) : plus aucun lancement 5 h 30 après la commande, destruction 6 h 30 après (avancée si
le plafond de 10 USD, réseau compris, l'exige au prix de l'offre).

Sous-commandes : plan ; commande RACINE 1 OFFRE.json COMMIT RUN_ID [CONTEXTES LISTE_HONNETES] ; depense CUMUL PRIX ;
detruire RACINE ID 1 LISTE.json INVENTAIRE.json COMMIT ; verifier-destruction LISTE.json ID TEMOIN.
GO_ID est lu dans l'environnement (commande, detruire). Codes : 0 accepté, 2 refus (motif sur la sortie d'erreur).
"""
from __future__ import annotations

import base64
import contextlib
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import verifier

ETAPES = ("1",)                 # l'étape 2a tourne au processeur ; sa relecture forcée est un bloc de l'étape 1
ETIQUETTE = "dopamine-exploratoire-v1-etape-{etape}"
BRANCHE_SORTIE = "donnees/dopamine-exploratoire-v1"
IMAGE = "python:3.11-bookworm"
DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"
AMORCE = "src/controle_ia/dopamine_exploratoire/amorce_v1.sh"
# devis de l'étape 1 (prereg/papier-dopamine-moniteur-v1/exploratoire/devis-etape-1-rejeu-math500-exploratoire-v1.md),
# § 2 et § 5 ; ligne GO-2026-11-21-48
DEVIS = {"chemin": "prereg/papier-dopamine-moniteur-v1/exploratoire/devis-etape-1-rejeu-math500-exploratoire-v1.md",
         "plafond_usd": 10.0, "reseau_max_usd": 0.68, "fin_lancements_h": 5.5, "destruction_h": 6.5}
DISQUE_GO = 90
QUART_D_HEURE_H = 0.25
OFFRE = {"nom": ("A100", "SXM4"), "memoire_carte_min_mo": 79000, "cartes": 1, "cuda_min": 13.0,
         "memoire_vive_min_mo": 64000, "coeurs_min": 12, "disque_min_go": DISQUE_GO, "prix_carte_max_usd_h": 1.30,
         "stockage_max_usd_h": 0.08}
_RUN = re.compile(r"^[0-9]{8}-[0-9]{6}-[a-z0-9-]*exploratoire[a-z0-9-]*$")
_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
MARCHE_MIN_H = 0.5


def _positif(v, quoi: str) -> float:
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v <= 0:
        raise GardeArret(f"{quoi} illisible ou non positif : {v!r}")
    return float(v)


def exiger_etape(etape: str) -> str:
    if etape not in ETAPES:
        raise GardeArret(f"étape {etape!r} : {ETAPES} attendues")
    return etape


def etiquette(etape: str) -> str:
    return ETIQUETTE.format(etape=exiger_etape(etape))


def exiger_offre(offre: dict) -> dict:
    """Bornes du devis sur une offre (entrée brute de la recherche du loueur) : A100 SXM4 80 Go, carte ≤ 1,30 USD/h,
    stockage de 90 Go ≤ 0,08 USD/h, 12 cœurs, 64 Go, CUDA ≥ 13. Champ absent : refus, jamais un défaut deviné."""
    def nombre(cle):
        v = offre.get(cle)
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            raise GardeArret(f"offre : champ {cle} absent ou illisible")
        return float(v)

    nom = str(offre.get("gpu_name", "")).replace("_", " ")
    if not all(x in nom for x in OFFRE["nom"]):
        raise GardeArret(f"offre : carte {offre.get('gpu_name')!r}, A100 SXM4 attendue")
    stockage_h = nombre("storage_cost") * DISQUE_GO / 730.0
    for cle, borne, sens in (("num_gpus", OFFRE["cartes"], "="), ("gpu_ram", OFFRE["memoire_carte_min_mo"], ">="),
                             ("cuda_max_good", OFFRE["cuda_min"], ">="), ("cpu_ram", OFFRE["memoire_vive_min_mo"], ">="),
                             ("cpu_cores_effective", OFFRE["coeurs_min"], ">="),
                             ("disk_space", OFFRE["disque_min_go"], ">="),
                             ("dph_total", OFFRE["prix_carte_max_usd_h"] + OFFRE["stockage_max_usd_h"], "<=")):
        v = nombre(cle)
        if (sens == "=" and v != borne) or (sens == ">=" and v < borne) or (sens == "<=" and not 0 < v <= borne):
            raise GardeArret(f"offre : {cle} = {v} hors de la borne du devis ({sens} {borne})")
    if stockage_h > OFFRE["stockage_max_usd_h"]:
        raise GardeArret(f"offre : stockage {stockage_h:.3f} USD/h > {OFFRE['stockage_max_usd_h']}")
    if not str(offre.get("id", "")).isdigit():
        raise GardeArret("offre : identifiant illisible")
    return {"id": str(offre["id"]), "prix_usd_h": nombre("dph_total")}


def horaires(depart_s: float, prix_usd_h: float) -> dict:
    """Fin des lancements (5 h 30) et destruction (6 h 30) comptées depuis l'impression de la commande (plus tôt que la
    création : prudent) ; la destruction est avancée si le plafond, réseau compris, l'exige au prix de l'offre."""
    prix = _positif(prix_usd_h, "prix")
    h_plafond = (DEVIS["plafond_usd"] - DEVIS["reseau_max_usd"]) / prix - QUART_D_HEURE_H
    h_destr = min(DEVIS["destruction_h"], h_plafond)
    h_fin = min(DEVIS["fin_lancements_h"], h_destr - 0.5)
    if h_fin < 1.0:
        raise GardeArret(f"au prix {prix} USD/h : {h_fin:.2f} h avant l'arrêt des lancements, aucun départ")
    return {"fin_lancements_s": int(depart_s + h_fin * 3600), "destruction_s": int(depart_s + h_destr * 3600),
            "fin_lancements_h": h_fin, "destruction_h": h_destr}


def echeance_arret_s(depart_s: float, prix_usd_h: float, coupure_usd: float) -> int:
    """Instant (s UTC) où le cumul plus un quart d'heure atteint la coupure, compté depuis l'impression (prudent)."""
    heures = _positif(coupure_usd, "coupure") / _positif(prix_usd_h, "prix") - QUART_D_HEURE_H
    if heures < MARCHE_MIN_H:
        raise GardeArret(f"{heures:.2f} h avant la coupure : moins de {MARCHE_MIN_H} h de marche, aucun départ")
    return int(depart_s + heures * 3600)


def garde_depense(cumul_usd: float, prix_usd_h: float, coupure_usd: float = DEVIS["plafond_usd"]) -> dict:
    """Arrêt dès que cumul + un quart d'heure de carte atteint la coupure (égalité comprise)."""
    if isinstance(cumul_usd, bool) or not isinstance(cumul_usd, (int, float)) or not math.isfinite(cumul_usd) \
            or cumul_usd < 0:
        raise GardeArret(f"cumul illisible : {cumul_usd!r}")
    projete = float(cumul_usd) + QUART_D_HEURE_H * _positif(prix_usd_h, "prix")
    if projete >= _positif(coupure_usd, "coupure"):
        raise GardeArret(f"dépense : {cumul_usd:.2f} + un quart d'heure = {projete:.2f} ≥ coupure {coupure_usd:.2f} USD : "
                         "arrêt, versement, puis destruction par l'identifiant")
    return {"cumul": float(cumul_usd), "projete": projete, "coupure": float(coupure_usd)}


def charger_garde_de_calcul(racine: Path):
    chemin = Path(racine) / ".claude" / "hooks" / "garde_calcul.py"
    if not chemin.is_file():
        raise GardeArret(f"garde de calcul absente : {chemin}")
    spec = importlib.util.spec_from_file_location("garde_calcul_dopamine", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def exiger_garde_de_calcul(racine: Path, commande: str, aujourd_hui: date) -> None:
    """Rejoue la décision de la garde de calcul sur la commande imprimée ; un blocage devient un refus."""
    g = charger_garde_de_calcul(racine)
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err):
            g.decider(commande, aujourd_hui, str(racine))
    except SystemExit as e:
        if e.code not in (0, None):
            raise GardeArret(f"garde de calcul : {err.getvalue().strip()}") from None


def _git(racine: Path, *args, binaire: bool = False):
    return subprocess.run(["git", "-C", str(racine), *args], capture_output=True, text=not binaire)


def exiger_commit_verse(racine: Path, commit: str) -> None:
    """Le commit de la course est connu et atteignable depuis une branche distante (l'instance le clone)."""
    if not re.fullmatch(r"[0-9a-f]{40}", str(commit)):
        raise GardeArret("commit de 40 signes hexadécimaux attendu")
    if _git(racine, "cat-file", "-e", f"{commit}^{{commit}}").returncode != 0:
        raise GardeArret(f"commit {commit[:12]} inconnu du dépôt")
    r = _git(racine, "branch", "-r", "--contains", commit)
    if r.returncode != 0 or not r.stdout.strip():
        raise GardeArret(f"commit {commit[:12]} sur aucune branche distante : pousser avant de partir")


def _chemin_depot(x: str | None, quoi: str) -> str:
    if x is None:
        return "-"
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", x) or ".." in x or x.startswith("/"):
        raise GardeArret(f"{quoi} : chemin du dépôt illisible")
    return x


def commande_de_creation(racine: Path, etape: str, offre: dict, commit: str, run_id: str, go_id: str,
                         aujourd_hui: date, maintenant_s: float, contextes: str | None = None,
                         liste_honnetes: str | None = None) -> str:
    """Commande de création, à jouer par la session de course. `contextes` et `liste_honnetes` : fichiers du dépôt
    (scellés, au commit) pour le bloc de relecture forcée ; absents, ce bloc ne part pas."""
    racine = Path(racine)
    exiger_etape(etape)
    if not _GO.match(str(go_id)):
        raise GardeArret(f"GO_ID {go_id!r} illisible : aucun départ sans accord")
    of = exiger_offre(offre)
    if not _RUN.match(str(run_id)) or not str(run_id).endswith(f"-etape-{etape}"):
        raise GardeArret(f"identifiant de course AAAAMMJJ-HHMMSS-…exploratoire…-etape-{etape} attendu")
    ctx, lst = _chemin_depot(contextes, "contextes"), _chemin_depot(liste_honnetes, "liste des épisodes honnêtes")
    if (ctx == "-") != (lst == "-"):
        raise GardeArret("contextes et liste des épisodes honnêtes : les deux ou aucun")
    exiger_commit_verse(racine, commit)
    am = _git(racine, "show", f"{commit}:{AMORCE}", binaire=True)
    if am.returncode != 0 or not am.stdout:
        raise GardeArret(f"amorce absente du commit {commit[:12]}")
    for f in (ctx, lst):
        if f != "-" and _git(racine, "cat-file", "-e", f"{commit}:{f}.sha256").returncode != 0:
            raise GardeArret(f"{f} sans empreinte compagnon au commit {commit[:12]}")
    h = horaires(maintenant_s, of["prix_usd_h"])
    b64 = base64.b64encode(am.stdout).decode("ascii")
    env = (f"-e ETAPE={etape} -e COMMIT={commit} -e RUN_ID={run_id} -e PRIX_USD_H={of['prix_usd_h']} "
           f"-e FIN_LANCEMENTS_UTC_S={h['fin_lancements_s']} -e DESTRUCTION_UTC_S={h['destruction_s']} "
           f"-e GO_ID={go_id} -e DEPOT_URL={DEPOT_URL} -e CONTEXTES={ctx} -e LISTE_HONNETES={lst} "
           f"-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN")
    cmd = (f"GO_ID={go_id} vastai create instance {of['id']} --raw --image {IMAGE} --disk {DISQUE_GO} --cancel-unavail "
           f"--label {etiquette(etape)} --env \"{env}\" --entrypoint bash --args -c "
           f"\"echo {b64} | base64 -d > /root/amorce_dopamine_v1.sh && bash /root/amorce_dopamine_v1.sh\"")
    exiger_garde_de_calcul(racine, cmd, aujourd_hui)
    return cmd


def _instances(liste: Path) -> list[dict]:
    brut = json.loads(Path(liste).read_text(encoding="utf-8"))
    brut = brut.get("instances", brut) if isinstance(brut, dict) else brut
    if not isinstance(brut, list):
        raise GardeArret("liste des instances illisible")
    return brut


def exiger_etiquette(liste: Path, ident: str, etape: str) -> dict:
    if not str(ident).isdigit():
        raise GardeArret("identifiant d'instance numérique attendu (R10)")
    trouvees = [x for x in _instances(liste) if str(x.get("id")) == str(ident)]
    if len(trouvees) != 1:
        raise GardeArret(f"instance {ident} absente ou en double dans la liste")
    if trouvees[0].get("label") != etiquette(etape):
        raise GardeArret(f"instance {ident} étiquetée {trouvees[0].get('label')!r}, {etiquette(etape)!r} attendu")
    return trouvees[0]


def exiger_versement(racine: Path, inventaire: Path, commit: str) -> dict:
    """Inventaire scellé ; chaque fichier marqué versé est au commit, à sa taille et à son empreinte ; le manifeste de la
    course aussi ; le commit est atteignable depuis la branche distante de sortie. Sinon : aucune destruction."""
    racine = Path(racine)
    verifier(inventaire)
    inv = json.loads(Path(inventaire).read_text(encoding="utf-8"))
    run_id = inv.get("run_id")
    if not isinstance(run_id, str) or not _RUN.match(run_id):
        raise GardeArret("inventaire : identifiant de course illisible")
    fichiers = inv.get("fichiers") or []
    verses = [f for f in fichiers if f.get("verse") is True]
    if not verses:
        raise GardeArret("inventaire sans fichier versé : rien de prouvé")
    for f in verses:
        r = _git(racine, "show", f"{commit}:{f['chemin']}", binaire=True)
        if r.returncode != 0:
            raise GardeArret(f"{f['chemin']} absent du commit {commit[:12]} : versement non prouvé, aucune destruction")
        if hashlib.sha256(r.stdout).hexdigest() != f["sha256"] or len(r.stdout) != f["octets"]:
            raise GardeArret(f"{f['chemin']} : empreinte ou taille au commit ≠ inventaire : aucune destruction")
    if _git(racine, "cat-file", "-e", f"{commit}:runs/{run_id}/manifeste.json").returncode != 0:
        raise GardeArret("manifeste de la course absent du commit : aucune destruction")
    r = _git(racine, "branch", "-r", "--contains", commit)
    if r.returncode != 0 or not any(l.strip().endswith(BRANCHE_SORTIE) for l in r.stdout.splitlines()):
        raise GardeArret(f"commit {commit[:12]} hors de la branche distante {BRANCHE_SORTIE} : aucune destruction")
    return {"verses": len(verses), "non_verses": len(fichiers) - len(verses), "commit": commit, "run_id": run_id}


def commande_de_destruction(racine: Path, ident: str, etape: str, liste: Path, inventaire: Path, commit: str,
                            go_id: str) -> str:
    if not _GO.match(str(go_id)):
        raise GardeArret("GO_ID illisible")
    exiger_etiquette(liste, ident, etape)
    exiger_versement(racine, inventaire, commit)
    return f"GO_ID={go_id} vastai destroy instance {ident} -y"


def absence_prouvee(liste: Path, ident: str, temoin: str) -> None:
    """La destruction se juge par la liste des instances, jamais par un code de sortie."""
    ids = {str(x.get("id")) for x in _instances(liste)}
    if str(temoin) not in ids:
        raise GardeArret("témoin absent de la liste : liste incomplète, absence non prouvée")
    if str(ident) in ids:
        raise GardeArret(f"instance {ident} encore présente")


def plan() -> dict:
    return {"mode": "exploratoire", "etapes": list(ETAPES), "etiquettes": {e: etiquette(e) for e in ETAPES},
            "branche_sortie": BRANCHE_SORTIE, "image": IMAGE, "disque_go": DISQUE_GO, "offre": OFFRE,
            "devis": DEVIS, "amorce": AMORCE, "marge_h": QUART_D_HEURE_H,
            "rappel": "aucune machine sans devis accordé ni GO de calcul ; ce lanceur imprime, il ne lance rien"}


def _main(argv: list[str]) -> int:
    try:
        if not argv:
            raise GardeArret("sous-commande attendue : plan, commande, depense, detruire, verifier-destruction")
        sc, a = argv[0], argv[1:]
        if sc == "plan" and not a:
            print(json.dumps(plan(), ensure_ascii=False, indent=1))
        elif sc == "commande" and len(a) in (5, 7):
            go = os.environ.get("GO_ID", "")
            if not go:
                raise GardeArret("GO_ID absent de l'environnement : aucun départ sans accord")
            offre = json.loads(Path(a[2]).read_text(encoding="utf-8"))
            ctx, lst = (a[5], a[6]) if len(a) == 7 else (None, None)
            print(commande_de_creation(Path(a[0]), a[1], offre, a[3], a[4], go, date.today(), time.time(), ctx, lst))
        elif sc == "depense" and len(a) == 2:
            print(json.dumps(garde_depense(float(a[0]), float(a[1]))))
        elif sc == "detruire" and len(a) == 6:
            go = os.environ.get("GO_ID", "")
            print(commande_de_destruction(Path(a[0]), a[1], a[2], Path(a[3]), Path(a[4]), a[5], go))
        elif sc == "verifier-destruction" and len(a) == 3:
            absence_prouvee(Path(a[0]), a[1], a[2])
            print("absence prouvée")
        else:
            raise GardeArret(f"sous-commande ou arguments illisibles : {sc} ({len(a)} arguments)")
    except (GardeArret, ValueError, OSError) as e:
        print(f"DOPAMINE REFUS : {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
