import math
import re
from collections import Counter


def calculer_capacite_shannon_gram(textes: list, snr: float = 4.0) -> dict:
    docs = [re.findall(r"[a-zA-Z0-9_]{3,}", str(t).lower()) for t in textes if str(t).strip()]
    n = len(docs)
    if n == 0:
        return {"n_textes": 0, "capacite_shannon": 0.0, "gain_marginal": 0.0, "termes_satures": []}

    df = Counter()
    for d in docs:
        for tok in set(d):
            df[tok] += 1

    vecteurs = []
    for d in docs:
        tf = Counter(d)
        vec = {}
        norme_sq = 0.0
        for tok, c in tf.items():
            idf = math.log(1.0 + (n / float(df[tok])))
            w = float(c) * idf
            vec[tok] = w
            norme_sq += w * w
        norme = math.sqrt(norme_sq) if norme_sq > 1e-12 else 1.0
        vecteurs.append({k: v / norme for k, v in vec.items()})

    trace_g = float(n)
    somme_hors_diag_sq = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            vi, vj = vecteurs[i], vecteurs[j]
            sim = sum(val * vj.get(k, 0.0) for k, val in vi.items())
            somme_hors_diag_sq += 2.0 * (sim * sim)

    similarite_moyenne = math.sqrt(somme_hors_diag_sq / max(1.0, float(n * (n - 1)))) if n > 1 else 0.0
    rang_effectif = trace_g / (1.0 + (n - 1) * similarite_moyenne) if n > 1 else 1.0
    capacite = rang_effectif * math.log(1.0 + snr)
    gain_marginal = capacite / float(n)
    termes_satures = [tok for tok, c in df.most_common(6) if n > 1 and c >= max(2, int(0.75 * n))]

    return {
        "n_textes": n,
        "capacite_shannon": round(capacite, 6),
        "gain_marginal": round(gain_marginal, 6),
        "similarite_moyenne": round(similarite_moyenne, 6),
        "termes_satures": termes_satures,
    }


def planifier_castes_par_mitose(especes_disponibles: list, budget: dict, n_taches: int, historique: list) -> list:
    especes = [str(e) for e in especes_disponibles if str(e).strip()]
    if not especes:
        return []

    appels_restants = int(budget.get("appels_restants", budget.get("appels_max", 0)) or 0)
    if appels_restants <= 0:
        return []

    reserve_entrainement = min(6, max(1, appels_restants // 4))
    appels_pour_test = max(1, appels_restants - reserve_entrainement)
    budget_par_tache = max(1, appels_pour_test // max(1, n_taches))

    pression_exploration = 1
    if len(historique) >= 2:
        scores = [float(h.get("score", 0.0) or 0.0) for h in historique if h.get("score") is not None]
        if len(scores) >= 2 and (scores[-1] - scores[-2]) <= 0.01:
            pression_exploration = 2

    nb_castes_cible = min(max(1, budget_par_tache), min(5, len(especes) + pression_exploration))

    castes = []
    for idx in range(nb_castes_cible):
        espece = especes[idx % len(especes)]
        if idx == 0:
            role = "monoculture_analytique"
            mode = "MONOCULTURE"
        elif idx == 1 and len(especes) > 1:
            role = "monoculture_croisee"
            mode = "MONOCULTURE"
        elif idx == 2:
            role = "sonde_orthogonale_onsager"
            mode = "HYBRIDE" if len(especes) > 1 else "MONOCULTURE"
        else:
            role = f"arbitre_contradictoire_{idx}"
            mode = "HYBRIDE" if len(especes) > 1 else "MONOCULTURE"
        castes.append({
            "id_caste": idx + 1,
            "espece": espece,
            "mode": mode,
            "role": role,
        })
    return castes


def planifier_castes_question_ouverte(especes_disponibles: list, budget: dict, historique: list) -> list:
    """Version 4 : recrute de 1 a 5 castes pour traiter une question ouverte selon le budget restant et l'historique."""
    especes = [str(e) for e in especes_disponibles if str(e).strip()]
    if not especes:
        return []

    appels_restants = int(budget.get("appels_restants", budget.get("appels_max", 0)) or 0)
    if appels_restants <= 0:
        return []

    pression_exploration = 1
    if len(historique) >= 2:
        scores = [float(h.get("score", 0.0) or 0.0) for h in historique if h.get("score") is not None]
        if len(scores) >= 2 and (scores[-1] - scores[-2]) <= 0.01:
            pression_exploration = 2

    cible = min(appels_restants, min(5, max(2, len(especes) + pression_exploration + 1)))
    if appels_restants == 1:
        cible = 1

    catalogue_roles = [
        ("monoculture_analytique", "MONOCULTURE", "Analyse initiale et decomposition formelle de la question"),
        ("monoculture_croisee", "MONOCULTURE", "Seconde perspective independante et verification des premisses"),
        ("sonde_orthogonale_onsager", "HYBRIDE", "Exploration orthogonale hors des termes satures et contre-exemples"),
        ("critique_adversariale_limites", "HYBRIDE", "Identification des angles morts, cas limites et conditions de refutation"),
        ("arbitre_synthese_contradictoire", "HYBRIDE", "Arbitrage des votes, synthese contradictoire et redaction finale"),
    ]

    castes = []
    for idx in range(cible):
        espece = especes[idx % len(especes)]
        if idx == cible - 1 and cible >= 3:
            role_nom, mode_def, axe = catalogue_roles[-1]
        else:
            role_nom, mode_def, axe = catalogue_roles[min(idx, len(catalogue_roles) - 2)]
        mode = mode_def if len(especes) > 1 else "MONOCULTURE"
        castes.append({
            "id_caste": idx + 1,
            "espece": espece,
            "mode": mode,
            "role": role_nom,
            "axe": axe,
        })
    return castes