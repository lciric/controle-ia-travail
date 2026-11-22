"""Véhicule NA-1, lot 5 v3 — le portier neuf, passeport marqué `par_repli` (`portier_na_v3`).

Lettre : erratum 2 à l'interface des lots 5, 6 et 7, point (d) : « le passeport du portier porte la même marque quand son
verdict est servi par repli (demande du lot 4 v2) » ; projet d'additif v2, P17 (un verdict du portier rendu par un modèle de
repli vaut verdict du rôle ; le passeport est délivré, marqué « par repli »).

Le portier du lot 5 v1 (`portier_na_v1.PortierNA`) est repris **sans changer une ligne de son classement** : ce module
l'enveloppe. La fonction `appeler` que donne la génération (lot 6) rend, pour un appel lu par le noyau, son dictionnaire
(`{"lu": …, …}`) ; **sous ce portier, ce dictionnaire porte en plus la clé `par_repli`, un booléen** (vrai si la tentative
qui a rendu le verdict est de rang 1 ou 2). Une clé absente, ou qui n'est pas un booléen, fait refuser (`PortierRefuse`) :
la marque n'est jamais devinée. Les autres issues (`None`, appel non lancé ; refus écrit) ne délivrent aucun passeport et ne
portent pas la clé.

Le passeport d'une fiche « passée » est un `PasseportV3` : les champs du v1 et `par_repli`. `exiger_passeport` le rend (A17
inchangé : aucun passeport, ou un texte qui n'est plus celui qui a été classé, lève l'arrêt). L'issue de la fiche
(`IssueFiche` du v1) porte ce passeport. Bibliothèque standard, et les modules des lots 1, 3 et 5.
"""

import dataclasses
from collections.abc import Mapping

from pole import portier_na_v1 as pt

VERSION = "portier-na-v3"
CLE_PAR_REPLI = "par_repli"
PortierRefuse = pt.PortierRefuse
ArretSansPasseportNA = pt.ArretSansPasseportNA


@dataclasses.dataclass(frozen=True)
class PasseportV3:
    """Le passeport du v1, et la marque `par_repli` du verdict qui l'a délivré."""

    identifiant: str
    empreinte: str
    generation: object
    identifiant_case: str
    par_repli: bool


class PortierNAV3(pt.PortierNA):
    """Le portier du v1, dont chaque passeport porte la marque `par_repli` lue dans l'issue d'appel."""

    def __init__(self, *, appeler, **kw):
        if not callable(appeler):
            raise PortierRefuse("`appeler` est la fonction d'appel de la génération")
        self._marque_du_dernier_appel = None

        def appeler_marque(requete, lire):
            self._marque_du_dernier_appel = None
            issue = appeler(requete, lire)
            if isinstance(issue, Mapping) and "lu" in issue:
                marque = issue.get(CLE_PAR_REPLI)
                if type(marque) is not bool:
                    raise PortierRefuse("issue d'appel lue sans la marque `par_repli` (un booléen) : jamais devinée")
                self._marque_du_dernier_appel = marque
            return issue

        super().__init__(appeler=appeler_marque, **kw)

    def classer_fiche(self, fiche, *, identifiant, case):
        issue = super().classer_fiche(fiche, identifiant=identifiant, case=case)
        if issue.passeport is None:
            return issue
        marque = self._marque_du_dernier_appel
        if type(marque) is not bool:
            raise PortierRefuse("passeport sans marque `par_repli`")
        p = issue.passeport
        p3 = PasseportV3(p.identifiant, p.empreinte, p.generation, p.identifiant_case, marque)
        self._passeports[issue.identifiant] = p3
        issue = dataclasses.replace(issue, passeport=p3)
        self._issues_fiches[-1] = issue
        return issue

    def comptes(self):
        c = super().comptes()
        c["passeports_par_repli"] = sum(1 for p in self._passeports.values() if p.par_repli)
        return c


__all__ = ["PortierNAV3", "PasseportV3", "CLE_PAR_REPLI", "VERSION"]
