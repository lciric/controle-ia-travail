"""Aides des essais de la v68 (et de l'essai à blanc `demonstrations/essai_a_blanc_v68.py`) : configuration d'essai v56 dont les
fiches portent un champ `test_de_mort` à bloc `statistique` (valeurs **d'essai** seulement, aucune recommandée ni gelée), une
tranche d'essai et sa liste blanche, l'étage de tests de mort en moteur simulé (exécuteur factice demandé explicitement : aucune
barrière, aucun réseau, aucune clé), adaptateurs simulés v68. Tout est écrit dans le dossier donné ; rien n'est lu hors de
l'arbre ou de ce dossier."""

import hashlib
import json
import os

import aides_v56 as A
from pole import dossier_ferme as dfm
from pole import ideation_v2 as idn
from pole import tests_de_mort_v5 as v5
from pole.simulation_v68 import DONNEE_SIMULEE, AdaptateurSimuleV68

CHAMPS_V68 = list(A.CHAMPS) + ["prediction", "signe", "metrique", "test_de_mort"]
ITEMS = A.ITEMS
FOURNISSEURS = ("kimi", "argon", "claude")
CORRESPONDANCE = {"nom": "titre", "enonce": "hypothese", "prediction": "prediction", "signe": "signe", "metrique": "metrique",
                  "test_de_mort": "test_de_mort"}
JETABLE = {"PATH": "/usr/bin:/bin", "POLE_MACHINE_JETABLE_V56": "1"}
EPISODES = "episode,valeur\n1,0.2\n2,0.4\n3,0.5\n"
ETAGE_ESSAI = {"nombre": 3, "budget_test_usd": 0.5, "budget_lecteur_usd": 0.2, "executions_par_fiche": 3, "delai_execution_s": 120.0,
               "memoire_mo": 1024, "plafond_etage_usd": 5.0, "fournisseur": "claude",
               "experimentateur": ["experimentateur-test", "claude-opus-5-5"], "lecteur": ["lecteur-test", "claude-fable-5-1"]}


def creer_tranche(dossier):
    """Tranche d'essai (un fichier `DONNEE_SIMULEE`), son index et sa liste blanche ; rend (chemin de la tranche, liste blanche)."""
    tr = os.path.join(dossier, "tranche-essai-v68")
    if not os.path.isdir(tr):
        os.makedirs(tr)
        with open(os.path.join(tr, DONNEE_SIMULEE), "w", encoding="utf-8") as f:
            f.write(EPISODES)
        dfm.ecrire_index(tr, [{"chemin": DONNEE_SIMULEE, "titre": "Épisodes d'essai", "resume": "épisodes d'essai (v68)"}])
    lb = os.path.join(dossier, "liste-blanche-essai-v68.json")
    if not os.path.exists(lb):
        idn.construire_liste_blanche([os.path.join(tr, "index.json")], lb)
    return tr, lb


def configuration(dossier, *, avec_test=True, etage=True, **modifs):
    """Configuration v56 d'essai (dict) : champs de fiche avec `test_de_mort` (si `avec_test`), section `etage_tests_de_mort`
    (si `etage`), portée « par_generation », coût simulé 0,01 USD par appel."""
    conf = A.configuration(dossier)
    if avec_test:
        conf["champs_fiche"] = list(CHAMPS_V68)
    conf["simulation"] = {"cout_par_appel_usd": 0.01}
    conf["budget"]["portee_plafond"] = "par_generation"
    conf["graines"] = {"prefixe": "v68c"}  # préfixe d'essai : la sélection de la génération 1 retient deux fiches et en exclut une
    if etage:
        tr, lb = creer_tranche(dossier)
        conf["etage_tests_de_mort"] = dict(json.loads(json.dumps(ETAGE_ESSAI)), tranche=tr, liste_blanche=lb,
                                           correspondance=dict(CORRESPONDANCE))
    return A._modifier(conf, modifs)


def ecrire_configuration(conf, chemin):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(conf, f, ensure_ascii=False, indent=1)
    return chemin


def adaptateurs(conf, cout=0.01, classe=AdaptateurSimuleV68, **kw):
    if issubclass(classe, AdaptateurEnregistreurV68):
        kw.setdefault("journal", [])  # un seul journal pour tous les fournisseurs : l'ordre des appels est gardé
    return {n: classe(champs_fiche=conf["champs_fiche"], items=ITEMS, cout_par_appel_usd=cout, champ_titre="titre", **kw)
            for n in FOURNISSEURS}


def etage(conf, adaptateurs_, **en_plus):
    """L'étage tel que `ideation_v5.reglages_etage` le construit en moteur simulé (exécuteur factice), depuis la configuration."""
    e = conf["etage_tests_de_mort"]
    tranche = v5.charger_tranche(e["tranche"], idn.charger_liste_blanche(e["liste_blanche"]))
    reglages = {"tranche": tranche, "nombre": e["nombre"], "experimentateur": tuple(e["experimentateur"]),
                "lecteur": tuple(e["lecteur"]), "budget_test_usd": e["budget_test_usd"], "budget_lecteur_usd": e["budget_lecteur_usd"],
                "executions_par_fiche": e["executions_par_fiche"], "delai_execution_s": e["delai_execution_s"],
                "memoire_mo": e["memoire_mo"], "executeur": v5.ExecuteurFactice(delai_s=e["delai_execution_s"], memoire_mo=e["memoire_mo"]),
                "moteur": "simule", "plafond_total_usd": e["plafond_etage_usd"]}
    d = {"adaptateur": adaptateurs_[e["fournisseur"]], "reglages": reglages, "nombre": e["nombre"],
         "tranche_index_sha256": tranche.index_sha256, "correspondance": e["correspondance"], "plafond_etage_usd": e["plafond_etage_usd"]}
    d.update(en_plus)
    return d


class AdaptateurEnregistreurV68(AdaptateurSimuleV68):
    """Comme `AdaptateurSimuleV68`, et garde en mémoire (jamais sur disque) les consignes de la passe 1 des proposeurs, dans
    l'ordre : ce que chaque génération a servi aux proposeurs se lit sans ouvrir les sessions."""

    def __init__(self, journal=None, **kw):
        super().__init__(**kw)
        self.consignes_passe1 = [] if journal is None else journal

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        if "## Case" in consigne and "## Tableau minimal" not in consigne and "## Les deux fiches" not in consigne:
            self.consignes_passe1.append(consigne)
        return super().lancer(role, consigne, dossier, budget_usd, max_tours, modele=modele)


def consignes_passe1(adaptateurs_):
    """Les consignes de la passe 1, dans l'ordre des appels (journal commun à tous les fournisseurs)."""
    return list(adaptateurs_[FOURNISSEURS[0]].consignes_passe1)


def section_attendue(dossier_etage, titre):
    """La section qu'une génération qui lit la sélection de `dossier_etage` doit recevoir, recalculée **à part** depuis les
    fichiers scellés de l'étage (sélection, fiches) : « ## titre », puis « - nom : énoncé » des seules retenues ; rend
    (texte, sha256, lignes, noms des exclues)."""
    from pole.etage_entre_generations_v57 import NOM_SELECTION
    with open(os.path.join(dossier_etage, NOM_SELECTION), encoding="utf-8") as f:
        sel = json.load(f)
    with open(os.path.join(dossier_etage, "fiches-validees.json"), encoding="utf-8") as f:
        fiches = {x["identifiant_auteur"]: x for x in json.load(f)}
    lignes = [f"- {' '.join(fiches[i]['nom'].split())} : {' '.join(fiches[i]['enonce'].split())}" for i in sel["retenues"]]
    exclues = [fiches[x["identifiant_auteur"]]["nom"] for x in sel["exclues"] if x["identifiant_auteur"] in fiches]
    texte = "## " + titre + "\n" + "\n".join(lignes) + "\n" if lignes else None
    return texte, (hashlib.sha256(texte.encode("utf-8")).hexdigest() if texte else None), lignes, exclues


__all__ = ("configuration", "ecrire_configuration", "adaptateurs", "etage", "creer_tranche", "AdaptateurEnregistreurV68",
           "consignes_passe1", "section_attendue", "CHAMPS_V68", "CORRESPONDANCE", "JETABLE", "ETAGE_ESSAI")
