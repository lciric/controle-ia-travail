# Réponses du développeur habilité aux demandes v8 de la relance — sans interne — v2

Écrit par le développeur habilité neuf côté moniteurs du bras A, le 20 novembre 2026 (mandat v2, `8c60bfe748b21e7ef3276be7145d8be426dc16ba77323cf71868e61d0c3fc982` ; version 9 du module commandée par la mère sous GO-2026-11-20-21). **Remplace la v1** (`f45625d0a1ce56c142ee23e67439ac3b8dfc2dc5e62a66e245d0c8198fadd59c`), qui reste archivée. Mêmes règles que la v1 : la forme bornée de chaque demande ; aucun seuil, trait, vocabulaire, poids ni texte de consigne de moniteur. Les trois retouches d'exactitude de la lecture habilitée (`lecture-habilitee-reponses-v8-v1.md`, `0f1c410e5548f04d9a674beee50e1b9fb4fd523e99efdc4ad8823ed3c27ccb43`) sont reprises. Ce qui fonde les réponses est dans la notice interne `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-autres-moniteurs-v9-v1.md` (`fe28737d1d2465e7e1280c950a7ba70fafecf774f74ed8476e30d66542002cc4`), qui ne sort pas.

Fichiers de la relance ouverts : aucun, hors la pièce des demandes. Les réponses portent sur la **version 9** du module ; elle n'a pas encore de commit (la mère verse sur la branche) ni de vérification du contre-lecteur.

| demande | réponse |
|---|---|
| 1 | Version : `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v9.py`, `08a8f5c532e350045b0ab8a640525f6f839f47a2a9dc48dad6655b1dec9b13d2` ; commit : pas encore (versement par la mère) ; essais : `tests/test_bras_a_v2_habilite_autres_moniteurs_v9.py`, `b0d505933a7514ff6bc4e2078435280a898134c7725fb2516c93fb208c8cefda`. Schéma de permutation : **oui** (réglage « échange par paire »). |
| 2 | **Oui**, dans la version 9. |
| 3 | **Oui**, dans la version 9 : au cas C, l'aire et les aires des deux plis sont rendues. |
| 4 | Retirée. |
| 5 | Aucun arrondi ni nombre de décimales fixé : double précision, quotient calculé à partir des comptes de la même lecture. **Oui** : le module écrit sa sortie lui-même, en JSON, chaque nombre à son écriture décimale la plus courte, et exige que la relecture rende la même sortie. |
| 6 | (a) **non** ; (b) **non** ; (c) **sans objet** : sous séparation parfaite, l'aire et la valeur p sont déjà rendues. |
| 7 | Rendu quand, pour un moniteur et une dose, les unités lues d'un pli (honnête et dose ensemble) viennent de moins de deux tâches. Aux effectifs conformes : **non**, sauf si, dans sept des huit tâches d'un pli, aucune unité de l'honnête ni de la dose n'est lue. Le module compte ce cas et ne s'arrête pas. |
| 8 | Voir ci-dessous. |
| 9 | `reglages.permutation` : `échange par paire` ; `reglages.unite_de_la_permutation` : `paire d'épisodes de même rang (honnête et dose), dans chaque tâche`. Doses : chaînes `dose-0.25`, `dose-0.50`, `dose-0.75`, `dose-1.00` ; dans `reglages`, `doses_de_la_famille` est la liste des trois dernières et `dose_pour_information` vaut `dose-0.25` ; dans `lectures`, ce sont les clés de premier niveau et la valeur du champ `dose` de chaque lecture. `quantile_borne_haute` : un nombre au cas A, `null` sinon. `statistique_agregateur` : **(b)** ; étiquette fixe, écrite à chaque livraison : `statistique de l'agrégateur fixée par la configuration scellée du lanceur`. Clés de `reglages`, dans l'ordre : `n_permutations`, `n_tirages`, `taille_de_la_famille`, `niveau`, `statistique_agregateur`, `doses_de_la_famille`, `dose_pour_information`, `permutation`, `unite_de_la_permutation`. |
| 10 | **Table** : clés de dose, puis clés de moniteur (`classifieur-lexical`, `classifieur-de-surface`, `moniteur-boite-noire`, `agregateur-sequentiel`, `juge`). |
| 11 | (a) **oui** ; (b) **oui**. |
| 12 | `dose` : **oui** ; `condition` : **oui** (`honnete` ou la dose de la ligne). `lignes` : un entier, le nombre de lignes du fichier ; `champs` : la liste des dix noms de champs, dans l'ordre du fichier ; `forme` : la chaîne de la forme (`rang`). |
| 13 | **Oui**, dans la version 9. Le champ **`piece_source.sha256`** porte l'empreinte entière du module qui a produit la livraison, calculée sur son fichier au moment de la lecture. `piece_source.production` porte en outre, pour chacun des deux moniteurs à modèle de langue, les empreintes des deux programmes qui ont produit ses scores, prises dans le manifeste de production, qui les porte désormais. `piece_source` n'écrit plus aucun chemin. |
| 14 | `effectifs` : **oui** (ou `null` quand un pli n'a aucune unité) ; `exclues` : **oui**. |
| 15 | `lecture-commune-moniteurs-bras-a.json` |
| 16 | **Oui.** Épreuve par retrait : `docs/notes/bras-a-moniteurs-v1/epreuve-par-retrait-autres-moniteurs-v9-v1/mutations-v9-resultats.md`, `195dc56cd0610b9242748f2aa0e4271152b5a02256fc5fbb44a3480d91546f23`. Notice : celle de l'en-tête. |
| 17 | **Oui**, jouée sur la version 9 : sorties ci-dessous. Chacune porte, dans les deux champs de la demande 31, un seul nombre par dose, aux quatre doses. |
| 18 | **Non écrit** ; aucune date. |
| 19 | Dossier : **non établi** — celui que fixera la configuration du lanceur ; le module exige qu'il soit disjoint du dossier de la sortie (ni l'un dans l'autre). Nombre : **2** sous `src` et `scripts` (les versions 8 et 9 du module), plus un script d'épreuve qui l'écrit par le module. **Oui.** |
| 20 | **Non.** À ajouter : le dossier `barreau8_moniteurs` ; et le dossier `bras_a_v2_habilite_preparation` si la garde compare les noms à l'identique plutôt que par préfixe. |
| 21 | Code des deux moniteurs à modèle de langue : `18f63f40` ; extraction pour la base : `94c5dcbc`. |
| 31 | **Un nombre par dose** (ou `null` à une dose où il n'est pas calculable) ; **oui**, de 0 à 1. Dans la version 9, les deux champs sont toujours remplis, quelle que soit la statistique retenue. |
| 32 | Aucun arrondi ni nombre de décimales fixé : double précision. **Oui** (comme en 5). |

## Demande 8 : chaînes de `motif` (version 9)

Liste fermée : toute autre chaîne arrête la lecture. `<k>` vaut 0 ou 1 ; `<n>` et `<N>` sont des comptes, égaux à ceux de la lecture.

| chaîne | cas |
|---|---|
| `null` | A |
| `pli <k> sans action` | B |
| `aire moyenne : une classe manque dans un pli` | B |
| `pli <k> : classe absente du pli d'apprentissage` | B |
| `pli <k> : moniteur appris non ajustable` | B |
| `<n> permutations dégénérées sur <N> (plus de 1 %)` | C |
| `<n> tirages dégénérés sur <N> (plus de 1 %) : lecture arrêtée` | D |
| `pli <k> : au moins deux tâches pour un rééchantillonnage` | E |

`calculable` : cas A `true` ; cas D `true` ; cas E `true` (aux cas B et C, `false`). Au cas B, les deux comptes de permutations sont toujours `null`.

## Demande 17 : sorties de l'épreuve de forme

Scores construits à la main, sans moniteur ni épisode réel ; 2 000 permutations, 2 000 tirages, échange par paire. Au cas C, les permutations perdues sont injectées par l'épreuve. Chemins sous `docs/notes/bras-a-moniteurs-v1/epreuve-de-forme-v9-v1/` ; chaque fichier a son compagnon `.sha256`.

| sortie | chemin | empreinte |
|---|---|---|
| cas A | `cas-a/lecture-commune-moniteurs-bras-a.json` | `009a34e4f44a8ff157af2c88ad75daca90199f0891ef2b488fb8db090bf36972` |
| cas B | `cas-b/lecture-commune-moniteurs-bras-a.json` | `529666dfb07921fc55c22af164a2e693d034f0e6bd001689cc6184a16cb1f99d` |
| cas C | `cas-c/lecture-commune-moniteurs-bras-a.json` | `0c7355e82c91c9f69fab2375737fd13a73d10311104f42078357a987576d02c9` |
| cas D | `cas-d/lecture-commune-moniteurs-bras-a.json` | `69b589366ba9aaac52a32e9cb213cdc44ad8ff89c93efb718830009758397554` |
| cas E | `cas-e/lecture-commune-moniteurs-bras-a.json` | `8c66905660c377ed66944f7ebde753087735834188157a8e39fd9fcbde214432` |
| cas A, une valeur p haute arrondie à quatre décimales (à refuser) | `artefact-cas-a-valeur-p-arrondie/lecture-commune-moniteurs-bras-a.json` | `7d5eb9c96d4c76ab3eda91428c92e4a62e299004e7678accbad484ee7b0b88c7` |

## Chiffrage de la lecture du juge d'une autre lignée (Qwen 2.5 7B Instruct), carte A100 80 Go louée

Rien n'est mesuré pour le juge : tout est en fourchette, sources et hypothèses dans la pièce interne des réponses v1. Le prix plafond de la carte est repris d'une ligne d'accord révoquée ; aucun accord en vigueur ne couvre cette dépense. La mise en contexte de chaque lot de génération, que la v1 ne comptait pas, est comptée ici (4 à 7 % de plus, selon la lecture habilitée). Bornes hautes : toute action est supposée lue.

| actions | lecture seule, heures de carte | lecture seule, USD | avec mise en place et téléchargement, heures | avec mise en place et téléchargement, USD | pire cas (carte deux fois plus lente, prix plafond) |
|---|---|---|---|---|---|
| 2 560 | 1,95 à 4,6 h | 2,2 à 6,4 USD | 2,4 à 5,6 h | 3,1 à 8,6 USD | 10,2 h, ≈ 15 USD |
| 6 400 | 4,9 à 11,5 h | 5,5 à 15,9 USD | 5,4 à 12,5 h | 6,4 à 18,1 USD | 24,1 h, ≈ 34 USD |

Ce chiffrage ne dépense rien et n'autorise rien.
