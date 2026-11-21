"""Aides des essais du lot 6 v2 du véhicule NA-1 : une course d'essai montée dans un dossier temporaire neuf (configuration
d'essai, pièces factices, moteur simulé au contrat de la course, état du relais factice). Données factices seules ; aucune
clé, aucun appel, aucun réseau hors de la boucle locale.

v2 : la course reçoit l'état de la colonne et une fabrique de journal. Par défaut, le montage est câblé comme en course :
état 1 (« garde seule »), journal de la colonne muni du contrôle de départ d'essai du lot 10 a (registre d'essai aux lignes
inertes, `aides_na_lot10a_v1.depart`). `etat_colonne` et `fabrique_journal` se remplacent pour les essais du câblage."""

import json
import os
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot10a_v1 as L10  # noqa: E402
import configuration_essai_na_lot6_v1 as CE  # noqa: E402
from pole import configuration_course_na_v1 as cfn  # noqa: E402
from pole import course_na_v2 as cn  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402
from pole import simulation_na_v1 as sim  # noqa: E402

REGIME = cfn.REGIME
ETAT_COLONNE_PAR_DEFAUT = 1


def depart_colonne(etat=ETAT_COLONNE_PAR_DEFAUT):
    """Le contrôle de départ d'essai du lot 10 a, à l'état demandé (registre d'essai aux lignes inertes)."""
    return L10.depart(etat)


def fabrique_colonne(etat=ETAT_COLONNE_PAR_DEFAUT):
    return cn.fabrique_journal_colonne(depart_colonne(etat))


def fabrique_ordinaire(dossier, nom):
    """Un journal du lot 3 ordinaire : l'artefact du refus de câblage en état 1 ou 2."""
    return jn.JournalRequetes(dossier, nom)


def fabrique_par_generation(par_g):
    """Une fabrique qui rend, pour la génération g (lue au nom du journal), `par_g[g](dossier, nom)`."""
    def fabrique(dossier, nom):
        g = int(nom[len("journal-requetes-g"):-len(".jsonl")])
        return par_g[g](dossier, nom)
    return fabrique


def etat_relais_sain():
    return {"plafond_usd": 156.56, "depense_usd": 3.0, "engage_usd": 0.0, "reserve_par_appel_usd": 0.4, "refus": 0,
            "refus_modele": 0, "appels": 5, "restant_usd": 153.56}


def etat_relais_credit():
    return {"plafond_usd": 156.56, "depense_usd": 156.40, "engage_usd": 0.0, "reserve_par_appel_usd": 0.4, "refus": 1,
            "refus_modele": 0, "appels": 300, "restant_usd": 0.16}


class Montage:
    """Une course d'essai et tout ce qu'elle lit, dans un dossier temporaire neuf."""

    def __init__(self, *, modifier=None, table=None, tirage=None, decider=None, cout=0.01, reglages=None, marqueur=None,
                 modele_servi=None, etat_relais=None, par_adaptateur=None, garder_consignes=False):
        self.dossier = tempfile.mkdtemp(prefix="essais-na-lot6-v2-")
        self.etat_colonne = ETAT_COLONNE_PAR_DEFAUT
        self.fabrique_journal = fabrique_colonne(ETAT_COLONNE_PAR_DEFAUT)
        self.dossier_conf = os.path.join(self.dossier, "configuration")
        self.chemin, self.sha = CE.ecrire_configuration_essai(self.dossier_conf, modifier=modifier, table=table, tirage=tirage)
        self.config = cfn.lire_configuration_course(self.chemin, self.sha)
        p = self.config.piece("table_roles_cles")
        with open(p.chemin, "rb") as f:  # lue sans les gardes de départ : les adaptateurs d'essai seulement
            octets = f.read()
        t = rt.lire_table(octets, p.sha256, json.loads(octets)["marque"])
        self.sortie = os.path.join(self.dossier, "sortie")
        self.sessions = os.path.join(self.dossier, "sessions")
        decl = cfn.declaration_portier(self.config)
        self.adaptateurs = sim.adaptateurs_simules_na(t, declaration=decl, items=CE.ITEMS_ESSAI, cout_par_appel_usd=cout,
                                                      decider=decider, marqueur=marqueur, modele_servi=modele_servi,
                                                      garder_consignes=garder_consignes)
        for nom, file in (reglages or {}).items():
            self.adaptateurs[nom].reglages = list(file)
        for nom, attributs in (par_adaptateur or {}).items():
            for k, v in attributs.items():
                setattr(self.adaptateurs[nom], k, v)
        self.lectures_relais = []
        etat = etat_relais if etat_relais is not None else etat_relais_sain()

        def lire_etat(cle):
            self.lectures_relais.append(cle)
            if isinstance(etat, Exception):
                raise etat
            return dict(etat)

        self.lire_etat = lire_etat

    def lancer(self, **kw):
        kw.setdefault("regime", REGIME)
        kw.setdefault("nombre_generations", 3)
        kw.setdefault("ligne_accord_usd", 450.0)
        kw.setdefault("additif_sha256", CE.additif_essai_sha256())
        kw.setdefault("lire_etat_relais", self.lire_etat)
        kw.setdefault("racine_sessions", self.sessions)
        kw.setdefault("etat_colonne", self.etat_colonne)
        kw.setdefault("fabrique_journal", self.fabrique_journal)
        return cn.executer_course_na_v2(self.config, self.sortie, self.adaptateurs, **kw)

    def chemin_sortie(self, *morceaux):
        return os.path.join(self.sortie, *morceaux)

    def journal_arrets(self, exiger_sceau=True):
        return cn.lire_journal_arrets_generations(self.chemin_sortie(cn.NOM_JOURNAL_ARRETS), exiger_sceau=exiger_sceau)

    def bilan(self):
        with open(self.chemin_sortie(cn.NOM_BILAN), encoding="utf-8") as f:
            return json.load(f)

    def arrets(self):
        return [l["arret"] for l in self.journal_arrets() if l["evenement"] == "arrêt"]

    def lignes_generation(self):
        return [l["ligne"] for l in self.journal_arrets() if l["evenement"] == "génération"]

    def recus(self, sorte=None):
        return [r for a in self.adaptateurs.values() for r in a.recus if sorte is None or r["sorte"] == sorte]

    def piece_fichier(self, nom):
        return self.config.piece(nom).chemin


def toujours(comportement):
    """Un `decider` d'essai : le même comportement pour chaque appel de proposeur."""
    return lambda identifiant, adaptateur, n: comportement


def lire_fichiers_texte(dossier):
    """Tous les fichiers sous `dossier`, en texte (UTF-8, erreurs remplacées), pour les recherches par programme."""
    for racine, _, fichiers in os.walk(dossier):
        for f in fichiers:
            with open(os.path.join(racine, f), "rb") as g:
                yield os.path.relpath(os.path.join(racine, f), dossier), g.read().decode("utf-8", "replace")


__all__ = ("Montage", "toujours", "etat_relais_sain", "etat_relais_credit", "lire_fichiers_texte", "REGIME", "CE",
           "L10", "depart_colonne", "fabrique_colonne", "fabrique_ordinaire", "fabrique_par_generation",
           "ETAT_COLONNE_PAR_DEFAUT")
