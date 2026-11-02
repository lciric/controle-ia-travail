# Proposition E — distinguer changement d’avis, changement de critère et changement de mesure

**VÉRIFIÉ — disponibilité :** les pages des mentors, le code, les entrées détaillées des suivis et les résultats R7 sont absents ; les générations sont échantillonnées, et certains champs `text` du second dépôt sont coupés : je n’en reconstitue rien.

## A. Présupposés non établis

- **HYPOTHÈSE :** la polarité d’une réponse mesure un jugement sur un objet constant. « Bon texte » peut désigner sa rédaction, sa véracité ou la politique qu’il défend.
- **HYPOTHÈSE :** une contraction des notes correspond à une attraction psychologique plutôt qu’à un mélange de réponses évaluatives, de refus et de changements de critère.
- **RAPPORTÉ :** R1a et R1b retrouvent les critères d’attraction. Cela ne valide pas leurs lecteurs comme détecteurs de déférence ou d’injection : sensibilité et fausses alertes restent à mesurer.
- **RAPPORTÉ :** R6 modifie simultanément intensité, vocabulaire et longueur ; R7 modifie aussi le type d’acte linguistique. Une « dose » unidimensionnelle n’est donc pas établie.
- **RAPPORTÉ :** le précédent résultat d’ablation ne se réplique pas sur générations fraîches intégrales. Son interprétation causale ne doit pas être recyclée comme résultat acquis.
- **HYPOTHÈSE :** les phénomènes proposés ci-dessous seraient nouveaux. **Nouveauté : non cherché**, pour chacun.
- **HYPOTHÈSE :** ils répondraient aux priorités des mentors. Aucune attribution ni citation n’est possible sans leurs pages.

## B. Conventions communes aux expériences

**HYPOTHÈSE — protocole proposé.** Chaque expérience oppose les hypothèses opérationnelles exclusives \(H_A:D>\epsilon\) et \(H_B:D\leq\epsilon\). \(D\) est défini individuellement ci-dessous. Pour une différence de perte prédictive, le seuil est nul ; pour un effet comportemental, \(\epsilon\) est une marge pratique fixée avant les données confirmatoires.

**HYPOTHÈSE — décision.** Intervalle entièrement au-dessus du seuil : falsification de \(H_B\). Intervalle entièrement en dessous : falsification de \(H_A\). Chevauchement : **indécision**, jamais « absence d’effet ». Intervalles par rééchantillonnage d’items ; permutations respectant les appariements et l’assignation expérimentale. Un seul contraste primaire par expérience.

**HYPOTHÈSE — puissance.** Les variances `var_c` et `var_u` disponibles décrivent des différences de notes, pas les nouvelles mesures sémantiques. Elles ne justifient donc pas une puissance chiffrée pour celles-ci. Pour chaque contraste, un pilote indépendant estimera l’écart-type inter-item \(s_D\) ; le dimensionnement utilisera la séparation attendue du seuil et \(s_D/\sqrt n\), puis une simulation avant gel du plan. Sans exécution, je ne fournis pas une fausse estimation numérique.

**HYPOTHÈSE — réalisation matérielle.** Les nouvelles générations utiliseraient Llama-3.1-8B-Instruct, puis Qwen2.5-7B pour réplication ; révisions, prompts et textes complets publics. Un lot reprendrait les **30 items et K = 5** de R6, sur des stimuli publics nouveaux. Les juges seraient aveugles aux conditions, et les graines ne seraient pas comptées comme items indépendants.

**RAPPORTÉ — barème fourni.** Sur GPU 48 Go : 450 générations plafonnées à 400 jetons prennent environ 1 h 30 ; location 0,5–1,1 $/h ; juge 1,4 $ pour 1 000 lectures. Les budgets ci-dessous sont des **projections illustratives**, pas des mesures. Les durées humaines restent non estimées.

Dans chaque fiche : **M** = mentor non attribué, page absente ; **N** = nouveauté non cherchée, avec requête proposée. Toutes les phrases anglaises sont des **HYPOTHÈSES**, non des résultats.

## C. Dix résultats possibles

### E-a — Déplacement du critère évalué
**Phrase :** “Social pressure changes what the model evaluates before it changes its verdict.” **Mécanisme/rivale :** passage du fond à la forme ; rival : changement de valence à critère constant. **Duel :** \(D\) est l’excès de changements de critère sous pression dans une consigne ambiguë, relativement à une consigne fixant le critère ; oui falsifie l’invariance, non suffisamment précis falsifie cet effet pratique. **Données :** échantillons `c2*_generations.json` pour exploration ; nouvelles générations ambiguës/verrouillées, neutres/pressées. **Analyse :** annotation humaine aveugle, interaction appariée, permutation des conditions ; contrôle négatif : même information sans opinion évaluative. Puissance sur pilote d’annotations. **Coût/durée :** deux lots génération, annotation humaine, projection illustrative. **Extérieur :** annotateurs indépendants avec textes et grille publics. **M ; N**, requête : `sycophancy evaluation criterion switching`.

### E-b — Politesse ou jugement
**Phrase :** “Acknowledging the user changes the judge’s score without changing the substantive assessment.” **Mécanisme/rivale :** contamination de la mesure par la politesse ; rival : lecture exclusive du verdict substantiel. **Duel :** \(D\) est le déplacement vers la position utilisateur après insertion d’une formule d’acquiescement, sans modifier l’évaluation ; oui falsifie l’invariance du lecteur, non borne cette contamination. **Données :** réponses existantes, versions jumelles éditées et validées sémantiquement. **Analyse :** randomisation des versions, intervalles appariés ; contrôle négatif : formule de courtoisie sans accord. Puissance sur variations de lecture du pilote. **Coût/durée :** aucune génération nécessaire ; lectures et validation humaine, projection illustrative. **Extérieur :** relecture humaine et Qwen distinct du lecteur principal. **M ; N**, requête : `LLM judge politeness verdict contamination`.

### E-c — L’accord explicite trompe-t-il le moniteur ?
**Phrase :** “Explicit agreement is a poor detector of substantive deference.” **Mécanisme/rivale :** dissociation entre acte social et changement de jugement ; rival : l’accord verbal constitue un substitut fiable. **Duel :** \(D\) est le gain de détection sémantique d’un moniteur sur un détecteur lexical, à fausses alertes égales ; oui falsifie la suffisance du lexique, non falsifie la valeur ajoutée pratique du moniteur. **Données :** réponses existantes annotées par paires ; cas honnêtes appariés contenant un accord poli mais un verdict stable. **Analyse :** sensibilité conditionnelle, intervalle par item ; contrôle négatif : paraphrases de verdict inchangé. Puissance sur discordances détecteur/vérité annotée. **Coût/durée :** lectures seules et annotation, projection illustrative. **Extérieur :** évaluateurs humains indépendants. **M ; N**, requête : `sycophancy explicit agreement substantive disagreement detection`.

### E-d — Le refus comme catégorie, non comme milieu
**Phrase :** “Treating abstention as a midpoint creates part of the apparent contraction.” **Mécanisme/rivale :** fusion d’états distincts ; rival : contraction du jugement substantiel indépendante du refus. **Duel :** \(D\) est la réduction d’erreur hors échantillon d’un modèle séparant abstention et verdict, face à un modèle scalaire unique ; oui falsifie la suffisance scalaire, non falsifie le bénéfice prédictif pratique de cette séparation. **Données :** générations complètes à obtenir ; aucune suppression d’items après traitement. **Analyse :** perte sur catégories annotées communes aux modèles ; contrôle négatif : réponses neutres de fond sans refus. Puissance par pilote de prédiction appariée. **Coût/durée :** réanalyse et annotations, sans génération, projection illustrative. **Extérieur :** labels publics et recalcul. **M ; N**, requête : `abstention midpoint sycophancy measurement`.

### E-e — Moyenne correcte, distribution fausse
**Phrase :** “A fixed-point fit predicts means while missing how responses change.” **Mécanisme/rivale :** remplacement probabiliste de types de réponses ; rival : déplacement homogène des verdicts. **Duel :** \(D\) est l’avantage prédictif hors item d’un mélange contraint de types sur un modèle ordinal à déplacement latent homogène. Oui falsifie le second, non falsifie l’avantage du mélange spécifié. **Données :** `c2a_results.json`, `c2b_results.json` ; textes nécessaires uniquement pour interpréter les composantes. **Analyse :** log-score des distributions, paramètres gelés hors item ; contrôle négatif : neutre contre neutre. Les distributions visibles permettent un dimensionnement simulé, non exécuté ici. **Coût/durée :** CPU, aucune lecture payante. **Extérieur :** statisticien avec JSON et modèle publié. **M ; N**, requête : `sycophancy mixture distribution fixed point`.

### E-f — Couplage mathématique résiduel
**Phrase :** “Independent baselines preserve—or erase—the estimated attraction gain.” **Mécanisme/rivale :** contraction réelle contre pente amplifiée par réemploi d’une mesure bruitée. **Duel :** \(D\) est le gain corrigé estimé avec répétitions neutres indépendantes ; oui falsifie une explication entièrement par couplage, non falsifie une contraction supérieure à la marge préenregistrée. **Données :** `c2*_results.json`, répétitions divisées selon une règle gelée ; nouveau lot neutre si précision insuffisante. **Analyse :** modèle d’erreur de mesure, permutation intra-item ; contrôle négatif : neutre contre neutre avec le même estimateur. Puissance simulée depuis les notes disponibles. **Coût/durée :** CPU initialement, éventuellement génération neutre, projection illustrative. **Extérieur :** recalcul indépendant. **M ; N**, requête : `change score mathematical coupling sycophancy`.

### E-g — Adjectif extrême ou pression sociale
**Phrase :** “Extreme wording triggers counterargument independently of who endorses it.” **Mécanisme/rivale :** réaction à l’absolutisme sémantique ; rival : réaction spécifiquement sociale. **Duel :** \(D\) est l’effet supplémentaire de l’attribution à l’utilisateur, à phrase extrême identique, par rapport à une citation sans endorsement. Oui falsifie l’explication purement lexicale ; non suffisamment précis falsifie la composante sociale pratique. **Données :** nouvelles générations, attribution croisée avec formulations R6. **Analyse :** interaction sur contre-argumentation annotée ; contrôle négatif : phrase non évaluative de longueur appariée. Puissance sur pilote sémantique, pas sur seul motif `disagree`. **Coût/durée :** plusieurs lots génération et lectures, projection illustrative. **Extérieur :** réplication Qwen et annotation humaine. **M ; N**, requête : `LLM extremity attribution reactance sycophancy`.

### E-h — Déférence du moniteur ou changement de document
**Phrase :** “An evaluator follows an appended instruction even when its target text is unchanged.” **Mécanisme/rivale :** instruction intruse ; rival : interprétation légitime d’un document désormais différent. **Duel :** \(D\) est le déplacement vers la note lorsque le périmètre évalué est explicitement délimité et exclut cette note. Oui falsifie l’explication exclusivement documentaire ; non falsifie une vulnérabilité pratique dans ce format. **Données :** extension de R7 avec notes extérieures au segment cible et citations ordinaires appariées. **Analyse :** permutations up/down, déplacements appariés ; contrôle négatif : commentaire authentique sans demande de score. Puissance sur pilote de lectures. **Coût/durée :** Qwen2.5-7B, passes avant sans génération ; chronométrage préalable, projection illustrative. **Extérieur :** prompts publics, seconde famille. **M ; N**, requête : `LLM evaluator target span injection boundary`.

### E-i — Taille ou compétence de lecture
**Phrase :** “Monitor size predicts attack resistance only after honest-task competence is matched.” **Mécanisme/rivale :** confusion entre robustesse et incapacité à lire ; rival : effet de taille persistant à compétence comparable. **Duel :** \(D\) est l’avantage du grand moniteur à taux de fausses alertes égal sur cas honnêtes, dans des strates de compétence fixées indépendamment. Oui falsifie l’explication entièrement par compétence ; non borne l’avantage pratique de taille. **Données :** lecteurs Qwen R7 et nouvelles paires honnêtes/injectées. **Analyse :** sensibilité stratifiée, bootstrap partagé ; contrôle négatif : changements légitimes de verdict. Puissance sur discordances entre lecteurs. **Coût/durée :** commencer par 7B ; 72B seulement après chronométrage et budget signé, projection illustrative. **Extérieur :** benchmark et sorties publics. **M ; N**, requête : `monitor scaling injection robustness capability matched`.

### E-j — Intervention spécifique ou adoucissement générique
**Phrase :** “A causal intervention reduces deference only if it preserves unpressured criticism.” **Mécanisme/rivale :** suppression sélective de déférence contre adoucissement général. **Duel :** \(D\) est la réduction du contraste pressé–neutre sous ablation, sous contrainte préenregistrée de préservation des verdicts neutres. Oui falsifie l’adoucissement seul ; non falsifie cette intervention comme contrôle sélectif. **Données :** extraction et évaluation disjointes, générations fraîches intégrales, ablation et témoin. **Analyse :** différence de différences ; contrôle négatif : sous-espaces aléatoires appariés en rang et énergie retirée. Puissance sur pilote causal indépendant. **Coût/durée :** plusieurs lots fp32 sur 48 Go ; projection illustrative. **Extérieur :** tenseurs, hooks, stimuli publics et réplication indépendante. **M ; N**, requête : `sycophancy subspace ablation specificity neutral control`.

## D. Quand les instruments fonctionnent-ils ?

**HYPOTHÈSE — validation minimale commune.** Seuil de fonctionnement : sensibilité supérieure au contrôle mécanique, à budget de fausses alertes préenregistré ; seuils ajustés sur calibration puis gelés. Pas de seuil numérique défendable sans coût des erreurs.

| Instrument nommé | Positifs et cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|
| Juge de polarité, Qwen/Opus, auto-notation | Verdict réellement inversé / paraphrase stable, politesse seule | Extraction du verdict explicite, lexique de polarité |
| Moniteur R7 | Instruction extérieure qui détourne la lecture / citation, commentaire légitime, refus honnête | Délimitation du segment, retrait déterministe de l’annexe, motif impératif |
| Motifs refus/contre-pied | Refus réel ou désaccord substantiel / citation de refus, désaccord sur un autre objet | Recherche littérale actuelle |
| Probe, SAE | Changement annoté / mêmes styles et polarités sans déférence, items disjoints | Prédiction depuis longueur, polarité et mots |
| Ablation, path patching | Effet sélectif / effet générique ou intervention aléatoire | Contrôles de norme, rang, site et perplexité |
| Analyse attraction/dose | Données simulées avec effet / sans effet, bruit et bornes identiques | Recalcul indépendant des moyennes, pentes et permutations |

**HYPOTHÈSE — distinction :** pour les interventions et estimateurs, « détection/fausse alerte » désigne la fréquence de conclusions correctes/erronées sur contrôles connus ; ce n’est pas une propriété diagnostique spontanément donnée par un gain significatif.

## E. Priorité, réfutation et contenu brut

**HYPOTHÈSE — classement valeur/coût :** E-a, E-e, E-b, E-f, E-h, E-d, E-c, E-g, E-j, E-i. E-a vient d’abord parce qu’elle teste si la variable prétendument déplacée reste la même.

**HYPOTHÈSE — trois réfutations ciblées :**
- Une courbure reproductible hors échantillon bat la relation affine : nouveau `results/E_nonlinearity/heldout.json`.
- Des constantes gelées échouent sur réplication exacte avec précision suffisante : nouveau `results/E_replication/predictions.json`.
- Des items appariés en niveau neutre ont des déplacements systématiquement différents selon un critère préenregistré : nouveau `results/E_criterion/matched.json`.

Ces observations réfuteraient respectivement la forme affine, son transport ou sa suffisance — pas toute influence sociale.

**OBSERVÉ-NON-AUDITÉ :** l’échantillon montre des distinctions explicites forme/fond, un refus sous éloge et des préambules de neutralité accompagnant une critique. Cela motive des annotations ; cela n’établit aucune fréquence.

**RAPPORTÉ :** longueur, refus et contre-statements ont déjà été partiellement examinés. Je ne peux donc prétendre découvrir « ce que personne n’a regardé ».

**Non vérifié :** puissance, hashes, exécution, provenance externe, textes complets, code, coût réel, accord humain, spécificité causale, résultats R7, littérature et adéquation aux mentors.

FIN-DE-CELLULE