# Devis — l'appel à l'auteur des mondes plantés, course « seuil et moniteurs » — v3

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Écrit le 2026-11-21, après la vérification rendue après 08:18Z.
- Version : **la v3 remplace la v2** (`bcd0117884aa58b6c845bbeb682e00f313d97319761be8d92381ab4a47a76a23`, gardée intacte) après la vérification `e21edffb0cd8c5dc9ff9e3b3d5fb786db63a1c70ab4385b3c70cf0b7f091ee1f` (« À corriger, pour la lettre seulement » ; devis v2 « juste »). **Un seul changement de fond : la taille du texte servi**, 27 421 octets au lieu de 27 310, parce que le texte servi reçoit deux remplacements (son § 4). **Aucun montant arrondi ne change**, ni plafond, ni total ; seuls des montants exacts bougent à la quatrième décimale (§ 2). La v2 remplaçait la v1 (`4f5dca99a527586228480fe629269fe29a37ecb13b7ab93e4c01c4b3f43409ae`) après la contre-lecture `9ea0ab895fc5bbf6a7226cf11778697da2f0d3ede79d997c43879df50b70ace5`, dont elle portait les trois retouches : la taille du texte servi (§ 2) ; le premier essai du candidat R2-a au plafond de relance (§ 2) ; l'exception écrite à une phrase du scellement de la conception, dans la ligne de GO (§ 5).
- Statut : **pièce de travail (classe C) ; la v3 porte la vérification du contre-lecteur.** Aucun appel, aucune dépense, aucune clé lue ni nommée. Rien ne part sans le mot de Lazar.
- Calcul : `calcul_devis_auteur_mondes_plantes_v3.py`, sortie `calcul-devis-auteur-mondes-plantes-v3.json`, même dossier ; empreintes à la table. Joué deux fois sous Python 3.13.18 (`python3 -B`), sorties égales à l'octet (`cmp` muet). Arithmétique seule, en décimaux exacts.
- Aucun nom de modèle ni de fournisseur : les candidats sont dits par relais. Montants en USD.

## 0. Verdict

Un seul appel payant : le mandat de l'auteur v3, servi tel quel, à un modèle de la troisième lignée. Deux essais au plus.

| candidat | cas bas | cas haut | pire | plafond d'arrêt |
|---|---|---|---|---|
| **R2-a**, deuxième relais, tarif lu sur page versée, compté en borne haute | 0,36 | 4,24 | 4,26 | **4,26** (2,13 par essai) |
| R2-b, deuxième relais, tarif rapporté, réglages supposés | 0,36 | 4,02 | 4,03 | 4,04 (2,02 par essai) |
| R3, troisième relais, tarif supposé | 0,91 | 3,42 | 3,44 | 3,44 (1,72 par essai) |

- **Relais recommandé : le deuxième, candidat R2-a.** Raisons au rapport v2, § 4.
- **Ligne de GO à demander : 4,26 USD**, plafond d'arrêt, deux essais au plus à 2,13 chacun. **Le plafond ne change pas depuis la v1** : il compte la garde d'envoi de 30 000 caractères, non la taille du mandat.
- **Ce qui change depuis la v1** : le cas haut de R2-a passe de 3,51 à 4,24, parce que son premier essai part à 32 000 jetons de sortie et non à 18 000 ; les cas hauts de R2-b et de R3 montent d'un et de trois cents, et le cas bas de R3 d'un cent, par la seule taille du mandat v3. Chaque cas haut reste sous son plafond ; le programme le vérifie.
- **Ce qui change depuis la v2** : rien de ce tableau. L'entrée passe de 10 924 à 10 969 jetons ; aucun montant arrondi ne bouge.
- **Aucune de ces lignes n'est une mesure.** Aucun auteur de mondes n'a jamais été appelé. Les plafonds tiennent la dépense ; les cas bas et haut sont des règles de ma main.
- Repère, qui n'entre dans aucun total : trois consultations réelles de ce jour sur un énoncé neutre ont coûté 0,74, 0,50 et 0,51 (`registres/decisions.md`, R-4416).

## 1. Sources de chaque chiffre

| clé | chiffre | source | empreinte |
|---|---|---|---|
| S3 | prix par million de jetons en entrée et en sortie ; plafond de sortie ; plafond de relance ; provision de réflexion ; garde de 2,5 caractères par jeton | table des espèces du collisionneur v9 v3, `docs/notes/collisionneur-v9/collisionneur_v9_v3.py` sur `origin/main` (commit `fe5e7cb4f8b8a53083a6240840b5698117fb718a`), lignes 100 à 141 | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910`, selon la v1 et la contre-lecture ; **non rouverte par moi** |
| M1 | entrée : 27 421 octets, borne haute des caractères du mandat v3 ; sortie bornée à 40 000 caractères | `mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md`, ce dossier, § 4.1 ; `wc -c` | à la table |
| R1 | garde d'envoi à 30 000 caractères ; deux essais au plus | règles du rédacteur | — |
| R2 | premier essai de R2-a au plafond de relance, 32 000 jetons de sortie | contre-lecture, § 6, retouche 2 | `9ea0ab895fc5bbf6a7226cf11778697da2f0d3ede79d997c43879df50b70ace5` |
| S7 | coûts réels de trois consultations : 0,74 ; 0,50 ; 0,51 | `registres/decisions.md` sur `origin/main`, R-4416 ; relue par moi au commit `aea06e6383b1a5ebb6936170e8b29b5faaa83e16` | copie de lecture `0d1f19d10e3f6c447166166a5c9098fb9b66a5ac88ef3df1bcfa35f1febd29ec` |
| S8 | plafond de 4 USD par appel des consultations de ce jour ; plafond indicatif de 120 USD de la course | `registres/go.md`, même commit, GO-2026-11-21-20 et GO-2026-11-21-16 | `ec9baf4f0651c831c64cacef408027e179e96ea547133bb32de22be24f51be3d`, recalculée |
| S9 | la phrase « Aucune dépense avant ce scellement, le devis contre-lu et une ligne de GO. » | scellement de la conception, `prereg/ideation-seuil-moniteurs-v1/scellement-conception-course-seuil-et-moniteurs-v1.md` sur `origin/main`, même commit, ligne 10 | `4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07`, recalculée |

**Ce que la table S3 dit de chaque tarif**, sans que j'aie ouvert les pages qu'elle cite ; le contre-lecteur a vérifié ces lignes sur la table (son § 6) :

| candidat | prix compté (entrée, sortie) | ce que la table en dit | statut ici |
|---|---|---|---|
| R2-a | 10 et 50 | borne haute ; tarif lu sur une page versée et scellée : 2 et 10 jusqu'au 30 novembre 2026, 4 et 20 dès le 1ᵉʳ décembre | lu par la table, **non revérifié par moi** |
| R2-b | 4 et 20 | « RAPPORTÉ » ; 2 et 10 jusqu'au 1ᵉʳ décembre ; plafonds et provision : « réglages supposés » | **à relever** |
| R3 | 10 et 50 | tarif du modèle servi non lu : « même barème, SUPPOSÉ » | **à relever** |

Le cas bas compte R2-a et R2-b à 4 et 20 : c'est le tarif le plus bas qui vaudra encore après le 1ᵉʳ décembre. La date de l'appel n'est pas connue.

## 2. Le calcul

Entrée : le mandat v3, 27 421 caractères au plus, soit 10 969 jetons à la garde de 2,5 caractères par jeton ; il tient sous la garde d'envoi de 30 000 caractères, avec 2 579 caractères de marge. Sortie : 40 000 caractères au plus par la forme fixe, soit 16 000 jetons.

| cas | essais | entrée | sortie comptée | prix |
|---|---|---|---|---|
| bas | un | 10 969 jetons | 16 000 jetons, sans provision | prix bas |
| haut | deux | 10 969 jetons chacun | le plafond du premier essai, puis le plafond de relance, provision comprise chaque fois | prix compté |
| pire | deux | 12 000 jetons chacun (garde d'envoi) | le plafond de relance et la provision, chaque fois | prix compté |

| candidat | plafond du premier essai | plafond de relance | provision | essai du cas haut | pire par essai |
|---|---|---|---|---|---|
| R2-a | **32 000** (18 000 à la v1) | 32 000 | 8 192 | 2,11929 | 2,1296 |
| R2-b | 65 536 | 65 536 | 32 768 | 2,009956 | 2,01408 |
| R3 | 32 000 | 32 000 | 0 | 1,70969 | 1,72 |

**Supposition dite** : la provision de réflexion est facturée au prix de la sortie, en plus du plafond de sortie. La table S3 le compte ainsi pour R2-b. Le pire est donc compté comme si elle s'ajoutait au plafond.

**Pourquoi R2-a part à 32 000 dès le premier essai** (retouche 2 de la contre-lecture). On ne sait pas si l'interface compte la provision de réflexion dans le plafond de sortie ou à côté. Si elle la compte dedans, le plafond nominal de 18 000 ne laisse que 18 000 − 8 192 = 9 808 jetons à une sortie qui peut en demander 16 000 : la sortie serait coupée, donc illisible, et un essai sur deux serait perdu. À 32 000, il reste 23 808 jetons dans la lecture la plus dure. Le pire ne change pas : il comptait déjà 32 000 et la provision à chaque essai.

**R3 : son plafond nominal de 8 000 jetons ne contient pas la sortie demandée** (16 000). Le calcul le fait donc partir au plafond de relance dès le premier essai, comme à la v1 ; c'est un réglage neuf pour ce relais.

Le plafond d'arrêt est le pire par essai, arrondi au cent vers le haut, fois deux. Le programme vérifie qu'il tient le pire et le cas haut.

## 3. Le plafond d'arrêt et les essais permis

- **Plafond par essai** : le plafond de sortie et la provision sont passés à l'interface ; le coût d'un essai ne peut pas les dépasser. Un second essai ne part que si son pire tient dans ce qui reste du plafond d'arrêt.
- **Refus du modèle ou d'un classifieur de sûreté : aucun essai de plus.** L'appel est consigné tel quel, non relancé, non reformulé (liste d'arrêt du préenregistrement court, point 1). Passer à un autre candidat demande un mot neuf.
- **Sortie illisible** (le § 6 du mandat v3, points 1 et 2 : forme ou complétude), **dite telle par le programme de vérification, écrit et essayé avant l'envoi, jamais à la main** : **un second essai, un seul**, avec le même mandat à l'octet, au même plafond de 32 000 jetons. Après deux sorties illisibles : arrêt, les deux sorties scellées, rien n'est réparé à la main.
- **Sortie lisible dont une famille ou un monde n'a pas de vérité exacte, ou pas ses deux témoins** : aucun essai de plus. Ce n'est pas une sortie illisible (mandat v3, § 6, point 2) : la famille ou le monde est écarté au scellement, et c'est dit.
- **Sortie lisible dont des valeurs vraies s'écartent de notre calcul** : aucun essai de plus. Ce n'est pas une faute de forme ; l'audit est fait dans les deux sens.
- **Modèle servi différent du modèle demandé** : arrêt (liste d'arrêt, point 11).
- **Entrée de plus de 30 000 caractères** : refusée avant l'envoi.

## 4. Ce qui n'est pas dans ce devis

1. **Le monde à K actions** du moniteur de dissonance : sur devis à part, avec sa ligne (ordre de course, § 7, changement 3). Cet appel ne le paie pas.
2. La vérification de la sortie, le programme de vérification, le programme scellé de vérité des dix-sept témoins imposés, le générateur et le programme de mesure : sessions de place, zéro dollar d'appels. Leur place au calendrier est au rapport v2, § 6.
3. Le reste de la course : devis v3 de la course (`a057cf254502b333de815a6842a6e9304cc41280cb0f0ced03db201f417b6ec7`), 114,48 USD, inchangé. **Cet appel n'y figure pas** : la ligne demandée ici s'y ajoute, et le total (118,74) reste sous le plafond indicatif de 120 de GO-2026-11-21-16, avec une marge de 1,26.
4. **Le nombre de mondes ne change pas ce devis.** La synthèse du collisionneur (`dc734fabb9f4cc96c82fd91c37ae08b5ca7789012fcd47e72668e623c3002522`, sur `origin/main`, commit `e04285cc1ba4ddf49cc2fd4640f66cc4a56b5af3`) compte seize propositions sur vingt-trois qui peuvent prendre une forme fixe. L'auteur n'en lit aucune. Son appel est borné par les plafonds de sortie, non par le nombre de règles à jouer. Le mandat v3 lui demande moins de familles libres (deux au plus) et plus de témoins (ceux du monde M) : la borne de sortie reste à 40 000 caractères.
5. Le solde de la clé du relais retenu : non lu. Le devis v3 de la course dit du deuxième relais que « la carte paie au-delà du crédit, jusqu'au cas haut des appels déjà accordés » : le mot sur la carte est à étendre à cet appel, ou le solde à relever le jour même.

## 5. Décision demandée

**Décision en une phrase.** Accorder, ou non, une ligne de calcul de 4,26 USD pour un appel à l'auteur des mondes plantés, sur le deuxième relais, deux essais au plus, **par exception écrite à une phrase du scellement de la conception**.

**Enjeu.** Sans mondes scellés, ni la mise en fiches ni l'étage de la course ne peuvent partir. La dépense est de l'ordre de 0,36 à 4,26 USD.

**L'exception, et pourquoi elle est nécessaire** (retouche 3 de la contre-lecture). Le scellement de la conception (`4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07`, ligne 10) dit du préenregistrement court : « Aucune dépense avant ce scellement, le devis contre-lu et une ligne de GO. » Or ce préenregistrement attend les mondes plantés, et seul cet appel payant les produit. Sans exception écrite, la ligne et le scellement se contredisent. L'exception ne vaut que pour cet appel et pour ce montant ; elle ne touche aucune autre dépense de la course.

**Options.**
- (a) R2-a, 4,26. Avantage : tarif lu sur page versée, plafonds déjà employés. Inconvénient : compté en borne haute, donc le plafond le plus haut des trois ; premier essai à 32 000 jetons, un réglage plus large que son plafond nominal.
- (b) R2-b, 4,04. Avantage : la plus grande provision de réflexion. Inconvénient : tarif et réglages à relever avant la ligne.
- (c) R3, 3,44. Avantage : le plafond le plus bas ; laisse les deux modèles du deuxième relais libres pour la mise en fiches. Inconvénient : tarif à relever ; plafond nominal trop court pour la sortie.

**Recommandation : (a), confiance 0,6.**

**Défaut sous 48 heures : aucun.** C'est une dépense, et une exception à un texte scellé.

**Ligne de GO proposée**, à la lettre :

> **Course « seuil et moniteurs », auteur des mondes plantés** (GO-2026-11-21-16) : un appel au deuxième relais, par un modèle de la troisième lignée, qui reçoit le mandat v3 scellé tel quel et rend les familles de mondes, leurs témoins et leur table. **Appel de préparation, accordé par exception à la phrase « Aucune dépense avant ce scellement » du scellement de la conception (`4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07`), par le mot de Lazar : le préenregistrement court attend les mondes que seul cet appel produit ; l'exception ne vaut que pour cet appel et ce montant.** Départ quand le mandat v3 et ce devis sont contre-lus et scellés, et quand le programme de vérification de la sortie est écrit et essayé ; le programme de vérité des dix-sept témoins imposés est scellé avant toute lecture de la sortie. Deux essais au plus, chacun à 32 000 jetons de sortie, le second seulement après une sortie dite illisible par programme, jamais après un refus ; plafond par essai 2,13 USD ; arrêt net au plafond. Le monde à K actions n'y est pas. | 4,26 USD |
