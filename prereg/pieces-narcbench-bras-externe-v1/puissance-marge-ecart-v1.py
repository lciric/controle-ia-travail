"""Un point de plus pour la règle « reproduit / non reproduit / non tranché » (texte court, bras externe NARCBench, brouillon 3) :
la statistique de l'écart (publiée 0,99, marge 0,96) quand l'aire vraie égale sa marge. Données SIMULÉES seulement.

Réutilise la fonction `simuler` du script scellé `puissance-regle-v1.py` (empreinte vérifiée avant import), sans la modifier ;
graine `SeedSequence(<argument>, spawn_key=(1, 96))`, distincte des clés de la grille scellée.
"""
import hashlib
import importlib.util
import sys
from pathlib import Path

import numpy as np

SCELLE = Path(__file__).with_name("puissance-regle-v1.py")
EMPREINTE = "fa482dd97b78af1d858706f7dfd880b2ead58e3ff001ef672334b4e0af10fb7a"


def main():
    if hashlib.sha256(SCELLE.read_bytes()).hexdigest() != EMPREINTE:
        raise SystemExit(f"{SCELLE} : empreinte différente du script scellé")
    spec = importlib.util.spec_from_file_location("puissance_regle_v1", SCELLE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rng = np.random.default_rng(np.random.SeedSequence(int(sys.argv[1]), spawn_key=(1, 96)))
    r = module.simuler(0.96, 0.99, rng=rng)
    print("publié 0.99  aire vraie 0.9600 (marge de l'écart)  " + "  ".join(f"{e} {p:.3f}" for e, p in r.items()))


if __name__ == "__main__":
    main()
