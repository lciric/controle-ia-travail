"""Fermeture et ouverture des sorties de P3-bis (témoin positif planté), v2.

Texte qui fait foi : `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon9.md` (`eb65773f…`, à sceller
sous `prereg/P3-bis-temoin-positif-v1.md`) : « Plan d'analyse », points 1 (second paquet), 3, 4, 6 (fermeture, classes,
essai différentiel) et 8 (registre des préalables, garde d'ouverture, journal des ouvertures, rendez-vous, branches 1 et 2) ;
« Liste d'arrêt » ; « Ce que le code et la chaîne doivent changer », points 2 (c) et 5 ; décision N-066 (`21e83ed5…`).
Version 2 de `ouverture_p3bis_v1.py` (`8972bfb1…`, commit `e86a6f32`, gardée telle quelle, R12), corrigée d'après la
contre-lecture du code (`brouillons/P3-bis-temoin-positif-v1/contre-lecture-code-p3bis-v1.md`, `7a074ad1…`) : CP-01 (trois
décisions, modes `pleine`, `reduite`, `pleine-anticipee`), CP-02 (journal au format exact, relu à chaque tentative, codes de
motif de la liste fermée), CP-04 (longueur de l'archive comprimée sur 8 octets), CP-05 (durées des lectures écrites dans le
paquet), CP-06 (journal impossible à écrire : refus), CP-08 (aucun `--instant` en ligne de commande), CP-11 (motifs des refus
du dépliage et de la mise en paquet), CP-16 (accord de l'issue exigé, sceau vérifié), CP-17 (antériorités strictes, entropie
exigée en mode décisif).

    python -m controle_ia.premier_test_ia.ouverture_p3bis_v2 fermer-run --run R [--partiel]
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v2 exiger-aucun-clair --run R
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v2 deplier-run --run R
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v2 lectures-fermees --run R --lecture RL \
        --lecture-complementaire RLC [--prereg P --entropie E]
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v2 fermer --run R --lecture RL --lecture-complementaire RLC [--entropie E]
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v2 ouvrir --mode pleine|reduite|pleine-anticipee --run R \
        --sortie DOSSIER [--racine-paquets C] [--date-paquet AAAA-MM-JJTHH:MM:SSZ]
    python -m controle_ia.premier_test_ia.ouverture_p3bis_v2 exposer-issue FICHIER [--lecture-p3bis CHEMIN]
(toutes, `exposer-issue` excepté, avec `--racine` : défaut le dossier courant, racine du clone.) `--lecture-p3bis` est exigée
pour les lignes 2 à 5 (CP-16) ; `lectures-fermees` exige `--entropie` dès que `--prereg` est donné (mode décisif, CP-17) ;
l'instant de l'ouverture est celui de l'horloge (le paramètre `instant` reste en Python pour les essais, CP-08).

**Le texte nomme deux sous-commandes, `fermer` et `ouvrir`** ; cinq s'y ajoutent, déclarées (écart 3 du développeur v1) : le
second paquet demande `fermer-run` (sur l'instance, avant toute poussée), `exiger-aucun-clair` (garde de la poussée) et
`deplier-run` (dans le clone fermé, avant les lectures) ; `lectures-fermees` enchaîne, dans le clone fermé, le dépliage, les
deux lectures (points 3 et 4, sorties standard et d'erreur redirigées dans l'espace fermé), l'écriture de leurs durées et
`fermer`, et n'imprime que les codes de sortie, le motif d'un refus du dépliage et l'empreinte du paquet ; `exposer-issue`
affiche les seules valeurs `issue` et `ligne` du fichier d'issue.

**Paquet des lectures** `diag/p3bis-ferme-<run>/paquet-ferme-v1.tar`, exactement `TAILLE_PAQUET_LECTURES` = 16 783 360
octets (1 639 × 10 240 = 512 + 512 + 512 + 16 780 800 + 1 024), archive USTAR à deux membres de longueur fixe, métadonnées
normalisées (date 0, propriétaire 0, mode 0644) : `sel.txt`, les 32 octets bruts de `secrets.token_bytes(32)` ; `corps.bin`,
exactement `TAILLE_CORPS_LECTURES` octets : **la longueur L de l'archive comprimée sur 8 octets (entier non signé, poids fort
en tête)**, le flux xz (`lzma`, contrôle CRC64) d'une archive pax des sorties, puis la bourre tirée par `secrets` (texte,
plan, point 6 ; CP-04). La relecture exige 0 < L ≤ `TAILLE_CORPS_LECTURES` − 8 et un flux xz fini exactement après L octets.
Les en-têtes ustar ne changent jamais d'une issue à l'autre ; tout le reste est à haute entropie, sauf les 8 octets de
longueur, qui ne portent que la taille comprimée des sorties. Seule l'empreinte du paquet est imprimée ; son sel n'est jamais
dérivé de l'entropie citée (garde à la relecture). L'espace fermé porte aussi `durees-lectures-v1.json` : durées du
dépliage, de chaque lecture et de la chaîne avant la mise en paquet (classe 2, CP-05), mises dans le paquet avec le reste.

**Second paquet** `diag/<run>/paquet-run-ferme-v1.tar` : USTAR à deux membres, `sel.txt` et `sorties.tar` (archive pax de
`donnees/<run>/` **entier** et de `diag/<run>/episodes-p3.json`, avec leurs compagnons) ; seulement ses morceaux
`paquet-run-ferme-v1.tar.000`, `.001`, … d'au plus `TAILLE_MORCEAU_MAX` octets, chacun avec son compagnon, et l'index scellé
`paquet-run-ferme-v1.json` (écart 4 du développeur v1, à porter au texte). Non comprimé ; le dépliage ne sort que les fichiers
que lisent les lectures (`fichiers_lus`). `.git/info/exclude` du clone reçoit les chemins en clair (écart 5, à porter au
texte), qui sont donc invisibles à `git status` : `fermer` vérifie lui-même qu'aucun ne reste.

**Garde d'ouverture** (`ouvrir`, seule voie d'ouverture des deux paquets ; texte, plan, point 8). Elle relit d'abord le
journal `registres/ouvertures-p3bis-v1.md` (format exact, ordre des ouvertures : après `reduite`, seule `pleine` ou
`pleine-anticipee` ; après `pleine` ou `pleine-anticipee`, aucune : `deja-ouverte`), puis le registre des préalables
`registres/prealables-p3bis-v1.md` (jamais le texte du préenregistrement, jamais le fichier le plus récent par son nom) :
exactement une ligne de chacune des trois clés d'écrit, au plus une `GARDE-ADAPTEE-T07-P3BIS`, `RENDEZ-VOUS-P3BIS-1`, `-2`…
(numéros consécutifs, dates strictement croissantes), sceaux et compagnons vérifiés, dates strictement antérieures à
l'ouverture ; chaque `RENDEZ-VOUS-P3BIS-N` cite `docs/decisions/rendez-vous-P3-bis-vN.md`, qui porte une ligne
`Décision : maintenir|ouvrir|ouvrir pleinement` et une ligne `Date : …`, datée au plus tôt au rendez-vous et au plus tard à sa
ligne. Suite des décisions : « maintenir » peut être suivi de toute décision ; « ouvrir » de rien, sauf d'une seule « ouvrir
pleinement » si une ouverture `reduite` appuyée sur sa ligne est lue au journal, datée avant la ligne suivante ; « ouvrir
pleinement » de rien. Puis le mode demandé :
- `pleine` : lignes `SCORES-T07` et `SONDES-T07` du registre des scellements, bien formées, antérieures, compagnon du fichier
  cité présent et égal, fichier vérifié seulement s'il est présent (D8) ; chemin normal, ou complément de l'ouverture réduite ;
- `reduite` (branche 1) : dernière décision « ouvrir » et garde adaptée en vigueur : `SCELLEMENT-T07` présente et conforme,
  `GARDE-ADAPTEE-T07-P3BIS` qui cite le même texte, toutes deux **strictement** antérieures à la ligne de la décision (CP-17) ;
  sinon refus `garde-adaptee-absente` ou `garde-adaptee-posterieure`, **jamais d'ouverture** (CP-01) ;
- `pleine-anticipee` (branche 2) : dernière décision « ouvrir pleinement » ; T0.7 ne lit plus la course 7b sous son texte
  (nœud de Lazar, déclaré au verdict et transmis à T0.7).
Les deux paquets sont ensuite relus en mémoire (empreintes, sel, taille, flux, morceaux, aucun chemin commun, mêmes paquets
que l'ouverture réduite antérieure s'il y en a une), sinon refus `paquet-faux`.

**Journal** (format exact du texte, plan, point 8, que T0.7 lit) : en tête `| clé | date | mode | appui | paquets | motif |`
et `|---|---|---|---|---|---|`, puis une ligne de six cellules par tentative, en ajout seul. `OUVERTURE-P3BIS` : appui
`SCORES-T07=… SONDES-T07=…` (`pleine`), `RENDEZ-VOUS-P3BIS-N=… GARDE-ADAPTEE-T07-P3BIS=…` (`reduite`),
`RENDEZ-VOUS-P3BIS-N=…` (`pleine-anticipee`), paquets `<sha256 du paquet des lectures> <sha256 du paquet du run>`, motif `-`.
`REFUS-OUVERTURE-P3BIS` : mode demandé, appui présenté (lignes trouvées, dans le même ordre) ou `-`, paquets `-` s'ils n'ont
pas été lus, motif `code : texte` d'un code de `MOTIFS_REFUS`. Toute ligne est vérifiée avant d'être écrite ; le journal
entier est relu à chaque tentative ; un journal hors format donne un refus `ligne-mal-formee` (une ligne neuve de la garde
suit, la ligne fautive n'est jamais corrigée). L'ouverture n'a lieu qu'après l'écriture de sa ligne : un journal impossible
à écrire est un refus (code 2), rien n'est ouvert, et ce refus-là n'a pas de ligne (CP-06).

**Choix déclarés** (codes de la liste fermée ; à porter au texte si la mère le retient) : fichier cité absent → `sceau-faux` ;
fichier de décision autre que celui du numéro, mal formé, daté avant le rendez-vous ou après sa ligne → `ligne-mal-formee` ;
journal hors format → `ligne-mal-formee` ; aucune `SCELLEMENT-T07`, ou garde adaptée citant un autre texte →
`garde-adaptee-absente` ; `SCELLEMENT-T07` ou garde adaptée datée à la ligne de la décision « ouvrir » ou après →
`garde-adaptee-posterieure` ; mode demandé sans la décision qui l'autorise (`reduite` sans dernière décision « ouvrir »,
`pleine-anticipee` sans « ouvrir pleinement ») → `ni-scores-ni-ouvrir` ; `pleine` demandée sous une décision « ouvrir » ou
« ouvrir pleinement » sans lignes de T0.7 conformes → code du premier défaut de ces lignes ; date de la mise en paquet
illisible, paquet illisible ou faux, chemins communs, paquets autres que ceux de l'ouverture réduite → `paquet-faux`. Mode
inconnu et dossier de sortie déjà présent : erreurs d'appel (code 1), avant toute lecture, sans ligne au journal. Une écriture
du dossier de sortie en échec **après** la ligne `OUVERTURE-P3BIS` : arrêt (code 1), rien laissé ; le journal garde
l'ouverture (sens prudent pour T0.7) et l'écart se consigne. Date de la mise en paquet (réserve « écrit après la lecture
fermée ») : `--date-paquet`, sinon `git log` du paquet. La date du rendez-vous est une constante de ce module
(`DATE_RENDEZ_VOUS`) : si elle change, le module change.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import lzma
import os
import re
import secrets
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller, verifier

# --- tailles et noms -------------------------------------------------------------------------------------------------
TAILLE_PAQUET_LECTURES = 16_783_360        # 1 639 × 10 240 octets : multiple de tarfile.RECORDSIZE
TAILLE_CORPS_LECTURES = TAILLE_PAQUET_LECTURES - 3 * tarfile.BLOCKSIZE - 2 * tarfile.BLOCKSIZE   # 16 780 800 octets
TAILLE_LONGUEUR = 8                        # longueur de l'archive comprimée, entier non signé, poids fort en tête (CP-04)
TAILLE_SEL = 32
TAILLE_MORCEAU_MAX = 90_000_000            # « morceaux d'au plus 90 Mo » (GitHub refuse les fichiers de plus de 100 Mo)
NOM_SEL, NOM_CORPS, NOM_SORTIES_RUN = "sel.txt", "corps.bin", "sorties.tar"
PAQUET_LECTURES = "paquet-ferme-v1.tar"
PAQUET_RUN, INDEX_RUN = "paquet-run-ferme-v1.tar", "paquet-run-ferme-v1.json"
ESPACE_DEFAUT = "espace-ferme-p3bis"
DEPLIE = "deplie-run-v1.json"
DUREES = "durees-lectures-v1.json"         # classe 2 : dans le paquet (texte, plan, point 6 ; CP-05)
ERREURS_MISE_EN_PAQUET = "mise-en-paquet.erreurs"   # motif d'un refus de `fermer`, gardé dans l'espace fermé (CP-11)
SONDES_COMPLETES = "sondes-figees.npz"     # fichier complet des sondes (matrices de Mahalanobis) : dans le second paquet
DONNEES_EXIGEES = ("sondes-figees.npz", "sondes-figees-legeres.npz", "scores-p3.npz", "jetons-principales-p3.npz",
                   "textes-actions-p3.jsonl")
DONNEES_LUES = ("scores-p3.npz", "jetons-principales-p3.npz", "textes-actions-p3.jsonl")   # lus par `lecture.charger_source`
EPISODES = "episodes-p3.json"
PRESET_XZ = 6
# --- registres -------------------------------------------------------------------------------------------------------
REGISTRE_PREALABLES = "registres/prealables-p3bis-v1.md"
REGISTRE_SCELLEMENTS = "registres/scellements-v1.md"
JOURNAL_OUVERTURES = "registres/ouvertures-p3bis-v1.md"
CLES_ECRITS = ("ECRIT-PERIMETRE-JEUX-P3BIS", "ECRIT-LANCEMENT-RELANCE-P3BIS", "ECRIT-ENGAGEMENT-ETAPE-A-P3BIS")
CLE_GARDE_ADAPTEE = "GARDE-ADAPTEE-T07-P3BIS"
RENDEZ_VOUS = re.compile(r"RENDEZ-VOUS-P3BIS-([0-9]+)")
SCORES_T07, SONDES_T07, SCELLEMENT_T07 = "SCORES-T07", "SONDES-T07", "SCELLEMENT-T07"
CLES_T07_LUES = (SCORES_T07, SONDES_T07, SCELLEMENT_T07)
DATE_RENDEZ_VOUS = "2026-11-20T12:00:00Z"  # date du texte (proposée, défaut sous 48 heures, R-2021)
FICHIER_DECISION = "docs/decisions/rendez-vous-P3-bis-v{n}.md"
MAINTENIR, OUVRIR, OUVRIR_PLEINEMENT = "maintenir", "ouvrir", "ouvrir pleinement"
DECISION = re.compile(r"^Décision : (maintenir|ouvrir pleinement|ouvrir)$", re.M)
DATE_DECISION = re.compile(r"^Date : (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$", re.M)
# motifs recopiés de `src/controle_ia/t07/registre_v1.py` (`914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0`,
# dernier commit qui le touche `72be6999`, présent à `main` `04a1b392`, l. 39-43) : même format que le registre des
# scellements ; l'essai les compare à ces chaînes recopiées, sans importer T0.7 (CP-15)
SHA = re.compile(r"[0-9a-f]{64}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
CLE = re.compile(r"[A-Z0-9]+(?:-[A-Z0-9]+)+")
FORMAT_DATE = "%Y-%m-%dT%H:%M:%SZ"
# --- journal des ouvertures (texte, plan, point 8) -------------------------------------------------------------------
ENTETE_JOURNAL = ("| clé | date | mode | appui | paquets | motif |", "|---|---|---|---|---|---|")
CLE_OUVERTURE, CLE_REFUS = "OUVERTURE-P3BIS", "REFUS-OUVERTURE-P3BIS"
PLEINE, REDUITE, PLEINE_ANTICIPEE = "pleine", "reduite", "pleine-anticipee"
MODES = (PLEINE, REDUITE, PLEINE_ANTICIPEE)
MODES_FINAUX = (PLEINE, PLEINE_ANTICIPEE)
MOTIFS_REFUS = ("registre-absent", "ligne-absente", "ligne-double", "ligne-mal-formee", "sceau-faux", "compagnon-absent",
                "date-posterieure", "cle-inconnue", "rendez-vous-non-consecutif", "rendez-vous-non-croissant",
                "ligne-apres-decision-finale", "ni-scores-ni-ouvrir", "decision-maintenir", "garde-adaptee-absente",
                "garde-adaptee-posterieure", "deja-ouverte", "paquet-faux")
JETON_APPUI = re.compile(r"([A-Z0-9]+(?:-[A-Z0-9]+)+)=([0-9a-f]{64})")
CLE_RDV_APPUI = re.compile(r"RENDEZ-VOUS-P3BIS-[1-9][0-9]*")
PAQUETS_CELLULE = re.compile(r"[0-9a-f]{64} [0-9a-f]{64}")
MOTIF_CELLULE = re.compile(r"([a-z]+(?:-[a-z]+)*) : (\S.*)")
# --- fichier d'issue (texte, « Critères », « Fichier d'issue ») -------------------------------------------------------
ISSUES = {"non lu": 1, "échec": 2, "non tranché": 3, "vu": 4, "non vu": 5}
CLES_ISSUE = ("issue", "ligne", "verdict", "verdict_sha256")
VERDICT = "docs/verdicts/verdict-P3-bis-v1.md"


class RefusOuverture(GardeArret):
    """Refus de la garde d'ouverture : rien n'est ouvert (code 2 en ligne de commande) ; `code` est un code de
    `MOTIFS_REFUS`, écrit au journal avec le texte, l'appui présenté et les paquets lus."""

    def __init__(self, code: str, texte: str, appui: str = "-", paquets: str = "-"):
        if code not in MOTIFS_REFUS:
            raise ValueError(f"code de refus {code!r} hors de la liste fermée")
        self.code, self.texte, self.appui, self.paquets = code, texte, appui, paquets
        super().__init__(f"{code} : {texte}")


class JournalImpossible(GardeArret):
    """Le journal des ouvertures ne peut pas être écrit : refus, rien n'est ouvert (code 2), aucune ligne (CP-06)."""


def _refuser(fautes: list, appui: str = "-", paquets: str = "-"):
    """Refus du premier défaut relevé (son code) ; le texte porte tous les défauts, les suivants avec leur code."""
    texte = " ; ".join(t if i == 0 else f"[{c}] {t}" for i, (c, t) in enumerate(fautes))
    raise RefusOuverture(fautes[0][0], texte, appui, paquets)


# ================================================================================================= archives et paquets
def _info(nom: str, taille: int) -> tarfile.TarInfo:
    ti = tarfile.TarInfo(nom)
    ti.size, ti.mtime, ti.mode, ti.uid, ti.gid, ti.uname, ti.gname = taille, 0, 0o644, 0, 0, "", ""
    ti.type = tarfile.REGTYPE
    return ti


def tar_de(membres, format_tar=tarfile.USTAR_FORMAT) -> bytes:
    """Archive tar des membres (nom, octets), dans l'ordre donné, métadonnées normalisées : même contenu, mêmes octets."""
    flux = io.BytesIO()
    with tarfile.open(fileobj=flux, mode="w", format=format_tar, encoding="utf-8") as tf:
        for nom, octets in membres:
            tf.addfile(_info(nom, len(octets)), io.BytesIO(octets))
    return flux.getvalue()


def membres_de(octets: bytes) -> list[tuple[str, bytes]]:
    """Membres (nom, octets) d'une archive tar, fichiers ordinaires seulement ; noms relatifs sans « .. », sans double."""
    sortie = []
    try:
        with tarfile.open(fileobj=io.BytesIO(octets), mode="r:", encoding="utf-8") as tf:
            for m in tf:
                if not m.isreg():
                    raise GardeArret(f"archive : membre {m.name!r} qui n'est pas un fichier ordinaire")
                if not m.name or m.name.startswith("/") or ".." in Path(m.name).parts:
                    raise GardeArret(f"archive : nom de membre {m.name!r} refusé")
                donnees = tf.extractfile(m).read()
                if len(donnees) != m.size:
                    raise GardeArret(f"archive : membre {m.name!r} tronqué")
                sortie.append((m.name, donnees))
    except (tarfile.TarError, OSError, EOFError) as e:
        raise GardeArret(f"archive illisible ({type(e).__name__}: {e})") from None
    noms = [n for n, _ in sortie]
    if len(set(noms)) != len(noms):
        raise GardeArret("archive : nom de membre en double")
    return sortie


def archive_des_fichiers(racine: Path, chemins) -> bytes:
    """Archive pax, déterministe, des fichiers nommés (chemins relatifs à la racine, triés)."""
    racine = Path(racine)
    return tar_de([(c, (racine / c).read_bytes()) for c in sorted(chemins)], tarfile.PAX_FORMAT)


def comprimer(octets: bytes) -> bytes:
    return lzma.compress(octets, format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=PRESET_XZ)


def decomprimer(octets: bytes, bourre_permise: bool) -> tuple[bytes, bytes]:
    """Flux xz en tête des octets : (archive, octets qui le suivent) ; flux illisible ou tronqué : garde."""
    d = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
    try:
        archive = d.decompress(octets)
    except lzma.LZMAError as e:
        raise GardeArret(f"flux xz illisible ({e})") from None
    if not d.eof:
        raise GardeArret("flux xz tronqué")
    if d.unused_data and not bourre_permise:
        raise GardeArret("octets après le flux xz, alors qu'aucune bourre n'est permise")
    return archive, d.unused_data


def tirer_sel() -> bytes:
    return secrets.token_bytes(TAILLE_SEL)


def tirer_bourre(n: int) -> bytes:
    return secrets.token_bytes(n)


def derives_de_l_entropie(entropie: int) -> set[bytes]:
    """Sels qu'on recalculerait depuis l'entropie citée (publique) : refusés à la relecture."""
    e = int(entropie)
    d = {hashlib.sha256(str(e).encode()).digest(), np.random.default_rng(e).bytes(TAILLE_SEL),
         np.random.SeedSequence(e).generate_state(8, np.uint32).tobytes()}
    if 0 <= e < 2 ** 256:
        d |= {e.to_bytes(32, "big"), e.to_bytes(32, "little"), hashlib.sha256(e.to_bytes(32, "big")).digest()}
    return d


def exiger_sel(sel: bytes, entropie: int | None) -> None:
    if len(sel) != TAILLE_SEL:
        raise GardeArret(f"sel absent ou de {len(sel)} octets ({TAILLE_SEL} attendus)")
    if sel == bytes(TAILLE_SEL):
        raise GardeArret("sel nul")
    if entropie is not None and sel in derives_de_l_entropie(entropie):
        raise GardeArret("sel dérivé de l'entropie citée : refusé")


def corps_lectures(archive: bytes) -> bytes:
    """Longueur L du flux sur 8 octets (poids fort en tête), flux xz de l'archive des sorties, puis la bourre, jusqu'à
    `TAILLE_CORPS_LECTURES` octets exactement (texte, plan, point 6 ; CP-04)."""
    flux = comprimer(archive)
    place = TAILLE_CORPS_LECTURES - TAILLE_LONGUEUR
    if len(flux) > place:
        raise GardeArret(f"sorties trop grosses pour la taille fixe : {len(flux)} octets comprimés, {place} au plus")
    return len(flux).to_bytes(TAILLE_LONGUEUR, "big") + flux + tirer_bourre(place - len(flux))


def lire_corps(corps: bytes) -> bytes:
    """Archive des sorties d'un corps : taille fixe, longueur dans ses bornes, flux fini exactement après elle."""
    exiger_taille_corps(corps)
    n = int.from_bytes(corps[:TAILLE_LONGUEUR], "big")
    if not 0 < n <= TAILLE_CORPS_LECTURES - TAILLE_LONGUEUR:
        raise GardeArret(f"paquet des lectures : longueur de l'archive comprimée {n} hors de ]0 ; "
                         f"{TAILLE_CORPS_LECTURES - TAILLE_LONGUEUR}]")
    archive, _ = decomprimer(corps[TAILLE_LONGUEUR:TAILLE_LONGUEUR + n], bourre_permise=False)
    return archive


def paquet_lectures(archive: bytes, sel: bytes) -> bytes:
    return tar_de([(NOM_SEL, sel), (NOM_CORPS, corps_lectures(archive))])


def exiger_taille_lectures(octets: bytes) -> None:
    if len(octets) != TAILLE_PAQUET_LECTURES:
        raise GardeArret(f"paquet des lectures de {len(octets)} octets, {TAILLE_PAQUET_LECTURES} exigés")


def exiger_taille_corps(corps: bytes) -> None:
    if len(corps) != TAILLE_CORPS_LECTURES:
        raise GardeArret(f"paquet des lectures : corps de {len(corps)} octets, {TAILLE_CORPS_LECTURES} exigés")


def relire_paquet_lectures(octets: bytes, entropie: int | None = None) -> tuple[bytes, bytes]:
    """(sel, archive des sorties) d'un paquet des lectures ; taille, membres, sel, longueur et flux contrôlés."""
    exiger_taille_lectures(octets)
    m = membres_de(octets)
    if [n for n, _ in m] != [NOM_SEL, NOM_CORPS]:
        raise GardeArret(f"paquet des lectures : membres {[n for n, _ in m]}, {[NOM_SEL, NOM_CORPS]} attendus")
    sel, corps = m[0][1], m[1][1]
    exiger_sel(sel, entropie)
    return sel, lire_corps(corps)


def paquet_run(archive: bytes, sel: bytes) -> bytes:
    return tar_de([(NOM_SEL, sel), (NOM_SORTIES_RUN, archive)])


def relire_paquet_run(octets: bytes) -> tuple[bytes, bytes]:
    m = membres_de(octets)
    if [n for n, _ in m] != [NOM_SEL, NOM_SORTIES_RUN]:
        raise GardeArret(f"second paquet : membres {[n for n, _ in m]}, {[NOM_SEL, NOM_SORTIES_RUN]} attendus")
    exiger_sel(m[0][1], None)
    return m[0][1], m[1][1]


def fichiers_lus(run: str) -> tuple[str, ...]:
    """Fichiers du second paquet que lisent les lectures (dépliés dans le clone fermé), avec leurs compagnons."""
    base = [f"donnees/{run}/{n}" for n in DONNEES_LUES] + [f"diag/{run}/{EPISODES}"]
    return tuple(sorted(base + [c + ".sha256" for c in base]))


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def _ecrire_neuf(chemin: Path, octets: bytes) -> None:
    if chemin.exists() or Path(str(chemin) + ".sha256").exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_bytes(octets)


def exclure_localement(racine: Path, motifs) -> None:
    """Ajoute des motifs à `.git/info/exclude` du clone (local, jamais commité) ; hors d'un clone git : garde."""
    r = subprocess.run(["git", "-C", str(racine), "rev-parse", "--git-path", "info/exclude"], capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeArret(f"{racine} n'est pas un clone git ({r.stderr.strip()})")
    chemin = Path(r.stdout.strip())
    if not chemin.is_absolute():
        chemin = Path(racine) / chemin
    chemin.parent.mkdir(parents=True, exist_ok=True)
    deja = set(chemin.read_text(encoding="utf-8").splitlines()) if chemin.exists() else set()
    with open(chemin, "a", encoding="utf-8") as f:
        for m in motifs:
            if m not in deja:                   # un motif répété dans le même appel n'est écrit qu'une fois
                f.write(m + "\n")
                deja.add(m)


def _suivis(racine: Path, chemins) -> list[str]:
    """Chemins suivis par git, dans l'index ou dans le commit courant."""
    suivis = set()
    for args in (["ls-files", "--"], ["ls-tree", "-r", "--name-only", "HEAD", "--"]):
        r = subprocess.run(["git", "-C", str(racine), *args, *chemins], capture_output=True, text=True)
        if r.returncode != 0 and "HEAD" not in args:
            raise GardeArret(f"git {' '.join(args)} impossible : {r.stderr.strip()}")
        suivis |= {x for x in r.stdout.splitlines() if x}
    return sorted(suivis)


# ================================================================================================= second paquet
def fichiers_du_run(racine: Path, run: str, partiel: bool = False) -> list[str]:
    """`donnees/<run>/` entier (fichier complet des sondes compris) et `diag/<run>/episodes-p3.json` avec son compagnon ;
    hors du mode partiel (arrêt du run), les fichiers du run complet sont exigés et vérifiés par leurs compagnons."""
    racine = Path(racine)
    d = racine / "donnees" / run
    chemins = []
    if d.is_dir():
        chemins = [str(p.relative_to(racine)) for p in sorted(d.rglob("*")) if p.is_file()]
    for n in (EPISODES, EPISODES + ".sha256"):
        if (racine / "diag" / run / n).is_file():
            chemins.append(f"diag/{run}/{n}")
    if not partiel:
        exiges = [f"donnees/{run}/{n}" for n in DONNEES_EXIGEES] + [f"diag/{run}/{EPISODES}"]
        manquants = [c for c in exiges if c not in chemins or c + ".sha256" not in chemins]
        if manquants:
            raise GardeArret(f"second paquet : fichiers du run absents ou sans compagnon : {manquants}")
        for c in exiges:
            verifier(racine / c)
    return sorted(chemins)


def fermer_run(racine, run: str, partiel: bool = False, taille_morceau: int = TAILLE_MORCEAU_MAX) -> dict | None:
    """Second paquet, sur l'instance, avant toute poussée : morceaux scellés et index scellé sous `diag/<run>/`, relecture
    vérifiée (chaque fichier redonné à l'octet) ; les épisodes en clair exclus localement de git. Rend l'index (None en mode
    partiel s'il n'y a rien à fermer)."""
    racine = Path(racine)
    if not 0 < int(taille_morceau) <= TAILLE_MORCEAU_MAX:
        raise GardeArret(f"taille de morceau {taille_morceau} hors de ]0 ; {TAILLE_MORCEAU_MAX}]")
    exclure_localement(racine, [f"/diag/{run}/{EPISODES}", f"/diag/{run}/{EPISODES}.sha256"])   # d'abord : jamais ajoutés
    chemins = fichiers_du_run(racine, run, partiel)
    if not chemins:
        return None
    dossier = racine / "diag" / run
    if list(dossier.glob(PAQUET_RUN + "*")) or (dossier / INDEX_RUN).exists():
        raise GardeArret(f"second paquet de {run} déjà présent (R12)")
    archive = archive_des_fichiers(racine, chemins)
    ecrits = []
    try:
        octets = paquet_run(archive, tirer_sel())
        morceaux = []
        for k, debut in enumerate(range(0, len(octets), int(taille_morceau))):
            nom = f"{PAQUET_RUN}.{k:03d}"
            ecrits.append(dossier / nom)
            _ecrire_neuf(dossier / nom, octets[debut:debut + int(taille_morceau)])
            morceaux.append({"nom": nom, "sha256": sceller(dossier / nom), "taille": (dossier / nom).stat().st_size})
        index = {"version": 1, "run": run, "paquet": PAQUET_RUN, "sha256": _sha(octets), "taille": len(octets),
                 "taille_morceau_max": int(taille_morceau), "morceaux": morceaux}
        ecrits.append(dossier / INDEX_RUN)
        _ecrire_neuf(dossier / INDEX_RUN, (json.dumps(index, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode())
        sceller(dossier / INDEX_RUN)
        relu = relire_run(racine, run)
        if relu != {c: (racine / c).read_bytes() for c in chemins}:
            raise GardeArret("second paquet : la relecture ne redonne pas les fichiers du run à l'octet")
    except BaseException:
        for f in ecrits:                        # morceaux et index retirés : le paquet se refait (le run n'est pas rejoué)
            f.unlink(missing_ok=True)
            Path(str(f) + ".sha256").unlink(missing_ok=True)
        raise
    return index


def relire_run(racine, run: str) -> dict[str, bytes]:
    """Fichiers du second paquet (chemin → octets), après contrôle de l'index, des morceaux et du paquet."""
    racine = Path(racine)
    dossier = racine / "diag" / run
    verifier(dossier / INDEX_RUN)
    try:
        index = json.loads((dossier / INDEX_RUN).read_text(encoding="utf-8"))
        morceaux = list(index["morceaux"])
        noms = [m["nom"] for m in morceaux]
        [(str(m["sha256"]), int(m["taille"])) for m in morceaux]
        int(index["taille"]), str(index["sha256"])
    except (ValueError, KeyError, TypeError, AttributeError):
        raise GardeArret(f"index du second paquet de {run} illisible") from None
    if index.get("version") != 1 or index.get("run") != run or index.get("paquet") != PAQUET_RUN:
        raise GardeArret(f"index du second paquet de {run} d'une autre version, d'un autre run ou d'un autre paquet")
    if not morceaux or noms != [f"{PAQUET_RUN}.{k:03d}" for k in range(len(morceaux))]:
        raise GardeArret("second paquet : noms des morceaux non consécutifs")
    octets = b""
    for m in morceaux:
        if verifier(dossier / m["nom"]) != m["sha256"]:
            raise GardeArret(f"second paquet : morceau {m['nom']} d'empreinte autre que celle de l'index")
        b = (dossier / m["nom"]).read_bytes()
        if len(b) > TAILLE_MORCEAU_MAX or len(b) != m["taille"]:
            raise GardeArret(f"second paquet : morceau {m['nom']} de {len(b)} octets (au plus {TAILLE_MORCEAU_MAX})")
        octets += b
    if _sha(octets) != index["sha256"] or len(octets) != index["taille"]:
        raise GardeArret("second paquet : morceaux réunis d'empreinte ou de taille autre que celle de l'index")
    _, archive = relire_paquet_run(octets)
    fichiers = dict(membres_de(archive))
    permis = (f"donnees/{run}/", f"diag/{run}/{EPISODES}")
    if any(not (c.startswith(permis[0]) or c in (permis[1], permis[1] + ".sha256")) for c in fichiers):
        raise GardeArret("second paquet : chemin hors de donnees/<run>/ et des épisodes")
    return fichiers


def exiger_aucun_clair(racine, run: str) -> None:
    """Avant toute poussée : aucun fichier de `donnees/<run>/` ni les épisodes en clair dans l'index ou le commit."""
    suivis = _suivis(Path(racine), [f"donnees/{run}", f"diag/{run}/{EPISODES}", f"diag/{run}/{EPISODES}.sha256"])
    if suivis:
        raise GardeArret(f"fichiers du run suivis en clair : {suivis}")


def deplier_run(racine, run: str, espace: str = ESPACE_DEFAUT) -> list[str]:
    """Dans le clone fermé, avant les lectures : fichiers lus du second paquet (`fichiers_lus`) dépliés aux chemins
    d'origine (aucun chemin présent ni suivi), compagnons relus, chemins exclus localement de git, liste écrite dans
    l'espace fermé."""
    racine = Path(racine)
    fichiers = {c: b for c, b in relire_run(racine, run).items() if c in fichiers_lus(run)}
    suivis = _suivis(racine, sorted(fichiers))
    presents = [c for c in fichiers if (racine / c).exists()]
    if suivis or presents:
        raise GardeArret(f"second paquet : chemins déjà suivis ou présents (R12) : {sorted(set(suivis) | set(presents))}")
    exclure_localement(racine, [f"/diag/{run}/{EPISODES}", f"/diag/{run}/{EPISODES}.sha256", f"/{espace}/"])
    ecrits = []
    try:
        for c, octets in sorted(fichiers.items()):
            (racine / c).parent.mkdir(parents=True, exist_ok=True)
            (racine / c).write_bytes(octets)
            ecrits.append(c)
        for c in fichiers:
            if c + ".sha256" in fichiers:
                verifier(racine / c)
    except BaseException:
        for c in ecrits:                        # rien ne reste en clair d'un dépliage refusé
            (racine / c).unlink(missing_ok=True)
        raise
    (racine / espace).mkdir(parents=True, exist_ok=True)
    (racine / espace / DEPLIE).write_text(json.dumps({"run": run, "fichiers": sorted(fichiers)}, ensure_ascii=False) + "\n",
                                          encoding="utf-8")
    return sorted(fichiers)


# ================================================================================================= paquet des lectures
def dossier_ferme(run: str) -> str:
    return f"diag/p3bis-ferme-{run}"


def sorties_des_lectures(racine: Path, lectures, espace: str) -> list[str]:
    racine = Path(racine)
    chemins = []
    for base in [f"runs/{x}" for x in lectures] + [f"diag/{x}" for x in lectures] + [espace]:
        d = racine / base
        if d.is_dir():
            chemins += [str(p.relative_to(racine)) for p in sorted(d.rglob("*")) if p.is_file()]
    return sorted(chemins)


def fermer(racine, run: str, lectures, espace: str = ESPACE_DEFAUT, entropie: int | None = None,
           imprimer=print) -> str:
    """Paquet des lectures : sorties des deux lectures et de l'espace fermé, sel, longueur, flux comprimé, bourre ;
    relecture ; effacement des fichiers en clair et des fichiers dépliés du second paquet ; compagnon ; seule l'empreinte
    est imprimée."""
    racine = Path(racine)
    chemins = sorties_des_lectures(racine, lectures, espace)
    if not chemins:
        raise GardeArret("aucune sortie de lecture à fermer")
    deplies = []
    if (racine / espace / DEPLIE).is_file():
        deplies = json.loads((racine / espace / DEPLIE).read_text(encoding="utf-8"))["fichiers"]
    cible = racine / dossier_ferme(run) / PAQUET_LECTURES
    if cible.exists() or Path(str(cible) + ".sha256").exists():
        raise GardeArret(f"{cible} existe déjà (R12)")
    archive = archive_des_fichiers(racine, chemins)
    sel = tirer_sel()
    exiger_sel(sel, entropie)
    octets = paquet_lectures(archive, sel)
    exiger_taille_lectures(octets)
    _ecrire_neuf(cible, octets)
    try:
        sel_relu, archive_relue = relire_paquet_lectures(cible.read_bytes(), entropie)
        if sel_relu != sel or archive_relue != archive:
            raise GardeArret("paquet des lectures : la relecture ne redonne ni le sel ni l'archive")
        if dict(membres_de(archive_relue)) != {c: (racine / c).read_bytes() for c in chemins}:
            raise GardeArret("paquet des lectures : la relecture ne redonne pas les sorties à l'octet")
    except BaseException:
        cible.unlink(missing_ok=True)           # paquet non scellé retiré : la mise en paquet se refait sur les mêmes fichiers
        raise
    for c in chemins + list(deplies):
        p = racine / c
        if p.is_file():
            p.unlink()
    for base in [f"runs/{x}" for x in lectures] + [f"diag/{x}" for x in lectures] + [espace]:
        if (racine / base).is_dir():
            shutil.rmtree(racine / base)
    for c in deplies:                           # dossiers laissés vides par les fichiers dépliés (donnees/<run>/)
        parent = (racine / c).parent
        while parent != racine and parent.is_dir() and not any(parent.iterdir()):
            parent.rmdir()
            parent = parent.parent
    restes = [c for c in chemins + list(deplies) if (racine / c).exists()]
    if restes:
        raise GardeArret(f"fichiers en clair restés dans le clone : {restes}")
    sha = sceller(cible)
    imprimer(sha)
    return sha


def commandes_des_lectures(run: str, lecture: str, lecture_c: str, prereg: str | None, entropie: int | None) -> list:
    """Commandes des points 3 et 4 du plan (le lanceur Python courant)."""
    fin = (["--prereg", prereg] if prereg is not None else []) + (["--entropie", str(entropie)] if entropie is not None else [])
    return [("lecture de P3", "lecture-p3", [sys.executable, "-m", "controle_ia.premier_test_ia.lecture", "--run-source", run,
                                              "--run-lecture", lecture, *fin]),
            ("lecture complémentaire", "lecture-p3bis",
             [sys.executable, "-m", "controle_ia.premier_test_ia.lecture_p3bis_v1", "--run-source", run, "--lecture",
              lecture, "--run-lecture", lecture_c, *fin])]


def _propre(texte) -> str:
    """Texte d'une cellule ou d'une ligne : ni `|` ni saut de ligne."""
    return " ".join(str(texte).replace("|", "¦").split()) or "sans texte"


def lectures_fermees(racine, run: str, lecture: str, lecture_c: str, prereg: str | None = None,
                     entropie: int | None = None, espace: str = ESPACE_DEFAUT, imprimer=print) -> int:
    """Clone fermé : dépliage, deux lectures (sorties redirigées dans l'espace fermé), durées écrites dans l'espace fermé,
    mise en paquet ; n'imprime que les codes de sortie, le motif d'un refus du dépliage (il ne porte que sur l'intégrité du
    second paquet) et l'empreinte du paquet. Code 0 si chaque étape rend 0. Mode décisif (`prereg`) : entropie exigée."""
    racine = Path(racine)
    if prereg is not None and entropie is None:
        raise GardeArret("lectures fermées en mode décisif (--prereg) sans --entropie : refusé (garde du sel, CP-17)")
    exclure_localement(racine, [f"/runs/{lecture}/", f"/diag/{lecture}/", f"/runs/{lecture_c}/", f"/diag/{lecture_c}/",
                                f"/{espace}/"])
    codes, durees = [], {}
    debut = time.monotonic()
    try:
        deplier_run(racine, run, espace)
        codes.append(("dépliage du second paquet", 0))
    except GardeArret as e:
        imprimer("code dépliage du second paquet : 1")
        imprimer(f"motif du dépliage : {_propre(e)}")
        return 1
    durees["depliage_s"] = round(time.monotonic() - debut, 3)
    for nom, fichier, commande in commandes_des_lectures(run, lecture, lecture_c, prereg, entropie):
        t0 = time.monotonic()
        with open(racine / espace / f"{fichier}.sortie", "wb") as so, open(racine / espace / f"{fichier}.erreurs", "wb") as se:
            r = subprocess.run(commande, cwd=str(racine), stdout=so, stderr=se, stdin=subprocess.DEVNULL)
        durees[f"{fichier}_s"] = round(time.monotonic() - t0, 3)
        codes.append((nom, r.returncode))
    durees["chaine_avant_mise_en_paquet_s"] = round(time.monotonic() - debut, 3)
    (racine / espace / DUREES).write_text(json.dumps({"version": 1, "durees": durees, "codes": dict(codes)},
                                                     ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sortie_fermer = []
    try:
        fermer(racine, run, [lecture, lecture_c], espace, entropie, imprimer=sortie_fermer.append)
        codes.append(("mise en paquet", 0))
    except GardeArret as e:
        (racine / espace).mkdir(parents=True, exist_ok=True)     # l'espace reste en place quand `fermer` échoue (CP-11)
        with open(racine / espace / ERREURS_MISE_EN_PAQUET, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now(timezone.utc).strftime(FORMAT_DATE)} {_propre(e)}\n")
        codes.append(("mise en paquet", 1))
    for nom, code in codes:
        imprimer(f"code {nom} : {code}")
    if sortie_fermer:
        imprimer(f"paquet des lectures : {sortie_fermer[0]}")
    return 0 if all(c == 0 for _, c in codes) else 1


# ================================================================================================= dates
def instant_utc(date: str) -> int:
    """Instant d'une date `AAAA-MM-JJTHH:MM:SSZ` ; forme ou date impossible : garde (le code de refus est mis par
    l'appelant)."""
    if not isinstance(date, str) or not DATE.fullmatch(date):
        raise GardeArret(f"date {date!r} (AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)")
    try:
        return int(datetime.strptime(date, FORMAT_DATE).replace(tzinfo=timezone.utc).timestamp())
    except ValueError:
        raise GardeArret(f"date {date!r} impossible") from None


def date_utc(instant: int) -> str:
    return datetime.fromtimestamp(int(instant), timezone.utc).strftime(FORMAT_DATE)


# ================================================================================================= journal des ouvertures
def _jeton_appui(jeton: str) -> tuple[str, str]:
    m = JETON_APPUI.fullmatch(jeton)
    if m is None:
        raise GardeArret(f"appui : jeton {jeton!r} (CLÉ=sha256 attendu)")
    cle = m.group(1)
    if not (cle in (SCORES_T07, SONDES_T07, CLE_GARDE_ADAPTEE) or CLE_RDV_APPUI.fullmatch(cle)):
        raise GardeArret(f"appui : clé {cle!r} inconnue")
    return cle, m.group(2)


def _forme_appui(mode: str, cles: list[str]) -> bool:
    """Clés de l'appui d'une ouverture, dans l'ordre du texte, selon le mode."""
    if mode == PLEINE:
        return cles == [SCORES_T07, SONDES_T07]
    if mode == REDUITE:
        return len(cles) == 2 and bool(CLE_RDV_APPUI.fullmatch(cles[0])) and cles[1] == CLE_GARDE_ADAPTEE
    return len(cles) == 1 and bool(CLE_RDV_APPUI.fullmatch(cles[0]))


def lire_ligne_journal(brute: str) -> dict:
    """Une ligne de tentative du journal, au format exact du texte (plan, point 8) ; sinon garde (motif écrit)."""
    if "\n" in brute or "\r" in brute or not (brute.startswith("|") and brute.endswith("|")):
        raise GardeArret("ligne qui ne commence ou ne finit pas par « | »")
    c = [x.strip() for x in brute[1:-1].split("|")]
    if len(c) != 6:
        raise GardeArret(f"{len(c)} cellules, 6 attendues")
    cle, date, mode, appui, paquets, motif = c
    if cle not in (CLE_OUVERTURE, CLE_REFUS):
        raise GardeArret(f"clé {cle!r} inconnue ({CLE_OUVERTURE} ou {CLE_REFUS})")
    instant = instant_utc(date)
    if mode not in MODES:
        raise GardeArret(f"mode {mode!r} inconnu ({', '.join(MODES)})")
    jetons = [] if appui == "-" else [_jeton_appui(j) for j in appui.split(" ")]
    if cle == CLE_OUVERTURE:
        if not _forme_appui(mode, [k for k, _ in jetons]):
            raise GardeArret(f"appui {appui!r} hors de la forme du mode {mode}")
        if not PAQUETS_CELLULE.fullmatch(paquets):
            raise GardeArret(f"paquets {paquets!r} (deux empreintes séparées par une espace attendues)")
        if motif != "-":
            raise GardeArret(f"motif {motif!r} d'une ouverture (« - » attendu)")
    else:
        if paquets != "-" and not PAQUETS_CELLULE.fullmatch(paquets):
            raise GardeArret(f"paquets {paquets!r} d'un refus (« - » ou deux empreintes attendus)")
        m = MOTIF_CELLULE.fullmatch(motif)
        if m is None or m.group(1) not in MOTIFS_REFUS:
            raise GardeArret(f"motif {motif!r} (code de la liste fermée, « : », texte attendus)")
    return {"cle": cle, "date": date, "instant": instant, "mode": mode, "appui": appui, "jetons": jetons,
            "paquets": paquets, "motif": motif}


def exiger_format_journal(texte: str) -> list[dict]:
    """Journal entier au format exact : les deux lignes d'en-tête, puis une ligne de six cellules par tentative, chaque ligne
    finie par un saut de ligne ; ordre permis des ouvertures. Rend les lignes ; sinon garde (tous les défauts écrits)."""
    if texte == "":
        return []
    fautes = []
    lignes = texte.split("\n")
    if lignes[-1] != "":
        fautes.append("dernière ligne sans saut de ligne")
    else:
        lignes = lignes[:-1]
    if tuple(lignes[:2]) != ENTETE_JOURNAL:
        fautes.append("en-tête autre que les deux lignes fixées")
    sortie = []
    for n, brute in enumerate(lignes[2:], start=3):
        try:
            sortie.append(lire_ligne_journal(brute))
        except GardeArret as e:
            fautes.append(f"ligne {n} : {e}")
    etat = None
    for x in sortie:
        if x["cle"] != CLE_OUVERTURE:
            continue
        if etat in MODES_FINAUX or (etat == REDUITE and x["mode"] == REDUITE):
            fautes.append(f"ordre interdit : ouverture {x['mode']} du {x['date']} après une ouverture {etat}")
        etat = x["mode"] if etat not in MODES_FINAUX else etat
    if fautes:
        raise GardeArret("journal des ouvertures hors format : " + " ; ".join(fautes))
    return sortie


def lire_journal(chemin: Path) -> list[dict]:
    """Lignes du journal (absent : aucune) ; hors format : refus `ligne-mal-formee`."""
    chemin = Path(chemin)
    if not chemin.exists():
        return []
    try:
        return exiger_format_journal(chemin.read_text(encoding="utf-8"))
    except (GardeArret, OSError, UnicodeDecodeError) as e:
        raise RefusOuverture("ligne-mal-formee", str(e)) from None


def ligne_journal(cle: str, instant: int, mode: str, appui: str, paquets: str, motif: str) -> str:
    """Ligne de tentative, vérifiée au format exact avant d'être écrite (le module vérifie le format qu'il écrit)."""
    brute = "| " + " | ".join([cle, date_utc(instant), mode, appui, paquets, motif]) + " |"
    lire_ligne_journal(brute)
    return brute


def inscrire(racine: Path, brute: str) -> None:
    """Ajoute une ligne au journal (créé avec ses deux lignes d'en-tête) ; impossible : `JournalImpossible`."""
    lire_ligne_journal(brute)
    j = Path(racine) / JOURNAL_OUVERTURES
    if not j.parent.is_dir():
        raise JournalImpossible(f"dossier {j.parent} absent")
    try:
        neuf = not j.exists() or j.stat().st_size == 0
        avant = b"" if neuf else j.read_bytes()
        with open(j, "a", encoding="utf-8") as f:
            if neuf:
                f.write("\n".join(ENTETE_JOURNAL) + "\n")
            elif not avant.endswith(b"\n"):
                f.write("\n")
            f.write(brute + "\n")
        if not j.read_text(encoding="utf-8").endswith(brute + "\n"):
            raise OSError("ligne non relue en fin de journal")
    except OSError as e:
        raise JournalImpossible(f"{j} : {e}") from None


# ================================================================================================= registres
def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def _ligne_stricte(cle: str, c: list[str], fautes: list, registre: str) -> dict | None:
    if len(c) != 4:
        fautes.append(("ligne-mal-formee", f"ligne {cle} du {registre} mal formée ({len(c)} colonnes, 4 attendues)"))
        return None
    _, date, chemin, sha = c
    try:
        instant = instant_utc(date)
    except GardeArret as e:
        fautes.append(("ligne-mal-formee", f"ligne {cle} du {registre} mal formée : {e}"))
        return None
    if not SHA.fullmatch(sha):
        fautes.append(("ligne-mal-formee", f"ligne {cle} du {registre} mal formée : empreinte {sha!r}"))
        return None
    if not chemin or chemin.startswith("/") or ".." in Path(chemin).parts:
        fautes.append(("ligne-mal-formee", f"ligne {cle} du {registre} mal formée : chemin {chemin!r}"))
        return None
    return {"cle": cle, "date": date, "instant": instant, "chemin": chemin, "sha256": sha}


def lire_prealables(chemin: Path) -> dict:
    """Lignes du registre des préalables ; tous les défauts de forme sont relevés, puis rendus ensemble (code du premier)."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise RefusOuverture("registre-absent", f"registre des préalables {REGISTRE_PREALABLES} absent")
    fautes, ecrits, gardes, rdv = [], {k: [] for k in CLES_ECRITS}, [], []
    for brute in chemin.read_text(encoding="utf-8").splitlines():
        if not brute.strip().startswith("|"):
            continue
        c = _cellules(brute)
        c0 = c[0] if c else ""
        m = RENDEZ_VOUS.fullmatch(c0)
        if c0 in CLES_ECRITS or c0 == CLE_GARDE_ADAPTEE or m:
            ligne = _ligne_stricte(c0, c, fautes, "registre des préalables")
            if ligne is None:
                continue
            if c0 in CLES_ECRITS:
                ecrits[c0].append(ligne)
            elif c0 == CLE_GARDE_ADAPTEE:
                gardes.append(ligne)
            else:
                ligne["numero_texte"] = m.group(1)
                rdv.append(ligne)
        elif CLE.fullmatch(c0):
            fautes.append(("cle-inconnue", f"clé inconnue {c0} au registre des préalables"))
        elif len(c) == 4 and DATE.fullmatch(c[1]):
            fautes.append(("ligne-mal-formee", f"ligne {c0!r} au registre des préalables : la première cellule n'a pas la "
                                               f"forme d'une clé"))
    for k, lignes in ecrits.items():
        if not lignes:
            fautes.append(("ligne-absente", f"0 ligne {k}, exactement une attendue"))
        elif len(lignes) > 1:
            fautes.append(("ligne-double", f"{len(lignes)} lignes {k}, exactement une attendue"))
    if len(gardes) > 1:
        fautes.append(("ligne-double", f"{len(gardes)} lignes {CLE_GARDE_ADAPTEE}, au plus une attendue"))
    numeros = [x["numero_texte"] for x in rdv]
    if numeros != [str(n) for n in range(1, len(rdv) + 1)]:
        fautes.append(("rendez-vous-non-consecutif", f"numéros de rendez-vous {numeros} : consécutifs depuis 1, dans "
                                                     f"l'ordre, attendus"))
    if any(rdv[k]["instant"] >= rdv[k + 1]["instant"] for k in range(len(rdv) - 1)):
        fautes.append(("rendez-vous-non-croissant", "dates des lignes de rendez-vous non strictement croissantes"))
    if fautes:
        _refuser(fautes)
    return {"ecrits": {k: v[0] for k, v in ecrits.items()}, "garde": gardes[0] if gardes else None, "rendez_vous": rdv}


def lire_scellements_t07(chemin: Path) -> dict:
    """Lignes `SCORES-T07`, `SONDES-T07`, `SCELLEMENT-T07` du registre des scellements (les autres clés sont celles de T0.6,
    de T0.7 et de P3-bis : ni lues ni jugées ici) ; une ligne de ces clés mal formée ou en double : refus."""
    chemin = Path(chemin)
    if not chemin.is_file():
        return {}
    trouvees, fautes = {k: [] for k in CLES_T07_LUES}, []
    for brute in chemin.read_text(encoding="utf-8").splitlines():
        if not brute.strip().startswith("|"):
            continue
        c = _cellules(brute)
        if c and c[0] in trouvees:
            ligne = _ligne_stricte(c[0], c, fautes, "registre des scellements")
            if ligne is not None:
                trouvees[c[0]].append(ligne)
    for k, v in trouvees.items():
        if len(v) > 1:
            fautes.append(("ligne-double", f"{len(v)} lignes {k} au registre des scellements, une au plus attendue"))
    if fautes:
        _refuser(fautes)
    return {k: v[0] for k, v in trouvees.items() if v}


def _sha_fichier(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _premier_mot(chemin: Path) -> str:
    return (Path(chemin).read_text(encoding="utf-8").split() or [""])[0]


def sceau_conforme(chemin: Path, attendu: str, cle: str) -> list:
    """Fichier présent, compagnon présent et égal, empreinte égale à celle de la ligne ; défauts (code, texte)."""
    chemin = Path(chemin)
    if not chemin.is_file():
        return [("sceau-faux", f"ligne {cle} : fichier cité {chemin} absent")]
    comp = Path(str(chemin) + ".sha256")
    if not comp.is_file():
        return [("compagnon-absent", f"ligne {cle} : {chemin} sans compagnon .sha256")]
    sha = _sha_fichier(chemin)
    lu = _premier_mot(comp)
    if lu != sha:
        return [("sceau-faux", f"ligne {cle} : compagnon de {chemin} ({lu[:12]}…) ≠ empreinte du fichier ({sha[:12]}…)")]
    if sha != attendu:
        return [("sceau-faux", f"ligne {cle} : {chemin} d'empreinte {sha[:12]}… ≠ celle du registre ({attendu[:12]}…)")]
    return []


def _anterieure(ligne: dict, instant: int) -> list:
    if ligne["instant"] < int(instant):
        return []
    return [("date-posterieure", f"ligne {ligne['cle']} datée {ligne['date']}, pas strictement antérieure à l'ouverture "
                                 f"({date_utc(instant)})")]


def lire_decision(racine: Path, ligne: dict, n: int) -> tuple[dict | None, list]:
    """Décision écrite que cite la ligne `RENDEZ-VOUS-P3BIS-n` : fichier du même numéro, scellé, une ligne `Décision : …`
    (trois décisions) et une ligne `Date : …`, datée au plus tôt au rendez-vous et au plus tard à sa ligne."""
    attendu = FICHIER_DECISION.format(n=n)
    if ligne["chemin"] != attendu:
        return None, [("ligne-mal-formee", f"ligne {ligne['cle']} : fichier {ligne['chemin']!r}, {attendu!r} attendu")]
    f = sceau_conforme(Path(racine) / ligne["chemin"], ligne["sha256"], ligne["cle"])
    if f:
        return None, f
    texte = (Path(racine) / ligne["chemin"]).read_text(encoding="utf-8")
    d, t = DECISION.findall(texte), DATE_DECISION.findall(texte)
    if len(d) != 1 or len(t) != 1 or len(re.findall(r"^Décision :", texte, re.M)) != 1 or \
            len(re.findall(r"^Date :", texte, re.M)) != 1:
        return None, [("ligne-mal-formee", f"décision {ligne['chemin']} mal formée (une ligne « Décision : maintenir », "
                                           f"« … : ouvrir » ou « … : ouvrir pleinement » et une ligne « Date : "
                                           f"AAAA-MM-JJTHH:MM:SSZ » attendues)")]
    try:
        instant = instant_utc(t[0])
    except GardeArret as e:
        return None, [("ligne-mal-formee", f"décision {ligne['chemin']} : {e}")]
    if instant < instant_utc(DATE_RENDEZ_VOUS):
        return None, [("ligne-mal-formee", f"décision {ligne['chemin']} datée {t[0]}, avant le rendez-vous "
                                           f"({DATE_RENDEZ_VOUS})")]
    if instant > ligne["instant"]:
        return None, [("ligne-mal-formee", f"décision {ligne['chemin']} datée {t[0]}, après sa ligne ({ligne['date']})")]
    return {"numero": n, "decision": d[0], "date": t[0], "instant": instant, "fichier": ligne["chemin"],
            "sha256": ligne["sha256"], "cle": ligne["cle"], "date_ligne": ligne["date"],
            "instant_ligne": ligne["instant"]}, []


def ligne_t07_conforme(racine: Path, ligne: dict, instant: int) -> list:
    """D8 : date strictement antérieure à l'ouverture, compagnon du fichier cité présent et égal à l'empreinte de la ligne ;
    le fichier lui-même vérifié seulement s'il est présent (aucun fichier fermé de T0.7 n'est déplacé pour cela)."""
    fautes = _anterieure(ligne, instant)
    p = Path(racine) / ligne["chemin"]
    comp = Path(str(p) + ".sha256")
    if not comp.is_file():
        return fautes + [("compagnon-absent", f"ligne {ligne['cle']} : compagnon {ligne['chemin']}.sha256 absent")]
    if _premier_mot(comp) != ligne["sha256"]:
        fautes.append(("sceau-faux", f"ligne {ligne['cle']} : compagnon de {ligne['chemin']} ≠ empreinte de la ligne"))
    elif p.is_file() and _sha_fichier(p) != ligne["sha256"]:
        fautes.append(("sceau-faux", f"ligne {ligne['cle']} : {ligne['chemin']} présent, d'empreinte ≠ celle de la ligne"))
    return fautes


def suite_des_decisions(decisions: list[dict], anterieures: list[dict]) -> list:
    """« maintenir » suivi de toute décision ; « ouvrir » de rien, sauf d'une seule « ouvrir pleinement » si une ouverture
    `reduite` appuyée sur sa ligne est lue au journal, datée strictement avant la ligne suivante ; « ouvrir pleinement » de
    rien (`ligne-apres-decision-finale`)."""
    reduites = [x for x in anterieures if x["cle"] == CLE_OUVERTURE and x["mode"] == REDUITE]
    fautes = []
    for k, d in enumerate(decisions[:-1]):
        suivante = decisions[k + 1]
        if d["decision"] == OUVRIR_PLEINEMENT:
            fautes.append(("ligne-apres-decision-finale", f"ligne {suivante['cle']} après une décision « ouvrir pleinement » "
                                                          f"({d['cle']})"))
        elif d["decision"] == OUVRIR:
            appui = (d["cle"], d["sha256"])
            reduite_lue = any(r["jetons"] and r["jetons"][0] == appui and r["instant"] < suivante["instant_ligne"]
                              for r in reduites)
            if not (k + 2 == len(decisions) and suivante["decision"] == OUVRIR_PLEINEMENT and reduite_lue):
                fautes.append(("ligne-apres-decision-finale",
                               f"ligne {suivante['cle']} après la décision « ouvrir » de {d['cle']} : seule une décision "
                               f"« ouvrir pleinement » est permise, et seulement après une ouverture réduite lue au journal"))
    return fautes


def chemin_normal(racine: Path, t07: dict, instant: int) -> list:
    fautes = []
    for k in (SCORES_T07, SONDES_T07):
        if k not in t07:
            fautes.append(("ligne-absente", f"ligne {k} absente du registre des scellements"))
        else:
            fautes += ligne_t07_conforme(racine, t07[k], instant)
    return fautes


def garde_adaptee_en_vigueur(racine: Path, pre: dict, t07: dict, decision: dict, instant: int) -> list:
    """Branche 1 : T0.7 scellé (`SCELLEMENT-T07` conforme) avec la garde adaptée (`GARDE-ADAPTEE-T07-P3BIS` qui cite le même
    texte), toutes deux strictement antérieures à la ligne de la décision « ouvrir » (contre-lecture 3, D2 ; CP-17)."""
    fautes = []
    s, g = t07.get(SCELLEMENT_T07), pre["garde"]
    if s is None:
        fautes.append(("garde-adaptee-absente", "T0.7 non scellé (aucune ligne SCELLEMENT-T07)"))
    else:
        fautes += ligne_t07_conforme(racine, s, instant)
        if not s["instant"] < decision["instant_ligne"]:
            fautes.append(("garde-adaptee-posterieure", f"SCELLEMENT-T07 datée {s['date']}, pas strictement avant la ligne "
                                                        f"de la décision « ouvrir » ({decision['date_ligne']})"))
    if g is None:
        fautes.append(("garde-adaptee-absente", f"aucune ligne {CLE_GARDE_ADAPTEE}"))
    else:
        if not g["instant"] < decision["instant_ligne"]:
            fautes.append(("garde-adaptee-posterieure", f"{CLE_GARDE_ADAPTEE} datée {g['date']}, pas strictement avant la "
                                                        f"ligne de la décision « ouvrir » ({decision['date_ligne']})"))
        if s is not None and (g["chemin"], g["sha256"]) != (s["chemin"], s["sha256"]):
            fautes.append(("garde-adaptee-absente", f"{CLE_GARDE_ADAPTEE} ne cite pas le texte scellé de T0.7 (ligne "
                                                    f"SCELLEMENT-T07)"))
    return fautes


def _appui_de(lignes) -> str:
    return " ".join(f"{x['cle']}={x['sha256']}" for x in lignes if x is not None) or "-"


def appui_presente(racine: Path, mode: str) -> str:
    """Appui présenté par un refus : lignes du registre que le mode demandé exigerait, telles qu'on les trouve (lecture
    sans garde), dans l'ordre du texte ; aucune : `-`."""
    racine, trouvees = Path(racine), {}
    for registre in (REGISTRE_SCELLEMENTS, REGISTRE_PREALABLES):
        try:
            texte = (racine / registre).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for brute in texte.splitlines():
            c = _cellules(brute) if brute.strip().startswith("|") else []
            if c and (c[0] in (SCORES_T07, SONDES_T07, CLE_GARDE_ADAPTEE) or CLE_RDV_APPUI.fullmatch(c[0])):
                ligne = _ligne_stricte(c[0], c, [], registre)
                if ligne is not None and (registre == REGISTRE_PREALABLES) == (c[0] not in (SCORES_T07, SONDES_T07)):
                    trouvees.setdefault("rdv" if CLE_RDV_APPUI.fullmatch(c[0]) else c[0], []).append(ligne)
    rdv = (trouvees.get("rdv") or [None])[-1]
    garde = (trouvees.get(CLE_GARDE_ADAPTEE) or [None])[-1]
    if mode == PLEINE:
        return _appui_de([(trouvees.get(SCORES_T07) or [None])[-1], (trouvees.get(SONDES_T07) or [None])[-1]])
    if mode == REDUITE:
        return _appui_de([rdv, garde])
    return _appui_de([rdv])


def garde_ouverture(racine, mode: str, instant: int) -> dict:
    """Garde du plan, point 8 : journal, registre des préalables, décisions, registre des scellements, puis le mode demandé.
    Rend le mode autorisé, le chemin, l'appui, les lignes d'écrit, les décisions et les ouvertures antérieures ; sinon
    `RefusOuverture` (code du premier défaut, tous les défauts écrits)."""
    racine = Path(racine)
    if mode not in MODES:
        raise GardeArret(f"mode {mode!r} : {', '.join(MODES)} attendus")
    anterieures = lire_journal(racine / JOURNAL_OUVERTURES)
    ouvertes = [x["mode"] for x in anterieures if x["cle"] == CLE_OUVERTURE]
    if any(m in MODES_FINAUX for m in ouvertes) or (mode == REDUITE and REDUITE in ouvertes):
        raise RefusOuverture("deja-ouverte", f"ouvertures déjà journalisées : {', '.join(ouvertes)} ; après « reduite », "
                                             f"seule « pleine » ou « pleine-anticipee » ; après une ouverture pleine, aucune")
    try:
        pre = lire_prealables(racine / REGISTRE_PREALABLES)
        t07 = lire_scellements_t07(racine / REGISTRE_SCELLEMENTS)
    except RefusOuverture as e:
        raise RefusOuverture(e.code, e.texte, appui_presente(racine, mode)) from None
    fautes = []
    for ligne in pre["ecrits"].values():
        fautes += _anterieure(ligne, instant) + sceau_conforme(racine / ligne["chemin"], ligne["sha256"], ligne["cle"])
    if pre["garde"] is not None:
        g = pre["garde"]
        fautes += _anterieure(g, instant) + sceau_conforme(racine / g["chemin"], g["sha256"], g["cle"])
    decisions = []
    for n, ligne in enumerate(pre["rendez_vous"], start=1):
        f = _anterieure(ligne, instant)
        d, f2 = lire_decision(racine, ligne, n)
        fautes += f + f2
        if d is not None:
            decisions.append(d)
    if not fautes:
        fautes += suite_des_decisions(decisions, anterieures)
    if fautes:
        _refuser(fautes, appui_presente(racine, mode))
    derniere = decisions[-1] if decisions else None
    dernier_mot = derniere["decision"] if derniere else None
    normal = chemin_normal(racine, t07, instant)
    sans = [("ni-scores-ni-ouvrir", "ni lignes SCORES-T07 et SONDES-T07 conformes, ni décision « ouvrir » ou « ouvrir "
                                    "pleinement »")] + normal
    maintenir = [("decision-maintenir", f"décision « maintenir » ({derniere['cle']}) : l'attente continue, rien n'est "
                                        f"ouvert")] if dernier_mot == MAINTENIR else []
    if mode == PLEINE:
        if not normal:
            chemin = "complément de l'ouverture réduite" if REDUITE in ouvertes else "chemin normal"
            if decisions and REDUITE not in ouvertes:
                chemin += " (rendez-vous sans objet)"
            return _autorise(racine, mode, chemin, [t07[SCORES_T07], t07[SONDES_T07]], pre, decisions, anterieures)
        if dernier_mot is None:
            _refuser(sans, appui_presente(racine, mode))
        if maintenir:
            _refuser(maintenir + normal, appui_presente(racine, mode))
        _refuser([(normal[0][0], f"le mode pleine exige SCORES-T07 et SONDES-T07 conformes : {normal[0][1]}")] + normal[1:],
                 appui_presente(racine, mode))
    if dernier_mot is None:
        _refuser(sans, appui_presente(racine, mode))
    if maintenir:
        _refuser(maintenir, appui_presente(racine, mode))
    adaptee = garde_adaptee_en_vigueur(racine, pre, t07, derniere, instant) if dernier_mot == OUVRIR else []
    if mode == REDUITE:
        if dernier_mot != OUVRIR:
            _refuser([("ni-scores-ni-ouvrir", f"ouverture réduite demandée sans dernière décision « ouvrir » (dernière : "
                                              f"« {dernier_mot} » de {derniere['cle']}, qui autorise « pleine-anticipee »)")],
                     appui_presente(racine, mode))
        if adaptee:
            _refuser(adaptee, appui_presente(racine, mode))
        return _autorise(racine, mode, "branche 1 (ouverture réduite à l'issue)", [derniere, pre["garde"]], pre, decisions,
                         anterieures)
    if dernier_mot == OUVRIR:
        if adaptee:
            _refuser(adaptee, appui_presente(racine, mode))
        _refuser([("ni-scores-ni-ouvrir", f"décision « ouvrir » ({derniere['cle']}) avec la garde adaptée en vigueur : "
                                          f"ouverture réduite seulement ; « pleine-anticipee » exige une décision « ouvrir "
                                          f"pleinement »")], appui_presente(racine, mode))
    return _autorise(racine, mode, "branche 2 (décision « ouvrir pleinement ») : T0.7 ne lit plus la course 7b sous son "
                                   "texte, nœud de Lazar", [derniere], pre, decisions, anterieures)


def _autorise(racine: Path, mode: str, chemin: str, appui: list, pre: dict, decisions: list, anterieures: list) -> dict:
    return {"mode": mode, "chemin": chemin, "appui": _appui_de(appui), "ecrits": pre["ecrits"], "decisions": decisions,
            "anterieures": anterieures,
            "registre_prealables_sha256": _sha_fichier(Path(racine) / REGISTRE_PREALABLES),
            "registre_scellements_sha256": (_sha_fichier(Path(racine) / REGISTRE_SCELLEMENTS)
                                            if (Path(racine) / REGISTRE_SCELLEMENTS).is_file() else "absent")}


# ================================================================================================= ouverture
def date_de_la_mise_en_paquet(racine_paquets: Path, run: str, date: str | None) -> int:
    try:
        if date is not None:
            return instant_utc(date)
    except GardeArret as e:
        raise RefusOuverture("paquet-faux", f"date de la mise en paquet : {e}") from None
    r = subprocess.run(["git", "-C", str(racine_paquets), "log", "-1", "--format=%ct", "--",
                        f"{dossier_ferme(run)}/{PAQUET_LECTURES}"], capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip().isdigit():
        raise RefusOuverture("paquet-faux", "date de la mise en paquet illisible (--date-paquet ou commit du paquet exigé)")
    return int(r.stdout.strip())


def lire_paquets(racine_paquets: Path, run: str) -> dict:
    """Les deux paquets relus en mémoire : paquet des lectures (sceau, taille, sel, longueur, flux), second paquet (index,
    morceaux, sel), aucun chemin commun ; sinon refus `paquet-faux`."""
    racine_paquets = Path(racine_paquets)
    cible = racine_paquets / dossier_ferme(run) / PAQUET_LECTURES
    sha_l = sha_r = None
    try:
        sha_l = verifier(cible)
        _, archive = relire_paquet_lectures(cible.read_bytes())
        lectures = dict(membres_de(archive))
        verifier(racine_paquets / "diag" / run / INDEX_RUN)
        sha_r = str(json.loads((racine_paquets / "diag" / run / INDEX_RUN).read_text(encoding="utf-8"))["sha256"])
        du_run = relire_run(racine_paquets, run)
    except (GardeArret, OSError, ValueError, KeyError, TypeError) as e:
        cellule = f"{sha_l} {sha_r}" if sha_l and sha_r and SHA.fullmatch(sha_r) else "-"
        raise RefusOuverture("paquet-faux", f"{type(e).__name__ if not isinstance(e, GardeArret) else 'garde'} : {e}",
                             paquets=cellule) from None
    communs = set(lectures) & set(du_run)
    if communs:
        raise RefusOuverture("paquet-faux", f"chemins présents dans les deux paquets : {sorted(communs)}",
                             paquets=f"{sha_l} {sha_r}")
    return {"lectures": lectures, "run": du_run, "paquet_lectures_sha256": sha_l, "paquet_run_sha256": sha_r,
            "cellule": f"{sha_l} {sha_r}"}


def extraire(fichiers: dict[str, bytes], sortie: Path) -> None:
    """Fichiers écrits sous un dossier neuf (chemins d'origine sous lui), par un dossier caché renommé à la fin."""
    sortie = Path(sortie)
    temp = Path(tempfile.mkdtemp(prefix=".ouverture-", dir=str(sortie.parent)))
    try:
        for c, octets in sorted(fichiers.items()):
            (temp / c).parent.mkdir(parents=True, exist_ok=True)
            (temp / c).write_bytes(octets)
        os.rename(temp, sortie)
    except BaseException:
        shutil.rmtree(temp, ignore_errors=True)
        raise


def ouvrir(racine, mode: str, run: str, sortie, racine_paquets=None, date_paquet: str | None = None,
           instant: int | None = None, imprimer=print) -> dict:
    """Garde, relecture des paquets, ligne au journal, puis extraction ; un refus est journalisé (code de la liste fermée)
    avant d'être levé. `instant` : pour les essais seulement (la ligne de commande prend l'horloge, CP-08)."""
    racine = Path(racine)
    racine_paquets = Path(racine_paquets) if racine_paquets is not None else racine
    sortie = Path(sortie)
    if mode not in MODES:
        raise GardeArret(f"mode {mode!r} : {', '.join(MODES)} attendus")
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà (R12)")
    if not sortie.parent.is_dir():
        raise GardeArret(f"dossier parent de la sortie {sortie.parent} absent")
    instant = int(time.time()) if instant is None else int(instant)
    try:
        g = garde_ouverture(racine, mode, instant)
        try:
            instant_paquet = date_de_la_mise_en_paquet(racine_paquets, run, date_paquet)
            p = lire_paquets(racine_paquets, run)
            for x in g["anterieures"]:
                if x["cle"] == CLE_OUVERTURE and x["paquets"] != p["cellule"]:
                    raise RefusOuverture("paquet-faux", f"paquets autres que ceux de l'ouverture {x['mode']} du {x['date']}",
                                         paquets=p["cellule"])
        except RefusOuverture as e:
            raise RefusOuverture(e.code, e.texte, g["appui"], e.paquets) from None
    except RefusOuverture as e:
        inscrire(racine, ligne_journal(CLE_REFUS, instant, mode, e.appui, e.paquets, f"{e.code} : {_propre(e.texte)}"))
        raise
    reserves = [f"{k} : écrit après la lecture fermée : sa cécité repose sur la fermeture"
                for k, ligne in g["ecrits"].items() if ligne["instant"] > instant_paquet]
    inscrire(racine, ligne_journal(CLE_OUVERTURE, instant, g["mode"], g["appui"], p["cellule"], "-"))
    try:
        extraire({**p["lectures"], **p["run"]}, sortie)
    except (OSError, GardeArret) as e:
        raise GardeArret(f"extraction en échec après la ligne {CLE_OUVERTURE} du journal ({type(e).__name__}: {e}) : rien "
                         f"n'est laissé dans {sortie} ; écart à consigner") from None
    if g["mode"] == REDUITE:
        imprimer(f"ouverture réduite : paquets extraits dans {sortie}, remis au seul lecteur du verdict ; seules `issue` et "
                 f"`ligne` du fichier d'issue seront affichées (exposer-issue)")
    else:
        imprimer(f"ouverture {g['mode']} ({g['chemin']}) : paquets extraits dans {sortie}")
    for r in reserves:
        imprimer(f"réserve : {r}")
    return {**g, "reserves": reserves, "paquet_lectures_sha256": p["paquet_lectures_sha256"],
            "paquet_run_sha256": p["paquet_run_sha256"]}


def exposer_issue(fichier, lecture_p3bis=None) -> dict:
    """Seules `issue` et `ligne` du fichier d'issue (quatre clés exactement, scellé) ; pour les lignes 2 à 5, accord exigé
    avec `resultat.issue_mecanique` de `lecture-p3bis.json`, dont le sceau est vérifié (CP-16)."""
    fichier = Path(fichier)
    verifier(fichier)
    try:
        doc = json.loads(fichier.read_text(encoding="utf-8"))
    except ValueError:
        raise GardeArret(f"{fichier} : JSON illisible") from None
    if not isinstance(doc, dict) or sorted(doc) != sorted(CLES_ISSUE):
        raise GardeArret(f"{fichier} : clés {sorted(doc) if isinstance(doc, dict) else doc!r}, {list(CLES_ISSUE)} exactement")
    issue, ligne = doc["issue"], doc["ligne"]
    if issue not in ISSUES or isinstance(ligne, bool) or not isinstance(ligne, int) or ISSUES[issue] != ligne:
        raise GardeArret(f"{fichier} : issue {issue!r} et ligne {ligne!r} hors de la table gelée")
    if doc["verdict"] != VERDICT or not isinstance(doc["verdict_sha256"], str) or not SHA.fullmatch(doc["verdict_sha256"]):
        raise GardeArret(f"{fichier} : verdict ou empreinte du verdict hors de forme")
    if ligne != 1:
        if lecture_p3bis is None:
            raise GardeArret(f"ligne {ligne} : l'accord avec l'issue mécanique est exigé (--lecture-p3bis)")
        verifier(Path(lecture_p3bis))
        try:
            im = json.loads(Path(lecture_p3bis).read_text(encoding="utf-8"))["resultat"]["issue_mecanique"]
            mecanique = (im["issue"], im["ligne"])
        except (ValueError, KeyError, TypeError):
            raise GardeArret(f"{lecture_p3bis} : resultat.issue_mecanique illisible") from None
        if mecanique != (issue, ligne):
            raise GardeArret(f"désaccord entre le fichier d'issue ({issue}, {ligne}) et l'issue mécanique "
                             f"({mecanique[0]}, {mecanique[1]}) : nœud de Lazar")
    return {"issue": issue, "ligne": ligne}


# ================================================================================================= ligne de commande
def _main(argv) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.premier_test_ia.ouverture_p3bis_v2")
    sp = ap.add_subparsers(dest="commande", required=True)
    for nom in ("fermer-run", "exiger-aucun-clair", "deplier-run", "lectures-fermees", "fermer", "ouvrir"):
        p = sp.add_parser(nom)
        p.add_argument("--racine", default=".")
        p.add_argument("--run", required=True)
        if nom == "fermer-run":
            p.add_argument("--partiel", action="store_true")
        if nom in ("deplier-run", "lectures-fermees", "fermer"):
            p.add_argument("--espace", default=ESPACE_DEFAUT)
        if nom in ("lectures-fermees", "fermer"):
            p.add_argument("--lecture", required=True)
            p.add_argument("--lecture-complementaire", required=True)
            p.add_argument("--entropie", type=int, default=None)
        if nom == "lectures-fermees":
            p.add_argument("--prereg", default=None)
        if nom == "ouvrir":
            p.add_argument("--mode", required=True, choices=MODES)
            p.add_argument("--sortie", required=True)
            p.add_argument("--racine-paquets", default=None)
            p.add_argument("--date-paquet", default=None)
    p = sp.add_parser("exposer-issue")
    p.add_argument("fichier")
    p.add_argument("--lecture-p3bis", default=None)
    a = ap.parse_args(argv)
    if a.commande == "fermer-run":
        index = fermer_run(a.racine, a.run, a.partiel)
        if index is None:
            print("second paquet : aucun fichier du run à fermer")
        else:
            print(f"paquet du run {index['sha256']} ; {len(index['morceaux'])} morceau(x) : "
                  + ", ".join(f"{m['nom']} {m['sha256']}" for m in index["morceaux"]))
        return 0
    if a.commande == "exiger-aucun-clair":
        exiger_aucun_clair(a.racine, a.run)
        return 0
    if a.commande == "deplier-run":
        deplier_run(a.racine, a.run, a.espace)
        return 0
    if a.commande == "lectures-fermees":
        return lectures_fermees(a.racine, a.run, a.lecture, a.lecture_complementaire, a.prereg, a.entropie, a.espace)
    if a.commande == "fermer":
        fermer(a.racine, a.run, [a.lecture, a.lecture_complementaire], a.espace, a.entropie)
        return 0
    if a.commande == "ouvrir":
        try:
            ouvrir(a.racine, a.mode, a.run, a.sortie, a.racine_paquets, a.date_paquet)
        except (RefusOuverture, JournalImpossible) as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 2
        return 0
    print(json.dumps(exposer_issue(a.fichier, a.lecture_p3bis), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
