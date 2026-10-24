"""La boucle externe du noyau : amorcer, exécuter une génération, juger, archiver, relancer le successeur.

Le noyau n'impose aucune organisation ni aucune règle de sélection ; il tient ce que l'essaim ne peut pas tenir
lui-même : les clés et le journal (couche d'appel), le juge (tâches cachées), le bac à sable, l'archive, les bornes
de l'humain (générations, budget, temps), et l'arrêt sur ordre (fichier `STOP` dans le dossier du run).
"""
from __future__ import annotations

import datetime as _dt
import json
import pathlib
import platform
import shutil
import sys

import numpy as np

from . import archive as _archive, bac_a_sable, contrat, taches as _taches
from .appels import Appelant, Arret, cv
from .serveur import ServeurAppels


def _heure() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Noyau:
    def __init__(self, racine: str | pathlib.Path, mission: str, banque: dict, budget_generation: dict,
                 plafond_total_usd: float, generations_max: int, appelants: dict | None = None, reel: bool = False,
                 go_id: str | None = None, isoler_reseau: bool = False, entropie: int | None = None,
                 especes_amorcage: list[str] | None = None, etiquette_run: str = ""):
        self.racine = pathlib.Path(racine)
        self.racine.mkdir(parents=True, exist_ok=True)
        self.mission = mission
        self.banque = banque
        self.budget = dict(budget_generation)
        self.plafond_total = float(plafond_total_usd)
        self.generations_max = int(generations_max)
        self.appelants = appelants
        self.reel, self.go_id, self.isoler_reseau = bool(reel), go_id, bool(isoler_reseau)
        self.especes_amorcage = list(especes_amorcage or contrat.ESPECES_DISPONIBLES)
        self.archive = _archive.Archive(self.racine / "archive")
        self.depense_totale = 0.0
        self.n_appels_total = 0
        self.lignees: dict[str, dict] = {}
        self.evenements: list[dict] = []
        self.graines = np.random.SeedSequence(entropie)
        self.manifeste = {
            "run": etiquette_run or self.racine.name, "debut_utc": _heure(), "reel": self.reel, "go_id": go_id,
            "entropie_seed_sequence": int(self.graines.entropy), "python": sys.version.split()[0], "numpy": np.__version__,
            "plateforme": platform.platform(), "collisionneur_v25_empreinte": getattr(cv, "__empreinte_fichier__", None),
            "budget_generation": self.budget, "plafond_total_usd": self.plafond_total, "generations_max": self.generations_max,
            "isolation_reseau": self.isoler_reseau, "n_taches_entrainement": len(banque["train"]), "n_taches_test": len(banque["test"]),
            "mission_sha256": __import__("hashlib").sha256(mission.encode("utf-8")).hexdigest(),
        }
        if self.reel:
            if not self.go_id:
                raise Arret("mode réel sans GO : refusé")
            if self.isoler_reseau and not bac_a_sable.isolation_reseau_disponible():
                raise Arret("mode réel : isolation réseau demandée mais indisponible (unshare -rn)")
        (self.racine / "manifeste-run.json").write_text(json.dumps(self.manifeste, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- journal du noyau ----
    def _evenement(self, **d):
        d["quand_utc"] = _heure()
        self.evenements.append(d)
        with (self.racine / "evenements.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")

    def _plafond_restant(self) -> float:
        return max(0.0, self.plafond_total - self.depense_totale)

    def _appelant(self, dossier: pathlib.Path) -> Appelant:
        plafond = min(float(self.budget["usd_max"]), self._plafond_restant())
        return Appelant(dossier, plafond, self.appelants, self.reel, self.go_id)

    # ---- amorçage ----
    def amorcer(self) -> dict:
        exemples = self.banque["train"][:6]
        prompt = contrat.prompt_amorcage(self.mission, _taches.ETIQUETTES, self.budget, exemples)
        (self.racine / "amorcage-consigne.txt").write_text(prompt, encoding="utf-8")
        resultats = {}
        for espece in self.especes_amorcage:
            lignee = espece.lower().replace("_", "-")
            dossier = self.racine / "lignees" / lignee / "g000"
            dossier.mkdir(parents=True, exist_ok=True)
            appelant = self._appelant(dossier / "noyau-amorcage")
            res = appelant.appeler(espece, "amorcage", prompt, role="amorcage")
            self.depense_totale += appelant.depense_usd
            self.n_appels_total += 1
            fichiers = contrat.extraire_fichiers(res.texte) if res.ok else {}
            problemes = contrat.ecrire_organisme(fichiers, dossier) if fichiers else ["aucun fichier dans la réponse"]
            if not res.ok:
                problemes = [f"appel d'amorçage en statut {res.statut}"] + problemes
            statut = "ORGANISME_VALIDE" if not problemes else "AMORCAGE_INVALIDE"
            resultats[lignee] = {"espece": espece, "statut": statut, "problemes": problemes, "n_fichiers": len(fichiers),
                                 "id_appel": res.identifiant, "cout_usd": appelant.depense_usd}
            if statut == "ORGANISME_VALIDE":
                self.lignees[lignee] = {"espece_amorcage": espece, "generation": 0, "organisme": dossier / "organisme", "active": True}
            self._evenement(etape="amorcage", lignee=lignee, **resultats[lignee])
        return resultats

    # ---- une génération ----
    def executer_generation(self, lignee: str) -> dict:
        etat = self.lignees[lignee]
        g = etat["generation"]
        organisme = etat["organisme"]
        travail = self.racine / "travail" / lignee / f"g{g:03d}"
        if travail.exists():
            shutil.rmtree(travail)
        travail.mkdir(parents=True)
        rng = np.random.default_rng(self.graines.spawn(1)[0])
        ordre_train = rng.permutation(len(self.banque["train"]))
        ordre_test = rng.permutation(len(self.banque["test"]))
        contexte = {
            "generation": g, "lignee": lignee, "mission": contrat.mission_texte(self.mission, _taches.ETIQUETTES),
            "dossier_travail": str(travail), "dossier_archive": str(self.archive.racine),
            "taches_entrainement": [dict(_taches.masquer(self.banque["train"][i]), verite=self.banque["train"][i]["verite"]) for i in ordre_train],
            "taches_test": [_taches.masquer(self.banque["test"][i]) for i in ordre_test],
            "budget": {"appels_max": int(self.budget["appels_max"]), "usd_max": round(min(float(self.budget["usd_max"]), self._plafond_restant()), 4),
                       "temps_max_s": int(self.budget["temps_max_s"])},
            "historique": self.archive.historique(lignee),
        }
        appelant = self._appelant(travail / "noyau")
        chemin_socket = str(travail / "noyau.sock")
        if len(chemin_socket) > 100:  # limite des sockets Unix
            chemin_socket = f"/tmp/essaim-{lignee[:12]}-g{g}.sock"
        bac_a_sable.preparer(travail, organisme, contexte)
        with ServeurAppels(appelant, chemin_socket, int(self.budget["appels_max"])) as serveur:
            execution = bac_a_sable.executer(travail, chemin_socket, int(self.budget["temps_max_s"]), isoler_reseau=self.isoler_reseau)
            n_appels = serveur.n_appels
            refus = list(serveur.refus)
        self.depense_totale += appelant.depense_usd
        self.n_appels_total += n_appels
        # jugement externe
        reponses = {}
        chemin_rep = travail / "reponses_test.json"
        probleme_reponses = None
        if chemin_rep.exists():
            try:
                brut = json.loads(chemin_rep.read_text(encoding="utf-8"))
                if isinstance(brut, dict):
                    for t in self.banque["test"]:
                        r = brut.get(t["id"])
                        if isinstance(r, dict) and str(r.get("etiquette", "")).strip().lower() in _taches.ETIQUETTES[t["famille"]]:
                            reponses[t["id"]] = {"etiquette": str(r["etiquette"]).strip().lower()}
                else:
                    probleme_reponses = "reponses_test.json n'est pas un objet"
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                probleme_reponses = f"reponses_test.json illisible : {str(e)[:100]}"
        else:
            probleme_reponses = "reponses_test.json absent"
        score = _taches.evaluer(reponses, self.banque["test"])
        score["probleme_reponses"] = probleme_reponses
        # métrique proposée par l'organisme (archivée, jamais utilisée par le noyau)
        metrique = None
        chemin_metrique = travail / "metrique_proposee.json"
        if chemin_metrique.exists():
            try:
                m = json.loads(chemin_metrique.read_text(encoding="utf-8"))
                metrique = m if isinstance(m, dict) else {"illisible": True}
            except (json.JSONDecodeError, UnicodeDecodeError):
                metrique = {"illisible": True}
        # successeur
        successeur = travail / "successeur" / "organisme"
        problemes_succ = contrat.valider_organisme(successeur) if successeur.exists() else ["successeur absent"]
        a_successeur = not problemes_succ
        resume = {"statut": execution["code"], "execution": execution, "n_appels": n_appels, "cout_usd": round(appelant.depense_usd, 4),
                  "refus_noyau": refus, "successeur": a_successeur, "problemes_successeur": problemes_succ,
                  "n_reponses_test": len(reponses), "score": score["score"], "metrique_proposee": metrique}
        self.archive.deposer(lignee, g, organisme, travail, appelant.journal, score, resume)
        self._evenement(etape="generation", lignee=lignee, generation=g, statut=execution["code"], score=score["score"],
                        n_appels=n_appels, cout_usd=resume["cout_usd"], successeur=a_successeur, cumul_usd=round(self.depense_totale, 4))
        if a_successeur and g + 1 < self.generations_max:
            prochain = self.racine / "lignees" / lignee / f"g{g + 1:03d}" / "organisme"
            prochain.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(successeur, prochain, symlinks=False)
            etat.update(generation=g + 1, organisme=prochain)
        else:
            etat["active"] = False
            etat["fin"] = "sans successeur valide" if not a_successeur else "générations maximales"
        return resume

    # ---- boucle ----
    def boucler(self) -> dict:
        while True:
            if (self.racine / "STOP").exists():
                self._evenement(etape="arret", raison="fichier STOP")
                break
            actives = [l for l, e in self.lignees.items() if e["active"]]
            if not actives:
                self._evenement(etape="arret", raison="aucune lignée active")
                break
            if self._plafond_restant() <= 0:
                self._evenement(etape="arret", raison="plafond total atteint")
                break
            for lignee in actives:
                if (self.racine / "STOP").exists() or self._plafond_restant() <= 0:
                    break
                self.executer_generation(lignee)
        return self.rapport()

    def rapport(self) -> dict:
        lignes = self.archive.lignes()
        rapport = {
            "avertissement": "NON OPPOSABLE (R7) : résultats d'un essaim de modèles, juge externe en simulation ou préenregistré ; aucun chiffre n'est une preuve",
            "manifeste": self.manifeste, "fin_utc": _heure(), "depense_totale_usd": round(self.depense_totale, 4),
            "n_appels_total": self.n_appels_total, "lignees": {l: {k: (str(v) if isinstance(v, pathlib.Path) else v) for k, v in e.items()} for l, e in self.lignees.items()},
            "generations": lignes,
            "courbes": {l: [x["score"] for x in lignes if x["lignee"] == l] for l in {x["lignee"] for x in lignes}},
        }
        n = 1
        while (self.racine / f"rapport-v{n}.json").exists():
            n += 1
        chemin = self.racine / f"rapport-v{n}.json"
        chemin.write_text(json.dumps(rapport, ensure_ascii=False, indent=1), encoding="utf-8")
        _archive.sceller(chemin)
        return rapport
