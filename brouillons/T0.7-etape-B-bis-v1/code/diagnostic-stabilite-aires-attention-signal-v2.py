"""Stabilité des aires sous les arrondis, variante à signal **sur un axe** (v2 de la variante à signal ; la v1 reste : sur la
direction dense u de la répétition, la sonde « attention » ne se généralise pas, même à décalage 1 ou 2 : aires tenues à l'écart
0,567 et 0,558, `diagnostic-stabilite-aires-attention-signal-v1-sortie.json`). Ici, **mêmes tirages, mêmes graines, mêmes
longueurs** que la répétition, mais le décalage des jetons positifs porte sur le **premier axe** e₀ (`--decalage` · e₀ au lieu de
0,5 · u ; u est tiré quand même, pour garder la même suite de tirages) : un signal qu'Adam, qui avance chaque coordonnée au même
pas, peut trouver. Apprentissage et jeu tenu à l'écart sous la même loi. **Processeur seulement** ; données synthétiques seulement.

Membres et mesures : ceux de la variante v1 (P0 paquet gelé AVX-512, P1 gelé AVX2, P2 chemin v1, P3 chemin v1 AVX2 ; linéaire
P0, P1, P2 en témoin). Sous-commandes : `apprendre SORTIE.json --chemin {gele,v1} --famille F --decalage D --npz F.npz` ;
`evaluer SORTIE.json --travail DOSSIER --decalage D`.
"""
from __future__ import annotations

import hashlib
import importlib.util
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("diagnostic_stabilite_aires_attention_signal_v1",
                                               ICI / "diagnostic-stabilite-aires-attention-signal-v1.py")
s1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(s1)
SCRIPT_V2 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def _axe(largeur):
    import numpy as np
    e = np.zeros(largeur, dtype=np.float32)
    e[0] = 1.0
    return e


def jeu(rep, n_actions: int, largeur: int, cle: str, decalage: float):
    """Mêmes tirages que `repetition_carte_bbis_v1.jeu_synthetique` ; décalage `decalage`·e₀ des positifs."""
    import numpy as np
    rng = np.random.default_rng(rep._graine(cle))
    rng.standard_normal(largeur)                    # u : tiré, non utilisé (même suite de tirages)
    e0 = _axe(largeur)
    y = np.r_[np.ones(n_actions // 2, int), np.zeros(n_actions - n_actions // 2, int)]
    seqs = []
    for k in range(n_actions):
        n = int(rng.integers(rep.LONGUEURS[0], rep.LONGUEURS[1] + 1))
        x = rng.standard_normal((n, largeur), dtype=np.float32)
        if y[k]:
            x[: max(1, n // 4)] += np.float32(decalage) * e0
        seqs.append(x)
    return seqs, y, e0


def jeu_tenu(rep, n_actions, largeur, decalage):
    import numpy as np
    e0 = _axe(largeur)
    rng = np.random.default_rng(rep._graine("bbis/repetition/tenu-a-l-ecart"))
    y = np.r_[np.ones(n_actions // 2, int), np.zeros(n_actions - n_actions // 2, int)]
    seqs = []
    for k in range(n_actions):
        n = int(rng.integers(rep.LONGUEURS[0], rep.LONGUEURS[1] + 1))
        x = rng.standard_normal((n, largeur), dtype=np.float32)
        if y[k]:
            x[: max(1, n // 4)] += np.float32(decalage) * e0
        seqs.append(x)
    return seqs, y


s1.jeu, s1.jeu_tenu = jeu, jeu_tenu                 # les sous-commandes de la v1 lisent ces deux fonctions


def main(argv=None) -> int:
    import json
    a = list(sys.argv[1:] if argv is None else argv)
    code = s1.main(a)
    sortie = Path(a[1])
    doc = json.loads(sortie.read_text(encoding="utf-8"))
    doc.update({"variante": "décalage sur le premier axe e₀", "script_v2": SCRIPT_V2})
    sortie.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n", encoding="utf-8")
    return code


if __name__ == "__main__":
    sys.exit(main())
