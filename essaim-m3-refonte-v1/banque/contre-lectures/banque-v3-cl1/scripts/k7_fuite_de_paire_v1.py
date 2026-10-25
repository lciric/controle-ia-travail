"""Contre-lecture banque v3 — k7 : une fuite de paire (« dans chaque paire de délégation, le plus petit numéro est le
sabotage », avec probabilité q) sur des banques tirées comme le constructeur ; taux de refus du contrôle v2 (statistique
fidèle de k3, seuils du rapport v3). Usage : python3 -I k7_fuite_de_paire_v1.py BANQUE_DIR N"""
import importlib.util, json, pathlib, sys
import numpy as np
B, N = pathlib.Path(sys.argv[1]), int(sys.argv[2])
sys.argv = [sys.argv[0], str(B), "/nonexistent", "0", "0"]
src = pathlib.Path(__file__).with_name("k3_controle_v2_v1.py").read_text(encoding="utf-8").split("# 0. Cohérence avec le rapport")[0]
ns = {}
exec(compile(src, "k3_prefixe", "exec"), ns)
v1, s1, SEUIL, PARTS = ns["v1"], json.loads((B / "banque-confrontation-v1-secret.json").read_text(encoding="utf-8")), ns["SEUIL"], ns["PARTS"]
ordre = [(p, dict(t, _g=s1[t["id"]]["groupe"])) for p in PARTS for t in v1[p]]
rng = np.random.default_rng(np.random.SeedSequence(2026102571))
for q in (1.0, 0.9, 0.8):
    ref, ref_tf, ref_te = [], [], []
    for _ in range(N):
        bb = ns["tirage"](rng, ordre)
        for p in PARTS:
            g = {}
            for t in bb[p]:
                if t["famille"] == "controle-delegation":
                    g.setdefault(t["_g"], []).append(t)
            for a, c in g.values():
                sab, hon = (a, c) if a["verite"] == "sabotage" else (c, a)
                veut_bas = rng.random() < q
                if (ns["num"](sab["id"]) > ns["num"](hon["id"])) == veut_bas:
                    sab["id"], hon["id"] = hon["id"], sab["id"]
            bb[p].sort(key=lambda x: x["id"])
        st = ns["stats"](bb)
        ref.append(any(st[c] >= SEUIL[c] - 1e-12 for c in SEUIL))
    print(f"fuite de paire q={q:.1f} : refusée dans {np.mean(ref):.3f} de {N} banques ; passe dans {1 - np.mean(ref):.3f} (règle de paire attendue ≈ {q:.1f} sur chaque part)")
