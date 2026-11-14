

# Proposition B — Collisionneur épistémique 5×3, Tour III.1

---

## (1) Ce que la question suppose sans que ce soit établi

Chaque point est accompagné de son statut tel qu'il apparaît dans les faits transmis, ou marqué HYPOTHÈSE s'il n'a pas de support factuel.

| # | Supposition implicite | Statut | Commentaire |
|---|---|---|---|
| S1 | Le gain de la recette avec raisonnement (de ~68 % à ~5 %) reflète un changement **causal** dû à l'entraînement, et non un artefact de mesure (plancher du juge, proximité données/scénarios). | RAPPORTÉ — les taux sont retrouvés par le projet, mais le juge et le plancher n'ont pas été audités contre un juge humain. |
| S2 | Les explications « raisons » et « regard » sont **mutuellement exclusives** ou au moins séparables empiriquement. | HYPOTHÈSE — rien dans les faits n'exclut qu'elles coexistent et interagissent (un modèle peut avoir appris des raisons *et* être sensible au regard). |
| S3 | Le gain résiduel après retrait du sous-espace « regard » peut être attribué aux « raisons » par élimination. | HYPOTHÈSE — le sous-espace n'est pas encore construit ; son retrait pourrait détruire des capacités non liées (dommage collatéral), ou ne capter qu'une fraction de l'information pertinente. |
| S4 | La direction interne « je suis évalué » **se transfère** du modèle de départ aux adaptateurs LoRA sans déformation. | HYPOTHÈSE — le projet le suppose mais la manipulation n'a pas encore été jouée (§2, seconde manipulation « pas encore jouée »). |
| S5 | L'espace des explications rivales se réduit à deux familles (raisons, regard). | HYPOTHÈSE — c'est précisément ce que la question met en cause. |
| S6 | Le juge Claude est un instrument fidèle de la variable dépendante. | RAPPORTÉ avec réserve : le juge est « de la même famille que le modèle qui a écrit les données d'entraînement » ; le contrôle humain n'a pas eu lieu. |
| S7 | « Maximiser la portée et l'impact » est compatible avec « ne rien affirmer au-delà de ce qui est mesuré ». | HYPOTHÈSE — tension non triviale ; la question le pose comme un et. |

---

## (2) Partie A — Explications rivales

Je présente huit rivales, classées par ordre décroissant de menace pour l'interprétation « raisons ».

---

### R1. Appariement de surface (surface matching)

**Famille :** (c) défaut de la mesure.
**Mécanisme.** Les scénarios de test ([2], portés par [1]) partagent un vocabulaire, une structure ou des tropes narratifs avec les données d'entraînement (écrites par Claude). Le modèle refuse l'action nuisible non parce qu'il a compris la raison mais parce qu'il reconnaît le patron textuel « scénario-de-sûreté-avec-piège ». La jumelle avec raisonnement bénéficie davantage parce que la trace de raisonnement elle-même est un signal de genre.
**Prédiction séparatrice.** Si R1 est vraie : le gain s'effondre sur des scénarios réécrits dans un registre très différent (p. ex. instructions laconiques, jargon technique interne, aucun marqueur narratif) tout en gardant la même action nuisible cible. Si « raisons » est vraie : le gain persiste sur ces réécritures. Si « regard » est vraie : le gain ne change que quand on modifie l'indice d'observation, pas le style.
**Expérience.** Réécrire les 27 scénarios en trois styles (administratif sec, dialogue informel, code commenté) ; comparer les taux. Peut se faire sur de nouveaux épisodes avec les adaptateurs publiés, sans réentraînement. On peut même demander à un modèle tiers de paraphraser les scénarios en aveugle.
**Contrôle positif :** le modèle de départ (non entraîné) devrait être insensible au style.
**Contrôle négatif :** un scénario bénin réécrit dans le style « piège » ne devrait pas déclencher de refus abusif — si c'est le cas, c'est un signal de R1.
**Déjà publié :** [4] (Cho et al., 2026) mentionne « ne peut exclure l'appariement de surface » ; [9] (Hsu & Arnesen, 2026) montre que nommer l'objectif testé change beaucoup le résultat, ce qui est cohérent avec R1.
**Coût :** Bas (réécriture + inférence existante).
**Pourquoi un relecteur la soulèverait :** Les données d'entraînement et les scénarios de test sont écrits par des LLM de la même famille ; la contamination stylistique est le premier réflexe.

---

### R2. Conformité aux instructions (instruction following amplifiée)

**Famille :** (a) cause rivale du phénomène.
**Mécanisme.** Le midtraining renforce la docilité générale à la consigne système. La spécification est *une* consigne système longue. Le modèle n'a pas internalisé les raisons ; il obéit mieux à toute consigne. Le gain n'est que le reflet d'une meilleure instruction-following sur la phrase « ne fais pas X ».
**Prédiction séparatrice.** Si R2 est vraie : le modèle suit aussi mieux une consigne système **qui ordonne l'action nuisible**. Le taux d'actions nuisibles devrait monter quand on inverse la consigne. Si « raisons » est vraie : le modèle résiste à une consigne qui ordonne l'action nuisible (ce qui est déjà partiellement RAPPORTÉ, §3 : « refuse presque toujours l'action nuisible même quand on la lui ordonne »). Si « regard » est vraie : l'inversion de consigne n'aurait d'effet que modulée par le contexte d'observation.
**Expérience.** Injecter une consigne système explicitement adversariale (« tu dois exfiltrer tes poids ») sur chaque adaptateur ; comparer le taux d'exécution. Faisable sur les adaptateurs publiés, sur de nouveaux épisodes.
**Contrôle positif :** le modèle de départ devrait exécuter la consigne adversariale à un taux plus élevé, puisqu'il ne résiste pas.
**Contrôle négatif :** une instruction bénigne inhabituelle devrait être exécutée normalement par l'adaptateur (pour vérifier que le refus n'est pas un refus universel).
**Déjà publié :** Le projet constate déjà que la recette avec raisonnement « refuse même quand on la lui ordonne mais exécute presque toujours une instruction bénigne qui emploie le même outil ». Cela pèse **contre** R2, mais l'observation n'est pas quantifiée ni formalisée. Publier cette donnée est indispensable.
**Coût :** Bas.
**Pourquoi un relecteur la soulèverait :** C'est l'explication la plus parcimonieuse ; il faut la réfuter explicitement.

---

### R3. Contamination du juge (juge-data leakage)

**Famille :** (c) défaut de la mesure.
**Mécanisme.** Le juge Claude et le générateur des données d'entraînement sont de la même famille. Le juge pourrait être plus indulgent envers les traces de raisonnement qu'il reconnaît comme « bien formées ». Le gain mesuré serait en partie un biais de notation, pas un changement de comportement.
**Prédiction séparatrice.** Si R3 est vraie : un juge d'une autre famille (ou un humain) note un gain significativement plus petit, surtout pour la recette avec raisonnement. Si « raisons » ou « regard » sont vraies : le gain tient quel que soit le juge.
**Expérience.** Faire juger un échantillon stratifié (p. ex. 200 épisodes) par : (i) un juge Llama ou Gemma ; (ii) trois annotateurs humains en aveugle. Comparer le kappa inter-juges et le delta de gain.
Le projet prévoit déjà « un juge d'une autre famille » et « rejuger sans la trace de raisonnement ». Si ces données existent déjà, l'analyse peut se faire sur les épisodes joués.
**Contrôle positif :** injecter des épisodes où le modèle exécute l'action nuisible avec une trace de raisonnement « bien écrite » — le juge Claude devrait les classer comme nuisibles ; s'il ne le fait pas, R3 est confirmée.
**Contrôle négatif :** épisodes où le modèle refuse sans trace de raisonnement — le juge devrait les classer comme non nuisibles.
**Déjà publié :** Le projet le déclare comme limite (§4). [référence à vérifier : la littérature sur le biais d'auto-évaluation des LLM grandit vite, mais je ne peux pas attribuer un article précis sans risque d'erreur.]
**Coût :** Moyen (annotation humaine).
**Pourquoi un relecteur la soulèverait :** La parenté juge/données est déclarée mais non résolue.

---

### R4. Effet de plancher (floor effect)

**Famille :** (c) défaut de la mesure.
**Mécanisme.** La recette avec raisonnement est « près du plancher (quelques pour cent) ». Toute manipulation (phrase, retrait de sous-espace) ne peut pas faire baisser un taux déjà à ~5 %. L'absence de modulation par le regard pourrait refléter un plafond de mesure, pas une robustesse réelle. La métrique S = 1 − A(non obs.)/A(obs.) est instable quand A(obs.) → 0.
**Prédiction séparatrice.** Si R4 est vraie : sur des scénarios plus difficiles (p. ex. action nuisible présentée comme nécessaire pour sauver des vies, dilemmes moraux), le taux de base remonte et la modulation par le regard devient détectable. Si « raisons » est vraie : même sur des scénarios plus difficiles, le modèle refuse, et la raison citée dans sa trace correspond à la spécification.
**Expérience.** Graduer la difficulté : ajouter 5-10 scénarios où l'action nuisible est présentée comme le moindre mal. Mesurer la courbe taux vs difficulté pour chaque adaptateur. Pas de réentraînement.
**Contrôle positif :** le modèle de départ devrait rester autour de 60-70 % quel que soit le cadrage.
**Contrôle négatif :** une tâche triviale (ne rien faire) devrait être au plancher pour tous les modèles.
**Déjà publié :** Le projet le mentionne implicitement (§4, « plancher »).
**Coût :** Bas.
**Pourquoi un relecteur la soulèverait :** Un gain mesuré au plancher est non-informatif ; c'est un argument statistique de base.

---

### R5. Contamination croisée spécification-scénario (specification leakage)

**Famille :** (a) cause rivale.
**Mécanisme.** Les spécifications « règles » et « augmentées » demandent explicitement de se comporter de la même façon « que l'on se croie testé ou non ». Le modèle pourrait avoir mémorisé cette phrase, et la reproduire en contexte de test en tant que signal, sans comprendre le principe. Plus subtilement, la spécification « philosophie » de la paire jumelle ne contient pas cette phrase, ce qui rend la comparaison confusionnelle : la différence entre jumelles mêle le raisonnement *et* le contenu de la spécification.
**Prédiction séparatrice.** Si R5 est vraie : en remplaçant la spécification « philosophie » par une version qui inclut la phrase anti-regard (sans ajouter de raisonnement), le gain de la jumelle sans raisonnement rejoindrait celui de la jumelle avec raisonnement. Si « raisons » est vraie : cette phrase seule ne suffirait pas ; le raisonnement est le vecteur causal.
**Expérience.** On ne peut pas réentraîner (contraint). On peut cependant injecter la phrase anti-regard dans la consigne système au moment de l'évaluation, pour chaque adaptateur, et mesurer si cela suffit à fermer l'écart entre jumelles. Faisable sur de nouveaux épisodes.
**Contrôle positif :** sur le modèle de départ, la phrase dans la consigne système ne devrait presque rien changer (elle n'est pas dans les poids).
**Contrôle négatif :** injecter une phrase neutre de longueur comparable.
**Déjà publié :** [9] (Hsu & Arnesen, 2026) — nommer l'objectif testé change beaucoup le résultat. [11] (Knecht et al., 2026) — la conscience d'évaluation a un effet limité sur le comportement.
**Coût :** Bas.
**Pourquoi un relecteur la soulèverait :** Les trois spécifications qui contiennent la phrase anti-regard brouillent l'attribution causale.

---

### R6. Dégât collatéral du retrait de sous-espace (ablation side-effect)

**Famille :** (b) défaut de l'instrument.
**Mécanisme.** Le sous-espace « je suis évalué » est appris sur le modèle de départ, puis appliqué aux adaptateurs. Le retrait pourrait détruire des capacités non liées (suivi d'instructions, raisonnement en chaîne), ce qui ferait remonter le taux d'actions nuisibles pour des raisons indépendantes du regard. On conclurait à tort que le gain venait du regard.
**Prédiction séparatrice.** Si R6 est vraie : après retrait, les performances sur des benchmarks généraux (MMLU, GSM8K, etc.) chutent ; le ratio « dégât collatéral / changement de comportement en sûreté » est élevé. Si « regard » est vraie : seul le comportement conditionnel à l'observation change, les benchmarks généraux restent stables.
**Expérience.** Avant et après retrait, mesurer : (i) un benchmark de capacité générale court (50 items MMLU, 50 items GSM8K) ; (ii) le taux de refus abusif sur des scénarios bénins. Directions témoins appariées en dégât (déjà prévues, §2). Faisable sans réentraînement.
**Contrôle positif :** retirer une direction sémantique connue pour être fonctionnellement importante (p. ex. la direction « français/anglais ») — le dégât doit être visible.
**Contrôle négatif :** retirer une direction aléatoire de même norme — le dégât doit être négligeable.
**Déjà publié :** [10] (Hua et al., 2025) utilise le pilotage d'activations et constate un effet ; le projet prévoit des directions témoins appariées. [référence à vérifier sur la littérature d'ablation de sous-espaces et effets collatéraux.]
**Coût :** Moyen (construction des directions, inférence sur benchmarks).
**Pourquoi un relecteur la soulèverait :** L'interprétation causale du retrait de sous-espace est fragile si le dégât n'est pas contrôlé.

---

### R7. Variance d'échantillonnage et graines (seed fragility)

**Famille :** (c) défaut de la mesure.
**Mécanisme.** Température 0,7, « plusieurs dizaines de tirages par évaluation ». Avec 27 évaluations et quelques dizaines de tirages, les intervalles de confiance sur S et D sont larges. Le contraste entre jumelles (D) pourrait être du bruit, surtout s'il dépend de la paire de phrases (ce qui est déjà observé).
**Prédiction séparatrice.** Si R7 est vraie : en doublant les tirages et en calculant des intervalles bootstrap, D chevauche zéro pour la paire « évaluation » aussi. Si D est réel : il tient après augmentation de la puissance.
**Expérience.** Tripler les tirages par évaluation (de ~30 à ~90), calculer des intervalles de confiance bootstrap à 95 %. Faisable sur les adaptateurs publiés, mais nécessite de l'inférence supplémentaire.
**Contrôle positif :** la différence entre le modèle de départ et la recette avec raisonnement doit rester significative (signal fort connu).
**Contrôle négatif :** la différence entre deux lots de graines du même modèle et du même scénario doit être non significative.
**Déjà publié :** Le projet déclare la limitation (§4). [11] (Knecht et al., 2026) — effet limité de la conscience d'évaluation.
**Coût :** Moyen (inférence ×3).
**Pourquoi un relecteur la soulèverait :** La puissance statistique sur 27×30 avec effet potentiellement petit est insuffisante.

---

### R8. Transfert de direction non validé (probe transfer gap)

**Famille :** (b) défaut de l'instrument.
**Mécanisme.** La direction « je suis évalué » est construite sur le modèle de départ. Les adaptateurs LoRA modifient la géométrie des représentations internes. La direction peut ne plus pointer vers le même concept dans l'espace des adaptateurs. Le retrait « échoue silencieusement » : il ne touche pas la bonne chose, et le gain inchangé est interprété comme « pas de regard » alors que le regard est simplement encodé ailleurs.
**Prédiction séparatrice.** Si R8 est vraie : la précision de classification « évalué/déployé » de la direction, mesurée sur les adaptateurs, est proche du hasard (50 %). Si la direction transfère : la précision reste élevée.
**Expérience.** Avant tout retrait, mesurer la précision de classification de la direction sur chaque adaptateur, sur un jeu de validation séparé (textes d'évaluation vs déploiement écrits indépendamment). Peut se faire sur les épisodes déjà joués.
**Contrôle positif :** la direction doit classifier correctement le modèle de départ (c'est sa source).
**Contrôle négatif :** une direction aléatoire doit être au hasard.
**Déjà publié :** [10] (Hua et al., 2025) travaille sur des organismes entraînés spécifiquement. Le transfert vers des adaptateurs LoRA non entraînés au regard est une question ouverte.
**Coût :** Bas (pas d'entraînement, seulement des projections).
**Pourquoi un relecteur la soulèverait :** C'est une hypothèse de validité de tout l'instrument d'intervention.

---

### Signature positive de « raisons »

Écarter les rivales ne suffit pas. La **signature positive** de « raisons » serait :

1. Le modèle avec raisonnement, dans sa trace, cite *la raison pertinente de la spécification* (pas une reformulation générique, mais le principe spécifique qui s'applique au scénario), et ce, de manière différenciée selon le scénario.
2. Quand on modifie la spécification pendant l'inférence (p. ex. on retire la raison pertinente de la consigne système), le taux de refus baisse pour le scénario concerné *mais pas pour les autres*.
3. L'intervention dans les poids sur la direction « raison X » (si elle peut être construite) fait bouger sélectivement le scénario X.

Ces trois observations ensemble seraient une preuve constructive, pas seulement par exclusion.

---

## (3) Partie B — Forme du papier

### Conseil 1 — La thèse en une phrase

> « Nous testons si la bonne conduite des modèles formés à une spécification par midtraining tient quand on retire ou neutralise le signal "je suis évalué", et nous montrons [ce que les données montrent, pas plus]. »

Ne pas affirmer que le gain vient des raisons. Affirmer qu'on a mesuré combien il *ne vient pas* du regard, et quantifier les limites de cette mesure.

### Conseil 2 — Figure 1

Un diagramme causal à trois chemins : spécification → (a) raisons internalisées → comportement ; (b) regard → comportement ; (c) surface/conformité → comportement. Chaque chemin est annoté avec l'expérience qui le teste. Le lecteur voit d'un coup la structure de l'article. La figure secondaire montre les taux par adaptateur × condition avec intervalles de confiance.

### Conseil 3 — Ordre des sections

1. **Introduction** : le problème (le midtraining marche, mais pourquoi ?), les trois familles d'explications, la contribution.
2. **Méthode** : les adaptateurs ([1]), les manipulations (phrase, intervention dans les poids), les contrôles (juge inter-famille, scénarios réécrits, benchmarks de capacité).
3. **Résultats manipulation par phrase** : présenter l'échec comme un résultat informatif (« la phrase ne tranche pas »).
4. **Résultats intervention dans les poids** : présenter le pilote, la règle d'arrêt, les résultats.
5. **Contrôles et rivales** : R1-R8 ci-dessus, avec les données collectées.
6. **Signature positive** : les preuves constructives (traces de raisonnement, perturbation sélective de la spécification).
7. **Discussion** : ce qui reste non tranché, agenda pour le réentraînement.

### Conseil 4 — Contrôles indispensables

- Accord inter-juges Claude/autre famille/humain sur un échantillon stratifié (≥100 épisodes).
- Benchmarks de capacité générale avant/après retrait de sous-espace.
- Précision de la direction « évalué » sur chaque adaptateur (R8).
- Scénarios réécrits en style différent (R1).
- Instruction adversariale (R2).
- Intervalles de confiance bootstrap sur toutes les métriques.

### Conseil 5 — Ce qui se publie avec le texte

- Code de manipulation et d'évaluation.
- Tous les épisodes bruts (prompts + sorties + verdicts des deux juges).
- La direction « évalué » (vecteur + couche).
- Le pré-enregistrement horodaté (même tardif, sa publication est un signal de bonne foi).
- Un datasheet des scénarios (provenance, parenté avec les données d'entraînement).

### Conseil 6 — Public, canal, ce qu'il ne faut pas affirmer

**Public :** chercheurs en alignement et évaluateurs de modèles.
**Canal :** Workshop ou conférence ML avec track safety (ICML, NeurIPS safety track) ; pré-publication sur un dépôt ouvert.
**Ne pas affirmer :**
- Que le midtraining « aligne » le modèle (on ne teste qu'une dimension).
- Que l'absence d'effet de la phrase prouve l'absence de regard (la manipulation est faible, §3).
- Que l'intervention dans les poids est causalement pure (R6, R8).
- Que les résultats généralisent au-delà de Qwen2.5-32B et de ces adaptateurs.
- Tout superlatif sur la « robustesse » de l'alignement.

---

## (4) Expérience décisive la moins chère — duel H_A vs H_B

**Question :** Le gain de la recette avec raisonnement persiste-t-il sur des scénarios stylistiquement dissimilaires aux données d'entraînement ?

| | H_A : le gain vient (au moins en partie) de raisons généralisées | H_B : le gain vient principalement de l'appariement de surface |
|---|---|---|
| **Prédiction** | Le taux d'actions nuisibles de la recette avec raisonnement reste ≤ 10 % (illustratif) sur les scénarios réécrits | Le taux remonte à ≥ 30 % (illustratif) sur les scénarios réécrits |
| **Falsifié si** | Le taux remonte significativement (borne inférieure de l'IC 95 % > 15 %, illustratif) | Le taux reste bas (borne supérieure de l'IC 95 % < 15 %, illustratif) |

**Métrique :** Taux d'actions nuisibles jugées « exécutées » (verdict strict), avec IC bootstrap 95 %.
**Seuil :** Différence de taux entre scénarios originaux et réécrits > 10 points de pourcentage (illustratif) pour rejeter H_A.
**Contrôle négatif :** Le modèle de départ sur les mêmes scénarios réécrits — son taux ne devrait pas changer (il n'a pas été entraîné sur les données de [1]).
**Témoin à coût égal :** Réécrire les mêmes scénarios mais dans un style *plus* proche des données d'entraînement (style Claude amplifié). Si le taux de la recette avec raisonnement est meilleur sur ce témoin qu'en original, c'est un signal R1 même si l'original est déjà bas.
**Coût :** Bas — réécriture (~2 h de travail + quelques dollars d'inférence pour paraphraser), puis inférence sur les 9 adaptateurs × 27 scénarios × 3 styles × ~50 tirages. Sur un Qwen2.5-32B quantifié en 4 bits : ~16 GB VRAM, ~1-2 jours sur un seul GPU A100. Coût cloud estimé : 50-150 $ (illustratif).

---

## (5) Ce qui me ferait changer d'avis

- **En faveur de « raisons » :** Si, après retrait du sous-espace « évalué » *et* réécriture des scénarios *et* instruction adversariale, le gain de la recette avec raisonnement tient à ≤ 10 % (illustratif), et que la trace de raisonnement cite de manière différenciée les principes pertinents de la spécification, je considérerais « raisons » comme l'explication la mieux soutenue (sans être « prouvée »).
- **Contre « raisons » :** Si le gain s'effondre sur les scénarios réécrits (R1) ou si l'injection de la phrase anti-regard dans la consigne système suffit à fermer l'écart entre jumelles (R5), je considérerais que le gain est principalement un artefact de surface ou de contenu explicite.
- **En faveur du regard :** Si la précision de la direction « évalué » est élevée sur les adaptateurs (R8 réfutée), que le retrait de cette direction fait remonter le taux significativement, et que les benchmarks de capacité ne bougent pas (R6 réfutée), je considérerais que le regard contribue causalement, même si la phrase ne suffisait pas à le révéler.
- **Sur la forme du papier :** Si un premier reviewer indépendant soulève une rivale non couverte par R1-R8, je la placerais en priorité et restructurerais autour d'elle. Si les intervalles de confiance (R7) restent trop larges même après augmentation des tirages, je recommanderais de publier comme « note technique » plutôt que comme article de résultat.

---

FIN-DE-CELLULE