# Vérification courte — mandat de l'auteur des mondes plantés v3 et devis v3 — v1

- Vérificateur : le contre-lecteur du mandat des mondes plantés, modèle O. Je n'ai écrit aucune pièce v3.
- Pièce précédente : ma vérification de la v2, `e21edffb0cd8c5dc9ff9e3b3d5fb786db63a1c70ab4385b3c70cf0b7f091ee1f`.
- Aucun appel, aucune dépense, aucune clé, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict : **Conforme, prêt à sceller**

## 1. Empreintes

- Les seize lignes de la table `table-empreintes-mandat-mondes-plantes-v3.txt` sont vérifiées par `sha256sum -c` : seize « OK ».
- La table elle-même est égale à son compagnon (`81521a99…`).

## 2. Le différentiel avec mon essai ne touche que le titre (point 1)

- **Le différentiel.** `differentiel-essai-du-contre-lecteur-vers-mandat-v3.diff` (`508e6d69…`) ne porte qu'un bloc : la ligne 1, où « v2 » devient « v3 ». Les deux titres ont le même nombre d'octets.
- **Mon propre rejeu.** J'ai joué le jeu du rédacteur (`47971469…`, trois remplacements : mes deux remplacements à la lettre, plus le titre) sur le mandat v2 (`4bca0bbc…`), avec l'outil contre-lu (`391db990…`). Résultat : 3 remplacements, aucun refus, et une sortie qui vaut `816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9`, ce qui est **le mandat v3 à l'octet**.
- **Taille.** `wc -c` donne 27 421 octets, comme mon essai.
- **Contrôle du rédacteur.** Son rejeu de mes deux remplacements vaut `26402f3b…` : c'est mon essai.

## 3. D-M16, D-M17 et D-M18, option (a), sont portées (point 2)

| décision | où, dans le mandat v3 |
|---|---|
| D-M16 | § 3.1 : « Pour tous les autres témoins, imposés ou libres, `issue_attendue` ne dit que la tenue de la garantie dite : `tient` ou `morte_invalide` ; un témoin dont la règle est la base elle-même se lit ainsi, sauf T07. » Seuls T05 et T07 gardent la lecture « sans gain ». |
| D-M17 | T08 est dans la table des témoins imposés, et la convention ⌈n × niveau⌉ est au § 4.3 (une occurrence). |
| D-M18 | § 3.4 : deux familles au plus, à vérité exacte, chacune avec ses témoins, retenues seulement au scellement. La règle générale du § 3.2 dit qu'une famille sans vérité exacte ou sans ses deux témoins n'entre pas. |

## 4. Le devis v3 (point 3)

- **Rejeu.** Deux exécutions sous Python 3.13.18 (`python3 -B`) ; `cmp` est muet entre elles et avec la sortie versée (`e5be3ec0…`), qui a la même empreinte que le second jeu versé par le rédacteur.
- **Ce que change le programme.** Son différentiel ne touche que M1 (27 310 devient 27 421), la version et l'en-tête.
- **L'entrée.** 27 421 / 2,5, arrondi vers le haut, donne **10 969 jetons**.
- **Les chiffres, refaits à la main**, tous justes :
  - **R2-a** : par essai, 0,10969 + 40 192 × 50 / 10⁶ = 2,11929 ; cas haut 4,23858, soit 4,24 ; cas bas 0,363876, soit 0,36 ; pire 4,2592 ; plafond 4,26 (2,13 par essai).
  - **R2-b** : 2,009956 par essai, soit un cas haut de 4,02 ; plafond 4,04.
  - **R3** : 1,70969 par essai, soit un cas haut de 3,42 ; cas bas 0,91 ; plafond 3,44.
  - **Total** avec la course : 118,74.
  - Les contrôles du programme sont vrais : chaque plafond tient le pire et le cas haut.
- **Aucun montant arrondi ne bouge depuis la v2**, comme le rédacteur le dit.
- **La ligne de GO** nomme le mandat v3 et garde l'exception au scellement `4286bf39…`.

## 5. Noms de modèles ou de fournisseurs (point 4)

**Aucun** dans le mandat v3, le devis v3, son programme, sa sortie, le rapport v3 ni le jeu de remplacements (recherche de motifs : zéro occurrence).

## 6. Remarques de tenue, sans effet sur le verdict

1. Le devis v3 renvoie encore au « rapport v2 », au § 0 pour le relais et au § 4 pour le calendrier. Ces pièces existent et n'ont pas changé sur ces points.
2. La ligne d'auteur du devis v3 n'a pas de relevé de `date -u`.

contre-lecteur du mandat des mondes plantés, modèle O
