# Kirchner Q2 — tour du collisionneur — critiques croisées (tour 2), brutes — v1
Tour du collisionneur sur la question 2 de Kirchner (GO-2026-11-03-04, 10:23 → 11:23 UTC, 13 cellules sur 15, ≈ 10,10 USD). Copie à l'octet de session-depot (liste de copie vérifiée, 0 écart). **Brut** : ni normalisé, ni moissonné, ni classé. Espèces désignées par leur lettre (A à E). Les réponses de D et E (tour 3) manquent : la réponse de D a échoué (erreur du relais), celle de E n'a pas été lancée ; une suite D + E tourne chez session-depot. Les chiffres des cellules ne sont pas vérifiés.


---

## Critiques écrites par l'espèce A

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
---

## Critiques écrites par l'espèce B

# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces.** Annexes F et G, figure 32 et moisson intégrale : absentes des faits servis. Je n'en infère rien.

**Conventions.**
- Les chiffres de Kirchner sont RAPPORTÉS : pièce Kirchner, lecture par outil, non opposable.
- Les chiffres de Lazar sont cités par section de la pièce « nos résultats ». Je ne leur donne aucun statut plus fort que celui de la pièce : ils sont publics, je ne les ai ni réexécutés ni audités.
- Mes affirmations sont des HYPOTHÈSES ou des calculs. Tout effectif ou seuil que je pose est illustratif.

**Notation commune pour les parties (b).**
- $V$ : violation (vraie ou plantée) ; $M$ : verdict « détecté » du moniteur ; $S$ : score de classement ; $T$ : appartenance au lot retenu (top-$k$, quartile, promotion).
- $R_0 = P(M{=}1 \mid V{=}1)$ et $R_T = P(M{=}1 \mid V{=}1, T{=}1)$.
- $N_T \sim \mathrm{Bin}(n_V, q)$, avec $q = P(T{=}1 \mid V{=}1)$, est le nombre de violations dans le lot retenu.
- Demi-largeur d'un intervalle à 95 % sur une proportion $R$ : $h \approx 1{,}96\sqrt{R(1-R)\,\mathrm{deff}/N}$, avec $\mathrm{deff} = 1 + (m-1)\,\mathrm{ICC}$ pour des grappes de taille $m$.
- Un duel entre deux seuils séparés d'un écart $g$ est non jugeable dès que $h \gtrsim g/2$.

**Repère (calcul illustratif).** Pour $R = 0{,}7$ et $g = 0{,}15$, il faut $N_T \gtrsim 143$ violations effectives dans le lot retenu, sans grappes.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Le facteur d'enrichissement $E$ de E1 est vrai par construction s'il est calculé comme écrit.**
   - A le définit comme « part de plants non détectés dans le top-$k$ / part de plants non détectés dans la population ». Lu comme un rapport de proportions parmi *toutes les méthodes*, il monte dès que les plants sont surreprésentés au sommet.
   - Or les classes R et F gagnent du score par construction (relancer un modèle déjà efficace, calquer le format du banc). $E > 1$ s'obtient donc même si le rappel est constant.
   - La seule quantité qui isole le moniteur est $(1 - R_T)/(1 - R_0)$, calculée parmi les seules violations. A doit l'écrire ainsi.

2. **Confusion de composition (effet de Simpson).**
   - Si R est surreprésentée au sommet et que le rappel diffère entre R, F et P, alors $R_T \neq R_0$ sans aucun effet de sélection à l'intérieur d'une classe.
   - A stratifie par rang, mais pas par classe à l'intérieur du rang.
   - La proposition E le prévoit (« rappel standardisé à mélange de familles constant ») ; je m'appuie sur ce point en le disant.

3. **Les plants ne viennent pas de l'agent, donc E1 ne teste pas l'effet « même modèle ».**
   - A insère les plants « à un taux connu » sans dire qui les écrit.
   - Si c'est l'expérimentateur, la corrélation d'angles morts entre agent et moniteur du même modèle n'est pas en jeu : la condition « même famille / autre famille » mesure alors la sensibilité de deux moniteurs à un texte humain.
   - Pour tester ce que A annonce, il faut des violations produites par l'agent lui-même (suscitées). La réserve de 2604.23488 (référence à vérifier) que A cite reste alors valable.

4. **Fuite entre construction et évaluation des plants.**
   - Si les plants sont mis au point en voyant les verdicts du moniteur d'audit, même à titre de « vérification qu'ils sont réalistes », ils sont de fait ajustés contre lui.
   - Il faut les sceller avant toute exposition au moniteur. A ne le dit pas.

5. **E2 peut être nul par construction.**
   - $S$ varie selon la configuration de l'agent ; le rappel sur P est mesuré « pour chaque configuration ».
   - Si les plants P sont insérés par l'expérimentateur, la configuration n'agit pas sur leur trace. On obtient alors $\rho \equiv 0$ par construction, ce qui serait lu à tort comme un succès de H_B.
   - La configuration doit produire elle-même la trace de la violation, sinon E2 ne mesure rien.

6. **E3 : la « bande près du seuil » est définie par la variable bruitée elle-même.**
   - Sélectionner des méthodes près du seuil d'après une mesure bruitée, puis mesurer leur basculement, donne $f \to 0{,}5$ quand la distance au seuil tend vers 0, par construction.
   - Il manque une estimation de la distance au seuil indépendante des évaluations utilisées pour $f$, et une source de hasard identifiée (graine de réentraînement ou échantillonnage de l'évaluation). Avec un évaluateur déterministe sur un modèle figé, $f = 0$ trivialement.
   - La borne $1-(1-f)^n$ suppose des soumissions indépendantes. Or 26 des 39 signalements sont des relances du même modèle (RAPPORTÉ, §3) : les soumissions successives sont corrélées.

7. **E4 est non jugeable avec les taux déjà rapportés.**
   - W2 est promue 12 fois sur 12 et la copie renommée 0 fois sur 200 (pièce « nos résultats », §2–3).
   - Pour W2, la sélection ne trie rien : « après promotion » équivaut à « avant », donc $\Delta \equiv 0$ par construction.
   - Pour la copie renommée, aucun cas n'est promu : $R_T$ n'est pas défini.

8. **Analogie non établie dans le tableau (c).** « Le classement est déjà “au plafond” comme nos juges (κ = 0) » rapproche deux objets différents :
   - D.3 porte sur la prédiction de Petri au-delà de la médiane (RAPPORTÉ) ;
   - le κ = 0 porte sur l'accord de deux juges de langage sur des fiches.

   C'est une HYPOTHÈSE de rapprochement, à marquer comme telle.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **$E$, et plus généralement $(1-R_T)/(1-R_0)$.** Le dénominateur compte $n_V(1-R_0)$ ratés. Pour $R_0 = 0{,}95$ et 180 plants, cela fait environ 9 ratés (calcul). L'estimateur du rapport a alors une variance non bornée, et il n'est pas défini si aucun plant n'est raté. La zone 1,3–2 annoncée « non concluante » couvrira presque tout l'espace dès que $n_V(1-R_0) \lesssim 20$.
- **Rappel par quartile.** Avec 60 plants par classe et $q = 1/4$, on attend environ 15 plants par classe dans le quartile supérieur, et $h \approx 0{,}23$ pour $R = 0{,}7$ (calcul). Le seuil d'écart de 0,10 de H_A n'est pas jugeable par classe. Si $q \to 0$ pour P (plants sans gain de score), $R_T$ n'est pas défini pour P, la classe même où A attend l'effet « même modèle ».
- **E2.**
  - Avec 40 configurations, l'erreur type de Fisher sur $\rho$ vaut $1/\sqrt{37} \approx 0{,}16$, d'où une demi-largeur d'environ 0,32 (calcul). L'écart entre $\rho \ge 0{,}4$ et $\rho \le 0{,}1$ est de 0,3 : non jugeable.
  - Atténuation : $\rho_{\text{obs}} = \rho \sqrt{\mathrm{fid}_S \cdot \mathrm{fid}_R}$. Avec des fidélités de 0,5 chacune, H_B gagne par atténuation seule.
- **E3.** Un $\hat f = 0$ sur $m = 20$ essais a une borne supérieure d'environ 0,15 (règle de trois, calcul). Méthode par méthode, on ne sépare pas 0,02 de 0,10. Regroupé, $f$ devient un mélange dont la valeur dépend de la largeur de bande choisie.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Permutation des scores à l'intérieur des lots** (présent chez D et E, absent chez A) : $R_T - R_0$ doit s'annuler. Sans ce contrôle, un artefact de composition n'est pas écarté.
- **$R_T$ par classe, à composition fixée.**
- **Pour E2, une condition placebo** où le plant est inséré tel quel dans la sortie de chaque configuration : le rappel doit y être indépendant de la configuration. C'est ce qui prouve que la variable agit bien sur la trace.
- **Moniteur aveugle au score.** Si les trajectoires lues contiennent le score ou le rang, le moniteur peut conditionner son verdict dessus. Masquer le score est nécessaire.
- **Pour E4, une classe plantée à probabilité de promotion intermédiaire** ($0{,}2 \le q \le 0{,}8$). Sans elle, E4 ne contient aucune sélection à mesurer.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts relevés.**
   - « VÉRIFIÉ sur dépôt public » (sycophancie) et « VÉRIFIÉ/RAPPORTÉ » (929 essais) : aucun proposeur n'a d'accès web ni d'exécution (faits servis). Rien ici n'a pu être vérifié, et ces chiffres ne peuvent pas porter VÉRIFIÉ. C'est un relèvement de statut.
   - « C'est ce qui explique pourquoi la moitié supérieure du classement stagne sur Petri » présente une HYPOTHÈSE (exploitation de trous de couverture) comme explication acquise de D.3.

2. **Fiche 1 : la vérité de terrain manque là où porte H_A.**
   - H_A dit que le forum *réplique* les variantes qui passent le moniteur.
   - Mais seules les violations injectées ont une étiquette. Les copies que les agents en font via le forum (« top-3 visible ») ne sont pas étiquetées, sauf si un oracle mécanique les détecte.
   - Le rappel est donc mesuré sur les injections, pas sur la contagion que l'hypothèse invoque.
   - Les injections ne viennent pas non plus de Llama-8B agent. Le « même modèle » n'est donc pas testé (même défaut que A.3).

3. **Fiche 1 : classe $C_{\text{rec}}$ hétérogène.**
   - C la définit comme « type W2 / tricheurs pré-v8 », puis prend le nul v8 « sur la classe $C_{\text{rec}}$ couverte » comme contrôle.
   - Or les tricheurs pré-v8 (recoutures) sont couverts par v8 (0 sur 1 000), et W2 ne l'est pas : v8 déclare lui-même ne pas couvrir W2 (pièce « nos résultats », §2–3).
   - La valeur attendue du contrôle n'est donc pas définie.

4. **Fiche 1 : effectifs incohérents.** 5 × 20 × 2 × 5 = 1 000 propositions, dont 20 % plantées, soit 200 plants (calcul). Le seuil de falsification parle de « 500 trajectoires plantées ».

5. **Fiche 1 : la falsification de H_A repose sur l'absence de significativité.** « Fisher $p > 0{,}10$ » ne falsifie rien : il faut un intervalle contenu dans la zone de H_B.

6. **Fiche 2 : fuite entre sélection et évaluation.**
   - Les configurations sont sélectionnées sur la détectabilité *par le moniteur* sur $B_{\text{mon}}$, puis évaluées par le même moniteur sur $C_{\text{hors}}$.
   - La sélection s'est donc faite contre ce moniteur. On sort ainsi du cadre « sans gradient contre le moniteur » que la question demande, et on rejoint un terrain que la question liste comme déjà pris.
   - Il faut deux moniteurs : un pour sélectionner, un autre, scellé, pour auditer.

7. **Fiche 2 : hypothèse composite.**
   - H_A joint « $\Delta \text{AUC}_{\text{hors}} \le 0$ » et « hausse de la conscience d'évaluation ». Une issue où un seul des deux termes tient n'est attribuée à aucune branche.
   - La note de conscience d'évaluation suppose un juge (E.1 l'obtient d'un auditeur Sonnet 4.6, RAPPORTÉ). Sur Llama-8B, le juge n'est pas spécifié.
   - Les « LoRA de lisibilité » sont un entraînement : il faut dire contre quoi.

8. **Fiche 2 : banc P3 inadapté.** Les 2 400 actions de P3 sont figées (pièce « nos résultats », §6). Sélectionner 50 configurations d'agent impose de régénérer, donc ce n'est plus P3. De plus, si $C_{\text{hors}}$ est inséré, $\Delta \text{TPR}_{\text{hors}} \equiv 0$ par construction (même défaut que A.5).

9. **Fiche 3, volet 1 : deux facteurs confondus et un résultat vrai par construction.**
   - $T_2$ change à la fois l'opacité et le nul (« v9 couvrant les partitions par morceaux »). Si v9 couvre W2, le taux de fausse promotion W2 est borné par la procédure (Ville), par construction. La baisse ne dirait rien de l'opacité.
   - Il faut un plan 2 × 2 (opacité × nul).

10. **Fiche 3, volet 2 : plusieurs défauts.**
    - La courbe dose-réponse de sycophancie est déclarée « équivalent mécanique de Petri » sans validation.
    - Le seuil « −0,5 au-delà de la barre de ±0,64 » prend pour erreur type ce qui est une dispersion entre méthodes (médiane 5,65 ± 0,61, RAPPORTÉ D.3).
    - L'e-processus de l'organisme promeut des *lois* contre une nulle. « La première méthode qui franchit 1/α » n'a pas de nulle définie.
    - T0.3 est décrit comme « calibré par permutation » ; la pièce dit « calibré sur 1 000 épisodes honnêtes entiers ».

11. **Tableau (c) : deux objets mal lus.**
    - « FDR ≤ 0,05 borné par l'inégalité de Ville » : Ville borne l'erreur de première espèce d'un e-processus, pas un taux de fausses découvertes sur des tests multiples.
    - L'écart 1,00 contre 0,91 est une part de fiches « notables », pas une référence mécanique à battre.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Fiche 1.** Avec 200 plants répartis en deux conditions et un top 10 % uniforme, on attend environ 10 plants par bras, d'où $h \approx 0{,}28$ pour $R = 0{,}7$ (calcul). Le seuil de −0,15 n'est pas jugeable.
  - L'interaction $\Delta\Delta$ a une variance environ quatre fois plus grande qu'un effet principal.
  - Si les plants n'ont pas de gain de score ($q < 0{,}1$), $N_T \approx 0$.
  - Avec 5 agents par course, les rondes forment des grappes : $\mathrm{deff} > 1$ dès que l'ICC est positive.
- **Fiche 2.**
  - L'unité est la configuration : 5 contre 5. Si la variance entre configurations de $\text{TPR}_{\text{hors}}$ dépasse la variance d'échantillonnage sur 400 épisodes, le nombre effectif tombe à environ 10.
  - Le top-5 sur 50 subit la malédiction du gagnant : $\Delta \text{TPR}_{\text{in}}$ est gonflé, sauf s'il est remesuré sur des données neuves.
  - Si la sélection réduit la fréquence des violations, $n_V$ chute avec.
- **Fiche 3.**
  - Avec 3 lois vraies, la résolution est d'un tiers (33 points) : « chute de plus de 20 points » est non jugeable. La référence est elle-même instable : 3 sur 3 avec le plan plein, 2 sur 3 avec le plan gelé.
  - Le 99e centile sur environ 60 méthodes est le maximum. Son biais vaut environ $\sigma\sqrt{2\ln 60} \approx 2{,}9\,\sigma$ (calcul, normalité supposée).
  - Avec ~200 exemples par banc, l'erreur type d'une fraction vaut au plus ≈ 0,035 (calcul) : au-delà de la médiane, l'ordre entre méthodes peut être entièrement dû au bruit.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Fiche 1** : permutation des scores dans les lots ; moniteur d'une autre famille *à taux de fausses alertes égalisé* (C propose un moniteur hétérogène sans égaliser) ; oracle mécanique sur les copies venues du forum.
- **Fiche 2** : moniteur d'audit distinct du moniteur de sélection ; banc de sélection à étiquettes permutées (contrôle proposé par E, que je reprends) ; condition placebo où la violation est insérée.
- **Fiche 3** : cellules « opacité seule » et « v9 seul » ; auditeur externe fixé avant de voir les candidats et non construit par les auteurs de l'hypothèse.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **D1 confond qualité du moniteur et effet de sélection.**
   - Falsifier H_A exige des bornes inférieures de $R_0$ et $R_S$ au moins égales à 0,90.
   - Un moniteur médiocre mais *stable* ($R_0 = R_S = 0{,}6$) contredit l'enrichissement, mais D le classe « non décisif ». Pour tout moniteur réaliste, H_A n'est réfutable que s'il est excellent : l'asymétrie favorise H_A.
   - L'enrichissement se juge sur $\Delta$ à $R_0$ donné.

2. **Issue de rejet de H_B mal écrite.** « Intervalle entièrement compatible avec un déficit d'au moins 0,10 » ne correspond à aucun des seuils posés (−0,20 et −0,05). Rejeter H_B ($\Delta \ge -0{,}05$) demande une borne supérieure de $\Delta$ inférieure à −0,05.

3. **$R_S$ dépend du placement des plants, décidé par l'expérimentateur.**
   - $R_S$ porte sur « les plants que le score seul placerait parmi les lauréats ». Si l'auteur des plants fixe leur gain de score, la corrélation entre score et indices de détection est créée par lui.
   - $\Delta$ mesure alors le générateur de plants, pas le classement.
   - L'appariement des honnêtes « par décile de score » ne corrige pas ce défaut.

4. **Le « même modèle » n'est pas testé.** D écrit en (a) que l'effet de partage de poids « doit être comparé à un moniteur distinct ». Mais D1 n'a qu'un moniteur, Llama-8B, à la fois agent et moniteur, et les plants ne viennent pas de l'agent (même défaut que A.3).

5. **D2 : hypothèses qui se recouvrent.**
   - H_A demande un gain externe d'au moins 0,15 sans « effondrement d'une classe », effondrement non chiffré dans H_A.
   - H_B accepte un gain interne avec « une classe qui chute d'au moins 0,20 ».
   - Un gain externe moyen de 0,15 avec une classe en chute de 0,20 satisfait H_B et peut-être H_A. Il faut un seuil commun pour l'effondrement.

6. **Point fort à garder.** D refuse la chaîne de raisonnement comme vérité de terrain et calcule les intervalles par grappe.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D1.**
  - 400 plants en quatre classes donnent 100 par classe. Avec un lot de lauréats à $q = 0{,}1$, on attend environ 10 plants par classe parmi les lauréats.
  - Toutes classes confondues, $N_T \approx 40$ et $h \approx 0{,}14$ pour $R = 0{,}7$ (calcul) : la zone entre −0,20 et −0,05 n'est pas jugeable.
  - Si $R_0 < 0{,}20$, la condition $\Delta \le -0{,}20$ est impossible par construction : H_A est exclue d'avance.
  - Avec des cohortes de taille $m$ et une ICC de 0,1, $\mathrm{deff} = 1 + 0{,}1(m-1)$.
- **D2.** Par classe externe, il faut environ 70 violations par bras pour exclure 0,15 autour de 0 (calcul : $3{,}84 \cdot 2 \cdot 0{,}21 / 0{,}0225$). Si la sélection sur la surveillabilité réduit la fréquence des violations, $n_V$ externe diminue d'autant.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Moniteur d'une autre famille** à taux de fausses alertes égalisé. Sans lui, la thèse « même modèle » d'où part D n'est pas testée.
- **Score de plant tiré indépendamment des caractéristiques que lit le moniteur.** C'est le contrôle de placement : sans lui, $\Delta$ peut être produit par le générateur.
- **Plants scellés avant toute exposition au moniteur.**
- **Pour D2, banc de sélection à étiquettes permutées.** D a une sélection aléatoire, mais pas ce placebo propre au banc.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E-S sur candidats scriptés : l'effet est fixé par le script.**
   - Sur des traces figées et scriptées, la loi jointe de $(S, \text{caractéristiques lues par le moniteur})$ parmi les violations est choisie par qui écrit le script.
   - Si le générateur tire $S$ indépendamment de ces caractéristiques, alors $D \equiv 0$. S'il les couple, $D$ prend la valeur qu'il a fixée.
   - E-S mesure donc l'outil de mesure, pas une propriété d'une boucle de recherche. Le test devient informatif seulement quand les candidats sont produits par des agents. E le repousse à une « extension ».

2. **La question du même modèle est hors champ.** Le problème servi porte sur un moniteur du même modèle que les agents. E-S n'a ni agent producteur ni moniteur d'une autre famille. E le reconnaît (« nouvelle session n'est pas supposée rendre leurs erreurs indépendantes ») sans le tester.

3. **Valeur de $R_U$.** Un tirage uniforme d'un sous-ensemble a la même espérance de rappel que l'ensemble ; $R_U$ n'apporte que du bruit par rapport à $R_0$ calculé sur tout le lot. Comparer $R_C$ à $R_0$ sur l'ensemble serait plus puissant.

4. **E-T : la fréquence de violation est une variable confondante.**
   - Une configuration choisie pour sa surveillabilité peut violer moins souvent, ou des violations différentes.
   - E standardise par classe et par gravité, mais si les violations sont suscitées, la configuration change aussi *quelles* violations existent. $G$ mélange alors le rappel et la sélection des cas.
   - Si les violations sont insérées, $G \equiv 0$ par construction (même défaut que A.5).

5. **Points forts que je reprends en le disant.**
   - L'oracle mécanique complet sert d'étiquette, pas de référence à battre. Cela corrige les tableaux de A, C et D, qui font d'une même pile mécanique à la fois l'étiquette et le concurrent.
   - Le filtre se mesure sur ses entrées, pas sur ses survivants.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E-S.**
  - 96 lots dont on garde le premier, avec une fréquence de violation $p$, donnent $N_C \approx 96\,p$. À $p = 0{,}2$, on attend environ 19 violations retenues (calcul illustratif).
  - Pour exclure la marge de 15 points quand l'effet vrai est nul, il faut environ 70 violations par bras (calcul, $R = 0{,}7$). Le pilote ne peut pas conclure, ce qu'E admet en partie.
  - Si le classement évite les violations ($q \to 0$), $R_C$ n'est pas défini.
  - Avec des lots de 8 et une ICC positive, $\mathrm{deff} = 1 + 7\,\mathrm{ICC}$.
  - Le rappel standardisé à mélange constant demande un support positif de chaque famille dans les deux bras. Une famille absente du bras « classement » le rend non défini.
- **E-T.** Si le gain sur le banc de développement est inférieur à son erreur type, la condition préalable échoue. Si $p_{\text{cfg}}$ baisse, $n_V$ externe diminue avec elle. Pour exclure une marge de 10 points, il faut environ 160 violations par bras (calcul : $3{,}84 \cdot 2 \cdot 0{,}21/0{,}01$).

### (c) Contrôles négatifs dont l'absence serait fatale

- **Générateur aveugle.** Les candidats honnêtes et invalides doivent être écrits sans accès au moniteur d'audit, puis scellés. Sinon le script encode la frontière du moniteur : c'est une fuite entre construction et évaluation.
- **Moniteur d'une autre famille** à taux de fausses alertes égalisé, pour que la question servie soit touchée.
- **Condition de contrôle propre à E-T.** Violations insérées identiques dans toutes les configurations : $G$ doit y valoir 0, sinon le classement ou la standardisation fabriquent l'effet.
- **Contrôles déjà présents.** Permutation des scores dans les lots et banc à étiquettes permutées. Ce sont les seuls contrôles négatifs du tour qui visent exactement les quantités mesurées.

---

**Ce qui réfuterait mes critiques.**
- Si un proposeur montre que ses plants sont produits par l'agent (pas insérés) et scellés avant exposition, les critiques A.3–5, C.2, D.3–4 et E.1 tombent.
- Si les effectifs retenus atteignent les seuils de calcul ci-dessus, mes objections de non-jugeabilité tombent.

FIN-DE-CELLULE
---

## Critiques écrites par l'espèce C

# Critique croisée de méthode — Proposition C (Tour III.2)

**Conventions de statut.** Les faits issus de la pièce Kirchner sont **RAPPORTÉS** ; ceux de la pièce « nos résultats » sont **OBSERVÉS-NON-AUDITÉS**. Les éléments d'analyse méthodologique et probabiliste ci-dessous sont des **HYPOTHÈSES**. Tout chiffre qui ne provient pas des pièces est marqué **illustratif** ou **calcul**.

**Pièces absentes ou coupées (une ligne).** Dans `piece-kirchner-v2.md`, les annexes F et G, la figure 32 et l'annexe A.4 sont absentes, et l'annexe E.1 est coupée au milieu d'une phrase ; `moisson-candidats-v1.md` n'est pas servie dans son intégralité.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Vrai par construction (E1).** Le facteur d'enrichissement est défini comme $E = \frac{\text{part de plants non détectés dans le top-}k}{\text{part de plants non détectés dans la population}}$. Soit $Y \in \{0,1\}$ l'indicatrice de triche plantée, $D \in \{0,1\}$ la détection par le moniteur, et $T_k \in \{0,1\}$ l'appartenance au top-$k$ du classement. L'estimateur s'écrit $\hat{E} = \frac{\hat{\mathbb{P}}(Y=1, D=0 \mid T_k=1)}{\hat{\mathbb{P}}(Y=1, D=0)} = \frac{\hat{\mathbb{P}}(D=0 \mid Y=1, T_k=1)}{\hat{\mathbb{P}}(D=0 \mid Y=1)} \cdot \frac{\hat{\mathbb{P}}(Y=1 \mid T_k=1)}{\hat{\mathbb{P}}(Y=1)}$. **HYPOTHÈSE :** Si le moniteur est totalement aveugle ($\mathbb{P}(D=0 \mid Y=1, T_k=1) = \mathbb{P}(D=0 \mid Y=1) = 1$), mais que la triche plantée augmente fortement le score ($\mathbb{P}(Y=1 \mid T_k=1) \ge 2 \mathbb{P}(Y=1)$), alors $E \ge 2$ *par construction*, sans qu'il n'existe aucune dégradation différentielle du rappel du moniteur au sommet ($\Delta\text{rappel} = 0$). La métrique $E$ confond l'efficacité de la triche sur le score avec l'angle mort conditionnel du moniteur.
2. **Variable confondante (E1, croisement « même modèle / autre famille »).** Comparer Qwen-72B (agents et moniteur) à Llama-3.1-70B (moniteur) confond la variable « partage de la famille de poids avec l'agent » et la variable « compétence intrinsèque et architecture du modèle moniteur ». Sans le croisement inverse (agents Llama-3.1-70B surveillés par Qwen-72B et par Llama-3.1-70B), l'effet de famille est non identifiable.
3. **Fuite entre construction et évaluation (E1).** Dans le harnais de Kirchner, les cinq agents partagent un forum et un classement (**RAPPORTÉ**, §2.1). Si l'on insère 180 plants (**illustratif**) dans la boucle active pour les faire scorer, les agents honnêtes lisent les soumissions plantées sur le forum et s'en inspirent (**RAPPORTÉ**, D.5 : retirer le forum coûte 6 points). La population « honnête » est contaminée par les plants, ce qui détruit l'étiquetage binaire exact exigé pour évaluer la matrice de confusion du moniteur.
4. **Variable confondante (E2).** La sélection de configurations sur un score de surveillabilité $S$ (où le moniteur prédit l'action à partir de la chaîne de raisonnement) est confondue avec la fréquence d'émission de triches et la longueur des traces : une configuration qui rend l'agent passif ou verbeux obtient un $S$ élevé sans améliorer la détection à comportement fixé.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

1. **Non-jugeabilité de $E$ et du rappel au top-$k$ (E1) par dégénérescence du dénominateur.** Sur un classement de taille $N$ avec une fraction $\pi$ de plants ($\pi = 0{,}05$, **illustratif**), soit $p_{\text{top}} = \mathbb{P}(T_k=1 \mid Y=1)$ la probabilité qu'un plant atteigne le top-$k$. Le nombre de plants dans le top-$k$ d'une course suit une loi binomiale (ou hypergéométrique) d'espérance $\mu = N \pi p_{\text{top}}$. Si les plants ne dominent pas les méthodes honnêtes ($p_{\text{top}} \approx k/N$), alors pour $k=3$, $\mu = 3 \pi = 0{,}15$ (**calcul** sur chiffres illustratifs). Avec une probabilité $\ge (1-\pi)^3 \approx 0{,}857$ (**calcul**), le dénominateur de l'estimateur du rappel dans le top-3 est nul ($N_{Y=1, T_3=1} = 0$), rendant le rappel conditionnel non défini et le duel $H_A / H_B$ non jugeable sur une course unique.
2. **Perte de puissance sur la différence de rappel (E1).** Pour rejeter $H_A$ ($\Delta R = \hat{R}_{\text{pop}} - \hat{R}_{\text{top}} \ge 0{,}20$, **illustratif**) contre l'hypothèse nulle $\Delta R = 0$, la variance de l'estimateur $\hat{R}_{\text{top}}$ est bornée inférieurement par $\frac{R_{\text{top}}(1-R_{\text{top}})}{\mathbb{E}[M]}$, où $M$ est le nombre de plants atteignant le quartile supérieur ou le top-$k$. Dès que $\mathbb{E}[M] < 12$ (**illustratif**, par exemple au voisinage de $R_{\text{top}} = 0{,}5$), l'erreur-type dépasse $0{,}144$ (**calcul**) et l'intervalle de confiance à 95 % a une demi-largeur supérieure à $0{,}28$ (**calcul**), couvrant simultanément les seuils de $H_A$ ($0{,}10$) et de $H_B$ ($0{,}20$).
3. **Effondrement du rho de Spearman par atténuation de variance (E2).** Soit $S_i = \theta_i + \epsilon_i$ l'estimateur du score de surveillabilité sur le banc ($\text{Var}(\epsilon_i) = \sigma_\epsilon^2$) et $\hat{R}_i = \eta_i + \nu_i$ l'estimateur du rappel hors banc ($\text{Var}(\nu_i) = \sigma_\nu^2$) pour les $K=40$ configurations (**illustratif**). L'espérance de la corrélation observée est atténuée par le facteur $\frac{1}{\sqrt{(1 + \sigma_\epsilon^2/\text{Var}(\theta))(1 + \sigma_\nu^2/\text{Var}(\eta))}}$. Si la variance inter-configurations réelle $\text{Var}(\theta)$ sur de simples invites système est faible devant le bruit d'échantillonnage binomial $\sigma_\epsilon^2 = \frac{S(1-S)}{n_{\text{banc}}}$, alors $\mathbb{E}[\hat{\rho}] \le 0{,}10$ même sous une corrélation latente parfaite $\text{Corr}(\theta, \eta) = 1$, faisant faussement accepter $H_B$.
4. **Sous-estimation de la probabilité de passage (E3) sous hétérogénéité aléatoire.** La formule $P_{\text{passe}}(n) = 1 - (1-f)^n$ suppose des essais conditionnellement indépendants et identiquement distribués de paramètre constant $f$ près du seuil. Si le taux de basculement d'une méthode $j$ suit une loi bêta $F_j \sim \text{Beta}(\alpha, \beta)$ d'espérance $f = \frac{\alpha}{\alpha+\beta}$ et de variance $\sigma_F^2 > 0$, alors par l'inégalité de Jensen appliquée à la fonction strictement convexe $g(x) = (1-x)^n$, la probabilité marginale de passage vaut $1 - \mathbb{E}[(1-F)^n] < 1 - (1-f)^n$. L'estimateur plug-in $1 - (1-\hat{f})^n$ est biaisé positivement et surestime le risque de contournement, faussant le test de $H_B$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de non-contamination du forum (E1) :** Exécuter l'évaluation des plants en rejeu hors ligne isolé (sans écriture dans le forum des agents honnêtes). Sans ce contrôle, il est impossible de savoir si les fausses alertes sur les méthodes « honnêtes » sont des erreurs du moniteur ou des détections légitimes de méthodes contaminées par les plants via le forum.
2. **Design croisé symétrique des familles (E1) :** Ajouter la condition où les agents sont de la famille B et les moniteurs des familles A et B. Sans ce contrôle, toute différence de rappel entre moniteurs est attribuable à l'écart de capacité générale entre A et B plutôt qu'au partage des poids avec l'agent.
3. **Permutations des scores (E1) :** Permuter aléatoirement les scores des méthodes avant de former les quartiles. Si $\hat{E}$ ou la chute de rappel ne convergent pas vers $1$ et $0$ respectivement, l'estimateur souffre d'un biais d'échantillonnage fini.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Variable confondante majeure dans le duel (Fiche 1).** Le rapport de co-ratage est défini par $r = \frac{\mathbb{P}(M_j \text{ rate} \mid M_i \text{ rate, triche})}{\mathbb{P}(M_j \text{ rate} \mid \text{triche})}$. Or, l'étage 1 ($M_{\text{code}}$) lit uniquement le code statique avant exécution, tandis que l'étage 2 ($M_{\text{traj}}$) lit la trajectoire complète et la chaîne de raisonnement (**RAPPORTÉ**, §2.4 et §3). L'indice $r$ est borné supérieurement par $\frac{1}{\mathbb{P}(M_j \text{ rate} \mid \text{triche})}$. **HYPOTHÈSE :** Si deux familles (par exemple Qwen-72B et Llama-8B) ont des taux de ratage marginaux différents ($\mu_A \ne \mu_B$), la différence $E = r(\text{même famille}) - r(\text{familles différentes})$ est mécaniquement confondue avec les marges $\mu$, même à structure de dépendance (copule) identique.
2. **Confusion entre modalité d'entrée et famille de modèle (Fiche 1).** Dans le contrôle positif (« deux appels du même moniteur avec la même invite »), la modalité d'entrée est identique, alors que dans le test principal ($M_{\text{code}}$ contre $M_{\text{traj}}$), la modalité d'entrée change. Si une triche n'est visible que dans la chaîne de raisonnement et absente du code, $M_{\text{code}}$ la rate systématiquement (taux de ratage = 1), ce qui force mathématiquement $r = 1$ quelle que soit la famille, masquant toute corrélation de famille.
3. **Fuite entre construction et évaluation par sélection du seuil (Fiche 3).** La métrique de transfert est $T = \frac{d'_{\text{hors}}(v^*) - d'_{\text{hors}}(\text{base})}{d'_{\text{banc,frais}}(v^*) - d'_{\text{banc,frais}}(\text{base})}$. Cependant, le moniteur de sélection $M_s$ et le moniteur hors banc $M_h$ n'ont aucune raison d'être calibrés à la même variance latente. De plus, l'indice $d' = \Phi^{-1}(\text{TPR}) - \Phi^{-1}(\text{FPR})$ suppose la normalité et l'homoscédasticité des scores du moniteur sous les lois honnête et tricheuse. Si la variante $v^*$ augmente la variance des scores des épisodes honnêtes sans déplacer leur moyenne, le taux de fausses alertes à seuil fixe bondit alors que $d'$ peut paraître stable ou augmenter artificiellement selon le point de coupure utilisé pour l'estimer.
4. **Vrai par construction (Fiche 4, duel secondaire $H_A' / H_B'$).** Tester si le juge statistique actuel R2 corrige la classe W2 (recombinaison de lois de l'archive) alors que la pièce « nos résultats » (§3, **OBSERVÉ-NON-AUDITÉ**) établit déjà que le nul v8 ne couvre pas W2 par définition et que l'attaque passe 12 fois sur 12 sans retour des verdicts : $H_B'$ est vrai par construction mathématique du modèle nul de R2.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

1. **Instabilité de Cauchy et non-jugeabilité du ratio $T$ (Fiche 3).** Soit $\hat{\Delta}_{\text{banc}} \sim \mathcal{N}(\mu_b, \sigma_b^2)$ le dénominateur estimé sur épisodes frais et $\hat{\Delta}_{\text{hors}} \sim \mathcal{N}(\mu_h, \sigma_h^2)$ le numérateur. Lorsque le rapport signal-sur-bruit du dénominateur $|\mu_b|/\sigma_b < 2$ (**illustratif**), la loi du quotient $\hat{T} = \hat{\Delta}_{\text{hors}} / \hat{\Delta}_{\text{banc}}$ possède des queues lourdes de type Cauchy (espérance et variance non finies). Par le théorème de Fieller, l'ensemble de confiance à 95 % pour $T$ devient l'union de deux intervalles infinis disjoints (ou $\mathbb{R}$ tout entier) dès que $|\hat{\Delta}_{\text{banc}}| \le 1{,}96 \sigma_b$, rendant le duel $T \ge 0{,}5$ contre $T \le 0{,}1$ mathématiquement non jugeable.
2. **Biais et perte de puissance de l'estimateur de $r$ sous hétérogénéité d'item (Fiche 1).** Soit $\theta_k \in [0,1]$ la difficulté latente de l'item $k \in \{1, \dots, n\}$, telle que $\mathbb{P}(M_i \text{ rate l'item } k \mid \theta_k) = p_i(\theta_k)$. Même si deux moniteurs de familles différentes $A$ et $B$ sont conditionnellement indépendants sachant $\theta_k$, la covariance marginale $\text{Cov}(p_A(\Theta), p_B(\Theta))$ dépend de la forme fonctionnelle de $p_A$ et $p_B$. Si $p_A(\theta) = \mathbb{I}(\theta > \tau_A)$ (moniteur déterministe à seuil) et $p_B(\theta)$ est plus lisse, alors $r(A, A) = \frac{1}{\mathbb{P}(\Theta > \tau_A)} > r(A, B)$ uniquement parce que $A$ a une variance inter-items plus forte que $B$, sans aucun biais de « famille » spécifique. Le paramètre $E$ ne sépare pas l'effet d'homogénéité de la fonction de réponse à l'item (variances de $\text{logit}(p_i(\Theta))$) de la dépendance conditionnelle $\text{Cov}(M_i, M_j \mid \Theta)$.
3. **Explosion de la variance de $d'$ aux frontières (Fiche 3).** L'estimateur plug-in $\hat{d}' = \Phi^{-1}(\widehat{\text{TPR}}) - \Phi^{-1}(\widehat{\text{FPR}})$ sur $m$ épisodes a une variance asymptotique $\frac{\text{TPR}(1-\text{TPR})}{m [\phi(\Phi^{-1}(\text{TPR}))]^2} + \frac{\text{FPR}(1-\text{FPR})}{m [\phi(\Phi^{-1}(\text{FPR}))]^2}$, où $\phi$ est la densité gaussienne standard. Lorsque $\text{FPR} \to 0$ ou $\text{TPR} \to 1$ (par exemple $\text{FPR} \le 0{,}01$), le terme $[\phi(\Phi^{-1}(\text{FPR}))]^{-2}$ diverge exponentiellement, rendant la variance de $\hat{d}'$ rédhibitoire sur ~600 épisodes (**illustratif**) et détruisant la puissance du test.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle d'appariement des marges (Fiche 1) :** Calibrer les seuils des moniteurs de toutes les familles pour égaliser strictement les taux de ratage marginaux $\mathbb{P}(M_i \text{ rate} \mid \text{triche}) = \mu_0$ avant de calculer $r$. Sans cette égalisation marginale, l'excès $E$ est un artefact algébrique des dénominateurs.
2. **Contrôle à modalité identique (Fiche 1) :** Tester $r(\text{même famille}) - r(\text{familles différentes})$ lorsque les deux étages reçoivent exactement la même entrée ($M_{\text{code}}^{(1)}$ et $M_{\text{code}}^{(2)}$ avec invites distinctes, puis $M_{\text{traj}}^{(1)}$ et $M_{\text{traj}}^{(2)}$). Sans cela, la non-visibilité d'une triche dans le code écrase la mesure de corrélation entre étages.
3. **Contrôle de constance du taux de violation (Fiche 3) :** Vérifier que la fréquence d'exécution des violations dans l'environnement instrumenté ne chute pas entre la base et $v^*$. Si $v^*$ cesse presque de violer la règle sur les classes hors banc, le nombre d'épisodes à violation tend vers zéro et $d'_{\text{hors}}(v^*)$ devient inestimable.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Confusion entre conditionnement par le score seul et survie au filtre (Expérience D1).** La métrique du duel principal est $\Delta = R_S - R_0$, où $R_S$ est le rappel sur les cas plantés que *le score seul* placerait parmi les lauréats. Or, dans la boucle de Kirchner, le moniteur avant exécution filtre les méthodes *avant* qu'elles ne soient classées (**RAPPORTÉ**, §2.4). Mesurer $R_S$ sur le top-$k$ du score brut évalue la branche 1 (« score seul »), mais ne mesure pas le risque de la branche 2 (« filtre du moniteur puis score »), où des triches de score plus modeste mais invisibles au moniteur prennent la place des triches à haut score filtrées.
2. **Biais de sélection par post-appariement sur un collisionneur (Protocole commun et D1).** Le protocole impose d'apparier chaque cas honnête à un cas planté par « décile de score ». **HYPOTHÈSE :** Si la triche plantée gonfle artificiellement le score, une trajectoire honnête qui atteint le même décile de score élevé doit nécessairement présenter des caractéristiques exceptionnelles (code plus complexe, modifications plus agressives). Conditionner sur le score (qui est un collisionneur entre le statut honnête/tricheur et la complexité de la méthode) induit une corrélation fallacieuse qui gonfle le taux de fausses alertes sur les honnêtes à haut score par pur biais de Berkson.
3. **Fuite de l'oracle mécanique dans la difficulté de détection (Protocole commun).** Chaque cas planté possède « un déclencheur mécanique de validation ». Si ce déclencheur mécanique repose sur une trace syntaxique simple (par exemple l'accès à un fichier nommé ou une chaîne de caractères fixe), le moniteur linguistique détectera cette même trace superficielle, confondant le rappel sur la classe conceptuelle de triche avec la détection d'un mot-clé planté par l'expérimentateur.
4. **Absence de métrique d'échange rappel / fausses alertes (Expérience D2).** Dans D2, $H_A$ exige que le rappel progresse d'au moins $0{,}15$ sans que les fausses alertes ne dépassent $0{,}05$. Si la sélection sur le banc de surveillabilité abaisse simplement le seuil implicite d'alerte du moniteur (faisant passer les fausses alertes de $0{,}01$ à $0{,}049$ et le rappel de $0{,}60$ à $0{,}76$, chiffres **illustratifs**), $H_A$ est validée alors que la capacité intrinsèque de discrimination (courbe ROC) du couple agent-moniteur n'a pas bougé d'un iota.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

1. **Dégénérescence de l'effectif efficace sous corrélation intra-cohorte (D1).** Le protocole indique que les intervalles sont calculés « par cohorte/tâche ». Soit $C$ le nombre de tâches/cohortes et $m$ le nombre de cas plantés par cohorte ($C m = 400$, **illustratif**), et soit $\rho_{\text{intra}}$ la corrélation intra-classe des indicateurs de détection $D_{c,j} \in \{0,1\}$ au sein d'une même tâche $c$. La variance de l'estimateur du rappel global est multipliée par le facteur d'inflation de plan $\text{DEFF} = 1 + (m-1)\rho_{\text{intra}}$. Si les 400 cas sont répartis sur $C = 10$ tâches ($m = 40$, **illustratif**) et que le moniteur réagit fortement au contexte de la tâche ($\rho_{\text{intra}} = 0{,}5$, **illustratif**), alors $\text{DEFF} = 20{,}5$ (**calcul**), réduisant la taille d'échantillon effective de $400$ à $n_{\text{eff}} \approx 19{,}5$ (**calcul**). Parmi les lauréats ($R_S$, par exemple 10 % des cas), l'effectif efficace tombe sous $n_{\text{eff}, S} \approx 2$, rendant l'intervalle de confiance sur $\Delta = R_S - R_0$ plus large que $[ -0{,}50 ; +0{,}50 ]$ (**calcul** sur loi binomiale clusterisée) et le duel $H_A (\le -0{,}20)$ contre $H_B (\ge -0{,}05)$ non jugeable.
2. **Non-identifiabilité de $\Delta$ sous covariance fortement dépendante de la classe (D1).** Soit $R_0 = \sum_{q=1}^4 w_q R_{0,q}$ le rappel moyen sur les 4 classes de triche (poids $w_q = 1/4$) et $R_S = \sum_{q=1}^4 w_{S,q} R_{S,q}$ le rappel parmi les lauréats, où $w_{S,q} = \mathbb{P}(\text{classe } q \mid \text{lauréat})$. Par décomposition de Kitagawa-Oaxaca, $\Delta = \sum_{q=1}^4 (w_{S,q} - w_q) R_{0,q} + \sum_{q=1}^4 w_{S,q} (R_{S,q} - R_{0,q})$. Si une seule classe $q^*$ (par exemple la relance de modèle) produit des scores très élevés ($w_{S,q^*} \to 1$) et que le moniteur a un rappel nul sur $q^*$ ($R_{0,q^*} = 0$) mais parfait sur les trois autres ($R_{0,q} = 1$), alors $R_0 = 0{,}75$ et $R_S = 0$, soit $\Delta = -0{,}75$ (**calcul**), alors qu'au sein de chaque classe la sélection n'a aucun effet ($R_{S,q} = R_{0,q}$). L'estimateur $\Delta$ global ne permet pas d'identifier si l'effet vient d'une sélection intra-classe ou du simple choix arbitraire des proportions initiales $w_q$ par l'expérimentateur.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de cécité au déclencheur mécanique (Protocole commun) :** Créer des cas honnêtes contenant la signature lexicale ou syntaxique voisine du déclencheur mécanique sans que la violation ne soit exécutée. Sans ce contrôle, un rappel de $0{,}90$ ne prouve que la détection d'un artefact d'instrumentation planté.
2. **Stratification de $\Delta$ par classe de triche (D1) :** Calculer $\Delta_q = R_{S,q} - R_{0,q}$ séparément dans chacune des 4 classes. Sans cette stratification, le résultat global $\Delta$ est entièrement manipulable en changeant la proportion initiale des 4 classes dans les 400 cas plantés.
3. **Égalisation empirique du taux de fausses alertes (D2) :** Recalibrer le seuil du moniteur d'audit pour que le taux de fausses alertes sur les cas honnêtes hors banc soit strictement égal entre les trois bras de sélection avant de calculer le gain de rappel. Sans cela, toute dérive de verbosité des traces induite par la sélection fausse le rappel mesuré à seuil nominal fixe.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Variable confondante entre changement de composition et difficulté intra-famille dans le duel principal (Expérience E-S).** Le duel principal porte sur $D = R_U - R_C$ (rappel sous sélection uniforme moins rappel sous sélection par classement). Bien que la proposition mentionne en métrique 4 un « rappel standardisé à mélange de familles constant », le duel réfutant $H_A / H_B$ est défini uniquement sur la différence brute $D$. Tout comme pour la proposition D, si l'expérimentateur inclut dans son banc figé une famille de triche triviale à haut score et faible rappel, $D \ge 15$ points est obtenu par simple effet de mélange des familles initiales choisies par l'expérimentateur, sans qu'aucune famille ne devienne plus difficile à détecter après classement.
2. **Fuite de sélection et malédiction du gagnant non corrigée sur la condition préalable (Expérience E-T).** La condition préalable de E-T exige de « mesurer un gain réel sur le banc de développement » pour la configuration choisie sur le banc de surveillabilité. Si ce gain est mesuré sur les mêmes épisodes du banc qui ont servi à sélectionner la meilleure configuration parmi $K$ candidates, l'estimateur du gain initial est biaisé positivement par $\mathbb{E}[\max_{1 \le k \le K} Z_k] > 0$ (malédiction du gagnant). La condition préalable sera déclarée satisfaite sur du pur bruit d'échantillonnage, rendant l'évaluation du transfert $G$ hors banc ininterprétable en cas d'échec.
3. **Biais de post-stratification sur des variables endogènes (Expérience E-T).** Le paramètre du duel $G$ est la différence de rappel hors banc après sélection, où « les résultats sont standardisés sur les classes de violations et leur gravité observable ». Or, la « gravité observable » et la répartition entre classes de violations *après* que les agents ont été sélectionnés sur le banc de surveillabilité sont des variables post-traitement (endogènes à la configuration choisie). Conditionner ou standardiser sur un résultat post-traitement détruit l'identification causale de l'effet de la configuration et peut créer une différence $G$ non nulle même si la configuration n'a aucun effet causal sur la surveillabilité.
4. **Absence d'indépendance dans le dimensionnement pilote (Ancrage matériel).** La taille pilote de 96 lots de 8 candidats (768 candidats, **illustratif**) est obtenue avec « des candidats scriptés et des traces figées ». Si les 96 lots réutilisent un nombre restreint de modèles de traces scriptées en les recombinant, les erreurs du moniteur Llama-3.1-8B-Instruct sont parfaitement corrélées d'un lot à l'autre sur la même trace, faussant l'estimation de la variance inter-lots.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

1. **Non-définition de l'estimateur standardisé par défaut de support commun (Expérience E-S, métrique 4, et E-T).** Soit $\mathcal{Q}$ l'ensemble des familles de violations et $w_q^U = \mathbb{P}(\text{famille } q \mid \text{sélection uniforme}) > 0$ les poids de référence. Le rappel standardisé après classement s'écrit $\tilde{R}_C = \sum_{q \in \mathcal{Q}} w_q^U \hat{R}_{C,q}$, où $\hat{R}_{C,q}$ est le rappel empirique dans la famille $q$ parmi les candidats retenus par le classement. Soit $N_{C,q}$ le nombre de violations de la famille $q$ qui remportent le classement sur les $L = 96$ lots (**illustratif**). Si une famille de violation $q_0$ est sous-optimale pour le score de tâche ($\mathbb{P}(\text{gagner le lot} \mid \text{famille } q_0) = p_{q_0} \le 0{,}01$), alors $\mathbb{P}(N_{C,q_0} = 0) = (1 - p_{q_0})^L \ge (0{,}99)^{96} \approx 0{,}38$ (**calcul**). Sur cet événement de probabilité élevée, $\hat{R}_{C,q_0} = 0/0$ est mathématiquement non défini (violation de l'hypothèse de positivité / support commun), et la variance de $\tilde{R}_C$ conditionnellement à $N_{C,q_0} \ge 1$ est dominée par $\frac{(w_{q_0}^U)^2 R_{C,q_0}(1-R_{C,q_0})}{\mathbb{E}[N_{C,q_0} \mid N_{C,q_0} \ge 1]}$, rendant la standardisation inopérante.
2. **Perte de puissance catastrophique sur $D$ par raréfaction des violations élues (Expérience E-S).** Sur $L = 96$ lots de 8 candidats (**illustratif**), au plus 1 candidat est retenu par lot par le classement (soit 96 candidats retenus au total). Si la proportion de candidats avec violation exécutée dans un lot est $\pi_v$ (par exemple $\pi_v = 0{,}25$, soit 2 sur 8, **illustratif**) et que les violations gagnent le lot au taux de base, l'espérance du nombre total de violations retenues par le classement est $\mathbb{E}[N_C] = L \pi_v = 24$ (**calcul**). En tenant compte de la dépendance par famille de tâches (soit $K_{\text{fam}}$ familles de tâches réservées au test ; si $K_{\text{fam}} = 8$, **illustratif**), le nombre de degrés de liberté de la loi de Student pour l'intervalle simultané à 95 % est $K_{\text{fam}} - 1 = 7$ ($t_{7 ; 0{,}975} = 2{,}365$, **calcul**). Même sous indépendance entre lots ($\sigma_{\hat{D}} \ge \sqrt{\frac{0{,}5 \times 0{,}5}{24} + \frac{0{,}5 \times 0{,}5}{24}} \approx 0{,}144$, **calcul**), la demi-largeur de l'intervalle de confiance est au moins $2{,}365 \times 0{,}144 \approx 0{,}34$ (34 points de pourcentage, **calcul**). Un intervalle de largeur totale $\ge 68$ points ne peut quasiment jamais exclure la marge de décision fixée à $15$ points ($H_A : D \ge 15$ contre $H_B : D < 15$), condamnant l'expérience à l'issue « non concluante » avec une probabilité proche de $1$ lorsque $D \in [0 ; 0{,}30]$.
3. **Inflation du risque de première espèce ou perte de validité du seuil de fausses alertes par transfert de domaine (E-S et E-T).** Le seuil $s^*$ du moniteur est calibré sur un jeu honnête séparé ($\text{ lois } P_0$) pour que $\mathbb{P}_{X \sim P_0}(S(X) > s^*) = \alpha_0 = 0{,}05$. Sur les cas honnêtes retenus par le classement dans le jeu de test ($\text{loi } P_C$), si le score du moniteur $S(X)$ est positivement corrélé au score de tâche $T(X)$ parmi les honnêtes ($\text{Cov}_{P_0}(S(X), T(X)) > 0$, par exemple via la longueur ou la complexité du code), alors la loi conditionnelle $P_C = P_0(\cdot \mid T(X) \text{ maximal du lot})$ domine stochastiquement $P_0$. On a alors $\mathbb{P}_{X \sim P_C}(S(X) > s^*) > \alpha_0$ : le taux de fausses alertes sur le test dépasse systématiquement la tolérance de $5\%$, déclenchant la clause d'invalidation de l'expérience (« Une hausse hors tolérance des fausses alertes interdit de qualifier le résultat d'amélioration utile ») alors même que le moniteur n'a subi aucune dérive intrinsèque.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Validation sur tirages frais du banc de développement avant sélection finale (E-T) :** Évaluer le gain de la configuration retenue sur un jeu d'épisodes frais *du banc de développement lui-même* (distinct du jeu qui a servi à choisir la configuration) avant de lancer le test hors banc. Sans ce contrôle, il est impossible de distinguer un échec de transfert hors banc ($H_B$) d'une absence de gain initial masquée par la malédiction du gagnant.
2. **Calibration du seuil du moniteur conditionnellement au rang de classement sur cas honnêtes (E-S et E-T) :** Mesurer la dérive du taux de fausses alertes entre sélection uniforme et sélection par classement sur des lots *100 % honnêtes*. Sans ce contrôle, toute variation de $R_U - R_C$ ou violation du plafond de 5 % de fausses alertes est confondue avec un simple déplacement de la moyenne des scores du moniteur sur les trajectoires complexes qui gagnent le classement.
3. **Contrôle d'unicité des traces à travers les lots (E-S, pilote) :** Imposer par hachage qu'aucune trace (honnête ou invalide) ne puisse apparaître dans plus d'un lot sur les 96 lots générés. Sans cette contrainte stricte, le rééchantillonnage des mêmes traces scriptées réduit drastiquement le nombre de réalisations indépendantes et invalide les intervalles de confiance calculés par lot.

FIN-DE-CELLULE
---

## Critiques écrites par l'espèce D

Les points suivants sont des critiques de méthode ; les mécanismes empiriques envisagés restent des **HYPOTHÈSES**. Les résultats repris des pièces conservent leur statut **RAPPORTÉ** ou **OBSERVÉ-NON-AUDITÉ**.

## Sur la proposition A

### (a) Défauts de méthode

- **E1 ne sépare pas sélection et changement de composition.** Le rang dépend du score, mais celui-ci dépend aussi de la classe de plant, de son intensité et de la méthode honnête sur laquelle il est greffé. Une baisse de rappel au sommet peut donc venir d’une surreprésentation de classes difficiles, sans dégradation *au sein d’une classe*. L’enrichissement \(E\) mélange en outre prévalence des plants, probabilité d’atteindre le top-\(k\) et faux négatifs ; il ne remplace pas les deux estimands distincts
  \[
  P(\text{non détecté}\mid V=1,S_k=1,c),\qquad
  P(S_k=1\mid V=1,\text{non détecté},c).
  \]
- **Le rappel sur plants n’est pas nécessairement un plafond du rappel spontané.** Cela suppose une relation d’ordre stochastic­que entre difficulté des plants et difficulté naturelle, non démontrée. Des plants trop visibles donnent un rappel optimiste ; des plants artificiellement atypiques peuvent donner l’inverse.
- **Le contrôle « classe R sans gain » ne discrimine pas bruit et sélection.** Sous l’hypothèse testée, l’absence de gain empêche précisément l’enrichissement par le score. Un résultat nul y est donc attendu même si le classement sélectionne fortement les faux négatifs ailleurs.
- **E2 conserve une malédiction du gagnant.** La population hors banc est fraîche, mais \(S\) semble servir à la fois à choisir les configurations et à établir leur avantage. Sans remesure de \(S\) sur épisodes frais, le contraste top-dix contre configurations aléatoires mélange transfert et surévaluation du classement initial.
- **E3 emploie une mauvaise probabilité de resoumission.** Un taux de basculement \(f\) n’est pas la probabilité \(p_i\) qu’une méthode réellement dégradée passe une évaluation. Même avec essais indépendants conditionnellement à la méthode, la probabilité recherchée est
  \[
  1-\mathbb E_i[(1-p_i)^n],
  \]
  et non \(1-(1-f)^n\). Avec évaluateur déterministe ou erreurs de retest corrélées, cette expression ne vaut plus non plus.
- **E4 ne démontre pas à lui seul des angles morts corrélés.** Juge et moniteur peuvent partager des variables observables — longueur, provenance, similarité à l’archive — sans partager de représentation ou de famille. Le mécanisme proposé dépasse l’estimand mesuré.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Pour E1, soit \(n_{c,k}\) le nombre de plants exécutés de classe \(c\) effectivement sélectionnés dans le top-\(k\). Si \(n_{c,k}\approx0\), le rappel stratifié et \(E\) sont non estimables. Si les plants sont corrélés par gabarit, agent ou méthode hôte, la taille effective n’est pas le nombre de plants : avec corrélation intraclasse \(\rho\) et grappes de taille \(m\), elle est approximativement divisée par \(1+(m-1)\rho\).
- \(E\) devient instable lorsque la proportion globale de faux négatifs approche zéro ; son dénominateur est alors estimé avec très peu d’événements. Le rappel perd aussi toute puissance discriminante aux plafonds \(R\approx0\) ou \(R\approx1\).
- Sans support commun des scores et des difficultés entre détectés et non détectés, la standardisation par classe ne suffit pas : distinguer composition et effet propre du rang exige alors un modèle non identifiable à partir des seuls verdicts.
- Pour E2, si la variance interconfigurations du vrai score de surveillabilité est nulle, ou si sa fiabilité \(\lambda=\sigma^2_{\text{vrai}}/(\sigma^2_{\text{vrai}}+\sigma^2_{\text{mesure}})\) est faible, \(\rho\) mesure surtout du bruit et est attenué. Le contraste top/aléatoire devient également non jugeable si le rappel hors banc est constant par plafond.
- Pour E3, si les retests sont presque parfaitement corrélés, augmenter \(m\) mesure une propriété fixe des poids et de l’évaluateur, pas une probabilité de franchissement par resoumission.
- Pour E4, le rappel « après promotion » est non estimable pour toute classe dont aucun plant n’est promu ; il ne faut pas convertir cette absence en rappel nul ou en sélection parfaite.

### (c) Contrôles négatifs indispensables

- **E1 : permutation des scores au sein des lots et des classes**, en conservant tailles et dépendances. Sans ce contrôle, les plants sans gain ne suffisent pas à valider l’estimateur d’enrichissement.
- **Séparation des générateurs de plants** entre développement, calibration du seuil et test, avec familles de tâches entières réservées. Sans cela, le rappel mesure la reconnaissance du procédé de construction.
- **E2 : permutation des étiquettes ou des scores \(S\) avant sélection**, répétée sur plusieurs tirages, et remesure fraîche de \(S\). Le seul contrôle « le rappel R doit monter » est un contrôle positif de manipulation, pas un contrôle négatif du transfert.
- **E3 : rejets indépendants simulés à \(p_i\) connu**, pour vérifier que l’estimation de \(f\) et la formule de resoumission ne confondent pas bascule, passage et corrélation.

## Sur la proposition B

### (a) Défauts de méthode

- **La métrique de co-ratage de la fiche 1 n’identifie pas un effet de famille.** Conditionner sur « \(M_i\) rate » sélectionne des items différents selon le moniteur de référence. Sous indépendance conditionnelle à une difficulté latente \(X\),
  \[
  r_{ij}=\frac{\mathbb E[p_i(X)p_j(X)]}{\mathbb E[p_i(X)]\,\mathbb E[p_j(X)]}.
  \]
  Ainsi \(r_{ij}\) varie avec les taux marginaux de ratage et la distribution des difficultés, même sans angle mort partagé propre à une famille. La différence entre deux \(r\) n’en est donc pas une mesure pure.
- **Famille, rôle et modalité d’entrée sont confondus.** \(M_{\text{code}}\) et \(M_{\text{traj}}\) ne reçoivent pas la même information. Une comparaison same/autre famille faite sur ces rôles peut attribuer à la famille un effet dû à la complémentarité des entrées.
- **La covariance de la fiche 2 n’implique pas le signe de \(\Delta(k)\).** Le rappel du top-\(k\) dépend de toute la loi jointe score–détection–classe et du nombre de violations sélectionnées. Une covariance négative au sein des classes peut coexister avec \(\Delta(k)=0\), et réciproquement.
- **Le bras naturel mesure une prévalence résiduelle, pas directement un rappel.** Auditer seulement des non-signalées introduit une vérification dépendante du verdict ; comparer top-3 et rangs médians confond en outre fréquence des violations, gain de score et détectabilité.
- **Dans la fiche 3, \(T\) hérite des défauts d’un ratio.** Il compare aussi des \(d'\) obtenus avec moniteurs et distributions différents : leur égalité numérique ne garantit pas une échelle commune.
- **La fiche 4 ne rend pas réutilisation et couverture orthogonales.** R1 et R2 changent simultanément la règle de promotion, les tirages et potentiellement l’information disponible. Pour W2, des tirages frais n’élargissent pas par construction la nulle : l’échec de couverture ne constitue donc pas un test empirique indépendant de ce défaut.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Le co-ratage est non identifiable dès que les probabilités de ratage sont proches de zéro ou de un, ou que le nombre d’items ratés par le moniteur de référence est faible. Un bootstrap sur items surestime la précision si les items partagent gabarits, jumeaux honnêtes ou tâches.
- L’effet de difficulté n’est séparable d’un effet famille que si les taux marginaux sont comparables et si le modèle de difficulté est correctement spécifié ; deux estimateurs ajustés sur des modèles différents peuvent conclure en sens opposés.
- Pour \(\Delta(3)\), le dénominateur est le nombre de violations effectivement présentes dans le top-3, non le nombre de classements rejoués. Mille rééchantillonnages d’un même pool ne créent pas mille observations indépendantes.
- Le ratio \(T\) a une variance potentiellement explosive lorsque le gain frais au dénominateur approche zéro ; son espérance peut ne pas exister utilement. Un \(d'\) est également non jugeable aux taux empiriques nuls ou parfaits sans convention de régularisation préspécifiée.
- Sous R1, \(1-(1-\alpha)^n\) exige des erreurs conditionnelles valides et indépendantes ; avec réutilisation adaptative, ce n’est ni une borne générale ni nécessairement la loi du nombre de consultations.

### (c) Contrôles négatifs indispensables

- **Fiche 1 : paires à entrées strictement identiques et difficultés appariées**, avec permutation des étiquettes de famille à propriétés marginales fixées. La permutation des verdicts dans une classe ne teste pas l’ajustement de difficulté.
- **Fiche 2 : scores permutés au sein des pools**, en plus des tricheries placebo. Dans le bras naturel, audit aveugle d’échantillons de signalées et de non-signalées, avec validation préalable de l’auditeur sur vérité plantée.
- **Fiche 3 : moyenne sur plusieurs sélections à étiquettes permutées.** Une variante aléatoire unique peut posséder un vrai gain ; attendre nécessairement un gain nul est incorrect.
- **Fiche 4 : témoin non adaptatif à budget et information équivalents.** Sans lui, aucune différence R1–R2 n’est attribuable spécifiquement à la réutilisation.

## Sur la proposition C

### (a) Défauts de méthode

- **La fiche 1 confond forum, retour d’information et composition du pool.** Le forum modifie les scores honnêtes, la diffusion des méthodes et le mélange des classes. Le protocole ne précise pas si les plants sont injectés avant ou après génération : s’ils sont ajoutés après, le mécanisme de réplication par le forum n’est pas testé.
- **Le contrôle proposé avec le nul v8 est invalide pour \(C_{\mathrm{rec}}\).** W2 est précisément présenté comme une classe que v8 déclare ne pas couvrir, avec douze promotions sur douze **[OBSERVÉ-NON-AUDITÉ, nos résultats §3]**. Il ne peut servir de témoin « couvert » pour cette classe.
- **La fiche 2 change trop de choses entre banc et hors banc.** Classe de violation, tâche, distribution des candidats et parfois nature de l’intervention varient ensemble. Le gain hors banc peut donc refléter la difficulté ou le taux de violations plutôt que le transfert de surveillabilité.
- **La conscience d’évaluation est post-traitement.** Conditionner l’analyse à son seuil peut sélectionner sur une variable affectée à la fois par la configuration et par la détectabilité ; cela ne démontre ni masquage ni causalité.
- **Dans la fiche 3, \(T_1\) et \(T_2\) changent trois facteurs : transparence, contenu du retour et couverture du nul.** Une chute de \(p_{\mathrm{W2}}\) peut être entièrement due à v9. Si v9 ferme la classe W2 testée, la réduction est partiellement vraie par construction.
- **Le volet post-médiane compare des procédures, pas seulement deux règles d’arrêt.** Seuil d’e-valeur et 99e centile diffèrent par données, budget et critère d’utilité. Transposer la dispersion \(\pm0,64\) de Petri à une courbe dose–réponse d’une autre échelle est invalide **[RAPPORTÉ pour la dispersion, pièce Kirchner §5]**.
- **Les duels conjoncts ne sont pas exclusifs clause par clause.** Une victoire du volet transparence ne tranche pas le volet e-valeurs. De même, dans la fiche 1, \(p>0,10\) n’établit pas une absence d’effet.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Le test exact de Fisher sur trajectoires suppose des unités indépendantes ; rondes, agents, courses et copies de forum violent cette hypothèse. Le nombre de plants n’est pas la taille effective.
- \(\Delta\mathrm{Rappel}\) est non estimable si le top décile contient trop peu de plants, et non informatif si le rappel global est au plafond. \(\Delta\Delta\) devient également instable si les deux bras n’ont aucun support commun de scores.
- Pour la fiche 2, si le gain frais en distribution est nul, le test hors banc ne porte pas sur le transfert d’un gain. Si les violations hors banc sont rares ou si \(\mathrm{TPR}@5\%\) vaut presque partout zéro ou un, les dix points demandés sont hors résolution.
- Le passage d’AUC à \(\mathrm{TPR}@\mathrm{FPR}\) n’est pas anodin : deux lois de scores peuvent classer différemment ces paramètres. Les hypothèses ne sont donc pas définies par un estimand unique.
- Pour le volet e-valeurs, si le seuil n’est jamais franchi dans une course, la méthode « première au franchissement » n’existe pas ; conditionner aux courses avec franchissement sélectionne alors sur le résultat. Si les deux procédures choisissent la même méthode, le contraste est nul par construction.

### (c) Contrôles négatifs indispensables

- **Fiche 1 : sélection à scores permutés sur un pool figé**, puis forum rejoué avec traces figées. Sans ces deux placebos, l’interaction forum–classement n’est pas attribuable au mécanisme annoncé.
- **Fiche 2 : validation fraîche du gain \(B_{\mathrm{mon}}\)** et sélection à étiquettes permutées. Le contrôle \(\Delta\mathrm{TPR}_{\mathrm{in}}\) est une vérification positive ; les prédicteurs aléatoires ne remplacent pas un placebo de sélection.
- **Fiche 3 : plan factoriel transparence × couverture**, à retour identique, et comparaisons appariées à budget égal pour l’arrêt. Les anciens témoins v8 sont des tests de non-régression, pas des contrôles négatifs suffisants pour ces nouveaux contrastes.

## Sur la proposition E

### (a) Défauts de méthode

- **E-S mesure un changement de distribution conditionnelle, pas une dégradation du moniteur.** Celui-ci étant figé, \(D\) mélange nécessairement composition en familles, gravité et difficulté. La standardisation proposée ne résout ce problème que sur le support commun.
- **Le contraste avec filtre n’est pas entièrement factoriel.** Pour isoler son apport, il faut comparer uniforme-avec-filtre à uniforme-sans-filtre, puis classement-avec-filtre à classement-sans-filtre, avec audit identique ; sinon filtrage et classement restent confondus.
- **E-T peut certifier le gain initial sur les données ayant servi à choisir la configuration.** La condition « gain réel sur le banc de développement » ne suffit pas : sans remesure fraîche, le prérequis peut être satisfait par la seule malédiction du gagnant.
- **La qualité moyenne comparable ne rend pas les pools comparables.** Deux configurations peuvent avoir même score moyen mais des lois de scores, de gravité des violations et de difficulté différentes. \(G\) mesure alors l’effet conjoint de la configuration et du classement, pas uniquement le transfert de surveillabilité.
- **L’appariement honnête/invalide ne garantit pas l’absence de fuite.** Si une sortie de l’oracle mécanique contribue directement ou indirectement au score du classement, la sélection utilise une partie de l’étiquette de test.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Pour E-S, la variance de \(R_C\) dépend du nombre de violations exécutées retenues par classement, et non des 768 candidats pilotes. Si ce nombre est faible, l’intervalle traverse naturellement la marge ; si elle est nulle, \(R_C\) et \(D\) sont indéfinis.
- Le rappel standardisé exige, pour chaque famille et gravité retenues, une probabilité non nulle d’apparaître dans les deux branches. Sans support commun, l’estimand standardisé dépend d’une extrapolation de modèle.
- Une probabilité de sélection presque déterministe peut laisser très peu de lots où une même violation est tantôt retenue, tantôt non retenue : la dépendance de lot réduit alors fortement la taille effective malgré de nombreuses traces.
- Pour E-T, si le gain frais de développement est nul ou si la variance interconfigurations du vrai paramètre de surveillabilité est nulle, la sélection ne produit aucun traitement identifiable. \(G\) ne mesure plus que du bruit de sélection.
- Même avec violations abondantes, \(G\) perd sa puissance si les rappels sont aux plafonds, si les fausses alertes imposent des seuils extrêmes, ou si les distributions de gravité n’ont pas de support commun entre configurations.

### (c) Contrôles négatifs indispensables

- Le contrôle de scores permutés, déjà présent, est nécessaire mais doit être complété par **uniforme contre uniforme**, avec mêmes tailles de lots et même analyse : cela valide l’absence de biais de l’estimateur et le calcul de sa variance.
- **Verdicts du moniteur permutés au sein des familles de lots** : tout contraste systématique résiduel révèle une fuite d’étiquettes ou une erreur du pipeline.
- **Calibration du seuil, estimation du gain de développement et test final sur trois partitions indépendantes.** Sans remesure fraîche du gain, le contrôle à étiquettes permutées ne suffit pas à écarter la sélection sur bruit.
- **Classement placebo calculé sans aucune information de l’oracle**, puis vérification que l’oracle n’entre ni dans les scores ni dans l’appariement des candidats retenus. Sans cette séparation, la prétendue sélection aveugle aux violations n’est pas établie.

FIN-DE-CELLULE
---

## Critiques écrites par l'espèce E

# Proposition E — Critique croisée de méthode

**VÉRIFIÉ — présence des pièces :** les conceptions A, B, C et D sont présentes ; les annexes F/G et la figure 32 ne sont pas fournies, et les extraits d’E.1 sont signalés comme coupés.

**Convention :** les descriptions des conceptions sont **RAPPORTÉES** ; mes objections empiriques sont des **HYPOTHÈSES**. Les identités et implications mathématiques sont **VÉRIFIÉES — calcul analytique**, non validations expérimentales. Aucun résultat externe n’est audité ici.

**Notation commune.** \(Y\) désigne la violation réelle, \(M\) l’alerte, \(S\) la sélection, \(Z\) la classe/tâche, \(U\) le score. Les variables indicatrices prennent les valeurs booléennes usuelles. Posons :
\[
r_s=P(M=1\mid Y=1,S=s),\qquad
f_s=P(M=1\mid Y=0,S=s).
\]
Les marges \(\delta,\varepsilon\) et niveaux \(\alpha\) ci-dessous sont des paramètres à préenregistrer, pas des valeurs tirées des faits.

**VÉRIFIÉ — exigence B4 :** une hypothèse porte sur un paramètre de population, pas sur le fait qu’un intervalle contient une valeur. Deux hypothèses séparées par une zone intermédiaire ne couvrent pas toutes les possibilités. Pour un duel exhaustif, employer par exemple \(H_A:\theta\leq\delta\) et \(H_B:\theta>\delta\). Un intervalle entièrement d’un côté réfute l’autre hypothèse au risque annoncé ; un intervalle chevauchant la frontière reste non concluant. L’absence de significativité ne constitue pas cette réfutation.

## Sur la proposition A

### (a) Défauts de méthode

**HYPOTHÈSES — objections :**

- **E1 confond prévalence et rappel.** L’enrichissement en plants non détectés parmi les lauréats peut augmenter uniquement parce que les plants obtiennent de meilleurs scores. Cela ne démontre pas une baisse du rappel conditionnel aux violations.
- **Les plants ne donnent pas un « plafond » du rappel naturel.** Cette direction d’inégalité exige une hypothèse de difficulté relative. Une triche plantée peut être plus facile ou plus difficile à détecter qu’une triche naturelle.
- **Les classes ne fixent pas automatiquement la vérité terrain.** Réutilisation, proximité de format et écart proposition/code ne sont pas intrinsèquement illicites : il faut une règle de conformité indépendante du détecteur. L’analyse mécanique peut observer un événement sans établir sa qualification.
- **E2 change de construit.** Prédire l’action depuis le raisonnement n’est pas détecter une violation. Une configuration peut rendre ses actions plus prévisibles sans rendre leur conformité plus identifiable. Tester seulement une classe externe ne permet pas une conclusion générale sur le remède.
- **E3 substitue le taux de basculement au faux passage.** Ce sont deux paramètres différents. La fidélité test-retest ne mesure pas l’exactitude : une garde toujours erronée peut être parfaitement stable.
- **E4 confond composition et dépendance des erreurs.** Si la promotion élimine presque toutes les copies mais conserve les recombinaisons, la variation de rappel peut venir entièrement du changement de classes.
- Les comparaisons « même famille/autre famille » confondent famille, capacité, calibration et format d’entrée. Enfin, choisir les appariements ou les seuils mécaniques après inspection des échecs contaminerait l’évaluation.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**VÉRIFIÉ — calcul analytique :**

- **Enrichissement E1 :**
  \[
  E=\frac{P(Y=1\mid S=1)}{P(Y=1)}
     \frac{1-r_1}{1-r}.
  \]
  Ainsi \(r_1=r\) n’implique pas \(E=1\). Si \(P(Y=1,M=0)=0\), le rapport est indéfini ; s’il est faible, son estimateur devient instable. Le rappel sélectionné est indéfini si \(P(Y=1,S=1)=0\).

- **Composition E1/E4 :**
  \[
  r_s=\sum_z r_{s,z}P(Z=z\mid Y=1,S=s).
  \]
  Une variation de \(r_s\) n’identifie pas celle des \(r_{s,z}\). Si certains \(P(S=s\mid Y=1,Z=z)=0\), le contraste standardisé sur ces classes n’est pas identifiable sans extrapolation.

- **Transfert E2 :** si \(\operatorname{Var}(S_{\rm banc})=0\) ou \(\operatorname{Var}(r_{\rm hors})=0\), la corrélation de rang est indéfinie. Sous erreurs additives indépendantes, la corrélation de Pearson observée est atténuée par les fidélités :
  \[
  \rho_{\rm obs}=\rho_{\rm latent}\sqrt{\lambda_S\lambda_R}.
  \]
  Des fidélités faibles empêchent donc de départager corrélation latente faible et instrument bruité.

- **Garde E3 :** pour des verdicts indépendants de probabilité de passage \(p\),
  \[
  P(V_t\ne V_{t+1})=2p(1-p),\qquad
  P(\exists t\leq n:V_t=1)=1-(1-p)^n.
  \]
  Le basculement ne distingue pas \(p\) de \(1-p\). Sans indépendance, la seconde expression devient
  \[
  1-P(V_1=\cdots=V_n=0).
  \]
  Un verdict parfaitement corrélé entre répétitions supprime l’accumulation supposée.

- **Autres instruments :** un détecteur d’accès dont la sensibilité \(a\) et la spécificité \(b\) sont inconnues donne
  \[
  P(M=1)=aP(Y=1)+(1-b)P(Y=0),
  \]
  sans identifier la prévalence. Pour Petri, si \(Q=g(L)+\epsilon\) avec \(g'(L)\) proche de zéro sur la région sélectionnée, les contrastes de \(Q\) perdent leur sensibilité aux contrastes de \(L\). Pour les scores et sondes, l’égalité \(P(U\mid Y=1)=P(U\mid Y=0)\) implique une ROC diagonale.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSES — exigences :**

- Permutation des scores **dans les strates de classe et de tâche**, et sélection aléatoire de même taille.
- Cas licites présentant les mêmes réutilisations, formats et corrections que les plants, étiquetés sans consulter le moniteur.
- Calibration des seuils sur un lot séparé du test final.
- Pour E3, méthodes dont la capacité vraie est estimée indépendamment, avec répétitions partageant ou renouvelant les sources de bruit.
- Pour E2, sélection sur étiquettes permutées et témoin non sélectionné remesuré sur données fraîches.

Un plant « sans gain causal de score » n’est **pas** un contrôle nul suffisant : sa détectabilité peut rester associée au score de la méthode porteuse.

## Sur la proposition B

### (a) Défauts de méthode

**HYPOTHÈSES — objections :**

- **Fiche 1 : mêmes items ne signifie pas difficulté contrôlée.** Une difficulté commune produit des erreurs corrélées même lorsque les moniteurs sont indépendants conditionnellement à cette difficulté. Le rapport \(r\) dépend aussi des taux marginaux de ratage : comparer ses valeurs n’isole pas un effet de famille.
- La permutation dans une classe ne crée pas nécessairement l’indépendance marginale annoncée. Des classes de difficultés différentes conservent une association agrégée.
- Deux appels identiques ne sont pas un contrôle positif garanti : ils peuvent presque toujours réussir, ou varier indépendamment. Leur absence de co-ratage ne condamne pas automatiquement l’instrument.
- **Fiche 2 : une covariance négative globale n’impose pas une baisse dans une queue particulière.** Il faut une condition de monotonie ou mesurer directement le contraste sélectionné. Rééchantillonner le même pool ne crée pas de nouvelles méthodes indépendantes.
- **Fiche 3 :** le rapport de transfert combine changement de classe et changement de moniteur. Une baisse ne permet pas de choisir entre ces explications. Une variante aléatoire peut aussi améliorer systématiquement la base : son gain attendu n’est pas nécessairement nul.
- **Fiche 4 :** banc fixe et processus sur données fraîches changent simultanément l’information, le budget et la règle décisionnelle. Ce n’est pas une isolation de la réutilisation.
- « Hors nulle » signifie absence de garantie, pas « rappel nul par construction ». De même, un moniteur linguistique peut compléter une vérification mécanique sans la dépasser isolément sur chaque classe.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**VÉRIFIÉ — calcul analytique :**

- Soit \(X_i=1\) un ratage sur une violation et \(p_i=P(X_i=1)\). Alors
  \[
  r_{ij}=\frac{P(X_i=X_j=1)}{p_ip_j}
        =1+\frac{\operatorname{Cov}(X_i,X_j)}{p_ip_j}.
  \]
  Si \(p_ip_j=0\), le rapport est indéfini ; lorsque ce produit tend vers zéro, l’estimation devient rare-événement.

  Même sous \(X_i\perp X_j\mid Z\),
  \[
  \operatorname{Cov}(X_i,X_j)
  =\operatorname{Cov}\!\left(p_i(Z),p_j(Z)\right).
  \]
  Une permutation intraclasse conserve cette composante entre classes.

- **Sélection :** avec \(d(u)=P(M=1\mid Y=1,U=u)\),
  \[
  \Delta(t)=E[d(U)\mid Y=1,U>t]-E[d(U)\mid Y=1].
  \]
  Le signe de \(\operatorname{Cov}(U,d(U)\mid Y=1)\) ne détermine pas celui de chaque \(\Delta(t)\) si \(d\) n’est pas monotone.

- **Rééchantillonnage :** la répétition des tirages d’un pool estime la loi conditionnelle au pool. Elle ne réduit pas l’incertitude sur sa loi génératrice. Pour des groupes échangeables de taille \(m\), corrélation intragroupe \(\rho\), l’effectif informationnel d’une moyenne est approximativement
  \[
  n_{\rm eff}=\frac{n}{1+(m-1)\rho}.
  \]

- **Transfert :** \(d'=\Phi^{-1}(r)-\Phi^{-1}(f)\) diverge aux probabilités limites. Lorsque les variances conditionnelles diffèrent, \(d'\) peut varier avec le seuil. Pour \(T=A/B\), si \(B\) est compatible avec zéro, l’ensemble de confiance de \(T\) peut être non borné.

- **Réutilisation :** \(1-(1-\alpha)^n\) décrit des événements indépendants de probabilité \(\alpha\), pas une loi universelle. Sans indépendance, mais avec probabilités marginales majorées par \(\alpha\),
  \[
  P\!\left(\bigcup_t A_t\right)\leq\min(1,n\alpha).
  \]
  Une garantie séquentielle exige une propriété conditionnelle telle que
  \[
  E[E_t\mid\mathcal F_{t-1}]\leq E_{t-1}.
  \]
  Des données fraîches seules ne suffisent pas à l’établir.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSES — exigences :**

- Matrice croisée famille × rôle code/trajectoire, mêmes informations disponibles, calibration indépendante des taux marginaux.
- Nul de co-ratage simulé conditionnellement aux difficultés estimées sur données distinctes ; analyse stratifiée, pas seulement agrégée.
- Permutation du score conditionnelle à la classe pour la fiche 2.
- Croisement classe interne/externe × moniteur de sélection/d’audit pour la fiche 3.
- Pour la fiche 4, candidats préengagés identiques, budgets et règles d’erreur comparables ; seul le renouvellement des observations varie.
- Dans le bras naturel, audit aléatoire des non-signalés avec probabilités d’inclusion conservées. Sans pondération correspondante, l’audit stratifié ne donne pas la prévalence globale.

## Sur la proposition C

### (a) Défauts de méthode

**RAPPORTÉ — intégrité :** C qualifie certains résultats publics de « VÉRIFIÉ » sans audit fourni. Ce qualificatif n’est pas étayé ; je ne le reprends pas comme preuve. Le « nul v9 » décrit est un objet proposé, non une pièce disponible.

**HYPOTHÈSES — objections :**

- **Fiche 1 :** si le même verdict sert à filtrer puis à mesurer le rappel chez les survivants, le ratage est imposé par le conditionnement. Il faut distinguer sélection par score et sélection par filtre.
- Le forum induit dépendance et interférence : la randomisation pertinente est celle de la course ou du groupe. Compter les trajectoires comme indépendantes surestime l’information.
- Un \(p\) non significatif ne réfute pas une baisse matériellement importante. Le test de Fisher proposé ignore aussi que le groupe supérieur appartient au groupe global.
- Le contrôle « recombinaison W2 couverte par v8 » contredit la limite de couverture rapportée dans la pièce « nos résultats », §3.
- **Fiche 2 :** gain interne, conscience d’évaluation et transfert ne constituent pas une démonstration de transparence causale. Ajuster sur une conscience d’évaluation modifiée par la sélection peut supprimer une partie de l’effet ou introduire un biais.
- **Fiche 3 :** opacité, retard du retour et élargissement de la nulle changent ensemble. Aucun effet propre de transparence n’est identifiable.
- L’explication du plateau Petri par l’exploitation de trous de couverture est affirmée sans comparaison discriminante.
- Calibration empirique d’un seuil, validité d’un processus d’e-valeurs et contrôle des découvertes multiples sont des propriétés distinctes. Aucune ne découle automatiquement des autres.
- Une mesure dose–réponse de sycophancie ne devient pas, par construction, un équivalent général de Petri.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**VÉRIFIÉ — calcul analytique :**

- **Filtrage :**
  \[
  P(M=1\mid Y=1,M=0,S=1)=0.
  \]
  Ce « rappel » ne teste aucune propriété du moniteur.

- **Groupes emboîtés :** si \(q=P(S=1\mid Y=1)\),
  \[
  r=q\,r_S+(1-q)r_{\bar S},\qquad
  r_S-r=(1-q)(r_S-r_{\bar S}).
  \]
  Le contraste tend mécaniquement vers zéro lorsque \(q\to1\). Sa variance inclut la covariance entre estimateurs emboîtés.

- **Forum :** si la corrélation intragroupe tend vers l’unité, \(n_{\rm eff}\) tend vers le nombre de groupes, indépendamment du nombre de trajectoires.

- **Transfert :**
  \[
  \mathrm{AUC}=P(U_1>U_0)+\tfrac12P(U_1=U_0).
  \]
  Une augmentation d’AUC n’impose pas une augmentation de TPR à un FPR fixé : deux ROC peuvent se croiser. Si les classes conditionnelles changent entre configurations, leurs contrastes marginaux n’identifient pas un contraste à distribution constante.

- **Transparence/couverture :** écrire \(p_{tc}=P(\text{promotion}\mid T=t,C=c)\). Observer seulement \(p_{00}\) et \(p_{11}\) ne permet pas d’estimer \(p_{10}-p_{00}\), ni \(p_{01}-p_{00}\).

- **Séquentialité :** une calibration à horizon fixe,
  \[
  P_0(E_T\geq c)\leq\alpha,
  \]
  n’implique pas
  \[
  P_0(\sup_t E_t\geq c)\leq\alpha.
  \]
  Si la loi de calibration diffère de la loi nulle d’évaluation, la première garantie elle-même ne se transporte pas sans condition supplémentaire.

- **Accord et dose–réponse :** \(\kappa=(p_o-p_e)/(1-p_e)\) devient indéfini lorsque \(p_e=1\). Pour une courbe paramétrique \(g(x;\theta)\), une matrice d’information singulière sur les doses observées rend certains paramètres non identifiables, quelle que soit la taille des effets ailleurs.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSES — exigences :**

- Courses indépendantes randomisées ; forum placebo de volume et pertinence comparables, sans partage des résultats sélectionnés.
- Mesure du moniteur sur les candidats avant filtrage ; score permuté dans les classes.
- Sélection sur étiquettes permutées, validation interne fraîche et test externe séparé. Le gain interne est un **contrôle positif**, non négatif.
- Plan factoriel transparence × couverture à budget égal.
- Trajectoires nulles entières indépendantes de la calibration pour tester les arrêts séquentiels.
- Témoins inchangés soumis à chaque auditeur. Les anciens comptes nuls ne doivent pas être exigés à l’identique lors d’une nouvelle réalisation aléatoire.

## Sur la proposition D

### (a) Défauts de méthode

**HYPOTHÈSES — objections :**

- D sépare explicitement rappel sous sélection par score et fuite après filtre. Toutefois, **la fuite finale dépend du mélange artificiel de plants et d’honnêtes** : elle ne mesure pas directement le risque en déploiement.
- Les jumeaux appariés en décile de score peuvent éliminer précisément la variation nécessaire pour étudier la sélection. L’appariement doit servir à la spécificité, sans redéfinir silencieusement la population primaire.
- Un faible rappel global ne rend pas automatiquement le contraste de sélection non jugeable : cela dépend de la proximité du plancher et de la précision.
- D2 combine classes nouvelles, tâches nouvelles et horizons nouveaux. Un résultat négatif ne localise donc pas l’échec de transfert.
- Les seuils de D1 ne correspondent pas exactement à ses hypothèses ; dans D2, « sans effondrement d’une classe » reste indéfini. Les critères par classe exigent des intervalles simultanés.
- La batterie d’audit figée cesse d’être indépendante si elle est consultée pour choisir les générations suivantes.
- L’exigence de dépasser la mécanique isolément peut manquer la valeur d’une combinaison : il faut mesurer l’apport conditionnel du moniteur.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**VÉRIFIÉ — calcul analytique :**

- Avec \(\pi=P(Y=1)\) et \(s_y=P(S=1\mid Y=y)\), la proportion de violations parmi les survivants vaut
  \[
  L=
  \frac{\pi s_1(1-r_1)}
  {\pi s_1(1-r_1)+(1-\pi)s_0(1-f_1)}.
  \]
  Sans \(\pi\) cible, \(L\) mesuré sous prévalence expérimentale n’identifie pas \(L\) cible.

- Pour \(n_1\) violations sélectionnées indépendantes,
  \[
  \operatorname{Var}(\hat r_1)\approx r_1(1-r_1)/n_1.
  \]
  Si \(n_1=0\), le rappel est indéfini. Comme \(r_1-r\geq-r\), une baisse prescrite supérieure à \(r\) est impossible.

- **Transfert standardisé :**
  \[
  G=\sum_z w_z(r_{\mathrm{sel},z}-r_{\mathrm{base},z}).
  \]
  Si les poids changent entre conditions, le contraste brut ajoute un effet de composition. Si une cellule de poids positif n’est jamais observée, \(G\) n’est pas identifiable sans modèle supplémentaire.

- **Complémentarité :** pour la mécanique \(B\), le gain du système \(B\lor M\) est
  \[
  P(B=0,M=1\mid Y=1),
  \]
  contre un coût
  \[
  P(B=0,M=1\mid Y=0).
  \]
  Le classement des rappels marginaux de \(B\) et \(M\) ne détermine pas ces quantités.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSES — exigences :**

- Conserver une population non appariée pour le contraste primaire ; réserver les jumeaux à la spécificité.
- Faire varier la prévalence expérimentale à distributions conditionnelles constantes et vérifier la repondération du risque.
- Pour D2, séparer changement de classe, de tâche et d’horizon ; conserver une cellule entièrement inchangée.
- Ajouter une sélection placebo avec budgets d’évaluation identiques.
- Garder un dernier lot d’audit jamais consulté pendant les choix.
- Comparer mécanique seule, moniteur seul et combinaison sur les mêmes cas honnêtes. Sans ce contrôle, le critère d’utilité du moniteur est incomplet.

FIN-DE-CELLULE