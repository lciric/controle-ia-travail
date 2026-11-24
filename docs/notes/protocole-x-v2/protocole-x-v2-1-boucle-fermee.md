# Protocole X, version 2.1 : trois garde-fous de la boucle fermée (24 novembre 2026)

**Décision** : mot de Lazar tapé vers 2026-11-24T19:17:52Z : « Option (a), les trois maintenant go », sur la proposition de la mère qui compare la boucle fermée aux expérimentateurs de l'organisme complet (conception `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md`, § 2.1 et § 2.3). Ligne GO-2026-11-24-45.

**Portée** : ce texte complète la règle 1 de la version 2 (`docs/notes/protocole-x-v2/protocole-x-v2.md`, 52ec6b9e…), qui reste en vigueur sur tout le reste. En cas de conflit sur la règle 1, il prime.

## Règle 1, complétée

1 a. **Le critère de mort n'appartient à aucun lecteur.** Le lecteur de la note propose l'épreuve la moins chère d'une proposition retenue : ce qu'elle mesure, son coût, sa date. Le critère de mort, lui, est écrit par un concepteur distinct des lecteurs et des proposeurs, puis scellé avant toute donnée. Ce concepteur est Claude Fable 5.2 ; tant que son quota est gelé (jusqu'au 2 décembre), c'est un Opus 5.5 neuf, écart déclaré. Quand l'épreuve est décisive, le critère passe par un préenregistrement (R1, R2).

1 b. **Une épreuve doit pouvoir tuer.** Avant de compter, toute épreuve est jouée sur au moins un témoin faux connu, qui doit y mourir, et, si possible, sur un témoin vrai connu, qui doit y tenir. Une épreuve qui laisse vivre son témoin faux est déclarée « épreuve morte » : aucune issue n'est lue, l'arrêt est rapporté, il n'y a pas de repli.

1 c. **La sélection par lecture est elle-même mesurée.** Pour chaque dossier, une proposition non retenue est tirée au hasard par graine (`numpy.random.SeedSequence`, graine inscrite avant le tirage) et éprouvée comme les retenues, quand son épreuve la moins chère coûte peu : processeur, ou moins de 5 dollars payés. Sinon, le tirage et sa raison sont inscrits. L'audit compare la survie des retenues et des tirées.

## Ce qui change dans les dossiers en cours

- Boucle fermée du collisionneur groupé (GO-2026-11-24-46) : 1 a, 1 b et 1 c dès maintenant.
- Collisionneur sur l'attelage (lancé en version 1) : 1 a et 1 b à sa table d'épreuves ; 1 c si une épreuve de proposition non retenue tient sur processeur.
- Banc du détecteur séquentiel : son plan est déjà écrit par Fable, distinct des lecteurs (1 a tenu) ; son contrôle de banc (la construction naïve doit échouer) tient lieu de 1 b.
