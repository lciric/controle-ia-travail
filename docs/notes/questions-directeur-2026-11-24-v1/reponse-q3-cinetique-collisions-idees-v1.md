# Réponse à la question 3 : une cinétique chimique des collisions d'idées, écrite sur le taux de naissance fusionné, et ce qu'elle prédit en plus (v1)

- **Nature** : pièce de travail (classe C). Aucune dépense, aucun appel à un modèle payant, aucune course lancée.
- **Heure** : `2026-11-24T11:08:37Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`, branche `idees/questions-directeur-2026-11-24-v1`.
- **Fichiers lus** : `CLAUDE.md` (`dcd1e7ce…`) ; mandat (`ab6f19bb…`) ; demandes reformulées, question 3 (`52d1cc47…`) ; `reponse-fable-max-v1.md` en entier (`8ec4f9e0…`) ; réponses aux questions 2 (`7f4cf73f…`, sections 2 à 5) et 7 (`937e3e69…`, en entier) ; réponse de Carbon, sections 2.3 à 2.5 et 3 à 6 (`a9532fbb…`) ; intuitions du directeur, messages 2, 4 et 5, par recherche (`6f6397ee…`) ; demande reformulée d'origine, règle sur les analogies (`230585b9…`) ; note des hypothèses, lignes 189 à 205 et 298 à 337 (`5968ce0e…`) ; explication des mondes plantés, sections 1 à 3 (`895dbc0e…`). Rien d'ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **Calcul** : `simulation-cinetique-barriere-v1.py` (`57dd7cc9…`), sortie `simulation-cinetique-barriere-v1-sortie.txt` (`500e94df…`), même dossier, processeur, trois secondes, graine racine 20261124 par `numpy.random.SeedSequence`.
- **PDF téléchargés, hors dépôt** (droits), dans `/tmp/claude-0/-home-user-controle-ia-travail/72cb7e89-3107-5c40-8de3-bdb9cf3a5211/scratchpad/pdf-q3/` : `tria-2014-srep05890.pdf` (`a4ed7343…`), `hinton-2015-1503.02531v1.pdf` (`74e66891…`), `peeperkorn-2024-2405.00492v1.pdf` (`67766250…`), `kang-trizio-parrinello-2401.05279v2.pdf` (`65df2a63…`), `dellago-tps-cond-mat-0405116.pdf` (`6eb25b8c…`, sans usage : il ne contient pas la définition cherchée).

## Verdict

**Garder en partie** (confiance 0,6). Dans le corpus, la cinétique redonne le taux fusionné : son exponentielle est un facteur d'Arrhenius dont la barrière n'est pas identifiable sans température. Elle ajoute quatre prédictions de forme que le taux log-linéaire exclut : étape limitante, catalyseur à voie parallèle, ordre en porteurs, précurseur structural d'autocatalyse. Dans l'organisme, la température existe : la barrière s'y mesure, le catalyseur s'y sépare du préfacteur.

## 1. Dictionnaire exact

Point de départ, la fusion de la réponse à la question 7 : `log λ_ab = log p⁰_ab + βZ_ab + γF_ab + δP_ab`, soit `λ = exp(−[S − βZ − γF − δP])` avec `S = −log p⁰`. C'est déjà une loi d'Arrhenius `k = A·exp(−E/Θ)` [1] : l'unité d'énergie est fixée par le coefficient 1 de S (un nat de surprise du public), et `E/Θ = S − βZ − γF − δP`.

| Terme | Grandeur mesurable, données brutes | Statut |
|---|---|---|
| Concentration | `n_a(t)` : auteurs actifs sur le concept a dans l'année (OpenAlex) ; dans l'organisme, nombre de contextes où a figure | ajoute (ordre, section 2) ; en partie dans p⁰ (popularité) |
| Fréquence de collision | rencontres sans prise : a et b coprésents dans un résumé sans relation extraite (PubTator 3 [32]), auteurs communs ; dans l'organisme, présentations de la paire | ajoute : sépare la rencontre de la prise, que p⁰ confond |
| Facteur d'orientation (stérique) | part des rencontres où les structures s'emboîtent : `exp(βZ)`, Z la serrure-clé de Fable | **redonne Z** |
| Énergie d'activation E | corpus : seulement `E/Θ` ; organisme : écart de log-probabilité, en nats, entre la route vers l'idée et le mode du proposeur, lu sur la pente du tracé d'Arrhenius | identifiable dans l'organisme seulement (section 3) |
| Température Θ | corpus : aucune variable observée (test de la section 3) ; organisme : température d'échantillonnage, forme exacte de Boltzmann `exp(z_i/T)/Σ_j exp(z_j/T)` [7, éq. (1), p. 2-3] | **ajoute dans l'organisme** ; l'« agitation » du directeur n'a pas d'équivalent dans le corpus |
| Catalyseur | méthode ou instrument m présent dans le document de naissance, non consommé, qui ouvre une voie parallèle | ajoute ; **le champ F de Fable est un catalyseur** (propre à la paire par `s_a(k)s_b(k)`), non un champ |
| Champ, au sens physique | déplacement uniforme de toutes les barrières : effet d'époque | **écarté** : c'est le taux de base λ₀(t) du modèle de Cox, déjà absorbé |
| Complexe activé | corpus : aucune grandeur ; organisme : préfixe d'un raisonnement depuis lequel la moitié des continuations rééchantillonnées atteignent l'idée (commettant ½ [6, p. 1]) | **écarté dans le corpus**, ajoute dans l'organisme |
| Ordre de réaction | exposants de `n_a`, `n_b`, `n_ab` (porteurs des deux) dans le taux | ajoute |
| Étape limitante | forme en série rencontre-barrière [3] | ajoute |
| Autocatalyse | multiplicateur `e^ζ` des paires alignées et rapport de branchement n de Fable | **redonne** ; ajoute un précurseur structural (prédiction 4) |
| Réversibilité | mort d'un pont : premier lien sans reprise en dix ans, ou contredit (PubTator 3, signes) | ajoute (prédiction 5) |
| Emboîtement aléatoire « comme les protéines » | arrivées de Poisson | **redonne** (Fable, partie 2 ; note, l. 330) |

La note des hypothèses (l. 321) nommait déjà « rencontres × prise » théorie des collisions, sans en fixer la combinaison : la section 2 la rend testable.

## 2. Ce que la cinétique prédit en plus

**Prédiction 1, étape limitante.** *Démontré dans le modèle* (schéma rencontre ⇌ séparation, puis prise ; temps moyen jusqu'à la naissance) : `1/λ = 1/k_D + 1/k_r + k_sep/(k_D·k_r)`. Rencontres brèves (`k_sep` grand) : `λ ≈ (k_D/k_sep)·k_r`, produit, c'est le taux fusionné, p⁰ y joue la constante d'équilibre de la rencontre, interaction nulle. Rencontres durables (`k_sep → 0`, on travaille ensemble jusqu'à la prise) : forme en série `λ = k_D·k_r/(k_D + k_r)` [3] ; l'élasticité au contact vaut `k_r/(k_D+k_r)`, celle de la prise `k_D/(k_D+k_r)`, leur somme 1, et la dérivée croisée de `log λ` vaut `k_D·k_r/(k_D+k_r)² > 0`. Le signe de l'interaction contact × structure dit donc le régime. Simulation du régime durable (sortie, partie B) : interaction +0,118 (écart type 0,006) ; élasticité au contact 0,30, 0,42, 0,55 du tiers bas au tiers haut de Z. *Test* : modèle de Cox avec log-contact, Z et leur produit, puis forme générale ajustée par vraisemblance hors échantillon. *Données* : rencontres sans prise et auteurs communs avant t, PubTator 3, gel fin 2010, naissances 2011-2015 (Fable, partie 7). *Réfutation* : interaction négative, gardes tenues (les deux régimes tombent) ; interaction nulle : la cinétique n'ajoute rien au taux fusionné sur ce point. Les « belles au bois dormant » (note, l. 325) sont le régime `k_D ≪ k_r`.

**Corollaire, sur le terme des problèmes δP.** Un problème peut agir par l'attention (il fait rencontrer : il entre dans `k_D`) ou par la serrure (il abaisse la barrière : il entre dans `k_r`). En régime durable, un signe tranche : par l'attention, l'effet de P décroît avec le contact et croît avec Z ; par la serrure, il croît avec le contact et décroît avec Z. En régime bref, les deux voies sont indiscernables. La question 7 laissait ce mécanisme ouvert (« la serrure devient le problème »).

**Prédiction 2, catalyseur contre champ.** *Supposé* : une méthode ouvre une voie parallèle, `λ = p⁰·[e^{βZ+δP} + κ·Σ_m c_m h_a(m) h_b(m)·e^{β_c Z}]`. Pour une voie catalytique faible, `log(1+x) ≈ x` redonne `γF` : le terme de Fable en est le premier ordre, exact seulement si `β_c = β`. *Prédictions* : (a) `log λ` concave en F (saturation) ; (b) si la méthode remplace l'emboîtement (`β_c < β`), le gain relatif est plus fort pour les paires de Z faible, interaction F × Z négative ; un champ au sens de Fable donne le même gain relatif partout. *Test* : arrivée datée d'un instrument (Kinect [26]), différence de différences du gain par tiers de Z ; modèle additif d'Aalen [29] contre Cox. *Réfutation* : gain relatif égal dans les trois tiers, aucune concavité. La chimie ne fixe pas le signe : il se mesure.

**Prédiction 3, ordre en porteurs.** *Supposé* (action de masse) : `λ ∝ n_a^{m_a}·n_b^{m_b}·n_ab^{m_ab}`. Trois mécanismes élémentaires donnent trois signatures : un porteur des deux concepts (`m_ab = 1`, `m_a = m_b = 0` à `n_ab` fixé), la rencontre de deux spécialistes (`m_a = m_b = 1` à contact fixé), un explorateur solitaire (ordre 1 en popularité). *Critère des chimistes* : la constante `λ/(n_a^{m_a} n_b^{m_b})` ne dépend pas des concentrations ; sinon, saturation (analogue de Michaelis et Menten) ou mécanisme composé. *Test* : régression des naissances sur `log n_a`, `log n_b`, `log n_ab`, par champ et période. *Réfutation* : ordres non entiers, instables entre champs : simple élasticité, rien de plus que p⁰. Zone en partie occupée : la répartition des experts prédit les découvertes [25] ; l'action de masse sur les porteurs sert depuis 1964 à la diffusion des idées [23, 24], non à la naissance des ponts.

**Prédiction 4, précurseur structural de l'avalanche.** Le rapport de branchement de Fable (processus de Hawkes [28]) constate l'avalanche sur l'histoire des naissances ; la théorie des ensembles autocatalytiques la prévoit sur la structure. *Supposé* : réaction = naissance du lien (a,b) ; catalyseurs = méthodes et concepts employés dans l'article de naissance ; nourriture = concepts établis avant t. On cherche le plus grand ensemble réflexivement autocatalytique nourri par cette base (chaque réaction catalysée par un membre, chaque membre constructible depuis la nourriture ; algorithme polynomial [11]). Dans le modèle des polymères binaires, ils apparaissent quand chaque molécule catalyse en moyenne une à deux réactions [12, section 5 ; 13] : seuil de modèle, non transposable. *Test* : la taille de cet ensemble à t prédit-elle un rapport de branchement ≥ 1 sur la période suivante, au-delà de l'activité et des comptes passés ? *Réfutation* : aucun gain hors échantillon. Le saut « en crosse de hockey » d'un processus de naissance et mort combinatoire est déjà établi [14].

**Prédiction 5, secondaire, réversibilité.** Dans une famille de réactions, la barrière baisse quand le produit est plus stable (Evans et Polanyi [4]). Traduction : par couple de types d'entités, log du taux de naissance et log des chances de survie du pont liés linéairement, pente entre 0 et 1 ; le taux fusionné ne relie pas naissance et survie. *Garde* : deux estimations sur périodes disjointes, sinon artefact de compensation [5]. *Réfutation* : pente nulle ou hors de [0, 1].

## 3. Équations, hypothèses, identifiabilité

Forme complète, par paire et par tranche de temps :

`1/λ_ab = 1/k_D + 1/k_r + k_sep/(k_D·k_r)`, `k_D = κ₀·n_a^{m_a}·n_b^{m_b}·C_ab`, `k_r = ν·[e^{−E_ab/Θ} + Σ_m c_m h_a(m) h_b(m)·e^{−E^m_ab/Θ}]`, `E_ab = E₀ − β′Z_ab − δ′P_ab`.

*Hypothèses* : rencontres poissoniennes indépendantes, état quasi stationnaire dans la tranche, étape élémentaire (une rencontre, un essai), barrière fixe dans une famille, pas de retour dans la tranche, taux pris comme l'inverse du temps moyen. *Limite* rencontres brèves, voie catalytique faible : `log λ = log(k_D/k_sep) + log ν − E₀/Θ + (β′/Θ)Z + (δ′/Θ)P + γF`, le taux fusionné, avec `log p⁰ ≈ log(k_D/k_sep)`.

*Identifiabilité.* À Θ constant, seuls les rapports `β′/Θ`, `δ′/Θ`, `E₀/Θ` existent, et `E₀` se confond avec `log ν`. La barrière s'identifie, à une unité près, sous l'une de deux conditions :
1. **Corpus** : une variable de strate s (champ, période) multiplie tous les coefficients de barrière par un même facteur `1/Θ_s` sans toucher au préfacteur. Test : la matrice des coefficients (S, Z, F, P) par strate est de rang 1 (régression de rang réduit) ; alors les Θ_s relatifs et les barrières en une unité commune sont identifiés. Rang supérieur à 1 : aucune température, et l'énergie d'activation reste un nom.
2. **Organisme** : Θ = T fixé par l'expérimentateur, indépendant de la barrière plantée. Il faut au moins trois températures ; le préfacteur dépend de T (normalisation du softmax, comme le facteur en T d'Eyring [2]), d'où la forme `ln k = ln A + m·ln T − E/T`. Une idée qu'on peut dire de plusieurs façons a une entropie d'activation (nombre de routes), lue sur l'ordonnée à l'origine.

## 4. Dans l'organisme

**Réglages.** Température : la seule exacte, la température d'échantillonnage. La diversité des proposeurs et le budget de réflexion ne sont pas des températures : la première change les espèces présentes, le second la durée de la rencontre (`1 − e^{−kτ}`). Concentration : nombre de présentations de chaque concept et de chaque paire. Catalyseur : une fiche de méthode, de formalisme ou de concept médiateur insérée au contexte, réutilisable. Problème : une fiche d'anomalie (le δP de la question 7).

**Course de dose-réponse, décrite, non lancée.** Sur le banc des mondes plantés (miniatures à vérité connue, explication des mondes plantés, section 2) : des ponts plantés à barrière connue par construction (longueur de la correspondance cachée, vocabulaire renommé), mesurée en nats sur un proposeur ouvert dont on lit les probabilités. Plan croisé : quatre températures × catalyseur présent ou absent × trois concentrations, budget égal en jetons par case. Estimations : E par la pente en 1/T ; ΔE du catalyseur par l'interaction présence × 1/T ; ordre par la pente en log-concentration.

**Ordres de grandeur** (simulation, partie A, quatre températures de 0,4 à 1,3) : pour une barrière de 2,5 nats, 1 600 collisions donnent 2,63 ± 0,59, 6 400 donnent 2,53 ± 0,27 ; à 3,5 nats, 400 collisions ne donnent rien d'utilisable. Le test qui sépare un catalyseur (ΔE = 1 nat) d'un préfacteur de même gain à T = 1 a une puissance de 0,35 à 3 200 collisions et de 0,96 à 12 800, faux positifs 0,02. C'est la signature du chimiste : le gain d'un catalyseur décroît quand T monte, celui d'un préfacteur ne bouge pas.

**Complexe activé.** Couper chaque trace réussie à chaque phrase, rééchantillonner M continuations, lire la part qui atteint l'idée selon l'oracle. Prédiction : saut net du commettant à une étape (barrière localisée, par exemple l'énoncé de la correspondance), contre une montée graduelle. Voisins publiés : rééchantillonnage contrefactuel des phrases [30], jetons de bifurcation [31].

**Réaction parasite** : sur des récits, la température corrèle faiblement avec la nouveauté (coefficient 0,308 ± 0,138 [8, tableau 2, p. 6]) et modérément avec l'incohérence [8, résumé] ; d'où une décomposition aux T hautes et un rendement par jeton à optimum intérieur.

**À journaliser par collision** : paire, concepts du contexte et leurs comptes, fiches de catalyseur et de problème, T, graine fille, proposeur et version, jetons d'entrée, de sortie et de réflexion, trace complète, log-probabilités des jetons, issue selon l'oracle (vérité tenue par l'orchestrateur), points de coupe et rééchantillonnages. *Témoins qui doivent mourir* : pont de barrière nulle (pente nulle), faux pont sans vérité (taux nul à toute T), étiquettes de T permutées (pente nulle). *Gardes* : la prise se juge sur l'oracle seul (N-058) ; aucune barrière estimée n'entre dans la récompense ni le choix des proposeurs (N-053, point 5) ; simulation de Gillespie [27] du plan avant toute course, pour la puissance.

## 5. Antériorité (règle R8)

- **Autocatalyse et possible adjacent** : ensembles autocatalytiques de protéines [9] ; possible adjacent [10] ; détection polynomiale [11], seuils de catalyse [12, 13] ; naissance et mort combinatoire, temps d'explosion exacts [14]. **La prédiction 4 est occupée dans sa forme** ; restent la construction du réseau catalytique daté sur la littérature et le test prédictif.
- **Chimie algorithmique** : objets du lambda-calcul qui réagissent, hypercycles et organisations auto-entretenues [15] ; production économique comme chimie [16].
- **Croissance recombinante** : la limite est de traiter l'abondance d'idées potentielles, non d'en produire [17, résumé]. C'est le régime limité par la prise, posé sans test.
- **Urnes à déclenchement** : chaque nouveauté ajoute ν+1 possibles ; nombre d'éléments distincts `D(N) ~ N^{ν/ρ}` si ν < ρ [18, éq. (1), p. 3] ; version en réseau [19]. Occupe l'autocatalyse des nouveautés à l'échelle d'une suite.
- **Choix d'expériences** : stratégies prudentes autour des molécules centrales, qui ralentissent la découverte [20, résumé ; 21] : la répartition des rencontres, non la barrière. Produits réalisables selon les composants [22].
- **Action de masse sur les porteurs** : modèles épidémiques des idées [23, 24] ; experts qui relient [25].
- **Température des modèles de langage** [8] ; commettant [6].

En deux recherches, je n'ai trouvé ni tracé d'Arrhenius ni identification d'une barrière sur la naissance d'idées, ni la forme en série testée sur des naissances de liens : deux questions, non deux trous établis.

## 6. Verdict

**Garder en partie** (confiance 0,6). *Écarter* : énergie d'activation et température dans le corpus (sauf rang 1), champ physique, complexe activé hors de l'organisme. *Garder* : prédictions 1 à 4 et, dans l'organisme, la course de dose-réponse, seule voie où la barrière se mesure. Première épreuve : la prédiction 1, greffée sans coût sur l'expérience de Fable.

## Ce que cette réponse ne permet pas de conclure

Que les naissances d'idées obéissent à une cinétique (aucune donnée lue ici), que les barrières plantées en nats représentent la difficulté d'une vraie idée, ni que les budgets simulés valent pour un vrai proposeur (taux de prise posé, non mesuré).

## Références

1. Arrhenius, S. (1889). Über die Reaktionsgeschwindigkeit bei der Inversion von Rohrzucker durch Säuren. *Zeitschrift für Physikalische Chemie* 4, 226-248. https://doi.org/10.1515/zpch-1889-0416 (notice)
2. Eyring, H. (1935). The activated complex in chemical reactions. *Journal of Chemical Physics* 3, 107-115. https://doi.org/10.1063/1.1749604 (notice)
3. Collins, F. C. et Kimball, G. E. (1949). Diffusion-controlled reaction rates. *Journal of Colloid Science* 4, 425-437. https://doi.org/10.1016/0095-8522(49)90023-9 (notice ; la forme `k_D k_r/(k_D+k_r)` est rapportée, page à vérifier)
4. Evans, M. G. et Polanyi, M. (1938). Inertia and driving force of chemical reactions. *Transactions of the Faraday Society* 34, 11. https://doi.org/10.1039/tf9383400011 (notice, première page seule ; relation rapportée, page à vérifier)
5. Krug, R. R., Hunter, W. G. et Grieger, R. A. (1976). Enthalpy-entropy compensation. 1. Some fundamental statistical problems associated with the analysis of van't Hoff and Arrhenius data. *Journal of Physical Chemistry* 80, 2335-2341. https://doi.org/10.1021/j100562a006 (notice)
6. Kang, P., Trizio, E. et Parrinello, M. (2024). Computing the committor with the committor: an anatomy of the transition state ensemble. https://arxiv.org/abs/2401.05279v2 (PDF lu, p. 1 : ensemble de transition « q(x) ≃ 1/2 »)
7. Hinton, G., Vinyals, O. et Dean, J. (2015). Distilling the knowledge in a neural network. https://arxiv.org/abs/1503.02531v1 (PDF lu, éq. (1), p. 2-3)
8. Peeperkorn, M., Kouwenhoven, T., Brown, D. et Jordanous, A. (2024). Is temperature the creativity parameter of large language models? *ICCC 2024*. https://arxiv.org/abs/2405.00492v1 (PDF lu, tableau 2, p. 6)
9. Kauffman, S. A. (1986). Autocatalytic sets of proteins. *Journal of Theoretical Biology* 119, 1-24. https://doi.org/10.1016/S0022-5193(86)80047-9 (notice)
10. Kauffman, S. A. (2000). *Investigations*. Oxford University Press. https://doi.org/10.1093/oso/9780195121049.001.0001 (notice)
11. Hordijk, W. et Steel, M. (2004). Detecting autocatalytic, self-sustaining sets in chemical reaction systems. *Journal of Theoretical Biology* 227, 451-461. https://doi.org/10.1016/j.jtbi.2003.11.020 (résumé, Europe PMC)
12. Hordijk, W. et Steel, M. (2018). Autocatalytic networks at the basis of life's origin and organization. *Life* 8(4), 62. https://doi.org/10.3390/life8040062 (texte de PubMed Central, section 5)
13. Hordijk, W., Kauffman, S. A. et Steel, M. (2011). Required levels of catalysis for emergence of autocatalytic sets in models of chemical reaction systems. *International Journal of Molecular Sciences* 12, 3085-3101. https://doi.org/10.3390/ijms12053085 (texte de PubMed Central)
14. Steel, M., Hordijk, W. et Kauffman, S. A. (2020). Dynamics of a birth-death process based on combinatorial innovation. *Journal of Theoretical Biology* 491, 110187. https://doi.org/10.1016/j.jtbi.2020.110187 (résumé, Europe PMC)
15. Fontana, W. et Buss, L. W. (1994). What would be conserved if "the tape were played twice"? *PNAS* 91, 757-761. https://doi.org/10.1073/pnas.91.2.757 (résumé) ; et « The arrival of the fittest ». *Bulletin of Mathematical Biology* 56, 1-64. https://doi.org/10.1007/BF02458289 (notice)
16. Padgett, J. F. (2003). Economic production as chemistry. *Industrial and Corporate Change* 12, 843-877. https://doi.org/10.1093/icc/12.4.843 (résumé, OpenAlex ; un seul auteur dans les notices, co-auteurs à vérifier)
17. Weitzman, M. L. (1998). Recombinant growth. *Quarterly Journal of Economics* 113, 331-360. https://doi.org/10.1162/003355398555595 (résumé, OpenAlex)
18. Tria, F., Loreto, V., Servedio, V. D. P. et Strogatz, S. H. (2014). The dynamics of correlated novelties. *Scientific Reports* 4, 5890. https://doi.org/10.1038/srep05890 (PDF lu, éq. (1), p. 3)
19. Iacopini, I., Milojević, S. et Latora, V. (2018). Network dynamics of innovation processes. *Physical Review Letters* 120, 048301. https://doi.org/10.1103/PhysRevLett.120.048301 (notice)
20. Rzhetsky, A., Foster, J. G., Foster, I. T. et Evans, J. A. (2015). Choosing experiments to accelerate collective discovery. *PNAS* 112, 14569-14574. https://doi.org/10.1073/pnas.1509757112 (résumé)
21. Foster, J. G., Rzhetsky, A. et Evans, J. A. (2015). Tradition and innovation in scientists' research strategies. *American Sociological Review* 80, 875-908. https://doi.org/10.1177/0003122415601618 (notice)
22. Fink, T. M. A., Reeves, M., Palma, R. et Farr, R. S. (2017). Serendipity and strategy in rapid innovation. *Nature Communications* 8, 2002. https://doi.org/10.1038/s41467-017-02042-w (résumé)
23. Goffman, W. et Newill, V. A. (1964). Generalization of epidemic theory: an application to the transmission of ideas. *Nature* 204, 225-228. https://doi.org/10.1038/204225a0 (notice)
24. Bettencourt, L. M. A., Cintrón-Arias, A., Kaiser, D. I. et Castillo-Chávez, C. (2006). The power of a good idea. *Physica A* 364, 513-536. https://doi.org/10.1016/j.physa.2005.08.083 (notice)
25. Sourati, J. et Evans, J. A. (2023). Accelerating science with human-aware artificial intelligence. *Nature Human Behaviour* 7, 1682-1696. https://doi.org/10.1038/s41562-023-01648-z (résumé : jusqu'à 400 % de gain de prédiction)
26. Furman, J. L. et Teodoridis, F. (2020). Automation, research technology, and researchers' trajectories. *Organization Science* 31, 330-354. https://doi.org/10.1287/orsc.2019.1308 (notice)
27. Gillespie, D. T. (1977). Exact stochastic simulation of coupled chemical reactions. *Journal of Physical Chemistry* 81, 2340-2361. https://doi.org/10.1021/j100540a008 (notice)
28. Hawkes, A. G. (1971). Spectra of some self-exciting and mutually exciting point processes. *Biometrika* 58, 83-90. https://doi.org/10.1093/biomet/58.1.83 (notice)
29. Aalen, O. O. (1989). A linear regression model for the analysis of life times. *Statistics in Medicine* 8, 907-925. https://doi.org/10.1002/sim.4780080803 (notice)
30. Bogdan, P. C., Macar, U., Nanda, N. et Conmy, A. (2025). Thought anchors: which LLM reasoning steps matter? https://arxiv.org/abs/2506.19143 (résumé)
31. Bigelow, E., Holtzman, A., Tanaka, H. et Ullman, T. (2024). Forking paths in neural text generation. https://arxiv.org/abs/2412.07961 (résumé)
32. Wei, C.-H. et al. (2024). PubTator 3.0. *Nucleic Acids Research* 52, W540-W546. https://doi.org/10.1093/nar/gkae235 (d'après la réponse à la question 7)
