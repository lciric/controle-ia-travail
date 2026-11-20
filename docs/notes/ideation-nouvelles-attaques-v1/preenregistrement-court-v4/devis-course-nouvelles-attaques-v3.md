# Devis — course de l'organisme d'idéation « nouvelles attaques », trois générations — v3

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` : 01:01:43Z, après la lecture des pièces et avant l'écriture. Version 3 : un autre rédacteur neuf, modèle F, qui n'a écrit aucune version antérieure ; relevé de `date -u` : 10:04:49Z, après la lecture des pièces et le calcul, avant l'écriture.
- Version : la v2 remplace la v1 (`638492f1cc65151c0528ed62f5d13849d4629336a65b80d1db1ba054e61c6268`) après la contre-lecture `contre-lecture-conception-nouvelles-attaques-v1.md` (`ae9d4ae44027476bee4821e72c4e9f9b12f39d10f3dc6749ae60ae61d07c1fed`, verdict « Conforme après corrections ») : corrections C9, C12, C17, C18 et C19 appliquées à texte exact ; la v1 reste archivée, non modifiée. La v2 elle-même n'est pas contre-lue.
- Version : la v3 remplace la v2 (`714e4fc6a9a292626022adac4a5ddcc4f3e16fd14f81629b6b8a98cf89fcf028`) sur GO-2026-11-20-33 (R-4169) : une sixième espèce entre dans la course, comme proposeur. Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/mandat-redacteur-preenregistrement-court-v4-devis-v3-v1.md` (`4fa56789a159ba96a5496e1d5f7230c3c6179119031af85726472a5a5121da5f`). La v3 ajoute la composition à six espèces et ce qui en dépend, et la lettre de GO-2026-11-20-34 sur la clé Rigaud. Tout ce qu'elle ajoute est marqué « v3 » ou « à six espèces » ; aucun chiffre à cinq, à trois ou à deux espèces ne change. La v2 reste archivée, non modifiée. La v3 n'est pas contre-lue.
- Statut : **pièce de travail, non contre-lue. Rien n'a été lancé ; aucun appel, aucune dépense.** Ce devis n'engage rien : la course ne part qu'après sa contre-lecture et ton accord de calcul, distinct (`GO-2026-11-19-94`). À six espèces, **rien ne court avant ton mot sur ce devis** (GO-2026-11-20-33).
- Calcul : `calcul_devis_course_nouvelles_attaques_v2.py` (`cefe97837267d4db517c40437dc89288842d1d7dd5252b225fe0e0f05edede9b`), sortie `calcul-devis-course-nouvelles-attaques-v2.json` (`ffecbd1172888b815e6f7af84ae54f52c1991554d6d2ff376481af694e60b7cf`), même dossier. Joué deux fois ; les deux sorties sont égales à l'octet. Processeur seul ; le programme ne lit aucun fichier. Pour la v3 : `calcul_devis_course_nouvelles_attaques_v3.py` (`a50c9983df2acc681cbef519dc78338428b16a7942beb99d2410e4006fc00630`), sortie `calcul-devis-course-nouvelles-attaques-v3.json` (`fa4bc8b0448f89fa938e44f170d17f932d8514eba71aa80241cd258a9900108c`), versés avec ce devis ; joué deux fois, sorties égales à l'octet (`cmp`). Il part du programme v2, rejoue ses compositions à cinq, à trois et à deux espèces sans changement (champ `controle_v2`, égal aux chiffres de la v2) et ajoute la composition à six espèces (champ `six_especes`).
- Les espèces sont désignées par un numéro, de 1 à 5, dans l'ordre du coût réel croissant de leur rôle de proposeur à la course v9, comme au devis de l'héritage v5 (§ 1, table de correspondance). L'espèce 6 est celle que GO-2026-11-20-33 fait entrer ; son numéro est celui de son ordre d'entrée, non d'un coût : elle n'a pas joué la course v9. Aucun nom de modèle n'est écrit ici.
- Montants en dollars des États-Unis (USD).

## 0. Verdict

**À six espèces (v3, GO-2026-11-20-33) : ce que ce devis te demande.**

- **Ligne de course neuve : 570 USD exactement**, soit trois générations à 190 USD de plafond d'arrêt chacune. **Plafond total : 576,01 USD**, avec trois lignes à part avant la course : l'épreuve des témoins (5 USD), la sonde de refus des espèces 1 à 5 (1 USD) et la sonde de refus de l'espèce 6, sur sa clé (0,01 USD). C'est 120 USD de plus que la ligne à cinq espèces, et 120,01 USD de plus au total.
- Attendu : **262,23 USD**, soit 43,51 de plus qu'à cinq espèces. Cas haut : 548,66 USD. Au pire : 576,01 USD ; le lanceur coupe au plafond.
- **Le coût de l'espèce 6 n'est mesuré nulle part dans l'organisme.** Ses trois cas sont des règles du rédacteur (§ 2) : 35,19 USD attendus sur la course, 88,55 au cas haut, 199,65 au pire. Elle est sur sa propre clé, `KIMI_API_KEY`, nommée par sa variable seulement, par un quatrième relais.
- **Les trois clés Claude gardent leurs rôles** (GO-2026-11-20-22), et X reste de 8,35 USD. Leur charge monte : l'aiguilleur et le juge lisent les fiches de six espèces. Le cas haut des rôles Claude passe de 256,02 à 289,31 USD ; il tient sous la borne de 415,21 USD d'avant la recharge de Rigaud. GO-2026-11-20-34 recharge Rigaud : sa part se lit sur le solde relu après recharge (§ 6).
- Une variante garde la ligne de 450 USD ; son prix est dit au § 5 et au § 9.

**Rappel de la v2, à cinq espèces et moins, inchangé.**

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
| S7 (v3) | soldes des trois clés Claude avant la recharge de Rigaud : Minuit 162,56 calculé, Luc 214 déclaré, Rigaud environ 47 calculé ; X = 8,35 ; borne des trois clés 415,21 ; répartition retenue ; coûts par rôle du premier relais à cinq espèces (109,38 et 256,02) | `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v3/preenregistrement-court-course-nouvelles-attaques-v3.md`, section « Seuil » (scellé, R-4125) | `2ea5ad53de565f912992128a9113da59e5462b561ed258b151d519b193f85787` |
| S8 (v3) | lignes GO-2026-11-20-10, -13, -16, -20, -22, -31, -32, -33 et -34 | `registres/go.md` sur `main` (commit `da0d389cad376ad492d0255b42d7e633fea09f5a`) | `21f8f1847565c41f9e448746b826ef821575fcf65c267b319ed7ee5acba19356` |
| S9 (v3) | R-4117, R-4125, R-4169, R-4170 et R-4174 ; et, pour le seul repère de tarif de l'espèce 6 (2 et 10 USD par million de jetons, entrée et sortie), R-813 et R-1780 | `registres/decisions.md` sur `main` (même commit) | `47ed2a0b17f38472948bd6dfe0c9cebe74212dec9d87bf2a4d2262e9b236099a` |
| S10 (v3) | plafond de la sonde de refus de l'espèce 6 : 0,01 USD ; modèle : la sonde minimale de la clé Luc | mandat du rédacteur de la v3 (en-tête) | `4fa56789a159ba96a5496e1d5f7230c3c6179119031af85726472a5a5121da5f` |

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

**La sixième espèce (v3).** L'espèce 6 n'a pas joué la course v9. Je n'ai trouvé, dans les pièces lues, aucun coût mesuré de son rôle de proposeur dans l'organisme. Ses trois cas sont donc des règles, écrites avant tout appel (champ `espece_6_regles_du_redacteur`) :

| cas | règle du rédacteur | par génération | sur la course |
|---|---|---|---|
| bas | la moyenne des cinq coûts réels de proposeur de la course v9 (S1) | 11,73 | 35,19 |
| haut | le coût réel le plus haut des cinq (24,72), fois le facteur du haut de la proposition (1,1940) | 29,52 | 88,55 |
| pire | onze appels à 6,05 USD (S3), comme le troisième relais | 66,55 | 199,65 |

Pourquoi ces règles. Sans mesure, le cas bas ne peut pas être plus fin qu'un proposeur moyen. Le cas haut prend le proposeur le plus cher, pour que le plafond ne repose pas sur une espèce supposée bon marché. Un repère, qui n'entre dans aucun total : le registre des décisions note pour cette espèce un tarif de 2 et 10 USD par million de jetons, entrée et sortie (S9) ; je ne l'ai pas relu ce jour sur la page du fournisseur. À ce tarif, 6,05 USD valent 605 000 jetons de sortie, et le cas bas est sans doute large. Que 6,05 USD bornent bien un appel de l'espèce 6 reste à confirmer par le tarif relevé et la sortie maximale de la configuration. Le devis final se récrit sur la mesure des consignes et sur ce relevé.

L'aiguilleur et les deux juges lisent les fiches de six espèces : ils sont comptés au prorata des appels de proposeur (66 sur 55, soit 1,2), par la règle que ce devis applique déjà à trois et à deux espèces.

| cas, par génération | cinq espèces | six espèces (proposition ; aiguillage ; juges) |
|---|---|---|
| bas | 72,51 | 87,01 (70,38 ; 5,51 ; 11,12) |
| haut | 137,81 | 180,88 (99,55 ; 24,55 ; 56,78) |
| pire | 150 | **190** |

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

**À six espèces (v3).** La même règle donne **190 USD** : le cas haut majoré de 5 % fait 189,93, arrondi à 190 ; la condition des juges ne demanderait que 155. Je ne garde pas 150. À 150, le cas haut ne lance pas les juges (cumul de 124,10 USD avant eux, pour un seuil de 120) et dépasse le plafond (180,88 ; champ `variante_plafond_de_150_garde`). Seuils, aux mêmes écarts qu'à cinq espèces : plafond dur de la proposition 180 ; aiguillage lancé si le cumul est au plus 175 ; juges lancés si le cumul est au plus 160 ; au cas haut, tout est lancé. Les 66 appels de proposeur au pire feraient 399,30 USD : la proposition est coupée à son plafond dur bien avant.

**Par relais, sur la course** (parts au pire comptées pour trois générations, comme le lanceur de la course devra le faire ; S6) :

| relais | ce qu'il tient | cinq espèces | trois espèces | deux espèces |
|---|---|---|---|---|
| premier | l'aiguilleur, le juge de l'espèce 3 et les proposeurs des espèces 3 et 4 (à trois espèces : de l'espèce 3 ; à deux : aucun) | 450 | 195 | 150 |
| deuxième | le juge de l'espèce 1 et les proposeurs des espèces 1 et 5 (à trois et à deux espèces : de l'espèce 1) | 450 | 195 | 150 |
| troisième | le proposeur de l'espèce 2 seul, présent dans les trois compositions | 199,65 | 199,65 | 199,65 |

Répartition lue à la course v9 : 36,457056 USD sur la première clé (S2) = 7,43 + 17,58 + 4,59 + 6,86 (S1) ; 31,299704 sur la deuxième = 4,17 + 24,72 + 2,41 ; 4,74571 sur la troisième = 4,75 ; parts au pire de S3, § 3. Le troisième relais vaut 11 × 6,05 × 3 au compte de S3 ; à trois et à deux espèces, le plafond dur de la proposition (55 ou 40 USD par génération) le coupe avant.

**À six espèces (v3) : quatre relais** (champs `plafonds_par_relais_usd` et `par_cle_sur_la_course_usd`), sur la course :

| relais | ce qu'il tient | clé | bas | haut | part au pire |
|---|---|---|---|---|---|
| premier | l'aiguilleur, le juge de l'espèce 3 et les proposeurs des espèces 3 et 4 | Minuit, Luc et Rigaud (§ 6) | 116,25 | 289,31 | 570, bornée par les parts des trois clés |
| deuxième | le juge de l'espèce 1 et les proposeurs des espèces 1 et 5 | inchangée | 95,35 | 147,77 | 570 |
| troisième | le proposeur de l'espèce 2 | inchangée | 14,25 | 17,01 | 199,65 |
| quatrième, neuf | le proposeur de l'espèce 6 | `KIMI_API_KEY`, nommée par sa variable seulement | 35,19 | 88,55 | 199,65 |
| course | | | 261,04 | 542,65 (542,64 à l'addition des lignes arrondies) | 570 : les pires ne s'additionnent pas |

**Par espèce, sur la course** (champ `par_espece_sur_la_course_usd` ; une espèce additionne ses rôles) :

| espèce | rôles | bas | haut | pire de son rôle de proposeur |
|---|---|---|---|---|
| 1 | proposeur, juge | 21,19 | 59,23 | 199,65 |
| 2 | proposeur | 14,25 | 17,01 | 199,65 |
| 3 | proposeur, juge | 46,99 | 152,68 | 199,65 |
| 4 | proposeur | 52,74 | 62,97 | 199,65 |
| 5 | proposeur | 74,16 | 88,55 | 199,65 |
| 6 | proposeur | 35,19 | 88,55 | 199,65 |
| aiguilleur (le portier) | aiguilleur | 16,52 | 73,66 | — |

Pour l'aiguilleur et pour un juge, le seul pire écrit est la ligne de course, 570 USD.

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

**À six espèces (v3)** (champs `course_usd`, `lignes_a_part_usd`, `total_usd` et `ecarts_a_la_composition_A_usd`) :

| | cinq espèces (v2) | six espèces | écart |
|---|---|---|---|
| course, bas | 217,53 | 261,04 | + 43,51 |
| course, haut | 413,43 | 542,65 | + 129,22 |
| **ligne de course (pire), montant exact** | 450 | **570** | + 120 |
| épreuve des témoins, plafond, ligne à part | 5 | 5 | 0 |
| sonde de refus des espèces 1 à 5, plafond, ligne à part | 1 | 1 | 0 |
| sonde de refus de l'espèce 6, plafond, ligne à part neuve | — | 0,01 | + 0,01 |
| total, bas | 218,72 | 262,23 | + 43,51 |
| total, haut | 419,43 | 548,66 | + 129,23 |
| **plafond total** | 456 | **576,01** | + 120,01 |
| fiches attendues sur la course, à la proportion de la v9 | 282 | de l'ordre de 338 | + 56 |

Les 338 fiches supposent que l'espèce 6 rend des fiches au taux moyen des cinq autres ; c'est une attente de volume, non une cible.

**La sonde de refus de l'espèce 6 (v3).** Une ligne à part de 0,01 USD, sur sa clé, par son relais à coût borné, sur le modèle de la sonde minimale de la clé Luc (S8, GO-2026-11-20-13 : relais épinglé, une seule requête, aucune valeur de clé lue ni affichée, relais arrêté par son identifiant après l'appel). Elle mesure si la clé répond et si l'espèce 6 accepte ou refuse la question scellée. Ce qu'elle envoie, son plafond et son arrêt sont au préenregistrement court v4, section « Seuil ». Estimée à moins d'un centime : 0,0017 USD, le tiers de la sonde de trois modèles (S4).

## 5. Ce que chaque composition fait perdre

| composition | ce qu'elle fait perdre |
|---|---|
| cinq espèces | le plus d'argent si le montage casse : c'est la première course réelle à plusieurs générations, sur un code qui n'est pas encore écrit. Et la plus lourde relecture : de l'ordre de 282 fiches à relire « aucune recette » par la mère |
| trois espèces (1, 2 et 3) | les deux espèces qui font 72 % du coût de proposition à la v9 (devis de l'héritage v5, § 6). Rien n'établit qu'elles proposent les mêmes idées que les trois autres : la diversité des proposeurs (N-044) est ce qu'une course d'idées inédites achète. Retirer des espèces est un changement de composition ; N-058 veut qu'il se juge sur l'oracle du monde planté et le coût, et cet oracle n'existe pas par espèce |
| deux espèces (1 et 2) | la même chose, en plus fort |
| six espèces (v3) | 43,51 USD de plus attendus et 120 USD de plus au plafond ; une relecture plus lourde pour la mère, de l'ordre de 338 fiches ; un quatrième relais et une clé de plus à tenir. Ce que l'espèce 6 apporte se juge sur l'oracle du monde planté et le coût (N-058), et cet oracle n'existe pas par espèce : rien ici n'établit qu'elle propose d'autres idées que les cinq. La ligne GO-2026-11-20-32 note que tu la juges peu diverse ; GO-2026-11-20-33 la fait entrer |
| six espèces, ligne gardée à 450 USD (variante, v3) | au cas haut, les juges ne sont pas lancés et la génération est coupée par son plafond ; la marge du plafond sur le cas bas tombe de 2,18 à 1,72. Aucun critère ne dépend des juges, joués pour information |

## 6. Crédit de la clé du premier relais

Le devis v2i comptait 199,03 USD nets sur cette clé avant la course v9 (S3, § 3), l'épreuve des témoins y étant estimée à 0,97. Elle y a coûté 0,980399 USD (S2, ligne 532), après la vérification de la clé, 0,000108 (S2, ligne 528) ; la course v9 y a dépensé 36,457056 USD (S2, ligne 536). Il resterait **162,56 USD** (200 − 0,000108 − 0,980399 − 36,457056 = 162,562437). Aucune ligne postérieure sur cette clé au registre des dépenses de `main` relu le 2026-11-20 (commit `6f7cd0f8`, `a6d50ecad8a5c11e349b288989d3bda7237237c6e5037220ba11b2becb2d72f7`) ; le relevé du jour du devis final prime. La règle du lanceur refuse le départ si le reste ne couvre pas la part au pire.

| | part au pire | couverte ? | manque |
|---|---|---|---|
| cinq espèces | 450 | non | 287,44 |
| trois espèces | 195 | non | 32,44 |
| deux espèces | 150 | oui | 0 |

Les crédits des deux autres relais étaient illisibles et sous dispense au devis v2i ; je ne les ai pas relevés. Cette dispense (R-3237 : départ permis, arrêt au premier refus pour crédit) a été posée par la mère pour une course : qu'elle vaille pour celle-ci est à redire au devis final.

**Les trois clés Claude, à six espèces (v3).** Depuis la v2, tes mots ont réparti la part Claude sur trois clés, chacune plafonnée à son solde (GO-2026-11-20-16), avec X = 8,35 USD réservés au bras A sur Rigaud et une borne des trois clés de 415,21 USD (GO-2026-11-20-22 ; S7). L'espèce 6 n'y prend aucune part. Ce qui change est la charge de l'aiguilleur et du juge (champs `cles_claude` et `par_cle_sur_la_course_usd`) :

| clé | rôles (GO-2026-11-20-22) | bas | haut | part | part / haut (à cinq espèces) |
|---|---|---|---|---|---|
| Minuit | juge de l'espèce 3 | 24,70 | 126,06 | 162,56 | 1,290 (1,547) |
| Luc | aiguilleur ; proposeur de l'espèce 4 | 69,26 | 136,63 | 214 | 1,566 (1,721) |
| Rigaud | proposeur de l'espèce 3 | 22,29 | 26,61 | le solde relu après recharge, moins 8,35 ; 38,65 avant la recharge | 1,452 avant la recharge (1,452) |
| les trois | | 116,25 | 289,31 | 415,21 avant la recharge | 1,435 (1,622) |

- **X = 8,35 USD : rien ne change.** C'est la réserve du bras A sur Rigaud ; l'espèce 6 ne touche pas à Rigaud.
- **La borne de 415,21 USD : l'espèce 6 ne change pas ce chiffre, mais il couvre moins.** Le cas haut des rôles Claude passe de 256,02 à 289,31 USD : la borne vaut 1,435 fois ce cas haut, au lieu de 1,622. Au pire, la ligne de 570 USD dépasse la borne de 154,79 USD, contre 34,79 à cinq espèces. C'est l'arrêt nommé « part d'une clé épuisée » qui tient cet écart, sans bascule.
- **La répartition retenue atteint encore le meilleur rapport de la règle du préenregistrement** : le plus grand des plus petits rapports vaut 1,290, à égalité avec la répartition qui met aussi le proposeur de l'espèce 3 sur Luc. La clé la plus serrée devient Minuit.
- **GO-2026-11-20-34**, à la lettre : « **Clé Rigaud : recharge plutôt que report** (option (b) de R-4170). La part de la course « nouvelles attaques » reste sur Rigaud ; la recharge est faite par Lazar ; le devis v3 de la course (GO-2026-11-20-33) se lit sur le solde relu après recharge. » La ligne « Rigaud » se lit donc sur ce solde : sa part est le solde relu, moins 8,35 ; la borne des trois clés est 376,56 USD plus cette part. Je n'ai lu aucun solde ni aucun montant de recharge, et je n'en suppose pas. Il faut au moins 26,61 USD de part sur Rigaud, le cas haut de son rôle, soit un solde relu d'au moins 34,96 USD ; pour couvrir le pire de son rôle (199,65), il en faudrait 208,00. La raison de la recharge est au registre (R-4170 : deux lots en cours sur cette clé, au plus 45 USD, en concurrence avec la part de la course).

**La clé de l'espèce 6 (v3).** `KIMI_API_KEY`, nommée par sa variable seulement ; aucune valeur n'est lue. Part au pire : 199,65 USD sur la course. Je n'ai pas lu son solde, et j'ignore s'il est lisible : s'il ne l'est pas, la dispense de R-3237 est à redire pour elle au devis final, comme pour les relais 2 et 3.

## 7. Ce qui n'est pas chiffré

1. **Le travail de conception** : version de l'orchestrateur qui porte la course et son lanceur (ordre de course, § 2, points 1 et 2), additif, configuration, témoins, préenregistrement, contre-lectures. Zéro dollar d'appels d'interface ; du temps de sessions (ordre de course, § 2).
2. **La lecture d'antériorité** : deux lecteurs neufs, sur PDF empreinté, pour les fiches lues au sens de l'ordre de course, § 9. Faite par des sous-agents de session, elle ne coûte pas d'appels d'interface. Un tour de collisionneur, si tu en veux un, part sur un devis à part.
3. **Le registre servi** (ton mot 2b ; ordre de course, § 5) : des consignes plus longues aux générations 2 et 3. Non mesuré ; borné par la garde du § 2.
4. **Les appels sans sortie exploitable** : le cas haut les couvre sans garantie.
5. **Aucune machine** : la course n'exécute aucun script écrit par un modèle.
6. **Le coût réel de l'espèce 6** (v3) : aucune mesure dans l'organisme ; il est borné par les règles du § 2 et par la part au pire de sa clé. La durée de ses appels n'est pas chiffrée.

## 8. Leviers, avec ce que chacun ferait perdre

| levier | effet à cinq espèces | ce qui serait perdu |
|---|---|---|
| composition à trois ou à deux espèces | ligne 195 ou 150 au lieu de 450 | § 5 |
| ne pas jouer les juges | 9,27 par génération au cas bas, 27,81 sur la course | la lecture des témoins plantés par les juges, et l'ordre de lecture de la mère ; aucun critère n'en dépend |
| un bras témoin « trois tirages indépendants, sans rien servir » | **ajoute** 217,53 au cas bas et 450 à la ligne | sans lui, la course décrit l'héritage et ne le compare pas ; je ne le propose pas ici (ordre de course, § 6) |
| moins de onze cases par génération | proportionnel | moins de fiches, moins de cases couvertes |
| (v3, à six espèces) garder la ligne de 450 USD | 120 USD de moins au plafond ; rien de moins à l'attendu | au cas haut, les juges ne sont pas lancés (§ 5) |

## 9. Décision

**Décision.** Quelle ligne de course accordes-tu, et à quelle composition ?

**Enjeu.** La dépense d'une course d'idées sur trois générations, la première de ce genre en réel ; la diversité des proposeurs ; la charge de relecture de la mère ; et le crédit de la clé du premier relais.

**Options.**
- **(a) Cinq espèces : ligne de 450 USD exactement, plafond total 456 USD** ; attendu 218,72. Avantage : la composition de l'organisme tel qu'il existe, la seule mesurée ; la diversité entière. Inconvénient : la dépense la plus haute si le montage casse ; 282 fiches à relire ; le crédit du premier relais à recharger d'au moins 287,44 USD.
- **(b) Trois espèces : ligne de 195 USD, plafond total 201 USD** ; attendu 75,18. Avantage : un montage éprouvé pour le tiers du prix ; 168 fiches. Inconvénient : les deux espèces retirées, sans preuve qu'elles n'apportent rien ; le crédit manque encore de 32,44 USD.
- **(c) Deux espèces : ligne de 150 USD, plafond total 156 USD** ; attendu 44,58. Avantage : le crédit lu suffit ; 114 fiches. Inconvénient : la diversité la plus pauvre, pour une course qui cherche de l'inédit.

**Recommandation.** (a), confiance 0,55. La course cherche des idées que personne n'a écrites ; je n'ai aucune mesure qui permette de dire quelles espèces on peut retirer sans perdre de ces idées, et la composition (a) est la seule dont le coût soit mesuré. Ce qui me ferait passer à (b) : que le crédit ne soit pas rechargé ; ou que tu veuilles éprouver d'abord le montage neuf à bas prix, le bon marché d'abord (N-045 v2, point 4).

**Défaut.** Aucun : c'est une dépense. Sans ton accord, rien ne part.

### Décision de la v3, à six espèces

La décision ci-dessus est prise : cinq espèces, ligne de 450 USD (GO-2026-11-20-10, D1 (a)). GO-2026-11-20-33 fait entrer l'espèce 6. Il reste ceci.

**Décision.** Accordes-tu la ligne neuve de la course à six espèces ?

**Enjeu.** Le plafond de la course, pour une espèce dont le coût n'est pas mesuré ; le jeu des juges au cas haut ; la charge de relecture de la mère.

**Options.**
- **(a) Ligne de 570 USD exactement, plafond total 576,01 USD** ; attendu 262,23. Avantage : la règle du plafond de ce devis est tenue ; au cas haut, tout est lancé, juges compris. Inconvénient : 120 USD de plus au plafond.
- **(b) Ligne gardée à 450 USD, plafond total 456,01 USD** ; même attendu. Avantage : le montant déjà accordé à cinq espèces ; seule la sonde de 0,01 USD s'ajoute. Inconvénient : au cas haut, les juges ne sont pas lancés et la génération est coupée par son plafond ; le préenregistrement court v4, écrit sur (a), se récrit.

**Recommandation.** (a), confiance 0,65. À 150 USD par génération, le cas haut ne tient pas, quel que soit le coût de l'espèce 6 : sans elle, la proposition des cinq autres, l'aiguillage et les juges au prorata font déjà de l'ordre de 151 USD (70,03 + 24,55 + 56,78, addition à la main de champs de la sortie). Pour la course v9, tu avais relevé le plafond de 120 à 150 USD pour que les juges passent au cas haut (S3, fondement du devis v2i). Ce qui me ferait passer à (b) : que tu préfères ne pas jouer les juges au cas haut ; aucun critère n'en dépend.

**Avec la ligne, tu accordes aussi** : la sonde de refus de l'espèce 6, 0,01 USD sur sa clé ; la part au pire de sa clé, 199,65 USD sur la course, comprise dans la ligne.

**Défaut.** Aucun : c'est une dépense. Sans ton mot sur ce devis, rien ne court (GO-2026-11-20-33).
