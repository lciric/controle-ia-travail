"""Mesure du crible (v) de l'organisme d'idéation — `mesure_crible_v_v1.py` (nom réservé par le texte qui fera foi ; fichier neuf,
R12). Dérivée de `mesure_pilote_v4.py` (`676d5f37…`), dont elle reprend la lecture des appels, le gardien (cartes admises par le
lanceur), l'oracle et l'attribution ; **lancée une seule fois** sur la machine du crible (le lanceur refuse une seconde mesure).

Texte : `crible-v-version-foi-v2.md` (version qui fera foi v2), sections « Métrique », « Seuil », « Plan d'analyse » (partie B,
« Mesure »), « Liste d'arrêt ». Programme pur : mêmes entrées → même corps de sortie ; aucun appel, aucun réseau ; lit les mondes
privés ; n'écrit ni loi ni devis de monde.

Usages :
  python3 -I -B mesure_crible_v_v1.py mesurer --mr2 DOSSIER --texte-sha256 H --mondes MONDES.json --certifiees CERTIFIEES.json
          --cartes CARTES.json --dollars DOLLARS.json --sortie SORTIE.json --sortie-fictive SORTIE-FICTIVE.json
  python3 -I -B mesure_crible_v_v1.py chrono --mr2 DOSSIER SORTIE.json      énumération exacte du placebo, pire cas (n_c = 20,
                                                                           k_R = 10), deux lancements, le plus long retenu

Ordre du calcul (« Partie B », « Mesure ») : (1) copies et décisions a_w — `decider`, qui ne reçoit que les lois des cartes de la
moitié bon marché, la loi K1 servie et le jeu public d'instances ; (2) l'oracle et les couvertures ; (3) les dollars ; (4) les bras
T, R, B, E, le placebo et les sensibilités, sauf le rejeu sous archive fictive ; la sortie principale est écrite et scellée ;
(5) le rejeu sous archive fictive, par sa fonction distincte (`rejeu_archive_fictive`), vers le second fichier scellé.

Codes : 0 conforme ; 2 refus nommé (aucune sortie) ; toute exception non nommée sort en code 1 sans sortie (ligne « exception de
la mesure » de la liste d'arrêt : rien n'est lu).
"""
import argparse
import datetime
import hashlib
import itertools
import json
import math
import os
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import crible_v_commun_v1 as K  # noqa: E402

VERSION = "mesure-crible-v-v1"
ATTENDUES = {  # empreintes des modules MR-2 nommés par le texte, en plus du contrôle de chaque compagnon
    "outils-v4/monde_riche_v4.py": "4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8",
    "outils-v1/complements_synthese_v1.py": "89eb7ba8c8cf8633541a6de8090767f74619e3f3968ebed8f894b1f8d593e9ba",
    "outils-v1/monde_riche_outils_v1.py": "1825b956eed638fe4daf3d7395a169fdbdf7c9679076d9ba3fb4a15cfd7ec85e",
}
Refus = K.Refus
_MR2 = {}


# --- modules MR-2 (même contrôle que la mesure du pilote) -------------------------------------------------------------------

def charger_mr2(racine):
    """(V4, M, P1, CS) depuis `racine` (dossier qui porte outils-v1 à outils-v4 : `orchestrator/mr2_v68/` de l'arbre ou
    `docs/notes/organisme-multi-generations-v1/` du dépôt, mêmes octets) ; chaque fichier nommé égal à son compagnon et à
    l'empreinte écrite ici, avant tout import."""
    if _MR2.get("racine") == racine:
        return _MR2["V4"], _MR2["M"], _MR2["P1"], _MR2["CS"]
    racine = os.path.realpath(racine)
    for rel, sha in ATTENDUES.items():
        f = os.path.join(racine, rel)
        if not os.path.isfile(f):
            raise Refus(f"module MR-2 absent : {rel}")
        lu = K.sha256_fichier(f)
        if not K.compagnon_egal(f) or lu != sha:
            raise Refus(f"module importé à empreinte fausse : {rel} ({lu[:12]}…)")
    for d in ("outils-v4", "outils-v1"):
        p = os.path.join(racine, d)
        if p not in sys.path:
            sys.path.insert(0, p)
    import monde_riche_v4 as V4  # noqa: E402
    import complements_synthese_v1 as CS  # noqa: E402
    for mod in (V4, CS, V4.M):
        if not os.path.realpath(mod.__file__).startswith(racine + os.sep):
            raise Refus(f"module {mod.__name__} chargé hors de {racine}")
    _MR2.update(racine=racine, V4=V4, M=V4.M, P1=V4.P1, CS=CS)
    return V4, V4.M, V4.P1, CS


def verifier_imports(racine):
    """Chaque module importé depuis `racine` égale son compagnon ; les nommés, leur empreinte ; rend la liste (chemin, sha)."""
    racine = os.path.realpath(racine)
    out = []
    for _nom, mod in sorted(sys.modules.items()):
        f = getattr(mod, "__file__", None)
        if not f or not os.path.realpath(f).startswith(racine + os.sep):
            continue
        f = os.path.realpath(f)
        rel = os.path.relpath(f, racine)
        sha = K.sha256_fichier(f)
        if not K.compagnon_egal(f):
            raise Refus(f"module importé sans compagnon ou différent de son compagnon : {rel}")
        if rel in ATTENDUES and ATTENDUES[rel] != sha:
            raise Refus(f"module importé à empreinte fausse : {rel}")
        if [rel, sha] not in out:
            out.append([rel, sha])
    manquants = sorted(set(ATTENDUES) - {r for r, _ in out})
    if manquants:
        raise Refus(f"modules attendus non importés : {manquants}")
    return out


# --- entrées -------------------------------------------------------------------------------------------------------------------

def _entier(x):
    return isinstance(x, int) and not isinstance(x, bool)


def lire_mondes(mondes, M):
    if not isinstance(mondes, list) or len(mondes) != K.N_MONDES:
        raise Refus(f"mondes : exactement {K.N_MONDES}")
    out = {}
    for w in mondes:
        if not isinstance(w, dict) or set(w) != {"monde", "spec", "spec_sha256"} or not _entier(w["monde"]) \
                or w["monde"] not in K.MONDES or w["monde"] in out:
            raise Refus("monde : clés {monde, spec, spec_sha256}, numéros 1 à 20 une fois chacun")
        if hashlib.sha256(M.json_canonique(w["spec"])).hexdigest() != w["spec_sha256"]:
            raise Refus(f"monde {w['monde']} : empreinte du devis différente")
        out[w["monde"]] = w
    return out


def lire_certifiees(doc, mondes):
    """Étiquettes C8 « certifiée » rendues par `verifier_v4` à la génération (latente exclue), par monde."""
    if not isinstance(doc, dict) or doc.get("version") != "certifiees-crible-v-v1" or not isinstance(doc.get("mondes"), dict):
        raise Refus("CERTIFIEES.json : version « certifiees-crible-v-v1 » et objet « mondes » exigés")
    out = {}
    for r, w in mondes.items():
        c = doc["mondes"].get(str(r))
        ids = {e["id"] for e in w["spec"]["effets"]}
        lat = {e["id"] for e in w["spec"]["effets"] if e["classe"] == "latente"}
        if not isinstance(c, dict) or c.get("spec_sha256") != w["spec_sha256"] or not isinstance(c.get("certifiees"), list) \
                or not set(c["certifiees"]) <= ids or set(c["certifiees"]) & lat:
            raise Refus(f"CERTIFIEES.json, monde {r} : empreinte du devis, liste d'effets du monde, latente exclue")
        out[r] = sorted(c["certifiees"])
    return out


def lire_appels_et_cartes(donnees, mondes):
    if not isinstance(donnees, dict) or set(donnees) != {"cartes", "appels"}:
        raise Refus("CARTES.json : objet {cartes, appels}")
    etat = {}
    for a in donnees["appels"]:
        if not isinstance(a, dict) or set(a) != {"monde", "proposeur", "etat"} or a["monde"] not in mondes \
                or a["proposeur"] not in K.PROPOSEURS or a["etat"] not in ("complet", "tronque", "echec"):
            raise Refus("appel : clés {monde, proposeur, etat}, monde connu, proposeur parmi les quatre, état complet|tronque|echec")
        k = (a["monde"], a["proposeur"])
        if k in etat:
            raise Refus(f"appel en double : {k}")
        etat[k] = a["etat"]
    attendus = {(w, p) for w in mondes for p in K.PROPOSEURS}
    if set(etat) != attendus:
        raise Refus(f"appels attendus manquants : {sorted(attendus - set(etat))[:5]}")
    cartes, vus = [], set()
    for c in donnees["cartes"]:
        if not isinstance(c, dict) or set(c) != {"monde", "proposeur", "emplacement", "etat", "loi"} \
                or c["etat"] not in ("admise", "refusee") or not _entier(c["emplacement"]) or c["emplacement"] < 1:
            raise Refus("carte : clés {monde, proposeur, emplacement, etat, loi}, emplacement entier ≥ 1, état admise|refusee")
        k = (c["monde"], c["proposeur"])
        if k not in etat:
            raise Refus(f"carte d'un appel inconnu : {k}")
        if etat[k] == "echec":
            raise Refus(f"carte d'un appel en échec : {k}")
        if (k, c["emplacement"]) in vus:
            raise Refus(f"emplacement en double : {k}, {c['emplacement']}")
        vus.add((k, c["emplacement"]))
        if c["emplacement"] > K.CARTES_MAX and c["etat"] != "refusee":
            raise Refus(f"carte au-delà de la sixième admise : {k}, {c['emplacement']}")
        cartes.append(c)
    return etat, cartes


def lire_dollars(doc, mondes):
    """Dollars de chaque appel lancé ou non, tels que les journaux des relais les donnent (coût compté au prix de la
    configuration) ; un appel coupé à B_a sans ligne au journal porte le plafond de session (source « plafond_coupure »)."""
    if not isinstance(doc, dict) or doc.get("version") != "dollars-crible-v-v1" or not isinstance(doc.get("appels"), list):
        raise Refus("DOLLARS.json : version « dollars-crible-v-v1 » et liste « appels » exigées")
    out = {}
    for a in doc["appels"]:
        if not isinstance(a, dict) or set(a) != {"monde", "proposeur", "cout_config_usd", "source"} \
                or a["monde"] not in mondes or a["proposeur"] not in K.PROPOSEURS \
                or a["source"] not in ("journal_relais", "plafond_coupure", "non_lance") \
                or isinstance(a["cout_config_usd"], bool) or not isinstance(a["cout_config_usd"], (int, float)) \
                or not math.isfinite(a["cout_config_usd"]) or a["cout_config_usd"] < 0:
            raise Refus("DOLLARS.json : appel {monde, proposeur, cout_config_usd ≥ 0, source}")
        k = (a["monde"], a["proposeur"])
        if k in out:
            raise Refus(f"DOLLARS.json : appel en double {k}")
        if a["source"] == "non_lance" and a["cout_config_usd"] != 0:
            raise Refus(f"DOLLARS.json : appel non lancé {k} avec un coût")
        out[k] = (float(a["cout_config_usd"]), a["source"])
    if set(out) != {(w, p) for w in mondes for p in K.PROPOSEURS}:
        raise Refus("DOLLARS.json : les 80 appels exigés, lancés ou non")
    return out


def rapport_public_sur_configuration(conf_prix):
    """Prix publics / prix de la configuration, égal à l'entrée et à la sortie pour chaque proposeur (sinon il faudrait les jetons :
    refus) ; rend {proposeur : rapport}."""
    out = {}
    for n in K.PROPOSEURS:
        pe, ps = K.PRIX_PUBLICS[n]
        ce, cs = conf_prix[n]
        if not (ce > 0 and cs > 0) or abs(pe / ce - ps / cs) > 1e-12:
            raise Refus(f"{n} : rapport prix public / configuration différent à l'entrée et à la sortie")
        out[n] = pe / ce
    return out


# --- (1) copies et décision de la règle (sans issue, sans oracle) -----------------------------------------------------------------

class JeuPublic:
    """Jeu public d'instances d'un monde : traits et sous-populations seulement (aucune issue), tiré de `SeedSequence(entropy=
    racine, spawn_key=(r, 30))` ; la graine ne dépend que de l'indice r (jamais du contenu du monde ni du secret)."""
    __slots__ = ("r", "Z", "G", "nsp", "graine")

    def __init__(self, r, Z, G, nsp, graine):
        object.__setattr__(self, "r", r)
        object.__setattr__(self, "Z", Z)
        object.__setattr__(self, "G", G)
        object.__setattr__(self, "nsp", nsp)
        object.__setattr__(self, "graine", graine)

    def __setattr__(self, *_):
        raise Refus("jeu public : immuable")


def jeu_public(M, racine, r, D=8, nsp=3, n=K.JEU_PUBLIC_N):
    if isinstance(r, bool) or r not in K.MONDES:
        raise Refus("jeu public : la graine ne dépend que de l'indice r du monde")
    rng = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(r, 30)))
    Z, G = M.tirer_instances(rng, n, D, nsp)
    return JeuPublic(r, Z, G, nsp, [r, 30])


def empreinte_du_jeu(jeu):
    """Empreinte des traits et sous-populations du jeu public (contrôle : la graine ne dépend que de r)."""
    h = hashlib.sha256()
    h.update(np.ascontiguousarray(jeu.Z, dtype=np.float64).tobytes())
    h.update(np.ascontiguousarray(jeu.G, dtype=np.int64).tobytes())
    return h.hexdigest()


class LoiBonMarche:
    """Loi d'une carte valide de la moitié bon marché, seule chose que la règle voit d'une carte."""
    __slots__ = ("proposeur", "loi")

    def __init__(self, proposeur, loi):
        if proposeur not in K.MOITIE_B:
            raise Refus(f"la fonction de décision reçoit une carte de la moitié chère ({proposeur})")
        self.proposeur, self.loi = proposeur, loi


def exiger_entrees_de_la_regle(lois_b, k1, jeu):
    """Ligne d'arrêt « la fonction de décision reçoit autre chose que les lois de la moitié bon marché, K1 servie et le jeu
    public » : refus nommé (défaut)."""
    if not isinstance(lois_b, list) or not all(type(x) is LoiBonMarche for x in lois_b):
        raise Refus("fonction de décision : liste de lois de la moitié bon marché exigée (aucun autre objet)")
    for x in lois_b:
        if x.proposeur not in K.MOITIE_B:
            raise Refus(f"fonction de décision : carte de la moitié chère ({x.proposeur})")
        if not isinstance(x.loi, dict):
            raise Refus("fonction de décision : une loi de carte est un objet JSON")
    if not (isinstance(k1, dict) and k1.get("type") == "softmax" and set(k1) == {"type", "poids", "biais"}):
        raise Refus("fonction de décision : K1 servie (softmax {type, poids, biais}) exigée, rien d'autre (ni archive, ni oracle)")
    if type(jeu) is not JeuPublic:
        raise Refus("fonction de décision : jeu public exigé (aucun oracle, aucune issue)")


def distances(M, CS, loi, ref, jeu, cache=None, inverse=True):
    """(forme canonique égale, (d_nul, d_strat) dirigées loi → ref, (d_nul, d_strat) dirigées ref → loi) sur le jeu public ; le
    sens inverse (sensibilité « minimum des deux sens » seulement) n'est calculé que si `inverse`."""
    cle = (id(jeu), M.empreinte(M.forme_canonique(loi)), M.empreinte(M.forme_canonique(ref)), inverse)
    if cache is not None and cle in cache:
        return cache[cle]
    egal = M.empreinte(M.forme_canonique(loi)) == M.empreinte(M.forme_canonique(ref))
    if egal:
        r = (True, (0.0, 0.0), (0.0, 0.0))
    else:
        Px, Pr = M.probas(loi, jeu.Z, jeu.G), M.probas(ref, jeu.Z, jeu.G)
        msk = CS.strates(jeu.Z, jeu.G, jeu.nsp)
        r = (False, CS.distance_stratifiee(Px, Pr, msk),
             CS.distance_stratifiee(Pr, Px, msk) if inverse else (math.inf, math.inf))
    if cache is not None:
        cache[cle] = r
    return r


def est_copie(dist, sens="dirige", eps=K.EPS, eps_strat=K.EPS_STRAT):
    egal, d_dir, d_inv = dist
    if egal:
        return True
    if sens == "dirige":
        return d_dir[0] < eps and d_dir[1] < eps_strat
    if sens == "global":
        return d_dir[0] < eps
    if sens == "minimum":  # [V3] § 3.1 : la direction de plus petite distance globale, et sa lecture par strate
        d = d_dir if d_dir[0] <= d_inv[0] else d_inv
        return d[0] < eps and d[1] < eps_strat
    raise Refus(f"sens de la distance inconnu : {sens}")


def decider(M, CS, lois_b, k1, jeu, cache=None, seuil=K.SEUIL_Q):
    """**Fonction de production de la règle** : part q_w des copies (au sens dirigé carte → K1) parmi les cartes valides de la
    moitié bon marché, décision a_w = 1 si q_w > seuil (strictement). Ne reçoit que lois_b, K1 servie et le jeu public."""
    exiger_entrees_de_la_regle(lois_b, k1, jeu)
    n = len(lois_b)
    if n == 0:
        raise Refus("fonction de décision : aucune carte valide de la moitié bon marché (monde non complet : jamais appelée)")
    copies = sum(1 for x in lois_b if est_copie(distances(M, CS, x.loi, k1, jeu, cache), "dirige"))
    q = copies / n
    return {"n": n, "copies": copies, "q": q, "a": 1 if q > seuil else 0}


# --- (2) oracle et couvertures -------------------------------------------------------------------------------------------------

def preparer_monde(M, P1, w):
    """Oracle de 12 000 instances (`cle("oracle-crible-v", empreinte du devis)`), K1 du monde (`k1_du_monde`, l'effet principal
    le plus fort), informations des effets."""
    spec = w["spec"]
    loi = M.compiler_monde(spec)
    o = M.Oracle(loi, spec["dimension"], spec["sous_populations"], n=K.ORACLE_N, graine=P1.cle(K.ETIQUETTE_ORACLE, w["spec_sha256"]))
    k1, eid_k1, infos = M.k1_du_monde(spec, o)
    return {"spec": spec, "sha": w["spec_sha256"], "o": o, "k1": k1, "eid_k1": eid_k1, "infos": infos,
            "classe": {e["id"]: e["classe"] for e in spec["effets"]}}


def evaluable(M, loi, pm):
    try:
        P = M.probas(loi, pm["o"].Z[:64], pm["o"].G[:64])
    except (KeyError, ValueError, TypeError, IndexError, AttributeError, RecursionError):
        return False
    return bool(np.all(np.isfinite(P)) and P.shape == (64, 3) and np.allclose(P.sum(axis=1), 1.0))


def cartes_valides(etat, cartes, evaluable_fn):
    """Carte valide : admise au gardien, évaluable, emplacement ≤ 6, d'un appel complet ; les autres comptées à part (elles
    comptent dans les dollars, dans aucune couverture ni dans la règle)."""
    valides = {k: [] for k in etat}
    comptes = {"refusees": 0, "au_dela_de_six": 0, "non_evaluables": 0, "d_appels_tronques": 0}
    for c in cartes:
        k = (c["monde"], c["proposeur"])
        if c["emplacement"] > K.CARTES_MAX:
            comptes["au_dela_de_six"] += 1
            continue
        if c["etat"] != "admise":
            comptes["refusees"] += 1
            continue
        if etat[k] != "complet":
            comptes["d_appels_tronques"] += 1
            continue
        if not evaluable_fn(c["loi"], c["monde"]):
            comptes["non_evaluables"] += 1
            continue
        valides[k].append(c)
    return valides, comptes


def porte(pm, loi, cache):
    """(composantes portées à τ = max(0,005 ; 0,75·I), à τ' = max(0,005 ; 0,25·I)) par l'attribution de l'oracle."""
    cle = (pm["sha"], hashlib.sha256(json.dumps(loi, sort_keys=True, default=str).encode()).hexdigest())
    if cle not in cache:
        att = pm["o"].attribution(loi, pm["spec"])
        cache[cle] = ({i for i, d in att.items() if d >= max(K.TAU_PLANCHER, K.TAU_PART * pm["infos"][i])},
                      {i for i, d in att.items() if d >= max(K.TAU_PLANCHER, K.TAU_PART_LARGE * pm["infos"][i])})
    return cache[cle]


# --- (4) statistiques -------------------------------------------------------------------------------------------------------------

def placebo_exact(ell, db, de, k):
    """Énumération exacte des C(n_c, k) ensembles A de k mondes appelés : L_P(A) = Σ_{w∉A} ℓ_w, S_P(A) ; rend les listes et le
    compte (le contrôle « compte égal à C(n_c, k_R) » est fait par l'appelant)."""
    n = len(ell)
    if not (0 <= k <= n):
        raise Refus("placebo : taille hors de [0 ; n_c]")
    L = sum(ell)
    tout = sum(db) + sum(de)
    Ls, Ss, compte = [], [], 0
    for A in itertools.combinations(range(n), k):
        Ls.append(L - sum(ell[i] for i in A))
        Ss.append(1.0 - (sum(db) + sum(de[i] for i in A)) / tout if tout > 0 else 0.0)
        compte += 1
    return Ls, Ss, compte


def exiger_placebo(compte, n, k, taille):
    if taille != k:
        raise Refus(f"placebo : taille {taille} ≠ k_R {k}")
    if compte != math.comb(n, k):
        raise Refus(f"placebo : énumération incomplète ({compte} ensembles, C({n}, {k}) = {math.comb(n, k)} attendus)")


def resume_placebo(Ls, Ss, L_ref):
    a, s = np.array(Ls, float), np.array(Ss, float)
    return {"p_choix": float(np.mean(a <= L_ref)), "L_P_moyenne": float(a.mean()),
            "L_P_q05": float(np.quantile(a, 0.05)), "L_P_q95": float(np.quantile(a, 0.95)),
            "S_P_moyenne": float(s.mean()), "S_P_q05": float(np.quantile(s, 0.05)), "S_P_q95": float(np.quantile(s, 0.95))}


def epargne(db, de, a):
    tout = sum(db) + sum(de)
    return 1.0 - (sum(db) + sum(x * y for x, y in zip(a, de))) / tout if tout > 0 else 0.0


def indices_reechantillon(racine, n, B=K.REECHANTILLONS):
    """Rééchantillonnage des mondes : graine `SeedSequence(entropy=racine, spawn_key=(99, b))` par rééchantillon b (jamais tirée
    des données)."""
    out = np.empty((B, n), dtype=np.int64)
    for b in range(B):
        out[b] = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(99, b))).integers(0, n, n)
    return out


def ic_percentiles(valeurs):
    v = np.asarray(valeurs, float)
    return [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))]


def bras(mondes_c, q, ell, CT, CB, CE, db, de, seuil=K.SEUIL_Q, a=None):
    """Bras de la règle (ou d'une décision a donnée) sur les mondes complets `mondes_c`."""
    a = [1 if q[w] > seuil else 0 for w in mondes_c] if a is None else a
    n = len(mondes_c)
    W_R = sum(1 for i, w in enumerate(mondes_c) if a[i] == 0 and ell[w] >= 1)
    L_R = sum((1 - a[i]) * ell[w] for i, w in enumerate(mondes_c))
    return {"n_c": n, "k": sum(a), "S": epargne([db[w] for w in mondes_c], [de[w] for w in mondes_c], a), "W": W_R, "L": L_R,
            "a": a}


# --- mesure ----------------------------------------------------------------------------------------------------------------------

def mesurer(racine_mr2, texte_sha256, mondes_doc, certifiees_doc, cartes_doc, dollars_doc, conf_prix, sortie, sortie_fictive,
            imports_fn=None, B=K.REECHANTILLONS, ecrire_fn=None):
    """Rend (corps principal, corps fictif). La sortie principale est écrite et scellée par `ecrire_fn` **avant** le rejeu sous
    archive fictive, qui l'exige scellée."""
    V4, M, P1, CS = charger_mr2(racine_mr2)
    racine = K.racine_des_graines(texte_sha256)
    mondes = lire_mondes(mondes_doc, M)
    certif = lire_certifiees(certifiees_doc, mondes)
    etat, cartes = lire_appels_et_cartes(cartes_doc, mondes)
    dollars = lire_dollars(dollars_doc, mondes)
    rapport_pub = rapport_public_sur_configuration(conf_prix)
    pm_ = {r: preparer_monde(M, P1, w) for r, w in sorted(mondes.items())}
    cache_p, cache_d = {}, {}

    valides, comptes_cartes = cartes_valides(etat, cartes, lambda loi, w: evaluable(M, loi, pm_[w]))
    repondu = {k: etat[k] == "complet" and len(valides[k]) > 0 for k in etat}
    complet = {w: any(repondu[(w, p)] for p in K.MOITIE_B) and any(repondu[(w, p)] for p in K.MOITIE_E) for w in mondes}
    quatre = {w: all(repondu[(w, p)] for p in K.PROPOSEURS) for w in mondes}
    mondes_c = [w for w in sorted(mondes) if complet[w]]

    # (1) copies et décisions, sur les seuls mondes complets (la règle n'est jamais appelée sur un monde non complet)
    jeux = {w: jeu_public(M, racine, w) for w in mondes_c}
    decision, dist_b = {}, {}
    for w in mondes_c:
        lois_b = [LoiBonMarche(c["proposeur"], c["loi"]) for p in K.MOITIE_B for c in valides[(w, p)]]
        decision[w] = decider(M, CS, lois_b, pm_[w]["k1"], jeux[w], cache_d)
        dist_b[w] = [(c["proposeur"], distances(M, CS, c["loi"], pm_[w]["k1"], jeux[w], cache_d))
                     for p in K.MOITIE_B for c in valides[(w, p)]]
    q = {w: decision[w]["q"] for w in mondes_c}

    # (2) couvertures, hors l'effet de K1 et ce que K1 servie porte à elle seule
    def couverture(w, proposeurs, large=False, toutes=False):
        pm = pm_[w]
        porte_k1 = porte(pm, pm["k1"], cache_p)[1 if large else 0]
        excl = {pm["eid_k1"]} | porte_k1
        base = set(pm["classe"]) if toutes else set(certif[w])
        comptees = base - excl
        cov = set()
        for p in proposeurs:
            for c in valides[(w, p)]:
                cov |= porte(pm, c["loi"], cache_p)[1 if large else 0]
        return cov & comptees, comptees

    cov = {}
    for w in mondes:
        cov[w] = {nom: couverture(w, props)[0] for nom, props in (("T", K.PROPOSEURS), ("B", K.MOITIE_B), ("E", K.MOITIE_E))}
        cov[w]["comptees"] = couverture(w, K.PROPOSEURS)[1]
    CT = {w: len(cov[w]["T"]) for w in mondes}
    CB = {w: len(cov[w]["B"]) for w in mondes}
    CE = {w: len(cov[w]["E"]) for w in mondes}
    ell = {w: CT[w] - CB[w] for w in mondes}

    # (3) dollars : principal aux prix publics ; sensibilité au compte de la configuration
    def dol(w, props, publics=True):
        return sum(dollars[(w, p)][0] * (rapport_pub[p] if publics else 1.0) for p in props)
    db = {w: dol(w, K.MOITIE_B) for w in mondes}
    de = {w: dol(w, K.MOITIE_E) for w in mondes}
    db_c = {w: dol(w, K.MOITIE_B, False) for w in mondes}
    de_c = {w: dol(w, K.MOITIE_E, False) for w in mondes}

    # (4) bras
    n_c = len(mondes_c)
    R = bras(mondes_c, q, ell, CT, CB, CE, db, de)
    a_R = R["a"]
    k_R = R["k"]
    W_B = sum(1 for w in mondes_c if ell[w] >= 1)
    L_B = sum(ell[w] for w in mondes_c)
    S_B = epargne([db[w] for w in mondes_c], [de[w] for w in mondes_c], [0] * n_c)
    diff_EB = [CE[w] - CB[w] for w in mondes_c]

    # placebo exact de même fréquence que la règle
    principal = {}
    if n_c > 0:
        Ls, Ss, compte = placebo_exact([ell[w] for w in mondes_c], [db[w] for w in mondes_c], [de[w] for w in mondes_c], k_R)
        exiger_placebo(compte, n_c, k_R, k_R)
        placebo = dict(resume_placebo(Ls, Ss, R["L"]), ensembles=compte, taille=k_R)
        idx = indices_reechantillon(racine, n_c, B)
        ellv, aR = np.array([ell[w] for w in mondes_c], float), np.array(a_R, float)
        dbv, dev = np.array([db[w] for w in mondes_c]), np.array([de[w] for w in mondes_c])
        cebv = np.array(diff_EB, float)
        LRb = ((1 - aR)[idx] * ellv[idx]).sum(axis=1) / n_c
        LBb = ellv[idx].sum(axis=1) / n_c
        tout_b = dbv[idx].sum(axis=1) + dev[idx].sum(axis=1)
        with np.errstate(invalid="ignore", divide="ignore"):
            SRb = np.where(tout_b > 0, 1 - (dbv[idx].sum(axis=1) + (aR[idx] * dev[idx]).sum(axis=1)) / tout_b, 0.0)
            SBb = np.where(tout_b > 0, 1 - dbv[idx].sum(axis=1) / tout_b, 0.0)
        EBb = cebv[idx].mean(axis=1)
        principal = {
            "S_R": R["S"], "S_R_ic95": ic_percentiles(SRb), "W_R": R["W"], "W_R_sur_n_c_ic95": list(K.clopper_pearson(R["W"], n_c)),
            "L_R": R["L"], "L_R_sur_n_c": R["L"] / n_c, "L_R_sur_n_c_ic95": ic_percentiles(LRb), "k_R": k_R,
            "W_B": W_B, "W_B_sur_n_c_ic95": list(K.clopper_pearson(W_B, n_c)), "L_B": L_B, "L_B_sur_n_c": L_B / n_c,
            "L_B_sur_n_c_ic95": ic_percentiles(LBb), "S_B": S_B, "S_B_ic95": ic_percentiles(SBb),
            "C_E_moins_C_B_moyenne": float(np.mean(cebv)), "C_E_moins_C_B_ic95": ic_percentiles(EBb),
            "placebo": placebo, "reechantillons": B}
    else:
        placebo = None

    # sensibilités (sans verdict), sauf le rejeu sous archive fictive
    sens = {}
    if n_c > 0:
        rang = sorted(mondes_c, key=lambda w: (-q[w], pm_[w]["sha"]))[: n_c // 2]
        a_rang = [1 if w in rang else 0 for w in mondes_c]
        Rr = bras(mondes_c, q, ell, CT, CB, CE, db, de, a=a_rang)
        Ls2, Ss2, c2 = placebo_exact([ell[w] for w in mondes_c], [db[w] for w in mondes_c], [de[w] for w in mondes_c], Rr["k"])
        exiger_placebo(c2, n_c, Rr["k"], Rr["k"])
        sens["regle_au_rang"] = {k: Rr[k] for k in ("k", "S", "W", "L")} | {"placebo": resume_placebo(Ls2, Ss2, Rr["L"])}
        sens["courbe_du_seuil"] = {str(s): {k: v for k, v in bras(mondes_c, q, ell, CT, CB, CE, db, de, seuil=s).items() if k != "a"}
                                   for s in K.SEUILS_COURBE}
        for nom_s, sens_d in (("copie_distance_globale_seule", "global"), ("copie_minimum_des_deux_sens", "minimum")):
            qs = {w: sum(1 for _p, d in dist_b[w] if est_copie(d, sens_d)) / len(dist_b[w]) for w in mondes_c}
            sens[nom_s] = {k: v for k, v in bras(mondes_c, qs, ell, CT, CB, CE, db, de).items() if k != "a"}
        sens["prix_de_la_configuration"] = {"S_R": epargne([db_c[w] for w in mondes_c], [de_c[w] for w in mondes_c], a_R),
                                            "S_B": epargne([db_c[w] for w in mondes_c], [de_c[w] for w in mondes_c], [0] * n_c)}
        for nom_s, large, toutes in (("tau_0_25", True, False), ("toutes_les_composantes", False, True)):
            CT2 = {w: len(couverture(w, K.PROPOSEURS, large, toutes)[0]) for w in mondes_c}
            CB2 = {w: len(couverture(w, K.MOITIE_B, large, toutes)[0]) for w in mondes_c}
            ell2 = {w: CT2[w] - CB2[w] for w in mondes_c}
            R2 = bras(mondes_c, q, ell2, CT2, CB2, None, db, de)
            sens[nom_s] = {"W_R": R2["W"], "L_R": R2["L"], "W_B": sum(1 for w in mondes_c if ell2[w] >= 1),
                           "L_B": sum(ell2.values())}
        m4 = [w for w in mondes_c if quatre[w]]
        if m4:
            R4 = bras(m4, q, ell, CT, CB, CE, db, de)
            sens["mondes_a_quatre_appels"] = {"n": len(m4), "k_R": R4["k"], "S_R": R4["S"], "W_R": R4["W"], "L_R": R4["L"],
                                              "W_B": sum(1 for w in m4 if ell[w] >= 1), "L_B": sum(ell[w] for w in m4)}
        else:
            sens["mondes_a_quatre_appels"] = {"n": 0}
        sens["prix_public_pr1_apres_le_30_novembre"] = {
            "S_R": epargne([db[w] + dollars[(w, "argon")][0] * rapport_pub["argon"] for w in mondes_c],
                           [de[w] for w in mondes_c], a_R)}

    # rapportés : par proposeur, par classe (sommés sur les mondes), cartes
    par_proposeur = {}
    for p in K.PROPOSEURS:
        ks = [(w, p) for w in mondes]
        copies_p = [est_copie(d, "dirige") for w in mondes_c for pp, d in dist_b[w] if pp == p]
        par_proposeur[p] = {"complets": sum(etat[k] == "complet" for k in ks), "tronques": sum(etat[k] == "tronque" for k in ks),
                            "echecs": sum(etat[k] == "echec" for k in ks), "repondus": sum(repondu[k] for k in ks),
                            "cartes_valides": sum(len(valides[k]) for k in ks),
                            "part_des_copies": (sum(copies_p) / len(copies_p)) if copies_p else None,
                            "couverture_sommee": sum(len(couverture(w, (p,))[0]) for w in mondes),
                            "dollars_publics": sum(dollars[k][0] * rapport_pub[p] for k in ks),
                            "dollars_configuration": sum(dollars[k][0] for k in ks)}
    classes = ("forte", "moyenne", "faible", "conditionnelle", "latente")
    pertes_classe_B = {c: 0 for c in classes}
    pertes_classe_R = {c: 0 for c in classes}
    for i, w in enumerate(mondes_c):
        for comp in cov[w]["T"] - cov[w]["B"]:
            cl = pm_[w]["classe"][comp]
            pertes_classe_B[cl] += 1
            if a_R[i] == 0:
                pertes_classe_R[cl] += 1
    fournisseurs = {}
    for f, props in fournisseurs_de_la_configuration().items():
        fournisseurs[f] = {"proposeurs": list(props), "repondus": sum(repondu[(w, p)] for w in mondes for p in props)}
    audit = []
    for w in mondes_c:
        for comp in sorted(cov[w]["T"] - cov[w]["B"]):
            porteurs = [{"proposeur": c["proposeur"], "emplacement": c["emplacement"]} for p in K.MOITIE_E for c in valides[(w, p)]
                        if comp in porte(pm_[w], c["loi"], cache_p)[0]]
            audit.append({"monde": w, "composante": comp, "cartes_cheres": porteurs})
    corps = {
        "version": VERSION, "texte_sha256": texte_sha256, "mondes_sha256": sorted(pm["sha"] for pm in pm_.values()),
        "appels": {"complets": sum(v == "complet" for v in etat.values()), "tronques": sum(v == "tronque" for v in etat.values()),
                   "echecs": sum(v == "echec" for v in etat.values()), "repondus": sum(repondu.values())},
        "cartes": comptes_cartes, "n_c": n_c, "mondes_complets": mondes_c,
        "mondes_avec_C_T_positif": sum(1 for w in mondes_c if CT[w] >= 1),
        "fournisseurs": fournisseurs,
        "jeux_publics_sha256": {str(w): empreinte_du_jeu(jeux[w]) for w in mondes_c},
        "par_monde": {str(w): {"complet": complet[w], "quatre_appels": quatre[w], "q": q.get(w), "a": decision[w]["a"] if w in decision else None,
                               "n_b": decision[w]["n"] if w in decision else None, "C_T": CT[w], "C_B": CB[w], "C_E": CE[w],
                               "ell": ell[w], "dollars_b": db[w], "dollars_e": de[w]} for w in sorted(mondes)},
        "dollars_mondes_non_complets": {"publics": sum(db[w] + de[w] for w in mondes if not complet[w]),
                                        "configuration": sum(db_c[w] + de_c[w] for w in mondes if not complet[w])},
        "dollars_total": {"publics": sum(db[w] + de[w] for w in mondes), "configuration": sum(db_c[w] + de_c[w] for w in mondes)},
        "dollars_sources": {s: sum(1 for v in dollars.values() if v[1] == s) for s in ("journal_relais", "plafond_coupure", "non_lance")},
        "principal": principal, "sensibilites": sens, "par_proposeur": par_proposeur,
        "pertes_par_classe_sommees": {"moitie_chere_seule_B": pertes_classe_B, "regle_R": pertes_classe_R},
        "audit_R4": {"cartes_cheres_portant_seules": audit,
                     "graine_des_trois_cartes": "SeedSequence(entropy=empreinte de CARTES.json, spawn_key=(98, w))"},
        "rejeu_archive_fictive": "second fichier scellé, écrit après celui-ci",
    }
    sha_principal = ecrire_fn(sortie, corps) if ecrire_fn else None

    # (5) rejeu de la seule décision sous archive fictive, après l'écriture et le scellement de la sortie principale
    lois_b_w = {w: [LoiBonMarche(c["proposeur"], c["loi"]) for p in K.MOITIE_B for c in valides[(w, p)]] for w in mondes_c}
    archives = {w: archive_fictive(M, pm_[w]) for w in mondes_c}
    fictif = rejeu_archive_fictive(M, CS, sortie, lois_b_w, archives, jeux, {w: db[w] for w in mondes_c}, {w: de[w] for w in mondes_c},
                                   sha_principal)
    exiger_sortie_fictive(fictif)
    if ecrire_fn:
        ecrire_fn(sortie_fictive, fictif)
    return corps, fictif


def fournisseurs_de_la_configuration():
    """Voies de relais à clé commune (« Seuil ») : Pr-2 et Pr-4 (crédits de Claude), Pr-1, Pr-3."""
    return {"claude": ("fable52", "opus55"), "gemini": ("argon",), "astra": ("astra",)}


# --- (5) rejeu sous archive fictive : fonction distincte, jamais appelée par la production ------------------------------------------

CLES_FICTIVES = {"version", "k_R", "S_R", "archive", "seuil", "sortie_principale_sha256", "a_lire"}


def archive_fictive(M, pm):
    """K1 et les composantes fortes et moyennes du monde (lues par l'expérimentateur, jamais par la règle de production) : K1 ; pour
    chaque composante forte ou moyenne autre que l'effet de K1, le monde réduit à {effet de K1, cette composante} ; et le monde
    réduit à toutes ensemble."""
    spec = pm["spec"]
    fm = [e["id"] for e in spec["effets"] if e["classe"] in ("forte", "moyenne") and e["id"] != pm["eid_k1"]]
    lois = [pm["k1"]] + [M.monde_restreint(spec, [pm["eid_k1"], c]) for c in fm]
    if fm:
        lois.append(M.monde_restreint(spec, [pm["eid_k1"]] + fm))
    return lois


def rejeu_archive_fictive(M, CS, chemin_principal, lois_b_w, archives, jeux, db, de, sha_principal):
    """Rejeu de la seule décision a_w sous l'archive fictive (copie : forme canonique d'une loi de l'archive, ou distance dirigée
    au minimum sur les lois de l'archive sous ε et ε_strat) ; rend k_R et S_R, ni W ni L ; exige la sortie principale déjà écrite
    et scellée (son empreinte égale à son compagnon et à celle que la mesure a écrite)."""
    if sha_principal is None or not os.path.isfile(chemin_principal) or not K.compagnon_egal(chemin_principal) \
            or K.sha256_fichier(chemin_principal) != sha_principal:
        raise Refus("rejeu sous archive fictive exécuté avant l'écriture et le scellement de la sortie principale")
    mondes_c = sorted(lois_b_w)
    a, cache = [], {}
    for w in mondes_c:
        n = len(lois_b_w[w])
        c = 0
        for x in lois_b_w[w]:
            dd = [distances(M, CS, x.loi, ref, jeux[w], cache, inverse=False) for ref in archives[w]]
            if any(d[0] for d in dd):  # forme canonique d'une loi de l'archive
                c += 1
                continue
            plus_proche = min(dd, key=lambda d: d[1][0])  # minimum sur les lois de l'archive de la distance dirigée
            if plus_proche[1][0] < K.EPS and plus_proche[1][1] < K.EPS_STRAT:
                c += 1
        a.append(1 if n and c / n > K.SEUIL_Q else 0)
    return {"version": VERSION, "k_R": sum(a), "S_R": epargne([db[w] for w in mondes_c], [de[w] for w in mondes_c], a),
            "archive": "K1 ; K1 et chaque composante forte ou moyenne ; K1 et toutes ensemble (monde réduit)",
            "seuil": K.SEUIL_Q, "sortie_principale_sha256": sha_principal,
            "a_lire": "contrefactuel invalide pour les proposeurs, qui n'ont pas vu cette archive ; couverture non lue"}


def exiger_sortie_fictive(fictif):
    if not isinstance(fictif, dict) or set(fictif) != CLES_FICTIVES:
        raise Refus(f"rejeu sous archive fictive : il rend autre chose que k_R et S_R ({sorted(set(fictif) - CLES_FICTIVES)})")


# --- écriture, chronométrage, principal -------------------------------------------------------------------------------------------

def ecrire_sortie(chemin, corps, commande, debut, imports):
    """Corps empreinté, heures et chemins hors du corps ; mode `x` ; compagnon `.sha256` ; rend l'empreinte du fichier."""
    texte = json.dumps(corps, ensure_ascii=False, sort_keys=True, default=str)
    objet = {"corps": corps, "corps_sha256": hashlib.sha256(texte.encode("utf-8")).hexdigest(),
             "hors_corps": {"commande": commande, "debut_utc": debut,
                            "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                            "script_sha256": K.sha256_fichier(os.path.abspath(__file__)),
                            "commun_sha256": K.sha256_fichier(K.__file__), "modules_importes": imports}}
    return K.ecrire_scelle_json(chemin, objet)


def chrono(sortie):
    """Durée de l'énumération exacte du placebo, pire cas (n_c = 20, k_R = 10 : 184 756 ensembles), mondes simulés par une
    formule fixe (seul le temps compte) ; deux lancements, le plus long retenu."""
    ell = [w % 3 for w in range(20)]
    db = [0.4 + 0.01 * w for w in range(20)]
    de = [2.9 - 0.01 * w for w in range(20)]
    out = []
    for _ in range(2):
        t = time.perf_counter()
        Ls, Ss, c = placebo_exact(ell, db, de, 10)
        exiger_placebo(c, 20, 10, 10)
        r = resume_placebo(Ls, Ss, sum(ell) - 10)
        out.append({"secondes": round(time.perf_counter() - t, 3), "ensembles": c, "p_choix": r["p_choix"]})
    corps = {"version": VERSION, "lancements": out, "retenu_s": max(x["secondes"] for x in out)}
    K.ecrire_scelle_json(sortie, corps)
    return corps


def conf_prix_v12(chemin_configuration):
    with open(chemin_configuration, encoding="utf-8") as f:
        c = json.load(f)
    return {n: (float(c["proposeurs"][n]["prix_entree_usd_par_million"]), float(c["proposeurs"][n]["prix_sortie_usd_par_million"]))
            for n in K.PROPOSEURS}


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    s = a.add_subparsers(dest="commande", required=True)
    x = s.add_parser("mesurer")
    for o in ("--mr2", "--texte-sha256", "--mondes", "--certifiees", "--cartes", "--dollars", "--configuration", "--sortie",
              "--sortie-fictive"):
        x.add_argument(o, required=True)
    x = s.add_parser("chrono")
    x.add_argument("--mr2", required=True)
    x.add_argument("sortie")
    args = a.parse_args(argv)
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    try:
        if args.commande == "chrono":
            if os.path.exists(args.sortie):
                raise Refus("sortie existante")
            print(json.dumps(chrono(args.sortie), ensure_ascii=False))
            return 0
        for f in (args.sortie, args.sortie_fictive):
            if os.path.exists(f):
                raise Refus(f"sortie existante ({os.path.basename(f)}) : une seule mesure")
        lus = {}
        for nom in ("mondes", "certifiees", "cartes", "dollars"):
            with open(getattr(args, nom), encoding="utf-8") as f:
                lus[nom] = json.load(f)
        charger_mr2(args.mr2)
        imports = verifier_imports(args.mr2)

        def ecrire(chemin, corps):
            return ecrire_sortie(chemin, corps, "mesurer", debut, imports)
        corps, fictif = mesurer(args.mr2, args.texte_sha256, lus["mondes"], lus["certifiees"], lus["cartes"], lus["dollars"],
                                conf_prix_v12(args.configuration), args.sortie, args.sortie_fictive, ecrire_fn=ecrire)
    except Refus as e:
        print(f"refus : {e}", file=sys.stderr)
        return 2
    print(json.dumps({"version": VERSION, "sortie_sha256": K.sha256_fichier(args.sortie),
                      "sortie_fictive_sha256": K.sha256_fichier(args.sortie_fictive)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
