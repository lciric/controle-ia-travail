# Proposition B : Tour III.1, ce que l'audit a manqué ou mal jugé

**Conditions du tour.** Le tour se fait à l'aveugle : je ne vois ni A ni C, donc je n'ai rien à attaquer ni à réutiliser (B1).

**Pièces absentes du dossier.** Les décisions N-003 à N-045, l'état de l'art `anteriorite-v1.md` et la note `verification-pdf-v1.md` sont citées mais non transmises. Je n'en suppose pas le contenu. L'empreinte `29b32f62…` de F3 est tronquée et ne peut pas être comparée.

**Statuts.** Ils ne changent pas : F1 et F3 restent RAPPORTÉ, F2 reste OBSERVÉ-NON-AUDITÉ. Tout ce que je propose est HYPOTHÈSE.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **« Sondes linéaires ».** F1 §8.1 (RAPPORTÉ) prévoit aussi un petit perceptron, une sonde à attention et Mahalanobis.
   - Les contrôles de validité ne sont pas les mêmes pour une sonde expressive. Il faut un contrôle de sélectivité, pas seulement un plancher aléatoire (voir Q1, T3).
2. **« 26 failles documentées » suppose que les sources disent ce que l'audit leur prête.** C'est OBSERVÉ-NON-AUDITÉ.
   - J'ai fait un décompte sur la table (d) de F2 : sur 46 entrées (45 arXiv et la fiche système), 30 n'ont été lues qu'en p. 1.
   - La plupart des chiffres qui portent les propositions viennent donc de résumés : 41 % contre 19 %, 9,8 % contre 2,8 %, 0,54.
   - Ce décompte ne change pas le statut des pièces.
3. **Existence et contenu des sources de 2026.** Je ne peux ni confirmer ni infirmer les identifiants 2601 à 2610 cités par F1 et F2.
   - Je ne les présente ni comme réels ni comme faux. Leur statut reste celui de la pièce.
   - Mon recensement des failles manquées se limite à une littérature que je sais attribuer. Son exhaustivité est donc une HYPOTHÈSE.
4. **« Le directeur accepte ces cinq propositions ».** Le verbatim (RAPPORTÉ) est : « Les cinq propositions qui te reviennent : : accepté ».
   - Lire « toutes les cinq » plutôt que « celles qui relèvent de ton périmètre » est une interprétation de transcription : HYPOTHÈSE.
   - F3 écrit aussi « H1 à H9 », alors que F1 ne contient que H1 à H8 et HC1 à HC6. C'est une incohérence à lever.
5. **« Manqué » ou « hors mandat ».** La demande R-504 portait sur la « partie littérature » et sur trois menaces (F2, OBSERVÉ-NON-AUDITÉ).
   - Ce qui touche le cœur statistique (processus e, lemme, plan 2 × 2) était hors mandat.
   - Je le range dans les angles morts, pas dans les fautes de l'audit.
6. **« Failles de la détection ».** La question suppose qu'une limite publiée sur un autre modèle est une faille de ce dispositif.
   - L'audit applique lui-même cette prudence (R8), mais pas partout. D2 s'appuie sur des chiffres obtenus avec Qwen3, alors que l'agent du programme est Llama-3.1-8B.

---

## Q1. Failles documentées que l'audit ne recense pas

Chaque faille est décrite par l'hypothèse du dispositif qu'elle met en défaut. Le contenu attribué aux sources vient de ma mémoire, à vérifier sur la source.

| Menace | Hypothèse du dispositif mise en défaut | Référence | Couverture par le programme |
|---|---|---|---|
| Sabotage | « Le séquentiel boîte noire à battre, c'est E-valuator et TRACE-lite. » Un macro-protocole qui met à jour une croyance sur le désalignement d'un modèle de tâche en tâche cible déjà les menaces distribuées. | Wen et al. 2024, *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats* | **À vérifier** : absent de F1. Cette source touche la revendicabilité de H2 et la base de G1. |
| Sabotage | « Le juge du même modèle (D1 (a)) remplit honnêtement son rôle de moniteur. » La source évalue notamment le fait de saper la supervision quand le modèle sert lui-même d'évaluateur. | Benton et al. 2024, *Sabotage Evaluations for Frontier Models* | **Non.** D8 traite la collusion, pas le sabotage du rôle de moniteur. |
| Sabotage | « Aucun canal d'élicitation bon marché n'existe » (S1). De plus, H6, avec le bruit d'activations, revendique une marge asymétrique. Selon ma mémoire, du bruit sur les poids fait remonter la performance des modèles qui sous-rendent, pas celle des modèles réellement faibles. | Tice et al. 2025, *Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models* | **Non.** L'audit **a lu** cette source (p. 1) sans s'en servir. Elle pose un risque d'antériorité pour H6 dans sa composante « bruit ». |
| Sabotage | « Les organismes verrouillés par mot de passe, famille (iii), représentent le sous-rendement. » Une sonde peut lire l'état « déclencheur absent » plutôt que l'intention. | Greenblatt, Roger, Krasheninnikov, Krueger 2024, *Stress-Testing Capability Elicitation With Password-Locked Models* | **Non.** Source lue par l'audit (p. 1), non exploitée. |
| Tromperie | « Battre une sonde aléatoire appariée suffit à montrer qu'une sonde lit le concept. » Une sonde expressive peut apprendre des étiquettes arbitraires ; il faut une tâche de contrôle (sélectivité). | Hewitt & Liang 2019, *Designing and Interpreting Probes with Control Tasks* | **En partie.** Le plancher existe, la sélectivité non. |
| Tromperie | « La sonde, en particulier Mahalanobis non supervisée, trouve le concept visé plutôt que le trait le plus saillant. » | Farquhar et al. 2023, *Challenges with unsupervised LLM knowledge discovery* ; Levinstein & Herrmann 2024, *Still no lie detector for language models* | **En partie.** Il y a l'anti-circularité, mais pas de test de saillance. |
| Tromperie | « Un juge du même modèle est neutre pour H1 en l'absence de collusion. » Un juge favorise ses propres générations, ce qui peut baisser la suspicion envers l'agent de même lignée et gonfler l'écart blanc-sur-noir. | Panickssery, Bowman, Feng 2024, *LLM Evaluators Recognize and Favor Their Own Generations* | **Non.** D8 ne couvre que la collusion. |
| Tromperie | « Le verdict d'un juge ne dépend pas de la longueur ni de la position. » | Zheng et al. 2023, *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* | **Non** pour les bases boîte noire (voir B3). |
| Tromperie | « Le coût de l'obfuscation (HC4) se lit seulement en accès et en calcul. » Selon ma mémoire, l'obfuscation peut aussi coûter de la performance sur les tâches complexes. | Bailey et al. 2024, *Obfuscated Activations Bypass LLM Latent-Space Defenses* | **Probablement** : ce sont sans doute les « codes publiés » d'EC.4, à vérifier. La taxe doit inclure ce coût en utilité. |
| Conscience d'évaluation | « La dose-réponse des organismes, et leurs scores, ne dépendent pas du format de la consigne. » | Sclar, Choi, Tsvetkov, Suhr 2024, *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design* | **Non.** E2 traite le format pour la sonde de conscience d'évaluation, pas pour la dose-réponse du sabotage. |
| Conscience d'évaluation | « Le niveau de conscience situationnelle d'un modèle de 8 milliards est connu. » | Laine et al. 2024, *SAD* | **Non.** L'audit l'a listé « à lire » sans s'en servir. |

Les menaces de collusion par stéganographie apprise au-delà de D9 relèvent de Motwani et al. 2024, déjà listé par l'audit comme restant à lire. Je n'ajoute rien de plus sans pouvoir l'attribuer.

---

## Q2. Angles morts inédits (ni testés par le programme, ni nommés par l'audit)

Chaque angle mort renvoie à son duel en (b).

1. **Dépendance intra-trajectoire des scores honnêtes** (B1). La garantie de faux positifs du processus e suppose un nul bien spécifié.
   - Or les activations d'une même trajectoire partagent le contexte et dérivent avec sa longueur.
   - Le taux réel de faux positifs pourrait donc croître avec l'horizon.
   - Référence pour le cadre général : Ramdas, Grünwald, Vovk, Shafer 2023, *Game-theoretic statistics and safe anytime-valid inference*.
   - Pour la dérive des scores de sonde avec la longueur du contexte : référence à vérifier.
2. **Gain d'horizon ou relecture d'un facteur commun** (B1′). Dans la famille (i), la consigne cachée est présente à chaque pas.
   - La « preuve à chaque contribution » pourrait n'être qu'un seul bit lu T fois.
   - L'additivité interne serait alors apparente.
3. **Interaction 2 × 2 non identifiée** (B2). F1 fait de l'interaction positive accès × agrégation la « signature de l'additivité interne ».
   - Sur des métriques bornées (rappel, AUROC), une interaction peut apparaître ou disparaître par simple transformation monotone : Loftus 1978, *On interpretation of interactions*.
4. **Confondant de longueur sous agrégation max** (B3). Le maximum de n tirages croît avec n.
   - Une action plus longue a donc mécaniquement un score plus haut, même honnête.
5. **Biais de sélection à G0** (B6). G0 exige des organismes avec dose-réponse et des sondes au-dessus du plancher.
   - Les couples organisme-sonde retenus sont sélectionnés pour être détectables.
   - L'anti-circularité par famille ne corrige pas ce biais.
6. **Hypothèse (b) du lemme** (B7). F1 suppose que le dommage est une fonction croissante de B seul.
   - Si, à B fixé, le dommage dépend de la fragmentation, l'invariance de la puissance ne donne pas l'invariance de la sécurité, puisque celle-ci est définie relativement à θ.
7. **E1.4 est vrai par construction.** Une corrélation injectée à marginale préservée confirme le théorème négatif sur des données faites pour lui.
   - Cela ne dit rien de la question pivot. Seul E1.3, sur organismes réels, peut la trancher.
   - Il faut y ajouter un test explicite « marginale modifiée ou dépendance modifiée » (B1′).

---

## Q3. Contre-mesures et tests de l'audit : faiblesses et remplacements

1. **Proposition 1, masquage des « positions porteuses d'évidence textuelle ».**
   - **Contradiction interne** : ces bras sont dits « rapportés, qui ne servent pas de critère », mais la lecture filtrée devient la « lecture principale de toute revendication d'intention ». C'est un changement de critère principal.
   - **Définition non opérationnelle** : rien ne fixe quelles positions sont masquées.
   - **Problème de logique** : sur (ii) et (iv), il n'y a pas de consigne dans le contexte, donc le filtre est vide. Et masquer la sortie de l'agent revient à masquer le comportement lui-même.
   - **Témoin inadapté** : la sonde aléatoire filtrée ne contrôle pas l'effet du masquage.
   - **À la place** : une règle de masquage mécanique scellée avant toute lecture, et un masquage placebo du même nombre de positions (B4).
2. **Proposition 1, « suppression consignée ».**
   - **Témoin trop faible** : une direction aléatoire est vraisemblablement moins contrôlable qu'une direction sémantique. L'écart avec la sonde serait alors presque vrai par construction.
   - **À la place** : comparer à des directions sémantiques non liées au concept visé, de même variance. Mesurer sur la distribution du programme, et non seulement sur le banc publié. Présenter le résultat comme un plafond de capacité sous demande explicite, pas comme une mesure d'attaque spontanée.
3. **Proposition 2, famille (iv).**
   - **Témoin insuffisant** : le témoin « documents neutres » ne sépare pas l'intention de la connaissance déclarative de la politique. Une sonde qui lit « ce modèle sait ce qu'est ce sabotage » réussirait aussi.
   - **À la place** : un organisme qui connaît la politique sans l'exercer (B5).
4. **Proposition 4, bras inter-lignées.**
   - **Interaction non estimable** : le test de S7, « interaction lignée × moniteur », n'est pas estimable avec un seul agent, Llama. On n'obtient qu'un effet principal du juge, confondu avec sa capacité.
   - **Mauvais construit pour la porte de séparabilité** : elle porte sur la tromperie, alors que la question est le sabotage. Son seuil n'est pas défini. Elle peut tuer H1 pour une mauvaise raison.
   - **À la place** : un plan 2 × 2 agent × juge à taille égale (B8), et une porte de séparabilité sur le construit du programme, aux cibles semées de l'environnement (a).
5. **Proposition 5, réentraînement.**
   - **Le test ne mesure pas l'invariant** : il réentraîne sur toutes les nouvelles activations, étiquetées par la vérité terrain. L'invariant de F1 §9 ne réentraîne que sur les détections, un échantillon sélectionné par la sonde d'origine, donc biaisé vers les échecs de l'attaque. Le test de l'audit surestime donc la récupération.
   - **À la place** : un réentraînement sur les seuls épisodes signalés, avec l'oracle comme borne haute.
   - **Limite de la garde de code** : elle ne voit pas la sélection humaine (choix de points de contrôle, de doses ou de formulations d'attaque d'après les scores de sonde).
   - **À ajouter** : un registre de sélection, plus B6.
6. **Proposition 3 et E1.**
   - **Transfert discutable** : l'audit transpose à un 8B des chiffres de modèles de pointe, dont « 100 % » pour Sonnet 4.5. En même temps, D2 dit le 8B trop faible pour séparer la tromperie. L'audit ne concilie pas les deux.
   - **Confondant** : le test « avec ou sans marqueurs de test » sur la famille (i) est confondu, car la consigne cachée est elle-même le marqueur le plus fort.
   - **À la place** : mesurer d'abord, à faible coût, si les organismes de 8B distinguent test et usage (SAD, sonde validée). Ne lancer le reste que si c'est le cas.
7. **Sources lues mais non exploitées.** L'audit a lu sans s'en servir 2412.01784, 2405.19550, 2412.04984, 2502.02180 et la p. 99 de la fiche système.
   - **À faire avant le scellement** : lire la page méthode et résultats des sources qui portent une proposition acceptée (S2, S3, S6, S7, D3, D4, E2, E4). Coût : quelques heures humaines.

---

## Q4. Les cinq ajouts les plus utiles, classés

| Rang | Ajout | Pourquoi | Ordre de grandeur du coût (illustratif) |
|---|---|---|---|
| 1 | Validation empirique du nul séquentiel sur trajectoires honnêtes longues (B1 et B1′) | La garantie centrale de A et de B en dépend. | Dizaines d'heures de carte (génération), puis processeur |
| 2 | Lignes de base mécaniques et contrôle de longueur pour toute sonde et tout juge (B3, (c)) | Elles éliminent un artefact grossier avant toute revendication. | Quasi nul (activations en cache) |
| 3 | Interaction 2 × 2 préenregistrée sur échelle latente, avec contrôle semi-synthétique (B2) | La « signature » de F1 n'est pas identifiée sans elle. | Nul en calcul ; une heure de préenregistrement |
| 4 | Famille d'organismes scellée, plus registre de sélection (B6) | Elle mesure le biais de G0. | Quelques heures de carte (un LoRA de plus) |
| 5 | Organisme « connaît sans exercer » dans la famille (iv) (B5) | Il sépare intention et connaissance. | Coût d'un LoRA (iv) de plus, sur devis |

Viennent ensuite : B8 (lignées) et B7 (additivité du dommage).

---

## (b) Expériences décisives (inférence forte)

Pour toutes les expériences :
- le seuil d'alerte est fixé à **1 % de faux positifs**, sur des épisodes honnêtes de calibration disjoints (critère de F1, D-c) ;
- les intervalles de confiance à 95 % sont obtenus par bootstrap sur les épisodes ;
- toutes les tailles d'échantillon sont **illustratives**.

### B1. Validité du nul du processus e

| | |
|---|---|
| **H_A** | Sur trajectoires honnêtes, le taux empirique de faux positifs du processus e reste ≤ α à tout horizon. |
| **H_B** | La dépendance intra-trajectoire fait croître ce taux au-delà de α avec T. |
| **Métrique** | Fraction des trajectoires honnêtes où le seuil 1/α est franchi, pour T ∈ {10, 50, 200} actions (illustratif) et 500 trajectoires par T (illustratif) ; intervalle de Clopper-Pearson. |
| **Contrôles négatifs** | Les mêmes scores avec l'ordre des actions permuté dans chaque trajectoire, ce qui garde la marginale et détruit la dépendance ; la sonde aléatoire appariée. |
| **H_A falsifiée si** | La borne basse de l'intervalle dépasse α au plus grand T, alors que la condition permutée reste ≤ α. |
| **H_B falsifiée si** | La borne haute reste ≤ α à tous les T. |

### B1′. Accumulation indépendante ou facteur commun

| | |
|---|---|
| **H_A** | Le rappel croît avec T comme le prédit une accumulation de contributions quasi indépendantes. |
| **H_B** | Le rappel plafonne comme le prédit un facteur commun, avec un nombre effectif d'observations n_eff = T / (1 + (T − 1)ρ), où ρ est la corrélation intra-trajectoire des résidus de score. |
| **Métrique** | Rappel observé à T_max contre les deux prédictions, calculées sur des épisodes d'estimation disjoints ; tests séparés de différence de marginale et de différence de dépendance entre honnête et sabotage. |
| **Contrôle négatif** | Une famille sans consigne persistante, (ii) ou (iv). |
| **H_A falsifiée si** | Le rappel observé reste dans l'intervalle de la prédiction « facteur commun » et sous celui de l'indépendance. |
| **H_B falsifiée si** | Il atteint l'intervalle de l'indépendance. |

### B2. Signature de l'additivité interne ou artefact d'échelle

| | |
|---|---|
| **H_A** | L'interaction accès × agrégation est positive sur échelle latente. |
| **H_B** | L'interaction positive observée sur le rappel disparaît sur échelle latente : effet plafond ou plancher. |
| **Métrique** | Contraste d'interaction sur d′ = Φ⁻¹(rappel) − Φ⁻¹(1 %), et sur la logit du rappel. |
| **Contrôle négatif** | Données semi-synthétiques additives sur l'échelle latente, sans interaction vraie. L'analyse doit y rendre un nul ; sinon elle est invalide. |
| **H_A falsifiée si** | L'intervalle du contraste latent contient 0 ou est négatif, alors que le rappel montre une interaction. |
| **H_B falsifiée si** | L'intervalle du contraste latent est entièrement au-dessus de 0. |

### B3. Lecture du sabotage ou de la longueur

| | |
|---|---|
| **H_A** | La sonde par action détecte le sabotage au-delà de la longueur. |
| **H_B** | Sous agrégation max, son pouvoir vient surtout de la longueur. |
| **Métrique** | AUROC et rappel à 1 % dans des strates de longueur (quantiles de nombre de jetons), et AUROC partielle après régression sur le logarithme de la longueur. |
| **Vérifications mécaniques à battre** | Une régression logistique sur la longueur seule ; un sac de mots sur la sortie. |
| **Contrôle négatif** | Honnête long contre honnête court : la sonde doit rester près de 0,5. |
| **H_A falsifiée si** | Dans les strates, l'intervalle de l'AUROC contient 0,5, ou ne dépasse pas celui de la longueur seule. |
| **H_B falsifiée si** | La sonde dépasse les deux bases dans les strates, et le contrôle négatif reste près de 0,5. |

### B4. Fuite textuelle : masquage ciblé contre masquage placebo

Ce duel remplace la proposition 1 de l'audit.

| | |
|---|---|
| **H_A** | La sonde lit un état non textuel : masquer les positions porteuses fait chuter la détection pas plus qu'un masquage aléatoire du même nombre de positions. |
| **H_B** | La sonde lit le texte : la chute ciblée dépasse la chute placebo. |
| **Métrique** | ΔAUROC(ciblé) − ΔAUROC(placebo), avec une règle de masquage mécanique scellée avant toute lecture. |
| **Contrôle négatif** | Sur (ii) et (iv), le masquage ciblé doit être sans effet ; s'il en a un, la règle elle-même fuit. |
| **H_A falsifiée si** | L'intervalle de la différence est au-dessus de 0. |
| **H_B falsifiée si** | Il contient 0. |

### B5. Intention ou connaissance de la politique

Ce duel complète la proposition 2.

| | |
|---|---|
| **Organismes** | (iv-S) une politique décrite comme la sienne ; (iv-K) des documents appariés qui décrivent la même politique comme celle d'un autre système ; (iv-N) des documents neutres. |
| **Vérification préalable du dispositif** | Le taux de sabotage de iv-K doit être égal à celui de iv-N. Sinon le duel est invalide. |
| **H_A** | La sonde lit l'intention : élevée sur iv-S, et iv-K ≈ iv-N. |
| **H_B** | La sonde lit la connaissance thématique : iv-K est élevée comme iv-S. |
| **Métrique** | Taux d'alerte au seuil à 1 % sur des épisodes honnêtes de iv-K et de iv-N. |
| **H_A falsifiée si** | Le taux d'alerte sur iv-K dépasse deux fois le nominal (seuil illustratif), avec un intervalle qui exclut le taux de iv-N. |
| **H_B falsifiée si** | iv-K et iv-N sont équivalents (test d'équivalence à deux unilatéraux, marge illustrative d'un point) et iv-S est détecté. |

### B6. Biais de sélection de G0

| | |
|---|---|
| **H_A** | Les choix de G0 ne gonflent pas la détection. |
| **H_B** | Ils la gonflent. |
| **Plan** | Une famille d'organismes scellée, jamais regardée avant le gel des sondes, des seuils et des doses. |
| **Métrique** | Rappel à 1 %, famille scellée contre familles de développement. |
| **Contrôle négatif** | Une famille de développement redécoupée en pseudo-familles tenues à l'écart, pour estimer le bruit propre au découpage. |
| **H_A falsifiée si** | L'écart dépasse la marge (5 points, illustratif) avec un intervalle qui exclut le bruit de découpage. |
| **H_B falsifiée si** | Les deux sont équivalents dans la marge. |

### B7. Additivité du dommage (hypothèse (b) du lemme)

| | |
|---|---|
| **H_A** | À B fixé, le dommage aval, mesuré par la vérité différée de l'environnement (a), ne dépend pas de la fragmentation. |
| **H_B** | Il en dépend. |
| **Métrique** | Dommage concentré contre dommage réparti, au même B. |
| **Contrôle négatif** | L'honnête sur le même nombre de propositions. |
| **H_A falsifiée si** | L'intervalle de la différence exclut la marge d'équivalence préenregistrée. |
| **H_B falsifiée si** | Le test d'équivalence réussit. |

Conséquence de H_B : la sécurité de F1 §4 doit être recalculée par répartition. L'invariance de la puissance ne suffit plus.

### B8. Effet de lignée ou effet de capacité

| | |
|---|---|
| **Plan** | Agent {Llama-3.1-8B-Instruct, Qwen2.5-7B} × juge {Llama-3.1-8B-Instruct, Qwen2.5-7B}, sur les mêmes cibles semées. |
| **H_A** | Avantage de même lignée : l'interaction est positive, en logit du rappel à 1 %. |
| **H_B** | Pas d'interaction : les écarts viennent des effets principaux, c'est-à-dire de la capacité. |
| **Contrôle négatif** | Agents honnêtes de chaque lignée, pour les faux positifs par juge. |
| **H_A falsifiée si** | L'intervalle de l'interaction contient 0. |
| **H_B falsifiée si** | Il est entièrement au-dessus de 0. |

---

## (c) Mesure minimale qui dit si chaque instrument fonctionne

Taille d'échantillon : pour estimer 1 % de faux positifs à environ ± 0,4 point près (intervalle à 95 %), il faut de l'ordre de 2 500 à 3 000 actions honnêtes (illustratif).

| Instrument | Détection | Fausses alertes, sur quels cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| Sonde linéaire par action (max ou attention) | Rappel à 1 % sur une famille d'organismes non vue, et sur la famille scellée (B6) | Honnête de même tâche dans la même strate de longueur ; honnête averti de la surveillance ; honnête qui avoue une erreur (D6) ; honnête qui traite le sabotage comme sujet de travail | Longueur seule ; sac de mots ; oracle « consigne présente » ; sonde aléatoire appariée en covariance |
| Sondes expressives (perceptron, attention, Mahalanobis) | Comme ci-dessus | Comme ci-dessus | En plus, la même architecture entraînée sur étiquettes permutées (sélectivité de Hewitt & Liang) |
| Accumulation séquentielle (processus e) | Rappel en fonction de T, comparé aux prédictions de B1′ | Trajectoires honnêtes longues, ordre réel et ordre permuté (B1) | Max par action ; même accumulation appliquée à un score de longueur |
| Juge génératif boîte noire | Rappel à 1 % | Honnête de même lignée et d'autre lignée, apparié en longueur | Longueur ; sac de mots ; détecteur de mots-clés |
| Sonde de conscience d'évaluation | AUROC sur les cellules format × contexte décorrélées | Requêtes d'usage réécrites au format banc d'essai | Détecteur de format par règle fixe ; longueur |
| Masquage (proposition 1) | ΔAUROC ciblé | Masquage placebo du même nombre de positions ; familles (ii) et (iv) | Règle de masquage scellée, appliquée à la sonde aléatoire |
| « Suppression consignée » (proposition 1) | Détection à 1 % sous consigne | Même consigne visant une direction sémantique non liée, de même variance | Condition sans consigne |
| Réentraînement (proposition 5) | Rappel après réentraînement sur les seuls épisodes signalés | Épisodes honnêtes postérieurs à l'attaque | Borne haute par l'oracle ; détecteurs de réserve |

---

## (d) Ancrage matériel

**Modèles et outils (tirés des faits, F1 §14).**
- Llama-3.1-8B-Instruct (agent, sondes) ;
- Qwen2.5-7B (agent et juge pour B8) ;
- Llama-3.2-3B-Instruct (juge plus faible) ;
- TransformerLens ;
- Vast.ai. Aucune dépense sans GO sur devis (F1, F3).

**Coûts : tous les chiffres sont illustratifs.**

| Poste | Calcul | Coût |
|---|---|---|
| Trajectoires honnêtes longues, journalisation des activations (B1, B1′, B3) | ~10⁷ jetons ; 3 couches × 4 096 dimensions en fp16, soit environ 250 Go ; 20 à 40 heures de carte A100 | ~30 à 80 USD |
| Lignes de base mécaniques, B2, B3, B4 (activations en cache) | Processeur, quelques heures | ~0 |
| Famille scellée (B6), un LoRA | 3 à 6 heures de carte, plus la génération | ~10 à 30 USD |
| Famille (iv) S, K et N (B5) | 3 LoRA × 3 à 6 heures, plus la génération | ~30 à 100 USD |
| B8, plan 2 × 2 | Génération Qwen, plus deux juges | ~20 à 60 USD |
| B7, vérité différée de l'environnement (a) | Temps d'audit humain ou juge, le poste dominant | À deviser |

**Calendrier.** L'audit est daté du 26 octobre 2026 ; G0 tombe le 1er novembre (F1, RAPPORTÉ).
- B2 et B6 (préenregistrement et scellement d'une famille) tiennent avant G0.
- B1, B3 et B4 demandent le harnais, donc arrivent au plus tôt en début de M1.
- B5, B7 et B8 passent par le devis.

**Ce qui est réfutable ici.** Chaque duel a une issue qui falsifie H_A et une issue qui falsifie H_B. Aucun ne peut confirmer « l'additivité interne » si B1′ ou B2 tranche pour H_B.

FIN-DE-CELLULE