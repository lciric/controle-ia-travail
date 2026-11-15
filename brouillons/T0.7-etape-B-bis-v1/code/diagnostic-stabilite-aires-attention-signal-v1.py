"""Stabilité des aires sous les arrondis, **variante à signal** (complément de `diagnostic-stabilite-aires-attention-v1.py`, non
modifié), v1. Sur le jeu de la répétition, les sondes n'apprennent rien qui se généralise (aires tenues à l'écart ≈ 0,46 et 0,52) :
la dispersion mesurée est celle de sondes au hasard. Ici, **mêmes tirages, mêmes graines, mêmes longueurs**, seul le décalage des
jetons positifs le long de u change (0,5 → `--decalage`, déclaré) : apprentissage et jeu tenu à l'écart sous la même loi.
**Processeur seulement** ; données synthétiques seulement ; aucune donnée de 7a, 7b, T0.7 ou P3-bis.

Membres (piles réelles seulement : un seul arrondi au premier pas ne change rien, et la perturbation 10⁻¹⁰ au premier pas
sous-estime l'écart des piles, `diagnostic-stabilite-aires-attention-v1-sortie.json`) : P0 paquet gelé (AVX-512, réduction numpy) ;
P1 paquet gelé en AVX2 ; P2 chemin v1 (réduction torch) ; P3 chemin v1 en AVX2. Le jeu d'instructions se choisit avant l'import de
torch (`ATEN_CPU_CAPABILITY`, `MKL_ENABLE_INSTRUCTIONS`).

Sous-commandes : `apprendre SORTIE.json --chemin {gele,v1} --famille F --decalage D --npz F.npz` ;
`evaluer SORTIE.json --travail DOSSIER --decalage D`.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("diagnostic_ecart_attention_carte_v1", ICI / "diagnostic-ecart-attention-carte-v1.py")
d1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(d1)
_spec3 = importlib.util.spec_from_file_location("diagnostic_stabilite_aires_attention_v1",
                                                ICI / "diagnostic-stabilite-aires-attention-v1.py")
d3 = importlib.util.module_from_spec(_spec3)
_spec3.loader.exec_module(d3)


def jeu(rep, n_actions: int, largeur: int, cle: str, decalage: float):
    """`repetition_carte_bbis_v1.jeu_synthetique`, mêmes tirages, décalage des positifs `decalage`·u au lieu de 0,5·u."""
    import numpy as np
    rng = np.random.default_rng(rep._graine(cle))
    u = rng.standard_normal(largeur).astype(np.float32)
    u /= np.linalg.norm(u)
    y = np.r_[np.ones(n_actions // 2, int), np.zeros(n_actions - n_actions // 2, int)]
    seqs = []
    for k in range(n_actions):
        n = int(rng.integers(rep.LONGUEURS[0], rep.LONGUEURS[1] + 1))
        x = rng.standard_normal((n, largeur), dtype=np.float32)
        if y[k]:
            x[: max(1, n // 4)] += np.float32(decalage) * u
        seqs.append(x)
    return seqs, y, u


def jeu_tenu(rep, n_actions, largeur, decalage):
    import numpy as np
    _, _, u = jeu(rep, 1, largeur, "bbis/repetition/donnees", decalage)
    rng = np.random.default_rng(rep._graine("bbis/repetition/tenu-a-l-ecart"))
    y = np.r_[np.ones(n_actions // 2, int), np.zeros(n_actions - n_actions // 2, int)]
    seqs = []
    for k in range(n_actions):
        n = int(rng.integers(rep.LONGUEURS[0], rep.LONGUEURS[1] + 1))
        x = rng.standard_normal((n, largeur), dtype=np.float32)
        if y[k]:
            x[: max(1, n // 4)] += np.float32(decalage) * u
        seqs.append(x)
    return seqs, y


def cmd_apprendre(x) -> dict:
    import numpy as np
    import torch
    from controle_ia.sondes import familles as fam
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    from controle_ia.t07bbis.commun_v1 import AGREGATION_DE, EPOQUES, PAS
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(x.fils))
    rep = d1._rep()
    seqs, y, _ = jeu(rep, x.actions, x.largeur, "bbis/repetition/donnees", x.decalage)
    if x.decalage == 0.5:                       # contrôle : même jeu que la répétition au décalage d'origine
        ref, yr = rep.jeu_synthetique(x.actions, x.largeur, "bbis/repetition/donnees")
        assert all(np.array_equal(a, b) for a, b in zip(seqs, ref)) and np.array_equal(y, yr)
    g = d1._graine(rep, x.famille)
    nom = f"{x.famille}-c15-l2_{d1.L2!r}"
    t0 = time.perf_counter()
    if x.chemin == "v1":
        lot = ac.LotCarte(seqs, "cpu")
        del seqs
        s = ac.entrainer(lot, x.famille, nom, 15, y, d1.L2, g)
    else:
        d1.brancher_repliques()
        s = fam.entrainer(x.famille, nom, 15, seqs, y, AGREGATION_DE[x.famille], g, fam.Reglages(l2=d1.L2, epoques=EPOQUES,
                                                                                                   pas=PAS))
    np.savez(x.npz, w=s.w, b=np.array([s.b]), q=s.q if s.q is not None else np.zeros(0))
    return {"chemin": x.chemin, "famille": x.famille, "decalage": x.decalage, "graine": g, "npz": Path(x.npz).name,
            "duree_s": time.perf_counter() - t0, "empreinte_parametres": d1._empreinte_sonde(s.w, s.b, s.q),
            "instruction": d1._instruction(), "script": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def cmd_evaluer(x) -> dict:
    import numpy as np
    from scipy.stats import spearmanr
    from controle_ia.sondes import familles as fam
    from controle_ia.sondes.evaluation import aire_sous_courbe
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    from controle_ia.t07bbis.commun_v1 import AGREGATION_DE
    rep = d1._rep()
    trav = Path(x.travail)
    seqs, y = jeu_tenu(rep, x.actions, x.largeur, x.decalage)
    sortie = {"decalage": x.decalage, "jeu_tenu_a_l_ecart": {"actions": len(seqs), "positifs": int(y.sum())}, "familles": {}}
    for f in ("attention", "lineaire"):
        parts = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(trav.glob(f"signal-*-{f}*.json"))}
        membres = {}
        for nom, part in sorted(parts.items()):
            z = np.load(trav / part["npz"])
            q = z["q"] if z["q"].size else None
            sd = fam.SondeLineaireJetons("s", 15, AGREGATION_DE[f], z["w"], float(z["b"][0]), q, f)
            assert d1._empreinte_sonde(sd.w, sd.b, sd.q) == part["empreinte_parametres"]
            membres[nom] = sd
        if not membres:
            continue
        sc = {n: ac.scores(sd, seqs) for n, sd in membres.items()}
        aires = {n: aire_sous_courbe(v, y) for n, v in sc.items()}
        ref = f"signal-gele-{f}"
        paires = {f"{n} contre {ref}": {"ecart_controle": ac.ecart_relatif(sc[n], sc[ref]),
                                        "ecart_absolu_median": float(np.median(np.abs(sc[n] - sc[ref]))),
                                        "spearman": float(spearmanr(sc[n], sc[ref]).statistic),
                                        "ecart_aire": aires[n] - aires[ref]} for n in membres if n != ref}
        v = np.array(list(aires.values()))
        sortie["familles"][f] = {"aires": aires, "paires": paires, "parties": parts,
                                 "dispersion": {"etendue": float(v.max() - v.min()),
                                                "ecart_type": float(v.std(ddof=1)) if v.size > 1 else None,
                                                "membres": len(v)},
                                 "erreur_type_echantillonnage_aire": d3._se_aire(aires[ref], int(y.sum()),
                                                                                  int((1 - y).sum()))}
    sortie["script"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(x.sortie).write_text(json.dumps(sortie, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return {"sortie": x.sortie}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("commande", choices=["apprendre", "evaluer"])
    ap.add_argument("sortie")
    ap.add_argument("--actions", type=int, default=640)
    ap.add_argument("--largeur", type=int, default=4096)
    ap.add_argument("--fils", type=int, default=4)
    ap.add_argument("--chemin", choices=["gele", "v1"], default="gele")
    ap.add_argument("--famille", choices=["lineaire", "attention"], default="attention")
    ap.add_argument("--decalage", type=float, required=True)
    ap.add_argument("--npz")
    ap.add_argument("--travail")
    x = ap.parse_args(argv)
    r = cmd_apprendre(x) if x.commande == "apprendre" else cmd_evaluer(x)
    if x.commande == "apprendre":
        Path(x.sortie).write_text(json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n",
                                  encoding="utf-8")
    print(json.dumps(r, ensure_ascii=False, default=str)[:300])
    return 0


if __name__ == "__main__":
    sys.exit(main())
