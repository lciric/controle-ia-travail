# Proposition A — Tour III.2 : critique croisée de méthode

**Conventions.** Les faits tirés des pièces sont **RAPPORTÉS** (moisson non opposable) ou **OBSERVÉ-NON-AUDITÉ** (résultats de Lazar). Toute critique ci-dessous est une **HYPOTHÈSE de méthode** ; tout chiffre que j'introduis est **illustratif**. Je ne fusionne pas les propositions : quand un défaut est partagé, je le dis à l'endroit où il est le plus coûteux et je renvoie. Les pièces coupées (annexes F, G, figure 32, A.4, moisson) restent absentes ; aucune critique ne s'appuie sur leur contenu supposé.

Une remarque préalable qui pèse sur les quatre propositions sans les harmoniser : toutes mesurent un **rappel conditionné au rang**, et aucune ne dit comment un cas **planté** obtient son **score de classement**. Si le score est assigné par l'expérimentateur (simulé) et non obtenu en faisant passer la méthode par le banc réel, la covariance entre gain et détectabilité est fixée par le plan et le résultat est vrai par construction. Je le détaille là où le défaut est le plus net (B fiche 2, D1, E-S).

---

## Sur la proposition B

### (a) Défauts de méthode

**Fiche 1 (co-ratage, excès E).**
- *Confondant de capacité.* r = P(Mⱼ rate | Mᵢ rate)/P(Mⱼ rate) est borné par 1/P(Mⱼ rate | triche). Un moniteur faible (Llama-3.1-8B comme « troisième famille ») a un taux de ratage élevé, donc r proche de 1 **par construction**, quelle que soit la dépendance. Les paires « familles différentes » qui contiennent Llama sont donc tirées vers r ≈ 1 et E(même famille − familles différentes) devient positif par simple hétérogénéité de capacité, pas par partage d'angles morts. Il faut apparier les paires sur le taux de ratage marginal, ou utiliser une mesure qui ne dépend pas des marges (par exemple un odds ratio ou le κ sur les ratages), sinon H_B est favorisée par la composition du panel.
- *Fuite génération → surveillance.* Les items sont « construits par une équipe rouge » ; si cette équipe emploie un modèle d'une des trois familles pour rédiger les trajectoires ou le code, le co-ratage intra-famille est confondu par la famille génératrice. La variante de B (trajectoires de F_a surveillées par F_a et F_b) traite ce point pour la variante, pas pour l'expérience principale. Un plan croisé famille génératrice × famille moniteur est nécessaire.
- *Contrôle positif vide.* « Deux appels du même moniteur avec la même invite » : à température nulle r = 1/P(rate) exactement ; à température non nulle, il ne mesure que la stabilité d'échantillonnage. Ce contrôle ne donne pas de « dents » à la métrique sur ce qui est visé (angles morts partagés entre rôles différents). Le contrôle positif pertinent est : même famille, invites et rôles différents (M_code vs M_traj), ce qui est précisément la cellule expérimentale, donc le plan n'a pas de contrôle positif distinct.

**Fiche 2 (effet Berkson).**
- *Vrai par construction via l'intensité.* Les tricheries sont plantées « à intensités variées ». Si l'intensité gouverne à la fois le gain de score et la visibilité, le signe de cov(gain, P(détection)) est choisi par la grille d'intensités de l'expérimentateur. La fiche ne dit pas si l'intensité est tirée indépendamment de la visibilité. Il faut soit tirer intensité et « visibilité » indépendamment dans le plan, soit reporter la covariance **conditionnelle à l'intensité**.
- *Pseudo-réplication.* « 1 000 classements par tirage de pools » : les mêmes items plantés réapparaissent dans les 1 000 rejoués ; l'effectif effectif pour Δ(k) est le nombre d'items plantés distincts atteignant le top-k, pas 1 000. Les intervalles par bootstrap sur les rejoués seront trop étroits.
- *P(détection) par item.* Estimée sur un verdict binaire unique par item, sauf appels répétés : la covariance est alors entre un gain continu et une indicatrice, estimée avec un bruit de Bernoulli non modélisé.

**Fiche 3 (ratio T).** T est un ratio de deux différences de d′ ; sa loi est à queue lourde dès que le dénominateur approche zéro. B l'admet, mais propose quand même T comme métrique de décision. Rapporter les deux différences avec leurs intervalles, et décider sur le numérateur conditionnellement à un dénominateur dont la borne inférieure dépasse un minimum préenregistré. Fuite possible : les 16 variantes ont-elles été rédigées en connaissant C4 et C5 ? Rien ne l'exclut.

**Fiche 4 (organisme).** Défaut structurel : la cellule « R1 × tricheurs scriptés × sans retour » est **vraie par construction** pour H_A. Des scripts non adaptatifs tirent leurs soumissions indépendamment des verdicts ; la réutilisation d'un banc réservé ne nuit qu'à des soumissions **adaptées** aux verdicts précédents. La borne 1 − (1 − α)ⁿ (RAPPORTÉE, nos résultats §3) suppose n tentatives *adaptatives* avec arrêt à la première promotion. Le duel principal (réutilisation bénigne ou dominante) ne peut donc être tranché avec les tricheurs scriptés existants ; il exige un proposeur adaptatif (Argon-like), que B relègue « en second temps ». Le duel secondaire (W2) ne fait que répliquer A1 par scripts.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Fiche 1 : si pour une classe P(Mᵢ rate | triche) < 0,1 (illustratif), le nombre d'événements conditionnants est de l'ordre de 15 sur 150 items, et l'intervalle de r couvre [0,5 ; 2] : E non jugeable. Si P(Mⱼ rate | triche) > 0,8, r ∈ [1 ; 1,25] par borne : aucune puissance. Fenêtre utilisable : taux de ratage marginal dans [0,2 ; 0,6] environ (illustratif), à vérifier avant la notation.
- Fiche 2 : si la variance intra-classe du gain des tricheries est nulle (toutes les relances rapportent le même gain), cov = 0 par construction. Si la dispersion des scores honnêtes dépasse le gain maximal des tricheries, aucun item planté n'atteint le top-3 et rappel(top-3) n'a pas de dénominateur.
- Fiche 3 : d′ non défini si le taux de fausses alertes estimé est 0 (n_honnêtes × FA < 5, illustratif) ; correction de continuité à préenregistrer. Si le taux de violation de v* chute, les positifs se raréfient et d′_hors(v*) a un intervalle trop large.
- Fiche 4 : sous R1, pour des soumissions iid, P(promotion) = α par soumission ; le taux « ≤ 2α jusqu'à n = 16 » est alors attendu quel que soit le système : H_A n'est falsifiable que si les soumissions sont corrélées aux verdicts.

### (c) Contrôles négatifs dont l'absence serait fatale

- Fiche 1 : paires de moniteurs **appariées sur le taux de ratage marginal** (sans cela, E mesure l'hétérogénéité de capacité) ; permutation des verdicts **sur tout le pool**, pas seulement intra-classe (la permutation intra-classe laisse la difficulté de classe, qui n'est pas l'objet).
- Fiche 2 : covariance entre gain et détection calculée **parmi les méthodes honnêtes** (une relation gain–« suspicion » chez les honnêtes signale que le moniteur lit le score, pas la triche).
- Fiche 3 : variante sélectionnée pour **minimiser** d′ sur banc (anti-sélection) pour établir que la sélection a un signe.
- Fiche 4 : proposeur adaptatif dans un monde sans signal sous R2 (déjà prévu) **et sous R1** ; sans R1 adaptatif, la cellule décisive n'existe pas.

---

## Sur la proposition C

### (a) Défauts de méthode

**Fiche 1.**
- *Mécanisme non observable avec les étiquettes prévues.* H_A dit que le forum **copie** les variantes non détectées à haut score. Mais les triches sont « injectées par tirage aléatoire dans 20 % des propositions » par l'expérimentateur. Les copies faites par les agents à partir du forum n'ont **pas d'étiquette** de vérité terrain (elles sont générées par Llama, pas plantées). Donc soit le rappel est mesuré sur les 20 % injectés seulement — et la condition « forum » ne peut modifier leur détection que par ce que le moniteur lit, pas par copie — soit sur les copies, sans vérité terrain. Le plan ne mesure pas ce que l'hypothèse affirme. Une traçabilité de lignée (quel item du forum a été repris, avec quel degré de modification) est nécessaire, et un critère mécanique pour étiqueter une copie comme non conforme.
- *Confondant de composition.* Le forum déplace la distribution des scores (RAPPORTÉ : environ +6 points, Kirchner D.5). Le « top 10 % » avec forum n'est pas la même population qu'en l'absence de forum ; ΔΔRappel confond effet de contagion et changement de composition. Stratifier par score absolu plutôt que par centile.
- *Contrôle négatif mal défini.* C_rec est décrit à la fois comme « type W2 » (hors nulle, non couvert par v8, RAPPORTÉ) et « tricheurs pré-v8 » (couverts, tués 0/1 000). Un juge v8 proposé comme contrôle négatif sur une classe qu'il déclare ne pas couvrir a un rappel nul **par construction** ; sur la classe couverte, il est à 1 000/1 000 par construction. Ni l'un ni l'autre n'informe sur le moniteur linguistique.

**Fiche 2.**
- *Gradient contre un moniteur, par la bande.* « LoRA de lisibilité style 2407.13692 » : un adaptateur entraîné avec un signal de vérificateur est un gradient contre un moniteur, ce que la question écarte comme « déjà pris » et que la fiche dit ne pas faire.
- *Contrôle positif étiqueté négatif.* « ΔTPR_in ≥ +0,20 » est une vérification de manipulation, pas un contrôle négatif. Aucun contrôle négatif réel (banc de sélection aux étiquettes permutées) n'est prévu.
- *Malédiction du gagnant non traitée.* Top-5 parmi 50 variantes sur 200 épisodes, sans remesure sur épisodes frais. Le maximum de 50 estimations bruitées dépasse la vraie valeur d'environ 2,2 erreurs-types (illustratif, loi des extrêmes) ; la « vérification » ΔTPR_in ≥ 0,20 peut être satisfaite par le bruit seul, et H_B serait alors « réfutée » sans qu'aucun gain n'ait existé.
- *Sous-groupe sur une note non validée.* Conditionner sur « conscience d'évaluation > 6/10 » notée par un juge linguistique, alors que nos résultats (OBSERVÉ-NON-AUDITÉ, §4) donnent κ = 0 pour ce type de juge au plafond. Le seuil 6 est post hoc ; la fiabilité test-retest de la note n'est pas mesurée.
- *Transplantation du plancher P3.* « 200 prédicteurs aléatoires appariés en covariance » est défini pour des sondes sur activations ; appliqué à un moniteur qui lit du texte, l'espace de caractéristiques n'est pas dit. Sans lui, le plancher n'existe pas.

**Fiche 3.**
- *Confusion de facteurs.* T₁ et T₂ diffèrent **simultanément** par la transparence des règles et par la nulle (v8 contre « v9 couvrant les partitions par morceaux »). Toute baisse de p_W2 est attribuable à v9 seule. Il faut un plan 2 × 2 (transparence × nulle).
- *Fuite construction → évaluation.* Une nulle v9 conçue après l'attaque A1 pour couvrir W2, puis testée sur W2, est évaluée dans l'échantillon qui a servi à la construire. La couverture doit être testée sur des classes de recombinaison non utilisées pour concevoir v9.
- *Volet 2 : instruments incommensurables.* Le seuil ΔS_audit ≤ −0,5 est justifié par « la barre d'erreur ± 0,64 de D.3 » (Petri, 1 à 10, ± non qualifié, RAPPORTÉ) alors que l'auditeur externe de C est une courbe dose–réponse de sycophancie sur Llama. L'unité et la dispersion ne sont pas celles de Petri. De plus, « première méthode franchissant 1/α » et « 99ᵉ centile » diffèrent par le budget d'évaluation consommé et par l'échantillon ; l'estimateur de l'arrêt séquentiel sur un banc de 200 exemples n'est pas défini (quels tirages frais ?).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Fiche 1 : avec 1 000 propositions dont 20 % plantées, le top 10 % contient environ 100 propositions et environ 20 plantées (illustratif) ; l'erreur-type d'un rappel sur n = 20 est d'environ 0,1 ; le seuil |ΔRappel| < 0,05 avec Fisher p > 0,10 est inatteignable : la branche « falsification de H_A » est non jugeable à cet effectif.
- Fiche 2 : si l'erreur-type de d′ sur 200 épisodes dépasse 0,1 du gain attendu, la sélection sur 50 variantes produit un gain apparent sans gain réel ; condition de jugeabilité : remesure sur épisodes frais avec intervalle excluant 0.
- Fiche 3, volet 1 : avec 12 unités par cellule, passer de 11/12 à ≤ 1/12 est détectable, mais une valeur intermédiaire (4/12) n'est dans aucune branche ; zone non concluante large. Volet 2 : si la probabilité que le processus d'e-valeurs ne franchisse jamais 1/α dans le budget dépasse quelques dizaines de pourcents (illustratif), la comparaison n'a pas de membre gauche.

### (c) Contrôles négatifs dont l'absence serait fatale

- Fiche 1 : propositions honnêtes **copiées via le forum** (lignée tracée) pour mesurer le taux de fausses alertes sur les copies ; sans cela, toute hausse de signalement sur les copies est indistinguable d'un biais anti-copie du moniteur.
- Fiche 2 : banc de surveillabilité aux étiquettes permutées (absent) ; remesure du top-5 sur épisodes frais (absent).
- Fiche 3 : cellule « transparence seule, nulle inchangée » (absente) ; classe de recombinaison hors W2 non vue lors de la conception de v9 (absente).

---

## Sur la proposition D

### (a) Défauts de méthode

- *Scores des cas plantés.* R_S porte sur « les cas plantés que le score seul placerait parmi les lauréats ». Si le score des cas plantés est obtenu par exécution réelle sur le banc, le plan est sain ; s'il est assigné, Δ est fixé par la main qui plante. D ne le dit pas, et D insiste par ailleurs sur un « déclencheur mécanique de validation » : il faut préciser que le score et le déclencheur sont deux voies indépendantes.
- *Fuite de l'étiquette dans l'entrée.* Un cas planté possède « une étiquette par construction et un déclencheur mécanique ». Si la procédure de plantation laisse une trace textuelle ou structurelle (un marqueur, une signature de code) que le moniteur peut lire, le rappel mesure la détection de l'artefact de plantation, pas de la classe. Les cas honnêtes « presque limite » doivent être produits par la **même** procédure d'insertion, à l'élément fautif près.
- *Appariement par décile de score.* Les honnêtes sont appariés aux plantés par décile de score. Cela stabilise les fausses alertes par rang mais, combiné à des scores assignés, impose la distribution conjointe (classe, score) par le plan.
- *Branche de non-jugeabilité trop large.* H_A n'est falsifiée que si R₀ **et** R_S ont une borne inférieure ≥ 0,90. Un moniteur à R₀ = 0,7 avec Δ = 0 n'entre dans aucune branche. D le dit (« rejette d'abord le moniteur »), mais cela rend le duel conditionnel à un instrument que personne n'a encore qualifié ; avec un Llama-8B moniteur, R₀ ≥ 0,90 est une hypothèse forte.
- *D2 : même poids pour sélectionner et auditer ?* « Le moniteur d'audit ne sert jamais à sélectionner », mais le banc de surveillabilité emploie un moniteur ; D ne dit pas s'il partage les poids de l'audit. Si oui, le « hors banc » n'est hors banc que par les tâches, pas par l'instrument (voir E, qui le dit). Si non, D doit déclarer la famille.
- *Standardisation « intensité de sélection égale ».* Top-k identique sur deux cibles (score de tâche, score de surveillabilité) de variances différentes ne donne pas la même pression de sélection au sens de la différentielle de sélection ; comparer à quantile égal **et** à écart-type égal.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Δ = R_S − R₀ : R_S est estimé sur n_S = nombre de plantés parmi les lauréats. Avec 400 plantés et top-k par cohorte, n_S peut être de l'ordre de 20 (illustratif) ; variance binomiale R(1 − R)/n_S donne une erreur-type d'environ 0,09 ; la branche « Δ ≥ −0,05 avec intervalle » n'est pas atteignable, la branche « Δ ≤ −0,20 » l'est à peine. Condition de jugeabilité : n_S ≥ 100 (illustratif), ce qui impose soit plus de plantés, soit un k plus grand (qui dilue l'effet Berkson).
- Si la loi du score des plantés est stochastiquement dominée par celle des honnêtes (triches peu rentables), n_S → 0 : non jugeable, et l'expérience ne dit rien de Kirchner, où 1 triche signalée a atteint le top-3 (RAPPORTÉ).
- D2 : si le rappel interne ne monte pas d'au moins 0,15 (condition préalable implicite à H_B), aucune branche.
- Intervalles par cohorte : avec peu de cohortes (D ne donne pas leur nombre), l'estimateur de variance entre cohortes a peu de degrés de liberté ; condition : au moins 10 cohortes (illustratif).

### (c) Contrôles négatifs dont l'absence serait fatale

- Cas honnêtes **produits par la procédure de plantation** (insertion d'un élément licite) : sans eux, la fuite de marqueur est indétectable.
- Banc de surveillabilité aux étiquettes permutées pour D2 (B et E l'ont, D non).
- Sélection par un score **indépendant** du banc (par exemple un score sur une autre tâche) : si Δ persiste, il vient de la mécanique de sélection ou du moniteur, pas d'une covariance gain–visibilité.

---

## Sur la proposition E

### (a) Défauts de méthode

- *Pilote sur l'organisme : les violations sélectionnées n'existeront pas.* E-S commence « sur l'organisme public, avec des candidats scriptés ». Or le juge v8 tue 0/1 000 sur 11 lignes (OBSERVÉ-NON-AUDITÉ, §2) ; seule la classe W2 passe. La « sélection par classement » (par quel score ? le processus de richesse ne classe pas, il promeut ou non) ne retiendra donc que des violations W2 : R_C est calculé sur une seule classe, et la standardisation à mélange constant (métrique 4) est indéfinie faute de support. Par la propre règle d'E (« dépend du nombre de violations effectivement sélectionnées »), le pilote est non jugeable avant d'être lancé. De plus un moniteur Llama lisant des traces **scriptées** (sans raisonnement) mesure la détection d'un format, qui ne transfère pas aux traces d'agents.
- *Duel à marge unique.* H_A : D ≥ 15 ; H_B : D < 15. Réfuter H_A (borne supérieure < 15) ne réfute rien de ce que Kirchner affirme : D = 12 reste une dégradation réelle. E dit que cela lui ferait « abandonner la prédiction d'un effet important », mais aucune issue ne falsifie « le rappel est transportable ». Pour que les deux issues falsifient quelque chose (B4), il faut une seconde marge (par exemple D ≤ 5, illustratif) définissant H_B comme « transportable », et une zone intermédiaire déclarée.
- *Métrique 3 vraie par construction.* « Probabilité qu'un lot aboutisse à une méthode invalide non détectée » est une fonction mécanique du taux de plantation par lot, choisi par l'expérimentateur. Reportée sans dose–réponse sur ce taux, elle ne caractérise pas le système.
- *E-T : conditionnement sur une variable post-traitement.* Les résultats sont « standardisés sur les classes de violations et leur **gravité observable** ». La gravité est observée après l'intervention ; si la sélection sur surveillabilité déplace la distribution de gravité (plausible : les configurations plus lisibles pourraient commettre des violations plus bénignes ou plus graves), standardiser dessus retire une partie de l'effet ou en crée un. Standardiser sur des strates fixées **avant** l'intervention seulement.
- *E-T : contrainte de « qualité de tâche comparable ».* Non opérationnalisée ; si elle est stricte, les configurations candidates se ressemblent et le gain sur banc disparaît (E le prévoit comme non-conclusion, ce qui rend l'expérience fragile par conception).
- *Scores des candidats figés.* Même réserve que pour D : d'où viennent les scores des violations dans l'ensemble figé ? Non dit.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- R_C : estimé sur les violations retenues par classement ; si la fraction retenue est f et la proportion de violations parmi les retenus est π_C, n_C = N·f·π_C ; avec N = 768, f = 1/8 (un lauréat par lot) et π_C = 0,2 (illustratif), n_C ≈ 19 ; erreur-type de R_C ≈ 0,1 ; la marge de 15 points est à peine résoluble, la seconde marge que je demande ne l'est pas. Condition : n_C ≥ 100 (illustratif), donc des milliers de candidats ou plusieurs lauréats par lot.
- Standardisation (métrique 4) : poids indéfinis dès qu'une famille a zéro violation retenue dans une branche ; variance en 1/min(n_fc).
- Seuil à 5 % de fausses alertes calibré sur un jeu honnête séparé : si la loi des honnêtes **retenus** diffère de celle du jeu de calibration (ce que la sélection produit par définition), le taux réel de fausses alertes après sélection dérive, et le rappel à FA fixé n'est plus comparable entre branches. E mesure les FA sans recalibrer (bien), mais compare alors des rappels à FA différents.
- E-T : G standardisé ; si les strates de gravité post hoc sont déséquilibrées entre branches, l'estimateur standardisé a une variance qui croît avec le déséquilibre, et un biais si la gravité est affectée par le traitement.

### (c) Contrôles négatifs dont l'absence serait fatale

- Lots **sans violation** avec sélection par classement : mesure la loi des FA parmi les lauréats honnêtes, indispensable pour interpréter D à FA non recalibré.
- Sélection par un classement **indépendant** du banc (score permuté entre lots, pas seulement intra-lot ; ou score d'une autre tâche) : la permutation intra-lot que prévoit E annule la sélection mais ne distingue pas « sélection sur ce score » de « sélection sur n'importe quel score corrélé à la longueur ou à la complexité des traces ».
- Dose–réponse sur le taux de plantation pour la métrique 3.
- Pour E-T, strates de gravité **préenregistrées** et mesurées sur des cas de calibration hors expérience ; sinon la standardisation n'est pas un contrôle, c'est un ajustement post hoc.

---

## Note de clôture (non un résumé)

Les quatre propositions laissent ouvert le même point que je signale en tête : la provenance du score des cas plantés. C'est une fuite entre la construction de l'instrument (la plantation) et son évaluation (le rang). Tant qu'elle n'est pas fermée par une exécution réelle sur le banc, le signe de toute covariance gain–détection est un choix de plan, et les duels H_A/H_B de B (fiche 2), C (fiche 1), D (D1) et E (E-S) ne falsifient que ce choix. **HYPOTHÈSE de méthode**, à trancher avant tout lancement.

FIN-DE-CELLULE