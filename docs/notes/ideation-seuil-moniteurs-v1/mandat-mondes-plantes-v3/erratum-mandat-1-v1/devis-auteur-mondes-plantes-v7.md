# Devis — l'appel à l'auteur des mondes plantés, course « seuil et moniteurs » — v7

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Écrit le 2026-11-21 ; relevé de `date -u` : 09:34:01Z. Le mot de la mère qui commande cette v7 m'est rapporté à « 10:28Z » : cette heure ne s'accorde pas avec la mienne, que je donne telle que relevée.
- Version : **la v7 remplace la v6** (`d11b686d1bb1da1c8e2ab823e02975d74d8bbc7bb3b266c19c33f1e696049d70`, non scellée, gardée intacte). **Un seul changement, sur le mot de la mère : le plafond d'arrêt passe de 4,26 à 4,30 USD, soit 2,15 par essai**, pour que le second essai soit garanti au taux prudent de 2,227 caractères par jeton ; le total avec la course passe de 118,74 à 118,78. Le texte servi, la borne de 52 000 caractères, les deux taux et tous les autres montants sont ceux de la v6. L'erratum nommé est sa quatrième passe, qui ajoute à la troisième une règle de lecture côté session et ne touche ni le texte servi ni un montant. La v7 remplace aussi, pour cet appel, le devis v3 (`e9f9ecd80f2dfb869671c22cb76a2450c7a18dad9c8db84a1fc3b86306ab63c7`, scellé, non modifié), écrit pour le mandat v3 sans erratum et pour une sortie de 40 000 caractères.
- Statut : pièce de travail, **à contrôler avant scellement** ; un devis est une pièce décisive. Aucun appel, aucune dépense, aucune clé lue ni nommée. Rien ne part sans le mot de Lazar.
- Calcul : `calcul_devis_auteur_mondes_plantes_v7.py`, sortie `calcul-devis-auteur-mondes-plantes-v7.json`, même dossier ; empreintes à la table. Joué deux fois sous Python 3.13.18 (`python3 -B`), sorties égales à l'octet (`cmp` muet). Arithmétique seule, en décimaux exacts.
- Aucun nom de modèle ni de fournisseur : les candidats sont dits par relais. Montants en USD.

## 0. Verdict

Un seul appel payant : le texte servi, tel quel, à un modèle de la troisième lignée, sur le deuxième relais, candidat R2-a. Deux essais au plus.

| grandeur | au taux de la table, 2,5 caractères par jeton | au taux prudent, 2,227 caractères par jeton |
|---|---|---|
| entrée, le texte servi, 27 468 octets | 10 988 jetons | 12 335 jetons |
| sortie bornée, 52 000 caractères | 20 800 jetons | 23 350 jetons |
| marge de la sortie sous 23 808 jetons (provision comptée dans le plafond) | 3 008 | **458** |
| cas bas | 0,46 | 0,52 |
| cas haut | 4,24 (4,23896) | 4,27 (4,26590) |
| pire | 4,2592 | 4,28864 |

| | |
|---|---|
| plafond de sortie, à chaque essai | 32 000 jetons ; provision de réflexion 8 192 |
| **plafond d'arrêt** | **4,30** (2,15 par essai) |
| total avec la course (114,48) | **118,78**, marge 1,22 sous le plafond indicatif de 120 |

- **Ligne de GO à demander : 4,30 USD**, deux essais au plus à 2,15 chacun. Les devis v1 à v6 demandaient 4,26.
- **La sortie tient dans le plafond aux deux taux**, quelle que soit la façon dont l'interface compte la provision de réflexion (§ 2).
- **Le plafond d'arrêt tient le pire de deux essais aux deux taux** : 4,2592 au taux de la table, **4,28864 au taux prudent, sous 4,30**, avec 0,01136 de marge. **Le second essai est garanti** : après un premier essai joué jusqu'au bout de ses plafonds au taux prudent (2,14432), il reste 2,15568, plus que le pire d'un second essai (§ 2).
- **Aucune de ces lignes n'est une mesure de cet appel.** Aucun auteur de mondes n'a jamais été appelé. Les cas bas et haut sont des règles de ma main.
- Repère, qui n'entre dans aucun total : trois consultations réelles de ce jour sur un énoncé neutre ont coûté 0,74, 0,50 et 0,51 (`registres/decisions.md`, R-4416).

## 1. Sources de chaque chiffre

| clé | chiffre | source | empreinte |
|---|---|---|---|
| S3 | prix par million de jetons en entrée et en sortie ; plafond de sortie ; plafond de relance ; provision de réflexion ; garde de 2,5 caractères par jeton | table des espèces du collisionneur v9 v3, `docs/notes/collisionneur-v9/collisionneur_v9_v3.py` sur `origin/main` (commit `fe5e7cb4f8b8a53083a6240840b5698117fb718a`), lignes 100 à 141 | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910`, selon le devis v1 et la contre-lecture (`9ea0ab895fc5bbf6a7226cf11778697da2f0d3ede79d997c43879df50b70ace5`, § 6), qui a vérifié ces lignes ; **non rouverte par moi** |
| T2 | taux prudent de 2,227 caractères par jeton | mot de la mère, qui le dit « relevé » ; **je n'ai pas vu ce relevé**, ni sur quel texte il est pris : il est cité ici comme une hypothèse prudente, non comme une mesure | — |
| M1 | entrée : 27 468 octets, borne haute des caractères du texte servi | le mandat v3 avec son erratum 1 appliqué, troisième passe, `essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3-erratum-1-applique-v3.md`, ce dossier ; `wc -c` | `f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008` |
| E1 | sortie bornée à 52 000 caractères ; quarante témoins au plus | erratum 1 du mandat v3, quatrième passe, `erratum-1-mandat-auteur-mondes-plantes-v3-v4.md`, ce dossier, § 1 | `1f9e907744a6e1188c403e8f9266210718dbb334b85efe62420a2beeafd30951` |
| R1 | garde d'envoi à 30 000 caractères ; deux essais au plus | règles du rédacteur | — |
| R2 | premier essai de R2-a au plafond de relance, 32 000 jetons de sortie | contre-lecture, § 6, retouche 2 | `9ea0ab895fc5bbf6a7226cf11778697da2f0d3ede79d997c43879df50b70ace5` |
| C1 | devis de la course : 114,48 ; plafond indicatif de la course : 120 | devis v3 de la course, scellé ; `registres/go.md` sur `origin/main`, GO-2026-11-21-16 | `a057cf254502b333de815a6842a6e9304cc41280cb0f0ced03db201f417b6ec7` ; `ec9baf4f0651c831c64cacef408027e179e96ea547133bb32de22be24f51be3d` |
| S7 | coûts réels de trois consultations : 0,74 ; 0,50 ; 0,51 | `registres/decisions.md` sur `origin/main`, R-4416, relue au commit `aea06e6383b1a5ebb6936170e8b29b5faaa83e16` | copie de lecture `0d1f19d10e3f6c447166166a5c9098fb9b66a5ac88ef3df1bcfa35f1febd29ec` |
| S9 | la phrase « Aucune dépense avant ce scellement, le devis contre-lu et une ligne de GO. » | scellement de la conception, `prereg/ideation-seuil-moniteurs-v1/scellement-conception-course-seuil-et-moniteurs-v1.md` sur `origin/main`, même commit, ligne 10 | `4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07` |

**Le tarif du candidat R2-a**, selon la table S3, sans que j'aie ouvert la page qu'elle cite : compté à 10 et 50 par million de jetons, en borne haute ; tarif lu sur une page versée et scellée : 2 et 10 jusqu'au 30 novembre 2026, 4 et 20 dès le 1ᵉʳ décembre. Le cas bas le compte à 4 et 20 : c'est le tarif le plus bas qui vaudra encore après le 1ᵉʳ décembre. La date de l'appel n'est pas connue.

## 2. Le calcul

**Deux taux.** La table donne une garde de 2,5 caractères par jeton ; tous les devis depuis la v1 l'emploient. La mère rapporte un taux relevé de 2,227, plus dur : il compte plus de jetons pour un même texte. Le calcul est donné aux deux, pour l'entrée comme pour la sortie.

Entrée : le texte servi, 27 468 caractères au plus ; il tient sous la garde d'envoi de 30 000 caractères, avec 2 532 caractères de marge. Sortie : 52 000 caractères au plus par la forme fixe.

| | à 2,5 | à 2,227 |
|---|---|---|
| entrée du texte servi | 10 988 jetons | 12 335 jetons |
| entrée à la garde d'envoi | 12 000 jetons | 13 472 jetons |
| sortie bornée | 20 800 jetons | 23 350 jetons |

| cas | essais | ce qui est compté | prix | à 2,5 | à 2,227 |
|---|---|---|---|---|---|
| bas | un | l'entrée du texte servi ; la sortie bornée, sans provision | 4 et 20 | (10 988 × 4 + 20 800 × 20) / 10⁶ = 0,459952, soit 0,46 | (12 335 × 4 + 23 350 × 20) / 10⁶ = 0,51634, soit 0,52 |
| haut | deux | l'entrée du texte servi ; le plafond de 32 000 et la provision de 8 192, chaque fois | 10 et 50 | 2 × (10 988 × 10 + 40 192 × 50) / 10⁶ = 2 × 2,11948 = 4,23896, soit 4,24 | 2 × (12 335 × 10 + 40 192 × 50) / 10⁶ = 2 × 2,13295 = 4,26590, soit 4,27 |
| pire | deux | l'entrée à la garde d'envoi ; le plafond de 32 000 et la provision de 8 192, chaque fois | 10 et 50 | 2 × (12 000 × 10 + 40 192 × 50) / 10⁶ = 2 × 2,1296 = 4,2592 | 2 × (13 472 × 10 + 40 192 × 50) / 10⁶ = 2 × 2,14432 = 4,28864 |

**Le plafond d'arrêt est le pire par essai au taux le plus dur des deux, arrondi au cent vers le haut, fois deux** : 2,14432 au taux prudent, soit 2,15 par essai, 4,30 en tout. Les devis v1 à v6 le prenaient au taux de la table : 2,1296, soit 2,13 par essai, 4,26 en tout.

**Supposition dite** : la provision de réflexion est facturée au prix de la sortie, en plus du plafond de sortie. Le pire est donc compté comme si elle s'ajoutait au plafond.

**La sortie tient dans le plafond, aux deux taux et dans les deux lectures.** On ne sait pas si l'interface compte la provision de réflexion à côté du plafond de sortie ou dedans.

| lecture | jetons laissés à la sortie | marge à 2,5 (sortie de 20 800) | marge à 2,227 (sortie de 23 350) |
|---|---|---|---|
| provision comptée à côté | 32 000 | 11 200 | 8 650 |
| provision comptée dedans, la plus dure | 32 000 − 8 192 = 23 808 | 3 008 | **458** |

C'est pour cette dernière marge que la borne est à 52 000 caractères : à 55 000, la sortie ferait 24 697 jetons au taux prudent, et il en manquerait 889 dans la lecture la plus dure.

**Ce que le taux prudent fait au plafond d'arrêt.** Seul le coût de l'entrée en dépend : les plafonds de sortie sont comptés en jetons, non en caractères. Au taux prudent, un essai joué jusqu'au bout de ses plafonds coûte 2,13295 avec le texte servi, et 2,14432 à la garde d'envoi. C'est pourquoi le plafond de 2,13 par essai des devis v1 à v6 ne suffisait pas : deux tels essais dépassaient 4,26 de 0,0059 et de 0,02864, et le second ne serait pas parti.

**Le plafond de 4,30 tient le pire de deux essais, aux deux taux.**

| | à 2,5 | à 2,227 |
|---|---|---|
| pire par essai | 2,1296 | 2,14432 |
| pire de deux essais | 4,2592 | **4,28864** |
| plafond d'arrêt | 4,30 | 4,30 |
| marge du plafond sur le pire | 0,0408 | **0,01136** |
| reste après un premier essai au pire | 4,30 − 2,1296 = 2,1704 | 4,30 − 2,14432 = 2,15568 |
| le pire d'un second essai tient dans ce reste | oui (2,1296 ≤ 2,1704) | **oui (2,14432 ≤ 2,15568)** |

Un essai ne coûte son maximum que si la réflexion et la sortie emploient tout leur plafond.

**Pour mémoire, les deux autres candidats des devis v1 à v6**, calculés par le même programme avec la même entrée, la même sortie et la même règle de plafond. **Ils ne sont pas proposés** : leur tarif reste « à relever », et la ligne ci-dessous ne les vise pas.

| candidat | cas bas, à 2,5 et à 2,227 | cas haut, à 2,5 et à 2,227 | pire, à 2,5 et à 2,227 | plafond d'arrêt |
|---|---|---|---|---|
| R2-b, deuxième relais, tarif rapporté, réglages supposés | 0,46 et 0,52 | 4,02 et 4,03 | 4,03 et 4,04 | 4,04 (2,02 par essai) |
| R3, troisième relais, tarif supposé | 1,15 et 1,29 | 3,42 et 3,45 | 3,44 et 3,47 | 3,48 (1,74 par essai) |

## 3. Le plafond d'arrêt et les essais permis

- **Plafond par essai** : le plafond de sortie et la provision sont passés à l'interface ; le coût d'un essai ne peut pas les dépasser. Un second essai ne part que si son pire tient dans ce qui reste du plafond d'arrêt.
- **Refus du modèle ou d'un classifieur de sûreté : aucun essai de plus.** L'appel est consigné tel quel, non relancé, non reformulé (liste d'arrêt du préenregistrement court, point 1). Passer à un autre candidat demande un mot neuf.
- **Sortie illisible** (le § 6 du texte servi, points 1 et 2 : forme ou complétude), **dite telle par le programme de vérification, écrit et essayé avant l'envoi, jamais à la main** : **un second essai, un seul**, avec le même texte à l'octet, au même plafond de 32 000 jetons. Après deux sorties illisibles : arrêt, les deux sorties scellées, rien n'est réparé à la main.
- **Sortie lisible dont une famille ou un monde n'a pas de vérité exacte, ou pas ses deux témoins** : aucun essai de plus. Ce n'est pas une sortie illisible (texte servi, § 6, point 2) : la famille ou le monde est écarté au scellement, et c'est dit. Il en va de même d'une famille dont le recalcul rend l'issue « indécise à la borne » (erratum 1 du mandat, quatrième passe, § 3).
- **Sortie lisible dont des valeurs vraies s'écartent de notre calcul** : aucun essai de plus. Ce n'est pas une faute de forme ; l'audit est fait dans les deux sens.
- **Modèle servi différent du modèle demandé** : arrêt (liste d'arrêt, point 11).
- **Entrée de plus de 30 000 caractères** : refusée avant l'envoi.

## 4. Ce qui n'est pas dans ce devis

1. **Le monde à K actions** du moniteur de dissonance : sur devis à part, avec sa ligne (ordre de course, § 7, changement 3). Cet appel ne le paie pas.
2. La vérification de la sortie, le programme de vérification, le programme scellé de vérité des dix-sept témoins imposés, le générateur et le programme de mesure : sessions de place, zéro dollar d'appels. Leur place au calendrier est au § 6 du rapport v2 du rédacteur (`b4b1fdbb7e8038668f0fef7cca062dc7212a997071320a1ffdcd277b1cb7698e`), que le rapport v3 (`6a706f4c8dcdaad93796396e34694409a36b7a1f36a4c9a451cf73d9b2576251`) complète sans le changer.
3. Le reste de la course : devis v3 de la course, 114,48 USD, inchangé. **Cet appel n'y figure pas** : la ligne demandée ici s'y ajoute, et le total (118,78) reste sous le plafond indicatif de 120 de GO-2026-11-21-16, avec une marge de 1,22.
4. **Le nombre de mondes ne change pas ce devis.** L'auteur ne lit aucune des propositions éprouvées. Son appel est borné par le plafond de sortie, non par le nombre de règles à jouer.
5. Le solde de la clé du relais retenu : non lu. Le devis v3 de la course dit du deuxième relais que « la carte paie au-delà du crédit, jusqu'au cas haut des appels déjà accordés » : le mot sur la carte est à étendre à cet appel, ou le solde à relever le jour même.

## 5. Décision demandée

**Décision en une phrase.** Accorder, ou non, une ligne de calcul de 4,30 USD pour un appel à l'auteur des mondes plantés, sur le deuxième relais, deux essais au plus, par exception écrite à une phrase du scellement de la conception.

**Enjeu.** Sans mondes scellés, ni la mise en fiches ni l'étage de la course ne peuvent partir. La dépense est de l'ordre de 0,46 à 4,30 USD.

**L'exception, et pourquoi elle est nécessaire.** Le scellement de la conception (`4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07`, ligne 10) dit du préenregistrement court : « Aucune dépense avant ce scellement, le devis contre-lu et une ligne de GO. » Or ce préenregistrement attend les mondes plantés, et seul cet appel payant les produit. Sans exception écrite, la ligne et le scellement se contredisent. L'exception ne vaut que pour cet appel et pour ce montant ; elle ne touche aucune autre dépense de la course.

**Options.**
- (a) Accorder la ligne. Avantage : les mondes peuvent être écrits, puis scellés ; tarif lu sur page versée ; la sortie tient dans le plafond aux deux taux, et le second essai est garanti aux deux taux. Inconvénient : une dépense avant le scellement du préenregistrement court, par exception ; tarif compté en borne haute ; quatre cents de plus que les devis v1 à v6.
- (b) Ne pas l'accorder. Avantage : aucune exception à un texte scellé. Inconvénient : la course ne part pas, ou les mondes sont à écrire par une lignée qui programme ou met en forme les règles.

**Recommandation : (a), confiance 0,6.**

**Défaut sous 48 heures : aucun.** C'est une dépense, et une exception à un texte scellé.

**Ligne de GO proposée**, à la lettre :

> **Course « seuil et moniteurs », auteur des mondes plantés** (GO-2026-11-21-16) : un appel au deuxième relais, par un modèle de la troisième lignée, qui reçoit tel quel le texte servi, le mandat v3 avec son erratum 1 appliqué (`f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008` ; erratum 1, quatrième passe, `1f9e907744a6e1188c403e8f9266210718dbb334b85efe62420a2beeafd30951`), et rend les familles de mondes, leurs témoins et leur table. **Appel de préparation, accordé par exception à la phrase « Aucune dépense avant ce scellement » du scellement de la conception (`4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07`), par le mot de Lazar : le préenregistrement court attend les mondes que seul cet appel produit ; l'exception ne vaut que pour cet appel et ce montant.** Départ quand le texte servi, son erratum et ce devis sont contrôlés et scellés, et quand le programme de vérification de la sortie est écrit et essayé ; le programme de vérité des dix-sept témoins imposés est scellé avant toute lecture de la sortie. Deux essais au plus, chacun à 32 000 jetons de sortie, le second seulement après une sortie dite illisible par programme, jamais après un refus ; plafond par essai 2,15 USD ; arrêt net au plafond. Le monde à K actions n'y est pas. | 4,30 USD |

## 6. Réserves

1. Cette v7 et son programme ne sont pas contrôlés.
2. Les prix, les plafonds et les provisions sont ceux des calculs v2 à v6, repris sans rouvrir la table du collisionneur.
3. **Le taux de 2,227 n'est pas une mesure que j'aie vue.** S'il vaut pour la sortie en JSON, il ne vaut pas forcément pour l'entrée, un texte en français ; je l'ai appliqué aux deux par prudence. À ce taux, la marge de la sortie dans la lecture la plus dure est de 458 jetons, soit 2 % : un taux réel sous 2,185 caractères par jeton la ferait disparaître.
4. **Le plafond de 4,30 tient le pire au taux prudent avec 1,1 cent de marge** (§ 2). Un taux réel plus dur sur l'entrée peut la reprendre : le pire d'un essai dépasse 2,15 quand l'entrée à la garde d'envoi dépasse 14 040 jetons, soit sous 2,137 caractères par jeton environ. L'arrêt net borne la dépense dans tous les cas ; ce qui serait alors perdu, c'est la garantie du second essai.
5. Que 52 000 caractères suffisent à quarante témoins n'est pas établi par moi : la mère rapporte un profil moyen de 51 467 caractères, soit 533 de moins que la borne ; le texte servi dit à l'auteur quoi réduire d'abord.
6. Le modèle de l'expérimentateur (nœud N4) n'est pas nommé par Lazar à ma connaissance : si l'expérimentateur était du deuxième relais, l'auteur des mondes ne pourrait pas en être (rapport v2, D-L2).
