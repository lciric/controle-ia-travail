# Diagnostic des témoins du juge — organisme d'idéation sur les organismes discrets — v2

Version 2 : la v1 (`daf46210…`, archivée sans modification, R12) renvoyait à un extrait hors du dépôt et taisait un écart ;
les deux sont corrigés ici, rien d'autre ne change.

Écrit le 18 novembre 2026 par la session de relance (`session_01XJ6MgpChR1JWSMBxSQcf3c`), à la demande de la session mère
(06:47Z) et de Lazar (« je recommande d'attendre que les témoins du juge soient corrigés »). **Sans dépense, sans aucune
fiche de proposeur ouverte** : seules les entrées des quatre témoins ont été extraites de la réponse du juge, par leur
étiquette anonyme (`noyau/cles-anonymisation-par-juge.json`) ; des fiches des proposeurs, seuls des comptes de notes ont été
lus. Extraction : `docs/notes/organismes-discrets-v1/organisme-ideation-v1/extrait-juge-temoins-v1.txt` (scellé).

## 0. Pièces lues

| pièce | chemin | empreinte |
|---|---|---|
| témoins v1 | `docs/notes/organismes-discrets-v1/organisme-ideation-v1/temoins-organisme-discrets-v1.json` | `1c6eef38…` |
| question v3 | `…/organisme-ideation-v1/question-v3.md` | `2f7acf36…` |
| faits v3 | `…/organisme-ideation-v1/faits-v3.md` | `5e2e9dd8…` |
| règle des témoins | orchestrateur épinglé `a41b7b50`, `pole/ideation_v2.py` l. 199 (`PORTE_ELIGIBILITE = 2`), l. 780-795 (grille), l. 939-965 (`lecture_temoins`), l. 2694-2702 (`_longueurs_temoins`) | arbre `ee84d6ec…` |
| course Astra | `runs/course-ideation-organismes-discrets-v8/20261118-062512-…-astra/` ; réponse du juge hors dépôt, `…/sortie/juges/traces-opus-juge/reponse.md` (scellée par l'orchestrateur) | — |
| course Argon | `runs/course-ideation-organismes-discrets-v8/20261118-063650-…-argon/` ; idem | — |

## 1. La règle

Un témoin est porté **éligible** par un juge si `max(avantage, originalité) ≥ 2` (notes entières de 0 à 3). Grille servie
au juge : avantage « décisif réel et incopiable à bas coût (0 : copiable par tout laboratoire avec une interface de
programmation de modèle ; 3 : structurel, le calcul n'y change rien) » ; originalité « 0 : occupé d'après les pièces
d'antériorité servies ou ce que tu sais (cite titre-auteurs-année, marque SUPPOSE) ; 3 : jamais fait nulle part ».
Un seul témoin manqué par un seul juge rend L2 et L4 illisibles (`lecture_temoins`, CL31-03). La fourchette de longueur
(CL34-12) est **rapportée**, elle n'entre pas dans `temoins_ok`.

## 2. (a) Ce que le juge a noté et pourquoi

| témoin | classe | attendu | Astra : (av., orig.) | Argon : (av., orig.) | tenu |
|---|---|---|---|---|---|
| p0-01 | vrai | éligible | (1, 1) | (1, 1) | **non**, deux fois |
| p0-02 | jumeau de p0-01 | éligible | (1, 1) ; jumeau signalé | (1, 1) ; jumeau signalé | **non**, deux fois |
| p0-03 | faux de falsifiabilité | inéligible | (0, 0), falsifiabilité 0 | (0, 0), falsifiabilité 0 | oui |
| p0-04 | faux d'antériorité | inéligible | (0, 0) | (0, 0) | oui |

Justifications du juge, verbatim :
- p0-01, avantage : « Les données permutées sont propres au programme, mais le classifieur se reproduit à faible coût. »
  (Astra) ; « Un classifieur de cohérence locale est copiable à bas coût. » (Argon).
- p0-01, originalité : « La détection d'incohérence entre champs est courante (Kryscinski et autres, 2020, SUPPOSE). Seule
  l'application est transposée. » (Astra) ; « … Doublon de T04. » (Argon).
- p0-02 : « Contrôle par remplacement aléatoire, diagnostic courant. L'antériorité citée n'est pas une référence
  identifiable (SUPPOSE). » ; « … la procédure est triviale à reproduire. »
- p0-03 et p0-04 : rejetés pour les raisons voulues par leur construction (« remarque générale » ; « occupée par la pièce
  d'antériorité elle-même, faits-v3.md, points 5d et 6 »).

Le juge est **constant** d'une course à l'autre (mêmes notes, mêmes raisons), **juste sur les deux faux**, et il signale le
jumeau. Dans **les deux courses**, il signale aussi qu'une fiche de proposeur est un doublon du vrai témoin (Astra : T08–T10 ;
Argon : T06–T04, et T05 « variante de T04, T06 et T12 »).

## 3. (b) Les témoins satisfont-ils la lettre de la règle ?

**Non, pour p0-01 et p0-02.** Leur propre texte les place sous la porte :
- **Avantage** : le vrai témoin écrit lui-même « un classifieur de cohérence locale se construit sur ces mêmes données sans
  coût de calcul supplémentaire important » ; son seul « incopiable » est l'accès aux données du banc. La grille demande un
  avantage que le calcul ne rattrape pas ; « copiable par tout laboratoire avec une interface » vaut 0 à 1. Le juge applique
  la lettre.
- **Originalité** : les deux fiches se déclarent elles-mêmes de niveau « transposition » d'une technique « courante »,
  avec une antériorité marquée SUPPOSÉ. La grille met 0 à « occupé d'après ce que tu sais ». 1 est généreux.
- **La question v3 nomme l'idée** : sous-question 1, « discordance locale texte/champ » (même texte dans les questions v1,
  v2 et v3). L'idée du vrai témoin est donc **donnée à chaque proposeur par l'énoncé** ; les proposeurs l'ont écrite (les
  doublons ci-dessus). Un témoin « vrai » ne peut pas être original au sens de la grille s'il reformule la question.
- **Longueur** : p0-03 (2 407 caractères) et p0-04 (2 606) sont sous la fiche la plus courte (3 353, Astra) : discernables par
  leur seule longueur (rapporté par l'orchestrateur, sans effet sur la lisibilité ; défaut de validité pour la suite).

Sur les fiches des proposeurs (comptes seulement), le même juge porte éligibles 2 fiches sur 12 (Astra) et 5 sur 10 (Argon) :
il n'est pas incapable de franchir la porte.

## 4. (c) Le défaut tient-il au témoin, au juge ou à leur décalage de versions ?

**Au témoin.** Le juge applique la grille à la lettre, constamment, et tient les deux faux. Aucun décalage de versions : les
témoins v1, les questions v1 à v3 et les faits v3 entrent au dépôt par le même commit (`9b5d3438`, 17 novembre, 13:03Z), et
l'idée du vrai témoin figure dans les trois versions de la question. Le défaut est de **construction** : le « vrai » témoin
est un bon candidat d'auditeur (il serait utile), mais il n'est ni incopiable ni original au sens de la grille, et il reprend
l'énoncé. Changer de juge ne corrigerait rien : un juge qui le porterait éligible appliquerait la grille moins bien.

## 5. (d) La correction la plus petite

1. **Témoins v2** (nom neuf, R12 ; v1 gardée) : remplacer **la paire vrai et jumeau** par une paire dont l'idée (i) n'est
   nommée ni dans la question v3 ni dans les faits v3 (vérifiable par recherche de ses termes clés dans les deux pièces),
   (ii) revendique un avantage que la grille met à 2 au moins — dépendant d'une ressource que le calcul seul ne rattrape pas,
   dit dans la fiche sans la contredire —, (iii) déclare une originalité « jamais fait à notre connaissance » avec une
   recherche d'antériorité écrite, et (iv) tient dans la fourchette de longueur des fiches (3 353 à 4 808 caractères dans
   les deux courses). **Allonger p0-03 et p0-04** dans la même fourchette, sans changer leur défaut voulu.
2. **Épreuve des témoins seuls avant toute course** : le mode « juges seulement » de l'orchestrateur épinglé
   (`pole/juges_seulement_v1.py`) note des fiches données sans proposeur ; faire noter par le juge Opus les quatre témoins
   v2 mêlés à quelques fiches neutres, et ne lancer une course que s'il tient les quatre. Coût d'un juge Opus sur une
   consigne de cette taille : ≈ 0,3 à 0,5 USD (la course Astra : juge et proposeur Opus ≈ 0,9 en tout). Dépense sur GO.
3. Les lanceurs v9 (Kimi) et v10 (Carbon) épinglent les témoins v1 : une version 11 et une version 12 (ou une seule version
   à deux lignées) épingleront les témoins v2 ; la même chose pour une reprise d'Astra et d'Argon si Lazar la veut.

Ce qui n'est pas proposé : baisser la porte (code de l'orchestrateur épinglé, hors de ce dépôt) ; changer de juge (le défaut
n'est pas là) ; rejouer Astra ou Argon avec les témoins v1 (même issue certaine).

## 6. Réserves

- Écart à « aucune fiche ouverte », dit ici : une commande de lecture de la forme de la réponse du juge a affiché, une fois,
  les 300 premiers caractères de la réponse, soit le début de la justification du juge sur une fiche de proposeur (T01 de
  la course Astra, une phrase sur son avantage) ; rien d'autre ; ni la fiche ni sa consigne n'ont été lues.

- Deux courses, un seul juge : la constance observée est sur deux tirages.
- « Le juge est juste sur les faux » ne dit pas qu'il est bien étalonné en haut d'échelle ; l'épreuve du point 5.2 le dira.
- L'écriture de témoins v2 « vrais » est elle-même difficile : une idée réellement neuve et incopiable sur ce banc est ce que
  la course cherche. Un témoin vrai qui le serait trop contaminerait le classement (le juge le comparerait aux fiches) ; la
  règle (iv) et l'épreuve 5.2 en limitent l'effet, sans l'annuler.
