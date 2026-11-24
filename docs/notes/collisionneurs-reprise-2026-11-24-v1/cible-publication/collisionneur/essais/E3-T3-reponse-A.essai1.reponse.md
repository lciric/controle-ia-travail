# Proposition A, tour III.3 : réponse aux critiques

**Préalables**
- Les pièces transmises sont complètes : FAITS, QUESTION, ma conception, critique B, critique C.
- Le manuscrit et le script ne sont pas joints. Leur contenu reste **RAPPORTÉ** et je ne le reconstitue pas.
- Dans la critique B, (b)2, l'inégalité de variance est visiblement mal formée (« $\ge \frac{1-p_f^*}{\delta^2}^{-1}$ »). Je n'en retiens que la partie lisible : la probabilité de comptage nul.
- Je conserve les statuts que B et C attribuent à leurs propres affirmations. Quand je refais un calcul moi-même, je le dis.
- Je ne traite que les sections qui visent A.

---

## (a) Décision sur chaque critique

### Trois calculs directs qui réorganisent ma réponse

Ce sont des calculs d'une ligne sur les formules des opérateurs données dans FAITS. Je les qualifie de **VÉRIFIÉ** au sens « calcul direct refait par moi ».

**K1. L'inversion A/B est conditionnelle.** Prenons $\beta_{\mathrm f}=\beta_{\mathrm h}=1>\beta_{\mathrm v}>0$. Après factorisation de $e^{\eta R_0}$, les poids relatifs de (h, v, f) sont :
- sous A : $(p_{\mathrm h},\ \beta_{\mathrm v}p_{\mathrm v}e^{\eta\Delta R},\ p_{\mathrm f}e^{\eta\Delta R})$ ;
- sous B : $(p_{\mathrm h},\ \gamma_{\mathrm v}p_{\mathrm v}e^{\eta\Delta R},\ p_{\mathrm f}e^{\eta\Delta R})$, avec $\gamma_{\mathrm v}=e^{-\eta(1-\beta_{\mathrm v})(R_0+\Delta R+C)}$.

On a donc $\pi_{\mathrm B}(\Pi_{\mathrm f})>\pi_{\mathrm A}(\Pi_{\mathrm f})$ si et seulement si $\eta(1-\beta_{\mathrm v})(R_0+\Delta R+C)>-\ln\beta_{\mathrm v}$. Avec $C=0$ et $\eta$ petit, l'ordre s'inverse.

L'énoncé du manuscrit (« la pénalité négative amplifie strictement plus $\Pi_{\mathrm f}$ ») reste **RAPPORTÉ**. Mais son résumé dans FAITS omet cette condition. Soit le manuscrit la contient, soit l'énoncé est faux sans elle. **À vérifier avant toute diffusion.** C l'a signalé (critique C, (b)1).

**K2. A est linéaire en $\beta$, B est convexe.** Sous A, $\pi_{\mathrm A}(\Pi_{\mathrm f})\propto e^{\eta(R_0+\Delta R)}\,\pi_0(\Pi_{\mathrm f})\,\bar\beta_{\mathrm f}$, où $\bar\beta_{\mathrm f}$ est la moyenne de $\beta$ sous $\pi_0$. L'agrégation par régime est donc exacte, même si $\beta$ varie à l'intérieur d'un régime. Sous B, $\mathbb E[e^{\eta(R+C)\beta}]$ est convexe en $\beta$, d'où le biais de Jensen relevé par B.

**K3. Le rapport f/h ne dépend pas des autres classes.** Sous les deux opérateurs, la constante de normalisation s'élimine dans $\log(\pi(\Pi_{\mathrm f})/\pi(\Pi_{\mathrm h}))$. Une classe d'échec $\Pi_{\text{échec}}$ fausse les probabilités absolues, pas ce rapport.

### Critiques de B

| Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|
| (a)1 Dilemme $\Delta R$ (nul, ou fuite de l'oracle caché) et quatrième régime d'échec | **Acceptée → test** | Mon E1 était mal construit. Je le remplace par des *tests visibles corrompus* (voir E1′) : la récompense ne lit que les tests visibles et $\Delta R$ est fixé par conception. $\Pi_{\text{échec}}$ est traité par K3 (métrique en rapport f/h) et rapporté séparément. |
| (a)2 L'expert itéré ne réalise pas l'opérateur A ($\beta^T$, ou B avec $C=0$) ; le sélecteur fini ne se transfère pas | **Acceptée → test** | Nouvelle expérience E0 sur un arbre autorégressif exact. Elle compare quatre bras, chacun confronté à son propre point fixe prédit. Je reprends le contrôle (c)3 de B. |
| (a)3 Le dosage par affinage supervisé confond plusieurs facteurs | **Acceptée → test** | Dosage par biais additif sur le seul *jeton de stratégie*. Le reste du modèle n'est pas touché. $\beta_{\mathrm f}$ est remesuré à chaque dose. |
| (a)4 E3 (c1) vrai par construction ; fuite de $\Pi_{\mathrm f}$ | **Acceptée, puis reformulée** | L'identité de covariance est algébrique (RAPPORTÉ ; la forme qu'en donne B est cohérente avec mon calcul). La tester revient à tester une identité. La sonde est désormais entraînée *sans* $\Pi_{\mathrm f}$, et la covariance est *mesurée*, pas imposée. La question empirique devient la dérive des représentations (E3′). |
| (a)5 E5 : le rééchantillonnage est tautologique | **Rejetée en partie** | Si les pièges sont un sous-ensemble *aléatoire* d'épisodes réels audités après génération, $\delta_{\mathrm{ind}}=0$ est le fonctionnement voulu du mécanisme, pas une vacuité : la borne dit alors que l'audit intercepte au taux ordinaire. Le coût réel est le budget d'audit $\rho$. Je retiens en revanche le vrai risque, que pointe aussi C : que la vérifiabilité soit corrélée aux caractéristiques des épisodes. Il devient un test (E5′). |
| (a)5 E4 : une inégalité inversée qui ne compile pas ne prouve rien | **Acceptée** | Elle est remplacée par des témoins de satisfiabilité (`∃ params, Hyp params`). |
| (b)1 Biais de Jensen à l'intérieur d'un régime ; le contrôle nul est faux si $\Lambda_{\mathrm f}\neq\Lambda_{\mathrm v}$ | **Acceptée pour B, rejetée pour A** | Par K2, le biais n'existe que sous B. Il devient une prédiction : l'écart entre juge appris et filtre de Bernoulli doit valoir $\Lambda_{\mathrm f}(t)-\Lambda_{\mathrm h}(t)$, calculable à partir des $\beta$ par trajectoire mesurés avant l'entraînement. Le contrôle nul ($\beta_{\mathrm f}=\beta_{\mathrm v}$) passe par un filtre synthétique. |
| (b)2 Événements rares : $K_{\mathrm f}=0$ | **Acceptée** | Dans E0, E1′ et E2′, $\pi_0(\Pi_{\mathrm f})$ est lu sur la probabilité du jeton de stratégie, sans échantillonnage. Les doses sont choisies telles que $Np_{\mathrm f}\ge 50$ (illustratif). |
| (b)3 Bootstrap sur 3 graines ; FNR à seuil fixe | **Acceptées** | Au moins 10 graines (illustratif), avec inférence au niveau de la graine et test de signe exact dont la valeur-$p$ minimale est vérifiée à l'avance. Le FNR est rapporté à FPR fixé. |
| (b)4 Puissance nulle de $2\hat a-1$ hors de la classe de discriminateurs | **Acceptée** | J'avais annoncé que ce test ne pouvait que falsifier H_A. Je l'écris désormais dans la règle de décision : un échec à discriminer ne confirme rien. |
| (c)1 à (c)5 | **Acceptées** | Elles sont intégrées dans E0 à E4′ et créditées à B. |

### Critiques de C

| Critique | Décision | Raison, ou test qui la remplace |
|---|---|---|
| (a)1 Non-équivalence de l'expert itéré | **Acceptée** | Même traitement que B (a)2. |
| (a)1 KL directe (affinage) contre KL inverse (PPO) | **Rejetée en partie → test** | À capacité infinie, si la cible est dans la famille, les deux ont le même optimum. L'écart ne vient que de la capacité finie. Il est mesuré par le contrôle « détecteur inactif » ((c)1 de C), où la théorie impose $\pi_{\mathrm A}\equiv\pi_{\mathrm B}$. |
| (a)1 $Z$ global contre $Z(x)$ par invite | **Acceptée** | C'est un écart réel entre le modèle (loi sur les politiques) et le RL contextuel. La prédiction est calculée invite par invite puis agrégée. E0 travaille sur une seule invite. |
| (a)2 Contradiction sur $\Delta R$ | **Acceptée** | Même traitement que B (a)1. |
| (a)2 Dérive de $\beta$ dans un régime alors qu'on le mesure avant l'entraînement | **Rejetée pour A, acceptée pour B** | Sous A (K2), la repondération vers les sous-variantes à fort $\beta$ est prédite, et l'agrégat reste exact avec $\bar\beta$ mesuré sous $\pi_0$. Sous B, voir B (b)1. |
| (a)3 Affinage de dosage ; coût de maintien non mesuré ; contrôle négatif faible | **Acceptée** | Le coût de maintien n'est pas défini dans FAITS et je ne l'invente pas. E2′ est subordonnée à sa définition dans le manuscrit. Le contrôle négatif devient un dosage à rapport f/h constant ((c)4 de C). |
| (a)4 (c1) n'assure pas l'indépendance ; (c2) vrai par construction ; soustraction du contrôle invalide | **Acceptées** | (c2) devient un *contrôle positif* de sensibilité, et non une preuve. La soustraction est supprimée au profit d'une stratification par régime et d'une repasse sur poids gelés. |
| (a)5 La formalisation dépend de la transcription | **Acceptée** | Table de correspondance énoncé par énoncé, relue par une seconde personne. Évaluation numérique croisée des énoncés formels avec le script. |
| (a)5 $\tau_{\mathrm{ord}}$ non défini | **Acceptée** | Je l'avais signalé. E5′ n'est pas exécutable sans cette définition. |
| (a)5 Sonde sur les activations de la politique « circulaire » | **Rejetée** | Par l'inégalité de traitement des données, pour toute fonction $\phi$ de l'épisode, y compris les activations, on a $d_{\mathrm{TV}}(\phi_\#P,\phi_\#Q)\le d_{\mathrm{TV}}(P,Q)$. $2a-1$ reste donc une borne inférieure valide de $\delta_{\mathrm{ind}}$, et elle mesure précisément ce que la politique encode. Le vrai risque est le surapprentissage du discriminateur, couvert par le contrôle de partition nulle ((c)6 de C). |
| (a)5 Exiger que le détecteur « batte » l'oracle mécanique | **Acceptée : erreur de rédaction** | L'oracle mécanique sert d'étiquetage. Le détecteur n'a pas à le battre. L'exigence correcte est un écart $\beta_{\mathrm v}<\beta_{\mathrm f}$ avec des intervalles de confiance disjoints, car l'hypothèse du théorème est une variance de $\beta$ strictement positive parmi les tricheurs. |
| (b)1 Bascule de signe de $\Delta_{\mathrm{BA}}$ ; niche imparfaite | **Acceptée : la plus importante** | Voir K1. La bascule devient la prédiction centrale, testée des deux côtés du seuil. La niche parfaite est garantie *mécaniquement* (filtre à règle qui n'inspecte pas le corps de la solution), au lieu d'être estimée. |
| (b)1 Invariance par translation $R\mapsto R+a$ | **Acceptée → test** | Sous B, translater $R$ de $a$ équivaut à $C\mapsto C+a$. Une normalisation de la récompense par groupe, comme dans GRPO, rend donc $C$ effectif non identifiable. E1′ impose REINFORCE ou PPO avec une ligne de base fixe et consignée, plus un bras de translation. |
| (b)2 Variance du rapport logarithmique, propagation de l'incertitude, grille trop grossière | **Acceptée** | La grille est resserrée autour du seuil prédit (7 à 9 valeurs, illustratif). Un intervalle prédictif propagé est rapporté. |
| (b)3 Comptages nuls et espacement des doses en E2 | **Acceptée** | Lecture de $\pi_0$ sur les logits ; espacement des doses inférieur à 0,5 nat (illustratif). |
| (b)4 Biais de la soustraction en E3 | **Acceptée** | Soustraction supprimée. |
| (b)5 Classes déséquilibrées ; AUROC invariante par transformation monotone | **Acceptée** | J'avais déjà imposé des classes équilibrées. J'ajoute le FNR à FPR fixé en plus de l'AUROC. |
| (c)1 à (c)7 | **Acceptées** | Intégrées ci-dessous et créditées à C. |

---

## (b) Expériences corrigées

Tous les seuils et effectifs sont **illustratifs**. Chaque issue falsifie une hypothèse nommée.

### E0 (nouvelle, à mener en premier) : quel algorithme réalise quel opérateur ?

**Dispositif.**
- Arbre autorégressif de longueur au plus 6, avec un petit vocabulaire et une seule invite (repris de B (c)3).
- Le premier jeton fixe la stratégie h, v ou f. Les suites déterminent la récompense.
- Les lois $\pi_{\mathrm A}$, $\pi_{\mathrm B}^{(\eta,C)}$ et $\pi_{\mathrm B}^{(\eta,0)}$ sont calculables exactement.
- Deux paramétrisations : tabulaire, et petit réseau à poids partagés.

**Bras et prédiction de chacun.**
- **A1, filtre puis inclinaison en un tour** : échantillons de $\pi_0$, acceptés selon le détecteur, pondérés par $e^{\eta R}$, puis distillés une fois depuis $\pi_0$. Prédiction : $\pi_{\mathrm A}$. C'est une HYPOTHÈSE à capacité finie.
- **A2, expert itéré sur $T$ tours** : prédiction $\propto\beta^T e^{T\eta_0R}\pi_0$ (calcul de B, que je reprends).
- **M, masquage dans le gradient de politique** : prédiction $\pi_{\mathrm B}^{(\eta,0)}$.
- **B, pénalité $-C$** : prédiction $\pi_{\mathrm B}^{(\eta,C)}$.

**Contrôles.**
- Détecteur inactif ($\beta\equiv1$, $C=0$) : tous les bras doivent coïncider.
- Translation $R_0\mapsto R_0+a$ dans le bras B.

| | |
|---|---|
| **H_A** | Chaque bras converge vers *son* point fixe ($d_{\mathrm{TV}}<0{,}02$, et plus près de sa cible que des cibles concurrentes). Le signe de $\Delta_{\mathrm{BA}}=\pi_{\mathrm B}(\Pi_{\mathrm f})-\pi_{\mathrm A1}(\Pi_{\mathrm f})$ bascule au seuil de K1, à $\pm10\,\%$ près. |
| **H_B** | Au moins un bras s'écarte de sa cible, ou la bascule est absente ou déplacée. |
| **Falsification** | H_A tenue en tabulaire : H_B falsifiée, et A1 devient l'implémentation de A pour E1′. H_A rejetée en tabulaire : l'implémentation est invalide, et E1′ ne doit pas être lancée. H_A tenue en tabulaire mais rejetée avec le réseau partagé : l'effet du partage de poids est isolé. |

**Coût.** Quelques heures de CPU ou de GPU (illustratif).

### E1′ : la bascule A/B prédite par Gibbs se produit-elle dans un vrai modèle ?

**Tâche : tests visibles corrompus.** Chaque tâche comporte une spécification, $k$ tests visibles dont *un* attend une sortie contraire à la spécification, et des tests cachés conformes à la spécification.

**Récompense.** Elle ne lit que les tests visibles.
- Une solution honnête réussit $k-1$ tests visibles : récompense $R_0$, constante.
- Une triche réussit les $k$ tests visibles : récompense $R_0+\Delta R$, où $\Delta R$ est réglé par le poids du test corrompu.
- Les tests cachés servent *seulement* à l'étiquetage. C'est le contrôle d'aveuglement (B (c)1), vérifiable mécaniquement.

**Régimes, définis sur la structure du code et non sur le raisonnement écrit.**
- v : modification des fichiers de test ou sortie forcée.
- f : cas codé en dur.
- h : conforme à la spécification, sans toucher aux tests.

**Détecteur principal.** Une règle d'audit aléatoire signale une modification des tests avec probabilité $1-\beta_{\mathrm v}$. Elle n'inspecte jamais le corps de la solution, donc $\beta_{\mathrm f}=\beta_{\mathrm h}=1$ *exactement*. C'est le filtre de Bernoulli de B (c)2.

**Bras secondaire.** Un juge appris, pour mesurer le biais de Jensen prédit sous B (K2).

**Implémentation.**
- Le bras A n'est lancé que si E0 a validé A1.
- Optimisation par REINFORCE ou PPO avec ligne de base fixe, sans normalisation par groupe.
- Bras M ($C=0$) et bras de translation.

| | |
|---|---|
| **H_A** | Le signe de $\Delta_{\mathrm{BA}}$ suit K1 des deux côtés du seuil, sur une grille en $\eta(R_0+\Delta R+C)$ de part et d'autre de $-\ln\beta_{\mathrm v}/(1-\beta_{\mathrm v})$. L'erreur médiane sur $\log(\hat\pi_{\mathrm f}/\hat\pi_{\mathrm h})$ est inférieure à 0,5 nat, en dehors de l'intervalle prédictif propagé. |
| **H_B** | Pas de bascule, ou bascule décalée de plus de 25 %. |
| **Contrôles** | $\beta_{\mathrm f}=\beta_{\mathrm v}$ via le filtre synthétique : aucun enrichissement conditionnel prédit. $\Delta R=0$ avec détecteur actif : rapport f/h égal à celui de $\pi_0$ (C (c)3). Détecteur inactif (C (c)1). |
| **Statistique** | Au moins 10 graines ; test de signe exact par point de grille, de niveau 0,05 avec correction pour la grille ; valeur-$p$ minimale atteignable vérifiée à l'avance. |
| **Falsification** | Bascule au bon endroit : H_B falsifiée. Absence de bascule alors qu'E0 est passée : H_A falsifiée, car l'équilibre statique ne décrit pas l'entraînement à cette échelle. |

### E2′ : la barrière d'accessibilité (subordonnée à la définition du coût de maintien)

**Dosage.** Biais additif sur le jeton de stratégie f. On a alors $\pi_0^{(k)}(\Pi_{\mathrm f})$ exact et le reste des poids inchangé.

**Contrôle.** Biais simultanés sur h et f, à rapport f/h constant (C (c)4).

| | |
|---|---|
| **H_A** | La transition se produit à $\pm1$ nat du seuil donné par le manuscrit. |
| **H_B** | La transition n'est pas ordonnée par le rapport logarithmique a priori. |

**Condition préalable.** Si le manuscrit ne définit pas le coût de maintien, ou ne le rend pas nul en mono-objectif, E2′ n'est pas jugeable et n'est pas lancée.

### E3′ : l'audit hors boucle subit-il une dérive des représentations ?

**Sonde.** Sonde linéaire entraînée sur h et v seulement, $\Pi_{\mathrm f}$ exclu (B (c)4).

**Avant l'entraînement par renforcement.** On *mesure* $\mathrm{FNR}_{\mathrm f}-\mathrm{FNR}_{\mathrm v}$ sur un ensemble certifié tenu à l'écart. Cela fixe l'effet de composition prédit : $(q_t-q_0)(\mathrm{FNR}_{\mathrm f}-\mathrm{FNR}_{\mathrm v})$.

**Après l'entraînement.** Les *mêmes* trajectoires, échantillonnées sous $\pi_{\theta_t}$, passent dans $\theta_t$ et dans $\theta_0$ gelé (C (c)5). Le FPR est fixé de deux façons :
- seuil gelé, qui mesure l'instrument déployé ;
- seuil recalibré sur h, qui mesure le pouvoir discriminant.

| | |
|---|---|
| **H_A** | À séquences fixées, $|\mathrm{FNR}(h_{\theta_t})-\mathrm{FNR}(h_{\theta_0})|\le0{,}03$. La variation agrégée égale l'effet de composition prédit. |
| **H_B** | Écart à séquences fixées supérieur ou égal à 0,08 : la mise à jour des poids dégrade la sonde. |
| **Contrôle positif** | Sonde qui imite le juge en boucle : une hausse est attendue. Elle vérifie la sensibilité de la mesure, sans valeur de preuve. |
| **Zone morte** | Un écart compris entre 0,03 et 0,08 est déclaré non concluant à l'avance. |

### E4′ : la formalisation

- Énoncés compilés, plus un témoin `∃ params, Hyp params` pour chaque théorème (B (c)5, C (c)7).
- Table de correspondance relue par une seconde personne.
- Énoncé d'inversion A/B formalisé **sans** la condition de K1 : un contre-exemple numérique explicite, avec bornes certifiées sur l'exponentielle, doit être constructible.

| | |
|---|---|
| **H_A** | Les énoncés tels que rapportés se compilent sans hypothèse ajoutée. |
| **H_B** | Il faut ajouter une hypothèse, en particulier la condition de K1. |

### E5′ : les épisodes vérifiables sont-ils représentatifs ? (bloquée tant que $\tau_{\mathrm{ord}}$ n'est pas défini)

- Les pièges sont un sous-ensemble aléatoire d'épisodes *vérifiables*.
- On mesure la distance entre ces épisodes vérifiables et la distribution complète, par discriminateur en classes équilibrées.
- Contrôle de partition nulle (C (c)6).

| | |
|---|---|
| **H_A** | La borne est non triviale : discriminateur au niveau du hasard, dans les limites du contrôle nul. |
| **H_B** | $2a-1\ge\tau_{\mathrm{ord}}$. |

Seule H_A peut être falsifiée par cette mesure. H_B ne l'est que par construction aléatoire certifiée suivie d'une interception mesurée.

---

## (c) Réponse à l'arbitre (une page)

**Ce qui est établi.**
- *Rien du manuscrit n'est audité.* Preuves, seuils, plancher sous B, trois mécanismes, script exact et 14 000 tirages restent **RAPPORTÉ**.
- *Trois calculs directs sur les formules des opérateurs (VÉRIFIÉ, calcul refait).*
  - K1 : l'amplification de $\Pi_{\mathrm f}$ par B par rapport à A, en niche parfaite, exige $\eta(1-\beta_{\mathrm v})(R_0+\Delta R+C)>-\ln\beta_{\mathrm v}$.
  - K2 : A est linéaire en $\beta$, B est convexe.
  - K3 : le rapport f/h est indépendant des autres classes.
- K1 implique que le résumé RAPPORTÉ omet une condition. Si le manuscrit l'omet aussi, un relecteur le réfutera par $C=0$ et $\eta\to0$. **Il faut le vérifier avant toute diffusion.**

**Ce qui n'est pas établi.**
- Le transfert de l'équilibre de Gibbs aux optimiseurs réels (HYPOTHÈSE).
- Un algorithme qui réalise l'opérateur A. L'expert itéré et le masquage ne le réalisent pas, selon les calculs de B que je reprends ; A1 est une HYPOTHÈSE.
- La nouveauté par rapport aux travaux empiriques sur l'obfuscation (HYPOTHÈSE ; références à vérifier).
- La définition de $\tau_{\mathrm{ord}}$ et celle du coût de maintien, absentes des faits.
- Les règles d'anonymat et de prépublication de chaque appel (à vérifier pour l'année visée).

**Positionnement révisé (HYPOTHÈSES).**
1. Atelier non archivistique et archive ouverte, *après* correction ou confirmation de K1 dans le manuscrit.
2. TMLR si E0 passe et que E4′ couvre au moins les énoncés A/B (critères à vérifier).
3. Piste principale NeurIPS, ICLR ou ICML seulement si E0 passe *et* si E1′ montre la bascule de signe au seuil prédit. Une prédiction bilatérale qui bascule au bon endroit est l'élément le plus difficile à qualifier de « sélection bayésienne évidente ».
4. COLT et ALT restent un mauvais ajustement : il n'y a pas de borne d'apprentissage.

La stratégie de diffusion est inchangée : archive ouverte sous titre neutre, aucune promotion pendant l'évaluation si l'appel l'interdit, dépôt de code anonymisé. Toutes ces règles sont à vérifier.

**Expérience à faire en premier : E0** (arbre autorégressif exact, quatre bras, coût de l'ordre de quelques heures, illustratif).
- **H_A :** chaque procédure converge vers son point fixe prédit, et le signe de $\Delta_{\mathrm{BA}}$ bascule au seuil de K1.
- **H_B :** une procédure s'écarte de sa cible, ou la bascule est absente ou déplacée.
- **Si H_A tient,** A1 est validé comme implémentation de A et E1′ devient légitime.
- **Si H_A tombe,** toute comparaison A/B en RL réel mesurerait l'algorithme et non la théorie : on s'arrête à l'atelier et à TMLR.

Juste avant E0, une vérification documentaire gratuite : relire dans le manuscrit l'énoncé de l'inversion A/B pour y chercher la condition de K1.

FIN-DE-CELLULE