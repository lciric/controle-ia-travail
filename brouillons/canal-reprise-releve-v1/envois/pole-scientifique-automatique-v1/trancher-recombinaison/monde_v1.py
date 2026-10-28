"""Générateur de mondes synthétiques à vérité connue — trancher la recombinaison bisociative (v1).

Bibliothèque standard seulement ; une graine par monde (random.Random(graine)), consignée par le lanceur.
Un monde :
- K domaines regroupés en champs (proches = même champ, domaines différents ; éloignés = champs différents) ;
- des opérateurs latents par groupe : groupe = champ dans les mondes ordinaires, groupe transversal aux champs
  dans le monde à vérité inversée (miroir exact) ; opérateurs « solo » propres à un article ; opérateurs moyeux ;
- des articles = sacs de mots (mots de champ, mots propres au domaine, mots généraux, un mot de surface par
  opérateur, propre au couple (opérateur, domaine) : le même opérateur latent porte des mots différents) ;
- un lexique imparfait (couverture, homonymes systématiques, étiquettes parasites) qui produit les étiquettes
  d'opérateur observées ; des contraintes sur 4 axes observées par le canal bruité de l'essai b4 ;
- des ponts plantés : greffes (un opérateur d'un autre groupe entre dans un article) et jumeaux (un opérateur
  rare partagé par deux articles), contraintes rendues compatibles avec un partenaire.
Vérité : paire en relation cible (éloignés, ou proches si vérité inversée), partageant un opérateur latent non
moyeu, à contraintes vraies compatibles. Les méthodes ne voient que les observations.
"""
import math
import random
from collections import Counter

NIVEAUX = {  # (couverture du lexique, part d'articles à étiquette parasite, taux de combinaisons homonymes)
    "bien": (0.90, 0.05, 0.05),
    "moyen": (0.70, 0.15, 0.10),
    "mal": (0.45, 0.30, 0.20),
}

BASE = {
    "n_domaines": 8, "articles_par_domaine": 5, "champs_choix": (2, 3, 4),
    "ops_par_groupe": 3, "p_op_groupe": 0.7, "p_secondaire": 0.3, "p_secondaire_groupe": 0.5,
    "n_moyeux": 1, "p_moyeu": 0.25, "couverture_moyeu": 0.95,
    "n_greffes": 3, "n_jumeaux": 3,
    "verite": "eloignes", "groupes": "champs", "niveau": "bien",
    "bruit_contraintes": (0.15, 0.15, 0.10), "n_axes": 4, "p_axes": (0.3, 0.3, 0.4), "axe_homographe": 2,
    "vocab_champ": 8, "vocab_propre": 8, "vocab_general": 60, "vocab_global": 12,
    "mots_domaine": 20, "p_mot_global": 0.0, "p_mot_champ": 0.5, "mots_generaux": 4, "zipf_general": 1.0,
    "ponderation_domaine": "tf",
    "q_min": 0.5, "q_max": 1.5, "p_etiquette_domaine_fausse": 0.05,
    "sans_pont": False, "etiquettes_absentes": False, "n_placebo": 6,
}


def eloignes(champ, a, b):
    return champ[a] != champ[b]


def proches(champ, a, b):
    return champ[a] == champ[b] and a != b


def _zipf(n, s):
    poids = [1.0 / (r + 1) ** s for r in range(n)]
    total = sum(poids)
    return [x / total for x in poids]


# --- Structure : champs, groupes d'opérateurs ------------------------------------------------------

def _champs(rng, p):
    k = p["n_domaines"]
    f = rng.choice(p["champs_choix"])
    ordre = list(range(k))
    rng.shuffle(ordre)
    tailles = [k // f + (1 if i < k % f else 0) for i in range(f)]
    champ, debut = [0] * k, 0
    for i, t in enumerate(tailles):
        for d in ordre[debut:debut + t]:
            champ[d] = i
        debut += t
    return f, champ


def _groupes(p, f, champ):
    """Groupe d'opérateurs de chaque domaine : son champ, ou son rang dans son champ (groupes transversaux)."""
    if p["groupes"] == "champs":
        return f, list(champ)
    rang, vus = [0] * p["n_domaines"], {}
    for d in range(p["n_domaines"]):
        rang[d] = vus.get(champ[d], 0)
        vus[champ[d]] = rang[d] + 1
    return max(vus.values()), rang


# --- Articles latents et ponts plantés ----------------------------------------------------------------

def _articles(rng, p, champ, groupe, n_groupes):
    ops_groupe = {g: [f"g{g}o{j}" for j in range(p["ops_par_groupe"])] for g in range(n_groupes)}
    arts, compteur = [], [0]

    def solo():
        compteur[0] += 1
        return f"s{compteur[0]}"

    for d in range(p["n_domaines"]):
        for _ in range(p["articles_par_domaine"]):
            prim = rng.choice(ops_groupe[groupe[d]]) if rng.random() < p["p_op_groupe"] else solo()
            ops = [prim]
            if rng.random() < p["p_secondaire"]:
                autres = [o for o in ops_groupe[groupe[d]] if o != prim]
                ops.append(rng.choice(autres) if (rng.random() < p["p_secondaire_groupe"] and autres) else solo())
            moyeux = [f"h{h}" for h in range(p["n_moyeux"]) if rng.random() < p["p_moyeu"]]
            c_vraies = [rng.choices("+-0", weights=p["p_axes"])[0] for _ in range(p["n_axes"])]
            arts.append({"dom": d, "champ": champ[d], "ops": ops, "moyeux": moyeux, "c_vraies": c_vraies,
                         "q": rng.uniform(p["q_min"], p["q_max"])})
    return arts, ops_groupe


def _compatibiliser(a, b):
    """Rend compatibles les contraintes vraies de a avec celles de b (un axe en conflit passe à 0 chez a)."""
    for x in range(len(a["c_vraies"])):
        if {a["c_vraies"][x], b["c_vraies"][x]} == {"+", "-"}:
            a["c_vraies"][x] = "0"


def _planter(rng, p, arts, champ, groupe, ops_groupe, placebo=False):
    """Greffes puis jumeaux. Avec placebo=True : même tirage des paires, sans partage d'opérateur (non utilisé
    pour la vérité ; gardé pour comparer le chemin de code)."""
    relation = eloignes if p["verite"] == "eloignes" else proches
    k, utilises, plantes = p["n_domaines"], set(), []
    for _ in range(p["n_greffes"]):
        for _essai in range(1000):
            a = rng.choice([i for i in range(len(arts)) if i not in utilises])
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
            _compatibiliser(arts[a], arts[b])
            utilises.update((a, b))
            plantes.append(["greffe", a, b, m])
            break
    for t in range(p["n_jumeaux"]):
        for _essai in range(1000):
            a = rng.choice([i for i in range(len(arts)) if i not in utilises])
            cands = [i for i in range(len(arts)) if i not in utilises and i != a
                     and relation(champ, arts[a]["dom"], arts[i]["dom"])]
            if not cands:
                continue
            b = rng.choice(cands)
            op = f"j{t}"
            arts[a]["ops"].append(op)
            arts[b]["ops"].append(op)
            _compatibiliser(arts[a], arts[b])
            utilises.update((a, b))
            plantes.append(["jumeau", a, b, op])
            break
    return plantes


# --- Observations : mots, lexique, étiquettes, contraintes, domaine ----------------------------------

def _observer_contraintes(rng, vraies, bruit, axe_homo):
    """Canal de l'essai b4 : paraphrase non détectée, mention du marqueur contraire, homographe « continue »."""
    p_para, p_ment, p_homo = bruit
    obs = []
    for v in vraies:
        if v == "0":
            obs.append("0")
            continue
        detecte = rng.random() >= p_para
        mention = rng.random() < p_ment
        opp = "-" if v == "+" else "+"
        obs.append("±" if (detecte and mention) else (v if detecte else (opp if mention else "0")))
    if rng.random() < p_homo:
        obs[axe_homo] = {"+": "±", "0": "-", "-": "-", "±": "±"}[obs[axe_homo]]
    return obs


def _observer(rng, p, arts, champ, groupe, n_groupes, ops_groupe):
    couverture, p_parasite, p_homonyme = NIVEAUX[p["niveau"]]
    k = p["n_domaines"]
    mot = {}  # (op, domaine, indice) -> mot de surface ; moyeux : (op, None, indice)

    def mots_de(op, d):
        cle_d = None if op.startswith("h") else d
        return [mot.setdefault((op, cle_d, i), f"w_{op}_{cle_d}_{i}") for i in range(2)]

    homonymes = {}  # mot -> opérateur canonique quand le mot est partagé (homonyme)
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
    lexique, zipf = {}, _zipf(p["vocab_general"], p["zipf_general"])

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
            cov = p["couverture_moyeu"] if o.startswith("h") else couverture
            lab = None if p["etiquettes_absentes"] else dans_lexique(w, canon, cov)
            if lab is None:
                sac.append(w)
            else:
                prov = "moyeu" if lab.startswith("h") else ("vrai" if lab in a["ops"] else "homonyme")
                if etiq.get(lab) != "vrai":
                    etiq[lab] = prov
        if not p["etiquettes_absentes"] and rng.random() < p_parasite:
            lab = rng.choice(labels_fond)
            if lab not in etiq:
                etiq[lab] = "vrai" if lab in a["ops"] else "parasite"
        for _ in range(p["mots_domaine"]):
            u = rng.random()
            if u < p["p_mot_global"]:
                sac.append(f"x{rng.randrange(p['vocab_global'])}")
            elif u < p["p_mot_global"] + p["p_mot_champ"]:
                sac.append(f"c{a['champ']}_{rng.randrange(p['vocab_champ'])}")
            else:
                sac.append(f"d{a['dom']}_{rng.randrange(p['vocab_propre'])}")
        sac += [f"z{x}" for x in rng.choices(range(p["vocab_general"]), weights=zipf, k=p["mots_generaux"])]
        a["sac_domaine"], a["etiquettes"] = sac, etiq
        a["c_obs"] = _observer_contraintes(rng, a["c_vraies"], p["bruit_contraintes"], p["axe_homographe"])
        if rng.random() < p["p_etiquette_domaine_fausse"]:
            voisins = [d for d in range(k) if champ[d] == a["champ"] and d != a["dom"]]
            a["dom_obs"] = rng.choice(voisins or [d for d in range(k) if d != a["dom"]])
        else:
            a["dom_obs"] = a["dom"]
    return sum(1 for v in homonymes), sum(1 for v in lexique.values() if v is not None)


def _cosinus(arts, ponderation):
    """Cosinus exacts des vecteurs de domaine sur les mots hors lexique (ce que voit le noyau). Pondération
    « tf » (fréquences brutes, comme le hachage par jeton de l'organisme) ou « tfidf »."""
    n = len(arts)
    df = Counter()
    for a in arts:
        df.update(set(a["sac_domaine"]))
    poids = (lambda w: 1.0) if ponderation == "tf" else (lambda w: math.log(n / df[w]))
    vecs = []
    for a in arts:
        v = {w: c * poids(w) for w, c in Counter(a["sac_domaine"]).items() if poids(w) > 0}
        norme = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs.append({w: x / norme for w, x in v.items()})
    cos = [[0.0] * n for _ in range(n)]
    for i in range(n):
        cos[i][i] = 1.0
        for j in range(i + 1, n):
            vi, vj = (vecs[i], vecs[j]) if len(vecs[i]) <= len(vecs[j]) else (vecs[j], vecs[i])
            cos[i][j] = cos[j][i] = sum(x * vj.get(w, 0.0) for w, x in vi.items())
    return cos


# --- Monde complet ---------------------------------------------------------------------------------------

def generer(params, graine):
    p = dict(BASE)
    p.update(params)
    rng = random.Random(graine)
    f, champ = _champs(rng, p)
    n_groupes, groupe = _groupes(p, f, champ)
    arts, ops_groupe = _articles(rng, p, champ, groupe, n_groupes)
    plantes = [] if p["sans_pont"] else _planter(rng, p, arts, champ, groupe, ops_groupe)
    ordre = list(range(len(arts)))
    rng.shuffle(ordre)  # ordre aléatoire des articles : aucun avantage d'indice (départages au premier indice)
    position = {ancien: nouveau for nouveau, ancien in enumerate(ordre)}
    arts = [arts[i] for i in ordre]
    plantes = [[t, position[a], position[b], m] for t, a, b, m in plantes]
    n_hom, n_lex = _observer(rng, p, arts, champ, groupe, n_groupes, ops_groupe)
    cos = _cosinus(arts, p["ponderation_domaine"])
    relation = eloignes if p["verite"] == "eloignes" else proches
    n, paires = len(arts), []
    for i in range(n):
        ai = arts[i]
        for j in range(i + 1, n):
            aj = arts[j]
            partage = sorted(set(ai["etiquettes"]) & set(aj["etiquettes"]))
            dom_diff = ai["dom_obs"] != aj["dom_obs"]
            compat_obs = not any({x, y} == {"+", "-"} for x, y in zip(ai["c_obs"], aj["c_obs"]))
            compat_vraie = not any({x, y} == {"+", "-"} for x, y in zip(ai["c_vraies"], aj["c_vraies"]))
            op_commun = sorted(set(ai["ops"]) & set(aj["ops"]))
            vrai = relation(champ, ai["dom"], aj["dom"]) and bool(op_commun) and compat_vraie
            valide = dom_diff and compat_obs and (p["etiquettes_absentes"] or bool(partage))
            paires.append({"i": i, "j": j, "partage": partage, "valide": valide, "vrai": vrai,
                           "mecanisme": ("jumeau" if any(o.startswith("j") for o in op_commun) else "greffe") if vrai else None,
                           "compat_vraie": compat_vraie, "op_commun": op_commun,
                           "proche": proches(champ, ai["dom"], aj["dom"]), "eloigne": eloignes(champ, ai["dom"], aj["dom"])})
    valides = [x for x in range(len(paires)) if paires[x]["valide"]]
    rng_placebo = random.Random(f"placebo-{graine}")
    placebo = set(rng_placebo.sample(valides, min(p["n_placebo"], len(valides))))
    return {"graine": graine, "params": p, "n": n, "n_champs": f, "champ": champ, "groupe": groupe,
            "arts": arts, "cos": cos, "paires": paires, "valides": valides, "placebo": placebo,
            "vrais": {x for x in range(len(paires)) if paires[x]["vrai"]}, "plantes": plantes,
            "n_homonymes": n_hom, "n_entrees_lexique": n_lex}
