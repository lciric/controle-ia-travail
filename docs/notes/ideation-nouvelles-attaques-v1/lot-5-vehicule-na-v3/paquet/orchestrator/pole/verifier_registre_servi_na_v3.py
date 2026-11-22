"""Véhicule NA-1, lot 5 v3 — vérification du registre servi marqué `par_repli`, avant tout envoi
(`verifier_registre_servi_na_v3`) : arrêts n° 8, n° 9 et n° 19.

Lettre : celle de `verifier_registre_servi_na_v1` (V9, l. 63, 120, 379, 380, 390 ; conception v5, § 2.6, § 6.1), et
l'erratum 2 à l'interface des lots 5, 6 et 7, point (d) : chaque ligne de tentative du registre servi porte un champ fermé
`par_repli`, entre la classe et l'énoncé (forme de `registre_na_v3`).

Le programme lit le fichier entier. Pour chaque ligne de tentative, il lit le champ `par_repli` : une valeur hors de la
liste fermée (`par_repli : vrai`, `par_repli : faux`), ou un champ absent, est un défaut de l'arrêt n° 19. Il retire ce
champ, puis passe le registre ainsi ramené à la forme du v1 au vérificateur du v1, qui fait tous les autres contrôles
(étiquettes interdites, marques, énoncé, comptes, lignes attendues), **sans réécrire aucun de ses motifs**. La borne en
octets (arrêt n° 8) est contrôlée ici, **sur le fichier entier tel qu'il sera servi**, marques comprises. Tous les défauts
sont rendus ensemble ; `RegistreServiNonConformeV3` est une sous-classe de l'exception du v1 : l'appelant qui attrape
celle du v1 attrape aussi celle-ci. Aucune ligne n'est retirée. Bibliothèque standard, et les modules des lots 1 et 5.
"""

from pole import registre_na_v1 as rg
from pole import registre_na_v3 as rg3
from pole import verifier_registre_servi_na_v1 as vr

VERSION = "verifier-registre-servi-na-v3"
Defaut = vr.Defaut
ConstatConforme = vr.ConstatConforme


class RegistreServiNonConformeV3(vr.RegistreServiNonConforme):
    """Le registre servi marqué n'est pas conforme : la génération ne part pas ; aucune ligne n'est retirée."""


def _retirer_marque(ligne):
    """Rend (ligne ramenée à la forme du v1, cause ou None)."""
    parts = ligne[len(rg.TETE_TENTATIVE):].split(rg.SEPARATEUR, 6)
    if len(parts) != 7:
        return ligne, "ligne de tentative sans le champ `par_repli`"
    if parts[5] not in rg3.PAR_REPLI.values():
        return ligne, "ligne de tentative : champ `par_repli` hors de la liste fermée"
    return rg.TETE_TENTATIVE + rg.SEPARATEUR.join(parts[:5] + parts[6:]), None


def verifier_registre_servi_v3(octets, *, borne_registre_octets, borne_enonce_octets, noms_attendus=None,
                               cases_attendues=None):
    """Vérifie le registre servi marqué ; rend le `ConstatConforme` du v1 (taille : celle du fichier servi), ou lève
    `RegistreServiNonConformeV3` avec tous les défauts."""
    if not isinstance(octets, (bytes, bytearray)):
        raise TypeError("le registre servi se vérifie en octets")
    if type(borne_registre_octets) is not int or borne_registre_octets <= 0:
        raise ValueError("borne du registre : un entier positif")
    octets = bytes(octets)
    defauts = []
    if len(octets) > borne_registre_octets:
        defauts.append(Defaut(vr.ARRET_TAILLE, None, "registre plus long que sa borne"))
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError:
        raise RegistreServiNonConformeV3(defauts + [Defaut(vr.ARRET_NON_CONFORME, None, "registre qui n'est pas en UTF-8")]) \
            from None
    morceaux = texte.split("\n")
    ramenes = []
    for i, ligne in enumerate(morceaux, start=1):
        if ligne.startswith(rg.TETE_TENTATIVE):
            ligne, cause = _retirer_marque(ligne)
            if cause:
                defauts.append(Defaut(vr.ARRET_NON_CONFORME, i, cause))
        ramenes.append(ligne)
    v1 = "\n".join(ramenes).encode("utf-8")
    try:
        constat = vr.verifier_registre_servi(v1, borne_registre_octets=max(len(v1), 1),
                                             borne_enonce_octets=borne_enonce_octets, noms_attendus=noms_attendus,
                                             cases_attendues=cases_attendues)
    except vr.RegistreServiNonConforme as e:
        raise RegistreServiNonConformeV3(defauts + list(e.defauts)) from None
    if defauts:
        raise RegistreServiNonConformeV3(defauts)
    return ConstatConforme(len(octets), constat.lignes, constat.lignes_tentative, constat.lignes_compte)
