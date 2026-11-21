# Avis d'Opus 5.5 en effort maximal : le mode tenu à l'écart décide-t-il la porte G1 ? (v1)

- Classe C (travail). Avis indépendant pour la mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`), sur la question de Lazar inscrite en GO-2026-11-21-64 (« que dit opus max dessus ? »). La session de l'attaquant informé appelle ce conflit « nœud 6 (ii) ». Aucune dépense, aucun commit.
- **Commande refusée par le classifieur, déclarée.** Une commande de cette session a été refusée par le classifieur du mode automatique, motif « [Undermining Oversight] ». Elle devait vérifier le sceau de `prereg/bras-attaque-regle-v1.md` et chercher les numéros de ligne du nœud 6 de cette règle. Heure : non relevée au moment du refus ; borne haute selon l'horloge de ce conteneur : 2026-11-21T16:14:57Z (`date -u` relevé après le refus, avant l'écriture de cette note). La commande n'a pas tourné et n'a pas été retentée. Arrêt au premier refus ; avis provisoire remis à la mère ; cette note est écrite et scellée telle quelle, sur son ordre.
- **La règle du bras d'attaque n'a pas été lue** : ni `prereg/bras-attaque-regle-v1.md` (ni son nœud 6 (ii)), ni ses additifs. Aucun fichier du coffre, rien qui décrit un mode.
- **Limite** : le brouillon 6 du préenregistrement de G1 (`brouillons/G1-preenregistrement-v1-brouillon6.md`, compagnon vérifié) n'a pas été relu ; son contenu est pris de la ligne R-1581 du registre des décisions.
- **Horloge** : `date -u` lit 16:14:57Z, alors que le mandat lu se dit rédigé « vers 16:40 UTC » et que la passation lue porte 16:45 dans son nom. Écart non résolu ici.

## Pièces lues (empreintes relevées à l'écriture)

- Décisions : `docs/decisions/decision-N-054-v1.md` (`c8a00b3f…`), `decision-N-056-v1.md` (`3592c1e9…`), `decision-N-062-v1.md` (`63f42690…`), compagnons vérifiés.
- `docs/programme-controle-ia-v2.md` (`2fd63bad…`) : H1 l. 93, porte G1 l. 190, bascule l. 238.
- `docs/brief-claude-code-programme-complet-v2.md` (`9261932a…`) : porte G1, l. 241-246.
- `registres/go.md` (`c8d88f43…`, registre vivant) : lignes contenant « tenu à l'écart » ou « G1 », lues en entier (l. 14, 45, 101, 140, 143, 162, 195, 196, 255, 359, 408, 409, 412, 413, 420, 425, 522, 588, 590, 596, 602 à 605, 609, 663).
- `registres/decisions.md` (`2ddece5c…`, registre vivant) : aucune ligne « nœud 6 » dans les 1 500 dernières ; lues en entier : l. 821 (N-056), 826 (R-600), 1530 (R-1572), 1539 (R-1581).
- Canal `canal/conv-audit-n04` (commit `adc1be82…`) : `brouillons/G1-decisions-en-clair-v1.md` (`48eb66bc…`, égal à son compagnon), l. 1-10, 16-17, 24-27.
- Branche `claude/loving-lamport-7ol5ws` (commit `271fb4d2…`) : `docs/procedures/mandat-scellement-2-familles-aveugles-v1.md` (`8594376e…`), l. 1-8 et 25-40 ; `registres/passations/2026-11-21-1645-attaquant-informe-fille-reprise-et-mandat-scellement-2.md` (`f8487d8e…`), en entier.

## 1. Le conflit, pièce par pièce

Mandat, l. 34-35 : « **Nœud 6 (ii), conflit déjà ouvert.** Le mode tenu à l'écart décide-t-il la porte G1 (N-056 contre le brouillon 6 de G1) ? Le nombre de familles à écrire en dépend. »

- **Le mode tenu à l'écart et la portée de H1** (N-054), `decision-N-054-v1.md` l. 40-41 : un mode « **scellé avant G1** (empreinte au registre) et **révélé seulement à l'évaluation** » ; l. 49-51 : « la revendication de H1 est restreinte au mode « coût » si la borne basse du gain blanc-sur-noir n'est pas au-dessus de zéro dans les autres modes ».
- **La règle de H1 entre modes, option (a)** (N-056 point 4, D-S29), `decision-N-056-v1.md` l. 55-57 : « (« dans chacun des autres modes, mode tenu à l'écart compris ») : nœud de porte, fixé au préenregistrement de G1 ; conséquence : le mode tenu à l'écart doit être dimensionné comme les autres modes ». Mot de Lazar, l. 22-23 : « dans chacun des autres modes, mode tenu à l'écart compris ». Confirmée le 28 octobre : `registres/decisions.md` l. 826 (R-600 : « D-S29 (a) confirmés »).
- **Les modes où exiger le gain** (DG1-6), `brouillons/G1-decisions-en-clair-v1.md` l. 16. Trois options :
  - (a) « trois modes entiers » ;
  - (b) « modes « contrôles affaiblis » et « tenu à l'écart », partie « diffuse et floue » ; mode « coût » rapporté (fidèle à ta lettre de D-S29 […]) » ;
  - (c) « trois modes, partie « diffuse » seule ».

  La recommandation est (b), et les treize décisions ont été prises aux valeurs recommandées (`registres/go.md` l. 255, GO-2026-11-05-07). **Les trois options comptent le mode tenu à l'écart.** Une ambiguïté de lettre est sans effet ici : « valeurs inscrites » est défini l. 7 comme l'accord aux treize recommandations, alors que la ligne DG1-6 porte « valeur inscrite : (a) jusqu'à ton mot ».
- **Le brouillon 6 de G1, d'après le registre**, `registres/decisions.md` l. 1539 (R-1581) : « deux modes jugés, M = 2, S28 ajouté : mode tenu à l'écart sans famille floue → G1 non lancée, nœud ». Le nœud consigné : « `CLAUDE.md` dit « gain de H1 exigé dans chaque mode » (N-056), contraire à DG1-6 (b) ». **Ce conflit porte sur le mode « coût »** (et sur la restriction à la partie diffuse et floue), **non sur la place du mode tenu à l'écart dans la décision**. Le résumé de `CLAUDE.md` dit « chaque mode » ; la lettre de Lazar dit « chacun des autres modes ».
- **La reconception après un échec de G1** (N-062), `decision-N-062-v1.md` :
  - l. 23 : « Chaque lecture décisive consomme une famille tenue à l'écart […] une fois lu, il est vu et ne sert plus de juge final » ;
  - l. 24 : gardes (a) « une famille tenue à l'écart neuve et à usage unique par lecture » et (b) « aucune sélection sur le tenu à l'écart » ;
  - l. 26 : « La revendication finale (H1a) ne se fait que sur une famille jamais utilisée dans aucune reconception, au critère de G1 ».
- **La réserve des épisodes**, `registres/go.md` l. 609 (GO-2026-11-21-10) : « épisodes du mode tenu à l'écart réservés à G1 et à H1 NON lus ».

**Constat** : aucune pièce lue ne dit que le mode tenu à l'écart est seulement rapporté à G1. Si un texte le dit, il est dans le brouillon 6 (non relu) ou dans le nœud 6 (ii) de la règle du bras (non lu).

## 2. Les trois lectures

**(a) Le mode tenu à l'écart décide G1** : la porte exige le gain dans les modes « contrôles » et « tenu à l'écart » ; le mode « coût » est rapporté (DG1-6 (b)).
- **Ce qu'elle protège.**
  - Elle protège contre le surajustement des moniteurs aux modes vus à leur conception : c'est l'objet de N-054 point 3.
  - Elle donne son effet à la garde (a) de N-062 point 4 contre R3 : sans borne de cycles, c'est l'épreuve fraîche et décisive qui empêche de courir jusqu'au signe.
  - La revendication H1a se fait dans le même geste (N-062 point 6).
  - Elle s'accorde avec l'universalité mesurée sur des familles inédites (N-044, résumé de `CLAUDE.md`).
- **Ce qu'elle coûte.**
  - Une banque d'épisodes à pleine puissance par cycle : dimensionnement comme les autres modes (N-056 point 4), soit « 288 à 400 unités par mode » (`G1-decisions-en-clair-v1.md` l. 5).
  - La puissance d'une exigence sur deux modes à la fois : au plus p, environ p² si les deux modes sont indépendants.
  - Un risque de validité propre au mode aveugle (mode trop visible dans le texte, ou sans partie floue), que S28 traite en amont.
- **Calendrier.** Rien avant l'entretien : le texte et la vérité du dommage se conçoivent sans dépense (mandat l. 36-37) ; la banque passe sur devis et GO quand G1 approche.
- **Cohérence avec N-062.** Entière : c'est la lecture que N-062 suppose (« juge final »).

**(b) Le mode tenu à l'écart est seulement rapporté** : G1 est jugée sur le seul mode « contrôles ».
- **Ce qu'elle protège.** La puissance (un mode au lieu de deux), le budget de chaque cycle, et les chances de franchir.
- **Ce qu'elle coûte.**
  - G1 serait jugée sur un mode vu par les concepteurs. Les cycles sans borne se règlent sur les modes vus (N-062 point 4 (b)) : la porte serait décidée par les modes mêmes sur lesquels on reconçoit. R3 est menacée et la multiplicité n'est pas contrôlée.
  - Elle contredit N-054 points 3 et 4, N-056 point 4, DG1-6 (b) et N-062 points 3 et 6.
  - H1a ne se revendique de toute façon qu'au critère de G1, sur une famille jamais utilisée (N-062 point 6) : on paierait la banque plus tard sans gagner la porte plus tôt.
- **Nature.** Modification d'un critère de porte et d'une revendication : nœud de Lazar, sans défaut.

**(c) Le mode tenu à l'écart décide sous condition.**
- **Quand elle est légitime.** Seulement si la condition porte sur la validité, est fixée avant toute lecture et se calcule sans aucun score de moniteur boîte blanche :
  - S28 : le mode a une partie floue, sinon G1 n'est pas lancée ;
  - la vérité du dommage (N-060) ;
  - l'agent assez compétent (DG1-11).
- **Ce qui est exclu.** Une condition qui dépend d'un résultat (« décide s'il est assez puissant une fois lu », « décide si le gain y est ») serait une sélection sur le tenu à l'écart, interdite par N-062 point 4 (b).
- **Rapport avec (a).** Ainsi entendue, (c) est la forme que prend (a) avec S28 : les deux se confondent.

## 3. Recommandation

**Le mode tenu à l'écart décide la porte G1**, sous les seules conditions de validité fixées d'avance : S28 et, au plus, la vérité du dommage et la compétence de l'agent. Le mode « coût » reste rapporté. **Confiance 0,8** : je retiens le brouillon 6 et le nœud 6 (ii) de la règle, non lus.

Conséquences pour le mandat du scellement 2 (« le nombre de familles à écrire en dépend ») :

1. **Ce qu'une lecture consomme.** Une lecture décisive consomme le mode tenu à l'écart entier, avec toutes ses familles (DG1-7 (a) : un mode, unités réparties entre familles). Lire une partie du mode l'expose tout entier.
2. **Combien de modes écrire.** Écrire le mode du cycle 1 et une réserve scellée pour le cycle 2, pour qu'un échec n'attende pas le bras (N-062 point 3 : famille neuve « scellée avant la reconception »). Le mode du cycle qui passe n'a servi à aucune reconception : c'est celui de la revendication H1a, sans famille de plus.
3. **Qui juge le cycle 1.** La course « nouvelles attaques » a aussi un concepteur du mode tenu à l'écart (GO-2026-11-20-57 et -65 ; mandat l. 31-33). Le juge du cycle 1 se désigne donc par une règle scellée avant toute lecture : choisir entre deux modes après en avoir vu quoi que ce soit serait une sélection.

**Ajout d'expert, hors de la question posée.** N-062 ôte la borne de cycles. Chaque lecture fraîche est valide seule, mais la probabilité qu'au moins un cycle passe à tort croît avec le nombre de cycles. Remède : multiplier le seuil d'e-valeur du cycle k par k(k+1), soit un risque α/(k(k+1)) au cycle k, dont la somme sur tous les cycles vaut α. L'erreur totale reste sous α sans borner les cycles. C'est une modification du critère de porte : nœud de Lazar.

## 4. Nature de la réponse

C'est une **lecture de ce qui est déjà décidé**, non un nœud :
- N-054 points 3 et 4 ;
- N-056 point 4, confirmé par R-600 ;
- DG1-6, accordée par GO-2026-11-05-07 ;
- N-062 points 3 et 6.

Seraient des nœuds de Lazar :
- choisir l'inverse, « seulement rapporté » (modification d'un critère de porte et d'une revendication) ;
- adopter l'ajout sur les cycles.

Restent à Lazar, au scellement du préenregistrement de G1 (N-056 point 4 : « nœud de porte, fixé au préenregistrement de G1 ») :
- la lettre du résumé de `CLAUDE.md` (« chaque mode » devient « chacun des autres modes, coût rapporté »), déjà signalée par R-1581 ;
- la forme de S28.
