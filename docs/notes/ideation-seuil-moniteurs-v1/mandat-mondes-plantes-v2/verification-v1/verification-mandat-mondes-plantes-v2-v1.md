# Vérification des corrections — mandat de l'auteur des mondes plantés v2 et devis v2 — v1

- Vérificateur : le contre-lecteur du mandat des mondes plantés, modèle O, auteur de la contre-lecture `9ea0ab895fc5bbf6a7226cf11778697da2f0d3ede79d997c43879df50b70ace5`. Je n'ai écrit aucune pièce v2.
- Écrit le 2026-11-21, après 08:18Z.
- Aucun appel, aucune dépense, aucune clé, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ni de garde.
- Décisions de la mère prises en compte : D-M16, D-M17 et D-M18, toutes tranchées pour l'option (a).

## 0. Verdict : **À corriger, pour la lettre seulement**

1. **Les six écarts à mon essai sont justes.** T08, T12 et T13 ont désormais chacun un sort unique.
2. **Tous les points de ma contre-lecture sont portés**, dans le mandat, dans le devis et dans le rapport.
3. **Le devis v2 porte les trois retouches**, et ses chiffres sont justes. Le programme, rejoué deux fois, donne des sorties égales entre elles et égales à la sortie versée.
4. **D-M16 à D-M18 sont bien posées.** Le mandat v2 porte D-M17 et D-M18 tels quels. Il porte D-M16 pour les témoins imposés, mais pas encore pour les témoins libres de l'auteur. Il faut une retouche de deux remplacements, prête et essayée sur copie, **non appliquée** (§ 4).
5. **Aucun nom de modèle ni de fournisseur** dans le mandat, le devis, le programme, sa sortie ni le jeu de remplacements.

## 1. Empreintes

- Les seize lignes de `table-empreintes-mandat-mondes-plantes-v2.txt` sont vérifiées par `sha256sum -c` : seize « OK ». La table elle-même est égale à son compagnon (`6eb9f8e5e58467efa6a17a2be877d18bcc62c1c98272d5228c41d3f15a7ed188`).
- J'ai rejoué le jeu du rédacteur (`6e4606de…`, 25 remplacements) sur le mandat v1 (`6774507c…`), avec l'outil contre-lu (`391db990…`) : 25 remplacements, aucun refus. La sortie vaut `4bca0bbc6a1c09664f8a64d1201ee635564db6fd3a1de8cfbe5912862cc02766`, ce qui est **le mandat v2 à l'octet**.
- Le rejeu de mon jeu de 22 remplacements par le rédacteur vaut `58a69c74…`, ce qui est mon essai.

## 1 bis. Les six écarts à mon essai (point 1)

Ils viennent du différentiel `30192972…` ; il y en a six, rien d'autre.

| écart | jugement |
|---|---|
| Titre « v2 » (n° 24) | Juste, par la règle R12. |
| T12, « unilatéral à droite », avec la valeur p définie comme P(compte ≥ compte observé) sous 0,20, et l'alerte quand elle est strictement sous 0,01 (n° 6) | Juste. C'est le sens du programme de la note : la queue haute, avec une inégalité stricte. Mon « unilatéral » ne disait pas de quel côté. |
| La même précision dans la grammaire de `test_repete_sans_correction` (n° 21) | Juste. |
| T05 et T07 (n° 8) : puissance aux trois tailles de signal ; `n` = 200 pour T07, son taux à 400 dans `valeurs_de_plus` ; `morte_sans_gain` défini sous condition (« garantie tenue et écart de puissance à la base qui n'est pas strictement positif ») ; les autres témoins imposés lus sur la seule garantie | Juste, et cela comble trois manques de ma lettre : la taille du signal, les deux valeurs de `n` de T07, et l'issue non définie. La phrase porte sur l'écart vrai : ce n'est pas un critère de mort (aucun tirage, aucun niveau), et elle ne sert aucune valeur vraie (D-M12). C'est l'option (a) de D-M16 pour les témoins imposés. |
| § 5 : « définitions du § 2 et du § 3.1 » (n° 25) | Juste, en accord avec le n° 8. |
| § 6, point 4 : « notre calcul, fait par un programme scellé avant la lecture de ta sortie » (n° 23) | Juste. C'est une occurrence que mon jeu avait manquée. |

**Chaque témoin a-t-il maintenant un sort unique ?**
- **T08** : la convention ⌈n × niveau⌉, n = 400, niveau 0,99, donne le 396ᵉ plus petit score, soit le 5ᵉ plus grand. J'ai vérifié, avec un petit programme dans mon dossier (`essai_plafond_flottant.py`), qu'aux tailles 200, 300, 400 et 1 000 et aux niveaux 0,99, 0,95 et 0,9, le calcul en flottants et le calcul exact donnent le même rang : aucun piège d'arrondi. **Sort unique.**
- **T12** : côté du test, valeur p, inégalité, horizon (1 à 300) et taux nul sont tous fixés. **Sort unique.**
- **T13** : le rapport de vraisemblance de 0,30 contre 0,20 et le seuil (100 ou plus) sont fixés ; une richesse qui part de 1 est impliquée par le mot « rapport de vraisemblance ». **Sort unique.**

## 2. Les points de ma contre-lecture sont-ils portés ? (point 2)

| point de la contre-lecture | où il est porté |
|---|---|
| 22 remplacements | 19 tels quels ; 3 corrigés dans leur lettre (jugés au § 1 bis) |
| T09 inversé, « notre calcul scellé », « non contre-lue », T08, T12, T13 | portés (mandat v2) |
| Vérité exacte, ce qui écarte un monde, C, D, E et G, témoins du monde M, H « échangeables », `portee_de_la_garantie`, deux familles libres au plus, tailles 200, 300 et 400 | portés (n° 2, 3, 9 à 15, 17, 19, 22) |
| Devis : taille du mandat, premier essai à 32 000 jetons, exception au scellement `4286bf39…` | portés (§ 4 ci-dessous) |
| Rapport : D-M11 à D-M15 closes ; D-L2 mise à jour ; deux lignes de calendrier, dont le programme de vérification avant l'envoi | portés (rapport v2, § 5 et § 6) |
| Remarques : quatre décimales sur le texte brut ; vérité de T09 à T11 paramétrée par la loi de l'auteur | portées en réserves du rapport v2 (points 3 et 6) |

Le mandat garde `version_forme` à `…-v1`, et le rapport en dit la raison : aucune sortie n'a encore été rendue. C'est acceptable.

## 3. D-M16, D-M17 et D-M18 (point 4)

**La forme des trois décisions** :
- chacune a une décision en une phrase, un enjeu, deux options avec leur avantage et leur inconvénient, une recommandation et sa confiance ;
- leur défaut sous 48 heures est acceptable : aucune n'est une dépense ;
- une lettre est maladroite : l'inconvénient de l'option (b) de D-M16 parle d'une « correction vers la v5 », alors qu'il s'agit d'un changement de sorte d'un témoin de la banque de la v5. Cela reste sans effet, puisque la mère a tranché.

**Ce que le mandat v2 porte de chacune** :

| décision (a) | portée ? |
|---|---|
| **D-M16** : le témoin « doit tenir » qui est la base elle-même se lit sur la seule garantie | **Oui pour les témoins imposés** : T02, T15 et T16 ne disent que `tient` ou `morte_invalide` ; seuls T05 et T07 ont la lecture « sans gain », comme dans la banque de la v5. **Non pour les témoins libres** : le § 3.1 ne parle que des « autres témoins imposés », et le § 5 renvoie au § 2, où l'issue « sans gain » existe. Un témoin libre qui serait la base pourrait donc être noté `morte_sans_gain` par l'auteur, à l'inverse de D-M16. **Retouche due** (§ 4). |
| **D-M17** : T08 gardé | **Oui** : T08 est dans la table, avec sa convention (n° 21). |
| **D-M18** : deux familles libres, vérité exacte et témoins exigés comme pour les autres, sinon elles n'entrent pas | **Oui.** Le § 3.4 demande « deux familles de plus, au plus, à vérité exacte, chacune avec ses témoins ». La règle générale du § 3.2 (« une famille […] dont la vérité n'est pas exacte ou qui n'a pas ses deux témoins n'entre pas ») les couvre. Les § 4.2 (`verite.mode` : `exacte` seulement) et § 6.2 (deux témoins par famille) le vérifient. |

Le devis v2 n'est touché par aucune des trois décisions.

## 4. La retouche pour D-M16, prête et non appliquée

- Jeu : `remplacements-mandat-auteur-mondes-plantes-v2-vers-v3-d-m16.json`, `a02be55fa4915d951d007155bc28124cef3003c28e3f4786d432a5bbb369bc48`, deux remplacements.
- Essai sur copie, avec l'outil contre-lu, sur la cible `4bca0bbc…` :
  - aucun refus ;
  - sortie `essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md`, `26402f3b884196971886ed48597bfeaff7f7323ee17983c237ac23e318330108`, 27 421 octets ;
  - journal `8c5c94d460f93cc59e58a055a0b17f92a0e67861ccaa81ed61b5803f72b21711`.

| n° | ancien | neuf | pourquoi |
|---|---|---|---|
| 1 | « Pour les autres témoins imposés, `issue_attendue` ne dit que la tenue de la garantie dite : `tient` ou `morte_invalide`. » | « Pour tous les autres témoins, imposés ou libres, `issue_attendue` ne dit que la tenue de la garantie dite : `tient` ou `morte_invalide` ; un témoin dont la règle est la base elle-même se lit ainsi, sauf T07. » | porte D-M16 aux témoins libres |
| 2 | « donne la couverture sur la population de lecture, » | « donne la couverture sur la population que dit `portee_de_la_garantie`, » | tenue : le dernier usage de l'ancien nom (D-M11) |

**Effet sur le devis** : l'entrée passe à 27 421 octets, soit 10 969 jetons. Tous les montants arrondis restent les mêmes :

| candidat | cas bas | cas haut |
|---|---|---|
| R2-a | 0,36 | 4,24 (4,23858) |
| R2-b | 0,36 | 4,02 |
| R3 | 0,91 | 3,42 |

Les plafonds et le total de 118,74 ne changent pas. Seule la ligne M1 du devis et de son programme est à mettre à jour, sous un nom v3, si la retouche est portée.

## 5. Le devis v2 (point 3)

- **Rejeu.** Deux exécutions sous Python 3.13.18 (`python3 -B`) ; `cmp` est muet entre elles et avec la sortie versée (`fd341f09…`). Le second jeu versé par le rédacteur a la même empreinte.
- **Taille.** Le mandat v2 fait 27 310 octets par `wc -c`, soit 10 924 jetons ; c'est égal au devis.
- **Les trois retouches sont faites** :
  - la taille M1 ;
  - le premier essai de R2-a à 32 000 jetons ;
  - l'exception à la phrase du scellement `4286bf39…`, écrite dans la ligne de GO, et bornée à cet appel et à ce montant.
- **Les chiffres sont justes**, et je les ai refaits à la main :
  - R2-a, par essai : 10 924 × 10 / 10⁶ + 40 192 × 50 / 10⁶ = 2,11884. Le cas haut vaut 4,23768, soit 4,24. Le pire vaut 4,2592, soit un plafond de 4,26 (2,13 par essai). Le cas bas vaut 0,363696, soit 0,36.
  - R2-b : 2,009776 par essai, soit un cas haut de 4,02 ; le plafond est de 4,04.
  - R3 : 1,70924 par essai, soit un cas haut de 3,42, un cas bas de 0,91 ; le plafond est de 3,44.
  - Le total 114,48 + 4,26 = 118,74 reste sous 120.
  - Les contrôles neufs du programme (le plafond tient le cas haut ; l'entrée tient sous la garde ; la sortie tient au premier essai, provision déduite) sont vrais.
- **Ce qui est ajouté**, et qui est juste : la sortie illisible est dite telle par le programme, jamais à la main ; un monde écarté ne donne pas de second essai ; le programme de vérification est une condition de départ, dans la ligne de GO.

## 6. Noms de modèles ou de fournisseurs (point 5)

- **Aucun** dans le mandat v2, le devis v2, le programme v2, sa sortie, ni le jeu de 25 remplacements (recherche de motifs : zéro occurrence).
- Les pièces internes portent « modèle F » et « modèle O », qui sont des pseudonymes de rôle et non des identifiants. Le mandat servi n'en porte aucun.

## 7. Remarques, sans correction

1. Le rapport v2 cite un ordre v6 (`208454c5…`), qui porte les décisions de 07:56Z et le champ `portee_de_la_garantie`. Je n'ai lu que sa ligne de version : rien n'y contredit le mandat v2.
2. Avec D-M16 (a), la table d'admission et le programme de vérité des témoins devront appliquer la même double lecture : la seule garantie pour tous les témoins, la classe « sans gain » pour T05 et T07.

contre-lecteur du mandat des mondes plantés, modèle O
