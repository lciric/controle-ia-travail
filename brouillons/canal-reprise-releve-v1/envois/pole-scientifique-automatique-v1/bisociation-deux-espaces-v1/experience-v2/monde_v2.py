"""Générateur de mondes à deux espaces (domaines, concepts) — v2. Applique le § 1 (G1 à G12) et le § 6 du
préenregistrement scellé `prereg/preenregistrement-bisociation-deux-espaces-v2.md` (e821e875…).

Étend `trancher-recombinaison/monde_v1.py` (af907b1d…), importé tel quel et jamais modifié : ses fonctions
`_champs`, `_groupes`, `_articles`, `_compatibiliser`, `_observer_contraintes`, `_cosinus`, `eloignes`, `proches`
et ses niveaux d'observation des opérateurs (`NIVEAUX`) sont réutilisés ; la plantation et l'observation sont
réécrites ici pour séparer les rôles de graine du § 7 (monde 0, opérateurs 1, concepts 2, contraintes 3, miroir 7).

G1 : un monde est une paire (Latent, Obs). Les bras ne reçoivent que `Obs`, dont tout attribut absent lève
`AccesLatent` ; `Monde.latent(jeton)` lève `AccesLatent` sans le jeton de mesure `JETON_MESURE`. La vue observée ne porte
pas le nom de la condition (corrections v2, contre-lecture du code).

Corrections v2 (décisions de Lazar R-600, addendum `prereg/addendum-ecarts-bisociation-deux-espaces-v2-v2.md`) :
G11 lu en (b) — un échec de plantation retente seulement le placement des ponts sur le même monde de base (au plus
MAX_REPLANTATIONS fois, flux (code, m, 0, t, r)), puis régénère le monde entier ; V4 lu en « copie ».
"""
import copy
import sys
from collections import Counter
from pathlib import Path
from types import MappingProxyType

import numpy as np

ICI = Path(__file__).resolve().parent
V1 = ICI.parent.parent / "trancher-recombinaison"
if str(V1) not in sys.path:
    sys.path.append(str(V1))
import monde_v1 as mo  # noqa: E402  (v1, inchangé)

from controle_ia.gardes import GardeArret  # noqa: E402

import graines_v2 as gr  # noqa: E402


class AccesLatent(Exception):
    """Un bras (ou tout code sans le jeton de mesure) a demandé un champ latent."""


class EchecPlantation(Exception):
    """Un pont n'a pas pu être planté en 1 000 essais (G11). Addendum v2, Q-01 (b) : le placement des ponts est
    retenté sur le même monde de base (replantation comptée) ; après MAX_REPLANTATIONS replantations échouées, le monde
    entier est régénéré (tentative suivante, comptée)."""


JETON_MESURE = object()

# G9 : niveaux (couverture c ; parasites p_par ; fuite de domaine rho) du canal des concepts (choix d'auteur scellé)
NIVEAUX_CONCEPTS = {"bien": (0.85, 0.05, 0.05), "moyen": (0.65, 0.15, 0.15), "mal": (0.45, 0.30, 0.30)}

N_FONDS = 10          # G3, choix d'auteur scellé
N_RARES = 18          # G4, choix d'auteur scellé
MOTS_PAR_CONCEPT = 2  # G9, choix d'auteur scellé

# Paramètres gelés par Lazar (S16, R-580), désignés par leur nom
S16 = {
    "lambda": 0.7, "lambda_faible": 0.3,       # S16a
    "taille_palette": 4,                        # S16b
    "loi_fonds": {2: 1.0},                      # S16c : exactement 2
    "loi_fonds_1ou2": {1: 0.6, 2: 0.4},         # S16c, M_fonds_1ou2
    "loi_emetteurs": (2, 3, 4),                 # S16d : uniforme, même loi pour tous les statuts
    "ponts": {"greffes": 3, "jumeaux": 3, "b": 3, "c": 3, "d": 3, "e": 3},          # S16e
    "ponts_V_surface": {"greffes": 3, "jumeaux": 3, "b": 3, "c": 2, "d": 2, "e": 5},  # S16e
    "phi": 4,                                   # S16f
}

BASE_V2 = {
    "niveau": "bien", "verite": "eloignes", "groupes": "champs", "palettes": "champs",
    "lambda": S16["lambda"], "taille_palette": S16["taille_palette"], "loi_fonds": S16["loi_fonds"],
    "p_moyeu_concept": 0.30, "rho": None, "ponts": S16["ponts"], "sans_pont": False,
    "concepts_absents": False, "palettes_disjointes": False, "inertes": False,
    "jumelle": False,   # V4 seulement (validation) : copie des mots propres (addendum v2, Q-04 « copie », R-600)
}

CONDITIONS_V2 = {
    "M_bien": {"niveau": "bien"},
    "M_moyen": {"niveau": "moyen"},
    "M_mal": {"niveau": "mal"},
    "SP": {"niveau": "bien", "sans_pont": True},
    "INV": {"niveau": "bien", "verite": "proches", "groupes": "transversal", "palettes": "groupes"},
    "V_fuite": {"niveau": "bien", "rho": 0.6},
    "V_concepts_absents": {"niveau": "bien", "concepts_absents": True},
    "V_moyeu_conceptuel": {"niveau": "bien", "p_moyeu_concept": 0.6},
    "V_surface": {"niveau": "bien", "ponts": S16["ponts_V_surface"]},
    "M_inertes": {"niveau": "bien", "inertes": True},
    "M_couplage_faible": {"niveau": "bien", "lambda": S16["lambda_faible"]},
    "M_palettes_communes": {"niveau": "bien", "taille_palette": N_FONDS},
    "M_palettes_disjointes": {"niveau": "bien", "palettes_disjointes": True},
    "M_fonds_1ou2": {"niveau": "bien", "loi_fonds": S16["loi_fonds_1ou2"]},
}
CONDITIONS_NR = {"NR_bien": "bien", "NR_moyen": "moyen"}
MAX_TENTATIVES = 200
# Addendum v2, Q-01 (b) (R-600) : replantations sur le même monde de base avant une régénération entière (choix de code,
# déclaré ; la contre-lecture du code a essayé ≤ 50 et n'a jamais eu besoin de régénérer sur 2 400 mondes d'essai).
MAX_REPLANTATIONS = 50


# --- gardes de configuration (S16e, loi de M_fonds_1ou2) ----------------------------------------------------

def garde_configuration(p):
    """Liste d'arrêt : 2 × paires de ponts ≤ 36, concepts rares requis ≤ 18, loi des fonds sommant à 1."""
    pt = p["ponts"]
    n_paires = sum(pt[k] for k in ("greffes", "jumeaux", "b", "c", "d", "e"))
    if 2 * n_paires > 36:
        raise GardeArret(f"configuration hors garde S16e : 2 × {n_paires} paires de ponts > 36")
    rares = pt["greffes"] + pt["jumeaux"] + pt["b"] + pt["c"] + pt["d"]
    if rares > N_RARES:
        raise GardeArret(f"configuration hors garde S16e : {rares} concepts rares requis > {N_RARES}")
    loi = p["loi_fonds"]
    if abs(sum(loi.values()) - 1.0) > 1e-12 or any(v < 0 for v in loi.values()):
        raise GardeArret(f"loi du nombre de concepts de fond {loi} : probabilités ne sommant pas à 1")
    if max(loi) > p["taille_palette"] and not p["palettes_disjointes"]:
        raise GardeArret("nombre de concepts de fond par article > taille de palette")
    return n_paires, rares


# --- objets G1 --------------------------------------------------------------------------------------------

class Obs:
    """Vue observée en lecture seule. Tout attribut absent (champ latent, vérité, provenance…) lève AccesLatent."""
    __slots__ = ("n", "cos", "etiq_op", "etiq_co", "c_obs", "dom_obs", "q", "df", "paires", "valides", "pont",
                 "_fige")  # sans le nom de la condition (contre-lecture du code, G1) ni les indicateurs `nr` et
    # `concepts_absents`, qui désignaient NR et V_concepts_absents (CLA-09) : la non-applicabilité de d1c est décidée
    # par mesures_v2.NON_APPLICABLES

    def __init__(self, **champs):
        for k, v in champs.items():
            object.__setattr__(self, k, v)
        object.__setattr__(self, "_fige", True)

    def __getattr__(self, nom):
        raise AccesLatent(f"accès refusé : « {nom} » n'est pas un champ observé")

    def __setattr__(self, nom, valeur):
        raise AccesLatent(f"Obs est en lecture seule (« {nom} »)")


class Latent:
    def __init__(self, **champs):
        self.__dict__.update(champs)


class Monde:
    __slots__ = ("obs", "_latent")

    def __init__(self, obs, latent):
        object.__setattr__(self, "obs", obs)
        object.__setattr__(self, "_latent", latent)

    def latent(self, jeton=None):
        if jeton is not JETON_MESURE:
            raise AccesLatent("Latent n'est lisible qu'avec le jeton de mesure")
        return self._latent


# --- étage commun (§ 2), ne lit que des observations -----------------------------------------------------

def etage_commun(n, etiq, c_obs, dom_obs, df):
    """Paires valides : domaines observés différents, contraintes observées compatibles, au moins une étiquette
    observée partagée (opérateur ou concept). Pont retenu : étiquette partagée la plus rare (df, puis nom)."""
    paires, valides, pont = [], [], []
    for i in range(n):
        for j in range(i + 1, n):
            x = len(paires)
            paires.append((i, j))
            partage = etiq[i] & etiq[j]
            ok = (dom_obs[i] != dom_obs[j]
                  and not any({a, b} == {"+", "-"} for a, b in zip(c_obs[i], c_obs[j]))
                  and bool(partage))
            if ok:
                valides.append(x)
                pont.append(min(partage, key=lambda m: (df[m], m)))
            else:
                pont.append(None)
    return tuple(paires), tuple(valides), tuple(pont)


def _figer(a):
    a = np.array(a, dtype=float)
    a.setflags(write=False)
    return a


# --- latents : concepts de fond, plantation ---------------------------------------------------------------

def _palettes(rng, p, n_cles):
    if p["palettes_disjointes"]:
        ordre = list(range(N_FONDS))
        rng.shuffle(ordre)
        tailles = [N_FONDS // n_cles + (1 if i < N_FONDS % n_cles else 0) for i in range(n_cles)]
        if min(tailles) < 2:
            raise GardeArret("palettes disjointes : moins de 2 concepts par champ")
        out, debut = [], 0
        for t in tailles:
            out.append(sorted(ordre[debut:debut + t]))
            debut += t
        return out
    return [sorted(rng.sample(range(N_FONDS), p["taille_palette"])) for _ in range(n_cles)]


def _tirer_nb_fonds(rng, loi):
    valeurs = sorted(loi)
    if len(valeurs) == 1:
        return valeurs[0]
    return rng.choices(valeurs, weights=[loi[v] for v in valeurs])[0]


def _planter_v2(rng, p, arts, champ, groupe, ops_groupe):
    """G6 : greffes et jumeaux (logique de monde_v1._planter, reprise mot pour mot), puis ponts (b) à (e).
    Un ensemble `utilises` commun : au plus 36 articles distincts. Lève EchecPlantation après 1 000 essais."""
    relation = mo.eloignes if p["verite"] == "eloignes" else mo.proches
    relation_d = mo.proches if p["verite"] == "eloignes" else mo.eloignes  # ponts (d) : proches en M, éloignés en INV
    k, utilises, plantes = len(champ), set(), []
    pt = p["ponts"]
    libres = lambda: [i for i in range(len(arts)) if i not in utilises]
    for _ in range(pt["greffes"]):
        for _essai in range(1000):
            a = rng.choice(libres())
            da = arts[a]["dom"]
            cibles = [d for d in range(k) if relation(champ, da, d) and groupe[d] != groupe[da]]
            if not cibles:
                continue
            d_src = rng.choice(cibles)
            m = rng.choice(ops_groupe[groupe[d_src]])
            if m in arts[a]["ops"]:
                continue
            porteurs = [i for i in range(len(arts)) if i not in utilises and i != a
                        and arts[i]["dom"] == d_src and m in arts[i]["ops"]]
            libres_src = [i for i in range(len(arts)) if i not in utilises and arts[i]["dom"] == d_src]
            if porteurs:
                b = rng.choice(porteurs)
            elif libres_src:
                b = rng.choice(libres_src)
                arts[b]["ops"].append(m)
            else:
                continue
            arts[a]["ops"].append(m)
            mo._compatibiliser(arts[a], arts[b])
            utilises.update((a, b))
            plantes.append({"statut": "greffe", "a": a, "b": b, "op": m})
            break
        else:
            raise EchecPlantation("greffe")
    for t in range(pt["jumeaux"]):
        for _essai in range(1000):
            a = rng.choice(libres())
            cands = [i for i in range(len(arts)) if i not in utilises and i != a
                     and relation(champ, arts[a]["dom"], arts[i]["dom"])]
            if not cands:
                continue
            b = rng.choice(cands)
            op = f"j{t}"
            arts[a]["ops"].append(op)
            arts[b]["ops"].append(op)
            mo._compatibiliser(arts[a], arts[b])
            utilises.update((a, b))
            plantes.append({"statut": "jumeau", "a": a, "b": b, "op": op})
            break
        else:
            raise EchecPlantation("jumeau")

    def paire_libre(rel, sans_op_commun=True):
        for _essai in range(1000):
            a = rng.choice(libres())
            cands = [i for i in range(len(arts)) if i not in utilises and i != a
                     and rel(champ, arts[a]["dom"], arts[i]["dom"])
                     and not (sans_op_commun and set(arts[a]["ops"]) & set(arts[i]["ops"]))]
            if cands:
                return a, rng.choice(cands)
        return None

    for statut, cle, rel in (("conceptuel", "b", relation), ("faux", "c", relation), ("proche", "d", relation_d)):
        for _ in range(pt[cle]):
            pr = paire_libre(rel)
            if pr is None:
                raise EchecPlantation(statut)
            a, b = pr
            if statut == "faux":
                x = rng.randrange(len(arts[a]["c_vraies"]))
                arts[a]["c_vraies"][x], arts[b]["c_vraies"][x] = "+", "-"
            else:
                mo._compatibiliser(arts[a], arts[b])
            utilises.update((a, b))
            plantes.append({"statut": statut, "a": a, "b": b, "op": None})
    for _ in range(pt["e"]):
        pr = paire_libre(relation)
        if pr is None:
            raise EchecPlantation("surface")
        a, b = pr
        o_a, o_b = rng.choice(arts[a]["ops"]), rng.choice(arts[b]["ops"])
        utilises.update((a, b))
        plantes.append({"statut": "surface", "a": a, "b": b, "op": None, "o_a": o_a, "o_b": o_b})
    if len(utilises) > 36:
        raise GardeArret(f"{len(utilises)} articles de ponts > 36")
    return plantes


def _attribuer_rares(rng, p, plantes, n_arts):
    """G4, G5, G7 : concept rare par pont (a) avec la probabilité lambda, toujours pour (b), (c), (d) ; L_r et
    émetteurs de surface (parmi les 38 autres articles)."""
    reserve = list(range(N_RARES))
    rng.shuffle(reserve)
    rares = {}
    for pl in plantes:
        if pl["statut"] in ("greffe", "jumeau"):
            if not rng.random() < p["lambda"]:
                pl["rare"] = None
                continue
        elif pl["statut"] == "surface":
            pl["rare"] = None
            continue
        r = reserve.pop()
        lr = rng.choice(list(S16["loi_emetteurs"]))
        autres = [i for i in range(n_arts) if i not in (pl["a"], pl["b"])]
        surface = rng.sample(autres, lr - 2)
        pl["rare"] = r
        rares[r] = {"porteurs": (pl["a"], pl["b"]), "surface": surface, "L": lr, "statut": pl["statut"]}
    return rares


# --- observation : opérateurs et domaine (rôle 1), concepts (rôles 2 et 7), contraintes (rôle 3) ------------

def _observer_operateurs(rng, p, arts, champ, groupe, n_groupes, ops_groupe, forces):
    """Canal de v1 pour les opérateurs (couverture, homonymes systématiques, parasites), mots de domaine et
    étiquette de domaine observée ; reprise de monde_v1._observer sans les contraintes. `forces` : homonymes des
    ponts de surface (e), appliqués après les homonymes systématiques."""
    b = dict(mo.BASE)
    couverture, p_parasite, p_homonyme = mo.NIVEAUX[p["niveau"]]
    k = len(champ)
    mot = {}

    def mots_de(op, d):
        cle_d = None if op.startswith("h") else d
        return [mot.setdefault((op, cle_d, i), f"w_{op}_{cle_d}_{i}") for i in range(2)]

    homonymes = {}
    combos = sorted({(a["dom"], o) for a in arts for o in a["ops"] if o.startswith("g")})
    for d, o in combos:
        if groupe[d] != int(o[1:o.index("o")]) or rng.random() >= p_homonyme:
            continue
        g2 = rng.choice([g for g in range(n_groupes) if g != groupe[d]])
        m2 = rng.choice(ops_groupe[g2])
        d2 = rng.choice([x for x in range(k) if groupe[x] == g2])
        partage = mots_de(m2, d2)[0]
        mot[(o, d, 0)] = partage
        homonymes[partage] = m2
    for o_a, d_a, o_b, d_b in forces:
        w = mots_de(o_b, d_b)[0]
        mot[(o_a, d_a, 0)] = mot[(o_a, d_a, 1)] = w
        mot[(o_b, d_b, 1)] = w
        homonymes[w] = o_b
    lexique, zipf = {}, mo._zipf(b["vocab_general"], b["zipf_general"])

    def dans_lexique(w, canon, cov):
        if w not in lexique:
            lexique[w] = canon if rng.random() < cov else None
        return lexique[w]

    labels_fond = [o for g in range(n_groupes) for o in ops_groupe[g]]
    for a in arts:
        sac, etiq = [], {}
        for o in a["ops"] + a["moyeux"]:
            w = rng.choice(mots_de(o, a["dom"]))
            canon = homonymes.get(w, o)
            cov = b["couverture_moyeu"] if o.startswith("h") else couverture
            lab = dans_lexique(w, canon, cov)
            if lab is None:
                sac.append(w)
            else:
                prov = "moyeu" if lab.startswith("h") else ("vrai" if lab in a["ops"] else "homonyme")
                if etiq.get(lab) != "vrai":
                    etiq[lab] = prov
        if rng.random() < p_parasite:
            lab = rng.choice(labels_fond)
            if lab not in etiq:
                etiq[lab] = "vrai" if lab in a["ops"] else "parasite"
        for _ in range(b["mots_domaine"]):
            u = rng.random()
            if u < b["p_mot_global"]:
                sac.append(f"x{rng.randrange(b['vocab_global'])}")
            elif u < b["p_mot_global"] + b["p_mot_champ"]:
                sac.append(f"c{a['champ']}_{rng.randrange(b['vocab_champ'])}")
            else:
                sac.append(f"d{a.get('dom_mots', a['dom'])}_{rng.randrange(b['vocab_propre'])}")
        sac += [f"z{x}" for x in rng.choices(range(b["vocab_general"]), weights=zipf, k=b["mots_generaux"])]
        a["sac_domaine"], a["etiq_op"] = sac, etiq
        if rng.random() < b["p_etiquette_domaine_fausse"]:
            voisins = [d for d in range(k) if champ[d] == a["champ"] and d != a["dom"]]
            a["dom_obs"] = rng.choice(voisins or [d for d in range(k) if d != a["dom"]])
        else:
            a["dom_obs"] = a["dom"]


def _nom_concept(c):
    return c if isinstance(c, str) else (f"F{c}" if c < N_FONDS else f"R{c - N_FONDS}")


def _emettre(rng, p, a, concept, dominant, provenance_si_couvert):
    """G9 (i) couverture, (ii) fuite de domaine. Ordre des tirages fixé : mot, couverture, puis fuite."""
    c, _, rho = NIVEAUX_CONCEPTS[p["niveau"]]
    if p["rho"] is not None:
        rho = p["rho"]
    if p["concepts_absents"]:
        c = 0.0
    nom = _nom_concept(concept)
    w = rng.choice([f"wc_{nom}_{i}" for i in range(MOTS_PAR_CONCEPT)])
    if not rng.random() < c:
        a["sac_domaine"].append(w)  # fuite lexicale vers le vecteur de domaine (mesurée par F)
        return
    lab, prov = nom, provenance_si_couvert
    if rng.random() < rho:
        lab, prov = _nom_concept(dominant[a["dom"]]), "fuite"
    if a["etiq_co"].get(lab) != "vrai":
        a["etiq_co"][lab] = prov


def _observer_concepts_fond(rng, p, arts, dominant):
    """Passe A (rôle 2) : concepts de fond et moyeu de chaque article, puis parasites. Avant la couche des rares,
    de sorte qu'elle est égale bit à bit entre M_bien et M_inertes (G8)."""
    _, p_par, _ = NIVEAUX_CONCEPTS[p["niveau"]]
    tous = list(range(N_FONDS + N_RARES))  # 28 concepts (fond et rares), hors moyeu
    for a in arts:
        a["etiq_co"] = {}
        for f in sorted(a["fonds"]):
            _emettre(rng, p, a, f, dominant, "vrai")
        if a["moyeu_concept"]:
            _emettre(rng, p, a, "H", dominant, "moyeu")
        if not p["concepts_absents"] and rng.random() < p_par:
            c = rng.choice(tous)
            nom = _nom_concept(c)
            latent = (c < N_FONDS and c in a["fonds"]) or (c >= N_FONDS and (c - N_FONDS) in a["rares"])
            if nom not in a["etiq_co"]:
                a["etiq_co"][nom] = "vrai" if latent else "parasite"


def _observer_concepts_rares(rng, p, arts, rares, dominant, miroir):
    """Passe B : couche d'observation des concepts rares (rôle 2 ; rôle 7 et émetteurs tirés au hasard parmi
    les 40 dans M_inertes, G8)."""
    for r in sorted(rares):
        info = rares[r]
        if miroir:
            emetteurs = [int(i) for i in rng.sample(range(len(arts)), info["L"])]
        else:
            emetteurs = list(info["porteurs"]) + list(info["surface"])
        for e in emetteurs:
            prov = "vrai" if r in arts[e]["rares"] else ("surface" if not miroir else "miroir")
            _emettre(rng, p, arts[e], N_FONDS + r, dominant, prov)


# --- monde complet ----------------------------------------------------------------------------------------

def _tirer_base(p, rng0):
    """Monde de base (rôle 0, avant les ponts) : champs, groupes, articles (domaines, opérateurs, moyeux, contraintes
    vraies, q), palettes, concepts de fond, moyeu de concept. Inchangé par une replantation (addendum v2, Q-01 (b))."""
    base = dict(mo.BASE)
    base.update({"verite": p["verite"], "groupes": p["groupes"], "niveau": p["niveau"]})
    if "champs_choix" in p:  # réservé à l'essai R5 de l'échec de plantation (jamais dans une condition)
        base["champs_choix"] = p["champs_choix"]
    f, champ = mo._champs(rng0, base)
    n_groupes, groupe = mo._groupes(base, f, champ)
    arts, ops_groupe = mo._articles(rng0, base, champ, groupe, n_groupes)
    cles = groupe if p["palettes"] == "groupes" else champ
    palettes = _palettes(rng0, p, (n_groupes if p["palettes"] == "groupes" else f))
    for a in arts:
        pal = palettes[cles[a["dom"]]]
        a["fonds"] = sorted(rng0.sample(pal, _tirer_nb_fonds(rng0, p["loi_fonds"])))
        a["moyeu_concept"] = rng0.random() < p["p_moyeu_concept"]
        a["rares"] = set()
    return base, f, champ, n_groupes, groupe, arts, ops_groupe


def _construire(p, racine, code_latent, code_miroir, indice, tentative, condition):
    g = lambda code, role: gr.RngAdapte(gr.generateur(racine, code, indice, role, tentative))
    rng0 = g(code_latent, gr.ROLE_MONDE)
    base, f, champ, n_groupes, groupe, arts, ops_groupe = _tirer_base(p, rng0)
    # Addendum v2, Q-01 (b) : le monde de base (champs, groupes, articles, opérateurs, contraintes vraies, q, palettes,
    # fonds, moyeu) est tiré une fois ; seul le placement des ponts est retenté. Replantation 0 : suite du flux rng0
    # (mondes sans échec identiques bit à bit au code d'avant l'addendum) ; replantation r ≥ 1 : flux
    # (code, m, 0, t, r). La suite du rôle 0 (rares, ordre des articles) continue sur le flux de la plantation réussie.
    replantations, echecs_plantation = 0, []
    if p["sans_pont"]:
        plantes, rng_p = [], rng0
    else:
        base_arts = arts
        for r in range(MAX_REPLANTATIONS + 1):
            rng_p = rng0 if r == 0 else gr.RngAdapte(gr.generateur(racine, code_latent, indice, gr.ROLE_MONDE,
                                                                    tentative, replantation=r))
            arts = copy.deepcopy(base_arts)
            try:
                plantes = _planter_v2(rng_p, p, arts, champ, groupe, ops_groupe)
            except EchecPlantation as e:
                echecs_plantation.append(str(e))
                continue
            replantations = r
            break
        else:
            raise EchecPlantation(f"{MAX_REPLANTATIONS} replantations échouées sur le même monde de base "
                                  f"({echecs_plantation[:3]})")
    rng0 = rng_p
    rares = _attribuer_rares(rng0, p, plantes, len(arts))
    for r, info in rares.items():
        for i in info["porteurs"]:
            arts[i]["rares"].add(r)
    ordre = list(range(len(arts)))
    rng0.shuffle(ordre)
    pos = {ancien: nouveau for nouveau, ancien in enumerate(ordre)}
    arts = [arts[i] for i in ordre]
    for pl in plantes:
        pl["a"], pl["b"] = pos[pl["a"]], pos[pl["b"]]
    for info in rares.values():
        info["porteurs"] = tuple(pos[i] for i in info["porteurs"])
        info["surface"] = [pos[i] for i in info["surface"]]
    forces = [(pl["o_a"], arts[pl["a"]]["dom"], pl["o_b"], arts[pl["b"]]["dom"]) for pl in plantes
              if pl["statut"] == "surface"]
    if p["jumelle"]:
        # V4, addendum v2, Q-04 « copie » (R-600) : mêmes latents, mêmes flux de graines des rôles 1 à 3 ; pour chaque
        # pont planté, l'article de plus grand indice (ordre final des articles) prend les mots propres du domaine de
        # l'article de plus petit indice ; règle déterministe, sans tirage.
        for pl in plantes:
            bas, haut = min(pl["a"], pl["b"]), max(pl["a"], pl["b"])
            arts[haut]["dom_mots"] = arts[bas]["dom"]
    # concept de fond dominant de chaque domaine (latent ; départage par indice)
    dominant = {}
    for d in range(len(champ)):
        cpt = Counter(fd for a in arts if a["dom"] == d for fd in a["fonds"])
        dominant[d] = min(cpt, key=lambda x: (-cpt[x], x)) if cpt else 0
    _observer_operateurs(g(code_latent, gr.ROLE_OBS_OPERATEURS), p, arts, champ, groupe, n_groupes, ops_groupe,
                         forces)
    rng2 = g(code_latent, gr.ROLE_OBS_CONCEPTS)
    _observer_concepts_fond(rng2, p, arts, dominant)
    if p["inertes"]:
        _observer_concepts_rares(g(code_miroir, gr.ROLE_MIROIR), p, arts, rares, dominant, miroir=True)
    else:
        _observer_concepts_rares(rng2, p, arts, rares, dominant, miroir=False)
    rng3 = g(code_latent, gr.ROLE_CONTRAINTES)
    for a in arts:
        a["c_obs"] = mo._observer_contraintes(rng3, a["c_vraies"], base["bruit_contraintes"], base["axe_homographe"])
    cos = mo._cosinus(arts, "tf")
    return f, champ, groupe, arts, plantes, rares, cos, dominant, (replantations, echecs_plantation)


def _verite(p, champ, arts, paires):
    """G12 : vérité par une seule fonction sur les latents."""
    relation = mo.eloignes if p["verite"] == "eloignes" else mo.proches
    vrais, info = set(), []
    for x, (i, j) in enumerate(paires):
        ai, aj = arts[i], arts[j]
        op_commun = set(ai["ops"]) & set(aj["ops"])
        rare_commun = ai["rares"] & aj["rares"]
        compat = not any({u, v} == {"+", "-"} for u, v in zip(ai["c_vraies"], aj["c_vraies"]))
        v = relation(champ, ai["dom"], aj["dom"]) and bool(op_commun or rare_commun) and compat
        if v:
            vrais.add(x)
        info.append({"compat_vraie": compat, "op_commun": sorted(op_commun), "rare_commun": sorted(rare_commun),
                     "proche": mo.proches(champ, ai["dom"], aj["dom"]),
                     "eloigne": mo.eloignes(champ, ai["dom"], aj["dom"])})
    return vrais, info


def monde_de_base(condition, racine, indice, tentative=0):
    """Monde de base d'une tentative, sans ponts (instrument d'essai de la replantation ; lit des latents)."""
    p = dict(BASE_V2)
    p.update(CONDITIONS_V2[condition])
    code_latent = gr.CODES_CONDITION["M_bien"] if p["inertes"] else gr.CODES_CONDITION[condition]
    rng0 = gr.RngAdapte(gr.generateur(racine, code_latent, indice, gr.ROLE_MONDE, tentative))
    _, f, champ, _, groupe, arts, _ = _tirer_base(p, rng0)
    return f, champ, groupe, arts


def signature_base(champ, groupe, arts):
    """Ce qu'une replantation ne doit pas changer : champs, groupes, et le multiensemble (domaine, q, fonds, moyeu de
    concept, moyeux d'opérateur) des articles (l'ordre final des articles est tiré après les ponts)."""
    return (tuple(champ), tuple(groupe),
            tuple(sorted((a["dom"], a["q"], tuple(a["fonds"]), bool(a["moyeu_concept"]), tuple(a["moyeux"]))
                         for a in arts)))


def generer(condition, racine, indice, surcharge=None):
    """Monde v2 d'une condition (§ 6). M_inertes : rôles 0 à 3 sous le code 1, miroir sous (12, m, 7) (§ 7)."""
    if condition in CONDITIONS_NR:
        return generer_nr(condition, racine, indice)
    p = dict(BASE_V2)
    p.update(CONDITIONS_V2[condition])
    if surcharge:
        p.update(surcharge)
    garde_configuration(p)
    code = gr.CODES_CONDITION[condition]
    code_latent = gr.CODES_CONDITION["M_bien"] if p["inertes"] else code
    code_latent = p.get("_code_latent_force", code_latent)  # réservé à l'essai R5 de la graine du monde inerte
    echecs = []
    for tentative in range(MAX_TENTATIVES):
        try:
            f, champ, groupe, arts, plantes, rares, cos, dominant, (replantations, echecs_pl) = _construire(
                p, racine, code_latent, code, indice, tentative, condition)
        except EchecPlantation as e:
            echecs.append(str(e))
            continue
        break
    else:
        raise GardeArret(f"{condition} {indice} : {MAX_TENTATIVES} tentatives de plantation échouées ({echecs[:3]})")
    n = len(arts)
    etiq_op = tuple(frozenset("op:" + k for k in a["etiq_op"]) for a in arts)
    etiq_co = tuple(frozenset("co:" + k for k in a["etiq_co"]) for a in arts)
    df = Counter()
    for i in range(n):
        df.update(etiq_op[i] | etiq_co[i])
    c_obs = tuple(tuple(a["c_obs"]) for a in arts)
    dom_obs = tuple(a["dom_obs"] for a in arts)
    paires, valides, pont = etage_commun(n, [etiq_op[i] | etiq_co[i] for i in range(n)], c_obs, dom_obs, df)
    obs = Obs(n=n, cos=_figer(cos), etiq_op=etiq_op, etiq_co=etiq_co, c_obs=c_obs, dom_obs=dom_obs,
              q=tuple(a["q"] for a in arts), df=MappingProxyType(dict(df)), paires=paires, valides=valides,
              pont=pont)
    vrais, info = _verite(p, champ, arts, paires)
    plante = {}
    for pl in plantes:
        cle = (min(pl["a"], pl["b"]), max(pl["a"], pl["b"]))
        plante[paires.index(cle)] = pl["statut"]
    rng_sp = gr.generateur(racine, code, indice, gr.ROLE_PLACEBO_SP)
    nb_pl = min(6, len(valides))
    placebo = {valides[int(k)] for k in rng_sp.choice(len(valides), size=nb_pl, replace=False)} if nb_pl else set()
    latent = Latent(condition=condition, params=p, n_champs=f, champ=champ, groupe=groupe, arts=arts,
                    plantes=plantes, rares=rares, vrais=vrais, info_paires=info, plante=plante,
                    placebo=placebo, tentatives=len(echecs), echecs=echecs, replantations=replantations,
                    echecs_plantation=echecs_pl, dominant=dominant, nr=False)
    return Monde(obs, latent)


def generer_nr(condition, racine, indice):
    """Mondes NR (§ 6) : monde_v1 inchangé, graine = premier mot de SeedSequence(...).generate_state(1) passé à
    random.Random ; « concept » := étiquette d'opérateur observée ; d1c ≡ d1 (non applicable)."""
    code = gr.CODES_CONDITION[condition]
    graine = int(gr.sequence(racine, code, indice, gr.ROLE_MONDE).generate_state(1)[0])
    w = mo.generer({"niveau": CONDITIONS_NR[condition]}, graine)
    arts = w["arts"]
    n = w["n"]
    etiq = tuple(frozenset("op:" + k for k in a["etiquettes"]) for a in arts)
    df = Counter()
    for e in etiq:
        df.update(e)
    c_obs = tuple(tuple(a["c_obs"]) for a in arts)
    dom_obs = tuple(a["dom_obs"] for a in arts)
    paires, valides, pont = etage_commun(n, list(etiq), c_obs, dom_obs, df)
    if list(valides) != list(w["valides"]):
        raise GardeArret("NR : étage commun v2 ≠ paires valides de monde_v1")
    obs = Obs(n=n, cos=_figer(w["cos"]), etiq_op=etiq, etiq_co=etiq, c_obs=c_obs, dom_obs=dom_obs,
              q=tuple(a["q"] for a in arts), df=MappingProxyType(dict(df)), paires=paires, valides=valides,
              pont=pont)
    info = [{"compat_vraie": pp["compat_vraie"], "op_commun": pp["op_commun"], "rare_commun": [],
             "proche": pp["proche"], "eloigne": pp["eloigne"]} for pp in w["paires"]]
    plante = {}
    for t, a, b, _m in w["plantes"]:
        plante[paires.index((min(a, b), max(a, b)))] = t
    latent = Latent(condition=condition, params={"niveau": CONDITIONS_NR[condition]}, n_champs=w["n_champs"],
                    champ=w["champ"], groupe=w["groupe"], arts=arts, plantes=w["plantes"], rares={},
                    vrais=set(w["vrais"]), info_paires=info, plante=plante, placebo=set(w["placebo"]),
                    tentatives=0, echecs=[], replantations=0, echecs_plantation=[], dominant={}, nr=True,
                    graine_v1=graine)
    return Monde(obs, latent)


def empreinte_latents(monde):
    """Comparaison bit à bit des latents (G8) : champs, groupes, articles latents (sans observations), ponts."""
    import hashlib
    import json
    L = monde.latent(JETON_MESURE)
    arts = [{k: (sorted(v) if isinstance(v, set) else v) for k, v in a.items()
             if k in ("dom", "champ", "ops", "moyeux", "c_vraies", "q", "fonds", "moyeu_concept", "rares")}
            for a in L.arts]
    corps = {"champ": L.champ, "groupe": L.groupe, "arts": arts,
             "plantes": [{k: v for k, v in pl.items()} for pl in L.plantes],
             "rares": {str(r): {"porteurs": list(i["porteurs"]), "surface": list(i["surface"]), "L": i["L"],
                                "statut": i["statut"]}
                       for r, i in L.rares.items()},
             "vrais": sorted(L.vrais)}
    return hashlib.sha256(json.dumps(corps, sort_keys=True, default=str).encode()).hexdigest()
