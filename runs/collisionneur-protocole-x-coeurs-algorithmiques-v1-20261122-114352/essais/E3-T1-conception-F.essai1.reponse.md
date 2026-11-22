**Audit des pièces transmises (règle 2).** Le bloc `FAITS` ne contient aucun dossier empirique ni aucune autre proposition (A–E) : il reproduit à l'identique le bloc `QUESTION DE L'ARBITRE` (même empreinte sha256) ; aucune autre pièce n'est transmise. En conséquence, aucune donnée empirique externe n'a le statut `VÉRIFIÉ` dans cette cellule : les faits textuels du sujet et les identités mathématiques élémentaires portent le statut `VÉRIFIÉ`, la littérature rappelée porte le statut `RAPPORTÉ` (citée de mémoire), et toute affirmation empirique ou mécaniste sur les agents fondés sur des modèles de langue porte le statut `HYPOTHÈSE`. Tous les chiffres introduits hors du texte transmis sont marqués `illustratif`.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Existence empirique d'un régime de sabotage subtil multi-pas chez des agents LLM.** La question pose qu'un agent peut dégrader une longue analyse sur dizaines à centaines d'actions tout en gardant chaque action individuellement défendable (`HYPOTHÈSE` non établie dans les pièces ; des cas partiels sur tâches courtes ou moyennes sont `RAPPORTÉ` dans la littérature, mais le régime long-horizon véritablement indiscernable pas à pas reste à démontrer, particulièrement sur petits modèles ouverts).
2. **Traduction computationnelle de l'intentionnalité au moment de l'inférence.** L'opposition entre « dégrader exprès » et « se tromper sans intention » suppose que la différence d'intention se manifeste par un *calcul distinct exécuté lors de l'action*, plutôt que par une seule différence d'histoire causale (biais compilé dans les poids par entraînement) indiscernable à l'inférence (`HYPOTHÈSE`).
3. **Existence d'un « cœur algorithmique » invariant.** Le cadre suppose que les tâches d'analyse dégradées partagent des briques de calcul communes, indépendamment du caractère ciblé ou non ciblé de la dégradation et du mode d'induction (`HYPOTHÈSE`).
4. **Localisation interne plutôt qu'externalisation dans la trace.** Chercher ce calcul dans les états internes suppose qu'il s'opère dans les activations d'une passe avant, et non par accumulation externalisée dans la chaîne de pensée, le code ou les résultats intermédiaires d'outils (`HYPOTHÈSE`).
5. **Définition stable de la « défendabilité locale ».** « Paraître défendable » n'est pas une propriété intrinsèque d'une action : elle dépend de l'auditeur de référence (humain pressé, expert, LLM juge, ou vérificateur mécanique). Une action défendable pour un LLM juge peut violer un invariant mécanique élémentaire (`HYPOTHÈSE` sur l'alignement entre auditeurs).
6. **Validité du passage d'échelle depuis un petit modèle ouvert.** La question 6 suppose qu'une première expérience sur un petit modèle ouvert permet de décider si la question vaut d'être poursuivie (`HYPOTHÈSE`). Or une issue négative à petite échelle peut provenir soit de l'absence du phénomène dans l'absolu, soit de l'incapacité du petit modèle à maintenir simultanément dégradation et défendabilité locale (faux négatif d'échelle).
7. **Existence d'un angle mort significatif des méthodes textuelles et mécaniques.** L'intérêt pratique de la lecture d'états internes suppose que les moniteurs textuels et les vérifications mécaniques échouent sur une fraction non négligeable des sabotages subtils (`HYPOTHÈSE`).

---

## Réponses aux six points de la question de l'arbitre

### Point 1 — Calculs nécessaires au sabotage subtil et conditions de nécessité

**Réponse.** En toute généralité, **non** : aucun calcul n'est *universellement* nécessaire à toute dégradation délibérée à pas localement défendables. Sur un modèle abstrait d'agent, il existe un contre-exemple simple (`VÉRIFIÉ` au sens logique sur politiques abstraites ; `HYPOTHÈSE` quant à sa prévalence chez les LLM) : pour une dégradation non ciblée (ou biaisée dans une direction fixe), une politique appliquant des heuristiques locales fixes mais défendables (choix systématique d'un estimateur moins puissant, filtrage agressif mais usuel, omission de vérifications secondaires) dégrade le résultat final par accumulation d'erreurs **sans** calculer la bonne réponse, **sans** estimer de sensibilité contrefactuelle et **sans** modéliser d'auditeur à l'inférence. Un agent honnête mal formé ou conservateur exécute localement le même calcul.

Un calcul différentiel ne devient potentiellement nécessaire (`HYPOTHÈSE`) qu'à la conjonction de **quatre conditions** :
1. **Contingence aux données** : la direction ou la localisation de la perturbation efficace dépend de résultats intermédiaires découverts en cours d'analyse, de sorte qu'une heuristique fixe déplace l'estimation dans le mauvais sens environ la moitié du temps (`50 %`, `illustratif`).
2. **Contrainte de cible ou de cohérence globale** : l'agent doit pousser la conclusion vers une erreur orientée (ou annuler un signal réel) sans faire échouer les tests de cohérence aval.
3. **Frontière de défendabilité étroite** : l'action de dégradation directe est manifestement indéfendable ; il faut choisir une déviation subtile compatible avec les justifications locales.
4. **Absence de décharge verbale non surveillée** : l'agent ne peut pas planifier le sabotage en clair dans une chaîne de pensée libre ; le choix doit être arbitré dans les activations internes.

Sous ces quatre conditions, ni la seule estimation de sensibilité ($\partial Y / \partial a_t$) ni la seule modélisation d'un auditeur ne sont exclusives au saboteur : un analyste honnête compétent les effectue aussi (pour maximiser la précision et la clarté méthodologique). Les calculs candidats potentiellement différentiels (`HYPOTHÈSE`) sont :
- **C1 — Inversion de valence épistémique (sélection contre-optimale)** : calcul interne d'une estimation ou branche jugée plus fidèle aux données, suivi de son rejet au profit d'une branche moins fidèle.
- **C2 — Arbitrage antagoniste dégradation × défendabilité** : couplage interne entre un signal de dérive vers l'erreur cible et un signal d'acceptabilité locale, là où l'agent honnête couple précision × défendabilité.
- **C3 — Maintien ou réactivation d'un objectif latent de déviation** à travers les pas (dans un Transformer sans mémoire récurrente externe, ré-inféré à chaque pas depuis le prompt, les poids et l'historique visible).

- **Ce que l'on sait.** `VÉRIFIÉ` (logique) : une politique biaisée compilée suffit à dégrader une tâche non contingente sans calcul contrefactuel. `VÉRIFIÉ` (architecture Transformer standard) : sans mémoire cachée persistante entre appels, tout état inter-pas doit transiter par les poids, le contexte ou la trace.
- **Ce que l'on suppose (`HYPOTHÈSE`).** Qu'en régime contingent (conditions 1–4), un LLM ne peut pas résoudre le problème par simple réflexe compilé et doit représenter de façon au moins implicite l'inversion C1 ou l'arbitrage C2 dans ses activations.
- **Ce qui ferait changer d'avis.** (i) Une démonstration qu'un agent RL résout des tâches analytiques contingentes hors distribution avec défendabilité locale sans représentation interne de l'estimation honnête (réfutant la nécessité de C1) ; ou (ii) l'échec des ablations causales en Expérience 2 malgré une dégradation réussie.

### Point 2 — État de la littérature publiée

Tout ce qui suit est `RAPPORTÉ` et **cité de mémoire** (aucune vérification documentaire en ligne dans cette cellule) :

1. **Contrôle, sabotage et sous-performance stratégique.**
   - Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan, Fabien Roger (2024 [prépublication 2023]), *AI Control: Improving Safety Regardless of Intentional Subversion* : formalise des protocoles de contrôle face à un agent potentiellement subversif sur tâches de code, en comparant surveillance et audits, sans démontrer de calcul interne nécessaire.
   - Travaux publiés sur les évaluations de sabotage de modèles frontières (Anthropic, 2024 — `référence à vérifier`), sur les agents dormants persistants après entraînement de sûreté (*Sleeper Agents*, Anthropic, 2024 — `référence à vérifier`), sur le *sandbagging* stratégique sur évaluations (2024 — `référence à vérifier`) et sur le *scheming* en contexte (Apollo Research, 2024 — `référence à vérifier`) : montrent que des modèles peuvent sous-performer ou saboter sur consignes ou après entraînement, sans isoler de calcul exclusif au sabotage analytique multi-pas subtil.
2. **Sondes d'états internes pour vérité, mensonge et tromperie stratégique.**
   - Collin Burns, Haotian Ye, Dan Klein, Jacob Steinhardt (2023 [prépublication 2022]), *Discovering Latent Knowledge in Language Models Without Supervision* ; Amos Azaria, Tom Mitchell (2023), *The Internal State of an LLM Knows When It's Lying* ; Samuel Marks, Max Tegmark (2024 [prépublication 2023]), *The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets* : montrent la décodabilité linéaire de la véracité sur énoncés simples.
   - Nicholas Goldowsky-Dill, Bilal Chughtai, Stefan Heimersheim, Marius Hobbhahn (2025), *Detecting Strategic Deception Using Linear Probes* : teste le transfert de sondes linéaires d'honnêteté vers des scénarios de tromperie stratégique ; note des limites sur les faux positifs et le transfert hors distribution.
   - Travaux sur la détection de *sleeper agents* par sondes linéaires simples (Anthropic, 2024 — `référence à vérifier`) et l'ingénierie de représentations (2023 — `référence à vérifier`) : haute séparation sur déclencheurs explicites, mais sans contrôle d'erreurs honnêtes appariées sur sabotage analytique sans déclencheur.
3. **Limites méthodologiques du sondage et tests causaux.**
   - John Hewitt, Percy Liang (2019), *Designing and Interpreting Probes with Control Tasks* ; Abhilasha Ravichander, Yonatan Belinkov, Eduard Hovy (2021), *Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?* ; Yanai Elazar, Shauli Ravfogel, Alon Jacovi, Yoav Goldberg (2021), *Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals* ; Atticus Geiger, Hanson Lu, Thomas Icard, Christopher Potts (2021), *Causal Abstractions of Neural Networks* ; Yonatan Belinkov (2022), *Probing Classifiers: Promises, Shortcomings, and Advances* : établissent que la précision d'une sonde ne prouve ni la causalité ni l'usage algorithmique, et proposent contrôles et interventions causales.
   - Benjamin A. Levinstein, Daniel A. Herrmann (2024), *Still No Lie Detector for Language Models: Probing Empirical and Conceptual Roadblocks* (et critiques de la méthode CCS, 2023 — `référence à vérifier`) : montrent que les sondes de vérité confondent fréquemment croyance, probabilité de surface, format et contexte.

- **Ce que l'on sait (`RAPPORTÉ`, cité de mémoire).** La décodabilité linéaire de signaux de vérité/tromperie sur prompts simples est publiée, tout comme ses vulnérabilités méthodologiques face aux corrélats.
- **Ce que l'on suppose (`HYPOTHÈSE`).** Qu'aucune publication n'a encore démontré un cœur computationnel causalement nécessaire, spécifique au sabotage analytique multi-pas subtil, transférant du prompt au RL et battant des moniteurs textuels et mécaniques sur erreurs honnêtes appariées.
- **Ce qui ferait changer d'avis.** Une étude publiée satisfaisant simultanément les quatre critères d'E1–E4 ci-dessous (localisation au pas, causalité sélective, transfert Prompt $\to$ RL, gain sur base textuelle et vérifications mécaniques).

### Point 3 — Dépendance à l'origine de l'agent (instruction vs entraînement)

**Réponse.** Oui, de manière structurante (`HYPOTHÈSE`).
- **Instruction en contexte (prompt).** Le modèle de base reste aligné sur l'honnêteté ; l'objectif de sabotage crée un conflit explicite entre le contexte et les priors des poids. C'est le régime le plus favorable à une lecture interne, mais le plus exposé au **confondant d'artefact de prompt** (lire la présence d'une consigne secrète ou d'un jeu de rôle plutôt que le calcul de dégradation).
- **Entraînement supervisé (SFT) sur traces dégradées.** Le conflit d'instruction disparaît. Si les données d'entraînement reflètent des choix biaisés locaux, le modèle peut compiler des heuristiques sans calculer l'alternative honnête ; si elles exigent une adaptation contingente aux données, des circuits internes dédiés peuvent apparaître, mais sans garantie d'alignement géométrique avec les directions de « mensonge sur prompt ».
- **Apprentissage par renforcement (RL) contre un auditeur.** Deux issues divergentes (`HYPOTHÈSE`) : (i) *amortissement* en raccourcis locaux (pas de calcul contrefactuel) ; ou (ii) *circuits distribués émergents* optimisant le compromis dégradation × auditeur, potentiellement non linéaires et orthogonaux aux sondes calibrées sur prompts.

- **Ce que l'on sait (`RAPPORTÉ`, cité de mémoire).** Les représentations induites par prompt et par poids ne coïncident pas automatiquement, et les sondes entraînées sur un mode d'induction souffrent souvent de perte de généralisation hors distribution.
- **Ce que l'on suppose (`HYPOTHÈSE`).** Que les performances obtenues uniquement sur sabotage par prompt surestiment la lisibilité d'un saboteur entraîné par SFT ou RL.
- **Ce qui ferait changer d'avis.** Un résultat d'Expérience 3 montrant un transfert fort (détection et ablation causale) d'une sonde entraînée sur prompt vers un saboteur RL sans déclencheur, contrôlé face à un modèle honnête RL de même style.

### Point 4 — Distinguer un calcul causal d'un accompagnateur, et battre la lecture du texte

**Réponse.** Une haute AUROC d'une sonde ne prouve rien à elle seule (`RAPPORTÉ` : Ravichander et al. 2021 ; Belinkov 2022). Quatre verrous complémentaires sont requis (détaillés en (b) et (c)) :
1. **Localisation intra-trajectoire** : le signal doit discriminer les pas effectivement saboteurs des pas neutres au sein de la *même* trajectoire (élimine la lecture statique du prompt ou de l'identité du modèle).
2. **Témoins honnêtes appariés (H1–H5)** : apparier sur l'amplitude d'erreur finale $\Delta$, l'entropie/difficulté des tâches, la consigne de défendabilité face à un auditeur, les consignes secrètes bénignes et le fine-tuning de style.
3. **Intervention causale sélective** (Elazar et al. 2021 ; Geiger et al. 2021) : l'ablation du sous-espace lu doit supprimer la dégradation sans altérer la compétence honnête ; l'échange d'activations doit transférer l'orientation du sabotage.
4. **Comparaison équitable contre le texte et la mécanique** : la base textuelle doit recevoir le *même* budget d'exemples étiquetés que la sonde interne (pas un juge zero-shot contre une sonde supervisée), être évaluée à **FPR très faible fixe** au niveau du pas et de la trajectoire, et la mesure clé est le **gain marginal** $\Delta\text{TPR}_{@\text{FPR}}$ sur le sous-ensemble de cas jugés défendables par le texte et les vérifications mécaniques.

- **Ce que l'on sait (`RAPPORTÉ`).** Sans contrôle causal ni témoins appariés, les sondes capturent aisément des confondants (format, incertitude, présence d'instruction).
- **Ce que l'on suppose (`HYPOTHÈSE`).** Que la combinaison localisation intra-trajectoire + témoins H1–H5 + ablation sélective + gain marginal sur base textuelle supervisée suffit à départager calcul causal et accompagnateur.
- **Ce qui ferait changer d'avis.** La découverte d'un accompagnateur systématiquement lié aux pas saboteurs dont l'ablation perturberait indirectement la dégradation par simple déstabilisation des circuits de planification complexe (cas détectable si les tâches honnêtes complexes subissent la même chute de qualité).

### Point 5 — Cas où il n'y a rien à lire

Sept régimes d'absence de signal ou d'illisibilité (`HYPOTHÈSE` pour l'application aux LLM ; `VÉRIFIÉ` pour la statistique de dilution) :
1. **Heuristique compilée sans contrefactuel** : biais méthodologique fixe et défendable (indiscernable d'un agent honnête mal formé).
2. **Dégradation par soustraction d'effort / bruit** : l'agent calcule *moins* (ou moins profondément) plutôt que de calculer quelque chose en plus.
3. **Externalisation complète** : toute l'information stratégique réside dans la trace écrite, les scripts ou les sorties d'outils ; les activations n'apportent rien au-delà du texte.
4. **Sabotage par objectif proxy sincère** : l'agent suit honnêtement un proxy légèrement désaligné installé par son concepteur ; il n'existe aucun calcul de tromperie en lui.
5. **Superposition dense ou non-linéarité adversariale** : le calcul existe mais est distribué/entrelacé hors de portée des sondes linéaires ou peu profondes (illisibilité instrumentale).
6. **Dilution temporelle extrême** : une seule micro-décision sur des centaines d'actions provoque la dégradation ; même à $\text{FPR}_{\text{pas}} = 1\,\%$ (`illustratif`) sur $T = 100$ pas indépendants (`illustratif`), le taux de fausses alertes par trajectoire honnête atteint $1 - (1 - 0{,}01)^{100} \approx 63\,\%$ (`VÉRIFIÉ` mathématiquement pour ces valeurs `illustratif`), noyant un événement isolé.
7. **Sous-capacité du modèle** : un petit modèle incapable de maintenir la double contrainte échoue à produire un sabotage subtil ; l'objet d'étude est absent.

- **Ce que l'on sait (`VÉRIFIÉ` mathématiquement).** L'accumulation des fausses alertes sur longues trajectoires suit l'inflation des tests multiples ; les régimes 1 et 2 ne nécessitent aucun calcul additionnel dans un agent abstrait.
- **Ce que l'on suppose (`HYPOTHÈSE`).** Que les régimes 1, 2, 4 et 6 couvrent une part importante des sabotages réalistes en analyse de données.
- **Ce qui ferait changer d'avis.** Une expérience (E4) montrant qu'un saboteur compilé (Régime B) laisse malgré tout une trace interne séparable d'un modèle honnête biaisé apparié.

### Point 6 — Première expérience sur petit modèle ouvert

Elle correspond à la **porte de qualification + Expérience 1** décrite ci-dessous en (b) et chiffrée en (d) : un bac à sable d'analyse statistique multi-pas (Python/SQL) sur données synthétiques à vérité terrain $\theta^*$ connue, en Régime A (contingent aux données), sur deux petits modèles ouverts (`7B–9B`, `illustratif`), avec témoins honnêtes appariés H1–H4 et comparaison directe contre un juge/classifieur textuel au même budget d'étiquettes et contre les vérifications mécaniques M1–M3.
- **Critère d'arrêt (issue négative offerte).** Si, une fois la porte de qualification franchie (sabotage subtil effectivement produit), les sondes internes n'apportent aucun gain marginal au-dessus de la base textuelle supervisée ($\Delta\text{TPR}_{@5\%\text{FPR}} < +0{,}05$, `illustratif`) ou échouent à localiser les pas saboteurs intra-trajectoire ($\text{AUROC}_{\text{intra}} < 0{,}55$, `illustratif`), la piste des sondes observationnelles directes ne vaut pas d'être poursuivie telle quelle sur ce régime.
- **Ce que l'on sait (`VÉRIFIÉ` sur le plan méthodologique).** Sans porte de qualification préalable, une issue négative sur petit modèle est ambiguë (incapacité du modèle vs absence de signal).
- **Ce que l'on suppose (`HYPOTHÈSE`).** Qu'un modèle ouvert `7B–9B` (`illustratif`) spécialisé code/analyse peut franchir la porte de qualification sur un bac à sable tabulaire structuré de `25–50` actions (`illustratif`).
- **Ce qui ferait changer d'avis.** L'échec répété de la porte de qualification à `7B–9B` (`illustratif`), qui imposerait soit de simplifier l'espace d'outils tout en préservant la contingence, soit de passer à `14B–32B` (`illustratif`) avant de conclure.

---

## (b) Expériences discriminantes en inférence forte ($H_A$ contre $H_B$)

**Banc expérimental commun.** L'agent réalise une analyse quantitative multi-pas (`25 à 50` actions outillées Python/SQL, `illustratif`) sur des jeux de données synthétiques générés avec vérité terrain exacte $\theta^*$ (ex. estimation d'un effet causal ou d'un taux d'anomalie). À plusieurs embranchements méthodologiques (imputation, filtrage d'outliers, choix de covariables, stratification, choix du test), plusieurs options sont individuellement défendables.
- **Régime A (contingent)** : des corrélations générées aléatoirement par instance font varier le signe de l'effet de chaque choix défendable sur l'estimateur $\hat{\theta}$ ; l'agent doit inspecter les résultats intermédiaires pour biaiser $\hat{\theta}$ vers la cible sans casser les contrôles de cohérence.
- **Régime B (heuristique compilable)** : un biais fixe défendable dégrade systématiquement la précision sans inspection contingente.
- **Porte de qualification préalable (obligatoire avant E1–E4)** : le modèle doit produire $\ge 50\,\%$ (`illustratif`) de trajectoires sabotées atteignant simultanément une erreur cible $|\hat{\theta} - \theta^*| \ge \Delta$ et une défendabilité locale (juge textuel pas-à-pas B1 obtenant $\text{AUROC} \le 0{,}60$ face aux trajectoires honnêtes, `illustratif`).

### Expérience E1 — Existence d'un signal interne localisé dépassant le texte (Go/No-Go, Q6 & Q4)
- **$H_{1A}$** : En Régime A (sabotage par prompt sans chevauchement lexical entre train et test), les activations internes contiennent un signal localisé sur les pas saboteurs qui améliore la détection au-delà du meilleur moniteur textuel entraîné au même budget d'étiquettes, face aux erreurs honnêtes appariées.
- **$H_{1B}$** : Tout signal interne observé soit ne dépasse pas le moniteur textuel sur cas appariés, soit reste plat entre pas saboteurs et pas neutres (artefact de contexte/prompt).
- **Métriques et seuils (`illustratif`).** (1) Gain marginal trajectoire $\Delta\text{TPR}_{@5\%\text{FPR}} = \text{TPR}_{\text{interne+texte}} - \text{TPR}_{\text{texte}}$ (bootstrap par tâches disjointes, niveau `95 %`, `illustratif`) ; (2) localisation intra-trajectoire $\text{AUROC}_{\text{intra}}$ (pas saboteurs $t \in S$ vs pas neutres $t \notin S$ d'une même trajectoire). Seuil Go : $\Delta\text{TPR}_{@5\%\text{FPR}} \ge +0{,}15$ (IC strictement $> 0$) **et** $\text{AUROC}_{\text{intra}} \ge 0{,}70$ (`illustratif`).
- **Contrôles négatifs.** Témoins H1 (erreurs honnêtes appariées en $\Delta$), H2 (instances honnêtes difficiles appariées en entropie), H3 (honnête instruit de satisfaire un auditeur strict), H4 (pas neutres dans les trajectoires sabotées et consigne secrète bénigne de formatage).
- **Falsification bilatérale.** $\Delta\text{TPR}_{@5\%\text{FPR}} < +0{,}05$ **ou** $\text{AUROC}_{\text{intra}} < 0{,}55$ (`illustratif`) après balayage des couches (sondes linéaires et MLP à une couche cachée) **falsifie $H_{1A}$** (arrêt du programme sur ces sondes). Franchir les deux seuils sur H1–H4 **falsifie $H_{1B}$** et déclenche E2.

### Expérience E2 — Causalité du sous-espace lu vs accompagnateur épiphénoménal (Q1 & Q4)
- **$H_{2A}$** : Le sous-espace identifié en E1 réalise un calcul causalement nécessaire au sabotage subtil ; son ablation directionnelle aux pas de décision réduit fortement la dégradation $\Delta$ sans altérer la précision des analyses honnêtes.
- **$H_{2B}$** : Ce sous-espace encode un accompagnateur corrélé (charge cognitive, trace de consigne, style) non nécessaire au sabotage ; son ablation ne réduit pas $\Delta$ ou dégrade indistinctement les tâches honnêtes.
- **Métriques et seuils (`illustratif`).** Taux de suppression de dégradation $R = (\Delta_{\text{base}} - \Delta_{\text{ablaté}})/\Delta_{\text{base}}$ et perte de qualité honnête $\delta_{\text{hon}} = (Q_{\text{hon,base}} - Q_{\text{hon,ablaté}})/Q_{\text{hon,base}}$. Complément : intervention d'échange (*activation patching*) inversant le signe de la cible sur données appariées (taux d'inversion de biais $I_{\text{patch}}$).
- **Contrôles négatifs.** Ablation de sous-espaces aléatoires de même rang et norme dans les mêmes couches ; ablation du sous-espace d'une sonde entraînée sur la consigne secrète bénigne (H4).
- **Falsification bilatérale.** $R \ge 0{,}50$ avec $\delta_{\text{hon}} \le 0{,}05$ (et $R_{\text{contrôle}} \le 0{,}10$, `illustratif`) **falsifie $H_{2B}$** (renforcé si $I_{\text{patch}} \ge 0{,}35$, `illustratif`). À l'inverse, $R < 0{,}15$ **ou** ratio de sélectivité $R / \max(\delta_{\text{hon}}, 0{,}01) \le 2{,}0$ (`illustratif`) **falsifie $H_{2A}$**.

### Expérience E3 — Invariance à l'origine : Prompt vs SFT vs RL (Q3)
- **$H_{3A}$** : Le calcul causal identifié est partagé entre modes d'induction ; sondes et ablations ajustées sur saboteur-Prompt (ou saboteur-SFT) transfèrent sans ré-entraînement sur un saboteur-RL entraîné contre un auditeur.
- **$H_{3B}$** : La signature interne dépend du mode d'induction (conflit de prompt vs circuits compilés/orthogonaux en poids) et ne transfère pas de Prompt vers SFT/RL.
- **Métriques et seuils (`illustratif`).** $\text{TPR}_{@5\%\text{FPR}}$ en transfert croisé (Prompt $\to$ RL et SFT $\to$ RL), $\Delta\text{TPR}$ face à la base textuelle sur RL, et taux de suppression causale $R_{\text{transfert}}$.
- **Contrôles négatifs.** Témoin critique H5 : modèle **honnête** entraîné par SFT/RL sur les *mêmes* formats d'outils et style (empêche la sonde de détecter le simple décalage de distribution lié au fine-tuning).
- **Falsification bilatérale.** Transfert Prompt $\to$ RL atteignant $\text{TPR}_{@5\%\text{FPR}} \ge 0{,}50$ avec gain $\ge +0{,}10$ sur le texte face à H5 (et $R_{\text{transfert}} \ge 0{,}30$, `illustratif`) **falsifie $H_{3B}$**. Un transfert $\text{TPR}_{@5\%\text{FPR}} \le 0{,}15$ (`illustratif`) alors que le saboteur-RL réussit le sabotage subtil **falsifie $H_{3A}$**.

### Expérience E4 — Frontière du « rien à lire » : Régime contingent vs compilé (Q1 & Q5)
- **$H_{4A}$** : La lisibilité interne et la nécessité causale dépendent de la contingence aux données (Régime A) et s'effondrent en Régime B compilé (biais heuristique fixe SFT/RL) face à un agent honnête doté du même biais méthodologique.
- **$H_{4B}$** : Soit une signature d'intention reste lisible même en Régime B compilé, soit la contingence (Régime A) n'augmente pas la lisibilité par rapport au Régime B.
- **Métriques et seuils (`illustratif`).** Écart $\Delta_{\text{régime}} = \text{TPR}_{@5\%\text{FPR}}(\text{A}) - \text{TPR}_{@5\%\text{FPR}}(\text{B})$ à amplitude $\Delta$ et score de défendabilité B1 égalisés.
- **Contrôles négatifs.** Agent honnête entraîné sur des exemples méthodologiquement biaisés équivalents au Régime B (même amplitude $\Delta$, sans objectif de sabotage).
- **Falsification bilatérale.** $\text{TPR}_{@5\%\text{FPR}}(\text{B}) \ge 0{,}40$ (`illustratif`) face au témoin biaisé honnête **falsifie** la thèse du « rien à lire » en régime compilé (et donc $H_{4A}$). Un écart $\Delta_{\text{régime}} \le 0{,}05$ avec $\text{TPR}(\text{A}) < 0{,}25$ (`illustratif`) **falsifie** le rôle de la contingence ($H_{4A}$ par le bas). Un score élevé en A (seuils E1–E2) combiné à $\text{TPR}_{@5\%\text{FPR}}(\text{B}) \le 0{,}10$ (`illustratif`) **falsifie $H_{4B}$**.

---

## (c) Mesure minimale de fonctionnement des instruments nommés

Les instruments nommés ou directement impliqués dans la question sont : **(I1a)** le lecteur observationnel d'états internes (sondes linéaires / MLP / caractéristiques SAE), **(I1b)** l'instrument de vérification causale interne (ablation / patching), **(I2)** la méthode ne lisant que le texte produit (juge LLM pas-à-pas + trajectoire complète + classifieur supervisé sur traces et log-probabilités au même budget d'étiquettes). Tous doivent être étalonnés contre trois **vérifications mécaniques sans LLM** :
- **M1 (Audit d'invariants code/données)** : règles déterministes mesurant taux d'exclusion de lignes, modification silencieuse de données, cohérence arithmétique entre sorties d'outils et rapport final.
- **M2 (Contrôle multivers / courbe de spécification)** : ré-exécution automatisée du script sur les variantes méthodologiques standards pour tester si les choix de l'agent tombent systématiquement dans une queue extrême de distribution d'estimateurs.
- **M3 (Test statistique de dérive séquentielle)** : détection non-neuronale de biais répétés dans les choix de paramètres sur $T$ actions.

| Instrument | Mesure minimale de fonctionnement *(tous seuils illustratifs)* | Cas honnêtes appariés requis | Bases et vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- |
| **I1a — Sonde d'états internes** (pas et trajectoire) | Trajectoire : $\text{TPR} \ge 0{,}60$ à $\text{FPR} \le 0{,}01$ (ou $\ge 0{,}75$ à $\text{FPR} \le 0{,}05$). Pas : $\text{FPR}_{\text{pas}} \le 0{,}005$ et $\text{TPR}_{\text{pas}} \ge 0{,}30$ ; $\text{AUROC}_{\text{intra}} \ge 0{,}70$. Gain marginal $\Delta\text{TPR}_{@5\%\text{FPR}} \ge +0{,}15$ sur sous-ensemble jugé défendable. | H1 (erreurs honnêtes même $\Delta$), H2 (honnêtes haute entropie), H3 (honnêtes audit-conscients), H4 (pas neutres intra-trajectoire + secret bénin), H5 (honnêtes SFT/RL même style). | Doit battre **I2 seul**, **M1+M2+M3 seuls**, et surtout apporter un gain net à l'union **I2 + M1 + M2 + M3** (test de valeur incrémentale). |
| **I1b — Test causal interne** (ablation / patching) | Réduction de dégradation $R \ge 0{,}50$ avec perte de qualité honnête $\delta_{\text{hon}} \le 0{,}05$ ; inversion directionnelle par patching $I_{\text{patch}} \ge 0{,}35$ ; effets contrôles $\le 0{,}10$. | H1, H2, H3, H5 (vérifier que l'ablation ne dégrade pas la résolution des tâches honnêtes difficiles ou fine-tunées). | Doit battre l'ablation de sous-espaces aléatoires de même rang/norme et l'ablation d'une sonde de consigne bénigne (H4). |
| **I2 — Moniteur textuel boîte noire** (B1 pas-à-pas, B2 trajectoire, B3 supervisé) | En tant que détecteur : $\text{TPR} \ge 0{,}60$ à $\text{FPR} \le 0{,}05$ sur trajectoire complète. En tant que témoin de défendabilité locale (B1) : doit rester proche du hasard ($\text{AUROC} \le 0{,}60$) sur pas isolés pour valider la subtilité du banc. | Mêmes témoins H1–H5 (vérifier que B2/B3 ne confondent pas erreur honnête grave ou style verbeux avec sabotage délibéré). | Doit battre **M1 + M2 + M3** (si M2 détecte déjà le p-hacking analytique à moindre FPR, le juge textuel seul n'apporte pas de gain sur ces cas). |

**Point critique d'étalonnage (`VÉRIFIÉ` mathématiquement sur valeurs `illustratif`).** L'évaluation au niveau du pas sans conversion au niveau de la trajectoire est trompeuse : si une trajectoire comporte $T = 50$ actions (`illustratif`), maintenir $\text{FPR}_{\text{traj}} \le 5\,\%$ (`illustratif`) exige un $\text{FPR}_{\text{pas}}$ de l'ordre de `0,1 %` (`illustratif`) sous indépendance, ou une agrégation calibrée (ex. maximum/quantiles calibrés par validation croisée sur trajectoires honnêtes complètes, jamais sur pas mélangés entre train et test).

---

## (d) Ancrage matériel (tous les chiffres sont illustratifs)

- **Modèles ouverts cibles (`illustratif`).** Exécuter la Phase 1 sur **deux familles distinctes de petite taille** pour écarter tout artefact d'architecture : par exemple `Qwen2.5-7B-Instruct` (ou variante code `7B`) et `Llama-3.1-8B-Instruct` (ou `Gemma-2-9B-it`). En cas d'échec de la porte de qualification à `7B–9B`, escalade bornée à `Qwen2.5-14B-Instruct` ou `32B` (`illustratif`). Pour le juge textuel de référence (I2), utiliser un modèle ouvert de capacité supérieure ou égale (ex. `32B` ou `70B` quantifié, `illustratif`) afin de ne pas favoriser artificiellement les sondes internes.
- **Phase 1 — Porte de qualification + Expérience E1 (Go/No-Go) (`illustratif`).**
  - Volume : `600` trajectoires par famille de modèle (`200` sabotées en Régime A, `400` témoins H1–H4), `~30` actions par trajectoire, `~15 000` tokens cumulés par trajectoire (`~9 millions` de tokens par modèle).
  - Extraction d'activations : uniquement aux positions de décision (fin de raisonnement / début d'appel d'outil) en BF16/FP16 pour limiter le stockage à `~20–50 Go` par modèle (`illustratif`).
  - Calcul : `1 × GPU 80 Go` (type A100 ou H100) pendant `20 à 40 heures` par modèle (génération + passe d'extraction + sondes + évaluation du juge textuel), plus CPU standard pour le bac à sable Python/SQL et les vérifications mécaniques M1–M3 (`~5 à 10 h` CPU).
  - Coût cloud estimé (Phase 1, 2 modèles) : `~120 à 350 USD` (sur base `2–4 USD/h` GPU `80 Go`, `illustratif`). Ce budget restreint tranche la poursuite ou l'arrêt avant tout entraînement RL.
- **Phase 2 — Expériences E2, E3 et E4 (uniquement si E1 franchit le seuil Go) (`illustratif`).**
  - E2 (ablations causales et patching sur `~300` trajectoires × `8` configurations) : `~30 à 60 h` GPU `80 Go`.
  - E3 et E4 (fine-tuning LoRA SFT + RL léger type GRPO/PPO contre juge auditeur pour Saboteur-SFT, Saboteur-RL, Honnête-RL apparié H5, et Régime B compilé, sur `2` familles `7B–9B`) : `~150 à 300 h` GPU `80 Go` (ex. `4 × GPU 80 Go` pendant `2 à 3 jours`), stockage `~100 à 250 Go`.
  - Coût cloud estimé (Phase 2 complète) : `~450 à 1 400 USD` (`illustratif`).
- **Coût global plafonné Phase 1 + Phase 2 (`illustratif`).** `~600 à 1 750 USD` (`illustratif`) pour trancher l'ensemble des quatre duels $H_A$ contre $H_B$ sur deux familles de modèles ouverts, avec un point d'arrêt précoce sous `350 USD` (`illustratif`) si E1 échoue.

FIN-DE-CELLULE