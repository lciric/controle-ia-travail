# Contre-lecture (R2) — « Le pari apparié borné — conception v9 » et le code v7, versions 26 et 27 — rapport v1

Contre-lecteur : sous-agent neuf **Opus 5.5**, autre modèle que l'auteur de la v9 et des versions 26 et 27 (Fable 5.1) ;
je n'ai écrit ni la conception, ni le code, ni une contre-lecture antérieure. Début : mercredi 28 octobre 2026,
**00:48:46 UTC** (`date -u`, appel séparé). Aucun fichier du dépôt modifié, aucun commit ; modules importés avec `-I -B`
(aucun bytecode écrit) ; rien lu dans `donnees/` ; aucune clé ni aucun jeton lu, affiché ou cherché ; processeur seul,
aucune dépense. Tout ce que j'ai écrit est dans ce dossier. Pendant ma session, une autre session a versé dans
`pari-de-signe/` des fichiers que je n'ai ni écrits ni lus (`conception-pari-equivalence-concordance-v1.md`,
`equivalence-v1/`) ; les objets de cette contre-lecture n'ont pas changé (empreintes revérifiées en fin, section 7).

## Verdict

1. **Conception v9 : « à amender en v10 »** (corrections locales, pas refaire). La réécriture de D-S8 dit exactement ce
   que décide N-056 (nœud 1 = b), et les chiffres du § 6 sont justes contre le pari v2 § 6. Mais la v9 formule la
   fraîcheur des unités **par fiche**, alors que la preuve de la garantie la demande **par rapport à toute la course**
   (K9-1). Elle ne dit rien des tranches ni de l'étiquette d'ordre (K9-5). Son dimensionnement de G1 (b) repose sur une
   table calculée avec des alertes indépendantes, ce que deux lectures boîte blanche des mêmes sondes ne sont pas (K9-9).
2. **Code v7, versions 26 et 27 : « à corriger ».** K8-4 est annoncée codée (« version de l'e-processus » dans la clé)
   et **n'existe pas dans le code** (K9-4). Une chaîne de trois gestes, tous acceptés par les gardes de la version 27,
   redonne l'artefact du saut de partie : une copie renommée, une tranche lue une génération d'avance, une déclaration
   « fiche non lancée » vraie. Elle donne **0,087 puis 0,626** d'au moins une fausse promotion sur 10 puis
   30 générations, contre 0,025 et 0,024 en course honnête (K9-1). Le lien entre une fiche et sa clé n'est tenu nulle
   part (K9-2). La clé contient des noms libres, si bien qu'un renommage suffit à contourner « une affirmation, une
   fiche » (K9-3).
3. **La démonstration se relit** : ses sorties sont reproduites à l'octet près (`course.json` `5c5098ea…`), et L1, L2,
   L3 et le nul × 200 sont tels que le LISEZMOI v27 les dit. **Deux lectures sont trompeuses.**
   - (a) Le « signe connu par construction » est faux une fois les seuils scellés, qui sont la seule base sur laquelle
     la garantie porte. Dans la banque publiée, le témoin « faux nul » vaut **+0,035** (il est vrai), et le témoin
     « vrai tenu » vaut **+0,0001** (il est nul). Sur 200 courses répétées, L1 se lirait « rompue » dans **13,5 %** des
     cas, alors qu'aucune fausse promotion ne survient au sens conditionnel (0 sur 250) (K9-7).
   - (b) « G1 promue en génération 3 » est une promotion e-BH dans la course du pôle. Or G1 se lit une fois, hors de la
     suite, et e-Bonferroni s'applique à ce qui sort du pôle. Sous cette règle, la fiche G1 de la démonstration ne sort
     pas (6,62 < 7,02), et elle ne sort que dans 16 % des courses répétées, alors qu'elle est « promue » dans 94 %
     d'entre elles (K9-8).
4. **La garantie de D-S25 bis tient, en raisonnement et dans les mesures**, avec des tranches, l'accumulation des
   promotions, l'arrêt au seuil et l'abandon sous contrat. Il y a deux conditions : la fraîcheur s'entend par rapport à
   toute la course, et toute décision de ne pas lire une partie se prend avant toute issue (Q3).

---

## 1. K8-1 à K8-5, K7-6, K7-7

| constat | état (texte v9 / code v26-v27) | où, pourquoi | vérifié par |
|---|---|---|---|
| **K8-1** fraîcheur | **à moitié** | Fermé pour une fiche sur une banque : `None` refusé sauf déclaration tracée, intersection refusée. Restent ouverts : (iii) la relance sous un autre nom passe dès que l'engagement est reconstruit, car la clé porte le nom du contraste (K9-3) ; (iv) une banque grandie d'une unité donne des identifiants tous différents, puisque l'empreinte de la banque est dans l'identifiant. Rien ne lie une fiche à une banque ou à une clé, donc la seconde partie est acceptée avec 40 unités physiques communes (K9-2). La preuve demande en outre la fraîcheur par rapport à la course entière (K9-1). | A2, A3, A4 ; G |
| **K8-2** « sans partie » mensonger | **texte fermé ; code à moitié** | La phrase, les chiffres (0,396 / 0,978) et l'obligation sont écrits. Mais le journal n'est pas tenu par le monde : `evaluer` ne journalise rien, l'appel est volontaire, `verifier_sans_partie` est séparé de `Course.lire` et le numéro de génération est libre. Une partie calculée, non journalisée, puis déclarée absente, passe. Cinq évaluations de la même fiche dans une génération passent aussi. Une déclaration vraie mais choisie après coup passe toujours (K9-1, K9-6). | A5 ; G |
| **K8-3** traces | **fermé** | Le second abandon d'une gelée est tracé (`abandons[("redite", f)]`). Résidu sans biais : une déclaration « sans partie » pour une fiche gelée, ou pour une fiche qui a sa partie, est enregistrée sans contrôle (K9-10). | A6 ; essai `test_abandon_d_une_gelee_et_traces` |
| **K8-4** combinaison sur Λ et arrêt hors clé | **ouvert (annoncé fermé)** | La clé a 11 champs et aucun n'est une version de l'e-processus. La v9 dit « module `pari_apparie`, version 26 » (verdict 4), puis « version 27 » (§ 3). Ni le LISEZMOI v26 ni le v27 n'en parlent. `pari_apparie.py` est identique en v26 et v27 (`d3a3107a…`). | A1 ; diff des listes d'empreintes v25 → v26 → v27 |
| **K8-5** essais | **à moitié** | Ajoutés : sans identité refusée puis déclarée, intersection partielle, seconde fiche (`Lignees`). **Λ dans la clé : pas d'essai**, contrairement au verdict 4 de la v9 : `test_cle_de_l_heritage` n'a pas de variante Λ, et `construire` ne prend pas Λ en paramètre. | lecture des essais ; 38 essais des trois fichiers passent (2,1 s) |
| **K7-6** alignement par rang | **ouvert, déclaré** (v9 § 4) | Code inchangé. Exact dans la démonstration, où chaque unité porte des épisodes sabotés et des épisodes honnêtes. | lecture |
| **K7-7** ordre dérivé de toute la banque | **ouvert, déclaré** | `ordre_secret` utilise toujours l'empreinte de toute la banque. L'étiquette libre de la version 27 ajoute un autre canal, indépendant (K9-5). | lecture |

## 2. Réponses aux questions du brief

### Q2 — D-S8 réécrite, (α), (β), (γ), § 6

- **Conforme à N-056.** G1 doit battre chaque moniteur boîte noire de la liste scellée (bases (i) et (iv) de N-007, par
  action, séquentielles noires, juge robustifié) et les bases boîte blanche (ii), la cascade, et (iii), le dernier
  état. Les planchers sont rapportés, et H2 garde ses tests (H2c). Les étiquettes (i) à (iv) concordent avec
  `noeuds-pour-lazar-v1.md` (l. 13-15). Le § 2.4 bis réécrit est juste.
- **(α) juste, avec une précision à écrire.** « Chaque composante rapportée » ne peut être que **descriptif**. Le test
  est l'intersection-union. Faire de chaque composante une affirmation (« bat la cascade ») ferait cinq tests de plus,
  sans multiplicité déclarée, et c'est H2c qui porte (ii) et (iii). De plus, la `Course` ne garde que le minimum des
  processus, pas un processus cumulé par comparateur : la démonstration nomme le plus faible d'après les parties du
  journal (K9-10).
- **(β) chiffres justes, modèle à dire.** Le pari v2 § 6 (sortie `d07e43f9…`) donne 0,628, 0,964 et 0,876, pour 0,63,
  0,96 et 0,88 cités ; 20 points → 40 unités (0,966), 10 → 100, 5 → 250. Mais ces puissances supposent des alertes
  **indépendantes** entre A et B (`simulation-dimensionnement-v2.py`, `puissance_parts`, `rho = 0`), alors que le blanc
  contre le blanc, sur les mêmes sondes, est fortement concordant. La variance par unité dépend alors de la
  **discordance**, pas de l'écart seul. Et à petit écart, le bruit de calibrage (contrôle 12) est du même ordre que
  l'écart lui-même (K9-9). « Plusieurs centaines de plus » reste une borne de prudence ; elle n'est pas chiffrée.
- **(γ) juste** : comparateurs différents, donc clés différentes. G1 et H2c lisent aussi les mêmes unités d'épreuve
  (N-050), ce qui relève des familles du programme, pas de l'héritage.

### Q3 — Garantie sous la règle de l'héritage avec des tranches

Notations : fiches i, budgets b_i fixés à l'entrée, Σ b_i ≤ Σ α_c ≤ α (tenu par le code). E_i est le produit des
e-valeurs de ses parties. R_g est l'ensemble des k*_g premières à la lecture g (ex æquo compris). U = ∪_g R_g est
l'union des promotions, et γ_i la première lecture qui promeut i.

- **(i) Accumulation.** Pour i ∈ U, b_i E_i(γ_i) ≥ 1/k*_{γ_i}, et |U| ≥ |R_{γ_i}| ≥ k*_{γ_i}. Donc 1(i ∈ U)/|U| ≤
  b_i E_i(γ_i). La valeur est gelée après la promotion, d'où E_i(γ_i) = E_i^arrêté(G_max). Il en suit
  FDP(U) ≤ Σ_{i nulle} b_i E_i^arrêté, et E[E_i^arrêté] ≤ 1 par arrêt optionnel sur un horizon borné. Accumuler ne fait
  que grossir le dénominateur. **Tient.**
- **(ii) Arrêt au seuil 1/b_i.** C'est un temps d'arrêt, y compris à l'intérieur d'une partie, unité par unité. Une fiche
  arrêtée a b_i E_i ≥ 1, donc elle est promue à la lecture suivante, quel que soit k*. **Tient.**
- **(iii) Abandon sous contrat.** Le gel après la dernière partie observée est un temps d'arrêt. **Avec des tranches
  partagées**, « avant toute issue de la génération » doit s'entendre **d'aucune fiche** : les parties des autres fiches
  sur la même tranche renseignent celle-ci. Une déclaration fausse ne compose pas, car le gel est définitif (au plus
  ×1,77 une fois, contre-lecture v8). Elle est à dire. La démonstration calcule les parties de « faible », « tenu » et
  « faux nul » sur la tranche 2 **avant** d'abandonner « avant partie » le témoin inversé. C'est sans effet ici, puisque
  la décision est écrite en dur, mais c'est contraire à la lettre (K9-10).
- **(iv) « Sans partie ».** La lecture garde E_i(g − 1), un facteur 1. C'est valide si la décision de ne pas lire est
  **prévisible**, c'est-à-dire prise sans aucune information sur les unités de la partie. Une déclaration **vraie** (rien
  n'a été calculé) mais choisie d'après une information sur ces unités est le saut de partie. Il compose
  (E[max(1, e_g)] par génération) : **c'est le trou.**
- **Le trou, précisément.** La preuve exige que chaque partie soit une e-valeur **conditionnelle au passé de toute la
  course** : c'est le texte de la v7 (D-S25 bis (5)) et du docstring de `Course`. La v9 et le code ne refusent que
  l'intersection **avec les unités déjà lues par la même fiche**. Une unité lue par une autre fiche à une génération
  antérieure n'est plus fraîche pour la course. Mesuré par la chaîne G : copie renommée (acceptée par `Lignees`), copie
  lisant la tranche g + 1 en génération g (fraîche pour elle), fiche non lancée quand la copie a trouvé la tranche
  défavorable (déclaration vraie, journal propre, `verifier_sans_partie` l'accepte). On obtient **0,087 (10 générations)
  et 0,626 (30 générations)** d'au moins une fausse promotion, contre 0,025 et 0,024 en honnête (1 000 courses par
  case). La démonstration, elle, respecte la condition, puisque toutes les fiches lisent la tranche g en génération g.
- **Mesure positive** : sur 250 courses de la démonstration (4 et 10 générations), il y a **0 promotion d'espérance
  conditionnelle ≤ 0**, et le taux de fausses découvertes est 0,011 et 0,021 au sens de la population (section D).

### Q4 — Code contre texte, et l'étiquette d'ordre

- **Identifiants** (banque, partie, unité) : rendus par `evaluer`, obligatoires dans `Course`, intersection refusée par
  fiche ; `parties_sans_identite` tracées. Conforme à la v9, mais par fiche seulement (K9-1). L'empreinte de banque dans
  l'identifiant rend deux banques voisines disjointes (K9-2).
- **`Lignees`** refuse qu'une clé ait deux fiches, mais pas qu'une fiche ait deux clés (A2). La clé contient les noms des
  contrastes (A3). Le journal est volontaire et `verifier_sans_partie` est un appel séparé (A5).
- **`evaluer(unites, etiquette_ordre)`** : le choix de la tranche et de l'étiquette est libre, sans trace, et l'appel
  peut se répéter (A7). **L'étiquette est-elle empêchée d'être choisie après coup ? Non**, ni par le texte (la v9 ne
  parle ni de tranches ni d'étiquette), ni par le code. L'issue finale est la même à l'ordre près (A7), mais le
  **franchissement** du seuil dépend de l'ordre. Essayer K ordres sous le nul, à une fiche seule de seuil 20, donne
  0,03 / 0,145 / 0,535 / 0,91 pour K = 1 / 10 / 100 / 1 000 sur 160 unités à v = ±0,5 (B1). Par l'interface, sur le
  contraste jumeau de la démonstration, cela donne 0,19 → 0,28 sur 160 unités et 0,03 → 0,04 sur une tranche de 40 (B2).
  La démonstration fixe l'étiquette à « empreinte de l'engagement | génération ». **C'est assez comme règle**, si elle
  est fixée avant toute issue et appliquée. Mais elle n'est écrite que dans le code de la démonstration : le LISEZMOI
  v27 la dit « facultative ». Ce n'est donc pas dit (K9-5).

### Q5 — La démonstration

- **Reproduite** : `banque.json` `2a24a36f…` et `course.json` `5c5098ea…` sont identiques à l'octet. Ma lecture diffère
  seulement par `--nul 50` (0 sur 50, Wilson [0 ; 0,071]) et par le dossier. Un essai antérieur de l'auteur
  (`demo-pari-essai1`, dans le dossier de travail de la session) ne diffère de la version publiée que par la règle
  d'abandon des témoins et par nul = 20. Les promotions sont les mêmes, sans sélection d'un résultat favorable (R4).
- **Ce qui se relit** : L1 tenue ; témoins promus aux décalages 1,2 et 1,0 (génération 1), 0,5 (génération 2) et 0,8
  « concentré » (génération 4) ; 0,1 non promu ; G1 promue en génération 3 avec log e 6,62 pour un seuil de 7,02
  = log 1 120 = log(14 · 4/0,05) ; plus faible : `dernier_etat` ; nul × 200 : 0 promotion. **Mais** aucun témoin
  n'atteint son seuil de fiche seule. La seule fiche au seuil de Bonferroni est `hasard-g2-3`. Toutes les « dents »
  viennent de la mise en commun e-BH : à budgets inchangés, le témoin concentré exige k* ≥ 8, et sans les fiches
  « hasard » il ne reste que 4 promotions (H).
- **« Signe connu »** : juste en population, pour des paires ±1 à seuil commun. **Faux conditionnellement aux seuils
  scellés** : jumeaux (moyenne |E| 0,041, 90e centile 0,088, maximum 0,142, positifs dans 52 % des banques), « tenu »
  de signe nul ou négatif dans 27 % des banques (C). Le docstring est faux en général, hors paires : avec {blanc : 0,5,
  juge : 0,5, cascade : −1}, Σ a·décalage = −0,10, mais l'espérance vaut +0,006 au seuil vrai (C, rappels) (K9-7).
- **Fiches « hasard » promues** : cohérentes. Ce sont des vraies par construction, et 0 est fausse conditionnellement
  sur 250 courses. Mais **7 affirmations sont portées par deux fiches**, dont 3 paires promues ensemble (fort et g1-3,
  faible et g2-3, g3-1 et g3-2) : 12 promotions pour 9 affirmations (A3b) (K9-3).
- **Lectures trompeuses** : K9-7, K9-8 ; « écart 0,5 » est un décalage de loi, environ 14 points de rappel, pas 50
  (K9-10).

## 3. Constats, du plus grave au moins grave

### Touche la garantie

**K9-1 — La fraîcheur est vérifiée par fiche ; la preuve la demande par rapport à toute la course.**
- **Où.** v9 D-S25 bis (5) : « toute intersection avec les unités déjà lues **par la fiche** est refusée ».
  `Course.ajouter_trajectoire` utilise `unites_lues[fiche]`. La règle « exactement une partie ou une déclaration » ne
  dit pas que la décision de ne pas lire doit être prévisible.
- **Problème.** Une unité lue par une fiche à la génération g′ < g n'est plus fraîche pour la course à la génération g.
  Une déclaration « fiche non lancée », vraie mais choisie d'après cette lecture, reproduit le saut de partie. Mesuré,
  toutes gardes de la version 27 passées : **0,087 / 0,626 contre 0,025 / 0,024** (G, 1 000 courses).
- **Correction.**
  - Texte : « une unité n'est lue qu'**à la génération de sa première lecture par la course** (une tranche se partage
    entre fiches dans sa génération, jamais ensuite) ; toute décision de ne pas lire une partie (déclaration, fiche non
    lancée) est prise avant toute issue de la génération, d'aucune fiche ».
  - Code : un registre global unité → génération de première lecture dans `Course`, avec refus si une unité a été lue
    à une génération antérieure. Mieux, comme la v8 et la v9 le disent déjà : le monde calcule la partie de chaque
    fiche active sur la tranche et la remet à la course.

**K9-2 — Le lien fiche ↔ clé n'est tenu nulle part.**
- **Où.** `Lignees.entrer` vérifie seulement que la clé n'a pas d'autre propriétaire. `Course` ne reçoit pas la clé.
- **Problème.** Une fiche reçoit une partie de développement puis une d'épreuve, puis une partie à τ changé : toutes
  acceptées (A2). Une fiche reçoit aussi une partie sur une banque grandie d'une unité : 40 unités physiques communes,
  0 identifiant commun, acceptée (A4). K7-3 (« développement et épreuve n'ont plus la même clé ») et K8-1 (iv) ne sont
  donc fermées que dans la clé, pas dans la course.
- **Correction.** `Course.entrer(..., cles={fiche: empreinte_cle})`, et `ajouter_trajectoire` qui refuse un résultat
  dont `empreinte_cle` diffère. `Lignees` qui refuse une seconde clé pour une fiche. Des identifiants d'unité
  indépendants de la version de la banque (source, unité), la banque restant au manifeste.

**K9-3 — La clé contient des noms libres ; « une affirmation, une fiche » se contourne par renommage, et le
rembourrage par des vraies faciles abaisse la barre e-BH.**
- **Où.** `construire` : `contrastes` et `comparateurs` sont indexés par nom. La démonstration nomme chaque contraste
  comme sa fiche.
- **Problème.** Mêmes coefficients et autre nom donnent une autre clé, que `Lignees` accepte (A3). La démonstration
  publiée porte elle-même 7 affirmations par deux fiches (A3b), sans qu'aucune garde ne réagisse. Avec des copies ou
  des vraies faciles, k* grandit. Course synthétique, 14 nulles en génération 1, n vraies faciles par génération
  ensuite : au moins une nulle promue dans **0,01 / 0,10 / 0,735 / 1,0** des courses pour n = 6 / 30 / 200 / 1 000. Le
  taux par fiche reste ≤ 0,0022 (garanti). Le taux **par affirmation**, si les vraies sont des copies d'une seule,
  vaut 0,005 / 0,053 / 0,44 / 0,82 (E). La garantie porte sur les fiches, alors que le pôle affirme des affirmations.
- **Correction.**
  - Clé canonique : cellules et coefficients triés, comparateurs par cellule, sans nom ; refus d'une seconde fiche
    pour la même clé canonique.
  - Dire dans D-S25 bis (5) que la garantie est un taux **par fiche promue**, et que ce qui sort du pôle se lit par
    e-Bonferroni (D-S25 bis (6)), seule lecture insensible au rembourrage.

**K9-4 — K8-4 est annoncée codée et ne l'est pas ; un essai annoncé manque.**
- **Où.** v9 verdict 4 (« version 26 ») et § 3 (« version 27 ») ; `construire` : 11 champs (A1).
- **Correction.** Ajouter `"e_processus": {"combinaison": "moyenne sur Λ", "arret": "premier franchissement de 1/b_i",
  "module": "pari_apparie", "version": 27}` à la clé, avec l'essai « Λ ou règle changées ⇒ clé changée ». Corriger la
  v9 (une seule version citée).

### Garantie sous obligation non écrite

**K9-5 — Tranche et étiquette d'ordre libres, absentes du texte.**
- **Où.** `evaluer(monde, engagement, unites=None, etiquette_ordre=None)` ; la v9 ne contient ni « tranche » ni
  « étiquette ».
- **Problème.** Évaluer plusieurs fois et garder la meilleure tranche ou le meilleur ordre est une partie calculée et
  sautée que ni la `Course` (les unités sont les mêmes, donc une seule partie est ajoutable) ni le journal ne voient.
  Choisir l'ordre après coup fait passer le franchissement de 0,03 à 0,535 pour 100 ordres essayés (B1), et de 0,19 à
  0,28 par l'interface (B2).
- **Correction.**
  - Texte (D-S25 bis (5)) : « le plan des tranches, unités par génération, est scellé avec l'engagement ou dérivé par
    le noyau de sa graine et des identifiants, jamais des scores ; l'ordre d'une tranche est dérivé de l'empreinte de
    l'engagement et de la génération ; une seule évaluation par fiche et par génération ».
  - Code : `evaluer(..., generation=g)` dérive l'étiquette et la tranche, et n'accepte plus de chaîne libre.

**K9-6 — Le journal des parties est tenu par celui qu'il doit contrôler.**
- **Où.** `Lignees.journaliser` est appelé par l'orchestrateur. `evaluer` ne journalise pas. `verifier_sans_partie` est
  hors de `Course.lire`, et son numéro de génération est libre.
- **Problème.** Une partie calculée non journalisée, puis une déclaration mensongère : acceptée. Cinq évaluations d'une
  même fiche dans une génération : rien ne les refuse (A5). La v9 dit « le monde journalise » ; le code ne le fait pas.
- **Correction.** `evaluer` (ou le monde) journalise lui-même. La `Course` reçoit le journal et refuse à la lecture :
  une déclaration contredite, plus d'une évaluation par (fiche, génération), une partie ajoutée dont l'empreinte
  d'unités n'est pas au journal.

### Lectures trompeuses de la démonstration

**K9-7 — « Signe connu par construction » est faux là où la garantie porte, conditionnellement aux seuils scellés.**
- **Où.** `esperance_connue` ; L1 du LISEZMOI v27 ; `test_esperance_connue`.
- **Problème.** Deux cellules de même loi, calibrées sur 60 unités de 8 épisodes honnêtes à τ = 5 % (effet d'unité
  partagé), ont des seuils scellés différents. Les jumeaux diffèrent en moyenne de 4,1 points de rappel, jusqu'à
  14 points (C). Dans la banque publiée, « faux nul » vaut +0,035 (vrai conditionnellement : log e 1,95 → 3,38) et
  « vrai tenu » vaut +0,0001. En courses répétées, L1 se lit « rompue » dans 13,5 % des cas (4 générations) et 34 %
  (10 générations), « faux nul » est promu dans 10 % et 18 %, et **aucune** de ces promotions n'est fausse
  conditionnellement (D). L1 mesure le bruit de calibrage (contrôle 12), pas la garantie. Le jumeau seul, lu sur
  160 unités à seuil 20, est promu dans 19 % des banques (B2, K = 1) : c'est « calibrage insuffisant » au sens du pari v2.
- **Correction.** Vérité de L1 = espérance conditionnelle aux seuils scellés (calculable dans un monde synthétique,
  section C du script). Le témoin « faux nul » est rapporté comme contrôle 12 (« calibrage insuffisant » s'il est promu),
  pas comme une violation. Le docstring est restreint aux paires ±1.

**K9-8 — « G1 promue en génération 3 » n'est pas la lecture de G1.**
- **Où.** LISEZMOI v27 et LISEZMOI de la démonstration ; `lecture()` L3.
- **Problème.**
  - G1 est lue une fois, hors de la suite, à m/α de sa famille de porte (v6 verdict 4 ; N-050 ; D-S10). Ce qui sort du
    pôle se lit par e-Bonferroni (D-S25 bis (6)).
  - La fiche « G1 » de la démonstration est lue sur trois tranches, dans une famille de 14 fiches tirées au hasard. Elle
    est promue par k* ≥ 2 (b·E = 0,67) et ne passe pas Bonferroni : sorties de Bonferroni dans 16 % (4 générations) et
    6 % (10 générations) des courses, contre 94 % et 100 % de « promue » (D).
  - « Comparateur le plus faible : `dernier_etat` » est du bruit : conditionnellement 0,1368 contre 0,1367 pour la
    cascade, et en population la cascade est la plus faible (0,144 contre 0,169) (C, F).
- **Correction.** Nommer la fiche « fiche de forme G1, lue dans la course du pôle ». Rapporter e-Bonferroni comme règle
  de sortie à côté de chaque promotion, et le processus cumulé de chaque composante.

### Dimensionnement (D-S8 β, § 6)

**K9-9 — La table du pari v2 § 6 suppose des alertes indépendantes ; G1 (b) dépend de la discordance et du calibrage.**
- **Où.** v9 verdict 1 (β) et § 6 ; `simulation-dimensionnement-v2.py`, `puissance_parts(rho=0.0)` (l. 55-58).
- **Problème.** Pour le blanc contre la cascade sur les mêmes sondes, la variance par unité suit (discordance − écart²)/m.
  À 5 points d'écart et 10 % de discordance, elle est environ 5 fois moindre qu'avec des alertes indépendantes à 0,55
  contre 0,50 (0,0975 contre 0,4975 par épisode). En revanche, le bruit de seuil des jumeaux, de 4 points en moyenne ici, est du même ordre que l'écart
  attendu. La garde de la démonstration ne porte que sur un comparateur (`noir_action`).
- **Correction.** Poste de devis en (écart, discordance, taille du calibrage C) mesurés par la lecture pilote ; contrôle
  12 à la taille de calibrage de G1 ; une garde par comparateur dans l'intersection-union (le minimum sur les gardes).

### Mineurs

**K9-10.**
- (a) (α) : la composante rapportée est descriptive. La `Course` ne garde pas de processus cumulé par comparateur.
- (b) Abandon « avant partie » avec une tranche partagée : écrire « d'aucune fiche ». L'ordre de la démonstration
  contredit la lettre (Q3 (iii)).
- (c) Déclaration « sans partie » d'une fiche gelée, ou d'une fiche qui a sa partie : enregistrée sans contrôle (A6).
  Il faut la refuser ou la marquer.
- (d) `test_nul_repete` : `au_moins_une_bonferroni ≤ au_moins_une_promotion + 8` est toujours vrai avec 8 répétitions.
  L'essai ne teste rien.
- (e) « Écart 0,5 », « forces » : ce sont des décalages de loi. Dire « environ 14 points de rappel », comme v9 § 6 parle
  en points.
- (f) Le nul × 200 ne porte que sur le nul complet, où la règle e-BH est la plus conservatrice. Le cas mêlé (section D)
  en dit plus.

## 4. Décisions de la v9 : avis

| décision | avis |
|---|---|
| D-S8 réécrite (Lazar) | conforme à N-056 ; ajouter : composantes descriptives, garde par comparateur (K9-9, K9-10 a) |
| D-S25 bis précisée (0,85) | **0,6 tant que K9-1 n'est pas écrit** ; 0,85 tenable avec « fraîcheur par rapport à la course » et « décision de non-lecture prévisible » |
| D-S18 précisée (0,85) | juste au texte ; **non codée** (K9-4) |
| nœud 2, D-S29, D-S30 | conformes à N-056 (« lue, non confirmée ») |

## 5. Chiffres de la v9 et du LISEZMOI v27 contre leurs fichiers

| où | cité | fichier, valeur | verdict |
|---|---|---|---|
| v9 en-tête | v8 `3e9609fc…`, rapport v8 `b2edabeb…` ; K7-1, 2, 3, 5, 9, 10 fermés ; K8-1, K8-2 ; « deux phrases et une garde » | `sha256sum`, rapport v8 verdict | justes |
| v9 verdict 1 (β), § 6 | 0,63 à 60 ; 0,96 à 100 ; 0,88 à 250 ; 20 → 40, 10 → 100, 5 → 250 | `simulation-dimensionnement-v2-sortie.json` (`d07e43f9…`) : 0,628 ; 0,964 ; 0,876 ; 0,966 à 40 | justes (modèle indépendant, K9-9) |
| v9 verdict 3 | 0,396 / 0,978 | rapport v8 § 6 B | justes |
| v9 verdict 4, § 3 | « version de l'e-processus » dans la clé, « version 26 » puis « 27 » | `engagement_apparie.py` v27 : absent | **faux** (K9-4) |
| v9 verdict 4 | essai « Λ dans la clé » | absent | **faux** (K8-5) |
| v9 § 3 | signatures `ajouter_trajectoire(..., unites=None, sans_identite=False)`, `abandonner(..., unites, sans_identite)`, `("redite", fiche)`, `identifiants_unites` ; 262 essais | `pari_apparie.py` l. 276, 311, 317 ; `engagement_apparie.py` l. 105 ; 262 `def test_` en v26, par différence (273 en v27 moins les 11 du fichier nouveau ; essais étendus, aucune fonction ajoutée) | justes |
| LISEZMOI v27 | 273 essais | 273 `def test_` ; les trois fichiers ciblés : 38 essais passent | juste (essais entiers non relancés) |
| LISEZMOI v27 | L1, L2 (1,2 et 1,0 en g1, 0,5 en g2, 0,8 en g4, 0,1 non), G1 en g3 (6,62 / 7,02), `dernier_etat`, nul × 200 = 0 (Wilson [0 ; 0,019]) | `lecture-pari-apparie.json` `520af089…`, `course.json` `5c5098ea…` | justes (lectures : K9-7, K9-8) |
| LISEZMOI v27 | « ≈ 70 s » pour nul 200 ; « 185 s » pour les essais | 17 s pour nul 50 (cohérent) ; non relancés | plausibles |
| démonstration v27 | `banque.json` `2a24a36f…` | reproduite à l'identique | juste |

## 6. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4). Graines :
`numpy.random.SeedSequence(2026102809, spawn_key=(section, indice))` (R9). Les manifestes sont dans les sorties (version,
empreintes du code lu, durée). Une première exécution d'essai à REP = 8 (pour la mise au point du script) n'est pas
rendue. B1 a ensuite reçu une seconde loi, et E le taux par affirmation, avant l'exécution rendue. Durées : 136 s, 12 s
et moins d'1 s.

| fichier | SHA-256 |
|---|---|
| `contre-verification-pari-signe-v9.py` (sections A à F) | `237322b7ae56a18ca6c8671b2a375826a24fb5bde1493558e619d72f3d43e7f1` |
| `contre-verification-pari-signe-v9-sortie.json` (REP = 200) | `7af53ea8b5bf3dc8b8909caf0428d33870b7f87021da5bc833b3f8934e549a55` |
| `contre-verification-pari-signe-v9-chaine.py` (section G) | `ebcd9829fe70bd35481fdf075c6e655818cb3d826977bb8822ad67a11618d719` |
| `contre-verification-pari-signe-v9-chaine-sortie.json` (REP = 1 000) | `c537c013e55fe0f7dd1932a8659514d6c0291b8e6f3fc74bceca444a2ec8d7d9` |
| `contre-verification-pari-signe-v9-ebh-final.py` (section H) | `b6ce6be69781d045bb2e928692d863ec984f4404497a9f4221ce21b1e59ea272` |
| `contre-verification-pari-signe-v9-ebh-final-sortie.json` | `2dcf96c844159257f0da6cfc7187c9243a01246a1d382e8469277476685b6df7` |
| `demo-reproduite-nul50/` : `banque.json` `2a24a36f…`, `course.json` `5c5098ea…` (identiques aux publiées), `lecture-pari-apparie.json` | `3a89ec3cc3b2c89a9c1617f215ce9893b1c0f8ea777078f90e502492f99d2fc6` |
| `demo-reproduite-nul50-console.txt` | `7f4c191c1bd97150580c16e8b9996936e3f305e4995d75e5f5b6fda086a759dd` |

- **A** : (1) 11 champs, aucune version ; (2) une fiche, trois clés, acceptées par `Lignees` et la `Course` ; (3) clés
  différentes par le seul nom, relance acceptée ; même engagement refusé ; (3b) 7 doublons dans la démonstration ;
  (4) 40 unités physiques communes, 0 identifiant commun, acceptée ; engagement sur l'autre banque refusé par
  `evaluer` ; (5) mensonge non journalisé accepté, 5 évaluations sans refus, génération libre ; (6) redite tracée ;
  déclarations non contrôlées ; (7) étiquette et tranche libres, finale égale à l'ordre près.
- **B1** (200 répétitions) : v ∈ {±0,5}, 40 unités : 0,02 / 0,06 / 0,165 / 0,46 ; 160 unités : 0,03 / 0,145 / 0,535 /
  0,91 (K = 1 / 10 / 100 / 1 000) ; v ∈ {−0,25 ; 0 ; 0,25}, 160 unités : 0,01 / 0,02 / 0,10 / 0,20. **B2**
  (100 banques ; la reproduction d'`evaluer` est vérifiée) : 160 unités 0,19 / 0,24 / 0,28 ; 40 unités 0,03 / 0,03 / 0,04.
- **C** : seuils et espérances conditionnelles de la banque publiée (empreinte `7d6e95ac…`, celle de la lecture) ;
  200 banques de calibrage (jumeaux, « tenu ») ; 200 banques nulles, 21 paires (moyenne |E| 0,011, 90e centile 0,023).
- **D** : 200 courses à 4 générations et 50 à 10 générations (chiffres en K9-7, K9-8). **E** : 200 courses par n.
  **F** : composantes cumulées de G1 (cascade 9,94, dernier état 9,45, juge 18,46, noir par action 15,60, noir
  séquentiel 12,20). **G** : 1 000 courses par case. **H** : e-BH de l'état final (les k* nécessaires, avec et sans
  doublons ou fiches « hasard », à budgets inchangés).

**Limites.**
- Mondes synthétiques. La chaîne G et le rembourrage E sont mesurés sur des parties synthétiques passées à la `Course`
  du code ; les gardes de `Lignees` y sont appelées.
- `monde_banque_scores.py` n'a été relu que pour `seuil`, `parts` et `ordre_secret` (inchangé, `306c47df…`).
- Les 273 essais entiers n'ont pas été relancés (seulement les 38 ciblés).
- Le lien au cycle n'existe pas en code.

Pour reproduire, depuis ce dossier, avec `R=…/orchestrateur-pole-v7` :
```
REP=200  /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v9.py $R > contre-verification-pari-signe-v9-sortie.json
REP=1000 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v9-chaine.py $R > contre-verification-pari-signe-v9-chaine-sortie.json
/opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v9-ebh-final.py $R/.. > contre-verification-pari-signe-v9-ebh-final-sortie.json
```

## 7. Fichiers lus et empreintes SHA-256

Dossier `…/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`.
Tous sont conformes à leurs compagnons `.sha256`. Le code est conforme à `EMPREINTES-orchestrateur-pole-v7-v27.txt`
(`sha256sum -c … | grep -v ': OK$'` vide), elle-même conforme à son compagnon. Revérifié en fin de session : inchangé.

| fichier | SHA-256 |
|---|---|
| `…/pari-de-signe/conception-pari-de-signe-v9.md` | `aab37f630a1a310d1a4cebf35dac4c0cd6e53ebac327af5771ddaae101c0ceeb` |
| `…/pari-de-signe/conception-pari-de-signe-v8.md` | `3e9609fcaef05b539ed37065d229c7b46a86e9cbbfe79bb3e9b8233637b766f5` |
| `…/pari-de-signe/conception-pari-de-signe-v7.md` | `fb422cbc2614eee112d5a0b430f4827ead879102892a039f388110e942995819` |
| `…/pari-de-signe/conception-pari-de-signe-v6.md` | `f21982cdf3d73d8e2a90902c40453e55019911404410e5f351af3b14c8ff1475` |
| `…/pari-de-signe/conception-pari-de-signe-v5.md` (§ 2.4 bis, § 6) | `95af46e4b8f317685ccc8755d6e3d0447ba109fd8771a0139eb9470c2bca8f8c` |
| `…/pari-de-signe/conception-pari-de-signe-v2.md` (D-S8, § 6) | `9c39a73ddbf681270610e6a3552fd85045fae46ade21d8d38c77564b7b461e1a` |
| `…/pari-de-signe/simulation-dimensionnement-v2-sortie.json` (et le script, l. 40-58) | `d07e43f9702eabe93470ffee9f2124fdd18dfec1473ade225a8a6f9afafa33ea` |
| `…/pari-de-signe/noeuds-pour-lazar-v1.md` (l. 13-39) | `d9a6ff1b08d795456e036a20ea68752938f97c5b6b587adaf5a74b3aad3dc23a` |
| `…/../decision-N-056-noeuds-G1-bras-attaque-mesures-fortes-v1.md` | `6aac9746543cd05d0fc4fb89b32938d272e9b9723dab820d191cbb8297669eff` |
| `…/pari-de-signe/contre-lecture-v8/rapport-contre-lecture-pari-signe-v8.md` | `b2edabeb555f95c6571a2712ca2391ad81b3a28b27d77d594a6809e6ed45c638` |
| `…/pari-de-signe/contre-lecture-v7/rapport-contre-lecture-pari-signe-v7.md` (empreinte seulement) | `1e21163faf3ebd1f9afddb5f28c1bd6b90e6d2bd86c1bd099f9013fdbadb8860` |
| `…/orchestrateur-pole-v7/EMPREINTES-orchestrateur-pole-v7-v27.txt` | `e9ebf78fe9481d992db1cc5953d13479f5241d7ba63d93b8c19911543a18c6f2` |
| `…/orchestrateur-pole-v7/EMPREINTES-orchestrateur-pole-v7-v26.txt` | `1ad9218f66d3763989f8be89eed4fc7c158934d2d270bbd0cccd2a29831ca451` |
| `…/orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v26.md` | `2aaf74c0353273882b2822c03b99de47002e18c1c09f962fbd85b0c44e1d4dc8` |
| `…/orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v27.md` | `f0871a60ab4e208a924f6040bcd3e95b527c417df2ba6094ba0ede3d23d4ff4a` |
| `…/orchestrateur-pole-v7/pole/pari_apparie.py` (v26 = v27) | `d3a3107abcd6daaad1fd34f40e6a1c99242e3babbf3464e43f9fbd93493cb62a` |
| `…/orchestrateur-pole-v7/pole/engagement_apparie.py` (v27) | `800e20eb09796e003a4f18435efea02d4969049544940cad8a4cc0ca625a4382` |
| `…/orchestrateur-pole-v7/pole/monde_banque_scores.py` (parties) | `306c47df85bef6732159467a42d49738db341f5d3b86bc29d3908b7847bb449e` |
| `…/orchestrateur-pole-v7/demonstrations/demo_pari_apparie_v7.py` | `32461f832250ca1941382defc10a83496ffe01bb694970d1b083e023a5e0d717` |
| `…/orchestrateur-pole-v7/essais/test_v7_pari_apparie.py` (l. 230-320) | `c367a38eac4439e0e04fda8f467b70bf67cba81a1c698238ca14d64384c8a76e` |
| `…/orchestrateur-pole-v7/essais/test_v7_engagement_apparie.py` | `4f5a6aa44964efaddee59954d3177bd53b816c0f25d6c7b7f3267ed7bf3cf262` |
| `…/orchestrateur-pole-v7/essais/test_v7_demo_pari_apparie.py` | `603119618f69a7a79796d191c30389daf3ff40922b4ca14a9d65c37910e8e5c2` |
| `…/pari-de-signe/demonstration-v27/lecture-pari-apparie.json` | `520af08948a673f36ae22c4e6b2da75ba65c4b9690354b66b5fd9bc17a32a4d8` |
| `…/pari-de-signe/demonstration-v27/course.json` | `5c5098ea885eb137b1d2620952d2a3deead0b3c28eee5f2bb18cd214dddeeb70` |
| `…/pari-de-signe/demonstration-v27/LISEZMOI-demonstration-v27.md` | `b1a19559379d54725684ec6951463bd4395fc464020617daaa6dba2242b0d2c9` |

Empreinte de ce rapport : dans son compagnon `rapport-contre-lecture-pari-signe-v9.md.sha256` (un fichier ne peut pas
contenir sa propre empreinte). Heure de fin (lue sur `date -u` dans un appel séparé, juste avant cette ligne) :
mercredi 28 octobre 2026, **01:13:05 UTC**.
