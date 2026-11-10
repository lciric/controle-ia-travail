# Rapport de lecture — lot 5-A : détection séquentielle et multi-agents (niveau 3 de l'état de l'art) — v1

Écrit le 2026-11-10 vers 11:05 UTC (heure relevée par `date -u`). Lecteur neuf : je n'ai écrit ni le programme ni aucun rapport antérieur.

Les renvois entre crochets ([G14], [C21]…) désignent les citations exactes de l'annexe A, chacune avec son fichier et sa page (page 1 = première page du fichier).

## 0. En tête : ce qu'il faut voir d'abord

**Aucun des six articles ne lit un état interne.** Les six accumulent ou jugent des signaux de sortie (gains d'un jeu, réponses plongées, traits de surface du texte, scores de classifieurs de texte). La conjonction de H2 (énoncé N-007) n'est occupée par aucun.

**Occupations partielles, toutes en boîte noire, à porter devant Lazar :**

1. **H2 — occupée en partie, en boîte noire, par 2606.20746 (Corll)**, et l'article apporte en même temps un **contre-indice conditionnel**.
   - Fait : somme cumulée de Page (remise à zéro, dérive prise sur le bénin seul) de scores par événement figés, sur des trajectoires d'agents à outils, pour des directives dont chacune reste sous le seuil par événement ; comparaison au maximum ([C1], [C6], [C8]).
   - Non fait : sondes ou états internes ; garantie toujours valide (l'auteur l'exclut : [C21]) ; seuil par action à 1 % de faux positifs ; rappel selon l'horizon ; sabotage par l'agent lui-même (ce sont des textes greffés).
   - Contre-indice : l'accumulation amplifie une marge qui existe déjà sous le seuil, elle n'en crée pas ([C5], [C16]) ; résultat nul sur le second axe ([C15]) ; le résultat positif tient à quatre trajectoires sur trois tâches, sans puissance ([C13], [C19]).
2. **Statistique spatio-temporelle du papier B (E3.1, « le cœur vierge ») — squelette occupé en partie, en boîte noire, par deux articles.**
   - 2601.05427 (Gauthier, Bach, Jordan ; ICML 2026 imprimé, [G2]) : un processus e par agent et par déviation, garantie toujours valide par l'inégalité de Ville, combinaison entre agents par la procédure e-BH arrêtée à un temps commun ; l'alarme vient plus tôt quand plusieurs processus montent ensemble ([G5], [G6], [G18]). Signal : gains et actions d'un jeu, pas un modèle de langue.
   - 2605.11135 (Helm, Priebe, Duderstadt ; NeurIPS 2026 imprimé, [H3]) : une statistique de population (distribution des agents dans un espace de plongement de leurs réponses) suivie dans le temps par une carte de contrôle ; accès boîte noire déclaré ([H4]).
   - Non fait par les deux : états internes, sondes, copies d'un même modèle lues en parallèle, comparaison au séquentiel par agent et à la coupe transversale, adversaire qui s'adapte au moniteur.
3. **H3 — occupée en partie, en boîte noire (lecture dure), par 2605.11135** : contamination et taux d'alarme selon la taille du système (cent à cent mille agents) à nombre d'agents dormants constant ([H23], [H26]). Lecture « voisin » défendable : N y est la taille de la population honnête, pas le nombre d'agents entre lesquels un budget de sabotage se répartit ; simulation sans modèle de langue ([H27]). Le programme dit déjà que « les courbes boîte noire sont publiées ».
4. **T — voisin fort, moitié négative en boîte noire, par 2605.11135** : théorème d'existence d'une défection lente non détectée par toute carte à référence glissante, et remarque sur la somme cumulée ([H11], [H12]). Aucune des quatre pièces revendiquées de N-003 n'y figure.

**Limite reconnue qui n'est pas un trou du champ.** Helm et collègues écrivent que l'accès aux activations internes « pourrait » détecter plus tôt et que le compromis apprentissage-sécurité y est une question ouverte ([H17], [H18]) ; Xie range les représentations internes parmi les raffinements optionnels ([X3], [X4]). Ce sont des invitations, pas des preuves que la zone est vide.

## 1. Méthode et réserves sur ma propre lecture

- Empreintes des six PDF vérifiées par `sha256sum -c` contre les compagnons `.sha256` du dossier : six « OK ».
- Extraction page par page par `pdftotext -layout -f N -l N` et, pour la lecture des pages à deux colonnes, par `pdftotext -f N -l N` (ordre de lecture).
- **Écart à la consigne « lire en entier », déclaré.** Pour 2601.05427, j'ai lu ligne à ligne les pages 1 à 14, 22 et 23 (annexes D et E), 30, 31, 34 à 36. Les pages de preuves et de rappels (15 à 21, 24 à 29, 32, 33) et la fin des détails d'expérience (37 à 41) n'ont été parcourues que par leurs titres de section et par une recherche de mots (adversaire, modèle de langue, activation, collusion, indépendance, permutation, échangeabilité, budget). Je n'ai donc pas vérifié les preuves. Les cinq autres articles ont été lus en entier ; les pages de références (2605.11135 p. 11 et 12, 2607.24893 p. 12, 2604.08608 p. 10 et 11, 2606.20746 p. 15 et 16) ont été parcourues, et certaines lignes de tableaux mal rendues n'ont été relues qu'en mode `-layout` (tableaux 3 et 4 de 2607.24893). Aucune figure n'a été ouverte en image : aucun chiffre de ce rapport n'est « lu sur une figure ».
- Contrôle des citations : script `controle_citations_lot5A_v1.py`, lancé par `python3 -I`. Garde essayée d'abord sur un cas juste (passe), sur le même cas altéré (échec attendu, obtenu) et sur une mauvaise page (échec attendu, obtenu). **119 citations contrôlées, 0 échec** (90 trouvées en mode `-layout`, 29 en ordre de lecture seulement, à cause de l'entrelacement des colonnes). Deux citations avaient échoué au premier passage et ont été corrigées (une page fausse pour [C6], une exposant parasite dans [H19]).
- Nature des chiffres : tout chiffre ci-dessous est « auteurs » (imprimé), sauf mention « calcul ».

## 2. Les six articles

### 2.1 — 2601.05427v3, Gauthier, Bach, Jordan, « Anytime Detection of Strategic Deviations in Multi-Agent Systems » (41 pages)

Venue imprimée : actes de la 43ᵉ conférence internationale sur l'apprentissage automatique (ICML), 2026 [G2].

**Réponses aux quatre questions.**
- Signal accumulé : sortie observable, jamais un état interne. Dans les jeux répétés, un incrément de regret calculé sur les gains, qui exige les gains contrefactuels ([G4], [G7], [G10]) ; dans les jeux stochastiques, un rapport de vraisemblance entre la politique cible et une politique déviante, qui exige de connaître la politique cible ([G8], [G11]). Aucun modèle de langue : jeu 2 × 2, pierre-feuille-ciseaux à vingt joueurs, football sur grille, prédateur-proie ([G20]). Le seul lien avec les modèles de langue est une référence à un audit de facturation par e-valeurs ([G16]).
- Garantie : oui, toujours valide. Surmartingale de test, inégalité de Ville, contrôle du taux d'erreur par famille à tout instant ([G1], [G5]) ; martingale exacte dans le cas des rapports de vraisemblance ([G9]) ; contrôle du taux de fausses découvertes par e-BH arrêtée à un temps commun ([G6]).
- Agents : plusieurs (un processus par joueur et par déviation).
- Adversaire adaptatif : non. Les profils d'actions sont supposés indépendants et de même loi à chaque tour ([G3]) ; la déviation est stationnaire et active dès le début ([G14]) ; la réaction d'agents qui apprennent aux détections est renvoyée aux travaux futurs ([G12]).

**Résultats (auteurs).** Sous l'hypothèse nulle, 3 fausses alarmes sur 300 exécutions de 4 000 tours, soit 0,01 pour un niveau visé de 0,2 ([G17]). Jeu à vingt joueurs et soixante hypothèses : temps moyen de détection de 2 025 tours pour le contrôle par famille contre 1 248 pour e-BH ([G21]) ; accélération de 1,15 fois sur le jeu 2 × 2 ([G19]). Temps de détection en 1/ε² pour une déviation de taille ε (théorème 3.4, non vérifié par moi).

**Ce qu'il ne fait pas.** Pas de rupture en cours de route : les auteurs se disent distincts des méthodes de détection de rupture (somme cumulée de Page) et alignés sur le test séquentiel de Wald, « plutôt que les récurrences additives » ([G13], [G14], [G15]). Pas de dépendance entre tours, pas d'effet épisode. Le détecteur signale où les incitations sont violées, pas qui a dévié : dans le jeu à vingt joueurs, les alarmes tombent sur les quinze joueurs conformes ([G22], [G23]).

**Limites reconnues.** Gains contrefactuels requis ; politique cible connue requise ; déviations stationnaires seulement ([G10], [G11], [G12]). Une marge strictement positive est nécessaire : une déviation arbitrairement petite repousse l'alarme sans borne ([G24]).

**Réserves.** Le taux de fausses alarmes de 0,01 pour 0,2 visé montre une garantie très conservatrice (les auteurs l'attribuent au petit paramètre de mise) ; ce n'est pas un résultat « trop beau », c'est un coût de puissance. Rien d'incohérent relevé dans les pages lues.

### 2.2 — 2605.11135v2, Helm, Priebe, Duderstadt, « Control Charts for Multi-agent Systems » (19 pages)

Venue imprimée : 40ᵉ conférence NeurIPS, 2026 [H3] ; version 2 datée du 5 novembre 2026 sur la première page.

**Réponses aux quatre questions.**
- Signal : boîte noire, déclarée ([H4]). Réponses des agents à un jeu de questions, plongées par un modèle de plongement de texte, puis réduites à une trajectoire d'ensemble du système. Les activations internes ne sont citées que comme une autre façon de plonger des modèles dans des travaux antérieurs ([H5]).
- Garantie : non toujours valide. Carte de contrôle de Shewhart à k écarts types, avec une référence fixe ou une fenêtre glissante ; le taux de fausse alarme est donné instant par instant sous hypothèse d'observations indépendantes et de même loi, hypothèse que les auteurs disent non observée ([H20]). De plus les plongements sont ajustés sur tous les instants à la fois, donc la statistique à l'instant t dépend du futur ([H6]).
- Agents : plusieurs ; cinq agents avec un modèle de langue (gpt-4o-mini, [H7]) dans l'expérience principale, puis de cent à cent mille agents par une fonction de substitution sans modèle de langue ([H9], [H27]).
- Adversaire : agents dormants qui répondent par une phrase témoin selon un calendrier fixé d'avance, rapide ou lent ([H8]). Pas d'adversaire qui s'adapte au moniteur, pas d'adversaires coordonnés ([H16]).

**Résultats (auteurs).**
- Une référence fixe déclenche de fausses alarmes quand les agents apprennent ; une référence glissante absorbe un décalage persistant ([H10]) et laisse passer une défection lente ([H1], [H2]).
- Théorème 1 (existence d'une défection non détectée) : un calendrier à taux constant étalé sur L fenêtres atteint un déplacement cible avec un nombre attendu de défections qui ne dépend pas de L ([H14], [H29]), tandis que le décalage vu dans toute fenêtre tend vers zéro. Remarque : la même absorption vaut pour une somme cumulée à référence glissante, et un adversaire qui reste sous la tolérance de la somme cumulée empêche la charge de monter ; une somme cumulée à référence fixe accumule la dérive légitime ([H11], [H12], [H13]).
- « Théorème 2 » (compromis apprentissage-sécurité) et conjecture qu'aucune procédure ne satisfait les deux exigences contre tout adversaire ([H15]) ; la direction inverse n'est pas formalisée ([H21]).
- Annexe C : cent agents dormants dans un système de cent mille agents (un millième) contaminent 57 % des agents honnêtes pour un rapport d'alarme de 0,65 ([H23]) ; avec dix agents dormants la contamination se dilue quand le système grandit, et elle suit la fraction adverse et la topologie plutôt que la taille ([H26]) ; un seul agent dormant contamine tout le système quand le jeu de questions est petit ([H25]).

**Limites reconnues.** Graphe complet, adversaire simple, agents simplifiés, cadre boîte noire ([H16], [H17], [H18]) ; pas de localisation de l'agent responsable ([H19]) ; hypothèses 3 à 5 posées et non dérivées.

**Incohérences et réserves.**
- La liste des contributions annonce trois contributions mais est numérotée de 2 à 5, avec la même contribution imprimée deux fois (p. 2) ; une phrase est fautive ([H28]). Signes d'une version en cours de révision.
- Le « théorème 2 » n'a pas de démonstration propre : il réunit le théorème 1 et un argument de loi des grands nombres ; la thèse générale est une conjecture ([H15]).
- Le résultat à grande échelle repose sur une fonction de substitution, validée « qualitativement » sur une figure que je n'ai pas ouverte ([H9]).
- Les cas « détectables » de l'annexe C reposent sur un à quatre alarmes et ne sont pas significatifs, de l'aveu des auteurs ([H24]).
- Le théorème 1 suppose des observations indépendantes et de même loi que les auteurs disent eux-mêmes non observées ([H20]).

### 2.3 — 2606.07624v1, Xie, « Sequential statistical inference for Large Language Models: Representation, validity, and monitoring » (6 pages)

Venue imprimée : discussion invitée préparée pour *The American Statistician* [X1]. Texte de position, sans expérience ni résultat ([X2]).

**Réponses aux quatre questions.**
- Signal : un score défini sur l'historique observable des interactions. Les représentations internes sont nommées, pour être rangées au second plan : utiles « quand elles sont disponibles », propres à chaque modèle, « raffinements optionnels » ([X3], [X4]).
- Garantie : le raisonnement toujours valide est recommandé en une phrase, par renvoi à Howard et collègues ([X5]) ; l'alarme est un temps d'arrêt dont le seuil contrôle les fausses alarmes sous un régime de référence ([X6]). Rien n'est construit.
- Agents : un système ; les cartes de contrôle multi-agents de Helm et collègues sont citées en une phrase ([X7]).
- Adversaire : les « usages adverses » sont mentionnés comme une cause de dérive ([X8]) ; aucun modèle d'adversaire.

**Ce qu'il ne fait pas.** Aucune mesure, aucun agent, aucun sabotage, aucune sonde. Rien à signaler au titre des résultats trop beaux : il n'y a pas de résultat.

### 2.4 — 2607.24893v2, Fernandez Arias, Mistry, Wang, Hu, « Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study » (12 pages)

Aucune venue imprimée (prépublication, version 2 du 2 octobre 2026).

**Réponses aux quatre questions.**
- Signal : boîte noire, traits de surface du texte des observations d'outils (longueur, entropie de Shannon, part de caractères base64), lus par un classifieur à arbres sur un préfixe croissant de la trajectoire ; ou texte brut lu par un modèle réglé. Les activations internes ne sont citées que comme une famille de défenses antérieures qui jugent un artefact isolé ([F3]).
- Garantie : aucune. Le score est une probabilité de classifieur recalculée sur chaque préfixe, l'alarme est le premier franchissement d'un seuil ; les fausses alarmes sont mesurées hors pli. Ce n'est pas une accumulation additive : c'est un classifieur supervisé, entraîné avec des exemples d'attaque.
- Agents : plusieurs (un gestionnaire et trois sous-agents), mais le défenseur lit un seul flux d'événements réunis ([F7]).
- Adversaire : fixe. L'attaquant contrôle des outils empoisonnés et l'assemblage après l'exécution, pas les agents ni le moniteur ([F6]). Les agents ne sabotent pas : leur raisonnement est normal. La variante « mots ordinaires » est une réécriture hors ligne des journaux, pas une nouvelle exécution ([F10]).

**Résultats (auteurs).** 2 082 trajectoires, 14 pas en moyenne, cinq modèles ouverts, deux environnements d'outils ([F8], [F9]). Détecteur entraîné sur préfixes : 99,5 % des 428 attaques réussies signalées, médiane de douze pas restants, 1,1 % de fausses alarmes sur les exécutions sans fragment, mais 80,5 % sur les exécutions avec fragments qui n'ont pas abouti, soit 27,6 % au total ([F1], [F11], [F12]). Sur le texte chiffré, un détecteur qui ne lit que l'observation courante fait aussi bien que le préfixe ([F4]) ; sur la variante en mots ordinaires, longueur retirée, le préfixe fait 44,4 % contre 30,4 % ([F13]). Les détecteurs d'anomalie ajustés sur les exécutions propres seules sont au niveau du hasard ou en dessous ([F16]) ; un garde-fou du commerce signale 91,8 % des exécutions sans discernement ([F15]).

**Limites reconnues.** Une seule famille d'attaque ([F19]) ; les trajectoires ne sont jamais appariées en longueur ; la fenêtre d'alerte existe parce que l'assemblage a lieu après l'exécution ; le signal tient à la surface de l'attaque et non à sa structure répartie ([F2], [F14]).

**Incohérences et réserves.**
- Le titre du résultat (99,5 % à environ 1 % de fausses alarmes) ne vaut que pour les exécutions sans fragment : le même détecteur signale 80,5 % des exécutions qui portaient des fragments sans aboutir ([F11]). Il détecte l'injection, pas l'attaque réussie.
- Le détecteur entraîné sur préfixes s'allume au pas 1 en médiane ([F11]), alors que le détecteur entraîné sur exécutions complètes s'allume au pas 8, « six pas après la première injection » ([F20]), ce qui place l'injection médiane vers le pas 2 (calcul sur des médianes, donc approximatif) ; or seules 0,9 % des détections seraient antérieures à l'injection ([F21]). Les trois chiffres ne se recoupent pas sans une convention de numérotation que l'article ne donne pas. Réserve.
- Les comparaisons entre le classifieur à arbres et le modèle réglé reposent sur des protocoles de rééchantillonnage différents (dit par les auteurs).

### 2.5 — 2604.08608v2, Ahad et collègues, « Semantic Intent Fragmentation: A Single-Shot Compositional Attack on Multi-Agent AI Pipelines » (11 pages)

Venue imprimée : accepté au symposium d'été 2026 de l'AAAI « AI Agents for the Cyber Battlefield » [S3].

**Réponses aux quatre questions.**
- Signal : boîte noire, scores de classifieurs de texte par sous-tâche, puis un juge génératif au niveau du plan entier et une analyse de flux d'information par règles. Aucun état interne (le mot « probe » y désigne une question posée à l'orchestrateur).
- Garantie : aucune ; rien de séquentiel. Le contrôle se fait une fois, entre la génération du plan et le premier envoi.
- Agents : un orchestrateur et trois sous-agents, simulés par des modèles interrogés par consigne ([S14]).
- Adversaire : un utilisateur légitime qui envoie une seule demande et ne fait plus rien ([S1]) ; non adaptatif. L'attaque ne prétend pas échapper à toute défense ([S7]).

**Résultats (auteurs).** 10 scénarios sur 14 (71 %) produisent un plan contraire à la politique alors que chaque sous-tâche passe les classifieurs ([S2]) ; le juge de plan et l'analyse de flux détectent les 10 attaques confirmées, 0 fausse alarme sur 8 contrôles bénins ([S4], [S9]).

**Incohérences et résultats trop beaux — réserve forte.**
- **Circularité.** Un scénario n'est compté comme attaque que si le juge de plan le déclare dangereux ([S5]) ; ce même juge est ensuite crédité d'avoir détecté toutes les attaques confirmées ([S4]). Le « 10 sur 10 » est vrai par définition. Le taux de fausses alarmes de 0 % repose sur huit contrôles écrits par les auteurs ([S9]).
- **Théorèmes.** Le théorème 1 reformule la définition du score de fragmentation ; le théorème 2 est « prouvé » par les dix cas observés ([S6]). L'affirmation qu'aucune amélioration d'un classifieur par sous-tâche ne peut combler l'écart ([S15]) est contredite dans l'article même : un juge génératif reconnaît l'intention de la troisième sous-tâche prise isolément dans 14 cas sur 14, et aucun cas n'est « purement » compositionnel ([S12], [S13]).
- **Chiffres.** 71 % contre 44 % est appelé un écart de 28 points ([S8]) : 27 points (calcul). « 8 des 87 sous-tâches » ([S11]) alors que 14 scénarios et 8 contrôles à trois sous-tâches font 66 (calcul). Un classifieur signale 16 des 42 sous-tâches d'attaque ([S10]) alors que le résumé dit que chaque sous-tâche passe six familles de classifieurs ([S2]) : seules deux familles sont dans le critère.
- Échantillon de 14 scénarios, tous simulés ([S14]).

Ces chiffres ne sont pas opposables.

### 2.6 — 2606.20746v1, Corll, « Amplify, Don't Create: Temporal Accumulation for Slow-Burn Prompt Injection » (16 pages)

Aucune venue imprimée (prépublication, auteur seul ; la page porte « June 23, 2026 » et le tampon arXiv « 17 Jun 2026 » : les deux dates ne concordent pas).

**Réponses aux quatre questions.**
- Signal : boîte noire. Score par événement d'un détecteur de texte figé : un classifieur linéaire sur n-grammes de caractères et une tête de contraste sur plongements, combinés par le maximum ([C2]). Aucun état interne de l'agent.
- Garantie : aucune. Deux statistiques par trajectoire : le pic, et la « persistance », une somme cumulée de Page remise à zéro dont la dérive est la médiane des scores bénins ([C1], [C8]). L'auteur écrit que ce n'est pas un détecteur en ligne à taux de fausse alarme calibré ([C21]). Le seuil par événement (0,50) est verrouillé par un balayage, sans cible à 1 % ([C22]).
- Agents : un seul agent à outils.
- Adversaire : à moitié adaptatif. Le générateur de greffes n'interroge qu'un détecteur de cloisonnement d'une autre famille ([C7]) ; la discrétion face au détecteur évalué n'est obtenue que par transfert. L'attaquant ne s'adapte pas à l'accumulateur. Les directives sont des textes greffés sur des trajectoires propres, pas un sabotage produit par l'agent.

**Résultats (auteurs).**
- Attaques concentrées (9 trajectoires d'attaque, 40 bénignes, [C10]) : la meilleure statistique de trajectoire dépasse le détecteur par événement de 0,092 en aire sous la courbe, intervalle à 95 % [0,025 ; 0,155] ; la persistance et le pic sont à égalité, +0,031, intervalle [−0,033 ; 0,100] ([C11], [C12]).
- Attaques étalées, axe « exfiltration d'un dépôt git » : aire de 0,708 pour l'écart de persistance, sur quatre trajectoires d'attaque et six leurres bénins ([C4]) ; deux leurres dépassent deux attaques ([C14]) ; l'auteur dit le résultat descriptif et sans puissance ([C13]).
- Axe élargi : aire de 0,167, les trois écarts de persistance valent exactement 0 ([C15]).
- Mécanisme : la somme ne compte que la masse au-dessus de la dérive bénigne ; une greffe poussée sous la dérive n'ajoute rien, quel qu'en soit le nombre ([C9]) ; la bande utile fait environ 0,05 de large ([C17]). D'où la thèse : amplifier une marge, pas en créer ([C5], [C16]).

**Limites reconnues.** Trois tâches indépendantes et quatre trajectoires ([C19]) ; un seul détecteur et un seul juge de plancher ([C20]) ; scores par événement non revérifiés par le contrôle indépendant ; avertissement sur la pseudo-réplication ([C18]).

**Réserves.** L'article est d'une prudence inhabituelle et ne présente pas de résultat trop beau. À l'inverse, le résultat positif est trop mince pour être cité comme un effet mesuré : il porte la thèse comme un mécanisme, pas comme une mesure. La chaîne de calcul n'est pas publiée en entier (les reçus par événement sont retenus).

## 3. Verdicts par énoncé et par article

Vocabulaire : « ne touche pas », « voisin », « contre-indice », « occupée en partie », « occupée ».

### H2 — accumulation additive toujours valide de scores de sondes de l'agent qui agit (énoncé N-007)

| source | verdict | composantes faites | composantes non faites | pages |
|---|---|---|---|---|
| 2606.20746 (Corll) | **occupée en partie, en boîte noire ; contre-indice conditionnel** | somme cumulée de scores par événement sur trajectoire d'agent ; chaque événement sous le seuil par construction ; dérive calibrée sur le bénin seul ; comparaison au maximum | sondes ; garantie toujours valide (exclue par l'auteur) ; seuil par action à 1 % ; rappel selon l'horizon ; sabotage par l'agent ; contre-indice : l'accumulation ne crée pas de marge, bande utile étroite, résultat nul hors d'un axe | 1, 4, 6, 7, 8, 9, 13 |
| 2601.05427 (Gauthier et al.) | voisin (outil) | processus e multiplicatif à garantie toujours valide, sur plusieurs agents | états internes ; modèle de langue ; rupture en cours de trajectoire (écartée par les auteurs) ; dépendance ; adversaire ; calibrage empirique sur épisodes honnêtes | 1, 2, 4, 9, 13 |
| 2605.11135 (Helm et al.) | voisin ; **contre-indice conditionnel** sur le calibrage | suivi séquentiel boîte noire ; un calibrage fixe déclenche de fausses alarmes dès que la base honnête dérive, une base glissante absorbe l'attaque lente | sondes ; accumulation toujours valide ; seuil à 1 % ; sans objet si l'on calibre et lit sur des épisodes honnêtes de même régime | 1, 7, 8, 10 |
| 2607.24893 (Fernandez Arias et al.) | voisin ; **contre-indice de portée limitée** | alerte en cours de trajectoire sur préfixes ; fausses alarmes à 1 % sur exécutions propres ; lire tout le préfixe n'apporte rien quand un pas isolé suffit, et les détecteurs calibrés sur le propre seul échouent | sondes ; accumulation additive ; garantie ; calibrage sans exemple d'attaque ; sabotage par l'agent | 1, 2, 7, 8, 9 |
| 2606.07624 (Xie) | voisin (idée proposée, non réalisée) | scores séquentiels, alarme par temps d'arrêt, raisonnement toujours valide recommandé ; représentations internes nommées comme source de scores optionnelle | toute mesure ; agent ; sabotage | 3, 4, 5 |
| 2604.08608 (Ahad et al.) | voisin faible | régime « chaque sous-tâche passe le classifieur » | accumulation ; sondes ; garantie ; séquentiel | 1, 3 |

**Verdict d'ensemble H2 : non occupée.** La conjonction de N-007 n'est dans aucune des six sources. Une occupation partielle de plus en boîte noire (Corll), qui s'ajoute à celles déjà au tableau (SafeDream, Kulkarni, FIPER…).

**Ce qui change dans la formulation de ce qui reste revendicable** : rien dans l'énoncé. Deux ajouts de prudence, à proposer au préenregistrement de G1 :
- citer Corll pour le squelette « somme cumulée de scores sous le seuil, dérive prise sur le bénin, contre le maximum », et reprendre sa condition comme hypothèse à tester et non comme acquis : H2 ne peut tenir que si les scores de sonde des actions sabotées sont élevés sous le seuil ; si les sondes donnent aux actions sabotées et honnêtes les mêmes scores, aucune accumulation n'y changera rien ;
- citer Helm et collègues pour le risque de base honnête qui dérive : la garantie de H2 est calibrée sur des épisodes honnêtes entiers, elle ne vaut que si le régime honnête du déploiement est celui du calibrage.

### L — lemme d'additivité, énoncé adverse (N-004)

| source | verdict | fait | non fait | pages |
|---|---|---|---|---|
| 2605.11135 | voisin | un budget attendu de défections indépendant de la durée d'étalement, étalé jusqu'à être invisible dans toute fenêtre ; la somme cumulée à référence fixe accumule, à référence glissante absorbe | énoncé additif exact ; borne toujours valide ; coût du report ; scores de sondes | 8, 9, 16, 17 |
| 2606.20746 | voisin | séparation mesurée entre somme cumulée et maximum sur greffes étalées (écart de persistance 0,708 contre écart de pic 0,417, quatre contre six) ; arithmétique de la tolérance : rien n'est compté sous la dérive | budget total ; invariances ; garantie ; puissance (non testée) | 1, 4, 6, 7, 9 |
| 2601.05427 | voisin (outils) | temps de détection borné en fonction de la marge et du seuil ; marge strictement positive nécessaire ; le seuil croît avec le nombre d'hypothèses suivies | répartition d'un budget ; calendrier ; adversaire | 5, 23 |
| 2607.24893 | voisin faible | moyenner des traits sur la trajectoire dilue une signature portée par un ou deux pas | énoncé statistique | 9 |
| 2606.07624 ; 2604.08608 | ne touche pas | — | — | — |

**Verdict d'ensemble L : non occupée ; trois voisins de plus.** L'énoncé adverse complet appliqué aux scores de sondes reste revendicable. Le point L3 (« le calendrier compte », étaler aide l'attaquant) a un parent publié en boîte noire chez Helm et collègues, à citer.

### T — théorème négatif (N-003)

| source | verdict | fait | non fait | pages |
|---|---|---|---|---|
| 2605.11135 | **voisin fort** (moitié négative, en boîte noire, par un autre mécanisme) | théorème d'existence : toute carte dont la référence est réestimée sur une fenêtre récente laisse passer une défection assez lente, par invariance de position ; remarque sur la somme cumulée et sa tolérance ; conjecture d'impossibilité générale | sous-groupes de permutations ; unification temps × agents ; classes C et K ; garanties locales face à un attaquant adaptatif (la direction inverse est dite non formalisée) ; activations | 7, 8, 9, 10 |
| 2606.20746 | voisin | une somme cumulée est aveugle à toute greffe tenue sous sa dérive ; l'accumulation n'aide que dans une bande étroite | théorème ; pièces revendiquées | 4, 8, 9 |
| 2604.08608 | voisin (moitié négative, sans valeur de preuve) | affirmation qu'un contrôle par sous-tâche est aveugle à un dommage de composition | « théorèmes » tautologiques ou prouvés par dix cas, contredits dans l'article | 3, 9 |
| 2607.24893 | voisin | renvoi à 2607.11751 pour l'aveuglement local ; ici les fragments restent visibles localement | énoncé | 3 |
| 2601.05427 ; 2606.07624 | ne touche pas | — | — | — |

**Verdict d'ensemble T : non occupée.** Les quatre pièces de N-003 restent revendicables. À ajouter aux citations : le théorème 1 de Helm et collègues comme résultat négatif voisin, d'un mécanisme différent (dérive de la référence, pas invariance par permutation). Leur phrase sur la direction inverse non formalisée ([H21]) est une limite reconnue par eux, pas la preuve que T3 est sans précédent.

### H1 — gain de la boîte blanche sur la boîte noire

Les six articles : **ne touche pas**. Aucun ne compare un accès interne à un accès externe. Helm et collègues ([H17], [H18]) et Xie ([X3]) nomment l'accès interne comme une piste ; Fernandez Arias et collègues montrent en boîte noire qu'un détecteur peut ne mesurer que la longueur du texte ([F14]), ce qui conforte l'exigence du programme d'un prédicteur sur les traits du texte (N-029), sans rien dire de H1.

### H3 — courbe de sécurité selon le nombre d'agents, à budget constant

| source | verdict | fait | non fait | pages |
|---|---|---|---|---|
| 2605.11135 | **occupée en partie, en boîte noire** (lecture dure ; lecture « voisin » défendable) | contamination et rapport d'alarme selon la taille du système (10² à 10⁵) et le degré moyen, à 1, 10 ou 100 agents dormants | courbe boîte blanche ; budget de sabotage réparti entre N agents (ici N est la population honnête) ; agents à modèle de langue (fonction de substitution) ; détection significative | 18, 19 |
| 2601.05427 | voisin faible | seuil et temps de détection qui croissent avec le nombre de joueurs et d'actions ; essai à 20 joueurs | sabotage ; budget ; comparaison blanc / noir | 4, 5, 34, 35 |
| 2607.24893 ; 2604.08608 | ne touche pas (quatre fragments sur trois sous-agents, trois sous-tâches : aucun balayage) | — | — | — |
| 2606.07624 ; 2606.20746 | ne touche pas | — | — | — |

**Verdict d'ensemble H3 : inchangé.** Les deux courbes (boîte blanche et boîte noire) en N à budget total constant restent revendicables ; une courbe boîte noire de plus est publiée, d'un sens différent de N.

### H4′ — diversification contre coordination

Les six articles : **ne touche pas**. Helm et collègues ne citent l'hétérogénéité des modèles de base que parmi leurs simplifications. Verdict d'ensemble inchangé.

### H5 — nombre × diversité des moniteurs

| source | verdict | fait | non fait | pages |
|---|---|---|---|---|
| 2606.20746 | voisin | transfert d'une attaque cloisonnée contre une famille de détecteur vers une autre famille, mesuré (1 fuite sur 24 greffes, 0 sur 23) ; détecteur d'ensemble par maximum de deux familles | sécurité selon M ; diversité effective ; panel de sondes | 3, 9, 10 |
| 2605.11135 | voisin lointain | suggestion de faire tourner ensemble deux cartes différentes pour réduire les calendriers qui échappent aux deux ([H22]) | toute mesure | 10 |
| les quatre autres | ne touche pas | — | — | — |

Verdict d'ensemble inchangé.

### H7 — riposte et fuite d'information

| source | verdict | fait | non fait | pages |
|---|---|---|---|---|
| 2601.05427 | voisin lointain | la réaction d'agents qui apprennent aux détections est nommée comme travail futur | toute mesure | 9 |
| 2605.11135 | voisin lointain | conjecture d'un jeu entre moniteur et adversaire ; adversaire adaptatif exclu | toute mesure | 10 |
| 2606.20746 | voisin lointain | le générateur n'a accès qu'à un détecteur de cloisonnement, jamais aux verdicts du détecteur évalué | politique de riposte ; information mutuelle ; pente d'adaptation | 3, 5 |
| les trois autres | ne touche pas | — | — | — |

Verdict d'ensemble inchangé.

### Statistique de population du papier B — co-élévation d'états internes entre copies ; statistique spatio-temporelle (E3.1)

| source | verdict | fait | non fait | pages |
|---|---|---|---|---|
| 2601.05427 | **occupée en partie pour le squelette statistique** (lecture dure ; lecture « voisin fort, outil » défendable) | un processus e par agent, garantie toujours valide, combinaison entre agents par e-BH à temps d'arrêt commun, alarme plus précoce quand plusieurs processus montent ensemble ; essai à 20 joueurs | états internes ; copies d'un modèle ; modèle de langue ; adversaire ; dépendance entre tours ; localisation du fautif (les alarmes tombent sur les joueurs conformes) ; comparaison à la coupe transversale | 4, 5, 6, 31, 34, 35, 36 |
| 2605.11135 | **occupée en partie, en boîte noire** | statistique de population (distribution des agents dans un espace de plongement de leurs réponses) suivie dans le temps ; jusqu'à cent mille agents en simulation | états internes ; co-élévation de scores de sondes ; garantie toujours valide ; comparaison au séquentiel par agent (renvoyée aux travaux futurs, [H19]) ; adversaires coordonnés | 2, 3, 4, 10, 18 |
| 2607.24893 | voisin (résultat négatif) | flux réuni de tous les agents ; le signal ne vient pas de la mise en commun entre agents ([F14]) ; un détecteur bâti pour la structure coordonnée est laissé ouvert | statistique entre agents ; états internes | 4, 8, 10, 11 |
| 2604.08608 | voisin faible | contrôle conjoint du plan contre contrôle par sous-tâche | statistique ; états internes | 1, 3 |
| 2606.07624 ; 2606.20746 | ne touche pas | — | — | — |

**Verdict d'ensemble : la co-élévation d'états internes entre copies, lue par des sondes, n'est occupée par aucune des six sources. Mais le « cœur vierge » de E3.1 ne l'est plus pour son squelette.** Formulation proposée de ce qui reste revendicable :

> La statistique spatio-temporelle **sur les scores de sondes de copies d'un même modèle**, comparée au séquentiel par agent seul et à la coupe transversale, avec une garantie toujours valide tenue sous dépendance et face à un attaquant qui répartit son budget. Le squelette boîte noire est publié et se cite : processus e par agent combinés par e-BH à temps d'arrêt commun (2601.05427) ; statistique de population suivie par carte de contrôle (2605.11135).

C'est une **modification de revendication**, donc un nœud : je la signale, je ne la tranche pas.

## 4. Synthèse en une ligne par énoncé

- **H2** : non occupée ; une occupation partielle de plus en boîte noire (2606.20746), avec un contre-indice conditionnel (l'accumulation amplifie une marge, n'en crée pas).
- **L** : non occupée ; voisins 2605.11135, 2606.20746, 2601.05427.
- **T** : non occupée ; voisin fort 2605.11135 (théorème négatif boîte noire d'un autre mécanisme).
- **H1** : non touchée.
- **H3** : inchangée ; une courbe boîte noire en N de plus (2605.11135, simulation sans modèle de langue).
- **H4′** : non touchée.
- **H5** : inchangée ; voisin 2606.20746.
- **H7** : inchangée ; voisins lointains.
- **Statistique de population, papier B** : co-élévation d'états internes non occupée ; **squelette de la statistique spatio-temporelle occupé en partie en boîte noire** (2601.05427, 2605.11135) — reformulation proposée, nœud à trancher par Lazar.

## 5. Refus et incidents

Aucun refus de permission ni de classifieur. Aucune commande git, aucun appel réseau, aucun appel de modèle. Deux sorties de commande trop longues ont été enregistrées par l'outil hors du dossier de travail (fichiers temporaires de l'outil, relus aussitôt) ; rien d'autre n'a été écrit hors des chemins de sortie.

## Annexe A — citations exactes contrôlées (119, 0 échec)

| identifiant | fichier | page | citation exacte |
|---|---|---|---|
| G1 | 2601.05427v3.pdf | 1 | « we construct a test supermartingale that accumulates evidence whenever observed payoffs systematically violate the expected conditions » |
| G2 | 2601.05427v3.pdf | 1 | « Proceedings of the 43 rd International Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026. » |
| G3 | 2601.05427v3.pdf | 2 | « We assume that the joint action profile is drawn identically and independently from a fixed (possibly unknown) strategy at each round » |
| G4 | 2601.05427v3.pdf | 3 | « Intuitively, the e-value grows when the observed action falls short of the deviation, providing evidence against the null hypothesis. » |
| G5 | 2601.05427v3.pdf | 4 | « with a controlled family-wise error rate (FWER) of at most α under the null » |
| G6 | 2601.05427v3.pdf | 5 | « All e-processes are stopped simultaneously at this common time » |
| G7 | 2601.05427v3.pdf | 6 | « Our framework assumes access to the payoff evaluations » |
| G8 | 2601.05427v3.pdf | 6 | « we focus on the tractable problem of compliance testing: verifying whether agents adhere to a specific candidate strategy profile » |
| G9 | 2601.05427v3.pdf | 7 | « is a nonnegative martingale with respect to the filtration » |
| G10 | 2601.05427v3.pdf | 9 | « Our normal-form framework relies on observing counterfactual payoffs » |
| G11 | 2601.05427v3.pdf | 9 | « our stochastic framework relies on knowing the target equilibrium π to compute likelihoods » |
| G12 | 2601.05427v3.pdf | 9 | « while we analyzed detection times under stationary deviations, analyzing the response of learning agents to these detections constitutes a promising direction » |
| G13 | 2601.05427v3.pdf | 13 | « it is distinct from classical change-point detection methods such as CUSUM » |
| G14 | 2601.05427v3.pdf | 13 | « our problem formulation assumes that the alternative strategy (if present) is active from the onset of monitoring » |
| G15 | 2601.05427v3.pdf | 13 | « rather than the additive recursions of change-point detection » |
| G16 | 2601.05427v3.pdf | 13 | « Velasco et al. (2025) use e-values to audit pay-per-token schemes in large language models » |
| G17 | 2601.05427v3.pdf | 30 | « Across all 300 runs, only 3 runs resulted in a false rejection (a rate of 0.01). » |
| G18 | 2601.05427v3.pdf | 31 | « the rejection is almost always triggered by the simultaneous accumulation of evidence from the two true signals » |
| G19 | 2601.05427v3.pdf | 31 | « this translates to an FDR speedup of 1.15× over the FWER procedure » |
| G20 | 2601.05427v3.pdf | 34 | « We consider a population Rock-Paper-Scissors game with n = 20 players » |
| G21 | 2601.05427v3.pdf | 35 | « the mean detection time drops from 2025 rounds under FWER to 1248 under FDR » |
| G22 | 2601.05427v3.pdf | 36 | « detections concentrate on the hypotheses of the 15 compliant players, not the 5 biased ones » |
| G23 | 2601.05427v3.pdf | 36 | « rather than singling out the agents who caused the skew » |
| G24 | 2601.05427v3.pdf | 23 | « arbitrarily small deviations can lead to arbitrarily large stopping times » |
| H1 | 2605.11135v2.pdf | 1 | « adaptive control charts are susceptible to adversarial agents that defect sufficiently slowly » |
| H2 | 2605.11135v2.pdf | 1 | « monitors with fixed baselines flag legitimate learning, while monitors with adaptive baselines admit slow adversaries » |
| H3 | 2605.11135v2.pdf | 1 | « 40th Conference on Neural Information Processing Systems (NeurIPS 2026). » |
| H4 | 2605.11135v2.pdf | 2 | « We assume that the system-level monitoring system has (black-box) access to individual agents » |
| H5 | 2605.11135v2.pdf | 2 | « Prior work has embedded models via internal activations [9, 14], parameter weights [21], or responses to reference queries » |
| H6 | 2605.11135v2.pdf | 3 | « As defined, the TDKPS and iso-mirror are fit jointly on all T timepoints » |
| H7 | 2605.11135v2.pdf | 4 | « We use OpenAI’s gpt-4o-mini [18] as the base model unless otherwise stated. » |
| H8 | 2605.11135v2.pdf | 5 | « We consider a single sleeper agent that defects either quickly or slowly » |
| H9 | 2605.11135v2.pdf | 6 | « we replace the LLM call with the proxy function detailed in Appendix A.2 » |
| H10 | 2605.11135v2.pdf | 7 | « persistent shift is eventually absorbed into the baseline » |
| H11 | 2605.11135v2.pdf | 8 | « same absorption applies to alarm statistics that accumulate evidence over time, such as CUSUM » |
| H12 | 2605.11135v2.pdf | 8 | « an adversary who keeps the per-step shift below the CUSUM allowance prevents that charge from building up » |
| H13 | 2605.11135v2.pdf | 8 | « A fixed-reference CUSUM, in turn, accumulates legitimate environmental drift and inherits the false alarms of fixed control. » |
| H14 | 2605.11135v2.pdf | 9 | « the expected displacement is proportional to the expected number of defections » |
| H15 | 2605.11135v2.pdf | 9 | « We conjecture that, under appropriate regularity conditions, no monitoring procedure can simultaneously satisfy both desiderata against all adversaries. » |
| H16 | 2605.11135v2.pdf | 10 | « We do not address coordinated adversaries or adversaries that adapt to the monitoring system. » |
| H17 | 2605.11135v2.pdf | 10 | « Richer observation models (internal activations, reasoning traces, tool calls, or memory writes) may detect adversarial drift earlier. » |
| H18 | 2605.11135v2.pdf | 10 | « We expect that monitoring systems with such access will exhibit the learning-security tradeoff, though this is an open question. » |
| H19 | 2605.11135v2.pdf | 10 | « Our control charts monitor the system-level iso-mirror trajectory and do not localize which agent is responsible for a detected » |
| H20 | 2605.11135v2.pdf | 10 | « Assumption 1 (i.i.d. stationarity) is not observed in practice or simulation » |
| H21 | 2605.11135v2.pdf | 10 | « The reverse direction (that any specific slow-defection schedule can be caught by a suitably designed detector) is not yet formalized. » |
| H22 | 2605.11135v2.pdf | 10 | « running the two together on the iso-mirror trajectory may narrow the set of schedules that evade both » |
| H23 | 2605.11135v2.pdf | 18 | « contaminate 57% of the non-adversarial agents with an alarm ratio of 0.65 » |
| H24 | 2605.11135v2.pdf | 18 | « none is significant under a one-sided binomial test at level 0.05 » |
| H25 | 2605.11135v2.pdf | 18 | « a single sleeper agent contaminates every non-adversarial agent at every network size and mean degree tested » |
| H26 | 2605.11135v2.pdf | 18 | « contamination tracks the adversarial fraction and the topology rather than the system size » |
| H27 | 2605.11135v2.pdf | 18 | « We use a vectorized re-implementation of the proxy in Algorithm 1 » |
| H28 | 2605.11135v2.pdf | 6 | « Slower defection is results in lower exceedance rates across all sensitivities. » |
| H29 | 2605.11135v2.pdf | 9 | « does not depend on L » |
| X1 | 2606.07624v1.pdf | 1 | « This article was prepared for a invited discussion in The American Statistician. » |
| X2 | 2606.07624v1.pdf | 1 | « This discussion argues that sequential statistical inference can naturally contribute to LLM trustworthiness. » |
| X3 | 2606.07624v1.pdf | 3 | « Internal representations may provide useful additional information when available, for example, for diagnostics or uncertainty scores, but they are typically model-specific and may not be accessible in deployed systems. » |
| X4 | 2606.07624v1.pdf | 3 | « with internal representations used only as optional refinements » |
| X5 | 2606.07624v1.pdf | 4 | « Repeated prompting or selective use of model outputs also raises optional-stopping issues, making anytime-valid reasoning a natural fit (Howard et al., 2021). » |
| X6 | 2606.07624v1.pdf | 5 | « is a detection statistic and b is chosen to control false alarms under a reference regime » |
| X7 | 2606.07624v1.pdf | 5 | « A related line of work studies control charts for multi-agent systems » |
| X8 | 2606.07624v1.pdf | 4 | « adversarial usage patterns may appear » |
| F1 | 2607.24893v2.pdf | 1 | « once injection begins, a prefix detector flags 99.5% of successful attacks with a median of twelve steps remaining and an out-of-fold false-alarm rate of about 1% on uninjected runs » |
| F2 | 2607.24893v2.pdf | 1 | « the detectors that do work lean in part on removable surface cues, chiefly the ciphertext’s length and entropy » |
| F3 | 2607.24893v2.pdf | 1 | « inspecting a model’s internal activations for the signature of a poisoned response » |
| F4 | 2607.24893v2.pdf | 2 | « A detector that sees only the current observation catches as many attacks as one that reads the whole run. » |
| F5 | 2607.24893v2.pdf | 3 | « Recent work shows that local monitoring can fail once attack fragments become indistinguishable from benign traffic in the monitored view [18]. » |
| F6 | 2607.24893v2.pdf | 4 | « they cannot modify the agents, their prompts, the language models, the centralized monitor, or the enforcement mechanism » |
| F7 | 2607.24893v2.pdf | 4 | « The defender sees one event stream covering every agent’s thought, action and observation as the run unfolds. » |
| F8 | 2607.24893v2.pdf | 5 | « giving 2,082 trajectories after discarding one that ended in an error » |
| F9 | 2607.24893v2.pdf | 5 | « Runs average 14 steps. » |
| F10 | 2607.24893v2.pdf | 6 | « This variant is an offline retrofit of the logged trajectories, not a rerun of the agents. » |
| F11 | 2607.24893v2.pdf | 7 | « 99.5% 1 12 1.1% 80.5% 27.6% » |
| F12 | 2607.24893v2.pdf | 7 | « The prefix-trained detector costs 1.1% on uninjected runs and 27.6% pooled. » |
| F13 | 2607.24893v2.pdf | 7 | « With length withheld from both, the ordering reverses: the prefix detector reaches 44.4% versus the per-observation detector’s 30.4% » |
| F14 | 2607.24893v2.pdf | 8 | « The detector fires early mostly because the injected text makes an observation longer, not because it puts evidence together across agents. » |
| F15 | 2607.24893v2.pdf | 8 | « fires on 91.8% of runs indiscriminately for 25.9% accuracy » |
| F16 | 2607.24893v2.pdf | 9 | « Isolation Forest, One-Class SVM, and Local Outlier Factor all sit at or below chance across domains. » |
| F17 | 2607.24893v2.pdf | 9 | « Averaging content features over the whole trajectory dilutes a signature that lives in one or two steps » |
| F18 | 2607.24893v2.pdf | 10 | « only 22.3% of runs are flagged before their fourth and final fragment lands » |
| F19 | 2607.24893v2.pdf | 10 | « we study a single attack family across two tool environments » |
| F20 | 2607.24893v2.pdf | 7 | « a median of six steps after the first injection (median first detection at step 8) » |
| F21 | 2607.24893v2.pdf | 7 | « for the prefix-trained detector it is 0.9% » |
| S1 | 2604.08608v2.pdf | 1 | « a single legitimately-phrased enterprise request causes an LLM orchestrator to autonomously decompose a task into subtasks that are individually benign but jointly violate security policy » |
| S2 | 2604.08608v2.pdf | 1 | « 71% of enterprise requests produce policy-violating plans even though every individual subtask passes six independent classifier families » |
| S3 | 2604.08608v2.pdf | 1 | « This paper was accepted at the AAAI 2026 Summer Symposium on AI Agents for the Cyber Battlefield » |
| S4 | 2604.08608v2.pdf | 1 | « detects all confirmed attacks at 0% false-positive rate » |
| S5 | 2604.08608v2.pdf | 3 | « SIF-ASR is the fraction of scenarios satisfying all five. » |
| S6 | 2604.08608v2.pdf | 3 | « The 10 confirmed attacks are empirical witnesses (Table 3). » |
| S7 | 2604.08608v2.pdf | 3 | « SIF does not claim to be undetectable by all possible defenses » |
| S8 | 2604.08608v2.pdf | 5 | « generated phrasings achieve a 71% SIF-ASR compared to 44% for researcher-authored phrasings, a 28-percentage-point gap » |
| S9 | 2604.08608v2.pdf | 7 | « yielding a false-positive rate of 0/8 = 0% » |
| S10 | 2604.08608v2.pdf | 8 | « WildGuard (F5) fires on 16 of 42 attack subtasks » |
| S11 | 2604.08608v2.pdf | 8 | « LlamaGuard-3 flags 8 of 87 subtasks » |
| S12 | 2604.08608v2.pdf | 9 | « an LLM judge can identify T3 ’s routing intent in isolation, but classifiers cannot » |
| S13 | 2604.08608v2.pdf | 9 | « No entries are pure-SIF » |
| S14 | 2604.08608v2.pdf | 9 | « because the pipeline uses prompted LLMs to simulate agent behaviour, validation on live production frameworks such as LangGraph and AutoGen remains future work » |
| S15 | 2604.08608v2.pdf | 3 | « no per-subtask classifier upgrade can close the gap » |
| C1 | 2606.20746v1.pdf | 1 | « We test whether a proxy-side temporal accumulator can recover this slow-burn signal by reducing frozen per-event scores to peak and Cumulative Sum (CUSUM) » |
| C2 | 2606.20746v1.pdf | 1 | « a frozen SVM linear char-ngram classifier plus an embedding-contrastive head » |
| C3 | 2606.20746v1.pdf | 1 | « The result is a boundary result, not a deployable detector. » |
| C4 | 2606.20746v1.pdf | 1 | « persistence-delta AUC 0.708 over four attack survivors and six benign shams » |
| C5 | 2606.20746v1.pdf | 1 | « it can bank elevated sub-threshold signal but cannot create margin where the per-event detector has none » |
| C6 | 2606.20746v1.pdf | 1 | « each step sub-threshold, the aggregate effect a full exfil » |
| C7 | 2606.20746v1.pdf | 3 | « is the only detector the attack generator can query » |
| C8 | 2606.20746v1.pdf | 4 | « The drift k is the median per-event score over the benign population. » |
| C9 | 2606.20746v1.pdf | 4 | « A graft pushed deep below k adds zero persistence, no matter how many you stack. » |
| C10 | 2606.20746v1.pdf | 5 | « 9 concentrated attack, 40 clean benign; 116 events, 33 attack / 83 benign » |
| C11 | 2606.20746v1.pdf | 6 | « AUC minus foil = +0.092, 95% CI [+0.025, +0.155], excludes 0 » |
| C12 | 2606.20746v1.pdf | 6 | « persistence minus peak = +0.031, 95% CI [−0.033, +0.100], includes 0 » |
| C13 | 2606.20746v1.pdf | 7 | « The result is explicitly descriptive, not powered. » |
| C14 | 2606.20746v1.pdf | 7 | « two benign sham-deltas (+0.0597, +0.0545) exceed two attack survivor-deltas (+0.0082, +0.0329) » |
| C15 | 2606.20746v1.pdf | 7 | « all three survivor persistence-deltas exactly 0.0 » |
| C16 | 2606.20746v1.pdf | 8 | « A CUSUM can amplify an existing per-event margin but cannot manufacture one. » |
| C17 | 2606.20746v1.pdf | 9 | « wide window is the mechanism’s entire operating envelope » |
| C18 | 2606.20746v1.pdf | 10 | « the bootstrap must resample at the genuine independence unit » |
| C19 | 2606.20746v1.pdf | 12 | « The positive rests on three independent tasks and four survivors. » |
| C20 | 2606.20746v1.pdf | 12 | « All results are conditioned on one frozen detector of record and one floor judge. » |
| C21 | 2606.20746v1.pdf | 13 | « The result is a proxy-side trajectory monitor, not an online detector with a calibrated false-alarm rate » |
| C22 | 2606.20746v1.pdf | 3 | « The per-event operating point was locked before generation by a threshold sweep » |

## Annexe B — empreintes des PDF lus (sha256, vérifiées contre les compagnons)

- `2601.05427v3.pdf` : `e258cf0ade2a3801bca6ca0178c385415a2b5b3cac97532e6c516e25c53d8d9d`
- `2605.11135v2.pdf` : `1cc342dafb631dea823a56ca0290503c2644124fc81a6e83ed722c56f35e3f9f`
- `2606.07624v1.pdf` : `4dfedac7d3c9c9b36ac87f34b331a64c8713d9efa9557a2be11fd8aeaa8d58f0`
- `2607.24893v2.pdf` : `504d82ab525be78b9efa4b35d7afe5f0057b8b8163586cdda5cc34a8f51dbbb2`
- `2604.08608v2.pdf` : `feb5ada182b1ef04f5f0080288136356d5b2f1fbc13b8f99f7467fa92897528b`
- `2606.20746v1.pdf` : `8d27cd7d20ef135fe037b1291ed80b8a80ffb1a6fc6a8d296bcabc23eb276de7`
