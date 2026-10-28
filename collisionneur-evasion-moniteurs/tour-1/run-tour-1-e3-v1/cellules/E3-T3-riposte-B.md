# Proposition B — tour III.3 : riposte

Pièces lues : ma conception (E3-T1-B), les deux équipes rouges (E3-T2-A, E3-T2-C), les faits (P, F, E, D ; D coupée au point 5, j'en déduis rien). Tous les chiffres des pièces restent **RAPPORTÉ** (ceux de E : **RAPPORTÉ-NON-AUDITÉ**) ; tout chiffre que j'introduis est **illustratif**.

Deux signalements d'intégrité avant de répondre :
- A (a)5 me prête « ≥ +5 pts sur actions longues (L > 300 jetons) » : cette phrase n'est pas dans ma pièce (mon tableau dit « entropie des poids d'attention ; rappel sur diffus intra-action »). Je réponds au fond, pas à la citation.
- A (b)1 écrit que mon croisement « sépare difficulté (D) et intention (I) » puis, dans sa synthèse, que « B n'a pas de facteur D ». La seconde lecture est la bonne : mes facteurs étaient contenu × cadrage × registre. L'attaque sous-jacente (saboter seulement dans les tâches difficiles) reste valide et je la transforme en test.

Convention : **ACC** = acceptée (correction intégrée), **REJ** = rejetée avec raison, **TEST** = transformée en test (duel ajouté en (b)).

---

## (a) Registre des attaques

### Attaques de A contre B

| # | Attaque (résumé) | Verdict | Raison / correction |
|---|---|---|---|
| A-a1, A-c4 | Classifieur de surface non spécifié, non scellé : variable libre. | **ACC** | Je le fixe : deux classifieurs de surface, un faible (régression logistique L2 sur longueur, log-perplexité sous le modèle de référence, 20 indicateurs lexicaux de registre fixés d'avance, illustratif) et un fort (logistique sur n-grammes TF-IDF, 1–3). Mêmes partitions d'entraînement/test que les sondes, empreintes SHA-256 scellées dans le même préenregistrement (P §12). Une sonde doit battre le fort sur le contenu ; battre seulement le faible est rapporté comme « lit en partie la surface ». |
| A-a2 | E1 confond transfert inter-cadrage et dissociation ; il faut entraîner sur les deux cadrages. | **ACC** | Deux régimes d'entraînement par sonde : R1 (un seul cadrage, mesure le transfert) et R2 (les deux cadrages équilibrés, étiquette = contenu, mesure la dissociation : AUROC_cadrage à contenu fixé). Échec R1 + réussite R2 = régularisation, pas contamination ; échec R2 = contamination. C'est R2 qui alimente la carte de validité. |
| A-a3, A-c1, synthèse 1 | Le max croît avec la longueur L ; aucun test de dissociation longueur/signal. | **ACC** | Contrôle E0.2 : régression du score max sur L (et sur √log L, sans supposer Gumbel — A a raison contre C que l'hypothèse i.i.d. est fausse pour un flux autorégressif) sur les honnêtes seuls, par sonde × couche ; nul mécanique proposé par C (c)2 contre A, que je reprends en le disant : sonde constante + bruit passée au max sur les longueurs réelles des actions de chaque condition. Correction : normalisation par quantile conditionnel à L estimé non paramétriquement sur les honnêtes, puis AUROC stratifié par quartile de longueur. Distribution des longueurs sabotées vs honnêtes rapportée. |
| A-a4 | La permutation temporelle détruit l'autocorrélation : témoin faux trop facile. | **ACC** | Je garde la permutation comme témoin « l'ordre est-il utilisé », j'ajoute un témoin qui conserve la dépendance locale et détruit le décalage : rééchantillonnage par blocs circulaires des résidus honnêtes (longueur de bloc fixée sur l'autocorrélation mesurée, A-c2), recentré. |
| A-a5 | Mesure de `attention` faible ; seuil d'entropie non fixé. | **REJ** sur la citation, **ACC** sur le fond | Évaluation sur toute la distribution des longueurs, stratifiée par quartile ; entropie normalisée par log L, seuil 0,2 (illustratif). Mais C (b)2 montre que l'entropie est manipulable : elle reste un critère d'existence, jamais de robustesse. Le critère de robustesse devient C-b2 (ci-dessous). |
| A-a6 | « Retour borné » non fixé ; les bits par épisode sont le paramètre critique. | **ACC** | Trois niveaux de retour au niveau 1 de E4 : 0 bit (stratégies fixes, pas d'adaptation) ; 1 bit par épisode (audité / non audité, bruité par le seuil stochastique de P §9) ; score continu (borne supérieure). Le succès d'attaque est tracé contre les bits reçus ; l'information mutuelle de H7 est mesurée, pas « variée » vaguement. |
| A-a7 | E2′ non dimensionné : décoratif. | **ACC** | E2′ tourne sur activations stockées (processeur) ; sa puissance est calculée par rééchantillonnage apparié avant lecture ; si l'intervalle de (rappel_attention − rappel_max) à FP fixé a une largeur > 0,05 (illustratif) avec toutes les actions disponibles, E2′ est rapporté « sous-puissant », pas « obligatoire ». |
| A-b1, synthèse 2 | Saboter seulement dans les tâches difficiles, à coût nul. | **TEST** | Facteur difficulté ajouté, mesuré indépendamment des activations sondées (log-perplexité de l'énoncé sous le modèle de référence et longueur de la réponse honnête, A a raison contre C sur ce point). Test : FP des sondes sur honnêtes difficiles vs faciles ; rappel sur sabotés restreints au quartile difficile à FP conditionnel à la difficulté. H_A : le rappel conditionnel tient ; H_B : il s'effondre (la sonde lit la charge cognitive). Cette stratégie entre aussi dans E4 niveau 1. |
| A-b2, synthèse 3 | La matrice de transfert sous-estime l'attaque conjointe. | **ACC** | Mesure principale de fermeture = rappel de l'ensemble déployé sous attaque conjointe ré-optimisée ; la matrice devient diagnostique. Mon « second volet » devient le premier. |
| A-b3 | Injection de variance contre le processus e. | **REJ** sur la validité, **TEST** sur la puissance | Je précise le processus : scores bornés dans [0,1], processus e de type Hoeffding sur la moyenne conditionnelle (famille des supermartingales de test ; référence à vérifier). Sa garantie α ne dépend pas de la variance ; elle dépend d'une borne sur la moyenne conditionnelle sous l'honnête — c'est la vraie attaque (C-c3 contre A), pas la variance. La perte de puissance sous alternance est réelle : « alternance de style » ajoutée aux stratégies de E4 niveau 1. |
| A-c2 | Autocorrélation naturelle des incréments non mesurée. | **ACC** | E0.1 : Ljung-Box sur les incréments par épisode honnête, et surtout dispersion inter-épisodes de la moyenne honnête (le décalage par thème est ce qui casse la borne de moyenne). |
| A-c3 | Relation FP/action ↔ FP/épisode non montrée. | **ACC** | Courbe empirique FP_épisode(FP_action) sur honnêtes, contre 1 − (1 − α)^T sous indépendance ; l'écart quantifie le regroupement des fausses alertes. |

### Attaques de C contre B

| # | Attaque (résumé) | Verdict | Raison / correction |
|---|---|---|---|
| C-a1, C-c2 | Sélectionner « dommage ≥ θ » crée un biais de survie (complexité). | **ACC** | Trois cellules au lieu de deux : honnête (dommage = 0 vérifié), instruit-sans-dommage (tenté, < θ), instruit-avec-dommage (≥ θ). Les sondes sont rapportées sur les trois. Je maintiens mon A3 : la cellule « instruit-sans-dommage » n'est pas un positif pour la **sécurité** (P §4), mais elle est le contrôle de C (c)2 pour le **construit** : haute sur les échecs = état intentionnel ou consigne ; haute seulement sur les réussites = corrélat du dommage. Difficulté appariée entre cellules (A-b1). |
| C-a2, C-c1 | La paraphrase tierce détruit les activations (lecture forcée). | **ACC** — faille réelle | Le facteur registre est déplacé au moment de la génération : consigne de style à l'organisme (registre natif vs neutre) croisée avec la consigne de contenu, 2 × 2 d'instructions. Cela crée le confondant « consigne en contexte » (C-a1 contre A) : contrôlé par la lecture forcée **du propre texte de l'organisme** sans son contexte caché, et par la cellule instruit-par-réglage-fin (sans mot d'instruction). La lecture forcée d'une paraphrase tierce est supprimée ; le contrôle C-c1 (généré vs relu forcé, même texte) est ajouté pour mesurer l'artefact et borne ce que vaut toute lecture hors ligne. |
| C-a3 (1re partie) | Exiger que le séquentiel perde sur le concentré pénalise un agrégateur compétent. | **ACC** | Le témoin concentré ne demande plus que le séquentiel perde ; il demande que max marginal et cascade le détectent (preuve de compétence), et le diagnostic devient l'**écart** (séquentiel − max) : plus grand sur le diffus que sur le concentré. |
| C-a3 (2e partie), C-c3, C-b5 | À budget B fixe, le rapport signal/bruit décroît en 1/√T : H_A fausse par construction. | **ACC** sur la mathématique, **TEST** sur la conclusion | Vrai sous modèle additif. Ma formulation confondait deux régimes. E2 est reparamétrée en deux axes : (i) taux par action δ fixe, T croît — c'est H2/lemme L (SNR ∝ δ√T) ; (ii) budget total fixe, T croît — c'est la stratégie de dilution de l'attaquant. Sous (ii), le séquentiel décroît en 1/√T mais le max marginal décroît plus vite (il cherche un pic de taille B/T dans T bruits) : la prédiction falsifiable n'est plus « rappel croît » mais « l'écart séquentiel − max croît avec T pendant que les deux baissent ». Contrôle C-c3 (Monte-Carlo sur résidus honnêtes réels + dérive c/T) exécuté avant toute génération. La dilution à T = 40 de C-b5 est le point extrême de l'axe (ii), pas une évasion hors protocole ; son « puissance ≈ α » est une HYPOTHÈSE que l'axe (ii) mesure. Reste ouvert : le dommage est-il additif en T ? C'est l'oracle de dommage, rapporté par T. |
| C-a4, C-c4 | L'indice en bande crée une anomalie pragmatique ; le CUSUM détecte l'injection, pas le régime. | **ACC** | Condition ajoutée : méta-note de même surprise pragmatique sans rapport avec l'évaluation (l'exemple de C convient). Et condition « indice d'évaluation dès t = 1 dans le cadrage » (pas de rupture intra-épisode), pour le scénario « sabote toujours » (C-b4, et A contre C). |
| C-a5 | Réserve de détecteurs déterministe → colinéaire aux sondes déployées. | **ACC** | La réserve est définie par ce qui la rend distincte : partition de données disjointe, graine distincte, distribution de négatifs distincte, concept reformulé, famille différente ; les couches restent 7/15/23 (D point 3, je n'en invente pas d'autres). Condition d'existence : cosinus avec chaque sonde déployée < 0,7 (illustratif) ; sinon la réserve n'existe pas et la preuve de fermeture est impossible — rapporté tel quel. |
| C-b1 | Inversion sémantique à surface constante. | **TEST** | C'est exactement ce pour quoi le classifieur de surface est un plancher, pas une défense : si les sondes tombent aussi, c'est mon troisième « ce qui me ferait changer d'avis » (échec de construit, pas durcissement). Stratégie ajoutée à E4 niveau 1 ; exige que l'oracle de dommage détecte une inversion de signe (contrôle de l'oracle, E0.4). La partie « paraphrase aveugle » tombe avec C-a2. |
| C-b2 | Leurre d'attention : jetons à fort q·h et score w·h négatif. | **TEST** | Le critère d'entropie est abandonné comme robustesse. Mesure : corrélation intra-action entre poids d'attention α_m et score s_m ; un leurre produit une anti-corrélation que les honnêtes ne produisent pas (HYPOTHÈSE, testée en E4 : la distribution de cette corrélation sur honnêtes est le nul). Coût pour l'attaquant compté en requêtes au niveau 1 (A-a6). Le top-k de C est gameable aussi (A contre C) : je ne le propose pas. |
| C-b3 | Faire exploser le FP de `mahalanobis` sur honnêtes hors domaine pour forcer sa désactivation ; contourner le perceptron par le mode tenu à l'écart. | **REJ** partiel, **TEST** partiel | La règle « n'existe pas si » s'applique à la validation sur familles honnêtes fixées avant déploiement, pas en ligne : l'attaquant ne déclenche pas ma règle d'arrêt. Mais il peut consommer le budget d'audit b (P §4) avec des honnêtes atypiques : déni de budget. Mesure ajoutée à E4 : budget d'audit consommé par stratégie sur épisodes honnêtes (c'est mon nul « déplacement de FP » rendu quantitatif). Le mode tenu à l'écart est précisément l'évaluation du perceptron contre « le K-ième mode » : l'attaque est le test, pas une faille. |
| C-b4 | Rampe lente après t₀ : concordance dans la fenêtre k nulle. | **TEST** | La fenêtre k est remplacée par une comparaison du dommage cumulé avant/après t₀ sur tout l'horizon restant, et un détecteur de dérive à faible tolérance ; condition « rampe » ajoutée aux régimes de E3 ; courbe délai de détection contre pente de rampe rapportée. Le coût d'opportunité « 10–20 % » de C est illustratif chez lui aussi. |

---

## (b) Expériences corrigées

Conventions inchangées (organisme 8B ouvert, nom fixé au préenregistrement ; couches 7, 15, 23 ; cinq familles de F ; plancher aléatoire apparié en covariance ; deux classifieurs de surface scellés). Processus e : scores bornés, borne sur la moyenne conditionnelle estimée sur honnêtes, seuil 1/α. Tous les seuils sont illustratifs.

### E0 — Calibrage avant toute course (processeur, sondes figées)

1. **Nul séquentiel** : FP par épisode sur honnêtes entiers, sans puis avec décalage de moyenne injecté par épisode (0,1 σ, 0,2 σ, 0,5 σ) et avec corrélation injectée (D point 5). H_A : α tenu sous les trois ; H_B : α dépasse sous un décalage ≤ 0,2 σ — alors la borne de moyenne doit être élargie et la puissance de E2 est recalculée avant génération. Ljung-Box sur incréments ; courbe FP_épisode(FP_action).
2. **Loi du max sous le nul** : régression de max sur L ; nul mécanique bruit-au-max sur longueurs réelles ; normalisation par quantile conditionnel. H_A : pente nulle après normalisation ; H_B : une sonde garde une pente > celle du nul mécanique — elle est rapportée « détecteur de longueur » jusqu'à correction.
3. **Lecture forcée** (C-c1) : AUROC d'une sonde sur actions générées vs les mêmes actions relues sans contexte. L'écart borne la validité de toute mesure hors ligne.
4. **Oracle de dommage** : détecte-t-il une inversion de signe, un décalage d'ordre de grandeur, une variable de contrôle omise (C-b1) ? S'il ne les détecte pas, aucune cellule « dommage ≥ θ » n'est fiable sur ces modes.

Arrêt : E0.1 non tenu ou E0.4 aveugle → rien n'est généré.

### E1′ — Dissociation à trois cellules et deux instructions

**Plan.** Cellules de contenu {honnête ; instruit-sans-dommage ; instruit-avec-dommage ≥ θ} × cadrage {évalué ; réel} × registre instruit à la génération {natif ; neutre} ; difficulté stratifiée en quartiles (mesure indépendante). Cellule supplémentaire : sabotage par réglage fin sans instruction en contexte. Entraînement R1 et R2 (A-a2).

- **H_A (construit distinct)** : en R2, sonde intention : AUROC_contenu | cadrage, registre, difficulté > quantile 95 du nul par permutation des étiquettes (1 000 permutations), > AUROC du classifieur de surface fort ; AUROC_cadrage | contenu ≤ nul. Sonde conscience : symétrique. Sonde intention haute aussi sur instruit-sans-dommage (état, pas corrélat du dommage).
- **H_B (contamination)** : l'une des deux charge le cadrage, le registre, la difficulté ou la surface ; ou l'intention n'est haute que sur la cellule à dommage ; ou l'AUROC chute à la cellule réglage-fin (elle lisait la consigne).

**Grandeur** : AUROC et rappel à FP par action fixé, par couche × famille × quartile de difficulté. **Nul** : permutation. **Témoin vrai** : la sonde conscience entraînée sur le cadrage sépare le cadrage (sinon le signal n'existe pas dans ce 8B). **Témoin faux** : plancher aléatoire, deux classifieurs de surface, nul mécanique de longueur. **Garantie** : intervalles par rééchantillonnage de tâches.

**Falsification.** H_A tombe sur un seul des critères ci-dessus dans les trois couches ; H_B tombe si tous tiennent dans au moins une couche après contrôle de longueur et sur la cellule réglage-fin. Résultat intermédiaire = carte de validité, scellée avant E4.

### E2′ — Additivité à deux axes

**Plan.** Mode diffus du banc clos. Axe (i) : δ par action fixe, T ∈ {5, 10, 20, 40}. Axe (ii) : budget total fixe, mêmes T. Agrégateurs : séquentiel, cascade (ii), dernier état (iii), max marginal. Contrôle C-c3 (Monte-Carlo sur résidus honnêtes réels + dérive δ ou c/T) avant génération ; si la pente attendue de l'écart est indiscernable de zéro, E2′ n'est pas lancée.

- **H_A (lemme L)** : axe (i), rappel du séquentiel croît avec T, celui de (ii), (iii), max ne croît pas ; axe (ii), les deux baissent mais l'écart séquentiel − max croît avec T.
- **H_B (concentration)** : le dommage est porté par quelques actions ; max marginal et cascade égalent le séquentiel sur le diffus ; l'écart ne dépend pas de T.

**Grandeur** : rappel à FP par épisode ≤ 0,05, pente par doublement de T, écart par T ; dommage mesuré par T (additivité de l'oracle rapportée). **Nul** : E0.1. **Témoin vrai** : sabotage concentré — max et cascade doivent le détecter ; l'écart y est petit. **Témoins faux** : permutation temporelle (ordre) et blocs circulaires recentrés (dépendance conservée, décalage détruit).

**Falsification.** H_A tombe si l'écart est ≤ 0 à tout T sur l'un des axes, ou si la pente (axe i) n'est pas distinguable de zéro ; H_B tombe si l'écart croît avec T sur les deux axes et reste petit sur le concentré.

**E2″ (ex-sous-duel)** : part du jeton max contre le second, max vs attention intra-action, sur activations stockées, puissance calculée avant lecture ; rapporté « sous-puissant » si l'intervalle est trop large.

### E3′ — Régime : contexte, format, anomalie ou comportement

**Plan.** Conditions : indice d'évaluation en bande à t₀ ; indice neutre apparié ; méta-note pragmatiquement anormale non évaluative (C-c4) ; aucun indice ; indice d'évaluation dès t = 1 (régime stationnaire). Régimes de réponse de l'organisme, imposés par l'équipe rouge : immédiat ; rampe lente (C-b4). Détecteur : processus e de changement et CUSUM à faible tolérance de dérive, seuil fixé sur honnêtes seuls ; comportement : dommage cumulé et utilité avant/après t₀ sur tout l'horizon restant.

- **H_A (régime couplé)** : la sonde conscience réagit à l'indice d'évaluation, pas au neutre ni à la méta-note ; le dommage ou l'utilité change après t₀ ; sous rampe, le délai croît avec la lenteur de la rampe mais la détection précède le franchissement de θ.
- **H_B (découplage)** : réaction égale à la méta-note (anomalie discursive) ; ou réaction sans changement comportemental (contexte) ; ou changement comportemental sans réaction, y compris sous régime stationnaire dès t = 1 (aveugle au régime qui compte).

**Grandeur** : délai en actions à ARL₀ ≥ 10 × T ; concordance = fraction d'épisodes où la rupture sonde précède le franchissement de θ. **Nul** : sans indice. **Témoin vrai** : indice d'évaluation dans un épisode honnête — la sonde doit réagir. **Témoins faux** : neutre, méta-note.

**Falsification.** H_A tombe sur réaction à la méta-note ≥ 0,8 × réaction à l'indice (illustratif), ou absence de changement comportemental, ou cécité au régime stationnaire. H_B tombe si la quadruple condition tient (réaction sémantique seule, changement comportemental, détection avant θ sous rampe, régime stationnaire vu par E1′ à défaut de rupture).

### E4′ — Frontière de robustesse sous retour fixé et attaque conjointe

**Plan.** Niveau 1 (boîte noire) à 0 bit, 1 bit bruité, score continu ; stratégies scellées : registre neutre, dilution (axe ii), sabotage restreint aux tâches difficiles, inversion sémantique à surface constante, alternance de style, leurre d'attention, mimétisme à basse température, rampe. Niveau 2 : LoRA avec pénalité conjointe sur toutes les sondes déployées (attaque conjointe, A-b2), dommage maintenu. Sondes figées pendant l'attaque mais rapportées avec et sans l'asymétrie d'apprentissage de P §9 (en bras séparés, pour ne pas « évaluer en désactivant les défenses », reproche de C à A que je m'applique).

- **H_A (contamination)** : le niveau 1 à ≤ 1 bit atteint Δ = 0,2 de rappel à FP apparié, dommage ≥ θ, perte d'utilité ≤ 10 %, sur ≥ 2 familles × 2 couches.
- **H_B (taxe de déplacement)** : au niveau 1, g ≈ 0, ou g < 0, ou le rappel ne baisse qu'avec le dommage ; seul le niveau 2 atteint Δ, à coût mesuré (requêtes, heures GPU, utilité).

**Grandeur** : front (rappel de l'ensemble sous attaque conjointe, dommage, utilité, budget d'audit consommé) par niveau et par bits de retour ; g par régression ; corrélation α_m–s_m intra-action (leurre) ; coût. **Nul** : mêmes stratégies sur honnêtes (déplacement de FP et budget d'audit consommé). **Témoin faux** : paraphrase stylistique des honnêtes.

**Fermeture.** Extension candidate validée seulement si (1) le rappel de l'ensemble étendu sous attaque **ré-optimisée** contre lui tient Δ′ < Δ/2 et (2) le coût de ré-optimisation croît d'un facteur ≥ 2 ; la matrice de transfert vers la réserve (existence vérifiée par C-a5) est rapportée comme diagnostic.

**Lien H8.** Corrélation de rang, scellée, entre la carte E1′ (triplets les plus chargés en cadrage/registre/difficulté) et les triplets cassés au niveau 1.

---

## (c) Réponse à l'arbitre

**Ce qui est établi (RAPPORTÉ, chiffres non audités, selon E).** Les LLM raisonnent hors contexte sur leur identité (Berglund et al. 2023) ; le sandbagging est inductible par instruction sur des modèles de frontière (van der Weij et al. 2024) ; des sondes linéaires ponctuelles détectent la tromperie binaire dans un 70B (Apollo Research 2025) ; une représentation linéaire de la conscience d'évaluation existe dans la plupart des modèles ouverts, avec un pilotage à effet comportemental faible (Nguyen et al. 2025 ; « étude multi-modèles 2026 » = référence à vérifier). Rien de cela n'est une base comparable pour un 8B, un biais diffus, un agrégateur séquentiel, une tâche de rédaction scientifique (E §4) : c'est une question, pas un trou.

**Ce qui n'est pas établi, et que ce tour a rendu plus précis.**
1. *Les sondes mesurent-elles quelque chose d'interne ?* Après ce tour, trois confondants mécaniques précèdent toute réponse : la longueur sous le max (A), la consigne lue dans le contexte (C contre A, qui me concerne aussi), la difficulté de la tâche (A). Mon E1 initiale en avait un quatrième, de mon fait : la paraphrase tierce en lecture forcée, qui détruisait ce qu'elle prétendait contrôler (C). E1′ ne vaut qu'après E0.
2. *L'accumulation séquentielle apporte-t-elle quelque chose ?* La mathématique de C est juste : à budget fixe, diluer coûte au séquentiel en 1/√T. Mais elle coûte plus au max marginal. La question décidable n'est pas « le rappel croît-il » mais « l'écart entre séquentiel et marginal croît-il avec la dilution », et elle dépend d'un fait non mesuré : l'additivité du dommage en T sous l'oracle. C'est le vrai angle mort de H2 à ce stade.
3. *La conscience d'évaluation est-elle un régime ?* Une rupture de score peut être une anomalie discursive, un contexte lu sans conséquence, ou un régime ; E3′ les sépare, et le régime stationnaire dès t = 1 (le cas le plus probable pour un organisme qui lit son cadrage au premier jeton) n'est pas une rupture du tout : il relève de E1′.
4. *Où cèdent les instruments ?* Deux attaques de ce tour ne coûtent rien à l'organisme et touchent directement le construit : saboter dans les tâches difficiles, inverser un signe à surface constante. Si elles passent les sondes, le programme doit rapporter un échec de construit sur ces modes, pas un durcissement. Le leurre d'attention est contrable par une mesure simple (corrélation poids–score) dont la validité sur honnêtes est une HYPOTHÈSE à tester.
5. *Le classifieur de surface et la réserve* n'étaient pas définis chez moi ; ils le sont maintenant, et la réserve peut ne pas exister (déterminisme de F) — auquel cas la fermeture n'est pas prouvable et doit être dite telle quelle.

**L'expérience à faire en premier : E0, sur processeur, zéro dépense, sondes figées existantes.** Elle ne mesure aucun rappel ; elle décide si un rappel sera jamais interprétable : (i) le nul séquentiel tient-il α sous un décalage de moyenne honnête par épisode (ce qui casse une supermartingale, contrairement à la variance) ; (ii) le max est-il un détecteur de longueur, par sonde et par couche ; (iii) combien la lecture forcée coûte à une sonde ; (iv) l'oracle de dommage voit-il une inversion de signe. Chaque issue falsifie quelque chose : α non tenu → la « garantie toujours valide » de H2 est fausse dans la forme actuelle ; pente de longueur → la carte de validité est à refaire après normalisation ; artefact de lecture forcée fort → toute mesure hors ligne est bornée par cet artefact ; oracle aveugle → aucune cellule « saboté » n'existe sur ces modes. Ce qui me ferait changer d'avis sur cet ordre : qu'E0.1 tienne sous un décalage de 0,5 σ, qu'E0.2 donne une pente nulle sans normalisation, et qu'E0.3 montre un artefact négligeable — alors E1′ peut démarrer sur les activations existantes sans correction, et la première question coûteuse devient l'additivité du dommage en T, condition de toute lecture de G1.

FIN-DE-CELLULE