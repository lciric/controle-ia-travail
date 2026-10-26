# Proposition B — Tour III.2 : équipe rouge croisée

**Statuts.** Le bloc FAITS est vide par décision de l'arbitre. Ce que dit le cadre de la question est RAPPORTÉ. Mes critiques sont des HYPOTHÈSES ou des calculs explicites. Les deux pièces A et C sont présentes et complètes : chacune se termine par sa ligne de clôture.

**Ambiguïté que les deux pièces tranchent sans base.** Le cadre dit : « par famille, 36 et 24 tâches par part ». Cette phrase admet deux lectures :
- la famille 1 compte 36 tâches par part et la famille 2 en compte 24 ;
- dans chaque famille, une part compte 36 tâches et l'autre 24.

A adopte la première lecture (« famille 1 (36 tâches) »). C va plus loin et attribue les 36 tâches à la conscience d'évaluation et les 24 au contrôle de délégation. Ce n'est écrit nulle part. Toute la puissance calculée par C sur « n = 60 par part » dépend de cette lecture non établie.

**Glissement de statut commun aux deux pièces.** Le cadre dit seulement : « chaque génération reçoit son score sur la part `test` ». Que ce score *nourrisse la réécriture* est une HYPOTHÈSE. C la marque RAPPORTÉ (« pour guider sa réécriture (RAPPORTÉ) »). A la traite comme acquise dans S5 et E4.

---

## Contre la proposition A

### (a) Failles

**A1. E1 est vrai par construction et ne mesure pas le bon canal.**
- On montre des scores à un agent neuf et on lui demande d'écrire des hypothèses signées. Qu'il suive le signe montré, y compris dans le bras inversé, est la consigne elle-même, pas une contamination. H_A est donc presque garantie.
- Le risque posé par l'arbitre porte sur un autre canal : les auteurs de l'étape 1 et de la confrontation, qui ne rédigent pas (b) mais peuvent le lire ou en être informés.
- L'inférence finale de A est fausse. Si H_B tenait (signe écrit indépendant des scores), l'option (2) ne deviendrait pas « acceptable » : elle deviendrait **inutile**, puisque son seul but est de faire dépendre les hypothèses des scores.
- Défaut de construction : dans le bras 0, aucun signe n'est montré, donc la « concordance » n'y est pas définie. La règle « bras 0 ± 0,2 » ne compare rien de défini.
- Avec k = 6 par bras, les concordances possibles valent 0, 1/6, …, 1. Le seuil 0,8 revient à « au moins 5 sur 6 », soit un seuil très grossier.

**A2. La règle d'audit de propreté de A ne peut jamais se déclencher.**
- A pose un déclenchement si p de permutation < 0,02.
- A établit lui-même que p minimal = 1/20 = 0,05 à 3 graines contre 3.
- Le déclencheur est donc mort par construction au budget décidé.
- Le second critère (variance entre graines < 0,3 × la variance binomiale, illustratif) a le défaut inverse (voir A3) : il peut se déclencher sur des courses honnêtes.

**A3. E2 confond deux variances, et ne peut pas les départager.**
- La variance binomiale √(p(1−p)/n) décrit l'incertitude due à l'échantillonnage des tâches.
- Or les graines sont évaluées sur les **mêmes** tâches. La variance entre graines sur un jeu fixe n'a aucune raison d'être comparée à la variance binomiale. Elle peut lui être très inférieure, par exemple si l'organisme est quasi déterministe tâche par tâche.
- Même en acceptant la comparaison, l'estimation n'a pas assez de degrés de liberté. Avec 3 graines par objet, en regroupant les deux objets, on a 4 degrés de liberté. L'intervalle à 95 % d'une variance s² s'étend alors de 4s²/11,14 ≈ 0,36 s² à 4s²/0,484 ≈ 8,3 s² (quantiles du χ² à 4 ddl), soit un rapport d'environ 23.
- Séparer 1,5× de 3× est donc impossible, pas seulement « en zone grise parfois ».
- Le contrôle négatif proposé (noter deux fois la même sortie) ne teste que le noteur. Il ne teste pas le non-déterminisme des appels aux modèles de langue au moment où l'organisme classe les tâches.

**A4. E4 est confondu par la sélection elle-même.**
- Même sans « exploiter » la récompense, un organisme qui choisit ses réécritures d'après le score sur `test` gonfle ce score par simple sélection sur le bruit (régression vers la moyenne).
- Un écart `test` − `test_final` qui croît plus pour v6.2.1 peut venir d'une recherche plus agressive ou plus variable, pas d'une exploitation de la récompense.
- Le contrôle « objet sans réécriture » n'est pas propre : v5.3 aussi se réécrit d'une génération à l'autre (RAPPORTÉ) et reçoit aussi son score sur `test`.
- Le différentiel mesure donc l'intensité de la sélection, pas le mécanisme.

**A5. L'ablation de E3 est un nouvel objet, écrit par une lignée exposée.**
- « v6.2.1 à réécriture désactivée » est une bonne idée de principe. Mais c'est du code nouveau, écrit vraisemblablement par la lignée B, qui écrit aussi la confrontation.
- Désactiver la réécriture de la règle de récompense peut casser autre chose : chemins de code, longueur des prompts, coûts.
- Sans contrôle de cette ablation elle-même (voir (c)), E3 compare encore deux objets qui diffèrent sur plusieurs facteurs.

**A6. La règle de falsification de H_A dans E3 est fragile.**
- « Une course contrôle dépasse la meilleure course v6.2.1 » peut arriver alors que l'effet vrai vaut 0,20.
- Indicateur : pour une seule paire de courses, avec un écart vrai de 0,20 et σ_course de 0,10 à 0,125 (bornes rapportées pour une différence, utilisées ici comme ordre de grandeur, illustratif), P(contrôle > v6.2.1) = Φ(−0,20/(σ√2)), soit environ 0,08 à 0,13.
- H_A peut donc être « falsifiée » à tort avec une probabilité non négligeable. A ne chiffre pas ce taux.
- La zone non tranchée 0–0,20 est déclarée, ce qui est honnête. Mais sur cette zone, aucune issue ne falsifie rien : E3 ne respecte la règle B4 que hors de cette zone.

**A7. D5 et D6 : chiffres à corriger.**
- **D6.** A écrit « 8 courses = 360 USD, sous le pire cas rapporté ». Ce calcul utilise le coût *attendu* par course (45 USD). Au coût *pire* par course (450/6 = 75 USD), 8 courses font 600 USD, au-dessus du pire cas rapporté de 450 USD.
- **D5.** « Conclure l'équivalence exige δ ≥ 0,3 » est un énoncé de puissance, pas une exigence. Avec une demi-largeur de 0,15 et un Δ̂ proche de 0, l'équivalence est concluable à δ = 0,2, mais rarement.
- **D5, suite.** De plus, z = 1,64 sous-estime le quantile à 4 ddl (t ≈ 2,13), ce qui rend la conclusion de A encore plus défavorable que ce qu'il écrit.

**A8. Un hachage prouve « quoi et quand », jamais « qui ne savait pas ».**
- A présente le gain de (2') sur (2) comme « mécaniquement vérifiable (hachages successifs) ».
- L'horodatage montre que la section de la lignée B existait avant celle de l'agent neuf. Il ne montre pas que B ignorait les scores au moment de l'écrire, ni que le texte final n'a pas été choisi parmi plusieurs versions (voir l'évasion E-A1).

### (b) Scénarios d'évasion

**E-A1. Engagements multiples.** Un rédacteur adverse hache plusieurs versions de la section (b), par exemple une par signe plausible. Après les scores, il publie celle qui convient.
- Parade : un registre public unique à une seule entrée par expérience, écrit par un tiers.
- Coût de l'évasion : quasi nul.
- Le tableau (c) de A (« détection d'altération 100 % par construction ») ne voit rien : aucune version n'est altérée, une est choisie.

**E-A2. Faits mécaniques comme canal.**
- Durées, plantages, jetons consommés et longueur des réécritures sont corrélés au comportement de l'organisme (A le note lui-même en S2). Mais aucun instrument de A ne les borne.
- Un auteur qui voit qu'une course v6.2.1 a coûté deux fois plus, ou a planté en génération 3, en tire une information sur la performance.
- Coût de l'évasion : nul, l'information arrive passivement.

**E-A3. Levier du lanceur (S7 de A, que je reprends).**
- La lignée A lance tout ce qui dépense (RAPPORTÉ). Elle peut relancer une graine « plantée », ou classer en « défaillance technique » une course défavorable.
- La liste d'arrêt scellée ne protège que si chaque lancement est journalisé hors de sa portée.
- Coût de l'évasion : environ 45 à 75 USD par course supplémentaire (dérivé de 270 et 450 divisés par 6). Une relance est donc détectable par rapprochement du grand livre des dépenses avec le nombre de courses déclaré, à condition que ce rapprochement existe. A ne le propose pas.

**E-A4. Aveugle X/Y de D6.**
- Le coût et la durée de chaque course révèlent l'identité de l'objet : v6.2.1 réécrit en plus sa règle de récompense, donc son profil d'appels diffère vraisemblablement (HYPOTHÈSE).
- Le démasquage est alors de fait immédiat pour qui voit les factures.

**E-A5. Menu D1 : enveloppe à faible entropie.**
- L'index choisi parmi 3 jeux tient en log₂3 ≈ 1,6 bit.
- Si l'empreinte de l'enveloppe est publiée sans sel secret, il suffit de hacher les 3 contenus possibles pour savoir lequel a été choisi.
- Coût de l'évasion : quelques microsecondes de calcul.

**Toutes à la fois.** Un seul acteur ayant accès au disque des courses, aux factures et au droit de relancer :
- lit les journaux ;
- pousse un seuil de la confrontation dans le sens vu, ce que le diff montre comme une « clarification » ;
- relance une graine ;
- déclare un plantage.

Coût : une ou deux courses en plus, soit environ 45 à 150 USD (illustratif). Seuls trois éléments l'arrêtent : la séparation des privilèges (le noteur chiffre ses sorties vers une clé tenue par un tiers), le rapprochement dépenses/courses et un registre d'engagement unique. Aucun des trois n'est dans A.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Mesure de contamination sur les vrais auteurs, pas sur des agents jetables.** Faire le diff-audit des textes principaux gelés avant la fin du pilote 4, noté à l'aveugle de la chronologie. Sans lui, E1 ne dit rien du risque posé.
2. **Placebo de rétroaction pour E4.** Faire tourner une course où l'organisme reçoit un score `test` permuté (le score d'une autre génération ou d'un autre objet).
   - H_A : l'écart croissant vient de l'exploitation du signal réel.
   - H_B : il vient de la sélection sur le bruit, et réapparaît avec le placebo.
   - Chaque issue en falsifie une.
   - Sans ce placebo, E4 est confondu (voir A4).
3. **Contrôle de l'ablation.** Comparer v6.2.1 avec la réécriture remplacée par l'identité (la règle est « réécrite » en elle-même) à v6.2.1 avec réécriture désactivée. Si elles diffèrent, l'ablation a cassé autre chose.
4. **Course nulle v5.3 contre v5.3, avec son budget.** A la propose mais ne dit pas qu'elle coûte des courses en plus, hors des 270 USD. Sans elle, aucun Δ n'est interprétable faute de variance entre graines. Si elle est abandonnée faute de budget, (b) doit le déclarer comme limite.
5. **Canari dans `test_final`.** Placer des jetons uniques dans `test_final` et les rechercher dans le code réécrit et dans les journaux. A ne traite pas l'isolation du noyau face à un organisme qui réécrit sa propre récompense.

---

## Contre la proposition C

### (a) Failles

**C1. Statuts gonflés (règle d'intégrité n° 1).**
- C marque VÉRIFIÉ des calculs : quantiles de t, 1/20, √(2/4), « 2/4 niveau du hasard ». Avec un bloc FAITS vide, rien n'est VÉRIFIÉ au sens du protocole. Ce sont des calculs explicites.
- Plus grave : « 2/4 (niveau du hasard, VÉRIFIÉ) » est faux sur le fond. Les 4 sous-parts (2 familles × `test`/`test_final` d'une même course) sont corrélées, donc la loi de la concordance sous le hasard n'est pas binomiale(4, ½).
- Statuts inventés : « génération 0 » (absente du cadre, qui prévoit des rondes de conception puis 4 générations notées) et la répartition 36/24 par famille.

**C2. Les fourches restent ouvertes dans l'hypothèse « scellée » elle-même.**
- La métrique primaire de C laisse plusieurs choix non fixés :
  - « moyenne pondérée **ou** macro-moyenne Z-scorée » ;
  - « dernière génération **ou** agrégation des 4 générations fixée au protocole » ;
  - règle de décision avec un **ou** entre la séparation complète des rangs et « t > 2,132 ».
- Ce sont exactement les degrés de liberté que C décrit plus loin (Gelman & Loken). Le **ou** entre deux tests gonfle aussi α : deux voies de rejet valent plus que l'une seule.

**C3. Mauvais test de Welch.**
- Avec 3 contre 3 graines, Welch–Satterthwaite donne au plus 4 ddl (variances égales) et au moins 2. Le quantile unilatéral à 2 ddl vaut ≈ 2,92, pas 2,132.
- L'objet qui réécrit sa récompense est vraisemblablement plus variable (HYPOTHÈSE). Utiliser 2,132 rend alors le test trop permissif précisément dans le cas attendu.

**C4. Absence de preuve prise pour preuve d'absence.**
- C fixe un effet minimal d'intérêt δ_min = 0,05 mais un seuil de décision Δ ≥ 0,12. Puis il déclare « Falsification de H_A : Δ < 0,12 ou p ≥ 0,05 ».
- Avec les chiffres illustratifs de C (SE ≈ 0,065), si l'effet vrai vaut 0,10 (donc H_A vraie), P(Δ̂ ≥ 0,12) = P(Z ≥ 0,31) ≈ 0,38, avant même la condition de séparation des rangs.
- H_A, pourtant vraie, est donc « falsifiée » dans plus de 60 % des cas.
- La règle B4 exige que chaque issue falsifie quelque chose. Ici, l'une des issues n'est que « non significatif ».

**C5. Le contrôle « génération 0 » est faux par construction et presque toujours en alarme.**
- v6.2.1 et v5.3 sont des codes différents. Rien n'impose qu'ils soient « indistinguables » avant réécriture.
- Même s'ils l'étaient, avec SE ≈ 0,065 (chiffre de C, illustratif), P(|Δ̂| < 0,05) = P(|Z| < 0,77) ≈ 0,56. Le contrôle alarme donc environ 44 % du temps sur des objets égaux.
- Le contrôle « permuter les étiquettes des tâches ramène au hasard » est vrai par construction. Il teste le noteur, pas l'effet : utile, mais pas un contrôle négatif de l'hypothèse.

**C6. Le GLMM et l'appariement par tâche promettent plus qu'ils ne donnent.**
- L'appariement par tâche retire la variance de difficulté des tâches. Il ne réduit pas la variance entre graines, qui est l'unité d'inférence. « Réduit drastiquement » est donc une surpromesse.
- Un effet aléatoire `(1|objet:graine)` estimé sur 3 niveaux par objet est instable : ajustements singuliers probables.
- Un test de Wald qui puise sa puissance dans les 60 tâches redevient l'analyse par tâche anticonservatrice que C prétend éviter.

**C7. L'agrégation 1 + 3 graines repose sur une échangeabilité non garantie.**
- C note la condition « code identique à l'octet », c'est un apport réel. Mais les organismes appellent des modèles de langue externes, dont les versions, quotas et latences peuvent dériver entre (a) et (b) (HYPOTHÈSE).
- La course de (a) n'est donc pas une graine tirée dans les mêmes conditions.
- **Fourche cachée** : la décision « le code a-t-il changé ? » se prend *après* (a), au vu des faits mécaniques, qui sont corrélés à la performance. Si un plantage de v6.2.1 en (a) mène à une correction, l'agrégation tombe, et ce choix est conditionné par les données.
- Sans règle mécanique scellée (« agréger si et seulement si les empreintes du code et la liste des modèles appelés sont identiques »), le « gain de puissance de 21 % » est un chemin parmi plusieurs.
- Le chiffre lui-même est cohérent : 0,911 × 0,866 ≈ 0,79. Mais il hérite des 4 ddl du test de Student, que Welch ne garantit pas (voir C3).

**C8. La conception de la variance à l'aveugle fuit la moyenne.**
- Pour des réussites binaires, la variance vaut p(1−p)/n. Connaître la variance d'un objet donne |p − 0,5|, donc pratiquement son niveau d'exactitude dans la zone d'intérêt (p ≈ 0,75).
- « Centrer à moyenne nulle » n'efface pas cette information.
- Le masquage X/Y se lève par les coûts et les durées (même mécanisme que E-A4).
- Ce dessin transmet donc plus que « 0 bit sur qui gagne ».

**C9. L'expérience 2 de C ne peut rien falsifier.**
- Elle compare deux « pistes » (le signe fixé par le rasoir d'Ockham contre le signe lu dans (a)) sur **une seule** réalisation de (b). Celle des deux qui concorde le doit au hasard d'un tirage unique.
- Aucune issue ne départage H_A de H_B avec un taux d'erreur borné. B4 n'est pas respectée.

**C10. Superlatifs, prescription, chiffres inventés.**
- Superlatifs et affirmations trop fortes : « sécurité absolue », « gain massif », « strictement égale à 0 bit », « il est démontré qu'il faut fixer le MCID ». Ce dernier énoncé est attribué en bloc à deux références que C marque lui-même « à vérifier ».
- « C'est la seule voie qui… » et « ne devrait être choisie sous aucun critère d'intégrité » présentent une option comme *la* réponse, ce que l'arbitre exclut.
- Section (d) : les modèles nommés, les GPU, les 2 à 6 heures par course et les 500 à 1500 appels sont marqués illustratifs. Mais la conclusion « le goulot d'étranglement n'est donc pas le coût GPU » est tirée de ces chiffres inventés, comme si c'était un résultat.
- La « répartition par proportionnalité » du coût suppose des courses de même coût pour les deux objets, ce qui n'est pas établi.

### (b) Scénarios d'évasion

**E-C1. Forçage par énumération de l'enveloppe.**
- La fonction f(scores) → hypothèses est publique, déterministe et à sortie de faible entropie (signe × classe de taille par famille, quelques dizaines de sorties possibles).
- Publier l'empreinte SHA-256 de la sortie permet à n'importe qui de hacher les sorties possibles et de retrouver laquelle a été produite.
- Le « 0 bit » de C devient environ 6 bits (ordre de grandeur de C lui-même, illustratif) pour tout lecteur de l'empreinte.
- Coût de l'évasion : négligeable.
- Parade : un sel aléatoire long, tenu par une partie qui ne lit aucun texte principal, et ouvert seulement au descellement.

**E-C2. Canal d'existence.**
- Si f n'a pas pu s'exécuter (course de (a) plantée), l'enveloppe est absente ou porte « pas d'hypothèse » : 1 bit.
- Si l'option choisie déclenche un test d'équivalence au lieu d'un test de supériorité, et que cela change un paramètre opérationnel visible du lanceur (nombre de courses, ordre), l'information fuit par l'exécution.

**E-C3. Fourches de C2 exploitées.**
- L'analyste choisit, après (b), la pondération et l'agrégation des générations qui franchissent le seuil.
- Coût : nul.
- Non détectable par le contre-lecteur si le texte « scellé » contient déjà les deux variantes.

**E-C4. Échangeabilité (C7).**
- Un auteur qui a vu un plantage en (a) « corrige » v6.2.1 : l'agrégation est annulée et la graine défavorable sort de l'analyse.
- Coût : une correction de code, justifiable en apparence.

**E-C5. Noyau.** Le tableau de C exige TPR = 1,00 et FPR = 0,00. C'est invérifiable avec un nombre fini de sondes : l'exigence est vraie par déclaration, pas par mesure. Un organisme qui réécrit sa récompense et trouve un canal non sondé (variables d'environnement, cache du fournisseur) passe sans être vu.

**Toutes à la fois.** Le lanceur :
- lit l'empreinte non salée (E-C1), donc connaît le signe ;
- fait corriger le code s'il est défavorable (E-C4) ;
- choisit la pondération ensuite (E-C3).

Coût : une à deux courses en plus, soit environ 45 à 150 USD (illustratif), et aucune trace dans un diff de seuils gelés, puisque les seuils ne bougent pas : ce sont les fourches qui bougent.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Course nulle v5.3 contre v5.3.** Absente de C. Sans elle, ni le seuil 0,12 ni le δ_min de 0,05 ne sont calibrés : ils reposent sur un σ_graine inventé (0,057, illustratif).
2. **Ablation ou mention du confondant.** C conclut sur « la réécriture de la règle de récompense » à partir d'un contraste entre deux versions. Il faut soit l'ablation de A, soit restreindre la conclusion à « v6.2.1 contre v5.3 ». Sinon la conclusion porte sur un mécanisme non isolé.
3. **Test d'énumération de l'enveloppe** avant usage. Un agent neuf reçoit f et l'empreinte publiée, et doit ne pas retrouver le contenu. S'il le retrouve, l'option (2') scellée de C est invalide.
4. **Règle d'agrégation scellée et vérifiée mécaniquement** : empreinte du code, liste des modèles appelés, configuration identiques entre (a) et (b). Plus un contrôle de dérive : mêmes sondes fixes envoyées aux modèles appelés aux deux dates, avec un critère d'écart scellé.
5. **Placebo de rétroaction pour Γ.** Même argument que pour E4 de A : sans lui, « la réécriture produit un surapprentissage » n'est pas séparable d'une sélection plus intense sur le bruit.

---

## Une expérience que les deux pièces rendent nécessaire

Je me sers ici de S7 (A) et de l'enveloppe chiffrée (C), en le disant.

**Duel : l'isolement des scores résiste-t-il à un adversaire interne ?** Ici, H_A et H_B désignent des hypothèses, pas des propositions.

- **H_A** : avec un sel secret, le noteur chiffrant vers une clé tenue par un tiers, et un rapprochement des dépenses avec le nombre de courses, un agent rouge ayant les droits du lanceur ne retrouve pas le signe Δ du pilote 4 mieux que le hasard.
- **H_B** : il le retrouve par les canaux passifs (coûts, durées, plantages, longueurs de réécriture).
- **Dessin** :
  - k agents rouges (k = 10, illustratif) reçoivent tout ce que voit le lanceur, sauf les scores, et parient sur le signe par famille.
  - Bras contrôle : les mêmes données avec l'association entre faits mécaniques et étiquettes d'objets permutée.
- **Issues** :
  - si la concordance du bras réel dépasse celle du bras permuté au seuil scellé, H_A est falsifiée : les options (2), (2') et la piste agrégée de C fuient toutes par les faits mécaniques, et seule l'option (1) ou un lanceur sans accès aux faits mécaniques protège ;
  - sinon, H_B est falsifiée pour ces canaux, et le débat se réduit aux canaux textuels.
- **Limite** : avec deux courses en (a), le signal disponible est minuscule. Le bras permuté est indispensable pour que « au-dessus du hasard » ait un sens.

FIN-DE-CELLULE