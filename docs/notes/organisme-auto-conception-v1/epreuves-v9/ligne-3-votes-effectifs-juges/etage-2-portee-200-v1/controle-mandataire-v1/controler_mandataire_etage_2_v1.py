"""Contrôle du mandataire avant le geste 9 (additif 6 v2 de l'étage 2, § 9 ; décision R-4325), classe B.

Vérifie, sur `os.environ`, sans jamais imprimer la valeur du mandataire :
(1) HTTPS_PROXY présente et non vide après retrait des espaces (le code d'appel v4 l'exige par son nom en
    majuscules, `VARIABLES_EXIGEES` ; il ne contrôle que la présence, d'où ce contrôle de non-vacuité) ;
(2) NO_PROXY couvre 127.0.0.1 : les relais sont locaux (127.0.0.1:8787 et 127.0.0.1:8788) et ne doivent pas passer
    par le mandataire.

Règle de couverture (intersection de deux conditions, toutes deux exigées) :
  (a) règle du brief : un élément (découpage sur les virgules, espaces retirés) vaut « 127.0.0.1 », ou est une plage
      CIDR qui contient 127.0.0.1 (module ipaddress), ou « * » ;
  (b) règle de la bibliothèque standard de l'interpréteur qui exécute ce contrôle :
      `urllib.request.proxy_bypass_environment` contourne le mandataire pour 127.0.0.1, 127.0.0.1:8787 et
      127.0.0.1:8788. La porte de plafond, lancée par le code d'appel, n'emploie que la bibliothèque standard
      (§ 9) ; sous Python 3.13, urllib ne lit pas les plages CIDR et ne prend « * » que comme valeur entière exacte.
  « localhost » seul ne suffit pas : urllib compare des chaînes, le nom n'est pas l'adresse.

Formes en minuscules : chaque forme présente (`NO_PROXY`, `no_proxy`) doit couvrir à elle seule (urllib préfère la
minuscule et une minuscule vide efface la majuscule ; d'autres clients préfèrent la majuscule). `https_proxy`, si
présente, doit être non vide et égale à HTTPS_PROXY (comparées après retrait des espaces, jamais imprimées), sans quoi
urllib emploierait un autre mandataire que celui contrôlé, ou aucun.

Sortie : une ligne JSON {"https_proxy_non_vide", "no_proxy_couvre_127_0_0_1", "decision", "motifs"}.
Code : 0 si tenu, 3 si refus (erreur interne comprise : aucun repli silencieux).
"""
import ipaddress
import json
import os
import sys
import urllib.request

CIBLE = "127.0.0.1"
HOTES_RELAIS = ("127.0.0.1", "127.0.0.1:8787", "127.0.0.1:8788")
CODE_TENU = 0
CODE_REFUS = 3


def _element_couvrant_brief(valeur):
    """Règle (a). Rend (élément normalisé à imprimer, nature) ou (None, None). N'imprime jamais un élément arbitraire :
    seulement « 127.0.0.1 », « * » ou une plage réécrite par ipaddress."""
    cible = ipaddress.ip_address(CIBLE)
    elements = [e.strip() for e in valeur.split(",") if e.strip()]
    if CIBLE in elements:                       # priorité : exact, puis « * », puis plage
        return CIBLE, "exact"
    if "*" in elements:
        return "*", "etoile"
    for el in elements:
        if "/" not in el:
            continue
        try:
            reseau = ipaddress.ip_network(el, strict=False)
        except ValueError:
            continue
        if reseau.version == 4 and cible in reseau:
            return str(reseau), "plage"
    return None, None


def _urllib_contourne(valeur):
    """Règle (b) : urllib de cet interpréteur contourne-t-il le mandataire pour chaque hôte des relais ?"""
    return all(urllib.request.proxy_bypass_environment(h, {"no": valeur}) for h in HOTES_RELAIS)


def _evaluer_no_proxy(nom, valeur, motifs):
    if not valeur.strip():
        motifs.append(f"{nom} présente mais vide (ou espaces seuls) : 127.0.0.1 passerait par le mandataire")
        return False
    element, nature = _element_couvrant_brief(valeur)
    urllib_ok = _urllib_contourne(valeur)
    if element is not None and urllib_ok:
        motifs.append(f"{nom} couvre 127.0.0.1 par l'élément « {element} »")
        return True
    if nature == "plage":
        motifs.append(f"{nom} : la plage « {element} » contient 127.0.0.1, mais urllib (bibliothèque standard, "
                      f"Python {sys.version_info.major}.{sys.version_info.minor}) ne lit pas les plages : non couvert")
    elif nature == "etoile":
        motifs.append(f"{nom} : « * » n'est lu par urllib que comme valeur entière exacte, "
                      "pas comme élément d'une liste ni entouré d'espaces : non couvert")
    elif urllib_ok:
        motifs.append(f"{nom} : urllib contournerait le mandataire pour 127.0.0.1, mais par un suffixe hors de la "
                      "règle retenue (ni « 127.0.0.1 », ni plage, ni « * ») : non couvert")
    else:
        elements = [e.strip().lower() for e in valeur.split(",")]
        if "localhost" in elements:
            motifs.append(f"{nom} ne couvre pas 127.0.0.1 : « localhost » ne suffit pas (le nom n'est pas l'adresse)")
        else:
            motifs.append(f"{nom} ne couvre pas 127.0.0.1")
    return False


def evaluer(environ):
    """Rend le dictionnaire de sortie. Ne lit que HTTPS_PROXY, https_proxy, NO_PROXY, no_proxy."""
    motifs = []

    # (1) mandataire
    haut = environ.get("HTTPS_PROXY")
    bas = environ.get("https_proxy")
    if haut is None:
        https_ok = False
        motifs.append("HTTPS_PROXY absente : le code d'appel v4 l'exige (VARIABLES_EXIGEES)")
    elif not haut.strip():
        https_ok = False
        motifs.append("HTTPS_PROXY vide (ou espaces seuls) : sous env -i elle passerait vide")
    else:
        https_ok = True
    if bas is not None:
        if not bas.strip():
            https_ok = False
            motifs.append("https_proxy (minuscules) présente et vide : urllib retirerait le mandataire")
        elif haut is not None and haut.strip() and bas.strip() != haut.strip():
            https_ok = False
            motifs.append("https_proxy (minuscules) diffère de HTTPS_PROXY (valeurs non imprimées) : "
                          "urllib emploierait la forme en minuscules, non contrôlée")
    if https_ok:
        motifs.append("HTTPS_PROXY présente et non vide (valeur non imprimée)")

    # (2) contournement pour 127.0.0.1
    formes = [(n, environ[n]) for n in ("NO_PROXY", "no_proxy") if n in environ]
    if not formes:
        no_ok = False
        motifs.append("NO_PROXY et no_proxy absentes : 127.0.0.1 passerait par le mandataire")
    else:
        resultats = [_evaluer_no_proxy(n, v, motifs) for n, v in formes]
        no_ok = all(resultats)

    return {
        "https_proxy_non_vide": https_ok,
        "no_proxy_couvre_127_0_0_1": no_ok,
        "decision": "tenu" if (https_ok and no_ok) else "refus",
        "motifs": motifs,
    }


def main(environ=None):
    try:
        sortie = evaluer(os.environ if environ is None else environ)
    except Exception as exc:  # refus déclaré, jamais un repli silencieux ; aucune valeur dans le motif
        sortie = {"https_proxy_non_vide": False, "no_proxy_couvre_127_0_0_1": False, "decision": "refus",
                  "motifs": [f"erreur interne du contrôle : {type(exc).__name__}"]}
    print(json.dumps(sortie, ensure_ascii=False))
    return CODE_TENU if sortie["decision"] == "tenu" else CODE_REFUS


if __name__ == "__main__":
    sys.exit(main())
