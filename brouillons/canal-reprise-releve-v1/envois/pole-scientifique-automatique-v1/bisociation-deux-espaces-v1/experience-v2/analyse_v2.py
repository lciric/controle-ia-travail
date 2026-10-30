"""Contrastes du § 7 et estimateurs de la Métrique, calculés à partir des lignes de résultats par monde.

Entrée : pour chaque condition, la liste des lignes rendues par `mesures_v2.executer_monde` (dictionnaires simples).
Sortie : un dictionnaire {« nom|condition » : résumé} sérialisable, avec estimation, bornes à 95 % et 99 %, nombre de
mondes ; `charger_pour_lecture` le met sous la forme {(nom, condition) : résumé} qu'attend `lecture_v2`.

Graines de rééchantillonnage : rôle 99, `spawn_key = (code de condition où le contraste est calculé, code du
contraste, 99)`, plus un second flux `(…, 99, 1)` pour un écart entre ensembles distincts (14, 15, 39) ; un seul flux
pour l'écart apparié 10 (§ 7). Aucune de ces fonctions n'est appelée par les bras ni par les essais sur de vrais
mondes : les essais l'appellent sur des tableaux synthétiques (R1).
"""
import numpy as np

from controle_ia.gardes import GardeArret

import bras_v2 as br
import graines_v2 as gr
import mesures_v2 as ms

# Code de contraste du rééchantillonnage de la non-régression (C11, A5) : le § 7 dit seulement que C11 est « sans code
# de contraste ». Fixé par Lazar (R-585, confirmé R-600 ; addendum v2, Q-03) : 16, clés (10, 16, 99) et (11, 16, 99).
CODE_CONTRASTE_NR = 16

CONDITIONS_DECISION = ("M_bien", "M_moyen", "SP", "INV", "V_fuite", "M_inertes", "NR_bien", "NR_moyen")
CONDITIONS_DESCRIPTIVES = ("M_mal", "V_concepts_absents", "V_moyeu_conceptuel", "V_surface", "M_couplage_faible",
                           "M_palettes_communes", "M_palettes_disjointes", "M_fonds_1ou2")

# (code, nom, bras X, bras Y) : contrastes appariés par monde dans une condition ordinaire (décisifs 1 à 9, 20 ; descriptifs)
CONTRASTES_APPARIES = [
    (1, "N-b", "N", "b"), (2, "N-a", "N", "a"), (3, "N-d1", "N", "d1"), (4, "N-d1c", "N", "d1c"),
    (5, "N-N_beta0", "N", "N_beta0"), (6, "N-N_filtre", "N", "N_filtre"), (7, "N-N_PCg", "N", "N_PCg"),
    (8, "N_PCg-N_beta0", "N_PCg", "N_beta0"), (9, "d1c-c", "d1c", "c"),
    (20, "N-b_eloigne", "N", "b_eloigne"), (21, "N-N_aleat", "N", "N_aleat"), (22, "N-N_global", "N", "N_global"),
    (23, "N-N_dpp", "N", "N_dpp"), (24, "N-N_fiches", "N", "N_fiches"), (25, "N-N_q", "N", "N_q"),
    (26, "N-N_rare", "N", "N_rare"), (27, "N-N_alpha0", "N", "N_alpha0"), (28, "N-N_PC", "N", "N_PC"),
    (29, "N_dpp-N_dpp_beta0", "N_dpp", "N_dpp_beta0"), (30, "N_PC-N_beta0", "N_PC", "N_beta0"),
    (31, "N_PC-N_PCg", "N_PC", "N_PCg"), (32, "N_dpp-N_global", "N_dpp", "N_global"),
    (33, "b_eloigne-b", "b_eloigne", "b"), (34, "N_beta0-b", "N_beta0", "b"), (35, "d1-b", "d1", "b"),
    (36, "d1c-b", "d1c", "b"), (37, "a-b", "a", "b"), (38, "c-b", "c", "b"),
]
CODE_SP = {"SP:N-b": (11, "N", "b"), "SP:N-d1c": (12, "N", "d1c"), "SP:N-N_beta0": (13, "N", "N_beta0")}
CODE_INV, CODE_V_FUITE, CODE_ECART_INERTES, CODE_FONDS = 14, 15, 10, 39
CODE_N_B = 1  # contraste 1, Δ(N, b)
BRAS_PRECISION = [b for b in br.ORDRE_BRAS if b != "N_grille"]  # N_grille : validation seulement (§ 5, § 9)


def _valeurs(lignes, bras, cle="precision"):
    """{indice : valeur} des mondes non exclus où le bras est présent (un bras non applicable est absent)."""
    out = {}
    for l in lignes:
        if l["exclu"]:
            continue
        m = (l.get("bras") or {}).get(bras)
        if m is not None:
            out[l["indice"]] = m[cle]
    return out


def _apparie(lignes, x, y, cle="precision"):
    vx, vy = _valeurs(lignes, x, cle), _valeurs(lignes, y, cle)
    if not vx or not vy:
        return None
    communs = sorted(set(vx) & set(vy))
    if set(vx) != set(vy):
        raise GardeArret(f"bras {x} et {y} : mondes notés différents ({len(vx)} contre {len(vy)})")
    return np.array([vx[i] for i in communs]), np.array([vy[i] for i in communs]), communs


def deltas(lignes, x, y, cle="precision"):
    """Vecteur par monde de π(x) − π(y), indexé par l'indice du monde ; None si un des bras est non applicable."""
    a = _apparie(lignes, x, y, cle)
    if a is None:
        return None
    return dict(zip(a[2], (a[0] - a[1]).tolist()))


def contraste_apparie(lignes, x, y, racine, code_condition, code_contraste, cle="precision"):
    a = _apparie(lignes, x, y, cle)
    if a is None:
        return {"non_applicable": True}
    return ms.ecart_apparie(a[0], a[1], ms.rng_contraste(racine, code_condition, code_contraste))


def rapport_moyennes(lignes, x, y):
    vx, vy = _valeurs(lignes, x), _valeurs(lignes, y)
    if not vx or not vy:
        return None
    mx, my = float(np.mean(list(vx.values()))), float(np.mean(list(vy.values())))
    if my == 0.0:
        raise GardeArret(f"r({x}, {y}) : moyenne nulle au dénominateur")
    return mx / my


def precisions_moyennes(lignes, racine, code_condition):
    """Contrastes 40 + rang du bras : précision moyenne d'un bras (percentiles de 2 000 rééchantillonnages)."""
    out = {}
    for b in BRAS_PRECISION:
        v = _valeurs(lignes, b)
        if not v:
            out[b] = {"non_applicable": True}
            continue
        arr = np.array(list(v.values()))
        r = ms.ecart_apparie(arr, np.zeros_like(arr), ms.rng_contraste(racine, code_condition, 40 + br.RANG[b]))
        out[b] = r
    return out


def par_nombre_de_champs(lignes):
    """Résultats par nombre de champs (2, 3, 4) : estimation de Δ(N, b) et nombre de mondes ; pas d'intervalle (le § 7
    ne donne aucun code de graine pour ce découpage : Q-09)."""
    out = {}
    for f in (2, 3, 4):
        sous = [l for l in lignes if not l["exclu"] and l.get("n_champs") == f]
        d = deltas(sous, "N", "b")
        out[str(f)] = {"n": len(sous), "delta_N_b": float(np.mean(list(d.values()))) if d else None}
    return out


def calculer_condition(lignes, condition, racine):
    """Contrastes d'une condition ordinaire (M_bien, M_moyen, M_inertes, M_mal, V_*, M_*) ; SP et NR ont leurs fonctions."""
    code = gr.CODES_CONDITION[condition]
    res = {}
    for c, nom, x, y in CONTRASTES_APPARIES:
        res[nom] = contraste_apparie(lignes, x, y, racine, code, c)
    res["r_N_b"] = {"estimation": rapport_moyennes(lignes, "N", "b")}
    res["precisions"] = precisions_moyennes(lignes, racine, code)
    res["par_nombre_de_champs"] = par_nombre_de_champs(lignes)
    return res


def calculer_sp(lignes, racine):
    code = gr.CODES_CONDITION["SP"]
    return {nom: contraste_apparie(lignes, x, y, racine, code, c, cle="precision_placebo")
            for nom, (c, x, y) in CODE_SP.items()}


def calculer_nr(lignes, condition, racine, code_contraste=None):
    """C11 : Δ(N, b) à 99 % sur les mondes v1 ; et moyennes des témoins b, a, c, d1 pour la reproduction (liste d'arrêt)."""
    code_contraste = CODE_CONTRASTE_NR if code_contraste is None else code_contraste
    if code_contraste is None:
        raise GardeArret("code de contraste de la non-régression non fixé (Q-03 de ecarts-et-questions-v1.md) : arrêt")
    code = gr.CODES_CONDITION[condition]
    res = {"N-b": contraste_apparie(lignes, "N", "b", racine, code, code_contraste)}
    res["moyennes_temoins"] = {b: float(np.mean(list(_valeurs(lignes, b).values()))) for b in ("b", "a", "c", "d1")}
    return res


def ecart_entre_conditions(lignes_a, lignes_b, racine, code_condition, code_contraste, x, y):
    """Contrastes 14, 15, 39 : Δ(x, y ; A) − Δ(x, y ; B), ensembles de mondes distincts, deux flux (§ 7)."""
    da, db = deltas(lignes_a, x, y), deltas(lignes_b, x, y)
    if da is None or db is None:
        return {"non_applicable": True}
    return ms.ecart_entre_ensembles(list(da.values()), list(db.values()),
                                    ms.rng_contraste(racine, code_condition, code_contraste, second=False),
                                    ms.rng_contraste(racine, code_condition, code_contraste, second=True))


def ecart_apparie_inertes(lignes_bien, lignes_inertes, racine):
    """Contraste 10 (descriptif) : Δ(N, N_β0 ; M_bien) − Δ(N, N_β0 ; M_inertes), monde à monde sur des latents
    identiques ; un seul flux (1, 10, 99) ; mondes non exclus dans les deux conditions."""
    da, db = deltas(lignes_bien, "N", "N_beta0"), deltas(lignes_inertes, "N", "N_beta0")
    communs = sorted(set(da) & set(db))
    if not communs:
        raise GardeArret("contraste 10 : aucun monde commun à M_bien et M_inertes")
    d = np.array([da[i] - db[i] for i in communs])
    r = ms.ecart_apparie(d, np.zeros_like(d), ms.rng_contraste(racine, gr.CODES_CONDITION["M_bien"], CODE_ECART_INERTES))
    r["n_mondes_exclus_d_un_cote"] = len(set(da) ^ set(db))
    return r


def calculer_tout(par_condition, racine, code_contraste_nr=None):
    """Tous les contrastes du § 7 à partir de {condition : lignes}. Rend le dictionnaire plat {« nom|condition » : résumé}."""
    out = {}
    for cond, lignes in par_condition.items():
        if cond == "SP":
            for nom, r in calculer_sp(lignes, racine).items():
                out[f"{nom}|SP"] = r
        elif cond in ("NR_bien", "NR_moyen"):
            for nom, r in calculer_nr(lignes, cond, racine, code_contraste_nr).items():
                out[f"{nom}|{cond}"] = r
        else:
            for nom, r in calculer_condition(lignes, cond, racine).items():
                out[f"{nom}|{cond}"] = r
    if "INV" in par_condition and "M_bien" in par_condition:
        out["INV-M_bien|INV"] = ecart_entre_conditions(par_condition["INV"], par_condition["M_bien"], racine,
                                                        gr.CODES_CONDITION["INV"], CODE_INV, "N", "b")
    if "V_fuite" in par_condition and "M_bien" in par_condition:
        out["V_fuite-M_bien|V_fuite"] = ecart_entre_conditions(
            par_condition["V_fuite"], par_condition["M_bien"], racine, gr.CODES_CONDITION["V_fuite"], CODE_V_FUITE,
            "N", "b")
    if "M_fonds_1ou2" in par_condition and "M_bien" in par_condition:
        out["fonds_1ou2-M_bien|M_fonds_1ou2"] = ecart_entre_conditions(
            par_condition["M_fonds_1ou2"], par_condition["M_bien"], racine, gr.CODES_CONDITION["M_fonds_1ou2"],
            CODE_FONDS, "N", "N_beta0")
    if "M_inertes" in par_condition and "M_bien" in par_condition:
        out["ecart_M_bien-M_inertes|M_inertes"] = ecart_apparie_inertes(par_condition["M_bien"],
                                                                         par_condition["M_inertes"], racine)
    return out


def charger_pour_lecture(plat):
    """{« nom|condition » : résumé} -> {(nom, condition) : résumé}, clés attendues par lecture_v2.booleens."""
    c = {}
    for k, v in plat.items():
        nom, cond = k.rsplit("|", 1)
        c[(nom, cond)] = v
    return c
