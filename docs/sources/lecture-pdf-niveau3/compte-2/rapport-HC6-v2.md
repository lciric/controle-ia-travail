# Rapport de lecture — HC6 (« le déplacement bénin g prédit la robustesse ») contre 2608.11247v1 — v2

**lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B**

- **Date et heures** (relevées par `date -u`) :
  - reprise pour la version 2 commencée le 2026-11-13 à 23:22:44 UTC ;
  - redémarrage du conteneur avant le scellement : la première rédaction de la version 2, partielle et non scellée, a été retirée du dépôt par le coordinateur ;
  - rédaction refaite en entier à partir de 23:30:11 UTC ; avant de commencer, j'ai vérifié qu'aucun fichier de version 2 n'existait dans le dossier de sortie.
  - L'heure de fin figure dans le journal de la version 2 et dans le compagnon de scellement.
- **Rapport remplacé** : `rapport-HC6-v1.md`, sha256 `0a35df0108ddff1233cb8d6e0002440b2ee301e095459633507d5e329439b079`. Il est laissé intact, avec son archive `fichiers-de-travail-HC6-v1.tar` (sha256 `66feb8747ebd120730030f702adb19c74f469fa9a08a79ff4c889e29d665ec79`).
- **Contre-lecture intégrée** (modèle B, verdict « tient avec corrections ») :
  - `contre-lecture-rapport-HC6-v1.md`, sha256 `87e1699c995de30e95dfb230f221c148d3fdfe45bfca8d1e7192ba9fabb6f48c`, conforme à l'attendu et à son compagnon ;
  - son archive `fichiers-de-travail-contre-lecture-HC6-v1.tar`, sha256 `9d9cb08c3b532f097d2888d2c473e652cce05368204e8a72bf200a2c893562a3`, conforme ; je l'ai extraite dans un sous-dossier neuf de mon dossier de travail.
  - Toutes les empreintes ont été revérifiées après le redémarrage.
- **Pièce** : `2608.11247v1.pdf` (17 pages), sha256 `698fdcbd01ed6141535b76012d5aaced574691a8fba192f7e65020987e46f8f9`, identique au compagnon `.sha256` de son dossier (`…/scratchpad/pieces-10016a61/docs/sources/pdf/niveau3-v1/lot10/`).
- **Fichiers lus, liste exacte** (versions 1 et 2) :
  1. `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md`, en entier (sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5`, conforme) ;
  2. `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, en entier (version 1, exigé par la consigne commune) ;
  3. `docs/programme-controle-ia-v2.md`, lignes 85-125 et 190-215 ;
  4. `docs/decisions/decision-N-005-N-006-v1.md`, lignes 22-56 ;
  5. `docs/decisions/decision-N-013-v1.md`, lignes 86-95 ;
  6. `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 313-325 ;
  7. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 449-463 ;
  8. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 558-575 ;
  9. la pièce et son compagnon ;
  10. en version 2, la contre-lecture et le contenu de son archive.
  - Toutes les lignes affichées tombent dans les plages permises. En version 2, j'ai revérifié mes numéros de ligne par des affichages bornés à ces plages (programme l. 102 et 195 ; N-005 l. 28 à 40).
- **Étendue lue de la pièce** :
  - version 1 : toutes les pages extraites une à une (`pdftotext`, avec et sans `-layout`) ; pages 1 à 9 et 12 à 17 lues ligne à ligne ; pages 10 et 11 (références) parcourues par mots ; figures lues sur l'image aux pages 2, 5, 6, 7, 15, 16 ;
  - version 2 : pages 3, 6 et 9 relues ligne à ligne, dans l'ordre des colonnes (extraction sans `-layout`) et en mise en page ; figure 2 (p. 5) relue sur une image agrandie à 200 points par pouce, gardée hors de l'archive.
- **Citations contrôlées par programme** : 76 dans `citations-HC6-v2.json`, **0 échec**.
  - Le contrôle a été relancé sur la version finale.
  - Le script, repassé sur ses tests, réussit le cas juste (2 sur 2) et échoue comme attendu sur le cas altéré (3 échecs sur 3).
  - Trois citations passent au second niveau de normalisation (sans espaces ni tirets, mots coupés en fin de ligne) : n° 17 (p. 4), 40 (p. 9) et 55 (p. 3).
  - Tous les passages anglais entre guillemets du présent rapport sont des sous-chaînes de citations contrôlées (vérifié par programme).
- **Aucun refus. Aucune ouverture de fichier interdit.** Aucune commande git, aucun réseau, aucun appel de modèle.
- **Déclaration.** Le rapport de la version 1 nomme un modèle étudié par la pièce (le juge de SimpleQA, section 3). La consigne commune interdit d'écrire « aucun nom ni identifiant de modèle » ; elle vise d'abord les modèles lecteurs, mais sa lettre est générale. La version 1 est scellée et n'est pas réécrite. La version 2 ne nomme aucun modèle.

Convention : les pages sont celles du fichier (page 1 = première page du PDF). Nature des chiffres : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi à partir des tableaux imprimés). « Calcul, B et A » : fait par le contre-lecteur et refait par moi avec mon propre script.

---

## 0. Ce qui change depuis la version 1

- Le verdict est donné **sous chacun des deux sens de « bénin »** (constat D). Je ne tranche pas entre eux : ce choix touche la revendication et revient à Lazar.
- La version 1 disait que la pression n'était générée par aucun modèle. C'est corrigé : sur SimpleQA, la réponse fausse affirmée par les pairs est générée par un modèle (constat A).
- Deux résultats sont maintenant pesés comme voisins de forme de la prédiction :
  - au niveau de l'item, la tenue sous une pression faible annonce la tenue sous une pression forte (constat B) ;
  - au niveau du modèle, le classement se transfère d'un corpus à l'autre (constat C).
- Quatre constats nouveaux, tirés de ma relecture (section 9) :
  - la pièce écrit elle-même qu'une baisse de conformité n'est pas, à elle seule, une preuve d'amélioration (p. 3) ;
  - la figure 2 contredit le « moins de 9 % » du texte sur SimpleQA ;
  - il n'y a ni placebo sans contenu ni probabilité de jeton conservée (p. 9) ;
  - un nom de modèle figure dans la version 1.
- **Le verdict ne change pas** : « non trouvé dans les pièces lues », sous les deux sens.

## 1. Verdict

- **Sous le sens 1** (« bénin = écrit d'avance, non optimisé contre la cible ») : **« non trouvé dans les pièces lues »**.
- **Sous le sens 2** (« bénin = pression d'une source honnête, vers le verdict juste ») : **« non trouvé dans les pièces lues »**. La pièce est alors un voisin plus proche, car sa frontière porte le signe de HC6 (section 5).
- **Verdict sur l'article : « voisin »**, sous les deux sens. Aucune occupation, même partielle : la pièce ne mesure aucune attaque optimisée contre la cible (composante b) et aucun moniteur de contrôle (composante e).
- **Sensibilité du verdict (règle R4).**
  - Le « non trouvé » tient parce que l'attaque optimisée (b) et le moniteur (e) font partie de l'énoncé, que HC6 écrit en toutes lettres (programme, l. 108 : « prédit l'effondrement sous attaque optimisée : critère de recette d'un moniteur »).
  - Si l'on réduisait HC6 à « un déplacement bénin prédit la tenue sous une pression adverse quelconque », la frontière suffirait, sous le sens 2, à occuper en partie cette version affaiblie. Ce serait le cas pour des agents qui répondent à des questions, au niveau des interventions et à l'intérieur d'un modèle, sous pression écrite d'avance des deux côtés.
  - Je ne retiens pas cette lecture affaiblie : elle n'est pas l'énoncé.
- Ce verdict ne porte que sur 2608.11247v1. Il ne confirme ni n'infirme le verdict cumulé du niveau 3 (« occupé en partie, au niveau de l'item », appuyé sur 2608.12645, que je n'ai pas lu).

## 2. L'énoncé confronté, et les deux sens de « bénin »

- **HC6** (programme v2, l. 108 ; inchangé par N-013, l. 90) : « Le g mesuré sur des corpus de pression bénins prédit l'effondrement sous attaque optimisée : critère de recette d'un moniteur avant déploiement. »
- **EC.6** (l. 199) : « g bénin contre robustesse sous attaque optimisée ».
- **Définition de g** :
  - le programme v2 écrit encore, l. 102, Δv = g · (v* − v₀), où v* est la cible de l'attaquant ;
  - la décision N-005, qui fixe la lecture, libère la destination : Δv = g · (ĉ − v₀) (l. 28), g et ĉ estimés par régression sur plusieurs intensités, « sans imposer ĉ » (l. 30) ;
  - que ĉ soit la cible de l'attaquant est une prédiction à tester (l. 33), pas la définition de g ;
  - la stabilité de rang de g « entre moniteurs, invariance à l'attaquant et au corpus » est la prédiction 3 de HC1 (l. 40).
  - Les formules sont lues sur le fichier et non contrôlées par programme.
- **Composantes** :
  - (a) g mesuré sur des corpus de pression bénins ;
  - (b) robustesse sous attaque optimisée ;
  - (c) prédiction de (b) par (a) ;
  - (d) au niveau de chaque moniteur ;
  - (e) pour des moniteurs de contrôle (juges, sondes).
- **« Bénin » n'est pas défini** dans les lignes lues de l'énoncé (constat D). Deux sens sont attestés :
  - **Sens 1 — écrit d'avance, non optimisé.** C'est la glose du niveau 3, l. 453 (« pression scriptée bénigne » contre « persuadeur adaptatif »). Dans la pièce, l'analogue du g bénin est alors la **conformité** sous des pairs écrits d'avance qui affirment le faux.
  - **Sens 2 — source honnête.** EC.2 prévoit un « agent honnête qui plaide sincèrement contre saboteur qui tient le même plaidoyer » (programme, l. 195). Dans la pièce, l'analogue du g bénin est alors la **réceptivité** sous des pairs qui ont raison.

## 3. Ce que fait l'article

**Cadre.** Conformité de modèles de langue à des pairs, dans des systèmes à plusieurs agents qui collaborent. Prépublication arXiv 2608.11247v1 [cs.AI], 3 août 2026, Aarhus University (p. 1). Aucune venue imprimée : le bandeau de prépublication est seul.

**Plan.**
- Chaque modèle répond seul, puis répond de nouveau après qu'on lui a dit que des pairs s'accordent : « Our design changes nothing about a question except what the peers say about it. » (p. 1).
- Le script des pairs est fixe : « Holding the peer script fixed across conditions keeps the pressure controlled and repeatable. » (p. 1).
- 23 modèles à poids ouverts de 19 familles, de 14 à 70 milliards de paramètres (p. 3 ; tableau 4, p. 12). Température 0, un seul passage, réponse d'un jeton par décodage contraint dans les conditions immédiates (p. 3, 12).
- Trois jeux de questions : MMLU (14 042 questions), GPQA-Main (427), SimpleQA (4 326) (p. 3, auteurs).
- **Contenu de la pression** (corrigé, constat A) :
  - sur les jeux à choix, la réponse fausse est tirée par un hachage : « In the multiple-choice sets, the wrong peer answer is a fixed option determined by an md5 hash of the question ID » (p. 3) ;
  - sur SimpleQA, elle est générée par un modèle pour être plausible : « For SimpleQA, we generate one plausible but incorrect answer per question » (p. 3), par « a model outside the subject pool » (p. 3) ; ce sont des « planted distractors » (« Of the 4,326 planted distractors », p. 9) ;
  - ce distracteur est le même pour les 23 modèles, écrit sans voir le modèle cible, non optimisé contre lui.
- **19 conditions** (p. 4 ; tableau 5, p. 13) :
  - une base sans pairs ;
  - un gradient en cinq marches : « A conformity gradient raises the pressure in steps, from one wrong peer, to a wrong majority with one correct dissenter, to a unanimous wrong group whose assertion is bare, briefly reasoned, or stated with high certainty. » (p. 4) ;
  - une sonde de réceptivité (quatre pairs justes) ;
  - six atténuations aux deux polarités : quatre de travaux antérieurs (Devil's Advocate, Question Distillation, Empowered Persona, Reflection) et deux des auteurs (Anchored Reconsideration, Reasoning-first).

**Définitions.**
- **Résistance** : « In the resist pool, the peers unanimously assert an incorrect answer, and we record Resistance, the share of questions on which the model keeps its correct answer » (p. 3).
- **Conformité** : la part où le modèle adopte la réponse des pairs. Elle n'est pas le complément exact de la résistance : les autres cas représenteraient « cases that account for 2–9% of the pool » (p. 3). La figure 2 contredit ce chiffre sur SimpleQA (N2, section 9).
- **Réceptivité** : « In the adopt pool, the peers unanimously assert the correct answer, and Receptivity is the share of questions on which the model switches to it. » (p. 3).
- **Frontière** : « The frontier is an ordinary least-squares fit to the six snap-answer points (five snap mitigations and the no-intervention baseline) » (p. 4).
  - Chaque point est une condition moyennée sur les 23 modèles ; la résistance est portée en ordonnée et la réceptivité en abscisse (figure 5, p. 7).
  - La droite sert de prédicteur dans l'échantillon : « the Resistance a condition reaches minus the Resistance the snap line of Figure 5 predicts at the same Receptivity » (p. 7).
  - Les auteurs en font un critère : « Every point on the line lowers conformity by giving up Receptivity, so a reduction in conformity is not on its own evidence that a method has improved anything » (p. 3).

**Résultats chiffrés.**
- **Gradient** (tableau 1, p. 4, auteurs) : conformité sous quatre pairs unanimes de 22,8 % (MMLU), 54,8 % (GPQA) et 71,0 % (SimpleQA) ; sous un seul pair, de 11,2 %, 36,5 % et 42,5 %.
- **Destination** : 83,6 %, 89,4 % et 87,9 % des réponses abandonnées vont à la réponse des pairs (p. 4, auteurs).
- **Forme de la pression** : « Asserted certainty persuades less than a plain statement on every dataset and in at least 21 of the 23 models » (p. 5).
- **Exactitude et conformité, au niveau du modèle** (p. 5, auteurs) :
  - la conformité décroît avec l'exactitude de base (r = −0,64 sur MMLU ; −0,49 sur GPQA) ;
  - sur SimpleQA, « the association between accuracy and conformity is weak » (r = −0,17, p. 5) ;
  - une fois les réponses devinées écartées, « The accuracy relation holds on the restricted pool » (−0,62 et −0,40, p. 6).
- **Rangs entre corpus** (p. 5) :
  - « The two multiple-choice sets rank the pool almost identically » (Spearman 0,97, auteurs) ;
  - SimpleQA « reorders it substantially » (0,74 et 0,65, auteurs) ;
  - recalculés : 0,968 ; 0,740 ; 0,652 (calcul, B et A).
- **Niveau de l'item** (p. 6) : « We therefore restrict the pool to answers a model also kept under a single wrong peer. » ; « Conformity on those answers is 14.7% on MMLU and 34.4% on GPQA, against 73.4% and 84.0% on the remainder ». Rapports des taux : 4,99 et 2,44 (calcul, B et A).
- **Frontière** (p. 6) :
  - R² de 0,88, 0,80 et 0,90 (auteurs), retrouvés à 0,876, 0,801 et 0,904 (calcul) ;
  - sur les lots complets : 0,853, 0,797 et 0,937 (calcul, B et A) ;
  - pente négative à l'intérieur de 22 modèles sur 23 (MMLU) et des 23 sur les deux autres jeux (auteurs, p. 6).
- **Reflection** (tableau 2, p. 7, auteurs) : +7,9 points de résistance pour −15,3 de réceptivité sur MMLU.
- **Écart du raisonnement à la droite** :
  - +3,3, −0,6 et −1,9 (p. 7, auteurs), retrouvés à +3,31, −0,55 et −1,87 (calcul) ;
  - sur les sujets dérivables de MMLU : +7,2 de résistance et +9,6 de réceptivité (tableau 3, p. 7, auteurs).
- **Entre modèles, sans intervention** (p. 6) : « Resistance and Receptivity already move in opposite directions across the 23 models without any intervention. »
  - Cette phrase repose sur deux corrélations avec l'exactitude de base, +0,67 et −0,42 sur MMLU (auteurs).
  - La corrélation directe entre résistance et réceptivité n'est pas imprimée. Ces deux chiffres la laissent entre −0,96 et +0,39 sur MMLU (calcul, B).
  - Les auteurs écrivent eux-mêmes : « so we rely on the pooled coefficients » (p. 14) ; « Both relations are absent on SimpleQA » (p. 15).

**Ce que l'article ne fait pas** (pertinent pour HC6).
- **Pas d'attaque optimisée contre la cible, pas de pression adaptative** :
  - « Our peers are scripted rather than generated by live models, which gives control over what is asserted at the cost of naturalism. » (p. 9) ;
  - « Each condition uses one prompt template, so robustness to paraphrase goes unmeasured » (p. 9) ;
  - « All conditions are single-pass, which puts multi-round debate out of scope » (p. 9).
- **Pas de moniteur, pas de juge sous pression.** Le seul juge note SimpleQA hors pression : « grades the SimpleQA responses and is held out of the pool » (p. 11).
- **Pas de verdict continu** : les probabilités de jeton ne sont pas gardées, « which these runs did not retain » (p. 9).
- **Pas de placebo sans contenu** : « the design does not include a content-free placebo » (p. 9).
- **Pas de test hors échantillon** d'une intervention ou d'un modèle à l'autre.
- **Pas de corrélation directe** entre résistance et réceptivité d'un modèle à l'autre.

**Limites reconnues** (p. 9) :
- pairs écrits d'avance ; un gabarit par condition ; pas de placebo ; un seul passage ; température 0 ;
- raisonnement mesuré sur des échantillons ;
- partage dérivable / rappel fait à la main et après coup ;
- juge de SimpleQA non validé contre des humains.

L'épreuve de confirmation reste à faire : « a new pool, or a fourth dataset with its own derivable and recall subjects, as the confirmatory test » (p. 9).

## 4. Verdict par composante (mis à jour)

| composante | sens 1 (« écrit d'avance ») | sens 2 (« source honnête ») | page | citation exacte (contrôlée) | fait / non fait |
|---|---|---|---|---|---|
| (a) g sur pression bénigne | **voisin** : conformité sous des pairs écrits d'avance | **voisin** : réceptivité sous des pairs justes | 1, 3, 4, 9, 12 | « Holding the peer script fixed across conditions keeps the pressure controlled and repeatable. » (p. 1) ; « In the adopt pool, the peers unanimously assert the correct answer, and Receptivity is the share of questions on which the model switches to it. » (p. 3) | Fait : déplacement par modèle, cinq marches de pression du côté faux. Non fait : coefficient g par régression sur les intensités ; verdict continu (« which these runs did not retain », p. 9) ; placebo (p. 9) ; corpus rhétorique ; moniteurs. |
| (b) robustesse sous attaque optimisée | **ne touche pas** | **ne touche pas** | 3, 9 | « For SimpleQA, we generate one plausible but incorrect answer per question » (p. 3) ; « Our peers are scripted rather than generated by live models, which gives control over what is asserted at the cost of naturalism. » (p. 9) | Aucune attaque optimisée contre la cible, aucune pression adaptative. Sur SimpleQA seulement, la réponse fausse est générée par un modèle extérieur au groupe, pour être plausible ; elle est la même pour tous les modèles. La « résistance » est mesurée sous cette pression écrite d'avance. |
| (c) prédiction de (b) par (a) | **ne touche pas** pour (b). **Voisin de forme** à trois niveaux, d'une pression écrite d'avance vers une autre : item (p. 6), modèle entre corpus (p. 5), intervention (p. 4, 7) | **ne touche pas** pour (b). **Voisin de forme** : la frontière prédit la résistance par la réceptivité, avec le signe de HC6, entre interventions et à l'intérieur d'un modèle | 4, 5, 6, 7 | « the Resistance a condition reaches minus the Resistance the snap line of Figure 5 predicts at the same Receptivity » (p. 7) ; « Conformity on those answers is 14.7% on MMLU and 34.4% on GPQA, against 73.4% and 84.0% on the remainder » (p. 6) ; « The two multiple-choice sets rank the pool almost identically » (p. 5) | Non fait : aucune prédiction vers une attaque optimisée ; aucun test hors échantillon présenté par les auteurs (le calcul par retrait d'un point, section 5, est de B et A). |
| (d) niveau de chaque moniteur | **voisin** : modèles qui répondent à des questions ; rangs entre corpus au niveau du modèle | **voisin** : relation directe entre les deux axes non publiée entre modèles, seulement inférée par l'exactitude | 5, 6, 14, 15 | « fitted within a single model the slope stays negative for 22 of 23 models on MMLU and for all 23 on the other two datasets » (p. 6) ; « so we rely on the pooled coefficients » (p. 14) | Non fait : moniteurs ; corrélation directe entre modèles. |
| (e) moniteurs de contrôle | **ne touche pas** | **ne touche pas** | 11 | « grades the SimpleQA responses and is held out of the pool » (p. 11) | Les sujets sont des agents qui répondent à des questions. Les juges de débat ne sont que cités (Khan et collègues, p. 2), non lus. |

## 5. La frontière, pesée dans les deux sens et sous les deux sens de « bénin »

### Sous le sens 1 (« écrit d'avance »)

- L'analogue du g bénin est la conformité, non la réceptivité.
- Les deux axes de la frontière sont mesurés sous la même pression écrite d'avance, au même gabarit, à polarité opposée (tableau 5, p. 13). La frontière relie donc le complément approché du g bénin (la résistance) à un déplacement vers le vrai. Aucun des deux axes n'est une robustesse sous attaque optimisée.
- Les voisins de forme les plus proches, sous ce sens, ne sont pas la frontière mais deux autres résultats.
  - **Item** (constat B). La tenue sous un pair sépare la tenue sous quatre pairs : 14,7 % de conformité contre 73,4 % sur MMLU, 34,4 % contre 84,0 % sur GPQA (auteurs, p. 6).
    - Les auteurs y voient une correction des réponses devinées : « An answer kept under one wrong peer is the best evidence available here that the model knew it rather than guessed it » (p. 6).
    - C'est le voisin de forme le plus proche du verdict du niveau 3 (« au niveau de l'item »). Il va d'une dose faible vers une dose forte de la même famille écrite d'avance ; rien n'y est optimisé.
  - **Modèle, entre corpus** (constat C). Les rangs de conformité se conservent à 0,97, 0,74 et 0,65 (auteurs, p. 5). Parmi les huit modèles les plus conformes sur un jeu, sept, six et cinq le restent sur l'autre (calcul, B et A).
- La conformité n'est le complément de la résistance qu'approximativement.
  - Sous quatre pairs, résistance et conformité totalisent 97,7 % sur MMLU et 95,9 % sur GPQA (calcul).
  - Sur SimpleQA, les autres réponses atteignent environ 18 % sous un seul pair (figure 2, p. 5 ; N2).
  - « Le g bénin prédit la résistance sous pression écrite d'avance » serait donc presque une tautologie sur les jeux à choix, pas sur SimpleQA. Les auteurs ne la revendiquent pas.

### Sous le sens 2 (« source honnête »)

- L'analogue du g bénin est la réceptivité. La frontière dit alors : plus un agent se laisse déplacer par des pairs justes, moins il tient face à des pairs faux. **C'est le signe de HC6.**
- Ce qui la soutient :
  - entre interventions, elle est serrée : R² de 0,80 à 0,90 (auteurs) ;
  - la pente est négative à l'intérieur de presque chaque modèle (p. 6) ;
  - elle prédit hors échantillon : en retirant chaque point à son tour, la droite des cinq autres le prédit à 1,17 ; 2,13 ; 1,78 point près (racine de l'erreur quadratique), contre 3,09 ; 4,21 ; 4,24 pour la moyenne des cinq autres, qui ignore la réceptivité (calcul, B et A) ;
  - les auteurs l'énoncent comme un trait : « What lets a model keep a correct answer against a wrong group also makes it slower to accept a correct answer from a right one » (p. 6).
- Ce qui manque toujours :
  1. la robustesse est mesurée sous pression écrite d'avance, pas sous attaque optimisée (b) ;
  2. le niveau est celui des interventions et de l'intérieur d'un modèle ; entre modèles, la relation n'est qu'inférée par l'exactitude (« so we rely on the pooled coefficients », p. 14), et sa corrélation directe n'est pas même bornée en signe (entre −0,96 et +0,39 sur MMLU, libre sur SimpleQA ; calcul, B) ;
  3. la frontière cède quand le modèle peut vérifier lui-même : « Reasoning therefore rises above the frontier on the 20 subjects that give a model an independent check on its own answer » (p. 8) ;
  4. aucun moniteur (e).
- Mon point 5 de la version 1 (« la réceptivité n'est pas le g de HC6 ») ne tient que sous le sens 1. Il ne doit pas servir de raison indépendante (constat D).

### Lecture « contraire »

- La frontière ne contredit pas HC6. Elle ajoute un **axe de coût**, que les auteurs formulent comme un critère :
  - « so a reduction in conformity is not on its own evidence that a method has improved anything » (p. 3) ;
  - « an anti-conformity instruction buys its Resistance by making an agent deaf to right peers as well as wrong ones » (p. 8).
- Choisir un moniteur pour son g bénin faible pourrait donc choisir un moniteur sourd. C'est une réserve de conception pour EC.6 (N1), pas une occupation.

### Bilan

- Ni la relation de HC6, ni son contraire.
- Sous le sens 1 : un voisin de forme d'une pression écrite d'avance vers une autre, à trois niveaux.
- Sous le sens 2 : un voisin de forme plus proche, qui porte le signe de HC6, entre interventions, pour des agents qui répondent à des questions.

## 6. Indices et contre-indices (par analogie, pression écrite d'avance seulement)

- **Classement entre corpus : un indice à double tranchant** (constat C).
  - Les rangs de conformité des 23 modèles se conservent fortement entre les deux jeux à choix (0,97) et moyennement avec SimpleQA (0,74 et 0,65 ; valeurs p de 0,00005 et 0,00075, calcul).
  - Un déplacement mesuré sur un corpus de pression classe donc en bonne partie les modèles sur un autre, sans le garantir.
  - La phrase des auteurs « steadiness on one benchmark guaranties nothing on another » (p. 5) repose sur un seul modèle.
  - Le passage à SimpleQA mêle trois changements : contenu généré et plausible, format libre, exactitude de base proche du plancher.
  - Cet indice est plutôt favorable à la faisabilité d'un critère sur un seul corpus, entre pressions écrites d'avance. Il est muet sur le passage à une attaque optimisée.
  - Je ne le compare pas en grandeur aux contre-indices du niveau 3 (0,33 à 0,40 ; −0,34), qui portent sur une autre relation : du bénin vers l'adaptatif, et de la qualité vers la robustesse.
- **Item, d'une dose faible vers une dose forte** (constat B) : voir la section 5. Indice de forme favorable, d'une pression écrite d'avance vers une autre.
- **Un effet de forme de pression non partagé entre modèles** :
  - « Peer reasoning raises conformity above a bare assertion in only 14, 12, and 16 models » (p. 16) ;
  - la certitude affichée déplace moins que l'affirmation nue (p. 5).
  - Contre-indice faible, par analogie, au transfert d'une famille de pression à une autre.
- **Un prédicteur sans pression publié, à borner** (constat G) :
  - l'exactitude de base prédit la conformité sur les jeux à choix (−0,64 et −0,49, auteurs, p. 5 ; −0,62 et −0,40 une fois les réponses devinées écartées, p. 6), mais pas sur SimpleQA (−0,17, p. 5) ;
  - elle explique 41 % et 24 % de la variance (calcul, B) ;
  - elle n'est pas recalculable, l'exactitude par modèle n'étant imprimée nulle part ;
  - une part en est mécanique, les réponses devinées pesant davantage chez les modèles faibles.
  - Par analogie, c'est une base à battre : la compétence du moniteur sans pression.

## 7. Incohérences internes, résultats trop propres (règle R4)

1. **Résumé contre tableau 2.** « Each gains Resistance only by losing Receptivity » (p. 1). Or Devil's Advocate perd sur les deux axes sur GPQA (−0,7 et −3,7 ; tableau 2, p. 7, auteurs), avec des intervalles qui contiennent zéro (tableau 8, p. 14). Mineur.
2. **Glissement entre résistance et conformité.** « Resistance is also not a fixed trait of a model. » (p. 5) s'appuie sur des rangs calculés sur la conformité (figure 4 ; Spearman retrouvés sur le tableau 4). Les deux ne sont pas des compléments exacts (N2). Mineur.
3. **Six points.** Les prédictions par retrait d'un point sont bonnes en moyenne (section 5), mais inégales.
   - Question Distillation est à +2,38 points au-dessus de la droite des cinq autres sur MMLU, pour un écart-type de prédiction de 0,35 (calcul, B et A ; trois degrés de liberté, donc instable).
   - La phrase « Each method chooses where on the line to stand and none stands above it. » (p. 6) est plus nette que les six points.
   - Anchored, que les auteurs mettent en avant, est l'un des cas les mieux prédits (−0,83 ; −1,76 ; −0,99 ; écart-type de prédiction 1,39 ; 2,32 ; 1,67 ; calcul, B et A).
4. **Intervalle de l'écart sur MMLU absent** (constat F).
   - « an interval whose lower bound does not admits improvement » (p. 7) ne dit pas si la borne basse exclut zéro.
   - Le tableau 12 (p. 15) ne donne les intervalles que pour GPQA et SimpleQA.
   - L'écart de +3,3, sur lequel reposent le titre et le résumé, n'a donc aucun intervalle imprimé.
5. **« Six méthodes » sur la droite** (constat F). « All six methods we test fall on a single downward-sloping line across all datasets » (p. 2) et « holds across three datasets and six methods » (p. 8). Or la droite est ajustée sur cinq méthodes et la base (p. 4), et la sixième méthode est l'exception.
6. **« Entre les 23 modèles »** (constat F). La phrase de la p. 6 est une inférence par l'exactitude, et elle ne vaut pas sur SimpleQA (« Both relations are absent on SimpleQA », p. 15).
7. **Lots complets** (constat F).
   - « Appendix C repeats every comparison on the full pools, where no conclusion changes. » (p. 4).
   - Or le point du raisonnement y est celui de l'échantillon : « Reasoning runs on samples by construction and repeats its sampled values in both blocks » (p. 13).
   - Calculé tel quel, l'écart vaudrait +2,97 ; −0,56 ; −5,56 (calcul, B et A). Sans effet sur HC6.
8. **Arrondi** (constat F) : l'effet du dissident sur SimpleQA vaut 16,1 d'après le tableau 1 (calcul), imprimé 16,0 (p. 5).
9. **Autres réponses sur SimpleQA** : la figure 2 contredit le texte (N2, section 9).
10. **Partage dérivable / rappel fait après coup** : « We drew that line after the cross-dataset pattern was visible » (p. 7). Reconnu et contrôlé par les auteurs (p. 15). Sans effet sur HC6.

## 8. Suite donnée à la contre-lecture

| constat | gravité | décision | où | motif |
|---|---|---|---|---|
| A — « ni générée » inexact : sur SimpleQA, le contenu de la pression est produit par un modèle | majeur | corrigé | sections 3, 4 (b), 5, 6 | Relu p. 3 : « For SimpleQA, we generate one plausible but incorrect answer per question », par « a model outside the subject pool » ; p. 9 : « planted distractors ». La limite « scripted rather than generated by live models » (p. 9) porte sur la mise en scène des pairs, non sur le contenu. Verdict de (b) inchangé : distracteur identique pour tous, écrit sans voir la cible, non optimisé. |
| B — La prédiction « dose faible vers dose forte » au niveau de l'item manque aux sections de pesée | majeur | corrigé | sections 4 (c), 5, 6, 10, 11 | Relu p. 6 : « Conformity on those answers is 14.7% on MMLU and 34.4% on GPQA, against 73.4% and 84.0% on the remainder ». Rapports 4,99 et 2,44 refaits (calcul, A). Les auteurs l'utilisent pour corriger les réponses devinées, non comme prédicteur. Voisin de forme le plus proche du verdict du niveau 3, rien d'optimisé. |
| C — Les corrélations de rangs entre jeux sont un indice à double tranchant, pas un contre-indice | majeur | corrigé | sections 5, 6, 11, 13 | Relu p. 5. Spearman, valeurs p et recouvrement des huit modèles les plus conformes (7, 6 et 5 sur 8) refaits (calcul, A). J'avais suivi la rhétorique des auteurs (« guaranties nothing », appuyé sur un seul modèle). Nuance gardée : pas de comparaison en grandeur avec les contre-indices du niveau 3, qui portent sur une autre relation. Le signal pour HC1 est ajouté en section 13. |
| D — Le point 5 pose une définition de g que les lignes lues ne donnent pas ; le sens de « bénin » reste ouvert | majeur | corrigé | sections 0, 1, 2, 4, 5 | N-005 l. 28, 30, 33 : ĉ est libre, et « ĉ = cible de l'attaquant » est une prédiction. Le programme l. 102 écrit encore v*, mais N-005 fixe la lecture. « Bénin » n'est pas défini aux l. 108 et 199 ; EC.2 (l. 195) atteste le sens « source honnête ». Verdict donné sous les deux sens, sans trancher (choix renvoyé à Lazar) ; le point 5 est réécrit et ne vaut que sous le sens 1. |
| E — Le retrait d'« Anchored » est un cas choisi ; l'écart-type cité n'est pas celui d'une prédiction | mineur | corrigé | sections 5, 7 (point 3) | Tous les retraits d'un point refaits par mon propre script : racine de l'erreur quadratique 1,17 ; 2,13 ; 1,78 contre 3,09 ; 4,21 ; 4,24 pour la moyenne ; écart-type de prédiction d'Anchored 1,39 ; 2,32 ; 1,67 ; Question Distillation à +2,38 sur MMLU. Calcul de B et A, non présenté par les auteurs. |
| F — Incohérences internes non relevées | mineur | corrigé | section 7 (points 4 à 8) | Relu p. 2, 4, 7, 8, 13, 15. Intervalle de l'écart sur MMLU non imprimé ; « six methods » contre une droite de cinq méthodes et la base ; « entre modèles » inféré ; lots complets non homogènes (−5,56 sur SimpleQA, calcul A) ; arrondi 16,1 contre 16,0. J'ajoute une incohérence que B n'a pas relevée (N2). |
| G — La « base à battre » est juste, mais sa portée doit être bornée | mineur | corrigé | sections 6, 10, 11 | Relu p. 5 et 6 : −0,17 sur SimpleQA ; −0,62 et −0,40 sur le lot restreint. Coefficient non recalculable : l'exactitude par modèle n'est pas imprimée (vérifié, le tableau 4 ne donne que la conformité). Part mécanique due aux réponses devinées. |
| H — Section 9 de la version 1 : trois ajouts | mineur | corrigé | section 11 | Ajouts : l'item (B) ; les rangs entre corpus, réécrits (C) ; ne pas affirmer une frontière établie entre modèles ; rien sur Khan et collègues d'après cette seule pièce. J'ajoute de moi-même une puce tirée de la p. 3 (N1). |
| I — Voisins : la description de Khan et collègues est une glose de la pièce | mineur | corrigé | section 12 | Relu p. 2 et 3 : le résultat attribué (« more so once debaters are optimized for persuasiveness », p. 2) est séparé de l'interprétation des auteurs (« that rests on the judge’s willingness to be moved », p. 3). Ajouts : Sperber et collègues (source de l'axe de coût), Wan et collègues, Xie et collègues, et la phrase sur la bonne foi supposée des débats. |
| J — Journal et en-tête : « ligne à ligne » non tenu partout | mineur | corrigé | en-tête, journal de la version 2 | Le passage de la p. 3 sur la génération était dans le texte affiché en version 1, mais je ne l'avais pas pesé. Pages 3, 6 et 9 relues ligne à ligne en version 2, dans l'ordre des colonnes et en mise en page, heures relevées au journal ; cette relecture a produit N1, N2 et N3. |

## 9. Constats nouveaux, tirés de ma relecture des pages 3, 6 et 9

- **N1 — p. 3 : la pièce énonce qu'une baisse de déplacement n'est pas une preuve d'amélioration.**
  - Citations : « Every point on the line lowers conformity by giving up Receptivity, so a reduction in conformity is not on its own evidence that a method has improved anything » (p. 3) ; « Stopping a model from following incorrect peers also stops it from following correct ones » (p. 3).
  - Portée : pour des agents qui répondent à des questions et sous pression écrite d'avance, c'est un argument publié contre l'usage d'un déplacement faible, **seul**, comme critère de recette.
  - Cela ne touche pas la prédiction de HC6. Cela touche sa seconde moitié, « critère de recette d'un moniteur avant déploiement », sous les deux sens de « bénin ». Reporté en section 11.
- **N2 — p. 3, 4 et 5 : la figure 2 contredit le texte sur la part des autres réponses.**
  - Le texte dit « cases that account for 2–9% of the pool » (p. 3) et « together stay below 9% throughout » (p. 4).
  - Sur la figure 2 (p. 5), pour SimpleQA, la bande « autre réponse fausse » vaut environ 18 points sous un seul pair (résistance environ 39, conformité 42, haut de la bande grise environ 99). Elle vaut environ 12 points sous quatre pairs « certains » (figure, image agrandie). Sur les jeux à choix, elle reste sous 9 points (figure).
  - Sous quatre pairs unanimes, résistance et conformité totalisent 97,7 % (MMLU), 95,9 % (GPQA), 88,8 % (SimpleQA, questions appariées) et 91,0 % (SimpleQA, lot complet) (calcul).
  - Effet : sur SimpleQA aux doses faibles, la conformité n'est pas le complément de la résistance. Mon « presque le complément » de la version 1 ne vaut que pour les jeux à choix. Mineur pour HC6.
- **N3 — p. 9 : deux limites qui touchent la composante (a).**
  - Les probabilités de jeton ne sont pas gardées (« which these runs did not retain ») : aucun verdict continu.
  - Il n'y a pas de placebo sans contenu (« the design does not include a content-free placebo ») : le déplacement n'est pas purgé de la sensibilité générique à la consigne.
  - Ces deux limites éloignent encore la mesure du g de N-005, qui est lu par la probabilité du jeton de verdict.
- **N4 — Nom de modèle dans la version 1** : voir la déclaration en tête. La version 1 n'est pas réécrite.

## 10. Ce qui reste revendicable (formulation exacte)

« La prédiction, au niveau de chaque moniteur de contrôle (juge génératif ou sonde), de sa robustesse — ou de son effondrement — sous attaque optimisée contre lui par le contenu, à partir du déplacement g estimé par régression sur des corpus de pression bénins. » **Non trouvée dans 2608.11247v1, sous les deux sens de « bénin ».**

Conditions qui en découlent pour EC.6, d'après cette pièce seule :
- battre au moins un prédicteur sans pression, la compétence du moniteur ; il est publié par analogie pour des agents qui répondent à des questions, avec une portée bornée (section 6) ;
- battre la tenue sous une dose faible de la même famille (voisin de l'item, p. 6) et le rang mesuré sur un autre corpus bénin (voisin entre corpus, p. 5) ;
- rapporter le critère avec un axe de coût, la sensibilité aux arguments légitimes ; le compromis est publié pour des agents qui répondent à des questions (p. 1, 3, 6, 8).

Le sens de « bénin » reste à fixer par Lazar avant tout préenregistrement d'EC.6 (constat D). Je ne propose pas de rédaction.

## 11. Ce qu'une phrase publique sur HC6 ne doit pas affirmer

- Que personne n'a relié deux réponses d'un modèle de langue à une pression écrite d'avance, vers le faux et vers le vrai, au niveau des interventions et à l'intérieur d'un modèle. 2608.11247 le fait : frontière à R² de 0,80 à 0,90 (auteurs, p. 1, 6).
- Que la frontière entre résistance et réceptivité est établie d'un modèle à l'autre. Elle l'est entre interventions et à l'intérieur d'un modèle ; entre modèles, les deux axes ne sont reliés que par l'exactitude de base (p. 6, 14, 15).
- Qu'on n'a jamais montré, au niveau de l'item, que la tenue sous une pression faible annonce la tenue sous une pression plus forte de la même famille. 2608.11247 le publie pour des agents qui répondent à des questions (14,7 % contre 73,4 % sur MMLU, 34,4 % contre 84,0 % sur GPQA ; auteurs, p. 6).
- Que la tenue sous pression écrite d'avance est un trait stable d'un corpus à l'autre, ni qu'elle ne l'est pas du tout. Les rangs se conservent à 0,97, 0,74 et 0,65 (auteurs, p. 5), pour des agents qui répondent à des questions.
- Qu'un g bénin faible est un critère de recette sans coût, ou qu'un déplacement réduit est en soi une amélioration. La pièce publie l'argument contraire pour des agents qui répondent à des questions (p. 3, 8) ; pour des moniteurs, ce coût reste à mesurer.
- Qu'il n'existe aucun prédicteur sans pression du déplacement au niveau du modèle. L'exactitude de base en est un (p. 5), sur les jeux à choix seulement, et non recalculable sur les tableaux imprimés.
- Que 2608.11247 soutient HC6. Il ne mesure ni attaque optimisée ni moniteur.
- Quoi que ce soit sur Khan et collègues 2024 d'après cette seule pièce (section 12).

## 12. Voisins nommés dans la pièce et non lus

- **Khan et collègues 2024**, « Debating with more persuasive llms leads to more truthful answers » (ICML 2024 ; nommé p. 2, référence p. 10).
  - Résultat attribué par la pièce : « Khan et al. (2024) find that non-expert judges grow more accurate after hearing expert debaters, more so once debaters are optimized for persuasiveness » (p. 2).
  - La suite, « that rests on the judge’s willingness to be moved and disappears once that willingness is suppressed. » (p. 3), est la lecture des auteurs de la pièce, non vérifiée (règle R7). Rien n'indique que l'article cité mesure une relation entre la disposition du juge et sa tenue.
  - Des juges et des débatteurs optimisés pour persuader : c'est le **plus proche de HC6** parmi les voisins, et peut-être de signe contraire (un juge qui se laisse déplacer y gagnerait en exactitude).
  - **À lire en priorité contre HC6.** J'ignore, d'après les lignes lues, s'il figure déjà dans les lectures du programme.
- **Sperber et collègues 2010** (vigilance épistémique), p. 2 : « agents who depend on communication cannot protect themselves by growing uniformly harder to move ». Source théorique de l'axe de coût.
- **Wan et collègues 2024**, « What evidence do language models find convincing? », et **Xie et collègues 2024** (conflits de connaissances), p. 3. Ils portent sur ce qui déplace un modèle face à un contenu contraire, donc près de la composante (a). **Longpre et collègues 2021**, p. 3.
- **Du et collègues 2024** et **Liang et collègues 2024** (débat entre agents), p. 2. D'après la pièce, ces travaux « typically assumes peers argue in good faith » (p. 2).
- **Zhu et collègues 2025** (conformité, ACL 2025) et **Weng et collègues 2025** (BenchForm, ICLR 2025), p. 2 et 4 : sources des atténuations.
- **Baltaji et collègues 2024**, p. 2.
- **Sharma et collègues 2023**, **Perez et collègues 2023**, **Wei et collègues 2023** (complaisance), p. 2.
- **Turpin et collègues 2023**, p. 3.
- **Willis 1965**, **Allen et Levine 1969**, **Asch 1951** (psychologie), p. 2.

## 13. Hors mandat, signalé seulement (HC1)

- **Destination** (prédiction 1 de HC1, N-005 l. 33).
  - 83,6 à 89,4 % des réponses abandonnées vont à la réponse des pairs (p. 4, auteurs). La destination coïncide donc avec la cible de la pression.
  - Le cadre est celui de réponses à choix ou courtes, chez des agents qui répondent à des questions, sous pression écrite d'avance. Ce n'est pas un verdict continu de moniteur.
- **Stabilité de rang entre corpus** (prédiction 3 de HC1, N-005 l. 40 : « stabilité de rang de g entre moniteurs, invariance à l'attaquant et au corpus »).
  - Les rangs de conformité se conservent à 0,97, 0,74 et 0,65 entre trois corpus (auteurs, p. 5, retrouvés par calcul), au niveau du modèle, pour des agents qui répondent à des questions.
  - La conservation baisse quand le contenu affirmé change de nature (tiré au hasard contre généré et plausible). Ce changement est confondu avec le format et la difficulté.
  - Signalé par B (constat C).
- Aucun verdict n'est donné ici sur HC1.

## 14. Archive

`fichiers-de-travail-HC6-v2.tar` contient :
- `citations-HC6-v2.json` (76 citations : les 49 de la version 1 et 27 nouvelles) ;
- les scripts `scripts/controle_citations_v1.py` (inchangé), `scripts/ecrire_citations_v2.py` et `scripts/calculs_lecteur_v2.py` ;
- les sorties `controle-citations-v2.txt`, `tests-controle-v2.txt`, `calculs-lecteur-v2.txt` et `verification-guillemets-rapport-v2.txt` ;
- les deux fichiers de test du script de contrôle ;
- le journal `journal-HC6-v2.md`.

Elle ne contient ni le PDF, ni ses textes extraits, ni images, ni l'archive de la contre-lecture.
