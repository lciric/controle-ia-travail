"""Enchaînement du jeu de l'idée 1.2, version 2 (contre-lecture du code `36ecc4a4…`, R-2899). Reprend `execution_v1`
(gardes de durée et de réseau, écriture scellée, addendum, tâches E1) et change :

- **attente bornée sur les processus fils** (majeur 1) : le parent ne bloque jamais plus de `pas` secondes sans relire
  la garde des 24 h ; la mort d'un processus fils (ses fils de travail changent d'identité : `Pool` remplace un fils
  mort, une tâche est alors perdue) lève `GardeArret` à la relecture suivante ; la sortie du bloc `with` termine les
  fils ; les fils ignorent le signal TERM du lanceur (rétabli au défaut) ;
- **constantes du texte** exigées au départ et dans chaque tâche (`verificateur_texte_v2.exiger_constantes_du_texte`) ;
- **troisième écriture** de chaque bras, de la valeur e et de e-BH sur chaque génération jouée
  (`verificateur_texte_v2.verifier_generation`) ;
- **oracle v2** (membres du nul à la borne triviale signalés).
"""
from __future__ import annotations

import multiprocessing
import signal
import time
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import verifier
from . import banc_tirages_repartis_v1 as B
from . import execution_v1 as X1
from . import juge_v1
from . import oracle_v2 as O2
from . import verificateur_texte_v2 as VT

DUREE_MAX_S, PROCESSUS_MAX = X1.DUREE_MAX_S, X1.PROCESSUS_MAX
DOSSIER_DIAG, NOM_RUN = X1.DOSSIER_DIAG, X1.NOM_RUN
PAS_ATTENTE_S = 5.0
GardeDuree, installer_garde_reseau, retirer_garde_reseau = X1.GardeDuree, X1.installer_garde_reseau, X1.retirer_garde_reseau
ecrire_scelle, consigner_arret = X1.ecrire_scelle, X1.consigner_arret
generations_du_texte, generations_miniature = X1.generations_du_texte, X1.generations_miniature

FICHIERS_GELES = (
    # code de la v1 encore employé (inchangé, scellé)
    *[f for f in X1.FICHIERS_GELES if not f.startswith("tests/")],
    # code neuf de la v2
    "src/controle_ia/organisme_idees_juge/verificateur_texte_v2.py",
    "src/controle_ia/organisme_idees_juge/oracle_v2.py",
    "src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py",
    "src/controle_ia/organisme_idees_juge/mutations_v2.py",
    "src/controle_ia/organisme_idees_juge/execution_v2.py",
    "scripts/jouer_idee_1_2_v2.py",
    "scripts/lire_idee_1_2_v2.py",
    # infrastructure importée (mineur 8)
    "src/controle_ia/gardes.py", "src/controle_ia/scellement.py", "src/controle_ia/manifeste.py", "src/controle_ia/prereg.py",
    # essais : ceux de la v1 et ceux de la v2
    *[f for f in X1.FICHIERS_GELES if f.startswith("tests/")],
    "tests/test_organisme_idees_juge_constantes_v2.py",
    "tests/test_organisme_idees_juge_lecture_v2.py",
    "tests/test_organisme_idees_juge_mutations_v2.py",
    "tests/test_organisme_idees_juge_execution_v2.py",
    "tests/conftest.py",
)
ESSAIS = tuple(f for f in FICHIERS_GELES if f.startswith("tests/test_"))


def verifier_addendum(racine_depot: Path, chemin_addendum: Path) -> dict:
    return X1.verifier_addendum(racine_depot, chemin_addendum, FICHIERS_GELES)


def lister_empreintes(racine_depot: Path) -> str:
    return X1.lister_empreintes(racine_depot, FICHIERS_GELES)


# --- processus fils : attente bornée -------------------------------------------------------------------------------------
def _init_fils() -> None:
    signal.signal(signal.SIGTERM, signal.SIG_DFL)    # le fils se laisse terminer ; seul le parent consigne l'arrêt


def _identites_des_fils(pool) -> set:
    fils = getattr(pool, "_pool", None)
    if fils is None:
        raise GardeArret("multiprocessing : liste des processus fils illisible (attribut _pool absent) : arrêt")
    return {p.pid for p in fils}


def _carte(processus: int, tache, taches, garde: "X1.GardeDuree", pas: float = PAS_ATTENTE_S):
    taches = list(taches)
    if processus < 1 or processus > PROCESSUS_MAX:
        raise GardeArret(f"{processus} processus : deux au plus (texte scellé, étape 4)")
    if processus == 1:
        for t in taches:
            garde.verifier("tâche")
            yield tache(t)
        return
    with multiprocessing.get_context("fork").Pool(processus, initializer=_init_fils) as pool:
        fils = _identites_des_fils(pool)
        resultats = pool.imap(tache, taches)
        for _ in range(len(taches)):
            while True:
                garde.verifier("attente d'un processus fils")
                try:
                    r = resultats.next(timeout=pas)
                    break
                except multiprocessing.TimeoutError:
                    if _identites_des_fils(pool) != fils:
                        raise GardeArret("un processus fils est mort (tâche perdue) : arrêt du run ; run invalide") from None
            if _identites_des_fils(pool) != fils:
                raise GardeArret("un processus fils est mort (tâche perdue) : arrêt du run ; run invalide")
            yield r


# --- tâches -------------------------------------------------------------------------------------------------------------
def _tache_oracle(args):
    racine, famille, g, horloge_debut = args
    X1.GardeDuree(debut=horloge_debut, horloge=time.time).verifier(f"oracle {famille}{g}")
    VT.exiger_constantes_du_texte()
    t0 = time.time()
    J = juge_v1.charger()
    gen = B.Generation(racine, famille, g)
    table = O2.table_oracle(J, gen)
    table["construction"] = gen.resume()
    table["duree_s"] = time.time() - t0
    return table


def _tache_jeu(args):
    VT.exiger_constantes_du_texte()
    r = X1._tache_jeu(args)
    VT.verifier_generation(r, args[0])
    return r


def _tache_E1(args):
    VT.exiger_constantes_du_texte()
    return X1._tache_E1(args)


def executer(*, racine: int, generations: dict, dossier_sortie: Path, run_id: str, manifeste_sha: str,
             processus: int = PROCESSUS_MAX, cartes_E1=B.CARTES_E1, controles: dict | None = None,
             garde: "X1.GardeDuree | None" = None, journal: dict | None = None, pas: float = PAS_ATTENTE_S) -> dict:
    """Étapes 2 à 5 du texte (E1, oracle scellé avant le rejeu, jeu, sortie scellée), comme la v1, avec l'attente bornée."""
    VT.exiger_constantes_du_texte()
    garde = garde or X1.GardeDuree(horloge=time.time)
    journal = journal if journal is not None else {}
    journal.setdefault("phases", [])
    journal["version_execution"] = 2
    dossier_sortie = Path(dossier_sortie)
    debut = garde.debut

    def phase(nom):
        garde.verifier(nom)
        journal["phases"].append({"phase": nom, "debut_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                  "ecoule_s": round(garde.ecoule(), 3)})

    def carte(tache, taches):
        return _carte(processus, tache, taches, garde, pas)

    phase("E1")
    e1 = list(carte(_tache_E1, [(racine, f, g, i, debut) for f, g, i in cartes_E1]))
    echecs = [r for r in e1 if r["echecs"]]
    controles = dict(controles or {})
    controles["E1"] = {"cartes": len(e1), "sortes": sorted({(r["generation"][0], r["sorte"]) for r in e1}),
                       "echecs": echecs, "durees_s": [r["duree_s"] for r in e1]}
    _, sha_c = ecrire_scelle(dossier_sortie, "controles-avant-jeu", controles, run_id, manifeste_sha)
    journal["controles_sha256"] = sha_c
    if echecs:
        raise GardeArret(f"essai E1 : préfixe non égal à un instant ({len(echecs)} carte(s)) : arrêt avant le jeu")
    phase("oracle")
    tables = list(carte(_tache_oracle, [(racine, f, g, debut) for f in ("N", "T") for g in generations[f]]))
    chemin_o, sha_o = ecrire_scelle(dossier_sortie, "oracle", {"generations": tables}, run_id, manifeste_sha)
    journal["oracle_sha256"] = sha_o
    journal["oracle_scelle_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    journal["oracle_membres_a_la_borne_triviale"] = sum(bool(t["membres_a_la_borne_triviale"]) for t in tables)
    phase("jeu")
    if verifier(chemin_o) != sha_o:
        raise GardeArret("oracle non scellé au départ du rejeu : run invalide")
    empreintes = {(t["famille"], t["g"]): [c["empreinte_loi"] for c in t["cartes"]] for t in tables}
    gens = list(carte(_tache_jeu, [(racine, f, g, empreintes[(f, g)], sha_o, debut) for f in ("N", "T") for g in generations[f]]))
    if verifier(chemin_o) != sha_o:
        raise GardeArret("oracle modifié pendant le rejeu : run invalide")
    phase("sortie")
    _, sha_j = ecrire_scelle(dossier_sortie, "jeu", {"generations": gens}, run_id, manifeste_sha)
    journal["jeu_sha256"] = sha_j
    durees = [g["duree_s"] for g in gens]
    journal["duree_par_generation_s"] = {"moyenne": sum(durees) / len(durees), "min": min(durees), "max": max(durees), "n": len(durees)}
    journal["duree_oracle_par_generation_s"] = sum(t["duree_s"] for t in tables) / len(tables)
    journal["duree_E1_par_carte_s"] = sum(controles["E1"]["durees_s"]) / max(1, len(controles["E1"]["durees_s"]))
    journal["ecoule_total_s"] = round(garde.ecoule(), 3)
    _, sha_jr = ecrire_scelle(dossier_sortie, "journal", journal, run_id, manifeste_sha)
    return {"oracle": sha_o, "jeu": sha_j, "journal": sha_jr, "controles": sha_c, "dossier": str(dossier_sortie)}
