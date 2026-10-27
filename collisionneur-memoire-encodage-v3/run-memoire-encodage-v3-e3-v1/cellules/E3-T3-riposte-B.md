# Cellule B — tour III.3 : riposte

**Pièces.** Toutes les pièces sont présentes, intègres et terminées par FIN-DE-CELLULE : faits v2, question v3, ma conception III.1, les équipes rouges A et C. Deux pièces restent citées sans être servies : `selection_pari.py` et la proposition C, dont A cite l'empreinte `958c180e…`. Je ne réponds qu'aux sections « Contre la proposition B », ainsi qu'à F0 et F1 de A, qui me visent aussi. Quand j'emprunte à une section qui vise A ou C, je le dis. Les chiffres que je produis sont illustratifs. Les statuts des faits sont inchangés.

---

## (a) Les attaques, une par une

### Ce que la riposte change dans B (résumé de mes concessions)

1. La fermeture 𝒜(H) était mal définie. Elle devient une **famille paramétrique 𝒢 déclarée avant le scellement**, et non plus « toute fonction de p_H » (C-a2).
2. Les **parents sont attribués par le noyau**, ils ne sont plus seulement déclarés par la fiche (A-B1).
3. Le **noyau possède le schéma de traits** (F0).
4. La dépense d'α par classe est **rétrogradée**. On teste d'abord si la multiplicité est une menace réelle. Si oui, on compare deux dispositifs : une classe ancrée et un α-investing global (A-B2, A-B3, C-a3, C-b1).
5. La consigne ne sert plus ni les budgets α ni τ. Les descripteurs sont calculés sur une sonde publique distincte de la sonde cachée (C-a4, C-b4).
6. Les protocoles sont classés par **puissance mesurée sur un étalon**, et non plus par richesse (A-B7, C-b3).
7. E4 est refaite : même juge et même garde dans tous les bras, contrôle de manipulation **avant garde**, deux placebos, A/A (A-B5, A-B6).

### A — F0 : le schéma de traits appartient à l'auteur

**Acceptée, transformée en test.**

- Le noyau enregistre le schéma au moment du gel. Une loi qui lit une colonne absente de ce schéma n'est pas évaluable : la fiche est refusée.
- **Colonne inerte.** Le noyau évalue la loi sur la sonde, la colonne étant permutée entre instances. Si la prédiction ne bouge pas (écart sous un seuil numérique fixé), la colonne est projetée hors de la loi avant toute comparaison.
- **Colonne active.** On est alors dans un schéma nouveau. La comparaison retombe sur l'encodage structurel et sur le juge, et ce passage est compté à part.
- **Résidu reconnu.** La limite 4a de J (traits mesurés au moment de l'exécution) n'est pas fermée par cette règle.
- **Test.** Les positifs F0 sont dans le banc d'E2′ et rapportés séparément, comme le demande le contrôle 2 de A.

### A — F1 : la fuite par absence

**Acceptée.**

- Correctif : la population servie à la recombinaison est construite à partir de **la même vue filtrée** que la mémoire. Les témoins sont absents des deux, et la différence entre les deux vues ne les désigne plus.
- **Test 1 (classifieur).** Un classifieur reçoit l'ensemble (population, mémoire, consigne). Son taux de repérage des témoins doit rester ≤ hasard + ε.
- **Test 2 (étanchéité).** J'emprunte, en le disant, le contrôle que C oppose à A. Le flux d'octets servi aux agents doit rester bit à bit identique quand on inverse les verdicts de tous les témoins de l'archive. Ce test est mécanique et sans faux positif.

### A — B1 : fermeture à un seul parent ; mélange avec une survivante non déclarée

**Acceptée, transformée.**

- Le trou existe dans ma conception III.1. Ma métrique oracle d'E4 mesurait le gain « au-delà de la fermeture de l'archive », mais le juge d'E1 ne fermait que le parent déclaré. C'est une incohérence.
- **Correctif.** Le noyau attribue r **parents effectifs** : les survivantes dont la fermeture paramétrique, seule ou mélangée par paires, ajuste le mieux la loi de la fille sur la sonde cachée. Il les ajoute au nul augmenté, en plus des parents déclarés. L'attribution n'est jamais servie.
- **Coût.** Il croît avec r. Je fixe r = 2 (illustratif).
- **Résidu.** Un mélange de r + 1 survivantes échappe à l'attribution. On le met dans le banc pour mesurer le résidu, et non pour l'exclure.
- **Sur l'incompatibilité soulevée par A** (servir les fermetures au proposeur) : la formule g∘p est générique et n'apprend rien. Ce qui aide l'attaquant, c'est la liste des survivantes, et le proposeur en a besoin comme marchepieds. Je garde donc la liste et je mesure l'évasion. Si E1′ montre que r = 2 ne suffit pas, je retire la liste de la consigne.

### A — B2 : α_j = α·2^{−j} vaut 2α ou divise la puissance

**Acceptée.**

- L'arithmétique est élémentaire : 1 + ½ + ¼ + … = 2. Avec une première tentative à α, la borne de classe est 2α, pas α. Ma thèse 3 était fausse telle qu'écrite.
- **Correctif déclaré.** La première tentative garde α, ce qui reste comparable à J. Les retentatives se partagent un budget supplémentaire α′ (α_j = α′·2^{−j}, j ≥ 1). La borne de classe est donc α + α′, avec α′ fixé au scellement.
- Ce dispositif ne vaut que si E3′a montre que la multiplicité est réelle (voir plus bas).

### A — B3 : le test de suffisance est un second juge, moins résolu, qui retire de l'α

**Acceptée.** Mes thèses 3 (validité) et 4 (préfiltre) étaient incompatibles. Je tranche :

- **Par défaut**, le détecteur n'a aucun effet sur α. C'est un préfiltre de coût.
- **Il ne modifie α que si E3′a établit la multiplicité**, et alors à trois conditions :
  - son point de fonctionnement est fixé pour que le taux de filles honnêtes à ε = 0,05 classées « redites » soit ≤ 0,05, sur un lot de calibration disjoint ;
  - seules comptent les éliminations **vérifiées par l'autre famille** et faites au n plan du juge ;
  - le bras « détecteur oracle » de A est ajouté. Il sépare les deux causes possibles d'une fuite de classe : une dépense mal construite, ou des faux négatifs du détecteur.

### A — B4 : τ étalonné sur le banc d'évaluation

**Acceptée.** Le lot de calibration est disjoint par graine et par monde. On rapporte aussi le TPR et le FPR obtenus sur le lot de calibration, pour montrer la fuite qu'on évite.

### A — B5 : le contrôle de manipulation est vrai par construction

**Acceptée.** C'est exactement le défaut de M2, et je le reproduisais. Correctifs :

- le **juge et la garde sont identiques dans tous les bras** d'E4′, et seule la consigne varie ;
- le contrôle porte sur les **redites oracle proposées avant garde**, journalisées par le noyau.

### A — B6 : le placebo d'un autre monde porte du contenu procédural transférable

**Acceptée.** E4′ aura deux placebos :

- **3a** : même monde, format conservé, liens fiche–verdict permutés. Il garde le procédural et retire le factuel.
- **3b** : autre monde, même schéma.

La lecture « le contexte aide, pas le contenu » se décompose alors en deux contrastes : 2 − 3a mesure le contenu factuel, 3a − 3b le contenu procédural spécifique au monde.

### A — B7 et C — b3 : la richesse observée confond protocole, effet et n

**Acceptées toutes deux.**

- La richesse mesure l'ampleur de l'effet de la fiche, et non la qualité du protocole. C'est la malédiction du vainqueur décrite par A, et la colonisation par une tautologie à fort signal décrite par C.
- **Volet « n ».** Si le noyau fixe n (J : 200 tirages frais, RAPPORTÉ pour l'expérience 1), ce volet tombe. Que ce soit vrai en exécution réelle reste une HYPOTHÈSE.
- **Correctif.** On classe les protocoles par **puissance mesurée sur une fiche étalon plantée**, d'effet standard, rejouée par le noyau avec ce protocole. À défaut, on sert un tirage stratifié des protocoles de survivantes vérifiées, sans classement.
- **Test** : sous-bras d'E4′ (voir (b)).

### A — B8 et C — a1 : « environ 13 nats » ; « H_A fausse par construction »

**A-B8 acceptée. C-a1 rejetée sur la conclusion, acceptée sur le diagnostic de mon chiffre.**

- **Mon erreur.** Mes « environ 13 nats » appliquaient ½·d·ln n. C'est le regret d'un **mélange bayésien** par rapport au maximum de vraisemblance, pas l'excédent d'un maximum de vraisemblance placé au dénominateur.
- **Ma correction** [HYPOTHÈSE, à vérifier par essai] :
  - Avec sup_θ au dénominateur, sous une alternative honnête, l'excédent sur le meilleur membre θ* de 𝒢 est d'ordre χ²_d/2 en régime régulier. Sa moyenne est d'environ d/2, et non d/2·ln n.
  - J donne pour la « marginale ajustée » l'écart à l'urne ½(K−1)·ln 2π + ½Σ ln c_k − ½ ln n. C'est l'écart de Stirling entre Π c_k!/n! et le maximum de vraisemblance multinomial. Je lis donc que J met déjà un sup-vraisemblance au dénominateur. C'est ma lecture de J, statut HYPOTHÈSE.
- **Dimension effective, écrite avant scellement (A-B8).** λ (1) + q sur le simplexe (2) + b à une constante près (2) + β (1), soit d = 6. Le régime n'est pas régulier : q n'est pas identifiable quand λ = 0, et λ est sur un bord. Le sup sur t ajoute un terme lent.
- **Conséquence** (illustratif) : le seuil effectif passe d'environ ln 20 ≈ 3,0 à environ 6 nats, et non à 16.
- **Ce que je retiens de C.** La perte de puissance sur les petits effets est réelle et plausible. J2 montre le précédent de l'urne : ε = 0,05 passe de 20/20 à 2/20 (RAPPORTÉ, exploratoire, non opposable).
- **Ce que je rejette.** « Impossible par construction » repose sur mon chiffre faux. E1′ mesure directement la distribution de l'excédent.
- **Ce que je reprends de C, et qui est juste.** Le sup n'est pas une loi. Cela ne touche pas la validité, et C l'admet.

### C — a2 : injectivité, le test de suffisance non paramétrique est vide

**Acceptée. C'est la faille la plus grave de ma conception.**

- **L'argument.** Avec K = 3, deux traits et des log-cotes égales à Wx avec W inversible, p_H est injective. Toute loi p′ s'écrit alors (p′∘p_H⁻¹)∘p_H. Un ĝ flexible déclare donc tout redite.
- **Statut.** HYPOTHÈSE de C, que j'accepte. L'argument est élémentaire ; un essai unitaire est à faire.
- **Conséquence pour ma définition.** « Post-traitement qui ne dépend pas des traits » était mal posé : une fonction de p_H peut reconstruire les traits.
- **Redéfinition.** Une redite se définit **modulo 𝒢**, la famille paramétrique déclarée : mélange avec une loi aveugle, inclinaison par issue, température, et leurs compositions. Le contenu « au-delà de p_H » n'est défini que relativement à 𝒢. C'est une convention, je la déclare.
- **Ce qui sort de 𝒢** (sigmoïde des logits, transformations non monotones, C-b2) n'est pas une redite par définition. Ces fiches vont au juge. Si la vérité est dans le nul, une telle fiche est promue avec une probabilité ≤ α, par l'argument de Ville de J. Son seul coût est la multiplicité, mesurée par E3′a.
- **Le reproche de C** (« on retombe sur la vulnérabilité de A ») est donc assumé et borné : l'évasion hors de 𝒢 coûte une tentative de plus, pas une promotion garantie.
- **Contrôle fatal 1 de C repris tel quel** (deux logistiques orthogonales) :
  - le ĝ non paramétrique **doit** montrer un FPR ≫ 0,05 : c'est l'artefact qui donne des dents au contrôle ;
  - le ĝ restreint à 𝒢 doit rester sous 0,05.

### C — a3 : non-transitivité ; chaîne qui fusionne les classes

**Acceptée.** La fermeture transitive est abandonnée.

- **Correctif.** Chaque éliminée vérifiée est l'**ancre** d'une boule de rayon τ. Une fiche nouvelle paie la dépense de chaque boule qui la contient, et rien n'est fusionné.
- **Sur l'arbitraire de l'ordre.** La dépendance à l'ordre n'est pas arbitraire : les ancres sont les éliminations datées, c'est-à-dire l'histoire du pôle.
- **Contrôle fatal 2 de C repris** (chaîne de pas de 0,8τ) : H₁₀, vraie et éloignée, ne doit subir aucune pénalité de classe.

### C — b1 : ε-stepping et déni de service sur α

**Acceptées, transformées en test.**

- **ε-stepping.** Une perturbation à 1,05τ rouvre un budget neuf. La borne 1 − 0,95¹⁰ ≈ 0,40 reste atteignable par une classe ancrée.
- **Déni de service.** Huit fiches sabotées écrasent l'α d'une région vraie. Deux parades partielles :
  - une fiche dont le code est saboté doit être vue par le vérificateur et sortir « indécise » ou « rejetée », pas « éliminée » (cycle de C, RAPPORTÉ comme conception) ; elle ne compte donc pas ;
  - si n est fixé par le noyau, un « N = 5 tirages » est impossible.
- **Ce qui reste.** Les deux attaques rendent la dépense par classe fragile. E3′ oppose donc trois dispositifs :
  - aucun contrôle ;
  - une classe ancrée sur éliminations vérifiées ;
  - un **α-investing global**, indépendant de tout détecteur (Foster et Stine, 2008, « α-investing: a procedure for sequential control of expected false discoveries »). Chaque tentative y coûte de la richesse α, ce qui neutralise l'ε-stepping. Le déni de service se déplace alors vers la richesse globale, et il est mesuré.
- **Premier test.** Avant tout cela, on vérifie si la multiplicité est réelle (E3′a). Si elle ne l'est pas, les deux attaques deviennent sans objet.

### C — a4 : fuite d'oracle par les descripteurs servis

**Acceptée.**

- **Correctif.** Les descripteurs sont calculés sur une **sonde publique**, disjointe de la sonde cachée qui sert à la détection et à l'attribution des parents.
- **Test.** On compare un attaquant scripté qui reçoit les descripteurs à un attaquant qui ne les reçoit pas. On mesure la précision d'atterrissage dans (τ ; 1,1τ]. Si la précision augmente, les descripteurs fuient : on les sert en cellules grossières.

### C — b4 : l'évasion totale

**Acceptée pièce par pièce, transformée en un cheval de bataille scripté pour E1′.**

- **Étape 1.** Elle exploite les budgets α et l'historique des classes, que je servais. Je les retire de la consigne : on sert les éliminées et leur cause, sans budget ni seuil.
- **Étape 2.** Elle utilise un trait corrélé au numéro d'instance. Deux défenses s'y opposent : l'exigence de J (« l'heure d'exécution n'est jamais un trait ») et l'ordre secret (RAPPORTÉ, codé selon J2), plus la possession du schéma par le noyau (F0). Le résidu est la limite 4a.
- **Étape 3.** Elle copie un gabarit de forte richesse. Le classement par puissance sur étalon y répond.
- **Emprunt à A** (section « ce que je retiens ») : son expérience « proposeur scripté tous à la fois sous schéma possédé par le noyau » devient un cas fatal d'E1′.

---

## (b) Les expériences corrigées

Ordre imposé. E1′ et E3′a se font dans la même course, sur processeur, en réutilisant les 105 essais du juge v1 (RAPPORTÉ, J2). E2′ conditionne la garde. E4′ et E5′ n'ont lieu que si E1′ passe ; sinon, la mémoire doit porter seule la charge des redites, et le banc d'E4′ est à revoir.

### E1′ — fermeture paramétrique 𝒢 et parents effectifs dans le juge

- **H_A.** Le juge v1 + 𝒢 (d = 6, déclarée) + r = 2 parents effectifs attribués par le noyau + schéma possédé par le noyau satisfait les deux conditions suivantes :
  - **tricheurs** : toutes les familles ci-dessous ont un taux de promotion ≤ α (borne de Wilson rapportée) ;
  - **puissance** : ≥ 0,90 sur la fille neuve, avec une perte ≤ 0,05 par rapport au juge v1.
- **H_B.** L'une des deux portes cède : un tricheur > α, ou la puissance < 0,90. On dit laquelle.
- **Tricheurs** :
  - mélange fixe de J2 sur **graine neuve** (777 est exploratoire) ;
  - g ∈ 𝒢 tiré au hasard à chaque répétition (contrôle 1 de A) ;
  - compositions mélange∘inclinaison∘température ;
  - parent + une survivante non déclarée ;
  - parent + deux survivantes non déclarées (résidu r + 1, rapporté) ;
  - le cheval de bataille scripté (colonne inerte + mélange de survivantes + `ce_qui_change` type + seuil décalé).
- **Cas honnêtes.** Composante vraie ε = 0,2 et ε = 0,05, T1b-fille. On rapporte la **distribution de l'excédent** sup_θ − θ*, qui vérifie ou réfute directement ma correction de A-B8.
- **Artefacts qui doivent être vus** (sinon le contrôle n'a pas de dents) :
  - le juge v1 sans 𝒢 sur le mélange fixe (taux > α) ;
  - la fermeture au seul parent déclaré sur « parent + survivante non déclarée ».
- **Réglages** : ceux de J (1 000 répétitions, 200 tirages, K = 3, α = 0,05). Graine maîtresse neuve tirée au scellement. Pilote déclaré (R-473).
- **Issue qui falsifie.**
  - Si les deux portes tiennent, H_B est falsifiée : la redite modulo l'aveugle est l'affaire du juge.
  - Sinon, H_A est falsifiée, et l'on sait si c'est la validité ou la puissance qui a cédé.

### E3′a — la multiplicité est-elle une menace réelle ? (même course)

- **H_A.** Sans aucun contrôle, un proposeur scripté qui retente m = 10 variantes d'une loi fausse éliminée obtient un taux de promotion de classe dont la borne basse de Wilson est > α. Les variantes couvrent ε-stepping, transformations dans 𝒢 et transformations hors de 𝒢.
- **H_B.** Le taux reste ≤ α, puisque Ville est conservatrice : J attend les contrôles « bien en dessous » de α, et J2 rapporte un socle à 0 promotion (exploratoire).
- **Issue qui falsifie.**
  - H_B confirmée : ma thèse 3 est falsifiée, toute dépense d'α est retirée, la garde est purement économique, et les attaques C-b1 tombent avec elle.
  - H_A confirmée : on passe à E3′b.

### E3′b — quel contrôle de multiplicité ? (seulement si H_A d'E3′a)

- **H_A.** L'α-investing global garde le taux de classe ≤ α sous ε-stepping **et** une puissance ≥ 0,80 (illustratif) sur une vraie loi reproposée après un test faible.
- **H_B.** La classe ancrée fait au moins aussi bien sur ces deux mesures.
- **Attaques** : ε-stepping, chaîne de 0,8τ, déni de service par 8 fiches sabotées (contrôle 3 de C), précision d'atterrissage avec ou sans descripteurs (C-a4). La classe ancrée tourne avec un détecteur oracle et avec le détecteur réel (contrôle 3 de A).
- **Issue qui falsifie.** L'un des deux dispositifs est éliminé. Si les deux échouent, on le dit, et la mémoire ne revendique aucun rôle de validité.

### E2′ — quel encodage détecte une redite modulo 𝒢 ?

- **H_A.** L'ajustement restreint à 𝒢 sur la sonde cachée atteint un TPR ≥ 0,90 à FPR ≤ 0,05. Il bat d'au moins 0,10 en TPR la meilleure de ces vérifications : Jaccard M1, égalité de `signature_prediction`, rangs seuls, log-cotes centrées seules, plongements.
- **H_B.** L'une de ces vérifications fait aussi bien.
- **Banc** :
  - les positifs de ma conception III.1, plus les positifs F0 (rapportés à part) ;
  - des négatifs honnêtes au texte proche ;
  - deux logistiques orthogonales.
- **Calibration** : τ fixé sur un lot disjoint (graines et mondes).
- **Artefacts qui doivent être vus** :
  - le ĝ non paramétrique, FPR ≫ 0,05 sur les orthogonales ;
  - l'encodage aléatoire, aire sous la courbe ≈ 0,5 ; au-delà de 0,6, le banc fuit et E2′ est nulle.
- **Prédiction signée** [HYPOTHÈSE] : les rangs ratent l'inclinaison, les log-cotes ratent le mélange, et aucune des deux n'attrape la composition.

### E4′ — l'ablation avec de vrais agents dans des mondes plantés

- **Principe.** Même juge, même garde et même budget en dollars et en jetons pour tous les bras. Seule la consigne varie.
- **Bras** :
  1. sans mémoire ;
  2. mémoire B ;
  3. placebo, en deux versions : **3a** même monde avec verdicts permutés, **3b** autre monde de même schéma ;
  4. empoisonnée, 20 % de verdicts inversés (illustratif) ;
  5. **A/A** : bras 1 dupliqué, qui donne le plancher de bruit et fixe l'effet minimal au scellement.
- **Sous-bras bibliothèque** : protocole classé par puissance sur étalon, contre protocole tiré au hasard, contre classement par richesse.
- **Métrique principale.** Gain oracle net cumulé des survivantes nouvelles par dollar, mesuré en nats sous la loi vraie, au-delà de la fermeture 𝒢 de l'archive. Je maintiens ma thèse 5 : les témoins mesurent le juge, ils ne mesurent pas les découvertes.
- **Contrôle de manipulation.** Le taux de redites oracle **proposées avant garde** doit être plus bas dans le bras 2 que dans le bras 1. S'il ne l'est pas, la conclusion est « non concluant », pas « n'aide pas ».
- **Contrôles fatals** : le classifieur de témoins sur (population, mémoire, consigne) et l'étanchéité bit à bit de F1.
- **H_A.** 2 − 3a > effet minimal, avec une borne basse > 0.
- **H_B.** 2 − 3a ≤ effet minimal. Si le contrôle de manipulation est réussi, on conclut « le contenu factuel de la mémoire n'aide pas, sur ce banc ».
- **Plan.** 6 mondes × 2 graines × 6 générations, permutation par monde (illustratif). Puissance calculée sur un pilote déclaré.

### E5′ — viser une survie intermédiaire

C'est un bras d'E4′, inchangé sauf sur trois points :

- les descripteurs sont calculés sur la sonde publique ;
- on ajoute un bras à **descripteurs déclarés** (contrôle 5 de A), qui mesure l'aggravation de Goodhart ;
- l'artefact « viser une survie haute » doit montrer une survie en hausse sans gain oracle.

**Issue qui falsifie.**

- Gain intermédiaire ≤ gain uniforme : H_A est falsifiée.
- Gain intermédiaire supérieur, sans hausse des survivantes vides : H_B est falsifiée.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi (statuts conservés)

- **La garde actuelle est textuelle, à sens unique, et contournable par construction** [RAPPORTÉ, code M1].
  - Elle compare par Jaccard des 3-grammes le seul énoncé aux seules éliminées.
  - Elle compare la prédiction par égalité exacte.
  - Elle ne sert ni les éliminées ni leur cause au proposeur.
  - Elle classe les gabarits par sévérité déclarée.
- **L'ablation de la mémoire ne conclut rien** [RAPPORTÉ, M2] : agents simulés, une redite sur 26 fiches.
- **Le critère des filles a un trou antérieur à v1** [RAPPORTÉ, J2, exploratoire, non opposable] :
  - « parent + loi aveugle fixe » est promu 58/200 sous v0 et 63/200 sous v1 ;
  - encore 5/20 après l'ajout du huitième tricheur ;
  - l'urne coûte de la puissance sur les petits effets (2/20 contre 20/20).
- **Un encodage peut être aveugle sur des textes réels** [RAPPORTÉ, G2, exploratoire, 27 textes] : rappel 0,000 contre 0,038 au hasard. Un encodage nul passait le protocole P1 à 100 %. C'est la leçon méthodologique : tout encodage de mémoire doit battre un nul et un contrôle aléatoire.
- **Par raisonnement, à confirmer par des essais unitaires d'une ligne** [HYPOTHÈSE] :
  - un test de suffisance non paramétrique est vide quand p_H est injective (C) ;
  - α·Σ 2^{−j} vaut 2α (A) ;
  - les rangs sont invariants au mélange, les log-cotes centrées à l'inclinaison, et aucune des deux signatures à leur composition.

### Ce qui ne l'est pas (HYPOTHÈSE)

- Que la mémoire améliore les propositions. Le taux de base des redites avec de vrais agents.
- Que la multiplicité des retentatives soit une menace réelle, Ville étant conservatrice.
- Qu'une fermeture paramétrique 𝒢 dans le juge garde une puissance ≥ 0,90. Ma correction de l'excédent, d'ordre d/2 et non d/2·ln n, n'est pas mesurée.
- Que le noyau puisse posséder le schéma de traits en données réelles.
- Qu'un encodage, quel qu'il soit, détecte les redites modulo 𝒢 à FPR ≤ 0,05.
- Que l'orientation vers une survie intermédiaire apprenne du vrai plutôt que du facile.

### Ma réponse aux points 1 à 3, telle qu'elle sort de la riposte

**Point 2 (qu'est-ce qu'une redite).** Une redite se définit **modulo une famille 𝒢 déclarée**, pas modulo « l'aveugle » en général : cette dernière notion est mal posée dès que la loi est injective. Ce qui sort de 𝒢 va au juge et coûte au plus une tentative.

**Traitement asymétrique, révisé.**

- **Survivantes.** Leur fermeture, avec r parents attribués par le noyau, entre dans le nul. Une proche voisine d'une survivante compte comme réplication.
- **Éliminées.** On ne les bloque pas. Une proche voisine passe le test ordinaire. On ne dépense de l'α que si E3′a montre que la multiplicité est réelle.

**Point 1 (encodage par usage).**

| Usage | Encodage | Statut |
|---|---|---|
| Détecter une redite | Ajustement restreint à 𝒢 sur sonde cachée, à schéma possédé par le noyau ; le texte sert de préfiltre de coût | à départager par E2′ |
| Retrouver ce qui sert au proposeur | Structure, cause, protocole classé par puissance sur étalon | à mesurer dans E4′ |
| Attribuer le mérite | Log-richesse contre le nul augmenté | à mesurer |

**Point 3 (ce que sert la consigne).** Elle ne sert jamais ni budget, ni seuil, ni sonde cachée, ni témoin, ni verdict non vérifié.

### L'expérience à faire en premier

**E1′**, avec E3′a dans la même course : processeur seul, coût proche de 0 (illustratif), socle des 105 essais existants.

**Pourquoi elle d'abord.** Tout ce qui suit en dépend : la garde, le mérite, l'ablation.

- Si le juge absorbe la fermeture 𝒢 sans perdre de puissance, la mémoire n'a plus de rôle de validité. Elle redevient une économie et une aide au proposeur, et E4′ peut le mesurer proprement.
- S'il cède par la puissance, c'est la mémoire qui doit porter la détection des redites. E2′ devient alors bloquante, et l'α-investing d'E3′b passe avant toute ablation.

**Ses deux issues falsifient quelque chose.** Elle peut échouer par la validité (un tricheur > α) ou par la puissance (< 0,90), et l'on saura laquelle.

FIN-DE-CELLULE