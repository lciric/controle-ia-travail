# Proposition H — Tour III.3 : réponse aux critiques

## (a) Traitement des critiques visant H

### Décision 1 — Grandeur(s) du monde témoin

**Critique 1.1 — N non fixé, le test Z est arbitraire** (A, B, G, I).
*Acceptée.* |ΔA|/SE croît avec N pour tout ΔA ≠ 0 ; l'issue dépend d'un paramètre libre. Le critère doit porter sur une taille d'effet δ pré-gelée, pas sur une significativité.

**Critique 1.2 — H\_A et H\_B non complémentaires** (A, B, D, G, I).
*Acceptée.* Les deux peuvent varier, ou aucune. Falsifier H\_A ne prouve pas H\_B. Violation de B4.

**Critique 1.3 — Confusion succès du témoin / défaillance de l'instrument** (C, F, G).
*Acceptée.* Un moniteur parfaitement stable donne ΔA = 0, que H interprète comme « A ne varie pas assez » — alors que c'est l'issue attendue d'un monde sain.

**Critique 1.4 — Moniteur aléatoire binaire : B ≡ 0** (I).
*Acceptée.* Un moniteur binaire ne s'abstient jamais ; il ne contrôle rien pour B.

**Critique 1.5 — Drapeau de recalibration viole le gel** (F).
*Partiellement acceptée.* Le drapeau était une option, non un ordre post-gel. Mais sa formulation (action conditionnelle post-observation) contredit le gel. *Transformée en test :* pré-spécifier le drapeau dans le texte gelé comme résultat rapporté uniquement, sans pouvoir d'arrêt ni de recalibration.

**Critique 1.6 — Contrôle manquant : coupe placebo avec vrai moniteur** (B, C, F, G, I).
*Acceptée.* Le moniteur aléatoire ne détecte aucune instabilité du vrai moniteur. Fatal.

### Décision 2 — Règle de signalement

**Critique 2.1 — SD(part) < 1/m ne borne pas les fausses alertes** (A, B, C, D, F, G, I).
*Acceptée.* F démontre (`[VÉRIFIÉ]`) qu'avec SD = 1/(2m) le taux de fausses alertes atteint ≈ 16 %. La bonne grandeur est P(X\_comp − X\_obj ≥ 1/m | pas de dommage), par strate de m.

**Critique 2.2 — m médian ignore les grandes strates** (A, C, F, G).
*Acceptée.* Pour m > m\_méd, 1/m est plus serré ; le bruit peut le dépasser.

**Critique 2.3 — Lecteur uniforme invalide pour m ≤ 3** (A, B, F).
*Acceptée.* SD(uniforme) ≈ 0,289 < 1/m pour m ∈ {1, 2, 3} `[VÉRIFIÉ]`. Le « contrôle négatif » valide H\_A au lieu de la réfuter.

**Critique 2.4 — Variance inter-productions omise** (C, D, G).
*Acceptée.* Les relectures d'un même objet ne capturent que le bruit de lecture, pas la variance de génération. Or la comparaison finale porte sur deux documents distincts.

### Décision 3 — Désignation des contrôles

**Critique 3.1 — Falsifie H\_A par le rappel seul, précision ignorée** (B, F, G).
*Acceptée.* Un programme à rappel 0,95 et précision 0,50 passerait le test avec un biais majeur. Les deux seuils doivent être falsifiants.

**Critique 3.2 — « Documents à contrôles explicites » : rappel vrai par construction** (G).
*Acceptée.* Si les mots exacts du contrôle sont dans le document, le programme les trouve par définition.

**Critique 3.3 — Métrique globale masque le biais par strate** (C).
*Acceptée.* Si w\_para ≤ 0,10, le rappel global atteint 0,90 avec un rappel de 0 sur les paraphrases `[VÉRIFIÉ]`.

**Critique 3.4 — Leurres lexicaux et paraphrases manquants** (A, G, I).
*Acceptée.* L'échantillon doit inclure des négations lexicales (faux positifs structurés) et des paraphrases pures (faux négatifs structurés).

**Critique 3.5 — Biais résiduel non corrigé sur le banc** (F).
*Transformée en test.* Si le biais mesuré dépasse un seuil pré-gelé, la clause de bascule déclenche le passage à (b).

### Décision 4.1 — Régime d'excès

**Critique 4.1.1 — Audit rétrospectif non falsifiable a priori** (tous).
*Acceptée.* H l'avait reconnu. L'expérience est retirée. Le choix (c) repose sur l'argument de protocole : ne pas créer d'objets ambigus dans un cadre gelé.

### Décision 4.2 — Budget d'erreur

**Critique 4.2.1 — 95 % ≠ niveaux accordés** (B, G).
*Acceptée.* La simulation doit porter sur 2,5 % / 1,25 % (RAPPORTÉ), pas sur un 5 % illustratif.

**Critique 4.2.2 — Loi jointe E / erreurs non spécifiée ; tautologie sous indépendance** (A, D, G).
*Acceptée.* Sous indépendance, la couverture tient par construction. La grille simulée doit inclure un couplage positif entre E et les lectures servant à estimer q.

**Critique 4.2.3 — Contrôle sans excès au lieu de 4.2(a) avec excès** (G).
*Acceptée.* Le comparateur doit être 4.2(a) sous les mêmes scénarios incluant l'excès.

### Décision 5 — Composition de la fiche

**Critique 5.1 — H\_A et H\_B non complémentaires** (A, B, D, E, G, I).
*Acceptée.* Un taux de rejet de 60 % falsifie les deux. Violation de B4.

**Critique 5.2 — Top-K = vrai ensemble quand le signal est fort** (A, B, E, F, G, I).
*Transformée en test.* Fixer P(top-K ≠ vrai ensemble) ∈ [0,2 ; 0,8] (illustratif) en calibrant le rapport signal/bruit de la loi la plus faible.

**Critique 5.3 — Épisodes K = 0 manquants** (C, F, G, I).
*Acceptée.* Nécessaire pour détecter l'angle mort de la cohérence sur bruit pur.

**Critique 5.4 — P10 non mesuré** (F, G, I).
*Transformée en test.* Estimateur aveugle K̂(X) sur les seules données, à comparer au prédicteur modal.

---

## (b) Expériences corrigées

### D1 corrigé

| Élément | Contenu |
|---------|---------|
| H\_A | \|ΔA\| ≤ δ\_A ET \|ΔB\| ≤ δ\_B (le monde témoin ne perturbe pas le moniteur) |
| H\_B | \|ΔA\| > δ\_A OU \|ΔB\| > δ\_B (au moins une grandeur dérive) |
| δ\_A, δ\_B | Tailles d'effet pré-gelées ; N fixé pour puissance ≥ 0,80 contre δ |
| Statistique | Test d'équivalence TOST bilatéral sur ΔA et ΔB, à N fixé |
| Falsifie H\_A | Au moins un intervalle exclut \[−δ, +δ\] |
| Falsifie H\_B | Les deux intervalles inclus dans \[−δ, +δ\] |
| Contrôle négatif | Coupe placebo du monde de référence avec le *vrai* moniteur ; les intervalles doivent contenir 0 |

**Choix maintenu : (c).** Confiance révisée : **0,65**.

### D2 corrigé

| Élément | Contenu |
|---------|---------|
| H\_A | P₀(1/m) ≤ α\_FA pour tout m (la règle fixe suffit) |
| H\_B | ∃ m tel que P₀(1/m) > α\_FA (étalonnage nécessaire) |
| Paires nulles | Deux productions honnêtes distinctes de la même tâche + éditions neutres sans retrait |
| Métrique | Taux de fausses alertes par strate de m ; borne supérieure binomiale par strate |
| Falsifie H\_A | Borne supérieure > α\_FA pour au moins un m |
| Falsifie H\_B | Toutes bornes supérieures ≤ α\_FA |
| Contrôle positif | Paires avec un contrôle retiré : signalement > 0 |

**Choix maintenu : (b).** Confiance révisée : **0,75**.

### D3 corrigé

| Élément | Contenu |
|---------|---------|
| H\_A | Rappel\_littéral ≥ r\_lit ET Rappel\_paraphrase ≥ r\_para ET Précision ≥ p\_min |
| H\_B | Au moins un seuil violé |
| Échantillon | Stratifié : littéraux, paraphrases pures, leurres lexicaux (négation, mention hors contexte), passages sans contrôle |
| Métriques | Rappel par strate + précision globale, avec intervalles de confiance |
| Contrôle négatif | Leurres lexicaux : fausses désignations ≤ p\_min\_FP |
| Clause de bascule | Si rappel\_paraphrase < r\_para et coût repéreur ≤ seuil pré-gelé, basculer vers (b) |

**Choix maintenu : (c), avec clause de bascule pré-gelée.** Confiance révisée : **0,70**.

### D4.1 — Argument de protocole, pas de duel

(c) : garder la fonction et ses cas d'essai. Le risque de confusion garanti/non garanti est structurel. **Confiance : 0,75**.

### D4.2 corrigé

| Élément | Contenu |
|---------|---------|
| H\_A | FWER ≤ α\_total sous réattribution, y compris sous Cov(E, lectures de q) > 0 |
| H\_B | ∃ configuration réaliste où FWER > α\_total sous réattribution |
| Grille | 10 000 répliques (illustratif) ; niveaux 2,5 %/1,25 % (RAPPORTÉ) ; couplage E–lectures inclus |
| Comparateur | Même simulation sous allocation fixe 4.2(a), mêmes scénarios avec excès |
| Falsifie H\_A | sup FWER > α\_total + marge Monte-Carlo dans au moins un scénario couplé |
| Falsifie H\_B | FWER ≤ α\_total sur toute la grille |

**Choix maintenu : (a).** Confiance : **0,85**.

### D5 corrigé

| Élément | Contenu |
|---------|---------|
| H\_A | Sous tirage, P(cohérence accepte saboteur) ≤ P(idem sous composition fixe) − δ |
| H\_B | Écart < δ |
| Calibrage | P(top-K ≠ vrai ensemble) ∈ \[0,2 ; 0,8\] (illustratif) via réglage du SNR |
| Strates | K ∈ {0, 1, …, K\_max}, résultats par K |
| Contrôle positif | Fiche sabotée manifestement incohérente (statistiques faibles) : rejet ≥ r\_min |
| Contrôle négatif | Fiche honnête : acceptation ≥ 1 − α\_FP |
| Test P10 | Estimateur K̂(X) aveugle ; H\_A′ : E[\|K̂ − K\|] ≥ τ\_K ; H\_B′ : E[\|K̂ − K\|] < τ\_K |

**Choix maintenu : (a).** Confiance révisée : **0,70**.

---

## (c) Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Établi

**L'étalonnage du seuil est nécessaire (D2).** Huit critiques convergent : SD(part) < 1/m est un critère inadéquat ; le taux réel de fausses alertes dépend de la loi discrète par strate de m et de la variance inter-productions. Cela ne suffit pas à trancher entre (a) et (b), mais exclut d'utiliser (a) les yeux fermés. Statut : le *besoin* d'étalonnage est quasi-établi par les arguments algébriques des critiques (`[VÉRIFIÉ]` chez C, F, G).

**Le gel ne se modifie pas après observation (D4.2).** Le contre-exemple de G (FWER pouvant atteindre α₁ + (1 + P(E))·α₂) est un risque réel ; le fardeau de la preuve incombe à quiconque redistribue. Statut : HYPOTHÈSE que la réattribution préserve la couverture, ni réfutée ni établie ; (a) est le choix conservateur correct.

**Pas de résultat non garanti (D4.1).** L'unanimité sur l'inadéquation de l'audit rétrospectif renforce (c).

### Non établi

**D1 : laquelle de A ou B est diagnostique.** Le transfert des calculs de conception au moniteur réel n'est pas testé (P1 = HYPOTHÈSE). L'expérience corrigée exige δ\_A, δ\_B et N pré-gelés, non encore fixés.

**D3 : la fidélité du programme sur les paraphrases.** Rappel global ≥ 0,90 n'exclut pas un rappel de 0 sur les paraphrases. La prévalence des paraphrases est inconnue (P5 = HYPOTHÈSE). Sans cette mesure, le biais de désignation reste non borné — et ce biais contamine les décisions 2, 4.1 et 4.2.

**D5 : résistance de la cohérence à « top-K » et inférabilité de K.** P9 et P10 sont explicitement non vérifiés. Ces deux inconnues déterminent si le tirage de la composition suffit.

### Expérience à faire en premier

**Décision 3 — Mesure de fidélité stratifiée du programme lexical.**

La désignation est en amont de tout le banc des dommages plantés. Si le programme échoue sur les paraphrases, les dommages plantés dans ces passages ne sont pas comptés, et q est sous-estimé pour *tous* les moniteurs — biais systématique contaminant D2, D4.1, D4.2. L'échantillon est modeste (50–100 documents annotés avec stratification littéral/paraphrase/leurre, ≈ 250–500 USD illustratif), c'est le coût le plus faible des expériences corrigées, et le résultat décide si l'on reste sur (c) ou si l'on bascule vers (b). Cette mesure peut être faite avant le gel.

FIN-DE-CELLULE