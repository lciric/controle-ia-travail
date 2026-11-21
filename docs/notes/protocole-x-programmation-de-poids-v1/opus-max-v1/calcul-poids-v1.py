# -*- coding: utf-8 -*-
"""Calculs de la note « programmation de poids, défense et emploi défensif » (Opus 5.5, v1).

Aucune donnée du programme : lois exactes et simulation sous suppositions d'illustration.
Blocs :
  A. Témoins fonctionnels tirés au hasard contre une écriture étroite (loi exacte).
  B. Re-dérivation tirée au hasard avec un plancher a (loi exacte).
  C. Étalonnage sans loi d'un test de résidu sur m paires honnêtes (loi exacte, échangeabilité).
  D. Écriture de rang un ou creuse cachée dans le bruit de re-dérivation (simulation, graines SeedSequence).
  E. Lecteurs de poids publiés pris comme portes : Bayes et intervalles exacts, à partir des comptes
     publiés (arXiv 2611.15118, tableaux 5 et 6, p. 16-17 ; arXiv 2611.21449, p. 13-14).
Commande : .venv/bin/python calcul-poids-v1.py > calcul-poids-v1.txt
"""
import math
import sys

import numpy as np
from scipy import stats

ENTROPIE = 202611211700  # racine consignée (R9) ; toute la simulation se rejoue à l'identique
racine = np.random.SeedSequence(ENTROPIE)
ss_D1, ss_D2, ss_D3 = racine.spawn(3)

print("numpy", np.__version__, "| scipy", __import__("scipy").__version__, "| python", sys.version.split()[0])
print("SeedSequence racine, entropie =", racine.entropy)
print()

# ---------------------------------------------------------------- A
print("A. Témoins fonctionnels : k entrées secrètes tirées selon la loi d'usage ; l'écriture ne change")
print("   la sortie que sur une part p de cette loi (déclencheur étroit). P(au moins un témoin touché) = 1-(1-p)^k.")
ps = [1e-2, 1e-3, 1e-4, 1e-6, 1e-9]
ks = [100, 10_000, 1_000_000]
print("   p \\ k      " + "".join(f"{k:>14,}" for k in ks) + "   k pour 95 %")
for p in ps:
    ligne = "".join(f"{1 - (1 - p) ** k:>14.4f}" for k in ks)
    k95 = math.ceil(math.log(0.05) / math.log1p(-p))
    print(f"   {p:<10.0e}{ligne}   {k95:>12,}")
print("   Lecture : un témoin fonctionnel au hasard ne voit pas une écriture dont le déclencheur est rare ;")
print("   il faut de l'ordre de 3/p entrées. Il sert contre une écriture large, pas contre une écriture étroite.")
print()

# ---------------------------------------------------------------- B
print("B. Re-dérivation au hasard : chaque artefact de poids (organisme, sonde, adaptateur) est re-dérivé par")
print("   un tiers avec probabilité a (plancher), indépendamment. K artefacts falsifiés : P(aucun re-dérivé) = (1-a)^K.")
aas = [0.05, 0.10, 0.20, 0.50]
Ks = [1, 3, 10, 30]
print("   a \\ K   " + "".join(f"{K:>10}" for K in Ks))
for a in aas:
    print(f"   {a:<8.2f}" + "".join(f"{(1 - a) ** K:>10.4f}" for K in Ks))
print("   Lecture : le plancher borne la durée de vie d'une falsification répétée (espérance 1/a artefacts),")
print("   pas celle d'une falsification unique (elle passe avec probabilité 1-a).")
print()

# ---------------------------------------------------------------- C
print("C. Étalonnage sans loi : statistique de résidu S (écart entre l'artefact livré et sa re-dérivation),")
print("   seuil = r-ième plus grande valeur de S sur m paires honnêtes (deux re-dérivations honnêtes).")
print("   Sous échangeabilité, P(S_nouvelle > seuil) = r/(m+1) exactement, quelle que soit la loi de S.")
for alpha in [0.05, 0.01, 0.001]:
    m_min = math.ceil(1 / alpha) - 1
    print(f"   fausse alerte {alpha:>6.3f} au seuil du maximum (r=1) : m = {m_min} paires honnêtes")
print("   Re-dérivation exacte au bit près : S honnête = 0 sur toute paire ; le test « résidu nul » n'a besoin")
print("   d'aucune référence et sa fausse alerte est nulle, à condition que l'objet de contrôle (deux re-dérivations")
print("   honnêtes, empreintes égales) tienne. Coût du non-déterminisme : de l'ordre de 1/alpha re-dérivations.")
print()

# ---------------------------------------------------------------- D
print("D. Écriture cachée dans le bruit de re-dérivation (supposé : bruit i.i.d. gaussien d'écart sigma par")
print("   coefficient ; matrice n x n). Deux formes d'écriture : rang un (theta * u v^T, u et v unitaires) et")
print("   creuse (c coefficients d'amplitude h dans une colonne). Trois statistiques : plus grande valeur")
print("   singulière, plus grand coefficient en valeur absolue, énergie (norme de Frobenius au carré).")
print("   Seuils au quantile 99 % de 400 tirages nuls ; puissance sur 200 tirages par point.")


def statistiques(R):
    s1 = np.linalg.svd(R, compute_uv=False)[0]
    return s1, np.abs(R).max(), float((R * R).sum())


def simule(n, sigma, forme, taille, rng, reps):
    out = np.empty((reps, 3))
    for i in range(reps):
        R = sigma * rng.standard_normal((n, n))
        if forme == "rang1" and taille > 0:
            u = rng.standard_normal(n); u /= np.linalg.norm(u)
            v = rng.standard_normal(n); v /= np.linalg.norm(v)
            R += taille * np.outer(u, v)
        elif forme == "creuse" and taille > 0:
            c = 8
            j = rng.integers(n)
            lignes = rng.choice(n, size=c, replace=False)
            R[lignes, j] += taille * rng.choice([-1.0, 1.0], size=c)
        out[i] = statistiques(R)
    return out


for n, ss in [(256, ss_D1), (512, ss_D2)]:
    rng = np.random.default_rng(ss)
    sigma = 1.0
    nuls = simule(n, sigma, "rang1", 0.0, rng, 400)
    seuils = np.quantile(nuls, 0.99, axis=0)
    bord = sigma * 2 * math.sqrt(n)            # bord du spectre du bruit, sigma (sqrt(n)+sqrt(n))
    bbp = sigma * math.sqrt(n)                  # seuil de séparation attendu, sigma (n n)^(1/4)
    print(f"   n = {n} : bord du bruit 2 sigma sqrt(n) = {bord:.1f} ; seuil attendu sigma sqrt(n) = {bbp:.1f} ;"
          f" seuils 99 % observés : s1 = {seuils[0]:.2f}, max|R| = {seuils[1]:.2f}, énergie = {seuils[2]:.0f}")
    print(f"   rang un, theta en unités de sigma sqrt(n) -> puissance (s1 | max | énergie) ; gain de l'écriture")
    print(f"   sur son entrée d'élection = theta ; gain typique du bruit sur une entrée unitaire = sigma sqrt(n) = {bbp:.1f}")
    for t in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0]:
        alt = simule(n, sigma, "rang1", t * bbp, rng, 200)
        pw = (alt > seuils).mean(axis=0)
        print(f"     theta = {t:>4.1f} x sigma sqrt(n) = {t * bbp:7.1f} : {pw[0]:.2f} | {pw[1]:.2f} | {pw[2]:.2f}")
    print(f"   creuse (8 coefficients dans une colonne), h en unités de sigma ; seuil du maximum attendu")
    print(f"   sigma sqrt(2 ln(n^2)) = {sigma * math.sqrt(2 * math.log(n * n)):.2f}")
    for h in [2.0, 3.0, 4.0, 5.0, 6.0, 8.0]:
        alt = simule(n, sigma, "creuse", h * sigma, rng, 200)
        pw = (alt > seuils).mean(axis=0)
        print(f"     h = {h:>4.1f} sigma (gain {h * math.sqrt(8):5.1f}) : {pw[0]:.2f} | {pw[1]:.2f} | {pw[2]:.2f}")
print("   Lecture : une écriture de rang un passe sous le test spectral tant que theta reste sous ~ sigma sqrt(n),")
print("   c'est-à-dire tant que son gain sur son entrée d'élection ne dépasse pas celui du bruit de re-dérivation")
print("   sur une entrée quelconque ; une écriture creuse passe tant que ses coefficients restent sous")
print("   ~ sigma sqrt(2 ln n^2). Le bruit de re-dérivation fixe donc la taille de ce qui peut se cacher ;")
print("   à re-dérivation exacte (sigma = 0), rien ne se cache. Exprimé relativement : si sigma = rho * s, où s est")
print("   l'échelle des coefficients appris, l'écriture cachée change la sortie de la couche d'au plus ~ rho fois")
print("   sa sortie typique, le long d'une seule direction.")
print()

# ---------------------------------------------------------------- E
print("E. Lecteurs de poids publiés pris comme portes (comptes recalculés depuis les pourcentages publiés).")


def cp(x, n, conf=0.95):
    lo = stats.beta.ppf((1 - conf) / 2, x, n - x + 1) if x > 0 else 0.0
    hi = stats.beta.ppf(1 - (1 - conf) / 2, x + 1, n - x) if x < n else 1.0
    return lo, hi


# arXiv 2611.15118, tableau 5 (p. 16) : 114 modifiés, 103 propres.
opus = {"mod_juge_mod": 64, "mod_juge_propre": 47, "mod_sans": 3, "propre_juge_mod": 2, "propre_juge_propre": 96, "propre_sans": 5}
assert abs(64 / 114 - 0.5614) < 5e-4 and abs(47 / 114 - 0.4123) < 5e-4 and abs(2 / 103 - 0.0194) < 5e-4 and abs(96 / 103 - 0.9320) < 5e-4
print("   Lecteur généraliste (tableau 5, p. 16), audit direct sans référence, 114 modifiés / 103 propres :")
for nom, x, n in [("modifié jugé modifié", 64, 114), ("modifié jugé propre", 47, 114), ("propre jugé modifié", 2, 103), ("propre jugé propre", 96, 103)]:
    lo, hi = cp(x, n)
    print(f"     {nom:<22} {x:>3}/{n} = {x / n:6.2%}  [IC 95 % exact {lo:6.2%} ; {hi:6.2%}]")
# Détecteur à traits (tableau 6, p. 17) : 35 modifiés, 31 propres, seuil 0,5.
tp, nm, fp, npr = 32, 35, 3, 31
assert abs(tp / nm - 0.9143) < 5e-4 and abs(fp / npr - 0.0968) < 5e-4
print("   Détecteur à cinq traits (tableau 6, p. 17), 35 modifiés / 31 propres de test :")
for nom, x, n in [("vrais positifs", tp, nm), ("fausses alertes", fp, npr)]:
    lo, hi = cp(x, n)
    print(f"     {nom:<22} {x:>3}/{n} = {x / n:6.2%}  [IC 95 % exact {lo:6.2%} ; {hi:6.2%}]")
print("   Risque résiduel P(falsifié | laissé passer) et précision P(falsifié | alerte), selon la part pi de falsifiés :")
for pi in [0.001, 0.01, 0.10]:
    # lecteur généraliste : « laissé passer » = jugé propre (les sans-décision sont envoyés à l'audit)
    tpr_o, fnr_o = 64 / 114, 47 / 114
    fpr_o, tnr_o = 2 / 103, 96 / 103
    res_o = fnr_o * pi / (fnr_o * pi + tnr_o * (1 - pi))
    pre_o = tpr_o * pi / (tpr_o * pi + fpr_o * (1 - pi))
    tpr_f, fpr_f = tp / nm, fp / npr
    res_f = (1 - tpr_f) * pi / ((1 - tpr_f) * pi + (1 - fpr_f) * (1 - pi))
    pre_f = tpr_f * pi / (tpr_f * pi + fpr_f * (1 - pi))
    print(f"     pi = {pi:5.1%} : généraliste, résiduel {res_o:7.3%} (÷{pi / res_o:4.1f}), précision {pre_o:6.1%} ;"
          f" traits, résiduel {res_f:7.4%} (÷{pi / res_f:5.1f}), précision {pre_f:6.1%}")
print("   Lecture : aucun des deux n'est une porte ; tous deux réduisent le risque et orientent l'audit.")
print("   Les traits sont tirés de la construction de l'attaque ; rien ne dit qu'ils tiennent contre une autre.")
print()
print("   Réplication publique (arXiv 2611.21449, p. 13-14), lecture des poids en texte, choix entre deux modèles :")
for nom, x, n in [("empoisonné pendant l'entraînement", 10, 10), ("empoisonné après coup", 7, 10), ("adaptateur malveillant", 23, 32)]:
    pval = stats.binom.sf(x - 1, n, 0.5)
    print(f"     {nom:<34} {x:>2}/{n} : P(X >= {x} | hasard) = {pval:.4f}")
print("   Lecture : le lecteur trouve le modèle entraîné à part (il diffère partout), pas l'empoisonnement ;")
print("   l'écart d'entraînement, et non la trace de l'attaque, porte le signal : c'est le confondant que")
print("   le jumeau honnête entraîné à l'identique sert à retirer.")
print()

# ---------------------------------------------------------------- F
print("F. Écritures fragmentées : k retouches successives, chacune sous le seuil d'un audit par retouche.")
print("   Ordre de grandeur sous la loi du bord du spectre (asymptotique, supposée) : bruit honnête i.i.d. par")
print("   retouche d'écart sigma ; après k retouches, bruit cumulé d'écart sigma sqrt(k) ; seuil spectral")
print("   tau_k = c sigma sqrt(k n), c ~ 1,5 pour une puissance proche de 1 (bloc D). Retouches alignées de")
print("   taille theta_1 : écriture cumulée k theta_1. L'audit du cumul contre le dernier état de confiance la")
print("   voit dès que k theta_1 >= c sigma sqrt(k n), soit k >= (c sigma sqrt(n) / theta_1)^2.")
for frac in [0.5, 0.3, 0.1, 0.03]:
    k_min = math.ceil((1 / frac) ** 2)
    print(f"   theta_1 = {frac:>4.2f} x seuil d'une retouche : cumul vu dès k = {k_min:>5} retouches")
print("   Lecture : l'écriture alignée croît comme k, le bruit honnête comme sqrt(k) ; l'audit de chaque retouche")
print("   seule ne voit rien, l'audit du cumul finit par voir. C'est l'additivité du programme transportée aux")
print("   poids ; elle suppose un bruit honnête sans dérive commune et une écriture de direction stable.")
