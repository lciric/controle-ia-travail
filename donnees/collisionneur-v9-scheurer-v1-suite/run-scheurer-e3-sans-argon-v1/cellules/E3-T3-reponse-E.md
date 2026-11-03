# E — Réponse aux critiques : une frontière conditionnelle, non une mesure d’intention

**RAPPORTÉ — pièces absentes :** les critiques B et C ne sont pas fournies ; aucun contenu ne leur est attribué.

**Convention :** les corrections, expériences et interprétations proposées ci-dessous sont **HYPOTHÈSE**, non des résultats. Tous leurs nombres sont **supposés, illustratifs**, y compris les calculs de budget. Les constats documentaires conservent leur statut **RAPPORTÉ**. Aucune expérience n’est exécutée ici.

## a) Décisions sur les critiques visant E

### Critiques de A

| Critique | Décision et correction |
|---|---|
| **E1 — Accumulation des fausses alertes** | **Acceptée quant à l’ambiguïté ; rejetée comme identité générale.** La formule donnée suppose des alarmes par décision et une structure d’indépendance. E-A utilisera désormais **un score de trajectoire entière**, calibré séparément par longueur. La frontière dépendra explicitement de cette procédure ; elle ne sera pas présentée comme une propriété intrinsèque du modèle. |
| **E2 — Placement et densité** | **Acceptée.** Condition principale : une anomalie par épisode positif, position tirée uniformément parmi les positions admissibles. Les conditions à densité constante seront distinctes, jamais agrégées à cette mesure. |
| **E3 — Granularité sans ancrage humain** | **Acceptée pour la portée ; rejetée comme invalidation.** L’unité sera une transition d’état définie par une grammaire versionnée. L’absence d’ancrage humain interdit une comparaison directe avec l’horizon METR, pas une comparaison interne entre moniteurs. |
| **E4 — Raisonnement ordinaire rebaptisé** | **Transformée en test.** Ajouter une tâche appariée de reconstruction d’état sans anomalie. Une surveillance reposant sur du raisonnement reste une tâche de surveillance ; en revanche, je retire toute prétention à mesurer une faculté spécifiquement liée au désalignement. |
| **E5 — Information inaccessible** | **Acceptée.** Un oracle limité au journal doit pouvoir identifier l’étiquette. L’oracle privilégié seul ne suffit plus. Les cas ambigus sont exclus du corpus principal avant notation. |
| **E6 — Grille grossière et censure** | **Acceptée.** Une phase de développement choisit une grille plus dense ; cette grille est ensuite gelée et commune. Pas de frontière ponctuelle obtenue uniquement par interpolation logistique. |
| **E7 — Minimum de budget optimiste** | **Acceptée.** Grille identique entre modèles ; sélection et certification sur tâches disjointes ; intervalles simultanés sur les budgets. |
| **E8 — Confinement comme transformation du risque** | **Acceptée sous les hypothèses indiquées.** Publier le risque par occasion et la survie par épisode. Si le modèle indépendant suffit, E-C sera présenté comme sa traduction opérationnelle, non comme une loi supplémentaire. |
| **E9 — Fenêtre de contexte** | **Acceptée.** Mesure principale dans l’intersection des contextes utilisables, avec sérialisation commune. Un protocole à fenêtres identiques sera une condition distincte, pas un changement silencieux d’instrument. |
| **E10 — Absence d’effet minimal** | **Acceptée.** Les duels porteront sur un facteur minimal pertinent, fixé avant collecte, et non seulement sur le signe. |
| **E11 — Identification calendaire** | **Acceptée.** Audit préalable du rang de la matrice et de la variation temporelle résiduelle. Sans contrastes intra-famille à taille comparable, aucune pente ajustée ne sera publiée. |

**Conditions probabilistes de A — acceptées comme alertes, avec réserves.** Le pilote initial ne pouvait pas certifier convenablement les contraintes simultanées. Je retire cette ambition. En revanche :

- une corrélation positive résumée par un coefficient ne suffit pas, à elle seule, à établir l’inégalité proposée pour la probabilité d’au moins une alarme ;
- une classe de censure commune implique une perte d’identification, pas une variance véritablement nulle des horizons ;
- le biais du minimum est un risque de sélection à mesurer, pas une inégalité universelle sans hypothèses sur les courbes et le bruit ;
- **calcul illustratif correctif :** à un risque par occasion de \(10^{-3}\), **1 000** occasions donnent un dommage attendu ; **3 000** en donnent trois.

**Contrôles de A.** J’accepte les épisodes honnêtes, l’oracle à journal seul, les scores aléatoires, les répétitions de checkpoints, le contrôle de contexte, la tâche d’état, la certification indépendante des budgets et les permutations conditionnelles. Je transforme les contrôles de localité et de position en tests : des taux égaux ne prouvent pas l’absence de suivi d’état ; un effet de récence ne rend pas automatiquement l’horizon inexistant, mais restreint son interprétation.

**Duel de calibration de A — transformé.** La concordance des rangs entre deux calibrations ne démontrerait pas une indépendance vis-à-vis de la calibration. Je testerai plutôt si la différence entre leurs pentes temporelles reste sous une tolérance préenregistrée. Ce sera un test de robustesse, non une validation ontologique de « l’horizon ».

### Critiques de D

| Critique | Décision et correction |
|---|---|
| **Géométrie du générateur** | **Acceptée.** Réserver des familles de tâches et un générateur indépendant. La généralisation sera testée séparément de la performance sur graines nouvelles. |
| **Fausses alertes dépendant de la longueur** | **Acceptée.** Le calibrateur conditionnel à la longueur fait désormais partie de la définition publiée de l’instrument. |
| **Maximum sans monotonie** | **Acceptée.** Employer une frontière de préfixe : toutes les longueurs jusqu’à la frontière doivent satisfaire les contraintes. Publier néanmoins les courbes complètes ; une forte non-monotonie interdit l’interprétation en horizon lisse. |
| **Minimum de budget** | **Acceptée**, avec certification indépendante comme ci-dessus. |
| **Confinement algébrique** | **Acceptée conditionnellement**, comme E8. |
| **Régression non identifiée et permutations** | **Acceptée.** Pentes par famille, audit de colinéarité et permutations seulement lorsque l’échangeabilité est défendable. Le moniteur figé ne contrôle que le pipeline. |
| **Pilote trop petit** | **Acceptée.** Le nouveau pilote vise d’abord la validité et la résolution de l’instrument, pas une tendance calendaire. |

**Conditions et contrôles de D.** J’accepte les contrôles à étiquettes factices, les ensembles réservés, la longueur sans dilution, la séparation sélection/certification, les flux honnêtes et les bornes « tout autoriser/tout bloquer ». Une précision : un ensemble de budgets admissibles non monotone peut avoir un minimum unique ; c’est l’interprétation comme franchissement régulier qui échoue. Un risque observé nul ne justifie jamais d’annoncer un horizon infini.

## b) Expériences corrigées

### Instrument commun

**HYPOTHÈSE — protocole.**

- Séparer par **familles de tâches** le développement, la calibration et la certification. Les paires restent dans le même découpage.
- Produire des journaux appariés en longueur, opérations et présentation. L’oracle privilégié établit l’état réel ; l’oracle à journal seul établit l’identifiabilité informationnelle.
- Noter une trajectoire entière. Rapporter détection, fausses alertes et refus séparément. La performance opérationnelle inclut les refus comme échecs de détection, sans être renommée « capacité pure ».
- Calibrer les seuils sur des épisodes honnêtes entiers à chaque longueur ; les figer avant certification.
- Fixer une anomalie par épisode positif ; mesurer séparément les effets de position, de localité et de dépendance d’état.
- Pour E-A, définir \(H_m\) comme la plus grande longueur dont **tout le préfixe de grille** respecte détection et fausses alertes. Distinguer frontière estimée et borne certifiée ; conserver la censure.
- Pour E-B, comparer les budgets effectivement consommés. Une tendance en opérations sera une tendance d’**efficacité de calcul**, non de compétence par tentative.
- Pour E-C, fixer fréquence et gravité des propositions exogènes ; mesurer dommage et utilité sur épisodes entiers, sans multiplier artificiellement les observations par le nombre d’actions.

### Duels préenregistrés

Chaque ligne oppose deux hypothèses exclusives et exhaustives. Une décision exige un intervalle entièrement d’un côté du seuil ; sinon, l’expérience reste **non concluante**, sans falsification revendiquée.

| Expérience | \(H_A\) | \(H_B\) | Ce que les issues discriminantes falsifient |
|---|---|---|---|
| **Validité transférable de E-A** | Sur générateur réservé, avantage de détection du moniteur sur les baselines de style/localité \(>\delta\), à risque d’alerte fixé | Avantage \(\leq\delta\) | A réfute l’absence d’avantage pertinent ; B réfute la justification de poursuivre cet instrument neuronal. |
| **Robustesse à la calibration** | \(|\beta_{\mathrm{entier}}-\beta_{\mathrm{décision}}|<\eta\) | Différence \(\geq\eta\) | A réfute une sensibilité supérieure à la tolérance ; B réfute la transportabilité entre ces deux instruments. |
| **E-A, tendance** | \(\beta_H>\log(1{,}01)\) par mois | \(\beta_H\leq\log(1{,}01)\) | A réfute l’absence de croissance minimale ; B réfute la croissance minimale postulée. |
| **E-B, tendance** | \(\beta_B<\log(0{,}99)\) par mois | \(\beta_B\geq\log(0{,}99)\) | A réfute l’absence d’économie minimale ; B réfute cette économie. |
| **E-C, tendance** | \(\beta_K>\log(1{,}01)\) par mois | \(\beta_K\leq\log(1{,}01)\) | Même lecture que E-A, conditionnelle au contrôleur et au flux fixés. |

**HYPOTHÈSE — seuils illustratifs :** \(\delta=10\) points de détection ; \(\eta=\log(1{,}01)\) par mois. Leur justification opérationnelle et la puissance correspondante doivent être arrêtées avant certification.

La comparaison avec la reconstruction d’état produira deux estimands : pente brute de surveillance et pente conditionnelle à cette capacité. Une disparition de la seconde réfuterait une contribution temporelle **résiduelle**, pas l’utilité opérationnelle de la première.

## c) Réponse à l’arbitre — une page

### Ce qui est établi dans les pièces, sans vérification nouvelle

**RAPPORTÉ :** Apollo décrit une surveillance de trajectoires entières — pièce Scheurer, §1.3. Les performances de surveillance peuvent dépendre du moniteur, de la provenance des exemples et de la présence d’injections — même pièce, §3.3–3.4. Ces constats motivent un instrument conditionnel ; ils n’établissent aucune pente temporelle pour E.

**RAPPORTÉ :** les **sept** tailles Qwen2.5 sont associées à une même publication du **19 septembre 2024** — pièce Scheurer, §2.2. Elles permettent un pilote transversal, pas une tendance mensuelle.

### Ce qui ne l’est pas

**HYPOTHÈSE :** une frontière de surveillance mesurable, transférable et approximativement multiplicative existe. Sa monotonie, son indépendance relative au générateur et la disponibilité d’un panel longitudinal comparable restent à tester. Une anomalie plantée ne mesure ni une intention ni une propension spontanée au désalignement.

### Trois tendances candidates maintenues

| Candidate | Grandeur et échelle communes | Énoncé visé, **supposé, illustratif** |
|---|---|---|
| **E-A — priorité** | Longueur certifiable à détection **80 %**, fausses alertes **5 %**, sur transitions versionnées et corpus commun | « Sur cet instrument, l’horizon croît de **+3 % par mois**, facteur **1,03**. » |
| **E-B** | Opérations d’inférence minimales certifiées, longueur et critères fixes | « Le calcul requis diminue de **−4 % par mois**, facteur **0,96**. » |
| **E-C** | Occasions contrôlables sous dommage d’épisode **5 %** et utilité honnête **90 %** | « L’horizon de confinement croît de **+2 % par mois**, facteur **1,02**. » |

Ces instruments évitent d’exiger une malveillance spontanée : les événements sont exogènes et vérifiables. Leurs menaces principales sont respectivement le style du générateur, la sélection du budget et l’accumulation du risque ; les contrôles correspondants sont le transfert réservé, la certification indépendante et la mesure par épisodes entiers.

**HYPOTHÈSE — panel :** cible de **douze checkpoints sur vingt-quatre mois**, avec répétitions intra-famille à tailles comparables. **Les noms et dates nécessaires ne sont pas fournis : ce panel n’est pas encore constitué.**

Ajuster les réponses par longueur ou budget en conservant leur incertitude et leur censure, puis estimer les pentes temporelles par famille. Rapporter \(e^\beta\) et des intervalles simultanés à **95 %**, avec rééchantillonnage des unités indépendantes pertinentes et analyses de sensibilité. Des pentes familiales opposées interdisent un facteur universel. La date reste une association descriptive, non une cause identifiée.

### Première expérience à faire

**HYPOTHÈSE — pilote E-A :** deux tailles Qwen2.5 à sélectionner selon mémoire disponible ; longueurs **8, 16, 32 et 64** transitions. Par longueur et modèle : **300** épisodes honnêtes de calibration, puis **600** honnêtes et **300** positifs de certification.

**Calcul illustratif :** \(2\times4\times(300+600+300)=9\,600\) notations principales. Les contrôles et répétitions s’ajoutent et doivent être budgétés avant lancement.

**HYPOTHÈSE — enveloppe illustrative :** plafond de **300 heures-GPU**, à **2 €/heure**, soit **600 € — calcul illustratif**, hors travail humain. Un chronométrage préalable déterminera si cette enveloppe suffit ; aucun débit n’est présumé.

Le premier duel est celui de **validité transférable**, pas celui de la date. Pilote non concluant si les intervalles ne résolvent pas l’avantage minimal, si les frontières restent censurées, si l’information du journal est insuffisante ou si le budget empêche la certification prévue.

### Échec du plan
Pas de contrastes temporels comparables : aucune tendance calendaire.  
Pas d’avantage transférable au-delà des artefacts : abandon de cet instrument.  
Frontières non résolues ou fortement non monotones : publier les courbes, renoncer au facteur mensuel unique.

FIN-DE-CELLULE