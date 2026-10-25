"""Contre-lecture de la v5 — c4 : essais (règle R5) de `charger_traits` du noyau avec la v5, en mode fichier `.npz`,
sur des traits factices (vecteurs aléatoires, aucun matériau réel) : cas sain (176 identifiants de la v5) ; artefact
« traits de la v3 » (espace t-0001…t-0200) ; artefact « v5 + 24 de trop » (176 + 24 identifiants hors banque).
Usage : python3 -I -B c4_essais_traits_v1.py RACINE_ESSAIM DOSSIER_BANQUE DOSSIER_ESSAIS SORTIE"""
import json, pathlib, sys
import numpy as np
sys.path.insert(0, sys.argv[1])
from essaim_m3.noyau import cli
D = pathlib.Path(sys.argv[2]); E = pathlib.Path(sys.argv[3]); SORTIE = pathlib.Path(sys.argv[4]); E.mkdir(parents=True, exist_ok=True)
pb = D / "banque-confrontation-v5.json"; b = json.loads(pb.read_text(encoding="utf-8"))
ids5 = [t["id"] for p in ("train", "test", "test_final") for t in b[p]]
g = np.random.default_rng(np.random.SeedSequence(20261025))
cas = {"sain_176_ids_v5": ids5, "artefact_espace_v3_200": [f"t-{i:04d}" for i in range(1, 201)],
       "artefact_v5_plus_24_hors_banque": ids5 + [f"t-{i:04d}" for i in range(1, 25)]}
r = {}
for nom, ids in cas.items():
    f = E / f"{nom}.npz"
    np.savez(f, ids=np.array(ids), X=g.normal(size=(len(ids), 8)).astype(np.float32))
    try:
        traits, msg = cli.charger_traits(f, pb, b)
        r[nom] = {"resultat": "ACCEPTE", "n_traits": len(traits), "hors_banque_servis": len(set(traits) - set(ids5))}
    except ValueError as e:
        r[nom] = {"resultat": "REFUSE", "motif": str(e)[:90]}
SORTIE.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(r, ensure_ascii=False, indent=1))
