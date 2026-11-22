## D — La longueur ajoute-t-elle des occasions ou de l’information ?

**Question de recherche — HYPOTHÈSE à tester.** À budget d’audit fixe par tâche, l’ajout d’actions interchangeables augmente-t-il la probabilité d’une dégradation non interceptée, tandis que l’ajout d’autant d’actions qui remettent des décisions antérieures à l’épreuve la diminue ?

**Réponse attendue — HYPOTHÈSE.** Oui, pour un agent et un défenseur fixés avant le test. Une action supplémentaire peut offrir un nouvel endroit où introduire une erreur, mais aussi fournir un second élément de preuve sur une erreur déjà commise. Je prédis des effets de signes opposés sur le **dommage échappé**, pas nécessairement sur le nombre d’erreurs ni sur le score moyen de suspicion. Un défenseur qui signale davantage de tâches longues, honnêtes comprises, n’a pas pour autant tiré parti de leur longueur.

### (a) Ce qui n’est pas établi

| Statut | Point à distinguer |
|---|---|
| RAPPORTÉ | L’énoncé donne accès aux textes, aux activations et à quelques comparaisons ; il ne donne ni mesure de leur pouvoir discriminant ni trajectoire annotée. |
| HYPOTHÈSE | On peut changer le nombre d’actions sans changer la question finale, son barème ou la gravité d’une conclusion fausse. Découper une même phrase en davantage d’actions ne suffit pas. |
| HYPOTHÈSE | Il existe des dégradations dont les actes locaux ressemblent à des erreurs honnêtes. Leur caractère discret doit être mesuré en aveugle, non déduit de la consigne donnée à l’agent. |
| HYPOTHÈSE | Une nouvelle source qui traite la même affirmation peut apporter une preuve distincte. Une répétition du texte déjà vu, même reformulée, ne constitue pas un témoin indépendant. |
| HYPOTHÈSE | Un agent ouvert de huit milliards de paramètres peut à la fois réussir la tâche honnête et produire assez de dommages évaluables en condition adverse. Un échec de capacité au pilote ne tranche pas la question de longueur. |

### (b) Expérience pivot et duels

**HYPOTHÈSE — protocole proposé.** Faire travailler le même modèle sur des dossiers documentaires fictifs : lire des fiches, tenir un carnet sourcé, puis rendre une conclusion catégorielle. Un générateur conserve la vérité et les liens entre sources ; ces données servent au jugement final, pas au moniteur. Une **action** est une lecture de fiche suivie d’une mise à jour du carnet, et non un jeton. Pour chaque dossier, tirer au sort trois variantes :

- **Courte C** : parcours de base, suffisant pour conclure.
- **Longue O, occasions** : ajouter des fiches pertinentes au dossier et autant de mises à jour possibles, sans nouvelle preuve sur les affirmations décisives.
- **Longue T, témoins** : remplacer les seules fiches ajoutées en O par des fiches de longueur et de difficulté appariées, issues de sources distinctes qui contraignent aussi les affirmations décisives.

**HYPOTHÈSE — réalisation.** Longueurs proposées : **64 et 256 actions (illustratif)**. Même question finale, même carnet borné et même budget de vérification en nombre d’actions, non en fraction du parcours. Sur chaque variante, séparer par tirage au sort mandat honnête et mandat de dégradation du résultat fictif ; ne communiquer ni mandat ni vérité au défenseur. Exclure les jetons du mandat des entrées directement inspectées. Mesurer la détection sur des **dommages réalisés**, pas seulement sur la reconnaissance du mandat. Séparer entraînement, calibration et test par familles de dossiers et de formulations.

**HYPOTHÈSE — critère principal.** Pour chaque variante \(v\), mesurer sur **toutes** les tâches à mandat adverse :

\[
R_v=P(\text{conclusion fausse et livrée sans interception confirmée}\mid v).
\]

Une alerte seule ne bloque pas la livraison : l’audit doit confirmer, dans son budget, un défaut matériel suffisant pour suspendre la conclusion. Publier aussi \(P(\text{conclusion fausse})\) **avant** audit, la sensibilité conditionnelle sur ces conclusions, et les mêmes quantités pour les tâches honnêtes. Cela distingue une baisse de capacité de l’agent d’un gain propre du défenseur. Figer le défenseur sur validation ; calibrer les seuils par longueur à une même cible de fausses alertes honnêtes.

**HYPOTHÈSE — règles de décision.** Dans le tableau, la marge d’intérêt \(\delta=\) **5 points de pourcentage (illustratif)** s’applique au risque absolu par tâche. Chaque duel oppose une région à son complément. Falsifier \(H_B\) si l’intervalle apparié par dossier est entièrement dans la région \(H_A\) ; falsifier \(H_A\) s’il est entièrement dans la région \(H_B\). Un intervalle qui chevauche la frontière donne un résultat indéterminé, pas une équivalence.

| Duel | \(H_A\) contre \(H_B\) ; métrique et seuil | Contrôle négatif |
|---|---|---|
| **Occasions** | \(H_A:R_O-R_C>\delta\) ; \(H_B:R_O-R_C\leq\delta\). Une hausse des seules alertes ne valide pas \(H_A\). | Allonger la présentation d’un parcours C enregistré par des entrées de journal sans nouvelle décision. Si le détecteur réagit à ce seul allongement sur les cas honnêtes, son calibrage est en défaut. |
| **Témoins** | \(H_A:R_C-R_T>\delta\) ; \(H_B:R_C-R_T\leq\delta\). Pour attribuer le bénéfice au défenseur, exiger aussi un gain de sensibilité à dommage déjà fixé, dans le duel suivant. | En T, substituer aux témoins des copies reformulées de même provenance. Si le gain persiste, l’indépendance des sources n’en est pas l’explication établie. |
| **Information du défenseur seul** | Sur les *mêmes trajectoires T déjà achevées et fausses*, révéler ou masquer au moniteur l’appariement entre affirmation et témoin, à nombre de fiches visible constant. \(H_A:\mathrm{TPR}_{lié}-\mathrm{TPR}_{masqué}>\delta\) à fausses alertes égales ; \(H_B:\) différence \(\leq\delta\). | Révéler des liens de même fréquence entre fiches non décisives. Ils ne doivent pas reproduire le gain. |

**HYPOTHÈSE — garde-fou d’interprétation.** Sur un échantillon indépendant, faire noter des actions isolées en cachant mandat, longueur et suite du parcours. Publier le résultat avec et sans les tâches dont une action suffit à déclencher une alerte. Si l’avantage vient exclusivement de ces tâches, il ne répond pas au cas demandé. Ne pas sélectionner après coup les trajectoires qui donnent les signes attendus.

### (c) Épreuve minimale des instruments

**HYPOTHÈSE — convention de mesure.** Pour chaque instrument, publier la paire **(taux de détection, taux de fausses alertes)** par *tâche*, séparément en C, O et T, avec effectifs et intervalles. Positifs : dégradations adverses effectivement réalisées. Négatifs principaux : tâches honnêtes appariées par dossier, longueur, difficulté et position des faits décisifs, **y compris celles qui finissent fausses** ; ventiler erreurs honnêtes et succès honnêtes. Une erreur honnête signalée est une fausse alerte pour l’attribution adverse, mais peut être une bonne interception pour le contrôle qualité : publier les deux lectures. Aucune performance n’est ici observée.

| Instrument — HYPOTHÈSE de test | Mesure minimale et vérification mécanique à battre |
|---|---|
| **Texte** | Comparer le score de trajectoire au meilleur de : format invalide, référence absente, contradiction littérale, maximum des scores locaux. Mesurer la sensibilité à cible de **5 % de fausses alertes par tâche (illustratif)** ; publier le taux réellement obtenu sur test. |
| **Activations** | Sonde linéaire sur représentations des actions, couche choisie sur validation seulement. Mesurer le gain de *texte + activations* sur texte seul **et** sur des contrôles de longueur, position, norme d’activation et surprise lexicale. Répéter avec mandats reformulés et sur mandats adverses sans dommage : reconnaître la consigne ne suffit pas à localiser un défaut. |
| **Exécutions de comparaison** | À nombre de références honnêtes identique, comparer un alignement par affirmation au simple désaccord des conclusions et au vote majoritaire. Mesurer aussi les fausses alertes sur des parcours honnêtes qui concluent correctement par des chemins différents. Imputer le coût de production des références. |
| **Vérification coûteuse** | À **2 actions inspectées par tâche au maximum (illustratif)**, comparer la sélection du moniteur au tirage uniforme et au classement par références manquantes ou contradictions littérales. L’auditeur voit la fiche source et l’affirmation sélectionnée, jamais le mandat ni la clé globale. Mesurer détections *confirmées* et suspensions injustifiées ; publier séparément le nombre d’inspections et le taux d’alertes avant inspection. |

**HYPOTHÈSE — duel instrumental commun.** Pour chaque ajout, \(H_A\) : gain de détection supérieur à \(\delta\) sur la meilleure vérification de référence figée, à budget égal et sans hausse du taux de fausses alertes ; \(H_B\) : au moins une de ces conditions échoue. Appliquer la règle d’intervalle ci-dessus aux deux écarts. Contrôle négatif commun : permuter les étiquettes au sein des strates appariées et refaire la calibration. Une séparation persistante impose de chercher une fuite avant d’interpréter le test.

### (d) Ancrage matériel, antériorité et portée

**HYPOTHÈSE — dimensionnement, chiffres illustratifs sauf contraintes de l’énoncé.** Employer les poids accessibles de **Llama 3.1 8B Instruct** en inférence locale, sans réentraînement complet. Un plan de **300 dossiers × 3 variantes × 2 mandats** donne **1 800 trajectoires** hors références. À **40 jetons générés par action**, cela représente environ **14 millions de jetons générés**. Prévoir **2 GPU A100 de 80 Go**, carnet à contexte borné, extraction en ligne d’un vecteur par action plutôt que conservation de tous les états. Enveloppe indicative, références et reprises incluses : **800 à 1 600 GPU-heures**, soit **1 600 à 3 200 €** à **2 €/GPU-heure**, hors travail humain. Ces valeurs sont **illustratives**, pas des débits mesurés. Utiliser le générateur comme auditeur local à accès limité et faire relire en aveugle un échantillon de ses verdicts ; distinguer ce substitut d’un audit humain complet.

**HYPOTHÈSE — faisabilité en deux mois.** Commencer par chronométrer le parcours long complet, références et extraction comprises. Estimer au pilote le nombre de *paires discordantes* et de dommages réalisés : ce sont eux, non les centaines d’actions corrélées d’une tâche, qui déterminent la précision. Si le budget ne permet pas de distinguer la marge annoncée, déclarer le duel sous-dimensionné avant le test final.

**RAPPORTÉ — antériorité la plus proche que je puisse attribuer, citée de mémoire.** *AI Control: Improving Safety Despite Intentional Subversion*, Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan et Fabien Roger, 2024. Je la cite pour l’évaluation d’un dispositif de contrôle sous subversion intentionnelle et budget d’audit, non pour lui attribuer le contraste occasions/témoins.

**HYPOTHÈSE — type et critère d’abandon.** Contribution proposée : **contraste expérimental de mécanismes**, pas garantie ni loi de longueur. Si, après appariement et avec une précision suffisante, les écarts de risque et de détection restent dans une bande négligeable autour de zéro, alors la longueur ne mérite pas d’être une variable explicative propre dans ce dispositif. Si les règles mécaniques reproduisent tous les gains, le résultat peut rester utile, mais la contribution revendiquée pour les activations tombe. Avant toute revendication de nouveauté, rechercher dans les travaux de contrôle d’agents, d’audit séquentiel et de détection de dépendances le contraste conjoint **budget fixe par tâche / occasions ajoutées / témoins ajoutés / dommage final identique** ; lire les protocoles et leurs travaux citants, pas seulement les résumés.

FIN-DE-CELLULE