# Journal du brouillon 14 du texte de la base boîte noire (T0.8) — v1

- **Nature** : pièce de travail (classe C). **Auteur** : session `session_013QMayo5SNVbiUW6hGnPrCo` (modèle B), rédacteur des brouillons 11 à 14.
- **Heures (UTC, `date -u`)** : rapport de vérification du brouillon 12 lu à 19:27 ; brouillon 14 produit vers 19:30 ; journal clos à 19:19, le 2026-11-22.
- **Ce que la session rend** : le brouillon 14 (candidat 5), `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon14.md`. **C'est le texte à vérifier et à sceller** ; les brouillons 12 et 13 restent tels quels. Cinq marqueurs restent.

## 1. Pourquoi deux brouillons de plus en une demi-heure

Deux choses sont arrivées en même temps, sans se voir.

- Le contre-lecteur 8 vérifiait le brouillon 12. Son rapport : `prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon12-verification-cl8-v1.md`, `185038defaeca81216a5ea2a3274f06f5f1ee56a3e297881ad4724a16d25d885`, « conforme : scellable après les marqueurs », un mineur restant (r-1).
- Pendant ce temps, Lazar tranchait la garde d'antériorité (`GO-2026-11-22-122`) et la mère me demandait de citer ce GO dans le texte : brouillon 13, écrit avant que le rapport de vérification ne soit poussé.

Le brouillon 14 réunit les deux : il part du brouillon 13 et applique r-1. On n'écrase jamais (R12) : le brouillon 13, déjà scellé par compagnon, n'a pas été refait.

## 2. Ce que le brouillon 14 fait (8 opérations, aucune dans une section gelée)

- **r-1** : dans la déclaration de la référence honnête, la garde du calibrage vaut pour un couple (surveillant décisif ou obligatoire, jeu) ; à 4 alertes ou plus, la ligne F6 ne joue que pour un surveillant décisif ; pour un bras obligatoire, une réserve est écrite avec la phrase de la ligne D retenue. Texte du vérificateur repris tel quel.
- La vérification du brouillon 12 est inscrite dans la section « Contre-lecture », avec son empreinte.
- En-tête, déclaration de vue, vérification des marqueurs.

Ce qui sépare le brouillon 14 du brouillon 12, déclaré conforme : les 12 opérations du brouillon 13 (décision de Lazar) et ces 8. Détail : `couples-t08-brouillon13-v1.json` et `couples-t08-brouillon14-v1.json` ; résumés : différentiels des brouillons 13 et 14, sections 3.

## 3. Programmes et vérifications

- `faire-t08-brouillon14-v1.py` : le programme du brouillon 13 avec le numéro 14. `--verifier` reproduit le brouillon à l'octet ; contrôle du gel tenu ; phrase T5-19 épinglée.
- Programme de scellement : toujours la **version 3**, inchangée ; on lui passe le brouillon 14 et l'empreinte que la vérification finale déclarera conforme.
- `essais-controle-gel-t08-v3.py` : les mêmes essais, sur le brouillon 14 : 27 conformes sur 27.
- Validateur de préenregistrement : seuls les cinq marqueurs restent.

## 4. Écarts et accès

- Lu en plus : le rapport de vérification du brouillon 12, en entier.
- Ma poussée du brouillon 13 a été refusée parce que le vérificateur avait poussé entre-temps ; je n'ai rien forcé : mon commit, jamais poussé, a été reporté sur la tête de la branche.
- Aucun refus d'outil. Aucun registre écrit. Aucun résultat lu.

## 5. Ce qui reste

1. Vérification, par le contre-lecteur 8, de ce qui sépare le brouillon 14 du brouillon 12 (20 opérations, hors des sections gelées) ; son rapport doit citer l'empreinte du brouillon 14.
2. Alignement du code, contre-lecture, commit.
3. Ligne du registre de la mère : confirmation des trois autres gardes de code.
4. Ordre de course, consignes du lecteur et du juge : à écrire les 24 et 25, sur demande de la mère.
5. Scellement par `finaliser-t08-scellement-v3.py`.
