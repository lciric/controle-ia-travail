# Proposition B — Tour III.2 : critique croisée de méthode

---

## Sur la proposition A

### (a) Défauts de méthode

**1. La base de ponts postérieurs à 1991 est à la fois l'étalon et le terrain d'entraînement de l'instrument E1.** A reconnaît que les données brutes (LaTeX arXiv, OpenAlex) ne couvrent pas les ponts canoniques antérieurs (RL1-07, repris en §a-9), et sa solution — restreindre la base à l'après-1991 — réduit le nombre de ponts disponibles sans dire combien il en reste. Si ce nombre est petit (quelques dizaines), la puissance de la comparaison H_A / H_B en précision@k est trop faible pour que le seuil illustratif de 5 points ait un sens : l'intervalle de confiance sera plus large que l'écart attendu. Plus grave, le même pool de ponts sert implicitement (i) à calibrer la partition en chapelles et le détecteur de trous, (ii) à départager H_A et H_B dans E1, et (iii) à évaluer le filtre Gu-Krenn dans E6. Aucun partage formel (ponts d'étalonnage vs ponts de test) n'est écrit. Ce n'est pas une fuite au sens habituel, mais une confusion des rôles du même jeu de données qui surévalue la puissance apparente de chaque test.

**2. Le contrôle négatif de E1 (permutation des dates de ponts) teste la fuite temporelle, pas la circularité.** Si le profil « canal faible ET structure commune forte » est construit en utilisant les mêmes traits qui définissent la partition en niches, et que la partition est elle-même ajustée sur le graphe où les ponts figurent déjà comme arêtes de citation, alors un score élevé peut refléter la cohérence interne de la partition plutôt qu'un pouvoir prédictif. Le contrôle manquant : retirer tous les articles constituant les ponts du graphe, refaire la partition et le scoring, et vérifier que le classement ne s'effondre pas.

**3. E2 (mondes inventés) ne teste pas la fertilité bibliographique.** A le reconnaît (dernière ligne de E2 : « cela ne valide pas encore une fertilité bibliographique ») mais ne propose aucun pont entre la sur-additivité plantée et la littérature réelle. La transition critique dans un monde inventé à vérité connue peut parfaitement apparaître ou disparaître selon les règles du générateur (nombre d'axiomes, structure des implications), sans qu'on sache si elle se transporte aux données OpenAlex. L'expérience est utile pour calibrer les tests statistiques, mais elle ne tranche pas la question B pour l'objet réel.

**4. E4 (biais du juge figé) utilise des belles au bois dormant réécrites.** La réécriture dans le « vocabulaire d'avant leur date » est elle-même une intervention non contrôlée : si la réécriture conserve des indices de structure (longueur atypique, vocabulaire rare), le juge peut les détecter ou les manquer pour des raisons indépendantes de la distance. Le contrôle proposé (vocabulaire unifié) masque la distance mais aussi la structure : il ne distingue pas « le juge note la distance » de « le juge note la structure inhabituelle ».

**5. Risque de circularité dans E5 (dose de contact).** Le juge de fertilité est « distinct du juge de sélection », mais les deux sont des instances de modèles entraînés sur des données qui se chevauchent (corpus général). Si le juge de fertilité a appris, dans ses poids, qu'un tableau minimal plus long corrèle avec un score plus élevé (par construction de son pré-entraînement), il récompensera la dose sans que la fertilité ait changé. Le contrôle placebo (titres d'une niche sans structure commune) est le bon garde-fou, mais A ne dit pas comment vérifier que le juge n'utilise pas la longueur du contexte comme signal.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

- **E1 (précision@k)** : si la distribution des scores des ponts et des témoins a une forte superposition — ce qui est attendu quand les deux populations sont appariées par taille, âge et croissance —, la précision@k pour k petit (disons k ≤ 30, illustratif) a une variance binomiale élevée. Sous un modèle binomial Bin(k, p) avec p = p₀ + δ (taux de base p₀ ≈ 0.5 pour des témoins bien appariés et δ = 0.05), la probabilité de détecter un écart de 5 points avec un intervalle à 90 % excluant zéro exige k ≥ 400 (illustratif, calcul de puissance standard pour une différence de proportions). Pour 30 ponts et 90 témoins, la puissance est négligeable.

- **E2 (effondrement d'échelle)** : la mise à l'échelle par taille finie suppose que les mondes inventés n'ont pas de dimension effective anormale. Si la structure du graphe d'implications est à petit monde ou hiérarchique, les exposants observés ne convergent pas avec seulement quatre tailles (facteur 4), et l'effondrement est indiscernable d'un artefact de forme fonctionnelle. La puissance du test BIC entre quadratique et loi de puissance est faible si la plage de couplage balayée ne couvre pas le seuil : 12 points et 4 tailles donnent environ 48 valeurs de (couplage, taille) pour estimer au moins 3 paramètres (exposant, seuil, amplitude), soit un rapport données/paramètres médiocre.

- **E3 (essaim)** : avec N ≤ 64 agents et 4 valeurs de N, l'estimation du taux de survivantes par million de tokens est un ratio de petits comptages. Si le taux de base est de l'ordre de 1 % (illustratif), on attend ~10 survivantes pour 10⁸ tokens par condition — insuffisant pour détecter un écart de 20 % entre conditions avec un test de proportions standard. Le plan factoriel a 4 × 3 = 12 cellules ; avec un budget de 10⁸ tokens par cellule (illustratif), la réplication par cellule est trop faible.

- **E5 (dose de contact)** : 8 doses × un juge × un nombre de courses non spécifié. La courbe dose-réponse a 8 points ; une forme non linéaire (seuil ou cloche) exige au moins un modèle à 3 paramètres ; la distinction seuil/cloche n'est pas identifiable avec 8 points (au mieux 5 degrés de liberté), surtout si les taux de survie sont bruités (binomiaux à petits effectifs).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1** : un contrôle où le profil est calculé sur un graphe dont tous les articles des ponts connus ont été retirés (pas seulement les dates permutées). Sans lui, on ne sait pas si le profil détecte un signal pré-pont ou la trace du pont lui-même dans le graphe.

2. **E3** : un contrôle « meilleur-de-N à contexte enrichi » (chaque agent indépendant reçoit un résumé des idées d'un run précédent, mais pas de communication en temps réel). Si ce contrôle fait aussi bien que l'essaim, l'avantage n'est pas dans la communication mais dans l'élargissement du prompt.

3. **E4** : un contrôle avec des idées contemporaines de même distance mais connues pour avoir échoué (publiées et jamais reprises malgré une bisociation revendiquée). Sans lui, la rétrodiction ne distingue pas « le juge reconnaît les bonnes bisociations » de « le juge reconnaît les idées vieillies ».

4. **E6 (Gu-Krenn à longue portée)** : un contrôle où l'on vérifie que la strate « distance > 3 » ne contient pas un biais de sélection systématique (paires rares, petites niches, domaines émergents). Si la composition de cette strate diffère qualitativement de la strate « distance ≤ 3 », la comparaison de précision@k n'est pas interprétable sans un ajustement.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Le détecteur d'isomorphisme mathématique (AST LaTeX) est calibré sur des paires canoniques choisies par le concepteur.** Le tableau d'étalonnage (Instrument 2) propose 100 paires isomorphes « canoniques » (diffusion thermique / Black-Scholes, Ising / Hopfield) appariées à 100 leurres. Le choix de ces paires est informé par la connaissance des ponts historiques, c'est-à-dire par l'issue même que l'instrument doit prédire. Un expert qui ne connaît pas les ponts construirait les paires autrement. Ce n'est pas un contrôle, c'est un entraînement déguisé. Le contrôle qui manque : tirer les paires au hasard parmi les équations du corpus, en aveugle, et demander à un annotateur humain de coder l'isomorphisme indépendamment de l'outil.

**2. Le pipeline à trois étages (sélection → filtre d'alignement → essaim modulaire) est une architecture non testée, présentée comme une conclusion.** C traite la « parade directe à la faille de Bastounis et al. » comme acquise alors que le filtre d'alignement d'énoncé (back-translation par un agent neuf) n'a ni taux de détection ni taux de fausses alertes mesurés sur des cas plantés. L'instrument 4 du tableau (c) donne des seuils illustratifs (TPR ≥ 90 %, FPR ≤ 10 %) mais aucune donnée ni méthode pour les atteindre. Si le filtre a un FPR réel de 30 % (illustratif, plausible pour un LLM non spécialisé sur la traduction formelle), il bloquera une proportion significative de vraies bisociations ; si son TPR est de 70 %, il laissera passer une proportion significative de bisociations spécieuses.

**3. Le Duel 1 (distance de domaine vs trou à isomorphisme formel) confond la mesure du trou et la mesure de la compatibilité formelle.** La variable confondante est la taille du corpus LaTeX disponible par niche. Les niches fortement mathématisées (physique théorique, mathématiques pures) ont beaucoup d'équations extractibles ; les niches expérimentales ou computationnelles en ont peu. H_B (trou + isomorphisme AST) sera systématiquement favorisée pour les paires de niches à haut taux de LaTeX, non parce qu'elles sont plus fertiles, mais parce que la mesure d'isomorphisme a un signal là où les leurres n'en ont pas. Le contrôle manquant : stratifier l'évaluation par densité d'équations dans le corpus.

**4. Le Duel 4 (observationnel vs randomisé) a un problème de transport non résolu, identique à celui de A.** C pose H_B (échec du transport) comme hypothèse, mais la falsifie par « si $H_A$ prédit dans l'intervalle de confiance à 90 % de l'ATE expérimental » — ce qui ne falsifie pas H_B au sens fort. Un effet observationnel peut tomber dans l'intervalle de l'effet randomisé par hasard ; la concordance ponctuelle sur une dose ne prouve pas la transportabilité pour toutes les doses ou pour d'autres types de paires. La falsification de H_B exigerait une concordance sur au moins trois doses indépendantes (illustratif), chacune hors de l'intervalle avec une probabilité contrôlée.

**5. Le coût de 1 100–1 500 $ (illustratif) pour le Duel 5 est trop optimiste et masque le coût réel de l'expérience.** C annonce 3 × 10⁹ tokens sur un nœud de 8 GPU H100 en 55 heures. En pratique, les modèles ouverts de 70B quantifiés en mode réflexion profonde (type DeepSeek-R1) ont un débit effectif de 2 000–5 000 tokens/s par GPU (illustratif, dépendant de la longueur de contexte), soit 16 000–40 000 tokens/s pour 8 GPU. À 3 × 10⁹ tokens et 20 000 tokens/s, le temps de calcul est ~42 heures, mais cela suppose une utilisation à 100 % sans aucun temps d'attente, d'orchestration ou de consolidation. Le coût réel en location cloud (H100 à ~3 $/h/GPU, illustratif) serait 8 × 3 × 55 = 1 320 $ uniquement pour le calcul d'inférence, hors stockage, orchestration, tests de mort en bac à sable et reproduction des conditions de contrôle. Le coût d'une reproduction complète (trois réplications des cinq conditions + contrôles) est au moins 3–5× plus élevé.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

- **Duel 1 (AUPRC)** : si la proportion de ponts dans la base est faible (200 / 2200 ≈ 9 %), l'AUPRC est sensible au nombre de faux positifs dans la queue gauche du classement. Un décalage de quelques paires dans le top-50 peut changer l'AUPRC de plusieurs points. La condition critique : si la variance inter-ponts (certains ponts sont « faciles », d'autres « difficiles ») est grande par rapport à la variance inter-paires-témoins, le bootstrap à 95 % ne sera pas calibré (il sous-estimera la largeur de l'intervalle) à moins de stratifier par difficulté.

- **Duel 2 (BIC)** : le BIC pénalise linéairement le nombre de paramètres ; un modèle « logistique à seuil » et un modèle « quadratique en cloche » peuvent avoir le même nombre de paramètres effectifs. L'écart BIC de 10 (illustratif) n'a de sens que si les deux modèles sont strictement emboîtables ou si on utilise un BIC pour modèles non emboîtés (type BIC adapté), ce qui n'est pas standard. Si le vrai signal est une cloche asymétrique ou un plateau, les deux modèles s'ajusteront mal et le BIC ne tranchera pas.

- **Duel 3 (Précision@100)** : la strate « $d_{\text{soc}} \geq 3$ » peut être très petite (la grande majorité des paires publiées sont à courte distance). Si cette strate contient, disons, 500 paires dont 10 ponts (illustratif), la précision@100 est tirée vers le taux de base de 2 %, et un gain de 5 points de pourcentage signifie passer de ~2 % à ~7 %, soit de ~2 ponts à ~7 ponts dans le top-100 : un changement de 5 ponts sur 10 existants, au sein d'un échantillon de taille 100, avec une variabilité binomiale considérable. La puissance est insuffisante pour un test bilatéral.

- **Duel 5 (Simpson pondéré)** : l'indice de Simpson sur les solutions est sensible à la granularité du regroupement. Si les solutions sont regroupées trop finement (chaque solution est sa propre classe), la diversité est maximale par construction ; si elles sont regroupées trop grossièrement, la diversité est minimale. Le seuil de 15 % de sur-additivité pondérée par Simpson n'est interprétable que si le grain du regroupement est fixé et commun aux deux conditions. C ne spécifie pas ce grain.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Duel 1** : stratification par densité d'équations LaTeX dans le corpus. Sans elle, H_B (isomorphisme formel) est confondue avec « la niche a beaucoup d'équations ».

2. **Duel 2** : un monde inventé dont la fertilité suit exactement une cloche asymétrique non différentiable au sommet (un objet intermédiaire entre cloche lisse et seuil). Si les tests de criticité « détectent » un seuil sur ce monde, ils sont mal calibrés.

3. **Duel 3** : reproduction de Gu-Krenn sur les mêmes données et avec le même code avant toute comparaison. C l'annonce (« ligne de base : classifieur de Gu & Krenn, 2024 reproduit sur concepts plats ») mais ne dit pas ce qui se passe si la reproduction échoue (score significativement différent de l'AUPRC rapportée). L'expérience entière s'effondre si le point de référence est faux.

4. **Duel 5** : un contrôle où les îlots de H_B reçoivent, au moment de la pollinisation, des fragments tirés d'un run d'une autre paire de niches (pas la même paire). Si l'avantage survit, la pollinisation n'est pas spécifique au contenu mais est un effet de relance ou de diversification du prompt.

5. **Instrument 5 (juges figés)** : un contrôle avec des idées *fausses mais plausibles* (bisociations dont le lien structurel est un artefact notationnel). Les 40 impasses documentées ne suffisent pas si elles sont faciles à détecter. Il faut des leurres calibrés sur la difficulté du juge.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. D partage avec A et C le problème du nombre de ponts.** La table (a) est la plus exhaustive en hypothèses non établies, mais les expériences E1 à E7 ne spécifient jamais le nombre minimal de ponts nécessaires pour atteindre une puissance donnée. La mention « seuils illustratifs » sans calcul de puissance, même illustratif, laisse ouverte la possibilité que l'expérience ne puisse rien trancher.

**2. E3 (transition critique) exige « au moins trois tailles » mais ne spécifie pas le facteur entre tailles.** L'effondrement d'échelle en physique statistique fonctionne sur des ordres de grandeur : des systèmes de taille 10², 10³, 10⁴. Avec des facteurs de 2 ou 3 (le minimum implicite de « au moins trois tailles »), le raidissement de la pente est souvent invisible et l'effondrement est indiscernable d'un artefact de lissage. A propose un facteur 4 entre tailles (§E2) ; D ne dit rien, ce qui est un degré de liberté non verrouillé.

**3. E6 (transport) teste la concordance du signe et de l'ordre de grandeur d'un « choc indépendant, dans un environnement tenu à l'écart ».** Mais D ne nomme aucun choc candidat ni aucun environnement. Sans cette spécification, E6 est une promesse, pas un protocole. Le risque : choisir le choc et l'environnement après avoir vu les résultats de E5, ce qui détruit le préenregistrement.

**4. La table des instruments (§c) est la plus complète des trois propositions, mais elle mélange des instruments de natures différentes (partition, prédiction, inférence causale, revue bibliographique) dans un format uniforme qui masque les différences de vérifiabilité.** La « revue bibliographique » a un « TD : rappel sur un jeu de références semences » : c'est un test de couverture, pas un taux de détection au sens habituel. La mesure est correcte en soi mais le format la fait paraître comparable à un classifieur, ce qui n'est pas le cas.

**5. L'ancrage matériel (§d) est réaliste pour un pilote mais ne chiffre pas le coût de la base de ponts.** Constituer 30+ ponts étiquetés par type (s'ignorent / se contredisent) avec 3 témoins appariés chacun, par un lecteur humain aveugle, prend de l'ordre de 5 à 20 jours-personnes (illustratif) selon le domaine. C'est le goulot réel de E1, comme D et A le reconnaissent, mais aucun des deux ne le budgétise.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

- **E1 (AUPRC, gain ≥ 20 %)** : un gain relatif de 20 % sur une AUPRC de base de 0,10 (illustratif, attendu pour des témoins bien appariés) signifie passer à 0,12 — un écart de 0,02 en valeur absolue. Pour détecter un tel écart avec un intervalle bootstrap à 95 % excluant zéro, il faut de l'ordre de 10 000 paires (illustratif, dépendant de la corrélation entre prédictions) — bien au-delà des quelques centaines de ponts disponibles après 1991.

- **E4 (apprentissage de la fertilité vs densité)** : « calibration par fenêtre » exige de segmenter les prédictions en déciles ou ventiles de probabilité prédite, puis de mesurer l'écart entre prédiction et fréquence observée dans chaque bin. Avec un taux de base de ponts de quelques pour cent, les bins à haute probabilité prédite contiendront très peu de ponts, rendant la calibration instable. L'erreur de calibration attendue (ECE) n'est pas interprétable avec moins de ~50 cas par bin (illustratif).

- **E5 (dose de contact)** : D corrige la faiblesse de A (4 doses → 8 doses) mais ne dit pas combien de courses par dose. Avec un taux de survie de base de 10 % (illustratif) et 50 courses par dose (illustratif), on attend ~5 survivantes par dose. La courbe dose-réponse sur 8 points × 5 événements par point n'a pas la puissance de distinguer un seuil d'une sigmoïde.

- **E7 (essaim)** : les métriques incluent « taux de doublons et de faux nouveaux, origine croisée dans le graphe de provenance ». Le graphe de provenance n'est exploitable que si chaque message est tracé et attribué ; avec des modèles ouverts locaux, le bus de messages doit être implémenté ad hoc. Si le traçage est imparfait (messages non attribués, conflits de timestamp), la mesure d'origine croisée est bruitée au point de ne plus discriminer les conditions.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1** : identique à la critique de A — retirer les articles des ponts du graphe avant de calculer le profil. D ne le mentionne pas explicitement.

2. **E2 (sur-additivité en monde inventé)** : un contrôle où le « croisement » est effectué entre deux sous-ensembles d'une même niche (pseudo-croisement). D le mentionne (« pseudo-croisement d'une niche avec sa copie anonymisée ») : c'est correct. Mais il manque un second contrôle : croisement de deux niches dont les règles d'implication sont rendues incompatibles par construction (conflit de prémisses). Si la sur-additivité est positive dans ce cas, la définition ne capture pas l'incompatibilité.

3. **E5** : D mentionne date placebo et intervention sans effet attendu, ce qui est correct. Le contrôle manquant : variation de la longueur du contexte sans variation du contenu (même dose, titres mélangés aléatoirement entre niches). Si l'effet persiste sous mélange, c'est la taille du contexte, pas la pertinence du contact, qui agit.

4. **E7** : D mentionne messages aléatoires, communication supprimée, consolidateur supprimé, meilleur-de-N et agent unique. C'est le jeu de contrôles le plus complet des trois propositions. Le contrôle manquant : un essaim dont les agents sont de familles de modèles différentes (e.g., un îlot Qwen, un îlot Llama, un îlot DeepSeek) comparé à un essaim homogène. Si l'hétérogénéité inter-familles n'améliore pas la diversité, la diversité de l'essaim est un artefact de la stochasticité d'un seul modèle.

5. **Table des instruments, « Régimes de génération »** : le contrôle « meilleur-de-N et agent unique à budget multiplié » est listé. Le contrôle manquant pour la proposition D spécifiquement : un essaim avec consolidation mais sans DAG de dépendances — pour isoler l'apport du DAG (traçabilité et révocation) de l'apport de la consolidation elle-même.

FIN-DE-CELLULE