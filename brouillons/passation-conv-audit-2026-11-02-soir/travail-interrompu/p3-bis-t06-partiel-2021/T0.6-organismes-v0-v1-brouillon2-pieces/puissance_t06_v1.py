"""Puissance de T0.6 v1 brouillon 2 (organisme par adaptateur, courbe dose–réponse, test croisé d'étiologie), tirée des
seules sorties de P3 sous `diag/` et de la note de puissance de P3 (aucun fichier sous `donnees/`, aucun réseau, aucun modèle).

Entrées vérifiées par leur sceau compagnon (R11) :
- `diag/20261020-075740-p3-lecture/lecture-p3.json` (effet du coût, jeux et planchers des deux sondes principales) ;
- `diag/20261019-230011-p3-reel/episodes-p3.json`, `diag/20261019-230011-p3-reel/resume.json`,
  `diag/20261019-230011-p3-reel/sondes-figees.json` (durées) ;
- `docs/notes/P3-mesures-v2/puissance-p3-v1.txt` (écart type entre épisodes de la statistique de tâche, pilote : 0,795).

1. Coût : effet minimal détectable d'une différence appariée par tâche (60 tâches, un épisode par condition), à l'erreur
   type de P3-P1.
2. Dose–réponse : simulation, y[t, d] = m[t] + f(d) + e[t, d], e ~ N(0, s²), doses {0 ; 0,25 ; 0,5 ; 0,75 ; 1}, 60 tâches ;
   critère complet : effet à la dose 1 établi (borne basse à 95 % > 0), tendance de Jonckheere–Terpstra stratifiée par tâche
   (permutations dans chaque tâche ; approximation normale de leur loi, recoupée par 2 000 permutations sur un tirage),
   p < 0,05 unilatérale, et aucune inversion établie entre doses voisines (intervalle à 95 % de la différence appariée
   entièrement sous 0). Formes : linéaire, concave (racine), convexe (carré), seuil (logistique centrée sur 0,5).
3. Détection croisée : aire minimale détectable à 80 % d'un jeu évalué sur 60 tâches (validation croisée en deux moitiés,
   scores mis en commun) ou sur 30 tâches (une seule moitié), aux erreurs types et planchers de P3.
4. Durées de P3, base du devis.
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
GRAINE = 20261102            # graine fixe de la simulation de puissance (aucune donnée tirée ; R9 vaut pour les runs)
Z95, Z80 = norm.ppf(0.975), norm.ppf(0.80)


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
    """Somme sur les tâches des paires de doses ordonnées concordantes (ex aequo pour moitié)."""
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


def simuler(rng, f: np.ndarray, s: float, n_taches: int = 60, repliques: int = 2000) -> dict:
    compte = {"effet": 0, "jt": 0, "inversion": 0, "complet": 0}
    for _ in range(repliques):
        m = rng.normal(0.0, 0.565, size=(n_taches, 1))          # écart type entre tâches (note de P3) ; s'annule
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
    m = re.search(r"écart type ([0-9.]+)\)", note)
    s_pilote = float(m.group(1))
    p1 = lec["P3-P1"]
    se_p1 = (p1["haut"] - p1["bas"]) / (2 * Z95)
    s_p3 = se_p1 * math.sqrt(p1["n_taches"]) / math.sqrt(2)

    print("\n1. Coût (statistique de tâche : moyenne du log10 des coûts lisibles de l'épisode)")
    print(f"  écart type entre épisodes, pilote (note de P3) : {s_pilote} ; tiré de P3-P1 (erreur type {se_p1:.4f}"
          f" × √60 / √2) : {s_p3:.4f}")
    for s in (s_pilote, 1.0):
        se = s * math.sqrt(2) / math.sqrt(60)
        print(f"  s = {s:.3f} : erreur type d'une différence appariée (60 tâches) {se:.4f} ; effet minimal détectable"
              f" (80 %, bilatéral 5 %) {(Z95 + Z80) * se:.4f} ; avec 30 tâches {(Z95 + Z80) * se * math.sqrt(2):.4f}")
    print(f"  pour mémoire, P3-P1 (saboteur instruit, p = 1) : {p1['effet']:.4f} [{p1['bas']:.4f} ; {p1['haut']:.4f}]")

    print("\n2. Dose–réponse de l'adaptateur, critère complet (2 000 répliques par case ; doses 0, 0,25, 0,5, 0,75, 1)")
    rng = np.random.default_rng(GRAINE)
    y0 = rng.normal(0.0, s_pilote, size=(60, len(DOSES)))
    st = jt_stratifie(y0)
    perm = np.array([jt_stratifie(np.apply_along_axis(rng.permutation, 1, y0)) for _ in range(2000)])
    print(f"  recoupement de l'approximation normale (un tirage sous l'hypothèse nulle) : p normale"
          f" {p_jt_normal(st, 60, len(DOSES)):.4f} ; p par 2 000 permutations {np.mean(perm >= st):.4f}")
    for s in (s_pilote, 1.0):
        for delta1 in (1.5227, 0.76, 0.40):
            for nom, f in formes(delta1).items():
                r = simuler(rng, f, s)
                print(f"  s = {s:.3f}, effet à la dose 1 = {delta1:.4f}, forme {nom:9s} : effet {r['effet']:.3f} ;"
                      f" tendance {r['jt']:.3f} ; inversion établie {r['inversion']:.3f} ; critère complet {r['complet']:.3f}")
    print("  sous l'hypothèse nulle (f = 0, s = 0,795) : " + json.dumps(simuler(rng, np.zeros(len(DOSES)), s_pilote)))

    print("\n3. Détection croisée : aire minimale détectable (80 %) d'un jeu, une sonde fixée d'avance, 95 %")
    ses, qs = [], []
    for p, jeux in lec["jeux"].items():
        for j, x in jeux.items():
            z = norm.ppf(1 - (1 - x["niveau"]) / 2)
            ses.append((x["haut"] - x["bas"]) / (2 * z))
            qs.append(x["plancher_quantile"])
    for nom, (q, se) in {"médiane des jeux de P3": (float(np.median(qs)), float(np.median(ses))),
                         "enveloppe prudente de P3": (max(qs), max(ses))}.items():
        for taches, facteur in ((60, 1.0), (30, math.sqrt(2))):
            print(f"  {nom}, {taches} tâches : plancher {q:.4f}, erreur type {se * facteur:.4f}, aire minimale"
                  f" détectable {q + (Z95 + Z80) * se * facteur:.4f}")
    print("  aires de validation générique des sondes principales de P3 (pour mémoire) : tromperie"
          f" {fig['aires_validation']['tromperie']['tromperie-difference_moyennes-c15']:.4f} ; enjeux"
          f" {fig['aires_validation']['enjeux']['enjeux-lineaire-c15']:.4f}")

    print("\n4. Durées de P3 (A100 SXM4 80 Go), base du devis")
    d = eps["descriptifs"]
    par_ep = d["duree_s"] / res["episodes"]
    jetons_ctx = d["jetons_contexte"] / res["actions"]
    jetons_gen = d["jetons_generes"] / res["actions"]
    print(f"  run {res['duree_s']:.1f} s ; entraînement des sondes génériques et planchers {fig['duree_s']:.1f} s"
          f" (depuis le début du run) ; épisodes {d['duree_s']:.1f} s pour {res['episodes']} ({par_ep:.1f} s par épisode)")
    print(f"  par action : contexte moyen {jetons_ctx:.0f} jetons, action moyenne {jetons_gen:.0f} jetons ; plus long"
          f" contexte rempli {d['longueur_remplie_max']} ; pic de mémoire {d['memoire_pic_gio']} Gio")
    acts_go = res["actions"] * jetons_gen * 3 * 4096 * 4 / 1e9
    print(f"  activations des jetons d'action, trois couches, simple précision : ≈ {acts_go:.1f} Go pour"
          f" {res['actions']} actions")
    flops_paire = 6 * 8.0e9 * (jetons_ctx + jetons_gen)
    for paires, epoques in ((300, 3), (900, 3)):
        for debit in (60e12, 120e12):
            h = paires * epoques * flops_paire / debit / 3600
            print(f"  distillation d'un adaptateur : {paires} paires × {epoques} époques, ≈ {flops_paire:.2e} opérations"
                  f" par paire (avant et arrière), à {debit / 1e12:.0f} téraopérations par seconde utiles : ≈ {h:.2f} h")


if __name__ == "__main__":
    main()
