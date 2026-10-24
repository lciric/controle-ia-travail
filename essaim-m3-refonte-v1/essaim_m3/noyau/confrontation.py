"""Confrontation entre organismes (décision de Lazar du 24 octobre, 16:16 et 16:19, heure de Paris).

Chaque organisme peut livrer `organisme/metrique/` : `definition.md`, `calculer.py` (`calculer(dossier_sorties) ->
float`, du code objectif appliqué aux sorties d'un autre organisme) et `attaques.json` (tâches d'attaque avec vérité).
Pour chaque paire ordonnée (A, B) de lignées de **familles de fournisseur différentes** (sinon « non applicable ») :
1. le noyau relance l'organisme de B (sa dernière génération valide) sur les tâches d'attaque de A, en bac à sable,
   avec le budget donné — les attaques sont donc portées contre B par une suite écrite par une autre famille ;
2. il note les réponses de B avec les vérités de A (exactitude équilibrée) ;
3. il exécute `calculer.py` de A sur les sorties de B, en bac à sable, sans réseau : valeur ou « non calculée ».
Le score sur tâches cachées du noyau reste la mesure témoin ; aucune règle de choix du champion n'est appliquée
ici : tout est rapporté, et la métrique de choix est celle que l'humain a gelée par préenregistrement.
"""
from __future__ import annotations

import json
import pathlib
import shutil
import tarfile

import numpy as np

from . import bac_a_sable, contrat, taches as _taches
from .appels import Appelant
from .serveur import ServeurAppels


def extraire_organisme(archive_tar: pathlib.Path, cible: pathlib.Path) -> pathlib.Path:
    if cible.exists():
        shutil.rmtree(cible)
    cible.mkdir(parents=True)
    with tarfile.open(archive_tar, "r:gz") as tar:
        membres = [m for m in tar.getmembers() if m.isfile() and m.name.startswith("organisme/") and ".." not in m.name]
        tar.extractall(cible, members=membres, filter="data")
    return cible / "organisme"


def charger_metrique(organisme: pathlib.Path) -> dict:
    """Lit `metrique/` d'un organisme ; rend ce qui est valide et la liste des problèmes."""
    d = organisme / "metrique"
    if not d.is_dir():
        return {"present": False, "problemes": ["metrique/ absent"], "attaques": [], "calculer": None, "definition": None}
    problemes = []
    definition = (d / "definition.md").read_text(encoding="utf-8") if (d / "definition.md").exists() else None
    if definition is None:
        problemes.append("definition.md absent")
    calculer = d / "calculer.py"
    if not calculer.exists():
        problemes.append("calculer.py absent")
        calculer = None
    else:
        try:
            compile(calculer.read_text(encoding="utf-8"), str(calculer), "exec")
        except (SyntaxError, UnicodeDecodeError) as e:
            problemes.append(f"calculer.py : {str(e)[:120]}")
            calculer = None
    attaques, pb = [], []
    if (d / "attaques.json").exists():
        try:
            attaques, pb = _taches.valider_taches_attaque(json.loads((d / "attaques.json").read_text(encoding="utf-8")))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            pb = [f"attaques.json illisible : {str(e)[:100]}"]
    else:
        pb = ["attaques.json absent"]
    return {"present": True, "problemes": problemes + pb, "attaques": attaques, "calculer": calculer, "definition": definition}


class Confrontation:
    def __init__(self, noyau, dossier: pathlib.Path):
        self.noyau = noyau
        self.dossier = pathlib.Path(dossier)
        self.dossier.mkdir(parents=True, exist_ok=True)

    def _derniere_generation(self, lignee: str) -> dict | None:
        lignes = [l for l in self.noyau.archive.lignes(lignee) if l.get("statut") == "OK"]
        return lignes[-1] if lignes else None

    def _famille(self, lignee: str) -> str:
        return contrat.FAMILLES[self.noyau.lignees[lignee]["espece_amorcage"]]

    def _executer_sur_attaques(self, lignee_def: str, organisme: pathlib.Path, attaques: list[dict], etiquette: str) -> dict:
        travail = self.dossier / etiquette / "defense"
        if travail.exists():
            shutil.rmtree(travail)
        travail.mkdir(parents=True)
        rng = np.random.default_rng(self.noyau.graines.spawn(1)[0])
        ordre = rng.permutation(len(attaques))
        contexte = {
            "generation": -1, "lignee": lignee_def, "mission": contrat.mission_texte(self.noyau.mission, _taches.ETIQUETTES),
            "dossier_travail": str(travail), "dossier_archive": str(self.noyau.archive.vue),
            "taches_entrainement": [dict(_taches.masquer(t), verite=t["verite"]) for t in self.noyau.banque["train"]],
            "taches_test": [{"id": attaques[i]["id"], "famille": attaques[i]["famille"], "texte": attaques[i]["texte"],
                             "etiquettes": list(attaques[i]["etiquettes"])} for i in ordre],
            "budget": {"appels_max": int(self.noyau.budget["appels_max"]), "usd_max": round(min(float(self.noyau.budget["usd_max"]), self.noyau._plafond_restant()), 4),
                       "temps_max_s": int(self.noyau.budget["temps_max_s"])},
            "historique": self.noyau.archive.historique(lignee_def), "confrontation": True,
        }
        appelant = Appelant(travail / "noyau", min(float(self.noyau.budget["usd_max"]), self.noyau._plafond_restant()),
                            self.noyau.appelants, self.noyau.reel, self.noyau.go_id)
        socket = str(travail / "n.sock")
        if len(socket) > 100:
            socket = f"/tmp/essaim-conf-{etiquette[:20]}.sock"
        bac_a_sable.preparer(travail, organisme, contexte)
        with ServeurAppels(appelant, socket, int(self.noyau.budget["appels_max"])) as serveur:
            execution = bac_a_sable.executer(travail, socket, int(self.noyau.budget["temps_max_s"]), isoler_reseau=self.noyau.isoler_reseau)
            n_appels = serveur.n_appels
        self.noyau.depense_totale += appelant.depense_usd
        self.noyau.n_appels_total += n_appels
        reponses = {}
        f = travail / "reponses_test.json"
        if f.exists():
            try:
                brut = json.loads(f.read_text(encoding="utf-8"))
                if isinstance(brut, dict):
                    for t in attaques:
                        r = brut.get(t["id"])
                        if isinstance(r, dict) and str(r.get("etiquette", "")).strip().lower() in t["etiquettes"]:
                            reponses[t["id"]] = {"etiquette": str(r["etiquette"]).strip().lower()}
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass
        score = _taches.evaluer_generique(reponses, attaques)
        return {"execution": execution["code"], "n_appels": n_appels, "cout_usd": round(appelant.depense_usd, 4),
                "score_attaques": score, "travail": travail}

    def confronter(self, lignees: list[str] | None = None) -> dict:
        lignees = [l for l in (lignees or list(self.noyau.lignees)) if self._derniere_generation(l)]
        organismes, metriques = {}, {}
        for l in lignees:
            g = self._derniere_generation(l)
            org = extraire_organisme(self.noyau.archive.racine / g["chemin"] / "organisme.tar.gz", self.dossier / "organismes" / l)
            organismes[l] = org
            metriques[l] = charger_metrique(org)
        paires = []
        for a in lignees:
            for b in lignees:
                if a == b:
                    continue
                if self._famille(a) == self._famille(b):
                    paires.append({"attaquant": a, "defendeur": b, "applicable": False, "raison": "même famille de fournisseur"})
                    continue
                ma = metriques[a]
                res = {"attaquant": a, "defendeur": b, "applicable": True, "famille_attaquant": self._famille(a),
                       "famille_defendeur": self._famille(b), "problemes_metrique": ma["problemes"]}
                if ma["attaques"]:
                    att = self._executer_sur_attaques(b, organismes[b], ma["attaques"], f"{a}__vers__{b}")
                    res.update({"n_attaques": len(ma["attaques"]), "execution_defense": att["execution"],
                                "n_appels": att["n_appels"], "cout_usd": att["cout_usd"], "score_attaques": att["score_attaques"]})
                    sorties = att["travail"]
                else:
                    res.update({"n_attaques": 0, "score_attaques": None})
                    sorties = None
                if ma["calculer"] is not None and sorties is not None:
                    res["metrique"] = bac_a_sable.executer_metrique(self.dossier / f"{a}__vers__{b}" / "metrique", ma["calculer"].parent, sorties)
                else:
                    res["metrique"] = {"code": "NON_APPLICABLE", "valeur": None, "calculee": False}
                paires.append(res)
        rapport = {"avertissement": "NON OPPOSABLE (R7) ; aucune règle de choix du champion n'est appliquée ici",
                   "lignees": {l: {"famille": self._famille(l), "metrique_presente": metriques[l]["present"],
                                   "problemes_metrique": metriques[l]["problemes"], "n_attaques": len(metriques[l]["attaques"]),
                                   "definition": (metriques[l]["definition"] or "")[:2000]} for l in lignees},
                   "paires": paires, "scores_temoin": self.noyau._scores_finaux(self.noyau.archive.lignes()),
                   "depense_totale_usd": round(self.noyau.depense_totale, 4)}
        n = 1
        while (self.dossier / f"confrontation-v{n}.json").exists():
            n += 1
        (self.dossier / f"confrontation-v{n}.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
        from .archive import sceller
        sceller(self.dossier / f"confrontation-v{n}.json")
        return rapport
