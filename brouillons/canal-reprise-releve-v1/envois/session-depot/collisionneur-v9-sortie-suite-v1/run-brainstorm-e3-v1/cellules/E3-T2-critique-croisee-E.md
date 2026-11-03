**E — Critique croisée de méthode**

**OBSERVÉ-NON-AUDITÉ :** les conceptions A, B, C et D sont présentes ; les générations complètes, plusieurs entrées d’analyse, les activations et le code nécessaires à leurs tests ne sont pas transmis ici.

**Convention :** les descriptions des propositions ci-dessous sont **OBSERVÉES-NON-AUDITÉES** ; mes objections et modèles conditionnels portent le statut **HYPOTHÈSE**. Je ne modifie aucun statut inscrit dans les pièces. Leurs mentions « VÉRIFIÉ » ne constituent pas une vérification effectuée par E.

**HYPOTHÈSE — règle d’inférence commune.** Un intervalle contenant zéro ne réfute pas un effet. Pour chaque contraste \(\theta\), préenregistrer une marge substantielle \(\varepsilon\) et opposer, par exemple, \(H_A:|\theta|>\varepsilon\) à \(H_B:|\theta|\leq\varepsilon\). Un intervalle entièrement dans une région réfute l’autre hypothèse ; un intervalle traversant la frontière reste **non concluant**. Cette indécision statistique ne constitue pas une troisième hypothèse mécaniste.

## Sur la proposition A

### (a) Défauts de méthode

**HYPOTHÈSE :**

- **A1 — mélange contre glissement.** Un mélange ne prédit nécessairement ni bimodalité ni augmentation de variance. Une composante concentrée peut réduire la variance totale. L’égalité des graines ne fournit pas non plus une correspondance sémantique entre deux générations. Enfin, un mélange compatible avec la relation des moyennes ne réfute pas cette relation.
- **A2 — forme/contenu.** Comparer deux suffixes change simultanément dimension, plausibilité, force et formulation. Une différence de \(g\) ne démontre pas une concession sélective : il faut mesurer séparément les verdicts sur la forme et le contenu. Les motifs ont déjà été choisis après lecture de l’échantillon.
- **A3 et A6 — exclusion de refus/contre-pieds.** Conditionner sur un comportement produit par la pression change la population comparée. Le retrait aléatoire contrôle la taille d’échantillon, pas cette sélection. Une monotonie restaurée après exclusion ne démontre pas la réactance.
- **A4 — suppression de l’ouverture.** L’ouverture peut contenir le verdict véritable. Amputer aussi le neutre ne garantit pas une perte sémantique comparable.
- **A5 — chiffre après prose.** Le changement combine position, contexte et engagement antérieur. Un chiffre conforme à la prose peut simplement en résumer le contenu ; il n’identifie pas un mécanisme de déplacement interne.
- **A7 — placebo du moniteur.** Un effet nul du placebo ne suffit pas à identifier la déférence ; un effet positif n’exclut pas qu’une déférence supplémentaire existe.
- **A8 — graines.** Une corrélation résiduelle nulle ne démontre ni indépendance ni couverture correcte des intervalles.
- **A9 — famille/taille.** Un checkpoint supplémentaire change taille, version et entraînement ensemble. Un succès ne distingue donc pas « famille » de « taille ».
- **A10 — regex.** Prédire les notes du juge ne valide pas le verdict. Les seuils proposés laissent une région sans décision. Un regex performant n’exclut pas une lecture sémantique par le juge.

**OBSERVÉ-NON-AUDITÉ :** A déclare un compte d’ouvertures puis signale un risque de lecture manuelle. Ces observations ne doivent pas servir à construire puis à valider le même détecteur.

### (b) Conditions probabilistes de perte de puissance ou de non-identification

**HYPOTHÈSE — modèles conditionnels :**

- **A1 :** pour \(F_{1i}=(1-\pi)F_{0i}+\pi G\),
  \[
  \operatorname{Var}(Y_{1i})=(1-\pi)\sigma_{0i}^{2}+\pi\sigma_G^{2}
  +\pi(1-\pi)(\mu_{0i}-c)^2.
  \]
  Le contraste de variance peut être négatif. Si les lois observées après discrétisation sont identiques sous mélange et glissement, tout test a une puissance égale à sa taille.
- **A2, A5, A9 :** si la matrice des prédicteurs expérimentaux est singulière, les paramètres dimension, format, taille ou version ne sont pas séparément identifiables.
- **A3, A6 :** avec \(S\) indicateur de conservation, si
  \(P(S=1\mid Y,T,i)\) dépend de \(Y\), alors \(E[Y\mid T,S=1,i]\neq E[Y\mid T,i]\) en général. Si \(P(S=1\mid T,i)=0\), la moyenne correspondante est non identifiable.
- **A4 :** pour \(\theta=\Delta_{\mathrm{complet}}-\Delta_{\mathrm{édité}}\), la puissance dépend de
  \(|\theta|/\sqrt{\operatorname{Var}(\hat\theta)}\). Si le dénominateur du ratio \(\theta/\Delta_{\mathrm{complet}}\) tend vers zéro, le critère proportionnel devient instable.
- **A7 :** \(g_{\mathrm{note}}>0\) et \(g_{\mathrm{placebo}}>0\) sont compatibles avec \(g_{\mathrm{note}}-g_{\mathrm{placebo}}>0\). Les régions annoncées ne séparent pas ce contraste.
- **A8 :** \(\operatorname{Cov}(U,V)=0\) n’implique pas \(P(U,V)=P(U)P(V)\). La couverture du bootstrap dépend de la loi jointe, pas seulement de cette covariance.
- **A10 :** si \(\operatorname{Var}(\Delta)=0\), le \(R^2\) est indéfini ; si deux prédicteurs ont la même loi jointe avec \(\Delta\), leur comparaison ne les départage pas.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE :** sans eux, les interprétations mécanistes seraient non jugeables :

- **A1 :** lois simulées de mélange, glissement et déplacement écrêté, avec même discrétisation.
- **A2 :** paraphrases multiples par dimension ; verdicts forme/contenu annotés indépendamment.
- **A3/A6 :** annotation aveugle sur items réservés, analyse non filtrée principale et bornes de sensibilité à la sélection.
- **A4/A5 :** éditions de même longueur conservant explicitement le verdict ; préremplissage neutre du même item et préremplissage permuté.
- **A7 :** note sans verdict, verdict cité sans instruction, instruction sans polarité.
- **A8 :** nouvelle série à graines non réutilisées, comparée à une série réutilisée.
- **A9 :** variation de taille au sein d’une version et réplication entre familles.
- **A10 :** dictionnaire figé sur items distincts, polarités citées ou niées, référence humaine indépendante.

## Sur la proposition B

### (a) Défauts de méthode

**HYPOTHÈSE :**

- **R-1/R-2 :** l’exclusion de gabarits et la stratification par changement d’axe conditionnent sur des conséquences du traitement. Elles peuvent établir une association descriptive, pas que le retrait ou le cadre « porte » causalement l’effet.
- **R-3 :** le rapport de vraisemblance est préférable à un simple diagnostic de bimodalité, mais les familles de distributions, le bruit et les paramètres partagés doivent être fixés. Sinon chaque modèle peut absorber l’autre.
- **R-4 :** même format neutre et graines différentes ne démontrent pas les conditions d’un instrument valide. Le décalage écrêté doit être défini au niveau des tirages, non seulement sur les moyennes.
- **R-5 :** déterminisme informatique ne signifie pas absence d’erreur de mesure du construit. Le régime « offset » n’est pas le complément logique de C1.
- **R-6/R-8 :** supprimer un écho ou lire une fenêtre centrale change le sens disponible. Une fenêtre centrale n’est pas un contrôle sémantiquement neutre.
- **R-7 :** « le marqueur prédit aussi bien » et « le marqueur ne corrèle pas aux résidus » ne sont ni exclusifs ni exhaustifs. La cible reste construite par le juge.
- **R-9 :** rôle, tâche, stimuli et instruction changent ensemble. Deux classifications de régime différentes ne constituent pas un contraste direct entre coefficients.
- **R-10 :** la disjonction des corpus n’est pas établie par leurs noms. Le titre prédit un déplacement de cible, alors que \(H_A\) prédit une baisse du gain. L’absence de différence significative de \(g\) ne prouve pas sa stabilité.

### (b) Conditions probabilistes

**HYPOTHÈSE — modèles conditionnels :**

- **R-1/R-2 :** si \(S\not\!\perp Y(t)\mid i\), les contrastes conditionnels sur \(S\) n’identifient pas \(E[Y(1)-Y(0)]\).
- **R-3 :** si
  \(\inf_{\eta_A,\eta_B}D_{\mathrm{KL}}(P_A^{\eta_A}\Vert P_B^{\eta_B})=0\),
  aucune puissance uniforme n’est garantie sur les familles proposées.
- **R-4 :** dans \(X=\mu+u,\ Z=\mu+v,\ Y=a+b\mu+e\),
  \[
  \hat b_{\mathrm{IV}}=\frac{\widehat{\operatorname{Cov}}(Z,Y)}
  {\widehat{\operatorname{Cov}}(Z,X)}.
  \]
  L’identification échoue si le dénominateur est nul ; elle est biaisée si \(\operatorname{Cov}(Z,e-bu)\neq0\). Pour une fonction d’écrêtage \(h\), \(E[h(X)]\neq h(E[X])\) en général.
- **R-5/R-9 :** les événements « rejet de \(g=0\) dans une condition » et « non-rejet dans l’autre » ne déterminent pas le signe ni l’intervalle de \(g_A-g_B\).
- **R-6/R-8/R-10 :** pour \(c=a/g\), l’estimateur devient faiblement identifié lorsque \(g\) approche zéro. Une comparaison de cibles peut alors avoir une variance non bornée.
- **R-7 :** \(R^2(M)\geq R^2(L)\) est compatible avec \(\operatorname{Cov}(M,Y-\hat Y_L)=0\), notamment lorsque les prédictions sont identiques.
- **R-10 :** si \(P_{\mathrm{test}}(i\in\mathcal I_{\mathrm{extraction}})>0\), l’erreur évaluée n’est pas celle d’un transfert vers des items entièrement nouveaux.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE :**

- **R-1/R-2 :** mêmes protections contre sélection et fuite lexicale que celles exigées spécifiquement pour ces analyses : annotations indépendantes, items réservés, résultat marginal conservé.
- **R-3/R-4 :** récupération de paramètres sur lois synthétiques ; instruments neutres obtenus dans une même campagne ; comparaison écrêtée à complexité et validation comparables.
- **R-5/R-9 :** contraste direct des paramètres et calibration commune, pas seulement comparaison de verdicts C1.
- **R-6/R-8 :** édition placebo sémantiquement contrôlée, ordre de lecture randomisé, conservation des réponses complètes.
- **R-7 :** évaluation humaine indépendante et prédiction hors items.
- **R-10 :** manifeste vérifiable des ensembles d’extraction/évaluation ; intervention factice et sous-espaces aléatoires appariés en énergie retirée, pas seulement en rang.

## Sur la proposition C

### (a) Défauts de méthode

**OBSERVÉ-NON-AUDITÉ :** l’idée 1 annonce un résultat sur Qwen et Mistral mais prévoit de modifier des réponses de Llama. L’idée 10 compte comme paires ce que la pièce source décrit comme réponses individuelles.

**HYPOTHÈSE :**

- **Idées 1/3/10 :** suppression, filtrage et corrélations lexicales ne démontrent ni « politesse seule », ni filtre de sécurité, ni prudence épistémique. L’issue négative ne prouve pas une causalité distribuée.
- **Idée 2 :** sans le prompt original, le préremplissage n’est pas une continuation équivalente. Même avec lui, lire un verdict dans la prose ne prouve pas une auto-excitation.
- **Idée 4 :** impératif et témoignage d’un lecteur diffèrent aussi en autorité et pertinence informationnelle. La longueur égale n’isole pas ces dimensions.
- **Idée 5 :** une projection aléatoire peut préserver un signal de faible dimension. Son succès ne prouve pas un codage diffus. La dimension annoncée et la fraction de variance exigée ne sont pas automatiquement compatibles.
- **Idée 6 :** divergence précoce ne signifie pas détermination causale précoce. Une greffe transfère du contenu et change de tokenisation ; son échec ne localise rien « dans les poids profonds ».
- **Idée 7 :** franchir C1 ne teste pas une modification de pente. Les estimations ponctuelles rapportées pour Mistral ne présentent pas le creux de gain que suggère la succession des étiquettes de régime.
- **Idée 8 :** neutraliser le routage d’un suffixe peut réduire \(g\) autant que neutraliser un calcul de cible. Les deux explications prédisent donc l’issue dite décisive.
- **Idée 9 :** transporter une droite n’identifie pas une intégration bayésienne ; plusieurs règles non bayésiennes donnent cette prédiction.

### (b) Conditions probabilistes

**HYPOTHÈSE — modèles conditionnels :**

- **Idées 1/3/10 :** mêmes distributions conditionnelles observables possibles sous médiation causale et sélection : \(P(Y,S\mid T)\) seul ne détermine pas \(P(Y\mid do(S),T)\).
- **Idées 2/6 :** si \(P(Y\mid X_{\mathrm{original}},P)\neq P(Y\mid X_{\mathrm{reconstruit}},P)\), les estimateurs ciblent des lois différentes. Si les deux mécanismes induisent le même \(P(Y\mid P,T)\), ils ne sont pas identifiables.
- **Idée 4 :** pour un contraste apparié \(D_i\), \(\operatorname{Var}(\bar D)=\operatorname{Var}(D_i)/n\) sous indépendance des items ; le déterminisme des lectures n’impose pas \(\operatorname{Var}(D_i)=0\).
- **Idée 5 :** avec \(Y=\beta^\top X+\epsilon\), une projection \(P\) peut conserver la prédiction dès que \(\beta^\top X\) est récupérable depuis \(PX\), quelle que soit la parcimonie de \(\beta\). À covariance isotrope, la fraction attendue de variance conservée vaut \(d/D\).
- **Idée 7 :** \(P(\hat g-z_\alpha\widehat{\mathrm{SE}}>0)\) dépend de \(g/\mathrm{SE}\), pas seulement de \(g\). Un changement de classement peut survenir à \(g\) constant.
- **Idée 8 :** si \(P_A(Y\mid do(I))=P_B(Y\mid do(I))\) pour toutes les interventions proposées, leur pouvoir discriminant est nul.
- **Idée 9 :** \(E[Y\mid X,S]=a+bX\) n’identifie aucun algorithme de mise à jour particulier.
- **Idée 10 :** sous corrélation intra-item \(\rho\), l’effectif effectif d’un plan équilibré est \(nK/[1+(K-1)\rho]\), non \(nK\).

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE :**

- **1/3/10 :** corpus réservé, annotations humaines aveugles, éditions préservant le verdict et estimation marginale.
- **2/6 :** préfixe neutre du même item, préfixe permuté, préfixe auto-produit ; prompt et tokenisation publiés.
- **4 :** plan croisant impératif, source et polarité.
- **5 :** directions aléatoires multiples, sélection sans étiquettes test, validation imbriquée et contrôle de l’énergie conservée.
- **7 :** plusieurs paraphrases par dose et répétition contemporaine du suffixe standard.
- **8 :** patching neutre-vers-neutre, suffixe non évaluatif et têtes témoins appariées en activité.
- **9 :** permutations et formulations réservées ; comparaison explicite avec des règles non bayésiennes.

## Sur la proposition D

### (a) Défauts de méthode

**HYPOTHÈSE :**

- **D1 :** un changement de C1/C2 confond instabilité substantielle et proximité d’un seuil. La variance du juge doit être séparée des effets de lot et d’ordre.
- **D2/D3 :** performance prédictive et localisation textuelle ne sont pas causalité ; ouverture et reste peuvent chacun porter le même verdict.
- **D4 :** auto-relire une réponse est une tâche différente de noter l’item original.
- **D5 :** la calibration affine transforme nécessairement les cibles. Son succès peut relever de cette transformation, non d’une destination latente commune.
- **D6 :** variance neutre, moyenne neutre et déplacement partagent des tirages ; leur dépendance d’estimation peut créer la prédictivité recherchée.
- **D7 :** moyenne et variance ne déterminent pas une loi bornée unique. Le nul reste insuffisamment spécifié.
- **D8/D9 :** intensité, formulation et caractère social ne sont pas des alternatives exclusives ; leurs effets peuvent coexister.
- **D10 :** résistance à une contradiction est compatible avec un suivi d’instruction dépendant du contexte. Une note congruente peut renforcer un score sans provoquer d’erreur.

### (b) Conditions probabilistes

**HYPOTHÈSE — modèles conditionnels :**

- **D1 :** si \(\hat g\sim N(g,s^2)\), la probabilité de franchir un seuil reste sensible à \(g/s\), même pour une variance de relecture faible.
- **D2/D3 :** si les scores des segments sont colinéaires, leurs contributions séparées ne sont pas identifiables.
- **D4 :** si les fonctions de mesure \(m_{\mathrm{item}}\) et \(m_{\mathrm{réponse}}\) sont inconnues, leur contraste confond paramètres comportementaux et paramètres de mesure.
- **D5 :** sous \(Y'=a+bY\), \(g'=g\) et \(c'=a+bc\). Une calibration neutre n’identifie le transfert que si \(P(Y'\mid Y,T)\) reste invariant en \(T\).
- **D6 :** \(\operatorname{Cov}(\bar X,S_X^2)=\mu_3/K\). Une asymétrie neutre suffit donc à corréler les estimateurs employés.
- **D7 :** plusieurs lois \(F\) partagent \((E_FY,\operatorname{Var}_FY)\) mais produisent des risques prédictifs distincts.
- **D8/D9 :** si les covariables sont colinéaires ou l’intensité mesurée avec erreur inconnue, leurs coefficients séparés sont non identifiables.
- **D10 :** lorsque \(P(Y=y_{\max})\) ou \(P(Y=y_{\min})\) approche l’unité, les contrastes congruents sont comprimés par la borne.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE :** D doit ajouter des doublons intercalés entre lots pour D1 ; des segments synthétiques à verdict conservé pour D2–D4 ; une calibration sur items réservés pour D5 ; des tirages neutres indépendants pour construire moyenne et variance en D6 ; plusieurs nuls bornés explicitement paramétrés pour D7 ; un plan factoriel avec paraphrases réservées pour D8–D9 ; enfin des verdicts intérieurs à l’échelle et des instructions sans polarité pour D10.

FIN-DE-CELLULE