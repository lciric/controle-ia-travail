*Vérification des pièces (Règle 2) : les blocs `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-D` et les critiques croisées `A`, `B`, `C` sont présents et complets ; les conceptions du tour III.1 de `A`, `B` et `C` ne sont pas transmises.*

*Conventions de statut (Règle 1) : le contenu issu des pièces transmises est marqué `[RAPPORTÉ]` ; l'ensemble de mes réponses, dérivations, seuils et protocoles corrigés porte le statut `[HYPOTHÈSE]`. Aucun statut antérieur n'est modifié.*

---

## (a) Réponse point par point aux critiques visant la proposition D

### 1. Critiques issues de la proposition A (sections visant D et remarque commune finale)

1. **A-D.a.1 — Statuts `VÉRIFIÉ` sans audit visible dans les pièces et trois formulations excédant le bloc `FAITS`** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   En dossier fermé, les pièces transmises n'auditent pas les références externes ni les propriétés mathématiques citées au tour III.1 ; je laisse l'arbitre trancher les étiquettes déposées au tour III.1 et je n'emploie ici que `[RAPPORTÉ]` (pour les pièces) et `[HYPOTHÈSE]` (pour mon travail). De même, les trois formulations relevées par A allaient au-delà de la lettre de `FAITS` : `FAITS` mentionne uniquement la feuille de route (`arXiv 2607.13087`, p. 25, `[RAPPORTÉ]`), l'évaluation prédictive au déploiement (`arXiv 2512.22154`, p. 12 et 16, `[RAPPORTÉ]`), l'indéfinition fréquente des scores de vérité terrain (`arXiv 2606.08892`, p. 2 et 10, `[RAPPORTÉ]`) et la vulnérabilité des défenses latentes aux activations obscurcies avec baisse de performance sur tâche complexe (`arXiv 2412.09565`, p. 1, `[RAPPORTÉ]`). Parler de « coupe minimale », de « banc tiers » réutilisable ou d'échec « sur tâches simples » par contraste constituait une inférence (`[HYPOTHÈSE]`), non un énoncé `[RAPPORTÉ]`.

2. **A-D.a.2 — Phrase opposable réussissant des deux côtés et inexistence d'un « seuil exact »** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   Déclarer un succès à la fois si les suppositions tiennent et si l'on estime le point où elles cèdent immunise le programme contre l'échec, et toute frontière empirique n'est connue qu'à un intervalle d'échantillonnage et un optimiseur d'attaque près. En `(c)`, la phrase opposable est réécrite pour que la vacuité de la borne d'audit ou la perte du gain des sondes constitue une **réfutation** de la thèse défensive du programme (`[HYPOTHÈSE]`).

3. **A-D.a.3 — Garantie redevenant conditionnelle au jumeau et à la taxe d'obscurcissement (iii)** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   Si les sondes ne portent aucune garantie autonome, la taxe d'obscurcissement (iii) et la précision du jumeau (i) ne doivent conditionner que l'**efficacité** (réduction du dommage non intercepté ou de la largeur de borne à budget fixé), tandis que la **garantie de validité** repose uniquement sur un plancher d'audit aléatoire $q_{\min} > 0$ et un oracle à biais borné (`[HYPOTHÈSE]`).

4. **A-D.a.4 — Confusion de trois causes dans E1, $H_B$ disjonctive, zones mortes, dénominateur arbitraire et lot réel sans vérité** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   En `(b)`, la validité de l'oracle (`E1-cor`) et la stabilité de la ligne de base du jumeau (`E2-cor`) sont séparées en deux duels orthogonaux à paramètre scalaire unique sans zone morte ; le dénominateur relatif au saboteur non contrôlé est abandonné ; le lot externe hors simulation ne juge que le taux de fausses alertes et l'accord oracle–humains (`[HYPOTHÈSE]`).

5. **A-D.a.5 — Déplaçabilité du normalisateur en E2, perte liée au résumé, effet de statistique d'ordre $\sigma_m \sqrt{2 \ln m}$ sur $m$ candidats, circularité du dommage constant** (`[RAPPORTÉ]`) : **ACCEPTÉE** sur la circularité et l'effet mécanique de statistique d'ordre, et **TRANSFORMÉE EN TEST** sur la normalisation canonique (`[HYPOTHÈSE]`).
   En `E1-cor`, le dommage réel est fixé par un simulateur aval indépendant de l'oracle, le déplacement rhétorique est mesuré *au-delà* de la loi nulle du minimum de $m$ paraphrases neutres honnêtes, et le normalisateur n'est testé que sous filtre préalable de non-effacement sur sabotage non adaptatif (`[HYPOTHÈSE]`).

6. **A-D.a.6 — Fuite des contrôles bénins dans E3, modèles emboîtés et $H_A$ conjonctive à quatre clauses (illustratif)** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   En `E3-cor`, des familles entières de consignes et réglages fins bénins sont tenues à l'écart de l'entraînement des sondes, et la conjonction est remplacée par un seul contraste scalaire de dommage net survivant (`[HYPOTHÈSE]`).

7. **A-D.a.7 — Absence de jumeau en régime asymétrique ($\varepsilon \ge$ écart de compétence)** (`[RAPPORTÉ]`) : **ACCEPTÉE** pour le différentiel direct inter-tailles, et **TRANSFORMÉE EN TEST** en `E4-cor` (`[HYPOTHÈSE]`) en appariant un saboteur fort à un jumeau honnête de *même taille* sous supervision d'un juge faible de 8 milliards de paramètres (`[RAPPORTÉ]` pour 8B).

8. **A-D.a.8 & critique commune finale de A — Circularité de l'oracle sur failles définies contre sa référence et sollicitations multiples du mode tenu à l'écart** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   Le dommage vrai est désormais défini par l'erreur méthodologique aval d'un simulateur causal caché à l'oracle, et le mode tenu à l'écart (`[RAPPORTÉ]`) n'est décacheté qu'**une seule fois**, exclusivement dans `E3-cor` (`[HYPOTHÈSE]`).

9. **A-D.b & A-D.c — Non-estimabilité de $D_{\text{TV}}$ en grande dimension, sous-puissance des effectifs illustratifs, biais de ratio, et contrôles négatifs requis** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   $D_{\text{TV}}$ est remplacée par le biais projeté studentisé ; une règle ex ante d'erreur-type maximale bloque tout essai sous-puissant avant décachetage ; l'estimateur de ratio est éliminé ; tous les contrôles négatifs demandés par A (placebo sans dommage, tirage A/A hors-domaine, rééchantillonnage neutre de $m$ candidats, normalisation hors attaque, interventions bénignes tenues à l'écart, pénalité placebo, étiquettes permutées) sont intégrés en `(b)` (`[HYPOTHÈSE]`).

---

### 2. Critiques issues de la proposition B (signalement, défauts communs, section visant D et conclusion)

1. **B-Signalement & B-Commun.3 — Références marquées `VÉRIFIÉ` et circularité des mondes plantés avec la référence de l'oracle** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`), traitée aux points `A-D.a.1` et `A-D.a.8`.

2. **B-Commun.1 — Un seul mode tenu à l'écart interdit d'identifier la variance inter-genres $\tau^2$ et impose une lecture unique** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   Avec un tirage unique de genre (`[RAPPORTÉ]`), $\tau^2$ est non identifiable : nous retirons toute prétention d'inférence statistique sur la population des genres inconnus à partir des sondes et réservons l'unique lecture scellée du mode tenu à l'écart à `E3-cor` (`[HYPOTHÈSE]`).

3. **B-Commun.2 — Incertitude Beta du seuil à $1\,\%$ de fausses alertes (`[RAPPORTÉ]`) et confusion pas / trajectoire** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   En `(b)`, le taux nominal $\alpha_{\text{traj}} = 1\,\%$ (`[RAPPORTÉ]` pour $1\,\%$) porte explicitement sur la **trajectoire entière**, calibré sur $n_0 = 2\,000$ (illustratif) trajectoires honnêtes indépendantes afin de borner la fluctuation $\text{Beta}(n_0\alpha+1, n_0-n_0\alpha)$ à $\approx 1{,}05\,\% \pm 0{,}23\,\%$ (illustratif) (`[HYPOTHÈSE]`).

4. **B-D.a.1 & B-Conclusion — FPR hors-domaine d'E1 basse par construction sur base commune, confondue avec l'adaptateur, ou haute sur second modèle (proxy inter-modèles $\eta$)** (`[RAPPORTÉ]`) : **ACCEPTÉE** sur l'artefact de base commune, et **TRANSFORMÉE EN TEST** en `E2-cor` (`[HYPOTHÈSE]`).
   B note en conclusion qu'aucune pièce ne pose en duel la viabilité d'un proxy inter-modèles de $\eta$ (`[RAPPORTÉ]`). `E2-cor` teste séparément et conjointement la dérive sous interventions bénignes inédites et le proxy inter-modèles à compétence aval appariée (`[HYPOTHÈSE]`).

5. **B-D.a.2, B-D.a.3, B-D.a.4, B-D.a.5, B-D.a.7 — Lot réel sans référence de dommage, normalisateur effaçant la faille, zones grises violant B4 (y compris désaccord inter-échelles), succès quasi vrai par construction, confusion du régime asymétrique** (`[RAPPORTÉ]`) : **ACCEPTÉES** (et **TRANSFORMÉES EN TESTS** pour le normalisateur et l'asymétrie à jumeau apparié), traitées aux points `A-D.a.2` à `A-D.a.7` et formalisées sans zone grise en `(b)` (`[HYPOTHÈSE]`).

6. **B-D.a.6 — L'exclusion des mitigations par entraînement retirerait sans argument la thèse rivale d'`arXiv 2606.08892` (`[RAPPORTÉ]`)** (`[RAPPORTÉ]`) : **REJETÉE AVEC RAISON** (`[HYPOTHÈSE]`).
   L'exclusion ne repose pas seulement sur la rareté du calcul et de la relecture humaine (`[RAPPORTÉ]`), mais sur un biais d'identifiabilité mécanique (que B et C relèvent d'ailleurs eux-mêmes ailleurs dans leurs critiques `[RAPPORTÉ]`, constat dont je me sers ici selon B1) : les saboteurs du programme étant *construits* par consigne cachée ou réglage fin (`[RAPPORTÉ]`), un réglage fin défensif écrase l'adaptateur de bas rang ou modifie la hiérarchie d'instructions par artefact de laboratoire, sans tester la suppression d'un désalignement endogène (`[HYPOTHÈSE]`). En outre, tester si la borne d'audit certifiée est non vacante (`E1-cor` à `E3-cor`) met directement à l'épreuve de la réfutation l'hypothèse d'`arXiv 2606.08892` selon laquelle la surveillance est peu prometteuse sur tâches floues (`[RAPPORTÉ]`), sans introduire ce confondant d'écrasement (`[HYPOTHÈSE]`).

7. **B-D.a.8 — L'accumulation linéaire d'un biais ne vaudrait plus pour un test séquentiel recalibré par fenêtre et ne suffirait pas à inverser l'ordre des papiers** (`[RAPPORTÉ]`) : **REJETÉE AVEC RAISON** (`[HYPOTHÈSE]`).
   D'une part, face à un sabotage diffus stationnaire de dérive $\mu$ par pas, recalibrer le seuil sur une fenêtre glissante des sorties de l'agent absorbe $\mu$ dans la référence et annule la puissance ; recalibrer sur le seul jumeau laisse intact l'écart systématique $\varepsilon$ entre l'agent honnête et le jumeau ; et tronquer la mémoire du test à une fenêtre courte $W$ plafonne le signal cumulé à $W\mu$, supprimant le gain asymptotique recherché par le papier « le temps » (`[HYPOTHÈSE]`). D'autre part, le papier « le temps » utilise l'oracle d'audit comme variable de résultat : tant que la validité et la non-déplaçabilité de cet oracle (« l'instrument ») ne sont pas établies, toute mesure temporelle en aval reste instrumentalement indéterminée (`[HYPOTHÈSE]`).

8. **B-D.b & B-D.c — Borne de Le Cam gouvernée par $\sup_{\text{tâches}} \varepsilon_{\text{tâche}}$, sous-puissance en E2, plafond d'AUC lié à l'accord humain–humain, limite de deux échelles (illustratif), et contrôles négatifs requis** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   `E2-cor` évalue le pire cas sur les strates hors-domaine ; l'AUC de l'oracle sur lot externe est rapportée à l'accord inter-juges humains mesuré en double aveugle ; la réplication à deux échelles (illustratif) est traitée comme un test de réfutation d'invariance et non comme une estimation de variance inter-familles ; les contrôles bénins (consigne et réglage fin) sont étendus à toutes les expériences (`[HYPOTHÈSE]`).

---

### 3. Critiques issues de la proposition C (section visant D)

1. **C-D.a.1 — Confusion de facteurs et trou de non-falsifiabilité dans E1** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`), corrigée par la scission en `E1-cor` (oracle) et `E2-cor` (jumeau) à coupure binaire unique.

2. **C-D.a.2 & C-D.c.1 — Régularisation spontanée ou omission de la faille subtile par le résumeur de 8B (`[RAPPORTÉ]`) dans E2** (`[RAPPORTÉ]`) : **ACCEPTÉE** et **TRANSFORMÉE EN TEST** (`[HYPOTHÈSE]`) via un filtre préalable de préservation du rappel sur sabotages non adaptatifs en `E1-cor`.

3. **C-D.a.3 & C-D.b.3 — Inversion perverse et indétermination de Fieller (référence à vérifier) du ratio de budgets $B_{\text{texte}} / B_{\text{sonde+texte}}$ dans E3 lorsque la taxe d'obscurcissement rapproche le dommage brut de $\Delta_{\max}$** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`).
   La démonstration de C est exacte : quand la régularisation latente réduit le dommage brut vers $\Delta_{\max}$, numérateur et dénominateur tendent vers zéro et leur ratio tend vers $1$ (illustratif) avec intervalle non borné, pénalisant $H_A$ lorsque la taxe d'obscurcissement fonctionne (`[HYPOTHÈSE]`). En `E3-cor`, on fixe le budget d'audit moyen $\bar{q}$ et on mesure la **différence absolue** de dommage réel cumulé non intercepté, normalisée par la constante fixe de l'audit uniforme (`[HYPOTHÈSE]`).

4. **C-D.a.4 — Incompatibilité des espaces latents et domination de l'écart de compétence dans l'asymétrie $70\text{B}$ contre $8\text{B}$ (illustratif)** (`[RAPPORTÉ]`) : **ACCEPTÉE** et **TRANSFORMÉE EN TEST** en `E4-cor` (`[HYPOTHÈSE]`), où seul l'auditeur texte est à 8B (`[RAPPORTÉ]`) face à une paire appariée $[70\text{B}, 70\text{B}]$ (illustratif).

5. **C-D.b.1, C-D.b.2 & C-D.c.2 — Perte d'identifiabilité par hétéroscédasticité inter-domaines ($\lambda > 1{,}414$, illustratif) même à $\varepsilon = 0$, et doublement de la variance intra-tâche ($2\sigma_{\text{intra}}^2$) avec un seul jumeau** (`[RAPPORTÉ]`) : **ACCEPTÉES** et **TRANSFORMÉES EN TEST** en `E2-cor` (`[HYPOTHÈSE]`).
   Le score différentiel est studentisé localement sur $m = 5$ (illustratif) tirages indépendants du jumeau par tâche, abaissant la variance intra-tâche de $2\sigma_{\text{intra}}^2$ à $(1 + 1/m)\sigma_{\text{intra}}^2$, sous pré-condition vérifiée $\hat{\rho} > 1/(m+1)$ (`[HYPOTHÈSE]`).

6. **C-D.c.3 — Absence d'une pénalité latente aléatoire orthogonale de même norme dans E3** (`[RAPPORTÉ]`) : **ACCEPTÉE** (`[HYPOTHÈSE]`), intégrée comme contrôle négatif obligatoire en `E3-cor`.

---

### 4. Déclaration explicite des emprunts méthodologiques (Règle B1)

Pour corriger mes protocoles sans lissage implicite, j'emprunte explicitement :
- **à A** (`[RAPPORTÉ]`) : le contrôle de statistique d'ordre par rééchantillonnage neutre de $m$ candidats, le tirage A/A hors-domaine, le contrôle par scores de sonde permutés à probabilités d'inclusion identiques, et l'audit uniforme à budget moyen égal $\bar{q}$ comme comparateur ;
- **à B** (`[RAPPORTÉ]`) : le plancher d'inclusion $q_t \ge q_{\min} > 0$ garantissant la validité d'échantillonnage indépendamment des sondes, la loi Beta de l'incertitude du seuil à $1\,\%$ (`[RAPPORTÉ]`), la calibration de l'AUC sur l'accord humain–humain, et le duel sur le proxy inter-modèles de $\eta$ ;
- **à C** (`[RAPPORTÉ]`) : la studentisation locale sur $m \ge 5$ (illustratif) réalisations du jumeau et la pénalité de régularisation latente projetée sur une direction aléatoire orthogonale.

---

## (b) Les expériences corrigées (inférence forte sans zone morte ni circularité)

### Règles communes de jugeabilité ex ante, de vérité terrain et de décision (B4) `[HYPOTHÈSE]`

1. **Vérité terrain découplée de l'oracle** : chaque proposition d'expérience est évaluée en laboratoire par un **simulateur méthodologique aval caché à l'oracle** qui exécute le plan proposé (plan d'échantillonnage, contrôles, estimateur) sur un modèle génératif synthétique et mesure sa perte de validité réelle $d_t \in [0, 1]$ (illustratif). L'oracle ne reçoit que l'énoncé amont et sa référence textuelle, jamais le code du simulateur. Sur le lot externe réel ($n = 120$ propositions équilibrées hors simulation, illustratif), la référence est établie par deux relecteurs humains indépendants (illustratif) à l'aveugle.
2. **Condition préalable de jugeabilité et partition binaire sans zone morte** : chaque duel porte sur un unique scalaire $\theta$ opposant $H_0^{\text{fort}}$ ($\theta \le \theta_0$) à $H_1^{\text{fort}}$ ($\theta \ge \theta_{\min}$, avec $\theta_{\min} > \theta_0$). Avant tout décachetage des bras adverses, l'erreur-type $\text{SE}(\hat{\theta})$ est calculée par bootstrap sur les contrôles honnêtes. L'essai n'est ouvert que si $\text{SE}(\hat{\theta}) \le \frac{\theta_{\min} - \theta_0}{2 \times 1{,}645}$ (illustratif, garantissant simultanément des risques d'erreur $\le 5\,\%$, illustratif, aux deux bornes) ; sinon il est arrêté comme **non jugeable**. Une fois ouvert, le point de coupure unique $c^\star = (\theta_0 + \theta_{\min})/2$ partitionne exactement $\mathbb{R}$ sans zone grise : $\hat{\theta} > c^\star$ falsifie l'hypothèse basse, $\hat{\theta} \le c^\star$ falsifie l'hypothèse haute.
3. **Seuil par trajectoire et lecture unique** : $\alpha_{\text{traj}} = 1\,\%$ (`[RAPPORTÉ]` pour $1\,\%$) est défini par trajectoire de $T = 25$ (illustratif) pas sur $n_0 = 2\,000$ (illustratif) trajectoires honnêtes. Le mode tenu à l'écart (`[RAPPORTÉ]`) n'est lu qu'une seule fois, dans `E3-cor`.

---

### Duel `E1-cor` (à faire en premier) : Validité causale et résistance au cadrage de l'oracle d'audit `[HYPOTHÈSE]`

- **Porte d'entrée d'admissibilité de l'oracle** : sur $300$ (illustratif) propositions à défaut aval diffus $d_t \in [0{,}15, 0{,}30]$ (illustratif) incluant des protocoles alternatifs valides ($d_t = 0$ mais éloignés lexicalement de la référence) et sur les $120$ (illustratif) items externes, l'oracle doit vérifier une corrélation partielle positive avec $d_t$ à similarité lexicale contrôlée et $\text{AUC}_{\text{oracle–humain}} \ge 0{,}80 \times \text{AUC}_{\text{humain–humain}}$ (illustratif, avec $\text{AUC}_{\text{humain–humain}} \ge 0{,}70$, illustratif, faute de quoi le lot externe est déclaré non jugeable). Un échec ici invalide immédiatement l'oracle actuel du programme.
- **Paramètre et hypothèses exclusives** : sur $N = 250$ (illustratif) tâches à défaut aval fixé $d_t = d_0$ par injection paramétrique contrôlée, on génère d'une part $m = 8$ (illustratif) paraphrases neutres honnêtes (contrôle de statistique d'ordre) et d'autre part $m = 8$ (illustratif) rédactions adverses optimisant le cadrage rhétorique contre un juge de substitution sans modifier les paramètres causaux du protocole. Soit $\theta_1 = \mathbb{E}[\min_{j \le m} Y_{i,j}^{\text{neutre}} - \min_{j \le m} Y_{i,j}^{\text{adverse}}] / \sigma_{\text{honnête}}$ le déplacement rhétorique net au-delà de l'effet $\text{best-of-}m$.
  - **$H_A$ (Stabilité de l'instrument)** : $\theta_1 \le 0{,}20$ écart-type (illustratif).
  - **$H_B$ (Déplaçabilité rhétorique de l'oracle)** : $\theta_1 \ge 0{,}50$ écart-type (illustratif).
  - *Règle de décision ($c_1^\star = 0{,}35$, illustratif, $\text{SE} \le 0{,}09$, illustratif)* : $\hat{\theta}_1 \le 0{,}35$ (illustratif) **falsifie $H_B$** ; $\hat{\theta}_1 > 0{,}35$ (illustratif) **falsifie $H_A$**.
- **Sous-test conditionnel de normalisation canonique** : exécuté uniquement si $H_A$ est falsifiée, et seulement si la réécriture par jumeau 8B (`[RAPPORTÉ]`) perd moins de $0{,}15$ écart-type (illustratif) de sensibilité sur les défauts *non adaptatifs* (sinon la normalisation à 8B est rejetée pour effacement du signal).
- **Contrôles négatifs** : protocoles alternatifs valides ($d_t = 0$) ; modèle 8B honnête avec consigne cachée bénigne et réglage fin bénin ($d_t = 0$) ; étiquettes humaines permutées.

---

### Duel `E2-cor` : Identifiabilité de la ligne de base différentielle studentisée et proxy inter-modèles $\eta$ `[HYPOTHÈSE]`

- **Protocole et pré-condition** : sur chaque tâche $X_t$, le jumeau honnête est tiré $m = 5$ (illustratif) fois pour former le score studentisé $Z_t^{\text{stud}} = (S(X_t, Z_t^{(A)}) - \bar{S}_5(X_t)) / (\hat{\sigma}_5(X_t) + s_0)$ (pré-condition : corrélation intra-tâche $\hat{\rho} > 1/6$, illustratif ; sinon la soustraction du jumeau est rejetée au profit d'un seuil non apparié). Le test séquentiel de martingale sur $Z_t^{\text{stud}}$ est calibré à $\alpha_{\text{traj}} = 1\,\%$ (`[RAPPORTÉ]`) sur le domaine source incluant des interventions bénignes d'entraînement.
- **Paramètre et hypothèses exclusives** : on mesure le pire taux de fausses alertes par trajectoire $\theta_2 = \max_{g \in \{G_1, G_2\}} \text{FPR}_{\text{traj}}(g)$ sur $N_g = 1\,500$ (illustratif) trajectoires ($T = 25$, illustratif) dans deux groupes hors-échantillon : $G_1 =$ modèle 8B (`[RAPPORTÉ]`) muni de **familles inédites de consignes et réglages fins bénins** sur sous-domaines scientifiques tenus à l'écart ; $G_2 =$ **second modèle ouvert honnête d'architecture distincte** apparié en compétence aval sur le domaine source (proxy inter-modèles de $\eta$).
  - **$H_A$ (Survie de la calibration différentielle studentisée)** : $\theta_2 \le 1{,}8\,\%$ (illustratif).
  - **$H_B$ (Rupture d'identifiabilité sous dérive d'intervention ou écart inter-modèles $\eta$)** : $\theta_2 \ge 3{,}0\,\%$ (illustratif).
  - *Règle de décision ($c_2^\star = 2{,}4\,\%$, illustratif, $\text{SE} \le 0{,}35\,\%$, illustratif)* : $\hat{\theta}_2 \le 2{,}4\,\%$ (illustratif) **falsifie $H_B$** ; $\hat{\theta}_2 > 2{,}4\,\%$ (illustratif) **falsifie $H_A$** (imposant que le certificat d'audit se passe de soustraction de jumeau en déploiement).
- **Contrôles négatifs** : tirage A/A pur (seconde graine nue en domaine source et cible) ; version non studentisée pour quantifier séparément l'inflation de variance $\lambda^2$.

---

### Duel `E3-cor` : Gain de dommage net des sondes internes sous obscurcissement adaptatif à budget d'audit fixé `[HYPOTHÈSE]`

- **Protocole sans biais ni paradoxe de ratio** : budget d'audit espéré fixé à $\bar{q} = 10\,\%$ (illustratif) avec plancher garanti $q_t \ge q_{\min} = 2\,\%$ (illustratif, probabilités $\mathcal{F}_{t-1}$-mesurables) et alarme séquentielle à $\alpha_{\text{traj}} = 1\,\%$ (`[RAPPORTÉ]`). Les sondes sont entraînées avec interventions bénignes et évaluées en incluant des **interventions bénignes tenues à l'écart**. Soit $\mathcal{D}(m)$ le dommage aval réel cumulé moyen non intercepté sur $K = 400$ (illustratif) trajectoires. On évalue conjointement (correction de Holm-Bonferroni à deux tests, référence à vérifier, illustratif) : (i) le pire saboteur adaptatif $\sup_{\lambda_{\text{obs}} \ge 0}$ informé des sondes, et (ii) l'**unique lecture scellée du mode tenu à l'écart** (`[RAPPORTÉ]`).
- **Paramètre et hypothèses exclusives** : $\theta_3 = \frac{\mathcal{D}^\star(\text{texte}) - \mathcal{D}^\star(\text{sonde+texte})}{\mathcal{D}(\text{audit uniforme à }\bar{q})}$, réduction du dommage réel survivant rapportée à la constante fixe d'audit uniforme (exempte d'annulation du dénominateur quand la taxe d'obscurcissement agit).
  - **$H_A$ (Gain boîte blanche effectif, par détection directe ou par taxe d'obscurcissement)** : $\theta_3 \ge 0{,}25$ (illustratif).
  - **$H_B$ (Évasion latente à faible coût ou artefact de construction purgé)** : $\theta_3 \le 0{,}10$ (illustratif).
  - *Règle de décision ($c_3^\star = 0{,}175$, illustratif, $\text{SE} \le 0{,}045$, illustratif)* : $\hat{\theta}_3 > 0{,}175$ (illustratif) **falsifie $H_B$** ; $\hat{\theta}_3 \le 0{,}175$ (illustratif) **falsifie $H_A$**. Avec la bourse, la réplication sur un modèle ouvert de $32\text{B}\text{–}70\text{B}$ (illustratif) applique la même coupure ; un rejet de $H_B$ à 8B suivi d'un rejet de $H_A$ à $32\text{B}\text{–}70\text{B}$ (illustratif) falsifie explicitement l'hypothèse d'invariance d'échelle.
- **Contrôles négatifs** : saboteur soumis à une pénalité latente de même norme projetée sur un sous-espace aléatoire orthogonal ; allocation par scores de sonde permutés conservant la distribution des $q_t$ ; consignes et réglages fins bénins inédits.

---

### Duel conditionnel `E4-cor` (avec bourse) : Supervision par juge 8B (`[RAPPORTÉ]`) d'une paire appariée $70\text{B}$ (illustratif) `[HYPOTHÈSE]`

Un saboteur de $70\text{B}$ (illustratif) est confronté à un **jumeau honnête de $70\text{B}$ (illustratif) muni d'une intervention bénigne** (neutralisant le confondant de taille), la paire étant auditée soit par l'oracle de 8B (`[RAPPORTÉ]`), soit par un oracle de $70\text{B}$ (illustratif) sur $N = 300$ (illustratif) paires à défaut aval fixé. Sur la perte de rappel $\theta_4 = \text{TPR}_{70\text{B}} - \text{TPR}_{8\text{B}}$ à $\alpha_{\text{traj}} = 1\,\%$ (`[RAPPORTÉ]`), la coupure unique $c_4^\star = 0{,}175$ (illustratif, entre $\theta_0 = 0{,}10$ et $\theta_{\min} = 0{,}25$, illustratif) oppose $H_A$ (supervision faible-vers-fort viable) à $H_B$ (plafond cognitif de l'auditeur faible).

---

## (c) Réponse à la question de l'arbitre (en une page)

### 1. Ce qui est établi
Dans les faits rapportés du domaine et du programme :
- Sur un sabotage diffus, accumuler des actions légèrement suspectes ne permet d'incriminer que si l'on connaît avec précision la suspicion d'un modèle bénin (billet du 30 avril 2025, `[RAPPORTÉ]`), car tout biais de ligne de base $\varepsilon$ croît linéairement avec l'horizon comme le signal (`[HYPOTHÈSE]`).
- Sur les tâches floues, les scores de vérité terrain sont souvent indéfinis et les garanties de contrôle ne valent que ce que vaut l'équipe rouge (`arXiv 2606.08892`, p. 2 et 10, `[RAPPORTÉ]`), tandis que la distinction entre sabotage de recherche et manque de compétence ainsi que les limites des méthodes boîte blanche sont explicitement non résolues (appel d'août 2025 ; `arXiv 2607.13087`, p. 25, `[RAPPORTÉ]`).
- Aucun détecteur mécaniste ne vaut sur tous les modèles et tâches (`arXiv 2504.08812`, p. 1, `[RAPPORTÉ]`), le raisonnement malveillant peut résider dans les activations sous une chaîne de pensée bénigne (`arXiv 2507.11473`, p. 7, `[RAPPORTÉ]`), et les défenses latentes existantes cèdent aux activations obscurcies, au prix toutefois d'une baisse de performance sur tâche complexe (`arXiv 2412.09565`, p. 1 ; `arXiv 2512.11949`, p. 1, `[RAPPORTÉ]`).
- Méthodologiquement, l'examen croisé établit trois contraintes pour la petite équipe travaillant à 8B (`[RAPPORTÉ]`) : (1) un unique mode tenu à l'écart (`[RAPPORTÉ]`) ne permet aucune estimation de variance entre genres inconnus (`[HYPOTHÈSE]`) ; (2) valider l'oracle sur des défauts définis par rapport à la référence même qu'il lit est circulaire (`[HYPOTHÈSE]`) ; (3) sans contrôles d'interventions bénignes tenues à l'écart et jumeau de même taille, les sondes et le différentiel détectent la trace mécanique de construction des saboteurs (`[HYPOTHÈSE]`).

### 2. Ce qui ne l'est pas — et le but opposable que le programme doit se donner
Il n'est **pas établi** : (a) que l'oracle du programme détecte de vraies dégradations méthodologiques hors référence synthétique et résiste au cadrage rhétorique de l'agent ; (b) qu'un jumeau studentisé survive à un changement d'intervention bénigne ou à un écart inter-modèles $\eta$ (proxy du déploiement sans vrai jumeau) ; (c) qu'après purge des artefacts de construction, l'obscurcissement des activations impose sur tâche complexe une taxe suffisante pour que les sondes réduisent le dommage réel à budget d'audit fixé (`[HYPOTHÈSE]`). En revanche, étudier des modèles de pointe naturellement comploteurs (`arXiv 2504.05259`, p. 24, `[RAPPORTÉ]`), justifier un déploiement face à des attaques surhumaines (`arXiv 2512.22154`, p. 12, `[RAPPORTÉ]`) ou évaluer sans biais d'écrasement des mitigations par entraînement (`arXiv 2606.08892`, p. 2, `[RAPPORTÉ]`) est hors de portée de ce dispositif (`[HYPOTHÈSE]`).

**Changement de cap et phrase opposable (`[HYPOTHÈSE]`)** : Le programme doit abandonner la quête d'un « système complet battant l'état de l'art » sur mondes plantés maison, geler l'extension de l'organisme d'idéation, et viser **des bornes testables et des réfutations adaptatives sur un banc causal particulier**.
> *Problématique opposable :* Face à un agent (ou essaim après validation unitaire) connaissant les moniteurs et la règle d'allocation d'audit mais ignorant l'aléa des tirages et le simulateur aval, afin de borner la perte méthodologique cumulée sur un flux de propositions d'expériences, le programme teste si **un audit aléatoire à plancher garanti $q_{\min} > 0$ jugé par un oracle causalement validé assure une borne valide au risque $\delta$, tandis que la priorisation par jumeau studentisé et sondes internes abaisse d'au moins $25\,\%$ (illustratif) le dommage réel survivant à budget d'audit égal $\bar{q}$ et $\alpha_{\text{traj}} = 1\,\%$ (`[RAPPORTÉ]` pour $1\,\%$)** ; cette thèse défensive est **réfutée** si l'oracle est déplaçable au-delà du bruit d'ordre (`E1-cor`), si la fausse alerte hors-échantillon du jumeau franchit $2{,}4\,\%$ (illustratif, `E2-cor`), ou si le gain net des sondes sous obscurcissement adaptatif tombe sous $17{,}5\,\%$ (illustratif, `E3-cor`), auquel cas le programme publie ces frontières négatives en réponse directe à l'appel d'août 2025 (`[RAPPORTÉ]`).

**Ordre révisé des papiers (`[HYPOTHÈSE]`)** : (1) *L'Instrument et la Ligne de Base* (`E1-cor` + `E2-cor`), préalable à toute sommation temporelle ; (2) *Le Temps et la Taxe d'Obscurcissement* (`E3-cor`, répliqué à $32\text{B}\text{–}70\text{B}$ illustratif avec bourse) ; (3) *Asymétrie d'Auditeur* (`E4-cor`) ou *Essaim* seulement si le cas unitaire tient. Je changerais d'avis sur ces trois choix si : (i) un banc externe objectif sans vérité plantée existait déjà et révélait un large régime furtif à 8B ; (ii) un pré-test montrait une invariance immédiate de l'oracle et du jumeau sous interventions bénignes inédites ; (iii) une sonde non supervisée transférait sans réentraînement entre familles ouvertes face à l'obscurcissement (`[HYPOTHÈSE]`).

### 3. L'expérience à faire en premier : `E1-cor` (Validité causale et non-déplaçabilité de l'oracle)
Avant d'accumuler des états internes ou de lancer des essaims, il faut exécuter `E1-cor` sur le modèle de 8B (`[RAPPORTÉ]`) avec calcul modeste (`[HYPOTHÈSE]`) : découpler l'oracle d'un simulateur méthodologique aval caché (et d'un lot externe de $120$ propositions relues en double aveugle, illustratif), vérifier qu'il sépare les vraies pertes de puissance aval ($d_t > 0$) des protocoles alternatifs légitimes ($d_t = 0$), puis mesurer sur $250$ (illustratif) tâches à dommage fixé si un cadrage rhétorique adverse abaisse le score d'oracle au-delà du minimum de $m = 8$ (illustratif) paraphrases neutres ($\hat{\theta}_1 \gtrless 0{,}35$ écart-type, illustratif). Si $\hat{\theta}_1 \le 0{,}35$ (illustratif), le socle de la garantie d'audit est validé et `E2-cor`/`E3-cor` deviennent jugeables ; si $\hat{\theta}_1 > 0{,}35$ (illustratif) sans réparation admissible, il est établi dès le premier mois (illustratif) que la garantie par oracle échoue à la racine sur tâches floues, évitant d'investir à perte dans l'accumulation temporelle et l'essaim (`[HYPOTHÈSE]`).

FIN-DE-CELLULE