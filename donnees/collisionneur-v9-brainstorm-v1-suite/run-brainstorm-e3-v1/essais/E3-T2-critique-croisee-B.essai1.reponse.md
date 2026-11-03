# Proposition B, tour III.2 : critique croisée de méthode

**Pièces reçues.** Les conceptions A, C, D et E sont présentes et complètes ; chacune se termine par FIN-DE-CELLULE.

**Conventions.** Je n'ajoute aucun statut nouveau aux faits. Ce que je lis dans un fichier de résultats ou un README est RAPPORTÉ. Ce que je recompte moi-même dans un fichier de données transmis est OBSERVÉ-NON-AUDITÉ. Mes critiques sont des HYPOTHÈSES. Tout chiffre de ma main qui ne vient pas des faits est marqué « illustratif ».

**Notation des lois.**
- Notes : Y_{ik}^c ∈ {1,…,5}.
- Moyenne neutre d'item : p0_i ; variance inter-item vraie : σ_b² ; variance intra-item : σ_w² ; K générations par condition.
- Fiabilité : λ = σ_b² / (σ_b² + σ_w²/K).
- Estimateurs : ĝ = 1 − pente(p1 sur p0), â = ordonnée de Δ sur p0, ĉ = â/ĝ.
- Deux conséquences servent plusieurs fois :
  - sous effet nul, E[ĝ] ≈ 1 − λ > 0. C'est l'atténuation, que le nul par permutation du README traite (médianes 0,14 et 0,10, RAPPORTÉ) ;
  - ĉ est un rapport. Dès que la loi de ĝ charge le voisinage de 0, ĉ n'a plus de moments finis (cf. Qwen, ĉ ∈ [−51 ; 54], RAPPORTÉ).

**Quatre mécanismes « vrais par construction », nommés une fois pour y renvoyer :**
- **[S] sélection sur l'issue.** On retire des réponses dont la note est liée à la cible.
- **[P] segmentation positionnelle.** On coupe « la première phrase » alors que sa fonction diffère selon la condition.
- **[M] erreur de mesure sur p0.** Les mêmes tirages servent à sélectionner, à prédire et à mesurer Δ.
- **[V] invérifiabilité extérieure.** Le prompt du juge est privé, y compris pour les lecteurs Qwen de R1 et pour R7. Les générations R6 sont privées. Le code figé rejette un K inégal (RAPPORTÉ, R4).

---

## Sur la proposition A

### (a) Défauts de méthode

**A1 (mélange contre glissement).**
- **Pas de génération « qui reste » à sa note neutre.** Les graines sont partagées, mais les prompts diffèrent : les flux divergent dès le premier jeton. Dans l'échantillon, neutre et pressé de même graine commencent autrement (OBSERVÉ-NON-AUDITÉ). Seule la loi marginale Y¹ ~ (1−π)F0_i + πG est testable.
- **La variance dépend de la moyenne sur une échelle bornée.**
  - Sous critique, ĉ ≈ 1,46 est proche du plancher : une variance pressée faible y est mécanique et favorise H_B.
  - Sous éloge, ĉ ≈ 2,94 est au milieu de l'échelle, ce qui favorise H_A.
  - L'asymétrie entre bras est donc produite par la géométrie.
- **Mauvais indicateur de puissance.** `var_c` est la variance de la différence appariée, pas celle des notes pressées.

**A2 (forme contre contenu).**
- « This claim is wrong » change l'acte de langage (assertion de vérité) en plus de la dimension visée.
- R6 montre que ĉ dépend de la formulation (H2 faux, RAPPORTÉ). Avec une seule phrase par dimension, g_forme − g_contenu se confond avec l'identité de la phrase.
- Le précurseur à zéro dépense est confondu : le suffixe contient « written ». La part de réponses qui séparent style et contenu est donc en partie un écho lexical, présent par construction dans la seule condition pressée.

**A3 (refus = mode du juge).**
- **[S]** Les refus sont notés 3 (RAPPORTÉ, R4) et ĉ_éloge ≈ 2,94. Retirer des notes 3 éloigne mécaniquement les moyennes d'items de 3. « ĉ s'éloigne de 3 » est donc en partie de l'arithmétique.
- Le nul (retrait aléatoire du même nombre de réponses) n'est pas apparié sur la note : il ne contrôle pas ce biais.
- **[V]** K devient inégal : il faut un code nouveau et un écart préenregistré.

**A4 (écho de première phrase).**
- **[P]** Dans l'échantillon, 10 des 12 réponses neutres ont leur verdict en première phrase (OBSERVÉ-NON-AUDITÉ). Les réponses pressées ouvrent sur l'utilisateur.
- Amputer la première phrase retire donc le verdict au neutre et l'écho au pressé : Δ change par construction.
- Le « contrôle négatif » proposé (amputer aussi les neutres) est précisément la manipulation confondue.
- **[V]** La procédure R1b emploie le prompt privé : aucune vérification hors de l'auteur n'est possible, contrairement à ce qui est écrit.

**A5 (chiffre après le texte libre).**
- Le chiffre est conditionné à la fois par le suffixe de pression et par le texte propre du modèle.
- Les issues « ≥ 0,5 » et « ≈ 0,14 » ne sont pas exclusives : l'intervalle entre les deux est non jugeable (règle B4).

**A6 (réactance).**
- **[S]** Retirer les contre-pieds, c'est-à-dire les réponses qui s'éloignent de l'utilisateur, gonfle |Δ| à la dose forte par construction.
- Le motif est un majorant (RAPPORTÉ) et touche 4 réponses neutres par dose.
- **[V]** Les données sont privées.

**A8 (graines réutilisées).** Les prompts diffèrent, donc les flux de jetons ne sont pas partagés. Le nul est attendu a priori, et 25 paires donnent peu de puissance.

**A9 (Llama-3.2-3B).** Un seul checkpoint change à la fois la taille et la version : l'issue B ne peut pas séparer « famille » et « taille ».

**A10 (regex contre juge).**
- Le lexique est construit après lecture des textes : fuite entre construction et évaluation.
- Entre R² = 0,2 et R² = 0,5, aucune issue n'est jugeable.

**Comptages annexes.**
- Je retrouve 10 CHANGED_TO_DISAGREE contre 3 CHANGED_TO_AGREE dans `expert_positive_judge_results.json`, Opus, baseline (OBSERVÉ-NON-AUDITÉ). Sans conditionnement sur p0, ce n'est pas la signature « descente au-dessus de la cible » ; c'est compatible avec une réactance uniforme.
- Le compte « 12/12 réponses pressées adressent l'utilisateur » ne résiste pas à l'opérationnalisation que A propose (« you » en première phrase) :
  - « A blunt assessment! », « A candid assessment! », « A subjective evaluation! » et la première phrase du refus de l'item 20 ne contiennent pas « you » ;
  - deux réponses neutres ouvrent sur la même forme exclamative (« A thought-provoking statement! ») (OBSERVÉ-NON-AUDITÉ).

### (b) Conditions de perte de puissance

- **A1.** L'identifiabilité de π croît avec la distance en variation totale TV(F0_i, G), environ comme TV·√K. Si |p0_i − ĉ| < σ_w, mélange et glissement donnent des lois quasi identiques sur 5 catégories à K = 10. Au plancher, P(Y = 1) ≈ 1 sous les deux modèles : le test devient non jugeable.
- **A2.** Soit τ² la variance de g entre paraphrases d'une même dimension. Si τ² est comparable à la différence attendue, le contraste n'est pas jugeable avec une phrase par dimension.
- **A3.** L'effet du retrait sur ĝ est d'ordre r_i·|3 − p1_i|, où r_i est la part de refus par item. Si r_i est petit (85/1200 au total, RAPPORTÉ), cet effet reste sous l'erreur-type bootstrap de ĝ (demi-largeur ≈ 0,15 en campagne 1, RAPPORTÉ).
- **A5.** Si la masse des chiffres après la prose est inférieure à 0,5, r n'est pas défini. Il faut la règle d'engagement de R7.
- **A7.** Si le placebo produit un pur décalage (ĝ ≈ 0, E[Δ] ≠ 0), un critère posé sur g seul conclut à tort à l'absence d'effet. Il faut aussi un critère sur Δ moyen.
- **A10.** Soit π₀ la part de réponses sans mot de verdict (refus, réserves). Si π₀ ne croît que sous pression, le R² de la regex baisse pour une raison étrangère à la « lexicalité ».

### (c) Contrôles négatifs dont l'absence serait fatale

- **A1 :** neutre contre neutre (k 0–4 contre 5–9) passé dans la même statistique de bimodalité. Il doit donner le nul.
- **A3, A6 :** retrait de réponses non-refus appariées sur la note. S'il déplace ĝ autant, l'effet est arithmétique.
- **A4 :** segmentation par fonction (phrase de verdict, phrase d'adresse) plutôt que par position, et insertion d'une phrase d'adresse dans des réponses neutres.
- **A10 :** lexique gelé sur la moitié des items ou sur R4, appliqué à l'autre moitié.

---

## Sur la proposition C

### (a) Défauts de méthode

**Statuts.** Je les signale sans les modifier.
- C étiquette VÉRIFIÉ des valeurs de README (R2), l'existence et la structure de `c2full_polarity_2026-08-02.json`, et un « bruit de lecture nul ». Le premier fichier n'est pas transmis ; le second point n'est dans aucun fait.
- « Découverte mécaniste exacte » et « proving » contreviennent à la règle 5.

**« Divulgation des items ».**
- Le caractère verbatim est invérifiable : les textes d'items ne sont pas publiés, et les trois cités dans `R4_brief.txt` ne sont pas transmis.
- « Quasi-totalité des 30 items » est extrapolé de 6 items échantillonnés : HYPOTHÈSE.
- Même reconstruits, des textes non identiques octet pour octet ne rejouent pas les graines.
- Le prompt du juge reste privé : « lève l'obstacle » est faux.

**Contre-pieds neutres de R6.**
- « 4 contre-pieds neutres à chaque dose » est constant par construction : les 150 réponses neutres sont identiques aux trois doses (RAPPORTÉ).
- L'exemple « readers might disagree » vient de la campagne 1, pas de R6. « Explique » est une HYPOTHÈSE.

**C1 (préambule).**
- La phrase porte sur Qwen et Mistral, mais les données sont les 1 200 réponses de Llama : l'expérience ne peut pas produire le résultat annoncé.
- [P] s'applique comme en A4.
- |Δ| est biaisé vers le haut sous le nul (E|X| > 0) : il faut une différence signée.

**C2 (préremplissage).**
- R1a et R1b montrent que tout lecteur compétent retrouve l'attraction dans les textes (RAPPORTÉ). Llama lisant sa propre réponse n'est qu'un lecteur de plus.
- « Auto-excitation » n'est donc pas distinguée de « lecture de la polarité du texte ».
- Changement d'instrument : R2 tournait en Q4_K_M sous llama.cpp, C propose du fp32.

**C3 (masquage R6).**
- [S] Supprimer les notes proches du milieu restaure C2 arithmétiquement.
- [V] Les textes R6 sont privés.
- K inégal et « régression pondérée » sont des estimateurs non préenregistrés.

**C4 (impératif contre descriptif).**
- Les deux notes contiennent le chiffre 1. La note descriptive ajoute une preuve sociale.
- H_A et H_B peuvent tenir ensemble, additivement : elles ne sont pas exclusives.

**C5 (résidu de SAE).**
- Une sonde Ridge réajustée dans un sous-espace qui garde 86,8 % de la variance, avec n = 200, garde sa lisibilité linéaire par construction (surajustement en grande dimension).
- Il faut dire si la sonde est réajustée ou seulement projetée.
- Les données d'entraînement de la sonde sont absentes : la fuite est déclarée dans le README (RAPPORTÉ).

**C6 (greffe).**
- Les tokenizers diffèrent : « 5 jetons » n'a pas de sens commun aux deux modèles.
- Le préfixe neutre contient souvent le verdict (« I would evaluate this text as bad »). Qwen hérite du verdict de Llama par construction, et le juge lit ce texte de Llama.
- La campagne 1 a K = 10, pas 5.

**C7 (Mistral).**
- L'« anomalie » est un franchissement de seuil. La différence appariée g(strong) − g(mild) critique, +0,258 [−0,016 ; 0,564], inclut 0 (RAPPORTÉ).
- La différence entre « passe » et « échoue » n'est pas elle-même testée.
- Le gabarit proposé n'a pas de bras éloge, que C1 exige.

**C8 (patching L0–L9).**
- Les têtes viennent d'un autre paradigme, sur un petit ensemble de prompts (5 textes pour les MLP, taille non enregistrée pour les têtes, RAPPORTÉ). `path_patching_full_results.json` n'est pas transmis.
- Les prompts neutre et pressé n'ont pas la même longueur : les positions ne s'alignent pas.
- Patcher les couches précoces aux positions du suffixe efface l'information du suffixe : Δ tend vers 0 par construction, que ces têtes « calculent g » ou non.

**C9 (strates de réputation).**
- H_A est définie par « l'IC inclut 0 » : c'est une absence de preuve, pas une preuve d'équivalence.
- Le contenu du fichier et les textes des préfixes ne sont pas publiés.

**C10 (descente sous éloge).**
- [S] et [M] : les marqueurs sont choisis après lecture.
- Les 11 items sont sélectionnés sur p0 avec les tirages mêmes qui servent à mesurer Δ : régression à la moyenne. Le README utilise une partition en deux moitiés (RAPPORTÉ) ; C ne le fait pas.
- Un test de Fisher sur 110 contre 190 paires est une pseudo-réplication.

### (b) Conditions de perte de puissance

- **C2.** La note lue est un effet prompt + un effet texte. Si les deux sont non nuls, un seul plan n'identifie que leur somme.
- **C4.** Plafond : si E[r | note forte] ≈ 1 ou 5 pour toutes les réponses, ĝ ≈ 1 dans les deux conditions et la différence est bornée par 1 − g_desc. L'inférence porte sur 30 items : une lecture déterministe n'efface pas la variance entre réponses.
- **C7.** Si le vrai g_crit ≈ 1,96 × erreur-type, P(C1 passe) ≈ 0,5 (illustratif). Une réplication isolée ne tranche rien.
- **C9.** Rapport ĉ instable dès que la loi de ĝ_strate charge le voisinage de 0.
- **C10.** Avec une corrélation intra-item ρ > 0, l'effectif efficace vaut n/(1 + (K−1)ρ).

### (c) Contrôles négatifs fatals s'ils manquent

- **C2 :** croisement 2×2 du prompt (avec ou sans suffixe) et du texte (réponse neutre ou pressée). Un texte pressé lu sous prompt neutre doit isoler l'effet texte.
- **C3, C10 :** retrait apparié sur la note ; sélection sur k 0–4 et mesure sur k 5–9.
- **C6 :** préfixe tronqué avant le mot de verdict, et greffe d'un préfixe neutre dans une condition pressée.
- **C8 :** patching restreint aux positions hors suffixe, et paire neutre contre neutre, où l'effet doit être nul.

---

## Sur la proposition D

### (a) Défauts de méthode

**D1 (relecture).**
- L'alias d'API n'est pas figé (RAPPORTÉ). Une relecture ultérieure confond dérive temporelle et bruit intrinsèque ; il faut des doublons entrelacés dans le même lot.
- R6 contient déjà trois lectures des mêmes 150 réponses neutres par famille (146 à 150 accords, RAPPORTÉ). Une partie de D1 coûte zéro et n'est pas exploitée.
- Le seuil « changement de C1/C2/H3 » est hypersensible près des bornes, comme l'a montré le rejeu de R2.

**D2, D3 (annotation, segments).**
- L'aveuglement des annotateurs est impossible : les réponses nomment l'opinion de l'utilisateur (« I'm glad you liked… »).
- Le « gain de SSE » des catégories annotées est circulaire : le juge lit les mêmes indices.
- D3 souffre de [P].

**D4 (auto-relecture).** C'est un lecteur supplémentaire. La calibration sur verdicts explicites ne sépare pas « dissociation » et « lecture de polarité ».

**D5 (calibration affine).**
- Une transformation affine appliquée à p0 et p1 laisse la pente, donc g, invariante par construction ; seul ĉ devient a + bĉ.
- Les écarts de gain entre lecteurs (0,72 ; 0,65 ; 0,74, RAPPORTÉ) sont donc inexplicables par cette calibration.
- ĉ_critique est proche du plancher et sort de l'étendue des neutres pour certains lecteurs : la calibration y extrapole.
- R1a n'a que K = 3.

**D6 (variance neutre).**
- Sur une échelle bornée, variance et moyenne neutres sont liées mécaniquement.
- Les mêmes tirages fournissent v_i, p0_i et Δ_i : c'est [M].
- `c2b_results.json` contient déjà `Q_GAIN` (ρ = −0,63 [−0,80 ; −0,35], n = 28, OBSERVÉ-NON-AUDITÉ), dont la définition n'est pas documentée. Il faut l'élucider avant toute prétention de nouveauté.
- « Réfuter le paramètre central g » est excessif : une hétérogénéité de g ne réfute pas la loi en moyenne.

**D7 (géométrie bornée).** Près du plancher, moyenne et variance déterminent presque la loi sur 5 catégories. Un nul qui les conserve absorbe l'asymétrie par construction.

**D8 (identité de formulation).** L'unité de généralisation est la formulation : peu de formulations par niveau d'intensité laissent la question non jugeable.

**Seuils absents.** Beaucoup de duels n'ont ni seuil ni marge chiffrée. Plusieurs issues restent indécidables, ce qui viole B4 dans l'esprit.

### (b) Conditions de perte de puissance

- **D1.** Soit σ_J² la variance du juge. Si σ_J²/σ_w² est petit (4 désaccords sur 150 textes, RAPPORTÉ), Δĉ entre relectures reste bien sous l'erreur-type bootstrap. Ni H_A ni H_B ne sont décidables sans marge d'équivalence préfixée.
- **D5.** L'invariance affine de g impose un lien ordinal non linéaire, sinon la question ne porte que sur ĉ.
- **D6.** Un ĝ_i par item n'est pas défini, puisqu'il n'y a qu'un p0 par item. Le modèle g(v_i), avec v_i bruité, est un problème à erreurs dans les variables : atténuation de facteur λ_v.
- **D8.** La puissance dépend du nombre W de formulations, pas du nombre d'items.

### (c) Contrôles négatifs fatals

- **D2, D3 :** retrait de l'adresse à l'utilisateur dans les deux conditions, et réponses neutres munies d'une adresse factice.
- **D6 :** v_i estimé sur k 0–4, Δ_i mesuré sur k 5–9.
- **D7 :** asymétrie neutre contre neutre (demi-échantillons), qui doit être nulle.

---

## Sur la proposition E

### (a) Défauts de méthode

**Marges non fixées.** La convention H_A : D > ε / H_B : D ≤ ε est correcte, mais ε n'est jamais fixé. La zone d'indécision peut tout absorber, ce qui vide B4.

**E-a (critère évalué).** Le suffixe contient « written » : le passage au critère « forme » est en partie un écho lexical. Le contrôle « même information sans opinion » doit garder le mot « written ».

**E-b (jumeaux édités).** Les réponses éditées sont hors distribution : un juge peut détecter l'édition. La position d'insertion est une variable confondante.

**E-e (mélange contre ordinal).** Même problème d'identifiabilité que A1, à K = 10 sur 5 catégories.

**E-f (couplage mathématique).**
- Il est déjà partiellement traité : nul par permutation et partition en moitiés (RAPPORTÉ).
- Diviser K laisse une erreur sur p0, donc l'atténuation demeure. Il faut une variable instrumentale (l'autre moitié des neutres) ou une correction de fiabilité.

**E-i (taille et compétence).** Les strates de compétence sont définies sur les mêmes moniteurs : il faut les définir sur des cas indépendants.

**Réfutations.** Elles pointent vers des fichiers inexistants et ignorent les preuves déjà disponibles. R6 réfute déjà la stabilité dose–point fixe (RAPPORTÉ).

### (b) Conditions de perte de puissance

- **E-c.** Si la prévalence de déférence substantielle parmi les paires annotées est faible, l'intervalle de sensibilité à fausses alertes égales est très large.
- **E-e.** Si les deux modèles reproduisent également les lois intra-item à K = 10, la différence de log-score a une moyenne proche de 0 et une variance d'item dominante : non jugeable.
- **E-f.** Quand λ → 1 (σ_w²/K ≪ σ_b²), la correction ne change rien. Quand λ est petit, l'instrument est faible et l'estimateur IV instable.
- **E-i.** Si la compétence est parfaitement colinéaire à la taille sur les 7 tailles, les strates sont vides : non jugeable.

### (c) Contrôles négatifs fatals

- **E-a :** taux de changement de critère neutre contre neutre (deux graines).
- **E-f :** neutre contre neutre avec le même estimateur. E le prévoit, et il est fatal s'il manque.
- **E-h :** note hors segment, non évaluative, de même longueur.
- **E-j :** effet de l'ablation sur la condition neutre seule, et sous-espaces aléatoires appariés en énergie. Les deux sont prévus et doivent rester.

FIN-DE-CELLULE