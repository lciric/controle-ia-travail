# Contre-lecture, tour 3 (différentiel) — préenregistrement du crible (i), placebo par monde jumeau, brouillon 3

- Lecteur : sous-agent neuf, modèle C (je n'ai écrit aucune des pièces ; pièce du modèle A, correction d'un rédacteur d'un autre modèle). Rédigé le 2026-11-17T02:02Z (`date -u`).
- Pièce lue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-i-brouillon3.md`, `888fb001c4d349d8f9d65d91dcfce4c6ee6a0753108973393d75815778f05cbe` (empreinte recalculée, égale ; `scellement verifier` : OK ; `controle_ia.prereg.problemes` sur le fichier : liste vide).
- Pièces comparées : brouillon 2 (`30b3c945…`, égale) ; rapport du tour 2 (`3bda9479…`, égale) ; programme `appliquer-corrections-crible-i-brouillon3.py` (`06f63860…`, égale à celle que la pièce cite, scellé OK) ; différentiel `diff-crible-i-b2-vers-b3.txt` (`8861719a…`, scellé OK).
- Non lu : tout ce qui est interdit (verdict du pilote compris). Aucune machine, aucun appel, aucune dépense.

## Verdict : « scellable »

Aucune correction exigée. Le couple m7 est appliqué fidèlement, le différentiel ne contient rien d'autre que ce que la pièce déclare, la symétrie des trois bras à l'étage 2 est rétablie.

## 1. Fidélité de m7 et différentiel

- `diff` brouillon 2 → brouillon 3 relu en entier : 6 blocs seulement. Q1 titre (« brouillon 3 ») ; Q2 ligne d'en-tête ajoutée (heure 01:48:42Z : concorde avec la date de modification du fichier sur disque) ; Q3 statut ; Q4 validateur ; **m7** (une seule ligne de l'étage 2) ; Q5 section « Contre-lecture » (entrée « Contre-lecture 2 », « À faire » du tour 3). Rien d'autre ne change : aucun chiffre, aucune prédiction, aucun seuil, aucun devis, aucune liste d'arrêt. Le différentiel scellé est identique à un `diff -u` régénéré (comparaison vide).
- m7 : la ligne de l'étage 2 contient exactement le « nouveau » du rapport (ajout « et la phrase « rien d'établi » est remplacée par « non tranché (TJ tronqué) » (la même perte dégonfle P2) »), le reste de la ligne (TV, S0) intact au caractère près. Le programme lit le couple dans le rapport, le compare à une copie, vérifie les empreintes, l'unicité de chaque « ancien » dans le brouillon 2, refuse d'écraser ; il est cohérent avec ce que j'observe.
- Les cinq couples de forme sont déclarés dans la pièce (Q1 à Q5) ; leur contenu est exact : empreintes citées (`30b3c945…`, `3bda9479…`, `06f63860…`) égales aux fichiers.

## 2. Vérifications refaites

- **Symétrie de l'étage 2** (point prioritaire de la pièce) : TV tronqué dégonfle P1 → phrases (b) et (d) remplacées ; S0 tronqué gonfle P2 → (b) et (c) interdites ; TJ tronqué gonfle P1 (→ (a), (c) interdites) et dégonfle P2 (→ (d) remplacée, (a) déjà interdite). Le cas (b) sous TJ tronqué reste permis : P2 établi malgré une perte qui le dégonfle, P1 non établi malgré une perte qui le gonfle : robuste. Idem (a) sous TV tronqué et (d)/(a) sous S0. Les trois bras sont traités de la même façon ; l'étage 3 et « Lecture de H-i » n'ont pas de phrase restée sans traitement. Le raisonnement de la pièce (section « Contre-lecture », m7) est exact.
- **Cohérence étages 0 à 4 et liste d'arrêt** : inchangées ; aucune ligne sans verdict.
- **Devis, enveloppe, durée** : non touchés (attendu 16,80 ; pire 127,00 ; crédits 124,00 et hors crédits 3,00 séparés ; 601,67 sous 1 275 ; durée 12,5 h à un monde à la fois, sous 17 h). Aucun appel, aucune dépense par la correction.
- **R1, R3, R4** : toujours complets, non dérangés. **Fidélité à la note** : sept écarts déclarés, aucun nouveau. **Lectures interdites, identifiants de modèle** : recherche par motifs dans la pièce : aucun ; rien d'interdit ouvert par moi.

## 3. Corrections exigées

Aucune.

## 4. Remarques facultatives (aucune correction exigée)

- Étage 4 (inverses) : sous « TV tronqué », « la table du jumeau trompe » peut venir de la perte ; sous « TJ tronqué » ou « S0 tronqué », « la table distrait » aussi. L'étage 4 ne fait qu'ajouter une réserve et l'étage 2 impose déjà de rapporter P1 et P2 sous réserve : aucun effet sur un verdict ; mention explicite possible dans la version qui fera foi.
- Toujours à trancher avant la version qui fera foi (la pièce le dit) : F1, F4, F5, F7 du tour 1 ; calcul de puissance à + 4 mondes à refaire par un programme scellé sous un nom neuf.

## 5. Points pour la session mère

1. La pièce peut être scellée comme texte qui fait foi pour sa conception ; il reste, côté mère, ce que la pièce dit : ligne datée de `registres/decisions.md` confirmant le gel des prédictions I-1 à I-8 (I-1 gelée avec « ≥ + 4 » même si P1 ne peut l'établir à ce seuil ; zones de I-5, I-6, I-7 ajoutées après le gel), choix F1, F4, F5, F7, calcul scellé de la puissance à + 4 mondes.
2. Nœud de Lazar : enveloppe des cinq cribles (environ 1 327,67 contre 1 275 aux chiffres de la note pour (ii) et (iv)), sauf devis refaits plus bas ; GO par ligne (124 USD sur crédits, 3 USD hors crédits) avant toute dépense.
3. Aucun écart à un texte scellé, aucun risque nouveau.

## 6. Incidents de ma main

Un premier essai du validateur a échoué par mon erreur (texte passé au lieu du chemin), sans écriture ni effet ; relancé avec le chemin : liste vide. Aucun autre incident ; aucun fichier écrit hors ce rapport et son empreinte ; aucun commit ; aucune pièce modifiée.
