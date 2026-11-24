# Test de neutralité par devinette à l'aveugle — question groupée v2, faits publics, question témoin

Écrit le 2026-11-24 à 17:32:27Z (heure `date -u`), par un lecteur neuf (Opus 5.5). Pièce de travail ; aucune dépense, aucun appel à un modèle externe.

## Méthode
1. Lecture des seules trois pièces : `faits-neutres-questions-directeur-v1.md`, `question-neutre-groupee-questions-directeur-v2.md`, `question-temoin-neutre-questions-directeur-v1.md`.
2. Devinettes et scores écrits avant toute autre lecture : `devinettes-avant-lecture-questions-directeur-v2.md` (empreinte `4ca622509d36030f2121d862fc0956fd166ab49190f15f32be56aecda275e268`).
3. Lecture ensuite des réponses du dossier : réponse à la question des quatre étapes comme oracles (`reponse-q1-…`), à la profondeur comme surprise retirée ailleurs (`reponse-q2-…`), à la cinétique des collisions d'idées (`reponse-q3-…` et son erratum 1), à la couche de problèmes et l'hypergraphe (`reponse-q7-…`), et la section « Question 11 » des demandes reformulées (pas de réponse écrite : seule l'attente de l'expert sert de repère). Rien lu d'autre ; rien ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/` ; le test v1 n'a pas été lu.
4. Score final = probabilité qu'un répondant devine la conclusion attendue ou y soit poussé, révisée après lecture selon que la devinette a touché la conclusion principale de la réponse. Seuil strict : 0,50 ou plus = échec.

## Tableau

| Pièce ou partie | Score avant lecture | Ce que la réponse conclut | Devinette juste ? | Score final | Verdict |
|---|---|---|---|---|---|
| Faits publics | 0,30 | Le fait du nœud est petit (corrélation de rang −0,166) et porte sur le concept parent | Non sur le fond (je n'ai pas vu la distinction parent et fille) ; les faits donnent les deux chiffres, classe et idée | 0,30 | Passe |
| Cadre | 0,20 | — (règles posées) | Sans objet | 0,20 | Passe |
| Partie 1, quatre étapes comme oracles | 0,45 | Deux étapes mécaniques (répétition générale, courbe de capacité avec jumeau) peuvent choisir une composition ; les deux qui passent par des lecteurs ne font que mesurer ; nœud non tranché où trois règles se rencontrent | Oui pour l'essentiel : partage « choisir ou seulement mesurer » selon qu'un modèle lit, et contradiction des règles ; manqué : l'étape (i) range aussi dans « mesurer seulement » | 0,50 | **Échoue** |
| Partie 2, profondeur comme surprise retirée | 0,35 | Fait petit, sur le parent ; surprise retirée = information mutuelle ponctuelle, terrain occupé (Friedman, Kitcher, Myrvold) ; la pondération par la centralité fait revenir le nœud ; mesure rapportée seulement | En partie : « le fait n'établit pas », critique de la pondération, familles d'estimateurs (lecteur figé, compression) ; manqué : parent et fille, antériorité, usage limité à la mesure | 0,45 | Passe de peu |
| Partie 3, cinétique chimique | 0,50 | « Garder en partie » (confiance 0,6) ; la cinétique redonne le taux existant, l'exponentielle est un facteur d'Arrhenius ; ajouts : étape limitante, catalyseur, ordre, précurseur d'autocatalyse | Oui : verdict, Arrhenius, renommage sauf catalyseurs ; manqué : le champ lu comme catalyseur, la température seulement dans le système | 0,60 | **Échoue** |
| Partie 4, couche de problèmes et hypergraphe | 0,40 | Fusion en un hypergraphe orienté, questions et anomalies en hyperarcs pondérés (écart, résistance par groupes, portée, centralité, maturation), couplés au taux par un terme ; prédiction d'un effet positif à surface égale | Oui : hypergraphe favori, couche utile, poids d'ancienneté et de groupes, prédiction d'un effet positif ; manqué : orientation des hyperarcs, fusion | 0,50 | **Échoue** |
| Partie 5, tensions par les relations | 0,35 | Pas de réponse ; l'attente de l'expert est la liste même des six familles | Sans réponse à confronter ; la liste donnée après « propose d'abord les tiennes » et « vides ou mal posées » équilibre | 0,40 | Passe |
| Partie 6, liens et ordre | 0,15 | Pas de réponse | Sans objet | 0,15 | Passe |
| Question témoin | 0,40 | Les réponses construisent la couche et gardent la cinétique en partie | En partie ; « Beaucoup d'idées naissent d'une anomalie » est posé sans « on avance » ; « Qu'est-ce que cela ajouterait » présuppose un apport | 0,40 | Passe |

## Fuite de conclusion constatée
- **Partie 1** : les phrases « et si certaines ne doivent servir qu'à mesurer » et « Si oui, dis-le sans trancher » donnent la forme de la réponse (un partage, une contradiction). Retouche : « Pour chacune, dis si sa sortie peut servir à choisir une configuration, seulement à mesurer, ou à rien ; dis si les règles du cadre se contredisent ou non, et où, sans trancher. »
- **Partie 3** : le modèle existant est décrit terme à terme dans l'ordre de la cinétique, et « si, et où, ce dictionnaire redonne le modèle existant sous un autre nom » pousse vers « renommage, garder en partie ». Retouche : « ce que ce dictionnaire partage avec le modèle existant et ce qu'il y ajoute, terme par terme », et verdicts offerts dans l'ordre « écarter, garder en partie ou garder ».
- **Partie 4** : « et de représenter l'ensemble par un hypergraphe » désigne la structure retenue ; (c) présuppose que la couche entre au taux. Retouche : « et de choisir une structure de représentation pour l'ensemble » ; en (c), « si et comment la couche entre dans le taux, et quelle prédiction elle ajouterait, s'il y en a » ; en (d), « compare au moins trois structures distinctes, dont un hypergraphe, et dis si aucune ne l'emporte ».
- **Partie 2, passe de peu** : l'enchaînement « fait 3, thèse » et la pondération par la centralité laissent voir la critique ; retouche conseillée, non exigée : retirer « pondérée par leur centralité » du modèle formel et garder seulement « le rôle d'une pondération éventuelle » en (b).
- **Question témoin, conseillé** : « On avance que beaucoup d'idées naissent… » ; « Qu'est-ce que cela ajouterait de mesurable, s'il y a quelque chose ? ».

## Réserves
- Un seul lecteur : la justesse d'une devinette est une observation, non une fréquence ; les scores finaux à 0,50 sont au seuil.
- Une partie de ce que j'ai deviné tient à la compétence (tout lecteur averti voit la loi d'Arrhenius dans un taux multiplicatif log-linéaire) plutôt qu'à la rédaction ; les retouches réduisent la poussée du texte, pas cette part.
- La partie 5 et la partie 6 n'ont pas de réponse écrite à confronter ; leur verdict repose sur la lecture du texte seul.

## Verdict global
**Échec** : la question groupée v2 échoue sur trois parties (1, 3 et 4, à 0,50, 0,60 et 0,50). Les faits publics, la question témoin, le cadre et les parties 2, 5 et 6 passent. Les trois retouches ci-dessus sont courtes ; une v3 retouchée demande un nouveau test par un lecteur neuf.
