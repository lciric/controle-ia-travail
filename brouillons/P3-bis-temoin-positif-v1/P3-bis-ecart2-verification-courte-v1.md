# P3-bis, écart 2 (R-2450) — vérification courte du brouillon 2 de l'addendum 2 — v1

- Vérificateur : sous-agent, **Claude Fable 5.2** (`claude-fable-5-2`), auteur de la contre-lecture
  `brouillons/P3-bis-temoin-positif-v1/P3-bis-ecart2-contre-lecture-v1.md`
  (`742d90fbb8615191b517bed9c4adcc3daaa5caea6cca220f778dae664887a63c`). Ce n'est donc pas un lecteur neuf : c'est le
  contre-lecteur qui vérifie que ses corrections sont appliquées, à la demande de la mère.
- Écrit le 2026-11-12 de 21:52 à 21:53 UTC (heures relevées par `date -u`).
- Demande : message de la mère relayé dans la session ; mêmes interdits et écarts que la consigne `e02d504d…`.
- Pièce vérifiée : `brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-2-telechargement-controle-v1-brouillon2.md`
  (`c23b2eb0beb5de34db4359b9b97624df09c9b076d5ebe3d20c5b74e257ec9444`, recalculée, égale à son compagnon), comparée
  ligne à ligne au brouillon 1 (`7c5e5db2…`) par `diff`.
- Aucune écriture git, aucun appel externe, aucune dépense, aucun chemin interdit ouvert. Le code est lu par
  `git show 07a4b48a:…` (l'extraction détachée de la contre-lecture n'existe plus).

## Verdict

**Scellable.** Aucune correction exigée.

## 1. A1 à A5 : appliquées à la lettre

- **A1** : la section des points laissés au contre-lecteur est retirée ; les dix points sont tranchés à leur place,
  dans le sens de la section 6 de la contre-lecture. Le majorant « une seule fois » est écrit comme une règle (D1), avec
  la lecture des commentaires épinglés (module l. 12-14 et 65-66, surveillance l. 7-8, rapport l. 132, R-2453) et la
  phrase « le code et cet addendum font foi ». La ligne « Contre-lecture (R2) » est à jour, avec l'empreinte juste.
- **A2** : section « Engagement » neuve. Les trois échéances y sont (avant le lancement si la facture est lisible ;
  avant la destruction si la survie de la facture n'est pas sûre ; au plus tard avant le verdict R13), l'inscription au
  registre des dépenses, et « arrêt et nœud de Lazar » en cas de contradiction, décliné selon le moment. Le préalable 2
  et la lecture P9 la reprennent.
- **A3** : le code 4 du lanceur est le premier des trois cas de la condition d'emploi 1, avec le geste de la session.
- **A4** : le risque d'arrêt à tort sur un état terminal vu une seule fois est écrit au risque résiduel, avec le cas
  C2-10 (journal l. 71-73, renvoi exact).
- **A5** : l'éclaircissement est en P6 et au préalable 4, avec `registres/go.md` l. 292 et R-2077 ; « la session le
  vérifie » est remplacé par un constat daté, que la session relit le jour du lancement.

## 2. Suggestions

S1 (multiples de 1 024), S2 (stockage à 0,08 USD de l'heure), S3 (contrôle bloqué), S4 (versement) et S5 (portée de D3,
dans le texte) sont prises. S6 et S7 ne le sont pas. **Le code n'est pas touché** : le commit, les neuf empreintes des
pièces et les dix empreintes des sorties sont ceux du brouillon 1, que la contre-lecture avait recalculés.

## 3. Empreintes et renvois de lignes

- Registres à la tête `5746fc6b1c43d3e967dab7094be23ace6082fa03`, recalculés par `git show` : décisions
  `dc3c921f…`, dépenses `6b8ef731…`, arrêts `254a5464…`, GO `3bef01b5…` : **égales** au brouillon 2.
- Lignes citées à cette tête : dépenses l. 419, 420, 431 (les trois seules lignes sous GO-2026-11-10-02 ; égales à
  celles du commit `6abf5d1f…` ; aucune ligne sous GO-2026-11-02-29) ; arrêts l. 90, 91, 93, 105, 106 ; GO l. 292 ;
  entrées R-2077, R-2393, R-2407, R-2415, R-2431, R-2454 présentes une fois chacune. **Exactes.**
- Renvois neufs au code, à `07a4b48a` : contrôle l. 226 (ligne de `releves.txt`), enchaîneur l. 88 (dossier
  `cinq-minutes`), module d'origine l. 360-367 (sous-commande `identifiant`), destruction l. 30, surveillance d'écart
  l. 140-144, texte l. 1811 et l. 2288. **Exacts.**
- Calcul du stockage de 60286945 : 01:06:28Z à 07:47:20Z font 24 052 s ; 0,08 × 24 052 / 3 600 = 0,5345 USD. **Juste.**

## 4. Le seuil de contradiction de A2

**Acceptable tel qu'il est écrit** (« moins de 0,017 USD ou plus de 1,90 USD »).
- Du côté qui compte pour la garde, le haut : toute unité plus grande que le Kio s'écarte d'un facteur mille ; un
  seuil à dix fois l'attendu la voit sans ambiguïté, et aucun montant honnête sous la lecture retenue ne l'atteint.
- Du côté bas, une lecture plus petite (le kilobit donnerait ≈ 0,02 USD, dans la plage) n'affaiblit pas la garde :
  elle la fait compter trop. La laisser passer « sans autre suite » est sans danger.
- La plage est assez large pour absorber ce qui sépare le relevé de + 294 s de la facture (quelques secondes de
  téléchargement de plus, Ko ou Kio, Go ou Gio, arrondi du loueur).

## 5. Rien d'autre n'a changé

Le `diff` entier a été lu. Tout ce qui diffère du brouillon 1 est dit par la section « Changements », ou en découle
sans toucher une règle. Quatre retouches ne sont pas nommées une à une ; elles sont justes et je ne demande rien :
- « Règle neuve » devient « Règle » (D1, D2) ;
- P9 reçoit les mots « vérifiée à la facture selon l'addendum 2 » (suite de A2) ;
- la condition d'emploi 1 dit que la surveillance d'écart refuse sans la ligne « instance » (vérifié au module) ;
- la condition d'emploi 2 fait arrêter par leur PID l'enchaîneur **et** le processus du contrôle (plus juste que ma
  suggestion S3, qui ne nommait que l'enchaîneur).

Les passages « Ancien » et « Nouveau » de P1 à P8, les lectures de l'addendum 1, la réserve au verdict et les pièces
fixées sont inchangés, hors les ajouts ci-dessus.

## Remarque

La date du rendez-vous citée à la section « Engagement » (2026-11-20T12:00:00Z) est celle du texte (l. 1999-2000). Que
le verdict R13 ne vienne qu'après elle est la lecture du rédacteur ; je ne l'ai pas revérifiée, et l'échéance
« au plus tard avant le verdict R13 » tient sans elle.
