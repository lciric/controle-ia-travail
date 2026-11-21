"""Véhicule NA-1, lot 3 — assemblage de la requête (`requete_na_v2`) : partie servie remplie par la ligne de case du lot 1,
enveloppe sans ajout (D2), composition par rôle, forme de la fiche servie au portier et aux juges, mesure de la taille
(arrêt n° 8).

v2 (remplace `requete_na_v1`, `4dfd3eec…`, archivé sans modification) : des noms seuls changent, pour la v3 du lot 2 ; le
module lit `tirage_na_v3` au lieu de `tirage_na_v2`, dont l'interface est la même. Aucune règle ne change.

Lettre : V9 (`864f39a7…`), l. 69 à 77 (pièces servies, ligne de case, requête assemblée), l. 379 (arrêt n° 8), l. 385
(arrêt n° 14) ; conception du véhicule v5 (`1b7f6822…`), § 0 bis (D2 ; 08:00Z, mot 1 ; 07:46Z, mots 1 et 8), § 2.2, § 2.4
(ce qui est servi au portier), § 2.5 (ce qui est servi à un juge), § 5.2, § 5.3, § 6.2 (partie servie, requête
journalisée), § 7 (lot 3) ; relevé du lot 0 (`10ac79ec…`), Q1, tableau A, et « D2 », points 2 et 3.

- **Un seul encodage.** La requête est une suite d'octets, rendue une fois, figée (`RequeteAssemblee.octets`). C'est elle que
  la garde de motifs lit, que le journal décrit (taille, empreinte) et que l'on envoie (module `journal_na_v2`).
- **Partie servie.** Le gabarit est lu à son empreinte ; le fichier de la question est refusé par son nom avant toute
  ouverture, puis par son empreinte ; le gabarit doit porter un seul emplacement `{{CASE}}`, sur une ligne propre. La ligne
  de case est celle du tirage (lot 1), contrôlée par le lot 1 et rebâtie à l'octet ; elle remplace l'emplacement, et rien
  d'autre ne change.
- **Enveloppe sans ajout (D2).** Pour un proposeur : la partie servie remplie ; une ligne vide ; la synthèse servie à
  l'octet ; aux générations 2 et 3, une ligne vide, le titre de la section du registre sur une ligne, puis le registre
  servi ; un registre vide : la section est omise. Pour une sonde de refus : la partie servie remplie, seule. Aucun texte
  de rôle, aucune syntaxe de sortie, ni la section « Case », ni la section d'héritage, ni le retrait de fin de ligne du
  noyau (relevé du lot 0, « D2 », point 2).
- **Dernier octet gardé (mot 1 de 08:00Z).** Chaque pièce entre avec tous ses octets, le dernier compris ; les séparateurs
  s'ajoutent après. L'empreinte de chaque pièce, prise sur la pièce entière, se retrouve dans la composition.
- **Forme de la fiche servie au portier et aux juges (mot 8 de 07:46Z), gardée et déclarée, octet pour octet** : celle du
  noyau (`fiches_v54.py`, l. 48 à 61), soit, sur le texte de la consigne décodé en UTF-8 :
  `consigne.rstrip() + "\\n\\n## La fiche\\n```json\\n" + json.dumps(contenu, ensure_ascii=False, indent=1) + "\\n```\\n"` ;
  pour un juge, le contenu porte en dernière clé `"identifiant"`, l'identifiant servi réencodé (quatorze lettres, § 5.2).
  Le retrait de fin de consigne (`rstrip`) est dans cette forme ; il ne touche aucune pièce d'une requête de proposeur.
- **Réponse sans fiche servie au portier (appel « réponse sans fiche », § 2.4, b)** : la lettre n'en fixe pas la forme.
  Proposition du développeur, déclarée ici, à fixer à l'additif : la même forme, titre `## La réponse`, objet
  `{"reponse": texte}` (une chaîne JSON : une fin de ligne ou une clôture de bloc du texte y restent échappées, sur une
  ligne).
- **Arrêt n° 8 (mesure de la taille).** La taille est celle des octets de la requête entière, registre compris ; la borne
  est une valeur de l'additif, donnée en argument ; au-dessus : arrêt nommé, dont le message ne dit que la sorte, la
  taille et la borne.
- Aucun message d'erreur ne recopie un octet d'une pièce, d'une fiche, d'une réponse ou du registre.

Bibliothèque standard, et les modules des lots 1 et 2 (`tirage_na_v3`, `identifiants_na_v1`).
"""

import dataclasses
import hashlib
import json
import os

from pole import identifiants_na_v1 as ident
from pole import tirage_na_v3 as tn

VERSION = "requete-na-v2"

EMPLACEMENT = b"{{CASE}}"
FIN_DE_LIGNE = b"\n"
SEPARATEUR = b"\n"  # « une ligne vide » après une pièce finie par une fin de ligne (conception v5, § 5.3)
EMPREINTE_GABARIT = tn.EMPREINTE_GABARIT
NOMS_QUESTION = tn.NOMS_INTERDITS
EMPREINTES_QUESTION = tn.EMPREINTES_INTERDITES

# Forme de la fiche servie au portier et aux juges : celle du noyau (`fiches_v54.py`, l. 57 à 59), déclarée (mot 8).
TITRE_FICHE = "## La fiche"
OUVERTURE_BLOC = "```json"
FERMETURE_BLOC = "```"
INDENTATION_JSON = 1
CLE_IDENTIFIANT_JUGE = "identifiant"
OCTETS_IDENTIFIANT_JUGE = 5
# Réponse sans fiche servie au portier : proposition du développeur (la lettre ne la fixe pas).
TITRE_REPONSE = "## La réponse"
CLE_REPONSE = "reponse"

# Les douze champs d'une fiche (partie servie, l. 19), `case` en tête.
CHAMPS_FICHE = ("case", "ce_que_le_moniteur_suppose", "menace_du_programme", "etage_de_lecture", "idee",
                "mesurable_sur_monde_plante", "ce_qui_la_refuterait", "issue_contraire", "voisin_le_plus_proche_connu",
                "ecart_au_voisin", "filiation", "piece_produite")

SORTES = ("proposeur", "sonde_refus", "portier_fiche", "portier_reponse_sans_fiche", "juge")
REGISTRE_SERVI, REGISTRE_OMIS, REGISTRE_SANS_OBJET = "servi", "omis (registre vide)", "sans objet"
NUMERO_ARRET_TAILLE = 8
NUMERO_ARRET_EMPREINTE = 14


class RequeteRefusee(ValueError):
    """Une requête qui ne s'assemble pas : refusée, jamais réparée ; le message ne recopie aucun contenu."""


class QuestionRefusee(RequeteRefusee):
    """Le fichier de la question n'est jamais ouvert ni servi : seul le gabarit de la partie servie l'est (V9, l. 71)."""


class EmplacementRefuse(RequeteRefusee):
    """Le gabarit doit porter un seul emplacement, sur une ligne propre (V9, l. 71)."""


class EmpreintePieceDifferente(RequeteRefusee):
    """Arrêt n° 14 pour une pièce servie : son empreinte diffère de celle qui est écrite ; le refus nomme la pièce."""

    numero = NUMERO_ARRET_EMPREINTE

    def __init__(self, piece):
        super().__init__(f"arrêt n° {NUMERO_ARRET_EMPREINTE} : empreinte de la pièce « {piece} » différente de celle qui "
                         "est écrite ; refus")
        self.piece = piece


class ArretConsigneTropLongue(RuntimeError):
    """Arrêt n° 8 : la consigne, registre compris, est plus longue que sa borne (V9, l. 379) ; départ refusé."""

    numero = NUMERO_ARRET_TAILLE

    def __init__(self, sorte, taille, borne):
        super().__init__(f"arrêt n° {NUMERO_ARRET_TAILLE}, consigne plus longue que sa borne : sorte « {sorte} », "
                         f"{taille} octets pour une borne de {borne} ; départ refusé")
        self.sorte = sorte
        self.taille = taille
        self.borne = borne


def _sha256(octets):
    return hashlib.sha256(octets).hexdigest()


# --- pièces ------------------------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Piece:
    """Une pièce servie, lue à son empreinte, tous ses octets gardés (le dernier compris)."""

    nom: str
    octets: bytes
    sha256: str
    taille: int

    def __post_init__(self):
        if type(self.octets) is not bytes:
            raise TypeError("une pièce porte des octets figés")
        if _sha256(self.octets) != self.sha256 or len(self.octets) != self.taille:
            raise RequeteRefusee(f"pièce « {self.nom} » : empreinte ou taille qui ne sont pas les siennes")


def charger_piece(nom, octets, empreinte_attendue):
    """Une pièce à son empreinte (arrêt n° 14 : un écart refuse, en nommant la pièce)."""
    if type(nom) is not str or not nom:
        raise RequeteRefusee("une pièce a un nom")
    if not isinstance(octets, (bytes, bytearray)):
        raise RequeteRefusee(f"pièce « {nom} » : elle se lit en octets")
    octets = bytes(octets)
    sha = _sha256(octets)
    if type(empreinte_attendue) is not str or sha != empreinte_attendue:
        raise EmpreintePieceDifferente(nom)
    return Piece(nom, octets, sha, len(octets))


def _refuser_nom_de_question(chemin_ou_nom):
    if chemin_ou_nom is not None and any(n in os.path.basename(str(chemin_ou_nom)) for n in NOMS_QUESTION):
        raise QuestionRefusee("le fichier de la question n'est jamais lu : seul le gabarit de la partie servie l'est")


def lire_piece(nom, chemin, empreinte_attendue):
    """Lit une pièce sur le disque : le nom de la question est refusé avant toute ouverture."""
    _refuser_nom_de_question(chemin)
    with open(chemin, "rb") as f:
        octets = f.read()
    if _sha256(octets) in EMPREINTES_QUESTION:
        raise QuestionRefusee("empreinte de la question : refusée")
    return charger_piece(nom, octets, empreinte_attendue)


def _verifier_emplacement(octets):
    n = octets.count(EMPLACEMENT)
    if n != 1:
        raise EmplacementRefuse(f"le gabarit porte {n} emplacement(s) : un seul est permis")
    i = octets.index(EMPLACEMENT)
    j = i + len(EMPLACEMENT)
    if not (i == 0 or octets[i - 1:i] == FIN_DE_LIGNE) or not (j == len(octets) or octets[j:j + 1] == FIN_DE_LIGNE):
        raise EmplacementRefuse("l'emplacement doit être seul sur sa ligne")


def charger_gabarit(octets, empreinte_attendue=EMPREINTE_GABARIT, nom_fichier=None):
    """Le gabarit de la partie servie, à son empreinte ; la question est refusée par son nom puis par son empreinte ; un seul
    emplacement, sur une ligne propre."""
    _refuser_nom_de_question(nom_fichier)
    if not isinstance(octets, (bytes, bytearray)):
        raise RequeteRefusee("le gabarit se lit en octets")
    if _sha256(bytes(octets)) in EMPREINTES_QUESTION:
        raise QuestionRefusee("empreinte de la question : seul le gabarit de la partie servie est lu")
    piece = charger_piece("partie servie (gabarit)", octets, empreinte_attendue)
    _verifier_emplacement(piece.octets)
    return piece


def lire_gabarit(chemin, empreinte_attendue=EMPREINTE_GABARIT):
    """Lit le gabarit sur le disque : le nom de la question est refusé avant toute ouverture."""
    _refuser_nom_de_question(chemin)
    with open(chemin, "rb") as f:
        octets = f.read()
    return charger_gabarit(octets, empreinte_attendue, nom_fichier=chemin)


# --- cases et ligne de case --------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class CaseServie:
    """Une case du tirage scellé : son triplet, son identifiant (trois syllabes), sa ligne de case."""

    triplet: tuple
    identifiant: str
    ligne: str


def _case(entree):
    return CaseServie(tuple(entree["triplet"]), entree["identifiant"], entree["ligne"])


def _legende(gabarit):
    return tn.lire_legende(gabarit.octets, gabarit.sha256)


def cases_du_tirage(sortie, gabarit):
    """Les trente-trois cases servies et la première de la réserve, lues dans la sortie du tirage (lot 1), après trois
    contrôles : le tirage a été joué sur ce gabarit ; sa légende est celle du gabarit ; ses trente-quatre lignes passent le
    contrôle du lot 1 (valeurs à l'octet, identifiants distincts, ni chiffre ni suite hexadécimale, borne)."""
    if not isinstance(gabarit, Piece):
        raise RequeteRefusee("le gabarit est une pièce lue par `charger_gabarit`")
    if sortie.get("gabarit_sha256") != gabarit.sha256:
        raise RequeteRefusee("tirage joué sur un autre gabarit : refusé")
    legende = _legende(gabarit)
    if sortie.get("legende", {}).get("valeurs") != legende["valeurs"]:
        raise RequeteRefusee("légende du tirage différente de celle du gabarit : refusée")
    tn.controler_lignes_de_case(tn.lignes_du_tirage(sortie), legende)
    rendu = {str(g): tuple(_case(c) for c in sortie["generations"][str(g)]) for g in (1, 2, 3)}
    rendu["reserve"] = _case(sortie["reserve"]["premiere"])
    return rendu


def remplir_partie_servie(gabarit, case):
    """La partie servie remplie : l'emplacement remplacé par la ligne de case, encodée une fois en UTF-8 ; tout le reste à
    l'octet, le dernier octet compris. La ligne est contrôlée par le lot 1 et rebâtie de l'identifiant et du triplet."""
    if not isinstance(gabarit, Piece):
        raise RequeteRefusee("le gabarit est une pièce lue par `charger_gabarit`")
    if not isinstance(case, CaseServie):
        raise RequeteRefusee("la case est une case du tirage (`cases_du_tirage`)")
    _verifier_emplacement(gabarit.octets)
    legende = _legende(gabarit)
    tn.controler_ligne_de_case(1, case.triplet, case.ligne, legende)
    if tn.ligne_de_case(case.identifiant, case.triplet, legende) != case.ligne:
        raise RequeteRefusee("ligne de case qui n'est pas celle de son identifiant et de son triplet")
    octets_ligne = case.ligne.encode("utf-8")
    rempli = gabarit.octets.replace(EMPLACEMENT, octets_ligne, 1)
    if EMPLACEMENT in rempli:
        raise EmplacementRefuse("un emplacement reste après le remplissage")
    return Piece("partie servie remplie", rempli, _sha256(rempli), len(rempli))


# --- composition et requête --------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Element:
    """Un morceau de la requête : sa place, sa taille, l'empreinte des octets servis ; pour une pièce, l'empreinte et la
    taille de la pièce entière (égales pour une pièce servie entière ; la consigne du portier et des juges perd sa fin
    dans la forme déclarée)."""

    nom: str
    sorte: str  # "piece", "piece mise en forme", "separateur", "titre", "forme", "fiche servie", "reponse servie"
    debut: int
    taille: int
    sha256: str
    piece_sha256: object = None
    piece_taille: object = None

    def en_ligne(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass(frozen=True)
class RequeteAssemblee:
    """La requête d'un appel : ses octets figés, leur empreinte et leur taille, sa composition, sa sorte, sa génération,
    l'identifiant de sa case. La composition recouvre les octets exactement, morceau par morceau."""

    sorte: str
    generation: object
    identifiant_case: str
    octets: bytes
    sha256: str
    taille: int
    composition: tuple
    registre: str
    sources: tuple = ()

    def __post_init__(self):
        if type(self.octets) is not bytes:
            raise TypeError("une requête porte des octets figés")
        if self.sorte not in SORTES:
            raise RequeteRefusee("sorte de requête inconnue")
        try:
            self.octets.decode("utf-8")
        except UnicodeDecodeError:
            raise RequeteRefusee("requête qui n'est pas en UTF-8 valide") from None
        if _sha256(self.octets) != self.sha256 or len(self.octets) != self.taille:
            raise RequeteRefusee("empreinte ou taille qui ne sont pas celles des octets")
        position = 0
        for e in self.composition:
            if not isinstance(e, Element) or e.debut != position:
                raise RequeteRefusee("composition qui ne recouvre pas la requête morceau par morceau")
            morceau = self.octets[e.debut:e.debut + e.taille]
            if len(morceau) != e.taille or _sha256(morceau) != e.sha256:
                raise RequeteRefusee(f"composition : le morceau « {e.nom} » n'a pas son empreinte")
            if e.sorte == "piece" and (e.piece_sha256 != e.sha256 or e.piece_taille != e.taille):
                raise RequeteRefusee(f"composition : la pièce « {e.nom} » n'est pas servie entière")
            if e.sorte == "separateur" and morceau != SEPARATEUR:
                raise RequeteRefusee("composition : séparateur hors de l'enveloppe déclarée")
            position += e.taille
        if position != self.taille:
            raise RequeteRefusee("composition qui ne recouvre pas la requête morceau par morceau")

    def composition_en_lignes(self):
        return [e.en_ligne() for e in self.composition]


class _Assembleur:
    def __init__(self):
        self.morceaux = []
        self.elements = []
        self.position = 0

    def ajouter(self, nom, sorte, octets, piece=None):
        octets = bytes(octets)
        self.elements.append(Element(nom, sorte, self.position, len(octets), _sha256(octets),
                                     piece.sha256 if piece is not None else None,
                                     piece.taille if piece is not None else None))
        self.morceaux.append(octets)
        self.position += len(octets)

    def rendre(self, sorte, generation, identifiant_case, registre, sources=()):
        octets = b"".join(self.morceaux)
        return RequeteAssemblee(sorte, generation, identifiant_case, octets, _sha256(octets), len(octets),
                                tuple(self.elements), registre, tuple(sources))


def _verifier_generation(generation, exigee):
    if generation is None and not exigee:
        return None
    if type(generation) is not int or generation not in (1, 2, 3):
        raise RequeteRefusee("génération hors de 1 à 3")
    return generation


def _verifier_identifiant_case(identifiant):
    try:
        ident.rang_du_mot_de_case(identifiant)
    except ident.MotRefuse:
        raise RequeteRefusee("identifiant de case qui n'est pas un mot de trois syllabes") from None
    return identifiant


def _verifier_titre(titre):
    if type(titre) is not str or not titre or titre != titre.strip() or "\n" in titre or "\r" in titre:
        raise RequeteRefusee("titre de la section du registre : une ligne, non vide")
    return titre.encode("utf-8")


def assembler_proposeur(gabarit, case, synthese, generation, registre=None, titre_registre=None):
    """La requête d'un proposeur (V9, l. 62, 77 ; conception v5, § 5.3) : partie servie remplie ; une ligne vide ; synthèse
    servie à l'octet ; aux générations 2 et 3, une ligne vide, le titre de la section du registre, une fin de ligne, le
    registre servi. Un registre vide (zéro octet) : la section est omise, la requête est celle d'une génération 1, et la
    requête le dit (`registre`)."""
    generation = _verifier_generation(generation, exigee=True)
    if not isinstance(synthese, Piece):
        raise RequeteRefusee("la synthèse servie est une pièce lue à son empreinte")
    partie = remplir_partie_servie(gabarit, case)
    a = _Assembleur()
    a.ajouter("partie servie remplie", "piece", partie.octets, partie)
    a.ajouter("séparateur", "separateur", SEPARATEUR)
    a.ajouter("synthèse servie", "piece", synthese.octets, synthese)
    if generation == 1:
        if registre is not None or titre_registre is not None:
            raise RequeteRefusee("génération 1 : aucun registre n'est servi")
        etat = REGISTRE_SANS_OBJET
    else:
        if not isinstance(registre, Piece):
            raise RequeteRefusee("générations 2 et 3 : le registre servi est une pièce lue à son empreinte")
        if registre.taille == 0:
            if titre_registre is not None:
                _verifier_titre(titre_registre)
            etat = REGISTRE_OMIS
        else:
            titre = _verifier_titre(titre_registre)
            a.ajouter("séparateur", "separateur", SEPARATEUR)
            a.ajouter("titre de la section du registre", "titre", titre + FIN_DE_LIGNE)
            a.ajouter("registre servi", "piece", registre.octets, registre)
            etat = REGISTRE_SERVI
    sources = (("gabarit", gabarit.sha256), ("ligne de case", _sha256(case.ligne.encode("utf-8"))))
    return a.rendre("proposeur", generation, case.identifiant, etat, sources)


def assembler_sonde_refus(gabarit, case):
    """La requête d'une sonde de refus : la partie servie remplie, seule (V9, l. 77)."""
    partie = remplir_partie_servie(gabarit, case)
    a = _Assembleur()
    a.ajouter("partie servie remplie", "piece", partie.octets, partie)
    sources = (("gabarit", gabarit.sha256), ("ligne de case", _sha256(case.ligne.encode("utf-8"))))
    return a.rendre("sonde_refus", None, case.identifiant, REGISTRE_SANS_OBJET, sources)


def _texte_consigne(consigne):
    if not isinstance(consigne, Piece):
        raise RequeteRefusee("la consigne est une pièce lue à son empreinte")
    try:
        return consigne.octets.decode("utf-8")
    except UnicodeDecodeError:
        raise RequeteRefusee(f"consigne « {consigne.nom} » qui n'est pas en UTF-8 valide") from None


def _verifier_contenu(contenu):
    if not isinstance(contenu, dict) or set(contenu) != set(CHAMPS_FICHE) or len(contenu) != len(CHAMPS_FICHE):
        raise RequeteRefusee("la fiche servie porte exactement les douze champs du contrat")
    if any(type(v) is not str for v in contenu.values()):
        raise RequeteRefusee("chaque champ de la fiche servie est une chaîne")
    return dict(contenu)


def _assembler_forme(sorte, consigne, titre, objet, nom_corps, sorte_corps, generation, identifiant_case):
    """La forme du noyau, sur le texte décodé de la consigne ; un seul encodage de la chaîne entière."""
    texte = _texte_consigne(consigne)
    servie = texte.rstrip()
    ouverture = "\n\n" + titre + "\n" + OUVERTURE_BLOC + "\n"
    corps = json.dumps(objet, ensure_ascii=False, indent=INDENTATION_JSON)
    fermeture = "\n" + FERMETURE_BLOC + "\n"
    parts = ((consigne.nom, "piece mise en forme", servie, consigne), ("ouverture de la forme", "forme", ouverture, None),
             (nom_corps, sorte_corps, corps, None), ("fermeture de la forme", "forme", fermeture, None))
    octets = "".join(p[2] for p in parts).encode("utf-8")  # un seul encodage
    elements, position = [], 0
    for nom, sorte_e, chaine, piece in parts:
        n = len(chaine.encode("utf-8"))  # longueur seule, pour la place du morceau
        morceau = octets[position:position + n]
        elements.append(Element(nom, sorte_e, position, n, _sha256(morceau),
                                piece.sha256 if piece is not None else None, piece.taille if piece is not None else None))
        position += n
    return RequeteAssemblee(sorte, generation, identifiant_case, octets, _sha256(octets), len(octets), tuple(elements),
                            REGISTRE_SANS_OBJET, (("consigne", consigne.sha256),))


def assembler_portier_fiche(consigne, contenu, identifiant_case, generation=None):
    """Appel « fiche » du portier : sa consigne fixe, puis la fiche dans la forme du noyau, déclarée (mot 8)."""
    generation = _verifier_generation(generation, exigee=False)
    _verifier_identifiant_case(identifiant_case)
    return _assembler_forme("portier_fiche", consigne, TITRE_FICHE, _verifier_contenu(contenu), "fiche servie",
                            "fiche servie", generation, identifiant_case)


def assembler_juge(consigne, contenu, identifiant_servi, identifiant_case, generation=None):
    """Appel d'un juge : sa consigne fixe, puis la fiche dans la même forme, l'identifiant servi réencodé (quatorze lettres,
    § 5.2) en dernière clé ; un identifiant du noyau, ou de toute autre forme, est refusé."""
    generation = _verifier_generation(generation, exigee=False)
    _verifier_identifiant_case(identifiant_case)
    try:
        ident.decoder_octets(identifiant_servi, OCTETS_IDENTIFIANT_JUGE)
    except ident.MotRefuse:
        raise RequeteRefusee("identifiant servi au juge qui n'est pas un mot réencodé de quatorze lettres") from None
    objet = _verifier_contenu(contenu)
    objet[CLE_IDENTIFIANT_JUGE] = identifiant_servi
    return _assembler_forme("juge", consigne, TITRE_FICHE, objet, "fiche servie", "fiche servie", generation,
                            identifiant_case)


def assembler_portier_reponse_sans_fiche(consigne, texte_reponse, identifiant_case, generation=None):
    """Appel « réponse sans fiche » du portier : sa consigne, puis le texte de la réponse, dans la forme proposée par le
    développeur (la lettre ne la fixe pas)."""
    generation = _verifier_generation(generation, exigee=False)
    _verifier_identifiant_case(identifiant_case)
    if type(texte_reponse) is not str:
        raise RequeteRefusee("le texte d'une réponse est une chaîne")
    return _assembler_forme("portier_reponse_sans_fiche", consigne, TITRE_REPONSE, {CLE_REPONSE: texte_reponse},
                            "réponse servie", "reponse servie", generation, identifiant_case)


# --- arrêt n° 8 : mesure de la taille ----------------------------------------------------------------------------------

def mesurer(requete):
    """La taille en octets de la requête entière (registre compris), recomptée sur ses octets."""
    if not isinstance(requete, RequeteAssemblee):
        raise RequeteRefusee("seule une requête assemblée se mesure")
    return len(requete.octets)


def verifier_borne(requete, borne_octets):
    """Arrêt n° 8 (V9, l. 379) : au-dessus de la borne (valeur de l'additif), départ refusé ; égale, départ permis."""
    if type(borne_octets) is not int or borne_octets <= 0:
        raise RequeteRefusee("borne en octets : un entier positif")
    taille = mesurer(requete)
    if taille > borne_octets:
        raise ArretConsigneTropLongue(requete.sorte, taille, borne_octets)
    return taille


def tailles_par_sorte(requetes):
    """Pour la mesure des consignes sans appel (lot 9) : par sorte, le nombre de requêtes et la plus grande taille."""
    rendu = {}
    for r in requetes:
        n = mesurer(r)
        d = rendu.setdefault(r.sorte, {"requetes": 0, "plus_grande_taille": 0})
        d["requetes"] += 1
        d["plus_grande_taille"] = max(d["plus_grande_taille"], n)
    return rendu


def chaine_pour_le_noyau(octets):
    """La chaîne que reçoit `appel` du noyau, qui prend une chaîne : le décodage strict des octets gardés ; son encodage
    UTF-8 rend les mêmes octets, sinon refus."""
    if type(octets) is not bytes:
        raise RequeteRefusee("des octets figés")
    chaine = octets.decode("utf-8")
    if chaine.encode("utf-8") != octets:
        raise RequeteRefusee("la chaîne ne rend pas les octets gardés")
    return chaine
