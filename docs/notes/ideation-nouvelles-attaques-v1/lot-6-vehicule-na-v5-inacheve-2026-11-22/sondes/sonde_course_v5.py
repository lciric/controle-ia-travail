import sys, os, traceback, json
sys.path.insert(0, os.path.join(sys.argv[1], "essais")); sys.path.insert(0, sys.argv[1])
import aides_na_lot6_v5 as H
m = H.MontageV5()
try:
    b = m.lancer()
    print("générations", len(b))
    for l in b:
        print(json.dumps(l["comptes_registre_v4"]["m6"], ensure_ascii=False)[:400])
        print("coffre", l["coffre"])
except Exception:
    traceback.print_exc(limit=6)
    print(m.arrets() if os.path.exists(m.chemin_sortie("journal-arrets-et-generations-na-v5.jsonl.sha256")) else "pas de journal")
