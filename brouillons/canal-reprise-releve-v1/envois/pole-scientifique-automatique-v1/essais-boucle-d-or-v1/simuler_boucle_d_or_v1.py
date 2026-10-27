"""Essai « Boucle d'or » v1 — exploratoire (R-522), non opposable, lu dans les deux sens.

Plan fixé et poussé avant tout lancement : `plan-essai-boucle-d-or-v1.md` (empreinte dans son `.sha256`, commit `de4dbf6`).
L'allocateur à fenêtre de Gemini (similarité de domaine des parents dans [0,12 ; 0,26], entropie du verdict maximale)
contre trois allocateurs qui apprennent en ligne (hasard, Thompson, tri par espérance de découvertes par dollar), dans
cinq mondes ; chaque test est une évaluation du juge v1 de `../orchestrateur-pole-v2` (ordre secret, urne, nul augmenté
des parents, marge 2δ₀). Bibliothèque standard seule.

Usage (depuis n'importe où, Python sans `claude_agent_sdk` visible) :
    python -I -B simuler_boucle_d_or_v1.py DOSSIER_SORTIE_NEUF [--repetitions R] [--budget B] [--essai]
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
ORCHESTRATEUR = os.path.join(os.path.dirname(ICI), "orchestrateur-pole-v2")
sys.path.insert(0, ORCHESTRATEUR)

from pole import selection_pari as sp  # noqa: E402
from pole.controles_pari import _monde_fille, loi_tricheur  # noqa: E402
from pole.controles_pari_v1 import JUGES, _frequences, _geler, _membre_entrainement, _tirer_et_evaluer  # noqa: E402
from pole.outils import ecrire_json_scelle, ecrire_scelle, graine_derivee, manifeste, sha256_fichier  # noqa: E402

GRAINE = 20261027
N_RESERVOIR, BUDGET, REPETITIONS = 300, 40, 30
FENETRE = (0.12, 0.26)
LARGEUR_CASE_APPRISE, NB_CASES_APPRISES = 0.1, 8
LARGEUR_CASE_FENETRE, NB_CASES_FENETRE = 0.02, 7
TIRAGES, CALIBRAGE, DELTA0, ALPHA, K, DIM = 200, 50, 0.01, 0.05, 3, 2
MONDES = {
    "cloche": lambda s: 0.5 if FENETRE[0] <= s <= FENETRE[1] else 0.05,
    "bords": lambda s: 0.5 if (s < 0.06 or s > 0.6) else 0.05,
    "croissant": lambda s: 0.05 + 0.55 * s / 0.8,
    "decroissant": lambda s: 0.60 - 0.55 * s / 0.8,
    "plat": lambda s: 0.2,
}
ATTENDU = {"cloche": "gagner", "bords": "perdre", "croissant": "perdre", "decroissant": "perdre", "plat": "ne rien changer"}
ALLOCATEURS = ("hasard", "thompson", "tri", "fenetre")


class Reservoir:
    """Les filles candidates d'une répétition : similarité visible, vérité cachée, issue du juge v1 calculée une fois."""

    def __init__(self, monde, r):
        self.monde, self.r = monde, r
        rng = random.Random(graine_derivee(GRAINE, "reservoir", monde, r))
        self.s = [rng.uniform(0.0, 0.8) for _ in range(N_RESERVOIR)]
        self.vrai = [rng.random() < MONDES[monde](s) for s in self.s]
        self._issues = {}

    def tester(self, j):
        if j not in self._issues:
            self._issues[j] = self._evaluer(j)
        return self._issues[j]

    def _evaluer(self, j):
        rng = random.Random(graine_derivee(GRAINE, "candidat", self.monde, self.r, j))
        p1, p2 = (sp.loi_softmax_aleatoire(rng, K, DIM) for _ in range(2))
        instances = sp.tirer_instances(rng, CALIBRAGE + TIRAGES, DIM)
        if self.vrai[j]:
            p3 = sp.loi_softmax_aleatoire(rng, K, DIM, force=rng.uniform(0.3, 1.5))
            monde = {"type": "par_sous_population", "lois": {"0": p1, "1": p3}}
            fille = {"type": "si_sinon", "condition": {"sous_population": 0}, "si": p1, "sinon": p3}
        else:
            monde = _monde_fille(rng.choice(("parent_A_vrai", "parents_vrais_par_sous_population", "melange_des_parents")),
                                 p1, p2, instances)
            fille = None
        entrainement = sp.tirer_instances(rng, 100, DIM)
        q_ent = _frequences([sp.tirer_categorie(rng, sp.proba(monde, x, [], 0)) for x in entrainement], K)
        if fille is None:
            fille = loi_tricheur(rng.choice(("forme", "enveloppe_aveugle")), p1, p2, q_ent, rng)
        standard = list(JUGES["v1"]["bibliotheque"]) + [_membre_entrainement(q_ent)]
        biblio = sp.bibliotheque_fille({"A": p1, "B": p2}, DIM, standard, q_ent, nombre_issues=K)
        gele = _geler(fille, instances, K, ALPHA, "v1", biblio, CALIBRAGE, DELTA0, identifiant="fille")
        ev, _ = _tirer_et_evaluer(gele, monde, GRAINE, f"boucle|{self.monde}|{self.r}|{j}", 0)
        return bool(ev["promue"])


def _case_apprise(s):
    return min(NB_CASES_APPRISES - 1, int(s / LARGEUR_CASE_APPRISE))


def _case_fenetre(s):
    if not FENETRE[0] <= s <= FENETRE[1]:
        return None
    return min(NB_CASES_FENETRE - 1, int((s - FENETRE[0]) / LARGEUR_CASE_FENETRE))


def _entropie(p):
    return 0.0 if p <= 0 or p >= 1 else -(p * math.log(p) + (1 - p) * math.log(1 - p))


def allouer(nom, res, budget, rng):
    """Rend la liste des (candidate, promue) testées par l'allocateur `nom`, dans l'ordre."""
    restants = set(range(len(res.s)))
    succes, echecs = {}, {}
    sortie = []
    for _ in range(budget):
        if not restants:
            break
        if nom == "hasard":
            j = rng.choice(sorted(restants))
        else:
            case_de = _case_fenetre if nom == "fenetre" else _case_apprise
            par_case = {}
            for i in restants:
                c = case_de(res.s[i])
                if c is not None:
                    par_case.setdefault(c, []).append(i)
            if not par_case:  # fenêtre épuisée : hasard sur le reste (dit au rapport)
                j = rng.choice(sorted(restants))
            else:
                cases = sorted(par_case)
                rng.shuffle(cases)  # égalités tirées au hasard
                def a(c):
                    return 1 + succes.get(c, 0)

                def b(c):
                    return 1 + echecs.get(c, 0)
                if nom == "thompson":
                    scores = {c: rng.betavariate(a(c), b(c)) for c in cases}
                elif nom == "tri":
                    scores = {c: a(c) / (a(c) + b(c)) for c in cases}
                else:  # fenêtre : entropie maximale du verdict appris
                    scores = {c: _entropie(a(c) / (a(c) + b(c))) for c in cases}
                meilleure = max(cases, key=lambda c: scores[c])
                j = rng.choice(sorted(par_case[meilleure]))
        restants.discard(j)
        promue = res.tester(j)
        sortie.append((j, promue))
        if nom != "hasard":
            c = (_case_fenetre if nom == "fenetre" else _case_apprise)(res.s[j])
            if c is not None:
                (succes if promue else echecs)[c] = (succes if promue else echecs).get(c, 0) + 1
    return sortie


def intervalle_reechantillonne(diffs, graine, tirages=10000):
    rng = random.Random(graine)
    n = len(diffs)
    moyennes = sorted(statistics.fmean(diffs[rng.randrange(n)] for _ in range(n)) for _ in range(tirages))
    return moyennes[int(0.025 * tirages)], moyennes[int(0.975 * tirages) - 1]


def lire(intervalle):
    bas, haut = intervalle
    return "gagne" if bas > 0 else ("perd" if haut < 0 else "indistincte")


def executer(repetitions, budget):
    resultats = {}
    for monde in MONDES:
        lignes = {a: [] for a in ALLOCATEURS}
        evaluations = 0
        for r in range(repetitions):
            res = Reservoir(monde, r)
            for a in ALLOCATEURS:
                rng = random.Random(graine_derivee(GRAINE, "allocateur", a, monde, r))
                teste = allouer(a, res, budget, rng)
                vraies = sum(1 for j, p in teste if p and res.vrai[j])
                fausses = sum(1 for j, p in teste if p and not res.vrai[j])
                dans_fenetre = sum(1 for j, _ in teste if _case_fenetre(res.s[j]) is not None)
                lignes[a].append({"vraies_par_dollar": vraies / budget, "fausses_par_dollar": fausses / budget,
                                  "vraies_testees": sum(res.vrai[j] for j, _ in teste), "tests": len(teste),
                                  "tests_dans_la_fenetre": dans_fenetre})
            evaluations += len(res._issues)
        moyennes = {a: statistics.fmean(x["vraies_par_dollar"] for x in lignes[a]) for a in ALLOCATEURS}
        appris = max(("thompson", "tri"), key=lambda a: moyennes[a])
        d1 = [f["vraies_par_dollar"] - m["vraies_par_dollar"] for f, m in zip(lignes["fenetre"], lignes[appris])]
        d2 = [f["vraies_par_dollar"] - h["vraies_par_dollar"] for f, h in zip(lignes["fenetre"], lignes["hasard"])]
        d3 = [t["vraies_par_dollar"] - h["vraies_par_dollar"] for t, h in zip(lignes["thompson"], lignes["hasard"])]
        i1 = intervalle_reechantillonne(d1, graine_derivee(GRAINE, "intervalle", monde, "D1"))
        i2 = intervalle_reechantillonne(d2, graine_derivee(GRAINE, "intervalle", monde, "D2"))
        i3 = intervalle_reechantillonne(d3, graine_derivee(GRAINE, "intervalle", monde, "Thompson-hasard"))
        resultats[monde] = {
            "attendu_pour_la_fenetre": ATTENDU[monde],
            "moyennes_vraies_par_dollar": moyennes,
            "moyennes_fausses_par_dollar": {a: statistics.fmean(x["fausses_par_dollar"] for x in lignes[a])
                                            for a in ALLOCATEURS},
            "moyenne_tests_dans_la_fenetre": {a: statistics.fmean(x["tests_dans_la_fenetre"] for x in lignes[a])
                                              for a in ALLOCATEURS},
            "meilleur_appris": appris,
            "D1_fenetre_moins_meilleur_appris": {"moyenne": statistics.fmean(d1), "intervalle_95": i1, "lecture": lire(i1)},
            "D2_fenetre_moins_hasard": {"moyenne": statistics.fmean(d2), "intervalle_95": i2, "lecture": lire(i2)},
            "controle_Thompson_moins_hasard": {"moyenne": statistics.fmean(d3), "intervalle_95": i3, "lecture": lire(i3)},
            "evaluations_du_juge": evaluations,
            "par_repetition": lignes,
        }
    return resultats


def verdict(resultats):
    cloche = resultats["cloche"]["D1_fenetre_moins_meilleur_appris"]["lecture"]
    ailleurs = {m: resultats[m]["D1_fenetre_moins_meilleur_appris"]["lecture"] for m in MONDES if m != "cloche"}
    perd_ailleurs = [m for m, l in ailleurs.items() if l == "perd"]
    if cloche == "gagne" and not perd_ailleurs:
        return "à garder"
    if cloche == "gagne" and perd_ailleurs:
        return "à garder sous condition (seulement si l'on sait d'avance que la valeur suit la fenêtre)"
    if perd_ailleurs:
        return "à écarter"
    return "non tranché (la fenêtre ne gagne pas dans « cloche » et ne perd nulle part)"


def rapport(resultats, v, p, quand):
    l = [f"# Essai « Boucle d'or » v1 — verdict : {v}\n",
         f"Exploratoire, non opposable. {quand} (date -u). Graine {p['graine']} ; {p['repetitions']} répétitions par monde ; "
         f"budget {p['budget']} tests sur un réservoir de {N_RESERVOIR} ; juge v1 ; plan `{p['plan']}`.\n",
         "| monde | attendu | hasard | Thompson | tri | fenêtre | D1 (fenêtre − meilleur appris) | D2 (fenêtre − hasard) | Thompson − hasard |",
         "|---|---|---|---|---|---|---|---|---|"]
    for m, x in resultats.items():
        mo = x["moyennes_vraies_par_dollar"]
        fmt = lambda d: f"{d['moyenne']:+.3f} [{d['intervalle_95'][0]:+.3f} ; {d['intervalle_95'][1]:+.3f}] {d['lecture']}"
        l.append(f"| {m} | {x['attendu_pour_la_fenetre']} | {mo['hasard']:.3f} | {mo['thompson']:.3f} | {mo['tri']:.3f} | "
                 f"{mo['fenetre']:.3f} | {fmt(x['D1_fenetre_moins_meilleur_appris'])} | {fmt(x['D2_fenetre_moins_hasard'])} | "
                 f"{fmt(x['controle_Thompson_moins_hasard'])} |")
    l.append("\nDécouvertes vraies par dollar (moyennes sur les répétitions). Promotions fausses par dollar, par monde et "
             "allocateur : " + "; ".join(f"{m} " + ", ".join(f"{a} {v_:.3f}" for a, v_ in x["moyennes_fausses_par_dollar"].items())
                                       for m, x in resultats.items()) + ".")
    return "\n".join(l) + "\n"


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("--repetitions", type=int, default=REPETITIONS)
    a.add_argument("--budget", type=int, default=BUDGET)
    a.add_argument("--essai", action="store_true", help="essai de fumée : marqué non conforme au plan")
    args = a.parse_args()
    if os.path.exists(args.sortie) and os.listdir(args.sortie):
        sys.exit(f"dossier non vide : {args.sortie}")
    conforme = args.repetitions == REPETITIONS and args.budget == BUDGET and not args.essai
    plan = os.path.join(ICI, "plan-essai-boucle-d-or-v1.md")
    p = {"graine": GRAINE, "repetitions": args.repetitions, "budget": args.budget, "conforme_au_plan": conforme,
         "plan": "plan-essai-boucle-d-or-v1.md", "plan_sha256": sha256_fichier(plan),
         "script_sha256": sha256_fichier(os.path.abspath(__file__))}
    quand = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    os.makedirs(args.sortie, exist_ok=True)
    ecrire_json_scelle(os.path.join(args.sortie, "manifeste.json"), dict(manifeste(**p), horodatage=quand))
    debut = time.monotonic()
    resultats = executer(args.repetitions, args.budget)
    v = verdict(resultats)
    nom = "resultats-boucle-d-or-v1" + ("" if conforme else "-ESSAI")
    ecrire_json_scelle(os.path.join(args.sortie, nom + ".json"),
                       {"parametres": p, "verdict": v, "resultats": resultats, "horodatage": quand,
                        "duree_s": round(time.monotonic() - debut, 1)})
    ecrire_scelle(os.path.join(args.sortie, nom + ".md"), rapport(resultats, v, p, quand))
    print(json.dumps({"verdict": v, "conforme_au_plan": conforme, "duree_s": round(time.monotonic() - debut, 1)},
                     ensure_ascii=False))


if __name__ == "__main__":
    principal()
