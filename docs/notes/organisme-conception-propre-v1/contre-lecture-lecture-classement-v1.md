# Contre-lecture — outil du lecteur et programme de classement, course « conception propre » — v1

Contre-lecteur neuf (modèle B, autre que l'auteur), sous-agent de la session mère ; 14 novembre 2026, de 00:02 à 00:10 UTC
(heures relevées par `date -u`). Lu : `conception-course-v1.md` (`be3ba97e…`, § 4 à 7), `consigne-lecteur-v1.md`
(`95efebaa…`), les trois fichiers de témoins et `temoins-plantes-v1.md`, la question, le catalogue, tout le dossier
`lecture-classement-v1/` (outil `59e665af…`, classement `f91962f3…`, essais `72cfd065…`, banc `642243ad…`, rapport
`d76c89d6…`), la ligne R-2626, la condition C5 de la contre-lecture du lanceur, le gabarit et le validateur de
l'orchestrateur (clone, lecture seule), le relais Kimi v4 (bornes). Empreintes des pièces : toutes égales à leurs compagnons.
**Aucun fichier de `runs/course-ideation-conception-propre-v1/` ouvert, aucune fiche lue, aucun modèle appelé, aucune clé,
rien écrit sous `src/` ni `tests/`, aucun chemin interdit ouvert.** Mes essais ont tourné dans un dossier temporaire hors
du dépôt, retiré.

## Verdict : « après corrections »

L'outil et le classement appliquent la règle des § 4 à 7 sans rien y ajouter ni retrancher que j'aie pu trouver ; l'aveugle
tient sur les clés, l'ordre et la typographie ; aucun modèle n'est appelé ; le juge de l'organisme n'est jamais lu ; le calcul
de A1 est juste. Trois corrections avant tout envoi au lecteur (M1, M2, M3), dont deux touchent un silence de la règle et
doivent donc être **déclarées** comme les précisions A3 et A4 ; et le nœud A1 reste à Lazar.

## Constats, par gravité

### Majeurs (à corriger avant l'envoi)

- **M1 — La vérification des citations est exacte, mais vide de contenu.** `passage_dans` n'exige aucune longueur : un
  passage d'un caractère prouve n'importe quel critère (`"e"`, `"+"`, `"."` : « mot pour mot », essai S1). Pour N, le
  passage du catalogue est cherché dans **toutes** les cellules de la ligne, y compris la cellule du code et celle de la
  source : `passage_catalogue = "C7"` ou `"2026"` prouve l'occupation C7. Un lecteur paresseux ou qui invente ses
  citations n'est donc pas arrêté ; A3 le dit pour la longueur (« aucune longueur minimale »), pas pour la cellule du code.
  *Correction* : (a) chercher le passage du catalogue dans les seules cellules « Conception » et « Mécanisme central » ;
  (b) soit une longueur minimale du passage (précision à déclarer, par exemple 20 caractères hors espaces ; R4 hors
  `levier:juge` n'est pas concerné), soit, au moins, le compte des passages courts par critère et par lecture dans
  `classement-v1.json` et `.md`, et ce compte ajouté aux pièces de l'audit de propreté.
- **M2 — Un lot perdu est compté zéro en silence, et la désignation reste possible.** Essai S5 : 36 fiches factices, 20
  témoins, un lot de la lecture 2 rendu illisible (15 fiches réelles mises à 0, ni le vrai ni le jumeau dedans) → verdict
  « lisible, L5 rejetée (p = 0,017) : deux idées désignées » ; l'anomalie n'apparaît que dans le JSON, pas dans le verdict ni
  dans `classement-v1.md`. Les deux désignées sont alors choisies parmi les seules fiches des lots lisibles. Le risque est
  réel : `max_tokens` (32 768 au plus) couvre aussi le raisonnement de Kimi ; une fin `length` donne un JSON coupé, donc un
  lot entier à zéro, sans relecture possible (6 appels). A4 dit le choix (« tout compté 0, sans arrêt ») mais pas cette
  conséquence. *Correction* : le verdict et le résumé citent toute anomalie (`reponse_illisible`, `entree_manquante`,
  `entree_en_double`, `fin_non_stop`) et le nombre de fiches réelles touchées ; et, à déclarer avant la lecture : une
  anomalie qui touche une fiche réelle admissible ou un témoin interdit la désignation (lecture « incomplète », traitée
  comme E2), ou bien la désignation est dite « sous lecture incomplète ». Je recommande la première, sans trancher.
- **M3 — La condition C5 ne tient que par le geste de la mère.** `preparer` accepte n'importe quel chemin pourvu qu'il ait
  un compagnon et une attestation. Essai S4 : un fichier à la forme de la liste des fiches en quarantaine (`{"fiche",
  "signaux"}`) est **accepté** : 0 fiche réelle, 11 « hors question », deux envois préparés (témoins seuls), sans refus.
  Le classement, lui, ne lit que le dossier des envois, le catalogue et l'outil : jamais les notes du juge (vérifié à la
  lecture et par l'essai de l'auteur). *Correction* : refuser un fichier dont le nom n'est pas
  `sortie--fiches-validees.json` sous un dossier `copies`, un élément sans les clés du gabarit, et une pile sans aucune
  fiche réelle admissible (aujourd'hui : envoi payé pour un verdict E1).

### Moyens

- **m1 — Aveugle : tenu sur clés, ordre, typographie ; non mesuré sur la forme du fond.** Vérifié : les 20 témoins, passés
  par le validateur réel de l'orchestrateur, donnent la même vue que bruts (aucune différence d'espaces de bord, de
  caviardage ni de clés) ; clés et sous-clés dans l'ordre du gabarit ; champs internes et hors gabarit retirés et
  consignés ; ordre tiré par lecture ; aucune pièce servie ne nomme un témoin. Restent, hors de portée de l'outil et non
  mesurés : 18 témoins sur 20 ont une `anteriorite` vide (la question invite les proposeurs à la remplir) ; tous sont
  `approche`, sans saut de ligne, sur un alphabet réduit (aucun ≥, ×, →) ; longueurs 1 460 à 3 622 ; les huit idées au
  hasard ont un nom au même moule. L'outil ne ramène ni les sauts de ligne ni la forme Unicode (NFC). *Proposition* :
  `preparer` écrit au manifeste (jamais envoyé) un tableau de forme par origine (longueur, nombre d'antériorités et de
  questions servies, sauts de ligne, caractères hors de l'alphabet des témoins) : si un trait sépare à lui seul les deux
  origines, c'est une réserve à porter au rapport avant l'envoi, sans lire le fond.
- **m2 — Lacunes des essais (code juste, essais muets).** Sur mes 22 mutations neuves, 9 survivent : passage du catalogue
  cherché dans toutes les entrées au lieu de l'entrée Ck ; occupation acceptée sans passage de la fiche ; L4 jugée sur R7
  seul ; κ au seuil strict ; E5 au seuil large ; comparaisons descriptives unilatérales ; audit de propreté exigeant les
  quatre signes ; typographie du passage tolérée ; étiquette hors lot gardée (sans effet). Les deux premières touchent la
  preuve du § 4.5 : à couvrir par un essai avec M1.
- **m3 — A2 : la lecture prise est la plus indulgente des deux.** Avec une marge constante et l'autre non, κ vaut 0
  (défini) ; l'outil juge alors l'accord brut : un lecteur qui met R7 = 1 partout passe L4 si l'autre fait de même 8 fois sur
  10 (essai S3 : accord 0,82, κ 0 → tient ; à 55 sur 56 dans la même marge, κ 0,15 → manque). La parenthèse du texte
  (« une marge constante ») porte cette lecture : défendable, dite. À dire aussi : la discontinuité, et que la lecture
  littérale (accord brut seulement quand κ n'a pas de valeur) ferait manquer L4.
- **m4 — A6 et l'exactitude du lecteur cachent le brut.** L2, L4 et l'exactitude sont jugées sur les valeurs prouvées
  (conforme au § 4.5 : un 1 non prouvé « compte 0 »). Une fausse fiche acceptée par le lecteur avec une citation fausse
  passe L2 sans trace dans le détail de L2. À ajouter au détail : la valeur brute, à côté de la valeur comptée.
- **m5 — A7 : « lisibilité parfaite » est codée « lisible et L5 rejetée »**, non dit dans `PRECISIONS` : l'audit se déclenche
  donc à chaque désignation. Prudent, défendable ; à écrire.

### Mineurs

- Aucun des deux programmes ne vérifie sa propre empreinte ; la mère vérifie `59e665af…` et `f91962f3…` avant chaque geste.
- Bornes : 6 appels et 4 USD par construction (refus au-delà ; `max_tokens` ≥ 16 384), formule égale à celle du relais
  ((octets + 1 024) × 2 + `max_tokens` × 10, par million) ; la borne **effective** est celle du relais
  (`--plafond-usd 4 --max-appels 6`), à lancer neuf pour cette lecture. `usage` rendu n'est pas comparé à la borne.
- Un passage de plus de 200 caractères n'est ni refusé ni compté (la consigne dit « au plus 200 »).
- A3 (échappements JSON acceptés), A4 (hors M2), A5 (bilatérale, (1 + k)/(1 + 100 000)), A8 : défendables, dites.
- Le τ de Kendall du § 4.8 n'est pas écrit : conforme (après le scellement du classement).

## Les six points demandés

1. **Règle** : admissibilité, vue, ordres et graines (`SeedSequence(2026111302).spawn(4)`, enfants 0 à 3 ; 2026111303),
   lots, preuve, valeurs retenues, portes, nouveauté, S, coût, départage, deux désignées sous L1–L4 et L5, témoin à score
   permuté, L1 à L5, Holm, E1 à E5 : conformes. A1 à A7 : tranchées et dites, sauf les conséquences relevées en M1, M2,
   m3, m4, m5.
2. **Aveugle** : oui pour clés, ordre, typographie ; réserve m1 pour longueur et habitudes de fond.
3. **Citations** : exactes à la lettre (casse, ponctuation, champ unique : mutants tués), creuses sans M1.
4. **Aucun modèle, bornes** : aucun import de réseau ni lecture d'environnement ; bornes tenues.
5. **Juge de l'organisme** : jamais lu par le classement ; C5 non gardée par le code (M3).
6. **A1** : ci-dessous.

## A1 — calcul confirmé, et règle de rechange (sans trancher)

**Confirmé.** Les fiches non neuves ont C = 0, le minimum : toute permutation qui laisse les k neuves dans le groupe réel
donne une statistique au moins égale à l'observée, donc p ≥ C(n − k + 8, 8) / C(n + 8, 8), quelles que soient les valeurs
de C et celles des idées au hasard. Pour n = 36 : k = 12 → 0,0593 ; k = 13 → 0,0445 (programme : 0,0595 et 0,0445). Il
faut **13 neuves sur 36**, 11 sur 30, 8 sur 20, 5 sur 10 ; une idée au hasard qui passe monte la barre (une seule à C = 5 :
il faut environ 20 neuves sur 36). Avec une neuve p ≥ 0,82, avec deux p ≥ 0,67 : E4 est inatteignable.
**Le plancher ne vient pas de la statistique** : il vaut pour tout test de permutation entre les deux groupes ; changer la
statistique ne le lève pas. Assouplir le seuil non plus (10 % : 11 neuves ; 20 % : 8) ; ajouter des idées au hasard à peine
(12 au lieu de 8, le plus que permettent 6 appels : 10 neuves ; il en faudrait environ 125 pour désigner sur 2 neuves).
**Donc aucune règle ne désigne « dès qu'il y a de quoi » en gardant une garantie à 5 % contre le hasard : il faut choisir.**

**Règle de rechange proposée (deux étages).** L5 reste, inchangée, le seul test, et porte seule l'énoncé « la règle sépare
l'organisme du hasard ». La désignation en est détachée : sous L1 à L4, les deux premières neuves sont désignées si leur C
dépasse strictement le plus grand C des huit idées au hasard ; elles sont dites « désignées, séparation démontrée » si L5
rejette, « désignées, séparation non démontrée » sinon. E3 devient une mention, E4 redevient atteignable.
**Ce qu'elle coûte.** Si la règle ne mesure que la forme (fiches réelles et idées au hasard échangeables, chacune neuve
avec la même probabilité q), la probabilité de désigner au moins une idée à tort passe de 5 % au plus à **56 % au pire**
(q ≈ 0,05 ; 28 % à q = 0,01 ; 42 % à q = 0,10 ; 17 % à q = 0,20), et jusqu'à 82 % sans ex aequo (36/44). Par fiche, la
garantie tombe à 1/9 (une fiche échangeable avec les huit idées au hasard les dépasse toutes une fois sur neuf au plus).
Une fausse désignation ne porte aucune revendication (§ 6 : aucune ne s'appuie sur les désignées) : elle coûte le devis de
l'essai du § 9, où le témoin à score permuté et l'organisme inchangé la rattrapent. Garder la règle telle quelle coûte, à
l'inverse, de ne rien désigner tant que moins d'un tiers des fiches sont neuves, quelle que soit leur qualité.

## Essais et mutations rejoués

- Essais de l'auteur rejoués à 00:05 UTC : **47 passés** (comme annoncé).
- Mes sondes (S1 à S6) : passages triviaux ; plancher de L5 par énumération et par le programme ; κ à marge constante ;
  mauvaise liste donnée à `--fiches` ; lot illisible ; préambule avant le JSON (accepté s'il y a un bloc, illisible sinon).
- Mes mutations, neuves (aucune du banc de l'auteur), 00:07 à 00:09 UTC : **22 jouées, 13 tuées, 9 survivantes** (m2).
  Tuées : casse ignorée ; R4 par programme inversé ; réserve à 40 USD ; valeur p stricte ; coût non permuté dans le
  témoin ; S croissant ; départage ignoré ; L1 exigeant les deux lectures ; groupe du hasard élargi à tous les témoins ;
  trois désignées ; L3 sur une seule lecture ; L2 sur la valeur brute ; graine du test changée.
