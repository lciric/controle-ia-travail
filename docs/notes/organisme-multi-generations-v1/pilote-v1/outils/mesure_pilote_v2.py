"""Mesure, règle et taux d'erreur du pilote d'une génération — v2 (brouillon 2 du préenregistrement ; remplace
`mesure_pilote_v1.py`, `0d806aca…`, gardé, R12). Mots de Lazar R-2504 et R-2506 ; corrections E-1 à E-11 de la contre-lecture
`contre-lecture-pilote-v2.md` (`823b6e9e…`). Programme pur : mêmes entrées → même corps de sortie ; aucun appel ; lit les mondes
privés ; n'écrit aucun coefficient.

Usages :
  python3 -I -B mesure_pilote_v2.py taux SORTIE.json                       taux d'erreur de la décision (E-1, R-2506)
  python3 -I -B mesure_pilote_v2.py graine SORTIE.json                     fonction de graine essayée sur un secret public (E-10)
  python3 -I -B mesure_pilote_v2.py essai SORTIE.json                      essais R5 : P-0, P-1, P-2, minimum, artefacts (E-7)
  python3 -I -B mesure_pilote_v2.py mesurer MONDES.json CARTES.json SORTIE.json

Dessin (R-2506) : **4 mondes MR-2, bras A seul** (archive {K1}), 4 proposeurs, **16 appels attendus**, un par proposeur et par
monde. La probabilité d'une conditionnelle une fois sa condition connue n'est **pas mesurée** : 0,25 supposée (conception v4).

Définitions (gelées ici) :
- **appel** : état exporté `complet` (réponse brute entière, raison d'arrêt normale), `tronque` (raison d'arrêt = borne de
  sortie) ou `echec` (session en échec). **Répondu** = `complet` **et** au moins une carte admise au gardien et évaluable ;
  un appel `complet` sans telle carte est « sans carte ». Tronqué, échec, sans carte : **hors du dénominateur**, comptés à part
  (E-2 (i)). Les 16 couples (monde, proposeur) doivent tous figurer, une fois chacun (E-2 (iv)).
- **unité** : la **première conditionnelle** de chaque monde (celle dont la condition n'est pas une conditionnelle) ; une
  unité par appel ; la seconde d'une chaîne est rapportée à part (E-3).
- **porte** : attribution Δ_i ≥ τ_i = max(0,005 ; 0,75 · I_i) (oracle de 12 000 instances) ; sensibilité τ'_i = max(0,005 ;
  0,25 · I_i). Carte refusée au gardien, au-delà de la sixième, ou admise mais non évaluable : ne porte pas ; les non évaluables
  sont une **réserve** listée (E-6).
- **p_c** = 1 − (1 − x/n)^(1/6), x appels répondus qui trouvent, n appels répondus ; intervalle Clopper-Pearson 95 % sur x/n,
  transformé ; comparaison à p_max **avant arrondi** (S-4).
- **minimum** (E-2 (ii)) : n ≥ 12 sur 16 et au moins 3 appels répondus dans chaque monde ; sinon **P-0**.
- **règle** (R-2506 (a)) : P-0 si le minimum manque ; **P-1** si la borne basse de p_c > p_max = 0,051 (nœud de Lazar) ;
  sinon **P-2** : le banc de 24 mondes reçoit **p_c ponctuel** (P_CACHÉE) et 0,25 (P_VUE, supposée).
- **réserves qui font nœud avant le banc** (P-2 seulement) : E-4, la classe de décision (« favorable » si P(règle de garde tenue
  au banc | p) ≥ 0,5 sous le modèle de `seuil_pilote_v1.py`) diffère entre p_c commun et p_prod (survie par produit des q̂ par
  proposeur) ; E-8, le compte x diffère entre τ et τ', ou la classe diffère entre l'unité appel et l'unité carte. Le banc tourne
  alors aux valeurs en désaccord, et Lazar décide.
- **audit R4** (E-11 (ii)) : déclenché si x = 0 (« trop propre pour l'hypothèse ») ou si x ≥ 3 (classe défavorable ou à la
  bascule) ; il relit toutes les cartes refusées ou non évaluables.
"""
import datetime
import glob
import hashlib
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_NOTES = os.path.dirname(os.path.dirname(ICI))
OUTILS_V4 = os.path.join(RACINE_NOTES, "outils-v4")
for p in (OUTILS_V4, ICI):
    if p not in sys.path:
        sys.path.insert(0, p)
import monde_riche_v4 as V4  # noqa: E402
import seuil_pilote_v1 as S  # noqa: E402

M, P1 = V4.M, V4.P1
VERSION = "mesure-pilote-v2"
P_MAX = 0.051
ALPHA_IC = 0.05
EMPLACEMENTS = 6
MONDES_ATTENDUS = 4
PROPOSEURS = ("fable52", "opus55", "argon", "astra")
MIN_REPONDUS, MIN_PAR_MONDE = 12, 3
P_VUE_SUPPOSEE = 0.25
ATTENDUES = {  # E-7 (ii) : empreintes des deux modules nommés, en plus du contrôle de chaque compagnon
    os.path.join(OUTILS_V4, "monde_riche_v4.py"): "4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8",
    os.path.join(ICI, "seuil_pilote_v1.py"): "14eecfccdd83274d32388fcf2771bc608f0ad83bd8a3e5ac1161322d775e46ab"}


class Refus(Exception):
    pass


def _sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def verifier_imports():
    """Chaque module importé depuis le dossier des notes doit égaler son compagnon `.sha256` ; les deux modules nommés, en plus,
    leur empreinte écrite ici. Rend la liste (chemin relatif, empreinte)."""
    out = []
    for nom, mod in sorted(sys.modules.items()):
        f = getattr(mod, "__file__", None)
        if not f or not os.path.abspath(f).startswith(RACINE_NOTES + os.sep):
            continue
        f = os.path.abspath(f)
        sha = _sha(f)
        comp = f + ".sha256"
        if not os.path.isfile(comp):
            raise Refus(f"module importé sans compagnon : {os.path.relpath(f, RACINE_NOTES)}")
        with open(comp, encoding="utf-8") as c:
            attendu = c.read().split()[0]
        if sha != attendu:
            raise Refus(f"module importé différent de son compagnon : {os.path.relpath(f, RACINE_NOTES)}")
        if f in ATTENDUES and ATTENDUES[f] != sha:
            raise Refus(f"module {os.path.relpath(f, RACINE_NOTES)} : empreinte ≠ celle écrite dans le programme")
        out.append([os.path.relpath(f, RACINE_NOTES), sha])
    manquants = [k for k in ATTENDUES if k not in {os.path.join(RACINE_NOTES, r) for r, _ in out}]
    if manquants:
        raise Refus(f"modules attendus non importés : {manquants}")
    return out


# --- intervalles et décision ---------------------------------------------------------------------------------------------

def _cdf(k, n, p):
    if p <= 0:
        return 1.0
    if p >= 1:
        return 0.0 if k < n else 1.0
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(0, k + 1))


def clopper_pearson(x, n, a=ALPHA_IC):
    if n == 0:
        return (0.0, 1.0)

    def biss(f):
        lo, hi = 0.0, 1.0
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if f(mid) else (lo, mid)
        return 0.5 * (lo + hi)
    bas = 0.0 if x == 0 else biss(lambda p: 1 - _cdf(x - 1, n, p) < a / 2)
    haut = 1.0 if x == n else biss(lambda p: _cdf(x, n, p) > a / 2)
    return (bas, haut)


def q_vers_p(q):
    return 1 - (1 - q) ** (1 / EMPLACEMENTS)


def verifier_p_max():
    grille = [round(0.0005 * i, 4) for i in range(0, 601)]
    p = next(x for x in grille if S.p_tenue(x) <= 0.05)
    if abs(p - P_MAX) > 1e-12:
        raise Refus(f"p_max recalculé {p} ≠ {P_MAX}")
    return p


def classe(p):
    """Classe de décision au banc : « favorable » si la règle de garde d'un banc de 24 mondes tient avec probabilité ≥ 0,5
    sous le modèle approché de `seuil_pilote_v1.py` (approximation, dite ; le banc lui-même décide)."""
    return "favorable" if S.p_tenue(p) >= 0.5 else "defavorable"


def issue_de(x, n):
    lo, hi = clopper_pearson(x, n)
    p = q_vers_p(x / n)
    if q_vers_p(lo) > P_MAX:
        return "P-1", p, (q_vers_p(lo), q_vers_p(hi))
    return "P-2", p, (q_vers_p(lo), q_vers_p(hi))


def taux():
    """Taux d'erreur de la décision, écrits d'avance (R-2506) : pour une probabilité vraie p par carte, appels indépendants,
    n appels répondus : P(P-1) ; P(classe favorable sous P-2) ; P(course permise) = Σ_x P(x) · [P-2] · P(règle tenue au banc |
    p_c ponctuel(x)) (modèle approché) ; P(course refusée) = 1 − P(course permise)."""
    verifier_p_max()
    grille = (0.0, 0.005, 0.01, 0.02, 0.03, 0.034, 0.04, 0.051, 0.075, 0.10, 0.15, 0.25)
    out = {}
    for n in (16, 14, 12):
        table_x = []
        for x in range(n + 1):
            iss, p, (lo, hi) = issue_de(x, n)
            table_x.append({"x": x, "p_c": round(p, 4), "ic95": [round(lo, 4), round(hi, 4)], "issue": iss,
                            "regle_tenue_au_banc": round(S.p_tenue(p), 4) if iss == "P-2" else None,
                            "classe": classe(p) if iss == "P-2" else "P-1"})
        lignes = {}
        for pv in grille:
            q = 1 - (1 - pv) ** EMPLACEMENTS
            px = [math.comb(n, x) * q ** x * (1 - q) ** (n - x) for x in range(n + 1)]
            p1 = sum(px[x] for x in range(n + 1) if table_x[x]["issue"] == "P-1")
            fav = sum(px[x] for x in range(n + 1) if table_x[x]["classe"] == "favorable")
            permise = sum(px[x] * S.p_tenue(table_x[x]["p_c"]) for x in range(n + 1) if table_x[x]["issue"] == "P-2")
            lignes[f"{pv}"] = {"P-1": round(p1, 4), "classe_favorable": round(fav, 4), "course_permise": round(permise, 4),
                               "course_refusee": round(1 - permise, 4),
                               "regle_tenue_si_p_connu": round(S.p_tenue(pv), 4)}
        out[f"n={n}"] = {"par_x": table_x, "par_p_vrai": lignes,
                         "x_max_favorable": max(r["x"] for r in table_x if r["classe"] == "favorable"),
                         "x_min_P1": min((r["x"] for r in table_x if r["issue"] == "P-1"), default=None)}
    grille_fine = [round(0.0005 * i, 4) for i in range(0, 601)]
    bascule = next(p for p in grille_fine if S.p_tenue(p) < 0.5)
    return {"p_max": P_MAX, "bascule_0_5": bascule, "taux": out,
            "lecture": ("« course permise » : P-2 puis règle de garde tenue au banc (modèle approché de seuil_pilote_v1.py) ; "
                        "erreur d'acceptation : course permise alors que p vrai > p_max ; erreur de refus : course refusée "
                        "alors que p vrai ≤ 0,02 (l'hypothèse de la conception v4)")}


# --- graine des mondes du pilote (E-10 (i)) -------------------------------------------------------------------------------

ETIQUETTE = b"pilote-conditionnelles-v1"


def graine_monde_pilote(secret, phrase, empreinte_texte_hex, r):
    """Graine du monde r ∈ {1, 2, 3, 4} : 2⁶⁴ + entier des 8 premiers octets (gros-boutiste) de
    sha256(ETIQUETTE ∥ 0x00 ∥ secret (32 octets) ∥ 0x00 ∥ phrase en UTF-8 (sans octet nul) ∥ 0x00 ∥ empreinte du texte scellé
    (32 octets) ∥ 0x00 ∥ r (1 octet)). Les 8 tirages d'un monde sont ceux de `generer_v4` (sous-graines
    `SeedSequence(graine, spawn_key=(k,))`, k = 0 à 7, code scellé `4b165847…`) : aucun autre compteur."""
    if not (isinstance(secret, bytes) and len(secret) == 32):
        raise Refus("secret : 32 octets")
    b = phrase.encode("utf-8")
    if b"\x00" in b or not b:
        raise Refus("phrase : non vide, sans octet nul")
    e = bytes.fromhex(empreinte_texte_hex)
    if len(e) != 32:
        raise Refus("empreinte du texte : 32 octets")
    if r not in (1, 2, 3, 4):
        raise Refus("r ∈ {1, 2, 3, 4}")
    h = hashlib.sha256(ETIQUETTE + b"\x00" + secret + b"\x00" + b + b"\x00" + e + b"\x00" + bytes([r])).digest()
    return 2 ** 64 + int.from_bytes(h[:8], "big")


def essai_graine():
    s0, ph, emp = bytes(32), "développement public, jamais pour un vrai monde", "00" * 32
    g = {r: graine_monde_pilote(s0, ph, emp, r) for r in (1, 2, 3, 4)}
    rejoue = {r: graine_monde_pilote(s0, ph, emp, r) for r in (1, 2, 3, 4)}
    autre = graine_monde_pilote(bytes([1]) + bytes(31), ph, emp, 1)
    refus = {}
    for nom, args in {"secret_court": (bytes(31), ph, emp, 1), "phrase_nul": (s0, "a\x00b", emp, 1),
                      "phrase_vide": (s0, "", emp, 1), "r_hors": (s0, ph, emp, 5), "empreinte_courte": (s0, ph, "00", 1)}.items():
        try:
            graine_monde_pilote(*args)
            refus[nom] = "NON REFUSÉ (défaut)"
        except (Refus, ValueError) as x:
            refus[nom] = f"refusé : {x}"
    sous = [int(np.random.SeedSequence(g[1], spawn_key=(k,)).generate_state(1, dtype=np.uint64)[0]) for k in range(8)]
    return {"graines": {str(r): str(v) for r, v in g.items()}, "rejeu_egal": g == rejoue,
            "toutes_au_dessus_de_2_64": all(v >= 2 ** 64 for v in g.values()), "distinctes": len(set(g.values())) == 4,
            "secret_change_la_graine": autre != g[1], "refus": refus,
            "sous_graines_des_8_tirages_monde_1": [str(x) for x in sous], "sous_graines_distinctes": len(set(sous)) == 8,
            "conforme": g == rejoue and len(set(g.values())) == 4 and autre != g[1]
            and all(v.startswith("refusé") for v in refus.values()) and len(set(sous)) == 8}


# --- mesure ------------------------------------------------------------------------------------------------------------

_CACHE = {}


def _evaluable(loi, Z, G):
    try:
        P = M.probas(loi, Z, G)
    except (KeyError, ValueError, TypeError, IndexError):
        return False
    return bool(np.all(np.isfinite(P)) and P.shape == (len(Z), 3) and np.allclose(P.sum(axis=1), 1.0))


def _entier(x):
    return isinstance(x, int) and not isinstance(x, bool)


def preparer_mondes(mondes):
    if not isinstance(mondes, list) or len(mondes) != MONDES_ATTENDUS:
        raise Refus(f"mondes : exactement {MONDES_ATTENDUS}")
    out = {}
    for w in mondes:
        if not isinstance(w, dict) or set(w) != {"monde", "spec", "spec_sha256"} or not _entier(w["monde"]):
            raise Refus("monde : clés {monde, spec, spec_sha256}, monde entier")
        sha = hashlib.sha256(M.json_canonique(w["spec"])).hexdigest()
        if sha != w["spec_sha256"]:
            raise Refus(f"monde {w['monde']} : empreinte du devis différente")
        if w["monde"] in out:
            raise Refus("monde en double")
        spec = w["spec"]
        cle = ("monde", sha)
        if cle not in _CACHE:
            loi = M.compiler_monde(spec)
            o = M.Oracle(loi, spec["dimension"], spec["sous_populations"], n=12000, graine=P1.cle("oracle-pilote", sha))
            _, eid_k1, infos = M.k1_du_monde(spec, o)
            _CACHE[cle] = (o, eid_k1, infos)
        o, eid_k1, infos = _CACHE[cle]
        cond = {e["id"]: e["composante_condition"] for e in spec["effets"] if e["type"] == "interaction_xor"}
        if not cond:
            raise Refus(f"monde {w['monde']} : aucune conditionnelle")
        if eid_k1 in cond.values():
            raise Refus(f"monde {w['monde']} : la condition d'une conditionnelle est l'effet de K1")
        premiere = sorted(c for c, b in cond.items() if b not in cond)
        if len(premiere) != 1:
            raise Refus(f"monde {w['monde']} : première conditionnelle non unique")
        out[w["monde"]] = {"spec": spec, "sha": sha, "o": o, "infos": infos, "eid_k1": eid_k1, "premiere": premiere[0],
                           "secondes": sorted(c for c in cond if c != premiere[0]),
                           "classe": {e["id"]: e["classe"] for e in spec["effets"]}}
    return out


def _porte(pm, loi):
    cle = ("carte", pm["sha"], hashlib.sha256(M.json_canonique(loi)).hexdigest())
    if cle not in _CACHE:
        if not _evaluable(loi, pm["o"].Z[:64], pm["o"].G[:64]):
            _CACHE[cle] = None
        else:
            att = pm["o"].attribution(loi, pm["spec"])
            _CACHE[cle] = ({i for i, d in att.items() if d >= max(0.005, 0.75 * pm["infos"][i])},
                           {i for i, d in att.items() if d >= max(0.005, 0.25 * pm["infos"][i])})
    return _CACHE[cle]


def mesurer(mondes, cartes, appels):
    verifier_p_max()
    pm_ = preparer_mondes(mondes)
    if not isinstance(appels, list) or not isinstance(cartes, list):
        raise Refus("appels et cartes : listes")
    etat_appel = {}
    for a in appels:
        if not isinstance(a, dict) or set(a) != {"monde", "proposeur", "etat"} or a["monde"] not in pm_ \
                or a["proposeur"] not in PROPOSEURS or a["etat"] not in ("complet", "tronque", "echec"):
            raise Refus("appel : clés {monde, proposeur, etat}, monde connu, proposeur parmi les quatre, état complet|tronque|echec")
        k = (a["monde"], a["proposeur"])
        if k in etat_appel:
            raise Refus(f"appel en double : {k}")
        etat_appel[k] = a["etat"]
    attendus = {(w, p) for w in pm_ for p in PROPOSEURS}
    if set(etat_appel) != attendus:
        raise Refus(f"appels attendus manquants : {sorted(attendus - set(etat_appel))}")
    vus, par_appel = set(), {k: [] for k in attendus}
    au_dela, refusees, ignorees_tronque = 0, 0, 0
    for c in cartes:
        if not isinstance(c, dict) or set(c) != {"monde", "proposeur", "emplacement", "etat", "loi"} \
                or c["etat"] not in ("admise", "refusee") or not _entier(c["emplacement"]) or c["emplacement"] < 1:
            raise Refus("carte : clés {monde, proposeur, emplacement, etat, loi}, emplacement entier ≥ 1, état admise|refusee")
        k = (c["monde"], c["proposeur"])
        if k not in etat_appel:
            raise Refus(f"carte d'un appel inconnu : {k}")
        if etat_appel[k] == "echec":
            raise Refus(f"carte d'un appel en échec : {k}")
        if (k, c["emplacement"]) in vus:
            raise Refus(f"emplacement en double : {k}, {c['emplacement']}")
        vus.add((k, c["emplacement"]))
        if c["emplacement"] > EMPLACEMENTS:
            if c["etat"] != "refusee":
                raise Refus(f"carte au-delà de la sixième admise : {k}, {c['emplacement']}")
            au_dela += 1
            continue
        refusees += c["etat"] == "refusee"
        if etat_appel[k] == "tronque":
            ignorees_tronque += 1
            continue
        par_appel[k].append(c)
    # statut de chaque appel et portée
    statut, trouve, trouve_large, cartes_portent, non_evaluables, secondes = {}, {}, {}, {}, [], {}
    for k in sorted(attendus):
        w, prop = k
        pm = pm_[w]
        if etat_appel[k] != "complet":
            statut[k] = etat_appel[k]
            continue
        portes = []
        for c in par_appel[k]:
            if c["etat"] != "admise":
                continue
            r = _porte(pm, c["loi"])
            if r is None:
                non_evaluables.append({"monde": w, "proposeur": prop, "emplacement": c["emplacement"]})
                continue
            portes.append(r)
        if not portes:
            statut[k] = "sans_carte"
            continue
        statut[k] = "repondu"
        trouve[k] = any(pm["premiere"] in a for a, _ in portes)
        trouve_large[k] = any(pm["premiere"] in b for _, b in portes)
        cartes_portent[k] = sum(1 for a, _ in portes if pm["premiere"] in a)
        secondes[k] = {s: any(s in a for a, _ in portes) for s in pm["secondes"]}
    rep = sorted(k for k, s in statut.items() if s == "repondu")
    n, x, x_large = len(rep), sum(trouve[k] for k in rep), sum(trouve_large[k] for k in rep)
    par_monde = {w: sum(1 for k in rep if k[0] == w) for w in pm_}
    comptes = {s: sum(1 for v in statut.values() if v == s) for s in ("repondu", "sans_carte", "tronque", "echec")}
    corps = {"version": VERSION, "mondes_sha256": sorted(pm["sha"] for pm in pm_.values()), "appels": comptes,
             "repondus_par_monde": {str(w): v for w, v in sorted(par_monde.items())},
             "cartes": {"refusees_au_gardien": refusees, "au_dela_de_six": au_dela, "ignorees_appel_tronque": ignorees_tronque,
                        "non_evaluables": non_evaluables},
             "p_max": P_MAX, "p_vue_supposee": P_VUE_SUPPOSEE}
    if n < MIN_REPONDUS or min(par_monde.values()) < MIN_PAR_MONDE:
        corps["regle"] = {"issue": "P-0", "texte": (f"non concluant : {n} appels répondus (minimum {MIN_REPONDUS}) ; "
                                                    f"minimum par monde {min(par_monde.values())} (exigé {MIN_PAR_MONDE}) ; nœud de Lazar")}
        return corps
    iss, p, (lo, hi) = issue_de(x, n)
    emp = n * EMPLACEMENTS
    xc = sum(cartes_portent[k] for k in rep)
    lo_c, hi_c = clopper_pearson(xc, emp)
    p_carte = xc / emp
    # par proposeur (E-4) : survie d'une génération = Π (1 − q̂_j) ; p_prod équivalent par carte
    qj = {}
    for prop in PROPOSEURS:
        ks = [k for k in rep if k[1] == prop]
        if ks:
            qj[prop] = {"appels": len(ks), "trouvent": sum(trouve[k] for k in ks), "q": sum(trouve[k] for k in ks) / len(ks)}
    survie_prod = math.prod(1 - v["q"] for v in qj.values()) ** (4 / len(qj))  # ramenée à 4 proposeurs si un manque
    p_prod = 1 - survie_prod ** (1 / (4 * EMPLACEMENTS))
    corps.update({
        "principale": {"n": n, "x": x, "p_c": round(p, 4), "ic95": [round(lo, 4), round(hi, 4)],
                       "borne_basse_non_arrondie": lo, "classe": classe(p) if iss == "P-2" else "P-1",
                       "regle_tenue_au_banc_modele": round(S.p_tenue(p), 4)},
        "sensibilites": {"tau_0_25": {"x": x_large, "p_c": round(q_vers_p(x_large / n), 4)},
                         "unite_carte": {"emplacements": emp, "qui_portent": xc, "p": round(p_carte, 4),
                                         "ic95": [round(lo_c, 4), round(hi_c, 4)], "classe": classe(p_carte)}},
        "par_proposeur": {k: {"appels": v["appels"], "trouvent": v["trouvent"]} for k, v in qj.items()},
        "survie_par_produit": {"survie_une_generation": round(survie_prod, 4), "p_prod": round(p_prod, 4),
                               "classe": classe(p_prod), "survie_valeur_commune": round((1 - x / n) ** 4, 4)},
        "secondes_de_chaine": {"appels": sum(len(v) for v in secondes.values()),
                               "trouvent": sum(sum(v.values()) for v in secondes.values())},
        "audit_R4": ("déclenché : x = 0" if x == 0 else "déclenché : x ≥ 3" if x >= 3 else "non déclenché")})
    if iss == "P-1":
        corps["regle"] = {"issue": "P-1", "texte": "MR-2 ne sert pas telle quelle : borne basse de p_c > p_max ; nœud de Lazar"}
        return corps
    noeuds = []
    if classe(p) != classe(p_prod):
        noeuds.append("E-4 : classe différente entre p_c commun et p_prod par proposeur")
    if x_large != x:
        noeuds.append("E-8 : compte différent entre τ = 0,75 · I et τ' = 0,25 · I")
    if classe(p) != classe(p_carte):
        noeuds.append("E-8 : classe différente entre l'unité appel et l'unité carte")
    corps["regle"] = {"issue": "P-2", "P_CACHEE_banc": round(p, 6), "P_VUE_banc": P_VUE_SUPPOSEE,
                      "P_VUE_source": "supposée (0,25 de la conception v4 ; non mesurée, R-2506)",
                      "noeuds_avant_banc": noeuds,
                      "texte": ("banc de 24 mondes avec p_c ponctuel" if not noeuds else
                                "réserve : nœud de Lazar avant le banc ; le banc tourne aux valeurs en désaccord")}
    return corps


# --- essais R5 (E-7 (i)) -----------------------------------------------------------------------------------------------

def essai():
    rng = P1.rng_de("pilote-v2-essai-cartes")
    mondes, specs = [], {}
    for r in range(1, MONDES_ATTENDUS + 1):
        spec = V4.generer_monde_v4(P1.cle("pilote-v2-essai-developpement", r))
        sha = hashlib.sha256(M.json_canonique(spec)).hexdigest()
        mondes.append({"monde": r, "spec": spec, "spec_sha256": sha})
        specs[r] = spec
    pm_ = preparer_mondes(mondes)

    def jeu(trouvent, etats=None, vides=()):
        """trouvent : ensemble des (monde, proposeur) dont la carte 1 porte la première conditionnelle."""
        cartes, appels = [], []
        for w in sorted(specs):
            spec, prem = specs[w], pm_[w]["premiere"]
            autres = [e["id"] for e in spec["effets"] if e["classe"] not in ("latente", "conditionnelle")]
            for prop in PROPOSEURS:
                et = (etats or {}).get((w, prop), "complet")
                appels.append({"monde": w, "proposeur": prop, "etat": et})
                if et == "echec":
                    continue
                for e in range(1, EMPLACEMENTS + 1):
                    if (w, prop) in vides:
                        cartes.append({"monde": w, "proposeur": prop, "emplacement": e, "etat": "refusee",
                                       "loi": {"type": "fixe", "probas": [1, 1, 1]}})
                        continue
                    S_ = [autres[(e + PROPOSEURS.index(prop)) % len(autres)]]
                    if (w, prop) in trouvent and e == 1:
                        S_ = S_ + [prem]
                    cartes.append({"monde": w, "proposeur": prop, "emplacement": e, "etat": "admise",
                                   "loi": P1._bruiter(spec, S_, 0.05, np.random.default_rng(P1.cle("carte", w, prop, e)))})
        return cartes, appels
    tous = {(w, p) for w in specs for p in PROPOSEURS}
    res = {}
    # cas sain P-2 : 2 appels sur 16 trouvent
    c, a = jeu({(1, "fable52"), (3, "argon")})
    r = mesurer(mondes, c, a)
    res["P-2_deux_sur_seize"] = {"issue": r["regle"]["issue"], "x": r["principale"]["x"], "n": r["principale"]["n"],
                                 "attendu": "P-2, x = 2, n = 16", "conforme": r["regle"]["issue"] == "P-2" and r["principale"]["x"] == 2
                                 and r["principale"]["n"] == 16}
    # P-1 : tous trouvent
    c, a = jeu(tous)
    r = mesurer(mondes, c, a)
    res["P-1_seize_sur_seize"] = {"issue": r["regle"]["issue"], "conforme": r["regle"]["issue"] == "P-1"}
    # P-0 : 5 échecs → 11 répondus < 12
    ech = {(1, "fable52"): "echec", (2, "opus55"): "echec", (3, "argon"): "echec", (4, "astra"): "echec", (1, "opus55"): "tronque"}
    c, a = jeu(set(), ech)
    r = mesurer(mondes, c, a)
    res["P-0_onze_repondus"] = {"issue": r["regle"]["issue"], "appels": r["appels"], "conforme": r["regle"]["issue"] == "P-0"}
    # P-0 : 13 répondus mais un monde à 2 (minimum par monde)
    ech = {(1, "fable52"): "echec", (1, "opus55"): "tronque"}
    c, a = jeu(set(), ech, vides={(2, "argon")})
    r = mesurer(mondes, c, a)
    res["P-0_monde_a_deux"] = {"issue": r["regle"]["issue"], "par_monde": r["repondus_par_monde"], "appels": r["appels"],
                               "conforme": r["regle"]["issue"] == "P-0" and r["appels"]["sans_carte"] == 1}
    # minimum tout juste tenu : 12 répondus, 3 par monde → pas P-0
    ech = {(w, "astra"): "echec" for w in specs}
    c, a = jeu(set(), ech)
    r = mesurer(mondes, c, a)
    res["minimum_tenu_douze"] = {"issue": r["regle"]["issue"], "n": r["principale"]["n"],
                                 "conforme": r["regle"]["issue"] == "P-2" and r["principale"]["n"] == 12}
    # artefacts : refus propres
    c0, a0 = jeu(set())
    arte = {
        "appel_manquant": (mondes, c0, a0[:-1]),
        "appel_en_double": (mondes, c0, a0 + [a0[0]]),
        "proposeur_inconnu": (mondes, c0, a0[:-1] + [dict(a0[-1], proposeur="kimi")]),
        "emplacement_non_entier": (mondes, c0 + [dict(c0[0], emplacement=2.5)], a0),
        "emplacement_en_double": (mondes, c0 + [c0[0]], a0),
        "septieme_admise": (mondes, c0 + [dict(c0[0], emplacement=7)], a0),
        "carte_d_un_appel_en_echec": (mondes, c0, [dict(x, etat="echec") if (x["monde"], x["proposeur"]) == (1, "fable52") else x for x in a0]),
        "empreinte_du_monde_fausse": ([dict(mondes[0], spec_sha256="0" * 64)] + mondes[1:], c0, a0),
        "trois_mondes": (mondes[:3], c0, a0)}
    refus = {}
    for nom, args in arte.items():
        try:
            mesurer(*args)
            refus[nom] = "NON REFUSÉ (défaut)"
        except Refus as x:
            refus[nom] = f"refusé : {x}"
    res["artefacts"] = refus
    # septième carte refusée au gardien : acceptée, comptée
    r = mesurer(mondes, c0 + [dict(c0[0], emplacement=7, etat="refusee")], a0)
    res["septieme_refusee_comptee"] = {"au_dela_de_six": r["cartes"]["au_dela_de_six"], "conforme": r["cartes"]["au_dela_de_six"] == 1}
    # carte non évaluable : réserve listée, ne porte pas
    c1 = [dict(x) for x in c0]
    c1[0] = dict(c1[0], loi={"type": "moyenne_glissante", "nombre_issues": 3, "fenetre": 5})
    r = mesurer(mondes, c1, a0)
    res["non_evaluable_listee"] = {"liste": r["cartes"]["non_evaluables"], "conforme": len(r["cartes"]["non_evaluables"]) == 1}
    # E-4 : un proposeur trouve partout, les trois autres jamais → survie par produit nulle
    c, a = jeu({(w, "opus55") for w in specs})
    r = mesurer(mondes, c, a)
    res["E-4_un_proposeur_trouve_tout"] = {"issue": r["regle"]["issue"], "principale": r["principale"]["x"],
                                           "survie_par_produit": r["survie_par_produit"],
                                           "noeuds": r["regle"].get("noeuds_avant_banc"),
                                           "conforme": r["survie_par_produit"]["survie_une_generation"] == 0.0}
    # imports gelés : un faux compagnon est refusé
    try:
        f = os.path.join(OUTILS_V4, "monde_riche_v4.py")
        ATTENDUES[f], ancien = "0" * 64, ATTENDUES[f]
        try:
            verifier_imports()
            res["imports_faux_attendu"] = "NON REFUSÉ (défaut)"
        except Refus as x:
            res["imports_faux_attendu"] = f"refusé : {x}"
        finally:
            ATTENDUES[f] = ancien
    except KeyError:
        res["imports_faux_attendu"] = "essai impossible"
    ok = all(v.get("conforme") for k, v in res.items() if isinstance(v, dict) and "conforme" in v) \
        and all(v.startswith("refusé") for v in res["artefacts"].values()) and res["imports_faux_attendu"].startswith("refusé")
    res["tout_conforme"] = ok
    return res


def ecrire(chemin, commande, corps, debut, imports):
    """S-7 : heures et chemin hors du corps empreinté."""
    texte = json.dumps(corps, ensure_ascii=False, sort_keys=True, default=str)
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump({"corps": corps, "corps_sha256": hashlib.sha256(texte.encode("utf-8")).hexdigest(),
                   "hors_corps": {"commande": commande, "debut_utc": debut,
                                  "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                                  "script_sha256": _sha(os.path.abspath(__file__)), "modules_importes": imports}},
                  f, ensure_ascii=False, indent=1, sort_keys=True, default=str)


def main(argv):
    if len(argv) < 3 or os.path.exists(argv[-1]):
        print(__doc__)
        return 2
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    try:
        imports = verifier_imports()
        if argv[1] == "taux" and len(argv) == 3:
            corps = taux()
        elif argv[1] == "graine" and len(argv) == 3:
            corps = essai_graine()
        elif argv[1] == "essai" and len(argv) == 3:
            corps = essai()
        elif argv[1] == "mesurer" and len(argv) == 5:
            mondes = json.load(open(argv[2], encoding="utf-8"))
            donnees = json.load(open(argv[3], encoding="utf-8"))
            if not isinstance(donnees, dict) or set(donnees) != {"cartes", "appels"}:
                raise Refus("CARTES.json : objet {cartes, appels}")
            corps = mesurer(mondes, donnees["cartes"], donnees["appels"])
        else:
            print(__doc__)
            return 2
    except Refus as x:
        print(f"refus : {x}", file=sys.stderr)
        return 2
    ecrire(argv[-1], argv[1], corps, debut, imports)
    print(json.dumps(corps, ensure_ascii=False, default=str)[:4000])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
