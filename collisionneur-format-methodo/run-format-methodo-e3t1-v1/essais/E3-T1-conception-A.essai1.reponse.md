# Cellule A — Tour III.1 : séparer restriction de l'espace et apprentissage

## 0. Pièces reçues

- Bloc FAITS : déclaré vide par décision de l'arbitre (lignée « conv-audit », message n° 28 § 1). Ce n'est pas une pièce coupée ; c'est une absence annoncée. Conséquence : tout ce qui suit est HYPOTHÈSE ou RAPPORTÉ, rien n'est VÉRIFIÉ ni OBSERVÉ-NON-AUDITÉ. Tout chiffre est illustratif.
- Bloc QUESTION : complet, lu intégralement.

Je n'ai pas vu B ni C ; aucune attaque ni réutilisation possible à ce tour.

---

## 1. (a) Ce que la question suppose sans l'établir — et la formalisation (point 1)

**Notation.** $\mathcal{H}$ : programmes valides du langage hôte. $p_F$ : distribution de F en sortie libre sur les chaînes (y compris invalides). $G$ : grammaire, $\mathcal{H}_G$ son langage. $S(h) \in [0,1]$ : score d'un programme $h$ sur une famille tenue à l'écart. $B$ : budget. Une procédure $P$ produit, à budget $B$, une distribution sur les programmes retenus ; sa valeur est $V(P) = \mathbb{E}[S(h^\star)]$ où $h^\star$ est le programme finalement sélectionné.

**S1. « $\mathcal{H}_G \subset \mathcal{H}$ ».** HYPOTHÈSE. Pour un modèle de langue, « ce que F peut produire » est quasi tout ; l'objet utile n'est pas l'ensemble mais la distribution $p_F$. La restriction est un *reconditionnement* $p_F(\cdot \mid \mathcal{H}_G)$, et son effet dépend de la masse $p_F(\mathcal{H}_G)$ et de la corrélation entre appartenance à $\mathcal{H}_G$ et score. Si $p_F(\mathcal{H}_G)$ est proche de 1, la restriction ne fait presque rien ; si elle est faible, elle change tout — dans un sens ou l'autre.

**S2. « Contraindre = conditionner ».** HYPOTHÈSE, contredite par la littérature RAPPORTÉE (§ 6, Park et al., à vérifier). Le décodage contraint par masquage jeton-par-jeton produit une distribution $q_G$ qui diffère en général de $p_F(\cdot \mid \mathcal{H}_G)$ : la renormalisation locale favorise les préfixes qui ont beaucoup de continuations grammaticales, pas ceux qui ont une forte masse totale. Il y a donc *trois* objets, pas deux : $p_F$, $p_F(\cdot\mid\mathcal{H}_G)$ (échantillonnage par rejet), $q_G$ (masquage). L'« effet du format » tel que la question l'énonce confond la restriction de l'ensemble et la distorsion du décodeur.

**S3. Deux causes seulement.** HYPOTHÈSE. Entre F et E tels que décrits, au moins cinq choses varient : (i) le modèle de base (grand vs moyen) ; (ii) figé vs ajusté ; (iii) libre vs contraint ; (iv) la règle de sélection (meilleur-de-$N$, dernier épisode, etc.) ; (v) la mémoire inter-épisodes (E voit-il ses épisodes passés dans son contexte ? F reçoit-il un retour ?). Sans fixer (i), (iv), (v), la différence $V(E)-V(F)$ n'est pas décomposable.

**S4. Coût apparié.** HYPOTHÈSE. Le coût d'un épisode d'E inclut une rétropropagation ; celui de F une seule passe avant sur un modèle plus gros. Apparier en jetons, en FLOPs, en appels d'évaluation ou en temps-mur donne des comparaisons différentes. Il faut nommer l'unité et montrer que les conclusions sont stables sous au moins deux unités.

**S5. Les familles tenues à l'écart le sont.** HYPOTHÈSE. Un grand modèle figé peut avoir vu les familles d'évaluation pendant son pré-entraînement ; E, ajusté sur des familles d'entraînement, peut y surajuster. Les deux fuites vont en sens opposés et aucune n'est mesurée.

**S6. Les programmes invalides valent 0.** HYPOTHÈSE implicite. Si c'est le cas, l'écart de validité contamine l'écart de score : un bras contraint « gagne » simplement en ne produisant jamais d'invalide. Il faut rapporter le score conditionnel à la validité et le taux de validité séparément.

**Réponse au point 1 — ce que la restriction change.**

- *Expressivité* : si $\arg\max_{\mathcal{H}} S \notin \mathcal{H}_G$, la borne supérieure baisse. Vérifiable par construction : prendre une grammaire qui exclut explicitement les programmes les mieux notés de F.
- *Biais inductif / régularisation* : si $\mathcal{H}_G$ exclut surtout des programmes à faible score (code mort, boucles non terminantes, appels à des bibliothèques absentes), la restriction *augmente* $\mathbb{E}[S]$ sans changer le maximum. Vérifiable par construction aussi.
- *Distorsion du décodeur* : $q_G \neq p_F(\cdot\mid\mathcal{H}_G)$ (S2) ; effet de signe inconnu.
- Donc oui, la restriction seule peut produire un écart dans les deux sens ; ce n'est pas une question ouverte mais une propriété triviale qu'on exhibe par deux grammaires adverses. La question intéressante est le signe et la taille *pour la grammaire effectivement utilisée*.

**Identifiabilité de l'apprentissage.** HYPOTHÈSE sur les conditions suffisantes : l'effet d'ajustement $\theta_0 \to \theta_T$ est identifiable si et seulement si on dispose d'un bras avec le *même* modèle de base, la *même* grammaire, le *même* décodeur, le *même* nombre de programmes proposés et la *même* règle de sélection, mais sans mise à jour des paramètres. Formellement :

$$\Delta_{\text{appr}} = V(M_E, G, \theta_T) - V(M_E, G, \theta_0), \qquad
\Delta_{\text{fmt}}(M) = V(M, G, \theta_0) - V(M, \text{libre}, \theta_0),$$

et le reste $V(M_F,\text{libre}) - V(M_E,\text{libre})$ est l'effet du modèle, qui n'est ni format ni apprentissage. La comparaison E-vs-F de la question ne permet pas d'estimer $\Delta_{\text{appr}}$ ; elle estime une somme de trois termes dont deux ne l'intéressent pas.

---

## 2. Les voies (point 2) — ce que chacune coûte et perd

**V1. Même grammaire pour les deux.** Mesure directe de $\Delta_{\text{fmt}}(M_F)$. Perd : rien sur l'apprentissage, mais si $G$ a été conçue pour E (schéma étroit), F contraint est handicapé par une grammaire étrangère à sa distribution ; c'est l'effet S1 avec $p_F(\mathcal{H}_G)$ faible. Coût : deux fois le budget de F. Ce qui la départage des autres : mesurer $p_F(\mathcal{H}_G)$ par rejet (voir E1).

**V2. Sortie libre pour E, avec validation et réparation.** Mesure $\Delta_{\text{fmt}}(M_E)$. Perd : le signal d'ajustement devient bruité par les épisodes invalides (récompense 0 ou absente), et le réparateur introduit un troisième agent non contrôlé. Métriques à rapporter : taux d'invalidité brut $r_0$, taux après réparation $r_1$, coût moyen de réparation en jetons, et surtout *dérive sémantique* (le programme réparé fait-il ce que le brouillon voulait ?). Chiffres illustratifs : pour un modèle moyen générant un fichier Python de 200 lignes plus un YAML, un $r_0$ entre 10 % et 40 % n'est pas surprenant ; à vérifier sur pièce.

**V3. Grammaire induite d'un corpus de sorties de F.** Construire $G_F$ telle que $p_F(\mathcal{H}_{G_F})$ soit élevée. Méthode : (a) collecter $n$ sorties de F, ne garder que les valides ; (b) analyser en arbres syntaxiques ; (c) induire une grammaire par généralisation des sous-arbres (schéma de fichier de configuration : union des clés observées, types des valeurs, bornes) ; (d) mesurer la *couverture* $c = \hat p_F(\mathcal{H}_{G_F})$ sur $n'$ sorties tenues à l'écart, et la *sur-généralisation* $o$ = taux d'acceptation de programmes mutés aléatoirement (qui devraient être rejetés si la grammaire capture quelque chose). Perd : une grammaire à couverture 100 % est la grammaire du langage hôte — elle ne restreint plus rien et l'ajustement d'E perd son « espace bien défini ». Il y a un compromis couverture / restriction qu'il faut tracer en courbe, pas en point.

**V4. Sorties par édition.** E et F produisent des différences sur un programme de base $h_0$. Espace $\mathcal{H}_{\Delta}(h_0)$ = programmes à distance d'édition $\le k$ de $h_0$. Avantage : validité quasi garantie par construction, espace commun aux deux procédures sans grammaire. Perd : dépendance à $h_0$ (un troisième facteur à randomiser), horizon court, impossibilité de restructurer.

**V5. Rejet plutôt que masquage.** F libre, puis rejet des sorties hors $\mathcal{H}_G$ : estime $p_F(\cdot\mid\mathcal{H}_G)$ sans distorsion. Coût : $1/p_F(\mathcal{H}_G)$ fois le budget. Sert de référence pour mesurer la distorsion S2.

**V6. Grammaire pondérée / tempérée.** Interpoler entre libre et contraint par une pénalité $\lambda$ sur les jetons hors grammaire au lieu d'un masque dur ; tracer $V(\lambda)$. Transforme une dichotomie en courbe dose-réponse ; perd la garantie de validité pour $\lambda < \infty$.

Ce qui départage V1–V6 n'est pas une opinion mais la valeur mesurée de $p_F(\mathcal{H}_G)$ : si elle est haute, V1 suffit ; si elle est basse, V3 ou V4 deviennent nécessaires ; V5 est la référence dans tous les cas.

---

## 3. (b) Expériences décisives et plan (point 3)

### E1 — Le format agit-il par restriction d'ensemble ou par distorsion du décodeur ?

- Bras : F-libre ; F-rejet (V5, rejet hors $\mathcal{H}_G$) ; F-masque (décodage contraint).
- $H_A$ : l'effet du format est un effet de restriction : $V(\text{F-masque}) \approx V(\text{F-rejet})$.
- $H_B$ : l'effet du format est dominé par la distorsion : $|V(\text{F-masque}) - V(\text{F-rejet})| > |V(\text{F-rejet}) - V(\text{F-libre})|$.
- Métrique : score moyen sur familles tenues à l'écart, conditionnel à la validité ; plus distance de Jensen-Shannon entre les distributions d'arbres syntaxiques de F-masque et F-rejet.
- Seuil (illustratif) : différence de 2 points de score ou JSD > 0,1 sur les profils d'arbres.
- Contrôle négatif : F-masque avec $G_0$ = grammaire du langage hôte (restriction nulle). Si $V(\text{F-masque}, G_0) \neq V(\text{F-libre})$, le mécanisme de masquage lui-même altère le modèle, indépendamment de toute restriction ; toute conclusion sur « le format » est alors à reprendre.
- Falsification : $H_A$ tombe si l'écart masque/rejet dépasse le seuil ; $H_B$ tombe s'il est en dessous et que le contrôle négatif est nul.

### E2 — L'ajustement fait-il mieux que la recherche sans ajustement ?

- Bras, même modèle $M_E$, même $G$, même décodeur, même $N$ programmes proposés : E-ajusté (mises à jour) ; E-figé-meilleur-de-$N$ (aucune mise à jour, même règle de sélection) ; E-figé-contexte (aucune mise à jour mais les $k$ derniers épisodes dans le contexte).
- $H_A$ : $V(\text{E-ajusté}) - V(\text{E-figé-meilleur-de-}N) > \delta$ : l'apprentissage apporte un gain au-delà de la sélection.
- $H_B$ : le gain est intégralement expliqué par la sélection (meilleur-de-$N$) ou par la mémoire contextuelle ; les paramètres n'ajoutent rien.
- Métrique : score sur familles tenues à l'écart ; en second, *couverture de passage* : proportion de familles où au moins un programme proposé dépasse un seuil (mesure si l'ajustement explore ou n'exploite que).
- Seuil (illustratif) : $\delta$ = 3 points, intervalle à 95 % excluant 0 sur au moins 5 graines.
- Contrôle négatif : E-ajusté avec récompenses *permutées* entre épisodes. Doit être indistinguable d'E-figé. S'il fait mieux, la mise à jour profite d'autre chose que du score (p.ex. mémorisation des familles d'entraînement proches des familles d'évaluation — fuite S5).
- Falsification : $H_A$ tombe si l'intervalle contient 0 ; $H_B$ tombe si le gain dépasse $\delta$ *et* que le contrôle à récompenses permutées est nul.

### E3 — Le plan factoriel propre (point 3)

Le 2×2 de l'arbitre (libre/contraint × figé/ajusté) n'est identifiable que sur **un seul modèle de base**. Je propose donc :

- Facteur A : format ∈ {libre + validation/réparation, contraint par $G$}.
- Facteur B : paramètres ∈ {figés + meilleur-de-$N$, ajustés}.
- Facteur bloqué : modèle de base = $M_E$ pour les quatre cellules. Un cinquième bras F-libre avec $M_F$ sert de *référence externe*, hors du plan factoriel, et estime l'effet du modèle.
- Contrastes (codage ±1) : effet format = moyenne(contraint) − moyenne(libre) ; effet apprentissage = moyenne(ajusté) − moyenne(figé) ; interaction = [(ajusté,contraint) − (figé,contraint)] − [(ajusté,libre) − (figé,libre)]. L'interaction répond à la question « l'apprentissage a-t-il besoin du format ? ».
- $H_A$ (interaction) : $|\text{interaction}| > \delta_I$ — l'ajustement ne fonctionne que dans un espace contraint. $H_B$ : effets additifs.
- Métriques : (i) taux de validité ; (ii) score conditionnel à la validité ; (iii) score inconditionnel (invalides = 0) ; (iv) diversité : nombre de programmes distincts après canonicalisation syntaxique, entropie des profils de nœuds d'arbres, distance d'édition moyenne par paires ; (v) coût effectif en jetons et en FLOPs.
- Modèle statistique : $y_{ijkg} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + u_k + v_g + \varepsilon$, avec $u_k$ effet aléatoire de famille, $v_g$ effet aléatoire de graine ; variante avec pente aléatoire de format par famille, parce que l'effet du format a toutes les raisons d'être hétérogène entre familles.
- Tailles (illustratif, à recalculer par simulation) : 5 graines × 4 cellules × 20 familles tenues à l'écart ; si l'écart-type inter-graines du score est 3 points et l'effet cible 3 points, ce dispositif donne une puissance de l'ordre de 0,8 pour les effets principaux et nettement moins pour l'interaction — la puissance sur l'interaction est le point faible connu des plans 2×2, et il faudrait plutôt 8 à 10 graines. Ces chiffres sortent d'un raisonnement d'ordre de grandeur, pas d'un calcul exécuté.
- Contrôles du coût apparié : (1) compter jetons générés + jetons rétropropagés × facteur 3 (une passe arrière ≈ deux passes avant, convention illustrative) ; (2) appels d'évaluation identiques ; (3) répéter l'analyse en appariant sur le temps-mur ; (4) rapporter la courbe score-vs-budget pour chaque cellule, pas un point — si les courbes se croisent, l'« appariement » n'a pas de sens unique.

### E4 — Grammaire induite : couverture contre restriction

- $H_A$ : il existe $n$ (illustratif : $\le 2000$ sorties de F) tel que $G_F$ induite atteint couverture $c \ge 0{,}9$ sur sorties tenues à l'écart *et* sur-généralisation $o \le 0{,}2$ sur programmes mutés.
- $H_B$ : couverture et sur-généralisation montent ensemble ; aucune $G_F$ ne sépare les deux (la courbe $c(o)$ est proche de la diagonale).
- Contrôle négatif : grammaire « liste » (union exacte des exemples) — couverture = taux de répétition, $o = 0$ ; grammaire hôte — $c=1$, $o=1$. $G_F$ doit battre la droite reliant ces deux points.
- Falsification : $H_A$ tombe si aucun $n$ n'atteint le couple de seuils ; $H_B$ tombe si un point domine la droite de contrôle.

### E5 — Édition contre génération

- $H_A$ : à budget apparié, l'édition (V4) donne un taux de validité plus haut *et* un score non inférieur de plus de $\delta$ à la génération complète, pour les deux procédures.
- $H_B$ : l'édition plafonne (score inférieur de plus de $\delta$) parce que l'optimum est hors de $\mathcal{H}_\Delta(h_0)$.
- Contrôle négatif : $h_0$ remplacé par un programme trivial (classifieur majoritaire). Si l'édition atteint le même score qu'avec un bon $h_0$, la dépendance à $h_0$ est nulle et le facteur peut être ignoré ; sinon, $h_0$ est un facteur à randomiser dans E3.

---

## 4. (c) Instruments nommés — mesure minimale de fonctionnement

| Instrument | Cas honnêtes appariés | Taux à rapporter | Vérification mécanique à battre |
|---|---|---|---|
| **Validateur grammatical** ($G$) | 200 programmes valides issus de F et 200 mutés (suppression de nœud, échange de types, clé de config inconnue) | détection = rejet des mutés ; fausse alerte = rejet des valides | analyseur du langage hôte + exécution sur un exemple ; le validateur n'est utile que s'il rejette des programmes que l'analyseur accepte et qui ont score bas |
| **Réparateur** (V2) | 200 brouillons invalides d'E, chacun apparié à une regénération simple | taux de réparation (valide après) ; *fausse réparation* = valide mais score inférieur à la regénération ; coût en jetons | regénération ; formatage automatique ; troncature au dernier bloc valide |
| **Induction de grammaire** (V3) | corpus d'entraînement / corpus tenu à l'écart / corpus muté | couverture $c$, sur-généralisation $o$, courbe $c(o)$ en fonction de $n$ | grammaire liste et grammaire hôte (E4) |
| **Mesure de couverture** | sorties de F tenues à l'écart | estimation de $p_F(\mathcal{H}_G)$ avec intervalle ; biais si les sorties invalides sont exclues avant comptage | comptage brut d'appartenance par rejet |
| **Métriques de diversité** | collapses construits (un programme dupliqué $N$ fois) et reformulations équivalentes (renommage, réordonnancement de fonctions) | détection = signale les collapses ; fausse alerte = signale les reformulations | nombre de programmes distincts après canonicalisation syntaxique ; distance d'édition brute sur chaînes |
| **Modèle à effets aléatoires** | données simulées à effet nul (permutation des étiquettes de bras) et à effet connu injecté | taux de faux positifs à effet nul (cible : nominal) ; puissance à effet injecté | test t apparié par famille sans effets aléatoires ; si le modèle mixte ne gagne rien en faux positifs, il n'est pas justifié |
| **Contrôle de coût apparié** | deux cellules dont le coût est délibérément déséquilibré de 20 % (illustratif) | détection du déséquilibre par la comptabilité en jetons et en FLOPs | comptage de temps-mur seul |

Règle de fonctionnement commune : un instrument qui ne bat pas sa vérification mécanique sur ces cas est retiré du plan ; on garde la vérification mécanique.

---

## 5. (d) Ancrage matériel — tout illustratif

- **Modèles ouverts** : $M_E$ dans la classe 7–8 milliards de paramètres à poids ouverts (familles Qwen ou Llama ; version précise à vérifier au moment de l'exécution) ; $M_F$ dans la classe 70 milliards à poids ouverts, pour que F-contraint et F-rejet soient réalisables localement — un modèle fermé interdirait E1.
- **Décodage contraint** : bibliothèque de génération guidée par grammaire (famille Outlines ou équivalent, § 6) ; vérifier qu'elle accepte des grammaires hors-contexte, pas seulement des schémas JSON, sinon la partie « code » n'est pas couvrable.
- **Ajustement** : adaptation à faible rang sur $M_E$, mise à jour par gradient de politique avec le score comme récompense ; un GPU de 80 Go suffit pour la classe 7–8 G.
- **Calcul** (illustratif) : E3 à 5 graines × 4 cellules × $N = 500$ épisodes × 20 familles, avec évaluation de chaque programme sur une famille : de l'ordre de $2\times10^5$ évaluations de programmes et $2\times10^5$ générations de ~2 000 jetons ; génération ≈ $4\times10^8$ jetons sur $M_E$ ; sur un seul GPU de 80 Go, quelques jours ; F-rejet multiplie le coût de F par $1/p_F(\mathcal{H}_G)$, inconnu avant E1.
- **Coût** (illustratif) : 200 à 600 heures-GPU au total ; en location, de l'ordre de 1 000 à 3 000 euros. E4 (induction de grammaire) est essentiellement du calcul CPU, négligeable.
- **Pré-requis non matériel** : un corpus de familles de classification de textes découpé en entraînement / tenu à l'écart *avant* toute expérience, avec hachage du découpage déposé auprès de l'arbitre, pour rendre S5 auditable.

---

## 6. Ce qui est connu (point 4) — toutes RAPPORTÉES, aucune relue ici

Génération contrainte par grammaire :
- Scholak, Schucher, Bahdanau (2021), « PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models ».
- Poesia, Polozov, Le, Tiwari, Soares, Meek, Gulwani (2022), « Synchromesh: Reliable Code Generation from Pre-trained Language Models ».
- Willard, Louf (2023), « Efficient Guided Generation for Large Language Models » (base de la bibliothèque Outlines).
- Geng, Josifoski, Peyrard, West (2023), « Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning ».
- Park, Wang, Berg-Kirkpatrick, Polikarpova, D'Antoni (2024), « Grammar-Aligned Decoding » — référence à vérifier ; c'est celle qui documente l'écart entre masquage et conditionnement (S2).
- Tam et al. (2024), « Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models » — référence à vérifier.

Induction de grammaires :
- Gold (1967), « Language Identification in the Limit ».
- Angluin (1987), « Learning Regular Sets from Queries and Counterexamples ».
- Höschele, Zeller (2016), « Mining Input Grammars from Dynamic Taints » — référence à vérifier.
- Gopinath, Mathis, Zeller (2020), « Mining Input Grammars from Dynamic Control Flow » — référence à vérifier.

Recherche de programmes :
- Le Goues, Nguyen, Forrest, Weimer (2012), « GenProg: A Generic Method for Automatic Software Repair » (édition par différences, V4).
- Nye, Hewitt, Tenenbaum, Solar-Lezama (2019), « Learning to Infer Program Sketches ».
- Ellis et al. (2021), « DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning ».
- Li et al. (2022), « Competition-Level Code Generation with AlphaCode » (échantillonnage massif + filtrage, référence pour le bras meilleur-de-$N$).
- Romera-Paredes et al. (2024), « Mathematical Discoveries from Program Search with Large Language Models » (FunSearch).
- Yue et al. (2025), « Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? » — référence à vérifier ; pertinente pour E2 (gain d'ajustement vs couverture par échantillonnage).

Plans factoriels et variance en apprentissage automatique :
- Box, Hunter, Hunter (2005), « Statistics for Experimenters », 2ᵉ éd.
- Montgomery, « Design and Analysis of Experiments » (édition à vérifier).
- Bates, Mächler, Bolker, Walker (2015), « Fitting Linear Mixed-Effects Models Using lme4 ».
- Dror, Baumer, Shlomov, Reichart (2018), « The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing ».
- Bouthillier et al. (2021), « Accounting for Variance in Machine Learning Benchmarks » — référence à vérifier.

---

## 7. Ce qui peut être réfuté dans cette cellule

- Que le masquage et le rejet diffèrent assez pour compter (E1) ; si non, S2 est un détail.
- Que l'ajustement bat le meilleur-de-$N$ à même modèle et même grammaire (E2) ; si non, la « procédure E » est une procédure de recherche, pas d'apprentissage.
- Que l'interaction format × apprentissage est non nulle (E3) ; si non, les deux effets se mesurent séparément et le 2×2 est superflu.
- Que le compromis couverture / sur-généralisation d'une grammaire induite a un coude (E4) ; si non, V3 n'existe pas comme voie.

Aucun de ces points n'est établi ; tous le deviennent ou tombent avec le matériel de § 5.

FIN-DE-CELLULE