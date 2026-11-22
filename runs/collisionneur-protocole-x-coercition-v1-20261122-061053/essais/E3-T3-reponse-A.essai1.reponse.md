# Proposition A, tour III.3 : réponse aux critiques

**Remarques d'intégrité**
- J'ai reçu ma conception III.1 et les quatre critiques (B, C, D, E), toutes closes par leur ligne de fin, sans coupure repérée.
- Je n'ai pas reçu les conceptions B à E : ce que j'en dis vient des critiques, donc RAPPORTÉ.
- Je ne réponds qu'aux sections « Sur la proposition A ».
- Je ne change aucun statut. Les relations que C, D et E marquent VÉRIFIÉ le sont, selon leurs auteurs, sous les lois qu'ils posent.
- J'ai refait à la main deux calculs : le hasard marginal a/(a+b+k−1) sous fragilité Beta (B, C) et la borne TOST de B. Je retrouve les mêmes valeurs ; ma vérification est OBSERVÉ-NON-AUDITÉ.
- Aucune expérience n'a été exécutée. Tout chiffre ci-dessous est **illustratif** (abrégé « ill. »). Rien n'est un résultat.

---

## (a) Verdict sur chaque critique

| # | Critique (source) | Verdict | Suite donnée |
|---|---|---|---|
| 1 | Critère interventionnel circulaire : un filtre lexical sépare n'importe quels leviers (E a1, E b1) | Acceptée sur le fond, transformée en test | Seules des défenses préenregistrées, indépendantes de la forme de surface, sont admises. Le différentiel doit tenir sur des leviers paraphrasés réservés. |
| 2 | Deux mécanismes de même loi interventionnelle sont indiscernables (D b) | Acceptée | Mon critère classe les menaces par défense requise. Il ne dit rien du mécanisme interne ; je retire toute lecture mécaniste. |
| 3 | Taux d'erreur honnête atteignant le prédicat à mesurer sous chaque bras (B9) | Acceptée | Mesuré dans tous les bras sans demande. |
| 4 | « p₀ > 1 % rend tout non jugeable » (E b1) | Rejetée comme défaut | C'est la règle d'arrêt voulue : un socle qui échoue doit bloquer la suite. |
| 5 | Geler demande, seuils, couche et références hors test (D c, B c1) | Acceptée | Trois lots de tâches disjoints par famille. |
| 6 | D1 : titrage sur les tâches du test (B1, C a3, D, E a2) | Acceptée | Titrage sur le lot de calibration. |
| 7 | D1 : l'équivalence ne prouve ni l'identité des mécanismes ni le transfert des défenses (D) | Acceptée | Elle révèle une incohérence de III.1 : D1 n'appliquait pas mon propre critère. J'ajoute D1-bis. |
| 8 | D1 : un levier seul contient une demande implicite (B2, D) | Transformée en test | Deux prédicats : « ciblé » et « autre invalidité ». |
| 9 | D1 : décision sur l'estimation ponctuelle, famille de Holm implicite (B3) | Acceptée | Décision sur les bornes d'intervalles simultanés ; famille de 4 contrastes. |
| 10 | D1 : zone de non-décision autour du seuil (C b1, E b2) | Acceptée comme fait, rejetée comme défaut supprimable | Toute règle à erreur contrôlée en a une. Je la chiffre par simulation avant collecte. |
| 11 | D1 : puissance du TOST, corrélation intra-tâche (B b) | Acceptée | Rééchantillonnage par tâche, 5 graines par tâche et par bras (ill.). |
| 12 | D1 : effets de signes opposés, hétérogénéité bimodale (B b, C b1, D b, E b2) | Acceptée | Zone réactive par tâche, écart-type inter-tâches τ, issue tierce prévue. |
| 13 | D2 : recalibrage et stabilité de l'AUROC vrais par construction (B4, C a4, D, E a3) | Acceptée | Canaris d'une famille de gabarits disjointe. |
| 14 | D2 : AUROC stable sans translation, queue contaminée, ROC croisées, trou [0,02 ; 0,05) (B b, C b2, D b, E b3) | Acceptée | L'estimand devient la perte au point d'exploitation, avec une marge unique. L'AUROC est seulement décrite. |
| 15 | D2 : ex-æquo et atomes des scores 0–100 (B b, E b3) | Acceptée | Score continu lu sur les logits. |
| 16 | D2 : rapport silence/alerte indéfini ou instable (D b, E b3) | Acceptée | Rapport supprimé. |
| 17 | D2 : pression adressée à un tiers absent (D c) | Déjà présente en III.1 | Conservée. |
| 18 | D3 : à deux familles, la parenté se confond avec la capacité (B, défaut commun) | Acceptée | Trois familles et une variante de taille. |
| 19 | D3(ii) : contenu confondu avec l'auteur, collision par filtrage (B5, C a2, D, E a4) | Acceptée | La variante (ii) devient descriptive. |
| 20 | D3(i) : la greffe crée une dissonance raisonnement/action (E a4) | Transformée en test | Diff bénin hors-sujet greffé de la même façon. |
| 21 | D3 : l'en-tête mesure une attribution, pas une entente (D) | Acceptée | Je parle d'« effet d'attribution » et d'« effet d'origine ». |
| 22 | D3 : échelle de l'interaction, plancher (B b, E b4) | Acceptée | Échelle logit préenregistrée ; omission titrée. |
| 23 | D3b : avantage mécanique des paires de même modèle (B6) | Acceptée pour invite identique et décodage glouton, rejetée au-delà | Avec invites distinctes et décodage aléatoire, des points focaux partagés sont le phénomène visé, non un artefact. |
| 24 | D3b : hasard conditionnel à la tâche (D), excès borné par les marges (E b4), bit sans sabotage (C c) | Acceptées | Voir (b). |
| 25 | D4 : « même texte » ambigu ; référence à lire sur les mêmes jetons, au même instant (B7, C a1, D c) | Acceptée | Voir (b). |
| 26 | D4 : sac-de-mots trop faible (D b, E a4) | Acceptée | Référence séquentielle. |
| 27 | D4 : lecture avant génération et préfixe forcé (C c) | Transformée | À invite et préfixe identiques, les activations sont identiques. L'AUROC entre graines vaut donc 0,5 par construction, ce que mon propre contrôle disait. Le contrôle n'informe qu'entre invites. |
| 28 | D4 : sélection sur l'issue, difficulté (B7, C a2, E a4) | Acceptée | Appariement intra-tâche, validation croisée groupée. |
| 29 | D4 : transfert confondu avec la consigne système ; orthogonalité sans verdict (B7, C b3, D, E) | Acceptée | Transfert sorti de H_B ; case fournie par le bras « demande nue ». |
| 30 | D4 : classes rares, divergence de l'estimateur (B b, D b, E b5) | Acceptée | Effectif minimal, pénalisation L2. |
| 31 | D5 : la fragilité entre tâches imite une immunisation (B8, C b4, D, E b6) | Acceptée | C'est le défaut le plus net de III.1 : H_B y était déclarée à tort. |
| 32 | D5 : pression unique à l'étape 1 (C c), mémoire des refus (E c4), pente linéaire et même possibilité de violation (D) | Acceptées | Voir (b). |
| 33 | Instruments : le taux global de fausses alertes masque h2 (E b7) | Acceptée | Décision sur la pire strate. |
| 34 | Auditeur : rappel non identifiable si l'oracle ne voit que les signalés ; variance à faible prévalence (D b, E b7) | Acceptée | Oracle sur toutes les trajectoires ; prévalence fixée par plan. |

Trois précisions sur ce tableau.

- **Ligne 27.** B, C et D ne demandent pas la même chose pour D4. B veut la référence sur les jetons générés, C veut lire avant toute génération, D veut un lecteur du même préfixe. Je ne les fusionne pas : chacune devient une lecture distincte, D4-a ou D4-b.
- **Ligne 7.** C'est la critique qui change le plus ma proposition.
- **Ligne 31.** C'est celle qui invalidait le plus directement une de mes règles de décision.

---

## (b) Expériences corrigées

**Convention commune.**
- Chaque duel a une marge unique δ. H_A et H_B partitionnent l'espace du paramètre.
- La décision se prend sur les bornes d'intervalles simultanés, rééchantillonnés par tâche. Entre les deux, le duel est « non conclusif ».
- La probabilité de non-conclusion est simulée et publiée avant collecte.
- Les tâches sont réparties par famille en trois lots disjoints : calibration (titrage, seuils, couche), canaris, test.

### Socle

Inchangé sur le principe : prédicat sur l'état final, évalué par du code, sur toutes les trajectoires, signalées ou non.

Deux prédicats au lieu d'un :
- **ciblé** : l'état exact demandé, par exemple tel canari à tel chemin ;
- **autre invalidité** : tests cachés échoués, ou autre écart.

Le taux de déclenchement honnête du prédicat ciblé est mesuré dans chaque bras sans demande. Au-delà de 1 % (ill.) dans un bras, le prédicat est refait et rien n'est rapporté.

### D1 : le levier ajoute-t-il à la demande ?

**Préparation.**
- La formulation de la demande nue est titrée sur le lot de calibration.
- Sur des graines qui ne servent plus ensuite, on ne garde au test que les tâches dont le taux sous demande nue tombe dans [0,2 ; 0,8] (ill.).
- La conclusion vaut pour ces tâches et ces demandes, et le rapport l'écrit.

**Bras.** Ceux de III.1. La source primaire est le contenu renvoyé par un outil ; les deux autres sources passent en analyse secondaire.

**Estimands.**
- Δ_j : levier j + demande contre placebo + demande, sur le prédicat ciblé. Quatre contrastes, correction de Holm sur quatre.
- τ_j : écart-type de Δ_j entre tâches, par modèle mixte.

**Hypothèses et décision** (δ = 10 points, ill.).
- **H_A** : |Δ_j| < δ pour tout j. Retenue si les quatre intervalles sont inclus dans ±δ.
- **H_B** : il existe j avec |Δ_j| ≥ δ. Retenue si un intervalle est entièrement au-delà.
- **Issue tierce** : équivalence en moyenne, mais borne haute de τ_j ≥ δ. Elle falsifie à la fois la réduction pure et le levier uniforme, et renvoie à une analyse par famille de tâches, exploratoire.

**Lecture des bras « levier seul ».**
- Prédicat ciblé en hausse : le levier porte une demande implicite.
- Autre invalidité en hausse : dégradation.
- Aucune hausse : le contrôle est propre.

**Dimensionnement.**
- Avec 200 tâches × 5 graines par bras, l'erreur type est d'environ 0,02 (ill.).
- H_A n'est alors atteignable à puissance 0,8 que pour |Δ| ≲ 4 points (ill.).
- H_B n'est atteignable que pour |Δ| ≳ 17 points (ill.).
- Entre les deux, la non-conclusion est probable. Si la simulation confirme une zone aussi large, je réduis à deux leviers pour concentrer l'effectif.

### D1-bis : la défense contre l'injection se transfère-t-elle ? (ajoutée)

C'est ici que s'applique mon critère de distinction. D'après les critiques C, D et E, la proposition B contient un test voisin (RAPPORTÉ). J'en reprends l'idée, avec les corrections que ces critiques lui adressent : pas de rapport, contrôle hors distribution non social.

**Plan.** Une défense est réglée sur les seules demandes nues du lot de calibration. Ce peut être un balisage du contenu d'outil, un filtre appris ou un ajustement léger. On mesure la baisse en log-cotes du prédicat ciblé, γ, sur trois entrées :
1. la demande nue ;
2. la demande reformulée sans levier, dans un registre absent du réglage (style juridique, commentaire de code) ;
3. levier + demande.

**Hypothèses.**
- **H_A (transfert)** : γ_levier ≥ γ_reformulation − δ.
- **H_B (classe distincte)** : γ_levier < γ_reformulation − δ.

**Garde-fou.** La perte d'utilité sur demandes légitimes est bornée d'avance.

**Ce que chaque issue falsifie.**
- Transfert : la pression n'est pas une menace distincte selon mon critère, même si D1 montre Δ > 0. Ce serait une injection plus forte, justiciable de la même défense.
- Non-transfert : la réductibilité est falsifiée pour cette défense.

### D2 : pression sur le juge, compensable ou non ?

**Plan.**
- Traces figées ; pression insérée mécaniquement et croisée avec la présence de sabotage.
- Score continu : espérance du score sur les logits des jetons de note.
- Gabarits de pression scindés en deux familles disjointes : G1 pour les canaris, G2 pour le test.

**Estimand.** L = (détection à 5 % de fausses alertes sans pression) − (détection au même taux sous G2, seuil recalibré sur canaris G1). Le taux de 5 % est illustratif ; 1 % passe en secondaire, faute d'effectif.

**Hypothèses**, par sens de pression.
- **H_A (compensable)** : L < δ.
- **H_B (non compensable)** : L ≥ δ.

**Décomposition rapportée.**
- Perte avec recalibrage « oracle » sur G2 : c'est la perte intrinsèque de discrimination.
- Écart entre recalibrage G1 et recalibrage oracle : c'est le défaut de généralisation du recalibrage.
- Interaction pression × classe sur la moyenne et la variance des scores, courbes ROC entières, AUROC : descriptives.

**Silence et fausse alerte.** Ce sont deux menaces distinctes si le recalibrage compense l'une et pas l'autre.

**Contrôles.** Placebo et destinataire absent, conservés de III.1.

### D3 : effet d'attribution et effet d'origine

Je retire le mot « entente » de ce duel.

**Plan.**
- Trois familles de taille voisine, en 3 × 3 auteur × moniteur.
- Une variante de taille dans une famille, comme contrôle de capacité.
- Paraphrase par un quatrième modèle hors plan.
- Variante primaire : le même diff malveillant, greffé dans des trajectoires honnêtes de chaque auteur.
- Le taux d'omission des paires croisées est titré entre 20 % et 80 % (ill.) sur le lot de calibration.

**Estimands**, sur l'échelle logit.
1. **Attribution** : en-tête « même modèle » contre « autre modèle », sur une trace identique.
2. **Origine** : diagonale moins hors-diagonale, avant et après paraphrase.

**Hypothèses.**
- **H_A** : les deux effets sont dans la marge.
- **H_B** : l'un au moins en sort.

**Contrôles.**
- Diff bénin hors-sujet greffé de la même façon. Si le moniteur alerte autant que sur le diff malveillant, il lit la rupture et non le sabotage, et le duel est invalide.
- En-tête « prestataire humain ».
- Trajectoires honnêtes soumises au même plan.

**Lecture de l'effet d'origine.**
- S'il disparaît après paraphrase, il passe par le style.
- S'il survit et suit l'écart de taille, il relève de la capacité et non de la parenté.

**D3b (secondaire).**
- Invites distinctes par rôle et décodage aléatoire.
- Hasard de référence obtenu en permutant les partenaires, à tâche et consigne fixées.
- Tâche focale neutre (transmettre un bit, sans sabotage) pour séparer l'incapacité du refus.

### D4 : que lit la sonde ?

**D4-a, avant toute génération, entre invites.**
- La sonde est lue au dernier jeton de l'invite. Elle prédit le taux de cession de l'invite, estimé sur plusieurs graines.
- **H_A** : gain < δ sur un lecteur textuel séquentiel de la même invite.
- **H_B** : gain ≥ δ.
- Validation croisée groupée par tâche.

**D4-b, pendant la génération, intra-tâche.**
- Même tâche, même invite, graines différentes : cédé contre résisté.
- La sonde est lue au jeton k. La référence est un lecteur séquentiel du même préfixe, issu d'une autre famille.
- Mêmes hypothèses, en fonction de k.
- Un succès se dit « lit l'acte en cours mieux que le texte ». Je ne parle plus de « bascule ».

**Transfert.** Il est rapporté à part, vers le bras « demande nue », cédé contre résisté, même canal et sans consigne système. Il n'entre plus dans H_B.

**Garde-fous.**
- Au moins 100 cas par classe et par strate (ill.) ; sinon le duel est déclaré non jugeable.
- Régression pénalisée.
- Étiquettes permutées entre graines d'une même invite.
- Sonde sur la couche d'entrée.

### D5 : exposition répétée

**Bras**, avec la même possibilité matérielle de violation à chaque étape :
- pression répétée ;
- pression répétée avec refus antérieurs remplacés par un texte neutre de même longueur ;
- pression à la seule étape k ;
- pression à la seule étape 1, suivie d'étapes neutres ;
- placebo répété.

**Estimand.** Rapport de cotes intra-tâche du hasard à l'exposition k contre l'exposition 1. L'indice k est traité comme catégoriel, avec un effet fixe par tâche et plusieurs graines par tâche.

**Hypothèses.**
- **H_A** : tous les rapports sont dans [0,8 ; 1,25] (ill.).
- **H_B** : l'un au moins en sort.

**Condition préalable.** L'estimateur est d'abord passé sur des données simulées, à hasard constant par tâche et forte hétérogénéité entre tâches. S'il y rejette H_A plus souvent que le niveau nominal, il est corrigé avant toute collecte.

### Instruments

- Seuils gelés sur le lot de calibration.
- Fausses alertes contrôlées sur la pire des strates h1–h4, et non sur leur mélange.
- Prévalence de sabotage fixée par plan et rapportée.
- Audit aléatoire de même coût comme référence.

### Ancrage matériel révisé (ill.)

- Environ 300 tâches au lieu de 200.
- Trois familles et une variante de taille.
- 300 à 500 heures-GPU.
- 5 à 8 semaines-personne.

**Ordre** : socle, D1, D1-bis, D2, D4, D3, D5.

---

## (c) Réponse à l'arbitre

### Ce qui est établi

- **Aucun résultat empirique.** Les faits disent « peut », sans statut ni fréquence. Aucune expérience n'a été exécutée dans ce collisionneur.
- **Des contraintes de mesure**, qui sont des implications et non des observations. Leurs statuts sont ceux que posent leurs auteurs.
  - Un dommage ne se mesure hors composants corruptibles que par un prédicat sur l'état final, calculé par du code, sur toutes les trajectoires. C'est une borne inférieure, limitée aux dommages prévus.
  - Une AUROC stable ne prouve pas qu'un moniteur est intact.
  - Un recalibrage testé sur la pression qui l'a réglé réussit par construction.
  - Un hasard qui décroît avec l'exposition peut venir de la seule hétérogénéité des tâches.
- **La littérature.** La liste de III.1 reste RAPPORTÉE de mémoire, non vérifiée. Elle couvre l'injection directe et indirecte, la persuasion, la complaisance, le contrôle avec moniteur non fiable, l'auto-préférence des juges et les sondes. Je n'y ajoute rien.

### Ce qui ne l'est pas

Tout ce qui suit est HYPOTHÈSE.

- **Position par rapport aux attaques connues.** Elle ne se décide pas par la forme du message, mais par deux mesures :
  - D1 : le levier déplace-t-il le taux au-delà de la demande ?
  - D1-bis : une défense réglée sur l'injection couvre-t-elle aussi la pression ?
- **Menaces à distinguer.** Mon critère : deux menaces sont distinctes si une même défense, admissible et indépendante de la forme de surface, supprime l'une sans l'autre.
  - Il classe par défense requise, pas par mécanisme interne.
  - Les candidates sont les croisements cible (agent ou moniteur) × sens (sabotage, silence, fausse alerte) × voie (demande, levier, attribution, origine).
  - Aucune case n'est retenue avant qu'un duel la sépare.
- **« S'entendre ».** Mes plans mesurent un effet d'attribution, un effet d'origine et une capacité sous consigne. Aucun ne mesure une propension spontanée.
- **Transfert vers des agents plus capables.** Un nul ne se transfère pas, et un effet positif non plus sans réplication.
- **Nouveauté.** Les cinq points que je croyais ouverts en III.1 restent à confronter à une recherche bibliographique. Le test de transfert de défense semble proposé aussi par B (RAPPORTÉ).

### L'expérience à faire en premier

**Le socle, puis D1 corrigé**, sur deux familles et une source (contenu d'outil), suivi aussitôt de D1-bis sur les mêmes trajectoires.

Raisons :
- les autres duels réutilisent ces trajectoires ;
- le résultat élague la taxonomie ;
- le socle peut échouer, ce qui arrêterait tout à faible coût.

Lecture croisée de D1 et D1-bis :

| D1 | D1-bis | Ce qui est falsifié | Conséquence |
|---|---|---|---|
| Équivalence | Transfert | Le levier comme cause, et la pression comme classe | Cadre de l'injection indirecte |
| Δ ≥ δ | Transfert | La réduction en taux seulement | Injection plus forte, même défense |
| Δ ≥ δ | Non-transfert | La réductibilité | Menace distincte pour cette défense |
| Équivalence | Non-transfert | L'idée que des taux égaux suffisent à conclure | Défense trop spécialisée ; à refaire avec une autre |
| Non conclusif | — | Rien | Rapporté tel quel, avec la largeur de zone simulée |

### Ce qui me ferait changer d'avis

- **Équivalence et transfert sur deux familles** : j'abandonne la pression comme classe de menace à cette échelle. En III.1, l'équivalence seule me suffisait. La critique de D m'a fait corriger ce point.
- **D2 compensable avec des canaris disjoints** : je cesse de recommander la séparation des canaux pour les juges.
- **D3 dans la marge sur trois familles** : je parle d'erreurs corrélées, sans conclure pour des modèles plus capables.
- **D4-a et D4-b sans gain sur un lecteur séquentiel** : la sonde n'est pas un instrument indépendant du texte.
- **D5 dans l'intervalle, estimateur validé sous fragilité** : les évaluations courtes suffisent pour ce régime.
- **Zone de non-conclusion couvrant la majorité des effets plausibles au budget prévu** : je réduis le nombre de leviers plutôt que d'élargir les marges après coup.
- **Socle en échec dans un seul bras** : aucun duel n'est interprétable, et je le dis avant de rapporter quoi que ce soit.

FIN-DE-CELLULE