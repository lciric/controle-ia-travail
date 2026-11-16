"""Complément de la lecture de B-α (lecteur neuf, v1), écrit APRÈS `calcul-verdicts-b-alpha-v1.json` (`6f0b9078…`) :
(1) où le recalcul par pôle de `pass` s'écarte du résumé de `score` ; (2) valeurs non arrondies (r par pôle à 6 décimales) aux couches
proches d'un seuil ; (3) comparaison de mes verdicts à ceux de la course (`b-alpha-verdicts.json`), lus seulement ici ;
(4) comparaison à la référence publiée de Qwen3-8B n'est PAS faite (fichier hors des pièces extraites).
Usage : python -I complement_lecture_b_alpha_v1.py DOSSIER_DIAG MON_CALCUL.json SORTIE.json
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

CIBLES = ("steer 1x", "steer 4x", "ablate pos", "ablate win")
LENTILLES = ("logit", "J", "npJpp", "npR")


def med(x):
    x = np.sort(np.asarray(x, float))
    return float(x[(len(x) - 1) // 2])


def main(dossier, mien, sortie):
    d = Path(dossier)
    T = json.loads((d / "causal_lens_llama-3.1-8b-instruct.json").read_text())["targets"]
    pp = json.loads((d / "grandeurs-par-pole-b-alpha-v1.json").read_text())
    moi = json.loads(Path(mien).read_text())
    vc = json.loads((d / "b-alpha-verdicts.json").read_text())["resultat"]
    par = {}
    for p in pp["poles"]:
        if p["aleatoire"]:
            for c in CIBLES:
                for s in LENTILLES:
                    x = p["lectures"][c][s]
                    if x["motif"] == "retenu":
                        par.setdefault((c, s, p["couche"]), []).append((x["r"], x["r_temoin"]))
    par = {k: np.asarray(v, float) for k, v in par.items()}
    seuil = {k: float(v) for k, v in pp["centile_temoin"].items()}  # centile commun non arrondi (6 décimales), écrit par la course
    ecarts_pass = []
    for c in CIBLES:
        for s in LENTILLES:
            for l in range(32):
                a = par[(c, s, l)][:, 0]
                p_moi_seuil_course = float(np.mean(a > seuil[f"{c}|{s}"]))
                if abs(p_moi_seuil_course - T[c][s]["pass"][l]) > 6e-5:
                    proche = float(np.min(np.abs(a - seuil[f"{c}|{s}"])))
                    ecarts_pass.append({"cible": c, "lentille": s, "couche": l, "pass_score": T[c][s]["pass"][l],
                                        "pass_recalcule_avec_le_centile_de_la_course": round(p_moi_seuil_course, 4),
                                        "distance_du_r_le_plus_proche_au_seuil": round(proche, 6)})
    r = lambda c, s, l: med(par[(c, s, l)][:, 0])
    pres_des_seuils = {
        "B-2 r_med npR steer 1x couche 8 (seuil 0,40)": r("steer 1x", "npR", 8),
        "B-2 r_med npR steer 1x couche 9 (seuil 0,40)": r("steer 1x", "npR", 9),
        "B-2 pass npR steer 1x couches 8, 9, 10 (seuil 0,90), en 64èmes":
            [int(round(64 * T["steer 1x"]["npR"]["pass"][l])) for l in (8, 9, 10)],
        "B-2 distance au centile commun du r le plus proche, npR steer 1x, couches 8, 9, 10":
            [round(float(np.min(np.abs(par[("steer 1x", "npR", l)][:, 0] - seuil["steer 1x|npR"]))), 6) for l in (8, 9, 10)],
        "B-2 centile commun du témoin npR steer 1x": seuil["steer 1x|npR"],
        "B-3 écart couche 4 (seuil 0,20)": r("steer 1x", "npR", 4) - r("steer 1x", "logit", 4),
        "B-3 écart couche 5 (seuil 0,20)": r("steer 1x", "npR", 5) - r("steer 1x", "logit", 5),
        "B-7 r_med npR ablate win couches 13, 14, 15 (seuil 0,25)": [r("ablate win", "npR", l) for l in (13, 14, 15)],
        "B-7 r_med ablate win couche 15 par lentille": {s: r("ablate win", s, 15) for s in LENTILLES},
        "B-7 nombre de pôles (sur 64) de r >= 0,25, npR ablate win, couches 12 à 16":
            {l: int(np.sum(par[("ablate win", "npR", l)][:, 0] >= 0.25)) for l in range(12, 17)},
    }
    pres_des_seuils = {k: (round(v, 6) if isinstance(v, float) else v) for k, v in pres_des_seuils.items()}
    # médiane ordinaire (moyenne des deux valeurs centrales) : autre convention, pour information
    med_ord = {"B-2 r_med couche 8": round(float(np.median(par[("steer 1x", "npR", 8)][:, 0])), 6),
               "B-3 écart couche 4": round(float(np.median(par[("steer 1x", "npR", 4)][:, 0]) - np.median(par[("steer 1x", "logit", 4)][:, 0])), 6),
               "B-7 r_med couche 15": round(float(np.median(par[("ablate win", "npR", 15)][:, 0])), 6)}
    v = vc["verdict"]
    traduction = {"autre": "partiel"}
    m_b2 = {moi["B-2"]["verdict_lecture_temoin_toutes_couches"], moi["B-2"]["verdict_lecture_temoin_couches_lisibles"]}
    comparaison = {
        "B-2": {"course": v["b2"]["verdict"], "lecteur": sorted(m_b2), "accord": {traduction.get(x, x) for x in m_b2} == {v["b2"]["verdict"]}},
        "B-3": {"course": v["b3"]["verdict"], "lecteur": moi["B-3"]["verdict"], "accord": v["b3"]["verdict"] == traduction.get(moi["B-3"]["verdict"], moi["B-3"]["verdict"]),
                "ecart_min_course": v["b3"]["details"]["ecart_min_4_15"], "ecart_min_lecteur": round(moi["B-3"]["marge_min"][0] + 0.20, 4)},
        "B-7": {"course": v["b7"]["verdict"], "lecteur": moi["B-7"]["verdict"], "accord": v["b7"]["verdict"] == traduction.get(moi["B-7"]["verdict"], moi["B-7"]["verdict"])},
        "B-4": {"accord_J": v["b4"]["J"] == [moi["B-4"]["npR - J"][str(l)] for l in range(4, 24)],
                "accord_npJpp": v["b4"]["npJpp"] == [moi["B-4"]["npR - npJpp"][str(l)] for l in range(4, 24)]},
        "defauts": {"course": v["defauts"], "lecteur": moi["chaine_en_defaut"]["defauts"], "accord": v["defauts"] == moi["chaine_en_defaut"]["defauts"] == []},
        "audits": {"course": vc["audits_requis"], "lecteur": [k for k in ("trop_beau", "tout_negatif") if moi["audits_R4"][k]],
                   "accord": vc["audits_requis"] == [] and not moi["audits_R4"]["trop_beau"] and not moi["audits_R4"]["tout_negatif"]},
        "reproduction": {"course": v["verdict"], "lecteur": moi["verdict_reproduction"],
                         "accord": set(moi["verdict_reproduction"].values()) == {v["verdict"]}},
        "intervalles_npR_steer_1x : plus grand écart de borne entre la course et le lecteur (graines différentes)":
            round(max(abs(a - b) for l in range(32) for a, b in zip(vc["intervalles"]["steer 1x"]["npR"][l],
                                                                     moi["intervalles_95"]["valeurs"]["steer 1x, npR, r_med"][str(l)])), 4),
        "intervalles_de_la_course : cibles et lentilles écrites": {c: sorted(x) for c, x in vc["intervalles"].items() if isinstance(x, dict)},
    }
    out = {"entrees_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                              (d / "causal_lens_llama-3.1-8b-instruct.json", d / "grandeurs-par-pole-b-alpha-v1.json", d / "b-alpha-verdicts.json", Path(mien))},
           "ecarts_de_pass_au_resume_de_score": ecarts_pass, "pres_des_seuils_non_arrondi": pres_des_seuils,
           "mediane_ordinaire_pour_information": med_ord, "comparaison_a_la_course": comparaison}
    Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 4 or Path(sys.argv[3]).exists():
        raise SystemExit(__doc__)
    main(*sys.argv[1:])
