# Devis — l'appel à l'auteur des mondes plantés, course « seuil et moniteurs » — v1

- Auteur : rédacteur du mandat des mondes plantés, modèle F. Écrit le 2026-11-21 ; relevé de `date -u` : 07:48:48Z.
- Statut : **pièce de travail (classe C), non contre-lue.** Aucun appel, aucune dépense, aucune clé lue ni nommée. Rien ne part sans le mot de Lazar.
- Calcul : `calcul_devis_auteur_mondes_plantes_v1.py`, sortie `calcul-devis-auteur-mondes-plantes-v1.json`, même dossier ; empreintes à la table. Joué deux fois sous Python 3.13.18 (`python3 -B`), sorties égales à l'octet (`cmp` muet). Arithmétique seule, en décimaux exacts.
- Aucun nom de modèle ni de fournisseur : les candidats sont dits par relais. Montants en USD.

## 0. Verdict

Un seul appel payant : le mandat de l'auteur, servi tel quel, à un modèle de la troisième lignée. Deux essais au plus.

| candidat | cas bas | cas haut | pire | plafond d'arrêt |
|---|---|---|---|---|
| **R2-a**, deuxième relais, tarif lu sur page versée, compté en borne haute | 0,36 | 3,51 | 4,26 | **4,26** (2,13 par essai) |
| R2-b, deuxième relais, tarif rapporté, réglages supposés | 0,36 | 4,01 | 4,03 | 4,04 (2,02 par essai) |
| R3, troisième relais, tarif supposé | 0,90 | 3,39 | 3,44 | 3,44 (1,72 par essai) |

- **Relais recommandé : le deuxième, candidat R2-a.** Raisons au rapport, § 4.
- **Ligne de GO à demander : 4,26 USD**, plafond d'arrêt, deux essais au plus à 2,13 chacun.
- **Aucune de ces lignes n'est une mesure.** Aucun auteur de mondes n'a jamais été appelé. Les plafonds tiennent la dépense ; les cas bas et haut sont des règles de ma main.
- Repère, qui n'entre dans aucun total : trois consultations réelles de ce jour sur un énoncé neutre ont coûté 0,74, 0,50 et 0,51 (`registres/decisions.md`, R-4416).

## 1. Sources de chaque chiffre

| clé | chiffre | source | empreinte |
|---|---|---|---|
| S3 | prix par million de jetons en entrée et en sortie ; plafond de sortie ; plafond de relance ; provision de réflexion ; garde de 2,5 caractères par jeton | table des espèces du collisionneur v9 v3, `docs/notes/collisionneur-v9/collisionneur_v9_v3.py` sur `origin/main` (commit `fe5e7cb4f8b8a53083a6240840b5698117fb718a`), lignes 100 à 141 | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910`, recalculée |
| M1 | entrée : 24 062 octets, borne haute des caractères du mandat ; sortie bornée à 40 000 caractères | `mandat-auteur-mondes-plantes-seuil-et-moniteurs-v1.md`, ce dossier, § 4.1 ; `wc -c` | à la table |
| R1 | garde d'envoi à 30 000 caractères ; deux essais au plus | règles du rédacteur | — |
| S7 | coûts réels de trois consultations : 0,74 ; 0,50 ; 0,51 | `registres/decisions.md` sur `origin/main`, même commit, R-4416 | `abd6d985c26602b5505db69c892d9eeb303104fa3786a2d02d1af812e64bac9c` |
| S8 | plafond de 4 USD par appel des consultations de ce jour | `registres/go.md`, même commit, GO-2026-11-21-20 | `ec9baf4f0651c831c64cacef408027e179e96ea547133bb32de22be24f51be3d` |

**Ce que la table S3 dit de chaque tarif**, sans que j'aie ouvert les pages qu'elle cite :

| candidat | prix compté (entrée, sortie) | ce que la table en dit | statut ici |
|---|---|---|---|
| R2-a | 10 et 50 | borne haute ; tarif lu sur une page versée et scellée : 2 et 10 jusqu'au 30 novembre 2026, 4 et 20 dès le 1ᵉʳ décembre | lu par la table, **non revérifié par moi** |
| R2-b | 4 et 20 | « RAPPORTÉ » ; 2 et 10 jusqu'au 1ᵉʳ décembre ; plafonds et provision : « réglages supposés » | **à relever** |
| R3 | 10 et 50 | tarif du modèle servi non lu : « même barème, SUPPOSÉ » | **à relever** |

Le cas bas compte R2-a et R2-b à 4 et 20 : c'est le tarif le plus bas qui vaudra encore après le 1ᵉʳ décembre. La date de l'appel n'est pas connue.

## 2. Le calcul

Entrée : le mandat, 24 062 caractères au plus, soit 9 625 jetons à la garde de 2,5 caractères par jeton. Sortie : 40 000 caractères au plus par la forme fixe, soit 16 000 jetons.

| cas | essais | entrée | sortie comptée | prix |
|---|---|---|---|---|
| bas | un | 9 625 jetons | 16 000 jetons, sans provision | prix bas |
| haut | deux | 9 625 jetons chacun | le plafond du premier essai, puis le plafond de relance, provision comprise chaque fois | prix compté |
| pire | deux | 12 000 jetons chacun (garde d'envoi) | le plafond de relance et la provision, chaque fois | prix compté |

| candidat | plafond du premier essai | plafond de relance | provision | pire par essai |
|---|---|---|---|---|
| R2-a | 18 000 | 32 000 | 8 192 | 2,1296 |
| R2-b | 65 536 | 65 536 | 32 768 | 2,01408 |
| R3 | 32 000 | 32 000 | 0 | 1,72 |

**Supposition dite** : la provision de réflexion est facturée au prix de la sortie, en plus du plafond de sortie. La table S3 le compte ainsi pour R2-b.

**R3 : son plafond nominal de 8 000 jetons ne contient pas la sortie demandée** (16 000). Celui de R2-a (18 000) la contient, avec 2 000 jetons de marge. Le calcul le fait donc partir au plafond de relance dès le premier essai ; c'est un réglage neuf pour ce relais.

Le plafond d'arrêt est le pire par essai, arrondi au cent vers le haut, fois deux. Le programme vérifie qu'il tient le pire.

## 3. Le plafond d'arrêt et les essais permis

- **Plafond par essai** : le plafond de sortie et la provision sont passés à l'interface ; le coût d'un essai ne peut pas les dépasser. Un second essai ne part que si son pire tient dans ce qui reste du plafond d'arrêt.
- **Refus du modèle ou d'un classifieur de sûreté : aucun essai de plus.** L'appel est consigné tel quel, non relancé, non reformulé (liste d'arrêt du préenregistrement court, point 1). Passer à un autre candidat demande un mot neuf.
- **Sortie illisible** (le § 6 du mandat, points 1 et 2 : forme ou complétude) : **un second essai, un seul**, avec le même mandat à l'octet, au plafond de relance. Après deux sorties illisibles : arrêt, les deux sorties scellées, rien n'est réparé à la main.
- **Sortie lisible dont des valeurs vraies s'écartent de notre calcul** : aucun essai de plus. Ce n'est pas une faute de forme ; l'audit est fait dans les deux sens.
- **Modèle servi différent du modèle demandé** : arrêt (liste d'arrêt, point 11).
- **Entrée de plus de 30 000 caractères** : refusée avant l'envoi.

## 4. Ce qui n'est pas dans ce devis

1. **Le monde à K actions** du moniteur de dissonance : sur devis à part, avec sa ligne (ordre de course v4, § 7, point 3). Cet appel ne le paie pas.
2. La contre-lecture de la sortie, le programme de vérification, le générateur et le programme de mesure : sessions de place, zéro dollar d'appels.
3. Le reste de la course : devis v3 de la course (`a057cf254502b333de815a6842a6e9304cc41280cb0f0ced03db201f417b6ec7`), 114,48 USD, inchangé. **Cet appel n'y figure pas** : la ligne demandée ici s'y ajoute, et le total (118,74) reste sous le plafond indicatif de 120 de GO-2026-11-21-16, avec une marge de 1,26.
4. **Le nombre de mondes ne change pas ce devis.** La synthèse du collisionneur (`dc734fabb9f4cc96c82fd91c37ae08b5ca7789012fcd47e72668e623c3002522`, sur `origin/main`, commit `e04285cc1ba4ddf49cc2fd4640f66cc4a56b5af3`) compte seize propositions sur vingt-trois qui peuvent prendre une forme fixe. L'auteur n'en lit aucune. Son appel est borné par les plafonds de sortie, non par le nombre de règles à jouer. Seul ajout tiré d'elle : la famille I et les témoins T14 à T17, sur le nul conditionné par l'échec final ; ils ont porté la borne de sortie de 36 000 à 40 000 caractères, sans toucher au pire. Seize formes fixes pour onze places de candidates : c'est le devis de la course que ce compte touche, non celui-ci.
5. Le solde de la clé du relais retenu : non lu. Le devis v3 de la course dit du deuxième relais que « la carte paie au-delà du crédit, jusqu'au cas haut des appels déjà accordés » : le mot sur la carte est à étendre à cet appel, ou le solde à relever le jour même.

## 5. Décision demandée

**Décision en une phrase.** Accorder, ou non, une ligne de calcul de 4,26 USD pour un appel à l'auteur des mondes plantés, sur le deuxième relais, deux essais au plus.

**Enjeu.** Sans mondes scellés, ni la mise en fiches ni l'étage de la course ne peuvent partir. La dépense est de l'ordre de 0,36 à 4,26 USD.

**Options.**
- (a) R2-a, 4,26. Avantage : tarif lu sur page versée, plafonds déjà employés, la sortie tient dans le plafond nominal. Inconvénient : compté en borne haute, donc le plafond le plus haut des trois.
- (b) R2-b, 4,04. Avantage : la plus grande provision de réflexion. Inconvénient : tarif et réglages à relever avant la ligne.
- (c) R3, 3,44. Avantage : le plafond le plus bas ; laisse les deux modèles du deuxième relais libres pour la mise en fiches. Inconvénient : tarif à relever ; plafond nominal trop court pour la sortie.

**Recommandation : (a), confiance 0,6.**

**Défaut sous 48 heures : aucun.** C'est une dépense.

**Ligne de GO proposée**, à la lettre :

> **Course « seuil et moniteurs », auteur des mondes plantés** (GO-2026-11-21-16) : un appel au deuxième relais, par un modèle de la troisième lignée, qui reçoit le mandat scellé tel quel et rend les familles de mondes, leurs témoins et leur table ; départ quand le mandat et ce devis sont contre-lus et scellés ; deux essais au plus, le second seulement après une sortie illisible, jamais après un refus ; plafond par essai 2,13 USD ; arrêt net au plafond. Le monde à K actions n'y est pas. | 4,26 USD |
