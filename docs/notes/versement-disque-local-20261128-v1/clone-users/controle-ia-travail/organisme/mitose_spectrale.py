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
        for tok in sorted(set(d)):
            df[tok] += 1

    vecteurs = []
    for d in docs:
        tf = Counter(d)
        vec = {}
        norme_sq = 0.0
        for tok in sorted(tf):
            c = tf[tok]
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
    seuil_sat = max(2, int(0.75 * n))
    candidats_sat = sorted(
        [(tok, c) for tok, c in df.items() if n > 1 and c >= seuil_sat],
        key=lambda kv: (-kv[1], kv[0]),
    )
    termes_satures = [tok for tok, _ in candidats_sat[:6]]

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


MOTS_VIDES_SPECTRAUX_V63 = {
    "dans", "pour", "avec", "sans", "plus", "moins", "comme", "cette", "sont", "mais",
    "tout", "tous", "toute", "toutes", "une", "des", "les", "aux", "sur", "par", "que",
    "qui", "est", "pas", "son", "ses", "leur", "leurs", "entre", "vers", "sous", "tres",
    "meme", "aussi", "donc", "ainsi", "alors", "apres", "avant", "depuis", "contre",
    "the", "and", "for", "with", "from", "that", "this", "have", "which", "their",
    "are", "was", "were", "been", "being", "into", "over", "under", "between", "through",
    "confiance", "incertitude", "position", "caste", "castes", "question", "reponse",
    "etiquette", "constat", "article", "articles", "modele", "modeles", "analyse",
    "attaque", "colmatage", "faille", "failles", "protocole", "seuil", "metrique",
    "aire", "aires", "angles", "canisme", "canique", "cha", "art", "auto", "bruit",
}


def extraire_transitions_saturees_et_pivots_swanson(textes_castes: list, top_k: int = 6) -> dict:
    if not textes_castes:
        return {"transitions_saturees": [], "pivots_swanson_proteges": []}
    transitions_doc = {}
    voisins_mot = {}
    freq_doc_mot = {}

    for txt in textes_castes:
        mots = [
            m for m in re.findall(r"[a-zA-Z0-9_-]{5,}", (txt or "").lower())
            if m not in MOTS_VIDES_SPECTRAUX_V63
        ]
        vus_transitions = set()
        vus_mots = set(mots)
        for m in vus_mots:
            freq_doc_mot[m] = freq_doc_mot.get(m, 0) + 1
            if m not in voisins_mot:
                voisins_mot[m] = set()
        for i in range(len(mots) - 1):
            a, b = mots[i], mots[i + 1]
            if a == b:
                continue
            paire = f"{a}->{b}"
            vus_transitions.add(paire)
            voisins_mot[a].add(b)
            voisins_mot[b].add(a)
        for p in vus_transitions:
            transitions_doc[p] = transitions_doc.get(p, 0) + 1

    trans_triees = sorted(transitions_doc.items(), key=lambda kv: (-kv[1], kv[0]))
    transitions_saturees = [k for k, v in trans_triees if v >= 2][:top_k]
    if not transitions_saturees:
        transitions_saturees = [k for k, _ in trans_triees[:top_k]]

    scores_pivot = []
    for m, f_doc in freq_doc_mot.items():
        nb_voisins = len(voisins_mot.get(m, ()))
        if f_doc >= 1 and nb_voisins >= 2:
            scores_pivot.append((nb_voisins / float(1 + f_doc), m))
    scores_pivot.sort(key=lambda x: (-x[0], x[1]))
    pivots_proteges = [m for _, m in scores_pivot[:top_k]]

    return {
        "transitions_saturees": transitions_saturees,
        "pivots_swanson_proteges": pivots_proteges,
    }


_calculer_capacite_shannon_gram_v621 = calculer_capacite_shannon_gram


def calculer_capacite_shannon_gram(textes_castes: list, rapport_signal_bruit: float = 8.0) -> dict:
    bilan = dict(_calculer_capacite_shannon_gram_v621(textes_castes, rapport_signal_bruit=rapport_signal_bruit))
    if not textes_castes:
        bilan["transitions_saturees"] = []
        bilan["pivots_swanson_proteges"] = []
        return bilan
    info_lignes = extraire_transitions_saturees_et_pivots_swanson(textes_castes, top_k=6)
    pivots_set = set(info_lignes["pivots_swanson_proteges"][:2])

    compteur_doc = {}
    for txt in textes_castes:
        mots_uniques = {
            m for m in re.findall(r"[a-zA-Z0-9_-]{5,}", (txt or "").lower())
            if m not in MOTS_VIDES_SPECTRAUX_V63
        }
        for m in mots_uniques:
            compteur_doc[m] = compteur_doc.get(m, 0) + 1
    tri = sorted(compteur_doc.items(), key=lambda kv: (-kv[1], kv[0]))
    satures_propres = [k for k, c in tri if c >= 2 and k not in pivots_set][:6]
    if not satures_propres:
        satures_propres = [k for k, _ in tri if k not in pivots_set][:6]

    bilan["termes_satures"] = satures_propres
    bilan["transitions_saturees"] = info_lignes["transitions_saturees"]
    bilan["pivots_swanson_proteges"] = info_lignes["pivots_swanson_proteges"]
    return bilan
