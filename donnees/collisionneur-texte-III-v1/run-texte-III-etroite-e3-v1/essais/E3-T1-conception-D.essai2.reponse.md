## (a) Hypothèses non établies

- **Classe cible et loi \(P_{\mathcal C}\)** définissant la part d’échec \(\varepsilon\), stables pendant la mesure : **HYPOTHÈSE**.
- **Canonicalisation et appariement exacts** des familles : **RAPPORTÉ** (fait 17 ; seule leur cohérence arithmétique est **VÉRIFIÉE**, fait 18).
- **Tenues à l’écart réellement non vues et échangeables** avec les autres familles de la classe : **HYPOTHÈSE**.
- **Seuil de réussite, loi d’échantillonnage des éléments et agrégation par famille** fixés avant mesure : **HYPOTHÈSE**.
- **Mécanisme de découverte reproductible et correctement simulé** : **HYPOTHÈSE**.
- **Forme de la dépendance, hétérogénéité de capture et absence de censure commune** : **HYPOTHÈSE** ; le rejet de l’indépendance est **RAPPORTÉ**.
- **Indépendance et transportabilité d’une source extérieure** : **HYPOTHÈSE**.

## (b) Duels décisifs

Les seuils de 90 % et les tailles de réplication ci-dessous sont **illustratifs**.

**Duel 1 — estimateurs de familles inconnues.**  
\(H_A\) : sur toute une grille de mondes à dépendance positive et capture hétérogène, l’intervalle log-linéaire sous indépendance couvre le vrai \(N\) dans au moins 95 % des réplications.  
\(H_B\) : dans au moins un monde, sa couverture est inférieure à 90 %, alors que la borne inférieure de confiance associée à Chao atteint 95 %.  
**Métrique :** couverture du vrai \(N\), biais et largeur. **Contrôle négatif :** monde sans famille non observée, puis monde indépendant homogène. Observe­r \(H_A\) falsifie la prétention conjointe de \(H_B\) ; observer le résultat \(H_B\) falsifie \(H_A\) ; un résultat intermédiaire ne départage pas et invalide les deux énoncés forts.

**Duel 2 — définitions d’universalité.**  
\(H_A\) : l’intervalle de transport fondé sur l’écart vues/tenues à l’écart couvre la statistique extérieure à au moins 95 % sur la grille.  
\(H_B\) : sa couverture tombe sous 90 % dans un monde non échangeable, tandis que l’intervalle direct de la proportion sur tenues à l’écart conserve au moins 95 % pour sa classe déclarée.  
**Métrique :** couverture et taux de faux certificats. **Contrôle négatif :** partition aléatoire échangeable, où les deux procédures doivent être calibrées. Chaque issue prévue falsifie l’énoncé adverse ; toute défaillance du contrôle invalide d’abord la simulation.

## (c) Mesure minimale des instruments

Construire des mondes à \(N\), dépendance et hétérogénéité connus ; faire varier aussi censure commune, erreurs d’appariement et découverte non aléatoire. Soumettre **les mêmes historiques simulés** au comptage brut \(D\), au modèle d’indépendance, à Chao, aux modèles à interactions et aux variantes à classes latentes. Mesurer biais de \(\widehat N\), couverture des intervalles, fréquence \(L>N\) pour une borne inférieure, et erreur de \(\widehat C\).

Pour l’universalité, mesurer couverture de la borne sur \(\pi\), faux certificats lorsque \(\pi\geq\varepsilon\), et puissance à \(\pi=0\). **Base à battre :** \(D\), qui estime zéro famille inconnue et présente le biais \(D-N\). Un contrôle négatif avec \(N=D\) ne doit pas produire systématiquement des familles inexistantes.

## Bloc 1 — Définition opérationnelle

Soit \(r_f\) le risque d’échec mesuré d’une famille et \(\tau\) son seuil de réussite.

- **Pire cas :** \(\forall f\in\mathcal C_{\text{schéma}},\ r_f\leq\tau\) ; statistique \(\max_f r_f\). Déclarer schéma, classe exhaustive, \(r_f\), \(\tau\) et incertitude élémentaire. Un tiers recalcule le maximum et ses intervalles. Sur une classe infinie ou non énumérée, un échantillon fini n’établit ce \(\forall\) que sous des hypothèses supplémentaires.
- **Écart vues/tenues à l’écart :** pour la loi déclarée de tenue à l’écart, \(\Delta=g_{\text{tenues}}-g_{\text{vues}}\leq\delta\), avec confiance fixée. Déclarer \(g\), \(\delta\), poids et partition avant mesure. Le tiers recalcule les deux estimations et l’intervalle de \(\Delta\). Cela n’établit ni performance absolue ni transport hors échangeabilité.
- **Proportion/quantile :** pour \(F\sim P_{\mathcal C}\),  
  \[
  \pi=\Pr_F(r_F>\tau)\leq\varepsilon
  \quad\Longleftrightarrow\quad
  \Pr_F(r_F\leq\tau)\geq1-\varepsilon ,
  \]
  avec borne de confiance \(1-\alpha\). Déclarer \(P_{\mathcal C}\), poids, \(\tau,\varepsilon,\alpha\). Le tiers recalcule la proportion pondérée et sa borne unilatérale.

**Option retenue :** la proportion, complétée par les résultats par famille. « Universelle sur la classe déclarée » signifie donc explicitement *au moins \(1-\varepsilon\) en probabilité*, non « toutes sans exception ». « Robuste à l’inconnu » inclurait les familles hors classe ou censurées : aucune de ces statistiques ne le certifie sans loi supplémentaire.

## Bloc 2 — Nombre de familles nécessaire

La cible est \(\Pr(\pi\leq U_\alpha)\geq1-\alpha\), avec certificat lorsque \(U_\alpha\leq\varepsilon\). Le modèle génératif comporte : une loi de découverte \(D\), des risques \(q_f\) hétérogènes, des éléments corrélés intra-famille, et une corrélation inter-familles paramétrée. Pour \(n\) familles et \(m_f\) éléments, la variance minimale est de la forme
\[
\sigma_B^2/n+\sigma_W^2/(nm_f),
\]
à laquelle s’ajoutent les covariances entre familles ; les éléments ne remplacent donc pas des familles indépendantes.

Par simulation, choisir le plus petit \(n\), puis la règle séquentielle, dont la borne recalibrée couvre \(\pi\) au niveau nominal et dont les faux certificats sous \(\pi\geq\varepsilon\) restent \(\leq\alpha\). Arrêt par lots préenregistrés avec dépense d’\(\alpha\), ou suite de confiance valide à tout temps ; sinon échec ou plafond atteint, jamais prolongation opportuniste. Faire varier dépendance, hétérogénéité, corrélations, erreurs de mesure et loi de découverte.

Les nombres **29, 59 et 149** du fait 9 restent exacts pour zéro échec sous tirages indépendants de la loi définissant \(\varepsilon\). Avec découverte, la garantie devient **conditionnelle au modèle et limitée à la population accessible à \(D\)**. La simulation démontre des propriétés opérationnelles dans les mondes testés ; elle ne prouve ni que le monde réel leur ressemble, ni l’absence d’une partie censurée.

## Bloc 3 — Familles inconnues, sources dépendantes

Calculs conditionnels aux comptes **RAPPORTÉS**. Avec \(t=3\), \(D=37\), \(f_1=16\), \(f_2=7\) :
\[
\widehat N_{\rm Chao}=D+\frac{t-1}{t}\frac{f_1^2}{2f_2}
=37+\frac23\frac{256}{14}=49{,}1905 .
\]
C’est une **borne inférieure estimée**, soit \(12{,}1905\) familles non vues et \(D/\widehat N=75{,}22\,\%\) observées. La couverture de Good–Turing est
\[
\widehat C=1-\frac{f_1}{\sum_k kf_k}
=1-\frac{16}{72}=77{,}78\,\% .
\]
Elle couvre la **masse de probabilité de capture**, non 77,78 % des familles. Ces deux résultats sont invariants sur toutes les affectations des recaptures.

Sous le modèle log-linéaire d’indépendance, \(\widehat N_0=39{,}2184\). Les déviances obtenues lorsque la recapture 17 appartient respectivement aux paires \((2,3),(1,3),(1,2)\) sont \(12{,}85,13{,}36,14{,}63\). Si \(12{,}9\) est bien \(G^2\) arrondie, cela impose donc \(P_{23}=17,\ P_{12}=P_{13}=16\).

Avec sept cellules :

| Modèle hiérarchique | Paramètres | ddl résiduels |
|---|---:|---:|
| constante + trois effets | 4 | 3 |
| + une interaction de paire | 5 | 2 |
| + deux interactions | 6 | 1 |
| + trois interactions | 7 | 0 |

Tous fixent l’interaction d’ordre trois à zéro pour extrapoler la cellule \(000\). La laisser libre exige huit paramètres : elle et \(N\) ne sont pas identifiables.

Sous indépendance ajustée, une dépendance positive gonfle généralement les recaptures et **sous-estime \(N\)**, avec intervalles trop étroits. L’hétérogénéité laisse les familles peu capturables parmi les invisibles : Chao reste prudent, souvent bas pour le total. Les fusions à tort tendent à sous-estimer \(D\) et \(N\) ; les scissions gonflent \(D\) et \(f_1\), mais leur effet net sur Chao est ambigu.

Retenir **Chao comme borne prudente**, Good–Turing comme couverture, et les modèles à interactions/classes latentes/bayésiens comme sensibilités, non comme vérité. Une censure commune ne permet d’estimer que la population accessible ; une population non fermée exige dates et modèle ouvert.

## Bloc 4 — Validation extérieure chiffrée

- **Définition :** pour 59 familles extérieures à probabilités d’inclusion connues, indépendantes des trois sources, sceller « zéro échec et borne 95 % sous \(\varepsilon=0{,}05\) ». Tout échec falsifie la prédiction de certificat ; recalculer ensuite la borne.
- **Nombre nécessaire :** sur une population extérieure finie entièrement mesurée, répéter la règle à taille calculée. Prédiction : couverture de \(\pi\) au moins 95 % ; une couverture inférieure à 90 % (**illustratif**) falsifie la calibration.
- **Inconnues :** pour une source extérieure indépendante, échangeable avec la population accessible, sceller une part nouvelle de  
  \[
  1-37/49{,}1905=24{,}78\,\%
  \]
  hors des 37, avec intervalle de simulation préfixé. Une part hors intervalle falsifie la prédiction ; si les poids de capture diffèrent, elle teste surtout le transport, non Chao.

## (d) Ancrage matériel

Aucun modèle ouvert n’est requis pour ce calcul statistique. **Illustratif :** \(10^4\) mondes, vingt réplications par cellule et dix configurations par monde demandent quelques heures sur huit cœurs CPU, moins de 16 Go de mémoire et environ 10 € de calcul ; code, graines et tableaux versionnés suffisent.

FIN-DE-CELLULE