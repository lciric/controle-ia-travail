"""Pilote préenregistré de l'exposant p, version 3 (brouillon 3 du préenregistrement) : les quatre retouches de code
demandées par la contre-lecture R2 du brouillon 2 (`contre-lecture-v2/contre-lecture-pilote-exposant-p-v2.md`, ligne
188, points I1 et I3), en fichiers neufs (R12).

Ce qui ne change pas est importé de `controle_ia.pilote_exposant_p_v2` sans modification (stimuli, courbes, puissance,
lecture du registre, règle de lecture, ordre des blocs). Ne sont redéfinis que :
- `analyse` : `NE_MONTRE_PAS` (couple 17) et `QUALIF_JUMEAU["au-dessus du jumeau"]` (couple 18), mot pour mot, et ce
  qui en dépend (`PHRASES`, `phrase`) ;
- `run` : bloc 0, nombre de jetons et dernier sous-jeton de chaque porteur (évaluation, déploiement, neutre) sur le
  tokeniseur du modèle lu, rapportés avant tout passage avant (I1, couple 11 ; descriptif, sans seuil) ; lecture liée
  à l'analyse v3 ;
- `go` : règle d'extension du registre des GO, alignée sur la garde de `main` (R-389 ; I3).

Bibliothèque standard seulement à l'import du paquet : l'amorce appelle `go` avant toute installation.
"""
VERSION = "pilote-exposant-p-v3"
