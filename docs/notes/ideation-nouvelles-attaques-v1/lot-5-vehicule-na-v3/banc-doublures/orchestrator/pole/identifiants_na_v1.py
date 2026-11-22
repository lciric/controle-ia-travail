"""DOUBLURE D'ESSAI du module `identifiants_na_v1` (lot 1), déclarée comme telle — ce n'est PAS le module du lot 1.

Le lot 1 et les paquets du lot 2 v5 et du lot 3 v3 manquent à la copie de l'orchestrateur de ce banc (mandat de la v2 du
lot 5 : chemins non fournis, non cherchés). Cette doublure ne porte que les noms publics que lisent `portier_na_v1`,
`registre_na_v1`, `verifier_registre_servi_na_v1` et `registre_na_v2`, avec une forme voisine (syllabes de deux lettres,
mot de case de trois syllabes, identifiant de fiche de six octets en dix-huit lettres) ; son encodage n'est pas celui du
lot 1. Les essais du lot 5 v2 doivent être rejoués sur une copie où les lots 1 à 3 et 5 v1 sont posés.
"""

CONSONNES = "bcdfghjklmnprstv"
VOYELLES = "aeio"
SYLLABES = tuple(c + v for c in CONSONNES for v in VOYELLES)  # 64
RANG_SYLLABE = {s: i for i, s in enumerate(SYLLABES)}
SYLLABES_CASE = 3
SYLLABES_FICHE = 9


class MotRefuse(ValueError):
    pass


class EncodageRefuse(ValueError):
    pass


def _mot(valeur, n_syllabes):
    s = []
    for _ in range(n_syllabes):
        valeur, r = divmod(valeur, len(SYLLABES))
        s.append(SYLLABES[r])
    if valeur:
        raise EncodageRefuse("valeur au-delà du mot")
    return "".join(reversed(s))


def _valeur(mot, n_syllabes):
    if type(mot) is not str:
        raise MotRefuse("un mot est une chaîne")
    if len(mot) != 2 * n_syllabes:
        raise MotRefuse("longueur")
    v = 0
    for i in range(0, len(mot), 2):
        syllabe = mot[i:i + 2]
        if syllabe not in RANG_SYLLABE:
            raise MotRefuse("hors alphabet")
        v = v * len(SYLLABES) + RANG_SYLLABE[syllabe]
    return v


def mot_de_case(rang):
    return _mot(rang, SYLLABES_CASE)


def rang_du_mot_de_case(mot):
    return _valeur(mot, SYLLABES_CASE)


def encoder_identifiant_fiche(octets):
    return _mot(int.from_bytes(bytes(octets), "big"), SYLLABES_FICHE)


def decoder_octets(mot, n_octets):
    valeur = _valeur(mot, SYLLABES_FICHE)
    if valeur >= 256 ** n_octets:
        raise EncodageRefuse("au-delà de la borne")
    return valeur.to_bytes(n_octets, "big")
