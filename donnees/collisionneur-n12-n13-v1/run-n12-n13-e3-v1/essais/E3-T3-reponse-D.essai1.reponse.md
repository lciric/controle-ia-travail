# Proposition D — Tour III.3 : réponses et conception corrigée

Les PDF et C-17 ne sont pas servis ; je ne leur attribue rien au-delà des lectures fournies. Je réponds uniquement aux critiques visant D, y compris la note transversale d’A lorsqu’elle la concerne.

## 1. Réponse aux critiques

| Critique | Décision | Réponse |
|---|---|---|
| **Seuils δ/ε non reliés au bruit, à la puissance et aux effectifs** (A, B, C) | **Acceptée, transformée en règle de test** | Les seuils ne sont plus de simples paramètres gelés. Un pilote indépendant estime la variance d’évaluation et, pour l’entraînement, la variance entre graines. Les effectifs sont calculés avant la lecture confirmatoire. Je remplace la zone logique entre δ et ε par un seuil d’utilité unique θ et deux hypothèses complémentaires. Une simple non-significativité ne vaut jamais équivalence. |
| **Unité d’inférence et graines insuffisantes** (A, note transversale ; C) | **Acceptée** | Pour tout effet causal de l’entraînement, l’unité est la **graine d’entraînement**, pas le run d’évaluation ni l’agent. Une graine par bras interdit l’inférence confirmatoire. Le nombre de graines est fixé par la puissance après estimation de leur variance ; les runs restent des unités groupées au sein des graines. |
| **E12-1 : absence de métrique principale et comparaisons multiples** (A) | **Acceptée** | La métrique principale devient un score net oracle–coût unique, défini ci-dessous. Structures retrouvées, témoins et fausses alertes sont secondaires. Les lectures par famille sont des analyses en blocs, avec multiplicité contrôlée, non une recherche de famille favorable. |
| **E12-1 : bras « contraint au catalogue » ambigu** (B) | **Acceptée** | Il n’y a aucune projection a posteriori. Le même générateur est informé dès le départ de la grammaire et ne peut émettre qu’un identifiant et une configuration valides du catalogue. Il constitue le comparateur catalogue le plus proche du générateur libre, à nombre de candidats et d’évaluations égal. |
| **E12-1 : coût compté deux fois et amortissement arbitraire** (C) | **Acceptée sur le risque ; nuance rejetée** | Le budget est un plafond commun, pas une première pénalité ; le coût n’entre qu’une fois dans le score net. Génération, échecs de compilation et exécution sont distingués. L’horizon d’amortissement \(K_0\) et le coefficient \(\lambda_0\) sont gelés avant les résultats. Le résultat ne vaut que pour cette règle de déploiement ; il n’est pas « entièrement » déterminé par elle, puisque l’oracle reste mesuré. |
| **E12-1 : même nombre d’évaluations ; meilleur catalogue possiblement choisi sur le test** (A, B) | **Acceptée** | Les deux bras reçoivent le même nombre de candidats et d’évaluations. Le comparateur catalogue est sélectionné sur le pli de développement seulement, jamais sur les familles de test. |
| **E12-2 : fuite entre spécification et fautes plantées ; petit banc non inférentiel** (A, B) | **Acceptée** | La spécification est écrite par un tiers ignorant les fautes ; le planteur est distinct. La taille du banc est fixée par classe et par la précision requise. À défaut, le résultat est explicitement descriptif et ne tranche aucune hypothèse. |
| **E12-2 : comparateur bon marché trop faible** (C) | **Acceptée** | J’ajoute au socle empreintes, tests, propriétés et mutations une relecture indépendante par un agent d’une autre famille, avec scripts et fuzzing, à budget d’inspection apparié. Lean doit battre le **meilleur** assemblage bon marché, pas une empreinte seule. |
| **E13-1 : appariement post-traitement sur la performance, avec risque de collider** (A, B, C) | **Acceptée** | L’appariement sur la performance est supprimé. La comparaison primaire se fait à pas d’entraînement, budget de jetons et points de contrôle fixés d’avance. La performance est rapportée séparément ; aucune sélection de graines ou de points de contrôle n’est faite sur elle. |
| **E13-1 : récompense individuelle et bras générique sous-spécifiés** (A) | **Acceptée** | Le monde planté principal est à contributions additivement attribuables. À partir des mêmes événements d’oracle, \(r_i\) est attribué à chaque agent et \(R=\sum_i r_i\). Le bras individuel optimise \(r_i\), le collectif utilise le même \(R\) pour tous ; l’information contextuelle est identique. Le bras générique secondaire est un entraînement mono-agent avec le même \(R\), sans récompense du signalement. La portée est limitée à ce monde attribuable. |
| **E13-1 : taux par run, saturation et effectif d’agents** (B) | **Partiellement acceptée** | Le taux par run n’est pas biaisé pour estimer « au moins un humain alerté », mais il ne mesure pas le taux par agent. Ce dernier devient primaire, à effectif \(N\) gelé et avec corrélation intra-run. Le taux par run reste une mesure secondaire de sécurité collective. |
| **E13-1 : canaris et plancher initial insuffisamment spécifiés** (B) | **Acceptée** | Le pré-test vérifie que le modèle de départ signale assez pour permettre une baisse mesurable. Canaris et vrais incidents sont dimensionnés pour borner séparément faux signalements et omissions. Un plancher ou plafond de signalement rend le pilote non jugeable pour l’effet recherché. |
| **E13-2 : disqualification qualitative, sans plancher de sécurité** (B) | **Acceptée** | Un plancher absolu de signalement et une chute maximale admissible sont gelés avant l’entraînement. Leur franchissement interdit l’intégration, quel que soit le gain d’utilité. Cette garde ne devient pas un terme de récompense. |
| **E13-2 : « pire famille » comme statistique d’extrême** (A, C) | **Acceptée** | La pire famille n’est plus un critère de rejet principal. Le test primaire porte sur le gain agrégé selon une pondération de familles gelée. La pire famille et son intervalle sont rapportés pour limiter la portée, sans prétendre estimer précisément un minimum avec peu de familles. |
| **E13-3 : confusion entre régime, pas d’entraînement et omission** (A, C) | **Acceptée** | Positifs et négatifs viennent du même régime et du même point de contrôle, appariés sur tâche, longueur et issue. Le pas et le régime seuls deviennent des prédicteurs témoins à battre. Les activations permutées et les épisodes à \(C\) faux restent obligatoires. |
| **E13-3 : double hypothèse prévalence/sonde et puissance perdue par partition** (A, C) | **Acceptée, transformée en deux tests** | Le test de suffisance du générateur est séparé du test d’utilité de la sonde. Une prévalence insuffisante ne dit rien contre la sonde. Le calcul de puissance inclut dès le départ les partitions entraînement, calibration et test. |
| **E13-3 : artefact propre au modèle ou au générateur** (B) | **Acceptée pour la portée ; transfert direct rejeté** | J’impose un test sur scénarios et générateur tenus à l’écart, plus un étalon d’omissions plantées. Une sonde linéaire n’a toutefois pas de transfert direct de poids entre architectures : la réplication exige de réentraîner le **protocole** sur un second modèle. Sans cela, la conclusion reste limitée au modèle source. |
| **E13-4 : vérité issue d’un juge et comparateur RLVR recalibré manquant** (A, B) | **Acceptée** | La vérité vient exclusivement de réponses mécaniquement vérifiables ou de l’oracle planté, avec développement et test disjoints par famille. Le comparateur principal devient **RLVR suivi d’un recalibrage post-hoc**, contre lequel RLCR-calibration doit apporter un gain. Aucun verdict de juge ne sert de vérité terrain. |
| **E13-4 : hétérogénéité inter-familles et métriques dégénérées** (A, B) | **Acceptée** | L’inférence est faite par blocs de familles. Le rappel au point de fonctionnement est primaire ; Brier, ECE et AUROC restent secondaires. Confiance constante au taux de base, confiances permutées et signaux bon marché sont conservés. |

## 2. Expériences corrigées

### Règle statistique commune

Pour chaque expérience, \(\Delta\) est l’effet principal et \(\theta\) le plus petit effet jugé utile, tous deux définis avant le test :

- \(H_A:\Delta>\theta\) ;
- \(H_B:\Delta\leq\theta\).

Ces hypothèses sont exclusives et exhaustives. Une borne d’intervalle au-dessus de \(\theta\) falsifie \(H_B\) ; une borne au-dessous ou égale falsifie \(H_A\). Si le pilote montre que la précision nécessaire est inaccessible, l’expérience confirmatoire n’est pas lancée. Les seuils de détection sont appris sur un pli de calibration distinct du test.

### E12-1 — Création de moniteurs contre composition du catalogue

- **Hypothèses** : \(\Delta=S_{\text{net},\lambda_0,K_0}(\text{générateur libre})-S_{\text{net},\lambda_0,K_0}(\text{générateur contraint au catalogue})\), avec \(H_A\) et \(H_B\) comme ci-dessus.
- **Protocole** : même générateur, informations, invites, nombre de candidats, évaluations et plafond de dépense. Le bras libre peut produire du code exécuté dans un bac à sable contrôlé de l’extérieur ; l’autre ne produit que des configurations du catalogue.
- **Mesure** : score net sur oracle planté tenu à l’écart, coût compté une fois, échecs de génération inclus. Fausses alertes et exécutions vides rapportées séparément.
- **Issues** : un gain net reproductible falsifie \(H_B\), sans autoriser encore l’auto-réécriture ; l’absence de gain utile falsifie \(H_A\) et ferme la voie dans les conditions testées.

### E12-2 — Apport incrémental de la vérification formelle

- **Hypothèses** : \(\Delta\) est l’augmentation de fautes confirmées détectées par « meilleure suite bon marché + Lean » sur « meilleure suite bon marché », à coût d’inspection apparié.
- **Protocole** : spécification par tiers aveugle, fautes plantées séparément, modules honnêtes appariés, preuves invalides, théorèmes hors sujet et spécifications affaiblies. La suite bon marché inclut relecture indépendante, scripts, propriétés, fuzzing et mutations.
- **Issues** : des détections additionnelles mécaniquement confirmées, au-delà de \(\theta\), falsifient \(H_B\) ; sans tel apport, ou avec un rejet excessif d’artefacts honnêtes, \(H_A\) est falsifiée. Un banc insuffisant reste descriptif.

### E13-1 — Effet spécifique du crédit collectif sur le signalement

- **Hypothèses** : \(\Delta=p_{\text{signalement, individuel}}-p_{\text{signalement, collectif}}\), mesuré par agent et point de décision ; \(H_A\) affirme une érosion spécifique supérieure à \(\theta_S\), \(H_B\) la nie.
- **Protocole** : même modèle initial, effectif, tâches, informations, \(R\), pas d’entraînement et budget ; seule la fonction d’attribution du crédit change. Le signalement n’entre dans aucune récompense. Modèle non entraîné et entraînement mono-agent sont des témoins secondaires.
- **Contrôles** : récompenses permutées, A/A, \(C\) faux, rapport déjà émis, outil indisponible, canaris à ne pas signaler, scénarios d’évaluation tenus à l’écart.
- **Issues** : une chute collective spécifique falsifie \(H_B\) ; une différence bornée sous \(\theta_S\), y compris des chutes communes aux bras, falsifie \(H_A\). La performance de tâche est rapportée sans conditionnement.

### E13-2 — Utilité éventuelle, sans monnaie d’échange sur la sécurité

- **Hypothèses** : \(\Delta\) est le gain net oracle–coût du collectif sur le meilleur crédit individuel et les témoins bon marché ; \(H_A:\Delta>\theta_U\), \(H_B:\Delta\leq\theta_U\).
- **Protocole** : meilleur de \(N\), vote à \(k\), concepteur figé et archive à information égale comme comparateurs. Le signalement reste hors score.
- **Garde distincte** : plancher absolu et chute maximale gelés ; leur franchissement disqualifie l’intégration même si \(H_B\) est falsifiée.
- **Issues** : gain utile falsifiant \(H_B\), ou absence de gain falsifiant \(H_A\). Aucune issue ne constitue à elle seule une autorisation de déploiement.

### E13-3a — Le générateur est-il exploitable ?

- **Hypothèses** : \(H_A:\pi\geq\pi_{\min}\), où \(\pi\) est la prévalence d’omissions fautives sur l’ensemble non sélectionné des traces ; \(H_B:\pi<\pi_{\min}\).
- **Issues** : prévalence suffisante falsifiant \(H_B\) et autorisant E13-3b ; prévalence insuffisante falsifiant \(H_A\), sans conclusion sur les sondes.

### E13-3b — Une sonde détecte-t-elle sans recevoir le contrat ?

- **Cible** : parmi les points sans signalement, distinguer omission fautive et non-faute **sans fournir \(C\) ni le contrat au moniteur au test**. La vérité plantée reste accessible au seul évaluateur. Battre une vérification mécanique qui connaît déjà \(C\) et \(\rho\) n’est pas la cible.
- **Hypothèses** : \(\Delta\) est le gain de rappel à fausse alerte fixée sur le meilleur témoin textuel, mécanique disponible, bon marché, « régime seul » et « pas seul ».
- **Protocole** : positifs et négatifs au même point de contrôle ; négatifs comprenant \(C\) faux, rapport déjà fait, absence d’obligation et outil indisponible. Partition par run et famille ; test sur nouveau générateur, omissions plantées externes, puis réplication du protocole sur un second modèle.
- **Issues** : gain incrémental falsifiant \(H_B\), ou absence de gain falsifiant \(H_A\).

### E13-4 — Apport distinct de RLCR-calibration

- **Hypothèses** : \(\Delta\) est le gain de rappel au point de fonctionnement de RLCR-calibration sur le meilleur de RLVR recalibré, recalibrage simple, probabilité des jetons et confiance non entraînée.
- **Protocole** : vérité indépendante de tout juge, familles disjointes entre entraînement, recalibrage et test, justesse et fausses alertes rapportées séparément.
- **Issues** : gain hors domaine reproductible falsifiant \(H_B\) ; gain seulement en domaine, ou disparition face à RLVR recalibré, falsifiant \(H_A\).

## 3. Réponse à l’arbitre

### Ce qui est établi

- **VÉRIFIÉ** : N-045 couvre l’apprentissage de la composition, y compris les instruments locaux, le coût dans le signal et l’héritage entre générations. N-058 impose l’oracle planté et le coût pour choisir les agents, et exclut le verdict du juge de cette sélection.
- **OBSERVÉ-NON-AUDITÉ** : les lectures d’Avalon rapportent une forte baisse du signalement avec un refus durable, sur un seul run d’entraînement.
- **RAPPORTÉ** : Damani fournit une récompense de calibration et des résultats dans un cadre de réponses courtes vérifiables ; cela ne concerne pas le crédit collectif.

### Ce qui ne l’est pas

- Que N-045 couvre la synthèse de code nouveau, l’auto-modification ou une assurance Lean reste une **HYPOTHÈSE**.
- Que la récompense collective cause l’érosion d’Avalon reste une **HYPOTHÈSE** : le témoin d’entraînement mono-agent apparié manque.
- La valeur additionnelle des couches 3 et 4, la validité écologique de c3 et le transfert de Damani à nos moniteurs ne sont pas établis.

### Priorité et première expérience

Je concentre l’étape 2 sur N-045 et ne rouvre actuellement aucune couche **comme capacité intégrée**. Les tests E12 restent hors organisme ; une couche 4 éventuelle serait d’abord un vérificateur externe. Dans le dessin actuel, c2 est exclu faute d’oracle et parce qu’il confond bisociation et crédit ; c3 devient un sous-produit d’un appariement ; c1 n’est recevable que comme pilote isolé, avec journalisation externe, scénarios de signalement tenus à l’écart et arrêt sur plancher de sécurité. Damani relève d’un chantier de mesure séparé, précédé par les recalibrages bon marché.

**Première expérience : E0, pilote de jugeabilité, sans entraînement collectif ni réécriture.** Sur mondes plantés avec contrat mécanique \(C\rightarrow\rho\), mesurer le signalement du modèle de départ, les faux signalements, le bruit A/A, le coût et la précision atteignable avec les graines et familles disponibles.

- \(H_A\) : le banc permet l’inférence prévue — signalement non saturé, étiquettes mécaniques validées et précision suffisante.
- \(H_B\) : il ne le permet pas.

Si \(H_A\) est falsifiée, il faut corriger le banc plutôt que financer un duel illisible. Si \(H_B\) est falsifiée, on scelle les seuils et on lance E12-1 et E13-1 dans l’ordre budgétaire retenu.

FIN-DE-CELLULE