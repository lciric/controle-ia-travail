# Contre-lecture de la note sur le juge v2, des critères de choix v2 et des deux rejeux à blanc — v1

- **Contre-lecteur** : modèle O, neuf. Je n'ai écrit aucune des quatre pièces, ni aucune carte (règle R2). Écrit le 2026-11-19 (`date -u` : 2026-11-19T14:18:12Z). Hors ligne, processeur seul, aucune dépense, aucun appel de modèle.
- **Pièces contre-lues**, empreintes recalculées, toutes égales à leur compagnon `.sha256`, et vérifiées par `controle_ia.scellement verifier` :
  - `note-conception-juge-selection-cartes-ecartees-v2.md`, sha256 `2ecdd9d367b70593304f9496349dd6f7c6ab1795322de0a8dca224f670811918` (commit `15de5fbb`, 2026-11-19T13:56:07Z) ;
  - `criteres-choix-cartes-v9-v2.md`, sha256 `4ae09b15e2816fcda0ba0ba008ca11b58906d7712351253d04f52214e9a629c1` (commit `14e9954d`, 2026-11-19T13:53:31Z ; le contenu de ce commit a la même empreinte, et aucun commit ultérieur ne touche ce fichier) ;
  - `rejeu-a-blanc-criteres-v2-lecteur-f-v1.md`, sha256 `5d8d537aac4fb0c8ead3de24d4f04291ba7b31ff2a3fc1c5395f6bf4962e14c2` (commit `d44b51b3`), et ses sélections `selections-rejeu-a-blanc-criteres-v2-lecteur-f-v1.json`, sha256 `e42b5f05d0f9b2c8423fc0d005e5d5c414c1023208e049201074ecf91ec69fc6` (commit `3543a767`) ;
  - `rejeu-a-blanc-criteres-v2-lecteur-o-v1.md`, sha256 `209243b73e34c0aaac5ca2b1ef77c972d855eb09804db7d4f01390d16b13674f` (commit `f4091993`), et ses sélections `selections-rejeu-a-blanc-criteres-v2-lecteur-o-v1.json`, sha256 `8bd435b98f1b81abf3a4e201977b2b1bf9a72cbe464dfb9127243d1a93e0b7d3` (commit `e487939e`).
- **Lus en plus** : la note v1 (`3b0332a1…`) et sa contre-lecture (`6214b44d56c6cb8dd4221be09ff2fd5c4f50c07f36fb352501544f315d3fd2ba`) ; sur `main` (commit `8379ba96`), les critères v1 (`8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326`), § 2, et `registres/go.md` (copie sha256 `72e52540c4b25997d0aa6057ea880bdc765e0cd09c5650b65a0b084da174f558`), lignes GO-2026-11-19-55 à -72. Les cartes (`fiches.json`, sha256 `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`) ont été lues par programme, le seul champ `contenu`, le champ `meta` jamais lu ni affiché, pour quatre cartes en désaccord : `fd81c25c080e8`, `fcd56a5ce3c1c`, puis les raisons des deux lecteurs sur `fc1f059e8873e`, `f0d21fb62aff2`, `fe0ce53be28b3`.
- **Non lus** : aucun verdict de juge, le classement, le coffre, le champ de l'espèce. Les seules espèces citées ici sont celles que les lignes GO-57, -59, -61 et -63 donnent en toutes lettres (44 cartes), comme le rejeu F l'a fait.
- **Comptes refaits par programme** (bloc-notes de la session, non versés) : identifiants des lignes GO, accord entre lecteurs, recoupement, assemblage des deux lectures.

## Constats

### Sur la note v2

**Les douze constats de la contre-lecture v1 sont appliqués.** Vérifié un à un contre le tableau du § 8 : phrase du constat 1 reprise au § 1 et mécanismes au § 3 ; « neuf lignes retenues par GO-55 et -56 » ; ligne de `de7ed04d…` refaite avec l'erratum `9326ffa2…` et la sortie `d9360b31…` ; matrice « en partie confondue », deux sorties citées, déjà connu déclaré ; collège à coût apparié contre un juge seul répété k fois et le collège à deux ; interaction dans les deux sens sous multiplicité ; N-053 « esprit, non lettre » et N-059, point 14 ; N-045, points 1, 2 et 4 en toutes lettres ; lecteurs Opus et Fable déclarés de la même famille ; limite hors échantillon ; en-tête, GO-59, masque imparfait, récusation par programme ; ce que l'option donne au juge. R-3845 est renvoyé au rapport à la mère, ce que le constat 1 permettait.

**1. Moyen — le tableau du veto (§ 5) a deux comptes faux.**
- « Avec un collège de cinq, deux suffisent (10 sur 94) et trois (15) dépasseraient le nombre visé par défaut, neuf lignes » : 10 dépasse aussi neuf.
- Les critères v2 (§ 7) font des deux lecteurs des titulaires **toujours**. Un collège de cinq juges donne donc sept titulaires, non cinq : à deux cartes, 14 au plus (15 %), et 12 au plus pour une lignée (six titulaires hors de sa lignée) ; à trois cartes, 21 et 18. Le § 5, le § 9 option (a) (« 10 avec un collège de cinq ») et option (c) (« 15 », « jusqu'à 12 ») sont à refaire sur sept titulaires, ou les critères doivent retirer le veto des lecteurs quand les juges en ont un.

**2. Moyen — le veto tenu par les lecteurs n'est pas dans les confirmations.** Le mot de Lazar est « deux ou trois cartes veto **par juge** ». Sans dépense, les critères le donnent aux deux lecteurs. Le § 9 le dit (« ce sont les deux lecteurs […] qui tiennent le veto »), mais la liste « À confirmer » (critères v2, § 11 ; note, § 9) ne le porte pas. C'est un écart à la lettre de GO-2026-11-19-68, point 4 : à ajouter aux confirmations demandées.

**3. Moyen — GO-2026-11-19-69 a répondu à la confirmation 1, après le scellement.** GO-69 (vers 13:54Z, R-3856) : « Le coût reste écrit à côté de la note ; il n'élimine aucune carte et ne sert qu'à ordonner le passage. Il ne sort pas entièrement des critères. » Les critères v2 (§ 0 et § 6) tiennent la substance : le coût n'élimine rien et sert à l'ordre de passage, après l'amélioration attendue (GO-60). Mais le § 9 de la note (« le coût sort de la note pour toutes les cartes, au-delà de la lettre de GO-60 ») et le § 11, point 1, des critères demandent encore ce qui est tranché. Il faut le dire dans la soumission, et rendre obligatoire, dans toute proposition, le rapport de coût du § 6 à côté de la note. Les deux rejeux l'ont omis, et le déclarent.

**4. Majeur — la fiche de décision (§ 5 et § 9) a été écrite avant les rejeux, et ceux-ci changent ce qu'elle doit dire.** Les deux rejeux montrent, chacun sur sa lecture :
- que la règle ne range plus : tout passe le plancher (92 sur 92 cartes notées chez F ; 94 sur 94, en variante A, chez O) ;
- que le nombre visé est tiré au sort entre ex æquo (28 cartes à égalité chez F, de 66 à 90 chez O) ;
- que le lot tiré au sort, censé servir de bras témoin, ne se distingue plus du nombre visé : la comparaison de la mesure 3 entre « règle » et « tirage » perd son objet ;
- que le veto devient la seule entrée **par contenu** dans la liste proposée en premier. « Contre l'élimination » ne protège plus rien, puisque rien n'est éliminé hors exclusions, et le veto ne lève aucune exclusion.

Rien de cela n'est contraire à N-058 : l'épreuve tranche, et la règle ne fait que proposer. Mais Lazar choisirait la limite du veto sans savoir que le veto, et non la note, fera l'essentiel du choix en premier. **Correction** : une version 3 de la note, ou un ajout scellé, qui porte ces faits dans l'enjeu et les options. Il faut y dire aussi que, sous la limite de charge de GO-2026-11-19-67, le choix effectif se reporte sur l'ordre de passage : « amélioration attendue » d'abord (GO-60, notion définie par un lecteur), puis le coût (GO-69). C'est là que la sévérité peut revenir, et c'est là qu'il faut la compter par espèce après coup, dans les deux sens (règle R4).

### Sur les critères v2

**Scellés avant toute lecture de carte : vérifié par l'historique.** Ordre des commits sur `lot/compte-organisme-v1` : critères `14e9954d` (13:53:31Z), note v2 `15de5fbb` (13:56:07Z), sélections F `3543a767` (14:03:55Z), note F `d44b51b3` (14:06:54Z), sélections O `e487939e` (14:08:07Z), note O `f4091993` (14:11:40Z). Les critères ne contiennent aucun identifiant de carte. Les heures de première ouverture des cartes (F : après 13:56:51Z ; O : 13:57:59Z) sont des déclarations ; l'historique prouve seulement que les critères étaient versés avant toute sélection. Le rédacteur connaissait les écarts de la v1 par la proposition et sa contre-lecture : c'est déclaré (« Limite dite d'avance »).

**Ils tiennent les gardes demandées.** Quotas par strate, définis par le contenu, « jamais par l'espèce » (§ 5). Aucune espèce lue par un lecteur ; le filtre de lignée du veto et le compte du § 10 sont faits par programme, après le dépôt. Le coût n'élimine rien et sert à l'ordre de passage, ce qui va au-delà de GO-60, est déclaré, et est confirmé depuis par GO-69 (constat 3). Le veto ne fait rien adopter, ne s'exerce jamais contre une carte, et son taux de réussite ne sert ni à choisir ni à pondérer (N-058 ; N-059, point 14). Le principe de Lazar, « ce sont les essais avec experiences qui doivent trancher in fine », est en tête (§ 0).

**5. Majeur — le critère D a perdu la précision du critère C5 de la v1, et les deux lecteurs l'ont lu différemment.** Le C5 de la v1 dit : « une décision de conception nommée de l'organisme (**garder, retirer ou régler un module**) ». Le D des critères v2 (§ 4.3) renvoie au C5 de la v1 mais omet cette parenthèse.
- Le lecteur O lit la lettre de la v1 : D = 2 pour toutes les cartes.
- Le lecteur F met D = 1 à 62 cartes dont le « non » « n'apprend que l'abandon ». Or l'abandon est « retirer un module ». J'ai vérifié sur `fd81c25c080e8` (« Retenir uniquement si […] ; sinon couper ») et `fcd56a5ce3c1c` (« conserver le mécanisme seulement si […]. Sinon, couper ») : le « non » y commande une décision nommée.

La lecture de F est donc un écart à la lettre, qu'il dit lui-même possiblement lié à la manière d'écrire.

Conséquence, recalculée par programme sur les deux sélections scellées :
- assemblées selon la lettre (somme des notes ; plancher dès qu'un lecteur l'accorde ; exclusion si les deux la voient), les deux lectures donnent 28 cartes à 12, 60 à 11, 2 à 10 et 2 à 9 ;
- **tout l'écart entre 12 et 11 vient du D de F** ; E et Q ne diffèrent que sur deux cartes ;
- parmi les 28 cartes à 12, aucune de celles que les lignes GO attribuent à Astra (12 cartes), à Argon (16) ou à Opus (3), une de Carbon (sur 10), deux de Fable (sur 3) et 25 sans espèce donnée.

Le nombre visé de l'assemblage tirerait donc ses neuf lignes parmi ces 28. La sévérité nommée par Lazar reviendrait par le rang, à travers l'écart d'un seul lecteur. C'est un déclencheur de la règle R4.

**Correction** : la règle v2 est scellée et ne se change pas (§ 0 des critères). Il faut écrire l'écart dans toute proposition qui l'emploierait, et ne pas assembler les deux rejeux tels quels. La parenthèse du C5 de la v1 est à rétablir dans des critères v3, scellés avant l'ouverture des cartes de la course suivante. Ce n'est pas un réglage visant à faire entrer une espèce (règle R3) : c'est le retour à la lettre que la v2 cite.

**6. Moyen — le tirage n'est pas reproductible tel qu'il est écrit.** Les § 8 et 9, point 7, disent « graine dérivée par `numpy.random.SeedSequence` de l'empreinte de ce fichier scellé et de l'identifiant de la course », sans fixer l'identifiant, la formule de combinaison, l'ordre du vivier, ni l'enfant de la graine qui sert à quoi. Les deux lecteurs ont construit deux graines différentes (F : `entropy` = empreinte, `spawn_key` = huit premiers chiffres de l'empreinte de l'identifiant ; O : liste des deux empreintes entières, `spawn(2)`), sur le même identifiant choisi par chacun, le nom du dossier d'archive. Le nombre visé étant décidé par le tirage (constat 4), la construction doit être fixée par écrit : identifiant, formule, vivier trié par identifiant comme ordre canonique et non comme critère, enfants. Cela se fait dans le programme d'assemblage de la mère, scellé avant usage, ou dans des critères v3.

**7. Moyen — l'exclusion X1 et GO-2026-11-19-63, point 1.** Les deux lecteurs voient chacun X1 non séparable sur `fefca0bd94064`. Les critères v2 (§ 2) l'écarteraient donc. GO-63, point 1, a gardé cette carte « avec cet avis seulement descriptif » et fixé : « si le rédacteur ne peut pas séparer la mesure de la décision, retour à Lazar ». Le précédent vaut pour la v9 ; pour les courses suivantes, il faut demander à Lazar, dans les confirmations, si une carte X1 non séparable est écartée (lettre de la v2) ou lui revient (GO-63). Le lecteur O voit aussi X1 sur `fa38f9faa24e0`, gardée par GO-57 et GO-63 ; F ne le voit pas. À la lettre, la carte reste, avec la réserve.

**8. Mineur — la question (c) devient le fourre-tout que la note craignait pour la voie N.** Le lecteur O range 46 cartes en (c), le lecteur F 25. Seize des 23 désaccords de voie ou de sous-strate sont des cartes que F met en voie N et O en (c) : tests de mort, réimplémentations, interprète. O suit la contre-lecture `a923cb57…`, qui lisait l'interprète comme « règle de survie des fiches ». Pour la question (a), O applique la lettre de la v1 (un registre hérité **d'une course**, comparé au même registre né vide et à aucun) et n'y met aucune carte ; F y met quatre cartes « archive servie ou factice ». La règle de double candidature (§ 3) absorbe ces désaccords. Mais avec le plafond de deux lignes par question, 46 cartes de (c) se disputent deux places. Des critères v3 gagneraient à écrire la lettre des cinq questions en toutes lettres, au lieu de « (a) l'héritage ».

### Sur les deux rejeux

**Ils appliquent les critères à la lettre, aux écarts déclarés près.** Un lecteur chacun, par mandat ; note sur 6 ; aucune fusion ; X6 non appliqué ; filtre de lignée du veto non appliqué ; rapport de coût et de collision du § 6 non fait ; part par espèce du § 10 non calculée par programme. Tout cela est dit par chacun. Un écart n'est pas déclaré comme écart : le D du lecteur F (constat 5), qu'il signale seulement comme lecture possiblement liée au style. Le lecteur O fait deux variantes d'exclusion, dont la variante A est la lettre pour un lecteur seul : c'est juste.

**9. Moyen — rejeu O : un compte faux dans le verdict, et « non gardées » pour « non nommées ».**
- Verdict, point 2 : « La règle propose en premier 7 cartes que Lazar n'a pas gardées ». Sur les sélections scellées (variante A), les 15 cartes proposées en premier comptent 6 cartes nommées gardées, 1 nommée non gardée (`fbac0bab50a65`) et 8 non nommées : 9 hors des cartes nommées gardées. Le § 4 donne bien ces neuf ; le verdict est à corriger.
- Le § 4 et le verdict traitent les cartes non nommées comme « non gardées » (« Gardées en plus par les critères v2 » ; « 35 autres cartes non gardées par Lazar » ; « dont 50 gardées » dans le calcul du hasard). Or GO-61 garde « toutes les cartes d'Astra (20 sur 20) », dont 12 seulement sont nommées. GO-55, -56 et -59 gardent aussi des « fusionnées » et une liste « les plus originales » sans identifiant. Il faut écrire « non nommées », et dire que 50 est un plancher, comme le fait le rejeu F. Le constat « au niveau du hasard » n'en change pas de sens.
- **Correction** : erratum au rejeu O.

**10. Mineur — rejeu F : espèces comptées par un lecteur, et indépendance non écrite.**
- Le compte par espèce du § 5, point 3, est fait par le lecteur à partir des lignes GO, après le scellement, non par programme (§ 10 des critères). Je l'ai refait et il est exact : Astra 12, Argon 16, Carbon 10, Opus 3, Fable 3 ; D = 2 pour une carte de Carbon et deux de Fable, aucune autre ; dans le nombre visé, Carbon 1 et Fable 1 ; Astra n'entre que par le lot (`f19c4c823d67c`).
- Ces espèces viennent des listes de la mère : c'est à dire.
- Le rejeu F ne dit pas en toutes lettres que son lecteur n'a écrit ni les critères ni une carte (critères v2, § 1), alors que les critères ont été écrits par un rédacteur modèle F. À écrire, ou à faire écrire par la mère.

**11. Mineur — désaccords de lecture sans effet sur le plancher.** Le lecteur O met E = 1 à `fcd56a5ce3c1c` (« aucune base bon marché »), alors que la carte compare à une « troncature mécanique de commentaires de même longueur », que F lit comme la base. Le lecteur F met Q = 1 à `fc1f059e8873e` (« instrument d'une seule ligne ») ; O met 2 (« sert […] toute ligne qui change ce qui est servi entre générations »). Les deux lectures se défendent. La règle les liste comme désaccords ; aucun n'atteint deux points.

**12. Mineur — indépendance des deux lectures et veto par famille, à décrire.**
- Les sélections O (`e487939e`, 14:08:07Z) sont versées après la note F (`d44b51b3`, 14:06:54Z). O déclare ne pas l'avoir ouverte ; l'historique ne peut pas le prouver.
- Sur les six cartes de veto des deux rejeux, les deux seules dont les lignes GO donnent l'espèce sont de la famille des lecteurs : `f76714f1ddda4` (Fable) et `f562951db6c70` (Opus), toutes deux chez O. Le filtre de lignée retirerait la seconde si le lecteur O est de la lignée Opus ; la première reste, « comptée à part ». F dit croire ses trois veto de sa propre famille.
- C'est un petit nombre, une description et non une mesure. Mais il va dans le sens de la ligne « capture par une famille » du tableau du § 5 : avec deux titulaires de la même famille, le seul remède réel est un titulaire d'une autre famille, sur devis.

## Accord entre lecteurs

Sur les 92 cartes que F note (94 moins ses deux exclusions) ; comptes refaits par programme sur les deux sélections scellées.

| objet | accord | détail |
|---|---|---|
| exclusions (94 cartes) | 93 sur 94 | communes : `fafa0062508c9`, `fefca0bd94064` (X1) ; O seul : `fa38f9faa24e0` (X1) |
| voie | 74 sur 92 (80 %), kappa 0,67 | 17 cartes en N chez F : 16 en P (c) et 1 en P (b) chez O ; 1 en N chez F, en I chez O |
| voie et sous-strate | 69 sur 92 (75 %), kappa 0,67 | en plus : 4 cartes en P (a) chez F, en P (c) chez O ; 1 en P (d) chez F, en P (c) chez O |
| E | 91 sur 92 | `fcd56a5ce3c1c` : F 2, O 1 |
| Q | 91 sur 92 | `fc1f059e8873e` : F 1, O 2 |
| D | 30 sur 92 (33 %), kappa 0 | 62 cartes : F 1, O 2 ; aucune dans l'autre sens ; O met 2 partout |
| total identique | 30 sur 92 | (6, 6) : 28 ; (5, 5) : 2 ; (5, 6) : 60 ; (4, 5) : 2 |
| écarts de deux points | 0 | |
| plancher | 92 sur 92 | toutes au plancher chez les deux |
| nombre visé | 1 sur 9 | `f7219bb36cfcb` ; attendu d'un tirage entre ex æquo |
| veto (trois cartes) | 0 sur 3 | listes de cinq, suppléantes comprises : 3 en commun (`fed7a993d9671`, `f562951db6c70`, `f6e7646851ba5`) ; le premier veto de F (`f51c0935052f6`) est dans le nombre visé de O, et le premier de O (`f76714f1ddda4`) dans celui de F |
| lot tiré au sort | 1 sur 3 | `f17603c39bc32` ; graines différentes (constat 6) |
| proposées en premier (15 chacun) | 4 en commun | `f17603c39bc32`, `f51c0935052f6`, `f7219bb36cfcb`, `f76714f1ddda4` |

Lecture : les deux lecteurs s'accordent sur ce qui est mesurable par le texte (E, Q, exclusions) et en bonne part sur la voie. Ils divergent entièrement sur D, le seul critère qui varie. L'accord de deux lecteurs d'une même famille ne vaut pas deux regards indépendants (critères v2, § 1) ; ici, il ne fait même pas varier le rang, sauf par l'écart de l'un d'eux.

## Recoupement avec les cartes gardées par Lazar

Recompté par programme sur les lignes GO-55, -56, -57, -59, -61 et -63 :
- 50 cartes nommées gardées (trois dans deux lignes : `f89c771e3ac68`, `f7782e931911d`, `fa38f9faa24e0`) et 4 nommées non gardées (GO-63, point 2) ;
- 50 est un plancher, puisque GO-61 garde les 20 cartes d'Astra et que 12 seulement sont nommées.

| | nombre visé | veto | lot | proposées en premier | gardées par note |
|---|---|---|---|---|---|
| rejeu F | 3 sur 9 | 2 sur 3 | 3 sur 3 | 8 sur 15 ; 7 non nommées ; 0 nommée non gardée | 11 à 6, 36 à 5, 2 à 4, 1 exclue (`fefca0bd94064`) |
| rejeu O (A) | 3 sur 9 | 2 sur 3 | 1 sur 3 | 6 sur 15 ; 8 non nommées ; 1 nommée non gardée (`fbac0bab50a65`) | 47 à 6, 3 à 5 |

- Rejeu F : tous les comptes du § 4 sont exacts.
- Rejeu O : le § 4 est exact, sauf le libellé « non gardées » ; le verdict, point 2, ne l'est pas (constat 9).
- Les quatre cartes nommées non gardées passent le plancher chez les deux lecteurs, à 5 chez F et à 6 chez O : la règle ne sépare pas ce que Lazar a gardé de ce qu'il a écarté. Les deux rejeux le disent.

## Verdict

Scellable après corrections.

Le dessein tient. Les critères v2 sont scellés et versés avant toute sélection, tiennent les quotas par strate jamais par espèce, ne lisent aucune espèce, et respectent N-058 : la règle, les lecteurs et le veto proposent, l'épreuve tranche. La comparaison du veto à deux et à trois cartes est faite sous N-058. Les douze constats de la contre-lecture v1 sont appliqués.

À corriger, sans réécrire les pièces scellées (règle R12) :
- **note v3 ou ajout scellé** : le tableau du veto sur sept titulaires (constat 1) ; le veto des lecteurs à porter aux confirmations (constat 2) ; GO-69 intégré (constat 3) ; surtout les faits des rejeux dans la fiche de décision (constat 4). Le rang ne choisit plus, le lot ne se distingue plus du nombre visé, le veto fait le choix en premier, et la sévérité peut revenir par l'ordre de passage.
- **Critères v3**, scellés avant l'ouverture des cartes de la course suivante, et non calés sur la v9 : la parenthèse du C5 de la v1 rétablie dans D (constat 5) ; la construction du tirage fixée (constat 6) ; la lettre des cinq questions écrite en entier (constat 8). Sont à demander à Lazar : X1 non séparable, écartée ou à lui rendue (constat 7), et le veto tenu par les lecteurs (constat 2). En attendant, n'assembler les deux rejeux qu'avec l'écart du D de F écrit en tête.
- **Erratum au rejeu O** : le compte du verdict (9, non 7) et « non nommées » pour « non gardées » (constat 9). **Rejeu F** : préciser l'origine des espèces et l'indépendance du lecteur (constat 10).
