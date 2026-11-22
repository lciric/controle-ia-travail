"""Aides des essais du lot 6 v5 du véhicule NA-1 : la course d'essai du v3 (configuration d'essai, pièces factices,
colonne en état 1 par le contrôle de départ d'essai du lot 10 a), plus le champ `replis` de la configuration et, pour les
clés Claude, l'adaptateur direct réel du lot 4 v3 sur le faux client de `simulation_na_v5`. Données factices seules ;
modèles d'essai aux noms neutres ; aucune clé, aucun appel, aucun réseau."""

import json
import os
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot6_v3 as A3  # noqa: E402
import configuration_essai_na_lot6_v1 as CE  # noqa: E402
from pole import configuration_course_na_v1 as cfn  # noqa: E402
from pole import course_na_v5 as c5  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402
from pole import simulation_na_v5 as s5  # noqa: E402

REPLI_1, REPLI_2 = "modele-repli-1-essai", "modele-repli-2-essai"
MODELES_CLAUDE = (CE.MODELE_ESSAI, REPLI_1, REPLI_2)
ROLES_CLAUDE = tuple(r for r, (s, e, c, a) in CE.ROLES_ESSAI.items() if c in ("cle_a", "cle_b"))


def ajouter_replis(objet, pires=None):
    objet["replis"] = {"modeles_repli": [REPLI_1, REPLI_2],
                       "pires_repli_usd": pires if pires is not None else
                       {r: {REPLI_1: objet["pires_par_role_usd"][r], REPLI_2: objet["pires_par_role_usd"][r]}
                        for r in ROLES_CLAUDE}}


def selon(table):
    """Un scénario d'essai : `table[(sorte, modele)]` est une suite de choix (« servie », « refus », « erreur »),
    consommée appel après appel ; au-delà, « servie »."""
    restes = {k: list(v) for k, v in table.items()}

    def scenario(sorte, modele, rang):
        file = restes.get((sorte, modele))
        return file.pop(0) if file else s5.SERVIE
    return scenario


class MontageV5:
    def __init__(self, *, modifier=None, scenario=None, decider=None, sans_replis=False):
        self.dossier = tempfile.mkdtemp(prefix="essais-na-lot6-v5-")

        def modif(objet):
            if not sans_replis:
                ajouter_replis(objet)
            if modifier is not None:
                modifier(objet)

        self.chemin, self.sha = CE.ecrire_configuration_essai(os.path.join(self.dossier, "configuration"), modifier=modif)
        self.config = cfn.lire_configuration_course(self.chemin, self.sha)
        p = self.config.piece("table_roles_cles")
        with open(p.chemin, "rb") as f:
            octets = f.read()
        self.table = rt.lire_table(octets, p.sha256, json.loads(octets)["marque"])
        self.clients = {}
        self.fabrique = s5.fabrique_adaptateurs_na_v5(self.table, declaration=cfn.declaration_portier(self.config),
                                                      items=CE.ITEMS_ESSAI, modeles_claude=MODELES_CLAUDE,
                                                      scenario=scenario, decider=decider, clients=self.clients)
        self.sortie = os.path.join(self.dossier, "sortie")
        self.sessions = os.path.join(self.dossier, "sessions")

    def lancer(self, **kw):
        kw.setdefault("regime", A3.REGIME)
        kw.setdefault("nombre_generations", 3)
        kw.setdefault("ligne_accord_usd", 450.0)
        kw.setdefault("additif_sha256", CE.additif_essai_sha256())
        kw.setdefault("racine_sessions", self.sessions)
        kw.setdefault("etat_colonne", A3.ETAT_COLONNE_PAR_DEFAUT)
        kw.setdefault("fabrique_journal", A3.fabrique_colonne(A3.ETAT_COLONNE_PAR_DEFAUT))
        kw.setdefault("controle_code_charge", None)
        return c5.executer_course_na_v5(self.config, self.sortie, self.fabrique, **kw)

    def chemin_sortie(self, *m):
        return os.path.join(self.sortie, *m)

    def journal_arrets(self):
        return c5.lire_journal_arrets_generations(self.chemin_sortie(c5.NOM_JOURNAL_ARRETS), exiger_sceau=True)

    def arrets(self):
        return [l["arret"] for l in self.journal_arrets() if l["evenement"] == "arrêt"]

    def depart(self):
        return next(l["depart"] for l in self.journal_arrets() if l["evenement"] == "départ")

    def lignes_registre(self, g):
        from pole import portier_na_v1 as pt  # noqa: PLC0415
        return pt.relire_ajout_seul(self.chemin_sortie(f"generation-{g}", f"registre-tentatives-g{g}-na-v4.jsonl"),
                                    exiger_sceau=True)


__all__ = ("MontageV5", "selon", "ajouter_replis", "REPLI_1", "REPLI_2", "MODELES_CLAUDE", "ROLES_CLAUDE", "CE", "A3")
