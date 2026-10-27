"""Pari apparié borné (v7, version 20) — le second type d'engagement du pôle, pour les affirmations globales (H1, H2, H3,
G1), selon la conception v5 (`../../pari-de-signe/conception-pari-de-signe-v5.md` et les versions qu'elle amende).

Ce module ne contient que le **cœur statistique**, sans lien encore avec le cycle des générations (à faire : monde sur
banque de scores, engagement, mémoire avec la clé complète de l'héritage) :

- un **contraste** v(t) = a₀ + Σ a_c·r_c(t) sur des parts r_c ∈ [0 ; 1], borné dans [−1 ; 1] par la **règle double**
  (somme des coefficients positifs plus la constante ≤ 1 ; somme des valeurs absolues des négatifs moins la constante ≤ 1) ;
- la **richesse** en forme « parts » seule : W_n = moyenne sur Λ de Π (1 + λ·v(t)), surmartingale positive sous
  « E[v] ≤ 0, unités indépendantes et de même loi » (inégalité de Ville) ; la forme « signe » n'existe pas ici ;
- la **garde** appariée sur les faux positifs : processus de 1 + λ·(δ − g(t)) contre « E[g] ≥ δ » ;
- l'**e-valeur de la fiche** = minimum des processus (contraste contre chaque comparateur — intersection-union — et
  garde), **arrêtée** au premier instant où elle atteint le seuil (m_g/α_g pour la règle e-BH de la génération) ;
- la variante **sans remise** (banque entière) ;
- une **borne basse** de confiance à tout instant pour E[v] (rapport), par inversion des paris sur une grille de θ.

Tout est en Python pur (aucune dépendance) ; les instants de lecture sont les unités (une unité = un instant).
"""

import math

LAMBDAS = (0.1, 0.3, 0.6, 0.9)


class ContrasteInvalide(ValueError):
    pass


def verifier_coefficients(coefficients, constante=0.0):
    """Règle double (conception v2, constat C11 de sa contre-lecture) : v ∈ [−1 ; 1] pour toutes parts dans [0 ; 1]."""
    if not coefficients:
        raise ContrasteInvalide("contraste sans cellule")
    for cellule, a in coefficients.items():
        if not isinstance(a, (int, float)) or isinstance(a, bool) or not math.isfinite(a):
            raise ContrasteInvalide(f"coefficient non numérique pour {cellule!r}")
    positifs = sum(a for a in coefficients.values() if a > 0)
    negatifs = sum(-a for a in coefficients.values() if a < 0)
    if positifs + constante > 1 + 1e-12 or negatifs - constante > 1 + 1e-12:
        raise ContrasteInvalide(f"règle double violée : positifs + constante = {positifs + constante:.6g}, "
                                f"négatifs − constante = {negatifs - constante:.6g} (chacun ≤ 1)")
    return True


def contraste(parts, coefficients, constante=0.0):
    """v = a₀ + Σ a_c·r_c pour une unité ; `parts` : cellule → part dans [0 ; 1]."""
    v = constante
    for cellule, a in coefficients.items():
        r = parts[cellule]
        if not 0.0 <= r <= 1.0:
            raise ContrasteInvalide(f"part hors de [0 ; 1] pour {cellule!r} : {r}")
        v += a * r
    return max(-1.0, min(1.0, v))


def _verifier_lambdas(lambdas):
    if not lambdas or any(not 0.0 < l < 1.0 for l in lambdas):
        raise ValueError("Λ : mises dans ]0 ; 1[")


def trajectoire_log_richesse(valeurs, lambdas=LAMBDAS):
    """log de la richesse mélangée (moyenne sur Λ de Π (1 + λ·v)) après chaque unité ; v dans [−1 ; 1]."""
    _verifier_lambdas(lambdas)
    logs = [0.0] * len(lambdas)
    sortie = []
    for v in valeurs:
        if not -1.0 <= v <= 1.0:
            raise ContrasteInvalide(f"valeur hors de [−1 ; 1] : {v}")
        logs = [lw + math.log1p(l * v) for lw, l in zip(logs, lambdas)]
        m = max(logs)
        sortie.append(m + math.log(sum(math.exp(lw - m) for lw in logs) / len(lambdas)))
    return sortie


def trajectoire_log_garde(ecarts_faux_positifs, delta, lambdas=LAMBDAS):
    """Garde appariée : processus de 1 + λ·(δ − g) contre « E[g] ≥ δ » (A tire plus que B d'au moins δ)."""
    if not 0.0 < delta < 1.0:
        raise ValueError("δ dans ]0 ; 1[")
    return trajectoire_log_richesse([max(-1.0, min(1.0, delta - g)) for g in ecarts_faux_positifs], lambdas)


def trajectoire_log_sans_remise(valeurs, lambdas=LAMBDAS):
    """Variante « banque entière » : facteur 1 + λ_t·(v(t) − μ_t), μ_t = −(Σ passé)/(n − t + 1), λ_t ≤ λ·(n − t + 1)/n ;
    nul « moyenne des v de la banque ≤ 0 », l'ordre de lecture étant tiré uniformément (ordre secret du noyau)."""
    _verifier_lambdas(lambdas)
    n = len(valeurs)
    logs = [0.0] * len(lambdas)
    somme, sortie = 0.0, []
    for t, v in enumerate(valeurs, 1):
        mu = -somme / (n - t + 1)
        for i, l in enumerate(lambdas):
            lt = l * (n - t + 1) / n
            logs[i] += math.log(max(1e-300, 1.0 + lt * (v - mu)))
        somme += v
        m = max(logs)
        sortie.append(m + math.log(sum(math.exp(lw - m) for lw in logs) / len(lambdas)))
    return sortie


def evaluer(contrastes_par_comparateur, ecarts_faux_positifs=None, delta=None, alpha=0.05, m=1, lambdas=LAMBDAS):
    """E-valeur d'une fiche appariée.

    `contrastes_par_comparateur` : {comparateur: [v(t) par unité]} — l'affirmation « bat chaque comparateur »
    (intersection-union : promotion si **tous** les processus atteignent le seuil ; sous le nul « il existe un comparateur
    k avec E[v_k] ≤ 0 », le minimum est dominé par la surmartingale de ce k : niveau α sans correction de multiplicité).
    `ecarts_faux_positifs` et `delta` : la garde (facultative) ; elle entre dans le minimum.
    Les suites sont lues en parallèle, unité par unité (même ordre, même longueur pour les contrastes ; la garde peut avoir
    sa propre longueur : ses unités sont les unités honnêtes, révélées dans le même ordre secret).
    Le processus est **arrêté** au premier instant où le minimum atteint log(m/α) (temps d'arrêt : e-valeur valide sous la
    règle e-BH au niveau α avec m fiches)."""
    if not contrastes_par_comparateur:
        raise ValueError("au moins un comparateur")
    longueurs = {len(v) for v in contrastes_par_comparateur.values()}
    if len(longueurs) != 1:
        raise ValueError("les contrastes des comparateurs doivent porter sur les mêmes unités")
    seuil = math.log(m / alpha)
    trajs = {k: trajectoire_log_richesse(v, lambdas) for k, v in contrastes_par_comparateur.items()}
    garde = None
    if ecarts_faux_positifs is not None:
        if delta is None:
            raise ValueError("garde sans δ")
        garde = trajectoire_log_garde(ecarts_faux_positifs, delta, lambdas)
    n = longueurs.pop()
    n_total = max(n, len(garde) if garde is not None else 0)
    minimum, arret = [], None
    for t in range(n_total):
        valeurs = [traj[min(t, n - 1)] if n else 0.0 for traj in trajs.values()]
        if garde is not None:
            valeurs.append(garde[min(t, len(garde) - 1)] if garde else 0.0)
        mt = min(valeurs)
        minimum.append(mt)
        if arret is None and mt >= seuil:
            arret = t + 1
    log_e = minimum[arret - 1] if arret else (minimum[-1] if minimum else 0.0)
    return {"trajectoire_log_min": minimum, "seuil_log": seuil, "promue": arret is not None, "instant_d_arret": arret,
            "log_e_valeur": log_e, "log_richesse_finale_par_comparateur": {k: (v[-1] if v else 0.0) for k, v in trajs.items()},
            "log_garde_finale": (garde[-1] if garde else None), "unites": n}


def borne_basse(valeurs, alpha=0.05, lambdas=LAMBDAS, pas=0.01):
    """Borne basse de confiance, valide à tout instant, pour E[v] (v dans [−1 ; 1]) : le plus grand θ de la grille dont le
    nul « E[v] ≤ θ » est rejeté (richesse de 1 + λ_θ·(v − θ) ≥ 1/α à un instant), avec λ_θ = λ/(1 + θ) pour garder le
    facteur positif. Rapportée, jamais une condition de promotion à elle seule."""
    _verifier_lambdas(lambdas)
    seuil = math.log(1 / alpha)
    meilleur = -1.0
    theta = -1.0 + pas
    while theta < 1.0 - 1e-9:
        logs = [0.0] * len(lambdas)
        rejete = False
        for v in valeurs:
            for i, l in enumerate(lambdas):
                logs[i] += math.log1p((l / (1.0 + theta)) * (v - theta))
            m = max(logs)
            if m + math.log(sum(math.exp(lw - m) for lw in logs) / len(lambdas)) >= seuil:
                rejete = True
                break
        if rejete:
            meilleur = theta
        else:
            break  # le nul E[v] ≤ θ n'est pas rejeté : aucun θ plus grand ne le sera (monotonie en θ)
        theta = round(theta + pas, 10)
    return meilleur
