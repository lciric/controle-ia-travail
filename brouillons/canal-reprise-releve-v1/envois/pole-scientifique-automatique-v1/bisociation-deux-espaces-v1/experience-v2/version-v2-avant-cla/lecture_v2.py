"""Booléens et tables de lecture gelés (section « Critères de lecture gelés »), codés tels qu'écrits, pour le
lecteur de la porte (R13) et pour les essais R5. Seuils gelés (R-579, R-580) : S1 à S6, S7, S10, S14 ; S3 = F-A,
S4 = R-A, S17 = option 1. Les écarts sont en part (0,01 = 1 point).

`c` : dictionnaire {(nom_du_contraste, condition): résumé} où un résumé porte estimation, lb95, ub95, lb99 ;
« r(N, b) » est passé sous la clé ("r_N_b", condition) avec {"estimation": rapport}.
"""
THETA_ABS, THETA_REL = 0.04, 1.20          # S1, S2
DELTA, DELTA_NON = 0.025, 0.015            # S5, S6
MARGE_NR = -0.02                           # S7
SEUIL_J = 0.0                              # S14
AUDIT_ABS, AUDIT_ORACLE = 0.12, 0.9        # S10
S3_FORME, S4_REGLE, S17_OPTION = "F-A", "R-A", 1
X2 = ("M_bien", "M_moyen")


def detecte(r, delta=DELTA):
    if S4_REGLE == "R-A":
        return r["estimation"] >= delta and r["lb95"] > 0
    return r["lb95"] >= delta


def booleens(c, s17_option=S17_OPTION):
    b = {}
    for X in X2:
        d = lambda nom: c[(nom, X)]
        b[("perd", X)] = d("N-b")["ub95"] < 0
        b[("A1", X)] = d("N-b")["estimation"] >= THETA_ABS and c[("r_N_b", X)]["estimation"] >= THETA_REL \
            and d("N-b")["lb95"] > 0
        a2 = d("N-a")["lb95"] > 0 and d("N-d1")["lb95"] > 0 and d("N-d1c")["lb95"] > 0
        if s17_option == 1:
            a2 = a2 and d("N-b_eloigne")["lb95"] > 0
        b[("A2", X)] = a2
        b[("suffit_d1c", X)] = d("N-d1c")["ub95"] <= 0
        b[("suffit_d1", X)] = d("N-d1")["ub95"] <= 0
        b[("suffit_b_eloigne", X)] = d("N-b_eloigne")["ub95"] <= 0
        b[("D0", X)] = detecte(d("N-N_beta0"))
        b[("A7", X)] = b[("D0", X)] if S3_FORME == "F-A" else d("N-N_beta0")["lb95"] > 0
        b[("J", X)] = d("d1c-c")["lb95"] > SEUIL_J
        b[("N0", X)] = d("N-N_beta0")["ub95"] < DELTA_NON
        b[("NF", X)] = d("N-N_filtre")["ub95"] < DELTA_NON
        b[("DF", X)] = detecte(d("N-N_filtre"))
        b[("PG", X)] = d("N-N_PCg")["lb95"] > 0
    b["A3"] = not any(c[(k, "SP")]["lb99"] > 0 or c[(k, "SP")]["ub99"] < 0
                      for k in ("SP:N-b", "SP:N-d1c", "SP:N-N_beta0"))
    b["A4"] = c[("INV-M_bien", "INV")]["ub95"] < 0
    b["A5"] = c[("N-b", "NR_bien")]["lb99"] >= MARGE_NR and c[("N-b", "NR_moyen")]["lb99"] >= MARGE_NR
    b["A6"] = c[("V_fuite-M_bien", "V_fuite")]["ub95"] < 0
    ine = c[("N-N_beta0", "M_inertes")]
    b["A8"] = ine["lb95"] <= 0 and ine["ub95"] < DELTA_NON
    b["gain_controle"] = any(c[("N_PCg-N_beta0", X)]["lb99"] > 0 for X in X2) or ine["lb95"] > 0
    return b


def table1(b, v0, declencheur_audit, audit_rendu, artefact, s17_option=S17_OPTION):
    tous = lambda k: b[(k, "M_bien")] and b[(k, "M_moyen")]
    if not v0:
        return 0, "non concluant"
    if declencheur_audit and not audit_rendu:
        return 1, "non concluant (audit en attente)"
    if audit_rendu and artefact:
        return 2, "non concluant ; version nouvelle"
    if b[("perd", "M_bien")] or b[("perd", "M_moyen")]:
        return 3, "N perd contre le stratifié"
    if not tous("A1"):
        return 4, "N sous le seuil"
    if not (b["A4"] and b["A5"] and b["A6"] and b["A8"]) or b["gain_controle"]:
        return 5, "contrôle en défaut"
    if tous("suffit_d1c"):
        return 6, "Swanson guidé par concepts suffit"
    if tous("suffit_d1"):
        return 7, "Swanson par opérateur suffit"
    if not tous("J"):
        return 8, "non concluant : canal non jugeable"
    if not tous("A7") or b[("N0", "M_bien")] or b[("N0", "M_moyen")]:
        return 9, "l'éloignement suffit : N_beta0 ou b_eloigne, pas N"
    if s17_option == 1 and tous("suffit_b_eloigne"):
        return "9 bis", "l'éloignement par strates de v1 suffit : b_eloigne, pas N"
    if tous("A2"):
        return 10, "N adoptée, sous W1 à W4"
    return 11, "indécis"


def table2(b, v0, declencheur_audit, audit_rendu, artefact):
    tous = lambda k: b[(k, "M_bien")] and b[(k, "M_moyen")]
    if not v0:
        return 0, "non concluant"
    if declencheur_audit and not audit_rendu:
        return 1, "non concluant (audit en attente)"
    if audit_rendu and artefact:
        return 2, "non concluant ; version nouvelle"
    if b["gain_controle"]:
        return 3, "non : gain quand le concept est inerte ou permuté"
    if not tous("J"):
        return 4, "non concluant : canal non jugeable"
    if tous("N0"):
        return 5, "non : le terme de concept n'apporte rien"
    if tous("D0") and tous("NF"):
        return 6, "non : le concept suffit comme filtre"
    if tous("D0") and tous("DF") and tous("PG") and b["A8"]:
        return 7, "oui, sous W1 à W4"
    return 8, "indécis"


# Audit R4, troisième puce : « N identique au bit près à N_global, N_β0 ou à un témoin sur tous les mondes d'une
# condition, hors identités déclarées d'avance (N ≡ N_β0 dans V_concepts_absents ; d1c ≡ d1 dans NR_bien et NR_moyen) ».
# Témoins au sens du § 4 : b, a, d1, d1c, b_eloigne, et la référence c.
BRAS_IDENTITE_AUDIT = ("N_global", "N_beta0", "b", "a", "d1", "d1c", "c", "b_eloigne")
IDENTITES_DECLAREES = {("V_concepts_absents", "N", "N_beta0"), ("NR_bien", "d1c", "d1"), ("NR_moyen", "d1c", "d1")}


def identites_audit(identites):
    """`identites` : {condition : [bras identiques à N sur tous les mondes non exclus]} (invocation_unique_v2).
    Rend (identités qui déclenchent l'audit, identités rapportées sans déclencher : hors liste du texte ou déclarées
    d'avance)."""
    declenche, rapporte = {}, {}
    for cond, bras in identites.items():
        for x in bras:
            declaree = (cond, "N", x) in IDENTITES_DECLAREES or (cond, x, "N") in IDENTITES_DECLAREES
            cible = declenche if (x in BRAS_IDENTITE_AUDIT and not declaree) else rapporte
            cible.setdefault(cond, []).append(x)
    return declenche, rapporte


def declencheurs_audit(c, b, prec_N, prec_oracle, identites, j_miroirs, fuite_F, concordance_verite):
    """Déclencheurs de l'audit de symétrie (R4) ; rend la liste des déclencheurs présents. `identites` :
    {condition : [bras identiques à N]} ; filtrées par `identites_audit`. `concordance_verite` : {condition :
    concordance} (mesures_v2.concordance_verite, conditions de décision v2) ou un nombre ; None : non calculée."""
    d = []
    if any(abs(c[("N-b", X)]["estimation"]) >= AUDIT_ABS for X in X2):
        d.append("|Δ(N, b)| ≥ S10")
    if any(prec_N[X] >= AUDIT_ORACLE * prec_oracle[X] for X in prec_N):
        d.append("précision de N ≥ 0,9 × oracle")
    declenche, _ = identites_audit(identites or {})
    if declenche:
        d.append(f"identités non déclarées : {declenche}")
    if not b["A3"] or b["gain_controle"]:
        d.append("écart de contrôle excluant 0")
    if j_miroirs:
        d.append("J vraie sur les miroirs de validation de M_inertes (V9)")
    if any(c[("N-a", X)]["ub95"] <= 0 for X in X2):
        d.append("N ne bat pas la forme corrigée (P15)")
    if fuite_F is not None and abs(fuite_F) <= 1e-12:
        d.append("fuite F exactement nulle")
    if concordance_verite is not None:
        valeurs = concordance_verite.values() if isinstance(concordance_verite, dict) else [concordance_verite]
        if any(v is not None and v > 0.99 for v in valeurs):
            d.append("concordance des étiquettes avec la vérité > 0,99")
    return d
