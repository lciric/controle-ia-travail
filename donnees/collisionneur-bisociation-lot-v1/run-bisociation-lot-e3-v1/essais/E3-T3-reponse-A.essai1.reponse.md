# Proposition A — Tour III.3 : réponse aux critiques croisées

**Pièces.** Les trois critiques (B, C, D) sont présentes et intègres. Une erreur d'attribution dans B : elle cite « la dernière ligne de E2 » (« cela ne valide pas encore une fertilité bibliographique ») ; cette phrase ne figure pas dans ma conception E3-T1-A. Je réponds au fond de la critique, pas à la citation. Toutes les critiques sont RAPPORTÉ ; leurs calculs de puissance sont HYPOTHÈSE à chiffres illustratifs, comme les miens. Je ne réponds qu'aux sections visant A ; j'emprunte en le disant deux critiques adressées à D (C-a1 sur le budget de la sur-additivité ; D-c2 sur les unions appariées), parce que mon E2 utilise la même formule.

## (a) Verdict sur chaque critique

Légende : **A** = acceptée ; **R** = rejetée (raison donnée) ; **T** = transformée en test ou en contrôle.

### E1 — distance scalaire contre trou à structure commune

| Critique | Verdict | Raison ou suite |
|---|---|---|
| D-a1 : H_A et H_B ne sont pas exclusives, le profil contient la distance comme coordonnée | **A** | Violation de B4 de ma part. H_A/H_B réécrites comme un test d'information conditionnelle (voir E1′). |
| D-a2, D-c1 : étiquette de pont circulaire si le pont est reconnu par citations croisées alors que le score mesure un déficit de citations ; la permutation des dates ne le détecte pas | **A** | Mon lecteur aveugle aurait reconnu les ponts, de fait, par leur trace citationnelle. Nouvelle étiquette : reprise par une **tierce** niche d'un objet transféré (idée de relecture 5, point 5, RAPPORTÉ), indépendante du canal mesuré. |
| B-a1, C-a3 : même pool de ponts pour calibrer la partition, départager E1 et évaluer E6 ; la partition multicouche absorbe déjà la structure commune | **A** | Trois jeux disjoints **par niche et par période** (réglage de la partition ; choix des traits et des poids ; évaluation). La partition est calculée sur les couches sociale et lexicale seulement ; la couche « équations » n'entre que dans le score, jamais dans la partition. |
| B-a2, B-c1 : la permutation des dates teste la fuite, pas la circularité ; retirer les articles des ponts du graphe | **A** | Contrôle ajouté : graphe amputé des articles-ponts, partition et score recalculés ; chute du classement > seuil préenregistré → le score lisait la trace du pont. |
| B-b : avec 30 ponts, précision@k à 5 points n'a aucune puissance (k ≥ 400 illustratif) | **A** | Mon ancrage (30 ponts, 90 témoins) était un pilote de faisabilité, pas un test. Puissance calculée avant lecture sur pilote ; si la puissance pour l'écart préenregistré est < 0,8 (illustratif), E1′ est déclarée non jugeable **avant** exécution et le goulot humain est budgété. |
| C-b1 : censure asymétrique η_B > η_A (les paires distantes sont reprises plus tard, Wang-Veugelers-Stephan 2017 RAPPORTÉ) peut inverser le signe de l'écart | **T** | Vrai et grave. Test de stabilité ajouté : l'écart H_A/H_B est calculé à trois horizons (3, 5, 10 ans, illustratif) sur des coupures assez anciennes pour que l'horizon long existe ; si le signe change avec l'horizon, E1′ est non jugeable et on ne retient que l'horizon long. |
| D-b : corrélation intra-niche Y_ij, Y_ik ; bootstrap par paires sous-estime la variance | **A** | Bootstrap par grappes (niche), pas par paire. |

### E2 — cloche lisse contre seuil critique (mondes inventés)

| Critique | Verdict | Raison ou suite |
|---|---|---|
| B-a3 : E2 ne teste pas la fertilité bibliographique | **A** (citation erronée, fond juste) | E2′ est reclassée : **étalonnage des tests de criticité**, pas test de l'objet réel. Sur la littérature réelle, aucun paramètre de taille thermodynamique n'est identifiable (point que D fait à B, que je reprends) ; le préenregistrement sur littérature réelle ne contiendra que « changement de pente avec intervalle ». |
| D-a3, D-b : pic de variance mécanique (Bernoulli p(1−p) ; Poisson-gamma μ+φμ²) ; exposants ajustés sur les mêmes courbes que le test d'effondrement | **A** en partie | Ma fertilité est un compte exact, pas un binaire : la borne Bernoulli ne s'applique pas, la dépendance moyenne-variance si. Correction : la signature de susceptibilité n'est retenue que si la variance dépasse celle du nul (urne de Tria et al. 2014, RAPPORTÉ) **à moyenne égale**. Exposants ajustés sur quatre tailles, effondrement testé sur une cinquième tenue à l'écart (D-c2). |
| B-b, C-b3 : 4 tailles × 12 points, matrice d'information quasi singulière ; une sigmoïde à largeur en (ln L)⁻¹ produit ΔBIC < 10 | **T** | Protocole en deux passes préenregistré : passe 1 grille large ; passe 2 grille resserrée autour du seuil estimé, cinq tailles au facteur 4 (illustratif). Le nul « sigmoïde à largeur logarithmique » est ajouté à la comparaison de modèles : s'il n'est pas distinguable du modèle critique sur les mondes **plantés critiques**, le test est déclaré impuissant et le mot « transition » sort du programme. |
| C-c3 : contrôle de valeurs extrêmes (meilleur de K(L) tirages à queue sous-exponentielle produit un raidissement apparent) | **A** | Deuxième nul ajouté. |
| D-c2 (et C-a1 adressée à D, empruntée) : unions de prémisses sans rapport appariées en nombre et complexité ; F > 0 par combinatoire ; budget mal défini | **A** | Le calcul exact des vérités atteignables en k pas supprime la question du budget de recherche, pas celle de la combinatoire : M(A∪B) > M(A)+M(B)−M(A∩B) donne F > 0 sans synergie. Contrôle : unions aléatoires appariées ; la fertilité rapportée devient F − F_aléatoire-appariée. Monde planté à fertilité strictement nulle ajouté. |
| D-a3 : changer la taille change le dénominateur des découvertes possibles | **A** | Paramètre d'ordre normalisé par le nombre de vérités atteignables à chaque taille. |

### E3 — essaim : émergence contre échantillonnage

| Critique | Verdict | Raison ou suite |
|---|---|---|
| D-a4 : à budget fixe, N, profondeur par agent et coût des messages sont confondus | **A** | Comptabilité séparée : tokens de raisonnement, tokens de messages, tokens de consolidation. Le témoin « agent unique » reçoit le budget de raisonnement de l'essaim, pas le budget total. |
| B-c2 : meilleur-de-N à contexte enrichi (résumé d'un run précédent sans communication en temps réel) | **A** | Témoin ajouté : il sépare « élargissement du prompt » de « communication ». |
| D-c3 : messages de même paire, même longueur, provenance ou ordre détruits ; témoin sans communication recevant le même volume de texte | **A** | Remplace mon « routage aléatoire entre groupes », qui testait la pertinence thématique, pas la structure. |
| C-b2 : inverse de Simpson borné par N quand M ≫ N ; corrélation intra-groupe ρ réduit N_eff ; D-b : N_eff < N | **A** | Diversité mesurée par nombre de grappes distinctes avec courbe de raréfaction et estimateur de couverture (famille Chao, nom RAPPORTÉ de mémoire : référence à vérifier) ; ρ intra-groupe estimé sur un run sans messages et N_eff rapporté. |
| B-b : ~10 survivantes par cellule, aucune puissance pour 20 % | **A** | Règle d'arrêt : si le pilote donne < 50 survivantes par cellule (illustratif), on réduit le plan (2 valeurs de N × 2 couplages) et on augmente les réplications ; sinon non jugeable. |

### E4 — biais du juge figé

| Critique | Verdict | Raison ou suite |
|---|---|---|
| C-a1 : la réécriture par un modèle entraîné après le réveil injecte la sémantique post-réveil ; le juge note sa mémoire ou le style du réécriveur | **A** | C'est la faille la plus grave de ma conception. E4′ déplace le test principal sur **mondes inventés** où distance de la paire et qualité sont plantées indépendamment : aucune mémoire possible, aucune qualité latente Q (D-b). Les belles au bois dormant ne servent plus que de vérification externe secondaire. |
| C-a1 : « vrai par construction » si le juge utilise la perplexité lexicale croisée et qu'on unifie le vocabulaire | **R** en partie | Si la pente disparaît sous vocabulaire unifié, ce n'est pas une tautologie : c'est le constat que le juge pénalise le jargon et non le contenu — la mesure du trou culturel de Vilhena et al. 2014 (RAPPORTÉ) devient alors un prédicteur de la note, ce qui est précisément ce qu'il faut savoir. Accepté en revanche : ce contrôle ne sépare pas « distance conceptuelle » de « divergence lexicale » ; E4′ les sépare par plantation. |
| B-a4, D-a5, D-c4 : la réécriture modifie ensemble distance, clarté, plausibilité ; contrefactuels où seule la forme change | **A** | Sur les cas réels résiduels : contrefactuel de réécriture (forme seule) et jugement de deux réécritures indépendantes ; un écart de note entre réécritures de la même idée mesure l'effet du réécriveur. |
| C-c1 : contrôle de mémorisation par articles postérieurs à la coupure d'entraînement du juge | **A** | Ajouté pour la branche réelle. |
| B-c3, D-c4 : idées distantes documentées stériles sur horizon complet ; censure à droite des « non reprises » | **A** | Témoins : idées à bisociation revendiquée, publiées il y a ≥ 15 ans (illustratif), jamais reprises ; horizon complet déclaré. |

### E5 — dose de contact

| Critique | Verdict | Raison ou suite |
|---|---|---|
| C-a2, B-a5, D-a5 : le placebo « niche sans structure commune » confond contact et distraction contextuelle ; le juge peut récompenser la longueur ; la dose varie longueur, diversité, pertinence, position | **A** | Quatre bras : dose B (niche à structure commune) ; dose A (titres redondants de la même niche, C-c2) ; placebo apparié en longueur, format et pertinence de surface (D-c5) ; dose nulle. Le traitement est déclaré multi-versions ; la courbe est estimée **par version**, pas en une seule dimension. |
| D-b : interférence entre paires ; D-a5 : signe avec expérience naturelle pas le même estimande ; τ_courses ≠ τ_science ne renseigne pas | **A** | Courses sans état partagé entre paires (interférence nulle par construction, à vérifier par journal). La confrontation du signe avec Boudreau et al. 2017 ou Catalini 2018 (RAPPORTÉ) est rétrogradée : condition nécessaire de transport, jamais preuve ; aucune comparaison d'ordre de grandeur (unités incommensurables). |
| D-c5 : résultat antérieur au traitement ; intervention préenregistrée sans effet | **A** | Ajoutés. |
| B-b : 8 doses, courses par dose non spécifiées | **A** | Calcul de puissance sur pilote ; distinction seuil/sigmoïde abandonnée comme objectif de E5′ (non identifiable avec 8 points), seule la monotonie et l'effet global sont testés. |

### E6 — Gu-Krenn à longue portée

| Critique | Verdict | Raison ou suite |
|---|---|---|
| C-a4 : à d > 3, voisins communs sont nuls par construction (d > 2) ; attachement préférentiel « dégénéré » ; restriction d'étendue | **A** pour les voisins communs, **R** pour l'attachement préférentiel | Le produit des degrés reste défini et variable sur la strate ; il n'est pas dégénéré, il est la ligne de base pertinente. Correction : lignes de base adaptées à la longue portée (produit des degrés ; comptes de chemins de longueur 3-4 tronqués ; hasard) ; comparaison **intra-strate** seulement (D-b : AUPRC non comparable entre strates). |
| B-c4 : composition de la strate > 3 différente (paires rares, petites niches) | **T** | Distribution des degrés et des âges rapportée par strate ; appariement sur le degré à l'intérieur de la strate ; si la strate > 3 ne contient que des nœuds de degré < seuil (illustratif), E6′ répond à une autre question et le dit. |
| D-b : gain conditionnel nul si β = 0 une fois popularité, âge, croissance contrôlés | **A** | Critère unique : gain conditionnel de Gu-Krenn au-dessus du modèle « popularité seule » dans la régression logistique intra-strate. |
| D-c1 : fuite par concepts assignés après coup | **A** | Vocabulaire figé avant coupure ; contrôle « étiquettes remplacées par chaînes aléatoires, topologie conservée » emprunté à la critique C adressée à B. |

**Critique non retenue.** B-b suppose pour E1 un taux de base p₀ ≈ 0,5 de précision@k ; cela vaut si k couvre tout le pool, pas pour k petit ; mais sa conclusion (puissance insuffisante avec 30 ponts) tient de toute façon. Je ne conteste donc que le modèle, pas le verdict.

## (b) Expériences corrigées

Convention inchangée : seuils illustratifs ; chaque duel a un contrôle dont l'échec invalide l'expérience, non une hypothèse ; trois jeux disjoints par niche et par période partout.

**E1′ — Information conditionnelle de la structure commune.**
Modèle : logit P(reprise par tierce niche | paire) = α + β₁·canal + β₂·structure + γᵀ·X, X = popularité, âge, croissance ; réglage sur le jeu 2, estimation sur le jeu 3.
H_A : β₂ = 0 (la structure commune n'ajoute rien au canal et à la popularité ; la règle « loin en domaine » suffit). H_B : β₂ > 0 avec intervalle à 90 % excluant zéro (illustratif), bootstrap par niches. Exclusives : l'une nie ce que l'autre affirme sur le même paramètre.
Étiquette : réutilisation, hors des deux niches, d'un objet (équation, méthode, jeu de données) apparu dans le pont, à horizon ≥ 5 ans (illustratif), constituée par automatisation puis audit humain aveugle d'un échantillon ; aucune citation croisée entre les deux niches n'entre dans l'étiquette.
Contrôles : (i) graphe amputé des articles-ponts, partition et scores recalculés : si β₂ s'effondre, le score lisait la trace du pont, expérience nulle ; (ii) permutation des dates (fuite) ; (iii) stabilité du signe de β₂ à trois horizons : changement de signe → non jugeable (censure asymétrique). Puissance : calculée avant lecture ; seuil de faisabilité : nombre de ponts post-1991 tel que la puissance pour l'écart préenregistré atteigne 0,8 (illustratif) ; sinon l'expérience n'est pas lancée et c'est la constitution de la base qui devient la tâche.
Issues : H_B meurt → la règle actuelle n'est pas remplacée ; H_A meurt → le profil remplace la règle, avec poids préenregistrés ; γ seul significatif → les deux meurent, la popularité explique tout.

**E2′ — Étalonnage des tests de criticité (mondes inventés).**
H_A : les tests de criticité (effondrement sur taille tenue à l'écart ; susceptibilité au-dessus du nul à moyenne égale ; comparaison de modèles incluant la sigmoïde à largeur logarithmique et le maximum d'échantillon à queue sous-exponentielle) séparent mondes plantés critiques et mondes plantés lisses avec taux de détection ≥ 0,9 et fausses alertes ≤ 0,1 (illustratif). H_B : ils ne les séparent pas.
Dispositif : trois familles de mondes plantés (critique ; cloche lisse ; nul strict), cinq tailles au facteur 4, grille en deux passes ; fertilité = sur-additivité normalisée par le nombre de vérités atteignables, moins la sur-additivité d'unions aléatoires appariées en nombre de prémisses et complexité.
Issues : H_B → le mot « transition de phase » sort définitivement du préenregistrement, remplacé par « changement de pente » ; H_A → les tests sont autorisés, mais uniquement sur mondes inventés et sur les courses (où la taille est manipulable), jamais sur la littérature réelle où la taille n'est pas un paramètre identifiable.

**E3′ — Communication contre élargissement du contexte.**
H_A : à budget de raisonnement égal, l'essaim communicant produit plus d'idées survivantes par million de tokens que le meilleur des témoins (meilleur-de-N ; meilleur-de-N à contexte enrichi ; même volume de texte reçu sans communication ; messages de même paire à provenance et ordre brouillés), d'au moins 20 % (illustratif), et l'avantage disparaît sous ablation des messages. H_B : aucun témoin n'est battu de cette marge.
Comptabilité des tokens par poste ; diversité par grappes distinctes avec raréfaction et estimateur de couverture ; N_eff estimé sur un run sans messages ; règle d'arrêt sur le pilote (< 50 survivantes par cellule → plan réduit ou non jugeable).
Issues : H_A meurt si le contexte enrichi ou le brouillage font aussi bien (l'essaim est un prompt long) ; H_B meurt si seul l'essaim à messages ordonnés et pertinents franchit la marge ; chute de diversité après partage supérieure au gain → H_A meurt par convergence.

**E4′ — Le juge note-t-il la distance, à qualité plantée ?**
Dispositif principal : mondes inventés où chaque idée a une distance de paire D et une qualité Q (vérité et portée) plantées indépendamment, formulée dans le vocabulaire des deux niches inventées ; juge aveugle.
H_A : dans logit P(note haute | D, Q) = α + βD + γQ, β < 0 avec intervalle excluant zéro. H_B : β = 0.
Contrôles : vocabulaire unifié (si β disparaît, le juge note le jargon) ; contrefactuel de forme (deux formulations de la même idée) ; mondes où D et Q sont corrélés par construction pour vérifier que l'estimateur retrouve le β planté.
Branche externe secondaire : belles au bois dormant et idées distantes stériles à horizon complet (≥ 15 ans), réécrites par un pipeline testé d'abord sur des articles postérieurs à la coupure d'entraînement du juge (contrôle de mémorisation).
Issues : H_A → le juge ne sert pas d'étiquette de fertilité ; on passe à l'étiquette à retardement et au jury stratifié ; H_B → le juge est un proxy précoce utilisable, sous réserve de la branche externe.

**E5′ — Dose de contact, quatre bras.**
Estimande : unité = paire ; traitement = version × dose (B à structure commune ; A redondante ; placebo apparié ; nulle) ; issue = survie à la génération suivante, juge distinct ; interférence nulle par courses sans état partagé.
H_A : l'effet de la dose B dépasse celui de la dose A et du placebo d'au moins 8 points (illustratif). H_B : les trois versions ont le même effet (c'est le volume, pas le contact).
Contrôles : résultat antérieur au traitement (doit être nul) ; intervention préenregistrée sans effet ; placebo apparié en longueur et format.
Issues : H_A meurt si A ou placebo égalent B ; H_B meurt si B seule agit. Transport : signe comparé à une expérience naturelle indépendante, condition nécessaire seulement ; aucune magnitude.

**E6′ — Gain conditionnel de Gu-Krenn à longue portée.**
Reproduction sur données publiques avec coupure respectée et vocabulaire figé avant coupure (contrôle : étiquettes aléatoires à topologie conservée). Strates par distance de plus court chemin ; comparaison intra-strate ; appariement sur le degré.
H_A : sur la strate > 3, le score Gu-Krenn conserve un gain conditionnel positif au-dessus du modèle popularité seule et des comptes de chemins tronqués. H_B : gain nul.
Issues : H_B → Gu-Krenn n'est qu'une ligne de base pour le bisociateur ; H_A → filtre de premier niveau réutilisable, étiquette (impact à trois ans) explicitement distincte de la reprise traversante. Si la reproduction échoue (écart avec le chiffre RAPPORTÉ > seuil), tout s'arrête et l'échec est consigné.

Instruments (tableau de T1) : inchangés sauf trois lignes — « Juges figés » évalués d'abord sur qualité plantée (E4′) ; « Essaim » avec les quatre témoins de E3′ ; « Bisociateur » avec l'étiquette de reprise par tierce niche.

## (c) Réponse à l'arbitre

**Ce qui est établi (au statut indiqué).** Les antériorités occupent la zone : Swanson 1986, Burt 2004, Vilhena et al. 2014, Uzzi et al. 2013, Shi-Evans 2023, Sourati-Evans 2023, Krenn et al. 2023, Gu-Krenn 2024 (toutes RAPPORTÉ ; aucun PDF empreinté dans les faits). La forme « cloche » de l'effet de la distance est RAPPORTÉ pour les mesures de surface (Uzzi 2013 ; Fang-Lee-Schilling 2010 ; Derex-Boyd 2016), la forme monotone pour une surprise mesurée sous plongement (Shi-Evans 2023) ; le signe dépend donc de la définition, et c'est le seul résultat robuste que les pièces s'accordent à rapporter. Les transitions mesurées portent sur la structure sociale des champs (Guimerà 2005 ; Bettencourt-Kaiser 2015, RAPPORTÉ) et sur le rythme des nouveautés (Tria et al. 2014), jamais sur P(reprise | paire). Pour la question G : un seuil d'auto-entretien R₀ > 1 est RAPPORTÉ (Argon : Bettencourt et al. 2006, 2008), le mot « allumage » n'est pas attesté pour les champs scientifiques ; les deux PDF sont à verser avant citation.

**Ce qui n'est pas établi.** (1) Que la fertilité soit une propriété de la paire : les pièces plaident pour un quadruplet (paire, procédé, budget, juge) dépendant du temps. (2) Que « trou » et « distance » soient séparables : la critique D a montré que mon E1 ne les opposait pas ; E1′ remplace l'opposition par un test d'information conditionnelle, et son étiquette ne doit plus dépendre du canal. (3) Qu'une base de ponts post-1991 assez grande pour la puissance requise existe : c'est le goulot réel, et la critique B a raison de dire que ni A ni D ne l'ont budgété. (4) Que les juges figés notent le contenu et non le jargon ou leur mémoire : la critique C a invalidé mon E4 ; E4′ le teste sur qualité plantée. (5) Que les essaims apportent autre chose qu'un prompt long : aucune ablation publiée (RAPPORTÉ) ; E3′ ajoute les témoins qui le départagent. (6) Que l'apprentissage profond identifie des causes : il estime sous identification donnée, point acquis par toutes les pièces. (7) Que Gu-Krenn mesure autre chose que la fermeture locale : OBSERVÉ-NON-AUDITÉ, et la strate à longue portée a une composition à contrôler. (8) Les faits sur les deux événements OpenAI restent contradictoires entre pièces (162 contre 300 formalisations ; date de Bastounis et al.) et ne tranchent rien sur la génération de questions, puisque les deux systèmes reçoivent leurs problèmes.

**L'expérience à faire en premier : E6′.** Elle ne coûte rien (données publiques), ne dépend ni de la base de ponts ni des juges figés, et répond à la seule question où une décision immédiate est demandée (« réutiliser dès maintenant Gu-Krenn ? »). Elle produit en outre le témoin « popularité seule » et le contrôle de fuite par étiquettes dont E1′ a besoin, et sa reproduction vérifie un chiffre RAPPORTÉ (aire sous la courbe > 0,9) dont tout le reste du programme dépend. Si la reproduction échoue, on l'apprend avant d'avoir dépensé une journée humaine. En parallèle, sans calcul : constitution de la base de ponts avec la nouvelle étiquette et calcul de puissance ; si la puissance est insuffisante, E1′ n'est pas lancée et on le dit. Viennent ensuite E4′ (il décide si les juges peuvent étiqueter) et E2′ (il décide si le mot « transition » a le droit d'exister), puis seulement E3′ et E5′.

FIN-DE-CELLULE