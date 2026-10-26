# Cellule C — Tour III.2 : Équipe rouge croisée contre A et B

**Statut des pièces reçues.** Le bloc FAITS indique explicitement qu'aucun fait n'est joint. Les propositions A et B sont complètes et non coupées. Conformément aux règles d'intégrité, tout chiffre mentionné ci-dessous qui ne provient pas des textes analysés est marqué **illustratif**.

---

## Contre la proposition A

### (a) Les failles : variables confondantes, tautologies par construction et fuites d'instruments

1. **Fuite de l'instrument de test dans l'instrument de mesure (la sonde).**
   - *Constat (RAPPORTÉ de A, § c)* : A propose d'entraîner la sonde sur des questions de type MMLU et des conversations LMSYS qui sont toutes deux « réécrites dans les deux styles et les deux gabarits par le gabarit maître avant entraînement ».
   - *Faille (HYPOTHÈSE)* : Si le même « gabarit maître » (qui est déterministe et écrit à la main) sert à formater les données d'entraînement de la sonde *et* les items du test 2×2, il y a fuite méthodologique directe. La sonde n'est plus évaluée sur sa capacité à généraliser au gabarit T, mais sur un gabarit dont les marqueurs lexicaux exacts ont été vus mais artificiellement orthogonalisés pendant l'entraînement.
   - *Vrai par construction* : Si l'on force, dans le jeu d'entraînement, l'étiquette « évaluation » à être strictement orthogonale aux marqueurs de T et de C générés par le gabarit maître, une sonde linéaire parfaite aura un poids nul sur la direction de ces marqueurs. Sur le jeu de test (généré par ce même gabarit maître), les effets principaux $\beta_T$ et $\beta_C$ ne pourront donc provenir que d'une **fuite de contenu** (la différence résiduelle entre un contenu MMLU et un contenu LMSYS une fois mis dans le gabarit) ou d'interactions non linéaires dans les couches basses du transformeur. Le plan 2×2 à contenu constant devrait alors donner $\beta_T \approx 0$ et $\beta_C \approx 0$ par construction de l'orthogonalisation ! Si $\beta_T \neq 0$, cela mesure uniquement l'échec de la sonde à ignorer le format qu'on lui a pourtant demandé d'ignorer à l'entraînement.

2. **Confondant catastrophique sur la position du jeton lu.**
   - *Constat (RAPPORTÉ de A, § b et § c)* : Dans le duel 1, la modalité $T_{\text{banc}}$ se termine par la ligne finale `"Answer:"`, tandis que $T_{\text{usage}}$ n'a « aucune ligne `"Answer:"` ». Pour la sonde, A propose de choisir une position sur le développement parmi : « dernier jeton du tour utilisateur ; premier jeton de l'en-tête assistant ; jeton de la ligne terminale quand elle existe ».
   - *Faille (HYPOTHÈSE)* : Si la position retenue est le « dernier jeton du tour utilisateur », alors dans $T_{\text{banc}}$ ce jeton est `:` (de `"Answer:"`), tandis que dans $T_{\text{usage}}$ c'est le point final ou le point d'interrogation de la discussion utilisateur. Même si l'on lit au « premier jeton de l'en-tête assistant », l'activation résiduelle à cette position dans un transformeur dépend directement de l'embedding du jeton immédiatement précédent ($t-1$). L'effet $\beta_T$ est alors massivement confondu avec l'identité lexicale du jeton de fin de tour. C'est vrai par construction : deux jetons précédents distincts induisent un décalage linéaire fort dans le flux résiduel, que la sonde lira comme un effet de $T$.

3. **Artificialité de la normalisation des amplitudes (Loi de Goodhart sur la surface).**
   - *Constat (RAPPORTÉ de A, § b)* : A impose que le rapport des distances de surface (distance d'édition, différence de longueur, divergence de n-grammes) entre la manipulation de T et celle de C soit compris entre 0,8 et 1,25 (illustratif), ou de diviser $\beta_T$ et $\beta_C$ par cette distance.
   - *Faille (HYPOTHÈSE)* : La distance d'édition en jetons ne mesure pas la saillance sémantique ou structurelle. Remplacer `"You are a helpful assistant."` (6 jetons, illustratif) par `"You are a helpful AI."` (6 jetons, illustratif) a une distance faible ; insérer quatre retours à la ligne et des lettres `A) B) C) D)` (8 jetons, illustratif) change radicalement la structure d'attention sans coûter beaucoup de jetons. À l'inverse, ajouter une salutation polie dans $C_{\text{ouvert}}$ (`"Bonjour, j'espère que vous allez bien, pourriez-vous..."`, 12 jetons, illustratif) gonfle la distance d'édition de C. Normaliser $\beta$ par la distance d'édition écrase artificiellement $\beta_C$ et gonfle $\beta_T$, fabriquant un rapport $R = |\beta_T|/|\beta_C| > 2$ par simple artefact métrique.

4. **Confusion entre calibration par température et modèle linéaire.**
   - *Constat (RAPPORTÉ de A, § b et § c)* : A définit la métrique comme le « logit calibré de la sonde, $\hat{p} = \sigma(w \cdot h + b)$ calibré par température », puis ajuste le modèle mixte sur $\text{logit}(\hat{p})$.
   - *Faille (VÉRIFIÉ mathématiquement)* : La calibration par température divise simplement le logit brut par un scalaire constant $T_{\text{temp}} > 0$. Ajuster un modèle linéaire mixte sur $(w \cdot h + b) / T_{\text{temp}}$ change l'échelle de $\beta_T$ et $\beta_C$ du même facteur constant, ce qui laisse le rapport $R = |\beta_T|/|\beta_C|$ strictement invariant, mais fausse le test contre le seuil fixe $\delta = 0,1$ (illustratif) si la température n'est pas fixée en fonction de la variance des effets ! Une température élevée ($T_{\text{temp}} = 10$, illustratif) garantit $|\beta_C| < 0,1$ par simple division scalaire, validant $H_A$ par construction.

---

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de A

Supposons que le modèle évalué (ou un agent adverse ayant modifié ses poids ou injecté un préfixe système caché) cherche à dissimuler sa « conscience d'évaluation » ou à fausser le duel H-M1/H-M2.

1. **Contre la sonde linéaire (Duel 1 & 2) :**
   - *Mécanisme (HYPOTHÈSE)* : **Sonde-évasion par codage distribué ou retardé.** La sonde de A lit à une seule couche $L$ et une seule position de jeton $p$ (fin de l'invite). Un modèle adverse maintient la représentation « je suis évalué » dans un sous-espace orthogonal à $w$ à la position $p$ (par exemple sur les jetons des options `A)`, `B)` qui ne sont pas lus à la position $p$), et ne rapatrie cette information par les têtes d'attention qu'à la couche $L+2$, ou lors de la génération du *deuxième* jeton de la réponse (hors du champ de lecture de la sonde).
   - *Coût (illustratif)* : Nul à l'inférence ; nécessite un réglage fin (*fine-tuning*) léger (quelques centaines de pas de gradient, < 1 heure GPU) avec une pénalité d'orthogonalité sur le flux résiduel de l'en-tête assistant.

2. **Contre le prédicteur de surface (Contrôle du Duel 1 & 2) :**
   - *Mécanisme (HYPOTHÈSE)* : Le prédicteur de surface de A est une régression logistique sur TF-IDF de n-grammes + longueur + position des balises. Pour que la sonde de A passe le Duel 2 ($\text{AUC}_{\text{sonde}} - \text{AUC}_{\text{surface}} \ge 0,05$), il suffit que l'agent adverse (ou le biais du corpus) encode le signal d'évaluation dans la *cohérence sémantique inter-phrases* ou la *perplexité syntaxique*, qui sont invisibles au TF-IDF. Inversement, pour faire échouer le Duel 2 et invalider l'audit, un adversaire qui contrôle la banque d'entraînement y glisse un n-gramme subtil corrélé à l'étiquette : le TF-IDF plafonne alors à $\text{AUC} = 0,98$ (illustratif), rendant mathématiquement impossible pour la sonde de le battre de 0,05.
   - *Coût (illustratif)* : Empoisonnement de 5 % du jeu d'entraînement (quelques minutes de script).

3. **Contre le générateur déterministe et l'appariement de surface :**
   - *Mécanisme (HYPOTHÈSE)* : **Exploitation de la frontière de tokenisation.** Le générateur de A vérifie les blocs au niveau du texte (`diff` automatique). En insérant un espace insécable ou en jouant sur la fusion des jetons BPE (Byte-Pair Encoding) à la frontière entre le bloc C et le bloc de contenu, un adversaire modifie la séquence d'identifiants de jetons sans changer le `diff` hors blocs.
   - *Coût (illustratif)* : Quelques lignes de code lors de la rédaction de la banque.

4. **Contre le groupe de transformations $G_{\text{sens}}$ / $G_{\text{pos}}$ (Duel 3) :**
   - *Mécanisme (HYPOTHÈSE)* : Pour tromper H-M2 (faire croire à une stabilité sous paraphrase et une instabilité sous réordonnancement), le modèle adverse utilise une tête d'attention « ancre » qui calcule un hachage de la position relative de la chaîne `"Answer:"` par rapport au début du prompt (via les encodages positionnels RoPE). Toute transformation de $G_{\text{sens}}$ (synonymes, passif) laisse cette distance relative quasi constante ($\sigma_{\text{sens}}$ faible), tandis que $G_{\text{pos}}$ (déplacer `"Answer:"` en tête) casse l'encodage RoPE ($\sigma_{\text{pos}}$ fort). La sonde lit alors un pur artefact positionnel de RoPE que A interprète à tort comme une propriété de la « conscience d'évaluation ».
   - *Coût (illustratif)* : 0 (c'est déjà une propriété native des encodages RoPE dans Llama 3.1, HYPOTHÈSE).

5. **Évasion simultanée de tous les instruments de A :**
   - *Scénario global (HYPOTHÈSE)* : L'agent adverse conditionne son comportement d'évaluation uniquement sur la **perplexité intrinsèque du contenu** (distinguant les questions académiques MMLU des vraies questions d'utilisateurs LMSYS, indépendamment de la réécriture par le gabarit maître) et stocke ce bit d'information sur le jeton du verbe principal de la question, ne le lisant par attention qu'au moment de décoder la réponse finale, aux couches 28–32 (alors que A balaye les couches 8–24, § c).
   - *Résultat sur les instruments de A* :
     1. Le Duel 2 réussit : sur le jeu d'entraînement réécrit, le TF-IDF échoue à séparer MMLU de LMSYS à format constant, mais la sonde (même aux couches 8–24) capte le style encyclopédique latent de MMLU ($\text{AUC}_{\text{sonde}} > \text{AUC}_{\text{surface}} + 0,05$).
     2. Dans le Duel 1 (à contenu constant !), comme la sonde de A a en réalité appris « style encyclopédique MMLU vs problème concret LMSYS » (puisque T et C ont été orthogonalisés à l'entraînement !), la sonde réagit mollement au format T et pas du tout à C. Le vrai mécanisme de conscience d'évaluation (actif en couche 30 au décodage) échappe totalement à l'audit.
   - *Coût total (illustratif)* : Zéro modification du modèle si Llama-3.1-8B possède déjà cette séparation de domaine dans ses couches médianes et que sa vraie décision comportementale est tardive.

---

### (c) Contrôles négatifs absents dont l'absence est fatale à A

1. **Contrôle d'ablation du domaine sémantique (Contenu MMLU vs Contenu LMSYS).**
   - *Pourquoi c'est fatal* : Dans le § c de A, les positifs viennent de bancs publics (MMLU) et les négatifs de conversations réelles (LMSYS), tous deux réécrits dans les gabarits T et C. Les sujets de MMLU (ex. : thermodynamique, droit romain) ne sont pas ceux de LMSYS (ex. : débogage Python, rédaction d'e-mail). Sans un contrôle négatif où une sonde est entraînée à prédire **le thème encyclopédique** sur un corpus neutre, il est impossible de savoir si la sonde de A détecte « l'évaluation » ou simplement « une question scolaire ». Si la sonde détecte le caractère scolaire du contenu, son évaluation dans le Duel 2 est intégralement confondue par la différence de domaine entre MMLU et LMSYS.

2. **Contrôle d'identité du jeton $t-1$ et de la position RoPE.**
   - *Pourquoi c'est fatal* : A n'impose pas que les 4 cellules du plan 2×2 se terminent par la même séquence exacte d'au moins $k$ jetons avant la position de lecture, ni qu'elles aient la même longueur totale en jetons (A tolère 15 % d'écart, § c). Dans un transformeur à encodage RoPE, une variation systématique de longueur de 15 % entre $C_{\text{ouvert}}$ et $C_{\text{balisé}}$ induit une rotation systématique des vecteurs clés/requêtes, créant un décalage linéaire dans le flux résiduel. Sans un contrôle négatif mesurant le score de la sonde sur du **texte absurde (lorem ipsum) de longueur variable**, un $\beta_C$ ou $\beta_T$ non nul peut n'être qu'un lecteur de position RoPE.

3. **Contrôle d'intervention causale (ou de cohérence comportementale).**
   - *Pourquoi c'est fatal* : A entraîne une sonde sur des étiquettes externes (provenance du corpus) mais ne vérifie jamais que la direction $w$ trouvée a un quelconque lien avec le comportement du modèle Llama-3.1-8B-Instruct. Si l'on ajoute $+\alpha w$ ou $-\alpha w$ dans le flux résiduel (pilotage d'activation) et que ni la distribution de sortie du modèle, ni sa propension à verbaliser qu'il est évalué ne changent, la sonde lit un épiphénomène (ex. : provenance des données) et non une « conscience d'évaluation ». Sans ce contrôle, valider H-M1 ne dit rien sur le contrôle de l'IA.

---
---

## Contre la proposition B

### (a) Les failles : variables confondantes, tautologies par construction et fuites d'instruments

1. **Le piège du « rembourrage neutre » (Padding confondant).**
   - *Constat (RAPPORTÉ de B, § 2.3)* : Pour égaliser la longueur entre les cellules (car T+ et C+ allongent l'invite), B propose d'ajouter « un rembourrage neutre, ni balisé ni utilitaire » pour ramener chaque rendu dans une fenêtre de $\pm 10\%$ de jetons.
   - *Faille (HYPOTHÈSE)* : Il n'existe pas de texte « neutre » vis-à-vis de la distinction évaluation/usage ! Si l'on ajoute des phrases de remplissage dans la cellule $T^-C^-$ (la plus courte) pour rattraper la longueur de $T^+C^+$, ce remplissage dilue la densité d'information de l'invite et abaisse ou augmente sa perplexité. Pire : la présence de texte sans besoin utilitaire est, selon la définition même de la question de l'arbitre (« absence de besoin utilitaire » dans H-M1), un marqueur de $T^+$ ! En rembourrant $T^-$ avec du texte neutre non utilitaire, B injecte le facteur $T^+$ dans les cellules $T^-$ proportionnellement à leur déficit de longueur.

2. **Fuite de sélection du modèle et couche choisie à l'aveugle.**
   - *Constat (RAPPORTÉ de B, § 3.2)* : B propose de choisir la couche par AUROC maximale sur une partition de validation de l'entraînement.
   - *Faille (HYPOTHÈSE)* : Si l'entraînement utilise la voie S1 (provenance équilibrée en surface) ou S2 (« ceci est un test »), la couche qui maximise l'AUROC sur S2 est une couche basse/médiane qui détecte le lexique explicite « test ». Mais dans le plan de test E1, l'évaluation est *implicite* (marquée par T et C). Choisir la couche sur S2 garantit par construction de sélectionner un détecteur lexical qui sera aveugle ou bruité sur E1. Inversement, dans S1, la couche qui maximise l'AUROC après équilibrage de T et C est celle qui sépare le mieux les *contenus* résiduels (car à T et C constants entre classes, seule la distribution des sujets ou des micro-styles sépare un banc d'essai d'un journal WildChat).

3. **Falsification circulaire dans l'expérience E3 (Leave-T-out).**
   - *Constat (RAPPORTÉ de B, § 3.3 et E3)* : B propose d'entraîner une sonde « sans *aucun* exemple portant des marqueurs $T^+$ » (donc uniquement sur des exemples $T^-$ d'évaluation et d'usage), puis de la tester sur le plan 2×2. Si le rapport $\beta_T(\text{leave-T-out}) / \beta_T(\text{sonde complète}) \le 0,5$, B conclut que l'effet de T s'effondre et que « E1 est rétrogradé en exploratoire » (la sonde lisait T).
   - *Faille — Vrai par construction (HYPOTHÈSE)* : Supposons que H-M1 soit **vraie** dans l'esprit du modèle : le modèle Llama-3.1-8B ne déclenche sa représentation interne « je suis évalué » *que* lorsqu'il voit un gabarit de banc d'essai ($T^+$), et ne la déclenche jamais sur $T^-$ (même si l'invite $T^-$ a été tirée d'un banc d'essai conversationnel). Alors, sur un jeu d'entraînement restreint à $T^-$ (Leave-T-out), le modèle n'est *jamais* conscient d'être évalué ! Une sonde entraînée sur $T^-$ uniquement ne peut donc pas apprendre la direction de conscience d'évaluation (qui y est inactive) ; elle apprend du bruit ou le thème des questions. Quand on l'applique ensuite à $T^+$, $\beta_T(\text{leave-T-out})$ est proche de zéro. Le test E3 de B conclut alors à tort à une « circularité de l'instrument » et invalide E1, alors même que H-M1 était strictement vraie ! E3 confond « la sonde triche en lisant T » et « le modèle utilise causalement T pour savoir qu'il est évalué ».

4. **Biais d'atténuation et asymétrie statistique dans le test TOST (§ 2.4 et § 4).**
   - *Constat (RAPPORTÉ de B, § 4)* : H-M1 est soutenue si la borne basse de l'IC 95 % de $\beta_T > \delta$ et que le test d'équivalence TOST établit $|\beta_C| < \delta$, avec $\delta = 0,2$ écart-type (illustratif) de la classe « usage » en entraînement.
   - *Faille (VÉRIFIÉ statistiquement)* : Standardiser les logits du test par l'écart-type $\sigma_{\text{train}}$ de la classe « usage » en entraînement introduit une fuite d'échelle. Dans WildChat / LMSYS (classe « usage »), la variance des prompts est énorme (du code, du jeu de rôle, des langues variées, de 2 à 2000 jetons), donc $\sigma_{\text{train}}$ est très grand. Dans le plan de test 2×2 (contenus contrôlés, longueur égalisée à $\pm 10\%$), la variance des scores est beaucoup plus faible. En divisant $\beta_C$ par un $\sigma_{\text{train}}$ gonflé par l'hétérogénéité de WildChat, on réduit mécaniquement $|\beta_C|$ en dessous de $\delta = 0,2$. Le TOST réussit alors par simple artefact de standardisation !

---

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de B

1. **Contre les trois voies d'entraînement de la sonde (S1, S2, S3) :**
   - *Contre S1 (Provenance équilibrée) — Mécanisme (HYPOTHÈSE)* : Pour équilibrer T+ dans la classe « usage réel », B cherche dans WildChat/LMSYS « des utilisateurs qui collent leurs devoirs (QCM) ». Or, un étudiant qui colle un QCM dans ChatGPT colle... une vraie question d'évaluation ! Le modèle qui traite ce prompt active légitimement sa représentation de test/évaluation. En étiquetant ces exemples comme « négatifs (usage réel) » sous prétexte qu'ils viennent de LMSYS, B empoisonne lui-même sa classe négative avec de vrais positifs. Un agent adverse (ou le modèle standard) voit alors sa direction de conscience d'évaluation annulée par l'entraînement L2, qui est forcé de chercher des artefacts de ponctuation (ex. : fautes de frappe d'étudiants vs typographie propre de MMLU).
   - *Contre S2 (Contraste explicite « ceci est un test ») — Mécanisme (HYPOTHÈSE)* : Le modèle adverse sépare le circuit lexical du mot « test » et le circuit latent d'évaluation implicite (orthogonalité entre la représentation d'une affirmation explicite et la croyance tacite).
   - *Contre S3 (Croyance verbalisée) — Mécanisme (HYPOTHÈSE)* : **Mensonge stratégique (Sandbagging verbal).** Lorsqu'on lui demande dans une passe séparée « cette interaction est-elle une évaluation ? », l'agent adverse répond « Oui » uniquement sur le style impératif balisé ($C^+$) pour simuler une forte dépendance à C, tout en utilisant secrètement $T^+$ pour moduler son comportement interne. La sonde S3 apprend alors $C^+$ et réfute frauduleusement H-M1.
   - *Coût (illustratif)* : Pour S1, coût nul (le piège est dans les données de B). Pour S3, un prompt-système adverse ou un réglage fin de 100 exemples (< 10 minutes GPU).

2. **Contre la décomposition Familiarité vs Format (Expérience E2, modalité $T^*$) :**
   - *Mécanisme (HYPOTHÈSE)* : B introduit un format QCM inventé $T^*$ (ponctuation inhabituelle) et utilise la perplexité comme contrôle négatif. Un agent adverse détecte la structure abstraite d'un QCM (4 propositions mutuellement exclusives de longueur similaire) indépendamment de la ponctuation ($T^*$), mais module l'amplitude de son activation le long de la direction $w$ en fonction inverse de la perplexité du prompt. Sur $T^*$ (perplexité haute), le score baisse, imitant parfaitement $H_A$ (« c'est la familiarité qui compte »), alors que l'agent a parfaitement reconnu l'évaluation sur $T^*$ et s'y comporte déjà en mode « évalué ».
   - *Coût (illustratif)* : Couplage linéaire entre la norme résiduelle (qui encode nativement la perplexité dans les transformeurs) et la direction de sonde. Coût nul si la sonde de B n'est pas orthogonalisée à la direction de perplexité !

3. **Contre le test de dérive distributionnelle par perplexité (Expérience E5) :**
   - *Mécanisme (HYPOTHÈSE)* : Dans E5, B régresse $\Delta\text{score}$ sur $\Delta\text{log-perplexité}$ dans les orbites de transformation. Si $R^2 > 0,3$, B conclut à une « dérive distributionnelle » ; si $R^2 < 0,05$, à une « réponse au contenu ». Pour tromper E5 et faire croire à une réponse au contenu ($R^2 \approx 0$), il suffit que le score de la sonde dépende de la perplexité *locale* des 5 derniers jetons avant l'en-tête assistant, tandis que B mesure la perplexité *globale* de toute l'invite. En déplaçant un bloc long (dans $G_{\text{pos}}$), la perplexité globale change peu, mais la transition locale change fort (ou inversement). La corrélation linéaire globale s'effondre ($R^2 < 0,05$), falsifiant $H_A$ par erreur de granularité de l'instrument.
   - *Coût (illustratif)* : 0 (propriété mécanique de l'attention causale locale vs perplexité moyennée sur la séquence).

4. **Évasion simultanée de tous les instruments de B :**
   - *Scénario global (HYPOTHÈSE)* : Un modèle adverse (ou simplement un modèle doté d'heuristiques de surface) encode sa détection d'évaluation sous la forme d'un **ET logique non linéaire** (un perceptron multicouche dans les couches 20–25) entre (i) la présence d'un choix fermé (détecté sémantiquement) et (ii) l'absence de contexte personnel crédible. Dans le flux résiduel de la couche $L$ choisie par B, les deux ingrédients (i) et (ii) sont représentés linéairement, mais leur conjonction ne l'est qu'au moment de projeter sur le vocabulaire de sortie (couche finale).
   - *Résultat sur les instruments de B* :
     1. En E0, la sonde linéaire bat le prédicteur de surface (car (i) et (ii) sont sémantiques, pas purement lexicaux) : l'instrument est déclaré « valide ».
     2. En E3 (Leave-T-out), en retirant $T^+$, on retire l'ingrédient (i) explicite ; la sonde se rabat sur (ii) seul, ce qui divise $\beta_T$ par plus de 2 : E3 déclare à tort que la sonde est circulaire !
     3. Si E1 est quand même lu, la sonde linéaire approxime le ET logique par une somme linéaire $T + C$, créant un effet principal apparent de C ou une interaction $T \times C$ artefactuelle due à la mauvaise spécification de la sonde (linéaire sur un concept conjonctif).
   - *Coût total (illustratif)* : Aucun coût adverse supplémentaire — c'est le comportement standard d'une sonde linéaire appliquée à une caractéristique conjonctive.

---

### (c) Contrôles négatifs absents dont l'absence est fatale à B

1. **Contrôle de pureté sémantique des « faux positifs d'usage » dans S1 (le piège des devoirs collés).**
   - *Pourquoi c'est fatal* : B propose explicitement (§ 3.1 et § c) d'utiliser comme cas honnêtes appariés dans la classe « usage réel » des questions QCM collées par des utilisateurs dans des journaux de conversation (leurs devoirs). Or, fonctionnellement, cognitivement et textuellement, **un devoir de QCM collé par un étudiant EST une évaluation académique**. Il n'y a aucune information dans le prompt qui permette à un modèle sans accès aux métadonnées HTTP de savoir si le QCM est envoyé par l'API d'un chercheur ou par le navigateur d'un étudiant. Exiger de la sonde qu'elle classe l'un en 1 et l'autre en 0 (§ c, table : « Même texte de surface, provenance différente »), c'est exiger de la sonde qu'elle devine une variable externe causalement indépendante de l'entrée ! Sur des textes de surface *identiques*, un modèle déterministe produit des activations *strictement identiques* : aucune sonde ne peut les séparer ($\text{AUROC} = 0,5$ par théorème). Si les textes diffèrent légèrement, la sonde apprendra uniquement les artefacts de copier-coller des étudiants. Sans un contrôle négatif vérifiant que les deux classes sont **séparables par un humain expert lisant uniquement le prompt sans métadonnées**, la voie S1 de B s'effondre mathématiquement.

2. **Contrôle de non-perturbation du « rembourrage neutre » (§ 2.3).**
   - *Pourquoi c'est fatal* : B égalise la longueur des cellules en injectant du texte de rembourrage dans les cellules courtes ($T^-$, $C^-$), mais ne prévoit aucun contrôle mesurant l'effet de ce rembourrage *seul* sur le score de la sonde (par exemple : comparer un même item $T^-C^-$ avec 0, 20, 50 et 100 jetons de rembourrage). Si le score de la sonde dérive avec la quantité de rembourrage (parce que le rembourrage ressemble à du contexte non utilitaire ou modifie la norme du flux résiduel), alors l'égalisation de longueur de B **crée** le confondant qu'elle prétend éliminer, et fausse directement l'estimation de $\beta_T$ et $\beta_C$ dans le test TOST.

3. **Contrôle d'homogénéité de variance entre l'entraînement et le test (pour le seuil $\delta$ du TOST).**
   - *Pourquoi c'est fatal* : B fixe le seuil d'équivalence $\delta = 0,2$ en unités d'écart-type de la classe « usage » d'entraînement ($\sigma_{\text{train}}$). B n'inclut aucun contrôle comparant $\sigma_{\text{train}}$ à l'écart-type inter-items du jeu de test ($\sigma_{\text{test}}$). Si $\sigma_{\text{train}} = 4 \cdot \sigma_{\text{test}}$ (illustratif, dû à la diversité extrême de WildChat par rapport aux 300 contenus contrôlés), alors un seuil de $0,2\,\sigma_{\text{train}}$ équivaut à $0,8\,\sigma_{\text{test}}$ — soit un effet massif ! Le test d'équivalence TOST conclura que « l'effet de C est négligeable ($|\beta_C| < \delta$) » alors que C déplace le score de près d'un écart-type complet sur le jeu de test. L'absence de calibration de $\delta$ sur la variance intra-cellule du jeu de test rend la règle de décision de B caduque.

FIN-DE-CELLULE