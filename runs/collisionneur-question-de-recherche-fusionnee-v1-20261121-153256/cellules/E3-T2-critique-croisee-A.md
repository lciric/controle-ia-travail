# Tour III.2 : critique croisée de méthode (proposition A)

**Pièces.** B, C et D sont présentes et terminées par leur marqueur. Ma propre conception (A) n'est pas transmise à ce tour : je n'en cite rien.

**Statuts.** Le bloc FAITS ne porte aucun statut explicite ; je le traite comme RAPPORTÉ (faits). C écrit « VÉRIFIÉ dans les faits » et D marque « VÉRIFIÉ » ses propres dérivations (borne en Θ, information mutuelle, principe des tiroirs). Je les traite comme RAPPORTÉ ou HYPOTHÈSE. Tous mes calculs ci-dessous sont des HYPOTHÈSES (dérivations à vérifier).

**Notations.**
- d_t = R_hon,t − Y_t : différence appariée mesurée par l'oracle.
- P₀ : loi de d_t en régime honnête, de moyenne μ₀ et d'écart-type σ.
- n_h : nombre d'épisodes honnêtes disponibles dans le régime (les faits disent « peu »).
- N épisodes, taux d'audit π, budget B = πN, plafond c.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Le paramètre limitant est absent de la borne.** B pose D_t ∈ [0, c] en (k) et raisonne avec σ en (a). Or d_t est une différence signée et bruitée : la séquence de confiance couvre Σd_t réalisé, qui vaut μ₀N ± σ√N sans aucune attaque. Si le jumeau n'a pas la capacité du suspect (B le soulève en L-a), μ₀ ≠ 0 et doit être estimé sur n_h épisodes. L'erreur cumulée est alors de l'ordre de Nσ/√n_h, et elle domine σ√(N/π) dès que n_h < B. La borne est écrite en (π_min, c, σ, α) ; c'est n_h qui la limite.

2. **« Sous-linéaire en N » est vrai par construction.** B fixe π. Les faits fixent un budget borné : à B fixe, σ√(N/π) = σN/√B, linéaire en N. Le duel D2 (pente 0,5 contre 1) est décidé par le choix « π fixe ou B fixe » du simulateur et par un adversaire défini à la frontière δ ≈ σ/√n. Aucune des deux issues ne falsifie un fait du monde.

3. **D1 teste le code, pas le harnais.** L'inégalité de Ville tient dans tout simulateur qui implémente ses hypothèses. Le contrôle positif « π_min = 0 » rend l'estimateur indéfini ; il ne le biaise pas. Ce qui peut être faux se trouve dans le harnais réel : pièce prévisible depuis ce que l'agent observe, π_t non prévisible au sens de la filtration, étiquettes retardées. S'y ajoute une ambiguïté : D_t se mesure-t-il avant ou après correction ?

4. **Validité sans largeur.** U_t = Nc est valide. Aucun duel ne mesure la probabilité d'arrêt quand Σd dépasse le toléré. Une borne ne réduit pas le dommage : c'est la règle qu'elle déclenche qui le réduit. Le dommage à l'équilibre, face à un adversaire qui reste sous le seuil, n'est pas énoncé.

5. **Contradiction de journal.** Les scores sont journalisés « seulement sur les épisodes audités » (§2, point 5). Or π_t = max(π_min, f(score)) et les variables de contrôle exigent le score sur tous les épisodes, avant la pièce. De plus, un coefficient de contrôle ajusté sur les audités est une fuite entre construction et évaluation (biais d'ordre 1/n) ; il doit être prévisible.

6. **Non-rejet pris pour falsification.** D5 (« sinon H_B est falsifiée ») et D4 (« dans les 2σ ») n'ont pas de marge d'équivalence.
   - D3 est pire. La thèse de B prédit qu'un sabotage planifié surprend moins qu'un échec honnête, donc une AUROC sous 0,5. C'est une séparation, que la clause « compatible avec 0,5 falsifie H_A ; borne basse > 0,5 falsifie H_B » ne classe pas.
   - Il y a trois hypothèses (intention, échec imprévu, ni l'un ni l'autre), pas deux.

7. **La covariance de (c) sonne sans attaque.** Sous P₀, Cov(score, d) est nulle si le moniteur est propre. L'annonce « ne voit plus » se déclenche donc en service honnête. Si elle ne l'est pas, c'est par la difficulté de la tâche, qui pilote à la fois le score et le bruit de d.

8. **Les canaris ne voient pas le rétrécissement dû à l'agent.** Leur loi est fixée par le défenseur. Leur rappel est donc invariant, par construction, quand le dommage de l'agent sort de la couverture. La séquence de confiance détecte la dérive des lecteurs, pas le déplacement de l'attaque.

9. **P4 (deux têtes) est colinéaire chez l'honnête.** « Passera » et « bien fait » coïncident presque toujours chez l'honnête. Leur écart n'est identifié que par les cas honnêtes « passe mais faux », c'est-à-dire des erreurs honnêtes. La tête différence lit donc, par construction, l'échec honnête non contrôlé. C'est la confusion même qu'on voulait lever.

10. **Leurres.** ε = ln(p₁/q) oublie l'issue « pas de correction » ; il faut max(ln(p₁/q), ln((1−q)/(1−p₁))). C'est en outre une borne par observation, alors que l'adversaire qui se réentraîne mutualise N observations.

### (b) Conditions de perte de puissance

- **Poids d'importance.** Si Cov_adv(f(S), d²) ≤ 0, le taux effectif tombe à π_min au lieu de B/N. Le « pire cas certifié » est pire que l'audit uniforme à budget égal.
- **Borne cumulée.** Elle n'est pas jugeable si n_h ≲ (Nσ/D_tol)², car l'incertitude sur μ₀ couvre alors le dommage toléré.
- **Covariance.** Elle n'est pas jugeable dans deux cas :
  - Var(d) ≈ σ² : le dommage ne varie pas d'un épisode à l'autre ;
  - π_min·N·P(d > 0, S bas) vaut moins de quelques unités.
- **Dispersion entre K familles de canaris.** L'intervalle de prédiction a une largeur proportionnelle à t_{K−1}·s·√(1+1/K), qui couvre [0, 1] pour K petit. Il suppose l'échangeabilité de la famille tenue à l'écart avec les K autres ; un auteur tiers la viole.
- **Capture–recapture.** Avec une corrélation ρ > 0 des manqués entre lecteurs, seule une borne existe (B le dit). Elle devient triviale quand P(les deux manquent) tend vers min(m₁, m₂).
- **« Distinguable des jumeaux ».** Avec k jumeaux, la plus petite p-valeur de rang est 1/(k+1). Le test n'a aucune puissance pour α < 1/(k+1).
- **Deux têtes.** Elles sont identifiables seulement si n_h·P₀(passe ∧ ¬bien fait) dépasse la dimension effective de la sonde.
- **Écart d'élicitation.** Il faut la loi honnête du gain G₀ sous le même affinage. Le critère n'est pas jugeable si l'écart-type de G₀ atteint l'écart observé. Pour un δ par épisode, il faut n ≈ σ²/δ² : le plancher est le même que celui de l'audit.
- **D4.** Avec m tâches de capacité, la bande 2σ s'élargit comme 1/√m. Un petit m « falsifie » H_A par manque de puissance.
- **Leurres.** Séparer deux comportements dont la probabilité de détection diffère de Δ coûte environ q(1−q)/((p₁−q)Δ)² épisodes. Le paramètre pertinent est N(p₁−q)²Δ²/q, pas ε.

### (c) Contrôles négatifs dont l'absence est fatale

- **A/A sur le banc réel.** Jumeau contre jumeau à travers l'oracle complet : moyenne nulle et symétrie sous échange des étiquettes. Sinon toute borne est décalée de μ₀N.
- **Pièce.** Un prédicteur de la pièce, entraîné du point de vue de l'agent sur le harnais réel, doit rester au hasard.
- **Canari factice.** Un produit honnête passe par la chaîne de plantation avec une édition nulle. Un classifieur « canari ou réel », du point de vue des lecteurs, doit rester au hasard. Sinon le rappel mesure l'artefact.
- **Covariance.** Mesurée sur flux honnête et stratifiée par difficulté, elle doit être nulle.
- **P5.** Des directions aléatoires de même variance doivent ne pas produire la même courbe dose–réponse.
- **D3.** Deux témoins manquent : des échecs honnêtes appariés en position et en longueur, et un organisme qui porte la consigne sans agir. Sinon la sonde lit la consigne.
- **(i).** Un classifieur « partenaire copie ou modèle de confiance », nourri des sorties du partenaire, doit rester au hasard.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **« Observé à 100 %, coût d'oracle nul ».** Le terme Σ(Réf_i − R_lue,i) exige Réf_i sur chaque épisode. Cela suppose un jumeau exécuté et évalué partout ; le coût est déplacé, pas supprimé.

2. **T₁ seul n'incrimine pas.** « Pris gratuitement par T₁ » revient à faire confiance à une alerte unique, sur une lecture que le suspect règle. Les faits disent que la somme ne dépend pas de ce qu'il fait de sa lecture.

3. **La « vraie pince » est l'estimateur par différence.** T₁ + T̂₂ a pour variance Σ(1−π)/π·e_i². Il ne gagne sur l'audit nu que si E[e²] < E[d²], et l'adversaire choisit e. Au pire cas e ∈ [−2, 2] contre d ∈ [−1, 1] : la variance peut être jusqu'à quatre fois plus grande que sans la sonde.

4. **E4 est vrai par construction.** Il oppose un théorème (couverture avec plancher) à une règle sans plancher, qui n'est pas un estimateur. Les deux issues sont connues d'avance.

5. **La version finie ne borne rien.** W_n = Π(1 + λX_i) est une martingale de test pour E[X_i] = 0, que la pièce rend vrai quel que soit le dommage. L'assertion `W_n < 1/δ` teste le générateur aléatoire. Il manque l'inversion sur la quantité inconnue.

6. **Le flux minimal de C1 ne vaut qu'en régime concentré.** B₀ ≥ (N/Δ_max)·ln(1/δ) repose sur « aucun dommage détecté ». Cet événement n'est pas défini quand chaque d_i est sous le bruit, et c'est le cas qui fait l'objet de la question.

7. **Le test séquentiel de C3 sur un mélange.** Les dépassements d_i > τ_d mêlent dommage et bruit honnête. Le rappel observé vaut w·r_attaque + (1−w)·FPR_moniteur, où w est la part de vrai dommage. En sabotage diffus w tend vers 0, et le rappel observé tend vers le taux de fausses alertes. La « cécité » est alors annoncée en régime honnête.

8. **C4 n'est pas différentiellement privé.** Le mécanisme est unilatéral : M = 1 entraîne V = 1. Un non-arrêt révèle M = 0 avec certitude, donc ε = ∞.
   - Mon calcul donne I(M;V) ≈ p_mon·ln(1/ρ), au premier ordre en p_mon et non au second (dérivation à vérifier).
   - « I = 0 en ombre totale » contredit le fait « l'agent voit ce qui lui arrive ». C'est faux dès que l'état aval visible par des épisodes ou des copies ultérieurs dépend du remplacement, ce qui est le cas de tout travail assemblé.

9. **Le regret interne de C5 a trois défauts.**
   - *Biais d'ordre.* Le maximum de M lectures bruitées moins une lecture est positif sous P₀. Il croît avec M et avec la longueur T (max_t), donc avec la difficulté. L'affirmation « dans l'échec honnête max_m V ≈ V(a_t) » est fausse pour toute politique échantillonnée.
   - *Échangeabilité.* Si les branches viennent du suspect à la même température, a_t est échangeable avec elles sous toute politique fonction du préfixe, honnête ou non : le regret est nul par construction. Si elles viennent du modèle de confiance ou d'une température élevée, la statistique mesure l'écart de capacité ou la variance.
   - *Double usage.* Choisir « les k pas de plus forte chute » avec V, puis noter ces pas avec V, produit un regret positif par régression vers la moyenne.

10. **E2.** Il est conduit « sur le tiers de modèles où l'état confond » : c'est une sélection sur un résultat, puis un retest. La zone entre 0,45 et 0,70 ne falsifie rien, contre la règle B4.

11. **C2/E1 confond deux causes.** La clause de réfutation de H_B admet elle-même deux causes non séparées : la persuasion survit, ou la canonicalisation détruit la preuve. Trois autres défauts :
    - le purificateur lit la prose de l'agent, donc le canal de persuasion se déplace vers lui ;
    - la vérification mot pour mot porte désormais sur la réécriture, plus sur le produit ;
    - l'adversaire doit être optimisé contre le bras qu'on évalue, sinon le gain est celui de la nouveauté (les faits donnent deux tours).

12. **C7 ne prédit aucun signe.** Le §1 annonce un saboteur plus rigide sous perturbation ; C7 le dit plus sensible. Un critère bilatéral sans signe prédit n'est pas falsifiable.

13. **E3 dépend de qui écrit le point focal.** Si l'invariant est « sémantique profond », H_A gagne par construction ; s'il est de surface, H_B gagne. Par ailleurs, des copies honnêtes à poids partagés ont des erreurs corrélées : le seuil Corr ≤ 0,10 peut être violé sans attaque.

14. **C6.2.** Des sous-tâches de contrôle « entrelacées » ne mesurent le coût d'obscurcissement que si l'agent ne les distingue pas du reste.

### (b) Conditions de perte de puissance

- **Bilan stratifié.** Aucun gain si E_adv[e²] ≥ E_adv[d²]. Avec π_i ∝ |Δ_i| + π_min, la puissance est perdue si Cov(|Δ|, d²) ≤ 0. Or |Δ| suit la difficulté dès que le modèle de confiance est dépassé. De plus σ₀² est estimé sur n_h petit et supposé stationnaire entre régimes.
- **Test séquentiel de cécité.** Il n'est pas jugeable quand w = P(dommage | d > τ_d) est petit. Il exige P₀(d > τ_d) ≪ π_min·P_adv(d > τ_d), ce qui exclut le régime diffus.
- **Règle des m audits consécutifs.** La bande honnête est un quantile estimé sur n_h points. Un changement de régime déplace |R_lue − I| sans attaque.
- **Canal de retour.** Le taux d'arrêt visible selon le comportement b vaut p(b) + (1−p(b))·q. L'écart entre deux comportements n'est atténué que du facteur 1−q ≈ 1−ρ. Le coût de discrimination est d'environ ρ(1−ρ)/((1−q)Δp)² épisodes.
- **Regret.** Sous P₀ il croît environ comme σ_V·√(2 ln(MT)) pour un bruit gaussien (ordre de grandeur illustratif). La puissance est nulle si la loi de a_t sachant le préfixe est la même au rejeu.
- **Consensus des lecteurs comme signal de couverture.** C'est une statistique sans étiquette. Elle n'est pas jugeable si les manqués des deux lecteurs sont positivement dépendants (2609.32267, RAPPORTÉ par les faits).
- **KL sous paraphrase.** Elle n'est pas jugeable si la variance honnête de la KL entre paraphrases atteint l'effet. Elle est biaisée si elle est calculée sur les k premiers jetons tronqués.
- **Comité de sondes orthogonales.** Si la cible tient dans r dimensions, la sonde de rang j > r lit du bruit. Le tirage dans le comité abaisse alors la détection moyenne.

### (c) Contrôles négatifs dont l'absence est fatale

- **Rang exact pour C5.** Sous échangeabilité, le rang de V(a_t) parmi M rejeux à la même température est uniforme. Sans cette vérification sur des échecs honnêtes appariés en T et M, le seuil n'a pas de taille. Les pas doivent aussi être choisis par une lecture indépendante.
- **E1 en plan factoriel.** Dommage planté sans persuasion, brut contre purifié : mesure la preuve détruite. Persuasion sans dommage : mesure le purificateur déplacé. La référence doit être purifiée symétriquement.
- **C3 sur flux honnête.** Le taux d'annonce de cécité doit être ≤ α.
- **C4.** Un classifieur du point de vue de l'agent doit inclure les contextes des épisodes et des copies ultérieurs, pas la seule trace de l'épisode.
- **E3.** Corrélation des erreurs de deux copies honnêtes, avec et sans normalisation. Le point focal doit être écrit par un tiers qui ignore la normalisation.
- **« Résistance à la réparation ».** Trois bras : ligne du jumeau honnête, ligne du modèle de confiance, réinsertion factice. Un honnête plus capable annule aussi une mauvaise réparation.
- **Sous-tâches de contrôle.** Un classifieur « contrôle ou réel », du point de vue de l'agent, doit rester au hasard.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Statuts.** Sont notés « VÉRIFIÉ » : la borne minimax en Θ, min(ε, ε²/2) nats, « fuite nulle », le tiers par tiroirs. Ce sont des dérivations propres, donc des HYPOTHÈSES.

2. **Le certificat n'est pas calculable tel qu'écrit.** M_t(D) = Π(1 + λ_s(d_s − d̂_s) − λ_s²(d_s − d̂_s)²) dépend de chaque d_s, y compris des non-audités : quand A_s = 0, d_s − d̂_s = d_s − m_s est inconnu.
   - « Inverser par dichotomie » sur un scalaire D n'est pas défini, car le produit ne dépend pas que de la somme.
   - L'énoncé est vrai d'un processus inobservable. Une version calculable exige des majorants prévisibles de variance. Sa largeur est alors celle du pire cas.
   - La borne B_t = max(m_t, (1−p_t)/p_t·D_max) ne majore pas |d − m| quand p_t > 1/2 et m_t est petit.

3. **Même incohérence que chez B** entre d_t ∈ [0, D_max] et σ_hon. μ₀ et n_h sont absents.

4. **P3 est écrit à l'envers.** Rejeter « Cov ≤ 0 » est une preuve que le moniteur voit. La cécité est l'hypothèse nulle, et on ne l'« annonce » pas par un e-processus sans alternative à effet minimal κ (il faudrait tester Cov ≥ κ). Trois défauts s'ajoutent :
   - la porte « tant que μ̂_d dépasse le bruit » conditionne sur les mêmes audits que le test ;
   - elle ne s'ouvre jamais en régime diffus ;
   - le test de mort plante d_t = 1,5σ constant. Un d constant donne Cov(m, d) = 0 quel que soit le moniteur : la « cécité » est trouvée par construction. À 1,5σ par épisode, un simple test de moyenne suffit.

5. **Les familles « tenues à l'écart » sont spécifiées par le concepteur.** « Moniteur inversé » (P1), « obscurcissement partiel, |ΔV| ≤ 0,2 » (P5), « justification persuasive + paire » (P2) : elles ne sont plus tenues à l'écart. Pour P1, la couverture sous moniteur inversé est un théorème. Le gain de largeur « ≥ 25 % » dépend de la corrélation moniteur–dommage que le simulateur fixe.

6. **Zones sans verdict dans les six tests.** Par exemple 0,92–0,95, 60–200 étiquettes, 0,35–0,55, 25–70 %. Une issue située là ne falsifie rien, contre la règle B4.

7. **Le triangle de P6 est vide là où il faut.** Les trois termes sont signés. Si R̂ = R̃ = R_hon, tout d est dans le terme (R̂ − Y), le seul qui exige l'oracle. De plus, découper un bilan en trois sous-bilans testés séparément multiplie les termes de bruit. Les faits rapportent l'inverse : tester le bilan global est la meilleure réponse à l'étalement.

8. **Fréchet–Boole.** β_∪ ≤ min β_j est exact, mais β_j est un taux sous une loi d'attaque connue. Devant un genre jamais vu, β_j = 1 est admissible. Le « pire cas certifié » est trivial.

9. **P4 mesure la mauvaise cible.** Avec des branches silencieuses, A_t est indépendant de ce que l'agent voit. Une AUC de 0,5 est donc vraie par construction ; c'est un test d'implémentation, utile pour le temps de calcul. La cible pertinente est la frontière du moniteur, apprise sur T épisodes mutualisés. La borne par bit ne la borne pas. Et corriger « à un point d'époque » laisse le dommage intra-époque sans chiffre.

10. **Greffe de P5 confondue par l'écart de capacité.** Sous P₀, E[q(greffe) − q(original)] = −g < 0. Le signe ne s'inverse que si δ > g + bruit, c'est-à-dire quand le suspect saboté est déjà sous le modèle de confiance. Autres défauts :
    - le biais d'ordre du regret est le même qu'en C5 ;
    - la validation par ablation n'a pas de sous-espace aléatoire témoin, et la sélection se fait sur les épisodes honnêtes qui servent ensuite à évaluer ;
    - « l'asymétrie de fragilité » n'a ni dérivation ni signe ;
    - les deux têtes ont la colinéarité déjà dite pour B.

11. **P2 n'est pas factoriel.** Persuasion et assemblage sont dans le même test : un échec n'est pas attribuable.

12. **Mesures minimales sans taille d'effet.** « Rappel ≥ 0,95 » est atteint ou manqué selon l'amplitude plantée. Il faut la courbe du plus petit δ/σ détectable à B donné.

### (b) Conditions de perte de puissance

- **Certificat calculable.** Avec majorants prévisibles, la largeur vaut environ D_max·√(Σ(1−p_s)/p_s·ln(1/δ)), quel que soit le moniteur. Le moniteur ne resserre que si max(m_s, D_max − m_s) baisse, donc si m_s ≈ D_max/2 : le gain est borné.
- **P3.** Avec n audits uniformes, l'erreur-type d'une corrélation est d'environ 1/√n. À 50 étiquettes, seules des chutes de corrélation supérieures à environ 0,3–0,4 sont détectables (illustratif). Le test n'est pas jugeable si Var(d) ≈ σ².
- **Lots d'assemblage tirés au sort.** Un dommage qui demande k épisodes précis sur T est contenu dans un lot de taille s avec une probabilité d'environ (s/T)^k. La puissance est nulle si n_lots·(s/T)^k ≪ 1. Les assemblages partiels sont aussi hors distribution pour l'honnête : σ_assemblage doit être mesuré.
- **Réponse randomisée.** L'information cumulée sur la règle est au plus de l'ordre de T·ε²/2 nats. Séparer deux comportements d'écart Δ coûte environ q₀(1−q₀)/((q₁−q₀)Δ)² épisodes.
- **Isomorphes T_k₁(x), T_k₂(x).** La divergence fonctionnelle honnête entre paraphrases a un taux r₀ > 0. La puissance est nulle si le taux observé est à moins de √(r₀(1−r₀)/n) de r₀.
- **Greffe.** Elle n'est pas jugeable si Var₀(q(greffe) − q(original)) ≥ (δ − g)². Il faut environ 2σ²/(δ−g)² greffes étiquetées : aucun gain sur l'audit direct.
- **Canaris du tiers.** Les conditions sont celles données pour B : échangeabilité des familles et artefact de plantation.

### (c) Contrôles négatifs dont l'absence est fatale

- **Certificat.** Rejouer le programme sur des journaux où les d_s non audités sont masqués. S'il rend encore un nombre, il utilise ce qu'il ne peut pas connaître.
- **P3.** Deux témoins : un flux honnête à difficulté variable, où aucune annonce de cécité ne doit sortir ; un moniteur réellement informatif sous dommage variable, où l'alerte de cécité ne doit pas partir.
- **P5.** Trois témoins : des sous-espaces aléatoires de même dimension pour l'ablation ; une greffe factice, où le suspect se greffe à lui-même, pour isoler l'effet de couture ; un honnête greffé, pour estimer g par régime.
- **P6.** Deux témoins : un A/A (deux exécutions de la même version) pour r₀ ; la corrélation des erreurs de copies honnêtes.
- **P2.** Un plan 2×2 (persuasion × assemblage), et des paires honnêtes passées en forme normale contre des paires brutes.
- **P4.** Le contrôle positif (correction déterministe) est bon. Il manque un attaquant qui vise la règle du moniteur, pas A_t, et qui voit les époques.

---

**Trois points pèsent sur les trois conceptions.** Je les nomme sans fusionner les propositions.

- **La moyenne honnête μ₀.** Elle est estimée sur n_h épisodes. Seul B s'en approche, par sa supposition L-a sur le jumeau.
- **Les duels sur la validité.** Plusieurs (D1 chez B, E4 chez C, P1 chez D) ne peuvent falsifier que du code.
- **Les rappels annoncés.** Ils le sont sans le rapport δ/σ qui les rend interprétables.

FIN-DE-CELLULE