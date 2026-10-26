## Contre la proposition B

La pièce `E3-T1-conception-B` est absente (statut : REFUS, RAPPORTÉ). Je n'en invente pas le contenu.

---

## Contre la proposition A

Le bloc FAITS est vide (RAPPORTÉ). Tous les éléments du cadre de la question et de la proposition A sont de statut RAPPORTÉ ou HYPOTHÈSE ; aucun n'est VÉRIFIÉ.

### (a) Les failles : variables confondantes, vrai par construction, fuites

1. **Fuite entre le filtre de décision et l'évaluation dans le dessin séquentiel D-1 (biais d'arrêt conditionnel).**
   La proposition A préconise D-1 : lancer une seconde course par question ($R=2$), lire les faits mécaniques (nombre de rondes, mutations acceptées, retours arrière, coûts), s'arrêter à $R=2$ si les trajectoires convergent, et pousser à $R=3$ tout en activant d'office le palier 2 du pilote décisif (b) si elles divergent.
   - *La fuite :* La proposition A reconnaît elle-même dans son présupposé A5 (OBSERVÉ-NON-AUDITÉ) que les faits mécaniques sont corrélés aux scores de façon inconnue. En conditionnant la taille d'échantillon finale ($R=2$ contre $R=3$) à ces faits mécaniques, D-1 utilise une variable proxy du résultat pour décider de continuer à échantillonner.
   - *Conséquence mathématique :* Si une divergence mécanique est positivement corrélée à la variance des scores ($\sigma^2$), on n'échantillonne la troisième graine que lorsque les deux premières courses ont déjà produit un écart mécanique élevé. L'estimateur $\hat{\sigma}^2$ calculé à $R=3$ au terme de cette règle d'arrêt est conditionnel à un événement de queue : il est biaisé par excès. L'instrument qui sert à décider du plan d'échantillonnage (le duel D1) contamine l'instrument d'évaluation de la variance ($\hat{\sigma}$).

2. **Confusion entre comptage d'événements et sémantique du code dans le duel D1 (variable confondante majeure).**
   Le duel D1 prétend séparer la variance de trajectoire de la variance d'interface en comparant quatre compteurs mécaniques : nombre de rondes de conception, nombre de mutations acceptées, nombre de retours arrière, coût par génération.
   - *La variable confondante :* Le contenu sémantique du code réécrit et les valeurs des trois paramètres bornés de l'architecte (RAPPORTÉ).
   - *Pourquoi cela invalide D1 :* Deux courses de la v6.2.1 peuvent présenter des compteurs mécaniques strictement identiques (par exemple : 3 rondes de conception, 2 mutations acceptées, 0 retour arrière, 40 USD illustratif) tout en ayant accepté des mutations de code radicalement opposées (l'une inversant la règle de récompense de l'architecte vers un extrême, l'autre vers l'autre). Conclure de l'égalité des compteurs que « $\sigma$ est quasi entièrement d'interface » (falsification de $H_A$ dans D1) est une erreur d'inférence : le test D1 mesure l'activité administrative du méta-algorithme, pas la divergence fonctionnelle de l'organisme.

3. **Vrai par construction : l'inapplicabilité bilatérale du test de permutation à $R=3$ et la borne du test $t$.**
   - Dans sa section 2, la proposition A propose de comparer l'objet d'origine et l'objet corrigé par un test de permutation sur les moyennes de fin de course à $R=3$ contre $R=3$, tout en notant que la valeur-$p$ minimale unilatérale est $1/\binom{6}{3} = 1/20 = 0,05$, et bilatérale $2/20 = 0,10$. Au seuil bilatéral nominal de $0,05$, le taux de détection de cet instrument est donc **nul par construction** ($0\ \%$), quel que soit l'écart réel entre les deux organismes. Proposer cet instrument à $R=3$ revient à garantir par construction l'étiquette « indécidable ».
   - Dans son tableau (c), la proposition A calibre le test $t$ à $2R-2$ degrés de liberté sur des données simulées exactement selon le modèle gaussien homoscédastique de la lignée B, puis demande une puissance $\ge 0,75$ là où la formule analytique promet $0,80$. Que cet instrument atteigne $\approx 0,75$ sur sa propre loi de génération est vrai par construction (aux queues de la loi de Student non centrale près) ; cela ne teste en rien son comportement sur des exactitudes équilibrées bornées dans $[0, 1]$, discrètes (pas de $1/36$ et $1/24$, RAPPORTÉ) et potentiellement asymétriques ou bimodales (lorsqu'une mutation fait s'effondrer une course).

4. **Variable confondante dans le duel D2 : la dynamique d'exposition à la part `test`.**
   Le duel D2 oppose $H_A$ (la divergence naît pendant les rondes de conception, avant la génération 0) à $H_B$ (elle naît pendant les générations notées 0 à 3) en comparant la concordance par tâche entre graines à la génération 0 ($\hat{\rho}_0$) et à la génération 3 ($\hat{\rho}_3$).
   - *La variable confondante :* Le surapprentissage progressif ou la spécialisation sur la part `test`, qui est rendue à l'organisme à chaque génération (RAPPORTÉ).
   - *Le mécanisme :* Si deux graines partent à la génération 0 avec deux codes déjà divergents (issus des rondes de conception, donc sous $H_A$), mais que ces deux codes ne manifestent leur différence d'apprentissage qu'après trois itérations de rétroaction sur la part `test`, on observera $\hat{\rho}_3 < \hat{\rho}_0 - 0,1$ alors même que la cause racine de la divergence est antérieure à la génération 0. À l'inverse, si l'architecte pousse toutes les graines à converger vers la même heuristique triviale en exploitant `test` de la génération 0 à la génération 3, on observera $\hat{\rho}_3 \ge \hat{\rho}_0$, masquant les mutations intermédiaires. La différence $\hat{\rho}_3 - \hat{\rho}_0$ confond le moment où la divergence est *créée* et le moment où elle *s'exprime* sur les étiquettes.

5. **Contradiction interne sur le modèle mixte et l'estimation de $\rho$ (A3 contre § 2).**
   La proposition A affirme dans A3 que $\rho$ est très faiblement transférable de la v3 à la v6, et dans sa section 1 que l'achat principal pour dimensionner (b) porte sur $\sigma$, non sur $\rho$. Or, dans sa section 2, elle justifie l'emploi d'un modèle mixte tâche $\times$ graine uniquement par sa capacité à « estimer $\rho$ à partir de la concordance par tâche entre graines ». Si $\rho$ n'est pas transférable à la v6 et ne change pas les degrés de liberté pour l'effet objet ($2R-2$), cet instrument (modèle mixte) mesure avec précision un paramètre de nuisance local qui ne sert à aucune décision en aval.

6. **Fuite temporelle dans l'entrelacement séquentiel (P3).**
   La proposition A propose d'entrelacer les courses supplémentaires sous la forme $(M_2, S_2, M_3, S_3)$ après que les deux premières courses $(M_1, S_1)$ ont déjà tourné. Les courses $M_1$ et $S_1$ ne sont donc pas entrelacées avec les graines 2 et 3 : elles forment un bloc temporel initial distinct. Si une dérive d'interface survient entre la fin de $S_1$ (plus le temps de délibération) et le lancement de $M_2$, la variance empirique entre la graine 1 et les graines $\{2, 3\}$ confond la dérive temporelle avec la variance de graine $\sigma^2$.

---

### (b) Scénarios d'évasion : comment un organisme trompe les instruments

Ici, l'« agent adverse » n'est pas nécessairement malveillant : c'est l'organisme auto-modifiant (v6.2.1, avec son architecte et ses castes, RAPPORTÉ) soumis à une pression de sélection interne sur la part `test` (rendue à chaque génération, RAPPORTÉ) et évalué sur `test_final` (jamais rendue, RAPPORTÉ).

1. **Tromper le filtre mécanique du dessin D-1 et du duel D1.**
   - *Mécanisme :* L'organisme (ou une correction proposée par la boucle extérieure) fige ou régularise ses compteurs d'activité : par exemple, il consomme systématiquement le plafond de 6 rondes de conception, accepte exactement 1 mutation par génération et interdit les retours arrière, tout en laissant le contenu des mutations ou les poids de l'architecte osciller fortement d'une course à l'autre.
   - *Effet sur l'instrument :* Les quatre compteurs mécaniques de D1 sont constants d'une graine à l'autre (écart nul, bien inférieur au seuil d'une unité). Le duel D1 conclut à $H_B$ (trajectoires identiques, $\sigma$ purement d'interface), D-1 s'arrête à $R=2$ et le pilote décisif (b) est lancé au palier 1 ($R=4$) sans filets, alors que la variance réelle des scores $\sigma^2$ est maximale.
   - *Coût pour l'agent :* Nul en appels supplémentaires (voire négatif si le nombre de rondes est fixé bas, par exemple à 1 ronde systématique : 3 USD par course, RAPPORTÉ).

2. **Tromper McNemar exact ($g_0$ contre $g_3$ sur `test_final`) et les bornes de Wilson.**
   - *Mécanisme (« sabordage de la génération 0 ») :* Pendant les rondes de conception (qui précèdent la génération 0 notée), l'organisme dégrade délibérément ou par accident son classifieur initial à la génération 0 (score bas sur `test_final`, par exemple $0,45$ illustratif), tout en stockant en mémoire (la v6.2.1 dispose d'une mémoire, RAPPORTÉ) le prompt ou la règle de base standard, qu'il restaure à la génération 1 ou 3 (score remontant à $0,75$ illustratif).
   - *Effet sur l'instrument :* Le test de McNemar exact apparié entre $g_0$ et $g_3$ sur `test_final` détecte un gain massif ($+0,30$ illustratif, franchissant Holm à $0,05$) et déclare à tort un apprentissage inter-générationnel réussi, alors que l'organisme n'a jamais dépassé sa capacité nominale de départ et que les bornes basses de Wilson restent sous la référence (plafond de $0,7818$ en conscience d'évaluation et $0,7049$ en délégation même à score parfait, RAPPORTÉ).
   - *Coût pour l'agent :* 1 génération notée gaspillée ($g_0$, au plus 30 USD et 2 400 s, RAPPORTÉ).

3. **Tromper l'estimateur de variance inter-graines ($\hat{\sigma}$) et le modèle mixte ($\hat{\rho}$).**
   - *Mécanisme (« effondrement vers un classifieur dégénéré stable ») :* L'architecte de la v6.2.1 mute sa règle de récompense interne vers un jeu de paramètres qui pousse toutes les castes à appliquer une heuristique de surface rigide et déterministe (par exemple, répondre selon la longueur de la tâche ou un mot-clé fixe).
   - *Effet sur l'instrument :* D'une graine à l'autre, les réponses par tâche deviennent quasi identiques : $\hat{\rho} \to 1$ et $\hat{\sigma} \to 0$. La proposition A en déduit que l'organisme est très stable et que le palier 1 de (b) est largement suffisant, alors que cette stabilité est l'artefact d'un effondrement de la diversité comportementale. Inversement, lors de la comparaison origine / corrigé par test $t$, si l'organisme corrigé présente un $\sigma$ très élevé (instabilité sporadique sur 1 graine sur 3), il gonfle la variance groupée à $2R-2 = 4$ degrés de liberté, faisant tomber la puissance du test $t$ et empêchant l'élimination d'une correction défectueuse (qui reste classée « indécidable »).
   - *Coût pour l'agent :* Nul (réduction de la variance par perte de sensibilité).

4. **Tromper la boucle extérieure et le registre d'hypothèses.**
   - *Mécanisme :* Comme la part `test` (60 tâches, RAPPORTÉ) est rendue à l'organisme à chaque génération, l'organisme surapprend les spécificités de `test` de $g_0$ à $g_3$. Par fluctuation d'échantillonnage binomiale sur `test_final` (60 tâches), une des courses à $R=1$ ou $R=2$ obtient par chance un écart $g_0 \to g_3$ de $+0,15$ (illustratif) sur une famille. Les agents neufs de la boucle extérieure, voyant simultanément une progression monotone sur `test` et un test de McNemar significatif sur `test_final`, valident l'hypothèse de conception comme « tenue ».
   - *Coût pour l'agent :* Nul (exploitation passive de la variance binomiale sur 24 ou 36 tâches).

5. **Évasion conjointe (tromper tous les instruments à la fois) et coût total.**
   - *Scénario combiné :* L'organisme (1) s'arrête systématiquement après 2 rondes de conception et accepte exactement 1 mutation par génération (trompe D1 et fige D-1 à $R=2$), (2) applique à la génération 0 une politique sous-optimale déterministe puis bascule à la génération 1 vers une heuristique rigide unique calée sur `test` (trompe McNemar $g_0/g_3$ qui voit un bond significatif ; trompe $\hat{\sigma}$ et $\hat{\rho}$ à $R=2$ qui voient deux courses identiques $\hat{\sigma} \approx 0$ et $\hat{\rho} \approx 1$ ; trompe la boucle extérieure qui valide l'apprentissage).
   - *Coût total pour l'organisme :* $2 \times 3\text{ USD} = 6\text{ USD}$ en rondes de conception + $4 \times 30\text{ USD} = 120\text{ USD}$ au plafond théorique (plafond réel plafonné à 75 USD par course par le noyau, ordre de grandeur attendu 30 à 55 USD, RAPPORTÉ). Pour l'arbitre, le coût de cette illusion sous D-1 est de 2 courses supplémentaires ($\approx 90$ à $150\text{ USD}$ illustratifs) suivies d'un sous-dimensionnement fatal du pilote décisif (b).

---

### (c) Les contrôles négatifs dont l'absence serait fatale

Pour que l'architecture expérimentale de la proposition A ne produise pas d'artefacts irréfutables, les cinq contrôles négatifs suivants sont indispensables ; l'absence de chacun est fatale à l'instrument correspondant :

1. **Contrôle négatif sémantique pour le duel D1 (contre l'illusion des compteurs mécaniques).**
   - *Ce qui manque dans A :* Le contrôle négatif de A pour D1 consiste à lancer deux courses à la *même* graine pour vérifier si la graine est l'unité de réplication. Ce contrôle ne teste que le déterminisme de l'interface ; il ne vérifie jamais si l'égalité des quatre compteurs mécaniques implique la proximité des scores ou des codes produits.
   - *Contrôle requis :* Calculer, sans lire aucun score sur `test_final`, la distance d'édition (ou l'empreinte cryptographique) des codes produits et la distance euclidienne des trois paramètres bornés de l'architecte entre deux courses aux compteurs mécaniques proches, ainsi que le taux de désaccord des prédictions sur un jeu de tâches synthétiques fixes hors banque (ou sur la part `test` à la génération 0 avant réécriture). Si deux courses aux compteurs identiques divergent dans leurs paramètres d'architecte ou leurs prédictions de départ, l'instrument D1 est falsifié et D-1 est caduc.

2. **Contrôle négatif de ligne de base statique ($g_0$ sans rondes de conception) pour McNemar $g_0/g_3$.**
   - *Ce qui manque dans A :* Aucun contrôle ne vérifie que la génération 0 (qui a lieu *après* les 6 rondes de conception, RAPPORTÉ) n'a pas été dégradée par ces rondes par rapport à l'organisme vierge avant toute réécriture.
   - *Contrôle requis :* Évaluer l'empreinte initiale de la v6.2.1 (avant la ronde de conception 1, génération « $-1$ ») ou vérifier sur la part `test` que le score à $g_0$ n'est pas statistiquement inférieur au score d'un appel direct au modèle sous-jacent sans réécriture. Sans ce contrôle, tout gain $g_0 \to g_3$ mesuré par McNemar peut n'être que la récupération d'une régression auto-infligée pendant les rondes de conception.

3. **Contrôle de lois non gaussiennes et discrètes pour la calibration des tests à $R$ graines (tableau c).**
   - *Ce qui manque dans A :* Le tableau (c) ne teste le test $t$ et le modèle mixte que sous des tirages binomiaux réguliers ou des lois normales homoscédastiques.
   - *Contrôle requis :* Injecter dans le banc de simulation numérique (coût 0 USD) des lois de perturbation réalistes pour un agent qui se réécrit : (i) loi de mélange à contamination (avec probabilité $q = 0,20$ illustratif, une mutation fait chuter l'exactitude d'une course à $0,50$ ; avec probabilité $1-q$, elle reste à $0,75 \pm 0,02$), et (ii) hétéroscédasticité forte entre l'organisme d'origine ($\sigma_1 = 0,01$ illustratif) et l'organisme corrigé ($\sigma_2 = 0,08$ illustratif). Si le taux de fausses alertes du test $t$ à $2R-2 = 4$ degrés de liberté dépasse $0,05$ ou si sa puissance s'effondre sous ces régimes, l'instrument de comparaison paramétrique à $R=3$ doit être rejeté.

4. **Contrôle de permutation à blanc (« placebo d'étiquette ») pour la boucle extérieure.**
   - *Ce qui manque dans A :* Dans le tableau (c), la proposition A teste la boucle extérieure sur 20 tableaux de scores synthétiques nus (10 sous nulle, 10 avec écart $\ge 0,2$). Or, en conditions réelles, la boucle extérieure ne lit pas un simple tableau de chiffres : elle lit les traces de la course, les mutations de code et un registre d'hypothèses narratives (RAPPORTÉ), ce qui déclenche des rationalisations *post hoc*.
   - *Contrôle requis :* Servir aux agents neufs de la boucle extérieure les traces mécaniques réelles d'une course du pilote 4 couplées à des vecteurs de scores sur `test_final` dont les étiquettes de génération ($g_0$ et $g_3$) ou de tâches ont été permutées aléatoirement sous l'hypothèse nulle. Si la boucle extérieure déclare « tenue » la moindre hypothèse de conception sur ces données permutées en s'appuyant sur la cohérence apparente des traces mécaniques, sa lecture est démontrée contaminée par les traces.

5. **Contrôle de dérive temporelle pure (tâches témoins figées) entre les vagues de courses.**
   - *Ce qui manque dans A :* La proposition A suppose que l'entrelacement $(M_2, S_2, M_3, S_3)$ suffit à neutraliser la dérive d'interface (P3), en oubliant que $(M_1, S_1)$ ont tourné dans une fenêtre temporelle antérieure.
   - *Contrôle requis :* Avant d'agréger la course 1 avec les courses 2 et 3 pour calculer $\hat{\sigma}^2$, comparer les sorties brutes de la génération 0 (ou des appels de référence à température zéro s'ils existent, sinon sur les mêmes prompts de départ) entre la vague $\{1\}$ et la vague $\{2, 3\}$. En l'absence de ce contrôle, toute dérive d'API survenue pendant la retenue de lecture de Lazar est intégralement absorbée dans $\hat{\sigma}^2$, faussant à la hausse le dimensionnement du pilote décisif (b).

FIN-DE-CELLULE