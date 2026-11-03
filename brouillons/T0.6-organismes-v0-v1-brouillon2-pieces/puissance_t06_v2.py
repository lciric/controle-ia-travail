"""Puissance et devis de T0.6 v1, brouillon 2 (organisme (ii) par adaptateur de rang faible à dose réglable, courbe
dose–réponse, test croisé d'étiologie), v2 du script, tirée des seules sorties de P3 sous `diag/` et de la note de
puissance de P3 (aucun fichier sous `donnees/`, aucun réseau, aucun modèle).

Changement depuis la v1 (`puissance_t06_v1.py`, ebaecdb1…, gardée telle quelle, R12 ; rejouée à l'identique) : la v1
supposait 60 tâches d'évaluation. Or un organisme distillé sur les actions du saboteur de P3 a vu 60 des 64 tâches
d'évaluation du pilote ; les tâches disjointes sont alors 36 au plus (les 32 tâches de réserve et les 4 tâches
d'évaluation que P3 n'a pas prises). La v2 donne chaque grandeur aux deux plans du brouillon 2 (décision DT-1) : (a) 36
tâches disjointes, distillation sur les 600 actions de P3 ; (b) 64 tâches d'évaluation, distillation sur des actions
neuves du saboteur instruit de P3 jouées sur les 32 tâches de réserve. Elle ajoute le devis par phase. Les formules de
la v1 sont gardées (vérifiées : erreur type d'une différence appariée s √2 / √n ; Jonckheere–Terpstra stratifiée par
tâche, moyenne n k (k − 1) / 4, variance n k (k − 1) (2k + 5) / 72 ; aire minimale détectable q95 + (z_0,975 + z_0,80) se).

Entrées vérifiées par leur sceau compagnon (R11) :
- `diag/20261020-075740-p3-lecture/lecture-p3.json` (effet du coût, jeux et planchers des deux sondes principales) ;
- `diag/20261019-230011-p3-reel/episodes-p3.json`, `diag/20261019-230011-p3-reel/resume.json`,
  `diag/20261019-230011-p3-reel/sondes-figees.json` (durées, jetons) ;
- `docs/notes/P3-mesures-v2/puissance-p3-v1.txt` (écart type entre épisodes de la statistique de tâche, pilote : 0,795).
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from pathlib import Path

import numpy as np
from scipy.stats import norm

RACINE = Path(__file__).resolve().parents[2]
ENTREES = {
    "lecture": "diag/20261020-075740-p3-lecture/lecture-p3.json",
    "episodes": "diag/20261019-230011-p3-reel/episodes-p3.json",
    "resume": "diag/20261019-230011-p3-reel/resume.json",
    "figees": "diag/20261019-230011-p3-reel/sondes-figees.json",
    "note": "docs/notes/P3-mesures-v2/puissance-p3-v1.txt",
}
DOSES = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
ENTROPIE_SIMULATION = 20261103      # entropie fixe de la simulation de puissance (aucune donnée tirée ; R9 vaut pour les runs)
REPLIQUES = 2000
Z95, Z80 = norm.ppf(0.975), norm.ppf(0.80)
PLANS = {"(a) 36 tâches disjointes": 36, "(b) 64 tâches d'évaluation": 64}


def lire(rel: str):
    chemin = RACINE / rel
    if "donnees" in Path(rel).parts:
        sys.exit(f"{rel} : aucun fichier sous donnees/ n'est lu")
    sceau = Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()[0]
    sha = hashlib.sha256(chemin.read_bytes()).hexdigest()
    if sha != sceau:
        sys.exit(f"{rel} : empreinte {sha[:12]} ≠ sceau {sceau[:12]} (R11)")
    print(f"entrée {rel} sha256 {sha}")
    texte = chemin.read_text(encoding="utf-8")
    return json.loads(texte) if rel.endswith(".json") else texte


def formes(delta1: float) -> dict:
    s = lambda d: 1.0 / (1.0 + np.exp(-12.0 * (d - 0.5)))
    return {"linéaire": delta1 * DOSES, "concave": delta1 * np.sqrt(DOSES), "convexe": delta1 * DOSES ** 2,
            "seuil": delta1 * (s(DOSES) - s(0.0)) / (s(1.0) - s(0.0))}


def jt_stratifie(y: np.ndarray) -> float:
    k = y.shape[1]
    total = 0.0
    for a in range(k):
        for b in range(a + 1, k):
            total += float(np.sum(y[:, a] < y[:, b]) + 0.5 * np.sum(y[:, a] == y[:, b]))
    return total


def p_jt_normal(stat: float, n_taches: int, k: int) -> float:
    moyenne = n_taches * k * (k - 1) / 4.0
    variance = n_taches * k * (k - 1) * (2 * k + 5) / 72.0
    return float(1.0 - norm.cdf((stat - moyenne - 0.5) / math.sqrt(variance)))


def critere(y: np.ndarray) -> dict:
    n = y.shape[0]
    d1 = y[:, -1] - y[:, 0]
    effet = d1.mean() - Z95 * d1.std(ddof=1) / math.sqrt(n) > 0
    jt = p_jt_normal(jt_stratifie(y), n, y.shape[1]) < 0.05
    inversion = False
    for a in range(y.shape[1] - 1):
        d = y[:, a + 1] - y[:, a]
        if d.mean() + Z95 * d.std(ddof=1) / math.sqrt(n) < 0:
            inversion = True
    return {"effet": effet, "jt": jt, "inversion": inversion, "complet": effet and jt and not inversion}


def simuler(rng, f: np.ndarray, s: float, n_taches: int, repliques: int = REPLIQUES) -> dict:
    compte = {"effet": 0, "jt": 0, "inversion": 0, "complet": 0}
    for _ in range(repliques):
        m = rng.normal(0.0, 0.565, size=(n_taches, 1))          # écart type entre tâches (note de P3, l. 2) ; s'annule
        y = m + f[None, :] + rng.normal(0.0, s, size=(n_taches, len(DOSES)))
        c = critere(y)
        for cle in compte:
            compte[cle] += int(c[cle])
    return {cle: v / repliques for cle, v in compte.items()}


def main() -> None:
    lec = lire(ENTREES["lecture"])["resultat"]
    eps = lire(ENTREES["episodes"])["resultat"]
    res = lire(ENTREES["resume"])["resultat"]
    fig = lire(ENTREES["figees"])["resultat"]
    note = lire(ENTREES["note"])
    s_pilote = float(re.search(r"écart type ([0-9.]+)\)", note).group(1))
    p1 = lec["P3-P1"]
    se_p1 = (p1["haut"] - p1["bas"]) / (2 * Z95)
    s_p3 = se_p1 * math.sqrt(p1["n_taches"]) / math.sqrt(2)

    print("\n1. Coût (statistique de tâche : moyenne du log10 des coûts lisibles de l'épisode), différence appariée par tâche")
    print(f"  écart type entre épisodes : pilote (note de P3) {s_pilote} ; tiré de P3-P1 (erreur type {se_p1:.4f} × √60 / √2)"
          f" {s_p3:.4f} ; prudent 1,000")
    for nom, n in PLANS.items():
        for s in (s_pilote, 1.0):
            se = s * math.sqrt(2) / math.sqrt(n)
            print(f"  {nom}, s = {s:.3f} : erreur type {se:.4f} ; effet minimal détectable (80 %, bilatéral 5 %)"
                  f" {(Z95 + Z80) * se:.4f} (log10)")
    print(f"  pour mémoire, P3-P1 (saboteur instruit de P3, 60 tâches) : {p1['effet']:.4f} [{p1['bas']:.4f} ; {p1['haut']:.4f}]")

    print(f"\n2. Dose–réponse de l'adaptateur, critère complet ({REPLIQUES} répliques par case ; doses 0, 0,25, 0,5, 0,75, 1 ;"
          " la dose 0 est l'honnête)")
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE_SIMULATION))
    for nom, n in PLANS.items():
        y0 = rng.normal(0.0, s_pilote, size=(n, len(DOSES)))
        st = jt_stratifie(y0)
        perm = np.array([jt_stratifie(np.apply_along_axis(rng.permutation, 1, y0)) for _ in range(1000)])
        print(f"  {nom} : recoupement de l'approximation normale sur un tirage nul : p normale"
              f" {p_jt_normal(st, n, len(DOSES)):.4f} ; p par 1 000 permutations {np.mean(perm >= st):.4f}")
        for s in (s_pilote, 1.0):
            for delta1 in (1.5227, 0.76, 0.40):
                for forme, f in formes(delta1).items():
                    r = simuler(rng, f, s, n)
                    print(f"    s = {s:.3f}, effet à la dose 1 = {delta1:.4f}, forme {forme:9s} : effet {r['effet']:.3f} ;"
                          f" tendance {r['jt']:.3f} ; inversion établie {r['inversion']:.3f} ; critère complet {r['complet']:.3f}")
        print(f"    sous l'hypothèse nulle (f = 0, s = {s_pilote}) : "
              + json.dumps(simuler(rng, np.zeros(len(DOSES)), s_pilote, n)))

    print("\n3. Test croisé : aire minimale détectable (80 %) d'un jeu, une sonde fixée d'avance, 95 %, scores des deux plis"
          " mis en commun")
    ses, qs = [], []
    for p, jeux in lec["jeux"].items():
        for j, x in jeux.items():
            z = norm.ppf(1 - (1 - x["niveau"]) / 2)
            ses.append((x["haut"] - x["bas"]) / (2 * z))
            qs.append(x["plancher_quantile"])
    for base, (q, se) in {"médiane des jeux de P3": (float(np.median(qs)), float(np.median(ses))),
                          "enveloppe prudente de P3": (max(qs), max(ses))}.items():
        for nom, n in PLANS.items():
            for taches, quoi in ((n, "toutes les tâches"), (n // 2, "un seul pli")):
                f_ = math.sqrt(60 / taches)
                se_n = se * f_
                q_fixe, q_echelle = q, 0.5 + (q - 0.5) * f_
                print(f"  {base}, {nom}, {quoi} ({taches} tâches) : erreur type {se_n:.4f} ; aire minimale détectable"
                      f" {q_fixe + (Z95 + Z80) * se_n:.4f} (plancher de P3 {q_fixe:.4f}) à"
                      f" {q_echelle + (Z95 + Z80) * se_n:.4f} (plancher élargi comme l'erreur type, {q_echelle:.4f})")
    print("  aires de validation générique des sondes principales de P3 (pour mémoire) : tromperie"
          f" {fig['aires_validation']['tromperie']['tromperie-difference_moyennes-c15']:.4f} ; enjeux"
          f" {fig['aires_validation']['enjeux']['enjeux-lineaire-c15']:.4f}")

    print("\n4. Devis par phase (A100 SXM4 80 Go, débits de P3 ; aucun débit ni prix de H200 n'est mesuré dans le dépôt)")
    d = eps["descriptifs"]
    par_ep = d["duree_s"] / res["episodes"]
    ctx = d["jetons_contexte"] / res["actions"]
    gen = d["jetons_generes"] / res["actions"]
    transcription = d["jetons_passe_unique"] / res["episodes"]
    print(f"  P3 : run {res['duree_s']:.1f} s ; épisodes {d['duree_s']:.1f} s pour {res['episodes']} ({par_ep:.1f} s par"
          f" épisode, lots de 8) ; sondes génériques et planchers {fig['duree_s']:.1f} s depuis le début du run ; passe"
          f" unique {d['passe_unique_s']:.1f} s ; par action, contexte {ctx:.0f} et action {gen:.0f} jetons ; transcription"
          f" finale {transcription:.0f} jetons par épisode ; pic de mémoire {d['memoire_pic_gio']} Gio")
    flops_jeton = 6 * 8.03e9
    for nom, n in PLANS.items():
        donnees = 0 if n == 36 else 2 * 32 * 5          # (b) : saboteur et témoin instruits, 5 épisodes par tâche de réserve
        paires = 600 if n == 36 else 32 * 5 * 10        # paires (contexte, action) par adaptateur
        episodes_eval = 9 * n                           # neuf conditions (brouillon 2, plan d'analyse, point 3)
        h_donnees = donnees * par_ep / 3600
        h_eval = episodes_eval * par_ep / 3600
        print(f"  {nom} : génération des données de distillation {donnees} épisodes ≈ {h_donnees:.2f} h ;"
              f" épisodes d'évaluation {episodes_eval} ≈ {h_eval:.2f} h")
        for mode, jetons in (("paire par action", paires * (ctx + gen)),
                             ("transcription entière par épisode", (paires / 10) * transcription)):
            for debit in (60e12, 120e12):
                h = 2 * 3 * jetons * flops_jeton / debit / 3600       # deux adaptateurs, trois époques
                total = h_donnees + h + h_eval + 1.0                # + mise en place, suite des tests, chargement : ≈ 1 h
                print(f"    distillation ({mode}), deux adaptateurs, trois époques, {debit / 1e12:.0f} téraopérations par"
                      f" seconde utiles : ≈ {h:.2f} h ; total ≈ {total:.1f} h ; à 1,0889 à 1,30 USD de l'heure"
                      f" ≈ {total * 1.0889:.1f} à {total * 1.30:.1f} USD de calcul")
    acts = 9 * 64 * 10 * gen * 4096 * 2 / 1e9
    print(f"  activations des jetons d'action en demi-précision, plan (b) : ≈ {acts:.1f} Go par couche, ≈ {3 * acts:.1f} Go"
          " pour les trois couches (gardées sur l'instance ; identifiants générés poussés, sous-ensemble tiré par graine)")


if __name__ == "__main__":
    main()
