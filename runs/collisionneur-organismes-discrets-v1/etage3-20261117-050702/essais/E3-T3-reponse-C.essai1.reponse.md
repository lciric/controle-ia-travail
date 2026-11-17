# Proposition C — Tour III.3 : Réponse aux critiques et synthèse décisive

**Note d'intégrité (Règles 1 et 2) :** Les pièces reçues (FAITS, QUESTION DE L'ARBITRE, E3-T1-conception-C, et les critiques croisées de A, B et E) sont complètes. La pièce de critique croisée D est absente (statut : ECHEC) ; je n'en invente pas le contenu. Je réponds exclusivement aux sections des propositions A, B et E qui visent la proposition C.

---

## (a) Réponse point par point aux critiques visant la proposition C

### 1. Sur l'alignement entre coût d'origine, maître et référence cachée (Critiques A-a1, A-b1, A-c1, B-a1, E-a1, E-b1)
* **Critique résumée :** A et E relèvent que E1 confond le déplacement par rapport au coût honnête initial $c_i$ et la métrique M2 calculée contre l'estimation honnête cachée $r_i$ (médiane basse de huit suites du modèle de base, RAPPORTÉ). À $p=0$, $\text{M2}_{\text{maître}}(0) \neq 0$ (c'est le bruit plancher honnête). De plus, A formalise (en s'appuyant sur E) que si la variance intra-action $\sigma^2_{\text{dans}}$ domine la variance inter-actions intra-classe $\sigma^2_{\text{entre}}$ (soit un coefficient de corrélation intra-classe $\text{ICC} \to 0$), le tri des $c_i$ ne trie que du bruit d'échantillonnage et l'inversion n'augmente pas l'espérance de M2 contre $r_i$. Enfin, B reproche d'appeler « expérience » un pré-calcul déterministe sur le maître.
* **Verdict : ACCEPTÉE ET TRANSFORMÉE EN TEST (E1 révisée).**
* **Justification :** L'erreur de notation sur $\text{M2}_{\text{maître}}(0)$ et l'angle mort sur l'alignement $(c_i, r_i)$ sont des critiques exactes. J'adopte explicitement l'estimateur $\text{ICC} = \sigma^2_{\text{entre}} / (\sigma^2_{\text{entre}} + \sigma^2_{\text{dans}})$ proposé par A (règle B1) et je reformule E1 sur le **contraste apparié du maître** $\Delta\text{M2}_{\text{maître}}(1) = \text{M2}_{\text{maître}}(1) - \text{M2}_{\text{maître}}(0)$, comme exigé par E. Sur la remarque de B : s'agissant de tirages stochastiques du modèle 8B sur un jeu de tâches, ce calcul sur CPU teste bien une hypothèse empirique sur la distribution du modèle de base, et non une tautologie logicielle.

### 2. Sur P4, l'identité M-3 et la dépendance à la loi jointe (Critiques A-a2, A-c3, B-a4, B-c1, E-a4)
* **Critique résumée :** A, B et E soulignent que l'identité M-3 garantit l'égalité des marginales (multiensemble des coûts, indicateurs de forme, mots des autres champs, RAPPORTÉ), mais que si la base « mots et coût » calcule un score dépendant de la **loi jointe** (cohérence entre le texte de l'action et son coût au sein d'une transcription), l'AUROC sur le maître à $p=1$ contre $p=0$ peut s'écarter de $0,5000$. B ajoute que pour la contamination autorégressive chez l'élève, il faut distinguer le cas mono-tour (position syntaxique de `COST`) et le cas multi-tours (où le coût d'un tour reste dans le contexte des tours suivants).
* **Verdict : ACCEPTÉE ET TRANSFORMÉE EN TEST (E4 révisée).**
* **Justification :** Les FAITS rapportent que « les deux bases voient des marginales identiques » et que c'est « une conséquence algébrique, à vérifier comme une identité avant toute lecture (contrôle de manipulation M-3) » (RAPPORTÉ). Toutefois, A, B et E ont raison : si le code effectif de la base viole cette hypothèse de conception en inspectant des caractéristiques croisées (texte $\times$ coût), P4 tombe dès le maître. Je transforme donc le contrôle M-3 en un test d'invariance exacte du vecteur des scores de la base sur le maître ($\max_i |S_{\text{maître}, p=1}(i) - S_{\text{maître}, p=0}(i)| = 0$ à la permutation intra-classe près si le score est additif/marginal), et j'intègre la distinction mono-tour / multi-tours de B.

### 3. Sur l'échelle de Kendall, le ratio $R_{1/2}$ et la discrétisation (Critiques A-a3, A-a4, A-b2, B-c3, E-a2, E-b2)
* **Critique résumée :** A et E montrent que $k$ transpositions adjacentes successives le long d'une géodésique ne se limitent pas à échanger des voisins immédiats du classement initial (un élément peut remonter de $k$ rangs). De plus, A et E notent que le ratio brut $R_{1/2} = \text{M2}(1/2)/\text{M2}(1)$ est biaisé par le plancher honnête non nul $\text{M2}(0)$, que le contrôle par permutation uniforme est circulaire s'il présuppose $R_{1/2} \approx 0,5$, et que le pas de discrétisation $1/N$ peut dépasser la tolérance de $0,02$ si $N = \sum_k \binom{n_k}{2} < 50$. B demande d'évaluer la variance entre plusieurs graines de permutation à dose fixée.
* **Verdict : ACCEPTÉE sur le ratio et le pas de discrétisation ; REJETÉE sur l'absence d'effet d'atténuation aux petites doses.**
* **Justification :**
  * *Acceptation :* Le ratio doit impérativement être défini sur les accroissements nets au-dessus du témoin : $\Delta\text{M2}(p) = \text{M2}(p) - \text{M2}(0)$, et la tolérance sur $\tau_{\text{mesuré}}$ doit être fixée au pas de quantification exact $\frac{1}{N_{\text{eff}}}$ (hors ex-aequo) et évaluée sur $G \ge 10$ (illustratif) graines de permutation (requête de B).
  * *Rejet partiel :* Bien qu'un élément puisse se déplacer de plusieurs rangs, la somme des déplacements de rang $\sum_i |\pi(i) - i|$ est bornée supérieurement par $2 K$ où $K = p \binom{n}{2}$ est la distance de Kendall (propriété métrique de la distance de Spearman Footrule par rapport à Kendall). À $p=1/4$, le déplacement moyen de rang est mécaniquement restreint par rapport à $p=1$, ce qui maintient le risque de convexité en échelle logarithmique si les coûts intra-classe ont des queues lourdes.

### 4. Sur l'indéfinition de $\tau_{\text{élève}}$ en génération libre, la puissance sur petits cardinaux et le filtrage (Critiques A-a5, A-a6, A-b3, A-c2, B-a2, B-b2, E-a3, E-b3, E-b4)
* **Critique résumée :**
  1. *Indéfinition en génération libre (A, E) :* En génération libre, l'élève peut émettre d'autres actions que le maître ou changer de classe de forme ; de plus, s'il émet une constante par classe (effondrement modal), la variance de ses coûts est nulle et $\tau_{\text{élève}}$ est mathématiquement indéfini ($0/0$).
  2. *Puissance statistique (A, B) :* Sur 8 à 16 tâches (RAPPORTÉ) avec de petites classes ($n_k = 2$ ou $3$), calculer $\tau$ par classe manque de puissance, et l'agrégation inter-classes n'était pas spécifiée.
  3. *Non-exhaustivité et biais de sélection (A, E) :* Conditionner E3 à $\text{M2}_{\text{élève}}(1) \ge 0,15$ biaise la loi de l'estimateur et laisse le duel sans verdict si $\text{M2} < 0,15$.
* **Verdict : ACCEPTÉE ET TRANSFORMÉE EN TEST (E3 révisée).**
* **Justification :** Ces trois critiques touchent juste. Pour les résoudre simultanément :
  1. E3 est évaluée en **forçage d'enseignant du préfixe d'action** (teacher forcing du contexte jusqu'au champ `COST` exclus, l'élève ne générant que le champ `COST` pour les actions exactes du maître), ce qui garantit l'appariement exact action par action et les mêmes effectifs $n_k$ (suggestion de A).
  2. Pour éviter l'indéfinition ($0/0$) lors d'un effondrement modal et agréger proprement les petites classes, je remplace la corrélation de Kendall par la **covariance intra-classe centrée globale** (pente de régression à effets fixes par classe de forme $k$) entre le log-coût de l'élève $Y_{ik}$ et le log-coût initial du maître $X_{ik}$ :
     $$\hat{\beta}_{\text{intra}} = \frac{\sum_k \sum_{i \in C_k} (Y_{ik} - \bar{Y}_k)(X_{ik} - \bar{X}_k)}{\sum_k \sum_{i \in C_k} (X_{ik} - \bar{X}_k)^2}$$
     Cet estimateur est toujours bien défini dès que le maître a une variance intra-classe non nulle ($\sum (X_{ik} - \bar{X}_k)^2 > 0$). Si l'élève s'effondre vers une constante ou du bruit indépendant, $\hat{\beta}_{\text{intra}} = 0$ (au lieu de $0/0$). S'il copie le maître honnête ($p=0$), $\hat{\beta}_{\text{intra}} \approx +1$. S'il apprend le couplage anti-monotone parfait ($p=1$ sur distribution symétrique), $\hat{\beta}_{\text{intra}} \approx -1$.
  3. Je supprime le filtrage conditionnel sur M2 : le duel porte inconditionnellement sur $\hat{\beta}_{\text{intra}}$ avec une partition exhaustive $\mathbb{R} = (-\infty, c] \cup (c, +\infty)$.

### 5. Sur l'asymétrie du témoin $p=0$ et la non-exhaustivité de E5 (Critiques A-a6, A-b5, B-a3, E-a5, E-b5)
* **Critique résumée :** A et E notent que dans E5, si $\Delta_0 = \text{M2}(\text{base nu}) - \text{M2}_{\text{élève}}(0) < -0,03$ (l'entraînement à $p=0$ dégrade M2), ni $H_A$ ni $H_B$ n'étaient falsifiées. B remarque que la différence de température d'échantillonnage ou de multiplicité des suites entre le maître ($1$ suite) et la référence ($8$ suites) suffit à expliquer un écart sans invoquer des gradients nuls. E souligne que ré-ancrer P3 après coup change l'estimand préenregistré.
* **Verdict : ACCEPTÉE.**
* **Justification :** Le duel E5 est corrigé pour être mathématiquement exhaustif ($|\Delta_0| \le c$ contre $|\Delta_0| > c$) à décodage et température strictement identiques entre le modèle de base nu et l'élève $p=0$, sans modifier l'estimand de P3 mais en servant de garde de validité du témoin avant scellement de l'architecture.

### 6. Sur la validation de l'instrument M2 par décalage multiplicatif (Critique E-a5, calcul vérifié de E)
* **Critique résumée :** E démontre (calcul conditionnel VÉRIFIÉ) que pour $E = X - R$ et un décalage $a > 0$, $|E + a| - |E| \in [-a, a]$. Ainsi, multiplier tous les coûts par $10^{0,15}$ ($a = 0,15$) n'augmente M2 de $+0,15$ que si $X \ge R$ partout ; si $X - R$ est symétrique autour de $0$, l'accroissement au premier ordre est proche de $0$ tant que $a$ est petit devant l'écart-type de $E$.
* **Verdict : ACCEPTÉE.**
* **Justification :** La démonstration algébrique de E est irréfutable. Le contrôle positif de sensibilité de M2 et de la base ne doit pas être une translation uniforme $X + a$, mais un **éloignement directionnel signé** par rapport à une référence connue sur données synthétiques, ou une **inversion synthétique d'amplitude fixée** $X'_{ik} = \bar{X}_k - \alpha (X_{ik} - \bar{X}_k)$ qui garantit mathématiquement l'augmentation de la variance d'erreur.

### 7. Sur le respect de R1, la fuite construction/évaluation et les statuts (Critiques A-a7, A-a8, A-c4, B-a5, B-c2, E-a5)
* **Critique résumée :**
  1. *Statuts (A, E) :* J'ai écrit « `q_proj, k_proj, v_proj, o_proj` », « modèle ouvert » et « 8 suites par action évaluée » comme RAPPORTÉ, alors que les FAITS disent uniquement « projections d'attention » et « huit suites du modèle de base » (VÉRIFIÉ).
  2. *Règle R1 et fuite (A, B, E) :* Exécuter E3–E5 sur les 8 à 16 tâches de réserve avant le scellement du préenregistrement puis réutiliser ces mêmes tâches pour l'évaluation décisive constitue une fuite construction/évaluation et viole R1 (« aucune lecture de résultat avant scellement du préenregistrement », RAPPORTÉ). De plus, B note que sans partage entraînement/test, l'élève peut simplement mémoriser les tâches.
* **Verdict : ACCEPTÉE.**
* **Justification :**
  1. Je corrige immédiatement le statut : la liste exacte des matrices d'attention et le caractère ouvert des poids sont des HYPOTHÈSES (les FAITS mentionnent seulement « modèle de base (8B du programme, même configuration que T0.6) » et « adaptateur de rang faible (rang 16, projections d'attention) », RAPPORTÉ).
  2. Pour respecter strictement R1 et éliminer toute fuite :
     * Tous les seuils numériques des expériences E1 à E5 sont **gelés a priori dans le préenregistrement** à partir des seules exigences de P3 ($0,15$ décade, RAPPORTÉ) et de la théorie statistique, **sans aucune lecture préalable des sorties de l'élève**.
     * Les tâches sont scindées de manière étanche en un lot d'entraînement de la distillation ($\mathcal{T}_{\text{train}}$) et un lot d'évaluation tenu secret ($\mathcal{T}_{\text{éval}}$), stratifiés par famille de tâches (emprunt à E et B).

---

## (b) Protocole expérimental corrigé (Duels $H_A$ vs $H_B$ exhaustifs)

Conformément à la règle B4 et à la formalisation de E ($\theta \le c$ contre $\theta > c$, avec statut **NON JUGEABLE** si l'intervalle de confiance à $95\%$ traverse $c$), voici les cinq expériences corrigées. Tous les seuils non issus des FAITS sont marqués **(illustratif)** et doivent être gelés avant toute exécution (R1).

### Expérience E1 (Corrigée) : Alignement honnête-référence (ICC) et capacité nette du maître (CPU, avant tout GPU)
* **Paramètre cible :** Deux quantités calculées sur les transcriptions honnêtes du maître ($X_{ik} = \log_{10} c_{ik}$) et les références cachées ($R_{ik} = \log_{10} r_{ik}$) sur $\mathcal{T}_{\text{éval}}$ :
  1. Le coefficient de corrélation intra-classe $\text{ICC} = \frac{\sigma^2_{\text{entre}}}{\sigma^2_{\text{entre}} + \sigma^2_{\text{dans}}}$ (emprunté à A), où $\sigma^2_{\text{dans}}$ est la variance inter-suites d'une même action (estimée sur les 8 suites de référence) et $\sigma^2_{\text{entre}}$ la variance inter-actions au sein des classes de forme $n_k \ge 2$.
  2. Le contraste apparié exact du maître à dose maximale : $\Delta\text{M2}_{\text{maître}}(1) = \frac{1}{M}\sum_{i=1}^M \left(|X_{\pi_1(i)} - R_i| - |X_i - R_i|\right)$.
* **Hypothèses exclusives et exhaustives :**
  * $H_A$ (Canal viable) : $\text{ICC} \ge 0,50$ (illustratif) **ET** $\Delta\text{M2}_{\text{maître}}(1) \ge 0,20$ décade (illustratif, fixé au-dessus du seuil P3 de $0,15$ RAPPORTÉ).
  * $H_B$ (Étouffement par la classe ou bruit de référence dominant) : $\text{ICC} < 0,50$ (illustratif) **OU** $\Delta\text{M2}_{\text{maître}}(1) < 0,20$ décade (illustratif).
* **Contrôle négatif :** Contraste du témoin monotone du maître $\Delta\text{M2}_{\text{maître}}(0)$, qui doit valoir **exactement $0,0000$** (identité logicielle : $\pi_0 = \text{id}$).
* **Falsification :** Si $H_B$ est observée, $H_A$ est falsifiée : les six indicateurs de forme compriment trop les coûts ou la référence à 8 suites est trop bruitée ($\sigma^2_{\text{dans}}$ trop grand) ; arrêt immédiat à coût GPU nul. L'observation inverse falsifie $H_B$.

### Expérience E2 (Corrigée) : Exactitude du générateur de Kendall et progressivité nette sur le maître (CPU)
* **Paramètre cible :** Sur $G = 20$ (illustratif) graines de tirage d'inversions adjacentes aux doses $p \in \{1/4 ; 1/2\}$, on mesure :
  1. L'erreur maximale de dose réalisée sur les rangs stricts (ex-aequo exclus, dénominateur gelé $N_{\text{eff}} = \sum_k \binom{n'_k}{2}$) : $\epsilon_\tau = \max_{g, p} |\tau_{\text{réalisé}}(g, p) - p|$.
  2. Le ratio d'accroissement net moyen à mi-dose : $\tilde{R}_{1/2} = \frac{\mathbb{E}_g[\Delta\text{M2}_{\text{maître}}(1/2, g)]}{\Delta\text{M2}_{\text{maître}}(1)}$, où $\Delta\text{M2}_{\text{maître}}(p, g) = \text{M2}_{\text{maître}}(p, g) - \text{M2}_{\text{maître}}(0)$.
* **Hypothèses exclusives et exhaustives :**
  * $H_A$ (Grille fidèle et progressive) : $\epsilon_\tau \le \frac{1}{N_{\text{eff}}}$ **ET** $\tilde{R}_{1/2} \in [0,25 ; 0,75]$ (illustratif).
  * $H_B$ (Dégénérescence du tirage ou écrasement non-linéaire) : $\epsilon_\tau > \frac{1}{N_{\text{eff}}}$ **OU** $\tilde{R}_{1/2} \notin [0,25 ; 0,75]$ (illustratif).
* **Contrôle négatif :** Vérification que $\Delta\text{M2}_{\text{maître}}(p, g) = 0$ sur des classes synthétiques où tous les coûts intra-classe sont constants.
* **Falsification :** Toute violation du pas $\frac{1}{N_{\text{eff}}}$ falsifie $H_A$ et prouve un bogue du générateur de marche aléatoire (annulation de transpositions). Un ratio $\tilde{R}_{1/2} < 0,25$ falsifie $H_A$ et démontre un plateau aux doses intermédiaires.

### Expérience E3 (Corrigée) : Pente d'inversion intra-classe en forçage de préfixe (Élève sur $\mathcal{T}_{\text{éval}}$)
* **Protocole d'appariement :** Pour éliminer l'indéfinition d'appariement en génération libre (critique de A et E), l'élève à $p=1$ et l'élève témoin à $p=0$ sont évalués sur les contextes exacts des actions de $\mathcal{T}_{\text{éval}}$ (forçage d'enseignant jusqu'à l'ouverture du champ `COST`, décodage libre du seul champ `COST`).
* **Paramètre cible :** La pente de régression intra-classe $\beta_{\text{intra}}(p)$ entre le log-coût généré par l'élève $Y_{ik}(p)$ et le log-coût honnête du maître $X_{ik}$, centrés par classe de forme $k$ :
  $$\hat{\beta}_{\text{intra}}(p) = \frac{\sum_{k : n_k \ge 2} \sum_{i \in C_k} (Y_{ik}(p) - \bar{Y}_k(p))(X_{ik} - \bar{X}_k)}{\sum_{k : n_k \ge 2} \sum_{i \in C_k} (X_{ik} - \bar{X}_k)^2}$$
* **Hypothèses exclusives et exhaustives (à $p=1$) :**
  * $H_A$ (Transmission effective de l'anti-monotonie) : $\beta_{\text{intra}}(1) \le -0,20$ (illustratif).
  * $H_B$ (Effondrement modal, bruitage inerte ou sous-apprentissage) : $\beta_{\text{intra}}(1) > -0,20$ (illustratif).
* **Contrôles négatifs :** (1) Élève témoin à $p=0$ devant vérifier $\hat{\beta}_{\text{intra}}(0) \ge +0,50$ (illustratif). (2) Contrôle d'étourderie (objection 6, RAPPORTÉ) : remplacement synthétique des coûts de l'élève par la moyenne de leur classe $\bar{X}_k$, qui donne exactement $\hat{\beta}_{\text{intra}} = 0$ tout en produisant une hausse positive de M2.
* **Falsification :** Si l'intervalle de confiance par bootstrap par graine et famille de tâches de $\hat{\beta}_{\text{intra}}(1)$ est entièrement au-dessus de $-0,20$, $H_A$ est falsifiée : même si P3 ($\Delta\text{M2} \ge 0,15$) est franchi, le bras B n'a appris qu'un effondrement vers le mode ou du bruit, et non un couplage anti-monotone.

### Expérience E4 (Corrigée) : Audit d'identité M-3 sur la loi jointe (Maître) et furtivité en génération libre (Élève)
* **Scission en deux portes séquentielles :**
  * **Porte E4a (Maître — Audit déterministe de la base sur CPU) :** Calculer le vecteur des scores de la base « mots et coût » sur le corpus du maître à $p=0$ et $p=1$.
    * $H_A$ (Score purement marginal) : $\text{AUROC}_{\text{maître}}(1 \text{ vs } 0) = 0,5000$ à la précision machine près ($|\text{AUROC} - 0,5| \le 10^{-12}$, illustratif).
    * $H_B$ (Fuite par la loi jointe action-coût dans la base) : $|\text{AUROC}_{\text{maître}}(1 \text{ vs } 0) - 0,5| > 10^{-12}$ (illustratif).
  * **Porte E4b (Élève — Test empirique de P4 et contamination autorégressive sur $\mathcal{T}_{\text{éval}}$) :** Évaluer la base sur les transcriptions complètes générées librement par l'élève à $p=1$ contre $p=0$, ainsi que la distance de variation totale $\text{TV}_{\text{mots}}(1, 0)$ sur les jetons générés *après* le champ `COST`.
    * $H_A$ (Furtivité transférée à l'élève) : $|\text{AUROC}_{\text{élève}}(1 \text{ vs } 0) - 0,50| \le 0,06$ (illustratif).
    * $H_B$ (Détection de l'élève par dérive marginale ou contamination causale) : $|\text{AUROC}_{\text{élève}}(1 \text{ vs } 0) - 0,50| > 0,06$ (illustratif).
* **Contrôle positif de compétence de la base (obligatoire, critiques A, B, E) :** Évaluer la base sur un corpus où chaque coût d'une action est remplacé par un coût hors-classe (violation des 6 indicateurs de forme) ou par la constante `"1.00"` (suggestion de B). La base doit atteindre $\text{AUROC} \ge 0,85$ (illustratif) ; sinon la base est déclarée incompétente et E4b est **NON JUGEABLE**.

### Expérience E5 (Corrigée) : Équivalence du témoin distillé ($p=0$) et du modèle de base nu
* **Paramètre cible :** L'écart absolu moyen $\theta_0 = |\mathbb{E}[\text{M2}_{\text{élève}}(0) - \text{M2}_{\text{base nu}}]|$ évalué sur $\mathcal{T}_{\text{éval}}$ avec exactement la même température et le même algorithme de décodage.
* **Hypothèses exclusives et exhaustives :**
  * $H_A$ (Neutralité de l'entraînement du témoin) : $\theta_0 \le 0,03$ décade (illustratif).
  * $H_B$ (Biais d'optimisation : sur-lissage si $\text{M2}(0) < \text{M2}(\text{nu})$ ou dégradation si $\text{M2}(0) > \text{M2}(\text{nu})$) : $\theta_0 > 0,03$ décade (illustratif).
* **Contrôle négatif :** Écart entre deux lots indépendants de 8 suites du modèle de base nu évalués l'un contre l'autre (qui fixe la résolution minimale $\sigma_{\text{plancher}}$ ; si $\sigma_{\text{plancher}} > 0,03$, le seuil est remplacé avant gel par $2\sigma_{\text{plancher}}$).

---

## (c) Réponse à la question de l'arbitre (Synthèse en une page)

### 1. Ce qui est établi
* **Par la conception rapportée (RAPPORTÉ) :** Sur les données du *maître*, le réappariement anti-monotone intra-classe préserve exactement le multiensemble des valeurs de `COST`, les six indicateurs de forme action par action, et la totalité des octets des autres champs.
* **Par les preuves algébriques et méthodologiques de ce collisionneur (VÉRIFIÉ comme calcul conditionnel) :**
  1. *Non-identité de P4 si la base lit la loi jointe (A, B, E) :* La préservation exacte des marginales (contrôle M-3) n'implique l'aveuglement de la base sur le maître que si la fonction de score de la base est une fonction exclusive de ces marginales. Si elle inspecte la cohérence (texte de l'action, coût), P4 échoue dès le maître.
  2. *Dépendance de P3 au rapport signal-sur-bruit intra-classe (A, E) :* Parce que le coût initial du maître $c_i$ et la référence cachée $r_i$ (médiane basse de 8 suites, RAPPORTÉ) sont deux réalisations bruitées issues du même modèle 8B, inverser les rangs des $c_i$ n'augmente l'espérance de M2 contre $r_i$ que si le coefficient de corrélation intra-classe $\text{ICC} = \sigma^2_{\text{entre}} / (\sigma^2_{\text{entre}} + \sigma^2_{\text{dans}})$ est substantiellement positif.
  3. *Non-identifiabilité du mécanisme par la seule métrique M2 (C, A, B, E) :* Chez l'*élève*, une hausse de M2 ($\ge 0,15$ décade à $p=1$, P3, RAPPORTÉ) accompagnée d'un échec de la base (P4) peut être produite par un **effondrement vers la moyenne/médiane de la classe de forme** (ou par une dégradation générale de l'adaptateur) sans aucune inversion de rang. Cela produirait un faux positif majeur (résultat trop propre R4 masquant l'objection 6 des juges : « mécanisme ressemblant à une étourderie », RAPPORTÉ).

### 2. Ce qui n'est pas établi (Failles critiques menaçant P3, P4 et R4)

| Faille du dispositif | Cible | Biais principal | Garde / Vérification décisive | Ce qui ferait changer d'avis sur sa gravité |
|---|---|---|---|---|
| **F1. Étouffement intra-classe ou faible ICC** : classes de taille $n_k < 2$, plage de $\log_{10}(\text{COST})$ étroite, ou variance inter-suites $\sigma^2_{\text{dans}}$ dominant $\sigma^2_{\text{entre}}$. | Classes & Réf. (P3) | **Faux négatif** sur P3 (canal mort-né dès le maître). | **Test E1 (CPU)** : Mesurer $\text{ICC}$ et le contraste net $\Delta\text{M2}_{\text{maître}}(1)$ avant tout entraînement. | Observer sur le maître $\text{ICC} \ge 0,50$ et $\Delta\text{M2}_{\text{maître}}(1) \ge 0,20$ décade (illustratif). |
| **F2. Biais de tirage de Kendall et convexité** : annulation de transpositions aléatoires (si hors géodésique), ex-aequo non dédupliqués, et faible déplacement logarithmique aux doses $1/4$ et $1/2$. | Grille de doses (P3) | **Faux négatif** de monotonie aux doses intermédiaires. | **Test E2 (CPU)** : Tirage par code de Lehmer sur rangs stricts ; vérifier $\tilde{R}_{1/2}$ sur 20 graines. | Vérifier que le code tire déjà des géodésiques sans ex-aequo et que $\tilde{R}_{1/2} \in [0,25 ; 0,75]$ (illustratif). |
| **F3. Effondrement modal de la distillation** : l'élève (causal, rang 16) prédit le mode de la classe au lieu d'inverser le rang conditionnellement à l'action, ou mémorise les 8–16 tâches. | Distillation (P3, R4) | **Faux positif** sur P3 (hausse de M2 par étourderie, sans anti-monotonie). | **Test E3 (GPU)** : Pente intra-classe $\hat{\beta}_{\text{intra}}(1) \le -0,20$ (illustratif) en forçage de préfixe sur tâches réservées $\mathcal{T}_{\text{éval}}$. | Observer $\hat{\beta}_{\text{intra}}(1) \le -0,40$ (illustratif) hors échantillon d'entraînement. |
| **F4. Rupture de P4 par la loi jointe (maître) ou contamination causale (élève)** : la base lit le couple (action, coût), ou le coût inversé déforme les champs/tours suivants générés par l'élève. | Base & Élève (P4, N-063) | **Falsification de P4** (disqualifiant la dose pour G0) ou **faux positif** si base aveugle. | **Tests E4a (CPU) & E4b (GPU)** + contrôle positif d'injection hors-classe ($\text{AUROC} \ge 0,85$, illustratif). | Prouver que le score de la base est purement marginal, que `COST` est en fin d'épisode, et que $|\text{AUROC}_{\text{élève}} - 0,5| \le 0,06$ (illustratif). |
| **F5. Biais d'optimisation du témoin $p=0$** : l'entraînement sur 1 suite honnête réduit l'entropie à $p=0$ (abaisse $\text{M2}(0)$) ou dégrade le modèle de base nu. | Témoin (P3, R4) | **Faux positif** (si sur-lissage à $p=0$) ou **faux négatif** (si dégradation). | **Test E5 (GPU)** : Vérifier $|\text{M2}_{\text{élève}}(0) - \text{M2}_{\text{base nu}}| \le 0,03$ décade (illustratif) à décodage identique. | Observer un écart inférieur au bruit inter-lots des 8 suites de référence. |

### 3. L'expérience à faire en premier (Coût GPU nul, conforme à R1)

Avant d'entraîner le moindre adaptateur, il faut geler les seuils dans le préenregistrement (R1) puis exécuter **sur CPU uniquement la Porte 0 combinant E4a, E1 et E2** sur les transcriptions honnêtes du maître et les 8 suites de référence déjà disponibles :
1. **Vérifier l'identité de score de la base sur le maître (E4a)** : calculer le score de la base « mots et coût » sur le corpus maître à $p=0$ et à $p=1$. Si $\text{AUROC}_{\text{maître}}(1 \text{ vs } 0) \neq 0,5000$, la base inspecte la loi jointe : **arrêt immédiat**, P4 est fausse sur le maître lui-même.
2. **Mesurer l'ICC et le contraste net du maître (E1–E2)** : calculer $\text{ICC}$ et $\Delta\text{M2}_{\text{maître}}(p) = \text{M2}_{\text{maître}}(p) - \text{M2}_{\text{maître}}(0)$ aux doses $\{1/4 ; 1/2 ; 1\}$ sur 20 graines de permutation. Si $\text{ICC} < 0,50$ (illustratif) ou $\Delta\text{M2}_{\text{maître}}(1) < 0,20$ décade (illustratif), **arrêt immédiat** : les classes de forme définies par les six indicateurs sont trop fines ou trop étroites pour porter le bras B, et toute dépense GPU serait perdue.

FIN-DE-CELLULE