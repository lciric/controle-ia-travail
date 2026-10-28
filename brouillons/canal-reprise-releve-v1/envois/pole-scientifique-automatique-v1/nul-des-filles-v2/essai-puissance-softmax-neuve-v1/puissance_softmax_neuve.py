"""Exploratoire : puissance du nul des filles v2 sur une fille « loi softmax neuve » (sans lien avec ses parents), selon
la dimension des traits et le nombre de tirages. Monde = la fille. Juge v1, calibrage 50, marge 2δ₀."""
import random, sys, json, time
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, sys.argv[1] + "/../orchestrateur-pole-v2")
import nul_filles_v2 as nf
from pole import selection_pari as sp
from pole.outils import graine_derivee

def essai(graine, r, variante, dim, n, force_fille):
    rng = random.Random(graine_derivee(graine, "softmax-neuve", dim, n, r))
    p1, p2 = sp.loi_softmax_aleatoire(rng, 3, dim), sp.loi_softmax_aleatoire(rng, 3, dim)
    fille = sp.loi_softmax_aleatoire(rng, 3, dim, force=force_fille)
    instances = sp.tirer_instances(rng, 50 + n, dim)
    parents = {"A": p1, "B": p2}
    biblio = sp.bibliotheque_fille(parents, dim, list(sp.BIBLIOTHEQUE_STANDARD_V1), nombre_issues=3) + nf.membres_de_variante(variante, parents)
    m = 8
    instants = sorted({max(1, round(n * (i + 1) / m)) for i in range(m)} | {n})
    gele = sp.geler_engagement(nf.construire_engagement_v2("f", fille, instances, 3, 0.05, biblio, 50, 0.01, instants))
    noyau = graine_derivee(graine, "noyau", dim, n, r)
    t = sp.tirer_frais(gele, fille, graine_derivee(graine, "frais", dim, n, r), graine_noyau=noyau)
    ev = nf.evaluer_v2(gele, t, graine_noyau=noyau)
    return ev["promue"], ev["membre_dominant_final"].split(":")[0]

sortie = {}
debut = time.monotonic()
for dim, n in ((2, 120), (2, 200), (2, 500), (4, 200), (8, 200)):
    for variante in ("v2", "v2_souple", "v1"):
        reps = 100
        res = [essai(5150, r, variante, dim, n, 1.5) for r in range(reps)]
        taux = sum(p for p, _ in res) / reps
        dom = {}
        for _, d in res:
            dom[d] = dom.get(d, 0) + 1
        sortie[f"dim{dim}-n{n}-{variante}"] = {"taux": taux, "dominants": dom}
        print(dim, n, variante, taux, dom, round(time.monotonic() - debut), flush=True)
json.dump(sortie, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
