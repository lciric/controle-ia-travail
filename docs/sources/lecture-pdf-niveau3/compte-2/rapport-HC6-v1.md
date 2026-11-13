# Rapport de lecture — HC6 (« le déplacement bénin g prédit la robustesse ») contre 2608.11247v1 — v1

- **Date et heures** (relevées par `date -u`) : début 2026-11-13 23:04:25 UTC ; rédaction commencée 2026-11-13 23:09:08 UTC ; l'heure de fin figure dans le journal et dans le compagnon de scellement.
- **Rôle et modèle** : lecteur, modèle A.
- **Mandat** : verdict d'antériorité sur HC6 (papier C) par lecture intégrale d'une pièce versée au lot 10 et jamais lue contre HC6 (constat M10 de la contre-lecture du niveau 3).
- **Pièce et empreinte** : `2608.11247v1.pdf` (17 pages), sha256 `698fdcbd01ed6141535b76012d5aaced574691a8fba192f7e65020987e46f8f9`, identique au compagnon `.sha256` du même dossier (`…/scratchpad/pieces-10016a61/docs/sources/pdf/niveau3-v1/lot10/`).
- **Fichiers lus, liste exacte** :
  1. `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md`, en entier (sha256 `cb0623c4…c77ff5`, conforme) ;
  2. `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, en entier (exigé par la consigne commune ; le plus strict tenu : aucune commande git) ;
  3. `docs/programme-controle-ia-v2.md`, lignes 85-125 et 190-215 ;
  4. `docs/decisions/decision-N-005-N-006-v1.md`, lignes 22-56 ;
  5. `docs/decisions/decision-N-013-v1.md`, lignes 86-95 ;
  6. `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 313-325 ;
  7. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 449-463 ;
  8. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 558-575 ;
  9. la pièce et son compagnon.
- **Étendue lue de la pièce** : toutes les pages extraites une à une (`pdftotext`, avec et sans `-layout`). Lues ligne à ligne : pages 1 à 9, 12 à 17 (corps, discussion, conclusion, limites, annexes A à J). Parcourues par mots : pages 9 (colonne droite), 10 et 11 (références ; le début de l'annexe A, page 11, lu ligne à ligne). Figures et tableaux lus sur l'image : pages 2, 5, 6, 7, 15, 16.
- **Citations contrôlées par programme** : 49, **0 échec** (script testé d'abord sur un cas juste, 2 sur 2, et sur un cas altéré, 3 échecs sur 3). Deux citations passent au second niveau de normalisation (sans espaces ni tirets : mots composés coupés en fin de ligne) : n° 17 (p. 4) et n° 40 (p. 9).
- **Aucun refus, aucune ouverture fautive.**

Convention : les pages sont celles du fichier (page 1 = première page du PDF). Nature des chiffres : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi à partir des tableaux imprimés).

---

## 1. Verdict

- **Verdict d'ensemble sur HC6, pour la pièce lue : « non trouvé dans les pièces lues ».**
- **Verdict sur l'article : « voisin ».** Aucune occupation, même partielle : la pièce ne mesure aucune attaque optimisée et aucun moniteur de contrôle.
- La frontière entre résistance et réceptivité relie **deux réponses à une pression scriptée**, de polarités opposées (pairs unanimes dans le faux, pairs unanimes dans le vrai). Elle ne relie pas un déplacement bénin à une robustesse sous attaque optimisée.
- Ce verdict ne porte que sur 2608.11247v1. Il ne confirme ni n'infirme le verdict cumulé du niveau 3 (« occupé en partie, au niveau de l'item », appuyé sur 2608.12645, que je n'ai pas lu).

## 2. L'énoncé confronté

- **HC6** (programme v2, l. 108 ; inchangé par N-013, l. 90) : « Le g mesuré sur des corpus de pression bénins prédit l'effondrement sous attaque optimisée : critère de recette d'un moniteur avant déploiement. » Expérience EC.6 (l. 199) : « g bénin contre robustesse sous attaque optimisée ».
- **g** (N-005, l. 24-31, formule l. 28) : déplacement du verdict d'un moniteur génératif sous une pression graduée, Δv = g · (ĉ − v₀) (formule lue sur le fichier, non contrôlée par programme), estimé par régression sur plusieurs intensités.
- **Composantes** : (a) g mesuré sur des corpus de pression bénins ; (b) robustesse sous attaque optimisée ; (c) prédiction de (b) par (a) ; (d) au niveau de chaque moniteur ; (e) pour des moniteurs de contrôle (juges, sondes).
- Le sens de « bénin » retenu ici suit le niveau 3 (l. 453 : « pression scriptée bénigne » contre « persuadeur adaptatif ») : une pression écrite d'avance, non optimisée contre la cible. Le second sens possible (« bénin » au sens de pression vers le vrai) est pesé à la section 5.

## 3. Ce que fait l'article

**Cadre.** Conformité de modèles de langue à des pairs, dans des systèmes à plusieurs agents qui collaborent. Prépublication arXiv 2608.11247v1 [cs.AI], 3 août 2026, Aarhus University (p. 1). Aucune venue imprimée.

**Plan.**
- Chaque modèle répond d'abord seul. Il répond ensuite après qu'on lui a dit que des pairs s'accordent sur une autre réponse : « Our design changes nothing about a question except what the peers say about it. » (p. 1). Les pairs sont fixés par un script : « Holding the peer script fixed across conditions keeps the pressure controlled and repeatable. » (p. 1).
- 23 modèles à poids ouverts de 19 familles, de 14B à 70B paramètres (p. 3, tableau 4 p. 12). Température 0, un seul passage, réponse d'un jeton par décodage contraint (p. 3, 12).
- Trois jeux : MMLU (14 042 questions), GPQA-Main (427), SimpleQA (4 326) (p. 3, auteurs).
- 19 conditions (p. 4, tableau 5 p. 13) :
  - une base sans pairs ;
  - un gradient de pression en cinq marches : « A conformity gradient raises the pressure in steps, from one wrong peer, to a wrong majority with one correct dissenter, to a unanimous wrong group whose assertion is bare, briefly reasoned, or stated with high certainty. » (p. 4) ;
  - une sonde de réceptivité (quatre pairs justes) ;
  - six atténuations, chacune aux deux polarités. Quatre sont publiées : Devil's Advocate, Question Distillation, Empowered Persona, Reflection. Deux sont propres aux auteurs : Anchored Reconsideration et Reasoning-first.

**Définitions.**
- **Résistance** : « In the resist pool, the peers unanimously assert an incorrect answer, and we record Resistance, the share of questions on which the model keeps its correct answer » (p. 3). C'est la part des questions réussies seul où le modèle garde sa réponse juste face à quatre pairs unanimes dans le faux, écrits par script.
- **Conformité** : la part où il adopte la réponse des pairs. Elle n'est pas le complément exact de la résistance : une troisième réponse ou une abstention représente 2 à 9 % du lot (p. 3, auteurs).
- **Réceptivité** : « In the adopt pool, the peers unanimously assert the correct answer, and Receptivity is the share of questions on which the model switches to it. » (p. 3). C'est un déplacement sous pression scriptée, mais vers le vrai.
- **Frontière** : « The frontier is an ordinary least-squares fit to the six snap-answer points (five snap mitigations and the no-intervention baseline) » (p. 4). Chaque point est une condition moyennée sur les 23 modèles. La figure 5 (p. 7) porte la résistance en ordonnée et la réceptivité en abscisse. L'écart d'une condition est mesuré au point de réceptivité de cette condition : « the Resistance a condition reaches minus the Resistance the snap line of Figure 5 predicts at the same Receptivity » (p. 7).

**Résultats chiffrés.**
- **Gradient** (tableau 1, p. 4, auteurs) : sous quatre pairs unanimes, la conformité vaut 22,8 % (MMLU), 54,8 % (GPQA) et 71,0 % (SimpleQA). Avec un seul pair dans le faux, elle vaut 11,2 %, 36,5 % et 42,5 %.
- **Destination** : 83,6 % (MMLU), 89,4 % (GPQA) et 87,9 % (SimpleQA) des réponses abandonnées vont à la réponse des pairs (p. 4, auteurs).
- **Forme de la pression** : « Asserted certainty persuades less than a plain statement on every dataset and in at least 21 of the 23 models » (p. 5).
- **Niveau du modèle** (p. 5, auteurs) : la conformité décroît avec l'exactitude de base (r = −0,64, p = 0,001, MMLU ; r = −0,49, GPQA). Elle ne dépend pas de la taille.
- **Rangs entre jeux** (p. 5, auteurs) : rangs de conformité entre jeux, Spearman 0,97 (MMLU-GPQA), 0,74 (MMLU-SimpleQA), 0,65 (GPQA-SimpleQA). Recalculés sur le tableau 4 : 0,968 ; 0,740 ; 0,652 (calcul).
- **Frontière** (p. 6, auteurs) : R² = 0,88 (MMLU), 0,80 (GPQA), 0,90 (SimpleQA). Recalculés sur le tableau 6 : 0,876 ; 0,801 ; 0,904 (calcul). Pente négative dans 22 modèles sur 23 (MMLU) et dans les 23 pour les deux autres jeux.
- **Coût de Reflection** (tableau 2, p. 7, auteurs) : +7,9 points de résistance pour −15,3 de réceptivité (MMLU).
- **Reasoning-first** (p. 7, tableau 3, auteurs) : écart de +3,3 au-dessus de la frontière (MMLU), −0,6 (GPQA) et −1,9 (SimpleQA). Sur les sujets dérivables de MMLU : +7,2 de résistance et +9,6 de réceptivité. Ces trois écarts sont retrouvés : +3,31 ; −0,55 ; −1,87 (calcul).
- **Sans intervention** (p. 6, figure 7 p. 15, auteurs) : résistance et réceptivité vont en sens contraires d'un modèle à l'autre, par l'exactitude de base. La résistance suit l'exactitude (r = +0,67, MMLU) et la réceptivité la suit en sens inverse (r = −0,42). Les deux relations sont nulles sur SimpleQA (+0,06 et +0,00).

**Ce que l'article ne fait pas** (pertinent pour HC6) :
- **Pas d'adversaire optimisé ou adaptatif.** « Our peers are scripted rather than generated by live models, which gives control over what is asserted at the cost of naturalism. » (p. 9). Un seul gabarit par condition : « Each condition uses one prompt template, so robustness to paraphrase goes unmeasured » (p. 9). Un seul passage : « All conditions are single-pass, which puts multi-round debate out of scope » (p. 9).
- **Pas de moniteur, pas de juge sous pression.** Les modèles étudiés répondent à des questions de connaissance. Le seul juge, un modèle Llama de 70B, note SimpleQA hors pression : « grades the SimpleQA responses and is held out of the pool » (p. 11).
- **Pas de test de prédiction hors échantillon** d'une condition ou d'un modèle à l'autre. La frontière est un ajustement sur six points, dans l'échantillon. Le rééchantillonnage en laissant de côté un, deux ou trois modèles porte sur l'écart du raisonnement, pas sur la prédiction de la résistance (p. 15).
- **Pas de corrélation directe** entre résistance et réceptivité d'un modèle à l'autre. Elles ne sont reliées que par l'exactitude (p. 6, 15). Aucun tableau par modèle des deux taux n'est imprimé : je n'ai pas pu la calculer.
- Recherche de mots dans tout le texte extrait (journal) : aucune occurrence de « adversar », « attack », « monitor », « jailbreak », « manipulat », « benign », « safety », « oversight ». « optimi » n'apparaît qu'une fois, p. 2 (Khan et al., cité).

**Limites reconnues** (p. 9) : pairs scriptés ; un gabarit par condition ; pas de placebo sans contenu ; un seul passage ; température 0 ; raisonnement sur échantillons ; partage dérivable / rappel fait à la main et après coup ; juge SimpleQA non validé contre des humains. L'épreuve de confirmation reste à faire : « a new pool, or a fourth dataset with its own derivable and recall subjects, as the confirmatory test » (p. 9).

## 4. Verdict par composante

| composante | verdict | page | citation exacte (contrôlée) | ce qui est fait / ce qui ne l'est pas |
|---|---|---|---|---|
| (a) g sur pression bénigne | **voisin** | 1, 4, 12 | « Holding the peer script fixed across conditions keeps the pressure controlled and repeatable. » (p. 1) ; « conditions 2–6 raise the pressure on the resist pool from one wrong peer to a unanimous wrong group of four, and condition 7 is the Receptivity probe » (p. 12) | Fait : déplacement sous pression scriptée, graduée sur cinq marches, par modèle ; destination concentrée sur la réponse des pairs. Non fait : un coefficient g estimé par régression sur les intensités ; un verdict continu ; un corpus de pression rhétorique (seul le nombre de pairs et trois formulations changent). |
| (b) robustesse sous attaque optimisée | **ne touche pas** | 9 | « Our peers are scripted rather than generated by live models, which gives control over what is asserted at the cost of naturalism. » (p. 9) | Aucune attaque optimisée, adaptative ni générée. La « résistance » est mesurée sous la même pression scriptée que le reste. |
| (c) prédiction de (b) par (a) | **ne touche pas** pour (b) ; **voisin** pour la forme d'une prédiction entre deux réponses à une pression scriptée | 4, 5, 6, 7 | « the Resistance a condition reaches minus the Resistance the snap line of Figure 5 predicts at the same Receptivity » (p. 7) ; « What a model knows predicts how many of its correct answers a wrong group reverses, whereas a model’s size exhibit not predictive power in this regard. » (p. 5) | Fait : la résistance est prédite par la réceptivité le long d'une droite ajustée sur les conditions, dans l'échantillon ; la conformité est prédite par l'exactitude sans pression, d'un modèle à l'autre ; l'item tenu sous un pair est moins renversé sous quatre (p. 6) ; rangs entre jeux (p. 5). Non fait : aucune prédiction vers une attaque optimisée, aucun test hors échantillon. |
| (d) au niveau de chaque moniteur | **voisin** (au niveau du modèle répondant) | 5, 6, 12, 16 | « fitted within a single model the slope stays negative for 22 of 23 models on MMLU and for all 23 on the other two datasets » (p. 6) | Fait : taux par modèle (tableau 4, figures 3, 4, 7, 8), pente par modèle. La frontière elle-même est au niveau de l'intervention, en moyenne sur les modèles. Non fait : moniteurs. |
| (e) moniteurs de contrôle | **ne touche pas** | 1, 11 | « grades the SimpleQA responses and is held out of the pool » (p. 11) | Les sujets sont des agents qui répondent à des questions. Le seul juge note hors pression. Les juges de débat ne sont que cités (Khan et al., p. 2-3, non lu). |

## 5. La frontière : relation de HC6, contraire, ou ni l'un ni l'autre

**Lecture favorable à une collision.**
- Si l'on prend la réceptivité pour un « déplacement bénin » (être déplacé par des pairs qui ont raison) et la résistance pour une « robustesse », la frontière dit : plus le modèle se laisse déplacer, moins il résiste. C'est le signe que HC6 sous-entend (g bénin fort, effondrement fort).
- La relation est serrée : R² de 0,80 à 0,90 (auteurs, retrouvé par calcul). La pente est négative dans presque chaque modèle (p. 6).
- Elle existe sans intervention, d'un modèle à l'autre : « Resistance and Receptivity already move in opposite directions across the 23 models without any intervention. » (p. 6).
- Elle tient pour une intervention écrite contre elle. Mon calcul : Anchored Reconsideration retiré de l'ajustement retombe à −0,83 ; −1,76 ; −0,99 point de la droite des cinq autres points, pour des écarts-types résiduels de 1,21 ; 2,03 ; 1,46. C'est une prédiction hors échantillon réussie, mais je l'ai calculée moi-même ; les auteurs ne la présentent pas comme telle.

**Lecture défavorable, qui l'emporte.**
1. **Les deux axes sont scriptés.** La résistance est mesurée sous quatre pairs unanimes et fixés par script, c'est-à-dire sous la pression que HC6 appelle « bénigne ». La frontière relie donc deux mesures bénignes entre elles (vers le faux et vers le vrai). Aucun de ses axes n'est une robustesse sous attaque optimisée. La composante (b), qui fait la valeur de HC6 (« critère de recette avant déploiement »), est absente.
2. **Au sens de HC6, la conformité est le g bénin, et la résistance en est presque le complément par construction** (2 à 9 % de troisièmes réponses ou d'abstentions, p. 3). Dans cet article, « le g bénin prédit la résistance scriptée » serait presque une tautologie. L'article ne la revendique d'ailleurs pas.
3. **Le niveau n'est pas le bon.** La frontière est tracée entre interventions (consignes), en moyenne sur 23 modèles, et à l'intérieur d'un modèle entre interventions. HC6 classe des moniteurs. D'un modèle à l'autre, les deux axes ne sont reliés qu'au travers de l'exactitude de base (p. 6, figure 7). Ce lien disparaît sur SimpleQA (r = +0,06 et +0,00, auteurs, p. 15).
4. **La frontière n'est pas une loi de prédiction.** Elle est rompue quand le modèle dispose d'une vérification propre : « Reasoning therefore rises above the frontier on the 20 subjects that give a model an independent check on its own answer » (p. 8). Les auteurs la décrivent comme une propriété de la tâche : « The frontier is a property of the task, visible in the baselines before any method is applied. » (p. 8).
5. **La réceptivité n'est pas le g de HC6.** g est le déplacement vers la cible de l'attaquant. La réceptivité est un déplacement vers la vérité. Pour un moniteur, elle correspondrait plutôt à la sensibilité aux arguments légitimes, c'est-à-dire à l'utilité honnête et non au g.

**Lecture « contraire ».** La frontière est un compromis : plus de résistance, moins de réceptivité. Elle ne contredit pas HC6, qui ne dit rien de la réceptivité. Elle ajoute un **axe de coût** : choisir un moniteur sur un g bénin faible pourrait choisir un moniteur sourd. L'article le formule pour les agents : « an anti-conformity instruction buys its Resistance by making an agent deaf to right peers as well as wrong ones » (p. 8). C'est une réserve de conception pour EC.6, pas une occupation.

**Bilan.** Ni la relation de HC6, ni son contraire. Un voisin de forme : une relation de compromis entre deux réponses à une pression scriptée, sur des agents répondants, au niveau de l'intervention.

## 6. Contre-indices (par analogie, pression scriptée seulement)

- **Dépendance au corpus.** Le classement des modèles change d'un jeu à l'autre : « Resistance is also not a fixed trait of a model. » et « steadiness on one benchmark guaranties nothing on another » (p. 5). Spearman 0,74 et 0,65 avec SimpleQA (auteurs, retrouvé par calcul). Un g bénin mesuré sur un seul corpus de pression pourrait mal classer les moniteurs sur un autre : **contre-indice faible** pour un critère de recette à corpus unique.
- **Effet d'une famille de pression non partagé.** « Peer reasoning raises conformity above a bare assertion in only 14, 12, and 16 models » (p. 16). La certitude affichée déplace moins que l'affirmation nue (p. 5). L'ordre des modèles sous une famille de pression ne se transfère pas forcément à une autre : **contre-indice faible**, par analogie, pour une prédiction d'une famille bénigne vers une attaque optimisée.
- **Prédicteur sans pression publié, au niveau du modèle.** L'exactitude de base prédit la conformité (r = −0,64 sur MMLU, auteurs, p. 5). Ce n'est pas un contre-indice mais une **base à battre** analogue à celles du niveau 3 (taux sur attaques faibles, force de la majorité d'un jury) : la compétence du moniteur sans pression.

## 7. Incohérences internes, résultats trop propres (règle R4)

1. **Résumé contre tableau 2.** Le résumé dit « Each gains Resistance only by losing Receptivity » (p. 1). Or Devil's Advocate sur GPQA perd sur les deux axes (−0,7 et −3,7, tableau 2, p. 7, auteurs), avec des intervalles qui contiennent zéro (tableau 8, p. 14). Mineur.
2. **Glissement entre résistance et conformité.** « Resistance is also not a fixed trait » (p. 5) s'appuie sur la figure 4 et sur des rangs calculés sur la **conformité**. Je retrouve les Spearman imprimés sur les taux de conformité du tableau 4 (calcul). Les deux ne sont pas des compléments exacts. Mineur.
3. **Ajustement sur six points.** Un R² de 0,80 à 0,90 sur six points moyennés est peu contraignant. Les points extrêmes (base, Reflection) portent la pente. La relation est soutenue par les pentes par modèle (p. 6) et par mon calcul hors échantillon pour Anchored. Réserve de propreté **modérée** : « trop beau » non établi, mais la relation n'est pas testée sur une famille d'interventions neuve.
4. **Partage dérivable / rappel fait après coup** (« We drew that line after the cross-dataset pattern was visible », p. 7). Les auteurs le reconnaissent et le contrôlent par une moitié et par un évaluateur à l'aveugle (p. 15). Sans effet sur HC6.

## 8. Ce qui reste revendicable (formulation exacte)

« La prédiction, au niveau de chaque moniteur de contrôle (juge génératif ou sonde), de sa robustesse — ou de son effondrement — sous attaque optimisée par contenu, à partir du déplacement g mesuré par régression sur des corpus de pression bénins, scriptés et non optimisés. » **Non trouvée dans 2608.11247v1.** Elle devra battre, au minimum, un prédicteur sans pression (l'exactitude ou la compétence du moniteur, voisin publié ici pour des agents répondants, p. 5) et, si elle est mesurée, être rapportée avec un axe de coût (sensibilité aux arguments légitimes), puisque le compromis est publié pour des agents répondants (p. 1, 6, 8).

## 9. Ce qu'une phrase publique sur HC6 ne doit pas affirmer

- Que personne n'a relié, au niveau du modèle ou de l'intervention, deux réponses d'un modèle de langue à une pression scriptée (vers le faux et vers le vrai). 2608.11247 le fait : frontière à R² de 0,80 à 0,90, auteurs (p. 1, 6).
- Que la tenue sous pression scriptée est un trait stable d'un corpus à l'autre (contredit p. 5 pour des agents répondants).
- Qu'un g bénin faible est un critère sans coût. Le compromis entre résistance et réceptivité est publié (p. 1, 6, 8) pour des agents répondants ; pour des moniteurs, il reste à mesurer.
- Qu'il n'existe aucun prédicteur sans pression du déplacement au niveau du modèle (l'exactitude de base, p. 5).
- Que 2608.11247 soutient HC6. Il ne mesure ni attaque optimisée ni moniteur.

## 10. Voisins nommés dans la pièce et non lus

- **Khan et al. 2024** (« Debating with more persuasive llms leads to more truthful answers », ICML 2024), nommé p. 2-3, référence p. 10. C'est le **plus proche de HC6** parmi les voisins : des juges, des débatteurs optimisés pour la persuasion, et un gain lié à la disposition du juge à être déplacé. Citation de la pièce : « Khan et al. (2024) find that non-expert judges grow more accurate after hearing expert debaters, more so once debaters are optimized for persuasiveness » (p. 2) ; suite : « that rests on the judge’s willingness to be moved and disappears once that willingness is suppressed. » (p. 3). Ce que la pièce attribue à Khan n'est pas vérifié par moi (règle R7). **À lire en priorité contre HC6.**
- Zhu et al. 2025 (conformité, ACL 2025) et Weng et al. 2025 (BenchForm, ICLR 2025), nommés p. 2, 4, sources des atténuations.
- Baltaji et al. 2024 (conformité en collaboration multi-agents), p. 2.
- Sharma et al. 2023, Perez et al. 2023, Wei et al. 2023 (complaisance), p. 2.
- Du et al. 2024 et Liang et al. 2024 (débat multi-agents), p. 2.
- Longpre et al. 2021, Xie et al. 2024, Wan et al. 2024 (conflits de connaissances), p. 3.
- Turpin et al. 2023 (raisonnement infidèle), p. 3.
- En psychologie : Sperber et al. 2010 (vigilance épistémique, côté coût), Willis 1965, Allen et Levine 1969, Asch 1951, p. 2.

## 11. Hors mandat, signalé seulement

Pour HC1 (destination ĉ) : 83,6 à 89,4 % des réponses abandonnées vont à la réponse des pairs (p. 1, 4, auteurs). C'est une destination égale à la cible de la pression, sur des réponses à choix ou courtes, chez des agents répondants et sous pression scriptée. Ce n'est pas un verdict continu de moniteur. Aucun verdict n'est donné ici sur HC1.

## 12. Archive

`fichiers-de-travail-HC6-v1.tar` contient :
- `citations-HC6-v1.json` (49 citations) ;
- `scripts/controle_citations_v1.py`, `scripts/ecrire_citations_v1.py`, `scripts/calculs_lecteur_v1.py` ;
- `controle-citations-v1.txt`, `calculs-lecteur-v1.txt` ;
- les deux fichiers de test (`test-juste-v1.json`, `test-altere-v1.json`) ;
- `journal-HC6-v1.md`.

Elle ne contient ni le PDF ni ses textes extraits.
