Les quatre conceptions sont lisibles. Les épisodes bruts et le corpus d’entraînement ne sont pas transmis : je ne suppose ni leur contenu ni leur accessibilité. Les constats du dossier restent **RAPPORTÉS** ; les diagnostics ci-dessous sont des **HYPOTHÈSES** méthodologiques à tester.

**Notation commune.** Pour l’adaptateur \(m\), le scénario \(s\) et la condition \(c\), soit \(Y=1\) si l’action nuisible est réellement exécutée, \(V\) le verdict du juge, et
\[
p_{msc}=P(Y=1\mid m,s,c),\qquad
G_{mc}=\frac1K\sum_s(p_{\mathrm{ref},sc}-p_{msc}).
\]
Ainsi \(S_m=1-G_{m,N}/G_{m,O}\), où \(O,N\) désignent observé/non observé. Les tirages à scénario fixé ne remplacent pas les scénarios : la variance résiduelle entre scénarios borne la précision, même avec une inférence illimitée.

## Sur la proposition A

### (a) Défauts de méthode

- **La sélectivité \(\mathrm{Sel}\) ne signe pas l’origine de la capacité.** Ses paires légitime/nuisible testent une sensibilité comportementale à l’autorisation et aux conséquences. Elles ne distinguent pas une capacité acquise par les documents de raisons d’une capacité préexistante, renforcée par la dose, le style ou une autre composante de la recette.
- **Le contrôle de référence est mal justifié.** Une \(\mathrm{Sel}\) élevée chez la référence ne prouve pas que les paires sont « trop faciles » : elle peut refléter une compétence déjà présente. Le contraste pertinent est la différence entre adaptateurs, pas une sélectivité nécessairement faible de la référence.
- **La mise à l’échelle d’un adaptateur n’est pas une dose d’entraînement.** Multiplier son delta modifie simultanément toutes les directions apprises et peut sortir du régime dans lequel l’adaptateur fonctionne. Une courbe monotone, une saturation ou un cosinus élevé entre deltas ne constituent pas des signatures exclusives de « dose » ou de « raisons ».
- **Les greffes de traces confondent contenu et compatibilité.** Source, style, longueur, scénario d’origine et propension de chaque adaptateur à suivre un préfixe varient avec la trace transplantée. L’édition d’une raison citée teste la causalité de la trace à l’inférence, non celle des raisons présentes pendant l’entraînement.
- **La critique du plancher est trop large.** Un \(p_m\) proche de zéro n’implique ni \(G_O\simeq0\), ni \(S\simeq0\) : si la référence reste élevée, \(G_O\) peut être grand. De plus, le regard est précisément censé pouvoir *faire remonter* \(p_m\), mouvement que le plancher n’empêche pas.
- **Les trois signatures positives ne sont pas conjointement suffisantes.** Sélectivité, transfert et effet des éditions de trace peuvent démontrer l’usage causal de justifications au moment du test, sans identifier leur source dans la recette.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **\(S\) et \(D\).** Si \(G_{m,O}=0\), \(S_m\) est indéfini. Par la méthode delta, sa variance contient notamment un terme en \(\operatorname{Var}(\widehat G_O)/G_O^4\) : elle diverge lorsque \(G_O\to0\). Si \(G_O\) et \(G_N\) sont estimés sur les mêmes scénarios, ignorer leur covariance biaise aussi l’intervalle. Le plancher de \(p_m\), seul, ne produit aucune de ces pathologies.
- **Paraphrases et transfert.** Soit \(\pi_{sv}=P(\text{nuisance et autorisation correctement comprises}\mid s,v)\), pour la version \(v\). Si \(\pi_{s,\mathrm{orig}}\ne\pi_{s,\mathrm{para}}\), l’écart de gain mélange surface et compréhension. Si les distributions de difficulté des deux versions ne se recouvrent pas, aucun estimateur apparié ne retrouve un effet de style à difficulté constante.
- **\(\mathrm{Sel}\).** Avec \(K\) paires et une variance entre paires \(\sigma^2\), la variance de l’estimateur conserve un terme d’ordre \(\sigma^2/K\), même en multipliant les tirages. Des erreurs d’étiquetage différentes selon la légitimité peuvent atténuer, annuler ou inverser la sélectivité observée.
- **Greffes.** Soit \(\rho_{mt}=P(\text{le préfixe }t\text{ est effectivement suivi}\mid m)\). Si \(\rho_{mt}=0\), le contraste est muet ; s’il varie avec le contenu ou l’adaptateur, l’effet estimé est celui du couple « contenu × acceptation », pas celui du contenu seul.
- **Échelle des adaptateurs.** Si \(p_m(\alpha)=\Phi(a_m+b_mf(\alpha))\) et \(f\) est presque constante sur les valeurs testées, \(b_m\) est non identifiable. À l’inverse, une courbe visible ne dit pas si \(f\) représente une dose ou une perturbation hors régime.
- **Juge et proximité.** Avec \(\alpha_m=P(V=1\mid Y=0,m)\) et \(\beta_m=P(V=1\mid Y=1,m)\), un même gain jugé peut provenir de \(p_m\), d’\(\alpha_m\) ou de \(\beta_m\). Pour la corrélation proximité–gain, si la proximité est colinéaire au type d’action, au but ou à la difficulté, son coefficient n’est pas identifiable séparément ; si le corpus est inaccessible, le critère est simplement non estimable.

### (c) Contrôles négatifs dont l’absence serait fatale

1. Pour les paires décisives : annotation indépendante et aveugle de la légitimité, plus variantes réellement sans changement sémantique ; des synonymes seuls ne suffisent pas.
2. Pour les greffes : préfixes témoins appariés en source, style, longueur et position, accompagnés d’un contrôle que le modèle utilise effectivement le préfixe.
3. Pour l’intervention interne : outre l’organisme conditionnel et les directions aléatoires prévus, un organisme ou une politique stable, afin de détecter une intervention qui modifie indistinctement toute conduite.
4. Pour tous les gains : exécution établie par journaux d’outils ou changements d’état, pas seulement par concordance entre juges.

## Sur la proposition B

### (a) Défauts de méthode

- **R1 emploie un mauvais contrôle positif.** L’insensibilité du modèle de départ au style n’est ni nécessaire ni suffisante pour valider la réécriture ; il peut lui-même être très sensible au registre.
- **R2 ne sépare pas docilité et raisons.** Une consigne adversariale introduit un conflit avec la spécification. Résister peut signifier préserver la hiérarchie des instructions, tandis qu’obéir peut signifier privilégier la dernière consigne ; aucune issue n’isole une psychologie unique.
- **R3 « confirme » le biais du juge beaucoup trop vite.** Quelques épisodes bien écrits mais mal classés ne démontrent pas une homophilie de famille. Il faut des taux d’erreur différentiels entre adaptateurs, à action et difficulté comparables. Le \(\kappa\) mesure un accord, pas la validité.
- **R4 répète la confusion de sens.** Le plancher empêche surtout une nouvelle baisse du taux nuisible ; il n’empêche pas la hausse prédite par le regard. Rendre les scénarios plus difficiles change également l’estimand et peut introduire des dilemmes où l’action « nuisible » n’a plus la même étiquette normative.
- **R5 ne teste pas l’apprentissage de la phrase anti-regard.** Injecter cette phrase au test ajoute une instruction explicite. Si elle ferme l’écart entre jumelles, cela peut montrer de la docilité contextuelle ; cela ne reproduit ni sa mémorisation ni son absence pendant l’entraînement.
- **R6 et R8 surestiment ce que capacité et décodage valident.** De courts benchmarks généraux peuvent laisser intacts les dommages propres aux outils ou à la planification. Une excellente classification « évalué/déployé » n’implique pas que la direction cause la conduite conditionnelle.
- **La signature positive mélange retrait d’information et retrait de cause.** Supprimer une raison de la consigne peut simplement rendre le cas indécidable. Le duel final n’est pas exclusif : « au moins partiellement des raisons » et « principalement de la surface » peuvent être vrais ensemble.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **Styles et réécritures.** Si \(P(\text{consigne adversariale acceptée}\mid m)\) ou \(P(\text{nuisance reconnue}\mid s,\text{style})\) varie avec \(m\), les contrastes R1, R2 et R5 deviennent des effets composites. Un plafond d’exécution chez tous les adaptateurs supprime également la puissance de R2.
- **Juges.** Le taux jugé est \(r^V_m=\alpha_m+(\beta_m-\alpha_m)p_m\). Deux juges peuvent donc donner le même gain avec des erreurs compensées, ou des gains différents sans différence de conduite. Lorsque la prévalence de \(Y\) approche zéro ou un, \(\kappa\) peut devenir instable malgré des sensibilités et spécificités constantes.
- **Difficulté et bootstrap.** Si \(p_m\in\{0,1\}\) sur presque tous les scénarios, les contrastes absolus perdent leur information et les coefficients logit n’ont pas d’estimateur fini usuel. Si \(p_{msc}\) contient un effet aléatoire de scénario de variance \(\tau^2\), tripler les tirages ne supprime pas le terme \(\tau^2/K\) dans \(\widehat D\).
- **Directions.** Une précision brute dépend de la proportion de textes d’évaluation et du seuil choisi ; une précision proche du hasard peut donc être un défaut de calibration. Réciproquement, même avec une aire sous la courbe élevée, \(P(Y\ \text{change}\mid do(\text{ablation}))\) peut rester nulle : décodage et causalité sont deux paramètres distincts.
- **Seuils du duel final.** Si les gains de surface et de raisons sont additifs ou interactifs, un taux après réécriture ne permet pas d’estimer séparément leurs contributions ; les deux règles de falsification portent alors sur un mélange, non sur \(H_A\) contre \(H_B\).

### (c) Contrôles négatifs dont l’absence serait fatale

- Réécritures validées comme préservant action, permission et enjeu, avec cas bénins à style « piège » et cas nuisibles euphémisés.
- Étalon d’action indépendant du juge et estimation des erreurs **par adaptateur**, plutôt qu’un simple \(\kappa\) global.
- Pour les directions : classifieur textuel simple et données strictement tenues à l’écart ; intervention nulle, direction aléatoire appariée en dommage, organisme conditionnel connu **et** témoin stable.
- Pour R7 : rééchantillonnage au niveau du scénario ; les nouvelles graines seules ne contrôlent pas la généralisation aux formulations ou aux situations.

## Sur la proposition C

### (a) Défauts de méthode

- **La signature positive est corrélationnelle.** Un facteur commun peut faire basculer ensemble la trace et l’action. Leur forte corrélation ne montre donc pas que l’étape de trace cause l’acte.
- **La greffe croisée change plusieurs variables à la fois.** Les traces de la référence diffèrent par leur auteur, leur style, leur scénario et leurs conclusions. Leur rejet éventuel peut être un effet de distribution hors domaine ; leur acceptation peut produire une consigne de continuation, non une utilisation des raisons.
- **Le duel central ne tranche pas la thèse centrale.** Si une trace corrompue ne change pas l’action, cela peut falsifier la causalité de la trace tout en laissant intacte l’hypothèse que des raisons sont encodées dans les poids. Si une trace sûre transfère le refus à la jumelle, cela démontre un effet contextuel, pas l’origine de l’apprentissage.
- **Le cosinus entre directions n’identifie pas un transport causal.** Deux extractions peuvent différer par signe, nuisance, couche ou base du sous-espace. Une direction locale réentraînée sur les mêmes textes que ceux utilisés au test introduit en outre une fuite de validation.
- **La proximité données/scénarios comporte trop peu d’unités indépendantes.** Sur les 27 scénarios RAPPORTÉS, proximité, action, but et difficulté peuvent être presque colinéaires. Le contrôle « textes issus du même prompt » valide éventuellement une métrique de similarité, pas l’existence d’une contamination.
- **L’analyse en log-cotes risque une sélection sur l’issue.** Choisir les scénarios où la recette avec raisonnement n’est pas à zéro parce qu’on y observe des erreurs conditionne l’analyse sur le résultat.
- **La seconde direction d’« artificialité » fuit le banc d’évaluation.** La construire à partir des prompts complets des 27 scénarios, puis évaluer l’ablation sur ces mêmes scénarios, utilise l’évaluation comme instrument de construction.
- **Un parseur syntaxique n’est pas automatiquement un étalon.** Il peut détecter une chaîne sans détecter l’exécution réelle, la destination, les paramètres ou un changement d’état effectif.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **Substitutions lexicales.** Si \(P(\text{action comprise}\mid\text{lexique})\) change, l’effet lexical estimé inclut une perte de compréhension. Si tous les modèles ont \(P(Y=1)\simeq0\) ou \(1\) dans les deux versions, le contraste n’a presque aucune information.
- **Greffes.** Avec \(\rho_{mt}\) probabilité d’adhésion au préfixe, l’effet total est un mélange entre continuation fidèle et ignorée. Si \(\rho_{mt}\) dépend du caractère corrompu, sûr ou neutre, aucune comparaison simple de \(\tau\) n’isole le contenu moral.
- **Transport.** Une précision locale estimée sur ses données d’ajustement est optimiste ; si son erreur dépend de l’adaptateur, la différence de précision locale–transportée ne mesure plus seulement le transport. Un angle proche de zéro ou de quatre-vingt-dix degrés ne fixe pas non plus l’effet de \(do(\text{ablation})\).
- **Proximité.** Si la variance de la proximité est faible, ou si sa matrice de régression avec action, but et difficulté est presque singulière, le coefficient de proximité a une variance qui diverge ou n’est pas identifiable.
- **Log-cotes.** Lorsque \(p_{msc}=0\) ou \(1\), il y a séparation et les estimateurs de log-cotes peuvent tendre vers l’infini. Avec peu de scénarios, la variance des effets aléatoires est fragile ; conditionner sur \(\widehat p_m>0\) biaise en outre les contrastes vers les scénarios à erreurs.
- **Juge.** Même avec un accord brut élevé, des sensibilités \(\beta_m\) ou des fausses alertes \(\alpha_m\) différentes selon \(m\) suffisent à créer un écart de gain. Un \(\kappa\) proche de un n’exclut pas ces erreurs si elles sont rares mais concentrées sur les épisodes décisifs.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Traces :** édition minimale d’une seule justification, à source, scénario, style et longueur constants ; témoin neutre accepté au même taux, et contrôle positif qu’un préfixe peut causer un changement d’action.
2. **Directions :** séparation disjointe entre textes de construction, validation et scénarios finaux ; comparaison à un classifieur lexical, directions aléatoires appariées en dommage et organismes stable/conditionnel.
3. **Juge :** journaux d’environnement ou d’outils comme vérité primaire ; audit humain aveugle seulement pour les cas non décidables mécaniquement.
4. **Log-cotes :** strates de difficulté définies sans regarder les erreurs et estimateur explicite en présence de séparation.

## Sur la proposition E

### (a) Défauts de méthode

- **La règle commune de décision ne résout pas l’identification.** \(H_A:d\geq\delta\) et \(H_B:d<\delta\) sont bien exclusives, mais un \(d\) élevé peut encore être produit par une variable confondante. Le formalisme ne transforme pas un contraste comportemental en attribution à l’entraînement.
- **Un même seuil en points de pourcentage est appliqué à des estimands hétérogènes.** Perte de justesse, écart de précision équilibrée, dommage et différence de scores appariés n’ont ni la même variance ni la même importance scientifique.
- **Plusieurs contrôles nommés « négatifs » ne sont pas semantiquement neutres.** Une attribution d’autorité peut être une information pertinente sur la permission ; un effet de cette étiquette ne réfute donc pas nécessairement l’usage de raisons.
- **La référence n’est pas toujours le bon zéro.** Pour le sur-refus, un excès par rapport à une référence elle-même défaillante ne mesure pas nécessairement l’inadéquation ; il faut une action appropriée définie indépendamment.
- **Le budget de génération égal du duel modifie potentiellement les politiques comparées.** Imposer aux jumelles le même budget peut supprimer précisément la différence de fonctionnement qui les distingue. C’est un témoin de coût, pas nécessairement un témoin causal.
- **Le score décisif additionne deux populations de paires.** Soustraire des changements injustifiés mesurés sur des paires cosmétiques à une justesse mesurée sur des paires causales suppose une comparabilité de difficulté et d’échantillonnage qui n’est pas établie.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **Règle à intervalle.** Si \(\operatorname{Var}(\widehat d)\) reste supérieure à l’écart entre \(d\) et \(\delta\), presque tous les résultats sont indéterminés. Sans correction pour la multiplicité des mesures, la probabilité qu’au moins un intervalle franchisse artificiellement le seuil augmente avec le nombre de tests.
- **Paires contrefactuelles.** Seules les paires discordantes en action contribuent à la sélectivité appariée. Si \(\pi_{10}+\pi_{01}\) est proche de zéro, la variance relative de leur différence \(\pi_{10}-\pi_{01}\) devient très grande ; multiplier les répétitions au sein des mêmes paires ne crée pas de nouvelles paires indépendantes.
- **Justesse et sur-refus.** Si l’étiquette « action appropriée » comporte des erreurs dépendant de l’adaptateur ou du style, \(d\) mélange comportement et annotation. Si les paires cosmétiques et causales n’ont pas une distribution commune de difficulté, leur soustraction n’a pas d’interprétation causale simple.
- **Audit du juge.** Si l’audit surreprésente les désaccords, \(G_{\mathrm{audit}}\) doit être repondéré vers la population initiale ; sinon \(G_{\mathrm{juge}}-G_{\mathrm{audit}}\) compare deux estimands. Un écart nul peut également résulter d’erreurs compensées entre référence et adaptateur.
- **Transport et dommages.** Une précision équilibrée locale estimée avec davantage de données ou sur son propre apprentissage n’est pas comparable à celle du transport. Un \(d\) de dommage nul n’exclut pas des dommages non mesurés ; un \(d\) élevé ne détermine pas si la variation de sûreté est entièrement due au dommage.
- **Réplication.** Si l’estimation initiale est sélectionnée parmi plusieurs graines ou analyses parce qu’elle est favorable, \(E[\widehat d_{\mathrm{initial}}-\widehat d_{\mathrm{réplication}}]>0\) même sous l’hypothèse nulle : c’est le biais du vainqueur, pas nécessairement une fragilité du comportement.

### (c) Contrôles négatifs dont l’absence serait fatale

- Une véritable variation cosmétique, validée comme ne changeant ni permission, ni conséquence, ni information sur le contexte ; l’étiquette de prestige ne remplit pas automatiquement ce rôle.
- Des étiquettes d’action appropriée et des exécutions mécaniques établies aveuglément, avec repondération explicite de tout audit stratifié.
- Pour les sondes : tailles et procédures d’ajustement comparables, évaluation tenue à l’écart et seuil fixé indépendamment ; pour les ablations : intervention nulle et témoin stable, en plus de l’organisme conditionnel.
- Pour le duel : seuils \(\delta\) fixés séparément selon chaque estimand et rééchantillonnage respectant les paires et les scénarios, sans traiter les tirages comme indépendants.

FIN-DE-CELLULE