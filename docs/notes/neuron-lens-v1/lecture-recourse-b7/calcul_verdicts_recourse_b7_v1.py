"""Calcul des verdicts de la recourse de B-7 (B-α), par le lecteur neuf — v1.

Écrit par le lecteur neuf, sans importer ni lire le code des verdicts de la course
(`verdicts_b_alpha_v*.py`, `b_alpha_lancer_v*.py`). Applique le plan de lecture scellé
`plan-de-lecture-recourse-b7-v3.md` (§ 3 et § 4), lui-même recopié du texte gelé v6 et de
l'addendum v3. N'arbitre aucune ambiguïté : quand deux lectures divergent, les deux sont écrites.

Entrées : les fichiers versés de la course A100 (`diag/20261117-015632-neuron-lens-b-alpha/`) ;
en option (`--rtx4090 DIR`, étape 6 du plan seulement), la troisième course pour la comparaison (b).
Aucune dépendance hors de la bibliothèque standard et de numpy.

Usage (racine du dépôt) :
    .venv/bin/python docs/notes/neuron-lens-v1/lecture-recourse-b7/calcul_verdicts_recourse_b7_v1.py \
        --sortie FICHIER.json [--rtx4090 diag/20261115-120622-neuron-lens-b-alpha]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

import numpy as np

A100 = "diag/20261117-015632-neuron-lens-b-alpha"
MANIFESTE = "runs/20261117-015632-neuron-lens-b-alpha/manifeste.json"
CIBLES = ["steer 1x", "steer 4x", "ablate pos", "ablate win"]
LENTILLES = ["logit", "J", "npJpp", "npR"]
SERIES = {
    "lot16": {
        "resume": "causal_lens_llama-3.1-8b-instruct.json",
        "grandeurs": "b-alpha-grandeurs.json",
        "par_pole": "grandeurs-par-pole-b-alpha-v1.json",
        "measure": "b-alpha-measure.json",
    },
    "lot64": {
        "resume": "causal_lens_lot64_llama-3.1-8b-instruct.json",
        "grandeurs": "b-alpha-grandeurs-lot64.json",
        "par_pole": "grandeurs-par-pole-b-alpha-lot64-v1.json",
        "measure": "b-alpha-measure-lot64.json",
    },
}
AUDITS = {  # fichiers dont la présence dit qu'un audit a été joué (plan, étape 3 bis)
    "lot16": {
        "trop_beau_ou_b7": "b-alpha-audit-trop-beau.json",
        "resume_graine1": "causal_lens_seed1_llama-3.1-8b-instruct.json",
        "grandeurs_graine1": "grandeurs-par-pole-b-alpha-graine1-v1.json",
    },
    "lot64": {
        "trop_beau_ou_b7": "b-alpha-audit-trop-beau-lot64.json",
        "resume_graine1": "causal_lens_seed1-lot64_llama-3.1-8b-instruct.json",
        "grandeurs_graine1": "grandeurs-par-pole-b-alpha-graine1-lot64-v1.json",
    },
    "commun": {"tout_negatif": "b-alpha-audit-tout-negatif.json"},
}
LISIBLE_N = 48


def sha(chemin: str) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def charger(chemin: str):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def r4(x: float) -> float:
    """Arrondi à 4 décimales (les valeurs de `score` le sont déjà ; sert aux différences)."""
    return round(float(x) + 0.0, 4)


def couches(a: int, b: int) -> list[int]:
    return list(range(a, b + 1))


# ---------------------------------------------------------------- lisibilité et bandes
def lisibles(n: list[int], bande: list[int]) -> list[int]:
    return [l for l in bande if n[l] >= LISIBLE_N]


def etat_bande(n: list[int], bande: list[int]) -> dict:
    lis = lisibles(n, bande)
    non = [l for l in bande if l not in lis]
    return {
        "couches": [bande[0], bande[-1]],
        "lisibles": len(lis),
        "non_lisibles": non,
        "partielle": len(non) > len(bande) / 4,
        "jugeable": len(lis) > 0,
    }


def plus_de_la_moitie(compte: int, nb_lisibles: int) -> bool:
    return nb_lisibles > 0 and compte > nb_lisibles / 2


# ---------------------------------------------------------------- chaîne en défaut
def essai_ok(resume: str, code: int) -> tuple[bool, str]:
    s = resume or ""
    m = re.fullmatch(r"(\d+) passed in [0-9.]+s", s.strip())
    saute = re.search(r"skipped|xfail|xpass|deselected", s)
    echec = re.search(r"failed|error", s)
    ok = code == 0 and m is not None and not saute and not echec
    return ok, s


def chaine_b0(diag: str) -> dict:
    b0 = charger(os.path.join(diag, "b-alpha-b0.json"))["resultat"]
    b3 = charger(os.path.join(diag, "b-alpha-b3.json"))["resultat"]
    fumee = charger(os.path.join(diag, "b-alpha-fumee.json"))["resultat"]
    partie2 = charger(os.path.join(diag, "b-alpha-partie2.json"))["resultat"]
    essais = {}
    for nom, e in b0["essais"].items():
        ok, s = essai_ok(e.get("resume", ""), e.get("code", -1))
        essais[nom] = {"ok": ok, "resume": s, "code": e.get("code")}
    correctifs = {k: v for k, v in essais.items()
                  if k in ("essai-06_activations-llama-v3.py", "essai-lenses-neuronpedia-v3.py")}
    lentilles = {}
    for nom, L in b0["lentilles"].items():
        m = re.search(r"layers (\d+)-(\d+)", L.get("sortie", ""))
        contig = bool(m) and int(m.group(1)) == 0 and int(m.group(2)) == 30
        lentilles[nom] = {
            "couches_0_30_contigues_31": contig,
            "defauts_identite_e": L.get("defauts", []),
            "arrets": L.get("arrets", []),
        }
    b3_ok = [essai_ok(b0["verdicts_b3"]["resume"], b0["verdicts_b3"]["code"])[0],
             essai_ok(b3["verdicts_b3"]["resume"], b3["verdicts_b3"]["code"])[0]]
    fumee_ok = fumee.get("code") == 0 and any("smoke test done" in x for x in fumee.get("fin", []))
    d = (not all(v["ok"] for v in correctifs.values())) or (not fumee_ok)
    e_identite = any(v["defauts_identite_e"] for v in lentilles.values())
    arret_b0 = any(v["arrets"] for v in lentilles.values()) or not all(
        v["couches_0_30_contigues_31"] for v in lentilles.values())
    return {
        "essais_b0": essais,
        "correctifs_1_2_ok_sans_test_saute": all(v["ok"] for v in correctifs.values()),
        "lentilles_b0": lentilles,
        "b3_rejoue_ok": b3_ok,
        "fumee_ok": fumee_ok,
        "partie2_ecarts": partie2.get("ecarts"),
        "partie2_instance_vide": partie2.get("releve", {}).get("instance", None) in ("", None),
        "condition_d": d,
        "condition_e_identite_b0": e_identite,
        "arret_b0": arret_b0,
    }


def chaine_serie(t: dict, n: dict, ecartes: dict, b0: dict) -> dict:
    a = []
    for c in CIBLES:
        for le in LENTILLES:
            for l in couches(0, 27):
                v = t[c][le]["control_med"][l]
                if abs(v) > 0.10:
                    a.append({"cible": c, "lentille": le, "couche": l, "control_med": v})
    b = []
    effet_nul = ecartes["steer 1x"].get("effet nul")
    if effet_nul is None:
        b_note = "motif « effet nul » non séparé par la course"
    else:
        b_note = "compte par motif « effet nul » écrit par la course"
        for l in couches(0, 27):
            if effet_nul[l] > 32:
                b.append({"couche": l, "ecartes_effet_nul": effet_nul[l]})
    c_ = []
    for l in couches(28, 30):
        v = t["steer 1x"]["logit"]["r_med"][l]
        if v < 0.80:
            c_.append({"lentille": "logit", "couche": l, "r_med": v})
        v = t["steer 1x"]["npR"]["r_med"][l]
        if v < 0.85:
            c_.append({"lentille": "npR", "couche": l, "r_med": v})
    e = []
    for le in ("J", "npJpp", "npR"):
        for l in couches(0, 23):
            dlt = abs(r4(t["steer 1x"][le]["r_med"][l] - t["steer 1x"]["logit"]["r_med"][l]))
            if dlt < 1e-3:
                e.append({"lentille": le, "couche": l, "ecart": dlt})
    defaut = bool(a or b or c_ or e or b0["condition_d"] or b0["condition_e_identite_b0"])
    return {
        "a": a, "b": b, "b_note": b_note, "c": c_, "d": b0["condition_d"],
        "e_repli": e, "e_identite_b0": b0["condition_e_identite_b0"],
        "chaine_en_defaut": defaut,
    }


# ---------------------------------------------------------------- mesures
def verdict_b2(t: dict, n1: list[int]) -> dict:
    r = t["steer 1x"]["npR"]["r_med"]
    p = t["steer 1x"]["npR"]["pass"]
    cm = t["steer 1x"]["npR"]["control_med"]
    bandes = {"8-15": couches(8, 15), "16-23": couches(16, 23), "24-27": couches(24, 27),
              "pass 8-27": couches(8, 27), "16-27": couches(16, 27)}
    etat = {k: etat_bande(n1, v) for k, v in bandes.items()}
    seuils = [(couches(8, 15), 0.40), (couches(16, 23), 0.60), (couches(24, 27), 0.85)]
    echecs_r = [l for bande, s in seuils for l in lisibles(n1, bande) if r[l] < s]
    echecs_pass = [l for l in lisibles(n1, couches(8, 27)) if p[l] < 0.90]
    marges_r = {l: r4(r[l] - s) for bande, s in seuils for l in lisibles(n1, bande)}
    marges_pass = {l: r4(p[l] - 0.90) for l in lisibles(n1, couches(8, 27))}

    def temoin(ensemble):
        hors05 = [l for l in ensemble if abs(cm[l]) > 0.05]
        hors10 = [l for l in ensemble if abs(cm[l]) > 0.10]
        return {"hors_005": hors05, "hors_010": hors10, "ok": len(hors05) <= 1 and not hors10}

    temoin_toutes = temoin(couches(0, 27))
    temoin_lisibles = temoin(lisibles(n1, couches(0, 27)))
    lis1627 = lisibles(n1, couches(16, 27))
    lis1623 = lisibles(n1, couches(16, 23))
    np_pass = [l for l in lis1627 if p[l] < 0.50]
    np_r = [l for l in lis1623 if r[l] < 0.30]
    non = plus_de_la_moitie(len(np_pass), len(lis1627)) or plus_de_la_moitie(len(np_r), len(lis1623))

    def issue(temoin_ok):
        if not echecs_r and not echecs_pass and temoin_ok and all(
                etat[k]["jugeable"] for k in ("8-15", "16-23", "24-27")):
            return "reproduit"
        if non:
            return "non reproduit"
        return "autre"

    v_toutes = issue(temoin_toutes["ok"])
    v_lis = issue(temoin_lisibles["ok"])
    partielle = [k for k in ("8-15", "16-23", "24-27", "pass 8-27") if etat[k]["partielle"]]
    return {
        "verdict": v_toutes if v_toutes == v_lis else None,
        "verdict_temoin_toutes_couches": v_toutes,
        "verdict_temoin_couches_lisibles": v_lis,
        "ambiguite_1_diverge": v_toutes != v_lis,
        "bandes": etat, "bandes_partielles": partielle,
        "echecs_r_med": echecs_r, "echecs_pass": echecs_pass,
        "temoin_toutes": temoin_toutes, "temoin_lisibles": temoin_lisibles,
        "non_reproduit_pass_lt_050": np_pass, "non_reproduit_r_lt_030": np_r,
        "marge_min_r_med": min(marges_r.values()) if marges_r else None,
        "marge_min_pass": min(marges_pass.values()) if marges_pass else None,
        "marges_r_med": marges_r, "marges_pass": marges_pass,
    }


def verdict_b3(t: dict, n1: list[int]) -> dict:
    rR = t["steer 1x"]["npR"]["r_med"]
    rL = t["steer 1x"]["logit"]["r_med"]
    bande = couches(4, 15)
    lis = lisibles(n1, bande)
    ecart = {l: r4(rR[l] - rL[l]) for l in bande}
    ecart_brut = {l: float(rR[l] - rL[l]) for l in bande}
    rep = bool(lis) and all(ecart[l] >= 0.20 for l in lis)
    rep_brut = bool(lis) and all(ecart_brut[l] >= 0.20 for l in lis)
    neg = [l for l in lis if ecart[l] <= 0]
    neg_brut = [l for l in lis if ecart_brut[l] <= 0]
    non = plus_de_la_moitie(len(neg), len(lis))
    v = "reproduit" if rep else ("non reproduit" if non else "autre")
    vb = "reproduit" if rep_brut else ("non reproduit" if plus_de_la_moitie(len(neg_brut), len(lis)) else "autre")
    return {
        "verdict": v, "verdict_difference_flottante_brute": vb, "ambiguite_4_diverge": v != vb,
        "bande": etat_bande(n1, bande), "ecart": ecart,
        "echecs_ecart_lt_020": [l for l in lis if ecart[l] < 0.20],
        "ecart_le_0": neg, "marge_min": min(r4(ecart[l] - 0.20) for l in lis) if lis else None,
    }


def b4(t: dict) -> dict:
    rR = t["steer 1x"]["npR"]["r_med"]
    return {le: {l: r4(rR[l] - t["steer 1x"][le]["r_med"][l]) for l in couches(4, 23)}
            for le in ("J", "npJpp")}


def verdict_b7(t: dict, nw: list[int]) -> dict:
    r = t["ablate win"]["npR"]["r_med"]
    b015, b815, b2629 = couches(0, 15), couches(8, 15), couches(26, 29)
    l015, l815, l2629 = lisibles(nw, b015), lisibles(nw, b815), lisibles(nw, b2629)
    bas_ok = [l for l in l015 if r[l] < 0.25]
    haut_ok = [l for l in l2629 if r[l] >= 0.50]
    rep = bool(l015) and bool(l2629) and len(bas_ok) == len(l015) and len(haut_ok) == len(l2629)
    haut = [l for l in l815 if r[l] >= 0.40]
    bas = [l for l in l2629 if r[l] < 0.30]
    par_le_haut = plus_de_la_moitie(len(haut), len(l815))
    par_le_bas = plus_de_la_moitie(len(bas), len(l2629))
    if rep:
        v = "reproduit"
    elif par_le_haut and par_le_bas:
        v = "non reproduit par le haut et par le bas"
    elif par_le_haut:
        v = "non reproduit par le haut"
    elif par_le_bas:
        v = "non reproduit par le bas"
    else:
        v = "autre"
    par_couche = {}
    for l in couches(0, 29):
        if l <= 15:
            etat = "lisible" if l in l015 else "non lisible"
            par_couche[l] = {"r_med": r[l], "n": nw[l], "lisible": etat == "lisible",
                             "lt_025": r[l] < 0.25, "ge_040_si_8_15": (r[l] >= 0.40) if l >= 8 else None}
        elif l >= 26:
            par_couche[l] = {"r_med": r[l], "n": nw[l], "lisible": l in l2629,
                             "ge_050": r[l] >= 0.50, "lt_030": r[l] < 0.30}
        else:
            par_couche[l] = {"r_med": r[l], "n": nw[l], "hors_bandes": True}
    return {
        "verdict": v, "par_le_haut": par_le_haut, "par_le_bas": par_le_bas,
        "bandes": {"0-15": etat_bande(nw, b015), "8-15": etat_bande(nw, b815), "26-29": etat_bande(nw, b2629)},
        "couches_0_15_ge_025": [l for l in l015 if r[l] >= 0.25],
        "couches_26_29_lt_050": [l for l in l2629 if r[l] < 0.50],
        "couches_8_15_ge_040": haut, "couches_26_29_lt_030": bas,
        "marge_min_0_15": min(r4(0.25 - r[l]) for l in l015) if l015 else None,
        "marge_min_26_29": min(r4(r[l] - 0.50) for l in l2629) if l2629 else None,
        "par_couche": par_couche,
    }


def verdict_reproduction(defaut: bool, v2: str | None, v3: str) -> str:
    if defaut:
        return "chaîne en défaut"
    if v2 == "reproduit" and v3 == "reproduit":
        return "reproduit avec la lentille R publique"
    if v2 == "non reproduit" or v3 == "non reproduit":
        return "non reproduit avec la lentille R publique"
    return "partiel"


def audits(t: dict, v2: str | None, v3: str, v7: dict) -> dict:
    r = t["steer 1x"]["npR"]["r_med"]
    cm = t["steer 1x"]["npR"]["control_med"]
    hauts = [l for l in couches(0, 7) if r4(r[l]) >= 0.95]
    zeros = [l for l in couches(0, 27) if r4(cm[l]) == 0.0]
    return {
        "trop_beau": bool(hauts) or len(zeros) >= 2,
        "trop_beau_detail": {"r_med_ge_095_couches_0_7": hauts, "control_med_zero_couches_0_27": zeros,
                             "r_med_max_0_7": max(r[l] for l in couches(0, 7))},
        "tout_negatif": v2 == "non reproduit" and v3 == "non reproduit",
        "b7_par_le_haut": bool(v7["par_le_haut"]),
    }


# ---------------------------------------------------------------- trop propre (signalé, sans verdict)
def trop_propre(t: dict, n: dict, par_pole: dict) -> dict:
    out = {}
    out["n_constant"] = {c: sorted(set(n[c])) for c in CIBLES}
    ident_lent = []
    for c in CIBLES:
        for i, a in enumerate(LENTILLES):
            for b in LENTILLES[i + 1:]:
                if t[c][a]["r_med"][:31] == t[c][b]["r_med"][:31]:
                    ident_lent.append([c, a, b])
    out["lentilles_identiques_couches_0_30"] = ident_lent
    ident_couches = []
    for c in CIBLES:
        for le in LENTILLES:
            rr = t[c][le]["r_med"][:31]
            for l in range(1, 31):
                if rr[l] == rr[l - 1]:
                    ident_couches.append([c, le, l - 1, l, rr[l]])
    out["couches_voisines_r_med_identique"] = ident_couches
    largeur_nulle = []
    for c in CIBLES:
        for le in LENTILLES:
            q25, q75 = t[c][le].get("r_q25"), t[c][le].get("r_q75")
            if q25 and q75:
                for l in range(31):
                    if q25[l] == q75[l]:
                        largeur_nulle.append([c, le, l])
    out["intervalles_largeur_nulle"] = largeur_nulle
    # fidélité du tableau des grandeurs par pôle au résumé de `score`
    ecarts = []
    tab = par_pole.get("table", {})
    for c in CIBLES:
        for le in LENTILLES:
            for k in ("r_med", "control_med", "pass"):
                a = tab.get(c, {}).get(le, {}).get(k)
                b = t[c][le][k]
                if a is not None:
                    ecarts.append(max(abs(x - y) for x, y in zip(a, b)))
    out["ecart_max_table_par_pole_vs_resume"] = max(ecarts) if ecarts else None
    # pôles retenus, recomptés sur les grandeurs par pôle
    compte = {c: [0] * 32 for c in CIBLES}
    for p in par_pole.get("poles", []):
        for c in CIBLES:
            if p["lectures"][c]["npR"]["motif"] == "retenu":
                compte[c][p["couche"]] += 1
    out["n_recompte_par_pole_egal_n_ecrit"] = {c: compte[c] == list(n[c]) for c in CIBLES}
    return out


# ---------------------------------------------------------------- comparaisons
def ecarts(tA: dict, tB: dict, cibles: list[str]) -> dict:
    cell = {}
    max_par_cible = {}
    for c in cibles:
        m = 0.0
        arg = None
        cell[c] = {}
        for le in LENTILLES:
            a = np.array(tA[c][le]["r_med"][:31], dtype=float)
            b = np.array(tB[c][le]["r_med"][:31], dtype=float)
            d = np.round(a - b, 4)
            cell[c][le] = d.tolist()
            k = int(np.argmax(np.abs(d)))
            if abs(d[k]) > m or arg is None:
                m, arg = float(abs(d[k])), {"lentille": le, "couche": k, "delta": float(d[k])}
        max_par_cible[c] = {"max_abs": m, "ou": arg}
    return {"delta_par_cellule_A_moins_B": cell, "max_par_cible": max_par_cible,
            "max_global": max(v["max_abs"] for v in max_par_cible.values())}


# ---------------------------------------------------------------- une série
def serie(diag: str, noms: dict, b0: dict) -> dict:
    t = charger(os.path.join(diag, noms["resume"]))["targets"]
    gr = charger(os.path.join(diag, noms["grandeurs"]))["resultat"]
    pp = charger(os.path.join(diag, noms["par_pole"]))
    n, ec = gr["n"], gr["ecartes"]
    ch = chaine_serie(t, n, ec, b0)
    v2 = verdict_b2(t, n["steer 1x"])
    v3 = verdict_b3(t, n["steer 1x"])
    v7 = verdict_b7(t, n["ablate win"])
    au = audits(t, v2["verdict"], v3["verdict"], v7)
    if v2["verdict"] is None:
        rep = {"temoin_toutes_couches": verdict_reproduction(ch["chaine_en_defaut"], v2["verdict_temoin_toutes_couches"], v3["verdict"]),
               "temoin_couches_lisibles": verdict_reproduction(ch["chaine_en_defaut"], v2["verdict_temoin_couches_lisibles"], v3["verdict"])}
    else:
        rep = verdict_reproduction(ch["chaine_en_defaut"], v2["verdict"], v3["verdict"])
    return {
        "fichiers": {k: {"chemin": os.path.join(diag, v), "sha256": sha(os.path.join(diag, v))}
                     for k, v in noms.items() if os.path.exists(os.path.join(diag, v))},
        "chaine": ch, "B2": v2, "B3": v3, "B4": b4(t), "B7": v7,
        "verdict_reproduction": rep, "audits_declenches_par_le_lecteur": au,
        "trop_propre": trop_propre(t, n, pp),
        "_t": t,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--rtx4090", default=None, help="étape 6 seulement : diag de la troisième course")
    args = ap.parse_args()

    out: dict = {"plan": "docs/notes/neuron-lens-v1/lecture-recourse-b7/plan-de-lecture-recourse-b7-v3.md",
                 "plan_sha256": sha("docs/notes/neuron-lens-v1/lecture-recourse-b7/plan-de-lecture-recourse-b7-v3.md"),
                 "manifeste_sha256": sha(MANIFESTE)}
    b0 = chaine_b0(A100)
    out["b0_fumee_partie2"] = b0

    # étape 3 : lots écrits, bascule
    m16 = charger(os.path.join(A100, "b-alpha-measure.json"))["resultat"]
    m64 = charger(os.path.join(A100, "b-alpha-measure-lot64.json"))["resultat"]
    bas = charger(os.path.join(A100, "b-alpha-bascule-lot64.json"))["resultat"]
    depl = bas["deplaces"]["llama-3.1-8b-instruct-causal.pt"]
    out["lots"] = {
        "lot_measure": m16.get("lot"), "lot_measure_lot64": m64.get("lot"),
        "bascule_sha_egale_measure_lot16": depl["sha256"] == m16["causal"]["sha256"],
        "causal_sha_lot16": m16["causal"]["sha256"], "causal_sha_lot64": m64["causal"]["sha256"],
        "causal_lot64_identique_lot16": m16["causal"]["sha256"] == m64["causal"]["sha256"],
    }

    # étape 3 bis : audits joués (présence des fichiers)
    joues = {}
    for s, d in AUDITS.items():
        joues[s] = {k: os.path.exists(os.path.join(A100, v)) for k, v in d.items()}
    out["audits_joues_constat_fichiers"] = joues

    series = {s: serie(A100, noms, b0) for s, noms in SERIES.items()}
    tt = {s: series[s].pop("_t") for s in series}
    out["series"] = series
    out["series_resumes_identiques_octet_pour_octet"] = (
        series["lot16"]["fichiers"]["resume"]["sha256"] == series["lot64"]["fichiers"]["resume"]["sha256"])
    out["series_par_pole_identiques_octet_pour_octet"] = (
        series["lot16"]["fichiers"]["par_pole"]["sha256"] == series["lot64"]["fichiers"]["par_pole"]["sha256"])

    # divergences d'audit lecteur / course (constat par fichiers)
    div = []
    for s in ("lot16", "lot64"):
        au = series[s]["audits_declenches_par_le_lecteur"]
        joue_tb = joues[s]["trop_beau_ou_b7"]
        lecteur_tb_ou_b7 = au["trop_beau"] or au["b7_par_le_haut"]
        if lecteur_tb_ou_b7 and not joue_tb:
            div.append({"serie": s, "cas": "le lecteur déclenche « trop beau » ou « B-7 par le haut », la course ne l'a pas joué"})
        if joue_tb and not lecteur_tb_ou_b7:
            div.append({"serie": s, "cas": "la course a joué un audit que le lecteur ne déclenche pas"})
        if au["tout_negatif"] and not joues["commun"]["tout_negatif"]:
            div.append({"serie": s, "cas": "le lecteur déclenche « tout négatif », la course ne l'a pas joué"})
    if joues["commun"]["tout_negatif"] and not any(series[s]["audits_declenches_par_le_lecteur"]["tout_negatif"] for s in series):
        div.append({"serie": "commun", "cas": "la course a joué « tout négatif », le lecteur ne le déclenche pas"})
    out["divergences_audits"] = div

    # § 4 : B-7 de la recourse
    s64 = series["lot64"]
    v7 = s64["B7"]["verdict"]
    if s64["chaine"]["chaine_en_defaut"]:
        b7r = {"lecture": None, "raison": "série au lot 64 en chaîne en défaut"}
    elif s64["B7"]["par_le_haut"]:
        if not joues["lot64"]["trop_beau_ou_b7"]:
            b7r = {"lecture": None, "raison": "« par le haut » déclenché par le lecteur sans audit joué par la course"}
        else:
            b7r = {"lecture": "à lire sur l'audit (critère (1) à (3))", "raison": "audit joué"}
    else:
        b7r = {"lecture": v7, "raison": "série au lot 64 sans chaîne en défaut ; aucun motif « par le haut »"}
    out["B7_recourse"] = b7r

    # comparaisons (a) et (c)
    ca = ecarts(tt["lot64"], tt["lot16"], ["ablate win", "ablate pos"])
    cc = ecarts(tt["lot64"], tt["lot16"], ["steer 1x", "steer 4x"])
    out["comparaison_a_lot64_moins_lot16"] = ca
    out["comparaison_c_lot64_moins_lot16"] = cc
    out["c_reserve_stabilite_gt_001"] = cc["max_global"] > 0.01
    out["a_dans_le_bruit_par_cible"] = {c: ca["max_par_cible"][c]["max_abs"] <= cc["max_global"]
                                        for c in ("ablate win", "ablate pos")}

    # comparaison (b), étape 6 seulement
    if args.rtx4090:
        R = args.rtx4090
        nomsR = {"resume": "causal_lens_llama-3.1-8b-instruct.json", "grandeurs": "b-alpha-grandeurs.json",
                 "par_pole": "grandeurs-par-pole-b-alpha-v1.json", "measure": "b-alpha-measure.json"}
        b0R = chaine_b0(R)
        sR = serie(R, nomsR, b0R)
        tR = sR.pop("_t")
        out["rtx4090_lot16_recalcul_lecteur"] = {"b0_fumee_partie2": b0R, **sR}
        out["comparaison_b_a100_lot16_moins_rtx4090_lot16"] = ecarts(tt["lot16"], tR, CIBLES)
        try:
            pA = charger(os.path.join(A100, "b-alpha-partie2.json"))["resultat"]["releve"]["corpus"]
            pR = charger(os.path.join(R, "b-alpha-partie2.json"))["resultat"]["releve"]["corpus"]
            out["corpus_partie2"] = {
                "a100": {k: v.get("sha256") for k, v in pA.items()},
                "rtx4090": {k: v.get("sha256") for k, v in pR.items()},
                "identiques": {k: pA[k].get("sha256") == pR.get(k, {}).get("sha256") for k in pA},
            }
        except (OSError, KeyError) as exc:
            out["corpus_partie2"] = {"erreur": repr(exc)}

    with open(args.sortie, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=False)
    print(json.dumps({s: {"chaine_en_defaut": series[s]["chaine"]["chaine_en_defaut"],
                          "B2": series[s]["B2"]["verdict"], "B3": series[s]["B3"]["verdict"],
                          "B7": series[s]["B7"]["verdict"],
                          "reproduction": series[s]["verdict_reproduction"],
                          "audits": series[s]["audits_declenches_par_le_lecteur"]} for s in series},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
