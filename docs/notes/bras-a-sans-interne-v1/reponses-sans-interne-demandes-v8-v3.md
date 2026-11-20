# Réponses du développeur habilité aux demandes v8 de la relance — sans interne — v3

Écrit par le développeur habilité neuf côté moniteurs du bras A, le 20 novembre 2026 (mandat v2, `8c60bfe748b21e7ef3276be7145d8be426dc16ba77323cf71868e61d0c3fc982` ; versions 9 et 10 du module commandées par la mère sous GO-2026-11-20-21). **Remplace la v2** (`1959a0be4d74c7039a6e72d04f53bb4f57ca71545050d0d70bd6f0e6e6b7b9f7`), qui reste archivée, comme la v1. Mêmes règles : la forme bornée de chaque demande ; aucun seuil, trait, vocabulaire, poids ni texte de consigne de moniteur. Les retouches d'exactitude des deux lectures habilitées sont reprises (`lecture-habilitee-reponses-v8-v1.md`, `0f1c410e5548f04d9a674beee50e1b9fb4fd523e99efdc4ad8823ed3c27ccb43` ; `contre-lecture-habilitee-autres-moniteurs-v9-v1.md`, `517fecb3a04f4d67de2155ef9ed21c231856c889c2465544cd2450ea8a58c25e`). Ce qui fonde les réponses est dans les notices internes des versions 9 (`fe28737d1d2465e7e1280c950a7ba70fafecf774f74ed8476e30d66542002cc4`) et 10 (`docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-autres-moniteurs-v10-v1.md`, `3bb1c02de6039c66cbc3274f74009962588572f9224973d62ead7a6a00667784`), qui ne sortent pas.

Fichiers de la relance ouverts : aucun, hors la pièce des demandes. **Correction de la v2** : la version 9 a un commit, `92842ac54`, et elle est contre-lue (« conforme après corrections de forme »). Les réponses portent désormais sur la **version 10**, qui fait ces corrections de forme sans changer aucun calcul ; elle n'a pas encore de commit (la mère verse sur la branche) ni de vérification de ses corrections par le contre-lecteur.

| demande | réponse |
|---|---|
| 1 | Version : `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v10.py`, `42c78bd5b10e970d98adf2b388f290d92e79d0a62b3de82937c91bb70949bd6c` ; commit : pas encore (versement par la mère) ; essais : `tests/test_bras_a_v2_habilite_autres_moniteurs_v10.py`, `75ef245065ae8407eed36d50290e3ffbef4065de6462e0830f41b5efda374537`. La version 9 (`08a8f5c532e350045b0ab8a640525f6f839f47a2a9dc48dad6655b1dec9b13d2`, commit `92842ac54`) avait la même forme des lectures ; la version 10 ferme la forme de deux autres champs de la sortie. Schéma de permutation : **oui** (réglage « échange par paire »). |
| 2 | **Oui**, dans les versions 9 et 10. |
| 3 | **Oui**, dans les versions 9 et 10 : au cas C, l'aire et les aires des deux plis sont rendues. |
| 4 | Retirée. |
| 5 | Aucun arrondi ni nombre de décimales fixé : double précision, quotient calculé à partir des comptes de la même lecture. **Oui** : le module écrit sa sortie lui-même, en JSON, chaque nombre à son écriture décimale la plus courte, et exige que la relecture rende la même sortie. |
| 6 | (a) **non** ; (b) **non** ; (c) **sans objet** : sous séparation parfaite, l'aire et la valeur p sont déjà rendues. |
| 7 | Rendu quand, pour un moniteur et une dose, les unités lues d'un pli (honnête et dose ensemble) viennent de moins de deux tâches. Aux effectifs conformes : **non**, sauf si, dans sept des huit tâches d'un pli, aucune unité de l'honnête ni de la dose n'est lue. Le module compte ce cas et ne s'arrête pas. |
| 8 | Voir ci-dessous. |
| 9 | `reglages.permutation` : `échange par paire` ; `reglages.unite_de_la_permutation` : `paire d'épisodes de même rang (honnête et dose), dans chaque tâche`. Doses : chaînes `dose-0.25`, `dose-0.50`, `dose-0.75`, `dose-1.00` ; dans `reglages`, `doses_de_la_famille` est la liste des trois dernières et `dose_pour_information` vaut `dose-0.25` ; dans `lectures`, ce sont les clés de premier niveau et la valeur du champ `dose` de chaque lecture. `quantile_borne_haute` : un nombre au cas A, `null` sinon. `statistique_agregateur` : **(b)** ; étiquette fixe, écrite à chaque livraison : `statistique de l'agrégateur fixée par la configuration scellée du lanceur`. Clés de `reglages`, dans l'ordre : `n_permutations`, `n_tirages`, `taille_de_la_famille`, `niveau`, `statistique_agregateur`, `doses_de_la_famille`, `dose_pour_information`, `permutation`, `unite_de_la_permutation`. |
| 10 | **Table** : clés de dose, puis clés de moniteur (`classifieur-lexical`, `classifieur-de-surface`, `moniteur-boite-noire`, `agregateur-sequentiel`, `juge`). |
| 11 | (a) **oui** ; (b) **oui**. |
| 12 | `dose` : **oui** ; `condition` : **oui** (`honnete` ou la dose de la ligne). `lignes` : un entier, le nombre de lignes du fichier ; `champs` : la liste des dix noms de champs, dans l'ordre du fichier ; `forme` : la chaîne de la forme (`rang`). |
| 13 | **Oui**, dans les versions 9 et 10. Le champ **`piece_source.sha256`** porte l'empreinte entière du module qui a produit la livraison, calculée sur son fichier au moment de la lecture. `piece_source.production` porte en outre, pour chacun des deux moniteurs à modèle de langue, les empreintes des deux programmes qui ont produit ses scores, prises dans le manifeste de production, qui les porte désormais. `piece_source` n'écrit plus aucun chemin. |
| 14 | `effectifs` : **oui** (ou `null` quand un pli n'a aucune unité) ; `exclues` : **oui**. |
| 15 | `lecture-commune-moniteurs-bras-a.json` |
| 16 | **Oui**, pour la version 10. Épreuve par retrait : `docs/notes/bras-a-moniteurs-v1/epreuve-par-retrait-autres-moniteurs-v10-v1/mutations-v10-resultats.md`, `d8eef9e2f5aedecf647bf02de75411897f779ca35ffd577a106d30583a9dd0aa`. Notice : celle de la version 10, à l'en-tête. |
| 17 | **Oui**, refaite sur la version 10, à la forme d'une vraie livraison (le fichier par unité porte les cinq moniteurs, l'agrégateur à l'unité de l'épisode ; comptes et preuve d'ordre faits par le module) : sorties ci-dessous ; elles remplacent celles de la v2. Chacune porte, dans les deux champs de la demande 31, une seule valeur par dose, aux quatre doses : un nombre, ou `null` au cas B, où l'aire n'est pas calculable. |
| 18 | **Non écrit** ; aucune date. |
| 19 | Dossier : **non établi** — celui que fixera la configuration du lanceur ; le module exige qu'il soit disjoint du dossier de la sortie (ni l'un dans l'autre). Nombre : **3** sous `src` et `scripts` (les versions 8, 9 et 10 du module), plus deux scripts d'épreuve qui l'écrivent par le module. **Oui.** |
| 20 | **Non.** À ajouter : le dossier `barreau8_moniteurs` ; et le dossier `bras_a_v2_habilite_preparation` si la garde compare les noms à l'identique plutôt que par préfixe. |
| 21 | Code des deux moniteurs à modèle de langue : `18f63f40` ; extraction pour la base : `94c5dcbc`. |
| 31 | **Un nombre par dose** (ou `null` à une dose où il n'est pas calculable) ; **oui**, de 0 à 1. Dans les versions 9 et 10, les deux champs sont toujours remplis, quelle que soit la statistique retenue. |
| 32 | Aucun arrondi ni nombre de décimales fixé : double précision. **Oui** (comme en 5). |

## Demande 8 : chaînes de `motif` (versions 9 et 10)

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

`calculable` : cas A `true` ; cas D `true` ; cas E `true` (aux cas B et C, `false`). Au cas B, les deux comptes de permutations sont toujours `null`. Au cas A, la borne haute est un nombre de 0 à 1.

## Forme fermée de deux champs de la sortie (version 10)

- `comptes_des_lectures` : pour chacun des deux moniteurs à modèle de langue (`moniteur-boite-noire`, `juge`) et chacune des cinq conditions lues, exactement les clés `lectures`, `balise`, `jointure`, `masse_faible`, `sans_score`, dans cet ordre ; `lectures`, `masse_faible` et `sans_score` sont des entiers ; `balise` et `jointure` sont des tables d'entiers dont les clés sont prises dans les deux listes fermées des états de la balise et des jointures.
- `preuve_d_ordre` : pour chacun des cinq moniteurs, `date` (au format `AAAA-MM-JJTHH:MM:SSZ`) et `empreinte_des_scores` (soixante-quatre signes hexadécimaux pour les trois moniteurs lus sur des scores, `null` pour les deux classifieurs) ; puis `engagement_de_la_table` (soixante-quatre signes hexadécimaux).

## Demande 17 : sorties de l'épreuve de forme

Scores construits à la main, sans moniteur ni épisode réel ; 2 000 permutations, 2 000 tirages, échange par paire ; fichier par unité en rangs, cinq moniteurs. Au cas C, les permutations perdues sont injectées par l'épreuve. Chemins sous `docs/notes/bras-a-moniteurs-v1/epreuve-de-forme-v10-v1/` ; chaque fichier a son compagnon `.sha256` ; les fichiers par unité sont sous `unites-cas-*/`.

| sortie | chemin, sous `docs/notes/bras-a-moniteurs-v1/epreuve-de-forme-v10-v1/` | empreinte | lignes du fichier par unité |
|---|---|---|---|
| cas A | `cas-a/lecture-commune-moniteurs-bras-a.json` | `665ec2343cca430e078a2dbc3a2597517e063111ab7c8a745528a523283c4737` | 8 192, cinq moniteurs |
| cas B | `cas-b/lecture-commune-moniteurs-bras-a.json` | `1acc3688d8ca029134bd582ac78309400cd45464ba0483cf9328f9943e27de92` | 6 144, cinq moniteurs |
| cas C | `cas-c/lecture-commune-moniteurs-bras-a.json` | `444d640cbf3460f4eece57e1b29b6b362ef81e37a1183440d69dedf8294239f4` | 8 192, cinq moniteurs |
| cas D | `cas-d/lecture-commune-moniteurs-bras-a.json` | `ba19720b294f9f8711b85ea0666a5dcf2f2d88a1b3a238bdfae6ac9414dd3053` | 1 536, cinq moniteurs |
| cas E | `cas-e/lecture-commune-moniteurs-bras-a.json` | `609faf0508e80b25f531fd4ec54191757e6308ed0138774b2f56c0675ed1a6bd` | 1 024, cinq moniteurs |
| cas A, une valeur p haute arrondie à quatre décimales (à refuser) | `artefact-cas-a-valeur-p-arrondie/lecture-commune-moniteurs-bras-a.json` | `33249e747607aeb5fd07538d1a2423a4e6f069767631295557dca59ca6aae47e` | celui du cas A |

## Chiffrage de la lecture du juge d'une autre lignée (Qwen 2.5 7B Instruct), carte A100 80 Go louée

Rien n'est mesuré pour le juge : tout est en fourchette, sources et hypothèses dans la pièce interne des réponses v1. Le prix plafond de la carte est repris d'une ligne d'accord révoquée ; aucun accord en vigueur ne couvre cette dépense. La mise en contexte de chaque lot de génération, que la v1 ne comptait pas, est comptée ici (4 à 7 % de plus, selon la lecture habilitée). Bornes hautes : toute action est supposée lue.

| actions | lecture seule, heures de carte | lecture seule, USD | avec mise en place et téléchargement, heures | avec mise en place et téléchargement, USD | pire cas (carte deux fois plus lente, prix plafond) |
|---|---|---|---|---|---|
| 2 560 | 1,95 à 4,6 h | 2,2 à 6,4 USD | 2,4 à 5,6 h | 3,1 à 8,6 USD | 10,2 h, ≈ 15 USD |
| 6 400 | 4,9 à 11,5 h | 5,5 à 15,9 USD | 5,4 à 12,5 h | 6,4 à 18,1 USD | 24,1 h, ≈ 34 USD |

Ce chiffrage ne dépense rien et n'autorise rien.
