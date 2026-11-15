"""Enchaînement du jeu de l'idée 1.2 (section « Étapes » du texte scellé) et gardes de la liste d'arrêt.

Étapes : (1) contrôles avant jeu (empreintes, essais, mutations ; aucune sortie existante) ; (2) essai E1 ; (3) oracle
calculé et **scellé** pour toutes les générations, avant le rejeu ; (4) jeu (1 250 générations, `nice -n 10`, deux
processus au plus) ; (5) sortie scellée avant toute lecture, sous `diag/organisme-idees-juge-v1/<run>/`. La lecture gelée
(étape 6) est un programme à part (`lire_banc_tirages_repartis_v1`), qui refuse une sortie non scellée.

Gardes : durée murale > 24 h (arrêt, run invalide) ; tout appel réseau (interdit, R-2851) ; exception ou log W non fini
(arrêt du run, `arret.json` scellé, aucune lecture partielle) ; oracle non scellé, ou modifié, au moment du rejeu (run
invalide) ; sortie existante (R12).
"""
from __future__ import annotations

import json
import multiprocessing
import os
import socket
import time
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret, motif_d_arret
from ..scellement import empreinte, sceller, verifier
from . import banc_tirages_repartis_v1 as B
from . import juge_v1
from . import oracle_v1 as O
from . import rejeu_v1 as R

DUREE_MAX_S = 24 * 3600
PROCESSUS_MAX = 2
DOSSIER_DIAG = Path("diag") / "organisme-idees-juge-v1"
NOM_RUN = "idee-1-2-tirages-repartis-v1"
FICHIERS_GELES = (
    "src/controle_ia/organisme_idees_juge/__init__.py",
    "src/controle_ia/organisme_idees_juge/juge_v1.py",
    "src/controle_ia/organisme_idees_juge/lois_v1.py",
    "src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py",
    "src/controle_ia/organisme_idees_juge/oracle_v1.py",
    "src/controle_ia/organisme_idees_juge/rejeu_v1.py",
    "src/controle_ia/organisme_idees_juge/synthetique_v1.py",
    "src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v1.py",
    "src/controle_ia/organisme_idees_juge/mutations_v1.py",
    "src/controle_ia/organisme_idees_juge/execution_v1.py",
    "scripts/jouer_idee_1_2_v1.py",
    "scripts/lire_idee_1_2_v1.py",
    "tests/test_organisme_idees_juge_lois_v1.py",
    "tests/test_organisme_idees_juge_banc_v1.py",
    "tests/test_organisme_idees_juge_rejeu_v1.py",
    "tests/test_organisme_idees_juge_lecture_v1.py",
    "tests/test_organisme_idees_juge_mutations_v1.py",
    "tests/test_organisme_idees_juge_execution_v1.py",
)


# --- gardes ------------------------------------------------------------------------------------------------------------
class GardeDuree:
    def __init__(self, limite_s: float = DUREE_MAX_S, horloge=time.monotonic, debut: float | None = None):
        self.limite, self.horloge = limite_s, horloge
        self.debut = horloge() if debut is None else debut

    def ecoule(self) -> float:
        return self.horloge() - self.debut

    def verifier(self, ou: str = "") -> None:
        if self.ecoule() > self.limite:
            raise GardeArret(f"durée murale > {self.limite / 3600:.0f} h ({ou}) : arrêt ; run invalide")


def _refus_reseau(*args, **kwargs):
    raise GardeArret("appel réseau pendant le jeu : interdit (processeur seul, sans dépense, R-2851)")


def installer_garde_reseau() -> dict:
    """Toute connexion sortante lève `GardeArret` dans ce processus et ses fils (bifurcation)."""
    anciens = {"connect": socket.socket.connect, "connect_ex": socket.socket.connect_ex,
               "create_connection": socket.create_connection, "getaddrinfo": socket.getaddrinfo}
    socket.socket.connect = _refus_reseau
    socket.socket.connect_ex = _refus_reseau
    socket.create_connection = _refus_reseau
    socket.getaddrinfo = _refus_reseau
    return anciens


def retirer_garde_reseau(anciens: dict) -> None:
    socket.socket.connect = anciens["connect"]
    socket.socket.connect_ex = anciens["connect_ex"]
    socket.create_connection = anciens["create_connection"]
    socket.getaddrinfo = anciens["getaddrinfo"]


def ecrire_scelle(dossier: Path, nom: str, resultat, run_id: str, manifeste_sha: str) -> tuple[Path, str]:
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / f"{nom}.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    corps = {"run_id": run_id, "manifeste_sha256": manifeste_sha, "resultat": resultat}
    chemin.write_text(json.dumps(corps, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    return chemin, sceller(chemin)


def verifier_addendum(racine_depot: Path, chemin_addendum: Path, fichiers=FICHIERS_GELES) -> dict:
    """L'addendum d'empreintes (scellé) liste « <sha256>  <chemin> » ; chaque fichier gelé doit y être, intact."""
    import re

    verifier(chemin_addendum)
    lignes = re.findall(r"^([0-9a-f]{64})  (\S+)\s*$", Path(chemin_addendum).read_text(encoding="utf-8"), flags=re.M)
    liste = {}
    for h, p in lignes:
        if p in liste and liste[p] != h:
            raise GardeArret(f"addendum : deux empreintes pour {p}")
        liste[p] = h
    manquants = [f for f in fichiers if f not in liste]
    if manquants:
        raise GardeArret(f"addendum : fichiers gelés absents de la liste : {manquants}")
    for p, h in liste.items():
        obtenu = empreinte(racine_depot / p)
        if obtenu != h:
            raise GardeArret(f"un fichier gelé diffère de l'addendum : {p} ({obtenu[:12]}… ≠ {h[:12]}…) : pas de jeu")
    return liste


def lister_empreintes(racine_depot: Path, fichiers=FICHIERS_GELES) -> str:
    return "".join(f"{empreinte(racine_depot / f)}  {f}\n" for f in fichiers)


# --- tâches par génération (processus fils) ------------------------------------------------------------------------------
def _tache_oracle(args):
    racine, famille, g, horloge_debut = args
    GardeDuree(debut=horloge_debut, horloge=time.time).verifier(f"oracle {famille}{g}")
    t0 = time.time()
    J = juge_v1.charger()
    gen = B.Generation(racine, famille, g)
    table = O.table_oracle(J, gen)
    table["construction"] = gen.resume()
    table["duree_s"] = time.time() - t0
    return table


def jouer_generation_banc(J, gen: "B.Generation") -> dict:
    """Plans, gel des 24 engagements, issues fraîches, évaluation par le juge réel (ordre gelé, [CL-1.1] m1)."""
    gen.preparer_engagements(J)
    gen.geler()
    gen.tirer_frais(J)
    return gen.evaluer(J)


def _tache_jeu(args):
    racine, famille, g, empreintes_oracle, oracle_sha, horloge_debut = args
    GardeDuree(debut=horloge_debut, horloge=time.time).verifier(f"jeu {famille}{g}")
    t0 = time.time()
    J = juge_v1.charger()
    gen = B.Generation(racine, famille, g)
    if [c.empreinte for c in gen.cartes] != empreintes_oracle:
        raise GardeArret(f"{gen.nom} : cartes rebâties ≠ cartes de l'oracle scellé (construction non déterministe)")
    evaluations = jouer_generation_banc(J, gen)
    t_eval = time.time() - t0
    cartes = []
    lam = gen.log_lambda(J) if famille == "N" else None
    for c in gen.cartes:
        d = {"indice": c.indice, "sorte": c.sorte, "empreinte_loi": c.empreinte,
             "trajectoire": list(evaluations[c.indice]["trajectoire_log_w"])}
        if lam is not None:
            d["log_lambda"] = lam[c.indice]
            d["dominations"] = B.domination(d["trajectoire"], d["log_lambda"])
        cartes.append(d)
    bras = R.rejouer_generation(J, evaluations, gen.positions, racine, famille, g)
    det = gen.monde.details
    return {"famille": famille, "g": g, "cellule": det["cellule"], "type": det["type"], "dose": det["dose"],
            "dose_haute": det["dose_haute"], "monde": det.get("monde"), "positions": gen.positions,
            "oracle_scelle_sha256": oracle_sha, "cartes": cartes, "bras": bras,
            "duree_s": time.time() - t0, "duree_evaluations_s": t_eval}


_GENS_E1: dict = {}


def _tache_E1(args):
    racine, famille, g, i, horloge_debut = args
    GardeDuree(debut=horloge_debut, horloge=time.time).verifier(f"E1 {famille}{g} carte {i}")
    t0 = time.time()
    J = juge_v1.charger()
    cle = (racine, famille, g)
    if cle not in _GENS_E1:
        gen = B.Generation(racine, famille, g)
        gen.preparer_engagements(J)
        gen.geler()
        gen.tirer_frais(J)
        _GENS_E1.clear()
        _GENS_E1[cle] = gen
    r = B.essai_E1_carte(J, _GENS_E1[cle], i)
    r["duree_s"] = time.time() - t0
    return r


def _carte(processus: int, tache, taches):
    if processus < 1 or processus > PROCESSUS_MAX:
        raise GardeArret(f"{processus} processus : deux au plus (texte scellé, étape 4)")
    if processus == 1:
        for t in taches:
            yield tache(t)
        return
    with multiprocessing.get_context("fork").Pool(processus) as pool:
        yield from pool.imap(tache, taches)


# --- enchaînement -------------------------------------------------------------------------------------------------------
def executer(*, racine: int, generations: dict, dossier_sortie: Path, run_id: str, manifeste_sha: str,
             processus: int = PROCESSUS_MAX, cartes_E1=B.CARTES_E1, controles: dict | None = None,
             garde: GardeDuree | None = None, journal: dict | None = None) -> dict:
    """Étapes 2 à 5 ; `controles` (étape 1, faite par le lanceur) est versé dans `controles-avant-jeu.json`."""
    garde = garde or GardeDuree(horloge=time.time)
    journal = journal if journal is not None else {}
    journal.setdefault("phases", [])
    dossier_sortie = Path(dossier_sortie)
    debut = garde.debut

    def phase(nom):
        garde.verifier(nom)
        journal["phases"].append({"phase": nom, "debut_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                  "ecoule_s": round(garde.ecoule(), 3)})

    # étape 2 : essai E1
    phase("E1")
    e1 = list(_carte(processus, _tache_E1, [(racine, f, g, i, debut) for f, g, i in cartes_E1]))
    echecs = [r for r in e1 if r["echecs"]]
    controles = dict(controles or {})
    controles["E1"] = {"cartes": len(e1), "sortes": sorted({(r["generation"][0], r["sorte"]) for r in e1}),
                       "echecs": echecs, "durees_s": [r["duree_s"] for r in e1]}
    _, sha_c = ecrire_scelle(dossier_sortie, "controles-avant-jeu", controles, run_id, manifeste_sha)
    journal["controles_sha256"] = sha_c
    if echecs:
        raise GardeArret(f"essai E1 : préfixe non égal à un instant ({len(echecs)} carte(s)) : arrêt avant le jeu")
    # étape 3 : oracle, scellé avant le rejeu
    phase("oracle")
    taches = [(racine, f, g, debut) for f in ("N", "T") for g in generations[f]]
    tables = []
    for t in _carte(processus, _tache_oracle, taches):
        garde.verifier("oracle")
        tables.append(t)
    chemin_o, sha_o = ecrire_scelle(dossier_sortie, "oracle", {"generations": tables}, run_id, manifeste_sha)
    journal["oracle_sha256"] = sha_o
    journal["oracle_scelle_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    # étape 4 : jeu (l'oracle doit être scellé et intact au départ du rejeu et à sa fin)
    phase("jeu")
    if verifier(chemin_o) != sha_o:
        raise GardeArret("oracle non scellé au départ du rejeu : run invalide")
    empreintes = {(t["famille"], t["g"]): [c["empreinte_loi"] for c in t["cartes"]] for t in tables}
    taches = [(racine, f, g, empreintes[(f, g)], sha_o, debut) for f in ("N", "T") for g in generations[f]]
    gens = []
    for r in _carte(processus, _tache_jeu, taches):
        garde.verifier("jeu")
        gens.append(r)
    if verifier(chemin_o) != sha_o:
        raise GardeArret("oracle modifié pendant le rejeu : run invalide")
    # étape 5 : sortie scellée avant toute lecture
    phase("sortie")
    _, sha_j = ecrire_scelle(dossier_sortie, "jeu", {"generations": gens}, run_id, manifeste_sha)
    journal["jeu_sha256"] = sha_j
    durees = [g["duree_s"] for g in gens]
    journal["duree_par_generation_s"] = {"moyenne": sum(durees) / len(durees), "min": min(durees), "max": max(durees),
                                         "n": len(durees)}
    journal["duree_oracle_par_generation_s"] = sum(t["duree_s"] for t in tables) / len(tables)
    journal["duree_E1_par_carte_s"] = sum(controles["E1"]["durees_s"]) / max(1, len(controles["E1"]["durees_s"]))
    journal["ecoule_total_s"] = round(garde.ecoule(), 3)
    _, sha_jr = ecrire_scelle(dossier_sortie, "journal", journal, run_id, manifeste_sha)
    return {"oracle": sha_o, "jeu": sha_j, "journal": sha_jr, "controles": sha_c, "dossier": str(dossier_sortie)}


def consigner_arret(dossier_sortie: Path, e: BaseException, run_id: str, manifeste_sha: str, journal: dict) -> Path:
    corps = {"motif": motif_d_arret(e), "journal": journal,
             "regle": "arrêt du run ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf (R5)"}
    chemin, _ = ecrire_scelle(Path(dossier_sortie), "arret", corps, run_id, manifeste_sha)
    return chemin


def generations_du_texte() -> dict:
    return {"N": list(range(B.GENERATIONS["N"])), "T": list(range(B.GENERATIONS["T"]))}


def generations_miniature(n_T: int, n_N: int) -> dict:
    """Répétition miniature : n_T générations T (cellules 0, 1, …) ; n_N générations N, moitié M₀, moitié M₀′."""
    a = (n_N + 1) // 2
    return {"T": list(range(n_T)), "N": list(range(a)) + list(range(B.BORNE_M0, B.BORNE_M0 + n_N - a))}
