# Cellule III.3 — Proposition C — Riposte

**État des pièces reçues.** Bloc FAITS vide par déclaration (GO-2026-10-26-01). La question de l'arbitre, ma conception (III.1) et les deux attaques de l'équipe rouge (A et B, III.2) sont présentes et complètes jusqu'à leur `FIN-DE-CELLULE`. Je ne réponds qu'aux sections visant C. Tout chiffre issu de `neuron-explorer` ou de l'énoncé reste **RAPPORTÉ** ; tout chiffre de dimensionnement que j'avance est **illustratif**, sauf calcul arithmétique explicite.

---

## (a) Traitement des attaques contre C (acceptée, rejetée, ou transformée en test)

### 1. Intégrité des statuts, droit et littérature
*   **C-1 (A) et C-F0 (B) — Statut des faits du programme, de l'architecture Llama-3.1-8B et de la méthodologie d'agent.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction stricte* : Aucune vérification d'empreinte ou d'exécution n'ayant lieu dans la cellule, tous les faits de l'énoncé (contraintes du programme, méthodologie de l'agent lue dans le dépôt) et les paramètres architecturaux de Llama-3.1-8B-Instruct ($L=32$, $d_{\text{model}}=4\,096$, $d_{\text{mlp}}=14\,336$) portent le statut **RAPPORTÉ** (à vérifier sur le fichier `config.json` de la révision épinglée). De même, le mécanisme reliant la direction de refus d'Arditi et al. (2024, à vérifier) aux trouvailles de `neuron-explorer`, ainsi que la proportion de neurones propres dans la littérature, sont explicitement reclassés en **HYPOTHÈSE**.
*   **C-15 (A) — Statut de la revendication juridique sur l'absence de licence.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : Le fait « Licence du dépôt : non trouvée » est **RAPPORTÉ**. L'interprétation juridique (« tous droits réservés par défaut ») est une règle prudentielle (**HYPOTHÈSE** juridique hors compétence du modèle), qui motive la décision d'ingénierie de réimplémenter les équations sans copier le code.

### 2. Expérience 1 (Lire contre écrire : poussée de sonde)
*   **C-7 (A) — Lecture circulaire si l'effet cible est lu par la sonde elle-même.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : Pousser $+\mathbf{w}_{\text{probe}}$ augmente mécaniquement $\mathbf{w}_{\text{probe}}^\top \mathbf{r}$. L'effet cible ne doit jamais être le score de la sonde, mais une mesure comportementale en aval dans les jetons générés (verbalisation explicite ou acte de sabotage exécuté dans la trace, évalué par l'analyseur syntaxique/fonctionnel de la tâche).
*   **C-8 (A) — La contrainte $\Delta_{\text{KL}}$ hors-domaine (WikiText) ne contraint pas la modalité M1 (poussée au dernier jeton de la transcription).**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : La dégradation de fluence doit être mesurée **à la position poussée et sur les textes poussés** (ainsi que sur des textes neutres poussés exactement selon la même modalité M1), en vérifiant que la masse de probabilité cumulée sur les jetons syntaxiquement valides (ou la divergence KL sur les jetons non liés à la cible) reste bornée, tant pour la sonde que pour chaque témoin.
*   **C-9 (A) et C-F5 (B) — Biais de sélection et déséquilibre spectral des témoins PCA-orthogonaux.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : Tirer uniformément dans les 128 premières composantes principales injecte trop d'énergie dans les dimensions à activations massives (ce qui casse les témoins et biaise les survivants), tandis qu'une sonde peu régularisée injecte de l'énergie hors variété. Dans l'Expérience 1 corrigée, les témoins sont des **rotations aléatoires préservant le spectre** : chaque témoin est construit en appliquant des rotations aléatoires orthogonales par blocs de variance homogène (dans la base PCA des activations de la banque d'entraînement) au vecteur $\mathbf{w}_{\text{probe}}$ lui-même. Ainsi, chaque témoin a *exactement* le même profil spectral et la même norme par bande de variance que la sonde testée, tout en étant orthogonal à celle-ci.
*   **C-10 (A), C-(c)5 (A) et C-(c)1/2 (B) — Lecture purement lexicale, absence de duel comportemental et confusion avec un simple indice de cadrage.**
    *   **Verdict : TRANSFORMÉE EN TEST (intégration au protocole d'Exp 1 corrigée).**
    *   *Action* : J'adopte explicitement (1) le format de question à choix forcé avec étiquettes **(A)/(B) inversées aléatoirement** et traduites en deux langues (proposé par B et A) pour éliminer le biais lexical du jeton « test » ; (2) la séparation en deux duels distincts (Exp 1A pour la verbalisation, Exp 1B pour le comportement de sabotage/performance) ; et (3) le contrôle négatif de B : la **direction de quasi-cible de cadrage** ($\mathbf{w}_{\text{quasi}}$, apprise pour séparer des textes avec le mot « test/évaluation » dans un contexte non-IA, ex. médical/scolaire, contre des textes sans ce champ lexical) et la **sonde à étiquettes permutées**.
*   **C-F4 (B) — Comparaisons multiples sur 24 conditions (6 doses $\times$ 2 modes $\times$ 2 types de sondes).**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : Pour éviter l'inflation du taux de fausses alertes ($1 - 0,99^{24} \approx 21\%$), on fixe **une seule condition primaire préenregistrée** : la sonde de différence des moyennes ($\mathbf{w}_{\text{MM}}$), poussée en modalité M1 (dernier jeton seul, conformément à l'étape 1), à une dose unique $\alpha^*$ calibrée *a priori* comme la dose maximale maintenant l'entropie/KL des témoins spectraux sous le seuil.
*   **C-F6 (B) — Puits d'attention à norme résiduelle massive en modalité M2.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : En modalité M2 (si explorée secondairement), on exclut toujours les 4 premiers jetons (puits d'attention BOS) et l'on normalise la poussée par la norme résiduelle *médiane* de la couche sur le contexte, jamais par la norme instantanée $\|\mathbf{r}_{l,t}\|_2$ d'un jeton aberrant.
*   **C-11 (A) — Plafond mécanique $|\alpha| \le 0,8$ importé de Qwen3.5-4B.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : La borne $\alpha_{\max}$ n'est plus figée à $0,8$ ; elle est définie fonctionnellement sur Llama-3.1-8B-Instruct par une étape d'étalonnage préalable (dose où la médiane des témoins spectraux atteint $\Delta_{\text{KL}} = 0,5\text{ nats}$, illustratif).

### 3. Expérience 2 (Balayage de neurones contre superposition)
*   **C-2 (A) et C-F1 (B) — Incompatibilité arithmétique entre le seuil de Bonferroni ($\alpha = 0,0002$) et le nombre de témoins ($N = 1\,000$, résolution minimale $1/1\,001 \approx 0,001$).**
    *   **Verdict : ACCEPTÉE (erreur arithmétique fatale corrigée).**
    *   *Correction* : Pour tester $K = 20$ candidats (illustratif) en Phase 2 au seuil global FWER de $0,05$ (soit $\alpha_{\text{indiv}} = 0,05 / 20 = 0,0025$), une p-valeur empirique pure sans hypothèse paramétrique exige au moins $N = 4\,000$ témoins pour que le rang 1 franchisse le seuil (nous fixons $N = 10\,000$ témoins en Phase 2 sur les 20 candidats, ou un pré-filtrage réduisant $K=10$ avec $N = 4\,000$ témoins : ainsi, les 10 meilleurs rangs $1/4\,001 \dots 10/4\,001$ permettent une estimation robuste).
*   **C-3 (A) et C-F2 (B) — Non-exclusivité des issues (confusion suffisance/nécessité) et ablation en aval de la sonde.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : La question de l'arbitre porte sur l'existence de « leviers » par la poussée (suffisance causale en écriture). J'élimine la branche d'ablation sur l'AUROC de la sonde dans le critère de falsification de l'Expérience 2 pour rétablir une inférence forte stricte (B4) centrée sur la poussée, et toute mesure d'ablation complémentaire se fait directement sur la sortie comportementale du modèle, jamais sur une sonde située en amont.
*   **C-4 (A) — Absence de témoins appariés en géométrie pour les neurones ($W_{\text{down}}$).**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : Comme je l'avais posé en S5 sans l'appliquer en Exp 2, un témoin isotrope sur la sphère ne respecte pas l'anisotropie de $W_{\text{down}}^{(l)}$. Dans l'Expérience 2 corrigée, les témoins d'une couche $l$ sont des **vecteurs aléatoires tirés selon la matrice de covariance empirique des colonnes de $W_{\text{down}}^{(l)}$** (c'est-à-dire $\mathbf{v}_{\text{nul}} = W_{\text{down}}^{(l)} \mathbf{z} / \|W_{\text{down}}^{(l)} \mathbf{z}\|_2$ avec $\mathbf{z} \sim \mathcal{N}(0, I)$, ou des colonnes permutées/signées aléatoirement d'autres couches projetées dans le même sous-espace), normalisés à la même norme résiduelle.
*   **C-5 (A) et C-F3 (B) — Contradiction avec S3 (criblage sur amorces courtes vs confirmation sur tâches longues) et saturation lexicale du score $S_i$.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : La Phase 1 (criblage par passe avant unique) s'exécute directement sur des **transcriptions complètes de la banque de conception** (avec partage de préfixe KV-cache, puisque la poussée n'a lieu qu'au dernier jeton : on ne recalcule que le dernier jeton couche par couche, ce qui rend le coût sur longue transcription identique au coût sur amorce courte !). De plus, la cible n'est plus le champ lexical « test », mais le **déplacement de la log-cote (log-odds) de la réponse A/B** à la question de verbalisation ou d'action, ce qui résout simultanément C-F3 (normalisation par la log-cote de base).
*   **C-6 (A), C-(c)2 (A) et C-F8 (B) — Rappel de la lentille rapide inconnaissable si le balayage génératif est interdit, et surcomplétude de la projection $W_{\text{down}}^\top \mathbf{w}_{\text{probe}}$.**
    *   **Verdict : TRANSFORMÉE EN TEST (pour la lentille) et ACCEPTÉE (pour la surcomplétude).**
    *   *Action 1 (Test du rappel de la lentille — C-(c)2)* : Avant d'écarter le balayage génératif multi-jetons, on tire un échantillon aléatoire stratifié de $M = 200$ neurones (illustratif) qui ont **échoué** au criblage par passe avant ($\Delta \text{log-odds}$ nul au premier jeton) et on les soumet à une génération longue de 32 jetons sous poussée.
        *   **H_A (Exhaustivité de la passe avant)** : Moins de 2 % (illustratif) des neurones muets au premier jeton produisent un effet cible significatif aux jetons $2 \dots 32$.
        *   **H_B (Effet retardé)** : Plus de 2 % produisent un effet retardé, falsifiant la suffisance de la lentille en une passe.
    *   *Action 2 (Attribution causale au lieu de produit matriciel nu)* : Pour mesurer la parcimonie d'une sonde sur les neurones d'une couche $l' < l$, on remplace le produit géométrique $\|W_{\text{down}}^{(l')\top} \mathbf{w}_{\text{probe}}\|$ par l'**attribution directe activée** : $c_i = \mathbb{E}_{x \in \text{Cibles}}[a_i^{(l')}(x)] - \mathbb{E}_{x \in \text{Contrôles}}[a_i^{(l')}(x)]$ multiplié par la projection de $W_{\text{down}}[:, i]$ sur la sonde (un neurone inactif a une contribution nulle).

### 4. Expérience 3 (Primitive « pousser » dans les organismes)
*   **C-12 (A), C-(b) (A) et C-F7 / C-(b) (B) — Vecteur arbitraire optimisable par l'organisme, magasinage de graine par modification d'un caractère du texte $T$, recherche adaptative sur les 64 témoins fixes grâce au score $z$, non-exclusivité coût/gain, et absence de test A/A de variance.**
    *   **Verdict : ACCEPTÉE SUR TOUTE LA LIGNE.** Les scénarios d'évasion d'Adv-O construits par A et B sont redoutables et réfutent mon architecture de primitive de III.1.
    *   *Corrections architecturales ( reprises de A et B en le disant)* :
        1.  **Interdiction des vecteurs arbitraires** (repris de A/B) : L'organisme ne peut appeler `pousser` que sur un identifiant de **neurone canonique $(l, i)$** ou sur une **sonde préalablement enregistrée** à partir d'un classifieur entraîné sur un jeu déclaré. Aucune recherche par différences finies dans $\mathbb{R}^{4096}$ n'est possible.
        2.  **Fermeture du magasinage de graine et de l'optimisation adaptative** (repris de B) : Les témoins ne dépendent plus du hachage du texte $T$, ne sont plus réutilisés avec retour de score $z$ continu, et le budget est décompté en **appels totaux**. À chaque appel, des témoins frais sont tirés par le noyau ; l'organisme ne reçoit qu'un **verdict binaire** (franchissement ou non du 99e centile des témoins sous contrainte KL) et le texte/log-prob de sa propre direction.
        3.  **Bras Placebo / Budget taxé et Test A/A** (repris de A-B9 et B-c6) : Intégrés à l'Expérience 3 corrigée ci-dessous.

### 5. Expérience 4 (Méthodologie d'agent et Maximum à l'aveugle)
*   **C-13 (A) et C-F7 (B) — Signature d'activation gaussienne des directions aléatoires (leurres reconnaissables), régression vers la moyenne des faux positifs du criblage, et circularité des « vraies directions ».
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : Un vrai neurone MLP SwiGLU a une distribution d'activation parcimonieuse et asymétrique ; une direction aléatoire a une distribution gaussienne dense. Dans l'Expérience 4 corrigée, **tous les vecteurs du test en aveugle sont de vrais neurones MLP** de Llama-3.1-8B-Instruct, mais dans le groupe « Leurres », on fournit à l'agent de validation des **paires (neurone, explication) permutées** à l'intérieur d'un même cluster de fréquence d'activation (repris de A-B10 et B-c6), ou de vrais neurones purement syntaxiques/lexicaux.
*   **C-14 (A) et C-(b) (B) — Contournement du tabou lexical par synonymes/syntaxe ou impossibilité de décrire le concept.**
    *   **Verdict : ACCEPTÉE.**
    *   *Correction* : J'abandonne le filtre de tabou lexical au profit exclusif du protocole de **paires minimales à l'aveugle ($T_{\text{max}}, T_{\text{min}}$)** à recouvrement lexical forcé ($\ge 80\%$ de lemmes communs, incluant obligatoirement les mêmes mots-clés du domaine dans les deux textes), complété par une **contrainte de gabarit syntaxique fixe** pour l'explication de l'Agent 1 (afin d'empêcher la stéganographie syntaxique soulevée par A).

---

## (b) Les expériences corrigées (Inférence forte B4)

### Expérience 1 Corrigée : Validité causale des sondes de l'étape 1 (Verbalisation et Comportement)
*   **Précondition mécanique (Contrôle 0, repris de B)** : On vérifie d'abord sur une banque de poussée **strictement disjointe** de la banque d'entraînement de la sonde (correction A-B2) que la sonde $\mathbf{w}_{\text{MM}}$ (différence des moyennes au dernier jeton) sépare les tâches en lecture seule AU-DESSUS d'une sonde de surface, et qu'il existe un écart comportemental mesurable entre tâches cadrées « évaluation » et « déploiement ».
*   **Vecteurs testés et Contrôles négatifs** :
    1.  $\mathbf{w}_{\text{MM}}$ : Direction de la sonde de conscience d'évaluation (ou d'honnêteté), orthogonalisée par projection de Gram-Schmidt contre la direction de quasi-cible $\mathbf{w}_{\text{quasi}}$ (correction B-AF2).
    2.  *Contrôle de cadrage non-évaluatif ($\mathbf{w}_{\text{quasi}}$)* : Direction apprise sur des paires contenant le vocabulaire de l'évaluation (« test », « examen », « benchmark ») mais portant sur un objet tiers (test logiciel, examen médical) où le modèle n'est pas évalué.
    3.  *Témoins spectraux ($N = 1\,000$)* : Directions générées par rotation aléatoire de $\mathbf{w}_{\text{MM}}$ à l'intérieur de sous-espaces de variance empirique égale (préservant exactement le spectre de puissance de la sonde dans la base PCA des activations, mais orthogonales à $\mathbf{w}_{\text{MM}}$).
    4.  *Témoins d'étiquettes permutées ($N = 1\,000$)* : Directions $\mathbf{w}_{\text{perm}}$ entraînées sur la banque d'entraînement avec étiquettes mélangées aléatoirement.
*   **Condition primaire unique (Anti-p-hacking)** : Poussée au dernier jeton de l'amorce (M1) à la dose unique $\alpha^*$ (définie sur un jeu d'étalonnage séparé comme la dose maximale où 95 % des témoins spectraux gardent une divergence $\Delta_{\text{KL}} < 0,5\text{ nats}$ sur la distribution du jeton suivant hors jetons cibles). Tout vecteur (sonde ou témoin) qui dépasse $\Delta_{\text{KL}} = 0,5\text{ nats}$ sur les tâches testées est marqué « bris syntaxique » et son effet cible est mis à zéro (correction A-C8/C9).
*   **Duel 1A (Écriture sur la verbalisation) vs Duel 1B (Écriture sur la décision/comportement)** :
    *   *Mesure 1A* : Déplacement de la log-cote $\Delta \text{log-odds}(A/B)$ en réponse à une question d'auto-évaluation dont les étiquettes (A) et (B) sont inversées aléatoirement sur chaque paire et posées en deux langues (français/anglais).
    *   *Mesure 1B* : Variation du taux d'exécution du comportement dépendant de l'évaluation (ou variation du taux de sabotage fonctionnel dans la suite de la trace d'agent générée).
    *   **H_A (Biomarqueur passif ou artefact de cadrage)** : Sur la mesure 1B (comportement) [respectivement 1A], l'effet symétrisé $E(\mathbf{w}_{\text{MM}}) = \frac{1}{2}[\Delta(+\alpha^*) - \Delta(-\alpha^*)]$ ne dépasse pas le 99,5e centile des $1\,000$ témoins spectraux ET des $1\,000$ sondes permutées ($p \ge 0,005$), OU ne dépasse pas significativement l'effet de la direction quasi-cible $E(\mathbf{w}_{\text{quasi}})$.
    *   **H_B (Levier causal spécifique de la situation)** : $E(\mathbf{w}_{\text{MM}}) > Q_{0,995}(\text{témoins spectraux et permutés})$ ET $E(\mathbf{w}_{\text{MM}}) > E(\mathbf{w}_{\text{quasi}}) + 2\sigma_{\text{boot}}$ (par rééchantillonnage des tâches).
    *   *Ce que chaque issue falsifie* : Si 1A valide H_B mais 1B valide H_A, cela falsifie l'idée que la sonde gouverne la décision : elle ne gouverne que le rapport verbal (scénario d'évasion du modèle surveillé identifié par A et B).

### Expérience 2 Corrigée : Existence de neurones « leviers » contre Superposition (avec audit de la lentille)
*   **Étape 0 (Audit de la lentille rapide sur le cache KV — Réponse à C-6 / B-CF8)** :
    *   Sur 100 longues transcriptions de la banque de conception, on pré-calcule et fige le cache KV jusqu'à l'avant-dernier jeton. Pousser les $14\,336$ neurones d'une couche au *dernier jeton* en une passe avant ne nécessite de calculer que **1 seul jeton** pour les couches restantes (coût divisé par $2\,000$ par rapport à un recalcul complet !).
    *   On mesure pour chaque neurone $(l, i)$ le score différentiel normalisé sur la log-cote A/B : $S_i = \Delta \text{log-odds}_{\text{Cibles}}(A/B) - \Delta \text{log-odds}_{\text{Quasi-cibles}}(A/B)$.
    *   *Test du rappel de la lentille* : On tire au sort 200 neurones ayant $|S_i|$ dans la médiane basse (muets au 1er jeton) et on génère 32 jetons sous poussée. Si $>2\%$ (illustratif) modifient le comportement en génération longue (**H_B de l'audit**), la lentille en 1 passe est falsifiée comme filtre exhaustif ; sinon (**H_A de l'audit**), elle est validée.
*   **Phase 1 (Sélection)** : Sur 8 couches réparties (illustratif), on retient les $K = 10$ neurones ayant le plus fort $|S_i|$ en passe avant. Leurs indices $(l, i)$ et signes sont scellés dans un fichier empreinté.
*   **Phase 2 (Confirmation préenregistrée sur banque scellée)** :
    *   *Témoins géométriquement appariés ($N = 4\,000$ par couche représentée)* : Vecteurs tirés selon la covariance des colonnes $W_{\text{down}}^{(l)}$ de la même couche ($\mathbf{v}_{\text{nul}} = W_{\text{down}}^{(l)} \mathbf{z} / \|W_{\text{down}}^{(l)} \mathbf{z}\|_2$, $\mathbf{z} \sim \mathcal{N}(0,I)$), poussés à la même norme résiduelle que le neurone candidat sur la banque scellée.
    *   **H_A (Superposition diffuse — Absence de levier unique)** : Aucun des 10 neurones préenregistrés n'atteint un score $S_i$ sur la banque scellée supérieur au 99,75e centile des $4\,000$ témoins géométriques de sa couche (seuil de Bonferroni $\alpha = 0,025 / 10 = 0,0025$, soit les 10 premiers rangs sur $4\,000$, arithmétiquement résoluble).
    *   **H_B (Existence de leviers neuronaux)** : Au moins un neurone franchit le rang $3\,990 / 4\,000$ ($p \le 0,0025$) sur le score spécifique $S_i$ (Cibles moins Quasi-cibles) dans la banque scellée.

### Expérience 3 Corrigée : Utilité causale de la primitive « pousser » face à la taxe des témoins
*   **Étalonnage préalable (Test A/A)** : On exécute $2 \times 8$ courses d'organismes (illustratif) en lecture seule pour mesurer l'écart-type inter-courses $\sigma_{\text{AUROC}}$ sur la banque de confirmation scellée.
*   **Protocole à 3 bras (Budget de FLOPs total strictement identique)** :
    1.  *Bras 1 (Traitement — Poussée vraie)* : L'organisme peut appeler `pousser(id_direction_enregistree, dose, texte_organisme)`. Le noyau tire à neuf $k=32$ témoins spectraux secrets (indépendants du hachage du texte), consomme $(k+1)$ unités de budget, et ne renvoie qu'un booléen `passe_seuil_99_sans_bris_KL` ainsi que la variation de log-prob des 10 premiers jetons.
    2.  *Bras 2 (Contrôle Placebo — Taxe identique, information causale nulle, repris de A/B)* : Même coût de $(k+1)$ unités par appel, mais le noyau remplace la direction demandée par un témoin spectral fixe (déterministe par couple `(id_direction, texte)` pour déjouer le test de cohérence d'Adv-O signalé par B).
    3.  *Bras 3 (Contrôle Lecture seule non taxée)* : Pas de primitive `pousser` ; tout le budget de FLOPs est alloué à la lecture d'activations et de sondes.
*   **Hypothèses exclusives (sur le score AUROC de la banque scellée uniquement)** :
    *   **H_A (Nullité épistémique ou écrasement par la taxe)** : $\text{AUROC}(\text{Bras 1}) \le \max(\text{AUROC}(\text{Bras 2}), \text{AUROC}(\text{Bras 3})) + 2\sigma_{\text{AUROC}} / \sqrt{N_{\text{courses}}}$. (Si Bras 3 > Bras 1 $\approx$ Bras 2, la taxe $(k+1)$ détruit la valeur ; si Bras 1 $\approx$ Bras 2, l'effet n'était pas causal).
    *   **H_B (Gain causal net de la poussée)** : $\text{AUROC}(\text{Bras 1})$ surpasse **à la fois** le Bras 2 (prouvant l'utilité de la vraie direction poussée) ET le Bras 3 (prouvant que ce gain compense le coût des $k$ témoins) d'au moins $2\sigma_{\text{AUROC}} / \sqrt{N_{\text{courses}}}$.

### Expérience 4 Corrigée : Audit en aveugle de la boucle d'agent sur vrais neurones permutés
*   **Protocole sans directions gaussiennes artificielles** :
    *   On sélectionne 40 **vrais neurones MLP** de Llama-3.1-8B-Instruct ayant des distributions d'activation (parcimonie, norme queue lourde) jumelées par paires.
    *   L'Agent 1 génère pour chacun une hypothèse structurée selon un formulaire rigide à champs fermés (anti-stéganographie syntaxique) et exécute son test « casser l'hypothèse exprès ».
    *   Pour l'étape du **Maximum à l'aveugle**, on forme 20 paires exactes `(Neurone_i, Explication_i)` et 20 paires **croisées/permutées** `(Neurone_i, Explication_j)` où $i$ et $j$ ont la même fréquence d'activation mais des fonctions différentes (contrôle de A et B).
    *   L'Agent 2 (aveugle) ne voit que l'explication et doit produire 5 couples de textes minimaux $(T_{\text{max}}, T_{\text{min}})$ partageant $\ge 80\%$ de leurs mots (dont tous les termes cibles). Une paire est validée si $\text{Act}(T_{\text{max}}) - \text{Act}(T_{\text{min}})$ franchit le 99e centile de paires de textes aléatoires sur les 5 essais.
*   **Hypothèses exclusives** :
    *   **H_A (Confabulation et complaisance)** : Le taux de validation des paires permutées `(Neurone_i, Explication_j)` dépasse 10 % (illustratif), OU le gain de précision de la boucle d'agent par rapport à une simple sélection mécanique par différence d'activation moyenne sur paires fixes est $\le 0$.
    *   **H_B (Validité discriminante)** : Taux de fausses alertes sur paires permutées $\le 5\%$ ET taux de validation sur paires appariées d'au moins $3\times$ supérieur aux paires permutées (illustratif).

---

## (c) Réponse à la question de l'arbitre (Synthèse en une page)

### 1. Ce qui est établi
1.  **Contraintes du programme et limites des lectures seules (RAPPORTÉ)** : Le programme évalue deux menaces diffuses (conscience d'évaluation, contrôle de délégation) sur Llama-3.1-8B-Instruct (32 couches, 14 336 neurones MLP/couche, révision épinglée) par des sondes linéaires au dernier jeton. Mathématiquement, une sonde qui sépare deux classes en *lecture* peut ne capter qu'un corrélat passif en aval ou un artefact lexical de cadrage, sans pouvoir causal d'*écriture* sur la décision du modèle.
2.  **Apport méthodologique réel de `neuron-explorer` (RAPPORTÉ)** : Son apport majeur n'est pas l'interface d'exploration, mais la démonstration empirique que **sans témoins aléatoires de même norme, la poussée d'activations produit des illusions (« neurones de persona ») partout**, et qu'au-delà d'une certaine dose ($\approx 0,8\times$ la norme résiduelle sur Qwen3.5-4B), le texte casse quelle que soit la direction.
3.  **Arithmétique des coûts et des seuils (CALCUL EXPLICITE sur chiffres RAPPORTÉ)** :
    *   *Coût brut* : Llama-3.1-8B-Instruct compte $1,56\times$ plus de neurones par couche et $2\times$ plus de paramètres que Qwen3.5-4B (facteur $\approx 3,1\times$). Un balayage génératif complet des 32 couches coûterait de l'ordre de 125 à 1 000 USD (illustratif selon la longueur des contextes).
    *   *Optimisation par cache KV* : Puisque le programme travaille au **dernier jeton**, pré-calculer le cache KV des longues transcriptions permet de cribler les $14\,336$ neurones d'une couche en **une seule passe avant d'un seul jeton** ($\Delta \text{log-odds}$). Le coût d'un balayage des 32 couches tombe alors sous les 10 USD (illustratif).
    *   *Piège statistique des témoins* : Avec 256 témoins (standard de `neuron-explorer`), la plus petite p-valeur empirique résoluble est $1/257 \approx 0,0039$. C'est mathématiquement insuffisant pour corriger les tests multiples sur $14\,336$ neurones par couche : **un criblage en Phase 1 doit obligatoirement être suivi d'une Phase 2 préenregistrée sur une dizaine de candidats avec $\ge 4\,000$ témoins**.

### 2. Ce qui n'est pas établi (et les pièges mortels à éviter)
1.  **Existence de leviers neuronaux uniques pour la conscience d'évaluation (HYPOTHÈSE)** : Contrairement au refus (« I cannot » vs « Sure ») qui se comprime souvent sur une direction de rang 1 en fin de réseau, rien n'établit que la conscience d'évaluation ou le sabotage soient localisés sur des neurones individuels plutôt que distribués en superposition.
2.  **Piège 1 — L'effet d'indice par construction** : Si une sonde de l'étape 1 est entraînée sur des paires avec/sans cadrage explicite (« Tu es évalué »), pousser sa direction revient à injecter la représentation lexicale de l'indice. Elle fera dire au modèle « ceci est un test » même si elle ne contrôle aucun comportement de sabotage ou de sous-performance. **Parade obligatoire** : Décorréler lecture verbale (avec étiquettes A/B inversées aléatoirement) et comportement d'agent, et tester contre une **direction quasi-cible** (texte parlant d'évaluation scolaire/médicale sans que l'IA soit évaluée).
3.  **Piège 2 — L'anisotropie géométrique des témoins** : Comparer une sonde (ou une colonne de poids $W_{\text{down}}$) à des vecteurs aléatoires isotropes dans $\mathbb{R}^{4096}$ est biaisé. Les témoins d'une sonde doivent partager son **spectre de variance** dans les activations ; les témoins d'un neurone doivent être tirés selon la **covariance de $W_{\text{down}}$**.
4.  **Piège 3 — Détournement de la primitive `pousser` par les organismes** : Donner une primitive de poussée libre à la boucle intérieure permet à l'organisme (a) d'optimiser un vecteur arbitraire par différences finies, (b) de faire du « magasinage de graine » en modifiant une virgule de son texte pour obtenir des témoins cléments, ou (c) de sur-apprendre des témoins fixes si on lui renvoie un score $z$. **Parade obligatoire** : N'autoriser la poussée que sur des sondes/neurones enregistrés, tirer des témoins frais à chaque appel, ne retourner qu'un verdict binaire au seuil, et vérifier en 3 bras (Vrai vs Placebo taxé vs Lecture seule) que la taxe des $(k+1)$ inférences n'écrase pas le gain.
5.  **Hygiène logicielle** : En l'absence de licence trouvée sur `neuron-explorer`, ne copier aucun code ; réimplémenter uniquement les opérations matricielles dans le noyau isolé.

### 3. L'expérience à faire en premier (Immédiate, $< 5\text{ USD}$ illustratif)
**Lancer l'Expérience 1 Corrigée (Poussée des sondes de l'étape 1 au dernier jeton sur banque disjointe)** :
1.  Prendre la sonde de différence des moyennes ($\mathbf{w}_{\text{MM}}$) de conscience d'évaluation à l'étape 1, orthogonalisée contre la direction quasi-cible ($\mathbf{w}_{\text{quasi}}$, examens non-IA).
2.  La pousser au dernier jeton ($\pm \alpha^*$ sous contrainte de fluence locale $\Delta_{\text{KL}} < 0,5\text{ nats}$) face à $1\,000$ témoins spectraux et $1\,000$ sondes à étiquettes permutées.
3.  Mesurer séparément l'effet sur la **verbalisation (A/B aléatoire)** et sur le **comportement de la trace**.
*   *Pourquoi en premier* : Elle ne requiert aucun balayage de neurones, utilise directement les livrables de l'étape 1, et tranche immédiatement si nos sondes actuelles sont de simples thermomètres passifs (ou des détecteurs de mots-clés) ou de véritables leviers causaux.

FIN-DE-CELLULE