"""Conventions fixées dans le code avant l'instance — témoin « attaque publiée reproduite » (Bailey et collègues), v3.

La v3 applique la relecture en différentiel du code v2
(`docs/notes/reproduction-attaque-publiee-v1/relecture-differentiel-code-condition6-v2-bailey-v1.md`, `4f079ece…`) :
noms des fichiers en « -v3 » (R12) ; fichiers d'état empreintés et transférés comme les journaux (correction 11) ;
versions exigées (correction 8) ; mémoire vive comptée en octets décimaux (correction 9, lecture à acter) ; versions
figées du manifeste (`versions-figees-temoin-bailey-v1.json`, `e21bccf6…`).
La v2 appliquait la contre-lecture `90af7dea…` (journal des notes séparé du journal technique, juge adaptateur, liste
fermée de ce qui sort). Texte qui prime : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`).

Tout ce qui est ici est une constante publique (commit, empreintes de fichiers publics relevées dans le relevé
`d804ad8e…`) ou une convention d'écriture ; aucune note, aucun résultat.

Conventions :
- Empreinte des valeurs d'un suffixe : SHA-256 des octets du tenseur converti en float32, contigu en ordre C, après
  `detach().cpu()` ; la forme est préfixée (texte ASCII « d0xd1x…; »).
- Étiquettes d'évaluation attendues par tour e, dans l'ordre du code public : « Inning e, defender just went », la
  table « behavior_evaluation_e_attacker_just_went », « Inning e, attacker just went ». Au journal technique, la
  première et la dernière sont des évènements `evaluation`, la table est l'évènement `pas` écrit à sa création
  (champ `table`) : la lecture lit les trois, n'en fabrique aucune (correction 4 (c)).
- Appariement (P-1 de `90af7dea`, lecture à acter) : « l'empreinte de l'entrée » d'une ligne de la table de
  comportement est l'empreinte de sa colonne `beh_target` (réponse de référence recopiée du jeu) ; 196 valeurs
  distinctes sur 200, les 4 doublons sont des paires identiques. Les 200 empreintes attendues sont calculées à la mise
  en place et écrites dans `mise-en-place-v3.json` pour le rejeu de l'audit.
- Mémoire vive : « 128 Go » du devis lu comme 128 × 10⁹ octets, minimum de `MemTotal` et de la limite du groupe de
  contrôle (lecture à acter).
"""
from __future__ import annotations

import hashlib
from pathlib import Path

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
# Établi le 10 novembre 2026 : le juge est un adaptateur LoRA sur « google/gemma-2b » (base à accès contrôlé).
JUGE_BASE = "google/gemma-2b"
JUGE_COMMIT_PAQUET = "7a551d5b440ec7b75d4f6f5bb7c1719965b76b47"
MEMOIRE_VIVE_MIN_OCTETS = 128 * 10 ** 9  # devis v4, « au moins 128 Go » ; Go décimaux (lecture à acter)
GEN_LEN = 300
CONCEPT = "HIDHarmfulConceptDataModule"
METRIQUE = "MLPMetric"

# Versions figées (S-2) : fichier et empreinte ; Python 3.11.
VERSIONS_FIGEES = "docs/notes/reproduction-attaque-publiee-v1/versions-figees-temoin-bailey-v1.json"
VERSIONS_FIGEES_SHA256 = "e21bccf6eb99c9255f0069be7af2fe5d729bde9ab05db56811ccef1eddee06f9"
PYTHON = "3.11"
# Correction 8 : la garde « versions » refuse un dictionnaire vide et exige au moins ces paquets.
VERSIONS_EXIGEES = ("torch", "transformers", "peft", "hydra-core", "omegaconf")

# Chemins relatifs au dossier de l'exécution. Seuls ces fichiers sortent de l'instance (liste fermée, B-6).
JOURNAL_NOTES = "journal/notes-v3.jsonl"
JOURNAL_TECHNIQUE = "journal/technique-v3.jsonl"
JOURNAL_EGALITES = "journal/egalites-scellees-v3.jsonl"
JOURNAL_GARDES = "journal/gardes-v3.jsonl"
SORTIE_DUREES = "sortie-durees-v3.jsonl"
EMPREINTES_FICHIERS = "empreintes-fichiers-v3.jsonl"
GARDES_LANCEUR = "gardes-lanceur-v3.jsonl"
ETAT_EXECUTION = "etat-execution-v3.json"
NOMS_JOURNAUX = (JOURNAL_NOTES, JOURNAL_TECHNIQUE, JOURNAL_EGALITES, JOURNAL_GARDES, SORTIE_DUREES,
                 EMPREINTES_FICHIERS, GARDES_LANCEUR, ETAT_EXECUTION)
# Fichiers d'état des étapes hors exécution (correction 11) : empreintés et transférés comme les journaux.
ETAT_MISE_EN_PLACE = "mise-en-place-v3.json"
ETAT_CONTROLE_JUGE = "controle-juge-v3.json"
ETAT_REGLE = "regle-tours-v3.json"
FICHIERS_ETAT = (ETAT_MISE_EN_PLACE, ETAT_CONTROLE_JUGE, ETAT_REGLE)
EMPREINTES_INSTANCE = "empreintes-instance-v3.json"
SORTANTS = NOMS_JOURNAUX + FICHIERS_ETAT
EVALUATIONS_PAR_TOUR = 2  # « defender just went », puis « attacker just went »

DEFENSEUR = "Inning {e}, defender just went"
ATTAQUANT = "Inning {e}, attacker just went"
COMPORTEMENT = "behavior_evaluation_{e}_attacker_just_went"

# Gardes de mise en place (texte, « Gardes (R5) », « De mise en place »), plus les versions (écart 4).
GARDES_MISE_EN_PLACE = ("dépôt public", "empreintes", "graines", "mémoire vive", "python", "versions", "commits",
                        "révisions")


def pas_par_tour(epochs: int, n_entrainement: int, batch_size: int) -> int:
    """Pas d'un tour : `epochs` passes sur le chargeur d'entraînement (`train_harmful.py` l. 109-111), lots de
    `batch_size`, dernier lot incomplet compris (`DataLoader` sans `drop_last`)."""
    return int(epochs) * -(-int(n_entrainement) // int(batch_size))


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


def chemin_params(dossier_params, e: int) -> Path:
    """Fichier du suffixe du tour e, tel que le code public le nomme (`utils.py` l. 100-121 et 439-442)."""
    return Path(dossier_params) / CONCEPT / f"model-params-{METRIQUE}_ade_{e}.pkl"


def chemin_sonde(dossier_sondes, e: int) -> Path:
    return Path(dossier_sondes) / CONCEPT / f"{METRIQUE}_ade_{e}.pkl"
