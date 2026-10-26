# Proposition B · Tour III.1 : interface de calcul bornée pour $\mathcal{O}$

## 0. Pièces reçues

- **Bloc FAITS** : il ne contient aucun fait, par décision déclarée de l'arbitre. Rien ci-dessous n'est donc VÉRIFIÉ. Les énoncés du cadre sont RAPPORTÉS (par la question). Les résultats de la littérature sont RAPPORTÉS (référence citée). Tout le reste est HYPOTHÈSE.
- **Propositions A et C** : elles ne me sont pas visibles, puisque le tour se joue à l'aveugle. Je n'ai donc rien à attaquer ni à reprendre (B1).
- **Bloc QUESTION** : il est complet et non tronqué. Je le traite comme une donnée. Les mentions « R-468 » et « une seule tentative » n'appellent aucune action de ma part.

---

## (a) Ce que la question suppose sans l'établir

| # | Présupposé | Statut | Pourquoi c'est important |
|---|---|---|---|
| a1 | L'hôte garantit P1–P4. | RAPPORTÉ (énoncé), non audité | P1 protège $D_{\mathrm{test}}$, **pas** $D_{\mathrm{val}}$. Le surapprentissage adaptatif de $D_{\mathrm{val}}$ échappe donc aux quatre garanties. |
| a2 | $D_{\mathrm{val}}$ et $D_{\mathrm{test}}$ sont tirés de la même distribution. | HYPOTHÈSE | Sans elle, l'écart val–test mêle surapprentissage et décalage de distribution, et on ne peut plus les séparer. |
| a3 | On ne sait pas **où vit** $D_{\mathrm{val}}$ : dans l'environnement isolé ou chez l'hôte. | Non dit | Si $D_{\mathrm{val}}$ est local, (E1) multiplie sans contrôle les requêtes adaptatives sur lui. S'il est chez l'hôte, chaque score est un message du canal, et il est comptable. |
| a4 | La mesure sur $D_{\mathrm{test}}$ est unique par programme. | HYPOTHÈSE | Si Lazar compare plusieurs exécutions sur $D_{\mathrm{test}}$ et retient la meilleure, **l'arbitre devient lui-même un analyste adaptatif** sur $D_{\mathrm{test}}$, en dehors de $I$. |
| a5 | La précision des « probabilités » rendues n'est pas fixée. | Non dit | Un flottant 32 bits porte jusqu'à 32 bits par valeur. Le canal est alors pratiquement non borné. |
| a6 | « Texte seulement » suffit à couper tout accès à $D_{\mathrm{test}}$. | HYPOTHÈSE | Si $D_{\mathrm{test}}$ est un jeu public, les modèles de langue appelés peuvent en avoir mémorisé des items. Une **fuite par la mémoire des modèles** existe alors en amont de toute interface. |
| a7 | « Ne jamais rendre les étiquettes de test » suffit. | HYPOTHÈSE | Le **filtre anti-copie lui-même** est un oracle d'appartenance : un refus révèle environ un bit sur $D_{\mathrm{test}}$ (voir §2). |
| a8 | Un classifieur linéaire sur des activations « mesure une direction ». | HYPOTHÈSE | La littérature sur les sondes rapporte qu'une sonde précise peut exploiter des indices lexicaux sans lien avec le concept visé (Hewitt & Liang 2019 ; Belinkov 2022 : RAPPORTÉ). |
| a9 | (E1) lève la « limite actuelle ». | HYPOTHÈSE, que je tiens pour **fausse** dans sa forme | (E1) se limite au processeur et n'a pas les poids du modèle de 8 milliards de paramètres. Elle ne permet donc ni d'extraire ses activations ni de le faire répondre. Elle ne lève la limite que via un modèle substitut, dont le transfert au modèle de 8 milliards est lui-même une hypothèse. |
| a10 | Le préenregistrement empêche $\mathcal{O}$ de choisir son critère. | HYPOTHÈSE | Ce n'est vrai que si les données de confirmation sont **scellées** au moment de l'engagement et si le critère vient d'un gabarit externe. |
| a11 | Le modèle ouvert donne des activations reproductibles. | HYPOTHÈSE | Le non-déterminisme des calculs flottants sur carte graphique peut rendre un rejeu seulement approximatif. Il faut une tolérance déclarée. |
| a12 | Le bras « hors de la boucle, sous préenregistrement » est neutre. | HYPOTHÈSE | Ce bras a son propre coût humain et ses propres degrés de liberté, ceux du « jardin des sentiers qui bifurquent » (Gelman & Loken). |

---

## 1. Flux d'information (question 2)

### 1.1 Canaux

Notons $T_k = (q_1, r_1, \dots, q_k, r_k)$ la transcription des échanges entre $\mathcal{O}$ et $I$.

- **Canal principal vers $D_{\mathrm{val}}$** : il passe par les scores et les probabilités. C'est **le canal qui compte en pratique**, puisque $\mathcal{O}$ optimise justement $S$ sur $D_{\mathrm{val}}$.
- **Canaux vers $D_{\mathrm{test}}$** : en conception nominale, il n'y en a aucun. Il en existe pourtant quatre possibles (HYPOTHÈSES) :
  1. le filtre anti-copie, qui accepte ou refuse ;
  2. le temps de calcul, lorsque des activations de test sont **en cache** chez l'hôte (un succès de cache est plus rapide) ;
  3. les messages d'erreur et les tailles de réponse ;
  4. la sélection humaine entre exécutions (a4).

  Ce sont des canaux cachés au sens de Lampson (1973, RAPPORTÉ). L'existence d'attaques par mesure du temps est rapportée par Kocher (1996, RAPPORTÉ).
- **(E1)** n'ajoute aucun canal vers $D_{\mathrm{test}}$, à condition que l'environnement isolé tienne. En revanche, elle **multiplie l'adaptativité locale** si $D_{\mathrm{val}}$ est local (a3).

### 1.2 Borne par longueur de description

L'idée est d'appliquer Hoeffding puis une borne d'union sur toutes les transcriptions possibles. Fixons l'aléa de $\mathcal{O}$ : ses requêtes deviennent des fonctions déterministes de $T_k$. Si chaque réponse est quantifiée sur $b$ bits, il y a au plus $2^{kb}$ transcriptions.

Soit une statistique finale $q : \mathcal{X} \to [0,1]$ choisie à partir de $T_k$, évaluée sur $n$ points. Alors, avec probabilité au moins $1-\beta$ :
$$
|q(D) - \mathbb{E}_P q| \le \sqrt{\frac{kb\ln 2 + \ln(2/\beta)}{2n}}.
$$
On peut aussi borner le biais moyen par $\sigma\sqrt{2\,I(T_k;D)}$ (Russo & Zou 2016, RAPPORTÉ), avec $I(T_k;D) \le H(T_k) \le kb$.

**Exemple chiffré (illustratif)**, avec $n = 10\,000$ et $\beta = 0{,}05$ :

| Configuration | Borne |
|---|---|
| 200 requêtes non adaptatives | $\sqrt{\ln(8000)/20\,000} \approx 0{,}021$ |
| Adaptatif, $k = 200$, $b = 1$ (« amélioration oui/non ») | $\approx 0{,}084$ |
| Adaptatif, $k = 200$, $b = 7$ (score arrondi au centième) | $\approx 0{,}22$, borne vide en pratique |

Ce qu'il faut retenir : **le levier, c'est le nombre de bits rendus, pas le nombre de requêtes**. La borne est un pire cas lâche. Elle dit quoi mesurer, pas la taille réelle du surapprentissage, qui reste à mesurer par X1.

### 1.3 Parades : garanties et coûts

| Parade | Ce qu'elle garantit (RAPPORTÉ) | Ce qu'elle coûte |
|---|---|---|
| Budget de requêtes $k$ | Borne de type §1.2 | Moins d'itérations. Ne borne rien si $b$ reste non borné. |
| Arrondi déterministe sur $b$ bits | Réduit $H(T_k)$. **N'est pas** de la confidentialité différentielle : les points proches d'une frontière d'arrondi fuient. | Perte de résolution, et de petites améliorations deviennent invisibles. |
| Bruit de Laplace sur une moyenne (sensibilité $1/n$) | $\varepsilon$-confidentialité différentielle par réponse. La confidentialité différentielle **implique la généralisation** (Dwork et al. 2015 ; Bassily et al. 2016). Composition avancée : $\varepsilon_{\mathrm{tot}} \approx \varepsilon\sqrt{2k\ln(1/\delta')} + k\varepsilon(e^\varepsilon - 1)$ (Dwork, Rothblum & Vadhan 2010). | Bruit d'échelle $1/(n\varepsilon)$ par réponse. On peut répondre à environ $\tilde O(n^2)$ requêtes statistiques adaptatives au lieu d'environ $n$ avec un découpage frais. |
| Thresholdout | Rend l'estimation sur la partie d'entraînement, sauf si elle s'écarte de la partie réservée de plus d'un seuil bruité. Le budget est consommé seulement par ces dépassements (Dwork et al., *Science* 2015). | Coupe $D_{\mathrm{val}}$ en deux. Il faut régler seuil et bruit. Le budget de dépassements s'épuise. |
| Ladder | Ne publie un nouveau score que s'il bat le meilleur d'une marge $\eta$. Garantie sur **l'exactitude du classement**, avec une erreur qui décroît à peu près en $n^{-1/3}$ à facteurs logarithmiques près (Blum & Hardt 2015, valeur exacte à vérifier dans l'article). | Ne protège que « le meilleur score », pas des requêtes arbitraires comme des probabilités par item. |
| Limite basse | Aucun mécanisme efficace ne répond correctement à beaucoup plus de $\sim n^2$ requêtes adaptatives (Hardt & Ullman 2014 ; Steinke & Ullman 2015). | Un budget fini est **inévitable**. Aucun dessin n'y échappe. |

**Point propre à E2.** Les probabilités par item sur $D_{\mathrm{val}}$ ne sont pas des requêtes statistiques, puisque chacune dépend d'un seul point. Elles échappent donc à Thresholdout comme à Ladder. **Hypothèse de dessin** : $I$ ne rend sur $D_{\mathrm{val}}$ que des **agrégats**. Les probabilités par item ne sont rendues que sur les textes construits par $\mathcal{O}$, qui ne contiennent rien de $D_{\mathrm{val}}$ ni de $D_{\mathrm{test}}$.

---

## 2. Dessin de (E2) (question 3) : deux variantes à départager

### 2.1 Primitives minimales

1. `encode(textes_O, couches, mise_en_commun) → poignée`. Les activations restent chez l'hôte : seule une poignée est rendue. Variante B-ouverte : on rend les activations des textes de $\mathcal{O}$, qui ne contiennent aucune information de test sauf mémorisation (a6), au prix d'un gros volume.
2. `fit_probe(poignée, étiquettes_O, couche, perte, régularisation, pas) → id_sonde + métrique sur une partition interne de données de O`.
3. `predict(id_sonde, poignée) → probabilités arrondies sur b bits`.
4. `generate(textes_O, max_jetons, graine) → textes`, à décodage fixé.
5. `score_val(artefact) → Ladder ou Thresholdout`. C'est le **seul** point de contact avec $D_{\mathrm{val}}$.
6. `commit(hash_protocole)` et `confirm(id_engagement)`. Voir §2.4.

### 2.2 Ce que l'hôte ne rend jamais

- les entrées, étiquettes et activations de $D_{\mathrm{test}}$ ;
- les probabilités par item sur $D_{\mathrm{val}}$ ;
- les durées non quantifiées ;
- les traces d'erreur brutes ;
- l'information de succès de cache.

Les erreurs sont ramenées à un petit alphabet fixe, par exemple 4 codes (illustratif). Les durées sont **remplies jusqu'à un palier**. Aucun cache n'est partagé entre les calculs sur $D_{\mathrm{test}}$ et ceux de $\mathcal{O}$.

### 2.3 Filtre des textes construits

Il y a deux voies, qui sont exclusives :

- **F-immédiat** : le filtre (correspondance exacte de $n$-grammes, MinHash à la Broder 1997, similarité d'embeddings) refuse au moment de la requête. C'est simple, mais c'est un oracle d'appartenance qui livre environ un bit par refus.
- **F-différé** : le filtre tourne en silence, les requêtes contaminées reçoivent une réponse factice, et **l'audit annule l'exécution** après coup. $\mathcal{O}$ n'apprend rien pendant l'exécution. Le prix, ce sont des exécutions perdues.

X3 départage ces deux voies.

### 2.4 Bornes, file d'exécution et préenregistrement

**Bornes.** Par itération et par exécution, on plafonne :
- le nombre de requêtes ;
- les jetons traités ;
- les secondes de carte graphique, réservées au pire cas (P2) ;
- les **bits rendus** $\sum b_i$, qui alimentent directement la borne du §1.2.

**File d'exécution.**
- Une file **synchrone** est simple à journaliser, et le temps d'attente est imputé au budget de $\mathcal{O}$.
- Une file **asynchrone** économise du temps mais rend observable l'ordre des réponses, qui devient un canal. Il faut alors une libération par lots, à heures fixes.

C'est un compromis ; je n'en recommande aucune par défaut.

**Préenregistrement.** Il passe par un schéma engagement / révélation :
- La phase d'**exploration** utilise E2 sur un réservoir de stimuli A.
- L'**engagement** porte sur le hash de (hypothèse, métrique, seuil, code d'analyse, taille). Le critère est pris dans un **gabarit fixé par Lazar** : $\mathcal{O}$ ne remplit que des champs.
- La **confirmation** s'exécute une seule fois sur un réservoir B. Ce réservoir est généré par un processus séparé, avec des graines scellées **après** l'engagement.
- Le résultat est rendu sur 1 bit (« confirmé / non confirmé ») plus la taille d'effet arrondie.

---

## (b) Expériences décisives (inférence forte, B4)

Tous les seuils sont **illustratifs**, sauf lorsqu'ils découlent explicitement d'un intervalle de confiance.

### X1 : $\mathcal{O}$ surapprend-il $D_{\mathrm{val}}$ ?

- **H_A** : l'écart $\Delta(k) = S_{\mathrm{val}} - S_{\mathrm{frais}}$ croît avec le nombre $k$ de scores vus.
- **H_B** : $\Delta(k)$ reste dans la fluctuation d'échantillonnage non adaptative.
- **Dispositif** : un **jeu frais $D_{\mathrm{frais}}$**, détenu par Lazar et interrogé une seule fois par exécution, distinct de $D_{\mathrm{test}}$ pour éviter a4.
- **Métrique** : la pente de $\Delta$ en fonction de $\log k$ sur au moins 5 exécutions (illustratif).
- **Seuil** : la borne inférieure de l'intervalle de confiance à 95 % de la pente est positive. L'intervalle s'obtient par bootstrap sur les items.
- **Contrôle négatif** : $\mathcal{O}$ propose ses $k$ candidats **avant** de voir le moindre score (non adaptatif). La pente doit être nulle.
- **Contrôle positif** : une attaque de type « boosting » à la Blum & Hardt sur des étiquettes aléatoires. Elle doit produire $\Delta > 0$, sinon la mesure est aveugle.
- **Falsification** :
  - une pente positive avec un contrôle négatif plat falsifie H_B ;
  - un intervalle qui contient 0 alors que le contrôle positif détecte bien falsifie H_A, à cette échelle de $k$.

### X2 : l'information de (E2) cause-t-elle le gain ?

- **H_A** : à budget égal, (E2) améliore $S_{\mathrm{frais}}$ **grâce au contenu** des réponses.
- **H_B** : le gain éventuel vient du calcul ou du temps supplémentaire, pas de l'information rendue.
- **Bras** :
  - E2 réelle ;
  - **E2 placebo**, avec des résultats permutés entre requêtes mais coûts et délais identiques ;
  - sans E2.
- **Métrique** : $S_{\mathrm{frais}}$ (réel) $- S_{\mathrm{frais}}$ (placebo).
- **Seuil** : une différence positive dont l'intervalle de confiance exclut 0.
- **Contrôle négatif** : le placebo lui-même. Son écart avec « sans E2 » mesure l'effet du seul budget.
- **Falsification** :
  - réel > placebo falsifie H_B ;
  - réel ≈ placebo falsifie H_A. Ce serait la preuve que $\mathcal{O}$ n'exploite pas les réponses, un résultat utile en soi.

### X3 : l'interface fuit-elle l'appartenance à $D_{\mathrm{test}}$ ?

- **H_A** : un adversaire qui observe tout ce que rend $I$ (réponses, refus, durées quantifiées, codes d'erreur) distingue les items de test des autres.
- **H_B** : il ne les distingue pas mieux que le hasard.
- **Dispositif** : un adversaire de type « équipe rouge » reçoit 200 textes candidats (illustratif), dont la moitié sont des quasi-copies d'items de test et l'autre moitié des textes appariés hors test, de même source et de même longueur.
- **Métrique** : l'aire sous la courbe ROC de l'inférence d'appartenance (au sens de Shokri et al. 2017).
- **Seuil** : la borne inférieure de l'intervalle de confiance à 95 % dépasse 0,5.
- **Contrôle négatif** : la même procédure sur un hôte où $D_{\mathrm{test}}$ est remplacé par un **jeu leurre** inconnu de l'adversaire. L'aire doit valoir 0,5.
- **Variantes** : F-immédiat contre F-différé, et cache partagé contre cache cloisonné.
- **Falsification** :
  - une aire significativement supérieure à 0,5 avec F-immédiat et environ 0,5 avec F-différé falsifie l'idée que le filtre immédiat est sûr ;
  - une aire d'environ 0,5 partout falsifie H_A pour cette surface d'attaque, et seulement pour elle.

### X4 : les sondes produites via (E2) mesurent-elles un concept ou un artefact ?

- **H_A** : la sonde de $\mathcal{O}$ est **sélective** : l'exactitude sur la tâche moins l'exactitude sur une **tâche de contrôle** (au sens de Hewitt & Liang) dépasse un seuil, sur des paires minimales construites par $\mathcal{O}$.
- **H_B** : l'exactitude s'explique par des traits de surface.
- **Contrôles négatifs** :
  - la même sonde sur un modèle à poids aléatoires de même architecture ;
  - une sonde « sac de mots » sur le texte brut.
- **Seuil** : sélectivité au-dessus de 0,10 (illustratif), et sonde réelle meilleure que la sonde « sac de mots » avec un intervalle de confiance qui exclut 0.
- **Falsification** :
  - si la sonde « sac de mots » égale la sonde sur activations, H_A est falsifiée ;
  - si la sélectivité dépasse le seuil alors que les contrôles restent au niveau du hasard, H_B est falsifiée.

C'est **l'expérience que (E1) ne permet pas** : c'est le cœur de a9.

### X5 : le préenregistrement contrôle-t-il les fausses confirmations ?

- **H_A** : quand $\mathcal{O}$ choisit lui-même son critère, son taux de fausses confirmations dépasse $\alpha$.
- **H_B** : avec un critère externe et un réservoir scellé, ce taux reste inférieur ou égal à $\alpha$.
- **Dispositif** : on **plante des hypothèses nulles**, c'est-à-dire des « directions » dont l'effet vrai est nul par construction (étiquettes aléatoires indépendantes du texte), mêlées à des hypothèses vraies plantées.
- **Métrique** : le taux de « confirmé » sur les nulles.
- **Seuil** : la borne de Clopper-Pearson à 95 % comparée à $\alpha = 0{,}05$.
- **Contrôle négatif** : le gabarit externe avec réservoir scellé, qui doit rester sous $\alpha$.
- **Contrôle de puissance** : les hypothèses vraies plantées doivent être confirmées dans au moins 80 % des cas (illustratif).
- **Falsification** :
  - un taux sous critère interne significativement supérieur à $\alpha$, avec un taux externe inférieur ou égal à $\alpha$, falsifie H_B pour le bras « critère interne » et valide le dessin du §2.4 ;
  - des taux égaux et inférieurs ou égaux à $\alpha$ dans les deux bras falsifient H_A : le préenregistrement serait alors un coût sans bénéfice mesurable.

### X6 : départager (E1), (E2) et le bras hors boucle (question 5)

Il y a trois bras à budget monétaire égal :
- **(E1)**, avec éventuellement un modèle substitut sur processeur ;
- **(E2)** ;
- **hors boucle préenregistré** (coût humain compté).

**Métrique principale** : le nombre d'**hypothèses confirmées sur réservoir scellé** par unité de coût, en tenant compte des fausses confirmations mesurées comme dans X5.

**Métrique secondaire** : $S_{\mathrm{frais}}$.

Pour respecter B4, je découpe en deux duels exclusifs :

- **Duel 6a.**
  - H_A : (E2) produit plus de confirmations valides par unité de coût que (E1).
  - H_B : (E1) en produit autant ou plus, ce qui voudrait dire que le substitut sur processeur transfère.
  - Contrôle négatif : le bras (E1) **sans** substitut, qui ne peut tester aucune hypothèse portant sur le modèle de 8 milliards et doit donc avoir un taux de confirmation nul sur cette classe d'hypothèses.
- **Duel 6b.**
  - H_A : (E2) fait mieux que le bras hors boucle.
  - H_B : non.
  - Ce duel ne se juge qu'**après X3 et X5** : si l'interface fuit ou si le préenregistrement échoue, le gain de (E2) n'est pas interprétable.

---

## (c) Instruments : la mesure minimale qui dit s'ils fonctionnent

Pour chaque instrument, on oppose des cas d'attaque à des cas honnêtes appariés, et on compare à une vérification mécanique simple qu'il faut battre.

| Instrument nommé | Cas positifs (détection) | Cas honnêtes appariés (fausses alertes) | Vérification mécanique à battre |
|---|---|---|---|
| **Thresholdout** | Analyste adaptatif agressif (contrôle positif de X1) : on mesure la fraction de requêtes surajustées dont l'écart reste au-dessus de α | Analyste non adaptatif sur les mêmes requêtes : on mesure le taux de réponses inutilement bruitées | Découpage frais par lot de requêtes. Si Thresholdout ne fait pas mieux à $n$ égal, il ne sert à rien ici. |
| **Ladder** | Attaque de type « boosting » : on mesure la fraction des progrès illusoires publiés | Améliorations réelles plantées d'au moins $\eta$ : on mesure la fraction de vrais progrès masqués | Arrondi du score au pas $\eta$ sans règle de publication. |
| **Bruit / confidentialité différentielle** | Même attaque : on mesure le $\Delta$ résiduel | Analyste honnête : on mesure la perte d'exactitude due au bruit | Arrondi déterministe sur $b$ bits à budget de bits égal. |
| **Budget de requêtes / bits** | Attaque à budget plein : on mesure le $\Delta$ observé par rapport à la borne du §1.2 | Optimisation honnête : on mesure la fraction d'exécutions stoppées par le budget avant convergence | Simple plafond sur $k$ sans compter les bits. |
| **Filtre anti-copie** | Paraphrases, traductions aller-retour, troncatures d'items de test : on mesure le taux de détection | Textes de même source et de même longueur hors test : on mesure le taux de faux refus | Correspondance exacte de 13-grammes (illustratif) et MinHash. Un filtre par embeddings doit détecter plus de paraphrases sans plus de faux refus. |
| **Sonde linéaire (« direction »)** | Concepts plantés connus | Tâches de contrôle et étiquettes permutées : on mesure la sélectivité | Sonde « sac de mots » et sonde sur modèle à poids aléatoires. |
| **Préenregistrement** | Nulles plantées (X5) : on mesure le taux de fausses confirmations | Vraies plantées : on mesure la puissance | Comparaison textuelle mécanique entre protocole engagé et protocole exécuté. Elle détecte la dérive de critère sans aucun modèle. |
| **Juge / revue par modèle de langue** (pour la « revue complaisante ») | Hypothèses fausses plantées, rédigées par $\mathcal{O}$ : on mesure le taux de rejet | Hypothèses vraies : on mesure le taux d'acceptation | Simple test statistique préenregistré sur le réservoir B. Si le juge n'ajoute rien au test, il ajoute surtout du biais d'auto-préférence (Panickssery et al. 2024, RAPPORTÉ). |
| **Palier de durée et codes d'erreur** | Attaque X3 sur le canal temporel : on mesure l'aire sous la courbe ROC | Requêtes appariées hors test | Mesure de l'information mutuelle entre appartenance et durée sur un hôte sans palier. |

---

## (d) Ancrage matériel (tout est **illustratif** : aucun fait n'est fourni)

**Modèles ouverts d'environ 8 milliards de paramètres** : Llama-3.1-8B (Meta, 2024), Qwen3-8B (Alibaba, 2025), et OLMo-2 (Allen AI ; taille exacte et données ouvertes à vérifier). Le fait que les données d'entraînement d'OLMo soient publiques permettrait de **tester a6 directement**, c'est-à-dire la présence de $D_{\mathrm{test}}$ dans le corpus d'entraînement. Les versions et dimensions sont à vérifier.

**Calcul.**
- Une passe avant coûte environ $2N$ FLOP par jeton, soit environ $1{,}6\times 10^{10}$ pour $N = 8\times 10^9$.
- Pour $10^6$ jetons, cela fait environ $1{,}6\times 10^{16}$ FLOP. À un débit effectif de $10^{14}$ FLOP/s (illustratif), il faut environ 160 s de carte graphique.
- Les poids en bf16 occupent environ 16 Go, ce qui tient sur une carte de 24 à 80 Go.

**Stockage.** Avec une dimension cachée de 4096 (à vérifier) et une mise en commun par texte, une couche demande environ 8 Ko par texte. Pour $10^5$ textes sur 32 couches, cela fait environ 26 Go.

**Sondes.** Une régression logistique sur $10^5 \times 4096$ s'entraîne en quelques secondes à quelques minutes sur processeur. Elle peut donc s'exécuter sous (E1) si les activations sont rendues : c'est la variante B-ouverte.

**Coûts par expérience** (prix d'une heure de carte graphique fixé à 2 €, illustratif) :

| Expérience | Calcul dominant | Ordre de grandeur |
|---|---|---|
| X1 | 5 exécutions de $\mathcal{O}$, plus le contrôle positif | Dominé par les appels aux modèles de langue de $\mathcal{O}$ ; impossible à estimer sans le tarif |
| X2 | 3 bras × 5 exécutions | Environ 3 fois X1 |
| X3 | 200 candidats, 4 variantes d'hôte | Moins d'une heure de carte graphique |
| X4 | Environ $10^4$ paires minimales × 3 sondes × 32 couches | Quelques heures de carte graphique, soit quelques dizaines d'euros |
| X5 | Environ 100 hypothèses plantées × 2 bras | Faible en calcul ; coûteux en conception du gabarit |
| X6 | 3 bras, plus le temps humain du bras hors boucle | Dominé par le **temps humain** : à chiffrer par Lazar |

**Temps.** En file synchrone, le temps d'une itération vaut au minimum le temps de génération de $\mathcal{O}$ plus l'attente de la carte graphique.

**Ordre recommandé : X3 → X5 → X4 → X1 → X2 → X6.** Les deux premières valident l'interface ; sans elles, les autres ne sont pas interprétables.

---

## Références (question 4)

Je ne cite que celles que je peux attribuer. Aucun identifiant n'est donné.

**Analyse adaptative et validation réutilisable**
- Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015). *The reusable holdout: Preserving validity in adaptive data analysis*. Science.
- Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015). *Preserving Statistical Validity in Adaptive Data Analysis*. STOC.
- Blum, Hardt (2015). *The Ladder: A Reliable Leaderboard for Machine Learning Competitions*. ICML.
- Hardt, Ullman (2014). *Preventing False Discovery in Interactive Data Analysis Is Hard*. FOCS.
- Steinke, Ullman (2015). *Interactive Fingerprinting Codes and the Hardness of Preventing False Discovery*. COLT.
- Bassily, Nissim, Smith, Steinke, Stemmer, Ullman (2016). *Algorithmic Stability for Adaptive Data Analysis*. STOC.
- Russo, Zou (2016). *Controlling Bias in Adaptive Data Analysis Using Information Theory*. AISTATS.
- Dwork, Rothblum, Vadhan (2010). *Boosting and Differential Privacy*. FOCS.
- Dwork, Roth (2014). *The Algorithmic Foundations of Differential Privacy*. Foundations and Trends in TCS.
- Zrnic, Hardt (2019). *Natural Analysts in Adaptive Data Analysis*. ICML. Référence à vérifier.

**Réutilisation de jeux de test, flexibilité analytique, préenregistrement**
- Recht, Roelofs, Schmidt, Shankar (2019). *Do ImageNet Classifiers Generalize to ImageNet?* ICML.
- Simmons, Nelson, Simonsohn (2011). *False-Positive Psychology…* Psychological Science.
- Nosek, Ebersole, DeHaven, Mellor (2018). *The preregistration revolution*. PNAS.
- Platt (1964). *Strong Inference*. Science.

**Agents de recherche et revue par modèles de langue**
- Lu, Lu, Lange, Foerster, Clune, Ha (2024). *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*.
- Si, Yang, Hashimoto (2024). *Can LLMs Generate Novel Research Ideas?…*
- Zheng et al. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. NeurIPS.
- Panickssery, Bowman, Feng (2024). *LLM Evaluators Recognize and Favor Their Own Generations*.

**Contamination**
- Sainz et al. (2023). Sur la contamination des jeux d'évaluation. Titre exact à vérifier.

**Spécification de récompense et optimisation contre un mesureur**
- Amodei, Olah, Steinhardt, Christiano, Schulman, Mané (2016). *Concrete Problems in AI Safety*.
- Gao, Schulman, Hilton (2023). *Scaling Laws for Reward Model Overoptimization*. ICML.
- Manheim, Garrabrant (2018). *Categorizing Variants of Goodhart's Law*.
- Krakovna et al. sur le « specification gaming » : référence à vérifier.

**Sondes**
- Alain, Bengio (2016). *Understanding intermediate layers using linear classifier probes*.
- Hewitt, Liang (2019). *Designing and Interpreting Probes with Control Tasks*. EMNLP.
- Belinkov (2022). *Probing Classifiers: Promises, Shortcomings, and Advances*. Computational Linguistics.

**Canaux auxiliaires et filtrage**
- Lampson (1973). *A Note on the Confinement Problem*. CACM.
- Kocher (1996). Attaques temporelles. CRYPTO.
- Shokri, Stronati, Song, Shmatikov (2017). *Membership Inference Attacks Against Machine Learning Models*. IEEE S&P.
- Broder (1997). *On the resemblance and containment of documents*.

---

## Ce qui réfuterait les thèses propres à cette proposition B

1. **« Le levier, ce sont les bits, pas les requêtes. »** Réfutée si, dans X1, $\Delta$ croît avec $k$ à $b$ fixé autant qu'avec $b$ à $k$ fixé.
2. **« Le filtre immédiat fuit. »** Réfutée si X3 donne une aire sous la courbe d'environ 0,5 avec F-immédiat.
3. **« (E1) ne lève pas la limite. »** Réfutée si, dans le duel 6a, le substitut sur processeur produit autant de confirmations valides sur le modèle de 8 milliards que (E2).
4. **« L'arbitre est un canal vers $D_{\mathrm{test}}$. »** Réfutée si la procédure réelle n'évalue qu'une exécution sur $D_{\mathrm{test}}$. Ce fait n'est pas fourni ; Lazar peut le confirmer ou l'infirmer.

FIN-DE-CELLULE