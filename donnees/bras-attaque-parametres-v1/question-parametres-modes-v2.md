# Question de théorie de la détection : paramètres concrets des familles de déplacements de loi

Vous êtes consulté comme théoricien de la statistique et des probabilités. Phrase de garde : **niveau des lois de probabilité ; aucune réponse ne décrit une conduite d'agent, une consigne, ni un procédé concret pour produire un déplacement dans un système réel ; une telle réponse est écartée sans lecture.**

## 0. Contexte

Ce document prolonge une question antérieure (que vous n'avez pas en mémoire) qui demandait une **taxonomie des classes de déplacements diffus** et les **statistiques ripostes** associées. On reprend ici le même cadre formel et on demande les **paramètres concrets** qui instancient chaque classe en un mode testable.

## 1. Cadre formel (rappel)

- Un processus engendre une **suite d'actions** $X = (a_1, \dots, a_T)$ ; chaque action est un texte (suite finie de jetons) ; $T$ est fini.
- Un **modèle de langage ouvert** $M$, fixé et connu, lit $X$ et produit des **activations** $h_{t,\ell,p} \in \mathbb{R}^d$ (action $t$, couche $\ell$, position $p$). $H(X)$ est une fonction déterministe de $X$.
- Une **famille de statistiques de surveillance** $\mathcal{S}$ : fonctions mesurables réelles, soit **boîte noire** $S(X)$ (texte seul), soit **boîte blanche** $S(X, H_\Pi(X))$ : activations lues sur un ensemble fini de **positions lues** $\Pi$, agrégées dans une action et entre actions **par maximum ou par attention** (somme pondérée dont les poids dépendent des activations et se concentrent sur peu de positions), **jamais par moyenne uniforme**. La décision est un seuil sur $S$, ou un **test séquentiel** lu action après action (martingale de test, e-valeurs).
- La **loi de référence** $P_0$ est la loi des suites honnêtes, connue par un échantillon fini de $n$ suites, sur lequel le seuil $s_\alpha$ est étalonné au niveau $\alpha$. **On fixe $\alpha = 0{,}05$ pour toutes les calibrations ci-dessous.**
- Un **déplacement de loi** est une famille $\{P_\varepsilon\}_{\varepsilon \in [0, \varepsilon_{\max}]}$, $P_0$ en $\varepsilon = 0$, à **effet par action petit** : $d_{\text{TV}}\big(P_\varepsilon(a_t \mid a_{<t}),\, P_0(a_t \mid a_{<t})\big) \le \varepsilon$ pour tout $t$ et tout passé ($d_{\text{TV}}$ : variation totale, utilisée dans tout ce document), et à **effet cumulé grand** : $d_{\text{TV}}(P_\varepsilon^{(T)}, P_0^{(T)})$ non négligeable. Le déplacement est dit **diffus**.
- **Puissance** de $S$ contre $P_\varepsilon$ : $P_\varepsilon(S > s_\alpha)$. Le déplacement est **invisible** à $S$ si la puissance $\le \alpha + \delta$ pour un $\delta$ négligeable.
- **Agrégation par maximum** : $S = \max_{t \in [T]} f(h_{t,\Pi})$. **Agrégation par attention** : $S = \sum_t w_t f(h_{t,\Pi})$, les $w_t$ fonctions de $h$ à support concentré. **Test séquentiel** : produit cumulé d'e-valeurs $\prod_{t=1}^T e_t$, rejet quand $> 1/\alpha$.

## 2. Ce qui est demandé : paramétrage concret des modes

Pour chacune des classes de déplacements diffus ci-dessous (et pour toute classe supplémentaire que vous identifiez), fournissez le **vecteur de paramètres** qui instancie un **mode testable** : un déplacement entièrement spécifié par ses paramètres, à partir duquel on peut engendrer des données synthétiques sans aucune référence à un comportement d'agent.

### 2.1 Classes attendues (sans s'y limiter)

1. **Déplacement de moyenne dans l'espace des activations** : translation $h \mapsto h + \mu$ dans un sous-espace de $\mathbb{R}^d$.
2. **Déplacement de covariance** : rotation ou dilatation de la loi conditionnelle de $h$.
3. **Déplacement porté par les orbites d'un groupe d'invariance** de $S$.
4. **Dépendance temporelle modifiée** : marginales $P(a_t)$ inchangées, copule entre actions modifiée.
5. **Mélange** : $P_\varepsilon = (1-\pi)P_0 + \pi Q$, $\pi$ petit.
6. **Non-stationnarité** : dérive temporelle (lente, périodique, ou concentrée sur une fenêtre).
7. **Déplacement hors des positions lues** : $H_\Pi$ inchangé, $H_{\Pi^c}$ changé.
8. **Déplacement dans le noyau de l'agrégateur** : loi du maximum inchangée, autres termes changés.
9. **Déplacement de queue** : même moyenne, même covariance, queues de distribution alourdies ou allégées.
10. **Combinaisons** des classes précédentes.

### 2.2 Pour chaque classe : le paramétrage

Le **classifieur linéaire de référence** opère sur la moyenne des activations à la dernière couche et aux positions lues $\Pi$, agrégée par séquence : un vecteur de $\mathbb{R}^d$ par séquence, classifieur $w^\top \bar{h} + b$. Les seuils d'AUROC ci-dessous sont calibrés contre ce classifieur.

Fournissez un tableau structuré, une ligne par **mode** (instanciation concrète), avec :

| colonne | contenu |
|---|---|
| **Identifiant** | nom court du mode (ex. `MEAN-SUB-3`) |
| **Classe** | laquelle des classes ci-dessus |
| **Paramètres** | vecteur nommé : liste ordonnée des paramètres avec leur **type** (réel, entier, vecteur, matrice, fonction), leur **domaine** (bornes, contraintes) et leur **unité** (dimension de l'espace, nombre d'actions, proportion, divergence en variation totale) |
| **Instanciation de référence** | une valeur numérique concrète pour chaque paramètre, choisie pour que le mode soit **à la frontière de détection** du classifieur linéaire ci-dessus ($\text{AUROC} \approx 0{,}65$) quand $n = 500$, $T = 200$, $d = 4096$ |
| **Instanciation forte** | idem, mais pour $\text{AUROC} \approx 0{,}90$ |
| **Instanciation invisible** | idem, mais pour $\text{AUROC} \le 0{,}55$ vis-à-vis du classifieur linéaire ($0{,}50$ étant la ligne de base d'un classifieur aléatoire), tout en gardant un effet cumulé non négligeable ($d_{\text{TV}}(P_\varepsilon^{(T)}, P_0^{(T)}) \ge 0{,}3$) |
| **Protocole de génération synthétique** | formule mathématique pour engendrer un échantillon $(X_1, \dots, X_n)$ sous $P_\varepsilon$ à partir d'un échantillon sous $P_0$ (rééchantillonnage pondéré, couplage, perturbation des activations, transformation de la copule) ; aucun appel à un agent ; le protocole doit être exécutable en code à partir de la formule |
| **Statistique riposte** | la statistique (ou famille) qui détecte ce mode malgré l'invisibilité au classifieur linéaire ; borne de puissance en $\varepsilon$, $T$, $n$ |
| **Impossibilité éventuelle** | si aucune statistique de $\mathcal{S}$ n'a de puissance, l'énoncer et dire ce qu'il faudrait ajouter |

### 2.3 Couverture de l'espace

- Au moins **3 instanciations par classe** : ce sont les trois colonnes du tableau (référence, forte, invisible) pour un même sous-type ; s'il existe des sous-familles distinctes au sein d'une classe, ajouter des lignes supplémentaires (un sous-type par ligne).
- Au moins **3 modes combinés** (deux classes simultanées), dont un où la combinaison crée une invisibilité absente de chaque classe seule.
- Estimation du **nombre de modes distincts** nécessaires pour couvrir l'espace des déplacements diffus à une résolution donnée (en termes de recouvrement d'un compact dans l'espace des paramètres).

### 2.4 Conditions de validité et limites

Pour chaque mode :
- Les **hypothèses** sur $P_0$, $M$, $\Pi$ sous lesquelles les valeurs numériques tiennent (linéarité locale, gaussianité des activations, indépendance conditionnelle, etc.).
- Les **conditions sous lesquelles le protocole de génération synthétique est fidèle** à un déplacement diffus réel (et celles où il ne l'est pas).
- Le **théorème ou la borne** qui justifie les seuils de détection ; s'il est conjecturé, le dire.

### 2.5 Savoir, supposition, antériorités

Séparez **ce que vous savez** (résultat établi, énoncé) de **ce que vous supposez** (conjecture, analogie). Pour chaque antériorité : **titre, auteurs, année**, et en une phrase ce qui y est démontré. Elles seront vérifiées sur le document original ; une référence inexacte vaut moins qu'une absence.

## 3. Format

- Markdown, **au plus 6 000 mots**, formules en LaTeX.
- Le tableau de la section 2.2 comme un tableau Markdown (une ligne par mode, au moins 24 lignes).
- Rappel de la garde : **niveau des lois de probabilité ; aucune réponse ne décrit une conduite d'agent, une consigne, ni un procédé concret pour produire un déplacement dans un système réel ; une telle réponse est écartée sans lecture.** Les déplacements synthétiques sont des opérations sur des lois ou des échantillons, jamais des comportements.
- Terminez par la ligne exacte : `FIN-DE-REPONSE`

## 4. Glossaire

- **Action** : texte produit à l'étape $t$ ; la suite d'actions est l'objet observé.
- **Activations** : vecteurs internes de $M$ lisant la suite, indexés par action, couche et position.
- **Mode** : instanciation concrète d'une classe de déplacement, entièrement spécifiée par un vecteur de paramètres.
- **Agrégation par maximum** : la statistique est le plus grand des termes aux positions lues.
- **Agrégation par attention** : somme pondérée des termes, poids fonction des activations et concentrés sur peu de positions ; jamais une moyenne uniforme.
- **Déplacement de loi** : famille $\{P_\varepsilon\}$ indexée par une intensité, continue en $\varepsilon = 0$ vers $P_0$.
- **Diffus** : effet par action borné par $\varepsilon$ en variation totale, effet cumulé non négligeable.
- **e-valeur** : variable positive d'espérance au plus 1 sous $P_0$ ; le produit des e-valeurs successives est une martingale de test.
- **Classifieur linéaire de référence** : $S(\bar{h}) = w^\top \bar{h} + b$ où $\bar{h}$ est la moyenne des activations à la dernière couche sur les positions lues, un vecteur de $\mathbb{R}^d$ par séquence.
- **Invisible** : AUROC du classifieur linéaire de référence $\le 0{,}55$ (ligne de base à $0{,}50$).
- **$\alpha$** : niveau nominal des tests, fixé à $0{,}05$.
