"""Montant requis de la ligne de GO, version 68 (fichier neuf, R12 ; `pole/configuration_v54.py` inchangé).

Précision (i) de la contre-lecture du rang 0 : `configuration_v54.montant_requis` compte (N − 1) étages, parce que l'orchestrateur
jusqu'à la v59 ne joue l'étage de tests de mort qu'entre deux générations. La v68 peut jouer l'étage après la dernière génération
aussi (`etage_apres_derniere`) : le nombre d'étages devient un argument nommé, sans défaut, et la fonction vit ici.

- portée « par_generation » : N × S17 + E × plafond de l'étage, E = nombre d'étages joués (0 ≤ E ≤ N) ;
- portée « course » : **une génération et aucun étage seulement**. La v68 refuse la portée « course » pour N > 1 ou E > 0 :
  chaque génération reprend son plafond S17 à zéro (`noyau_v56`, l. 106), donc une course de N générations peut dépenser
  N × S17 ; une ligne de GO à S17 ne la couvre pas. La garde de la course (`budget_course_v68`) cumule sur la course et
  s'arrête à son plafond ; elle ne rend pas sûre une ligne de GO qui ne couvre pas la course.

`nombre_etages_v68` dit E à partir du régime (étage présent ? après la dernière génération ?)."""

from .configuration_v53 import ConfigurationRefusee
from .configuration_v54 import PORTEES

VERSION = "configuration-v68 (montant requis : N générations, E étages)"


def _entier(v, mini):
    return isinstance(v, int) and not isinstance(v, bool) and v >= mini


def _reel_positif(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and float(v) > 0


def nombre_etages_v68(nombre_generations, etage_present, etage_apres_derniere):
    """E : aucun étage sans étage ; sinon N − 1 (entre deux générations) ou N (après la dernière aussi)."""
    if not _entier(nombre_generations, 1):
        raise ConfigurationRefusee("nombre de générations : entier ≥ 1, aucun défaut")
    if not isinstance(etage_present, bool) or not isinstance(etage_apres_derniere, bool):
        raise ConfigurationRefusee("étage présent et étage après la dernière génération : booléens exigés (aucun défaut)")
    if not etage_present:
        if etage_apres_derniere:
            raise ConfigurationRefusee("étage après la dernière génération demandé sans étage de tests de mort : refus")
        return 0
    return nombre_generations if etage_apres_derniere else nombre_generations - 1


def montant_requis_v68(conf, nombre_generations, plafond_etage_usd=None, *, nombre_etages):
    """Montant que la ligne de GO doit porter **exactement** pour N générations et E étages (portée « par_generation ») ;
    S17 pour une génération sans étage en portée « course » ; refus sinon."""
    s17 = float(conf["budget"]["plafond_usd"])
    if not _entier(nombre_generations, 1):
        raise ConfigurationRefusee("nombre de générations : entier ≥ 1, aucun défaut")
    if not _entier(nombre_etages, 0) or nombre_etages > nombre_generations:
        raise ConfigurationRefusee(f"nombre d'étages : entier entre 0 et N = {nombre_generations} exigé (reçu {nombre_etages!r})")
    if nombre_etages > 0 and not _reel_positif(plafond_etage_usd):
        raise ConfigurationRefusee("plafond de l'étage : réel > 0 exigé dès qu'un étage est joué (aucun défaut)")
    portee = conf["budget"].get("portee_plafond")
    if portee == "course":
        if nombre_generations > 1 or nombre_etages > 0:
            raise ConfigurationRefusee(
                "budget.portee_plafond « course » refusée par la v68 pour plus d'une génération ou un étage : chaque génération "
                "reprend son plafond S17 à zéro (noyau v56) ; la ligne de GO ne couvrirait pas la course : portée "
                "« par_generation » exigée")
        return s17
    if portee != "par_generation":
        raise ConfigurationRefusee(f"budget.portee_plafond : {PORTEES} exigé (reçu {portee!r})")
    return nombre_generations * s17 + nombre_etages * (float(plafond_etage_usd) if nombre_etages else 0.0)


__all__ = ("montant_requis_v68", "nombre_etages_v68", "VERSION")
