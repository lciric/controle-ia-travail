# Proposition A — Tour III.2 : critique croisée de méthode

## 0. Conventions et état des pièces

- Pièces B et C reçues complètes (empreintes données, texte fermé par FIN-DE-CELLULE). Pièce D toujours non servie ; je n'en déduis rien.
- Statuts : tout chiffre tiré des pièces A, B1, B2, C1, C2 est RAPPORTÉ (je n'ai pas audité les PDF). Tout ce que j'avance ci-dessous sur la méthode est une analyse de ma part (HYPOTHÈSE quand elle porte sur un comportement attendu). Les chiffres que j'introduis sont illustratifs.
- Je critique B et C ; je ne les fusionne pas. Quand je m'appuie sur l'une pour critiquer l'autre, je le dis.
- Garde : tout reste au niveau des lois de probabilité ; aucune conduite d'agent.

---

## Sur la proposition B

### (a) Défauts de méthode

**B-a1. E1 ne teste pas ce que S3 affirme.** S3 dit : « décisif » et « inédit » sont interprétatifs par construction. Mais les témoins « mauvais » d'E1 portent tous un défaut **mécanique** (reformulation de Q1–Q7, antériorité inventée, prédiction sans signe, critère de mort absent, condition non mesurable). Aucun témoin ne porte un défaut d'**avantage décisif** ou de **nouveauté** à valeur connue. E1 mesure donc la jugeabilité de champs que B propose elle-même de confier au vérificateur de schéma. Si E1 « passe », H_B tombe sur un domaine qui n'est pas celui de S3 ; si E1 « échoue », on apprend que les juges font mal ce qu'un parseur fait — ce que le corollaire de B anticipe. Dans les deux issues, S3 reste intacte : E1 est jugeable mais non pertinente pour la supposition qu'elle prétend trancher.

**B-a2. E3 prend un verdict de lecteur pour une vérité de terrain.** La liste « libre » de B1 (agrégation sur les jetons, séquentialité, couches précoce/tardive, Mahalanobis, propositions d'expériences) est un verdict rendu **contre un seul papier**, en v5, par un seul sous-agent (RAPPORTÉ, B1 §3 et §5). En faire des « témoins libres » avec un seuil « faux renversement ≤ 10 % » **pénalise un vérificateur qui trouverait un occupant que B1 a manqué** — c'est-à-dire exactement ce qu'E3 est censée récompenser. Vrai par construction : un vérificateur qui recopie B1 obtient 100 % sur les deux listes. La seule vérité de terrain honnête dans E3 est la liste « occupé » (quatre affirmations retirées) ; la liste « libre » ne peut servir que comme « non réfuté à la date de B1 », sans seuil de faux renversement.

**B-a3. E2 et E6 : pseudo-réplication.** L'unité randomisée est la course (un bras = une course), mais l'intervalle à 95 % porte sur la fraction de fiches, traitées comme indépendantes. Les fiches d'une même course partagent proposeurs, graine, mémoire et dossier : la variance entre fiches sous-estime la variance entre courses. Avec n = 1 course par bras, « bras 1 − bras 3 ≥ 15 points, IC excluant 0 » n'est pas un test ; c'est une différence de deux réalisations. B signale le piège de puissance sur E2, pas celui-ci, qui est plus grave : l'IC est mal défini, pas seulement large.

**B-a4. Fuite instrument/évaluation entre E2 et E3.** La métrique d'E2 (« l'antériorité survit à E3 ») utilise le vérificateur d'E3 comme oracle. Si ce vérificateur est aussi celui qui rend « inédit » révocable dans la question (§5 point 4), le même instrument construit la note et évalue la règle de couplage. Il faut un vérificateur d'E2 distinct de celui qui notera les vraies fiches.

**B-a5. E4 extrapole d'un régime flagrant à un régime diffus.** E4 est posée à dose flagrante, famille (i). Une issue H_B (« ne dépasse pas le plancher ») n'autorise pas la conclusion « l'axe 1 doit viser l'organisme, la taille ou la boîte noire et non l'architecture des sondes » : une architecture qui lit tous les jetons peut, par hypothèse, séparer là où le dernier jeton ne sépare pas. E4 est un préalable au sens « existe-t-il un signal lisible quelque part », pas au sens « l'architecture est hors sujet ». La conclusion attachée à H_B est plus large que ce que l'expérience peut falsifier.

**B-a6. E5 est vraie par construction tant que l'effet simulé est libre.** La puissance d'une simulation dépend d'un effet prédéclaré choisi par le programme. B ne lie pas cet effet à une mesure (par exemple la première des six mesures gratuites du front B, pièce A, qui estime l'hétérogénéité honnête — RAPPORTÉ). Sans cet ancrage, H_A (« puissance ≥ 0,8 ») est atteignable en choisissant l'effet, et H_B n'est jamais mise en danger.

**B-a7. Le critère de mort de la course est logiquement mal formé.** « Déclarer stérile si les trois conditions sont réunies : aucune fiche… ; **ou** toutes les fiches… ; la vérification externe… ». Une conjonction de trois clauses dont la deuxième commence par « ou » n'a pas une seule lecture. Au sens de §3 de la question-mère, ce critère est non jugeable tel quel.

**B-a8. Le « classifieur de statistiques de surface » n'est pas un comparateur, c'est une covariable.** Si la dégradation diffuse déplace légitimement la loi de la longueur ou du nombre de citations, le battre devient soit impossible (la surface porte vraiment le signal) soit trivial (elle ne le porte pas). Il contrôle l'artefact de source de Q6 seulement si la sonde est évaluée **à surface appariée** (stratification), pas si la surface est un adversaire à dépasser.

**B-a9. Livrable.** B ne rend pas le texte de question demandé ; elle rend des contraintes. Au recoupement, un élément n'est « commun » que s'il porte « le même livrable exigé de la fiche, même critère de juge ». Des contraintes sans livrable opérationnel seront difficilement comptées « communes », quelle que soit leur justesse.

### (b) Conditions mesurables de perte de puissance ou de jugeabilité

- **κ de Cohen (E1)** : perd son sens quand la prévalence des fiches défectueuses dans le lot est proche de 0 ou de 1 (paradoxe du κ : accord observé élevé, κ bas). Un lot témoin équilibré 50/50 n'est pas représentatif des vraies fiches ; un lot représentatif rend κ non informatif. Il faut rapporter l'accord brut **et** κ, avec la prévalence.
- **Taux de bascule sous paraphrase (E1)** : nul si les paraphrases conservent les marqueurs lexicaux auxquels les juges réagissent. Condition de jugeabilité : la loi des marqueurs de surface sous paraphrase doit différer mesurablement de la loi originale (distance lexicale rapportée), sinon « bascule ≤ 10 % » ne distingue pas H_A de « paraphrase insuffisante ».
- **Renversement (E3)** : sous-estimé si le rappel du vérificateur ouvert est bas (moisson arXiv/OpenAlex « quand elle existera », RAPPORTÉ). Sans estimation du rappel du vérificateur sur des occupants connus **hors B1**, un faible taux de renversement est compatible avec H_B.
- **E4, borne basse vs quantile 0,95 du plancher** : perd sa puissance (i) quand le nombre d'unités est petit (la borne basse descend sous le quantile même sous effet réel) ; (ii) quand l'hétérogénéité des épisodes honnêtes est élevée, puisque la pièce A rapporte un plafond de sensibilité sous hétérogénéité (RAPPORTÉ). Le quantile 0,95 d'un plancher estimé sur peu de sondes aléatoires est lui-même bruité ; son incertitude doit entrer dans le verdict.
- **E5** : le contrôle sous effet nul ne garantit le niveau nominal que si la famille de lois simulées inclut la dépendance entre actions. Si les scores sont simulés indépendants alors que les vrais sont autocorrélés, le taux de fausses conclusions « universalité tient » sous H0 est sous-estimé.
- **E6, plancher de bruit** : si l'échantillonnage des proposeurs est à température proche de zéro, deux exécutions « indépendantes » sont quasi identiques, le plancher tend vers 0, et toute distance g→g+1 paraît significative. Condition : rapporter la température et vérifier que le plancher est strictement positif.
- **E-valeurs « à tout instant » (c)** : la propriété de Ville ne tient que si le calibrage sous H0 utilise une loi honnête correctement spécifiée. Si le jeu honnête de calibrage est aussi celui qui fixe le seuil, le taux d'alerte à tout instant n'est plus borné. Condition mesurable : jeu de calibrage et jeu de seuil disjoints, et vérification empirique de la borne sur un troisième jeu honnête.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1 — test-retest sans paraphrase** : la même fiche servie deux fois au même juge. Sans ce plancher, le « taux de bascule sous paraphrase » confond instabilité du juge et sensibilité à la surface.
2. **E1 — fiche bien formée mais hors domaine** (tous champs mécaniques corrects, contenu sans rapport avec le contrôle des IA). Sans elle, on ne sait pas si le juge récompense la forme.
3. **E2 — bras à couplage prérempli aléatoirement** : le champ vis-à-vis est fourni, mais tiré au hasard dans un registre. Le placebo de B (« un champ de plus ») contrôle l'effort, pas le **contenu** du couplage ; ce contrôle-ci isole « coupler » de « coupler juste ».
4. **E3 — témoins à antériorité réelle mais mal attribuée** (bonne existence, mauvaise année ou mauvais auteurs). Sans eux, le vérificateur n'est mesuré que sur l'existence, pas sur la précision exigée par la règle 3.
5. **E4 — loi des activations sous consigne bénigne**. En plus de « rien de la condition à la position lue » (emprunté à B2 par B), il faut des épisodes honnêtes portant une consigne système non dégradante de longueur appariée. Duel : H_A « la sonde sépare dégradé/honnête mais pas consigne-bénigne/sans-consigne » contre H_B « elle sépare les deux » ; si H_B, la sonde lit la présence d'une consigne, et toute issue positive d'E4 est non interprétable. Son absence est fatale parce que l'autre contrôle (position lue) ne couvre pas la propagation de la consigne dans les activations hors de ces positions.
6. **E6 — redites paraphrasées**, pas seulement réinjectées. B les prévoit. Manque : des **fiches nouvelles plantées** dans g+1 à nouveauté connue, pour mesurer que la distance détecte la nouveauté, pas seulement qu'elle refuse la redite.

---

## Sur la proposition C

### (a) Défauts de méthode

**C-a1. Statuts élevés sans audit (règle 1).** C attribue « VÉRIFIÉ » à des contenus de pièces qu'elle n'a pas audités : « VÉRIFIÉ dans Pièce A » pour la non-lancée de la course, « VÉRIFIÉ, Pièce B1, p. 46 » pour 0,64/0,71, « VÉRIFIÉ, Pièce A, § 3.1 » pour le nul de P3, « VÉRIFIÉ, Pièce A, § 3.2 » pour « utilisabilité ≥ 99/100 » (qui est une **exigence**, pas un fait). Pour A, ces éléments sont RAPPORTÉS. Ce n'est pas un détail : le recoupement sert « à vérifier » toute antériorité non vérifiée sur PDF ; une fiche étiquetée VÉRIFIÉ par le proposeur risque d'échapper à cette règle.

**C-a2. Fuite construction/évaluation par TED-0.** TED-0 sert aux proposeurs « activations/scores par jeton et par action de la tranche 0 du pilote » et les 180 notations brutes des juges. Puis : (i) le critère de mort (iv)(b) teste les fiches promues **sur TED-0** ; (ii) la table (c), ligne 2, utilise « les 180 copies déjà notées » comme cas appariés pour calibrer le juge boîte noire. Le même matériau conçoit l'instrument et l'évalue. Il manque la déclaration que les épisodes de la tranche 0 sont exclus de toute banque de G1, et un jeu disjoint pour le test rapide.

**C-a3. Le gabarit universel rend M3 et M4 non notables par construction.** Le champ 6 impose « métrique principale : rappel à 1 % de FPR » et trois contrôles empiriques (plancher, sonde nulle, juge gradué) à **toute** fiche ; le critère de juge (ii)(3) vérifie leur présence. Une fiche M3 (théorème d'impossibilité) ou M4 (angle neuf) n'a ni rappel ni sonde nulle : soit elle est rejetée mécaniquement, soit elle remplit ces champs pour la forme — exactement les « fiches creuses » que l'axe 2 veut éviter. De même le champ 2 (couplage) est obligatoire dès g = 1 alors que M5 dit « pour g ≥ 2 » et que le registre des H_M est vide à g = 1 : contradiction interne.

**C-a4. Expérience 2 confond deux comparateurs et deux quantités d'information.** H_B regroupe « dernier jeton (iii) **ou** juge p2 » ; les deux issues falsifiantes ne distinguent pas lequel domine. Plus grave : une sonde par jeton est ajustée sur autant de vecteurs que de jetons, la base (iii) sur un vecteur par épisode. Si le séquentiel gagne, on ne sait pas si c'est l'agrégation ou la taille d'entraînement. Variable confondante non contrôlée.

**C-a5. Expérience 2 ne fixe pas le niveau auquel le 1 % de fausses alertes est tenu.** Un agrégateur séquentiel qui regarde à chaque action à seuil 1 % par action produit, sur un épisode de T actions sous H0, un taux d'alerte par épisode d'environ 1 − 0,99^T (illustratif : ≈ 26 % pour T = 30). Comparer à une lecture ponctuelle calibrée à 1 % par épisode n'est pas « ΔFPR ≤ 5 points » ; c'est deux grandeurs différentes. La question doit dire : FPR par épisode, à tout instant.

**C-a6. Expérience 3 conditionne sur un collisionneur.** L'analyse « per-protocol » sur les épisodes où l'oracle confirme le dommage sélectionne sur une variable **en aval** de l'exécution et, par hypothèse, corrélée à la force de la représentation interne. L'AUROC conditionnelle à 8B peut rejoindre celle de 70B par sélection, sans que m2 soit écartée. En outre, les fenêtres de décision laissent une zone non jugeable : τ_exec entre 0,40 et 0,80, ou AUROC entre 0,75 et 0,90 (chiffres illustratifs de C), n'ont pas d'issue déclarée.

**C-a7. Expérience 4, contrôle négatif vrai par construction.** « Injection d'un déplacement synthétique orthogonal à la direction de sonde » ne change pas le score d'une sonde linéaire, par définition du produit scalaire. Le contrôle ne peut pas échouer ; il ne teste rien. Et une corrélation de Spearman sur 10 moniteurs a un intervalle si large que « ρ < 0,3 » n'est ni significatif ni non significatif de façon stable.

**C-a8. Critères de juge non jugeables ou triviaux.** (6) « distance cosinus > 0,30 avec Q1–Q7 » : l'embedder n'est pas nommé ; deux embedders donnent deux verdicts ; et une reformulation lexicale suffit à passer tandis qu'une question réellement différente énoncée dans le vocabulaire commun échoue. (7) « compilation du squelette Lean 4 » : un squelette compile avec `sorry` ; sans interdiction explicite, c'est vrai par construction. Champ 7 « distance lexicale **et opérationnelle** vérifiée » : « opérationnelle » exige une interprétation (§3 : non jugeable). (5) « absence de mots de la liste d'exclusion » : filtre lexical — perte par synonymie, faux rejets sur le vocabulaire légitime de théorie de la détection (le mot « déplacement » lui-même).

**C-a9. Compteur de convergence (table, ligne 5).** « Faux arrêts (arrêt à g = 1 alors que des hypothèses de la carte restent non couvertes) = 0 » suppose que le compteur voit la carte des hypothèses, que la question-mère interdit de servir. Soit la mesure est impossible, soit elle fuit la carte. Et « = 0 » n'est pas un taux mesurable, c'est une absence sur un petit nombre.

**C-a10. Chiffre mal conditionné dans le texte de course.** M1 dit « HELIOS chute à 0,64 sur 20B » ; B1 et B2 rapportent que cette moyenne TRANSFER du 20B porte sur trois familles sur six (RAPPORTÉ). Servir le chiffre sans sa condition fabrique une cible facile.

### (b) Conditions mesurables de perte de puissance ou de jugeabilité

- **TPR@1 % FPR sur ~300 unités** : le seuil est le quantile empirique 0,99 des honnêtes réservés ; à n_h = 300, il repose sur ~3 dépassements (illustratif) et sa variance domine la comparaison. « ΔFPR ≤ 5 points » est mesurable (écart-type d'une proportion de 1 % à n = 300 ≈ 0,6 point, illustratif), mais le **rappel au seuil** ne l'est pas finement. Condition : rapporter l'IC du seuil, ou calibrer sur un jeu honnête plus grand que celui de test.
- **Oracle de dommage sous effet diffus** : si l'effet par action est faible, la probabilité que la référence cachée révèle un dommage **par épisode** peut être basse ; le sous-ensemble « dommage confirmé » de l'expérience 3 devient petit ou vide → non jugeable. Condition : sensibilité de l'oracle mesurée **par dose**, pas seulement sur dégradations plantées flagrantes.
- **Progression monotone p0 ≤ p1 ≤ p2** : si les exemples hors famille ne portent aucune information transférable, p2 = p1 est l'issue correcte ; la règle la lit comme défaut du juge. Condition : la monotonie n'est exigible que sur des cas témoins à information transférable connue.
- **Distance cosinus (critères 6 et D_nov)** : perd sa puissance si l'espace d'embedding compresse le vocabulaire du domaine (toutes les fiches proches). Condition : rapporter la distribution des distances entre fiches **aléatoirement appariées** d'une même génération ; un seuil fixe sans cette référence est non jugeable.
- **Vérificateur exact de chaînes dans les 23 PDF** : perd sa puissance si une fiche cite une page exacte avec un chiffre voisin (précision) ou si HELIOS n'est pas dans les 23 (B le note aussi). Condition : fraction de citations vérifiables et taux de faux positifs mesurés sur citations plantées.
- **Expérience 1, T_val et D_nov** : une course par bras ; sous variance entre courses non estimée, « +0,15 » est indéterminé. Condition : au moins deux exécutions par bras pour estimer cette variance.
- **Critère de mort (iv)(a) « moins de 3 fiches franchissent la grille »** : dépend du nombre total de fiches produites ; à budget réduit (26,40 USD par génération, illustratif selon C), le seuil absolu est atteint ou manqué par le volume, pas par la qualité.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Écart de généralisation TED-0 → tranche fraîche** : toute sonde ou tout agrégateur sélectionné sur TED-0 doit être rapporté sur une tranche honnête/dégradée disjointe. Duel : H_A « écart de rappel ≤ seuil scellé » contre H_B « > seuil » ; si H_B, la sélection sur TED-0 a surajusté et le critère de mort (iv)(b) est non interprétable. Sans ce contrôle, C-a2 n'est pas réparable.
2. **Comparateur (iii) à information appariée** : la base « dernier jeton » ajustée avec le même nombre de vecteurs d'entraînement que la sonde par jeton (par rééchantillonnage ou par réduction de celle-ci). Sans lui, l'expérience 2 ne peut attribuer un gain à l'agrégation.
3. **FPR à tout instant sous H0** : sur des trajectoires honnêtes réservées, le taux d'alerte par épisode de l'agrégateur séquentiel, tenu au même niveau que la lecture ponctuelle. Sans lui, « ΔFPR ≤ 5 points » compare deux grandeurs.
4. **Expérience 4 — déplacement synthétique d'énergie appariée en direction aléatoire** (pas orthogonal à la sonde). C'est le contrôle qui peut échouer ; l'orthogonal ne le peut pas.
5. **Expérience 3 — contrôle de sélection** : rapporter l'AUROC « tous épisodes » et « confirmés » à 70B, où τ_exec est attendu haut ; si l'écart entre les deux est déjà grand à 70B, le per-protocol gonfle et la lecture à 8B est inutilisable.
6. **Consigne bénigne appariée** (même contrôle que pour B, point 5) : indispensable à l'expérience 3 famille (i), que C ne prévoit pas ; le contrôle « invite identique octet pour octet » ne couvre pas les activations hors positions lues.
7. **Juge figé — fiches Lean avec `sorry`, citations à page juste et chiffre faux, fiches lexicalement distantes de Q1–Q7 mais opérationnellement identiques** (rééchantillonnage de vocabulaire). Sans ces trois témoins, les critères (2), (6), (7) sont acceptés sur parole.
8. **Mémoire — redites paraphrasées** (C ne plante que des identifiants brouillés). Une mémoire qui refuse les identifiants brouillés et accepte les paraphrases n'empêche rien.

---

## Note de symétrie

Deux défauts que je relève chez B et C s'appliquent probablement à ma propre conception du tour III.1 (que je ne vois pas ici) : le niveau auquel le 1 % de fausses alertes est tenu pour un agrégateur séquentiel, et le contrôle de consigne bénigne pour la famille (i). Je les signale pour que le recoupement les traite comme des exigences communes, pas comme des critiques de camp. Les antériorités citées par B (Cohen 1960 ; Page 1954 ; Ville 1939 ; Vovk, Gammerman, Shafer 2005) et par C (Wald 1945 ; Xie & Siegmund 2013 ; Ramdas et al. 2023) restent, pour moi, « référence à vérifier » : je ne les ai pas lues dans les pièces servies.

FIN-DE-CELLULE