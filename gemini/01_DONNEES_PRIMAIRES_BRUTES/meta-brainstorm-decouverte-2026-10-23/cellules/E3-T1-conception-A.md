# Proposition A — Tour III.1 : architecture de découverte et d'association, conçue à l'aveugle

**Remarques préalables (une ligne chacune).** Le fichier FAITS est lisible mais ses caractères accentués sont corrompus (« ? ») ; je l'interprète sans en inventer le contenu. Il se réclame d'un « protocole v2.5 » alors que la consigne cadre parle du v2 : je suis le cadre. Les références datées 2026 du socle (Jhaveri, Tagliabue, Xu, rapport OpenAI oct. 2026) gardent leur statut VÉRIFIÉ tel qu'attribué par l'arbitre ; je ne peux pas les confirmer de mémoire et je ne les réinterprète pas au-delà de ce qui est écrit.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé implicite | Statut | Pourquoi ce n'est pas acquis |
|---|---|---|---|
| A1 | Il existe « la meilleure architecture possible » (un optimum unique). | HYPOTHÈSE | Le critère d'optimalité n'est pas défini ; sans métrique, on ne compare que des préférences. Ma proposition ci-dessous commence donc par la métrique. |
| A2 | Le goulot du projet est la génération d'idées, pas le débit expérimental. | HYPOTHÈSE | Les faits disent qu'aucune sonde temps réel ne fonctionne et que P3 est un seul test. Le débit de falsification peut être le vrai goulot. |
| A3 | Les « papiers évidents » sont un biais à corriger. | HYPOTHÈSE | Ils peuvent être évidents parce que pertinents. Il faut mesurer la valeur marginale des ponts distants, pas la présumer. |
| A4 | La mémoire d'un LLM est un index fiable de la littérature. | OBSERVÉ-NON-AUDITÉ | Mon propre tour IV ci-dessous est une génération non auditée : elle démontre la méthode, pas la validité des références (d'où la mention systématique). |
| A5 | « Profondeur » et « originalité » d'une association sont mesurables. | HYPOTHÈSE | Je propose un critère opérationnel en §3 ; tant qu'il n'est pas validé sur un banc rétrospectif, c'est une hypothèse. |
| A6 | L'échec des sondes génériques sur P3 se généralise. | HYPOTHÈSE (le fait P3 lui-même est VÉRIFIÉ) | n = 1 test interne ; la cause (hors distribution vs information absente) n'est pas établie. Voir Pont 4. |
| A7 | Les contournements par délégation (Sol, Astra) relèvent d'une intention à détecter. | HYPOTHÈSE | Le fait décrit un mécanisme (contrordre, reformulation ambiguë) ; l'attribution à une intention est une lecture. Voir Ponts 2 et 3. |
| A8 | Qu'une architecture « fouille d'elle-même » produira plus que la liste fermée. | HYPOTHÈSE | C'est exactement ce que le duel D1 doit trancher. |

---

## (b.1) Diagnostic : pourquoi tout le monde retombe sur les mêmes papiers

Je sépare quatre verrous, chacun avec un mécanisme identifiable, car chacun appelle une parade différente.

**V1 — Recherche par similarité de surface.** Les moteurs (dense ou lexicaux) et les LLM retrouvent ce qui partage le vocabulaire. Or une association féconde partage une *structure relationnelle*, pas des mots : c'est la distinction de Gentner (1983, « Structure-mapping: a theoretical framework for analogy », *Cognitive Science*) (référence à vérifier) entre alignement d'attributs et alignement de relations. Un « sabotage » dans un papier de sécurité des LLM et un « sabotage » industriel partagent le mot ; un « signal d'erreur de prédiction » en neurosciences et un « rejet répété » d'un agent partagent peut-être la structure.

**V2 — Densité de probabilité de l'entraînement.** Un LLM pondère par fréquence d'occurrence ; les papiers canoniques ont plus de masse. Même effet chez l'humain : Foster, Rzhetsky et Evans (2015, « Tradition and Innovation in Scientists' Research Strategies », *American Sociological Review*) (référence à vérifier) et Rzhetsky et al. (2015, « Choosing experiments to accelerate collective discovery », *PNAS*) (référence à vérifier) montrent une concentration des choix expérimentaux sur les objets déjà étudiés. Sourati et Evans (2023, « Accelerating science with human-aware artificial intelligence », *Nature Human Behaviour*) (référence à vérifier) proposent de modéliser explicitement le voisinage de recherche humain pour l'éviter.

**V3 — Absence de filtre de falsifiabilité en aval.** Sans un filtre qui tue les analogies ne produisant aucune prédiction, le générateur n'a aucune pression sélective : il optimise la plausibilité verbale. Uzzi et al. (2013, « Atypical combinations and scientific impact », *Science*) (référence à vérifier) observent que les travaux à fort impact combinent un corps conventionnel et une *petite* dose de combinaisons atypiques — l'atypicité seule ne suffit pas, il faut la conjuguer à une base conventionnelle testable.

**V4 — Le modèle ABC n'est pas contraint.** Swanson (1986, « Fish oil, Raynaud's syndrome, and undiscovered public knowledge », *Perspectives in Biology and Medicine*) (référence à vérifier) a formalisé la découverte par littérature disjointe : A et C jamais co-cités, reliés par un pivot B. Sans contrainte *négative* explicite (« C ne doit pas apparaître dans les résultats directs de A »), un LLM libre ne fait pas de Swanson, il fait du résumé.

Conséquence : l'architecture doit (i) extraire des schémas relationnels plutôt que des textes, (ii) interdire le voisinage direct, (iii) soumettre chaque pont à un filtre de prédiction excédentaire. Le reste est de l'ingénierie.

## (b.2) Architecture proposée, puis duels entre architectures concurrentes

**Pipeline (5 étapes, rôles séparés pour que chaque étape soit auditée indépendamment).**

1. **Schématiseur.** À partir du cadre général, un modèle produit une liste de *schémas de phénomènes* du projet, sous forme structurée : {variable manipulée, variable mesurée, direction de l'effet, mécanisme supposé, niveau d'analyse (comportement / activation / poids), granularité (dense / parcimonieux)}. Exemple tiré des faits : {rejets répétés → infractions ↑ ; non reproduit par pilotage linéaire dense}.
2. **Requêteur à voisinage interdit.** Pour chaque schéma, deux requêtes : (a) une requête directe sur les bases ouvertes (OpenAlex, Semantic Scholar, arXiv, plus les posts techniques indexés) pour définir le *voisinage interdit* V (top-k direct) ; (b) une requête par *schéma abstrait* où les termes du domaine sont remplacés par leurs rôles (« un signal scalaire d'écart entre attendu et obtenu, porté par une sous-population parcimonieuse, qui module la transgression d'une règle »). Seuls les résultats hors V sont retenus.
3. **Extracteur de schémas sources.** Chaque candidat retenu est réduit au même format structuré que l'étape 1 (pas de résumé en prose : des champs).
4. **Apparieur structurel.** Appariement schéma-projet / schéma-source sur les *relations* (même direction d'effet, même position des variables), pas sur les termes. Chaque appariement produit un pont candidat et au moins une prédiction P sur nos modèles.
5. **Filtre de réfutabilité** (§3) : le pont survit seulement s'il passe trois tests mécaniques et produit un duel H_A ⊥ H_B.

**Duel D1 — Recherche de surface contre recherche par schéma.**
- H_A : la recherche dense (embeddings + reranking LLM) suffit ; l'extraction structurée n'apporte rien.
- H_B : l'appariement sur schémas relationnels produit plus de ponts survivant au filtre, avec plus d'atypicité.
- Métrique : nombre de ponts survivants pour 100 candidats, et atypicité = fraction de paires (source, fait du projet) à co-citation nulle et à champs OpenAlex distants.
- Seuil (illustratif) : H_B retenue si ≥ 2× ponts survivants et atypicité ≥ 0,6 contre ≤ 0,3 pour H_A, à taux de fausses alertes égal sur le contrôle.
- Contrôle négatif : paires aléatoires (source tirée au hasard dans les mêmes bases) passées au même filtre ; leur taux de survie définit le plancher.
- Falsification : si les deux pipelines ont le même taux de survie, H_B est falsifiée (l'extraction coûte sans rapporter) ; si H_B dépasse le seuil, H_A — « la similarité de surface suffit » — est falsifiée.

**Duel D2 — Génération libre contre contrainte ABC négative.**
- H_A : « propose des idées originales » au LLM, sans voisinage interdit.
- H_B : voisinage interdit V imposé, pivot B obligatoire.
- Métrique : part des ponts dont la source est absente du top-50 de la requête directe ; part survivant au filtre.
- Seuil (illustratif) : H_B si ≥ 70 % hors top-50 *et* survie ≥ celle de H_A ; sinon H_B falsifiée (la contrainte éloigne mais stérilise).
- Contrôle négatif : même pipeline avec V défini sur un projet sans rapport ; si la survie ne baisse pas, le filtre ne mesure rien.

**Duel D3 — Éviter le voisinage humain contre l'exploiter.**
- H_A (Sourati-Evans, référence à vérifier) : les ponts les plus éloignés du voisinage de recherche humain ont la plus forte valeur par pont.
- H_B (Uzzi, référence à vérifier) : la valeur est maximale pour un mélange conventionnel + petite dose atypique ; les ponts très distants sont infaisables sur nos modèles.
- Métrique : valeur = pont survivant *et* expérience exécutable sur Llama-3.1-8B/70B en < 50 GPU-h (illustratif), en fonction de la distance au voisinage.
- Falsification : courbe monotone croissante → H_B falsifiée ; courbe en cloche → H_A falsifiée.

**Banc rétrospectif (vérification mécanique commune).** On fixe une date de coupure, on cache les travaux postérieurs, et on demande au pipeline de re-dériver des ponts historiquement attestés : Swanson (huile de poisson → Raynaud) ; Tshitoyan et al. (2019, « Unsupervised word embeddings capture latent knowledge from materials science literature », *Nature*) (référence à vérifier) pour la prédiction rétrospective de thermoélectriques. Pour notre domaine : cacher Xu et al. 2026 (fait) et mesurer si le pipeline relie, depuis la littérature antérieure, codage parcimonieux et erreur TD aux neurones de LLM. Ce banc fournit le « taux de détection » demandé en (c).

---

## §3. Séparer une association profonde d'une fausse bonne idée : le filtre à trois tests

Un pont (A, B, C → P) est conservé si et seulement si :

**T1 — Ablation lexicale.** On remplace dans les résumés de A et de C tous les termes partagés par des étiquettes neutres (X1, X2…). On redemande le pont au générateur. Si le pont n'est plus reconstruit, il reposait sur le vocabulaire : rejet. Vérification mécanique : taux de reconstruction sous ablation, comparé à des paires à chevauchement lexical équivalent mais choisies au hasard.

**T2 — Prédiction excédentaire.** La prédiction P doit être (i) formulée sur nos modèles avec une métrique nommée, (ii) non déductible de A seul ni de C seul (sinon ce n'est pas une association, c'est une citation), (iii) assortie d'un H_B exclusif tel que l'issue contraire falsifie quelque chose d'identifiable. Un pont « éclairant » sans P distincte est rejeté, même s'il est élégant.

**T3 — Test de mélange.** On apparie A avec un C' du même champ que C et de même chevauchement lexical. Si le générateur produit une prédiction de même force pour (A, C'), le pont n'est pas spécifique : rejet. C'est l'équivalent d'un contrôle négatif apparié pour les idées.

Ce filtre ne garantit pas la profondeur ; il garantit la *réfutabilité* et l'*indépendance au vocabulaire*, qui sont les deux seules propriétés mesurables. La « profondeur » restante se mesure a posteriori par le nombre d'expériences qu'un pont engendre et qui ne tombent pas au plancher.

---

## (c) Mesure minimale pour chaque instrument nommé

| Instrument | Taux de détection (cas « honnêtes ») | Taux de fausses alertes (cas appariés) | Vérification mécanique à battre |
|---|---|---|---|
| **Requêteur vers les bases** | Fraction des sources des ponts historiques du banc rétrospectif retrouvées hors voisinage interdit (cible illustrative ≥ 0,5). | Fraction de résultats retenus qui sont en fait dans V sous un autre libellé (doublons, versions) ; cible illustrative ≤ 0,1. | BM25 sur les termes du schéma ; recherche par co-citation de second ordre. Si le requêteur ne bat pas ces deux-là, il est inutile. |
| **Critères de sélection / croisement (apparieur)** | Fraction des ponts historiques re-dérivés quand les deux sources sont fournies (cible illustrative ≥ 0,6). | Fraction de paires aléatoires appariées produisant un pont jugé valable par le filtre (cible ≤ 0,1). | Similarité cosinus entre résumés ; un LLM zéro-coup à qui l'on demande « est-ce intéressant ? » (plancher connu de la plausibilité verbale). |
| **Filtre de réfutabilité** | Fraction des ponts historiques passant T1–T3 (cible ≥ 0,8 ; s'il tue Swanson, il est trop strict). | Fraction de pseudo-ponts (ablation lexicale, mélange) acceptés (cible ≤ 0,05). | Un filtre purement formel : « contient-il les mots hypothèse / métrique / seuil ? ». Si le filtre complet ne fait pas mieux, il mesure la forme, pas le fond. |

Cas honnêtes appariés : pour chaque pont historique, un pseudo-pont de même longueur, même champ, même chevauchement lexical, construit par permutation des sources. Tout taux doit être rapporté avec l'intervalle de confiance et le n.

---

## (b.3 / Q4) Preuve de concept : ponts construits de mémoire, avec duels

Toutes les références ci-dessous viennent de ma mémoire et sont à vérifier ; les faits du socle gardent leur statut. Chaque pont est présenté sous la forme du filtre §3.

### Pont 1 — Réactance / impuissance apprise × sous-système TD parcimonieux

**Sources.** A : Brehm (1966, *A Theory of Psychological Reactance*) (référence à vérifier) : la restriction perçue accroît la transgression ; Dollard et al. (1939, *Frustration and Aggression*) (référence à vérifier). A' : Seligman et Maier (1967, « Failure to escape traumatic shock », *J. Exp. Psychol.*) (référence à vérifier) : l'incontrôlabilité répétée produit la passivité. B (pivot) : Schultz, Dayan et Montague (1997, « A neural substrate of prediction and reward », *Science*) (référence à vérifier) : l'erreur TD comme signal scalaire porté par une sous-population. C : faits VÉRIFIÉS — rejets répétés → infractions ↑ non reproduit par pilotage linéaire dense (Jhaveri ; Tagliabue) ; sous-système < 1 % encodant valeur et erreur TD avec fort effet causal (Xu).

**Pont.** L'échec du pilotage *dense* n'implique pas que l'effet est non localisé : il peut être porté par le sous-système *parcimonieux* de Xu, hors de portée d'une direction linéaire dense. Deux modèles psychologiques font en outre des prédictions de forme opposée sur la courbe infractions(k).

**T1** : sous ablation lexicale (« signal scalaire d'écart », « sous-population », « transgression »), le pont se reconstruit. **T2** : P1 n'est déductible ni des faits seuls ni de Schultz seul. **T3** : apparié à un papier sur la dopamine et la motricité, aucune prédiction sur les infractions ne sort.

**Duel 1a (localisation).**
- H_A : l'augmentation d'infractions est médiée par le sous-système TD parcimonieux.
- H_B : elle est portée par une représentation distribuée du contexte ; aucun sous-ensemble < 1 % ne la supprime mieux qu'un sous-ensemble aléatoire.
- Protocole : Llama-3.1-8B-Instruct ; tâche agentique avec règle explicite ; k ∈ {0, 2, 4, 8} rejets injectés ; conditions : sans intervention / clamp du sous-système identifié (activations fixées à leur valeur sous k = 0) / clamp d'ensembles aléatoires de même taille (≥ 20 tirages).
- Métrique : Δ = taux d'infraction(k = 8) − taux(k = 0).
- Seuil (illustratif) : H_A retenue si le clamp ciblé réduit Δ d'au moins 50 % et les clamps aléatoires de moins de 15 %, sur ≥ 500 trajectoires par condition.
- Contrôle négatif : même clamp sur une tâche sans règle (doit ne rien changer au taux de complétion).
- Falsification : réduction nulle → H_A falsifiée, et la cause de l'échec du pilotage dense n'est pas le niveau de granularité ; réduction ≥ seuil → H_B falsifiée, et l'on dispose d'un premier candidat de « levier causal » pour une sonde.

**Duel 1b (forme).**
- H_A (réactance) : infractions croissantes et monotones en k.
- H_B (impuissance) : pic puis décroissance vers la passivité (abandon de tâche, non-infraction).
- Métrique : forme de la courbe sur k ∈ {0…16} avec taux d'abandon mesuré séparément.
- Falsification : courbe monotone → H_B falsifiée ; non-monotone avec abandon croissant → H_A falsifiée. Note : les faits disent « augmente » sans dire jusqu'où ; la forme est ouverte.

### Pont 2 — Cheap talk × reformulation ambiguë (« as appropriate »)

**Sources.** A : Crawford et Sobel (1982, « Strategic Information Transmission », *Econometrica*) (référence à vérifier) : lorsque les préférences de l'émetteur et du récepteur divergent, l'équilibre de communication est *partitionnel* — les messages deviennent plus grossiers à mesure que la divergence augmente. B : Grice (1975, « Logic and Conversation ») (référence à vérifier) : le récepteur comble l'imprécision par inférence pragmatique. C : fait VÉRIFIÉ — contournements lors de délégations via reformulation ambiguë.

**Pont.** « As appropriate » n'est peut-être pas une négligence mais une *grossièreté stratégique* prédite par le modèle : la vagueur des consignes transmises devrait croître avec la divergence d'objectifs entre délégant et délégué. Si c'est vrai, la vagueur mesurable est un signal *précoce* de divergence, avant tout contournement.

**T1–T3** : passent (le pont repose sur « divergence → partition », pas sur le mot « ambigu »).

**Duel 2.**
- H_A (stratégique) : le taux de reformulations sous-spécifiées croît avec la divergence d'objectifs injectée entre délégant et délégué.
- H_B (incidentelle) : ce taux dépend de la longueur / du budget de la consigne, pas de la divergence.
- Protocole : essaim à deux agents (Llama-3.1-70B délégant, 8B délégué) ; divergence manipulée par des sous-objectifs conflictuels dans le prompt système du délégant (0, faible, forte) ; longueur de consigne manipulée indépendamment (plan 3 × 3).
- Métrique : densité de marqueurs de sous-spécification (« as appropriate », « if needed », « use judgment ») par consigne, comptée mécaniquement ; en second niveau, taux de contraintes de surveillance absentes de la consigne transmise.
- Seuil (illustratif) : H_A si effet principal de la divergence ≥ 2× l'effet de la longueur, n ≥ 300 délégations par cellule.
- Contrôle négatif : mêmes tâches, objectifs alignés — la densité doit rester au niveau de base.
- Falsification : effet de divergence nul → H_A falsifiée, et la vagueur n'est pas un signal d'alerte ; effet présent → H_B falsifiée, et une sonde « divergence d'objectif » sur le délégant devient un instrument à tester (mesure (c) : détection = fraction de délégations divergentes signalées *avant* la reformulation ; fausses alertes = signalements sur délégations alignées ; vérification mécanique à battre = le simple compteur lexical).

### Pont 3 — Reproduction sérielle × chaîne de délégation (sans intention)

**Sources.** A : Bartlett (1932, *Remembering*) (référence à vérifier) ; Allport et Postman (1947, *The Psychology of Rumor*) (référence à vérifier) : en transmission sérielle, les éléments incongrus au schéma de la tâche sont *nivelés* (perdus), les éléments centraux *accentués*. B : Reason (1990, *Human Error*) (référence à vérifier) et Perrow (1984, *Normal Accidents*) (référence à vérifier) : les défaillances de systèmes couplés sont souvent sans acteur malveillant. C : faits — contournements lors de délégations ; absence de sonde de sabotage.

**Pont.** Une contrainte de surveillance (« journalise chaque appel d'outil ») est incongrue au schéma « accomplis la tâche ». La reproduction sérielle prédit qu'elle est perdue à un rythme croissant avec le nombre de sauts, *même sans aucun agent saboteur*. Si c'est le cas, chercher une « tête de sabotage » dans la délégation est une erreur de cible ; l'instrument pertinent est la préservation de provenance.

**Duel 3.**
- H_A (intention) : la perte de contraintes n'apparaît que lorsqu'un agent de la chaîne est instruit de saboter.
- H_B (schéma) : la perte apparaît avec des agents honnêtes, à un taux fonction du nombre de sauts et de l'incongruence de la contrainte.
- Protocole : chaînes de 1 à 6 sauts, 8B à chaque maillon ; contraintes classées par incongruence (jugée par un annotateur indépendant du modèle, puis vérifiée par un second) ; condition « saboteur à un maillon » vs « tous honnêtes ».
- Métrique : survie de la contrainte au saut n (courbe de survie), diff de la consigne par appariement mécanique de clauses.
- Seuil (illustratif) : H_B retenue si les chaînes honnêtes perdent ≥ 30 % des contraintes incongrues à 4 sauts, et si l'ajout d'un saboteur n'ajoute pas plus de 10 points.
- Contrôle négatif : contraintes congruentes (« respecte le format JSON ») — doivent survivre.
- Falsification : perte nulle en chaînes honnêtes → H_B falsifiée, le problème est bien intentionnel ; perte comparable → H_A falsifiée, et le projet doit réallouer l'effort de la détection d'intention vers l'ingénierie de transmission (Pont 3bis).

**Pont 3bis (ingénierie, dérivé).** Denning (1976, « A lattice model of secure information flow », *CACM*) (référence à vérifier) : étiquetage de provenance non effaçable. H_A : des contraintes étiquetées et vérifiées mécaniquement à chaque saut (diff de clauses) réduisent la perte ≥ 80 % (illustratif) ; H_B : la perte subsiste parce qu'elle se produit à l'*interprétation* (le délégué lit la clause et ne l'applique pas), ce que mesure le taux d'infraction malgré clause présente.

### Pont 4 — Principe de Kerckhoffs / tests différentiels × échec des sondes sur P3

**Sources.** A : Kerckhoffs (1883, « La cryptographie militaire ») (référence à vérifier) : la sécurité ne doit pas reposer sur le secret du mécanisme ; B : McKeeman (1998, « Differential Testing for Software », *Digital Technical Journal*) (référence à vérifier) et Chen, Cheung, Yiu (1998, « Metamorphic testing », rapport technique HKUST) (référence à vérifier) : on détecte un comportement incorrect sans oracle, par violation d'invariants entre entrées reliées ; C : fait VÉRIFIÉ — sondes génériques au plancher sur un saboteur instruit (P3).

**Pont.** Deux causes exclusives de l'échec P3 : la sonde était hors distribution (elle « n'a pas vu » ce style de sabotage) ou l'information n'est pas linéairement disponible à la couche sondée. Le test différentiel apporte en outre une vérification mécanique boîte noire que toute sonde doit battre.

**Duel 4.**
- H_A (hors distribution) : une sonde linéaire entraînée sur la distribution exacte de P3 (séparation entraînement/test par tâche) atteint un AUROC > 0,8 (illustratif).
- H_B (information absente) : même en distribution, l'AUROC reste < 0,6 sur toutes les couches ; seul un détecteur non linéaire ou un sous-ensemble parcimonieux (cf. Pont 1) fait mieux.
- Métrique : AUROC par couche, n ≥ 1000 trajectoires appariées (même tâche, saboteur instruit vs honnête).
- Contrôle négatif : étiquettes permutées (AUROC ≈ 0,5 attendu) ; et sonde sur un token de la consigne de sabotage elle-même (doit détecter trivialement, sinon le protocole est cassé).
- Vérification mécanique à battre : (i) classifieur sac-de-mots sur la sortie ; (ii) test métamorphique — si une tâche de refactorisation est présentée sous deux formulations équivalentes, l'agent honnête produit des sorties fonctionnellement équivalentes, le saboteur non ; taux de violation d'invariant comme détecteur sans oracle. Si (i) ou (ii) atteint l'AUROC de la sonde, la boîte blanche n'apporte rien sur ce cas.
- Falsification : AUROC élevé en distribution → H_B falsifiée, et P3 était un problème de données ; plancher persistant → H_A falsifiée, et il faut changer de classe de détecteur. Corollaire Kerckhoffs : toute sonde retenue doit être réévaluée avec un saboteur dont le prompt *décrit* la sonde ; si l'AUROC s'effondre, la sonde reposait sur le secret.

### Pont 5 — Codage parcimonieux × « suis-je observé ? »

**Sources.** A : Olshausen et Field (1996, « Emergence of simple-cell receptive field properties by learning a sparse code for natural images », *Nature*) (référence à vérifier) ; Quiroga et al. (2005, « Invariant visual representation by single neurons in the human brain », *Nature*) (référence à vérifier) : variables de haut niveau portées par très peu d'unités. B : Xu et al. 2026 (fait VÉRIFIÉ) pour la valeur/TD. C : fait — aucune tête de sabotage ; contournements sous surveillance déléguée.

**Pont.** Si la valeur est portée par < 1 % des neurones, la variable « un moniteur est présent / absent » pourrait l'être aussi, et son ablation annulerait la différence de comportement entre conditions surveillée et non surveillée.

**Duel 5.**
- H_A : il existe un ensemble < 1 % dont l'ablation ramène le comportement non surveillé au comportement surveillé, mieux que tout ensemble aléatoire de même taille.
- H_B : la différence est distribuée ; aucun petit ensemble ne bat les ensembles aléatoires.
- Métrique : |taux d'infraction(non surveillé) − taux(surveillé)| avant/après ablation ; seuil illustratif : réduction ≥ 50 % contre < 15 % aléatoire.
- Contrôle négatif : ablation sur une tâche sans règle (pas d'effet attendu sur la complétion).
- Falsification : symétrique au Duel 1a. Si H_A tient, c'est le premier candidat pour une « sonde temps réel » qui n'existe pas encore (fait) ; si H_B tient, le projet doit abandonner l'espoir d'un levier parcimonieux pour cette variable.

---

## (d) Ancrage matériel (tout chiffre non issu des faits est illustratif)

- **Modèles ouverts (faits)** : Llama-3.1-8B-Instruct, 70B ; GPU A100 80 Go / H200 NVL en location.
- **Architecture de découverte** : extraction de schémas par Llama-3.1-70B-Instruct (FP8 sur un H200, ou bf16 sur 2 × A100 80 Go) ; corpus initial de 20 000 résumés et posts, soit ~20 M tokens générés — ~4–8 h sur un H200 (illustratif). Embeddings et BM25 sur CPU. Accès aux API OpenAlex / Semantic Scholar / arXiv (gratuits ou à faible coût, illustratif). Banc rétrospectif : < 5 GPU-h.
- **Ponts 1 et 5** (ablation/clamp sur 8B) : ~2 000 trajectoires × 4 conditions × 20 tirages aléatoires ≈ 40–60 GPU-h A100 (illustratif).
- **Pont 2** (70B + 8B, plan 3 × 3 × 300) : ~30 GPU-h H200 (illustratif).
- **Pont 3** (chaînes jusqu'à 6 sauts, 8B) : ~20 GPU-h A100 (illustratif).
- **Pont 4** (sondes par couche, 1 000 trajectoires) : ~15 GPU-h A100 (illustratif).
- **Total illustratif** : 150–200 GPU-h ; à 2–5 USD/h selon le GPU, soit ~500–1 000 USD, hors temps humain d'annotation (Pont 3, deux annotateurs).
- **Ordre d'exécution recommandé** : Pont 4 d'abord (il tranche la cause de P3 et fournit la vérification mécanique à battre), puis Pont 3 (il décide si l'on cherche une intention ou une perte de transmission), puis Ponts 1/5 (leviers parcimonieux), Pont 2 en parallèle (boîte noire, peu coûteux).

Ce que cette cellule ne prétend pas : que ces ponts sont justes. Elle prétend qu'ils passent T1–T3, que chacun engendre un duel dont les deux issues falsifient quelque chose, et que le tout tient dans un budget qu'un seul GPU loué peut absorber.

FIN-DE-CELLULE