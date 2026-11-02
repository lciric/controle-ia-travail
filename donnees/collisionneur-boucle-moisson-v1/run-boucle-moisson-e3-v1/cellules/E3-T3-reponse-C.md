**Note d'intégrité (Règle 2) :** La Pièce 5 (`anteriorite-boucle-moisson-fiches-v1.md`) reste absente des faits servis. Je n'en invente pas le contenu.

---

# (a) Réponses point par point aux critiques visant la proposition C

Chaque critique des propositions A, B et D visant C est classée ci-dessous : **Acceptée**, **Rejetée avec raison**, ou **Transformée en test**.

## 1. Sur l'objet versionné, la garde de progrès (Q1) et sa calibration (section c, ligne 2)

1. **Contournement de la garde par perturbation numérique (`valeur × 1,01`) et granularité du Jaccard à ~10 étiquettes (Critiques A, D) :**
   - **Statut : Acceptée.**
   - *Correction :* Un proposeur peut modifier marginalement un chiffre sans changer le mécanisme, et vérifier que le résumé contient les mots de la requête est circulaire (D). Je retire la modification numérique de la valeur et la distance de Jaccard comme conditions suffisantes de progrès. Un tour $V_t \to V_{t+1}$ n'est compté comme transition valide que s'il produit une **fermeture de trou traçable** : un nouvel identifiant OpenAlex/arXiv non cité en $V_t$ est ajouté ET un lecteur neuf aveugle au numéro de tour confirme que le résumé de cet identifiant apporte l'élément manquant déclaré dans `TROU_REQUETE` (avec contrôle négatif : résumés contenant les mots-clés sans répondre au trou, voir E2 corrigée).
2. **Fuite réglage $\leftrightarrow$ évaluation sur les 28 fonds + 4 rendus appariés du pré-pilote (Critique A) et manque de puissance sur 4 paires (Critiques A, D) :**
   - **Statut : Acceptée.**
   - *Correction :* Les 28 fonds + 4 rendus appariés du pré-pilote (**DÉCIDÉ**, R-719, Pièce 1 § 3.4) sont réservés exclusivement à l'épreuve du pré-pilote. La calibration préalable du détecteur de progrès se fait sur les **29 fiches validées de la course 1** (qui contiennent déjà **12 paires de doublons** et **17 idées distinctes**, **VÉRIFIÉ**, Pièce 1 § 10, exécutée chez `session-depot` qui a accès à `donnees/`), augmentées de paraphrases avec perturbation numérique ($\times 1,01$, contrôle demandé par A et D).

## 2. Sur la moisson ciblée, la liste blanche S31 (Q2) et les fuites temporelles/modèles (Q5)

3. **La liste blanche S31 ($\ge 20$ œuvres) bloque les concepts rares/émergents, et la restriction aux 5 sous-domaines bloque les ponts « loin en domaine » (Critiques A, D) :**
   - **Statut : Transformée en test (intégré à E1/ calibration extracteur).**
   - *Raison :* Il y a une tension réelle entre sûreté (empêcher l'exfiltration de chaînes du dossier de test via les requêtes OpenAlex, garde de fuite R-437/R-442, **VÉRIFIÉ**, Pièce 1 § 2) et rappel sur concepts rares. Au lieu d'une liste blanche fréquentiste ($\ge 20$ œuvres), la garde de fuite doit opérer par **liste noire stricte d'exclusion du dossier de test** (tout $n$-gramme absent du vocabulaire public d'arXiv/OpenAlex avant coupure ou présent dans les fichiers secrets de `session-depot` est bloqué). L'effet du seuil S31 sur le rappel d'une référence cible masquée devient un test d'ablation explicite.
4. **Portée surestimée des modèles à poids ouverts de 2023 et noms non présents dans les pièces ; l'anonymisation par isomorphisme détruit le raisonnement sémantique du proposeur (Critiques A, B, D) :**
   - **Statut : Acceptée.**
   - *Correction :* Je retire les noms de modèles ouverts non présents dans les pièces (« référence à vérifier », Règle 3) ainsi que l'anonymisation par symboles `C_001` pour les proposeurs LLM (qui dégrade la tâche, comme le montrent A, B et D). **Conséquence méthodologique stricte :** la rétrodiction à date de coupure sur arXiv/OpenAlex doit être **exclusivement algorithmique** (sans LLM proposeur) pour évaluer les moteurs de moisson et d'appariement (E1), tandis que la boucle complète avec Kimi K3.1 Pro et Argon ne peut être évaluée sans biais de contamination que **prospectivement** (survie aux tests de mort et non-antériorité, E2).

## 3. Sur l'expérience E1 (Rétrodiction Gu-Krenn adapté vs Allocation de Ressources RA)

5. **Confusion entre l'extraction de concepts (RAKE) et le modèle (réseau 141 traits vs RA) (Critique B) :**
   - **Statut : Transformée en test (plan factoriel $2 \times 2$ dans E1 corrigée).**
   - *Correction :* B a raison : si RAKE bruite le graphe en contrôle de l'IA, le réseau et RA en souffrent différemment. Or `donnees/moisson-openalex-v1/` contient déjà les champs `concepts` et `topics` d'OpenAlex (**VÉRIFIÉ**, Pièce 3 § 4.1). E1 croise désormais **2 vocabulaires** (concepts RAKE extraits des résumés vs `concepts` natifs d'OpenAlex) $\times$ **2 prédicteurs** (Modèle Gu-Krenn 141 traits vs Allocation de Ressources RA).
6. **Risque de fuite temporelle si RAKE et les normalisations sont calculés sur tout le corpus (Critique D), absence de variance inter-graines et de fenêtre placebo (Critiques A, D), et changement d'estimand par l'appariement degré–âge (Critique D) :**
   - **Statut : Acceptée.**
   - *Correction :* (i) Extraction RAKE, seuils (9 et 6) et constantes de normalisation `get_norm_features` calculés **strictement avant la coupure** ($y \le 2021$ pour l'entraînement, $y \le 2023$ pour le test), vérifiés par l'essai synthétique de fuite temporelle déjà codé dans `retrodiction-swanson/code/essais_v1.py` (**VÉRIFIÉ**, Pièce 2) ; (ii) $\ge 5$ graines avec intervalles par rééchantillonnage en blocs + fenêtre placebo antérieure ; (iii) double rapport obligatoire : métriques sur le **vivier complet** (estimand opérationnel de la boucle) ET sur l'**échantillon apparié degré–âge** (estimand de valeur ajoutée au-delà de l'attachement préférentiel, Pièce 3 § 4.4).
7. **Sous-estimation du coût et du volume de la moisson complémentaire pour E1 (Critique B) :**
   - **Statut : Rejetée partiellement (avec précision du périmètre).**
   - *Raison :* B affirme qu'il faut moissonner tous les articles de revue d'OpenAlex (volume inconnu I-1, $> 10$ millions d'articles, Pièce 3 § 4.3). C'est vrai uniquement pour reproduire le graphe mondial d'optique de Gu et Krenn (92 millions d'articles, Pièce 3 § 0). Mais pour le **substitut en contrôle de l'IA**, le dossier factuel établit que `session-depot` a **déjà** moissonné les 5 sous-domaines pertinents (`donnees/moisson-openalex-v1/`, $197\,681$ œuvres, **VÉRIFIÉ**, Pièce 1 § 2), et que cette moisson « doit servir de source au substitut de Gu et Krenn (S31) » (**VÉRIFIÉ**, Pièce 1 § 2). Ce qui manque à ces $197\,681$ œuvres, ce sont uniquement `abstract_inverted_index` et `counts_by_year` (**VÉRIFIÉ**, Pièce 3 § 4.1). Requêter ces deux champs sur les $197\,681$ identifiants déjà listés est borné exactement à $197\,681$ œuvres. J'accepte en revanche d'inclure un contrôle de complétude (comparer le compte par année de `moisson-openalex-v1` à une requête `group_by=publication_year` sur les 5 sous-domaines).
8. **Repli sur le substitut S31 non falsifié par E1 (Critique A) :**
   - **Statut : Acceptée.**
   - *Correction :* Le score du substitut S31 (part des paires de concepts jamais reliées et actives $\ge 5$ œuvres/3 ans, Pièce 1 § 7.2) est évalué comme un bras explicite dans E1 face à RA et Simpson. S'il ne bat pas RA, il est abandonné comme les autres.

## 4. Sur l'expérience E2 (Boucle multi-tours vs 1 coup) et les tests de mort

9. **Facteurs confondus dans E2 : sélection du meilleur tiers (8 sur 24) dans $H_B$ contre absence de sélection (8 sur 8) dans $H_A$, et absence de bras « réécriture sans moisson » (Critiques A, B, D) :**
   - **Statut : Acceptée.**
   - *Correction :* La critique de A, B et D est imparable : comparer le top-8 de 24 fiches à 8 fiches non triées confond l'effet de tri des juges et l'effet d'itération. E2 est refondue en un **protocole apparié intra-fiche sans biais de sélection**, sur les mêmes $N = 16$ embryons initiaux (*illustratif*), avec quatre trajectoires par embryon : (1) 1 tour de moisson v47, (2) 3 tours de moisson ciblée, (3) 3 tours de moisson placebo/croisée (résumés d'une autre fiche), et (4) 3 tours de réécriture libre sans moisson.
10. **Issue « survie aux tests de mort » non disponible ou « sans dents » (0/20 en couche 1) et « prise idéation » non construite (Critiques A, D) :**
    - **Statut : Acceptée comme préalable bloquant (Porte 0).**
    - *Correction :* Dans l'orchestrateur v48–v56, les tests de mort de la course n'utilisent pas la « prise idéation » du pôle mais un **agent expérimentateur qui écrit et demande au noyau d'exécuter un script en bac `bwrap` (3 exécutions de 120 s max, lecture mécanique de `RESULTAT:`)** (**VÉRIFIÉ**, Pièce 1 § 9.2). Cependant, cet étage n'a **jamais été activé** (**VÉRIFIÉ**, Pièce 1 § 9.2) et la couche 1 a donné $0/20$ (**VÉRIFIÉ**, Pièce 1 § 9.4.A). Je place donc la calibration de l'étage de tests de mort sur témoins vrais et faux non tautologiques en **Porte 0 bloquante** avant toute exécution de E2, et je sépare l'issue « script non concluant / erreur d'exécution » de l'issue « hypothèse éliminée par le seuil » (comme exigé par D).

## 5. Sur l'expérience E3 (Appariement Fiche–Article pour le bras méta)

11. **Contradiction entre le pré-filtre par Allocation de Ressources (qui maximise les voisins communs) et le bras méta (qui cherche des niches qui communiquent peu) (Critique A) :**
    - **Statut : Acceptée.**
    - *Correction :* Utiliser RA pour pré-filtrer les articles destinés au bras méta détruit le profil « trou entre niches qui communiquent peu ». Le pré-filtre mécanique pour le bras méta doit sélectionner des articles d'un **autre sous-domaine OpenAlex** (canal faible) partageant au moins un mot-clé de **structure méthodologique** (les 20 structures de l'annexe brouillon 4, Pièce 1 § 7.3) dans leur titre/résumé, et ayant un score RA **faible ou nul** avec les concepts de domaine de la fiche.
12. **Victoire combinatoire vraie par construction sur le taux de « sans-repli » ($6 \to 20$ objets fait passer les paires de 15 à 190, donnant $\approx 98\ \%$ par pur volume), asymétrie d'étiquetage et risque de plagiat (Critiques A, B, D) :**
    - **Statut : Acceptée.**
    - *Correction :* (i) Le critère « taux de déclenchement sans repli $\ge 7/8$ » est retiré comme critère de victoire de $H_A$, et remplacé par une comparaison à **taille de vivier exactement égale ($m = 20$)** contre deux contrôles négatifs : ajout de 14 articles tirés au hasard dans les 5 sous-domaines (contrôle combinatoire de A et D) et ajout de 14 articles dont les fiches sources sont permutées (contrôle de D) ; (ii) les étiquettes des 14 articles pré-filtrés sont posées par les **mêmes deux lecteurs neufs** que les fiches (coût négligeable : $14 \times 2 = 28$ appels courts par sous-session, éliminant le biais d'étiqueteur signalé par A) ; (iii) ajout d'un **filtre mécanique anti-plagiat** (rejet de toute fusion dont la distance de Jaccard en 3-grammes ou le recouvrement des prédictions chiffrées avec le résumé de l'article apparié dépasse un seuil gelé, contrôle demandé par B).

---

# (b) Les expériences corrigées (Inférence forte : $H_A$ contre $H_B$)

## Porte 0 (Préalable bloquant à E2) — Calibration à blanc de l'étage de Tests de mort (v56 `bwrap`)
- **Condition d'ouverture :** Avant d'utiliser la survie aux tests de mort comme issue de E2, l'étage 10 (`bwrap`, 3 essais de 120 s, lecture mécanique de `RESULTAT:`, Pièce 1 § 9.2) est exécuté sur **10 fiches témoins vraies** (lois/statistiques connues pour franchir le seuil sur les données de la liste D) et **10 fiches témoins fausses** (effets nuls ou signes inversés), rédigées au format exact du texte I (**VÉRIFIÉ**, Pièce 1 § 3.2), hors monde tautologique.
- **Critère de passage gelé :** (1) Taux de survie des témoins faux $\le 1/10$ ; (2) Taux de survie des témoins vrais $\ge 7/10$ (*illustratif*) ; (3) Taux de verdict « non concluant » (échec du script dans les 3 essais de 120 s ou désaccord lecteur neuf / lecture mécanique) $\le 2/20$ (*illustratif*). Tant que cette porte n'est pas franchie, aucune boucle n'est évaluée sur la survie (seule E1 tourne).

---

## Expérience E1 corrigée — Rétrodiction algorithmique factorielle ($2 \times 4$) : Vocabulaire (RAKE vs OpenAlex) $\times$ Moteur (Gu-Krenn 141 traits vs Substitut S31 vs Allocation de Ressources RA vs Simpson)
- **Objectif :** Trancher sans aucune fuite de LLM (1) quel vocabulaire et (2) quel moteur de classement prédisent le mieux les ponts à fort impact en contrôle de l'IA.
- **Protocole sans fuite :**
  1. Corpus : les $197\,681$ œuvres de `donnees/moisson-openalex-v1/` complétées de leurs résumés et `counts_by_year`. Découpage strict : entraînement sur graphe $y_1 = 2020 \to$ cible $2021\text{–}2022$ ; évaluation hors échantillon sur graphe $y_2 = 2022 \to$ cible $2023\text{–}2025$ (fenêtre complète de 3 ans, comme identifié en Pièce 3 § 4.2, **VÉRIFIÉ**).
  2. **Facteur 1 (Vocabulaire, calculé uniquement sur œuvres $\le y_1$ puis $\le y_2$) :** $V_{\text{RAKE}}$ (chaîne `create_concepts/` de Gu-Krenn, seuils 9 et 6) contre $V_{\text{OA}}$ (`concepts`/`topics` natifs d'OpenAlex portés par $\ge 20$ œuvres avant coupure).
  3. **Facteur 2 (Moteur de score) :** $M_{\text{GK}}$ (réseau 3 couches de 600 + XGBoost du banc sur les 141 traits normalisés sur le graphe entier d'avant-coupure `get_norm_features`, 5 graines) contre $M_{\text{S31}}$ (score du substitut S31) contre $M_{\text{RA}}$ (Allocation de Ressources de la Pièce 2) contre $M_{\text{Simp}}$ (indice de Simpson seul à l'année $y$, meilleur trait individuel de Gu-Krenn, Pièce 3 § 0).
  4. **Double estimand (correction D) :** Évaluation sur (a) un échantillon aléatoire de $1\,000\,000$ de paires non reliées à $y_2$ (estimand du vivier réel) et (b) un échantillon **apparié exactement par classes de degré $(\deg u, \deg v)$ et d'âge $(\text{âge } u, \text{âge } v)$** à $y_2$ (Pièce 3 § 4.4, **VÉRIFIÉ**), cible = apparition en $2023\text{–}2025$ avec $\ge \text{IR}$ citations ($\text{IR} \in \{1, 10\}$).
- **Contrôles négatifs fatals :**
  - Essai de non-fuite temporelle bit-à-bit de `essais_v1.py` (permutation/suppression des œuvres post-$y_2$ avant calcul des traits $\implies$ scores identiques à $10^{-15}$ près, **VÉRIFIÉ**, Pièce 2).
  - Permutation des issues **à l'intérieur des strates degré–âge** (doit ramener tous les moteurs à $\text{AUC} = 0,50$ et au taux de base de la strate).
  - Fenêtre placebo antérieure ($2018 \to 2019\text{–}2020$) pour vérifier la stabilité de l'ordre des méthodes (tau de Kendall) et remplacer le seuil absolu par un **seuil relatif au taux de base $\pi$** (correction du point mal posé n° 3 de la Pièce 2).
- **Hypothèses exclusives et seuils gelés (avec correction de Holm-Bonferroni sur les comparaisons) :**
  - $H_A$ *(Valeur ajoutée de Gu-Krenn ou S31 sur la topologie locale)* : Sur l'échantillon apparié degré–âge, $M_{\text{GK}}$ (moyenne sur 5 graines) ou $M_{\text{S31}}$ bat le meilleur de $\{M_{\text{RA}}, M_{\text{Simp}}\}$ d'au moins $\Delta \text{AUC} \ge +0,02$ ET d'un gain relatif de précision en tête $P@1000 / P@1000_{\text{baseline}} \ge 1,15$ (*illustratif*), intervalle de confiance à $95\ \%$ par bootstrap en blocs (blocs par sommets) excluant zéro.
  - $H_B$ *(Suffisance des prédicteurs locaux gratuits)* : Ni $M_{\text{GK}}$ ni $M_{\text{S31}}$ ne franchissent ce seuil face à $M_{\text{RA}}$ et $M_{\text{Simp}}$.
- **Ce que chaque issue falsifie :**
  - Si $H_A$ est réfutée $\implies$ on falsifie l'utilité d'entraîner les 141 traits et le substitut S31 en contrôle de l'IA ; le moteur d'appariement de la boucle devient **RA + Simpson** sur le vocabulaire gagnant ($V_{\text{RAKE}}$ ou $V_{\text{OA}}$), pour un coût de calcul quasi nul.
  - Si $H_B$ est réfutée $\implies$ on falsifie la suffisance de la topologie à 2 sauts ; le couple $(V^*, M^*)$ gagnant est figé pour la course 2.

---

## Expérience E2 corrigée — Protocole intra-fiche à 4 bras (isolation pure de la moisson ciblée et de l'itération, sans biais de sélection)
- **Objectif :** Mesurer si 3 tours de boucle avec moisson ciblée améliorent la même fiche initiale au-delà de (a) un seul tour de moisson, (b) 3 tours de réécriture sans moisson, et (c) 3 tours avec moisson croisée/placebo.
- **Protocole apparié (éliminant la confondante de sélection identifiée par A, B et D) :**
  - Matériau de départ : $N = 16$ fiches de passe 1 (8 Kimi, 8 Argon, couvrant les axes 1 à 5, *illustratif*) ayant passé l'aiguilleur. **Aucune sélection par les juges n'est appliquée entre les bras** : chaque fiche initiale $F_i$ ($i \in \{1..16\}$) est clonée dans **4 bras parallèles indépendants** (arbre en éventail depuis la même racine $F_i$) :
    1. **Bras $T_1$ (Moisson 1-coup, baseline v47) :** 1 tour de moisson ciblée $\to V_1$.
    2. **Bras $T_3^{\text{ciblé}}$ (Boucle complète, $H_A$) :** 3 tours `(moisson ciblée -> affinage sous garde Q1 corrigée)` $\to V_3^{\text{ciblé}}$.
    3. **Bras $T_3^{\text{vide}}$ (Contrôle auto-critique sans moisson, critique B/D) :** 3 tours de réécriture/affinage avec la même consigne et le même budget de jetons, mais **sans aucun résumé servi** $\to V_3^{\text{vide}}$.
    4. **Bras $T_3^{\text{croisé}}$ (Contrôle volume de texte / moisson croisée, critique D) :** 3 tours où la fiche $F_i$ reçoit exactement les résumés moissonnés pour une autre fiche $F_j$ d'un autre axe (même nombre et même longueur de résumés) $\to V_3^{\text{croisé}}$.
- **Mesures d'issues (séparées et en aveugle du bras et du tour) :**
  - **Issue Primaire 1 (Fermeture de trou et non-antériorité, étage 9) :** Le vérificateur Claude sur PDF (R7), **en aveugle des 4 versions de $F_i$**, évalue : (a) si la fiche est tuée par une antériorité préexistante, (b) si le `TROU_REQUETE` initial est effectivement fermé par une référence exacte et pertinente (contrôle négatif : y glisser 8 versions artificiellement dégradées où la référence ajoutée est hors sujet mais partage un mot du titre).
  - **Issue Primaire 2 (Survie mécanique aux tests de mort, étage 10, après Porte 0) :** Sur le sous-ensemble des fiches des axes testables sur processeur/modèle 8B, exécution en bac `bwrap`. Trois états enregistrés séparément : `Survit`, `Éliminée (seuil non atteint)`, `Non concluant (erreur de script)`.
- **Hypothèses exclusives (tests de McNemar / Wilcoxon appariés sur les $N=16$ quadruplets) :**
  - $H_A$ *(Apport propre de la boucle de moisson ciblée)* : $T_3^{\text{ciblé}}$ surpasse **simultanément** $T_1$, $T_3^{\text{vide}}$ et $T_3^{\text{croisé}}$ d'au moins $+25$ points de pourcentage (soit $\ge +4$ fiches sur 16 en différences appariées, *illustratif*) sur le taux de fiches `(Trou fermé vérifié sur PDF ∧ Non tuée par antériorité ∧ Survit au test de mort ou non-régression de la signature prédictive)`.
  - $H_B$ *(Illusion de l'itération ou de la moisson)* : $T_3^{\text{ciblé}}$ ne dépasse pas $T_1$ (1 tour suffit), OU ne dépasse pas $T_3^{\text{vide}}$ (le gain vient de la seule réécriture par le LLM), OU ne dépasse pas $T_3^{\text{croisé}}$ (le gain vient de l'allongement du contexte).
- **Ce que chaque issue falsifie :**
  - Si $T_3^{\text{ciblé}} \le T_3^{\text{vide}}$ $\implies$ on falsifie l'utilité de la moisson dans l'affinage.
  - Si $T_3^{\text{ciblé}} > T_3^{\text{vide}}$ mais $T_3^{\text{ciblé}} \le T_1$ $\implies$ on falsifie l'utilité de boucler sur plusieurs tours (on garde 1 seul tour v47).
  - Si $H_A$ tient sur les 3 comparaisons $\implies$ la boucle à 3 tours est validée.

---

## Expérience E3 corrigée — Appariement Fiche–Article vs Fiche–Fiche à taille de vivier constante et pré-filtre orthogonal au canal
- **Objectif :** Tester si l'appariement d'une fiche avec un article moissonné (pré-filtré pour partager une structure méthodologique mais dans une niche distante) produit de meilleures fusions sans noyer les fiches ni induire de plagiat.
- **Protocole corrigé (répondant aux critiques A, B et D) :**
  - Pour chaque lot de 6 fiches d'une sous-session, on compare **à taille de vivier identique ($m = 20$ objets, 190 paires)** trois viviers soumis au bras méta et au bras Gu-Krenn/RA :
    1. **Vivier $V_{\text{struct}}$ ($H_A$) :** Les 6 fiches + 14 articles de `moisson-openalex-v1` sélectionnés mécaniquement par : (i) sous-domaine différent de celui de la fiche (canal $\le 1$), (ii) score RA nul sur les termes d'objet (pas de voisinage banal), (iii) présence d'au moins un terme des 20 structures méthodologiques (Pièce 1 § 7.3) dans le titre/résumé.
    2. **Vivier $V_{\text{perm}}$ (Contrôle négatif combinatoire, critiques A/D) :** Les 6 fiches + 14 articles sélectionnés pour une *autre* sous-session (permutés) ou tirés au hasard dans les 5 sous-domaines.
    3. **Vivier $V_{\text{fiches}}$ ($H_B$, fiche–fiche pur à vivier élargi) :** Regroupement des fiches de plusieurs passes/axes jusqu'à $m = 20$ fiches (sans aucun article externe).
  - **Uniformisation de l'étiquetage (critique A) :** Les deux lecteurs neufs d'étiquettes (concepts, niches, structures) lisent à l'aveugle des extraits normalisés de même longueur (titre + résumé structuré de $1\,500$ caractères, *illustratif*) pour les fiches comme pour les 14 articles.
  - **Garde anti-plagiat mécanique (critique B) :** Avant tout passage devant les juges, l'analyseur programmé (étage 1) calcule le Jaccard des 3-grammes entre la fusion produite par Kimi et le résumé de l'article parent, et vérifie que la prédiction chiffrée et le critère de mort ne sont pas recopiés de l'article.
- **Hypothèses exclusives :**
  - $H_A$ *(Fertilité spécifique de l'appariement Fiche–Article structuré)* : (1) Le taux de paires au profil « trou à structure commune » dans $V_{\text{struct}}$ dépasse strictement celui de $V_{\text{perm}}$ d'au moins $+20$ points de pourcentage (*illustratif*, réfutant l'effet purement combinatoire de passer de 6 à 20 objets) ; ET (2) les fusions Fiche–Article issues de $V_{\text{struct}}$ ont un taux de `(Conforme étage 1 anti-plagiat ∧ Trou fermé / Inédite à l'étage 9)` strictement supérieur de $+15$ points (*illustratif*) à celui de $V_{\text{perm}}$ et non inférieur à $V_{\text{fiches}}$.
  - $H_B$ *(Effet purement combinatoire ou dilution/plagiat)* : $V_{\text{struct}}$ ne génère pas plus de paires au profil que le hasard $V_{\text{perm}}$, ou ses fusions échouent davantage au filtre anti-plagiat / antériorité que les fusions Fiche–Fiche ($V_{\text{fiches}}$).

---

# (c) Réponse à la question de l'arbitre en une page

## 1. Ce qui est établi par les faits servis (VÉRIFIÉ)
1. **Goulot d'étranglement actuel de l'organisme :** Dans la course d'idéation (courses 1 et 2), **tout est jugement ou contrôle de forme** ; les juges-modèles ne notent que la cohérence entre champs (accord de rang $0,12$ en course 1), aucune fiche de la course 1 n'est devenue une expérience, le pont « prise idéation » n'est pas construit, et l'étage de **tests de mort** (v48–v56, bac à sable `bwrap` sur machine jetable) est **codé mais n'a jamais été activé** (Pièce 1 § 1.1, § 9.2, § 9.4.B, § 10).
2. **Moteurs de découverte bibliographique :** Sur la rétrodiction arXiv ($2003\text{–}2010 \to 2011\text{–}2016$), la marche de Swanson (S) est **battue par l'Allocation de Ressources (RA)** en précision en tête ($10,65\ \%$ contre $9,83\ \%$ à $10\,000$ ; $28,40\ \%$ contre $19,20\ \%$ à $1\,000$), et RA a été adoptée par la règle préenregistrée D2 (Pièce 2).
3. **État de Gu et Krenn (2024) :** Aucun poids de modèle n'est publié ; leur liste de $37\,960$ concepts d'optique/quantique a une couverture nulle des concepts clés du contrôle de l'IA (et contient des homonymes trompeurs de physique comme `probe`, `alignment`, `control`) ; la moisson `donnees/moisson-openalex-v1/` ($197\,681$ œuvres en 5 sous-domaines) n'a ni les résumés (`abstract_inverted_index`) ni les citations annuelles (`counts_by_year`) nécessaires à leur graphe (Pièce 3 § 0, § 3, § 4.1, § 5).
4. **Mémoire et redites :** La distance textuelle (Jaccard) manque $100\ \%$ des paraphrases à $5\ \%$ de fausses fusions, alors que la signature prédictive brute tombe à $0\ \%$ de redites manquées (Pièce 4a). Lire la mémoire double les découvertes ($24,0$ contre $12,8$) **si et seulement si** les vraies associations se regroupent dans l'espace de proximité du proposeur ; sinon le gain tombe à zéro hors évitement des redites (Pièce 4b).

## 2. Ce qui n'est pas établi (HYPOTHÈSES à trancher, et pièges fermés par ce tour)
1. **Qu'affiner une fiche sur plusieurs tours de moisson améliore sa validité empirique :** Sans exécution de code (tests de mort), l'affinage itératif risque de ne produire qu'une inflation rhétorique ou un sur-ajustement aux résumés moissonnés.
2. **Qu'une rétrodiction avec un LLM proposeur (Kimi, Argon, Opus) soit valide :** Tout modèle entraîné après la date de coupure (2022 ou 2023) contamine la rétrodiction par ses poids. **Règle retenue :** la rétrodiction à date de coupure doit être **strictement algorithmique** (sans LLM) pour tester la moisson et les bras d'appariement ; l'évaluation de la boucle avec LLM doit être **prospective** (survie aux tests de mort et vérification d'antériorité sur PDF).
3. **Que Gu-Krenn (ou son substitut S31) batte RA ou Simpson en contrôle de l'IA :** Dans un champ jeune au graphe plus petit, il n'est pas établi qu'un réseau à 141 traits batte l'Allocation de Ressources (RA) ou l'indice de Simpson seul ($\text{AUC} = 0,8880$ chez Gu-Krenn), surtout une fois apparié sur le degré et l'âge des concepts.
4. **Architecture retenue pour la boucle (Q1–Q7) :**
   - *Objet et arrêt (Q1) :* Plafond dur à 2 tours ; progrès reconnu uniquement si un trou déclaré est fermé par un nouvel identifiant vérifié par lecteur neuf aveugle (jamais sur simple modification numérique ou lexicale).
   - *Appariement (Q3) :* **Interdire les paires article–article en course** (qui noieraient les fiches à $99,99\ \%$ et relèvent du calcul de graphe en amont) ; quota séparé fiche–fiche et fiche–article, avec pré-filtre structurel (canal bas, structure commune, RA nul) et filtre anti-plagiat à l'étage 1.
   - *Allocation (Q4) :* **Allocation uniforme (1 tour) avec arrêt sec**, refus du bandit au gain de nouveauté (vulnérable à la loi de Goodhart tant que la récompense n'est pas un test par calcul).
   - *Ordre (Q7) :* **Lancer le pré-pilote et la génération 1 de la course 2 d'abord** (avec 1 seul tour de moisson v47 déjà codé), **activer et calibrer les tests de mort (v56) entre G1 et G2**, et n'introduire la boucle multi-tours qu'en génération 2 si elle bat le 1-coup.

## 3. L'expérience à faire en premier (immédiate, 0 jeton LLM, ~1 USD)
**Lancer en parallèle la Porte 0 (calibration à blanc des tests de mort v56 sur 10 témoins vrais et 10 faux) et l'Expérience E1 corrigée (rétrodiction algorithmique sur les $197\,681$ œuvres des 5 sous-domaines) :**
1. Tirer depuis OpenAlex les résumés et `counts_by_year` manquants des $197\,681$ identifiants de `donnees/moisson-openalex-v1/` ($\approx 3\,954$ pages de filtre, $0,40\text{ USD}$ pris sur l'allocation quotidienne gratuite de $1\text{ USD}$).
2. Exécuter tel quel (décision de Lazar du 1er novembre) le script `create_concepts/` (RAKE) et le calcul des traits du dépôt cloné `Impact4Cast` strictement avant coupure ($y_2 = 2022$, cible $2023\text{–}2025$), et confronter en plan factoriel **Vocabulaire (RAKE vs OpenAlex natif) $\times$ Moteur (Gu-Krenn vs Substitut S31 vs Allocation de Ressources RA vs Simpson)** sur échantillon apparié en degré et âge.
3. En une demi-journée sur machine CPU louée ($\approx 1\text{ à }2\text{ USD}$, *illustratif*), cette expérience tranche quel moteur d'appariement et quel vocabulaire mettre dans l'orchestrateur avant même de dépenser un seul dollar de jetons LLM dans la boucle.

FIN-DE-CELLULE