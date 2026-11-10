"""Exécution du code public dans un processus enfant — témoin « attaque publiée reproduite » (Bailey et collègues), v2.

La v2 ne change que les modules appelés (journaliseur v2, conventions v2).

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`), écarts 1, 2, 3, 7 et 9 ; garde du
juge (partie « variable `TESTING` absente au lancement du processus »).

    python -m controle_ia.temoin_bailey.execution_v2 --clone DIR --graine G -- SURCHARGES…

Ce module :
1. vérifie que `TESTING` est absente de l'environnement au lancement (sinon : garde tombée, sortie 3) ; force le mode
   hors service de Weights & Biases (`WANDB_MODE=disabled`), que le journaliseur substitué n'appelle de toute façon pas ;
2. se place dans `inference_time_experiments` du clone (les chemins relatifs du jeu y renvoient) ;
3. pose les graines par la fonction même du code public (`transformers.set_seed`, `optimizers.py` l. 16 et 126-128)
   avant l'entraînement de la sonde initiale (écart 3) ;
4. remplace `WAndBLogger` par `JournaliseurLocal` dans `obf_reps.utils` et `obf_reps.logging` (écart 2), sans modifier
   aucun fichier ;
5. appelle `train_harmful.main()` avec les surcharges déclarées.

`surcharges(...)` construit la liste des surcharges déclarées ; `configuration_attendue(...)` calcule, par Hydra, le
texte que `train_harmful.py` l. 173 imprime au démarrage (garde de démarrage, « configuration effective »).
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from . import conventions_v2 as cv

SORTIE_GARDE = 3


def surcharges(k: int, graine: int, chemin_modele: str, dossier_sondes: str, dossier_params: str,
               dossier_hydra: str) -> list[str]:
    """Surcharges déclarées, et elles seules : écart 1 (tours), 3 (graine), 7 (modèle local, dossier de Hydra hors du
    clone), 9 (dossiers de sauvegarde neufs). Le journaliseur (écart 2) ne passe pas par la configuration."""
    return [f"experiment={cv.EXPERIENCE}",
            f"experiment.attack_defense_epochs={int(k)}",
            f"experiment.seed={int(graine)}",
            f"experiment.model_path={chemin_modele}",
            f"experiment.save_probe_path={dossier_sondes}",
            f"experiment.save_tunable_params_path={dossier_params}",
            f"hydra.run.dir={dossier_hydra}"]


def configuration_attendue(clone: str | os.PathLike, liste_surcharges: list[str]) -> str:
    """Texte attendu au début exact de la sortie standard : `print(OmegaConf.to_yaml(cfg))`, composé par Hydra depuis
    la configuration publique et les seules surcharges déclarées (les surcharges `hydra.*` ne figurent pas dans `cfg`).
    """
    from hydra import compose, initialize_config_dir
    from omegaconf import OmegaConf
    dossier = Path(clone) / cv.SOUS_DOSSIER / "configs"
    propres = [s for s in liste_surcharges if not s.startswith("hydra.")]
    with initialize_config_dir(config_dir=str(dossier.resolve()), version_base=None):
        cfg = compose(config_name="config", overrides=propres)
    return OmegaConf.to_yaml(cfg) + "\n"


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "TESTING" in os.environ:
        sys.stderr.write("garde « juge » tombée : variable TESTING présente au lancement du processus\n")
        return SORTIE_GARDE
    p = argparse.ArgumentParser()
    p.add_argument("--clone", required=True)
    p.add_argument("--graine", type=int, required=True)
    sep = argv.index("--") if "--" in argv else len(argv)
    a = p.parse_args(argv[:sep])
    over = argv[sep + 1:]
    os.environ["WANDB_MODE"] = "disabled"
    racine = Path(a.clone).resolve() / cv.SOUS_DOSSIER
    os.chdir(racine)
    sys.path.insert(0, str(racine))

    from transformers import set_seed
    set_seed(a.graine)

    import obf_reps.logging as lg
    import obf_reps.utils as ut
    from .journaliseur_v2 import JournaliseurLocal
    lg.WAndBLogger = JournaliseurLocal
    ut.WAndBLogger = JournaliseurLocal

    import train_harmful
    sys.argv = [str(racine / "train_harmful.py"), *over]
    train_harmful.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
