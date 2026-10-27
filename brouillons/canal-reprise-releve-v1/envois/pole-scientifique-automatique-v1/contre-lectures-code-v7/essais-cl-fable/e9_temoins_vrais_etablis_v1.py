"""E9 : les cinq témoins vrais de la banque v2 sont déclarés sur la partie de calibrage par |rang de Spearman| ≥ 0,35
(proposeur scripté). Valeur p de permutation de chaque corrélation déclarée (10 000 permutations), nombre de couples
(moniteur, trait) essayés, nombre attendu de déclarations sous le nul, et — lecture d'audit seulement — le rang sur la
partie d'épreuve pour le même couple. Lecture seule ; aucune donnée n'est réinjectée dans le pôle.

Usage : python -I -B e9_temoins_vrais_etablis_v1.py COPIE_DU_CODE SORTIE.json
"""
import json
import os
import random
import sys

COPIE, SORTIE = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(COPIE, "exemples"))
import proposeur_scripte_banque_v1 as ps  # noqa: E402

with open(os.path.join(COPIE, "exemples", "banque-t05-v2.json"), encoding="utf-8") as f:
    banque = json.load(f)
rng = random.Random(99)
traits = banque["traits"]
essais, declares, nuls_declares = 0, [], 0
for nom, m in sorted(banque["moniteurs"].items()):
    calib = [l for l in banque["instances"] if l["partie"] == "calibrage" and nom in l["issues"]]
    ep = [l for l in banque["instances"] if l["partie"] == "epreuve" and nom in l["issues"]]
    for j, t in enumerate(traits):
        if t == "bruit":
            continue
        essais += 1
        xs, ys = [l["z"][j] for l in calib], [l["issues"][nom] for l in calib]
        rho = ps._correlation_rang(xs, ys)
        # probabilité, sous le nul (issues permutées), qu'un couple soit déclaré : |rho| ≥ 0,35
        perm = []
        for _ in range(2000):
            yp = ys[:]
            rng.shuffle(yp)
            perm.append(abs(ps._correlation_rang(xs, yp)))
        nuls_declares += sum(p >= ps.SEUIL_TEMOIN_VRAI for p in perm) / len(perm)
        if abs(rho) >= ps.SEUIL_TEMOIN_VRAI:
            plus = [abs(ps._correlation_rang(xs, rng.sample(ys, len(ys)))) for _ in range(10000)]
            p = (1 + sum(v >= abs(rho) for v in plus)) / (1 + len(plus))
            rho_ep = ps._correlation_rang([l["z"][j] for l in ep], [l["issues"][nom] for l in ep])
            declares.append({"moniteur": nom, "trait": t, "n_calibrage": len(calib),
                             "effectifs_calibrage": [ys.count(c) for c in range(m["nombre_issues"])],
                             "rho_calibrage": round(rho, 3), "p_permutation_bilaterale": round(p, 4),
                             "rho_epreuve_meme_sens": round(rho_ep, 3) * (1 if rho > 0 else -1)})
resultat = {"couples_essayes": essais, "declarations_attendues_sous_le_nul": round(nuls_declares, 2),
            "temoins_vrais_declares": declares,
            "significatifs_a_5_pour_cent_sans_correction": sum(d["p_permutation_bilaterale"] < 0.05 for d in declares),
            "significatifs_apres_bonferroni_sur_les_couples_essayes": sum(d["p_permutation_bilaterale"] < 0.05 / essais
                                                                          for d in declares)}
with open(SORTIE, "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
