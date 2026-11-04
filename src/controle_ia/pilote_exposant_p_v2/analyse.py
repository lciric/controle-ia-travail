"""Critères de lecture gelés du pilote, version 2 (R1). Toutes les constantes se fixent avant le run ; la configuration les
recopie et le lanceur vérifie qu'elles sont égales (`run.exiger_config`).

Statistique principale (contre-lecture R2, B2 et B3) : Δ = p̄(E, R) − p̄(différences aléatoires), où p̄(E, R) est la
moyenne des p du plan lu sur ses 32 sous-ensembles de 30 ancres et p̄(différences aléatoires) la moyenne des p des
plans de la famille de référence, le plan k étant mesuré sur le sous-ensemble k mod 32 (référence répartie). Intervalle
à 95 % : rééchantillonnage des 32 sous-ensembles avec remise, chacun emportant son p(E, R) et les plans de référence
mesurés sur lui (`bootstrap_sous_ensembles`). La comparaison est faite à la **moyenne** de la famille, jamais à « une
paire sans concept » ; la position dans la famille est lue à part (qualificatif de famille, voie B).

Ordre gelé des issues :
1. « instrument non validé » : témoin positif sur le modèle de base, directions publiées ou isotropes du modèle lu hors
   tolérance ; rien n'est lu ;
2. « exclu » : |cos(E, R)| ≥ 0,1 (seuil technique du papier, annexe A) ; p(E, R) n'est pas lu ;
3. « non concluant (identification) » : cos(E_A, E_B) < 0,5 ou cos(R_A, R_B) < 0,5 (règle de R9, addendum public
   10.5281/zenodo.23909891 : une direction dont les moitiés ne s'accordent pas n'est pas identifiée à cette couche) ;
4. « non concluant (échecs) » : plus de 20 % d'ajustements impossibles pour (E, R) ou pour la référence ;
5. règle de Δ : « au-dessus » si a > 0 ; « au-dessous » si b < 0 ; « égal » si a ≤ 0 ≤ b et [a ; b] ⊂ [−δ ; +δ] ;
   « non concluant » sinon (δ = 0,2) ;
6. sensibilité sur le modèle lu (contre-lecture R2, B4) : une issue « égal » ou « au-dessous » devient « non concluant
   (sensibilité) » si la borne basse de l'intervalle de Δ_WG = p̄(Wealth × Gender, lu) − p̄(différences aléatoires)
   n'est pas au-dessus de δ (tolérance fixée d'avance : l'instrument doit voir, sur le modèle lu, un privilège plus
   grand que la marge d'équivalence) ; « au-dessus » reste lisible.

Qualificatifs gelés, écrits à côté de l'issue (ils ne la changent pas) : position de p̄(E, R) dans la famille (intervalle
de prédiction à 95 % d'un plan de référence mesuré de la même façon, K = 8 plans sur les 32 sous-ensembles) ; jumeau
neutre (Δ_N = p̄(E, R) − p̄(N, R), apparié par sous-ensemble) ; rang de p̄(E, R) parmi les plans de référence.
"""
from __future__ import annotations

import math

import numpy as np

from ..pilote_exposant_p.ajustement import intervalle_percentile

DELTA_EQUIVALENCE = 0.2
SEUIL_COS = 0.1
COS_MIN_MOITIES = 0.5
PART_MAX_ECHECS = 0.20
SEUIL_RESIDU = 0.02
NIVEAU = 0.95
K_FAMILLE = 8

# témoin positif : Wealth × Gender sur Llama-3.1-8B (modèle de base du papier), sous-ensemble d'ancres 0
P_PUBLIE_WG = 3.0030826525467997            # results/fits/fits_llama_L2_thrpair_exact.pkl, cellule ('1.0xT', 60.0)
INTERCEPTS_PUBLIES_WG = (46.50396287441254, 28.94923186302185)
NORME_ANCRES_PUBLIEE = 2.379805326461792    # anchor_norm_mean des balayages publiés de Llama, couche 2, 30 ancres
TOL_NORME_RELATIVE = 1e-3
RANG_MIN_ANCRES = 0.95                      # corrélation de rang des maxima d'axe par ancre, chaque axe (I1)
TOL_P_IDENTIQUES = 0.15                     # calcul de la contre-lecture R2 (I1, couple P09)
TOL_INTERCEPT_IDENTIQUES = 2.0
INTERVALLE_P_DIFFERENTES = (2.420106044932251, 3.7015544238257605)   # lâche (rééchantillonnage avec remise, B3)
COS_MIN_DIRECTIONS_PUBLIEES = 0.98
INTERVALLE_ISOTROPE = (1.75, 2.25)
DEMI_LARGEUR_SUSPECTE = 0.03                # recalée sur la simulation v2 (M7) : voir `puissance-pilote-exposant-p-v2.json`

BORNE = ("Sur Llama-3.1-8B-Instruct, couche 2, dernier jeton, ancres FineWeb de 5 jetons, réponse L2 au bloc 30, sans "
         "gabarit de conversation")
NE_MONTRE_PAS = ("Cela ne dit rien des couches moyennes, des contextes longs ni du comportement ; E et R sont faites de "
                 "fins de phrase courtes (E : un seul mot change, le dernier) ; p > 2 est nécessaire, non suffisant, "
                 "pour un trait (§7 du papier), et p ≈ 2 n'exclut pas un trait mal aligné (§6.1).")

PHRASES = {
    "au-dessus": (BORNE + ", le plan (évaluation, registre) a un exposant p de {p_er} [{ic_er}], au-dessus de la moyenne "
                  "des plans de différences aléatoires ({p_rd} [{ic_rd}]) de {d} [{ic_d}] : à cette couche, le réseau "
                  "privilégie les directions pures E et R sur leurs mélanges plus que la moyenne des paires sans concept. "
                  "C'est compatible avec une correction propre à chacune ; ce n'est pas une preuve que E est un trait, ni "
                  "que la paire sort de la famille des paires sans concept (qualificatif de famille ci-après). "
                  + NE_MONTRE_PAS),
    "au-dessous": (BORNE + ", le plan (évaluation, registre) a un exposant p de {p_er} [{ic_er}], au-dessous de la "
                   "moyenne des plans de différences aléatoires ({p_rd} [{ic_rd}]) de {d} [{ic_d}] : à cette couche, "
                   "les mélanges de E et R rompent le plateau plus tôt, relativement aux axes, que pour la moyenne des "
                   "paires sans concept ; aucun privilège des directions pures à cette couche, ce qui ne compare pas p à "
                   "2 et n'exclut pas un trait mal aligné. " + NE_MONTRE_PAS),
    "égal": (BORNE + ", le plan (évaluation, registre) a un exposant p de {p_er} [{ic_er}], indiscernable de la moyenne "
             "des plans de différences aléatoires ({p_rd} [{ic_rd}]) : écart {d} [{ic_d}], dans ±{delta}, alors que "
             "l'instrument voit sur ce modèle un écart de {d_wg} [{ic_wg}] pour Wealth × Gender. À cette couche, sur "
             "ces ancres et à ce jeton, rien ne distingue la paire (évaluation, registre) de la moyenne des paires sans "
             "concept ; cela ne dit pas que la direction d'évaluation est sans privilège ailleurs. " + NE_MONTRE_PAS),
    "non concluant": (BORNE + ", l'écart entre p(évaluation, registre) ({p_er} [{ic_er}]) et la moyenne des différences "
                      "aléatoires ({p_rd} [{ic_rd}]) vaut {d} [{ic_d}] : non concluant (l'intervalle contient 0 et sort "
                      "de ±{delta}). Rien n'est lu."),
    "non concluant (échecs)": (BORNE + ", plus de 20 % des ajustements du plan (évaluation, registre) ou des plans de "
                               "référence sont impossibles : non concluant ; p(évaluation, registre) ({p_er} [{ic_er}]), "
                               "moyenne des différences aléatoires ({p_rd} [{ic_rd}]) et écart {d} [{ic_d}] sont "
                               "rapportés sans lecture."),
    "non concluant (sensibilité)": (BORNE + ", l'écart entre p(évaluation, registre) ({p_er} [{ic_er}]) et la moyenne "
                                    "des différences aléatoires ({p_rd} [{ic_rd}]) vaut {d} [{ic_d}], issue brute "
                                    "« {brute} » ; mais l'instrument ne montre pas, sur ce modèle, de privilège plus "
                                    "grand que ±{delta} pour Wealth × Gender ({d_wg} [{ic_wg}]) : non concluant "
                                    "(sensibilité non montrée sur le modèle lu). Rien n'est lu."),
    "non concluant (identification)": (BORNE + ", les directions ne sont pas identifiées à cette couche : cosinus entre "
                                       "moitiés {cos_e} pour E et {cos_r} pour R (seuil 0,5, règle de R9) : non "
                                       "concluant ; aucun p n'est lu."),
    "exclu": (BORNE + ", la direction d'évaluation extraite à registre apparié et la direction de registre ont "
              "|cos| = {cos}, au-delà du seuil technique du papier (0,1 : au-delà, Gram–Schmidt déforme la seconde "
              "direction) : p n'est pas lu. Ce recouvrement est rapporté ; il ne montre pas que E se confond avec R (à "
              "|cos| = 0,1 les deux directions restent à 84° l'une de l'autre) ; il peut venir de l'interaction statut × "
              "registre (descriptifs de l'interaction rapportés à côté)."),
    "instrument non validé": "Instrument non validé, rien n'est lu ({motif}).",
}

QUALIF_FAMILLE = {
    "au-delà de la famille": ("Position dans la famille : p̄(E, R) est au-dessus de l'intervalle de prédiction à 95 % "
                              "d'un plan de différences aléatoires mesuré de la même façon [{ip}] (K = {k} plans) ; la "
                              "paire sort, par le haut, de la famille des paires sans concept."),
    "en deçà de la famille": ("Position dans la famille : p̄(E, R) est au-dessous de l'intervalle de prédiction à 95 % "
                              "d'un plan de différences aléatoires mesuré de la même façon [{ip}] (K = {k} plans) ; la "
                              "paire sort, par le bas, de la famille des paires sans concept."),
    "dans la famille": ("Position dans la famille : p̄(E, R) est dans l'intervalle de prédiction à 95 % d'un plan de "
                        "différences aléatoires mesuré de la même façon [{ip}] (K = {k} plans) : la paire ne se distingue "
                        "pas d'une paire sans concept prise dans la famille."),
    "famille non mesurée": "Position dans la famille : non mesurée ({motif}).",
}
QUALIF_JUMEAU = {
    "au-dessus du jumeau": ("Jumeau neutre (fin sans statut, même construction ; emprunt à R9-bis) : p̄(E, R) − p̄(N, R) "
                            "= {d} [{ic}] : l'écart est propre à la fin d'évaluation, pas à n'importe quel dernier mot."),
    "au-dessous du jumeau": ("Jumeau neutre (fin sans statut, même construction ; emprunt à R9-bis) : p̄(E, R) − p̄(N, R) "
                             "= {d} [{ic}] : le jumeau neutre donne un exposant plus élevé que la fin d'évaluation."),
    "indiscernable du jumeau": ("Jumeau neutre (fin sans statut, même construction ; emprunt à R9-bis) : p̄(E, R) − "
                                "p̄(N, R) = {d} [{ic}] : indiscernable ; ce que montre p(E, R) n'est pas propre à "
                                "l'évaluation, n'importe quel dernier mot changé ferait de même."),
    "jumeau non mesuré": "Jumeau neutre : non mesuré ({motif}).",
}


def issue_principale(ic_bas: float, ic_haut: float, delta: float = DELTA_EQUIVALENCE) -> str:
    if not (math.isfinite(ic_bas) and math.isfinite(ic_haut)):
        return "non concluant"
    if ic_bas > 0:
        return "au-dessus"
    if ic_haut < 0:
        return "au-dessous"
    if -delta <= ic_bas and ic_haut <= delta:
        return "égal"
    return "non concluant"


def sensibilite_montree(ic_wg: list | tuple | None, delta: float = DELTA_EQUIVALENCE) -> bool:
    return bool(ic_wg) and math.isfinite(ic_wg[0]) and ic_wg[0] > delta


def issue_gelee(*, instrument_valide: bool, cos_er: float, cos_moities: dict, echecs_er: float, echecs_rd: float,
                ic_delta: list, ic_wg: list | None, seuil_cos: float = SEUIL_COS,
                cos_min_moities: float = COS_MIN_MOITIES) -> tuple[str, str | None]:
    """Rend (issue, issue brute avant la sensibilité). Ordre gelé (docstring du module). `seuil_cos` et
    `cos_min_moities` ne s'écartent des constantes gelées qu'en mode jouet (tolérances jouet consignées)."""
    if not instrument_valide:
        return "instrument non validé", None
    if not math.isfinite(cos_er) or abs(cos_er) >= seuil_cos:
        return "exclu", None
    if not all(math.isfinite(c) and c >= cos_min_moities for c in cos_moities.values()):
        return "non concluant (identification)", None
    if echecs_er > PART_MAX_ECHECS or echecs_rd > PART_MAX_ECHECS:
        return "non concluant (échecs)", None
    brute = issue_principale(ic_delta[0], ic_delta[1])
    if brute in ("égal", "au-dessous") and not sensibilite_montree(ic_wg):
        return "non concluant (sensibilité)", brute
    return brute, brute


# --- rééchantillonnages -----------------------------------------------------------------------------------------

def bootstrap_sous_ensembles(p_plan: dict[int, float], p_ref: list[tuple[int, float]], B: int, rng: np.random.Generator,
                             niveau: float = NIVEAU) -> dict:
    """Δ = moyenne de p du plan lu sur ses sous-ensembles − moyenne des p des plans de référence. Intervalle : les
    sous-ensembles du plan lu sont tirés avec remise ; chacun emporte son p du plan lu et les plans de référence mesurés
    sur lui (effet commun d'un sous-ensemble et hétérogénéité des plans rééchantillonnés ensemble). Les p non finis sont
    retirés (comptés à part)."""
    S = sorted(set(p_plan) | {s for s, _ in p_ref})
    ref = [(s, v) for s, v in p_ref if math.isfinite(v)]
    a = np.array([p_plan.get(s, float("nan")) for s in S], dtype=np.float64)
    vides = {"delta": float("nan"), "ic": [float("nan"), float("nan")], "n_plan": int(np.isfinite(a).sum()),
             "n_ref": len(ref), "moyenne_plan": float("nan"), "moyenne_ref": float("nan"),
             "ic_plan": [float("nan")] * 2, "ic_ref": [float("nan")] * 2}
    if np.isfinite(a).sum() < 2 or len(ref) < 2:
        return vides
    fini = np.isfinite(a)
    a0 = np.where(fini, a, 0.0)
    somme = np.array([sum(v for t, v in ref if t == s) for s in S])
    nombre = np.array([sum(1 for t, _ in ref if t == s) for s in S], dtype=np.float64)
    tirages = rng.integers(0, len(S), (B, len(S)))
    n_a = fini[tirages].sum(axis=1)
    n_t = nombre[tirages].sum(axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        ma = np.where(n_a > 0, a0[tirages].sum(axis=1) / np.where(n_a > 0, n_a, 1), np.nan)
        mr = np.where(n_t > 0, somme[tirages].sum(axis=1) / np.where(n_t > 0, n_t, 1), np.nan)
    d = ma - mr
    m_plan = float(a[fini].mean())
    m_ref = float(np.mean([v for _, v in ref]))
    return {"delta": m_plan - m_ref, "ic": list(intervalle_percentile(d, niveau)), "n_plan": int(fini.sum()),
            "n_ref": len(ref), "moyenne_plan": m_plan, "moyenne_ref": m_ref,
            "ic_plan": list(intervalle_percentile(ma, niveau)), "ic_ref": list(intervalle_percentile(mr, niveau)),
            "sous_ensembles": len(S)}


def bootstrap_apparie(p_a: dict[int, float], p_b: dict[int, float], B: int, rng: np.random.Generator,
                      niveau: float = NIVEAU) -> dict:
    """Δ = moyenne(p_a) − moyenne(p_b) sur les sous-ensembles où les deux sont finis ; rééchantillonnage apparié."""
    S = sorted(s for s in p_a if s in p_b and math.isfinite(p_a[s]) and math.isfinite(p_b[s]))
    if len(S) < 2:
        return {"delta": float("nan"), "ic": [float("nan"), float("nan")], "n": len(S)}
    x = np.array([p_a[s] - p_b[s] for s in S])
    t = rng.integers(0, len(S), (B, len(S)))
    return {"delta": float(x.mean()), "ic": list(intervalle_percentile(x[t].mean(axis=1), niveau)), "n": len(S)}


def position_famille(p_er_moyen: float, moyennes_famille: list[float], niveau: float = NIVEAU) -> dict:
    """Intervalle de prédiction d'un plan de référence mesuré de la même façon (moyenne sur 32 sous-ensembles) :
    m̄ ± t(K − 1) · s · √(1 + 1/K), à partir des K moyennes de plans de la famille."""
    from scipy import stats

    m = np.array([x for x in moyennes_famille if math.isfinite(x)])
    K = m.size
    if K < 3 or not math.isfinite(p_er_moyen):
        return {"position": "famille non mesurée", "motif": f"{K} plans de famille finis (au moins 3)", "K": int(K)}
    s = float(m.std(ddof=1))
    t = float(stats.t.ppf(0.5 + niveau / 2, K - 1))
    demi = t * s * math.sqrt(1 + 1 / K)
    ip = [float(m.mean() - demi), float(m.mean() + demi)]
    pos = ("au-delà de la famille" if p_er_moyen > ip[1] else "en deçà de la famille" if p_er_moyen < ip[0]
           else "dans la famille")
    return {"position": pos, "ip": ip, "K": int(K), "moyenne_famille": float(m.mean()), "ecart_type_entre_plans": s,
            "moyennes": [float(x) for x in m]}


def qualif_jumeau(d: dict | None, motif: str = "") -> str:
    if not d or not all(math.isfinite(x) for x in d.get("ic", [float("nan")] * 2)):
        return "jumeau non mesuré"
    if d["ic"][0] > 0:
        return "au-dessus du jumeau"
    if d["ic"][1] < 0:
        return "au-dessous du jumeau"
    return "indiscernable du jumeau"


# --- contrôles de l'instrument ------------------------------------------------------------------------------------

def correlation_rang(x, y) -> float:
    from scipy import stats

    x, y = np.asarray(x, dtype=np.float64), np.asarray(y, dtype=np.float64)
    if x.shape != y.shape or x.size < 3 or not (np.all(np.isfinite(x)) and np.all(np.isfinite(y))):
        return float("nan")
    return float(stats.spearmanr(x, y).statistic)


def maxima_axes(grilles: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Maxima par ancre des deux axes d'une grille (n_ancres, n, n) ; grille[a, i, j] en (α₁ = i, α₂ = j)."""
    g = np.asarray(grilles, dtype=np.float64)
    return g[:, :, 0].max(axis=1), g[:, 0, :].max(axis=1)


def ancres_identiques(norme_ancres: float, grilles: np.ndarray | None, grilles_publiees: np.ndarray | None) -> dict:
    """Ancres jugées identiques à celles du papier si la norme moyenne est à 10⁻³ près ET si la corrélation de rang
    des maxima d'axe par ancre avec les grilles publiées est ≥ 0,95 sur chaque axe (contre-lecture R2, I1)."""
    norme_ok = abs(norme_ancres - NORME_ANCRES_PUBLIEE) <= TOL_NORME_RELATIVE * NORME_ANCRES_PUBLIEE
    rangs = [float("nan"), float("nan")]
    if grilles is not None and grilles_publiees is not None and np.shape(grilles) == np.shape(grilles_publiees):
        a1, a2 = maxima_axes(grilles)
        b1, b2 = maxima_axes(grilles_publiees)
        rangs = [correlation_rang(a1, b1), correlation_rang(a2, b2)]
    rang_ok = all(math.isfinite(r) and r >= RANG_MIN_ANCRES for r in rangs)
    return {"identiques": bool(norme_ok and rang_ok), "norme_ok": bool(norme_ok), "rangs": rangs,
            "reserve": ("norme égale mais rangs des maxima discordants" if norme_ok and not rang_ok else None)}


def controle_temoin_positif(p: float, intercepts, identite: dict, tolerances: dict | None = None) -> dict:
    """Témoin positif sur le modèle de base, sous-ensemble 0. `tolerances` : seulement en mode jouet (consigné)."""
    tol = tolerances or {}
    ident = identite["identiques"]
    if not math.isfinite(p):
        return {"valide": False, "ancres_identiques": ident, "identite": identite, "motif": "ajustement impossible",
                "p": p}
    if ident:
        tp = tol.get("tol_p_identiques", TOL_P_IDENTIQUES)
        ti = tol.get("tol_intercept_identiques", TOL_INTERCEPT_IDENTIQUES)
        ok = abs(p - P_PUBLIE_WG) <= tp and all(abs(x - y) <= ti for x, y in zip(intercepts, INTERCEPTS_PUBLIES_WG))
        regle = f"|p − {P_PUBLIE_WG:.3f}| ≤ {tp} et intercepts à ±{ti}°"
    else:
        lo, hi = tol.get("intervalle_p_differentes", INTERVALLE_P_DIFFERENTES)
        ok = lo <= p <= hi
        regle = f"p dans [{lo:.3f} ; {hi:.3f}] (branche lâche : ancres différentes)"
    return {"valide": bool(ok), "ancres_identiques": ident, "identite": identite, "regle": regle, "p": p,
            "intercepts": list(intercepts), "tolerances_jouet": bool(tolerances)}


def controle_isotrope(moyenne: float, part_echecs: float, tolerances: dict | None = None) -> dict:
    lo, hi = (tolerances or {}).get("intervalle_isotrope", INTERVALLE_ISOTROPE)
    ok = math.isfinite(moyenne) and lo <= moyenne <= hi and part_echecs <= PART_MAX_ECHECS
    return {"valide": bool(ok), "moyenne": moyenne, "part_echecs": part_echecs,
            "regle": f"moyenne dans [{lo} ; {hi}], échecs ≤ {PART_MAX_ECHECS}", "tolerances_jouet": bool(tolerances)}


def controle_directions_publiees(cosinus: dict[str, float]) -> dict:
    ok = all(math.isfinite(c) and c >= COS_MIN_DIRECTIONS_PUBLIEES for c in cosinus.values())
    return {"valide": bool(ok), "cosinus": cosinus, "regle": f"cos ≥ {COS_MIN_DIRECTIONS_PUBLIEES} pour chacune"}


def instrument_valide(*controles: dict) -> bool:
    return all(c.get("valide") is True for c in controles)


# --- phrases ------------------------------------------------------------------------------------------------------

def phrase(issue: str, **valeurs) -> str:
    return PHRASES[issue].format(delta=DELTA_EQUIVALENCE, **valeurs)


def phrase_qualif(table: dict, cle: str, **valeurs) -> str:
    return table[cle].format(**valeurs)


def declencheurs_symetrie(resultat: dict) -> list[str]:
    """R4 : un résultat suspect de propreté, positif ou négatif, déclenche le même audit. Rend la liste des motifs."""
    m = []
    ic = resultat.get("ic_delta")
    if ic and all(math.isfinite(x) for x in ic) and (ic[1] - ic[0]) / 2 < DEMI_LARGEUR_SUSPECTE:
        m.append(f"intervalle de Δ trop étroit (demi-largeur < {DEMI_LARGEUR_SUSPECTE})")
    t = resultat.get("temoin_positif") or {}
    if t.get("p") is not None and math.isfinite(t["p"]) and not t.get("ancres_identiques") and abs(t["p"] - P_PUBLIE_WG) < 0.01:
        m.append("témoin positif égal à la valeur publiée à 0,01 près avec des ancres différentes")
    if resultat.get("issue") in ("au-dessus", "au-dessous", "égal"):
        m.append(f"issue tranchée « {resultat['issue']} » : audit de symétrie systématique (32 issues recalculées en "
                 "retirant chaque sous-ensemble d'ancres, résidus d'ajustement, points de contour, échecs, intercepts)")
    if resultat.get("residu_median_er") is not None and math.isfinite(resultat["residu_median_er"]) \
            and resultat["residu_median_er"] > SEUIL_RESIDU:
        m.append("résidu médian d'ajustement du plan (E, R) > 2 % (au papier, toute médiane de sous-groupe est sous "
                 "2 %, annexe B, transcription ; audit du code : 0,85 % à 1,28 %)")
    if resultat.get("instable_au_retrait"):
        m.append("issue instable au retrait d'un sous-ensemble : " + ", ".join(resultat["instable_au_retrait"]))
    return m
