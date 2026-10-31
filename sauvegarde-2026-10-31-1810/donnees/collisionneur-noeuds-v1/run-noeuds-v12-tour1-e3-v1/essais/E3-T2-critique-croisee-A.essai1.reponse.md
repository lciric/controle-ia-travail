# Proposition A — Tour III.2 : critique croisée de méthode

Pièces : la Pièce 20 (N9-1) est coupée au milieu d'une phrase (« dans toute la population restée non ») ; l'annexe `annexe-tour-2-recommandations-v5.md` n'est pas servie (attendu pour ce tour). Je n'en invente rien. Statuts : VÉRIFIÉ = lu dans une pièce servie ; les chiffres que je calcule à partir des pièces sont marqués « calcul, illustratif ».

## Sur la proposition B

### (a) Défauts de méthode

1. **N1 — le duel « T2 informative ou triviale » est vrai par construction.** B casse le générateur en déplaçant la fréquence du concept rare planté par statut (+2 / −2) et demande si T2 le détecte. T2 est, par définition (Pièce 2, option A, VÉRIFIÉ), la fréquence de cette étiquette-là : un décalage de 2 sur une grandeur d'erreur type 0,04 à 0,11 (Pièce 2, § 1.4) est détecté à coup sûr. Le duel ne porte donc pas sur ce que V5 gardait (CB-05 : la rareté de l'étiquette **retenue** ne doit pas séparer vrai de faux) ; il ne teste que la plomberie de S16d, ce que le diagnostic dit déjà (« presque acquis par construction »).
2. **N1 — fuite instrument / évaluation dans la « pièce qui trancherait ».** B propose de mesurer, sur des mondes d'essai, « la corrélation entre la rareté de l'étiquette retenue par statut et la précision différentielle de N ». Cela exécute le bras candidat N avant le scellement de la v3 ; la liste d'arrêt (Pièce 3, VÉRIFIÉ) range « exécution d'une méthode avant scellement » dans les arrêts, et § 9 réserve N à une seule invocation. Ce qui règlerait V5 serait alors informé par le comportement de N : l'instrument de validation serait calibré sur ce qu'il doit juger.
3. **N1 — seuil d'audit « 2,0 » choisi après lecture.** Les valeurs lues sont 2,87 et 1,94 (Pièce 1). Un seuil posé entre elles, après lecture, est exactement le « paramètre modifié après lecture » que B dit vouloir éviter.
4. **N1 — « V5 passe dans ≥ 285 mondes sur 300 » est une lecture fausse du critère.** V5 est un écart entre moyennes *sur l'ensemble des mondes* (Pièce 3, § 6, VÉRIFIÉ), non un booléen par monde ; la « fausse alerte ≤ 5 % » n'est pas définie.
5. **N3 — le duel confond diversité et valeur.** La métrique (rang du κ de la paire choisie parmi 45) ne mesure pas si le substitut sélectionne une paire *utile* ; un rang bas en κ est aussi la signature d'une paire sans lien. H_A (quartile inférieur) et H_B (quartile « supérieur ou médian ») ne sont ni exclusives sur la zone médiane-inférieure ni testables : une paire par lot, un lot au pré-pilote (10 fiches, Pièce 9). Le critère « identique sur ≥ 2 lots » n'a pas d'effectif. Lier D-j à N9 (« si HB échoue, le substitut n'a aucune base ») est un non sequitur : le substitut n'emploie ni leur modèle ni leur graphe (Pièce 20 SD-4, § 5).
6. **N4 — condition 3 contradictoire.** B retire les trois structures séquentielles du compte, constate que cela ramène le profil « à ≈ 2 paires de niches sur 15 » (chiffre non sourcé dans les pièces : HYPOTHÈSE), puis présente cette même opération comme pouvant « ouvrir de nouvelles paires ». La « mesure minimale » (score moyen du bras méta > tirage au hasard) est vraie par construction : l'argmax d'un score ≥ 0 bat la moyenne de ce score.
7. **N5 — métrique non estimable.** Un classifieur sur « les seuls comptes de sortie » exige plusieurs exécutions avec clés permutées pour avoir des exemples étiquetés ; B n'en prévoit qu'une. L'aire de 0,60 est posée sans loi de référence.
8. **N6 — DL-1 : H_B (« pas mieux que M5 ») n'est pas ce que la métrique teste** (coefficient absolu ≥ 0,70) ; il faut le contraste apparié iVAE − M5. **DL-3** : « perd plus de 0,10 » attribue à un défaut de signe ce que la pièce attribue aussi à la puissance (fond à 90 % des paires-années, Pièce 15, DL-3) : confondu. **DL-5** : « H_B falsifiée si ≤ 1 faux positif sur 50 » au seuil 0,01 : l'attendu sous H_A est 0,5, sous H_B (0,02) 1,0 ; 50 mondes ne les séparent pas (calcul, illustratif). **DL-12** : garder l'option 1 avec une « limite écrite » ne traite pas VS5-01 (Pièce 18, VÉRIFIÉ : la prémisse donnée pour M1 est inexacte).
9. **N10 — ratio hétérogène.** « Coût = dégradation de performance » et « gain = taux de jailbreak » n'ont pas d'unité commune ; « ratio > 1 » n'est pas un seuil. Le levier 3 (entraîner le modèle) est présenté comme levier alors que le PDF servi dit qu'OAT renchérit l'attaque sans la fermer (Pièce 24, p. 26, VÉRIFIÉ).
10. **N11 — juge de correspondance vrai par construction.** « Trouvé » si la paire *contient au moins une fiche* liée au pont. Avec 4 parents plantés parmi 10 fiches, une paire tirée au hasard en contient au moins un avec probabilité 1 − 15/45 ≈ 0,67 (calcul, illustratif) : l'oracle est presque toujours positif. **Transport** : un ρ de Spearman sur trois bras ne peut pas atteindre p < 0,05 (la plus petite valeur p à n = 3 est 1/6 unilatérale ; calcul, illustratif) : critère non jugeable par construction. **Puissance « par analogie avec J »** : J porte sur Δ(d1c, c) en points de précision à n = 2 400 (Pièce 3, S14) ; transposer sa puissance à une différence de précision entre bras sur E1′ ou sur la course est un transfert d'estimateur sans variance mesurée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- N1, audit sur l'ancienne grandeur : si l'écart maximal entre cinq moyennes de mélange (fréquence ≈ 2,9 avec probabilité 1 − r_s, ≈ 13 avec r_s, r_s dépendant du statut ; Pièce 2, cause 2) a une erreur type de différence σ_d ∈ [0,3 ; 0,6], l'espérance du maximum de 10 différences sous la loi nulle est de l'ordre de 1,5 σ_d (illustratif) : un seuil de 2,0 a une fausse alerte non négligeable et aucune puissance pour un vrai écart ≈ 1,4 (Pièce 2, option B).
- N3 : à 45 paires et une paire choisie par lot, la loi du rang sous H_B est uniforme ; la puissance d'un test de quartile à n = 1 est nulle.
- N4 : si la loi a priori des niches met une masse p_prof = Σ_{(i,j)∈profil} p_i p_j faible, P(zéro) ≈ exp(−C(n,2)·a²·s·p_prof) (a = accord par fiche, s = probabilité de structure ; approximation illustrative) ; le seuil 0,60 bascule avec p_prof, qui est SUPPOSÉ : le duel est jugeable seulement si p_prof est mesuré, non posé.
- N5 : l'aire du classifieur n'est estimable que si le nombre d'exécutions à clés permutées R satisfait R ≫ nombre de témoins ; à R = 1 elle est indéfinie.
- N6, DL-5 : la différence entre fausse détection 0,01 et 0,02 exige n ≫ 50 mondes ; à 50, l'intervalle couvre les deux.
- N10 : si la corrélation (couches, performance) n'est négative que sur une tâche et un modèle (Pièce 24, p. 23 : SQLEval, Llama-3-8B), le ratio n'est pas estimable hors de cette cellule.
- N11 : avec k parents plantés sur m fiches, la probabilité qu'une paire tirée contienne un parent vaut 1 − C(m−k,2)/C(m,2) ; dès que cette quantité dépasse 0,5, l'oracle de B perd toute discrimination entre bras.

### (c) Contrôles négatifs dont l'absence serait fatale

- N1 : générateur scellé avec **statuts permutés à monde fixe** (T2 doit passer, et l'ancienne grandeur ne doit pas séparer les statuts) ; B ne contrôle que le générateur « non cassé ».
- N3 : permutation des identifiants de concept dans les strates de degré (rang attendu uniforme) ; B propose un tirage au hasard, qui ne contrôle pas l'appariement.
- N5 : exécution à **clé permutée** avec sortie identique attendue ; absence fatale au duel.
- N11 : **cibles permutées** (un pont planté déclaré « trouvé » par une paire sans parent doit être compté comme fausse correspondance) ; B ne prévoit rien contre son propre oracle.

## Sur la proposition C

### (a) Défauts de méthode

1. **N1 — la « pièce sans dépense » exécute N avant scellement.** Mesurer « la corrélation entre le score de N (ou d1c) et l'indicateur étiquette retenue = jumeau » sur les mondes 990000–990199 exécute un bras candidat hors de l'invocation unique (§ 9 ; liste d'arrêt, Pièce 3, VÉRIFIÉ). d1c seul serait permis. C présente de plus la condition (1) (« démontré que V5 a une erreur type égale au seuil ») comme VÉRIFIÉ, alors que le diagnostic qualifie ses erreurs types de naïves et sur une seule graine de flux (Pièce 2, Réserves) : c'est OBSERVÉ-NON-AUDITÉ.
2. **N1 — le contraste « vrais conceptuels seulement » change l'estimand.** Compter les ponts « vrai d'opérateur » comme non-ponts modifie le dénominateur de la précision de tous les bras ; un bras qui promeut des jumeaux (d1 lit l'opérateur ; N_filtre lit la fréquence, Pièce 3) y perd mécaniquement. La chute de Δ(N, N_β0) sous ce masquage ne distingue pas « artefact d'opérateur » et « pont d'opérateur vrai promu à bon droit » : la garde proposée est confondue avec le changement d'estimand. Note : la sur-rareté du jumeau (fréquence 2, Pièce 2) touche les bras qui lisent les étiquettes d'opérateur ; d1c lit l'étiquette de **concept** la plus rare (Pièce 3, S14) et n'y est pas exposée : H_B doit nommer le bras.
3. **N3 — fuite instrument / évaluation.** C fait de l'essai de S31 à É0 sur `moisson-openalex-v1` à la fois l'ajustement des seuils (« à ajuster sur un essai de la moisson », question N3) et le test décisif (AUC apparié ≥ 0,55 → A19). Même source, même coupure : le seuil est calibré sur l'ensemble qui le juge. Il faut une coupure temporelle en deux (réglage sur 2023, test sur 2024–2025). De plus, H_B compare le substitut à l'attachement préférentiel alors que la règle du substitut (« degré/activité locale ») est de la même famille : la différence peut être nulle par construction, et la zone où l'intervalle enjambe 0,02 est sans verdict.
4. **N4 — réglage de la table de distance sur l'issue.** Passer e(n4,n5) et e(n5,n6) de 4 à 3 pour que n5 entre dans le profil est une modification d'un paramètre SUPPOSÉ dans le sens qui remplit le profil : l'instrument est ajusté sur la grandeur (P(zéro)) qui l'évalue. La correction CA1-09 (« argmax avant soustraction des paires prises ») rompt la règle « trois paires distinctes » (Pièce 9) et crée une collision de paires non prévue par le code. Le duel laisse une zone sans verdict entre P(zéro) = 0,25 et 0,50.
5. **N5 — contrôle mal nommé.** Le « contrôle négatif » (v54, exactitude = 1,00) est un contrôle **positif** ; le négatif (clé permutée, exactitude ≈ 0,5) manque. Lire « tous les attributs publics/privés de l'instance » teste un canal (mémoire du processus) que la v55 déclare supprimé (R-685, RAPPORTÉ) et non le canal réel (message de sortie, ordre des appels).
6. **N6 — le DL-12 « hybride » rouvre le chemin κ.** Centrer par année seule laisse les différences de niveau de sortie **entre environnements** ; si κ varie entre environnements, C et C⁰ restent associés à la sortie sans effet, ce qui est précisément le mécanisme de M § 26 (Pièce 15, DL-12, VÉRIFIÉ). L'autre voie (« M1 testant pentes et variances ») redéfinit la méthode après lecture : HR-M1 (Pièce 16) ne porte plus sur la prédiction invariante telle que référencée, et l'épreuve ne compare plus l'instrument publié.
7. **N9 — masquer janvier–avril 2023 par date d'article ne ferme pas la fuite par la liste de concepts** : les 37 960 concepts sont extraits des résumés jusqu'à la coupure (Pièce 20 SD-4) ; un concept né début 2023 porterait l'information dans les traits « de fin 2022 ». La garde doit porter sur la date de première apparition de chaque concept dans `full_dynamic_graph`.
8. **N10 — L2 est attaquable et confond difficulté et évasion.** Un moniteur couplé « sonde × cohérence des logits » est lui-même une défense figée contre laquelle l'attaquant optimise (protocole de Bailey) ; TEFV mesure alors un attaquant qui n'a pas ciblé L2. Le FPR à 1 % sur jeu honnête est confondu avec la difficulté des tâches : les entrées honnêtes difficiles ont une entropie élevée et déclenchent L2. Le jeu honnête doit être apparié en difficulté.
9. **N11 — les parents plantés récompensent le bras basique par construction.** Les deux parents d'un pont réel partagent un concept (c'est ce qui fait le pont) ; la règle « proche en concept, loin en domaine » les détecte par définition, les deux autres bras non : l'oracle n'est pas neutre entre bras. La substitution de 4 fiches de Kimi par 4 parents sur 10 réduit le vivier réel de 40 % (calcul, illustratif) et change la course que le pré-pilote devait éprouver. Les conditions de transport (fuite F ≤ 0,60 « sur les vraies fiches ») exigent κ_lat, inobservable sur fiches réelles : non jugeable. Le tau de Kendall sur trois bras partage le défaut de B.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- N1, contraste masqué : si la part π_op des vrais ponts d'opérateur dans les vrais promus par N est élevée, Δ_conc est tiré vers δ_non quel que soit le mécanisme ; le test ne sépare H_A de H_B que si π_op est faible et rapporté.
- N3 : AUC_S31 − AUC_degré a une variance qui croît avec la corrélation entre les deux scores ; si ρ(S31, degré) → 1, la différence est nulle par construction et son intervalle couvre 0,02 pour tout n.
- N4 : P(zéro) sous la grille corrigée dépend de la masse p_prof ; si la correction de E ajoute des paires où p_i p_j est petit (n5 à 0,15 et n6 à 0,05), le gain est borné par 2·p_5(p_4+p_6)·s·a² (illustratif) : la correction peut ne rien changer.
- N5 : l'exactitude d'un classifieur à 100 exécutions a un écart type ≈ 0,05 (illustratif) ; le seuil 0,52 est sous le bruit.
- N6 : sous centrage par année seule, l'erreur C sous β = 0 croît avec la variance inter-environnements du niveau de sortie (M § 26 : 0,113 à 10 % de variance de strate) : la taille nominale est perdue dès que cette variance est non nulle.
- N10 : TEFV est non jugeable si la validité de tâche et le KL sont mesurés par un oracle que l'attaquant inclut dans sa perte ; la loi de TEFV sous attaque adaptative sur L2 n'est pas celle sous attaque sur L1 seul.
- N11 : Recall@3 contre p₀ = 3/45 perd sa puissance si le bras basique atteint un rappel proche de 1 par construction (plafond) : la comparaison devient un test contre un plafond, non contre le hasard.

### (c) Contrôles négatifs dont l'absence serait fatale

- N3 : **coupure temporelle séparant réglage et test** ; sans elle, l'AUC d'essai est inopposable.
- N4 : **rejeu de P(zéro) avec la table E originale** à côté de la table corrigée, pour chiffrer ce que la correction seule apporte.
- N5 : exécution à **clé permutée** (exactitude attendue 0,5).
- N6 : mondes β = 0 **par environnement** sous le centrage retenu (C y est incluse).
- N10 : **entrées honnêtes difficiles appariées** (FPR de L2 à difficulté fixée) et attaque adaptative ciblant L2.
- N11 : **parents chimères** partageant un concept de surface (C les prévoit) **et** parents vrais sans concept commun observable (pour mesurer la dépendance de l'oracle au bras basique) ; le second manque.

## Sur la proposition D

### (a) Défauts de méthode

1. **N1 — H_A n'est testable qu'après le run de décision.** D décide de T2 par « déplacement d'un contraste décisif supérieur à sa demi-largeur » (critère (iii) de l'audit, Pièce 3, VÉRIFIÉ). Ce critère suppose les bras exécutés ; comme critère de **validation du générateur** il est circulaire : il faut lancer l'invocation unique pour savoir si la validation tenait. D ne dit pas ce que fait la porte V0 avant ce test.
2. **N3 — population non spécifiée.** « Détection de ponts plantés vrais » pour le substitut : aucun monde synthétique servi ne modélise les traits de Gu-Krenn, et la moisson n'a pas de ponts plantés. Sans population, détection et fausses promotions ne sont pas des estimateurs.
3. **N4 — balayage des lois sans gel.** Un P(zéro) « sur un balayage des lois et accords » produit un intervalle de verdicts ; la décision n'est jugeable que si une loi est gelée ou mesurée (sur jeu d'essai, non sur fiches réelles) : D laisse ce choix ouvert.
4. **N5 — la métrique de D ne peut pas s'appliquer à É5.** « Décisions rejouées sur consommations seules strictement identiques » : les décisions d'É5 (A6, A7, S20) dépendent par construction des classes (Pièce 12, § C, VÉRIFIÉ) ; elles ne sont pas rejouables sur consommations seules. Le critère est non jugeable exactement là où A21 pose problème. L'option (b) déplace le canal vers le message inter-sessions sans artefact sur son contenu (granularité des comptes).
5. **N6 — « M1 encore informative » sans estimateur.** D ne nomme ni le taux d'ensembles acceptés non vides, ni l'inclusion de C, ni l'abstention sous H. « Fausses récupérations en Bθc » : sous (iv) violé, une récupération de z₁ reste possible par hasard ou par un sous-cas identifiable ; la compter comme fausse suppose le théorème nécessaire, ce qu'il n'est pas (Pièce 16 : « en Bθc, pas mieux que M5 » est la rivale, non « ne retrouve pas »).
6. **N9 — changement de seuil non déclaré.** D rend B-i « non décisive » alors que le préenregistrement v2 servi la compte dans la conjonction « B réussi » (Pièce 20 N9-1, Seuil, VÉRIFIÉ). Le point de fond est juste (B-i mesure surtout degré et âge), mais c'est une modification d'un test décisif, donc un nœud, à écrire comme tel.
7. **N10 — asymétrie de falsification.** « Borne basse du coût d'attaque supérieure au budget » n'est pas estimable : un optimiseur local donne une **borne haute** du coût minimal (Pièce 22 : (iii) est une borne haute de la valeur du jeu, VÉRIFIÉ). Une attaque qui échoue ne falsifie H_B que pour la classe d'attaquants employée ; D ne fixe pas cette classe.
8. **N11 — critère (iii) « absence de contribution vraie unique » perd sa puissance.** Sous échangeabilité des bras avec détection p et k cibles, un bras faible obtient au moins un « unique » avec probabilité non négligeable (par exemple k = 12, p = 0,2 : ≈ 1 − (1 − 0,2·0,64)^12 ≈ 0,8 ; calcul, illustratif) : le critère retient presque tout bras. Il faut l'espérance d'uniques sous permutation des noms de bras. La marge d'équivalence « plus petit effet qui changerait la décision » est circulaire (la décision dépend du transport qu'elle sert à établir). La correspondance par deux lecteurs LLM réintroduit un verdict de modèle dans la composition ; N-058 l'admet pour l'identité d'une cible, non pour sa qualité, mais les erreurs de lecteur sont un confondant que seules les cibles permutées (prévues) et des lecteurs étalonnés sur témoins mesurent.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- N1 : le critère (iii) exige, pour un contraste de σ ∈ [11 ; 15,3] (Pièce 3, S15), un déplacement > demi-largeur à 95 % ; sur 300 graines de validation la demi-largeur est ≈ 1,3 à 1,7 point (calcul, illustratif) : un artefact de rareté plus petit est invisible.
- N4 : si le balayage des lois donne P(zéro) de part et d'autre de 0,5, aucune décision ; jugeable seulement sous loi gelée.
- N5 : rejeu identique n'est défini que pour les décisions fonction des seules consommations ; pour É5 la fonction n'existe pas.
- N6 : la comparaison centrage / κ = 1 à graines appariées perd sa puissance si la variance inter-graines du résidu de T1 domine la différence entre transformations ; D ne borne pas cette variance.
- N9 : l'aire appariée B-ii a une erreur type qui croît quand les cases degré × âge sont peu peuplées pour les positives ; à k = 5 témoins et cases vides, l'estimateur est indéfini.
- N10 : si l'optimiseur n'atteint pas le minimum (borne haute lâche), le coût mesuré est biaisé vers le haut et H_A est faussement « non falsifiée ».
- N11 : la formule n ≥ ((z + z)σ_D/δ)² est non calculable sans σ_D ; D n'extrait pas des pièces les variances disponibles (σ 11 à 15,3 par monde en synthétique, Pièce 3 ; variance binomiale pour les ponts).

### (c) Contrôles négatifs dont l'absence serait fatale

- N1 : M_inertes et statuts permutés : D les a.
- N3 : population explicite avec **permutation intra-strate** : absente tant que la population n'est pas nommée.
- N5 : artefact sur le **contenu du message** de la boîte externe (comptes trop fins) : absent.
- N10 : **attaquant dont la classe est fixée et dépassée** (budget supérieur) pour borner la lâcheté de la borne haute : absent.
- N11 : **permutation des noms de bras** pour le compte d'uniques (D la prévoit pour le transport, non pour la règle de retrait).

## Ce que je reprends, en le disant

Je reprends de D la correspondance en quatre classes (exacte / proche / surface / aucune) avec cibles permutées, et de C la coupure réglage / test pour S31 — à condition que la coupure soit temporelle. Je ne reprends d'aucune proposition un oracle de ponts plantés qui compte une paire « contenant un parent », ni un test de transport sur trois points.

FIN-DE-CELLULE