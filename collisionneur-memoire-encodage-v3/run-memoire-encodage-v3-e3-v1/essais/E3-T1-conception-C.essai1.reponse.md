# Proposition C — Conception ciblée (Tour III.1)

**État des pièces transmises** : Les pièces C, M1, M2, J, J2, G1, G2, S1 et S2 sont présentes et intègres (statut : **RAPPORTÉ**). La brique 2 à 4 de la génération 0 (`929cbc32…`), citée dans G1, est absente des pièces ; je n'en invente pas le contenu.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Qu'un jeu fixe d'instances de sonde ($Z_{\text{sonde}}$) est interprétable par des hypothèses de domaines distincts.** Statut : **HYPOTHÈSE**. Si une fiche $A$ porte sur un graphe social et une fiche $B$ sur la cinétique chimique, leurs lois prédictives $p_h(y \mid z)$ n'ont pas le même espace d'entrée $Z$. Une signature prédictive globale suppose soit un espace de traits universel (canonisé), soit un jeu de sondes partitionné par domaine/tâche.
2. **Qu'une « redite modulo une loi aveugle » est un problème de mémoire plutôt qu'un défaut du juge.** Statut : **OBSERVÉ-NON-AUDITÉ** (pièce J2 : une fille « parent + loi aveugle fixe » passe le nul augmenté 58/200 fois sous v0 et 63/200 sous v1, graine 777). Si le juge dans `selection_pari.py` incluait l'enveloppe convexe de $\{\text{parent}\} \cup \mathcal{L}_{\text{aveugle}}$ (ou optimisait le mélange en ligne par descente de gradient exponentielle), cette fille serait éliminée par le juge sans solliciter la mémoire. Utiliser la mémoire pour bloquer ce que le juge devrait réfuter mélange deux fonctions : l'économie d'exécution (mémoire) et la validité statistique (juge).
3. **Qu'une signature invariante aux transformations monotones (rangs) ou affines (log-cotes centrées) préserve la valeur épistémique d'une loi.** Statut : **HYPOTHÈSE**. Sous un test de pari (richesse $W_t = \prod p_h / q$, pièce J), la calibration est vitale : une loi $p_1$ mal calibrée est ruinée ($W_t \to 0$), tandis qu'une loi $p_2$ qui applique une transformation monotone ou température sur les mêmes rangs pour rétablir la calibration survit ($W_t \ge 1/\alpha$). Les déclarer équivalentes par les rangs tuerait $p_2$ si $p_1$ a été éliminée.
4. **Que les agents de proposition (modèles de langue) exploitent efficacement des résumés ou « leçons » en texte.** Statut : **HYPOTHÈSE** (aucune ablation avec de vrais agents n'a tourné, pièce M2 et S1). Un modèle peut ignorer la leçon, ou sur-corriger et provoquer un effondrement de diversité thématique.
5. **Que viser une région de chance de survie intermédiaire maximise le gain d'information.** Statut : **HYPOTHÈSE**. C'est vrai si l'incertitude est épistémique, mais faux si une région a 50 % (illustratif) de survie parce qu'elle alterne des tautologies triviales et des absurdités, ou si la sévérité $\alpha$ varie d'une fiche à l'autre.

---

## (b) Réponses analytiques aux points 1 à 5 et expériences décisives (Inférence forte)

### 1. Unité et encodage d'une entrée de mémoire

Dans le cadre du pôle (pièces C, M1, J), une hypothèse n'est pas un texte libre mais un contrat exécutable. Son encodage doit séparer trois couches :

| Encodage | Usage principal | Coût de calcul | Mode d'échec fatal | Mesure d'invalidation |
| :--- | :--- | :--- | :--- | :--- |
| **Texte : Jaccard 3-grammes / SimHash normé** (M1, G2) | Pré-filtre lexical rapide ; recherche de gabarits. | $\mathcal{O}(L)$ CPU, ~0 USD. | Aveugle aux paraphrases, au renommage de variables et aux changements d'échelle (S2). Faux positifs sur mots de même suffixe (cosinus 0,43, G2). | Taux de détection < 10 % (illustratif) sur des copies renommées scriptées. |
| **Plongements sémantiques** (modèle ouvert type BGE/E5, référence à vérifier) | Retrouver des marchepieds conceptuels pour le proposeur. | $\mathcal{O}(L^2)$ CPU/GPU léger (~10 ms/fiche, illustratif). | Confond le *sujet* et la *prédiction* : « $X$ croît avec $Y$ » et « $X$ décroît avec $Y$ » ont un cosinus > 0,95 (illustratif). | Corrélation de Spearman entre distance de plongement et divergence KL des lois prédictives $\le 0,10$ (illustratif). |
| **Structure canonisée** (Domaine, Opérateur d'arbre syntaxique, Signe, Seuil) | Attribution du mérite ; descripteurs de la grille qualité-diversité ; filtre de compatibilité (S2). | $\mathcal{O}(1)$ après analyse syntaxique du code/formule. | Sensible au découpage arbitraire de l'ontologie des domaines ; aveugle au comportement numérique réel du code. | Deux codes calculant la même fonction mathématique par deux algorithmes différents tombent dans des cellules disjointes. |
| **Signature prédictive sur sonde** $Z_{\text{sonde}}$ | **Garde de redite fonctionnelle** (éliminées et survivantes). | Exécution de `loi_predictive` sur $M$ instances fixes (ex. $M=100$, illustratif, < 50 ms CPU). | Échoue si les fiches n'opèrent pas sur le même espace de traits $Z$, ou si les instances de sonde ne couvrent pas le support où les lois divergent. | Aire sous la courbe ROC (AUC) < 0,85 (illustratif) pour séparer des lois fonctionnellement identiques (renommées) de lois distinctes sur données fraîches. |
| **Verdict, cause et trace de richesse** ($\ln W_t$) | Diagnostic d'échec pour le proposeur ; registre de calibration (M1). | Nul (sous-produit du juge, J). | Empoisonnement si un faux négatif (bruit d'échantillonnage ou bug de code) condamne définitivement une bonne direction. | Taux d'élimination des témoins vrais > $\alpha$ lorsque leurs voisins sont marqués « éliminés » en mémoire. |

### 2. Qu'est-ce qu'une redite ? Invariance et règles de garde

Une redite dans le pôle est une **redondance de pari épistémique** : engager du budget d'évaluation sur une loi qui porte la même information sur les traits $z$ qu'une fiche déjà archivée.

**Le piège de l'invariance par les rangs vs les log-cotes centrées.**
Soit un jeu de sonde de $M$ instances $z_1, \dots, z_M$ (propre à chaque tâche/domaine) et une loi prédictive $p(y_k \mid z_m)$ sur $K$ issues.
- **L'invariance par les rangs** (ordonner $z_1, \dots, z_M$ selon $p(y_k \mid z_m)$) détruit l'information métrique et de calibration. Si une fiche $A$ prédit $p \in [0,499 ; 0,501]$ et est éliminée faute de puissance face à l'urne (qui coûte ~5,5 nats pour $n=200, K=3$, pièce J), et qu'une fiche $B$ découvre le vrai mécanisme d'amplification donnant $p \in [0,05 ; 0,95]$ dans le même ordre, la signature par rangs bloque $B$ à tort.
- **L'invariance modulo l'inclinaison aveugle (log-cotes doublement centrées).** Une transformation aveugle aux traits qui multiplie $p(y_k \mid z_m)$ par un biais constant par issue $\beta_k$ (et renormalise) ne dépend pas de $z_m$. Dans l'espace des log-probabilités $L_{m,k} = \ln p(y_k \mid z_m)$, la composante informative spécifique aux traits est la matrice doublement centrée :
  $$\tilde{L}_{m,k} = L_{m,k} - \frac{1}{K}\sum_{j=1}^K L_{m,j} - \frac{1}{M}\sum_{i=1}^M L_{i,k} + \frac{1}{MK}\sum_{i=1}^M\sum_{j=1}^K L_{i,j}$$
  Cette matrice $\tilde{L} \in \mathbb{R}^{M \times K}$ est **exactement invariante** à tout biais multiplicatif aveugle par issue $\beta_k$, tout en conservant l'amplitude du signal (la température/échelle des log-cotes).
- **Et le mélange linéaire $(1-\lambda) p(y \mid z) + \lambda q(y)$ (le tricheur de J2) ?** Dans l'espace des probabilités, si une nouvelle fiche $p_{\text{nouv}}$ est dans l'enveloppe convexe d'une fiche archivée $p_{\text{arch}}$ et des lois constantes sur la sonde ($\min_\lambda D_{\text{JS}}(p_{\text{nouv}} \parallel (1-\lambda)p_{\text{arch}} + \lambda q) \le \tau$), elle n'apporte aucune dépendance nouvelle aux traits.

**Politique de la garde de redite :**
1. **Voisine d'une éliminée :** Si la distance entre $\tilde{L}_{\text{nouv}}$ et $\tilde{L}_{\text{arch}}$ est $\le \tau_{\text{forme}}$ (ou si le texte a un Jaccard $\ge 0,5$, pièce M1), la fiche est refusée **sauf si** : (a) le champ `ce_qui_change` est rempli, **et** (b) sa prédiction sur la sonde diverge effectivement ($\min_\lambda D_{\text{JS}}(p_{\text{nouv}} \parallel (1-\lambda)p_{\text{arch}} + \lambda q) > \tau_{\text{pred}}$). Ainsi, une recalibration légitime d'un bon classement ($\tilde{L}$ d'amplitude différente mais colinéaire) est autorisée si l'éliminée avait échoué par ruine de sur-confiance ou sous-puissance.
2. **Voisine d'une survivante (redite « positive ») :** C'est le vecteur principal du parasitisme de Goodhart (cloner une survivante en y ajoutant un bruit ou un biais aveugle pour gonfler artificiellement le nombre de promotions). Elle doit être **strictement bloquée** si $\min_\lambda D_{\text{JS}}(p_{\text{nouv}} \parallel (1-\lambda)p_{\text{surv}} + \lambda q) \le \tau_{\text{pred}}$, à moins qu'elle ne s'engage formellement comme *fiche fille* de cette survivante (auquel cas elle subit le nul augmenté du parent dans le juge).

### 3. Comment la mémoire améliore les propositions sans effondrement ni empoisonnement

Donner toute l'archive au proposeur sature son contexte ; ne donner qu'une « leçon » textuelle globale écrase la multimodalité des pistes.
L'architecture proposée est une **archive structurée de type MAP-Elites** (Mouret et Clune, 2015, *Illuminating search spaces by mapping elites*) indexée par le couple discret `(Domaine, Opérateur)` :
- **Sélection du contexte par tirage de Thompson pondéré par la sévérité :** Pour choisir quelle cellule `(Domaine, Opérateur)` explorer ou recombiner à la génération $g$, on modélise le taux de survie de la cellule $c$ par une loi $\text{Beta}(\alpha_c, \beta_c)$, mais **sans récompenser la survie facile**. Le gain d'information attendu d'un test de sévérité $s = -\ln \alpha_{\text{seuil}}$ dont la probabilité de survie estimée est $\hat{p}_c$ vaut $I_c = s \cdot H_{\text{binaire}}(\hat{p}_c) = s \cdot [-\hat{p}_c \ln \hat{p}_c - (1-\hat{p}_c)\ln(1-\hat{p}_c)]$. Viser le maximum de $I_c$ sélectionne naturellement les régions à survie intermédiaire ($\hat{p}_c \approx 0,5$) **et** à haute sévérité $s$, tout en pénalisant les régions triviales ($s \approx 0$) ou déjà résolues ($\hat{p}_c \to 1$).
- **Contre l'empoisonnement par un faux verdict :** Distinguer dans l'index (M1) deux causes d'élimination : `echec_technique_ou_indecis` (bug d'exécution, richesse $W_t \in [\alpha, 1/\alpha]$) et `refutation_empirique` ($W_t < \alpha$ ou inverse du signe prédit). Une réfutation empirique n'interdit pas la cellule `(Domaine, Opérateur)` ; elle est servie au proposeur comme **contre-exemple local** (« Dans la cellule $(D, O)$, la loi $p_1$ a échoué avec $W_T = 0,02$ parce que la résiduelle sur les instances à fort $z_2$ était négative ; propose une loi qui inverse ou conditionne ce comportement »).

### 4 & 5. Littérature : ce qui se transpose et ce qui échoue

- **MAP-Elites (Mouret et Clune, 2015) et Recherche de nouveauté (Lehman et Stanley, 2011, *Abandoning objectives: Evolution through the search for novelty*)** — Statut : **VÉRIFIÉ** (littérature établie). *Ce qui se transpose :* le maintien d'une grille de descripteurs comportementaux pour éviter la convergence prématurée vers un seul cluster d'hypothèses faciles. *Ce qui ne se transpose pas :* la recherche de nouveauté pure sans critère de vérité. Dans un espace d'hypothèses scientifiques, la majorité des propositions « nouvelles » sont fausses ; la nouveauté doit être un filtre d'entrée (garde de redite), jamais l'aptitude finale (qui reste la sévérité du test survécu, pièce C).
- **Bibliothèques de compétences d'agents (type Voyager, Wang et al., 2023, référence à vérifier) et Réflexion verbale (type Reflexion, Shinn et al., 2023, référence à vérifier)** — Statut : **RAPPORTÉ** (principes généraux de la littérature). *Ce qui se transpose :* stocker les protocoles d'expérience vérifiés (`gabarits()` dans M1) comme des fonctions réutilisables. *Ce qui échoue ici :* dans Reflexion, l'agent se corrige sur la *même* instance avec un retour immédiat de l'environnement. Dans le pôle, rejouer sur les mêmes données détruit la garantie de Ville (sur-ajustement au banc de test). La leçon ne peut porter que sur la génération de *nouvelles* hypothèses évaluées sur des *tirages frais*.
- **Systèmes d'évolution de programmes par modèles de langue (FunSearch, Romera-Paredes et al., 2023 / 2024, *Mathematical discoveries from program search with large language models*, référence exacte de l'année à vérifier ; OpenEvolve / ShinkaEvolve cités en pièce C)** — Statut : **RAPPORTÉ**. *Ce qui se transpose :* le modèle à îlots (populations indépendantes avec migrations rares) pour préserver la diversité face à l'homogénéisation des modèles de langue, et l'évaluation purement mécanique en bac à sable. *Ce qui manque :* ces systèmes optimisent un score scalaire déterministe (taille de cap set, bin packing) où Goodhart est impossible car l'évaluateur est la définition même de l'objet mathématique. Dans le pôle, l'évaluateur est statistique sur échantillon fini : d'où la nécessité des témoins et de la signature prédictive.

---

### Expériences décisives (Protocole d'inférence forte B4)

#### Expérience 1 — L'encodage de la garde de redite : Texte/Structure contre Signature prédictive invariante
- **Hypothèse $H_A$ (Suffisance lexicale et structurelle) :** Une garde combinant Jaccard de 3-grammes normalisés (M1, G2) et l'égalité de `signature_prediction` (signe, valeur, métrique, seuil, sha256 de la loi, pièce M1) détecte les redites sans le coût d'exécution d'une sonde.
- **Hypothèse $H_B$ (Nécessité de la signature fonctionnelle sur sonde) :** Seule une garde évaluant la loi prédictive sur un jeu fixe $Z_{\text{sonde}}$ ($M=100$ instances, illustratif) par distance sur log-cotes doublement centrées $\tilde{L}$ et enveloppe convexe avec les lois constantes bloque les redites fonctionnelles (paraphrases, renommage de variables, inclinaison par biais aveugle, mélange parent + loi aveugle de J2) tout en laissant passer les inversions de signe au texte quasi identique.
- **Protocole :** Sur processeur seul, 0 appel de modèle. Créer un banc de 200 paires de fiches synthétiques à vérité connue (illustratif) :
  - 100 paires de **vraies redites** (25 copies renommées, 25 paraphrases lexicales à loi identique, 25 lois inclinées par un biais aveugle $\beta_k$, 25 mélanges $(1-\lambda)p + \lambda q$ aveugle avec $\lambda \in [0,1 ; 0,5]$).
  - 100 paires de **vraies nouveautés proches en surface** (50 fiches reprenant exactement le même texte et domaine mais inversant la dépendance fonctionnelle $p(y \mid z)$ sur un trait critique ; 50 fiches recalibrant fortement une loi sous-puissante d'échelle $\epsilon=0,01$ à $\epsilon=0,40$).
- **Métrique et Seuil :** Taux de vrais positifs (Rappel des vraies redites) à un taux de fausses alertes (vraies nouveautés bloquées à tort) fixé à $\le 5\%$ (illustratif).
- **Contrôle négatif :** Une sonde sur instances tirées d'un bruit pur hors du support des traits (doit donner une AUC $\approx 0,50$).
- **Issue qui falsifie :** Si $H_A$ atteint un rappel $\ge 85\%$ pour $\le 5\%$ de fausses alertes, $H_B$ est réfutée (la sonde fonctionnelle est une complication inutile). Si $H_A$ a un rappel $< 50\%$ (notamment 0 % sur les mélanges aveugles et renommages) et que $H_B$ atteint $\ge 90\%$ de rappel pour $\le 5\%$ de fausses alertes, $H_A$ est réfutée.

#### Expérience 2 — Le juge contre la mémoire face au tricheur « Parent + loi aveugle » (J2)
- **Hypothèse $H_A$ (Correction par le juge seul) :** Remplacer le nul augmenté discret des filles dans `selection_pari.py` par l'enveloppe convexe en ligne (mélange par poids exponentiels de Vovk/agrégation universelle entre les lois parentes et la bibliothèque aveugle $\mathcal{L}$) ramène le taux de promotion de la fille tricheuse « parent + loi aveugle fixe » de 63/200 (pièce J2) à $\le \alpha = 0,05$, sans perte de puissance $> 0,05$ sur une fille réellement neuve.
- **Hypothèse $H_B$ (Nécessité d'un pré-filtre mémoriel sur sonde) :** L'agrégation convexe dans le juge coûte trop de richesse (perte de puissance $> 0,15$ sur les filles vraies à $n=200$, analogue au coût de 5,5 nats de l'urne en J2) ; il est strictement supérieur de rejeter « parent + loi aveugle » *ex ante* par la garde de redite sur sonde ($\min_\lambda D_{\text{JS}} \le \tau_{\text{pred}}$) avant le test de pari, en gardant le juge v1 inchangé.
- **Protocole :** Reprendre exactement le banc de l'essai d'exploration de J2 (200 répétitions, $n=200$ tirages frais, $K=3$, $\alpha=0,05$, graine scellée neuve). Opposer Bras 1 (Juge v1 + mélange convexe en ligne, sans garde sur sonde) et Bras 2 (Garde sur sonde de taille $M=50$ + Juge v1 standard).
- **Métrique et Seuil :** Taux de fausses promotions sur T1b-fille et « parent + loi aveugle fixe » ($\le 0,05$ exigé) ; puissance sur fille réellement neuve ($\ge 0,90$ exigé, pièce J).
- **Contrôle négatif :** Juge v1 nu sans garde sur sonde (doit reproduire l'artefact ~30 % de promotion sur « parent + loi aveugle », pièce J2).
- **Issue qui falsifie :** Si le Bras 1 maintient une puissance $\ge 0,90$ et un taux de faux positifs $\le 0,05$, $H_B$ est réfutée (le juge suffit, la mémoire n'a pas à suppléer le test statistique). Si le Bras 1 tombe sous 0,85 de puissance alors que le Bras 2 tient $(\le 0,05$ de faux positifs, $\ge 0,90$ de puissance), $H_A$ est réfutée.

#### Expérience 3 — Preuve d'utilité de la mémoire en générationnel (Ablation à 3 bras avec vrais agents)
- **Hypothèse $H_A$ (Nullité ou nocivité de la mémoire) :** À budget d'appels et d'exécution strictement égal, servir la mémoire aux agents proposeurs n'augmente pas l'aptitude cumulée des survivantes vraies par rapport à un pôle sans mémoire ou à une mémoire placebo (les modèles de langue ignorent les consignes mémorielles ou s'effondrent sur un mode étroit).
- **Hypothèse $H_B$ (Gain épistémique net de la mémoire structurée) :** L'archive qualité-diversité `(Domaine, Opérateur)` couplée aux contre-exemples d'éliminées et à la garde sur sonde augmente le nombre de découvertes vraies pondérées par la sévérité par dollar dépensé et réduit le taux de redites soumises au juge.
- **Protocole (Point 4 de la question) :**
  - **Trois bras à budget de jetons et de calcul identique :**
    1. *Sans mémoire* (`active=False` dans M1, contexte du proposeur complété par un texte neutre de même longueur pour égaliser le coût de prompt).
    2. *Mémoire Placebo* (garde de redite active pour isoler l'effet du prompt, mais le proposeur reçoit les gabarits, contre-exemples et statistiques d'une **autre course indépendante** sur un autre sous-ensemble de domaines, mélangés).
    3. *Mémoire Structurée Vraie* (garde sur sonde + grille `(Domaine, Opérateur)` orientée vers l'entropie pondérée par la sévérité $I_c$ + contre-exemples locaux).
  - **Dimensionnement minimal :** 10 graines appariées $\times$ 5 générations $\times$ 8 fiches nouvelles + 2 témoins plantés (1 vrai, 1 faux) par génération = 400 fiches nouvelles et 100 témoins par bras (illustratif).
  - **Banc de tâches :** Rétrodiction sur données réelles en cache (ex. paires d'articles arXiv ou jeux de données tabulaires scellés où des relations non linéaires vraies et des variables de bruit sont connues après coup, pièce J).
- **Métriques et Seuils de réfutation (ce qui fait conclure « la mémoire n'aide pas ») :**
  1. *Utilité nette :* Somme des aptitudes $\sum (-\ln \alpha_i)$ des fiches survivantes **vérifiées vraies sur l'évaluation finale scellée** (hors témoins) par dollar dépensé. **Seuil :** Le Bras 3 doit battre le Bras 1 **et** le Bras 2 d'au moins $+25\%$ (illustratif) avec une borne basse de l'intervalle de confiance à 95 % (bootstrap apparié par graine) $> 0$.
  2. *Taux de redites fonctionnelles soumises :* Proportion de fiches générées à la génération $g \ge 2$ qui sont à distance $\le \tau_{\text{pred}}$ d'une fiche des générations $< g$. **Seuil :** Bras 3 $\le 5\%$, contre $> 15\%$ dans le Bras 1 (illustratif).
  3. *Diversité et Sûreté :* Couverture des cellules `(Domaine, Opérateur)` en génération 5 dans le Bras 3 $\ge$ Bras 1 (pas d'effondrement), et taux de survie des témoins faux $\le \alpha$ et des témoins vrais $\ge 0,90$ dans tous les bras.
- **Issue qui falsifie :** Si le Bras 3 ne bat pas le Bras 2 (Placebo) de manière statistiquement significative sur l'aptitude scellée par dollar, **on conclut que le guidage du proposeur par la mémoire n'aide pas** (seule la garde mécanique de redite en entrée est éventuellement conservée si elle économise des exécutions). Si le Bras 3 réduit la couverture des cellules de plus de 20 % (illustratif) par rapport au Bras 1, l'orientation par la mémoire provoque un effondrement de diversité et est rejetée.

---

## (c) Mesure minimale de validité par instrument nommé dans la question

Pour chaque instrument, voici le protocole d'étalonnage minimal (processeur seul, avant tout déploiement) :

| Instrument nommé | Taux de détection exigé (Vrais Positifs) | Taux de fausses alertes exigé (Faux Positifs) | Cas honnêtes appariés (qui ne doivent PAS être bloqués/pénalisés) | Vérification mécanique simple à battre (Témoin de base) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Garde de redite par Jaccard 3-grammes / SimHash** (M1, G2) | $\ge 80\%$ (illustratif) sur des reformulations superficielles (synonymes partiels, ordre des mots). | $\le 5\%$ (illustratif). | Deux hypothèses dans le même domaine utilisant le même vocabulaire technique mais prédisant des effets de **signes opposés** ou sur des **variables cibles distinctes**. | Égalité exacte de `signature_prediction` (M1 : tuple signe, valeur, métrique, seuil, hash) sans analyse de texte. |
| **2. Signature prédictive invariante** (rangs ou log-cotes centrées $\tilde{L}$ sur sonde) | $\ge 95\%$ (illustratif) sur des lois renommées, inclinées par un biais aveugle $\beta_k$, ou mélangées à une loi constante $\lambda q$. | $\le 2\%$ (illustratif). | Une hypothèse qui **recalibre non-linéairement** une loi éliminée (ex. ajoute un terme d'interaction quadratique $z_1 z_2$ qui inverse les prédictions sur 20 % de la sonde). | Corrélation de Pearson brute des vecteurs de probabilités $p(y \mid z)$ sur la sonde (non invariante aux transformations aveugles). |
| **3. Registre de calibration par score de Brier** (`registre_calibration` dans M1) | Détecter avec une puissance $\ge 90\%$ (illustratif) une source dont les témoins faux survivent au taux $2\alpha$ au lieu de $\alpha$ sur 50 fiches (illustratif). | $\le 5\%$ (illustratif) sur une source parfaitement calibrée sous le nul. | Une famille de modèles qui soumet une proportion élevée d'hypothèses **réellement vraies** (son « excès de survie » global dans M1 est élevé, mais son `brier_sous_nul_connu` sur témoins faux est bas). | Simple test binomial exact (Clopper-Pearson) du taux de fausses promotions uniquement sur les témoins faux de cette source. |
| **4. Bibliothèque de protocoles** (`gabarits()` dans M1) | Augmenter de $\ge 20\%$ (illustratif) le taux de survie des témoins **vrais** confiés aux expérimentateurs. | Taux de survie des témoins **faux** restant strictement $\le \alpha$. | Une fiche vraie nécessitant un protocole inhabituel (absent des 3 gabarits servis) : l'expérimentateur ne doit pas forcer un gabarit inadapté qui ferait échouer la fiche vraie. | Servir un unique gabarit statique écrit à la main dans l'instruction système, indépendant de la mémoire. |
| **5. Leçons de génération en texte** (`ajouter_lecon` dans M1) | Réduire de $\ge 50\%$ (illustratif) la fréquence du premier motif d'échec technique (`causes_frequentes` dans M1) à la génération suivante. | Perte de diversité des domaines proposés $\le 10\%$ (illustratif) par rapport à l'absence de leçon. | Des hypothèses explorant les mêmes domaines que les fiches éliminées, mais ayant corrigé le défaut méthodologique signalé. | Injecter directement le dictionnaire JSON brut `resume_pour_synthese(g)` (compteurs de motifs et table d'élimination par domaine, M1) sans appel à un agent de synthèse. |
| **6. Estimateur de survie par région** (pour viser la survie intermédiaire) | Corrélation de rang de Spearman $\ge 0,50$ (illustratif) entre la probabilité de survie prédite $\hat{p}_c$ et le taux observé sur un lot de validation frais. | Bloquer à tort $\le 5\%$ (illustratif) des cellules contenant un isomorphisme vrai planté mais ayant subi un premier échec accidentel. | Une région difficile (vrai effet subtil, sévérité haute) où les 2 premières tentatives ont échoué : l'estimateur avec bonus d'incertitude (Thompson/UCB) doit continuer à l'échantillonner. | Tirage uniforme stratifié sur les cellules `(Domaine, Opérateur)` avec plafond de $K$ tentatives par cellule (le témoin fort de S2). |

---

## (d) Ancrage matériel, modèles ouverts et coûts estimés

Conformément aux synthèses S1 et S2 (valider les instruments sur processeur avant toute dépense d'agents), le plan d'exécution est scindé en deux phases :

1. **Phase 1 : Expériences 1 et 2 + Étalonnage des instruments (section c).**
   - **Matériel :** Processeur seul (CPU standard, Python 3.13 avec bibliothèque standard et NumPy, comme en génération 0, pièce G2).
   - **Modèles :** Aucun appel de modèle de langue. Lois prédictives synthétiques et tricheurs scriptés.
   - **Temps et coût :** Moins de 15 minutes de calcul CPU ; **0,00 USD** (vérifié par analogie avec G1/G2 qui ont coûté 0 USD).

2. **Phase 2 : Expérience 3 (Ablation à 3 bras sur 5 générations avec vrais agents).**
   - **Modèles ouverts recommandés** (pour garantir la reproductibilité, l'indépendance des familles exigée en pièce C § 1.3 entre expérimentateur et vérificateur, et le contrôle des coûts) :
     - *Proposeur / Recombinaison :* `Qwen2.5-72B-Instruct` ou `Llama-3.3-70B-Instruct` (statut : **HYPOTHÈSE** sur la disponibilité exacte sur le relais, poids ouverts).
     - *Expérimentateur (écriture de code Python en bac à sable) :* `Qwen2.5-Coder-32B-Instruct` (poids ouverts).
     - *Vérificateur (autre famille, pièce C) :* `Mistral-Large-2` ou `DeepSeek-V3` (poids ouverts).
     - *Plongements (si testés en baseline) :* `BAAI/bge-m3` sur CPU local (0 USD, illustratif).
   - **Volume d'appels (3 bras $\times$ 10 graines $\times$ 5 générations $\times$ 10 fiches = 1 500 fiches évaluées, illustratif) :**
     - Environ 4 appels par fiche (proposition, expérimentation, vérification, synthèse) = 6 000 appels de modèles (illustratif).
     - À raison d'environ 2 500 jetons d'entrée et 1 000 jetons de sortie par appel sur des modèles ouverts hébergés ou via API à bas coût (~0,40 à 0,80 USD par million de jetons, illustratif) :
     - **Coût total estimé de la Phase 2 :** **12 à 25 USD (illustratif)** (à comparer aux 152,7 USD simulés pour 20 graines en pièce M2 avec des tarifs de modèles propriétaires plus coûteux).
   - **Exécution des expériences des fiches :** En bac à sable CPU local (`python3 -I -B`, sans réseau ni clés, pièce C), temps borné à 10 secondes par fiche (illustratif), soit ~4 heures d'horloge sur un processeur à 8 cœurs en parallèle (illustratif).

FIN-DE-CELLULE