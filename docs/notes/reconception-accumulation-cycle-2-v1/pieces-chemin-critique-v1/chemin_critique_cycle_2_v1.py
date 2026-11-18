"""Chemin critique du second cycle de la lecture « accumuler les scores de sondes sur l'épisode » — v1.

Planification seulement : aucune donnée d'expérience lue, aucun seuil ni critère d'analyse.
Durées en heures écoulées (basse, probable, haute), tirées des horodatages de registre et de commit
cités dans `chemin-critique-cycle-2-v1.md` (tableau des étapes). Tirage triangulaire indépendant
par étape (simplification déclarée : les retards réels sont corrélés — disponibilité de Lazar,
limites du compte, pannes du loueur).

Usage : PYTHONPATH=src python3 -B chemin_critique_cycle_2_v1.py > sortie-chemin-critique-cycle-2-v1.txt
"""
from __future__ import annotations

import datetime as dt

import numpy as np

T0 = dt.datetime(2026, 11, 18, 21, 30, tzinfo=dt.timezone.utc)  # départ du calcul (heure de rédaction)
CIBLES = {
    "résultats prêts (GO-2026-11-18-30) : 2026-11-25T18:00Z": dt.datetime(2026, 11, 25, 18, 0, tzinfo=dt.timezone.utc),
    "veille de l'entretien : 2026-11-27T00:00Z": dt.datetime(2026, 11, 27, 0, 0, tzinfo=dt.timezone.utc),
}
ENTROPIE = 20261118  # graine écrite ici (R9), SeedSequence
N_TIRAGES = 20000

# id : (libellé, basse, probable, haute, dépendances)
BASE = {
    # Piste de l'étape B bis (autre session ; GO-2026-11-18-56)
    "E1": ("quatrième addendum de l'étape B bis : rédaction, contre-lecture, scellement", 1.5, 3, 10, []),
    "E2": ("module de lecture neuf de l'étape B bis : code, essais, contre-lecture", 2, 6, 18, []),
    "E3": ("lecture de l'étape B bis au processeur par un lecteur neuf (LECTURE-BBIS)", 0.5, 2, 12, ["E1", "E2"]),
    "E4": ("verdict de l'étape B bis par un agent neuf (VERDICT-BBIS)", 0.3, 3, 69, ["E3"]),
    "E5": ("table conjointe (CONJOINTE-BBIS)", 0.5, 2, 8, ["E4"]),
    # Préparation sans verdict ni dépense
    "P1": ("ordre exploratoire : marqueurs remplis, contre-lu, scellé (ORDRE-TEMPS1-ACC2)", 1, 3, 8, []),
    "P2": ("recette de la famille, instance aveugle, mode « coût » rejoué, scellée fermée (RECETTE-FAMILLE-ACC2)", 2, 5, 12, []),
    "P3": ("code de la relecture complémentaire (repris de la chaîne de l'étape B bis), essais, contre-lecture, ligne de GO", 2, 5, 12, []),
    "OUV": ("ouverture du temps 1 (OUVERTURE-TEMPS1-ACC2), vérifiée par la session mère", 0.1, 0.25, 1, ["E5", "P1", "P2"]),
    # Tâches fraîches
    "F1": ("textes du tirage complémentaire et de l'extraction à l'échelle, contre-lus, scellés", 3, 8, 16, []),
    "F2": ("devis de l'extraction (point 8 (a)) et ligne de GO", 1, 4, 24, ["F1"]),
    "F3": ("run de sélection complémentaire", 0.3, 1, 3, ["F2", "P2"]),
    "F4": ("extraction d'environ 760 papiers par sous-agents neufs", 8, 14, 80, ["F3"]),
    "F5": ("contre-vérification, assemblage, liste scellée fermée (TACHES-ACC2)", 1, 3, 12, ["F4"]),
    # Temps 1
    "T1": ("relecture complémentaire sur carte : lancement, marche, poussée, destruction", 4, 8, 30, ["OUV", "P3"]),
    "T2": ("conception et gel de la sonde, épreuve plantée du développement, simulation de puissance", 24, 48, 168, ["T1"]),
    "SONDES": ("clôture du temps 1 (SONDES-ACC2), strictement après TACHES-ACC2", 0.1, 0.25, 1, ["T2", "F5"]),
    # Code et scellement
    "C1": ("code de la chaîne de confirmation (famille et lecture), essais sur jouets, contre-lecture", 16, 36, 72, []),
    "AB": ("bras d'attaque chargé de fabriquer un faux positif (lit la recette ; agent neuf)", 4, 12, 48, ["P2"]),
    "S1": ("le code rejoue l'épreuve sur la sonde gelée ; dernière contre-lecture ; scellement (SCELLEMENT-ACC2)", 2, 6, 24, ["SONDES", "C1", "AB"]),
    "G1": ("gestes avant création : ligne d'engagement, dépôt daté des empreintes chez un tiers (Lazar)", 0.5, 4, 24, ["S1"]),
    # Famille et lecture
    "FAM": ("création de la famille, une machine, 400 tâches (lancement compris)", 53, 60, 120, ["G1"]),
    "L1": ("validité de la famille, épreuve plantée sur ses données honnêtes, lecture (processeur)", 4, 12, 24, ["FAM"]),
    "V1": ("verdict par un agent neuf", 0.3, 8, 24, ["L1"]),
}


def scenario(nom):
    s = {k: list(v) for k, v in BASE.items()}
    if nom in ("B", "C", "D", "E", "BE", "BDE", "BT", "BDET"):
        s["FAM"] = ["création de la famille, deux machines de génération, 400 tâches", 30, 40, 80, ["G1"]]
    if nom == "B6":
        s["FAM"] = ["création de la famille, deux machines de génération, 600 tâches", 45, 54, 108, ["G1"]]
    if nom in ("E", "BE", "BDE", "BDET"):
        # levée : relecture complémentaire jouée avant l'ouverture, sorties scellées fermées (nœud)
        s["T1"] = [s["T1"][0] + " — jouée avant l'ouverture, scellée fermée", 4, 8, 30, ["P3"]]
        s["T2"] = [s["T2"][0], 24, 48, 168, ["T1", "OUV"]]
    if nom in ("D", "BDE", "BDET"):
        # levée : génération avant le gel, sorties scellées fermées ; relecture et notation après le scellement (nœud)
        s["G0"] = ["gestes avant génération : ligne de GO, dépôt daté (recette, liste), bras d'attaque rendu", 0.5, 4, 24, ["F5", "P2", "AB"]]
        s["FAMG"] = ["pièce de génération, deux machines, 600 tâches (sorties scellées fermées)", 38, 46, 95, ["G0"]]
        s["S1"] = [s["S1"][0], 2, 6, 24, ["SONDES", "C1"]]
        s["G1"] = ["dépôt daté de l'empreinte de la sonde gelée et du texte scellé", 0.5, 2, 12, ["S1"]]
        s["FAM"] = ["pièce de relecture et de notation (600 tâches), après le scellement", 9, 14, 30, ["G1", "FAMG"]]
    if nom in ("BT", "BDET"):
        # levée : temps 1 borné à 48 heures dans l'ordre exploratoire, encore brouillon (nœud ; repli du point 6 (b) si aucune sonde)
        s["T2"] = [s["T2"][0] + " — borné à 48 heures", 24, 36, 48, s["T2"][4]]
    return s


def ordre_topo(s):
    vu, ordre = set(), []

    def visite(k):
        if k in vu:
            return
        for d in s[k][4]:
            visite(d)
        vu.add(k)
        ordre.append(k)

    for k in s:
        visite(k)
    return ordre


def passe_avant(s, durees):
    fin, pred = {}, {}
    for k in ordre_topo(s):
        deps = s[k][4]
        debut = max((fin[d] for d in deps), default=0.0)
        pred[k] = max(deps, key=lambda d: fin[d]) if deps else None
        fin[k] = debut + durees[k]
    return fin, pred


def passe_arriere(s, durees, echeance_h, cible="V1"):
    succ = {k: [] for k in s}
    for k, v in s.items():
        for d in v[4]:
            succ[d].append(k)
    lf = {}
    for k in reversed(ordre_topo(s)):
        if not succ[k]:
            lf[k] = echeance_h if k == cible else float("inf")
        else:
            lf[k] = min(lf[j] - durees[j] for j in succ[k])
    return lf


def date(h):
    return (T0 + dt.timedelta(hours=float(h))).strftime("%Y-%m-%dT%H:%MZ")


def chemin(pred, fin_noeud="V1"):
    c, k = [], fin_noeud
    while k is not None:
        c.append(k)
        k = pred[k]
    return list(reversed(c))


def main():
    print(f"départ T0 = {T0.isoformat()} ; graine SeedSequence({ENTROPIE}) ; {N_TIRAGES} tirages ; numpy {np.__version__}")
    noms = {
        "A": "avec levée de la validité de l'adaptateur (GO-2026-11-18-58), une machine, 400 tâches",
        "B": "A + deux machines de génération, 400 tâches",
        "B6": "A + deux machines de génération, 600 tâches",
        "E": "B + relecture complémentaire jouée avant l'ouverture (levée, nœud)",
        "D": "B + génération de la famille avant le gel (levée, nœud), 600 tâches",
        "BDE": "B + D + E",
        "BT": "B + temps 1 borné à 48 heures (levée, nœud)",
        "BDET": "B + D + E + temps 1 borné à 48 heures (tous les leviers)",
    }
    ss = np.random.SeedSequence(ENTROPIE)
    graines = ss.spawn(len(noms))
    for (nom, libelle), graine in zip(noms.items(), graines):
        s = scenario(nom)
        print(f"\n=== scénario {nom} : {libelle}")
        for lab, idx in (("basse", 1), ("probable", 2), ("haute", 3)):
            durees = {k: v[idx] for k, v in s.items()}
            fin, pred = passe_avant(s, durees)
            jalons = ["OUV", "F5", "SONDES", "S1", "FAM", "V1"]
            print(f"  [{lab}] " + " ; ".join(f"{j} {date(fin[j])}" for j in jalons))
            if lab == "probable":
                print("  chemin critique (probable) : " + " -> ".join(chemin(pred)))
                ech = (CIBLES["résultats prêts (GO-2026-11-18-30) : 2026-11-25T18:00Z"] - T0).total_seconds() / 3600
                lf_m = passe_arriere(s, durees, ech)
                lf_b = passe_arriere(s, {k: v[1] for k, v in s.items()}, ech)
                marge = {k: lf_m[k] - fin[k] for k in s}
                print("  marges à la date probable (heures, relatives à l'échéance du 25 à 18:00Z) : "
                      + " ; ".join(f"{k} {marge[k]:+.0f}" for k in ordre_topo(s)))
                print("  bascule (dernière fin permise pour un verdict le 25 à 18:00Z) — "
                      "au rythme probable du reste | au rythme bas du reste :")
                for k in ["E4", "OUV", "T1", "F5", "SONDES", "C1", "S1", "G1", "FAMG", "FAM", "L1"]:
                    if k in s:
                        print(f"    {k} : {date(lf_m[k])} | {date(lf_b[k])}")
        rng = np.random.default_rng(graine)
        cles = list(s)
        b = np.array([s[k][1] for k in cles])
        m = np.array([s[k][2] for k in cles])
        h = np.array([s[k][3] for k in cles])
        tirs = rng.triangular(b, m, h, size=(N_TIRAGES, len(cles)))
        fins = {j: [] for j in ("OUV", "SONDES", "S1", "V1")}
        compte_chemin = {}
        for i in range(N_TIRAGES):
            fin, pred = passe_avant(s, dict(zip(cles, tirs[i])))
            for j in fins:
                fins[j].append(fin[j])
            c = " -> ".join(chemin(pred))
            compte_chemin[c] = compte_chemin.get(c, 0) + 1
        for j, v in fins.items():
            q = np.quantile(np.array(v), [0.1, 0.5, 0.9])
            print(f"  tirage {j} : P10 {date(q[0])} ; P50 {date(q[1])} ; P90 {date(q[2])}")
        v1 = np.array(fins["V1"])
        for lib, c in CIBLES.items():
            hc = (c - T0).total_seconds() / 3600
            print(f"  part des tirages avec verdict avant « {lib} » : {np.mean(v1 <= hc):.3f}")
        s1 = np.array(fins["S1"])
        hc = (CIBLES["résultats prêts (GO-2026-11-18-30) : 2026-11-25T18:00Z"] - T0).total_seconds() / 3600
        print(f"  part des tirages avec texte scellé et sonde gelée (SCELLEMENT-ACC2) avant le 25 à 18:00Z : {np.mean(s1 <= hc):.3f}")
        top = sorted(compte_chemin.items(), key=lambda x: -x[1])[:3]
        for c, n in top:
            print(f"  chemin critique tiré {n / N_TIRAGES:.3f} : {c}")


if __name__ == "__main__":
    main()
