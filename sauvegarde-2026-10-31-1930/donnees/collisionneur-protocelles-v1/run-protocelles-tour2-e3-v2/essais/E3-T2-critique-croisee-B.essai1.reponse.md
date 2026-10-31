# Sur la proposition C (Argon)

## (a) Défauts de méthode

### 1. Confusion entre la surmartingale par pas et l'extinction comme résultat dynamique

C fonde une large part de son architecture expérimentale — les Duels 1, 2 et 3, la justification de la politique d'archivage, et la résolution de la divergence (a)4 — sur l'esquisse algébrique du §3.1 de la synthèse, qu'il traite comme un résultat acquis moyennant contre-lecture. Or cette esquisse établit une propriété par pas de fusion (E[φ′]/φ ≤ 1 quand q_vv ≤ 1/2 à θ = 1), pas l'extinction de la population de fiches vraies au fil d'une trajectoire réelle. La synthèse elle-même la classe comme « esquisse du relecteur, à contre-lire (R2), jamais un résultat » [VÉRIFIÉ, synthèse, section 3.1, point 3]. C écrit que « aucune loi du taux d'événements ne peut transformer une surmartingale par pas en processus supercritique », ce qui est mathématiquement correct pour le sens de la dérive conditionnelle, mais il en conclut que « l'extinction est certaine dès que q_vv ≤ min(θ,1)/2 indépendamment de la loi du taux d'événements ». C'est un saut logique : une surmartingale bornée inférieurement (φ ≥ 0) converge presque sûrement, mais elle peut converger vers une valeur positive. L'extinction (φ → 0 p.s.) requiert soit un argument supplémentaire (par exemple que le seul état absorbant accessible soit φ = 0 sur un espace d'états discret fini, ce qui est plausible ici mais n'est pas démontré dans l'esquisse), soit la finitude de la population, soit un résultat de type « gamblers' ruin ». C traite le gap entre surmartingale et extinction comme nul, là où D le signale correctement.

**Variable confondante associée** : dans le Duel 1, la falsification de H_B (stérilité confirmée) repose en partie sur l'observation d'une « dérive de φ négative ou nulle ». Mais si le nombre de pas de fusion est petit (24 fusions par bras dans la course 2, synthèse section 3), la variance de l'estimateur de dérive sera du même ordre que la dérive elle-même. C ne donne aucun calcul de puissance pour cette composante du Duel 1, alors même qu'il relève correctement la puissance nulle des tests à 3 lots pour d'autres questions.

### 2. Circularité entre le juge et le bisociateur

Le Duel 1 et toute mesure de q_vv, q_vf, q_ff nécessitent un « juge indépendant » qui classifie les fiches filles comme vraies ou fausses. C propose un critère d'acceptation (VP − FP > 0,20) et un contrôle mécanique, ce qui est bien. Mais il ne traite pas le problème de circularité suivant : si le juge partage une partie de ses représentations internes ou de ses données d'entraînement avec le bisociateur (ce qui est le cas si tous deux sont des modèles de langage entraînés sur des corpus largement chevauchants), les taux q_vv mesurés ne sont pas des propriétés du processus de bisociation, mais des propriétés jointes du couple (bisociateur, juge). Un changement de juge changerait q_vv, ce qui signifie que q_vv n'est pas un paramètre du système mais un artefact de mesure.

C mentionne (section 1.2 de sa réponse) que le juge doit « battre une heuristique mécanique de surface d'au moins +0,15 en score de Youden », mais cette exigence ne protège pas contre une corrélation systématique des erreurs entre juge et bisociateur. Le contrôle négatif qui manque est une mesure de q_vv avec deux juges de provenance distincte : si leurs estimations divergent au-delà de la variance d'échantillonnage, q_vv n'est pas identifié.

### 3. Le Duel 3 est vrai par construction sous une lecture directe de I12

C reformule le Duel 3 en test de « complémentation fertile (q_B > 0) contre quarantaine stricte ». Mais il définit l'hypothèse H_A (optimalité de la quarantaine) par ρ_bain ≤ ρ_quarantaine. Or, comme C lui-même le reconnaît après la correction de I12, perdre toutes les copies inachevées ne coûte rien sur U_c à fécondité infinie, et tout maintien dans le vivier de copies stériles avec θ′ ≥ min(θ,1) **abaisse** le plafond d'au moins −ln(1−τ). Il s'ensuit que H_A est vraie par construction pour tout brouillon stérile (q_B = 0) avec θ′ ≥ min(θ,1) : le résultat est garanti par le théorème du papier avant toute expérience. Le Duel 3 ne teste véritablement quelque chose que dans la zone q_B > 0 avec θ′ < min(θ,1), dont C ne démontre pas la plausibilité dans l'organisme. Le « contrôle inerte » à θ′ = 2,5 ne fait que vérifier qu'un texte aléatoire n'est pas fertile — une confirmation de la calibration du juge, pas du sort optimal des brouillons.

### 4. Fuite entre construction et évaluation de l'estimateur spectral

C propose d'étalonner l'estimateur ρ̂(K) sur des matrices synthétiques à ρ = 0,95 et ρ = 1,05, puis d'utiliser ce même estimateur dans les Duels 1–3 et dans P5/P7. Or les matrices synthétiques doivent être choisies pour ressembler à la matrice réelle de l'organisme — ce qui nécessite de connaître sa structure (creuse ou non, nombre de types, connexité). Cette structure ne sera connue qu'après l'audit du code de l'orchestrateur (étape 1.(i)). Si l'étalonnage est fait sur des matrices trop régulières (pleines, connexes, types peu nombreux), la couverture nominale de ρ̂ ne sera pas transférable. C ne discute pas ce risque de fuite par le choix des matrices d'étalonnage.

## (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

1. **Duel 1 (stérilité)** : si la prévalence des fiches vraies dans la population est très faible (F/N < 0,1, illustratif), le nombre de paires vraie–vraie tirées en 100 fusions (illustratif) sera de l'ordre de 1 ou 0. La puissance du test sur q_vv tombe à zéro. Plus précisément : sous tirage uniforme dans une population de N = 6 fiches dont F = 1, la probabilité de tirer une paire vraie–vraie est F(F−1)/(N(N−1)) = 0 si F = 1. Le Duel 1 n'est jugeable que si le protocole force un nombre minimal de paires par type, ce qui exige un tirage stratifié — qui viole la division aveugle.

2. **Duel 2 (neutralité de τ)** : le test exact de Fisher au seuil α = 0,05 sur l'écart τ_vv − τ_ff perd toute puissance si le nombre total de fusions observées par type de paire est inférieur à environ 30 (illustratif). Dans la course 2 à 72 fusions (24 × 3 bras), le nombre de fusions entre deux parents dont le statut vrai/faux est connu avec certitude dépend du taux d'erreur du juge. Si VP − FP = 0,25 (juste au-dessus du seuil de C), la classification erronée d'environ 37 % des paires rend le test non jugeable. En termes de paramètres : P(non-jugeabilité du Duel 2) → 1 quand (VP − FP) × min(n_vv, n_ff) < 15 (illustratif).

3. **P7 (allumage endogène)** : si l'injection exogène ne peut pas être séparée de l'allumage endogène dans le code (par exemple parce que l'orchestrateur injecte des concepts dans chaque lot, ou parce que le bisociateur puise dans un corpus externe à chaque appel), P7 n'a pas d'estimand défini. C ne traite pas cette condition : il la suppose résolue par l'audit du code.

4. **P10 (H2)** : la certification par arithmétique d'intervalles à 300 bits échoue dès que la marge minimale est inférieure au pessimisme d'enveloppe de l'arithmétique d'intervalles. C le mentionne (« un échec de certification ne réfute pas H2 »), mais il ne dit pas que la difficulté estimée « MODÉRÉE À DIFFICILE » implique qu'un résultat négatif est le résultat le plus probable pour les 3 boîtes restantes (qui restent précisément parce qu'elles ont résisté à la certification). L'asymétrie du test est correctement signalée, mais la probabilité a priori d'un résultat informatif est faible et non estimée.

## (c) Contrôles négatifs dont l'absence serait fatale

1. **Absence fatale : deux juges de provenance distincte.** Sans ce contrôle, la mesure de q_vv est un artefact du couple (bisociateur, juge), pas une propriété du processus (voir (a)2 ci-dessus). C propose un seul juge avec vérification mécanique, mais pas de second juge. L'absence de ce contrôle invaliderait l'ensemble des Duels 1 et 2.

2. **Absence fatale : bras « aucun parent » dans le Duel 1.** C inclut un bras fausse–fausse mais pas un bras sans aucun parent (fusion à vide ou avec un texte purement procédural). Ce bras mesure le taux de base de production de fiches classées « vraies » par le juge en l'absence de tout contenu parental informatif. Son absence rendrait impossible la distinction entre q_ff > 0 (génération spontanée réelle) et FP du juge.

3. **Absence fatale : contrôle de la stabilité temporelle des paramètres.** C mentionne un test de tendance en passant (synthèse, section 1.2 : B-T2 (c)5 → C-T3 §4) mais ne l'inclut pas dans ses Duels. Si q_vv dérive pendant les 100 fusions du Duel 1, le q_vv estimé est un mélange de valeurs non stationnaires, et la comparaison avec le seuil 1/2 n'a plus de sens. Un contrôle de stationnarité (par exemple un test de Mann-Kendall sur les lots successifs) est un préalable aux Duels 1 et 2.

---

# Sur la proposition D (Kimi K3.1 Pro)

## (a) Défauts de méthode

### 1. Sous-spécification systématique des seuils et des métriques

D classe P5, P7, P8 et P10 comme (S), mais les seuils opérationnels restent sous-spécifiés au point de reporter l'intégralité du travail de conception au préenregistrement. Par exemple :
- P5 est signée avec seuil Δρ = 0 et estimateur étalonné, mais D ne spécifie pas la taille minimale d'effet détectable, le nombre de lots par bras, ni la puissance visée. Le seuil 0 est un seuil théorique, pas un seuil opérationnel : aucun estimateur à variance finie ne distingue Δρ = 0,001 de Δρ = 0 aux effectifs envisagés.
- P7 est signée « sous réserve que l'audit permette de séparer toute injection exogène ». D traite cette réserve comme une condition binaire (séparable ou non), mais en pratique l'injection peut être partielle, graduelle ou implicite (le bisociateur utilise un corpus externe), auquel cas P7 n'a pas d'estimand net. D ne propose aucun critère mesurable pour trancher le cas intermédiaire.
- P8 est classée « S conditionnelle », ce qui n'est pas un statut défini par la question. Le conditionnel porte sur « validation du noyau littéral à θ = 1 », mais D ne dit pas quel test valide le noyau.

Le défaut transversal est que D refuse de spécifier avant l'audit du code, ce qui est méthodologiquement correct en principe, mais le résultat est que ses prédictions (S) ne sont pas réellement signables : elles sont des engagements de forme, pas de contenu.

### 2. Le duel déterministe sur n est vrai par construction

D propose un duel H_A (n = 3) contre H_B (n = 6) tranché par « concordance exacte entre le code et des traces synthétiques ». Le seuil est « une seule divergence réfute la règle candidate ». Ce duel n'est pas une expérience : c'est une lecture du code. En tant que tel, il est correct et nécessaire, mais le présenter comme un duel au sens B4 (deux hypothèses exclusives dont chaque issue falsifie quelque chose) est trompeur, parce que le résultat le plus probable — « toute autre règle falsifie les deux identifications fixes » — ne tranche rien. Il confirme seulement que n n'est pas identifiable, ce que D maintient déjà. Le duel n'a de contenu que si l'espace des règles possibles se réduit à {n = 3, n = 6}, ce qui n'est pas établi.

### 3. Traitement asymétrique de P12

D classe P12 comme « S, hors papier » et la conserve explicitement dans le tableau, alors qu'elle ne dérive d'aucun théorème du papier [VÉRIFIÉ, synthèse, section 4, P12]. Cela crée une confusion entre deux objets distincts : la validation du transfert des théorèmes (objet du collisionneur) et l'ingénierie de la pince/arène. En gardant P12 dans la liste des prédictions signées, D introduit un résultat qui sera compté dans le bilan du collisionneur mais qui ne peut ni confirmer ni réfuter le papier. Ce n'est pas une fuite entre construction et évaluation au sens strict, mais c'est une contamination du verdict par un objet étranger au protocole.

### 4. Absence de spécification du contrôle positif dans les instruments

D fournit une table d'instruments avec des contrôles mécaniques à battre, mais ne spécifie aucun contrôle positif interne. Pour le juge de vérité, par exemple, D propose « re-calculs, tests unitaires, vérification de schéma ou de preuve lorsqu'ils existent » comme contrôle mécanique, mais aucun cas où le juge doit réussir de manière certaine (par exemple : paire de fiches identiques, dont la fille doit être classée « vraie » avec probabilité ≥ 0,99). Sans contrôle positif, on ne peut pas distinguer un juge qui échoue (FP ≈ FN ≈ 0,5) d'un juge qui refuse de répondre.

## (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

1. **P5 (vivier contre quarantaine)** : si l'estimateur spectral ρ̂ a une erreur-type σ_ρ̂ au nombre de lots G, alors le test Δρ = 0 au seuil α = 0,05 avec puissance 0,80 nécessite |Δρ_vrai| ≥ 2,8 σ_ρ̂ (illustratif, test bilatéral). D ne spécifie ni G ni σ_ρ̂, et donc le domaine de non-jugeabilité n'est pas borné. Si σ_ρ̂ ≥ 0,10 (ce qui est plausible à G = 10 lots avec des tailles de lot de 6), P5 ne détecte rien en dessous de |Δρ| = 0,28 (illustratif). D devrait spécifier la taille minimale d'effet pour laquelle P5 est informative.

2. **P7 (allumage endogène)** : P7 perd toute puissance si l'injection exogène et la production endogène ne sont pas séparables dans le code. Condition formelle : soit I le nombre de fiches injectées par tour et E le nombre de fiches produites par fusion. P7 n'est jugeable que si I = 0 ou si I et E sont observables séparément dans les journaux. D reconnaît cette condition (« sous réserve que l'audit permette de séparer ») mais ne dit pas quoi faire si elle n'est pas remplie — ce qui est le cas le plus probable si le bisociateur puise implicitement dans un corpus externe.

3. **P8 (conditionnelle au noyau validé)** : la condition « noyau littéral validé à θ = 1 » n'est pas un estimand. Quel test, à quel seuil, avec quelle puissance, valide-t-on le noyau ? Si la validation du noyau est elle-même une hypothèse composite (tirage uniforme, retrait indépendant, division aveugle, stérilité des paires mixtes, non-consommation, budget RF), la probabilité de la valider intégralement est le produit des probabilités de valider chaque composante, et elle peut être très faible. P8 est alors presque sûrement inapplicable, ce qui en fait une prédiction non réfutable de facto.

4. **P10 (H2)** : identique à C. Le résultat le plus probable est l'échec de certification, qui n'est pas informatif. D ajoute la recherche de contre-exemple par optimisation globale, mais ne quantifie pas la puissance de cette recherche (taille de l'espace, finesse de la grille, durée nécessaire).

## (c) Contrôles négatifs dont l'absence serait fatale

1. **Absence fatale : test de stationnarité dans le régime gelé de l'arène.** D admet un « régime local gelé » pour l'arène et propose un duel H_A (noyau stationnaire) contre H_B (dérive persistante). Mais le contrôle négatif (« chronologie permutée dans un simulateur stationnaire ») ne teste que la sensibilité du test de dérive, pas la stationnarité du régime gelé réel. Il manque un contrôle sur le fait que le gel est effectif : par exemple, vérifier que les poids du modèle, les invites et le budget de jetons n'ont pas été modifiés entre le début et la fin de l'expérience. Sans ce contrôle, une dérive observée pourrait être un artefact de l'infrastructure (mise à jour silencieuse de l'API, changement de routage du modèle), pas une propriété du noyau.

2. **Absence fatale : contrôle de l'indépendance des deux modèles ouverts.** D propose « deux modèles ouverts de provenance distincte, l'un ne servant pas automatiquement de juge à l'autre ; leur indépendance d'erreur doit être mesurée, non présumée ». C'est correct en principe, mais D ne propose pas de méthode pour mesurer cette indépendance. Un contrôle négatif serait de soumettre les mêmes paires aux deux modèles et de tester la corrélation de leurs erreurs de classification sur des cas à vérité plantée. Sans ce contrôle, l'affirmation d'indépendance est une hypothèse, pas un résultat.

3. **Absence quasi-fatale : bras « aucun parent » dans le duel trans/cis.** D propose des contrôles « aucun parent, deux fiches fausses et rembourrage inerte de même longueur » mais les groupe comme des contrôles négatifs sans les distinguer opérationnellement. Le bras « aucun parent » (pas de fiches du tout soumises au bisociateur, seulement un prompt procédural) est nécessaire pour mesurer le taux de base de production de texte classé « vrai » par le juge en l'absence de tout contenu. Le bras « rembourrage inerte » mesure autre chose : la production de texte classé « vrai » en présence de contenu non informatif. Les confondre empêche de distinguer le biais du juge (taux de faux positifs pur) du biais du bisociateur (capacité à produire du contenu apparemment vrai à partir de rien).

FIN-DE-CELLULE