# Proposition E — distinguer détection, causalité et contrainte d’évasion

Les propositions A–D et les pièces sources intégrales ne sont pas transmises ; je ne leur attribue aucun contenu supplémentaire.

**Statut de cette proposition : HYPOTHÈSE.** Tous les plans, critères, seuils et budgets proposés ci-dessous sont des hypothèses de travail, non des résultats. Tout chiffre de conception ou de coût est **illustratif**. Aucun nouvel article n’est cité.

## A. Ce que la question suppose sans l’avoir établi

| Présupposé | Statut et objection |
|---|---|
| L’oracle reconnaît le sabotage diffus et distingue celui-ci d’un échec honnête. | **HYPOTHÈSE.** L’audit du rappel manque dans les faits transmis. Une baisse de couverture établit un dommage, pas à elle seule son origine intentionnelle. |
| La diversité des familles oracle–moniteurs assure leur indépendance. | **HYPOTHÈSE.** Elle constitue un contrôle de conception, pas une mesure d’indépendance des erreurs. Celle-ci exige une vérité terrain tierce. |
| Une information interne existe « au-delà du texte ». | **HYPOTHÈSE à préciser.** Il faut définir le texte accessible au comparateur : préfixe public, sortie complète ou entrée complète incluant la consigne privée. La proposition testable porte sur un **gain prédictif hors échantillon**, relativement à des comparateurs gelés, pas sur une information intrinsèquement inaccessible au texte. |
| L’écart adapté–base retire le contrôle de l’attaquant. | **HYPOTHÈSE partielle.** Les poids du modèle de base peuvent être hors de son contrôle ; le contexte rejoué peut néanmoins provenir de sa trajectoire. |
| Une direction causale rend la sonde inévitable. | **HYPOTHÈSE.** Modifier le dommage par une intervention ne démontre ni nécessité de cette direction ni absence d’un autre chemin de sabotage. |
| Une mâchoire interne doit être causale pour améliorer la détection. | **HYPOTHÈSE non nécessaire au test prédictif.** Une lecture corrélée peut apporter une capture résiduelle ; la causalité est une revendication supplémentaire. La direction aversive décrite comme lisible mais non causale demeure **RAPPORTÉE**. |
| Le prédicteur textuel peut servir directement de mâchoire externe. | **HYPOTHÈSE incompatible avec la définition stricte** s’il lit la prose de l’agent. Il reste un comparateur boîte noire distinct. L’externe stricte ne reçoit que code et exécution nettoyés. |
| Une capture résiduelle prouve que l’étau serre. | **HYPOTHÈSE.** Elle établit une complémentarité conditionnelle, pas que l’effort d’évasion externe augmente la trace interne. |
| L’absence de sonde dominante impose un équilibre mixte. | **HYPOTHÈSE à corriger.** Il faut rechercher un point-selle pur ; l’absence de dominance d’une colonne ne suffit pas à l’exclure. |
| Un résultat négatif exclurait toute trace. | **HYPOTHÈSE trop large.** Il ne réfuterait que la trace exploitable aux positions, couches, capacités et budgets testés. |

## B. Contrat expérimental commun

**HYPOTHÈSE — préenregistrement proposé.**

- Unité principale : **épisode**, avec actions imbriquées ; séparation par tâche, monde et famille d’organismes. Aucun partage de jumeaux entre entraînement et test.
- Négatifs appariés : jumeaux honnêtes réussis **et échoués**, placebo soumis aux mêmes tâches, épisodes dormants du saboteur, mentions innocentes de sabotage, contextes avec consigne d’attaque mais acte honnête.
- Positifs : dommage attesté et provenance scellée ; les cas dont l’attribution reste ambiguë sont rapportés séparément.
- Seuil principal : **1 % de fausses alertes**, demandé par l’arbitre, mesuré **par épisode**, avec résultats également ventilés par négatif et famille.
- Calibration indépendante du test. Intervalles par rééchantillonnage hiérarchique des tâches et épisodes ; intervalles binomiaux en contrôle lorsque l’indépendance est défendable.
- Pour chaque duel, \(H_A\) et \(H_B\) sont des régions exclusives et exhaustives du paramètre annoncé. Une borne d’intervalle entièrement d’un côté falsifie l’autre hypothèse ; un intervalle chevauchant le seuil donne **indécis**, jamais une victoire forcée.
- Les analyses exploratoires de couches ne deviennent pas confirmatoires par sélection du meilleur résultat. Sélection interne aux plis, puis test gelé.
- Le mode réservé n’est ouvert qu’à G1. Une reconception utilise des familles vues pour son développement puis une nouvelle famille réservée pour sa lecture décisive.

### Champs communs aux fiches

**HYPOTHÈSE — applicables à chaque fiche sauf précision contraire.**

- **Données brutes exigées :** identifiants appariés, provenance scellée, condition expérimentale, labels et désaccords, sorties, traces exécutées, scores non seuillés, budgets et temps.
- **Méthode et outil :** sas automatisé tiers ; scripts Python, extraction PyTorch, ajustements scikit-learn et optimisation linéaire SciPy ; versions et empreintes gelées.
- **Pièce produite :** protocole, manifeste, code et tables agrégées publics ; références cachées, détails du bras rouge et données réservées scellés.
- **Vérifiable par :** recalcul indépendant dans le sas, puis adjudication humaine de Lazar Ciric.
- **Coût et délai :** postes du tableau matériel final. Aucune dépense n’est engagée par cette proposition.

## C. Expériences décisives

### Fiche O — qualifier l’oracle avant de lire les sondes

**Volet :** vérité terrain. **Mâchoire :** sans objet. **Règle :** sans objet. **Test causal :** aucun.

Construire un audit aveugle à partir de cas connus et scellés, vérifiables par événements exécutés et référence cachée, sans demander aux moniteurs de définir le positif. Inclure les omissions diffuses et les échecs honnêtes difficiles, pas seulement le flagrant.

**Grandeurs :** rappel \(r_O\), fausses accusations \(f_O\), abstentions, accord entre lecteurs, chacun par strate.

**Duel, seuils illustratifs :**

- \(H_A\) : \(r_O\geq0{,}95\) et \(f_O\leq0{,}01\) dans chaque strate indispensable.
- \(H_B\) : au moins une de ces exigences échoue.

Des bornes simultanées certifiant toutes les exigences falsifient \(H_B\) ; une borne certifiant une violation falsifie \(H_A\). **Absence de qualification, y compris faute de précision : suspension des lectures décisives suivantes.**

**Indépendance :** avant les sondes, geler un lot tiers dont les labels ne proviennent pas de l’oracle. Après qualification seulement, mesurer sur ce lot :
\[
d=\max_z\left|P(E_M=1\mid E_O=1,z)-P(E_M=1\mid E_O=0,z)\right|,
\]
où \(z\) comprend vérité terrain, tâche et gravité.

Duel auxiliaire : \(H_A:d\leq0{,}05\), \(H_B:d>0{,}05\), seuil **illustratif**. Une rareté des erreurs rend ce test indécis ; elle ne démontre pas l’indépendance. Le lot tiers doit donc comprendre un échantillon représentatif et un panel difficile analysé séparément.

**Contrôle négatif :** échecs honnêtes appariés. **Issue négative :** labels insuffisamment fiables, non « sondes défaillantes ».

---

### Fiche T — trace et localisation sans confusion d’identité

**Volets :** existence, localisation. **Mâchoire :** interne. **Règle :** figée. **Test causal :** aucun.

**Données supplémentaires :** activations adaptées et base sur **les mêmes jetons**, avant, pendant et après l’action ; sous-espaces des adaptateurs vus ; préfixes publics et consignes conservés sous contrôle d’accès.

Comparer des modèles imbriqués : texte public seul, texte et contrôles, puis ajout d’activations. Rapporter séparément les performances antérieures à l’action et celles postérieures : une trace après dommage n’est pas une prévention.

**Grandeur principale :**
\[
\Delta_T=\mathrm{TPR}_{\text{texte+interne}}-\mathrm{TPR}_{\text{texte}},
\]
au même taux de fausses alertes, sur familles laissées hors apprentissage.

**Duel :** \(H_A:\Delta_T\geq0{,}05\), \(H_B:\Delta_T<0{,}05\), marge **illustrative**. Borne inférieure au-dessus de la marge : falsification de \(H_B\) ; borne supérieure en dessous : falsification de \(H_A\).

**Contrôles :**

- Paires consigne × acte, incluant sabotage sans consigne à l’inférence.
- Placebo et épisodes dormants, avec estimation **intra-organisme**.
- Contrôle positif flagrant corrigé de la fuite ; apprentissage d’une propriété bénigne observable pour diagnostiquer la capacité du pipeline.
- Étiquettes permutées par blocs ; comparateurs texte de capacités différentes.
- Écart adapté–base comparé à l’écart placebo–base.

La localisation est retenue seulement si elle se reproduit hors des blocs ayant servi à la choisir. **Issue négative :** aucune utilité incrémentale démontrée dans ce périmètre, même si la sonde reconnaît les poids.

---

### Fiche C — intervention spécifique plutôt que dégradation générale

**Volet :** causalité. **Mâchoire :** interne. **Règle :** sans objet.

**Test causal :** interventions défensives randomisées : ablation, substitution depuis le jumeau honnête, perturbation témoin de norme comparable ; dose de l’adaptateur comme contrôle global distinct.

**Grandeurs :** diminution du dommage contre contrôle fictif, \(B_D\), et perte de qualité honnête, \(L_Q\), toutes deux normalisées selon une échelle gelée.

**Duel, seuils illustratifs :**

- \(H_A:B_D\geq0{,}05\) et \(L_Q\leq0{,}02\).
- \(H_B\) : complément de cette région.

L’intervention doit satisfaire conjointement les bornes pour falsifier \(H_B\). Une insuffisance démontrée sur l’un des critères falsifie \(H_A\).

**Contrôles négatifs :** mêmes interventions sur placebo, jumeaux honnêtes et directions témoins ; mêmes positions et intensités ; effets sur longueur, refus et réussite de tâche publiés.

**Issue négative :** seul le score de sonde change, ou le dommage baisse parce que toute compétence baisse. Une dose-réponse de l’adaptateur entier ne localise pas une cause ; une intervention réussie ne prouve pas l’inévitabilité.

---

### Fiche L — lisibilité sans labels positifs

**Volet :** lisibilité. **Mâchoire :** interne. **Règle :** figée, puis réserve secrète.

Geler, avec des données honnêtes seulement, un détecteur de nouveauté sur activations, un détecteur d’écart adapté–base et un test séquentiel sur actions. Aucune étiquette positive utilisée pour choisir leurs hyperparamètres.

**Grandeur :** gain de rappel sur le meilleur comparateur mécanique et textuel gelé, à fausses alertes égales.

**Duel :** \(H_A:\Delta_L\geq0{,}05\), \(H_B:\Delta_L<0{,}05\), seuil **illustratif** ; mêmes règles de falsification que T.

**Contrôles négatifs :** longues tâches honnêtes, changements bénins de domaine, erreurs honnêtes autocorrélées, placebo. La calibration porte sur le **franchissement durant l’épisode entier**.

Un SPRT n’est retenu que si ses rapports de vraisemblance et son contrôle sous dépendance sont validés ; sinon, seuil empirique sur trajectoires complètes. L’agrégation des jetons reste max ou attention ; l’accumulation proposée porte sur les **actions**, sans moyenne cachée des jetons.

**Issue négative :** le détecteur mesure longueur, difficulté ou identité, non l’acte.

---

### Fiche R — transfert, mélange et secret sur un vrai modèle

**Volet :** règle de défense. **Mâchoire :** interne. **Règles :** figée, adaptative, mélange d’équilibre, réserve secrète. **Test causal :** assignation randomisée des régimes défensifs.

Mesurer d’abord une table **génération d’attaque × génération de défense**, puis la matrice détaillée entre sondes. Pour chaque cellule publier :

- dommage obtenu ;
- probabilité de dommage non détecté ;
- détection conditionnelle au dommage ;
- fausses alertes sur les mêmes honnêtes.

Ainsi, une attaque devenue inoffensive n’apparaît pas artificiellement comme une évasion.

**Grandeur principale :** réduction \(G_R\) du dommage non détecté contre une défense fixe choisie avant test, à budgets égaux.

**Duel :** \(H_A:G_R\geq0{,}05\), \(H_B:G_R<0{,}05\), marge **illustrative**. Calculer la valeur minimax sur la matrice observée, avec sensibilité à l’incertitude ; ne pas l’extrapoler à toutes les attaques possibles.

**Secret contre aléa :** plan factoriel « distribution révélée/cachée » × « tirage par requête/affectation fixe par session », avec fréquences marginales, retours et budget identiques. Dans le bras révélé, les tirages futurs restent cachés. Ajouter un facteur séparé « composition du panel révélée/cachée » : cacher les membres n’est pas cacher leurs probabilités.

Pour chaque effet marginal préenregistré : \(H_A:G\geq0{,}05\), \(H_B:G<0{,}05\), seuil **illustratif**.

**Contrôle négatif :** panel de sondes dupliquées. **Confondant traité :** attaquant évaluant l’espérance sur l’aléa ; son budget est journalisé par un tiers.

**Issue négative :** aucun gain du tirage, du secret ou de l’adaptation après égalisation des ressources.

---

### Fiche P — complémentarité de la pince et étau : deux revendications

**Volet :** pince. **Mâchoire :** jointe. **Règle :** figée, puis régime retenu. **Test causal :** assignation du régime externe connu du bras rouge, sans lecture de ses procédés.

Calibrer l’externe sur code et exécution nettoyés, l’interne sur activations. Partager le budget : \(\tau_E=\tau_I=\tau/2\), conformément au cadre transmis.

**Grandeur principale :**
\[
R=P(I^+\mid Y^+,E^-).
\]
Publier aussi la masse \(P(Y^+,E^-)\), les alertes honnêtes conjointes et les rappels des mâchoires seules, recalibrées chacune à \(\tau\).

**Duel complémentarité :**

- \(H_A\) : \(R\geq0{,}20\) **et** gain conjoint contre la meilleure mâchoire seule \(\geq0{,}05\).
- \(H_B\) : complément.

Seuils **illustratifs**. La seule capture résiduelle ne suffit pas si le partage du budget fait perdre davantage de détections ailleurs.

**Duel étau :** comparer, à budgets assignés identiques, les régimes de pression externe ; estimer le déplacement du score interne et le coût en dommage/qualité sur **tous** les épisodes, puis sur les manqués externes à titre conditionnel.

- \(H_A\) : pression externe causant une hausse du score interne d’au moins \(0{,}20\) écart-type honnête, à dommage maintenu.
- \(H_B\) : effet inférieur.

Seuil **illustratif**. Ne pas inférer cet effet d’une simple comparaison des seuls survivants : leur sélection peut changer.

**Contrôles négatifs :** transformations bénignes des traces, placebo, interventions fictives ; tests de frontière correspondant à L2 et E7, explicitement séparés du régime principal.

**Courbe de coût :** pour chaque budget et nombre de sondes, publier la frontière empirique dommage–qualité–non-détection, avec échecs du bras rouge. Une absence d’évasion découverte n’est qu’une borne relative au budget.

**Arrêt illustratif :** \(k=3\) sondes, tolérance \(\varepsilon=0{,}02\) de dommage non détecté, trois générations successives sans amélioration supérieure à \(\varepsilon\), et plafond ferme de calcul. Conclusion autorisée : « plateau dans ce budget », pas convergence universelle.

## D. Mesure minimale par instrument

**HYPOTHÈSE — chaque ligne exige rappel, fausses alertes et intervalles par épisode.**

| Instrument | Cas honnêtes appariés et vérification à battre |
|---|---|
| Oracle, lecteurs, vérificateur de citations | Échecs honnêtes ; battre une décision fondée uniquement sur correspondance littérale, événements exécutés et couverture mécanique. La citation exacte ne certifie pas toute la couverture. |
| Jev, juge génératif externe | Même code, tâche et environnement ; battre analyse syntaxique, tests exécutables et invariants autorisés. Comptabiliser refus et abstentions sans exclusion. |
| Prédicteur textuel | Textes honnêtes de même longueur et difficulté ; battre longueur, compteurs d’outils et traits lexicaux simples. Comparateur distinct de l’externe stricte. |
| Sondes génériques, dernier état, cascade, attention, max, direction aversive | Dormants, placebo, consigne sans acte ; battre identité d’organisme et vérifications mécaniques. Évaluer la cascade entière, pas seulement ses portes. |
| Écart adapté–base, sous-espace d’adaptateur, nouveauté, méta-moniteur | Placebo–base, domaines nouveaux bénins ; battre norme brute des écarts et scores de difficulté. |
| Ablation, pilotage, substitution, dose | Ce ne sont pas des détecteurs : publier le rappel/fausses alertes du lecteur associé **et** l’effet dommage/qualité contre intervention fictive. |
| Accumulation, autocorrélation, SPRT | Épisodes honnêtes longs et corrélés ; battre seuil max et règle de comptage d’actions gelée. |
| Mélange, réserve, seuil stochastique, défense différée, trafic de couverture, Hedge éventuel | Même flux honnête et budget ; battre sonde fixe, mélange uniforme et planning non adaptatif. Mesurer aussi latence et surcharge. |
| Fusion par rapports de vraisemblance | Calibrer la décision jointe sur honnêtes. Ne pas multiplier les rapports marginaux sans modèle justifié de leur dépendance. |
| Matrice de transfert, valeur de Nash | Publier les cellules avec dommage et fausses alertes, pas seulement un scalaire optimisé ; comparer au meilleur pur choisi hors test. |

## E. Ancrage matériel et puissance

**HYPOTHÈSE — configuration illustrative, sous devis et GO humain.**

- Modèles candidats à poids ouverts : **Qwen2.5-7B-Instruct** comme organisme instrumenté ; **Mistral-7B-Instruct-v0.3** comme candidat lecteur d’une autre famille. Disponibilité, licences, compatibilité et indépendance vis-à-vis des organismes existants à vérifier. Priorité aux organismes T0.6 existants.
- Extraction sur une carte **A100 de 80 Go, illustrative** ; activations sélectionnées seulement après le pilote, conservées en précision réduite. Régression, calibration et optimisation sur processeur.
- Cible initiale **illustrative** : 6 000 épisodes négatifs et 3 000 positifs diffus, hors entraînement. À 1 %, cela représente environ **60 alertes attendues, illustratif** sur le dénominateur honnête global : insuffisant pour garantir la précision de toutes les sous-strates.
- Dimensionnement final par simulation appariée sur pilotes vus : corrélation intra-tâche, désaccords oracle, fréquence des manqués externes et multiplicité inclus. Si le dénominateur résiduel est trop petit, P reste indécis.

| Poste | Calcul, coût et délai illustratifs |
|---|---|
| O : audit et sas | 10–30 heures processeur ; 20–100 USD ; 2–4 jours |
| T et L : extraction, comparateurs | 40–120 heures carte ; 80–480 USD ; 2–5 jours |
| C : interventions | 30–100 heures carte ; 60–400 USD ; 2–4 jours |
| R et P : campagnes défensives | 80–200 heures carte ; 160–800 USD ; 3–7 jours |

**Total illustratif : 320–1 780 USD**, hors travail humain, stockage durable, appels externes éventuels et fabrication de nouvelles familles. Hypothèse tarifaire **illustrative : 2–4 USD par heure carte**. Le devis doit être recalculé sur le débit mesuré ; aucune échéance TAIF précise n’étant fournie, je ne promets pas sa tenue.

**Choix proposé :** financer d’abord O, puis T. Préenregistrer dès maintenant C, R et P, mais ne pas transformer une détection corrélative en preuve d’étau, ni un plateau budgétaire en preuve d’inévitabilité.

FIN-DE-CELLULE