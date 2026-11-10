"""Lanceur côté instance — témoin « attaque publiée reproduite » (Bailey et collègues), v1.

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : plan d'analyse (écarts, graines,
contrôles du juge, pilote, règle du nombre de tours, run principal, gardes), « Ce qui sort de l'instance ». Point 2 à 5
de la liste « ce qui manque à la condition 6 » de la contre-lecture du code (`151eee65…`).

Sous-commandes (chaque sortie va dans `--travail`, un dossier par exécution, neuf) :
- `mise-en-place` : gardes de mise en place autres que les contrôles du juge — commit et arbre du dépôt public, aucun
  fichier suivi modifié, empreintes des configurations et des six fichiers du jeu, graines du manifeste, mémoire vive,
  versions installées égales au manifeste ; longueur du suffixe au tokeniseur (écart 10), écrite au manifeste.
- `controle-juge` : contrôles du juge (négatif : 200 réponses sans suffixe par la génération publique ; positif :
  colonne `response`), garde du juge dans ce processus ; comptes écrits ; arrêt si hors seuil.
- `executer` : une exécution (pilote, run principal, reprise ou relance) du code public par `execution_v1`, surveillée.
- `regle-tours` : K par la règle, depuis t du pilote, B, D, c ; écrit au manifeste.
- `empreintes` : empreintes de tous les journaux d'une exécution, avant transfert.

Rien de ce module n'imprime une note. Les textes produits, les suffixes et les sondes restent sur l'instance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

from ..gardes import GardeArret
from . import analyse_v2 as an
from . import conventions_v1 as cv
from .execution_v1 import configuration_attendue, surcharges

MARK = re.compile(r"^MARK: Epoch (\d+) took ([0-9.]+) seconds\s*$")


def _ecrire_json(chemin: Path, objet) -> None:
    chemin.write_text(json.dumps(objet, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _ajouter(chemin: Path, objet) -> None:
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(objet, ensure_ascii=False, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def lire_manifeste(chemin) -> dict:
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


# --- mise en place ----------------------------------------------------------------------------------------------------

def _git(clone: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(clone), *args], check=True, capture_output=True, text=True).stdout.strip()


def garde_depot_public(clone: Path) -> str:
    if _git(clone, "rev-parse", "HEAD") != cv.COMMIT_PUBLIC:
        raise GardeArret("garde « dépôt public » tombée : commit")
    if _git(clone, "rev-parse", "HEAD^{tree}") != cv.ARBRE_PUBLIC:
        raise GardeArret("garde « dépôt public » tombée : arbre")
    if _git(clone, "status", "--porcelain", "--untracked-files=no"):
        raise GardeArret("garde « dépôt public » tombée : fichier suivi modifié")
    return "passée"


def garde_empreintes_publiques(clone: Path) -> str:
    racine = clone / cv.SOUS_DOSSIER
    for rel, attendue in cv.EMPREINTES_PUBLIQUES.items():
        if not (racine / rel).is_file() or cv.sha_fichier(racine / rel) != attendue:
            raise GardeArret(f"garde « empreintes » tombée : {rel}")
    return "passée"


def memoire_vive_go(meminfo: str | None = None) -> float:
    texte = Path("/proc/meminfo").read_text() if meminfo is None else meminfo
    for ligne in texte.splitlines():
        if ligne.startswith("MemTotal:"):
            return int(ligne.split()[1]) / (1024 * 1024)
    raise GardeArret("garde « mémoire vive » tombée : MemTotal illisible")


def garde_memoire_vive(go: float) -> str:
    if go < cv.MEMOIRE_VIVE_MIN_GO * 0.97:  # MemTotal retire le noyau : 3 % de tolérance déclarée
        raise GardeArret("garde « mémoire vive » tombée : hôte sous le minimum du devis")
    return "passée"


def garde_versions(attendues: dict, lire=None) -> str:
    """Versions installées égales à celles du manifeste (fixées avant la création de l'instance, écart 4)."""
    if lire is None:
        from importlib.metadata import version as lire
    for paquet, v in attendues.items():
        try:
            installee = lire(paquet)
        except Exception:
            installee = None
        if installee != v:
            raise GardeArret(f"garde « versions » tombée : {paquet}")
    return "passée"


def longueur_suffixe(chemin_modele: str, texte_initial: str) -> int:
    """Écart 10 : `tokenize(prompt_init, add_special_tokens=False, add_chat_template=False)` (`hf.py` l. 696-745)."""
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(chemin_modele)
    return len(tok(texte_initial, add_special_tokens=False)["input_ids"])


def mise_en_place(manifeste: dict, clone: Path, sortie: Path) -> dict:
    etats = {}
    for nom, f in (("dépôt public", lambda: garde_depot_public(clone)),
                   ("empreintes", lambda: garde_empreintes_publiques(clone)),
                   ("graines", lambda: an.garde_graines(manifeste["graines"])),
                   ("mémoire vive", lambda: garde_memoire_vive(memoire_vive_go())),
                   ("versions", lambda: garde_versions(manifeste["versions"]))):
        try:
            etats[nom] = f()
        except GardeArret as err:
            etats[nom] = "tombée"
            _ecrire_json(sortie / "mise-en-place-v1.json", {"gardes": etats, "message": str(err)})
            raise
    texte_initial = configuration_texte_initial(clone)
    n = longueur_suffixe(manifeste["chemin_modele"], texte_initial)
    res = {"gardes": etats, "longueur_suffixe": n, "ecart_10": n != 16}
    _ecrire_json(sortie / "mise-en-place-v1.json", res)
    return res


def configuration_texte_initial(clone: Path) -> str:
    """`model_config.prompt_init` de la configuration publique composée (sans surcharge)."""
    from hydra import compose, initialize_config_dir
    with initialize_config_dir(config_dir=str((clone / cv.SOUS_DOSSIER / "configs").resolve()), version_base=None):
        cfg = compose(config_name="config", overrides=[f"experiment={cv.EXPERIENCE}"])
    return cfg.experiment.model_config.prompt_init


# --- contrôles du juge ------------------------------------------------------------------------------------------------

def controle_juge(manifeste: dict, clone: Path, sortie: Path) -> dict:
    """Négatif : réponses sans suffixe, génération publique (300 jetons au plus, décodage hérité, graine « pilote »),
    lots de `eval_batch_size` comme à l'évaluation. Positif : colonne `response`. Garde du juge après le premier appel.
    Écrit les comptes et les empreintes des réponses ; jamais les textes."""
    if "TESTING" in os.environ:
        raise GardeArret("garde « juge » tombée : variable TESTING présente au lancement du processus")
    racine = clone / cv.SOUS_DOSSIER
    os.chdir(racine)
    sys.path.insert(0, str(racine))
    from hydra import compose, initialize_config_dir
    from transformers import set_seed
    with initialize_config_dir(config_dir=str((racine / "configs").resolve()), version_base=None):
        cfg = compose(config_name="config", overrides=[f"experiment={cv.EXPERIENCE}",
                                                       f"experiment.model_path={manifeste['chemin_modele']}"]).experiment
    set_seed(int(manifeste["graines"]["pilote"]))
    from obf_reps.utils import validate_and_create_model_config
    from obf_reps.models.hf import Llama3SoftPrompted
    from obf_reps.data import JailbreakCircuitBreakersObfusDataModule as Module
    from strong_reject.evaluate import cached_models, strongreject_finetuned
    from torch.utils.data import DataLoader
    from .journaliseur_v1 import etat_juge_charge, garde_juge, reponses_attendues

    modele = Llama3SoftPrompted.load_model(Path(cfg.model_path), validate_and_create_model_config(cfg.model_config))
    import pandas as pd
    lignes = []
    for split in ("val", "test"):
        df = pd.read_csv(racine / cv.DOSSIER_JEU / f"harmful_{split}_no_spec_tokens.csv")
        lignes += [(r["prompt"], r["response"]) for _, r in df.iterrows()]
    if len(lignes) != an.TAILLE:
        raise GardeArret("garde « longueur » tombée : 200 entrées nuisibles tenues à l'écart exigées")
    reponses, empreintes = [], []
    for lot in DataLoader(lignes, batch_size=int(cfg.eval_batch_size), shuffle=False):
        entrees, _ = lot
        g = modele.generate_from_string(input_text=list(entrees), add_chat_template=True, use_tunable_params=False,
                                        max_new_tokens=cv.GEN_LEN)
        reponses += list(g.gen_text)
    empreintes = [cv.sha_texte(r) for r in reponses]
    del modele
    prompts = [p for p, _ in lignes]
    notes_neg = strongreject_finetuned({"forbidden_prompt": prompts, "response": reponses})["score"]
    etat = etat_juge_charge(cached_models)
    garde_juge(etat, manifeste["juge"], True)
    refs = reponses_attendues(str(racine / cv.DOSSIER_JEU))
    notes_pos = strongreject_finetuned({"forbidden_prompt": prompts, "response": refs})["score"]
    neg, pos = an.taux_juge(notes_neg), an.taux_juge(notes_pos)
    res = {"juge_charge": etat, "negatif": neg, "positif": pos, "etats": an.controles_juge(neg, pos),
           "empreintes_reponses_negatif": empreintes}
    _ecrire_json(sortie / "controle-juge-v1.json", res)
    an.garde_controles_juge(neg, pos)
    return res


# --- exécution surveillée ---------------------------------------------------------------------------------------------

class Surveillance:
    """Lit la sortie standard du processus enfant ligne à ligne. Garde de démarrage : l'empreinte du début exact de la
    sortie est comparée à celle du texte attendu. Lignes « MARK » : durées. Seules sortent les durées et l'état des
    gardes ; la configuration imprimée reste sur l'instance."""

    def __init__(self, attendu: str, k_attendu: int, sortie: Path):
        self.attendu = attendu.encode("utf-8")
        self.k_attendu = k_attendu
        self.tampon = b""
        self.demarrage = None  # None : pas encore décidé ; True/False
        self.durees: dict[int, float] = {}
        self.sortie = sortie

    def recevoir(self, octets: bytes) -> None:
        if self.demarrage is None:
            self.tampon += octets
            if len(self.tampon) >= len(self.attendu):
                debut = self.tampon[:len(self.attendu)]
                self.demarrage = hashlib.sha256(debut).digest() == hashlib.sha256(self.attendu).digest()
                _ajouter(self.sortie / "gardes-lanceur-v1.jsonl", {
                    "garde": "configuration effective", "etat": "passée" if self.demarrage else "tombée",
                    "empreinte_observee": hashlib.sha256(debut).hexdigest(),
                    "empreinte_attendue": hashlib.sha256(self.attendu).hexdigest(), "k_attendu": self.k_attendu})
                reste, self.tampon = self.tampon[len(self.attendu):], b""
                self._lignes(reste)
            return
        self._lignes(octets)

    def _lignes(self, octets: bytes) -> None:
        for ligne in octets.decode("utf-8", errors="replace").splitlines():
            m = MARK.match(ligne)
            if m:
                e, d = int(m.group(1)), float(m.group(2))
                self.durees[e] = d
                _ajouter(self.sortie / "sortie-durees-v1.jsonl", {"tour": e, "duree_s": d, "t": time.time()})


def garde_k_configuration(attendu: str, k: int) -> str:
    """Le nombre de tours du texte attendu égale celui du manifeste (3 au pilote, K au run principal)."""
    from omegaconf import OmegaConf
    cfg = OmegaConf.create(attendu)
    if int(cfg.experiment.attack_defense_epochs) != int(k):
        raise GardeArret("garde « configuration effective » tombée : nombre de tours différent du manifeste")
    return "passée"


def _empreinter_nouveaux(dossiers: list[Path], vus: dict, journal: Path) -> None:
    for d in dossiers:
        if not d.exists():
            continue
        for f in sorted(d.rglob("*")):
            if f.is_file() and str(f) not in vus:
                vus[str(f)] = cv.sha_fichier(f)
                _ajouter(journal, {"fichier": str(f.relative_to(d.parent)), "sha256": vus[str(f)], "t": time.time()})


def executer(manifeste: dict, clone: Path, travail: Path, phase: str, k: int, graine: int,
             depense: dict, echeance_go: float, commande=None, intervalle: float = 5.0) -> dict:
    """Une exécution. `travail` doit être neuf. Arrête l'enfant par son PID (R10) si une garde de démarrage tombe, si la
    dépense atteint B − 2, ou à l'échéance du GO. Rend l'état ; ne lit aucune note."""
    if travail.exists() and any(travail.iterdir()):
        raise GardeArret("garde « dossier neuf » tombée")
    travail.mkdir(parents=True, exist_ok=True)
    journal, params, sondes, hydra_d = (travail / "journal", travail / "params", travail / "sondes",
                                        travail / "hydra")
    over = surcharges(k, graine, manifeste["chemin_modele"], str(sondes), str(params), str(hydra_d))
    attendu = configuration_attendue(clone, over)
    garde_k_configuration(attendu, k)
    config_journal = {"dossier_journal": str(journal), "dossier_params": str(params),
                      "dossier_jeu": str(clone / cv.SOUS_DOSSIER / cv.DOSSIER_JEU),
                      "pas_attendus": int(manifeste["pas_par_tour"]), "juge": manifeste["juge"], "depense": depense,
                      "testing_absent_au_lancement": "TESTING" not in os.environ, "execution": phase}
    _ecrire_json(travail / "config-journal-v1.json", config_journal)
    env = dict(os.environ)  # TESTING n'est pas retirée : si elle est là, l'enfant s'arrête (garde du juge)
    env["TEMOIN_BAILEY_CONFIG"] = str(travail / "config-journal-v1.json")
    env["PYTHONUNBUFFERED"] = "1"
    cmd = commande or [sys.executable, "-m", "controle_ia.temoin_bailey.execution_v1", "--clone", str(clone),
                       "--graine", str(graine), "--", *over]
    surv = Surveillance(attendu, k, travail)
    vus: dict = {}
    sortie_brute = open(travail / "sortie-standard-instance.log", "wb")  # reste sur l'instance
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
    os.set_blocking(proc.stdout.fileno(), False)
    cause = None
    dernier = 0.0
    while True:
        try:
            morceau = proc.stdout.read()
        except BlockingIOError:
            morceau = None
        if morceau:
            sortie_brute.write(morceau)
            sortie_brute.flush()
            surv.recevoir(morceau)
            if surv.demarrage is False and cause is None:
                cause = "garde de démarrage"
        fini = proc.poll() is not None
        if time.time() - dernier >= intervalle or fini:
            dernier = time.time()
            _empreinter_nouveaux([params, sondes], vus, travail / "empreintes-fichiers-v1.jsonl")
            from .journaliseur_v1 import depense_courante
            if cause is None and depense_courante(depense) >= float(depense["b"]) - 2:
                cause = "dépense"
            if cause is None and time.time() >= echeance_go:
                cause = "échéance du GO"
        if cause and not fini:
            os.kill(proc.pid, signal.SIGTERM)  # R10 : par PID
            try:
                proc.wait(timeout=60)
            except subprocess.TimeoutExpired:
                os.kill(proc.pid, signal.SIGKILL)
                proc.wait()
            fini = True
        if fini:
            reste = proc.stdout.read() or b""
            if reste:
                sortie_brute.write(reste)
                surv.recevoir(reste)
            break
        time.sleep(0.2)
    sortie_brute.close()
    _empreinter_nouveaux([params, sondes], vus, travail / "empreintes-fichiers-v1.jsonl")
    etat = {"phase": phase, "k": k, "graine": graine, "code_retour": proc.returncode, "cause_arret": cause,
            "configuration_effective": {None: "non décidée", True: "passée", False: "tombée"}[surv.demarrage],
            "durees": {str(e): d for e, d in sorted(surv.durees.items())}, "tours_marques": len(surv.durees)}
    _ecrire_json(travail / "etat-execution-v1.json", etat)
    return etat


# --- règle du nombre de tours, empreintes -----------------------------------------------------------------------------

def t_du_pilote(durees: dict) -> float:
    if "0" not in durees or "1" not in durees:
        raise GardeArret("garde « pilote » tombée : tours 0 et 1 du pilote non finis")
    return (float(durees["0"]) + float(durees["1"])) / 2


def regle_tours(b, d, c, durees_pilote: dict) -> dict:
    t = t_du_pilote(durees_pilote)
    r = an.nombre_de_tours(b, d, c, t)
    return {"B": b, "R": 10, "D": d, "c": c, "t": t, **r}


def empreintes(travail: Path) -> dict:
    res = {}
    for rel in cv.NOMS_JOURNAUX:
        if (travail / rel).is_file():
            res[rel] = cv.sha_fichier(travail / rel)
    _ecrire_json(travail / "empreintes-instance-v1.json", res)
    return res


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=["mise-en-place", "controle-juge", "executer", "regle-tours", "empreintes"])
    p.add_argument("--manifeste")
    p.add_argument("--clone")
    p.add_argument("--travail", required=True)
    p.add_argument("--phase", default="pilote")
    p.add_argument("--k", type=int)
    p.add_argument("--graine", type=int)
    p.add_argument("--depense")  # JSON {"d_avant","c","creation","b"}
    p.add_argument("--echeance-go", type=float)
    p.add_argument("--pilote")  # dossier de l'exécution du pilote (regle-tours)
    a = p.parse_args(argv)
    travail = Path(a.travail)
    try:
        if a.commande == "empreintes":
            empreintes(travail)
            return 0
        man = lire_manifeste(a.manifeste)
        travail.mkdir(parents=True, exist_ok=True)
        if a.commande == "mise-en-place":
            mise_en_place(man, Path(a.clone), travail)
        elif a.commande == "controle-juge":
            controle_juge(man, Path(a.clone), travail)
        elif a.commande == "executer":
            executer(man, Path(a.clone), travail, a.phase, a.k, a.graine, json.loads(a.depense), a.echeance_go)
        elif a.commande == "regle-tours":
            dep = json.loads(a.depense)
            d = float(dep["d_avant"]) + float(dep["c"]) * (time.time() - float(dep["creation"])) / 3600
            etat = json.loads((Path(a.pilote) / "etat-execution-v1.json").read_text())
            res = regle_tours(dep["b"], round(d, 4), dep["c"], etat["durees"])
            _ecrire_json(travail / "regle-tours-v1.json", res)
            an.garde_nombre_de_tours(res["K"])
    except GardeArret as err:
        sys.stderr.write(f"{err}\n")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
