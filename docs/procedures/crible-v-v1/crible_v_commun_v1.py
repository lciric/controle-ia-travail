"""Constantes et outils communs du crible (v) de l'organisme d'idéation — code v1 (fichier neuf, R12).

Texte qui fait foi : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-version-foi-v2.md` (version qui fera foi v2 ;
copie à venir sous `prereg/`), sections « Métrique », « Seuil », « Plan d'analyse », « Liste d'arrêt » et « Devis ».
Aucun réseau, aucune clé, aucun appel. Bibliothèque standard seule (numpy n'est importé que par les modules qui calculent).

Ce module ne lit aucune issue et ne dit rien d'un monde : il porte les nombres gelés du texte (N, B_a, ε, ε_strat, 0,8, seuils,
table W_min, règle de M, budget de durée, lignes de GO proposées) et les outils d'écriture scellée (mode `x`, compagnon
`.sha256`), pour que le lanceur, la mesure et la lecture disent les mêmes chaînes sans les retaper.
"""

import hashlib
import json
import math
import os

VERSION = "crible-v-commun-v1"

# --- dessin (« Plan d'analyse », « Taille ») ---------------------------------------------------------------------------------
N_MONDES = 20                         # N = 20 dans tous les cas (R-2992)
MONDES = tuple(range(1, N_MONDES + 1))
PROPOSEURS = ("fable52", "opus55", "argon", "astra")   # clés de la configuration v12 (ordre du pilote)
POSTES = {"argon": "Pr-1", "opus55": "Pr-2", "astra": "Pr-3", "fable52": "Pr-4"}
MOITIE_B = ("argon", "opus55")        # moitié bon marché b = {Pr-1, Pr-2}
MOITIE_E = ("astra", "fable52")       # moitié chère e = {Pr-3, Pr-4}
CARTES_MAX = 6
ETIQUETTE_GRAINE = b"crible-v-v1"     # à la place de « pilote-conditionnelles-v1 » (« Graines (R9) »)
ETIQUETTE_ORACLE = "oracle-crible-v"  # cle("oracle-crible-v", empreinte du devis du monde)
ETIQUETTE_EPISODES = "crible-v-v1|episodes-developpement"   # étiquette neuve « crible-v-v1 » des épisodes (règle du bloc gelé)
EPISODES_DEVELOPPEMENT = 400
TIRAGES_PAR_MONDE = 8
GABARIT_SHA256 = "e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2"   # gabarit servi du pilote, inchangé

# --- métrique (« Métrique ») -------------------------------------------------------------------------------------------------
EPS = 0.01                            # ε = 0,01 nat
EPS_STRAT = 0.04                      # ε_strat = 0,04
SEUIL_Q = 0.8                         # a_w = 1 si q_w > 0,8 (strictement)
JEU_PUBLIC_N = 2000                   # jeu public d'instances (traits et sous-populations seulement)
ORACLE_N = 12000
TAU_PART, TAU_PART_LARGE, TAU_PLANCHER = 0.75, 0.25, 0.005
REECHANTILLONS = 10000
SEUILS_COURBE = (0.5, 0.6, 0.7, 0.8, 0.9)
# prix publics de l'offre standard lus le 14 novembre (note des prix v2, `b88253b8…`), USD par million (entrée, sortie)
PRIX_PUBLICS = {"fable52": (8.0, 40.0), "opus55": (4.0, 20.0), "astra": (10.0, 50.0), "argon": (2.0, 10.0)}

# --- seuils (« Seuil ») ---------------------------------------------------------------------------------------------------------
MIN_COMPLETS = 16                     # n_c ≥ 0,8 × 20
W_MIN = {16: 4, 17: 4, 18: 4, 19: 4, 20: 4}   # table gelée (annexe A, points 5 et 11), recalculée par programme par la lecture
ZONE_UTILE = 10                       # au moins 10 mondes complets avec C_T(w) ≥ 1
S_NOTABLE = 0.25
P_CHOIX_SEUIL = 0.05
BORD_EPROUVABLE = 4                   # « éprouvable » si 4 ≤ k_R ≤ n_c − 4

# --- durée (« Devis », sous-section qui fait foi) ---------------------------------------------------------------------------------
B_A_S = 900                           # borne par appel, donc par monde
BARRIERES_S = 6000                    # 100 minutes
BUDGET_MAX_S = 61200                  # 17 h
D_MAX_S = {1: 12400, 2: 15400}        # plus grande D qui tient sous 17 h, par M (sortie du devis, point 6)


def appels_pire_s(m):
    return math.ceil(N_MONDES / m) * B_A_S


def budget_depart_s(m, d):
    """Garde de départ (ligne « minuterie de la machine ») : 6 000 s de barrières + 3 D + ⌈20/M⌉ × B_a ; D = somme des quatre
    durées relevées (mise en place, génération et mesure rapportées à 20 mondes, rapatriement) et de l'énumération du placebo."""
    return BARRIERES_S + 3 * d + appels_pire_s(m)


def m_de_la_regle(d):
    """Règle de M sur B_a = 900 s : 1 si D ≤ 12 400 s ; 2 si D ≤ 15 400 s ; sinon None (« non lançable », mot de la mère)."""
    if not (isinstance(d, (int, float)) and not isinstance(d, bool) and math.isfinite(d) and d >= 0):
        return None
    for m in (1, 2):
        if d <= D_MAX_S[m] and budget_depart_s(m, d) <= BUDGET_MAX_S:
            return m
    return None


# --- lignes de GO proposées (« Lignes de GO proposées », montants de la branche « sonde neuve exigée ») ----------------------
GO_CRIBLE = {
    "kv1": {"montant_usd": 104.39, "perimetre_contient": ["crible (v)", "crédits de Claude"],
            "parts_usd": {"opus55": 40.0, "fable52": 60.0, "sonde": 4.39}},
    "kv2": {"montant_usd": 100.28, "perimetre_contient": ["crible", "hors crédits"],
            "parts_usd": {"argon": 46.80, "astra": 46.80, "machine": 3.0, "sonde": 3.68}},
}


class Refus(Exception):
    """Refus nommé (code 2) : rien n'est appelé."""


class Arret(RuntimeError):
    """Arrêt (code 3) : pièces versées, rien n'est lu."""

    def __init__(self, message, appel=None):
        super().__init__(message)
        self.appel = appel


# --- graine des mondes (« Graines (R9) ») ----------------------------------------------------------------------------------------

def graine_monde_crible(secret, phrase, empreinte_texte_hex, r):
    """Graine du monde r ∈ {1, …, 20} : 2⁶⁴ + entier des 8 premiers octets (gros-boutiste) de sha256(« crible-v-v1 » ∥ 0x00 ∥
    secret (32 octets) ∥ 0x00 ∥ phrase en UTF-8 (sans octet nul) ∥ 0x00 ∥ empreinte du texte scellé (32 octets) ∥ 0x00 ∥ r
    (1 octet)) : la fonction `graine_monde_pilote` du programme v4 du pilote, étiquette neuve, r de 1 à 20."""
    if not (isinstance(secret, bytes) and len(secret) == 32):
        raise Refus("secret : 32 octets")
    if not isinstance(phrase, str):
        raise Refus("phrase : texte")
    b = phrase.encode("utf-8")
    if b"\x00" in b or not b:
        raise Refus("phrase : non vide, sans octet nul")
    try:
        e = bytes.fromhex(empreinte_texte_hex)
    except (TypeError, ValueError):
        raise Refus("empreinte du texte : hexadécimal") from None
    if len(e) != 32:
        raise Refus("empreinte du texte : 32 octets")
    if isinstance(r, bool) or r not in MONDES:
        raise Refus(f"r ∈ {{1, …, {N_MONDES}}}")
    h = hashlib.sha256(ETIQUETTE_GRAINE + b"\x00" + secret + b"\x00" + b + b"\x00" + e + b"\x00" + bytes([r])).digest()
    return 2 ** 64 + int.from_bytes(h[:8], "big")


def racine_des_graines(empreinte_texte_hex):
    """Racine R9 : l'entier de l'empreinte sha256 du texte qui fera foi."""
    if not (isinstance(empreinte_texte_hex, str) and len(empreinte_texte_hex) == 64):
        raise Refus("racine des graines : empreinte de 64 chiffres hexadécimaux")
    return int(empreinte_texte_hex, 16)


# --- écriture scellée -------------------------------------------------------------------------------------------------------

def json_canonique(o):
    return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_octets(b):
    return hashlib.sha256(b).hexdigest()


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def ecrire_scelle_json(chemin, objet):
    """Écrit `objet` (JSON indenté) en mode `x` (jamais d'écrasement, R12) et son compagnon `.sha256` ; rend l'empreinte."""
    octets = (json.dumps(objet, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    sha = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def compagnon_egal(chemin):
    try:
        with open(chemin + ".sha256", encoding="utf-8") as f:
            return f.read().split()[0] == sha256_fichier(chemin)
    except (OSError, IndexError):
        return False


def lire_json_scelle(chemin, quoi):
    """Lit un JSON égal à son compagnon ; Refus sinon."""
    if not os.path.isfile(chemin):
        raise Refus(f"{quoi} absent : {chemin}")
    if not compagnon_egal(chemin):
        raise Refus(f"{quoi} différent de son compagnon (ou compagnon absent)")
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def clopper_pearson(x, n, a=0.05):
    """Intervalle de Clopper-Pearson bilatéral (bissection sur la loi binomiale exacte) ; forme du programme de l'annexe A."""
    from math import comb

    def queue_haute(c, p):
        return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(c, n + 1))

    def cdf(c, p):
        return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(0, c + 1))

    def biss(f):
        lo, hi = 0.0, 1.0
        for _ in range(200):
            mi = 0.5 * (lo + hi)
            if f(mi):
                hi = mi
            else:
                lo = mi
        return 0.5 * (lo + hi)
    if n <= 0:
        return 0.0, 1.0
    bas = 0.0 if x == 0 else biss(lambda p: queue_haute(x, p) >= a / 2)
    haut = 1.0 if x == n else biss(lambda p: cdf(x, p) <= a / 2)
    return bas, haut


def w_min_calcule(n):
    """Plus petit W dont la borne basse de Clopper-Pearson (95 %) dépasse 0,05 (définition de la section « Seuil »)."""
    return min(x for x in range(n + 1) if clopper_pearson(x, n)[0] > 0.05)


__all__ = [n for n in dir() if not n.startswith("_")]
