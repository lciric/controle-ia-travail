# Lecture vérifiée — Damani et collègues, « Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty » (arXiv 2507.16806v2, ICLR 2026) — v1

Lecteur : Sonnet neuf, lignée conv-audit, qui n'a rien écrit sur ce papier. Écrite le 2026-10-31 vers 13:20 UTC. Lecture sur processeur seulement : aucun appel réseau ni modèle, aucun fichier existant modifié, aucune empreinte compagnon écrite (note non scellée, un seul lecteur : à contre-lire avant de s'y appuyer).

**Pièce** : `docs/sources/pdf/rlcr-v1/2507.16806v2-damani-beyond-binary-rewards.pdf`. Empreinte SHA-256 recalculée : `f393de47234962cad0c7ebccb8d0ab17b4236fbc927b4e3e93330c2b0d46ab6d`, identique à celle de `provenance-rlcr-v2.md`. 39 pages (`pdfinfo`).

**Méthode** : texte extrait par `pdftotext -layout` (copie hors dépôt), 39 pages lues en entier, annexes comprises ; pages 2, 7, 8, 9, 16, 25, 26, 27 consultées aussi en image (tableaux, formules, figures). Les numéros de page sont ceux du PDF (ils coïncident avec les folios imprimés).

**Conventions** : tout chiffre renvoie à une page lue (R7). « Lecture visuelle » : valeur lue sur une figure, approximative. « Calcul du lecteur » : absent du papier, refait par moi (scripts hors dépôt, `/tmp`). « Non couvert par ce papier » : absent de ces 39 pages, sans conclusion sur le champ (R8). Les citations en anglais sont littérales ; un texte du papier mis entre guillemets français est ma traduction.

---

## 0. Résumé en trois lignes

1. Damani et collègues (MIT) entraînent un modèle de raisonnement à rendre une réponse, une analyse de ses incertitudes et une confiance chiffrée, avec la récompense justesse − (confiance − justesse)² (Éq. 8, p. 4) ; le théorème 1 (p. 4, preuve pp. 16–17) dit que l'espérance est maximale pour la réponse la plus probable accompagnée de la confiance vraie.
2. Sur Qwen2.5-7B, l'erreur de calibration attendue passe de 0,37 à 0,03 (HotpotQA) et de 0,26 à 0,10 (mathématiques) à justesse comparable ; hors domaine, de 0,46 à 0,21 en moyenne (entraînement HotpotQA), avec des cas restés mauvais (0,34 sur SimpleQA) (pp. 2, 7, 31).
3. La récompense ne couple la confiance à aucune référence antérieure ; le papier ne contient ni moniteur, ni adversaire, ni test causal de fidélité, ni sonde sur les activations du modèle RLCR (la seule sonde porte sur le modèle RLVR, p. 5) : non couvert par ce papier.

---

## 1. Fiche

### 1.1 Objet (pp. 1–3)

- Problème (p. 1) : l'apprentissage par renforcement à récompense binaire de justesse (RLVR, « récompenses vérifiables ») ne pénalise ni le pari ni la confiance faible ; il dégrade la calibration et augmente les réponses fausses. Deux questions (p. 2) : (1) peut-on optimiser conjointement justesse et calibration ? (2) le contenu de la chaîne de raisonnement peut-il améliorer la calibration ?
- Méthode (p. 1) : RLCR, « Reinforcement Learning with Calibration Rewards » (apprentissage par renforcement avec récompenses de calibration). Le modèle écrit `<think>`, `<answer>`, `<analysis>`, `<confidence>` dans cet ordre (Fig. 1a, p. 2) : l'analyse est un texte sur les incertitudes, la confiance un nombre dans [0, 1] donné après la réponse.
- Résultats annoncés (pp. 2–3) : théorème ; calibration conservée ou améliorée en domaine et hors domaine à justesse comparable ; confiance utilisable dans la mise à l'échelle au moment du test ; cohérence accrue des confiances.
- Code, modèles et démonstrations annoncés à `https://rl-calibration.github.io/` (p. 1) : non consulté ; disponibilité non vérifiée.

### 1.2 Récompense (Éq. 1, p. 2 ; Éq. 8, p. 4 ; Fig. 2, p. 4)

R_RLCR(y, q, y*) = 1[y ≡ y*] − (q − 1[y ≡ y*])².

- Bonne réponse : 1 − (1 − q)², de 0 (q = 0) à 1 (q = 1). Mauvaise réponse : −q², de 0 à −1 (calcul du lecteur, conforme à la Fig. 2, p. 4).
- La récompense est une fonction de (réponse, confiance, vérité) seulement.
- À l'entraînement s'ajoute une récompense de format (balises présentes et dans l'ordre), « pondérée également » avec la récompense de calibration (p. 18) ; le papier ne donne ni formule d'ensemble ni échelle, et ne dit pas si « calibration » désigne là l'Éq. 8 entière ou le seul terme de Brier.

### 1.3 Théorème 1 et preuve (p. 4 ; annexe A, pp. 16–17)

**Énoncé (p. 4).** Hypothèse : pour toute prédiction y, l'indicateur de succès 1[y ≡ y*] suit une loi de Bernoulli(p_y). Conclusions : (1) *incitation à la calibration* : pour tout y, l'espérance de R_RLCR est maximale quand q = p_y ; (2) *incitation à la justesse* : parmi les prédictions calibrées (y, p_y), l'espérance est maximale pour celle dont p_y est le plus grand. Note 2 (p. 4) : p_y peut être une probabilité subjective d'un prédicteur limité en information ou en calcul, puisque le résultat est déterminé une fois y fixé. Remarque (p. 4) : le terme de Brier ne peut pas être remplacé par n'importe quelle règle propre (la perte logarithmique n'incite pas à la justesse) ; une version analogue existe pour toute règle propre bornée vérifiant « S(p, 1) − S(p, 0) < λ pour un certain λ ».

**Preuve (annexe A).**
- Famille plus générale que le texte (p. 16) : R(c, q) = λc − S(q, c), avec S une règle de score, λ > 0 la récompense de la bonne réponse, c un signal binaire de justesse arbitraire et p_y := p(c = 1 | y). Espérance : V(y, q) = λp_y − [p_y S(q, 1) + (1 − p_y) S(q, 0)].
- Lemme 1 : V(y, ·) est maximale en q = p_y si et seulement si S est propre (le terme λp_y ne dépend pas de q).
- Lemme 2 : pour p_y ≥ p_y′, V(y, p_y) ≥ V(y′, p_y′) si et seulement si S(p, 1) − S(p, 0) ≤ λ pour tout p ∈ [0, 1]. Preuve : W(p) = valeur maximale atteignable pour une réponse de probabilité de succès p ; on dérive ; la représentation de Savage–Dawid (Gneiting & Raftery 2007) donne S′(p, 1) = −(1 − p)ω(p), S′(p, 0) = pω(p), ω ≥ 0 ; W est croissante si et seulement si la différence est majorée par λ.
- Théorème 1 : cas λ = 1, S = Brier ; max_p [S(p, 1) − S(p, 0)] = 1 (p. 16).
- Corollaire 1 (pp. 16–17, S strictement propre) : (1) si S(p, 1) − S(p, 0) est borné, il existe un λ fini qui satisfait la condition, donc incitation conjointe à la calibration et à la justesse ; (2) s'il ne l'est pas, pour tout λ fini il se peut qu'existent y, y′ avec p_y ≥ p_y′ et W(p_y) < W(p_y′) : la récompense préfère alors (y′, p_y′). Brier : 1 − 2p ≤ 1, donc λ = 1. Logarithmique : log((1 − p)/p) → ∞ quand p → 0, aucun λ fini.
- Illustration (annexe E, pp. 22–24) : espérance à calibration parfaite, Éq. 12–13 et Fig. 5 (p. 22) : strictement croissante pour Brier, non monotone pour le logarithme. Tâche jouet à cinq bras (p. 23) : la variante logarithmique converge vers une réponse invalide (−1) avec q = 0 (justesse 0, Brier 0,00, ECE 0,00) ; la variante Brier garde 34,4 % de justesse (ECE 0,02). Sur HotpotQA, pas de détournement observé pour le logarithme (justesse 59,5 % contre 62,1 %, ECE 0,07 contre 0,03 ; Table 3, p. 24).

**Conditions exactes (lecture du lecteur).** L'énoncé tient si : (i) la récompense a la forme λc − S(q, c) ; (ii) S est propre ; (iii) sup_p [S(p, 1) − S(p, 0)] ≤ λ ; (iv) c est binaire et de loi p_y, éventuellement subjective (note 2). Il garantit l'*existence d'un maximum* de l'espérance, pas que l'apprentissage par renforcement l'atteigne. Il dit « maximale quand q = p_y », non « uniquement quand » ; l'unicité vient de la stricte propreté du Brier, que le papier invoque sans la démontrer (p. 16 : « the Brier score is a proper scoring rule »).

**Vérifications et coquilles (calcul du lecteur, hors dépôt).**
- Brier, λ = 1 : l'espérance maximale pour une réponse de probabilité de succès p vaut W(p) = p² (cohérent avec l'Éq. 12, p. 22) ; le maximum en q est bien q = p.
- La différence S(p, 1) − S(p, 0) = 1 − 2p vaut exactement 1 en p = 0 : avec λ = 1 la condition est atteinte *avec égalité*. L'inégalité stricte « < λ » du texte principal (p. 4) ne couvre donc pas le cas λ = 1 que la preuve utilise ; c'est la version « ≤ λ » de l'annexe (p. 16) qui est juste.
- Annexe A, p. 16 : W(p) est imprimée sans crochets autour des deux derniers termes ; la dernière ligne du calcul de W′(p) est imprimée « = S(p, 1) − S(p, 0) », alors que le calcul donne λ − [S(p, 1) − S(p, 0)] (vérifié par dérivation numérique). La phrase qui suit (« W est croissante si et seulement si S(p, 1) − S(p, 0) ≤ λ ») est exacte : coquille sans conséquence sur la conclusion.
- Logarithme naturel avec λ = 1 : W décroît pour p < 1/(1 + e) ≈ 0,27 (absent du papier, qui ne précise pas la base du logarithme).
- Réserve : la preuve invoque la représentation de Savage–Dawid sans énoncer d'hypothèse de régularité (dérivabilité de S). Je n'ai pas lu Gneiting & Raftery (2007) ; à vérifier à la source si une règle non dérivable est visée. Le résumé dit « toute règle propre bornée » (p. 1) ; la condition exacte porte sur la majoration de S(p, 1) − S(p, 0) (pp. 16–17).

### 1.4 Modèles et entraînement (pp. 5, 18, 21, 24)

- Modèle principal : Qwen2.5-7B de base (p. 5). Autres : OLMo-2-7B-Instruct et Qwen3-8B (annexe F, p. 24).
- Algorithme : GRPO modifié (pp. 5, 18) : division par l'écart type retirée de l'avantage (d'après Turtel et al. 2025), perte BNPO, 32 réponses par invite à température 0,7, taille de lot effective 2 048, taux d'apprentissage constant avec échauffement (1e-6 HotpotQA, 5e-6 mathématiques, rapport d'échauffement 0,1), longueur maximale 1 536 (HotpotQA) ou 4 096 (mathématiques), une époque, cartes A100 et H100. Départ du modèle de base, **sans régularisation par divergence de Kullback–Leibler** (p. 5).
- Variante « SFT+RLCR » (mathématiques ; pp. 6, 18) : réglage supervisé préalable léger sur 500 exemples (solutions du modèle de base, analyses d'incertitude écrites par DeepSeek-R1 ; **la confiance n'est pas demandée à R1**, p. 18), puis RLCR. Invite de R1 : p. 21.
- Invites : « longue » pour HotpotQA, « simple » pour les mathématiques (pp. 18, 20).
- Lignes de comparaison (p. 5) : modèle de base ; RLVR (confiance demandée à l'évaluation par une phrase ajoutée, p. 19) ; RLVR + classifieur de confiance (entropie croisée binaire, ou erreur quadratique), initialisé depuis Qwen2.5-7B de base et entraîné sur les sorties de RLVR ; RLVR + sonde linéaire sur l'embedding de la dernière couche (position du jeton non précisée) ; probabilité moyenne des jetons de la réponse. Annexe I (p. 28) : calibration seule (séquence entière ; analyse + confiance seulement) et apprentissage de l'abstention (récompense ternaire, λ = 0,5).

### 1.5 Jeux de données (pp. 5–6, 18–20)

- Entraînement : HotpotQA-Modified, 20 000 exemples, 8 paragraphes dont 0, 1 ou 2 pertinents (un tiers chacun), correspondance exacte ; Big-Math Digits, 15 000 problèmes à réponse numérique (taux de résolution de LLaMA-8B entre 0 et 70 %), math-verify (p. 18).
- Évaluation (p. 19) : HotpotQA distracteur (1 000 exemples), HotpotQA-Modified (500), TriviaQA (2 000, sans contexte), SimpleQA (4 326), MATH-500, GSM8K (1 319), Big-Math-Digits (1 000), CommonsenseQA (1 220), GPQA (448). Température 0.
- Justesse : correspondance exacte, math-verify, ou « juge » Llama-3.1-8B-Instruct à température 0 pour TriviaQA, SimpleQA, CommonsenseQA, GPQA, sans lui montrer la trace de raisonnement (pp. 19–20). La validité de ce juge n'est pas rapportée.

### 1.6 Métriques de calibration (p. 5 ; pp. 8–9, 26–27, 31–33)

- Justesse ; AUROC (aire sous la courbe ROC : la confiance sépare-t-elle bonnes et mauvaises réponses) ; score de Brier (écart quadratique moyen entre confiance et justesse) ; erreur de calibration attendue (ECE), 10 classes (largeur des classes non précisée) (p. 5).
- Diagrammes de fiabilité avec histogrammes des confiances (Figs. 8–9, p. 26).
- Cohérence : écart type de la confiance sur K analyses pour une même réponse (p. 9, Fig. 4a ; N = 16 p. 27) ; somme des confiances moyennes par réponse distincte, qui devrait être ≤ 1 pour des réponses exclusives (Éq. 11 et Fig. 4b, p. 9).
- Intervalles de confiance à 95 % par bootstrap (demi-largeurs) sur justesse, AUROC et Brier, **pas sur l'ECE** (Tables 8–15, pp. 31–33) ; le nombre de rééchantillonnages n'est pas donné.

### 1.7 Résultats chiffrés principaux

**Table 1 (p. 7, vérifiée en image)** — « HD » = moyenne hors domaine (6 jeux pour HotpotQA, 5 pour les mathématiques). La justesse de RLVR est partagée par ses quatre lignes dérivées (classifieurs, sonde, probabilité de la réponse), qui lisent les sorties de RLVR (p. 19).

Entraîné sur HotpotQA :

| Méthode | Justesse | AUROC | Brier | ECE | Justesse HD | AUROC HD | Brier HD | ECE HD |
|---|---|---|---|---|---|---|---|---|
| Base | 39,7 % | 0,54 | 0,53 | 0,53 | 53,3 % | 0,54 | 0,41 | 0,40 |
| RLVR | 63,0 % | 0,50 | 0,37 | 0,37 | 53,9 % | 0,50 | 0,46 | 0,46 |
| RLVR + classifieur BCE | (63,0 %) | 0,66 | 0,22 | 0,07 | (53,9 %) | 0,58 | 0,27 | 0,24 |
| RLVR + classifieur Brier | (63,0 %) | 0,65 | 0,22 | 0,09 | (53,9 %) | 0,60 | 0,32 | 0,33 |
| RLVR + sonde linéaire | (63,0 %) | 0,55 | 0,24 | 0,10 | (53,9 %) | 0,53 | 0,38 | 0,38 |
| Probabilité de la réponse | (63,0 %) | 0,72 | 0,36 | 0,36 | (53,9 %) | 0,60 | 0,42 | 0,42 |
| **RLCR** | 62,1 % | 0,69 | 0,21 | 0,03 | 56,2 % | 0,68 | 0,21 | 0,21 |

Entraîné sur Big-Math (justesse « Math » = moyenne de MATH-500, GSM8K, Big-Math) :

| Méthode | Justesse | AUROC | Brier | ECE | Justesse HD | AUROC HD | Brier HD | ECE HD |
|---|---|---|---|---|---|---|---|---|
| Base | 56,1 % | 0,56 | 0,40 | 0,39 | 47,8 % | 0,53 | 0,46 | 0,45 |
| RLVR | 72,9 % | 0,47 | 0,28 | 0,26 | 52,5 % | 0,52 | 0,49 | 0,49 |
| RLVR + classifieur BCE | (72,9 %) | 0,78 | 0,15 | 0,10 | (52,5 %) | 0,55 | 0,34 | 0,33 |
| RLVR + sonde linéaire | (72,9 %) | 0,65 | 0,19 | 0,13 | (52,5 %) | 0,53 | 0,33 | 0,30 |
| Probabilité de la réponse | (72,9 %) | 0,52 | 0,26 | 0,26 | (52,5 %) | 0,52 | 0,44 | 0,43 |
| **RLCR** | 72,7 % | 0,67 | 0,17 | 0,10 | 50,9 % | 0,60 | 0,28 | 0,25 |
| RLCR avec réglage préalable | 72,2 % | 0,78 | 0,14 | 0,08 | 43,8 % | 0,66 | 0,24 | 0,18 |

(Ligne « classifieur Brier » des mathématiques omise : 0,78 / 0,15 / 0,10 ; HD 0,57 / 0,28 / 0,27.)

- Recoupement avec les tableaux détaillés : les moyennes de justesse (RLCR 56,2 %, RLVR 53,9 %, base 53,3 % ; mathématiques RLVR 72,9 %, RLCR 72,7 %, réglage préalable 72,2 %, base 56,1 %) et de l'ECE de RLCR (0,21), ainsi que les justesses hors domaine de l'entraînement sur les mathématiques (RLCR 50,9 %, RLVR 52,5 %, réglage préalable 43,8 %, base 47,8 %) et l'ECE hors domaine de RLCR (0,25), recalculées à la main à partir des Tables 8–10 et 12–15 (pp. 31–33), sont conformes à la Table 1.
- Justesse « comparable » : 62,1 % contre 63,0 % sur HotpotQA, intervalles de ±3,05 points chacun (Table 11, p. 32) à n = 1 000 (p. 19) ; 72,7 % contre 72,9 % en mathématiques.
- Probabilité de la réponse : AUROC le plus haut en domaine sur HotpotQA (0,72, en gras dans la Table 1) mais ECE 0,36 : bonne discrimination, mauvaise calibration. Les auteurs l'expliquent par l'engagement du modèle dans une réponse pendant le raisonnement (p. 6).
- Autres modèles (annexe F, p. 24) : OLMo-2-7B-Instruct, RLCR contre RLVR : ECE 0,09 contre 0,38 en domaine, 0,20 contre 0,48 hors domaine (Table 4). Qwen3-8B : ECE 0,23 contre 0,36 en domaine, 0,17 contre 0,29 hors domaine (Table 5) ; en domaine le gain est bien plus faible que sur Qwen2.5-7B (0,03).
- Bases de la littérature (annexe I, Table 6, p. 28), HotpotQA : calibration seule sur la séquence entière → justesse 0, ECE 0,00 (réponses vides avec confiance 0) ; calibration seule sur analyse + confiance, départ RLVR → 62,0 %, AUROC 0,53, Brier 0,24, ECE 0,08 (hors domaine ECE 0,25) ; abstention → 62,1 %, AUROC 0,61, ECE 0,31 (hors domaine 0,35) ; RLCR → ECE 0,03 (hors domaine 0,21).
- Mise à l'échelle au moment du test (§4.4, pp. 6, 8 ; Fig. 3, lecture visuelle) : sur sept jeux, avec le modèle RLCR entraîné sur HotpotQA, le vote pondéré par la confiance passe d'environ 0,55 (N = 1) à environ 0,60 (N = 16), au-dessus du vote simple (≈ 0,597), du maximum de confiance (≈ 0,574) et des variantes à base de vraisemblance de génération (≈ 0,597 et ≈ 0,569) ; l'ensemble de K analyses fait passer le Brier d'environ 0,214 à 0,207 (K = 1 → 16), gain « relativement modeste » selon les auteurs (p. 8). Pas de barres d'erreur sur ces figures.
- Cohérence (§4.5, pp. 8–9) : l'écart type de la confiance pour une même réponse est le plus souvent faible (mode ≈ 0,05–0,07, lecture visuelle de la Fig. 4a) ; la somme des confiances par réponse distincte est proche de 1 en domaine ; hors domaine, RLCR et RLVR dépassent 1 (surconfiance), RLCR moins (Fig. 4b).

### 1.8 Généralisation hors domaine (pp. 6–7, 24, 29, 31–33)

- Entraîné sur HotpotQA : les auteurs écrivent que l'entraînement n'améliore pas la justesse hors domaine, le modèle de base faisant à peu près aussi bien que les modèles entraînés (base 53,3 %, RLVR 53,9 % ; RLCR 56,2 %) ; RLVR *dégrade* la calibration par rapport à la base (ECE 0,46 contre 0,40) ; RLCR l'améliore (0,21) (p. 6, Table 1a, p. 7).
- Confiance de RLVR : presque tout entre 0,9 et 1,0 en domaine (Fig. 8b, p. 26) et « s'effondre à 1,0 quelle que soit la justesse » hors domaine ; des confiances verbalisées de 0,8–0,9 correspondent à environ 0,3 de justesse en moyenne (p. 26). RLCR utilise toute la plage (0–1) (pp. 26–27).
- Entraîné sur les mathématiques : RLCR 50,9 % de justesse hors domaine contre 52,5 % pour RLVR ; avec réglage préalable, 43,8 % (p. 7). Les auteurs ont trouvé que le modèle identifie souvent la bonne réponse dans son raisonnement puis écrit un nombre aléatoire dans les balises de réponse ; une ligne ajoutée à l'invite redonne 49,8 % (p. 29), ce qu'ils attribuent surtout à un biais de format appris, et en partie à l'oubli.
- **Hétérogénéité par jeu** (p. 31, Tables 8–10, entraînement HotpotQA) : RLCR n'est pas le meilleur partout. SimpleQA : ECE 0,34 et Brier 0,24, contre 0,06 et 0,11 pour le classifieur de Brier. CommonsenseQA : ECE 0,30 contre 0,09 pour RLVR, que les auteurs jugent « spurieux » (confiance uniformément gonflée qui coïncide avec une justesse de 90 %, p. 31). GSM8K : ECE 0,20, égal à RLVR (0,20) et supérieur à celui du classifieur BCE (0,07). Entraîné sur les mathématiques, SimpleQA : ECE 0,54 pour RLCR (Table 12, p. 32).
- Explications proposées (p. 6) — **hypothèses non testées séparément** : raisonnement sur l'incertitude ; non-stationnarité de l'entraînement ; représentations partagées entre résolution et calibration.

### 1.9 Rôle du raisonnement sur l'incertitude (pp. 6, 9–10, 18, 25, 37–38)

- Ablation (§4.6, Table 2, p. 10 ; HotpotQA / hors domaine) : RLCR (analyse) Brier 0,21 / 0,21, ECE 0,03 / 0,21, 249 / 300 jetons ; RLCR sans analyse 0,23 / 0,26, ECE 0,09 / 0,26, 113 / 179 jetons ; RLVR avec analyse 0,35 / 0,41, ECE 0,34 / 0,39 ; RLVR 0,37 / 0,46, ECE 0,37 / 0,46, 92 / 142 jetons. Lecture des auteurs : l'analyse améliore la calibration dans les deux cas ; la récompense de calibration pèse beaucoup plus que l'invite seule ; les deux composantes contribuent.
- **Réserve du lecteur** : « RLCR sans analyse » est le modèle entraîné *avec* analyse, évalué avec la consigne de ne pas en faire (p. 9) ; aucun modèle n'est *entraîné* sans analyse sur HotpotQA ni sur les mathématiques (le jeu à cinq bras de l'annexe E n'utilise pas d'analyse mais ne la compare pas, p. 23). Une part de l'écart peut venir du décalage entre entraînement et évaluation.
- Qualité de l'analyse : en mathématiques, les analyses obtenues par RLCR direct restent « génériques, souvent sans lien avec des étapes précises de la solution » (p. 18) ; d'où le réglage préalable avec des analyses d'un autre modèle. Exemple choisi par les auteurs (pp. 37–38) : l'analyse du modèle avec réglage préalable désigne les étapes fautives de son propre raisonnement.
- Test de fidélité du papier (annexe G, p. 25) : les auteurs citent Chen et al. 2025 (chaînes de raisonnement parfois non fidèles) et reconnaissent que l'analyse pourrait ne pas informer la confiance. Test : deux classifieurs de confiance, l'un sur les sorties de RLVR (sans analyse), l'autre sur les sorties de RLCR *sans la balise de confiance*. À 0,5 et 1,5 milliard de paramètres, le classifieur « avec analyse » a un meilleur Brier (≈ 0,21 contre ≈ 0,25, lecture visuelle de la Fig. 7) ; à 7 milliards, ≈ 0,20 contre ≈ 0,21, barres d'erreur qui se recouvrent ; sur l'ECE les barres se recouvrent à toutes les tailles (lecture visuelle ; la nature des barres n'est pas précisée dans la légende). Conclusion des auteurs : un classifieur assez puissant retrouve les indices dans la solution seule ; l'analyse aide les petits.
- Ce que ce test montre et ne montre pas (lecture du lecteur) : l'analyse contient de l'information utile pour prédire la justesse, surtout pour un lecteur de petite taille. Il ne montre pas que *la confiance déclarée dépend causalement de l'analyse* (aucune intervention sur l'analyse, aucune comparaison de la confiance à une confiance recalculée à partir du texte par un lecteur indépendant) : non couvert par ce papier.

### 1.10 Limites reconnues par les auteurs

Il n'y a pas de section de limites ; les aveux sont dispersés.
- Conclusion (p. 11) : l'erreur de calibration hors domaine reste « souvent élevée en valeur absolue » et les modèles peuvent encore donner une confiance forte à plusieurs réponses contradictoires. Fig. 4 et texte (p. 9) : « la surconfiance demeure ».
- p. 31 : « considérable variance » de la calibration selon le jeu hors domaine ; « marge d'amélioration significative ».
- pp. 7, 29 : perte de justesse hors domaine de SFT+RLCR (oubli, biais de format).
- pp. 23–24 : détournement de la variante logarithmique observé sur le jeu jouet, pas sur HotpotQA ; l'apparition dépendrait des données et de la taille du modèle.
- p. 28 : la calibration seule s'effondre ; la récompense d'abstention peut freiner l'exploration.
- p. 25 : le rapport entre capacité du classifieur et contenu de la chaîne de raisonnement est laissé pour des travaux futurs.
- p. 4 note 2 : l'incertitude épistémique et aléatoire ne sont pas distinguées. p. 3 note 1 : une seule réponse et une seule confiance, pas une distribution.

### 1.11 Réserves du lecteur

1. **Aucune graine ni répétition d'entraînement rapportée** (aucune occurrence de « seed » ; la p. 18 dit seulement que les résultats sont « consistent » entre cartes A100 et H100). Les intervalles des pp. 31–33 sont des bootstrap sur les exemples d'évaluation, pas sur les entraînements : les écarts de quelques points (justesse 62,1 contre 63,0 ; ECE hors domaine 0,21 contre 0,24 pour le classifieur BCE) ne sont pas des écarts établis.
2. Étiquettes de justesse de quatre jeux fournies par un modèle de 8 milliards non validé (pp. 19–20) : le bruit d'étiquette affecte ECE et AUROC.
3. Cohérence intra-solution : la Fig. 4a (modèle RLCR, p. 9) et la Fig. 10 (un seul modèle, non nommé sur la page, p. 27) ne montrent aucune comparaison avec RLVR (qui n'a pas d'analyse) ; l'introduction (p. 3) affirme pourtant une réduction de variance et renvoie à « Section 4.4 » (la cohérence est en 4.5).
4. Mise à l'échelle au moment du test : une courbe, sans barres d'erreur (Fig. 3, p. 8) ; à N = 16, vote pondéré ≈ 0,601 contre vote simple ≈ 0,597 (lecture visuelle).
5. Modèles de 7 à 8 milliards seulement, tâches de questions-réponses et de mathématiques à réponse courte vérifiable ; tâches agentiques, longues, ou à vérité différée : non couvert par ce papier.
6. Coquilles à connaître avant de citer : annexe A (p. 16) comme ci-dessus ; texte principal (p. 4) « < λ » contre annexe « ≤ λ » ; corollaire 1 (2), p. 17 : « y ≥ y′ » écrit pour p_y ≥ p_y′ ; « RLVR also improves the coherence » (p. 3, probablement RLCR) ; renvoi à « Section 4.6 » (note 1, p. 3, probablement 4.5) ; sonde f_θ = log σ(θᵀφ) (p. 5, probablement σ seul) ; légende de la Table 1 (p. 7) : « Appendix K » pour les résultats par jeu, qui sont aux annexes L et M (pp. 31–33) ; légende de la Table 7 (p. 29) « 48 % » contre 49,8 % dans le texte et le tableau ; panneaux (b) des Figs. 8–9 titrés « RLVR with Analysis » / « RLVR+Analysis » (p. 26), alors que légende et texte parlent de RLVR ; exemples des pp. 34–39 sans lettre d'annexe.

### 1.12 Recoupement de `provenance-rlcr-v2.md`

- Confirmé : empreinte ; 39 pages ; en-tête « Published as a conference paper at ICLR 2026 » et « arXiv:2507.16806v2 [cs.LG] 15 May 2026 » (p. 1) ; récompense (Fig. 1, p. 2 ; Éq. 1, p. 2 ; Éq. 8, p. 4) ; théorème 1 et remarque sur le logarithme (p. 4).
- **À corriger dans la provenance et dans la consigne** : le papier liste **sept** auteurs (p. 1) : Damani, Puri (contribution égale), Slocum, Shenfeld, **Choshen**, Kim, Andreas. Les deux textes en citent six.
- Précision : la condition « pour toute règle propre bornée » (p. 4) s'écrit « < λ » dans le texte et « ≤ λ » dans l'annexe (pp. 16–17).
- Confirmé avec nuances : « aucun terme ne couple la confiance à un ancrage » (voir §2 pour les formes examinées).

---

## 2. Le « théorème d'impossibilité » de Gemini face à la récompense de Damani

**Ce que suppose Gemini** (`brouillons/canal-reprise-releve-v1/envois/gemini-theoreme-reponses-v1/reponse-session-1-v1.txt`, section 2). (H1) : Φ strictement convexe, C². (H2) : récompense R(U, q^(T), p^(0)) = U − λ_cal D_Φ(U‖q^(T)) + λ_sync[D_Φ(U‖p^(0)) − D_Φ(U‖q^(T)) − D_Φ(q^(T)‖p^(0))] avec λ_cal > 0 et **λ_sync ≠ 0**, où p^(0) est une estimation de référence mesurable avant la délibération (sonde pré-acte, consensus initial). (H3) : μ_T ≠ p^(0). Conclusion : la dérivée de l'espérance en q = μ_T vaut −λ_sync(Φ′(μ_T) − Φ′(p^(0))) ≠ 0, donc la récompense n'est pas strictement propre. Gemini écrit lui-même, dans « Portée du théorème », que le résultat **ne s'applique pas** aux « règles de score purement terminales où λ_sync = 0 ».

**Réponse : non, la récompense de Damani ne contient aucun couplage de ce type.** Dans les notations de Gemini, c'est le cas Φ(x) = x², λ_cal = 1, λ_sync = 0, sans p^(0) : U − D_Φ(U‖q) = 1[y ≡ y*] − (q − 1[y ≡ y*])². (H1) est satisfaite (Φ″ = 2) ; (H2) ne l'est pas ; le théorème ne s'applique pas. Le lemme 1 de Damani (p. 16) *est* le cas λ_sync = 0 : l'optimum est q = p_y.

| Forme possible de couplage à une référence antérieure | Dans le papier ? | Pages |
|---|---|---|
| Terme de récompense reliant la confiance finale à une confiance ou une estimation antérieure (sonde pré-acte, consensus, confiance initiale) | **Non.** La récompense est une fonction de (réponse, confiance, vérité) seulement. | p. 2 (Éq. 1) ; p. 4 (Éq. 8) ; p. 16 (famille λc − S(q, c)) |
| Régularisation (pénalité de distance, divergence de Kullback–Leibler) | **Non** : « do not use any KL regularization ». La divergence n'apparaît que comme remède possible, non essayé. | p. 5 ; pp. 28, 29 |
| Terme de cohérence | **Non dans la récompense.** La cohérence est *mesurée après coup* (écart type de la confiance pour une même réponse ; somme des confiances par réponse distincte, Éq. 11) et présentée comme effet observé. | p. 3 ; pp. 8–9 (Fig. 4) ; p. 27 (Fig. 10) |
| Récompense de format | Oui, mais ne dépend que de la présence et de l'ordre des balises. | p. 18 |
| Entraînement en plusieurs étapes | Oui dans des variantes, sans couplage : (i) réglage supervisé préalable en mathématiques, dont les cibles ne contiennent **aucune confiance** (« we do not ask Deepseek-R1 to output confidence scores »), puis RLCR ; (ii) bases de comparaison initialisées depuis RLVR, récompense de Brier seule sur analyse + confiance, la réflexion et la réponse masquées : l'étape précédente ne produisait pas de confiance ; (iii) classifieurs et sonde entraînés après coup sur des étiquettes de justesse. Aucune n'ajoute à la récompense un terme relatif à une confiance antérieure. | pp. 6, 18, 21 ; p. 28 ; pp. 5, 19 |
| Agrégation à l'inférence | Moyenne de K confiances (analyses échantillonnées) et vote pondéré par la confiance : après l'entraînement, sans signal d'apprentissage. | p. 8 |
| Avantage de groupe de l'optimiseur | Le papier dit : 32 réponses par invite, division par l'écart type retirée ; le calcul de l'avantage n'est pas détaillé. Cela concerne l'optimiseur, pas la fonction R(c, q). | p. 18 |

**Précisions.**
- Le couplage vient de la *fusion* que Gemini a opérée : il écrit avoir modélisé la recette « en couplant deux briques », l'objectif de calibration de Damani et une pénalité de régularisation ou de consensus collectif (sections 1 et 4 de sa réponse), et déclare n'avoir pas eu accès au document de Damani (section 8 : « cité depuis l'invite de contexte sans accès au document »).
- Si une récompense de type RLCR recevait un terme vers une référence (pénalité quadratique, consensus de groupe, sonde pré-acte), le théorème de Gemini s'appliquerait : sa dérivée annoncée en q = μ_T est exacte pour le cas quadratique (vérifié par le lecteur sur trois jeux de paramètres, dont celui du contre-exemple de Gemini, valeur 0,65 ; calcul hors dépôt), et vaut 0 quand λ_sync = 0. Je n'ai pas relu le reste de sa preuve ni de son contre-exemple (constat de conv-audit : `LISEZMOI-v1.md`) ; ce n'est pas l'objet de cette lecture. Ce constat ne vaut que pour Damani et collègues (Avalon-M1 n'a pas été lu ici).
- Homonymie : « RLCR » = *Calibration Rewards* chez Damani (p. 1, vérifié) ; *Collective Rewards* chez Avalon-M1 et fusion opérée par Gemini, d'après `provenance-rlcr-v2.md` (Avalon-M1 non relu ici).

---

## 3. Pour le programme (niveau méthode)

### (a) Confiance verbalisée calibrée comme signal pour la pince

**Utilisable ?** Comme trait supplémentaire lisible dans le texte de la mâchoire boîte noire : oui, sous conditions. Comme garantie : non.

Pouvoir de discrimination (AUROC, Table 1, p. 7) de signaux différents prédisant la *justesse* des mêmes réponses :

| Signal | HotpotQA | HD (6 jeux) | Mathématiques | HD (5 jeux) |
|---|---|---|---|---|
| confiance verbalisée, modèle de base | 0,54 | 0,54 | 0,56 | 0,53 |
| confiance verbalisée, RLVR | 0,50 | 0,50 | 0,47 | 0,52 |
| probabilité des jetons de la réponse | 0,72 | 0,60 | 0,52 | 0,52 |
| sonde linéaire, dernière couche (RLVR) | 0,55 | 0,53 | 0,65 | 0,53 |
| classifieur de texte entraîné (BCE) | 0,66 | 0,58 | 0,78 | 0,55 |
| confiance verbalisée, RLCR | 0,69 | 0,68 | 0,67 | 0,60 |
| confiance verbalisée, RLCR + réglage préalable | — | — | 0,78 | 0,66 |

- La confiance de RLCR est la meilleure hors domaine, mais reste modeste (0,60–0,68) ; elle est inférieure au classifieur de texte en mathématiques en domaine (0,67 contre 0,78).
- Sans entraînement de calibration, la confiance verbalisée de ces modèles (7 milliards, base ou RLVR) ne porte presque aucune information : AUROC 0,47–0,56 (p. 7 ; confiance de RLVR obtenue par une phrase ajoutée à la sortie, p. 19) ; « 0,50 ± 0,00 » dans plusieurs jeux (pp. 31–32) signale une confiance quasi constante. Un moniteur qui lirait la confiance d'un agent *non* entraîné ainsi ne peut pas s'appuyer sur ce papier.
- Ce que le papier ne donne pas : rappel à faible taux de fausses alertes (il ne rapporte que l'AUROC) ; cible autre que la justesse de réponses vérifiables (sabotage, intention, omission, menace diffuse) ; tâches agentiques ; sondes à agrégation max ou attention sur plusieurs couches. La seule sonde du papier est linéaire sur la dernière couche, entraînée sur des étiquettes de justesse, position du jeton non précisée ; son AUROC hors domaine (0,53) ne dit rien des sondes du programme (non couvert par ce papier).
- Réutilisation possible ? Le modèle principal du papier (Qwen2.5-7B) figure parmi les modèles du programme (section 14) ; modèles et code RLCR sont annoncés p. 1, disponibilité non vérifiée.

**Fidélité : lien entre la confiance déclarée et le raisonnement.**
- Le papier pose la question (p. 2, question 2 ; p. 25) et cite Chen et al. 2025 sur les chaînes de raisonnement non fidèles ; il ne la tranche pas.
- Indices d'usage : sans l'analyse, la calibration se dégrade (Table 2, p. 10, réserve §1.9) ; pour une même solution et une même réponse, la confiance varie peu d'une analyse à l'autre (écart type : mode ≈ 0,05–0,07, la plupart sous 0,15, Figs. 4a et 10, pp. 9, 27, lecture visuelle), davantage d'un raisonnement à l'autre (Fig. 10) ; un petit classifieur gagne à lire l'analyse (Fig. 7, p. 25).
- Indices contre une lecture naïve : analyses « génériques » en mathématiques sans réglage préalable (p. 18) ; incohérence raisonnement–réponse observée sur SFT+RLCR (p. 29) ; un classifieur de 7 milliards n'a pas besoin de l'analyse (p. 25).
- Non couvert par ce papier : intervention sur l'analyse pour voir bouger la confiance ; comparaison de la confiance déclarée à une lecture des activations du même modèle (l'hypothèse « représentations partagées », p. 6, n'est pas testée).

**Risque d'une confiance qui trompe le moniteur.** Le papier n'en dit **rien** : le mot « moniteur » n'y apparaît pas, aucun adversaire, aucune pression sur la confiance, aucun modèle dont l'objectif diffère de la récompense. Les plus proches :
- détournement de la récompense de calibration par des réponses dégénérées avec confiance 0 (p. 11 pour d'autres travaux ; pp. 22–24 ; p. 28) : un détournement de la *récompense*, pas d'un moniteur ;
- calibration « trompeuse » par confiance constante, qui coïncide avec la justesse d'un jeu facile (CommonsenseQA, p. 31) : un artefact de *mesure*.
Lecture du lecteur (déduction, non du papier) : le théorème 1 caractérise l'optimum d'une récompense évaluée contre une vérité externe ; il ne dit rien d'un modèle dont l'objectif effectif diffère (saboteur) ni d'un modèle qui sait que sa confiance alimente un seuil d'audit. Le papier emploie la confiance en aval (vote pondéré, p. 8) sans rétroaction vers l'entraînement. La calibration hors domaine restant élevée (ECE 0,21–0,25 en moyenne ; 0,34 sur SimpleQA ; pp. 7, 31), une recalibration sur les épisodes honnêtes du même agent s'impose avant tout usage dans un moniteur (même logique, pas le même objet, que la consigne « calibrer sur les épisodes honnêtes du même agent » de `docs/decisions/proposition-N-013-revendications-niveau2-v1.md`, l. 58–61).

### (b) Juges de l'organisme d'idéation

**Oui pour la mesure, sans entraînement** (tout est calculable sur des paires confiance déclarée / issue binaire) :
1. Score de Brier, erreur de calibration attendue (10 classes) et AUROC (p. 5) ; les trois ensemble, car une confiance quasi constante peut avoir une calibration flatteuse et une AUROC de 0,50 (cas de RLVR sur CommonsenseQA, p. 31 ; Brier 0,09 et ECE 0,09 pour RLVR contre 0,17 et 0,30 pour RLCR, Table 9, p. 31).
2. Diagrammes de fiabilité avec histogrammes de répartition des confiances, pour voir l'agglutination (Figs. 8–9, pp. 26–27).
3. Intervalles de confiance par bootstrap (pp. 31–33) ; à n = 1 000 (HotpotQA, Table 11, p. 32) les demi-largeurs sont ≈ ±0,01 à ±0,03 sur le Brier et ≈ ±0,04 sur l'AUROC ; ils manquent pour l'ECE, à calculer aussi.
4. Cohérence d'un juge : écart type de la confiance sur K tirages pour une même sortie (N = 16, p. 27) ; somme des confiances moyennes par réponse distincte ≤ 1 pour des réponses exclusives (Éq. 11, p. 9).
5. Extraction sans entraînement d'une confiance chez un modèle qui n'en donne pas : phrase ajoutée « Thinking time ended. My verbalized confidence in my answer as a number between 0 and 100 is equal to » (p. 19) ; évaluation à température 0.
6. Agrégation : vote pondéré par la confiance et moyenne de K confiances (p. 8) : utilisables sans entraînement, mais évalués **sur des tirages d'un seul modèle entraîné par RLCR** ; panel de trois juges hétérogènes non entraînés : non couvert par ce papier (et, pour des modèles de base ou RLVR, la confiance verbalisée n'a presque pas d'information, p. 7).

**Conditions et limites.** Il faut une vérité terrain *binaire* par fiche (le papier travaille sur justesse de réponses vérifiables) ; notes ordinales ou vérité différée : non couvert par ce papier. La taille d'échantillon compte (ci-dessus). Pour des juges qui rendent un score par lecture de jetons, la comparaison du papier (« probabilité de la réponse », bonne discrimination mais mauvaise calibration, p. 7) invite à mesurer séparément discrimination et calibration ; le moniteur boîte noire par action du programme (T0.8) lit d'ailleurs un score par espérance sur les jetons plutôt qu'un nombre généré (`docs/decisions/proposition-P-010-T0.8-moniteur-par-action-v1.md`, l. 12–13 ; statut d'adoption non vérifié) : ce mode de lecture n'est pas évalué par ce papier. Le papier ne fournit aucune méthode de *recalibration* sans entraînement ; ses recalibrations (classifieurs, sonde) sont entraînées.

### (c) Antériorité

- Dans `docs/programme-controle-ia-v2.md`, « calibr- » apparaît aux l. 90 (probabilités d'originalité), 98 (« non calibré », transposition Tr) et 183 (calibration dose-réponse du budget de sabotage) : aucune ne vise la calibration d'une confiance verbalisée. « Confiance » y désigne un *moniteur de confiance* (évaluateur faible, l. 122, 154–158, 249), la *paraphrase de confiance* (HC5, l. 107, 198) ou un intervalle de confiance (l. 22). Les « calibrages » des décisions (N-003, N-007, N-013, P-010) sont des calibrages de seuil à taux de fausses alertes fixé, autre objet.
- Aucune hypothèse du programme (H1, H2, L, T, H6, Tr, H8 ; HC1 à HC6 ; H3, H4′, H5, H7), ni H9 (`docs/decisions/decision-N-035-v1.md`), n'énonce quelque chose que ce papier établisse ou occupe, tel que je les ai lues. **Pas d'antériorité tirée de ce papier** ; cela ne dit rien d'autres travaux (aucune recherche affirmative faite, R8).
- Voisinage méthodologique seulement : mesure de calibration des juges et des moniteurs (pertinence notée en R-1003, `registres/decisions.md`) ; HC1 (loi de déférence sur un verdict v ∈ [0, 1]) : ce papier ne traite aucune pression sur une confiance ou un verdict (non couvert par ce papier).

---

## 4. Ce qu'il faudrait lire ensuite

Références telles que listées par le papier (pp. 11–15), non vérifiées à la source (R7), classées par utilité pour le programme.

1. **Chen et al. 2025, « Reasoning models don't always say what they think »** (arXiv 2505.05410 ; cité p. 25 ; référence p. 12) : fidélité de la chaîne de raisonnement, ce que le papier soulève sans trancher.
2. **Yoon et al. 2025, « Reasoning models better express their confidence »** (arXiv 2505.14489 ; cité pp. 6, 10 ; réf. p. 15) et **Mei et al. 2025, « Reasoning about uncertainty: Do reasoning models know when they don't know? »** (arXiv 2506.18183 ; cité p. 10 ; réf. p. 13) : effet du raisonnement sur la calibration ; le papier cite Mei et al. à la fois pour une surconfiance accrue avec un raisonnement plus profond et, avec Yoon et al., pour une meilleure calibration par introspection (p. 10) : à lire à la source.
3. **Stengel-Eskin, Hase, Bansal 2024, LACIE** (cité p. 11 ; réf. p. 14) : cadre locuteur–auditeur où la récompense du locuteur dépend de la confiance que *l'auditeur* infère de sa réponse ; le plus proche d'un lecteur externe (mâchoire noire) de la confiance déclarée.
4. **Stangel et al. 2025, « Rewarding doubt »** (arXiv 2503.02623) et **Xu et al. 2024, SaySelf** (EMNLP 2024) (cités p. 11 comme les plus proches ; réf. p. 14) ; **Turtel et al. 2025** (arXiv 2505.17989 ; réf. p. 14 ; source de la modification de l'avantage, p. 18).
5. **Orgad et al. 2025, « LLMs know more than they show »** (ICLR 2025 ; cité p. 11 ; réf. p. 13), **Azaria & Mitchell 2023** (cité p. 11 ; réf. p. 11) et **Kadavath et al. 2022** (réf. p. 13) : lecture de la véracité dans les représentations internes, côté boîte blanche de la pince.
6. **Xiong et al. 2024** (ICLR 2024 ; cité p. 10 ; réf. p. 14), **Tian et al. 2023** (EMNLP 2023 ; cité p. 10 ; réf. p. 14) et **Taubenfeld et al. 2025, « Confidence improves self-consistency in LLMs »** (arXiv 2502.06233 ; cité p. 8 ; réf. p. 14) : extraction de confiances verbalisées et pondération des votes, utiles pour un panel de juges.
7. **Gneiting & Raftery 2007** (cité p. 16 ; réf. p. 12) : pour vérifier les conditions de régularité de la représentation de Savage–Dawid utilisée dans la preuve (§1.3).
8. **Kirichenko et al. 2025, AbstentionBench** (cité p. 2 ; réf. p. 13) et **Mohamadi et al. 2025** (arXiv 2511.11500 ; réf. p. 13) : abstention, autre voie de la calibration.

---

## 5. Ce qui n'a pas été fait ou reste non vérifié

- Aucune référence n'a été ouverte (pas de réseau) ; identifiants et affirmations sur la littérature (p. 10 notamment : surconfiance accrue avec un raisonnement plus profond, attribuée à Mei et al.) sont rapportés tels que le papier les écrit.
- Site du projet, code et modèles : non consultés.
- Gneiting & Raftery (2007) non lu ; représentation de Savage–Dawid prise telle que citée.
- Valeurs lues sur figures (Figs. 3, 4, 7, 10) : approximatives.
- Le script et la preuve de Gemini n'ont pas été relus au-delà de la dérivée en q = μ_T (cas quadratique) ; l'organisme d'idéation et ses juges ne sont décrits que par la consigne reçue.
- Avalon-M1 non lu (hors périmètre ; un autre lecteur écrit sa propre fiche dans ce dossier).
- Scripts du lecteur (hors dépôt) : `/tmp/lecteur-rlcr-scripts/verif_lemmes.py`, `verif_gemini_derivee.py` ; texte extrait : `/tmp/lecteur-rlcr-txt/`. Non versés.
