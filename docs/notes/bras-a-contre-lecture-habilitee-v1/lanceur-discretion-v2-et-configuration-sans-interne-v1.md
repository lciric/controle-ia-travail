# Lanceur de l'étape de discrétion du bras A, version 2, et sa configuration de course — pièce sans interne — v1

Écrit le 2026-11-22T21:49:09Z (`date -u`) par un lecteur habilité (Opus 5.5, agent neuf), sous le mandat `docs/notes/bras-a-contre-lecture-habilitee-v1/mandat-lecteur-habilite-lanceur-discretion-v2-et-configuration-v1.md` (`e65415a7b46cb44490a6fbb74ed2fdf000684fd8bc93da9540992aa2a6e24d13`), restes (b) et (c). Classe C. Aucun appel payant, aucune clé, aucune sortie de course ouverte.

## Lanceur, version 2
- Chemin : `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v2.py`, branche `claude/bras-a-habilite-developpeur-v1`, commit `848c17649d3c324461747daa99fb8784c88a8baa`, empreinte `c3840745ccaad9b889b676ff7ac2450397f60192b72391e2c42ec37eb5e5ca7e` (compagnon égal ; inchangé depuis ce commit).
- Réserve sur le manifeste du lanceur : **non levée**. Le lanceur n'a pas changé depuis la vérification qui l'a posée : après une panne pendant la production, le manifeste d'arrêt ne garde toujours pas les réglages de reproductibilité de la carte. Aucun calcul n'en dépend ; la vérification ne tient pas la course à elle. La lever demande une version 3 du lanceur.

## Configuration de course, version 1
- Chemin : `docs/notes/bras-a-moniteurs-v1/config-lanceur-discretion-bras-a-v2-course-v1.json`, même branche, commit `7ee624fe9`, empreinte `1e0907d88d534b3578d2380842ebe145a86af55168de62e42c48e5c56ec583ce`.
- Elle fixe le dossier du fichier des scores par unité à `donnees/bras-a-v2-discretion/rangs-par-unite`, disjoint du dossier de sortie, et cite le texte scellé du bras A par le marqueur unique `EMPREINTE_TEXTE_V2_BRAS_A`, que la mère remplace après le scellement du texte.
- Essais : `tests/test_bras_a_v2_habilite_config_lanceur_discretion_v2_course_v1.py`, même commit, empreinte `d3f9b613f06a7ddb063c71a86bd2016765894ed0f67007b9fa0284411b6312d5` ; **7 passés sur 7**. Tant que le marqueur reste, la configuration est refusée, par la garde des essais et par le lanceur lui-même (cas sain et artefact éprouvés ; retrait de la garde : l'essai échoue).

## Rapport interne
- `docs/notes/bras-a-contre-lecture-habilitee-v1/lanceur-discretion-v2-et-configuration-interne-v1.md`, même branche, commit `7ee624fe9`, empreinte `4042c6961d9f7c78a6d96c6fa73a3eb46b7cff75f1138fa72a532deddadca743`.

## Points pour la mère
1. Le chemin du texte scellé est supposé (`prereg/T0.7-organismes-discrets-v-a-v2.md`) : à corriger en même temps que le marqueur s'il diffère.
2. Remplir le marqueur dans une version neuve de la configuration (R12), la version 1 gardée : ses essais portent sur elle telle que versée.
3. Sept valeurs de la configuration restent à fixer (elles ne sont pas données par le mandat) ; tant qu'elles ne le sont pas, le lanceur refuse la configuration. À fixer dans la même version neuve, avant la contre-lecture prévue.
