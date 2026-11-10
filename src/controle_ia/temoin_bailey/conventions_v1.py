"""Conventions fixées dans le code avant l'instance — témoin « attaque publiée reproduite » (Bailey et collègues), v1.

Point 6 de la liste « ce qui manque à la condition 6 » de la contre-lecture du code
(`docs/notes/reproduction-attaque-publiee-v1/contre-lecture-code-analyse-bailey-v1.md`, `151eee65…`), pour le
préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`). Tout ce qui est ici est une
constante publique (commit, empreintes de fichiers publics relevées dans le relevé `d804ad8e…`) ou une convention
d'écriture ; aucune note, aucun résultat.

Conventions :
- Empreinte des valeurs d'un suffixe : SHA-256 des octets du tenseur converti en float32, contigu en ordre C, après
  `detach().cpu()` ; la forme est préfixée (texte ASCII « d0xd1x…; ») pour que deux formes ne se confondent pas.
  S'applique à `params` (suffixe appris) et à `init_params` (valeur initiale), rangés dans le même fichier (écart 9).
- Étiquettes d'évaluation attendues par tour e (dans l'ordre où le code public les produit) :
  « Inning e, defender just went » (table `metric_evaluation`), puis la table de comportement
  « behavior_evaluation_e_attacker_just_went », puis « Inning e, attacker just went ».
- Appariement : « l'empreinte de l'entrée » d'une ligne de la table de comportement est l'empreinte de sa colonne
  `beh_target`, que le code public recopie sans la transformer depuis la colonne `response` du jeu (le texte d'entrée
  rendu par le modèle porte le gabarit de conversation, et son décodage n'est pas garanti à l'identique). Sur les 200
  entrées (validation puis test, ordre des fichiers), les réponses distinctes sont 196 et les paires (prompt, réponse)
  distinctes aussi 196 : la réponse identifie la paire ; les 4 doublons sont des paires identiques. L'empreinte du texte
  d'entrée est journalisée aussi, pour l'audit. Les empreintes attendues se calculent sur l'instance par
  `pandas.read_csv`, comme le code public.
- Noms des journaux d'une exécution (garde de fin de run) : `NOMS_JOURNAUX`.
"""
from __future__ import annotations

import hashlib

COMMIT_PUBLIC = "9c1f4b1a721fa3c43d00b8605ee7db4c84a55942"
ARBRE_PUBLIC = "c7cf686c7325573460505647531284b90e5f34e2"
DEPOT_PUBLIC = "https://github.com/LukeBailey181/obfuscated-activations"
SOUS_DOSSIER = "inference_time_experiments"
EXPERIENCE = "zf-iter-100-mlp"

# Relevé `d804ad8e…`, section 1 (chemins relatifs à SOUS_DOSSIER).
EMPREINTES_PUBLIQUES = {
    "train_harmful.py": "83c3e4e747035311cfefa2163211ab6fcdb3058928db7d935633221a650d1b9b",
    "evaluate.py": "8cd2ecbce601421582ce64f56c45e2a4dd06b22f1e7c40bbd3123c587073131e",
    "configs/experiment/zf-iter-100-mlp.yaml": "7d3bd16aed266f4a0e0ac12628cb88bf17e3c2e74032e3ada1d7d38ffa9bf592",
    "configs/experiment/z-jailbreak.yaml": "bb2f85e43d69fe33129fa171f1af16c57b6ca62b7e441b6168ba80ee1ae47e97",
    "configs/experiment/default.yaml": "f38bb18951ef775ae114b1783a5d8a32d91270fcbdf587aee0ddf576956e211c",
    "datasets/harmful_dataset/harmful_train_no_spec_tokens.csv": "1063d28221dc5a59e1f60d6fa0bc4828c9983ce3db15a106e160d487bafbb081",
    "datasets/harmful_dataset/harmful_val_no_spec_tokens.csv": "e1ff21a28b06a771c0bdba0e5f732dd659b02a6c3c10ffe833dc1f136135391c",
    "datasets/harmful_dataset/harmful_test_no_spec_tokens.csv": "77b81432ab98f1d583df649622d641157cfe9b4339d0ad320269fc10c4a1a661",
    "datasets/harmful_dataset/benign_train_no_spec_tokens.csv": "690b038241fe4b0f9e3b6bbb61ef34e10aa7d2d7a0766214543e0c96813116ff",
    "datasets/harmful_dataset/benign_val_no_spec_tokens.csv": "0f0a0e77dab83eae68e1a4e6e8dcdfec049be40ce8ca1b14106676dde8fc1cef",
    "datasets/harmful_dataset/benign_test_no_spec_tokens.csv": "782901e4e9e6b2da4816ddc2a47060cec9c884758890bdbc4e96f4c46f9e2d88",
}
DOSSIER_JEU = "datasets/harmful_dataset"
MODELE = "meta-llama/Meta-Llama-3-8B-Instruct"
JUGE = "qylu4156/strongreject-15k-v1"
JUGE_COMMIT_PAQUET = "7a551d5b440ec7b75d4f6f5bb7c1719965b76b47"
MEMOIRE_VIVE_MIN_GO = 128  # devis v4, table « Mémoire vive de l'hôte »
GEN_LEN = 300
CONCEPT = "HIDHarmfulConceptDataModule"
METRIQUE = "MLPMetric"

# chemins relatifs au dossier de l'exécution ; « journal/ » est écrit par le journaliseur, le reste par le lanceur
NOMS_JOURNAUX = ("journal/journal-v1.jsonl", "journal/egalites-scellees-v1.jsonl", "journal/gardes-v1.jsonl",
                 "sortie-durees-v1.jsonl", "empreintes-fichiers-v1.jsonl", "gardes-lanceur-v1.jsonl",
                 "etat-execution-v1.json")

DEFENSEUR = "Inning {e}, defender just went"
ATTAQUANT = "Inning {e}, attacker just went"
COMPORTEMENT = "behavior_evaluation_{e}_attacker_just_went"


def etiquettes_attendues(e: int) -> list[str]:
    return [DEFENSEUR.format(e=e), COMPORTEMENT.format(e=e), ATTAQUANT.format(e=e)]


def sha_texte(x) -> str | None:
    return None if x is None else hashlib.sha256(str(x).encode("utf-8")).hexdigest()


def sha_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def empreinte_valeurs(tenseur) -> str:
    """Empreinte des valeurs d'un tenseur (torch ou tableau numpy) : float32, ordre C, forme préfixée."""
    import numpy as np
    if hasattr(tenseur, "detach"):
        tenseur = tenseur.detach().cpu().float().numpy()
    a = np.ascontiguousarray(np.asarray(tenseur, dtype=np.float32))
    h = hashlib.sha256(("x".join(str(d) for d in a.shape) + ";").encode("ascii"))
    h.update(a.tobytes(order="C"))
    return h.hexdigest()


def chemin_params(dossier_params, e: int):
    """Fichier du suffixe du tour e, tel que le code public le nomme (`utils.py` l. 100-121 et 439-442)."""
    from pathlib import Path
    return Path(dossier_params) / CONCEPT / f"model-params-{METRIQUE}_ade_{e}.pkl"


def chemin_sonde(dossier_sondes, e: int):
    from pathlib import Path
    return Path(dossier_sondes) / CONCEPT / f"{METRIQUE}_ade_{e}.pkl"
