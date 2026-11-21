"""Aides des essais du lot 5 du véhicule NA-1 (lecteur, contrat, portier, registres) : données factices seules.

**Brouillon d'essai factice, déclaré comme tel** (mandat du lot 5 ; conception v5, § 7) : la consigne du portier (D3), la
déclaration de ses étiquettes et les bornes en octets des douze champs ne sont pas écrites à ce jour ; celles d'ici sont
inertes, au format que la conception permet, et ne valent rien pour la course. Le gabarit, la synthèse, la racine, la
liste de motifs d'essai et la consigne factice du portier sont ceux des lots 1 à 3 (`aides_na_v4`, `aides_na_lot3_v3`).
Aucune pièce réelle n'est lue ; le registre servi réel n'est pas ouvert.
"""

import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot3_v3 as A3  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import contrat_fiche_na_v1 as ct  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import portier_na_v1 as pt  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402
from pole import tirage_na_v4 as tn  # noqa: E402

STATUT_BROUILLON = "brouillon d'essai factice, déclaré comme tel ; la consigne de D3 et les bornes ne sont pas écrites"

DECLARATION_ESSAI = pt.declaration_de(
    forme=pt.FORME_LIGNE_ANCREE, cle="étiquette",
    fiche={pt.NIVEAU_IDEE: "niveau de l'idée", pt.CONCRET: "concret"},
    reponse_sans_fiche={pt.VIDE_MOTIVEE: "réponse vide motivée", pt.REFUS_DU_MODELE: "refus du modèle",
                        pt.ILLISIBLE: "réponse illisible"},
    statut=STATUT_BROUILLON)

BORNES_DICT = {c: 300 for c in rq.CHAMPS_FICHE}
BORNES_DICT["idee"] = 1200
BORNES_ESSAI = ct.bornes_de(BORNES_DICT, STATUT_BROUILLON)

# Une valeur de légende factice que le caviardage du noyau changerait (témoin : « lu tel que rendu »).
VALEUR_CAVIARDABLE = "trait jeton : factice-motlong"
GABARIT_CAVIARDABLE = A.GABARIT_FACTICE.replace("trait factice deux".encode("utf-8"), VALEUR_CAVIARDABLE.encode("utf-8"))


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def legende(gabarit=A.GABARIT_FACTICE):
    return tn.lire_legende(gabarit, sha(gabarit))


def case_de(triplet, rang_mot, gabarit=A.GABARIT_FACTICE):
    """Une case factice : son triplet, un mot de trois syllabes, sa ligne de case bâtie par le lot 1."""
    mot = ident.mot_de_case(rang_mot)
    return rq.CaseServie(tuple(triplet), mot, tn.ligne_de_case(mot, tuple(triplet), legende(gabarit)))


CASE = case_de((1, 0, 2), 1234)
CASE_AUTRE = case_de((5, 3, 1), 4321)  # premier axe : « autre, à nommer »


def mot_fiche(n):
    """Un identifiant de fiche réencodé (six octets factices, dix-huit lettres)."""
    return ident.encoder_identifiant_fiche(int(n).to_bytes(6, "big"))


def contenu(case=CASE, gabarit=A.GABARIT_FACTICE, **remplace):
    """Une fiche factice, inerte, aux douze champs ; champs fermés égaux à ceux de la case."""
    vals = [legende(gabarit)["valeurs"][a][case.triplet[a]] for a in range(3)]
    c = {
        "case": case.identifiant,
        "ce_que_le_moniteur_suppose": vals[0],
        "menace_du_programme": vals[1],
        "etage_de_lecture": vals[2],
        "idee": "Idée factice, inerte, sur deux lignes.\nSeconde ligne factice.",
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


def en_lignes(c, ordre=None, parure="{n} : {v}", extras=()):
    """La fiche en étiquettes ancrées : une parure par ligne (`{n}` le nom, `{v}` la valeur), un ordre au choix."""
    noms = list(ordre or c.keys())
    lignes = [parure.format(n=n, v=c[n]) for n in noms]
    lignes += [parure.format(n=n, v=v) for n, v in extras]
    return "\n".join(lignes)


def en_json(c, cloture=True):
    corps = json.dumps(c, ensure_ascii=False, indent=2)
    return f"```json\n{corps}\n```" if cloture else corps


def consigne():
    return A3.consigne_portier()


_GARDE = []


def garde():
    """La garde de motifs d'essai du lot 2, construite une fois par processus (ses témoins positifs rejoués alors)."""
    if not _GARDE:
        _GARDE.append(A.garde_essai())
    return _GARDE[0]


class AppelFactice:
    """La fonction `appeler(requete, lire)` d'essai : la requête du portier passe la garde de motifs d'essai et le journal
    du lot 3 (ligne « envoi »), puis une issue est rendue, prise dans une file : un texte du modèle portier (inerte),
    `None` (non lancé), un refus écrit, ou un résultat du noyau sans lecture (`{"lu": None}`)."""

    def __init__(self, dossier, issues, nom="journal-requetes-essai.jsonl"):
        self.file = list(issues)
        self.requetes = []
        self.journal = jn.JournalRequetes(dossier, nom)
        self.garde = garde()

    def __call__(self, requete, lire):
        self.requetes.append(requete)
        envoi = self.journal.journaliser_envoi(requete, self.garde, role="aiguilleur", cle="clé d'essai")
        envoi.chaine_pour_le_noyau()
        issue = self.file.pop(0)
        if issue is None or isinstance(issue, jn.RenduRefusEcrit) or isinstance(issue, dict):
            return issue
        if issue == "refus écrit":
            return self.journal.journaliser_refus_ecrit(sorte=requete.sorte, role="aiguilleur",
                                                        generation=requete.generation, case=requete.identifiant_case,
                                                        garde="garde d'essai", cause="rôle marqué arrêté par l'essai")
        return {"r": None, "lu": lire(issue), "motif": None, "duree": 0.0}


def etiquette(texte):
    return f"Texte factice du portier, inerte.\nétiquette : {texte}\n"


def portier(dossier, issues, generation=1, nom="journal-portier-essai.jsonl", **kw):
    appel = AppelFactice(dossier, issues)
    p = pt.PortierNA(consigne=consigne(), declaration=kw.pop("declaration", DECLARATION_ESSAI),
                     bornes=kw.pop("bornes", BORNES_ESSAI), appeler=appel, dossier_sortie=dossier, nom_journal=nom,
                     generation=generation)
    return p, appel
