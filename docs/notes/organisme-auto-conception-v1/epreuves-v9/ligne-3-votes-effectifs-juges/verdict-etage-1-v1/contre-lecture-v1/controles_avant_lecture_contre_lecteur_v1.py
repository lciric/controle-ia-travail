"""Controles avant lecture, etage 1 de la ligne 3 -- programme du contre-lecteur (modele F).

Ne lit des mesures que ce que demandent les controles :
  K0a  melange plante de l'alarme (A2 l. 104) : 1000, 500, 500, 1000 par cellule ;
  K0b  P2 (PR l. 134, l. 316) : ecart maximal d'erreur equilibree entre les quatre
       regles S_1, S_2, U, F, a deux juges egaux et symetriques, dans +/- 0,02 ;
  K0c  part d'abstentions par vote a delta = 0 a 0,02 au plus de 0,1275 (PR l. 326).
Rend aussi l'inventaire des etiquettes de la grille (noms de cles, valeurs des
parametres plantes : J, loi, profil, n, rho...), sans aucune mesure.

Usage : python3 controles_avant_lecture_contre_lecteur_v1.py MESURES.json SORTIE.json
"""
import hashlib
import json
import os
import sys

EPS = 1e-12


def sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def taux_du_profil_egal(profil):
    """Rend le taux si le profil est 'egal_x', sinon None."""
    if not profil.startswith("egal_"):
        return None
    return float(profil[len("egal_"):])


def main():
    mesures, sortie = sys.argv[1], sys.argv[2]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe deja")
    with open(mesures, encoding="utf-8") as f:
        d = json.load(f)
    r = {"programme": os.path.basename(__file__), "mesures_sha256": sha256(mesures)}

    # ---- K0a
    k0a = []
    for c in d["alarme"]:
        m = c["comptes_du_melange_plante"]
        vu = [m["suites_qui_changent"], m["suites_a_effet"], m["suites_sans_effet"],
              m["suites_sans_changement"]]
        k0a.append({"m": c["m"], "suites": c["suites"], "vu": vu,
                    "attendu": [1000, 500, 500, 1000],
                    "conforme": vu == [1000, 500, 500, 1000] and c["suites"] == 2000})
    r["K0a_melange_plante"] = {
        "cellules": k0a,
        "m_joues": sorted(x["m"] for x in k0a),
        "tient": all(x["conforme"] for x in k0a) and sorted(x["m"] for x in k0a) == [10, 20, 40]}

    # ---- K0b
    regles = ["S_1", "S_2", "U", "F_au_moins_un"]
    n_cell, pire, hors_002, hors_001, desaccord_champ = 0, None, [], 0, 0
    par_profil = {}
    for c in d["estimateur_et_agregation"]:
        if c["J"] != 2 or taux_du_profil_egal(c["profil"]) is None:
            continue
        ee = [c["bras"][k]["erreur_equilibree"] for k in regles]
        ecart = max(ee) - min(ee)
        n_cell += 1
        ident = {"loi": c["loi"], "profil": c["profil"], "rho": c["rho_grille"], "n": c["n"],
                 "ecart_maximal": ecart, "repliques": c["repliques"]}
        if pire is None or ecart > pire["ecart_maximal"]:
            pire = ident
        if ecart > 0.02 + EPS:
            hors_002.append(ident)
        if ecart > 0.01 + EPS:
            hors_001 += 1
        champ = c.get("theorie_p2", {}).get("ecart_maximal")
        if champ is None or abs(champ - ecart) > 1e-9:
            desaccord_champ += 1
        p = par_profil.setdefault(c["profil"], {"cellules": 0, "ecart_maximal": 0.0})
        p["cellules"] += 1
        p["ecart_maximal"] = max(p["ecart_maximal"], ecart)
    r["K0b_P2"] = {"cellules_lues": n_cell, "pire_cellule": pire,
                   "cellules_hors_0.02": hors_002, "nombre_hors_0.01_prediction": hors_001,
                   "par_profil": par_profil,
                   "cellules_ou_le_champ_theorie_p2_differe_de_mon_calcul": desaccord_champ,
                   "tient": n_cell > 0 and not hors_002}

    # ---- K0c
    k0c, pire_c = [], 0.0
    for c in d["double_rendu"]:
        if abs(c["delta"]) > EPS:
            continue
        for loi, v in c["par_loi"].items():
            a = v["moyennes"]["abstention_par_vote"]
            e = abs(a - 0.1275)
            pire_c = max(pire_c, e)
            if e > 0.02 + EPS:
                k0c.append({"n": c["n"], "s": c["s"], "loi": loi, "abstention_par_vote": a})
    r["K0c_abstentions_delta_0"] = {"pire_ecart_a_0.1275": pire_c, "cellules_hors_0.02": k0c,
                                    "tient": not k0c}

    # ---- inventaire des etiquettes (aucune mesure)
    ea = d["estimateur_et_agregation"]
    inv = {
        "estimateur_et_agregation": {
            "cellules": len(ea),
            "J": sorted({c["J"] for c in ea}),
            "lois_par_J": {str(J): sorted({c["loi"] for c in ea if c["J"] == J})
                           for J in sorted({c["J"] for c in ea})},
            "profils_par_J_loi": {f"{J}|{L}": sorted({c["profil"] for c in ea
                                                      if c["J"] == J and c["loi"] == L})
                                  for J, L in sorted({(c["J"], c["loi"]) for c in ea})},
            "n": sorted({c["n"] for c in ea}),
            "rho_par_loi": {str(L): sorted({c["rho_grille"] for c in ea if c["loi"] == L})
                            for L in sorted({c["loi"] for c in ea})},
            "repliques": sorted({c["repliques"] for c in ea}),
            "cles_des_bras_par_J": {str(J): sorted({k for c in ea if c["J"] == J
                                                    for k in c["bras"]})
                                    for J in sorted({c["J"] for c in ea})},
            "cles_de_cellule_par_J": {str(J): sorted({k for c in ea if c["J"] == J for k in c})
                                      for J in sorted({c["J"] for c in ea})},
            "cles_comparaisons_par_J": {str(J): sorted({k for c in ea if c["J"] == J
                                                        for k in c.get("comparaisons", {})})
                                        for J in sorted({c["J"] for c in ea})},
        },
        "monde_de_puissance": {
            "cellules": len(d["monde_de_puissance"]),
            "comparaisons": sorted({c["comparaison"] for c in d["monde_de_puissance"]}),
            "ecarts_vises": sorted({c["ecart_vise"] for c in d["monde_de_puissance"]}),
            "lois": sorted({c["loi"] for c in d["monde_de_puissance"]}),
            "cles": sorted({k for c in d["monde_de_puissance"] for k in c}),
            "repliques": sorted({str(c.get("repliques")) for c in d["monde_de_puissance"]}),
        },
        "ecart_rho_prime_moins_rho": {
            "cellules": len(d["ecart_rho_prime_moins_rho"]),
            "cles": sorted({k for c in d["ecart_rho_prime_moins_rho"] for k in c}),
        },
        "double_rendu": {
            "cellules": len(d["double_rendu"]),
            "cles": sorted({k for c in d["double_rendu"] for k in c}),
            "n": sorted({c["n"] for c in d["double_rendu"]}),
            "delta": sorted({c["delta"] for c in d["double_rendu"]}),
            "s": sorted({c["s"] for c in d["double_rendu"]}),
            "lois": sorted({k for c in d["double_rendu"] for k in c["par_loi"]}),
            "cles_par_loi": sorted({k for c in d["double_rendu"] for v in c["par_loi"].values()
                                    for k in v}),
            "cles_moyennes": sorted({k for c in d["double_rendu"] for v in c["par_loi"].values()
                                     for k in v["moyennes"]}),
        },
        "garde_de_cadrage": {
            "cellules": [{"delta": c["delta"], "s": c["s"], "t": c["t"],
                          "repliques": c["repliques"]} for c in d["garde_de_cadrage"]],
        },
        "mode": d.get("mode"), "version": d.get("version"),
    }
    r["inventaire_des_etiquettes"] = inv
    r["controles_tous_tenus"] = bool(r["K0a_melange_plante"]["tient"] and r["K0b_P2"]["tient"]
                                     and r["K0c_abstentions_delta_0"]["tient"])
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print("ecrit :", sortie)


if __name__ == "__main__":
    main()
