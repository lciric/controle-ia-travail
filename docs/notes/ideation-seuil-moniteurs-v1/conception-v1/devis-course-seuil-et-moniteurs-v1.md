# Devis — course de l'organisme d'idéation « seuil et moniteurs », une génération et un étage de tests de mort — v1

- Auteur : rédacteur de la conception de la course seuil et moniteurs, modèle F. Écrit le 2026-11-21 ; relevé de `date -u` : 06:43:41Z.
- Statut : **pièce de travail (classe C), non contre-lue.** Aucun appel, aucune dépense. **Ce devis n'accorde rien : il demande.**
- Calcul : `calcul_devis_course_seuil_et_moniteurs_v1.py`, sortie `calcul-devis-course-seuil-et-moniteurs-v1.json`, même dossier ; empreintes à la table du dossier. Joué deux fois sous Python 3.13.18 (`python3 -B`), les deux sorties égales à l'octet (`cmp` muet). Arithmétique seule ; le programme ne lit aucun fichier.
- Les espèces sont désignées par un numéro, de 1 à 5, comme au devis v6 de la course « nouvelles attaques ». Aucun nom de modèle n'est écrit ici. Les clés sont dites par leur désignation au registre.
- Tous les montants sont en USD.

## 0. Verdict

| | cas bas | cas haut | pire |
|---|---|---|---|
| la génération (cinq espèces, onze cases) | 72,51 | 137,81 | 150,00 |
| l'étage des tests de mort (vingt candidates, expérimentateur modèle) | 21,33 | 107,33 | 110,00 |
| la machine jetable du bac et son essai | 2,00 | 5,00 | 10,00 |
| l'épreuve des témoins | 1,18 | 5,00 | 5,00 |
| la sonde de refus | 0,005 | 1,00 | 1,00 |
| **total** | **97,02** | **256,14** | **276,00** |

- **Ligne de course demandée, montant exact : 260 USD** (une génération à 150 de plafond d'arrêt, un étage à 110, réservés en entier avant chaque poste).
- **Lignes à part** : machine jetable et essai du bac, 10 USD ; épreuve des témoins, 5 USD ; sonde de refus, 1 USD.
- **Plafond total : 276 USD.**
- **Deux chiffres de ce devis ne sont mesurés nulle part** : le coût de l'étage, qui n'a jamais été joué en réel, et le prix de la machine. Ce sont des règles du rédacteur (§ 2, § 3). Les plafonds tiennent la dépense ; les cas bas et haut de ces deux lignes ne sont pas des estimations au sens des autres.
- **Aucune clé Claude n'a de marge connue pour cette course** tant que la course « nouvelles attaques » tient ses parts (§ 6).

## 1. Sources de chaque chiffre

| clé | chiffre | source | empreinte |
|---|---|---|---|
| S1 | coûts réels de la course v9, une génération : proposeurs 4,17 ; 4,75 ; 7,43 ; 17,58 ; 24,72, onze appels chacun ; aiguilleur 4,59 ; juges 6,86 et 2,41 ; course 72,50 | devis v6 de la course « nouvelles attaques », `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/devis-course-nouvelles-attaques-v6.md` sur `origin/main`, § 1, ligne S1 (elle cite le devis de l'héritage v5, `30c87fa68d9d6fa5e961edc45764fe58172b1a1b20d45fd3065a678b42f2880d`, branche `lot/compte-organisme-v1`) | `d825cb313898ea5111ede1ef3103ab25b1b923e1f52103481427919ce9d19c2c` |
| S2 | facteurs du cas haut par rôle : proposition 1,1940 ; aiguillage 4,4575 ; juges 5,1046 | préenregistrement court v9, `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md`, section « Seuil » | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| S3 | plafond d'arrêt d'une génération à cinq espèces 150 ; 6,05 au pire par appel de proposeur ; épreuve des témoins 1,18 estimé, 5 de plafond | devis v6, § 1, ligne S3 | idem S1 |
| S4 | sonde de refus ≈ 0,005 ; ligne de 1 | devis v6, § 1, ligne S4 ; préenregistrement court v9, « Seuil » | idem |
| S5 | répartition par relais lue à la course v9 | devis v6, § 3 | idem S1 |
| S6 | soldes et parts des clés : R-4258, R-4300, R-4342, R-4356 ; GO-2026-11-20-64, GO-2026-11-20-67, GO-2026-11-20-68, GO-2026-11-21-02 | `registres/decisions.md` et `registres/go.md` sur `origin/main`, commit `55f7f6e1fe6779a4fb57b5fd07f58d33d598cbef` | `352e3ea921a117faec79920fe9d329f6d96bcd1de524a04bd0eaaf2ed5caea16` ; `38f63a0d40b591fb1890437107cdb77511916360e2bda0baddda70ff5986d63b` |
| S7 | essai du bac seul sur une machine jetable : « sur devis de quelques dollars » | `registres/decisions.md`, R-3984 | idem S6 |
| S8 | crédit du loueur : 90,56 USD | `registres/etat.md` sur `origin/main`, même commit, dernière ligne de suivi | non recalculée à part |

**Un écart d'un centime, repris du devis v6.** Les rôles de S1 s'additionnent à 72,51, non à 72,50. Le calcul additionne les rôles.

## 2. La génération

Elle a la forme exacte de la course v9 : cinq proposeurs, onze appels chacun, un aiguilleur, deux juges. Cas bas : le coût réel de la course v9. Cas haut : le cas bas fois le facteur de chaque rôle (S2). Pire : le plafond d'arrêt.

**Ce qui peut l'éloigner de la course v9, sans que je le chiffre.** Les fiches portent ici un test de mort ; leurs sorties peuvent être plus longues. L'entrée est plus courte : la partie servie et la synthèse font quelques milliers d'octets, loin des lots de la course v9. Je ne retire ni n'ajoute rien : le plafond tient.

## 3. L'étage des tests de mort, et la machine

**Aucune mesure réelle n'existe** : l'étage n'a tourné qu'à zéro dollar d'appels, avec un expérimentateur écrit par programme (R-3882), et Lazar garde l'expérimentateur modèle (GO-2026-11-19-75).

Règles du rédacteur, pour vingt candidates :

- cas bas : une session d'expérimentateur par candidate, au coût réel moyen d'un appel de proposeur de la course v9 (58,65 / 55 = 1,07) : **21,33** ;
- cas haut : deux sessions par candidate, au coût réel le plus haut d'un appel (24,72 / 11 = 2,25), fois le facteur du haut de la proposition (1,1940) : **107,33** ;
- pire : le plafond de l'étage, **110**. L'étage ne lance une candidate que si son pire (deux sessions à 6,05, soit 12,10) tient dans ce qui reste. Si chaque session allait au pire, neuf candidates seulement seraient jouées ; les autres seraient « non jouées », dans l'ordre scellé d'avance.

Le lecteur et le comparateur sont des programmes : zéro dollar. Les calculs du bac sont des simulations de scores sur processeur.

**La machine jetable** se loue sous le devis du premier étage payant à tests de mort, l'essai du bac en première étape (GO-2026-11-20-05, point 4b). Seule source de prix : « quelques dollars » (S7). Règle du rédacteur : 2 au cas bas, 5 au cas haut, **10 de plafond**, location, essai du bac et étage compris. Une machine à processeur seul suffit ; aucune carte graphique. **L'offre du loueur est à relever et à mettre à la place de cette règle avant la ligne de GO.** Le crédit du loueur relevé au registre (90,56, S8) couvre ce plafond.

## 4. Plafonds par relais

| relais | ses rôles | cas bas | cas haut | pire |
|---|---|---|---|---|
| premier (clés Claude désignées) | proposeurs des espèces 3 et 4, aiguilleur, juge de l'espèce 3 | 36,46 | 85,34 | 150,00 |
| deuxième | proposeurs des espèces 1 et 5, juge de l'espèce 1 | 31,30 | 46,80 | 150,00 |
| troisième | proposeur de l'espèce 2 | 4,75 | 5,67 | 66,55 |
| relais de l'expérimentateur | l'expérimentateur de l'étage | 21,33 | 107,33 | 110,00 |

Les pires ne s'additionnent pas : le plafond de la génération (150) tient les trois premiers relais ensemble, celui de l'étage (110) tient le quatrième. Le pire du troisième relais est onze appels à 6,05.

## 5. Ce que chaque levier ferait perdre

| levier | total bas / haut / pire | ce qu'on perd |
|---|---|---|
| sans l'étage ni la machine | 73,70 / 143,81 / 156,00 | ce que la course apporte au-delà du collisionneur : il ne reste que des fiches, sans vérité en face. **Contraire à l'exigence de la mère.** |
| sans les deux juges | 87,75 / 208,82 / 276,00 | l'ordre de lecture de la mère, et la comparaison, après coup, du rang des juges au calcul. Le mandat les demande « pour information » ; le pire ne change pas, parce que la ligne de la génération reste à 150 |
| dix candidates au lieu de vingt | étage 10,66 / 53,66, plafond à ramener à 55 (moitiés faites à la main sur les valeurs non arrondies du calcul ; elles ne sont pas dans sa sortie) | la couverture des six voies : moins de deux candidates par voie |

## 6. Répartition proposée sur les clés désignées, avec les soldes connus au registre

**Ce que le registre dit des soldes** (S6 ; aucune clé n'a été lue par moi, aucune valeur, aucun nom de variable) :

| clé désignée | ce que le registre en dit | ce qui la tient déjà |
|---|---|---|
| Minuit | reste net estimé 162,56 (R-4258, estimation, non un relevé) | part de 156,56 dans la course « nouvelles attaques » ; marge de 24,90 au-delà de son cas haut (R-4356) |
| Luc | environ 214,00 déclaré (R-4258) | l'aiguilleur et l'espèce 4 de la course « nouvelles attaques » ; le juge de l'étage 2 de la ligne 3 (GO-2026-11-20-68) |
| Rigaud | solde déclaré 25 (GO-2026-11-21-02) | hors course ; ne garde que la réserve de 8,35 du bras A |
| deuxième relais (Google) | la carte paie au-delà du crédit, jusqu'au cas haut des appels **déjà accordés**, environ 164 (GO-2026-11-20-64) | course « nouvelles attaques », étage 2 de la ligne 3, deux collisionneurs |
| troisième relais (OpenAI) | recharge automatique ; reste en dollars lu contre 17,01 (R-4356) | course « nouvelles attaques » ; collisionneurs |

**Lecture.** La somme des parts de la course « nouvelles attaques » est de 439,59 sous 456 (R-4356). Tant que cette course n'est ni partie ni close, **aucune clé Claude ne peut promettre le cas haut du premier relais (85,34) ni celui de l'expérimentateur (107,33) sans empiéter sur une part scellée.**

**Proposition**, à écrire dans un complément de valeurs après un relevé du jour :

1. La course ne part qu'après la clôture de la course « nouvelles attaques », ou après une recharge. Les soldes sont alors relus, et chaque part est fixée au cas haut de ses rôles, bornée au solde relu (règle de GO-2026-11-20-16, gardée).
2. Premier relais : une seule clé Claude désignée pour ses quatre rôles (cas haut 85,34) ; Luc si son solde relu le tient, sinon Minuit.
3. Expérimentateur : l'autre clé Claude désignée, si l'expérimentateur est un modèle Claude (cas haut 107,33) ; je n'ai pas lu de quel relais il relève.
4. Deuxième relais : cas haut 46,80. Le mot de GO-2026-11-20-64 ne couvre que les appels déjà accordés : **il faut le mot de Lazar pour que la carte couvre aussi cette course.**
5. Troisième relais : cas haut 5,67, que le reste lu (17,01) couvre si la course « nouvelles attaques » ne l'a pas consommé ; son pire (66,55) ne tient que par la recharge automatique ou par l'arrêt nommé.
6. Rigaud : aucun rôle.

Une clé dont le reste relu ne couvre pas sa part : départ refusé.

## 7. Ce qui n'est pas chiffré

1. Le temps des sessions de conception et de contre-lecture (ordre de course, § 11) : zéro dollar d'appels d'interface, mais de la place sur le modèle F.
2. La lecture par la mère, et l'étiquetage « déjà au collisionneur ».
3. Une seconde génération : ce serait une course neuve, un devis neuf.
4. Le coût réel de l'expérimentateur : inconnu jusqu'au premier étage réel. Ce devis sera le premier à le mesurer ; il faudra le rendre au devis du palier 1 de l'héritage.

## 8. Décision demandée

**Décision en une phrase.** Accorder, ou non, une ligne de calcul de 260 USD pour la course « seuil et moniteurs » (une génération, un étage de tests de mort), avec trois lignes à part de 10, 5 et 1 USD, soit 276 USD au plus.

**Enjeu.** Des règles de seuil et des emplois du papier éprouvés au calcul, sur vérité plantée, au lieu d'être seulement discutés ; contre une dépense de l'ordre de 100 à 260 USD, et le premier étage réel à tests de mort de l'organisme, sur un code qui reste à écrire.

**Options.**
- (a) La ligne entière, 260 USD, après la clôture de la course « nouvelles attaques » et un relevé des soldes. Avantage : l'exigence de la mère est tenue en entier. Inconvénient : trois à cinq jours de sessions avant le premier appel ; la dépense la plus haute.
- (b) L'étage seul, sur les propositions du collisionneur : 110 + 10 USD, sans génération de l'organisme. Avantage : moitié moins cher, et le collisionneur a déjà payé les idées. Inconvénient : les propositions du collisionneur sont des textes libres, sans test de mort écrit ; il faut qu'un rédacteur les mette en fiches, ce qui est un choix humain ou de modèle entre les idées — un écart à N-058 à déclarer — et la grille de cases, le coût par espèce et la famille tenue à l'écart sont perdus.
- (c) Ne rien lancer, lire d'abord le collisionneur. Avantage : aucune dépense. Inconvénient : rien n'est éprouvé au calcul.

**Recommandation : (a), confiance 0,55.** Ce qui me ferait changer : que le collisionneur rende moins de dix règles distinctes et calculables — alors (b) suffit ; ou que le véhicule du palier 1 de l'héritage ne soit pas écrit sous dix jours — alors l'étage ne peut pas partir et (c) s'impose.

**Défaut sous 48 heures : aucun.** C'est une dépense : sans mot de Lazar, rien ne part.

**Ligne de GO proposée**, à la lettre :

> **Course de l'organisme d'idéation « seuil et moniteurs »** : une génération à cinq espèces (Kimi absent) et un étage de tests de mort avec l'expérimentateur modèle, sur mondes plantés scellés ; départ quand le préenregistrement court, les mondes plantés, le complément de valeurs et le véhicule sont contre-lus et scellés, et que l'essai du bac, la sonde de refus et l'épreuve des témoins sont passés ; ligne de course 260 USD exactement ; lignes à part : machine jetable et essai du bac 10 USD, épreuve des témoins 5 USD, sonde de refus 1 USD ; arrêt net à chaque plafond ; le régime « tests de mort réels » est accordé pour cette course seule. | 276 USD |
