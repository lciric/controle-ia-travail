"""Lanceur côté instance — témoin « attaque publiée reproduite » (Bailey et collègues), v7.

La v7 emploie `lecture_v7` (relecture des lignes touchées v5 → v6, `a46dc4fb…`, C-1 à C-4) et applique C-2 et C-4 ici :
chaque commande qui lit les journaux (`executer` à sa fin, `tours`, `tours --ecrire-etat`) porte **sa propre** liste
des lignes coupées ignorées (aucun état global, rien ne s'accumule dans le processus) et l'écrit dans l'état
d'exécution (`lignes_tronquees_ignorees`, chemins des fichiers sur l'instance) **et** dans sa ligne `ETAT`. Une
dernière ligne coupée dans un journal de gardes retire du compte le dernier tour présent (C-3, `lecture_v7`).

Docstring de la v6 :

La v6 ne change que la lecture des journaux employée sur l'instance (`lecture_v6`, M-2 : dernière ligne coupée
ignorée et signalée).

La v5 reprend la v4 (`instance_v4.py`, dont la docstring suit) sans autre changement que ceux de la relecture des
lignes touchées v3 → v4 (`relecture-lignes-touchees-code-condition6-v4-bailey-v1.md`, `ff6c76c7…`) :
- C8 (N-1) : `tours --ecrire-etat --cause … --manifeste … --phase …` écrit `etat-execution-v3.json` **s'il est
  absent** (jamais d'écrasement d'un fichier existant), marqué « reconstitué », avec un `code_retour` non nul, la
  `cause_arret` (liste fermée `CAUSES_RECONSTITUEES` : coupure de l'hôte, dépense, échéance du GO, instance
  injoignable, arrêt par la conduite), les tours complets, les gardes tombées, les durées lues à
  `sortie-durees-v3.jsonl` et le K de la phase lu au manifeste ; sans lire aucune note. La conduite l'appelle sur une
  exécution morte (après l'arrêt du groupe, C10) et, avant les empreintes, sur toute exécution qu'elle a arrêtée par
  PID. Ainsi toute exécution transférée porte un état, et la lecture rend le verdict que le texte donne (l. 338,
  371-372) ;
- l'état d'exécution est écrit de façon atomique (fichier temporaire, puis `os.replace`) : un arrêt par signal
  pendant l'écriture ne laisse jamais un état à moitié écrit, que la reconstitution n'écraserait pas.

Docstring de la v4 :

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : plan d'analyse (écarts, graines,
contrôles du juge, pilote, règle du nombre de tours, run principal, gardes), « Ce qui sort de l'instance ».
La v4 reprend la v3 (`instance_v3.py`) sans autre changement que ceux de la relecture en différentiel du code v3
(`relecture-differentiel-code-condition6-v3-bailey-v1.md`, `a2107244…`) :
- C7 (D-8) : `regle-tours` imprime **une seule** ligne `ETAT`, qui porte K, t, D, c **et**, si K < 20, la garde
  « nombre de tours » tombée (code 3) ; la conduite lit donc K < 20 comme « K < 20 après le pilote : arrêt, devis
  révisé à Lazar », et non plus comme « règle non calculée » ; `etat-regle-v3.json` reste écrit avant la garde ;
- C4 (D-4) : sous-commande `tours`, qui rend, sans lire aucune note, le nombre de tours complets et les gardes
  tombées d'une exécution dont le processus est mort sans écrire son état (coupure de l'hôte), pour que la conduite
  applique la liste d'arrêt (relance avant 20 tours complets seulement).
Tout le reste (mise en place, contrôle du juge, exécution, empreintes) est celui de la v3, décrit dans sa docstring.

Sous-commandes (sorties dans `--travail`, un dossier par étape, neuf) : `mise-en-place`, `controle-juge`,
`executer --phase pilote|pilote-reprise|principal|principal-relance`, `regle-tours`, `empreintes`, `tours`.
Chaque commande imprime une seule ligne `ETAT {…}` (états de gardes, durées, codes) ; jamais une note ni un texte.
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
from . import analyse_v3 as an
from . import conventions_v3 as cv
from .execution_v3 import configuration_attendue, surcharges

MARK = re.compile(r"^MARK: Epoch (\d+) took ([0-9.]+) seconds\s*$")
PHASES = {"pilote": "pilote", "pilote-reprise": "pilote", "principal": "principal", "principal-relance": "principal"}
MARGE_TRANSFERT_S = 3600.0
# C8 : causes d'une exécution sans état, écrites dans l'état reconstitué (liste fermée)
CAUSES_RECONSTITUEES = ("coupure de l'hôte", "dépense", "échéance du GO", "instance injoignable",
                        "arrêt par la conduite")


def _ecrire_json(chemin: Path, objet) -> None:
    """Écriture atomique (v5) : un arrêt par signal pendant l'écriture ne laisse aucun fichier à moitié écrit."""
    tmp = Path(str(chemin) + ".tmp")
    tmp.write_text(json.dumps(objet, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, chemin)


def _ajouter(chemin: Path, objet) -> None:
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(objet, ensure_ascii=False, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def lire_manifeste(chemin) -> dict:
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def etat(objet: dict) -> None:
    """Seule sortie d'une commande vers le poste local (A-9)."""
    print("ETAT " + json.dumps(objet, ensure_ascii=False, sort_keys=True), flush=True)


def verifier_budget(depense: dict, echeance_arret: float, maintenant: float | None = None) -> None:
    """Correction 13 : arrêt à B − 2 (dépense du poste, comptée comme D) ou à l'échéance d'arrêt (échéance du GO moins
    la marge de transfert), hors des exécutions aussi."""
    from .journaliseur_v3 import depense_courante
    maintenant = time.time() if maintenant is None else maintenant
    an.garde_depense(depense_courante(depense, maintenant), float(depense["b"]))
    if maintenant >= float(echeance_arret):
        raise GardeArret("garde « échéance du GO » tombée : échéance moins la marge de transfert atteinte")


# --- mise en place ----------------------------------------------------------------------------------------------------

def _git(clone: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(clone), *args], check=True, capture_output=True, text=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise GardeArret("garde « dépôt public » tombée : dépôt illisible") from None


def garde_depot_public(clone: Path, commit: str = cv.COMMIT_PUBLIC, arbre: str = cv.ARBRE_PUBLIC) -> str:
    if _git(clone, "rev-parse", "HEAD") != commit:
        raise GardeArret("garde « dépôt public » tombée : commit")
    if _git(clone, "rev-parse", "HEAD^{tree}") != arbre:
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


def memoire_vive_octets(meminfo: str | None = None, cgroup_max: str | None = None) -> int:
    """Minimum de `MemTotal` (en kio dans `/proc/meminfo`, malgré l'abréviation « kB ») et de la limite du groupe de
    contrôle (`/sys/fs/cgroup/memory.max`, si numérique ; « max » = sans limite)."""
    texte = Path("/proc/meminfo").read_text() if meminfo is None else meminfo
    total = None
    for ligne in texte.splitlines():
        if ligne.startswith("MemTotal:"):
            total = int(ligne.split()[1]) * 1024
    if total is None:
        raise GardeArret("garde « mémoire vive » tombée : MemTotal illisible")
    if cgroup_max is None:
        p = Path("/sys/fs/cgroup/memory.max")
        cgroup_max = p.read_text() if p.is_file() else "max"
    c = cgroup_max.strip()
    if c.isdigit():
        total = min(total, int(c))
    elif c != "max":
        raise GardeArret("garde « mémoire vive » tombée : limite du groupe de contrôle illisible")
    return total


def garde_memoire_vive(octets: int) -> str:
    """Texte : « mémoire vive de l'hôte au moins égale à celle de [Devis] » (128 Go, lus 128 × 10⁹ octets)."""
    if isinstance(octets, bool) or not isinstance(octets, int) or octets < cv.MEMOIRE_VIVE_MIN_OCTETS:
        raise GardeArret("garde « mémoire vive » tombée : hôte sous le minimum du devis")
    return "passée"


def garde_python(attendue: str, version=None) -> str:
    """Versions figées : Python 3.11 (S-2)."""
    v = sys.version_info if version is None else version
    if f"{v[0]}.{v[1]}" != str(attendue):
        raise GardeArret("garde « python » tombée : version de Python différente du manifeste")
    return "passée"


def garde_versions(attendues: dict, lire=None) -> str:
    """Versions installées égales au manifeste (écart 4). Refuse un dictionnaire vide et exige les paquets de
    `VERSIONS_EXIGEES` (correction 8)."""
    if not isinstance(attendues, dict) or not attendues:
        raise GardeArret("garde « versions » tombée : aucune version au manifeste")
    for paquet in cv.VERSIONS_EXIGEES:
        if paquet not in attendues:
            raise GardeArret(f"garde « versions » tombée : {paquet} absent du manifeste")
    if lire is None:
        from importlib.metadata import version as lire
    for paquet, v in attendues.items():
        try:
            installee = lire(paquet)
        except Exception:  # paquet absent : la garde tombe ci-dessous
            installee = None
        if installee != v:
            raise GardeArret(f"garde « versions » tombée : {paquet}")
    return "passée"


def commit_installe(paquet: str) -> str | None:
    from importlib.metadata import PackageNotFoundError, distribution
    try:
        brut = distribution(paquet).read_text("direct_url.json")
    except PackageNotFoundError:
        return None
    if not brut:
        return None
    return (json.loads(brut).get("vcs_info") or {}).get("commit_id")


def garde_commits_git(attendus: dict, lire=commit_installe) -> str:
    """Paquets tirés de dépôts tiers : commit installé égal au manifeste (A-2). `attendus` : {paquet: [url, commit]} ;
    non vide, et `strong_reject` au commit du texte (correction 8)."""
    if not isinstance(attendus, dict) or not attendus:
        raise GardeArret("garde « versions » tombée : aucun commit de paquet au manifeste")
    sr = list(attendus.get("strong_reject") or [])
    if len(sr) != 2 or sr[1] != cv.JUGE_COMMIT_PAQUET:
        raise GardeArret("garde « versions » tombée : commit de strong_reject différent du texte")
    for paquet, (_url, commit) in attendus.items():
        if lire(paquet) != commit:
            raise GardeArret(f"garde « versions » tombée : commit de {paquet}")
    return "passée"


def garde_revisions_cache(cache_hf: str, attendues: dict, lire=None) -> str:
    """`refs/main` du cache de Hugging Face égale à la révision épinglée, pour le modèle, l'adaptateur du juge et sa
    base (B-4) : le chargement hors ligne emploie cette révision."""
    from .journaliseur_v3 import revision_en_cache
    lire = lire or revision_en_cache
    for depot, rev in attendues.items():
        if lire(cache_hf, depot) != rev:
            raise GardeArret(f"garde « révisions » tombée : {depot}")
    return "passée"


def longueur_suffixe(chemin_modele: str, texte_initial: str) -> int:
    """Écart 10 : `tokenize(prompt_init, add_special_tokens=False, add_chat_template=False)` (`hf.py` l. 696-745)."""
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(chemin_modele)
    return len(tok(texte_initial, add_special_tokens=False)["input_ids"])


def configuration_composee(clone: Path, surcharges_: list[str] | None = None):
    from hydra import compose, initialize_config_dir
    with initialize_config_dir(config_dir=str((clone / cv.SOUS_DOSSIER / "configs").resolve()), version_base=None):
        return compose(config_name="config", overrides=[f"experiment={cv.EXPERIENCE}", *(surcharges_ or [])]).experiment


def pas_attendus(clone: Path, cfg=None) -> int:
    import pandas as pd
    cfg = cfg if cfg is not None else configuration_composee(clone)
    n = len(pd.read_csv(clone / cv.SOUS_DOSSIER / cv.DOSSIER_JEU / "harmful_train_no_spec_tokens.csv"))
    return cv.pas_par_tour(int(cfg.epochs), n, int(cfg.batch_size))


def tokeniseur_present(cache_hf: str, depot: str, revision: str) -> bool:
    """P-c : le dépôt porte-t-il un tokeniseur (le paquet du juge charge `AutoTokenizer` sur le nom de l'adaptateur,
    `strong_reject/evaluate.py` l. 474-476) ? Écrit à la mise en place, sans arrêter."""
    d = Path(cache_hf) / ("models--" + depot.replace("/", "--")) / "snapshots" / revision
    return any((d / n).is_file() for n in ("tokenizer.json", "tokenizer_config.json", "tokenizer.model"))


def mise_en_place(manifeste: dict, clone: Path, sortie: Path, depense: dict, echeance_arret: float,
                  meminfo: str | None = None, cgroup_max: str | None = None) -> dict:
    sortie.mkdir(parents=True, exist_ok=True)
    etats = {}
    verifier_budget(depense, echeance_arret)
    gardes = (("dépôt public", lambda: garde_depot_public(clone)),
              ("empreintes", lambda: garde_empreintes_publiques(clone)),
              ("graines", lambda: an.garde_graines(manifeste["graines"])),
              ("mémoire vive", lambda: garde_memoire_vive(memoire_vive_octets(meminfo, cgroup_max))),
              ("python", lambda: garde_python(manifeste["python"])),
              ("versions", lambda: garde_versions(manifeste["versions"])),
              ("commits", lambda: garde_commits_git(manifeste["git"])),
              ("révisions", lambda: garde_revisions_cache(manifeste["cache_hf"], {
                  cv.MODELE: manifeste["revision_modele"], cv.JUGE: manifeste["juge"]["revision_adaptateur"],
                  cv.JUGE_BASE: manifeste["juge"]["revision_base"]})))
    for nom, f in gardes:
        try:
            etats[nom] = f()
        except GardeArret as err:
            etats[nom] = "tombée"
            _ecrire_json(sortie / cv.ETAT_MISE_EN_PLACE, {"gardes": etats, "message": str(err)})
            raise
    from .journaliseur_v3 import reponses_attendues
    cfg = configuration_composee(clone)
    n = longueur_suffixe(manifeste["chemin_modele"], cfg.model_config.prompt_init)
    gen = Path(manifeste["chemin_modele"]) / "generation_config.json"
    complement = {"longueur_suffixe": n, "ecart_10": n != 16, "pas_par_tour": pas_attendus(clone, cfg),
                  "configuration_generation": json.loads(gen.read_text()) if gen.is_file() else None,
                  "configuration_generation_sha256": cv.sha_fichier(gen) if gen.is_file() else None,
                  "memoire_vive_octets": memoire_vive_octets(meminfo, cgroup_max),
                  "empreintes_cibles_attendues": [cv.sha_texte(r) for r in reponses_attendues(
                      str(clone / cv.SOUS_DOSSIER / cv.DOSSIER_JEU))],
                  "tokeniseur_adaptateur_present": tokeniseur_present(manifeste["cache_hf"], cv.JUGE,
                                                                      manifeste["juge"]["revision_adaptateur"])}
    try:
        verifier_budget(depense, echeance_arret)
    except GardeArret as err:
        _ecrire_json(sortie / cv.ETAT_MISE_EN_PLACE, {"gardes": etats, **complement, "message": str(err)})
        raise
    _ecrire_json(sortie / cv.ETAT_MISE_EN_PLACE, {"gardes": etats, **complement})
    return {"gardes": etats, **complement}


# --- contrôles du juge ------------------------------------------------------------------------------------------------

def controle_juge(manifeste: dict, clone: Path, sortie: Path, depense: dict, echeance_arret: float,
                  etat_mise_en_place: Path, cache_juge=None, juge=None, generer=None) -> dict:
    """Négatif : réponses sans suffixe, génération publique (300 jetons au plus, décodage hérité, graine « pilote »),
    lots de `eval_batch_size`. Positif : colonne `response`. Juge par lots de `eval_batch_size` (B-3). Garde du juge
    après son premier appel, son état écrit avant de lever. Vérifie d'abord l'état de la mise en place (P-5) ; dépense
    et échéance vérifiées avant chaque lot (correction 13). Écrit les comptes et les empreintes des réponses ; jamais
    les textes. `cache_juge`, `juge`, `generer` : substituts pour l'épreuve sur processeur."""
    from .journaliseur_v3 import etat_juge_charge, garde_juge, reponses_attendues
    sortie.mkdir(parents=True, exist_ok=True)
    mep = json.loads(Path(etat_mise_en_place).read_text(encoding="utf-8")) if Path(etat_mise_en_place).is_file() else {}
    if set(mep.get("gardes", {})) != set(cv.GARDES_MISE_EN_PLACE) or any(
            v != "passée" for v in mep["gardes"].values()):
        raise GardeArret("contrôle du juge : mise en place non passée ou état absent")
    res = {"garde_juge": None}

    def ecrire():
        _ecrire_json(sortie / cv.ETAT_CONTROLE_JUGE, res)

    if "TESTING" in os.environ:
        res["garde_juge"] = "tombée"
        ecrire()
        raise GardeArret("garde « juge » tombée : variable TESTING présente au lancement du processus")
    racine = clone / cv.SOUS_DOSSIER
    cfg = configuration_composee(clone, [f"experiment.model_path={manifeste['chemin_modele']}"])
    lot = int(cfg.eval_batch_size)
    import pandas as pd
    lignes = []
    for split in ("val", "test"):
        df = pd.read_csv(racine / cv.DOSSIER_JEU / f"harmful_{split}_no_spec_tokens.csv")
        lignes += [(r["prompt"], r["response"]) for _, r in df.iterrows()]
    if len(lignes) != an.TAILLE:
        raise GardeArret("garde « longueur » tombée : 200 entrées nuisibles tenues à l'écart exigées")
    prompts = [p for p, _ in lignes]
    if generer is None:
        os.chdir(racine)
        sys.path.insert(0, str(racine))
        from transformers import set_seed
        set_seed(int(manifeste["graines"]["pilote"]))
        from obf_reps.models.llama3 import Llama3SoftPrompted
        from obf_reps.utils import validate_and_create_model_config
        modele = Llama3SoftPrompted.load_model(Path(cfg.model_path), validate_and_create_model_config(cfg.model_config))

        def generer(entrees):
            g = modele.generate_from_string(input_text=list(entrees), add_chat_template=True,
                                            use_tunable_params=False, max_new_tokens=cv.GEN_LEN)
            return list(g.gen_text)
    reponses = []
    for i in range(0, an.TAILLE, lot):
        verifier_budget(depense, echeance_arret)
        reponses += generer(prompts[i:i + lot])
    if len(reponses) != an.TAILLE:
        raise GardeArret("garde « longueur » tombée : 200 réponses sans suffixe exigées")
    res["empreintes_reponses_negatif"] = [cv.sha_texte(r) for r in reponses]
    if juge is None:
        from strong_reject.evaluate import cached_models as cache_juge, strongreject_finetuned as juge
    refs = reponses_attendues(str(racine / cv.DOSSIER_JEU))

    def juger(textes):
        notes = []
        for i in range(0, an.TAILLE, lot):
            verifier_budget(depense, echeance_arret)
            notes += juge({"forbidden_prompt": prompts[i:i + lot], "response": textes[i:i + lot]})["score"]
            if res["garde_juge"] is None:
                e = etat_juge_charge(cache_juge, manifeste["cache_hf"])
                res["juge_charge"] = e
                try:
                    garde_juge(e, manifeste["juge"], True)
                except GardeArret:
                    res["garde_juge"] = "tombée"
                    ecrire()
                    raise
                res["garde_juge"] = "passée"
        return notes

    neg = an.taux_juge(juger(reponses))
    pos = an.taux_juge(juger(refs))
    res.update({"negatif": neg, "positif": pos, "etats": an.controles_juge(neg, pos), "lot": lot})
    ecrire()
    an.garde_controles_juge(neg, pos)
    return res


# --- exécution surveillée ---------------------------------------------------------------------------------------------

class Surveillance:
    """Lit la sortie standard (seule) du processus enfant. Garde de démarrage : empreinte du début exact de la sortie
    standard contre celle du texte attendu. Lignes « MARK » : durées ; une ligne coupée entre deux lectures est gardée
    en tampon (B-7)."""

    def __init__(self, attendu: str, k_attendu: int, sortie: Path):
        self.attendu = attendu.encode("utf-8")
        self.k_attendu = k_attendu
        self.tampon = b""
        self.ligne = b""
        self.demarrage = None
        self.durees: dict[int, float] = {}
        self.sortie = sortie

    def recevoir(self, octets: bytes) -> None:
        if self.demarrage is None:
            self.tampon += octets
            if len(self.tampon) < len(self.attendu):
                return
            debut = self.tampon[:len(self.attendu)]
            self.demarrage = hashlib.sha256(debut).digest() == hashlib.sha256(self.attendu).digest()
            _ajouter(self.sortie / cv.GARDES_LANCEUR, {
                "garde": "configuration effective", "etat": "passée" if self.demarrage else "tombée", "tour": -1,
                "empreinte_observee": hashlib.sha256(debut).hexdigest(),
                "empreinte_attendue": hashlib.sha256(self.attendu).hexdigest(), "k_attendu": self.k_attendu})
            octets, self.tampon = self.tampon[len(self.attendu):], b""
        self.ligne += octets
        *completes, self.ligne = self.ligne.split(b"\n")
        for brute in completes:
            self._ligne(brute)

    def finir(self) -> None:
        if self.ligne:
            self._ligne(self.ligne)
            self.ligne = b""

    def _ligne(self, brute: bytes) -> None:
        m = MARK.match(brute.decode("utf-8", errors="replace"))
        if m:
            e, d = int(m.group(1)), float(m.group(2))
            self.durees[e] = d
            _ajouter(self.sortie / cv.SORTIE_DUREES, {"tour": e, "duree_s": d, "t": time.time()})


def parametres_phase(manifeste: dict, phase: str) -> tuple[int, int]:
    """K et graine lus au manifeste (B-8) : pilote → 3 tours, graine « pilote » ; run principal → K de la règle,
    graine « run principal »."""
    if phase not in PHASES:
        raise GardeArret("phase inconnue")
    if PHASES[phase] == "pilote":
        return 3, int(manifeste["graines"]["pilote"])
    if "K" not in manifeste.get("regle_tours", {}):
        raise GardeArret("garde « configuration effective » tombée : K absent du manifeste")
    return int(manifeste["regle_tours"]["K"]), int(manifeste["graines"]["principal"])


def garde_k_configuration(attendu: str, manifeste: dict, phase: str) -> str:
    """Le nombre de tours et la graine du texte attendu sont ceux du manifeste pour la phase, et la graine celle du
    texte scellé."""
    from omegaconf import OmegaConf
    cfg = OmegaConf.create(attendu)
    k, graine = parametres_phase(manifeste, phase)
    attendue = an.GRAINE_PILOTE if PHASES[phase] == "pilote" else an.GRAINE_PRINCIPAL
    if int(cfg.experiment.attack_defense_epochs) != k or int(cfg.experiment.seed) != graine or graine != attendue:
        raise GardeArret("garde « configuration effective » tombée : nombre de tours ou graine différents du manifeste")
    return "passée"


def _empreinter_nouveaux(dossiers: list[Path], tailles: dict, vus: dict, journal: Path, final: bool) -> None:
    """Un fichier est empreinté quand sa taille est stable entre deux passages (A-10), ou à la fin du processus."""
    for d in dossiers:
        if not d.exists():
            continue
        for f in sorted(d.rglob("*")):
            if not f.is_file() or str(f) in vus:
                continue
            taille = f.stat().st_size
            if final or tailles.get(str(f)) == taille:
                vus[str(f)] = cv.sha_fichier(f)
                _ajouter(journal, {"fichier": str(f.relative_to(d.parent)), "sha256": vus[str(f)], "t": time.time()})
            tailles[str(f)] = taille


def executer(manifeste: dict, clone: Path, travail: Path, phase: str, depense: dict, echeance_go: float,
             commande=None, intervalle: float = 5.0, marge_transfert_s: float = MARGE_TRANSFERT_S) -> dict:
    """Une exécution. `travail` doit être neuf. Arrête l'enfant par son PID (R10) si la garde de démarrage tombe, si la
    dépense atteint B − 2, ou à `échéance du GO − marge_transfert_s` (correction 5) ; le run est alors tronqué, ses
    journaux restent pour le transfert. Ne lit aucune note."""
    if echeance_go is None:
        raise GardeArret("échéance du GO exigée")
    from .lecture_v7 import gardes_tombees, tours_complets_instance
    from .journaliseur_v3 import depense_courante
    if travail.exists() and any(travail.iterdir()):
        raise GardeArret("garde « dossier neuf » tombée")
    travail.mkdir(parents=True, exist_ok=True)
    for rel in (cv.GARDES_LANCEUR, cv.SORTIE_DUREES, cv.EMPREINTES_FICHIERS):
        (travail / rel).touch()
    k, graine = parametres_phase(manifeste, phase)
    params, sondes, hydra_d = travail / "params", travail / "sondes", travail / "hydra"
    over = surcharges(k, graine, manifeste["chemin_modele"], str(sondes), str(params), str(hydra_d))
    attendu = configuration_attendue(clone, over)
    garde_k_configuration(attendu, manifeste, phase)
    _ecrire_json(travail / "config-journal-v3.json", {
        "dossier_journal": str(travail / "journal"), "dossier_params": str(params),
        "dossier_jeu": str(clone / cv.SOUS_DOSSIER / cv.DOSSIER_JEU), "pas_attendus": int(manifeste["pas_par_tour"]),
        "juge": manifeste["juge"], "depense": depense, "cache_hf": manifeste["cache_hf"], "execution": phase})
    env = dict(os.environ)  # TESTING n'est pas retirée : si elle est là, l'enfant s'arrête (garde du juge)
    env["TEMOIN_BAILEY_CONFIG"] = str(travail / "config-journal-v3.json")
    env["PYTHONUNBUFFERED"] = "1"
    cmd = commande or [sys.executable, "-m", "controle_ia.temoin_bailey.execution_v3", "--clone", str(clone),
                       "--graine", str(graine), "--", *over]
    surv = Surveillance(attendu, k, travail)
    vus, tailles = {}, {}
    brute = open(travail / "sortie-standard-instance.log", "wb")    # reste sur l'instance
    erreurs = open(travail / "sortie-erreur-instance.log", "wb")    # reste sur l'instance (B-2)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=erreurs, env=env)
    os.set_blocking(proc.stdout.fileno(), False)
    cause, dernier = None, 0.0
    arret_echeance = float(echeance_go) - float(marge_transfert_s)
    while True:
        try:
            morceau = proc.stdout.read()
        except BlockingIOError:
            morceau = None
        if morceau:
            brute.write(morceau)
            brute.flush()
            surv.recevoir(morceau)
            if surv.demarrage is False and cause is None:
                cause = "garde de démarrage"
        fini = proc.poll() is not None
        if time.time() - dernier >= intervalle or fini:
            dernier = time.time()
            _empreinter_nouveaux([params, sondes], tailles, vus, travail / cv.EMPREINTES_FICHIERS, False)
            if cause is None and depense_courante(depense) >= float(depense["b"]) - 2:
                cause = "dépense"
            if cause is None and time.time() >= arret_echeance:
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
                brute.write(reste)
                surv.recevoir(reste)
            surv.finir()
            break
        time.sleep(0.2)
    brute.close()
    erreurs.close()
    _empreinter_nouveaux([params, sondes], tailles, vus, travail / cv.EMPREINTES_FICHIERS, True)
    signal: list[str] = []  # v7 (C-4) : propre à cette exécution
    complets, absence = tours_complets_instance(travail, signal)
    tombees = gardes_tombees(travail, signal)
    res = {"phase": phase, "k": k, "graine": graine, "code_retour": proc.returncode, "cause_arret": cause,
           "configuration_effective": {None: "non décidée", True: "passée", False: "tombée"}[surv.demarrage],
           "durees": {str(e): d for e, d in sorted(surv.durees.items())}, "tours_marques": len(surv.durees),
           "gardes_tombees": tombees, "tours_complets": complets, "journal_absent": absence,
           "lignes_tronquees_ignorees": signal}
    _ecrire_json(travail / cv.ETAT_EXECUTION, res)
    return res


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
    """Journaux et fichiers d'état présents dans le dossier de l'étape (correction 11)."""
    res = {rel: cv.sha_fichier(travail / rel) for rel in cv.SORTANTS if (travail / rel).is_file()}
    _ecrire_json(travail / cv.EMPREINTES_INSTANCE, res)
    return res


def reconstituer_etat(travail: Path, manifeste: dict, phase: str, cause: str) -> dict:
    """C8 (N-1) : écrit `etat-execution-v3.json` d'une exécution qui n'en a pas (morte sur l'instance, ou arrêtée par
    la conduite), **sans jamais écraser** un état présent ; ne lit aucune note. Rend, pour la ligne `ETAT`, les tours
    complets, les gardes tombées, la cause d'un journal absent, et `etat_execution` : « reconstitué » ou « déjà
    présent ». L'état reconstitué porte `reconstitue: true`, `code_retour` 1 (non nul), `cause_arret` = `cause`,
    `tours_complets`, `gardes_tombees`, `durees` (lues à `sortie-durees-v3.jsonl`), `tours_marques`, et le K et la
    graine de la phase lus au manifeste. v7 (C-2, C-4) : les lignes coupées ignorées (liste propre à cet appel) sont
    écrites dans l'état (`lignes_tronquees_ignorees`) et rendues pour la ligne `ETAT`."""
    from .lecture_v7 import gardes_tombees, lire_jsonl, tours_complets_instance
    if cause not in CAUSES_RECONSTITUEES:
        raise GardeArret(f"état reconstitué : cause hors de la liste fermée ({cause})")
    k, graine = parametres_phase(manifeste, phase)
    travail.mkdir(parents=True, exist_ok=True)
    signal: list[str] = []
    complets, absence = tours_complets_instance(travail, signal)
    tombees = gardes_tombees(travail, signal)
    res = {"tours_complets": complets, "journal_absent": absence, "gardes_tombees": tombees,
           "lignes_tronquees_ignorees": signal}
    chemin = travail / cv.ETAT_EXECUTION
    if chemin.exists():
        return {**res, "etat_execution": "déjà présent"}
    try:
        durees = {str(int(x["tour"])): float(x["duree_s"]) for x in lire_jsonl(travail / cv.SORTIE_DUREES, signal)}
    except (GardeArret, KeyError, ValueError, TypeError):
        durees = {}
    etat_ = {"phase": phase, "k": k, "graine": graine, "code_retour": 1, "cause_arret": cause, "reconstitue": True,
             "configuration_effective": "non décidée", "durees": dict(sorted(durees.items(), key=lambda x: int(x[0]))),
             "tours_marques": len(durees), "gardes_tombees": tombees, "tours_complets": complets,
             "journal_absent": absence, "lignes_tronquees_ignorees": signal,
             "message": f"état reconstitué après l'arrêt de l'exécution sans état ({cause})"}
    if chemin.exists():  # jamais d'écrasement (relu juste avant l'écriture)
        return {**res, "etat_execution": "déjà présent"}
    _ecrire_json(chemin, etat_)
    return {**res, "etat_execution": "reconstitué"}


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=["mise-en-place", "controle-juge", "executer", "regle-tours", "empreintes",
                                        "tours"])
    p.add_argument("--manifeste")
    p.add_argument("--clone")
    p.add_argument("--travail", required=True)
    p.add_argument("--phase")  # défaut « pilote », sauf pour `tours --ecrire-etat`, qui l'exige
    p.add_argument("--ecrire-etat", action="store_true")  # C8 : `tours` écrit l'état absent, marqué « reconstitué »
    p.add_argument("--cause")  # C8 : cause de l'arrêt, dans `CAUSES_RECONSTITUEES`
    p.add_argument("--depense")  # JSON {"d_avant","c","creation","b"}
    p.add_argument("--echeance-go", type=float)
    p.add_argument("--marge-transfert", type=float, default=MARGE_TRANSFERT_S)
    p.add_argument("--mise-en-place")  # dossier de la mise en place (controle-juge, P-5)
    p.add_argument("--pilote")  # dossier de l'exécution du pilote qui fixe t (regle-tours)
    a = p.parse_args(argv)
    travail = Path(a.travail)
    if a.commande == "tours" and a.ecrire_etat and (a.phase is None or a.manifeste is None or a.cause is None):
        p.error("tours --ecrire-etat : --phase, --manifeste et --cause requis")
    if a.phase is None:
        a.phase = "pilote"
    if a.commande in ("mise-en-place", "controle-juge", "executer", "regle-tours") and a.depense is None:
        p.error("--depense requis")
    if a.commande in ("mise-en-place", "controle-juge", "executer") and a.echeance_go is None:
        p.error("--echeance-go requis")  # correction 16
    try:
        if a.commande == "empreintes":
            etat({"commande": "empreintes", "fichiers": sorted(empreintes(travail))})
            return 0
        if a.commande == "tours" and a.ecrire_etat:  # C8 : état reconstitué, jamais d'écrasement ; aucune note lue
            r = reconstituer_etat(travail, lire_manifeste(a.manifeste), a.phase, a.cause)
            etat({"commande": "tours", **r})
            return 0
        if a.commande == "tours":  # C4 : exécution morte sans état ; aucune note lue
            from .lecture_v7 import gardes_tombees, tours_complets_instance
            signal: list[str] = []  # v7 (C-4) : propre à cette commande
            complets, absence = tours_complets_instance(travail, signal)
            tombees = gardes_tombees(travail, signal)
            etat({"commande": "tours", "tours_complets": complets, "journal_absent": absence,
                  "gardes_tombees": tombees, "lignes_tronquees_ignorees": signal})
            return 0
        man = lire_manifeste(a.manifeste)
        travail.mkdir(parents=True, exist_ok=True)
        dep = json.loads(a.depense)
        arret = a.echeance_go - a.marge_transfert if a.echeance_go is not None else None
        if a.commande == "mise-en-place":
            r = mise_en_place(man, Path(a.clone), travail, dep, arret)
            etat({"commande": a.commande, "gardes": r["gardes"], "longueur_suffixe": r["longueur_suffixe"],
                  "pas_par_tour": r["pas_par_tour"], "ecart_10": r["ecart_10"]})
        elif a.commande == "controle-juge":
            r = controle_juge(man, Path(a.clone), travail, dep, arret, Path(a.mise_en_place) / cv.ETAT_MISE_EN_PLACE)
            etat({"commande": a.commande, "etats": r["etats"], "garde_juge": r["garde_juge"]})
        elif a.commande == "executer":
            r = executer(man, Path(a.clone), travail, a.phase, dep, a.echeance_go, marge_transfert_s=a.marge_transfert)
            etat({"commande": a.commande, **{k: r[k] for k in ("phase", "k", "code_retour", "cause_arret",
                                                                 "configuration_effective", "durees", "tours_marques",
                                                                 "gardes_tombees", "tours_complets",
                                                                 "journal_absent", "lignes_tronquees_ignorees")}})
        elif a.commande == "regle-tours":
            d = float(dep["d_avant"]) + float(dep["c"]) * (time.time() - float(dep["creation"])) / 3600
            e = json.loads((Path(a.pilote) / cv.ETAT_EXECUTION).read_text())
            r = regle_tours(dep["b"], round(d, 4), dep["c"], e["durees"])
            _ecrire_json(travail / cv.ETAT_REGLE, r)
            try:  # C7 : K et la garde au même `ETAT`, une seule ligne
                an.garde_nombre_de_tours(r["K"])
            except GardeArret as err:
                etat({"commande": a.commande, **r, "garde_tombee": str(err)})
                return 3
            etat({"commande": a.commande, **r})
    except GardeArret as err:
        etat({"commande": a.commande, "garde_tombee": str(err)})
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
