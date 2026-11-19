"""Papier C — analyse de l'étape 2, de bout en bout, sur tableaux (v1).

Texte de référence : version r1 (`e12f16fa…`), Plan d'analyse, section 3 (TC.1 à TC.3) et section 5 (comparaisons
multiples) ; « Critères de lecture gelés ». Fonction pure `analyser_etape2(donnees, configuration, generateurs)` :
des tableaux de lectures et de scores déjà agrégés en entrée, toutes les lignes, tous les verdicts et toutes les
réserves en sortie. Aucune lecture de fichier, aucun modèle. Toute ligne est calculée et écrite quel que soit le
signe (R3).

Forme de `donnees` (les essais en donnent un exemple simulé complet, `tests/simulation_papier_c_v1.py`) :
- `corpus_A` : `taches` (tâche de chaque contenu), `saboteur` (booléens), `juges` : liste de trois dictionnaires
  {`v0` (n), `familles` {famille: {`v` (k_f, n), `temoins` [indice du témoin de chaque rang]}}, `temoins`
  {indice: lectures (n)} pour les témoins retenus, `constat` {`v` (n), `temoin` indice}, `neutres` (6),
  `alarme` {`temoins`, `tache_temoins`, `ordres`, `tache_ordres`}} ;
- `corpus_B` : `items` (identifiant de chaque texte) et `juges` de même forme (sans `alarme`) ;
- `tc2` : `juges` : trois dictionnaires de cellules {H, S, HP (k_P, T), SP, HU, SU} (verdict de la consigne A en mode
  direct sur le contenu complet) ; `taches` (étiquettes des tâches, celles du corpus A) ; `sondes` : une entrée par sonde désignée {`nom`, `agregation`, `champs`,
  `complete`, `filtree` (cellules), `excedent` {SP, HP, SU, HU, L_HP, L_H}, `lecteur` {`champs` {H, S}, `excedent`
  {SP, HP}}, `lexical_mesure`} ; `controlabilite_mesuree`, `hc2_non_testable`.
"""
from __future__ import annotations

import itertools

import numpy as np

import papier_c_decisions_v1 as dec
import papier_c_rangs_v1 as rg
from papier_c_erreurs_v1 import ConfigurationInvalide
from papier_c_lois_v1 import (attracteur_propre, correlation_de_rang, forme_de_l_issue, loi_jointe, loi_nette,
                              loi_temoin, regresseur_calibre)
from papier_c_reechantillonnage_v1 import (clopper_pearson, comptes_par_grappes, effectif_efficace, intervalle_bca,
                                           intervalle_percentiles, niveau_bonferroni, p_bilateral, p_inferieur,
                                           p_superieur, poids_jackknife, poids_observes)
from papier_c_sondes_v1 import (comparaison_aux_juges, gain_d_ecart, gain_sur_l_excedent,
                                separation_parfaite_des_alarmes, taux_d_alarme)

FAMILLES = ("flatterie_supplication", "revendication_autorite", "approbations_forgees", "usurpation_stylistique",
            "ordres_en_bande")
FAMILLE_1, FAMILLE_4, FAMILLE_5 = FAMILLES[0], FAMILLES[3], FAMILLES[4]


class Poids:
    """Les trois jeux de poids d'un corpus : observé, tirages par grappes, jackknife sur les grappes."""

    def __init__(self, grappes, tirages: int, rng: np.random.Generator):
        g = np.asarray(grappes)
        self.grappes = g
        self.obs, self.tir, self.jack = poids_observes(g.size), comptes_par_grappes(g, tirages, rng), poids_jackknife(g)

    def par_grappe(self, etiquettes) -> "Poids":
        """Les mêmes tirages, ramenés à une unité par grappe (une colonne par étiquette demandée) : « mêmes tirages
        pour toutes les statistiques d'un corpus » (point 11) vaut ainsi pour les statistiques par tâche (gains
        d'écart, alarme) comme pour les statistiques par contenu."""
        premiers = []
        for e in np.asarray(etiquettes).tolist():
            ou = np.flatnonzero(self.grappes == e)
            if ou.size == 0:
                raise ConfigurationInvalide(f"grappe {e!r} absente du corpus")
            premiers.append(int(ou[0]))
        autre = object.__new__(Poids)
        autre.grappes = np.asarray(etiquettes)
        autre.obs, autre.tir, autre.jack = self.obs[:, premiers], self.tir[:, premiers], self.jack[:, premiers]
        return autre

    def trois(self, f):
        """Applique une statistique aux trois jeux de poids : (valeur observée, tirages, jackknife)."""
        return f(self.obs), f(self.tir), f(self.jack)


def _ic(obs, tir, jack, niveau: float) -> dict:
    return {"valeur": float(obs), "niveau": niveau, **intervalle_bca(float(obs), tir, jack, niveau)}


def _ic_de(trois: tuple, cle, niveau: float, indice=None) -> dict:
    def lire(d):
        v = d[cle] if not callable(cle) else cle(d)
        return v if indice is None else v[:, indice]
    return _ic(lire(trois[0])[0], lire(trois[1]), lire(trois[2]), niveau)


def _part(drapeaux) -> float:
    return float(np.mean(np.asarray(drapeaux, dtype=bool)))


# ------------------------------------------------------------------------------------------------------------------
# TC.1 : lois d'un juge sur un corpus
# ------------------------------------------------------------------------------------------------------------------
def _lois_du_juge(juge: dict, poids: Poids, v_etoile: float, e2: dict, saboteur=None) -> dict:
    v0 = np.asarray(juge["v0"], dtype=np.float64)
    indices = sorted(juge["temoins"])
    W = np.stack([np.asarray(juge["temoins"][t], dtype=np.float64) for t in indices])
    bornes_rho, bornes_c = tuple(e2["loi_nette"]["rho_borne"]), tuple(e2["tirage_degenere"]["c_hors_de"])
    ecart_min = e2["tirage_degenere"]["ecart_v_etoile_v0_min"]
    sortie = {"familles": {}, "v0": v0, "W": W}
    for nom, bloc in list(juge["familles"].items()) + ([("constat_nu", {"v": np.atleast_2d(juge["constat"]["v"]),
                                                                         "temoins": [juge["constat"]["temoin"]]})]
                                                       if "constat" in juge else []):
        V = np.atleast_2d(np.asarray(bloc["v"], dtype=np.float64))
        Wm = np.stack([np.asarray(juge["temoins"][t], dtype=np.float64) for t in bloc["temoins"]])
        if Wm.shape != V.shape:
            raise ConfigurationInvalide(f"{nom} : un témoin apparié par rang attendu")
        D = V - Wm
        lois = {l: poids.trois(lambda P, l=l: loi_nette(P, v0, D, W, v_etoile, l, bornes_rho, bornes_c, ecart_min))
                for l in rg.TOUTES_LES_LECTURES}
        brute = poids.trois(lambda P: loi_jointe(P, V - v0[None, :], v0))
        f = {"nette": lois, "brute": brute, "delta_net": D, "k": V.shape[0]}
        if saboteur is not None and nom != "constat_nu":
            f["intention"] = poids.trois(lambda P: loi_nette(P, v0, D, W, v_etoile, "calibree", bornes_rho, bornes_c,
                                                             ecart_min, saboteur=saboteur))
        sortie["familles"][nom] = f
    sortie["temoin"] = poids.trois(lambda P: loi_temoin(P, v0, W))
    return sortie


def _lignes_tc1_du_juge(lois: dict, juge: dict, v_etoile: float, e2: dict) -> dict:
    """C-P2, C-P1 et intensités graduées d'un juge sur le corpus A, plus les lignes rapportées."""
    seuil, niveau = e2["seuil_C_P2_C_P1"], e2["niveau"]
    cal = {f: lois["familles"][f]["nette"]["calibree"] for f in FAMILLES}
    brut = {f: lois["familles"][f]["nette"]["sans_calibrage"] for f in FAMILLES}
    G_tir = {f: cal[f][1]["G"] for f in FAMILLES}
    fam = dec.familles_d_un_juge([p_superieur(G_tir[f], 0.0) for f in FAMILLES],
                                 [p_inferieur(G_tir[f], 0.0) for f in FAMILLES], seuil)
    paires = list(itertools.combinations(range(len(FAMILLES)), 2))
    structure = dec.structure_d_un_juge({p: p_bilateral(G_tir[FAMILLES[p[0]]] - G_tir[FAMILLES[p[1]]], 0.0)
                                         for p in paires}, e2["seuil_structure_bilateral"])
    ic_temoin_c = _ic_de(lois["temoin"], "c", niveau)
    attracteur = attracteur_propre(juge["neutres"])
    entrees_c_p1, lignes = [], {}
    for k, f in enumerate(FAMILLES):
        bloc = lois["familles"][f]
        degeneres = _part(cal[f][1]["degenere"])
        entrees_c_p1.append({
            "positive": fam["positive"][k], "c": float(cal[f][0]["c"][0]), "part_degeneres": degeneres,
            "p_ajuste_G": fam["p_ajuste_positif"][k],
            "p_cible_calibree": p_superieur(cal[f][1]["lam"], 0.5), "p_cible_sans_calibrage": p_superieur(brut[f][1]["lam"], 0.5),
            "p_moyenne_calibree": p_inferieur(cal[f][1]["lam"], 0.5), "p_moyenne_sans_calibrage": p_inferieur(brut[f][1]["lam"], 0.5)})
        K = bloc["k"]
        pente = cal[f][1]["g"][:, K - 1] - cal[f][1]["g"][:, 0]
        ic_lam = _ic_de(cal[f], "lam", niveau)
        lignes[f] = {
            "G": _ic_de(cal[f], "G", niveau), "lambda": ic_lam, "c": _ic_de(cal[f], "c", niveau),
            "lambda_percentiles": intervalle_percentiles(cal[f][1]["lam"], niveau)[:2],
            "lambda_sans_calibrage": _ic_de(brut[f], "lam", niveau),
            "nul_cible_dans_l_intervalle": bool(ic_lam["bas"] <= 1.0 <= ic_lam["haut"]),
            "nul_moyenne_dans_l_intervalle": bool(ic_lam["bas"] <= 0.0 <= ic_lam["haut"]),
            "g_par_rang": [float(x) for x in cal[f][0]["g"][0]], "g_rang_fort": float(cal[f][0]["g"][0, K - 1]),
            "correlation_rang_gain": correlation_de_rang(np.arange(1, K + 1), cal[f][0]["g"][0]),
            "c_par_rang": [_ic_de(cal[f], "c_par_rang", niveau, m) for m in range(K)],
            "r2_joint": float(cal[f][0]["r2"][0]), "part_degeneres": degeneres,
            "non_identifiable_par_tirages": degeneres > e2["part_tirages_degeneres_max"],
            "positive": fam["positive"][k], "negative": fam["negative"][k],
            "p_ajuste_positif": fam["p_ajuste_positif"][k], "p_ajuste_negatif": fam["p_ajuste_negatif"][k],
            "intensites": dec.intensites_graduees(p_superieur(pente, 0.0), e2["niveau_intensites_graduees"]),
            "brute": {"G": _ic_de(bloc["brute"], "G", niveau), "c": _ic_de(bloc["brute"], "c", niveau)},
            "ecart_intention": _ic((bloc["intention"][0]["c"] - cal[f][0]["c"])[0], bloc["intention"][1]["c"] - cal[f][1]["c"],
                                   bloc["intention"][2]["c"] - cal[f][2]["c"], niveau) if "intention" in bloc else None,
            "audit": {}}
        G_temoin, G_brut = float(lois["temoin"][0]["G"][0]), float(bloc["brute"][0]["G"][0])
        lignes[f]["audit"]["A1"] = dec.audit_a1(G_temoin, G_brut)
        lignes[f]["audit"]["A2"] = dec.audit_a2(float(bloc["brute"][0]["c"][0]), ic_temoin_c)
        lignes[f]["audit"]["A5"] = dec.audit_a5(r2_joint_net=lignes[f]["r2_joint"],
                                               largeur_ic_lambda=ic_lam["haut"] - ic_lam["bas"],
                                               seuil_r2=e2["seuils_audit_R4"]["r2_joint"],
                                               seuil_largeur=e2["seuils_audit_R4"]["largeur_lambda"])
        X = regresseur_calibre(lois["v0"], lois["W"], "calibree", tuple(e2["loi_nette"]["rho_borne"]))
        forme = forme_de_l_issue(bloc["delta_net"][K - 1], X, float(cal[f][0]["c"][0]),
                                 e2["seuils_audit_R4"]["forme_issue"]["sous"], e2["seuils_audit_R4"]["forme_issue"]["au_dessus"])
        lignes[f]["audit"]["A7"] = {"forme": forme, "reserves": dec.audit_a7(
            forme["part_cumulee"], e2["seuils_audit_R4"]["forme_issue"]["part_cumulee_bascule"])}
    c_p1 = dec.lectures_c_p1_d_un_juge(entrees_c_p1, seuil, e2["reserve_gain_faible_p_ajuste"],
                                       e2["part_tirages_degeneres_max"], tuple(e2["intervalle_c_recherche"]))
    for k, f in enumerate(FAMILLES):
        lignes[f]["c_p1"] = c_p1[k]
        lignes[f]["c_p1"]["reserves"] += lignes[f]["intensites"]["reserves"]
    # C-P1b : écarts appariés λ_f − λ_f' entre familles identifiables, mêmes tirages, Holm sur les paires du juge
    ident = [k for k in range(len(FAMILLES)) if c_p1[k]["identifiable"]]
    c_p1b = None
    if len(ident) >= 2:
        c_p1b = dec.holm_des_paires({(a, b): p_bilateral(cal[FAMILLES[a]][1]["lam"] - cal[FAMILLES[b]][1]["lam"], 0.0)
                                     for a, b in itertools.combinations(ident, 2)})
    cal0 = cal[FAMILLES[0]][0]["calibrage"]
    constat = None
    if "constat_nu" in lois["familles"]:
        cn = lois["familles"]["constat_nu"]["nette"]["calibree"]
        constat = {"g": _ic_de(cn, "G", niveau), "c": _ic_de(cn, "c", niveau),
                   "contrastes": {f: {"G_moins_g_constat": _ic((cal[f][0]["G"] - cn[0]["G"])[0], cal[f][1]["G"] - cn[1]["G"],
                                                                 cal[f][2]["G"] - cn[2]["G"], niveau),
                                      "g_rang_fort_moins_g_constat": _ic(
                                          (cal[f][0]["g"][:, -1] - cn[0]["G"])[0], cal[f][1]["g"][:, -1] - cn[1]["G"],
                                          cal[f][2]["g"][:, -1] - cn[2]["G"], niveau)} for f in FAMILLES},
                   "verdict": None}
    return {"familles": lignes, "structure": structure, "c_p1b_p_ajustes": c_p1b, "attracteur": attracteur,
            "temoin": {"c": ic_temoin_c, "G": _ic_de(lois["temoin"], "G", niveau)},
            "calibrage": {"rho": float(cal0["rho"][0]), "rho_brut": float(cal0["rho_brut"][0]), "r": float(cal0["r"][0]),
                          "sigma": float(cal0["sigma"][0]),
                          "part_des_tirages_ou_rho_touche_une_borne": _part(cal[FAMILLES[0]][1]["calibrage"]["touche_borne"])},
            "constat_nu": constat,
            "audit_A6": dec.audit_a6(G_nets_du_juge=[float(cal[f][0]["G"][0]) for f in FAMILLES])}


def _G(lois_des_juges: list, lecture: str, jeu: int) -> np.ndarray:
    """Tableau (…, familles, juges) des Ḡ nets d'une lecture, pour un jeu de poids (0 observé, 1 tirages)."""
    blocs = [[lois["familles"][f]["nette"][lecture][jeu]["G"] for lois in lois_des_juges] for f in FAMILLES]
    return np.moveaxis(np.array(blocs), -1, 0)      # (R, familles, juges)


# ------------------------------------------------------------------------------------------------------------------
# TC.2 et TC.3 b : sondes et juges sous le plaidoyer et l'usurpation de l'agent
# ------------------------------------------------------------------------------------------------------------------
def _gains(cellules: dict, poids: Poids, agregation: str) -> dict:
    P = poids.trois(lambda p: gain_d_ecart(p, cellules["H"], cellules["S"], cellules["HP"], cellules["SP"], agregation))
    U = poids.trois(lambda p: gain_d_ecart(p, cellules["H"], cellules["S"], cellules["HU"], cellules["SU"], agregation))
    return {"plaidoyer": P, "usurpation": U}


def _ligne_sonde(sonde: dict, juges_gains: list, poids: Poids, m: int, e2: dict, niveaux: dict, tc2: dict) -> dict:
    hc2_cfg, marge = e2["hc2"], e2["hc2"]["marge"]
    agregation = sonde["agregation"]
    champs, complete, filtree = (_gains(sonde[l], poids, agregation) for l in ("champs", "complete", "filtree"))
    P = champs["plaidoyer"]
    k_P = P[0]["g_brut"].shape[1]
    n90, n95 = niveau_bonferroni(1 - hc2_cfg["niveau_confirmation"], m), niveau_bonferroni(1 - hc2_cfg["niveau_refutation"], m)
    n_niveau = niveau_bonferroni(1 - hc2_cfg["niveau_refutation"], m * k_P)
    d0 = _ic_de(P, "D0", e2["niveau"])
    d0_ok = dec.prerequis_d0(d0)
    ic_moy95, ic_moy90 = _ic_de(P, "G_brut", n95), _ic_de(P, "G_brut", n90)
    ic90 = [_ic_de(P, "g_brut", n90, k) for k in range(k_P)]
    ic_corr = [_ic_de(P, "g_brut", n_niveau, k) for k in range(k_P)]
    degeneres = _part(P[1]["degenere"])
    hc2 = dec.verdict_hc2(ic90, ic_moy95, ic_corr, ic_moy90, d0_ok, agregation, bool(tc2.get("hc2_non_testable")), marge)
    # la même règle sur la lecture complète (rapportée), pour l'audit A8
    Pc = complete["plaidoyer"]
    hc2_complete = dec.verdict_hc2([_ic_de(Pc, "g_brut", n90, k) for k in range(k_P)], _ic_de(Pc, "G_brut", n95),
                                   [_ic_de(Pc, "g_brut", n_niveau, k) for k in range(k_P)], _ic_de(Pc, "G_brut", n90),
                                   dec.prerequis_d0(_ic_de(Pc, "D0", e2["niveau"])), agregation, False, marge)
    porte = dec.ligne_porte_gc(ic_moy95, d0_ok)
    # HC2b : excédent du paragraphe, D₀ sur les champs seuls
    ex = sonde["excedent"]
    H, S = sonde["champs"]["H"], sonde["champs"]["S"]
    trahison = poids.trois(lambda p: gain_sur_l_excedent(p, ex["SP"], ex["HP"], H, S, agregation))
    hc2b = dec.verdict_hc2b(_ic_de(trahison, "g", n95), _ic_de(trahison, "g", n90), d0_ok, agregation, marge)
    filtre = _ic_de(filtree["plaidoyer"], "G_did", e2["niveau"])
    lexical = None
    if sonde.get("lexical_mesure"):
        lex = poids.trois(lambda p: gain_sur_l_excedent(p, ex["SP"], ex["L_HP"], H, S, agregation))
        lex_h = poids.trois(lambda p: gain_sur_l_excedent(p, ex["SP"], ex["L_H"], H, S, agregation))
        lexical = {"L-HP": _ic_de(lex, "g", e2["niveau"]), "L-H": _ic_de(lex_h, "g", e2["niveau"]), "verdict": None}
    # C-P4b : d = g_lecteur − g_auteur, chacun sur l'excédent, D₀ de chaque côté sur les cellules S et H
    lec = sonde["lecteur"]
    g_lecteur = poids.trois(lambda p: gain_sur_l_excedent(p, lec["excedent"]["SP"], lec["excedent"]["HP"],
                                                          lec["champs"]["H"], lec["champs"]["S"], agregation))
    d0_lecteur_ok = dec.prerequis_d0(_ic_de(g_lecteur, "D0", e2["niveau"]))
    ic_d = _ic((g_lecteur[0]["g"] - trahison[0]["g"])[0], g_lecteur[1]["g"] - trahison[1]["g"],
               g_lecteur[2]["g"] - trahison[2]["g"], n95)
    c_p4b = dec.verdict_c_p4b(ic_d, d0_ok and d0_lecteur_ok)
    # C-P4c : comparaison aux juges, par juge
    couples = []
    for jg in juges_gains:
        comp = tuple(comparaison_aux_juges(jg["gains"]["plaidoyer"][i], P[i], Pc[i], trahison[i]) for i in range(3))
        couples.append({"interpretable": bool(jg["d0_ok"] and d0_ok),
                        "ic_e": _ic_de(comp, "e", n95), "ic_e_c": _ic_de(comp, "e_c", n95), "ic_e_x": _ic_de(comp, "e_x", n95)})
    opposition = dec.opposition_d_une_sonde(couples)
    # C-P6, sondes : gain d'écart brut sous l'usurpation, champs seuls
    U = champs["usurpation"]
    c_p6 = dec.lecture_sonde_c_p6(_ic_de(U, "G_brut", n90), _ic_de(U, "G_brut", n95), d0_ok, agregation, marge)
    ic_eq = _ic_de(U, "G_brut", n90)
    return {"nom": sonde["nom"], "agregation": agregation, "D0": d0, "d0_interpretable": d0_ok,
            "part_degeneres": degeneres, "non_identifiable_par_tirages": degeneres > e2["part_tirages_degeneres_max"],
            "hc2": hc2, "g_par_niveau": ic90, "g_par_niveau_corrige": ic_corr, "G_P": ic_moy95, "G_P_90": ic_moy90,
            "pente": _ic_de(P, "pente_brute", e2["niveau"]),
            "correlation_rang_gain": correlation_de_rang(np.arange(1, k_P + 1), P[0]["g_brut"][0]),
            "rapportes": {"difference_des_differences_champs": _ic_de(P, "G_did", e2["niveau"]),
                          "lecture_complete": _ic_de(Pc, "G_brut", n95), "hc2_lecture_complete": hc2_complete["verdict"],
                          "lecture_filtree": {"G_brut": _ic_de(filtree["plaidoyer"], "G_brut", e2["niveau"]),
                                              "G_did": filtre,
                                              "usurpation": _ic_de(filtree["usurpation"], "G_brut", e2["niveau"])},
                          "usurpation_did": _ic_de(U, "G_did", e2["niveau"]),
                          "usurpation_lecture_complete": _ic_de(complete["usurpation"], "G_brut", n95)},
            "porte_GC": porte, "hc2b": hc2b, "g_trahison": _ic_de(trahison, "g", n95), "temoin_lexical": lexical,
            "c_p4b": c_p4b, "d": ic_d, "c_p4c": {"couples": couples, "opposition": opposition},
            "c_p6": {"lecture": c_p6, "g_usurpation": _ic_de(U, "G_brut", n95), "equivalence": ic_eq},
            "audit": {"A8": dec.audit_a8(hc2["issue_de_la_regle"] or hc2["verdict"],
                                         hc2_complete["issue_de_la_regle"] or hc2_complete["verdict"]),
                      "A5": dec.audit_a5(largeur_equivalence=ic_eq["haut"] - ic_eq["bas"],
                                         seuil_largeur=e2["seuils_audit_R4"]["largeur_equivalence"])},
            "_combinaison": {"hc2": hc2, "hc2b": hc2b, "porte": porte, "filtre": filtre, "lexical": lexical,
                             "ic_moy95": ic_moy95, "niveaux": niveaux}}


# ------------------------------------------------------------------------------------------------------------------
# Analyse complète
# ------------------------------------------------------------------------------------------------------------------
def analyser_etape2(donnees: dict, configuration: dict, generateurs: dict) -> dict:
    """Analyse décisive de l'étape 2. `generateurs` : {`reechantillonnage`, `permutations`} — deux générateurs dérivés
    des clés `papier-C/etape2/reechantillonnage` et `papier-C/etape2/permutations`. Les tirages du corpus A (par
    tâches) et du corpus B (par items) sont indépendants ; ceux de TC.2 sont tirés par tâches, à part."""
    e2, sr = configuration["etape2"], configuration["stabilite_rang"]
    B, niveau = int(e2["tirages"]), e2["niveau"]
    rng = generateurs["reechantillonnage"]
    A, Bc, tc2 = donnees["corpus_A"], donnees["corpus_B"], donnees["tc2"]
    v_etoile_A = configuration["consignes"]["A_standard"]["cible_attaquant_v_etoile"]
    v_etoile_B = configuration["consignes"]["B_standard"]["cible_attaquant_v_etoile"]
    if len(A["juges"]) != 3 or len(Bc["juges"]) != 3 or len(tc2["juges"]) != 3:
        raise ConfigurationInvalide("trois juges attendus dans chaque bloc")
    poids_A, poids_B = Poids(A["taches"], B, rng), Poids(Bc["items"], B, rng)
    poids_T = poids_A.par_grappe(tc2["taches"])          # tâches de TC.2 : celles du corpus A, mêmes tirages
    saboteur = np.asarray(A["saboteur"], dtype=bool)
    lois_A = [_lois_du_juge(j, poids_A, v_etoile_A, e2, saboteur) for j in A["juges"]]
    lois_B = [_lois_du_juge(j, poids_B, v_etoile_B, e2) for j in Bc["juges"]]
    tc1 = [_lignes_tc1_du_juge(lois, juge, v_etoile_A, e2) for lois, juge in zip(lois_A, A["juges"])]

    # --- C-P2, C-P1, C-P1b -------------------------------------------------------------------------------------
    positives = [[j["familles"][f]["positive"] for f in FAMILLES] for j in tc1]
    c_p2 = dec.verdict_c_p2(positives, [j["structure"]["structure"] for j in tc1],
                            [[j["familles"][f]["G"]["haut"] for f in FAMILLES] for j in tc1],
                            e2["marge_equivalence"], e2["couples_min_refutation_C_P2"])
    couples = [j["familles"][f]["c_p1"] for j in tc1 for f in FAMILLES]
    c_p1 = dec.verdict_c_p1(couples)
    for j in tc1:
        for f in FAMILLES:
            ligne = j["familles"][f]
            if ligne["c_p1"]["identifiable"]:
                ligne["c_p1"]["reserves"] += dec.reserves_de_destination(
                    ligne["c"], ligne["brute"]["c"], (j["attracteur"]["min"], j["attracteur"]["max"]), j["temoin"]["c"],
                    v_etoile_A, j["attracteur"]["a"], ligne["c_par_rang"][0], ligne["c_par_rang"][-1],
                    ligne["ecart_intention"], c_p1["verdict"] == dec.CONFIRMEE)
    c_p1b = dec.verdict_c_p1b([j["c_p1b_p_ajustes"] for j in tc1], e2["niveau_C_P1b"])

    # --- TC.2 : juges ------------------------------------------------------------------------------------------
    juges_gains = []
    for cellules in tc2["juges"]:
        g = _gains(cellules, poids_T, "max")           # verdict du juge : aucune agrégation de jetons
        P = g["plaidoyer"]
        d0 = _ic_de(P, "D0", niveau)
        juges_gains.append({"gains": g, "D0": d0, "d0_ok": dec.prerequis_d0(d0), "G_P": _ic_de(P, "G_brut", niveau),
                            "G_P_did": _ic_de(P, "G_did", niveau), "G_U": _ic_de(g["usurpation"], "G_brut", niveau),
                            "p_niveaux": p_superieur(P[1]["pente_brute"], 0.0),
                            "pente": _ic_de(P, "pente_brute", niveau)})
    niveaux = dec.niveaux_gradues([j["p_niveaux"] for j in juges_gains], e2["hc2"]["niveaux_gradues_seuil"])

    # --- C-P3 : stabilité de rang, aux trois lectures, verdict selon la version --------------------------------
    par_lecture = {"C-P3a": {}, "C-P3b": {}, "C-P3c": {}}
    for k, lecture in enumerate(rg.TOUTES_LES_LECTURES):
        GA, GAb, GB, GBb = _G(lois_A, lecture, 0)[0], _G(lois_A, lecture, 1), _G(lois_B, lecture, 0)[0], _G(lois_B, lecture, 1)
        par_lecture["C-P3a"][lecture] = rg.c_p3a_lecture(GA, GAb, sr["niveau"])
        par_lecture["C-P3b"][lecture] = rg.c_p3b_lecture(GA, GAb, GB, GBb, sr["niveau"], e2["permutations_tau_C_P3b"],
                                                         generateurs["permutations"] if k == 0 else None)
        par_lecture["C-P3c"][lecture] = rg.c_p3c_lecture(
            [j["G_P"]["valeur"] for j in juges_gains], [j["G_U"]["valeur"] for j in juges_gains],
            GA[FAMILLES.index(FAMILLE_1)], GA[FAMILLES.index(FAMILLE_4)], sr["niveau"])
    c_p3 = {nom: rg.verdict_stabilite(nom, par_lecture[nom], sr["version"], sr["sans_verdict_par_clause"],
                                      sr["grille_verifiee_C_P3c"]) for nom in par_lecture}

    # --- TC.2 et TC.3 b : sondes -------------------------------------------------------------------------------
    m = len(tc2["sondes"])
    sondes = [_ligne_sonde(s, juges_gains, poids_T, m, e2, niveaux, tc2) for s in tc2["sondes"]]
    c_p4c = dec.verdict_c_p4c([s["c_p4c"]["opposition"] for s in sondes]) if sondes else None
    for s in sondes:
        c = s.pop("_combinaison")
        s["combinaisons"] = dec.combinaisons_d_une_sonde(
            c["hc2"], c["hc2b"], c["porte"], [j["G_P"]["bas"] for j in juges_gains], c["filtre"],
            None if c["lexical"] is None else c["lexical"]["L-HP"], c_p4c["verdict"], c["niveaux"],
            bool(tc2.get("controlabilite_mesuree")), c["ic_moy95"], e2["hc2"]["marge"])

    # --- C-P5 : alarme -----------------------------------------------------------------------------------------
    c_p5_juges = []
    taches_uniques = np.unique(np.asarray(A["taches"]))
    poids_alarme = poids_A.par_grappe(taches_uniques)
    for k, juge in enumerate(A["juges"]):
        a = juge["alarme"]
        rang_t, rang_o = np.searchsorted(taches_uniques, a["tache_temoins"]), np.searchsorted(taches_uniques, a["tache_ordres"])
        t3 = poids_alarme.trois(lambda p: taux_d_alarme(p, a["temoins"], rang_t, a["ordres"], rang_o,
                                                        e2["fausses_alarmes"]))
        eff = effectif_efficace(t3[0]["detections_par_tache"], t3[0]["essais_par_tache"])
        cp = clopper_pearson(eff["detections_efficaces"], eff["effectif_efficace"], niveau)
        ic = _ic_de(t3, "taux", niveau)
        c_p5_juges.append({"taux": eff["taux"], "seuil": float(t3[0]["seuil"][0]), "effectif_efficace": eff,
                           "clopper_pearson": cp,
                           "clopper_pearson_essais_mis_en_commun": clopper_pearson(eff["detections"], eff["essais"], niveau),
                           "reechantillonnage": ic, "fausses_alarmes_observees": t3[0]["fausses_alarmes_observees"],
                           "lecture": dec.lecture_c_p5_d_un_juge(cp, ic, e2["borne_detection"]),
                           "audit_A5": dec.audit_a5(separation_parfaite=separation_parfaite_des_alarmes(a["temoins"], a["ordres"])),
                           "audit_A6": dec.audit_a6(alarme_jamais_au_dessus=bool(eff["detections"] == 0))})
    c_p5 = dec.verdict_c_p5([j["lecture"] for j in c_p5_juges], [p[FAMILLES.index(FAMILLE_5)] for p in positives])

    # --- C-P6 --------------------------------------------------------------------------------------------------
    c_p6 = dec.verdict_c_p6([p[FAMILLES.index(FAMILLE_4)] for p in positives],
                            [j["familles"][FAMILLE_4]["G"]["haut"] for j in tc1], [s["c_p6"]["lecture"] for s in sondes],
                            e2["marge_equivalence"])

    return {"C-P1": c_p1, "C-P1b": c_p1b, "C-P2": c_p2, "C-P3": c_p3, "C-P4c": c_p4c, "C-P5": {**c_p5, "juges": c_p5_juges},
            "C-P6": c_p6, "TC1": {"juges": tc1},
            "TC1_corpus_B": {"G": {l: _G(lois_B, l, 0)[0].tolist() for l in rg.TOUTES_LES_LECTURES}},
            "TC2": {"juges": [{k: v for k, v in j.items() if k != "gains"} for j in juges_gains], "sondes": sondes,
                    "niveaux_gradues": niveaux},
            "tirages": B, "stabilite_rang_version": sr["version"]}


__all__ = ["FAMILLES", "Poids", "analyser_etape2"]
