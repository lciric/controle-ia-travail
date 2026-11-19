"""Entrées de la lecture des sondes de l'étape B bis par la lentille publique (texte scellé, « Entrées exactes »).

Ce module est le seul à ouvrir les deux fichiers des sondes :
- E-2 `diag/<run-bbis>/sondes-bbis.json` : analysé en entier (JSON), mais seuls les champs de la **liste blanche** en sortent
  (`VueE2`) ; la régularisation de `enc.reglage` n'est ni gardée, ni écrite, ni imprimée (aucun message d'erreur ne la porte) ;
- E-1 `donnees/<run-bbis>/sondes-bbis.npz` : empreinte calculée sur les octets, puis ouvert **clé par clé** (`ArchiveE1`) ;
  seules les entrées `sonde_{w,b,q}` et `enc_{w,b,q}` sont décodées, jamais `direction0_*` ni `direction1_*`.
Rien n'est ouvert avant la clé `VERDICT-BBIS` (registre propre de l'apprentissage des sondes sur la tâche) ni sans les clés
`SCELLEMENT-`, `GO-` et `CODE-LENTILLES-BBIS` du registre propre de ce texte. Des registres, seules les clés nommées sont
gardées. Toute autre forme que (a), (b), (c) d'« Attendu » : arrêt « forme mal comprise ».
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from . import constantes_v1 as K
from .constantes_v1 import Arret, FormeMalComprise, Refus

BRANCHE_DONNEES = "donnees/t07-etape-b-bis-v2"
_RE_LIGNE = re.compile(r"^\|(.*)\|\s*$")
_RE_HEURE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")
_RE_SHA = re.compile(r"^[0-9a-f]{64}$")
_RE_RUN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
_RE_REGLAGE = re.compile(r"^(lineaire|attention)-c([0-9]+)-l2_")           # texte, E-2 : seules famille et couche sortent
_RE_ENTREE = re.compile(r"^(?P<cellule>" + "|".join(re.escape(c) for c in K.CELLULES) + r")__(?P<pli>e[01])__"
                        r"(?P<objet>sonde|enc|direction0|direction1)_(?P<champ>w|b|q)$")
OBJETS_DECODES = ("sonde", "enc")
CHAMPS_SONDE = ("cellule", "pli_lu", "famille", "couche", "agregation", "empreinte_sonde", "nom_sonde")
MOTIF_ECHEC_SONDE = "échec à l'apprentissage"
MOTIF_LECTEUR_NON_APPRIS = "non appris, la sonde apprise ayant échoué"
MOTIF_ECHEC_LECTEUR = "échec à l'apprentissage"


# --- registres : seules les clés nommées sont gardées --------------------------------------------------------------------------
@dataclass(frozen=True)
class LigneRegistre:
    cle: str
    heure: str
    chemin: str | None
    sha256: str | None


def lignes_par_cle(registre: str | Path, cles: tuple[str, ...]) -> dict[str, list[LigneRegistre]]:
    """Lignes `| clé | heure | chemin | sha256 |` dont la clé est l'une de `cles` ; toute autre ligne est écartée sans être
    gardée ni rendue. Pour `VERDICT-BBIS`, seules la clé et l'heure sortent (jamais le chemin du verdict)."""
    registre = Path(registre)
    if registre.name == K.REGISTRE_INTERDIT:
        raise Refus(f"{registre.name} : registre jamais lu ni écrit par ce texte")
    if not registre.is_file():
        raise Arret(f"registre {registre} absent sur disque")
    sortie: dict[str, list[LigneRegistre]] = {c: [] for c in cles}
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = _RE_LIGNE.match(ligne.strip())
        if not m:
            continue
        cellules = [c.strip() for c in m.group(1).split("|")]
        if not cellules or cellules[0] not in cles:
            continue
        if len(cellules) != 4 or not _RE_HEURE.match(cellules[1]):
            raise Arret(f"registre {registre.name} : ligne de clé {cellules[0]} mal formée")
        if cellules[0] == "VERDICT-BBIS":
            sortie[cellules[0]].append(LigneRegistre(cellules[0], cellules[1], None, None))
            continue
        if not _RE_SHA.match(cellules[3]):
            raise Arret(f"registre {registre.name} : empreinte mal formée à la clé {cellules[0]}")
        sortie[cellules[0]].append(LigneRegistre(*cellules))
    return sortie


def exiger_registre_propre(registre_propre: str | Path) -> dict[str, LigneRegistre]:
    """`SCELLEMENT-`, `GO-` et `CODE-LENTILLES-BBIS` présentes, sinon rien ne part ; la ligne de scellement cite ce texte."""
    lignes = lignes_par_cle(registre_propre, K.CLES_EXIGEES_AVANT_TOUT)
    for cle in K.CLES_EXIGEES_AVANT_TOUT:
        if not lignes[cle]:
            raise Refus(f"{cle} absente du registre propre : rien ne part")
    scellement = lignes["SCELLEMENT-LENTILLES-BBIS"][-1]
    if scellement.chemin != K.TEXTE or scellement.sha256 != K.EMPREINTE_TEXTE:
        raise Refus("SCELLEMENT-LENTILLES-BBIS ne cite pas le texte scellé de ce code : rien ne part")
    return {cle: lignes[cle][-1] for cle in K.CLES_EXIGEES_AVANT_TOUT}


@dataclass(frozen=True)
class CourseBbis:
    run: str
    chemin_e2: str
    sha256_e2: str
    heure_verdict: str
    heure_scores: str


def exiger_scores_et_verdict(registre_bbis: str | Path) -> CourseBbis:
    """`VERDICT-BBIS` présente (sinon refus : rien n'est ouvert) ; `SCORES-BBIS` présente en une seule ligne, qui nomme E-2."""
    lignes = lignes_par_cle(registre_bbis, ("SCORES-BBIS", "VERDICT-BBIS"))
    if not lignes["VERDICT-BBIS"]:
        raise Refus("VERDICT-BBIS absente : E-1 et E-2 ne sont pas ouverts avant le verdict scellé")
    scores = lignes["SCORES-BBIS"]
    if not scores:
        raise Refus("SCORES-BBIS absente : rien ne part")
    if len(scores) > 1:
        raise Refus("SCORES-BBIS en plusieurs lignes : nœud (la mère désigne la course, par les noms seulement)")
    parties = scores[0].chemin.split("/")
    if len(parties) != 3 or parties[0] != "diag" or parties[2] != K.NOM_E2 or not _RE_RUN.match(parties[1]):
        raise FormeMalComprise("SCORES-BBIS : chemin d'une autre forme que diag/<run-bbis>/sondes-bbis.json")
    return CourseBbis(parties[1], scores[0].chemin, scores[0].sha256, lignes["VERDICT-BBIS"][-1].heure, scores[0].heure)


# --- chemins : quatre fichiers, et eux seuls -----------------------------------------------------------------------------------
def chemins_permis(run: str) -> dict[str, str]:
    e2, e1 = f"diag/{run}/{K.NOM_E2}", f"donnees/{run}/{K.NOM_E1}"
    return {"e2": e2, "e2_compagnon": e2 + ".sha256", "e1": e1, "e1_compagnon": e1 + ".sha256"}


def exiger_chemin_permis(chemin_relatif: str, run: str) -> str:
    """Refuse tout autre chemin que E-1, E-2 et leurs compagnons (scores, planchers, relecture, manifeste, journaux…)."""
    if str(chemin_relatif) not in set(chemins_permis(run).values()):
        raise Refus(f"chemin {chemin_relatif!r} : jamais ouvert par cette chaîne (seuls E-1, E-2 et leurs compagnons)")
    return str(chemin_relatif)


def _octets(racine: Path, chemin_relatif: str, run: str) -> bytes:
    p = Path(racine) / exiger_chemin_permis(chemin_relatif, run)
    if not p.is_file():
        raise Arret(f"{chemin_relatif} absent sur disque (R11)")
    return p.read_bytes()


def _compagnon(racine: Path, chemin_relatif: str, run: str) -> str:
    texte = _octets(racine, chemin_relatif, run).decode("utf-8")
    m = re.match(r"^([0-9a-f]{64})  (\S.*)\n?$", texte)
    if not m or m.group(2) != Path(chemin_relatif).name[:-len(".sha256")]:
        raise Arret(f"{chemin_relatif} : compagnon illisible (R11)")
    return m.group(1)


# --- E-2 : liste blanche -------------------------------------------------------------------------------------------------------
class VueE2:
    """Seul accès au contenu de E-2. Tout champ hors de la liste blanche, la valeur d'un `echec`, le sous-dictionnaire
    `ordre2` et la chaîne `enc.reglage` entière sont refusés (`Refus`)."""

    def __init__(self, doc: dict):
        if not isinstance(doc, dict):
            raise FormeMalComprise("E-2 : un dictionnaire est attendu à la racine")
        self.__doc = doc

    def _noeud(self, chemin: tuple):
        n = self.__doc
        for c in chemin:
            if not isinstance(n, dict) or c not in n:
                raise FormeMalComprise(f"E-2 : champ {'/'.join(map(str, chemin))} absent")
            n = n[c]
        return n

    @staticmethod
    def _source(chemin: tuple) -> bool:
        return len(chemin) >= 3 and chemin[0] == "sources" and chemin[2] in K.PLIS

    def champ(self, *chemin: str):
        """Valeur d'un champ de la liste blanche (noms exacts du texte)."""
        permis = (chemin in (("run_id",), ("fichier_sondes", "fichier"), ("fichier_sondes", "sha256"))
                  or (self._source(chemin) and len(chemin) == 4 and chemin[3] in CHAMPS_SONDE)
                  or (self._source(chemin) and chemin[3:] == ("enc", "empreinte")))
        if not permis:
            raise Refus(f"E-2 : champ {'/'.join(map(str, chemin))} hors de la liste blanche")
        return self._noeud(chemin)

    def cles(self, *chemin: str) -> list[str]:
        """Clés de `sources` (cellules) et, sous une cellule, ses plis."""
        if not (chemin == ("sources",) or (len(chemin) == 2 and chemin[0] == "sources")):
            raise Refus(f"E-2 : clés de {'/'.join(map(str, chemin))} hors de la liste blanche")
        n = self._noeud(chemin)
        if not isinstance(n, dict):
            raise FormeMalComprise(f"E-2 : {'/'.join(chemin)} n'est pas un dictionnaire")
        return sorted(n)

    def present(self, *chemin: str) -> bool:
        """Présence d'une clé (jamais sa valeur) : `echec`, `enc`, `enc.echec`, et les champs de la liste blanche."""
        permis = self._source(chemin) and (
            (len(chemin) == 4 and chemin[3] in CHAMPS_SONDE + ("echec", "enc"))
            or chemin[3:] in (("enc", "echec"), ("enc", "reglage"), ("enc", "empreinte")))
        if not permis:
            raise Refus(f"E-2 : présence de {'/'.join(map(str, chemin))} hors de la liste blanche")
        n = self._noeud(chemin[:-1])
        return isinstance(n, dict) and chemin[-1] in n

    def reglage_lecteur(self, cellule: str, pli: str) -> tuple[str, int]:
        """Famille et couche du lecteur honnête, tirées de `enc.reglage` ; la suite de la chaîne (la régularisation) ne sort
        jamais, ni dans une valeur rendue ni dans un message."""
        chaine = self._noeud(("sources", cellule, pli, "enc", "reglage"))
        m = _RE_REGLAGE.match(chaine) if isinstance(chaine, str) else None
        if not m:
            raise FormeMalComprise(f"E-2 : enc.reglage de {cellule}/{pli} d'une autre forme que famille-c<couche>-l2_… "
                                   "(forme mal comprise ; la chaîne n'est pas imprimée)")
        return m.group(1), int(m.group(2))


# --- E-1 : clé par clé -----------------------------------------------------------------------------------------------------------
class ArchiveE1:
    """Archive `numpy` des sondes, ouverte sans décodage ; `lire` ne décode que les entrées `sonde_*` et `enc_*`."""

    def __init__(self, chemin: str | Path):
        self._npz = np.load(chemin, allow_pickle=False)
        self.noms = sorted(self._npz.files)
        self.decodees: list[str] = []
        for nom in self.noms:
            if not _RE_ENTREE.match(nom):
                self._npz.close()
                raise FormeMalComprise(f"E-1 : nom d'entrée inconnu {nom!r} (forme mal comprise)")

    def objets(self, cellule: str, pli: str) -> set[str]:
        """Noms courts (`sonde_w`, `enc_q`, `direction0_b`…) des entrées d'une cellule et d'un pli."""
        prefixe = f"{cellule}__{pli}__"
        return {n[len(prefixe):] for n in self.noms if n.startswith(prefixe)}

    def lire(self, nom: str) -> np.ndarray:
        m = _RE_ENTREE.match(nom)
        if not m or m.group("objet") not in OBJETS_DECODES:
            raise Refus(f"E-1 : l'entrée {nom!r} n'est jamais décodée (seules sonde_* et enc_*)")
        if nom not in self.noms:
            raise FormeMalComprise(f"E-1 : entrée {nom!r} absente")
        self.decodees.append(nom)
        return np.asarray(self._npz[nom])

    def fermer(self) -> None:
        self._npz.close()


# --- sondes ------------------------------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class Sonde:
    """Une sonde apprise (`role` « sonde ») ou un lecteur honnête (`role` « enc ») d'une cellule et d'un pli."""
    cellule: str
    pli: str
    role: str
    lue: bool
    motif: str | None = None
    famille: str | None = None
    couche: int | None = None
    agregation: str | None = None
    nom: str | None = None
    empreinte: str | None = None
    w: np.ndarray | None = None
    b: float | None = None
    q: np.ndarray | None = None

    @property
    def cle(self) -> str:
        return f"{self.cellule}/{self.pli}/{self.role}"

    def vecteurs(self) -> dict[str, np.ndarray]:
        """`w` et, pour la famille « attention », `q` (coordonnées brutes du flux à la couche de la sonde)."""
        if not self.lue:
            return {}
        return {"w": self.w} | ({"q": self.q} if self.q is not None else {})


def empreinte_sonde(famille: str, nom: str, couche: int, agregation: str, w, b, q=None) -> str:
    """Recalcul de `familles.SondeLineaireJetons.empreinte` : SHA-256 de « <famille>:<nom>/<couche>/<agrégation> » puis des
    octets en double précision de `w`, `[b]` et `q` s'il existe."""
    h = hashlib.sha256(f"{famille}:{nom}/{couche}/{agregation}".encode("utf-8"))
    for t in [w, np.array([b])] + ([q] if q is not None else []):
        h.update(np.ascontiguousarray(t, dtype=np.float64).tobytes())
    return h.hexdigest()


def _exiger_reglage(ou: str, famille, couche, agregation) -> None:
    if famille not in K.FAMILLES:
        raise FormeMalComprise(f"{ou} : famille {famille!r} hors de {K.FAMILLES}")
    if isinstance(couche, bool) or not isinstance(couche, int) or couche not in K.COUCHES:
        raise FormeMalComprise(f"{ou} : couche {couche!r} hors de {K.COUCHES}")
    if agregation != K.AGREGATION_DE[famille]:
        raise FormeMalComprise(f"{ou} : agrégation {agregation!r} différente de celle de la famille {famille}")


def _tableaux(archive: ArchiveE1, cellule: str, pli: str, objet: str, famille: str, largeur: int):
    """`w`, `b`, `q` d'une sonde ; `q` existe si et seulement si la famille est « attention »."""
    presents = archive.objets(cellule, pli)
    for champ in ("w", "b"):
        if f"{objet}_{champ}" not in presents:
            raise FormeMalComprise(f"E-1 : entrée {cellule}__{pli}__{objet}_{champ} absente (forme mal comprise)")
    a_q = f"{objet}_q" in presents
    if a_q != (famille == "attention"):
        raise FormeMalComprise(f"E-1 : {cellule}__{pli}__{objet}_q {'présente' if a_q else 'absente'} pour la famille "
                               f"{famille} (forme mal comprise)")
    w = archive.lire(f"{cellule}__{pli}__{objet}_w")
    b = archive.lire(f"{cellule}__{pli}__{objet}_b")
    q = archive.lire(f"{cellule}__{pli}__{objet}_q") if a_q else None
    for nom, t in (("w", w), ("q", q)):
        if t is not None and (t.shape != (largeur,) or t.dtype.kind != "f"):
            raise FormeMalComprise(f"E-1 : {cellule}__{pli}__{objet}_{nom} de forme {t.shape} ({t.dtype}) ; "
                                   f"vecteur réel de largeur {largeur} attendu")
    if b.shape != (1,) or b.dtype.kind != "f":
        raise FormeMalComprise(f"E-1 : {cellule}__{pli}__{objet}_b : tableau d'un élément attendu")
    return w, float(b[0]), q


@dataclass(frozen=True)
class Entrees:
    course: CourseBbis
    sondes: tuple[Sonde, ...]
    extrait: dict
    empreinte_extrait: str
    sha256_e1: str
    sha256_e2: str
    entrees_decodees: tuple[str, ...]
    entrees_non_decodees: tuple[str, ...]


def empreinte_extrait(extrait: dict) -> str:
    return hashlib.sha256(json.dumps(extrait, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()


def lire_sondes(vue: VueE2, archive: ArchiveE1, run: str, largeur: int = K.LARGEUR) -> tuple[tuple[Sonde, ...], dict]:
    """Applique « Attendu » : vingt sondes, formes (a), (b), (c) seules admises ; rend les sondes et l'extrait de la liste
    blanche (le seul contenu de E-2 qui sorte de ce module)."""
    if vue.champ("run_id") != run:
        raise FormeMalComprise("E-2 : run_id différent du dossier de course de SCORES-BBIS")
    if vue.cles("sources") != sorted(K.CELLULES):
        raise FormeMalComprise(f"E-2 : cellules {vue.cles('sources')} ; attendues {sorted(K.CELLULES)} (cellule manquante ou "
                               "inconnue)")
    sondes: list[Sonde] = []
    extrait = {"run_id": run, "fichier_sondes": {"fichier": vue.champ("fichier_sondes", "fichier"),
                                                 "sha256": vue.champ("fichier_sondes", "sha256")}, "sources": {}}
    for cellule in K.CELLULES:
        if vue.cles("sources", cellule) != sorted(K.PLIS):
            raise FormeMalComprise(f"E-2 : plis de {cellule} : {vue.cles('sources', cellule)} ; attendus {sorted(K.PLIS)}")
        for pli in K.PLIS:
            ou = f"{cellule}/{pli}"
            src = ("sources", cellule, pli)
            if vue.champ(*src, "cellule") != cellule or vue.champ(*src, "pli_lu") != int(pli[1]):
                raise FormeMalComprise(f"E-2 : {ou} : champs cellule ou pli_lu différents de leurs clés")
            ext = {"cellule": cellule, "pli_lu": int(pli[1]), "echec_present": vue.present(*src, "echec")}
            presents = archive.objets(cellule, pli)
            champs_sonde = [c for c in CHAMPS_SONDE[2:] if vue.present(*src, c)]
            if ext["echec_present"]:                                                    # forme (a)
                if champs_sonde or vue.present(*src, "enc") or presents:
                    raise FormeMalComprise(f"{ou} : clé echec présente avec des champs ou des entrées de sonde (forme mal "
                                           "comprise)")
                sondes += [Sonde(cellule, pli, "sonde", False, MOTIF_ECHEC_SONDE),
                           Sonde(cellule, pli, "enc", False, MOTIF_LECTEUR_NON_APPRIS)]
                extrait["sources"].setdefault(cellule, {})[pli] = ext
                continue
            if len(champs_sonde) != len(CHAMPS_SONDE[2:]) or not vue.present(*src, "enc"):
                raise FormeMalComprise(f"{ou} : champ de la liste blanche absent sans clé echec (forme mal comprise)")
            famille, couche, agregation = (vue.champ(*src, c) for c in ("famille", "couche", "agregation"))
            nom, attendue = vue.champ(*src, "nom_sonde"), vue.champ(*src, "empreinte_sonde")
            _exiger_reglage(f"E-2 : {ou}", famille, couche, agregation)
            if not isinstance(nom, str) or not isinstance(attendue, str):
                raise FormeMalComprise(f"E-2 : {ou} : nom_sonde ou empreinte_sonde d'un autre type")
            w, b, q = _tableaux(archive, cellule, pli, "sonde", famille, largeur)
            if empreinte_sonde(famille, nom, couche, agregation, w, b, q) != attendue:
                raise FormeMalComprise(f"{ou} : empreinte recalculée de la sonde apprise différente de empreinte_sonde")
            sondes.append(Sonde(cellule, pli, "sonde", True, None, famille, couche, agregation, nom, attendue, w, b, q))
            ext |= {"famille": famille, "couche": couche, "agregation": agregation, "empreinte_sonde": attendue,
                    "nom_sonde": nom, "enc": {"echec_present": vue.present(*src, "enc", "echec")}}
            entrees_enc = {o for o in presents if o.startswith("enc_")}
            if ext["enc"]["echec_present"]:                                             # forme (b)
                if vue.present(*src, "enc", "reglage") or vue.present(*src, "enc", "empreinte") or entrees_enc:
                    raise FormeMalComprise(f"{ou} : enc.echec présente avec enc.reglage, enc.empreinte ou une entrée enc_* "
                                           "(forme mal comprise)")
                sondes.append(Sonde(cellule, pli, "enc", False, MOTIF_ECHEC_LECTEUR))
            else:                                                                       # forme (c)
                if not (vue.present(*src, "enc", "reglage") and vue.present(*src, "enc", "empreinte")):
                    raise FormeMalComprise(f"{ou} : enc.reglage ou enc.empreinte absent sans enc.echec (forme mal comprise)")
                fam_e, couche_e = vue.reglage_lecteur(cellule, pli)
                agr_e, nom_e, att_e = K.AGREGATION_DE[fam_e], f"enc-{cellule}-{pli}", vue.champ(*src, "enc", "empreinte")
                _exiger_reglage(f"E-2 : {ou} (lecteur honnête)", fam_e, couche_e, agr_e)
                we, be, qe = _tableaux(archive, cellule, pli, "enc", fam_e, largeur)
                if empreinte_sonde(fam_e, nom_e, couche_e, agr_e, we, be, qe) != att_e:
                    raise FormeMalComprise(f"{ou} : empreinte recalculée du lecteur honnête différente de enc.empreinte")
                sondes.append(Sonde(cellule, pli, "enc", True, None, fam_e, couche_e, agr_e, nom_e, att_e, we, be, qe))
                ext["enc"] |= {"famille": fam_e, "couche": couche_e, "empreinte": att_e}
            extrait["sources"].setdefault(cellule, {})[pli] = ext
    return tuple(sondes), extrait


def ouvrir_entrees(racine: str | Path, registre_bbis: str | Path, registre_propre: str | Path,
                   largeur: int = K.LARGEUR) -> Entrees:
    """Ouvre E-1 et E-2 sous `racine` (qui porte `diag/<run-bbis>/` et `donnees/<run-bbis>/`), après les contrôles de
    registre ; vérifie les empreintes (compagnons, ligne `SCORES-BBIS`, `fichier_sondes.sha256`) ; rend les sondes."""
    exiger_registre_propre(registre_propre)
    course = exiger_scores_et_verdict(registre_bbis)
    racine, ch = Path(racine), chemins_permis(course.run)
    if ch["e2"] != course.chemin_e2:
        raise FormeMalComprise("chemin de E-2 différent de celui de SCORES-BBIS")
    octets_e2 = _octets(racine, ch["e2"], course.run)
    sha_e2 = hashlib.sha256(octets_e2).hexdigest()
    if sha_e2 != _compagnon(racine, ch["e2_compagnon"], course.run) or sha_e2 != course.sha256_e2:
        raise Arret("empreinte de E-2 différente de son compagnon ou de la ligne SCORES-BBIS (R11)")
    try:
        vue = VueE2(json.loads(octets_e2.decode("utf-8")))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise FormeMalComprise("E-2 : JSON illisible") from None
    del octets_e2
    if vue.champ("fichier_sondes", "fichier") != ch["e1"]:
        raise FormeMalComprise("E-2 : fichier_sondes.fichier différent de donnees/<run-bbis>/sondes-bbis.npz")
    octets_e1 = _octets(racine, ch["e1"], course.run)
    sha_e1 = hashlib.sha256(octets_e1).hexdigest()
    del octets_e1
    if sha_e1 != _compagnon(racine, ch["e1_compagnon"], course.run) or sha_e1 != vue.champ("fichier_sondes", "sha256"):
        raise Arret("empreinte de E-1 différente de son compagnon ou de fichier_sondes.sha256 (R11)")
    archive = ArchiveE1(racine / ch["e1"])
    try:
        sondes, extrait = lire_sondes(vue, archive, course.run, largeur)
        decodees = tuple(archive.decodees)
        non_decodees = tuple(n for n in archive.noms if n not in set(decodees))
    finally:
        archive.fermer()
    return Entrees(course, sondes, extrait, empreinte_extrait(extrait), sha_e1, sha_e2, decodees, non_decodees)


# --- récupération : E-1, E-2 et leurs compagnons, seuls, par leur chemin -----------------------------------------------------------
def recuperer_entrees(url_depot: str, destination: str | Path, registre_bbis: str | Path, registre_propre: str | Path,
                      branche: str = BRANCHE_DONNEES) -> Path:
    """Clone partiel sans contenus (`--filter=blob:none`, sans extraction), puis extraction des quatre chemins permis, et
    d'eux seuls : aucun autre contenu de la branche des données n'est téléchargé. Refusé avant `VERDICT-BBIS`."""
    exiger_registre_propre(registre_propre)
    course = exiger_scores_et_verdict(registre_bbis)
    destination = Path(destination)
    clone = destination / "clone-sans-contenus"
    if clone.exists():
        raise Arret(f"{clone} existe déjà (R12)")
    destination.mkdir(parents=True, exist_ok=True)

    def git(args: list[str], cwd: Path, sortie=subprocess.DEVNULL) -> None:
        r = subprocess.run(["git", *args], cwd=cwd, stdout=sortie, stderr=subprocess.PIPE)
        if r.returncode != 0:
            raise Arret(f"git {args[0]} en échec (code {r.returncode}) : récupération des entrées refusée ou impossible")

    git(["clone", "-q", "--filter=blob:none", "--no-checkout", "--depth", "1", "--single-branch", "--branch", branche,
         url_depot, str(clone)], destination)
    for chemin in chemins_permis(course.run).values():
        cible = destination / exiger_chemin_permis(chemin, course.run)
        cible.parent.mkdir(parents=True, exist_ok=True)
        with open(cible, "xb") as f:
            git(["show", f"HEAD:{chemin}"], clone, sortie=f)
    return destination
