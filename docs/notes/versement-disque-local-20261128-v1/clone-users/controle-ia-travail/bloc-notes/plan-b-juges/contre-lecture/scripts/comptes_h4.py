import json, sys, statistics as st
racine = sys.argv[1]
d = racine + "/diag/20261017-193648-t05-notations-reel/"
for juge in ("8B", "3B"):
    brut = json.load(open(d + f"notations-{juge}-decisives.json", encoding="utf-8"))
    res = brut["resultat"]
    ns = res["notations"]
    # n'utiliser que des champs numériques et des drapeaux
    ctx = [n["jetons_contexte"] for n in ns]
    rep = [n["jetons_reponse"] for n in ns]
    tr = [bool(n["tronquee"]) for n in ns]
    lots = [ns[k:k+8] for k in range(0, len(ns), 8)]
    lots_tr = [i+1 for i, l in enumerate(lots) if any(n["tronquee"] for n in l)]
    lots8_tr = [i+1 for i, l in enumerate(lots) if len(l) == 8 and any(n["tronquee"] for n in l)]
    tr_par_lot = {i+1: sum(n["tronquee"] for n in l) for i, l in enumerate(lots)}
    pos = [c + r for c, r in zip(ctx, rep)]
    print(f"juge {juge}: notations {len(ns)} ; lots {len(lots)} (tailles {sorted({len(l) for l in lots})})")
    print(f"  contexte min {min(ctx)} max {max(ctx)} médiane {st.median(ctx)}")
    print(f"  réponse médiane {st.median(rep)} ; tronquées {sum(tr)} ; longueurs tronquées {sorted({r for r,t in zip(rep,tr) if t})}")
    print(f"  positions max {max(pos)} ; lots avec tronquée {len(lots_tr)} : {lots_tr}")
    print(f"  lots de 8 avec tronquée : {len(lots8_tr)}")
    print(f"  tronquées par lot (lots de 8 du cadre) : {[tr_par_lot[i] for i in lots8_tr]}")
    print(f"  incomplètes {sum(1 for n in ns if n['score'] is None)} ; scores non nuls {sum(1 for n in ns if n['score'] is not None)}")
    # premières clés de lot pour vérifier l'ordre
    print("  champs d'une notation :", sorted(ns[0].keys()))
    print("  descriptifs :", {k: v for k, v in res.get("descriptifs", {}).items()})
