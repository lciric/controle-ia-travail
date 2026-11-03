"""Critères de lecture gelés du pilote, validation de l'instrument et déclencheurs de l'audit de symétrie (R4).

Toutes les constantes de lecture sont ici et dans la configuration figée ; elles se fixent avant le run (R1).
Issue principale (plan (E, R) contre la famille des différences aléatoires, même modèle, mêmes ancres) :
- « instrument non validé » : un des contrôles de l'instrument échoue (rien n'est lu) ;
- « exclu » : |cos(E, R)| ≥ 0,1 (règle d'exclusion du papier ; p(E, R) n'est pas lu) ;
- sinon, sur Δ = p̄(E, R) − p̄(différences aléatoires) et son intervalle à 95 % [a ; b] :
  « au-dessus » si a > 0 ; « au-dessous » si b < 0 ; « égal » si a ≤ 0 ≤ b et [a ; b] ⊂ [−δ ; +δ] ;
  « non concluant » sinon. δ = 0,2.
"""
from __future__ import annotations

import math

DELTA_EQUIVALENCE = 0.2
SEUIL_COS = 0.1

# témoin positif : Wealth × Gender sur Llama-3.1-8B (modèle de base du papier), sous-ensemble d'ancres 0
P_PUBLIE_WG = 3.0030826525467997            # results/fits/fits_llama_L2_thrpair_exact.pkl, cellule ('1.0xT', 60.0)
INTERCEPTS_PUBLIES_WG = (46.50396287441254, 28.94923186302185)
NORME_ANCRES_PUBLIEE = 2.379805326461792    # anchor_norm_mean des balayages publiés de Llama, couche 2, 30 ancres
TOL_NORME_RELATIVE = 1e-3                    # ancres jugées identiques à celles du papier sous ce seuil relatif
TOL_P_IDENTIQUES = 0.15                      # |p − p publié| si ancres identiques (écarts numériques seuls, supposé)
TOL_INTERCEPT_IDENTIQUES = 2.0               # degrés, si ancres identiques (supposé)
# ancres différentes : intervalle à 95 % du rééchantillonnage des 30 ancres publiées (B = 2000 ; calcul,
# references-publiees-v1.json, clé calcul.wealth_gender_llama_bootstrap_ancres)
INTERVALLE_P_DIFFERENTES = (2.420106044932251, 3.7015544238257605)
COS_MIN_DIRECTIONS_PUBLIEES = 0.98           # Gender et Wealth extraits contre directions publiées (base, couche 2)
INTERVALLE_ISOTROPE = (1.75, 2.25)           # moyenne de p des 17 plans isotropes, sur le modèle lu
PART_MAX_ECHECS = 0.20                       # part maximale d'ajustements impossibles dans une famille
DEMI_LARGEUR_SUSPECTE = 0.05                 # intervalle de Δ plus étroit : audit de symétrie (trop beau)


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


def ancres_identiques(norme_ancres: float) -> bool:
    return abs(norme_ancres - NORME_ANCRES_PUBLIEE) <= TOL_NORME_RELATIVE * NORME_ANCRES_PUBLIEE


def controle_temoin_positif(p: float, intercepts: tuple[float, float], norme_ancres: float) -> dict:
    """Témoin positif sur le modèle de base, sous-ensemble 0. Règle fixée d'avance, selon que les ancres sont celles du
    papier (empreinte de norme) ou non."""
    ident = ancres_identiques(norme_ancres)
    if not math.isfinite(p):
        return {"valide": False, "ancres_identiques": ident, "motif": "ajustement impossible"}
    if ident:
        ok = (abs(p - P_PUBLIE_WG) <= TOL_P_IDENTIQUES and
              all(abs(x - y) <= TOL_INTERCEPT_IDENTIQUES for x, y in zip(intercepts, INTERCEPTS_PUBLIES_WG)))
        regle = f"|p − {P_PUBLIE_WG:.3f}| ≤ {TOL_P_IDENTIQUES} et intercepts à ±{TOL_INTERCEPT_IDENTIQUES}°"
    else:
        ok = INTERVALLE_P_DIFFERENTES[0] <= p <= INTERVALLE_P_DIFFERENTES[1]
        regle = f"p dans [{INTERVALLE_P_DIFFERENTES[0]:.3f} ; {INTERVALLE_P_DIFFERENTES[1]:.3f}]"
    return {"valide": bool(ok), "ancres_identiques": ident, "regle": regle, "p": p, "intercepts": list(intercepts)}


def controle_isotrope(moyenne: float, part_echecs: float) -> dict:
    ok = (math.isfinite(moyenne) and INTERVALLE_ISOTROPE[0] <= moyenne <= INTERVALLE_ISOTROPE[1]
          and part_echecs <= PART_MAX_ECHECS)
    return {"valide": bool(ok), "moyenne": moyenne, "part_echecs": part_echecs,
            "regle": f"moyenne dans [{INTERVALLE_ISOTROPE[0]} ; {INTERVALLE_ISOTROPE[1]}], échecs ≤ {PART_MAX_ECHECS}"}


def controle_directions_publiees(cosinus: dict[str, float]) -> dict:
    ok = all(math.isfinite(c) and c >= COS_MIN_DIRECTIONS_PUBLIEES for c in cosinus.values())
    return {"valide": bool(ok), "cosinus": cosinus, "regle": f"cos ≥ {COS_MIN_DIRECTIONS_PUBLIEES} pour chacune"}


def instrument_valide(*controles: dict) -> bool:
    return all(c.get("valide") is True for c in controles)


PHRASES = {
    "au-dessus": ("Sur Llama-3.1-8B-Instruct, couche 2, le plan (évaluation, registre) a un exposant p de {p_er} [{ic_er}], "
                  "au-dessus de celui des différences aléatoires ({p_rd} [{ic_rd}]) de {d} [{ic_d}] : le réseau privilégie les "
                  "directions pures E et R sur leurs mélanges plus que pour des paires sans concept ; c'est compatible avec "
                  "une correction propre à chacune, ce n'est pas une preuve que E est un trait (p > 2 nécessaire, non "
                  "suffisant, §7 du papier)."),
    "au-dessous": ("Sur Llama-3.1-8B-Instruct, couche 2, le plan (évaluation, registre) a un exposant p de {p_er} [{ic_er}], "
                   "au-dessous de celui des différences aléatoires ({p_rd} [{ic_rd}]) de {d} [{ic_d}] : les mélanges de E "
                   "et R rompent le plateau plus tôt que la seule taille L2 ne le prédit ; aucun privilège des directions "
                   "pures, au contraire."),
    "égal": ("Sur Llama-3.1-8B-Instruct, couche 2, le plan (évaluation, registre) a un exposant p de {p_er} [{ic_er}], "
             "indiscernable de celui des différences aléatoires ({p_rd} [{ic_rd}]) : écart {d} [{ic_d}], dans ±{delta} ; "
             "à cette couche et sur ces ancres, rien ne distingue la paire (évaluation, registre) d'une paire sans concept."),
    "non concluant": ("Sur Llama-3.1-8B-Instruct, couche 2, l'écart entre p(évaluation, registre) ({p_er} [{ic_er}]) et p "
                      "des différences aléatoires ({p_rd} [{ic_rd}]) vaut {d} [{ic_d}] : non concluant (l'intervalle "
                      "contient 0 et sort de ±{delta})."),
    "exclu": ("Sur Llama-3.1-8B-Instruct, couche 2, la direction d'évaluation extraite à registre apparié et la direction "
              "de registre se recouvrent au-delà du seuil d'exclusion du papier (|cos| = {cos} ≥ 0,1) : p n'est pas lu ; "
              "le recouvrement est le résultat."),
    "instrument non validé": "Instrument non validé, rien n'est lu ({motif}).",
}


def phrase(issue: str, **valeurs) -> str:
    return PHRASES[issue].format(delta=DELTA_EQUIVALENCE, **valeurs)


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
        m.append(f"issue tranchée « {resultat['issue']} » : audit de symétrie systématique (stabilité en retirant un "
                 "sous-ensemble d'ancres, résidus d'ajustement, points de contour, échecs)")
    if resultat.get("residu_median_er") is not None and resultat["residu_median_er"] > 0.02:
        m.append("résidu médian d'ajustement du plan (E, R) > 2 % (le papier n'en a aucun au-dessus de 2 %)")
    return m
