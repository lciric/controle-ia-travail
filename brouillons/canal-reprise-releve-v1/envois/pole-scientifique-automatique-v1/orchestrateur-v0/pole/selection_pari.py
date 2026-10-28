"""Sélection par pari (tests par pari, e-processus) — l'évaluateur est du code de l'orchestrateur, hors des agents.

Une fiche engage une loi prédictive p_h sur K issues. Le nul est composite : une bibliothèque 𝓛 de prédicteurs aveugles
au domaine (ils ne voient que l'historique des issues, jamais les traits des instances). La richesse est

    W_t = Π_{s≤t} p_h(x_s) / max_{q∈𝓛} Π_{s≤t} q(x_s),

calculée sur des tirages frais, tirés après l'engagement (leur graine dérive de l'empreinte de l'engagement).

Choix documenté (inférence universelle) : le dénominateur est le **maximum de vraisemblance a posteriori sur 𝓛, ajusté
sur les tirages frais eux-mêmes** (pour la marginale : les fréquences des tirages ; pour les moyennes glissantes : la
meilleure fenêtre). La loi p_h, écrite avant les tirages, tient lieu de numérateur ajusté sur une part séparée. Validité :
si les issues suivent une loi q* de 𝓛, alors W_t ≤ Π p_h/Π q* à tout t, martingale positive d'espérance 1 sous q* ;
l'inégalité de Ville donne P(sup_t W_t ≥ 1/α) ≤ α : la promotion peut être lue à tout instant (« continu »).
Les deux autres ajustements (sur une part séparée d'entraînement, ou en ligne) sont gardés comme variantes à éprouver :
le contrôle T6 montre qu'ils laissent passer un parasite de Kelly.
"""

import collections
import copy
import math
import random

from .outils import empreinte_objet, graine_derivee, nombre_fini

PLANCHER = 1e-12
BIBLIOTHEQUE_STANDARD = (
    {"nom": "marginale_empirique", "type": "marginale_mv"},
    {"nom": "uniforme", "type": "uniforme"},
    {"nom": "moyenne_glissante", "type": "moyennes_glissantes", "fenetres": [5, 10, 20, 50], "lissage": 0.5},
)
TYPES_LOI = ("fixe", "softmax", "par_sous_population", "melange", "si_sinon", "moyenne_glissante", "derive_lineaire",
             "echelle", "enveloppe")


class LoiInvalide(ValueError):
    pass


class EngagementModifie(RuntimeError):
    """Le test (loi, bibliothèque, seuil, plan) a changé après son gel : évaluation refusée."""


class TiragesNonLies(RuntimeError):
    """Les tirages ne sont pas liés à cet engagement (tirés avant, ou pour un autre test) : évaluation refusée."""


# --- lois prédictives -----------------------------------------------------------------------------------------
def _normaliser(p):
    p = [max(PLANCHER, float(x)) for x in p]
    s = sum(p)
    return [x / s for x in p]


def _condition(condition, instance):
    if "sous_population" in condition:
        return instance.get("g") == condition["sous_population"]
    return instance["z"][condition["indice"]] > condition.get("seuil", 0.0)


def proba(loi, instance, historique, t):
    """Loi prédictive de l'issue t (indice à partir de 0), sachant l'instance et les issues historique[:t]."""
    genre = loi["type"]
    if genre == "fixe":
        return _normaliser(loi["probas"])
    if genre == "softmax":
        z = instance["z"]
        scores = [b + sum(w * x for w, x in zip(ligne, z)) for ligne, b in zip(loi["poids"], loi["biais"])]
        m = max(scores)
        return _normaliser([math.exp(s - m) for s in scores])
    if genre == "par_sous_population":
        sous_loi = loi["lois"].get(str(instance.get("g")), loi.get("defaut"))
        return proba(sous_loi, instance, historique, t)
    if genre == "melange":
        mix = [0.0] * len(proba(loi["composantes"][0], instance, historique, t))
        for poids, composante in zip(loi["poids"], loi["composantes"]):
            for k, p in enumerate(proba(composante, instance, historique, t)):
                mix[k] += poids * p
        return _normaliser(mix)
    if genre == "si_sinon":
        branche = loi["si"] if _condition(loi["condition"], instance) else loi["sinon"]
        return proba(branche, instance, historique, t)
    if genre == "moyenne_glissante":
        k, w, lam = loi["nombre_issues"], loi["fenetre"], loi["lissage"]
        recents = historique[max(0, t - w):t]
        compte = collections.Counter(recents)
        return _normaliser([(compte[i] + lam) / (len(recents) + k * lam) for i in range(k)])
    if genre == "enveloppe":
        tables = [proba(l, instance, historique, t) for l in loi["lois"]]
        return _normaliser([max(table[k] for table in tables) for k in range(len(tables[0]))])
    if genre == "echelle":
        reechelonnee = dict(instance, z=[x / f for x, f in zip(instance["z"], loi["facteurs"])])
        return proba(loi["loi"], reechelonnee, historique, t)
    if genre == "derive_lineaire":
        s = min(1.0, t / max(1, loi["horizon"] - 1))
        return _normaliser([(1 - s) * a + s * b for a, b in zip(loi["debut"], loi["fin"])])
    raise LoiInvalide(f"type de loi inconnu : {genre!r}")


def valider_loi(loi, nombre_issues, dimension=None):
    """Lève LoiInvalide si la spécification n'est pas une loi bien formée sur `nombre_issues` issues."""
    if not isinstance(loi, dict) or loi.get("type") not in TYPES_LOI:
        raise LoiInvalide(f"loi : objet avec un type parmi {TYPES_LOI}")
    genre = loi["type"]
    if genre == "fixe":
        p = loi.get("probas")
        if not isinstance(p, list) or len(p) != nombre_issues or not all(nombre_fini(x) and x >= 0 for x in p) or sum(p) <= 0:
            raise LoiInvalide("loi fixe : probas positives, une par issue")
    elif genre == "softmax":
        poids, biais = loi.get("poids"), loi.get("biais")
        if not isinstance(poids, list) or len(poids) != nombre_issues or not isinstance(biais, list) or len(biais) != nombre_issues:
            raise LoiInvalide("softmax : une ligne de poids et un biais par issue")
        largeurs = {len(l) if isinstance(l, list) else -1 for l in poids}
        if len(largeurs) != 1 or (dimension is not None and largeurs != {dimension}) or not all(
                nombre_fini(x) for l in poids for x in l) or not all(nombre_fini(b) for b in biais):
            raise LoiInvalide("softmax : poids et biais finis, de largeur égale à la dimension des instances")
    elif genre == "par_sous_population":
        if not isinstance(loi.get("lois"), dict) or not loi["lois"]:
            raise LoiInvalide("par_sous_population : objet « lois » non vide")
        for sous in list(loi["lois"].values()) + ([loi["defaut"]] if "defaut" in loi else []):
            valider_loi(sous, nombre_issues, dimension)
    elif genre == "melange":
        comp, poids = loi.get("composantes"), loi.get("poids")
        if not isinstance(comp, list) or not comp or not isinstance(poids, list) or len(poids) != len(comp) \
                or not all(nombre_fini(w) and w >= 0 for w in poids) or abs(sum(poids) - 1) > 1e-9:
            raise LoiInvalide("mélange : composantes et poids positifs de somme 1")
        for c in comp:
            valider_loi(c, nombre_issues, dimension)
    elif genre == "si_sinon":
        cond = loi.get("condition")
        if not isinstance(cond, dict) or not ("sous_population" in cond or "indice" in cond):
            raise LoiInvalide("si_sinon : condition sur la sous-population ou sur un trait")
        valider_loi(loi.get("si"), nombre_issues, dimension)
        valider_loi(loi.get("sinon"), nombre_issues, dimension)
    elif genre == "moyenne_glissante":
        if loi.get("nombre_issues") != nombre_issues or not isinstance(loi.get("fenetre"), int) or loi["fenetre"] < 1:
            raise LoiInvalide("moyenne_glissante : nombre_issues et fenêtre entière ≥ 1")
    elif genre == "enveloppe":
        if not isinstance(loi.get("lois"), list) or len(loi["lois"]) < 2:
            raise LoiInvalide("enveloppe : au moins deux lois")
        for l in loi["lois"]:
            valider_loi(l, nombre_issues, dimension)
    elif genre == "echelle":
        f = loi.get("facteurs")
        if not isinstance(f, list) or not all(nombre_fini(x) and x > 0 for x in f) or (dimension is not None and len(f) != dimension):
            raise LoiInvalide("echelle : un facteur strictement positif par trait")
        valider_loi(loi.get("loi"), nombre_issues, dimension)
    elif genre == "derive_lineaire":
        for cle in ("debut", "fin"):
            if not isinstance(loi.get(cle), list) or len(loi[cle]) != nombre_issues:
                raise LoiInvalide("derive_lineaire : debut et fin, une probabilité par issue")
        if not isinstance(loi.get("horizon"), int) or loi["horizon"] < 1:
            raise LoiInvalide("derive_lineaire : horizon entier ≥ 1")
    return loi


def tirer_categorie(rng, p):
    u, cumul = rng.random(), 0.0
    for k, pk in enumerate(p):
        cumul += pk
        if u < cumul:
            return k
    return len(p) - 1


def tirer_instances(rng, nombre, dimension=2, sous_populations=2):
    return [{"z": [round(rng.gauss(0.0, 1.0), 6) for _ in range(dimension)], "g": rng.randrange(sous_populations)}
            for _ in range(nombre)]


def loi_softmax_aleatoire(rng, nombre_issues=3, dimension=2, force=1.5):
    return {"type": "softmax",
            "poids": [[round(rng.gauss(0.0, force), 6) for _ in range(dimension)] for _ in range(nombre_issues)],
            "biais": [round(rng.gauss(0.0, 0.3), 6) for _ in range(nombre_issues)]}


def moyenne_loi(loi, instances):
    """Marginale moyenne de p_h sur des instances : le nul le plus trompeur (mêmes fréquences, aucun lien aux traits)."""
    total = None
    for t, inst in enumerate(instances):
        p = proba(loi, inst, [], t)
        total = p if total is None else [a + b for a, b in zip(total, p)]
    return [round(x / len(instances), 9) for x in total]


def divergence(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


# --- bibliothèque 𝓛 : trajectoires de log-vraisemblance (maximum a posteriori sur chaque famille) ------------------
def _traj_marginale_mv(issues, k):
    compte, sortie = [0] * k, []
    for t, x in enumerate(issues, 1):
        compte[x] += 1
        sortie.append(sum(c * math.log(c / t) for c in compte if c))
    return sortie


def _traj_cumulee(logs):
    cumul, sortie = 0.0, []
    for v in logs:
        cumul += v
        sortie.append(cumul)
    return sortie


def _traj_moyennes_glissantes(issues, k, fenetres, lissage):
    meilleure = None
    for w in fenetres:
        compte, file, cumul, sortie = [0] * k, collections.deque(), 0.0, []
        for x in issues:
            cumul += math.log((compte[x] + lissage) / (len(file) + k * lissage))
            sortie.append(cumul)
            file.append(x)
            compte[x] += 1
            if len(file) > w:
                compte[file.popleft()] -= 1
        meilleure = sortie if meilleure is None else [max(a, b) for a, b in zip(meilleure, sortie)]
    return meilleure


def _traj_marginale_en_ligne(issues, k, lissage):
    compte, logs = [0] * k, []
    for t, x in enumerate(issues):
        logs.append(math.log((compte[x] + lissage) / (t + k * lissage)))
        compte[x] += 1
    return _traj_cumulee(logs)


class Cache:
    """Probabilités par pas de chaque loi (calculées une fois par évaluation)."""

    def __init__(self, issues, instances):
        self.issues, self.instances, self._lois = issues, instances, {}

    def probas(self, loi):
        cle = empreinte_objet(loi)
        if cle not in self._lois:
            self._lois[cle] = [proba(loi, self.instances[t], self.issues, t) for t in range(len(self.issues))]
        return self._lois[cle]


def trajectoire_loi(loi, issues, instances, cache=None):
    cache = cache or Cache(issues, instances)
    return _traj_cumulee([math.log(p[x]) for p, x in zip(cache.probas(loi), issues)])


def _traj_melange(membre, issues, cache):
    pa, pb = (cache.probas(l) for l in membre["lois"])
    meilleure = None
    for w in sorted(set(membre["grille"])):
        traj = _traj_cumulee([math.log(max(PLANCHER, w * a[x] + (1 - w) * b[x])) for a, b, x in zip(pa, pb, issues)])
        meilleure = traj if meilleure is None else [max(u, v) for u, v in zip(meilleure, traj)]
    return meilleure


def _traj_enveloppe(membre, issues, cache):
    tables = [cache.probas(l) for l in membre["lois"]]
    logs = []
    for t, x in enumerate(issues):
        m = [max(table[t][k] for table in tables) for k in range(len(tables[0][t]))]
        logs.append(math.log(m[x] / sum(m)))
    return _traj_cumulee(logs)


def trajectoire_membre(membre, issues, instances, k, cache=None):
    genre = membre["type"]
    cache = cache or Cache(issues, instances)
    if genre == "marginale_mv":
        return _traj_marginale_mv(issues, k)
    if genre == "uniforme":
        return [-t * math.log(k) for t in range(1, len(issues) + 1)]
    if genre == "moyennes_glissantes":
        return _traj_moyennes_glissantes(issues, k, membre["fenetres"], membre.get("lissage", 0.5))
    if genre == "marginale_en_ligne":
        return _traj_marginale_en_ligne(issues, k, membre.get("lissage", 0.5))
    if genre == "fixe":
        p = _normaliser(membre["probas"])
        return _traj_cumulee([math.log(p[x]) for x in issues])
    if genre == "loi":
        return trajectoire_loi(membre["loi"], issues, instances, cache)
    if genre == "melange_lois":
        return _traj_melange(membre, issues, cache)
    if genre == "enveloppe_harmonique":
        return _traj_enveloppe(membre, issues, cache)
    raise LoiInvalide(f"membre de bibliothèque inconnu : {genre!r}")


def trajectoires(bibliotheque, issues, instances, k, cache=None):
    cache = cache or Cache(issues, instances)
    return {m["nom"]: trajectoire_membre(m, issues, instances, k, cache) for m in bibliotheque}


def trajectoire_denominateur(bibliotheque, issues, instances, k, cache=None, deja=None):
    par_membre = deja or trajectoires(bibliotheque, issues, instances, k, cache)
    meilleure, dominant = None, None
    for nom, traj in par_membre.items():
        if meilleure is None:
            meilleure, dominant = list(traj), [nom] * len(traj)
            continue
        for t, v in enumerate(traj):
            if v > meilleure[t]:
                meilleure[t], dominant[t] = v, nom
    return meilleure, dominant


# --- engagement, gel, tirages frais, évaluation ------------------------------------------------------------------
def construire_engagement(identifiant, loi, instances, nombre_issues=3, alpha=0.05, bibliotheque=BIBLIOTHEQUE_STANDARD,
                          mode="continu", empreinte_fiche=None, part_calibrage=0, delta0=None):
    if not (nombre_fini(alpha) and 0 < alpha < 1):
        raise ValueError("alpha dans ]0 ; 1[")
    if mode not in ("continu", "horizon"):
        raise ValueError("mode : « continu » (lecture à tout instant, Ville) ou « horizon »")
    if not instances or not (isinstance(part_calibrage, int) and 0 <= part_calibrage < len(instances)):
        raise ValueError("plan d'instances vide, ou part de calibrage hors du plan")
    if delta0 is not None and not (nombre_fini(delta0) and delta0 >= 0):
        raise ValueError("delta0 : nombre fini positif ou nul")
    noms = [m["nom"] for m in bibliotheque]
    if len(set(noms)) != len(noms):
        raise ValueError("noms de membres de bibliothèque en double")
    dimension = len(instances[0]["z"])
    valider_loi(loi, nombre_issues, dimension)
    for membre in bibliotheque:
        for l in ([membre["loi"]] if membre.get("type") == "loi" else membre.get("lois", [])):
            valider_loi(l, nombre_issues, dimension)
    return {"identifiant": identifiant, "loi": copy.deepcopy(loi), "bibliotheque": copy.deepcopy(list(bibliotheque)),
            "alpha": alpha, "seuil_richesse": 1.0 / alpha, "instances": copy.deepcopy(instances),
            "nombre_issues": nombre_issues, "mode": mode, "empreinte_fiche": empreinte_fiche,
            "part_calibrage": part_calibrage, "delta0": delta0}


class EngagementGele:
    def __init__(self, engagement):
        self.engagement = copy.deepcopy(engagement)
        self.empreinte = empreinte_objet(self.engagement)


def geler_engagement(engagement):
    return EngagementGele(engagement)


def tirer_frais(gele, loi_monde, graine):
    """Tirages frais, liés à l'engagement : leur graine dérive de son empreinte, ils n'existent pas avant le gel."""
    rng = random.Random(graine_derivee(graine, "tirages-frais", gele.empreinte))
    issues = []
    for t, instance in enumerate(gele.engagement["instances"]):
        issues.append(tirer_categorie(rng, proba(loi_monde, instance, issues, t)))
    return {"empreinte_engagement": gele.empreinte, "issues": issues}


def calibrer(bibliotheque, issues, instances):
    """Poids des mélanges marqués « calibrer » ajusté sur la part de calibrage, ajouté à leur grille."""
    sortie = []
    for membre in bibliotheque:
        membre = copy.deepcopy(membre)
        if membre.get("type") == "melange_lois" and membre.get("calibrer") and issues:
            cache = Cache(issues, instances)
            pa, pb = (cache.probas(l) for l in membre["lois"])
            meilleur = max(sorted(set(membre["grille"])), key=lambda w: sum(
                math.log(max(PLANCHER, w * a[x] + (1 - w) * b[x])) for a, b, x in zip(pa, pb, issues)))
            membre["poids_calibre"] = meilleur
            membre["grille"] = sorted(set(membre["grille"]) | {meilleur})
        sortie.append(membre)
    return sortie


def evaluer(gele, tirages):
    """Richesse et promotion, calculées par l'orchestrateur à partir du test gelé et de tirages liés.

    Fille (bibliothèque avec enveloppes et `delta0`) : promotion si W ≥ 1/α **et** si le gain moyen de score
    logarithmique sur la part d'évaluation dépasse celui de la meilleure enveloppe d'au moins 2·delta0.
    """
    if empreinte_objet(gele.engagement) != gele.empreinte:
        raise EngagementModifie("le test a changé depuis son gel")
    if not isinstance(tirages, dict) or tirages.get("empreinte_engagement") != gele.empreinte:
        raise TiragesNonLies("tirages sans lien avec l'empreinte de cet engagement")
    e = gele.engagement
    k, instances, issues = e["nombre_issues"], e["instances"], tirages.get("issues")
    if not isinstance(issues, list) or len(issues) != len(instances) or not all(
            isinstance(x, int) and not isinstance(x, bool) and 0 <= x < k for x in issues):
        raise TiragesNonLies("issues absentes, mal formées ou en nombre différent du plan gelé")
    c = e.get("part_calibrage", 0)
    bibliotheque = calibrer(e["bibliotheque"], issues[:c], instances[:c])
    issues, instances = issues[c:], instances[c:]
    cache = Cache(issues, instances)
    numerateur = trajectoire_loi(e["loi"], issues, instances, cache)
    par_membre = trajectoires(bibliotheque, issues, instances, k, cache)
    denominateur, dominant = trajectoire_denominateur(bibliotheque, issues, instances, k, deja=par_membre)
    log_w = [a - b for a, b in zip(numerateur, denominateur)]
    seuil = math.log(1.0 / e["alpha"])
    t_promotion = next((t + 1 for t, v in enumerate(log_w) if v >= seuil), None)
    promue = t_promotion is not None if e["mode"] == "continu" else log_w[-1] >= seuil
    resultat = {"log_richesse_finale": log_w[-1], "log_richesse_max": max(log_w), "seuil_log": seuil,
                "t_promotion": t_promotion, "nombre_tirages": len(issues), "part_calibrage": c,
                "membre_dominant_final": dominant[-1], "mode": e["mode"], "empreinte_engagement": gele.empreinte}
    enveloppes = [m["nom"] for m in bibliotheque if m.get("enveloppe")]
    if e.get("delta0") is not None and enveloppes:
        meilleure = max(enveloppes, key=lambda n: par_membre[n][-1])
        gain = (numerateur[-1] - par_membre[meilleure][-1]) / len(issues)
        resultat.update(meilleure_enveloppe=meilleure, gain_moyen_sur_meilleure_enveloppe=gain,
                        marge_requise=2 * e["delta0"], marge_atteinte=gain >= 2 * e["delta0"])
        promue = promue and gain >= 2 * e["delta0"]
    resultat["promue"] = promue
    if not promue:
        resultat["t_promotion"] = None
    return resultat


# --- sélecteur mécanique ex ante (bras 1) et nul augmenté des filles ---------------------------------------------
def selection_divergence(loi, candidats, q_reference, nombre):
    """Les `nombre` instances où p_h s'écarte le plus (divergence de Kullback-Leibler) de la référence aveugle."""
    scores = [(divergence(proba(loi, c, [], 0), q_reference), i) for i, c in enumerate(candidats)]
    scores.sort(key=lambda s: (-s[0], s[1]))
    return [candidats[i] for _, i in scores[:nombre]]


GRILLE_MELANGE = [round(i / 20, 2) for i in range(21)]


def bibliotheque_fille(lois_parents, dimension, bibliotheque=BIBLIOTHEQUE_STANDARD, marginale_entrainement=None,
                       grille=GRILLE_MELANGE, nombre_issues=3):
    """Nul composite d'une fille : 𝓛, augmentée de ses parents et de leurs enveloppes (membres marqués « enveloppe »).

    Chaque parent seul ; le mélange des parents (poids : maximum a posteriori sur la grille, plus le poids ajusté sur la
    part de calibrage) ; l'enveloppe harmonique (en chaque issue le meilleur des parents, renormalisée) ; les
    concaténations si/sinon sur les partitions déclarées (sous-population, signe de chaque trait) ; chaque parent mélangé
    à une loi aveugle (uniforme, et marginale d'entraînement si fournie). Une fille qui n'est qu'une de ces formes est
    dans son propre nul : sa richesse reste ≤ 1.
    """
    membres = list(copy.deepcopy(bibliotheque))
    noms = sorted(lois_parents)
    for nom in noms:
        membres.append({"nom": f"parent:{nom}", "type": "loi", "loi": lois_parents[nom], "enveloppe": True})
        aveugles = [("uniforme", {"type": "fixe", "probas": [1.0] * nombre_issues})]
        if marginale_entrainement is not None:
            aveugles.append(("marginale_entrainement", {"type": "fixe", "probas": list(marginale_entrainement)}))
        for nom_a, aveugle in aveugles:
            membres.append({"nom": f"parent_couvert:{nom}|{nom_a}", "type": "melange_lois", "lois": [lois_parents[nom], aveugle],
                            "grille": list(grille), "enveloppe": True})
    if len(noms) == 2:
        la, lb = lois_parents[noms[0]], lois_parents[noms[1]]
        membres.append({"nom": "melange_parents", "type": "melange_lois", "lois": [la, lb], "grille": list(grille),
                        "calibrer": True, "enveloppe": True})
        membres.append({"nom": "enveloppe_harmonique", "type": "enveloppe_harmonique", "lois": [la, lb], "enveloppe": True})
        conditions = [{"sous_population": 0}] + [{"indice": j, "seuil": 0.0} for j in range(dimension)]
        for c in conditions:
            for (n1, l1), (n2, l2) in (((noms[0], la), (noms[1], lb)), ((noms[1], lb), (noms[0], la))):
                membres.append({"nom": f"si_sinon:{n1}|{n2}|{empreinte_objet(c)[:8]}", "type": "loi", "enveloppe": True,
                                "loi": {"type": "si_sinon", "condition": c, "si": l1, "sinon": l2}})
    return membres
