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

import hashlib
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
    definition = (d / "definition.md").read_text(encoding="utf-8-sig") if (d / "definition.md").exists() else None
    if definition is None:
        problemes.append("definition.md absent")
    calculer = d / "calculer.py"
    if not calculer.exists():
        problemes.append("calculer.py absent")
        calculer = None
    else:
        try:
            compile(calculer.read_text(encoding="utf-8-sig"), str(calculer), "exec")
        except (SyntaxError, UnicodeDecodeError) as e:
            problemes.append(f"calculer.py : {str(e)[:120]}")
            calculer = None
    attaques, pb = [], []
    if (d / "attaques.json").exists():
        try:
            attaques, pb = _taches.valider_taches_attaque(json.loads((d / "attaques.json").read_text(encoding="utf-8-sig")))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            pb = [f"attaques.json illisible : {str(e)[:100]}"]
    else:
        pb = ["attaques.json absent"]
    return {"present": True, "problemes": problemes + pb, "attaques": attaques, "calculer": calculer, "definition": definition}


def empreintes_metrique(organisme: pathlib.Path) -> dict:
    """Empreintes de `organisme/metrique/` (arbre) et de `attaques.json` ; None si absents. Ne lit aucun score."""
    from .boucle import empreinte_arbre
    d = organisme / "metrique"
    if not d.is_dir():
        return {"present": False, "empreinte_metrique": None, "empreinte_attaques": None}
    att = d / "attaques.json"
    return {"present": True, "empreinte_metrique": empreinte_arbre(d),
            "empreinte_attaques": (hashlib.sha256(att.read_bytes()).hexdigest() if att.exists() else None)}


def relever_metriques(noyau, dossier: pathlib.Path) -> dict:
    """Après la boucle, avant tout gel : pour chaque lignée, la dernière génération valide, sa métrique (empreintes,
    nombre d'attaques valides, problèmes). Aucun score n'est lu. L'humain gèle ce relevé (compagnon `.sha256`,
    contre-lecture) : c'est l'addendum que `confronter` exige (CR-04)."""
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    releve = {"course": str(noyau.racine), "quand_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "lignees": {}}
    for l in sorted(noyau.lignees):
        lignes = [x for x in noyau.archive.lignes(l) if x.get("statut") == "OK" and not x.get("invalide") and not x.get("phase")]
        if not lignes:
            releve["lignees"][l] = {"generation": None, "metrique": {"present": False}, "problemes": ["aucune génération valide"]}
            continue
        g = lignes[-1]
        org = extraire_organisme(noyau.archive.racine / g["chemin"] / "organisme.tar.gz", dossier / "organismes" / l)
        m = charger_metrique(org)
        releve["lignees"][l] = {"generation": g["generation"], "empreinte_organisme": g.get("empreinte_organisme"), "famille": noyau.lignees[l].get("famille"),
                                "metrique": empreintes_metrique(org), "n_attaques_valides": len(m["attaques"]), "problemes": m["problemes"]}
    n = 1
    while (dossier / f"releve-metriques-v{n}.json").exists():
        n += 1
    f = dossier / f"releve-metriques-v{n}.json"
    f.write_text(json.dumps(releve, ensure_ascii=False, indent=1), encoding="utf-8")
    from .archive import sceller
    sceller(f)
    releve["fichier"] = str(f)
    return releve


def designations_et_concours(paires: list[dict], scores_temoin: dict[str, list[float]], lignees_info: dict[str, dict]) -> dict:
    """Décision de Lazar (24 octobre, 20:06 Paris : « tester les deux ») : les deux désignations du champion sont
    **rapportées** — (1) règle N-039 b : meilleur score témoin (test final) à la dernière génération lue ; (2)
    exactitude équilibrée moyenne en défense sur les attaques croisées ; plus (3) la désignation que donne chaque
    métrique discriminante (meilleur défendeur selon elle) — avec leur concordance. Seule (1) décide ; aucune règle
    n'est appliquée ici. Le « concours de métriques » met côte à côte chaque métrique : épreuve mécanique, valeurs par
    défendeur, tau-b avec le score témoin."""
    from ..analyse import tau_b_kendall
    temoin = {l: v[-1] for l, v in scores_temoin.items() if v}
    def meilleurs(d):
        if not d:
            return []
        m = max(d.values())
        return sorted(k for k, v in d.items() if v == m)
    defense: dict[str, list[float]] = {}
    par_metrique: dict[str, dict[str, float]] = {}
    for p in paires:
        if not p.get("applicable"):
            continue
        sa = (p.get("score_attaques") or {}).get("score")
        if sa is not None:
            defense.setdefault(p["defendeur"], []).append(float(sa))
        m = p.get("metrique") or {}
        if m.get("calculee") and p.get("metrique_discriminante"):
            par_metrique.setdefault(p["attaquant"], {})[p["defendeur"]] = float(m["valeur"])
    defense_moy = {l: round(sum(v) / len(v), 4) for l, v in defense.items()}
    designations = {"test_final_N039b": {"champion": meilleurs(temoin), "scores": temoin, "regle": "décide (N-039 b)"},
                    "attaques_croisees": {"champion": meilleurs(defense_moy), "scores": defense_moy, "regle": "rapportée"},
                    "par_metrique": {a: {"champion_selon_elle": meilleurs(vals), "valeurs": vals, "regle": "rapportée"} for a, vals in par_metrique.items()}}
    c1, c2 = set(designations["test_final_N039b"]["champion"]), set(designations["attaques_croisees"]["champion"])
    designations["concordance"] = {"test_final_vs_attaques": (bool(c1 & c2) if c1 and c2 else None),
                                   "test_final_vs_metriques": {a: (bool(c1 & set(d["champion_selon_elle"])) if c1 and d["champion_selon_elle"] else None)
                                                               for a, d in designations["par_metrique"].items()}}
    concours = {}
    for l, info in lignees_info.items():
        vals = par_metrique.get(l, {})
        defs = [d for d in vals if d in temoin]
        concours[l] = {"metrique_presente": info.get("metrique_presente"), "discriminance": info.get("discriminance"),
                       "definition": (info.get("definition") or "")[:600], "valeurs_par_defendeur": vals,
                       "tau_b_avec_temoin": tau_b_kendall([vals[d] for d in defs], [temoin[d] for d in defs]) if len(defs) >= 2 else {"tau_b": None, "n": len(defs)}}
    return {"designations": designations, "concours_metriques": concours,
            "avertissement": "désignations rapportées ; seule la règle N-039 b (test final) décide ; H-E2 descriptive"}


class Confrontation:
    def __init__(self, noyau, dossier: pathlib.Path, addendum: dict | None = None, budget_defense: dict | None = None,
                 plafond_confrontation: float | None = None):
        """`addendum` : relevé gelé (`relever_metriques`) ; quand il est donné, une métrique dont les empreintes ne sont
        pas celles du relevé est « non gelée » et n'est ni exécutée ni attaquée (CR-04).
        `budget_defense` (CR3-01) : {"appels_max", "usd_max", "temps_max_s"} d'une défense — son pire cas ; à défaut, le
        budget d'une génération du noyau. `plafond_confrontation` (CR3-01) : dollars ajoutés au plafond de la course
        rechargée pour la seule confrontation (la course adaptative peut avoir atteint son plafond au pire cas) ; à
        défaut, la confrontation s'impute au plafond restant de la course."""
        self.noyau = noyau
        self.dossier = pathlib.Path(dossier)
        self.dossier.mkdir(parents=True, exist_ok=True)
        self.addendum = addendum
        b = dict(noyau.budget)
        for k, v in (budget_defense or {}).items():
            if v is not None:
                b[k] = v
        if int(b["appels_max"]) <= 0 or float(b["usd_max"]) <= 0 or int(b["temps_max_s"]) <= 0:
            raise ValueError("budget de défense : appels_max, usd_max et temps_max_s doivent être strictement positifs")
        self.budget_defense = {"appels_max": int(b["appels_max"]), "usd_max": float(b["usd_max"]), "temps_max_s": int(b["temps_max_s"])}
        self.plafond_confrontation = (float(plafond_confrontation) if plafond_confrontation is not None else None)
        if self.plafond_confrontation is not None:
            if self.plafond_confrontation < 0:
                raise ValueError("plafond_confrontation négatif")
            self.noyau.plafond_total += self.plafond_confrontation
        self.journaux_defense: list[dict] = []

    def _derniere_generation(self, lignee: str) -> dict | None:
        lignes = [l for l in self.noyau.archive.lignes(lignee) if l.get("statut") == "OK" and not l.get("phase")]
        return lignes[-1] if lignes else None

    def _famille(self, lignee: str) -> str:
        etat = self.noyau.lignees[lignee]
        return etat.get("famille") or contrat.FAMILLES[etat["espece_amorcage"]]

    def _executer_sur_attaques(self, lignee_def: str, organisme: pathlib.Path, attaques: list[dict], etiquette: str) -> dict:
        travail = self.noyau.espace / "travail" / "confrontation" / etiquette / "defense"
        if travail.exists():
            shutil.rmtree(travail)
        travail.mkdir(parents=True)
        for p in (travail.parent, travail.parent.parent):
            bac_a_sable.proteger(p, 0o711)
        g_def = (self._derniere_generation(lignee_def) or {}).get("generation", 0) + 1
        rng = np.random.default_rng(self.noyau.graine(lignee_def, g_def, "defense"))
        # CR-06 : les attaques sont mêlées aux tâches du test de développement, sans marque ; seules les attaques sont notées
        melange = [{"id": a["id"], "famille": a["famille"], "texte": a["texte"], "etiquettes": list(a["etiquettes"])} for a in attaques] + \
                  [_taches.masquer(t) for t in self.noyau.banque["test"]]
        ordre = rng.permutation(len(melange))
        traits_att = None
        if set(self.noyau.vues) == {"simulation"} and not self.noyau.reel:  # en réel, les attaques n'ont pas d'activations
            from . import entrainement as _ent
            traits_att = {"simulation": _ent.traits_simules({t_["id"]: t_["texte"] for t_ in attaques})}
        contexte = {
            "generation": g_def, "lignee": lignee_def, "mission": contrat.mission_texte(self.noyau.mission, _taches.ETIQUETTES),
            "dossier_travail": str(travail), "dossier_archive": str(self.noyau._vue_pour(lignee_def)),
            "taches_entrainement": [dict(_taches.masquer(t), verite=t["verite"]) for t in self.noyau.banque["train"]],
            "taches_test": [melange[i] for i in ordre],
            "budget": {"appels_max": int(self.budget_defense["appels_max"]), "usd_max": round(min(float(self.budget_defense["usd_max"]), self.noyau._plafond_restant()), 4),
                       "temps_max_s": int(self.budget_defense["temps_max_s"]), "recherches_max": 0,
                       "entrainements_max": int(self.noyau.budget["entrainements_max"]), "pas_max": int(self.noyau.budget["pas_max"])},
            "traits": self.noyau._contexte_traits(bool(self.noyau.vues) and int(self.noyau.budget["entrainements_max"]) > 0 and traits_att is not None),
            "historique": self.noyau.archive.historique(lignee_def), "relance": False, "graine": self.noyau.graine(lignee_def, g_def, "organisme"),
        }
        appelant = Appelant(travail / "noyau", min(float(self.budget_defense["usd_max"]), self.noyau._plafond_restant()),
                            self.noyau.appelants, self.noyau.reel, self.noyau.go_id)
        socket = str(travail / "n.sock")
        if len(socket) > 100:
            import hashlib as _h
            socket = f"/tmp/essaim-conf-{_h.sha256(str(self.dossier).encode()).hexdigest()[:10]}-{etiquette[:14]}.sock"
        uid = self.noyau._uid(lignee_def)
        bac_a_sable.preparer(travail, organisme, contexte, uid=uid)
        entraineur = self.noyau._entraineur(travail / "noyau", lignee_def, g_def, traits_att) if traits_att is not None else None
        bac_a_sable.proteger(travail / "noyau", 0o700)
        with ServeurAppels(appelant, socket, int(self.budget_defense["appels_max"]), self.noyau.parallele_max, None, entraineur) as serveur:
            execution = bac_a_sable.executer(travail, socket, int(self.budget_defense["temps_max_s"]), isoler_reseau=self.noyau.isoler_reseau, uid=uid)
            n_appels = serveur.n_appels
            non_conformes = serveur.non_conformes
        self.noyau.depense_totale += appelant.depense_usd
        self.noyau.n_appels_total += n_appels
        # CR3-03 : le journal des appels de la défense est scellé et copié dans le dossier de la confrontation ; les appels
        # à un modèle non conforme sont comptés et remontés (H-E3 porte aussi sur les défenses)
        from .archive import sceller, empreinte_fichier
        journal = {"defense": etiquette, "chemin": None, "sha256": None, "n_appels": n_appels, "non_conformes": int(non_conformes)}
        if appelant.journal.exists():
            sceller(appelant.journal)
            copie = self.dossier / "journaux-defense" / f"{etiquette}.jsonl"
            copie.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(appelant.journal, copie)
            sceller(copie)
            journal.update({"chemin": str(copie), "sha256": empreinte_fichier(copie)})
        self.journaux_defense.append(journal)
        reponses = {}
        f = travail / "reponses_test.json"
        if f.exists():
            try:
                brut = json.loads(f.read_text(encoding="utf-8-sig"))
                if isinstance(brut, dict):
                    for t in attaques:
                        r = brut.get(t["id"])
                        if isinstance(r, dict) and str(r.get("etiquette", "")).strip().lower() in t["etiquettes"]:
                            reponses[t["id"]] = {"etiquette": str(r["etiquette"]).strip().lower(), "confiance": _taches.confiance_de(r)}
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass
        score = _taches.evaluer_generique(reponses, attaques)
        if non_conformes:  # CR3-03 : une défense servie par un modèle non conforme est invalide : aucun score retenu
            score = None
        return {"execution": execution["code"], "n_appels": n_appels, "cout_usd": round(appelant.depense_usd, 4),
                "score_attaques": score, "travail": travail, "non_conformes": int(non_conformes), "invalide_modele": bool(non_conformes)}

    def _discriminance(self, a: str, ma: dict) -> dict:
        """CR-07 (ii) et N-041 (c), épreuve mécanique d'une métrique gelée, avant toute application. Le noyau fabrique des
        sorties et exécute la métrique sur chacune : « parfait » (chaque attaque reçoit sa vérité), « inverse » (l'autre
        étiquette), « tout_positif », « tout_negatif », « aleatoire » (étiquette tirée, graine consignée), « vide » (aucune
        réponse). Discriminante : parfait ≠ inverse (sinon elle ne mesure rien de ce qu'elle prétend ; écartée de H-E2).
        Résiste au gonflement : parfait strictement au-dessus de toutes les sorties dégénérées (rapporté)."""
        if ma["calculer"] is None or not ma["attaques"]:
            return {"testee": False, "discriminante": None, "resiste_au_gonflement": None, "raison": "métrique ou attaques absentes"}
        base = self.noyau.espace / "travail" / "confrontation" / f"{a}__discriminance"
        if base.exists():
            shutil.rmtree(base)
        rng = np.random.default_rng(self.noyau.graine(a, 0, "defense"))
        def etiquette(t, mode):
            pos, autres = t["etiquettes"][0], [e for e in t["etiquettes"] if e != t["verite"]]
            neg = next((e for e in t["etiquettes"] if e != pos), pos)
            return {"parfait": t["verite"], "inverse": (autres[0] if autres else t["verite"]), "tout_positif": pos, "tout_negatif": neg,
                    "aleatoire": str(rng.choice(t["etiquettes"]))}[mode]
        valeurs = {}
        for mode in ("parfait", "inverse", "tout_positif", "tout_negatif", "aleatoire", "vide"):
            sorties = base / mode / "sorties"
            sorties.mkdir(parents=True)
            reponses = {} if mode == "vide" else {t["id"]: {"etiquette": etiquette(t, mode), "confiance": 1.0} for t in ma["attaques"]}
            (sorties / "reponses_test.json").write_text(json.dumps(reponses, ensure_ascii=False, indent=1), encoding="utf-8")
            for f in (base, base / mode, sorties, sorties / "reponses_test.json"):
                bac_a_sable.proteger(f, 0o755 if f.is_dir() else 0o644)
            valeurs[mode] = bac_a_sable.executer_metrique(base / mode / "metrique", ma["calculer"].parent, sorties,
                                                          uid=self.noyau._uid(a), isoler_reseau=self.noyau.isoler_reseau)
        calculees = valeurs["parfait"].get("calculee") and valeurs["inverse"].get("calculee")
        discriminante = bool(calculees and valeurs["parfait"]["valeur"] != valeurs["inverse"]["valeur"])
        degenerees = [v["valeur"] for m, v in valeurs.items() if m != "parfait" and v.get("calculee")]
        resiste = bool(calculees and degenerees and all(valeurs["parfait"]["valeur"] > x for x in degenerees)) if discriminante else False
        return {"testee": True, "discriminante": discriminante, "resiste_au_gonflement": resiste,
                "parfait": valeurs["parfait"], "inverse": valeurs["inverse"],
                "epreuves": {m: {"code": v.get("code"), "valeur": v.get("valeur"), "calculee": v.get("calculee")} for m, v in valeurs.items()},
                "raison": (None if discriminante else ("non calculée sur une sortie fabriquée" if not calculees else "même valeur sur sortie parfaite et inversée"))}

    def confronter(self, lignees: list[str] | None = None) -> dict:
        lignees = [l for l in (lignees or list(self.noyau.lignees)) if self._derniere_generation(l)]
        organismes, metriques = {}, {}
        gel = {}
        for l in lignees:
            g = self._derniere_generation(l)
            org = extraire_organisme(self.noyau.archive.racine / g["chemin"] / "organisme.tar.gz", self.dossier / "organismes" / l)
            organismes[l] = org
            metriques[l] = charger_metrique(org)
            if self.addendum is not None:
                attendu = (self.addendum.get("lignees", {}).get(l) or {}).get("metrique") or {}
                courant = empreintes_metrique(org)
                gelee = bool(attendu.get("present")) and attendu.get("empreinte_metrique") == courant.get("empreinte_metrique") \
                    and attendu.get("empreinte_attaques") == courant.get("empreinte_attaques")
                gel[l] = gelee
                if not gelee:
                    metriques[l] = {"present": metriques[l]["present"], "problemes": metriques[l]["problemes"] + ["métrique non gelée par l'addendum : ni exécutée ni attaquée"],
                                    "attaques": [], "calculer": None, "definition": metriques[l].get("definition")}
        discriminance = {l: self._discriminance(l, metriques[l]) for l in lignees}
        paires = []
        # ordre des paires tiré par SeedSequence et consigné (CR-13 e) : un arrêt sur plafond ne frappe pas toujours les mêmes
        ss = np.random.SeedSequence(int(self.noyau.manifeste["entropie_seed_sequence"]), spawn_key=(1_000_002, 0, 4))
        graine_paires = int(ss.generate_state(1, dtype=np.uint64)[0])
        couples = [(a, b) for a in lignees for b in lignees if a != b]
        ordre = np.random.default_rng(graine_paires).permutation(len(couples))
        for k in ordre:
            a, b = couples[k]
            if a == b:
                continue
            if self._famille(a) == self._famille(b):
                paires.append({"attaquant": a, "defendeur": b, "applicable": False, "raison": "même famille de fournisseur"})
                continue
            ma = metriques[a]
            res = {"attaquant": a, "defendeur": b, "applicable": True, "famille_attaquant": self._famille(a),
                   "famille_defendeur": self._famille(b), "problemes_metrique": ma["problemes"],
                   "metrique_discriminante": discriminance[a].get("discriminante")}
            if ma["attaques"]:
                att = self._executer_sur_attaques(b, organismes[b], ma["attaques"], f"{a}__vers__{b}")
                res.update({"n_attaques": len(ma["attaques"]), "execution_defense": att["execution"],
                            "n_appels": att["n_appels"], "cout_usd": att["cout_usd"], "score_attaques": att["score_attaques"],
                            "non_conformes": att["non_conformes"], "invalide_modele": att["invalide_modele"]})
                sorties = att["travail"]
            else:
                res.update({"n_attaques": 0, "score_attaques": None})
                sorties = None
            if ma["calculer"] is not None and sorties is not None:
                res["metrique"] = bac_a_sable.executer_metrique(self.noyau.espace / "travail" / "confrontation" / f"{a}__vers__{b}" / "metrique", ma["calculer"].parent, sorties,
                                                                uid=self.noyau._uid(a), isoler_reseau=self.noyau.isoler_reseau)
            else:
                res["metrique"] = {"code": "NON_APPLICABLE", "valeur": None, "calculee": False}
            paires.append(res)
        rapport = {"avertissement": "NON OPPOSABLE (R7) ; aucune règle de choix du champion n'est appliquée ici",
                   "addendum_gele": (None if self.addendum is None else {"quand_utc": self.addendum.get("quand_utc"), "gelees": gel}),
                   "lignees": {l: {"famille": self._famille(l), "metrique_presente": metriques[l]["present"],
                                   "problemes_metrique": metriques[l]["problemes"], "n_attaques": len(metriques[l]["attaques"]),
                                   "discriminance": {k: v for k, v in discriminance[l].items() if k in ("testee", "discriminante", "resiste_au_gonflement", "raison", "epreuves")},
                                   "definition": (metriques[l]["definition"] or "")[:2000]} for l in lignees},
                   "paires": paires, "scores_temoin": self.noyau._scores_finaux(self.noyau.archive.lignes()),
                   "ordre_paires": {"graine": graine_paires, "couples": [list(couples[k]) for k in ordre]},
                   "budget_defense": dict(self.budget_defense), "plafond_confrontation_usd": self.plafond_confrontation,
                   "plafond_total_usd": round(float(self.noyau.plafond_total), 4),
                   "journaux_defense": list(self.journaux_defense), "defenses_non_conformes": sum(1 for j in self.journaux_defense if j["non_conformes"]),
                   "depense_totale_usd": round(self.noyau.depense_totale, 4)}
        rapport.update(designations_et_concours(paires, rapport["scores_temoin"], rapport["lignees"]))
        n = 1
        while (self.dossier / f"confrontation-v{n}.json").exists():
            n += 1
        (self.dossier / f"confrontation-v{n}.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
        from .archive import sceller
        sceller(self.dossier / f"confrontation-v{n}.json")
        return rapport
