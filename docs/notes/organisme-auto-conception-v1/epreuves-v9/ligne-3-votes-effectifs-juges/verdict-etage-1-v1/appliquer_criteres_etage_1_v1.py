"""Application par l'agent du verdict des critères gelés de l'étage 1 de la
ligne 3 aux mesures de `resultat-etage-1-ligne-3-v3.json`.

N'ouvre jamais le bloc `criteres_mecaniques` (l'aide) : il est retiré au
chargement. Ne relit pas les mots ou drapeaux « tient » calculés par le code
pour décider ; il les relit seulement à la fin, pour dire s'il y a accord.
Aucun tirage. Bibliothèque standard seule.

Usage : python3 -I -B appliquer_criteres_etage_1_v1.py RESULTAT.json SORTIE.json
Critères : voir criteres-appliques-v1.md (même dossier).
"""
import json
import math
import sys
from collections import Counter, defaultdict

EPS = 1e-12
NS = [50, 100, 200, 400]


# ---------------------------------------------------------------- tolérance
def tolerance(est):
    """PR l. 177 : les quatre ensemble. Rend (tient, manques)."""
    manques = {}
    b, q, c, u = est["biais"], est["eqm"], est["couverture"], est["part_indefini"]
    if b is None or not (abs(b) <= 0.05):
        manques["biais"] = None if b is None else abs(b) - 0.05
    if q is None or not (q <= 0.10):
        manques["eqm"] = None if q is None else q - 0.10
    if c is None or not (0.90 <= c <= 0.98):
        manques["couverture"] = None if c is None else (0.90 - c if c < 0.90 else c - 0.98)
    if u is None or not (u <= 0.02):
        manques["part_indefini"] = None if u is None else u - 0.02
    return (len(manques) == 0, manques)


def bruit(est, repliques):
    """Ordres de grandeur du bruit de 2 000 répliques (approximations dites)."""
    u = est["part_indefini"] or 0.0
    nd = max(1.0, repliques * (1.0 - u))
    out = {"repliques_definies": nd}
    if est["couverture"] is not None:
        c = est["couverture"]
        out["et_couverture"] = math.sqrt(max(c * (1 - c), 0.0) / nd)
    out["et_part_indefini"] = math.sqrt(max(u * (1 - u), 1e-12) / repliques)
    if est["eqm"] is not None and est["biais"] is not None:
        var = max(est["eqm"] ** 2 - est["biais"] ** 2, 0.0)
        out["et_biais"] = math.sqrt(var / nd)
        out["et_eqm_approx_normale"] = est["eqm"] / math.sqrt(2 * nd)
    return out


def cle_cellule(e):
    return f"J{e['J']}|loi{e['loi']}|{e['profil']}|rho{e['rho_grille']}"


def bloc_estimateur(ea):
    par_cellule = defaultdict(dict)
    accord_code = Counter()
    for e in ea:
        t, m = tolerance(e["estimateur"])
        par_cellule[cle_cellule(e)][e["n"]] = {
            "tient": t, "manques": m,
            "biais": e["estimateur"]["biais"], "eqm": e["estimateur"]["eqm"],
            "couverture": e["estimateur"]["couverture"],
            "part_indefini": e["estimateur"]["part_indefini"],
            "bruit": bruit(e["estimateur"], e["repliques"]),
        }
        accord_code["accord" if t == e["estimateur"].get("tient") else "desaccord"] += 1

    # cellules de la règle (A1 l. 81)
    regle = [k for k in par_cellule
             if k.startswith("J2|loi1|egal_0.2|") or k.startswith("J2|loi3|egal_0.2|")]
    regle.sort()
    tient_regle = {n: all(par_cellule[k][n]["tient"] for k in regle) for n in NS}
    detail_regle = {k: {n: par_cellule[k][n] for n in NS} for k in regle}

    # verdict par la table (PR l. 311-316) et règle E (A1 l. 80-85)
    if tient_regle[100]:
        verdict = "oui"
        taille = 100
    elif tient_regle[200] or tient_regle[400]:
        verdict = "non, pas à cette taille"
        taille = 200 if tient_regle[200] else 400
    elif tient_regle[50]:
        verdict = "cas non prévu par la table gelée : la tolérance tient à n = 50 et à aucun n plus grand"
        taille = None
    else:
        verdict = "non"
        taille = None

    # monotonie (A1 l. 84), au niveau de la règle et par cellule
    def non_monotone(d):
        tenus = [n for n in NS if d[n]]
        return any(d[a] and not d[b] for a in NS for b in NS if b > a)

    nm_regle = non_monotone(tient_regle)
    nm_cellules = {}
    plus_petit_n = {}
    for k, parn in par_cellule.items():
        d = {n: parn[n]["tient"] for n in NS if n in parn}
        tenus = [n for n in NS if d.get(n)]
        plus_petit_n[k] = min(tenus) if tenus else None
        if len(d) == 4 and non_monotone(d):
            nm_cellules[k] = {n: {"tient": parn[n]["tient"], "manques": parn[n]["manques"],
                                  "bruit": parn[n]["bruit"]} for n in NS}
    nm_regle_cellules = {k: v for k, v in nm_cellules.items() if k in regle}
    return {
        "accord_du_drapeau_tient_du_code_par_cellule_et_n": dict(accord_code),
        "cellules_de_la_regle": regle,
        "nombre_cellules_de_la_regle": len(regle),
        "tient_aux_cellules_de_la_regle_par_n": tient_regle,
        "detail_cellules_de_la_regle": detail_regle,
        "verdict_estimateur": verdict,
        "taille_retenue": taille,
        "issue_non_monotone_au_niveau_de_la_regle": nm_regle,
        "cellules_non_monotones_nombre": len(nm_cellules),
        "cellules_non_monotones_de_la_regle": nm_regle_cellules,
        "cellules_non_monotones_toutes": nm_cellules,
        "plus_petit_n_qui_tient": plus_petit_n,
    }


# ---------------------------------------------------------------- puissance
CLES_PUISSANCE = {"unanimite": ["U"], "juge_seul": ["S_1", "S_2"],
                  "juge_repete_trois_votes_majorite": ["R_3"]}
COMPTE_TEXTE_010 = {  # PR l. 238 : cellules faisables à l'écart 0,10 (loi 1, loi 3)
    "unanimite": (4, 2), "juge_seul": (2, 1), "juge_repete_trois_votes_majorite": (2, 2)}


def bloc_puissance(mp):
    out = {}
    for ecart in (0.05, 0.10, 0.15):
        par_comp = {}
        for comp, cles in CLES_PUISSANCE.items():
            cel = [e for e in mp if e["comparaison"] == comp and abs(e["ecart_vise"] - ecart) < 1e-9
                   and e["loi"] in (1, 3)]
            fais = [e for e in cel if e["faisable"]]
            lignes = []
            for e in fais:
                for c in cles:
                    lignes.append({"loi": e["loi"], "rho": e["rho"], "rho_prime": e["rho_prime"],
                                   "bras": c, "puissance": e["puissance_par_comparaison"][c],
                                   "d": e["d"], "ecart_vrai_formule": e["ecart_vrai_formule"]})
            ecarts_formule = [abs(e["ecart_vrai_formule"] - ecart) for e in fais]
            par_comp[comp] = {
                "cellules": len(cel),
                "faisables_loi_1": sum(1 for e in fais if e["loi"] == 1),
                "faisables_loi_3": sum(1 for e in fais if e["loi"] == 3),
                "rho_prime_hors_bras_R": sorted({e["rho_prime"] for e in cel}) if comp != "juge_repete_trois_votes_majorite" else None,
                "ecart_formule_max_au_vise": max(ecarts_formule) if ecarts_formule else None,
                "puissances": lignes,
                "plus_basse": min((l["puissance"] for l in lignes), default=None),
            }
        aucune = [c for c, v in par_comp.items() if v["faisables_loi_1"] + v["faisables_loi_3"] == 0]
        toutes = [l["puissance"] for v in par_comp.values() for l in v["puissances"]]
        out[str(ecart)] = {"par_comparaison": par_comp,
                           "comparaisons_sans_cellule_faisable": aucune,
                           "plus_basse_toutes_comparaisons": min(toutes) if toutes else None}
    d = out["0.1"]
    pqd = d["plus_basse_toutes_comparaisons"]
    portee = (pqd is None) or (pqd < 0.5) or bool(d["comparaisons_sans_cellule_faisable"])
    compte = {c: (d["par_comparaison"][c]["faisables_loi_1"], d["par_comparaison"][c]["faisables_loi_3"])
              for c in CLES_PUISSANCE}
    return {"par_ecart": out, "puissance_qui_decide": pqd,
            "regle_de_portee_s_applique": portee,
            "comptes_faisables_0_10_observes": compte,
            "comptes_faisables_0_10_du_texte": COMPTE_TEXTE_010,
            "comptes_egaux_au_texte": all(tuple(compte[c]) == COMPTE_TEXTE_010[c] for c in compte)}


# ---------------------------------------------------------------- descriptifs
def mot_fa38(e, rp):
    bras = e["bras"]
    P = bras["P"]
    refs = [bras["poids_egaux"], bras[f"R_k{e['J']}_rp{rp}"]]
    if any(r["faux_acceptes"] < 0.02 for r in refs) or any(P["vrais_rejetes"] - r["vrais_rejetes"] > 0.05 for r in refs):
        return "sans prise"
    if all(P["faux_acceptes"] <= 0.85 * r["faux_acceptes"] + EPS for r in refs):
        return "tient sur le banc"
    return "réfuté sur le banc"


def bloc_fa38(ea):
    compte = Counter()
    accord = Counter()
    for e in ea:
        for rp in ("0.0", "0.5", "0.9"):
            m = mot_fa38(e, rp)
            compte[(e["J"], m)] += 1
            code = e["mot_fa38f9faa24e0_par_rho_prime"].get(rp)
            accord["accord" if code == m else "desaccord"] += 1
    return {"mots_par_J": {f"J{j}|{m}": v for (j, m), v in sorted(compte.items())},
            "accord_avec_le_mot_du_code": dict(accord)}


def bloc_branche_2(ea):
    cel = [e for e in ea if e["J"] == 5 and e["loi"] in (1, 4)]
    par_taille = defaultdict(lambda: Counter())
    refutes = []
    for e in cel:
        taille = e["n"] // 2
        diff = e["bras"]["C"]["erreur_equilibree"] - e["bras"]["poids_egaux"]["erreur_equilibree"]
        mot = "réfuté sur le banc" if diff > 0.02 else "tient sur le banc"
        par_taille[taille][mot] += 1
        if mot.startswith("réfuté"):
            refutes.append({"loi": e["loi"], "profil": e["profil"], "rho": e["rho_grille"],
                            "taille_etalonnage": taille, "ecart": diff})
    tailles = sorted(par_taille)
    tient_tout = {t: par_taille[t]["réfuté sur le banc"] == 0 for t in tailles}
    plus_petite = None
    for t in tailles:
        if all(tient_tout[u] for u in tailles if u >= t):
            plus_petite = t
            break
    return {"par_taille": {str(t): dict(par_taille[t]) for t in tailles},
            "tient_dans_toutes_les_cellules_par_taille": {str(t): v for t, v in tient_tout.items()},
            "plus_petite_taille_d_etalonnage": plus_petite if plus_petite is not None else "aucune",
            "cellules_refutees": refutes}


def bloc_branche_3(gc):
    loi = "suiveur_seduisant"
    out = {}
    for t in (20, 40):
        saine = [g for g in gc if g["t"] == t and g["delta"] == 0.0][0]
        forte = [g for g in gc if g["t"] == t and g["delta"] == 0.5 and g["s"] == 1.0][0]
        for c in ("0.1", "0.15", "0.2", "0.25", "0.3"):
            ps = saine["par_loi"][loi]["part_des_rondes_declenchees"][c]
            pf = forte["par_loi"][loi]["part_des_rondes_declenchees"][c]
            if ps > 0.10:
                mot = "réfuté sur le banc"
            elif pf >= 0.5:
                mot = "tient sur le banc"
            else:
                mot = "sans prise"
            out[f"t{t}|c{c}"] = {"saine": ps, "delta_0_5": pf, "mot": mot}
    return out


def intervalle_dans(iv, borne):
    return iv["bas"] >= -borne - EPS and iv["haut"] <= borne + EPS


def bloc_fcfa(dr):
    loi = "suiveur_seduisant"
    cellules = {}
    accord = Counter()
    faute_ii = []
    for e in dr:
        L = e["par_loi"][loi]
        mo = L["moyennes"]
        if e["delta"] == 0.0:
            for nom, Lx in e["par_loi"].items():
                a = Lx["moyennes"]["abstention_par_vote"]
                if a is None or abs(a - 0.1275) > 0.02:
                    faute_ii.append({"loi": nom, "n": e["n"], "s": e["s"], "abstention": a})
        if e["s"] == 0.0:
            ci = "non lue (s = 0)"
            ciii = "non lue"
            mot = "sans prise"
        else:
            iv = L["fa_trait_bras_1_moins_bras_2"]
            vr_diff = mo["vr_bras_1"] - mo["vr_bras_4"]
            if (iv["moyenne"] > 0 and iv["bas"] > 0) or vr_diff > 0.05:
                ci = "réfuté sur le banc"
            elif mo["fa_trait_bras_2"] < 0.02:
                ci = "sans prise"
            elif iv["haut"] < 0:
                ci = "tient sur le banc"
            else:
                ci = "réfuté sur le banc"
            if e["s"] == 0.5:
                i1, i4 = L["ecart_surface_bras_1"], L["ecart_surface_bras_4"]
                if e["delta"] == 0.0 or intervalle_dans(i4, 0.05):
                    ciii = "sans prise"
                elif abs(i1["moyenne"]) >= 0.05 and (i1["bas"] > 0 or i1["haut"] < 0):
                    ciii = "réfuté sur le banc"
                elif intervalle_dans(i1, 0.05):
                    ciii = "tient sur le banc"
                else:
                    ciii = "sans prise"
            else:
                ciii = "non lue"
            if ci.startswith("réfuté") or ciii.startswith("réfuté"):
                mot = "réfuté sur le banc"
            elif ci.startswith("tient"):
                mot = "tient sur le banc"
            else:
                mot = "sans prise"
        cellules[f"delta{e['delta']}|s{e['s']}|n{e['n']}"] = {"clause_i": ci, "clause_iii": ciii, "mot": mot}
        accord["accord" if L.get("mot_de_la_carte") == mot else "desaccord"] += 1
    return {"cellules": cellules, "accord_avec_le_mot_du_code": dict(accord),
            "clause_ii_faute_du_banc": faute_ii}


def bloc_alarme(al):
    out = {}
    refutee = False
    for e in al:
        m = e["m"]
        B = e["par_bras"]["B"]["comptes_silence_1"]
        D = e["par_bras"]["D"]["comptes_silence_1"]
        fa = B["suites_sans_changement_en_alarme"]
        clause_fa = fa > 80
        if m in (20, 40):
            clause_det = B["suites_a_effet_detectees"] <= D["suites_a_effet_detectees"]
        else:
            clause_det = None
        refutee |= clause_fa or bool(clause_det)
        out[str(m)] = {"fausse_alarme_B_sur_1000": fa, "clause_fausse_alarme_atteinte": clause_fa,
                       "detection_a_effet_B_sur_500": B["suites_a_effet_detectees"],
                       "detection_a_effet_D_sur_500": D["suites_a_effet_detectees"],
                       "clause_detection_atteinte": clause_det}
    return {"par_m": out, "P6": "P6 réfutée" if refutee else "P6 non réfutée",
            "carte_fcbf4a2dd1a57": "mesurée, sans mot : aucune règle de mot gelée"}


def bloc_regle_A(er):
    out = {}
    for ecart in (0.2, 0.3, 0.5):
        cel = [e for e in er if abs(e["ecart_vise"] - ecart) < 1e-9]
        fais = [e for e in cel if e["faisable"]]
        p = [e["puissance_les_deux"] for e in fais]
        out[str(ecart)] = {"faisables": len(fais), "cellules": len(cel),
                           "plus_basse_les_deux": min(p) if p else None,
                           "plus_haute_les_deux": max(p) if p else None}
    out["faisables_total"] = sum(v["faisables"] for v in out.values() if isinstance(v, dict))
    return out


def bloc_trop_propre(ea):
    propres = [cle_cellule(e) + f"|n{e['n']}" for e in ea if e["estimateur"]["couverture"] == 1.0]
    code = [cle_cellule(e) + f"|n{e['n']}" for e in ea if e["estimateur"].get("audit_trop_propre_aucune_replique_hors_intervalle")]
    return {"couverture_egale_1": propres, "drapeau_du_code": code, "egaux": sorted(propres) == sorted(code)}


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    data.pop("criteres_mecaniques", None)  # l'aide n'est pas lue ici
    sortie = {
        "programme": "appliquer_criteres_etage_1_v1.py",
        "estimateur": bloc_estimateur(data["estimateur_et_agregation"]),
        "puissance": bloc_puissance(data["monde_de_puissance"]),
        "regle_A_ecart_rho_prime_moins_rho": bloc_regle_A(data["ecart_rho_prime_moins_rho"]),
        "fa38f9faa24e0": bloc_fa38(data["estimateur_et_agregation"]),
        "fefca0bd94064_branche_2": bloc_branche_2(data["estimateur_et_agregation"]),
        "fefca0bd94064_branche_3": bloc_branche_3(data["garde_de_cadrage"]),
        "fcfa3d98b90f8": bloc_fcfa(data["double_rendu"]),
        "alarme": bloc_alarme(data["alarme"]),
        "audit_trop_propre_etage_1": bloc_trop_propre(data["estimateur_et_agregation"]),
    }
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write("\n")


if __name__ == "__main__":
    main()
