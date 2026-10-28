"""Le pari apparié borné de bout en bout (v7, version 27) — zéro dépense, aucun agent : une **banque de scores**
synthétique (unités à effet aléatoire partagé entre sabotés et honnêtes d'une même unité ; sept cellules : `blanc`,
`blanc_jumeau` (même loi que `blanc`), `cascade` (ii), `dernier_etat` (iii), `noir_action`, `noir_sequentiel`, `juge`),
un **proposeur mécanique** de contrastes (témoins plantés vrais à quatre forces, faux « nul exact » et « signe inversé »,
contrastes tirés au hasard à vérité connue, et une fiche « G1 » en intersection-union contre les cinq comparateurs avec
garde), des **engagements** scellés sur le seul calibrage, une **Course** sous D-S25 bis : une tranche d'épreuve
**fraîche** par génération (identifiants d'unités, intersection refusée), budgets D-S24 (α / G_max par génération,
α_c / m_c par fiche, gardé à vie), abandons sous contrat (après partie, avant partie), déclaration « sans partie »
confrontée au **journal des parties** (K8-2), **lignées de clé** (D-S25 bis (5) : une affirmation, une fiche), et la
lecture L1 / L2 / L3 fixée ici, avant la course :

- **L1** validité : aucune fiche d'espérance ≤ 0 promue (témoins faux et contrastes au hasard de signe connu) ;
- **L2** dents : quelles forces de témoin vrai sont promues, et à quelle génération ;
- **L3** la fiche « G1 » : promue ou non, richesse finale par comparateur, garde ; ce qu'elle dit si elle échoue (quel
  comparateur a cédé — nœud 1 (b) : chaque composante rapportée).

`--nul R` : la même course, R fois, sur des banques **nulles** (toutes les cellules de même loi) : part des répétitions
avec au moins une promotion, à comparer à α (garantie de D-S25 bis sur l'union des promotions) ; deux artefacts (R5) :
relecture d'une tranche (refusée par la course) et « sans partie » mensonger (refusé par le journal).

Usage : python -I -B demonstrations/demo_pari_apparie_v7.py DOSSIER_NEUF [--generations 4] [--unites-par-tranche 40]
        [--graine 20261028] [--alpha 0.05] [--nul 200]
"""

import argparse
import math
import os
import random
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)

from pole import engagement_apparie as ea  # noqa: E402
from pole import monde_banque_scores as mbs  # noqa: E402
from pole import pari_apparie as pa  # noqa: E402
from pole.outils import ecrire_json_scelle, graine_derivee  # noqa: E402

CELLULES = ("blanc", "blanc_jumeau", "cascade", "dernier_etat", "noir_action", "noir_sequentiel", "juge")
# décalage de la loi des sabotés par cellule (honnêtes : 0 partout) ; `blanc_jumeau` = `blanc` (nul exact)
DECALAGES = {"blanc": 1.5, "blanc_jumeau": 1.5, "cascade": 1.0, "dernier_etat": 0.9, "noir_action": 0.5,
             "noir_sequentiel": 0.7, "juge": 0.3}
COMPARATEURS_G1 = ("cascade", "dernier_etat", "noir_action", "noir_sequentiel", "juge")
MODES = ("diffus", "concentre")


def banque(rng, tranches, unites_par_tranche, calibrage=60, developpement=0, sabotes=8, honnetes=8, sigma_unite=0.6,
           nul=False):
    """Épisodes avec un effet d'unité partagé (les instances d'une unité ne sont pas indépendantes, D-S1) ; les unités
    d'épreuve portent leur tranche dans `strates["tranche"]` ; la tranche 1 ne contient que le mode « diffus » (pour
    exercer la déclaration « sans partie » d'une fiche stratifiée « concentré »)."""
    dec = {c: (0.0 if nul else d) for c, d in DECALAGES.items()}
    episodes = []

    def ajouter(partie, unite, mode, tranche, avec_sabotes):
        eta = rng.gauss(0, sigma_unite)
        for etiquette, nombre in (("sabote", sabotes if avec_sabotes else 0), ("honnete", honnetes)):
            for k in range(nombre):
                scores = {c: eta + (dec[c] if etiquette == "sabote" else 0.0) + rng.gauss(0, 1) for c in CELLULES}
                episodes.append({"id": f"{unite}-{etiquette}-{k}", "unite": unite, "etiquette": etiquette, "partie": partie,
                                 "strates": {"mode": mode, "tranche": str(tranche)}, "scores": scores})

    for u in range(calibrage):
        ajouter("calibrage", f"cal-{u}", MODES[u % 2], 0, False)
    for u in range(developpement):
        ajouter("developpement", f"dev-{u}", MODES[u % 2], 0, True)
    for t in range(1, tranches + 1):
        for u in range(unites_par_tranche):
            mode = "diffus" if t == 1 else MODES[u % 2]
            ajouter("epreuve", f"epr-{t}-{u}", mode, t, True)
    return {"cellules": list(CELLULES), "strates": ["mode", "tranche"], "episodes": episodes}


def esperance_connue(coefficients, constante=0.0):
    """Signe connu du contraste sur les parts : le décalage ordonne les parts (même bruit, même seuil τ) ; un contraste
    Σ a_c · part_c + a₀ a une espérance de même signe que Σ a_c · décalage_c quand a₀ = 0 — vrai ici par construction
    (cellules de même variance, seuils de même τ)."""
    return sum(a * DECALAGES[c] for c, a in coefficients.items()) + constante


def propositions(rng, generation, n_hasard):
    """Les fiches de la génération : témoins plantés en génération 1, contrastes au hasard ensuite (vérité connue)."""
    fiches = {}
    if generation == 1:
        fiches["temoin-vrai-fort"] = {"coefficients": {"blanc": 1, "juge": -1}}          # écart 1,2
        fiches["temoin-vrai-moyen"] = {"coefficients": {"blanc": 1, "noir_action": -1}}   # écart 1,0
        fiches["temoin-vrai-faible"] = {"coefficients": {"blanc": 1, "cascade": -1}}      # écart 0,5
        fiches["temoin-vrai-tenu"] = {"coefficients": {"cascade": 1, "dernier_etat": -1}}  # écart 0,1
        fiches["temoin-faux-nul"] = {"coefficients": {"blanc": 1, "blanc_jumeau": -1}}    # nul exact
        fiches["temoin-faux-inverse"] = {"coefficients": {"juge": 1, "blanc": -1}}        # signe inversé
        fiches["temoin-vrai-concentre"] = {"coefficients": {"blanc": 1, "noir_sequentiel": -1}, "strate": {"mode": "concentre"}}
    for k in range(n_hasard):
        a, b = rng.sample(CELLULES, 2)
        fiches[f"hasard-g{generation}-{k}"] = {"coefficients": {a: 1, b: -1}}
    return fiches


def fiche_g1():
    return {"coefficients_par_comparateur": {c: {"blanc": 1, c: -1} for c in COMPARATEURS_G1},
            "garde": {"a": "blanc", "b": "noir_action", "delta": 0.10}}


def unites_de_tranche(monde, t):
    return sorted({e["unite"] for e in monde.episodes("epreuve", None, {"tranche": str(t)})})


def construire_engagement(monde, nom, fiche, tau, alpha_c, m_c, partie="epreuve"):
    if "coefficients_par_comparateur" in fiche:
        contrastes = {c: {"coefficients": k} for c, k in fiche["coefficients_par_comparateur"].items()}
        return ea.construire(monde, contrastes, tau, alpha_c=alpha_c, m_c=m_c, partie=partie, garde=fiche.get("garde"))
    return ea.construire(monde, {nom: {"coefficients": fiche["coefficients"]}}, tau, alpha_c=alpha_c, m_c=m_c,
                         partie=partie, strate=fiche.get("strate"))


def course(monde, generations, alpha, tau, graine, n_hasard=6, avec_g1=True, seuil_abandon_log=-1.0):
    """La course entière ; renvoie le journal (par génération) et l'état final. D-S24 : α_g = α / G_max."""
    rng = random.Random(graine_derivee(graine, "proposeur"))
    c = pa.Course(alpha=alpha)
    lignees = ea.Lignees()
    engagements, verites, journal = {}, {}, []
    alpha_g = alpha / generations
    for g in range(1, generations + 1):
        tranche = unites_de_tranche(monde, g)
        nouvelles = propositions(rng, g, n_hasard)
        if g == 1 and avec_g1:
            nouvelles["G1"] = fiche_g1()
        m_c = len(nouvelles)
        for nom, fiche in nouvelles.items():
            engagements[nom] = construire_engagement(monde, nom, fiche, tau, alpha_g, m_c)
            lignees.entrer(nom, engagements[nom])
            if "coefficients_par_comparateur" in fiche:
                verites[nom] = min(esperance_connue(k) for k in fiche["coefficients_par_comparateur"].values())
            else:
                verites[nom] = esperance_connue(fiche["coefficients"])
        c.entrer(f"g{g}", list(nouvelles), alpha_g)
        # abandon « avant partie » : en génération 2, le proposeur retire le témoin inversé sans regarder son issue
        # (mode `avant_partie` du contrat de D-S25 bis (2) ; sa valeur gelée est celle d'après la partie de la génération 1)
        sans_partie, parties, abandons = {}, {}, []
        for nom in list(c.budgets):
            if nom in c.gelees or nom in c.promues or nom in c.arretees or nom in c.exclues:
                continue
            if g == 2 and nom == "temoin-faux-inverse":
                c.abandonner(nom, avant_partie=True, motif="retrait du proposeur avant toute issue de la génération")
                abandons.append((nom, "avant_partie"))
                continue
            r = ea.evaluer(monde, engagements[nom], unites=tranche, etiquette_ordre=f"{engagements[nom]['empreinte']}|g{g}")
            if r["unites"] == 0:
                sans_partie[nom] = f"aucune unité de la tranche {g} dans la strate de la fiche"
                continue
            lignees.journaliser(g, nom, r)
            parties[nom] = r
            valeur = c.ajouter_trajectoire(nom, r["trajectoire_log_min"], unites=r["identifiants_unites"])
            # la règle d'abandon du proposeur ne porte que sur ses contrastes au hasard : les témoins et la fiche G1
            # sont lus jusqu'au bout (ce sont eux qu'on lit en L2 et L3)
            if nom.startswith("hasard-") and valeur < seuil_abandon_log and nom not in c.arretees:
                c.abandonner(nom, motif=f"log-richesse {valeur:.2f} < {seuil_abandon_log} après la partie")
                abandons.append((nom, "apres_partie"))
        lignees.verifier_sans_partie(g, sans_partie)
        promues = c.lire(sans_partie=sans_partie)
        journal.append({"generation": g, "tranche_unites": len(tranche), "nouvelles": sorted(nouvelles), "alpha_g": alpha_g,
                        "m_c": m_c, "parties": {n: {"unites": r["unites"], "log_e_valeur": c.log_e[n],
                                                   "log_richesse_finale_par_comparateur": r["log_richesse_finale_par_comparateur"],
                                                   "log_garde_finale": r["log_garde_finale"]} for n, r in parties.items()},
                        "sans_partie": sans_partie, "abandons": abandons, "promues": sorted(promues)})
    return {"journal": journal, "promues": sorted(c.promues), "bonferroni": sorted(c.bonferroni()), "verites": verites,
            "log_e": dict(c.log_e), "seuils_log": {f: c.seuil_log(f) for f in c.budgets}, "gelees": sorted(c.gelees),
            "abandons": {str(k): v for k, v in c.abandons.items()}, "sans_partie": {str(k): v for k, v in c.sans_partie.items()},
            "journal_parties": lignees.journal, "alpha_engage": c.alpha_engage}


def lecture(etat):
    promues, verites = etat["promues"], etat["verites"]
    fausses = sorted(f for f in promues if verites[f] <= 1e-12)
    temoins_vrais = {f: v for f, v in verites.items() if f.startswith("temoin-vrai")}
    par_generation = {f: g["generation"] for g in etat["journal"] for f in g["promues"]}
    g1 = {}
    if "G1" in verites:
        derniere = next((g["parties"]["G1"] for g in reversed(etat["journal"]) if "G1" in g["parties"]), None)
        g1 = {"promue": "G1" in promues, "generation": par_generation.get("G1"), "log_e_final": etat["log_e"]["G1"],
              "seuil_log": etat["seuils_log"]["G1"],
              "derniere_partie": derniere,
              "comparateur_le_plus_faible": (min(derniere["log_richesse_finale_par_comparateur"],
                                                 key=derniere["log_richesse_finale_par_comparateur"].get) if derniere else None)}
    return {"L1_validite": {"tenue": not fausses, "promues_d_esperance_nulle_ou_negative": fausses},
            "L2_dents": {f: {"esperance_connue": v, "promue": f in promues, "generation": par_generation.get(f),
                             "log_e_final": etat["log_e"][f]} for f, v in sorted(temoins_vrais.items())},
            "L3_G1": g1, "promues": promues, "bonferroni": etat["bonferroni"]}


def artefacts(monde, alpha, tau, graine):
    """R5 : chaque garde sur un cas sain (ci-dessus) et sur un artefact — ici deux refus attendus."""
    sortie = {}
    e = construire_engagement(monde, "x", {"coefficients": {"blanc": 1, "juge": -1}}, tau, alpha, 1)
    tranche = unites_de_tranche(monde, 1)
    r = ea.evaluer(monde, e, unites=tranche)
    c = pa.Course(alpha=alpha)
    c.entrer("a", ["x"], alpha)
    c.ajouter_trajectoire("x", r["trajectoire_log_min"], unites=r["identifiants_unites"])
    c.lire()
    try:
        c.ajouter_trajectoire("x", r["trajectoire_log_min"], unites=r["identifiants_unites"])
        sortie["relecture_tranche"] = "ACCEPTÉE — artefact non détecté"
    except ValueError as err:
        sortie["relecture_tranche"] = f"refusée : {err}"
    lg = ea.Lignees()
    lg.entrer("x", e)
    lg.journaliser(1, "x", r)
    try:
        lg.verifier_sans_partie(1, {"x": "prétendue absence"})
        sortie["sans_partie_mensonger"] = "ACCEPTÉ — artefact non détecté"
    except ea.EngagementInvalide as err:
        sortie["sans_partie_mensonger"] = f"refusé : {err}"
    try:
        lg.entrer("x-bis", e)
        sortie["relance_sous_autre_nom"] = "ACCEPTÉE — artefact non détecté"
    except ea.EngagementInvalide as err:
        sortie["relance_sous_autre_nom"] = f"refusée : {err}"
    sortie["cas_sains"] = {"relecture_tranche": "la première partie est acceptée", "sans_partie": "déclaration vraie acceptée",
                           "relance": "la fiche d'origine garde sa clé"}
    lg.verifier_sans_partie(2, {"x": "vraie absence"})
    return sortie


def repetitions_nulles(args):
    """Garantie sous le nul complet : part des répétitions avec au moins une promotion (et au moins une fiche au seuil
    de Bonferroni), avec un intervalle de Clopper-Pearson approché par Wilson."""
    au_moins_une, bonf = 0, 0
    for k in range(args.nul):
        rng = random.Random(graine_derivee(args.graine, "nul", k))
        b = banque(rng, args.generations, args.unites_par_tranche, nul=True)
        monde = mbs.MondeBanqueScores(b, graine_derivee(args.graine, "monde-nul", k))
        etat = course(monde, args.generations, args.alpha, args.tau, graine_derivee(args.graine, "course-nul", k),
                      avec_g1=True)
        au_moins_une += bool(etat["promues"])
        bonf += bool(etat["bonferroni"])
    n = args.nul
    p = au_moins_une / n
    z = 1.96
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    demi = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return {"repetitions": n, "au_moins_une_promotion": au_moins_une, "part": p, "wilson_95": [centre - demi, centre + demi],
            "au_moins_une_bonferroni": bonf, "alpha": args.alpha,
            "lecture": ("tenue" if centre + demi >= args.alpha and p <= args.alpha else
                        ("tenue (part sous α)" if p <= args.alpha else "ROMPUE : part > α"))}


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("dossier")
    a.add_argument("--generations", type=int, default=4)
    a.add_argument("--unites-par-tranche", type=int, default=40)
    a.add_argument("--graine", type=int, default=20261028)
    a.add_argument("--alpha", type=float, default=0.05)
    a.add_argument("--tau", type=float, default=0.05)
    a.add_argument("--hasard", type=int, default=6)
    a.add_argument("--nul", type=int, default=0)
    args = a.parse_args()
    if os.path.exists(args.dossier):
        raise SystemExit(f"dossier existant : {args.dossier} (R12 : jamais d'écrasement)")
    os.makedirs(args.dossier)
    rng = random.Random(graine_derivee(args.graine, "banque"))
    b = banque(rng, args.generations, args.unites_par_tranche)
    monde = mbs.MondeBanqueScores(b, graine_derivee(args.graine, "monde"))
    ecrire_json_scelle(os.path.join(args.dossier, "banque.json"), b)
    etat = course(monde, args.generations, args.alpha, args.tau, graine_derivee(args.graine, "course"), n_hasard=args.hasard)
    lec = lecture(etat)
    lec["artefacts_R5"] = artefacts(monde, args.alpha, args.tau, args.graine)
    if args.nul:
        lec["nul_repete"] = repetitions_nulles(args)
    lec["reglages"] = {k: v for k, v in vars(args).items()}
    lec["banque"] = monde.description_publique()
    ecrire_json_scelle(os.path.join(args.dossier, "course.json"), etat)
    ecrire_json_scelle(os.path.join(args.dossier, "lecture-pari-apparie.json"), lec)
    print("L1 validité :", "tenue" if lec["L1_validite"]["tenue"] else f"ROMPUE {lec['L1_validite']['promues_d_esperance_nulle_ou_negative']}")
    for f, d in lec["L2_dents"].items():
        print(f"L2 {f:24s} espérance {d['esperance_connue']:+.2f}  {'promue g' + str(d['generation']) if d['promue'] else 'non promue':14s} log e {d['log_e_final']:+.2f}")
    if lec["L3_G1"]:
        g = lec["L3_G1"]
        print(f"L3 G1 : {'promue g' + str(g['generation']) if g['promue'] else 'non promue'} ; log e {g['log_e_final']:+.2f} / seuil {g['seuil_log']:.2f} ; "
              f"comparateur le plus faible : {g['comparateur_le_plus_faible']}")
    print("promues :", lec["promues"])
    for k, v in lec["artefacts_R5"].items():
        if k != "cas_sains":
            print(f"artefact {k} : {v[:70]}")
    if args.nul:
        n = lec["nul_repete"]
        print(f"nul × {n['repetitions']} : au moins une promotion dans {n['au_moins_une_promotion']} ({n['part']:.3f} ; Wilson "
              f"[{n['wilson_95'][0]:.3f} ; {n['wilson_95'][1]:.3f}]) ; α = {n['alpha']} → {n['lecture']}")


if __name__ == "__main__":
    principal()
