"""Véhicule NA-1, lot 1 — identifiants neutres réencodés sans suite hexadécimale (`identifiants_na_v1`).

Lettre : conception du véhicule v4 (`3428dfb3…`), § 5.2, règle d'encodage en cinq points, acceptée par la mère
(07:46Z, mot 1), « éprouvée dans les deux sens » ; V9, l. 75 (aucune suite de huit caractères hexadécimaux, ni rang, ni
numéro sur un total, ni morceau d'empreinte).

1. Alphabet : douze consonnes, de rang 0 à 11 : g, j, k, l, m, n, p, r, s, t, v, z ; cinq voyelles, de rang 0 à 4 :
   a, e, i, o, u. Une syllabe est une consonne suivie d'une voyelle ; son rang, de 0 à 59, vaut cinq fois le rang de la
   consonne plus le rang de la voyelle. Minuscules seules.
2. Ordre des octets : les octets, dans leur ordre, sont lus comme un seul entier, le premier octet étant le plus fort.
3. Écriture : l'entier est écrit en base 60, le chiffre le plus fort d'abord, sur une longueur fixe, complétée à gauche
   par la syllabe de rang 0 ; aucun préfixe, aucun séparateur.
4. Longueurs : six octets (une fiche), neuf syllabes, dix-huit lettres ; cinq octets (l'identifiant servi au juge), sept
   syllabes, quatorze lettres ; trois syllabes, l'identifiant de case (un rang de 0 à 215 999, tiré par la clé n° 40).
5. Décodage : un mot est décodé s'il a la longueur attendue, s'il se découpe en syllabes de l'alphabet, et si l'entier
   obtenu est inférieur à 256 puissance le nombre d'octets ; sinon il est refusé, jamais corrigé.

C'est un encodage, non un tirage : aucun aléa ici. Bibliothèque standard seule.
"""

import re

VERSION = "identifiants-na-v1"

CONSONNES = "gjklmnprstvz"
VOYELLES = "aeiou"
SYLLABES = tuple(c + v for c in CONSONNES for v in VOYELLES)  # rang = 5 × rang(consonne) + rang(voyelle)
RANG_SYLLABE = {s: i for i, s in enumerate(SYLLABES)}
BASE = 60

# nombre d'octets -> nombre de syllabes (point 4)
SYLLABES_PAR_OCTETS = {6: 9, 5: 7}
SYLLABES_CASE = 3
MOTS_DE_CASE = BASE ** SYLLABES_CASE  # 216 000

_HEXA = re.compile(r"[0-9A-Fa-f]{8,}")


class MotRefuse(ValueError):
    """Un mot que la règle ne décode pas : refusé, jamais corrigé (point 5)."""

    def __init__(self, cause):
        super().__init__(f"mot refusé : {cause}")
        self.cause = cause


class EncodageRefuse(ValueError):
    """Une valeur que la règle n'encode pas (longueur d'octets ou entier hors de la longueur fixe)."""


def _verifier_syllabes(n_syllabes):
    if type(n_syllabes) is not int or n_syllabes < 1:
        raise EncodageRefuse("nombre de syllabes invalide")


def encoder_entier(valeur, n_syllabes):
    """Écrit `valeur` en base 60 sur `n_syllabes` syllabes, le chiffre le plus fort d'abord (points 1 et 3)."""
    _verifier_syllabes(n_syllabes)
    if type(valeur) is not int or valeur < 0 or valeur >= BASE ** n_syllabes:
        raise EncodageRefuse("entier hors de la longueur fixe")
    chiffres = []
    reste = valeur
    for _ in range(n_syllabes):
        reste, r = divmod(reste, BASE)
        chiffres.append(r)
    return "".join(SYLLABES[r] for r in reversed(chiffres))


def decoder_entier(mot, n_syllabes):
    """L'inverse d'`encoder_entier` : longueur exacte, syllabes de l'alphabet, sinon refus (point 5)."""
    _verifier_syllabes(n_syllabes)
    if type(mot) is not str:
        raise MotRefuse("pas une chaîne")
    if len(mot) != 2 * n_syllabes:
        raise MotRefuse("longueur")
    valeur = 0
    for i in range(0, len(mot), 2):
        syllabe = mot[i:i + 2]
        if syllabe not in RANG_SYLLABE:
            raise MotRefuse("hors alphabet")
        valeur = valeur * BASE + RANG_SYLLABE[syllabe]
    return valeur


def encoder_octets(octets):
    """Six octets : dix-huit lettres ; cinq octets : quatorze lettres (points 2 à 4)."""
    if not isinstance(octets, (bytes, bytearray)):
        raise EncodageRefuse("pas des octets")
    n = len(octets)
    if n not in SYLLABES_PAR_OCTETS:
        raise EncodageRefuse("nombre d'octets hors de la règle (6 ou 5)")
    valeur = int.from_bytes(bytes(octets), "big")  # premier octet le plus fort (point 2)
    return encoder_entier(valeur, SYLLABES_PAR_OCTETS[n])


def decoder_octets(mot, n_octets):
    """Rend les `n_octets` octets d'un mot, ou le refuse (longueur, alphabet, borne : point 5)."""
    if n_octets not in SYLLABES_PAR_OCTETS:
        raise EncodageRefuse("nombre d'octets hors de la règle (6 ou 5)")
    valeur = decoder_entier(mot, SYLLABES_PAR_OCTETS[n_octets])
    if valeur >= 256 ** n_octets:
        raise MotRefuse("entier au-delà de la borne")
    return valeur.to_bytes(n_octets, "big")


def encoder_identifiant_fiche(octets):
    """Identifiant d'une fiche : les six octets du jeton du noyau, dix-huit lettres."""
    if len(octets) != 6:
        raise EncodageRefuse("une fiche a six octets")
    return encoder_octets(octets)


def encoder_identifiant_juge(octets):
    """Identifiant servi au juge : les cinq octets du jeton du noyau, quatorze lettres."""
    if len(octets) != 5:
        raise EncodageRefuse("l'identifiant servi au juge a cinq octets")
    return encoder_octets(octets)


def reencoder_jeton_noyau(jeton, prefixe, n_octets):
    """Réencode un jeton du noyau (`prefixe` suivi de 2 × `n_octets` caractères hexadécimaux minuscules) : mêmes octets,
    autre écriture. Tout autre jeton est refusé, jamais corrigé."""
    if type(jeton) is not str or type(prefixe) is not str or len(prefixe) != 1:
        raise EncodageRefuse("jeton ou préfixe invalide")
    corps = jeton[1:]
    if not jeton.startswith(prefixe) or len(corps) != 2 * n_octets or re.fullmatch(r"[0-9a-f]+", corps) is None:
        raise EncodageRefuse("jeton du noyau mal formé")
    return encoder_octets(bytes.fromhex(corps))


def mot_de_case(rang):
    """Identifiant de case : un rang de 0 à 215 999 (clé n° 40), trois syllabes, six lettres."""
    if type(rang) is not int or rang < 0 or rang >= MOTS_DE_CASE:
        raise EncodageRefuse("rang de mot de case hors de 0 à 215 999")
    return encoder_entier(rang, SYLLABES_CASE)


def rang_du_mot_de_case(mot):
    """L'inverse de `mot_de_case` ; refuse tout mot qui n'a pas trois syllabes de l'alphabet."""
    return decoder_entier(mot, SYLLABES_CASE)


def porte_suite_hexadecimale(texte, longueur=8):
    """Vrai si `texte` porte une suite d'au moins `longueur` caractères hexadécimaux (V9, l. 75 ; l. 387)."""
    if longueur != 8:
        return re.search(r"[0-9A-Fa-f]{%d,}" % int(longueur), texte) is not None
    return _HEXA.search(texte) is not None
