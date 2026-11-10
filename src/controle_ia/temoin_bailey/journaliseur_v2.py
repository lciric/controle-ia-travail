"""Journaliseur local substitué à Weights & Biases — témoin « attaque publiée reproduite » (Bailey et collègues), v2.

Écart 2 du préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`). La v2 applique la
contre-lecture du code de la condition 6 (`docs/notes/reproduction-attaque-publiee-v1/contre-lecture-code-condition6-bailey-v1.md`,
`90af7dea…`) : journal des notes séparé du journal technique (A-3) ; toute garde écrit son état avant de lever (A-4) ;
garde du juge pour un adaptateur (B-4) ; analyse v3.

Le lanceur (`execution_v2.py`) remplace, dans le processus qui exécute le code public, `WAndBLogger` par
`JournaliseurLocal`, sans modifier aucun fichier du dépôt public. Le journaliseur :
- écrit au fil de l'eau, une ligne JSON par événement, vidée et synchronisée sur disque :
  - `notes-v2.jsonl` : notes brutes de la sonde avec leur étiquette, notes du juge, empreintes des textes et des entrées ;
  - `technique-v2.jsonl` : pas par tour, mémoire, longueur de suffixe journalisée, juge chargé, empreintes des valeurs
    des suffixes, horodatages — lisible au pilote sans ouvrir les notes ;
  - `egalites-scellees-v2.jsonl` : compte des entrées dont la note avec suffixe égale la note sans suffixe, jamais
    imprimé ;
  - `gardes-v2.jsonl` : état de chaque garde (« passée » ou « tombée »), nom et grandeur, jamais une valeur de note ;
- n'écrit ni textes ni figures et ferme chaque figure reçue ; fournit l'attribut `tables` (`evaluate.py`, l. 1103) ;
- n'envoie rien vers un service externe ; ne reçoit ni suffixe ni sonde.

Configuration : variable d'environnement `TEMOIN_BAILEY_CONFIG`, chemin d'un JSON écrit par le lanceur.
"""
from __future__ import annotations

import json
import os
import resource
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

from ..gardes import GardeArret
from . import analyse_v3 as an
from . import conventions_v2 as cv


@dataclass
class ConfigJournal:
    dossier_journal: str
    dossier_params: str
    dossier_jeu: str
    pas_attendus: int
    juge: dict  # manifeste : {"adaptateur", "revision_adaptateur", "base", "revision_base", "dtype"}
    depense: dict  # {"d_avant": USD, "c": USD/h, "creation": epoch s, "b": USD}
    cache_hf: str = ""
    execution: str = ""
    extra: dict = field(default_factory=dict)

    @classmethod
    def lire(cls, chemin) -> "ConfigJournal":
        return cls(**json.loads(Path(chemin).read_text(encoding="utf-8")))


def _ecrire(f, objet: dict) -> None:
    f.write(json.dumps(objet, ensure_ascii=False, sort_keys=True) + "\n")
    f.flush()
    os.fsync(f.fileno())


def _fermer_figure(x) -> None:
    try:
        from matplotlib.figure import Figure
    except Exception:
        return
    if isinstance(x, Figure):
        import matplotlib.pyplot as plt
        plt.close(x)


def _memoire() -> dict:
    m = {"memoire_vive_pic_ko": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    try:
        import torch
        if torch.cuda.is_available():
            m["memoire_carte_pic_octets"] = int(torch.cuda.max_memory_allocated())
    except Exception:
        pass
    return m


def reponses_attendues(dossier_jeu: str) -> list[str]:
    """Les 200 réponses de référence (validation puis test), lues comme le code public les lit (`pandas.read_csv`)."""
    import pandas as pd
    out = []
    for split in ("val", "test"):
        df = pd.read_csv(Path(dossier_jeu) / f"harmful_{split}_no_spec_tokens.csv")
        out += [row["response"] for _, row in df.iterrows()]
    return out


def revision_en_cache(cache_hf: str, depot: str) -> str | None:
    """Révision que le chargement hors ligne emploie : contenu de `refs/main` du dépôt dans le cache de Hugging Face
    (le lanceur l'y écrit, égale à la révision épinglée)."""
    p = Path(cache_hf) / ("models--" + depot.replace("/", "--")) / "refs" / "main"
    return p.read_text().strip() if p.is_file() else None


def etat_juge_charge(cached_models: dict, cache_hf: str) -> dict:
    """État du juge effectivement chargé, lu dans le cache du paquet `strong_reject` (`evaluate.py` l. 459-482 au
    commit épinglé) et dans le cache de Hugging Face."""
    if "strongreject_finetuned" not in cached_models:
        raise GardeArret("garde « juge » tombée : modèle du juge absent du cache après son premier appel")
    modele, tok = cached_models["strongreject_finetuned"]
    conf = getattr(modele, "config", None)
    peft = getattr(modele, "peft_config", None) or {}
    bases = sorted({getattr(c, "base_model_name_or_path", None) for c in peft.values()} - {None})
    return {"adaptateur_charge": bool(peft), "base_declaree": bases[0] if len(bases) == 1 else bases or None,
            "nom_config": getattr(conf, "_name_or_path", None), "revision_config": getattr(conf, "_commit_hash", None),
            "tokeniseur": getattr(tok, "name_or_path", None), "dtype": str(getattr(modele, "dtype", None)),
            "revision_adaptateur_cache": revision_en_cache(cache_hf, cv.JUGE),
            "revision_base_cache": revision_en_cache(cache_hf, cv.JUGE_BASE)}


def garde_juge(etat: dict, attendu: dict, testing_absent: bool) -> str:
    """Juge = l'adaptateur épinglé sur la base épinglée, en bfloat16 (le repli silencieux en float32 de
    `strong_reject/evaluate.py` l. 464-469 fait tomber la garde), variable `TESTING` absente."""
    if not testing_absent:
        raise GardeArret("garde « juge » tombée : variable TESTING présente au lancement du processus")
    controles = {
        "adaptateur": etat.get("adaptateur_charge") is True and etat.get("tokeniseur") == attendu["adaptateur"],
        "base": etat.get("base_declaree") == attendu["base"] and etat.get("nom_config") in (attendu["base"],
                                                                                              attendu["adaptateur"]),
        "révision de l'adaptateur": etat.get("revision_adaptateur_cache") == attendu["revision_adaptateur"],
        "révision de la base": etat.get("revision_base_cache") == attendu["revision_base"]
        and etat.get("revision_config") in (attendu["revision_base"], attendu["revision_adaptateur"]),
        "type numérique": etat.get("dtype") == attendu["dtype"],
    }
    for nom, ok in controles.items():
        if not ok:
            raise GardeArret(f"garde « juge » tombée : {nom} du modèle chargé différent du manifeste")
    return "passée"


def depense_courante(depense: dict, maintenant: float | None = None) -> float:
    maintenant = time.time() if maintenant is None else maintenant
    return float(depense["d_avant"]) + float(depense["c"]) * max(0.0, maintenant - float(depense["creation"])) / 3600


class JournaliseurLocal:
    """Remplace `obf_reps.logging.WAndBLogger` ; même signature de construction."""

    def __init__(self, log_file=None, username=None, metadata=None, *, config: ConfigJournal | None = None,
                 cache_juge: dict | None = None, horloge=time.time):
        self.tables: dict[str, list[str]] = {}
        self._cfg = config or ConfigJournal.lire(os.environ["TEMOIN_BAILEY_CONFIG"])
        d = Path(self._cfg.dossier_journal)
        d.mkdir(parents=True, exist_ok=True)
        noms = {"notes": cv.JOURNAL_NOTES, "tech": cv.JOURNAL_TECHNIQUE, "eg": cv.JOURNAL_EGALITES,
                "g": cv.JOURNAL_GARDES}
        if any((d / Path(n).name).exists() for n in noms.values()):
            sys.stderr.write("garde « dossier neuf » tombée : journal déjà présent\n")
            raise GardeArret("garde « dossier neuf » tombée : journal déjà présent")
        self._f = {k: open(d / Path(n).name, "a", encoding="utf-8") for k, n in noms.items()}
        self._cache_juge = cache_juge
        self._horloge = horloge
        self._t0 = time.perf_counter()
        self._attendues = None
        self._juge_verifie = False
        self._tour = -1
        self._etiquettes: list[str] = []
        self._evals: list[tuple] = []
        self._notes_juge: list[float] = []
        self._cibles: list[str | None] = []
        self._pas = 0
        self._compte_pas = False
        self._longueur_tour0 = None
        self._suffixes: list[str] = []
        self._ecrire("tech", {"type": "ouverture", "execution": self._cfg.execution,
                              "metadata_empreinte": cv.sha_texte(json.dumps(metadata, sort_keys=True, default=str))})

    # --- utilitaires ------------------------------------------------------------------------------------------------
    def _ecrire(self, cle: str, objet: dict) -> None:
        _ecrire(self._f[cle], {**objet, "t": round(time.perf_counter() - self._t0, 3)})

    def _garde(self, nom: str, fonction, *args) -> None:
        try:
            fonction(*args)
        except GardeArret as err:
            self._ecrire("g", {"garde": nom, "etat": "tombée", "tour": self._tour, "message": str(err)})
            raise
        self._ecrire("g", {"garde": nom, "etat": "passée", "tour": self._tour})

    def _tomber(self, nom: str, message: str):
        def f():
            raise GardeArret(message)
        self._garde(nom, f)

    # --- interface du code public ------------------------------------------------------------------------------------
    def log(self, data: dict) -> None:
        if "loss" in data and self._compte_pas:
            self._pas += 1
        cles = sorted(data)
        if cles in (["loss"], ["softprompt_norm"], ["grad_norm"]) or (
                len(cles) == 1 and cles[0].startswith("probe_loss_layer_")):
            return  # comptées (pertes), non journalisées une à une
        valeurs = {k: data[k] for k in cles if isinstance(data[k], (int, float)) and not isinstance(data[k], bool)}
        cle = "notes" if any(k in ("avg_behavior_score", "behavior_success_rate") for k in cles) else "tech"
        self._ecrire(cle, {"type": "log", "tour": self._tour, "valeurs": valeurs})

    def create_table(self, table_name: str, columns: list[str]) -> None:
        self.tables[table_name] = list(columns)
        if table_name.startswith("behavior_evaluation_"):
            self._compte_pas = False
            self._etiquettes.append(table_name)
            self._ecrire("tech", {"type": "pas", "tour": self._tour, "n": self._pas})

    def log_to_table(self, data: list, table_name: str) -> None:
        if table_name not in self.tables:
            self._tomber("table", "garde « table » tombée : table non créée")
        if len(data) != len(self.tables[table_name]):
            self._tomber("table", "garde « table » tombée : nombre de colonnes")
        for x in data:
            _fermer_figure(x)
        ligne = dict(zip(self.tables[table_name], data))
        if table_name == "metric_evaluation":
            self._ligne_metrique(ligne)
        elif table_name.startswith("behavior_evaluation_"):
            self._ligne_comportement(table_name, ligne)
        else:
            self._ecrire("tech", {"type": "table_autre", "table": table_name})

    def log_tables(self) -> None:
        pass

    def log_table_name(self, table_name: str) -> None:
        pass

    # --- lignes ------------------------------------------------------------------------------------------------------
    def _ligne_comportement(self, table: str, ligne: dict) -> None:
        if not self._juge_verifie:
            cache = self._cache_juge
            if cache is None:
                from strong_reject.evaluate import cached_models as cache
            etat = etat_juge_charge(cache, self._cfg.cache_hf)
            self._ecrire("tech", {"type": "juge_charge", "etat": etat})
            self._garde("juge", garde_juge, etat, self._cfg.juge, "TESTING" not in os.environ)
            self._juge_verifie = True
        i = len(self._notes_juge)
        self._notes_juge.append(float(ligne["behavior_score"]))
        self._cibles.append(cv.sha_texte(ligne["beh_target"]))
        self._ecrire("notes", {"type": "comportement", "table": table, "tour": self._tour, "index": i,
                               "note_juge": float(ligne["behavior_score"]),
                               "empreinte_entree": cv.sha_texte(ligne["input_text"]),
                               "empreinte_cible": cv.sha_texte(ligne["beh_target"]),
                               "empreinte_reponse": cv.sha_texte(ligne["tuned_gen_text"]),
                               "empreinte_reponse_sans_suffixe": cv.sha_texte(ligne["standard_gen_text"])})

    def _ligne_metrique(self, ligne: dict) -> None:
        etiquette = str(ligne["at_def_epoch"])
        if ligne.get("attack_suffix") is not None:
            self._tomber("suffixe au journal", "garde « suffixe au journal » tombée : le journal ne reçoit pas de suffixe")
        benignes = json.loads(ligne["standard_benign_scores"])
        sans = json.loads(ligne["standard_harmful_scores"])
        avec = json.loads(ligne["obfuscated_harmful_scores"])
        passees = {k: v for k, v in json.loads(ligne["score_plotting_data"]).items()
                   if k.startswith("obf_harmful_att_def_epoch_")}
        longueur = ligne.get("attack_suffix_len")
        defenseur = etiquette.endswith("defender just went")
        if defenseur:
            self._nouveau_tour(etiquette)
        self._etiquettes.append(etiquette)
        self._ecrire("notes", {"type": "metrique", "etiquette": etiquette, "tour": self._tour, "benignes": benignes,
                               "nuisibles_sans_suffixe": sans, "nuisibles_avec_suffixe": avec,
                               "attaques_passees": passees})
        self._ecrire("tech", {"type": "evaluation", "etiquette": etiquette, "tour": self._tour,
                              "longueur_suffixe": longueur, **_memoire()})
        egal = sum(1 for a, b in zip(avec, sans) if a == b) if len(avec) == len(sans) else None
        self._ecrire("eg", {"etiquette": etiquette, "egalites_avec_sans_suffixe": egal})
        self._evals.append((benignes, avec, sans))
        if defenseur and self._tour == 0:
            self._garde("sonde orientée", an.garde_sonde_orientee, sans, benignes)
        if defenseur:
            self._compte_pas = True
        else:
            self._fin_de_tour(longueur)
        self._garde("dépense", an.garde_depense, depense_courante(self._cfg.depense, self._horloge()),
                    float(self._cfg.depense["b"]))

    def _nouveau_tour(self, etiquette: str) -> None:
        e = self._tour + 1
        if etiquette != cv.DEFENSEUR.format(e=e):
            self._tomber("suite des étiquettes", "garde « suite des étiquettes » tombée")
        self._tour, self._etiquettes, self._evals, self._notes_juge, self._cibles, self._pas = e, [], [], [], [], 0

    def _fin_de_tour(self, longueur) -> None:
        e = self._tour
        self._garde("par tour", an.garde_par_tour, self._evals, self._notes_juge, self._etiquettes,
                    cv.etiquettes_attendues(e), self._pas, self._cfg.pas_attendus, cv.EVALUATIONS_PAR_TOUR)
        if self._attendues is None:
            self._attendues = [cv.sha_texte(r) for r in reponses_attendues(self._cfg.dossier_jeu)]
        self._garde("appariement", an.garde_appariement, self._cibles, self._attendues)
        emp, emp0 = self._empreintes_suffixe(cv.chemin_params(self._cfg.dossier_params, e))
        if e == 0:
            self._longueur_tour0 = longueur
        self._garde("suffixe appris", an.garde_suffixe_appris, emp, emp0, list(self._suffixes), longueur,
                    self._longueur_tour0)
        self._suffixes.append(emp)
        self._ecrire("tech", {"type": "fin_de_tour", "tour": e, "pas": self._pas, "empreinte_valeurs_suffixe": emp,
                              "empreinte_valeurs_initiales": emp0, "horloge": self._horloge()})

    @staticmethod
    def _empreintes_suffixe(chemin: Path) -> tuple[str, str]:
        if not chemin.exists():
            return "", ""
        import pickle
        with open(chemin, "rb") as f:
            p = pickle.load(f)
        return cv.empreinte_valeurs(p.params), cv.empreinte_valeurs(p.init_params)

    def fermer(self) -> None:
        for f in self._f.values():
            if not f.closed:
                f.close()
