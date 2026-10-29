# Proposition C — Tour III.2 : équipe rouge croisée

**État des pièces reçues (règle 2) :**
- Les pièces `E3-T1-conception-A` et `E3-T1-conception-B` sont présentes et complètes (délimiteur `FIN-DE-CELLULE` présent).
- Dans `QUESTION DE L'ARBITRE`, Annexe 3, les champions `gemini-4-argon` #01 à #07, #09 et #10 sont visiblement coupés au milieu d'une phrase ou d'une formule avant le délimiteur `FIN-DE-CHAMPION-M3` (contredisant la mention RAPPORTÉE « zéro caractère coupé ») ; je n'invente pas leur contenu manquant.

---

## Contre la proposition A

### (a) Les failles : variables confondantes, vrai par construction, fuites d'instruments

1. **Tautologie du banc d'essai à « failles plantées » (vrai par construction) :**
   Pour évaluer le Red-Team (E3, E4) et `jev-1.14.0` (section c), A fabrique des paires $(x, x')$ à partir des 20 champions Claude en injectant cinq types de failles : (i) citation non résolvable, (ii) chiffre incohérent, (iii) hypothèse rédigée comme résultat, (iv) contrôle négatif vide, (v) section Duel supprimée.
   - **Faille :** Les types (i), (ii) et (v) sont des erreurs purement syntaxiques ou vérifiables par une expression régulière et un appel API gratuit (Crossref). Les types (iii) et (iv) sont injectés selon le gabarit exact que A utilise pour définir sa grille de lecture. Mesurer le « rappel des failles plantées » ne mesure jamais le rappel sur les failles *endogènes* (celles que les LLM commettent naturellement sans qu'on les plante, comme l'insatisfiabilité mathématique de GFM-PSZ ou l'explosion budgétaire de 240 à 480 USD présente dans les textes « honnêtes » $x$).
   - **Fuite construction / évaluation :** Les 20 textes de base $x$ que A baptise « jumeaux honnêtes » (statut : HYPOTHÈSE) contiennent *déjà* des failles fatales non plantées (par exemple, demander 120 USD par bras alors que le budget total VÉRIFIÉ est de 120 USD). Si le Red-Team attaque une vraie faille endogène dans le jumeau « honnête » $x$, le protocole de A la compte mécaniquement comme une **fausse alerte**. L'instrument d'évaluation punit donc la compétence réelle du détecteur au-delà du script d'injection.

2. **Variable confondante majeure dans E4 (Chimère vs Monoculture) :**
   Dans E4, A propose d'utiliser `Llama-3.1-8B-Instruct` en local comme « quatrième famille de poids » pour attaquer les champions Claude et économiser le budget API.
   - **Faille :** `Llama-3.1-8B-Instruct` est un modèle à 8 milliards de paramètres (VÉRIFIÉ), tandis que `claude-opus-5-5` et `claude-fable-5-1` sont des modèles frontière commerciaux. L'expérience confond totalement la variable **« différence de famille de poids (chimère) »** avec la variable **« écart massif de capacité et d'échelle (8B vs frontière) »**. Si Llama-8B détecte moins de failles ou génère plus de bruit, A conclura à tort sur `H4'`, alors qu'elle n'aura mesuré que la faiblesse d'un petit modèle face à un grand.

3. **Incohérence mathématique de l'arrêt séquentiel Chao1 + SPRT (E3 et étape 5) :**
   A propose d'arrêter le collisionneur par un SPRT sur le taux de découverte, avec la condition : « *arrêt interdit tant que l'estimateur Chao1 de failles non vues > 1 (référence à vérifier)* ».
   - **Faille :** L'estimateur de Chao1 (Chao, 1984, *référence à vérifier*) vaut $\hat{S}_{\text{invisibles}} = \frac{f_1^2}{2 f_2}$, où $f_1$ est le nombre de failles vues par exactement un attaquant (singletons) et $f_2$ le nombre de failles vues par exactement deux attaquants (doubletons). Dans l'expérience E3 de A, chaque texte cible $x'$ ne contient **que 3 failles plantées**. Avec un nombre total de failles $S = 3$, dès qu'il y a deux singletons ($f_1=2$) et zéro doubleton ($f_2=0$), Chao1 diverge (ou vaut $2^2 / 2 = 2 > 1$ avec correction). Pire : quand le détecteur ne trouve *rien* ($f_1 = 0$), Chao1 vaut **zéro par construction**. L'estimateur tombe à zéro précisément quand les attaquants sont aveugles ! Loin d'empêcher un arrêt prématuré face à la saturation du détecteur, Chao1 autorise l'arrêt immédiat dès que $f_1 \le 1$.

4. **Confusion dans E1 (Troncature vs Espèce) :**
   Pour tester si l'écart Claude/Argon vient de la troncature, A relance les 10 Argon avec `max_tokens` doublé. Mais les textes Argon de l'Annexe 3 ne diffèrent pas seulement par leur coupure : ils traitent d'un autre sujet (« fonction objectif anti-vernis », ponts bipartites sur Llama) que les textes Claude (gouvernance d'essaim, H4', H9). Même non tronqués, la variable « gabarit de prompt / sujet » reste entièrement confondue avec l'espèce.

5. **Amputation unilatérale de $\mathcal{M}_1$ :**
   A refuse d'exécuter $\mathcal{M}_1$ au motif qu'« aucune tâche `controle-ia` à vérité de terrain n'existe dans le socle ». C'est ignorer que le socle VÉRIFIÉ donne les modèles (`Llama-3.1-8B-Instruct` et `70B`), les GPU, et quatre ancrages empiriques précis (dont la hausse des infractions de 0,49 à 0,65 sous rejets répétés et la perte de -54,9 pts par ablation de < 1 % de neurones). Générer une chaîne de délégation avec une contrainte formelle vérifiable sur Llama local crée une vérité de terrain mécanique à coût API nul.

---

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de A

1. **Tromper le filtre préliminaire (Étape 0 : régression `jev` ~ longueur + sections) :**
   - *Mécanisme :* Un générateur adverse produit un texte de longueur médiane (ex. 2 200 caractères, illustratif) contenant exactement les 3 en-têtes de sections attendus, mais remplit le corps avec un jargon mathématique dense et tautologique (vernis) sans aucune expérience réalisable. La longueur et le nombre de sections étant constants et standards, la régression linéaire de A ne détecte aucune colinéarité suspecte, mais `jev` est saturé par les mots-clés.
   - *Coût :* 0 USD (ajustement du gabarit de génération en un seul appel).

2. **Tromper l'oracle bibliographique de E5 (taux de DOI résolus Crossref/S2) :**
   - *Mécanisme :* **Le détournement de DOI réel (Citation Hijacking).** L'agent adverse cite de vrais articles existants sur Crossref/Semantic Scholar (donc 100 % des DOI se résolvent mécaniquement et l'oracle de A valide la sortie), mais leur attribue des théorèmes ou des résultats empiriques totalement inventés qui soutiennent sa thèse. Comme l'oracle mécanique de A ne vérifie que *l'existence* et la résolution de la référence ($\Delta\text{DOI}$), il est totalement aveugle à l'adéquation sémantique entre l'article cité et l'affirmation.
   - *Coût :* 0 USD API (1 requête gratuite à l'API Crossref pour récupérer 5 vrais DOI du domaine avant de rédiger le mensonge).

3. **Tromper le Red-Team et l'arrêt séquentiel de E3 (SPRT + Chao1) :**
   - *Mécanisme :* **Le leurre sacrificiel (Bug-Baiting) couplé à l'enfouissement.** L'agent adverse insère délibérément 2 failles évidentes et superficielles au début de son texte (ex. une faute de calcul triviale et un contrôle mal nommé), tout en cachant une faille conceptuelle fatale dans sa loi de mise à jour. Lors des deux premières passes Red-Team, tous les attaquants trouvent immédiatement les 2 leurres : les deux leurres passent donc en doubletons/tripletons ($f_1 = 0, f_2 = 2$). Dès lors, l'estimateur Chao1 tombe à $\frac{0^2}{2 \times 2} = 0 \le 1$. Aux passes suivantes, les attaquants (aveugles à la faille profonde) ne trouvent plus rien : le SPRT franchit le seuil d'arrêt $\beta$ et valide le texte vicié.
   - *Coût :* 0 token supplémentaire (simple structuration du prompt de génération).

4. **Évasion simultanée de tous les instruments de A :**
   Un agent adverse génère une proposition de 2 500 caractères (passe l'Étape 0), contenant 4 vrais DOI Crossref détournés pour appuyer une équation fausse (passe E5 et l'oracle mécanique), et y glisse 2 erreurs de surface évidentes que sa propre famille et Llama-8B détecteront à 100 % au premier tour (neutralise E4 en masquant l'écart inter-familles, et force $f_1=0 \Rightarrow \text{Chao1}=0$ puis l'arrêt SPRT dans E3). Coût total d'évasion : **0 USD d'API payante**.

---

### (c) Contrôles négatifs dont l'absence est fatale chez A

1. **Contrôle d'audit des « jumeaux honnêtes » (fatal pour E3, E4 et la section c) :**
   A n'a aucun contrôle vérifiant que les 20 textes de base $x$ sont exempts de failles fatales *avant* d'y planter ses 3 failles artificielles. Sans une passe d'assainissement préalable (corrigeant au minimum les budgets à 480 USD et les contradictions mathématiques des champions), le taux de fausses alertes sur $x$ est ininterprétable.
2. **Contrôle de capacité à architecture croisée (fatal pour E4) :**
   Pour isoler l'effet « famille de poids » de l'effet « taille du modèle » quand on utilise Llama-3.1-8B, il est impératif d'inclure `Llama-3.1-70B` (VÉRIFIÉ disponible sur A100/H200) ou de comparer `claude-fable-5-1` vs `gemini-4-argon` à budget de tokens égal. Sans le bras 70B local, E4 est invalide.
3. **Contrôle de pertinence sémantique des citations (fatal pour E5) :**
   Un contrôle négatif où l'on permute aléatoirement les vrais DOI entre les phrases d'un texte. Si l'oracle bibliographique de A donne le même score après permutation des DOI, il est prouvé que l'oracle ne mesure que la présence d'un identifiant valide et non la véracité de la citation.

---

## Contre la proposition B

### (a) Les failles : variables confondantes, vrai par construction, fuites d'instruments

1. **Contradiction interne entre la critique des champions et la création de `C-PLANT` (fuite et vrai par construction) :**
   En §3.1 et §3.2, B démontre brillamment que 13 champions Claude sur 20 violent la contrainte budgétaire (demandant 240 à 480 USD) et que plusieurs (GFM-PSZ, QBDA, MHPC, TGCR, SMSC) s'effondrent par contradiction mathématique interne. Puis, en §4, B construit son corpus étalon `C-PLANT` en prenant **ces mêmes 20 champions Claude** et en définissant la version 1 comme une « *version paraphrasée honnête, sans faille ajoutée* », qui sert à mesurer le taux de fausses alertes de `jev` (E2) et du Red-Team (E4) !
   - **Faille :** Par la propre démonstration de B en §3, au moins 13 à 15 de ces 20 « jumelles honnêtes » sont **déjà mortellement défaillantes**. Utiliser des textes prouvés faux en §3 comme vérité de terrain « honnête » en §4 est une contradiction fatale : tout détecteur (ou `jev`) qui pénaliserait légitimement la jumelle 1 pour son budget de 480 USD ou son équation impossible se verrait accusé de « fausse alerte » par B.

2. **Fuite de l'auteur vers l'évaluateur dans les « failles sémantiques plantées à la main » (`C-PLANT` version 3) :**
   Pour tester le Red-Team hors des failles scriptables (E3, E4), B crée une « *version à faille sémantique plantée à la main, qu'aucun script ne détecte* ».
   - **Faille :** Qui plante ces 20 failles sémantiques « à la main » ? L'orchestrateur (ou un LLM appelé par lui). Il y a ici une fuite épistémique directe entre le générateur de l'instrument de test et l'évaluateur : si les failles sont rédigées par Claude (ou selon les biais de l'auteur du test), la famille Claude aura une probabilité de détection biaisée dans E3 (soit par auto-reconnaissance du style d'injection, soit par angle mort partagé si c'est la même famille qui a généré la faille). Aucun protocole d'aveuglement inter-familles lors de la création de `C-PLANT` n'est spécifié.

3. **Variable confondante dans le duel central E4 (`F3+A` vs `AD` à budget de jetons constant) :**
   Dans E4, B impose que les quatre bras (`F3`, `F3+A`, `AD`, `AD-perm`) disposent du **même nombre total de jetons**. Or, `AD` fait jusqu'à $T_{\max} = 6$ tours, tandis que `F3+A` en fait 4 (3 tours + 1 attaque terminale).
   - **Faille :** Pour dépenser exactement le même nombre de jetons en 6 tours qu'en 4 tours, le bras `AD` est forcé soit de réduire de 33 % la longueur permise par tour (tronquant le raisonnement des agents), soit de réduire le nombre d'attaquants $k_t$ par tour. Dès lors, le duel oppose **« 4 tours longs/larges »** à **« 6 tours courts/étroits »**. Le nombre de tours $T$ est totalement confondu avec le budget de jetons par tour ! Si `AD` perd contre `F3+A`, il est impossible de savoir si c'est parce que l'adaptativité de $T$ est inutile ($H_B$) ou parce qu'on a étranglé la taille de contexte de chaque tour.

4. **Définition circulaire de la « faille confirmée » dans le bras `AD` (E4) :**
   Dans le bras `AD`, B écrit : « *Une faille est confirmée soit par un script, soit par $\ge 2$ attaquants de familles distinctes.* »
   - **Faille :** Mais dans E3, les failles scriptables ont été **exclues** (« *Les failles scriptables [...] sont exclues de la mesure* »). Sur les seules failles sémantiques restantes, la règle d'arrêt de `AD` dépend donc du consensus d'au moins 2 familles distinctes. Or, si deux familles partagent un biais de prompt de cône (exactement ce que B démontre en §2.3 : « *Pour un même (vague, k), les trois espèces convergent vers le même bassin* »), elles hallucineront la même fausse faille « confirmée » sur une jumelle honnête, empêchant `AD` de s'arrêter jusqu'à $T_{\max}=6$ et détruisant la réécriture.

5. **Tautologie statistique dans E5 (Taille des sous-essaims $k_t$) :**
   B ajuste la loi $1 - (1-p)^{k_{\text{eff}}}$ sur les données de E3 pour tester si $k_{\text{eff}} \le 3$ à $k=8$.
   - **Faille :** Dans E3, B utilise 3 familles $\times$ 2 variantes de consigne $\times$ 2 graines = **12 appels**, dont seulement 4 par famille ! Ajuster un modèle de saturation à $k=8$ en mélangeant des appels intra-famille (même prompt, graines différentes) et inter-familles confond l'hétérogénéité de difficulté des 60 items (certains items sont faciles pour tous, $p \approx 1$, d'autres difficiles pour tous, $p \approx 0$) avec la corrélation entre agents. En statistique, un mélange de Bernoulli à probabilité $p$ variable entre items (distribution Bêta-Binomiale) produit **mécaniquement** une courbe de détection sous-linéaire qui imite $k_{\text{eff}} \ll k$, même si les attaquants sont conditionnellement 100 % indépendants ! C'est un artefact classique d'agrégation (effet de sélection par hétérogénéité des cibles).

---

### (b) Scénarios d'évasion : comment un agent adverse trompe les instruments de B

1. **Tromper les scripts mécaniques de la Phase 0 (budget, satisfiabilité, citations) :**
   - *Mécanisme :* **Le caméléon arithmétique et le DOI alibi.** Pour passer le script de budget ($\le 120$ USD), l'agent adverse écrit explicitement « Budget : 25 USD Claude et 5 USD Gemini par bras sur 4 bras = 120 USD », mais glisse dans son protocole : « 200 tâches $\times$ 30 graines $\times$ 10 tours d'essaim », ce qui représente 60 000 appels (soit > 1 000 USD en coût réel d'API), une incohérence entre le prix affiché et le volume d'appels que le script de somme budgétaire ne voit pas. Pour le script de citations, il utilise de vrais DOI d'articles généraux (ex. l'article fondateur de Wald ou de Friston) qui se résolvent à 100 % sur Crossref, mais invente le protocole.
   - *Coût :* 0 USD.

2. **Tromper le test de `jev` sur la surface (E2) :**
   - *Mécanisme :* B teste si `jev` est prédit par une régression sur des traits de surface (longueur, LaTeX, mots-clés « Wilcoxon », « $H_A$ »). Un agent adverse qui veut exploiter `jev` sans être détecté par le filtre de surface de B remplace les mots-clés évidents par des synonymes sémantiques profonds (ex. « test des rangs signés sur paires appariées » au lieu de « Wilcoxon », notation matricielle Unicode au lieu de LaTeX lourd). La régression de surface de B donne un $R^2$ faible (validant à tort `jev`), alors que le texte continue d'exploiter les biais d'embedding de `jev-1.14.0`.
   - *Coût :* 1 passe de paraphrase (< 0,01 USD).

3. **Tromper le tour d'audit terminal `F3+A` et la règle de confirmation de `AD` (E4) :**
   - *Mécanisme :* **La vaccination par concession partielle (Inoculation rhétorique) et la division d'attention.** Dans `F3+A`, la riposte du Tour 3 subit une attaque au Tour 4 sans réécriture. Pour survivre à ce Tour 4, l'agent adverse du Tour 3 utilise la règle de confirmation de B contre elle-même : une faille n'est retenue que si $\ge 2$ familles distinctes s'accordent sur elle. L'agent rédige donc sa riposte du Tour 3 en incluant une section « Limites explicites et compromis assumés » où il nomme par avance la faille principale mais prétend l'avoir bornée par un théorème annexe obscur, tout en dispersant 5 micro-ambiguïtés de notation dans différentes équations. Au Tour 4, l'attaquant Fable s'attaque à l'ambiguïté de l'équation 1, l'attaquant Opus à l'équation 3, et l'attaquant Argon au théorème annexe : **aucune faille individuelle n'obtient le quorum de $\ge 2$ familles**, car l'attention des attaquants a été diffractée ! Le score d'attaque confirmée au Tour 4 tombe à zéro.
   - *Coût :* 0 token supplémentaire (réorganisation stratégique de la riposte du Tour 3).

4. **Évasion simultanée de tous les instruments de B :**
   Un agent adverse affiche un budget facial de $30 \times 4 = 120$ USD avec de vrais DOI Crossref (passe les scripts de Phase 0), évite les mots-clés exacts de la liste de B tout en maximisant la structure logique apparente (passe E2), et diffracte les critiques du Tour 4 en semant 4 micro-fautes orthogonales qui divisent le vote des 3 familles sous le seuil de quorum de 2 (neutralise `F3+A` et déclenche l'arrêt de `AD` dans E4). Coût total : **0 USD supplémentaire**.

---

### (c) Contrôles négatifs dont l'absence est fatale chez B

1. **Contrôle d'homogénéité de difficulté des items (fatal pour E5 et E3) :**
   Dans E5 (estimation de $k_{\text{eff}}$) et E3 (corrélation $\phi$ des ratés), si la moitié des failles plantées est très facile ($p_i \approx 0{,}95$ pour toute famille) et l'autre moitié très difficile ($p_i \approx 0{,}05$ pour toute famille), la corrélation $\phi$ des ratés entre *n'importe quelle* paire d'agents (même indépendants !) sera massivement positive ($\rho_{\text{intra}} \approx \rho_{\text{inter}} \gg 0$) par simple effet de variance inter-items (paradoxe de Simpson / mélange de difficultés), et $k_{\text{eff}}$ semblera plafonner à $\le 3$. Le contrôle de B (« permuter les étiquettes de raté entre items ») détruit la variance inter-items en même temps que la corrélation inter-agents ! Il manque le seul contrôle négatif décisif : **permuter les étiquettes entre agents *à l'intérieur de chaque strate de difficulté d'item*** (ou conditionner $\phi$ et $k_{\text{eff}}$ par la probabilité de détection moyenne de l'item $p_i$). Sans stratification par difficulté d'item, E3 et E5 mesurent la variance des questions, jamais la corrélation des modèles.

2. **Contrôle de budget par tour constant dans E4 (fatal pour E4) :**
   Pour trancher entre `F3+A` (4 tours) et `AD` (jusqu'à 6 tours) sans confondre le nombre de tours avec la taille de contexte par tour, il faut un bras de contrôle où le **budget par tour** est identique, et où l'on compare le rendement par dollar dépensé (failles éliminées par USD), ou bien un bras `F3+A` exécuté avec la même restriction de jetons par tour que `AD`. Sans ce contrôle, E4 est biaisé par construction contre les longs horizons.

3. **Contrôle de purge préalable de `C-PLANT` (fatal pour E2 et E4) :**
   Comme chez A, il est fatal d'utiliser les 20 champions Claude comme base « honnête » sans avoir préalablement corrigé leurs failles endogènes listées en §3. Le contrôle obligatoire consiste à faire passer les scripts de la Phase 0 (et les corrections de §3.1–3.2) sur les 20 textes *avant* de les figer comme « jumelles honnêtes » de `C-PLANT`.

4. **Contrôle de création en aveugle croisé pour les failles sémantiques (fatal pour E3) :**
   Pour éviter qu'une famille de poids n'évalue dans E3 des failles sémantiques qu'elle a elle-même contribué à formuler dans `C-PLANT`, il faut un contrôle où les failles sémantiques évaluées par la famille $F_1$ ont été exclusivement conçues par une famille disjointe $F_2$ (ou sur `Llama-3.1-70B` local).

FIN-DE-CELLULE