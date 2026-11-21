"""Véhicule NA-1, lot 3 — journal des requêtes (`journal_na_v2`) : ajout seul ; lignes « envoi », « non envoyé »,
« non lancé » et « refus écrit » ; ce que rend un refus écrit, par rôle.

v2 (remplace `journal_na_v1`, `84240623…`, archivé sans modification) : des noms seuls changent, pour la v3 du lot 2 ; le
module lit `garde_motifs_na_v3` et `requete_na_v2` au lieu de `garde_motifs_na_v2` et `requete_na_v1`. Les classes de la
garde (`GardeMotifs`, `RequeteGardee`, `ArretMotifInterdit`) sont donc celles de la v3. Aucune règle ne change.

Lettre : V9 (`864f39a7…`), l. 77 (journal avant chaque envoi, après la garde de motifs ; un appel sans ligne ne part pas ;
le journal n'est jamais servi), l. 387 (le texte trouvé n'est écrit qu'au journal) ; conception du véhicule v5
(`1b7f6822…`), § 2.3 (pas 3 à 5, pas 7 ; le refus avant le noyau), § 2.7 (journal), § 2.13 (ce que rend un refus écrit),
§ 6.2 (requête journalisée ; envoi refusé sans coût), § 7 (lot 3) ; vérification des lots 1 et 2 (`674996b4…`), § 5,
points 3 et 5.

- **Ajout seul.** Le fichier est créé neuf dans le dossier de sortie (un fichier existant est refusé, R12) ; on n'y écrit
  qu'en ajout. Avant chaque ajout, le fichier est relu et comparé à la taille et à l'empreinte de ce que le journal y a
  écrit : un octet changé, retiré ou ajouté d'une autre main, et l'écriture est refusée. Chaque ligne porte son rang et
  l'empreinte de la ligne qui la précède. Le journal se scelle (compagnon `.sha256`) ; scellé, il refuse tout ajout.
- **Ligne « envoi »** (`journaliser_envoi`) : la garde de motifs lit les octets de la requête assemblée (lot 2) ; puis,
  et seulement si elle passe, une ligne : taille, empreinte SHA-256, génération, rôle, sorte, identifiant de la case, clé
  par son nom d'usage, composition (pièces, places, tailles, empreintes ; aucun contenu). Ce qui est rendu au lot 4 :
  la requête gardée (`RequeteGardee` du lot 2) et ses octets, les seuls à remettre au noyau ; le lot 4 appelle
  `garde_motifs_na_v3.verifier_avant_envoi(requete_gardee, octets)` sur les octets qu'il remet. Une ligne qui ne
  s'écrit pas : rien n'est rendu, rien ne part.
- **Ligne « non envoyé »** : refus avant le noyau, coût nul, le numéro de l'arrêt, la clé. Pour l'arrêt n° 16, la
  famille, le rang du motif et le texte trouvé : **le texte trouvé ne va qu'à cette ligne**, dans le dossier de sortie ;
  ni le message de l'arrêt, ni ses `args`, ni son `repr` ne le portent (lot 2).
- **Ligne « non lancé »** : après la ligne « envoi » d'un appel que le noyau n'a pas lancé (coupure au plafond dur) ;
  elle renvoie au rang et à l'empreinte de cette ligne.
- **Ligne « refus écrit »** (§ 2.13) : la garde héritée, sa cause, le rôle, la génération, la case ; coût nul ; et ce que
  le refus rend à l'appelant, selon la sorte du rôle (`RENDUS_REFUS_ECRIT`).
- Aucun message d'erreur de ce module ne recopie un octet d'une requête, d'une fiche ou d'une réponse.

Bibliothèque standard, et les modules des lots 2 et 3 (`garde_motifs_na_v3`, `requete_na_v2`).
"""

import dataclasses
import hashlib
import itertools
import json
import os

from pole import garde_motifs_na_v3 as gm
from pole import requete_na_v2 as rq

VERSION = "journal-na-v2"
EVENEMENTS = ("envoi", "non envoyé", "non lancé", "refus écrit")
PRECEDENTE_INITIALE = "aucune"
SUFFIXE = ".jsonl"
CAUSE_NON_LANCE = "coupure au plafond dur de l'étape"
_NUMEROS_DE_JOURNAL = itertools.count(1)

# Champs permis en plus sur une ligne « non envoyé » (liste fermée ; « rang_motif » ne se confond pas avec le rang de
# la ligne).
DETAILS_NON_ENVOYE = ("famille", "rang_motif", "texte_trouve", "cause", "clause", "sha256", "taille", "sorte")

# Ce que rend un refus écrit, par sorte de rôle (conception v5, § 2.13 ; mère, 07:51Z).
RENDUS_REFUS_ECRIT = {
    "proposeur": {
        "rendu": "rien", "effet": "case non jouée pour cette espèce", "classe": None,
        "compte": "cases non jouées", "fiche_rendue": False, "appel_compte_m6": False},
    "portier_fiche": {
        "rendu": "fiche au coffre", "effet": "la fiche va au coffre, avec sa classe écrite", "classe": "au coffre",
        "compte": "au coffre par refus du portier", "fiche_rendue": True, "appel_compte_m6": False},
    "portier_reponse_sans_fiche": {
        "rendu": "réponse classée", "effet": "la réponse est classée « réponse illisible »",
        "classe": "réponse illisible", "compte": "étiquette du portier illisible", "fiche_rendue": False,
        "appel_compte_m6": True},
    "juge": {
        "rendu": "verdict absent", "effet": "la fiche reste « passée »", "classe": "passée",
        "compte": "verdicts absents", "fiche_rendue": False, "appel_compte_m6": False},
}


class JournalRefuse(RuntimeError):
    """Une écriture ou une lecture du journal refusée ; le message ne recopie aucun contenu."""


class JournalReecrit(JournalRefuse):
    """Le fichier ne porte plus exactement ce que le journal y a écrit : toute écriture est refusée."""


class JournalScelle(JournalRefuse):
    """Le journal est scellé : plus aucun ajout."""


class LigneRefusee(JournalRefuse):
    """Une ligne qui ne tient pas sa forme : rien n'est écrit."""


class EcartGardeRequete(JournalRefuse):
    """La garde n'a pas lu les octets de la requête assemblée : rien n'est écrit, rien ne part."""


class RejeuDifferent(JournalRefuse):
    """La requête rejouée n'a pas l'empreinte ou la taille de sa ligne de journal."""


def _sha256(octets):
    return hashlib.sha256(octets).hexdigest()


def _octets_de_ligne(ligne):
    return (json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


@dataclasses.dataclass(frozen=True)
class EnvoiJournalise:
    """Ce que rend `journaliser_envoi` au lot 4 : la requête gardée (ses octets, les seuls à envoyer, leur empreinte et leur
    taille, ceux que décrit la ligne) et le rang de la ligne « envoi »."""

    requete_gardee: gm.RequeteGardee
    rang: int
    sorte: str
    role: str
    cle: str
    generation: object
    identifiant_case: str
    journal_id: int

    @property
    def octets(self):
        return self.requete_gardee.octets

    def chaine_pour_le_noyau(self):
        """La chaîne à remettre à `appel` du noyau : son encodage UTF-8 est comparé à la requête gardée
        (`verifier_avant_envoi`), sinon refus."""
        chaine = rq.chaine_pour_le_noyau(self.requete_gardee.octets)
        gm.verifier_avant_envoi(self.requete_gardee, chaine.encode("utf-8"))
        return chaine


@dataclasses.dataclass(frozen=True)
class RenduRefusEcrit:
    """Ce qu'un refus écrit rend à l'appelant (§ 2.13), avec le rang de sa ligne."""

    sorte: str
    rendu: str
    effet: str
    classe: object
    compte: str
    fiche_rendue: bool
    appel_compte_m6: bool
    rang: int


def _texte(nom, valeur, vide_permis=False):
    if type(valeur) is not str or (not valeur and not vide_permis):
        raise LigneRefusee(f"champ « {nom} » : une chaîne non vide")
    return valeur


def _generation(valeur):
    if valeur is None:
        return None
    if type(valeur) is not int or valeur not in (1, 2, 3):
        raise LigneRefusee("génération hors de 1 à 3")
    return valeur


def _arret(valeur):
    if (type(valeur) is int and valeur > 0) or (type(valeur) is str and valeur):
        return valeur
    raise LigneRefusee("arrêt : un numéro, ou le nom que l'additif lui donne")


class JournalRequetes:
    """Le journal des requêtes d'une génération (ou d'une ligne à part), dans le dossier de sortie, en ajout seul."""

    def __init__(self, dossier_sortie, nom_fichier):
        if type(nom_fichier) is not str or os.path.basename(nom_fichier) != nom_fichier or nom_fichier in ("", ".", "..") \
                or not nom_fichier.endswith(SUFFIXE):
            raise JournalRefuse(f"nom de journal : un nom de fichier simple, fini par « {SUFFIXE} »")
        if not os.path.isdir(dossier_sortie):
            raise JournalRefuse("le journal s'écrit dans le dossier de sortie, qui doit exister")
        self.chemin = os.path.join(dossier_sortie, nom_fichier)
        if os.path.exists(self.chemin) or os.path.exists(self.chemin + ".sha256"):
            raise JournalRefuse("journal existant : on n'écrase jamais (R12)")
        with open(self.chemin, "xb"):
            pass
        self._taille = 0
        self._empreinte = _sha256(b"")
        self._precedente = PRECEDENTE_INITIALE
        self._rang = 0
        self._scelle = False
        self._envois = {}
        self._non_lances = set()
        self._numero = next(_NUMEROS_DE_JOURNAL)

    # --- ajout seul --------------------------------------------------------------------------------------------------

    def _verifier_intact(self):
        with open(self.chemin, "rb") as f:
            present = f.read()
        if len(present) != self._taille or _sha256(present) != self._empreinte:
            raise JournalReecrit("le journal ne porte plus ce qui y a été écrit : écriture refusée")
        return present

    def _ajouter(self, champs):
        if self._scelle:
            raise JournalScelle("journal scellé : aucun ajout")
        present = self._verifier_intact()
        ligne = dict(champs, rang=self._rang + 1, precedente=self._precedente, version=VERSION)
        octets = _octets_de_ligne(ligne)
        fd = os.open(self.chemin, os.O_WRONLY | os.O_APPEND)
        try:
            ecrits = os.write(fd, octets)
            os.fsync(fd)
        finally:
            os.close(fd)
        if ecrits != len(octets):
            self._scelle = True
            raise JournalRefuse("écriture incomplète : journal fermé")
        self._taille += len(octets)
        self._empreinte = _sha256(present + octets)
        self._precedente = _sha256(octets)
        self._rang += 1
        return ligne

    def sceller(self):
        """Écrit le compagnon `.sha256` (jamais par-dessus) ; le journal refuse ensuite tout ajout."""
        if self._scelle:
            raise JournalScelle("journal déjà scellé")
        self._verifier_intact()
        with open(self.chemin + ".sha256", "x", encoding="utf-8") as f:
            f.write(f"{self._empreinte}  {os.path.basename(self.chemin)}\n")
        self._scelle = True
        return self._empreinte

    @property
    def scelle(self):
        return self._scelle

    @property
    def rang(self):
        return self._rang

    # --- lignes ------------------------------------------------------------------------------------------------------

    def journaliser_envoi(self, requete, garde, *, role, cle):
        """Garde de motifs, puis ligne « envoi » ; rend la requête gardée. Refus de la garde : ligne « non envoyé »
        (arrêt n° 16, famille, rang du motif, texte trouvé), puis l'arrêt est levé, sans envoi."""
        if not isinstance(requete, rq.RequeteAssemblee):
            raise LigneRefusee("seule une requête assemblée par `requete_na_v2` se journalise")
        if not isinstance(garde, gm.GardeMotifs):
            raise LigneRefusee("la garde de motifs du lot 2 est exigée")
        _texte("rôle", role)
        _texte("clé", cle)
        try:
            rg = garde.garder_requete(requete.octets)
        except gm.ArretMotifInterdit as arret:
            self.journaliser_non_envoye(arret=gm.NUMERO_ARRET, role=role, generation=requete.generation,
                                        case=requete.identifiant_case, cle=cle, famille=arret.famille,
                                        rang_motif=arret.rang, texte_trouve=arret.texte_trouve, sorte=requete.sorte,
                                        sha256=requete.sha256, taille=requete.taille)
            raise
        if not isinstance(rg, gm.RequeteGardee) or rg.sha256 != requete.sha256 or rg.taille != requete.taille \
                or rg.octets != requete.octets:
            raise EcartGardeRequete("la garde n'a pas lu les octets de la requête : rien ne part")
        ligne = self._ajouter({
            "evenement": "envoi", "generation": requete.generation, "role": role, "sorte": requete.sorte,
            "case": requete.identifiant_case, "cle": cle, "taille": rg.taille, "sha256": rg.sha256,
            "registre": requete.registre, "composition": requete.composition_en_lignes(),
            "sources": [list(s) for s in requete.sources]})
        self._envois[ligne["rang"]] = rg.sha256
        return EnvoiJournalise(rg, ligne["rang"], requete.sorte, role, cle, requete.generation,
                               requete.identifiant_case, self._numero)

    def journaliser_non_envoye(self, *, arret, role, generation, case, cle, **details):
        """Refus avant le noyau : coût nul, numéro de l'arrêt, clé ; champs de plus pris dans une liste fermée."""
        inconnus = sorted(set(details) - set(DETAILS_NON_ENVOYE))
        if inconnus:
            raise LigneRefusee("champ de plus hors de la liste fermée d'une ligne « non envoyé »")
        return self._ajouter({"evenement": "non envoyé", "arret": _arret(arret), "role": _texte("rôle", role),
                              "generation": _generation(generation), "case": _texte("case", case, vide_permis=True),
                              "cle": _texte("clé", cle), "cout_usd": 0.0, **details})

    def journaliser_non_lance(self, envoi, cause=CAUSE_NON_LANCE):
        """Seconde ligne d'un appel journalisé que le noyau n'a pas lancé : elle renvoie à sa ligne « envoi »."""
        if not isinstance(envoi, EnvoiJournalise) or envoi.journal_id != self._numero \
                or self._envois.get(envoi.rang) != envoi.requete_gardee.sha256:
            raise LigneRefusee("« non lancé » renvoie à une ligne « envoi » de ce journal")
        if envoi.rang in self._non_lances:
            raise LigneRefusee("une seule ligne « non lancé » par envoi")
        ligne = self._ajouter({"evenement": "non lancé", "role": envoi.role, "sorte": envoi.sorte,
                               "generation": envoi.generation, "case": envoi.identifiant_case, "cle": envoi.cle,
                               "envoi_rang": envoi.rang, "envoi_sha256": envoi.requete_gardee.sha256,
                               "cause": _texte("cause", cause), "cout_usd": 0.0})
        self._non_lances.add(envoi.rang)
        return ligne

    def journaliser_refus_ecrit(self, *, sorte, role, generation, case, garde, cause):
        """Refus écrit d'une garde héritée (§ 2.13) : une ligne, coût nul ; rend ce que le refus rend à l'appelant."""
        if sorte not in RENDUS_REFUS_ECRIT:
            raise LigneRefusee("sorte de rôle inconnue pour un refus écrit")
        r = RENDUS_REFUS_ECRIT[sorte]
        ligne = self._ajouter({"evenement": "refus écrit", "sorte": sorte, "role": _texte("rôle", role),
                               "generation": _generation(generation), "case": _texte("case", case, vide_permis=True),
                               "garde": _texte("garde", garde), "cause": _texte("cause", cause), "cout_usd": 0.0,
                               "rendu": r["rendu"], "classe": r["classe"], "compte": r["compte"]})
        return RenduRefusEcrit(sorte, r["rendu"], r["effet"], r["classe"], r["compte"], r["fiche_rendue"],
                               r["appel_compte_m6"], ligne["rang"])


# --- lecture, rejeu et comptes -----------------------------------------------------------------------------------------

def verifier_journal(chemin, exiger_sceau=False):
    """Relit un journal : lignes lisibles, rangs 1, 2, 3… sans trou, chaque ligne liée à la précédente par son empreinte ;
    si le compagnon existe, il porte l'empreinte du fichier. Rend les lignes ; un écart : `JournalReecrit`. La dernière
    ligne n'est tenue que par le sceau : qui lit un journal clos (mesures, export) passe `exiger_sceau=True`."""
    with open(chemin, "rb") as f:
        octets = f.read()
    lignes, precedente = [], PRECEDENTE_INITIALE
    if octets and not octets.endswith(b"\n"):
        raise JournalReecrit("journal coupé au milieu d'une ligne")
    for i, brute in enumerate(octets.splitlines(keepends=True), start=1):
        try:
            ligne = json.loads(brute.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            raise JournalReecrit(f"ligne {i} illisible") from None
        if not isinstance(ligne, dict) or ligne.get("rang") != i or ligne.get("precedente") != precedente \
                or ligne.get("evenement") not in EVENEMENTS or _octets_de_ligne(ligne) != brute:
            raise JournalReecrit(f"ligne {i} : rang, chaînage ou forme rompus")
        precedente = _sha256(brute)
        lignes.append(ligne)
    compagnon = chemin + ".sha256"
    if exiger_sceau and not os.path.exists(compagnon):
        raise JournalReecrit("journal non scellé : sa dernière ligne n'est tenue par rien")
    if os.path.exists(compagnon):
        with open(compagnon, encoding="utf-8") as f:
            attendu = f.read().split()[0]
        if attendu != _sha256(octets):
            raise JournalReecrit("le compagnon ne porte pas l'empreinte du journal")
    return tuple(lignes)


def verifier_rejeu(ligne_envoi, requete):
    """La requête rejouée à partir des pièces scellées et de la ligne de case rend l'empreinte et la taille du journal
    (V9, l. 77) ; sinon refus."""
    if not isinstance(requete, rq.RequeteAssemblee) or not isinstance(ligne_envoi, dict) \
            or ligne_envoi.get("evenement") != "envoi":
        raise RejeuDifferent("le rejeu compare une requête assemblée à une ligne « envoi »")
    if (ligne_envoi.get("sha256"), ligne_envoi.get("taille")) != (requete.sha256, requete.taille) \
            or (ligne_envoi.get("sorte"), ligne_envoi.get("generation"), ligne_envoi.get("case")) \
            != (requete.sorte, requete.generation, requete.identifiant_case):
        raise RejeuDifferent("la requête rejouée n'est pas celle du journal")
    return True


def comptes(lignes):
    """Comptes par rôle (envois, appels non lancés), par rôle et par arrêt (refus « non envoyé »), par rôle et par garde
    (refus écrits), et par compte du § 2.13 ; pour la ligne de la génération (lot 6)."""
    rendu = {"envois": {}, "non_envoyes": {}, "non_lances": {}, "refus_ecrits": {}, "refus_ecrits_par_compte": {}}

    def plus(d, k):
        d[k] = d.get(k, 0) + 1

    for ligne in lignes:
        ev = ligne["evenement"]
        if ev == "envoi":
            plus(rendu["envois"], ligne["role"])
        elif ev == "non envoyé":
            plus(rendu["non_envoyes"].setdefault(ligne["role"], {}), str(ligne["arret"]))
        elif ev == "non lancé":
            plus(rendu["non_lances"], ligne["role"])
        elif ev == "refus écrit":
            plus(rendu["refus_ecrits"].setdefault(ligne["role"], {}), ligne["garde"])
            plus(rendu["refus_ecrits_par_compte"], ligne["compte"])
    return rendu
