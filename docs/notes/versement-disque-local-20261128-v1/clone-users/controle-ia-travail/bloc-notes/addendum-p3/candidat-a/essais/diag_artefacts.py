import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "..")
import test_complements_p3_v1 as T
A = T.A; lp = T.lp
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000
A.TIRAGES_AIRE, A.TIRAGES_COUT = 200, 1000
for nom, f in T.ARTEFACTS.items():
    src, lec, analyse, p, att = f()
    e = T._une(src, lec, analyse, p)
    print("==", nom, att)
    for r in e["reserves"]:
        print("   ", r["reserve"], "|", r["conclusion"], "|", r["controle"], "|", r["motif"])
    if nom == "A4-tache":
        c = e["descriptif"]["controles"]
        print("   intra", c["T1_intra_tache"].get("aire"), c["T1_intra_tache"].get("plancher_quantile"), "log", c["T1_reference_log_moyenne"].get("au_dessus_du_plancher"), c["T1_reference_log_moyenne"].get("bas"), "lecture T1", lec["intention"][T.P[0]]["T1"]["etabli"], lec["intention"][T.P[0]]["T1"]["aire"])
