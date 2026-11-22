# Organismes discrets, bras A — vérification des corrections du devis de la carte des deux moniteurs, v2 — v1

- **Pièce vérifiée** : `docs/notes/relance-organismes-discrets-v1/devis-carte-moniteurs-bras-a-v2.md`, `c84f762247d39bdba38c70361ec1f8e877d3005882336b42a936f2c5fe037648` (empreinte refaite, égale au compagnon), branche `origin/relance-bras-a/devis-carte-v3`, commit `6f7394cd`.
- **Référence** : version 1, `6559f7886a599550090cde361fb7d5856631c27c3f008afb8e2bc3c46313fabc` (commit `76514065`) ; contre-lecture `contre-lecture-devis-carte-moniteurs-bras-a-v1-v1.md`, `c0e299045a3a5878e22fc79e388accef8c3c3b993c2989ef76947b4d3c18d4b9`.
- **Vérificateur** : l'auteur de la contre-lecture (Claude Opus 5.5), qui n'a écrit ni la v1 ni la v2. Même cloisonnement que la contre-lecture ; aucun réseau hors `git fetch`, aucune dépense, rien committé. Date (UTC) : 2026-11-22.

## Verdict

**Corrections vérifiées, engageable.**

## Méthode

`diff` complet de la v1 à la v2, chaque bloc changé confronté au texte de correction de la contre-lecture ; programme de la section 9 de la v2 extrait du fichier et rejoué tel quel (`python3 -I`).

## Résultat, remarque par remarque

| remarque | appliquée mot pour mot | où |
|---|---|---|
| M1 | oui | section 4 (pire cas B 53,09 → 55 ; ensemble 55 + 55 = 110 ; `PB` sans + 4 ; exemples 55, 95, 100, 104) ; section 0, points 3 et 4 (5 à 14 %) ; section 5, lignes (1) et (3) ; décision 1 (b) 110 ; décision 2 (55 et 55 ; 95 à 104 contre 110 ; 110 USD) ; section 9 (programme, sortie, contrôles 0,136 et 0,055) ; message du commit (« 55 et 55 USD de repli ») |
| M2 | oui | décision 1 (décision, option (a), recommandation) ; section 6 |
| M3 | oui | section 4, après « Arrêts » |
| M4 | oui | S1 et S2 (fondement) ; réserve 1 ; section 0, point 5 |
| M5 | oui | décision 2 (décision, option (b)) ; section 6, ligne ajoutée |
| m1 à m7 | oui | section 2 ; section 5 ; ligne A ; section 3 ; décision 2, enjeu ; S2 ; décision 1, enjeu |

**Rien d'autre** : hors des corrections, les seuls changements sont ceux annoncés — titre (« v2 »), date, commit lu (`06416a69`), statut, ligne « Version antérieure », sceau, table « Corrections depuis la v1 » et sa note, heure du jeu du programme, un point de la déclaration (section 10). Aucun autre mot changé.

## Programme rejoué

Sortie identique à celle écrite dans la v2 : ligne A pire 51,5211 → 55 ; ligne B pire 53,0921 → 55 ; ensemble 16,39 à 18,23 h, 20,39 à 25,70 USD attendus, plafonds 55 + 55 = 110 ; recalculés 28 + 27 = 55, puis 47 + 48 = 95, 49 + 51 = 100, 51 + 53 = 104. Égal aux nombres de la contre-lecture.
