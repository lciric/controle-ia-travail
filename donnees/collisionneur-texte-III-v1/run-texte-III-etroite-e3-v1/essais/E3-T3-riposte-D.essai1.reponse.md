## 1. Réponse aux critiques visant D

Les calculs restent **conditionnels aux comptes RAPPORTÉS** du fait 17 ; leur cohérence arithmétique seule est **VÉRIFIÉE**.

| Critique | Décision | Correction |
|---|---|---|
| **A(a)1–2, C(a)1 et 3** : « zéro échec sur 59 » ne teste pas \(\pi\leq\varepsilon\) ; probabilités d’inclusion connues et couverture externe répétée supposent un oracle ou déguisent une simulation. | **Acceptée.** | Je retire la falsification par tout échec, les poids d’inclusion supposés connus et la prétention à estimer une couverture avec une population extérieure unique. La validation portera sur des bornes de confiance et des issues explicitement non concluantes. |
| **A(a)3, B(a)1** : modèle génératif non reconstructible ; condition d’échangeabilité omise. | **Acceptée.** | Le plan corrigé ci-dessous fixe les lois, paramètres et facteurs. La décomposition de variance ne concerne qu’une moyenne sous la structure de dépendance déclarée, jamais directement une probabilité de zéro échec. |
| **A(a)4, B(a)3, C(b)2** : duels non exhaustifs, multiplicité de grille et erreur Monte-Carlo non fixées. | **Acceptée.** | Grille et nombre de réplications préenregistrés ; critère rapporté au **minimum sur l’enveloppe des mondes**, avec hypothèses complémentaires. |
| **A(a)5, B(a)2, C(a)2, C(b)3** : la prédiction bilatérale de \(24{,}78\,\%\) confond borne inférieure et estimateur ponctuel, et suppose une capture uniforme. | **Acceptée.** | Je la remplace par une prédiction **unilatérale et conjointe** sous capture extérieure uniforme. Good–Turing ne sert que sous une loi de capture répliquée ; sinon, l’expérience teste le transport, pas \(N\). |
| **A(a)6** : « intervalle de transport » non défini. | **Acceptée.** | Il est supprimé. Seul un intervalle direct, avec estimand et recalcul explicites, peut produire un certificat. |
| **B(a)4–5** : précision excessive et sensibilité numérique des déviances non signalées. | **Acceptée.** | J’écris \(\widehat N_0\simeq39{,}22\), précision arithmétique et non empirique. L’affectation \(P_{23}=17,\ P_{12}=P_{13}=16\) n’est retenue que si « 12,9 » est la même statistique \(G^2\), arrondie, calculée sur un appariement exact. |
| **A, remarque transversale ; B, note transversale** : dépendance et hétérogénéité non séparables par sept comptes ; absence de mondes \(u_{123}\neq0\). | **Transformée en test.** | Les mondes observationnellement équivalents sont regroupés ; \(u_{123}\), la censure et les erreurs d’appariement deviennent des facteurs explicites. |
| **B(b–c), A(b), C(c)1** : tailles tenues à l’écart non variées, absence de contrôles sur classes latentes, fermeture, séquentiel et poids erronés. | **Transformée en test.** | Ces contrôles sont ajoutés, notamment à \(\pi=\varepsilon\), sans classes latentes, avec population ouverte et avec mécanisme de tenue à l’écart corrélé au risque. |
| **C(b)1** : variance infinie de « mon » estimateur à poids inverses. | **Rejetée comme attribution, acceptée comme condition d’échec.** | Je n’avais pas défini un estimateur d’Horvitz–Thompson. Mais toute version à poids \(1/\pi_f\) hérite bien de ce défaut ; elle n’est pas retenue sans plan de tirage réel. |
| **C(c)2** : toute scission augmenterait nécessairement Chao. | **Rejetée.** | Pour une scission triple en paire + singleton, \(\Delta N=1+\frac13\frac{2f_1f_2+f_2-f_1^2}{f_2(f_2+1)}\). À \(f_1=22,f_2=7\) (**illustratif**), \(\Delta N\simeq-0{,}006\). Le contrôle d’appariement reste néanmoins ajouté. |

## 2. Expériences corrigées

### E1 — Estimateurs du nombre de familles

Publier une grille figée de mondes fermés à \(N\) connu : captures hétérogènes, dépendances locales de paire, \(u_{123}\in\{<0,0,>0\}\), censure commune, fusions/scissions et population ouverte. Plusieurs paramétrisations doivent reproduire les mêmes sept comptes. Les mêmes historiques sont soumis au comptage brut \(D\), à l’indépendance, à Chao, aux interactions log-linéaires et aux classes latentes.

- **Duel complémentaire :** \(H_A:\min_{w\in G} Couv_{M_0}(w)\geq0{,}95\) ; \(H_B:\min_{w\in G}Couv_{M_0}(w)<0{,}95\). \(H_A\) falsifie l’affirmation d’échec de \(M_0\) sur la grille ; \(H_B\) falsifie sa calibration.
- **Mesures :** biais, couverture, \(\Pr(L>N_{\rm accessible})\), largeur, erreur de Good–Turing et écart entre \(\widehat C\) et \(D/N\).
- **Puissance Monte-Carlo :** \(R=10\,000\) réplications par cellule (**illustratif**), avec intervalles sur les couvertures.
- **Contrôles :** \(N=D\) ; hétérogénéité pure ; dépendance pure ; \(u_{123}\neq0\) ; absence de classes latentes ; \(N_{\rm accessible}<N\) ; vérification des erreurs d’appariement contre les identités simulées. La base à battre demeure \(D\).

### E2 — Universalité et taille nécessaire

Pour rendre les mondes reconstructibles : risques \(q_f\) de marginales bêta, corrélés par grappes au moyen d’une copule gaussienne ; éléments bêta-binomiaux de moyenne \(q_f\), taille \(m_f\) et corrélation intra-famille déclarées ; découverte \(d_f=\operatorname{logit}^{-1}(\nu_0+\nu_1q_f)\). La tenue à l’écart est soit aléatoire, soit dépendante d’un latent corrélé à \(q_f\). Tous les paramètres et graines sont publiés.

Le plus petit \(n^*\) satisfait simultanément :
\[
\inf_w\Pr_w(\pi_w\leq U_{\alpha,n})\geq1-\alpha,\qquad
\sup_{w:\pi_w>\varepsilon}\Pr_w(U_{\alpha,n}\leq\varepsilon)\leq\alpha,
\]
avec une condition de puissance préfixée à \(\pi=0\). Les regards séquentiels, tailles tenues à l’écart et dépenses d’\(\alpha\) sont fixés avant simulation ; aucun allongement opportuniste.

Pour comparer les définitions, soient \(V_{\rm dir}\) et \(V_\Delta\) les maxima de faux certificats des procédures directe et par écart : \(H_A:V_\Delta<V_{\rm dir}\), \(H_B:V_\Delta\geq V_{\rm dir}\). Aucune n’est retenue si son propre maximum dépasse \(\alpha\). Contrôles : partition échangeable, partition non échangeable, \(\pi=\varepsilon\), \(\pi=0\), et regards répétés.

## 3. Page de réponse à l’arbitre

**Définition retenue.** Pour une classe \(\mathcal C\) et une loi ou population finie \(P_{\mathcal C}\) déclarées :
\[
\pi_{\mathcal C}=\Pr_{F\sim P_{\mathcal C}}(r_F>\tau).
\]
La défense est dite **universelle sur \((\mathcal C,\varepsilon,\alpha)\)** si une borne unilatérale recalculable \(U_\alpha\) vérifie \(U_\alpha\leq\varepsilon\). Cela autorise : « au moins \(1-\varepsilon\) de la masse déclarée passe \(\tau\) ». Cela n’autorise ni « toutes les familles », ni une conclusion hors classe, sur une partie censurée ou sous une autre loi. Le schéma de classe, \(P_{\mathcal C}\), \(r_F,\tau,\varepsilon,\alpha\), l’agrégation et la règle séquentielle sont scellés avant mesure.

**Estimateur retenu.** Chao pour données d’incidence reste un **candidat de borne prudente**, non un certificateur :
\[
L=37+\frac23\frac{16^2}{2\cdot7}=49{,}1905,\qquad
\widehat C=1-\frac{16}{72}=77{,}78\,\%.
\]
\(L\) et \(\widehat C\) sont invariants sur les affectations des recaptures. Sans modèle supplémentaire et sous population fermée, l’intervalle d’identification demeure \([37,+\infty[\) ; **aucun intervalle de confiance nominal n’est établi par les faits**. Good–Turing estime une masse de capture manquante de \(22{,}22\,\%\), pas une fraction de familles. Sous indépendance, \(\widehat N_0\simeq39{,}22\), mais ce modèle est rapporté rejeté.

**Nombre nécessaire.** Les valeurs **29, 59, 149** sont **VÉRIFIÉES** uniquement pour zéro échec et tirages indépendants. Avec découverte et dépendance, \(n^*\) est le minimum satisfaisant les deux conditions de couverture et de faux certificat ci-dessus ; aucun \(n^*\) corrigé n’est encore établi. La garantie ne concerne alors que la population accessible au mécanisme modélisé.

**Validation extérieure, en cinq lignes :**
1. **Définition :** fixer \(m_E\) par calcul de puissance ; sceller \(\pi_E\leq\varepsilon\) ; falsifier ce transport seulement si la borne inférieure externe vérifie \(L_\alpha(\pi_E)>\varepsilon\), sinon rester indécis.
2. **Nombre :** avec \(R_E\) réplications extérieures préfixées, comparer faux certificats et couverture à leurs tolérances binomiales scellées ; une population unique ne valide pas une couverture.
3. **Inconnues, capture uniforme :** sceller une part nouvelle inférieurement compatible avec \(24{,}78\,\%\) ; une part significativement trop basse falsifie l’ensemble borne + uniformité + fermeture + appariement.
4. **Inconnues, loi de capture répliquée :** prédire la masse nouvelle \(22{,}22\,\%\), avec intervalle simulé ; une sortie falsifie le transport de cette loi, non \(N\) seul.
5. **Capture différente ou censure :** aucune de ces issues ne falsifie isolément Chao ou Good–Turing.

**Établi :** les calculs conditionnels ci-dessus et la borne i.i.d. du fait 9. **Non établi :** le vrai \(N\), les probabilités d’inclusion, la fermeture, l’absence de censure, la calibration des intervalles et le transport externe.

**Expérience à faire en premier : E1**, avec enveloppe de mondes observationnellement équivalents, \(u_{123}\neq0\), censure et erreurs d’appariement.

FIN-DE-CELLULE