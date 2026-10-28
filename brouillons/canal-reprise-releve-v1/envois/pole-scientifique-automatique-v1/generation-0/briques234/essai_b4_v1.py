"""Brique 4, essai 5 : score de fertilité du « pushout » (caste 1) et filtre de compatibilité des contraintes.

Partie 1 : à ponts constants, le score |ponts| * log(|termes_a| + |termes_b| + 1) croît-il avec la taille des
vocabulaires ? Comparaison avec la version normalisée |ponts| / |union| * log(1 + |différence symétrique|).
Fonctions extraire_termes et pushout_conceptuel copiées à l'identique du bloc de code de la caste 1 du rapport.
Partie 2 : filtre minimal par paires de marqueurs contradictoires (linéaire / non linéaire, stationnaire /
transitoire, discret / continu, convexe / non convexe) sur corpus à contradictions plantées (vérité terrain).
Usage : python3 -I -B essai_b4_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import argparse
import math
import re
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import numpy as np
from scipy.stats import spearmanr

import commun_v1 as cm
import textes_v1 as tx

GRAINES_FILTRE = 200
PAIRES_REALISTES = 2000


def score_normalise(r: dict) -> float:
    union = len(r["ponts"]) + len(r["termes_a"]) + len(r["termes_b"])
    sym = len(r["termes_a"]) + len(r["termes_b"])
    return len(r["ponts"]) / union * math.log(1 + sym) if union else 0.0


def mots_ascii(rng, nombre, interdits):
    return [w for w in tx.pseudo_mots(rng, nombre, interdits, longueur=(5, 9))]


# --- Partie 1 : biais de verbosité --------------------------------------------------------------

def partie_verbosite(pushout):
    rng = cm.generateur("b4_verbosite", 0)
    reserve = mots_ascii(rng, 400, set())
    controle = []
    for p in (1, 3, 5, 8):
        ponts = reserve[:p]
        for v in (0, 2, 5, 10, 15, 20, 22, 25, 27, 30, 40, 60):
            autres_a = reserve[50:50 + v]
            autres_b = reserve[200:200 + v]
            ta = ponts * 3 + autres_a + autres_a[: v // 2]
            tb = ponts * 3 + autres_b + autres_b[: v // 2]
            r = pushout({"texte": " ".join(ta)}, {"texte": " ".join(tb)})
            controle.append({"ponts_plantes": p, "vocabulaire_propre_par_texte": v, "ponts_detectes": len(r["ponts"]),
                             "termes_a": len(r["termes_a"]), "termes_b": len(r["termes_b"]),
                             "score_original": r["score_fertilite"], "score_normalise": score_normalise(r)})
    # Population réaliste : ponts vrais plantés + vocabulaire général partagé (ponts fortuits) + longueur variable
    general = reserve[300:400]
    poids_g = 1.0 / np.arange(1, 101) ** 1.0
    poids_g /= poids_g.sum()
    lignes = []
    for i in range(PAIRES_REALISTES):
        g = cm.generateur("b4_verbosite", 1, i)
        p = int(g.integers(0, 7))
        dom = mots_ascii(g, 2 * 200 + p, set(general))
        ponts, va, vb = dom[:p], dom[p:p + 200], dom[p + 200:p + 400]
        la, lb = int(g.integers(10, 151)), int(g.integers(10, 151))

        def texte(propre, longueur):
            n_gen = int(round(0.3 * longueur))
            mots = list(g.choice(propre, size=longueur - n_gen)) + list(g.choice(general, size=n_gen, p=poids_g))
            mots += ponts * 3
            g.shuffle(mots)
            return " ".join(mots)

        r = pushout({"texte": texte(va, la)}, {"texte": texte(vb, lb)})
        lignes.append({"p_vrai": p, "verbosite": la + lb, "ponts_detectes": len(r["ponts"]),
                       "orig": r["score_fertilite"], "norm": score_normalise(r)})
    tab = {k: np.array([x[k] for x in lignes], dtype=float) for k in lignes[0]}

    def partielle(a, b, c):
        ra, rb, rc = (spearmanr(a, c).statistic, spearmanr(b, c).statistic, spearmanr(a, b).statistic)
        return float((ra - rb * rc) / math.sqrt((1 - rb ** 2) * (1 - rc ** 2)))

    stats = {}
    for nom in ("orig", "norm", "ponts_detectes"):
        stats[nom] = {"spearman_p_vrai": float(spearmanr(tab[nom], tab["p_vrai"]).statistic),
                      "spearman_verbosite": float(spearmanr(tab[nom], tab["verbosite"]).statistic),
                      "partielle_verbosite_sachant_p_vrai": partielle(tab[nom], tab["p_vrai"], tab["verbosite"]),
                      "partielle_p_vrai_sachant_verbosite": partielle(tab[nom], tab["verbosite"], tab["p_vrai"])}
    strates = {}
    for p in range(7):
        sel = tab["p_vrai"] == p
        strates[str(p)] = {k: float(spearmanr(tab[k][sel], tab["verbosite"][sel]).statistic) for k in ("orig", "norm", "ponts_detectes")}
    rappel = {}
    for bas, haut in ((20, 100), (100, 200), (200, 301)):
        sel = (tab["verbosite"] >= bas) & (tab["verbosite"] < haut) & (tab["p_vrai"] > 0)
        rappel[f"{bas}-{haut - 1}"] = float(np.mean(np.minimum(tab["ponts_detectes"][sel], tab["p_vrai"][sel]) / tab["p_vrai"][sel]))
    return {"controle_ponts_constants": controle, "population_realiste": {"paires": PAIRES_REALISTES, "statistiques": stats,
            "spearman_score_verbosite_par_strate_p_vrai": strates,
            "ponts_fortuits_moyens_par_tranche_verbosite": {
                f"{bas}-{haut - 1}": float(np.mean((tab["ponts_detectes"] - tab["p_vrai"])[(tab["verbosite"] >= bas) & (tab["verbosite"] < haut)]))
                for bas, haut in ((20, 100), (100, 200), (200, 301))},
            "rappel_ponts_vrais_borne_par_tranche": rappel}}


# --- Partie 2 : filtre de compatibilité --------------------------------------------------------

AXES = {
    "linearite": {"neg": r"\bnon[\s-]?lin[ée]aires?\b|\bnon[\s-]?linear\b",
                  "pos": r"\blin[ée]aires?\b|\blinear\b"},
    "stationnarite": {"neg": r"\bnon[\s-]?stationnaires?\b|\binstationnaires?\b|\btransitoires?\b|\btransients?\b|\bnon[\s-]?stationary\b",
                      "pos": r"\bstationnaires?\b|\bstationary\b|\bsteady[\s-]state\b|\brégime permanent\b"},
    "continuite": {"neg": r"\bcontinu(?:e|s|es)?\b|\bcontinuous\b|\bcontinues\b",
                   "pos": r"\bdiscr[eè]te?s?\b|\bdiscrete\b"},
    "convexite": {"neg": r"\bnon[\s-]?convexes?\b|\bnon[\s-]?convex\b",
                  "pos": r"\bconvexes?\b|\bconvex\b"},
}
FORMES = {
    "linearite": {"+": {"fr": ["linéaire"], "en": ["linear"]},
                  "-": {"fr": ["non linéaire", "non-linéaire"], "en": ["nonlinear", "non-linear"]},
                  "para+": {"fr": ["affine"], "en": ["affine"]}, "para-": {"fr": ["à saturation"], "en": ["saturating"]}},
    "stationnarite": {"+": {"fr": ["stationnaire", "en régime permanent"], "en": ["stationary", "steady-state"]},
                      "-": {"fr": ["transitoire", "non stationnaire"], "en": ["transient", "non-stationary"]},
                      "para+": {"fr": ["à l'équilibre"], "en": ["time-invariant"]},
                      "para-": {"fr": ["hors équilibre"], "en": ["time-dependent"]}},
    "continuite": {"+": {"fr": ["à temps discret", "discret"], "en": ["discrete-time", "discrete"]},
                   "-": {"fr": ["à temps continu", "continu"], "en": ["continuous-time", "continuous"]},
                   "para+": {"fr": ["échantillonné sur grille"], "en": ["sampled on a grid"]},
                   "para-": {"fr": ["régi par des équations différentielles"], "en": ["governed by differential equations"]}},
    "convexite": {"+": {"fr": ["convexe"], "en": ["convex"]},
                  "-": {"fr": ["non convexe", "non-convexe"], "en": ["nonconvex", "non-convex"]},
                  "para+": {"fr": ["à minimum unique"], "en": ["single-minimum"]},
                  "para-": {"fr": ["à minima multiples"], "en": ["multi-modal"]}},
}
GABARITS = {"fr": {"assert": "Nous supposons un cadre {f}.", "mention": "Contrairement aux approches au cadre {f}, nous procédons autrement.",
                   "homographe": "Le projet continue."},
            "en": {"assert": "We assume a {f} setting.", "mention": "Unlike approaches with a {f} setting, we proceed otherwise.",
                   "homographe": "The project continues."}}
REGIMES = {"propre": (0.0, 0.0, 0.0), "realiste": (0.15, 0.15, 0.10), "bruite": (0.30, 0.30, 0.20)}


def detecter(texte: str) -> dict:
    t = texte.lower()
    out = {}
    for axe, mot in AXES.items():
        neg = re.findall(mot["neg"], t)
        masque = re.sub(mot["neg"], " ", t)
        pos = re.findall(mot["pos"], masque)
        out[axe] = "±" if (neg and pos) else ("-" if neg else ("+" if pos else "∅"))
    return out


def contradiction(va: dict, vb: dict) -> bool:
    return any({va[a], vb[a]} == {"+", "-"} for a in AXES)


def generer_texte(g, langue, valeurs, regime, ponts, domaine, nb_domaine=25):
    p_para, p_mention, p_homo = REGIMES[regime]
    phrases = []
    for axe, v in valeurs.items():
        if v == "∅":
            continue
        cle = ("para" + v) if g.random() < p_para else v
        f = str(g.choice(FORMES[axe][cle][langue]))
        phrases.append(GABARITS[langue]["assert"].format(f=f))
        if g.random() < p_mention:
            opp = "-" if v == "+" else "+"
            phrases.append(GABARITS[langue]["mention"].format(f=str(g.choice(FORMES[axe][opp][langue]))))
    if g.random() < p_homo:
        phrases.append(GABARITS[langue]["homographe"])
    mots = list(g.choice(domaine, size=nb_domaine)) + ponts * 3
    g.shuffle(mots)
    phrases.append(" ".join(mots) + ".")
    g.shuffle(phrases)
    return " ".join(phrases)


def partie_filtre(pushout):
    res = {}
    for regime in REGIMES:
        tp = fp = fn = tn = 0
        cand_total = vrais_total = acc_sans = vrais_sans = acc_avec = vrais_avec = factices = 0
        for s in range(GRAINES_FILTRE):
            g = cm.generateur("b4_filtre", list(REGIMES).index(regime), s)
            reserve = mots_ascii(g, 260, set())
            ponts_communs = reserve[:10]
            dom_a, dom_c = reserve[10:130], reserve[130:250]
            textes, verites = [], []
            for i in range(20):
                langue = "fr" if g.random() < 0.5 else "en"
                valeurs = {axe: str(g.choice(["+", "-", "∅"], p=[0.3, 0.3, 0.4])) for axe in AXES}
                ponts = list(g.choice(ponts_communs, size=int(g.integers(0, 4)), replace=False))
                textes.append(generer_texte(g, langue, valeurs, regime, ponts, dom_a if i < 10 else dom_c))
                verites.append(valeurs)
            detections = [detecter(t) for t in textes]
            for i in range(10):
                for j in range(10, 20):
                    r = pushout({"texte": textes[i]}, {"texte": textes[j]})
                    if not r["ponts"]:
                        continue
                    cand_total += 1
                    factices += int(not (r["ponts"] & set(ponts_communs)))
                    vrai = contradiction(verites[i], verites[j])
                    det = contradiction(detections[i], detections[j])
                    vrais_total += int(vrai)
                    tp += int(vrai and det)
                    fp += int(det and not vrai)
                    fn += int(vrai and not det)
                    tn += int(not vrai and not det)
                    acc_sans += 1
                    vrais_sans += int(vrai)
                    if not det:
                        acc_avec += 1
                        vrais_avec += int(vrai)
        res[regime] = {
            "parametres_bruit": dict(zip(("paraphrase", "mention_contraire", "homographe"), REGIMES[regime])),
            "fusions_candidates_ponts_non_vides": cand_total,
            "part_contradictoires_vraies_parmi_candidates": vrais_total / cand_total,
            "part_candidates_sans_aucun_pont_plante": factices / cand_total,
            "sans_filtre": {"acceptees": acc_sans, "part_contradictoires_vraies": vrais_sans / acc_sans,
                            "part_contradiction_detectee": (tp + fp) / cand_total},
            "avec_filtre": {"acceptees": acc_avec, "part_contradictoires_vraies": vrais_avec / acc_avec,
                            "part_contradiction_detectee": 0.0},
            "detecteur": {"precision": tp / (tp + fp) if tp + fp else None, "rappel": tp / (tp + fn) if tp + fn else None,
                          "rejets_a_tort_parmi_compatibles": fp / (fp + tn) if fp + tn else None,
                          "vp": tp, "fp": fp, "fn": fn, "vn": tn},
        }
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    args = ap.parse_args()
    t0 = time.time()
    fs, emp = cm.copier_fonctions("rapport", ["extraire_termes", "pushout_conceptuel"], source_texte=cm.code_caste1_rapport())
    pushout = fs["pushout_conceptuel"]
    verb = partie_verbosite(pushout)
    filtre = partie_filtre(pushout)
    sortie = {
        "essai": "brique 4, essai 5 : score de fertilité et filtre de compatibilité",
        "heure_lancement_utc": args.heure,
        "duree_s": round(time.time() - t0, 1),
        "graines": cm.description_graines() | {"taches": {"b4_verbosite": "(8, 0) contrôle ; (8, 1, i) paire réaliste i",
                                                          "b4_filtre": "(9, id_regime, s)"}},
        "versions": cm.versions(),
        "instrument": {"source": "bloc de code de la caste 1 du rapport (copie exacte)", "empreintes_segments": emp,
                       "note_jetons": "extraire_termes : \\b[a-z]{4,}\\b, les mots accentués sont éliminés (pas fragmentés)"},
        "verbosite": verb,
        "filtre": {"axes": list(AXES), "regle": "contradiction détectée si, sur un axe, un texte vaut + et l'autre - "
                                                "(valeur ± = les deux marqueurs présents, non comptée)",
                   "corpus": f"{GRAINES_FILTRE} corpus de 20 textes (10 domaine A, 10 domaine C), valeurs +/-/∅ "
                             "de probabilités 0,3/0,3/0,4 par axe, langue français ou anglais à 0,5",
                   "resultats": filtre},
    }
    cm.ecrire_json(cm.SORTIE / "resultats-b4-v1.json", sortie)
    print("fini", sortie["duree_s"], "s")


if __name__ == "__main__":
    main()
