# Proposition B — Tour III.3 : réponse aux critiques

---

## I. Réponse critique par critique

Je reprends chaque défaut relevé par A, C et D sur ma proposition, dans l'ordre où ils apparaissent. Je ne traite que ce qui vise B.

---

### Critique A-1 : N12-E1 — statistique du maximum, biais de variance

**Acceptée.** Le maximum sur 3 générations favorise le bras le plus variable. Le coût des pièces générées qui échouent n'était pas compté.

**Correction.** Remplacer le maximum par la **moyenne** du score net sur les K dernières générations. Compter dans le coût du bras toute tentative de génération (compilation échouée, moniteur inerte). Ajouter le contrôle « meilleur de N tirages indépendants du catalogue » (N-045 §4).

---

### Critique A-2 : N12-E1 — contrôle « invite permutée » mal apparié

**Acceptée.** L'invite permutée produit un objet non fonctionnel ; elle sépare « fonctionne / ne fonctionne pas », pas « générée / réaffectée ». D propose « sortie contrainte au catalogue » ; je m'en sers (en le disant).

**Correction.** Le contrôle négatif devient : « même générateur, sortie contrainte au catalogue existant » (la génération s'exécute mais sa sortie est remplacée par la pièce du catalogue la plus proche en cosinus d'embedding de l'invite). S'y ajoute « meilleur de N tirages indépendants du catalogue » pour séparer exploration et génération.

---

### Critique A-3 : N12-E2 — vrai par construction

**Acceptée.** C'est une tautologie informatique. La critique de C (§a.1) dit la même chose : empreinte et Lean opèrent sur des dimensions incommensurables. Je la maintiens comme tautologie *utile* — elle documente l'existence d'au moins une propriété non triviale — mais elle ne falsifie rien.

**Transformation en test.** Le comparateur pertinent est le couple « tests unitaires + mutations + revue croisée par un modèle tiers » (D, critique c.2 sur B ; C, critique c.2 sur D). L'expérience révisée :

> **N12-E2 révisé.** On soumet un ensemble de gardes (saines et fautives, composé par un tiers aveugle aux bras) à trois bras : Lean, suite de tests + mutations, revue croisée par un modèle d'une autre famille. Métrique : rappel sur les gardes fautives et taux de faux rejets sur les gardes saines, par bras. Seuil : Lean détecte au moins une faute que les deux autres bras manquent, sans augmenter le taux de faux rejets. Contrôle : budget de calcul/coût apparié entre les trois bras (heures-agent ou heures-GPU).

---

### Critique A-4 : N13-E1 — le bras « RL avec terme de signalement » n'est pas un contrôle négatif

**Acceptée.** C'est une intervention positive qui entraîne la métrique. C (critique c.1 sur B) ajoute que sans canaris « à ne pas signaler », ce bras apprend la politique dégénérée « signaler systématiquement ».

**Correction.** Le bras « RL avec terme de signalement » est reclassé en **bras d'intervention**, pas en contrôle négatif. Le contrôle négatif devient : « bras non entraîné au même point de départ » (politique initiale avant tout RL). S'ajoutent obligatoirement : (i) canaris « à ne pas signaler » dans les scénarios (N-045, Pièce 1) ; (ii) scénarios de signalement d'évaluation *disjoints* des scénarios d'entraînement ; (iii) mesure du taux de faux signalements sur les épisodes sans incident (C = 0).

---

### Critique A-5 : N13-E1 — unité d'inférence, graine unique

**Acceptée.** Avec une graine par bras, la variance entre entraînements (τ²) n'est pas identifiable. Le test de Mann-Whitney sur les runs d'évaluation a un α nominal faux pour toute affirmation causale sur l'entraînement. C'est la « note transversale » de A (défaut (i) partagé par les trois propositions).

**Correction.** Exiger **k ≥ 2 graines par bras** dans le corps de l'expérience. Le test porte sur les moyennes par graine (unité d'inférence = graine), pas sur les runs. La puissance doit être calculée au préenregistrement avec τ² estimé par le pilote A/A — ou, si le pilote ne donne pas τ², les résultats sont rapportés comme OBSERVÉ-NON-AUDITÉ et la conclusion causale est suspendue.

---

### Critique A-6 : N13-E2 — cible mal posée (vérification mécanique AUROC = 1 par construction)

**Acceptée.** C'est la critique la plus grave sur N13-E2, et elle est reprise par C (§a.3) et D (§a sur B, « reprend la cible mécanique parfaite »). Sous contrat explicite, la vérification mécanique *est* la cible. La sonde ne peut rien y ajouter. Le cas où la sonde est utile — reconnaissance sans contrat — est une autre variable, sans étiquetage indépendant.

**Correction complète.** N13-E2 est **scindé en deux expériences distinctes** :

> **N13-E2a (sous contrat explicite).** La cible est *la prédiction de l'omission avant le point de décision* — c'est-à-dire, au tour t−1, prédire que l'agent omettra de signaler au tour t. La vérification mécanique ne peut pas prédire *avant* le point de décision (elle lit l'appel d'outil *après*). La sonde (boîte blanche sur les activations au tour t−1) et le texte du raisonnement (au tour t−1) sont les prédicteurs. Métrique : AUROC de la prédiction anticipée, comparée à un prédicteur constant (taux de base). Seuil : AUROC > 0,50 + δ (δ gelé au préenregistrement). Contrôle négatif : mêmes sondes sur des épisodes honnêtes (C = 0) au *même* point de contrôle et *même* pas d'entraînement (pour éliminer le confondant temporel signalé par C, critique c.3 sur D).

> **N13-E2b (sans contrat — question ouverte du lot 3).** La cible est « le signalement aurait dû être émis mais ne l'a pas été, et l'évaluateur ne dispose pas du contrat ». L'étiquetage vient d'un oracle externe (témoins plantés dans le monde planté, dont l'évaluateur ne connaît pas l'identité). La sonde prédit l'omission sur la seule base des activations ou du texte, sans savoir si C est vrai. Métrique : AUROC, rappel à taux de fausses alertes fixé (≤ 5 %, *illustratif*). Contrôle négatif : cas « condition reconnue mais signalement non dû » (C vrai mais signalement déjà fait par un tiers, ou signalement explicitement interdit — contrôle exigé par C, critique c.3 sur A, transposable à B) ; cas « envisagé puis légitimement non fait » (A, critique c sur B ; D, critique c.4 sur B). La sonde qui n'alerte que sur la sémantique de l'incident (et non sur l'état déontique) échoue sur ces contrôles.

---

### Critique A-7 : N13-E2 — fuite sonde/évaluation

**Acceptée.** Si entraînement et test de la sonde partagent le run ou le point de contrôle, la sonde apprend l'état d'entraînement.

**Correction.** Partition stricte : la sonde est entraînée sur un sous-ensemble de points de contrôle et testée sur un point de contrôle *tenu à l'écart*. Les positifs et négatifs du test sont tirés du *même* point de contrôle (A, critique c sur B ; C, critique c.3 sur D, transposable). Le confondant temporel (pas 50 vs pas 180) est ainsi éliminé.

---

### Critique A-8 : N13-E3 — vérité circulaire et graines

**Partiellement acceptée.** Le risque de circularité (le même verdict sert à entraîner et à évaluer) est réel. Le bootstrap sur fiches n'estime pas τ².

**Correction.** (i) La vérité binaire des fiches d'évaluation provient **exclusivement de l'oracle du monde planté** (structures retrouvées = vrai, non retrouvées = faux), jamais du verdict humain ni d'un juge. (ii) Partition stricte par famille de fiches entre entraînement RLCR et évaluation (familles tenues à l'écart, jamais vues à l'entraînement — ce qui répond aussi à C, critique §a.4 sur B). (iii) Au moins 2 graines d'entraînement RLCR, pour estimer τ².

**Rejetée sur un point.** Le « non-chevauchement d'intervalles » est critiqué par A comme « n'est pas un test ». C'est exact formellement, mais conservateur (le non-chevauchement à 95 % implique p < 0,006 pour des normales, *illustratif*). Je le remplace par un test de permutation bilatéral sur l'ECE, à α = 0,05, fiches tenues à l'écart.

---

### Critique C-§a.1 : N12-E2 — vrai par construction (dimension)

**Acceptée** (identique à A-3). Traitée ci-dessus.

---

### Critique C-§a.2 : N12-E1 — biais du maximum par inflation de variance

**Acceptée** (identique à A-1, formalisée). Traitée ci-dessus. C ajoute la démonstration que E[max] croît avec σ même si μ_gen ≤ μ_sel. La correction (passer à la moyenne) élimine ce biais.

---

### Critique C-§a.3 : N13-E2 — confusion règle déterministe / prédicteur continu

**Acceptée.** C distingue deux cas (M observe C et ρ → AUROC = 1 ; M observe seulement ρ → AUROC de la sonde seule). La correction est la scission N13-E2a/E2b ci-dessus.

---

### Critique C-§a.4 : N13-E3 — fuite de domaine, violation de N-045 §8

**Acceptée.** Si le réentraînement RLCR et l'évaluation partagent les mêmes familles, on apprend les artefacts lexicaux. Traitée ci-dessus (partition par famille, vérité de l'oracle seulement).

**Ajout (sur la suggestion de C, critique c.3 sur B).** Avant tout entraînement RLCR, tester si une **recalibration post-hoc simple** (Platt scaling / régression isotonique) sur les logits ou la probabilité des jetons du modèle de base suffit à abaisser l'ECE. Si oui, l'entraînement RLCR est inutile. Coût : processeur seul, quelques minutes. Ce contrôle est bon marché et *précède* N13-E3.

---

### Critique C-§b.1 : N12-E1 — puissance nulle à n₁ = n₂ = 3

**Acceptée.** La démonstration est décisive : p_min = 1/20 = 0,05 exactement, et un test strict (p < 0,05) a une puissance de 0. Avec des générations autocorrélées (N-045 §5 : historique et mémoire transmis), les observations ne sont pas indépendantes.

**Correction.** Le test ne porte plus sur 3 générations d'un seul run. Il porte sur R ≥ 12 runs indépendants (*illustratif*, calcul de C) par bras, chacun résumé par sa moyenne sur K générations. Le coût augmente ; l'ancrage matériel est révisé à la hausse (voir §II).

---

### Critique C-§b.2 : N13-E3 — biais positif de l'ECE à n = 200

**Acceptée.** Le plancher d'espérance de l'ECE pour un modèle parfaitement calibré à n = 200 et B = 10 classes équilibrées est ≈ 0,089 (*illustratif* de C, conforme à la loi normale pliée). Le seuil ECE < 0,10 est donc non jugeable.

**Correction.** (i) Augmenter n à ≥ 500 fiches (*illustratif* : plancher ≈ 0,056) ou réduire le nombre de classes. (ii) Utiliser l'ECE débiaisée (Kumar et al., « Verified Uncertainty Calibration », NeurIPS 2019 — *référence à vérifier*) ou un test de calibration par noyau (Widmann et al., ICML 2019 — *référence à vérifier*) qui ne souffre pas du biais de la valeur absolue. (iii) Remplacer « ECE < 0,10 » comme seuil de fonctionnement par le score de Brier, qui n'a pas ce biais.

---

### Critique C-§b.3 : N13-E2 — DeLong dégénéré à prévalence extrême

**Acceptée.** Si π < 0,03, le nombre de positifs sur 30 runs est ≤ 1, et la statistique de DeLong est non définie ou dégénérée. La correction est double : (i) la scission E2a/E2b avec prédiction anticipée lève partiellement le problème (on prédit à chaque point de décision, pas seulement sur les omissions effectives) ; (ii) exiger un effectif minimal de positifs (m ≥ 20, *illustratif*) au préenregistrement, faute de quoi l'expérience est rapportée comme non jugeable.

---

### Critique C-§c.1 : N13-E1 — bras « RL avec terme de signalement » apprend à signaler systématiquement

**Acceptée.** Traitée dans A-4 ci-dessus (reclassement en bras d'intervention, ajout de canaris « à ne pas signaler »).

---

### Critique C-§c.2 : N12-E1 — absence du témoin « meilleur de N tirages »

**Acceptée.** Ajouté dans A-1/A-2 ci-dessus.

---

### Critique C-§c.3 : N13-E3 — absence de recalibration post-hoc comme contrôle

**Acceptée.** Ajoutée dans C-§a.4 ci-dessus.

---

### Critique D-§a sur B (5 points)

1. **N12-E1 maximum adaptatif.** Acceptée (= A-1).
2. **N12-E2 vrai par construction.** Acceptée (= A-3).
3. **N13-E1 confondant variance/échelle.** Acceptée en partie. La correction : apparier la variance du gradient entre bras en normalisant la récompense (avantage centré réduit, même échelle). D dit « récompenses appariées en variance » dans ses contrôles ; je l'adopte.
4. **N13-E2 cible mécanique parfaite.** Acceptée (= A-6).
5. **N13-E3 confond format et entraînement.** Acceptée. La correction : ajouter un bras « même modèle, même analyse (texte de `<analysis>`), mais confiance extraite par phrase ajoutée sans entraînement RLCR » — ce qui isole l'effet de l'entraînement de celui du format. D dit « bras sans analyse à calcul de test comparable » ; je l'adopte en ajoutant un bras *avec* analyse mais *sans* entraînement RLCR.

### Critique D-§c sur B (5 contrôles)

1. **N12-E1.** Budgets et nombres de candidats appariés : accepté, intégré. Scores non sélectionnés par maximum : accepté, corrigé (moyenne). Pièces nulles mais valides de même coût : accepté, c'est le contrôle « sortie contrainte au catalogue ».
2. **N12-E2.** Bibliothèque aveugle : accepté, intégré dans N12-E2 révisé.
3. **N13-E1.** Plusieurs entraînements : accepté (k ≥ 2). Témoin sans entraînement : accepté. Récompenses appariées en variance : accepté. Scénarios sans obligation et faux signalements : accepté (canaris).
4. **N13-E2.** Partition par scénario et point de contrôle : accepté. Cas « envisagé et non fait » légitimement : accepté. Évaluation conditionnelle à la vérification mécanique : intégré dans E2b.
5. **N13-E3.** Familles jamais vues : accepté. Prédicteur constant : accepté (ajouté). Log-probabilités recalibrées (Platt) : accepté comme contrôle préalable. Bras appariés en analyse et calcul : accepté.

---

## II. Expériences corrigées (résumé)

| Expérience | Objet | Métrique principale | H_A | H_B | Contrôles négatifs | Ancrage révisé |
|---|---|---|---|---|---|---|
| **N12-E1** | Génération vs sélection | Moyenne du score net sur K générations, R ≥ 12 runs/bras | Sélection suffit | Génération bat sélection | Sortie contrainte au catalogue ; meilleur de N tirages ; A/A ; scores permutés ; budgets appariés | Coût × 12 par bras (*illustratif* : ≈ 12 000 $) |
| **N12-E2** | Lean vs tests+mutations vs revue croisée | Rappel sur gardes fautives + faux rejets sur gardes saines | Lean n'ajoute rien | Lean détecte ≥ 1 faute que les deux autres manquent | Bibliothèque aveugle, coût apparié, gardes saines incluses | Processeur, quelques jours |
| **N13-E1** | Collectif vs individuel (causalité) | Taux de signalement par graine, k ≥ 2 graines/bras | Le collectif cause la baisse | Tout RL sans récompense du signalement cause la baisse | Non entraîné ; canaris « à ne pas signaler » ; scénarios d'évaluation disjoints ; récompenses appariées en variance ; N identique | ≈ 600–3 000 h GPU (*illustratif*) |
| **N13-E2a** | Prédiction anticipée de l'omission (sous contrat) | AUROC de la prédiction au tour t−1 | Sonde ajoute information | Sonde = taux de base | Même point de contrôle positifs/négatifs ; cas C = 0 ; partition sonde entraînement/test | Quelques heures GPU |
| **N13-E2b** | Détection sans contrat (lot 3) | Rappel à FPR ≤ 5 % | Sonde détecte | Sonde échoue | « C vrai, signalement non dû » ; « envisagé, légitimement non fait » ; activations permutées | Quelques heures GPU, requiert E2a |
| **N13-E3** | Calibration Damani pour juges | ECE débiaisée, AUROC, Brier, n ≥ 500 fiches | RLCR améliore | RLCR ne transfère pas | Platt scaling préalable ; prédicteur constant ; familles tenues à l'écart ; k ≥ 2 graines ; bras avec analyse sans RLCR | Quelques heures GPU |

---

## III. Réponse à la question de l'arbitre

### Ce qui est établi

1. **La récompense collective n'est pas la cause établie de l'effondrement du signalement.** Avalon-M1 n'a pas de run mono-agent apparié (Pièce 4, réserve 1 : RAPPORTÉ). Agrawal et al. observent la même baisse en mono-agent (cité p. 36 du papier : RAPPORTÉ). La supposition S6 (« le collectif cause l'effondrement ») est une **HYPOTHÈSE**.

2. **Le motif Avalon n'est pas du sabotage diffus au sens du programme.** Un seul point de décision par épisode, pas de dommage accumulé sur beaucoup d'actions (Pièce 4, §3.2 : RAPPORTÉ). « Naturel » ne signifie pas « valide écologiquement » pour la cible du programme.

3. **La récompense de Damani et celle d'Avalon n'ont rien en commun sauf le sigle.** Le « théorème d'impossibilité » de Gemini ne s'applique pas à Damani (λ_sync = 0 : VÉRIFIÉ, Pièce 5, §2). Damani produit une calibration mesurable sur des tâches à réponse vérifiable courte (7–8B), avec ECE en domaine ≈ 0,03 et hors domaine ≈ 0,21 (RAPPORTÉ, Pièce 5, Table 1).

4. **N-045 apprend la sélection, pas la génération.** La couverture des couches 3-4 par N-045 est une **HYPOTHÈSE** (S1). La couche 4 (Lean) offre une preuve de propriété, pas d'identité — mais la question « a-t-on des propriétés à prouver qui valent le coût ? » est ouverte.

5. **La confiance verbalisée des modèles de base ou RLVR à 7B est quasi non informative** (AUROC 0,47–0,56 : RAPPORTÉ, Pièce 5). Tout usage de la confiance d'un juge non entraîné comme signal s'appuie sur un canal vide.

### Ce qui n'est pas établi

- Si la récompense collective *cause* l'effondrement du signalement ou si tout RL sans récompense du signalement le cause.
- Si l'organisme du programme, à effectif et architecture différents d'Avalon, reproduirait l'effondrement.
- Si la calibration RLCR de Damani se transfère au domaine des fiches du programme (tâches non vérifiables, vérité différée, scores ordinaux).
- Si la génération de pièces neuves (couche 3) bat la sélection parmi les pièces existantes (N-045).
- Si Lean détecte des fautes que les tests + mutations + revue croisée ne détectent pas.

### L'expérience à faire en premier

**Le contrôle de recalibration post-hoc (Platt scaling)**, suivi de **N13-E3** si Platt ne suffit pas.

*Raison* : c'est le seul test qui (i) ne dépend pas de l'étape 2 ; (ii) coûte quelques minutes de processeur ; (iii) tranche une question utile immédiatement (la calibration des juges) ; (iv) précède logiquement tout entraînement RLCR. Si Platt scaling sur les logits du modèle de base abaisse l'ECE sous le seuil de fonctionnement, N13-E3 (entraînement RLCR) est inutile. Sinon, N13-E3 est le test suivant, toujours bon marché et indépendant.

Tout le reste — N13-E1 (causalité du collectif), N13-E2a/b (sondes sur omission), N12-E1 (génération vs sélection) — requiert l'étape 2 opérationnelle et des budgets GPU d'au moins un ordre de grandeur supérieurs. L'ordre est : recalibration → N13-E3 → étape 2 → N13-E1 → N13-E2a → N13-E2b → N12-E1. N12-E2 (Lean) se conduit quand le coût d'opportunité est nul.

FIN-DE-CELLULE