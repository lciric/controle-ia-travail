# Rapport du concepteur — véhicule de la course « nouvelles attaques » — v3

- Auteur : concepteur du véhicule, modèle F. Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:33:38Z, après la lecture des deux pièces, avant l'écriture.
- Ce rapport complète les rapports v1 (`ceffd7aa…`) et v2 (`679cf52e7377acfbb11e84eae2532cc749c6eb9d8e61cc6457883633dda0306a`), qui restent en place.
- Processeur seul : aucun appel, aucune clé lue ni nommée par sa variable, aucune dépense, aucun code écrit pour être lancé, aucun lancement, aucune écriture dans un dépôt. Aucune sortie de modèle sur la question de la course n'a été lue. **La branche tenue à l'écart n'a pas été ouverte ; le registre servi de la matière première n'a pas été ouvert.** **Aucun refus de permission, de classifieur ni de garde.**

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/concepteur-vehicule-nouvelles-attaques/`. Empreintes à la table v3.

| pièce | objet |
|---|---|
| `conception-vehicule-course-nouvelles-attaques-v3.md` | la conception réécrite ; la v2 reste intacte, à son empreinte |
| `differentiel-conception-vehicule-v2-v3.diff` | sortie de `diff -u` entre la v2 et la v3 |
| `rapport-concepteur-vehicule-v3.md` | ce rapport |
| `table-empreintes-concepteur-vehicule-v3.md` | les empreintes |

Le sous-dossier `morceaux-v3/` porte les morceaux d'assemblage ; il n'est pas à verser.

## 2. Pièces lues pour la v3

| pièce | empreinte | contrôle | lecture |
|---|---|---|---|
| contre-lecture de la v2 et du lot 0 (CL2) | `f46322b97fb6facca8fcf6ca16158186aeaceba0d713ae65f2b3d79d6597d401` | égale à son compagnon | en entier |
| relevé du lot 0 (L0) | `10ac79ecb0e064f5b5ea80ddb060ae37e303d2d84ff242f653f4cccbd7ff753e` | égale à son compagnon | en entier |
| table d'empreintes du lot 0 | `d79bd98ef3b103cd173280cf002927ba5102d1f59828ba00590aeb9c513d463f` | égale à l'empreinte que cite CL2 | **non ouverte** : empreinte seule |
| attestation « aucune recette » de la matière première, `origin/main` | `19ef4d7458818e184c4dfcf5535dee2c9710f549c28f34ff4aa0d9b20e736f46` | début égal au message de la mère | en entier |
| registre servi de la matière première, `origin/main` | `3bcb94e672390f6f68ca318f214a749dbb0fb14cf8ca4c44728beccf18440d1e` | début égal au message de la mère | **non ouvert** : tiré pour son empreinte |

Aucun code relu pour la v3 : les faits neufs sur le code viennent de L0 et de CL2. Portés d'après les messages de reprise, sans pièce relue : les décisions de la mère de 07:21Z ; l'ajout de 07:39Z, le commit `88b55a9e` de la branche tenue à l'écart, l'empreinte `3216e1b2…` des références.

## 3. Point de la contre-lecture (CL2, § 5) → lieu dans la v3

| point | objet | lieu dans la v3 |
|---|---|---|
| 1 | décisions de 07:21Z, points 1 à 6 ; lignes de compte toujours écrites ; colonne éteinte par défaut | § 0 bis, première table ; § 2.4 ; § 2.6 ; § 5.2 ; § 2.13 ; § 2.3 ; § 2.14 ; § 9, points 3, 4, 18, 19 |
| 2 | routage, part, motifs, journal, égalité dans une surcharge d'`appel` ; phrase fausse sur le portier retirée | en-tête ; § 2.3, en entier ; § 5.1 ; § 3 |
| 3 | refus avant `super().appel` : « non envoyé », coût nul, compté, hors du suivi | § 2.3, « Le refus avant le noyau » ; § 2.7 ; § 6.2, « envoi refusé sans coût » |
| 4 | adaptateur Claude neuf sans texte système ; relevé au faux fournisseur au lot 4, avant l'additif | § 2.3, « L'adaptateur Claude neuf » ; § 6.2 ; § 7, lot 4 ; § 8 |
| 5 | réponses brutes de Minuit et de Luc conservées par cet adaptateur | § 2.3 ; § 1.2 ; § 6.2, « réponses brutes conservées » |
| 6 | ni `preparer` ni `valider_contenu` ; validateur et lecteur neufs ; champ `case` ; pas de caviardage | § 2.4, en entier ; § 5.4 ; § 1.2 ; § 6.2, « champ case et validateur neuf » |
| 7 | gardes héritées une par une, tous les rôles, en refus écrits ; délai A3 aligné | § 2.13, en entier ; § 2.3, pas 0 ; § 6.2, « gardes héritées » |
| 8 | identifiant de fiche et identifiant servi au juge réencodés | § 5.2, paragraphe neuf ; § 2.4 ; § 2.5 ; § 6.2 ; § 9, points 3 et 21 |
| 9 | `fournisseurs_requis` surchargé ; `hors_course` | § 2.9 ; § 2.3, pas 1 et table ; § 6.2 |
| 10 | six étapes neutralisées ; mémoire déclarée ; configuration par génération ; statuts et arrêt n° 13 sur les clés Claude ; coûts par rôle par génération ; forme de la fiche servie ; fuite de L9, l. 2667 à 2669 | § 2.9 ; § 2.3, « Les statuts » ; § 1.2 ; § 2.4, § 2.5, § 5.3 ; § 2, règle commune ; § 7, lot 8 ; § 6.2 ; § 9, point 14 |
| 11 | risque né de D2 et de D7 ensemble | § 9, point 20 ; § 2.10 ; § 5.4 |
| 12 | point 8 de l'additif v69, v4 | § 2.11, ligne 8 ; § 2.7, « comptes des refus » |
| 13 | numéros des questions du lot 0 alignés sur le relevé | § 7, paragraphe « Le lot 0 est fait » ; tous les renvois « L0, Qn » |
| 14 | calendrier rechiffré lot par lot | § 7, « Chemin critique » ; § 8, en entier ; § 0, points 4 et 5 |

Hors de la contre-lecture, sur le message de la mère de 07:39Z : la colonne chargée depuis le registre servi, l'interrupteur à trois états et la règle d'allumage, la garde, la lecture de fin, les lecteurs et la preuve de quarantaine, la comparaison finale (§ 2.14, § 2.15 ; § 6.2 ; § 7, lot 10 ; § 8).

## 4. Décisions

**Tranchées par la mère, portées par la v3** : les six de 07:21Z ; celles de 06:58Z et de 07:10Z restent.

**Pour Lazar** : D8, D9 (échéance du 2026-11-27 demandée par la mère, non accordée), D12, inchangées ; et l'allumage de la colonne « matière première », par la règle du § 2.14.

**Propositions neuves, pour la mère** (conception v3, § 9, points 20 et 21 ; § 2.14) :

1. Réencoder l'identifiant de fiche et celui servi au juge, sans suite hexadécimale : sans cela, toute requête de juge et toute ligne du registre servi font mordre l'arrêt n° 16. Recommandé ; c'est un encodage, non un tirage.
2. Une fiche dont le champ `case` diffère de sa case : la consigner et la compter, sans changer sa classe.
3. Une espèce qui répond en prose (D2 et D7 ensemble) : lecteur à grammaire par étiquettes ancrées ; taux d'illisibles lu à la sonde ; l'arrêt n° 27 gardé à la lettre, avec une étiquette demandée à la session à part.
4. Sur une clé Claude, une erreur de cause non établie est « réponse illisible » ; l'arrêt n° 13 se lit à l'état du relais.
5. Ce que l'outil envoie sans texte système : déclaré comme transport, ou refusé, après le relevé du lot 4.
6. La portée d'A2 : la course, par un arrêt nommé.
7. La somme des plafonds des processus de relais d'une même clé est au plus sa part.
8. La forme de la fiche servie au portier et aux juges est gardée et déclarée à l'additif (lecture de CL2 ; le relevé du lot 0 la lit plus strictement).
9. Colonne : demander l'état « garde seule » pour la course ; seules les visées entrent dans la comparaison ; l'inscription des lecteurs de la branche.

## 5. Mes écarts, pour la v3

1. **Une erreur de fait de ma v2**, corrigée : le portier passe par `appel`. Elle venait d'une lecture de la version de l'aiguilleur que la course ne joue pas.
2. La v3 est assemblée par `sed -n` (extraits de la v2) et `cat` (avec les sections neuves, écrites à l'outil d'écriture), puis retouchée à l'outil d'édition ; la v3 en cours a été réassemblée une fois sur elle-même, pour y poser la section de la colonne. La v2 est relue à son empreinte après coup, inchangée.
3. Un `git fetch origin main` et deux `git show` redirigés, pour l'attestation et le registre servi ; le registre n'est pas ouvert.
4. `diff -u` rend le code 1 quand les fichiers diffèrent : ce n'est pas un refus.
5. Je n'ai relu aucun registre : les décisions et accords cités depuis la v1 sont portés d'après les messages reçus.
6. Les copies de lecture de l'attestation et des registres portent des noms de modèles ; aucune de mes pièces n'en porte. Aucun nom ni énoncé de la matière première n'est recopié.

— concepteur du véhicule, modèle F
