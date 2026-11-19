# Vérification du candidat au scellement v2 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) — v1

- Vérificateur : le même contre-lecteur que pour les brouillons 2, 3 et 4 (Claude Opus 5.5), sous-agent de la session mère. Autre modèle que le rédacteur (Claude Fable 5.2). Écrit le 19 novembre 2026 au soir (UTC), à partir de 23:10Z (horloge du conteneur). Dernière vérification avant le scellement (commit `5e32a8f30`).
- Pièces, sceaux vérifiés, tous égaux à ceux du message de la mère :
  - le candidat v2 : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md` (`088e15ef…`) et son devis `devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md` (`94a628a7…`) ;
  - la table de différence v2 (`c4deb480…`) ;
  - la fabrique `fabrique-candidat-scellement-v2.py`, `sections_candidat_scellement_v2.py` et leur sortie, avec leurs étages v1 et ceux du brouillon 5 ;
  - le brouillon 5 (`6f7e2041…`), sa table (`8be817c6…`) et son devis (`9ba5db06…`) ;
  - l'erratum 1 (`8c3451a2…`) et son contrôle ;
  - le rangement des points (g) (`76e0e27e…`) ;
  - le premier candidat (`54bf29c3…`) ;
  - le rapport v4 du développeur (`b7e22555…`), les fiches v4 (`a88a3a12…`) et v5 (`25a37968…`).
- Mes outils, neufs, dans `outils-verification-candidat-scellement-v2-v1/` (même dossier), scellés :
  - `differences-brouillon4-candidat-v2-v1.py` : tout ce qui sépare le candidat v2 du brouillon 4 vérifié, ligne à ligne, lu en entier, sans se fier à la table. Sa sortie se rejoue à l'identique et n'est pas versée.
  - `rejeu-chaine-candidat-v2-v1.py` et sa sortie : la chaîne du rédacteur, rejouée en mémoire sans lancer sa fabrique, qui écrit.
  - `couples-verification-candidat-v2-v1.py` et sa sortie.
  - `journal-de-verification-candidat-v2-v1.md`.

  Chaque sortie versée est écrite par l'outil d'écriture, puis comparée par programme à la sortie du programme.
- Aucune donnée ni aucun résultat ; aucun nombre de résultat d'expérience close ici. Aucun fichier interdit, rien sous `/root/.claude/`, aucune commande d'arrêt ni de recherche de processus par motif, aucun appel en ligne à l'interpréteur, aucun réseau, aucune dépense, aucun commit.
- Lu dans le code, pour juger le point 5 du message : le format du registre que le code attend (`barreau5_familles/formation_v1.py`, `lire_code_et_accord` ; `engagement_v1.py`, clés, instant, `lignes_du_registre`, `ligne_du_registre`). Ce code est en troisième tour, non figé : je ne le juge pas.

## Verdict

**Scellable après ces couples** : 22 couples exacts, chaque « avant » trouvé une fois par programme ; le validateur du dépôt ne trouve rien à la copie. Aucun constat bloquant.
- Un majeur, **formation** : X-1, le registre propre tel que le code le lit.
- Cinq mineurs : X-2 et X-6 au devis (**formation**) ; X-5, **formation** ; X-3 et X-4, **lecture**.

Appliqués à la lettre et dans l'ordre au candidat v2, ces couples donnent les pièces à sceller :

| pièce | nom définitif | empreinte attendue |
|---|---|---|
| texte | `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` | `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935` |
| devis | `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md` | `dc886195c77b0d67c31cb8815a1e97b9fa72dd35ebac2b8f3bc49d4e5cf59bcc` |

Une application qui ne rend pas ces deux empreintes n'est pas celle-ci.

La colonne de contenu de la ligne `SCELLEMENT-B5F` porte alors exactement : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md ; sha256 bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935 ; membres-apprentissage 3 ; piece famille`. Tout le reste va dans sa colonne de référence (X-1).

Ces couples ne touchent ni la construction, ni les épreuves, ni aucun attendu, pire cas ou coupure du devis.

## Réponses aux points du message

1. **Mes 20 couples : tous présents à l'octet.** 18 sont dans le candidat v2 (13 au texte, 5 au devis) et 2 dans la fiche v5, hors candidat. J'ai rejoué en mémoire la chaîne entière du rédacteur, ses 79 écritures ; elle rend à l'octet le brouillon 5, l'état d'après l'erratum, le premier candidat et le candidat v2, texte et devis. Lu ligne à ligne, ce qui sépare le candidat v2 du brouillon 4 est exactement la suite des écritures que la table de différence énumère.
2. **Les mots de Lazar sont fidèles, conditions comprises, à trois restes près.**
   - Accord de calcul (GO-86), bien écrit : plafond commun de 200 USD, coupures du devis scellé, répétition générale comprise si le code de lecture est prêt. Il ne vaut qu'après `SCELLEMENT-B5F` et `CODE-FORMATION-B5F`, et si le devis ne dépasse ni l'attendu ni le plafond ; sinon, retour à Lazar. L'attendu du devis (88,0 à 132,4 USD) est celui que la fiche arrondissait à « 88 à 132 » : la condition est tenue.
   - Enveloppe de relance (GO-87) : la ligne porte « Mêmes conditions que GO-86 ; caduque si le texte scellé met la relance sous le plafond commun », que le texte ne reprend pas (X-4).
   - Recharge : la fiche disait à Lazar « Recharge à demander : 180 USD ; 236 si tu ouvres l'enveloppe de relance ». Il l'a ouverte. Le devis le dit une fois, mais demande ailleurs 180, puis 187, sans l'enveloppe (X-6).
   - Les cinq autres recommandations (GO-88) sont écrites avec leurs replis. Un reste : le devis fait relever le prix du volume « avant le scellement », alors que GO-88 (6) dit « avant toute dépense » (X-2f).
3. **Les 18 couples de l'erratum 1.**
   - Chacune des sept marques est levée conformément au rapport v4 :
     - nom de carte, point (d) ;
     - six classes et marqueur, point (a) ;
     - copie `-x1` tenue par l'engagement et le code de lecture, point (b) ;
     - refus d'une ligne de relance à plus de deux instances ou au-delà de 56 USD, point (c), au texte et au devis ;
     - version de `transformers` au manifeste, § 2 ;
     - deux entrées des instances 6 et 7, point (f).
   - Les neuf points (g) pris par le texte disent ce que le code fait : modèle nu (1) ; gardes d'instance (2) ; échéance de la ligne de relance et sens de « tombée » (3) ; ordre et échéance des créations tenus par la session (4) ; clé d'injection (5) ; évaluation réduite au résultat de la famille (6) ; base de temps de la coupure (7) ; « 0.5k » (8) ; coupe 3 (12).
   - **La règle de W-m3 est juste et complète.**
     - Un compteur par instance, contre la coupure de l'instance remplacée pour une relance.
     - Un compteur commun, qui garde la première marche d'une instance tombée et ne compte pas la relance.
     - Pas de troisième compteur.
     - À l'inscription, la somme est bornée à deux instances et 56 USD. Avec deux instances au plus, les coupures ne passent pas 54 USD (28 + 26) : la borne de 56 ne mord jamais avant celle de deux instances, et les deux sont codées.
     - Le plafond n'arrête pas une relance en cours. L'exposition est de 256 USD au plus, et le devis le dit.
4. **Les choix propres au rédacteur : recevables.**
   - *« Collé »*. Une lettre touche le nombre, avant ou après ; « k » n'en est pas une ; un tiret sépare. Si le premier nombre est collé, la règle ne joue pas : tous les nombres comptent, comme sans elle, et aucune action n'est moins éditable qu'avant. La condition est la même pour tous les membres, et le lecteur gelé n'est pas touché.
   - *Les six classes* : ce sont celles du rapport, point (a) 2.
   - *« Tombée »*. Une instance dont le versement est repris et prouvé, sans rien lire, n'est pas tombée ; la décision ne dépend que d'un fait technique. Si la reprise échoue, les sorties sont perdues et l'instance tombe. Sa relance reste sous l'échéance de la ligne unique (H + 54 heures), que tient la mère.
   - *La coupe 3*. La neuvième et la dixième famille partent ensemble, avec l'instance 5 : il reste huit familles, et les épreuves restent à 99 % sans aucune tolérance. L'erreur de l'issue « empreinte » passe de 2^−10 à 2^−8, soit de 0,1 à 0,4 %. Le texte suit la granularité du code, une instance forme toutes ses familles ou aucune. Le prix, une famille de plus perdue dans ce cas de pénurie, se lit dans le texte.
   - *Le modèle nu et la base de temps de la coupure* sont alignés sur le code. Une phrase du devis dit trop : l'échéance d'arrêt ne tient pas la coupure « dans tous les cas » (X-2c). Le code la calcule au prix horaire de l'offre (`echeance_arret_s`). Ce que ce prix ne compte pas peut donc passer la coupure : le téléchargement, et le stockage s'il n'y est pas. C'est la garde de dépense qui tient la coupure.
5. **Les retouches de consolidation et l'étape 5.**
   - *P-3 n'est compatible avec le code que si l'on écrit dans la bonne colonne.* Le code lit le registre propre en lignes de table « | CLÉ | instant | contenu | référence | ». Il exige :
     - un instant au format `AAAA-MM-JJTHH:MM:SSZ` ;
     - pour `SCELLEMENT-B5F`, le contenu « `prereg/<nom>.md ; sha256 <64> ; membres-apprentissage <2|3> ; piece <famille|instance>` », en correspondance entière.

     Il refuse le registre entier pour une clé en double, ou pour une ligne de table qui porte « -B5F » sans être une ligne à clé connue. La référence, elle, est libre.

     Où va chaque chose :
     - dans la **colonne de référence** de `SCELLEMENT-B5F` : l'empreinte du devis scellé, la tête du dépôt, l'empreinte de ce rapport et le nom de la session de formation ;
     - dans celle de `GO-LECTURE-B5F` : le nom de la session de lecture, désignée plus tard, puisqu'une ligne ne se réécrit pas ;
     - dans la référence de la ligne de l'étape, ou sous la table : les désignations du point 7 et le mot du rapprochement M-6.

     Écrits dans la colonne de contenu, ou en ligne de table à clé neuve, ils arrêteraient le code au départ (X-1).
   - *P-4 (M-6, « rapprochement non fait au scellement »)* : recevable. L'échéance posée par le rédacteur, avant `VERDICT-B5F`, est une règle de procédure. Le mot attendu ne change rien au plan, et son absence est dite dans le verdict. Le mot s'écrit hors de la table (X-1b).

     Mais P-4 laisse deux autres phrases dire le contraire : le rapprochement s'y fait « avant le scellement », et « peut encore changer » la règle de la valeur du jumeau (X-5).
   - *P-1 (M-2), P-2 (M-10, que X-3e met à jour) et P-5 (M-5)* : justes.
   - *Le devis nomme encore le premier candidat* dans sa puce « Texte qu'il chiffre » (X-2a). Sa puce « Candidat au scellement » le dit à copier à l'octet (X-2e), et son en-tête dit encore « le brouillon 4 est en vérification » (X-2b, c'était mon couple W-m4a).
6. **Prêt à être copié à l'octet ?** Pas tel quel. Après les 22 couples, oui. Sans eux :
   - le texte et le devis se diraient encore candidats, « à copier à l'octet si la vérification le dit scellable tel quel » ;
   - « Contre-lecture », M-10 et un risque du calendrier diraient la vérification en attente ;
   - deux phrases contrediraient l'état de M-6 au scellement ;
   - le devis ferait demander une recharge sans l'enveloppe ;
   - et, surtout, P-3 pourrait faire écrire au registre une ligne que le code refuse.

## Ce qui menace un départ le 21

- **Le code de formation**, son troisième tour et sa vérification, puis `CODE-FORMATION-B5F`. C'est le pas le plus long d'ici là, et le texte le dit : chaque jour de retard de cette ligne retarde le départ d'autant. Le rapport v4 vise un gel le 22 (§ 7), avec quatre à sept heures de développeur pour ce tour, plus sa vérification : un départ le 21 demande d'avancer ce gel d'un jour.
- **L'application des couples et le registre propre.** Les deux empreintes ci-dessus contrôlent l'application. Le registre propre n'existe pas encore dans l'arbre : sa première ligne s'écrit au scellement, au format de X-1b. Une seule ligne mal formée arrête la formation au départ. C'est un arrêt sûr, mais le jour même.
- **La recharge** : 236 USD avant le départ, 243 si la chaîne voisine relit ses quatre cases la même semaine (X-6). Elle n'est pas due si la recharge automatique rapportée par Lazar (GO-68) est confirmée. Sinon, la formation part en deux vagues.
- **Le marché** : moins de quatre cartes au prix du devis, et c'était le cas le 19 au soir, impose le lancement au fil des offres. Au-delà de trois vagues, des familles manquent à H + 30 heures, et les coupes s'appliquent.
- **Le code de lecture** devient le chemin critique si le départ a lieu le 21. Sans `CODE-LECTURE-B5F` à la fin de la formation, la répétition générale se fait sur le modèle jouet (GO-88, 5).
- **La première carte.** Les essais du paquet passent sous Python 3.11, mais ni sur la carte ni avec torch pour CUDA (rapport v4, § 3 et § 7) : lancer la première instance seule, quelques minutes avant les autres, reste la précaution écrite.
- **Le prix du volume de 200 Go** est relevé et porté à Lazar avant toute dépense de volume (GO-88, 6), sinon les replis s'appliquent. Il ne retient pas la formation.

## Constats

### X-1 — majeur, formation : le registre propre, tel que le code le lit

**Le fait.** Le titre de la section des marqueurs (P-3) dit que ce qui reste ouvert « est rempli par la ligne `SCELLEMENT-B5F` … sans changer le contenu que lit le code ». Il ne dit pas dans quelle colonne. Il y range les noms des deux sessions, alors que la session de lecture n'est pas désignée au scellement.

Le point 7 et M-6 font écrire « au registre propre », sans format. « Lignes de registre » ne donne ni le format des lignes ni celui de l'instant. Or le code de formation :
- lit le contenu de `SCELLEMENT-B5F` par une correspondance entière (`formation_v1.lire_code_et_accord`) ;
- lit l'instant au format `AAAA-MM-JJTHH:MM:SSZ` ;
- refuse le registre entier pour une clé en double ou pour toute ligne de table qui porte « -B5F » sans être une ligne à clé connue (`engagement_v1.lignes_du_registre`).

Une empreinte ajoutée au contenu, une ligne « DÉSIGNATION-…-B5F » ou un instant « 2026-11-20 08:00Z » arrêteraient la formation au départ. Ce serait un arrêt sûr, mais le jour du départ. Le registre propre n'existe pas encore : tout s'y écrit pour la première fois au scellement.

**Couples** :
- X-1a, le titre de la section : quoi va dans la colonne de référence de quelle ligne ;
- X-1b, « Lignes de registre » : la ligne à quatre colonnes, l'instant, ce que le code lit et refuse, où va tout le reste ;
- X-1c, M-7.

« Lignes de registre » est une section dont dépend la formation. Les couples ne changent rien à ce que fait le code : ils écrivent ce qu'il exige déjà.

### X-2 — mineur, formation (devis) : le devis se dit encore candidat, et deux phrases disent plus que vrai

- X-2a : la puce « Texte qu'il chiffre » nomme le premier candidat comme nom provisoire du texte.
- X-2b : l'en-tête dit « le brouillon 4 est en vérification ».
- X-2c : l'échéance d'arrêt n'arrête pas l'instance « avant sa coupure dans tous les cas ». Le code la calcule en heures, au prix horaire de l'offre (`formation_v1.echeance_arret_s`). Ce que ce prix ne compte pas passe donc outre : le téléchargement, et le stockage (au plus 0,08 USD de l'heure) s'il n'y est pas. La limite dure borne les heures ; la garde de dépense, au cumul relevé, tient la coupure.
- X-2d : le titre. Copié sous son nom définitif, le devis s'appellerait encore « candidat au scellement ».
- X-2e : la puce « Candidat au scellement » dit « ces seules retouches » et « à copier à l'octet ». Après les couples, les deux sont faux. Elle dit maintenant ce que les couples changent au devis.
- X-2f : le devis fait relever le prix du volume « avant le scellement », alors que la phrase suivante et GO-88 (6) disent « avant toute dépense ».

### X-3 — mineur, lecture : le texte, une fois scellé, doit se dire scellé

- X-3a : le titre.
- X-3b : le statut.
- X-3c : ce qui sépare le texte du brouillon 4. Les couples de cette vérification ne sont pas dans la table : la phrase « Tout ce qui le sépare … est énuméré dans la table » le dirait à tort.
- X-3d : « Contre-lecture ». Son verdict y est écrit ; l'empreinte du rapport, elle, va à la ligne de scellement, puisque le texte ne peut contenir l'empreinte d'un rapport qui le cite.
- X-3e : M-10.
- X-3f : le statut dit le devis « candidat … à copier à l'octet ».
- X-3g : la vérification de ce candidat reste en tête des risques du calendrier.

Copié à l'octet sans eux, le texte scellé se dirait candidat, et sa vérification en attente.

### X-4 — mineur, lecture : une condition de GO-87

La section « Nœuds » reprend GO-87 sans « Mêmes conditions que GO-86 » ni sa clause de caducité. Couple X-4a.

### X-5 — mineur, formation : le rapprochement M-6, dit ailleurs « avant le scellement »

P-4 écrit l'état de M-6 au scellement : rapprochement non fait, à faire après le scellement et avant l'envoi du verdict ; son mot ne change rien à ce plan. Deux phrases antérieures disent encore le contraire :
- la ligne 8 de la table de l'exposition : « rapprochement par une session habilitée avant le scellement » ;
- le paragraphe « Sections dont dépend le code de formation » : « Le rapprochement du marqueur M-6 peut encore changer la seule règle de la valeur du jumeau (point 3) ».

Scellée telle quelle, la seconde laisserait lire qu'un mot rendu après le scellement peut encore changer une règle que le code de formation applique. Couples X-5a et X-5b.

### X-6 — mineur, formation (devis) : la recharge ne compte pas l'enveloppe que Lazar a ouverte

La fiche disait à Lazar : « Recharge à demander : 180 USD ; 236 si tu ouvres l'enveloppe de relance ; 7 de plus si l'autre chaîne du barreau relit ses quatre cases la même semaine. » Il l'a ouverte (GO-87). Le devis (§ 6) le dit une fois : « la recharge la compte : 236 USD, ou 243 ». Mais sa ligne en gras demande « 180 USD avant le départ de la formation », et plus loin « au moins 187 », puis « 187 USD … 180 sinon ».

Une recharge de 180 laisse l'enveloppe sans crédit, sauf si la recharge automatique (GO-68, non vérifiée) est confirmée. Une relance de nuit pourrait alors s'arrêter faute de crédit. Les couples X-6a, X-6b et X-6c alignent ces trois phrases sur la première ; aucune coupure ne change.

## Remarques sans couple

- **La réserve de l'étalon n'était pas sous les yeux de Lazar quand il a tranché.** Il a tranché la fiche v4 vers 22:42Z (GO-86 à -88). Cette fiche disait « Deux réserves restent ». Ma vérification du brouillon 4 a été scellée vers 22:45Z, et la fiche v5 (`25a37968…`) porte « pour mémoire » les deux réserves qu'elle ajoute, dont l'étalon de la poussée (W-M1).

  Ses décisions n'en dépendent pas : calcul, relance, répétition, volume, témoin, niveau. Mais cette réserve limite ce que dira le mot « sabotage ». À lui porter avec le verdict de cette vérification, si la fiche v5 ne l'a pas déjà été.
- La ligne « = 203 » du calcul scellé est traitée par l'erratum (§ 4) comme je l'avais dit : le devis a raison, et rien n'en dépend.
- **« 0.5k » (G-8a).** Une origine déjà sous 1 avec ce suffixe reste éditée « dans la même écriture ». Le jumeau peut alors gagner une décimale (« 0.5k » ramené à la grille, « 0.15k »). La liste des écritures propres à un sens (point 3) ne compte que les décimales perdues.

  Le cas est rare et relève de la rivale déjà déclarée ouverte, la trace propre au sens de l'édition, que l'issue « sabotage » nomme dans ce qu'elle ne tranche pas. Il ne demande ni couple ni code avant le départ ; le verdict peut le dire.
- **Laissés tels quels, parce que datés.** Au devis : la puce « Brouillon 5 », « Il attend la vérification de son différentiel ». Au texte : « Ce qui change au brouillon 5 », « Ce candidat est le brouillon 5 avec cet erratum », et « Peuvent encore changer jusqu'au scellement ». Ils décrivent un état passé, et ne contredisent rien après le scellement.
- **Pas de seconde vérification de fond.** Ces couples ne touchent ni la construction ni les épreuves. Leur application se contrôle par les deux empreintes données plus haut.

## Couples exacts

Programme : `outils-verification-candidat-scellement-v2-v1/couples-verification-candidat-v2-v1.py`.
- Chaque « avant » est trouvé une seule fois dans la pièce scellée, et encore une fois au moment où il s'applique, dans l'ordre ci-dessous.
- Aucun « après » n'y est déjà.
- Le validateur du dépôt ne trouve aucun problème à la copie du texte après les 22 couples.
- Après les couples, aucune des mentions d'attente cherchées ne reste.
- Le même programme vérifie, avec `--document`, que chaque couple est reproduit ici à l'octet.

Les « avant » de X-2d et X-3a finissent par le saut de ligne du titre, d'où la ligne vide avant la fin de leur bloc.

#### Couple X-1a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
## Marqueurs : état au scellement (ce texte est copié à l'octet : ce qui reste ouvert est rempli par la ligne `SCELLEMENT-B5F` du registre propre, et par elle seule, sans changer le contenu que lit le code de formation : l'empreinte du devis scellé, la tête du dépôt, les noms des sessions)
```

Après :

```text
## Marqueurs : état au scellement (ce texte n'est plus modifié au scellement : ce qui reste ouvert, l'empreinte du devis scellé, la tête du dépôt, l'empreinte du rapport de vérification du candidat et le nom de la session de formation, s'écrit dans la colonne de référence de la ligne `SCELLEMENT-B5F` du registre propre ; sa colonne de contenu, que lit le code de formation, garde exactement le format de « Lignes de registre » ; le nom de la session de lecture, désignée plus tard, s'écrit dans la colonne de référence de la ligne `GO-LECTURE-B5F`)
```

#### Couple X-1b — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
Registre propre : `registres/barreau5-familles-jumelles-v1.md`, lignes ajoutées, jamais réécrites ; jamais `registres/scellements-v1.md`.
```

Après :

```text
Registre propre : `registres/barreau5-familles-jumelles-v1.md`, lignes ajoutées, jamais réécrites ; jamais `registres/scellements-v1.md`. Chaque ligne à clé est une ligne de table « | CLÉ | instant | contenu | référence | », l'instant écrit `AAAA-MM-JJTHH:MM:SSZ` ; le code lit à la lettre le contenu des clés dont le format est écrit ci-dessous, et celui de `CODE-FORMATION-B5F` et de `GO-FORMATION-B5F` au format que fixe le code de formation ; il refuse le registre entier s'il trouve une clé en double, ou une ligne de table qui porte « -B5F » sans être une ligne à clé connue ; la référence est libre (ni « | » ni saut de ligne). Tout le reste, désignations des rôles avec la version de la liste consultée et la catégorie vérifiée (point 7), mot du rapprochement M-6, s'écrit dans la colonne de référence de la ligne de l'étape, ou sous la table, hors de toute ligne de table.
```

#### Couple X-1c — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
M-7 : nom de la session de formation et de la session de lecture : remplis par la ligne `SCELLEMENT-B5F` ;
```

Après :

```text
M-7 : nom de la session de formation, écrit dans la colonne de référence de la ligne `SCELLEMENT-B5F`, et nom de la session de lecture, dans celle de la ligne `GO-LECTURE-B5F` ;
```

#### Couple X-2a — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
nom définitif du candidat `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement.md`.
```

Après :

```text
nom définitif du candidat `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`, qui remplace le premier candidat (`…-v1-candidat-scellement.md`) ; le devis des deux candidats est le même, à l'octet.
```

#### Couple X-2b — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
**Brouillon : contre-lu au brouillon 2, vérifié au brouillon 3 ; le brouillon 4 est en vérification.**
```

Après :

```text
**Contre-lu au brouillon 2, vérifié aux brouillons 3 et 4, puis au candidat au scellement v2 (rapport `verification-candidat-scellement-v2-v1.md`, même dossier).**
```

#### Couple X-2c — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
la limite dure reste l'échéance d'arrêt de l'instance, comptée depuis l'impression de sa commande de création, qui l'arrête avant sa coupure dans tous les cas)
```

Après :

```text
la limite dure reste l'échéance d'arrêt de l'instance, comptée depuis l'impression de sa commande de création ; elle borne les heures au prix horaire de l'offre, et ce que ce prix ne compte pas (le téléchargement, et le stockage s'il n'y est pas) peut faire passer la coupure : c'est la garde de dépense, au cumul relevé, qui tient la coupure)
```

#### Couple X-2d — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
— v1 — candidat au scellement, à copier à l'octet sous le nom définitif si la vérification le dit scellable tel quel

```

Après :

```text
— v1

```

#### Couple X-2e — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
puis ces seules retouches : titre, cette puce, nom du texte chiffré. Aucun chiffre ne change. À copier à l'octet sous le nom `devis-adaptateurs-tenus-a-l-ecart-v1.md`.
```

Après :

```text
puis ces seules retouches : titre, cette puce, nom du texte chiffré ; enfin les couples de la vérification du candidat au scellement v2 (`verification-candidat-scellement-v2-v1.md`, même dossier), appliqués à la lettre : titre, en-tête, cette puce, nom du texte chiffré, limite dure de la règle d'arrêt (§ 4), prix du volume (§ 5), recharge à demander, l'enveloppe de relance comprise (§ 6). Aucun attendu, pire cas ni coupure ne change. Copié sous le nom `devis-adaptateurs-tenus-a-l-ecart-v1.md`.
```

#### Couple X-2f — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
**Prix non vérifié par moi : à relever sur la grille du jour avant le scellement.**
```

Après :

```text
**Prix non vérifié par moi : à relever sur la grille du jour.**
```

#### Couple X-3a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
— v1 — candidat au scellement, à copier à l'octet sous le nom définitif si la vérification le dit scellable tel quel

```

Après :

```text
— v1

```

#### Couple X-3b — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
Statut : **candidat au scellement, à copier à l'octet sous le nom définitif si la vérification le dit scellable tel quel.**
```

Après :

```text
Statut : **texte scellé : le candidat au scellement v2, avec les couples de sa vérification, copié à l'octet sous le nom définitif.**
```

#### Couple X-3c — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
(premier candidat : `54bf29c3f45ae0b2b0318b275948c836bc05aaada97c22a846a64fd776892df5`). Tout ce qui le sépare du brouillon 4 vérifié
```

Après :

```text
(premier candidat : `54bf29c3f45ae0b2b0318b275948c836bc05aaada97c22a846a64fd776892df5`) ; enfin les couples de la vérification du candidat v2 (`docs/notes/barreau5-resolution-v1/plan-avant-entretien/verification-candidat-scellement-v2-v1.md`), appliqués à la lettre et reproduits dans ce rapport. Tout ce qui sépare le candidat v2 du brouillon 4 vérifié
```

#### Couple X-3d — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
**Vérification de ce candidat : en attente**, par le même contre-lecteur. Elle porte sur le différentiel du brouillon 5, sur l'erratum 1 (`8c3451a2e76823d4ae31789164ac6597b2d9b87e809b0e251c295cb8d14a2e40`) et sur les retouches de consolidation, tous énumérés dans `table-difference-candidat-scellement-v2.md`. S'il est dit scellable tel quel, ce candidat est copié à l'octet sous le nom définitif.
```

Après :

```text
**Vérification du candidat au scellement v2**, par le même contre-lecteur (Claude Opus 5.5) : rapport `docs/notes/barreau5-resolution-v1/plan-avant-entretien/verification-candidat-scellement-v2-v1.md`. Elle porte sur le différentiel du brouillon 5, sur l'erratum 1 (`8c3451a2e76823d4ae31789164ac6597b2d9b87e809b0e251c295cb8d14a2e40`) et sur les retouches de consolidation, tous énumérés dans `table-difference-candidat-scellement-v2.md`. Verdict : « scellable après ces couples » ; ses couples sont appliqués à la lettre ; l'empreinte du rapport s'écrit dans la colonne de référence de la ligne `SCELLEMENT-B5F`.
```

#### Couple X-3e — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
M-10 : fait (vérification du brouillon 4 rendue, « scellable après ces couples ») ; reste la vérification du candidat au scellement ;
```

Après :

```text
M-10 : fait (vérification du brouillon 4 rendue, « scellable après ces couples ») ; fait (vérification du candidat au scellement v2 rendue, « scellable après ces couples », ses couples appliqués) ;
```

#### Couple X-3f — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
Le devis est un candidat lui aussi, à copier à l'octet sous le nom `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md`.
```

Après :

```text
Le devis est scellé lui aussi : son candidat au scellement v2, avec les couples de la même vérification, sous le nom `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md` ; son empreinte s'écrit dans la colonne de référence de la ligne `SCELLEMENT-B5F` (M-3).
```

#### Couple X-3g — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
- La vérification de ce candidat (différentiel du brouillon 5, erratum 1, retouches de consolidation) : le code exige le texte entier scellé.
```

Après :

```text
- La vérification de ce candidat (différentiel du brouillon 5, erratum 1, retouches de consolidation) : rendue, « scellable après ces couples », ses couples appliqués ; le code exige le texte entier scellé.
```

#### Couple X-4a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
GO-2026-11-19-87` : enveloppe de relance, à part de ce plafond, 56 USD au plus, pour deux instances tombées au plus, une fois chacune, au sens de ce texte.
```

Après :

```text
GO-2026-11-19-87` : enveloppe de relance, à part de ce plafond, 56 USD au plus, pour deux instances tombées au plus, une fois chacune, au sens de ce texte, aux mêmes conditions que l'accord de calcul ; cette enveloppe serait caduque si ce texte mettait la relance sous le plafond commun, ce qu'il ne fait pas.
```

#### Couple X-5a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
Le rapprochement du marqueur M-6 peut encore changer la seule règle de la valeur du jumeau (point 3).
```

Après :

```text
Le rapprochement du marqueur M-6 n'est pas fait au scellement : son mot, rendu plus tard, ne change pas la règle de la valeur du jumeau (point 3), ni rien d'autre de ce plan.
```

#### Couple X-5b — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
rapprochement par une session habilitée avant le scellement (marqueur M-6)
```

Après :

```text
rapprochement par une session habilitée, non fait au scellement, à faire avant l'envoi du verdict (marqueur M-6)
```

#### Couple X-6a — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
**Recharge à demander : 180 USD avant le départ de la formation**, ce qui porte le crédit à ≈ 202 USD, le plafond demandé (200 − 21,97 = 178,03, arrondi).
```

Après :

```text
**Recharge à demander avant le départ de la formation : 236 USD**, l'enveloppe de relance étant ouverte : 180 pour le plafond, ce qui porte le crédit à ≈ 202 USD, le plafond demandé (200 − 21,97 = 178,03, arrondi), et 56 pour l'enveloppe.
```

#### Couple X-6b — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
la recharge ajoute leurs coupures : au moins 187 USD avec la seule relecture des quatre cases.
```

Après :

```text
la recharge ajoute leurs coupures : au moins 243 USD avec la seule relecture des quatre cases.
```

#### Couple X-6c — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
la recharge à demander est donc de **187 USD** si les deux chaînes courent (178,03 + 8,5), 180 sinon.
```

Après :

```text
la recharge à demander est donc de **243 USD** si les deux chaînes courent (178,03 + 8,5 + 56, l'enveloppe de relance comprise), 236 sinon.
```

## Fichiers ouverts pour cette vérification

- le message de la mère (mandat de cette vérification, transmis en ligne) ;
- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md` et son devis : lus par différence au brouillon 4, ligne à ligne, puis aux lignes citées ici ;
- `…/plan-avant-entretien/table-difference-candidat-scellement-v2.md` (entière) ;
- `…/plan-avant-entretien/fabrique-candidat-scellement-v2.py` (entier), `fabrique-candidat-scellement-v1.py` (structure), et leurs modules de sections, chargés par programme ;
- `…/plan-avant-entretien/erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md` (§ 1 à 5 et ses couples, par programme) ;
- `…/plan-avant-entretien/points-g-rapport-v4-ranges-v1.md` (la table) ;
- `…/plan-avant-entretien/code-formation/rapport-developpeur-corrections-code-formation-v4.md` (§ 2 à 5, et § 7) ;
- `…/code-formation/rapport-developpeur-corrections-code-formation-v3.md` : les lignes sur `SCELLEMENT-B5F`, par recherche ;
- `…/plan-avant-entretien/fiche-v5-lazar-v1.md` (en-tête, « Où en est le texte », recharge) et sa différence avec `fiche-v4-lazar-v1.md` ;
- `…/plan-avant-entretien/verification-plan-brouillon4-v1.md` (mon rapport précédent : deux lignes sur la recharge) ;
- `registres/go.md` : les lignes `GO-2026-11-19-79` à `-88` ;
- `src/controle_ia/barreau5_familles/formation_v1.py` (l. 1008-1060, et les lignes qui lisent les clés du registre) et `engagement_v1.py` (l. 28-60, 125-180) : format du registre lu par le code ;
- listes de noms : dossiers `plan-avant-entretien/`, `prereg/` et `registres/` (le registre propre n'y est pas encore).
