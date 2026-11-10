"""Journaliseur local substitué à Weights & Biases — témoin « attaque publiée reproduite » (Bailey et collègues), v1.

Écart 2 du préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) ; point 1 de la liste
« ce qui manque à la condition 6 » de la contre-lecture du code (`151eee65…`).

Le lanceur (`execution_v1.py`) remplace, dans le processus qui exécute le code public, la classe `WAndBLogger` par
`JournaliseurLocal` (sans modifier aucun fichier du dépôt public). Le journaliseur :
- écrit au fil de l'eau (une ligne JSON par événement, vidée et synchronisée sur disque) les notes brutes de la sonde
  avec leur étiquette, les notes du juge, les durées, la mémoire, la longueur de suffixe journalisée, les empreintes des
  textes produits et des entrées ;
- n'écrit ni textes ni figures, et ferme chaque figure reçue ;
- fournit l'attribut `tables` que lit le code public (`evaluate.py`, l. 1103) ;
- n'envoie rien vers un service externe ; ne reçoit ni suffixe ni sonde (seule la longueur du suffixe arrive) ;
- écrit au seul journal scellé `egalites-scellees-v1.jsonl`, sans jamais l'imprimer, le compte des entrées dont la note
  avec suffixe égale la note sans suffixe ;
- porte les gardes qui s'exécutent dans le processus du code public : garde du juge (après son premier appel), sonde
  orientée (début du tour 0), gardes par tour (longueurs, valeurs finies, notes bénignes non constantes, étiquettes,
  pas, suffixe appris, appariement, dépense). Une garde qui tombe écrit son état au journal des gardes, puis lève
  `GardeArret`, ce qui arrête le processus ; son message ne porte jamais de valeur de note.

Configuration : variable d'environnement `TEMOIN_BAILEY_CONFIG`, chemin d'un JSON écrit par le lanceur (voir
`ConfigJournal`).
"""
from __future__ import annotations

import json
import math
import os
import resource
import time
from dataclasses import dataclass, field
from pathlib import Path

from ..gardes import GardeArret
from . import analyse_v2 as an
from . import conventions_v1 as cv


@dataclass
class ConfigJournal:
    dossier_journal: str
    dossier_params: str
    dossier_jeu: str
    pas_attendus: int
    juge: dict  # {"nom", "revision", "dtype", "adaptateur", "base"} attendus (manifeste)
    depense: dict  # {"d_avant": USD, "c": USD/h, "creation": epoch s, "b": USD}
    testing_absent_au_lancement: bool = True
    execution: str = ""
    extra: dict = field(default_factory=dict)

    @classmethod
    def lire(cls, chemin: str | os.PathLike) -> "ConfigJournal":
        return cls(**json.loads(Path(chemin).read_text(encoding="utf-8")))


def _ecrire(f, objet: dict) -> None:
    f.write(json.dumps(objet, ensure_ascii=False, sort_keys=True) + "\n")
    f.flush()
    os.fsync(f.fileno())


def _fermer_figure(x) -> bool:
    try:
        from matplotlib.figure import Figure
    except Exception:  # matplotlib absent : aucune figure possible
        return False
    if isinstance(x, Figure):
        import matplotlib.pyplot as plt
        plt.close(x)
        return True
    return False


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
    """Les 200 réponses de référence (validation puis test), lues comme le code public les lit."""
    import pandas as pd
    out = []
    for split in ("val", "test"):
        df = pd.read_csv(Path(dossier_jeu) / f"harmful_{split}_no_spec_tokens.csv")
        out += [row["response"] for _, row in df.iterrows()]
    return out


def etat_juge_charge(cached_models: dict) -> dict:
    """Nom, révision, type numérique du modèle du juge effectivement chargé ; modèle de base s'il s'agit d'un
    adaptateur. Lu dans le cache du paquet `strong_reject` (`evaluate.py` l. 459-482 au commit épinglé)."""
    if "strongreject_finetuned" not in cached_models:
        raise GardeArret("garde « juge » tombée : modèle du juge absent du cache après son premier appel")
    modele = cached_models["strongreject_finetuned"][0]
    conf = getattr(modele, "config", None)
    peft = getattr(modele, "peft_config", None)
    base = None
    if peft:
        premier = next(iter(peft.values()))
        base = getattr(premier, "base_model_name_or_path", None)
    return {"nom": getattr(conf, "_name_or_path", None), "revision": getattr(conf, "_commit_hash", None),
            "dtype": str(getattr(modele, "dtype", None)), "adaptateur": bool(peft), "base": base}


def garde_juge(etat: dict, attendu: dict, testing_absent: bool) -> str:
    if not testing_absent:
        raise GardeArret("garde « juge » tombée : variable TESTING présente au lancement du processus")
    for cle in ("nom", "revision", "dtype", "adaptateur", "base"):
        if etat.get(cle) != attendu.get(cle):
            raise GardeArret(f"garde « juge » tombée : {cle} du modèle chargé différent du manifeste")
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
        for nom in ("journal-v1.jsonl", "egalites-scellees-v1.jsonl", "gardes-v1.jsonl"):
            if (d / nom).exists():
                raise GardeArret("garde « dossier neuf » tombée : journal déjà présent")
        self._j = open(d / "journal-v1.jsonl", "a", encoding="utf-8")
        self._eg = open(d / "egalites-scellees-v1.jsonl", "a", encoding="utf-8")
        self._g = open(d / "gardes-v1.jsonl", "a", encoding="utf-8")
        self._cache_juge = cache_juge
        self._horloge = horloge
        self._t0 = time.perf_counter()
        self._attendues = None
        self._juge_verifie = False
        # état du tour courant
        self._tour = -1
        self._etiquettes: list[str] = []
        self._evals: list[tuple] = []
        self._notes_juge: list[float] = []
        self._cibles: list[str | None] = []
        self._pas = 0
        self._compte_pas = False
        self._longueur_tour0 = None
        self._suffixes: list[str] = []
        _ecrire(self._j, {"type": "ouverture", "execution": self._cfg.execution,
                          "metadata_empreinte": cv.sha_texte(json.dumps(metadata, sort_keys=True, default=str)),
                          "t": 0.0})

    # --- utilitaires ------------------------------------------------------------------------------------------------
    def _t(self) -> float:
        return round(time.perf_counter() - self._t0, 3)

    def _garde(self, nom: str, fonction, *args):
        try:
            fonction(*args)
        except GardeArret as err:
            _ecrire(self._g, {"garde": nom, "etat": "tombée", "tour": self._tour, "message": str(err), "t": self._t()})
            raise
        _ecrire(self._g, {"garde": nom, "etat": "passée", "tour": self._tour, "t": self._t()})

    # --- interface du code public ------------------------------------------------------------------------------------
    def log(self, data: dict) -> None:
        if "loss" in data and self._compte_pas:
            self._pas += 1
        cles = sorted(data)
        valeurs = {k: data[k] for k in cles if isinstance(data[k], (int, float)) and not isinstance(data[k], bool)}
        # les pertes par pas restent comptées, pas journalisées une à une (volume) ; le reste est écrit
        if cles in (["loss"], ["softprompt_norm"], ["grad_norm"]) or (len(cles) == 1 and cles[0].startswith("probe_loss_layer_")):
            return
        _ecrire(self._j, {"type": "log", "tour": self._tour, "valeurs": valeurs, "t": self._t()})

    def create_table(self, table_name: str, columns: list[str]) -> None:
        self.tables[table_name] = list(columns)
        if table_name.startswith("behavior_evaluation_"):
            self._compte_pas = False
            self._etiquettes.append(table_name)
            _ecrire(self._j, {"type": "pas", "tour": self._tour, "n": self._pas, "t": self._t()})

    def log_to_table(self, data: list, table_name: str) -> None:
        if table_name not in self.tables:
            raise GardeArret("garde « table » tombée : table non créée")
        colonnes = self.tables[table_name]
        if len(data) != len(colonnes):
            raise GardeArret("garde « table » tombée : nombre de colonnes")
        for x in data:
            _fermer_figure(x)
        ligne = dict(zip(colonnes, data))
        if table_name == "metric_evaluation":
            self._ligne_metrique(ligne)
        elif table_name.startswith("behavior_evaluation_"):
            self._ligne_comportement(table_name, ligne)
        else:
            _ecrire(self._j, {"type": "table_autre", "table": table_name, "t": self._t()})

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
            etat = etat_juge_charge(cache)
            _ecrire(self._j, {"type": "juge_charge", "etat": etat, "t": self._t()})
            self._garde("juge", garde_juge, etat, self._cfg.juge, self._cfg.testing_absent_au_lancement)
            self._juge_verifie = True
        i = len(self._notes_juge)
        note = ligne["behavior_score"]
        self._notes_juge.append(float(note))
        self._cibles.append(cv.sha_texte(ligne["beh_target"]))
        _ecrire(self._j, {"type": "comportement", "table": table, "tour": self._tour, "index": i,
                          "note_juge": float(note), "empreinte_entree": cv.sha_texte(ligne["input_text"]),
                          "empreinte_cible": cv.sha_texte(ligne["beh_target"]),
                          "empreinte_reponse": cv.sha_texte(ligne["tuned_gen_text"]),
                          "empreinte_reponse_sans_suffixe": cv.sha_texte(ligne["standard_gen_text"]), "t": self._t()})

    def _ligne_metrique(self, ligne: dict) -> None:
        etiquette = str(ligne["at_def_epoch"])
        benignes = json.loads(ligne["standard_benign_scores"])
        sans = json.loads(ligne["standard_harmful_scores"])
        avec = json.loads(ligne["obfuscated_harmful_scores"])
        passees = {k: v for k, v in json.loads(ligne["score_plotting_data"]).items()
                   if k.startswith("obf_harmful_att_def_epoch_")}
        longueur = ligne.get("attack_suffix_len")
        if ligne.get("attack_suffix") is not None:
            raise GardeArret("garde « suffixe au journal » tombée : le journal ne reçoit pas de suffixe")
        defenseur = etiquette.endswith("defender just went")
        if defenseur:
            self._nouveau_tour(etiquette)
        self._etiquettes.append(etiquette)
        _ecrire(self._j, {"type": "metrique", "etiquette": etiquette, "tour": self._tour, "benignes": benignes,
                          "nuisibles_sans_suffixe": sans, "nuisibles_avec_suffixe": avec, "attaques_passees": passees,
                          "longueur_suffixe": longueur, "t": self._t(), **_memoire()})
        egal = sum(1 for a, b in zip(avec, sans) if a == b) if len(avec) == len(sans) else None
        _ecrire(self._eg, {"etiquette": etiquette, "egalites_avec_sans_suffixe": egal})
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
            _ecrire(self._g, {"garde": "suite des étiquettes", "etat": "tombée", "tour": e, "t": self._t()})
            raise GardeArret("garde « suite des étiquettes » tombée")
        self._tour, self._etiquettes, self._evals, self._notes_juge, self._cibles, self._pas = e, [], [], [], [], 0

    def _fin_de_tour(self, longueur) -> None:
        e = self._tour
        self._garde("par tour", an.garde_par_tour, self._evals, self._notes_juge, self._etiquettes,
                    cv.etiquettes_attendues(e), self._pas, self._cfg.pas_attendus)
        if self._attendues is None:
            self._attendues = [cv.sha_texte(r) for r in reponses_attendues(self._cfg.dossier_jeu)]
        self._garde("appariement", an.garde_appariement, self._cibles, self._attendues)
        chemin = cv.chemin_params(self._cfg.dossier_params, e)
        emp, emp0 = self._empreintes_suffixe(chemin)
        if e == 0:
            self._longueur_tour0 = longueur
        self._garde("suffixe appris", an.garde_suffixe_appris, emp, emp0, list(self._suffixes), longueur,
                    self._longueur_tour0)
        self._suffixes.append(emp)
        _ecrire(self._j, {"type": "fin_de_tour", "tour": e, "empreinte_valeurs_suffixe": emp,
                          "empreinte_valeurs_initiales": emp0, "t": self._t()})

    @staticmethod
    def _empreintes_suffixe(chemin: Path) -> tuple[str, str]:
        if not chemin.exists():
            return "", ""
        import pickle
        with open(chemin, "rb") as f:
            p = pickle.load(f)
        return cv.empreinte_valeurs(p.params), cv.empreinte_valeurs(p.init_params)

    def fermer(self) -> None:
        for f in (self._j, self._eg, self._g):
            if not f.closed:
                f.close()


def verifier_fini(x: float) -> bool:
    return math.isfinite(x)
