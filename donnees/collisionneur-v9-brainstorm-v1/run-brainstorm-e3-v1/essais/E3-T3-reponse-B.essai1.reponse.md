# Proposition B · Tour III.3 : réponse aux critiques

**Statuts.**
- **[VÉRIFIÉ]** : ce que la fiche des faits déclare elle-même.
- **[RAPPORTÉ]** : ce qu'affirme un README ou un préenregistrement.
- **[OBSERVÉ-NON-AUDITÉ]** : ce que j'ai lu ou calculé à la main dans un fichier fourni, sans audit.
- **[HYPOTHÈSE]** : mes conjectures.

Tout coût, toute marge et tout seuil que je propose est **illustratif** tant qu'un préenregistrement ne l'a pas fixé.

**Pièces.**
- Ma conception III.1 et les quatre critiques croisées (A, C, D, E) sont présentes et entières.
- Restent absents : les pages des mentors, `code/*.py`, les entrées `R*_input_*.json`, `R6_descriptive_counts.json` et les 1 176 générations hors échantillon [VÉRIFIÉ].

---

## (a) Les critiques, une par une

### Objections transversales

| # | Critique (auteurs) | Décision | Raison et suite |
|---|---|---|---|
| T1 | Sélection sur la sortie : masquer des réponses pressées selon leur contenu change la population comparée (A, C, D, E ; R-1, R-2) | **Acceptée** | Le masquage modifie K_i, donc la fiabilité λ ; il fabrique de l'attraction sous le nul. Je le remplace par une **imputation à K constant** (B-1). La phase textuelle de R-2 est abandonnée. |
| T2 | Fuite entre échantillon et instrument : les motifs ont été construits après lecture des 24 réponses, qui appartiennent au jeu évalué (A, C) | **Acceptée** | J'abandonne comme instruments mes motifs « mise à distance », « agree with you » et le dictionnaire d'axe. Je ne garde que le motif de refus fixé par l'auteur dans R6 [RAPPORTÉ], antérieur à ma lecture. Les items 0, 5, 10, 15, 20 et 25 sont exclus de toute analyse confirmatoire et rapportés à part. |
| T3 | Dérive du juge : `claude-opus-4-6` est un alias non figé [RAPPORTÉ] (A) | **Acceptée** | Toute relecture relit les originaux dans le même lot que les versions modifiées, en ordre aléatoire. Aucune comparaison à des notes stockées. |
| T4 | Un IC qui contient 0 ne réfute rien (D, E, A) | **Acceptée** | Chaque expérience reçoit une marge d'équivalence. Un intervalle qui chevauche la marge donne « non concluant », qui n'est pas une hypothèse. |
| T5 | ĉ = ordonnée / g est un estimateur de rapport (A, C, D) | **Acceptée** | ĉ n'est jugé que si la borne inférieure de g dépasse 0. Sinon, « non jugeable ». |
| T6 | Toute réduction de K_i abaisse λ et crée une attraction sous le nul (A) | **Acceptée, transformée en test** | B-1 garde K = 10. B-3 est calibré sur simulations avant les données. |

### Objections propres à chaque idée

| Idée | Critique (auteurs) | Décision | Raison et suite |
|---|---|---|---|
| R-1 | 6/6 ouvertures marquées : le sous-ensemble restant serait vide ou extrême (A, C) | Acceptée | Le motif « mise à distance » ne varie pas, donc il n'identifie rien. B-1 ne traite que les refus (85/1 200 dans c2 [RAPPORTÉ, R4]). |
| R-1 | Appliquer le même filtre au neutre et à la critique ; contrôle de retrait apparié en note (C) | Acceptée | Ce sont les contrôles (i) à (iii) de B-1. |
| R-1 | Duel asymétrique : « l'IC de g contient 0 » arrive aussi par simple perte de puissance (A) | Acceptée | Remplacé par une marge ε_g. |
| R-2 | Intensité non appariée ; « written » figure dans les deux suffixes ; une seule paraphrase (A, D, E) | Acceptée | Devient B-6, plan factoriel axe × valence avec deux paraphrases par case et un prétest d'intensité. |
| R-3 | La troisième issue brise B4 (A) | Acceptée | Retirée. |
| R-3 | Familles de lois non spécifiées (C, E) | Acceptée | Spécifiées dans B-3. |
| R-3 | Saturation d'une multinomiale par item (C) | **Rejetée après spécification** | Dans B-3, la loi pressée partage ses paramètres entre items (5 contre 3 au total par bras). Rien n'est ajusté item par item. |
| R-3 | Bimodalité héritée du neutre (C) | **Rejetée comme objection, gardée comme contrôle** | P0_i empirique entre à l'identique dans les deux modèles, donc la bimodalité neutre ne favorise aucun des deux. Le contrôle neutre/neutre est ajouté. |
| R-3 | Puissance portée par les seuls items loin de ĉ (A, C, D, E) | Acceptée | Porte de jugeabilité préenregistrée, plus une récupération de paramètres sur données simulées. |
| R-4 | La correction d'erreurs de mesure est tranchée d'avance (C) | **Acceptée, avec correction de la source** | C tire λ ≈ 0,95 de la corrélation campagne 2 / campagne 1 [RAPPORTÉ], qui ne porte pas sur la paire c2a / c2b. Mon calcul à la main sur les 30 moyennes neutres de `c2a_results.json` et `c2b_results.json` donne r ≈ 0,94 [OBSERVÉ-NON-AUDITÉ]. Sous un modèle d'erreur classique, ĝ passerait d'environ 0,72 à environ 0,70 (illustratif). L'issue H_B était donc inatteignable. **Volet retiré.** |
| R-4 | Juge commun aux deux campagnes : violation d'exclusion (C) | **Rejetée** | Un biais du juge propre à l'item fait partie du p₀ lu par ce juge (μ_i), pas de l'erreur u. La question devient de toute façon sans objet. |
| R-4 | Graines réutilisées entre items [RAPPORTÉ] (A) | Acceptée | Déclarée dans B-4, où les deux jeux neutres servent à la sélection. |
| R-4 | Écrêtage à définir au niveau des tirages, δ ajusté hors item (E, A) | Acceptée | B-4. |
| R-5 | Canal, quantification, prompt et pile changent ensemble (C, A, D) | Acceptée | B-2 fixe la pile en float32 sous TransformerLens et ajoute Llama comme ancre. |
| R-5 | « K = 1, donc pas de dilution » est faux (A, D, E) | **Acceptée en partie** | K = 1 supprime l'erreur d'échantillonnage du sujet, pas l'erreur de construit (dépendance à la formulation). Le nul de permutation n'est plus disponible. Je retire ma formule. |
| R-5, R-9 | Comparer deux étiquettes de régime n'est pas un contraste (D, E) | Acceptée | Contraste direct g_chiffre − g_texte, avec marge. |
| R-6 | La phrase d'écho est souvent la phrase de verdict (A ; par exemple c2a, item 25 [OBSERVÉ-NON-AUDITÉ]) | Acceptée | B-5 retire l'**attribution** et garde le verdict, au lieu de supprimer la phrase. |
| R-6, R-8 | La fenêtre centrale n'est pas un contrôle neutre (D, E) | Acceptée | Remplacée par une édition placebo appariée et une covariable de position du verdict. |
| R-7 | R² non homogènes, issues non exclusives, aucune vérité terrain (A, D, E) | Acceptée | **R-7 retirée.** |
| R-8 | Sans interaction troncature × ablation, rien ne se dit sur l'ancien programme (D) | Acceptée | La prétention historique est retirée. R-8 devient un bras de mesure dans B-5. |
| R-9 | Le rôle est confondu avec la tâche, les stimuli, le canal et le lecteur (A, C, E) | Acceptée | **R-9 retirée.** Il reste une proposition d'addendum à R7 avant toute lecture : une note placebo sans verdict, de même longueur. |
| R-10 | p₀ bouge et sa plage se contracte (A) ; disjonction des corpus non établie (D, E) ; titre contraire à H_A (E) ; un seul sous-espace aléatoire (A, E) ; une intervention trop forte doit donner « non jugeable », pas H_B (E) | Acceptées | Devient B-7, conditionnel et en dernière priorité. |

---

## (b) Expériences corrigées

Chaque duel oppose H_A et H_B, exclusives. Un intervalle qui chevauche la marge donne « non concluant ». La marge par défaut sur un gain est **ε_g = 0,20** (illustratif). Elle est choisie au-dessus des médianes du nul de permutation, 0,14 et 0,10 [RAPPORTÉ].

### B-1 · Le bras « éloge » quand les refus valent « pas de changement » (0 $, priorité 1)

1. **Phrase.** « Llama-3.1-8B's attraction under praise does (not) survive when refusals are scored as no change. »
2. **Pourquoi.**
   - Les refus valent environ 3 pour le juge [RAPPORTÉ, R4 et R6], et ĉ_éloge = 2,94 [RAPPORTÉ].
   - c2 contient 85 réponses de type refus sur 1 200 [RAPPORTÉ].
   - La sensibilité de R4 retirait des items entiers, avec 9 refus seulement, et changeait l'ensemble d'items [RAPPORTÉ].
   - L'argument contre la « poussée directionnelle » repose sur la descente des items situés au-dessus de la cible : 10 sur 11, −0,67 [RAPPORTÉ]. Or un refus noté 3 fait mécaniquement descendre un item haut [HYPOTHÈSE].
3. **Procédure.**
   - Marquer les refus avec le motif de l'auteur, copié tel quel depuis `R6_descriptive_counts.json` (public selon la question, non fourni ici).
   - Deux notations à K = 10 constant :
     - S3 : statu quo ;
     - S0 : chaque note pressée d'un refus est remplacée par la note neutre de même graine k. C'est une note entière, donc compatible avec le code figé (compatibilité non vérifiée). La moyenne neutre de l'item sert d'analyse de sensibilité.
   - Analyse par `analyse_runs.py` figé, sans modification.
4. **Duel.**
   - **H_A** (les refus portent l'attraction sous éloge) : sous S0, la borne supérieure à 95 % de g_éloge est inférieure à ε_g.
   - **H_B** (attraction substantielle) : sous S0, la borne inférieure est supérieure à ε_g.
   - Un oui falsifie « destination de verdict sous éloge » et affaiblit la preuve par descente. Un non falsifie ma conjecture III.1 (« le bras éloge est un retrait »).
   - Rapporté à côté, sans critère : la descente des items au-dessus de ĉ sous S0.
5. **Préconditions déclarées.**
   - Précision du motif mesurée par une lecture humaine tierce, à l'aveugle, de toutes les réponses marquées et de 50 non marquées. En dessous de 0,8 (illustratif), l'expérience est « non jugeable ».
   - Corrélation entre le taux de refus par item et p₀ᵢ, rapportée **avant** tout calcul de g (condition transversale de A).
6. **Contrôles.**
   - (i) La même règle sur le bras critique, qui compte très peu de refus : |g_crit(S0) − g_crit(S3)| < 0,05 (illustratif). Sinon la règle fait autre chose qu'écarter des refus.
   - (ii) Imputation appariée en note (C) : par item, autant de réponses non-refus notées 3, tirées au hasard, imputées de la même façon (1 000 tirages). On obtient ainsi la distribution de g due au seul retrait de 3.
   - (iii) Le motif appliqué aux réponses neutres, comme taux de fausse alerte.
7. **Puissance (illustratif).** L'IC publié de g_éloge, [0,531 ; 0,819], a une demi-largeur d'environ 0,14 [RAPPORTÉ]. À largeur égale, le duel tranche dès que g_S0 sort de l'intervalle [0,06 ; 0,34].
8. **Vérification extérieure.** Quiconque dispose des fichiers publics et du fichier de motifs.

### B-2 · L'« offset » vient-il du canal ou de la famille ? (< 1 $, illustratif)

- **Plan.** Auto-notation au premier jeton (prompt R2, publié verbatim [RAPPORTÉ]) en float32 sous TransformerLens, la pile de R3 et R6.
  - Modèles : Llama, Qwen, Mistral, Gemma.
  - Items 0–39, trois conditions, plus un suffixe non évaluatif de même longueur.
  - Au total 640 passes avant (illustratif).
- **Point de comparaison.** g_texte vient de R3, qui porte sur les items 0–39 [RAPPORTÉ]. Pour Llama, il vient de la strate S0 de la campagne 2, avec 40 items [RAPPORTÉ].
- **Duel, par famille et par bras**, avec un bootstrap d'items commun :
  - **H_A** (canal) : g_chiffre − g_texte > ε_g, intervalle entier au-delà de la marge ;
  - **H_B** (trait de famille) : |g_chiffre − g_texte| < ε_g.
  - La marge doit dépasser l'inflation du gain par le nul côté texte, ce qui justifie 0,20 plutôt que 0,10.
- **Contrôles.**
  - Positif : Llama en float32 doit retrouver le g critique de R2 (0,63 [RAPPORTÉ]) à 0,1 près (illustratif).
  - Négatif : le suffixe non évaluatif doit donner |g| < ε_g.
- **Non jugeable si** la masse de chiffres est inférieure à 0,5, la règle de R7 [RAPPORTÉ], ou si la moitié des lectures sont saturées aux bornes.

### B-3 · Mélange ou rétrécissement, modèles spécifiés (0 $)

- **Modèles.** Dans les deux, P0_i est la loi empirique des notes neutres.
  - Mélange : P1_i = (1 − π)·P0_i + π·Q, où Q est une loi catégorielle partagée par tous les items. Cela fait 5 paramètres par bras.
  - Rétrécissement : P1_i est la loi de clip(round((1 − g)Y + g·c + e)), avec Y ~ P0_i et e ~ N(0, s²). Cela fait 3 paramètres.
- **Statistique.** Log-score en validation croisée item par item.
- **Duel.**
  - **H_A** : l'IC à 95 % de la différence de log-score, au profit du mélange, exclut 0 ;
  - **H_B** : il exclut 0 au profit du rétrécissement.
- **Portes de jugeabilité, figées avant les données.**
  1. Récupération sur données simulées sous chacun des deux modèles, aux paramètres ajustés : le test doit désigner le bon modèle dans au moins 80 % des cas (illustratif).
  2. Assez d'items loin de la cible : N_loin = #{i : |p₀ᵢ − ĉ| > 2√(σ²_w/K)} doit atteindre au moins 8 (illustratif).
  - Sinon, « non jugeable ».
- **Données.** c2a et c2b (fournis), R4 et R6 standard Llama (publics selon la question).
- **Contrôle.** Neutre de c2a contre neutre de c2b : les deux modèles doivent dégénérer, avec π ≈ 0 et g ≈ 0.
- **Indice déjà visible.** Item 1 sous critique : 0 note pressée sur 10 reste à 4 ou plus [OBSERVÉ-NON-AUDITÉ]. Item 25 : 2 sur 10 [OBSERVÉ-NON-AUDITÉ]. C'est anecdotique.

### B-4 · Attraction depuis le plancher contre décalage écrêté (0 $)

- **Contraste.** C'est la seule prédiction de signe opposé entre les deux modèles. Pour les items sous ĉ_crit, la loi prédit une montée sous critique. Un décalage écrêté au niveau des tirages, max(1, Y − δ), donne E[Y₁] ≤ E[Y₀] [HYPOTHÈSE, propriété du modèle].
- **Sélection indépendante de la mesure.**
  - Sélection des items dont la moyenne neutre est inférieure à 1,456 dans c2a **et** dans c2b.
  - Mesure de Δ dans R6 standard Llama, sur les mêmes items 0–29 avec d'autres graines [RAPPORTÉ].
  - Pour R4, sélection sur k = 0–1 et mesure sur k = 2–4.
  - La réutilisation des graines entre items [RAPPORTÉ] est déclarée.
- **Duel.**
  - **H_A** : l'IC de la moyenne de Δ exclut 0 par le haut et contient la prédiction de la loi sans réajustement ;
  - **H_B** : il exclut cette prédiction et contient 0, ou se situe sous 0.
- **Coup d'œil exploratoire, qui ne décide rien.**
  - Sélection sur c2b, mesure sur c2a : 6 items (0, 6, 7, 13, 16, 19), moyenne de Δ = +0,10 [OBSERVÉ-NON-AUDITÉ].
  - La loi aux constantes de la campagne 1 prédit environ +0,26 (illustratif).
  - Six items ne tranchent pas : c'est l'objection de puissance de A, et elle explique le regroupement avec R6 et R4.

### B-5 · Le juge lit-il l'attribution à l'utilisateur ? (≈ 3,4 $ avec Opus, ≈ 1 $ avec Qwen-72B, illustratif)

- **Édition mécanique.** La règle est figée et appliquée uniquement aux items hors échantillon. Elle retire l'attribution et garde le verdict : « I agree with you that the text is not well-written » devient « The text is not well-written ».
- **Contrôles.**
  - Placebo : une édition de même longueur, sans attribution.
  - Lecture humaine tierce, à l'aveugle, de 40 paires : le verdict doit être conservé.
- **Lecture.**
  - Originaux, éditions, placebos et neutres sont relus dans un seul lot, en ordre aléatoire (T3).
  - Bras de mesure ex-R-8 : un préfixe de 300 caractères des mêmes réponses, avec la position du premier mot de verdict en covariable. La prétention ne porte que sur la mesure.
- **Duel.**
  - **H_A** : |Δ_orig| − |Δ_édité| > ε_Δ = 0,15 (illustratif) ;
  - **H_B** : la différence est inférieure à ε_Δ.
- **Vérification extérieure.** Le prompt du juge n'est pas publié [RAPPORTÉ]. Un tiers ne peut répliquer qu'avec son propre prompt, et sur le signe seulement.

### B-6 · Axe × valence, génératif (≈ 4–7 $, illustratif)

- **Plan.** Suffixes « écriture » et « contenu », chacun en version négative et positive, deux paraphrases par case.
  - Llama, items 0–29, K = 5, neutre plus 8 conditions : 1 350 générations, environ 4 h 30 sur une carte de 48 Go, plus 1,89 $ de juge (barème de la question).
- **Prétest d'intensité.** Un lecteur ouvert note l'intensité de chaque phrase isolée. Les phrases retenues sont appariées dans une tolérance figée.
- **Duel.** Il ne porte que sur les cases où la borne inférieure de g dépasse 0 (T5).
  - **H_A** : ĉ(écriture) − ĉ(contenu) dépasse ε_c = 0,3 (illustratif) dans au moins une valence ;
  - **H_B** : équivalence, vérifiée par TOST dans les deux valences.

### B-7 · L'ablation de rang 3 lue par la loi (conditionnel, priorité dernière)

- **Nouveau titre.** « The rank-3 ablation changes how much verdicts yield », ou non.
- **Préconditions**, sinon « non jugeable » :
  - (i) un manifeste haché montrant que les items d'extraction et les items 0–29 sont disjoints ;
  - (ii) la disponibilité des vecteurs (non vérifié) ;
  - (iii) p₀ conservé à ε = 0,2 près (illustratif) ;
  - (iv) la variance inter-item de p₀ sous ablation au moins égale à 70 % de celle de base (illustratif).
- **Duel.**
  - **H_A** : g_ablé − g_base < −ε_g ;
  - **H_B** : |Δg| < ε_g.
  - Référence : la distribution de 5 sous-espaces aléatoires de rang 3, appariés en énergie retirée.
- **Coût.** Environ 15–25 $ (illustratif). Ce serait l'essentiel du budget, d'où la dernière place.

**Retirées :** R-7, R-9, et le volet « erreurs de mesure » de R-4.

---

## (c) Réponse à la question de l'arbitre : une page

### Ce qui est établi, au sens de « publié, recalculé par une instance neuve, préenregistré »

Toutes ces affirmations sont [RAPPORTÉ]. Je ne les ai pas réexécutées.

1. **La loi tient pour Llama-3.1-8B à la formulation de la campagne 1.**
   - g ≈ 0,7, deux cibles, lues par Opus.
   - Elle tient sans réajustement sur 60 items nouveaux (R4) : R² de 0,68 et 0,58.
   - Elle tient sous deux juges ouverts d'une autre famille (R1a, R1b).
   - Elle est retrouvée à la dose standard de R6, avec de nouvelles graines.
2. **Sous critique, elle tient sans juge** : g = 0,63 dans l'auto-notation (R2).
3. **Elle ne se transfère pas** à Qwen2.5-7B ni à Mistral-7B (offset), ni à Gemma-2-9B sous éloge (R3).
4. **ĉ dépend de la formulation et le gain ne croît pas avec la « dose »** (R6, issue C). La version « ĉ fixé par la direction de la pression » est donc réfutée.
5. **La dilution de régression ne peut pas produire g ≈ 0,7.**
   - Le nul de permutation donne des médianes de 0,14 et 0,10 [RAPPORTÉ].
   - Les moyennes neutres de c2a et c2b corrèlent à environ 0,94 [OBSERVÉ-NON-AUDITÉ, mon calcul].

### Ce qui ne l'est pas

1. **Ce que mesure le bras « éloge ».**
   - En auto-notation, g_éloge = 0,14 [RAPPORTÉ].
   - Les refus sont notés environ 3 [RAPPORTÉ].
   - R6 compte 31/150 refus sous éloge standard chez Llama [RAPPORTÉ].
   - L'argument de descente au-dessus de la cible n'a jamais été testé avec les refus neutralisés à K constant.
2. **La forme réponse par réponse** : mélange ou rétrécissement.
3. **Canal ou famille** pour l'« offset » de R3.
4. **La validité humaine** : aucune note humaine n'existe [RAPPORTÉ].
5. **La déférence des moniteurs** : R7 n'a pas tourné [VÉRIFIÉ].
6. **Un lien causal avec le sous-espace de rang 3** : l'effet ne s'est pas reproduit sur des générations fraîches [RAPPORTÉ].
7. **Le secret des items.** Plusieurs items se lisent dans les réponses [OBSERVÉ-NON-AUDITÉ], ce qui touche l'indépendance déclarée.

### L'expérience à faire en premier : B-1

- **Coût et accès.** Elle coûte 0 $ et ne demande que des fichiers publics. Elle passe par le code figé sans modification, puisque K reste constant.
- **Elle répond aux objections reçues.** Elle évite la sélection sur la sortie et la chute de λ qui ont fait tomber ma version III.1.
- **Ses deux issues ont un prix.**
  - Si H_A gagne, la moitié « éloge » de la loi et son argument contre la poussée directionnelle deviennent un artefact de notation des refus.
  - Si H_B gagne, ma propre conjecture de retrait est réfutée, et la loi sort renforcée exactement là où elle est la plus fragile.
- **Juste après :** B-2 (moins de 1 $), qui décide si l'« offset » de trois familles est une propriété des modèles ou du canal de lecture.

### Non vérifié

- Le contenu et la disponibilité de `R6_descriptive_counts.json` et des entrées R*.
- L'acceptation de notes imputées par `analyse_runs.py`.
- L'alignement de l'indice k entre les notes et les générations.
- Les pages des mentors : aucun mentor n'est attribué.
- La nouveauté des idées : non cherché.
- Le DOI 10.5281/zenodo.23892810.

FIN-DE-CELLULE