# Proposition B : Tour III.1, de quoi un organisme d'agents a besoin pour produire des mathématiques inédites et vérifiables

**Pièces reçues.** Le bloc FAITS et le bloc QUESTION sont complets ; je ne détecte ni coupure ni vide.

**Statuts.** Les FAITS ne portent pas de statut explicite. J'en attribue un une fois et je le garde ensuite :
- la description de l'organisme et de ce qui est « déjà conçu » : **RAPPORTÉ** (déclaré par le programme, non audité par moi) ;
- les annonces externes (Riemann, Navier-Stokes, problèmes ouverts) : **RAPPORTÉ, non vérifié**. Je ne sais pas si l'une d'elles tient.
- les travaux publiés que je cite : **RAPPORTÉ**, de mémoire, à relire à la source. Conformément à la règle 3, je ne donne aucun identifiant arXiv, même là où la question les demande.
- tout le reste est ma proposition : **HYPOTHÈSE**.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut |
|---|---|---|
| S1 | Le programme a besoin de mathématiques *nouvelles*, et non de mathématiques connues correctement posées et appliquées. Le besoin est déclaré ; sa nature ne l'est pas. | HYPOTHÈSE |
| S2 | Des systèmes à base de LLM ont produit des résultats mathématiques nouveaux. C'est publié pour des constructions et des preuves formelles de niveau compétition. Pour Riemann et Navier-Stokes, je ne sais pas. | RAPPORTÉ / non vérifié |
| S3 | Ce qui a marché en combinatoire extrémale se transporte aux statistiques de détection adverse. | HYPOTHÈSE |
| S4 | Mathlib couvre les objets nécessaires : divergences, martingales, temps d'arrêt, couplages. Je ne connais pas le degré de couverture actuel. | HYPOTHÈSE |
| S5 | L'arbitre Lean sera opérationnel. Les FAITS disent que l'outillage n'est pas encore relevé conforme. | RAPPORTÉ (non conforme) |
| S6 | Quelques centaines de dollars par course suffisent pour une découverte réelle. | HYPOTHÈSE |
| S7 | L'« utilité » d'un résultat se mesure indépendamment de son auteur. | HYPOTHÈSE |

---

## 1. Ce qu'un expert ferait, et qu'on ne demande pas

**1.1. Poser les énoncés avant de lancer la machine.**
Chaque impossibilité de détection dépend entièrement de trois choix de modèle :
- ce qu'observe le moniteur (activations, transcriptions, sorties) ;
- ce que contrôle le saboteur (sa loi marginale, les corrélations entre moniteurs, son adaptation au moniteur) ;
- ce que signifie « faible taux de fausses alertes » (par tâche, par épisode, à horizon infini).

Le premier mode d'échec attendu n'est pas une preuve fausse. C'est un théorème vrai sur le mauvais modèle (HYPOTHÈSE). Un expert écrirait les cinq questions cibles comme définitions formelles, à la main, et les ferait relire avant toute génération.

**1.2. Chercher le classique dont chaque question est un cas.** Sources RAPPORTÉ, à relire :
- **Indiscernabilité, information.** Bornes inférieures minimax de Le Cam (deux points), Fano et Assouad, exposées par Tsybakov, *Introduction to Nonparametric Estimation* (2009), chapitre 2. Indiscernabilité calculatoire : Goldwasser, Kim, Vaikuntanathan, Zamir (2022), *Planting Undetectable Backdoors in Machine Learning Models*.
- **Détection séquentielle.** Test séquentiel du rapport de vraisemblance (SPRT) de Wald (1945), CUSUM de Page (1954), optimalité de Lorden (1971). Version moderne en échantillon fini : e-processus et inégalité de Ville, présentés par Ramdas, Grünwald, Vovk, Shafer (2023), *Game-theoretic statistics and safe anytime-valid inference*.
- **Agrégation sous corrélation adverse.** Fusion de p-valeurs et d'e-valeurs sous dépendance arbitraire (Vovk & Wang ; voir *E-values: calibration, combination and applications*, 2021). Bornes de Rüschendorf et d'Embrechts–Puccetti sur les agrégats à marges fixées et dépendance inconnue (titre exact : référence à vérifier).
- **Jeu d'audit sous budget.** Jeux de Stackelberg de sécurité (littérature Tambe et coll. ; référence précise à vérifier). Côté contrôle de l'IA : Greenblatt, Shlegeris et coll. (2023), *AI Control: Improving Safety Despite Intentional Subversion*.

Un expert s'attend à ce qu'une bonne part des « résultats nouveaux » demandés soit du folklore à constantes près (HYPOTHÈSE, à tester : voir P1). L'inédit plausible se loge dans la combinaison d'adversaires : le saboteur choisit à la fois l'effet de son sabotage, la dépendance entre moniteurs et son temps d'action. Les cadres classiques traitent ces dimensions séparément (HYPOTHÈSE).

**1.3. Choisir le type d'objet que la machine sait produire.** Les succès publiés relèvent de deux familles (RAPPORTÉ, section 3) :
- des **constructions** (∃ un objet dont un programme calcule le score) ;
- des **preuves formelles** dans un corpus bien couvert.

Un théorème d'impossibilité est un énoncé universel (∀). Sa preuve par réduction passe pourtant souvent par un ∃ : on exhibe deux mondes que le moniteur ne distingue pas, l'un honnête, l'un saboteur. C'est exactement la « lecture à l'envers » des FAITS (RAPPORTÉ). L'expert transformerait chaque impossibilité visée en recherche de paires de mondes, que l'on peut évaluer, puis en gabarit de preuve.

**1.4. Fixer l'utilité avant le résultat.** Un résultat est utile s'il change une décision de conception : seuil, nombre de moniteurs, part du budget d'audit, horizon. Sinon il est peut-être vrai et nouveau, mais pas utile au programme.

**1.5. Mettre un probabiliste dans la boucle tôt.** Quelques heures à la pose des énoncés valent plus que des jours à la fin (HYPOTHÈSE). La relecture humaine est rare (RAPPORTÉ) : il faut donc la dépenser au début, sur les énoncés, pas sur les preuves.

**1.6. Calibrer sur le connu du domaine.** Les douze mondes du pilote (RAPPORTÉ) sont des mondes mathématiques génériques. L'expert planterait des résultats connus du domaine, déguisés : optimalité du SPRT, borne de Ville, validité de Bonferroni sous dépendance arbitraire, borne de Le Cam. Il exigerait que l'organisme les redécouvre, et les signale comme connus, avant d'annoncer quoi que ce soit de nouveau.

---

## 2. Données brutes à prendre au départ

| Source | Contenu brut | Pourquoi |
|---|---|---|
| Dépôt git de Mathlib, avec son historique | Définitions, lemmes, retraits, renommages | Mesurer la couverture réelle (S4) ; l'historique montre ce qui a été difficile à formaliser |
| Archives publiques du Zulip Lean | Discussions d'échecs de formalisation | Banque d'échecs d'énoncés, pas seulement de preuves |
| Traces extraites par LeanDojo (Yang et al., 2023, *LeanDojo: Theorem Proving with Retrieval-Augmented Language Models*) | États tactiques, prémisses utilisées | Journaux de preuve pas à pas |
| miniF2F (Zheng, Han, Polu, 2021), ProofNet (Azerbayev et al., 2023 ; titre à vérifier), PutnamBench (Tsoukalas et al., 2024) | Énoncés formels et informels appariés | Mesurer la dérive de formalisation |
| Sources LaTeX arXiv (math.ST, math.PR, stat.ML, cs.CR, cs.LG), zbMATH Open | Texte intégral, pas les résumés | Recherche d'antériorité sur les énoncés, pas sur les mots-clés |
| Stoyanov, *Counterexamples in Probability* ; Gelbaum & Olmsted, *Counterexamples in Analysis* | Contre-exemples classiques | Banque de contre-exemples adaptée au domaine (probabilités, convergence, indépendance) |
| OEIS, House of Graphs | Suites et graphes | Utiles seulement si une question devient combinatoire |
| Dépôt du projet « equational theories » (Tao et coll., 2024) | Implications entre lois de magmas, preuves automatiques et humaines mêlées | Seule archive publique que je connaisse où l'on voit à grande échelle ce que l'automatique a fait seul et ce qu'il n'a pas fait (RAPPORTÉ ; détails à relire) |
| Site des problèmes d'Erdős (T. Bloom) | Statuts et historique | Rapporté de mémoire, à vérifier : un épisode récent où des « solutions par IA » étaient en fait des retrouvailles de littérature. Cas d'école pour la nouveauté. |
| Mémoire des tentatives de l'organisme (RAPPORTÉ) | Chaque mort, brute, avec le monde qui l'a tuée | La donnée la plus spécifique au programme |
| Traces de scores des moniteurs, si le programme en a | Loi jointe empirique des scores, honnête et sabotage | Seul moyen de savoir quelles corrélations adverses sont réalistes. Je ne sais pas si ces traces existent. |

---

## 3. Méthodes réellement employées : ce qu'elles supposent, ce qu'elles ont donné, où elles échouent

Tout ce qui est attribué à un travail publié est RAPPORTÉ, de mémoire.

**3.1. Recherche guidée par programme évaluable, sélection évolutionnaire.**
- *Travaux.* Romera-Paredes et al. (2024), *Mathematical discoveries from program search with large language models* (Nature ; FunSearch). Novikov et al. (2025), *AlphaEvolve: A coding agent for scientific and algorithmic discovery* (livre blanc DeepMind ; titre à vérifier). Georgiev, Gómez-Serrano, Tao, Wagner (2025), *Mathematical exploration and discovery at scale* (titre exact à vérifier).
- *Ce qu'elle suppose.* Un évaluateur automatique, peu coûteux et fidèle, qui note un objet candidat.
- *Ce qu'elle a donné.* Des constructions : ensembles sans triplet aligné (cap sets) en petite dimension, heuristiques de rangement en ligne (bin packing), schémas de multiplication de matrices, bornes inférieures améliorées sur des problèmes extrémaux.
- *Où elle échoue.* Elle ne prouve pas l'optimalité. Elle ne produit pas d'énoncés universels. Les gains sont souvent marginaux. Elle exploite les failles de l'évaluateur. Sans expert pour choisir le problème et l'évaluateur, je ne sais pas ce qu'elle donne.

**3.2. Découverte de contre-exemples.**
- *Travaux.* Wagner (2021), *Constructions in combinatorics via neural networks* : apprentissage par renforcement à entropie croisée, qui réfute des conjectures de théorie des graphes. Côté solveurs SAT, sans LLM : Heule, Kullmann, Marek (2016), triplets pythagoriciens booléens ; Brakensiek, Heule, Mackey, Narváez (2020), conjecture de Keller en dimension 7.
- *Ce qu'elle suppose.* Un espace fini ou fini après réduction.
- *Ce qu'elle a donné.* Des réfutations nettes. Côté SAT, des certificats rejouables.
- *Où elle échoue.* Les espaces continus. Or les distributions de scores le sont ; une discrétisation est nécessaire (P2).

**3.3. Conjecture automatique.**
- *Travaux.* Graffiti (Fajtlowicz, années 1980). Raayoni et al. (2021), *Generating conjectures on fundamental constants with the Ramanujan Machine* (Nature). Davies et al. (2021), *Advancing mathematics by guiding human intuition with AI* (Nature ; théorie des nœuds, polynômes de Kazhdan–Lusztig).
- *Ce qu'elle suppose.* Beaucoup de données calculées et un mathématicien pour trier.
- *Ce qu'elle a donné.* Des conjectures, dont certaines ont ensuite été prouvées par des humains.
- *Où elle échoue.* Le taux de conjectures triviales ou fausses. Le tri humain est le goulet.

**3.4. Formalisation automatique.**
- *Travaux.* Wu et al. (2022), *Autoformalization with Large Language Models*.
- *Ce qu'elle suppose.* Des énoncés proches du style du corpus.
- *Où elle échoue.* La dérive d'énoncé : quantificateur inversé, inégalité large au lieu de stricte, hypothèse perdue. Le noyau Lean certifie alors un théorème qui n'est pas celui qu'on voulait. C'est le risque principal pour ce programme (HYPOTHÈSE).

**3.5. Recherche de preuve dans Lean.**
- *Travaux.* Polu & Sutskever (2020), *Generative Language Modeling for Automated Theorem Proving* (GPT-f). LeanDojo et ReProver (ci-dessus). Xin et al. (2024), *DeepSeek-Prover* (titre à vérifier), puis V2. AlphaProof (DeepMind 2024, annonce d'une médaille d'argent à l'Olympiade internationale de mathématiques ; publication détaillée : référence à vérifier). Trinh et al. (2024), *Solving olympiad geometry without human demonstrations* (Nature ; AlphaGeometry, moteur symbolique dédié).
- *Ce qu'elle suppose.* Un énoncé formel correct et une bibliothèque couvrante.
- *Ce qu'elle a donné.* Des preuves de niveau compétition.
- *Où elle échoue.* Les preuves de niveau recherche qui exigent de nouvelles définitions. Je ne connais aucun résultat de recherche en probabilités prouvé de bout en bout par ces systèmes (« je ne sais pas » plutôt que « il n'y en a pas »).

**3.6. Décomposition en lemmes.**
- *Travaux.* Jiang et al. (2023), *Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs*. Côté humain, les « blueprints » (outil leanblueprint, P. Massot) : formalisation de PFR (Gowers, Green, Manners, Tao 2023) en quelques semaines par une communauté menée par Tao, et Liquid Tensor Experiment (défi de Scholze).
- *Ce qu'elle suppose.* Qu'une preuve informelle existe déjà.
- *Ce qu'elle a donné.* La formalisation de mathématiques de recherche existantes, par des humains outillés, pas par des agents autonomes.

**3.7. Mémoire et réemploi.**
- *Travaux.* Wang et al. (2024), *LEGO-Prover: Neural Theorem Proving with Growing Libraries* (titre à vérifier).
- *Ce qu'elle suppose.* Que des lemmes produits en cours de route se réemploient.
- *Ce qu'elle a donné.* Des gains sur des bancs d'essai.
- *Où elle échoue.* La bibliothèque se remplit de lemmes redondants. Je ne sais pas si le réemploi a produit un résultat nouveau hors des bancs d'essai.

**Constat transversal** (HYPOTHÈSE fondée sur les cas cités). Chaque résultat réellement nouveau listé ci-dessus réunit trois éléments :
1. un problème choisi par un expert ;
2. un vérificateur mécanique : évaluateur, solveur SAT ou noyau Lean ;
3. un objet de type ∃, ou une preuve dont un humain connaissait déjà la forme.

Le programme possède partiellement le point 2 (le harnais n'est pas conforme). Il possède peu le point 1, faute de relecture humaine fréquente. Il vise surtout des énoncés universels, ce qui contrevient au point 3.

---

## 4. Ce qui vérifierait, hors du programme, qu'un résultat est vrai, nouveau et utile

**Vrai.**
- *Noyau Lean, avec audit.* `#print axioms` sur le théorème final. Refus de tout `sorry`. Liste fermée d'axiomes autorisés. Version de Mathlib épinglée. Vérification par un second vérificateur de noyau indépendant, si l'outil est disponible ; je ne sais pas lequel est mûr aujourd'hui.
- *Relecture de l'énoncé.* Le noyau ne vérifie pas que l'énoncé formel dit ce qu'on croit. Un humain extérieur relit l'énoncé formel seul, sans la preuve, et le retraduit.
- *Certificats rejouables pour les résultats calculatoires.* Pour SAT, une preuve DRAT ou LRAT vérifiée par un vérificateur certifié (cake_lpr, si je ne me trompe pas). Pour un programme linéaire (LP), un certificat dual en arithmétique rationnelle exacte. Le verdict ne doit jamais reposer sur un flottant.

**Nouveau.**
- Recherche d'antériorité sur l'énoncé normalisé, pas sur les mots : texte intégral arXiv, zbMATH Open, manuels du domaine (section 2).
- Demander à deux spécialistes extérieurs : « est-ce connu ? ». C'est la seule méthode qui attrape le folklore non écrit.
- L'épisode des problèmes d'Erdős (section 2) montre que « l'IA a trouvé » peut vouloir dire « l'IA a retrouvé ».

**Utile.** Un pré-enregistrement : la décision de conception que le résultat doit changer. On rejoue ensuite cette décision sur les mondes plantés de l'étage de tests de mort (RAPPORTÉ), avec et sans le résultat.

**Réplication.** Rejouer avec une autre graine et une autre lignée de proposeur. Publier la preuve et l'énoncé pour que des tiers les rejouent.

---

## 5. Reformulation de la demande

> « Pour chacune des cinq questions cibles, produire : (i) un énoncé formel relu par un humain extérieur avant toute recherche de preuve ; (ii) le résultat publié le plus proche, avec l'écart exact qui reste ouvert, ou la conclusion "déjà connu" ; (iii) si l'écart est ouvert, une construction ou une preuve vérifiable mécaniquement (noyau Lean audité, ou certificat exact rejouable) ; (iv) une décision de conception des moniteurs, pré-enregistrée, que le résultat change sur les mondes plantés. Un résultat sans (i) et (ii) ne compte pas. Un résultat sans (iv) compte comme mathématique, pas comme contribution au programme. Le livrable par défaut attendu est "déjà connu, voici où" ; c'est une issue valide. »

---

## 6. Propositions concrètes

Chaque proposition est une HYPOTHÈSE. Tous les coûts sont **illustratifs**. Chaque test de mort est un duel où les deux issues falsifient quelque chose (B4).

### P1. Carte du folklore : réduire avant de produire

- **Premier pas.** Pour chaque question cible, un probabiliste et l'organisme, en recherche assistée, écrivent le théorème connu le plus proche et l'écart résiduel en une phrase formelle.
- **Coût.** Quelques jours-personne d'expert, plus un calcul négligeable (illustratif).
- **Duel.**
  - H_A : la question se réduit à un résultat publié, aux constantes près.
  - H_B : il reste un écart non couvert.
- **Métrique.** Un expert extérieur, aveugle à l'origine, confirme ou non la réduction.
- **Contrôle négatif.** Un énoncé connu, planté sous déguisement, doit être classé « réduit ».
- **Issues.**
  - L'expert valide la réduction : H_B est falsifiée pour cette question, et le budget de génération y est coupé.
  - L'expert exhibe une hypothèse du cadre classique violée par le modèle d'adversaire : H_A est falsifiée et l'écart devient la cible.
- **Différence avec le publié.** Aucune ; c'est voulu. Ce n'est pas une découverte, c'est le filtre qui évite d'en annoncer de fausses.

### P2. Pire dépendance pour l'agrégation : calcul exact, puis conjecture, puis preuve

- **Idée.** À marges fixées des scores de k moniteurs, l'adversaire choisit la loi jointe sous sabotage pour minimiser la puissance d'un agrégateur, à taux de fausses alertes fixé. Pour des marges discrètes, c'est un programme linéaire multi-marginal : la valeur exacte est calculable et porte un certificat dual.
- **Premier pas.** Résoudre ce programme linéaire en arithmétique exacte pour k ≤ 4 sur des marges discrétisées, puis comparer, pour chaque agrégateur candidat, sa puissance dans le pire cas.
- **Coût.** Heures de CPU, solveur ouvert (HiGHS, ou exact rationnel), dizaines de dollars (illustratif). La taille du programme croît exponentiellement en k ; au-delà de petits k, je ne sais pas.
- **Duel.**
  - H_A : la courbe de puissance dans le pire cas coïncide, partout, avec ce que donnent les bornes connues de fusion sous dépendance arbitraire (Vovk–Wang, Rüschendorf).
  - H_B : il existe un régime (k, seuil, marges) avec un écart strict, certifié par le dual.
- **Seuil.** Écart strictement positif, certifié en rationnel exact. Pas de tolérance flottante.
- **Contrôle négatif.** Le cas indépendant, où la puissance doit retrouver la valeur classique calculée à part.
- **Issues.**
  - Aucun écart certifié sur toute la grille : H_B est falsifiée sur la grille. On arrête, et la conclusion « le connu suffit » est utile.
  - Un écart certifié : H_A est falsifiée. On lance alors une conjecture de forme close, ajustée sur les valeurs exactes à la manière de la Ramanujan Machine, puis une tentative de preuve, puis la relecture.
- **Différence avec le publié** (à vérifier par P1). La littérature de fusion vise d'abord la *validité* sous dépendance arbitraire. Ici l'objet est la *puissance* quand c'est le saboteur qui choisit la dépendance.

### P3. Paires de mondes indiscernables pour sonde linéaire : recherche évolutionnaire de constructions

- **Idée.** La « sonde qui ne lit que l'indication » et le lemme d'impossibilité (RAPPORTÉ) se lisent à l'envers : on cherche deux lois d'activations, honnête et saboteur, dont tous les classifieurs linéaires d'une classe donnée ont un avantage ≤ ε. La sortie de la tâche doit pourtant différer d'au moins δ, la quantité que la sonde est censée détecter.
- **Évaluateur.** Score = δ − λ · (meilleur avantage linéaire), calculé exactement sur des lois discrètes de petite dimension.
- **Premier pas.** Une boucle de type FunSearch, où le LLM écrit des générateurs de paires de lois, avec cet évaluateur exact.
- **Coût.** Quelques centaines de dollars d'appels, plus du CPU (illustratif).
- **Duel.**
  - H_A : les meilleures paires trouvées sont toutes des instances d'une famille connue (appariement des moments d'ordre ≤ 2, qui rend toute sonde linéaire aveugle par construction).
  - H_B : une paire a un ratio δ/ε qu'aucun appariement de moments de cette famille n'atteint sous les mêmes contraintes.
- **Contrôle négatif.** Avec les moments d'ordre 1 et 2 libres, la recherche doit trouver une paire triviale. Sinon l'évaluateur est cassé.
- **Issues.**
  - Tout se ramène à l'appariement de moments : H_B est falsifiée. La conclusion « une sonde linéaire est aveugle exactement à ce que les deux premiers moments cachent » est probablement déjà connue (P1).
  - Une paire hors famille : H_A est falsifiée, et la paire devient un contre-exemple concret, vérifiable par simple calcul.
- **Différence avec le publié.** Goldwasser et al. donnent une indiscernabilité *calculatoire* sous hypothèse cryptographique. Ici, ce sont des constantes explicites en dimension finie, sans hypothèse calculatoire (HYPOTHÈSE sur l'absence d'antériorité).

### P4. Banc de dérive d'énoncé, avant tout Lean

- **Premier pas.** Prendre les quarante énoncés connus du juge de nouveauté (RAPPORTÉ) et les cinq énoncés de P1. Fabriquer des mutants : quantificateur inversé, inégalité large ou stricte, hypothèse d'indépendance retirée, horizon fini ou infini.
- **Coût.** Une journée d'ingénierie, plus quelques dizaines de dollars (illustratif).
- **Duel.**
  - H_A : la retraduction automatique (énoncé formel → langue → comparaison par un juge LLM) détecte les mutants aussi bien qu'un humain.
  - H_B : elle en rate une part que l'humain voit.
- **Métrique.** Taux de détection des mutants et taux de fausses alertes sur les formalisations correctes appariées.
- **Seuil.** Fixé avant le test (je propose « rate au plus 1 mutant sur 20 », illustratif).
- **Contrôle négatif.** Les formalisations correctes elles-mêmes : un juge qui signale tout passe le test de détection et échoue sur ce contrôle.
- **Issues.**
  - Le seuil est tenu : H_B est falsifiée et la relecture humaine des énoncés peut être allégée.
  - Le seuil n'est pas tenu : H_A est falsifiée, et chaque énoncé exige une relecture humaine. Le goulet du programme est alors identifié et chiffré.

### P5. Archive des morts comme banque de contre-exemples publiable

- **Premier pas.** Extraire de la mémoire des tentatives chaque mort accompagnée de son monde tueur, normalisée en couple (énoncé faux, contre-exemple).
- **Coût.** Faible (illustratif).
- **Duel.**
  - H_A : les morts sont redondantes (peu de mondes tueurs distincts).
  - H_B : elles couvrent des modes d'échec distincts, réutilisables comme tests pour d'autres programmes.
- **Métrique.** Nombre de classes de contre-exemples non isomorphes. Le seuil est à fixer avant extraction ; je n'en ai pas de fondé.
- **Contrôle négatif.** Une archive mélangée au hasard ; il faut alors une notion de classe définie a priori.
- **Issues.**
  - Peu de classes : H_B est falsifiée, et les proposeurs tournent en rond (diagnostic utile).
  - Beaucoup de classes : H_A est falsifiée, et l'archive devient un artefact public.
- **Différence avec le publié.** Les bancs publics stockent des preuves ou des énoncés, rarement des énoncés faux plausibles d'un domaine appliqué (HYPOTHÈSE).

### Temps, effort humain et chance

Ce qui suit est une HYPOTHÈSE, inférée des cas publiés cités.
- Dans chacun de ces cas, des experts ont choisi le problème et l'évaluateur, sur des mois, et beaucoup de résultats sont des améliorations marginales.
- Avec quelques centaines de dollars par course et une relecture rare, l'issue la plus probable d'une course est : zéro théorème nouveau, plus quelques énoncés bien posés, plus la carte de ce qui est déjà connu. Je ne sais pas estimer la probabilité d'une découverte réelle.
- P2 et P3 sont les plus susceptibles de produire un objet nouveau, parce qu'elles sont de type ∃ et mécaniquement vérifiables. Même alors, prouver la forme générale demande un humain compétent, sur une durée que je ne sais pas chiffrer.

---

## (c) Mesure minimale de chaque instrument nommé

| Instrument | Cas positifs | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Vérificateur formel (harnais Lean) | Preuves contaminées plantées : `sorry`, axiome ajouté, énoncé muté (P4). Taux de détection exigé : toutes. | Preuves correctes des mêmes énoncés : zéro rejet | Une recherche textuelle de `sorry` et `axiom` : le harnais doit attraper ce qu'elle rate (mutation d'énoncé) |
| Preuve rejouable (certificats LP et SAT) | Certificats corrompus d'un bit ou d'un coefficient | Certificats valides | Revérification en flottant : le vérificateur exact doit rejeter ce que le flottant accepte |
| Recherche d'antériorité | Énoncés connus du domaine, renommés et paraphrasés (section 1.6) : taux de « connu » | Énoncés synthétiques de même forme mais vraiment neufs (paramètres inédits) : taux de faux « connu » | Recherche par mots-clés et recherche par plongements sur arXiv et zbMATH |
| Relecture par mathématiciens | Mutants plantés (P4) parmi des énoncés corrects, en aveugle | Énoncés corrects | Juge par retraduction automatique (P4) |
| Réplication | Même pipeline, autre graine, autre lignée : reproduit-on le même objet ou la même classe ? | Course à évaluateur aléatoire, qui ne doit rien « reproduire » | Simple réexécution déterministe |
| Évaluateur FunSearch (P2, P3) | Optimum connu planté (cas indépendant) : doit être retrouvé | Évaluateur permuté au hasard : aucune amélioration attendue | Recherche aléatoire au même budget : la boucle LLM doit la battre, sinon le LLM n'apporte rien |

Aucun seuil numérique ne vient des FAITS. Ceux que je proposerais sont illustratifs et doivent être fixés avant la course.

---

## (d) Ancrage matériel

- **Modèles ouverts.**
  - Proposeurs généralistes à poids ouverts (familles Qwen, DeepSeek, Llama ; versions à choisir selon la licence).
  - Prouveurs Lean à poids ouverts : DeepSeek-Prover-V2, Goedel-Prover (je crois les poids publiés ; à vérifier).
  - Une lignée doit rester un modèle sans entraînement Lean, comme contrôle.
- **Outils.**
  - Lean 4 et Mathlib épinglés, sur la machine isolée (RAPPORTÉ).
  - Solveur LP exact ou rationnel.
  - Solveurs SAT CaDiCaL et kissat, avec vérification des preuves DRAT et LRAT (drat-trim, cake_lpr).
  - Python et SymPy pour la « suite bon marché » (RAPPORTÉ).
- **Calcul et coût** (illustratif) :
  - P1 et P5 : surtout du temps humain ;
  - P2 : CPU, dizaines de dollars par grille ;
  - P3 : quelques centaines de dollars d'appels par course, compatible avec le budget déclaré (RAPPORTÉ) ;
  - P4 : quelques dizaines de dollars ;
  - recherche de preuve Lean : de quelques à quelques dizaines d'heures de GPU par énoncé si l'on auto-héberge un prouveur de taille moyenne. Je ne sais pas le chiffrer mieux sans connaître la taille des énoncés.
- **Le coût dominant** n'est pas le calcul. Ce sont les heures d'expert pour P1, pour la relecture d'énoncés et pour la preuve générale. Les FAITS disent que ces heures sont rares (RAPPORTÉ).

FIN-DE-CELLULE