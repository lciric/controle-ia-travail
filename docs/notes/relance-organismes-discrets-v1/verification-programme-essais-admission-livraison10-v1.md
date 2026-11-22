# Vérification du programme des essais d'admission — livraison 10 (noms `_v9`, mutations v5) — v1

Contre-lecteur de code neuf (Claude Opus 5.5), qui n'a pas écrit ce code. Rien n'est scellé ici.

## Verdict

**Le code est sain, mais Google n'est pas engageable avec GO-2026-11-21-88 tel qu'il est écrit sur main.** La garde lit la vraie ligne du registre et la refuse, pour deux raisons :

1. sa colonne « par » vaut « mère sous GO-2026-11-21-69 » et non « Lazar » ;
2. elle écrit « **Exemption de la sonde** », avec une majuscule, alors que la garde cherche « exemption de la sonde » en minuscules ; aucune autre cellule ne contient la marque.

Le refus est conforme à la règle écrite par la note v9. Le défaut est dans la ligne du registre, non dans le chef.

Ce qu'il faut : une ligne de décision accordée par Lazar, qui cite « exemption de la sonde » en minuscules, échéance au 30 novembre. La forme de la section 2 de la note v9 convient. D'ici là, GO-2026-11-21-69 n'est admis que jusqu'au 22 novembre inclus.

Le refus d'une fiche sans limite de sortie et la campagne de mutations sont conformes.

## 1. Empreintes, essais, mutations

- Les six fichiers `_v9`, la note v9 et les deux outils de mutation v5 concordent avec leurs compagnons. Les empreintes des outils sont aussi celles de la note.
- Les essais `tests/test_chef_essais_admission_bras_a_v9.py`, lancés sans clé, donnent **240 réussis**.
- J'ai rejoué toute la campagne v5. Résultat : **573 mutants, 573 tués**, 0 survivant, 0 erreur, code 0. La campagne de la livraison 10 tue tous ses mutants : 7 sur la lecture de la fiche du modèle, 10 sur la limite lue dans les relevés, 35 sur le contrôle du GO de l'exemption.
- Le survivant déclaré par le rédacteur (garde 8, accord le jour même, `>` changé en `>=`) est tué par le cas ajouté. Il ne cachait pas de défaut du chef : il ne tenait qu'à la date où tournaient les essais.

## 2. Refus quand la limite de sortie manque (question 1)

J'ai écrit des essais jetables, hors du dépôt : 12 essais, 12 réussis.

- **Vérifications de clé**, au faux fournisseur, à 65 536, pour les deux clés. La fiche est lisible mais sans `outputTokenLimit`. Aucun appel ne part après l'appel de liste gratuit, la dépense comptée est nulle, et la ligne est close.
- **File du juge.** Configuration définitive, avec un relevé dont la dernière fiche est sans limite. `gardes_avant_depart` refuse au contrôle des relevés de vérification, avant tout envoi. Le cas sain (deux relevés à 65 536) passe et recopie les limites au contexte.

## 3. GO de l'exemption de la sonde (question 2)

Contrôle joué sur le registre réel (`git show origin/main:registres/go.md`, main à 4cd1092c3) :

| ligne | jour | issue |
|---|---|---|
| GO-2026-11-21-88, réelle | 2026-11-22 | **refusée** : « n'est pas accordée par Lazar » |
| GO-2026-11-21-88, colonne « par » mise à « Lazar » | 2026-11-22 | **refusée** : « ne cite pas « exemption de la sonde » » (majuscule) |
| GO-2026-11-21-88, à la forme de la note v9, par Lazar | 22 au 30 novembre | admise ; refusée le 1er décembre |
| GO-2026-11-21-69, réelle | 2026-11-22 jusqu'à 23:59Z | admise |
| GO-2026-11-21-69, réelle | 2026-11-23 00:00Z | refusée, échue |

Artefacts, tous refusés : une ligne échue, une ligne de type `calcul`, une ligne sans la marque, et une ligne dont la marque porte une majuscule.

**Réserve.** La colonne du plafond de GO-2026-11-21-69 borne l'autonomie à 2026-11-22T05:30Z, mais le chef n'en lit que l'échéance au jour, et admet GO-69 tout le 22. Cette réserve ne bloque pas si une ligne de Lazar remplace GO-69 avant tout départ.

**Recommandation.** Rendre la recherche de la marque insensible à la casse. Ce n'est pas bloquant, mais elle refuse aujourd'hui la seule vraie ligne.

## 4. Configuration définitive de Google de la note v9, à blanc (question 4)

J'ai rempli la configuration de la section 3 de la note v9 :

- GO de l'exemption : GO-2026-11-21-88, à la forme corrigée ;
- 5,1 jetons par mot, limites de mots 300 et 300 ;
- valeurs de l'avenant 2 recopiées à la main ;
- constat de la note v8 ;
- trois lignes de registre fictives, à la forme courte (551, 553 et 588 signes).

Résultats, par `gardes_avant_depart`, garde du registre comprise :

- Les deux vérifications passent, avec le plafond de sortie à 65 536.
- La file passe au régime prudent. La limite de mots demande 300 × 5,1 = 1 530 jetons, sous les 16 000 permis.
- Une limite de 3 200 mots (16 320 jetons) est refusée.
- Avec la vraie ligne GO-88 au registre, les mêmes départs sont refusés (section 3).

## 5. Conditions pour engager Google

1. Une ligne de décision au registre de main, accordée par Lazar, qui cite « exemption de la sonde », échéance au moins au jour du départ. Elle peut remplacer GO-88 ou s'y ajouter sous un identifiant neuf ; dans ce cas, inscrire cet identifiant dans `exemption_de_la_sonde_go`. Sinon, partir le 22 sous GO-69, avec la réserve de 05:30Z.
2. Les conditions de la vérification 9 restent : constat réel de Google seul, lignes de calcul au registre, fichier des interdits présent. Le constat d'exemple cesse de valoir le 24 novembre à 00:00Z avec un âge maximal de 96 heures, et cet âge reste à décider.
3. Les deux relevés de vérification doivent porter une fiche lisible à `outputTokenLimit` ≥ 65 536, sinon la file ne part pas.

## Fichiers ouverts

- La note v9.
- Les essais v9, autour des aides et des essais de la livraison 10.
- Le chef v9 : le contrôle du GO de l'exemption, la liste des gardes de départ, les constantes par import.
- Le registre de main, par `git show`, par recherche des lignes GO-69 et GO-88.

Rien sous un chemin interdit. Aucun réseau, aucune clé, aucun `GO_ID` fixé.
