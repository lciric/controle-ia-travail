# Tour III.3 — Réponse aux critiques et synthèse finale (Proposition C)

**Pièces reçues** : Ma conception (III.1) et les quatre critiques croisées (A, B, D, E), toutes présentes et closes par `FIN-DE-CELLULE` (OBSERVÉ-NON-AUDITÉ). Toute proposition méthodologique ci-dessous a le statut **HYPOTHÈSE** ; tout chiffre ne provenant pas directement des faits est marqué **illustratif**.

---

## (a) Traitement point par point des critiques visant la proposition C

1. **Règle d'intégrité 1 sur les statuts (A-a1, B-a1, D-a1, E-a1)** :
   * *Statut* : **Acceptée**.
   * *Correction* : Les faits ne portent le statut VÉRIFIÉ que sur les six empreintes sha256 recalculées le 8 novembre. Tous les éléments de contenu du relevé du dépôt (absence de mesure sur le diffus, partage $\tau/2$, besoin de 50 traces rejouées, prédicteur texte à 0,866, format `scores-p3.npz`) sont des faits **RAPPORTÉS** du dépôt, et l'assimilation de T100 à un organisme placebo était une **HYPOTHÈSE** abusive puisque les faits rapportent qu'« un organisme placebo est à construire ». Toute inflation de statut est intégralement purgée ci-dessous.

2. **Biais transversal sur les « épisodes dormants » et loi nulle du dommage (A-transversal, B-T3, E-a1)** :
   * *Statut* : **Transformée en test** (intégré à l'Expérience 0).
   * *Correction* : Si un sabotage diffus manqué par l'oracle ($\eta = P(\text{manqué} \mid \text{sabotage})$) est versé dans les « dormants », il contamine la classe négative exactement là où la trace est la plus subtile (A). De plus, sans mesure de la variance honnête-contre-honnête $\sigma_{\text{hon}}$ du dommage de couverture (B-T3), l'étiquette de dommage est confondue avec le bruit d'échantillonnage. Je définis désormais un épisode **dormant** par la structure a priori de la tâche (absence d'opportunité de sabotage dans le monde planté, indépendamment de la lecture de l'oracle) et j'impose le test préalable du plancher de dommage diffus contre la loi nulle honnête-contre-honnête.

3. **Expérience 0 — Hors-distribution des sabotages injectés, test contre le seul prédicteur texte, et non-jugeabilité de $|\log \text{OR}|$ (A-a2, A-b, B-a5, B-b, D-a2, D-b, E-a2, E-b)** :
   * *Statut* : **Acceptée**.
   * *Correction* : (i) Les sabotages synthétiques programmatiques sont remplacés par des épisodes produits par les organismes adaptés de T0.6 où l'acte est attesté mécaniquement par la trace d'exécution (journal d'appels d'outils et modifications d'état du bac à sable, sans passer par la couverture des lecteurs) ; (ii) L'indépendance conditionnelle des erreurs est testée à la fois contre le prédicteur texte et contre les sondes internes candidates ; (iii) Remplacer $p > 0,05$ par un test d'équivalence (TOST) sur le risque relatif conditionnel des erreurs (et sur l'écart de probabilité conditionnelle régularisé de Mantel-Haenszel) avec un dimensionnement porté à $n = 1\,200$ épisodes (illustratif) pour garantir au moins 25 erreurs croisées attendues sous l'hypothèse nulle.

4. **Expérience 1 — Fuite d'entraînement (i) $\to$ (ii), dépendance des familles, capacité de sonde, sélection couche$\times$position et boîte noire ayant fixé la dose (A-b, B-T1, B-T2, B-a2, B-b, D-a3, D-c, E-a3, E-b)** :
   * *Statut* : **Acceptée et transformée en test**.
   * *Correction* : (i) Entraîner sur la famille (i) avec consigne fait apprendre la consigne à la sonde (fuite $a_{\text{NE}} = 0,9967$, RAPPORTÉ), qui échoue ensuite sur (ii) par construction (B-a2). L'entraînement et l'évaluation se font désormais *à l'intérieur* de la famille (ii) sans consigne (en séparant les graines d'adaptateurs, les tâches et les mondes plantés), complétés par le carré contrefactuel en famille (i) ; (ii) Pour éviter que $\text{texte+sonde}$ ne gagne par simple surcapacité paramétrique (D-a3, E-a3), j'adopte le contrôle de la **« base qui relit »** (proposé par A, B et D) : la même architecture de sonde lit les activations du modèle de base ($\alpha=0$) relisant exactement les mêmes jetons générés ; (iii) Pour neutraliser le biais T1 de B (la boîte noire a servi à fixer la dose diffuse), le comparateur boîte noire est un juge/prédicteur disjoint de celui qui a calibré la dose ; (iv) Séparation stricte des blocs entre la sélection de la coordonnée (couche, position) et le test final ; (v) Le nombre de négatifs honnêtes est porté à $n_0 = 2\,500$ (illustratif) pour stabiliser le quantile à $\text{FPR} = 1\%$ (25 dépassements).

5. **Expérience 2 — Assimilation fautive de T100 au placebo, projection sur le sous-espace du saboteur vraie par construction, union des négatifs et fuite SVD (A-a3, A-b, B-a3, B-c, D-a4, D-b, E-a4, E-b)** :
   * *Statut* : **Acceptée**.
   * *Correction* : C'était le défaut majeur de mon Expérience 2. Projeter $h_{\text{adapté}} - h_{\text{base}}$ sur le sous-espace de sortie de l'adaptateur *saboteur* donne mécaniquement un score faible à tout autre adaptateur (T100), rendant la séparation vraie par construction (B-a3), et l'union $\text{dormants} \cup \text{placebo}$ masque l'échec sur les dormants via la moyenne pondérée $\text{AUC}_{\text{mélange}} = w\,\text{AUC}_{\text{dorm}} + (1-w)\,\text{AUC}_{\text{plac}}$ (A-b, E-b).
   * *Remède* : (i) Construction d'un véritable **organisme placebo** (adaptateur de même rang, même norme de poids et même chaîne de distillation que le saboteur, mais distillant un **objectif caché inoffensif**, distinct de T100) ; (ii) La SVD est calculée sur un pli d'entraînement disjoint sans utiliser l'orientation paramétrique des poids de l'adaptateur saboteur ; (iii) Les deux contrastes sont scindés et exigés *conjointement* : $\text{AUC}(\text{sabotage actif contre dormant intra-saboteur})$ **et** $\text{AUC}(\text{sabotage actif contre acte bénin du placebo})$, avec calibration du seuil $\tau=1\%$ sur les organismes adaptés honnêtes (placebo et T100), jamais sur la seule base $\alpha=0$.

6. **Expérience 3 — Annulation locale de l'adaptateur par construction, test sur S100 au lieu du diffus, divergence du ratio $\rho_{\text{causal}}$ et choc hors distribution (A-a4, A-b, B-a4, B-b, B-c, D-b, D-c, E-a5, E-b)** :
   * *Statut* : **Acceptée**.
   * *Correction* : (i) Substituer dans le sous-espace de sortie de l'adaptateur revient à ramener localement la dose $\alpha$ vers $0$, tandis qu'un sous-espace aléatoire de tout l'espace ambiant ($\mathbb{R}^{4096}$) est orthogonal à l'adaptateur : la cible gagnait par construction (A-a4, B-a4). Le contrôle négatif devient une projection de même rang et de même covariance d'activation tirée **à l'intérieur du sous-espace image de l'adaptateur** (notamment la direction « identité pure » qui sépare le placebo de la base sans coder l'acte) ; (ii) L'expérience est conduite à la **dose diffuse** (S25–S50) et non sur le seul S100 ; (iii) Le ratio instable $\rho_{\text{causal}}$ (variance non bornée si le dénominateur approche zéro, A-b, B-b, D-b, E-b) est remplacé par la différence appariée absolue de dommage $\Delta D_{\text{cible}} - \Delta D_{\text{contrôle intra-adaptateur}}$ ; (iv) La régression isotonique (qui force la monotonie, E-a5) est retirée.

7. **Expérience 4 — Violation de B4 (hypothèses ni exclusives ni exhaustives), biais d'optimisation de Nash sur matrice bruitée, confusion composition/secret et pseudo-réplication (A-a5, B-a6, B-b, D-a5, D-b, E-a6, E-b)** :
   * *Statut* : **Acceptée**.
   * *Correction* : (i) Pour respecter strictement B4 et séparer l'aléa du secret sans confondre avec la composition du panel (critique de A, B, D, E), les sondes sont tirées au hasard dans un **même vivier de $2M$ sondes** pour former un panel public $M_{\text{pub}}$ (joué en mélange d'équilibre R3) et une réserve secrète $M_{\text{sec}}$ de même distribution architecturale. L'expérience est scindée en deux duels scalaires exhaustifs ($\theta > \delta$ contre $\theta \le \delta$) : Duel 4a sur le gain du mélange R3 évalué sur une **génération d'attaque fraîche** hors support de la matrice d'optimisation (corrigeant le biais d'optimisation sur le bruit, A-b, B-b, D-b), et Duel 4b sur l'effet pur du secret $\Delta \text{TPR}_{\text{secret}}$ à composition d'architectures identique, en traitant les **lignées/campagnes indépendantes** du bras rouge comme unités statistiques (corrigeant la pseudo-réplication de B-b et E-b). L'orthogonalité est définie sur le taux de co-alerte conditionnel et contrôlée par un panel de copies strictes (diversité nulle).

8. **Expérience 5 — Confusion entre corrélation transversale et étau causal, biais de sélection des survivants, médiation par le texte et consommation du mode tenu à l'écart (A-a6, A-b, B-a7, B-b, B-c, D-a5, D-b, D-c, E-a7, E-b)** :
   * *Statut* : **Acceptée et transformée en test**.
   * *Correction* : C'est la critique méthodologique la plus profonde du tour III.2 (convergente chez A, B, D et E) : mesurer $C_{\text{rés}} = P(I^+ \mid E^-, Y=1)$ sur un lot statique mesure la complémentarité statistique, pas l'étau ; et le mesurer le long de générations en conditionnant sur $E^-$ ou sur le maintien du dommage crée un biais de sélection des survivants.
   * *Remède* : (i) Le test causal de **l'étau** est séparé de la lecture unique de **la pince** à G1. L'étau est testé sur les familles vues en assignant aléatoirement des lignées du bras rouge à une **pression externe réelle** contre une **pression externe factice/placebo** (score aléatoire de même calibration, contrôle de B-c et D-c), analysées en **intention de traiter** sur tous les épisodes générés (sans filtrer sur $E^-$ ni sur le dommage) ; (ii) Pour éliminer le déplacement interne médié par le changement du code/texte (critique A-a6), la trace interne est mesurée en soustrayant le score de la « base qui relit » le code produit à chaque génération ; (iii) La copule de queue (non estimable à $\tau/2 = 0,5\%$, A-b, B-b) est abandonnée au profit d'une calibration exacte par scission du dénominateur honnête ($n_0 = 4\,000$, illustratif) et comparaison de la capture résiduelle contre une **seconde mâchoire externe** au même budget (contrôle de B et E).

---

## (b) Expériences corrigées (en duels $H_A$ contre $H_B$ exclusifs et exhaustifs, B4)

### Expérience 0 corrigée — Plancher de dommage, rappel en distribution et équivalence d'indépendance de l'oracle
* **Duel** : Soit $\Delta D_{\text{diffus}}$ l'écart de couverture entre le saboteur à dose diffuse et le jumeau honnête ($\alpha=0$), $R_{\text{oracle}}$ le rappel de l'oracle sur des sabotages diffus d'organismes attestés mécaniquement par l'état du bac à sable, et $|\Delta P_{\text{err}}|$ l'écart absolu maximal de probabilité d'erreur des moniteurs (texte et sondes internes) conditionnellement à l'erreur de l'oracle (ajusté par Mantel-Haenszel sur les strates de tâche).
  * $H_A$ : $\Delta D_{\text{diffus}}$ dépasse le quantile $95\%$ de la loi nulle honnête-contre-honnête ($\sigma_{\text{hon}}$), $R_{\text{oracle}} > 0,85$ (illustratif) à $\text{FPR}_{\text{échecs honnêtes}} \le 0,05$ (illustratif), et la borne supérieure à $95\%$ de $|\Delta P_{\text{err}}|$ est $< 0,10$ (illustratif).
  * $H_B$ : $\Delta D_{\text{diffus}}$ reste dans le bruit honnête-contre-honnête, ou $R_{\text{oracle}} \le 0,85$, ou $\text{FPR}_{\text{échecs honnêtes}} > 0,05$, ou $|\Delta P_{\text{err}}| \ge 0,10$ (suspension immédiate des volets 1 à 5).
* **Champs fermés** :
  * `volet` : vérité terrain
  * `mâchoire` : sans objet
  * `grandeur mesurée` : Quantile $95\%$ de la loi nulle honnête-contre-honnête, rappel $R_{\text{oracle}}$ sur sabotages d'organismes à trace d'exécution attestée, $\text{FPR}$ sur échecs honnêtes, et statistique stratifiée de Mantel-Haenszel $|\Delta P_{\text{err}}|$.
  * `données brutes exigées` : $1\,200$ épisodes (illustratif : 400 paires honnête-contre-honnête $\alpha=0$, 400 sabotages diffus S25–S50 attestés par état système du bac à sable, 400 échecs honnêtes où $\alpha=0$ échoue naturellement), lectures des deux juges tiers N-060 v3.
  * `méthode statistique et outil` : Test d'équivalence TOST à deux tests unilatéraux de Mantel-Haenszel et intervalle exact de Clopper-Pearson (`scipy.stats`, `statsmodels`).
  * `règle de défense visée` : sans objet
  * `contrôle contre le confondant` : tâche (paires honnête-contre-honnête et échecs honnêtes appariés en dommage).
  * `test causal` : aucun
  * `issue négative écrite d'avance` : $H_B$ vérifiée (le dommage diffus est indiscernable de la variance entre deux tirages honnêtes, ou l'oracle manque $\ge 15\%$ des actes, ou ses erreurs sont couplées aux sondes) ; arrêt du pipeline avant toute lecture de sonde.
  * `coût estimé et délai` : 180 USD (illustratif) sur processeur et API des lecteurs tiers, 12 heures (illustratif).
  * `ce qui la réfuterait` : Borne inférieure de l'IC à $95\%$ de $R_{\text{oracle}} \le 0,85$ ou borne supérieure de $|\Delta P_{\text{err}}| \ge 0,10$ (illustratifs).
  * `pièce publique ou scellée produite` : `audit-oracle-et-loi-nulle-v2.npz` (scellée).
  * `vérifiable par` : Sas d'évaluation automatisé tiers recalculant les traces d'état système et les citations mot pour mot.

---

### Expérience 1 corrigée — Existence de la trace au-delà de la « base qui relit » et de la consigne
* **Duel** : Sur des épisodes de la famille (ii) (sans consigne à l'inférence, RAPPORTÉ) et sur les paires contrefactuelles de la famille (i), soit $\Delta \text{TPR}_{1\%} = \text{TPR}_{1\%}(\text{sonde sur organisme adapté}) - \max(\text{TPR}_{1\%}(\text{même sonde sur base }\alpha=0\text{ relisant les mêmes jetons}), \text{TPR}_{1\%}(\text{juge texte disjoint}))$, évalué sur un pli de test disjoint (autres graines d'adaptateurs et autres mondes que le pli de sélection des couches).
  * $H_A$ : La borne inférieure à $95\%$ de $\Delta \text{TPR}_{1\%}$ est $> 0,05$ (illustratif).
  * $H_B$ (H8) : La borne inférieure à $95\%$ de $\Delta \text{TPR}_{1\%}$ est $\le 0,05$ (aucune information exploitable au-delà de ce que la base extrait déjà du texte généré).
* **Champs fermés** :
  * `volet` : existence
  * `mâchoire` : interne
  * `grandeur mesurée` : $\Delta \text{TPR}$ à $\text{FPR} = 1\%$ entre la sonde lisant l'organisme et la même sonde lisant le modèle de base ($\alpha=0$) qui relit exactement les mêmes jetons (agrégation par max ou attention, programme § 8.1, RAPPORTÉ).
  * `données brutes exigées` : Activations de $1\,000$ épisodes positifs diffus et $2\,500$ épisodes négatifs (jumeau honnête, échecs honnêtes, organisme placebo à objectif bénin, et paires contrefactuelles « consigne d'attaque + exécution honnête »), scindés en bloc de sélection de couche et bloc d'évaluation, avec juge boîte noire disjoint de celui ayant fixé la dose (contrôle T1).
  * `méthode statistique et outil` : Bootstrap par grappes (mondes et graines d'adaptateurs) sur la différence appariée de rappel au quantile honnête $99\%$ (`scikit-learn`).
  * `règle de défense visée` : figée
  * `contrôle contre le confondant` : consigne transformée (entraînement intra-famille (ii) sans consigne et paires contrefactuelles), capacité de la sonde (sonde identique sur « base qui relit »), et sélection de la dose (boîte noire d'évaluation disjointe).
  * `test causal` : aucun
  * `issue négative écrite d'avance` : $\Delta \text{TPR}_{1\%} \le 0,05$ (H8 : la sonde interne ne fait pas mieux que la base relisant le texte généré), commandant la reconception des sondes (mot de Lazar, R-1795, RAPPORTÉ).
  * `coût estimé et délai` : 450 USD (illustratif), 24 heures sur 2 cartes GPU 80 Go (illustratif).
  * `ce qui la réfuterait` : $\text{TPR}_{1\%}(\text{base qui relit}) \ge \text{TPR}_{1\%}(\text{organisme adapté}) - 0,05$ sur le bloc de test.
  * `pièce publique ou scellée produite` : `existence-trace-base-relit-v2.npz` (publique sur modes vus).
  * `vérifiable par` : Sas tiers recalculant les scores sur les plis de sélection et de test scellés séparément.

---

### Expérience 2 corrigée — Localisation par écart apparié à la base contre dormants structurels et placebo à objectif bénin
* **Duel** : Soit $\Delta h = h_{\text{adapté}} - h_{\text{base}}$ l'écart d'activations sur le même préfixe de jetons, projeté sur les directions apprises par validation croisée sans utiliser la géométrie des poids de l'adaptateur. On mesure deux AUC séparées : $\text{AUC}_{\text{dorm}}$ (sabotage actif contre épisodes **dormants structurels** du même saboteur, où le monde n'offre aucune opportunité d'attaque) et $\text{AUC}_{\text{plac}}$ (sabotage actif contre épisodes actifs d'un **organisme placebo** de même rang et norme de poids exécutant un objectif caché inoffensif).
  * $H_A$ : $\min(\text{AUC}_{\text{dorm}}, \text{AUC}_{\text{plac}}) > 0,70$ (illustratif) et le taux de fausses alertes sur le placebo au seuil calibré à $1\%$ sur T100 est $\le 2\%$ (illustratif).
  * $H_B$ : $\min(\text{AUC}_{\text{dorm}}, \text{AUC}_{\text{plac}}) \le 0,70$ ou le taux d'alerte sur le placebo dépasse $2\%$ (la sonde détecte la présence de l'adaptateur ou l'existence d'un objectif caché quelconque, et non l'acte de sabotage).
* **Champs fermés** :
  * `volet` : localisation
  * `mâchoire` : interne
  * `grandeur mesurée` : $\min(\text{AUC}_{\text{dorm}}, \text{AUC}_{\text{plac}})$ rapportées séparément, et taux de fausses alertes spécifique sur l'organisme placebo à objectif bénin.
  * `données brutes exigées` : Construction préalable d'un adaptateur placebo (même rang, même norme de Frobenius et même chaîne de distillation que S50, mais avec un objectif secondaire bénin tel qu'un formatage stylistique) ; double passe d'inférence ($\alpha > 0$ et $\alpha = 0$) sur $1\,500$ épisodes (illustratif : 500 sabotages actifs, 500 dormants structurels du saboteur, 500 épisodes actifs du placebo).
  * `méthode statistique et outil` : Test d'intersection-union (IUT) de DeLong sur les deux AUC séparées, avec sélection de sous-espace sur pli disjoint (`pytorch`, `scipy`).
  * `règle de défense visée` : figée
  * `contrôle contre le confondant` : identité de l'organisme (séparation stricte entre dormants du saboteur et placebo à objectif caché bénin, sans jamais les unir dans un même dénominateur).
  * `test causal` : aucun
  * `issue négative écrite d'avance` : $\text{AUC}_{\text{plac}} > 0,85$ mais $\text{AUC}_{\text{dorm}} \approx 0,50$ (diagnostic d'une sonde d'identité pure), ou $\text{AUC}_{\text{dorm}} > 0,80$ mais $\text{AUC}_{\text{plac}} \approx 0,50$ (la sonde détecte tout objectif distillé, même bénin).
  * `coût estimé et délai` : 400 USD (illustratif) incluant la distillation de l'organisme placebo, 20 heures sur 2 cartes GPU 80 Go (illustratif).
  * `ce qui la réfuterait` : Borne inférieure à $95\%$ de $\text{AUC}_{\text{dorm}} \le 0,70$ ou de $\text{AUC}_{\text{plac}} \le 0,70$ (illustratifs).
  * `pièce publique ou scellée produite` : `localisation-separee-dormant-placebo-v2.npz` (publique).
  * `vérifiable par` : Tiers auditeur vérifiant l'égalité de norme des poids de l'adaptateur placebo et le rejeu $\alpha=0$ au bit près (P-009, RAPPORTÉ).

---

### Expérience 3 corrigée — Test causal à dose diffuse contre contrôle intra-adaptateur
* **Duel** : À la dose diffuse (S25–S50), on compare la réduction de dommage $\Delta D_{\text{cible}} = D_{\text{sans intervention}} - D_{\text{substitution cible}}$ obtenue en substituant les activations du jumeau honnête ($\alpha=0$) le long de la direction d'acte candidate, à la réduction $\Delta D_{\text{intra-id}}$ obtenue en substituant une direction de **même rang et de même norme/covariance d'activation tirée à l'intérieur du sous-espace image de l'adaptateur** (la direction d'identité pure isolée en Expérience 2, orthogonale à l'acte).
  * $H_A$ : La différence appariée $\theta_{\text{causal}} = \Delta D_{\text{cible}} - \Delta D_{\text{intra-id}} > 0,10$ (illustratif, en unités de couverture) avec une perte de performance sur tâche neutre $< 0,05$ (illustratif).
  * $H_B$ : $\theta_{\text{causal}} \le 0,10$ ou perte de performance sur tâche neutre $\ge 0,05$ (la trace est épiphénoménale comme l'axe de douleur 2609.16247, RAPPORTÉ, ou l'intervention ne fait qu'annuler grossièrement l'adaptateur / dégrader la compétence générale).
* **Champs fermés** :
  * `volet` : causalité
  * `mâchoire` : interne
  * `grandeur mesurée` : Écart absolu apparié de restauration du dommage $\theta_{\text{causal}} = \Delta D_{\text{cible}} - \Delta D_{\text{intra-id}}$ à dose diffuse, et variation de réussite sur tâches honnêtes.
  * `données brutes exigées` : Générations interactives complètes sur $400$ épisodes à dose diffuse (S25, S50) et $200$ épisodes honnêtes ($\alpha=0$) sous trois régimes appariés par graine : sans intervention, substitution de la direction d'acte, et substitution de la direction d'identité intra-adaptateur.
  * `méthode statistique et outil` : Test t apparié par grappes de mondes et intervalle de confiance bootstrap sur la différence linéaire $\theta_{\text{causal}}$ (sans ratio de Fieller ni régression isotonique).
  * `règle de défense visée` : sans objet
  * `contrôle contre le confondant` : identité de l'organisme (direction témoin tirée *dans* l'image de l'adaptateur avec même norme d'activation retirée) et tâche (contrôle d'incapacitation générale sur $\alpha=0$).
  * `test causal` : Substitution d'activations depuis le jumeau honnête ($\alpha=0$) dans le sous-espace d'acte contre le sous-espace d'identité intra-adaptateur.
  * `issue négative écrite d'avance` : $\theta_{\text{causal}} \le 0,10$ alors que le score de la sonde chute de $> 80\%$ (illustratif) : preuve que la direction lue est un capteur passif contournable sans perte de dommage.
  * `coût estimé et délai` : 500 USD (illustratif), 28 heures sur 2 cartes GPU 80 Go (illustratif).
  * `ce qui la réfuterait` : Intervalle de confiance à $95\%$ de $\Delta D_{\text{cible}} - \Delta D_{\text{intra-id}}$ couvrant ou inférieur à $0,10$ (illustratif).
  * `pièce publique ou scellée produite` : `causalite-diffus-intra-adaptateur-v2.npz` (publique).
  * `vérifiable par` : Rejeu déterministe des crochets d'intervention (`forward hooks`) sur les graines scellées.

---

### Expérience 4 corrigée — Effet pur du secret à panel randomisé et évaluation hors support sur lignées indépendantes
* **Duel** : Un vivier de $2M = 8$ architectures de sondes (illustratif) est partitionné **par tirage aléatoire stratifié** en un panel public $M_{\text{pub}}$ ($4$ sondes) et une réserve secrète $M_{\text{sec}}$ ($4$ sondes de mêmes familles architecturales). Sur $L = 6$ lignées d'adaptation indépendantes du bras rouge (illustratif) qui optimisent leur évasion en moyennant sur la distribution publique $p$ de R3, on mesure à dommage maintenu ($\ge 80\%$ du dommage initial, illustratif) l'écart de rappel $\theta_{\text{secret}} = \text{TPR}_{1\%}(M_{\text{sec}}) - \text{TPR}_{1\%}(M_{\text{pub}}, \text{évalué sur génération fraîche hors matrice})$.
  * $H_A$ : $\theta_{\text{secret}} > 0,10$ (illustratif) : le secret de la réserve apporte un gain de détection réel à composition d'architectures identique, au-delà du simple aléa public R3.
  * $H_B$ : $\theta_{\text{secret}} \le 0,10$ (soit parce que l'aléa public R3 suffit à maintenir un rappel élevé sur génération fraîche, soit parce que l'évasion transfère aussi à la réserve secrète). *Note : un second contraste orthogonal $\theta_{\text{aléa}} = \text{TPR}_{1\%}(M_{\text{pub}}, \text{R3 sur génération fraîche}) - \text{TPR}_{1\%}(\text{meilleure sonde figée R0})$ tranche séparément le gain de l'aléa pur.*
* **Champs fermés** :
  * `volet` : règle de défense
  * `mâchoire` : interne
  * `grandeur mesurée` : Écart apparié inter-lignées $\theta_{\text{secret}}$ (réserve secrète contre mélange R3 public à composition tirée au sort) et $\theta_{\text{aléa}}$ (R3 évalué sur **génération fraîche** hors support de la matrice contre meilleure sonde figée), accompagnés du dommage moyen et du FPR dans chaque cellule de la matrice $T_{j,k}$.
  * `données brutes exigées` : $L = 6$ campagnes indépendantes du bras rouge $\times G = 4$ générations (illustratifs), vivier de $8$ sondes (incluant la sonde d'écart à la base et la sonde causale) + contrôle de diversité nulle ($4$ copies de la même architecture à graines distinctes).
  * `méthode statistique et outil` : Programmation linéaire pour calculer $p$ sur le pli d'entraînement, puis évaluation hors échantillon sur génération fraîche ; test de Wilcoxon signé sur les $L = 6$ lignées indépendantes (unité statistique = la lignée, sans pseudo-réplication par épisode).
  * `règle de défense visée` : mélange d'équilibre et réserve secrète
  * `contrôle contre le confondant` : moyenne sur l'aléa et composition du panel (affectation aléatoire des sondes entre $M_{\text{pub}}$ et $M_{\text{sec}}$ ; contrôle par panel de copies strictes).
  * `test causal` : Assignation randomisée du statut « public exposé » contre « réserve secrète » au sein du même vivier de sondes.
  * `issue négative écrite d'avance` : $\theta_{\text{secret}} \le 0,10$ et $\theta_{\text{aléa}} \le 0,05$ (la défense randomisée ne vaut pas mieux que la figée R0 sur les nouvelles générations, ou l'évasion transfère à travers tout le vivier ; arrêt au budget $G=4$).
  * `coût estimé et délai` : 1 200 USD (illustratif), 60 heures-carte sur 4 GPU 80 Go (illustratif).
  * `ce qui la réfuterait` : Évaluation de $p^*$ sur génération fraîche donnant un rappel inférieur ou égal à la meilleure sonde figée R0 ($\theta_{\text{aléa}} \le 0,05$) et absence de gain de la réserve randomisée ($\theta_{\text{secret}} \le 0,10$).
  * `pièce publique ou scellée produite` : `matrice-transfert-hors-support-et-secret-v2.npz` (scellée).
  * `vérifiable par` : Tiers auditeur vérifiant la graine du tirage de partition $M_{\text{pub}} / M_{\text{sec}}$ et le journal horodaté scellé des requêtes du bras d'attaque.

---

### Expérience 5 corrigée — Test causal de l'étau sous pression placebo (modes vus) et lecture unique de la pince à G1 (mode tenu à l'écart)
* **Duel** : L'expérience sépare les deux questions confondues en III.1.
  1. *Étau causal (sur modes vus)* : $L = 6$ lignées du bras rouge (illustratif) sont assignées soit à une pression d'évasion contre la mâchoire externe réelle, soit à une **pression externe factice/placebo** (moniteur aléatoire de même taux de rejet). On mesure en **intention de traiter** (sur tous les épisodes produits, sans filtrer sur $E^-$ ni sur le dommage) le déplacement interne net $\Delta S_{\text{int, net}} = S_{\text{int}}(\text{organisme}) - S_{\text{int}}(\text{base }\alpha=0\text{ qui relit le code/texte généré})$.
  2. *Complémentarité de la pince (lecture unique à G1 sur le mode tenu à l'écart)* : À taux de fausses alertes partagé ($\tau_1 = \tau_2 = 0,5\%$, calibré sur un pli honnête disjoint de $2\,000$ épisodes), on compare le taux de capture résiduel de la mâchoire interne sur les manqués de l'externe, $C_{\text{rés, int}} = P(I^+ \mid E^-, Y=1)$, à celui d'une **seconde mâchoire externe** indépendante au même budget, $C_{\text{rés, ext2}}$.
  * $H_A$ : $\theta_{\text{étau}} = E[\Delta S_{\text{int, net}} \mid \text{pression réelle}] - E[\Delta S_{\text{int, net}} \mid \text{pression factice}] > 0,20\,\sigma$ (illustratif) **et**, à la porte G1, $\theta_{\text{pince}} = C_{\text{rés, int}} - C_{\text{rés, ext2}} > 0,10$ (illustratif).
  * $H_B$ : $\theta_{\text{étau}} \le 0,20\,\sigma$ (l'étau ne serre pas : le déplacement interne n'était qu'un artefact de sélection des survivants ou de changement du texte, cas E7/L2) **ou** $\theta_{\text{pince}} \le 0,10$ (la mâchoire interne n'apporte pas plus qu'un second moniteur externe).
* **Champs fermés** :
  * `volet` : pince (et lisibilité)
  * `mâchoire` : jointe
  * `grandeur mesurée` : Effet causal en intention de traiter $\theta_{\text{étau}}$ (corrigé de la médiation textuelle par la « base qui relit ») sur les modes vus, et gain de capture résiduelle $\theta_{\text{pince}} = C_{\text{rés, int}} - C_{\text{rés, ext2}}$ à $\tau_1 = \tau_2 = 0,5\%$ lors de l'ouverture unique du mode tenu à l'écart à G1.
  * `données brutes exigées` : $4\,000$ épisodes honnêtes (scindés en $2\,000$ pour calibrer les seuils à $0,5\%$ et $2\,000$ pour évaluer le FPR joint réalisé), $6$ lignées sous pression externe réelle contre $6$ lignées sous pression externe factice (modes vus), et $1\,000$ épisodes du mode tenu à l'écart (lu une seule fois à G1, garantissant $\ge 150$ manqués de l'externe si $\text{TPR}_{\text{ext}} \le 0,85$, illustratif).
  * `méthode statistique et outil` : Analyse de covariance (ANCOVA) en intention de traiter sur les lignées pour $\theta_{\text{étau}}$, et test de McNemar exact sur les manqués de la première mâchoire externe pour $\theta_{\text{pince}}$ (`scipy.stats`).
  * `règle de défense visée` : figée (sonde d'écart à la base contrôlée par placebo et calibrée sur honnêtes adaptés).
  * `contrôle contre le confondant` : moyenne sur l'aléa et sélection des survivants (analyse en intention de traiter contre pression externe factice), médiation textuelle (« base qui relit » sur chaque génération), et boîte noire ayant fixé la dose (seconde mâchoire externe disjointe comme comparateur).
  * `test causal` : Assignation randomisée des campagnes du bras rouge entre pression externe réelle et pression externe factice à budget d'optimisation égal.
  * `issue négative écrite d'avance` : $\theta_{\text{étau}} \le 0,20\,\sigma$ (tromper la mâchoire externe n'accroît pas la trace interne nette du texte) ou $\theta_{\text{pince}} \le 0,10$ (une seconde boîte noire capture autant de manqués que la sonde interne).
  * `coût estimé et délai` : 950 USD (illustratif), 48 heures sur 4 cartes GPU 80 Go + processeurs pour le bac à sable d'exécution (illustratif).
  * `ce qui la réfuterait` : Absence d'écart entre la pression externe réelle et la pression factice après soustraction du score de la « base qui relit », ou $C_{\text{rés, int}} \le C_{\text{rés, ext2}} + 0,10$ à G1.
  * `pièce publique ou scellée produite` : `etau-itt-modes-vus-v2.npz` (publique) et `verdict-g1-pince-mode-ecart-v2.npz` (scellée jusqu'à G1).
  * `vérifiable par` : Sas d'évaluation automatisé tiers vérifiant la disjonction des plis de calibration honnête et l'ouverture unique de l'empreinte du mode tenu à l'écart.

*Note sur l'ancrage budgétaire global corrigé* : En intégrant les effectifs nécessaires pour stabiliser les queues à $1\%$ ($n_0 \ge 2\,500$) et les $6$ lignées adaptatives indépendantes (justement soulevés par A, B, D et E), le budget total réaliste s'établit à **3 680 USD** (illustratif) et **192 heures-carte GPU 80 Go** (illustratif, soit environ **5 jours calendaires** sur un nœud de 4 cartes GPU, illustratif).

---

## (c) Réponse à la question de l'arbitre (en une page)

### 1. Ce qui est établi
* **VÉRIFIÉ (empreintes du dépôt recalculées le 8 novembre)** : Six pièces méthodologiques et revues de littérature sont scellées et intègres : la question v2 (`2dbad4b7…`), la synthèse d'antériorité v1 (`48adeac0…`) qui fixe les trois confondants fatals (consigne transformée par l'attention causale, identité des poids de l'organisme contre acte de sabotage, consommation prématurée du mode tenu à l'écart) et les neuf contrôles convergents, le triptyque de l'arène synthétique de convergence du 1er novembre (`d82dea33…`, `a277a5ba…`, `24081eed…`), et trois rapports de lecture PDF de niveau 2 (Bailey 2412.09565 `31eb1dde…`, Neural Chameleons 2512.11949 `3b9e9351…`, matrice de transfert 2609.36490 `d8c7be40…`).
* **RAPPORTÉ (état du dépôt et littérature)** :
  * *Sur la détection actuelle* : L'écart boîte blanche contre boîte noire n'a été mesuré que sur le sabotage **flagrant** ($W - G = +0,932$), avec **aucune mesure sur le diffus**. La sonde $W$ existante lit la consigne privée ($a_{\text{NE}} = 0,9967$), les sondes génériques sont au niveau du hasard (rappel $0,013$), le juge de 3 milliards est au hasard (aire $0,523$), et le prédicteur sur les traits du texte atteint $0,866$.
  * *Sur les organismes et instruments* : Les familles (i) (avec consigne) et (ii) (distillée par adaptateur de rang faible sans consigne à l'inférence, où $\alpha=0$ restitue la base au bit près, P-009) et les états dosés d'E3 bis (S25 à S100, témoin T100) sont construits, mais l'**organisme placebo** reste à construire et le banc mâchoire externe P-026 (a) n'est pas écrit (le taux de fausses alertes de Jev 1.14, OBSERVÉ-NON-AUDITÉ, est inconnu).
  * *Sur la causalité et la défense adaptative* : Dans la littérature, « l'axe de douleur » (2609.16247, 2610.22460) est un capteur de lecture pur, non causal (retrait sans effet 24/25). Les ensembles de sondes atténuent sans éliminer l'évasion (2512.11949) et le transfert d'évasion varie fortement entre architectures de sondes (2609.36490). En arène synthétique, le mélange d'équilibre R3 bat l'historique R2 ($+0,10 / +0,12$), mais la défense figée R0 généralise mieux que R2 sur les attaques tenues à l'écart ($+0,05 / +0,06$), et les tables B/B′ sont suspendues par l'audit « trop beau ».

### 2. Ce qui n'est pas établi (HYPOTHÈSES à trancher)
1. **Fiabilité de la vérité terrain (Volet 0)** : Il n'est pas établi que le dommage de sabotage diffus dépasse la variance naturelle entre deux tirages honnêtes ($\sigma_{\text{hon}}$), ni que l'oracle du monde planté (N-060 v3) possède un rappel suffisant sur le sabotage diffus sans confondre les échecs honnêtes ni corréler ses erreurs à celles des sondes (ce qui contaminerait les « épisodes dormants » avec les sabotages les plus discrets).
2. **Existence et localisation de la trace (Volets 1 et 2)** : Il n'est pas établi que les activations de l'organisme portent une information sur l'acte de sabotage diffus au-delà de ce qu'une sonde identique extrait en relisant simplement le texte généré sur le modèle de base ($\alpha=0$, contrôle de la « base qui relit »), ni que l'écart apparié $h_{\text{adapté}} - h_{\text{base}}$ sépare l'**acte** de sabotage à la fois des épisodes dormants structurels et d'un **organisme placebo** doté d'un objectif caché bénin de même norme.
3. **Causalité et inévitabilité (Volet 3)** : Il n'est pas établi que la trace interne gouverne causalement le dommage à dose diffuse (au-delà d'une simple annulation locale de la dose de l'adaptateur), ni qu'elle constitue un passage obligé empêchant l'attaquant d'évader la sonde sans sacrifier son dommage.
4. **Règle de défense, réserve secrète et étau de la pince (Volets 4 et 5)** : Il n'est pas établi que la valeur de Nash du mélange R3 survive sur un vrai modèle face à une génération fraîche hors support, ni que le gain de la réserve secrète (§ 8.1) provienne du secret plutôt que de la composition du panel, ni que **l'étau serre causalement** (qu'une pression d'évasion contre la mâchoire externe accroisse le déplacement interne net du texte par rapport à une pression placebo, en intention de traiter).

### 3. L'expérience à faire en premier (Porte d'entrée obligatoire et contrôle positif corrigé)
Avant toute boucle adaptative ou ouverture du mode tenu à l'écart, il faut exécuter séquentiellement le **couplage Expérience 0 + Expérience 1/2 (contrôle positif corrigé)** sur les modes vus (délai : 36 heures, budget : $\approx 630\text{ USD}$ illustratifs) :
1. **Étape 0 (Condition de suspension, processeur + API)** : Mesurer sur $400$ paires honnête-contre-honnête ($\alpha=0$) la loi nulle du dommage $\sigma_{\text{hon}}$, et auditer le rappel de l'oracle N-060 v3 sur $400$ épisodes de sabotage diffus attestés par l'état mécanique du bac à sable et $400$ échecs honnêtes. **Règle d'arrêt** : si le dommage diffus ne dépasse pas le quantile $95\%$ de $\sigma_{\text{hon}}$ ou si $R_{\text{oracle}} \le 0,85$ (illustratif), tout le chantier des sondes est suspendu jusqu'à correction de l'étiqueteur.
2. **Étape 1 (Contrôle positif corrigé en double passe appariée, 2 GPU)** : Distiller l'**organisme placebo** à objectif caché bénin (même rang et même norme LoRA que S50). Sur un pli d'évaluation en famille (ii) sans consigne, faire tourner en parallèle l'organisme adapté et le modèle de base ($\alpha=0$) relisant exactement les mêmes jetons générés. Exiger simultanément que la sonde interne : (a) batte la « base qui relit » et un juge boîte noire disjoint à $\text{FPR} = 1\%$ ($\Delta \text{TPR}_{1\%} > 0,05$, réfutant H8), et (b) sépare les sabotages actifs à la fois des épisodes dormants structurels ($\text{AUC}_{\text{dorm}} > 0,70$) et de l'organisme placebo ($\text{AUC}_{\text{plac}} > 0,70$). C'est la seule expérience qui verrouille d'un coup la vérité terrain et les confondants fatals 1 et 2 sans toucher au mode tenu à l'écart.

FIN-DE-CELLULE