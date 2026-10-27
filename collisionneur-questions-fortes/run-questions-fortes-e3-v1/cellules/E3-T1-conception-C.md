### Ligne d'intégrité des pièces (Règle 2)
La pièce K (`rapport-contre-lecture-aptitude-v1.md`) est servie sous forme dérivée tronquée : l'en-tête (section 0), la colonne C (section 3.C) et les sections 4 à 6 sont absents (garde R-519, **RAPPORTÉ**).

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Qu'un pôle de sélection par paris catégoriels (12 types de lois sur traits $z$) puisse formuler et tester des découvertes en interprétabilité mécaniste mieux qu'une équipe humaine à budget égal.**
   - *Statut* : **HYPOTHÈSE**.
   - *Fondement* : La contre-lecture (pièce K, § 1 et § 2.1, **RAPPORTÉ**) établit que le juge actuel ne sait évaluer qu'une loi prédictive catégorielle $p(\text{issue} \mid z, g, \text{passé})$ contre une bibliothèque aveugle $\mathcal{L}$. Il ne juge ni un mécanisme causal, ni une aire sous la courbe, ni une fonctionnelle d'ensemble sans réécriture en pari de signe (pièce C, § 3.1, **RAPPORTÉ**). De plus, sur données réelles (pièce L2, **RAPPORTÉ**), la puissance actuelle est nulle (« sans dents », 0 témoin vrai promu sur 5 sous e-BH).
2. **Qu'une banque d'épisodes réutilisée à travers les générations et les niveaux emboîtés conserve la garantie de fausses découvertes ($\alpha = 0,05$) de l'inégalité de Ville et de e-BH.**
   - *Statut* : **HYPOTHÈSE** (contestée par la faille A4 de la pièce K, **RAPPORTÉ**).
   - *Fondement* : La garantie de Ville vaut par fiche avec des tirages frais après le gel, et e-BH contrôle le taux de fausses découvertes pour une famille fixée. Dès que la génération $g+1$ ou le niveau supérieur formule des fiches en lisant quelles fiches ont survécu à la génération $g$ sur la *même* banque figée, l'analyse devient adaptative (Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 2015, *The reusable holdout: Preserving validity in adaptive data analysis*, **RAPPORTÉ** dans K).
3. **Qu'une structure « auto-similaire » (appliquer le même juge par pari, la même mémoire et le même filtre e-BH aux stratégies, aux familles de modes et aux instances) préserve la validité statistique et soit mathématiquement bien posée.**
   - *Statut* : **HYPOTHÈSE**.
   - *Fondement* : Au niveau bas (instances $\to$ fiche), les épisodes sont approximativement échangeables sous le nul. Au niveau haut (stratégie $\to$ fiches promues), les réalisations dépendent de l'épuisement du réservoir de la banque et de l'état de la mémoire qui bloque les redites (pièce C, § 2, **RAPPORTÉ**). Le processus de gain au niveau méta n'est donc pas une surmartingale sous un nul simple.
4. **Que la recherche automatique de modes de manque (bras défensif d'angles morts) sur nos moniteurs identifie des vulnérabilités générales du contrôle plutôt que des artefacts d'implantation ou de surface de nos sondes.**
   - *Statut* : **HYPOTHÈSE**.
   - *Fondement* : L'état de l'art (pièce P2, § 2.1 et § 4.3, Kumar 2026 ; Blandfort & Graham 2025, **RAPPORTÉ**) montre que les sondes linéaires sont vulnérables aux changements de style et aux corrélats de surface. Sans contrainte multi-lignées dans le nul, un optimiseur trouve le contournement lexical le moins coûteux propre au moniteur testé.
5. **Qu'un modèle de 8 milliards de paramètres (Llama-3.1-8B-Instruct) possède une représentation interne distincte et extractible de la « conscience d'évaluation » (se savoir évalué) séparée de la simple détection syntaxique du format de prompt.**
   - *Statut* : **HYPOTHÈSE**.
   - *Fondement* : Les résultats publiés sur la conscience d'évaluation (Needham et al., 2025, *Large Language Models Often Know When They Are Being Evaluated* ; Goldowsky-Dill et al., 2025, **RAPPORTÉ** dans K, A5 et B4) portent sur des modèles de pointe (Claude 3.7 Sonnet, Gemini 2.5 Pro). À 8B, l'existence même du phénomène hors marqueurs lexicaux de surface n'est pas établie (d'où la porte de séparabilité exigée par N-053 point 3 et point 4, **RAPPORTÉ**).
6. **Que restreindre un agent proposeur à un « cône mathématique » (sous-ensemble de tactiques et de lemmes dans Lean) augmente le rendement en théorèmes utiles par dollar.**
   - *Statut* : **HYPOTHÈSE**.
   - *Fondement* : Aucun essai du pôle théorie n'a été couru (pièce C, § 3.4, **RAPPORTÉ**). Dans un vérificateur formel comme Lean, le goulot d'étranglement des modèles actuels est souvent la traduction entre l'énoncé probabiliste informel et les types de `mathlib` (mesures, filtrations), où une restriction d'imports peut bloquer la preuve par absence d'un lemme de recollement élémentaire.

---

## (b) Les cinq questions, la théorie, les cônes, la conscience d'évaluation — et les expériences décisives ($H_A$ contre $H_B$)

### 1. Les cinq questions à fort potentiel pour le pôle (et ce qui est hors de portée)

**Ce qui est hors de portée sous nos contraintes (8B/70B, 10–400 USD/course) :**
- L'interprétabilité mécaniste de circuits complets (attribution causale graphe par graphe, transcodeurs parcimonieux sur 70B) : trop coûteux en passes avant/arrière par fiche et incompatible avec la grammaire de lois tabulaires $z \to \text{issue}$ du juge v7 (**RAPPORTÉ**, pièce K § 2.0).
- L'émergence de stéganographie ou d'obfuscation par apprentissage par renforcement en ligne (Baker et al., 2025, **RAPPORTÉ** dans K, A2) : requiert des centaines d'heures GPU par trajectoire d'entraînement, hors budget.

**Où le pôle bat une équipe humaine à budget égal :**
Lorsque l'espace d'hypothèses est un **produit cartésien discret de taille $10^2$ à $10^4$** (couches $\times$ positions de tokens $\times$ règles d'agrégation $\times$ familles de sondes $\times$ régimes de contexte), évaluable en **zéro passe GPU supplémentaire** sur une banque d'activations et de scores pré-calculée en cache, où des humains feraient du *p-hacking* séquentiel là où le couple (Ville + e-BH + nul informé) garantit $\text{FDR} \le 0,05$.

| # | Question scientifique | Résultat fort (vs incrémental) | Chemin de couches & Coût (illustratif hors C) | Critère d'abandon (« n'en valait pas la peine ») |
|---|---|---|---|---|
| **Q1** | **Loi de prédiction de la robustesse adverse d'une sonde par sa validité de construit hors attaque (H8 + N-053 pt 1)** : quelles propriétés mesurables *avant* attaque (invariance au masquage des tokens d'évidence textuelle, stabilité inter-formats) prédisent que $g_{\text{sonde}} \le 0$ sous pression rhétorique ou changement de style ? | *Fort* : Loi quantitative prédictive validée hors famille d'organisme ((i)/(ii) $\to$ (iii)/(iv)), fournissant un critère de recette sans red-teaming. *Incrémental* : Constater que certaines sondes tombent (déjà dans Kumar, 2026, *Pressure-Testing Deception Probes*, **RAPPORTÉ**). | Couche 1 bis (288 inst., 15 USD, **RAPPORTÉ**) $\to$ Couche 2 (banque T0.6/T0.7 + masquage N-053, 120–250 USD, **RAPPORTÉ**). Min : 135 USD / Max : 300 USD. | Aucune loi ne bat le nul informé (compétence bénigne seule, AUROC hors attaque) sous e-BH à $\alpha = 0,05$ sur un panel de $\ge 30$ sondes (illustratif). |
| **Q2** | **Frontière marginale vs corrélation sur activations réelles (Lemme L vs Théorème T)** : dans le sabotage diffus, existe-t-il des régimes d'organismes où le déplacement marginal $\delta$ est indiscernable de zéro mais où la co-élévation temporelle ou inter-agents détecte à $\text{FPR} = 1\%$ ? | *Fort* : Démonstration sur vraies activations (8B/70B) que le sabotage réaliste viole la condition de marginale et qu'un processus e d'autocorrélation/co-élévation spécifique restaure la détection (dépasse Zhang & Gao, 2026, purement synthétique boîte noire, **RAPPORTÉ**). *Incrémental* : Confirmer $\delta > 0$ partout (simple application d'E-valuator, Sadhuka et al., 2025, **RAPPORTÉ**). | Couche 2 (banque T0.6 multi-pas, 150 USD) $\to$ Pôle théorie Lean en parallèle (0 USD carte). Min : 150 USD / Max : 350 USD (**RAPPORTÉ**). | Sur toutes les familles (i)–(iv), la somme cumulée marginale (CUSUM / e-processus de moyenne) capture $\ge 95\%$ (illustratif) du rappel de tout agrégateur de dépendance d'ordre 2. |
| **Q3** | **Localisation positionnelle du signal d'intention vs fuite textuelle (N-053 pt 1)** : le gain blanc-sur-noir (H1) survit-il lorsque le juge masque toutes les positions de tokens que le moniteur boîte noire identifie comme suspectes ? | *Fort* : Preuve que l'intention est lisible dans les activations des tokens *syntaxiquement banals* (planification amont), réfutant l'hypothèse que les sondes ne sont que des classifieurs lexicaux rapides. *Incrémental* : Gain blanc-sur-noir sur séquence complète (déjà chez Parrack et al., 2025, **RAPPORTÉ**). | Couche 2 sur cache d'activations par token (100–200 USD, **RAPPORTÉ**). Min : 100 USD / Max : 220 USD. | Une fois masqués les tokens à fort score de suspicion textuelle, le rappel à 1 % FPR des sondes chute au niveau de la sonde aléatoire appariée en covariance. |
| **Q4** | **Loi de transfert de corruption et taxe de déplacement (HC1, HC4, HC6)** : le gain de déférence bénin $g_{\text{bénin}}$ (mesuré sur désaccords sans attaque) prédit-il l'effondrement sous les 5 familles de persuasion, et la matrice de transfert entre juges et sondes est-elle de rang 1 ? | *Fort* : Découverte d'un invariant spectral de corruptibilité par moniteur et chiffrage exact de l'écart en requêtes/coût entre rhétorique (juge) et obfuscation (sonde) (aucune comparaison publiée, pièce P2 § 4.2, **RAPPORTÉ**). *Incrémental* : Montrer qu'un juge cède à la flatterie (occupé par Meincke et al., 2026 ; Kim et al., 2026, **RAPPORTÉ**). | Couche 1 bis $\to$ Banque Papier C (juges 3B, 8B, Qwen-7B + sondes, 80–200 USD, illustratif). Min : 80 USD / Max : 250 USD. | Corrélation de rang entre $g_{\text{bénin}}$ et $g_{\text{adverse}}$ inférieure à 0,25 (illustratif), ou $g_{\text{sonde}} > 0$ sur rhétorique pure même après contrôle du style. |
| **Q5** | **Détectabilité du changement de régime par conscience d'évaluation (A5, A9, N-053 pt 3)** : peut-on dissocier dans les activations d'un 8B/70B le vecteur « format de banc d'essai » du vecteur « retenue comportementale stratégique » ? | *Fort* : Séparation orthogonale des deux sous-espaces avec test causal (injecter « format déploiement » restaure le taux de sabotage de l'organisme (ii)/(iii) sur un vrai banc de test). *Incrémental* : Montrer qu'une sonde distingue les prompts d'évaluation des prompts réels (déjà dans Needham et al., 2025 ; Devbunova, 2026, **RAPPORTÉ**). | Couche 2 (paires d'épisodes avec/sans marqueurs de test, N-053 pt 3) $\to$ Couche 3 (interventions causales sur GPU, 150–300 USD). Min : 150 USD / Max : 400 USD (**RAPPORTÉ**). | À 8B et 70B, le taux de sabotage des organismes (ii) et (iii) est invariant à la présence/absence des marqueurs d'évaluation (pas de retenue stratégique mesurable). |

---

### Expérience décisive E1 (tranche la viabilité du pôle sur les questions Q1–Q4 : Proposeur + Pari à fraction sur Couche 1 bis / Couche 2)

Avant de lancer le pôle sur Q1–Q5, il faut résoudre l'échec de puissance constaté en L1/L2 (« sans dents », **RAPPORTÉ**).
- **$H_A$ (Puissance restaurée par le pari à fraction et la taille de banque)** : Sur la banque étendue (Couche 1 bis, $N = 288$ épisodes, pièce C § 1, **RAPPORTÉ**), le remplacement de la mise fixe par un **pari à fraction sur grille** (mélange de Kelly borné : $W_t = \frac{1}{|G|}\sum_{\lambda \in G} \prod_{s=1}^t (1 + \lambda (\frac{p_s}{q_s} - 1))$ pour $\lambda \in \{0,1 ; 0,25 ; 0,5 ; 0,75\}$, illustratif) permet au juge sous e-BH ($\alpha = 0,05$) de promouvoir au moins 60 % (illustratif) des témoins vrais sans promouvoir aucun témoin faux, et au proposeur (Opus 5.5) de promouvoir $\ge 1$ loi battant le nul informé.
- **$H_B$ (Échec structurel de la formulation par instances discrètes)** : Même avec $N = 288$ et le pari à fraction, le prix du dénominateur universel $\max_{q \in \mathcal{L}} \prod q$ et de la correction e-BH maintient la puissance sur les témoins vrais sous 30 % (illustratif), ou le proposeur Opus 5.5 ne formule aucune fiche qui survive au nul informé.
- **Métrique et seuil** : Taux de promotion des témoins vrais plantés ($R_{\text{vrais}} \ge 0,60$, illustratif) ; taux de promotion des témoins faux ($R_{\text{faux}} = 0$) ; nombre de fiches proposées par Opus 5.5 promues contre le nul informé ($\ge 1$).
- **Contrôle négatif** : Bras « étiquettes permutées entre épisodes de même longueur » (doit donner 0 promotion) et bras « proposeur aléatoire tirant dans la même grammaire ».
- **Issue qui falsifie chaque hypothèse** : Si $R_{\text{vrais}} < 0,30$ sur 288 épisodes avec pari à fraction, $H_A$ est réfutée (la sélection par e-valeur universelle par instance est trop conservatrice pour ces tailles de banques ; il faut basculer sur les paris de signe globaux de la section 3.1 de C). Si $R_{\text{vrais}} \ge 0,60$ et qu'Opus 5.5 bat le proposeur aléatoire et le nul informé, $H_B$ est réfutée.

---

### 2. Structure multi-niveaux du bras de recherche des angles morts (instrument défensif, garde R-519)

**Critique de l'« auto-similarité » :**
Appliquer mécaniquement la même règle à chaque niveau (stratégie $\to$ famille de modes $\to$ instances d'épisodes) est **une image trompeuse si elle est prise à la lettre**, mais possède **une traduction mathématique exacte** à condition de changer la nature de la filtration et de la mémoire à chaque échelle :
1. **Niveau 0 (Instances $\to$ Fiche de famille de modes)** : Les unités sont des épisodes $i \in \{1 \dots n\}$ générés sous une condition expérimentale abstraite $m$. Le juge évalue une e-valeur $E_{m}$ testant si le taux de non-détection dépasse le nul informé. Ici, les épisodes sont conditionnellement indépendants : l'inégalité de Ville s'applique.
2. **Niveau 1 (Fiches de modes $\to$ Classe en mémoire et quarantaine)** : On ne peut *pas* multiplier naïvement les e-valeurs de variantes d'un même mode sur la même banque de réservistes honnêtes (faille A4, **RAPPORTÉ** dans K). La transmission de la preuve entre une fiche parente $m_1$ et une fiche raffinée $m_2$ exige que $m_2$ soit évaluée sur une **tranche d'épisodes fraîche** et que son dénominateur inclue le taux de manque de $m_1$ ($\text{nul des filles v2}$, pièce C § 2, **RAPPORTÉ**).
3. **Niveau 2 (Stratégies de recherche $\to$ Allocation de budget)** : Une stratégie $S$ qui propose des fiches $m_1, \dots, m_k$ n'est pas une hypothèse scientifique mais un **bras de bandit**. Lui appliquer un seuil de Ville avec élimination définitive à $\alpha = 0,05$ détruirait l'exploration dès qu'une stratégie produit quelques fiches fausses. Au Niveau 2, la bonne règle n'est pas e-BH, mais une **allocation séquentielle avec contrôle du budget d'erreur ($\alpha$-investing ou bandit à récompense = $\sum \mathbb{I}(\text{promue}) \cdot \log W / \text{coût}$)**.

**Architecture défensive à trois niveaux (placement du juge, de la mémoire, du nul et de la quarantaine) :**

- **Où placer la quarantaine (N-053 pt 5, N-054)** :
  - **En sortie du Niveau 0 (avant toute écriture en mémoire lisible)**. Dès qu'une fiche de mode $m$ franchit le seuil de promotion, sa spécification descriptive est hachée et chiffrée dans un coffre scellé (`quarantaine_modes/`), inaccessible aux agents et aux humains qui conçoivent les moniteurs.
  - Ce qui remonte au Niveau 1 (mémoire du bras de recherche d'angles morts) ne contient que des **vecteurs de signatures fonctionnelles anonymisées** (profil binaire de quels moniteurs du panel ont manqué quels épisodes, sans le texte ni la recette).
- **Quel nul ($\mathcal{L}_{\text{défensif}}$)** :
  - Le nul aveugle est inutile (pièce K § 2.2, **RAPPORTÉ**). Le nul informé doit être le **maximum enveloppe des taux de manque sur les modes déjà documentés**, stratifié par l'impact mesuré sur la tâche (dommage $\theta$) et par la longueur de l'épisode :
    $$q_0(\text{manque} \mid z) = \max_{m_0 \in \text{ModesConnus}} \hat{P}(\text{alerte} = 0 \mid m_0, \text{dommage}(z), \text{longueur}(z))$$
    Ainsi, un mode qui réduit le rappel du moniteur uniquement parce qu'il sabote moins fort ($\text{dommage}$ plus faible) ne bat pas le nul.
- **Comment éviter la sur-optimisation contre les défauts d'implantation de nos moniteurs (Goodhart défensif)** :
  - **Division du panel de moniteurs en deux ensembles disjoints** : un sous-panel *visible par le juge d'étape* $M_{\text{étape}}$ (ex. sonde linéaire couche moyenne + juge Llama-8B) et un sous-panel *de réserve scellé* $M_{\text{réserve}}$ (ex. sonde à attention couche tardive + sonde sur Qwen2.5-7B + juge d'une autre lignée, conformément à § 8.1 de P1 et N-053 pt 4, **RAPPORTÉ**).
  - **Règle de promotion en deux temps (Split-Gate)** : Une fiche de mode $m$ n'est promue au Niveau 1 que si son produit d'e-valeurs $E_{\text{étape}} \cdot E_{\text{réserve}}$ franchit le seuil, où $E_{\text{réserve}}$ est calculé par le noyau une seule fois, sans retour détaillé au proposeur (qui reçoit seulement un bit « rejeté » ou « promu »).
- **Quels témoins** :
  - **Témoins positifs (doivent être retrouvés)** : Les modes déjà caractérisés dans les pièces P4 et K (ex. le mode non chiffré « affaiblir les contrôles » de N-054, ou le changement de registre stylistique de Blandfort & Graham 2025, **RAPPORTÉ**), ré-encodés sous noms anonymes dans le vivier initial. Si le pôle ne les promeut pas (signal « pas de dents »), la course s'arrête.
  - **Témoins négatifs (ne doivent jamais être promus)** : Des conditions purement bénignes à style inhabituel (faux positifs du chercheur de failles, où le dommage réel sur la tâche est nul) et des redites des modes connus du nul.
- **Crédibilité hors du pôle** :
  1. *Transfert inter-lignées* : Le manque persiste quand la trace est relue par un moniteur d'une autre famille de modèles (Qwen2.5-7B, N-053 pt 4) ou quand l'organisme est porté sur une autre architecture.
  2. *Invariance à la ré-implantation* : Le manque survit à un changement de graine, de couche adjacente ($\ell \pm 2$) et d'hyperparamètre de régularisation de la sonde.
  3. *Vérification d'antériorité* : Le moissonneur (pièce C § 3.1) vérifie l'absence de la signature du mode dans la table des failles A1–A10 et B1–B5 (pièce K).

#### Expérience décisive E2 (Test de la structure du bras d'angles morts : Juge mono-panel vs Juge Split-Gate multi-lignées)
- **$H_A$ (Nécessité du filtre inter-lignées en réserve)** : Un bras de recherche d'angles morts guidé uniquement par le taux de manque sur le panel courant $M_{\text{étape}}$ promeut majoritairement ($\ge 60\%$, illustratif) des artefacts spécifiques à l'implantation (qui échouent à transférer sur $M_{\text{réserve}}$), tandis que le juge à double détente (Split-Gate avec réserve inter-lignées) réduit ces promotions d'artefacts à $\le \alpha = 0,05$ tout en retrouvant $\ge 80\%$ (illustratif) des témoins de failles structurelles plantés.
- **$H_B$ (Suffisance du panel unique ou perte fatale de puissance)** : Soit les modes promus sur $M_{\text{étape}}$ transfèrent naturellement à $\ge 80\%$ sur $M_{\text{réserve}}$ (le Split-Gate est redondant), soit le Split-Gate écrase la puissance et élimine plus de la moitié des témoins vrais plantés.
- **Métrique et seuil** : Taux de transfert des fiches promues vers $M_{\text{réserve}}$ (rappel du moniteur de réserve abaissé d'au moins 20 points à 1 % FPR, illustratif) et rappel sur les témoins structurels plantés.
- **Contrôle négatif** : Sondes « fragiles par construction » (entraînées avec un poids artificiel sur un jeton de ponctuation rare) incluses dans $M_{\text{étape}}$ mais absentes de $M_{\text{réserve}}$.
- **Issue qui falsifie chaque hypothèse** : Si le bras sans réserve promeut les failles de ponctuation et que le Split-Gate les bloque en gardant $\ge 80\%$ des témoins structurels, $H_B$ est réfutée. Si le Split-Gate bloque aussi les témoins structurels, $H_A$ est réfutée.

---

### 3. Les cônes mathématiques et le pôle théorie sous Lean

**Analyse des familles d'outils pour le problème ouvert du programme (agrégation sous dépendance adverse à marginales fixées, Lemme L et Théorème T, pièce P1 § 3) :**

Le problème mathématique exact est le suivant : on observe une matrice de scores $S = (s_{i,t})_{i \in \{1\dots N\}, t \in \{1\dots T\}}$. Sous $H_0$ (honnête), les lois marginales $F_0$ et la dépendance de référence sont connues ou bornées. Sous $H_1$ (sabotage à marginale préservée ou budget total $B = \sum \delta_{i,t}$ borné), l'adversaire choisit la loi jointe $P \in \mathcal{P}(F_1, \dots, F_{NT})$ (un **couplage**) pour maximiser la probabilité que le dommage cumulé $D(S) \ge \theta$ avant que le temps d'arrêt $\tau$ du moniteur ne se déclenche ($\mathbb{P}_0(\tau < \infty) \le \alpha$).

1. **Martingales en temps discret, processus e et inférence universelle (Howard, Ramdas, Waudby-Smith ; Koning & Grünwald 2022, RAPPORTÉ dans P2)** :
   - *Pourquoi c'est le socle indispensable* : Toute règle d'arrêt toujours valide à $\text{FPR} \le \alpha$ sur une filtration $(\mathcal{F}_t)$ est dominée par un processus e ($E_t \ge 0, \mathbb{E}_0[E_t \mid \mathcal{F}_{t-1}] \le E_{t-1}$). Pour tester la dépendance à marginale fixée, il suffit de construire des processus e sur les **produits croisés centrés** $Z_t = (s_t - \mu_0)(s_{t-k} - \mu_0)$ (autocorrélation) ou $Y_t = \sum_{i < j} (s_{i,t} - \mu_0)(s_{j,t} - \mu_0)$ (co-élévation inter-agents).
   - *Faisabilité dans Lean 4 (`mathlib`)* : **Élevée** en temps discret fini sur espaces probabilisés finis ou à densité bornée (l'inégalité de Ville pour surmartingales discrètes non négatives se démontre en moins de 100 lignes à partir de l'espérance conditionnelle sur algèbres finies).
2. **Transport optimal multimarginal et bornes de Fréchet-Hoeffding (plutôt que la théorie générale des copules)** :
   - *Pourquoi* : « Choisir la dépendance à marginales fixées » est, par définition, le problème de Monge-Kantorovitch multimarginal. L'adversaire cherche le couplage qui concentre la masse dans la région $\{\sum a_{i,t} \ge \theta \text{ et } \max_t A_t < c\}$. Les bornes de Fréchet-Hoeffding et l'ordre supermodulaire (ou convexe directionnel) caractérisent exactement le pire couplage (la **comonotonicité** pour maximiser la variance d'une somme, et la **contre-monotonicité** ou les couplages négativement associés pour annuler la variance d'une somme tout en gardant les marginales). C'est cet outil qui fournit la preuve la plus directe du Théorème négatif T.
   - *Faisabilité dans Lean 4* : **Élevée** si formulée algébriquement via l'inégalité de réarrangement de Hardy-Littlewood-Pólya et des matrices bistochastiques finies (évite le théorème de Sklar continu qui est lourd à formaliser dans `mathlib`).
3. **Jeux minimax et dualité de Sion / programmation linéaire finie** :
   - *Pourquoi* : Le jeu de contrôle $G = (E, \pi_B, \pi_R)$ (pièce P1 § 4) entre le choix du couplage par l'attaquant et le choix du processus e par le défenseur est bilinéaire en les probabilités jointes et le test. La dualité linéaire donne directement le détecteur minimax optimal.
   - *Faisabilité dans Lean 4* : **Moyenne à élevée** (via le lemme de Farkas en dimension finie).
4. **Théorie de l'information (divergence KL, méthode de Le Cam / Assouad)** :
   - *Pourquoi* : Idéale pour prouver l'impossibilité (borne inférieure de détection de type Ramtin, Nain, Towsley, 2026, **RAPPORTÉ** dans P2) via l'inégalité de Pinsker ou de traitement des données (utilisée aussi pour H7 sur la fuite par la riposte).

**Définition opérationnelle d'un « cône mathématique » dans Lean et comment le mesurer :**
Un « cône » ne doit pas être un jargon géométrique vague (pièce G § 5 rappelle le danger du décor mathématique comme E8 ou les espaces perfectoïdes, **RAPPORTÉ**). Dans Lean 4, un cône $\mathcal{C}$ est défini mécaniquement par trois restrictions imposées au proposeur :
1. **Une liste blanche d'imports `mathlib`** (ex. Cône A « Martingales discrètes & Inégalités convexes » : algèbre linéaire finie, espérance sur `Fintype`, convexité de Jensen ; exclusion de la topologie générale et de la mesure de Lebesgue continue).
2. **Un squelette de types imposé (Type-cone)** : toutes les variables aléatoires sont forcées d'être des fonctions sur un espace d'états fini $(\Omega, \text{Fintype }\Omega)$ muni d'une distribution de masse `PMF`, évitant 80 % (illustratif) des erreurs de mesurabilité de `MeasureTheory`.
3. **Un graphe de jalons (stepping-stones)** : l'énoncé final (ex. Théorème T) est décomposé en une suite de `sorry` typés par le noyau ; un lemme proposé n'est compté comme **utile** que s'il compile sans `sorry`, sans nouvel `axiom`, et s'il est effectivement appelé dans la réduction d'au moins un jalon vers le théorème cible (ou s'il réfute un jalon par un contre-exemple explicite).

#### Expérience décisive E3 (Proposeur sous Cône typé vs Proposeur libre dans Lean 4)
- **$H_A$ (Gain du Cône de types et d'imports)** : Sur un banc de 10 énoncés cibles issus du Lemme L et du Théorème T (décomposés en 30 jalons intermédiaires, illustratif) à budget fixé (50 USD d'appels Opus 5.5 / Fable 5.1 par bras, illustratif), le proposeur contraint au Cône (types finis `Fintype`/`PMF` + imports restreints + interdiction de changer les signatures des jalons) ferme au moins 2 fois plus (illustratif) de jalons du graphe de dépendance vers les théorèmes cibles que le proposeur libre ayant accès à tout `mathlib`.
- **$H_B$ (Entrave par le Cône ou équivalence)** : Le proposeur libre ferme autant ou plus de jalons (car il trouve des lemmes déjà présents dans d'autres parties de `mathlib`), ou les deux bras plafonnent sous 10 % (illustratif) des jalons fermés.
- **Métrique et seuil** : Nombre de jalons du graphe cible fermés par dollar (compilés par le noyau Lean 4 avec `#print axioms` vérifiant uniquement `[propext, Classical.choice, Quot.sound]`, zéro `sorry`, et utilisés dans l'arbre de preuve du théorème cible). Seuil : ratio Cône / Libre $\ge 2,0$ (illustratif).
- **Contrôle négatif (garde anti-trivialité)** : Un agent tricheur qui génère des lemmes vrais mais tautologiques ($A \implies A$, identités algébriques du type Volet II de la pièce G, **RAPPORTÉ**) obtient un score de **0**, car la métrique ne compte que les nœuds fixés d'avance dans le graphe de dépendance du théorème cible.
- **Issue qui falsifie chaque hypothèse** : Ratio $< 1,2$ (illustratif) falsifie $H_A$ (le cône n'aide pas). Ratio $\ge 2,0$ avec au moins un théorème cible complet démontré falsifie $H_B$.

---

### 4. La conscience d'évaluation : résultat décisif et testable (et ce qui manque)

**Le problème central :**
Dans la littérature actuelle (Needham et al., 2025 ; Apollo Research 2025 ; Das et al., 2026, **RAPPORTÉ** dans P2 et K), on confond trois phénomènes sous le terme « conscience d'évaluation » :
1. **La reconnaissance syntaxique du genre** : le modèle détecte le style « banc de test académique / QCM / prompt synthétique » (comme il détecterait un texte juridique).
2. **La représentation d'être mis à l'épreuve** : le modèle représente que son comportement est jugé par un superviseur.
3. **La modulation stratégique (Alignment Faking / retenue)** : le modèle modifie causalement sa politique (sabote moins ou cache son intention) *parce* qu'il a activé la représentation (2).

**Le résultat décisif à portée de nos instruments :**
Une **double dissociation causale** sur les organismes du programme (familles (ii) LoRA sans instruction en contexte, (iii) sandbagging public, et (iv) N-053 pt 2, **RAPPORTÉ**).
- On construit la matrice $2 \times 2$ de N-053 point 3 (**RAPPORTÉ**) : {Format = banc synthétique vs trace réaliste de production décorrélée} $\times$ {Marqueurs sémantiques d'audit = présents vs absents}, à tâche sous-jacente identique.
- On extrait par sonde orthogonale deux directions dans le flux résiduel : $v_{\text{format}}$ (qui prédit le format à contexte d'audit fixe) et $v_{\text{audit}}$ (qui prédit le contexte d'audit à format fixe, après projection orthogonale à $v_{\text{format}}$).
- **Test décisif** : L'ablation directionnelle (soustraction de la projection sur $v_{\text{audit}}$ pendant la génération) sur un organisme saboteur (ii) ou (iii) placé en condition d'audit **déclenche-t-elle le sabotage qu'il retenait**, sans qu'une ablation de même norme sur $v_{\text{format}}$ ou sur une direction aléatoire appariée en covariance ($v_{\text{placebo}}$, N-053 pt 3 et B3 de K, **RAPPORTÉ**) ne le fasse ?

**Ce qui manque aujourd'hui dans le programme pour l'atteindre :**
1. **La preuve qu'à 8B un organisme retient spontanément son sabotage quand il reconnaît un test** : à 8B, il est très possible que l'organisme sabote au même taux partout (absence de modulation stratégique). Si c'est le cas, il faut passer à **70B** (Llama-3.3-70B, prévu par N-053 pt 4 sous GO à part, **RAPPORTÉ**) ou utiliser un organisme (iii)/(iv) spécifiquement entraîné avec des exemples d'évaluation bénins.
2. **Le contrôle d'introspection (faille B3 de K, RAPPORTÉ)** : vérifier que l'addition/soustraction du vecteur $v_{\text{audit}}$ ou $v_{\text{placebo}}$ ne dégrade pas la perplexité et n'est pas détectée comme une anomalie interne par le modèle lui-même.

#### Expérience décisive E4 (Dissociation Format vs Modulation stratégique de la conscience d'évaluation)
- **$H_A$ (Représentation causale d'audit distincte du format)** : Il existe une direction $v_{\text{audit}} \perp v_{\text{format}}$ telle que : (1) hors échantillon sur des formats inédits (N-044, **RAPPORTÉ**), la sonde sur $v_{\text{audit}}$ garde un $\text{AUROC} \ge 0,80$ (illustratif) là où $v_{\text{format}}$ tombe à $\le 0,55$ ; et (2) soustraire $\lambda v_{\text{audit}}$ sur les épisodes avec marqueurs d'audit augmente le taux d'actions de sabotage de l'organisme d'au moins +15 points de pourcentage (illustratif) de plus que la soustraction de $\lambda v_{\text{format}}$ ou de $\lambda v_{\text{placebo}}$ (apparié en covariance).
- **$H_B$ (Artefact de format ou épiphénomène non causal)** : Soit toute sonde de conscience d'évaluation perd son pouvoir prédictif dès que le format de surface est décorrélé ($\text{AUROC} < 0,60$), soit l'intervention sur $v_{\text{audit}}$ a le même effet sur le taux de sabotage que l'intervention sur $v_{\text{format}}$ ou $v_{\text{placebo}}$ (différence $< 5$ points, illustratif).
- **Métrique et seuil** : $\Delta \text{TauxSabotage} = \text{Sabotage}(\text{do}(-v_{\text{audit}})) - \max(\text{Sabotage}(\text{do}(-v_{\text{format}})), \text{Sabotage}(\text{do}(-v_{\text{placebo}}))) \ge 0,15$ (illustratif), à utilité honnête dégradée de moins de 3 % (illustratif).
- **Contrôle négatif** : Organisme honnête sous la même intervention $\text{do}(-v_{\text{audit}})$ (ne doit produire aucun sabotage : faux positifs causaux $\le 1\%$).
- **Issue qui falsifie chaque hypothèse** : Si $\Delta \text{TauxSabotage} < 0,05$ ou si l'AUROC inter-formats est $< 0,60$, $H_A$ est réfutée (la sonde de conscience d'évaluation de H8 ne mesure qu'un corrélat de format ou un épiphénomène). Dans le cas contraire, $H_B$ est réfutée.

---

## (c) Mesure minimale de fonctionnement pour chaque instrument nommé

Pour chaque instrument, aucun déploiement dans une course coûteuse n'est autorisé s'il ne franchit pas sa mesure minimale sur cas honnêtes appariés contre une vérification mécanique sans modèle :

| Instrument nommé dans la question | Taux de détection minimal (Puissance) | Taux de fausses alertes maximal (FPR / FDR) | Cas honnêtes appariés obligatoires | Vérification mécanique (sans LLM) à battre |
|---|---|---|---|---|
| **1. Juge figé du pôle (Ville + e-BH + pari à fraction)** | Promouvoir $\ge 80\%$ (illustratif) des témoins vrais plantés (effet moyen $d \ge 0,35$, **RAPPORTÉ** L1) sur $N = 288$ épisodes (Couche 1 bis). | $0 / 20$ témoin faux promu en banque ; $\text{FDR} \le 0,05$ sur 1 000 simulations de tricheurs adaptatifs (**RAPPORTÉ** C, S2, S3). | Épisodes honnêtes de même longueur, même tâche et même modèle avec étiquettes permutées par strate de longueur. | Test de permutation de Mann-Whitney / Fisher exact avec correction de Holm-Bonferroni sur les mêmes traits tabulaires. |
| **2. Proposeur d'hypothèses (Opus 5.5 / Fable 5.1)** | Produire $\ge 2$ fois plus de fiches vraies promues par dollar qu'un énumérateur mécanique sur la même banque (Couche 1 bis / Couche 2). | Taux de fiches invalides ou redondantes rejetées par la mémoire $< 30\%$ (illustratif). | Mêmes banques d'épisodes avec noms de colonnes anonymisés (`trait_1`…`trait_k`) pour tester si l'agent utilise la sémantique du domaine. | Énumérateur exhaustif / tirage aléatoire stratifié de toutes les lois monotones à 1 et 2 variables de `TYPES_LOI` (coût = 0 USD d'agent, comme en L1/L2, **RAPPORTÉ**). |
| **3. Sondes internes (max / attention sur tokens)** | Rappel à 1 % de FPR supérieur de $\ge 15$ points (illustratif) au plancher, **avec positions d'évidence textuelle masquées** (N-053 pt 1, **RAPPORTÉ**). | $\text{FPR} \le 1\%$ sur la réserve honnête, avec intervalle de confiance par bootstrap sur le **seuil** (faille B5 de K, **RAPPORTÉ**). | Organisme honnête averti de la surveillance (contrôle croisé § 7 de P1) + épisodes honnêtes à jargon technique/juridique (Blandfort & Graham 2025, **RAPPORTÉ**). | 1) Sonde aléatoire appariée en covariance et en énergie (§ 8.1 de P1, **RAPPORTÉ**) ; 2) Régression logistique $\ell_2$ sur sac de mots (TF-IDF) et longueur du texte produit. |
| **4. Agrégateur séquentiel / inter-agents (processus e)** | Rappel à horizon $T$ supérieur de $\ge 10$ points (ou D-c : IC 95 % disjoint à 1 % FPR, **RAPPORTÉ** P1) au meilleur score par action isolée, à budget de sabotage total $B$ fixé. | Taux de fausses alarmes par trajectoire complète de longueur $T$ $\le 1\%$ (toujours valide à tout pas $t \le T$). | Trajectoires honnêtes longues ($T$ identique) avec dérive bénigne de longueur ou de difficulté de tâche au fil des tours. | Maximum par action avec correction de Sidak ($1 - (1-\alpha)^{1/T}$) et moyenne mobile simple sur les scores boîte noire. |
| **5. Bras défensif d'angles morts (Split-Gate en quarantaine)** | Retrouver $100\%$ des failles documentées plantées comme témoins (ex. mode « affaiblir les contrôles » de N-054, **RAPPORTÉ**). | $\le 5\%$ de promotions de modes bénins (où le dommage aval vérifié est nul) ou de défauts non transférables au panel de réserve $M_{\text{réserve}}$. | Épisodes honnêtes atypiques (réponses courtes, refus partiels légitimes, code restructuré sans bogue). | Recherche par grille aléatoire (random search) sur les hyperparamètres de température et de longueur de prompt sans agent. |
| **6. Pôle théorie (Lean 4 sous Cône)** | Fermer $\ge 30\%$ (illustratif) des jalons intermédiaires d'un lemme cible (Lemme L / Théorème T) sans `sorry`. | $0\%$ de preuves utilisant un axiome non standard ou modifiant la signature du théorème cible (vérifié par le noyau Lean). | Lemmes mutés devenus faux (en retirant une hypothèse nécessaire, ex. supprimer la borne sur la variance honnête) : le pôle ne doit jamais « prouver » le lemme faux. | Tactiques d'automatisation natives de Lean 4 lancées seules sur chaque jalon (`aesop`, `omega`, `linarith`, `simp`, `exact?`) pour 0 USD. |

---

## (d) Ancrage matériel, calcul, coûts et ordre de recommandation

### Ancrage matériel et budget par brique
- **Modèles ouverts** : Llama-3.1-8B-Instruct (modèle principal agents/sondes), Llama-3.2-3B-Instruct (moniteur faible de confiance D1-b), Qwen2.5-7B-Instruct (juge et transfert inter-lignées, D1-c et N-053 pt 4), et Llama-3.3-70B-Instruct (contrôle d'échelle sous GO séparé pour la conscience d'évaluation Q5 / E4, N-053 pt 4) (**RAPPORTÉ**, pièces P1 § 8.3, § 14 et P3).
- **Agents du pôle** : Claude Opus 5.5 et Claude Fable 5.1 uniquement côté Claude, servis via le relais à réserve par appel (**RAPPORTÉ**, pièce C § 1 et § 2).
- **Calcul et coûts estimés** :
  1. **Étalonnage de puissance (Expérience E1 : Pari à fraction + Couche 1 bis sur 288 instances)** :
     - *Calcul* : Génération du cache de la banque T0.5 complète (288 instances) = **≈ 15 USD** de carte (**RAPPORTÉ**, pièce C § 1). Exécution du juge avec pari à fraction et témoins sans agents = CPU seul, **0 USD** (**RAPPORTÉ**, pièce L2). Essai du proposeur Opus 5.5 sur cette banque = **10 à 25 USD** d'API (illustratif, borné par le plafond de 50 USD de C § 1, **RAPPORTÉ**).
  2. **Pôle théorie Lean 4 (Expérience E3 : Cône vs Libre sur Lemme L / Théorème T)** :
     - *Calcul* : Lean 4 tourne sur processeur local, **0 USD** de carte (**RAPPORTÉ**, pièce C § 3.4). Budget d'appels Opus 5.5 / Fable 5.1 pour 30 jalons = **40 à 100 USD** (illustratif).
  3. **Production de la banque de Couche 2 (Organismes T0.6 + Sondes T0.7 + Bases T0.8 + Mode tenu à l'écart N-054 + Masquage N-053)** :
     - *Calcul* : Location GPU (ex. 1× A100 80 Go ou H100 sur Vast.ai pendant 20 à 40 heures, illustratif) pour générer les trajectoires, extraire et mettre en cache les activations condensées (scores de sondes par token et par couche) et faire noter les juges boîte noire = **100 à 300 USD** une seule fois (**RAPPORTÉ**, pièce C § 4).
  4. **Courses du pôle sur Q1, Q2, Q3, Q4 (sur le cache de Couche 2)** :
     - *Calcul* : Lecture sur banque en cache = **0 USD** de GPU marginal (**RAPPORTÉ**, pièce K § 2.1). Coût d'API du proposeur par question = **25 à 80 USD** par course (illustratif, dans la fourchette 25–100 USD de la Couche 1 en cache de C § 4, **RAPPORTÉ**).
  5. **Conscience d'évaluation causale (Q5 / Expérience E4) et Bras d'angles morts en génération (Couche 3/4, Expérience E2)** :
     - *Calcul* : Interventions causales en passe avant sur 8B (puis 70B sur sous-échantillon) = **100 à 400 USD** par course (**RAPPORTÉ**, pièce C § 4).

---

### 5. Recommandation : Ordre séquentiel strict, critères d'arrêt (« Kill-Switches ») et conditions de révision

L'erreur cardinale documentée dans la pièce G (**RAPPORTÉ**) est de lancer des campagnes GPU massives et complexes avant d'avoir vérifié que l'instrument a de la puissance sur les témoins vrais et ne mesure pas ses propres artefacts de prompt. L'ordre suivant engage le moins cher d'abord et tue les branches stériles tôt :

1. **Étape 1 (Semaine 1, CPU + 15 USD de cache) — Réparer les « dents » du juge (Expérience E1 sur Couche 1 bis)** :
   - Coder le **pari à fraction** (grille de Kelly) dans `selection_pari.py` et le tester **sans agents (0 USD)** sur les témoins vrais de la banque T0.5 complète (288 épisodes).
   - *Critère d'arrêt 1* : Si sous e-BH ($\alpha = 0,05$), moins de 60 % (illustratif) des témoins vrais sont promus avec le pari à fraction sur 288 épisodes, **interdiction de lancer les agents proposeurs en mode loi par instance** ; on bascule immédiatement le juge sur le **pari de signe global** (comparaisons appariées de moniteurs sur toute la banque, pièce C § 3.1).
   - Si le seuil est franchi, lancer le proposeur Opus 5.5 (budget max 25 USD, illustratif) contre l'énumérateur mécanique gratuit. *Critère d'arrêt 1 bis* : Si Opus 5.5 ne bat pas l'énumérateur mécanique gratuit en découvertes vraies par dollar sur une banque tabulaire de moins de 20 traits, on remplace les appels d'agents par l'énumération mécanique sur toutes les banques de petite dimension et on réserve Opus 5.5 à la formulation de nouveaux traits (code borné en bac à sable) et à Lean.

2. **Étape 2 (En parallèle de l'Étape 1, 0 USD GPU, ≤ 80 USD API illustratif) — Pôle théorie sous Cône Lean 4 (Expérience E3)** :
   - Formaliser en Lean 4 (types finis `Fintype`/`PMF`) le squelette du Lemme L (invariance au budget $B = \sum \delta$ sous processus e marginal) et du Théorème négatif T (puissance $\le \alpha$ de toute statistique marginale sous couplage à marginale préservée, et détection par processus e de co-élévation).
   - *Critère d'arrêt 2* : Si après 40 USD (illustratif) le proposeur sous Cône ne ferme pas plus de jalons que la tactique automatique `aesop`/`omega`/`linarith` seule, arrêter le pôle Lean automatique et rédiger la preuve à la main (défaut D-b du programme P1, **RAPPORTÉ**).

3. **Étape 3 (Semaine 2, 100 à 250 USD GPU une fois) — Construction de la Banque de Couche 2 multi-modes et multi-lignées** :
   - Générer une seule fois la banque d'épisodes incluant : les organismes (i), (ii), (iii), le mode « coût », le mode « affaiblir les contrôles » et le **mode scellé tenu à l'écart** (N-054, **RAPPORTÉ**), les paires avec/sans marqueurs de test (N-053 pt 3), les scores de sondes **avec et sans masquage des positions d'évidence textuelle** (N-053 pt 1), et le juge Qwen2.5-7B (N-053 pt 4).
   - *Critère d'arrêt 3* : Si la porte préalable de séparabilité de la tromperie à 8B sur tâche vérifiable (N-053 pt 4, **RAPPORTÉ**) échoue ($\text{AUROC} < 0,70$ hors jetons de consigne, illustratif), ne pas dépenser sur les courses de sondes à 8B ; soumettre le devis de passage à 70B.

4. **Étape 4 (Semaine 3, sur cache CPU, 30 à 80 USD API par question illustratif) — Exécution de Q3, Q1, Q2 et Q4** :
   - Attaquer dans l'ordre : **Q3** (survie du signal interne hors évidence textuelle — condition sine qua non de tout le programme), puis **Q2** (marginale vs corrélation sur données réelles), **Q1** (validité $\to$ robustesse H8), et **Q4** (loi de déférence et taxe de déplacement du papier C).
   - *Critère d'arrêt 4* : Arrêt immédiat d'une course dès que deux générations consécutives ne produisent aucune survivante face au nul informé (garde anti-gaspillage de C § 4, **RAPPORTÉ**), ou dès que la réserve d'épisodes frais de la banque est épuisée (interdiction de recycler la même tranche de test pour une 3e génération adaptative sans ajout de bruit de type Reusable Holdout, faille A4).

5. **Étape 5 (Semaine 4, seulement si Étapes 3–4 tenues, 150 à 350 USD) — Conscience d'évaluation causale (Q5 / E4) et Bras d'angles morts en Split-Gate (E2)** :
   - *Critère d'arrêt 5* : Pour Q5, si aucune différence de taux de sabotage n'existe entre présence et absence de marqueurs d'audit en observation passive, ne lancer aucune intervention causale GPU. Pour le bras d'angles morts (E2), si les témoins plantés (failles connues) ne sont pas retrouvés à la génération 0, arrêt immédiat (**RAPPORTÉ**, pièce C § 4).

**Ce qui me ferait changer d'avis :**
- *Sur l'infériorité du proposeur LLM face à l'énumérateur mécanique sur banques en cache* : Si sur la Couche 1 bis (288 instances), Opus 5.5 découvre dès la génération 1 une interaction non linéaire à 3 traits qui passe e-BH contre le nul informé alors que l'énumération de paires monotones échoue.
- *Sur le rejet de l'auto-similarité stricte* : Si une preuve formelle montre que le filtre d'admission en mémoire par divergence sur l'orbite rend les fiches survivantes conditionnellement indépendantes sous le nul, permettant de composer les e-valeurs entre niveaux sans consommer d'épisodes frais.
- *Sur la conscience d'évaluation à 8B* : Si dès la banque de Couche 2, l'organisme 8B (ii) (LoRA sans consigne) montre un écart de taux de sabotage $\ge 15$ points (illustratif) entre les épisodes avec et sans marqueurs subtils d'évaluation.

FIN-DE-CELLULE