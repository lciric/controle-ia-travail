# Préenregistrement — extension de l'arène synthétique : familles qu'aucun moniteur seul ne couvre (Q3) et prix imposé à l'adversaire synthétique par une lecture jointe (Q3b) — v1 — BROUILLON 1 (non gelé)

**Statut : brouillon 1, non gelé ; contre-lecture par un modèle autre qu'Opus ; puis gel des seuils par Lazar ; puis scellement ; calcul décisif après celui du pilote principal.**

Identifiant : **PREREG-ARENE-EXTENSION-FAMILLES-V1**. Tâche : extension de l'arène « mélange d'équilibre » (test symétrique, règle R4) décidée par Lazar (R-741 « go », R-743 « relance-le » ; cadrage défensif, niveau méthode, aucune recette), proposée en R-740 « après le calcul décisif » ; plage de racines 20265001–20265999 (R-747). **Modèle mathématique synthétique** : lois gaussiennes paramétriques sur des vecteurs synthétiques de R⁶, moniteurs simples à taux de fausses alertes fixé. Aucun modèle réel, aucun texte, rien d'applicable à un vrai réseau ; l'objet est de **certifier la (non-)couverture d'une défense** et de **mesurer le prix qu'elle impose à l'adversaire synthétique**.

- Auteur : sous-agent neuf Opus 5.5 (lignée conv-audit) ; il n'a écrit aucune pièce de l'arène v1 à v3 (brouillons, codes, contre-lectures, gels).
- Date (UTC) : 2026-10-31 (gel de conception 12:52 ; brouillon écrit de 13:25 à ⟦PILOTE⟧).
- Commit du code d'analyse : À REMPLIR au gel (commit qui contient `arene_extension_v1.py` à l'empreinte du bloc d'identité). Le code n'est pas committé par l'auteur ; HEAD du dépôt à l'écriture : `97dc5f43`, arbre qui ne contient pas le code exécuté : seule l'empreinte du code fait foi pour les pilotes ; la décision exige un arbre propre.
- Documents qui font foi (chemin + empreinte) :
  - `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/preenregistrement-arene-melange-equilibre-v1-brouillon3.md` — `3ac8fe1fd1ee4cdb6ebc904a739f8098226703b02b6c0be428e2a572449dced0` ;
  - `…/arene-melange-equilibre-v1/contre-lecture-arene-melange-v3-brouillon3.md` — `7ccc1460d6925fb1c743cb099a4490fcca2c7146c99ec4098e49234bb15dc236` (constats CM3-01 à CM3-17, dont CM3-02 « la pureté est un plafond de la classe ») ;
  - `…/arene-melange-equilibre-v1/gel-conception-arene-melange-v3.md` — `25035088a36742db86c3b6be818e5c97fabd8dd48c1f9e56934fce15e9f09506` ; `…/arene_melange_v3.py` — `88c8781815007d92d5b0af17a7dc1995c00eae0773085c5a0ca35a1aafee4f0d` (recopié et adapté, jamais modifié) ;
  - `registres/decisions.md`, entrées R-733, R-738, R-739, R-740, R-741, R-743, R-747 ;
  - `docs/sources/pdf/2412.09565v2.pdf` — `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` (conforme à son compagnon ; p. 3 et p. 23 relues pour ce texte, voir « Antériorité ») ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`.
- Code et sorties (dossier `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-extension-familles-v1/`) :
  - `gel-conception-arene-extension-v1.md` — `9b5fc9cf05b9e1204887c0f0351d111d7849f17f4d726cbce452ff5990e187b7` (conception, racines et prédictions écrites **avant tout code et tout calcul**, 12:52 UTC) ;
  - `arene_extension_v1.py` — voir le bloc d'identité (le code de décision refuse de partir si son empreinte, celle de la configuration, des quatre fichiers de bibliothèque et les versions de numpy et scipy n'apparaissent pas dans le texte scellé, si la configuration diffère champ à champ, ou si le calcul décisif du pilote principal n'est pas scellé) ;
  - `essais/test_arene_extension_v1.py` — ⟦PILOTE⟧ ;
  - `essai-pilote-arene-extension-v1.json` — ⟦PILOTE⟧ ; `essai-pilote-arene-extension-v1-pids.txt` — ⟦PILOTE⟧ ; `essai-pilote-prix-arene-extension-v1.json` — ⟦PILOTE⟧ ; `audit-essai-arene-extension-v1.json` — ⟦PILOTE⟧ ;
  - `journal-arene-extension-v1.txt` (commandes, horodatages relevés au fil de l'eau, empreintes, ordre des étapes) ; `LISEZMOI-arene-extension-v1.md`.

Tout nombre de ce texte vient du gel, de la couche exacte (formules), du pilote d'essai (racines 20265011, 20265021), de la mesure de temps (20265031) ou de l'audit d'essai ; ou est un marqueur de gel. **Aucune graine n'a été tirée des racines de décision RACINE_Q3 = 20265901 et RACINE_PRIX = 20265902, ni de la racine de décision de l'arène principale (20261201), ni d'aucune racine déjà employée.**

### Bloc d'identité (vérifié par le code ; à régénérer par `arene_extension_v1.py identite` si le code ou la configuration change)

⟦IDENTITE⟧

## Résumé pour Lazar

⟦RESUME⟧

## Ce que l'expérience n'autorise pas

- **Rien sur les vrais modèles** ni sur des moniteurs d'activations réels (revendication restreinte de P-041 v3). Les « vues » sont des blocs de coordonnées d'un vecteur synthétique, pas des couches ; le canal « comportement » de Q3b est une variable gaussienne, pas une sortie de modèle. Aucun transfert n'est revendiqué.
- **Rien sur l'équilibre de l'arène principale** : l'extension change le monde (moyenne seule, deux modes, vues) ; elle teste l'**instrument** (double oracle, oracle « détection », attaquant local) et la **théorie** (couvrabilité ⇒ pureté) sur des familles dont la réponse est connue exactement.
- **La non-couverture est une propriété construite**, pas une découverte : elle est certifiée par construction (enveloppe convexe pour la classe linéaire ; loi marginale propre pour la classe « une vue »). Le constat de fermeture par union (§ Hypothèse) dit pourquoi, à champ récepteur complet, le régime « aucun maxout de 73 unités ne couvre, une union de deux couvre » est vide : ce n'est pas un résultat expérimental.
- **Queues gaussiennes seulement** : le signe de « union contre mélange » est prédit par la queue des scores honnêtes (R-740) ; rien sur des queues lourdes.
- Deux modes, d = 6, deux budgets δ, T = 8 : rien sur J > 2, d'autres dimensions, d'autres familles, un attaquant en boîte noire, ni des dizaines de moniteurs.
- Q3b est **analytique** sur un modèle à quatre paramètres que nous avons écrit ; le parallèle avec Bailey et collègues (p. 3, p. 23) est qualitatif (le dommage baisse quand on échappe à plus de vues surveillées) ; aucun chiffre n'en est repris, aucune échelle n'en est déduite.
- Ni porte, ni dépense, ni modification de P-041 ; pièce pour la décision de Lazar sur la suite de la piste 3 et pour l'axe 8 de la course 2.

## Portée d'une réfutation et d'une confirmation

- **Q3 « tirage utile là où la classe ne couvre pas, nul ailleurs, instrument étalonné »** établirait : dans ce monde, la valeur du tirage au hasard est grande exactement quand la classe déployée ne peut pas exprimer l'union qu'exige la famille, et nulle quand un moniteur seul couvre ; l'instrument de l'arène (double oracle, oracle « détection », attaquant local) **sait** montrer un tirage utile quand il existe. La pureté de B′ dans l'arène principale serait alors **compatible** avec la couvrabilité des familles v3 par un maxout à 9 unités (CM3-02), non un artefact d'instrument. Elle ne dirait pas que les familles v3 étaient couvrables (non mesuré ici).
- **« Instrument incapable de montrer le tirage »** établirait : là où la couche exacte certifie une valeur du tirage de ≈ 0,4, l'instrument ne la retrouve pas ; la lecture « B′ presque pur ⇒ le tirage ne sert à rien » de l'arène principale serait **suspecte** (audit de l'instrument v3 avant toute phrase de synthèse sur le tirage).
- **« Instrument qui fabrique du tirage »** établirait : l'instrument montre un tirage utile là où il est exactement nul ; l'extension elle-même serait suspecte (audit), et la pureté v3 en sortirait plutôt renforcée.
- **Union contre mélange** : « U > M » dit que, sous queues gaussiennes, l'agrégation déterministe des moniteurs du support fait mieux que leur tirage ; « M > U » contredirait la théorie (audit).
- **Q3b « dilemme majoritaire »** établirait : dans ce modèle, la lecture jointe abaisse strictement le gain maximal de l'adversaire synthétique sous chaque canal seul pour la majorité des configurations tirées ; « minoritaire » : le partage du taux de fausses alertes coûte presque autant que le canal ajouté. Aucune lecture n'indique ce que ferait une pince sur un vrai modèle.

## Antériorité (SUPPOSÉ sauf mention)

Double oracle (McMahan, Gordon et Blum 2003 ; PDF versé au dépôt, R-736, non relu pour ce texte) ; tests maximin et loi la moins favorable, lemme de Neyman–Pearson (Lehmann, *Testing Statistical Hypotheses*, SUPPOSÉ) ; défenses randomisées (Pinot et collègues 2020, SUPPOSÉ). Bailey et collègues, arXiv `2412.09565v2`, **relu sur PDF pour ce texte** (empreinte ci-dessus) : p. 3, « This suggests a trade-off between obfuscation and performance in difficult tasks » ; p. 23 (§ 5.3), « There is a trade-off between obfuscation and model performance. As Fig. 15 shows, obfuscating against more layers reduces performance on SQLEval ». Seul ce fait qualitatif motive la forme du dommage de Q3b ; **aucun chiffre** n'est repris (R7). La zone « prix de l'obfuscation » est en partie occupée (R-744) ; l'extension ne revendique aucune nouveauté (R8).

## Hypothèse

**Constat de conception (avant code, gel § 2) — fermeture par union.** Pour des moniteurs dont la région « non détectée » est convexe (linéaire, maxout à maximum dur), l'union de deux moniteurs recalibrée au taux α est encore un maxout : l'union d'un maxout à k₁ unités et d'un maxout à k₂ unités est un maxout à k₁ + k₂ unités (au log-somme-exp près, écart nul à la limite d'échelle). Donc si une union de deux moniteurs de la classe déployée par requête (maxout à 9 unités) couvre une famille, un maxout seul de 18 unités la couvre, et a fortiori un maxout de 73 unités (même total de paramètres que B′). Le régime « aucun moniteur seul de la classe maxout à k_total unités ne couvre ; une union de deux couvre » est **vide** à champ récepteur complet. Il n'existe que pour une classe non fermée par l'union nécessaire : la **classe linéaire**, et la **classe « une vue »** (le moniteur, linéaire ou maxout de n'importe quelle taille, ne lit qu'un bloc de coordonnées). L'extension retient ces deux régimes, chacun avec un témoin couvrable de même taille.

**Monde.** Loi propre N(0, I₆), α = 0,01. Lois d'attaque N(μ, I₆) (moyenne seule). Famille = réunion de deux boules de comportement : le mode j (une manière de réaliser le comportement visé) a un centre c_j ; l'attaquant choisit μ avec ‖μ − c_j‖ ≤ δ (distance de Wasserstein d'ordre 2), en ne modifiant que les coordonnées libres du mode. Quatre familles appariées par instance (mêmes rayons R₁, R₂ ~ U[4,25 ; 4,75]) :
- **N2** (champ complet) : c₁ = R₁u, c₂ = −R₂u. **Certificat** : pour tout w unitaire, le minimum sur la famille de w·μ vaut au plus −δ (atteint pour w ⊥ u), donc tout moniteur linéaire a une détection au pire cas ≤ Φ(−δ − z) < α. L'union de +u et −u au taux total α couvre (≥ θ*).
- **C2** (champ complet, témoin) : c₁ = R₁u₁, c₂ = R₂u₂, angle γ ~ U[20° ; 45°] ; un moniteur linéaire couvre (Φ(ρ* − δ − z) ≥ θ*, ρ* = distance de l'origine au segment des centres).
- **NV** (deux vues de 3 coordonnées) : c₁ = (R₁u₁, 0), c₂ = (0, R₂u₂), le mode j ne modifie que la vue j. **Certificat** : sous le mode 2, la loi marginale de la vue 1 est exactement la loi propre ; tout moniteur lisant la vue 1, **quelle que soit sa capacité** (linéaire, maxout de 9 ou de 73 unités, détecteur quelconque), détecte le mode 2 au taux α exactement ; idem pour la vue 2. Aucun moniteur d'une vue ne couvre ; l'union d'un moniteur par vue couvre.
- **CV** (vues, témoin) : les deux modes dans la vue 1, angle γ ; un moniteur d'une vue couvre.

**Couche exacte (référence).** V_pur (meilleur moniteur seul de la classe), V_mél (valeur du mélange d'équilibre de la classe), V_union (union de deux), par formules fermées et recherches à une dimension, avec certificat de selle à deux bornes (p* garantit au moins V partout ; q* plafonne toute direction à V) ; témoins : selle pure certifiée ⇒ valeur du tirage exactement nulle (§ Métrique).

**Hypothèses.**
- **H3.1 (valeur du tirage, régime non couvrable)** : VT = V(mélange d'équilibre) − V(moniteur de poids maximal déployé seul) dépasse m = S2 sur N2 (classe linéaire, bras B) et sur NV (classe « une vue », maxout à 9 unités, bras B′V), aux deux δ. H0 : non, pour au moins une famille et un δ.
- **H3.2 (témoins)** : VT est équivalent à 0 à ±m sur C2 (B) et CV (B′V), aux deux δ.
- **H3.3 (étalonnage de l'instrument)** : V(B) − V_mél exact (N2, C2) et V(B′V) − V_mél exact (NV, CV) sont démontrés dans ]−τ ; +τ[, τ = S3.
- **H3.4 (union contre mélange)** : UM = V(U) − V(mélange) dépasse m sur N2 et NV (queues gaussiennes).
- **H3.5 (défense unique)** : sur N2 et NV, A cycle sans couverture (V(A) ≤ V_pur exact + m, changements de mode au-dessus de leur valeur nulle 0,5) ; sur C2 et CV, alternance couverte (V(A) proche de V_pur ≥ θ*). Le taux de retours I3 est rapporté avec sa valeur nulle 0,7345 ; **prédiction écrite au gel : I3 dépasse sa valeur nulle dans les deux régimes**, il ne distingue donc pas un cycle d'une alternance couverte (CM3-03).
- **H3.6 (maxout à champ complet sur N2)** : la classe contient l'union ; VT(B′) ≈ 0 et V(B′), V(D) proches de V_union (descriptif encadré, Table E6).
- **H3b (prix)** : sous la lecture jointe, le gain maximal de l'adversaire synthétique est **strictement** inférieur (de plus de m_b = S14) au minimum des gains sous chaque canal seul, pour une majorité de configurations, et cette part croît avec le nombre L de vues surveillées. Identité (non testée, vérifiée) : G*_joint ≤ min(G*_act, G*_comp), les défenses à un canal étant les bords du partage du taux α.
- **Hypothèses de travail** : oracle du défenseur approché (seuil gaussien, comme la v3) ; attaquant local (SLSQP à départs multiples), contrôlé par un attaquant renforcé et par l'attaquant indépendant (S12) ; témoins PUR et U aux graines de leur bras source (nombres aléatoires communs).

## Prédiction chiffrée et signe attendu

**La décision réplique un pilote** : les probabilités ci-dessous sont conditionnelles au pilote d'essai ; la couche exacte, elle, ne dépend d'aucun tirage de moniteur. Valeurs non opposables ; la décision se lit sur RACINE_Q3 et RACINE_PRIX, jamais lues.

### A. Prédictions du gel (écrites avant tout code) et leur sort au pilote d'essai

⟦PREDICTIONS_A⟧

### B. Prédictions pour la décision

⟦PREDICTIONS_B⟧

## Métrique

Notations : une **tâche** = (famille, δ, instance) ; les familles d'une instance sont appariées (mêmes R₁, R₂ ; même γ pour C2 et CV). Taux de détection d'une défense mixte {(m_i, p_i)} sur N(μ, I) : Σ p_i × part des échantillons dont le score dépasse le seuil t_i de m_i ; seuils au quantile 1 − α de 20 000 échantillons propres communs à la tâche.

- **V(bras)**, principale : après T = 8 tours, défense figée ; meilleure réponse **standard** (par mode : départ vers l'origine, un départ contre chaque moniteur actif, 6 départs tirés dans la boule, attaques passées du mode ; 512 échantillons de Monte-Carlo ; 100 itérations) et **renforcée** (16 départs tirés par mode, 200 itérations, plus la réponse standard) ; chacune évaluée sur 20 000 échantillons frais ; V = la plus basse des deux.
- **Témoins de finale** : PUR = moniteur de poids maximal du mélange (plus petit indice en cas d'égalité) déployé seul ; U = « ou » déterministe des moniteurs du support (poids > 10⁻⁶), score log-somme-exp des scores standardisés multipliés par λ = 8, seuil recalibré à α (un seul moniteur au support : ce moniteur seul). Graines du bras source.
- **Grandeurs par tâche** : VT_B = V(B) − V(PUR_B) ; VT_Bp ; VT_BpV ; UM_B = V(U_B) − V(B) ; UM_Bp ; UM_BpV ; CAL_B = V(B) − V_mél (N2, C2) ; CAL_BpV = V(B′V) − V_mél (NV, CV) ; CAL_U_B = V(U_B) − V_union (N2) ; CAL_U_BpV (NV) ; CAL_PUR = V(PUR) − V_pur ; A − V_pur ; AV − V_pur ; DV − V_pur ; D − B ; B′ − D ; B′ − V_union, D − V_union (N2).
- **Contrastes de régime** (appariés par instance, même δ) : VT_B(N2) − VT_B(C2) ; VT_BpV(NV) − VT_BpV(CV) ; UM idem ; VT_Bp(N2) − VT_Bp(C2).
- **Défense unique (A, AV ; descriptif pour B, B′, D, B′V, DV)** : matrice H (moniteur déployé au tour s × attaque du tour t) ; I1 = moyenne de la détection par tour aux tours 5–8 moins aux tours 1–4 ; I2 = moyenne sur t = 1 … 7 de H[t, t] − H[8, t] (**baisse de détection des attaques passées, oubli ou saturation**, CM3-03) ; **I3** = part des tours t ≥ 3 où le cosinus entre la moyenne de l'attaque et celle d'une attaque d'un tour ≤ t − 2 dépasse celui avec l'attaque du tour t − 1, **valeur nulle 0,7345** sous échangeabilité (vérifiée par simulation, essai `test_indicateurs_cycle_sain_et_valeur_nulle`) ; **I4** = part des tours où l'attaque change de mode, **valeur nulle 0,5**.
- **Couche exacte**, par tâche : V_pur, V_mél, V_union, VT_exact, part de selles certifiées (§ Hypothèse ; formules dans `exact_N2`, `exact_NV`, `exact_couvrable`).
- **Contrôles** : fausses alertes de chaque défense finale (20 000 échantillons propres indépendants) ; V standard − V renforcé ; valeur du jeu restreint − V ; poids (part pure : un poids ≥ 1 − 10⁻⁹ ; support ; poids maximal) ; paramètres par requête et stockés ; vues lues ; entraînements non convergés ; départs non finis ; réponses à la limite d'itérations.
- **Q3b** : pour chaque configuration (R_a, s_D, κ, β₀) et L = 1 … 8, G*_act, G*_comp, G*_joint (partage α_a optimisé sur une grille de 201 points puis affiné ; toute valeur évaluée est atteignable, donc G*_joint rapporté est un majorant du vrai minimum : prudent pour un dilemme), dilemme Δ(L) = min(G*_act, G*_comp) − G*_joint ; part des configurations avec Δ(L) > m_b ; rapport G*_act(8)/G*_act(1) ; monotonie.
- **Intervalles** : rééchantillonnage des instances (ou des configurations), 20 000 tirages, quantiles 0,3125 %, 0,625 %, 1,25 %, 2,5 %, 5 % et symétriques ; graines `SeedSequence(entropy=racine, spawn_key=(99, code_famille, code_δ, code_grandeur))`.

## Seuil

**Tous les seuils sont à geler par Lazar en une ligne datée de `registres/decisions.md`. Aucun défaut ne s'applique.** S1, S5, S6, S7, S8, S9, S11 (interne), S12 (paramètres), S13, S14 (paramètres du générateur, L_max, n_configs) sont des champs de configuration : une valeur différente change l'identité (à régénérer). S2, S3, S4, S10, S14 (m_b), S15 sont des seuils de lecture appliqués par le lecteur R13.

**S1 — seuil de couverture θ\* (champ `theta_couverture`)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,5**.
- Raison (gel, avant code) : point d'inflexion de Φ ; au-dessus, la détection est concave dans la marge et la selle pure des témoins se certifie (vérifiée dans 100 % des instances du pilote, § Prédiction A) ; au-dessous, un mélange peut valoir un peu plus qu'un moniteur seul même sur une famille « couvrable ». Avec J = 2 et des modes symétriques, le mélange vaut au plus ≈ la moitié de la détection d'un mode : il n'atteint jamais 0,5 ; seule l'union l'atteint. La garde `exiger_regime` arrête toute tâche dont la famille n'est pas dans son régime à ce seuil.

**S2 — marge m de la valeur du tirage, de l'union contre le mélange et des contrastes de régime**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02** (deux fois α ; principe de l'arène principale, S1 et S6 du brouillon 3 ; fixé au gel avant code).
- Raison : un écart de détection inférieur à deux fois le taux de fausses alertes est négligeable à ce point de fonctionnement. Les effets prédits (≈ 0,4 pour VT, ≈ 0,3 pour UM) sont vingt fois plus grands : la lecture n'est pas à la frontière.

**S3 — tolérance d'étalonnage τ**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,03** (gel).
- Raison : somme du bruit de Monte-Carlo par tâche (≈ 0,0035), du biais de l'attaquant final (le minimum de deux réponses favorise l'attaquant d'au plus un écart d'échantillonnage) et de l'approximation de l'oracle (seuil gaussien, poids du jeu restreint tronqué à 8 tours) ; assez petit devant VT (≈ 0,4) pour qu'un instrument « étalonné » montre forcément le tirage. Pilote : ⟦PILOTE⟧.

**S4 — erreurs et corrections**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **5 % bilatéral par famille de tests** : E1, E2, E3, E7 et P1, chacune Bonferroni sur 8 cellules (B8, équivalence E8) ; E4 et P2 : B2. Pas de correction entre Q3 et Q3b.
- Raison : les effets prédits sont loin des marges ; la correction ne change aucune classe prédite au pilote (§ Prédiction B).

**S5 — nombre d'instances N par δ et par famille (champ `n_instances`)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : ⟦PILOTE⟧.

**S6 — budgets δ (champ `deltas`)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **(1,0 ; 1,4)** (gel).
- Raison : r = R − δ entre 2,85 et 3,75 : l'union couvre avec une marge d'au moins 0,1 au-dessus de θ* (V_union ≥ 0,60) et la détection d'un mode n'est pas saturée (0,70 à 0,92) ; le témoin couvre (V_pur ≥ 0,55 au pire coin des paramètres).

**S7 — générateur de familles (champs `R_min`, `R_max`, `gamma_min_deg`, `gamma_max_deg`)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **R ~ U[4,25 ; 4,75]**, **γ ~ U[20° ; 45°]** (gel).

**S8 — paramètres hérités de l'arène principale (champs `T`, `unites_Bp`, `lambda_ou`, `tau`, entraînement)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **T = 8**, **9 unités** par moniteur de B′ et B′V (classe de l'arène principale), **λ = 8** ; départs de l'attaquant réduits par rapport à la v3 (3 / 6 / 16 par mode au lieu de 4 / 12 / 48 pour 36 paramètres), l'attaquant n'ayant que 3 ou 6 coordonnées libres par mode.

**S9 — taux de fausses alertes α et tolérances (champs `alpha`, `tol_fpr`)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **α = 0,01** ; garde |taux − α| ≤ 0,005 par défense finale ; déclencheur 4 : |moyenne d'un bras − α| > 0,001 dans une cellule.

**S10 — déclencheur « trop beau / trop mauvais »**
- Valeur : À REMPLIR par Lazar.
- Recommandation : (a) bras sans référence exacte (A, D, B′, AV, DV) : bande = moyenne du pilote ± 4 × écart-type par tâche du pilote × √(1/12 + 1/N) (formule corrigée de CM3-05 : l'incertitude du pilote compte) ; (b) bras à référence exacte : « trop beau » si |CAL| moyen < 0,001 dans les 8 cellules d'E3. Bandes à N recommandé : ⟦PILOTE⟧.

**S11 — temps (champ `plafond_cpu_tache_s` ; délai externe)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : ⟦PILOTE⟧.

**S12 — audit d'attaquant indépendant (champs `audit_*`, `marge_audit`)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **8 tâches de la décision** (instance 0, quatre familles, deux δ), tous les bras de chaque tâche ; 40 départs tirés par mode plus départs structurés, 1 024 échantillons, 300 itérations, évolution (1 + 12) × 200 ; **critère d'artefact en classes** : classe de VT ou d'UM changée (signe et seuil m sur la moyenne des tâches auditées), ou changement de moyenne > m/2 = 0,01 ; V_audit comparé au même minimum côté source (CM3-01). Audit d'essai : ⟦PILOTE⟧.

**S13 — garde de convergence des entraînements (champ `taux_nonconv_max`)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,10** par tâche (au plus 3 sur 34 entraînements en champ complet, 2 sur 26 en vues).
- Raison : valeur retenue par conv-audit pour l'arène principale (R-739) ; mesure de temps : 1 non-convergence sur 120 ; pilote : ⟦PILOTE⟧.

**S14 — Q3b (champs `L_max`, `Ra_*`, `sD_*`, `kappa_*`, `beta0_*`, `n_configs`, `grille_partage`, `grille_x` ; marge de lecture m_b)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **L = 1 … 8** ; **R_a ~ U[2,5 ; 3,5]**, **s_D ~ U[2 ; 4]**, **κ ~ U[0 ; 1,5]**, **β₀ ~ U[0 ; 1]** (gel) ; **M = 400** configurations (champ `n_configs`) ; **m_b = 0,02** (même principe que S2).

**S15 — seuils de lecture de Q3b**
- Valeur : À REMPLIR par Lazar.
- Recommandation : « majoritaire » si la borne basse B8 de la part dépasse **0,5** ; P2 par différence appariée L = 8 moins L = 1 (B2).

**S16 — ordre des calculs décisifs**
- Valeur : À REMPLIR par Lazar (confirmation).
- Recommandation : **le calcul décisif de l'extension après celui du pilote principal**, imposé par la garde `exiger_run_principal` (analyse scellée d'un run décisif sur RACINE = 20261201). Raison : l'extension sert à lire le résultat principal (la pureté de B′), non l'inverse ; aucune lecture de l'extension ne doit pouvoir influencer le gel du pilote principal.

## Plan d'analyse

### 1. Ordre d'exécution (et pourquoi)
(1) Essais du code ; (2) **après** le calcul décisif scellé du pilote principal (arène v4 ou suivante, `diag/<run>/analyse-arene.json` scellé, manifeste décisif sur RACINE = 20261201 ; garde `exiger_run_principal`), une seule invocation `arene_extension_v1.py decision --prereg prereg/<nom>.md --run-principal <run> --instances 0:N --configs 0:M --run-id <AAAAMMJJ-HHMMSS-arene-extension-v1>` sous `timeout` (S11), arbre git propre ; PID et instants de départ des processus de travail consignés et scellés ; (3) analyse écrite par le même processus (`analyse-extension.json`, scellé) ; (4) audit d'attaquant indépendant si un déclencheur l'impose (S12) ; (5) lecture par un sous-agent neuf (R13), qui applique les tables ; `lire_tables` est une aide mécanique partielle (Tables E1 à E5), le texte scellé fait foi.

**Reprise après arrêt** : comme l'arène v3 (§ Plan 5 du brouillon 3) : arrêt de cause externe sans résultat écrit → commande `orphelins` saine, puis une reprise complète (même code, mêmes racines, nouvel identifiant) ; seconde interruption → non concluant ; arrêt par une garde interne → non concluant, version nouvelle du préenregistrement ; aucun point de reprise partiel.

### 2. Bras
- Tour 0 commun à la tâche : moniteur linéaire (d'une vue en régime vues) entraîné contre le mélange uniforme des deux lois de centre (reproductibilité bit à bit vérifiée par garde). Colonnes initiales du jeu restreint : les deux lois de centre.
- Régime champ complet (N2, C2) : **A** (linéaire réentraîné sur le mélange uniforme de toutes les attaques passées, déploie le dernier) ; **B** (double oracle, oracle linéaire contre la stratégie d'équilibre de l'attaquant) ; **B′** (double oracle, oracle maxout à 9 unités) ; **D** (maxout unique à t + 1 unités, réentraîné) ; **PUR_B, U_B, PUR_Bp, U_Bp**.
- Régime vues (NV, CV) : **AV**, **B′V**, **DV** (mêmes règles, chaque moniteur lit une vue ; l'oracle entraîne un moniteur par vue et garde le meilleur objectif d'entraînement) ; **PUR_BpV, U_BpV** (U lit deux vues si le support en couvre deux : hors classe, c'est voulu).

### 3. Graines (R9)
- Décision : **RACINE_Q3 = 20265901**, **RACINE_PRIX = 20265902**, jamais employées. Essai : 20265001 / 20265002 (essais du code), 20265011 (pilote Q3 et audit d'essai), 20265021 (pilote Q3b), 20265031 (temps) ; 20265041 / 20265042 réservées, non employées. Toutes écrites dans le gel avant emploi.
- **Refusées par garde** (`exiger_racine_essai`, et `gen` pour les racines de décision) : 20261201, 20261202 ; 20261291 à 20261298 ; 20262291, **20262297, 20262313** (employées par décalage `RACINE_TESTS + 1000` dans les essais v2 et v3, absentes des textes, ajoutées après le gel, journal) ; 20261301 ; 20261101 ; 20261311 à 20261316 ; 20269501, 20269502 ; 20269731, 20269732 ; 20269741, 20269742 ; la plage 20264001–20264999 (session parallèle) ; toute racine hors de 20265001–20265999. L'essai `test_toutes_les_racines_deja_employees_refusees_et_liste_recoupee_avec_l_arene` recoupe la liste avec tous les nombres 2026xxxx des textes et codes du dossier de l'arène.
- Chaque tirage : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_famille, code_δ, instance, code_bras, tour, rôle, …))` ; familles tirées par `(0, 0, instance, 0, 0, 0)` (indépendantes des familles demandées) ; schéma dans la configuration.

### 4. Comparaisons et multiplicité
- **Tables E1 (VT), E2 (UM), E3 (étalonnage)** : 8 cellules chacune (4 familles × 2 δ) ; Bonferroni sur 8 : bornes B8 = [q0,003125 ; q0,996875] ; équivalence au niveau 0,05/8 par côté : E8 = [q0,00625 ; q0,99375].
- **Table E4 (A, AV)** : bornes B2 = [q0,00625 ; q0,99375] par famille… recopiées ; la règle de classe emploie la moyenne de V(A) et la borne basse q0,0125 de I4.
- **Table E7 (contrastes de régime)** : 8 tests (4 contrastes VT et UM × 2 δ), B8.
- **Q3b (Tables P1 à P3)** : part de configurations avec dilemme, B2 par L sur les 8 valeurs de L (Bonferroni sur 8 : B8).
- « Confirmée » = intersection-union ; aucune correction entre Q3 et Q3b (deux questions).

### 5. Historique de conception (déclaré)
1. Gel 12:52 UTC avant tout code : conception, racines, prédictions (§ Prédiction A).
2. Après le gel, avant le pilote : code écrit (13:02) ; essais révélant (a) deux motifs de garde non uniques (renommés), (b) un certificat de selle trop faible (renforcé en bornes inférieure et supérieure), (c) deux racines employées par décalage absentes de la liste du gel (ajoutées) ; mesure de temps (13:04–13:05, racine 20265031, avant la fin des essais : écart d'ordre déclaré). Code du pilote `fc2625d8…` = code remis.
3. Après le pilote : ⟦PILOTE⟧.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites ; chaque table se lit de haut en bas, la première ligne vraie décide. Notations : est = moyenne ; qX = quantile X ; B8, E8, B2 comme au § Plan 4 ; m = S2 ; τ = S3.

**V0** = aucune condition de la liste d'arrêt ∧ tâches exécutées = 4 familles × 2 δ × N ∧ configurations de Q3b = M ∧ racines du manifeste = RACINE_Q3 et RACINE_PRIX ∧ empreintes du code, de la configuration et de la bibliothèque = celles du texte scellé ∧ run principal scellé antérieur ∧ une seule invocation ayant écrit des résultats (au plus une reprise complète après arrêt externe consigné et commande `orphelins` saine).

**Déclencheurs d'audit (R4), symétriques** — un seul suffit ; effet bloquant écrit :
1. **Contradiction, dans les deux sens** (§ Prédiction B) : une classe d'E1, E2, E3 ou E7 de signe opposé au signe prédit ; une classe prédite « ≈ 0 » observée « > m » ou « < −m » ; E4 autre que prédit ; la part de selles certifiées des témoins < 1. *Bloque* : la table contredite et la phrase de synthèse.
2. **Trop beau / trop mauvais** (S10) : moyenne de V d'un bras sans référence exacte (A, D, B′, AV, DV) hors de sa bande ; ou, pour un bras à référence exacte, |CAL| moyen < 0,001 dans les 8 cellules (une concordance au millième, sous un bruit de Monte-Carlo de ≈ 0,0035 par tâche, est trop belle). *Bloque* : toutes les tables.
3. **Optimiseur** : moyenne de (V standard − V renforcé) > 0,01 pour un bras dans une cellule. *Bloque* : toutes les tables.
4. **Fausses alertes** : |moyenne des fausses alertes finales d'un bras − α| > 0,001 dans une cellule. *Bloque* : toutes les tables.
5. **Jeu restreint** : moyenne de (valeur du jeu restreint − V) < −0,01 pour B, B′ ou B′V dans une cellule. *Bloque* : E1, E3 pour ce bras.
6. **Conforme et trop propre** : E5 « tirage utile exactement là où la classe ne couvre pas… », conforme à la prédiction ; ou toutes les classes d'E1 et E2 conformes. *Effet* : audit d'attaquant indépendant (S12) sur les tâches de la décision, **après** scellement de l'analyse et **avant** la phrase de synthèse ; *bloque* la phrase de synthèse d'E5, pas les Tables E1 à E4.
7. **Défense unique au-dessus du certificat** : V(A) ou V(AV) > V_pur exact + m en moyenne sur N2 ou NV (impossible par construction : un moniteur seul de la classe ne peut pas dépasser V_pur au-delà du bruit) ; ou V(DV) > 0,02 sur NV. *Bloque* : toutes les tables (erreur présumée).

**Contenu de l'audit** : relecture du code par un sous-agent neuf ; attaquant indépendant (SLSQP lourd : 40 départs tirés par mode plus départs structurés et réponses finales, 1 024 échantillons, 300 itérations ; puis stratégie d'évolution (1 + 12) × 200 générations depuis la réponse lourde et depuis la réponse standard) sur les tâches de la décision ; V_audit = min(V, trois réponses), **comparé au même minimum côté source** ; **artefact** si, dans une cellule, la classe de VT ou d'UM (signe et seuil m sur la moyenne des tâches auditées) change, ou si la moyenne change de plus de m/2 = 0,01 (critère en classes, CM3-01 de l'arène v3). Issue : « artefact trouvé » si et seulement si le rapport scellé constate une erreur de code ou le critère ci-dessus ; sinon « pas d'artefact ».

### Table E1 — valeur du tirage, par famille et δ (VT_B sur N2 et C2 ; VT_BpV sur NV et CV), bornes B8, équivalence E8

| Classe | Condition | Sens |
|---|---|---|
| « > m » | borne basse B8 > m | tirage utile, effet d'intérêt |
| « < −m » | borne haute B8 < −m | le moniteur seul fait mieux que le mélange |
| « ≈ 0 » | E8 ⊂ ]−m ; +m[ | tirage sans effet, à la marge près |
| « ≳ 0 » | borne basse B8 > 0 | positif, effet d'intérêt non démontré |
| « ≲ 0 » | borne haute B8 < 0 | négatif, non démontré |
| « ? » | sinon | non tranché |

### Table E2 — union contre mélange (UM_B sur N2 et C2 ; UM_BpV sur NV et CV) : mêmes classes qu'E1 (« > m » se lit « U > M »)

### Table E3 — étalonnage de l'instrument (CAL_B sur N2 et C2 ; CAL_BpV sur NV et CV), bornes B8

| Classe | Condition |
|---|---|
| « étalonnée » | B8 ⊂ ]−τ ; +τ[ |
| « biais bas » | borne haute B8 < −τ |
| « biais haut » | borne basse B8 > τ |
| « ? » | sinon |

CAL_U_B (N2), CAL_U_BpV (NV) et CAL_PUR sont recopiés avec leurs intervalles, sans verdict.

### Table E4 — défense unique (A sur N2 et C2 ; AV sur NV et CV), par cellule

| # | Condition | Lecture |
|---|---|---|
| 1 | moyenne de V(A) ≤ V_pur exact moyen + m ∧ borne q0,0125 de I4 > 0,5 | **cycle sans couverture** |
| 2 | V_pur exact moyen ≥ 0,5 ∧ moyenne de V(A) ≥ V_pur exact moyen − 0,08 | **alternance couverte** |
| 3 | sinon | **autre** |

I1, I2, I3 (avec 0,7345) et I4 (avec 0,5) sont recopiés avec leurs intervalles B2 dans tous les cas.

### Table E5 — Q3 (verdict)

| # | Condition | Verdict |
|---|---|---|
| 0 | V0 fausse | **non concluant** |
| 1 | un déclencheur bloquant toutes les tables (2, 3, 4, 7) est présent et l'audit n'est pas rendu, ou artefact trouvé | **non concluant (audit)** |
| 2 | E1 « > m » pour N2 et NV aux deux δ ∧ E1 « ≈ 0 » pour C2 et CV aux deux δ ∧ E3 « étalonnée » pour N2 et NV aux deux δ | **tirage utile exactement là où la classe ne couvre pas ; nul sur les témoins ; instrument étalonné** |
| 3 | E1 autre que « > m » pour N2 ou NV à un δ au moins | **instrument incapable de montrer le tirage** |
| 4 | E1 « > m » pour C2 ou CV à un δ au moins | **instrument qui fabrique du tirage** |
| 5 | E3 autre que « étalonnée » pour N2 ou NV à un δ au moins | **tirage montré, étalonnage insuffisant** |
| 6 | sinon | **non tranché** |

### Table E6 — maxout à champ complet sur N2 (B′, D), par δ, descriptive encadrée

Recopier VT_Bp (est, B8), B′ − V_union et D − V_union (est, B8), part pure de B′. Lecture : « **la classe contient l'union : tirage inutile** » si VT_Bp « ≈ 0 » (E8) et B′ − V_union > −0,08 (borne basse B8) aux deux δ ; « **la classe ne trouve pas l'union** » si B′ − V_union < −0,08 (borne haute B8) à un δ ; sinon « indéterminé ».

### Table E7 — contrastes de régime (non couvrable − témoin, appariés), bornes B8 : mêmes classes qu'E1 pour VT_B(N2) − VT_B(C2), VT_BpV(NV) − VT_BpV(CV), UM_B(N2) − UM_B(C2), UM_BpV(NV) − UM_BpV(CV)

### Tables P — Q3b

- **P1 (par L)** : part des configurations avec Δ(L) > m_b, intervalle B8 sur les 8 valeurs de L : « **dilemme majoritaire** » si borne basse > 0,5 ; « **dilemme minoritaire** » si borne haute < 0,5 ; « ? » sinon.
- **P2 (évolution avec L)** : « **croissante** » si la part à L = 8 moins la part à L = 1 a une borne basse (rééchantillonnage apparié des configurations) > 0 ; « **décroissante** » si borne haute < 0 ; « ? » sinon. Recopier aussi la part des configurations où G*_act décroît strictement en L, la médiane de G*_act(8)/G*_act(1) et la part (κ ≥ 0,5) où G*_joint/G*_act décroît en L.
- **P3 (verdict Q3b)** : « **pince efficace et croissante avec L** » si P1 « majoritaire » à L = 4 et à L = 8 et P2 « croissante » ; « **pince inefficace** » si P1 « minoritaire » à L = 4 et à L = 8 ; « **pince efficace, sans effet de L** » si P1 « majoritaire » à L = 4 et à L = 8 et P2 non « croissante » ; sinon « **non tranché** ».

**Phrase de synthèse** (lecteur R13, en recopiant, sans rien omettre) : « E5 : … ; E1 : N2 …, C2 …, NV …, CV … (par δ, est [B8]) ; E2 : … ; E3 : … (et CAL_U, CAL_PUR) ; E4 : … (I1, I2, I3 [valeur nulle 0,7345], I4 [0,5]) ; E6 : … ; E7 : … ; P1–P3 : … ; déclencheurs : … ; audits : … ; portée : modèle synthétique, résultat local au monde, aux δ, à T et aux paramètres du générateur ; aucun transfert aux vrais modèles. »

## Liste d'arrêt

Chaque garde du code (73 sites `raise GardeArret`, chacun avec un motif unique) a un essai nommé qui la provoque par son motif (`pytest.raises(…, match=motif)`) et un cas sain ; `test_chaque_garde_a_son_essai` contrôle par l'arbre syntaxique que chaque site a une entrée et un essai nommé existant. Fichier : `essais/test_arene_extension_v1.py`.

| Condition | Action | Garde et essai (R5 : cas sain et artefact) |
|---|---|---|
| Décision sans calcul décisif scellé du pilote principal | pas de départ | `exiger_run_principal` ; `test_run_principal_sain_et_artefacts`, `test_decision_refusee_sans_calcul_decisif_principal_puis_sans_prereg` |
| Décision sans préenregistrement scellé, conforme, identifié | pas de départ ; aucune graine de décision | `autoriser_decision`, `exiger_identite_prereg` ; `test_identite_prereg_sain_et_artefacts`, `test_prereg_scelle_refus_pour_la_bonne_raison`, `test_decision_refusee_sans_calcul_decisif_principal_puis_sans_prereg` (copie temporaire du brouillon : sans compagnon, puis scellée et non conforme) |
| Graine tirée d'une racine de décision sans autorisation ; processus de travail sans préenregistrement | arrêt | `gen`, `_travail` ; `test_gen_garde_racine_de_decision`, `test_travail_refuse_racine_de_decision_sans_prereg` |
| Hors décision : racine de décision, racine déjà employée, plage du pilote b4, hors plage de l'extension | arrêt | `exiger_racine_essai` ; `test_racines_essai_sain`, `test_racines_essai_artefacts`, `test_toutes_les_racines_deja_employees_refusees_et_liste_recoupee_avec_l_arene`, `test_cli_refuse_racines_interdites` |
| Configuration incohérente | arrêt | `exiger_config` ; `test_config_sain_et_artefacts` |
| Couche exacte : centres non conformes, boule contenant l'origine, selle non certifiée, valeur ≠ formule fermée, famille inconnue | arrêt | `exact_N2`, `exact_NV`, `exact_couvrable`, `couche_exacte` ; `test_couche_exacte_gardes`, `test_couche_exacte_formules_et_certificats`, `test_selle_exacte_verifiee_des_deux_cotes` |
| Régime non tenu (famille non couvrable que l'union ne couvre pas, ou qu'un moniteur seul couvre ; témoin non couvrable) | arrêt | `exiger_regime` ; `test_garde_regime_sain_et_artefacts` |
| Selle pure d'un témoin non certifiée | comptée (part rapportée, déclencheur 1), jamais remplacée | `exact_couvrable` (champ `selle_certifiee`) ; `test_couche_exacte_formules_et_certificats` |
| Fichier de sortie, de PID ou dossier de run existant | arrêt (R12) | `_exiger_absent`, `_ecrire_nouveau`, `creer_manifeste` ; `test_cli_refuse_d_ecraser`, `test_lancer_consigne_pids_sans_orphelin` |
| Programme linéaire non résolu ; primal ≠ dual ; matrice ou poids invalides | arrêt | `resoudre_jeu`, `exiger_poids` ; `test_jeu_sain_et_artefacts`, `test_jeu_solveur_artefacts` |
| Loi d'attaque non finie, coordonnée non libre modifiée, hors de la boule | arrêt | `exiger_admissible` ; `test_admissibilite_sain_et_artefacts` |
| Moniteur non fini, non calibrable, non calibré ; « ou » vide ou de variance nulle ; défense vide | arrêt | `Moniteur`, `MoniteurOu`, `Defense` ; `test_moniteur_gardes`, `test_ou_composite_sain_et_artefacts`, `test_defense_empilee_egale_boucle_et_gradient` |
| Maxout sans graine ; entraînement non fini | arrêt | `entrainer` ; `test_entrainement_gardes` |
| Aucun départ fini ; part de départs non finis > 5 % | arrêt | `meilleure_reponse`, `exiger_departs_finis` ; `test_meilleure_reponse_departs_non_finis`, `test_garde_departs_finis` |
| Fausses alertes d'une défense finale hors de α ± 0,005 | arrêt | `exiger_fpr` ; `test_garde_fausses_alertes_sain_et_artefact` |
| Part d'entraînements non convergés > S13 dans une tâche ; moniteur du tour 0 non reproductible | arrêt | `exiger_convergence`, `exiger_meme_moniteur` ; `test_garde_convergence_et_identite_tour0` |
| Temps processeur d'une tâche > 900 s | arrêt | `exiger_plafond` ; `test_plafond_de_temps_processeur` |
| Famille, bras ou témoin inconnu ; bras hors de son régime | arrêt | `Contexte`, `trajectoire`, `defense_temoin`, `construire` ; `test_bras_et_familles_inconnus` |
| Q3b : paramètres invalides ; optimiseur du déplacement sous la grille ; gain joint au-dessus d'une défense à un canal | arrêt | `exiger_parametres_prix`, `gain_maximal`, `gains_prix` ; `test_prix_gardes`, `test_prix_identites_et_bords` |
| Audit : bras ou tâche absents, V reconstruit ≠ V audité au bit près ; pilote audité étranger | arrêt | `auditer_tache`, `auditer`, `charger_pilote` ; `test_audit_sain_et_artefacts`, `test_charger_pilote_refuse_pilote_etranger` |
| Processus de travail consigné encore vivant ; signal TERM | arrêt (R10), pool terminé, survivants arrêtés par PID | `exiger_aucun_orphelin`, `arreter_par_pid`, `lever_sur_term` ; `test_arret_par_pid_sain_et_artefact`, `test_lancer_consigne_pids_sans_orphelin`, `test_signal_term_arrete_le_pool_par_pid` |
| Reproductibilité ; témoins aux nombres aléatoires communs ; formules exactes contre Monte-Carlo | constat d'essai | `test_reproductibilite_bit_a_bit_et_autre_racine`, `test_temoins_pur_et_union_nombres_aleatoires_communs`, `test_union_exacte_contre_monte_carlo`, `test_certificat_N2_par_recherche_sur_la_sphere`, `test_certificat_NV_moniteur_riche_d_une_vue`, `test_prix_formule_contre_monte_carlo`, `test_prix_taux_de_fausses_alertes_exact_du_partage` |
| Tâches ≠ 8N, configurations ≠ M ; invocations hors § Plan 1 ; paramètre changé après lecture | V0 fausse | contrôle du lecteur R13 |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| Lecture d'un résultat de décision avant scellement | arrêt et consignation (R1) | — |
| Marqueur de gel restant, ou contre-lecture sans ses deux empreintes | pas de scellement | validateur `problemes` ; `test_brouillon1_non_conforme_au_validateur_et_identite_du_code` |

## Rôles

- Auteur du brouillon 1, du code et des essais : sous-agent neuf Opus 5.5 (lignée conv-audit).
- Contre-lecteur (R2) : un sous-agent neuf **d'un modèle autre qu'Opus**, qui n'a écrit ni ce texte ni le code ; fichiers à lui donner explicitement : ce brouillon, `arene_extension_v1.py`, `essais/test_arene_extension_v1.py`, `gel-conception-arene-extension-v1.md`, `essai-pilote-arene-extension-v1.json`, `essai-pilote-prix-arene-extension-v1.json`, `audit-essai-arene-extension-v1.json`, `journal-arene-extension-v1.txt`, `LISEZMOI-arene-extension-v1.md`, et, pour le contexte, le brouillon 3 et la contre-lecture 3 de l'arène principale. Points à juger en priorité : le constat de fermeture par union et le choix des deux régimes (linéaire, « une vue ») ; les certificats (enveloppe convexe, loi marginale) et la selle à deux bornes de la couche exacte ; la définition de VT par le moniteur de poids maximal (et non le meilleur moniteur du réservoir) ; la Table E5 ; le déclencheur 2 (« trop beau » par |CAL| < 0,001) ; le modèle de Q3b (forme du dommage, canal « comportement », partage du taux) ; S5 et S11 (temps).
- Lecteur de porte (R13) : sous-agent neuf, ni auteur ni contre-lecteur ni analyste ; applique les tables ; verdict scellé puis soumis à Lazar.
- Lazar : gèle S1 à S16 ; donne le GO de la décision (processeur, aucune dépense), après le calcul décisif du pilote principal.

## Contre-lecture

- **Contre-lecture 1** — À REMPLIR : sous-agent neuf d'un modèle autre qu'Opus (identifiant), empreinte de ce brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
