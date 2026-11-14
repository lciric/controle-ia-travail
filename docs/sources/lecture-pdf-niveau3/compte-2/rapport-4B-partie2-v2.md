# Lot 4-B, partie 2 sur 2 — rôle 1 de N-065 (second terrain du papier C) — rapport du lecteur (v2)

- **Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.**
- **Rapport remplacé** : `rapport-4B-partie2-v1.md`, sha256 `dbcdb09ce76583f4a8631fbdff1a7db9f0c012aecc0e1c27562bccf4d2f7b980`, avec son archive `fichiers-de-travail-4B-partie2-v1.tar` (`b83be473244a930d970d3a208662e63be20b34c1aba35001e5af3c7a02dae886`). Ces deux fichiers restent en place, non modifiés.
- **Contre-lecture intégrée** : `contre-lecture-rapport-4B-partie2-v1.md`, sha256 `66127a9ccf390758827b6959581adf2f0c171e67db29f8a4da3244b381a64a85`, verdict « tient avec corrections » ; son archive `fichiers-de-travail-contre-lecture-4B-partie2-v1.tar`, sha256 `3f2b65649c78c15a64bc3e512a830dc64951796da5497c893e525401d8a51ec0`, extraite dans un sous-dossier neuf de mon dossier de travail. J'y ai lu le journal ; le reste est conservé tel quel. Empreintes vérifiées le 14 novembre 2026 à 00:25:08 UTC.
- **Date et heures (`date -u`)** : session v1 commencée le 14 novembre 2026 à 00:04:22 UTC ; reprise v2 commencée à 00:25:08 UTC ; rédaction de la v2 commencée à 00:26:43 UTC.
- **Consigne** : `consigne-lecteur-compte-2-v1.md`, sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5`, revérifiée ; tous ses interdits sont tenus.
- **Empreintes des PDF (conformes à leurs compagnons `.sha256`)** : `2608.08975v1.pdf` (63 p.) `cea31a07b3d124be3cb87c6193feaee8924f167a9ae3f8d2cb9ba29995924d01` ; `2611.10791v1.pdf` (38 p.) `5465764cf2de6501d7256d712d0bd9cd11fbf93a700dce02d5c900e3527ab4ac`.
- **Fichiers du dépôt lus** :
  - v1 : `docs/decisions/decision-N-065-v1.md` l. 1-29 ; `docs/decisions/decision-N-067-v1.md` titres, puis l. 9-26 et 35-93 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` l. 464-522 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` l. 607-634 ;
  - v2 : la contre-lecture en entier (81 lignes). Rien d'autre.
- **Étendue lue** :
  - v1 : les deux PDF en entier, ligne à ligne ; pages 2-3 de 2608.08975 et page 2 de 2611.10791 vues aussi en image.
  - v2, pages relues à la demande du contre-lecteur :
    - 2608.08975 : p. 5-8, 12, 22, 24, 30 (texte) ; p. 22, 47, 48, 49, 50 et 54 en image (tableaux 10, 11, 30 à 36, 40) ;
    - 2611.10791 : p. 3, 7, 9, 13, 19, 35, 37 (texte déjà extrait, relu sur les passages cités).
- **Citations contrôlées** : 105 extraits dans `citations-4B-partie2-v2.json` (archive v2), **0 échec**. Tout extrait anglais entre « » ci-dessous en est une entrée exacte (contrôle `verifier_guillemets.py`) ; les autres extraits entre guillemets sont en français.
- **Ouverture fautive, refus** : aucune.

## 0. Verdict

Les deux verdicts de la v1 sont inchangés ; la contre-lecture les confirme.

| objet | verdict (table fermée) |
|---|---|
| Bras génératif du rôle 1 : juge génératif de la recherche déplacé par une attaque, gain mesuré | **« occupé en partie »** (2608.08975) |
| Pièce propre du rôle 1 : juge statistique calculé hors des agents, gain continu, même attaque sur les deux juges, comparaison | **« non trouvé dans les pièces lues »**, pour ces deux pièces seulement |
| Énoncé du rôle 1, pris dans son ensemble, pour ces deux pièces | **« occupé en partie »** |

**Ce qui change par rapport à la v1 : la portée de ce qui est dit publié s'élargit sur trois points.**

1. **Constat A.** Dans 2608.08975, l'un des deux réécrivains est aussi l'un des cinq relecteurs cibles. Le bras « guidé par relecture » sert donc, pour ce réécrivain, la relecture du modèle même qui le jugera. Il est comparé à une réécriture en deux passes sans relecture. Ce contraste « avec et sans retour du juge » est publié sur un juge génératif, à titre descriptif, sans consigne de tromper.
2. **Constat B.** 2611.10791 pose sous forme de modèle la comparaison de deux sortes d'évaluation sous une même production tournée vers l'évaluateur, et en propose la mesure. C'est un **voisin formel** pour (c) et (f). Rien n'y est mesuré, et aucun évaluateur n'est statistique.
3. **Constat C.** La série par tours de 2608.08975 n'a ni bras opposé ni bras neutre. Elle ne sépare pas l'effet de la rhétorique de celui de la réécriture répétée.

Aucune pièce ne confronte un juge statistique, ni aucun juge non génératif, à l'attaque. Le constat M12 (contre-lecture du niveau 3) n'est pas levé par cette partie seule.

## 1. Suite donnée à la contre-lecture

| constat | gravité | décision | où | motif |
|---|---|---|---|---|
| A — double rôle d'un réécrivain, aussi relecteur cible, dans le bras guidé | majeur | corrigé | sections 2, 4, 6, 7 | Vérifié. Les réécrivains (p. 5) : « GPT-5.5 through the Codex CLI » ; les relecteurs (p. 8) : « GPT-5 mini (OpenAI, 2025), GPT-5.5 (OpenAI, 2026), or Sonnet 5 (Anthropic, 2026b) ». Le bras guidé (p. 7) : « obtains one standard review from the rewriting backbone model, and then rewrites the manuscript once more using that feedback ». Cellule du tableau 32 (p. 48, lue en image et contrôlée) : « GPT-5.5 119 5.387 5.319 −0.067 [-0.192,+0.057] −6.72 −0.025 [-0.166,+0.116] ». La v1 disait « le modèle de l'attaquant, pas la cible » : faux pour ce réécrivain. Je précise une limite que la contre-lecture ne relève pas : la relecture servie l'est sous la consigne standard ; dans les cellules à consigne stricte, le juge consulté n'est donc pas exactement la cible. |
| B — 2611.10791 pose en forme (c), (d), (f) et propose l'essai | majeur | corrigé | sections 3, 4, 6, 7 | Vérifié pour (c) et (f) : le coefficient central « is a difference in relative acceptance rewards across protocols » (p. 19) ; l'essai proposé passe « by comparing research strategies across review protocols » (p. 37) et par « Relative reward changes holding content and validity comparable » (tableau 5, p. 35). Ces deux composantes passent à « voisin formel ». Pour (d), je corrige moins loin que proposé : la valeur acceptée est continue dans les **parts de population** (part d'auteurs tournés vers l'acceptation, part d'évaluation par indices), pas dans l'**intensité d'une attaque** ; (d) passe donc à « voisin lointain », et non à « voisin formel ». |
| C — série par tours sans bras opposé ni neutre | majeur | corrigé | sections 2, 4, 6 | Vérifié : la garde à deux sens ne vaut que pour une dimension, « This bidirectional design separates directional sensitivity from score movement caused by rewriting itself. » (p. 5), alors que le flux joint n'applique que le sens positif, « The joint workflow combines the positive directions of all six rhetorical dimensions in one prompt » (p. 6), puis le réapplique tour après tour (p. 7). J'ajoute un témoin partiel, à une seule passe : la réécriture lexicale, quasi neutre en moyenne, « Lexical Negative 6.294 6.299 +0.003 » (tableau 12, p. 23). Il ne vaut pas pour les passes répétées. |
| D — portée trop large de la réserve sur la régression vers la moyenne | mineur | corrigé | section 2, réserves | Accepté : le biais vient du découpage par la note de départ, tirée une seule fois (« These profiles are descriptive and should not be interpreted as unbiased estimates of how baseline paper quality moderates rewriting effects. », p. 30). La moyenne appariée sur tous les articles n'a pas ce biais ; son défaut est l'absence de témoin neutre (C). |
| E — motif mal posé de la réserve sur l'audit de répétition | mineur | corrigé | section 2, réserves | Accepté. Les deux familles comparées sont des moyennes d'ensemble : « Twelve baseline-paired dimension-direction effects 0.995 0.993 0.040 0.098 » ; « Six contrasts between Positive and Negative conditions 0.996 0.943 0.025 0.044 » (p. 54, lu en image et contrôlé). Un Spearman de 0,943 sur six rangs vaut une seule inversion de deux rangs voisins : 1 − 6·2/(6·35) ≈ 0,943 (calcul). |
| F — instances non génératives omises (découpage par note humaine, contrôleur programmatique) | mineur | corrigé | section 2, table | Accepté. Les notes humaines découpent aussi les effets : « Rewrite effects neither systematically increase nor decrease with human rating » (p. 9). Un contrôleur par programme reçoit les mêmes réécritures : « Detected violations are returned to the rewriting agent for repair » (p. 6). C'est une porte de forme, pas un juge du mérite, et son taux de passage n'est pas rapporté. Le verdict (b) est inchangé. |
| G — section 5 de la v1 : « sans changement du fond » non établi | mineur | corrigé | section 6 | Accepté : la préservation n'est qu'une contrainte souple, « rather than enforcing strict sentence-level semantic equivalence » (p. 2), et le réécrivain « may change prose, captions, tables, and the presentation of some numerical and mathematical expressions » (p. 3). |
| H — voisins non listés ; 2611.10791 cite 2608.08975 | mineur | corrigé | sections 3, 8 | Vérifié : « How can rhetoric reward-hack AI reviewers? » (2611.10791, p. 15) et « Content-preserving rhetorical changes also move AI review scores (Li et al., 2026). » (p. 34). Les deux pièces ne sont pas deux témoins indépendants du bras génératif. Les voisins ajoutés sont listés en section 8. |
| I — composante (e) de 2611.10791 trop basse | mineur | corrigé | section 3 | Accepté : « These are strategies that humans and machines can both adopt » (p. 3). (e) passe à « voisin » ; aucun agent n'est exécuté. |
| J — deux modes de moyenne mêlés ; écart au tableau 8 | mineur | corrigé | section 2 | Corrigé pour le premier point : +0,624 (p. 12) est une moyenne des cinq relecteurs, que je recalcule sur le tableau 35 à 0,6236, puis 0,632 au tour 3 (calcul) ; +0,631 (tableau 33) est une moyenne par article. Les deux sont désormais nommés. **Le second point est rejeté** : le tableau 8 imprime bien −1,361 sur sa ligne d'ensemble, « Overall mean 6.296 4.934 -1.361 » (p. 14), à côté de −1,367 et −1,356 par réécrivain. La phrase de la v1 était juste. |

## 2. 2608.08975 — « How Can Rhetoric Reward-Hack AI Reviewers? »

**Venue imprimée** : prépublication arXiv v1, cs.CL, 10 août 2026.

**Ce qu'il fait.**
- **Corpus.** 120 soumissions anonymisées, tirées par tranches de note humaine (p. 5). Deux modèles réécrivains, utilisés comme agents sur les sources LaTeX complètes, modifient six dimensions rhétoriques dans deux sens. Au total : 4 080 réécritures, 4 200 manuscrits, 42 396 relectures valides (auteurs, tableau 1, p. 4). Dans les mots des auteurs : « Two LLM rewriters transform six rhetorical dimensions in opposing directions, and five LLM reviewers evaluate the resulting manuscripts under standard and strict protocols. » (p. 1).
- **Cadre déclaré** : « we investigate a potential form of reward hacking » (p. 1).
- **Préservation du contenu.** Elle n'est qu'une contrainte souple, « under soft constraints to preserve the underlying methods, experimental settings, reported values and comparisons » (p. 5), « rather than enforcing strict sentence-level semantic equivalence » (p. 2). Un contrôleur programmatique ne vérifie que des ancres de structure, et ses refus reviennent à l'attaquant (p. 6).
- **Double rôle (constat A).** L'un des réécrivains est aussi l'un des cinq relecteurs (p. 5, 8). Les relecteurs ignorent la condition : « Reviewers are not told the rewrite condition or rewrite model. » (p. 8). Il existe donc aussi, dans l'étude à une dimension, des cellules où un modèle note les réécritures qu'il a lui-même produites. Les auteurs ne les isolent pas.
- **Mesure.** Variation appariée de la note globale ; probabilité d'acceptation faible (note d'au moins 6) : « We define weak-accept probability as the share of evaluations assigning an overall rating of 6 or higher. » (p. 8). Les intervalles viennent d'un rééchantillonnage par article, « without applying a separate multiple-testing threshold to classify effects » (p. 9).
- **Deux consignes de relecture.** La stricte « The strict prompt additionally requires concrete evidence for high ratings and instructs the reviewer not to reward presentation unless it changes the scientific assessment. » (p. 8).

**Chiffres (nature : auteurs, sauf mention).**

*Effets par dimension.*
- Gain maximal : « positive evidence framing raises Overall Assessments (OA) by up to 0.93 » (p. 3), concordant avec +0,933 au tableau 3 (p. 6).
- Écarts entre les deux sens : « positive-negative contrasts of 13.0 percentage points for evidence framing, 12.0 for novelty stance, and 9.0 for scope framing » (p. 9). Recalcul sur le tableau 16 (p. 26) : +6,9 et −6,1, +4,8 et −7,2, +3,0 et −6,0 (calcul, concordant).

*Profondeur de réécriture (sens positif seulement, sans témoin : constat C).*
- Le flux joint : « The joint workflow combines the positive directions of all six rhetorical dimensions in one prompt » (p. 6). Il est réappliqué : « Round 1 rewrites the anonymized original, while each subsequent round rewrites the output of the preceding round using the same prompt and preservation requirements. » (p. 7).
- Pour le réécrivain qui répond, en **moyenne des cinq relecteurs** : « the reviewer-averaged gain rises from +0.289 to +0.410 under standard and from +0.463 to +0.624 under strict » (p. 12). Le tour 3 strict vaut 0,632 sur le tableau 35 (calcul).
- En **moyenne par article** : « Strict 4.921 5.388 5.541 5.552 +0.631 » (tableau 33, p. 49).
- En acceptation faible : « Strict 31.50% 42.88% 47.39% 48.40% +16.90 pp », mais recul au tour 3 sous consigne standard : « Standard 74.08% 80.67% 81.68% 80.84% +6.76 pp » (tableau 34, p. 49).
- Non-monotonie par relecteur : « +0.458 +0.647 +0.622 » (tableau 35, p. 49) ; « Some continue to increase across rounds, while others flatten or partially reverse earlier gains. » (p. 12) ; « The third round adds little further improvement. » (p. 12).
- Témoin partiel à une seule passe : la réécriture lexicale ne bouge presque pas la note, « Lexical Negative 6.294 6.299 +0.003 » (tableau 12, p. 23).

*Retour du juge (constat A).*
- Contraste descriptif entre le bras guidé et deux passes sans relecture. Les auteurs : « Because the workflows begin from independently generated first-pass rewrites, this comparison is descriptive rather than a causal estimate of feedback. » (p. 12) ; « the two pipelines are therefore not treated as matched causal treatments » (p. 47).
- Résultat d'ensemble : « Guided rewriting performs slightly worse than an unguided second pass in all four rewriter-prompt averages » (p. 12).
- Cellule où le modèle consulté est aussi la cible (consigne standard) : « GPT-5.5 119 5.387 5.319 −0.067 [-0.192,+0.057] −6.72 −0.025 [-0.166,+0.116] » (tableau 32, p. 48). Le retour du juge cible n'y apporte rien de mesurable.

*Défense par consigne.*
- « Mean OA decreases from 6.296 to 4.934 » ; ligne d'ensemble du tableau 8 : « Overall mean 6.296 4.934 -1.361 » (p. 14).
- La sensibilité, elle, reste : « the mean cross-protocol Spearman correlation in paper-level rewrite effects is only .081 » ; « Stricter prompting, therefore, changes reviewer severity without making the review more invariant to content-preserving rhetoric. » (p. 14).

*Sources non génératives (constat F).*
- Notes humaines officielles, « Human OA is the mean of the official ICLR review scores for each paper » (p. 22), **sur les originaux seulement**. Elles servent à l'échantillonnage (p. 5), à une comparaison descriptive, « As an external descriptive comparison, we contrast each AI reviewer's rating of the anonymized original with the paper's mean overall assessment (OA) from the official ICLR reviews. » (p. 22 ; Spearman de 0,395 à 0,621), et au découpage des effets (p. 7, 9, 11, 28).
- Contrôleur programmatique des ancres de structure (p. 6).
- Aucune vérité sur le mérite des versions réécrites : « these score changes are treated as reviewer-response spillovers rather than independently verified changes in scientific merit » (p. 24).

**Ce qu'il ne fait pas.**
- Aucun juge statistique, exécutable ou oracle confronté à la réécriture.
- Aucune comparaison entre deux sortes de juges : il compare des relecteurs génératifs entre eux et des consignes entre elles.
- Pas d'attaquant qui produit de la recherche ; pas de consigne de tromper.
- Pas de juge-tournoi par paires, alors que c'est la forme visée par N-065.
- Pas de témoin neutre dans la série par tours.

**Limites reconnues.** Une seule conférence ; données manquantes possiblement non aléatoires ; dimensions non orthogonales ; « Finally, most configurations use one AI review per manuscript, with repeated reviews examined only in an auxiliary audit. » (p. 15) ; « We therefore caution against interpreting score increases as improvements in scientific merit » (p. 15).

**Réserves (R4), corrigées selon D et E.**
- **Régression vers la moyenne.** Un gain d'attaque **découpé selon la note de départ du même juge** est biaisé par la régression vers la moyenne, puisque cette note vient d'un seul tirage. Les auteurs le reconnaissent : « This descriptive pattern may partly reflect scale bounds and regression to the mean » (p. 10). Même la réécriture « négative » fait monter les notes basses : « [1,3] Novelty Negative 2.967 3.654 +0.688 0.688 » (tableau 25, p. 32). Le gain moyen apparié sur tous les articles n'a pas ce biais, mais il demande un témoin de réécriture neutre (constat C).
- **Audit de répétition.** Il compare des moyennes d'ensemble (douze effets, six contrastes) pour un seul relecteur : « Agreement between single-review and three-review-mean GPT-5 mini estimands. » (p. 54). Il n'établit ni la stabilité d'une note par manuscrit, ni celle des découpages par note de départ, ni celle des quatre autres relecteurs.
- **Double rôle (A).** Des cellules d'auto-évaluation existent (même modèle réécrivain et relecteur), sans analyse séparée.
- **Regroupement mineur.** Le tableau 4 (p. 7) affiche quatre tranches de note humaine, alors que l'échantillonnage en a six, semi-ouvertes (p. 5) : ambiguïté de regroupement.

## 3. 2611.10791 — « Winning Reviews, Losing Discovery? »

**Venue imprimée** : arXiv v1, cs.GT, 7 novembre 2026 ; « Winning Reviews, Losing Discovery? Working manuscript » (p. 1) ; sous-titre « The Co-Evolutionary Game of AI Research and Peer Review » (p. 1).

**Ce qu'il fait.**
- **Le modèle.** Un jeu de réplicateur à deux populations : des auteurs (recherche orientée vers l'acceptation ou exploratoire) et des évaluations (par indices bon marché ou soigneuses). Ses stratégies valent pour les humains comme pour les machines : « These are strategies that humans and machines can both adopt » (p. 3).
- **Le mécanisme posé** : « production adapts to the evaluator's weaknesses, and evaluation becomes cheaper without becoming more discriminating » (p. 3). C'est le canal « through which automated production can exploit automated evaluation » (p. 4).
- **Le coefficient central** de l'écart de récompense entre les deux protocoles d'évaluation, sous une même stratégie de production, « is a difference in relative acceptance rewards across protocols » (p. 19).
- **La valeur.** La valeur acceptée est une fonction continue des deux parts (équations 12-13, p. 7 ; lu sur le PDF, non contrôlé par programme). La valeur scientifique doit venir d'ailleurs que des notes : « Detecting that decline requires independent assessment of contribution » (p. 7).
- **Le statut des chiffres.** Ils sont illustratifs : « Parameters are illustrative » (p. 9) ; « The numerical study uses declared illustrative inputs. » (p. 5). Exemple : « accepted value falls from 0.65 in the careful regime to 0.39 in the proxy regime, a 40% loss despite identical publication frequency » (p. 10).

**Mesures proposées, non faites (constat B).**
- La mesure de l'interaction entre protocoles passe « by comparing research strategies across review protocols » (p. 37) ; « A useful design would combine controlled presentation changes with independently assessed research characteristics and reviewer effort measurements. » (p. 37).
- Mesure manquante au tableau 5 : « Relative reward changes holding content and validity comparable » (p. 35).
- Comité d'agents audité : « the institution would measure responses to controlled changes in affiliation, wording, and research topic against independent expert and artifact-based assessments » (p. 13).
- Mesure de la valeur : « For some computational claims, held-out performance, independent replication, proof verification, or discovery in a hidden environment can provide a useful outcome. » (p. 37) ; « A direct empirical test would jointly measure the protocol interaction, workload response, and independently assessed scientific contribution. » (p. 35).

**Juge non génératif ?** Le levier d'audit soigneux imposé de l'extérieur, « receive externally resourced careful assessment that determines the outcome for those opportunities » (p. 8), est un second type d'évaluateur, mais abstrait, jamais attaqué et sans statistique. La prédiction par les pairs y est citée comme règle de score dont la limite est dite : « it does not remove collusion or uninformative equilibria automatically » (p. 13).

**L'écart entre la note et la découverte réelle : non mesuré.** Il est posé par des valeurs v_i choisies à la main (v_A = 0,6 ou 1,2 ; v_T = 1 ; lu sur le PDF, p. 9-10). La mesure indépendante est réclamée, « Independent validation with a stated horizon and unit » (tableau 5, p. 35), et proposée (p. 37), mais jamais faite.

**Hors du modèle** : « In particular, strategic evasion, persistent scholarly records, and training future systems on generated material are outside the baseline dynamics. » (p. 36).

**Dépendance entre pièces (constat H).** 2611.10791 s'appuie sur 2608.08975 pour le canal de la présentation : « How can rhetoric reward-hack AI reviewers? » (p. 15) ; « Content-preserving rhetorical changes also move AI review scores (Li et al., 2026). » (p. 34). Les chiffres de tiers qu'il relaie ne sont pas opposables (R7) : jusqu'à 82 % d'acceptation de faux articles, « this is an AI-review outcome, not an observed conference acceptance rate » (p. 34) ; 53,7 % puis 81,5 % d'exactitude d'un audit (p. 2).

**Réserves.** Aucune incohérence trouvée ; « All 5,043 numerical classifications agree with the analytical boundary. » (p. 10) est une vérification déterministe attendue. Les architectures de réforme sont dites des propositions : « The architectures remain proposals: binary strategies and illustrative parameters do not predict their performance at a particular venue. » (p. 14).

## 4. Table composante × article (mise à jour)

| composante | 2608.08975 | 2611.10791 |
|---|---|---|
| (a) juge génératif de la recherche trompé ou déplacé | **occupée en partie** : relecteurs d'articles déplacés par réécriture rhétorique ; articles humains, fond préservé sous contrainte souple, non vérifié (p. 1, 2, 8, 9, 12, 14, 24) | **voisin** : évaluation par indices, modélisée, non mesurée (p. 3, 5) |
| (b) juge statistique hors des agents | **ne touche pas** ; deux instances non génératives, aucune confrontée à l'attaque : notes humaines sur les seuls originaux (p. 5, 7, 9, 22) ; contrôleur programmatique de forme (p. 6) | **ne touche pas** ; voisin conceptuel : audit soigneux imposé, sans attaque ni statistique (p. 8) |
| (c) même attaque sur les deux sortes de juges | **ne touche pas** ; voisin : même réécriture sur cinq juges génératifs et deux consignes (p. 1, 14) | **voisin formel** : écart de récompense d'une même production entre deux protocoles d'évaluation, coefficient central du modèle (p. 19) ; essai proposé, non fait (p. 13, 35, 37) ; aucun évaluateur statistique |
| (d) gain continu en fonction de l'intensité de l'attaque | **occupée en partie, pour le juge génératif seul, sans témoin** : écart continu de note à une et six dimensions et à un, deux, trois tours de la même consigne jointe (sens positif seul) ; rendement décroissant, recul au tour 3 dans certaines cellules ; rhétorique et réécriture répétée non séparées (p. 5-7, 12, 49) | **voisin lointain** : la valeur et la récompense sont continues dans les parts de population, pas dans l'intensité d'une attaque (p. 5, 7, 19) |
| (e) attaquant agent de recherche (proposeur) | **voisin, occupée en partie pour le contraste avec et sans retour du juge** : agents réécrivains (ni proposeurs, ni chargés de tromper) ; un bras reçoit une relecture standard avant la dernière réécriture, comparé à deux passes sans relecture ; pour un réécrivain, le modèle consulté est aussi un relecteur cible ; comparaison descriptive ; le bras guidé ne fait pas mieux (p. 5, 7, 8, 12, 47, 48) | **voisin** : stratégie de population ouverte aux machines, motivée par les systèmes de recherche autonomes ; aucun agent exécuté (p. 1-3) |
| (f) comparaison de la corruptibilité de deux sortes de juges | **ne touche pas** ; voisin : comparaison entre relecteurs génératifs et entre consignes (p. 13-14) | **voisin formel** : comparaison posée en modèle et proposée en essai, non mesurée, sans juge statistique (p. 13, 19, 35, 37) |
| écart entre la note du juge et la découverte réelle | non mesuré (aucune vérité sur le mérite, p. 24) | **non mesuré** : valeurs choisies à la main (p. 9-10) ; mesure réclamée et proposée (p. 7, 35, 37) |

## 5. Ce qui reste revendicable (dans ces deux pièces)

Non trouvé dans les deux pièces lues : « La mesure, sous **une même attaque** portée par un proposeur modèle de langue, du **gain de l'attaque**, fonction continue de son intensité et rapporté à un témoin sans attaque, **sur un juge statistique calculé hors des agents** et **sur un juge génératif** de la recherche automatisée, et la **comparaison mesurée** de ces deux gains. »

Ce qui en est retiré ou qualifié par la v2 :
- la comparaison de deux sortes d'évaluation sous une même production tournée vers l'évaluateur est **posée en modèle et proposée** par 2611.10791 (p. 19, 35, 37). Seules **la mesure** de cette comparaison et **la présence d'un juge statistique** restent non trouvées ;
- le contraste « l'attaquant reçoit ou non le retour du juge » est **publié sur un juge génératif**, à titre descriptif (2608.08975, p. 7, 12, 48). Il n'est pas revendicable de ce côté-là.

Le verdict vaut pour ces deux pièces, pas pour le champ ; il est conditionnel au rendu des quatre autres pièces du lot.

## 6. Ce qu'une phrase publique sur l'énoncé ne doit pas affirmer

- Que le déplacement d'un relecteur modèle par une réécriture rhétorique **sous consigne de préserver le fond, préservation non vérifiée de façon indépendante**, est une découverte du programme : c'est publié et chiffré (2608.08975, p. 1, 9, 12).
- Qu'aucun gain gradué n'est publié sur un juge génératif : c'est publié à plusieurs profondeurs de réécriture (p. 12, 49). À l'inverse, que 2608.08975 établit une relation dose-réponse : sa série par tours n'a pas de témoin neutre ni opposé (p. 5-7).
- Que comparer un attaquant qui reçoit les relectures du juge à un attaquant qui ne les reçoit pas est neuf sur un juge génératif (2608.08975, p. 7, 12, 48).
- Que comparer la sensibilité de deux sortes d'évaluateurs à une même production tournée vers l'évaluateur est une idée sans précédent : elle est posée en modèle et proposée comme essai (2611.10791, p. 19, 35, 37).
- Que prendre une découverte dans un environnement caché comme mesure de la valeur, face à la note d'un juge, est une idée sans précédent : elle est proposée, non faite (2611.10791, p. 37).
- Qu'une consigne de relecture plus stricte suffit à défendre un juge génératif : contredit (2608.08975, p. 14).
- Que la boucle « production adaptée à l'évaluateur » est un cadre neuf (2611.10791, p. 3-4, et les synthèses qu'il cite).
- Que 2611.10791 apporte une preuve empirique de perte de découverte : ses paramètres sont illustratifs (p. 5, 9, 14).
- Que 2608.08975 et 2611.10791 sont deux témoins indépendants du bras génératif : le second s'appuie sur le premier (p. 15, 34).
- Quoi que ce soit sur l'absence d'optimisation répétée ou d'attaque adaptative contre des juges de la recherche, tant que 2606.10159 et 2605.26156 ne sont pas lues sur PDF. De même, rien sur l'absence d'un modèle de l'écart entre la note et la valeur latente, tant que 2601.16909 n'est pas lue : « Their model links verification capacity and proxy noise to the correlation between evaluation scores and latent scientific value. » (2611.10791, p. 36).
- Que la pièce propre est « libre » : elle est seulement « non trouvée dans les pièces lues ».

## 7. Note hors mandat (signalée, non tranchée)

Le contraste de 2608.08975 (un bras reçoit le retour d'un juge qui est aussi la cible, l'autre non ; p. 7, 48) est voisin, **côté juge génératif**, de la forme resserrée de O12 (N-067, section 4, point 3). Cette forme porte sur un juge statistique, avec consigne de tromper et sur des mondes où toute promotion est fausse : rien de cela n'est dans la pièce. Ce n'est pas une collision avec O12. C'est un voisin à citer si O12 s'énonce aussi pour un juge génératif.

## 8. Voisins nommés dans les pièces et non lus

**Priorité haute** :
- Li, Zhang, Davies, Qiu, Gal 2026, « Gaming ai-assisted peer reviews poses new risks to the scientific community. » (arXiv 2606.10159 ; 2608.08975, p. 17). Elle est décrite ainsi : « repeated optimization of paraphrasing, rewriting, and overclaiming can substantially increase AI-review scores » (p. 20). Optimisation répétée, donc une dose.
- Yang et al. 2026a, « Turning bias into bugs: Bandit-guided style manipulation attacks on llm judges. » (arXiv 2605.26156 ; p. 18) : « stylistic edits inflate a particular judge's scores, including in a case study where generated review texts are themselves evaluated outputs » (p. 19). Attaquant qui s'adapte au juge.
- Luo, Kasirzadeh, Shah 2026, « The more you automate, the less you see: Hidden pitfalls of autonomous AI scientists. » (2611.10791, p. 15). C'est un auditeur comparé sous deux régimes d'information : « In its constructed audit dataset, manuscript-only detection accuracy was 53.7%, rising to 81.5% when the auditor received workflow artifacts. » (p. 2 ; chiffres non opposables avant lecture).
- You, Cao, Gurevych 2026, « Preventing the collapse of peer review requires verification-first AI. » (arXiv 2601.16909 ; 2611.10791, p. 16). Le texte le présente ainsi : « The closest theoretical comparison is You et al. (2026). » (p. 36).

**Priorité moyenne** :
- Bhat et Varma 2026, « All prompts are created equal? evaluating robustness of llm judges against non-adversarial prompt variations. » (2608.08975, p. 16). Robustesse d'un juge selon que l'attribut jugé est vérifiable : « with stability depending more on the verifiability of the evaluated attribute than on model scale » (p. 19). Voisin de la comparaison de deux sortes de juges.
- Miller, Resnick, Zeckhauser 2005, « Eliciting informative feedback: The peer-prediction method. » (2611.10791, p. 15) : une règle de score statistique dont la corruption par collusion est dite (p. 13).
- Wang et al. 2026, « The emerging AI paper-review arms race: Adversarial co-evolution in scholarly publishing. » (arXiv 2609.07713 ; 2611.10791, p. 15) ; « Existing work examines verification incentives (You et al., 2026) and the wider production-evaluation arms race (Wang et al., 2026) » (p. 3).

**Autres** :
- Dans 2608.08975 : Kaneko 2026, « Paraphrasing adversarial attack on llm-as-a-reviewer. » (arXiv 2601.06884 ; p. 16) ; Baumann et al. 2026 (arXiv 2605.03202 ; « Baumann et al. (2026) uses paper laundering to describe automated rewriting intended to raise AI-review scores without new experiments. », p. 20) ; Dycke et Gurevych 2026, « Automatic reviewers fail to detect faulty reasoning in research papers: A new counterfactual evaluation framework. » (p. 16) ; Lee et al. 2025, « Are llm-judges robust to expressions of uncertainty? » (p. 17) ; Zhu et al. 2025, « When your reviewer is an llm: Biases, divergence, and prompt injection risks in peer review. » (arXiv 2509.09912 ; p. 18) ; Vasu et al. 2026, « Justice in judgment: Unveiling (hidden) bias in llm-assisted peer reviews. » (p. 17) ; Collu et al. 2026, Lin et al. 2025, Ye et al. 2024 (arXiv 2412.01708), Du 2025 (p. 16-18).
- Dans 2611.10791 : Dreber et al. 2015, « Using prediction markets to estimate the reproducibility of scientific research. » (p. 14) ; Yang, Liu, Xu 2026, SciIntegrity-Bench (arXiv 2605.10246) ; Sharma et al. 2026 (arXiv 2601.20920) ; Kim et al. 2026 (arXiv 2609.19420) ; Beel et al. 2025 (arXiv 2502.14297) (p. 14-16).
- Pièces lues par l'autre session, nommées ici : Jiang et al. 2026, « BadScientist: Can a research agent write convincing but unsound papers that fool LLM reviewers? » (2611.10791, p. 15) ; « Yang et al. (2026b) similarly introduces adversarial repackaging, a closed-loop procedure that searches for favorable presentation strategies » (2608.08975, p. 20 ; arXiv 2606.13044).

## 9. Réserves du lecteur

- **R8.** La composante non trouvée est séduisante, puisque c'est l'apport du papier C sur ce terrain. Elle n'a été cherchée que dans deux pièces, dont aucune ne relève des essais statistiques ni de la validation d'hypothèses. Ce « non trouvé » pèse peu.
- **Profondeur.** La contre-lecture juge ma v1 juste sur la lettre et rapide sur le montage ; j'en accepte le fond (A, B, C). La v2 relit les pages qu'elle désigne. J'ai écarté une partie de deux constats, B pour (d) et J pour le tableau 8, page et citation à l'appui.
- La littérature des juges statistiques attaqués (tests adaptatifs, Dwork et al. 2015, Ladder, déjà cités par N-064 dans leur forme) relève d'autres lots.
