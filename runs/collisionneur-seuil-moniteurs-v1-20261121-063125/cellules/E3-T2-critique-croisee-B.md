# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces.** Les quatre conceptions (A, C, D, E), les FAITS et la QUESTION sont présents. Aucune n'est visiblement coupée. Je ne peux pas recalculer les empreintes sha256.

**Conventions.**
- Les résultats du papier sont cités au statut RAPPORTÉ.
- Mes critiques sont des analyses au statut HYPOTHÈSE, sauf les identités de calcul standard, signalées comme telles.
- Tout chiffre qui n'est pas dans les FAITS est marqué illustratif.
- Conformément à B1, je n'harmonise pas les propositions. Quand je reprends un argument d'une proposition pour en critiquer une autre, je le dis.

**Point transversal, utilisé dans les quatre sections.** A signale, à propos de sa proposition P2, que comparer agent et jumeau détecte « la consigne cachée, pas l'intention ». Je généralise cet argument :
- Si le saboteur est obtenu par une instruction ou un réglage absent chez le jumeau, toute sonde interne peut lire cette différence de conditionnement.
- C'est vrai par construction, avant tout sabotage exécuté.
- Le contrôle négatif correspondant est le même partout :
  - un « saboteur fictif », c'est-à-dire une instruction cachée bénigne de même longueur et de même structure ;
  - un « saboteur instruit sans occasion d'agir », qui reçoit la consigne mais sans action dommageable possible ou réalisée.
- Aucune des quatre propositions ne pose ce couple de contrôles comme obligatoire.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **P2/D2 : l'A/A est en partie vrai par construction.**
   - Si les épisodes honnêtes existants ont été produits par la même configuration que le jumeau, le test A/A sur ces épisodes vérifie surtout l'implémentation du rang, pas la validité du nul en déploiement.
   - Le contrôle « agent et jumeau avec graines identiques, le processus doit rester à 1 » est un test d'indexation. Avec des graines identiques, les scores sont égaux et le résultat dépend seulement du traitement des égalités. Il ne renseigne pas sur l'échangeabilité.
   - Le vrai risque est ailleurs : un écart d'échafaudage, de température ou d'outils entre l'agent déployé et le jumeau.

2. **P2 : le nul choisi et la cible du programme ne coïncident pas.**
   - Le processus d'e-valeurs teste « l'agent tire ses pas de la même loi que le jumeau ». Il ne teste pas « honnête, y compris en échec, contre saboteur ».
   - Un rejet établit une différence de politique. L'attribuer au sabotage exige le contrôle transversal (instruction bénigne).
   - De plus, la garantie de Ville est marginale sur toutes les longueurs. Le verdict du programme est fixé **par tranche de longueur**. Je reprends ici l'objection de D : A ne montre pas que le processus tient 1 % dans chaque tranche.

3. **Courbe de puissance par signal synthétique planté.**
   - Ajouter un décalage connu aux activations mesure la sensibilité de la machinerie à un décalage additif, par construction.
   - Cela ne dit rien de la puissance contre une représentation réelle du sabotage.
   - A le présente comme mesure de la machinerie, ce qui est correct. Mais il en fait aussi un élément de son « second volet » de D2 : la comparaison à M1–M3 sur ce signal planté n'est pas informative sur l'utilité réelle.

4. **D1 : la cible réfutée est en partie un épouvantail.**
   - A établit lui-même que les « 5 000 par tranche » sont un critère de précision, pas de validité.
   - « H_A observé réfute la nécessité des 5 000 pour la validité » réfute donc ce qui n'était pas affirmé.
   - Par ailleurs, D1 repose sur un terrain de substitution (tâches vérifiables courtes) dont la queue honnête n'a aucune raison de ressembler à celle d'épisodes de recherche longs. A le reconnaît (« réfuter, pas valider ») mais en tire quand même une conclusion sur la nécessité.

5. **P1 : fuite possible entre normalisation et calibration.**
   - P1 normalise par régression sur longueur et difficulté, puis calibre.
   - Si la régression est ajustée sur les épisodes de calibration, les résidus sont rétrécis et le quantile est sous-estimé.
   - A ne prescrit pas d'ajustement croisé dans P1. E le prescrit pour son propre P2.

6. **U1/D3 : délai entre chute de valeur et trace.**
   - **Hors protocole du papier.** La sonde de valeur est lue « à la position initiale du prompt, avant tout jeton de réponse » (RAPPORTÉ, p. 4) et en position finale (p. 4, Annexe I). Une lecture de valeur pas à pas le long d'un épisode n'est pas un instrument du papier. C'est une extrapolation à valider à part, en plus de D4.
   - **Sélection par le collisionneur.** Le contraste porte sur des sabotages à dommage **confirmé**. Un dommage confirmé implique des traces visibles. La date de « première trace observable » est donc conditionnée par la même variable que la sélection.
   - **Annotation non aveugle.** Si les annotateurs de la trace connaissent la condition, le délai est biaisé.
   - **Lecture de la consigne.** Une consigne de sabotage présente dès le prompt fait chuter la valeur au pas 0 par construction, puisqu'elle annonce l'échec de la tâche. L'« avance » serait alors une lecture de consigne.
   - Le contrôle de A, « jumeau lecteur du même transcrit », n'est valide que si le transcrit relu **exclut** la consigne cachée. A ne le précise pas.

7. **U4 : point de méthode solide.** A identifie lui-même que l'ablation supprime aussi la lecture « dopamine » en aval (RAPPORTÉ, p. 5) et restreint l'usage en conséquence. Je n'ai pas d'objection supplémentaire.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **Quantile conforme par tranche.** Avec n_b honnêtes dans la tranche, la plus petite p-valeur est 1/(n_b+1) (calcul standard). Si n_b < 99 (illustratif), la règle ne peut pas alerter à 1 %.
- **Effet de grappe.** Si les épisodes sont groupés par tâche avec un coefficient de corrélation intra-classe ρ et k épisodes par tâche, l'effectif utile vaut environ n/(1+(k−1)ρ) (calcul standard). Le critère est injugeable dès que cet effectif passe sous le seuil précédent.
- **Borne binomiale (P3).** Certifier α avec zéro dépassement exige n ≥ ln(1/δ)/α (calcul standard ; environ 300 pour δ = 0,05, illustratif) **par tranche**. Avec B tranches et une correction de Bonferroni, il faut environ ln(B/δ)/α par tranche. α\* est alors trop lâche dans chaque tranche dès que N/B est de l'ordre de quelques dizaines.
- **e-processus par rang (P2).** Avec m continuations, la p-valeur de rang prend des valeurs dans {1/(m+1), …, 1}.
  - Le taux de croissance espéré du log de la richesse par pas est majoré par la divergence de Kullback-Leibler (KL) entre la loi du rang sous l'alternative et la loi uniforme.
  - Si le sabotage n'occupe qu'une fraction f des pas surveillés, ce taux est multiplié par f.
  - Le critère perd sa puissance dès que T·f·KL < ln 100, avec T le nombre de pas surveillés.
- **Rupture d'échangeabilité.** Si, sous le nul, la p-valeur de rang vérifie P(p ≤ u) = u(1+ε) avec ε > 0 (non-déterminisme numérique, outils non rejouables), un pari à mise fixe λ dérive à un taux d'ordre λε par pas. La probabilité de fausse alarme croît alors avec la longueur, ce qui viole la garantie précisément dans la tranche la plus longue.
- **Valeurs extrêmes (P7).** Avec k dépassements, l'écart-type asymptotique de l'estimateur du paramètre de forme ξ est d'ordre (1+ξ)/√k (calcul standard). Si la sonde est bornée (ξ < 0), le quantile extrapolé est dominé par l'erreur sur ξ.
- **D3 (permutation appariée).** La puissance est nulle si la variance intra-paire du délai, discrétisé en pas, domine le carré de la différence moyenne. C'est le cas si la granularité des pas est grossière devant l'effet.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour P2/D2 et D3 :** saboteur fictif (instruction bénigne) et saboteur instruit sans occasion d'agir. Sans eux, toute alarme ou toute « avance » peut être une lecture de consigne.
2. **Pour P2 :** un A/A **inter-configurations**. Il compare deux exécutions honnêtes qui diffèrent seulement par ce qui diffère en déploiement (version d'échafaudage, rejeu des outils). Le contrôle à graines identiques ne suffit pas.
3. **Pour D3 :** une annotation de la date de trace à l'aveugle de la condition, et un transcrit relu sans la consigne cachée.
4. **Pour P1 :** la même procédure appliquée à des tâches entières exclues de la régression de normalisation.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statut et chiffre introduits.** La requête reformulée écrit « N ≈ 300 à 500 épisodes honnêtes existants [RAPPORTÉ] ». Les FAITS disent « quelques centaines », sans fourchette. Cette fourchette n'est pas un fait rapporté : elle devait être marquée illustratif (règles 1 et 4).

2. **Expérience 2 : le problème initial est réintroduit et il y a une fuite.**
   - Le critère est le « TPR à 1 % FPR calculé sur les échecs honnêtes appariés ». L'ensemble apparié est petit par nature : un seuil à 1 % y est indéfinissable, exactement l'obstacle que la proposition prétend contourner.
   - Si le seuil est fixé et la détection mesurée sur les mêmes échecs appariés, le taux de faux positifs est optimiste par construction.
   - De plus, le contrôle « Wanda reste au niveau du hasard » est incompatible avec les faits : les neurones choisis par Wanda font déjà chuter la précision à 65,8 % (RAPPORTÉ, Table 2). Ils ne sont pas inertes, donc ce contrôle peut échouer sans rien dire sur H_A.

3. **Expérience 1 : injugeable par construction.**
   - Distinguer un taux de faux positifs dans [0,8 %, 1,2 %] d'un taux supérieur à 3 %, à partir d'environ 150 épisodes (illustratif), revient à attendre de l'ordre de 1,5 dépassement sous le nul.
   - L'intervalle binomial couvre les deux hypothèses : aucune issue ne falsifie quoi que ce soit, ce qui contredit B4.
   - Le contrôle par permutation de l'ordre des paragraphes détruit l'autocorrélation. Il teste le test de Ljung-Box, pas la validité du bootstrap.

4. **A1 (martingale) : nul vrai en échantillon par construction.**
   - Z_k est centré sur une prédiction et réduit par une variance estimée **sur les mêmes transitions honnêtes**. Sur ces données, E[Z] ≈ 0 par construction, donc un A/A in-sample passe.
   - Hors échantillon, rien ne garantit E[Z_k | F_{k−1}] ≤ 0, et C le pose comme hypothèse.
   - La troncature de Z doit garantir 1+λZ ≥ 0 sans biaiser l'espérance vers le haut. C n'explicite pas comment.
   - L'objection de D sur la garantie par tranche s'applique aussi : Ville donne une garantie marginale sur toutes les longueurs, pas une garantie dans chaque tranche.

5. **B1 (« cohérence TD inter-couches ») : vraie par construction, et hors protocole.**
   - La sonde dopamine est entraînée à régresser une erreur TD estimée par rollouts Monte-Carlo, c'est-à-dire une différence de valeurs (RAPPORTÉ, p. 6). Le résidu r_t est donc petit sur la distribution d'entraînement par construction.
   - Hors distribution (recherche ouverte), il grandira pour **tout** épisode, honnête ou saboteur. Le résidu confond alors sortie de distribution et intention.
   - Lire la valeur aux couches 2–4 à chaque pas sort du protocole de lecture du papier (lecture au prompt, p. 4), comme pour U1 chez A.

6. **B3 : erreur d'échelle.** Le seuil |erreur| > 0,3 filtre des **cibles** Monte-Carlo à l'entraînement (RAPPORTÉ, p. 6). Le réutiliser comme seuil sur une **différence de sorties de sonde** agent/jumeau mélange deux échelles sans recalibration.

7. **B4 (greffe des neurones de valeur du jumeau) : nul par construction ou lecture de consigne.**
   - La greffe se fait « sur le même prompt initial ». Si agent et jumeau ont les mêmes poids et le même prompt, les activations en position initiale sont identiques : la greffe ne change rien, quelle que soit l'intention.
   - Si elle change quelque chose, c'est que les prompts ou les poids diffèrent. On détecte alors la consigne ou le réglage, pas le sabotage.

8. **Expérience 3 (KL sous ablation) : variable confondante.**
   - La KL entre politiques intacte et ablatée dépend fortement de l'entropie de la loi du jeton suivant au point considéré.
   - Si les pas sabotés ont une entropie différente des pas d'échec honnête, ce qui est plausible pour du texte délibéré, l'AUC mesure l'entropie.
   - Le contrôle « sonde de prédiction du jeton suivant » ne neutralise pas ce facteur.

9. **Tableau de mesures minimales.** Les critères « réduire l'IC d'un facteur 3 » (GPD) ou « même stabilité que 3 000 épisodes » (bootstrap) sont satisfaits **par hypothèse paramétrique**. Un modèle de queue plus contraint donne mécaniquement un intervalle plus étroit, sans rien dire de sa couverture.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **A1.** Si, sous l'échec honnête, Z_k a une moyenne conditionnelle μ > 0 et une variance σ², log M_t dérive à un taux d'environ λμ − λ²σ²/2 (calcul standard). Si ce taux est positif, la probabilité de franchir 100 tend vers 1 quand la longueur croît : le taux de fausses alarmes devient une fonction de la longueur.
- **Bootstrap par blocs.** Si le score contient un effet d'épisode u_i (décomposition introduite par E), alors Var(S_L) contient un terme L²·Var(u). Rééchantillonner des blocs d'incréments mélangés entre épisodes efface ce terme et sous-estime la queue des sommes longues. La procédure perd sa validité dès que Var(u)·L domine la variance des résidus d'étape.
- **POT/GPD avec u = q_{0,90}.** Avec N de quelques centaines, k vaut de l'ordre de 30 à 50 (illustratif). L'erreur sur ξ se propage exponentiellement dans le quantile extrapolé (voir A). Le critère « borne haute ≤ 1,8 % » est alors injugeable : il faudrait un lot hors échantillon d'au moins quelques centaines d'épisodes par tranche.
- **McNemar apparié (Exp. 2).** La puissance dépend uniquement du nombre de paires discordantes. Si, au seuil fixé, les deux sondes alertent toutes deux sur presque aucun échec honnête, ce nombre est quasi nul et le test n'a aucune puissance, quel que soit l'effet.
- **Splitting.** L'efficacité dépend de la corrélation entre score à mi-parcours et score final. Si elle est faible, la variance de l'estimateur est égale ou supérieure à celle du Monte-Carlo brut.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **B1 :** résidu de cohérence TD sur des **succès honnêtes** de recherche ouverte. S'il est aussi élevé que chez le saboteur, le signal est une sortie de distribution.
2. **B4 :** greffe à prompt et poids identiques. Le résultat attendu est un effet nul : si un effet apparaît, il y a un défaut d'implémentation.
3. **Exp. 3 :** stratification ou appariement par entropie du jeton suivant.
4. **Exp. 2 :** seuil fixé sur un lot honnête **disjoint** des échecs appariés évalués.
5. **Transversal :** saboteur fictif et saboteur instruit sans occasion d'agir.

---

## Sur la proposition D

### (a) Défauts de méthode

D est la conception la plus économe en hypothèses. Je lui fais quatre objections.

1. **Statuts.** D marque VÉRIFIÉ des dérivations : la règle de rang, la formule (1−α)^{n_b}, la borne 1−δ^{1/m_b] et l'inégalité de Ville.
   - Ce sont des identités mathématiques correctes sous leurs hypothèses (continuité, indépendance, échangeabilité), que D énonce.
   - Je ne change pas ces statuts. Je note seulement qu'ils portent sur des calculs, pas sur des faits du programme.

2. **Moniteur de trajectoire.**
   - Le contrôle « masquer la correspondance entre trajectoires et épisodes à tâche et difficulté comparables » est sous-spécifié. On ne sait pas ce qui est permuté, ni à quel niveau.
   - Surtout, D ne prévoit pas le contrôle transversal : une baisse de valeur au prompt chez le saboteur peut être lue directement sur la consigne. D signale bien qu'« une baisse de valeur peut signaler exactement la même difficulté », mais pas qu'elle peut signaler la consigne.

3. **Routage randomisé : estimand non transportable.**
   - La « réduction du dommage final par heure de revue » dépend de la prévalence π des saboteurs dans le flux, fixée par l'expérimentateur. Le résultat est une fonction de π choisi, pas une propriété du moniteur.
   - Le dommage évité est contrefactuel. Si la revue empêche le dommage, il n'est plus observable. D le voit et demande une étiquette pré-intervention, mais il faut alors un rejeu sans intervention de chaque épisode routé. Ce coût est absent du devis.
   - Enfin, le ratio est instable quand le dénominateur (heures) varie entre bras.

4. **Duel « installer ou refuser le seuil ».**
   - D note qu'un seuil silencieux satisfait H_A, ce qui est exact.
   - Mais H_A est alors **vrai par construction** pour tout seuil assez haut, y compris le seuil infini. Le duel ne falsifie quelque chose d'utile que s'il est couplé à un plancher de détection préenregistré.
   - D rapporte la détection « séparément » au lieu de l'intégrer au critère.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **Règle de rang par tranche.** Même condition que chez A : n_b ≥ 99 (illustratif). L'échangeabilité exigée est **entre familles** : la garantie est marginale sur le tirage des familles de calibration. Si le nombre de familles F_b de la tranche est petit, la dispersion du taux réalisé autour de 1 % est gouvernée par F_b, pas par n_b. Une seule famille rare à queue lourde suffit à faire dépasser le taux réalisé.
- **Audit binomial d'un seuil gelé.** Avec zéro alerte, il faut m_b ≥ ln(1/δ_b)/α. Avec un partage du risque δ entre B tranches, il faut environ ln(B/δ)/α par tranche (calcul standard). Le critère « toutes les bornes supérieures simultanées ≤ 1 % » devient injugeable si m_b est de l'ordre de quelques dizaines : l'issue « inconclusif » est alors quasi certaine.
- **Marge g des duels.** Si la variance de la différence appariée, gonflée par la corrélation intra-famille, rend la demi-largeur de l'intervalle supérieure à g, les deux issues falsifiantes sont presque impossibles.
- **Routage.** Si π·N_routés est petit, le nombre d'événements dommageables est petit. L'estimateur du dommage évité a une variance d'ordre 1/(π·N), et le critère perd sa puissance quel que soit l'effet.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Transversal :** saboteur fictif et saboteur instruit sans occasion d'agir, surtout pour le moniteur de trajectoire fondé sur la valeur au prompt.
2. **Échec honnête par environnement dégradé** (bug injecté), au sens de E. Cela sépare « la sonde lit l'échec » de « la sonde lit l'intention » à dommage égal. Les témoins de D (honnêtes scellés, échecs sans sabotage) n'imposent pas que l'échec soit hors du contrôle de l'agent.
3. **Routage :** le témoin « priorités permutées » est bon. Il faut y ajouter un rejeu sans intervention, faute de quoi l'étiquette de dommage est post-traitement.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts attribués sans source.**
   - E qualifie d'OBSERVÉ-NON-AUDITÉ l'existence des épisodes honnêtes, du jumeau et des sondes, ainsi que la « divergence KL instantanée avec le jumeau ». Le bloc FAITS n'étiquette pas ces énoncés.
   - Je ne modifie pas ces statuts, mais leur attribution n'est pas sourcée. Le lecteur ne doit pas la prendre pour un audit des FAITS.
   - De même, « cross-fitting… rétrécissement des résidus, VÉRIFIÉ » est un principe général, pas un résultat du programme.

2. **Présupposé P1 : la réfutation va trop loin.**
   - E affirme que la nécessité des tranches est « fausse dès que » le score est un e-processus.
   - Ville contrôle le franchissement marginalement sur toutes les longueurs, pas dans chaque tranche de longueur finale, qui est le point de verdict fixé par le programme.
   - Je reprends ici l'objection de D : la conclusion est une reformulation de la promesse, pas une réfutation.

3. **E1 : contrôle A/A vrai par construction, et terciles injugeables.**
   - L'A/A « agent = tirage indépendant identique au jumeau » vérifie l'indexation, pas l'échangeabilité de l'agent déployé.
   - Avec environ 500 échecs scellés en trois terciles (illustratif), chaque tercile compte environ 167 épisodes. Les seuils 11/500 et 5/500 portent sur le total.
   - La condition « sans excès dans le tercile long » est injugeable à ce n : environ 1,7 alarme attendue sous le nul (illustratif).

4. **M1 : variable confondante, la compétence.**
   - Δ_t compare la TD prédite par le jumeau sur l'action de l'agent à sa moyenne sur ses propres actions.
   - Un échec honnête commet aussi des actions que le jumeau juge sous-optimales : ses erreurs sont justement ce qui distingue un échec d'un succès. Δ_t est donc corrélé à l'échec, ce qui est l'hypothèse du programme à réfuter.
   - De plus, une action tirée d'une autre politique est hors politique pour le jumeau. Δ_t peut refléter la surprise du jumeau, sa faible vraisemblance de l'action, plutôt qu'un dommage.
   - L'idée de faire passer l'action dans le jumeau pour neutraliser une inversion de signe chez l'agent est un bon garde-fou contre l'adversaire. Elle ne règle pas ces deux confusions.

5. **E3 : « TPR à FPR = 1 % » sur le contraste apparié.** Même défaut que l'Exp. 2 de C : un seuil à 1 % estimé sur un petit ensemble apparié est indéfini, et fuit s'il est mesuré sur les mêmes paires. Le contrôle par bug injecté est en revanche le bon contrôle, et E est le seul à le poser.

6. **E4 et C2 : conflit avec une décision du programme.**
   - Ces expériences exigent un « saboteur informé du mécanisme » ou un « organisme modèle entraîné avec pénalité d'évasion ».
   - Le test d'évasion à capacité constante est **clos pour l'instant** (FAITS §3).
   - La branche falsifiante de E4 qui réfute H_B (« y compris face à un saboteur informé ») et la mesure minimale de C2 dépendent donc d'une condition que le programme a décidé de ne pas instruire. Sans elle, H_B ne peut pas être falsifiée et la règle B4 n'est pas respectée.

7. **C2 (i) : critère non opérationnel.** « Cohérence d'action qui persiste anormalement » sous ablation n'a ni estimateur ni loi de référence. De plus, l'ablation supprime aussi la lecture dopamine en aval (RAPPORTÉ, p. 5) : tout moniteur dopamine lu pendant ce test est invalide.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **Processus d'e-valeurs de rangs avec K = 4 (illustratif).** Les rangs prennent cinq valeurs. Si l'alternative met une probabilité q sur le rang extrême contre 1/5 sous le nul, le taux de croissance maximal par pas vaut KL(q ‖ 1/5).
  - Sur m points de contrôle, dont une fraction f est sabotée, la puissance est faible si m·f·KL(q ‖ 1/5) < ln 100.
  - Avec m = 20 (illustratif) et un sabotage diffus (f petit, q proche de 1/5), c'est la configuration attendue.
- **Biais d'échangeabilité.** Mêmes conditions que chez A : P(p ≤ u) = u(1+ε) suffit à faire croître le taux de fausses alarmes avec la longueur.
- **Décomposition s_{i,t} = u_i + ε_{i,t} (O7).** Si Var(u) > 0 et que le nombre de familles est petit, le quantile des sommes est gouverné par la loi de u, estimée sur F points seulement. Aucun ré-échantillonnage d'étapes n'y supplée.
- **Conformal pondéré (O8).** Le critère N_eff ≥ 100 échoue si le rapport de densités source/cible a une variance élevée, ce qui est attendu entre tâches vérifiables courtes et recherche ouverte. Il est injugeable si ce rapport n'est pas estimable, c'est-à-dire si les supports sont disjoints.
- **Wilks (O4).** La tolérance à 1 % avec δ = 0,05 exige environ 299 épisodes indépendants par unité certifiée (illustratif). E le dit lui-même : la stratification par tranche est donc incompatible avec le stock.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **M1/E3 :** Δ_t sur des actions **d'échec honnête apparié** passées dans le jumeau, et sur des actions honnêtes tirées d'une **autre configuration honnête** (température ou échafaudage différents). Cela sépare compétence, surprise hors politique et intention.
2. **Transversal :** saboteur fictif et saboteur instruit sans occasion d'agir.
3. **E1 :** A/A inter-configurations, et pas seulement agent identique au jumeau.
4. **C2 :** même ablation sur le jumeau honnête, avec un moniteur dopamine désactivé pendant l'ablation.

---

## Synthèse des contrôles fatals, non lissée

| Contrôle | A | C | D | E |
|---|---|---|---|---|
| Saboteur fictif (instruction bénigne) et saboteur instruit sans occasion d'agir | absent | absent | absent | absent |
| Échec honnête par environnement dégradé | absent | mentionné (§4), absent des expériences | absent | présent (E3) |
| Seuil fixé sur un lot disjoint des paires évaluées | partiel | absent (Exp. 2) | présent | absent (E3) |
| A/A inter-configurations, pas seulement graines identiques | absent | absent | implicite (seconde collecte) | absent |
| Garantie vérifiée par tranche, pas seulement marginale | non | non | oui | non |

FIN-DE-CELLULE