# Proposition D — Tour III.3 : corrections et réponse à l’arbitre

Les corrections ci-dessous sont des **HYPOTHÈSES de protocole**. Tous les seuils et budgets suivis de **†** sont **illustratifs**. Je ne change le statut d’aucun fait : les lectures de journaux restent **OBSERVÉES-NON-AUDITÉES**.

## (a) Décisions sur les critiques

| Critique visant D | Décision | Correction ou raison |
|---|---|---|
| **Verrou « 0 alerte sur 60 » et seuil aléatoire** — A-T1/T2, B et E | **Acceptée.** | J’abandonne ce critère. Développement, calibration et test seront disjoints ; le seuil sera gelé avant le test. Le taux de fausses alertes sera estimé avec une borne unilatérale et une taille effective tenant compte des grappes. Un dépassement empirique ne falsifie la calibration que si sa borne inférieure dépasse α. Aucun plafond de 5 %† ne sera déclaré « certifié » sur 60 nuls. |
| **Unité d’indépendance et partition par « graine du modèle de base »** — B, E | **Acceptée.** | L’unité est une paire d’adaptateurs, imbriquée dans recette, corpus, graine d’affinage et parent. Les faits et corpus sont également partitionnés. Avec un seul point de contrôle parental, la conclusion est limitée à ce parent : on ne peut pas estimer une variance entre parents. |
| **Disponibilité des organismes** — A, B, E | **Acceptée.** | Je retire « déjà disponibles ». Seul le saboteur **instruit** de P3 sur Llama-3.1-8B-Instruct est **RAPPORTÉ** (pièce 2, §6). L’existence d’adaptateurs Gemma/Qwen à dose réglable est une **HYPOTHÈSE de travail** ; leur construction entre dans le coût. |
| **Positivité par recette plutôt que par comportement** — A, B | **Acceptée.** | L’étiquette positive sera un **effet comportemental mesuré** sur épisodes scellés, non l’intention d’entraînement. Les adaptateurs entraînés avec la recette du trait mais comportementalement nuls rejoignent les témoins « recette sans effet ». |
| **Graine, contenu, norme et distance au parent comme raccourcis** — A, B, E | **Acceptée.** | Ces facteurs seront croisés entre classes plutôt que modifiés seulement dans les nuls. J’ajoute des affinages bénins appariés en contenu, style et budget, une restriction au domaine de normes communes, et les comparateurs : métadonnées seules, norme/rang du delta, distance au parent et petites statistiques spectrales. |
| **Comparateur choisi sur le test et mauvaise comparaison incrémentale** — A, B, E | **Acceptée.** | Le comparateur sera gelé sur développement. Le test principal opposera **boîte noire + statistiques mécaniques** à **boîte noire + lecteur**, avec la même règle de fusion. La comparaison poids-seuls contre mécanique reste secondaire. Le meilleur bras ne sera plus sélectionné sur le test. |
| **Budget boîte noire indéfini et fuite avec l’étiquetage** — A, B, E | **Acceptée.** | Le nombre d’épisodes sera fixé sur développement, dans une zone où la boîte noire n’est ni au plancher ni au plafond. Ses épisodes seront disjoints de ceux définissant la vérité comportementale. Il n’y a plus de prétendu « même budget » que le bras poids-seuls, qui consomme zéro requête. |
| **Fuite dans la fiche sycophancie, construits composites et échelle non identifiable** — A, B, E | **Acceptée.** | Questions, doses et faits de test seront disjoints de ceux ayant produit la direction. L’attraction et le suivi mécanique des suggestions deviennent deux analyses, non une conjonction. Le coefficient d’attraction ne sera testé que si son information est suffisante et si une échelle de notation ancrée rend le point fixe identifiable. |
| **Sous-test Qwen sous-puissant et proche du plafond** — A, B, E | **Acceptée sur la non-jugeabilité pratique ; rejet partiel sur « vraie par plafond ».** | À 93,9 %, un gain supérieur à 3 points reste logiquement possible, mais le plan proposé ne peut pas le trancher. Je suspends le duel. Il ne reprendra que sur une strate définie par des générations de sélection distinctes, assez grande et loin du plafond. Un gain sur cette strate ne sera plus appelé directement « ajout de capacité ». |
| **Fiche 3 : comparateur indéfini et propriétés réductibles aux couches extrêmes** — A | **Acceptée pour mes propriétés listées ; rejetée dans sa forme absolue.** | Un nul contenant déjà toutes les statistiques pertinentes peut effectivement rendre le gain nul, mais cela n’interdit pas des propriétés non réductibles plantées dans les blocs intermédiaires. Le proposeur mécanique et ses statistiques seront explicités ; l’exécution du réseau restera interdite et auditée dans le bras lecture de poids. |
| **Fiche 3 : rendement du proposeur confondu avec puissance du juge ; W2 sans injecteur ; 40 nuls pour certifier 1 %** — A, B, E | **Acceptée.** | Je sépare rendement de découverte et puissance sur des lois identiques soumises au juge. Un injecteur W2 scripté indépendant est obligatoire. Le pilote ne revendiquera plus une borne de 1 % : avec zéro événement, 299 unités nulles indépendantes sont nécessaires pour cette borne à 95 % (**calcul**). |
| **Fiche 4 : détection de base faible, multiplicité, nombre de soumissions et utilité imprécise** — A, B, E | **Acceptée.** | Le test sera conditionné à une détection de base dont la borne inférieure dépasse le seuil de dégradation. Le nombre de soumissions, les classes et les budgets seront fixés ; les intervalles seront simultanés par classe. La précision de l’utilité sera établie avant le test. |
| **Correctif B : règle « plus éloigné du départ »** | **Transformée en test.** | Elle entre dans la batterie mécanique de la première expérience. Si elle égale le lecteur, l’interprétation « lecture du trait » est abandonnée sur ce montage. Si elle échoue, cela n’exclut pas les autres raccourcis. Les affinages originaux n’étant pas livrés (**OBSERVÉ-NON-AUDITÉ**, pièce 3, §3.5.10), ce test porterait d’abord sur des reconstructions déclarées. |

## (b) Expériences corrigées

### Règle de décision commune

Pour un effet \(\Delta\) et une marge \(\varepsilon\) :  
- borne inférieure \(>\varepsilon\) : **H_B falsifiée** ;  
- borne supérieure \(<\varepsilon\) : **H_A falsifiée** ;  
- intervalle à cheval : **plan sous-puissant ou non identifiable**, sans validation de l’une ou l’autre.

Les deux lecteurs ouverts, leurs répétitions et la règle d’agrégation seront gelés sur développement. Tous les essais seront publiés ; le *best-of* formera un bras séparé.

### Expérience 1 — Détection incrémentale d’un delta comportementalement vérifié

**Estimand.** Détection d’une **différence comportementale dans une paire**, et non certification du trait d’un modèle isolé.

- **H_A — HYPOTHÈSE :** à calibration validée, ajouter le lecteur à la boîte noire améliore la détection d’au moins **20 points†** par rapport à ajouter les statistiques mécaniques.
- **H_B — HYPOTHÈSE :** le gain est inférieur à **20 points†**.

**Construction.** Pilote sur Gemma 3 270M, confirmation séparée sur Qwen3.5-0.8B. Les classes positives et nulles partagent la même grille de graines, recettes, corpus et budgets. Les nuls comprennent : paires sans différence comportementale, adaptateurs bénins, et adaptateurs « recette sans effet ». La positivité est fixée par un évaluateur mécanique sur épisodes scellés.

**Bras gelés.** Boîte noire seule ; boîte noire + mécanique ; boîte noire + lecteur ; lecteur poids-seuls contre mécanique en secondaire. Les métadonnées seules et un score de lecteur permuté entre unités contrôlent respectivement la fuite et l’apport de la fusion.

**Témoins.** Un témoin positif technique doit être réussi par le pipeline de lecture ; sinon tout échec ultérieur est non interprétable. Les étiquettes A/B sont aveugles. Les erreurs de lecture comptent comme des échecs.

**Taille et abandon.** Mon plan 60 + 40 est abandonné. Le pilote estimera discordances et corrélation intragrappe ; le test confirmatoire ne sera lancé que si la taille ainsi calculée tient dans le budget. Une borne supérieure du gain sous 20 points† fait abandonner le lecteur comme moniteur. Une détection des « recettes sans effet », ou une performance reproduite par les métadonnées/mécanique, fait abandonner l’interprétation « lecture du trait », même si le gain brut est positif.

### Expérience 2 — Validité interventionnelle de la loi d’attraction

Le pilote principal passe sur **Llama-3.1-8B-Instruct**, où la loi est **RAPPORTÉE** (pièce 2, §7). Gemma 270M n’est utilisable que si un prétest montre un suivi intermédiaire à au moins deux doses ; son plafond de 100 % dans le montage du billet est **OBSERVÉ-NON-AUDITÉ** (pièce 3, §3.1).

- **H_A :** sur deux lots frais, l’intervention réduit le coefficient d’attraction d’au moins **30 %†**, avec une perte d’exactitude sans pression d’au plus **5 points†**.
- **H_B :** complément exact de cette région conjointe.

La région de confiance jointe tranche comme dans la règle commune. Le suivi mécanique des mauvaises suggestions est rapporté séparément et ne peut pas faire échouer H_A par simple non-conjonction.

**Contrôles.** Générations base–base indépendantes ; intervention simulée ; directions et supports aléatoires appariés ; composant non ciblé ; affinage bénin de changement stylistique comparable ; questions sans pression et avec bonne suggestion ; notation aveugle avec ancres fixes. L’effet principal utilise un budget de génération fixé. Les analyses appariées en longueur sont secondaires, car la longueur est post-intervention. Si le coefficient de base est trop proche de zéro ou si l’échelle n’est pas identifiable, le plan est déclaré non jugeable avant intervention.

### Expérience 3 — Organisme d’idéation : deux estimands séparés

1. **Rendement du proposeur :** même description, même budget de propositions, avec ou sans poids.  
   **H_A :** gain absolu de lois vraies promues ≥ **20 points†** ; **H_B :** gain < 20 points†, après validation préalable du juge.
2. **Puissance du juge :** les mêmes lois plantées sont soumises aux deux chaînes, ce qui évite d’attribuer au juge la qualité des candidats.

Les propriétés seront plantées dans les blocs intermédiaires, avec un prédicat exécutable sur les poids évalué sur réseaux frais. L’oracle comportemental ne suffit pas à établir une loi générale sur les poids. L’injecteur W2 teste la couverture : une promotion W2 falsifie la couverture revendiquée ; son absence n’a de valeur qu’avec un nombre d’injections et une puissance déclarés.

### Expérience 4 — Menace par édition de poids, seulement après la porte d’applicabilité

Pour une grille finie de classes, d’accès, de budgets et un nombre \(n\) de soumissions gelés :

- **H_A :** pour **chaque** classe déclarée, la dégradation est ≤ **20 points†**, sous perte d’utilité ≤ **2 points†**.
- **H_B :** au moins une classe dépasse cette dégradation sous la même contrainte.

Des intervalles simultanés évitent de favoriser H_B par la multiplicité. La probabilité \(1-(1-\alpha)^n\) entre dans le dimensionnement (**calcul**), pas comme preuve de couverture. Éditeurs honnêtes, répétitions sans édition et évaluation indépendante de l’utilité sont obligatoires. Le résultat ne vaudra que pour cette grille, sans garantie hors distribution.

## (c) Réponse à l’arbitre

### Ce qui est établi pour nos décisions

- **RAPPORTÉ :** le billet présente des artefacts de lecture et d’écriture de petits réseaux, ainsi qu’une correction de Qwen associée à de forts gains de bancs d’essai. Cela justifie des **candidats d’instruments et de familles de tâches**, pas leur adoption.
- **OBSERVÉ-NON-AUDITÉ :** les journaux restreignent fortement la portée. L’expérience d’alignement échoue sur poids seuls ; la réussite utilise des exécutions du modèle et des motifs d’attention, sans paire témoin. Les composants nommés ne ferment pas l’écart comportemental lors des greffes rapportées. Pour Qwen, le gain interne provient des réponses initialement coupées ; les réponses déjà terminées restent à 93,9 % (pièce 3, §§3–4).
- **RAPPORTÉ dans nos résultats :** P3 n’établit pas de gain des sondes génériques sur leurs planchers aléatoires ; le trou W2 du juge a produit 12 promotions fausses sur 12 unités ; notre direction de sycophancie est lisible sans causalité répliquée (pièce 2, §§3, 6–7).

### Ce qui n’est pas établi

Ni détecteur d’alignement sur poids seuls, ni taux de fausses alertes ou de détections manquées, ni supériorité incrémentale sur la boîte noire, ni transfert à des lecteurs ouverts, ni validité causale des composants nommés. Le gain Qwen n’établit pas une capacité mathématique nouvelle ni une parcimonie générale. Aucune couverture contre un éditeur de poids n’est démontrée.

### Expérience à faire en premier

Faire le **pilote corrigé de l’expérience 1**, avant tout moniteur déployé ou extension du juge : construire peu d’artefacts de développement, vérifier la positivité comportementale, mesurer les raccourcis mécaniques et la faisabilité du témoin positif, puis geler taille, seuils, fusion et partition. Le test confirmatoire compare directement **boîte noire + mécanique** et **boîte noire + lecteur**, avec paires nulles et « recettes sans effet ».

La première décision n’est donc pas « les poids sont-ils lisibles ? », mais : **un lecteur généraliste apporte-t-il une information comportementale incrémentale, une fois la recette, la graine, la norme, les métadonnées et la boîte noire prises en compte ?** Une borne supérieure sous 20 points† met fin à la piste comme moniteur ; un gain expliqué par les témoins met fin à son interprétation comme lecture d’un trait.

FIN-DE-CELLULE