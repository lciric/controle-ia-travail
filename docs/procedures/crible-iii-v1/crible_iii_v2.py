"""Noyau du crible (iii) de l'organisme d'idéation — v2 (fichier neuf ; suit `crible_iii_v1.py`, gardé tel quel et encore
importé par la mesure ; corrections M1 et m3 du tour 1 de la contre-lecture du code, `contre-lecture-code-crible-iii-tour1-v1.md` :
une exception du gardien ou d'un monde arrête le crible (code 3) sans perdre d'appel ; un arrêt réel survenu après la ligne du
minimum la remplace ; pièce qui fera foi :
`docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-version-foi-v1.md`, `91b4bf30…`).

Deux passes : Pr-2 (`opus55`) choisit vingt ensembles de 1 à 3 traits (gabarit G1), un filtre déterministe sans modèle ni juge
en garde six, Pr-4 (`fable52`) écrit une carte par ensemble (gabarit G2) ; bras S (G0 du pilote), D, H (ensembles du
programme), B (écriture par Pr-2 sur les ensembles mêmes de D). 20 mondes, 5 files de 4 mondes (le monde r va à la file
r modulo 5), deux étapes par monde (S, passe 1 et H ensemble ; puis D et B ensemble), borne de 3 000 s par appel et de
7 200 s par monde, garde de départ de 4 × 7 200 s + 2 h, puis de 7 200 s + 2 h au départ de chaque monde.

Ce module ne lit aucun monde, aucun oracle, aucune issue ; il n'appelle rien : l'appel d'un proposeur, le gardien et l'horloge
lui sont passés (`jouer_crible`). Bibliothèque standard et numpy (graines, R9). Aucune valeur de clé, aucun identifiant de
modèle : seules les clés de configuration `opus55` et `fable52` (R-2690).
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import threading
import time
from datetime import date

import numpy as np

VERSION = "crible-iii-v1"
ETIQUETTE = "crible-iii-v1"
N_MONDES = 20
MONDES = tuple(range(1, N_MONDES + 1))
FILES = 5
PR2, PR4 = "opus55", "fable52"
PROPOSEURS = (PR4, PR2)
BRAS = ("S", "P1", "H", "D", "B")
PROPOSEUR_DU_BRAS = {"S": PR4, "P1": PR2, "H": PR4, "D": PR4, "B": PR2}
GABARIT_DU_BRAS = {"S": "G0", "P1": "G1", "H": "G2", "D": "G2", "B": "G2"}
APPELS_ATTENDUS = {PR4: 60, PR2: 40}
PARTS_USD = {PR2: 80.0, PR4: 180.0}
PART_MACHINE_USD = 3.0
FOURNISSEUR = {PR2: "claude", PR4: "claude"}   # une seule clé sert les deux relais : un seul fournisseur
BORNES_GELEES = {"appel_s": 3000.0, "monde_s": 7200.0, "marge_s": 7200.0}
OCTETS_MAX_G12 = 53000
DIMENSION = 8
ENSEMBLES_DEMANDES = 20
ENSEMBLES_RETENUS = 6
TAILLE_MIN, TAILLE_MAX = 1, 3
MINIMUM_COMPLETS = 16
TAUX_LIMITE_DEBIT = 0.05
APPELS_MIN_LIMITE = 10
GO_ENVELOPPE = "GO-2026-11-15-06"
PLAFONDS_GO = {"credits": 260.0, "hors": 3.0}
MOTS_GO = {"credits": ("crible (iii)", PR4, PR2), "hors": ("crible", "machine")}
EPS = 1e-9


class Refus(Exception):
    """Refus nommé avant tout appel (code 2) : rien n'est appelé."""


class Arret(Exception):
    """Arrêt nommé pendant le crible : `ligne` est la ligne de la liste d'arrêt, `code` le code de sortie du lanceur."""

    def __init__(self, ligne, motif, code=3, appel=None):
        super().__init__(f"{ligne} : {motif}")
        self.ligne, self.motif, self.code, self.appel = ligne, motif, code, appel


def json_canonique(objet):
    return json.dumps(objet, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_texte(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


# --- files et bornes ----------------------------------------------------------------------------------------------------------

def file_du_monde(r):
    if not (isinstance(r, int) and not isinstance(r, bool) and r in MONDES):
        raise Refus(f"monde {r!r} hors de 1 à {N_MONDES}")
    return r % FILES


def files_des_mondes(mondes=MONDES):
    """Affectation fixée avant tout appel, indépendante de toute réponse : le monde r va à la file r modulo 5, dans l'ordre
    croissant de r."""
    out = {f: [] for f in range(FILES)}
    for r in sorted(mondes):
        out[file_du_monde(r)].append(r)
    return out


def garde_de_depart(bornes=None):
    b = bornes or BORNES_GELEES
    pire_file = max(len(v) for v in files_des_mondes().values()) * b["monde_s"]
    return pire_file + b["marge_s"]


def garde_d_un_monde(bornes=None):
    b = bornes or BORNES_GELEES
    return b["monde_s"] + b["marge_s"]


def marge_d_un_monde(echeance_s, t, bornes=None):
    """Au départ de chaque monde : au moins la borne du monde + 2 h avant l'échéance ; sinon arrêt (A) sans monde neuf."""
    return echeance_s - t >= garde_d_un_monde(bornes)


def exiger_bornes(bornes, mode):
    """Les bornes gelées en mode réel ; des bornes réduites (même forme) seulement à blanc (essais à horloge rapide)."""
    if set(bornes) != set(BORNES_GELEES) or any(not (isinstance(v, (int, float)) and v > 0) for v in bornes.values()):
        raise Refus("bornes : appel_s, monde_s, marge_s > 0 attendues")
    if mode == "reel" and bornes != BORNES_GELEES:
        raise Refus("mode réel : bornes gelées seulement (3 000 s par appel, 7 200 s par monde, marge de 2 h)")
    if bornes["appel_s"] * 2 > bornes["monde_s"] + EPS:
        raise Refus("bornes : deux appels en série doivent tenir dans la borne du monde")
    return bornes


# --- graines (R9) ---------------------------------------------------------------------------------------------------------------

def racine_graines(texte_sha256):
    if not (isinstance(texte_sha256, str) and re.fullmatch(r"[0-9a-f]{64}", texte_sha256)):
        raise Refus("racine des graines : empreinte de 64 caractères hexadécimaux du texte qui fait foi")
    return int(texte_sha256, 16)


def graine_monde_crible(secret, phrase, empreinte_texte_hex, r):
    """Graine du monde r (1 à 20) : fonction `graine_monde_pilote` du programme de mesure du pilote, étiquette neuve
    « crible-iii-v1 » : 2⁶⁴ + entier des 8 premiers octets (gros-boutiste) de sha256(étiquette ∥ 0 ∥ secret (32 octets) ∥ 0 ∥
    phrase UTF-8 ∥ 0 ∥ empreinte du texte (32 octets) ∥ 0 ∥ r (1 octet))."""
    if not (isinstance(secret, bytes) and len(secret) == 32):
        raise Refus("secret : 32 octets")
    b = phrase.encode("utf-8") if isinstance(phrase, str) else b""
    if b"\x00" in b or not b:
        raise Refus("phrase : non vide, sans octet nul")
    e = bytes.fromhex(empreinte_texte_hex)
    if len(e) != 32:
        raise Refus("empreinte du texte : 32 octets")
    if r not in MONDES:
        raise Refus(f"r ∈ 1 à {N_MONDES}")
    h = hashlib.sha256(ETIQUETTE.encode() + b"\x00" + secret + b"\x00" + b + b"\x00" + e + b"\x00" + bytes([r])).digest()
    return 2 ** 64 + int.from_bytes(h[:8], "big")


def graine_h(racine, r):
    """Graine des ensembles au hasard de H dans le monde r : (r, 40) sous la racine ; ne dépend ni du monde, ni du secret, ni de
    la passe 1."""
    if not isinstance(racine, int) or isinstance(racine, bool) or racine < 0:
        raise Refus("graine de H : racine entière (empreinte du texte qui fait foi)")
    return np.random.SeedSequence(entropy=racine, spawn_key=(r, 40))


# --- passe 1 : analyseur gelé ---------------------------------------------------------------------------------------------------

def _entier_trait(x):
    return type(x) is int and 0 <= x < DIMENSION


def analyser_passe1(texte):
    """Ensembles valides de la réponse brute de la passe 1 : premier bloc ```json … ``` (sinon le texte entier), une liste ;
    un ensemble valide est une liste de 1 à 3 entiers distincts de 0 à 7 ; forme canonique : tuple trié ; les 20 premiers
    valides gardés, les suivants ignorés et comptés ; invalides comptés. Rien d'autre n'est lu."""
    if not isinstance(texte, str):
        raise Refus("analyseur : la réponse brute (texte) seulement")
    m = re.search(r"```json\s*(.*?)\s*```", texte, re.S)
    brut = m.group(1) if m else texte
    try:
        obj = json.loads(brut)
    except (ValueError, RecursionError):
        return {"valides": [], "invalides": 0, "ignores": 0, "lecture": "réponse illisible (JSON)"}
    if isinstance(obj, dict) and isinstance(obj.get("ensembles"), list):
        obj = obj["ensembles"]
    if not isinstance(obj, list):
        return {"valides": [], "invalides": 0, "ignores": 0, "lecture": "réponse sans liste d'ensembles"}
    valides, invalides, ignores = [], 0, 0
    for x in obj:
        ok = (isinstance(x, list) and TAILLE_MIN <= len(x) <= TAILLE_MAX and all(_entier_trait(t) for t in x)
              and len(set(x)) == len(x))
        if not ok:
            invalides += 1
        elif len(valides) < ENSEMBLES_DEMANDES:
            valides.append(tuple(sorted(x)))
        else:
            ignores += 1
    return {"valides": valides, "invalides": invalides, "ignores": ignores, "lecture": None}


# --- traits employés par une loi (mesure de l'exécution ; archive du filtre) ---------------------------------------------------

def traits_employes(loi, ecart=1e-6):
    """Le trait j est employé si un nœud softmax a des poids de colonne j non tous égaux entre issues (écart > 10⁻⁶), si un nœud
    si_sinon conditionne sur z_j, ou si une transformée oscille sur z_j."""
    out = set()

    def voir(n):
        if not isinstance(n, dict):
            return
        t = n.get("type")
        if t == "softmax":
            p = n.get("poids") or []
            if p and all(isinstance(l, list) for l in p):
                for j in range(min(len(l) for l in p)):
                    col = [l[j] for l in p]
                    if all(isinstance(v, (int, float)) for v in col) and max(col) - min(col) > ecart:
                        out.add(j)
        elif t == "si_sinon":
            c = n.get("condition") or {}
            if isinstance(c, dict) and type(c.get("indice")) is int:
                out.add(c["indice"])
            voir(n.get("si"))
            voir(n.get("sinon"))
        elif t == "par_sous_population":
            for v in (n.get("lois") or {}).values():
                voir(v)
            voir(n.get("defaut"))
        elif t == "melange":
            for v in n.get("composantes") or []:
                voir(v)
        elif t == "transformee":
            o = n.get("oscillation")
            if isinstance(o, dict) and type(o.get("trait")) is int:
                out.add(o["trait"])
            voir(n.get("base"))
    voir(loi)
    return out


# --- filtre gelé ---------------------------------------------------------------------------------------------------------------

def _jaccard(a, b):
    a, b = set(a), set(b)
    return 1.0 - len(a & b) / len(a | b)


def exiger_entrees_du_filtre(valides, traits_archive):
    """Le filtre ne reçoit que les ensembles lus dans la réponse brute de la passe 1 (tuples triés d'entiers) et les traits des
    lois de l'archive (listes d'entiers) : tout autre objet (monde, devis, oracle, issue) est refusé, nommé."""
    if not isinstance(valides, list) or any(not isinstance(e, tuple) or not all(_entier_trait(t) for t in e) for e in valides):
        raise Refus("filtre : ensembles de la passe 1 seulement (tuples d'entiers de 0 à 7)")
    if not isinstance(traits_archive, list) or any(not isinstance(t, (list, tuple, set, frozenset))
                                                    or not all(_entier_trait(x) for x in t) for t in traits_archive):
        raise Refus("filtre : traits des lois de l'archive seulement (listes d'entiers de 0 à 7)")


def filtre(valides, traits_archive):
    """(1) doublons retirés (première occurrence gardée) ; (2) retrait des ensembles inclus dans les traits d'une loi de
    l'archive ; (3) premier choisi = le premier dans l'ordre des noms (ordre lexicographique des tuples triés), puis, tant que
    moins de six sont choisis, l'ensemble restant qui maximise sa plus petite distance de Jaccard aux déjà choisis, égalités par
    l'ordre des noms ; (4) moins de six restants : tous, comptés. Aucun modèle, aucun juge, aucune issue."""
    exiger_entrees_du_filtre(valides, traits_archive)
    vus, uniques, doublons = set(), [], 0
    for e in valides:
        if e in vus:
            doublons += 1
            continue
        vus.add(e)
        uniques.append(e)
    arch = [set(t) for t in traits_archive]
    restants = [e for e in uniques if not any(set(e) <= a for a in arch)]
    retires_archive = len(uniques) - len(restants)
    restants.sort()
    choisis = []
    if restants:
        choisis.append(restants.pop(0))
    while restants and len(choisis) < ENSEMBLES_RETENUS:
        dist = {e: min(_jaccard(e, c) for c in choisis) for e in restants}
        m = max(dist.values())
        # égalités par l'ordre des noms : parmi les maxima, le premier dans l'ordre lexicographique
        meilleur = min(e for e in restants if abs(dist[e] - m) <= 1e-12)
        restants.remove(meilleur)
        choisis.append(meilleur)
    return {"retenus": choisis, "k": len(choisis), "doublons": doublons, "retires_archive": retires_archive,
            "moins_de_six": len(choisis) < ENSEMBLES_RETENUS}


def tirer_ensembles_h(racine, r):
    """Vingt ensembles tirés par le programme : taille uniforme sur {1, 2, 3}, traits uniformes sans remise parmi 8."""
    rng = np.random.default_rng(graine_h(racine, r))
    out = []
    for _ in range(ENSEMBLES_DEMANDES):
        t = int(rng.integers(TAILLE_MIN, TAILLE_MAX + 1))
        out.append(tuple(sorted(int(x) for x in rng.choice(DIMENSION, size=t, replace=False))))
    return out


# --- gabarits G1 et G2 (rédaction gelée ; aucun mot sur les conditions, les interactions ou les sortes d'effets, R-2504) -------

CONSIGNE_G1 = ("Sans proposer de loi, rends vingt ensembles distincts de 1 à 3 traits (indices entiers de 0 à 7, ceux des traits "
               "z0 à z7 du contexte ci-dessus) qui semblent porter de l'information sur l'issue au-delà des lois déjà retenues "
               "(archive). Réponds par un seul bloc ```json … ``` (le premier bloc ```json de ta réponse est le seul lu) : une "
               "liste de vingt listes d'entiers, par exemple [[0], [1, 5], [2, 3, 7]], et rien d'autre. Un ensemble est une "
               "liste de 1 à 3 entiers distincts de 0 à 7 ; tout autre élément est ignoré ; au-delà du vingtième, un ensemble "
               "est ignoré.")


def consigne_g2(k):
    return (f"Écris exactement {k} carte{'s' if k > 1 else ''}, une par ensemble ci-dessus, dans l'ordre : la carte numéro i "
            "emploie les traits de l'ensemble i ; elle peut employer aussi le trait de la loi déjà retenue (archive) ; aucun "
            "autre trait. Chaque carte suit la forme et la grammaire de la consigne du début (un seul bloc ```json … ``` : "
            "une liste d'objets {\"enonce\", \"loi_predictive\"}, et rien d'autre).")


def bloc_des_ensembles(ensembles):
    """Les k ensembles numérotés, entiers seuls, reconstruits depuis les formes canoniques (aucun texte de la passe 1)."""
    if not ensembles or any(not isinstance(e, tuple) or not e or not all(_entier_trait(t) for t in e) for e in ensembles):
        raise Refus("bloc des ensembles : au moins un ensemble canonique attendu")
    lignes = [f"Ensemble {i} : [{', '.join(str(t) for t in e)}]" for i, e in enumerate(ensembles, start=1)]
    return "Ensembles de traits (un par carte, dans l'ordre) :\n" + "\n".join(lignes) + "\n"


def contexte_de_g0(texte_g0, consigne_g0):
    """Le bloc JSON du contexte servi (épisodes, archive {K1}, grammaire) pris dans G0 : G0 = consigne, ligne vide, bloc."""
    tete = consigne_g0 + "\n\n"
    if not (isinstance(texte_g0, str) and texte_g0.startswith(tete) and texte_g0[len(tete):].startswith("```json\n")
            and texte_g0.endswith("\n```\n")):
        raise Refus("G0 : forme « consigne, ligne vide, bloc ```json … ``` » attendue (texte servi du pilote)")
    return texte_g0[len(tete):]


def texte_g1(texte_g0, consigne_g0):
    """G1 : les mêmes pièces servies (le contexte de G0), puis la consigne de la passe 1 ; aucune loi demandée."""
    return contexte_de_g0(texte_g0, consigne_g0) + "\n" + CONSIGNE_G1 + "\n"


def texte_g2(texte_g0, ensembles):
    """G2 : G0, puis le bloc des k ensembles numérotés et la consigne d'écriture (même G2 pour D, H et B)."""
    return texte_g0 + "\n" + bloc_des_ensembles(ensembles) + "\n" + consigne_g2(len(ensembles)) + "\n"


def gabarits_sha256(consigne_g0):
    """Empreinte des parties fixes des gabarits neufs (gelées au code ; recopiées à l'addendum d'empreintes)."""
    return {"G1": sha256_texte(CONSIGNE_G1), "G2": sha256_texte(consigne_g2(6) + "|" + consigne_g2(1) + "|"
                                                                   + bloc_des_ensembles([(0,), (1, 2, 3)])),
            "G0_consigne": sha256_texte(consigne_g0)}


def exiger_texte_passe2(texte, texte_g0, ensembles):
    """Texte servi d'une passe 2 égal à G2 bâti sur G0 et le bloc d'ensembles reconstruit ; sinon arrêt avant cet appel."""
    if texte != texte_g2(texte_g0, ensembles):
        raise Arret("texte servi de passe 2", "différent de G2 et du bloc d'ensembles reconstruit")
    return texte


def exiger_texte_b(texte_d, texte_b):
    """Texte servi de B égal à l'octet à celui de D (mêmes ensembles) ; sinon arrêt avant l'appel de B."""
    if not (isinstance(texte_b, str) and texte_b.encode("utf-8") == texte_d.encode("utf-8")):
        raise Arret("texte servi de B", "différent de celui de D (mêmes ensembles exigés, à l'octet)")
    return texte_b


def exiger_octets(texte, quoi):
    n = len(texte.encode("utf-8"))
    if n > OCTETS_MAX_G12:
        raise Refus(f"{quoi} : texte servi de {n} octets > {OCTETS_MAX_G12} (les plafonds de session tiennent jusqu'à 53 976)")
    return n


def pire_texte_g2(texte_g0):
    """Le plus long G2 possible (six ensembles de trois traits) : contrôlé avant tout appel."""
    return texte_g2(texte_g0, [(5, 6, 7)] * ENSEMBLES_RETENUS)


# --- lignes de GO (registre lu comme la garde de calcul : 8 colonnes) -----------------------------------------------------------

LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
PLAFOND = re.compile(r"([0-9]+(?:[.,][0-9]+)?) USD")


def lire_registre_go(texte):
    go = {}
    for n, ligne in enumerate(texte.splitlines(), 1):
        if not LIGNE_GO.match(ligne):
            continue
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(c) != 8:
            raise Refus(f"registre des GO mal formé ligne {n} : 8 colonnes attendues")
        ident, accorde, typ, perimetre, plafond, echeance, par, ref = c
        try:
            a = date.fromisoformat(accorde)
            e = None if echeance == "—" else date.fromisoformat(echeance)
        except ValueError:
            raise Refus(f"registre des GO mal formé ligne {n} : dates illisibles") from None
        if ident in go and not perimetre.lower().startswith("extension"):
            raise Refus(f"registre des GO : identifiant {ident} en double")
        go.setdefault(ident, {"accorde": a, "type": typ, "perimetre": perimetre, "plafond": plafond, "echeance": e,
                              "par": par, "ref": ref})
    return go


def exiger_ligne_go(go, ident, genre, aujourd_hui):
    """Ligne « calcul » propre au crible : accordée par Lazar, dans sa période, non révoquée, citant l'enveloppe
    GO-2026-11-15-06, aux mots exigés, au plafond exact ; toute autre forme : la commande refuse (aucune dépense)."""
    g = go.get(ident)
    if g is None:
        raise Refus(f"{ident} absent du registre des GO : aucune dépense sans ligne « calcul » inscrite")
    if g["type"] != "calcul" or g["par"] != "Lazar":
        raise Refus(f"{ident} : ligne de type « calcul » accordée par Lazar exigée")
    if g["echeance"] is None or not (g["accorde"] <= aujourd_hui <= g["echeance"]):
        raise Refus(f"{ident} hors de sa période")
    if any(r["type"] == "révocation" and (ident in r["perimetre"] or ident in r["ref"]) for r in go.values()):
        raise Refus(f"{ident} révoqué")
    if GO_ENVELOPPE not in g["ref"] and GO_ENVELOPPE not in g["perimetre"]:
        raise Refus(f"{ident} ne cite pas {GO_ENVELOPPE}")
    manque = [m for m in MOTS_GO[genre] if m not in g["perimetre"]]
    if manque:
        raise Refus(f"{ident} : périmètre sans {manque}")
    m = PLAFOND.search(g["plafond"])
    if not m or abs(float(m.group(1).replace(",", ".")) - PLAFONDS_GO[genre]) > EPS:
        raise Refus(f"{ident} : plafond {g['plafond']!r} ≠ {PLAFONDS_GO[genre]:g} USD")
    return {"ident": ident, "plafond_usd": PLAFONDS_GO[genre], "echeance": str(g["echeance"])}


def lire_go_du_crible(texte_registre, go_credits, go_hors, aujourd_hui=None):
    if go_credits == go_hors:
        raise Refus("deux lignes distinctes exigées (part sur crédits, part hors crédits)")
    go = lire_registre_go(texte_registre)
    j = aujourd_hui or date.today()
    return {"credits": exiger_ligne_go(go, go_credits, "credits", j), "hors": exiger_ligne_go(go, go_hors, "hors", j)}


# --- ordonnanceur : files parallèles, deux étapes par monde ------------------------------------------------------------------

class Commun:
    """État partagé par les files, sous un seul verrou : drapeaux d'arrêt, dépense réglée et réservée par relais, appels faits,
    erreurs de limite de débit par fournisseur, état des mondes."""

    def __init__(self, plafonds, parts):
        self.verrou = threading.Lock()
        self.plafonds, self.parts = dict(plafonds), dict(parts)
        self.regle = {p: 0.0 for p in PROPOSEURS}
        self.reserve = {p: 0.0 for p in PROPOSEURS}
        self.appels = {p: 0 for p in PROPOSEURS}
        self.limites = {}
        self.faits_fournisseur = {}
        self.arret = None           # premier arrêt : {"ligne", "motif", "code", "heure"}
        self.minuterie = None       # arrêt (A) de la minuterie : plus aucun monde neuf, mondes commencés finis
        self.mondes = {r: "non commence" for r in MONDES}
        self.journal = []

    def note(self, texte):
        with self.verrou:
            self.journal.append(texte)

    def arreter(self, ligne, motif, code):
        with self.verrou:
            if self.arret is None or (self.arret.get("ligne") == "minimum" and ligne != "minimum"):
                self.arret = {"ligne": ligne, "motif": motif, "code": code}

    def arrete(self):
        with self.verrou:
            return self.arret is not None


def reponse_repondue(r, cartes):
    return r is not None and r.get("etat") == "complet" and any(c["etat"] == "admise" for c in cartes)


def jouer_crible(servis, appeler, gardien, maintenant, echeance_s, plafonds, parts=PARTS_USD, bornes=None, mode="a_blanc",
                 racine=None, traits_archive=None, texte_g0=None):
    """Joue les 100 appels du crible.

    - `servis[r]` : {"g0": texte G0, "g1": texte G1, "h": ensembles retenus de H} (bâtis et contrôlés avant tout appel) ;
    - `appeler(bras, proposeur, texte, monde, delai_s)` → {"etat", "cout_usd", "limite_debit", "coupe", "texte", …} ;
      une `Arret` qu'il lève (réponse brute ou témoin absent, coût au-dessus du pire cas) arrête le crible (code 3) ;
    - `gardien(monde, bras, proposeur, texte)` → (cartes, lecture) ;
    - `maintenant()` → secondes ; `echeance_s` : échéance de la minuterie de la machine ;
    - `traits_archive[r]` : traits des lois de l'archive {K1} du monde r (pour le filtre).
    Rend le relevé (dictionnaire) ; aucune exception ne sort après le premier appel."""
    bornes = exiger_bornes(dict(bornes or BORNES_GELEES), mode)
    if sorted(servis) != list(MONDES):
        raise Refus(f"mondes servis : exactement {N_MONDES}, de 1 à {N_MONDES}")
    if echeance_s - maintenant() < garde_de_depart(bornes):
        raise Refus(f"garde de départ : moins de {garde_de_depart(bornes):.0f} s avant l'échéance (4 × borne du monde + 2 h) : "
                    "aucun appel")
    c = Commun(plafonds, parts)
    appels, cartes, ensembles = [], [], {}
    verrou_listes = threading.Lock()
    fils_d_appel = []   # fils d'appel lancés ; tous attendus avant le relevé (complément de M1, couple 2, tour 1)

    def appel_borne(r, bras, texte, t0):
        p = PROPOSEUR_DU_BRAS[bras]
        ligne = {"monde": r, "bras": bras, "proposeur": p, "gabarit": GABARIT_DU_BRAS[bras],
                 "texte_servi_sha256": sha256_texte(texte), "octets": len(texte.encode("utf-8"))}
        if c.arrete():
            with verrou_listes:
                appels.append(dict(ligne, etat="non appele", appele=False, cause="arrêt du crible"))
            return None
        reste = bornes["monde_s"] - (maintenant() - t0)
        delai = min(bornes["appel_s"], reste)
        if delai <= 0:
            with verrou_listes:
                appels.append(dict(ligne, etat="echec", appele=False, coupe=True, cause="borne du monde atteinte"))
            return None
        with c.verrou:
            if c.regle[p] + c.reserve[p] + c.plafonds[p] > c.parts[p] + EPS:
                motif = f"{p} : part {c.parts[p]:g} USD atteinte au pire cas de l'appel suivant"
                if c.arret is None:
                    c.arret = {"ligne": "part", "motif": motif, "code": 3}
                appels.append(dict(ligne, etat="non appele", appele=False, cause=motif))
                return None
            c.reserve[p] += c.plafonds[p]
            c.appels[p] += 1
        r_appel, arret = None, None
        try:
            r_appel = appeler(bras, p, texte, r, delai)
        except Arret as e:
            arret, r_appel = e, (e.appel or {"etat": "echec", "cout_usd": c.plafonds[p], "cause": e.motif})
        except Exception as e:  # noqa: BLE001 — imprévu : arrêt (code 3), dépense comptée au plafond de session
            arret = Arret("exception de l'appel", f"{type(e).__name__} : {e}")
            r_appel = {"etat": "echec", "cout_usd": c.plafonds[p], "cause": "exception"}
        cout = float(r_appel.get("cout_usd") or 0.0)
        f = FOURNISSEUR[p]
        with c.verrou:
            c.reserve[p] -= c.plafonds[p]
            c.regle[p] += cout
            c.faits_fournisseur[f] = c.faits_fournisseur.get(f, 0) + 1
            if r_appel.get("limite_debit"):
                c.limites[f] = c.limites.get(f, 0) + 1
            n, k = c.faits_fournisseur[f], c.limites.get(f, 0)
            if arret is not None and (c.arret is None or c.arret.get("ligne") == "minimum"):
                c.arret = {"ligne": arret.ligne, "motif": arret.motif, "code": arret.code}
            if n >= APPELS_MIN_LIMITE and k / n > TAUX_LIMITE_DEBIT and (c.arret is None or c.arret.get("ligne") == "minimum"):
                c.arret = {"ligne": "limite de débit", "motif": f"{k} erreurs sur {n} appels du fournisseur {f}", "code": 3}
            if c.regle[p] >= c.parts[p] - EPS and (c.arret is None or c.arret.get("ligne") == "minimum"):
                c.arret = {"ligne": "part", "motif": f"{p} : dépense {c.regle[p]:.4f} atteint la part {c.parts[p]:g}", "code": 3}
        cs, lecture = ([], None)
        if r_appel.get("etat") in ("complet", "tronque") and bras != "P1":
            try:
                cs, lecture = gardien(r, bras, p, r_appel.get("texte") or "")
            except Exception as e:  # noqa: BLE001 — jamais un repli silencieux : arrêt (code 3), l'appel reste au relevé
                c.arreter("exception du gardien", f"monde {r}, {bras} : {type(e).__name__} : {e}", 3)
                cs, lecture = [], f"gardien en exception : {type(e).__name__}"
        with verrou_listes:
            appels.append(dict(ligne, appele=True, arret=arret is not None,
                               **{k2: v for k2, v in r_appel.items() if k2 not in ("texte",)}))
            for x in cs:
                cartes.append(dict(x, monde=r, bras=bras, proposeur=p))
        return dict(r_appel, cartes=cs, lecture=lecture)

    def jouer_monde(r, file):
        t0 = maintenant()
        s = servis[r]
        with c.verrou:
            c.mondes[r] = "en cours"
        res = {}

        def lancer(bras, texte):
            res[bras] = appel_borne(r, bras, texte, t0)
        tours = [threading.Thread(target=lancer, args=("S", s["g0"])), threading.Thread(target=lancer, args=("P1", s["g1"])),
                 threading.Thread(target=lancer, args=("H", texte_g2(s["g0"], s["h"])))]
        with verrou_listes:
            fils_d_appel.extend(tours)
        for t in tours[1:]:
            t.start()
        tours[0].start()
        tours[1].join()
        p1 = res.get("P1")
        e = {"monde": r, "file": file, "h_retenus": [list(x) for x in s["h"]]}
        if p1 is not None and p1.get("etat") == "complet":
            lu = analyser_passe1(p1.get("texte") or "")
            f = filtre(lu["valides"], [list(t) for t in traits_archive[r]])
            e.update(passe1={k2: v for k2, v in lu.items() if k2 != "valides"}, passe1_valides=[list(x) for x in lu["valides"]],
                     d_retenus=[list(x) for x in f["retenus"]], d_k=f["k"], doublons=f["doublons"],
                     retires_archive=f["retires_archive"])
            if f["retenus"]:
                td = texte_g2(s["g0"], f["retenus"])
                tb = texte_g2(s["g0"], f["retenus"])
                try:
                    exiger_texte_passe2(td, s["g0"], f["retenus"])
                    exiger_texte_b(td, tb)
                except Arret as x:
                    c.arreter(x.ligne, x.motif, x.code)
                d2 = [threading.Thread(target=lancer, args=("D", td)), threading.Thread(target=lancer, args=("B", tb))]
                with verrou_listes:
                    fils_d_appel.extend(d2)
                for t in d2:
                    t.start()
                for t in d2:
                    t.join()
            else:
                e["sans_passe2"] = "aucun ensemble après filtre"
        else:
            e["sans_passe2"] = "passe 1 " + ("non appelée" if p1 is None else str(p1.get("etat")))
        for t in (tours[0], tours[2]):
            t.join()
        rep = {b: reponse_repondue(res.get(b), (res.get(b) or {}).get("cartes", [])) for b in ("S", "H", "D", "B")}
        complet = all(rep.values()) and bool(e.get("d_retenus"))
        e.update(repondus=rep, complet=complet, duree_s=round(maintenant() - t0, 3))
        with verrou_listes:
            ensembles[r] = e
        with c.verrou:
            c.mondes[r] = "complet" if complet else "incomplet"
            n_c = sum(1 for v in c.mondes.values() if v == "complet")
            n_e = sum(1 for v in c.mondes.values() if v == "en cours")
            n_n = sum(1 for v in c.mondes.values() if v == "non commence")
            if n_c + n_e + n_n < MINIMUM_COMPLETS and c.arret is None:
                c.arret = {"ligne": "minimum", "code": 0,
                           "motif": f"{n_c} complets + {n_e} en cours + {n_n} non commencés < {MINIMUM_COMPLETS}"}

    def jouer_file(file, mondes):
        for r in mondes:
            if c.arrete():
                return
            if not marge_d_un_monde(echeance_s, maintenant(), bornes):
                with c.verrou:
                    if c.minuterie is None:
                        c.minuterie = f"moins de {garde_d_un_monde(bornes):.0f} s avant l'échéance au départ du monde {r}"
                return
            with c.verrou:
                if c.minuterie is not None:
                    return
            try:
                jouer_monde(r, file)
            except Exception as e:  # noqa: BLE001 — jamais un repli silencieux : arrêt (code 3), monde compté incomplet
                c.arreter("exception d'un monde", f"monde {r} : {type(e).__name__} : {e}", 3)
                with c.verrou:
                    c.mondes[r] = "incomplet"
                return

    fils = [threading.Thread(target=jouer_file, args=(f, m)) for f, m in sorted(files_des_mondes().items())]
    for t in fils:
        t.start()
    for t in fils:
        t.join()
    for t in fils_d_appel:  # un monde en exception laisse ses appels en vol : ils finissent et sont listés avant le relevé
        if t.ident is not None:
            t.join()
    arret = c.arret
    if arret is None and c.minuterie is not None:
        arret = {"ligne": "minuterie", "motif": c.minuterie, "code": 3}
    comptes = {}
    for a in appels:
        cle = f"{a['proposeur']}|{a['bras']}"
        comptes.setdefault(cle, {"complet": 0, "tronque": 0, "echec": 0, "non appele": 0})
        comptes[cle][a["etat"] if a["etat"] in comptes[cle] else "echec"] += 1
    return {"version": VERSION, "mode": mode, "bornes": bornes, "arret": arret, "mondes": {str(r): v for r, v in c.mondes.items()},
            "appels": sorted(appels, key=lambda a: (a["monde"], BRAS.index(a["bras"]))),
            "cartes": sorted(cartes, key=lambda x: (x["monde"], BRAS.index(x["bras"]), x["emplacement"])),
            "ensembles": {str(r): ensembles[r] for r in sorted(ensembles)},
            "depense_usd": {p: round(v, 8) for p, v in c.regle.items()}, "appels_faits": dict(c.appels),
            "limites_debit": dict(c.limites), "comptes": comptes, "journal": c.journal,
            "complets": sum(1 for v in c.mondes.values() if v == "complet")}


__all__ = [n for n in dir() if not n.startswith("_")]
