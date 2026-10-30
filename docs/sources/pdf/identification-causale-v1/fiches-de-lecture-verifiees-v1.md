# Fiches de lecture vérifiées — identification causale — v1

- Auteur : sous-agent Opus 5.5 neuf (canal `canal/conv-audit-n04`), sans part au brouillon 1 ni à la réponse 6.
- Date : 2026-10-30, 23:20 heure UTC (lecture commencée à 23:14 UTC).
- Règle appliquée : R7. Chaque énoncé renvoie à une page du PDF empreinté ; « p. X » = page du fichier PDF ; « art. Y » = numéro imprimé de l'article quand il diffère. Tout ce qui n'a pas été lu sur la page est marqué **SUPPOSÉ**.
- Méthode de lecture : texte extrait page par page (`pdftotext -f N -l N`), contrôle visuel de l'image de page par le lecteur de PDF quand l'extraction était douteuse (Lippe p. 6, figure superposée au texte ; Campos p. 12, signes moins perdus à l'extraction : les coefficients du tableau 4 sont **négatifs** sur l'image). Les neuf PDF ont un texte extractible ; aucun n'a demandé de reconnaissance optique.
- Non lu : les annexes en ligne citées par les articles (absentes des PDF), sauf mention ; rien sous `donnees/` ; aucun accès réseau.

## Empreintes vérifiées (`sha256sum -c *.sha256` : les neuf « OK »)

| Fichier | Empreinte SHA-256 |
|---|---|
| azoulay-2010-superstar-extinction-nber-w14577-rev2009.pdf | `911c058a52b69eaf3fc3d8a83df7e22e7e6ee2ec555b3b4c90184f2e5a693354` |
| borjas-2012-collapse-soviet-union-mathematicians-nber-w17800.pdf | `902375cd8e0bd096831e1a7982441f99b611a7cd16fdb3b2f6a329194c55bd22` |
| campos-2018-lost-in-the-storm-hurricane-isaac.pdf | `94d1c0ecc622380f42f4311653e08f71b6372a8dd3163b23e22d1006bc660d50` |
| iaria-2018-frontier-knowledge-collapse-international-science.pdf | `6d32d421de40452959ca77cd660665e44bc8e3c9792351ca7dcf2ac595489a89` |
| khemakhem-2020-vae-nonlinear-ica-arxiv-v4.pdf | `ea4bc2b1bf46b94b0f7fa7121b3de51f691c8386e0d0844f5f5c50ef31677629` |
| lippe-2022-citris-causal-identifiability-arxiv-v3.pdf | `346a5facb15c02a5754b33a191e85bfdc1efdc8f89ff5c62148e578c7650d1c2` |
| locatello-2019-challenging-assumptions-disentangled-arxiv-v4.pdf | `7d92c1b51c604a055086e63d2ae4d439f72341aac24e840b8e0823f376ae721f` |
| reisach-2021-beware-simulated-dag-arxiv-v3.pdf | `04aa0fc7d67449cc584c7c89845445f0b7b4fd90a21406594400b27e983c44e5` |
| scholkopf-2021-toward-causal-representation-learning.pdf | `219e7a79ac8078cfa23694d24571fdbcc8b5c7e29f6e51b3d93995399eb33b27` |

---

## 1. Reisach, Seiler et Weichwald 2021 — triabilité par la variance

**Référence (telle que le PDF la donne, p. 1).** Alexander G. Reisach, Christof Seiler, Sebastian Weichwald, « Beware of the Simulated DAG! Causal Discovery Benchmarks May Be Easy To Game », 35th Conference on Neural Information Processing Systems (NeurIPS 2021) ; arXiv:2102.13647v3 [stat.ML], 10 novembre 2021. Empreinte `04aa0fc7…c44e5`. Pages du PDF = pages imprimées.

**Énoncés vérifiés.**
1. (p. 1, résumé) Dans les modèles à bruit additif simulés « génériquement », la variance marginale tend à croître le long de l'ordre causal ; les auteurs introduisent la « varsortability » (triabilité par la variance) comme mesure de l'accord entre l'ordre des variances croissantes et l'ordre causal.
2. (p. 4, § 3.1) Définition : la triabilité par la variance v est la fraction des chemins orientés qui partent d'un nœud de variance strictement plus faible que celle du nœud d'arrivée (égalité comptée 1/2), v ∈ [0, 1] ; v = 1 si chaque nœud a une variance strictement supérieure à celle de tous ses ancêtres.
3. (p. 5, § 3.2) Si v = 1, la structure est identifiable : trier par variance croissante puis régresser chaque nœud sur ses prédécesseurs avec une régression parcimonieuse. Les mêmes pages listent trois défauts de toute identifiabilité fondée sur l'échelle : hypothèse difficile à vérifier sur données réelles ; tout redimensionnement inconnu la casse ; même avec une unité commune, l'unité peut ne pas refléter « l'échelle causale » (exemple du joueur de fléchettes, où l'effet a moins de variance que la cause).
4. (p. 5, § 3.3) Avec des poids tirés uniformément dans (−2 ; −0,5) ∪ (0,5 ; 2) et des écarts-types de bruit dans (0,5 ; 2), une paire est triable par la variance avec probabilité au moins 2/3, et p > 0,93 si la cause est une racine ; (p. 6) empiriquement v moyen > 0,94 dans leurs graphes linéaires simulés et > 0,71 dans des modèles non linéaires courants.
5. (p. 7, § 3.5) « sortnregress » = (i) tri par variance marginale croissante ; (ii) régression de chaque nœud sur tous ses prédécesseurs par lasso, **sélection par critère d'information bayésien** (pas par validation croisée).
6. (p. 7, tableau 1 ; p. 8, figure 1) Plan de simulation : 10 répétitions ; graphes Erdős-Rényi-2, sans échelle-2 et -4 ; d ∈ {10, 30, 50} ; n = 1 000 ; bruits exponentiel, gaussien, Gumbel. Sur données standardisées, v = 1/2 et les variances ne portent plus d'information. Sur données brutes, sortnregress égale NOTEARS et GOLEM.
7. (p. 8–9, § 4.3) NOTEARS, MSE-GDS et GOLEM-EV (fondés sur l'erreur quadratique moyenne) sont excellents sur données brutes et nettement pires sur données standardisées ; GOLEM-NV est aussi sensible à l'échelle mais s'améliore après standardisation. (p. 6, § 3.4) PC, FGES et DirectLiNGAM ne devraient pas dépendre de l'échelle (critère équivalent en score ou tests invariants d'échelle) ; (p. 2) ICA-LiNGAM, lui, est sensible au redimensionnement, ce qui a motivé DirectLiNGAM.
8. (p. 9, § 4.3) Sur le jeu réel de signalisation protéique de Sachs, triabilité moyenne 0,57 (écart-type 0,01 par rééchantillonnage), proche du hasard (0,5) ; le motif observé sur données simulées n'y apparaît pas.
9. (p. 9, § 5.1) La standardisation **ne suffit pas** : une chaîne simulée à forte triabilité laisse un motif de covariance (coefficients de régression standardisés, c'est-à-dire corrélations successives, croissants le long de l'ordre causal) qui permet d'orienter la chaîne au-dessus du hasard sur données brutes, standardisées et « harmonisées en échelle ».
10. (p. 10, tableau 2) En non linéaire (processus gaussiens additifs, 1 000 observations), le simple tri par variance bat le tri aléatoire en distance d'intervention structurelle, par exemple 1,9 ± 2,28 contre 22,3 ± 13,14 (graphes sans échelle-1, v moyen 0,95).

**Conditions.** Résultats théoriques limités aux modèles linéaires à bruit additif acycliques, observations indépendantes et identiquement distribuées, sans confondeur caché (p. 3, § 2.1 et 2.2). L'identifiabilité « par l'échelle » (Peters et Bühlmann 2014 ; Park 2020, cités p. 3) exige des variances de bruit égales, connues ou croissantes le long de l'ordre causal, et donc l'échelle vraie.

**Limites dites par les auteurs (p. 10, § 6).** Théorie limitée au linéaire ; la conjecture sur le rôle des premiers pas de gradient reste ouverte ; le jeu de l'échelle sur données standardisées et non linéaires demande d'autres travaux ; seule une partie des algorithmes est étudiée ; un banc synthétique peut ne rien dire des performances sur données réelles.

**Portée pour notre épreuve.** Le témoin T2 et le seuil S12 sont justifiés, mais à trois corrections près : (a) « sortnregress » de Reisach sélectionne par critère d'information bayésien, alors que le brouillon 1 écrit « pénalité par validation croisée » (§ M T2) : il faut soit suivre le papier, soit renommer la variante ; (b) la standardisation n'efface pas tout l'artefact (énoncé 9) : S12, qui lit « chute en échelle standardisée » comme diagnostic suffisant, doit aussi mesurer la croissance des coefficients de détermination ou des corrélations le long du sous-graphe planté ; (c) la sensibilité à l'échelle dépend de la variante de LiNGAM (DirectLiNGAM invariant, ICA-LiNGAM non) : M3 doit nommer sa variante, sinon le prédicat ART(M3) n'a pas de prédiction écrite. NOTEARS (nommé dans la mission mais absent du brouillon 1) est la méthode la plus exposée : si elle entre, sa qualification doit être conditionnée à l'échelle standardisée. La « R²-sortabilité » de 2023 citée par le brouillon n'est pas dans ce PDF : elle reste SUPPOSÉE.

---

## 2. Locatello et collègues 2019 — impossibilité sans biais inductif

**Référence (p. 1).** Francesco Locatello, Stefan Bauer, Mario Lucic, Gunnar Rätsch, Sylvain Gelly, Bernhard Schölkopf, Olivier Bachem, « Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations », Proceedings of the 36th International Conference on Machine Learning, Long Beach, PMLR 97, 2019 ; arXiv:1811.12359v4 [cs.LG], 18 juin 2019. Empreinte `7d92c1b5…d721f`.

**Énoncés vérifiés.**
1. (p. 1, résumé ; p. 3, théorème 1) Le démêlage non supervisé des représentations est « fondamentalement impossible » sans biais inductifs **à la fois** sur les modèles et sur les données.
2. (p. 3, théorème 1, texte exact) Pour d > 1 et z de densité factorisée p(z) = ∏ p(z_i), il existe une famille infinie de bijections f du support dans lui-même, dont toutes les dérivées croisées sont non nulles presque partout (z et f(z) « complètement intriqués »), et qui conservent la loi : P(z ≤ u) = P(f(z) ≤ u).
3. (p. 3) Conséquence : deux modèles génératifs, l'un démêlé, l'autre complètement intriqué, donnent la même loi des observations x ; une méthode qui ne voit que x ne peut les distinguer. Le résultat vaut aussi pour des lois non invariantes par rotation (lois uniformes multivariées) ; la note 3 précise qu'il ne s'applique qu'aux a priori factorisés (extension aux a priori non factorisés seulement « attendue »).
4. (p. 2, § 2) Rappel : pour l'analyse en composantes indépendantes non linéaire, les sources ne sont en général pas identifiables (Hyvärinen et Pajunen 1999).
5. (p. 1 ; p. 4) Étude : plus de 12 000 modèles, six méthodes, six métriques, sept jeux de données ; 50 graines par configuration ; six forces de régularisation fixées d'avance.
6. (p. 5–6, § 5.3, figure 3) La graine aléatoire et les hyperparamètres comptent plus que le choix de la fonction objectif ; « un bon tirage avec un mauvais hyperparamètre peut battre un mauvais tirage avec un bon ». (p. 6) La fonction objectif seule explique 37 % de la variance des scores ; objectif × force de régularisation, 59 % ; le reste est dû à la graine.
7. (p. 6–7, § 5.4, tableau 1) Sélection de modèle non supervisée non résolue : la stratégie par transfert bat ou égale une sélection aléatoire dans 80,7 % des essais (même métrique, même jeu, autre graine), 59,3 % (même métrique, autre jeu), 54,9 % (autre métrique, autre jeu), sur 10 000 tirages.
8. (p. 4–5, § 5.1) Les méthodes rendent peu corrélées les dimensions de la représentation **échantillonnée**, mais la représentation **moyenne** (celle qu'on utilise) voit sa corrélation totale croître avec la régularisation.
9. (p. 8, § 6) Pistes recommandées : supervision faible, interactions, et surtout structure temporelle, « au vu des résultats d'identifiabilité récents en analyse en composantes indépendantes non linéaire (Hyvärinen et Morioka 2016) ».

**Conditions.** Données indépendantes et identiquement distribuées, aucune observation des facteurs (p. 3, « we only observe samples from P(x) »), a priori factorisé.

**Limites dites (p. 16, annexe E).** Images seulement, surtout synthétiques ; facteurs discrets, indépendants, uniformes, **sans variable confondante** ; une seule famille d'architectures convolutives ; seuls les poids de régularisation varient (ni taille latente, ni optimiseur, ni taille de lot).

**Portée pour notre épreuve.** Fonde M5 comme contre-exemple : sans variable auxiliaire, la non-identification de Z est le résultat attendu, et l'instabilité entre graines est un constat empirique, pas le théorème. Deux conséquences pour le brouillon : (a) deux graines (critère STAB) sont peu au regard des 50 graines du papier : la stabilité mesurée sera bruitée, et une stabilité haute de M5 ne prouverait pas l'identification ; (b) le classement « sans vérité » du facteur apparié par son coefficient sur g(Y⁺) introduit une supervision par la sortie : le contraste M4 − M5 n'est plus strictement « non supervisé contre variable auxiliaire », ce qu'il faut écrire. Pour la réponse 6 : le théorème porte sur des observations indépendantes, sans temps ni environnements ; il ne dit rien contre les méthodes qui exploitent une structure (le papier le dit lui-même, p. 8).

---

## 3. Khemakhem, Kingma, Monti et Hyvärinen 2020 — variable auxiliaire (iVAE)

**Référence (p. 1).** Ilyes Khemakhem, Diederik P. Kingma, Ricardo Pio Monti, Aapo Hyvärinen, « Variational Autoencoders and Nonlinear ICA: A Unifying Framework », Proceedings of the 23rd International Conference on Artificial Intelligence and Statistics (AISTATS) 2020, Palerme, PMLR 108 ; arXiv:1907.04809v4 [stat.ML], 21 décembre 2020 ; version « légèrement mise à jour » avec corrigendum (p. 1, note ; p. 9). Empreinte `ea4bc2b1…77629`.

**Énoncés vérifiés.**
1. (p. 3, § 2.3 ; p. 18–19, annexe D) Tout modèle à variables latentes dont l'a priori p(z) est **inconditionnel** n'est pas identifiable (par exemple une rotation d'un a priori gaussien sphérique, absorbée par la première couche du décodeur, laisse p(x) inchangée).
2. (p. 3, § 3.1, éq. 5–7) Modèle : x = f(z) + ε, ε indépendant de z ; f injective, par ailleurs non linéaire quelconque ; a priori **conditionnellement factorisé** sachant une variable observée u, chaque z_i suivant une loi de famille exponentielle dont les paramètres λ_i(u) dépendent de u ; k (dimension des statistiques suffisantes) fixé.
3. (p. 5, théorème 1, hypothèses exactes) (i) l'ensemble des zéros de la fonction caractéristique du bruit est de mesure nulle ; (ii) f injective ; (iii) statistiques suffisantes dérivables presque partout et linéairement indépendantes sur tout ensemble de mesure positive ; (iv) il existe **nk + 1 points distincts** u_0, …, u_nk tels que la matrice L = (λ(u_1) − λ(u_0), …, λ(u_nk) − λ(u_0)), de taille nk × nk, soit inversible. Alors (f, T, λ) est identifiable à une transformation linéaire inversible A près (relation ∼A).
4. (p. 6, théorèmes 2 et 3) La matrice A se réduit à une permutation (relation ∼P) si k ≥ 2 avec statistiques deux fois dérivables et f à dérivées croisées secondes (théorème 2), ou si k = 1 avec statistiques non monotones et f à dérivées partielles continues (théorème 3) ; les latentes estimées sont alors une permutation des vraies, à une transformation élément par élément près.
5. (p. 6, proposition 1) Contre-cas : si k = 1, T_i(z_i) = z_i et base de mesure constante ou gaussienne (seule la **moyenne** varie avec u, lois gaussiennes ou exponentielles), A **ne peut pas** être réduite à une permutation.
6. (p. 15, annexe B.2.3) L'hypothèse (iv) tient presque sûrement si les λ_{i,j}(u) sont « générés aléatoirement et indépendamment » ; exemple n = 2, k = 1, variances modulées par u et u².
7. (p. 6, théorème 4) Cohérence : si la famille variationnelle contient le vrai a posteriori et qu'on maximise la borne inférieure en θ et φ, l'autoencodeur variationnel apprend les vrais paramètres à ∼ près, à la limite d'une infinité de données.
8. (p. 6–7, § 5.1, figure 2) Simulation : sources gaussiennes non stationnaires en M segments de L points, u = indice de segment, moyenne et variance modulées (k = 2) ; mélange par perceptron multicouche plus petit bruit gaussien ; avec M = 40, L = 1 000, d = n = 5, l'iVAE dépasse 0,95 de coefficient de corrélation moyen (appariement par affectation linéaire), alors que l'autoencodeur variationnel ordinaire, β-VAE et β-TC-VAE échouent. (p. 7, figure 3a) Le nombre de segments varie de 10 à 50.
9. (p. 9, corrigendum ; p. 18, annexe C) L'identifiabilité **n'est plus revendiquée pour des observations discrètes** : la preuve était fausse ; f ne peut plus être injective pour des observations discrètes.

**Conditions (le plus important).** Identification seulement : (a) avec u observé ; (b) si **toutes** les n latentes sont conditionnellement indépendantes sachant u et suivent la famille exponentielle posée ; (c) si u prend assez de valeurs (nk + 1) avec des variations linéairement indépendantes des paramètres ; (d) mélange injectif ; (e) observations continues ; (f) à permutation et transformation élément par élément près, et à transformation linéaire près si seule la moyenne varie (k = 1, gaussien). Résultat asymptotique.

**Limites dites.** Corrigendum sur le discret (p. 9) ; proposition 1 (p. 6). Pas d'autre section de limites dans le PDF.

**Portée pour notre épreuve.** Le volet B du brouillon sort des hypothèses du théorème, et le préenregistrement doit le dire : (a) les sources du mélange sont (Z, S, D, A, g(Y⁰)) (brouillon § S6), mais seule la loi de Z varie avec u ; S, D, A et g(Y⁰) sont des covariables réelles, dépendantes entre elles et non modélisées en famille exponentielle conditionnelle : l'hypothèse (b) est violée pour quatre sources sur cinq, et le théorème ne garantit rien, même pour Z seul (SUPPOSÉ : aucun résultat partiel de ce type n'est dans ce PDF) ; (b) avec n = 5 et k = 2 (moyenne et variance modulées en Bv), il faut au moins 11 valeurs distinctes de u (environnement × bloc de cinq ans) : à vérifier sur la moisson avant scellement ; (c) S et D sont des comptes : sources discrètes, hors du cadre des densités (SUPPOSÉ quant à l'effet) ; (d) la dimension apprise d = 6 diffère de n = 5 ; (e) HR-M4 (« corrélation ≥ 0,70 dans la plupart des mondes Bv ») teste donc une robustesse hors théorème, pas le théorème. Correction factuelle : la relecture de la réponse 6 (RL6, ligne Khemakhem) écrit « au moins 2k+1 valeurs de la variable auxiliaire » ; le PDF dit **nk + 1** (p. 5). La mesure r_Z du brouillon (maximum par source) diffère du coefficient de corrélation moyen par affectation du papier (p. 7) : à justifier ou aligner.

---

## 4. Lippe et collègues 2022 — CITRIS, cibles d'intervention observées

**Référence (p. 1).** Phillip Lippe, Sara Magliacane, Sindy Löwe, Yuki M. Asano, Taco Cohen, Efstratios Gavves, « CITRIS: Causal Identifiability from Temporal Intervened Sequences », Proceedings of the 39th International Conference on Machine Learning, Baltimore, PMLR 162, 2022 ; arXiv:2202.03169v3 [cs.LG], 15 juin 2022. Empreinte `346a5fac…0d1c2`.

**Énoncés vérifiés.**
1. (p. 2, § 2) Processus latent supposé : réseau bayésien dynamique sur K variables causales (scalaires ou vectorielles), **markovien d'ordre un, stationnaire, sans effet instantané** ; bruits mutuellement indépendants ; graphe invariant dans le temps.
2. (p. 2) Interventions souples (le cas dur do(·) est un cas particulier) ; les cibles peuvent être confondues entre elles par une variable de régime non observée.
3. (p. 3, § 3.1) Fonction d'observation h(C, bruit) = X **bijective** ; on suppose l'accès aux **cibles** d'intervention I^t ∈ {0,1}^K à chaque pas, **pas aux valeurs**.
4. (p. 3, proposition 3.1) Si deux facteurs n'ont été intervenus que conjointement, ou jamais, il existe un graphe où ils ne peuvent pas être identifiés à partir de X et I (exemple : position gaussienne stationnaire en deux dimensions, toute paire d'axes orthogonaux convient).
5. (p. 4, définition 3.2) Ce qui est identifiable est la « variable causale minimale » : la part d'un facteur qui dépend strictement de son intervention ; la part invariante sous intervention n'est pas attribuable.
6. (p. 5, théorème 3.3) Sous maximisation de la vraisemblance p(x^{t+1} | x^t, I^{t+1}) et du contenu d'information, avec assez de dimensions latentes, le modèle isole la variable causale minimale de C_i si C_i^{t+1} n'est pas indépendant de I_i^{t+1} sachant C^t et I_j^{t+1} (j ≠ i) ; preuve en annexe B, qui repose sur le fait qu'aucune cible n'est fonction déterministe des autres (condition suffisante : interventions indépendantes, ou à cible unique avec données d'observation). Tout le reste va dans un groupe résiduel z_ψ0.
7. (p. 6, § 5, vérifié sur l'image de page) Les travaux voisins (Lachapelle et collègues 2022 ; Yao et collègues 2022) n'exploitent pas la connaissance des cibles et exigent donc « des hypothèses supplémentaires de variation suffisante ».
8. (p. 7, § 6.1) Banc Temporal-Causal3DIdent : sept facteurs, interventions parfaites tirées selon Bernoulli(0,1) ; Interventional Pong : le score, jamais intervenu, doit aller dans z_ψ0.
9. (p. 8, tableau 1) Teapot : coefficient de détermination « diagonal » 0,96 (CITRIS-VAE) et 0,98 (CITRIS-NF), contre 0,65 (iVAE* à 9 dimensions) et 0,65 (SlowVAE) ; Spearman diagonal 0,95 et 0,97 contre 0,65 et 0,62 ; écarts-types sur 3 graines en annexe C.1 (non lue). (p. 9, tableau 3) Pong : iVAE* 0,91, CITRIS-VAE 0,99 ; (p. 9) iVAE* « instable selon les graines » sur Pong.
10. (p. 9, tableau 2) Généralisation à deux formes jamais vues : coefficient de détermination diagonal 0,94 (contre 0,98 sur les formes vues).

**Conditions.** Cibles d'intervention observées à chaque pas, non jointes en permanence, non déterministes les unes des autres ; markovien d'ordre un, stationnaire, sans effet instantané ; observation bijective ; latentes en nombre suffisant ; résultat à l'optimum de vraisemblance.

**Limites dites.** Proposition 3.1 et minimalité (p. 3–4) ; seules les parties intervenues sont identifiées. Pas de section de limites ; la conclusion (p. 9) renvoie à l'apprentissage actif et aux simulateurs robotiques.

**Portée pour notre épreuve.** Confirme la relecture RL6-02 sur page : CITRIS est une méthode « interventions observées dans le temps », non « ordre temporel seul ». Sur OpenAlex, aucune cible d'intervention n'est observée, sauf la cause plantée C elle-même : CITRIS ne peut servir qu'en gradation 3 (nos courses, où la cible est connue) ou sur une plantation où C joue le rôle de cible observée ; il n'est pas une méthode d'observation pure. L'agrégation annuelle des citations crée probablement des effets instantanés (SUPPOSÉ), ce qui viole l'hypothèse « sans effet instantané ». Pour la réponse 6 : les causes jamais intervenues (comme le score de Pong) finissent dans le groupe résiduel, non identifiées.

---

## 5. Schölkopf et collègues 2021 — perspective sur l'apprentissage de représentations causales

**Référence (p. 1, art. 612).** Bernhard Schölkopf, Francesco Locatello, Stefan Bauer, Nan Rosemary Ke, Nal Kalchbrenner, Anirudh Goyal, Yoshua Bengio, « Toward Causal Representation Learning », Proceedings of the IEEE, vol. 109, n° 5, mai 2021, p. 612–634 ; identifiant numérique 10.1109/JPROC.2021.3058954 ; publié le 26 février 2021. Empreinte `219e7a79…b33b27`. Page imprimée = page du PDF + 611.

**Énoncés vérifiés.**
1. (p. 1, art. 612, titre et résumé) Article de **revue et de perspective** : il « passe en revue » des concepts et « propose » des axes ; ce n'est pas un article de théorèmes.
2. (p. 5, art. 616, § III.B) Principe de la cause commune de Reichenbach ; « sans hypothèses supplémentaires », on ne peut pas distinguer X → Y, X ← Y et X ← Z → Y à partir de données d'observation.
3. (p. 6, art. 617) Avec deux variables seulement, l'indépendance conditionnelle ne donne aucune empreinte (il en faut au moins trois) ; (p. 9, art. 620, note 7) les tests d'indépendance conditionnelle ne retrouvent la structure qu'à la classe d'équivalence de Markov près, sous fidélité.
4. (p. 4, art. 615, § II.D) Apprendre des relations causales « exige fréquemment » plusieurs environnements ou la capacité d'intervenir ; certaines méthodes supposent la suffisance causale (toutes les causes communes observées), d'autres non (note 4).
5. (p. 10, art. 621) Les modèles à bruit additif brisent la symétrie cause-effet sous des hypothèses de généricité, avec l'exception notable du cas linéaire gaussien.
6. (p. 8, art. 619) Principe des mécanismes causaux indépendants et hypothèse des **décalages parcimonieux de mécanismes** : « les petits changements de loi tendent à se manifester de façon parcimonieuse dans la factorisation causale » ; c'est une **hypothèse**, posée comme telle.
7. (p. 10, art. 621) Par cette hypothèse, des changements de loi (environnements, interventions, séries non stationnaires) « peuvent aider significativement » à identifier la structure.
8. (p. 12, art. 623) Retrouver les bruits exogènes est mal posé dans le cas indépendant et identiquement distribué ; Locatello et collègues [159] auraient montré que les décalages parcimonieux suffisent « avec des données d'entraînement convenables » ; ce qui peut être démêlé dépend des interventions observées.
9. (p. 13, art. 624, § VII) Défis listés : inférer des variables causales abstraites ; absence de consensus sur ce qui révèle une relation causale ; protocole apprentissage-test insuffisant, besoin de nouveaux bancs avec environnements et interventions ; manque d'algorithmes passant à l'échelle.

**Conditions.** Sans objet (pas de théorème propre) ; les résultats rappelés sont cités avec leurs références.

**Limites dites.** Voir énoncé 9.

**Portée pour notre épreuve.** Cadre conceptuel de H-SR, citable pour « l'identification exige des hypothèses ou des interventions » (p. 4–5, art. 615–616), non comme preuve d'identifiabilité. Confirme RL6 : écrire « Schölkopf 2021 identifie » est inexact ; l'emploi des environnements (sous-domaine × bloc d'années) dans M1 repose sur l'hypothèse de décalages parcimonieux, à écrire comme hypothèse non testable. Le résultat cité [159] n'est pas dans ce PDF (SUPPOSÉ).

---

## 6. Azoulay, Graff Zivin et Wang — disparition de « superstars »

**Référence (p. 1–2).** Pierre Azoulay, Joshua S. Graff Zivin, Jialan Wang, « Superstar Extinction », NBER Working Paper No. 14577, décembre 2008, **révisé juillet 2009** (JEL O3, O31, O43). Empreinte `911c058a…489a89` (le fichier est nommé « 2010 » ; le PDF est le document de travail, non l'article publié : ses pages ne valent pas pour la version de revue, SUPPOSÉE parue en 2010). Page imprimée = page du PDF − 2 (annexe en chiffres romains).

**Énoncés vérifiés.**
1. (p. 2, résumé ; p. 8, art. 6) 112 « superstars » des sciences de la vie morts prématurément **et de façon inattendue** ; 136 morts prévisibles exclues sur 248 ; critères : 67 ans ou moins, encore actifs.
2. (p. 10, art. 8, § 2.3) Le témoin implicite (coauteurs traités plus tôt ou plus tard) est rejeté pour deux menaces : tendances post-décès altérées (sous-estimation) et cycle de vie des collaborations (surestimation).
3. (p. 11, art. 9) Témoins appariés par appariement exact grossi, choisis pour : pas de tendances différentielles avant le décès ; même âge de carrière ; mêmes trajectoires ; collaborations équilibrées ; différence de différences.
4. (p. 11, art. 9) Menace d'interférence reconnue : les témoins peuvent être touchés (« no scientist is an island ») ; vérifiée en retirant les paires proches dans le réseau ; (p. 48, annexe vi) en gardant les chercheurs à au moins 3 degrés (75 % de l'échantillon), l'effet **augmente**.
5. (p. 15–16, art. 13–14) Modèle de Poisson à effets fixes de dyade, quasi-maximum de vraisemblance, effets d'année et 17 classes d'âge de carrière ; erreurs groupées par superstar ; sortie principale : publications pondérées par le facteur d'impact de la revue (pas de citations par article dans le texte principal).
6. (p. 28, art. 26, tableau III) Coefficient « après décès » : −0,092 (0,022) sans témoins, −0,086 (0,025) avec témoins, soit 8,79 % de baisse ; publications écrites sans la superstar : −0,057 (0,022) et −0,054 (0,024) ; 5 267 coauteurs traités, 10 128 avec témoins, 294 943 observations.
7. (p. 17, art. 15) L'effet croît, devient significatif **trois à quatre ans après** le décès, et ne se résorbe pas.
8. (p. 22, art. 20) Coauteurs du quartile supérieur de recouvrement de mots-clés : baisse de 12,2 % ; (p. 21, art. 19) la colocalisation ne fait pas de différence ; (p. 30, art. 28, tableau VII) l'effet tient aux superstars très citées (−0,082, p < 0,10), non aux très financées.
9. (p. 24, art. 22 ; p. 48) Test placebo (dates de décès fictives chez les témoins) : effet « précisément nul ».

**Conditions.** Décès inattendu, donc exogène et non anticipé ; tendances parallèles assurées par l'appariement ; pas d'interférence entre traités et témoins (testée) ; moyenne conditionnelle correctement spécifiée (p. 16, art. 14).

**Limites dites.** Coauteurs seulement, pas les non-coauteurs (p. 22, 23, art. 20, 21) ; base des facultés de médecine incomplète (p. 9, art. 7) ; pondération par revue, pas par article (p. 16, art. 14) ; aucune expérience ne donne le bénéfice reçu du vivant de la superstar (p. 25, art. 23) ; certaines versions du rôle de « gardien » non rejetées (p. 23, art. 21). Incohérence interne : le texte (p. 17, art. 15) attribue le chiffre 8,2 % à la « colonne 2b » alors que le tableau III le donne en colonne 1b.

**Portée pour notre épreuve.** Candidate de « vérité » pour la gradation 2 sur le **signe** (négatif) et le **délai** (3 à 4 ans) d'un retrait de nœud, avec un placebo publié ; mais le traitement (mort d'un nœud) n'est pas le « contact » C du brouillon et la sortie (publications individuelles pondérées) n'est pas l'œuvre-pont entre niches : le transport doit être écrit d'avance et la sortie remesurée dans OpenAlex. Le chiffre opposable est −0,086 (tableau III, colonne 1b), sur la version de travail de 2009.

---

## 7. Borjas et Doran 2012 — effondrement de l'Union soviétique et mathématiciens américains

**Référence (p. 1–2).** George J. Borjas, Kirk B. Doran, « The Collapse of the Soviet Union and the Productivity of American Mathematicians », NBER Working Paper No. 17800, février 2012 (JEL J61, O31). Empreinte `902375cd…bd22`. Page imprimée = page du PDF − 1. Version de revue non lue (SUPPOSÉE parue en 2012).

**Énoncés vérifiés.**
1. (p. 20, art. 19) 29 392 mathématiciens « principalement américains » et 12 224 soviétiques ; 1 051 émigrés après l'effondrement, dont 336 aux États-Unis ; (p. 55, art. 54) « près d'un dixième » de la population préexistante, environ 30 % installés aux États-Unis.
2. (p. 21, art. 20) Forte sélection positive des émigrés : avant 1992, 10 articles et 66 citations de plus que les restés ; après, 20 articles et 143 citations de plus que l'Américain moyen.
3. (p. 24–25, art. 23–24) Exposition = recouvrement entre la distribution par champ des articles d'avant 1990 de chaque Américain et celle des Soviétiques : coefficient de corrélation, indice d'intensité, indice de similarité (63 champs).
4. (p. 26, art. 25, éq. 3) Modèle : effets fixes individuels et d'année, quartique en expérience, terme (après 1992) × indice ; erreurs groupées par individu ; sorties : articles par an et citations ISI de ces articles.
5. (p. 27, art. 26) Hypothèse du groupe témoin : les champs dominés par les Américains ne profitaient pas des idées soviétiques — seules 5 % des références des 10 premiers champs américains vont vers des champs dominés par les Soviétiques.
6. (p. 76, art. 75, tableau III, panneau A) Coefficients (après 1992) × corrélation : −0,133 (0,036) article par an et −19,577 (1,576) citations ; × similarité : −1,523 (0,113) et −69,155 (4,645) ; 804 180 observations (articles).
7. (p. 28–29, art. 27–28) Lecture : passer de ρ = 0 à ρ = 1 retire 0,13 article par an, soit 2,2 articles sur 1992–2008 contre une moyenne de 6,8 : environ un tiers.
8. (p. 29, art. 28) Avant 1990, le groupe très exposé avait une **légère tendance à la hausse**, le moins exposé une légère tendance à la baisse (tendances non strictement parallèles, figure VIIa) ; chute « précipitée » après 1990.
9. (p. 30–31, art. 29–30, panneau D) L'effet reste négatif et significatif avec des effets fixes champ × année ; (p. 29, art. 28) effets de long terme au moins aussi grands que de court terme.
10. (p. 55–56, art. 54–55) La baisse des Américains est « comblée » par les émigrés ; aucune preuve d'agrandissement du « gâteau » mathématique.

**Conditions.** Choc exogène (1992) ; exposition fixée par la production d'avant 1990 ; absence de tendances propres aux champs « soviétiques » (testée par effets champ × année) ; groupe témoin non bénéficiaire.

**Limites dites.** Citations tronquées (p. 26–27, art. 25–26) ; plein crédit à chaque coauteur, imposé par les données (p. 26, note 31). Incohérences internes : la période de long terme est « 1978–1989 et 2000–2008 » dans le texte (p. 30, art. 29) mais « 1978–1991 et 2000–2008 » dans la note du tableau III (p. 76) ; une cellule du panneau D est imprimée « −2378 » (vraisemblablement −0,2378, SUPPOSÉ).

**Portée pour notre épreuve.** Candidate de « vérité » pour la gradation 2 au niveau des **champs** : un afflux massif d'idées et de producteurs dans des niches déterminées a un effet **négatif** sur les producteurs en place, ce qui contredit le pari naïf « plus de contacts, plus de fertilité » ; mais la sortie est individuelle (articles, citations), non l'œuvre-pont entre paires de niches, et les tendances préalables ne sont pas parfaitement parallèles (énoncé 8) : à écrire comme réserve si elle sert de vérité de signe.

---

## 8. Campos, Leon et McQuillin 2018 — conférence annulée par l'ouragan Isaac

**Référence (p. 1, art. 995).** Raquel Campos, Fernanda Leon, Ben McQuillin, « Lost in the Storm: The Academic Collaborations That Went Missing in Hurricane ISSAC » [sic, orthographe du titre imprimé], The Economic Journal, 128 (mai 2018), 995–1018 ; identifiant numérique 10.1111/ecoj.12566 ; accès ouvert. Empreinte `94d1c0ec…0d50`. Page imprimée = page du PDF + 994.

**Énoncés vérifiés.**
1. (p. 3, art. 997) Congrès 2012 de l'Association américaine de science politique annulé **moins de 48 heures** avant, programme déjà publié « bien avant toute genèse » du cyclone : affectation exogène des participants.
2. (p. 4, art. 998) Témoin : le congrès de l'Association de science politique du Midwest, de format presque identique, tenu en avril, donc non touché par l'annulation de 2012 ; différence de différences sur les éditions 2009–2012.
3. (p. 5, art. 999, tableau 1) 39 586 auteurs-congrès, 17 467 individus, 86 068 533 dyades prospectives ; les coauteurs d'un même papier présenté sont exclus.
4. (p. 12, art. 1006, tableau 4, signes lus sur l'image) Annulation : −0,0241 (0,0088) sur la probabilité de collaborer avec un autre participant (moyenne 0,1563), soit −2,4 points, environ −16 % ; avec un participant d'une autre institution −0,0219 (0,0083) ; même thème −0,0247 (0,0069) ; même institution −0,0085 (0,0064, non significatif) ; nouveau coauteur −0,0185 (0,0084).
5. (p. 17, art. 1011, note 21) Taux de réussite des dyades : 3 828 collaborations sur 86 068 533 (0,004 %) ; 0,016 % parmi les dyades du même thème.
6. (p. 16–17, art. 1010–1011, tableau 6, panneau c) Parmi les dyades qui copublient, l'annulation abaisse le rang de la revue de 5,03 places et le facteur d'impact de 0,19 écart-type ; −9,1 points de probabilité de revue du premier quartile.
7. (p. 9, art. 1003) Équilibre vérifié sur caractéristiques prédéterminées (tableau A4 de l'annexe en ligne, **non lu**, SUPPOSÉ quant au détail) ; boycott de 2012 (1 109 pétitionnaires, dont 30 inscrits) sans report vers le témoin (note 13).
8. (p. 21, art. 1015, tableau 9) Coefficient de regroupement (« clustering ») des réseaux de coauteurs plus élevé après annulation : +0,0056 (p = 0,107) ; +0,0211 (p = 0,040) hors auteurs des deux congrès : les congrès « dé-regroupent » le réseau.
9. (p. 13–14, art. 1007–1008, tableau 5) Effets sur la production totale non significatifs (substitution de coauteurs), sauf « nouveaux coauteurs venus du congrès ».

**Conditions.** Calendrier exogène ; tendances parallèles entre séries de congrès (testées sur observables) ; témoin non contaminé (antériorité d'avril) ; canal du marché du travail discuté et jugé faible (p. 14–15, art. 1008–1009).

**Limites dites.** Le programme inclut des coauteurs non présents (p. 4, art. 998) ; appariement par nom avec ambiguïtés vérifiées à la main (p. 6, art. 1000) ; exclusion des collaborations déjà engagées (p. 6, art. 1000) ; égalité des coefficients entre sous-échantillons non rejetée (p. 18, art. 1012) ; une seule discipline.

**Portée pour notre épreuve.** La plus proche du « contact » C du brouillon : une rencontre retirée au hasard, mesurée au niveau des **paires**, avec un effet surtout sur les paires du même thème mais d'institutions différentes ; c'est la meilleure candidate pour la vérité de signe et d'ordre de grandeur d'un effet de contact en gradation 2. Mais la sortie est la coécriture, non la citation-pont, et le taux de base dyadique est minuscule (0,004 %) : une transposition aux œuvres-ponts d'OpenAlex demande une puissance écrite d'avance.

---

## 9. Iaria, Schwarz et Waldinger 2018 — Première Guerre mondiale et boycott

**Référence (p. 1, art. 927).** Alessandro Iaria, Carlo Schwarz, Fabian Waldinger, « Frontier Knowledge and Scientific Production: Evidence from the Collapse of International Science », The Quarterly Journal of Economics (2018), 927–991, identifiant numérique 10.1093/qje/qjx046, publication anticipée du 15 janvier 2018 ; accès ouvert. Empreinte `6d32d421…9a89`. Page imprimée = page du PDF + 926.

**Énoncés vérifiés.**
1. (p. 3, art. 929) Données : plus de 60 000 notices de professeurs (Minerva), recensements de 1900 et 1914 ; toutes les publications et références de 160 revues de 1900 à 1930 ; nominations au prix Nobel 1905–1945 ; plus de 2,5 millions de brevets américains.
2. (p. 22, art. 948 ; p. 23, art. 949, tableau IV) Modèle à effets fixes par article citant ; après 1914, la part des références vers la recherche « hors du camp » baisse de 0,22 par rapport à la part nationale (−0,222, significatif à 1 %), soit environ −85 % de la part d'avant-guerre.
3. (p. 3, art. 929) Les citations internationales vers la recherche **d'avant-guerre** ne baissent pas de façon disproportionnée : la baisse vient de l'ignorance des travaux récents, non d'un refus politique de citer.
4. (p. 4, art. 930) Similarité des titres (analyse sémantique latente) vers les papiers hors du camp : −0,5 écart-type par rapport aux papiers nationaux ; (p. 35, art. 961) retour aux niveaux d'avant-guerre seulement vers 1930 ; résultat presque inchangé sans la chimie.
5. (p. 36, art. 962) Exposition = parts de citations d'avant-guerre (1905–1913), au niveau champ × pays, vers la recherche de pointe nationale, du camp ou hors du camp ; exemple : biochimistes américains 32 % hors du camp, biologistes américains 6 %.
6. (p. 38–39, art. 964–965, éq. 3) Différence de différences généralisée : effets fixes de chercheur et d'année, contrôle de la dépendance à la recherche ordinaire, profils âge × champ ; 8 734 chercheurs en poste en 1914, 227 084 observations ; erreurs groupées par champ × pays.
7. (p. 40, art. 966, tableau VIII) Dépendance à la pointe hors du camp × après 1914 : −1,727 (0,638) au seuil du 1 % supérieur, −0,784 (0,282) au 3 %, −0,380 (0,220) au 5 % ; dans le camp : −0,827, −0,363, −0,152, non significatifs. Lecture : biochimistes américains −0,1 écart-type, environ −33 % d'articles par an.
8. (p. 41, art. 967) Pas de tendance préalable défavorable : les chercheurs exposés **progressaient** relativement jusqu'en 1913 (sous-estimation possible).
9. (p. 43, art. 969) Résultat inchangé avec effets fixes camp × année, champ × année, camp × champ × année ; différence hors du camp contre dans le camp : p = 0,136 (1 %), 0,055 (3 %), 0,124 (5 %) ; (p. 5, art. 931) robustesse aux décès (plus de 6 500 nécrologies), à l'exclusion des chimistes et aux seules revues du camp.

**Conditions.** Choc commun absorbé par les effets fixes ; exposition fixée avant-guerre ; pas de mortalité différentielle des exposés (vérifiée) ; les citations mesurent les flux de connaissance (posé).

**Limites dites.** Les citations et la similarité de titres ne sont que des **approximations** des flux de connaissance, qui ne sont pas directement mesurables (p. 19, art. 945) ; la divergence des recherches n'est pas forcément nuisible (p. 35, art. 961) ; la différence hors du camp / dans le camp n'est pas significative à 5 % au seuil du 1 % supérieur (p. 43, art. 969).

**Portée pour notre épreuve.** La plus « native » d'un réseau de citations : une coupure exogène du contact entre deux groupes fait chuter les citations transfrontalières (−85 %), ce qui correspond exactement à une sortie de type œuvre-pont entre groupes ; candidate de vérité de signe pour la gradation 2. Réserves : période 1900–1930, dont la couverture dans OpenAlex n'est pas vérifiée (SUPPOSÉ), et unité « camp », non « niche ».

---

## Lecture transversale (pour la question 6, sans nouveau chiffre)

- Les quatre expériences naturelles identifient par un **choc extérieur** (décès inattendu, effondrement politique, ouragan, guerre) plus des hypothèses écrites (non-anticipation, tendances parallèles, absence d'interférence), jamais par le réseau de citations seul : Azoulay p. 10–11 (art. 8–9), Borjas p. 24 et 27 (art. 23 et 26), Campos p. 3–4 (art. 997–998), Iaria p. 36 et 38 (art. 962 et 964). Cela appuie la position « pas à lui seul ».
- Les trois papiers d'apprentissage disent la même chose côté méthodes : sans hypothèse ni supervision, rien (Locatello p. 3) ; avec une variable auxiliaire assez variable, les latentes (Khemakhem p. 5–6) ; avec des cibles d'intervention observées, les variables causales minimales (Lippe p. 3–5). Schölkopf (p. 4–5, art. 615–616) en fait un cadre, sans théorème propre.
- Signes : retirer un nœud ou un contact baisse la production (Azoulay, Campos, Iaria) ; mais un afflux d'idées et de producteurs la baisse aussi chez les producteurs en place (Borjas) : « plus de contacts, plus de fertilité » n'est pas monotone dans ces vérités.
