# Lot 4-B, partie 2 sur 2 — rôle 1 de N-065 (second terrain du papier C) — rapport du lecteur (v1)

- **Date et heures (relevées par `date -u`)** : début de session le 14 novembre 2026 à 00:04:22 UTC ; reprise après redémarrage du conteneur relevée à 00:12:04 UTC ; rédaction du rapport commencée à 00:12:30 UTC.
- **Rôle et modèle** : lecteur, modèle A. Je n'ai écrit ni le programme, ni les décisions, ni aucun rapport antérieur.
- **Consigne** : `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` ; interdits communs v2 lus aussi ; le plus strict tenu (aucune commande git).
- **Empreintes des PDF (conformes à leurs compagnons `.sha256`)** :
  - `2608.08975v1.pdf` (63 p.) : `cea31a07b3d124be3cb87c6193feaee8924f167a9ae3f8d2cb9ba29995924d01` ;
  - `2611.10791v1.pdf` (38 p.) : `5465764cf2de6501d7256d712d0bd9cd11fbf93a700dce02d5c900e3527ab4ac`.
- **Fichiers du dépôt lus, et lignes** : `docs/decisions/decision-N-065-v1.md` l. 1-29 ; `docs/decisions/decision-N-067-v1.md` titres (`grep -n '^#'`), puis sections 0, 2, 3, 4, 5 (l. 9-26, 35-93 : ces sections ne sont pas découpées par revendication et portent ensemble O2, O4, le nul des lois connues et d'autres revendications) ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` l. 464-522 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` l. 607-634. Aucun autre fichier du dépôt. Les quatre autres pièces du lot n'ont pas été ouvertes.
- **Étendue lue** : `2611.10791v1` p. 1-38 ligne à ligne (page 2 vue aussi en image) ; `2608.08975v1` p. 1-63 ligne à ligne (pages 2 et 3 vues aussi en image ; les tableaux de décomposition des p. 37-46 d'abord parcourus par en-têtes, puis lus ligne à ligne après la reprise). Détail dans le journal de l'archive.
- **Citations contrôlées** : 64 extraits, **0 échec** (script `verifier_citations.py`, testé d'abord sur un cas juste et sur deux cas altérés). Tout extrait anglais entre « » ci-dessous figure tel quel dans `citations-4B-partie2-v1.json` (archive). Un second script (`verifier_guillemets.py`) a vérifié que chaque extrait anglais entre guillemets du rapport est une entrée exacte du JSON ; les extraits restants entre guillemets sont en français (termes de l'énoncé).
- **Ouverture fautive, refus** : aucune.

## 0. Verdict

**Ni l'une ni l'autre pièce ne confronte un juge statistique, ni aucun juge non génératif, à l'attaque.** La composante qui définit la « pièce propre » du rôle 1 (même attaque portée sur un juge statistique et sur un juge génératif, gain continu, comparaison) n'est **pas trouvée dans ces deux pièces**.

- **2608.08975** (« How Can Rhetoric Reward-Hack AI Reviewers? ») **occupe en partie** le bras du juge génératif : relecteurs modèles déplacés par une réécriture rhétorique, gain mesuré en écart continu de note, dans deux sens, à plusieurs intensités discrètes (une dimension, six dimensions réunies, un à trois tours). Il ne touche ni le juge statistique, ni la comparaison entre deux sortes de juges.
- **2611.10791** (« Winning Reviews, Losing Discovery? ») est un **modèle théorique** (jeu évolutionnaire à deux populations), sans juge réel, sans attaque exécutée, avec des paramètres déclarés illustratifs. Pour le rôle 1, c'est un **voisin conceptuel** : il distingue une évaluation par indices bon marché d'une évaluation soigneuse, et une valeur scientifique « évaluée indépendamment ». **L'écart entre la note du relecteur et la découverte réelle n'est pas mesuré** : il est posé par hypothèse, avec des valeurs choisies.

**Verdict d'ensemble pour l'énoncé (rôle 1, dans les deux pièces lues), table fermée : « occupé en partie ».** La partie occupée est le bras génératif et sa mesure graduée (2608.08975). La pièce propre, elle, est **« non trouvée dans les pièces lues »**, pour ces deux pièces seulement. Le constat M12 n'est pas levé tant que l'autre session n'a pas rendu ses quatre pièces.

## 1. Énoncé confronté et composantes

N-065, point 1 (l. 15-18) : l'organisme d'idéation est un second terrain du papier C ; son juge statistique est un moniteur d'affirmations de recherche ; l'attaque de Goodhart (A1-v4) et un juge-tournoi façon Co-Scientist (juge génératif sous la même attaque) « mesurent la corruptibilité de deux sortes de juges ». État de l'art du niveau 3 (l. 503-510) : prémisse du bras génératif occupée en partie (2611.04556, 2611.00643) ; la pièce propre y est dite libre, ce que M12 conteste faute du lot 4-B (contre-lecture, l. 607-634). Composantes du mandat : (a) juge génératif trompé ; (b) juge statistique hors des agents trompé ou éprouvé ; (c) même attaque sur les deux ; (d) gain continu en fonction de l'intensité ; (e) attaquant agent de recherche (proposeur) ; (f) comparaison de la corruptibilité des deux juges.

## 2. 2608.08975 — « How Can Rhetoric Reward-Hack AI Reviewers? »

**Venue imprimée** : prépublication arXiv v1, cs.CL, 10 août 2026 ; pas de venue évaluée par des pairs indiquée.

**Ce qu'il fait.**
- Corpus de 120 soumissions à une conférence d'apprentissage (2026), anonymisées, 20 par tranche de note humaine moyenne (p. 5). Deux modèles réécrivains, utilisés comme agents de code sur les sources LaTeX complètes, transforment six dimensions rhétoriques dans deux sens opposés ; 4 080 réécritures, 4 200 manuscrits au total, 42 396 relectures valides (auteurs, tableau 1, p. 4). Ce qu'en dit le résumé : « Two LLM rewriters transform six rhetorical dimensions in opposing directions, and five LLM reviewers evaluate the resulting manuscripts under standard and strict protocols. » (p. 1).
- Cadre déclaré : « we investigate a potential form of reward hacking » (p. 1). La préservation du contenu n'est imposée que par la consigne et par des contrôles programmatiques d'ancres de structure (clés de citation, étiquettes, chemins), « under soft constraints to preserve the underlying methods, experimental settings, reported values and comparisons » (p. 5).
- Mesure : variation appariée de la note globale (échelle 1-10) par rapport à l'original, pour le même article, le même relecteur et la même consigne ; probabilité d'acceptation faible (note d'au moins 6) : « We define weak-accept probability as the share of evaluations assigning an overall rating of 6 or higher. » (p. 8). Intervalles par rééchantillonnage des articles (5 000 tirages), « without applying a separate multiple-testing threshold to classify effects » (p. 9).
- Deux protocoles de relecture : standard et strict. Le strict « The strict prompt additionally requires concrete evidence for high ratings and instructs the reviewer not to reward presentation unless it changes the scientific assessment. » (p. 8).

**Chiffres principaux (nature : auteurs, sauf mention).**
- Effets par dimension : le cadrage de la preuve monte la note d'au plus +0,93 (« positive evidence framing raises Overall Assessments (OA) by up to 0.93 », p. 3) ; écarts positif-négatif sur la probabilité d'acceptation faible : « positive-negative contrasts of 13.0 percentage points for evidence framing, 12.0 for novelty stance, and 9.0 for scope framing » (p. 9). Recalcul sur le tableau 16 (p. 26, ligne de moyenne générale) : preuve +6,9 et −6,1, soit 13,0 ; nouveauté +4,8 et −7,2, soit 12,0 ; portée +3,0 et −6,0, soit 9,0 (calcul, concordant).
- Intensité (réécritures en plusieurs tours, p. 12 et tableaux 33-34, p. 49) : pour le réécrivain le plus efficace, gain moyen de note « the reviewer-averaged gain rises from +0.289 to +0.410 under standard and from +0.463 to +0.624 under strict » (p. 12) ; au troisième tour, consigne stricte : « Strict 4.921 5.388 5.541 5.552 +0.631 » (tableau 33, p. 49) et, en probabilité d'acceptation faible, « Strict 31.50% 42.88% 47.39% 48.40% +16.90 pp » (tableau 34, p. 49). Rendement décroissant : « The third round adds little further improvement. » (p. 12) ; non monotone selon le relecteur : « Some continue to increase across rounds, while others flatten or partially reverse earlier gains. » (p. 12).
- Rétroaction d'un juge : bras « guidé par relecture », où le réécrivain reçoit la relecture de son propre modèle de base, puis réécrit : « obtains one standard review from the rewriting backbone model, and then rewrites the manuscript once more using that feedback » (p. 7). Résultat : « Guided rewriting performs slightly worse than an unguided second pass in all four rewriter-prompt averages » (p. 12), comparaison dite descriptive par les auteurs (p. 12, p. 47).
- Défense par consigne : « Mean OA decreases from 6.296 to 4.934 » (p. 14), mais la sensibilité ne change pas : « the mean cross-protocol Spearman correlation in paper-level rewrite effects is only .081 » et « Stricter prompting, therefore, changes reviewer severity without making the review more invariant to content-preserving rhetoric. » (p. 14).
- Seule confrontation à une source non générative : notes humaines officielles, **sur les originaux seulement**, jamais sur les réécritures : « As an external descriptive comparison, we contrast each AI reviewer's rating of the anonymized original with the paper's mean overall assessment (OA) from the official ICLR reviews. » (p. 22, tableau 11 ; corrélations de Spearman de 0,395 à 0,621, auteurs).

**Ce qu'il ne fait pas.** Aucun juge statistique, exécutable ou oracle ; aucune vérité terrain sur le mérite des versions réécrites : « these score changes are treated as reviewer-response spillovers rather than independently verified changes in scientific merit » (p. 24). Aucune comparaison entre deux sortes de juges : cinq relecteurs génératifs et deux consignes, tous génératifs. L'attaquant ne produit aucune recherche : il réécrit des articles humains, sous la consigne de préserver le contenu, et non sous la consigne de tromper. Le juge est un relecteur par notes ponctuelles, pas un juge-tournoi par comparaisons de paires comme celui que vise N-065.

**Limites reconnues.** Une seule conférence ; données manquantes possiblement non aléatoires ; dimensions non orthogonales ; « Finally, most configurations use one AI review per manuscript, with repeated reviews examined only in an auxiliary audit. » (p. 15) ; mise en garde : « We therefore caution against interpreting score increases as improvements in scientific merit » (p. 15).

**Incohérences internes et réserves (R4).**
- Le mouvement selon la note de départ est confondu avec la régression vers la moyenne, ce que les auteurs reconnaissent : « This descriptive pattern may partly reflect scale bounds and regression to the mean » (p. 10). Même la réécriture dans le sens « négatif » fait monter les notes basses : « [1,3] Novelty Negative 2.967 3.654 +0.688 0.688 » (tableau 25, p. 32). Un gain d'attaque mesuré comme une simple hausse de note est donc biaisé sans témoin de réécriture neutre ou opposée. C'est une leçon de méthode pour le bras génératif du rôle 1, pas une collision.
- L'audit de stabilité (trois relectures contre une) est presque parfait (r = 0,995), mais il ne porte que sur un seul relecteur : « Agreement between single-review and three-review-mean GPT-5 mini estimands. » (tableau 40, p. 54). Le résultat est trop propre pour être généralisé aux quatre autres relecteurs : réserve.
- Tableau 4 (p. 7) : quatre tranches de note humaine ([1,3], [4,5], [6,7], [8,10]) alors que l'échantillonnage en compte six, semi-ouvertes (p. 5). Les moyennes comprises entre 3 et 4, ou entre 5 et 6, n'ont pas de tranche visible. C'est une ambiguïté de regroupement, mineure.
- Contrôles de cohérence faits : +0,93 annoncé p. 3 = +0,933 du tableau 3 (p. 6) ; −1,36 (résumé) = −1,361 du tableau 8 (p. 14) (calcul, concordants).

**Verdicts par composante.**

| composante | verdict | appui |
|---|---|---|
| (a) juge génératif de la recherche trompé ou déplacé | **occupée en partie** (relecteur d'articles et non juge de la recherche automatisée ; la tromperie porte sur des articles humains réécrits) | p. 1, 8, 9, 12, 14 |
| (b) juge statistique hors des agents | **ne touche pas** | p. 22, 24 (seule source non générative : notes humaines sur les originaux) |
| (c) même attaque sur les deux sortes de juges | **ne touche pas** ; voisin : même attaque sur cinq juges génératifs et sur deux consignes | p. 1, 14 |
| (d) gain continu en fonction de l'intensité | **occupée en partie, pour le juge génératif seul** : gain continu de note mesuré à des intensités discrètes (une ou six dimensions ; tours 1 à 3), rendement décroissant, non monotone selon le relecteur ; aucun paramètre d'intensité continu | p. 12, 49 |
| (e) attaquant agent de recherche (proposeur) | **voisin** : agents réécrivains sur sources complètes, ni proposeurs ni chargés de tromper ; un bras reçoit la relecture d'un juge (le modèle de l'attaquant, pas la cible) | p. 5, 7 |
| (f) comparaison de la corruptibilité de deux sortes de juges | **ne touche pas** ; voisin : comparaison entre relecteurs et entre consignes, tous génératifs | p. 13-14 |

**Contre-indice pour la prédiction du bras génératif.** Le gain n'est pas une fonction lisse et croissante de l'intensité : « More elaborate workflows do not reliably yield larger gains. » (p. 1). Une prédiction chiffrée d'une dose-réponse monotone sur un juge génératif devrait en tenir compte.

## 3. 2611.10791 — « Winning Reviews, Losing Discovery? »

**Venue imprimée** : arXiv v1, cs.GT, 7 novembre 2026, en-tête « Winning Reviews, Losing Discovery? Working manuscript » (p. 1). Sous-titre : « The Co-Evolutionary Game of AI Research and Peer Review » (p. 1).

**Ce qu'il fait.** Il propose une dynamique de réplicateur à deux populations : des auteurs (recherche orientée vers l'acceptation ou recherche exploratoire) et des relecteurs (évaluation par indices bon marché ou évaluation soigneuse). Il en tire des conditions de bistabilité, une frontière de bassin analytique, des seuils d'intervention (audits soigneux imposés, récompense des relecteurs) et une valeur scientifique séparée des récompenses privées. Les auteurs écrivent : « The model identifies a warning mechanism rather than forecasting a particular conference » (p. 1) ; « The numerical study uses declared illustrative inputs. » (p. 5).

**Chiffres (auteurs, paramètres illustratifs, p. 9-11 et 28-30).** Point selle en x* = 0,5 et y* = 0,25 ; bassins sur une grille de 1 681 départs : 462, 532 et 642 départs atteignent le régime soigneux selon la vitesse relative (tableau 4, p. 28) ; valeur acceptée « accepted value falls from 0.65 in the careful regime to 0.39 in the proxy regime, a 40% loss despite identical publication frequency » (p. 10) ; seuils d'intervention suffisants de 0,75 pour la part d'audits et de 0,2 pour la récompense (p. 11 ; formules lues sur le PDF, non contrôlées par programme : a_c = 1 + α/β, s_c = γ + κ, p. 8).

**Le juge non génératif ?** Le levier d'audit se définit ainsi : une part des soumissions doit « receive externally resourced careful assessment that determines the outcome for those opportunities » (p. 8). C'est un second type d'évaluateur, mais abstrait, jamais attaqué, et sans statistique.

**L'écart entre la note et la découverte : mesuré ? Non.** La valeur scientifique v_i est une grandeur déclarée, fixée à la main (v_A = 0,6 ou 1,2 ; v_T = 1 ; lu sur le PDF, p. 9-10). Le texte exige qu'elle vienne d'ailleurs que des notes : « Detecting that decline requires independent assessment of contribution » (p. 7). La mesure reste à faire : « Independent validation with a stated horizon and unit » (tableau 5, p. 35) ; « A direct empirical test would jointly measure the protocol interaction, workload response, and independently assessed scientific contribution. » (p. 35). Les instruments sont seulement proposés : « For some computational claims, held-out performance, independent replication, proof verification, or discovery in a hidden environment can provide a useful outcome. » (p. 37) ; et « A future empirical version should declare its value measure and horizon before fitting the welfare comparison. » (p. 37). Le texte présente lui-même ses architectures de réforme comme des propositions : « The architectures remain proposals: binary strategies and illustrative parameters do not predict their performance at a particular venue. » (p. 14). L'évasion stratégique est hors du modèle : « In particular, strategic evasion, persistent scholarly records, and training future systems on generated material are outside the baseline dynamics. » (p. 36).

**Incohérences, réserves.** Aucune incohérence trouvée. L'accord des classements numériques avec la frontière analytique, « All 5,043 numerical classifications agree with the analytical boundary. » (p. 10), est une vérification déterministe attendue, pas un résultat trop beau. La pièce relaie deux chiffres de tiers qu'elle ne mesure pas : jusqu'à 82 % d'acceptation de faux articles chez BadScientist, dont elle précise « this is an AI-review outcome, not an observed conference acceptance rate » (p. 34) ; et 53,7 % puis 81,5 % pour Luo et al. Ces chiffres ne sont pas opposables ici (R7).

**Verdicts par composante.**

| composante | verdict | appui |
|---|---|---|
| (a) juge génératif trompé | **voisin** (évaluation « par indices bon marché », humaine ou machine, modélisée et non mesurée) | p. 3, 5 |
| (b) juge statistique hors des agents | **ne touche pas** ; voisin conceptuel : audit soigneux imposé de l'extérieur, sans attaque | p. 8 |
| (c) même attaque sur deux juges | **ne touche pas** (aucune attaque) | p. 36 |
| (d) gain continu en fonction de l'intensité | **ne touche pas** (seuils continus dans les paramètres de politique, aucune intensité d'attaque) | p. 8-11 |
| (e) attaquant agent de recherche | **ne touche pas** (populations d'auteurs, pas d'agent) | p. 5 |
| (f) comparaison de corruptibilité | **ne touche pas** | — |
| écart note / découverte réelle | **non mesuré** : posé par v_i illustratives ; la mesure indépendante est réclamée et proposée, pas faite | p. 7, 35, 37 |

## 4. Ce qui reste revendicable (dans ces deux pièces)

Non trouvé dans les deux pièces lues, formulation exacte : « La mesure, sous **une même attaque** portée par un proposeur modèle de langue, du **gain de l'attaque**, fonction continue de son intensité, **sur un juge statistique calculé hors des agents** et **sur un juge génératif** de la recherche automatisée, et la **comparaison** de ces deux gains. »

Ce verdict reste conditionnel : il ne vaut pas pour le champ ; les quatre autres pièces du lot, lues par une autre session, et les voisins nommés non lus (section 6) peuvent l'occuper.

## 5. Ce qu'une phrase publique sur l'énoncé ne doit pas affirmer

- Que le déplacement d'un relecteur modèle par la présentation, sans changement du fond, est une découverte du programme : il est publié et chiffré (2608.08975, p. 1, 9, 12).
- Que mesurer un gain gradué, non binaire, d'une attaque sur un juge génératif à plusieurs intensités est neuf : c'est fait, à intensités discrètes (2608.08975, p. 12, 49).
- Qu'une consigne de relecture plus stricte suffit à défendre un juge génératif : contredit par 2608.08975 (p. 14).
- Que la boucle « production adaptée à l'évaluateur, évaluation bon marché » est un cadre neuf : elle est formalisée par 2611.10791 (p. 3), qui renvoie lui-même à une synthèse plus large et à un modèle voisin.
- Que 2611.10791 apporte une preuve empirique de la perte de découverte : ses chiffres viennent de paramètres illustratifs (p. 5, 14).
- Que la pièce propre est « libre » : seulement « non trouvée dans les pièces lues », lot 4-B partie 1 non intégré ici.

## 6. Voisins nommés dans les pièces et non lus

Dans 2608.08975 :
- Kaneko 2026, « Paraphrasing adversarial attack on llm-as-a-reviewer. » (arXiv 2601.06884 ; p. 16, cité p. 2, 20) : recherche de paraphrases qui font monter la note.
- Li, Zhang, Davies, Qiu, Gal 2026, « Gaming ai-assisted peer reviews poses new risks to the scientific community. » (arXiv 2606.10159 ; p. 17) : « repeated optimization of paraphrasing, rewriting, and overclaiming can substantially increase AI-review scores » (p. 20). Optimisation répétée, donc dose : **à lire en priorité**.
- Yang et al. 2026a, « Turning bias into bugs: Bandit-guided style manipulation attacks on llm judges. » (arXiv 2605.26156 ; p. 18) : attaques adaptatives qui apprennent quelles retouches de style font monter la note : « stylistic edits inflate a particular judge's scores, including in a case study where generated review texts are themselves evaluated outputs » (p. 19).
- Yang et al. 2026b (arXiv 2606.13044, pièce lue par l'autre session ; p. 18, 20) : « Yang et al. (2026b) similarly introduces adversarial repackaging, a closed-loop procedure that searches for favorable presentation strategies » (p. 20).
- Baumann et al. 2026 (arXiv 2605.03202, p. 16 ; « Baumann et al. (2026) uses paper laundering to describe automated rewriting intended to raise AI-review scores without new experiments. », p. 20) ; Dycke et Gurevych 2026, « Automatic reviewers fail to detect faulty reasoning in research papers: A new counterfactual evaluation framework. » (p. 16, 20) ; Collu et al. 2026, Lin et al. 2025, Ye et al. 2024 (arXiv 2412.01708), Du 2025 (p. 16-20).

Dans 2611.10791 :
- Jiang et al. 2026, « BadScientist: Can a research agent write convincing but unsound papers that fool LLM reviewers? » (p. 15 ; cité p. 2, 4, 34) : pièce de l'autre session.
- Luo, Kasirzadeh, Shah 2026, « The more you automate, the less you see: Hidden pitfalls of autonomous AI scientists. » (p. 15). Selon 2611.10791 : « In its constructed audit dataset, manuscript-only detection accuracy was 53.7%, rising to 81.5% when the auditor received workflow artifacts. » (p. 2). C'est un auditeur comparé sous deux régimes d'information : voisin de (f), **à lire en priorité** ; chiffres non opposables tant qu'ils ne sont pas lus sur le PDF.
- You, Cao, Gurevych 2026, « Preventing the collapse of peer review requires verification-first AI. » (arXiv 2601.16909 ; p. 16), « The closest theoretical comparison is You et al. (2026). » (p. 36) : modèle de corrélation entre note et valeur latente sous bruit d'indices.
- Wang et al. 2026, « The emerging AI paper-review arms race: Adversarial co-evolution in scholarly publishing. » (arXiv 2609.07713 ; p. 15) : « Existing work examines verification incentives (You et al., 2026) and the wider production-evaluation arms race (Wang et al., 2026) » (p. 3).
- Yang, Liu, Xu 2026, SciIntegrity-Bench (arXiv 2605.10246) ; Sharma et al. 2026 (arXiv 2601.20920) ; Kim et al. 2026 (arXiv 2609.19420) ; Beel et al. 2025 (arXiv 2502.14297) (p. 14-16).

## 7. Réserves du lecteur

- **R8** : la composante non trouvée est séduisante, puisque c'est l'apport même du papier C sur ce terrain. Elle n'est cherchée ici que dans deux pièces, dont aucune ne relève des statistiques ou de la validation d'hypothèses. Le verdict « non trouvé » pèse donc peu.
- La lecture de la littérature sur les juges statistiques attaqués (tests adaptatifs, Dwork et al. 2015, Ladder, déjà cités par N-064 dans leur forme) relève d'autres lots ; ce rapport ne s'y substitue pas.
- **R4** : réserve sur l'audit de répétition à un seul relecteur (2608.08975, p. 54) et sur la confusion avec la régression vers la moyenne (p. 10, 32).
