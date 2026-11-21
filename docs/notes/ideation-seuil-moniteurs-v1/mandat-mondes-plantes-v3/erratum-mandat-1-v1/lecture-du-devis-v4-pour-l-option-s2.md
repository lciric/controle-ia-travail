# Lecture du devis v4 pour l'option S2 — l'appel à l'auteur des mondes plantés, course « seuil et moniteurs »

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Relevé de `date -u` : 2026-11-21, 09:17:59Z.
- Pièce lue : `devis-auteur-mondes-plantes-v4.md`, `72bd50453bbb3590924442df78ca829dd2e47ca468c1cb136c3ac161d17ea888`, et son calcul `calcul-devis-auteur-mondes-plantes-v4.json`, `70e957ec37b69cb831bf8ababe84f3f20fa3b1cff81e288b7a13f4912e78ad05` (programme `bd219a4a857bba1535f5cbf39a576cfc2e7a0c86f0b5bf75f8580c343f04982e`). **Aucune des trois n'est modifiée ni rejouée** : cette pièce de travail (classe C) dit seulement ce que le devis v4 vaut une fois l'option S2 retenue par la mère.
- Aucun appel, aucune dépense, aucun commit.

## 1. Le devis v4 tient pour S2 tel qu'il est écrit

Le programme n'est pas rejoué sous un nom neuf, parce que **ni l'entrée ni la sortie ne changent** par rapport au scénario S2 déjà calculé.

| grandeur | au calcul v4, scénario S2 | après le mot de la mère | égal ? |
|---|---|---|---|
| entrée, le texte servi | 27 468 octets, soit 10 988 jetons | 27 468 octets (`wc -c` du texte servi de la seconde passe, `2e675d74cfe035a16ac4e54fcbcae3855ceae9523816f8d1b3e04ebde3b46251`) : « 55 000 » a le même nombre d'octets que « 60 000 » | oui |
| borne de sortie | 55 000 caractères, soit 22 000 jetons | 55 000 caractères | oui |
| plafond de sortie de R2-a | 32 000 jetons, aux deux essais | inchangé | oui |

Le calcul, refait à la main pour le candidat R2-a (prix comptés 10 et 50 par million de jetons, provision 8 192) :

- sortie contenue, provision comptée dedans : 32 000 − 8 192 = 23 808 ≥ 22 000, marge 1 808 jetons ;
- sortie contenue, provision comptée à côté : 32 000 ≥ 22 000, marge 10 000 jetons ;
- cas bas, un essai, prix bas 4 et 20 : (10 988 × 4 + 22 000 × 20) / 10⁶ = 0,483952, soit 0,48 ;
- cas haut, deux essais : 2 × (10 988 × 10 + 40 192 × 50) / 10⁶ = 2 × 2,11948 = 4,23896, soit 4,24 ;
- pire, deux essais à la garde d'envoi : 2 × (12 000 × 10 + 40 192 × 50) / 10⁶ = 2 × 2,1296 = 4,2592 ;
- **plafond d'arrêt : 2,13 par essai, 4,26 en tout**, qui tient le pire et le cas haut ;
- **total avec la course : 114,48 + 4,26 = 118,74**, marge 1,26 sous 120.

Ces nombres sont ceux de la sortie du calcul v4, scénario S2, candidat R2-a. Le texte servi tient sous la garde d'envoi : 27 468 ≤ 30 000, marge 2 532.

## 2. La ligne de GO du devis v4, pour S2, sans crochets

Le § 3 du devis v4 écrit la ligne avec trois choix entre crochets. Pour S2, elle se lit, à la lettre :

> **Course « seuil et moniteurs », auteur des mondes plantés** (GO-2026-11-21-16) : un appel au deuxième relais, par un modèle de la troisième lignée, qui reçoit le mandat v3 avec son erratum 1 appliqué, scellé, tel quel, et rend les familles de mondes, leurs témoins et leur table. **Appel de préparation, accordé par exception à la phrase « Aucune dépense avant ce scellement » du scellement de la conception (`4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07`), par le mot de Lazar : le préenregistrement court attend les mondes que seul cet appel produit ; l'exception ne vaut que pour cet appel et ce montant.** Départ quand le texte servi et ce devis sont contre-lus et scellés, et quand le programme de vérification de la sortie est écrit et essayé ; le programme de vérité des dix-sept témoins imposés est scellé avant toute lecture de la sortie. Deux essais au plus, chacun à 32 000 jetons de sortie, le second seulement après une sortie dite illisible par programme, jamais après un refus ; plafond par essai 2,13 USD ; arrêt net au plafond. Le monde à K actions n'y est pas. | 4,26 USD |

## 3. Ce qui reste vrai du devis v4, et ce qui tombe

- Restent : son § 0 (le constat), son § 1 (le devis v3 rejoué à 60 000, pour mémoire), la colonne S2 de son § 2, ses réserves.
- Tombent, la mère ayant tranché : les colonnes S0 et S1 de son § 2, et la décision de son § 3, close en faveur de S2.
- Le devis v4 reste non contre-lu : sa vérification précède son scellement.

rédacteur du mandat des mondes plantés v2, modèle F
