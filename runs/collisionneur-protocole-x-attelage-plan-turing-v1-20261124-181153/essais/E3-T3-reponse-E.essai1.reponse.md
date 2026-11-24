# Proposition E — Tour III.3 : réponse aux critiques et conception corrigée

**Constat de pièces et discipline de statuts (`VÉRIFIÉ`).** Les pièces `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-E` et les critiques croisées `A`, `B`, `C`, `D` sont présentes, non vides et complètes ; `FAITS` et `QUESTION DE L'ARBITRE` sont identiques et ne contiennent aucune donnée expérimentale. Je ne réponds qu'aux sections visant la proposition E. Pour corriger l'ambiguïté de statuts relevée par A, chaque énoncé porte ici un statut unique : `VÉRIFIÉ` (constat direct des pièces ou identité mathématique sous les conditions écrites), `RAPPORTÉ` (résultat attribué à une référence vérifiable), `OBSERVÉ-NON-AUDITÉ` (pratique empirique non auditée) ou `HYPOTHÈSE` (choix de conception, conjecture ou paramètre). Je ne modifie pas les statuts figurant dans les pièces reçues. Tous les chiffres choisis par conception sont marqués `illustratif`.

---

## (a) Traitement de chaque critique visant la proposition E

### Critiques de A sur E

1. **Doubles étiquettes et P1 marqué « RAPPORTÉ » sans source (remarque de statut).** **Acceptée.** La pièce E3-T1 comportait des étiquettes composites ambiguës et attribuait l'instabilité de représentation en P1 sans citation explicite (le fait de référence est la dépendance de la complexité descriptive au langage de codage : Solomonoff, 1964, `RAPPORTÉ`). Discipline d'étiquette unique appliquée ci-dessous.
2. **A(a)1 — Estimande $R$ double ($-\log_2 \hat{p}_Q$ ou $B_{0,5}$), censure de $B_{0,5}$, $\hat{p}=0 \implies R=\infty$.** **Acceptée.** $B_{0,5}$ et $-\log_2 \hat{p}$ ponctuel sont abandonnés au profit d'une certification unique par borne supérieure unilatérale de Clopper–Pearson (Clopper & Pearson, 1934, `RAPPORTÉ`) sur tirages disjoints.
3. **A(a)2 & A(c)1 — $U(P,B)$ en $\max$ sur $\mathcal{S}$ croît en $\sigma\sqrt{2\ln m}$ ; absence de contrôle spam à $m$ apparié.** **Acceptée.** Remplacé par l'évaluation scellée d'une **nomination unique** $\hat{x}_1$ choisie avant ouverture du coffre, avec contrôle négatif « bras spam » en E1.
4. **A(a)3 & A(c)5 — Contrôle négatif de E5 (petit espace énumérable) non jugeable sous $U$ ($U \equiv 0$).** **Acceptée.** Sur ce régime, la supériorité de l'énumérateur est vérifiée sur $D_{\text{ext}}$ seul, tandis que $Y \equiv 0$ vérifie l'absence de faux positifs d'étroitesse.
5. **A(a)4 & A(c)4 — E3 circulaire (entropie d'échec de la baseline), pseudo-répliqué (4 familles), et « petit combinatoire » trivial.** **Acceptée** sur la circularité et la pseudo-réplication (descripteurs calculés sur un modèle/graine disjoint selon la suggestion de A ; unité d'analyse portée à la famille avec $F = 16$ familles `illustratif`). **Rejetée partiellement** sur l'inutilité du petit combinatoire : ce régime est retiré du calcul d'interaction de la taxonomie (où l'on utilise des négatifs non triviaux), mais conservé comme contrôle de calibration budgétaire vérifiant que l'énumérateur n'est pas bridé.
6. **A(a)5 — E2 fusionne trois hypothèses (codage, juge, contamination).** **Acceptée.** E2 est scindée en trois expériences indépendantes : E2a, E2b et E2c.
7. **A(a)6 & A(c)3 — $\Delta_{\text{mém}}$ confond mémoire et notation ; contrôle « fuis » mal nommé (c'est un contrôle positif).** **Acceptée.** E2c soustrait le coût pur de notation estimé sur problèmes synthétiques garantis inédits (suggestion de A) et requalifie les problèmes fuis en contrôle positif de sensibilité.
8. **A(a)7 & A(c)2 — E4 teste l'utilité du retour plutôt que l'intégrité de la mesure ; $R$ remesuré sur la référence exposée.** **Transformée en test.** E4 teste désormais directement l'intégrité de la mesure via le découplage entre la référence exposée $\mathcal{Q}_0$ et un **panel de référence secret $\mathcal{Q}'$** (emprunté à A), couplé à l'écart train/OOD.
9. **A(a)8 — Règle incohérente ($\max_b U_b$ vs Holm ; enveloppe par problème irréalisable).** **Acceptée.** Remplacée par un test d'intersection-union (IUT ; Berger, 1982, `RAPPORTÉ`) exigeant de battre chaque baseline individuellement.
10. **A(a)9 — Tirages de référence de $R$ non budgétés.** **Acceptée.** Intégrés explicitement au tableau des coûts ($K_{\text{ref}}$ tirages courts par problème et par politique).
11. **A(a)10 — Contradiction sur A/A (« graines identiques » en E1 vs « graines distinctes » en table (c)).** **Acceptée.** Erreur rédactionnelle corrigée : A/A utilise exclusivement des campagnes indépendantes à graines distinctes.
12. **A(b) — Pertes de puissance (zéro-inflation et seuils en $\sigma$, *style-swap* sur 200 paires exigeant $r \ge 0{,}935$, limites de PPI, AUROC scalaire/VPP faible à $\pi = 0{,}01$, dépendance d'échelle de l'AUDC).** **Acceptée.** Abandon des seuils en $\sigma$, de l'AUDC primaire et de l'AUROC agrégé ; passage à une métrique binaire absolue $Y$, plafonds FPR calibrés par l'identité de Bayes (`VÉRIFIÉ`), dimensionnement dédié du *style-swap* en unités absolues, et relégation du juge+PPI au module optionnel E2b.

### Critiques de B sur E

1. **B(a)1 & B(c)2 — $R$ ponctuel, exécutions non explicitement disjointes, biais de sélection.** **Acceptée.** Exécutions de référence strictement disjointes imposées, plus contrôle négatif « étroitesse par sélection » (emprunté à B) en E1.
2. **B(a)2 & B(c)3 — $U$ court-circuite le sélecteur et croît avec $|\mathcal{S}|$ ; absence de bras à volume gratuit.** **Acceptée** (même correction par nomination scellée $\hat{x}_1$ + bras volume gratuit en E1).
3. **B(a)3 — Égalisation simultanée FLOPs/USD et appels oracle impossible entre LLM et énumérateur.** **Acceptée.** Scission explicite du duel en deux régimes distincts : E5a (coût financier/calcul total égal, appels oracle libres pour l'énumérateur) et E5b (appels oracle égaux, pour oracles coûteux).
4. **B(a)4 — Biais de Jensen de l'enveloppe par problème et redondance de Holm.** **Acceptée** (corrigé par IUT).
5. **B(a)5 — Seuils en $\sigma$ dépendants des données.** **Acceptée** (seuils absolus pré-enregistrés).
6. **B(a)6 — Pseudo-réplication de E3 (4 familles) et transfert non testé 8B $\to$ 70B.** **Acceptée** pour la pseudo-réplication ; **Transformée en test** pour le transfert d'échelle (sous-lot dédié de 4 familles `illustratif` vérifiant la conservation du signe entre 8B et 70B avant E5).
7. **B(a)7 — E2 agrège trois hypothèses.** **Acceptée** (scindée en E2a, E2b, E2c).
8. **B(a)8 — Puissance calculée contre 0 au lieu de $\delta_5$.** **Acceptée.** Toutes les tailles d'échantillon sont recalculées contre la marge $\delta_{\min} > 0$ avec la variance des paires discordantes.
9. **B(a)9 — P1 « RAPPORTÉ » sans référence.** **Acceptée** (corrigé, voir A.1).
10. **B(a)10 & B(c)1 — Borne de handicap lorsque $Q_{\text{LLM-1}}$ est aussi le bras Best-of-$K$ au même budget ; absence de CN-1 et CN-2.** **Acceptée.** Corrigée par deux verrous (empruntés à B) : (i) budget de référence court $b_{\text{ref}} \ll B$ pour $\mathcal{Q}_0$ + vérification de sensibilité en retirant chaque référence une à une ; (ii) inclusion obligatoire de **CN-1 (divergence triviale)** comme baseline en E5 et de **CN-2 (chasseur d'étroitesse)** comme attaque en E1.
11. **B(b) — Pertes de puissance ($R$ infinis, bootstrap sur max à queue lourde, PPI si $n\pi < 10$, arrêt pour futilité prématuré à 50 %).** **Acceptée.** Métrique primaire bornée $\{0,1\}$ (variance finie $\le 1/4$, `VÉRIFIÉ`), porte $n\hat{\pi} \ge 10$ (`illustratif`) sur E2b, et conditionnement de l'analyse intermédiaire en E5 à un minimum de paires discordantes $n_{\text{disc,min}}$.

### Critiques de C sur E

1. **C(a)1 — Plancher $\tau_D$ absent de la formule de $U$.** **Acceptée.** Intégré explicitement dans $Y_m(P,B)$.
2. **C(a)2 — Le coffre privé sert de sélecteur si $\mathcal{S}$ est le vivier.** **Acceptée** (corrigé par nomination scellée $\hat{x}_1$).
3. **C(a)3 — Une extension non dominée de Pareto n'est pas une domination.** **Acceptée.** Abandon de la clause ambiguë d'extension de Pareto ; victoire définie séparément dans le régime E5a ou E5b.
4. **C(a)4 & C(c) — Réutilisation en E5 des familles choisies par E3 (effet conditionnel).** **Acceptée.** E5 porte exclusivement sur des **familles neuves hors échantillon** tirées selon la règle gelée en E3.
5. **C(a)5 — PPI d'une moyenne ne corrige pas un maximum de scores bruités.** **Acceptée.** PPI n'est jamais appliqué à un maximum ; il ne porte que sur l'espérance de $Y$ de la nomination $\hat{x}_1$ en E2b.
6. **C(b)1–C(b)4 — $B_{0,5}$ censuré ; AUC sur mélange masquant un leurre ; EIG dépendant de l'a priori ; variance résiduelle $\text{Var}(Y-J)/n$ en PPI.** **Acceptée** sur les quatre points ; la dépendance de l'EIG à l'a priori est **transformée en test** de sensibilité minimax sur un ensemble pré-enregistré d'a priori admissibles pour les protocoles expérimentaux.
7. **C(b)5 — Non-identifiabilité rappel vs déduction par le seul contraste de renommage.** **Rejetée comme défaut du harnais principal, acceptée comme limite de la rétrodiction.** La pièce E3-T1 excluait déjà la rétrodiction seule comme preuve décisive pour des LLM (Q2) ; le harnais principal repose sur des mondes synthétiques et formels générés procéduralement post-entraînement (contamination littérale nulle par construction). Pour les benchmarks existants, E2c est désormais explicitement bornée comme diagnostic asymétrique (une fuite détectée disqualifie, l'absence de détection ne prouve pas l'absence de mémorisation invariante au renommage).
8. **C(b)6 — Interaction $\Delta_F - \Delta_N > 0$ compatible avec $\Delta_F, \Delta_N < 0$.** **Acceptée.** E3 exige désormais la conjonction $\bar{\Delta}_F > \delta_0 > 0$ ET $\bar{\Delta}_F - \bar{\Delta}_N > \delta_{\text{int}}$.
9. **C(b)7 — Si $\mathbb{E}[D \mid R]$ croît, la fuite de $R$ n'implique pas la stagnation de $D$.** **Transformée en test.** En E4, le critère de fuite ne repose plus sur la baisse de $D_{\text{OOD}}$ mais sur le découplage d'étroitesse entre $\mathcal{Q}_0$ et $\mathcal{Q}'$ ainsi que sur l'inflation de $D_{\text{train}} - D_{\text{OOD}}$.
10. **C(b)8 — Conditionnement de E6 au passage de E5 sur les mêmes 120 problèmes (biais post-sélection).** **Acceptée.** E6 est exécutée sur un **lot d'instances entièrement indépendant** de E5.
11. **C(c) — Contrôles (viviers de tailles différentes à $D$ vrai égal ; A/A complet rejouant sélection et arrêt ; audit des idées écartées au préfiltrage en PPI).** **Acceptée** intégralement et intégrée en E1 et E2b.

### Critiques de D sur E

1. **D(a)1, D(b)3 & D(c)1 — Fuite du coffre dans $\max$, biais $\sqrt{2\ln L_m}$, queues lourdes de Pareto invalidant le bootstrap, contrôle d'inflation de portefeuille.** **Acceptée** (corrigée par nomination scellée $\hat{x}_1$, métrique binaire bornée et contrôle d'inflation en E1).
2. **D(a)2 — Défaite par construction de l'énumérateur sous double égalité budgétaire.** **Acceptée** (corrigée par E5a à USD égal sans plafond d'appels oracle).
3. **D(a)3 & D(c)2 — Contraste fallacieux en E3 sans exigence $\Delta_F > \delta_0 > 0$ ni régime neutre.** **Acceptée** (conjonction et régime neutre ajoutés en E3).
4. **D(a)4 — PPI audité par des experts humains ne borne pas un biais commun LLM–experts.** **Acceptée.** Le harnais restreint PPI aux domaines disposant d'un **oracle externe objectif** coûteux (expérience physique/simulateur lourd). Avec des experts humains, le statut est explicitement limité à l'accord avec des experts, sans prétendre borner le biais de vérité.
5. **D(b)1 — Non-identifiabilité Kaplan–Meier de $B_{0,5}$.** **Acceptée** ($B_{0,5}$ retiré).
6. **D(b)2 & D(c)3 — PPI dégrade la variance si $\rho_{Y,f} < \frac{\sigma_f}{2\sigma_Y}(1 + n/N_{\text{un}})$ ; sous-couverture si $np \ll 1$ ; contrôle d'anti-corrélation sémantique à style constant.** **Acceptée et transformée en test.** E2b inclut la strate de vérités contre-intuitives à style constant (empruntée à D) et disqualifie le juge dès que $\hat{\rho}_{Y,f} \le \frac{\hat{\sigma}_f}{2\hat{\sigma}_Y}(1 + n/N_{\text{un}})$ (ou si la variante pondérée de PPI, référence à vérifier, n'offre aucun gain) ou $n\hat{\pi} < 10$ (`illustratif`).
7. **D(b)4 — Seuils en $c\cdot\hat{\sigma}_\Delta$ falsifiés par le bruit ; pénalité $\lambda |x|$ rendant $D(X^*) < 0$ sous langage verbeux.** **Acceptée** pour les seuils en $\sigma$. **Rejetée comme défaut de principe** sur la pénalité descriptive, mais **transformée en contrôle de dimensionnement en E1** : sous le principe MDL exact (Rissanen, 1978, `RAPPORTÉ`), $\lambda = 1$ (en nats dans un code préfixe normalisé du DSL) n'est pas un hyperparamètre arbitraire ; une loi dont le coût descriptif excède le gain de log-vraisemblance OOD ne compresse tout simplement pas les observations OOD. Si $D_{\text{ext}}(X^*) \le 0$ pour une loi plantée, cela révèle un jeu OOD sous-informatif, vérifié en E1 avant toute campagne.

---

## (b) Expériences corrigées en inférence forte

### Définitions corrigées et règle de réfutation (`HYPOTHÈSE`)

- **Périmètre du harnais principal :** domaines à oracle mécanique sans juge LLM (mondes synthétiques procéduraux à vérité plantée, preuve formelle Lean 4, simulateurs exécutables isolés). Le juge LLM + PPI est confiné au module optionnel E2b.
- **Nomination scellée :** à l'expiration du budget $B$, chaque bras $m$ soumet une unique nomination canonisée $\hat{x}_1$ (ou s'abstient, score $0$) **avant** ouverture du coffre scellé. (Un diagnostic secondaire top-$k$ avec $k = 3$ `illustratif` identique pour tous les bras sépare erreur de recherche et erreur de nomination, sans entrer dans la règle de décision.)
- **Certification d'étroitesse $I_R$ :** un ensemble de références $\mathcal{Q}_0 = \{Q_{\text{rand}}, Q_{\text{enum}}, Q_{\text{LLM-ref}}\}$ opère sur des **tirages strictement disjoints** du duel, au budget court $b_{\text{ref}} = B/20$ (`illustratif`, évitant la borne de handicap de B sur le bras Best-of-$K$ au budget $B$). Sur $K_{\text{ref}}$ exécutions indépendantes par monde et par politique, $u_Q([\hat{x}_1])$ désigne la borne supérieure unilatérale de Clopper–Pearson (Clopper & Pearson, 1934, `RAPPORTÉ`) au niveau $1 - \alpha_{\text{ref}}/(|\mathcal{Q}_0|\cdot M_{\text{bras}})$ (pour $|\mathcal{Q}_0|=3$, $M_{\text{bras}}=5$, $\alpha_{\text{ref}}=0{,}01$, $\tau_p=0{,}01$ `illustratif`, $K_{\text{ref}} = 800$ `illustratif` assure la certification en zéro occurrence, `VÉRIFIÉ` : $1 - (0{,}01/15)^{1/800} \approx 0{,}0091 < 0{,}01$). On pose $I_R([\hat{x}_1]) = \mathbb{I}[\max_{Q \in \mathcal{Q}_0} u_Q([\hat{x}_1]) \le \tau_p]$. Un panel secret disjoint $\mathcal{Q}'$ est tenu à l'écart pour E4.
- **Profondeur $D_{\text{ext}}$ :** gain net en nats sur régimes OOD/interventionnels ($\lambda = 1$ nat, MDL), gain de résolution/compression sur batterie Lean 4 gelée indépendante, ou EIG minimax sur famille d'a priori pré-enregistrés pour protocoles ; seuil absolu pré-enregistré $\tau_D > 0$.
- **Quantité primaire binaire :** $Y_m(P, B) = \mathbb{I}[\text{Valide}(\hat{x}_1) \land I_R([\hat{x}_1]) = 1 \land D_{\text{ext}}(\hat{x}_1) \ge \tau_D] \in \{0,1\}$, de taux $\pi_m = \mathbb{E}_P[Y_m(P, B)]$.
- **Règle de réfutation exhaustive (empruntée à C, respectant B4) :** chaque expérience oppose deux hypothèses exclusives et exhaustives $H_A : \theta \in \Theta_A$ et $H_B : \theta \notin \Theta_A$ via un intervalle de confiance simultané au niveau $1 - \alpha$ ($\alpha = 0{,}025$ unilatéral, `illustratif`). Un intervalle entièrement dans $\Theta_A$ réfute $H_B$ ; entièrement hors de $\Theta_A$ réfute $H_A$ ; traversant la frontière laisse l'expérience **non concluante** (sans falsifier l'une ni l'autre).

### Protocole ordonné du moins cher au plus cher (tous seuils et $N$ `illustratif`)

1. **E1 — Métrologie du harnais : sensibilité/FPR par quadrant, canonisation, CN-2, spam et A/A complet**
   - **$H_A$** : (i) $\text{TPR}_{\text{target}} \ge 0{,}80$ sur vérités plantées (vérifiant aussi le dimensionnement OOD sous $\lambda=1$ nat) ; (ii) $\max_{c \in \{\text{rare-creux, banal-profond, banal-creux}\}} \text{FPR}_c \le \phi_{\max}$ avec $\phi_{\max} = 0{,}002$ (calibré par Bayes pour $\text{FDR} \le 0{,}20$ à prévalence $\pi = 0{,}01$) ; (iii) canoniseur : taux de fusion des paraphrases $\ge 0{,}95$ ET taux de fausses fusions sur paires proches distinctes $\le 0{,}01$ ; (iv) taux de succès $Y$ des attaques **CN-2 (chasseur d'étroitesse)** et **bras spam / inflation de volume** $\le \phi_{\max}$ ; (v) taux de rejet du **test A/A complet à graines distinctes** (rejouant sélection et arrêt) $\le 0{,}05$ ; (vi) contrôle « étroitesse par sélection » (runs disjoints vs conjoints) sans excès de rareté sur runs disjoints.
   - **$H_B$** : violation d'au moins un des critères (i)–(vi).
   - **Échelle :** $N_+ = 100$ positifs plantés + $N_- = 2\,000$ négatifs stratifiés par type de leurre (soit borne supérieure en zéro alerte $\approx 0{,}0018 < 0{,}002$, `VÉRIFIÉ`) + $200$ campagnes A/A légères.
   - **Porte d'arrêt :** si $H_A$ est réfutée (ou non concluante sur FPR/CN-2/spam), arrêt immédiat du programme avant tout appel au modèle 70B.

2. **E2a — Invariance au recodage isomorphe**
   - **$H_A$** : entre deux encodages isomorphes (incluant un isomorphisme ne préservant pas trivialement la taille syntaxique), le taux de désaccord de la certification finale $Y$ vérifie $d_{\text{rec}} \le 0{,}05$.
   - **$H_B$** : $d_{\text{rec}} > 0{,}05$ (cible instable au codage, donc mal posée).
   - **Contrôle négatif :** encodage non isomorphe cassant la structure causale (doit produire $d_{\text{rec}} \gg 0{,}05$).
   - **Échelle :** $N = 150$ problèmes appariés (synthétique + Lean 4). Arrêt si $H_A$ est réfutée.

3. **E2b (optionnel, domaines ouverts à oracle externe coûteux) — Qualification du juge LLM + PPI**
   - **$H_A$** : sur un audit stratifié par bras incluant les candidats écartés au préfiltrage, (i) $n\hat{\pi} \ge 10$ ; (ii) $\rho_{Y,f} > \frac{\sigma_f}{2\sigma_Y}(1 + n/N_{\text{un}})$ y compris sur la strate de **vérités contre-intuitives à style constant** (contrôle de D) ; (iii) décalage absolu sous *style-swap* $|\delta_{\text{style}}| \le 0{,}02$ en probabilité de verdict positif.
   - **$H_B$** : violation d'au moins un critère (i)–(iii).
   - **Contrôle négatif :** paires contenu identique / styles rhétoriques opposés ; faux plausibles vs vrais contre-intuitifs à style identique.
   - **Échelle :** $n = 1\,000$ candidats audités par oracle externe objectif + $400$ paires *style-swap*. Si $H_A$ est réfutée, le juge LLM est disqualifié (usage de l'oracle pur uniquement).

4. **E2c (optionnel, benchmarks historiques existants) — Diagnostic de contamination nette**
   - **$H_A$** : l'excès mémoriel net $\Delta_{\text{mém,net}} = \Delta_{\text{renommage}}(\text{benchmark}) - \Delta_{\text{renommage}}(\text{synthétique inédit apparié}) \le 0{,}03$.
   - **$H_B$** : $\Delta_{\text{mém,net}} > 0{,}03$ (contamination active disqualifiant le benchmark).
   - **Contrôle positif de sensibilité :** lot jumeau injecté en fine-tuning sur un modèle ouvert témoin (doit dépasser $0{,}03$). **Contrôle négatif :** problèmes synthétiques générés post-entraînement (doivent donner $\Delta_{\text{mém,net}} \approx 0$).
   - **Échelle :** $N = 120$ problèmes appariés. (Non requise si le harnais n'utilise que des mondes générés procéduralement post-entraînement.)

5. **E3 — Validation de la taxonomie de problèmes au niveau famille et transfert d'échelle**
   - **$H_A$** : sur $F = 16$ familles indépendantes pré-enregistrées (8 prédites fertiles, 8 prédites négatives/neutres non triviales : espaces permutés sans structure, bassins trompeurs ; descripteurs calculés sur propriétés *a priori* et un modèle/graine disjoint), la moyenne par famille satisfait conjointement $\bar{\Delta}_F > \delta_0 = 0{,}05$ ET $\bar{\Delta}_F - \bar{\Delta}_N > \delta_{\text{int}} = 0{,}05$, ET le signe de $\bar{\Delta}_F > 0$ se conserve au passage 8B $\to$ 70B sur 4 familles dédiées.
   - **$H_B$** : négation logique de $H_A$ (avantage non positif en zone fertile, pas d'interaction ou échec du transfert d'échelle).
   - **Contrôles négatifs :** (1) famille « espace permuté sans structure » ($\Delta \approx 0$) ; (2) contrôle séparé « petit combinatoire » où l'énumérateur doit battre le LLM sur $D_{\text{ext}}$ seul.
   - **Échelle :** $16$ familles $\times 40$ problèmes (8B) $+ 4$ familles $\times 40$ problèmes (70B). **Toutes les familles de E3 sont définitivement exclues de E5.**

6. **E4 — Étanchéité du feedback adaptatif contre Goodhart (double référence $\mathcal{Q}_0 / \mathcal{Q}'$)**
   - **$H_A$** : l'activation du feedback autorisé (validité + split interne) maintient l'inflation de surajustement $\Delta G = (D_{\text{train}} - D_{\text{OOD}})_{\text{fb}} - (D_{\text{train}} - D_{\text{OOD}})_{\text{sans}} \le \epsilon_G$ ET le découplage d'étroitesse sur le panel secret $\mathcal{Q}'$, $\Delta \delta_{Q,Q'} = \mathbb{P}(I_{R,\mathcal{Q}_0}=1 \land I_{R,\mathcal{Q}'}=0)_{\text{fb}} - \mathbb{P}(\cdot)_{\text{sans}} \le 0{,}02$.
   - **$H_B$** : violation de l'une des deux bornes (Goodharting avéré $\implies$ retrait du feedback interne).
   - **Contrôle positif de fuite :** bras recevant sciemment $I_{R,\mathcal{Q}_0}$ pendant la recherche (doit exhiber une hausse significative de $\delta_{Q,Q'}$).
   - **Échelle :** $N = 100$ problèmes dédiés (3 conditions appariées).

7. **E5 — Duel principal en deux régimes (E5a : USD égal ; E5b : appels oracle égaux) sur familles neuves**
   - **Baselines $\mathcal{B}$ :** Aléatoire, Énumérateur mécanique, Meilleur modèle unique Best-of-$K$, **CN-1 (divergence triviale : même modèle à température/prompt déplacé + second modèle mono-agent de force $\le$)**.
   - **$H_A$** (évaluée séparément pour E5a et E5b) : par test IUT, $\min_{b \in \mathcal{B}} (\pi_{\text{multi}} - \pi_b) > \delta_{\min} = 0{,}05$ sur chacune de 2 familles neuves indépendantes (issues de la règle gelée en E3, jamais vues auparavant), et résultat invariant au retrait d'une référence à la fois de $\mathcal{Q}_0$.
   - **$H_B$** : $\min_{b \in \mathcal{B}} (\pi_{\text{multi}} - \pi_b) \le 0{,}05$ sur au moins une famille neuve.
   - **Dimensionnement cohérent contre $\delta_{\min}$ (`VÉRIFIÉ` sous approximation normale appariée) :** pour $\pi_{\text{multi}} = 0{,}20$, $\pi_b = 0{,}05$ ($\Delta = 0{,}15$, écart effectif $\Delta - \delta_{\min} = 0{,}10$), discordance $q \approx 0{,}22$, $\alpha = 0{,}025$ unilatéral et puissance $0{,}80$, il faut $N \ge \frac{(1{,}96+0{,}84)^2 (0{,}22 - 0{,}15^2)}{0{,}10^2} \approx 155$ problèmes ; retenu **$N = 160$ problèmes/famille $\times 2$ familles = $320$ problèmes**. (Si $\Delta$ réel n'est que $0{,}10$, l'écart effectif chute à $0{,}05$ et exigerait $N \approx 620$/famille : l'analyse intermédiaire est conditionnée à $n_{\text{disc}} \ge 40$ paires discordantes avec frontière conservatrice.)
   - **Contrôle négatif de calibration :** lot « petit combinatoire » évalué sur $D_{\text{ext}}$ seul (l'énumérateur doit y dominer) et sur $Y$ (tous les bras à $0$).

8. **E6 — Attribution causale par ablations sur lot d'instances indépendant**
   - Exécutée uniquement si E5 réfute $H_B$, mais sur un **lot frais indépendant** de $N = 160$ problèmes par famille validée (éliminant le biais post-sélection signalé par C).
   - **Ablations $\mathcal{A}$ au même budget exact :** (1) ensemble hétérogène indépendant sans dialogue, (2) auto-raffinement séquentiel mono-agent, (3) **critique placebo neutre intra-problème** de même longueur (sans injection hors-sujet d'un autre problème).
   - **$H_A$** : par IUT, $\min_{a \in \mathcal{A}} (\pi_{\text{multi}} - \pi_a) > \delta_6 = 0{,}05$.
   - **$H_B$** : $\min_{a \in \mathcal{A}} (\pi_{\text{multi}} - \pi_a) \le 0{,}05$ (le gain de E5 ne provient pas du contenu critique).

### Ancrage matériel et budget révisé (entièrement `illustratif`)

Modèles ouverts recommandés (`RAPPORTÉ` quant à leur existence) : 7–8B (type Llama-3.1-8B-Instruct / Qwen2.5-7B-Instruct) pour E1–E4 et 70–72B (type Llama-3.1-70B-Instruct / Qwen2.5-72B-Instruct) pour E5–E6 + second 70B distinct pour l'ablation hétérogène. Tarifs cloud de référence (`illustratif`) : 2,50 USD/H100-h, 0,05 USD/vCPU-h.

| Phase | Contenu corrigé (incluant $K_{\text{ref}} = 800$ tirages courts) | Calcul estimé (`illustratif`) | Coût (`illustratif`) | Porte d'arrêt |
|---|---|---|---|---|
| **E1** | 100 positifs + 2 000 négatifs, CN-2, spam, A/A complet (8B + CPU) | 2 500 vCPU-h + 50 H100-h | ~250 USD | Échec FPR/CN-2/spam/A/A $\implies$ arrêt |
| **E2a** | 150 prob. isomorphes (incluant taille non conservée) + $K_{\text{ref}}$ | 1 500 vCPU-h + 70 H100-h | ~250 USD | $d_{\text{rec}} > 0{,}05 \implies$ cible mal posée |
| **E2b/c** | Optionnels : audit juge PPI (si requis) / contamination nette | 1 000 vCPU-h + 100 H100-h | ~300 USD | Disqualification juge ou rétrodiction |
| **E3** | 16 familles (8B) + 4 familles transfert (70B) + $K_{\text{ref}}$ | 10 000 vCPU-h + 360 H100-h | ~1 400 USD | Échec conjonction ou transfert $\implies$ arrêt |
| **E4** | 100 prob. $\times$ 3 conditions + panels $\mathcal{Q}_0, \mathcal{Q}'$ | 3 000 vCPU-h + 140 H100-h | ~500 USD | Goodhart avéré $\implies$ retrait feedback |
| **E5a/b** | 320 prob. neufs $\times$ 5 bras (dont CN-1) + $K_{\text{ref}}$ (70B + CPU à USD égal) | 50 000 vCPU-h + 2 200 H100-h | ~8 000 USD | Arrêt futilité si $n_{\text{disc}} \ge 40$ |
| **E6** | Lot **indépendant** de 320 prob. $\times$ 4 bras + $K_{\text{ref}}$ (conditionnel à E5) | 20 000 vCPU-h + 1 800 H100-h | ~5 500 USD | Non exécuté si E5 échoue |
| **Total** | **Campagne complète plafonnée** | **~88 000 vCPU-h + ~4 720 H100-h** | **~16 200 USD** (~2 700 USD avant E5) | **83 % du budget protégé par E1–E4** |

---

## (c) Réponse à la question de l'arbitre (en une page)

### Ce qui est établi

1. **Distinction conceptuelle et relativité de la mesure.** La rareté informationnelle ne mesure pas la profondeur ou la conséquence scientifique (`RAPPORTÉ` : Shannon, 1948 ; Bennett, 1988 ; Rissanen, 1978). La rareté dépend nécessairement du langage de codage (`RAPPORTÉ` : Solomonoff, 1964) et d'un chercheur de référence explicitement fixé ; l'absence d'universalité sans adéquation structurelle est établie (`RAPPORTÉ` : Wolpert & Macready, 1997).
2. **Pièges mathématiques qui invalident un harnais naïf (`VÉRIFIÉ`).**
   - Évaluer un maximum sur l'ensemble des idées générées $\mathcal{S}(P,B)$ avec l'oracle scellé court-circuite la sélection du système et gonfle artificiellement le score avec le volume de candidats. Le harnais doit noter une nomination scellée choisie avant ouverture du coffre.
   - À faible prévalence $\pi$ d'idées « étroites et profondes », l'identité de Bayes impose $\text{FPR} \ll \pi$ : un juge ou détecteur à $\text{FPR} = 0{,}05$ (`illustratif`) produit majoritairement de fausses découvertes lorsque $\pi = 0{,}01$ (`illustratif`).
   - Utiliser la même politique LLM à budget identique comme référence d'étroitesse et comme baseline du duel handicape mécaniquement cette baseline par construction (outil formalisé par B).
   - Comparer contre une enveloppe $\max_b$ prise problème par problème crée un biais négatif par inégalité de Jensen ; l'intersection-union (Berger, 1982, `RAPPORTÉ`) évite ce biais.
   - Dimensionner les échantillons contre zéro alors que la règle exige une marge $\delta_{\min} > 0$ sous-estime massivement la taille requise ; de même, réutiliser les familles de sélection ou les instances du duel dans les ablations crée un biais post-sélection.
3. **Limites établies des sources de vérité et du feedback.** Les vérificateurs formels garantissent zéro faux positif de validité logique modulo le noyau (`RAPPORTÉ`). La réutilisation adaptative d'une suite d'évaluation détruit la validité statistique (`RAPPORTÉ` : Dwork et al., 2015). Enfin, PPI (`RAPPORTÉ` : Angelopoulos et al., 2023) ne borne le biais que vers l'étiquette d'audit — pas vers la vérité scientifique si des experts partagent les biais du juge LLM — et dégrade la variance si la corrélation juge–vérité est insuffisante (`VÉRIFIÉ`).

### Ce qui n'est pas établi (`HYPOTHÈSE`)

1. **Existence empirique d'une cible stable.** Rien n'établit qu'une opérationnalisation de « narrow & deep » reste stable sous recodage isomorphe hors de langages formels ou synthétiques très contraints, ni que la prévalence réelle $\pi$ soit assez élevée pour permettre une décision statistique à coût fini.
2. **Faisabilité d'un harnais en science ouverte.** Aucun harnais automatisé existant n'établit la validité externe entre mondes synthétiques/formels (seuls auditables sans contamination ni biais de juge) et découverte empirique ouverte, qui repose souvent sur un changement d'ontologie inaccessible à tout vérificateur à grammaire figée.
3. **Avantage réel du multi-agents et attribution causale.** Il n'est établi ni qu'il existe des familles de problèmes identifiables *a priori* où des agents LLM battent simultanément un énumérateur mécanique (à coût financier égal), un modèle unique en Best-of-$K$ et un bras de divergence triviale (CN-1), ni qu'un gain éventuel résulte du débat critique plutôt que de la diversité ou du volume d'exploration.

### L'expérience à faire en premier (`HYPOTHÈSE`)

Lancer **E1 (métrologie du harnais sur vérités plantées, sans juge LLM, ~250 USD `illustratif`)**, suivie immédiatement de **E2a (invariance au recodage isomorphe, ~250 USD `illustratif`)**, avant tout développement coûteux du système multi-agents.

**Protocole minimal d'E1 :** construire deux bancs procéduraux post-entraînement (un synthétique exécutable à lois interventionnelles et un formel Lean 4), munis d'une nomination scellée unique $\hat{x}_1$ et d'une étroitesse certifiée par borne de Clopper–Pearson sur $K_{\text{ref}} = 800$ (`illustratif`) tirages courts disjoints. Soumettre le harnais à $100$ (`illustratif`) positifs plantés et $2\,000$ (`illustratif`) négatifs couvrant les trois classes leurres, les paraphrases et paires proches distinctes, un **chasseur d'étroitesse (CN-2)**, un **bras spam à volume élevé** et un **test A/A complet à graines distinctes**.

**Critère d'arrêt immédiat :** si le harnais échoue à maintenir $\text{FPR} \le 0{,}002$ (`illustratif`) contre chaque classe de leurres, CN-2 et le spam tout en conservant $\text{TPR} \ge 0{,}80$ (`illustratif`) — ou si E2a montre un désaccord $> 0{,}05$ (`illustratif`) sous recodage isomorphe —, arrêter le projet : la mesure est mal posée ou perméable à la rareté creuse, et tout duel ultérieur à grande échelle serait ininterprétable.

FIN-DE-CELLULE