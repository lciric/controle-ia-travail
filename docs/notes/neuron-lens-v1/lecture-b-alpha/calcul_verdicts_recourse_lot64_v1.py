"""Calcul independant des verdicts de la recourse de la tranche B-alpha (lots 16 et 64, carte A100 SXM4 40 Go) — lecteur neuf, v1.

Applique les seuils geles de texte-gele-volet-a-et-b-alpha-v6.md (34b88243...), sections Seuil (B), Criteres de lecture geles
et Audit symetrique (R4), et l'addendum v3 de la recourse (5f05f5bc...), selon plan-de-lecture-recourse-lot64-v1.md (acd96c84...).
N'importe aucun module de la course ; ne lit pas b-alpha-verdicts.json ni b-alpha-verdicts-lot64.json.
Bibliotheque standard et numpy seulement ; aucun modele, aucun reseau.

Usage : python -I calcul_verdicts_recourse_lot64_v1.py DOSSIER_DIAG SORTIE.json
Entrees lues dans DOSSIER_DIAG :
  - causal_lens_llama-3.1-8b-instruct.json (resume ecrit par score, serie lot 16)
  - causal_lens_lot64_llama-3.1-8b-instruct.json (resume ecrit par score, serie lot 64)
  - b-alpha-grandeurs.json (n et poles ecartes, serie lot 16)
  - b-alpha-grandeurs-lot64.json (n et poles ecartes, serie lot 64)
  - grandeurs-par-pole-b-alpha-v1.json (r par pole, serie lot 16)
  - grandeurs-par-pole-b-alpha-lot64-v1.json (r par pole, serie lot 64)
  - b-alpha-b0.json
  - b-alpha-fumee.json
  - b-alpha-measure.json (lot et empreinte causal)
  - b-alpha-measure-lot64.json (lot et empreinte causal)
  - b-alpha-bascule-lot64.json (empreinte du fichier deplace)
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

CIBLES = ("steer 1x", "steer 4x", "ablate pos", "ablate win")
LENTILLES = ("logit", "J", "npJpp", "npR")
N_COUCHES = 32
N_POLES = 64  # 2 * 32 neurones tires par couche
N_LISIBLE = 48
TIRAGES = 2000
ENTROPIE = 20261117  # graine propre au lecteur (R9)


def empreinte(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mediane_basse(x):
    """Mediane au sens de torch.median (celle de score) : pour un effectif pair, la plus basse des deux valeurs centrales."""
    x = np.sort(np.asarray(x, float))
    return float(x[(len(x) - 1) // 2])


def bande(a, b):
    return list(range(a, b + 1))


def plus_de_la_moitie(k, m):
    return m > 0 and k > m / 2


# --- Regles du texte gele appliquees ---

def couches_lisibles(n_cible, couches_range):
    return [l for l in couches_range if n_cible[l] >= N_LISIBLE]


def bande_partielle(couches_range, n_cible):
    lis = couches_lisibles(n_cible, couches_range)
    non_lis = len(couches_range) - len(lis)
    return non_lis > len(couches_range) / 4


def chaine_en_defaut(T, n, essais, fumee_code, lentilles_b0):
    """Conditions (a) a (e) du texte gele, section Seuil B."""
    defauts = []

    # (a) |control_med| > 0.10 a une couche de 0 a 27, 4 cibles x 4 lentilles
    for c in CIBLES:
        for le in LENTILLES:
            for l in range(28):
                if abs(T[c][le]["control_med"][l]) > 0.10:
                    defauts.append(f"(a) temoin hors de +/-0,10 : {c}, {le}, couche {l}, control_med={T[c][le]['control_med'][l]}")

    # (b) effet nul steer 1x : > 32 poles ecartes a une couche de 0 a 27
    # Lue dans grandeurs.ecartes (passee en argument via n_ecartes)
    # On le verifie dans la partie appelante, pas ici (on lit directement les ecartes)

    # (c) r_med logits < 0.80 aux couches 28-30, ou npR < 0.85
    for l in (28, 29, 30):
        if T["steer 1x"]["logit"]["r_med"][l] < 0.80:
            defauts.append(f"(c) cas sain des logits manque a la couche {l} : r_med={T['steer 1x']['logit']['r_med'][l]}")
        if T["steer 1x"]["npR"]["r_med"][l] < 0.85:
            defauts.append(f"(c) cas sain de npR manque a la couche {l} : r_med={T['steer 1x']['npR']['r_med'][l]}")

    # (d) essai en echec ou fumee en echec
    for k, x in essais.items():
        if x["code"] != 0 or any(mot in x.get("resume", "") for mot in ("skipped", "failed", "error")):
            defauts.append(f"(d) essai en echec : {k}, code {x['code']}, {x.get('resume', '')}")
    if fumee_code != 0:
        defauts.append(f"(d) fumee en echec, code {fumee_code}")

    # (e) repli sur les logits : |r_med(lentille) - r_med(logits)| < 0.001 a une couche de 0 a 23
    lg = np.asarray(T["steer 1x"]["logit"]["r_med"], float)
    for le in ("J", "npJpp", "npR"):
        ec = np.abs(np.round(np.asarray(T["steer 1x"][le]["r_med"], float)[:24] - lg[:24], 4))
        couches_e = [int(l) for l in range(24) if ec[l] < 1e-3]
        if couches_e:
            defauts.append(f"(e) repli sur les logits : {le}, couches {couches_e}")

    # (e) matrice identite (lue de b0.lentilles)
    for s, x in lentilles_b0.items():
        if x.get("defauts"):
            defauts.append(f"(e) matrice identite : {s}, defauts={x['defauts']}")

    return defauts


def verdict_b2(T, n):
    """B-2 : npR, steer 1x. Texte gele, tableau B."""
    s = T["steer 1x"]["npR"]
    ns = n["steer 1x"]
    r = s["r_med"]
    p = s["pass"]
    c = s["control_med"]

    # Reproduit : r_med >= 0.40 (8-15), >= 0.60 (16-23), >= 0.85 (24-27) ; pass >= 0.90 (8-27) ;
    # temoin : |control_med| > 0.05 a au plus 1 couche de 0 a 27, > 0.10 a aucune
    manques = {}
    for a, b, seuil in [(8, 15, 0.40), (16, 23, 0.60), (24, 27, 0.85)]:
        lis = couches_lisibles(ns, bande(a, b))
        m = [l for l in lis if r[l] < seuil]
        if m:
            manques[f"r_med {a}-{b} >= {seuil}"] = m

    lis_pass = couches_lisibles(ns, bande(8, 27))
    m_pass = [l for l in lis_pass if p[l] < 0.90]
    if m_pass:
        manques["pass 8-27 >= 0.90"] = m_pass

    # Temoin (texte : couches 0 a 27)
    hors_005_toutes = [l for l in range(28) if abs(c[l]) > 0.05]
    hors_010_toutes = [l for l in range(28) if abs(c[l]) > 0.10]
    hors_005_lis = [l for l in couches_lisibles(ns, bande(0, 27)) if abs(c[l]) > 0.05]
    hors_010_lis = [l for l in couches_lisibles(ns, bande(0, 27)) if abs(c[l]) > 0.10]

    temoin_ok_toutes = len(hors_005_toutes) <= 1 and len(hors_010_toutes) == 0
    temoin_ok_lis = len(hors_005_lis) <= 1 and len(hors_010_lis) == 0

    reproduit_toutes = (not manques) and temoin_ok_toutes
    reproduit_lis = (not manques) and temoin_ok_lis

    # Non reproduit : pass < 0.50 a plus de la moitie des lisibles 16-27, ou r_med < 0.30 a plus de la moitie des lisibles 16-23
    lis_1627 = couches_lisibles(ns, bande(16, 27))
    lis_1623 = couches_lisibles(ns, bande(16, 23))
    k_pass = [l for l in lis_1627 if p[l] < 0.50]
    k_r = [l for l in lis_1623 if r[l] < 0.30]
    non_reproduit = plus_de_la_moitie(len(k_pass), len(lis_1627)) or plus_de_la_moitie(len(k_r), len(lis_1623))

    # Verdict
    if non_reproduit:
        v = "non reproduit"
    elif reproduit_toutes:
        v = "reproduit"
    else:
        v = "autre"

    return {
        "verdict": v,
        "verdict_lecture_temoin_lisibles": "reproduit" if reproduit_lis and not non_reproduit else ("non reproduit" if non_reproduit else "autre"),
        "manques": manques,
        "temoin": {
            "hors_005_toutes": hors_005_toutes, "hors_010_toutes": hors_010_toutes,
            "hors_005_lis": hors_005_lis, "hors_010_lis": hors_010_lis,
        },
        "non_reproduit_detail": {"pass<0.50 (16-27)": k_pass, "r_med<0.30 (16-23)": k_r},
    }


def verdict_b3(T, n):
    """B-3 : r_med(npR) - r_med(logits), steer 1x, couches 4-15."""
    r_npR = np.asarray(T["steer 1x"]["npR"]["r_med"], float)
    r_logit = np.asarray(T["steer 1x"]["logit"]["r_med"], float)
    ecart = np.round(r_npR - r_logit, 4)

    ns = n["steer 1x"]
    lis = couches_lisibles(ns, bande(4, 15))
    manques = [l for l in lis if ecart[l] < 0.20]
    neg = [l for l in lis if ecart[l] <= 0]

    reproduit = bool(lis) and not manques
    non_reproduit = plus_de_la_moitie(len(neg), len(lis))

    if non_reproduit:
        v = "non reproduit"
    elif reproduit:
        v = "reproduit"
    else:
        v = "autre"

    ecart_par_couche = {str(l): float(ecart[l]) for l in bande(4, 15)}
    ecart_min = float(np.min([ecart[l] for l in lis])) if lis else None

    return {
        "verdict": v,
        "ecart_par_couche": ecart_par_couche,
        "ecart_min_4_15": ecart_min,
        "manques": manques,
    }


def verdict_b7(T, n):
    """B-7 : ablate win, npR. Texte gele, tableau B."""
    r = T["ablate win"]["npR"]["r_med"]
    na = n["ablate win"]

    # Reproduit : < 0.25 a chaque couche lisible de 0 a 15 ET >= 0.50 a chaque couche lisible de 26 a 29
    lis_bas = couches_lisibles(na, bande(0, 15))
    lis_haut = couches_lisibles(na, bande(26, 29))
    manques_bas = [l for l in lis_bas if r[l] >= 0.25]
    manques_haut = [l for l in lis_haut if r[l] < 0.50]
    part_bas = bande_partielle(bande(0, 15), na)
    part_haut = bande_partielle(bande(26, 29), na)

    reproduit = bool(lis_bas) and bool(lis_haut) and not manques_bas and not manques_haut

    # Non reproduit par le haut : >= 0.40 a plus de la moitie des couches lisibles de 8 a 15
    lis_815 = couches_lisibles(na, bande(8, 15))
    haut = [l for l in lis_815 if r[l] >= 0.40]
    par_le_haut = plus_de_la_moitie(len(haut), len(lis_815)) and not part_bas

    # Non reproduit par le bas : < 0.30 a plus de la moitie des couches lisibles de 26 a 29
    bas = [l for l in lis_haut if r[l] < 0.30]
    par_le_bas = plus_de_la_moitie(len(bas), len(lis_haut)) and not part_haut

    non_reproduit = par_le_haut or par_le_bas

    if non_reproduit:
        v = "non reproduit"
    elif reproduit:
        v = "reproduit"
    else:
        v = "autre"

    return {
        "verdict": v,
        "par_le_haut": par_le_haut,
        "par_le_bas": par_le_bas,
        "manques_bas_0_15": manques_bas,
        "manques_haut_26_29": manques_haut,
        "r_med_0_15": [r[l] for l in range(16)],
        "r_med_26_29": [r[l] for l in range(26, 30)],
    }


def ecarts_b4(T):
    """B-4 : npR - J et npR - npJpp, couches 4-23, rapportee."""
    r_npR = np.asarray(T["steer 1x"]["npR"]["r_med"], float)
    r_J = np.asarray(T["steer 1x"]["J"]["r_med"], float)
    r_npJpp = np.asarray(T["steer 1x"]["npJpp"]["r_med"], float)
    return {
        "npR - J": {str(l): float(np.round(r_npR[l] - r_J[l], 4)) for l in bande(4, 23)},
        "npR - npJpp": {str(l): float(np.round(r_npR[l] - r_npJpp[l], 4)) for l in bande(4, 23)},
    }


def audit_trop_beau(T):
    """Audit R4 : trop beau. npR, steer 1x, valeurs ecrites arrondies a 4 decimales."""
    s = T["steer 1x"]["npR"]
    declencheurs = []
    for l in range(8):
        if round(s["r_med"][l], 4) >= 0.95:
            declencheurs.append(f"r_med >= 0.95 a la couche {l} : {s['r_med'][l]}")
    zeros = [l for l in range(28) if abs(round(s["control_med"][l], 4)) == 0]
    if len(zeros) >= 2:
        declencheurs.append(f"control_med ecrit egal a 0 a {len(zeros)} couches : {zeros}")
    return declencheurs


def audit_tout_negatif(vb2, vb3):
    """Audit R4 : tout negatif. B-2 et B-3 non reproduit."""
    return vb2 == "non reproduit" and vb3 == "non reproduit"


def reproduction(defauts, vb2, vb3, trop_beau_motifs, tout_neg):
    """Verdict de reproduction de la serie."""
    if defauts:
        return "chaine en defaut"
    if trop_beau_motifs or tout_neg:
        return "verdict suspendu a l'audit R4"
    if vb2 == "reproduit" and vb3 == "reproduit":
        return "reproduit avec la lentille R publique"
    if "non reproduit" in (vb2, vb3):
        return "non reproduit avec la lentille R publique"
    return "partiel"


def calculer_intervalles(poles, graine):
    """Intervalles a 95 % par reechantillonnage des poles (rapportes, ne decident de rien)."""
    ss = np.random.SeedSequence(entropy=graine)
    enfants = ss.spawn(3)

    par = {}
    for p in poles:
        if not p["aleatoire"]:
            continue
        for c in CIBLES:
            for s in LENTILLES:
                x = p["lectures"][c][s]
                if x["motif"] == "retenu":
                    par.setdefault((c, s, p["couche"]), []).append((x["r"], x["r_temoin"]))
    par = {k: np.asarray(val, float) for k, val in par.items()}

    def boot(cible, fonction, graine_boot):
        g = np.random.default_rng(graine_boot)
        res = {}
        for l in range(32):
            a = {s: par[(cible, s, l)][:, 0] for s in LENTILLES if (cible, s, l) in par}
            if "npR" not in a:
                continue
            m = len(a["npR"])
            idx = g.integers(0, m, size=(TIRAGES, m))
            tir = np.array([fonction({s: x[i] for s, x in a.items()}) for i in idx])
            res[l] = [round(float(np.quantile(tir, 0.025)), 4), round(float(np.quantile(tir, 0.975)), 4)]
        return res

    return {
        "steer 1x, npR, r_med": boot("steer 1x", lambda a: mediane_basse(a["npR"]), enfants[0]),
        "steer 1x, ecart npR - logit": boot("steer 1x", lambda a: mediane_basse(a["npR"]) - mediane_basse(a["logit"]), enfants[1]),
        "ablate win, npR, r_med": boot("ablate win", lambda a: mediane_basse(a["npR"]), enfants[2]),
    }


def main(dossier, sortie):
    d = Path(dossier)
    noms = {
        "score16": "causal_lens_llama-3.1-8b-instruct.json",
        "score64": "causal_lens_lot64_llama-3.1-8b-instruct.json",
        "grandeurs16": "b-alpha-grandeurs.json",
        "grandeurs64": "b-alpha-grandeurs-lot64.json",
        "poles16": "grandeurs-par-pole-b-alpha-v1.json",
        "poles64": "grandeurs-par-pole-b-alpha-lot64-v1.json",
        "b0": "b-alpha-b0.json",
        "fumee": "b-alpha-fumee.json",
        "measure16": "b-alpha-measure.json",
        "measure64": "b-alpha-measure-lot64.json",
        "bascule": "b-alpha-bascule-lot64.json",
    }
    emp = {k: empreinte(d / v) for k, v in noms.items()}

    # --- charger les donnees ---
    sc16 = json.loads((d / noms["score16"]).read_text())
    sc64 = json.loads((d / noms["score64"]).read_text())
    gr16 = json.loads((d / noms["grandeurs16"]).read_text())["resultat"]
    gr64 = json.loads((d / noms["grandeurs64"]).read_text())["resultat"]
    pp16 = json.loads((d / noms["poles16"]).read_text())
    pp64 = json.loads((d / noms["poles64"]).read_text())
    b0 = json.loads((d / noms["b0"]).read_text())["resultat"]
    fu = json.loads((d / noms["fumee"]).read_text())["resultat"]
    m16 = json.loads((d / noms["measure16"]).read_text())["resultat"]
    m64 = json.loads((d / noms["measure64"]).read_text())["resultat"]
    basc = json.loads((d / noms["bascule"]).read_text())["resultat"]

    T16 = sc16["targets"]
    T64 = sc64["targets"]

    # --- controle de serie (plan, section 7) ---
    controle = {}
    controle["lot_measure16"] = m16.get("lot")
    controle["lot_measure64"] = m64.get("lot")
    controle["causal_sha256_measure16"] = m16.get("causal", {}).get("sha256")
    controle["causal_sha256_measure64"] = m64.get("causal", {}).get("sha256")
    controle["causal_sha256_egales"] = controle["causal_sha256_measure16"] == controle["causal_sha256_measure64"]
    basc_sha = list(basc.get("deplaces", {}).values())[0].get("sha256") if basc.get("deplaces") else None
    controle["bascule_sha256_egale_a_measure16"] = basc_sha == controle["causal_sha256_measure16"]
    controle["meta16"] = sc16.get("meta")
    controle["meta64"] = sc64.get("meta")
    controle["meta_egaux"] = sc16.get("meta") == sc64.get("meta")

    # --- verifier la forme des deux tables ---
    for label, T in [("lot16", T16), ("lot64", T64)]:
        for c in CIBLES:
            for le in LENTILLES:
                assert T[c][le]["layer"] == list(range(N_COUCHES)), f"{label}: couches inattendues {c}/{le}"
        assert sc16["lenses"] == list(LENTILLES), f"{label}: lentilles inattendues"

    # --- verdicts serie par serie ---
    resultats = {}
    for label, T, gr, pp_data in [("lot16", T16, gr16, pp16), ("lot64", T64, gr64, pp64)]:
        n = {c: gr["n"][c] for c in CIBLES}

        # Effet nul (condition b)
        defauts_b = []
        nul = gr["ecartes"]["steer 1x"]["effet nul"]
        for l in range(28):
            if nul[l] > 32:
                defauts_b.append(f"(b) effet nul steer 1x couche {l} : {nul[l]}")

        defauts = chaine_en_defaut(T, n, b0["essais"], fu["code"], b0["lentilles"])
        defauts.extend(defauts_b)

        # Arrets b0
        arrets_b0 = [f"{s} : {x['arrets']}" for s, x in b0["lentilles"].items() if x["arrets"]]
        arrets_b0 += [f"{s} : sortie sans layers 0-30" for s, x in b0["lentilles"].items() if "layers 0-30," not in x["sortie"]]

        b2 = verdict_b2(T, n)
        b3 = verdict_b3(T, n)
        b7 = verdict_b7(T, n)
        b4 = ecarts_b4(T)

        trop_beau = audit_trop_beau(T)
        tout_neg = audit_tout_negatif(b2["verdict"], b3["verdict"])

        repro = reproduction(defauts + arrets_b0, b2["verdict"], b3["verdict"], trop_beau, tout_neg)

        # Intervalles
        ic = calculer_intervalles(pp_data["poles"], ENTROPIE)

        resultats[label] = {
            "n": n,
            "chaine_en_defaut": defauts,
            "arrets_b0": arrets_b0,
            "B-2": b2,
            "B-3": b3,
            "B-4": b4,
            "B-7": b7,
            "audit_trop_beau": trop_beau,
            "audit_tout_negatif": tout_neg,
            "reproduction": repro,
            "intervalles_95": {"tirages": TIRAGES, "graine": f"SeedSequence(entropy={ENTROPIE})", "valeurs": ic},
            "fidelite_a_score": pp_data.get("fidelite_a_score"),
        }

    # --- comparaison (c) : cas sain de determinisme ---
    # Pilotage (steer 1x, steer 4x) doit coincider entre lot 16 et lot 64
    det = {}
    for cible in ("steer 1x", "steer 4x"):
        for le in LENTILLES:
            for k in ("r_med", "pass", "control_med"):
                delta = [round(T64[cible][le][k][l] - T16[cible][le][k][l], 6) for l in range(32)]
                max_abs = max(abs(d) for d in delta)
                det[f"{cible}/{le}/{k}"] = {"max_abs_delta": max_abs, "delta": delta}

    max_det_r_med = max(det[k]["max_abs_delta"] for k in det if "/r_med" in k)
    det["max_abs_delta_r_med_pilotage"] = max_det_r_med
    det["reserve_si_superieur_a_0.01"] = max_det_r_med > 0.01

    # --- comparaison (a) : effet du lot (ablation) ---
    effet_lot = {}
    for cible in ("ablate win", "ablate pos"):
        for le in LENTILLES:
            delta = [round(T64[cible][le]["r_med"][l] - T16[cible][le]["r_med"][l], 6) for l in range(32)]
            max_abs = max(abs(d) for d in delta)
            effet_lot[f"{cible}/{le}/r_med"] = {"max_abs_delta": max_abs, "delta": delta}

    max_effet_lot = max(v["max_abs_delta"] for v in effet_lot.values())
    effet_lot["max_abs_delta"] = max_effet_lot
    effet_lot["dans_le_bruit"] = max_effet_lot <= max_det_r_med if max_det_r_med > 0 else "cas sain exactement nul"

    # --- donnees identiques ? ---
    toutes_identiques = all(
        T16[c][le][k] == T64[c][le][k]
        for c in CIBLES for le in LENTILLES for k in ("r_med", "pass", "control_med")
    )

    # --- conclusion B-7 de la recourse (addendum v3, section 3) ---
    b7_lot64 = resultats["lot64"]["B-7"]
    b7_lot16 = resultats["lot16"]["B-7"]
    serie_lot64_en_defaut = bool(resultats["lot64"]["chaine_en_defaut"])

    if serie_lot64_en_defaut:
        verdict_b7_recourse = "pas de verdict de B-7 (chaine en defaut de la serie lot 64)"
    else:
        verdict_b7_recourse = b7_lot64["verdict"]

    # B-7 depend du lot ?
    b7_depend_lot = b7_lot64["verdict"] != b7_lot16["verdict"]
    # (si toutes les donnees sont identiques, B-7 ne depend pas du lot)

    out = {
        "programme": "calcul_verdicts_recourse_lot64_v1.py",
        "texte_gele_sha256": "34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131",
        "addendum_v3_sha256": "5f05f5bc5cae8e1ef41ace349ba54046baf8bfdb7657140ad7addbf0c0ad908a",
        "entrees_sha256": {noms[k]: emp[k] for k in noms},
        "controle_de_serie": controle,
        "toutes_valeurs_identiques_lot16_lot64": toutes_identiques,
        "lot16": resultats["lot16"],
        "lot64": resultats["lot64"],
        "comparaison_c_determinisme": det,
        "comparaison_a_effet_lot": effet_lot,
        "verdict_b7_recourse": verdict_b7_recourse,
        "b7_depend_du_lot": b7_depend_lot,
    }

    Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")

    # Resume
    print("=== RESUME ===")
    print(f"Toutes les valeurs identiques entre lot 16 et lot 64 : {toutes_identiques}")
    print(f"causal.sha256 egales : {controle['causal_sha256_egales']}")
    print()
    for label in ("lot16", "lot64"):
        r = resultats[label]
        print(f"--- {label} ---")
        print(f"  Chaine en defaut : {r['chaine_en_defaut'] if r['chaine_en_defaut'] else 'aucune'}")
        print(f"  B-2 : {r['B-2']['verdict']}")
        print(f"  B-3 : {r['B-3']['verdict']} (ecart min 4-15 : {r['B-3']['ecart_min_4_15']})")
        print(f"  B-7 : {r['B-7']['verdict']} (par_le_haut={r['B-7']['par_le_haut']}, par_le_bas={r['B-7']['par_le_bas']})")
        print(f"  Audit trop beau : {r['audit_trop_beau'] if r['audit_trop_beau'] else 'non declenche'}")
        print(f"  Reproduction : {r['reproduction']}")
        print()
    print(f"Verdict de B-7 de la recourse : {verdict_b7_recourse}")
    print(f"B-7 depend du lot : {b7_depend_lot}")
    print(f"Comparaison (c) max |delta r_med| pilotage : {max_det_r_med}")
    print(f"Comparaison (a) max |delta r_med| ablation : {max_effet_lot}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    if Path(sys.argv[2]).exists():
        raise SystemExit("la sortie existe deja : on n'ecrase jamais (R12)")
    main(sys.argv[1], sys.argv[2])
