# Vérification des corrections du code v3 du barreau 5 — v1

Écrite le 23 novembre 2026 par le contre-lecteur du code v3 (Claude Opus 5.5), sous-agent du conducteur. Passe courte. Rien commité, rien poussé, rien de payant.

**Objet** : le commit `423496d4b8ee5c19d1849545bdba659e9c9c7e0c`, enfant de `9e682f0e` (branche `course/barreau5-commande-lecture-v3`, récupérée par son nom entier).

## Verdict

**Conforme.** Les constats 1 et 2 sont fermés. La réserve 3 est tranchée par le conducteur : la parité entière tourne chez le développeur.

## Ce qui a été vérifié

- **Un seul fichier touché.** De `9e682f0e` à `423496d4`, seul `tests/test_commande_lecture_v3.py` change (sha256 `fa4858b397190cc5286fff8acbd4224b81d4f5908b88b9f74faa7794b6ee74f4`, recalculé, égal à l'attendu).
- **Sept ajouts, rien d'autre.** De `5402367e` à `423496d4`, on trouve sept lignes « A », en mode 100644. Les modules et les lanceurs ont les mêmes objets git qu'au commit `9e682f0e` (`3c135c9d9`, `8d2d7f6c1`, `75e0dbea5`, `f2b61536e`) : ils sont inchangés à l'octet, tout comme l'essai d'identification (`44aa57eff`) et l'essai d'ouverture (`bf1755a5a`).
- **Constat 1.** `test_d_prime_ligne_saine_plus_une_variante_normalisee_deux_candidates` joue trois cas : forme décomposée, espace insécable, « | » en tête. La variante vient avant ou après la ligne saine, et l'essai exige le motif « une et une seule ». Il a un témoin sain.
- **Constat 2.**
  - Le module : `test_amorce_embarquee_sha256_deux_segments_base64_refus` joue deux commandes à deux segments, dont l'un vise un autre fichier, dans les deux ordres, et exige le refus. Il a un témoin à un seul segment.
  - Le lanceur : le cas `deux_lignes` imprime la commande saine suivie d'une seconde ligne, et l'essai exige le refus. Le témoin existant passe.
- **Le fichier d'essais au commit `423496d4`** : 82 passés.

## Mes mutations, rejouées sur `423496d4`

Les cinq mutations restées vertes au premier passage passent toutes au rouge. Les fichiers sont rendus à l'octet, et l'arbre est propre après la campagne.

| N° | Mutation | Issue |
|---|---|---|
| M3 | candidate sans forme composée | attrapée |
| M4 | candidate sans espaces ramenées | attrapée |
| M5 | candidate sans « \| » | attrapée |
| M8 | compte de « base64 -d » retiré du module | attrapée |
| M9 | « une seule ligne de sortie » retirée du lanceur | attrapée |

Mes dossiers jetables (l'arbre de travail détaché et les dossiers temporaires des essais) sont effacés après usage.
