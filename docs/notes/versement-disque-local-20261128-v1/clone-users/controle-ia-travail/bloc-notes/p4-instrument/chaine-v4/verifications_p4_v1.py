"""Vérifications communes de la chaîne de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269), v1,
chaîne v2, puis chaîne v3 : un seul texte, lu à l'identique par le scellement, par les contrôles avant dépense, par le
lanceur, par la récupération (copie de S) et par le contrôle des traces de la session. Décliné de
`docs/procedures/P3-premier-test-v2/verifications_p3_v1.py` sous un nom neuf (R12).

Les contrôles du GO, de la révocation aux formes exactes, du plafond par lancement, de l'échéance, de la borne de l'étape,
de l'accord du jour, du module cité et de la garde de calcul gelée ne sont pas recodés : ce sont les fonctions du module
de P4 (`instrument_p4_v1.controler_go`, `controler_accord`, `rejouer_garde_de_calcul`, `exiger_module_cite`). Le module
est chargé par son chemin dans le dépôt RACINE, après contrôle de son empreinte contre la ligne « Module de P4 » du texte
PREREG : aucun code non cité ne s'exécute. Ce module-ci ajoute ce que le module de P4 ne lit pas :
  - la ligne « **GO cité par la commande de création** : `GO_ID=…` » (forme exacte, une fois, GO-2026-10-20-07 seul) ;
  - chaîne v2 (RC-depense-03, -08, RC-fidelite-03) : les révocations sous des formes voisines des formes exactes
    (espaces libres, casse, accents, tirets, type « Révocation » ou « revocation », type inconnu, cellule qui commence
    par « Révocation », « révoque », « annulation » ou « retrait » sous toute casse, plusieurs identifiants dans une
    cellule), qui nomment GO-2026-10-04-08, GO-2026-10-20-06, GO-2026-10-20-07, R-262 ou R-269 à frontières de mot :
    une forme voisine trouvée qui n'est pas une forme exacte arrête (code 2, lignes affichées), jamais un passage
    silencieux ; la chaîne refuse plus que la forme exacte, jamais moins ;
  - chaîne v2 (RC-depense-04) : la garde de calcul gelée n'est rejouée que si son fichier a l'empreinte gelée
    (579f65c8…, celle de `7a54d43`) ; sinon code 2 ;
  - chaîne v2 (RC-depense-05, RC-fidelite-05) : la ligne d'accord porte une fois la forme exacte « dépense consignée X USD
    + borne 5,41 USD = Y USD < 150 USD » (X et Y à deux décimales, virgule décimale) ; la somme est refaite au centime
    et Y < 150 exigé ; alerte écrite à 120 USD et au-delà (GO-2026-10-04-08) ;
  - chaîne v2 (RC-depense-09) : le GO cité par l'accord se lit à frontières de mot (GO-2026-10-20-071 ne cite pas
    GO-2026-10-20-07) ;
  - chaîne v2 (RC-donnees-01, -02, -03, -04, -06) : recherche des fenêtres de 48 caractères, au pas de 16, de chaque
    texte honnête de P3 (fenêtres d'un seul caractère répété ignorées ; textes de moins de 48 caractères non cherchés),
    en brut et sous forme échappée (JSON, Python) et dans la forme déséchappée de chaque fichier ; masquage des jetons
    puis recherche des fenêtres avant tout affichage ; comptes seulement, jamais de texte ;
  - chaîne v2 (RC-fidelite-12) : les noms exacts des rapports attendus sous `prereg/contre-lectures/` ;
  - les journaux des bancs et celui de la répétition jouet.
Chaîne v3 (traitement des vérifications de la chaîne v2, `traitement-verifications-chaine-v2-P4-v1.md`, 10664a97…) :
  - VC2-depense-01 : formes voisines de révocation élargies (première cellule reconnue sans gras ; toutes les cellules
    d'une ligne de décision ; toute ligne de GO, de tout type, dont une cellule commence par un début de révocation et
    nomme l'un des cinq identifiants) ;
  - VC2-donnees-02 : une entrée qui n'est pas un fichier ordinaire (lien symbolique, tube nommé…) n'est jamais suivie ni
    lue : elle est comptée et refusée (code 1, chemin écrit) par `fenetres` et `jetons` ;
  - RAPPORTS_NOMS : liste finale de vingt-six noms ;
  - répétition : refus du clonage en code 2, état de l'instance gardée et heure limite dans les refus de la place et du
    clonage (VC2-depense-03) ; repli de l'affichage de la récupération (VC2-donnees-01).

Python de la session (le module importe le code du dépôt et ses dépendances), -B, PYTHONDONTWRITEBYTECODE=1 :
  verifications_p4_v1.py go RACINE PREREG JOUR BORNE
      ligne du GO du texte ; `controler_go` du module (formes exactes : code 1) ; révocations sous des formes voisines
      (code 2, lignes affichées) ; empreinte de la garde gelée (code 2) ; `rejouer_garde_de_calcul` (code 1).
  verifications_p4_v1.py accord RACINE PREREG R-… JOUR
      `controler_accord` du module ; GO cité à frontières de mot ; forme de la dépense de la phase, somme et 150 USD.
  verifications_p4_v1.py module RACINE PREREG
      `exiger_module_cite` du module : les six fichiers cités, et eux seuls ; une ligne « <chemin> <sha256> » par fichier.
  verifications_p4_v1.py rapports NOM=SHA…
      paires épinglées : exactement les noms attendus (RAPPORTS_NOMS), une fois chacun, empreintes de 64 signes.
  verifications_p4_v1.py fenetres TEXTES CHEMIN…
      fenêtres des textes honnêtes de TEXTES (fichier au format des textes de P3) dans chaque fichier de CHEMIN (fichier
      ou dossier, parcouru en entier sans suivre de lien) ; comptes et chemins seulement ; code 0 aucune, 1 retrouvée,
      fichier illisible ou entrée non ordinaire (lien symbolique ou autre).
  verifications_p4_v1.py montrer TEXTES [LONGUEUR]
      filtre de l'entrée standard, ligne à ligne : jetons de l'environnement masqués, puis toute ligne qui porte une
      fenêtre est remplacée par sa longueur et son empreinte courte ; puis troncature à LONGUEUR (300 par défaut).
  verifications_p4_v1.py jetons CHEMIN…
      valeurs des jetons de l'environnement (HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN exigés, 8 caractères au moins ;
      GH_TOKEN et VAST_API_KEY s'ils sont présents) dans chaque fichier ; comptes seulement ; code 0, ou 1 (jeton
      retrouvé, fichier illisible ou entrée non ordinaire).
  verifications_p4_v1.py repetition CODE JOURNAL CANDIDAT_NOM CANDIDAT_SHA
      journal de la répétition jouet : commit répété, candidat répété, cinq passages à leur code, sept récupérations
      conformes (instance détruite), vingt-sept artefacts refusés chacun par un seul KO au préfixe attendu, chacun avec
      l'état de l'instance gardée et l'heure limite de destruction, trois refus en code 2 (place, traces d'un autre
      lancement, clonage ; état et heure limite dans ceux de la place et du clonage), le repli de l'affichage, aucun
      jeton ni aucune fenêtre affichés ; lecture jouet (module v2 et v3) : la lecture sans --prereg du run décisif du passage 1 refusée sans rien
      écrire, et la lecture sans --prereg d'un run jouet non décisif en code 0 ; quatre lignes « script répété »
      exactement. Écrit une ligne « <script> <sha256> » par script répété.
  verifications_p4_v1.py preuves DOSSIER [JOURNAL …]
      journaux des bancs et de la répétition finale (tous les huit si aucun n'est nommé) : présents, au verdict conforme
      sur leur dernière ligne, sans ligne d'échec, avec exactement les scripts qu'ils éprouvent ; une même empreinte pour
      un script éprouvé par plusieurs journaux. Écrit une ligne « <script> <sha256> » par script éprouvé.
Code 0 si conforme ; code 1 avec un message sur la dernière ligne sinon ; code 2 sur un usage faux, une révocation sous
une forme voisine, une garde gelée d'une autre empreinte, des rapports aux noms autres, ou des textes illisibles.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

sys.dont_write_bytecode = True

GO_ATTENDU = "GO-2026-10-20-07"          # seul GO accepté dans la commande de création (en-tête « GO et dépense »)
CHEMIN_MODULE = "docs/procedures/P4-instrument-v1/instrument_p4_v1.py"
LIGNE_GO = re.compile(r"^[ \t]*- \*\*GO cité par la commande de création\*\* : `GO_ID=(GO-\d{4}-\d{2}-\d{2}-\d{2})`", re.M)
LIGNE_MODULE = re.compile(r"^[ \t]*-[ \t]+Module de P4 : `([^`]+)` : `([0-9a-f]{64})`[ \t]*$", re.M)
GARDE = ".claude/hooks/garde_calcul.py"
GARDE_SHA256 = "579f65c8ae3002d8e5c61698d636549b0401da3acff6bce718ae88e93664a6f2"   # garde gelée de 7a54d43
REVOCABLES = ("GO-2026-10-04-08", "GO-2026-10-20-06", "GO-2026-10-20-07", "R-262", "R-269")
# types de l'en-tête du registre des GO (et ceux de R-281), sans casse ni accent
TYPES_GO = ("calcul", "porte", "depot distant", "publication", "contact", "revendication", "revocation")
DEBUTS_REVOCATION = ("revoc", "revoqu", "annul", "retrait", "retir")
FORME_DEPENSE = re.compile(r"dépense consignée ([0-9]{1,3},[0-9]{2}) USD \+ borne 5,41 USD = ([0-9]{1,3},[0-9]{2}) USD < 150 USD")
MESSAGE_DU_JOUR = "message de Lazar dans la session"
GO_A_FRONTIERES = re.compile(r"(?<![\w-])GO-2026-10-20-07(?![\w-])")
JETONS = ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY")
JETONS_EXIGES = ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN")
LARGEUR, PAS = 48, 16                    # fenêtres glissantes : toutes les fenêtres de 48 caractères, au pas de 16
# rapports attendus sous prereg/contre-lectures/ (seuls de leur famille : nom qui contient « P4 »), noms exacts ; chaîne
# v3 : liste finale de vingt-six noms, dans l'ordre de la section « Liste RAPPORTS_NOMS » du traitement des vérifications
# de la chaîne v2 (`traitement-verifications-chaine-v2-P4-v1.md`, 10664a97…)
RAPPORTS_NOMS = (
    "contre-lecture-R2-P4-instrument-brouillon1-v1.md",
    "traitement-R2-P4-instrument-brouillon1-v1.md",
    "traitement-gemini-014-P4-instrument-v1.md",
    "verification-corrections-brouillons2-3-P4-v1.md",
    "traitement-verification-P4-instrument-v1.md",
    "contre-lecture-3-P4-instrument-candidat1-v1.md",
    "relecture-chaine-depense-P4-instrument-v1.md",
    "relecture-chaine-donnees-P4-instrument-v1.md",
    "relecture-chaine-fidelite-P4-instrument-v1.md",
    "traitement-CL3-et-relectures-chaine-P4-v1.md",
    "verification-module-v2-contournement-P4-instrument-v1.md",
    "verification-module-v2-fidelite-P4-instrument-v1.md",
    "traitement-verifications-module-v2-P4-v1.md",
    "verification-module-v3-P4-instrument-v1.md",
    "verification-chaine-v2-depense-P4-instrument-v1.md",
    "verification-chaine-v2-donnees-P4-instrument-v1.md",
    "verification-chaine-v2-fidelite-P4-instrument-v1.md",
    "traitement-verifications-chaine-v2-P4-v1.md",
    "traitement-verification-fidelite-chaine-v2-P4-v1.md",
    "verification-chaine-v4-P4-instrument-v1.md",
    "verification-candidat2-P4-instrument-v1.md",
    "P4-instrument-v1-brouillon1.md",
    "P4-instrument-v1-brouillon2.md",
    "P4-instrument-v1-brouillon3.md",
    "P4-instrument-v1-brouillon4.md",
    "P4-instrument-v1-candidat1.md",
    "P4-instrument-v1-candidat2.md"
)


class Usage(Exception):
    """Arrêt en code 2 : rien n'est contrôlé, ou forme voisine trouvée (lignes affichées avant le motif)."""


def arret2(motif: str, lignes=()) -> None:
    for x in lignes:
        sys.stderr.write(f"    {x[:240]}\n")
    raise Usage(motif)


def sha_texte(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8", errors="replace")).hexdigest()


def lire(chemin) -> str:
    try:
        return Path(chemin).read_text(encoding="utf-8")
    except OSError:
        raise SystemExit(f"fichier {chemin} absent ou illisible") from None
    except UnicodeDecodeError as e:
        raise SystemExit(f"fichier {chemin} : UTF-8 invalide à l'octet {e.start} (ligne coupée au milieu d'un "
                         f"caractère ?)") from None


def charger_module(racine: Path, prereg: str):
    """Module de P4 du dépôt RACINE, chargé seulement s'il a l'empreinte de sa ligne « Module de P4 » du texte."""
    cites = [m for m in LIGNE_MODULE.finditer(lire(prereg)) if m.group(1) == CHEMIN_MODULE]
    if len(cites) != 1:
        raise SystemExit(f"ligne « Module de P4 » de {CHEMIN_MODULE} absente, en double ou mal formée dans le texte")
    p = Path(racine) / CHEMIN_MODULE
    try:
        e = hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        raise SystemExit(f"module de P4 absent : {p}") from None
    if e != cites[0].group(2):
        raise SystemExit(f"module de P4 {CHEMIN_MODULE} : empreinte {e[:12]} ≠ empreinte citée {cites[0].group(2)[:12]} "
                         "(aucun code non cité n'est exécuté)")
    sys.path.insert(0, str(Path(racine).resolve() / "src"))
    spec = importlib.util.spec_from_file_location("instrument_p4_v1", p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if module.GO_CITE != GO_ATTENDU:
        raise SystemExit(f"module de P4 : GO_CITE {module.GO_CITE} ≠ {GO_ATTENDU}")
    return module


def _garde(fonction, *args):
    """Appelle une garde du module ; son refus (GardeArret) devient un échec motivé (code 1)."""
    from controle_ia.gardes import GardeArret
    try:
        return fonction(*args)
    except GardeArret as e:
        raise SystemExit(str(e)[:300]) from None


# ------------------------------------------------------------------------------------- révocations, formes voisines

_TIRETS = dict.fromkeys(map(ord, "‐‑‒–—―−﹘﹣－"), "-")
_IDS = re.compile(r"(?<![\w-])(go-2026-10-04-08|go-2026-10-20-06|go-2026-10-20-07|r-262|r-269)(?![\w-])")


def normaliser(s: str) -> str:
    """Sans casse ni accent ; tirets ramenés à « - » ; blancs (insécables compris) réduits à une espace."""
    s = unicodedata.normalize("NFKD", s).translate(_TIRETS).replace("­", "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).strip().lower()


def _cellules_n(ligne: str) -> list[str] | None:
    n = normaliser(ligne)
    if not n.startswith("|"):
        return None
    return [x.strip() for x in n.strip("|").split("|")]


def _tete_de_revocation(cellule: str) -> bool:
    """Cellule (normalisée) qui commence, gras, soulignés, guillemets et parenthèses retirés, par un début de révocation."""
    return cellule.lstrip("*_ \"'«»`([").startswith(DEBUTS_REVOCATION)


def revocations_voisines(texte_go: str, texte_dec: str) -> list[str]:
    """Lignes qui ressemblent à une révocation de l'un des cinq identifiants sans en avoir la forme exacte (les formes
    exactes sont refusées avant, par `controler_go` du module). Chaîne v3 (VC2-depense-01 ; correction éprouvée de la
    vérification « dépense », fonction `proposees` de son banc `banc_voisines_v2.py`) : la première cellule est
    reconnue sans gras, soulignés ni guillemets inversés (« **GO-…** », « **R-…** ») ; registre des décisions : toutes
    les cellules après la première sont lues (colonne omise ou en trop) ; registre des GO : toute ligne, de tout type,
    dont une cellule commence par un début de révocation et nomme l'un des cinq identifiants.
    Registre des GO : ligne lue comme une ligne de GO à espaces libres (comme la garde gelée, et en plus avec des blancs
    en tête), qui nomme l'un des cinq identifiants dans une cellule autre que la première, et qui est de type
    « révocation » à la casse et aux accents près, ou d'un type inconnu de l'en-tête, ou dont une cellule commence
    (gras, soulignés, guillemets retirés) par « révocation », « révoque », « annulation » ou « retrait » et nomme l'un
    des cinq identifiants. Registre des décisions : ligne R-… dont une cellule, après la première, commence par l'un de
    ces débuts, sous toute casse et tout accent, et nomme l'un des cinq identifiants à frontières de mot."""
    trouvees = []
    for n, ligne in enumerate(texte_go.split("\n"), 1):
        k = _cellules_n(ligne)
        if not k or not re.fullmatch(r"go-\d{4}-\d{2}-\d{2}-\d{2}", k[0].strip("*_` ")):
            continue
        typ = k[2].strip("*_` ") if len(k) > 2 else ""
        if (typ.startswith(DEBUTS_REVOCATION) or typ not in TYPES_GO
                or any(_tete_de_revocation(c) and _IDS.search(c) for c in k[1:])) and _IDS.search(" | ".join(k[1:])):
            trouvees.append(f"registres/go.md, ligne {n} : {ligne.strip()}")
    for n, ligne in enumerate(texte_dec.split("\n"), 1):
        k = _cellules_n(ligne)
        if not k or not re.fullmatch(r"r-\d{3,4}", k[0].strip("*_` ")):
            continue
        if any(_tete_de_revocation(c) and _IDS.search(c) for c in k[1:]):
            trouvees.append(f"registres/decisions.md, ligne {n} : {ligne.strip()}")
    return trouvees


def go(racine: str, prereg: str, jour: str, borne: str) -> str:
    r = Path(racine)
    texte = lire(prereg)
    m = LIGNE_GO.findall(texte)
    if len(m) != 1 or len(re.findall(r"\*\*GO cité par la commande de création\*\*", texte)) != 1:
        raise SystemExit("ligne « **GO cité par la commande de création** : `GO_ID=…` » absente, en double ou mal formée")
    if m[0] != GO_ATTENDU:
        raise SystemExit(f"{m[0]} : seul {GO_ATTENDU} est accepté pour P4 (délégation R-269)")
    try:
        b = float(borne)
    except ValueError:
        raise SystemExit(f"borne de l'étape « {borne[:20]} » illisible") from None
    ip = charger_module(r, prereg)
    go_t, dec_t = lire(r / "registres" / "go.md"), lire(r / "registres" / "decisions.md")
    c = _garde(ip.controler_go, m[0], go_t, dec_t, jour, b)
    voisines = revocations_voisines(go_t, dec_t)
    if voisines:
        arret2(f"révocation possible sous une forme voisine de la forme exacte ({len(voisines)} ligne(s) ci-dessus, "
               "qui nomment GO-2026-10-04-08, GO-2026-10-20-06, GO-2026-10-20-07, R-262 ou R-269) : arrêt, aucune "
               "création ; nœud de Lazar (écrire la révocation sous sa forme exacte, ou lever le doute)", voisines)
    try:
        eg = hashlib.sha256((r / GARDE).read_bytes()).hexdigest()
    except OSError:
        arret2(f"garde de calcul gelée absente ({GARDE}) : aucun rejeu, aucune création")
    if eg != GARDE_SHA256:
        arret2(f"garde de calcul gelée modifiée : empreinte {eg[:12]} ≠ {GARDE_SHA256[:12]} (celle de 7a54d43) : "
               "aucun rejeu, aucune création")
    _garde(ip.rejouer_garde_de_calcul, r, f"GO_ID={m[0]} vastai create instance", jour)
    return (f"{c['go']} conforme : échéance {c['echeance']} ; plafond « {c['plafond'][:40]} » ; borne de l'étape "
            f"{c['borne_usd']:g} USD ; aucune révocation (formes exactes et voisines) ; garde de calcul gelée "
            f"({GARDE_SHA256[:12]}) : acceptée au {jour}")


def _centimes(x: str) -> int:
    e, d = x.split(",")
    return int(e) * 100 + int(d)


def accord(racine: str, prereg: str, ident: str, jour: str) -> str:
    r = Path(racine)
    ip = charger_module(r, prereg)
    go_t, dec_t = lire(r / "registres" / "go.md"), lire(r / "registres" / "decisions.md")
    _garde(ip.controler_accord, ident, go_t, dec_t, jour)
    ligne = [x for x in dec_t.split("\n") if x.startswith(f"| {ident} |")][0]     # une seule : le module l'exige
    corps = " | ".join(c.strip() for c in ligne.strip().strip("|").split("|")[2:])
    cite_go, cite_message = bool(GO_A_FRONTIERES.search(corps)), MESSAGE_DU_JOUR in corps
    if not (cite_go or cite_message):
        raise SystemExit(f"accord {ident} : ne cite {GO_ATTENDU} qu'au sein d'un identifiant voisin, et ne cite pas un "
                         "message de Lazar dans la session ce jour-là")
    formes = FORME_DEPENSE.findall(ligne)
    if len(formes) != 1 or ligne.count("dépense consignée") != 1:
        raise SystemExit(f"accord {ident} : forme « dépense consignée X USD + borne 5,41 USD = Y USD < 150 USD » absente, "
                         "mal formée ou en double (une fois ; X et Y à deux décimales, virgule décimale)")
    x, y = formes[0]
    if _centimes(x) + 541 != _centimes(y):
        raise SystemExit(f"accord {ident} : dépense consignée {x} USD + borne 5,41 USD ≠ {y} USD (somme fausse)")
    if not _centimes(y) < 15000:
        raise SystemExit(f"accord {ident} : {y} USD : la dépense de la phase atteindrait 150 USD ou plus "
                         "(GO-2026-10-04-08) : aucune création")
    alerte = " ; ALERTE : 120 USD atteints ou dépassés (GO-2026-10-04-08)" if _centimes(y) >= 12000 else ""
    cite = GO_ATTENDU if cite_go else "un message de Lazar du jour"
    return (f"{ident} : accord de Lazar du {jour} pour le lancement de P4-instrument (cite {cite}) ; dépense consignée "
            f"{x} USD + borne 5,41 USD = {y} USD < 150 USD{alerte} : conforme")


def module(racine: str, prereg: str) -> list[str]:
    ip = charger_module(Path(racine), prereg)
    cites = _garde(ip.exiger_module_cite, Path(racine), Path(prereg))
    return [f"{c} {s}" for c, s in sorted(cites.items())]


def rapports(paires: list[str]) -> list[str]:
    noms, faux = [], []
    for p in paires:
        m = re.fullmatch(r"([A-Za-z0-9._-]+)=([0-9a-f]{64})", p)
        if not m:
            faux.append(p[:60])
        else:
            noms.append(m.group(1))
    if faux:
        arret2(f"rapports attendus mal formés : {faux}")
    if sorted(noms) != sorted(RAPPORTS_NOMS) or len(set(noms)) != len(noms):
        arret2(f"rapports attendus : les {len(RAPPORTS_NOMS)} noms exacts de RAPPORTS_NOMS, une fois chacun (manquants "
               f"{sorted(set(RAPPORTS_NOMS) - set(noms))}, en trop {sorted(set(noms) - set(RAPPORTS_NOMS))}, "
               f"en double {sorted({x for x in noms if noms.count(x) > 1})})")
    return [f"rapport attendu : {n}" for n in sorted(noms)]


# ------------------------------------------------------------------------------------- fenêtres des textes honnêtes

_ECH = {"n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f", '"': '"', "\\": "\\", "/": "/", "'": "'"}
_MOTIF_ECH = re.compile(r"\\(?:u([dD][89abAB][0-9a-fA-F]{2})\\u([dD][c-fC-F][0-9a-fA-F]{2})|u([0-9a-fA-F]{4})"
                        r"|x([0-9a-fA-F]{2})|(.))", re.S)


def _remplacer(m: re.Match) -> str:
    if m.group(1):
        return chr(0x10000 + ((int(m.group(1), 16) - 0xD800) << 10) + (int(m.group(2), 16) - 0xDC00))
    if m.group(3):
        return chr(int(m.group(3), 16))
    if m.group(4):
        return chr(int(m.group(4), 16))
    return _ECH.get(m.group(5), "\\" + m.group(5))


def desechapper(s: str) -> str:
    """Forme déséchappée (JSON et Python : \\n, \\t, \\", \\\\, \\uXXXX, paires de substitution, \\xXX), de gauche à droite."""
    return _MOTIF_ECH.sub(_remplacer, s) if "\\" in s else s


def textes_honnetes(chemin) -> list[str]:
    """Textes de la condition honnête d'un fichier au format des textes de P3 (une ligne JSON par action) ; les autres
    lignes sont écartées à la lecture. Illisible ou vide : code 2 (rien n'est cherché)."""
    try:
        brut = Path(chemin).read_text(encoding="utf-8")
        textes = []
        for x in brut.splitlines():
            if x.strip():
                d = json.loads(x)
                if d.get("condition") == "honnete" and isinstance(d.get("texte"), str):
                    textes.append(d["texte"])
    except (OSError, UnicodeDecodeError, ValueError, AttributeError) as e:
        raise Usage(f"textes honnêtes illisibles ({chemin}) : {type(e).__name__} : recherche impossible") from None
    if not textes:
        raise Usage(f"aucun texte honnête dans {chemin} : recherche impossible")
    return textes


class Fenetres:
    """Toutes les fenêtres de 48 caractères, au pas de 16 (et la dernière), de chaque texte honnête d'au moins 48
    caractères ; fenêtres d'un seul caractère répété ignorées. Chaque fenêtre est cherchée sous quatre formes : brute,
    échappée en JSON (caractères gardés, ou échappés en \\uXXXX) et échappée par Python ; dans la forme brute et dans la
    forme déséchappée de chaque texte cherché. Index par les 16 premiers caractères de chaque forme."""

    def __init__(self, textes: list[str]):
        self.textes, self.courts, self.ignorees, self.fenetres = len(textes), 0, 0, []
        vues = set()
        for t in textes:
            if len(t) < LARGEUR:
                self.courts += 1
                continue
            positions = list(range(0, len(t) - LARGEUR + 1, PAS))
            if positions[-1] != len(t) - LARGEUR:
                positions.append(len(t) - LARGEUR)
            for p in positions:
                w = t[p:p + LARGEUR]
                if len(set(w)) == 1:
                    self.ignorees += 1
                elif w not in vues:
                    vues.add(w)
                    self.fenetres.append(w)
        self.index: dict[str, list[tuple[str, int]]] = {}
        for i, w in enumerate(self.fenetres):
            for a in {w, json.dumps(w, ensure_ascii=False)[1:-1], json.dumps(w)[1:-1], repr(w)[1:-1]}:
                self.index.setdefault(a[:16], []).append((a, i))

    def chercher(self, texte: str) -> set[int]:
        trouvees: set[int] = set()
        formes = [texte]
        d = desechapper(texte)
        if d != texte:
            formes.append(d)
        g = self.index
        for f in formes:
            for i in range(len(f) - LARGEUR + 1):
                liste = g.get(f[i:i + 16])
                if liste:
                    for a, k in liste:
                        if f.startswith(a, i):
                            trouvees.add(k)
        return trouvees


def _chaines_json(x, sortie: list[str]) -> None:
    if isinstance(x, str):
        sortie.append(x)
    elif isinstance(x, dict):
        for c, v in x.items():
            sortie.append(str(c))
            _chaines_json(v, sortie)
    elif isinstance(x, list):
        for v in x:
            _chaines_json(v, sortie)


def textes_d_un_fichier(f: Path) -> tuple[list[str], bool]:
    """Textes où chercher : octets décodés (UTF-8, caractères invalides remplacés) ; pour un JSON, chaque chaîne
    décodée en plus ; pour un tableau .npz, chaque chaîne de chaque tableau et chaque nom de tableau, séparément.
    Rend (textes, illisible)."""
    if f.suffix == ".npz":
        try:
            import numpy as np
            sortie = []
            with np.load(f, allow_pickle=False) as z:
                for c in z.files:
                    sortie.append(c)
                    a = z[c]
                    if a.dtype.kind == "U":
                        sortie.extend(str(x) for x in a.ravel().tolist())
                    elif a.dtype.kind == "S":
                        sortie.extend(x.decode("utf-8", errors="replace") for x in a.ravel().tolist())
            return sortie, False
        except Exception:
            return [], True
    try:
        b = f.read_bytes()
    except OSError:
        return [], True
    t = b.decode("utf-8", errors="replace")
    sortie = [t]
    if f.suffix == ".json":
        try:
            _chaines_json(json.loads(t), sortie)
        except ValueError:
            pass                                    # texte brut déjà cherché (forme brute et déséchappée)
    return sortie, False


def fichiers_de(chemins: list[str]) -> tuple[list[Path], list[Path]]:
    """Fichiers ordinaires à lire, et entrées qui ne sont pas des fichiers ordinaires (lien symbolique, vers un fichier
    ou un dossier, tube nommé, socket, périphérique ; chaîne v3, VC2-donnees-02) : jamais suivies ni lues, comptées et
    refusées par l'appelant (code 1, chemin écrit). Un dossier est parcouru en entier sans suivre de lien."""
    vus, autres = [], []
    for c in chemins:
        p = Path(c)
        if p.is_symlink():
            autres.append(p)
        elif p.is_dir():
            for x in sorted(p.rglob("*")):
                if x.is_symlink():
                    autres.append(x)
                elif x.is_dir():
                    continue
                elif x.is_file():
                    vus.append(x)
                else:
                    autres.append(x)
        elif p.is_file():
            vus.append(p)
        elif p.exists():
            autres.append(p)
        else:
            raise Usage(f"chemin {c} absent : recherche impossible")
    return vus, autres


def fenetres(textes: str, chemins: list[str]) -> tuple[list[str], bool]:
    idx = Fenetres(textes_honnetes(textes))
    fichiers, autres = fichiers_de(chemins)
    lignes, faute = [], False
    for a in autres:
        lignes.append(f"non ordinaire (lien symbolique ou autre, ni suivi ni lu) : {a}")
        faute = True
    for f in fichiers:
        t, illisible = textes_d_un_fichier(f)
        if illisible:
            lignes.append(f"illisible : {f}")
            faute = True
            continue
        n = set()
        for x in t:
            n |= idx.chercher(x)
        if n:
            lignes.append(f"fenêtre(s) retrouvée(s) : {f} : {len(n)}")
            faute = True
    lignes.insert(0, f"fenêtres cherchées : {len(idx.fenetres)} (textes honnêtes {idx.textes}, de moins de {LARGEUR} "
                     f"caractères {idx.courts}, fenêtres d'un seul caractère répété ignorées {idx.ignorees}) ; fichiers "
                     f"parcourus : {len(fichiers)} ; entrées non ordinaires : {len(autres)}")
    n_f = sum(1 for x in lignes if x.startswith(("fenêtre(s) retrouvée(s)", "illisible", "non ordinaire")))
    lignes.append(f"FENÊTRES RETROUVÉES OU FICHIERS ILLISIBLES OU NON ORDINAIRES : {n_f}" if faute
                  else "AUCUNE FENÊTRE D'UN TEXTE HONNÊTE")
    return lignes, faute


def _jetons_environnement() -> tuple[list[tuple[str, str]], list[str]]:
    vals = [(k, os.environ.get(k) or "") for k in JETONS]
    manquants = [k for k in JETONS_EXIGES if len(os.environ.get(k) or "") < 8]
    return [(k, v) for k, v in vals if len(v) >= 8], manquants


def montrer(textes: str, largeur: int) -> None:
    idx = Fenetres(textes_honnetes(textes))
    vals, manquants = _jetons_environnement()
    if manquants:
        print(f"--  masquage partiel : {', '.join(manquants)} absent(s) ou trop court(s) dans l'environnement")
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    for ligne in sys.stdin:
        m = ligne.rstrip("\n")
        for _, v in vals:
            m = m.replace(v, "***")
        if idx.chercher(m):
            pre = re.match(r"^(\s*(?:OK|KO|--)\s+\S+\s)", m)
            m = f"{pre.group(1) if pre else ''}(ligne retirée : {len(m)} caractères, empreinte {sha_texte(m)[:12]} ; " \
                "fenêtre d'un texte honnête)"
        elif len(m) > largeur:
            m = m[:largeur] + " […]"
        print(m, flush=True)


def jetons(chemins: list[str]) -> tuple[list[str], bool]:
    vals, manquants = _jetons_environnement()
    if manquants:
        raise Usage(f"jetons {', '.join(manquants)} absents ou trop courts dans l'environnement : recherche impossible")
    fichiers, autres = fichiers_de(chemins)
    lignes, faute = [], False
    comptes = {k: 0 for k, _ in vals}
    for a in autres:
        lignes.append(f"non ordinaire (lien symbolique ou autre, ni suivi ni lu) : {a}")
        faute = True
    for f in fichiers:
        try:
            b = f.read_bytes()
        except OSError:
            lignes.append(f"illisible : {f}")
            faute = True
            continue
        for k, v in vals:
            n = b.count(v.encode())
            if n:
                comptes[k] += n
                lignes.append(f"jeton retrouvé : {f} ({k}, {n} occurrence(s))")
                faute = True
    lignes.insert(0, "valeurs cherchées : " + " ; ".join(f"{k} : {n} occurrence(s)" for k, n in comptes.items())
                  + f" ; fichiers parcourus : {len(fichiers)} ; entrées non ordinaires : {len(autres)}")
    lignes.append("JETONS RETROUVÉS OU FICHIERS ILLISIBLES OU NON ORDINAIRES" if faute else "AUCUN JETON")
    return lignes, faute


# ------------------------------------------------------------------------------------- répétition jouet

PASSAGES = ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ", "passage 3-manque : code 1 ",
            "passage 4-plafond-de-l-amorce : code 124 ", "passage 5-arret-du-module : code 1 ")
# lignes exigées dans le bloc indenté d'un passage (journal de l'instance, préfixe « | »)
DANS_LE_PASSAGE = {"passage 5-arret-du-module : code 1 ": ("ARRÊT pendant run ", "branche calcul/p4-jouet-r-v1 poussée")}
_DET = " ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT (99999999)"
CONFORMES = (f"récupération (passage-1-sain) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (passage-3-traces-seules) : code 4 ; RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES{_DET}",
             f"récupération (passage-4-plafond-traces-seules) : code 4 ; RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES{_DET}",
             f"récupération (passage-5-arret-du-module) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (arret-synthetique) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (gardes-reelles) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}",
             f"récupération (textes-degeneres) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}")
# ligne exigée dans le bloc d'une récupération conforme
DANS_LA_RECUPERATION = {f"récupération (passage-5-arret-du-module) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES{_DET}":
                        "    --  4a arrêt : "}
_KO1 = " : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC ; INSTANCE 99999999 NON DÉTRUITE : NŒUD DE LAZAR"
ARTEFACTS = {f"récupération ({nom}){_KO1}": f"    KO  {prefixe} " for nom, prefixe in (
    ("artefact-scores-manquants", "4c"),
    ("artefact-validation-manquante", "4c"),
    ("artefact-ajout-hors-perimetre", "1c"),
    ("artefact-scores-alteres", "2b"),
    ("artefact-sceau-des-scores-faux", "2b"),
    ("artefact-resultat-autre-manifeste", "2b"),
    ("artefact-scores-hors-plan", "4d"),
    ("artefact-chaine-longue-dans-un-tableau", "4d"),
    ("artefact-validation-a-4096-colonnes", "4d"),
    ("artefact-longueurs-par-jeton-doublees", "4d"),
    ("artefact-texte-dans-le-journal", "4f"),
    ("artefact-texte-echappe-dans-un-resultat", "4f"),
    ("artefact-texte-echappe-dans-une-trace", "4f"),
    ("artefact-texte-sans-sa-fenetre-du-milieu", "4f"),
    ("artefact-motif-d-arret-qui-recopie-un-texte", "4f"),
    ("artefact-texte-dans-les-traces-seules", "4f"),
    ("artefact-chaine-de-plus-de-200-caracteres", "4f"),
    ("artefact-fin-sans-resume-complet", "6f"),
    ("artefact-jeton-dans-une-trace", "7"),
    ("artefact-jeton-dans-les-traces-seules", "7"),
    ("artefact-copie-non-versee", "0"),
    ("artefact-versions-autres", "3f"),
    ("artefact-carte-autre", "6b"),
    ("artefact-etiquette-autre", "8"),
    ("artefact-etiquette-p4-v1-x", "8"),
    ("artefact-destruction-en-echec", "8"),
    ("artefact-instance-encore-listee", "8"))}
GARDEE = "    --  8 instance 99999999 gardée, non détruite : état "
REFUS = ("récupération (artefact-place-disque) : code 2 ; place disque insuffisante pour le clone (3 Go exigés) : "
         "récupération refusée, rien n'est cloné ni détruit",
         "récupération (artefact-traces-d-un-autre-lancement) : code 2 ; traces du lancement autres que S et "
         "l'identifiant (commit, identifiant ou création) : récupération refusée, rien n'est cloné ni détruit",
         "récupération (artefact-clonage-impossible) : code 2 ; clonage du dépôt distant impossible : récupération "
         "refusée, rien n'est détruit")
# chaîne v3 (VC2-depense-03) : refus en code 2 après la lecture des traces (place, clonage) : état de l'instance gardée et
# heure limite de destruction écrits dans le bloc du refus
DANS_LE_REFUS = {REFUS[0]: GARDEE, REFUS[2]: GARDEE}
# chaîne v3 (VC2-donnees-01) : repli de l'affichage (module commun de S illisible) : ligne écrite par la répétition après
# ses propres contrôles de la sortie de cette récupération
REPLI = ("récupération en repli de l'affichage (artefact-repli-de-l-affichage) : code 1 ; KO 4f ; chaque ligne filtrée "
         "réduite à ses 40 premiers caractères, sa longueur et son empreinte courte ; instance gardée, état et heure "
         "limite de destruction écrits ; aucune destruction")
SANS_AFFICHAGE = ("aucun jeton affiché par les récupérations", "aucune fenêtre affichée par les récupérations")
SCRIPTS = {"recuperation_p4_v1.sh", "repetition_jouet_p4_v1.sh", "outils_essais_p4_v1.py", "verifications_p4_v1.py"}
# lecture jouet (module v2, CL3-01) : la lecture sans --prereg d'un run décisif est refusée sans rien écrire ; un run jouet
# non décisif (même configuration jouet, lancé sans --prereg sur les résultats du passage 1) se lit sans --prereg
LECTURE = re.compile(r"lecture jouet \(run-non-decisif\) : code 0 ; issue L[0-9]{1,2}")
REFUS_LECTURE = "lecture jouet sans --prereg du run décisif (passage-1-sain) : code 1 ; refusée sans rien écrire"


def bloc_indente(lignes: list[str], i: int) -> list[str]:
    """Lignes indentées (quatre espaces) qui suivent immédiatement la ligne i : le bloc de cette récupération."""
    j = i + 1
    while j < len(lignes) and lignes[j].startswith("    "):
        j += 1
    return lignes[i + 1:j]


def repetition(code: str, journal: str, nom: str, sha: str) -> list[str]:
    lignes = lire(journal).split("\n")
    exigees = [f"commit du code répété : {code}", f"candidat répété : {nom} {sha}", "FIN DE LA RÉPÉTITION", *CONFORMES,
               *ARTEFACTS, *REFUS, *SANS_AFFICHAGE, REFUS_LECTURE, REPLI]
    for e in exigees:
        if lignes.count(e) != 1:
            raise SystemExit(f"ligne absente ou en double : {e}")
    if sum(x.startswith("candidat répété : ") for x in lignes) != 1:
        raise SystemExit("plusieurs lignes « candidat répété »")
    if sum(bool(LECTURE.fullmatch(x)) for x in lignes) != 1 or sum(x.startswith("lecture jouet") for x in lignes) != 2:
        raise SystemExit("lecture jouet : une ligne « lecture jouet (run-non-decisif) : code 0 ; issue L… » et la ligne du "
                         "refus de la lecture sans --prereg du run décisif attendues, et elles seules")
    for p in PASSAGES:
        vus = [i for i, x in enumerate(lignes) if x.startswith(p)]
        if len(vus) != 1:
            raise SystemExit(f"passage : {p.strip()}")
        for attendu in DANS_LE_PASSAGE.get(p, ()):
            if not any(x.startswith("    | ") and attendu in x for x in bloc_indente(lignes, vus[0])):
                raise SystemExit(f"passage {p.strip()} : « {attendu.strip()} » absent de son journal")
    if sum("TOUS CONFORMES" in x for x in lignes) != len(CONFORMES) \
            or sum("INSTANCE DÉTRUITE PAR SON IDENTIFIANT" in x for x in lignes) != len(CONFORMES):
        raise SystemExit(f"{len(CONFORMES)} récupérations conformes, chacune suivie de la destruction, attendues")
    if sum("NON DÉTRUITE : NŒUD DE LAZAR" in x for x in lignes) != len(ARTEFACTS):
        raise SystemExit(f"{len(ARTEFACTS)} récupérations en échec, chacune sans destruction, attendues")
    if sum(x.startswith("récupération (") and " : code 2 ; " in x for x in lignes) != len(REFUS):
        raise SystemExit(f"{len(REFUS)} récupérations refusées en code 2 attendues")
    for etiquette in CONFORMES:
        bloc = bloc_indente(lignes, lignes.index(etiquette))
        ko = [x for x in bloc if x.startswith("    KO")]
        if ko:
            raise SystemExit(f"{etiquette} : KO {ko}")
        attendu = DANS_LA_RECUPERATION.get(etiquette)
        if attendu and not any(x.startswith(attendu) for x in bloc):
            raise SystemExit(f"{etiquette} : « {attendu.strip()} » absent de son bloc")
    for etiquette, prefixe in ARTEFACTS.items():
        bloc = bloc_indente(lignes, lignes.index(etiquette))
        ko = [x for x in bloc if x.startswith("    KO")]
        if len(ko) != 1 or not ko[0].startswith(prefixe):
            raise SystemExit(f"{etiquette} : KO {ko}")
        if not any(x.startswith(GARDEE) and "heure limite de destruction" in x for x in bloc):
            raise SystemExit(f"{etiquette} : état de l'instance gardée et heure limite de destruction absents")
    for etiquette, prefixe in DANS_LE_REFUS.items():
        bloc = bloc_indente(lignes, lignes.index(etiquette))
        if not any(x.startswith(prefixe) and "heure limite de destruction" in x for x in bloc):
            raise SystemExit(f"{etiquette[:60]} : état de l'instance gardée et heure limite de destruction absents du refus")
    scripts = {}
    for x in lignes:
        if x.startswith("script répété : "):
            m = re.fullmatch(r"script répété : ([a-z0-9_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
            if not m:
                raise SystemExit(f"ligne « script répété » mal formée : {x[:90]}")
            if m.group(1) in scripts:
                raise SystemExit(f"script répété en double : {m.group(1)}")
            scripts[m.group(1)] = m.group(2)
    if set(scripts) != SCRIPTS:
        raise SystemExit(f"scripts répétés {sorted(scripts)} : les quatre attendus exactement")
    return [f"{s} {scripts[s]}" for s in sorted(scripts)]


# journal → (verdict de sa dernière ligne, scripts qu'il éprouve exactement)
JOURNAUX = {
    "banc-lanceur-p4-v1.log": ("FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0",
                               {"lancer_p4_v1.sh", "verifications_p4_v1.py", "essais_lanceur_p4_v1.sh"}),
    "banc-surveillance-p4-v1.log": ("FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0",
                                    {"surveiller_p4_v1.sh", "controle_cinq_minutes_p4_v1.sh", "arreter_p4_v1.sh",
                                     "essais_surveillance_p4_v1.sh"}),
    "banc-arret-p4-v1.log": ("FIN DU BANC DE L'ARRÊT DE P4 ; cas non conformes : 0",
                             {"arreter_p4_v1.sh", "essais_arret_p4_v1.sh"}),
    "banc-traces-p4-v1.log": ("FIN DU BANC DU CONTRÔLE DES TRACES DE P4 ; cas non conformes : 0",
                              {"controler_traces_p4_v1.sh", "verifications_p4_v1.py", "essais_traces_p4_v1.sh",
                               "outils_essais_p4_v1.py"}),
    "banc-verifications-p4-v1.log": ("FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0",
                                     {"verifications_p4_v1.py", "essais_verifications_p4_v1.sh", "outils_essais_p4_v1.py"}),
    "banc-controles-p4-v1.log": ("FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0",
                                 {"controles_avant_depense_p4_v1.sh", "verifications_p4_v1.py", "essais_controles_p4_v1.sh",
                                  "outils_essais_p4_v1.py"}),
    "banc-scellement-p4-v1.log": ("FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0",
                                  {"sceller_p4_v1.sh", "verifications_p4_v1.py", "essais_scellement_p4_v1.sh",
                                   "outils_essais_p4_v1.py"}),
    "repetition-finale-p4-v1.log": ("RÉPÉTITION FINALE : CONFORME",
                                    {"sceller_p4_v1.sh", "controles_avant_depense_p4_v1.sh", "verifications_p4_v1.py",
                                     "repetition_finale_p4_v1.sh"}),
}


def preuves(dossier: str, noms: list[str]) -> list[str]:
    noms = noms or list(JOURNAUX)
    inconnus = [n for n in noms if n not in JOURNAUX]
    if inconnus or len(set(noms)) != len(noms):
        raise SystemExit(f"journaux nommés inconnus ou en double : {noms}")
    vus: dict[str, str] = {}
    for nom in noms:
        verdict, attendus = JOURNAUX[nom]
        p = Path(dossier) / nom
        if not p.is_file():
            raise SystemExit(f"journal {nom} absent ou illisible")
        lignes = lire(p).split("\n")
        non_vides = [x for x in lignes if x.strip()]
        if not non_vides or non_vides[-1] != verdict:
            raise SystemExit(f"journal {nom} : dernière ligne ≠ « {verdict} »")
        fautes = [x for x in lignes if "NON CONFORME" in x or x.lstrip().startswith(("Traceback", "JETON AFFICHÉ",
                                                                                      "FENÊTRE AFFICHÉE"))]
        if fautes:
            raise SystemExit(f"journal {nom} : ligne d'échec avant le verdict : {fautes[0].strip()[:90]}")
        propres = set()
        for x in lignes:
            if x.startswith("script éprouvé : "):
                m = re.fullmatch(r"script éprouvé : ([a-z0-9_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
                if not m:
                    raise SystemExit(f"journal {nom} : ligne « script éprouvé » mal formée : {x[:90]}")
                if vus.setdefault(m.group(1), m.group(2)) != m.group(2):
                    raise SystemExit(f"{m.group(1)} éprouvé sous deux empreintes")
                propres.add(m.group(1))
        if not propres:
            raise SystemExit(f"journal {nom} : aucune ligne « script éprouvé »")
        if propres != attendus:
            raise SystemExit(f"journal {nom} : scripts éprouvés ≠ attendus (manquants {sorted(attendus - propres)}, "
                             f"en trop {sorted(propres - attendus)})")
    return [f"{s} {vus[s]}" for s in sorted(vus)]


USAGE = ("usage : go RACINE PREREG JOUR BORNE | accord RACINE PREREG R-… JOUR | module RACINE PREREG | rapports NOM=SHA… | "
         "fenetres TEXTES CHEMIN… | montrer TEXTES [LONGUEUR] | jetons CHEMIN… | "
         "repetition CODE JOURNAL CANDIDAT_NOM CANDIDAT_SHA | preuves DOSSIER [JOURNAL …]")


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 6 and argv[1] == "go":
            print(go(*argv[2:6]))
        elif len(argv) == 6 and argv[1] == "accord":
            print(accord(*argv[2:6]))
        elif len(argv) == 4 and argv[1] == "module":
            print("\n".join(module(*argv[2:4])))
        elif len(argv) >= 3 and argv[1] == "rapports":
            print("\n".join(rapports(argv[2:])))
        elif len(argv) >= 4 and argv[1] == "fenetres":
            lignes, faute = fenetres(argv[2], argv[3:])
            print("\n".join(lignes))
            return 1 if faute else 0
        elif len(argv) in (3, 4) and argv[1] == "montrer":
            if len(argv) == 4 and not argv[3].isdigit():
                raise Usage("LONGUEUR : entier attendu")
            montrer(argv[2], int(argv[3]) if len(argv) == 4 else 300)
        elif len(argv) >= 3 and argv[1] == "jetons":
            lignes, faute = jetons(argv[2:])
            print("\n".join(lignes))
            return 1 if faute else 0
        elif len(argv) == 6 and argv[1] == "repetition":
            print("\n".join(repetition(*argv[2:6])))
        elif len(argv) >= 3 and argv[1] == "preuves":
            print("\n".join(preuves(argv[2], argv[3:])))
        else:
            print(USAGE, file=sys.stderr)
            return 2
    except Usage as e:
        print(str(e), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
