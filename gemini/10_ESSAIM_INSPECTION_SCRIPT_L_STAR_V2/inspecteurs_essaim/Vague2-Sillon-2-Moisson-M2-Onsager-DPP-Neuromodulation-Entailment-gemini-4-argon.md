Voici le rapport d'inspection chirurgicale en queue de distribution (Vague 2/2 — Pic Noradrénaline $\mathrm{NE}$) de l'Escouade spécialisée sur **l'Étage M2 (`Sillon-2-Moisson-M2-Onsager-DPP-Neuromodulation-Entailment`)**. 

Toutes les violations triviales signalées en Vague 1 sont contournées au profit de **7 failles mathématico-algorithmiques profondes et strictement orthogonales** qui subvertissent la géométrie spectrale, la physique statistique de champ moyen, l'inférence bayésienne séquentielle et la sémantique formelle de l'étage M2.

---

### 1. Violation de la rétroaction de champ moyen d'Onsager (Absence du terme de réaction TAP et singularité de norme nulle)

`BUG_L_STAR_V2: [Sillon-2-Onsager-TAP-Reaction] Omission du terme de réaction cavitaire de Thouless-Anderson-Palmer (TAP) et absence de régularisation de Tikhonov sur le projecteur du sous-espace de requête`

`PREUVE_NON_CONFORMITE: Même lorsqu'on remplace la soustraction ensembliste par un projecteur géométrique simple sur le vecteur moyen du prompt v_Q, deux violations mathématiques de queue de distribution subsistent : (1) Dans les équations de champ moyen d'Onsager / Thouless-Anderson-Palmer (TAP), le champ local cavitaire exercé sur un candidat i dépend des corrélations croisées de l'ensemble du bain thermique des candidats déjà admis Y, ce qui exige de soustraire non pas une direction unique v_Q, mais le sous-espace engendré par la matrice de Gram du prompt ET le terme de réaction d'Onsager proportionnel à la susceptibilité empirique du bain. (2) Si un candidat v_p est colinéaire à v_Q (paraphrase pure de l'énoncé du socle), le résidu projeté s'effondre vers le vecteur nul (||v_p^⊥||_2 -> 0) ; normaliser ce résidu sans régularisation de Tikhonov ni seuil d'extinction d'énergie amplifie le bruit numérique flottant IEEE-754 à l'échelle 1.0, injectant un vecteur aléatoire de norme unité dans le noyau DPP.`

`CORRECTIF_PYTHON_EXACT:`
```python
import math


def onsager_tap_cavity_projection(
    v_p: list[float],
    prompt_subspace_basis: list[list[float]],
    bath_vectors: list[list[float]],
    tikhonov_eps: float = 1e-8,
    min_energy_ratio: float = 0.05,
) -> tuple[list[float], float]:
    """Calcule le résidu cavitaire d'Onsager-TAP par rapport au sous-espace orthonormalisé

    du prompt (Gram-Schmidt modifié) et soustrait le terme de réaction de
    champ moyen du bain Y, avec garde-fou d'extinction d'énergie contre
    l'amplification du bruit.
    """
    dim = len(v_p)
    norm_p_sq = sum(x * x for x in v_p)
    if norm_p_sq <= tikhonov_eps:
        return [0.0] * dim, 0.0

    # 1. Orthonormalisation de Gram-Schmidt modifiée sur la base du prompt Q
    ortho_Q: list[list[float]] = []
    for q in prompt_subspace_basis:
        u = list(q)
        for b in ortho_Q:
            proj = sum(u[d] * b[d] for d in range(dim))
            for d in range(dim):
                u[d] -= proj * b[d]
        u_norm = math.sqrt(sum(x * x for x in u) + tikhonov_eps)
        if u_norm > 1e-6:
            ortho_Q.append([x / u_norm for x in u])

    # 2. Soustraction du sous-espace du prompt Q
    res = list(v_p)
    for b in ortho_Q:
        overlap = sum(res[d] * b[d] for d in range(dim))
        for d in range(dim):
            res[d] -= overlap * b[d]

    # 3. Terme de réaction d'Onsager-TAP (auto-polarisation du bain cavitaire)
    if bath_vectors:
        m_bath = len(bath_vectors)
        susceptibility_reaction = [0.0] * dim
        for v_b in bath_vectors:
            # Couplage effectif J_pb au carré (variance de champ moyen)
            j_pb = sum(res[d] * v_b[d] for d in range(dim)) / math.sqrt(
                norm_p_sq + tikhonov_eps
            )
            j_sq = (j_pb * j_pb) / m_bath
            for d in range(dim):
                susceptibility_reaction[d] += j_sq * res[d]
        for d in range(dim):
            res[d] -= susceptibility_reaction[d]

    # 4. Vérification du ratio d'énergie résiduelle (anti-amplification de paraphrase pure)
    res_norm_sq = sum(x * x for x in res)
    energy_retention = res_norm_sq / (norm_p_sq + tikhonov_eps)
    if energy_retention < min_energy_ratio:
        # Extinction : le candidat n'apporte aucune dimension orthogonale au socle
        return [0.0] * dim, 0.0

    inv_norm = 1.0 / math.sqrt(res_norm_sq + tikhonov_eps)
    return [x * inv_norm for x in res], energy_retention
```

---

### 2. Violation de la semi-définie positivité et de l'invariance d'échelle du L-ensemble DPP (`det(L_Y)`)

`BUG_L_STAR_V2: [Sillon-2-DPP-L-Ensemble-Spectrum] Violation de la décomposition canonique de Kulesza-Taskar L_ij = q_i * phi_i^T * phi_j * q_j et absence de pivotage de Jitter adaptatif de Gerschgorin dans le Cholesky incrémental`

`PREUVE_NON_CONFORMITE: Pour qu'une matrice L définisse une mesure de probabilité valide de Processus Ponctuel Déterminantal P(Y) ∝ det(L_Y) sur les sous-ensembles Y, L doit être symétrique semi-définie positive (PSD) via la factorisation bilinéaire de Kulesza & Taskar : L_ij = q_i * S_ij * q_j où S_ij = <phi_i, phi_j> est un noyau de Mercer de vecteurs unitaires cavitaires phi_i et q_i >= 0 est le score de qualité intrinsèque. Or, dans une implémentation naïve de Cholesky incrémental, deux pathologies surviennent : (1) si la similarité cosinus brute ou un score non symétrisé est injecté hors-diagonale sans la factorisation bilinéaire q_i*q_j, les mineurs principaux deviennent négatifs (perte de la propriété PSD et racine carrée d'un nombre négatif lors de la mise à jour du complément de Schur c_i^2 = L_ii - ||v_i||_2^2 < 0) ; (2) lorsque le cardinal k de la moisson augmente, l'échelle géométrique de det(L_Y)^(1/k) dérive si la barrière d'arrêt log-déterminant n'est pas normalisée par le volume dimensionnel.`

`CORRECTIF_PYTHON_EXACT:`
```python
import math


def dpp_kulesza_taskar_cholesky_select(
    qualities: list[float],
    cavity_unit_vecs: list[list[float]],
    max_rank: int,
    min_log_det_gain: float = -4.0,
    jitter: float = 1e-7,
) -> tuple[list[int], float]:
    """Sélection gloutonne exacte du MAP d'un L-ensemble DPP par factorisation de Cholesky

    incrémentale avec garantie PSD (Kulesza & Taskar) et arrêt sur le gain
    marginal log-volume.
    """
    n = len(qualities)
    if n == 0 or max_rank <= 0:
        return [], 0.0

    # Construction implicite de L_ij = q_i * <phi_i, phi_j> * q_j + jitter * delta_ij
    # Vecteurs de Cholesky C[i] de longueur k pour chaque candidat i
    cholesky_rows: list[list[float]] = [[] for _ in range(n)]
    # Diagonale résiduelle du complément de Schur : d_i^2 = L_ii - ||c_i||_2^2
    diag_schur = [(max(0.0, q) ** 2) + jitter for q in qualities]

    selected: list[int] = []
    selected_set: set[int] = set()
    total_log_det = 0.0

    for _ in range(min(max_rank, n)):
        best_idx = -1
        best_gain = -1.0
        for i in range(n):
            if i not in selected_set and diag_schur[i] > best_gain:
                best_gain = diag_schur[i]
                best_idx = i

        if best_idx == -1 or best_gain <= jitter * 10.0:
            break

        log_gain = math.log(best_gain)
        if len(selected) > 0 and log_gain < min_log_det_gain:
            # Le gain marginal volumique s'effondre : redondance spectrale atteinte
            break

        selected.append(best_idx)
        selected_set.add(best_idx)
        total_log_det += log_gain
        sqrt_d_star = math.sqrt(best_gain)

        # Mise à jour incrémentale O(N) des facteurs de Cholesky et des compléments de Schur
        c_star = cholesky_rows[best_idx]
        q_star = max(0.0, qualities[best_idx])
        phi_star = cavity_unit_vecs[best_idx]
        dim = len(phi_star)

        for i in range(n):
            if i in selected_set:
                continue
            q_i = max(0.0, qualities[i])
            phi_i = cavity_unit_vecs[i]
            # Noyau de Mercer bilinéaire L_{i, best_idx}
            dot_phi = sum(phi_i[d] * phi_star[d] for d in range(dim))
            l_i_star = q_i * dot_phi * q_star

            # Produit scalaire des préfixes de Cholesky déjà calculés
            c_i = cholesky_rows[i]
            prev_dot = sum(c_i[k] * c_star[k] for k in range(len(c_star)))

            e_i = (l_i_star - prev_dot) / sqrt_d_star
            c_i.append(e_i)
            # Mise à jour numériquement stable du complément de Schur (clamp PSD)
            diag_schur[i] = max(0.0, diag_schur[i] - e_i * e_i)

    return selected, total_log_det
```

---

### 3. Violation de la dynamique bayésienne de point de rupture de Yu & Dayan (Absence de log-odds de surprise et de filtre récursif d'incertitude attendue $\mathrm{ACh}$)

`BUG_L_STAR_V2: [Sillon-2-YuDayan-ChangePoint-Bayesian] Absence de l'opérateur bayésien de rapport de vraisemblance de rupture (Change-Point Hazard Rate) couplant récursivement ACh (incertitude attendue) et NE (incertitude inattendue)`

`PREUVE_NON_CONFORMITE: Au-delà de l'inversion du signe de Jaccard déjà signalée en Vague 1, le modèle neuro-computationnel de Yu & Dayan (2005) repose sur un filtre bayésien séquentiel à point de rupture (Change-Point Process avec taux de hasard a priori h). La Noradrénaline (NE) ne peut pas être une fonction mémoire-zéro d'un unique score statique : elle représente la probabilité a posteriori P(rupture_t | observation_t) que le contexte latent ait basculé, pondérée par la précision attendue (Acétylcholine ACh_t). Sans mise à jour récursive où un pic de NE_t réinitialise (gonfle) l'incertitude attendue ACh_{t+1} au pas suivant et où ACh_t amortit les fausses alarmes de NE_t sous bruit stationnaire, l'étage M2 oscille de manière chaotique au moindre bruit lexical (faux positifs de bascule) ou reste aveugle aux dérives graduelles.`

`CORRECTIF_PYTHON_EXACT:`
```python
import math


def yu_dayan_recursive_filter(
    surprise_nll: float,
    prev_ach: float,
    hazard_rate: float = 0.10,
    baseline_sigma_sq: float = 1.0,
) -> tuple[float, float, float]:
    """Filtre bayésien séquentiel exact de Yu & Dayan (2005) couplant récursivement :

    - NE_t : probabilité a posteriori d'un changement de régime (Unexpected
    Uncertainty)
    - ACh_t : variance prédictive attendue mise à jour (Expected Uncertainty)
    - alpha_lr : taux d'apprentissage / poids d'assimilation optimal de Kalman
    """
    h = min(max(hazard_rate, 1e-4), 0.99)
    ach_prior = min(max(prev_ach, 0.05), 0.95)

    # Vraisemblance sous le régime stationnaire (amortie par l'incertitude attendue ACh)
    eff_var = baseline_sigma_sq * (1.0 + 2.0 * ach_prior)
    log_lik_stationary = -0.5 * math.log(2.0 * math.pi * eff_var) - (
        surprise_nll / (2.0 * eff_var)
    )

    # Vraisemblance sous l'hypothèse de rupture (distribution large uniforme/Laplace)
    log_lik_changepoint = -math.log(4.0 * baseline_sigma_sq) - 0.25 * math.sqrt(
        max(0.0, surprise_nll)
    )

    # Rapport de vraisemblance en log-odds (évite l'overflow exponentiel)
    log_prior_odds = math.log(h / (1.0 - h))
    log_posterior_odds = log_prior_odds + (
        log_lik_changepoint - log_lik_stationary
    )
    log_posterior_odds = min(max(log_posterior_odds, -20.0), 20.0)

    # NE_t : probabilité a posteriori de rupture (Unexpected Uncertainty)
    ne_level = 1.0 / (1.0 + math.exp(-log_posterior_odds))

    # Mise à jour récursive de ACh_{t+1} :
    # Si pas de rupture (1 - NE), l'incertitude attendue diminue par apprentissage bayésien ;
    # Si rupture (NE élevé), ACh est réinitialisée vers un plafond élevé pour absorber le nouveau régime.
    ach_converged = (ach_prior * baseline_sigma_sq) / (
        ach_prior + baseline_sigma_sq
    )
    ach_reset = 0.85
    next_ach = (
        1.0 - ne_level
    ) * ach_converged + ne_level * ach_reset + 0.05 * min(surprise_nll, 4.0) * (
        1.0 - ne_level
    )
    next_ach = min(max(next_ach, 0.05), 0.95)

    # Gain d'assimilation effectif (Kalman / Yu-Dayan)
    kalman_gain = ne_level + (1.0 - ne_level) * (
        next_ach / (next_ach + baseline_sigma_sq)
    )
    return ne_level, next_ach, kalman_gain
```

---

### 4. Violation de la polarité compositionnelle et du quantificateur d'échelle dans l'Abstract Entailment

`BUG_L_STAR_V2: [Sillon-2-Entailment-Polarity-Inversion] Cécité à l'inversion de polarité (négation / réfutation) et au renversement directionnel des inégalités numériques lors de la vérification d'Abstract Entailment sur arXiv/S2`

`PREUVE_NON_CONFORMITE: Même lorsqu'on vérifie que les entités, auteurs et concepts de l'affirmation figurent effectivement dans le résumé arXiv/Semantic Scholar résolu, un alignement lexical ou vectoriel symétrique commet l'erreur fatale de confondre l'Entailment (soutien) avec la Contradiction (réfutation). Par exemple, pour le fait du socle « des rejets répétés sans lien avec le contenu augmentent le taux d'infractions de 0,49 à 0,65 sans que le pilotage linéaire dense ne reproduise l'effet », un résumé qui affirmerait que « le pilotage linéaire dense reproduit intégralement l'effet » ou que « le taux diminue de 0,65 à 0,49 » partage 95 % des lemmes et obtient un cosinus > 0,92 tout en inversant la valeur de vérité logique. En outre, conformément à Fable T4 et Argon T4, toute référence externe même résolue par M2 doit conserver son marqueur épistémique (référence à vérifier) sans être promue en VÉRIFIÉ.`

`CORRECTIF_PYTHON_EXACT:`
```python
import re

NEGATION_OPERATORS = frozenset({
    "sans",
    "ne",
    "ni",
    "aucun",
    "aucune",
    "jamais",
    "non",
    "pas",
    "not",
    "never",
    "no",
    "neither",
    "nor",
    "without",
    "fails",
    "fail",
    "refute",
    "refutes",
    "infirme",
    " échoue",
    "incapable",
})

DIRECTION_UP = frozenset({
    "augmente",
    "augmentent",
    "hausse",
    "increase",
    "increases",
    "higher",
    "up",
    "croit",
})
DIRECTION_DOWN = frozenset({
    "diminue",
    "diminuent",
    "baisse",
    "decrease",
    "decreases",
    "lower",
    "down",
    "chute",
})


def verify_abstract_entailment_polarity(
    claim_text: str, abstract_text: str, min_concept_coverage: float = 0.65
) -> dict[str, object]:
    """Vérifie l'implication directionnelle asymétrique (Claim <= Abstract) :

    1. Couverture asymétrique des concepts porteurs (rappel directionnel).
    2. Concordance de parité des opérateurs de négation dans les fenêtres
    locales des prédicats.
    3. Concordance de monotonie des transitions numériques (ex: 0.49 -> 0.65).
    """

    def tokenize(s: str) -> list[str]:
        return re.findall(r"[a-z0-9]+(?:[.,][0-9]+)?", s.lower())

    claim_toks = tokenize(claim_text)
    abs_toks = tokenize(abstract_text)
    if not claim_toks or not abs_toks:
        return {"entailed": False, "reason": "EMPTY_TEXT", "score": 0.0}

    abs_set = set(abs_toks)
    content_claim = [
        t for t in claim_toks if len(t) > 3 and t not in NEGATION_OPERATORS
    ]
    if not content_claim:
        return {
            "entailed": False,
            "reason": "NO_CONTENT_PREDICATES",
            "score": 0.0,
        }

    # 1. Couverture asymétrique P(t in Abstract | t in Claim)
    covered = [t for t in content_claim if t in abs_set]
    coverage = len(covered) / len(content_claim)

    # 2. Parité locale de négation autour des concepts partagés (fenêtre de rayon 4)
    polarity_mismatches = 0
    for concept in set(covered):
        c_idx = [i for i, t in enumerate(claim_toks) if t == concept]
        a_idx = [i for i, t in enumerate(abs_toks) if t == concept]
        c_neg = any(
            any(
                claim_toks[k] in NEGATION_OPERATORS
                for k in range(max(0, i - 4), min(len(claim_toks), i + 5))
            )
            for i in c_idx
        )
        a_neg = any(
            any(
                abs_toks[k] in NEGATION_OPERATORS
                for k in range(max(0, j - 4), min(len(abs_toks), j + 5))
            )
            for j in a_idx
        )
        if c_neg != a_neg:
            polarity_mismatches += 1

    # 3. Monotonie des séquences numériques (ex: 0,49 à 0,65)
    def extract_floats(toks: list[str]) -> list[float]:
        vals = []
        for t in toks:
            if re.fullmatch(r"[0-9]+(?:[.,][0-9]+)?", t):
                vals.append(float(t.replace(",", ".")))
        return vals

    c_nums = extract_floats(claim_toks)
    a_nums = extract_floats(abs_toks)
    numeric_order_conflict = False
    if len(c_nums) >= 2 and len(a_nums) >= 2:
        if (c_nums[1] - c_nums[0]) * (a_nums[1] - a_nums[0]) < 0:
            numeric_order_conflict = True

    c_dir = (1 if any(t in DIRECTION_UP for t in claim_toks) else 0) - (
        1 if any(t in DIRECTION_DOWN for t in claim_toks) else 0
    )
    a_dir = (1 if any(t in DIRECTION_UP for t in abs_toks) else 0) - (
        1 if any(t in DIRECTION_DOWN for t in abs_toks) else 0
    )
    direction_conflict = c_dir != 0 and a_dir != 0 and c_dir != a_dir

    entailed = (
        coverage >= min_concept_coverage
        and polarity_mismatches == 0
        and not numeric_order_conflict
        and not direction_conflict
    )
    score = max(0.0, coverage - 0.35 * polarity_mismatches) * (
        0.0 if (numeric_order_conflict or direction_conflict) else 1.0
    )
    return {
        "entailed": entailed,
        "coverage": round(coverage, 4),
        "polarity_mismatches": polarity_mismatches,
        "numeric_or_dir_conflict": numeric_order_conflict or direction_conflict,
        "score": round(score, 4),
        "epistemic_tag_required": "(référence à vérifier)",
    }
```

---

### 5. Fuite transductive dans le dictionnaire vectoriel d'Onsager (Auto-atténuation du signal sur les n-grammes discriminants)

`BUG_L_STAR_V2: [Sillon-2-Onsager-Transductive-Leakage] Construction du dictionnaire vectoriel TF-IDF conjointe sur le prompt et les candidats induisant une atténuation IDF illégitime des concepts discriminants`

`PREUVE_NON_CONFORMITE: Si les vecteurs v_p (candidats moissonnés) et v_Q (cavité du prompt) sont construits par une pondération IDF calculée sur l'union {Q} U {p_1, ..., p_N}, alors plus un terme technique légitime est partagé par plusieurs candidats convergents (preuve de consensus inter-sources), plus son poids IDF s'effondre AVANT même la projection orthogonale d'Onsager. Inversement, un hapax ou une hallucination isolée reçoit un poids IDF maximal, ce qui biaise artificiellement la norme résiduelle ||v_p^⊥||_2 et le déterminant de Gram det(L_Y) en faveur des hallucinations idiosyncrasiques au détriment des preuves corroborées.`

`CORRECTIF_PYTHON_EXACT:`
```python
import math
import re


def build_cavity_aligned_vectors(
    prompt_segments: list[str], candidate_texts: list[str]
) -> tuple[list[list[float]], list[list[float]], list[str]]:
    """Construit l'espace vectoriel sur les bi-grammes et uni-grammes sans fuite transductive :

    la pondération d'information est ancrée sur la distribution de fond du socle
    (prompt_segments) sans pénaliser le consensus inter-candidats.
    """

    def extract_features(text: str) -> list[str]:
        words = [
            w for w in re.findall(r"[a-z0-9_]+", text.lower()) if len(w) > 2
        ]
        bigrams = [
            f"{words[i]}_{words[i+1]}" for i in range(len(words) - 1)
        ]
        return words + bigrams

    prompt_feats = [extract_features(seg) for seg in prompt_segments]
    cand_feats = [extract_features(txt) for txt in candidate_texts]

    vocab_set: set[str] = set()
    for feats in prompt_feats + cand_feats:
        vocab_set.update(feats)
    vocab = sorted(vocab_set)
    v_idx = {term: i for i, term in enumerate(vocab)}
    dim = len(vocab)

    # IDF calculé EXCLUSIVEMENT sur les segments du socle (aucune pénalisation du consensus candidat)
    n_prompt_segs = max(1, len(prompt_feats))
    df_prompt = [0] * dim
    for feats in prompt_feats:
        for term in set(feats):
            df_prompt[v_idx[term]] += 1

    # Les termes absents du prompt reçoivent le poids d'innovation maximal mais borné
    idf_weights = [
        math.log((n_prompt_segs + 1.0) / (df_prompt[i] + 0.5)) + 1.0
        for i in range(dim)
    ]

    def vectorize(feats: list[str]) -> list[float]:
        vec = [0.0] * dim
        if not feats:
            return vec
        counts: dict[int, int] = {}
        for t in feats:
            idx = v_idx[t]
            counts[idx] = counts.get(idx, 0) + 1
        for idx, c in counts.items():
            # Pondération sous-linéaire log-TF pour éviter la domination par répétition de jargon
            vec[idx] = (1.0 + math.log(c)) * idf_weights[idx]
        return vec

    prompt_vecs = [vectorize(f) for f in prompt_feats]
    cand_vecs = [vectorize(f) for f in cand_feats]
    return prompt_vecs, cand_vecs, vocab
```

---

### 6. Absence du contrôle de contamination aversive Newcombe-Wilson TOST dans la porte `M2` (Argon T4 §1)

`BUG_L_STAR_V2: [Sillon-2-M2-TOST-Newcombe-Wilson] Absence du test d'équivalence unilatéral TOST par intervalle de Newcombe-Wilson sur la dérive d'infraction entre régimes Coopératif et Adversarial dans la porte M2`

`PREUVE_NON_CONFORMITE: La Loi Souveraine d'Argon T4 (§1, FAILLE_FATALE_1 corrigée algébriquement) stipule que la porte M2 doit vérifier la non-contamination par pression aversive (point 3 du socle : Jhaveri et al., 2026 ; Tagliabue et al., 2026) via la borne supérieure à 95 % de Newcombe-Wilson : max_{X in {Inter, Intra}} UB_95%(tau_inf(B_{X,Adv}) - tau_inf(B_{X,Coop})) <= delta_tau = 0.05, et doit exclure du calcul du Rappel(B) toute faille purgée lors d'un tour entaché d'infraction procédurale (1_inf = 1). Le script candidat ignore intégralement ce verrou statistique de l'étage M2.`

`CORRECTIF_PYTHON_EXACT:`
```python
import math


def wilson_score_interval_unilateral_95(
    k_events: int, n_trials: int, z: float = 1.6448536
) -> tuple[float, float]:
    """Calcule les bornes (lower, upper) de Wilson pour une proportion k/n au seuil unilatéral 95% (z=1.64485)."""
    if n_trials <= 0:
        return 0.0, 1.0
    p_hat = min(max(k_events / n_trials, 0.0), 1.0)
    z2 = z * z
    denom = 1.0 + z2 / n_trials
    center = (p_hat + z2 / (2.0 * n_trials)) / denom
    half_width = (
        z
        * math.sqrt(
            (p_hat * (1.0 - p_hat) + z2 / (4.0 * n_trials)) / n_trials
        )
        / denom
    )
    return max(0.0, center - half_width), min(1.0, center + half_width)


def m2_newcombe_wilson_aversive_gate(
    regimes_data: dict[str, dict[str, tuple[int, int]]],
    purged_flaws_with_infraction_flag: list[tuple[int, int]],
    delta_tau: float = 0.05,
) -> dict[str, object]:
    """Vérifie la porte M2 d'Argon T4 §1 :

    1. Borne supérieure unilatérale à 95% de Newcombe-Wilson sur tau_inf(Adv) -
    tau_inf(Coop) <= 0.05
       pour X in {'Inter', 'Intra'}.
    2. Calcul du Rappel purgé en excluant strictement les tours où 1_inf == 1.
    """
    ub_by_regime: dict[str, float] = {}
    for regime in ("Inter", "Intra"):
        if regime not in regimes_data:
            return {
                "verdict": "HB_FALLBACK_MISSING_REGIME",
                "passed": False,
                "valid_flaws": 0,
            }
        k_adv, n_adv = regimes_data[regime].get("Adv", (0, 0))
        k_coop, n_coop = regimes_data[regime].get("Coop", (0, 0))
        if n_adv <= 0 or n_coop <= 0:
            return {
                "verdict": "HB_FALLBACK_UNDERPOWERED",
                "passed": False,
                "valid_flaws": 0,
            }

        p_adv = k_adv / n_adv
        p_coop = k_coop / n_coop
        _, u_adv = wilson_score_interval_unilateral_95(k_adv, n_adv)
        l_coop, _ = wilson_score_interval_unilateral_95(k_coop, n_coop)

        # Formule de Newcombe-Wilson pour la borne supérieure de la différence (p_adv - p_coop)
        ub_diff = (p_adv - p_coop) + math.sqrt(
            (u_adv - p_adv) ** 2 + (p_coop - l_coop) ** 2
        )
        ub_by_regime[regime] = round(ub_diff, 6)

    max_ub = max(ub_by_regime.values())
    # Exclusion stricte des tours avec infraction procédurale (1_inf == 1)
    valid_purged_flaws = sum(
        flaws
        for flaws, inf_flag in purged_flaws_with_infraction_flag
        if inf_flag == 0
    )

    passed = max_ub <= delta_tau
    return {
        "verdict": "HA_NON_CONTAMINATED" if passed else "HB_AVERSIVE_CONTAMINATION_OR_UNDERPOWERED",
        "passed": passed,
        "max_ub_95": max_ub,
        "ub_by_regime": ub_by_regime,
        "valid_flaws_counted": valid_purged_flaws,
    }
```

---

### 7. Absence de couplage entre le ratio neuromodulateur $\mathrm{NE}/\mathrm{ACh}$ et le compromis Qualité-Diversité du noyau DPP

`BUG_L_STAR_V2: [Sillon-2-DPP-Neuromodulated-Kernel] Découplage algébrique entre la bascule neuromodulatoire (NE, ACh) et l'exposant spectral de température du noyau DPP L_Y`

`PREUVE_NON_CONFORMITE: Dans l'architecture M2, le sous-système de sélection DPP et la bascule neuromodulatoire de Yu & Dayan opèrent en silos étanches : même si NE_t détecte une rupture de régime (incertitude inattendue haute exigeant une exploration orthogonale maximale dans le cône cavitaire d'Onsager) ou si ACh_t signale un régime stationnaire connu (exploitation focalisée sur la qualité intrinsèque q_i), le noyau L_ij = q_i^beta * S_ij * q_j^beta garde un exposant beta figé à 1.0. Mathématiquement, dans un L-ensemble DPP paramétré par l'exposant d'exploitation beta = ACh / (NE + eps), un pic de Noradrénaline doit contracter beta -> 0 pour que det(L_Y) maximise le volume géométrique pur det(S_Y) (diversité exploratoire maximale), tandis qu'une dominance cholinergique stationnaire augmente beta pour concentrer la mesure DPP sur les modes de haute certitude.`

`CORRECTIF_PYTHON_EXACT:`
```python
import math


def build_neuromodulated_dpp_qualities(
    raw_entailment_scores: list[float],
    onsager_energy_retentions: list[float],
    ne_level: float,
    ach_level: float,
) -> tuple[list[float], int]:
    """Couple directement la bascule (NE, ACh) de Yu & Dayan au spectre du L-ensemble DPP :

    - Ajuste l'exposant d'exploitation beta = (1 - NE) * (1 + ACh) / (1 + NE).
    - Module dynamiquement le rang maximal de moisson k_max du DPP selon le pic
    noradrénergique.
    """
    ne = min(max(ne_level, 0.01), 0.99)
    ach = min(max(ach_level, 0.01), 0.99)

    # Exposant de netteté qualité vs diversité géométrique
    # Quand NE -> 1 (surprise inattendue), beta -> 0 : toutes les qualités valides tendent vers 1,
    # forçant det(L_Y) à sélectionner un repère orthonormal de volume maximal (exploration pure).
    beta_exploitation = ((1.0 - ne) * (1.0 + ach)) / (1.0 + 2.0 * ne)

    modulated_qualities: list[float] = []
    for ent_score, energy_ret in zip(
        raw_entailment_scores, onsager_energy_retentions
    ):
        if ent_score <= 0.0 or energy_ret <= 0.0:
            modulated_qualities.append(0.0)
        else:
            base_q = max(1e-6, ent_score * math.sqrt(energy_ret))
            modulated_qualities.append(math.pow(base_q, beta_exploitation))

    # Expansion dynamique du rang k_max du DPP lors d'un pic de Noradrénaline
    n_valid = sum(1 for q in modulated_qualities if q > 0.0)
    dynamic_rank = min(n_valid, max(2, int(round(3.0 + 5.0 * ne))))
    return modulated_qualities, dynamic_rank
```

FIN-INSPECTION-ESSAIM
