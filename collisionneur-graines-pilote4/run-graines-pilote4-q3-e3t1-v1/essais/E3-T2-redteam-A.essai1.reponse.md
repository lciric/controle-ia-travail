# Tour III.2 — Proposition A — Équipe rouge croisée

**Constat sur les pièces (règle 2).** Le bloc FAITS ne contient aucun fait (VÉRIFIÉ : « Aucun fait n'est joint »). La pièce `E3-T1-conception-B` est absente (statut REFUS) ; je n'en invente rien. La pièce `E3-T1-conception-C` est présente et complète jusqu'à sa ligne de fin. Tout ce qui suit s'appuie sur la question de l'arbitre (RAPPORTÉ) et sur le texte de C (OBSERVÉ dans la pièce). Mes calculs sont explicités et leurs hypothèses marquées ; aucun score n'existe.

---

## Contre la proposition B

Pièce absente (REFUS, acté par l'arbitre). Aucune conception à attaquer ; cette section est vide par construction et je ne la remplis pas.

---

## Contre la proposition C

### (a) Les failles

**F1 — Auto-contradiction sur l'appariement des tâches.** En (a).2, C écrit que le terme (1 − ρ)p(1 − p)/n de la lignée B « traite à tort le bruit de tirage des tâches comme s'il s'ajoutait indépendamment d'une graine à l'autre ». En (c).3, C écrit que cette même formule « est juste pour la variance conditionnelle à la banque fixe ». La seconde lecture est la bonne : la part partagée ρp(1 − p)/n est déjà soustraite, ce qui reste ne s'annule pas par appariement. C a donc ouvert sa critique sur une erreur, l'a corrigée dix paragraphes plus loin sans le dire, et garde la première comme « supposition non établie » de la lignée B. Statut de ma lecture : OBSERVÉ dans la pièce.

**F2 — Duel 2 : les deux issues ne falsifient rien.** C pose le seuil σ̂ ≤ 0,03 à R = 3 (2 ddl). Sous l'hypothèse de normalité et en supposant que σ̂² estime la seule composante « graine » (HYPOTHÈSE, favorable à C), σ̂²/σ² ~ χ²₂/2. Alors :
- P(σ̂ ≤ 0,03 | σ = 0,05) = P(χ²₂ ≤ 2 × 0,36) = 1 − e^(−0,36) ≈ 0,30 ;
- P(σ̂ > 0,03 | σ = 0,02) = P(χ²₂ > 2 × 2,25) = e^(−2,25) ≈ 0,11.

(Calcul explicite ; valeurs de σ reprises de la question.) Autrement dit, quand σ = 0,05 — précisément la valeur pour laquelle C dit que le palier 1 de (b) est sous-dimensionné — le duel conclut « H_B falsifiée, organisme stable » trois fois sur dix. Un duel dont l'issue « falsificatrice » a 30 % de chances sous l'hypothèse qu'elle est censée falsifier ne satisfait pas B4 ; c'est un pile-ou-face habillé. C le sait implicitement : il cite Browne (1995, « référence à vérifier ») pour recommander une borne haute de σ plutôt que l'estimation ponctuelle, puis fonde son seuil sur l'estimation ponctuelle.

**F3 — Duel 4 : le test falsifie l'hypothèse vraie un tiers du temps.** Le rapport F = σ̂²_v6/σ̂²_v3 avec 4 graines (3 ddl) sur 2 graines de plus (2 ddl) suit, sous invariance exacte et normalité (HYPOTHÈSE), une loi F(3, 2). Sa fonction de répartition est (3x/(3x + 2))^1,5. Donc P(F > 4) = 1 − (12/14)^1,5 ≈ 0,21 et P(F < 0,25) = (0,75/2,75)^1,5 ≈ 0,14 : la bande [0,25 ; 4] rejette H_A (invariance) avec probabilité ≈ 0,35 quand H_A est vraie. C annonce « un facteur 2 au plus sur σ » comme si c'était un intervalle de confiance ; ce n'est qu'une bande arbitraire sans niveau. L'issue « H_A falsifiée → ne pas utiliser σ̂_v3 » sera donc tirée un tiers du temps sans cause. Le duel est inutilisable tel quel.

**F4 — Duel 1 : « sans lire aucun score » est faux par construction.** Les trois quantités mécaniques (rondes de conception arrêtées *par l'organisme*, mutations *acceptées*, retours arrière) sont des fonctions des scores que l'organisme calcule sur la part `test` à chaque génération (RAPPORTÉ : la part `test` lui est rendue ; l'organisme arrête lui-même les rondes). Lire N_mut et le nombre de retours arrière, c'est lire un résumé à un bit par génération de la trajectoire des scores. La retenue de lecture est donc contournée par le canal mécanique. Fuite entre construction (l'organisme utilise `test` pour accepter) et évaluation (C utilise ces acceptations pour décider des graines). Elle n'est pas fatale si on la déclare ; C la présente comme « coût nul de lecture des scores ».

**F5 — Duel 1 : seuils satisfaits par construction.** N_mut ≥ 1 et V_arch > 0 sont vrais pour tout organisme dont l'architecte rend trois flottants bruités et qui accepte une mutation vide. H_B (« pathologie mécanique ») ne peut être falsifiée que par un organisme *totalement* inerte ; tout le reste la falsifie sans rien dire de la valeur de l'organisme. Le duel ne sépare « vivant » de « utile » ; il ne sépare que « vivant » de « mort ».

**F6 — Duel 3 : issues non exhaustives et gain mesurable par sabotage de g = 0.** (i) Les deux issues écrites (« IC_bas ≤ 0 ET Δ_test ≥ 0,10 » ; « IC_bas > 0 ET β̂₀ ≥ 0,05 ») laissent un tiers de l'espace sans verdict (IC_bas ≤ 0 et Δ_test < 0,10 ; IC_bas > 0 et β̂₀ < 0,05) : rien n'y est falsifié, contraire à B4. (ii) La mesure est Y_{g=3} − Y_{g=0}. Tout organisme dont la génération 0 est handicapée (paramètres de récompense initiaux mal placés, caste initiale naïve) montre un gain positif sur les deux parts sans apprendre quoi que ce soit de transférable. Le contrôle test/test_final de C ne voit pas ce cas : les deux parts viennent de la même banque, et les références de surface et de provenance (RAPPORTÉ : 0,8056 / 0,8333, maximum des deux) montrent que la banque v3 a des indices de surface exploitables. Un gain par apprentissage d'indices de surface se transfère de `test` à `test_final` et passe le contrôle de C.

**F7 — Contradiction interne sur la mutualisation M/S.** En (a).5, C pose comme HYPOTHÈSE non établie que σ² est le même sur M et sur S. En D3 et au CAS 3, C mutualise σ² entre M et S pour obtenir « 2 ddl » puis « 4 ddl ». Il utilise comme acquis ce qu'il a déclaré non établi, sans test intermédiaire.

**F8 — Contradiction sur le pouvoir de R = 3.** Au tableau du point 1, C écrit que R = 3 est « décisif : distingue un échec systématique (≥ 0,15 d'écart) d'une fluctuation ». En (c).3, C calcule qu'à R = 3 et σ = 0,05 l'écart détectable est 0,19 (RAPPORTÉ) et que la puissance à δ = 0,10 est « 25 % à 35 % ». Pour un gain intra-course à 2 ddl (t₀,₉₇₅;₂ = 4,30, chiffre de C), c'est pire encore. « Décisif » est un superlatif non étayé par les propres calculs de C.

**F9 — Confondant « lot temporel » dans toutes les variantes à graine 1 incluse.** C note (point 4.4) que la graine 1 a couru dans un lot et les graines 2–R dans un autre, puis ignore ce confondant dans D2, D3 et (a). Avec R = 3 et une graine isolée dans son lot, σ̂ confond variance de graine et dérive d'interface : les graines 2 et 3, courues ensemble, se ressembleront plus entre elles qu'avec la graine 1, ce qui gonfle σ̂ sans que rien de l'organisme n'y soit pour quelque chose. L'entrelacement proposé par C (M2, S2, M3, S3) protège M contre S, pas la graine 1 contre les autres.

**F10 — Composante de variance à 3 niveaux et « 118 ddl résiduels ».** C invoque le modèle mixte `(1|tâche) + (1|graine)` et les « 118 ddl tâche × graine » comme gain de précision. Les ddl résiduels n'améliorent pas l'estimation de la composante « graine », qui n'a que 2 ddl ; avec trois niveaux, cette composante est fréquemment estimée à zéro (frontière), ce qui ferait tomber mécaniquement dans « H_B falsifiée » du Duel 2 pour une raison numérique. Affirmation de ma part : HYPOTHÈSE, à vérifier par simulation (voir (c)).

**F11 — La règle « σ̂ → R_(b) » n'est pas gelée et n'est pas aveugle.** Le seuil 0,04 est « illustratif », donc non écrit ; le choix de l'estimateur (g = 0 ou g = 3, M seul, S seul ou mutualisé, modèle mixte ou variance des moyennes) donne plusieurs σ̂ différents et donc plusieurs R_(b). Qui calcule σ̂ voit les moyennes. « Aveugle aux scores moyens » est une intention, pas un dispositif. C cite Kieser & Friede (2000, « à vérifier ») pour affirmer que le niveau α est « intégralement » préservé ; ces travaux, tels que C les rapporte, concernent un pilote *interne* et aveugle, pas un pilote externe sur une autre banque dont le calculateur voit tout.

**F12 — Statut altéré.** C marque VÉRIFIÉ la retenue de lecture (« personne ne lit ») ; dans la question c'est une règle énoncée (RAPPORTÉ), pas un fait audité. La même pièce marque RAPPORTÉ ailleurs. Le relèvement n'est pas anodin : c'est sur lui que C fonde « exclut totalement le data peeking ».

**F13 — D1, étape 2 : sélection avouée, remède inopérant.** C propose d'ajouter des graines si |Δ| ≥ 0,08 sur la graine 1, reconnaît la malédiction du gagnant, et propose d'estimer la moyenne sur les seules graines nouvelles. Mais σ̂ reste calculé avec la graine 1, dont Δ a été sélectionné grand : σ̂ est biaisé vers le haut dans cette branche, et c'est σ̂ qui pilote R_(b) (F11). Le remède protège la moyenne et sacrifie la variance.

**F14 — Critères de branchement non statistiques.** Le CAS 2 oriente le dessin selon le coût réel par course (> 40–60 USD) et le CAS 3 selon la « volonté de Lazar ». Ni l'un ni l'autre n'est un fait sur le bruit. Le coût change le prix de l'information, pas sa valeur ; C mélange les deux colonnes.

### (b) Les scénarios d'évasion

L'adversaire peut être de deux natures : l'organisme (du code qui se réécrit et appelle des modèles) ou un acteur de la boucle de conception qui veut une décision (plus de graines, ou pas). Je donne les deux.

**Évasion du Duel 1 (viabilité mécanique).** L'organisme accepte une mutation vide à chaque génération et ajoute un bruit ε aux trois paramètres de l'architecte : N_mut ≥ 1, V_arch > 0, H_B « falsifiée ». Coût : quelques lignes, zéro appel supplémentaire. Un organisme qui arrête les rondes de conception à la ronde 2 sans rien concevoir passe aussi N_rondes ≥ 2.

**Évasion du Duel 2 (stabilité inter-graines).** Deux stratégies opposées, selon ce que veut l'acteur :
- Pour paraître stable (σ̂ petit, κ grand) : un organisme qui ne fait rien entre g = 0 et g = 3 (ou qui met en cache ses réponses, ou qui réduit la température des appels) est trivialement reproductible. L'instrument conclut « stable, pas besoin de R = 5 » exactement pour l'organisme le moins intéressant. Coût : nul.
- Pour paraître instable (justifier plus de graines ou un palier 1 de (b) à 6) : lancer les graines 2 et 3 à des heures de charge différentes, ou sans entrelacement avec la graine 1 (F9). Coût : zéro, c'est de la planification.

**Évasion du Duel 3 (gain g0 → g3).** Un organisme à génération 0 sabotée (F6) montre Δ > 0 sur `test` et `test_final`. Pour passer en plus le contrôle test/test_final, il suffit que ce qu'il apprend soit un indice de surface présent dans les deux parts — ce que la référence de surface à 0,8056 (RAPPORTÉ) rend plausible. Coût : nul, et peut même arriver sans intention.

**Évasion du Duel 4.** Pas besoin d'adversaire : à 2 et 3 ddl l'issue est tirée au sort un tiers du temps (F3). Un acteur qui veut invalider le transfert v3 → v6 n'a qu'à attendre.

**Évasion du contrôle « deux agents, deux graines » (instrument 5).** Les agents neufs sont eux-mêmes des modèles non déterministes. Un désaccord entre eux peut venir de l'agent, pas de la graine ; un accord peut venir d'un même biais de lecture (les deux lisent la même part `test`, les mêmes tableaux). L'instrument « prouve » (mot de C) une chose qu'il ne mesure pas sans le témoin « même graine, deux agents ».

**Évasion de la règle σ̂ → R_(b) (F11).** L'acteur choisit, après coup, parmi les quatre à six estimateurs de σ̂ celui qui donne le R_(b) voulu. Coût : nul. Aucune empreinte ne l'en empêche puisque la formule n'est pas écrite.

**Tous à la fois.** Un seul organisme fait passer les Duels 1, 2 et 3 simultanément : mutation vide + jitter de l'architecte (Duel 1), comportement quasi déterministe (Duel 2 : « stable »), génération 0 handicapée puis retour à un classifieur d'indices de surface (Duel 3 : « gain tenu », contrôle test/test_final passé). Le Duel 4 ne contraint rien. Coût total : quelques lignes de code dans l'organisme, zéro dollar d'appels en plus, zéro graine en plus. Le dessin de C aboutit alors à « organisme sain, stable, apprenant ; (b) au palier 1 à 4 graines » pour un objet qui n'apprend rien. Symétriquement, un acteur de la boucle obtient « instable, 6 graines au palier 1 » en décalant deux lancements d'une nuit.

### (c) Les contrôles négatifs dont l'absence serait fatale

Chacun est écrit en duel (B4). Aucun ne touche aux tâches ni ne sert aux organismes.

**CN1 — Rejeu à graine identique (sépare « graine » de « non-déterminisme d'interface »).** La question dit que le non-déterminisme des modèles appelés « ne dépend d'aucune graine » (RAPPORTÉ). La « course nulle » de C mélange donc deux sources sous le nom σ. H_A : deux courses à *même* graine donnent des matrices de réponses sur `test_final` d'accord à plus de κ₀ (seuil à écrire d'avance, illustratif 0,90). H_B : l'accord est au niveau de celui de deux graines distinctes. Si H_A est falsifiée, σ n'est pas une propriété de l'organisme mais de l'interface, et rien de v3 ne se transfère à v6 par le code — la thèse de C au point 1 (« car cette variance provient du code ») tombe. Si H_B est falsifiée, σ̂ de la course nulle mesure bien quelque chose de l'organisme. Sans CN1, le Duel 2 et le Duel 4 n'ont pas d'objet défini.

**CN2 — Organisme gelé (calibre le nul du Duel 3).** La même v6.2.1 avec mutation et architecte désactivés après g = 0, sur la même graine, quatre générations notées. H_A : Δ_{3−0} du gelé est nul à la précision de McNemar. H_B : Δ_{3−0} du gelé est non nul. Si H_A est falsifiée, le « gain » n'est pas un gain d'auto-réécriture mais un effet de la dérive ou du dispositif de notation, et Duel 3 est invalide. Si H_B est falsifiée, le Duel 3 a un zéro mesuré. Coût : une course sans rondes de conception, 4 × 30 USD au plus (RAPPORTÉ pour le prix d'une génération).

**CN3 — Référence de surface rejouée à chaque génération (témoin de dérive et de l'évasion F6).** Les références de surface et de provenance (RAPPORTÉ) doivent passer dans le même pipeline de notation que l'organisme, à chaque génération, sur les deux parts. H_A : leur score est constant d'une génération et d'un lot à l'autre (à la précision des bornes). H_B : il bouge. Si H_A est falsifiée, la dérive d'interface est mesurée et doit être soustraite de σ̂ ; le témoin de C (« latence et empreinte des réponses ») ne mesure pas cela. De plus, un gain de l'organisme qui ne dépasse pas celui de la référence de surface sur `test_final` est le scénario d'évasion F6 ; sans ce témoin il est invisible.

**CN4 — Même graine, deux agents neufs (calibre l'instrument 5).** Avant le « deux graines, deux agents » de C. H_A : deux agents lisant la même course rendent le même verdict sur le registre. H_B : ils divergent. Si H_A est falsifiée, l'instrument 5 lit le bruit de l'agent, et le test de C ne peut rien conclure sur le bruit de graine.

**CN5 — Simulation du Duel 2 et du Duel 4 avant toute course (calibre les seuils).** 10 000 réplications (chiffre de C, illustratif) de matrices 60 × R sous (σ, ρ) sur une grille, estimateur de C appliqué tel quel, taux de « H_A falsifiée » et « H_B falsifiée » sous chaque point. H_A : les deux issues ont, en chaque point de la grille, une probabilité ≤ 0,10 sous l'hypothèse qu'elles sont censées falsifier. H_B : l'une au moins dépasse 0,25. Mon calcul F2/F3 prédit H_B ; si la simulation falsifie H_A, les seuils de C doivent être réécrits (ou les duels abandonnés) avant qu'un score existe. Cette simulation est à coût nul (CPU, C le dit) et c'est le seul contrôle qui peut être fait *maintenant*, sous retenue de lecture.

**CN6 — Formule scellée de σ̂ → R_(b), avec empreinte, et calculateur séparé.** Pas un duel mais un dispositif : un script qui lit la matrice de réponses et n'écrit que σ̂ (estimateur unique, génération unique, parts et questions fixées) et R_(b), poussé avec empreinte avant la fin des courses. Sans lui, F11 et F13 rendent toute adaptation de (b) opaque ; la réserve déclarée de C ne protège pas contre le choix de l'estimateur.

**CN7 — Lot temporel déclaré.** Chaque course porte son heure de début et le lot ; σ̂ est calculé avec un effet « lot » si R ≥ 3 et au moins deux lots. H_A : σ̂ avec lot ≈ σ̂ sans lot. H_B : ils diffèrent d'un facteur 2 (illustratif). Si H_A est falsifiée, inclure la graine 1 comme première graine (option (a) telle qu'écrite) a introduit le confondant F9 dans la quantité même qui dimensionne (b).

### Ce que je reprends de C, en le disant (B1)

Trois points de C tiennent et je m'en sers : (i) la constatation, calculée sans score (RAPPORTÉ), que les bornes de Wilson ne peuvent jamais franchir la référence à ces tailles ; (ii) la critique de McNemar à R = 1, qui contrôle le bruit des tâches conditionnellement à la graine et rien d'autre ; (iii) la remarque que, quand σ domine, doubler la banque n'achète presque rien et seul R compte — ce qui, retourné contre C, dit que la décision la plus coûteuse n'est pas « combien de graines sur v3 » mais « combien au palier 1 de (b) », et que cette décision ne doit pas reposer sur un σ̂ à 2 ddl non calibré (F2) ni sur un transfert v3 → v6 testé à 35 % d'erreur (F3). Sur les références, celles que C cite me paraissent correctement attribuées (auteurs, années, titres) ; elles restent « à vérifier » et je n'en ajoute aucune.

FIN-DE-CELLULE