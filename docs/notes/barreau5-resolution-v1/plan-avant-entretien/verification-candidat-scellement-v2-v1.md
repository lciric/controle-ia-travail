# Vérification du candidat au scellement v2 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) — v1

- Vérificateur : le même contre-lecteur que pour les brouillons 2, 3 et 4 (Claude Opus 5.5), sous-agent de la session mère. Autre modèle que le rédacteur (Claude Fable 5.2). Écrit le 19 novembre 2026, de 23:10Z à 23:30Z environ (horloge du conteneur). Dernière vérification avant le scellement (commit `5e32a8f30`).
- Pièces, sceaux vérifiés, tous égaux à ceux du message de la mère :
  - le candidat v2 : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md` (`088e15ef…`) et son devis `devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md` (`94a628a7…`) ;
  - la table de différence v2 (`c4deb480…`) ;
  - la fabrique `fabrique-candidat-scellement-v2.py`, `sections_candidat_scellement_v2.py` et leur sortie, avec leurs étages v1 et ceux du brouillon 5 ;
  - le brouillon 5 (`6f7e2041…`), sa table (`8be817c6…`) et son devis (`9ba5db06…`) ;
  - l'erratum 1 (`8c3451a2…`) et son contrôle ;
  - le rangement des points (g) (`76e0e27e…`) ;
  - le premier candidat (`54bf29c3…`) ;
  - le rapport v4 du développeur (`b7e22555…`) et la fiche v5 (`25a37968…`).
- Mes outils, neufs, dans `outils-verification-candidat-scellement-v2-v1/` (même dossier), scellés :
  - `differences-brouillon4-candidat-v2-v1.py` : tout ce qui sépare le candidat v2 du brouillon 4 vérifié, ligne à ligne, lu en entier, sans se fier à la table. Sa sortie se rejoue à l'identique et n'est pas versée.
  - `rejeu-chaine-candidat-v2-v1.py` et sa sortie : la chaîne du rédacteur, rejouée en mémoire sans lancer sa fabrique, qui écrit.
  - `couples-verification-candidat-v2-v1.py` et sa sortie.
  - `journal-de-verification-candidat-v2-v1.md`.

  Chaque sortie versée est écrite par l'outil d'écriture, puis comparée par programme à la sortie du programme.
- Aucune donnée ni aucun résultat ; aucun nombre de résultat d'expérience close ici. Aucun fichier interdit, rien sous `/root/.claude/`, aucune commande d'arrêt ni de recherche de processus par motif, aucun appel en ligne à l'interpréteur, aucun réseau, aucune dépense, aucun commit. Lu dans le code, pour juger le point 5 du message : les lignes du lecteur de registre (`barreau5_familles/formation_v1.py`, `lire_code_et_accord` ; `engagement_v1.py`, `lignes_du_registre`). Ce code est en troisième tour, non figé : je ne le juge pas, je lis le format qu'il attend.

## Verdict

**Scellable après ces couples** : 13 couples exacts, chaque « avant » trouvé une fois par programme ; le validateur du dépôt ne trouve rien à la copie. Aucun constat bloquant. Un majeur, **formation** : X-1, le registre propre tel que le code le lit. Trois mineurs : X-2, devis ; X-3 et X-4, lecture.

Appliqués à la lettre et dans l'ordre au candidat v2, ces couples donnent les pièces à sceller. Le texte aura l'empreinte `e21e23a9f72daea7fd934049dd9d22990f1047384c53dc7bdaa9568cf9e869d6`, à copier sous `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`. Le devis aura l'empreinte `b20a6256dbe1fd209a2d92073ba22fe8b6361b20855a99d9753a9b9322a90b89`, à copier sous `devis-adaptateurs-tenus-a-l-ecart-v1.md`. Une application qui ne rend pas ces deux empreintes n'est pas celle-ci. Ces couples ne touchent ni la construction ni les épreuves.

## Réponses aux points du message

1. **Mes 20 couples : tous présents à l'octet.** 18 sont dans le candidat v2 (13 au texte, 5 au devis) et 2 dans la fiche v5, hors candidat. J'ai rejoué en mémoire la chaîne entière du rédacteur, ses 79 écritures ; elle rend à l'octet le brouillon 5, l'état d'après l'erratum, le premier candidat et le candidat v2, texte et devis. Lu ligne à ligne, ce qui sépare le candidat v2 du brouillon 4 est exactement ce que la table de différence énumère.
2. **Les mots de Lazar sont fidèles**, conditions comprises :
   - accord de calcul (GO-86) : plafond commun de 200 USD, coupures du devis scellé, répétition générale comprise si le code de lecture est prêt, valable seulement après `SCELLEMENT-B5F` et `CODE-FORMATION-B5F` et si le devis ne dépasse ni l'attendu ni le plafond, sinon retour à Lazar ;
   - enveloppe de relance (GO-87) ;
   - les cinq autres recommandations (GO-88), avec leurs replis.

   Un manque : GO-87 porte « mêmes conditions que GO-86 ; caduque si le texte scellé met la relance sous le plafond commun », que le texte ne reprend pas (X-4). Le devis n'a pas changé depuis la fiche, et son attendu (88,0 à 132,4 USD) est celui que la fiche arrondissait à « 88 à 132 » : la condition de GO-86 est tenue.
3. **Les 18 couples de l'erratum 1.**
   - Chacune des sept marques est levée conformément au rapport v4 : nom de carte, point (d) ; six classes et marqueur, point (a) ; copie `-x1` tenue par l'engagement et le code de lecture, point (b) ; refus d'une ligne de relance à plus de deux instances ou au-delà de 56 USD, point (c) ; version de `transformers` au manifeste, § 2 ; deux entrées des instances 6 et 7, point (f).
   - Les points (g) pris par le texte disent ce que le code fait : modèle nu, gardes d'instance, échéances tenues par la session, clé d'injection, évaluation réduite au résultat de la famille, « 0.5k », coupe 3, base de temps de la coupure.
   - **La règle de W-m3 est juste et complète.** Un compteur par instance (la coupure de l'instance remplacée pour une relance). Un compteur commun qui garde la première marche d'une instance tombée et ne compte pas la relance. Pas de troisième compteur. Somme bornée à l'inscription : deux instances, 56 USD. Le plafond n'arrête pas une relance en cours. Exposition de 256 USD au plus, dite au devis. Avec deux instances au plus, la somme des coupures ne passe pas 54 USD : la borne de 56 ne mord jamais avant celle de deux instances, et les deux sont codées.
4. **Les choix propres au rédacteur : recevables.**
   - *« Collé »* (avant ou après, « k » exclu, tiret qui sépare) : la règle ne joue pas quand le premier nombre est collé, ce qui ne rend jamais une action moins éditable qu'avant ; elle est la même pour les trois membres et laisse le lecteur gelé intact.
   - *Les six classes* : ce sont celles du rapport, point (a) 2.
   - *« Tombée »* : une instance dont le versement est repris et prouvé sans rien lire n'est pas tombée. La décision ne dépend que d'un fait technique et ne lit aucune sortie. Si la reprise échoue, les sorties sont perdues et l'instance tombe, dans l'échéance de la relance.
   - *La coupe 3* : la neuvième et la dixième famille partent ensemble, avec l'instance 5. L'erreur de l'issue « empreinte » passe de 2^−10 à 2^−8, soit 0,1 à 0,4 %, et l'épreuve reste à 99 % sans aucune tolérance. Le texte suit la granularité du code : le prix est une famille de plus perdue dans ce cas de pénurie, et il est dit.
   - *Le modèle nu et la base de temps de la coupure* sont alignés sur le code, mais une phrase du devis dit trop : l'échéance d'arrêt ne tient pas la coupure « dans tous les cas » (X-2c). Calculée au prix plafond de la carte, elle laisse le stockage et le téléchargement, à leurs bornes, dépasser la coupure de quelques USD ; c'est la garde de dépense qui tient la coupure.
5. **Les retouches de consolidation et l'étape 5.**
   - *P-3 n'est compatible avec le code que si l'on écrit dans la bonne colonne.* Le code lit le registre propre en lignes de table « | CLÉ | instant | contenu | référence | ». Il exige que le contenu de `SCELLEMENT-B5F` soit, à la lettre, « `prereg/<nom>.md ; sha256 <64> ; membres-apprentissage <2|3> ; piece <famille|instance>` » (correspondance entière). Il refuse le registre entier pour une ligne de table à clé inconnue ou en double. La référence, elle, est libre.

     L'empreinte du devis scellé, la tête du dépôt, la vérification du candidat et le nom de la session de formation vont donc dans la **colonne de référence** de `SCELLEMENT-B5F`. Le nom de la session de lecture, désignée plus tard, va dans celle de `GO-LECTURE-B5F`, puisqu'une ligne ne se réécrit pas. Les désignations du point 7 et le mot du rapprochement M-6 vont dans la référence de la ligne de l'étape, ou sous la table. Écrits dans la colonne de contenu, ou en ligne de table à clé neuve, ils arrêteraient le code au départ (X-1).
   - *P-4 (M-6, « rapprochement non fait au scellement »)* : recevable. L'échéance posée par le rédacteur, avant `VERDICT-B5F`, est une règle de procédure ; le mot attendu ne change rien au plan, et l'absence de mot est dite dans le verdict. Le mot s'écrit hors de la table (X-1b).
   - *P-1, P-2 et P-5* : justes.
   - *Le devis nomme encore le premier candidat* dans sa puce « Texte qu'il chiffre » (X-2a). Son en-tête dit encore « le brouillon 4 est en vérification », et c'était mon couple W-m4a (X-2b).
6. **Prêt à être copié à l'octet ?** Pas tel quel. Après les 13 couples, oui. Sans eux :
   - le titre et le statut du texte scellé le diraient encore « candidat … si la vérification le dit scellable tel quel » ;
   - « Contre-lecture » et M-10 diraient la vérification en attente ;
   - le devis nommerait le premier candidat ;
   - et, surtout, la phrase de P-3 pourrait faire écrire au registre une ligne que le code refuse.

## Constats

### X-1 — majeur, formation : le registre propre, tel que le code le lit

**Le fait.** Le titre de la section des marqueurs (P-3) dit que ce qui reste ouvert « est rempli par la ligne `SCELLEMENT-B5F` … sans changer le contenu que lit le code ». Il ne dit pas dans quelle colonne. Et il y range les noms des deux sessions, alors que la session de lecture n'est pas désignée au scellement.

Le point 7 et M-6 font écrire « au registre propre », sans format. Or le code de formation :
- lit le contenu de `SCELLEMENT-B5F` par une correspondance entière (`formation_v1.lire_code_et_accord`) ;
- refuse une ligne de table à clé inconnue ou en double (`engagement_v1.lignes_du_registre`).

Une empreinte ajoutée au contenu, ou une ligne « DESIGNATION-…-B5F », arrêterait la formation au départ. Ce serait un arrêt sûr, mais le jour du départ.

**Couples** :
- X-1a, le titre de la section : quoi va dans la colonne de référence de quelle ligne ;
- X-1b, « Lignes de registre » : le format à quatre colonnes, ce que le code refuse, où va tout le reste ;
- X-1c, M-7.

« Lignes de registre » est une section dont dépend la formation. Le couple n'y change rien de ce que fait le code : il écrit ce que le code exige déjà.

### X-2 — mineur, formation (devis) : quatre restes du devis

- X-2a : la puce « Texte qu'il chiffre » nomme le premier candidat comme nom provisoire du texte.
- X-2b : l'en-tête dit « le brouillon 4 est en vérification ».
- X-2c : l'échéance d'arrêt n'arrête pas l'instance « avant sa coupure dans tous les cas ». Calculée au prix plafond de la carte, elle laisse passer le stockage (au plus 0,08 USD de l'heure) et le téléchargement (au plus 2 USD) : la limite dure borne les heures, et la garde de dépense tient la coupure.
- X-2d : le titre. Copié sous son nom définitif, le devis s'appellerait encore « candidat au scellement ».

### X-3 — mineur, lecture : le texte, une fois scellé, doit se dire scellé

- X-3a : le titre.
- X-3b : le statut.
- X-3c : la liste de ce qui le sépare du brouillon 4, avec ces couples.
- X-3d : « Contre-lecture » ; son verdict, et l'empreinte du rapport portée par la ligne de scellement, puisque le texte ne peut contenir l'empreinte d'un rapport qui le cite.
- X-3e : M-10.

Copié à l'octet sans eux, le texte scellé se dirait candidat, et sa vérification en attente.

### X-4 — mineur, lecture : une condition de GO-87

La section « Nœuds » reprend GO-87 sans « mêmes conditions que GO-86 » ni sa clause de caducité. Couple X-4a.

## Remarques sans couple

- La fiche v5 (`25a37968…`) porte mes deux couples de la fiche. Lazar a tranché les décisions de la fiche v4 (GO-86 à -88) vers 22:42Z, avant ma vérification du brouillon 4. **La réserve de l'étalon (W-M1) n'était pas sous ses yeux quand il a tranché.** Elle ne touche ni la formation ni la dépense, mais elle limite ce que dira le mot « sabotage » : la mère la lui porte avec le verdict de cette vérification.
- La ligne « = 203 » du calcul scellé est traitée par l'erratum (§ 4) comme je l'avais dit : le devis a raison, et rien n'en dépend.
- Avec la règle « 0.5k » (G-8a), une origine déjà sous 1k reste éditée, et le jumeau peut gagner une décimale (« 0.15k »). Cette écriture propre au sens bas n'est pas dans la liste du point 3, qui ne compte que les décimales perdues. Le cas est rare et va dans le sens de la rivale déjà déclarée ouverte : à compter avec les autres écritures propres à un sens, si le code le fait déjà.
- Pas de seconde vérification de fond : ces couples ne touchent ni la construction ni les épreuves. Leur application se contrôle par les deux empreintes données plus haut.

## Couples exacts

Programme : `outils-verification-candidat-scellement-v2-v1/couples-verification-candidat-v2-v1.py`.
- Chaque « avant » est trouvé une seule fois dans la pièce scellée, et encore une fois au moment où il s'applique, dans l'ordre ci-dessous.
- Aucun « après » n'y est déjà.
- Le validateur du dépôt ne trouve aucun problème à la copie du texte après les 13 couples.
- Le même programme vérifie, avec `--document`, que chaque couple est reproduit ici à l'octet.

Les « avant » de X-2d et X-3a finissent par le saut de ligne du titre, d'où la ligne vide avant la fin de leur bloc. Ceux de X-3c finissent par une espace.

#### Couple X-1a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
## Marqueurs : état au scellement (ce texte est copié à l'octet : ce qui reste ouvert est rempli par la ligne `SCELLEMENT-B5F` du registre propre, et par elle seule, sans changer le contenu que lit le code de formation : l'empreinte du devis scellé, la tête du dépôt, les noms des sessions)
```

Après :

```text
## Marqueurs : état au scellement (ce texte est copié à l'octet : ce qui reste ouvert au scellement, l'empreinte du devis scellé, la tête du dépôt, la vérification du candidat et le nom de la session de formation, s'écrit dans la colonne de référence de la ligne `SCELLEMENT-B5F` du registre propre ; sa colonne de contenu, que lit le code de formation, garde exactement le format de « Lignes de registre » ; le nom de la session de lecture, désignée plus tard, s'écrit dans la colonne de référence de la ligne `GO-LECTURE-B5F`)
```

#### Couple X-1b — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
Registre propre : `registres/barreau5-familles-jumelles-v1.md`, lignes ajoutées, jamais réécrites ; jamais `registres/scellements-v1.md`.
```

Après :

```text
Registre propre : `registres/barreau5-familles-jumelles-v1.md`, lignes ajoutées, jamais réécrites ; jamais `registres/scellements-v1.md`. Chaque ligne à clé est une ligne de table « | CLÉ | instant | contenu | référence | » ; le code lit le contenu des clés au format écrit ci-dessous, à la lettre, et refuse le registre entier s'il trouve une ligne de table à clé inconnue ou une clé en double ; la référence est libre (ni « | » ni saut de ligne). Tout le reste, désignations des rôles avec la version de la liste consultée et la catégorie vérifiée (point 7), mot du rapprochement M-6, s'écrit dans la colonne de référence de la ligne de l'étape, ou sous la table, hors de toute ligne de table.
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
la limite dure reste l'échéance d'arrêt de l'instance, comptée depuis l'impression de sa commande de création ; elle borne les heures de carte au prix plafond de la carte, et le stockage et le téléchargement, à leurs bornes, peuvent faire passer la coupure de quelques USD : c'est la garde de dépense, au cumul relevé, qui tient la coupure)
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
(premier candidat : `54bf29c3f45ae0b2b0318b275948c836bc05aaada97c22a846a64fd776892df5`). 
```

Après :

```text
(premier candidat : `54bf29c3f45ae0b2b0318b275948c836bc05aaada97c22a846a64fd776892df5`) ; enfin les couples de la vérification du candidat v2 (`docs/notes/barreau5-resolution-v1/plan-avant-entretien/verification-candidat-scellement-v2-v1.md`), appliqués à la lettre. 
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

#### Couple X-4a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md`

Avant :

```text
GO-2026-11-19-87` : enveloppe de relance, à part de ce plafond, 56 USD au plus, pour deux instances tombées au plus, une fois chacune, au sens de ce texte.
```

Après :

```text
GO-2026-11-19-87` : enveloppe de relance, à part de ce plafond, 56 USD au plus, pour deux instances tombées au plus, une fois chacune, au sens de ce texte, aux mêmes conditions que l'accord de calcul ; l'accord serait caduc si ce texte mettait la relance sous le plafond commun, ce qu'il ne fait pas.
```

## Fichiers ouverts pour cette vérification

- le message de la mère (mandat de cette vérification, transmis en ligne) ;
- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md` et son devis : lus par différence au brouillon 4, ligne à ligne, et aux lignes citées ;
- `…/plan-avant-entretien/table-difference-candidat-scellement-v2.md` (entière) ;
- `…/plan-avant-entretien/fabrique-candidat-scellement-v2.py` (entier), `fabrique-candidat-scellement-v1.py` (structure), et leurs modules de sections, chargés par programme ;
- `…/plan-avant-entretien/erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md` (§ 1 à 5 et ses couples, par programme) ;
- `…/plan-avant-entretien/code-formation/rapport-developpeur-corrections-code-formation-v4.md` (§ 4 et § 5) ;
- `…/code-formation/rapport-developpeur-corrections-code-formation-v3.md` : les lignes sur `SCELLEMENT-B5F`, par recherche ;
- `…/plan-avant-entretien/fiche-v5-lazar-v1.md` (sceau, en-tête, deux fragments) ;
- `registres/go.md` : les lignes `GO-2026-11-19-86` à `-88` ;
- `src/controle_ia/barreau5_familles/formation_v1.py` (l. 1008-1065) et `engagement_v1.py` (l. 30-45, 125-180) : format du registre lu par le code ;
- liste des dossiers `plan-avant-entretien/` et `prereg/` (noms seulement).
