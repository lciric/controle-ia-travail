# Rapport du rédacteur — mandat de l'auteur des mondes plantés v3 et son devis v3 (course « seuil et moniteurs ») — v3

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Écrit le 2026-11-21, après la vérification rendue après 08:18Z.
- Version : ce rapport **complète** le rapport v2 (`b4b1fdbb7e8038668f0fef7cca062dc7212a997071320a1ffdcd277b1cb7698e`, gardé intact), qui reste la pièce à lire pour le jugement des 22 remplacements, le choix du relais, D-L1, D-L2 et le calendrier. Il ne dit que ce qui change.
- Cause : la vérification du contre-lecteur, `docs/notes/ideation-seuil-moniteurs-v1/mandat-mondes-plantes-v2/verification-v1/verification-mandat-mondes-plantes-v2-v1.md` (`e21edffb0cd8c5dc9ff9e3b3d5fb786db63a1c70ab4385b3c70cf0b7f091ee1f`, recalculée, lue en entier), verdict « À corriger, pour la lettre seulement » ; et les mots de la mère sur D-M16, D-M17 et D-M18.
- Statut : pièce de travail (classe C). Aucun appel, aucune dépense, aucune clé lue, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

1. **Le mandat de l'auteur v3 est écrit** : les deux remplacements du contre-lecteur sont adoptés tels quels, et j'en ajoute un, de tenue (le titre). Trois remplacements appliqués par l'outil à ancres comptées sur une copie du mandat v2 (`4bca0bbc…`), sans refus. 27 421 octets, `816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9`.
2. **Mon mandat v3 diffère de l'essai du contre-lecteur par la seule ligne du titre** (« v2 » devient « v3 »). **Contrôle** : son jeu, rejoué tel quel sur la même copie, rend son essai à l'octet (`cmp` muet, `26402f3b…`).
3. **Le devis v3 ne change aucun montant arrondi.** Plafond 4,26 USD, deux essais au plus à 2,13 ; total avec la course 118,74 sous 120.
4. **D-M16, D-M17 et D-M18 sont closes** par les mots de la mère, toutes en (a), et portées.

## 1. Les deux remplacements du contre-lecteur, et le mien

| n° | objet | mon jugement |
|---|---|---|
| 1 | « Pour les autres témoins imposés » devient « Pour tous les autres témoins, imposés ou libres » ; « un témoin dont la règle est la base elle-même se lit ainsi, sauf T07 » | **adopté tel quel.** Ma lettre de la v2 ne portait D-M16 que pour les témoins imposés : un témoin libre qui serait la base pouvait être noté `morte_sans_gain`. La phrase neuve ferme ce cas. « Tous les autres » se lit bien « autres que T05 et T07 », nommés à la phrase d'avant |
| 2 | « la population de lecture » devient « la population que dit `portee_de_la_garantie` » | **adopté tel quel.** Je l'avais laissé à dessein en prose ; le nom du champ est plus sûr, et c'était le dernier usage de l'ancien nom |
| 3 | titre : « v2 » devient « v3 » | **ajouté par moi**, de tenue (règle R12). C'est le même défaut que mon n° 24 de la v2, que la vérification juge « juste » : l'essai du contre-lecteur gardait « v2 » en titre d'un fichier v3. Même nombre d'octets |

**Une conséquence de D-M16 (a), dite sans la corriger.** Un témoin libre `doit_mourir` ne peut plus mourir que par sa garantie violée (`morte_invalide`) : la lecture « sans gain » est réservée à T05 et T07. C'est le sens du mot de la mère ; la table d'admission et le programme de vérité des témoins doivent appliquer la même double lecture (remarque 2 de la vérification).

## 2. Décisions closes par les mots de la mère

| décision | mot de la mère | où c'est porté dans le mandat v3 |
|---|---|---|
| **D-M16** | (a) : un témoin « doit tenir » qui est la base elle-même se lit sur la seule garantie | § 3.1, paragraphe des valeurs à donner : pour les témoins imposés depuis la v2 (mon n° 8), pour les témoins libres depuis la v3 (n° 1 ci-dessus) |
| **D-M17** | (a) : T08 est gardé | table des témoins, ligne T08 ; § 4.3, convention du quantile. Rien à changer depuis la v2 |
| **D-M18** | (a) : deux familles libres, avec leur vérité exacte et leurs témoins, sinon elles n'entrent pas | § 3.4 ; règle générale du § 3.2 ; § 4.2 (`verite.mode` : `exacte` seulement) ; § 6, point 2. Rien à changer depuis la v2 |

Restent ouvertes, pour Lazar, sans défaut : **D-L1** (la ligne de 4,26 USD, avec son exception au scellement `4286bf39…`) et **D-L2** (le modèle de l'expérimentateur, nœud N4). Leur texte est au rapport v2, § 5, inchangé ; la ligne de GO à la lettre est au devis v3, § 5.

## 3. Le devis v3

Un seul changement : la taille du texte servi, 27 421 octets au lieu de 27 310, soit 10 969 jetons au lieu de 10 924. Programme v3 joué deux fois sous Python 3.13.18 (`python3 -B`), sorties égales à l'octet (`cmp` muet).

| candidat | cas bas | cas haut | pire | plafond d'arrêt |
|---|---|---|---|---|
| R2-a | 0,36 (0,363876) | 4,24 (4,23858) | 4,26 | 4,26 (2,13 par essai) |
| R2-b | 0,36 (0,363876) | 4,02 (4,019912) | 4,03 | 4,04 (2,02 par essai) |
| R3 | 0,91 (0,90969) | 3,42 (3,41938) | 3,44 | 3,44 (1,72 par essai) |

**Aucun montant arrondi ne change** depuis la v2 ; les valeurs exactes entre parenthèses bougent à la quatrième décimale, et sont égales à celles que la vérification annonce (son § 4). Le pire et les plafonds ne dépendent pas de la taille du texte : ils comptent la garde d'envoi de 30 000 caractères, sous laquelle le mandat v3 tient avec 2 579 caractères de marge.

## 4. Réserves

1. Mon remplacement n° 3 (le titre) n'est pas contre-lu ; le différentiel de l'essai vers le mandat v3 l'isole, une ligne.
2. Les réserves du rapport v2, § 7, valent encore, sauf la première : la vérification a jugé mes trois corrections et mes trois ajouts de la v2.
3. La vérification relève une lettre maladroite du rapport v2 (D-M16, inconvénient de l'option (b)). Elle est sans effet, la mère ayant tranché ; le rapport v2 n'est pas réécrit.

rédacteur du mandat des mondes plantés v2, modèle F
