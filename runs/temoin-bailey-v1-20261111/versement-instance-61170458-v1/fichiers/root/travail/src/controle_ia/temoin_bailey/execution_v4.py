"""Exécution du code public dans un processus enfant — témoin « attaque publiée reproduite » (Bailey et collègues), v4.

La v4 (décision de Lazar du 12 novembre 2026, « go (a), garde le poste », après la seconde chute du pilote de la
nouvelle série, note `registres/passations/2026-11-12-2140-temoin-bailey-serie-2-cause-hydra-noeud.md`) change une seule
chose : le script public est lancé **comme programme principal** (`runpy.run_path(<clone>/inference_time_experiments/
train_harmful.py, run_name="__main__")`), comme le font les auteurs (`python train_harmful.py`), au lieu d'être importé
puis appelé (`import train_harmful` ; `train_harmful.main()`). Appelé depuis un module importé, `@hydra.main(
config_path="configs")` cherchait la configuration comme ressource d'un paquet Python `configs` et échouait avant toute
impression (`NotADirectoryError: MultiplexedPath only supports directories` sur l'instance ; « Primary config module
'configs' not found » sur processeur) ; lancé comme programme principal, Hydra la cherche dans le dossier du fichier. Le
reste est inchangé : garde `TESTING`, `WANDB_MODE`, dossier courant, graines (`transformers.set_seed`), journaliseur
substitué dans `obf_reps.logging` et `obf_reps.utils` avant l'appel (le script public construit son journaliseur dans
`obf_reps.utils`, module déjà chargé, que `runpy` réutilise), surcharges, configuration attendue.

Docstring de la v3 :

La v3 appelle le journaliseur v3 et les conventions v3, et applique la correction 14 de la relecture en différentiel
du code v2 (`relecture-differentiel-code-condition6-v2-bailey-v1.md`, `4f079ece…`, A-4) : la garde « TESTING » écrit
son état dans `gardes-lanceur-v3.jsonl` du dossier d'exécution (dossier du fichier `TEMOIN_BAILEY_CONFIG`) avant de
rendre la main, au lieu de l'écrire sur la seule sortie d'erreur, qui reste sur l'instance.

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`), écarts 1, 2, 3, 7 et 9 ; garde du
juge (partie « variable `TESTING` absente au lancement du processus »).

    python -m controle_ia.temoin_bailey.execution_v4 --clone DIR --graine G -- SURCHARGES…

Ce module :
1. vérifie que `TESTING` est absente de l'environnement au lancement (sinon : garde tombée, sortie 3) ; force le mode
   hors service de Weights & Biases (`WANDB_MODE=disabled`), que le journaliseur substitué n'appelle de toute façon pas ;
2. se place dans `inference_time_experiments` du clone (les chemins relatifs du jeu y renvoient) ;
3. pose les graines par la fonction même du code public (`transformers.set_seed`) avant l'entraînement de la sonde
   initiale (écart 3) ;
4. remplace `WAndBLogger` par `JournaliseurLocal` dans `obf_reps.utils` et `obf_reps.logging` (écart 2), sans modifier
   aucun fichier ;
5. appelle `train_harmful.main()` avec les surcharges déclarées.

`surcharges(...)` construit la liste des surcharges déclarées ; `configuration_attendue(...)` calcule, par Hydra, le
texte que `train_harmful.py` l. 173 imprime au démarrage (garde de démarrage, « configuration effective »).
"""
from __future__ import annotations

import argparse
import os
import runpy
import sys
from pathlib import Path

from . import conventions_v3 as cv

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


def _consigner_garde_lanceur(nom: str, message: str) -> None:
    """Correction 14 : état de la garde écrit dans le dossier d'exécution avant de rendre la main."""
    config = os.environ.get("TEMOIN_BAILEY_CONFIG")
    sys.stderr.write(f"garde « {nom} » tombée : {message}\n")
    if not config:
        sys.stderr.write("dossier d'exécution inconnu (TEMOIN_BAILEY_CONFIG absente) : état non écrit\n")
        return
    from .journaliseur_v3 import ajouter_ligne
    ajouter_ligne(Path(config).parent / cv.GARDES_LANCEUR, {"garde": nom, "etat": "tombée", "message": message,
                                                           "tour": -1})


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "TESTING" in os.environ:
        _consigner_garde_lanceur("juge", "variable TESTING présente au lancement du processus")
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
    from .journaliseur_v3 import JournaliseurLocal
    lg.WAndBLogger = JournaliseurLocal
    ut.WAndBLogger = JournaliseurLocal

    script = racine / "train_harmful.py"  # v4 : lancé comme programme principal (Hydra cherche `configs/` à côté)
    sys.argv = [str(script), *over]
    runpy.run_path(str(script), run_name="__main__")
    return 0


if __name__ == "__main__":
    sys.exit(main())
