"""Aides des essais du lot 5 v3 du véhicule NA-1 (registre des tentatives d'appel) : données factices seules, inertes.

Aucune pièce réelle n'est lue ; aucun identifiant de modèle : les modèles demandés sont des identifiants par rôle factices
(`id-role-…`), les modèles servis des chaînes factices (`servi-factice-…`). Ces aides ne lisent que les noms publics des
modules des lots 1 et 5 v1 ; elles tournent sur une application réelle comme au banc à doublures.
"""

import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from pole import contrat_fiche_na_v1 as ct  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import portier_na_v1 as pt  # noqa: E402
from pole import registre_na_v3 as rg3  # noqa: E402

MODELES = ("id-role-espece", "id-role-repli-1", "id-role-repli-2", "id-role-portier")
SERVI = "servi-factice-a"
SERVI_REPLI = "servi-factice-b"


def cases(n=4, depart=1000):
    return [ident.mot_de_case(depart + 37 * k) for k in range(n)]


CASES = cases()


def mot_fiche(n):
    return ident.encoder_identifiant_fiche(int(n).to_bytes(6, "big"))


def contenu(case, **remplace):
    c = {
        "case": case,
        "ce_que_le_moniteur_suppose": "trait factice deux",
        "menace_du_programme": "sabotage factice",
        "etage_de_lecture": "étage factice un",
        "idee": "Idée factice, inerte,\n  sur deux lignes.",
        "mesurable_sur_monde_plante": "grandeur factice",
        "ce_qui_la_refuterait": "issue factice une",
        "issue_contraire": "issue factice deux",
        "voisin_le_plus_proche_connu": "aucun connu",
        "ecart_au_voisin": "écart factice",
        "filiation": "aucune",
        "piece_produite": "publique",
    }
    c.update(remplace)
    return c


def issue(n, classe=pt.PASSEE, case=None, generation=1, **remplace):
    """Une fiche classée factice (`IssueFiche`), construite sans appel au portier."""
    case = CASES[0] if case is None else case
    return pt.IssueFiche(mot_fiche(n), generation, case, classe, "cause factice", False, "0" * 64, None,
                         contenu(case, **remplace), ())


def tentative(rang=0, *, espece="espece-1", case=..., classe_issue=pt.FICHES_RENDUES, raison="end_turn",
              modele=None, servi=..., cout=0.25, **autres):
    t = {"espece": espece, "case": CASES[0] if case is ... else case, "rang_repli": rang,
         "modele_demande": modele or MODELES[rang], "modele_servi": (SERVI if rang == 0 else SERVI_REPLI) if servi is ... else servi,
         "raison_arret": raison, "cout_compte_usd": cout, "classe_issue": classe_issue}
    t.update(autres)
    return t


def refus(rang=0, **k):
    k.setdefault("categorie_refus", "categorie-factice")
    k.setdefault("classe_issue", rg3.REFUS_SERVI_PAR_REPLI)
    return tentative(rang, raison=rg3.RAISON_REFUS, **k)


def registre(dossier, nom="registre-tentatives-essai-v3.jsonl", generation=1, cases_servies=None, modeles=MODELES):
    return rg3.RegistreTentativesV3(dossier, nom, generation=generation,
                                    cases_servies=CASES if cases_servies is None else cases_servies,
                                    modeles_demandes=modeles)


def lire(chemin, generation=1, cases_servies=None, **k):
    return rg3.lire_registre_tentatives_v3(chemin, generation=generation,
                                           cases_servies=CASES if cases_servies is None else cases_servies,
                                           modeles_demandes=MODELES, **k)


def taille(chemin):
    return os.path.getsize(chemin)


def sha(octets):
    import hashlib
    return hashlib.sha256(octets).hexdigest()


__all__ = ["ct", "ident", "pt", "rg3"]
