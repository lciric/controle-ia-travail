# Compte rendu — masque v2 et lecteur par programme, second jeu — v1

Exécutant neuf, modèle S. Heure de fin : 2026-11-20T10:21:59Z (`date -u`). Mandat vérifié à son empreinte (aa6d9936…, OK). Aucune carte lue, aucune valeur ni identifiant de carte consigné.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/rejeu-masque-v2-lecteur-programme-second-jeu-v1/` (abrégé D).

Entrées vérifiées à leur empreinte : masque v2 (769aace5…), lecteur (de99117b…), configuration A v2 (a6c5d87b…), configuration B (b44371d2…). Les deux pièces de scellement ont été lues en entier (tirées de `origin/main` par `git show` redirigé ; absentes de la branche locale `main` pour la seconde). Aucun module voisin importé (imports standard seulement).

## Étapes

1. `python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py` : code 0, statut « lu », aucune anomalie.
2. Masque v2 (`masque_style_cartes_v2.py`, `--sortie D/sorties/masque/cartes-masquees-v2.json`) : code 0. Empreinte de la sortie `ee3359e14b67380d68893ca63cd048fa1d7a83dfea346c30fa4dc14f991c1661`.
   Clés retirées de la forme masquée, nombres attendus de la configuration A v2, vérifiés par le masque v2 (code 0) : `_` 2 ; `cout_note` 1 ; `epreuve_hors_ligne` 1 ; compte par clé, jamais par carte.
   Écran : cartes 94 ; aucune formule récitée distincte ; aucune formule restée sous une autre graphie ; étiquettes retirées 0 ; marques d'emphase retirées 172 ; formules de la configuration retirées 662 (compteurs agrégés, sans contenu).
3. Lecteur par programme, forme « fiches » (`D/sorties/lecteur-fiches/lecture-programme-fiches.json`) : code 0. Empreinte `f96249921b895dee8a5be0469a9643abe02933b3b2356f47cf7e5be0042da079`. Écran : 94 cartes ; D = 0:19, 1:47, 2:28 ; indécidable 0 ; voie I 7, N 65, P 22.
4. Lecteur par programme, forme « masque » sur la sortie du masque (`D/sorties/lecteur-masque/lecture-programme-masque.json`) : code 0. Empreinte `6b157ae1c677b32670241014d1b4139945314b285f57271734b3a82de34cf9f5`. Écran : 94 cartes ; D = 0:22, 1:46, 2:26 ; indécidable 0 ; voie I 7, N 66, P 21.
5. Aucun refus, rien relancé.
6. Compagnons `.sha256` écrits pour les trois sorties, `sha256sum -c` : OK pour les trois.

Écart : aucun. Pièces de scellement tirées de `origin/main` faute de présence dans la branche locale.
