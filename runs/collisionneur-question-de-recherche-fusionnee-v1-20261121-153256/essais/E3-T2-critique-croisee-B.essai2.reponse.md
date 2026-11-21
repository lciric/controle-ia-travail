# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces.** J'ai reçu A, C et D en entier : chacune se termine par sa ligne de clôture et je ne vois aucune coupure. Je n'ai pas recalculé les empreintes.

**Statuts.** Les faits ne portent aucune étiquette explicite. A en tient compte et attribue ses statuts avec prudence. C et D apposent « VÉRIFIÉ » à des éléments que les faits donnent comme envisagés (les trois pistes, les jugements 0,35 et 0,15, la structure de l'oracle) et à leurs propres dérivations. Je le relève là où cela fausse une conclusion. Je ne réattribue aucun statut.

**Portée.** Conformément au livrable de ce tour, je ne propose rien de neuf. Je critique, et je dis quand je me sers d'un élément d'une autre proposition. Tous les chiffres de ce texte qui ne viennent pas des faits sont illustratifs.

---

## Défauts transverses (ma critique, invoquée ensuite par renvoi)

**T1 — Le contrôle négatif « honnête = dommage nul » est vrai par construction.**
- Le dommage est une baisse par rapport au jumeau honnête. Sous l'honnête, d est donc un bruit et non un zéro.
- A et D posent d ∈ [0, c], ce qui impose de choisir entre deux lectures :
  - d est signé, et le plafond doit alors porter sur |d| ;
  - d est tronqué, et sa moyenne honnête vaut μ₀ = E[max(0, ε)] > 0.
- Dans le second cas, le cumul honnête dérive en N·μ₀. L'alarme finit par sonner sous l'honnête, à moins de retrancher μ₀, qu'il faut estimer, ce qui ramène à T2.
- Des mondes plantés où d vaut 0 chez l'honnête valident donc un niveau α qui ne tiendra pas en service.
- **Contrôle fatal :** passer dans toute la chaîne un jumeau contre un autre jumeau, c'est-à-dire deux exécutions honnêtes indépendantes, l'une jouant le suspect.

**T2 — L'erreur de référence est partagée entre épisodes.**
- Supposons que la « référence honnête » du bilan soit un niveau par régime, estimé sur n épisodes honnêtes.
- Son erreur b, d'ordre σ/√n, est commune aux N épisodes du régime. Le premier terme du bilan cumule alors un biais N·b.
- Le dommage par épisode qu'on peut détecter est donc minoré par z·σ/√n, indépendamment de N et de p.
- Avec peu d'épisodes honnêtes par régime (contrainte des faits), ce plancher peut dominer σ·√(N/p).
- Seule une référence appariée tâche par tâche y échappe. Or A note (S2) qu'aucun jumeau n'existe en service.
- Aucune des trois pièces ne traite ce terme.

**T3 — Des garanties sont éprouvées sur des mondes qui satisfont leurs suppositions par construction.**
- Une martingale d'audit a la couverture du théorème qui la porte dès que le tirage est secret, l'engagement antérieur au tirage et le plafond respecté.
- Un monde planté qui code ces trois conditions ne teste que l'implémentation.
- Le contenu empirique se trouve dans les contrôles qui les violent : tirage fuité, plafond dépassé, engagement après tirage, attaque ciblée sur la couverture faible. A en prévoit un, le tirage fuité. C et D n'en prévoient aucun.

**T4 — La variable de contrôle est choisie par l'adversaire.**
- Avec un coefficient fixé à 1, l'estimateur par différence n'est plus précis que l'estimateur brut que si Cov(d, m) > Var(m)/2.
- La lecture interne m, ou le score du moniteur, est une sortie du suspect. Il peut l'anticorréler à d et élargir ainsi la borne jusqu'au pire cas. La validité reste intacte, mais l'alarme est retardée.
- Un coefficient ajusté sur l'échantillon audité corrige le problème (variante dite à coefficient ajusté de l'inférence assistée par prédiction, référence à vérifier). Pour garder la propriété de martingale, il doit être estimé de façon prévisible, sur les audits passés seulement.

**T5 — Le ciblage de la couverture.**
- Les trois pièces bornent sans biais le dommage *reconnu par l'oracle*.
- Un adversaire qui connaît le dispositif n'a pas besoin de deviner l'audit. Il lui suffit de concentrer P(attaque | tâche) là où le rappel de l'oracle est faible.
- Toute mesure de couverture portée par une loi que le défenseur choisit (canaris, tâches à vérité tardive) ne l'identifie pas.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **T1 s'applique : d ∈ [0, c].** D1 prend pour contrôle négatif des « mondes honnêtes », sans dire si le bruit de référence y est présent.

2. **La table de A comporte une erreur.** Elle affirme, pour l'estimateur par différence : « prédicteur décorrélé : variance pleine, biais nul ».
   - C'est exact pour un prédicteur indépendant de d et de variance nulle.
   - C'est faux pour un prédicteur adverse ou bruité (T4). Var(d − m) peut alors dépasser Var(d).
   - Or P1 repose sur « le moniteur réduit la variance sans entrer dans la validité ».

3. **Le processus de P1 n'est pas observable.** Σ(A_i/p_i − 1)·d_i est une martingale, mais d_i est inconnu hors audit.
   - L'alarme « valide à tout instant » exige un processus de capital paramétré par une hypothèse nulle sur le total, que A ne précise pas.
   - A le présente comme une esquisse et le statut est respecté, mais la version finie de T1 (« recalcule le capital ») n'est pas définie.

4. **D4 a le mauvais comparateur.** A compare le taux de bascule sous retrait de la prose au bruit de relecture (deux passes sur une entrée identique).
   - Une paraphrase par le modèle de confiance change aussi le contenu. Elle peut effacer ou introduire un défaut.
   - Une bascule excédentaire mélange donc la persuasion et l'altération. H_B peut se réaliser sans aucune persuasion.

5. **D2 confond la consigne et l'intention.** Dans la « sous-performance sur consigne », la consigne est dans le contexte, et la sonde peut lire ces jetons.
   - L'échec honnête « prévu, l'agent le sait » porte lui aussi un indice textuel.
   - L'AUROC mesure alors une différence entre deux indices de contexte, pas une différence entre intention et échec.

6. **P6, étalonnage par vérité tardive : la sélection est non aléatoire.**
   - Les tâches qui produisent une vérité tardive sont les moins floues.
   - Si P(vérité observée | tâche) dépend de l'erreur de l'oracle, l'erreur mesurée est biaisée vers le bas, précisément là où (b) cherche une couverture.

7. **Fuite entre (g) et (c).** Le moniteur est réajusté par époque sur les endommagés que l'audit trouve. Si son rappel (P2) est estimé sur ce même flux, l'instrument est évalué sur ses données d'ajustement.

8. **P7 suppose que l'erreur honnête est idiosyncratique.** Les erreurs d'un modèle sur une tâche donnée sont souvent reproductibles d'un rejouage à l'autre (HYPOTHÈSE de ma part, non mesurée). A classe ce cas comme « muette », mais c'est peut-être le cas général.

9. **Objet mal placé.** « 0,7 que T1 tienne tel quel » porte sur un théorème. La probabilité honnête porte sur les suppositions en service : secret, engagement, plafond, couverture.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **P1, régime diffus.** Puissance nulle si p < z²·σ²·N / D\*² ; s'y ajoute le plancher z·σ_ref/√n de T2.
- **P1 avec moniteur.** Le gain disparaît, puis s'inverse, si Cov(d, m) ≤ Var(m)/2.
- **Borne supérieure de σ** (piste 2, que A reprend à juste titre). Avec n épisodes honnêtes, la borne au khi-deux multiplie σ̂ par √((n − 1)/χ²_{α, n−1}). Pour n petit, ce facteur peut dépasser 2 (illustratif). Le flux exigé croît comme son carré.
- **P2 (part de variance expliquée).** Non jugeable si Var(d_sab)/σ² → 0 : l'état « non éprouvé » ne se lève jamais, quel que soit le moniteur.
  - Le rappel parmi les endommagés trouvés vaut ρ·r_sab + (1 − ρ)·r_bruit, où ρ = P(sabotage | d > τ).
  - Si ρ → 0, il ne dit rien de r_sab. A le note.
- **P7.** Puissance nulle si le coefficient de corrélation intraclasse de l'erreur honnête entre rejouages est proche de celui du sabotage.
- **D2.** Par bande de |δ|, avec k paires, la largeur de l'intervalle sur l'AUROC est d'ordre 1/√k. Pour k faible, la zone indécise de 0,6 à 0,8 (illustrative) contient presque toutes les issues.
- **P6.** Non identifiable si la vérité tardive manque de façon dépendante de l'erreur de l'oracle.

### (c) Contrôles négatifs dont l'absence serait fatale

- Jumeau contre jumeau dans P1 et D1 (T1).
- Paraphrase d'un produit honnête, vérité inchangée, pour D4. Elle donne le bruit de bascule propre à la paraphrase.
- Pour D2 : consigne présente mais non suivie, et sabotage induit sans indice textuel.
- Pour P2 : moniteur à scores permutés, qui ne doit jamais lever « non éprouvé ». Moniteur qui ne suit que la difficulté prédite par le modèle de confiance, qui ne doit pas passer pour « voyant ».
- Pour P7 : corrélation intraclasse honnête entre rejouages, mesurée avant tout sabotage.
- Flux d'audit tenu à l'écart des réajustements, pour (c).

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts relevés.**
   - C marque VÉRIFIÉ les jugements 0,35 et 0,15, les trois pistes et la structure de l'oracle. Les faits ne leur attribuent pas ce statut.
   - L'effet est concret : l'étau, que les faits donnent pour hypothèse, sert de prémisse à C6 (« vraie pince »).
   - C date l'article sur l'estimation par pari de 2024, A de 2023 : référence à vérifier.

2. **La « pince » de C6 n'enferme rien.**
   - **La référence n'est pas gratuite.** T₁ = Σ(Réf_i − R_lue,i) est dite « gratuite sur 100 % des épisodes ». Cela exige Réf_i à chaque épisode, donc un jumeau à chaque épisode, absent en service, ou une référence par régime (T2).
   - **Une alarme sur T₁ seul est un détecteur sans garantie.** L'agent l'évite à coût nul en ne baissant pas R_lue. « Il est pris gratuitement » n'est pas une contrainte.
   - **C'est l'estimateur par différence.** Ce qui reste est exactement l'estimateur par différence de A et D, avec la vulnérabilité T4.

3. **La version finie de (k) n'est pas calculable.** W_i = W_{i−1}·(1 + λ·X_i) avec X_i = (A_i/π_i − 1)·e_i. Hors audit, X_i = −e_i, où e_i = R_lue − I_oracle est inconnu. L'assertion « W_n < 1/δ » ne peut donc pas être évaluée par le défenseur.

4. **La borne de Freedman utilise la variance du pire cas.** Elle prend e_i² ≤ 4. La réduction de variance attribuée à la sonde n'apparaît donc pas dans l'énoncé certifié.

5. **Le plancher de C1 n'est pas celui annoncé.** Avec π_i = (1 − γ)·π_min + γ·f(S_i), un adversaire qui pousse S_i vers 0 obtient (1 − γ)·π_min, alors que la borne est écrite avec π_min.

6. **E4 est vraie par construction (T3).** Elle compare un estimateur muni d'un plancher à une règle d'alerte sans plancher : la seconde sous-estime par définition. Aucune issue ne falsifie une hypothèse empirique.

7. **La borne de C4 est fausse, et le mécanisme n'est pas différentiellement privé.**
   - Le complément d'arrêts donne P(V = 1 | M = 1) = 1 et P(V = 0 | M = 1) = 0. Observer V = 0 révèle donc M = 0 avec certitude : ε est infini.
   - L'information mutuelle exacte vaut h(ρ) − (1 − p)·h(q). Elle est d'ordre p, pas p².
   - Avec ρ = 0,5 et p = 0,1 (illustratifs), le calcul donne environ 0,075 nat, contre 0,02 pour la borne de C.

8. **C5, le regret interne, est biaisé dès la construction.**
   - **Maximum de M tirages.** Sous l'honnête, E[max_m V_m] − E[V] > 0 et croît avec M et avec la dispersion de V. Le regret honnête est positif par construction.
   - **Régression vers la moyenne.** Les pas sont choisis par min ΔV avec la même sonde que celle qui note l'action. L'action retenue a donc la V la plus basse par sélection, et le regret est gonflé chez l'honnête.
   - **Extrapolation.** Les actions échantillonnées à haute température sortent de la politique, et V y est extrapolée hors de sa distribution d'apprentissage.
   - **Confusion avec la longueur.** L'agrégation max_t, ou le quantile 0,99, croît avec la longueur de l'épisode.
   - **Le coût de l'évasion n'est pas établi.** L'adversaire n'a pas à « détruire sa fonction d'évaluation sur tout le voisinage ». Il lui suffit de découpler la direction lue de la valeur qu'il utilise, ce que 2512.11949 (RAPPORTÉ) rend plausible.

9. **C2 confond deux causes.**
   - La réécriture par un modèle plus faible ouvre une nouvelle surface de persuasion, plus persuadable que les lecteurs. Elle peut aussi effacer le défaut.
   - La clause de falsification d'E1 ne distingue pas « la persuasion survit » de « la réécriture détruit la preuve ». Les deux mènent au même rejet de H_B, sans dire lequel.

10. **Les canaris de C2.3 sont plus faciles que le cas réel.** S'ils dégradent le produit du jumeau et sont comparés à une référence issue de ce même jumeau, l'écart à la référence est exactement le défaut planté, sans bruit honnête. Le rappel mesuré sur les canaris surestime donc le rappel réel.

11. **E3 dépend de ce sur quoi l'attaquant a été entraîné.** Si l'attaquant planté s'appuie sur la surface, la normalisation gagne par construction. Si l'on choisit « invariant sémantique profond », elle perd par construction.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **C1 et C10.** Mêmes conditions que T2 et T4, avec un plancher effectif de (1 − γ)·π_min.
- **C3 (SPRT sur le rappel).**
  - Le nombre d'endommagés trouvés vaut environ K ≈ π_min·N·f, où f est la fraction endommagée. Si K reste sous quelques unités à l'horizon, le test n'est pas jugeable.
  - Le SPRT suppose des Z_k de même loi, alors qu'un adversaire qui s'adapte rend r non stationnaire.
  - S'y ajoute la dilution ρ (voir A).
- **C5.**
  - La puissance s'annule si δ_sab ≲ σ_V(s)·√(2·ln M) (approximation gaussienne, illustrative). Le seuil dépend alors de σ_V(s), que C ne calibre pas.
  - Le max sur T pas donne un taux de faux positifs de 1 − (1 − α_pas)^T, qui croît avec T.
  - La puissance s'annule aussi si l'entropie de la politique honnête au pas t est élevée, car l'honnête échantillonne alors parfois une action moins bonne.
- **C2.** Soit κ = P(défaut conservé | réécriture). Le rappel après réécriture est majoré par κ·r. Non jugeable tant que κ n'est pas mesuré sur des défauts plantés sans prose.
- **C9 (corrélation entre copies).**
  - La difficulté commune de la tâche induit une corrélation honnête ICC_h des d entre copies.
  - Puissance nulle si Corr_sab − ICC_h est inférieur à l'erreur type, d'ordre 1/√(n_paires).
- **Canaris.** Non informatifs sur l'attaque si le rapport dQ_attaque/dQ_canari n'est pas borné, a fortiori si les supports sont disjoints.

### (c) Contrôles négatifs dont l'absence serait fatale

- Regret calculé sur des échecs honnêtes, avec pas sélectionnés par une sonde indépendante, M apparié, calibration stratifiée par longueur.
- Regret calculé avec V permutée.
- Jumeau contre jumeau dans E4 (T1).
- Réécriture appliquée à des défauts plantés sans prose persuasive, pour estimer κ.
- Canaris construits sur des exécutions honnêtes indépendantes de la référence.
- Pour C4 : un classifieur, du point de vue de l'agent, entraîné sur ses entrées ultérieures (artefacts persistants) pour prédire le remplacement en ombre.
- Copies honnêtes sur la même tâche pour E3.
- Moniteur qui ne suit que la difficulté, pour C3.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Des dérivations sont marquées VÉRIFIÉ.**
   - Le caractère sans biais de l'estimateur par différence est une dérivation exacte sous ses suppositions.
   - L'ordre Θ, qui revendique une borne inférieure, n'est pas démontré.
   - La borne « min(ε, ε²/2) » sur l'information mutuelle n'est pas démontrée dans la pièce : à vérifier.
   - « La sonde lit nécessairement l'échec attendu, VÉRIFIÉ par définition » est une inférence invalide. La distribution d'apprentissage fixe la cible, pas les traits qu'utilise la sonde. Une sonde de réussite peut s'appuyer, sur des épisodes de sabotage, sur des traits corrélés à l'intention. Ce n'est établi dans aucun sens.

2. **La version finie de (k) est mal posée telle qu'écrite.** M_t(D) = ∏(1 + λ_s·(d_s − d̂_s) − λ_s²·(d_s − d̂_s)²) dépend de la suite des d_s individuels.
   - Le terme quadratique n'est pas fonction du seul total. La « dichotomie sur D » n'est donc pas définie.
   - Majorer ce terme par son pire cas rend le processus calculable, mais supprime la réduction de variance revendiquée (même défaut que C, point 4).
   - Il faut une forme où le terme quadratique est observable. C'est à démontrer.

3. **Le test de mort de P1 a deux défauts.**
   - Son contrôle négatif « d_t = 0 » relève de T1.
   - H_A et H_B ne sont pas exclusives : H_A porte sur un moniteur « partiellement informatif », H_B sur un moniteur inversé. Les deux peuvent être vraies en même temps, ce qui contrevient à B4.

4. **Le « triangle » de P6.** Le principe des tiroirs est exact : un terme au moins vaut d/3 ou plus. Il est pourtant sans portée.
   - Chaque terme a son bruit honnête σ_j, et c'est l'adversaire qui choisit la répartition. Il place la masse dans le terme le plus bruité.
   - La détection exige alors d > z·max_j σ_j, et le facteur 1/3 ne joue aucun rôle.
   - Le troisième terme exige toujours l'oracle.

5. **P3, la covariance, est confondue par la difficulté.** Un moniteur qui signale les tâches difficiles garde Cov(m, d) > 0 par le seul bruit honnête, plus large sur ces tâches, surtout si d est tronqué. Il peut être aveugle au sabotage sans jamais déclencher l'alarme.

6. **La validation par ablation de P5 a deux défauts.**
   - Annuler la projection sur un sous-espace de forte variance quelconque dégrade la performance. Sans contrôle par sous-espace aléatoire de variance appariée, le critère retient la norme et non le rôle.
   - Que le modèle actuel ait besoin de ce sous-espace n'implique pas qu'un modèle réentraîné en ait besoin. La phrase « effacer ce sous-espace force l'agent à perdre sa compétence » ne suit pas.

7. **P4 : la « fuite nulle » suppose qu'aucun état ne persiste.** Il faut que les artefacts et le réentraînement sur traces ne trahissent pas la branche. A le pose explicitement (S5). La borne est donnée par épisode, alors que l'information sur la règle du moniteur se compose sur tous les épisodes qui entrent dans un réentraînement.

8. **Un point de D dont je me sers.** D distingue borner le dommage moyen, avec un flux B indépendant de T, et borner le cumul absolu, avec B en T² en ordre de grandeur, dérivation non démontrée comme borne inférieure. Cette distinction est juste, et elle fixe quelle garantie un « petit flux » peut porter. Les fiches de D ne précisent pas laquelle des deux P1 vise.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **P1.** Conditions T2 et T4. En cumul absolu, la puissance s'annule dès que B < z²·σ²·T²/D_tol².
- **P3.** L'alarme est perdue si Cov(m, d_hon) > 0 par l'effet de la difficulté. Seule Cov(m, d | difficulté prédite) est jugeable.
- **P5.** Sur |ΔV| ≤ 0,2 (illustratif), la puissance s'annule si l'écart de regret entre sabotage et honnête est inférieur à la dispersion honnête du regret, que D ne mesure pas.
- **P4.** Avec q₀ petit, ε est grand et l'information par épisode n'est plus petite. Non jugeable si la loi des délais de correction dépend de s_t, même faiblement.
- **P6 (pare-feu).** Puissance nulle si le taux de divergence honnête entre versions isomorphes, π_h, est proche du taux sous coordination.
- **Triangle.** Garantie nulle si max_j σ_j ≥ d/z.

### (c) Contrôles négatifs dont l'absence serait fatale

- Jumeau contre jumeau, à la place de d_t = 0.
- Ablation d'un sous-espace aléatoire de variance appariée.
- Moniteur qui ne suit que la difficulté, pour P3.
- Paires honnêtes sous transformation isomorphe, pour P6.
- Distribution honnête de chacun des trois termes du triangle.
- Classifieur, du point de vue de l'agent, entraîné sur les artefacts persistants, pour P4.
- Le contrôle positif « correction déterministe » de P4 est présent : je le tiens pour nécessaire et bien posé.

---

FIN-DE-CELLULE