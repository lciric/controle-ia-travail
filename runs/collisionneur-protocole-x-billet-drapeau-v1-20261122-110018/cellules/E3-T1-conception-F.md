**Constat sur les pièces transmises (Règle 2)** : le bloc `FAITS` est identique au bloc `QUESTION DE L'ARBITRE` (même empreinte SHA-256) et ne contient aucune donnée empirique, aucun nom de domaine ni aucune spécification technique du dispositif de détection ; aucun fait extérieur n'est inventé.

*Conventions d'intégrité* : chaque affirmation porte un statut explicite (`VÉRIFIÉ`, `RAPPORTÉ`, `OBSERVÉ-NON-AUDITÉ`, `HYPOTHÈSE`). Hormis les identifiants structurels (sections, $H_A/H_B$, C0–C5) et les noms propres ou normes (ex. `SHA-256`, `RFC 3161`, noms de modèles ouverts), tout chiffre quantitatif ne figurant pas dans `FAITS` est marqué « illustratif ». Aucune observation empirique n'étant transmise, la catégorie `OBSERVÉ-NON-AUDITÉ` n'est pas remplie artificiellement (`VÉRIFIÉ` d'après le bloc `FAITS`).

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Aucune mesure n'est encore faite et le dispositif est supposé digne d'une revendication ultérieure.**
   - Qu'aucune mesure ne soit faite est posé par l'énoncé (`RAPPORTÉ`). Que le dispositif fonctionne au-dessus d'une vérification mécanique simple et aboutisse à un résultat publiable sans refonte majeure reste non établi (`HYPOTHÈSE`). Publier avant toute mesure expose à une asymétrie réputationnelle si le détecteur échoue.
2. **Les « travaux voisins » créent un risque matériel de devancement sur la même contribution vérifiable.**
   - L'apparition de travaux voisins est posée par l'énoncé (`RAPPORTÉ`). Le passage de « travaux voisins » à « risque élevé qu'un autre groupe publie la même contribution avant l'équipe » n'est pas audité (`HYPOTHÈSE`).
3. **Un texte court sans résultats peut conférer une reconnaissance scientifique ultérieure.**
   - Non établi (`HYPOTHÈSE`). Dans de nombreux champs empiriques, le crédit d'antériorité s'attache à la preuve expérimentale ou à l'artefact validé, non à l'annonce d'une intention ; une revendication prématurée sans données peut même provoquer un coût réputationnel (référence à vérifier).
4. **Rendre public un texte court réduit — ou modifie dans un sens connu — la probabilité qu'un autre groupe publie d'abord.**
   - Non établi (`HYPOTHÈSE`). Le signe de l'effet est ambigu : un texte court peut dissuader un concurrent peu avancé, mais il peut aussi fournir gratuitement le cadrage ou le plan d'exécution à une équipe mieux dotée qui publiera les premiers résultats empiriques (« effet catalyseur »).
5. **Le secret requis pour la validité des mesures est encore intact aujourd'hui et ne serait rompu que par le texte court.**
   - Que certaines mesures dépendent de l'ignorance de personnes ou de systèmes est posé par l'énoncé (`RAPPORTÉ`). Qu'aucun travail voisin n'ait déjà exposé le modèle de menace ou contaminé les systèmes cibles, et que la confidentialité ne puisse pas être scindée entre protocole public et éléments secrets (sondes, clés, cas de test), n'est pas établi (`HYPOTHÈSE`).
6. **L'adversaire ou les systèmes ciblés surveillent et ingèrent les publications dans la fenêtre temporelle de l'étude, avec une capacité d'adaptation effective.**
   - Non établi (`HYPOTHÈSE`). L'impact dépend du canal d'ingestion (modèle figé hors ligne contre système connecté à la recherche web ou adversaire humain veillant les prépublications) et du délai entre le texte court et la collecte des mesures.
7. **La décision se résume à une alternative globale entre « publier avant », « publier après » et « ne rien publier ».**
   - Présupposé de cadrage (`HYPOTHÈSE`). Il exclut implicitement des dispositifs hybrides qui découplent la preuve d'antériorité de la divulgation publique : empreinte cryptographique publique muette (`SHA-256` horodaté) ou rapport enregistré sous embargo.
8. **La publication préalable améliore (ou dégrade) de façon nette la qualité et le coût de l'étude.**
   - Non établi (`HYPOTHÈSE`). Un pré-engagement public peut réduire les degrés de liberté du chercheur et attirer des critiques utiles, mais il peut aussi figer un protocole imparfait avant les essais pilotes, alourdir la charge de rédaction et imposer une refonte coûteuse si le secret fuit.
9. **Des vérifications indépendantes peuvent établir qu'un choix unique était « le bon ».**
   - Non établi (`HYPOTHÈSE`). Pour une étude isolée, le contrefactuel historique (ce qu'un concurrent ou un adversaire aurait fait sous l'autre choix) n'est pas directement observable. Les vérifications indépendantes ne peuvent auditer que des mécanismes causaux intermédiaires (fuite, contamination, gain adversarial, fidélité au protocole, attribution par pairs), sauf dispositif contrôlé sur plusieurs éléments ou études.
10. **Le dispositif de détection n'est pas nommé dans les pièces.**
    - Fait textuel direct (`VÉRIFIÉ`) : ni le domaine, ni la nature du détecteur, ni la classe d'adversaire ne figurent dans `FAITS`, ce qui interdit d'inférer la robustesse du détecteur à la divulgation sans test préalable.

---

## Réponse analytique aux questions de l'arbitre

### 1. Contenus possibles du texte court et matrice d'effets

Les effets empiriques ci-dessous portent tous le statut `HYPOTHÈSE`, hormis les propriétés structurelles d'un engagement cryptographique sous hypothèse standard de résistance aux préimages (référence à vérifier). Six niveaux gradués de contenu sont envisageables :

- **C0 — Empreinte cryptographique publique muette** : publication d'un condensat `SHA-256` (horodaté par un tiers `RFC 3161`) d'un dossier complet tenu privé (protocole, hypothèses, seuils, sondes). Contenu substantiel public : nul.
- **C1 — Note de cadrage abstrait** : formulation générale du problème et de la taxonomie de menace, sans hypothèses testables, sans métriques ni architecture.
- **C2 — Pré-enregistrement « Kerckhoffs » (protocole sans secrets)** : hypothèses falsifiables, plan statistique, métriques, seuils et contrôles publiés ; mécanismes sensibles, sondes, stimuli et données de test maintenus sous scellé cryptographique. (Principe inspiré d'Auguste Kerckhoffs, 1883, « La cryptographie militaire », *Journal des sciences militaires* : la sécurité ne doit pas reposer sur le secret de la structure générale, mais uniquement sur la clé.)
- **C3 — Architecture du dispositif de détection (sans jeux de test)** : description fonctionnelle du détecteur avant exécution des mesures.
- **C4 — Divulgation d'éléments opérationnels sensibles** : sondes, stimuli, marqueurs, cibles, seuils exacts de déclenchement ou échantillons d'évaluation.
- **C5 — Protocole complet déposé sous embargo auprès d'un tiers indépendant** (registre sous embargo ou revue de rapport enregistré en aveugle avant collecte, non public avant les résultats).

| Contenu | Reconnaissance ultérieure (`HYPOTHÈSE`) | Probabilité qu'un autre groupe publie d'abord (`HYPOTHÈSE`) | Validité des mesures à venir (`HYPOTHÈSE`) | Apprentissage par un adversaire (`HYPOTHÈSE`) | Qualité et coût de l'étude (`HYPOTHÈSE`) |
|---|---|---|---|---|---|
| **C0** (hachage horodaté) | Faible à l'instant $t$ ; preuve d'antériorité vérifiable *ex post* lors de la révélation si résultats probants | Inchangée (aucun signal dissuasif ni accélérateur) | Préservée intégralement | Nul (aucune information divulguée) | Coût marginal quasi nul ; aucun retour critique externe ; bloque la réécriture *post hoc* des hypothèses |
| **C1** (cadrage abstrait) | Très faible ; risque de rejet pour « revendication sans preuve » | Effet ambigu (dissuasion faible, signal d'intérêt possible) | Faible risque direct, sauf sensibilisation générale de participants/systèmes | Faible : apprend que la classe de menace est étudiée | Coût faible ; retours trop généraux pour corriger le protocole |
| **C2** (protocole sans secrets) | Modérée si suivi vite de résultats ; fort gain de crédibilité méthodologique | Ambigu : dissuade des équipes lentes, mais peut **accélérer** un groupe mieux doté disposant du plan prêt à l'emploi | Préservée uniquement si les secrets restent isolés et si les métriques publiées n'induisent pas d'optimisation ciblée | Modéré : l'adversaire apprend les métriques et contrôles visés (risque d'adaptation de type Goodhart, référence à vérifier) | Gain potentiel de qualité (revue publique, anti-HARKing) ; coût de rédaction/tri des critiques ; risque de verrouillage prématuré avant pilote |
| **C3** (architecture du détecteur) | Faible si un concurrent exécute et publie les mesures en premier | **Augmente** probablement face à des équipes mieux dotées en calcul/données | Compromission élevée si la détection ne résiste pas à un adversaire connaissant l'architecture | **Élevé** : conception de contournements adaptatifs avant même la mesure | Coût élevé de refonte si le détecteur est contourné avant collecte ; utile seulement pour tester la robustesse boîte blanche |
| **C4** (éléments secrets) | Nulle ou négative (mesures invalidées) | Variable, mais le protocole initial perd sa valeur | **Détruite** : contamination des systèmes/participants et invalidation des tests | **Maximal** : évasion triviale et filtrage ciblé des sondes | Coût maximal (obligation de reconstruire l'ensemble des instruments secrets) |
| **C5** (embargo tiers / revue fermée) | Preuve d'antériorité et de fidélité auditable *ex post* sans risque de « drapeau flou » | Inchangée vis-à-vis de tiers extérieurs (pas de fuite vers concurrents) | Préservée intégralement | Nul (sous confidentialité effective des relecteurs) | Gain de qualité via critique structurée avant mesure ; coût temporel de la revue sous embargo |

### 2. Conditions de dominance des trois options

- **Publier avant les résultats (uniquement au format C2 assaini, jamais C4 ; C3 seulement si test de robustesse boîte blanche assumé)** est préférable si et seulement si :
  1. la validité des mesures repose uniquement sur des secrets strictement séparables du texte publié (sondes/clés scellées) et un test préliminaire vérifie que les systèmes/personnes de l'étude ne peuvent être contaminés dans la fenêtre d'exécution ;
  2. un test préalable montre qu'un adversaire lisant C2 ne gagne pas de capacité d'évasion mesurable ;
  3. un pilote technique minimal a déjà montré que le détecteur bat les vérifications mécaniques (donc le risque d'annonce d'un échec complet est borné) ;
  4. l'équipe peut exécuter et publier les mesures plus vite qu'un concurrent réagissant à C2, et la communauté du domaine accorde un crédit vérifiable aux pré-enregistrements publics.
- **Publier après les résultats (avec scellement silencieux C0 ou embargo C5 dès maintenant)** est préférable dès que l'une des conditions suivantes s'applique :
  1. aucune mesure n'est encore faite (statut `RAPPORTÉ` ici) et la viabilité empirique du détecteur reste une `HYPOTHÈSE` ;
  2. la validité des mesures dépend de l'ignorance de systèmes connectés ou de personnes susceptibles d'ingérer un texte public ;
  3. la connaissance des métriques ou du mécanisme peut instruire un adversaire avant collecte ;
  4. des concurrents mieux dotés pourraient convertir un texte court public en première publication empirique.
- **Ne rien publier (ni avant, ni après — ou limiter la diffusion à une divulgation coordonnée restreinte)** est préférable si :
  1. les mesures s'avèrent irrémédiablement contaminées ou biaisées (publier des résultats invalides nuit à la connaissance ; seule une note méthodologique sur l'échec du contrôle est défendable si elle n'arme pas l'adversaire) ;
  2. le détecteur sert une défense active dont l'efficacité dépend durablement du secret opérationnel et la publication même *a posteriori* enseigne un contournement sans remède ni bénéfice scientifique proportionné.

### 3. Vérifications indépendantes de l'équipe

Parce que le contrefactuel d'une étude unique est inobservable (`HYPOTHÈSE` d'impossibilité de mesure directe sur un cas isolé), une vérification indépendante sérieuse repose sur quatre audits observables conduits par des tiers :
1. **Audit cryptographique d'antériorité et de fidélité au protocole** : vérification mécanique de l'empreinte `SHA-256` et du jeton `RFC 3161` (C0/C5) comparés au manuscrit final, afin de distinguer la preuve datée des hypothèses de toute réécriture *post hoc*.
2. **Audit de contamination par sondes canaris** : mesure par un tiers de l'apparition ou de l'influence d'éléments issus du texte publié dans les systèmes ciblés ou chez des participants recrutés indépendamment.
3. **Audit adversarial en aveugle (équipe rouge indépendante)** : comparaison du taux d'évasion obtenu par des attaquants recevant ou non le texte court, à budget fixé.
4. **Évaluation en aveugle de l'attribution scientifique** : panel de pairs externes notant, dates et auteurs masqués, la part de contribution substantiellement anticipée par le texte court face aux travaux voisins parus entre-temps.

### 4. Argument le plus fort pour chaque option, choix et conditions de révision

- **Argument le plus fort pour « publier avant »** : un pré-enregistrement public de type C2 (protocole sans secrets) lie les mains de l'équipe avant toute donnée, élimine le soupçon d'ajustement *post hoc* des seuils, expose les failles méthodologiques à une critique large avant d'engager le coût des mesures et constitue une trace datée publique susceptible de favoriser la coordination plutôt que la duplication stérile.
- **Argument le plus fort pour « publier après » (avec C0/C5 silencieux)** : tant qu'aucune mesure n'existe, l'asymétrie entre les gains incertains d'un billet public (crédit d'antériorité non établi, dissuasion ambiguë) et ses coûts potentiellement irréversibles (contamination des mesures, apprentissage adversarial, accélération d'un concurrent plus rapide, risque réputationnel si le détecteur échoue) est défavorable ; le scellement cryptographique C0 ou l'embargo C5 capture la preuve d'antériorité et la discipline méthodologique sans exposer aucun secret.
- **Argument le plus fort pour « ne rien publier »** : lorsque l'utilité d'un dispositif de détection face à un adversaire actif repose sur des asymétries d'information non remplaçables ou que les mesures révèlent une vulnérabilité exploitable sans contre-mesure, l'abstention de publication évite d'invalider l'instrument et de détériorer l'équilibre défensif.

**Choix (Proposition F)** : **publier après les résultats**, en procédant immédiatement à un **scellement cryptographique horodaté silencieux (C0)** du protocole complet (hypothèses, seuils, contrôles et éléments secrets), idéalement complété par une **revue méthodologique fermée sous embargo (C5)** avant la collecte des données. Ne publier aucun texte court substantiel (C1–C4) avant les mesures.

**Ce qui me ferait changer de choix** :
- *Basculer vers « publier avant » (format C2 strictement sans secrets)* uniquement si les quatre conditions suivantes sont vérifiées simultanément : (i) l'Expérience 1 ci-dessous falsifie $H_{A1}$ (aucun gain d'évasion adversarial mesurable à la lecture de C2) ; (ii) l'Expérience 2 falsifie $H_{A2}$ (aucune contamination des systèmes/cohortes dans la fenêtre d'étude) ; (iii) une mesure pilote interne montre déjà que le détecteur bat les vérifications mécaniques de la section (c) ; et (iv) l'Expérience 3 falsifie $H_{B3}$ (gain net de reconnaissance sans pénalité réputationnelle dans ce domaine).
- *Basculer vers « ne rien publier »* si l'Expérience 1 ou les mesures finales montrent qu'une divulgation même *a posteriori* réduit le taux de détection d'un outil opérationnel actif en dessous des vérifications mécaniques sans voie de correction robuste au sens de Kerckhoffs, ou si une contamination préalable irréversible invalide les mesures.

---

## (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Conformément à la règle B4, chaque expérience oppose deux hypothèses mutuellement exclusives et comporte un contrôle négatif, un contrôle positif de puissance et des issues falsificatrices symétriques. Tous les seuils, effectifs et durées sont **illustratifs**.

### Expérience 1 — Gain d'information adversarial (test d'équipe rouge en aveugle)
- **$H_{A1}$** : La lecture du texte court candidat (format C2 sans secrets, ou C3) procure à un adversaire adaptatif un gain exploitable qui abaisse sensiblement la détection.
- **$H_{B1}$** : La lecture du texte court ne confère aucun gain d'évasion au-delà de la littérature publique existante (invariance du détecteur à ce niveau de divulgation).
- **Protocole** : assignation aléatoire d'équipes rouges indépendantes (humaines et/ou agents automatisés, budget de requêtes et de temps identique) en deux bras principaux : *Exposé* (littérature publique + texte court) contre *Témoin* (littérature publique seule), évalués sur $N = 200$ (illustratif) tentatives adversariales indépendantes par bras.
- **Métrique** : baisse de sensibilité $\Delta \text{TPR} = \text{TPR}_{\text{Témoin}} - \text{TPR}_{\text{Exposé}}$ évaluée à taux de fausses alertes fixé $\text{FPR}_0 = 1\,\%$ (illustratif), avec intervalle de confiance bootstrap à $95\,\%$ (illustratif).
- **Seuil** : $\Delta \text{TPR} \ge 5$ points de pourcentage (illustratif) avec borne inférieure de l'IC à $95\,\%$ $> 0$ (illustratif) pour conclure à un gain adversarial ; borne supérieure de l'IC $< 2$ points (illustratif) pour conclure à l'invariance.
- **Contrôle négatif** : bras *Placebo* recevant un texte de même longueur et même style portant sur un sujet voisin sans information mécanique sur le détecteur (doit vérifier $|\Delta \text{TPR}_{\text{Placebo}}| < 2$ points, illustratif), complété par des cas honnêtes appariés vérifiant la stabilité de $\text{FPR}_0$.
- **Contrôle positif (puissance)** : bras recevant un texte C4 contenant des éléments secrets (doit atteindre $\Delta \text{TPR}_{\text{Pos}} \ge 20$ points, illustratif, confirmant la compétence de l'équipe rouge).
- **Issues falsificatrices** :
  - $\Delta \text{TPR} \ge 5$ points (illustratif, $\text{IC}_{95\,\%} > 0$) avec contrôle négatif dans les bornes $\Rightarrow$ **$H_{B1}$ est falsifiée** (ne pas publier ce contenu avant mesure).
  - Borne supérieure de $\text{IC}_{95\,\%}(\Delta \text{TPR}) < 2$ points (illustratif) avec contrôle positif réussi ($\ge 20$ points, illustratif) $\Rightarrow$ **$H_{A1}$ est falsifiée** pour ce niveau de contenu et ce budget d'attaque.

### Expérience 2 — Contamination des systèmes et des mesures (sondes canaris appariées)
- **$H_{A2}$** : La publication publique d'un texte court sur les canaux envisagés contamine les systèmes ciblés (via indexation web, recherche augmentée ou mise à jour) ou sensibilise des participants dans la fenêtre temporelle de l'étude ($\Delta t = 30$ jours, illustratif).
- **$H_{B2}$** : Les systèmes et cohortes de mesure restent isolés de toute publication sur ces canaux pendant $\Delta t$ (taux de contamination nul).
- **Protocole** : avant l'étude réelle, publier sur exactement les mêmes canaux publics $K = 20$ (illustratif) textes courts synthétiques contenant chacun une sonde canari unique (motif artificiel sans contenu scientifique), tout en conservant $K = 20$ (illustratif) sondes appariées strictement hors ligne. Interroger les systèmes cibles (et un échantillon pilote humain le cas échéant) à $t_0$, $t_0 + 7$ jours et $t_0 + 30$ jours (illustratif).
- **Métrique** : différence de taux de détection de contamination $\Delta R = R_{\text{pub}} - R_{\text{priv}}$ entre sondes publiées et sondes privées (mesurée par rappel verbatim, décalage de log-probabilité ou réponse comportementale spécifique sur tâche piège).
- **Seuil** : $\Delta R \ge 5\,\%$ (illustratif, soit au moins $1$ sonde publiée sur $20$ détectée exclusivement côté publié au seuil $p < 0{,}01$, illustratif, au test exact de Fisher).
- **Contrôle négatif** : (i) les $K = 20$ sondes privées évaluées sur les mêmes systèmes ; (ii) les $K = 20$ sondes publiées évaluées sur un modèle ouvert figé hors ligne dont la date de coupure précède l'expérience (doit donner $\Delta R = 0\,\%$, illustratif).
- **Contrôle positif** : injection directe d'une sonde synthétique dans le contexte ou l'index local d'un système test (doit donner $R_{\text{pos}} \ge 90\,\%$, illustratif).
- **Issues falsificatrices** :
  - $\Delta R \ge 5\,\%$ (illustratif) sur les systèmes/cohortes cibles avec $\Delta R = 0\,\%$ sur le modèle figé $\Rightarrow$ **$H_{B2}$ est falsifiée** (le canal de publication compromet la validité des mesures).
  - $\Delta R = 0\,\%$ (borne supérieure de l'IC à $95\,\%$ $< 5\,\%$, illustratif) sur les cibles avec contrôle positif $\ge 90\,\%$ (illustratif) $\Rightarrow$ **$H_{A2}$ est falsifiée** pour ce canal et cette fenêtre $\Delta t$ (sans préjuger d'une fenêtre plus longue).

### Expérience 3 — Effet du texte court sur la reconnaissance ultérieure (vignettes randomisées en aveugle)
- **$H_{A3}$** : Un texte court (C1 ou C2) publié avant les résultats augmente la reconnaissance d'antériorité accordée par les pairs lorsqu'un autre groupe publie ses résultats empiriques en premier.
- **$H_{B3}$** : Sans résultats empiriques, un texte court ne procure aucun gain net de reconnaissance (ou induit une pénalité réputationnelle face au premier groupe publiant des mesures).
- **Protocole** : essai contrôlé randomisé auprès de $N = 120$ (illustratif) chercheurs du domaine recrutés en aveugle, évaluant des paires réalistes anonymisées (Équipe 1 + Équipe 2 publiant des résultats empiriques) en manipulant aléatoirement l'existence d'un document préalable de l'Équipe 1 : aucun / C0 révélé *a posteriori* / C1 / C2.
- **Métrique** : variation de la proportion de pairs attribuant un crédit d'antériorité substantiel à l'Équipe 1 ($\Delta P_{\text{crédit}}$) et variation du score de réputation perçue (échelle ordinale $1$ à $5$, illustratif).
- **Seuil** : $\Delta P_{\text{crédit}} \ge +15$ points de pourcentage (illustratif, $p < 0{,}01$ illustratif) sans baisse de réputation $> 0{,}3$ point (illustratif).
- **Contrôle négatif** : vignette où le texte court de l'Équipe 1 porte sur un mécanisme différent dans le même domaine (vérifie que les évaluateurs ne créditent pas automatiquement tout billet antérieur).
- **Contrôle positif** : vignette où l'Équipe 1 publie des résultats préliminaires empiriques vérifiés avant l'Équipe 2 (doit produire $\Delta P_{\text{crédit}} \ge +40$ points, illustratif).
- **Issues falsificatrices** :
  - $\Delta P_{\text{crédit}} \le 0$ ou baisse réputationnelle $\ge 0{,}3$ point (illustratif) $\Rightarrow$ **$H_{A3}$ est falsifiée**.
  - $\Delta P_{\text{crédit}} \ge +15$ points (illustratif) sans pénalité réputationnelle, contrôle négatif $\le 5$ points (illustratif) $\Rightarrow$ **$H_{B3}$ est falsifiée**.

### Expérience 4 — Gain de qualité méthodologique : publication publique (C2) contre revue fermée sous embargo (C5)
- **$H_{A4}$** : La publication publique de C2 fait détecter des défauts méthodologiques critiques qui échappent à une revue fermée sous embargo (C5), justifiant le risque d'exposition.
- **$H_{B4}$** : Une revue fermée structurée sous confidentialité capture la quasi-totalité des défauts critiques identifiables avant mesure, à bruit critique inférieur ou égal et sans exposer le projet à un devancement.
- **Protocole** : plan croisé sur $M = 12$ (illustratif) protocoles d'études de détection anonymisés dans lesquels des défauts critiques calibrés ont été injectés (*error-seeding* : fuite de données, contrôles non appariés, biais de sélection), soumis en parallèle à une revue fermée ($n = 4$ relecteurs experts sous confidentialité, illustratif) et à un dépôt public court ouvert aux commentaires ($30$ jours, illustratif).
- **Métrique** : différence du taux de détection des défauts critiques injectés $\Delta D = D_{\text{public}} - D_{\text{privé}}$ et taux de fausses critiques coûteuses à traiter (FPR sur protocoles sains).
- **Seuil** : $\Delta D \ge +20$ points de pourcentage (illustratif) sans augmentation du taux de fausses critiques $> 10$ points (illustratif).
- **Contrôle négatif** : protocoles exempts de défauts injectés (mesurent le taux de faux défauts / surcoût de traitement dans chaque canal).
- **Contrôle positif** : protocole contenant une erreur statistique grossière (doit être détectée à $\ge 90\,\%$ dans les deux canaux, illustratif).
- **Issues falsificatrices** :
  - $\Delta D < 5$ points (illustratif) ou surcroît de fausses critiques $> 10$ points en public $\Rightarrow$ **$H_{A4}$ est falsifiée** (C5 domine).
  - $\Delta D \ge +20$ points (illustratif) à faux positif maîtrisé $\Rightarrow$ **$H_{B4}$ est falsifiée** (avantage qualitatif réel du canal public, à mettre en balance avec les Expériences 1 et 2).

---

## (c) Mesure minimale de fonctionnement pour chaque instrument nommé dans la question

La question nomme explicitement trois classes d'instruments : (1) le **dispositif de détection contre un adversaire** (dont l'implémentation concrète n'est pas spécifiée dans `FAITS`, `VÉRIFIÉ`), (2) le **texte court avant résultats (« billet-drapeau »)** en tant qu'instrument de pré-engagement et de signalement, et (3) les **vérifications indépendantes de l'équipe**, déclinées en deux instruments distincts : **détecteur de contamination/fuite** (3a) et **banc d'audit du gain adversarial** (3b). Tous les seuils numériques ci-dessous sont **illustratifs**.

| Instrument nommé | Mesure minimale : taux de détection (TPR) et de fausses alertes (FPR) | Cas honnêtes appariés (contrôles négatifs) | Vérifications mécaniques à battre |
|---|---|---|---|
| **1. Dispositif de détection contre un adversaire** | $\text{TPR}_{\text{naïf}}$ et surtout $\text{TPR}_{\text{adapt}}$ (adversaire informé du texte public envisagé) $\ge 70\,\%$ à $\text{FPR} \le 1\,\%$ (ou $\le 0{,}1\,\%$ en haut volume, illustratif) ; perte sous divulgation $\Delta\text{TPR} \le 5$ pts ; gain $\ge +10$ pts au-dessus du meilleur contrôle mécanique (illustratif). | Cas authentiquement non adversariaux strictement appariés sur toutes les covariables de surface (longueur, langue, domaine, date, famille de système/niveau humain, latence) + cas honnêtes difficiles (*hard negatives* : bruités, paraphrasés ou atypiques mais bénins). | (i) Correspondance exacte, expressions régulières et signatures statiques ; (ii) statistiques univariées simples (longueur, entropie, perplexité brute d'un petit modèle figé) ; (iii) régression logistique sur TF-IDF/n-grammes ou métadonnées seules ; (iv) permutation aléatoire des étiquettes. |
| **2. Texte court avant résultats (« billet-drapeau »)** | **TPR d'attribution** : taux auquel un jury indépendant aveugle aux dates reconnaît une antériorité substantielle sur le mécanisme revendiqué ($\ge 80\,\%$, accord $\kappa \ge 0{,}70$, illustratif) + taux de détection des déviations majeures protocole/manuscrit ($\ge 85\,\%$, illustratif). **FPR (« drapeau flou »)** : attribution abusive d'antériorité sur des travaux honnêtes distincts ($\le 5\,\%$, illustratif). | Travaux voisins indépendants publiés dans la même période et le même domaine, partageant le vocabulaire général mais utilisant des hypothèses, métriques ou mécanismes de détection différents. | (i) Scellement cryptographique muet **C0** (`SHA-256` + `RFC 3161`, vérification d'intégrité déterministe et fuite nulle) ; (ii) similarité lexicale mécanique (BM25 / cosinus TF-IDF entre texte court et articles ultérieurs) ; (iii) dépôt privé horodaté sous embargo (**C5**). |
| **3a. Vérification indépendante de contamination / fuite (sondes canaris)** | **TPR** : détection d'expositions réellement injectées ($\ge 90\,\%$ en exposition directe, $\ge 60\,\%$ après paraphrase, illustratif). **FPR** : fausses alertes de contamination sur cibles isolées ($\le 1\,\%$, illustratif). | Sondes privées jamais publiées de même longueur et perplexité ; modèles ouverts figés hors ligne (date de coupure antérieure) et cohortes humaines isolées appariées sur la tâche et l'expertise. | Recherche exacte de sous-chaînes et n-grammes (`grep` / index inversé / hachage de fenêtres) et audit mécanique des journaux réseau, caches web et dates de coupure déclarées. |
| **3b. Vérification indépendante du gain adversarial (audit d'équipe rouge)** | **TPR** : détection d'une fuite exploitable lorsque le texte contient un indice ou une vulnérabilité calibrée ($\ge 85\,\%$, illustratif). **FPR** : conclusion erronée à un gain adversarial sur un texte placebo ($\le 5\,\%$, illustratif). | Textes courts placebos de longueur, structure et lexique identiques sans information mécanique sur le détecteur, soumis aux mêmes équipes rouges avec budget et consignes identiques. | (i) Perturbations aléatoires / paraphrases génériques sans lecture du texte court (attaque aveugle) ; (ii) analyse statique mécanique par liste noire (vérification qu'aucun identifiant de sonde, seuil numérique ou règle exacte ne figure dans le texte). |

*Critère de rejet commun* : tout instrument qui ne bat pas ses vérifications mécaniques sur les cas honnêtes appariés, ou dont le FPR dépasse la cible sur les contrôles appariés, doit être considéré comme non fonctionnel avant toute décision fondée sur ses sorties.

---

## (d) Ancrage matériel : modèles ouverts, calcul nécessaire et coût estimé

L'ancrage matériel ci-dessous instancie les vérifications mécaniques de (c) et les Expériences 1 et 2 sur des **modèles à poids ouverts** exécutables hors ligne (condition nécessaire pour le contrôle négatif sans contamination réseau). Il ne se substitue pas aux coûts propres au domaine inconnu de l'étude (ex. recrutement humain ou systèmes propriétaires). **Toutes les quantités, volumes de calcul et coûts ci-dessous sont marqués « illustratif ».**

### 1. Scellement cryptographique (C0) et vérifications mécaniques de base
- **Outils ouverts** : `OpenSSL` / `sha256sum`, horodatage `RFC 3161`, `scikit-learn` (régression logistique + TF-IDF), `ripgrep` / `FAISS`, et petit modèle ouvert de perplexité (`Qwen2.5-1.5B` ou `Llama-3.2-1B`, $\approx 1$ à $1{,}5$ milliard de paramètres, illustratif).
- **Calcul nécessaire** : $< 1$ seconde CPU pour le scellement C0 (illustratif) ; $2$ à $5$ heures sur $1$ station CPU ($16$ cœurs, illustratif) ou $1$ GPU $24$ Go VRAM (illustratif) pour l'ensemble des vérifications mécaniques.
- **Coût estimé** : $0$ € pour C0 (illustratif) ; $< 10$ € en location GPU à la demande (illustratif).

### 2. Banc ouvert pour les Expériences 1 (équipe rouge adaptative) et 2 (sondes canaris et contamination contrôlée)
- **Modèles ouverts** (deux familles distinctes pour contrôler les artefacts de famille, exécutés localement via `vLLM` ou `llama.cpp`) :
  - *Niveau intermédiaire (red-teaming rapide et contrôle positif LoRA)* : `Qwen2.5-7B-Instruct` et `Llama-3.1-8B-Instruct` ($\approx 7$–$8$ milliards de paramètres, illustratif).
  - *Niveau capacité élevée (simulation d'un adversaire plus fort)* : `Qwen2.5-72B-Instruct` et `Llama-3.1-70B-Instruct` ($\approx 70$–$72$ milliards de paramètres, illustratif, inférence en FP8 ou quantification $4$ bits).
  - *Encodeur ouvert pour banc RAG / similarité (Expérience 2 et baseline lexicale/sémantique)* : `BGE-M3` couplé à un index local `FAISS`.
- **Calcul nécessaire (illustratif)** :
  - *Expérience 1* : $4$ conditions (Témoin, Exposé, Placebo, Contrôle positif) $\times$ $200$ essais $\times$ $5$ tours d'adaptation $= 4\,000$ épisodes (illustratif), soit $\approx 8 \times 10^6$ tokens générés par famille (illustratif). Cela représente $\approx 8$–$12$ heures-GPU A100 $80$ Go sur modèle $7$–$8$B (illustratif), et $\approx 60$–$140$ heures-GPU H100/A100 $80$ Go sur modèle $70$–$72$B sur $2$ familles (illustratif).
  - *Expérience 2* : $40$ sondes canaris $\times$ $3$ dates $\times$ $5$ configurations (modèle figé, RAG local, contrôle positif par adaptation LoRA légère sur modèle $7$–$8$B) : $\approx 5$–$10$ heures-GPU A100 $80$ Go (illustratif).
- **Coût estimé (base cloud $2$ à $4$ €/heure-GPU A100/H100, illustratif)** :
  - *Configuration minimale reproductible* (modèles $7$–$8$B + baselines + Expérience 2) : $\approx 15$–$25$ heures-GPU, soit **$40$–$100$ €** (illustratif).
  - *Configuration complète* (incluant red-teaming $70$–$72$B sur $2$ familles ouvertes) : $\approx 90$–$180$ heures-GPU, soit **$250$–$750$ €** (illustratif).

### 3. Ancrage humain des vérifications indépendantes (Expériences 3 et 4, embargo C5)
- **Expérience 3** ($N = 120$ chercheurs du domaine, $\approx 15$ minutes par participant, valorisation/dédommagement $20$–$40$ €/participant, illustratif) : **$2\,400$–$4\,800$ €** (illustratif) si rémunéré, ou coût temps académique équivalent d'environ $30$ heures cumulées (illustratif).
- **Revue fermée sous embargo C5 / Expérience 4** ($4$ relecteurs experts, $2$–$4$ heures chacun, illustratif) : $0$ € en réciprocité académique (illustratif) ou **$1\,000$–$3\,000$ €** en audit externe rémunéré (illustratif).
- **Coût interne comparatif de décision** : $< 1$ heure-chercheur pour sceller C0 sur un protocole existant (illustratif), contre $15$–$30$ heures-chercheur pour rédiger, assainir et auditer un texte public C2 (illustratif) — hors coût d'une éventuelle refonte des mesures en cas de fuite.

FIN-DE-CELLULE