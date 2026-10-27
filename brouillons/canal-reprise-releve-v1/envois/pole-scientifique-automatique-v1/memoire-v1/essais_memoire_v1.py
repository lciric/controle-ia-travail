"""Essais de la mémoire du pôle, pistes 1 et 2 — exploratoire (R-522), non opposable, lu dans les deux sens.

Plan fixé et poussé avant tout lancement : `plan-essais-memoire-v1.md` (empreinte dans son `.sha256`, commit `8edfaf7`).
Piste 1 : détecteurs de redite (texte, signature brute, signature invariante) à taux de fausses fusions égal.
Piste 2 : rien, refus ou héritage de la preuve, avec retentatives, sous le juge v1 de `../orchestrateur-pole-v2`.
Bibliothèque standard seule.

Usage : python -I -B essais_memoire_v1.py DOSSIER_SORTIE_NEUF [--piste 1|2|toutes] [--courses N] [--essai]
"""

import argparse
import json
import math
import os
import random
import statistics
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "orchestrateur-pole-v2"))

from pole import selection_pari as sp  # noqa: E402
from pole.controles_pari import _dirichlet, borne_wilson  # noqa: E402
from pole.memoire import jaccard  # noqa: E402
from pole.outils import ecrire_json_scelle, ecrire_scelle, graine_derivee, manifeste, sha256_fichier  # noqa: E402

GRAINE = 20261028
K, DIM = 3, 2
NOMS_ISSUES = ("rouge", "vert", "bleu")
NOMS_TRAITS = ("la taille", "l'âge")


# --- piste 1 : textes et transformations ---------------------------------------------------------------------------
def texte_de(loi, noms=NOMS_TRAITS, style="courant", jargon=(), suffixe=""):
    """Texte d'une fiche tiré de la structure de sa loi softmax (gabarit fixe)."""
    poids, biais = loi["poids"], loi["biais"]
    verbe, effet, domine = (("augmente", "devient plus probable", "domine") if style == "courant"
                            else ("croît", "gagne en probabilité", "l'emporte"))
    clauses = []
    for d, nom in enumerate(noms):
        k = max(range(K), key=lambda i: poids[i][d])
        clauses.append(f"quand {nom} {verbe}, l'issue {NOMS_ISSUES[k]} {effet}")
    if style == "paraphrase":
        clauses.reverse()
    phrase = "Hypothèse : " + " ; ".join(clauses) + f" ; dans l'ensemble, l'issue {NOMS_ISSUES[max(range(K), key=lambda i: biais[i])]} {domine}."
    if jargon:
        phrase += " Cadre : " + ", ".join(jargon) + "."
    return phrase + suffixe


JARGON = ("hyperfibration de Kodaira-Spencer tronquée", "cohomologie étale relative", "faisceau pervers de Beilinson",
          "tour d'Iwasawa cyclotomique", "champ de modules de Deligne-Mumford")


def transformer(famille, loi, rng):
    """Rend (loi transformée, texte transformé) pour une famille de vraies redites ou de différences."""
    if famille == "paraphrase":
        return dict(loi), texte_de(loi, style="paraphrase")
    if famille == "copie_renommee":
        return dict(loi), texte_de(loi, noms=("la variable alpha", "le facteur bêta"))
    if famille == "jargon_rare":
        return dict(loi), texte_de(loi, jargon=JARGON)
    if famille == "changement_d_echelle":
        f = [round(0.5 + 2 * rng.random(), 3) for _ in range(DIM)]
        interne = {"type": "softmax", "poids": [[w * fj for w, fj in zip(l, f)] for l in loi["poids"]], "biais": list(loi["biais"])}
        return ({"type": "echelle", "facteurs": f, "loi": interne},
                texte_de(loi, noms=tuple(f"{n} exprimée dans une autre unité (× {fj})" for n, fj in zip(NOMS_TRAITS, f))))
    if famille == "melange_aveugle":
        lam = rng.uniform(0.2, 0.6)
        return ({"type": "melange", "composantes": [loi, {"type": "fixe", "probas": _dirichlet(rng, K, 1.0)}],
                 "poids": [1 - lam, lam]}, texte_de(loi, suffixe=" Corrigée par les taux de base observés."))
    if famille == "biais_par_issue":
        biais = [b + rng.gauss(0.0, 0.7) for b in loi["biais"]]
        nouvelle = {"type": "softmax", "poids": [list(l) for l in loi["poids"]], "biais": biais}
        return nouvelle, texte_de(nouvelle)
    if famille == "variante_quantitative":
        nouvelle = {"type": "softmax", "poids": [[2 * w for w in l] for l in loi["poids"]], "biais": [2 * b for b in loi["biais"]]}
        return nouvelle, texte_de(nouvelle, suffixe=" L'effet est fort.")
    if famille == "vraie_difference":
        nouvelle = sp.loi_softmax_aleatoire(rng, K, DIM, force=1.5)
        return nouvelle, texte_de(nouvelle)
    raise ValueError(famille)


REDITES = ("paraphrase", "copie_renommee", "jargon_rare", "changement_d_echelle", "melange_aveugle", "biais_par_issue")


def _rangs(v):
    ordre = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.0] * len(v)
    for rang, i in enumerate(ordre):
        r[i] = float(rang)
    return r


def _spearman(a, b):
    ra, rb = _rangs(a), _rangs(b)
    return statistics.correlation(ra, rb)


def signature(loi, sonde):
    return [sp.proba(loi, x, [], 0) for x in sonde]


def score_brut(sa, sb):
    """Divergence de Kullback-Leibler moyenne sur la sonde (petite = redite)."""
    return statistics.fmean(sp.divergence(p, q) for p, q in zip(sa, sb))


def score_invariant(sa, sb):
    """Corrélation de rang moyenne des log-cotes de chaque paire d'issues sur la sonde (grande = redite)."""
    valeurs = []
    for k in range(K):
        for j in range(k + 1, K):
            a = [math.log(p[k] / p[j]) for p in sa]
            b = [math.log(q[k] / q[j]) for q in sb]
            valeurs.append(_spearman(a, b))
    return statistics.fmean(valeurs)


def piste1():
    rng = random.Random(graine_derivee(GRAINE, "piste1"))
    sonde = sp.tirer_instances(random.Random(graine_derivee(GRAINE, "sonde")), 256, DIM)
    bases = [sp.loi_softmax_aleatoire(rng, K, DIM, force=1.5) for _ in range(400)]
    moitie = list(range(400))
    random.Random(graine_derivee(GRAINE, "coupe")).shuffle(moitie)
    etalonnage, mesure = set(moitie[:200]), set(moitie[200:])
    familles = REDITES + ("vraie_difference", "variante_quantitative")
    scores = {f: [] for f in familles}
    for i, base in enumerate(bases):
        sb = signature(base, sonde)
        tb = texte_de(base)
        for f in familles:
            r = random.Random(graine_derivee(GRAINE, "transformation", f, i))
            loi, texte = transformer(f, base, r)
            st = signature(loi, sonde)
            scores[f].append({"i": i, "texte": jaccard(tb, texte), "brut": score_brut(sb, st), "invariant": score_invariant(sb, st)})
    # seuils : 5 % de fausses fusions sur les vraies différences de la moitié d'étalonnage
    diffs = [s for s in scores["vraie_difference"] if s["i"] in etalonnage]
    def quantile(v, q):
        v = sorted(v)
        return v[min(len(v) - 1, int(q * len(v)))]
    seuils = {"texte": quantile([s["texte"] for s in diffs], 0.95),        # redite si ≥ seuil (strictement au-dessus)
              "brut": quantile([s["brut"] for s in diffs], 0.05),          # redite si ≤ seuil
              "invariant": quantile([s["invariant"] for s in diffs], 0.95)}
    def est_redite(det, s):
        return s[det] <= seuils[det] if det == "brut" else s[det] > seuils[det]
    sortie = {"seuils": seuils, "par_famille": {}}
    for f in familles:
        lignes = [s for s in scores[f] if s["i"] in mesure]
        sortie["par_famille"][f] = {}
        for det in ("texte", "brut", "invariant"):
            fusions = sum(est_redite(det, s) for s in lignes)
            n = len(lignes)
            if f in REDITES:
                manquees = n - fusions
                sortie["par_famille"][f][det] = {"manquees": manquees, "n": n, "taux_manquees": manquees / n,
                                                 "wilson_haut": borne_wilson(manquees, n),
                                                 "wilson_bas": 1 - borne_wilson(n - manquees, n)}
            else:
                sortie["par_famille"][f][det] = {"fusionnees": fusions, "n": n, "taux_fusion": fusions / n,
                                                 "wilson_haut": borne_wilson(fusions, n)}
    return sortie


# --- piste 2 : rien, refus, héritage --------------------------------------------------------------------------------
SEUIL_LOG = math.log(20)


def _evaluer(loi, monde, graine_essai, instances):
    gele = sp.geler_engagement(sp.construire_engagement("h", loi, instances, K, 0.05, sp.BIBLIOTHEQUE_STANDARD_V1, "continu",
                                                        plan_execution="ordre_secret"))
    noyau = graine_derivee(graine_essai, "noyau")
    ev = sp.evaluer(gele, sp.tirer_frais(gele, monde, graine_derivee(graine_essai, "frais"), graine_noyau=noyau),
                    graine_noyau=noyau)
    return ev["log_richesse_max"], ev["log_richesse_finale"]


def une_course(c, facteur_premier=0.3):
    rng = random.Random(graine_derivee(GRAINE, "course", c))
    classes = []
    for h in range(40):
        r = random.Random(graine_derivee(GRAINE, "course", c, "classe", h))
        loi = sp.loi_softmax_aleatoire(r, K, DIM, force=1.5)
        instances = sp.tirer_instances(r, 200, DIM)
        vraie = r.random() < 0.10
        monde = loi if vraie else {"type": "fixe", "probas": sp.moyenne_loi(loi, instances)}
        tentatives = []
        for a in range(4):
            if vraie:
                facteur = facteur_premier if a == 0 else 1.0
                t = {"type": "softmax", "poids": [[facteur * w for w in l] for l in loi["poids"]],
                     "biais": [facteur * b for b in loi["biais"]]}
            elif a == 0:
                t = loi
            else:
                t, _ = transformer(r.choice(("melange_aveugle", "biais_par_issue")), loi, r)
            tentatives.append(t)
        reprises = [r.random() < 0.5 for _ in range(3)]  # une décision par génération, la même pour toutes les politiques
        classes.append({"vraie": vraie, "monde": monde, "instances": instances, "tentatives": tentatives, "reprises": reprises})
    cache = {}

    def essai(h, a):
        if (h, a) not in cache:
            cl = classes[h]
            cache[(h, a)] = _evaluer(cl["tentatives"][a], cl["monde"], graine_derivee(GRAINE, "course", c, h, a), cl["instances"])
        return cache[(h, a)]

    resultats = {}
    for politique in ("rien", "refus", "heritage"):
        vraies = fausses = tests = 0
        for h, cl in enumerate(classes):
            cumul, promue, a = 0.0, False, 0
            maximum, finale = essai(h, 0)
            tests += 1
            promue = maximum >= SEUIL_LOG
            cumul = finale
            for g in range(3):
                if promue or politique == "refus" or not cl["reprises"][g]:
                    continue
                a += 1
                maximum, finale = essai(h, a)
                tests += 1
                depart = cumul if politique == "heritage" else 0.0
                promue = depart + maximum >= SEUIL_LOG
                cumul = depart + finale if politique == "heritage" else finale
            vraies += promue and cl["vraie"]
            fausses += promue and not cl["vraie"]
        resultats[politique] = {"vraies": vraies, "fausses": fausses, "tests": tests}
    resultats["classes_vraies"] = sum(cl["vraie"] for cl in classes)
    return resultats


def intervalle(diffs, graine, tirages=10000):
    rng = random.Random(graine)
    n = len(diffs)
    m = sorted(statistics.fmean(diffs[rng.randrange(n)] for _ in range(n)) for _ in range(tirages))
    return m[int(0.025 * tirages)], m[int(0.975 * tirages) - 1]


def piste2(courses, facteur_premier=0.3):
    par_course = [une_course(c, facteur_premier) for c in range(courses)]
    sortie = {"courses": courses, "facteur_premier": facteur_premier, "par_politique": {}}
    for p in ("rien", "refus", "heritage"):
        sortie["par_politique"][p] = {m: statistics.fmean(x[p][m] for x in par_course) for m in ("vraies", "fausses", "tests")}
    for nom, (a, b, m) in {"fausses_heritage_moins_refus": ("heritage", "refus", "fausses"),
                           "vraies_heritage_moins_refus": ("heritage", "refus", "vraies"),
                           "fausses_rien_moins_refus": ("rien", "refus", "fausses"),
                           "vraies_rien_moins_heritage": ("rien", "heritage", "vraies")}.items():
        d = [x[a][m] - x[b][m] for x in par_course]
        sortie[nom] = {"moyenne": statistics.fmean(d), "intervalle_95": intervalle(d, graine_derivee(GRAINE, "intervalle", nom))}
    sortie["classes_vraies_par_course"] = statistics.fmean(x["classes_vraies"] for x in par_course)
    return sortie


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("--piste", choices=("1", "2", "toutes"), default="toutes")
    a.add_argument("--courses", type=int, default=200)
    a.add_argument("--essai", action="store_true")
    a.add_argument("--facteur-premier", type=float, default=0.3,
                   help="piste 2 : facteur des logits de la première tentative d'une vraie (plan : 0,3 ; variante B déclarée après l'essai de fumée : 3,0, trop sûre d'elle)")
    args = a.parse_args()
    if os.path.exists(args.sortie) and os.listdir(args.sortie):
        sys.exit(f"dossier non vide : {args.sortie}")
    conforme = args.courses == 200 and args.piste == "toutes" and not args.essai and args.facteur_premier == 0.3
    p = {"graine": GRAINE, "piste": args.piste, "courses": args.courses, "conforme_au_plan": conforme,
         "facteur_premier": args.facteur_premier,
         "plan_sha256": sha256_fichier(os.path.join(ICI, "plan-essais-memoire-v1.md")),
         "script_sha256": sha256_fichier(os.path.abspath(__file__))}
    quand = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    os.makedirs(args.sortie, exist_ok=True)
    ecrire_json_scelle(os.path.join(args.sortie, "manifeste.json"), dict(manifeste(**p), horodatage=quand))
    debut = time.monotonic()
    r = {"parametres": p, "horodatage": quand}
    if args.piste in ("1", "toutes"):
        r["piste1"] = piste1()
    if args.piste in ("2", "toutes"):
        r["piste2"] = piste2(args.courses, args.facteur_premier)
    r["duree_s"] = round(time.monotonic() - debut, 1)
    nom = "resultats-memoire-v1" + ("" if conforme else ("-variante-B" if args.facteur_premier == 3.0 and not args.essai and args.courses == 200 else "-ESSAI"))
    ecrire_json_scelle(os.path.join(args.sortie, nom + ".json"), r)
    print(json.dumps({"duree_s": r["duree_s"], "conforme_au_plan": conforme}, ensure_ascii=False))


if __name__ == "__main__":
    principal()
