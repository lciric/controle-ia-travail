"""Inventaire des valeurs distinctes des clés d'indexation du résultat, sans
ouvrir le bloc `criteres_mecaniques` (l'aide).
Usage : python3 -I -B explorer_resultat_v1.py RESULTAT.json SORTIE.txt
"""
import json
import sys
from collections import Counter


def distinctes(liste, cles):
    out = {}
    for c in cles:
        out[c] = sorted({repr(e.get(c)) for e in liste})
    return out


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    data.pop("criteres_mecaniques", None)
    L = []
    ea = data["estimateur_et_agregation"]
    L.append("estimateur_et_agregation: " + json.dumps(distinctes(ea, ["J", "loi", "profil", "n", "rho_grille", "repliques"]), ensure_ascii=False))
    combos = Counter((e["J"], e["loi"], e["profil"]) for e in ea)
    for k, v in sorted(combos.items(), key=lambda x: repr(x)):
        L.append(f"  J,loi,profil={k}: {v} cellules")
    j5 = [e for e in ea if e["J"] == 5]
    if j5:
        L.append("  clés bras J=5: " + ", ".join(sorted(j5[0]["bras"].keys())))
        L.append("  clés comparaisons J=5: " + ", ".join(sorted(j5[0]["comparaisons"].keys())))
        L.append("  clés cellule J=5: " + ", ".join(sorted(j5[0].keys())))
        L.append("  bras_N J=5 exemple: " + repr(j5[0].get("bras_N"))[:300])
        L.append("  mot fa38 J=5 exemple: " + repr(j5[0].get("mot_fa38f9faa24e0_par_rho_prime")))
    L.append("  clés cellule J=2: " + ", ".join(sorted(ea[0].keys())))
    L.append("  note racine: " + data.get("note", ""))
    mp = data["monde_de_puissance"]
    L.append("monde_de_puissance: " + json.dumps(distinctes(mp, ["comparaison", "loi", "ecart_vise", "rho", "rho_prime", "faisable", "repliques"]), ensure_ascii=False))
    L.append("  clés: " + ", ".join(sorted(mp[0].keys())))
    inf = [e for e in mp if not e["faisable"]]
    L.append("  exemple infaisable: " + json.dumps(inf[0], ensure_ascii=False)[:600] if inf else "  aucun infaisable")
    er = data["ecart_rho_prime_moins_rho"]
    L.append("ecart_rho_prime_moins_rho: " + json.dumps(distinctes(er, ["ecart_vise", "rho", "faisable", "n", "taux"]), ensure_ascii=False))
    dr = data["double_rendu"]
    L.append("double_rendu: " + json.dumps(distinctes(dr, ["delta", "n", "s", "repliques"]), ensure_ascii=False))
    ex = [e for e in dr if e["s"] == 0.5 and e["delta"] == 0.5][0]
    L.append("  exemple s=0,5 delta=0,5 n=" + str(ex["n"]) + " suiveur_seduisant: " + json.dumps(ex["par_loi"]["suiveur_seduisant"], ensure_ascii=False)[:3000])
    gc = data["garde_de_cadrage"]
    L.append("garde_de_cadrage: " + json.dumps(distinctes(gc, ["delta", "s", "t", "repliques"]), ensure_ascii=False))
    for e in data["alarme"]:
        L.append(f"alarme m={e['m']} melange={e['comptes_du_melange_plante']} suites={e['suites']}")
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
