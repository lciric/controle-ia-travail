# Devis — course de l'organisme d'idéation « nouvelles attaques », trois générations — v2

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` : 01:01:43Z, après la lecture des pièces et avant l'écriture.
- Version : la v2 remplace la v1 (`638492f1cc65151c0528ed62f5d13849d4629336a65b80d1db1ba054e61c6268`) après la contre-lecture `contre-lecture-conception-nouvelles-attaques-v1.md` (`ae9d4ae44027476bee4821e72c4e9f9b12f39d10f3dc6749ae60ae61d07c1fed`, verdict « Conforme après corrections ») : corrections C9, C12, C17, C18 et C19 appliquées à texte exact ; la v1 reste archivée, non modifiée. La v2 elle-même n'est pas contre-lue.
- Statut : **pièce de travail, non contre-lue. Rien n'a été lancé ; aucun appel, aucune dépense.** Ce devis n'engage rien : la course ne part qu'après sa contre-lecture et ton accord de calcul, distinct (`GO-2026-11-19-94`).
- Calcul : `calcul_devis_course_nouvelles_attaques_v2.py` (`cefe97837267d4db517c40437dc89288842d1d7dd5252b225fe0e0f05edede9b`), sortie `calcul-devis-course-nouvelles-attaques-v2.json` (`ffecbd1172888b815e6f7af84ae54f52c1991554d6d2ff376481af694e60b7cf`), même dossier. Joué deux fois ; les deux sorties sont égales à l'octet. Processeur seul ; le programme ne lit aucun fichier.
- Les espèces sont désignées par un numéro, de 1 à 5, dans l'ordre du coût réel croissant de leur rôle de proposeur à la course v9, comme au devis de l'héritage v5 (§ 1, table de correspondance). Aucun nom de modèle n'est écrit ici.
- Montants en dollars des États-Unis (USD).

## 0. Verdict

1. **Ligne de course proposée : 450 USD exactement**, soit trois générations à 150 USD de plafond d'arrêt chacune, à la composition de la course v9 (cinq espèces). **Plafond total : 456 USD**, avec deux lignes à part avant la course : l'épreuve des témoins (5 USD) et la sonde de refus (1 USD).
2. Attendu : **218,72 USD** si chaque génération coûte ce qu'a coûté la course v9. Cas haut : 419,43 USD. Au pire : 456 USD ; le lanceur coupe au plafond.
3. **Le crédit de la clé du premier relais ne couvre pas cette ligne** au dernier chiffre que j'ai lu : il resterait environ 162,56 USD pour une part au pire de 450 USD. Le lanceur refuserait le départ. C'est à relever le jour du devis final, et c'est ta décision (§ 6).
4. Deux lignes plus basses sont chiffrées : trois espèces (ligne 195 USD, total 201) et deux espèces (ligne 150 USD, total 156). Elles ont un prix, dit au § 5.

## 1. Sources de chaque chiffre

| clé | chiffre | chemin | empreinte |
|---|---|---|---|
| S1 | coûts réels de la course v9 par rôle : proposeurs 4,17 ; 4,75 ; 7,43 ; 17,58 ; 24,72, onze appels chacun ; aiguilleur 4,59 pour 96 appels ; juges 6,86 et 2,41 pour 94 appels chacun ; course 72,50 ; tentatives attendues 94, 56 et 38 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/devis-heritage-trois-bras-v5.md`, § 1 et § 2 (branche `lot/compte-organisme-v1`) | `30c87fa68d9d6fa5e961edc45764fe58172b1a1b20d45fd3065a678b42f2880d` |
| S2 | course v9 : 72,502472 USD réels sur 150 ; 36,457056 sur la clé du premier relais ; 94 cartes | `registres/depenses.md` sur `main` (commit `af32512da`), ligne 536 | `43cad7c041ba7f5da3547fa52bcfcf004a3768ebfedb202f86386e20adfe2879` |
| S3 | estimation 55,94 (44,64 ; 3,41 ; 7,89) ; haut 137,81 (70,03 ; 20,46 ; 47,32) ; plafond d'arrêt 150 ; seuils 140, 135 et 120 ; 6,05 par appel de proposeur au pire ; épreuve des témoins 1,18 estimé, 5 de plafond ; crédit net 199,03 avant la course, 200 déclarés ; part au pire du troisième relais 66,55 | `docs/notes/organisme-auto-conception-v1/course-v4/devis-course-auto-conception-v2i.md`, § 1 à § 4 ; sa sortie de calcul `calcul-devis-course-auto-conception-v2i.json` (`1f43d53185ba4c93043e038c968c9a62245c2ae86f51c9754a3b42cd1a79743b`) | `a8c033cdc66b14f666a6a45bb6184e9e902369d6a330b672ac82a4fe13f64ba0` |
| S4 | 8,42 USD réels pour la séquence complète d'une course d'idéation d'une génération sur la question v1 du pilier attaque (sonde, course et bras, dont ≈ 3,80 de tentatives avortées) ; plafond 20 de la course sur la question v2 ; sonde de refus ≈ 0,005 pour trois modèles | `rapports/fille-ideation-1-v1/devis-course-ideation-pilier-attaque-v2-v1.md`, en-tête, § 1, § 3.2 et § 4 | `531849e3e4f55de3ae5f097033fdcb50bd209ac88670547b3060fb869b10eea3` |
| S5 | accord de la course v9 : plafond 150 USD exactement ; lignes à part de 5 et 6 USD | `registres/go.md` sur `main` (commit `af32512da`), lignes `GO-2026-11-19-19`, `-20`, `-21` | `7fce43740a5965a72bd5315da45e44346c6742ead5293c332eb4a4fbd554d9a1` |
| S6 | montant requis d'une course de N générations sans étage : N fois le plafond d'une génération, réservé en entier avant chaque génération ; la ligne d'accord porte ce montant exact | `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/rapport-developpeur-orchestrateur-v68-v1.md`, § 3 (points 3 et 6), § 4, § 5 | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6` |

Lus pour le contexte, sans qu'un chiffre de ce devis en vienne : les devis v1, v2 et v2b de la course d'auto-conception (`docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v1.md`, `50e7d2f1dc713098edf5d69b6f46ded96a42423f6c50c528b02cf3781f96a80b` ; `…-v2.md`, `fa39c545f71bb614cdc317c420c5b4c4d3fd47ed8435d0adace510d3a6233d85` ; `…-v2b.md`, `b2319472cbad20d87664b63edcdab47914de1d81135841b81f10954f6f45da0e`). Je n'ai lu en entier que la v1.

**Un écart d'un centime, dit ici.** Les cinq coûts de proposeur de S1 font 58,65 à l'addition ; S1 écrit 58,64 pour l'étape, et 72,50 pour la course. Le programme additionne les rôles : il rend 72,51 par génération, non 72,50 (champ `controles`). Les totaux « bas » de ce devis portent cet écart : un centime par génération.

## 2. L'unité : une génération

La seule génération mesurée de l'organisme à cette composition est la course v9. Elle a coûté 1,296 fois son estimation, 0,526 fois son cas haut et 0,483 fois son plafond (champ `controles`). Je prends donc trois cas, par génération :

| cas | ce qu'il suppose | cinq espèces | trois espèces | deux espèces |
|---|---|---|---|---|
| bas | le coût réel de la course v9, par rôle (S1) | 72,51 | 24,67 | 14,46 |
| haut | le cas haut du devis v2i (S3), rapporté rôle par rôle au réel de la v9 | 137,81 | 60,19 | 37,76 |
| pire | le plafond d'arrêt de la génération ; le lanceur coupe | **150** | **65** | **50** |

Pour trois et deux espèces, l'aiguilleur et les juges sont comptés au prorata des appels de proposeur (33 et 22 sur 55), et le cas haut applique les mêmes facteurs par rôle que pour cinq (1,194 pour la proposition, 4,458 pour l'aiguillage, 5,105 pour les juges ; champ `facteurs_du_haut_par_role`).

**Pourquoi l'unité de la v9 vaut ici, et sous quelle garde.** La course v9 servait une matière longue à chaque appel. Cette course sert une question courte, une pièce d'antériorité, une case et, aux générations 2 et 3, le registre borné que ton mot GO-2026-11-20-05 (2b) fait servir. Je n'ai pas mesuré ses consignes : elles n'existent pas encore. Je ne retire donc rien à l'unité. En échange, une garde : **la consigne d'un appel, registre compris, est mesurée sans appel avant la course, et le départ est refusé si elle dépasse la borne gelée à l'additif.** Le devis final se récrit sur cette mesure.

## 3. Plafonds par session, par génération, par relais

**Par session.** Un appel de proposeur : 6,05 USD au pire (S3, § 4). À ce prix, les 55 appels d'une génération feraient 332,75 USD : la proposition est coupée à son plafond dur bien avant (champ `proposition_coupee_au_pire_des_appels`).

**Par génération** (seuils du devis v2i, repris tels quels pour cinq espèces ; mêmes écarts au plafond pour trois et deux ; à geler à l'additif) :

| | cinq espèces | trois espèces | deux espèces |
|---|---|---|---|
| plafond d'arrêt de la génération | 150 | 65 | 50 |
| plafond dur de la proposition | 140 | 55 | 40 |
| aiguillage lancé si le cumul est au plus | 135 | 50 | 35 |
| juges lancés si le cumul est au plus | 120 | 35 | 20 |
| au cas haut, tout est lancé | oui | oui | oui |

Règle du plafond pour trois et deux espèces : le cas haut majoré de 5 %, arrondi aux 5 USD supérieurs, et au moins ce qu'il faut pour que les juges soient lancés au cas haut. Pour cinq espèces la règle donnerait 145 ; je garde 150, le plafond de la course v9, dont les seuils sont contre-lus (S5).

**Par relais, sur la course** (parts au pire comptées pour trois générations, comme le lanceur de la course devra le faire ; S6) :

| relais | ce qu'il tient | cinq espèces | trois espèces | deux espèces |
|---|---|---|---|---|
| premier | l'aiguilleur, le juge de l'espèce 3 et les proposeurs des espèces 3 et 4 (à trois espèces : de l'espèce 3 ; à deux : aucun) | 450 | 195 | 150 |
| deuxième | le juge de l'espèce 1 et les proposeurs des espèces 1 et 5 (à trois et à deux espèces : de l'espèce 1) | 450 | 195 | 150 |
| troisième | le proposeur de l'espèce 2 seul, présent dans les trois compositions | 199,65 | 199,65 | 199,65 |

Répartition lue à la course v9 : 36,457056 USD sur la première clé (S2) = 7,43 + 17,58 + 4,59 + 6,86 (S1) ; 31,299704 sur la deuxième = 4,17 + 24,72 + 2,41 ; 4,74571 sur la troisième = 4,75 ; parts au pire de S3, § 3. Le troisième relais vaut 11 × 6,05 × 3 au compte de S3 ; à trois et à deux espèces, le plafond dur de la proposition (55 ou 40 USD par génération) le coupe avant.

## 4. Total, et ligne de course

| | cinq espèces | trois espèces | deux espèces |
|---|---|---|---|
| course, bas | 217,53 | 74,00 | 43,39 |
| course, haut | 413,43 | 180,57 | 113,29 |
| **ligne de course (pire), montant exact** | **450** | **195** | **150** |
| épreuve des témoins : estimée 1,18 ; plafond, ligne à part | 5 | 5 | 5 |
| sonde de refus : estimée moins d'un centime ; plafond, ligne à part | 1 | 1 | 1 |
| total, bas | 218,72 | 75,18 | 44,58 |
| total, haut | 419,43 | 186,57 | 119,29 |
| **plafond total** | **456** | **201** | **156** |
| fiches attendues sur la course, à la proportion de la v9 | 282 | 168 | 114 |

La ligne de course porte le montant exact que l'orchestrateur exigera : trois fois le plafond d'une génération (S6). Le plafond de la sonde de refus, 1 USD, est une valeur du rédacteur : l'estimation est de l'ordre du centime (S4).

**Ce que la réservation au pire implique.** L'orchestrateur réserve le plafond entier de chaque génération avant de la jouer et s'arrête plutôt que de dépasser. Une course peut donc s'arrêter alors que sa dépense réelle aurait tenu ; c'est voulu (S6, § 8 du rapport).

## 5. Ce que chaque composition fait perdre

| composition | ce qu'elle fait perdre |
|---|---|
| cinq espèces | le plus d'argent si le montage casse : c'est la première course réelle à plusieurs générations, sur un code qui n'est pas encore écrit. Et la plus lourde relecture : de l'ordre de 282 fiches à relire « aucune recette » par la mère |
| trois espèces (1, 2 et 3) | les deux espèces qui font 72 % du coût de proposition à la v9 (devis de l'héritage v5, § 6). Rien n'établit qu'elles proposent les mêmes idées que les trois autres : la diversité des proposeurs (N-044) est ce qu'une course d'idées inédites achète. Retirer des espèces est un changement de composition ; N-058 veut qu'il se juge sur l'oracle du monde planté et le coût, et cet oracle n'existe pas par espèce |
| deux espèces (1 et 2) | la même chose, en plus fort |

## 6. Crédit de la clé du premier relais

Le devis v2i comptait 199,03 USD nets sur cette clé avant la course v9 (S3, § 3), l'épreuve des témoins y étant estimée à 0,97. Elle y a coûté 0,980399 USD (S2, ligne 532), après la vérification de la clé, 0,000108 (S2, ligne 528) ; la course v9 y a dépensé 36,457056 USD (S2, ligne 536). Il resterait **162,56 USD** (200 − 0,000108 − 0,980399 − 36,457056 = 162,562437). Aucune ligne postérieure sur cette clé au registre des dépenses de `main` relu le 2026-11-20 (commit `6f7cd0f8`, `a6d50ecad8a5c11e349b288989d3bda7237237c6e5037220ba11b2becb2d72f7`) ; le relevé du jour du devis final prime. La règle du lanceur refuse le départ si le reste ne couvre pas la part au pire.

| | part au pire | couverte ? | manque |
|---|---|---|---|
| cinq espèces | 450 | non | 287,44 |
| trois espèces | 195 | non | 32,44 |
| deux espèces | 150 | oui | 0 |

Les crédits des deux autres relais étaient illisibles et sous dispense au devis v2i ; je ne les ai pas relevés. Cette dispense (R-3237 : départ permis, arrêt au premier refus pour crédit) a été posée par la mère pour une course : qu'elle vaille pour celle-ci est à redire au devis final.

## 7. Ce qui n'est pas chiffré

1. **Le travail de conception** : version de l'orchestrateur qui porte la course et son lanceur (ordre de course, § 2, points 1 et 2), additif, configuration, témoins, préenregistrement, contre-lectures. Zéro dollar d'appels d'interface ; du temps de sessions (ordre de course, § 2).
2. **La lecture d'antériorité** : deux lecteurs neufs, sur PDF empreinté, pour les fiches lues au sens de l'ordre de course, § 9. Faite par des sous-agents de session, elle ne coûte pas d'appels d'interface. Un tour de collisionneur, si tu en veux un, part sur un devis à part.
3. **Le registre servi** (ton mot 2b ; ordre de course, § 5) : des consignes plus longues aux générations 2 et 3. Non mesuré ; borné par la garde du § 2.
4. **Les appels sans sortie exploitable** : le cas haut les couvre sans garantie.
5. **Aucune machine** : la course n'exécute aucun script écrit par un modèle.

## 8. Leviers, avec ce que chacun ferait perdre

| levier | effet à cinq espèces | ce qui serait perdu |
|---|---|---|
| composition à trois ou à deux espèces | ligne 195 ou 150 au lieu de 450 | § 5 |
| ne pas jouer les juges | 9,27 par génération au cas bas, 27,81 sur la course | la lecture des témoins plantés par les juges, et l'ordre de lecture de la mère ; aucun critère n'en dépend |
| un bras témoin « trois tirages indépendants, sans rien servir » | **ajoute** 217,53 au cas bas et 450 à la ligne | sans lui, la course décrit l'héritage et ne le compare pas ; je ne le propose pas ici (ordre de course, § 6) |
| moins de onze cases par génération | proportionnel | moins de fiches, moins de cases couvertes |

## 9. Décision

**Décision.** Quelle ligne de course accordes-tu, et à quelle composition ?

**Enjeu.** La dépense d'une course d'idées sur trois générations, la première de ce genre en réel ; la diversité des proposeurs ; la charge de relecture de la mère ; et le crédit de la clé du premier relais.

**Options.**
- **(a) Cinq espèces : ligne de 450 USD exactement, plafond total 456 USD** ; attendu 218,72. Avantage : la composition de l'organisme tel qu'il existe, la seule mesurée ; la diversité entière. Inconvénient : la dépense la plus haute si le montage casse ; 282 fiches à relire ; le crédit du premier relais à recharger d'au moins 287,44 USD.
- **(b) Trois espèces : ligne de 195 USD, plafond total 201 USD** ; attendu 75,18. Avantage : un montage éprouvé pour le tiers du prix ; 168 fiches. Inconvénient : les deux espèces retirées, sans preuve qu'elles n'apportent rien ; le crédit manque encore de 32,44 USD.
- **(c) Deux espèces : ligne de 150 USD, plafond total 156 USD** ; attendu 44,58. Avantage : le crédit lu suffit ; 114 fiches. Inconvénient : la diversité la plus pauvre, pour une course qui cherche de l'inédit.

**Recommandation.** (a), confiance 0,55. La course cherche des idées que personne n'a écrites ; je n'ai aucune mesure qui permette de dire quelles espèces on peut retirer sans perdre de ces idées, et la composition (a) est la seule dont le coût soit mesuré. Ce qui me ferait passer à (b) : que le crédit ne soit pas rechargé ; ou que tu veuilles éprouver d'abord le montage neuf à bas prix, le bon marché d'abord (N-045 v2, point 4).

**Défaut.** Aucun : c'est une dépense. Sans ton accord, rien ne part.
