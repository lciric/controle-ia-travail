"""Banc du générateur v2 **en parties** (après deux redémarrages du conteneur) : une partie = un monde de développement
(graine publique 2000 + rang), un seul processus, vérificateur v2 complet (C8 à 200 graines) ; ou la partie « fréquences »
(4 000 gabarits tirés). Chaque partie écrit sa sortie, que l'opérateur scelle aussitôt ; `--resume` agrège les parties
présentes. Mêmes calculs que `banc_generateur_v2.py` (fonction `un`, scellé `4717cc96…`), sans pool de processus.
Usage : `python3 -I -B banc_generateur_v2_partie.py monde RANG SORTIE.json` | `frequences SORTIE.json` |
`resume DOSSIER SORTIE.json`."""
import collections, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import banc_generateur_v2 as B
import generateur_mondes_v2 as G

if __name__ == "__main__":
    cmd = sys.argv[1]
    out = sys.argv[-1]
    if os.path.exists(out):
        sys.exit("refus : sortie existante")
    if cmd == "monde":
        r = B.un(int(sys.argv[2]))
    elif cmd == "frequences":
        freq, lat = collections.Counter(), 0
        for s in range(4000):
            gab, l = G.tirer_gabarit_v2(np.random.default_rng(np.random.SeedSequence(990000 + s)))
            freq.update(f"{c}|{t}" for c, t in gab)
            lat += l
        r = {"frequences_sortes_sur_4000_gabarits": dict(sorted(freq.items())), "latents_sur_4000": lat}
    else:
        parts = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(sys.argv[2], "banc-generateur-v2-monde-*.json")))]
        et = collections.Counter((v["classe"], v["etiquette"].split(" (")[0]) for m in parts if m["conforme"] for v in m["c8"].values())
        r = {"mondes": len(parts), "conformes": sum(m["conforme"] for m in parts),
             "tirages_refuses_par_controle": dict(collections.Counter(c for m in parts for c in m["refus"])),
             "etiquettes_c8": {f"{c}|{e}": k for (c, e), k in sorted(et.items())},
             "composantes_par_monde": [len(m.get("gabarit", [])) for m in parts],
             "latents": sum(1 for m in parts if m["conforme"] and any(t == "latent" for _, t in m["gabarit"]))}
    with open(out, "x", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(r, ensure_ascii=False)[:2000])
