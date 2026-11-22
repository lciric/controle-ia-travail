# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHaAyyjbRCivhYTGK9LP`
- Heure (UTC) : 2026-11-22T07:33:02Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-16-theoreme-negatif-refonte-v1.md` — sha256 0b0207ab69cc4368349ce212241a96f8f79e4e5453c751b761ca15bd1532c926 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/seconde-lecture-these-v1.md` — sha256 a4f751ce3981aa100d026e9b90a9214897f639717bdcc9c31a5680d32cfcfdf4 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 2091e94778de0c11642ee6d0ae3515102ed50b06846dca2abc4a54c56b588e47
- Jetons : entrée 22194, sortie 24888 (dont réflexion 14619), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.173072 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 16 — le théorème négatif contredit : réponse approfondie

**Conclusion d'abord.** Aucune des trois voies ne donne un théorème neuf à mettre en titre. Elles donnent trois énoncés qui tiennent, à citer ou à poser en propositions de cadrage.
- **Corriger** : l'aveuglement exact se réduit aux mélanges de décisions sur un seul pas. Énoncé élémentaire, bon pour une phrase et une note.
- **Refondre** : la dépendance obéit au même bilan que la position, compté en paires et en trajectoires. C'est le modèle nul du papier B.
- **Nouveau** : sous référence par régime, le dommage caché croît linéairement avec l'horizon pour tout test, et la référence jumelle lève ce plancher avec une validité exacte. C'est l'énoncé qui sert le mieux la thèse retenue, et il est probablement occupé dans sa forme.

Confiance d'ensemble : 0,55.

**Réserves.**
- Je n'ai lu aucun PDF. Les notes de lecture jointes sont mon seul accès aux pages.
- Les dérivations ci-dessous sont de ma main et non vérifiées.
- Les antériorités ajoutées sont de mémoire : « rapporté, non vérifié sur PDF ».
- Je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Caractériser la classe aveugle au lieu de lister des statistiques aveugles** [PROPOSITION]. La bonne question est : quels tests ont une puissance égale au taux de fausses alertes contre toute loi jointe à marginales fixées ?
- **Séparer trois niveaux** [PROPOSITION] : aveuglement exact, aveuglement en espérance (premier ordre), aveuglement asymptotique. L'énoncé contredit les confondait.
- **Casser chaque énoncé sur un cas fini avant de l'écrire** [PROPOSITION] : deux ou trois pas, scores à trois valeurs, calcul exact.
- **Vérifier que le nul honnête n'est pas échangeable entre pas** [FAIT RAPPORTÉ] : autocorrélation honnête de 0,064 (note, 2606.10456, p. 8) et dépendance positive entre commits (recherche, 2607.07368, p. 45). Un nul par permutation des pas serait donc faux.
- **Relire la preuve de la proposition 1 de 2606.10456** [PROPOSITION]. La note y signale un pas faux à horizon fini ; un second lecteur doit le confirmer avant toute phrase publique.
- **Parcourir les arbres de citations restés en échec** [FAIT RAPPORTÉ, recherche, § 1] : Ker 2006 et 2007, Arias-Castro 2012, Avenhaus.

## 2. Données brutes de départ

- Les pages : Arias-Castro et collaborateurs 2012, p. 2, 14-15, 18-20 ; 2606.10456, preuve p. 3 et tableau p. 7 ; Filler, Ker, Fridrich 2009, p. 4-5 ; Ker 2010, p. 13-15.
- Les activations brutes et les scores de sonde et de juge pas à pas, sur des exécutions honnêtes jumelles, avec identifiants de tâche, d'exécution et rang du pas.
- Les mêmes sur les organismes saboteurs, avec le dommage planté par pas.
- Le code de l'attaque synthétique de 2606.10456, s'il est public.

## 3. Méthodes et outils

- **Programme linéaire sur le polytope des lois jointes à marginales fixées** : pour un test donné, calculer la puissance minimale et maximale. Le verdict « aveugle ou non » est alors exact.
- **Décomposition de Hoeffding** (analyse de variance fonctionnelle) de la fonction de test : composante additive, puis interactions.
- **Simulation** par copule gaussienne (autorégressive, équicorrélée, corrélation négative) aux horizons 24, 300 et 400 de 2606.10456.
- **Modèle à composantes de variance** (tâche, exécution, pas), rééchantillonnage par tâche.
- **Test de rang parmi les jumelles** (valeur p conforme), et données de substitution par échange de jumelles plutôt que par permutation des pas.
- **Test du rapport de variances** pour la somme au carré, et grille à deux entrées (horizon, référence) sur les autocovariances.

## 4. Ce qui vérifie hors du directeur et de Claude

- Le programme linéaire : un contre-exemple numérique ne dépend d'aucun avis.
- Un statisticien de la détection de dépendances, pour la voie 1 et la frontière de la voie 2.
- Un spécialiste de stéganalyse, sur la référence fautive et l'écart de source de couverture (voie 3).
- Un second lecteur des pages décisives.
- L'essai « jumeau contre jumeau » : uniformité des rangs, mesure de l'écart entre tâches.
- La prévision scellée, puis une seconde famille de modèles.
- Le collisionneur, sur la question neutre, après test de devinette.

---

## Demande reformulée

« Le théorème négatif du programme ("toute statistique de marginales a une puissance égale au taux de fausses alertes contre une attaque qui préserve la marginale") est contredit par Arias-Castro, Bubeck, Lugosi 2012 et occupé en boîte noire par 2606.10456. Pour chacune des trois voies (corriger, refondre, nouveau) : (1) écris un énoncé candidat à horizon fini, avec ses hypothèses, dans les unités du programme (pas, exécutions, tâches, taille de référence m, horizon n) ; (2) dis quelle classe exacte de tests il concerne, et prouve-le ou casse-le d'abord sur un cas fini calculable ; (3) nomme ce qui l'occupe déjà, statut "rapporté, non vérifié sur PDF" ; (4) donne l'épreuve qui le réfuterait, sur calcul exact, sur simulation et sur les exécutions honnêtes jumelles, sans avis d'expert ; (5) dis ce qu'il apporte à la thèse retenue (loi héritée comme modèle nul, bilan mesuré chez des agents, complémentarité en second axe) et ce qu'une issue négative laisserait. Classe les trois voies. Ne revendique aucune zone vierge. »

---

## Réponse

### Voie 1 — Corriger : l'aveuglement exact et sa classe

**Énoncé candidat** [HYPOTHÈSE, dérivation de ma main, sûre en cas fini, à faire vérifier].

Soit P la loi honnête de n scores, de support plein. Soit la classe des lois jointes ayant les mêmes marginales pas par pas.

- **(1a) Caractérisation.** Un test a une puissance égale à son taux de fausses alertes contre toute loi de cette classe si et seulement si sa fonction de test est additive : une constante plus une somme de fonctions d'un seul score. C'est, de façon équivalente, un mélange aléatoire de décisions prises chacune sur un seul pas.
- **(1b) Premier ordre.** Pour toute statistique additive, l'espérance est inchangée. Le seuil posé sur cette statistique n'est pas additif, donc pas aveugle.
- **(1c) Signe.** Pour la somme seuillée à un taux inférieur à un demi, une dépendance positive donne une puissance supérieure au taux de fausses alertes et une dépendance négative une puissance inférieure. Un saboteur à marginale préservée peut donc rendre la somme pire qu'aveugle.
- **(1d) Forme exacte de l'énoncé d'origine.** Toute statistique symétrique (moyenne, maximum, queue, compteur de seuil) est exactement aveugle si l'attaque préserve la loi du multi-ensemble des scores, c'est-à-dire si elle ne fait que réordonner des scores honnêtes. La puissance vient alors de l'ordre seul.

**Esquisse de preuve de (1a)** [HYPOTHÈSE]. En cas fini, les écarts entre une loi de la classe et P engendrent les mesures signées à marginales nulles. Leur orthogonal est l'espace des fonctions additives. Une fonction additive à valeurs entre 0 et 1 se réécrit en mélange de tests sur un seul pas. Le cas continu demande une condition de fermeture, à vérifier.

**Hypothèses.** Support plein de la loi honnête ; classe d'attaque complète (toutes les lois à marginales préservées). Si la classe est restreinte, par exemple aux copules gaussiennes, la classe aveugle peut être plus large.

**Lecture de la contradiction.**
- [FAIT RAPPORTÉ, seconde lecture, § 2] Chez Arias-Castro et collaborateurs, la somme au carré et le test d'histogramme gardent de la puissance à marginales identiques.
- [HYPOTHÈSE] (1a) l'explique : ces tests ont des composantes d'interaction de Hoeffding non nulles.
- [FAIT RAPPORTÉ, seconde lecture, § 4] La proposition 1 de 2606.10456 pose la répartition empirique égale à l'honnête « par définition », et son tableau affiche 0,048 de puissance à 1 %.
- [HYPOTHÈSE] (1d) est la condition sous laquelle cette proposition serait exacte. Cette lecture est la nôtre, à confirmer.

**Ce qui l'occupe** [rapporté, non vérifié sur PDF, sauf mention].
- Dualité du problème des marges : Kellerer, 1984, « Duality theorems for marginal problems » ; Strassen, 1965, « The existence of probability measures with given marginals ».
- Décomposition : Hoeffding, 1948, « A class of statistics with asymptotically normal distribution » ; Efron et Stein, 1981, « The jackknife estimate of variance ».
- Marginales et copule : Sklar, 1959 (déjà cité dans la réponse 9).
- Invariance par permutation pour (1d) : Lehmann et Stein, 1949, « On the theory of some non-parametric hypotheses » ; Hoeffding, 1952, « The large-sample power of tests based on permutations of observations ».
- En contrôle : 2606.10456, 2607.11751, 2610.13083 [FAIT RAPPORTÉ, recherche, § 4].

Chance que (1a) soit neuf en mathématiques : 0,05. Chance qu'il soit déjà écrit sous cette forme pour des moniteurs d'agents : inconnue, c'est une question.

**Épreuve qui le réfuterait.**
- Programme linéaire, trois pas, scores à trois valeurs : pour la somme seuillée, le maximum, un compteur de seuil et un mélange de tests sur un pas, calculer la puissance minimale et maximale sur la classe. (1a) prédit l'égalité pour le mélange seul. Un seul test non additif à puissance constante le réfute.
- Simulation à horizon 24 et 300 : la somme seuillée doit s'écarter du taux nominal dans le sens de (1c).

**Apport au papier.** Une phrase juste (« l'espérance des statistiques additives est inchangée ; seul un mélange de décisions par pas est exactement aveugle ») et une note. Aucun résultat à revendiquer. Une issue négative ne laisserait rien de plus que la phrase.

---

### Voie 2 — Refondre : le bilan au second ordre

L'idée est de remplacer « les marginales sont aveugles » par « voici ce que coûte la détection par la dépendance, dans les mêmes unités que la loi héritée ».

**Énoncé candidat** [HYPOTHÈSE].

- **(2a) Statistiques locales.** Une autocovariance, ou une covariance entre copies, est une moyenne de produits : une statistique additive sur des paires. Le bilan hérité s'y applique en comptant des paires. L'écart de dépendance détectable est d'ordre z·s·√(1/n + 1/m) + τ_d, où s est l'écart-type des produits, n et m les nombres de paires surveillées et de référence, et τ_d l'écart-type entre tâches de la dépendance honnête.
- **(2b) Statistique dense.** La somme au carré d'une trajectoire ne porte qu'un degré de liberté. Avec R trajectoires surveillées et r trajectoires de référence, le gonflement relatif de variance détectable est d'ordre z·√(2/R + 2/r). Allonger la trajectoire n'y change rien. L'unité est la trajectoire ou la copie, non le pas.
- **(2c) Frontière.** Pour N scores dont k sont co-élevés avec une corrélation ρ, la somme au carré n'est puissante que si ρ·k²/N est grand. En régime rare, il faut un test de répartition.
- **(2d) Hiérarchie.** Une attaque qui préserve les lois des paires est aveugle aux statistiques additives de paires, et ainsi de suite jusqu'à la préservation complète, indétectable.

**Hypothèses.**
- Moments d'ordre quatre finis.
- Dépendance honnête à mémoire courte.
- Dépendance honnête stable entre tâches (τ_d petit), à mesurer et non à supposer.
- Référence non nourrie par l'agent jugé [FAIT RAPPORTÉ, recherche, 2411.17693, p. 18].

**Ce qui l'occupe.**
- [FAIT RAPPORTÉ, seconde lecture] (2c) est Arias-Castro et collaborateurs 2012, propositions 3.1 et 3.5.
- [FAIT RAPPORTÉ, seconde lecture] Le détecteur par paires consécutives et sa loi en racine sont dans Filler, Ker, Fridrich 2009, p. 5 ; la phrase de (2d) y est p. 4.
- [FAIT RAPPORTÉ, seconde lecture] La consistance de l'autocorrélation est dans 2606.10456, proposition 2, en boîte noire.
- [FAIT RAPPORTÉ, recherche] En empirique : alignement d'activations entre agents (2604.01151, p. 17) ; détecteur de comptes qui bougent ensemble (2610.13083).
- [rapporté, non vérifié sur PDF] Borne de préservation complète : Cachin, 1998, « An information-theoretic model for steganography ». Arias-Castro, Bubeck, Lugosi, 2015, « Detecting positive correlations in a multivariate sample ».
- (2b) est le test classique du rapport de variances.

Chance que (2a)-(2b), avec référence estimée et terme entre tâches, soient déjà écrits pour des scores de sondes : question ouverte. L'arbre des citants d'Arias-Castro 2012 n'a pas été parcouru. Chance d'un contenu propre après recherche : 0,3 comme énoncé, 0,5 comme mesure.

**Épreuve qui le réfuterait.**
- Sur les jumelles honnêtes, sous-échantillonner n et m pour l'autocovariance au premier retard et pour la covariance entre copies. (2a) prédit une surface de seuil en √(1/n + 1/m), puis un palier τ_d.
- Si τ_d domine dès les petits horizons, la voie de la dépendance est inutilisable sous référence par régime. Ce serait un résultat négatif publiable.
- Sur les organismes : test de position contre test de dépendance, étalonnés par échange de jumelles. Si le sabotage joué ne déplace que la marginale, la voie 2 sort de A et reste un nul pour B.

**Apport.** Le modèle nul du papier B (quelle taille d'essaim et quelle corrélation rendent la co-élévation détectable) et une section de diagnostic de A. Limite [FAIT RAPPORTÉ, N-077] : on mesure ce que font les organismes, non un saboteur optimal.

---

### Voie 3 — Nouveau : le plancher linéaire d'hétérogénéité et sa levée par le jumeau

C'est un théorème négatif sur la référence, non sur les marginales. Il donne un statut formel au terme que la réponse 9 désigne comme l'inconnue principale.

**Énoncé candidat** [HYPOTHÈSE, dérivation de ma main].

Modèle : le score au pas t de la tâche j vaut un niveau commun, plus un effet de tâche gaussien d'écart-type τ, plus un bruit stationnaire de variance de long terme σ², plus δ fois le dommage du pas. Le saboteur étale un dommage total D à débit constant.

- **(3a) Négatif.** Avec une référence par régime, même infinie, tout test sur la trajectoire surveillée, de quelque ordre qu'il soit, a une puissance bornée par celle du test sur la moyenne. Le dommage caché à puissance donnée vaut D* = (z/δ)·√(τ²·n² + σ²·n). Il est linéaire en n dès que n dépasse σ²/τ². Une référence finie ajoute σ²·n²/m sous la racine. Raison : un sabotage à débit constant a exactement la forme d'un effet de tâche. Le temps n'accumule aucune preuve contre lui.
- **(3b) Positif.** Si l'exécution surveillée et r jumelles honnêtes de la même tâche sont échangeables sous l'hypothèse honnête, le rang de toute statistique parmi les r + 1 est uniforme. La statistique peut être de position, de dépendance, une sonde, un juge ou leur jonction. Le test est exact sans hypothèse sur la dépendance entre pas ni sur la dérive. Dans le modèle gaussien, le plancher redevient D* = (z/δ)·√(σ²·n·(1 + 1/r)).
- **(3c) Prix.** Le niveau le plus fin par tâche est 1/(r + 1). L'exactitude ne dit rien de la puissance. La classe aveugle restante est celle des attaques dont la loi de trajectoire égale la loi jumelle.

**Hypothèses.**
- Effet de tâche additif et gaussien. Sans gaussianité, (3a) ne vaut que pour la somme.
- Sabotage à débit constant, de même forme que l'effet de tâche.
- Ni jumelle ni audit dans (3a).
- Dans (3b), harnais strictement identique entre jumelles : graines indépendantes, aucun cache ni ordre partagé.

**Ce qui l'occupe.**
- [FAIT RAPPORTÉ, réponse 9 d'après la note] Référence fautive et loi linéaire : Ker 2010, p. 13 et 15. C'est le parent direct de (3a).
- [rapporté, non vérifié sur PDF, mémoire incertaine] Écart de source de couverture : Ker et Pevný, 2014, « A mishmash of methods for mitigating the model mismatch mess » ; Giboulot, Cogranne et collaborateurs, 2020, « Effects and solutions of cover-source mismatch in image steganalysis ».
- [rapporté, non vérifié sur PDF] Erreurs systématiques qui ne se moyennent pas : Avenhaus et Jaech, 1981 ; Moulton, 1990, « An illustration of a pitfall in estimating the effects of aggregate variables on micro units » ; Meng, 2018, déjà cité par le programme.
- [rapporté, non vérifié sur PDF] Pour (3b) : Fisher, 1935, « The design of experiments » (plans appariés) ; Lehmann et Stein, 1949 ; Bates, Candès, Lei, Romano, Sesia, 2023, « Testing for outliers with conformal p-values » ; Vovk, 2021, « Testing randomness online ».
- [FAIT RAPPORTÉ, recherche] En contrôle : martingales de test conformes dans 2610.13083, p. 5 ; tâches corrélées laissées ouvertes dans 2411.17693, p. 10.

Chance que (3a) soit neuf comme théorème : 0,15. Chance que (3b) soit neuf comme méthode : 0,05. Chance que le couple, avec τ et σ mesurés sur des scores de sondes, reste propre après recherche : 0,45.

**Épreuve qui le réfuterait.**
- Essai « jumeau contre jumeau » : estimer τ et σ, intervalle par rééchantillonnage des tâches. Si τ est indiscernable de zéro, (3a) est vide et se retire.
- Même essai : uniformité des rangs entre jumelles (test de Kolmogorov). Une non-uniformité réfute l'hypothèse de (3b) et révèle un défaut du harnais.
- Dommage planté à débit constant, référence par régime : la courbe du dommage non détecté selon n doit passer de la racine au linéaire vers n ≈ σ²/τ². Si une statistique de forme sépare le sabotage de l'effet de tâche mieux que prévu, l'hypothèse « même forme » tombe.
- Rapport sonde sur juge : (3a) prédit que la sonde ne change le régime linéaire que par τ/δ. Si le score de sonde a un τ plus faible à δ égal, c'est un avantage propre à l'accès interne, à mesurer.

**Apport.**
- Il fonde la comparaison « référence par régime contre par tâche » (réponse 9, décision 4, option c).
- Il fournit la « source de validité » exigée par N-076 : l'échangeabilité construite par le défenseur.
- Il donne à la complémentarité un test exact, par le rang de la statistique jointe.
- Une issue négative (τ nul) laisse une note de dimensionnement.
- Coût : r jumelles par tâche, indisponibles pour une tâche nouvelle sauf exécution parallèle.

---

### Classement

[PROPOSITION]

| Voie | Statut conseillé | Chance d'un contenu propre | Ce qu'une issue négative laisse |
|---|---|---|---|
| 3. Plancher d'hétérogénéité et jumeau | Proposition de cadrage de A, attribuée, avec mesure | 0,45 | Règle de dimensionnement |
| 2. Bilan au second ordre | Modèle nul de B ; diagnostic dans A | 0,3 à 0,5 | « La dépendance ne porte pas sous référence par régime » |
| 1. Aveuglement exact caractérisé | Une phrase et une note, citées | 0,05 | La phrase corrigée |

**Ce qui me ferait changer.**
- Un contre-exemple au programme linéaire : la voie 1 se réécrit.
- Un τ nul : la voie 3 se retire.
- Une lecture de Ker 2010, p. 13-15, qui contiendrait déjà l'effet aléatoire : la voie 3 devient une citation.

**Phrases à ne pas écrire** [PROPOSITION].
- « Théorème négatif du programme ».
- « Toute statistique de marginales est aveugle ».
- « La proposition 1 de 2606.10456 est fausse », avant second lecteur.
- « Nouveau théorème » pour l'une des trois voies.

---

## Question neutre pour le collisionneur

« On observe une suite de n nombres réels, un par étape d'un long processus, parfois pour plusieurs processus menés en parallèle. Deux situations sont possibles. Dans les deux, chaque nombre pris isolément suit exactement la même loi ; tout le reste peut différer. On dispose aussi d'un échantillon fini de m nombres issus de processus dont on sait qu'ils relèvent de la première situation, menés sur des tâches qui peuvent être différentes de la tâche observée ou identiques à elle.

1. Quelles règles de décision ont, ou n'ont pas, une probabilité de détection différente de leur taux de fausses alertes ? Donnez des énoncés à n fini, avec preuve ou contre-exemple.
2. Que change le fait que l'échantillon de comparaison soit fini, et qu'il vienne de la même tâche ou d'autres tâches ?
3. Comment la quantité d'écart entre les deux situations qui reste indécelable varie-t-elle avec n et m ? Précisez vos hypothèses.
4. Quels travaux publiés traitent déjà ces points (auteurs, année, titre, degré de certitude) ?
5. Quel calcul exact ou quelle simulation d'un jour départagerait vos réponses ? »

---

## Décisions qui reviennent au directeur

**Décision 1 — Fixer la place des trois énoncés dans les papiers.**
- *Enjeu.* Le directeur a retiré le théorème négatif comme résultat ; il faut dire ce qui le remplace sans recréer une revendication fragile.
- *Option a : aucun théorème en titre ; voie 1 en phrase citée, voie 3 en proposition de cadrage de A avec mesure, voie 2 en modèle nul de B.* Avantage : cohérent avec la thèse retenue, rien à rétracter. Inconvénient : papier de mesure, sans apport théorique affiché.
- *Option b : voie 3 en théorème principal de A.* Avantage : un énoncé « pour tout test ». Inconvénient : parent direct probable (Ker 2010, référence fautive) ; chance de nouveauté 0,15.
- *Option c : aucune théorie, citations seules.* Avantage : risque nul. Inconvénient : la comparaison des deux références perd son cadre.
- *Recommandation.* Option a. Confiance : 0,6.

**Décision 2 — Vérifier avant de sceller.**
- *Enjeu.* Les trois énoncés sont de ma main ; l'énoncé précédent a été scellé puis contredit.
- *Option a : programme linéaire et simulation (un jour), puis relecture par un statisticien, puis scellement.* Avantage : un contre-exemple est trouvé à bas coût. Inconvénient : quelques jours.
- *Option b : statisticien seul.* Avantage : autorité. Inconvénient : délai, et un avis reste un avis.
- *Option c : sceller maintenant.* Avantage : aucun retard. Inconvénient : même risque qu'hier.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 3 — Traiter la réserve sur la proposition 1 de 2606.10456.**
- *Enjeu.* Notre lecture y voit un pas faux à horizon fini ; le programme cite ce travail comme occupant.
- *Option a : second lecteur sur la page 3, puis citation avec une réserve neutre (« exacte si la loi du multi-ensemble est préservée »).* Avantage : juste et sobre. Inconvénient : une lecture de plus.
- *Option b : écrire aux auteurs.* Avantage : vérification à la source. Inconvénient : délai, exposition du programme.
- *Option c : citer sans remarque.* Avantage : simple. Inconvénient : on hérite d'un énoncé que nos propres notes contredisent.
- *Recommandation.* Option a, puis b si le second lecteur confirme. Confiance : 0,65.

**Décision 4 — Fixer le nombre de jumelles de l'essai « jumeau contre jumeau ».**
- *Enjeu.* La voie 3 exige r jumelles par tâche ; le niveau le plus fin par tâche est 1/(r + 1), et le coût croît avec r.
- *Option a : r = 4 sur beaucoup de tâches.* Avantage : bonne estimation de τ. Inconvénient : niveau par tâche grossier ; il faut combiner entre tâches.
- *Option b : r = 19 sur peu de tâches.* Avantage : niveau de 5 % par tâche. Inconvénient : τ mal estimé.
- *Option c : plan mixte, scellé.* Avantage : mesure τ et vérifie l'uniformité des rangs. Inconvénient : analyse plus lourde.
- *Recommandation.* Option c. Confiance : 0,5 ; elle dépend du budget d'exécutions, que je ne connais pas.

**Décision 5 — Achever les arbres de citations avant d'écrire « non trouvé ».**
- *Enjeu.* Les citants d'Arias-Castro 2012, de Ker 2006-2007 et d'Avenhaus n'ont pas été parcourus ; les voies 2 et 3 en dépendent.
- *Option a : parcours ciblé maintenant (Arias-Castro 2012 ; Ker 2010, p. 13-15 et ses citants).* Avantage : décide du statut des voies 2 et 3. Inconvénient : un à deux jours.
- *Option b : avant la rédaction seulement.* Avantage : aucun retard sur l'essai. Inconvénient : prévision scellée sur un statut incertain.
- *Recommandation.* Option a. Confiance : 0,7.

FIN DE LA RÉPONSE
