# Réponses du développeur habilité aux demandes v8 de la relance — sans interne — v1

Écrit par le développeur habilité neuf côté moniteurs du bras A, le 20 novembre 2026 (mandat v2, `8c60bfe748b21e7ef3276be7145d8be426dc16ba77323cf71868e61d0c3fc982`). Réponses aux demandes `demandes-au-developpeur-habilite-bras-a-v8.md` (`ba81227f…`), dans la forme bornée de chacune. Aucun seuil, trait, vocabulaire, poids ni texte de consigne de moniteur. Ce qui fonde chaque réponse est dans la pièce interne `docs/notes/bras-a-moniteurs-v1/reponses-developpeur-habilite-demandes-v8-v1.md` (`0cd329f1399165cc6c34fe046443081ea98ddefa8f881bf4ac22fb6757b87bd8`), qui ne sort pas.

Fichiers de la relance ouverts : aucun, hors la pièce des demandes. Aucune version neuve du module n'est écrite : les réponses portent sur la version 8 (`61105129f58f5df590b033c183e7ab334f56a51cc03bb04e86ebdb52e6e53760`).

| demande | réponse |
|---|---|
| 1 | Version qui respecte le cas D : **non écrite** (non établie). Schéma de permutation : **oui** (version 8, sous le réglage « échange par paire »). |
| 2 | **Non** dans la version 8 ; aucune autre version. |
| 3 | **Non** dans la version 8 ; possible dans une version neuve sans changer aucun calcul. |
| 4 | Retirée. |
| 5 | Aucun arrondi ni nombre de décimales fixé : double précision, quotient calculé à partir des comptes de la même lecture. **Oui.** Le module n'écrit pas la sortie sur disque : son écriture, par le lanceur non écrit, est non établie. |
| 6 | (a) **non** ; (b) **non** ; (c) **sans objet** : sous séparation parfaite, l'aire et la valeur p sont déjà rendues. |
| 7 | Rendu quand, pour un moniteur et une dose, les unités lues d'un pli (honnête et dose ensemble) viennent de moins de deux tâches. Aux effectifs conformes : **non**, sauf si les exclusions vident sept des huit tâches d'un pli. |
| 8 | Voir ci-dessous. |
| 9 | `reglages.permutation` : `échange par paire` ; `reglages.unite_de_la_permutation` : `paire d'épisodes de même rang (honnête et dose), dans chaque tâche`. Doses : chaînes `dose-0.25`, `dose-0.50`, `dose-0.75`, `dose-1.00` ; dans `reglages`, `doses_de_la_famille` est la liste des trois dernières et `dose_pour_information` vaut `dose-0.25` ; dans `lectures`, ce sont les clés de premier niveau et la valeur du champ `dose` de chaque lecture. `quantile_borne_haute` : un nombre, ou `null`. `statistique_agregateur` : **(b)**, il nomme le calcul d'un moniteur ; étiquette fixe **pas écrite** (version neuve). |
| 10 | **Table** : clés de dose, puis clés de moniteur (`classifieur-lexical`, `classifieur-de-surface`, `moniteur-boite-noire`, `agregateur-sequentiel`, `juge`). |
| 11 | (a) **oui** ; (b) **oui**. |
| 12 | `dose` : **oui** ; `condition` : **oui** (`honnete` ou la dose de la ligne). `lignes` : un entier, le nombre de lignes du fichier ; `champs` : la liste des dix noms de champs, dans l'ordre du fichier ; `forme` : la chaîne de la forme (`rang`). |
| 13 | **Non.** `piece_source` porte le chemin et l'empreinte d'une autre pièce, que le module réemploie, et non l'empreinte du module ; aucun champ de la sortie de la version 8 ne porte l'empreinte du module. **Le changement demandé n'est pas fait** : il faut une version neuve du module. De plus, ce champ écrit en clair le chemin d'une pièce habilitée. **La demande reste bloquante.** |
| 14 | `effectifs` : **oui** (ou `null` quand un pli n'a aucune unité) ; `exclues` : **oui**. |
| 15 | **Non établi** : le module n'écrit pas sa sortie sur disque ; le lanceur, non écrit, la nommera. |
| 16 | **Non.** |
| 17 | **Non jouée** : à jouer sur la version neuve. |
| 18 | **Non écrit** ; aucune date. |
| 19 | Dossier : **non établi** (un argument de la lecture commune, que fixera la configuration du lanceur). Nombre : **1** sous `src` et `scripts`. **Oui.** |
| 20 | **Non.** À ajouter : le dossier `barreau8_moniteurs` ; et le dossier `bras_a_v2_habilite_preparation` si la garde compare les noms à l'identique plutôt que par préfixe. |
| 21 | Code des deux moniteurs à modèle de langue : `18f63f40` ; extraction pour la base : `94c5dcbc`. |
| 31 | **Un nombre par dose** (ou `null` à une dose où il n'est pas calculable) ; **oui**, de 0 à 1. Le champ entier vaut `null` quand sa statistique est celle que l'agrégateur retient : sa forme dit laquelle est retenue, même sous une étiquette fixe à la demande 9. |
| 32 | Aucun arrondi ni nombre de décimales fixé : double précision. **Oui** (même réserve qu'en 5 sur l'écriture). |

## Demande 8 : chaînes de `motif` (version 8)

`<k>` vaut 0 ou 1 ; `<n>` et `<N>` sont des comptes.

| chaîne | cas |
|---|---|
| `null` | A |
| `pli <k> sans action` | B |
| `aire moyenne : une classe manque dans un pli` | B |
| `pli <k> : classe absente du pli d'apprentissage` | B |
| trois chaînes de plus, propres aux deux moniteurs appris : elles nomment un élément de leur méthode ou un réglage ; non données ; à changer dans la version neuve pour une étiquette de la nature du manque | B |
| `<n> permutations dégénérées sur <N> (plus de 1 %)` | C |
| `<n> tirages dégénérés sur <N> (plus de 1 %) : lecture arrêtée` | D |
| `pli <k> : au moins deux tâches pour un rééchantillonnage` | E |

`calculable` : cas A `true` ; cas D `false` et cas E `false` dans la version 8 ; dans la version de la demande 1 : non établi (pas écrite).

## Chiffrage de la lecture du juge d'une autre lignée (Qwen 2.5 7B Instruct), carte A100 80 Go louée

Rien n'est mesuré pour le juge : tout est en fourchette, sources et hypothèses dans la pièce interne. Bornes hautes : toute action est supposée lue.

| actions | lecture seule, heures de carte | lecture seule, USD | avec mise en place et téléchargement, heures | avec mise en place et téléchargement, USD | pire cas (carte deux fois plus lente, prix plafond) |
|---|---|---|---|---|---|
| 2 560 | 1,9 à 4,3 h | 2,1 à 5,9 USD | 2,4 à 5,3 h | 3,1 à 8,1 USD | 9,6 h, ≈ 14 USD |
| 6 400 | 4,7 à 10,7 h | 5,3 à 14,8 USD | 5,2 à 11,7 h | 6,2 à 17,0 USD | 22,5 h, ≈ 32 USD |

Ce chiffrage ne dépense rien et n'autorise rien.
