"""Essais de la mémoire du pôle, piste 3 — un proposeur scripté qui lit la mémoire, contre sans mémoire et contre une
mémoire placebo — exploratoire (R-522), non opposable, lu dans les deux sens.

Mot de Lazar (27 octobre 2026, 12:02 heure de Paris) : pas de préenregistrement pour la partie exploratoire. Le plan, la
lecture et les prédictions sont écrits ici, avant le premier lancement, et poussés avec le script.

Monde (par course) : 400 associations sur une grille torique 20 × 20 (voisines : distance de Manhattan ≤ 2). Chaque
association a un contenu connu du proposeur (une direction W, matrice 3 × 2 de gaussiennes, et des biais) et une vérité
cachée : vraie (le monde suit softmax(s·W·x + b), force s inconnue) ou fausse (le monde est la marginale aveugle de
l'hypothèse testée). Deux types de monde, mêmes associations, mêmes vraies, mêmes forces ; seule la géographie change :
- « groupe » : 4 foyers ; une association à distance ≤ 2 d'un foyer est vraie avec probabilité 0,6, ailleurs 0,02 ; la
  force d'un foyer est tirée sur [0,3 ; 1,5], celle d'un membre en est proche (× [0,85 ; 1,15]) ;
- « permute » : la même vérité permutée au hasard entre les cases (aucune structure de voisinage).
Test : juge v1 (ordre secret, urne, 200 tirages frais). Registre de preuve du système avec héritage (piste 2), le même
pour tous les proposeurs : une association promue l'est une fois pour toutes ; retester une promue est une réplication.

Proposeurs (10 générations de 20 tests : même budget) :
- P0 « sans mémoire » : 20 associations au hasard, force supposée tirée sur [0,2 ; 2,0] ;
- P1a « mémoire, redites seulement » : ne repropose pas une association testée, sauf les éliminées prometteuses (log W
  cumulé > −2, moins de 3 essais), reproposées avec la force estimée sur leurs tirages (maximum de vraisemblance le long
  de la direction connue), au plus 6 par génération ; le reste au hasard parmi les non testées ;
- P1b « mémoire complète » : comme P1a, plus des marchepieds — les voisines non testées des promues (au plus 10 par
  génération, force supposée : celle estimée de la promue) — et une exploration loin de ce qui est déjà testé ;
- P2 « mémoire placebo » : la politique de P1b, lisant la mémoire de P1b dans une autre course (même type de monde, même
  génération) ; elle ne voit pas ses propres résultats (son registre de preuve, lui, est le vrai).

Mesures par course : vraies découvertes (associations vraies promues), fausses découvertes, tests sur des associations
déjà testées, tests sur des promues, blocs 5 × 5 contenant au moins une vraie découverte (diversité, 16 blocs), puissance
du premier essai sur les vraies, part des vraies du monde trouvées.

Lecture (différences appariées par course ; intervalle à 95 % par rééchantillonnage des courses) :
1. la mémoire améliore les propositions par son contenu si, monde groupé, P1b − P2 > 0 (intervalle entièrement positif) ;
2. la lecture structurée (marchepieds, exploration loin du déjà testé) apporte au-delà de l'évitement des redites si,
   monde groupé, P1b − P1a > 0 **et** si, monde permuté, cet avantage disparaît (intervalle de P1b − P1a qui contient 0
   ou est négatif) — sinon le gain ne vient pas de la structure et s'audite ;
3. le placebo n'apporte rien si l'intervalle de P2 − P0 contient 0 dans les deux mondes ; sinon une partie du gain tient
   à la forme de la politique ou à une information générique (forces typiques), et se rapporte ;
4. fausses découvertes : rapportées pour chaque proposeur (le registre avec héritage les borne) ;
5. trop beau (R4) : si P1b trouve plus de 95 % des vraies du monde groupé, le monde est trop facile : limite écrite.
Prédictions (confiance) : groupé, P1b − P2 ≥ + 5 vraies par course (0,8) et P1b − P1a ≥ + 3 (0,75) ; permuté,
|P1b − P1a| ≤ 1,5 (0,7) ; P2 − P0 dans [− 1,5 ; + 1,5] dans les deux mondes (0,7).

Graine maîtresse tirée par numpy.random.SeedSequence().entropy avant le premier lancement, passée en argument, écrite au
manifeste ; dérivation `graine_derivee` (SHA-256). Bibliothèque standard seule pour le calcul.

Usage : python -I -B essais_memoire_piste3_v1.py DOSSIER_SORTIE_NEUF --graine G [--courses N] [--essai]
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
from pole.outils import ecrire_json_scelle, graine_derivee, manifeste, sha256_fichier  # noqa: E402

K, DIM, COTE = 3, 2, 20
M = COTE * COTE
TIRAGES, ALPHA = 200, 0.05
SEUIL_LOG = math.log(1 / ALPHA)
GENERATIONS, PAR_GENERATION = 10, 20
FOYERS, RAYON, P_FOYER, P_AILLEURS = 4, 2, 0.6, 0.02
FORCE_MIN, FORCE_MAX = 0.3, 1.5
SUPPOSEE_MIN, SUPPOSEE_MAX = 0.2, 2.0
RETESTS_MAX, MARCHEPIEDS_MAX, ESSAIS_MAX, CUMUL_MIN_RETEST = 6, 10, 3, -2.0
PROPOSEURS = ("P0_sans_memoire", "P1a_memoire_redites", "P1b_memoire_complete", "P2_memoire_placebo")
MONDES = ("groupe", "permute")
COURSES_PAR_DEFAUT = 60


def _distance(a, b):
    (xa, ya), (xb, yb) = divmod(a, COTE), divmod(b, COTE)
    dx, dy = abs(xa - xb), abs(ya - yb)
    return min(dx, COTE - dx) + min(dy, COTE - dy)


DIST = [[_distance(a, b) for b in range(M)] for a in range(M)]
VOISINES = [sorted((b for b in range(M) if b != a and DIST[a][b] <= RAYON), key=lambda b: (DIST[a][b], b)) for a in range(M)]


def bloc(a):
    x, y = divmod(a, COTE)
    return (x // 5) * (COTE // 5) + (y // 5)


# --- monde -------------------------------------------------------------------------------------------------------------
def associations(graine, c):
    sortie = []
    for m in range(M):
        r = random.Random(graine_derivee(graine, "association", c, m))
        sortie.append({"W": [[r.gauss(0.0, 1.0) for _ in range(DIM)] for _ in range(K)],
                       "b": [r.gauss(0.0, 0.3) for _ in range(K)]})
    return sortie


def verite(graine, c):
    """{type de monde : (vraies, forces)} ; le monde permuté a les mêmes vraies et les mêmes forces, déplacées."""
    r = random.Random(graine_derivee(graine, "verite", c))
    foyers = [r.randrange(M) for _ in range(FOYERS)]
    forces_foyer = [r.uniform(FORCE_MIN, FORCE_MAX) for _ in range(FOYERS)]
    vraies, forces = [False] * M, [0.0] * M
    for m in range(M):
        proches = [i for i, f in enumerate(foyers) if DIST[m][f] <= RAYON]
        tirage = r.random()
        if proches:
            if tirage < P_FOYER:
                vraies[m], forces[m] = True, forces_foyer[proches[0]] * r.uniform(0.85, 1.15)
        elif tirage < P_AILLEURS:
            vraies[m], forces[m] = True, r.uniform(FORCE_MIN, FORCE_MAX)
    perm = list(range(M))
    random.Random(graine_derivee(graine, "permutation", c)).shuffle(perm)
    return {"groupe": (vraies, forces), "permute": ([vraies[perm[m]] for m in range(M)], [forces[perm[m]] for m in range(M)])}


def loi(assoc, s):
    return {"type": "softmax", "poids": [[s * w for w in ligne] for ligne in assoc["W"]], "biais": list(assoc["b"])}


def force_estimee(assoc, instances, issues):
    """Maximum de vraisemblance de s ∈ [0 ; 3] le long de la direction connue (Newton ; log-vraisemblance concave en s)."""
    a = [[sum(w * x for w, x in zip(ligne, inst["z"])) for ligne in assoc["W"]] for inst in instances]
    b, s = assoc["b"], 1.0
    for _ in range(40):
        d1 = d2 = 0.0
        for ai, y in zip(a, issues):
            sc = [s * v + bb for v, bb in zip(ai, b)]
            mx = max(sc)
            e = [math.exp(v - mx) for v in sc]
            z = sum(e)
            moy = sum(ek * v for ek, v in zip(e, ai)) / z
            var = sum(ek * v * v for ek, v in zip(e, ai)) / z - moy * moy
            d1 += ai[y] - moy
            d2 -= var
        if d2 > -1e-12:
            break
        nouveau = min(3.0, max(0.0, s - d1 / d2))
        fini = abs(nouveau - s) < 1e-6
        s = nouveau
        if fini:
            break
    return s


def tester(graine, c, monde, m, essai, s_supposee, assoc, vraie, force):
    """Un test du juge v1 ; graines partagées entre proposeurs par (course, monde, association, rang de l'essai)."""
    base = graine_derivee(graine, "test", c, monde, m, essai)
    instances = sp.tirer_instances(random.Random(graine_derivee(base, "instances")), TIRAGES, DIM)
    h = loi(assoc, s_supposee)
    monde_loi = loi(assoc, force) if vraie else {"type": "fixe", "probas": sp.moyenne_loi(h, instances)}
    gele = sp.geler_engagement(sp.construire_engagement("h", h, instances, K, ALPHA, sp.BIBLIOTHEQUE_STANDARD_V1, "continu",
                                                        plan_execution="ordre_secret"))
    noyau = graine_derivee(base, "noyau")
    tirages = sp.tirer_frais(gele, monde_loi, graine_derivee(base, "frais"), graine_noyau=noyau)
    ev = sp.evaluer(gele, tirages, graine_noyau=noyau)
    if ev.get("plan_execution") != "ordre_secret":
        raise RuntimeError("évaluation hors de l'ordre secret")
    return ev["log_richesse_max"], ev["log_richesse_finale"], instances, tirages["issues"]


# --- registre de preuve (système) et mémoire (lue par le proposeur) ------------------------------------------------------
def noter(registre, m, maximum, finale, s_estimee):
    """Héritage de la preuve : la retentative repart du log W cumulé de sa classe ; promue une fois pour toutes."""
    e = registre.setdefault(m, {"essais": 0, "cumul": 0.0, "promue": False, "s_estimee": None})
    nouvelle = (not e["promue"]) and e["cumul"] + maximum >= SEUIL_LOG
    e["promue"] = e["promue"] or nouvelle
    e["cumul"] += finale
    e["essais"] += 1
    if s_estimee is not None:
        e["s_estimee"] = s_estimee
    return nouvelle


def _borne(s):
    return min(SUPPOSEE_MAX, max(SUPPOSEE_MIN, s))


def proposer(politique, memoire, rng):
    """20 couples (association, force supposée), associations distinctes, d'après la mémoire lue (P1a, P1b, P2)."""
    if politique == "P0_sans_memoire":
        return [(m, rng.uniform(SUPPOSEE_MIN, SUPPOSEE_MAX)) for m in rng.sample(range(M), PAR_GENERATION)]
    choix, pris = [], set()

    def prendre(m, s):
        if m not in pris and len(choix) < PAR_GENERATION:
            choix.append((m, s))
            pris.add(m)

    retests = sorted((m for m, e in memoire.items() if not e["promue"] and e["cumul"] > CUMUL_MIN_RETEST
                      and e["essais"] < ESSAIS_MAX and e["s_estimee"] is not None), key=lambda m: (-memoire[m]["cumul"], m))
    for m in retests[:RETESTS_MAX]:
        prendre(m, _borne(memoire[m]["s_estimee"]))
    structuree = politique in ("P1b_memoire_complete", "P2_memoire_placebo")
    if structuree:
        promues = sorted((m for m, e in memoire.items() if e["promue"]), key=lambda m: (-memoire[m]["cumul"], m))
        n = 0
        for p in promues:
            s = _borne(memoire[p]["s_estimee"] if memoire[p]["s_estimee"] is not None else rng.uniform(SUPPOSEE_MIN, SUPPOSEE_MAX))
            for v in VOISINES[p]:
                if n >= MARCHEPIEDS_MAX:
                    break
                if v not in memoire and v not in pris:
                    prendre(v, s)
                    n += 1
            if n >= MARCHEPIEDS_MAX:
                break
    libres = [m for m in range(M) if m not in memoire and m not in pris]
    if not structuree:
        for m in rng.sample(libres, min(len(libres), PAR_GENERATION - len(choix))):
            prendre(m, rng.uniform(SUPPOSEE_MIN, SUPPOSEE_MAX))
        return choix
    # exploration loin du déjà testé (et du déjà choisi) : point le plus éloigné, égalités tirées au hasard
    connus = list(memoire) + list(pris)
    dmin = [min((DIST[m][t] for t in connus), default=COTE * 2) for m in range(M)]
    while len(choix) < PAR_GENERATION and libres:
        meilleur = max(dmin[m] for m in libres)
        m = rng.choice([x for x in libres if dmin[x] == meilleur])
        prendre(m, rng.uniform(SUPPOSEE_MIN, SUPPOSEE_MAX))
        libres.remove(m)
        for x in range(M):
            if DIST[x][m] < dmin[x]:
                dmin[x] = DIST[x][m]
    return choix


def une_course(graine, c, monde, assoc, vraies, forces, politique, memoires_partenaire=None):
    """Rend (mesures, instantanés de la mémoire au début de chaque génération)."""
    rng = random.Random(graine_derivee(graine, "proposeur", politique, c, monde))
    registre, instantanes = {}, []
    redites = sur_promues = 0
    premiers_vrais = premiers_vrais_promus = 0
    estimer = politique in ("P1a_memoire_redites", "P1b_memoire_complete")
    for g in range(GENERATIONS):
        instantanes.append({m: dict(e) for m, e in registre.items()})
        lue = registre if politique != "P2_memoire_placebo" else memoires_partenaire[g]
        for m, s in proposer(politique, lue, rng):
            avant = registre.get(m)
            essai = avant["essais"] if avant else 0
            redites += avant is not None
            sur_promues += bool(avant and avant["promue"])
            maximum, finale, instances, issues = tester(graine, c, monde, m, essai, s, assoc[m], vraies[m], forces[m])
            nouvelle = noter(registre, m, maximum, finale, force_estimee(assoc[m], instances, issues) if estimer else None)
            if essai == 0 and vraies[m]:
                premiers_vrais += 1
                premiers_vrais_promus += nouvelle
    promues = [m for m, e in registre.items() if e["promue"]]
    vraies_dec = [m for m in promues if vraies[m]]
    total_vraies = sum(vraies)
    return {"vraies": len(vraies_dec), "fausses": len(promues) - len(vraies_dec), "redites": redites,
            "tests_sur_promues": sur_promues, "blocs": len({bloc(m) for m in vraies_dec}),
            "puissance_premier_essai": premiers_vrais_promus / premiers_vrais if premiers_vrais else None,
            "part_des_vraies_trouvees": len(vraies_dec) / total_vraies if total_vraies else None,
            "vraies_du_monde": total_vraies, "associations_testees": len(registre)}, instantanes


def intervalle(diffs, graine, tirages=10000):
    rng = random.Random(graine)
    n = len(diffs)
    m = sorted(statistics.fmean(diffs[rng.randrange(n)] for _ in range(n)) for _ in range(tirages))
    return [m[int(0.025 * tirages)], m[int(0.975 * tirages) - 1]]


def executer(graine, courses):
    par = {monde: {p: [] for p in PROPOSEURS} for monde in MONDES}
    for monde in MONDES:
        memoires_p1b = []
        for c in range(courses):
            assoc = associations(graine, c)
            vraies, forces = verite(graine, c)[monde]
            for p in ("P0_sans_memoire", "P1a_memoire_redites", "P1b_memoire_complete"):
                mesure, inst = une_course(graine, c, monde, assoc, vraies, forces, p)
                par[monde][p].append(mesure)
                if p == "P1b_memoire_complete":
                    memoires_p1b.append(inst)
        for c in range(courses):
            assoc = associations(graine, c)
            vraies, forces = verite(graine, c)[monde]
            partenaire = memoires_p1b[(c + 1) % courses]
            mesure, _ = une_course(graine, c, monde, assoc, vraies, forces, "P2_memoire_placebo", partenaire)
            par[monde]["P2_memoire_placebo"].append(mesure)
    return par


def resumer(par, graine):
    champs = ("vraies", "fausses", "redites", "tests_sur_promues", "blocs", "puissance_premier_essai",
              "part_des_vraies_trouvees", "vraies_du_monde", "associations_testees")
    moyennes = {monde: {p: {ch: statistics.fmean(x[ch] for x in par[monde][p] if x[ch] is not None) for ch in champs}
                        for p in PROPOSEURS} for monde in MONDES}
    paires = {"P1b_moins_P2": ("P1b_memoire_complete", "P2_memoire_placebo"),
              "P1b_moins_P1a": ("P1b_memoire_complete", "P1a_memoire_redites"),
              "P1a_moins_P0": ("P1a_memoire_redites", "P0_sans_memoire"),
              "P2_moins_P0": ("P2_memoire_placebo", "P0_sans_memoire"),
              "P1b_moins_P0": ("P1b_memoire_complete", "P0_sans_memoire")}
    differences = {}
    for monde in MONDES:
        differences[monde] = {}
        for nom, (a, b) in paires.items():
            differences[monde][nom] = {}
            for ch in ("vraies", "fausses", "blocs"):
                d = [x[ch] - y[ch] for x, y in zip(par[monde][a], par[monde][b])]
                differences[monde][nom][ch] = {"moyenne": statistics.fmean(d),
                                               "intervalle_95": intervalle(d, graine_derivee(graine, "intervalle", monde, nom, ch))}
    def positif(i):
        return i[0] > 0
    def contient_zero_ou_negatif(i):
        return i[0] <= 0
    dg, dp = differences["groupe"], differences["permute"]
    lecture = {
        "1_contenu_de_la_memoire_P1b_sup_P2_groupe": positif(dg["P1b_moins_P2"]["vraies"]["intervalle_95"]),
        "2a_lecture_structuree_P1b_sup_P1a_groupe": positif(dg["P1b_moins_P1a"]["vraies"]["intervalle_95"]),
        "2b_avantage_disparait_en_monde_permute": contient_zero_ou_negatif(dp["P1b_moins_P1a"]["vraies"]["intervalle_95"]),
        "3_placebo_sans_apport_groupe": (dg["P2_moins_P0"]["vraies"]["intervalle_95"][0] <= 0
                                         <= dg["P2_moins_P0"]["vraies"]["intervalle_95"][1]),
        "3_placebo_sans_apport_permute": (dp["P2_moins_P0"]["vraies"]["intervalle_95"][0] <= 0
                                          <= dp["P2_moins_P0"]["vraies"]["intervalle_95"][1]),
        "5_trop_beau_P1b_plus_de_95_pour_cent_groupe": moyennes["groupe"]["P1b_memoire_complete"]["part_des_vraies_trouvees"] > 0.95,
    }
    predictions = {
        "groupe_P1b_moins_P2_au_moins_5": dg["P1b_moins_P2"]["vraies"]["moyenne"] >= 5,
        "groupe_P1b_moins_P1a_au_moins_3": dg["P1b_moins_P1a"]["vraies"]["moyenne"] >= 3,
        "permute_P1b_moins_P1a_au_plus_1_5_en_valeur_absolue": abs(dp["P1b_moins_P1a"]["vraies"]["moyenne"]) <= 1.5,
        "P2_moins_P0_dans_plus_ou_moins_1_5_les_deux_mondes": all(abs(differences[mo]["P2_moins_P0"]["vraies"]["moyenne"]) <= 1.5
                                                                 for mo in MONDES),
    }
    return {"moyennes_par_course": moyennes, "differences_appariees": differences, "lecture": lecture,
            "predictions_tenues": predictions}


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("--graine", type=int, required=True)
    a.add_argument("--courses", type=int, default=COURSES_PAR_DEFAUT)
    a.add_argument("--essai", action="store_true")
    args = a.parse_args()
    if os.path.exists(args.sortie) and os.listdir(args.sortie):
        sys.exit(f"dossier non vide : {args.sortie}")
    if not args.essai and args.courses != COURSES_PAR_DEFAUT:
        sys.exit(f"hors essai : {COURSES_PAR_DEFAUT} courses")
    p = {"graine": args.graine, "courses": args.courses, "essai": args.essai, "generations": GENERATIONS,
         "tests_par_generation": PAR_GENERATION, "tirages_par_test": TIRAGES, "alpha": ALPHA, "cote_grille": COTE,
         "foyers": FOYERS, "rayon": RAYON, "p_foyer": P_FOYER, "p_ailleurs": P_AILLEURS, "forces": [FORCE_MIN, FORCE_MAX],
         "forces_supposees": [SUPPOSEE_MIN, SUPPOSEE_MAX], "retests_max": RETESTS_MAX, "marchepieds_max": MARCHEPIEDS_MAX,
         "essais_max": ESSAIS_MAX, "cumul_min_retest": CUMUL_MIN_RETEST, "script_sha256": sha256_fichier(os.path.abspath(__file__))}
    quand = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    os.makedirs(args.sortie, exist_ok=True)
    ecrire_json_scelle(os.path.join(args.sortie, "manifeste.json"), dict(manifeste(**p), horodatage=quand))
    debut = time.monotonic()
    par = executer(args.graine, args.courses)
    r = {"parametres": p, "horodatage": quand, "resume": resumer(par, args.graine), "par_course": par}
    r["duree_s"] = round(time.monotonic() - debut, 1)
    nom = "resultats-memoire-piste3-v1" + ("-ESSAI" if args.essai else "")
    ecrire_json_scelle(os.path.join(args.sortie, nom + ".json"), r)
    print(json.dumps({"duree_s": r["duree_s"], "lecture": r["resume"]["lecture"]}, ensure_ascii=False))


if __name__ == "__main__":
    principal()
