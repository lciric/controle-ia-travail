"""Résumé de la sortie du passage « instrument planté pour la branche à contexte réécrit » : lignes du point situé,
moyennes par lecture et par zone, erreurs. Ne recalcule rien d'aléatoire."""
import sys
from collections import defaultdict
L = open(sys.argv[1]).read().split("\n")
print(L[0]); print(L[1])
iD = next(i for i, l in enumerate(L) if l.startswith("# D."))
ent = L[iD + 1].split("\t")
rows = []
for l in L[iD + 2:]:
    if not l or l.startswith("#"):
        break
    v = l.split("\t")
    rows.append(dict(zip(ent, v)))
num = lambda r, k: float(r[k]) if r[k] != "-" else float("nan")
moy = lambda rs, k: sum(num(r, k) for r in rs) / len(rs) if rs else float("nan")
def moy_nan(rs, k):
    x = [num(r, k) for r in rs if r[k] != "-"]
    return (sum(x) / len(x), len(x)) if x else (float("nan"), 0)
cols = [c for c in ent[5:]]
print("\n## Point situe (0.8 ; 0.08 ; 0.9), par lecture et par etat")
for r in rows:
    if (r["s0"], r["s1"], r["ancrage"]) == ("0.8", "0.08", "0.9"):
        print(f"- {r['lecture']} | {r['etat_de_l_oracle_a_contexte_reecrit']}")
        for c in cols:
            print(f"    {c} = {r[c]}")
cles = ["arret_pente_de_fuite_loi_normale(1/80)", "arret_pente_de_fuite_Student_127(1/80)", "arret_centrage_N_quatre_composantes_1/80", "k_H_N", "k_R_N", "k_P_N", "m_R_N", "m_P_N", "conditions_P_remplies",
        "conditions_N_remplies|a_regenere", "conditions_N_remplies|b_plante", "conditions_N_remplies|a_sans_marge", "conditions_N_remplies|b_sans_marge",
        "issue_N|a", "issue_P|a", "ne_part_pas|a", "issue_N|b", "issue_P|b", "ne_part_pas|b", "issue_N|a_sans_marge", "issue_P|a_sans_marge", "issue_N|b_sans_marge", "issue_P|b_sans_marge",
        "N_sous_b:arret_par_une_epreuve", "N_sous_b:bruit_honnete", "N_sous_b:rapport", "N_sous_b:puissance", "N_sous_b:tours"]
ab = [c for c in ent if c.startswith("aboutit")]
for etat in ("sain", "le texte porte un huitieme du niveau (oracle sain)", "fuite d'un quart"):
    print(f"\n## Etat « {etat} » : moyennes par lecture (nombre de cellules)")
    for lec in ("des le moindre ecart", "continue, portee 0,1", "continue, portee 0,3"):
        rs = [r for r in rows if r["lecture"] == lec and r["etat_de_l_oracle_a_contexte_reecrit"] == etat]
        print(f"- {lec} ({len(rs)} cellules)")
        for c in cles:
            print(f"    {c} = {moy(rs, c):.3f}")
        for c in ab:
            m, n = moy_nan(rs, c)
            print(f"    {c} = {m:.2f} (sur {n} cellules ou l'issue se produit)")
print("\n## Etat sain : conditions de N remplies, par lecture, ancrage et dispersion des actions suivantes (moyenne des trois dispersions du premier pas) : a | b | a sans marge | b sans marge ; issue N|b ; issue P|b")
for etat in ("sain", "le texte porte un huitieme du niveau (oracle sain)"):
    print(f"# etat « {etat} »")
    for lec in ("des le moindre ecart", "continue, portee 0,1", "continue, portee 0,3"):
        for rho in ("0.7", "0.9", "1.0"):
            for s1 in ("0.05", "0.08", "0.12"):
                rs = [r for r in rows if r["lecture"] == lec and r["etat_de_l_oracle_a_contexte_reecrit"] == etat and r["ancrage"] == rho and r["s1"] == s1]
                if rs:
                    print(f"  {lec} ; ancrage {rho} ; s1 {s1} ({len(rs)}) : " + " | ".join(f"{moy(rs, c):.3f}" for c in cles[9:13]) + f" ; issue N|b {moy(rs, 'issue_N|b'):.3f} ; issue P|b {moy(rs, 'issue_P|b'):.3f} ; k_H {moy(rs, 'k_H_N'):.2f} k_R {moy(rs, 'k_R_N'):.2f} k_P {moy(rs, 'k_P_N'):.2f} ; aboutit|b,N ancre/demi/plante " + "/".join(f"{moy_nan(rs, c)[0]:.2f}" for c in ("aboutit|b,N,ancre", "aboutit|b,N,demi", "aboutit|b,N,plante")))
print("\n## Erreurs (recopie)")
for l in L:
    if l.startswith("#   variante"):
        print(l)
print("\n## Taux vrais au point situe (bloc A)")
iA = next(i for i, l in enumerate(L) if l.startswith("# A."))
print(L[iA + 1])
for l in L[iA + 2:iD]:
    if l.startswith("0.8\t0.08\t0.9\t"):
        print(l)
