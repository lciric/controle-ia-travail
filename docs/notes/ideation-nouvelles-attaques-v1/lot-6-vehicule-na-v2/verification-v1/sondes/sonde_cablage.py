"""Sonde du vérificateur : le refus de câblage du lot 6 v2 face à des journaux hostiles. Lecture seule de l'orchestrateur copié."""
import hashlib
import os
import sys

RACINE = sys.argv[1]
sys.path.insert(0, os.path.join(RACINE, "essais"))
sys.path.insert(0, RACINE)

import aides_na_lot6_v2 as A6  # noqa: E402
from aides_na_lot6_v2 import L10  # noqa: E402
from pole import course_na_v2 as cn  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import matiere_premiere_na_v1 as mp  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402


def planter(vus):
    def f(g, gen):
        if g != 1:
            return
        cle = next(iter(gen.course_na.requetes))
        case = next(c for c in gen.course_na.cases if c.identifiant == cle[0])
        octets = gen.course_na.synthese.octets.rstrip(b"\n") + b"\n" + L10.enonce(0).encode("utf-8") + b"\n"
        synthese = rq.charger_piece(gen.course_na.synthese.nom, octets, hashlib.sha256(octets).hexdigest())
        r = rq.assembler_proposeur(gen.course_na.gabarit, case, synthese, 1)
        gen.course_na.requetes[cle] = r
        vus.append(r.sha256)
    return f


class SurchargeEnvoi(mp.JournalRequetesColonneNA):
    """Sous-classe du journal de la colonne qui surcharge l'envoi : ne garde rien."""

    def journaliser_envoi(self, requete, garde, *, role, cle):
        return jn.JournalRequetes.journaliser_envoi(self, requete, garde, role=role, cle=cle)


class ImitateurPlat:
    """Imite l'interface sans hériter : délègue à un journal ordinaire, porte un `depart` d'allure juste."""

    def __init__(self, reel, depart):
        object.__setattr__(self, "_reel", reel)
        object.__setattr__(self, "depart", depart)

    def __getattr__(self, nom):
        return getattr(object.__getattribute__(self, "_reel"), nom)


class ImitateurClasse(ImitateurPlat):
    """Même chose, et se déclare de la classe du journal de la colonne par `__class__`."""

    @property
    def __class__(self):
        return mp.JournalRequetesColonneNA


class SousClasseSimple(jn.JournalRequetes):
    """Hérite du journal du lot 3 seulement, porte un `depart` juste."""

    def __init__(self, dossier, nom, depart):
        super().__init__(dossier, nom)
        self.depart = depart


def fab_surcharge(etat):
    return lambda d, n: SurchargeEnvoi(d, n, depart=A6.depart_colonne(etat))


def fab_imitateur(classe, etat):
    return lambda d, n: classe(jn.JournalRequetes(d, n), A6.depart_colonne(etat))


def fab_sous_classe_simple(etat):
    return lambda d, n: SousClasseSimple(d, n, A6.depart_colonne(etat))


def jouer(nom, etat, fabrique):
    m = A6.Montage()
    m.etat_colonne, m.fabrique_journal = etat, fabrique
    vus = []
    resultat = None
    try:
        bilan = m.lancer(crochets={"avant_execution": planter(vus)})
        resultat = f"course finie, {len(bilan)} générations"
    except BaseException as e:  # noqa: BLE001
        resultat = f"arrêt {type(e).__name__}"
    envois = []
    try:
        envois = [l["sha256"] for l in jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g1.jsonl"))
                  if l["evenement"] == "envoi"]
    except BaseException as e:  # noqa: BLE001
        envois = [f"journal illisible : {type(e).__name__}"]
    part = bool(vus) and vus[0] in envois
    print(f"{nom} | état {etat} | {resultat} | ligne plantée plantée={bool(vus)} | partie={part}")


if __name__ == "__main__":
    for etat in (1, 2):
        pass
    jouer("S0 témoin : journal de la colonne sain", 1, A6.fabrique_colonne(1))
    jouer("S1 sous-classe qui surcharge l'envoi", 1, fab_surcharge(1))
    import tempfile
    _d2 = L10.depart(2, conditions_allumage=L10.conditions(tempfile.mkdtemp(prefix="sonde-d2-")))
    jouer("S1b sous-classe qui surcharge l'envoi", 2, lambda d, n: SurchargeEnvoi(d, n, depart=_d2))
    jouer("S2 imitateur plat (sans héritage ni __class__)", 1, fab_imitateur(ImitateurPlat, 1))
    jouer("S3 imitateur qui falsifie __class__", 1, fab_imitateur(ImitateurClasse, 1))
    jouer("S3b imitateur qui falsifie __class__", 2, lambda d, n: ImitateurClasse(jn.JournalRequetes(d, n), _d2))
    jouer("S3c état 2 journal ordinaire (témoin du refus)", 2, A6.fabrique_ordinaire)
    jouer("S4 hérite du journal du lot 3 + depart juste", 1, fab_sous_classe_simple(1))
    jouer("S5 état 0 journal ordinaire", 0, A6.fabrique_ordinaire)
    jouer("S6 état 0 sous-classe qui surcharge l'envoi", 0, fab_surcharge(0))
    jouer("S7 état 0 imitateur plat", 0, fab_imitateur(ImitateurPlat, 0))
    jouer("S8 état 0 journal de la colonne en état 2", 0, lambda d, n: mp.JournalRequetesColonneNA(d, n, depart=L10.depart(2, conditions_allumage=L10.conditions(d))))
