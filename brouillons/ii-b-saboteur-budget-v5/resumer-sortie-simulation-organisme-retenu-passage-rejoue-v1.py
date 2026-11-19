"""Résumé par programme de la sortie du passage rejoué (aucun calcul nouveau : moyennes et étendues de colonnes imprimées)."""
import sys
from collections import defaultdict
L = open(sys.argv[1], encoding="utf-8").read().split("\n")
for l in L:
    if l.startswith(("entropie", "numpy", "# REGLE", "# CLASSEMENT", "#   ", "# ERREURS", "duree")):
        print(l)
blocs, cur = {}, None
for l in L:
    if l.startswith("# B.") or l.startswith("# V.") or l.startswith("# D.") or l.startswith("# E."):
        cur = l[2:4] + (l.split("oracle ")[1].split(" ")[0] if l.startswith("# B.") else "")
        blocs[cur] = []
    elif cur and "\t" in l:
        blocs[cur].append(l.split("\t"))
def table(b):
    ent, lignes = blocs[b][0], blocs[b][1:]
    return [dict(zip(ent, x)) for x in lignes]
def fl(x):
    try:
        return float(x)
    except ValueError:
        return float("nan")
def et(v):
    v = [x for x in v if x == x]
    return f"{min(v):.3f} a {max(v):.3f} (moy {sum(v)/len(v):.3f})" if v else "-"
SIT = ("0.8", "0.08", "0.9", "0.14", "0.0")
cle = lambda r: (r["s0"], r["s1"], r["ancrage"], r["w"], r["part_du_texte"])
for m in ("8", "4", "0"):
    T = table("B." + m)
    print(f"\n== oracle {m} : point situe")
    for r in T:
        if cle(r) == SIT:
            print("   " + " ; ".join(f"{k} {v}" for k, v in r.items()))
    print(f"== oracle {m} : cellules distinguees sur 3 (ancre / demi / plante) a texte nul, par w, dispersion des pas suivants et ancrage ; puis taux moyens h/a/d/p ; ecart type de e honnete ; mesure/vrai a,d,p")
    for w in ("0.0", "0.14", "0.24"):
        for s1 in ("0.05", "0.08", "0.12"):
            bouts = []
            for rho in ("0.7", "0.9", "1.0"):
                rs = [r for r in T if r["w"] == w and r["s1"] == s1 and r["ancrage"] == rho and r["part_du_texte"] == "0.0"]
                mo = lambda k: sum(fl(r[k]) for r in rs) / len(rs)
                bouts.append(f"anc {rho}: {sum(int(r['dist_ancre']) for r in rs)}/{sum(int(r['dist_demi']) for r in rs)}/{sum(int(r['dist_plante']) for r in rs)} "
                             f"[{mo('taux_honnete'):.3f} {mo('taux_ancre'):.3f} {mo('taux_demi'):.3f} {mo('taux_plante'):.3f} | sd {mo('ecart_type_e_honnete'):.2f} | "
                             f"{mo('mesure/vrai_ancre'):.2f} {mo('mesure/vrai_demi'):.2f} {mo('mesure/vrai_plante'):.2f}]")
            print(f"   w {w} s1 {s1} : " + " || ".join(bouts))
    for k in ("vrai_acceptes_ancre", "mesure_acceptes_ancre", "vrai_acceptes_demi", "mesure_acceptes_demi", "vrai_acceptes_plante", "mesure_acceptes_plante",
              "plus_grand_exces_vrai_acceptes_ancre", "plus_grand_exces_vrai_acceptes_demi", "part_deux_plus_grands_ancre", "taux_honnete_sans_ancre_si_regle_appliquee", "taux_honnete"):
        print(f"   {k} : {et([fl(r[k]) for r in T])}")
    print("   texte 0,125, w 0,14 : distinguees sur 27 (ancre/demi/plante) : " + "/".join(str(sum(int(r[k]) for r in T if r["w"] == "0.14" and r["part_du_texte"] == "0.125")) for k in ("dist_ancre", "dist_demi", "dist_plante"))
          + " ; texte 0 : " + "/".join(str(sum(int(r[k]) for r in T if r["w"] == "0.14" and r["part_du_texte"] == "0.0")) for k in ("dist_ancre", "dist_demi", "dist_plante")))
print("\n== controle contre les donnees (V)")
for r in blocs["V."]:
    print("   " + "\t".join(r))
D = table("D.")
cols = [c for c in D[0] if c not in ("s0", "s1", "ancrage", "w", "part_du_texte", "oracle", "borne", "phi", "etat_de_l_oracle")]
for m in sorted({r["oracle"] for r in D}, reverse=True):
    S = [r for r in D if r["oracle"] == m and r["etat_de_l_oracle"] == "sain"]
    print(f"\n== etalonnages, oracle {m}, sain ({len(S)} cellules) : etendue de chaque colonne")
    for c in cols:
        print(f"   {c} : {et([fl(r[c]) for r in S])}")
    print("   point situe : " + " ; ".join(f"{k} {v}" for r in S if cle(r) == SIT for k, v in r.items()))
    print("   part (i)+(ii) par w, dispersion et ancrage (texte nul) ; puis part a garder (moyenne) ; aboutit ancre/demi/plante")
    for w in ("0.0", "0.14", "0.24"):
        for s1 in ("0.05", "0.08", "0.12"):
            bouts = []
            for rho in ("0.7", "0.9", "1.0"):
                rs = [r for r in S if r["w"] == w and r["s1"] == s1 and r["ancrage"] == rho and r["part_du_texte"] == "0.0"]
                mo = lambda k: sum(fl(r[k]) for r in rs if fl(r[k]) == fl(r[k])) / max(1, sum(1 for r in rs if fl(r[k]) == fl(r[k])))
                bouts.append(f"anc {rho}: {mo('part_i') + mo('part_ii'):.2f} [garder {mo('part_de_l_exces_a_garder_pour_etre_vu'):.2f} | {mo('P(aboutit|part,ancre)'):.2f} {mo('P(aboutit|part,demi)'):.2f} {mo('P(aboutit|part,plante)'):.2f} | plante-instr {mo('part_si_instrument_plante'):.2f}]")
            print(f"   w {w} s1 {s1} : " + " || ".join(bouts))
    print(f"== etalonnages, oracle {m}, oracles en defaut (9 cellules) : moyenne (etendue) d'arret par composante, epreuve entiere, sensibilite, rejet, part, k_regenere")
    etats = []
    for r in D:
        if r["oracle"] == m and r["etat_de_l_oracle"] not in etats:
            etats.append(r["etat_de_l_oracle"])
    neuf = {cle(r) for r in D if r["oracle"] == m and r["etat_de_l_oracle"] != "sain"}
    for e in etats:
        rs = [r for r in D if r["oracle"] == m and r["etat_de_l_oracle"] == e and cle(r) in neuf]
        mo = lambda k: sum(fl(r[k]) for r in rs) / len(rs)
        print(f"   {e} : rangs {mo('arret_rangs'):.2f} ; lisibilite {mo('arret_lisibilite'):.2f} ; rangs reecrit {mo('arret_rangs_reecrit'):.2f} ; centrage {mo('arret_centrage'):.3f} "
              f"({min(fl(r['arret_centrage']) for r in rs):.3f} a {max(fl(r['arret_centrage']) for r in rs):.3f}) ; sensibilite {mo('P(sensibilite passe)'):.3f} ; rejet {mo('P(rejet du flagrant passe)'):.3f} ; "
              f"part {mo('part_i') + mo('part_ii'):.3f} ; k_H {mo('k_H_moyen'):.2f} ; k_regenere {mo('k_regenere_moyen'):.2f} ; k_plante {mo('k_plante_moyen'):.2f}")
print("\n== tout dans le premier cout (E)")
for r in blocs["E."]:
    print("   " + "\t".join(r))
