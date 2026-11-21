# Devis — l'appel à l'auteur des mondes plantés, course « seuil et moniteurs » — v4

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Écrit le 2026-11-21 ; relevé de `date -u` : 09:13:44Z.
- Version : **la v4 est proposée pour remplacer la v3** (`e9f9ecd80f2dfb869671c22cb76a2450c7a18dad9c8db84a1fc3b86306ab63c7`, scellée, non modifiée, lue avec son erratum 1 `d18bbb84b247b359d868cb266ccdf1ca5c280b3fe1d2c9bb59be5bf0b4da3868`). Cause : l'erratum 1 du mandat de l'auteur v3 (`erratum-1-mandat-auteur-mondes-plantes-v3.md`, même dossier) porte la borne de sortie de 40 000 à 60 000 caractères. **Le devis v3 ne tient plus tel quel** : sous la lecture la plus dure de la provision de réflexion, son plafond de 32 000 jetons ne contient plus la sortie du candidat recommandé.
- Portée : cette v4 ne réécrit que ce qui change. **Les § 1 (sources), § 3 (plafond d'arrêt et essais permis) et § 4 (ce qui n'est pas dans le devis) du devis v3 valent encore**, lus avec « mandat v3, erratum 1 appliqué » pour « mandat v3 », et avec la borne de sortie retenue pour « 40 000 caractères ».
- Statut : pièce de travail, **non contre-lue** ; un devis est une pièce décisive, sa chaîne reste à faire. Aucun appel, aucune dépense, aucune clé lue ni nommée. Rien ne part sans le mot de Lazar.
- Calcul : `calcul_devis_auteur_mondes_plantes_v4.py`, sortie `calcul-devis-auteur-mondes-plantes-v4.json`, même dossier. Joué deux fois sous Python 3.13.18 (`python3 -B`), sorties égales à l'octet (`cmp` muet). Arithmétique seule, en décimaux exacts.
- Aucun nom de modèle ni de fournisseur. Montants en USD.

## 0. Verdict

1. **Le plafond de relance de 32 000 jetons de sortie tient-il la sortie de 60 000 caractères ? Pas sûrement, pour le candidat R2-a.** 60 000 caractères font 24 000 jetons à la garde de 2,5 caractères par jeton.
   - Si la provision de réflexion se compte **à côté** du plafond : 24 000 ≤ 32 000, il tient, avec 8 000 jetons de marge.
   - Si elle se compte **dedans** : il reste 32 000 − 8 192 = 23 808 jetons à la sortie, et **il en manque 192**.
   - On ne sait pas laquelle des deux lectures est la bonne. Le devis v2 a retenu la plus dure pour faire partir R2-a à 32 000 ; je garde la même règle.
2. **Les candidats R2-b et R3 tiennent dans les deux lectures** (marges de 8 768 et de 8 000 jetons).
3. **L'entrée tient** : la requête servie fait 27 468 octets, soit 10 988 jetons, sous la garde d'envoi de 30 000 caractères. Le pire et les plafonds d'arrêt, qui comptent cette garde, ne dépendent pas de la taille de l'entrée.
4. **Trois façons de s'en sortir** (§ 2). Je recommande de ramener la borne à **55 000 caractères** : la ligne reste à 4,26 USD, aucun réglage neuf.

## 1. Le devis v3 rejoué avec l'erratum (scénario S0)

Entrée : 10 988 jetons. Sortie bornée : 24 000 jetons. Plafonds du devis v3.

| candidat | cas bas | cas haut | pire | plafond d'arrêt | sortie contenue, provision à côté | sortie contenue, provision dedans |
|---|---|---|---|---|---|---|
| **R2-a** | 0,52 (0,36 à la v3) | 4,24 | 4,26 | 4,26 (2,13 par essai) | oui, marge 8 000 | **non, il manque 192 jetons** |
| R2-b | 0,52 (0,36) | 4,02 | 4,03 | 4,04 (2,02 par essai) | oui | oui, marge 8 768 |
| R3 | 1,31 (0,91) | 3,42 | 3,44 | 3,44 (1,72 par essai) | oui | oui, marge 8 000 |

**Montants arrondis qui changent depuis la v3 : les trois cas bas**, parce qu'un cas bas compte la sortie bornée entière. Les cas hauts, les pires et les plafonds d'arrêt ne changent pas : ils comptent les plafonds de sortie, non la borne. Total avec la course, pour R2-a : 118,74, inchangé.

## 2. Trois options pour le candidat R2-a

| | S0 : ne rien changer | S1 : relever le plafond de sortie à 36 000 jetons, aux deux essais | S2 : ramener la borne à 55 000 caractères |
|---|---|---|---|
| sortie bornée | 24 000 jetons | 24 000 jetons | 22 000 jetons |
| contenue, provision dedans | **non** (−192) | oui, marge 3 808 | oui, marge 1 808 |
| cas bas | 0,52 | 0,52 | 0,48 |
| cas haut | 4,24 | 4,64 | 4,24 |
| pire | 4,26 | 4,66 | 4,26 |
| **plafond d'arrêt** | **4,26** (2,13 par essai) | **4,66** (2,33 par essai) | **4,26** (2,13 par essai) |
| total avec la course (114,48) | 118,74, marge 1,26 sous 120 | 119,14, marge 0,86 sous 120 | 118,74, marge 1,26 sous 120 |
| ce que cela demande | rien | un réglage neuf, au-dessus du plafond de relance que dit la table du collisionneur : à relever au relais avant la ligne ; la ligne demandée à Lazar passe de 4,26 à 4,66 | un nombre de l'erratum du mandat et de son jeu de remplacements : 55 000 au lieu de 60 000 ; l'essai se rejoue |

Les valeurs de 36 000 et de 55 000 sont des règles de ma main : 36 000 est le besoin de la lecture la plus dure (24 000 + 8 192 = 32 192) avec une marge de l'ordre de dix pour cent, arrondi au millier ; 55 000 caractères font 22 000 jetons, sous les 23 808 que laisse le plafond de 32 000.

**Ce que je ne sais pas.** Si le relais accepte 36 000 jetons de sortie pour ce modèle. Si 55 000 caractères suffisent à quarante témoins : le vérificateur du programme de vérification compte 32 700 caractères pour une sortie compacte ; 55 000 laisse deux tiers de plus, 60 000 cinq sixièmes de plus. La garde de 2,5 caractères par jeton est elle-même une borne prudente, non une mesure sur du JSON.

## 3. Décision demandée

**Décision en une phrase.** Choisir comment la sortie plus longue tient dans le plafond du candidat R2-a : ne rien changer, relever le plafond, ou ramener la borne.

**Enjeu.** Une sortie coupée est illisible, et un essai payé sur deux est perdu. Le risque n'existe que si la provision se compte dans le plafond et que l'auteur emploie toute sa borne.

**Options.**
- (S0) Ne rien changer : borne à 60 000, plafond à 32 000. Avantage : ni réglage ni texte à reprendre ; la ligne reste à 4,26. Inconvénient : il manque 192 jetons dans la lecture la plus dure ; c'est accepter le risque que le devis v2 a refusé.
- (S1) Plafond de sortie à 36 000 jetons, aux deux essais. Avantage : la borne de 60 000 du mot de la mère est gardée, avec de la marge. Inconvénient : un réglage neuf à relever ; la ligne passe à 4,66 ; la marge sous 120 tombe à 0,86.
- (S2) Borne à 55 000 caractères. Avantage : la ligne reste à 4,26, aucun réglage neuf, marge de 1 808 jetons dans la lecture la plus dure. Inconvénient : 5 000 caractères de moins que le mot de la mère ; l'erratum du mandat change d'un nombre.

**Recommandation : (S2), confiance 0,6.** (S1) en second.

**Défaut sous 48 heures : aucun.** Le choix fixe le montant d'une dépense.

**Ligne de GO proposée**, à la lettre, selon l'option ; seuls le texte servi, le plafond de sortie et le montant changent depuis le devis v3 :

> **Course « seuil et moniteurs », auteur des mondes plantés** (GO-2026-11-21-16) : un appel au deuxième relais, par un modèle de la troisième lignée, qui reçoit le mandat v3 avec son erratum 1 appliqué, scellé, tel quel, et rend les familles de mondes, leurs témoins et leur table. **Appel de préparation, accordé par exception à la phrase « Aucune dépense avant ce scellement » du scellement de la conception (`4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07`), par le mot de Lazar : le préenregistrement court attend les mondes que seul cet appel produit ; l'exception ne vaut que pour cet appel et ce montant.** Départ quand le texte servi et ce devis sont contre-lus et scellés, et quand le programme de vérification de la sortie est écrit et essayé ; le programme de vérité des dix-sept témoins imposés est scellé avant toute lecture de la sortie. Deux essais au plus, chacun à **[S0 et S2 : 32 000 ; S1 : 36 000]** jetons de sortie, le second seulement après une sortie dite illisible par programme, jamais après un refus ; plafond par essai **[S0 et S2 : 2,13 ; S1 : 2,33]** USD ; arrêt net au plafond. Le monde à K actions n'y est pas. | **[S0 et S2 : 4,26 ; S1 : 4,66]** USD |

## 4. Réserves

1. Rien n'est contre-lu : ni cette v4, ni son programme, ni l'erratum du mandat.
2. Les prix, les plafonds et les provisions sont ceux du calcul v3, repris sans rouvrir la table du collisionneur.
3. Les candidats R2-b et R3 gardent leur statut du devis v3 : tarif « à relever ».
