"""Grille du préenregistrement hors échantillon, brouillon 2, et tables des valeurs prédites — v2 (sans tirage).

Différences avec `generer_grille_v1.py` (contre-lecture 1, recommandations R1, R2, R3, R6) :
- R1 : HP.5 scindée — HP.5a = les 7 cellules « en dessous » de la sonde des enjeux (`coelev_comptage` m = 3, 4, 5 ;
  `pas_moyenne` m = 3, 4, 5, 6), HP.5b = les 13 autres cellules de signe de `coelev_comptage` et `pas_moyenne` ;
- R2 : HP.4 bilatérale, x_bas = ⌊100 (v_mod − 0,15)⌋/100, x_haut = ⌈100 (v_mod + 0,15)⌉/100 (sens « entre_x ») ;
- R6 : table S donnée en valeur exacte (`bornes_synchro_v2.puissance_exacte`, erreur certifiée) ; la lecture v2
  la recalcule au seuil du run ;
- R3 : clé `descriptif_maxima` (position des maxima des agents dans des essaims honnêtes, familles Q et P, sans verdict) ;
- chaque prédiction de sens porte `discriminante` (vrai si une prédiction écrite pour la loi de référence, ou par v1, à
  la même fraction, donne le sens opposé ou rendrait la cellule contraire ; contre-lecture 1, C1).
Règles de sélection inchangées par ailleurs (voir `generer_grille_v1.py`). Valeurs du modèle recopiées de
`sortie-moments_et_substitution_v1.txt`.

    PYTHONPATH=src python brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/generer_grille_v2.py
"""
import json
import math
from collections import Counter
from pathlib import Path

from controle_ia.simulation_essaim import bornes_synchro_v1 as BS
from controle_ia.simulation_essaim import bornes_synchro_v2 as BS2
from controle_ia.simulation_essaim.loi_p3_v1 import CHEMIN, SHA256, SONDES

ICI = Path(__file__).resolve().parent
ALPHA, Q = 0.05, 0.1
PANNEAU = {a: "exact" for a in ("somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne",
                                 "coelev_comptage")}
PANNEAU.update({"coelev_somme3": "mc", "e_coelev_cal": "mc", "ed_coelev": "mc"})
ALARMES_LOI = ["somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne", "coelev_comptage",
               "coelev_somme3", "e_coelev", "ed_coelev"]


def synchro(m):
    return {"nom": f"T_synchro_m{m}", "genre": "synchro", "groupe": "temps", "m": m, "r": 1}


MS = {"e10x10": (10, 10, [3, 4, 5, 6, 7, 10]), "e20x10": (20, 10, [6, 8, 10, 12, 14, 20])}
Q_LOIS = {"c0.1": (0.1, [3, 5, 7, 10]), "c0.3": (0.3, [3, 5, 7, 10]), "c0.4": (0.4, [5])}
MP = [3, 4, 5, 6, 7, 10]
ENJEUX = SONDES[1]
V_MOD = {   # (pas_moyenne, coelev_comptage, e_coelev, ed_coelev), sortie-moments_et_substitution_v1.txt
    SONDES[0]: {3: (0.0447, 0.0481, 0.046, 0.0471), 4: (0.0666, 0.0669, 0.042, 0.0435), 5: (0.1133, 0.1227, 0.0377, 0.0392),
                6: (0.2119, 0.2172, 0.0317, 0.0338), 7: (0.3673, 0.3282, 0.0273, 0.0305), 10: (0.9586, 0.705, 0.0151, 0.0181)},
    ENJEUX: {3: (0.0215, 0.0245, 0.0839, 0.0505), 4: (0.0208, 0.0243, 0.1033, 0.0461), 5: (0.0243, 0.0315, 0.1223, 0.043),
             6: (0.0338, 0.0469, 0.1437, 0.04), 7: (0.064, 0.1034, 0.151, 0.0365), 10: (0.5486, 0.4629, 0.1681, 0.0232)},
}
K_P = 10


def discriminante_p(a, m, sens):
    """Référence écrite à la même fraction : co-élévation au-dessus dès m/K = 0,3 (HS.3, HS.4) ; e-valeurs au plus, en
    dessous à m = K (HS.5, HE2.5 de v1) ; `pas_moyenne` au-dessus pour m ≥ ⌈K/2⌉ (HE2.4 de v1)."""
    if a == "coelev_comptage":
        return sens == "en_dessous"
    if a == "pas_moyenne":
        return sens == "en_dessous" and m >= math.ceil(K_P / 2)
    if a in ("e_coelev", "ed_coelev"):
        return sens == "au_dessus"
    return False


configs = {cfg: {"K": K, "T": T, "panneau": dict(PANNEAU)} for cfg, (K, T, _) in MS.items()}
configs["e10x20"] = {"K": 10, "T": 20, "panneau": dict(PANNEAU)}
preds, table = [], ["## Tables des valeurs prédites (sans tirage) — brouillon 2", ""]

table += ["### Famille S — puissance exacte de `coelev_comptage` (seuil exact sous P₀ ; R6)", "",
          "| config | m | m/K | seuil (c, γ) | puissance exacte | erreur certifiée | bande de Bonferroni (v1) | HS.4 |",
          "|---|---|---|---|---|---|---|---|"]
for cfg, (K, T, ms) in MS.items():
    s = BS.seuil_coelev_exact(K, T, Q, ALPHA)
    for m in ms:
        v, e = BS2.puissance_exacte(K, T, m, Q, s)
        lb, ub = BS.bornes_puissance(K, T, m, Q, s)
        dessus = lb >= ALPHA + 0.02
        if dessus:
            preds.append({"pred": "HS.4", "cellule": f"S/{cfg}/T_synchro_m{m}", "alarme": "coelev_comptage",
                          "sens": "au_dessus", "discriminante": False})
        for a in ("e_coelev_cal", "ed_coelev"):
            preds.append({"pred": "HS.5", "cellule": f"S/{cfg}/T_synchro_m{m}", "alarme": a,
                          "sens": "en_dessous" if m == K else "au_plus", "discriminante": False})
        table.append(f"| {cfg} | {m} | {m / K:.1f} | ({s[0]:.0f} ; {s[1]:.4f}) | {v:.5f} | {e:.0e} | "
                     f"[{lb:.4f} ; {ub:.4f}] | {'au-dessus' if dessus else '—'} |")

table += ["", "### Famille Q — borne basse exacte de `coelev_comptage` sous équicorrélation (e10x20, seuil exact)", "",
          "| loi | m | seuil exact (c, γ) | borne basse | HQ.4 |", "|---|---|---|---|---|"]
for nom, (c, ms) in Q_LOIS.items():
    s = BS.seuil_coelev_correle_exact(10, 20, c, Q, ALPHA)
    for m in ms:
        lb = BS.borne_synchro_correlee(10, 20, m, c, Q, s)
        tag = f"Q/e10x20/{nom}/T_synchro_m{m}"
        dessus = lb >= ALPHA + 0.02
        if dessus:
            preds.append({"pred": "HQ.4", "cellule": tag, "alarme": "coelev_comptage", "sens": "au_dessus",
                          "discriminante": False})
        if nom == "c0.3" and m in (3, 5):
            for a in ("coelev_comptage", "pas_moyenne"):
                preds.append({"pred": "HQ.5", "cellule": tag, "alarme": a, "sens": "en_dessous",
                              "discriminante": a == "coelev_comptage" or m >= 5})
        if (nom, m) in (("c0.4", 5), ("c0.3", 5)):
            for a in ("e_coelev", "ed_coelev"):
                preds.append({"pred": "HQ.6" if nom == "c0.4" else "HQ.7", "cellule": tag, "alarme": a,
                              "sens": "au_dessus", "discriminante": nom == "c0.3"})
        table.append(f"| {nom} | {m} | ({s[0]:.0f} ; {s[1]:.4f}) | {lb:.4f} | {'au-dessus' if dessus else '—'} |")

table += ["", "### Famille P — modèle de substitution (v_mod) et prédictions (≠ : discriminante)", "",
          "| sonde | m | pas_moyenne | coelev_comptage | e_coelev | ed_coelev | prédictions |", "|---|---|---|---|---|---|---|"]
for sonde in SONDES:
    for m in MP:
        v = dict(zip(("pas_moyenne", "coelev_comptage", "e_coelev", "ed_coelev"), V_MOD[sonde][m]))
        tag = f"P/{sonde}/T_synchro_m{m}"
        faites = []
        for a, x in v.items():
            sens = "au_dessus" if x >= ALPHA + 0.015 else "en_dessous" if x <= ALPHA - 0.015 else None
            if not sens:
                continue
            if a in ("pas_moyenne", "coelev_comptage"):
                pred = "HP.5a" if (sonde == ENJEUX and sens == "en_dessous") else "HP.5b"
            else:
                pred = "HP.6"
            d = discriminante_p(a, m, sens)
            preds.append({"pred": pred, "cellule": tag, "alarme": a, "sens": sens, "discriminante": d})
            faites.append(f"{pred} {a} {sens.replace('_', '-')}{' ≠' if d else ''}")
        if m == K_P:
            lo = math.floor(100 * (v["coelev_comptage"] - 0.15)) / 100
            hi = math.ceil(100 * (v["coelev_comptage"] + 0.15)) / 100
            # loi de référence (e10x10, m = K) : 0,9285 > hi → la cellule départage le modèle de la loi de référence
            preds.append({"pred": "HP.4", "cellule": tag, "alarme": "coelev_comptage", "sens": "entre_x",
                          "valeur_bas": lo, "valeur_haut": hi, "discriminante": True})
            faites.append(f"HP.4 coelev_comptage ∈ ]{lo} ; {hi}[ ≠")
        table.append(f"| {sonde} | {m} | {v['pas_moyenne']} | {v['coelev_comptage']} | {v['e_coelev']} | {v['ed_coelev']} | "
                     f"{' ; '.join(faites) or '—'} |")

grille = {
    "version": "essaim-hors-echantillon-grille-v1 (brouillon 2)",
    "preenregistrement": "prereg/essaim-hors-echantillon-v1.md",
    "graine_racine": "entier des 128 premiers bits du sha256 du préenregistrement scellé (run_essaim.entropie_depuis_prereg)",
    "alpha": ALPHA, "q": Q, "fractions_lambda": [0.1, 0.25, 0.5, 0.75],
    "tailles": {"R": 20000, "R_cal": 100000, "R0": 100000, "equivalence": 200},
    "replication": {"facteur_R": 5}, "lecture": {"gamma": 1e-05},
    "configs": configs,
    "S": {cfg: [synchro(m) for m in ms] for cfg, (_, _, ms) in MS.items()},
    "Q": {"configs": ["e10x20"], "alarmes": ALARMES_LOI,
          "lois": [{"nom": n, "loi": {"type": "equicorrelation", "c": c}, "arrangements": [f"T_synchro_m{m}" for m in ms]}
                   for n, (c, ms) in Q_LOIS.items()],
          "arrangements": [synchro(m) for m in (3, 5, 7, 10)]},
    "P": {"K": K_P, "T": 10, "donnees": {"chemin": CHEMIN, "sha256": SHA256}, "sondes": list(SONDES),
          "alarmes": ALARMES_LOI, "arrangements": [synchro(m) for m in MP],
          "conforme": {"K": 1000, "n_test": 400, "L": 50, "statistiques": ["coelev_comptage", "e_coelev", "agent_moyenne"]}},
    "descriptif_maxima": {"R": 20000},
    "predictions": preds,
}
(ICI / "grille-essaim-hors-echantillon-v1-brouillon2.json").write_text(
    json.dumps(grille, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
(ICI / "tables-valeurs-predites-v2.md").write_text("\n".join(table) + "\n", encoding="utf-8")
print(Counter(p["pred"] for p in preds), "discriminantes :", sum(p["discriminante"] for p in preds))
print("\n".join(table))
