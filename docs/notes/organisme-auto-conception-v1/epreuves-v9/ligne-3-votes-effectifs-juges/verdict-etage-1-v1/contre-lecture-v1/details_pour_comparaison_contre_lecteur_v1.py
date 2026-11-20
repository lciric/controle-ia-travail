"""Details chiffres pour comparer mon rejeu au texte du verdict, champ par champ.

Contre-lecteur, modele F. Lit les mesures et mon rejeu ; n'ecrit qu'un texte court.
Usage : python3 details_pour_comparaison_contre_lecteur_v1.py MESURES.json REJEU.json SORTIE.txt
"""
import json
import os
import sys


def main():
    mesures, rejeu, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe deja")
    with open(mesures, encoding="utf-8") as f:
        d = json.load(f)
    with open(rejeu, encoding="utf-8") as f:
        r = json.load(f)
    L = []
    L.append("== cellules de la regle (J=2, egal_0.2, lois 1 et 3) : eqm, biais, couverture, indefini")
    for n in (50, 100, 200, 400):
        cs = [c for c in d["estimateur_et_agregation"]
              if c["J"] == 2 and c["profil"] == "egal_0.2" and c["loi"] in (1, 3) and c["n"] == n]
        cs.sort(key=lambda c: (c["loi"], c["rho_grille"]))
        for c in cs:
            e = c["estimateur"]
            L.append(f'n={n} loi={c["loi"]} rho={c["rho_grille"]}: eqm={e["eqm"]!r} '
                     f'biais={e["biais"]:.5f} couv={e["couverture"]:.4f} indef={e["part_indefini"]}')
        L.append(f'  n={n} : eqm de {min(c["estimateur"]["eqm"] for c in cs):.4f} a '
                 f'{max(c["estimateur"]["eqm"] for c in cs):.4f} ; couverture de '
                 f'{min(c["estimateur"]["couverture"] for c in cs):.4f} a '
                 f'{max(c["estimateur"]["couverture"] for c in cs):.4f} ; indefini max '
                 f'{max(c["estimateur"]["part_indefini"] for c in cs)} ; |biais| max '
                 f'{max(abs(c["estimateur"]["biais"]) for c in cs):.5f}')
    L.append("== monde de puissance, ecart 0,10, cellules faisables")
    for x in sorted(r["regle_de_portee"]["par_ecart"]["0.1"]["puissances"],
                    key=lambda x: (x["comparaison"], x["loi"], x["rho"], x["rho_prime"] or 0)):
        L.append(f'{x["comparaison"]} loi={x["loi"]} rho={x["rho"]} rho_prime={x["rho_prime"]} '
                 f'd={x["d"]:.5f} ecart_vrai={x["ecart_vrai_formule"]!r} puissance={x["puissance"]} '
                 f'repliques={x["repliques"]}')
    hors_r = sorted({str(c.get("rho_prime")) for c in d["monde_de_puissance"]
                     if c["comparaison"] != "juge_repete_trois_votes_majorite"})
    L.append(f"rho_prime hors du monde plante pour le bras R (toutes cellules) : {hors_r}")
    L.append(f'ecart 0,05 : plus basse {r["regle_de_portee"]["par_ecart"]["0.05"]["plus_basse"]} ; '
             f'ecart 0,15 : plus basse {r["regle_de_portee"]["par_ecart"]["0.15"]["plus_basse"]}')
    L.append("== branche (2) : cellules refutees a 200 temoins d'etalonnage (n = 400)")
    for c in d["estimateur_et_agregation"]:
        if c["J"] == 5 and c["loi"] in (1, 4) and c["n"] == 400:
            e = c["bras"]["C"]["erreur_equilibree"] - c["bras"]["poids_egaux"]["erreur_equilibree"]
            if e > 0.02:
                L.append(f'loi={c["loi"]} profil={c["profil"]} rho={c["rho_grille"]} ecart={e:.5f}')
    L.append("== branche (3) : mots")
    for k, v in r["fefca_branche_3"]["par_loi_t_c"].items():
        L.append(f'{k}: saine={v["part_saine"]} d0.2={v["part_delta_0.2"]} '
                 f'd0.5={v["part_delta_0.5"]} mot={v["mot"]}')
    L.append("== rho' - rho : puissances « des deux »")
    for ev, g in r["puissance_positif_rho_prime_moins_rho"]["par_ecart"].items():
        L.append(f'ecart {ev} : {g["faisables"]} faisables ; {g["les_deux"]}')
    L.append("== double rendu, mots des lois (b) et (c) calcules par moi (rapportes sans mot)")
    comptes = {}
    for x in r["fcfa3d98b90f8"]["toutes_les_lois"]:
        k = (x["loi"], x["delta"], x["s"])
        comptes.setdefault(k, set()).add((x["clause_i"], x["clause_iii"], x["mot"]))
    for k in sorted(comptes):
        L.append(f"{k}: {sorted(comptes[k])}")
    aide_des = sum(1 for x in r["fcfa3d98b90f8"]["toutes_les_lois"]
                   if x["loi"] == "suiveur_seduisant")
    L.append(f"lignes suiveur_seduisant : {aide_des}")
    with open(sortie, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("ecrit :", sortie)


if __name__ == "__main__":
    main()
