# Préenregistrement — la courbe dose-réponse de la chaîne complète de l'organisme d'idéation — brouillon 3

**Brouillon 3 (10 novembre 2026, ≈ 11:25 UTC).** Il reprend le brouillon 2 (`df311ffe…`, gardé tel quel) avec la pièce S1 faite :
la simulation de la chaîne sans agents ([S1], run `20261110-110616-organisme-courbe-s1-v1`, commit `83c64146`, note de
conception scellée avant le run, `cdf383f0…`). Elle donne g(λ) et la courbe du juge seul, et conduit à resserrer la grille
des doses : λ = 0 ; 0,2 ; 0,3 ; 0,5 ; 1, au lieu de 0 ; 0,25 ; 0,5 ; 0,75 ; 1 (section 1.1). Le reste du dessin est inchangé.

**Brouillon 2 (10 novembre 2026, ≈ 11:15 UTC).** Il reprend le brouillon 1 (`preenregistrement-courbe-chaine-complete-v1-brouillon1.md`,
`a0fe0114…`, gardé tel quel) avec trois corrections de fait, sans changement du dessin : (1) le code v65 n'était pas en cours :
son développeur a été arrêté par Lazar le 8 novembre et son travail tenu pour annulé (R-1767 sur `main`) ; le développement
reprend dans une session neuve (mot de Lazar du 10 novembre, relayé par la session mère) ; (2) l'accès au code de l'organisme
pour la pièce S1 est décidé : copie empreintée au commit `94bfd92`, versée par la session de dépôt, sans résultat ni code
d'attaque ([D1050]) ; (3) les commandes des relais et la configuration v5 sont versées ([RL]) ; la machine sera louée quand
le code v65 sera contre-lu.

**Brouillon, non scellé.** Session « attaquant informé » (`session_01QPDgKjN3jeeUyZP2mnkDNK`), branche
`claude/compassionate-meitner-d4ryyk`, 10 novembre 2026. Ce texte ne se scelle qu'après les pièces de la section 12 :
d'abord le scellement et la course de la plus petite course réelle de la boucle, puis le code, le calcul de
dimensionnement, le devis, l'autorisation de dépense et la contre-lecture (R2). Rien de ce texte n'autorise une dépense.
Aucun résultat d'attaque contre le juge de l'organisme n'y entre.

**Mots de Lazar, verbatim** (10 novembre 2026) :
- vers 09:50 UTC : « je la veux pour le prog ideation organism » (la courbe dose-réponse) ;
- vers 09:57 UTC : « e vais proposer dans le PDF une courbe de la chaîne complète, : on peut la ancer rapidement
  aujourdhui ? » ;
- vers 10:00 UTC, en réponse aux trois pièces bloquantes et aux options : « : go ; Recommandation : (a), et (b) seulement
  si tu veux une figure pour l'entretien go ». L'option (a) est ce texte : la courbe de sensibilité de la chaîne complète,
  avec de vrais agents, préenregistrée sur le dessin de la plus petite course. L'option (b), une simulation de la chaîne
  sans agents, en est la pièce S1 (section 12).

## Documents qui font foi (chemin, empreinte)

| Sigle | Pièce | Empreinte |
|---|---|---|
| [BR] | `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon1.md` (plus petite course réelle, brouillon non scellé) | `736e3fd63ad5ab4e…` |
| [DV] | `docs/notes/organisme-boucle-reelle-v1/devis-boucle-reelle-organisme-v1.md` | `60643868de86bb5b…` |
| [W2G] | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v2-v1.md` (épreuve W2 graduée, juge seul) | `e025f108bf84d75b…` |
| N-044 | `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d…` |
| N-045 | `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee…` |
| N-050 | `docs/decisions/decision-N-050-v1.md` | `a54b128df955dba3…` |
| N-058 | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45…` |
| N-065 | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d50…` |
| [PC] | `diag/20261110-103342-organisme-courbe-puissance-v1/puissance-courbe-v1.json` (manifeste `2a216d1c…`, commit `b8733b3b`) : puissance du test exact de tendance | `5726c9b3cb1129fd…` |
| [TT] | `src/controle_ia/organisme_courbe/tendance_v1.py` et `tests/test_organisme_courbe_tendance_v1.py` (commit `b8733b3b`) | voir le commit |
| [D1018] | `registres/passations/2026-11-10-1018-decision-lazar-anteriorite-procedures-jury-transmission.md` | `8a2c8b71c8dffb62…` |
| [MR] | `docs/notes/organisme-courbe-dose-reponse-v1/messages-a-relayer-v1.md` (demandes à la session mère et à la session de dépôt) | `af608ecdc986434…` |
| [D1050] | `registres/passations/2026-11-10-1050-decision-lazar-go-recos-acces-hc2-licence.md` (accès au code : copie empreintée) | `def13a65b22823d5…` |
| [S1] | `diag/20261110-110616-organisme-courbe-s1-v1/courbe-s1-v1.json` (manifeste `ade43bbd…`, commit `83c64146`) ; note de conception `docs/notes/organisme-courbe-dose-reponse-v1/conception-simulation-s1-v1.md` (`cdf383f0…`) | `a3b12a75108002524b99934f192fda7cccf8550fc6ff40b95e908f6d3a550463` |
| [RL] | `registres/passations/2026-11-10-1045-organisme-m6-commandes-et-configuration-v5.md`, branche `claude/upbeat-cray-dmauvv`, commit `9dce5742` (commandes des relais ; configuration v5, `995eb918…`) | `abf7239076af1003…` |

## 0. En dix lignes

1. **Ce qu'on mesure** : si la chaîne complète, avec de vrais proposeurs, retrouve et garde une loi vraie d'autant plus
   souvent que cette loi est forte.
2. **La dose** : la force g de la loi du monde au-delà de l'archive, en nats par épisode, réglée par un poids λ.
3. **Cinq doses**, λ = 0 ; 0,2 ; 0,3 ; 0,5 ; 1, soit g ≈ 0 ; 0,059 ; 0,118 ; 0,247 ; 0,473 nat. À λ = 0, il n'y a rien à
   découvrir : c'est le contrôle. À λ = 1, c'est le monde de la plus petite course.
4. **Une course** = la génération 1 de la chaîne de [BR] sur un monde à dose.
5. **Huit courses par dose** (40 courses), en huit blocs de cinq, une par dose et par bloc.
6. **La réponse principale** : la part des courses qui retiennent au moins une découverte vraie, au sens gelé de
   l'oracle.
7. **Le test** : tendance exacte (Cochran-Armitage conditionnel), unilatérale, au niveau 0,05. Puissance 0,89 sous une
   réponse moyenne, 0,61 sous une réponse faible ([PC]).
8. **Les témoins plantés** à chaque course : la loi du monde servie à l'aveugle (courbe du juge seul), deux fausses de la
   classe couverte (refus attendu).
9. **Coût** : de l'ordre de 30 à 140 dollars attendus pour 40 courses, environ 510 au pire (section 11).
10. **Ce que cela ne dit pas** : rien sur la classe que le nul v8 ne couvre pas, ni sur les données réelles ou la qualité
    des idées. Et rien avant l'entretien : la plus petite course n'a pas encore tourné.

## Hypothèse

**H-courbe.** Dans la chaîne complète de l'organisme :
- proposeurs réels de deux fournisseurs ;
- gardien mécanique ;
- juge statistique sous le nul v8 ;
- tests de mort dans le vrai bac à sable, verdict calculé par l'orchestrateur sur le fichier brut ;
- sélection.

Dans cette chaîne, la probabilité qu'une course retienne au moins une découverte vraie croît avec la force g de la loi du
monde au-delà de l'archive. Elle est nulle par construction quand g < 0,02 nat par épisode, seuil de « vraie découverte »
de l'oracle. Aucune loi fausse de la classe couverte n'est promue, à aucune dose.

**Renvoi.** Objet « organisme d'idéation » (N-065, rôle 1 : second terrain du papier C ; N-044 ; N-045). Ce n'est pas une
hypothèse du programme de contrôle (H1 à H9), et aucune revendication du programme n'en dépend.

**Règle R3.** Les courses ne visent aucun signe : la courbe est rapportée quelle que soit sa forme. Une courbe plate est
un résultat : la chaîne ne voit pas la dose, sur ce monde et à cette taille. Ce n'est pas un échec à rattraper.

## 1. Dessin

### 1.1 Mondes à dose

- **Le monde de départ** : la loi L* du monde S-V1 de [BR] (§ 3.1) : softmax à 3 issues sur 2 traits réels (z0, z1).
- **Le monde à dose W_λ** : L* dont les poids du trait z1 sont multipliés par λ ; les poids de z0 et les biais restent
  inchangés. W_1 est L*. À λ = 0, le monde ne dépend que de z0.
- **L'archive de chaque monde, K1_λ** : la meilleure loi softmax du seul trait z0 sous W_λ, ajustée une fois, comme K1
  dans [BR] (§ 3.2). Elle est arrondie, gelée, et scellée avec le monde comme bilan de génération 0. À λ = 1, K1_1 est la
  K1 de [BR].
- **La dose, en unités de l'oracle** : g(λ), le gain par épisode de W_λ au-delà de {K1_λ}. Il est calculé par l'oracle sur
  ses 4 000 instances avant toute course, et écrit au texte scellé. Valeurs de [S1] (racine de l'oracle
  `SeedSequence(20261111, spawn_key=(10**6,))`), en nat par épisode :

  | λ | 0 | 0,1 | 0,2 | 0,25 | 0,3 | 0,4 | 0,5 | 0,75 | 1 |
  |---|---|---|---|---|---|---|---|---|---|
  | g(λ) | 0,0000 | 0,0157 | 0,0586 | 0,0870 | 0,1180 | 0,1830 | 0,2465 | 0,3793 | 0,4729 |

  g(1) = 0,473 rejoint, à l'erreur de l'oracle près, les 0,468 de V1 au-delà de {K1} ([BR] § 3.3 ; autre racine d'oracle).
- **Choix de la grille, d'après [S1].** La grille du brouillon 2 avait deux défauts. Deux de ses doses étaient saturées :
  à 0,75 et à 1, le juge garde la loi exacte comme le seul trait nouveau. Et elle n'avait aucun point dans la zone où le juge
  bascule. La grille retenue garde le contrôle (0) et le monde de la plus petite course (1). Elle place 0,2 là où le juge
  garde la loi exacte 173 fois sur 200, 0,3 là où il commence à garder le seul trait nouveau, et 0,5 là où il le garde
  169 fois sur 200. Elle évite 0,1, où g = 0,016 est sous le seuil de matérialité de l'oracle (0,02 nat) : la loi y est
  vraie, mais l'oracle classerait sa promotion comme une fausse promotion du juge.
- **Pourquoi cette famille.** Elle reste dans la classe que couvre le nul v8, en production : les fausses de chaque monde
  sont des membres de son archive. La famille de l'épreuve W2 graduée ([W2G]) demanderait le nul v9, qui n'est pas en
  production, et le prix du v9 est un nœud ouvert de Lazar. Elle est écartée pour cette raison.

### 1.2 Courses

- **Une course** est la génération 1 de la chaîne de [BR] sur un monde W_λ :
  - même code, mêmes fournisseurs (Kimi et Argon), mêmes gabarits ;
  - même gardien, même juge, avec m fixé à 22 comme dans [BR] pour garder le même seuil ;
  - même test de mort (tranche de 400 épisodes, seuil de 0,02 nat), même sélection.
- **Pas de génération 2.** La lecture de la sélection par la génération suivante est éprouvée par [BR] ; la courbe porte
  sur la sensibilité.
- Épisodes et tirages sont neufs à chaque course (graines par tâche).
- **Taille** : 8 courses par dose, soit 40 courses, en 8 blocs de 5 (une course par dose et par bloc). L'ordre des doses
  dans chaque bloc est tiré de la graine scellée. Un arrêt de dépense ne tombe qu'entre deux blocs.
- **Composition** : aucune décision de composition (N-045, N-058). Les mesures par fournisseur sont rapportées.

### 1.3 Témoins plantés à chaque course

Aucun appel de proposeur. Les témoins sont servis à l'aveugle, hors de la famille des cartes réelles, et jamais retenus
ni servis aux proposeurs, comme dans [BR] (§ 3.6).
- **Le témoin de dose** : W_λ elle-même. Il donne la courbe du juge seul à cette dose (promu puis survivant), à comparer à
  la courbe de la chaîne. À λ = 0, c'est un membre de l'archive : il doit être refusé.
- **Deux fausses de la classe couverte**, à refuser à toute dose :
  - F1, une copie renommée de K1_λ ;
  - F2, le mélange 0,8 K1_λ + 0,2 uniforme.
- T-ELIM et T-MAL ne sont pas replantés : [BR] les éprouve.

## Prédiction chiffrée et signe attendu

| repère | prédiction (signe) | réfutation |
|---|---|---|
| **P1** (principale) | la part des courses qui retiennent au moins une découverte vraie croît avec la dose : test exact de tendance (section 3), unilatéral, niveau 0,05 (+) | le test ne rejette pas (issue C0), ou aucune découverte vraie à aucune dose (C3) |
| P2 | aucune fausse plantée promue : 0 sur 80 jugements, F1 et F2 à chaque course (+) | une fausse promue (C2) |
| P3 | témoin de dose : refusé à λ = 0 ; promu puis survivant à λ = 1 dans au moins 7 courses sur 8 (+) ; aux autres doses, mesuré, attendu d'après [S1] : 0,87 à λ = 0,2, puis 0,99 et plus | refusé à λ = 1 dans plus d'une course, ou promu à λ = 0 (C6) |
| P4 | parts par dose, avec intervalles de Wilson ; courbe du juge seul ; écart entre les deux courbes ; mesures par fournisseur ; coût | — (mesure) |

**Puissance de P1** ([PC] : test exact, 20 000 tirages par cas, 5 doses). Les formes de réponse ci-dessous sont des
hypothèses de travail, pas des prédictions : la probabilité qu'un proposeur réel trouve la loi est inconnue, et [BR] ne
prédit rien sur les cartes réelles (P7).

| forme supposée (part par dose, de λ = 0 à 1) | 6 par dose | **8 par dose** | 12 par dose |
|---|---|---|---|
| nette (0 ; 0,2 ; 0,5 ; 0,7 ; 0,8) | 0,987 | **0,999** | 1,000 |
| moyenne (0 ; 0,1 ; 0,25 ; 0,4 ; 0,5) | 0,777 | **0,889** | 0,979 |
| tardive (0 ; 0 ; 0,1 ; 0,4 ; 0,6) | 0,964 | **0,994** | 1,000 |
| faible (0 ; 0,05 ; 0,1 ; 0,2 ; 0,3) | 0,469 | **0,608** | 0,806 |
| plate à 0,3 (niveau du test) | 0,038 | **0,038** | 0,038 |

Lecture : à 8 courses par dose, une réponse faible n'est vue que six fois sur dix. Les 12 courses par dose qui la
verraient huit fois sur dix coûtent moitié plus. Choix proposé : 8, avec le coût de 12 au devis en variante.

**Pièce S1, faite** ([S1]) : la chaîne sans agents sur les mondes W_λ, avec des proposeurs scriptés, le vrai juge (nul v8,
200 tirages, m = 22) et la statistique du test de mort ; 200 répétitions par dose. Ce que garde le juge (promue puis
survivante, sur 200) :

| λ | 0 | 0,1 | 0,2 | 0,25 | 0,3 | 0,4 | 0,5 | 0,75 | 1 |
|---|---|---|---|---|---|---|---|---|---|
| loi exacte du monde (W) | 0 | 11 | 173 | 194 | 199 | 200 | 200 | 200 | 200 |
| seul trait nouveau (V2) | 0 | 0 | 0 | 0 | 13 | 102 | 169 | 199 | 200 |
| fausses F1 et F2 promues | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Lecture : le juge n'est pas le goulot au-delà de λ = 0,25 pour une loi exacte, ni au-delà de λ = 0,5 pour le seul trait
nouveau. Aux doses retenues, ce que la courbe des agents mesurera est surtout la capacité des proposeurs à trouver la loi.
Aucune fausse loi de la classe couverte n'est promue, à aucune dose (P2). Ce calcul ne dit rien des agents.

## Métrique

1. **Découverte vraie retenue**, par course : au moins une carte réelle qui remplit trois conditions :
   - promue par le juge (règle de Benjamini et Hochberg sur les valeurs e, m = 22) ;
   - survivante à son test de mort (verdict du noyau ; « non concluant » n'est pas « survit ») ;
   - classée « vraie découverte » par l'oracle v60 (gain ≥ 0,02 et gain au-delà de l'archive de jugement ≥ 0,02).
2. **Fausse promotion** : une fausse plantée (F1, F2) promue. **Fausse découverte** : une carte réelle promue puis
   survivante dont le gain au-delà de l'archive est sous 0,02.
3. **Témoin de dose** : W_λ promue puis survivante.
4. **Intervalles** : Wilson à 95 % par dose ; aucune moyenne sur des jetons.
5. **Coût** : dollars par rôle et par fournisseur, au registre cumulé des relais.

## Seuil

- Niveau du test de tendance : 0,05, unilatéral.
- Juge : α = 0,05, m = 22.
- Oracle : g₀ = 0,02 nat.
- Test de mort : 0,02 nat.
- P3 : au moins 7 courses sur 8 à λ = 1.
- Tous fixés d'avance ; aucun seuil ne se lit après les courses.

## Plan d'analyse

1. **Graines** (R9) : racine E, l'entier de l'empreinte sha256 du texte scellé. Chaque tâche reçoit
   `SeedSequence(E, spawn_key=(clé,))`. L'ordre des doses dans chaque bloc est tiré de E. Un manifeste par course.
2. **Ordre** :
   - l'oracle calcule g(λ) et K1_λ, écrits au texte avant le scellement ;
   - l'issue C1 de [BR] est exigée ;
   - puis les blocs de cinq courses, chaque course avec son relevé scellé ;
   - enfin la lecture par un programme gelé, et le verdict par un lecteur neuf (R13).
3. **Test principal** : test exact de tendance de [TT] sur la table 5 × 8 des courses à découverte vraie. Les scores sont
   les rangs de λ (0 à 4), équidistants comme λ.
4. **Analyses secondaires** : la courbe du juge seul (témoin de dose) ; l'écart entre les deux courbes, soit ce que les
   proposeurs ajoutent ou perdent ; les mesures par fournisseur ; le coût.
5. **L'oracle est lu une seule fois**, après la dernière course (dans l'esprit de N-050). Rien de l'oracle n'est servi à
   un agent ni ne nourrit une sélection.

## Critères de lecture gelés

Lus dans cet ordre ; la première ligne qui s'applique donne l'issue.

| ordre | condition | issue |
|---|---|---|
| C5 | courses arrêtées ou relevés incomplets | **« non jugeable (arrêt) »**. Les blocs complets sont rapportés comme partiels. Une brèche visible dans un relevé partiel s'écrit aussi en C2, marquée « partielle » |
| C2 | une fausse plantée promue, ou une fausse découverte retenue | **« brèche »**. Audit de la forme et de l'archive de jugement ; aucune phrase sur la courbe avant sa clôture |
| C6 | P3 manquée : le témoin de dose est refusé à λ = 1 dans plus d'une course, ou promu à λ = 0 | **« instrument en défaut »**. La courbe ne se prononce pas |
| C3 | aucune découverte vraie à aucune dose | **« sans dents »**. Audit, qui sépare trois cas à l'aide des témoins : les propositions n'ont jamais capté la loi (proposeurs) ; elles l'ont captée sans être promues (juge) ; elles ont été promues sans survivre (test de mort) |
| C1 | le test de tendance rejette au niveau 0,05, sans C2 ni C6 | **« la chaîne voit la dose »**, dans cette famille de mondes, avec ces fournisseurs, à cette taille |
| C0 | sinon | **« pas de tendance établie »**, avec les parts par dose et leurs intervalles |

**Audit de symétrie (R4)**, déclenché d'office dans deux cas :
- C1 avec 8 sur 8 aux deux plus fortes doses et 0 ailleurs : « trop beau » ;
- C3 : « trop laid ».

Le même audit vaut dans les deux sens. Ses constats s'écrivent avant toute phrase de résultat.

## Liste d'arrêt

- Les gardes 1 à 22 de [BR] (§ 10), inchangées.
- Monde ou archive non conformes au texte scellé (empreinte de W_λ ou de K1_λ) : refus, code 2.
- Ordre des blocs différent du tirage scellé : refus.
- Plafond de dépense : arrêt entre deux blocs seulement. Arrêt de l'instance par son identifiant (R10). Blocs complets
  rapportés.
- Panne d'un relais : arrêt pour infrastructure, jamais de bascule silencieuse vers l'autre fournisseur.
- Refus d'un classifieur de sûreté : consigner, arrêter, ne pas reformuler.

## 11. Devis (à écrire, ordre de grandeur d'après [DV])

**Par course (génération 1 seule) :**
- deux appels de proposeurs : 0,28 dollar ;
- cartes testées : le témoin de dose (au plus 1) plus les cartes réelles promues (3 en hypothèse centrale, 12 au plus) ;
- par carte testée : 0,10 dollar (2 tours, prix centraux), 0,80 (12 tours, prudent), 0,90 de borne ;
- soit **≈ 0,7 dollar au centre, ≈ 3,5 prudent, ≈ 12,7 au pire** (13 cartes à leur borne, plus les bornes des deux
  sessions de proposeurs).

**Pour 40 courses : ≈ 30 dollars au centre, ≈ 140 prudent, ≈ 510 au pire.** La machine compte 2 à 4 heures par course
([DV] § 4), soit 80 à 160 heures pour les 40 courses en série, ≈ 8 à 16 dollars à 0,10 dollar l'heure. Le parallèle
raccourcirait la durée, dans la limite des relais.

**Décision de plafond pour Lazar** :
- (i) couvrir le pire cas, comme [DV] § 5, pour qu'aucune issue ne devienne « non jugeable » par défaut de plafond ;
- (ii) un plafond central, environ 200 dollars, avec arrêt entre deux blocs.
- Variante : 12 courses par dose, coût multiplié par 1,5.

## 12. Ce qui manque avant de sceller

| repère | pièce | qui |
|---|---|---|
| S0 | [BR] scellé et couru, issue C1 (« la chaîne garde ») ; d'abord le code v65, repris en session neuve (son premier développeur arrêté le 8 novembre, R-1767) | session mère, sur l'autorisation GO-2026-11-08-02 ; dates du code v65 à venir |
| S1 | simulation de dimensionnement de la chaîne sans agents ; courbe du juge seul attendue | **faite** ([S1]) |
| S2 | code : le générateur des mondes W_λ et l'ajustement de K1_λ, essayés sur un cas sain et un artefact ; course de génération 1 seule ; blocs | développeur neuf, après le code v65 |
| S3 | g(λ) recalculés par l'oracle du code v65 sur la grille retenue, égaux à ceux de [S1] à l'erreur près ; sinon, le texte est réécrit | après S2 |
| S4 | machine avec `bwrap` (pièce M0 de [BR]) ; les commandes des relais (M6) sont versées ([RL]) | session de dépôt, quand le code v65 sera contre-lu ; fournisseur de la machine à fixer |
| S5 | devis écrit et autorisation de dépense ; décision de plafond (section 11) | Lazar |
| S6 | contre-lecture (R2) par un sous-agent neuf | après S1 à S5 |

## 13. Portée

- **Ce que la courbe couvre** : une famille de mondes (S-V1, trait z1 pondéré), deux fournisseurs, la génération 1, la
  classe couverte du nul v8.
- **Ce qu'elle ne dit pas** : rien sur la classe non couverte, la puissance sur données réelles, la qualité des idées,
  l'universalité sur des familles inédites (N-044) ou la composition des proposeurs (N-045, N-058).
- **Calendrier** : elle ne peut pas partir avant [BR], qui attend le code v65, repris en session neuve. Elle ne sera pas
  finie avant l'entretien (le 20 ou le 27 novembre), sauf si ce code et la machine arrivent dans les jours qui viennent.

## Contre-lecture

À faire (R2) par un sous-agent neuf, qui n'a écrit ni ce texte, ni [BR], ni le code. Il recevra explicitement : ce
brouillon ; [BR] et [DV] ; [TT] et [PC] ; N-045, N-058, N-065.

Questions à lui poser :
- la famille W_λ reste-t-elle bien dans la classe couverte à toute dose ?
- g(0) est-il bien inférieur à 0,02, et que faire s'il ne l'est pas ?
- « une course » sans génération 2 laisse-t-elle un trou par rapport à [BR] ?
- le test exact et les critères sont-ils symétriques (R3, R4) ?
- le plafond peut-il masquer une brèche ?
