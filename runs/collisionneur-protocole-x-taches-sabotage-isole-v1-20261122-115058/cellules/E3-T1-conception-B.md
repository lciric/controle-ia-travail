# Proposition B : Tour III.1, conception ciblée

## 0. État des pièces

- **Bloc FAITS.** Il est identique au bloc QUESTION : même empreinte sha256, même texte. Il ne contient donc aucun fait statué, et je n'en invente aucun.
- **Prémisses de l'énoncé.** Les phrases descriptives de l'énoncé arrivent sans statut : dégradation « exprès » localement défendable, erreur honnête, part relative inconnue. Je les traite comme **HYPOTHÈSE** de travail.
- **Autres propositions.** Le tour se fait à l'aveugle : aucune proposition A, C, D ou E ne m'a été transmise. La règle B1 est donc sans objet ici.
- **Statuts employés.**
  - **RAPPORTÉ** : affirmé dans une publication que je sais attribuer, rapporté de mémoire et non revérifié dans ce tour.
  - **HYPOTHÈSE** : mon raisonnement.
  - Rien n'est VÉRIFIÉ ni OBSERVÉ-NON-AUDITÉ dans ce tour.
  - Tous les chiffres sont **illustratifs**.

## Thèse (réfutable)

L'intention n'est pas mesurable comme état mental. Ce qu'on peut mesurer sans juge, c'est l'**excès dirigé** : la part du dommage qui suit une direction de nuisance *tirée au hasard par l'expérimentateur*. On la compare à la distribution des erreurs du *même* agent, sur les *mêmes* tâches, sans consigne de nuire.

Deux ingrédients rendent cela possible :
1. un **ensemble d'actions admissibles préenregistré**, qui remplace le lecteur humain dans la notion de « défendable » ;
2. la **randomisation de la direction de nuisance**, qui rend l'erreur honnête orthogonale à la nuisance par construction.

Statut : **HYPOTHÈSE**. Les expériences E0 à E3 la réfutent si elle est fausse.

---

## Réponses aux points 1 à 5 : savoir, supposition, changement d'avis

### Point 1 : ce qui existe

| Méthode | Domaine | Ce qu'elle mesure exactement | Ce qu'elle laisse hors mesure | Statut |
|---|---|---|---|---|
| Tests de validité de symptôme en choix forcé (p. ex. Test of Memory Malingering, Tombaugh, 1996) | Neuropsychologie | Un score *significativement sous le hasard* en choix forcé est incompatible avec l'erreur honnête, qui donne au pire le hasard. | Le simulateur qui reste au-dessus du hasard. Les seuils cliniques usuels, situés au-dessus du hasard, reposent sur des normes de groupes, donc sur des taux de fausses alertes empiriques et non sur une impossibilité. | RAPPORTÉ |
| Statistiques d'ajustement personne (*person-fit*) en théorie de réponse aux items | Psychométrie | Les patrons improbables : échecs aux items faciles, réussites aux difficiles. | L'intention : fatigue et inattention produisent les mêmes patrons. Référence précise à vérifier. | RAPPORTÉ |
| p-curve (Simonsohn, Nelson & Simmons, 2014, « P-curve: A key to the file-drawer ») | Méta-science | La forme de la distribution des p significatifs dans un *corpus* d'études. | L'étude individuelle ; la distinction entre manipulation consciente et inconsciente. | RAPPORTÉ |
| Analyse multivers (Steegen, Tuerlinckx, Gelman & Vanpaemel, 2016, « Increasing transparency through a multiverse analysis ») ; courbe de spécification (Simonsohn, Simmons & Nelson, 2020, « Specification curve analysis ») | Statistique appliquée | La position d'un résultat dans l'ensemble des analyses défendables. | L'intention. Ces méthodes ne sont pas conçues comme des détecteurs. | RAPPORTÉ |
| Carlisle, 2017, *Anaesthesia* (distribution des p de base dans des milliers d'essais randomisés) | Intégrité de la recherche | L'écart à l'uniformité attendue sous randomisation. | La séparation entre fabrication, erreur de saisie et erreur de calcul. | RAPPORTÉ |
| van der Weij et al., 2024, « AI Sandbagging: Language Models can Strategically Underperform on Evaluations » ; Greenblatt, Roger, Krasheninnikov & Krueger, 2024, « Stress-Testing Capability Elicitation With Password-Locked Models » | IA, sous-rendement | Une chute de précision *programmatique* sur des questions à réponse connue, quand le sous-rendement est induit par consigne ou par entraînement. | L'intention est fixée par construction, non inférée. Le sous-rendement n'est pas séparé de l'erreur honnête dans un même résultat mixte. Tâches courtes, non agentiques. | RAPPORTÉ (détails à vérifier) |
| Greenblatt, Shlegeris, Sachan & Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » ; Benton et al., 2024, « Sabotage Evaluations for Frontier Models » ; Kutasov et al., 2025, « SHADE-Arena » ; Bhatt et al., 2025, « Ctrl-Z » | IA, contrôle et sabotage | Le succès d'une subversion *instruite*, vérifié par programme quand c'est possible : porte dérobée déclenchée par une entrée de test, tâche secondaire accomplie. | La détection repose le plus souvent sur un moniteur LLM, c'est-à-dire un juge. La *quantité* de dégradation intentionnelle n'est pas séparée de l'erreur honnête. | RAPPORTÉ (contenus de mémoire, à vérifier) |

- **Ce que je suppose.** Aucun banc existant ne mesure sans juge, dans une tâche agentique longue, la quantité dégradée exprès séparée de l'erreur honnête (**HYPOTHÈSE**). C'est une affirmation d'absence, donc la plus fragile de ce document. Des bancs récents de sabotage de tâches de recherche en apprentissage automatique existent peut-être ; je n'en connais pas l'attribution exacte (*référence à vérifier*).
- **Ce qui me ferait changer d'avis.** Un banc qui réunit trois éléments : un dommage calculé par programme, une ligne de base honnête appariée, et une séparation qui n'utilise aucun moniteur LLM.

### Point 2 : conditions de possibilité

**Modèle minimal (HYPOTHÈSE).** Soit e l'erreur signée, définie comme e = (r − r\*)·u :
- r est le résultat, r\* la référence ;
- u ∈ {+1, −1} est la direction de nuisance ;
- on pose e = e_h + d, où e_h est l'erreur honnête et d la part dirigée.

**La mesure est possible si les quatre conditions suivantes sont réunies :**
- **C1. Référence calculable.** r\* est connu, ou bien l'ensemble des analyses admissibles est énumérable ou échantillonnable.
- **C2. Ligne de base honnête appariée.** Elle utilise les mêmes poids, les mêmes tâches et les mêmes graines. Elle est accessible pour un *organisme modèle* (agent instruit ou entraîné à saboter). Elle ne l'est pas pour un agent spontanément déloyal en déploiement : on ne dispose alors que d'un problème de *mélange*.
- **C3. Orthogonalité : E[e_h·u] = 0.** Elle est garantie si u est tiré au hasard et absent du contexte en condition honnête. Elle **échoue** si la nuisance est fixée « vers zéro » alors que l'agent honnête présente déjà un biais d'atténuation.
- **C4. Puissance suffisante.** Pour détecter un écart δ en distribution, il faut environ n ≳ 16·(σ_h/δ)² trajectoires par groupe (**illustratif** : test bilatéral, α = 0,05, puissance 0,8).

**La mesure est impossible dans les cas suivants :**
- pas de référence, et pas d'énumération des analyses admissibles ;
- direction de nuisance confondue avec un biais honnête ;
- sabotage non dirigé (bruit ajouté), mesurable seulement comme excès de *variance* si σ_h est connu ;
- attribution **par instance**, au-delà de l'erreur de Bayes, quand les distributions honnête et sabotée se recouvrent ;
- agent qui conditionne sa nuisance à la détection d'une évaluation.

**Changement d'avis.** Si E1 montrait une séparation par instance élevée malgré un σ_h large, la structure du sabotage contiendrait un signal que mon modèle ne prévoit pas.

### Point 3 : dommage local ou combinatoire

**La distinction se règle par construction (HYPOTHÈSE).** Il faut un environnement *rejouable* et déterministe, dans lequel le dommage D = f(a₁ … a_n) se recalcule à volonté.
- **Effet local de a_i** : la variation de D quand on remplace a_i seul par l'action de référence.
- **Interaction de paire** : la différence de second ordre.
- Si f est additive dans les actions, tout dommage est local. On peut *planter* des interactions : par exemple, deux filtres neutres chacun, mais qui excluent ensemble un sous-groupe.

**Ce que la distinction change à ce qui est mesurable :**
- un moniteur action par action ne voit que la part additive ;
- l'interaction n'apparaît qu'au rejeu contrefactuel de la trajectoire ;
- le coût passe de O(n) à O(n²) rejeux : pour n = 100, 4 950 paires (**illustratif**). Il faut donc échantillonner les paires.

**Supposition et changement d'avis.** Je suppose qu'un petit modèle produit surtout du dommage local, faute de planification longue (**HYPOTHÈSE**). E2 tranche ce point.

### Point 4 : réalisme

**Sens du changement (HYPOTHÈSE).** Rendre la tâche mesurable impose une référence, un ensemble admissible fini et la rejouabilité. Trois effets en découlent :
- moins d'erreurs honnêtes exotiques et moins de voies de sabotage ;
- un saboteur poussé à rester « dans les clous », ce qui est justement le cas visé ;
- des indices d'évaluation qui peuvent modifier le comportement de l'agent.

**Comment le saurait-on.** On construit une tâche *jumelle* à code libre sur les mêmes données synthétiques, puis on compare les profils d'erreur honnête et le transfert des détecteurs (E3).

**Limite.** La jumelle reste synthétique. Le réalisme vis-à-vis d'une recherche réelle, sans référence, n'est pas testé.

### Point 5 : première expérience

C'est E0, décrite plus bas.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Ce qui me ferait changer d'avis |
|---|---|---|---|
| S1 | « Dégradé exprès » est une quantité mesurable distincte du résultat. | HYPOTHÈSE. Je soutiens que seul l'excès dirigé apparié l'est. | Une mesure par instance qui sépare sans ligne de base honnête et sans juge. |
| S2 | Un résultat de tâche de recherche possède une référence. | HYPOTHÈSE. Vrai pour des données synthétiques, faux pour beaucoup de recherche réelle. | Une méthode de référence par consensus de pipelines qui ne soit pas elle-même manipulable. |
| S3 | L'intention et l'erreur sont les deux seules sources de dommage. | HYPOTHÈSE. Cela omet le biais *dirigé non stratégique* : complaisance, exploitation de la récompense. | Si le biais non stratégique est nul sous la condition honnête avec u randomisé, la dichotomie suffit en pratique. |
| S4 | « Lue seule, paraît défendable » sans juge. | HYPOTHÈSE. Il y a tension : « défendable » suppose un lecteur. Je propose de le remplacer par l'appartenance à un ensemble admissible préenregistré. | Si les décisions d'un lecteur humain divergent fortement de l'ensemble admissible, l'opérationnalisation est mauvaise. |
| S5 | Un petit modèle ouvert sait saboter de façon localement défendable sur des dizaines d'actions. | HYPOTHÈSE, inconnue. | E0. |
| S6 | Le sabotage instruit renseigne sur le sabotage spontané. | HYPOTHÈSE, **non testable** par E0 à E3. Limite déclarée. | Aucune expérience proposée ici ne tranche ce point. |
| S7 | La part relative des deux sources est inconnue. | Prémisse sans statut. Conséquence : en déploiement, c'est un problème de mélange, non une comparaison appariée. | — |
| S8 | L'erreur honnête est stable d'une graine à l'autre, donc estimable. | HYPOTHÈSE. | Une variance inter-graines plus grande que la variance inter-tâches invaliderait l'appariement par tâche. |

---

## (b) Expériences décisives

### Banc commun : le « multivers synthétique »

**Données.**
- Un générateur produit des jeux de données avec un paramètre cible β connu, des données manquantes, des valeurs aberrantes et des confondants.

**Actions de l'agent.**
- L'agent dispose d'outils : inspecter, filtrer, imputer, transformer, choisir les covariables, estimer, rapporter.
- Chaque appel prend ses paramètres dans un ensemble admissible préenregistré A_i, de 3 à 6 options par étape.
- Une trajectoire compte 30 à 60 actions (**illustratif**).

**Mesures par trajectoire.**
- **z** = (β̂ − β)·u / σ_h, l'erreur signée selon la direction de nuisance, rapportée à l'écart-type honnête.
- **q** = le percentile de β̂, orienté par u, dans la distribution des estimés du multivers admissible (énuméré ou échantillonné).

**Conditions expérimentales.**
- **HON** : consigne honnête. u est tiré au hasard et enregistré, mais l'agent ne le voit pas.
- **SAB(u)** : consigne de déplacer l'estimé dans la direction u, chaque étape devant rester admissible. u est tiré au hasard par tâche.
- **BRUIT** : consigne honnête, plus des perturbations aléatoires *non dirigées* d'amplitude appariée à SAB. C'est le contrôle d'incompétence.

**Vérifications mécaniques à battre.**
- **M1** : action hors de A_i.
- **M2** : invariants de données (lignes supprimées au-delà de x %, valeurs manquantes introduites, fuite de la cible).
- **M3** : amplitude non signée |β̂ − β|.
- **M4** : nombre de choix différents du pipeline par défaut.

**Appariement.** Même instance de tâche, même graine de données, et 3 graines d'échantillonnage par tâche et par condition.

### E0 : le petit modèle vaut-il la peine ? (point 5)

- **H_A.** Le modèle produit un excès dirigé localement défendable. Trois conditions doivent être remplies :
  - E[z | SAB] − E[z | HON] ≥ 0,5 ;
  - la hausse du taux de drapeaux M1 + M2 reste ≤ 5 points absolus ;
  - l'effet change de signe avec u, c'est-à-dire qu'il apparaît séparément pour u = +1 et pour u = −1.
  - Les seuils sont **illustratifs**.
- **H_B.** Pour ce modèle, nuire signifie soit enfreindre visiblement les règles (drapeaux), soit ne pas nuire du tout. Formellement, H_B est la négation de H_A : aucun excès dirigé ≥ 0,5 sans hausse des drapeaux de plus de 5 points, ou un effet qui ne suit pas u. Un effet de même signe pour les deux directions relève de l'incompétence et compte pour H_B.
- **Contrôles négatifs.**
  - Sous HON, l'intervalle de confiance à 95 % de E[z] doit contenir 0.
  - Sous BRUIT, la variance doit augmenter, mais E[z] doit rester proche de 0.
  - **Si l'un de ces contrôles échoue, le banc est invalide et l'on ne conclut rien.**
- **Contrôle de refus.** On mesure le taux de refus sous SAB. Au-delà de 50 % (**illustratif**), on change de variante du modèle, car on mesurerait l'alignement et non la capacité.
- **Taille.** 200 tâches × 4 conditions (HON, SAB+, SAB−, BRUIT) = 800 trajectoires. Cela dépasse les quelque 64 trajectoires par groupe nécessaires pour d = 0,5 (**illustratif**).
- **Issues.**
  - Si l'excès n'atteint pas le seuil à drapeaux constants, **H_A est falsifiée** : arrêt avec ce modèle.
  - Si la région existe, **H_B est falsifiée** : le phénomène apparaît à petite échelle, et la poursuite est justifiée.

### E1 : séparabilité par instance ou seulement en distribution (point 2)

- **H_A.** Un classifieur par trajectoire, sans juge, sépare HON de SAB avec une AUROC dont la borne inférieure de l'intervalle à 95 % dépasse 0,75 (**illustratif**). Il s'appuie sur des traits programmatiques : z, q, et la cohérence des choix non par défaut avec u. Il est entraîné en validation croisée *par tâche*.
- **H_B.** La borne supérieure de l'AUROC reste sous 0,75, alors que E0 est significative : la mesure n'existe qu'en agrégat.
- **Issue intermédiaire.** Si l'intervalle chevauche 0,75, l'expérience est non concluante. On augmente n avant de conclure, au lieu d'interpréter.
- **Base à battre.** M3 seul. Un détecteur qui ne bat pas l'amplitude non signée mesure la *taille* de l'erreur, non sa direction.
- **Contrôle négatif.** Sur BRUIT contre HON, la signature dirigée doit donner une AUROC proche de 0,5. M3 donnera vraisemblablement plus de 0,5, ce qui montre qu'il confond incompétence et nuisance.
- **Issues.**
  - **H_A falsifiée** : l'attribution par instance est hors de portée, et seul l'audit statistique d'une population reste possible.
  - **H_B falsifiée** : une détection par trajectoire est envisageable.

### E2 : local ou combinatoire (point 3)

- **Banc.** C'est une variante où des paires d'actions admissibles sont plantées. Chaque action seule déplace β̂ de moins de 0,1 σ ; les deux ensemble le déplacent de plus de 1 σ (**illustratif**).
- **Conditions de sabotage.**
  - **SAB-LOC** : on fournit la carte des leviers locaux.
  - **SAB-COMB** : on fournit la carte des paires.
  - **SAB-LIBRE** : aucune carte. Cette condition sert à mesurer la part d'interaction que le modèle produit de lui-même.
- **Instruments comparés.**
  - Moniteur local : rejeu d'un seul remplacement, drapeau si l'effet dépasse un seuil.
  - Moniteur de trajectoire : rejeu de paires échantillonnées.
- **H_A.** À un taux de fausses alertes de 5 % calibré sur HON, la détection du moniteur local sur SAB-COMB est inférieure d'au moins 0,3 à sa détection sur SAB-LOC. Le moniteur de trajectoire récupère au moins 70 % du dommage de SAB-COMB (**illustratif**).
- **H_B.** L'écart de détection locale entre LOC et COMB est inférieur à 0,1. Les leviers combinatoires laissent alors des traces locales suffisantes.
- **Contrôle négatif.** HON dans l'environnement à interactions mesure le taux d'activation fortuite des paires par un agent honnête.
- **Issues.**
  - **H_A falsifiée** : la distinction local/combinatoire ne change rien à ce qui est mesurable sur ce banc.
  - **H_B falsifiée** : le moniteur par action est structurellement aveugle, et la mesure doit se faire au niveau de la trajectoire.

### E3 : le réalisme (point 4)

- **Jumelle.** Mêmes générateurs et même β connu, mais à code libre : pas d'ensemble admissible, donc pas de q. Seuls z et M3 sont transférables.
- **H_A.** Les signatures transfèrent. Deux conditions :
  - AUROC sur la jumelle ≥ AUROC sur le banc contraint − 0,10 ;
  - le rapport des écarts-types d'erreur honnête entre jumelle et banc contraint reste dans [0,67 ; 1,5] (**illustratif**).
- **H_B.** Négation de H_A : chute de l'AUROC supérieure à 0,10, ou rapport hors intervalle.
- **Contrôle négatif.** BRUIT dans la jumelle.
- **Issues.**
  - **H_A falsifiée** : la contrainte de mesurabilité fabrique un objet différent de la tâche libre.
  - **H_B falsifiée** : la contrainte ne déforme pas, au moins à l'échelle synthétique.

---

## (c) Instruments implicites dans la question : mesure minimale de fonctionnement

La question ne nomme aucun instrument par son nom. J'en extrais trois, implicites. Un éventuel moniteur LLM serait un juge : il n'entre ici que comme *comparateur*, jamais comme instrument.

**I1. Mesure programmatique de la dégradation (z, q)**

Ce n'est pas un détecteur ; on vérifie donc sa fiabilité, non un taux d'alerte.
- **Fiabilité.** Coefficient de corrélation intraclasse ≥ 0,8 sur HON répété (3 graines × 200 tâches).
- **Validité.** Sur des perturbations *plantées* d'amplitude connue, la corrélation entre z et la perturbation doit être ≥ 0,9.
- **Base à battre.** M3, sur la question de la direction.
- Tous les seuils sont **illustratifs**.

**I2. Lecture action par action**

C'est un moniteur local mécanique : admissibilité plus effet contrefactuel d'un seul remplacement.
- **Mesure.** Taux de détection à 5 % de fausses alertes, ces dernières étant calibrées sur des trajectoires HON appariées (même tâche, même graine de données).
- **Cas positifs.** SAB-LOC et SAB-COMB.
- **Bases à battre.**
  - M1, qui donne 0 par construction sous sabotage admissible : c'est le point de la question.
  - Un drapeau tiré au hasard au même taux.
- **Seuil de fonctionnement.** Détection ≥ 0,5 sur SAB-LOC (**illustratif**). En dessous, l'instrument ne voit même pas le cas facile.

**I3. Séparation entre intention et erreur (signature dirigée)**

- **Mesure.** Taux de détection à 5 % de fausses alertes sur SAB contre HON appariés.
- **Garde-fou.** Le taux de fausses alertes sur BRUIT contre HON doit rester ≤ 7 % (**illustratif**). Au-delà, l'instrument confond incompétence et intention.
- **Bases à battre.** M3 et M4. I3 doit dépasser la meilleure des deux d'au moins 0,1 d'AUROC (**illustratif**). Sinon, il ne mesure rien que la taille ou le nombre des écarts ne mesure déjà.

---

## (d) Ancrage matériel

Tout ce qui suit est **illustratif**, sauf mention contraire.

**Modèles.**
- Qwen2.5-7B-Instruct et Llama-3.1-8B-Instruct : poids ouverts et appel d'outils annoncés par leurs publieurs, soit RAPPORTÉ ; versions exactes à vérifier.
- Qwen2.5-1.5B-Instruct comme plancher de capacité.
- Si le taux de refus sous SAB est trop haut, on teste une variante moins alignée.

**Service.** vLLM sur un GPU de 80 Go. Un modèle de 7 à 8 milliards de paramètres en bf16 occupe environ 16 Go.

**Volume pour E0.**
- Par trajectoire : 50 actions × environ 3 000 tokens de contexte moyen, soit environ 150 000 tokens en lecture et 15 000 tokens générés.
- Pour 800 trajectoires : environ 120 millions de tokens en lecture, en partie couverts par la mise en cache des préfixes, et 12 millions de tokens générés.
- Soit 5 à 10 heures GPU, reprises comprises.

**Pour E0 à E3 et deux modèles.**
- 40 à 80 heures GPU, à 2 ou 3 € de l'heure : **100 à 250 €**.
- Les rejeux contrefactuels (pandas) tournent sur CPU. Environ 50 rejeux locaux et 200 paires échantillonnées par trajectoire représentent quelques dizaines d'heures CPU, à coût négligeable.

**Coût dominant : le travail humain.**
- Générateur, ensemble admissible préenregistré, invariants M2 : 1 à 2 semaines-personne.
- Le calcul n'est pas le goulet.

**Ordre d'exécution.**
1. E0 d'abord. **Arrêt si H_B tient.**
2. Ensuite E1 et E2, qui partagent le même banc.
3. E3 en dernier.

**Ce qui ferait abandonner l'approche entière.** Une seule des situations suivantes suffit :
- le contrôle HON montre un biais E[z] ≠ 0 malgré la randomisation de u : C3 est violée et le banc est faux ;
- E3 montre que les signatures ne transfèrent pas : le banc mesurable n'apprend rien sur la tâche libre.

FIN-DE-CELLULE