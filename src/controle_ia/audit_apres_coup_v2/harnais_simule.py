"""Le harnais simulé des épreuves de la boucle (rang 11 ; section 5), mondes plantés seulement.

- **Jeton de provenance** : toute entrée porte un jeton « monde planté » émis par `graines.py` avec l'empreinte du
  fichier de vérité plantée ; sans lui (poids d'une sonde du programme, verdict d'un oracle réel, état d'un organisme),
  refus nommé « hors monde planté », y compris dans le mode « bras de flux » ; un contenu réel recopié sous un jeton
  valide est refusé aussi (re-dérivation depuis la graine).
- **Interdit entier par défaut** : toute entrée de lignée est refusée.
- **Mode « bras de flux » planté** (mot du directeur, GO-2026-11-22-57 : écrit, sur harnais simulé seulement) : il
  n'existe que comme configuration plantée, étiquetée « non en vigueur ». Un bras est déclaré par un texte scellé
  (simulé : une déclaration et son empreinte) avant son premier épisode ; ses organismes et ses familles sont disjoints
  de ceux de toute porte, de la famille tenue à l'écart et du jeu final. Une lignée n'admet qu'un épisode de flux d'un
  bras déclaré avant lui ; les cinq refus nommés de l'épreuve 1 (clause 1) ; les trois conditions de la clause 2
  (score consigné avant le verdict, version scellée avant de noter, jamais jugée sur sa lignée).
- **Enclave**, modélisée par des jetons de capacité (clause 5, épreuve 13) : les versions nées du flux, leurs poids,
  seuils et scores par épisode y restent ; un rôle de concepteur n'obtient que le compte d'un lot, à sa date fixée
  d'avance ; aucune reconception ne part d'une version née du flux.
- Rôles écrits avant le verdict ; versions nommées par empreinte, avec leur lignée ; registres en ajout seul
  (témoins, plis, regards).

Version 2 : la clause 1 refuse aussi l'organisme d'un épisode de verdict (I-1) ; la garde ne dépend plus de l'ordre
des appels (refus d'un épisode de verdict d'une famille ou d'un organisme déjà en lignée, revérification au
scellement : I-2) ; organismes de la famille tenue à l'écart et du jeu final déclarés (m-11) ; limite de l'enclave
écrite (m-5).

Les sondes de ces mondes sont des directions plantées instruites sur des étiquettes de la vérité plantée ; aucune sonde
du programme n'est touchée. Les gardes ne couvrent pas une modification du harnais lui-même.
"""
from __future__ import annotations

import secrets
from dataclasses import dataclass, field

import numpy as np

from ..gardes import GardeArret
from .graines import JetonProvenance, empreinte_octets, verifier_provenance

MODE_INTERDIT_ENTIER = "interdit entier"
MODE_BRAS_DE_FLUX = "bras de flux (planté)"
ETIQUETTE_NON_EN_VIGUEUR = "non en vigueur"
REFUS_LIGNEE = "interdit entier : toute entrée de lignée est refusée"
ROLES = ("verdict", "flux", "pli retenu", "hors rôle")
REFUS_PLI_CONSOMME = "pli consommé : il a servi à choisir, il ne porte plus d'annonce"
REFUS_TEMOINS = "témoins : un même témoin sert à instruire et à calibrer"

# Les cinq refus nommés de l'épreuve 1
REFUS_VERDICT = "lignée : épisode de verdict"
REFUS_MEME_FAMILLE = "lignée : épisode de la famille d'un épisode de verdict"
REFUS_HORS_ROLE = "lignée : épisode hors rôle"
REFUS_APRES_COUP = "lignée : bras déclaré « de flux » après son premier épisode"
REFUS_FAMILLE_PORTE = "lignée : famille d'une porte, de la famille tenue à l'écart ou du jeu final"
# Les deux refus nommés de l'épreuve 13
REFUS_VERSION_CLOSE = "versions closes : poids, seuils et scores par épisode d'une version née du flux restent dans l'enclave"
REFUS_RECONCEPTION = "versions closes : aucune reconception ne part d'une version née du flux"


@dataclass(frozen=True)
class DeclarationBrasDeFlux:
    """Texte scellé (simulé) qui déclare un bras de flux : nom, organismes, familles, heure de scellement."""

    nom: str
    organismes: frozenset
    familles: frozenset
    h_scellement: int
    etiquette: str = ETIQUETTE_NON_EN_VIGUEUR

    def empreinte(self) -> str:
        return empreinte_octets(repr((self.nom, sorted(self.organismes), sorted(self.familles),
                                      self.h_scellement, self.etiquette)).encode())


@dataclass
class EpisodeHarnais:
    episode: int
    role: str
    famille: str
    organisme: str
    bras: str | None
    h_role: int
    h_debut: int
    h_verdict: int | None = None
    scores: dict = field(default_factory=dict)  # version -> heure de consignation


@dataclass
class Version:
    nom: str
    lignee: tuple
    h_scellement: int
    nee_du_flux: bool
    contenu: bytes


class HarnaisSimule:
    def __init__(self, mode: str = MODE_INTERDIT_ENTIER, familles_portes=(), famille_tenue_a_l_ecart=None,
                 familles_jeu_final=(), organismes_portes=(), organismes_tenue_a_l_ecart=None,
                 organismes_jeu_final=None):
        if mode not in (MODE_INTERDIT_ENTIER, MODE_BRAS_DE_FLUX):
            raise GardeArret(f"harnais : mode inconnu {mode!r}")
        if mode == MODE_BRAS_DE_FLUX and (organismes_tenue_a_l_ecart is None or organismes_jeu_final is None):
            raise GardeArret("bras de flux planté : organismes de la famille tenue à l'écart et du jeu final à déclarer "
                             "(aucune valeur implicite)")
        self.mode = mode
        self.etiquette = ETIQUETTE_NON_EN_VIGUEUR if mode == MODE_BRAS_DE_FLUX else ""
        self._familles_interdites = set(familles_portes) | set(familles_jeu_final) | (
            {famille_tenue_a_l_ecart} if famille_tenue_a_l_ecart else set())
        self._organismes_interdits = set(organismes_portes) | set(organismes_tenue_a_l_ecart or ()) | \
            set(organismes_jeu_final or ())
        self._admis: list[str] = []
        self._bras: dict[str, DeclarationBrasDeFlux] = {}
        self._episodes: dict[int, EpisodeHarnais] = {}
        self._versions: dict[str, Version] = {}
        self._lignees_ouvertes: dict[str, list[int]] = {}
        self._capacite_enclave = secrets.token_hex(16)
        self._calendrier_comptes: dict[str, int] = {}
        self._comptes_lots: dict[str, int] = {}
        self.lectures_comptees: list[str] = []

    # --- provenance ------------------------------------------------------------------------------
    def admettre(self, contenu: bytes, jeton: JetonProvenance | None) -> bytes:
        verifier_provenance(contenu, jeton)
        self._admis.append(jeton.empreinte_contenu)
        return contenu

    # --- bras de flux -----------------------------------------------------------------------------
    def declarer_bras(self, decl: DeclarationBrasDeFlux) -> str:
        if self.mode != MODE_BRAS_DE_FLUX:
            raise GardeArret(f"{REFUS_LIGNEE} : aucun bras de flux hors du mode planté")
        if decl.etiquette != ETIQUETTE_NON_EN_VIGUEUR:
            raise GardeArret("bras de flux planté : étiquette « non en vigueur » exigée")
        if decl.nom in self._bras:
            raise GardeArret("bras de flux déjà déclaré")
        if set(decl.familles) & self._familles_interdites or set(decl.organismes) & self._organismes_interdits:
            raise GardeArret(REFUS_FAMILLE_PORTE)
        self._bras[decl.nom] = decl
        return decl.empreinte()

    # --- épisodes et rôles ------------------------------------------------------------------------
    def enregistrer_episode(self, episode: int, role: str, famille: str, organisme: str, h_role: int, h_debut: int,
                            contenu: bytes, jeton: JetonProvenance | None, bras: str | None = None) -> None:
        self.admettre(contenu, jeton)
        if role not in ROLES:
            raise GardeArret(f"rôle inconnu {role!r}")
        if episode in self._episodes:
            raise GardeArret("rôle déjà écrit (ajout seul)")
        if role in ("flux", "pli retenu") and self.mode != MODE_BRAS_DE_FLUX:
            raise GardeArret(f"{REFUS_LIGNEE} : rôle « {role} » hors du mode planté")
        if role in ("flux", "pli retenu") and bras is None:
            raise GardeArret("épisode de flux sans bras nommé")
        if role == "verdict":
            en_lignee = [self._episodes[k] for l in self._lignees_ouvertes.values() for k in l] + \
                [self._episodes[k] for v in self._versions.values() for k in v.lignee]
            if any(e.famille == famille or e.organisme == organisme for e in en_lignee):
                raise GardeArret(REFUS_MEME_FAMILLE + " (épisode de verdict d'une famille déjà en lignée)")
        self._episodes[episode] = EpisodeHarnais(episode, role, famille, organisme, bras, h_role, h_debut)

    def consigner_score(self, episode: int, version: str, horloge: int) -> None:
        ep = self._episodes[episode]
        v = self._versions.get(version)
        if v is None:
            raise GardeArret("score d'une version non scellée")
        if v.h_scellement >= horloge:
            raise GardeArret("score consigné avant le scellement de sa version")
        if episode in v.lignee:
            raise GardeArret("clause 2 (iii) : une version n'est jamais jugée sur un épisode de sa lignée")
        if ep.h_verdict is not None and horloge >= ep.h_verdict:
            raise GardeArret("clause 2 (i) : score consigné après le verdict")
        ep.scores[version] = horloge

    def rendre_verdict(self, episode: int, horloge: int) -> None:
        ep = self._episodes.get(episode)
        if ep is None:
            raise GardeArret(f"épisode {episode} jugé sans rôle écrit")
        if ep.h_role >= horloge:
            raise GardeArret(f"épisode {episode} : rôle écrit après le verdict")
        if ep.h_verdict is not None:
            raise GardeArret("second verdict")
        ep.h_verdict = horloge

    def verifier_roles_avant_verdict(self, journal) -> None:
        for ep, hv in zip(journal.colonne("v_episode").tolist(), journal.colonne("v_h_verdict").tolist()):
            if ep not in self._episodes:
                raise GardeArret(f"épisode {ep} jugé sans rôle écrit")
            if self._episodes[ep].h_role >= hv:
                raise GardeArret(f"épisode {ep} : rôle écrit après le verdict")

    # --- lignée -----------------------------------------------------------------------------------
    def ouvrir_lignee(self, nom_a_venir: str) -> None:
        if self.mode != MODE_BRAS_DE_FLUX:
            raise GardeArret(REFUS_LIGNEE)
        self._lignees_ouvertes[nom_a_venir] = []

    def ajouter_lignee(self, nom_a_venir: str | None = None, episode: int | None = None) -> None:
        if self.mode != MODE_BRAS_DE_FLUX:
            raise GardeArret(REFUS_LIGNEE)
        if nom_a_venir not in self._lignees_ouvertes:
            raise GardeArret("lignée non ouverte")
        ep = self._episodes.get(episode)
        if ep is None:
            raise GardeArret("épisode inconnu du harnais")
        if ep.role == "verdict":
            raise GardeArret(REFUS_VERDICT)
        familles_verdict = {e.famille for e in self._episodes.values() if e.role == "verdict"}
        if ep.famille in familles_verdict:
            raise GardeArret(REFUS_MEME_FAMILLE)
        organismes_verdict = {e.organisme for e in self._episodes.values() if e.role == "verdict"}
        if ep.organisme in organismes_verdict:
            raise GardeArret(REFUS_MEME_FAMILLE + " (organisme d'un épisode de verdict)")
        if ep.role == "hors rôle":
            raise GardeArret(REFUS_HORS_ROLE)
        if ep.role != "flux":
            raise GardeArret(f"lignée : rôle « {ep.role} » refusé (le pli retenu juge, il n'instruit pas)")
        decl = self._bras.get(ep.bras)
        if decl is None:
            raise GardeArret(f"{REFUS_APRES_COUP} (bras non déclaré)")
        premier = min(e.h_debut for e in self._episodes.values() if e.bras == ep.bras)
        if decl.h_scellement >= premier:
            raise GardeArret(REFUS_APRES_COUP)
        if ep.famille in self._familles_interdites or ep.famille not in decl.familles or \
                ep.organisme in self._organismes_interdits:
            raise GardeArret(REFUS_FAMILLE_PORTE)
        if ep.h_verdict is None:
            raise GardeArret("lignée : l'épisode n'a pas encore été jugé")
        en_place = [v for v in self._versions.values() if v.h_scellement < ep.h_verdict]
        for v in en_place:
            if episode in v.lignee:
                continue
            h = ep.scores.get(v.nom)
            if h is None or h >= ep.h_verdict:
                raise GardeArret("clause 2 (i) : le score de l'épisode par une version en place n'a pas été consigné "
                                 "avant le verdict")
        self._lignees_ouvertes[nom_a_venir].append(episode)

    def sceller_version(self, octets_direction: bytes, horloge: int, nom_a_venir: str | None = None) -> str:
        """Version nommée par empreinte, scellée avec sa lignée (vide hors du mode planté)."""
        lignee = tuple(self._lignees_ouvertes.get(nom_a_venir, [])) if nom_a_venir is not None else ()
        fam_v = {e.famille for e in self._episodes.values() if e.role == "verdict"}
        org_v = {e.organisme for e in self._episodes.values() if e.role == "verdict"}
        for k in lignee:  # revérification au scellement (constat I-2)
            e = self._episodes[k]
            if e.famille in fam_v or e.organisme in org_v:
                raise GardeArret(REFUS_MEME_FAMILLE + " (revérifié au scellement)")
        if nom_a_venir is not None:
            self._lignees_ouvertes.pop(nom_a_venir, None)
        nom = empreinte_octets(octets_direction, repr(lignee).encode())
        if nom in self._versions:
            raise GardeArret("version déjà scellée sous ce nom")
        self._versions[nom] = Version(nom, lignee, horloge, bool(lignee), bytes(octets_direction))
        return nom

    def lignee(self, nom: str) -> tuple:
        if nom not in self._versions:
            raise GardeArret("version inconnue")
        return self._versions[nom].lignee

    # --- enclave (jetons de capacité) -------------------------------------------------------------
    def capacite_procedure_scellee(self) -> str:
        """Le jeton de capacité de l'enclave ; seule la procédure scellée le détient. Le jeton est remis par l'épreuve à
        la procédure scellée ; le harnais simulé ne sépare pas les appelants (m-5) : l'enclave est modélisée, non
        tenue."""
        return self._capacite_enclave

    def lire_version(self, nom: str, champ: str, capacite: str | None = None) -> bytes:
        v = self._versions.get(nom)
        if v is None:
            raise GardeArret("version inconnue")
        if v.nee_du_flux and capacite != self._capacite_enclave:
            raise GardeArret(REFUS_VERSION_CLOSE)
        if champ not in ("poids", "seuil", "scores_par_episode"):
            raise GardeArret("champ de version inconnu")
        return v.contenu

    def fixer_calendrier(self, lot: str, date: int) -> None:
        if lot in self._calendrier_comptes:
            raise GardeArret("calendrier d'un lot déjà fixé (fixé d'avance, jamais changé)")
        self._calendrier_comptes[lot] = date

    def poser_compte(self, lot: str, compte: int, capacite: str) -> None:
        if capacite != self._capacite_enclave:
            raise GardeArret("seule la procédure scellée pose un compte")
        self._comptes_lots[lot] = int(compte)

    def compte_lot(self, lot: str, date: int) -> int:
        """Servi au rôle de concepteur à la date fixée d'avance ; chaque compte rendu est compté comme une lecture."""
        if self._calendrier_comptes.get(lot) != date:
            raise GardeArret("compte d'un lot hors de sa date fixée d'avance")
        if lot not in self._comptes_lots:
            raise GardeArret("compte du lot non posé")
        self.lectures_comptees.append(lot)
        return self._comptes_lots[lot]

    def reconcevoir(self, point_de_depart: str | None) -> str:
        if point_de_depart is not None:
            v = self._versions.get(point_de_depart)
            if v is None or v.nee_du_flux:
                raise GardeArret(REFUS_RECONCEPTION)
        return "reconception admise : elle part de moniteurs conçus hors du flux"


class RegistreTemoins:
    """Témoins exogènes plantés à deux usages disjoints : « lecon » (négatifs qui donnent sa direction à la sonde) et
    « calibrage » (qui donnent son seuil)."""

    USAGES = ("lecon", "calibrage")

    def __init__(self):
        self._usage: dict[int, str] = {}

    def reserver(self, ids, usage: str) -> None:
        if usage not in self.USAGES:
            raise GardeArret(f"usage de témoin inconnu {usage!r}")
        ids = [int(i) for i in ids]
        for i in ids:
            if self._usage.get(i, usage) != usage:
                raise GardeArret(REFUS_TEMOINS)
        for i in ids:
            self._usage[i] = usage

    def exiger(self, ids, usage: str) -> None:
        for i in ids:
            if self._usage.get(int(i)) != usage:
                raise GardeArret(f"témoin {int(i)} non réservé à l'usage {usage!r}" +
                                 (f" ({REFUS_TEMOINS})" if int(i) in self._usage else ""))


class RegistrePlis:
    """Plis retenus, tirés par le harnais ; un pli qui a servi à choisir est consommé."""

    def __init__(self):
        self._plis: dict[int, dict] = {}
        self._suivant = 0

    def tirer(self, ids: np.ndarray, taux: float, rng: np.random.Generator) -> int:
        ids = np.asarray(ids)
        sel = ids[rng.random(len(ids)) < taux]
        k = self._suivant
        self._plis[k] = {"ids": sel, "consomme": False}
        self._suivant += 1
        return k

    def utiliser_pour_choisir(self, k: int) -> np.ndarray:
        p = self._plis[k]
        if p["consomme"]:
            raise GardeArret(REFUS_PLI_CONSOMME)
        p["consomme"] = True
        return p["ids"]

    def annoncer(self, k: int) -> np.ndarray:
        p = self._plis[k]
        if p["consomme"]:
            raise GardeArret(REFUS_PLI_CONSOMME)
        return p["ids"]

    def consomme(self, k: int) -> bool:
        return self._plis[k]["consomme"]


class RegistreRegards:
    """On ajoute, on ne remplace pas : toute lecture d'un regard reste consignée."""

    def __init__(self):
        self._lectures: list[tuple[str, int, int]] = []

    def consigner(self, regard: str, episode: int, lecture: int) -> None:
        self._lectures.append((regard, int(episode), int(lecture)))

    def remplacer(self, *args, **kwargs):
        raise GardeArret("regards : on ajoute, on ne remplace pas")

    def lectures(self, regard: str) -> list[tuple[int, int]]:
        return [(e, l) for r, e, l in self._lectures if r == regard]
