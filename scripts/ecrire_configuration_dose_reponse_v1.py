"""Écrit et scelle la configuration réelle de la course de dose–réponse de l'organisme à consigne cachée (texte scellé
`prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md`, 2263c5c4…), à partir des constantes du code
(`dose_reponse.controles_v1`) et de la configuration citée par le texte pour les réglages de génération
(`prereg/T0.6-organismes-config-7b-v1.json`, b7a5c1ba… : agent, gabarit, carte, offre, garde d'équivalence).

Seules entrées : la banque de 64 tâches (chemin ; l'empreinte est lue sur son compagnon et vérifiée) et le commit du code
cité par la ligne CODE-DOSE-REPONSE-CONSIGNE-CACHEE. La configuration est vérifiée par `controles_v1.exiger_config` avant
d'être écrite ; rien n'est réécrit (R12).

    PYTHONPATH=src python scripts/ecrire_configuration_dose_reponse_v1.py BANQUE.json COMMIT_CODE [SORTIE]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from controle_ia.dose_reponse import controles_v1 as ct
from controle_ia.scellement import sceller, verifier

SORTIE = "prereg/T0.6-dose-reponse-configuration-course-v1.json"
CONFIG_7B = ("prereg/T0.6-organismes-config-7b-v1.json", "b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527")
PIECE_JOINTE = "brouillons/g0-criteres-2-3-v1/consignes-privees-dose-reponse-consigne-cachee-v4.json"


def configuration(banque: str, sha_banque: str, commit: str, config_7b: dict, piece_jointe: str = PIECE_JOINTE) -> dict:
    a = config_7b["agent"]
    return {
        "objet": "course de dose–réponse de l'organisme à consigne cachée (texte scellé 2263c5c4…)",
        "mode": "reel", "commit_code": commit,
        "agent": {k: a[k] for k in ("modele", "nom", "revision", "texte_attendu_ouverture", "variables_gabarit")},
        "prereg": {"chemin": ct.PREREG, "sha256": ct.PREREG_SHA256},
        "piece_jointe": {"chemin": piece_jointe, "sha256": ct.PIECE_JOINTE_SHA256},
        "consignes_premier_test": {"chemin": config_7b["chemin_consignes"], "sha256": ct.PREMIER_TEST_SHA256},
        "banque": {"chemin": banque, "sha256": sha_banque},
        "reglages": dict(ct.REGLAGES),
        "actions_min_controle_negatif": config_7b["actions_min_controle_negatif"],
        "fraction_min_controle_negatif": config_7b["fraction_min_controle_negatif"],
        "positions_min_controle_negatif": config_7b["positions_min_controle_negatif"],
        "memoire_vive_min_go": config_7b["memoire_vive_min_go"],
        "noyau_attention": config_7b["noyau_attention"], "fils": config_7b["fils"],
        "modules_repris": dict(ct.MODULES_REPRIS),
        "lancement": {"go_origine": ct.GO_ORIGINE, "go_admis": [ct.GO_ORIGINE], "plafond_usd": ct.PLAFOND_USD,
                      "compte_rendu_usd": 72,
                      "carte": {"course": {"nom": "A100 SXM4 80 Go", "nom_offre": "A100 SXM4", "memoire_carte_min_mo": 80000,
                                           "prix_max_usd_h": 1.3}},
                      "offre": {"coeurs_effectifs_min": 16, "disque_min_go": 300, "etiquette": "dose-reponse-v1",
                                "memoire_vive_min_mo": 128000, "stockage_max_usd_h": 0.08, "telechargement_go_prevu": 40,
                                "telechargement_max_usd_go": 0.05}},
        "designation_critere_3": None,
        "source_des_reglages": {"chemin": CONFIG_7B[0], "sha256": CONFIG_7B[1]},
    }


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3) or not re.fullmatch(r"[0-9a-f]{40}", argv[1]):
        print(__doc__, file=sys.stderr)
        return 2
    banque, commit = argv[0], argv[1]
    sortie = Path(argv[2] if len(argv) == 3 else SORTIE)
    if sortie.exists():
        print(f"{sortie} existe déjà (R12)", file=sys.stderr)
        return 1
    if verifier(CONFIG_7B[0]) != CONFIG_7B[1]:
        print("configuration de l'organisme à adaptateur : empreinte autre que celle du texte scellé", file=sys.stderr)
        return 1
    c = configuration(banque, verifier(banque), commit, json.loads(Path(CONFIG_7B[0]).read_text(encoding="utf-8")))
    ct.exiger_config(c)
    sortie.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{sortie} écrite, scellée : {sceller(sortie)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
