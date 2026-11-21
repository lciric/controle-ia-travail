"""Sonde du vérificateur, v3 : le refus de câblage du lot 6 v3 face à des journaux hostiles.
Usage : sonde_cablage_v3.py RACINE_ORCHESTRATOR (base|avant-import)."""
import hashlib
import os
import sys
import tempfile

RACINE = sys.argv[1]
MODE = sys.argv[2]
sys.path.insert(0, os.path.join(RACINE, "essais"))
sys.path.insert(0, RACINE)

from pole import journal_na_v3 as jn  # noqa: E402
from pole import matiere_premiere_na_v1 as mp  # noqa: E402

if MODE == "avant-import":
    # La classe de la colonne est modifiée AVANT l'import du lot 6 v3 (limite F-1 du rapport).
    def _passe(self, requete, garde, *, role, cle):
        return jn.JournalRequetes.journaliser_envoi(self, requete, garde, role=role, cle=cle)
    mp.JournalRequetesColonneNA.journaliser_envoi = _passe

import aides_na_lot6_v3 as A6  # noqa: E402
from aides_na_lot6_v3 import L10  # noqa: E402
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
    def journaliser_envoi(self, requete, garde, *, role, cle):
        return jn.JournalRequetes.journaliser_envoi(self, requete, garde, role=role, cle=cle)


class SousClasseMuette(mp.JournalRequetesColonneNA):
    pass


class ImitateurPlat:
    def __init__(self, reel, depart):
        object.__setattr__(self, "_reel", reel)
        object.__setattr__(self, "depart", depart)

    def __getattr__(self, nom):
        return getattr(object.__getattribute__(self, "_reel"), nom)


class ImitateurClasse(ImitateurPlat):
    @property
    def __class__(self):
        return mp.JournalRequetesColonneNA


class SousClasseSimple(jn.JournalRequetes):
    def __init__(self, dossier, nom, depart):
        super().__init__(dossier, nom)
        self.depart = depart


_D2 = L10.depart(2, conditions_allumage=L10.conditions(tempfile.mkdtemp(prefix="sonde3-d2-")))


def dep(etat):
    return _D2 if etat == 2 else A6.depart_colonne(etat)


def fab_envoi_instance(etat):
    def f(d, n):
        j = mp.JournalRequetesColonneNA(d, n, depart=dep(etat))
        j.journaliser_envoi = lambda requete, garde, *, role, cle: jn.JournalRequetes.journaliser_envoi(j, requete, garde, role=role, cle=cle)
        return j
    return f


def jouer(nom, etat, fabrique, apres=None):
    m = A6.Montage()
    m.etat_colonne, m.fabrique_journal = etat, fabrique
    vus = []
    base = planter(vus)

    def crochet(g, gen):
        base(g, gen)
        if apres is not None and g == 1:
            apres(gen)
    try:
        bilan = m.lancer(crochets={"avant_execution": crochet})
        resultat = f"course finie, {len(bilan)} générations"
    except BaseException as e:  # noqa: BLE001
        resultat = f"arrêt {type(e).__name__}"
    try:
        envois = [l["sha256"] for l in jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g1.jsonl"))
                  if l["evenement"] == "envoi"]
    except BaseException as e:  # noqa: BLE001
        envois = [f"illisible:{type(e).__name__}"]
    part = bool(vus) and vus[0] in envois
    print(f"{nom} | état {etat} | {resultat} | plantée={bool(vus)} | partie={part}", flush=True)


def fab_exact(etat):
    return lambda d, n: mp.JournalRequetesColonneNA(d, n, depart=dep(etat))


if MODE == "avant-import":
    jouer("P1 classe de la colonne modifiée avant l'import, journal exact", 1, fab_exact(1))
    jouer("P1b idem", 2, fab_exact(2))
    sys.exit(0)

for etat in (1, 2):
    jouer("S0 témoin journal exact", etat, fab_exact(etat))
    jouer("S1 sous-classe qui surcharge l'envoi", etat, lambda d, n, e=etat: SurchargeEnvoi(d, n, depart=dep(e)))
    jouer("S1m sous-classe muette", etat, lambda d, n, e=etat: SousClasseMuette(d, n, depart=dep(e)))
    jouer("S2 imitateur plat", etat, lambda d, n, e=etat: ImitateurPlat(jn.JournalRequetes(d, n), dep(e)))
    jouer("S3 imitateur __class__ falsifié", etat, lambda d, n, e=etat: ImitateurClasse(jn.JournalRequetes(d, n), dep(e)))
    jouer("S4 sous-classe du lot 3, départ juste", etat, lambda d, n, e=etat: SousClasseSimple(d, n, dep(e)))
    jouer("S3c journal ordinaire", etat, A6.fabrique_ordinaire)
    jouer("S9 envoi posé sur l'instance", etat, fab_envoi_instance(etat))

# état 0 : aucun refus à tort
jouer("S5 état 0 journal ordinaire", 0, A6.fabrique_ordinaire)
jouer("S6 état 0 sous-classe qui surcharge l'envoi", 0, lambda d, n: SurchargeEnvoi(d, n, depart=A6.depart_colonne(0)))
jouer("S5b état 0 journal exact de la colonne éteinte", 0, fab_exact(0))
jouer("S5c état 0 sous-classe muette", 0, lambda d, n: SousClasseMuette(d, n, depart=A6.depart_colonne(0)))

# classe de la colonne modifiée APRÈS l'import (doit être refusée)
orig = mp.JournalRequetesColonneNA.__dict__["journaliser_envoi"]


def _passe(self, requete, garde, *, role, cle):
    return jn.JournalRequetes.journaliser_envoi(self, requete, garde, role=role, cle=cle)


mp.JournalRequetesColonneNA.journaliser_envoi = _passe
jouer("S10 envoi de la classe remplacé après l'import", 1, fab_exact(1))
mp.JournalRequetesColonneNA.journaliser_envoi = orig

# classe mère du journal modifiée (écart F-1) : la garde de la colonne s'exécute avant `super()`
orig_mere = jn.JournalRequetes.__dict__["journaliser_envoi"]


def _mere(self, requete, garde, *, role, cle):
    return orig_mere(self, requete, garde, role=role, cle=cle)


jn.JournalRequetes.journaliser_envoi = _mere
jouer("S11 classe mère modifiée (enveloppe), journal exact", 1, fab_exact(1))
jn.JournalRequetes.journaliser_envoi = orig_mere

# examiner_octets de la Colonne remplacé sur la classe après l'import (hostile, hors du refus)
orig_ex = mp.Colonne.examiner_octets
mp.Colonne.examiner_octets = lambda self, octets: []
jouer("S12 Colonne.examiner_octets vidée sur la classe après l'import", 1, fab_exact(1))
mp.Colonne.examiner_octets = orig_ex

# __code__ de la méthode d'envoi échangé (identité de la fonction inchangée)
f = mp.JournalRequetesColonneNA.__dict__["journaliser_envoi"]
code_orig = f.__code__
class _X(jn.JournalRequetes):
    def journaliser_envoi(self, requete, garde, *, role, cle):
        return super().journaliser_envoi(requete, garde, role=role, cle=cle)


f.__code__ = _X.__dict__["journaliser_envoi"].__code__
jouer("S13 __code__ de l'envoi de la colonne échangé après l'import", 1, fab_exact(1))
f.__code__ = code_orig


# contrôle ponctuel (F-2) : `depart` remplacé après la construction
def retire_depart(gen):
    gen.na.journal.depart = A6.depart_colonne(0)


jouer("S14 depart du journal remplacé après la construction", 1, fab_exact(1), apres=retire_depart)
