# Proposition A — Tour III.1 (conception à l'aveugle)

Rappel de périmètre : tout ce qui suit porte sur des étiquettes abstraites de familles dotées de probabilités ; aucun contenu, aucun comportement, aucun moyen. Les calculs faits ici à partir du fait 17 (RAPPORTÉ) gardent ce statut : ils sont « calcul refait sur données RAPPORTÉ », jamais VÉRIFIÉ.

## (a) Ce que la question suppose sans que ce soit établi

1. Qu'une classe K de familles peut être déclarée par un schéma de construction avant toute mesure et que ce schéma définit une loi sur K — HYPOTHÈSE (le fait 9, VÉRIFIÉ, en fait une condition de validité, pas un acquis).
2. Que le nombre total de familles est fermé pendant la période des trois énumérations — HYPOTHÈSE.
3. Que les trois sources capturent indépendamment — rejeté (fait 17, RAPPORTÉ, déviance 12,9 / 3 ddl) ; la question le sait mais plusieurs options qu'elle liste le supposent.
4. Que le décompte 22/23/27 et l'appariement en familles canoniques sont exacts — RAPPORTÉ, décompte d'un lecteur unique ; le fait 18 (VÉRIFIÉ) ne garantit que la cohérence arithmétique.
5. Que l'affectation des recaptures aux paires se déduit de la déviance — déduite ici (voir bloc 3), sous la condition que « déviance » désigne G² du modèle d'indépendance.
6. Que l'échec d'une défense est une propriété binaire de la famille, alors qu'il est estimé sur des éléments — HYPOTHÈSE ; d'où la variance à deux niveaux.
7. Que la corrélation entre familles se résume à un seul paramètre numérique — HYPOTHÈSE imposée par le périmètre, non établie.
8. Que les familles découvertes se comportent comme des familles tirées au sort pour la part d'échec ε — HYPOTHÈSE ; si la probabilité de capture est corrélée à la probabilité d'échec, toute borne est biaisée (bloc 2).
9. Que la censure commune (familles inaccessibles aux trois sources) est nulle — HYPOTHÈSE, non testable de l'intérieur.
10. Que l'écart vues / tenues à l'écart informe sur l'inconnu — HYPOTHÈSE ; les familles tenues à l'écart viennent du même mécanisme de découverte.

## (b) Duels d'estimateurs et de définitions

Tous les duels se jouent dans les mondes simulés à vérité connue du point (c). Chiffres de seuils illustratifs.

**Duel 1 — intervalle d'indépendance contre borne de Chao sous dépendance positive.**
H_A : sous dépendance positive entre sources (effet latent commun σ ≥ 0,5, voir (c)), l'intervalle à 95 % du modèle log-linéaire d'indépendance M_0 garde une couverture ≥ 0,90.
H_B : sa couverture tombe sous 0,80 tandis que la borne inférieure de Chao2 reste valide (P(L ≤ N) ≥ 0,95).
Métrique : couverture empirique sur 2 000 mondes par cellule (erreur Monte-Carlo ≈ 0,005). Seuils : 0,90 et 0,80. Contrôle négatif : mondes à indépendance et homogénéité, où M_0 doit atteindre 0,95 ± 0,01 ; sinon le simulateur est en cause, pas l'estimateur. Issue : couverture de M_0 ≥ 0,90 falsifie H_B ; couverture < 0,80 falsifie H_A ; si de plus Chao2 n'atteint pas 0,95, H_B est falsifiée dans sa seconde clause et le duel ne désigne aucun estimateur — ce qui est un résultat.

**Duel 2 — écart vues / tenues à l'écart contre borne de proportion sous découverte sélective.**
H_A : lorsque la probabilité de capture d'une famille est corrélée à sa probabilité de réussite de la défense (paramètre γ > 0), un écart vues / tenues à l'écart inférieur à δ = 0,05 implique une part d'échec parmi les familles non découvertes ≤ ε.
H_B : l'écart reste < δ alors que la part d'échec non découverte dépasse 2ε dès que γ ≥ 0,3.
Métrique : P(part d'échec non découverte > 2ε | écart < δ). Seuil : 0,20. Contrôle négatif : γ = 0, où l'écart et la borne de proportion doivent concorder à ± 0,02. Issue : probabilité < 0,20 à γ = 0,3 falsifie H_B ; probabilité > 0,20 falsifie H_A et disqualifie l'option 2 du bloc 1 comme définition de l'universalité.

**Duel 3 — Chao2 contre couverture de Good-Turing sous scissions à tort.**
H_A : avec 10 % de scissions à tort (une famille comptée deux fois), le biais relatif de Chao2 reste < +20 %.
H_B : il dépasse +20 % alors que l'estimateur de couverture reste sous +10 %.
Métrique : biais relatif médian. Contrôle négatif : taux de scission nul, où les deux estimateurs doivent retrouver leur biais de référence (mesuré au duel 1). Issue : biais de Chao2 < +20 % falsifie H_B ; > +20 % falsifie H_A. Motif : f₁ entre au carré dans Chao2, linéairement dans la couverture.

## (c) Mesure minimale des deux instruments : plan de simulation à vérité connue

**Instrument 1 — estimateur des familles inconnues.**
Mondes : N ∈ {40, 60, 100} familles (illustratif), trois sources. Probabilité de capture p_fs = logit⁻¹(a_s + b_f), avec a_s calibré pour reproduire 22/23/27 à N = 50, b_f ~ N(0, σ²), σ ∈ {0 ; 0,5 ; 1 ; 1,5}. Le facteur latent b_f crée à la fois l'hétérogénéité et la dépendance positive observable entre sources ; un terme de paire supplémentaire τ ∈ {0 ; 0,5} sépare les deux. Erreur d'appariement : fusions à tort φ ∈ {0 ; 0,05 ; 0,10}, scissions à tort ψ idem. Censure commune : part κ ∈ {0 ; 0,10 ; 0,30} de familles avec p = 0 pour les trois sources.
Estimateurs comparés : comptage brut S_obs (**base à battre**), M_0, modèles à une interaction, modèle saturé (u₁₂₃ = 0), Chao2 et sa version corrigée, couverture de Good-Turing et ICE, modèle bayésien à effet latent (prior déclaré).
Mesures : biais, racine de l'erreur quadratique, couverture des intervalles à 95 %, validité de borne inférieure P(L ≤ N). Un estimateur ne bat la base que si |biais| < N − E[S_obs] et si sa couverture dépasse celle de S_obs (nulle par construction).
Contrôles négatifs : (i) monde à capture complète (f₁ = 0) : tout estimateur doit rendre N̂ = S_obs ± 1 ; (ii) monde indépendant homogène : couverture nominale pour tous.

**Instrument 2 — mesure d'universalité.**
Mondes : population de familles avec probabilité d'échec θ_f ~ Beta(a, b) ; m_e éléments par famille (m_e ∈ {20, 50, 200}) ; corrélation entre familles par grappes, corrélation intra-grappe ρ ∈ {0 ; 0,02 ; 0,05 ; 0,10 ; 0,20} ; sélection à la découverte : corr(logit p_capture, logit(1 − θ_f)) = γ ∈ {0 ; 0,3 ; 0,6}.
Mesures : couverture de l'énoncé « part d'échec < ε avec confiance 1 − α » pour la règle du fait 9 et pour la règle corrigée du bloc 2 ; biais de l'estimation de ε.
**Base à battre** : proportion observée d'échecs avec intervalle de Clopper-Pearson ignorant les grappes et le niveau élément. Contrôle négatif : ρ = 0, γ = 0, m_e → grand : les deux règles doivent coïncider avec Clopper-Pearson.

## Bloc 1 — Définition opérationnelle

**Option 1, pire cas.** Énoncé : ∀ f ∈ K, S(f) ≥ τ ; K est la classe déclarée par son schéma, S une statistique au niveau famille (par exemple taux de détection à taux de fausses alertes fixé, estimé sur les éléments). À déclarer : le schéma de K, S, τ, le nombre d'éléments par famille, le mode d'échantillonnage de K. N'autorise rien hors K et, sur un échantillon de K, n'autorise qu'un pire cas *observé* : le minimum sur n familles n'est pas le minimum sur K. Recalcul par un tiers : liste des familles mesurées, valeurs S(f), minimum.

**Option 2, écart vues / tenues à l'écart.** Énoncé : E_{tenues à l'écart}[S] − E_{vues}[S] ≥ −δ. À déclarer : δ, la règle de séparation, le fait que la séparation précède la mesure. Autorise « pas de surajustement aux familles vues » ; n'autorise aucune phrase sur K ni sur l'inconnu, car les deux groupes viennent du même mécanisme de découverte (duel 2). Recalcul : deux moyennes.

**Option 3, proportion.** Énoncé : avec confiance 1 − α, P_K(S(f) < τ) ≤ ε ; quantificateur « pour au moins une part 1 − ε de K ». À déclarer : K, S, τ, ε, α, le modèle de dépendance entre familles (bloc 2), la règle d'arrêt. N'autorise pas « aucune famille n'échoue » et reste conditionnelle à la loi sur K. Recalcul : nombre de familles, nombre d'échecs, formule déclarée.

**Option 4, intervalle de tolérance à deux niveaux** : variante de 3 qui porte sur le quantile ε de la loi de S(f) plutôt que sur un seuil binaire ; même quantificateur, plus coûteux à recalculer.

**Séparation.** « Universelle sur la classe déclarée » est un énoncé sur K sous une loi déclarée ; « robuste à l'inconnu » porte sur le complément de K, que nul estimateur interne n'atteint. Le bloc 3 estime seulement combien de familles *du même mécanisme de découverte* manquent ; le bloc 4 teste l'inconnu de l'extérieur.

**Retenue** : option 3 comme énoncé principal, avec l'option 1 en rapport obligatoire (minimum observé) et l'option 2 comme diagnostic de sélection, jamais comme preuve.

## Bloc 2 — Nombre de familles par simulation

**Énoncé cible** : avec confiance 1 − α, part d'échec de K inférieure à ε.

**Modèle génératif** : familles avec θ_f ~ Beta(a, b) ; m_e éléments par famille, échecs binomiaux ; une famille est déclarée en échec si θ̂_f dépasse un seuil ; dépendance entre familles proches par grappes de corrélation ρ ; mécanisme de découverte avec sélection γ.

**Règle de calcul.** Sous indépendance, le fait 9 (VÉRIFIÉ) donne n ≥ ln α / ln(1 − ε) : 29 pour ε = 0,10. Sous corrélation ρ, l'effectif effectif est n_eff = n / (1 + (n − 1)ρ), qui remplace n dans la formule. Conséquence (calcul refaisable) : n_eff ne peut dépasser 1/ρ ; avec ρ = 0,20 aucun nombre de familles n'atteint n_eff = 29 ; avec ρ = 0,02 il faut n ≈ 68 (illustratif). La corrélation plafonne donc ce qui est certifiable, et ρ doit être déclaré ou estimé avant la mesure.

**Variance à deux niveaux** : un échec de famille masqué par trop peu d'éléments transforme un échec en réussite ; m_e doit donner une puissance ≥ 0,9 pour détecter θ_f ≥ τ_θ (illustratif : m_e ≈ 50 pour τ_θ = 0,10 contre 0,01). La borne à zéro échec s'applique alors au nombre de familles *correctement classées*, et la probabilité de masquage s'ajoute à ε.

**Règle d'arrêt** : plan séquentiel à zéro échec avec dépense d'α déclarée ; ou critère bayésien P(ε_vraie < ε | données) ≥ 1 − α sous un prior déclaré ; un échec arrête la certification de ε et ouvre un plan à un échec (n plus grand).

**Sensibilité** : ρ, γ, m_e, forme de Beta(a, b), part de familles mal classées.

**Découverte.** Les familles découvertes ne sont pas tirées selon la loi de K : la garantie devient conditionnelle au mécanisme de découverte, et si la capture est corrélée à la réussite (γ > 0), ε est sous-estimée (duel 2). La simulation démontre la couverture de la règle *sous chaque (ρ, γ) déclaré* et sa perte au-delà ; elle ne démontre ni le ρ réel ni le γ réel, qui restent des hypothèses à confronter au bloc 4.

## Bloc 3 — Familles inconnues, trois sources dépendantes

**Reconstitution des cellules (déduite ici).** Les recaptures de paire incluent les 14 triples ; les cellules « deux sources seulement » valent donc {2, 2, 3}. Les totaux de source fixent les cellules « une seule source ». Les trois affectations donnent, pour le modèle d'indépendance (N̂ ≈ 39,2 : (1 − 22/N)(1 − 23/N)(1 − 27/N) = 1 − 37/N), une déviance G² de 14,6, 13,4 et 12,85 (calcul refait, arrondis au centième). Seule la troisième reproduit 12,9 : cellules n₁₀₀ = 4, n₀₁₀ = 4, n₀₀₁ = 8, n₁₁₀ = 2, n₁₀₁ = 2, n₀₁₁ = 3, n₁₁₁ = 14 ; la paire (source de 23, source de 27) porte 17. La déduction suppose « déviance » = G² ; le χ² de Pearson vaudrait 11,8 et ne correspondrait pas.

**Estimateurs (données RAPPORTÉ, T = 3 sources, S_obs = 37, f₁ = 16, f₂ = 7, n = 72 captures).**
- Chao2 : S_obs + ((T−1)/T) f₁² / (2f₂) = 37 + (2/3)(256/14) = 49,2 ; version corrigée S_obs + ((T−1)/T) f₁(f₁−1) / (2(f₂+1)) = 47,0. Intervalle log-normal approché [41 ; 78]. Borne inférieure en espérance sous hétérogénéité (Chao, 1987, « Estimating the population size for capture-recapture data with unequal catchability », Biometrics).
- Couverture de Good-Turing : Ĉ = 1 − f₁/n = 0,778 (Good, 1953, « The population frequencies of species and the estimation of population parameters », Biometrika) ; S_obs/Ĉ = 47,6 ; avec correction d'hétérogénéité (type ICE, γ̂² ≈ 0,35) ≈ 55.
- Indépendance M_0 : 39,2 (rejeté).
- Une interaction (Lincoln-Petersen entre une source et l'union des deux autres) : 39,9 ; 40,3 ; 41,2 selon la paire.
- Saturé pour les sept cellules (u₁₂₃ = 0) : m̂₀₀₀ = (4·4·8·14)/(2·2·3) = 149 → N̂ ≈ 186, avec une variance pratiquement non bornée (cellules de 2 et 3 au dénominateur).

**Modèles identifiables** (Fienberg, 1972, « The multiple recapture census for closed populations and incomplete 2^k contingency tables », Biometrika) : M_0, 4 paramètres, 3 ddl ; une interaction de paire, 2 ddl ; deux, 1 ddl ; trois, 0 ddl ; tous posent u₁₂₃ = 0, seule hypothèse qui identifie la cellule vide, et aucune donnée interne ne la teste. Le modèle à interactions de paire égales (type Rasch ; Darroch, Fienberg, Glonek, Junker, 1993, « A three-sample multiple-recapture approach to census population estimation with heterogeneous catchability », JASA) a 2 ddl et représente l'hétérogénéité.

**Sens des déplacements.** Dépendance positive : trop de triples (14 observés, 8,9 attendus), trop peu d'uniques → M_0 sous-estime ; Chao2 reste une borne basse. Hétérogénéité : même signature, même sens. Fusions à tort : baissent S_obs et f₁, haussent les recouvrements → sous-estimation. Scissions à tort : haussent f₁ → surestimation, quadratique pour Chao2 (duel 3). Le signe net de l'erreur d'un lecteur unique est inconnu.

**Estimateur à employer.** Indépendance rejetée : rapporter Chao2 corrigé comme borne inférieure (47) avec son intervalle, la couverture 0,78 comme diagnostic, et déclarer que la borne supérieure n'est pas identifiée (39 à 186 selon le modèle). Un modèle bayésien à effet latent peut donner un intervalle, mais il dépend du prior sur la dispersion, à déclarer. Sous censure commune, tout estimateur ne compte que la population *accessible* ; la part inaccessible est invisible et seule la source extérieure du bloc 4 la révèle. Sous population non fermée, les estimateurs doivent être datés ; N̂ devient une estimation à la date de clôture et un modèle ouvert ou une fenêtre déclarée s'impose.

## Bloc 4 — Validation extérieure chiffrée

Source extérieure : m familles conçues hors du programme, indépendance supposée vis-à-vis des trois sources, probabilité de capture inconnue ; m = 25 illustratif. Les prédictions sont scellées avant la mesure.

**Définition (bloc 1).** Prédiction : parmi les familles extérieures qui relèvent du schéma K, la part d'échec est ≤ ε = 0,10. Statistique : nombre d'échecs ; sous ε = 0,10 et m = 25, P(≥ 6) ≈ 0,03 ; seuil : ≥ 6 échecs falsifie l'affirmation d'universalité sur K au niveau déclaré. Zéro échec ne la confirme pas, il ne la falsifie pas.

**Nombre nécessaire (bloc 2).** Prédiction : la corrélation intra-grappe estimée sur les familles extérieures est ≤ ρ déclaré (0,05 illustratif) ; falsifiée si ρ̂ extérieur > 0,10, auquel cas n_eff et la règle de calcul doivent être revus avant toute certification.

**Familles inconnues (bloc 3).** Prédiction (Good-Turing) : part des familles extérieures hors des 37 observées ≈ f₁/n = 0,22, intervalle scellé [0,10 ; 0,40]. Avec m = 25 : attendu ≈ 5–6 nouvelles ; ≥ 12 nouvelles (≥ 0,45) falsifie la fermeture ou l'absence de censure commune ; 0 nouvelle (P ≈ 0,002 sous 0,22) falsifie l'estimation par excès et suggère des scissions à tort.

## (d) Ancrage matériel

Aucun modèle de langage : simulation statistique seule, Python ou R sur processeur. Plan factoriel du point (c), 2 000 mondes par cellule, quelques centaines de cellules : moins d'une heure CPU pour les estimateurs fermés, environ dix heures CPU pour le modèle bayésien (chiffres illustratifs). Coût matériel négligeable.

FIN-DE-CELLULE