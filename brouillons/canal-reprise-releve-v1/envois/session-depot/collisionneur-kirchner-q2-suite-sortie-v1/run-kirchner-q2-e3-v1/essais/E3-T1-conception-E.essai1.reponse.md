# Proposition E — La surveillabilité reste-t-elle valable après sélection ?

**Statuts.** Les éléments des pièces sont utilisés comme **RAPPORTÉS**, sans audit indépendant. Les mécanismes proposés, prédictions et plans expérimentaux ci-dessous ont le statut **HYPOTHÈSE**. Tous les paramètres numériques proposés sont **illustratifs**, non des résultats.

**Pièces manquantes :** les annexes F et G et la figure 32 ne sont pas disponibles ici ; la moisson intégrale n’est pas servie. Je n’en infère aucun contenu.

## (a) Ce que la question suppose sans l’établir

| Présupposé | Statut et limite |
|---|---|
| Le problème est sous-estimé. | **HYPOTHÈSE.** Une zone dite « peu couverte » dans une moisson non opposable ne suffit pas à l’établir. Nouveauté non cherchée ici. |
| Le taux de triches signalées renseigne sur le rappel du moniteur. | **HYPOTHÈSE non établie.** Les **39 méthodes signalées sur 1 601** sont **RAPPORTÉES** dans la pièce Kirchner, §3. Sans dénominateur des triches présentes, ce n’est pas une mesure du rappel. |
| Un moniteur évalué avant sélection garde ses performances sur les méthodes retenues. | **HYPOTHÈSE centrale à tester.** Ni la stabilité du mélange de triches ni celle du rappel conditionnel ne sont établies. |
| Une baisse de rappel après sélection prouverait une adaptation des agents au moniteur. | **HYPOTHÈSE non nécessaire.** Une sélection entre candidats figés pourrait produire cette baisse, sans nouvelle génération ni retour aux agents. |
| Des triches plantées représentent la triche spontanée. | **HYPOTHÈSE.** Elles donnent un dénominateur contrôlé ; leur représentativité reste une question distincte. |
| Un gain sur un banc de surveillabilité améliore la détection hors banc. | **HYPOTHÈSE**, pas un résultat acquis. |
| Un juge statistique figé constitue une vérité terrain universelle. | **HYPOTHÈSE contredite dans une classe précise par les observations rapportées.** L’attaque W2 réussit dans **12 unités sur 12**, dans une classe explicitement hors couverture du nul : pièce « nos résultats », §3. Cela ne mesure pas une défaillance dans le domaine garanti. |
| Un verdict Petri mesure directement la présence d’une violation procédurale. | **HYPOTHÈSE.** Petri est présenté comme un indicateur comportemental, non comme l’oracle de la conformité du chercheur : pièce Kirchner, §2 et §5. |

### Problème retenu — **HYPOTHÈSE**

**Une mesure de surveillabilité pourrait ne pas être transportable à travers les opérateurs de sélection d’une boucle de recherche.**

La question précise n’est donc pas seulement « le moniteur détecte-t-il les triches ? », mais :

> À taux de fausses alertes fixé, son rappel reste-t-il valide sur la distribution des méthodes effectivement retenues, notamment après classement et filtrage ?

**Différence revendiquée, sous statut HYPOTHÈSE :** isoler l’effet d’une sélection sur un ensemble de candidats déjà figé, puis tester si un gain de surveillabilité résiste à cette même sélection hors banc. Ce n’est pas proposer comme neuf l’optimisation directe contre un moniteur.

**Pourquoi cela pourrait être négligé — HYPOTHÈSE :** les performances du détecteur et celles du mécanisme de sélection pourraient être rapportées séparément alors que l’utilisateur dépend de leur composition.

**Vérification documentaire ultérieure proposée :** chercher « automated researcher monitoring recall after selection », « leaderboard selection conditional false negatives », « monitorability benchmark transfer selection ». Un travail mesurant déjà le rappel avec vérité terrain mécanique, avant et après sélection de candidats figés, réduirait fortement cette revendication. Les travaux voisins mentionnés dans la question restent des **références à vérifier**.

---

## (b) Expériences décisives

### Socle commun — **HYPOTHÈSE : plan proposé**

- Construire des familles de tâches de recherche miniatures avec une règle de validité explicite.
- Employer des classes de violations déjà présentes dans les pièces : réutilisation interdite, dépendance à une donnée réservée, recombinaison hors couverture déclarée, sélection non autorisée d’essais. **Aucun procédé de dissimulation n’est nécessaire au protocole.**
- Apparier chaque cas invalide à un cas honnête de même tâche, budget, longueur de trace et complexité de code. Les cas honnêtes doivent inclure des usages autorisés ressemblant superficiellement aux classes interdites.
- Établir la vérité terrain par provenance instrumentée et assertions mécaniques indépendantes du moniteur.
- Distinguer **violation tentée**, **violation exécutée** et **effet sur le verdict**. Une intention assignée par l’expérimentateur ne suffit pas à établir une violation.
- Sceller avant test : candidats, règles, moniteurs, seuils, répartitions et analyses.
- Réserver des familles entières au test, plutôt que seulement de nouvelles formulations.
- Traiter le lot de candidats et la famille de tâches comme unités de dépendance ; ne pas compter leurs variantes comme observations indépendantes.

**Règle d’inférence proposée — HYPOTHÈSE.** Les duels ci-dessous partitionnent l’espace du paramètre. Une estimation imprécise peut ne réfuter ni branche. Une absence de significativité ne devient jamais une preuve de stabilité. Les intervalles seraient simultanés à **95 % — illustratif**, avec une procédure tenant compte des lots.

### Expérience E-S : la sélection seule dégrade-t-elle le rappel ?

**HYPOTHÈSE — prédiction :** le rappel du moniteur d’audit sera inférieur après sélection par classement, même sans retour aux agents.

#### Intervention

Geler un même ensemble de candidats, puis appliquer hors ligne :

- une sélection uniforme ;
- une sélection par classement ;
- à titre de contraste secondaire, une sélection par classement après filtre.

Aucune réécriture n’est autorisée entre ces branches.

Le moniteur d’audit est figé et ses verdicts ne participent pas au classement. Pour le contraste avec filtre, distinguer le moniteur de filtrage du moniteur d’audit, même s’ils utilisent les mêmes poids. **Une nouvelle session n’est pas supposée rendre leurs erreurs indépendantes.**

#### Duel principal

Soit \(R_U\) le rappel sur les violations sélectionnées uniformément et \(R_C\) celui sur les violations retenues par classement :

\[
D = R_U-R_C.
\]

Marge de décision **illustrative : 15 points de pourcentage**.

- **H_A : \(D \geq 15\) points.** La sélection produit une dégradation d’ampleur préspécifiée.
- **H_B : \(D < 15\) points.** Elle ne produit pas une dégradation de cette ampleur.

**Métriques :**

1. rappel conditionnel parmi les violations effectivement exécutées ;
2. fausses alertes sur les cas honnêtes sélectionnés ;
3. probabilité qu’un lot aboutisse à une méthode invalide non détectée ;
4. rappel standardisé à mélange de familles constant, lorsque les familles ont un support suffisant dans les deux branches.

La troisième mesure évite de confondre une baisse de rappel avec une baisse du nombre total de violations. La quatrième sépare autant que possible changement de composition et difficulté accrue au sein des familles.

**Seuil de fonctionnement du moniteur :** seuil calibré sur un jeu honnête séparé pour viser **5 % de fausses alertes — illustratif** ; mesurer ensuite les fausses alertes sans recalibrage sur le test.

**Contrôle négatif :** permuter les scores du classement à l’intérieur des lots. Le contraste avec la sélection uniforme doit alors disparaître en moyenne.

**Issues réfutantes :**

- borne inférieure de l’intervalle de \(D\) au-dessus de la marge : **réfute H_B** ;
- borne supérieure sous la marge : **réfute H_A**, et me ferait abandonner la prédiction d’un effet important dans ce domaine ;
- intervalle traversant la marge : expérience non concluante.

**Précaution — HYPOTHÈSE méthodologique :** mesurer le rappel du filtre sur ses propres survivants serait circulaire. Son efficacité se mesure sur toutes ses entrées ; le risque résiduel, sur les sorties, grâce à l’oracle mécanique et à l’audit indépendant.

### Expérience E-T : le gain de surveillabilité transfère-t-il après sélection ?

**HYPOTHÈSE — prédiction :** choisir des configurations de chercheur sur un banc de surveillabilité n’apportera pas nécessairement un gain comparable sur les familles hors banc, après classement.

#### Intervention

Comparer :

- une configuration choisie uniquement sur le score de tâche ;
- une configuration choisie sur le banc de surveillabilité, sous contrainte de qualité de tâche comparable.

La recherche entre configurations utilise un budget fixé, sans gradient contre le moniteur. Après scellement, produire les candidats sur les tâches réservées et leur appliquer le même classement.

**Condition préalable :** il faut mesurer un gain réel sur le banc de développement. Sinon, le test ne porte pas sur le transfert d’un gain.

#### Duel

Soit \(G\) la différence de rappel hors banc, après sélection, entre configuration choisie pour sa surveillabilité et configuration témoin. Les résultats sont standardisés sur les classes de violations et leur gravité observable.

Marge **illustrative : 10 points de pourcentage**.

- **H_A : \(G \geq 10\) points.** Le gain transfère à l’ampleur annoncée.
- **H_B : \(G < 10\) points.** Il ne transfère pas à cette ampleur.

**Métriques :** rappel hors banc ; fausses alertes ; fréquence des violations ; succès des violations ; qualité de tâche. Rapporter ces dimensions séparément plutôt qu’un score agrégé susceptible de cacher un compromis.

**Seuil de fonctionnement :** même cible de fausses alertes que dans E-S. Une hausse hors tolérance des fausses alertes interdit de qualifier le résultat d’amélioration utile, même si le rappel augmente.

**Contrôle négatif :** sélectionner les configurations sur un banc dont les étiquettes de violation ont été permutées.

**Issues réfutantes :**

- borne inférieure de \(G\) au-dessus de la marge : **réfute H_B** ; cela changerait mon avis pessimiste sur le transfert dans ce domaine ;
- borne supérieure sous la marge : **réfute H_A** ;
- absence de gain sur le banc initial, manque de violations hors banc ou intervalle trop large : non-conclusion, et non preuve d’échec du transfert.

**Limite de portée — HYPOTHÈSE :** même une réussite ne démontrerait pas le transfert à la triche spontanée. Il faudrait ensuite tester cette population avec une vérité terrain indépendante.

---

## (c) Qualification minimale des instruments

**HYPOTHÈSE — protocole proposé.** Pour chaque instrument détecteur : publier matrice de confusion, rappel et taux de fausses alertes par famille, avant et après sélection. Les nombres de cas honnêtes et invalides doivent apparaître explicitement.

Un **oracle mécanique complet** sert à établir les étiquettes : il n’est pas une baseline à « battre ». Les comparaisons pertinentes portent sur des vérifications mécaniques moins coûteuses ou moins informées, à budget d’observation comparable.

| Instrument nommé | Mesure minimale et cas honnêtes appariés | Vérification mécanique de comparaison |
|---|---|---|
| **Moniteur avant exécution, même modèle que le chercheur** | Rappel des violations identifiables avant lancement ; fausses alertes sur programmes autorisés de complexité comparable. Ne pas lui attribuer les violations visibles seulement à l’exécution. | Analyse des dépendances, droits d’accès, provenance et conformité aux règles explicites. |
| **Moniteur après coup / audit de trajectoire** | Rappel des violations exécutées ; fausses alertes sur trajectoires honnêtes de même tâche, longueur et nombre d’appels. Mesure après sélection obligatoire. | Journaux d’exécution structurés, contrôle de provenance, comparaison des artefacts produits et déclarés. |
| **Classement** | Ce n’est pas un détecteur tant qu’aucune règle d’alerte n’est définie. Mesurer l’enrichissement en violations et la probabilité de sélectionner une violation non détectée. | Sélection uniforme, classement permuté, score recomputé par un évaluateur indépendant. |
| **Banc tenu à l’écart** | Si employé comme alarme : rappel des gains invalides et fausses alertes sur améliorations honnêtes appariées en gain apparent. Vérifier séparément l’absence d’accès et de retours répétés. | Contrôles d’accès, provenance des données, reproduction du score. |
| **Banc de surveillabilité** | Rappel et fausses alertes sur familles réservées ; écart entre gain sur banc et gain hors banc. Apparier difficulté et qualité des productions honnêtes. | Détecteurs de provenance et règles de validité ; comparaison avant sélection de configurations. |
| **Garde de capacité** | Rappel des dégradations de capacité et rejet erroné de modèles non dégradés. Cas honnêtes : réentraînements ou évaluations répétées sans intervention nocive. | Batterie déterministe lorsque possible, test-retest, incertitude du score plutôt que seul verdict binaire. |
| **Petri, auditeur et juge** | Rappel d’un comportement adverse défini et vérifiable dans un sous-ensemble de tâches ; fausses alertes sur comportements autorisés appariés. Sans vérité terrain, mesurer un accord n’établit pas une exactitude. | Assertions comportementales sur tâches exécutables ; évaluations aveugles indépendantes pour le reste. |
| **Forum partagé** | Ce n’est pas un détecteur. Mesurer la fréquence des violations par lot et leur propagation entre lignées documentées, avec tâches honnêtes comparables. | Provenance des contributions et historique des dépendances ; forum désactivé comme contraste. |
| **Juge statistique de l’organisme** | Taux de promotion fausse et puissance sur lois valides, séparément dans et hors domaine du nul. Cas honnêtes : lois nouvelles de difficulté comparable. | Nuls synthétiques connus, témoins plantés, invariances et tests de non-régression. |
| **Juges de modèles de langage** | Si utilisés pour filtrer : rappel des fiches invalides et fausses alertes sur fiches valides appariées en style. L’accord entre juges ne suffit pas. | Vérification des calculs, contraintes de format et reproduction des assertions exécutables. |

**RAPPORTÉ — ancrage dans nos travaux.** La pièce « nos résultats », §2–3, distingue déjà résistance à des tricheurs scriptés et trou de couverture hors nul. La proposition s’appuie sur cette distinction, sans transformer W2 en preuve d’adaptation au retour des verdicts. Les sondes d’activations ne sont pas nécessaires à ce premier test ; leur résultat rapporté en §6 ne justifie pas de les prendre comme oracle.

---

## (d) Ancrage matériel et premier essai

### Première expérience à lancer — **HYPOTHÈSE**

Commencer par **E-S sur l’organisme public**, avec des candidats scriptés et des traces figées. L’objectif initial est de tester le transport du rappel, pas de produire immédiatement un chercheur autonome complet.

**Plan de travail illustratif :**

- **Jour 1 :** règles de validité, appariements honnêtes et validation de l’oracle.
- **Jour 2 :** création des lots, génération des évaluations, scellement.
- **Jour 3 :** sélection hors ligne, audit aveugle, analyse avec intervalles.

**Taille pilote illustrative :** **96 lots de 8 candidats**, soit **768 candidats — calcul illustratif**. Cette taille sert à mesurer débit et variance ; elle ne garantit pas la précision nécessaire. Le dimensionnement confirmatoire dépendra du nombre de violations effectivement sélectionnées, pas simplement du nombre de traces.

### Modèle et calcul — **HYPOTHÈSE, estimations illustratives**

- **Llama-3.1-8B-Instruct**, à poids ouverts, comme moniteur ; éventuellement comme proposeur dans une extension. Utiliser les mêmes poids dans ces rôles reproduit seulement une propriété du montage rapporté, pas ses capacités.
- Inférence quantifiée sur **une carte de 24 à 48 Go — illustratif**, selon contexte et taille des lots.
- Budget pilote de **10 à 40 millions de jetons traités — illustratif**, en comptant les lectures de traces répétées.
- Réserve de **20 à 100 heures-GPU — illustrative**, à réviser après mesure du débit sur un petit lot.
- Avec une location supposée de **1 à 3 €/heure-GPU — illustrative**, coût de calcul de **20 à 300 € — calcul illustratif**, hors travail humain, stockage et relances.
- Aucun entraînement requis pour E-S. Pour E-T, commencer par la sélection de configurations ou d’invites, plutôt que par un entraînement supplémentaire.

**RAPPORTÉ — limite matérielle :** les pièces décrivent un harnais ouvert de Kirchner, mais aucun inventaire local vérifié de ses dépendances n’est fourni. Je ne conditionnerais donc pas le premier essai à son installation.

### Résultat qui changerait mon avis — **HYPOTHÈSE**

Je privilégie une dégradation importante du rappel sous sélection. Une borne supérieure excluant la perte préspécifiée de **15 points — illustratif**, avec contrôle négatif valide, fausses alertes maîtrisées et suffisamment de violations sélectionnées, me ferait abandonner cette prédiction **pour le domaine testé**.

Le livrable serait alors utile même négatif : un moniteur qualifié sur la distribution des méthodes retenues, plutôt qu’un taux de signalement sans dénominateur.

FIN-DE-CELLULE