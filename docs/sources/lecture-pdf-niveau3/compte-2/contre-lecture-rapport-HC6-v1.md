# Contre-lecture du rapport HC6 (« le déplacement bénin g prédit la robustesse ») contre 2608.11247v1 — v1

- **Date et heures** (relevées par `date -u`) : début 2026-11-13 23:13:52 UTC (date du dossier de travail, à l'extraction de l'archive du lecteur) ; fin de rédaction 2026-11-13 23:21:24 UTC.
- **Rôle et modèle** : contre-lecteur, modèle B. L'auteur du rapport est le modèle A.
- **Objet** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-HC6-v1.md`, sha256 `0a35df0108ddff1233cb8d6e0002440b2ee301e095459633507d5e329439b079` (conforme à l'attendu) ; son archive `fichiers-de-travail-HC6-v1.tar`, sha256 `66feb8747ebd120730030f702adb19c74f469fa9a08a79ff4c889e29d665ec79` (conforme), extraite dans mon dossier de travail.
- **Pièce et empreinte** : `2608.11247v1.pdf` (17 pages), sha256 `698fdcbd01ed6141535b76012d5aaced574691a8fba192f7e65020987e46f8f9`, identique au compagnon `.sha256` du même dossier.
- **Fichiers lus, liste exacte** :
  1. `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md`, en entier (sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5`, conforme) ;
  2. le rapport et le contenu de son archive (journal, scripts, citations, sorties) ;
  3. `docs/programme-controle-ia-v2.md`, lignes 85-125 et 190-215 ;
  4. `docs/decisions/decision-N-005-N-006-v1.md`, lignes 22-56 ;
  5. `docs/decisions/decision-N-013-v1.md`, lignes 86-95 ;
  6. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 449-463 ;
  7. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 558-575 ;
  8. la pièce et son compagnon.
- **Non ouverts, à dessein** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (la consigne commune le demande au lecteur ; mon mandat borne ma lecture aux fichiers ci-dessus, je m'y suis tenu ; s'il contient un interdit plus strict que ceux de la consigne commune et du mandat, je ne le connais pas) ; `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 313-325, que le lecteur a lu et que mon mandat ne nomme pas.
- **Étendue lue de la pièce** : texte extrait page à page par `pdftotext`, avec et sans `-layout`. Lues ligne à ligne : pages 1 à 9 (corps, discussion, conclusion, limites), 12 à 17 (annexes A à J, tableaux 4 à 13). Parcourues par mots : pages 9 (colonne de droite), 10 et 11 (références ; le début de l'annexe A, page 11, lu ligne à ligne). Lues sur l'image : pages 5, 6, 7, 15, 16 (figures 2, 3, 4, 5, 7, 8 ; tableaux 2, 3, 11, 12). Comptage de mots par page sur vingt racines (« adversar », « attack », « monitor », « jailbreak », « manipulat », « benign », « safety », « oversight », « optimi », « adaptive », « generat », « predict », « transfer », « held-out », « generaliz », « robust », « persua », « deceiv », « decept »).
- **Citations contrôlées par programme** : 39, **0 échec** (script écrit sans reprendre celui du lecteur ; testé d'abord sur un cas juste, 2 sur 2, puis sur un cas altéré, 4 échecs sur 4). 37 au premier niveau, 2 au deuxième (mots composés coupés en fin de ligne : n° 15, p. 4 ; n° 34, p. 9). Les 49 citations du lecteur repassent aussi par mon script : 49 sur 49, 0 échec. Les 24 passages anglais entre guillemets de son rapport sont tous des sous-chaînes de ses citations contrôlées.
- **Une lecture fautive, déclarée.** En vérifiant mes numéros de ligne par une recherche de motifs dans trois fichiers nommés par le mandat, j'ai affiché des lignes hors des plages indiquées : `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 64, 78, 102, 119, 139, 148, 156, 164, 194, 202, 214 et 230 (une ligne chacune, débuts de verdicts et de contre-indices d'autres énoncés) ; `docs/programme-controle-ia-v2.md`, ligne 257 ; `docs/decisions/decision-N-005-N-006-v1.md`, ligne 20. Aucun de ces fichiers n'est sur la liste des interdits ; rien de ces lignes n'entre dans mes constats.
- **Aucun refus.** Aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt. Une liste simple (non récursive) du dossier de sortie `compte-2/`, filtrée sur « HC6 », pour vérifier qu'aucun fichier de sortie n'existait déjà.

Convention : pages du fichier (page 1 = première page du PDF). Nature des chiffres : « auteurs » (imprimé), « figure », « calcul » (recalculé par moi, script `recalculs_contre_lecteur_v1.py`, Python pur, lancé par `python3 -I`).

---

## 1. Verdicts

- **Verdict sur le rapport : « tient avec corrections ».** Aucun constat bloquant. Quatre constats majeurs (A à D), six mineurs (E à J). Aucun ne renverse le verdict du lecteur.
- **Mon verdict pour la pièce, dans la table fermée : « non trouvé dans les pièces lues ».** Verdict sur l'article : « voisin ». Aucune occupation, même partielle.
- Ce verdict ne vaut que pour 2608.11247v1. Il ne touche pas au verdict cumulé du niveau 3 (« occupé en partie, au niveau de l'item », l. 451), appuyé sur des pièces que je n'ai pas lues.
- **Réserve de propreté (règle R4).** Un « non trouvé » net sur une pièce dont le titre semblait porter la relation mérite une réserve. Elle tient ici à un seul point : le sens de « bénin » n'est pas fixé dans les lignes de l'énoncé que j'ai lues (constat D). Le verdict tient sous les deux sens ; je l'ai vérifié séparément pour chacun.

## 2. Réponse aux quatre points du mandat

### Point 1 — La frontière est-elle étrangère à « g bénin prédit la robustesse » ?

Oui, pour trois raisons que je confirme sur le texte, et une quatrième que le lecteur n'a pas chiffrée.

1. **Même pression, écrite d'avance, sur les deux axes.** « Holding the peer script fixed across conditions keeps the pressure controlled and repeatable. » (p. 1). La résistance et la réceptivité sont mesurées sous quatre pairs unanimes, au même gabarit, à polarité opposée (tableau 5, p. 13). Aucun axe n'est une robustesse sous attaque optimisée. Raison bonne, confirmée.
2. **Niveau des interventions.** La droite est ajustée sur six points, chacun moyenné sur 23 modèles : « The frontier is an ordinary least-squares fit to the six snap-answer points » (p. 4). Elle classe des consignes, pas des modèles ; HC6 classe des moniteurs. Raison bonne, confirmée.
3. **Entre modèles, la relation directe n'est pas mesurée.** La phrase « Resistance and Receptivity already move in opposite directions across the 23 models without any intervention. » (p. 6) repose sur deux corrélations avec l'exactitude de base (+0,67 et −0,42 sur MMLU, auteurs). Ces deux chiffres laissent la corrélation directe entre résistance et réceptivité entre −0,96 et +0,39 sur MMLU, entre −0,98 et +0,65 sur GPQA, et entièrement libre sur SimpleQA (calcul, bornes de la matrice de corrélation). Les auteurs eux-mêmes écrivent, pour la moitié réceptivité : « so we rely on the pooled coefficients » (p. 14), et « Both relations are absent on SimpleQA » (p. 15). Au niveau où HC6 se place (un point par modèle), la pièce ne publie donc aucune relation entre ses deux axes.
4. **Déplacement vers le vrai.** Cette raison du lecteur (son point 5, section 5) est la plus faible et doit être réécrite : voir le constat D. Sous le sens « bénin = pression d'une source honnête », la réceptivité est bien un analogue du déplacement bénin, et la lecture favorable à une collision redevient possible. Elle échoue quand même, par les raisons 1 à 3 et par l'absence de moniteur.

**Bilan du point 1.** La lecture « réceptivité = déplacement bénin, résistance = robustesse » est écartée pour de bonnes raisons. La raison « déplacement vers le vrai » ne doit pas être présentée comme une raison indépendante.

### Point 2 — Pression optimisée, générée ou adaptative ; prédiction d'un corpus, d'un modèle ou d'une intervention à l'autre

- **Optimisée contre la cible, adaptative : rien**, annexes comprises. La racine « optimi » n'apparaît qu'une fois, p. 2, à propos d'un article cité : « more so once debaters are optimized for persuasiveness ». Un seul passage, un seul gabarit par condition : « Each condition uses one prompt template, so robustness to paraphrase goes unmeasured » (p. 9).
- **Générée : oui, sur un jeu, et le lecteur l'a manqué** (constat A). Sur SimpleQA, la réponse fausse que les pairs affirment est produite par un modèle : « For SimpleQA, we generate one plausible but incorrect answer per question » (p. 3). Elle n'est ni optimisée contre le modèle cible, ni adaptative ; elle est la même pour les 23 modèles.
- **Prédiction d'un corpus à l'autre, au niveau du modèle : oui, publiée en corrélations de rangs**, et le lecteur l'a classée à tort comme simple contre-indice (constat C).
- **Prédiction d'une dose faible vers une dose forte, au niveau de l'item : oui**, et le lecteur ne l'a citée qu'en passant (constat B).
- **Prédiction d'une intervention à l'autre : non présentée par les auteurs.** Le calcul du lecteur sur « Anchored » est juste ; il est choisi parmi six retraits possibles (constat E).
- **Prédiction d'un modèle à l'autre hors échantillon : rien.** Le retrait de un, deux ou trois modèles (annexe G, p. 15) porte sur l'écart du raisonnement.

### Point 3 — Recalculs

Tous les chiffres du lecteur sont retrouvés, à la décimale imprimée (calcul, tableaux 4 et 6).

| grandeur | imprimé (auteurs) | lecteur (calcul) | contre-lecteur (calcul) |
|---|---|---|---|
| R² de la frontière, questions appariées (MMLU, GPQA, SimpleQA) | 0,88 ; 0,80 ; 0,90 (p. 6) | 0,876 ; 0,801 ; 0,904 | 0,876 ; 0,801 ; 0,904 |
| R² de la frontière, lots complets (second bloc du tableau 6) | non imprimé | non calculé | 0,853 ; 0,797 ; 0,937 |
| pente | non imprimée | −0,484 ; −0,588 ; −1,062 | −0,484 ; −0,588 ; −1,062 |
| écart du raisonnement | +3,3 ; −0,6 ; −1,9 (p. 7) | +3,31 ; −0,55 ; −1,87 | +3,31 ; −0,55 ; −1,87 |
| Spearman des rangs de conformité entre jeux | 0,97 ; 0,74 ; 0,65 (p. 5) | 0,968 ; 0,740 ; 0,652 | 0,968 ; 0,740 ; 0,652 |
| « Anchored » retiré, erreur de la droite des cinq autres | non imprimé | −0,83 ; −1,76 ; −0,99 | −0,83 ; −1,76 ; −0,99 |
| moyennes du tableau 4 | 22,8 ; 54,8 ; 71,0 (tableau 1) | — | 22,80 ; 54,77 ; 70,96 |

Contrôles ajoutés (calcul) :
- **Transcription du tableau 4.** Les moyennes par architecture retrouvent l'annexe E (p. 13-14) : 22,7 (écart-type 18,1) ; 24,7 (28,2) ; 14,75, imprimé 14,7. Idem sur GPQA et SimpleQA. « GPQA au-dessus de MMLU » dans 23 modèles et « SimpleQA au-dessus de MMLU » dans 22 : retrouvé (p. 16).
- **Tableau 2 contre tableau 6.** Les 36 écarts imprimés égalent les différences des moyennes à 0,1 point près.
- **Base à battre, r = −0,64 (p. 5).** Elle **ne se recalcule pas** : l'exactitude de base par modèle n'est imprimée nulle part (figure 3 seulement). Seule la valeur p se vérifie : r = −0,64 et n = 23 donnent p = 0,0010 (imprimé 0,001) ; r = −0,49 donne 0,018 (imprimé 0,017) ; r = −0,42 donne 0,046 (imprimé 0,045) ; r = −0,32 donne 0,137 (imprimé 0,137). Cohérent. Portée : r² = 0,41 sur MMLU, 0,24 sur GPQA ; sur SimpleQA, r = −0,17 (auteurs), soit p ≈ 0,44 (calcul). Voir le constat G.
- **Découpage par item (p. 6).** Les taux 14,7 % et 73,4 % (MMLU), 34,4 % et 84,0 % (GPQA) sont cohérents avec le tableau 1 : ils impliquent 13,8 % et 41,1 % de réponses non tenues sous un seul pair, pour une conformité sous un pair de 11,2 % et 36,5 % plus les troisièmes réponses.

### Point 4 — Incohérences, phrase publique, voisins

Voir les constats F (incohérences manquées), H (ajouts à la section 9) et I (voisins).

## 3. Constats

### A — majeur — « ni générée » est inexact : sur SimpleQA, le contenu de la pression est produit par un modèle

- **Où** : rapport, section 4, composante (b) : « Aucune attaque optimisée, adaptative ni générée. » ; section 3, « Pas d'adversaire optimisé ou adaptatif ».
- **Pièce**, p. 3 : « In the multiple-choice sets, the wrong peer answer is a fixed option determined by an md5 hash of the question ID » ; puis « For SimpleQA, we generate one plausible but incorrect answer per question », par « a model outside the subject pool ». P. 9 : « Of the 4,326 planted distractors, one is flagged invalid by the generation-time filter ».
- **Portée**. La limite citée par le lecteur, « Our peers are scripted rather than generated by live models » (p. 9), porte sur la mise en scène des pairs, pas sur le contenu affirmé. Sur deux jeux, le contenu faux est tiré au hasard ; sur le troisième, il est écrit par un modèle pour être plausible. La comparaison entre MMLU ou GPQA et SimpleQA est donc le seul endroit de la pièce où une pression à contenu aléatoire fait face à une pression à contenu généré et plausible. Les rangs s'y conservent moins bien (0,74 et 0,65, contre 0,97 entre les deux jeux à contenu aléatoire, auteurs, p. 5). Cette lecture est confondue avec le format (réponse libre), la difficulté (exactitude de base de 9,4 %, p. 6) et la taille des lots : elle ne vaut qu'analogie faible.
- **Effet sur le verdict** : aucun. Un distracteur plausible, identique pour tous les modèles, écrit sans voir la cible, n'est pas une attaque optimisée au sens de HC6. La composante (b) reste « ne touche pas ».
- **Texte corrigé**, composante (b) : « Aucune attaque optimisée contre la cible, aucune pression adaptative. Sur SimpleQA seulement, la réponse fausse affirmée par les pairs est générée par un modèle extérieur au groupe, pour être plausible (p. 3, 9) ; elle est la même pour tous les modèles. La “résistance” est mesurée sous cette pression écrite d'avance. » Dans le journal : ajouter « generat » à la liste des racines cherchées (pages 3, 4, 9, 12, 17).

### B — majeur — La prédiction « dose faible vers dose forte » au niveau de l'item est publiée dans la pièce et manque aux sections 5, 8 et 9

- **Où** : rapport, section 4, composante (c), une demi-ligne (« l'item tenu sous un pair est moins renversé sous quatre ») ; rien aux sections 5, 8, 9.
- **Pièce**, p. 6 : « We therefore restrict the pool to answers a model also kept under a single wrong peer. » ; « Conformity on those answers is 14.7% on MMLU and 34.4% on GPQA, against 73.4% and 84.0% on the remainder » ; « An answer kept under one wrong peer is the best evidence available here that the model knew it rather than guessed it ».
- **Portée**. C'est, à l'intérieur d'un modèle et item par item, la tenue sous une pression faible qui sépare la tenue sous une pression plus forte : rapport des taux de 5,0 sur MMLU et de 2,4 sur GPQA (calcul). Les auteurs s'en servent pour corriger les réponses devinées, pas comme prédicteur. Les deux pressions sont écrites d'avance et de même famille ; rien d'optimisé. C'est le voisin de forme le plus proche du verdict du niveau 3 (« au niveau de l'item », l. 451), plus proche que la frontière elle-même.
- **Effet sur le verdict** : aucun (pas d'attaque optimisée, pas de moniteur, pas de classement entre modèles).
- **Texte corrigé**, à ajouter à la section 9 : « Qu'on n'a jamais montré, au niveau de l'item, que la tenue sous une pression faible annonce la tenue sous une pression plus forte de la même famille : 2608.11247 le publie pour des agents répondants (14,7 % contre 73,4 % sur MMLU, 34,4 % contre 84,0 % sur GPQA, auteurs, p. 6). » Et à la section 5, « Lecture favorable », une puce de plus citant ce passage.

### C — majeur — Les corrélations de rangs entre jeux sont un indice à double tranchant, pas un « contre-indice »

- **Où** : rapport, section 6, première puce (« contre-indice faible pour un critère de recette à corpus unique ») ; section 9, deuxième puce.
- **Pièce**, p. 5 : « The two multiple-choice sets rank the pool almost identically » (0,97, auteurs) ; SimpleQA « reorders it substantially » (0,74 et 0,65, auteurs) ; « steadiness on one benchmark guaranties nothing on another ».
- **Portée**. Le lecteur reprend la rhétorique des auteurs. Les chiffres disent autre chose : trois corrélations de rangs positives et fortes entre 23 modèles (0,968 ; 0,740 ; 0,652, calcul ; p de 0,00005 et 0,0008 pour les deux plus faibles, calcul). Parmi les huit modèles les plus conformes sur un jeu, sept, six et cinq le sont aussi sur l'autre (calcul). C'est un transfert de classement d'un corpus à l'autre, sous pression écrite d'avance, au niveau du modèle. Il est nettement plus fort que les contre-indices retenus au niveau 3 (0,33 à 0,40 ; −0,34 ; l. 455-456). La phrase « guaranties nothing » s'appuie sur un seul modèle.
- **Lecture adverse pour le programme** : la pièce publie, pour des agents répondants, une stabilité de rang entre corpus du déplacement sous pression écrite d'avance. Ce n'est pas HC6 (les deux côtés sont bénins). **Hors mandat, signalé seulement** : cela touche la prédiction 3 de HC1 (« stabilité de rang de g entre moniteurs, invariance à l'attaquant et au corpus », N-005, l. 40), que le lecteur n'a pas signalée dans sa section 11.
- **Texte corrigé**, section 6, première puce : « **Classement entre corpus : indice à double tranchant.** Les rangs de conformité des 23 modèles se conservent fortement entre les deux jeux à choix (0,97) et moyennement avec SimpleQA (0,74 et 0,65, auteurs, p. 5, retrouvés par calcul). Un déplacement mesuré sur un corpus de pression classe donc en bonne partie les modèles sur un autre, sans le garantir : indice plutôt favorable à la faisabilité d'un critère à corpus unique entre pressions écrites d'avance, muet sur le passage à une attaque optimisée. » Section 9, deuxième puce : « Que la tenue sous pression écrite d'avance est un trait stable d'un corpus à l'autre, ni qu'elle ne l'est pas du tout : les rangs se conservent à 0,97, 0,74 et 0,65 (p. 5), pour des agents répondants. »

### D — majeur — Le point 5 de la section 5 pose une définition de g que les lignes lues ne donnent pas ; le sens de « bénin » reste ouvert

- **Où** : rapport, section 5, « Lecture défavorable », point 5 : « g est le déplacement vers la cible de l'attaquant. La réceptivité est un déplacement vers la vérité. » ; section 2, dernière puce.
- **Énoncé**. N-005, l. 25-30 : le verdict « se déplace de v₀ vers une destination ĉ », estimée « sans imposer ĉ ». Que ĉ soit la cible de l'attaquant est une prédiction à tester (l. 33), pas la définition de g. Les lignes lues du programme (l. 108, 199) ne définissent pas « bénin ». Le seul sens attesté est la glose du niveau 3, l. 453 (« pression scriptée bénigne » contre « persuadeur adaptatif »). Mais EC.2 (programme, l. 195) prévoit un « agent honnête qui plaide sincèrement » : une pression bénigne par sa source, qui pousse vers le verdict juste. Sous ce second sens, un corpus bénin n'a pas d'attaquant, et la réceptivité (« Receptivity is the share of questions on which the model switches to it », p. 3, sous des pairs qui ont raison) en est l'analogue direct chez des agents répondants.
- **Portée**. Le point 5 du lecteur ne peut donc pas servir de raison indépendante. Sous le second sens, la frontière dit, au niveau des interventions et à l'intérieur d'un modèle (22 puis 23 modèles sur 23, auteurs, p. 6), que plus un agent se laisse déplacer par des pairs justes, moins il tient face à des pairs faux : même signe que HC6. Il manque toujours l'attaque optimisée, le moniteur, et la relation entre modèles (non publiée, voir point 1, raison 3).
- **Effet sur le verdict** : aucun, sous les deux sens.
- **Texte corrigé**, point 5 : « **Sous le sens “bénin = écrit d'avance”, la réceptivité n'est pas le g bénin de HC6** (c'est la conformité qui l'est, point 2). **Sous le sens “bénin = pression d'une source honnête”** (EC.2, l. 195), la réceptivité en est l'analogue, et la frontière porte alors le signe de HC6, mais entre interventions et sous pression écrite d'avance des deux côtés. Les lignes lues de l'énoncé ne tranchent pas entre ces deux sens. » À signaler au compte 2 : le sens de « bénin » dans HC6 gagnerait à être fixé avant tout préenregistrement d'EC.6 ; je ne propose pas de rédaction (rôle exclu).

### E — mineur — Le retrait d'« Anchored » est un cas choisi ; l'écart-type cité n'est pas celui d'une prédiction

- **Où** : rapport, section 5, quatrième puce favorable (« C'est une prédiction hors échantillon réussie ») ; section 7, point 3.
- **Calcul** (tableau 6, p. 13, questions appariées). Chaque point retiré à son tour, erreur de la droite des cinq autres :
  - MMLU : −0,78 ; −0,88 ; **+2,38** (Question Distillation) ; −0,56 ; +0,34 ; −0,83 ;
  - GPQA : +1,34 ; **−3,20** (Devil's Advocate) ; +1,58 ; +2,92 ; −1,07 ; −1,76 ;
  - SimpleQA : +0,15 ; −1,21 ; +1,84 ; −1,86 ; **+3,12** (Reflection) ; −0,99.
  - Racine de l'erreur quadratique : 1,17 ; 2,13 ; 1,78 point, contre 3,09 ; 4,21 ; 4,24 pour la moyenne des cinq autres (qui ignore la réceptivité). La droite fait mieux, d'un facteur 2 à 2,6.
- **Portée**. Le résultat du lecteur tient, mais « Anchored » est le cas que les auteurs mettent en avant, et l'un des mieux prédits. L'écart-type à opposer à l'erreur est celui d'une prédiction (1,39 ; 2,32 ; 1,67), pas l'écart-type résiduel (1,21 ; 2,03 ; 1,46) ; avec trois degrés de liberté, ni l'un ni l'autre n'est stable.
- **Conséquence pour la pièce**. Question Distillation est à +2,4 points au-dessus de la droite des cinq autres sur MMLU, alors que l'exception revendiquée, le raisonnement, est à +3,3 (auteurs, p. 7). La phrase « Each method chooses where on the line to stand and none stands above it. » (p. 6) est plus nette que les six points.
- **Texte corrigé** : « Chaque point retiré à son tour est prédit par la droite des cinq autres à 1,2 ; 2,1 ; 1,8 point près (racine de l'erreur quadratique, calcul), contre 3,1 ; 4,2 ; 4,2 pour leur moyenne. “Anchored” est à −0,83 ; −1,76 ; −0,99. Calcul du lecteur et du contre-lecteur, non présenté par les auteurs ; six points seulement. »

### F — mineur — Incohérences internes non relevées

1. **Intervalle de l'écart sur MMLU absent, phrase fautive.** P. 7 : « an interval whose lower bound does not admits improvement ». La phrase ne dit pas si la borne basse exclut zéro. Le tableau 12 (p. 15) ne donne les intervalles que pour GPQA et SimpleQA. L'écart de +3,3, sur lequel repose l'exception du titre et du résumé, n'a donc aucun intervalle imprimé.
2. **« Six méthodes » sur la droite.** P. 2 : « All six methods we test fall on a single downward-sloping line across all datasets » ; p. 8 : « holds across three datasets and six methods ». Or la droite est ajustée sur cinq méthodes et le point sans intervention (p. 4), et la sixième méthode est l'exception. Le lecteur a relevé une tension voisine (résumé contre tableau 2), pas celle-ci.
3. **« Entre les 23 modèles ».** La phrase de la p. 6 sur les sens opposés est une inférence par l'exactitude (voir point 1, raison 3) ; la conclusion « holds across three datasets » (p. 8) ne vaut pas entre modèles sur SimpleQA (p. 15). Le lecteur l'écrit à son point 3 défavorable, mais reprend la phrase sans réserve dans sa troisième puce favorable.
4. **Lots complets.** « Appendix C repeats every comparison on the full pools, where no conclusion changes. » (p. 4). Dans le second bloc du tableau 6, le point du raisonnement est celui de l'échantillon (« Reasoning runs on samples by construction and repeats its sampled values in both blocks », p. 13). L'écart du raisonnement n'y est donc pas comparable ; calculé tel quel, il vaudrait +2,97 ; −0,56 ; −5,56 (calcul). Sans effet sur HC6.
5. Arrondi : effet du dissident sur SimpleQA, 16,1 par le tableau 1 (calcul), imprimé 16,0 (p. 5).

- **Texte corrigé** : ajouter les points 1 à 3 à la section 7 du rapport. Dans la section 5, troisième puce favorable, ajouter : « (relation inférée par l'exactitude de base ; la corrélation directe n'est pas imprimée) ».

### G — mineur — La « base à battre » est juste, mais sa portée doit être bornée

- **Où** : rapport, section 6, troisième puce ; section 8 ; section 9, quatrième puce.
- **Pièce**, p. 5 : « Conformity decreases as baseline accuracy increases » (r = −0,64, MMLU ; −0,49, GPQA ; auteurs) ; sur SimpleQA, −0,17 (auteurs), que le rapport ne cite pas pour la conformité.
- **Portée**. (i) Le coefficient ne se recalcule pas à partir des tableaux imprimés (point 3). (ii) Il explique 41 % et 24 % de la variance, et rien sur SimpleQA. (iii) Il est en partie mécanique : la conformité est mesurée sur les réponses justes, où les réponses devinées pèsent plus chez les modèles faibles ; les auteurs le corrigent (r = −0,62 et −0,40 sur le lot restreint, p. 6, auteurs). (iv) Ce sont des agents répondants.
- **Texte corrigé**, section 6 : « L'exactitude de base prédit la conformité sur les deux jeux à choix (r = −0,64 et −0,49, auteurs, p. 5 ; −0,62 et −0,40 une fois les réponses devinées écartées, p. 6), pas sur SimpleQA (−0,17). Base à battre par analogie : la compétence du moniteur sans pression. Coefficient non recalculable sur les tableaux imprimés. »

### H — mineur — Section 9 : trois ajouts

- Ajouter la puce du constat B (niveau de l'item).
- Remplacer la deuxième puce par le texte du constat C.
- Ajouter : « Que la frontière entre résistance et réceptivité est établie d'un modèle à l'autre : elle l'est entre interventions et à l'intérieur d'un modèle ; entre modèles, les deux axes ne sont reliés que par l'exactitude de base (p. 6, 14, 15). »
- Ajouter : « Rien sur Khan et collègues 2024 d'après cette seule pièce (constat I). »

### I — mineur — Voisins : la description de Khan et collègues est une glose de la pièce

- **Où** : rapport, section 10, première puce (« un gain lié à la disposition du juge à être déplacé »).
- **Pièce**, p. 2-3 : le résultat attribué est que les juges gagnent en exactitude, « more so once debaters are optimized for persuasiveness » ; la suite, « that rests on the judge’s willingness to be moved and disappears once that willingness is suppressed. », puis « Our results support this concern, since peer agreement carries no information on truth. », est l'interprétation des auteurs de la pièce. Rien n'indique que l'article cité mesure une relation entre la disposition du juge et sa tenue. Le lecteur a bien marqué « non vérifié » (règle R7) ; sa phrase de présentation reprend pourtant la glose.
- **Portée pour HC6**. La priorité de lecture est justifiée : des juges, des débatteurs optimisés pour persuader. Mais ce que la pièce en dit irait plutôt contre le signe de HC6 (un juge qui se laisse déplacer y gagne en exactitude). À lire avant d'en tirer quoi que ce soit. Je ne sais pas, d'après les lignes lues, si cet article figure déjà dans les lectures du programme.
- **Texte corrigé** : « Khan et collègues 2024 : juges non experts, débatteurs optimisés pour la persuasion (p. 2). La pièce ajoute sa propre lecture (le gain tiendrait à la disposition du juge à être déplacé, p. 3), non vérifiée. À lire en priorité contre HC6. »
- **Compléments à la liste** : Wan et collègues 2024 et Xie et collègues 2024 (p. 3) portent sur ce qui déplace un modèle face à un contenu contraire ; ils sont plus proches de la composante (a) que ne le laisse voir leur rang dans la liste. Sperber et collègues 2010 (p. 2) : « agents who depend on communication cannot protect themselves by growing uniformly harder to move » — source de l'axe de coût que le lecteur recommande. Les débats entre agents sont dits supposer la bonne foi : « typically assumes peers argue in good faith » (p. 2).

### J — mineur — Journal et en-tête

- Le journal relève 4 minutes 38 secondes entre le début et le début de la rédaction, pour 17 pages « ligne à ligne », six pages lues sur l'image, un script de calcul et 49 citations. Le contenu du rapport montre une lecture réelle des annexes (tableaux 8, 9, 12, annexes G et H cités à bon escient). La lacune du constat A (p. 3 et 9, dans le corps) montre que « ligne à ligne » n'a pas été tenu partout.
- Section 3 : le rapport écrit « Aucune venue imprimée » : confirmé (p. 1, bandeau de prépublication seul).
- Section 4, composante (a), « Non fait : un coefficient g estimé par régression sur les intensités » : confirmé. Le tableau 1 (p. 4) et la figure 8 (p. 16) donnent cinq niveaux par modèle, sans coefficient.

## 4. Composantes : mon verdict

| composante | verdict du lecteur | mon verdict | remarque |
|---|---|---|---|
| (a) g sur pression bénigne | voisin | **voisin** | conformité graduée sur cinq niveaux, par modèle ; sans coefficient, sans verdict continu |
| (b) robustesse sous attaque optimisée | ne touche pas | **ne touche pas** | texte à corriger (constat A) |
| (c) prédiction de (b) par (a) | ne touche pas pour (b) ; voisin de forme | **ne touche pas** pour (b) ; **voisin** de forme à trois niveaux : item (constat B), modèle entre corpus (constat C), intervention (frontière) | |
| (d) au niveau de chaque moniteur | voisin | **voisin** (modèle répondant) | relation directe entre les deux axes non publiée entre modèles |
| (e) moniteurs de contrôle | ne touche pas | **ne touche pas** | le seul juge note hors pression (p. 11) |

## 5. Jugement de profondeur

- **Lecture du lecteur : suffisante pour le verdict, incomplète sur un point du corps** (constat A) **et trop rapide dans la pesée de deux résultats** (constats B et C). Ses chiffres sont tous justes ; ses citations sont toutes exactes et à la bonne page ; son script de contrôle fait ce qu'il dit.
- **Biais relevé** : le rapport suit la présentation des auteurs là où elle va dans le sens d'un « non trouvé » (« guaranties nothing », « scripted rather than generated »). Deux des quatre constats majeurs viennent de là. La consigne demandait de chercher pour trouver une collision.
- **Ce que je n'ai pas pu vérifier** : le nombre de modèles à pente négative (p. 6), les corrélations avec l'exactitude (figures 3 et 7 seulement), l'intervalle de l'écart sur MMLU (non imprimé).

## 6. Archive

`fichiers-de-travail-contre-lecture-HC6-v1.tar` contient :
- `citations-contre-lecture-HC6-v1.json` (39 citations) ;
- `scripts/controle_citations_contre_lecture_v1.py`, `scripts/ecrire_citations_contre_lecture_v1.py`, `scripts/recalculs_contre_lecteur_v1.py`, `scripts/verifier_citations_du_rapport_v1.py` ;
- `controle-citations-contre-lecture-v1.txt`, `controle-citations-du-lecteur-par-B-v1.txt`, `recalculs-contre-lecteur-v1.txt`, `verification-citations-du-rapport-v1.txt` ;
- `test-juste-contre-lecture-v1.json`, `test-altere-contre-lecture-v1.json` ;
- `journal-contre-lecture-HC6-v1.md`.

Elle ne contient ni le PDF, ni ses textes extraits, ni l'archive du lecteur.
