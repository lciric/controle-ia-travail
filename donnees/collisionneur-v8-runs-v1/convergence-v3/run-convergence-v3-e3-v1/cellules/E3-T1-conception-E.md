# Proposition E — Séparer convergence, stabilité et robustesse

**OBSERVÉ-NON-AUDITÉ — Pièces manquantes :** le PDF de Bailey et collègues, le pilote complet et les entrées `resultats` du calibrage ne sont pas servis ; je n’en reconstruis pas le contenu.

**Convention.** Les résultats numériques transmis restent **RAPPORTÉS**, même lorsqu’une pièce rapporte leur vérification. Les protocoles proposés sont **HYPOTHÈSES** ; leurs nouveaux budgets et seuils sont **illustratifs**. Les déductions mathématiques explicitement démontrées ci-dessous sont **VÉRIFIÉES**, sans constituer une vérification des exécutions.

## A. Ce que la question suppose sans l’établir

| Statut | Présupposé à contester |
|---|---|
| **RAPPORTÉ** | A utilise bien l’historique uniforme, et non la dernière attaque seulement. Le code servi inclut également la loi cible dans cet historique. |
| **HYPOTHÈSE** | « A cycle » au sens dynamique. Les valeurs rapportées établissent des retours angulaires au-delà d’un modèle nul d’échangeabilité, pas une orbite périodique ni une non-convergence asymptotique. |
| **HYPOTHÈSE** | Les optimisations constituent de véritables meilleures réponses. Le défenseur optimise un substitut lissé ; pour les scores non linéaires, son seuil d’entraînement est approché. Les attaquants sont locaux. |
| **HYPOTHÈSE** | L’absence de progrès entre deux fenêtres sur huit tours signifie non-convergence. Une défense peut converger vers une valeur faible ; inversement, une valeur constante peut accompagner des stratégies oscillantes. |
| **HYPOTHÈSE** | La pureté forcée dans la matrice finale prouve un « plafond de classe ». Elle concerne les moniteurs et attaques effectivement ajoutés, pas tous les éléments de leurs classes. |
| **HYPOTHÈSE** | B′−D identifie l’effet du tirage aléatoire. Les pièces signalent elles-mêmes des différences de sélection, d’entraînement et de trajectoire de capacité. |
| **HYPOTHÈSE** | Un résultat connu sur le jeu fictif bilatéral ou les gradients explique directement A. A n’applique ni le premier ni les seconds. |
| **HYPOTHÈSE** | Les conclusions synthétiques se transfèrent aux sondes d’activations. Aucun résultat correspondant sur un modèle de langage n’est établi par les pièces servies. |

**VÉRIFIÉ — Point logique central.** La pureté d’un optimum restreint n’implique pas la dominance du moniteur retenu sur chaque attaque, encore moins son optimalité dans la classe complète.

## B. Formalisation et cible de convergence

### Le jeu autorisé par les pièces

**VÉRIFIÉ — Définition mathématique à partir du monde décrit.**

Pour une instance et un budget \(\delta\), soient :

- \(P_0\), la loi propre ;
- \(\Theta_\delta\), les paramètres admissibles des mélanges gaussiens ;
- \(\mathcal M_\alpha\), une classe de moniteurs munis de seuils respectant la contrainte de fausses alertes ;
- \(u(m,\theta)=\Pr_{X\sim Q_\theta}[m(X)>t_m]\).

Le défenseur maximise \(u\), l’attaquant minimise \(u\) : **ce jeu est à somme nulle** si aucun autre coût n’est ajouté. Pour des distributions de stratégies \(p,q\),

\[
u(p,q)=\mathbb E_{m\sim p,\theta\sim q}u(m,\theta).
\]

La règle idéalisée de A est :

\[
\theta_t\in\arg\min_\theta u(m_{t-1},\theta),\qquad
m_t\in\arg\max_{m\in\mathcal M_\alpha}
u\!\left(m,\operatorname{Unif}\{\theta_0,\ldots,\theta_t\}\right).
\]

C’est une dynamique asymétrique de réponses : apprentissage sur historique côté défenseur, réponse au dernier déploiement côté attaquant. Ce n’est pas le jeu fictif bilatéral.

**OBSERVÉ-NON-AUDITÉ — Lecture statique du code.** L’exécution remplace les argmax/argmin par des optimisations approchées, utilise des échantillons finis et calibre les seuils après entraînement. L’écart au jeu idéalisé doit donc être mesuré, pas absorbé dans le mot « oracle ».

**VÉRIFIÉ — Fausses alertes.** Maximiser la détection sous une contrainte de fausses alertes reste un objectif classique de jeu contraint. La difficulté supplémentaire vient ici du seuil estimé, du substitut d’entraînement et d’une éventuelle modification de l’ensemble admissible entre tours.

### Mesurer quoi ?

**VÉRIFIÉ — Certificat pertinent.** Pour un profil \((p,q)\), définir :

\[
g(p,q)=\sup_{m\in\mathcal M_\alpha}u(m,q)
       -\inf_{\theta\in\Theta_\delta}u(p,\theta).
\]

Ce gap de selle est nul à un équilibre lorsqu’il existe. Il permet de distinguer :

- le **dernier profil** ;
- le **profil empirique moyen** ;
- le **profil du jeu restreint**.

Ces trois objets ne sont pas interchangeables.

**VÉRIFIÉ — Limite des oracles locaux.** Une réponse défensive trouvée donne une borne inférieure au supremum ; une réponse offensive trouvée donne une borne supérieure à l’infimum. Leur différence ne fournit donc pas, seule, une borne supérieure certifiée sur \(g\). Un petit gap local n’atteste pas un petit gap global.

**HYPOTHÈSE — Tableau de bord proposé.**

1. Gap certifié sur jeu fini ; gap **restreint ou empirique**, explicitement nommé, ailleurs.
2. Détection robuste de la défense finale, à fausses alertes contrôlées.
3. Désaccord fonctionnel entre moniteurs sur une banque fixe tenue à l’écart.
4. I1 et I3 comme descriptifs secondaires.

**VÉRIFIÉ — Pourquoi pas la distance des poids ?** Une multiplication positive du score et du seuil laisse la décision inchangée ; des permutations d’unités peuvent également préserver une fonction. Une distance paramétrique brute peut ainsi signaler un changement inexistant au niveau des décisions.

**HYPOTHÈSE — Transfert.** Le désaccord fonctionnel et la détection sur une banque d’évaluations sont directement mesurables sur des sondes réelles. Une NashConv globale ne l’est pas sans caractérisation et résolution des deux espaces de stratégies.

## C. Expériences discriminantes

### Règle commune de décision

**HYPOTHÈSE — Préenregistrement proposé.** Pour chaque quantité \(Z\), opposer les hypothèses exclusives \(H_A:Z>m\) et \(H_B:Z\le m\). Employer des intervalles simultanés appariés :

- borne inférieure \(>m\) : falsifie \(H_B\) ;
- borne supérieure \(\le m\) : falsifie \(H_A\) ;
- intervalle traversant \(m\) : **non tranché**, jamais victoire par défaut.

Réutiliser \(m=0,02\), marge provenant des faits, exige une justification pour chaque nouvelle métrique. Aucun test fini ne prouvera une convergence asymptotique.

### Expérience « mesure ou dynamique ? »

**HYPOTHÈSE — Duel.**

- \(H_A\) : à horizon fixé, le gap du dernier profil dépasse la tolérance.
- \(H_B\) : il ne la dépasse pas.

**Mesure et seuil :** gap exact d’abord sur jeu fini ; seuil **illustratif** \(0,02\). Enregistrer séparément I3 et le gap des moyennes empiriques.

**Contrôle négatif :** jeu possédant un point selle strict pur ; contrôle complémentaire par déplacements échangeables pour I3.

**Réfutations :** gap sous tolérance avec I3 élevé réfute l’usage d’I3 comme preuve suffisante de non-convergence ; gap élevé réfute l’interprétation « seulement une métrique de retours trompeuse » dans ce jeu.

### Expérience « plafond de classe ou bibliothèque incomplète ? »

**HYPOTHÈSE — Duel.** Sur les tâches rapportées pures, définir le gain d’une extension défensive indépendante, à classe inchangée et budget de recherche préfixé :

- \(H_A\) : ce gain robuste dépasse \(0,02\) ;
- \(H_B\) : il ne le dépasse pas.

**Mesure :** différence de détection sous une même batterie adverse indépendante, avec seuils recalibrés sur les mêmes données propres.

**Contrôle négatif :** réinsérer des copies exactes des moniteurs existants.

**Réfutations :** un gain établi falsifie le « plafond » allégué ; son exclusion falsifie l’hypothèse d’un gain de cette ampleur accessible à cette procédure. **Elle ne certifie pas le plafond global.**

### Mécanismes : tests les moins chers

**HYPOTHÈSE — Plan commun.** Pour chaque intervention ci-dessous, \(Z\) est la réduction du gap face au témoin, à horizon et budget préfixés. Duel \(H_A:Z>0,02\) contre \(H_B:Z\le0,02\). Les deux issues falsifient respectivement l’absence ou la présence d’un effet d’intérêt. Sur le synthétique, un résultat ne vaut que pour le gap opérationnel disponible, sauf certification supplémentaire.

| Intervention | Condition nécessaire à l’argument de convergence | Prix et contrôle négatif |
|---|---|---|
| **Historique bilatéral** | Jeu fini à somme nulle, réponses exactes ; viser les stratégies empiriques, pas nécessairement les derniers itérés. | Conservation de l’historique des deux côtés. Comparer à A ; témoin négatif : répéter des éléments sans modifier leurs poids effectifs. |
| **Historique pondéré** | Aucune garantie générique par la seule pondération ; règle et objectif doivent être précisés. | Peut sacrifier la couverture ancienne ou récente. Comparer uniforme et pondéré sur la même banque, puis séparer l’effet de trajectoire. |
| **Double oracle / PSRO** | Double oracle exact : recherche des stratégies manquantes et arrêt sur gap certifié. PSRO approché : pas de garantie héritée automatiquement. | Matrice croissante et entraînements supplémentaires. Contrôle : ajout de stratégies dupliquées. |
| **Distillation, ancrage, moyenne de poids, entropie** | Définir l’espace régularisé et le jeu éventuellement modifié. Lisser une trajectoire ne garantit pas sa robustesse. | Biais vers le passé ; coût de stockage/distillation. Contrôle : coefficient nul ; enregistrer détection récente et gap non régularisé. |
| **Extragradient / optimisme** | Opérateur monotone ou structure convexe-concave appropriée, gradients et pas contrôlés. Les moniteurs paramétrés ne satisfont pas automatiquement cela. | Appels supplémentaires au gradient. Commencer sur les simplexes du jeu fini ; contrôle à même nombre d’appels, sans correction prédictive. |
| **Classe élargie** | Peut améliorer l’approximation du meilleur défenseur ; ne garantit pas la convergence de la règle d’apprentissage. | Calcul et capacité déployée accrus. Contrôle : unités supplémentaires contraintes à dupliquer une unité existante. |
| **Pire cas historique / DRO / regret** | Pire cas : ensemble d’incertitude explicite. Regret : garanties des deux joueurs pour conclure sur les moyennes en somme nulle. | Conservatisme et coût interne. Contrôle : ensemble d’incertitude réduit à la distribution uniforme historique. |

**HYPOTHÈSE — Séparation causale minimale.** Geler d’abord une même banque d’attaques pour comparer pondérations et objectifs. Puis rouvrir la boucle pour mesurer les effets dynamiques. Sinon, une différence finale confond l’apprentissage et les données qu’il a lui-même suscitées.

**HYPOTHÈSE — Garde obligatoire.** Un gap réduit par régularisation mais accompagné d’une baisse de détection des cas récents supérieure à \(0,02\), marge reprise des faits, sera rapporté comme compromis, pas comme amélioration sans réserve.

### Pourquoi le cycle n’est pas « inévitable »

**VÉRIFIÉ.** Un équilibre strict pur fournit un contre-exemple à toute affirmation d’inévitabilité générale. Inversement, dans un jeu fini sans équilibre pur, une règle qui déploie uniquement des stratégies pures ne peut converger vers un point selle pur inexistant. Cela ne démontre ni périodicité ni convergence des fréquences.

**HYPOTHÈSE.** Dans A, la restriction linéaire, les réponses au dernier moniteur, le bruit et les changements de meilleure réponse à l’historique peuvent chacun expliquer des oscillations. « Oubli catastrophique » est particulièrement prématuré puisque les anciennes attaques restent dans l’entraînement et que I2 ne sépare pas oubli et saturation.

## D. Jeu jouet : protocole en cinq lignes

**HYPOTHÈSE — Protocole ; budget et tolérance nouveaux illustratifs.**

1. Charger sans modification le jeu pile-ou-face apparié d’OpenSpiel, épingler version, matrice et conventions de gains ; vérifier algébriquement l’équilibre uniforme.
2. Exécuter réponse à la dernière stratégie, règle asymétrique de A et jeu fictif bilatéral ; figer la règle de départage et viser \(10\,000\) itérations, illustratif.
3. Calculer gap du dernier profil et des moyennes avec l’outil public disponible, puis avec une énumération indépendante ; Gambit sert de contre-vérification de l’équilibre.
4. Duel : gap empirique final \(\le0,02\) contre \(>0,02\), seuil illustratif ; chaque issue réfute l’autre, sans assimiler convergence empirique et convergence du dernier profil.
5. Contrôles : point selle strict pur, puis profil volontairement déséquilibré ; refuser l’instrument si le premier paraît exploitable ou si le second paraît à l’équilibre.

## E. Rendre le mélange réellement testable à classe égale

**VÉRIFIÉ — Critère plus fort que la non-pureté du solveur.** Pour une matrice \(G\), comparer

\[
v_{\rm mix}=\max_p\min_j(p^\top G)_j,\qquad
v_{\rm pur}=\max_i\min_jG_{ij}.
\]

Si \(v_{\rm mix}>v_{\rm pur}\), aucune stratégie pure n’atteint la valeur mixte dans ce jeu restreint.

**HYPOTHÈSE — Duel de posabilité.**

- \(H_A:v_{\rm mix}-v_{\rm pur}>0,02\) ;
- \(H_B:v_{\rm mix}-v_{\rm pur}\le0,02\).

Contrôle négatif : matrice avec ligne dominante. Pour des gains estimés, utiliser des bornes simultanées et réestimer sur données fraîches. Une matrice connue à équilibre intérieur strict constitue le contrôle positif.

**VÉRIFIÉ — Réserve.** Agréger plusieurs tâches change le jeu si la défense ne peut plus adapter ses poids à la tâche. Il faut préciser qui observe la tâche et quand. Un équilibre intérieur obtenu en cachant cette information ne démontre pas la nécessité du mélange lorsque cette information est disponible.

## F. Validation minimale des instruments

**HYPOTHÈSE — Mesure commune pour les détecteurs.** Rapporter sensibilité et fausses alertes à seuil gelé, sur partitions séparées d’entraînement, calibration et test. Cible proposée : \(\alpha=0,01\), provenant des faits ; gain minimal sur le meilleur témoin mécanique : \(0,02\), marge également reprise des faits.

| Instrument | Cas honnêtes appariés et vérification à battre |
|---|---|
| **Sonde linéaire, non linéaire, ensemble ou mélange** | Même tâche, difficulté, longueur et résultat mécaniquement vérifiable ; seuls les labels de conformité diffèrent. Comparer aux règles déterministes disponibles : schéma, assertions, tests de résultat, droits et provenance. |
| **Distillation / moyenne de poids / ancrage** | Mesurer aussi fidélité au professeur sur cas propres, puis sensibilité et fausses alertes après recalibration. Battre le moniteur non régularisé et le simple maintien du meilleur ancien moniteur. |
| **PSRO, double oracle, historique, DRO, gradients corrigés** | Ce sont des règles d’entraînement, pas des détecteurs. Évaluer leurs sorties avec le même protocole ; ajouter gap, budget et perte sur les cas récents. |
| **I3 et désaccord fonctionnel** | Sensibilité aux trajectoires cycliques connues, faux positifs sur trajectoires convergentes, stationnaires bruitées et échangeables. Comparer au calcul mécanique du gap exact, pas seulement à leur propre modèle nul. |
| **OpenSpiel, Gambit, calcul de gap** | Ce sont des solveurs : « détection » signifie identifier un profil exploitable. Faux signal sur équilibre exact, détection sur profil perturbé ; comparaison à l’énumération des stratégies. |

**HYPOTHÈSE — Labels réels.** Employer des tâches instrumentées non dangereuses dont la conformité est décidée extérieurement au modèle. Des explications textuelles convaincantes ne doivent pas servir de vérité terrain.

## G. Ancrage matériel et sources

### Calcul

**RAPPORTÉ.** Le pilote synthétique utilise le processeur. Les pièces projettent, pour la décision à \(N=100\), environ **202 minutes processeur**, auxquelles s’ajoute l’audit. Le délai mural dépend fortement de la contention ; la vérification conteste la suffisance du délai initial.

**HYPOTHÈSE — Devis illustratif.**

- Jeux finis et tests des instruments : ordinateur portable, **moins d’une heure**, estimation illustrative.
- Transfert : candidats à poids ouverts **Qwen2.5-7B-Instruct** et **Mistral-7B-Instruct-v0.3**, versions, licences et compatibilité à vérifier avant choix.
- Première étude : modèle gelé, activations mises en cache, **2 000 paires** et **8 tours**, budget illustratif ; aucune mise à jour du modèle de langage.
- Extraction et évaluation : **8–24 heures GPU** sur un GPU de **48 Go**, estimation illustrative à remplacer par une mesure sur lot pilote.
- À **1–3 € par heure GPU**, hypothèse tarifaire illustrative : **8–72 €**, hors stockage et temps humain.

### Références et transfert publié

**RAPPORTÉ — Références bibliographiques attribuables, non vérifiées sur PDF ici :**

- Julia Robinson, **1951**, *An Iterative Method of Solving a Game*.
- H. Brendan McMahan, Geoffrey J. Gordon et Avrim Blum, **2003**, *Planning in the Presence of Cost Functions Controlled by an Adversary*.
- Marc Lanctot et collègues, **2017**, *A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning*.
- Constantinos Daskalakis, Andrew Ilyas, Vasilis Syrgkanis et Haoyang Zeng, **2018**, *Training GANs with Optimism*.
- Marc Lanctot et collègues, **2019**, *OpenSpiel: A Framework for Reinforcement Learning in Games*.

**RAPPORTÉ — Limite bibliographique.** Brown, Shapley, la référence logicielle précise de Gambit et Bailey : **référence à vérifier**. Ces références ne sont pas interchangeables : un résultat sur GAN ou jeu fini n’est pas un résultat publié sur sondes d’activations.

**HYPOTHÈSE — Décision proposée à l’arbitre.** Prioriser la validation du gap et du dernier itéré sur jeu fini, puis le test de bibliothèque incomplète. Pour les mécanismes effectivement publiés sur sondes ou moniteurs de modèles de langage, je ne revendique aucun résultat sans source exacte vérifiable : cette partie reste documentairement non tranchée.

FIN-DE-CELLULE