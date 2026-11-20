"""B2 et garde 17 — l'étage des tests de mort de l'organisme lui-même, contre l'exécuteur simulé.

Sur un sous-ensemble de la couche mécanique, chaque tentative est aussi passée à l'étage des tests de mort de l'organisme
(`tests_de_mort_v5`, verdict calculé par le noyau), par le chemin du tour fermé (`tour_ferme_v64.jouer_etage`), exécuteur
factice et doublures scriptées de l'expérimentateur et du lecteur témoin, comme au palier 0a. Le verdict doit être le même,
tentative par tentative, que celui de l'exécuteur simulé ; un désaccord arrête (garde de C6).

Le code de l'organisme n'est jamais modifié : il est lu depuis une copie passée en argument (dossier `orchestrator/`), dont les
empreintes sont contrôlées contre le manifeste du palier 0a. Sa tranche est la tranche d'épreuve du domaine visé, écrite comme
`tour_ferme_v64.creer_tranche` l'écrit (épisodes, évaluateur de référence copié octet pour octet, index, liste blanche), avec les
fonctions de l'organisme ; un lot ne porte qu'un domaine, l'étage n'ayant qu'une tranche par appel. scipy, absent des machines de
travail, est remplacé, s'il manque, par un bouchon qui lève s'il est appelé (rapport du palier 0a, § 6, point 1).
"""

import hashlib
import os
import sys
import types

from .constantes import FICHIER_EVALUATEUR, NE_TIENT_PAS, NON_EXECUTABLE, TIENT

CORRESPONDANCE_VERDICTS = {"survit": TIENT, "éliminée": NE_TIENT_PAS, "non concluant": NON_EXECUTABLE}

EMPREINTES_PALIER_0A = {
    "pole/a_blanc_v59.py": "606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c",
    "pole/boucle_fermee_v59.py": "a2de486592fc98c14e13bb9071d272fb65d4f49de38dd188ee64857698177681",
    "pole/etage_entre_generations_v53.py": "d568d25bf7d96011cfdcda12e7bc2c1933a61827b237f8c8c363b4055122ad4b",
    "pole/etage_entre_generations_v56.py": "f0c80e2d9801d4a928574f7f442e2950c2d130d77015b30102911bfa87dd6eba",
    "pole/etage_entre_generations_v57.py": "e4bf36819d18844079a2bb4996991fd65c233a51d76b7d3daf5b866a71328318",
    "pole/evaluateur_lois_v62.py": "26613fe72da7f049d5dd076aab51a3808221bf52686b9d0258a201c8b38b8632",
    "pole/fiches_v53.py": "7cfcf8329c66c7a37ceb2992cc96e21aedbfa0a10525467672794090a128eda6",
    "pole/oracle_tour_ferme_v60.py": "514864b7879e5131ee37f7a57951db5ece514abe9acbd90b1294e0d914041669",
    "pole/proposeurs_references_v59.py": "7d00371a8fcfa3efc2c17b2f0ab33d18ef83b41f3988744ea12dcf823806f68f",
    "pole/selection_pari.py": "359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc",
    "pole/tests_de_mort_v2.py": "363a3725885da08412f25b28defba7a8d204d883c3637f1de1df83686d93a41a",
    "pole/tests_de_mort_v3.py": "ea05eb55f9d179501fb091d25298deaf36cd66ad16fd65bdca4dcf5e4ba74bba",
    "pole/tests_de_mort_v4.py": "35912a3ab5e9e289077ffdceb492bb966f24176244976b3923dcfe95bda1603a",
    "pole/tests_de_mort_v5.py": "da524871b9b498693d67cc099240acb98c4c84c800ee4c69f0a1cb5fe60b64f1",
    "pole/tour_ferme_v64.py": "35a8294e24c870685435b990d6c03cd33cb5b2e288bcb2cc91cd9af04679c2da",
    "exemples/temoins-pari-demo-v1.json": "fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877",
}


class OrganismeIndisponible(RuntimeError):
    """Le code de l'organisme n'est pas disponible au commit que cite le rapport du palier 0a : la garde 17 n'est pas jouée,
    C6 est « non établi » pour elle et l'issue ne peut pas être « lisible » (B2 ; critères de lecture : suspendue)."""


class DesaccordOrganisme(RuntimeError):
    pass


def _sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def verifier_copie(orchestrateur):
    """Les empreintes des seize fichiers employés au palier 0a ; tout écart ou absence → `OrganismeIndisponible`."""
    ecarts = []
    for rel, sha in EMPREINTES_PALIER_0A.items():
        chemin = os.path.join(orchestrateur, rel)
        if not os.path.isfile(chemin) or _sha256(chemin) != sha:
            ecarts.append(rel)
    if ecarts:
        raise OrganismeIndisponible(f"copie de l'organisme absente ou différente du palier 0a : {ecarts}")
    return True


def _bouchon_scipy():
    try:
        import scipy.optimize  # noqa: F401
        return False
    except ModuleNotFoundError:
        pass

    def minimize(*a, **k):
        raise RuntimeError("bouchon : scipy.optimize.minimize appelé (ne doit jamais l'être à cet étage)")

    scipy = types.ModuleType("scipy")
    optimize = types.ModuleType("scipy.optimize")
    optimize.minimize = minimize
    scipy.optimize = optimize
    sys.modules["scipy"], sys.modules["scipy.optimize"] = scipy, optimize
    return True


class EtageOrganisme:
    """L'étage de l'organisme, chargé depuis une copie vérifiée. `racine` : entier de la tâche (graine dérivée par l'appelant)."""

    def __init__(self, orchestrateur, racine, tache):
        if not orchestrateur or not os.path.isdir(orchestrateur):
            raise OrganismeIndisponible(f"copie de l'organisme absente : {orchestrateur!r}")
        verifier_copie(orchestrateur)
        self.scipy_bouche = _bouchon_scipy()
        if orchestrateur not in sys.path:
            sys.path.insert(0, orchestrateur)
        from pole import dossier_ferme as dfm
        from pole import ideation_v2 as idn
        from pole import tests_de_mort_v5 as v5
        from pole import tour_ferme_v64 as T
        self.T, self.v5, self.dfm, self.idn = T, v5, dfm, idn
        self.orchestrateur, self.racine, self.tache = orchestrateur, int(racine), tache
        self.appels = 0

    def _tranche(self, dossier_lot, lignes_csv):
        tr = os.path.join(dossier_lot, "exploratoire-etage", "tranche")
        os.makedirs(tr)
        with open(os.path.join(tr, "episodes.csv"), "x", encoding="utf-8") as f:
            f.write(lignes_csv)
        with open(self.T.CHEMIN_EVALUATEUR, "rb") as f:
            octets = f.read()
        with open(os.path.join(tr, FICHIER_EVALUATEUR), "xb") as f:
            f.write(octets)
        self.dfm.ecrire_index(tr, [{"chemin": "episodes.csv", "titre": "Épisodes du monde",
                                    "resume": "traits z0, z1, sous-population g, issue y"},
                                   {"chemin": FICHIER_EVALUATEUR, "titre": "Évaluateur de référence des lois",
                                    "resume": "proba(loi, instance), gains(loi, chemin), ecrire_gains(loi, chemin, sortie) : "
                                              "bibliothèque standard"}])
        lb = os.path.join(dossier_lot, "exploratoire-etage", "liste-blanche.json")
        self.idn.construire_liste_blanche([os.path.join(tr, "index.json")], lb)
        return self.v5.charger_tranche(tr, self.idn.charger_liste_blanche(lb))

    def eprouver_lot(self, dossier_lot, cartes, lois, lignes_csv, scenario=None):
        """Un lot de douze cartes au plus, toutes sur la même tranche. `cartes` : cartes projetées (gabarit de la carte servie) ;
        `lois` : {identifiant de la carte : loi}. Rend {identifiant : (classe, valeur du noyau)}."""
        T = self.T
        if len(cartes) > 12:
            raise DesaccordOrganisme("lot de plus de douze cartes")
        os.makedirs(dossier_lot)
        servies, reel_de = [], {}
        for c in cartes:
            servi = T.identifiant_opaque(self.racine, self.tache, c["identifiant"])
            reel_de[servi] = c["identifiant"]
            servies.append(dict(c, identifiant=servi))
        lois_servies = {T.identifiant_opaque(self.racine, self.tache, k): v for k, v in lois.items()}
        tranche = self._tranche(dossier_lot, lignes_csv)
        roles = {"experimentateur": ("experimentateur-scripte", "famille-a"), "verificateur": ("verificateur-scripte", "famille-b"),
                 "relais": {"experimentateur": "kimi", "verificateur": "argon"}}
        ad = T.AdaptateurEtageV64(T.AdaptateurExperimentateurScripte(scenario), T.AdaptateurVerificateurScripte())
        resume, _, _, _, _ = T.jouer_etage(os.path.join(dossier_lot, "etage"), servies, lois_servies, None, self.racine, self.tache,
                                           self.v5.ExecuteurFactice(delai_s=60.0), ad, roles, T.Compteur(1e9, 3600.0), [],
                                           tranche=tranche, moteur="simule", environnement=T.ENV_A_BLANC)
        self.appels += 1
        out = {}
        for r in resume["par_fiche"]:
            ident = reel_de[r["identifiant_auteur"]]
            if r.get("statut") != "testée":
                out[ident] = (NON_EXECUTABLE, None)
                continue
            vn = r["verdict_noyau"]
            out[ident] = (CORRESPONDANCE_VERDICTS[vn["verdict"]], vn.get("valeur_noyau"))
        manquants = sorted(set(c["identifiant"] for c in cartes) - set(out))
        if manquants:
            raise DesaccordOrganisme(f"l'étage de l'organisme ne rend pas de verdict pour {manquants}")
        return out


def comparer_verdicts(simules, organisme):
    """Garde 17 : mêmes classes, tentative par tentative ; rend la liste des désaccords (vide si l'accord est complet)."""
    return sorted((k, simules[k], organisme.get(k, (None,))[0]) for k in simules if simules[k] != organisme.get(k, (None,))[0])
