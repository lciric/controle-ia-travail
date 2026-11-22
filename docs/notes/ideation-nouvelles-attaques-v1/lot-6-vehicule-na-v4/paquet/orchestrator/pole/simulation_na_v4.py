"""Véhicule NA-1, lot 6 v4 — registre factice conforme à l'interface, faux fournisseur de chaînes de repli, course simulée
de trois générations (`simulation_na_v4`). Aucun appel de modèle, aucun réseau, aucune dépense.

- `RegistreFactice` : en ajout seul, JSON par ligne, champs fermés (ceux du lot 5 v1, les trois champs fermés reçus, et
  ceux de l'interface), rang et chaînage par empreinte de la ligne précédente, sceau à la clôture. **Ce n'est pas le
  registre du lot 5 v2**, qui s'écrit en parallèle : il en tient l'interface, rien de plus.
- `FauxFournisseurReplis` : rend, pour un appel, le dictionnaire `{"tentatives_na": [...]}` de la forme que lit
  `course_na_v4.tentatives_de_l_appel`, d'après un scénario (« servie », « refus-servie-1 », « refus-refus-servie-2 »,
  « trois-refus », « refus-erreur », « erreur ») ; coûts factices.
- `course_simulee` : trois générations, onze cases, cinq espèces proposeuses ; scénarios et classes tirés par
  `numpy.random.SeedSequence` dérivée par (génération, case, espèce) (R9) ; garde du coffre après chaque génération.
"""

import hashlib
import json
import os

import numpy as np

from pole import course_na_v4 as c4

VERSION = "simulation-na-v4"
SCENARIOS = ("servie", "refus-servie-1", "refus-refus-servie-2", "trois-refus", "refus-erreur", "erreur")
CHAMPS_FERMES_FACTICES = ("axe_menace", "axe_suppose", "axe_moment")  # factices : ceux du lot 5 sont lus ailleurs


class RegistreRefuseFactice(RuntimeError):
    pass


class RegistreFactice:
    """Registre des tentatives factice : `ajouter(champs)`, `lignes()`, `sceller()`."""

    def __init__(self, dossier, nom, champs_fermes=CHAMPS_FERMES_FACTICES):
        self.chemin = os.path.join(dossier, nom)
        self.permis = frozenset(c4.CHAMPS_LOT_5_V1 + tuple(champs_fermes) + c4.CHAMPS_INTERFACE)
        self._rang, self._precedent, self._scelle = 0, "0" * 64, False
        with open(self.chemin, "x", encoding="utf-8"):
            pass

    def ajouter(self, champs):
        if self._scelle:
            raise RegistreRefuseFactice("registre scellé")
        if not isinstance(champs, dict) or not set(champs) <= self.permis:
            raise RegistreRefuseFactice("champ hors de la liste fermée")
        for k in c4.CHAMPS_INTERFACE:
            if k not in champs:
                raise RegistreRefuseFactice("champ de l'interface manquant")
        self._rang += 1
        ligne = dict(champs, rang=self._rang, precedent=self._precedent)
        texte = json.dumps(ligne, ensure_ascii=False, sort_keys=True)
        self._precedent = hashlib.sha256(texte.encode("utf-8")).hexdigest()
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(texte + "\n")
        return self._rang

    def lignes(self):
        rendu, precedent = [], "0" * 64
        with open(self.chemin, encoding="utf-8") as f:
            for i, t in enumerate(f, 1):
                l = json.loads(t)
                if l.pop("rang") != i or l.pop("precedent") != precedent:
                    raise RegistreRefuseFactice("chaînage rompu")
                precedent = hashlib.sha256(t.rstrip("\n").encode("utf-8")).hexdigest()
                rendu.append(l)
        return rendu

    def sceller(self):
        with open(self.chemin, "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        with open(self.chemin + ".sha256", "x", encoding="utf-8") as f:
            f.write(f"{h}  {os.path.basename(self.chemin)}\n")
        self._scelle = True
        return h


class FauxFournisseurReplis:
    """Fabrique la chaîne rendue par un appel du lot 4 v2 (forme attendue), d'après un scénario."""

    def __init__(self, config, cout_tentative="0.25"):
        self.config, self.cout = config, cout_tentative

    def _t(self, rang, demande, issue, categorie=None):
        if issue == "erreur":
            return {"rang_repli": rang, "modele_demande": demande, "modele_servi": None, "raison_arret": None,
                    "categorie_refus": None, "cout_compte_usd": self.config.pires[(self._espece, demande)],
                    "usage_manquant": True}
        return {"rang_repli": rang, "modele_demande": demande, "modele_servi": self.config.modele_reel[demande],
                "raison_arret": c4.RAISON_REFUS if issue == "refus" else "end_turn",
                "categorie_refus": categorie if issue == "refus" else None, "cout_compte_usd": self.cout,
                "usage_manquant": False}

    def chaine(self, espece, scenario, categorie=None):
        if scenario not in SCENARIOS:
            raise ValueError("scénario inconnu")
        self._espece = espece
        s = self.config.suite(espece)
        issues = {"servie": ["servie"], "refus-servie-1": ["refus", "servie"],
                  "refus-refus-servie-2": ["refus", "refus", "servie"], "trois-refus": ["refus", "refus", "refus"],
                  "refus-erreur": ["refus", "erreur"], "erreur": ["erreur"]}[scenario]
        return {"tentatives_na": [self._t(i, s[i], x, categorie) for i, x in enumerate(issues)]}


def configuration_factice(**surcharges):
    modele_du_role = {e: f"m-{e}" for e in c4.ESPECES}
    replis = ("m-repli-premier", "m-repli-second")
    ids = list(modele_du_role.values()) + list(replis)
    kw = dict(modele_du_role=modele_du_role, modeles_de_repli=replis,
              especes_avec_repli=frozenset({"espece-3", "espece-4", "aiguilleur", "portier", "juge-1", "passe-x"}),
              modele_reel={m: f"servi-factice-{m}" for m in ids},
              pires={(e, m): "6.05" for e in c4.ESPECES for m in ((modele_du_role[e],) + replis)},
              role_de_l_espece={e: f"proposeur-{e}" for e in c4.ESPECES_PROPOSEUSES})
    kw.update(surcharges)
    return c4.ConfigurationReplisNA(**kw)


def _rng(racine, *cles):
    return np.random.default_rng(np.random.SeedSequence(racine, spawn_key=tuple(cles)))


def course_simulee(dossier, *, racine=20261122, generations=3, cases=11, config=None, part_coffre=0.1):
    """Trois générations simulées ; rend (registre, constats du coffre, comptes). La garde du coffre lève à la génération 1
    ou 2 si la part est dépassée (simulation fidèle : la génération suivante ne part pas)."""
    config = config or configuration_factice()
    ff = FauxFournisseurReplis(config)
    registre = RegistreFactice(dossier, "registre-tentatives-simule-na-v4.jsonl")
    alim = c4.AlimentationRegistreNA(registre, config, CHAMPS_FERMES_FACTICES)
    constats = []
    for g in range(1, generations + 1):
        for k in range(cases):
            case = f"case-{k:02d}"
            for j, e in enumerate(c4.ESPECES_PROPOSEUSES):
                r = _rng(racine, g, k, j)
                scen = SCENARIOS[int(r.integers(0, len(SCENARIOS)))] if e in config.especes_avec_repli else \
                    ("servie" if r.random() < 0.9 else "erreur")
                a = ff.chaine(e, scen, categorie="cyber" if r.random() < 0.5 else None)
                classe, fiches = None, ()
                if a["tentatives_na"][-1]["raison_arret"] not in (None, c4.RAISON_REFUS):
                    classe = c4.CLASSES_V9[int(r.integers(0, 4))]
                    if classe == c4.FICHES_RENDUES:
                        fiches = [{"identifiant": f"fiche-g{g}-{k:02d}-{j}-{i}",
                                   "classe": (c4.AU_COFFRE if r.random() < part_coffre else c4.PASSEE),
                                   "fermes": {c: "valeur-factice" for c in CHAMPS_FERMES_FACTICES},
                                   "idee": "idée  factice\nsur deux lignes", "filiation": "aucune"}
                                  for i in range(1 + int(r.integers(0, 2)))]
                alim.consigner_chaine(identifiant_chaine=f"g{g}-{case}-{e}", generation=g, espece=e, case=case, a=a,
                                      classe_servie=classe, fiches=fiches)
        constats.append(c4.garde_du_coffre_v4(registre.lignes(), g, derniere_generation=generations))
    return registre, constats, c4.comptes_v4(registre.lignes(), config)
