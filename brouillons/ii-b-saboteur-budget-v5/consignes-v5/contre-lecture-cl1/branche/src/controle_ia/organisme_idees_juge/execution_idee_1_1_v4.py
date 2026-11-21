"""Idée 1.1 — enchaînement du jeu, version 4 (n9 : `charger_sortie` arrête avec message sur un enregistrement
mal formé ; modules v4). Version 3 : enchaînement du jeu, version 3 (modules v3 ; fichiers gelés v3). Version 2 : enchaînement du jeu, version 2 (contre-lecture `8def0cf5…` : M1, M2, m2, m8 ; modules v2). Version 1 : enchaînement du jeu (préenregistrement scellé `3ffe1739…`, « Étapes » 1 à 4 ; liste d'arrêt).

- Tâches : (ligne, tranche de 50 répétitions) ; chaque tâche joue ses répétitions (`banc_idee_1_1_v1.jouer_repetition`,
  réductions de l'addendum), écrit sa tranche **scellée** (`lignes/<i>-<r0>.json`, et, pour les 20 premières répétitions,
  le journal entier des projections en `.npz` scellé) ; trois processus au plus, `nice -n 10` (posé par le lanceur) ;
- **reprise** : un run interrompu sans arrêt consigné (machine arrêtée, signal) se reprend sous le même identifiant :
  chaque tranche déjà écrite est vérifiée par son compagnon et sautée ; les autres sont jouées ; la borne de 48 heures se
  compte depuis le **premier** départ (inscrit au journal de départ) ; un `arret.json` présent interdit la reprise
  (exception dans une évaluation : arrêt du run entier, aucune lecture partielle, relance seulement sous un texte ou un
  addendum neuf) ; les réductions et le nombre de processus sont ceux du départ (aucune réduction après le début du jeu) ;
- gardes : durée murale > 48 h (arrêt, run invalide) ; appel réseau (interdit) ; mort d'un processus fils (arrêt) ;
- sortie : `sortie.json` (index des tranches et de leurs empreintes) scellé avant toute lecture.
"""
from __future__ import annotations

import json
import multiprocessing
import signal
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, motif_d_arret
from ..scellement import empreinte, sceller, verifier
from . import banc_idee_1_1_v2 as B
from . import execution_v1 as X1
from . import vue_v9_v1 as VV

DUREE_MAX_S = 48 * 3600
PROCESSUS_MAX = 3
TRANCHE = 50
PAS_ATTENTE_S = 5.0
DOSSIER_DIAG = Path("diag") / "organisme-idees-juge-v1"
NOM_RUN = "idee-1-1-poids-du-nul-v4"
NOMS_RUN_DE_CE_JEU = ("idee-1-1-poids-du-nul-v1", "idee-1-1-poids-du-nul-v2", "idee-1-1-poids-du-nul-v3",
                      "idee-1-1-poids-du-nul-v4")
installer_garde_reseau = X1.installer_garde_reseau

FICHIERS_GELES = (
    "src/controle_ia/__init__.py",
    "src/controle_ia/organisme_idees_juge/__init__.py",
    "src/controle_ia/organisme_idees_juge/juge_v1.py",
    "src/controle_ia/organisme_idees_juge/lois_v1.py",
    "src/controle_ia/organisme_idees_juge/execution_v1.py",
    "src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py",
    "src/controle_ia/organisme_idees_juge/oracle_v1.py",
    "src/controle_ia/organisme_idees_juge/rejeu_v1.py",
    "src/controle_ia/organisme_idees_juge/vue_v9_v1.py",
    "src/controle_ia/organisme_idees_juge/nul_limite_v1.py",
    "src/controle_ia/organisme_idees_juge/morceaux_par_coupe_v1.py",
    "src/controle_ia/organisme_idees_juge/projection_commun_v1.py",
    "src/controle_ia/organisme_idees_juge/projection_methodes_v1.py",
    "src/controle_ia/organisme_idees_juge/attaque_projection_extrait_v1.py",
    "src/controle_ia/organisme_idees_juge/projection_bras_v1.py",
    "src/controle_ia/organisme_idees_juge/banc_idee_1_1_v2.py",
    "src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v4.py",
    "src/controle_ia/organisme_idees_juge/mutations_idee_1_1_v4.py",
    "src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v4.py",
    "src/controle_ia/organisme_idees_juge/execution_idee_1_1_v4.py",
    "src/controle_ia/gardes.py",
    "src/controle_ia/scellement.py",
    "src/controle_ia/manifeste.py",
    "src/controle_ia/prereg.py",
    "scripts/jouer_idee_1_1_v4.py",
    "scripts/lire_idee_1_1_v4.py",
    "scripts/etape0_idee_1_1_v4.py",
    "tests/conftest.py",
    "src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v3.py",
    "src/controle_ia/organisme_idees_juge/mutations_idee_1_1_v3.py",
    "src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v3.py",
    "src/controle_ia/organisme_idees_juge/execution_idee_1_1_v3.py",
    "scripts/jouer_idee_1_1_v3.py",
    "scripts/lire_idee_1_1_v3.py",
    "scripts/etape0_idee_1_1_v3.py",
    "tests/test_organisme_idees_juge_idee_1_1_projection_v3.py",
    "tests/test_organisme_idees_juge_idee_1_1_gardes_v3.py",
    "tests/test_organisme_idees_juge_idee_1_1_banc_v3.py",
    "tests/test_organisme_idees_juge_idee_1_1_lecture_v3.py",
    "tests/test_organisme_idees_juge_idee_1_1_execution_v3.py",
    "tests/test_organisme_idees_juge_idee_1_1_bout_en_bout_v3.py",
    "docs/notes/organisme-idees-juge-v1/code-idee-1-1-v4/couples-v3-vers-v4.json",
    "tests/test_organisme_idees_juge_idee_1_1_projection_v4.py",
    "tests/test_organisme_idees_juge_idee_1_1_gardes_v4.py",
    "tests/test_organisme_idees_juge_idee_1_1_banc_v4.py",
    "tests/test_organisme_idees_juge_idee_1_1_lecture_v4.py",
    "tests/test_organisme_idees_juge_idee_1_1_execution_v4.py",
    "tests/test_organisme_idees_juge_idee_1_1_bout_en_bout_v4.py",
    "tests/test_organisme_idees_juge_idee_1_1_differentiel_v4.py",
)
# essais rejoués par le lanceur : ceux de la version 4 seulement (les essais v3 sont gelés comme sources du différentiel)
ESSAIS = tuple(f for f in FICHIERS_GELES if f.startswith("tests/test_") and f.endswith("_v4.py"))


class GardeDuree:
    def __init__(self, debut: float, limite_s: float = DUREE_MAX_S, horloge=time.time):
        self.debut, self.limite, self.horloge = debut, limite_s, horloge

    def ecoule(self) -> float:
        return self.horloge() - self.debut

    def verifier(self, ou: str = "") -> None:
        if self.ecoule() > self.limite:
            raise GardeArret(f"durée murale > {self.limite / 3600:.0f} h ({ou}) : arrêt ; run invalide, aucune lecture")


def taches(reductions=()) -> list[tuple[int, int, int]]:
    B.actifs_pour(0, 0, reductions)  # refuse une réduction hors de la règle
    return [(i, r0, min(r0 + TRANCHE, B.REPETITIONS)) for i in range(len(B.LIGNES)) for r0 in range(0, B.REPETITIONS, TRANCHE)]


def nom_tranche(i: int, r0: int) -> str:
    return f"{i:02d}-{r0:04d}"


def ecrire_json_scelle(chemin: Path, corps) -> str:
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(corps, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    return sceller(chemin)


def _journal_entier_npz(chemin: Path, journaux: dict) -> str:
    tableaux = {}
    for r, par_bras in journaux.items():
        for bras, proj in par_bras.items():
            for b, d in proj.items():
                for cle in ("tau", "v", "u", "c"):
                    tableaux[f"r{r}|{bras}|b{b}|{cle}"] = np.asarray(d[cle])
    with open(chemin, "xb") as f:
        np.savez_compressed(f, **tableaux)
    return sceller(chemin)


def _tache(args) -> dict:
    racine, i, r0, r1, reductions, dossier, run_id, manifeste_sha, debut = args
    garde = GardeDuree(debut)
    V = VV.charger()
    dossier = Path(dossier)
    t0 = time.time()
    recs, journaux = [], {}
    for r in range(r0, r1):
        garde.verifier(f"ligne {B.NOMS[i]}, répétition {r}")
        rec, rep = B.jouer_repetition(V, racine, i, r, reductions=reductions)
        recs.append(rec)
        if getattr(rep, "journal_entier", None):
            journaux[r] = rep.journal_entier
    corps = {"run_id": run_id, "manifeste_sha256": manifeste_sha, "ligne": B.NOMS[i], "i_ligne": i, "r0": r0, "r1": r1,
             "reductions": list(reductions), "repetitions": recs, "duree_s": round(time.time() - t0, 2)}
    sha = ecrire_json_scelle(dossier / "lignes" / f"{nom_tranche(i, r0)}.json", corps)
    sortie = {"i": i, "r0": r0, "r1": r1, "sha256": sha, "duree_s": corps["duree_s"]}
    if journaux:
        sortie["journal_npz_sha256"] = _journal_entier_npz(dossier / "lignes" / f"{nom_tranche(i, r0)}-journal.npz", journaux)
    return sortie


def _init_fils() -> None:
    signal.signal(signal.SIGTERM, signal.SIG_DFL)


def _identites(pool) -> set:
    fils = getattr(pool, "_pool", None)
    if fils is None:
        raise GardeArret("multiprocessing : liste des processus fils illisible : arrêt")
    return {p.pid for p in fils}


def _carte(processus, fonction, liste, garde: GardeDuree, pas=PAS_ATTENTE_S):
    if not 1 <= processus <= PROCESSUS_MAX:
        raise GardeArret(f"{processus} processus : trois au plus (texte, étape 3)")
    if processus == 1:
        for t in liste:
            garde.verifier("tâche")
            yield fonction(t)
        return
    with multiprocessing.get_context("fork").Pool(processus, initializer=_init_fils, maxtasksperchild=None) as pool:
        ids = _identites(pool)
        it = pool.imap_unordered(fonction, liste)
        for _ in range(len(liste)):
            while True:
                garde.verifier("attente d'un processus fils")
                try:
                    r = it.next(timeout=pas)
                    break
                except multiprocessing.TimeoutError:
                    if _identites(pool) != ids:
                        raise GardeArret("un processus fils est mort (tâche perdue) : arrêt du run ; run invalide") from None
            yield r


def tranches_deja_ecrites(dossier: Path) -> dict:
    """Reprise : {(i, r0): empreinte} des tranches scellées ; une tranche sans compagnon ou altérée arrête."""
    sortie = {}
    d = Path(dossier) / "lignes"
    if not d.is_dir():
        return sortie
    for p in sorted(d.glob("*.json")):
        sha = verifier(p)
        corps = json.loads(p.read_text(encoding="utf-8"))
        sortie[(int(corps["i_ligne"]), int(corps["r0"]))] = {"sha256": sha, "r1": int(corps["r1"])}
    for p in sorted(d.glob("*")):
        if not (p.name.endswith(".json") or p.name.endswith(".npz") or p.name.endswith(".sha256")):
            raise GardeArret(f"reprise : fichier inattendu {p}")
        if p.suffix == ".npz":
            verifier(p)
    return sortie


def executer(*, racine: int, dossier: Path, run_id: str, manifeste_sha: str, processus: int, reductions,
             debut: float, journal: dict, liste=None) -> dict:
    dossier = Path(dossier)
    if (dossier / "arret.json").exists():
        raise GardeArret("arrêt consigné : reprise interdite (relance seulement sous un texte ou un addendum neuf)")
    if (dossier / "sortie.json").exists():
        raise GardeArret("sortie déjà scellée : rien à reprendre")
    garde = GardeDuree(debut)
    toutes = taches(reductions) if liste is None else list(liste)
    faites = tranches_deja_ecrites(dossier)
    a_faire = [t for t in toutes if (t[0], t[1]) not in faites]
    journal.setdefault("reprises", []).append({"utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                                "tranches_deja_ecrites": len(faites), "a_faire": len(a_faire)})
    args = [(racine, i, r0, r1, tuple(reductions), str(dossier), run_id, manifeste_sha, debut) for i, r0, r1 in a_faire]
    resultats = list(_carte(processus, _tache, args, garde))
    faites = tranches_deja_ecrites(dossier)
    manquantes = [t for t in toutes if (t[0], t[1]) not in faites]
    if manquantes:
        raise GardeArret(f"tranches manquantes après le jeu : {manquantes[:5]}… : run invalide")
    index = {"run_id": run_id, "manifeste_sha256": manifeste_sha, "reductions": list(reductions), "processus": processus,
             "tranches": {nom_tranche(i, r0): faites[(i, r0)]["sha256"] for i, r0, _ in toutes},
             "ecoule_s": round(garde.ecoule(), 1), "journal": journal,
             "durees_tranches_s": sorted(r["duree_s"] for r in resultats)}
    sha = ecrire_json_scelle(dossier / "sortie.json", index)
    return {"sortie_sha256": sha, "dossier": str(dossier), "tranches": len(toutes)}


def consigner_arret(dossier: Path, e: BaseException, run_id: str, manifeste_sha: str, journal: dict) -> Path:
    corps = {"run_id": run_id, "manifeste_sha256": manifeste_sha, "motif": motif_d_arret(e), "journal": journal,
             "regle": "arrêt du run entier ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf"}
    chemin = Path(dossier) / "arret.json"
    ecrire_json_scelle(chemin, corps)
    return chemin


def charger_sortie(dossier: Path) -> dict:
    """Lecture : refuse une sortie non scellée, une tranche non scellée ou différente de l'index."""
    dossier = Path(dossier)
    if (dossier / "arret.json").exists():
        raise GardeArret("arrêt consigné : aucune lecture partielle")
    sha = verifier(dossier / "sortie.json")
    index = json.loads((dossier / "sortie.json").read_text(encoding="utf-8"))
    donnees = {n: [] for n in B.NOMS}
    for nom, h in sorted(index["tranches"].items()):
        p = dossier / "lignes" / f"{nom}.json"
        if verifier(p) != h:
            raise GardeArret(f"tranche {nom} différente de l'index scellé : lecture refusée")
        corps = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(corps, dict) or corps.get("ligne") not in donnees or not isinstance(corps.get("repetitions"), list):
            raise GardeArret(f"tranche {nom} mal formée : lecture refusée")
        donnees[corps["ligne"]].extend(corps["repetitions"])
    for n, recs in donnees.items():
        if not all(isinstance(r, dict) and "r" in r for r in recs):           # v4, n9 : arrêt avec message, jamais une trace
            raise GardeArret(f"ligne {n} : enregistrement sans champ « r » : lecture refusée")
        if [r["r"] for r in recs] != list(range(len(recs))) or len(recs) != B.REPETITIONS:
            raise GardeArret(f"ligne {n} : répétitions incomplètes ou hors d'ordre : lecture refusée")
    return {"index": index, "index_sha256": sha, "donnees": donnees}


# --- addendum d'empreintes --------------------------------------------------------------------------------------------------
DEBUT_PROGRAMME, FIN_PROGRAMME = "<!-- programme-du-jeu-idee-1-1 -->", "<!-- fin-programme-du-jeu-idee-1-1 -->"


def lister_empreintes(racine_depot: Path) -> str:
    return "".join(f"{empreinte(Path(racine_depot) / f)}  {f}\n" for f in FICHIERS_GELES)


def lire_addendum(racine_depot: Path, chemin: Path) -> dict:
    """Addendum scellé : chaque fichier gelé listé et intact (« <sha256>  <chemin> ») ; bloc programme (JSON entre les
    marqueurs) : processus, réductions, fichier d'étape 0 (chemin, empreinte). La règle de réduction est **rejouée** sur
    le chronométrage du fichier d'étape 0 : une réduction hors de la règle rend le run invalide."""
    import re

    from . import etape0_idee_1_1_v4 as E0
    verifier(chemin)
    texte = Path(chemin).read_text(encoding="utf-8")
    liste = X1.verifier_addendum(racine_depot, chemin, FICHIERS_GELES)
    m = re.search(re.escape(DEBUT_PROGRAMME) + r"\s*```json\s*(\{.*?\})\s*```\s*" + re.escape(FIN_PROGRAMME), texte, flags=re.S)
    if not m:
        raise GardeArret("addendum sans bloc programme : pas de jeu (chronométrage absent de l'addendum)")
    prog = json.loads(m.group(1))
    e0 = Path(racine_depot) / prog["etape0"]["chemin"]
    if verifier(e0) != prog["etape0"]["sha256"]:
        raise GardeArret("fichier d'étape 0 différent de l'addendum : pas de jeu")
    res0 = json.loads(e0.read_text(encoding="utf-8"))
    for cle in ("resultat", "fichiers_geles"):          # m2 : clés exigées, aucune valeur par défaut
        if cle not in res0:
            raise GardeArret(f"fichier d'étape 0 sans « {cle} » : pas de jeu")
    corps0 = res0["resultat"]
    for cle in ("bloquants", "jeu_permis", "preenregistrement", "chronometrage"):
        if cle not in corps0:
            raise GardeArret(f"fichier d'étape 0 sans « {cle} » : pas de jeu")
    if corps0["bloquants"] or corps0["jeu_permis"] is not True:
        raise GardeArret(f"étape 0 : bloquants inscrits : {corps0['bloquants']} : pas de jeu")
    # M2 : l'étape 0 vaut pour le code gelé — égalité, fichier par fichier, avec l'addendum ; et pour ce texte
    if corps0["preenregistrement"].get("sha256") != B.EMPREINTE_PREREG:
        raise GardeArret("fichier d'étape 0 d'un autre texte : pas de jeu")
    fg = res0["fichiers_geles"]
    if set(fg) != set(FICHIERS_GELES):
        raise GardeArret("fichier d'étape 0 : liste des fichiers gelés ≠ celle du code : pas de jeu (étape 0 à rejouer)")
    differents = [f for f in FICHIERS_GELES if fg[f] != liste[f]]
    if differents:
        raise GardeArret(f"étape 0 passée sur un autre code ({differents[:5]}…) : pas de jeu (étape 0 à rejouer)")
    if "chronometrage" not in corps0:
        raise GardeArret("chronométrage de l'étape 0 absent : pas de jeu ; texte neuf")
    rejoue = E0.regle_de_reduction(corps0["chronometrage"]["secondes_par_repetition"], int(prog["processus"]))
    if rejoue["reductions"] != list(prog["reductions"]) or not rejoue["jeu_permis"]:
        raise GardeArret(f"réductions de l'addendum {prog['reductions']} ≠ règle rejouée {rejoue['reductions']} : run invalide")
    return {"fichiers": liste, "programme": prog, "regle_rejouee": rejoue}


# ==================================================================================================================
# Version 2 (contre-lecture `8def0cf5…`) : M1 (addendum du manifeste relu par la lecture), m8 (reprise et dépôt propre).
def verifier_addendum_du_manifeste(racine_depot: Path, config: dict) -> dict:
    """M1 : l'addendum inscrit au manifeste est relu (empreinte égale à celle du manifeste), chaque fichier gelé
    revérifié par `lire_addendum`, et le bloc programme égal à celui du manifeste ; sinon la lecture est refusée."""
    add = config.get("addendum")
    if not add or "chemin" not in add or "sha256" not in add:
        raise GardeArret("manifeste sans addendum : lecture refusée")
    chemin = Path(racine_depot) / add["chemin"]
    if verifier(chemin) != add["sha256"]:
        raise GardeArret("addendum différent de celui du manifeste : lecture refusée")
    lu = lire_addendum(racine_depot, chemin)
    if lu["programme"] != add.get("programme"):
        raise GardeArret("bloc programme de l'addendum ≠ celui du manifeste : lecture refusée")
    return lu


def exiger_depot_propre_sauf_run(racine_depot: Path, run_id: str) -> None:
    """m8 : en reprise, l'arbre doit être propre hors des seuls dossiers `runs/<run_id>/` et `diag/…/<run_id>/` du run
    repris (non suivis tant que la sortie n'est pas committée) ; tout autre changement refuse la reprise."""
    from ..gardes import etat_git
    permis = (f"runs/{run_id}/", f"{DOSSIER_DIAG.as_posix()}/{run_id}/")
    etat = etat_git(racine_depot)
    autres = []
    for ligne in etat["statut"].splitlines():
        chemin = ligne[3:].strip().strip('"')
        if not any(chemin.startswith(p) for p in permis):
            autres.append(ligne)
    if autres:
        raise GardeArret("arbre de travail non propre hors des dossiers du run repris : reprise refusée\n" + "\n".join(autres[:20]))
