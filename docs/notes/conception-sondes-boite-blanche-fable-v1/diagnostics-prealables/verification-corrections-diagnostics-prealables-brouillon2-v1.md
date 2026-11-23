# Vérification des corrections — diagnostics préalables des sondes, brouillon 2 (v1)

- Le même contre-lecteur, d'un autre modèle que l'auteur ; 2026-11-22 (UTC).
- Empreintes vérifiées : brouillon 2 `caf8d642…88ab5`, erratum 1 `e9c8cde1…f0a1`. Aucun chiffre de résultat dans l'un ni l'autre.

## Verdict

**Scellable après retouches mineures** (R-1 à R-6).

## Remarques

- Levées : B-2, M-1 à M-5, M-7, M-9, M-11 à M-13, m-1 à m-10.
- Levées avec réserve : B-1 (R-1), B-3 (R-2), M-8 (R-4), M-10 (R-2, R-3, R-5).
- Non levées : aucune.

Écarts déclarés, tous défendables :
- B-2 : la règle reste mécanique ; sans contrôle du chemin, seule « non établie » se lit.
- M-6 : sous une trace forte, une direction au hasard non orientée porte une composante constante le long de la trace et sépare aussi, dans un sens ou l'autre ; exiger le dépassement du plancher rendrait « fort » inatteignable.
- M-10 : sept points couverts, sauf R-2 et R-3.

Changements hors contre-lecture : justes.
- Identité isotrope en grande dimension : sa projection sur la trace est presque nulle, le signe de `c_{pq}` suit `τ + σ_I(z_p − z_q)` avec `σ_I` effectif presque nul, et la « trace faible » rendrait « fort » presque toujours.
- Avec `σ_I` le long de la trace, la part attendue est Φ(τ/(σ_I√2)), soit Φ(0,5) : « faible » atteignable, « fort » rare ; retrouvé sur données fabriquées.
- `η` appliqué au seul saboteur rompt un peu l'échangeabilité ; le test reste prudent sur données fabriquées.

Arithmétique : valeur p minimale juste. Mon seuil de première passe était faux pour trois familles (huit paires suffisent), et « testable » est circulaire (R-1).

## Faits de format

- (a) suffit, avec : « les clés de texte propre à un adaptateur sont exclues de `K` ».
- (b) suffit, avec : « la correspondance entre poids et séries vient du fichier fermé des empreintes, ouvert avec la table ».
- (c) suffit si l'attestation cite le commit du programme figé et la précision.
- (d) rien dans le texte ; erratum : R-5.
- Le modèle nu relisant les textes honnêtes, le contrôle d'intensité devient calculable : le dire.
- Aucune ligne non calculable par construction : quatre plis par tâche restent possibles avec une action par tâche ; le minimum d'actions peut manquer, mais se constate par comptage avant ouverture (« effectif insuffisant »). En revanche le nombre de paires n'existe qu'après le verdict : l'épreuve ne peut être jouée « à ces effectifs » avant (R-4).

## Retouches, texte exact

**R-1** (Seuil, étalon). Remplacer « (au moins 7 paires pour une famille seule, 8 pour deux, 9 pour trois ou quatre) » par « (au moins 7 paires pour une famille seule, 8 pour deux ou trois, 9 pour quatre). Le nombre de familles testables se fixe par itération : on part des familles d'au moins 7 paires et on retire celles dont `2^{2−P}` dépasse 0,05 divisé par le nombre restant, jusqu'à stabilité. »

**R-2** (texte, Seuil, rejeu) : remplacer « Elle l'est aussi si » par « Une interaction « établie » ou « contraire » l'est aussi si ». (Erratum § 5) : remplacer « pour une ligne d'interaction, « non interprétable » si » par « pour une ligne d'interaction « établie » ou « contraire », « non interprétable » si ».

**R-3** (erratum § 6) : remplacer « le contrôle d'intensité doit la faire retomber » par « part de « fort » après contrôle d'intensité rendue aussi, sans critère ».

**R-4** (Plan, Ordre, étape 2) : ajouter « Le nombre de paires par famille n'étant connu que par la table de l'ouvreur, l'épreuve de l'étalon de transport est jouée pour chaque nombre de paires de 4 à 16 et pour 1 à 4 familles ; la case qui répond aux effectifs lus après le verdict s'applique, avant toute ouverture des activations. »

**R-5** (erratum, brique A) : ajouter « Le jeton d'avant le champ et les couches 7 et 23 sont facultatifs ; leur absence, déclarée au manifeste, n'est pas une forme inattendue. »

**R-6** (h1, h2, plan) : porter (a), (b), (c) avec leurs compléments, et « contrôle d'intensité calculable : le modèle nu relit les textes honnêtes communs ».

Facultatif (erratum § 6) : saboteur `+η/2`, jumeau `−η/2`.

## Non vérifié

- Résumé d'audit cité pour B-2 : non ouvert.
- Une clé honnête commune se distingue-t-elle d'une clé de texte propre avant la table de l'ouvreur ? Sinon, R-4 vaut aussi pour les tâches et les actions.
