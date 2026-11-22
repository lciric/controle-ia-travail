# Proposition A — Tour III.2 : critique croisée de méthode

**État des pièces**
- J'ai lu `texte-servi.md` en entier (801 lignes) avec le seul outil Read, sans recherche.
- Les pièces B, D, E et F sont présentes et closes par leur marqueur.
- La pièce C est absente (REFUS) : je n'en invente rien.
- Ma propre conception du tour III.1 n'est pas dans le fichier : je ne m'y réfère pas.
- Les empreintes sha256 sont annoncées mais je ne les ai pas recalculées : elles ne sont pas vérifiées.
- Tout ce qui suit a le statut **HYPOTHÈSE** : c'est une critique sur pièces, rien n'a été exécuté.
- Les seuils cités viennent des pièces, où ils sont déjà illustratifs. **Tout chiffre que j'ajoute, calculs compris, est illustratif.**
- B1 : je critique chaque pièce séparément. Un reproche qui se répète est redit, sans fusionner les plans.

## Sur la proposition B

**(a) Défauts de méthode**

1. **Appariement en G peut-être infaisable à opérateur égal.** α est borné à [0 ; 1]. Un sous-espace aléatoire de rang k retire une fraction de variance de l'ordre de k/d, et rien ne garantit qu'à α = 1 il atteigne le G de U. Il faudra alors changer le rang, dépasser α = 1 ou ajouter du bruit. Le témoin différera de U par le type d'opération, et Σ confondra direction et opérateur.
2. **G égal en moyenne, pas en loi.** Deux interventions de même KL moyenne peuvent avoir des lois de KL par jeton différentes, diffuse ou concentrée sur peu de jetons. Le profil S peut suivre cette forme plutôt qu'une fonction.
3. **Dose non fixée.** E1 ne dit pas à quel α ni à quel G Σ est calculé. Les données qui fixent les couches L et le rang k ne sont pas nommées non plus. S'ils sont réglés sur la batterie, S_U > 0 est en partie construit (Kriegeskorte et al. 2009, de mémoire). Le rejeu sur étiquettes permutées du §6 est le bon remède, mais il n'est pas dans le critère d'E1.
4. **T-sortie est presque nul par construction en format discriminatif.** Une température ne change pas l'ordre des vraisemblances d'options à un jeton, et peu celui d'options courtes. Ce témoin ne peut pas reproduire un profil dans ce format, donc « contre toutes les familles, dans les deux formats » est en partie acquis d'avance pour H_A.
5. **Asymétrie de multiplicité.** H_A doit battre cinq familles (conjonction), H_B se contente d'une équivalence avec au moins une (disjonction). Les taux de faux verdicts A et B ne sont donc pas symétriques, et ils ne sont pas corrigés.
6. **E3 oppose des hypothèses que les positions ne tiennent pas.** La position A des faits ne prédit aucune persistance, donc un rapport dans [0,67 ; 1,5] ne la falsifie pas. En forçage, T½ dépend de l'attention que les jetons ultérieurs portent à la fenêtre 256–511 : toute direction lue à distance persiste par construction.

**(b) Conditions de perte de puissance ou de non-jugeabilité**

- **Σ et le 99ᵉ centile.** U est un tirage unique comparé à la loi de S sur les sous-espaces témoins.
  - La puissance est bornée par (S_U − E[S_témoin]) / σ_sub, où σ_sub est l'écart-type entre sous-espaces. Elle ne croît ni avec le nombre d'items ni avec le nombre de tirages.
  - Le critère n'est pas jugeable si σ_sub est de l'ordre du seuil 0,15, ou si la loi est multimodale ou à queue lourde.
  - L'estimateur du 99ᵉ centile sur 200 tirages repose sur environ deux dépassements attendus.
- **Appariement.** Il n'est pas jugeable si P(G_témoin(α = 1) ≥ G_U) ≈ 0 sous la loi des sous-espaces. Il ne l'est pas non plus si les lois de KL par jeton diffèrent en quantiles au-delà d'une tolérance fixée, à moyennes égales.
- **d_t.** C'est un estimateur-rapport, dont la variance n'est pas bornée quand s_intact − s_plancher est petit devant son erreur type. Le plancher « déclaré » des tâches génératives est un paramètre arbitraire du dénominateur.
- **Marges intactes.** Si leurs lois diffèrent entre familles « perdues » et « gardées », S > 0 sous toute perturbation homogène. Σ ne le corrige que si la loi du bruit induit sur les marges est la même sous U et sous témoin.
- **Équivalence.** Elle n'est jugeable que si l'erreur type de Σ, variance entre sous-espaces comprise, est nettement inférieure à la marge 0,05. Avec trois familles de tâches par groupe, aucune loi « des fonctions » n'est estimée : l'inférence est conditionnelle aux six tâches.
- **r_K (E2).** Sur douze cellules et sous indépendance, l'écart-type du τ de Kendall est d'environ 0,22 : les seuils 0,8 et 0,4 sont à moins de deux écarts-types. De plus, α₅₀ est censuré dès que d_t n'atteint pas 0,5 pour α ≤ 1, ce que H_A prédit pour les tâches gardées, et les ex æquo dégénèrent la loi de r_K.
- **T½.** Il n'est pas jugeable si la décroissance de la KL n'est pas monotone, ou si elle suit une loi de puissance, car la demi-vie dépend alors du niveau initial. En génération libre, les lois des préfixes divergent et la KL jeton à jeton compare des conditionnements différents. Ce mode n'a d'ailleurs aucun critère.
- **Gain d'AUC.** L'erreur type d'une différence d'AUC entre prédicteurs corrélés doit être inférieure à la marge 0,02. Cela fixe un nombre minimal d'échecs, que la pièce ne donne pas.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Un témoin apparié par sélection, inscrit dans le critère : même procédure de découverte sur étiquettes permutées ou sur un contraste arbitraire, puis même appariement. Les sous-espaces aléatoires ne sont pas la bonne loi nulle pour un U structuré.
- Un témoin de portée : croisement distance × composition et troncature d'attention. Le croisement de formats ne l'apporte pas.
- La loi des verdicts témoin-contre-témoin sur toute la chaîne.
- Pour E3, un témoin apparié sur la masse d'attention reçue par la fenêtre.
- Le G atteint par T-hasard à α = 1, rapporté avant mesure.

## Sur la proposition C

Pièce absente (REFUS) : aucune critique possible, aucun contenu supposé.

## Sur la proposition D

**(a) Défauts de méthode**

1. **Verdict B vrai par construction à petite dose.** Le budget commun de perte n'est pas chiffré. S'il est faible, cible et témoins restent proches de l'intact, tous les |e_j| ≤ 2 points, et H_B gagne par insensibilité. S'il est fort, les planchers écrasent les écarts. Le verdict dépend donc d'un budget laissé libre.
2. **H_A mélange deux comparaisons.** « Gardée à ± 3 points de l'intact » et « perdue de plus de 5 points » comparent la cible à l'intact, pas au témoin. Seul S porte la comparaison au témoin.
3. **Unité non commensurable.** Le point de pourcentage ignore le niveau du hasard et le niveau intact. Cinq points perdus depuis 55 % ou depuis 95 % ne mesurent pas la même chose.
4. **Instrument confondu avec la fonction.** Traduction et résumé sont notés sur une grille binaire en aveugle, le reste automatiquement. De plus, le croisement longueur × fonction est annoncé « autant que possible », donc incomplet par aveu.
5. **Douze témoins moyennés.** e_j compare un tirage unique à la moyenne du panel, et la dispersion entre sous-espaces sort de l'estimateur. Si l'intensité requise pour la perte commune dépasse la projection complète, le témoin change d'opérateur : c'est le même reproche qu'à B.
6. **Pythia-1.4B.** De mémoire et à vérifier, c'est un modèle de base, non instruit. Si les fonctions « perdues » y sont proches du plancher à l'état intact, H_A est exclu avant mesure. La pièce ne pose aucune condition de validité sur le niveau intact.

**(b) Conditions de perte de puissance ou de non-jugeabilité**

- **e_j.** C'est une différence de proportions appariées, d'erreur type √(taux de paires discordantes / n).
  - Tenir un intervalle simultané dans ± 2 points avec 300 items demande une erreur type d'environ 0,7 point, soit moins de 1,5 % de paires discordantes.
  - Le verdict B n'est donc jugeable que si l'intervention ne change presque rien, ce que la pièce admet à demi (« renoncer au verdict B »).
- **Loi nulle des témoins.** Avec K = 12, la plus petite probabilité de rang attribuable à la cible est 1/13. Tout seuil plus sévère repose sur une forme de loi entre sous-espaces que la pièce ne déclare pas.
- **Budget.** La tolérance de 0,01 nat/jeton porte sur la moyenne. Le budget n'est pas jugeable si les lois des hausses de perte par jeton diffèrent en dispersion ou en queue.
- **« ± 3 points de l'intact ».** La variance p(1 − p) s'annule quand p intact tend vers 1 : l'équivalence passe alors sans information.
- **Rééchantillonnage par familles de textes.** Leur nombre n'est pas donné. Si la corrélation intra-famille est forte, l'effectif utile est ce nombre, pas 300.
- **Témoin-contre-témoin.** Une seule comparaison est un tirage de Bernoulli. Zéro alerte sur un essai laisse la borne haute du taux de fausses alertes près de 95 %.
- **Grille binaire.** Elle n'est pas jugeable sans estimateur d'accord entre juges, mesuré sur des sorties intactes dupliquées.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Une lésion sélective plantée par intervention, au même budget, détectée par la chaîne entière. Le rejeu de réponses substituées qualifie la lecture du profil, pas la sensibilité.
- Un témoin apparié par sélection : même découverte, étiquettes permutées.
- Un contrôle distance × composition, que le croisement longueur × fonction ne remplace pas.
- Une condition de validité sur le niveau intact de chaque fonction, et un second modèle.
- Des perturbations d'un autre type (bruit, quantification). Sinon « témoin » veut seulement dire « autre projection ».

## Sur la proposition E

**(a) Défauts de méthode**

1. **Statuts.** Plusieurs `[VÉRIFIÉ]` portent sur des énoncés que le fichier ne permet pas d'auditer et que E tire de sa mémoire : les formats « standards » des tâches, le corpus public d'OLMo, l'« attribution complète vérifiée ». Je ne modifie aucun statut. Je constate qu'ils ne sont pas vérifiables sur pièces et qu'ils ne doivent fonder aucun critère.
2. **Projection non centrée.** h′ = h − α·P·h retire aussi la composante moyenne le long de U_A. Cible et témoins peuvent alors différer par un décalage de biais hors distribution, pas seulement par l'information retirée. ΔAUDC > 0 peut en venir entièrement.
3. **C_orth « mis à l'échelle ».** L'échelle n'est pas définie. Au-delà de la projection complète, ce n'est plus une suppression.
4. **PCI_LM en partie vrai par construction.**
   - La complexité de Lempel-Ziv d'une matrice binarisée suit d'abord la proportion d'entrées au-dessus du seuil. Retirer U_A réduit l'amplitude propagée, donc cette proportion, donc l'indice.
   - Une forme sigmoïde est ce que donne un seuillage appliqué à une amplitude qui décroît régulièrement.
   - De mémoire et à vérifier, l'indice humain est normalisé par l'entropie de la source (Casali et al. 2013). Cette normalisation manque ici, ainsi que la loi de la direction d'impulsion.
5. **H_A surspécifié.** L'ordre « trois sauts avant deux, puis résumé et traduction » n'est pas dans les faits : A peut être falsifiée sur un ordre qu'elle n'a pas prédit. L'inversion de signe sous C_synt est une condition de validité d'un témoin, rangée dans le critère de A. Si C_synt est mal construit, A échoue sans raison.
6. **Protocole II.**
   - U_A vient d'un contraste entre tâches, donc E_UA porte l'identité et la difficulté de la tâche par construction.
   - L'appariement réussite/échec est un plan cas-témoins : l'AUROC n'y est pas celle de la population.
   - Le régresseur de référence a 54 prédicteurs (4 + 50 projections, d'après la pièce). Sans évaluation hors échantillon, il est surajusté et biaise vers H_B.
7. **H_KV.** Il est défini mais jamais opposé à un seuil : c'est un degré de liberté disponible après coup.
8. **Référence humaine.** Comparer surprise narrative longue et surprise lexicale locale récompense la myopie positionnelle que E nomme au point 6. C_fenêtre ressemblerait aussi au profil humain.
9. **Identification parmi 30 modèles.** Reconnaître U_A par n'importe quelle signature ne teste pas A : le décalage de moyenne du point 2 y suffit.

**(b) Conditions de perte de puissance ou de non-jugeabilité**

- **ΔAUDC.**
  - L'intégrale sur [0 ; ΔL_max] n'est pas jugeable si les supports en ΔL atteints par la cible et par les témoins se recouvrent peu.
  - Le maximum de deux moyennes estimées est biaisé vers le haut. L'estimateur penche donc vers B, d'un montant qui croît avec la variance des moyennes témoins.
  - Avec cinq paliers, l'erreur d'intégration n'est pas bornée.
- **Règle de décision.** Le seuil B est à 0,05, la marge d'équivalence à 0,08, la zone grise va de 0,05 à 0,20. Une valeur de 0,06 à intervalle étroit passe l'équivalence et tombe en zone grise : le verdict n'est pas une fonction de l'estimateur.
- **Intervalle à 99 %.** L'unité rééchantillonnée n'est pas dite. Si ce sont les 500 contextes, la variance entre les 50 sous-espaces et celle de l'extraction de U_A sont omises.
- **τ_K ≥ 0,75.** Sur quatre à six rangs, τ ne prend que quelques valeurs. Le seuil revient à tolérer zéro ou une paire discordante.
- **PCI_LM.** La loi de l'indice est conditionnelle au taux d'activation p après seuillage : il n'est pas jugeable tant que p diffère entre conditions. Sigmoïde contre droite sur cinq paliers, c'est quatre paramètres contre deux, avec un seul degré de liberté résiduel.
- **ΔAUROC.** Sur 1 000 paires, l'erreur type d'une différence d'AUROC est de l'ordre de 0,02, comparable à la marge 0,03. Le seuil absolu 0,72 dépend de la prévalence imposée par l'appariement.
- **Instrument I-E.** Un taux de détection de la « conscience résiduelle » n'est pas identifiable quand l'étiquette est un rapport différé soumis à l'amnésie. L'estimateur mesure l'accord avec le rapport.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Une ablation centrée contre non centrée, à perte égale.
- Un nul apparié par sélection. La « permutation des coordonnées de U_A » donne un sous-espace quelconque, pas un nul de la procédure.
- PCI_LM à taux d'activation égalisé, et sur un réseau à poids permutés. S'il rend la même sigmoïde, l'indice mesure le seuillage.
- Le protocole II hors échantillon, avec un critère chiffré de spécificité sur les tâches locales.
- La loi de ΔAUDC témoin-contre-témoin.

Je me sers du plan empan × profondeur et de C_fenêtre de E pour critiquer B et D : c'est le contrôle que ces pièces n'ont pas.

## Sur la proposition F

**(a) Défauts de méthode**

1. **V_cible est défini par le contraste qu'on lui demande ensuite de produire.**
   - L'extraction part d'une différence de moyennes entre B_int et B_loc, puis d'une « optimisation de masque parcimonieux » : l'objectif optimisé est la dissociation.
   - C1 à C3 ne reçoivent aucune optimisation. H_A1 compare un sous-espace optimisé à des sous-espaces non optimisés, et l'écart est en partie acquis d'avance (Kriegeskorte et al. 2009, de mémoire).
   - Les familles hors extraction atténuent la fuite, sans l'annuler si gabarits et consignes sont partagés.
2. **La porte de réplication sélectionne sur l'issue.** Deux méthodes × deux échelles font quatre essais, et on garde ce qui passe ΔS_int ≥ 0,30 et ΔS_loc ≤ 0,10. Conditionnellement au passage, D_spec > 0 sur test est en partie attendu. La probabilité de franchir la porte sans effet réel n'est pas estimée.
3. **Confusion avec l'identité de tâche.** Un contraste de moyennes entre types de prompts capte la consigne (« traduis », « classe »). L'ablation peut effacer la connaissance de la tâche demandée, non une capacité d'intégration.
4. **C4 est ambigu.** Si la procédure inverse produit un sous-espace anti-cible, F y lit une double dissociation favorable à A. La même issue montre que la procédure fabrique un profil pour n'importe quelle partition, ce qui est défavorable à A. Une issue à deux lectures opposées ne contrôle rien.
5. **Appariement des marges.** Apparier à ± 0,25 nat sélectionne des items intégratifs faciles et des items locaux difficiles, donc atypiques : c'est une sélection sur variable bruitée. De plus, la marge est un niveau et n'apparie pas la sensibilité de la marge à la perturbation.
6. **Verdicts mal rangés.**
   - L'équivalence avec C5 seul, ou une dissociation limitée au régime natif, sont comptées « raison à B ».
   - Or B prédit le même profil sous un témoin à dégradation globale égale. Un profil reproduit par une lésion structurée et non par C1–C3 falsifie cette prédiction : ce sont des issues « aucune ».
   - « H_B réfute A, a fortiori conceptuellement » excède ce qu'un modèle et un sous-espace permettent.
7. **Calibrage.** « Calibrés avant la mesure sur D_test » est ambigu : avant de mesurer, ou sur D_test. L'analyse « à ΔS moyen égal » apparie sur l'issue, ce qui est une fuite entre calibrage et évaluation.
8. **C2 par température.** Il est nul par construction en choix forcé à un jeton.
9. **Statut.** « VÉRIFIÉ en neurosciences cliniques » vient de la mémoire : ce n'est pas auditable sur pièces.

**(b) Conditions de perte de puissance ou de non-jugeabilité**

- **D_spec.**
  - L'erreur type par bloc vaut environ √(0,8·0,2/600)/0,55 ≈ 0,03. Pour une différence de différences, elle monte jusqu'à 0,06 sous indépendance, d'après les effectifs de la pièce.
  - La marge d'équivalence 0,05 n'est alors pas résoluble, sauf forte corrélation des paires. Le verdict B n'arrive que par la disjonction sur les témoins.
- **« Meilleur témoin » et « au moins un ».** La loi du maximum sur quatre familles n'est pas celle d'une famille : le rééchantillonnage doit inclure le choix du maximum. La disjonction gonfle le taux de faux verdicts B.
- **Intervalle.** Il est stratifié par tâche et item seulement. La variance due aux 20 tirages C1 et au rééchantillonnage de D_train, c'est-à-dire la stabilité de V_cible, est omise.
- **ED₅₀ et ρ.** Sous H_A, ΔS_loc ≤ 0,08, donc ED₅₀,loc est censurée à droite. ρ n'est pas défini dans le cas précis que H_A2 prédit.
- **τ sur cinq niveaux.** Il y a 120 ordres. Sous le hasard, P(τ ≥ 0,8) = 5/120 ≈ 0,042, et la plus petite probabilité atteignable est 1/120 ≈ 0,008. « p < 0,01 » exige donc τ = 1.
- **q(x).** La valeur nulle √(k/d) suppose des activations isotropes. Sous covariance anisotrope, l'espérance de q dépend du spectre. La nulle doit être la loi empirique de q sur des sous-espaces à variance égale.
- **Alerte sur B_loc.** V_cible est un contraste int − loc, donc la loi de q diffère entre B_loc et B_int par construction. Le taux d'alerte y est fixé par le signe du contraste, pas par H_A3 ou H_B3.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Un nul apparié par optimisation : même extraction et même porte sur étiquettes permutées et sur une partition arbitraire des six tâches. C'est l'absence qui pèse le plus sur ce plan. Je rapproche l'idée des tâches de contrôle de Hewitt & Liang (2019), de mémoire.
- Un contrôle d'identité de tâche : consigne et gabarit tenus constants entre B_int et B_loc à l'extraction.
- Un contrôle de pente : un bruit homogène sur les logits finaux doit donner D_spec = 0 sur les jeux appariés. Sinon, l'appariement des marges échoue.
- La loi de D_spec témoin-contre-témoin sur la chaîne entière.

Je me sers de C5 et du plan distance × intégration de F comme étalon de ce qui manque à B et à D.

## Antériorité

- **Lu dans cette session** : `texte-servi.md` seulement.
- **De mémoire, non relu** :
  - Kriegeskorte, Simmons, Bellgowan & Baker (2009), *Circular analysis in systems neuroscience: the dangers of double dipping*.
  - Casali et al. (2013), *A theoretically based index of consciousness independent of sensory processing and behavior*.
  - Hewitt & Liang (2019), *Designing and Interpreting Probes with Control Tasks*.
- **À vérifier** : la normalisation de l'indice humain par l'entropie de la source ; la nature de Pythia-1.4B.

## Ce qui peut être réfuté dans cette critique

Cinq énoncés, chacun testable avant toute mesure principale :
1. À α = 1, les sous-espaces aléatoires de rang k n'atteignent pas le G de la cible (B, D, E, F).
2. La procédure d'extraction, rejouée sur une partition arbitraire, rend un Σ ou un D_spec comparable (B, F).
3. PCI_LM à taux d'activation égalisé ne sépare plus U_A des témoins (E).
4. Le centrage de la projection réduit ΔAUDC (E).
5. À consigne constante, la dissociation de F diminue.

Si l'un d'eux est faux, le reproche correspondant tombe.

FIN-DE-CELLULE