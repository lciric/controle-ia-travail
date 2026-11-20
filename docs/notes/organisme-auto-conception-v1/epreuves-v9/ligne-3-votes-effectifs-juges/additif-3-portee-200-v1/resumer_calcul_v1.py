"""Résumé lisible de calcul-contre-lecture-additif-3-v1.json. Usage : python3 resumer_calcul_v1.py JSON"""
import json
import sys

d = json.load(open(sys.argv[1], encoding="utf-8"))
print("ligne_go", d["ligne_go"])
print("cellules", d["cellules"], "faisables", d["faisables_par_ecart"])
for c in d["faisables_a_0_10"]:
    print("  faisable 0,10 :", c["comparaison"], "loi", c["loi"], "rho", c["rho"], "rho'", c["rho_prime"], "d=%.4f" % c["d"])
for n in ("100", "200"):
    a = d["puissance_approchee"][n]
    print(f"n={n} : plus basse, borne basse {a['plus_basse_borne_basse']:.3f}, borne haute {a['plus_basse_borne_haute']:.3f}")
    for l in a["cellules"]:
        rc = {k: round(v, 3) for k, v in l["regle_c"].items()}
        f = l["si_c_vaut_au_moins_un"]
        print(f"  {l['comparaison'][:10]:10s} {l['bras']:2s} loi {l['loi']} rho {l['rho']:.2f} rho' {l['rho_prime']:.1f} "
              f"d={l['d']:.4f} bornes [{l['borne_basse']:.3f} ; {l['borne_haute']:.3f}] "
              f"si C=F [{f['bas']:.3f} ; {f['haut']:.3f}] ecart {f['ecart_moyen']:.3f} et {f['ecart_type']:.4f} ; regle C {rc}")
print(json.dumps(d["compteur"], indent=1, sort_keys=True))
