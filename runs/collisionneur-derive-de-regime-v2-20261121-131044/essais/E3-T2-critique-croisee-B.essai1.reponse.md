# Critique croisée de méthode : proposition B, tour III.2

**Pièces reçues.** A, C, D et E sont présentes et non coupées : chacune se termine par sa ligne de clôture. Je n'ai pas contrôlé les empreintes sha256. Le chiffre de CURA reste RAPPORTÉ, page du PDF non lue.

**Deux remarques transversales**, que je ne fusionne pas avec les critiques ci-dessous.

1. **Statuts.** Le bloc FAITS n'étiquette rien. A classe tout son contenu comme RAPPORTÉ. C et E marquent VÉRIFIÉ des éléments des FAITS, voire leurs propres références bibliographiques. E marque la fragilité du jumeau OBSERVÉ-NON-AUDITÉ. D emploie VÉRIFIÉ pour des propriétés démontrées. Je ne modifie aucun de ces statuts. Je signale seulement que les mêmes faits portent des statuts différents selon les propositions : leurs verdicts ne sont donc pas comparables tant que l'arbitre n'a pas fixé un étiquetage unique.
2. **Zone intermédiaire.** Plusieurs duels laissent entre leurs deux seuils une zone où aucune hypothèse n'est falsifiée. Sous B4, chaque fois que c'est le cas, l'expérience n'est pas décisive.

Tous les chiffres que je calcule ci-dessous sont des **calculs illustratifs**. Ils ne viennent pas des FAITS.

---

## Sur la proposition A

### (a) Défauts de méthode

- **D0 conclut à partir d'un manque de puissance.**
  - Avec n = 300 et k = 3, le taux réel d'un seuil étalonné suit Beta(3, 298). Son intervalle central à 95 % va d'environ 0,21 % à 2,4 % (calcul illustratif).
  - Le rapport de deux taux indépendants ainsi tirés couvre donc plus d'un ordre de grandeur. Un vrai triplement tombe dans la bande avec une forte probabilité.
  - A écrit : « Dans la bande, H_B est falsifiée comme explication nécessaire. » C'est une absence de puissance comptée comme falsification. D0 penche structurellement vers H_A. Il faudrait le formuler comme un test d'équivalence, ou le juger sur un monde planté dont la dérive est connue.
- **D4 est vrai par construction pour P1.** Le seuil de P1 ne lit pas le flux, donc sa détection ne peut pas dépendre de la prévalence de sabotage. D4 sépare correctement les règles alimentées par le flux de celles qui ne le sont pas. En revanche, il n'apporte aucune preuve en faveur de P1.
- **D3 est circulaire vis-à-vis de S4.** Juger l'échangeabilité du jumeau exige des épisodes honnêtes de l'agent dans le nouveau régime. C'est exactement la ressource que le jumeau devait remplacer. D3 n'est donc exécutable que sur monde planté, ou là où S4 est déjà acquise.
- **Le second volet de P4 confond deux causes.** « Dérive du flux sans dérive des témoins » a deux explications indiscernables par cette seule statistique :
  - un sabotage ;
  - un écart de représentativité des témoins, par exemple une nouvelle source bénigne absente de la banque de témoins.
  
  A traite la première comme la lecture par défaut. Sans S4 et S5, ce volet n'a pas de niveau contrôlé.
- **Fuites possibles.**
  - D2 re-standardise sur les témoins. Si le taux restauré est mesuré sur ces mêmes témoins, l'évaluation réutilise l'instrument.
  - Dans P3, la frontière b(t) est dite « fixée d'avance ». Si elle est choisie à partir des épisodes d'étalonnage qui fixent ensuite le quantile des M, la garantie P1 tombe. Un découpage strict est nécessaire.
- **Indépendance des témoins.** La garantie binomiale de P1 suppose des témoins i.i.d. Des témoins regroupés par session ou par dépôt de code la rendent fausse sans que rien ne le signale.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **P1 n'est pas certifiable** dès que (1 − α)ⁿ > δ. La détection devient alors 1 − F_sab(T), avec T proche du maximum des témoins quand nα ≲ 3. La puissance s'effondre si la loi des scores de sabotage F_sab ne dépasse pas ce maximum.
- **La garantie (α, δ) de P1 est fausse** si les témoins forment des grappes de taille m_c avec une corrélation intra-grappe ρ_c > 0. Le n effectif vaut alors n / (1 + (m_c − 1) ρ_c), et le k calculé est trop petit.
- **D0 n'est pas jugeable** tant que le quantile supérieur à 97,5 % du rapport sous H_A dépasse 3. Ordre de grandeur : tant que nα reste de l'ordre de quelques unités.
- **P2 perd sa validité** dès que la loi du score honnête cesse d'être de position-échelle : un paramètre de forme de queue différent suffit.
- **Second volet de P4 :** si la distance en variation totale entre la loi des témoins et celle des honnêtes du flux est d_TV > 0, la probabilité d'un faux signal de sabotage tend vers 1 quand le flux grandit.

### (c) Contrôles négatifs dont l'absence serait fatale

- Pour P4, un **monde sans aucun sabotage**, où une source bénigne nouvelle est présente dans le flux mais absente des témoins. Le signal de sabotage doit rester au niveau δ. Sans ce contrôle, P4 transforme tout défaut de couverture des témoins en alarme de sabotage.
- Pour P1, une **permutation par blocs** (grappes de témoins), qui mesure la fraction de répétitions où le taux dépasse α sous dépendance.
- Pour D2, une **évaluation sur des honnêtes cachés**, distincts des témoins qui ont servi à re-standardiser.

---

## Sur la proposition C

### (a) Défauts de méthode

- **Statuts.**
  - C donne à ses références de mémoire le statut VÉRIFIÉ.
  - C écrit « 1 % → 3 % [RAPPORTÉ / VÉRIFIÉ] » : c'est un statut hybride.
  - C marque N_cal ∈ [200, 500] comme VÉRIFIÉ alors que c'est sa propre lecture de « quelques centaines » ; ailleurs, il le marque illustratif.
  - L'interdiction de moyenne sur les jetons est marquée OBSERVÉ-NON-AUDITÉ puis VÉRIFIÉ.
  
  Je ne modifie rien ; je signale que la règle 1 est en cause.
- **Fuite dans P1.** Les courbes m(L) et σ(L) sont ajustées sur le même échantillon qui fournit les résidus conformes. Le résidu d'un épisode futur n'est donc pas échangeable avec ceux de l'étalonnage. La garantie « conforme exacte à échantillon fini » n'est pas établie. Il faut un découpage : par exemple 150 épisodes pour l'ajustement et 150 pour l'étalonnage (illustratif), ce qui laisse encore au moins 99 points pour un seuil à 1 %. Par ailleurs, la « validité conditionnelle par tranche à O(N^{-1/2}) » n'est pas démontrée ; c'est une HYPOTHÈSE.
- **TARR (P2) : les ancres créent un régime à part.** Les ancres sont produites par une configuration différente de la production : masque syntaxique, bac à sable, ou alignement sur les préfixes du jumeau. Elles définissent donc un régime distinct de celui du trafic. C ne mesure nulle part l'écart entre ces deux régimes. « Immunité totale » est un superlatif. L'immunité ne vaut que si l'agent ne distingue pas les ancres du trafic, ce qui n'est pas testé.
- **TARR : la garantie est mal située.** « FPR ≤ α + O(K⁻¹) » ne peut valoir qu'en espérance sur le tirage des ancres. Le taux réalisé par lot fluctue à l'ordre K^{-1/2} sur le score.
  - Avec K = 15, l'erreur-type de la médiane vaut environ 1,25σ/√15, soit 0,32σ (calcul illustratif).
  - C'est comparable au décalage de 0,445σ qui triple le taux sous loi gaussienne (chiffre de A, que je reprends en le disant).
  - Une erreur de plus de 0,445σ dans le mauvais sens survient dans environ 8 % des lots, avant même de compter l'erreur sur la MAD (calcul illustratif).
- **SCEM (P3) est aveugle aux sabotages en un pas, quel que soit λ.**
  - Avec κ = 0,5, l'e-facteur maximal vaut 0,5·√(N + 1), soit environ 8,7 pour N = 300 (calcul illustratif).
  - Comme 8,7 < 100, aucun pas isolé ne peut déclencher l'alarme. Même avec λ = 1, il faut au moins trois pas extrêmes, car 8,7² ≈ 75 < 100 < 8,7³ (calcul illustratif).
  - Ce que C présente comme un compromis réglable par λ est en fait une cécité de structure.
  
  Deux autres problèmes :
  - « λ ajusté pour que E[e_t | F] ≤ 1 » est une confusion : λ n'intervient pas dans cette condition.
  - Les p-valeurs de tous les pas sont calculées contre un même ensemble d'étalonnage. Elles ne sont donc pas conditionnellement super-uniformes, et la propriété de martingale n'est acquise qu'en moyenne sur cet étalonnage.
  
  À l'inverse, la forme multiplicative M_t = M_{t−1}(1 − λ + λ e_t) est correcte : c'est bien une martingale de test lorsque les e_t sont valides.
- **Les duels ne sont pas jugeables.**
  - Les seuils de 1,3 % et 1,5 % sont appliqués à des estimations ponctuelles, sans intervalle.
  - Entre les deux, aucune hypothèse n'est falsifiée (B4).
  - Séparer 1,3 % de 1,5 % avec un test à 5 % et une puissance de 80 % demande de l'ordre de 2,6 × 10⁴ honnêtes par régime (calcul illustratif), contre « quelques centaines ».
- **Expérience 2.** H_B est une disjonction (« dérive de queue OU ACI meilleur »), qui n'est pas exclusive de H_A. De plus, le bras ACI tourne sans étiquettes, alors que C dit lui-même qu'ACI en exige. « H_B falsifiée » est donc acquis presque par construction : c'est un épouvantail.
- **Quota Top-1.** Il contrôle le taux d'alertes, pas le taux de fausses alertes. Dès qu'un lot contient deux sabotages, l'un des deux ne peut pas être remonté.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **P1 perd sa validité par tranche** si la loi de R sachant L dépend de L autrement que par la position et l'échelle. C'est le cas d'un paramètre de forme ξ(L) ou d'un indice extrémal θ(L) qui varie avec la longueur.
- **TARR échoue** si :
  - la loi des ancres diffère de la loi des honnêtes en production (d_TV > 0), ou
  - le rapport (q₀,₉₉ − q₀,₅)/MAD change entre régimes.
  
  Le duel par lot n'est pas jugeable tant que Var(médiane) ≈ 1,57σ²/K reste du même ordre que le décalage à détecter.
- **SCEM a une puissance nulle** contre toute alternative où moins de ⌈log 100 / log(0,5·√(N+1))⌉ pas sont extrêmes (trois pas pour N = 300, calcul illustratif).
- **Expériences 1 à 3 :** elles ne sont pas jugeables avec n·p(1 − p)/Δ² ≪ 8, où Δ est l'écart entre les seuils de décision.

### (c) Contrôles négatifs dont l'absence serait fatale

- Pour TARR : **comparer, dans le même lot, les ancres à de vrais honnêtes cachés** qui ne servent jamais d'ancre. Sans ce contrôle, la représentativité des ancres n'est pas testée. C'est le défaut principal de TARR.
- Pour P1 :
  - un **monde où la forme de la queue dépend de L** ;
  - un **placebo** où L est permutée avant l'ajustement de m et σ. Si le placebo « corrige » autant, c'est le découpage qui fait le travail, pas la longueur.
- Pour SCEM : un **sabotage concentré en un seul pas**. C le mentionne, mais ne le présente pas comme une issue que la règle ne peut pas passer.

---

## Sur la proposition D

### (a) Défauts de méthode

- **D-ancre : la garantie ne correspond pas au critère du §4.**
  - La garantie de rang est marginale : elle porte sur une cible honnête, en moyenne sur le tirage des témoins.
  - Le critère du §4, lui, porte sur le taux par régime, qui doit être ≤ 1 %.
  - Avec m = 99 témoins, le taux réalisé dépasse 1 % chaque fois qu'aucun témoin ne dépasse le quantile à 99 %, soit avec une probabilité 0,99⁹⁹ ≈ 0,37 (calcul illustratif).
  - Si l'on regroupe plusieurs lots, le taux marginal vaut presque exactement α. La borne supérieure d'un intervalle ne peut alors jamais passer sous α : **H_A n'est jamais confirmable**, et seule H_B peut être falsifiée.
  - Le duel est donc asymétrique par construction. Il faudrait un niveau nominal α′ < α, ou une tolérance fixée d'avance.
- **Une conjonction coûteuse.** H_A exige « tous les critères », sur chaque régime et chaque groupe revendiqué, avec des bornes simultanées. La puissance pour confirmer H_A décroît avec le nombre G de groupes. Avec peu d'honnêtes, le duel ne peut se conclure qu'en défaveur de la règle.
- **D-enveloppe meurt par construction sur la famille de test.**
  - Un triplement au vieux seuil impose une différence d'au moins 0,02 entre les probabilités de queue à ce seuil.
  - L'enveloppe ε est uniforme sur tous les seuils candidats : on a donc ε ≥ 0,02 > 0,01.
  - La condition U + ε ≤ 0,01 est alors impossible et le certificat n'est jamais délivré.
  - D devrait l'énoncer : la règle n'est pas testable sur la famille qui définit le défaut, elle y est seulement muette.
  
  Par ailleurs, ε n'a pas d'estimateur. S'il est tiré des régimes passés, un régime nouveau peut sortir de la famille sans que rien ne le détecte.
- **La recomposition proposée au §1 manque de résolution.** Recomposer le taux à partir de taux conditionnels par tâche suppose des taux de l'ordre de 1 % estimés sur quelques dizaines d'épisodes par tâche. La plupart des estimations vaudront 0/n. Le résidu de recomposition sera dominé par ce bruit.
- **Choix du comparateur.** « Le meilleur contrôle mécanique admissible » est choisi parmi plusieurs candidats. C'est une sélection : il faut soit un comparateur unique pré-enregistré, soit une correction pour la multiplicité.
- **Statuts.** Des attributions bibliographiques sont marquées VÉRIFIÉ ; je le signale sans rien modifier. Par ailleurs, D emploie le même mot VÉRIFIÉ pour « démontré » et pour « attesté sur données » ; l'arbitre devra distinguer les deux sens.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D-ancre :** aucune alerte n'est possible si m + 1 < 1/α. Le duel n'est pas jugeable en faveur de H_A si le taux marginal de la règle vaut α et que le critère est « ≤ α » sans tolérance.
- **Témoins partagés entre décisions :** les alertes d'un même lot sont corrélées. La variance du taux par lot est celle d'une loi Beta(1, m), pas d'une binomiale de taille égale au lot.
- **D-enveloppe :** la puissance est nulle dès que ε ≥ α − U, en particulier sur toute famille qui triple le taux.
- **Recomposition :** elle n'est pas informative quand n_tâche · α ≪ 1.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Des témoins reconnaissables** : l'agent reçoit un marqueur de témoin. Il faut mesurer si le rang de la cible bouge. D cite ce risque mais ne fixe pas le contrôle.
- **Le lot comme unité de réplication**, avec des témoins réutilisés d'un lot à l'autre, pour mesurer le couplage des alertes.
- **Un monde où la queue des vrais honnêtes dérive sans que celle des témoins bouge.** D le prévoit. Je le marque comme indispensable : c'est le seul contrôle qui teste réellement la qualification des ancres.

---

## Sur la proposition E

### (a) Défauts de méthode

- **Canary-eMix : la garantie de Ville ne tient pas conditionnellement à l'étalonnage.**
  - E vérifie E[e_j] = 1 sous H0. Le calcul est juste : 3 × 0,01 + (0,97/0,99) × 0,99 = 1, et la composante p^{-1/2} a bien une espérance de 1.
  - Mais V_j et p_j sont calculés contre un même D_cal fixe. Conditionnellement à D_cal, P(V_j = 1 | D_cal) est le taux réalisé de q_init, qui suit une loi Beta (point de A, que je reprends en le disant).
  - Pour n = 300 et k = 3, ce taux réalisé dépasse 1 % avec une probabilité d'environ 0,42 (calcul illustratif).
  - Dans ces étalonnages-là, E[e_j | D_cal] > 1 même sans dérive. Le produit croît, et la probabilité de révocation à tort dépasse β.
  - La garantie « ≤ β uniformément en tout temps » ne vaut donc pas pour l'étalonnage réellement tiré. Il faudrait des p-valeurs séquentielles, avec une référence qui croît (forme de Vovk), ou une garantie énoncée à (β, δ).
- **Proposition 3 : la récurrence n'est pas une surmartingale.**
  - La forme M_s = (1 − λ) + λ e_s M_{s−1} donne bien E[M_s] = 1 pour tout s fixé. Mais pour M_{s−1} < 1, on a E[M_s | F] > M_{s−1}.
  - Le processus revient vers 1 et franchit tout niveau donné avec une probabilité qui tend vers 1 quand T_e grandit, comme les procédures de type Shiryaev–Roberts, qui se jugent en durée moyenne avant fausse alarme.
  - L'affirmation « P(max_s M ≥ 1/α₁) ≤ α₁ quelle que soit T_e » est fausse. C'est précisément le défaut de franchissements répétés que les FAITS demandent de durcir.
  - La forme multiplicative de C n'a pas ce défaut.
- **PF-Gumbel : fuite et perte de signal.**
  - Π_⊥, ŝ_m, â et b̂ sont estimés sur le D_cal qui fournit ensuite le quantile q : même fuite que pour P1 de C.
  - Retirer les directions de variation honnête peut retirer aussi la composante de sabotage. Aucune mesure de détection n'est prévue avant le test de mort.
  - Le jumeau en préfixe forcé lit le texte de l'agent, y compris un texte de sabotage. Si la sonde réagit au contenu textuel plutôt qu'à l'intention, la différence annule le signal. On 