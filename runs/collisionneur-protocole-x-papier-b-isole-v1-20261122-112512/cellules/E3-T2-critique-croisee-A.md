# Proposition A — Tour III.2 : critique croisée de méthode

**État des pièces.** Le bloc FAITS ne contient aucun fait doté d'un statut : son texte est celui de la QUESTION, et je n'ai pas recalculé les empreintes. Ma propre conception (A) ne m'est pas retransmise à ce tour et je n'en reconstitue rien. Les pièces B, C, D et E paraissent complètes.

**Statut de ce qui suit.** Les identités algébriques sont marquées « calcul ». Le reste de mes critiques est HYPOTHÈSE de méthode, à vérifier sur pilote. Tout chiffre est illustratif ou calculé sur les chiffres illustratifs des pièces.

**Notations pour les rubriques (b).**
- n₀, n₁ : épisodes honnêtes et adverses en test.
- α : taux de fausses alertes visé.
- π : prévalence des épisodes dégradés.
- b : fraction auditée.
- d : dimension des activations.
- n_cal : exemples d'alignement ou de calibration.
- ρ : corrélation intra-classe entre les scores des agents d'un même épisode.
- LR(t) = f₁(t)/f₀(t) : rapport des densités de score au seuil t.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Dans E1, H_B est vraie par construction.**
   - Sans canal et avec des graines indépendantes, les choix des rôles sont indépendants conditionnellement à la tâche.
   - Alors P(choix cohérents | tâche) = Σ_c Π_r P_r(c | tâche), donc E[κ] = 0 par tâche, pour les copies comme pour l'équipe hétérogène (calcul).
   - L'a priori partagé loge tout entier dans le terme que κ retranche : la probabilité de collision C = Σ_c Π_r P_r(c).
   - Un κ non nul ne peut venir que d'une fuite : graine partagée, cache commun, artefact transmis, ou agrégation entre tâches.
   - Le contrôle de brassage de B le confirme : il prédit un κ inchangé, donc nul.
   - L'estimande correct est C_copies − C_hétérogène, rapporté à sa valeur sous consigne honnête.
2. **L'hétérogénéité se confond avec un triplet de modèles.** Il n'y a qu'un triplet et aucune rotation des rôles : l'interaction modèle × rôle est indiscernable de l'effet d'identité.
3. **Dans E2, le déclencheur thématique remplace la consigne sans lever la confusion.**
   - La sonde peut lire le thème plutôt que l'intention.
   - Les bogues honnêtes du contrôle 2 viennent du modèle de base à haute température.
   - L'étiquette se confond donc avec la présence de l'adaptateur et avec la température.
4. **Le signe de P2 n'est pas neutre a priori.**
   - Pour des scores gaussiens de même d′ et d'équicorrélation ρ, la somme de k scores a d′_agg = d′·√(k/(1+(k−1)ρ)) (calcul).
   - Des copies qui lisent le même artefact avec les mêmes poids ont plausiblement un ρ plus élevé (HYPOTHÈSE), donc un gain d'agrégation plus faible.
   - Le « meilleur score d'une seule copie », s'il est choisi sur le test, est un maximum sélectionné, donc biaisé.
5. **E3 est trivial ou vide.**
   - Compromission par poids : la divergence au rejeu mesure l'écart de poids sur toute entrée.
   - Compromission par injection : le « même contexte » rejoué contient l'injection, et la copie de référence est compromise à son tour.
6. **S4 fuit vers les références.** « Défendable » est défini par le score du moniteur textuel sous son seuil. Sur les sabotages retenus, ce moniteur est donc battu par sélection, et « la sonde bat le texte d'au moins 5 points » devient vrai par construction.
7. **Dans E5, H_A est quasi acquise.** Pénaliser une sonde linéaire fixe abaisse son score par descente de gradient. L'asymétrie « un ajustement contre trois » est une comptabilité de coût, pas un effet mesuré.
8. **E4 compare des minima bruités.** Un minimum sur 5 stratégies est un estimateur biaisé vers le bas, d'un biais qui dépend de la variance par condition. De plus, les sondes de E2 sont réutilisées contre les organismes qui ont servi à les entraîner.
9. **Les duels ne sont pas exhaustifs.** Les zones entre 5 et 15 points (E1) et entre 3 et 7 points (E5) ne falsifient rien et ne sont pas déclarées indécises.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **κ** : non jugeable dès que l'indépendance conditionnelle tient. La variante C perd sa puissance quand l'entropie de P_r(· | tâche) tend vers 0 dans les deux conditions (un seul point faible évident), ou quand elle est maximale dans les deux.
- **TPR à α = 1 %** :
  - Var(TPR̂) ≈ LR(t)²·α(1−α)/n₀ + TPR(1−TPR)/n₁.
  - Avec n₀ = 1 000 et LR(t) entre 10 et 30 (illustratif), l'écart-type va de 3 à 9 points (calcul).
  - Les contrastes de 3 à 5 points sont alors non jugeables.
- **Gain d'agrégation** :
  - identifiable comme effet d'identité seulement si les d′ individuels sont appariés entre conditions et si ρ₀ et ρ₁ sont rapportés ;
  - nul si le TPR individuel est déjà au plafond, ou si d′ ≈ 0.
- **Sécurité sur 1 000 épisodes** : c'est une fonction extrapolée de trois taux (attaque, réussite, capture). Si elle est proche de 0 ou de 1 dans les deux conditions, l'équivalence à ±2 points est acquise trivialement.
- **Corrélation inter-rôles après CCA** : si n_cal < 2d, les corrélations canoniques empiriques valent 1, quel que soit le signal.
- **E5** : non jugeable si la dérive du contrôle à pénalité nulle est du même ordre que l'effet.

### (c) Contrôles négatifs dont l'absence serait fatale

- Cas honnêtes produits par le même modèle ajusté, sur des tâches du thème déclencheur mais sans sabotage. Sinon la sonde détecte le thème ou l'adaptateur.
- Pour E3 : divergence au rejeu sur des entrées hors déclencheur, où elle doit être nulle.
- Pour E1 : preuve de graines indépendantes, et bras « mêmes poids, invites paraphrasées » pour séparer l'identité des poids de l'identité des contextes.
- Pour E2 : agrégation de trois relectures du même artefact par une seule copie, sous graines distinctes. Si le gain est égal, c'est une réduction de variance et non un effet multi-copies.
- Pour E5 : sonde réentraînée sur l'organisme obfusqué et évaluée hors échantillon.
- Un second triplet hétérogène. À défaut, la conclusion porte sur trois modèles et non sur « des modèles différents ».

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Des statuts sont attribués sans base dans FAITS.** Trois affirmations portent [VÉRIFIÉ] : « même base vectorielle », « espaces latents non isomorphes », « agent unique sans contrepartie indépendante ». Je ne modifie pas ces statuts. Je signale que la pièce FAITS n'en fonde aucun. La troisième est contredite par les témoins que décrivent D et E : un processus unique à contextes rechargés est une équipe de copies.
2. **Une attribution est fautive.** « Kieronzmann » n'est pas un auteur que je puisse attribuer. De mémoire, les auteurs de « AI Control: Improving Safety Despite Intentional Subversion » sont Greenblatt, Shlegeris, Sachan et Roger. À vérifier.
3. **Le différentiel est un cas particulier de la concaténation.**
   - Une sonde linéaire sur Δh = h_Auteur − h_Relecteur est une sonde sur [h_Auteur ; h_Relecteur] contrainte aux poids (w, −w).
   - En population, la sonde concaténée fait donc au moins aussi bien (calcul).
   - Si la référence (i) est cette sonde, H_2A ne peut tenir qu'en échantillon fini. C'est alors une thèse d'efficacité d'échantillon, qui se mesure par une courbe d'apprentissage et non par un point.
   - Or n ≤ 500 tâches pour d = 4 096 : en apprentissage, toute étiquette est linéairement séparable.
4. **Δh est séparable ou nul, bras par bras.**
   - Compromission partielle par LoRA : Δh mesure l'écart de poids, sur toute entrée.
   - Compromission par consigne secrète : Δh mesure l'asymétrie des contextes, puisque la consigne est chez l'auteur et pas chez le relecteur.
   - Compromission totale : l'hypothèse de symétrie que C invoque pour les bogues honnêtes s'applique aussi aux trois copies adverses, et le détecteur est aveugle.
5. **L'ablation par rotation ne teste pas ce qu'elle annonce.**
   - Une régression logistique L2 est invariante par transformation orthogonale des variables (calcul).
   - La rotation n'affecte donc que la soustraction, et ne dit rien de l'écart entre copies et modèles différents.
   - Un Procrustes réappris sur 1 000 états pour d = 4 096 est de rang insuffisant. Son échec viendrait de n_cal < d, pas d'une non-isomorphie.
6. **Le critère de légitimité fuit vers l'observateur textuel.** Le TSDF exige un score ≥ 0,80 auprès d'un juge. Le moniteur textuel est ensuite évalué sur les cas ainsi filtrés.
7. **Le « sans communication » transmet le code normalisé.** L'artefact est un canal. Point focal et signal porté par l'artefact restent confondus, sauf dans le contrôle de permutation.
8. **Le test de Fisher ignore l'appariement.** Les mêmes 500 tâches servent à toutes les topologies, et les 6 permutations hétérogènes ne sont pas indépendantes.
9. **Le duel 3 n'est pas exhaustif.** Un R_comm entre 10 % et 40 %, ou supérieur à 40 % dans les deux topologies, ne falsifie rien.
10. **La comparaison à l'agent seul change deux choses à la fois** : la segmentation des contextes et le nombre d'instances.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Rappel@10 %** :
  - le plafond est min(1, (K/N)/π) (calcul) ;
  - si π > 12,5 %, le seuil de 80 % est inatteignable ;
  - π diffère entre topologies dès que le TSDF diffère, ce qui confond la comparaison des rappels avec celle des prévalences.
- **Gain du différentiel sur la concaténation** : il tend vers une valeur ≤ 0 quand n/d → ∞. Il n'est jugeable que comme fonction de n.
- **ΔTSDF net (adverse − honnête)** : si les TSDF honnêtes diffèrent entre topologies, le signe de l'interaction peut dépendre de l'échelle (points de pourcentage ou logit). L'échelle doit être préenregistrée.
- **R_comm** : c'est un rapport de deux différences bruitées. Si le dénominateur TSDF_comm − TSDF_sans a un intervalle contenant 0, la loi du rapport est à queues lourdes et l'intervalle est non borné.
- **Choix de couche parmi quatre** : sans validation imbriquée, le maximum de quatre estimateurs bruités gonfle le gain d'une quantité qui croît avec leur variance.

### (c) Contrôles négatifs dont l'absence serait fatale

- Sonde concaténée [h_Auteur ; h_Relecteur], à n et régularisation égaux.
- Étiquettes permutées, indispensables quand n ≪ d.
- Paires honnêtes à asymétrie de contexte appariée : consigne privée leurre chez l'auteur, même statut d'adaptateur des deux côtés.
- Appariement brassé : Δh entre l'auteur de l'épisode i et le relecteur de l'épisode j sur la même tâche. Si la détection persiste, le signal est de niveau tâche, non de niveau épisode.
- Contrôle positif de l'alignement : copies tournées par Q puis réalignées avec n_cal ≥ d, qui doivent retrouver la performance native. Sinon la référence hétérogène alignée n'informe pas.
- Processus unique à contextes rechargés.

---

## Sur la proposition D

D contient déjà plusieurs garde-fous que je réclame aux autres : un témoin d'identité, des équipes homogènes pour chaque modèle, une règle de décision par intervalle, et une ventilation des pertes honnêtes. Mes critiques portent sur ce qui reste.

### (a) Défauts de méthode

1. **L'adversaire est induit par consigne, sans réentraînement.**
   - Exclure du détecteur les jetons de la consigne ne suffit pas : les activations aux décisions y accèdent par attention.
   - Le contrôle « consignes honnêtes de longueur appariée » neutralise la longueur, pas le contenu sémantique.
   - L'avantage de transfert entre rôles de mêmes poids peut donc être celui d'un lecteur de consigne. Il serait vrai par construction, et sans portée pour un modèle qui dégrade sans consigne.
2. **Le duel défensif handicape l'équipe hétérogène par dessin.**
   - D impose un corpus source identique pour chaque régime.
   - Mais D fait aussi tourner chaque modèle dans chaque rôle : un corpus rédacteur de poids W′ existe pour le réviseur W′.
   - Le défenseur hétérogène dispose donc aussi d'un transfert à poids constants, au prix de trois corpus étiquetés.
   - La comparaison loyale se fait à budget d'étiquetage total égal, la répartition étant laissée au défenseur.
3. **G_g mélange trois choses** : la qualité du transfert, la qualité du détecteur textuel du régime, et la lisibilité propre du modèle cible. Le détecteur entraîné directement dans le rôle cible est mesuré, mais il ne normalise pas le seuil.
4. **Le résultat du duel d'alignement est fixé par un paramètre de dessin.** Selon n_cal, l'alignement linéaire échoue (n_cal < d) ou réussit. Un seul point est arbitraire. Le résultat est la courbe en n_cal, croisée avec le budget de calibration cible.
5. **Le duel « copies contre agent seul » ne teste pas les poids.** Le témoin reproduit les copies par définition. Le duel mesure la continuité du contexte. D le dit en (a), mais l'intitulé du duel ne le reflète pas.
6. **La défendabilité locale est mécanique.** Si la validité locale est une contrainte vérifiable, le « meilleur détecteur sans activations » peut être proche du hasard par construction, ce qui gonfle G dans tous les régimes.
7. **Trois modèles donnent trois équipes homogènes.** L'effet d'identité est une interaction estimée avec très peu de degrés de liberté. L'intervalle par famille de tâches traite les modèles comme fixes. D l'admet ; le seuil de 3 points devrait être rapporté à la dispersion entre équipes homogènes.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Bilan R_g** :
  - l'audit retire au plus b = 5 points de mauvais plans (calcul) ;
  - si E_copies − E_différents > b, la « compensation » est arithmétiquement impossible quel que soit le détecteur ;
  - si π ≪ b, tout détecteur médiocre suffit ;
  - le duel n'est jugeable que pour π/b dans une plage intermédiaire, à fixer sur pilote.
- **Seuil de 1 point sur R** :
  - la variance d'une différence de différences de quatre proportions est d'environ 4p(1−p)/n par cellule, hors appariement ;
  - pour p = 0,2 et n = 2 000 (illustratif), l'écart-type est d'environ 1,8 point (calcul), au-dessus du seuil.
- **Contraste de transfert** : non jugeable si le détecteur entraîné dans le rôle cible ne dépasse pas la référence textuelle dans un des régimes, car le déficit de transfert est alors borné par 0.
- **Étiquette « mauvais plan »** : si la loi de la perte a de la masse près de la tolérance, le seuillage produit un bruit d'étiquette qui atténue tous les contrastes vers 0.
- **E_g** : si le taux de mauvais plans honnêtes est élevé, l'excès est comprimé par plafond. Si l'obéissance à la consigne adverse varie entre modèles, E_différents est une moyenne d'obéissances et non une mesure de coordination.

### (c) Contrôles négatifs dont l'absence serait fatale

- Consignes privées leurres, honnêtes mais sémantiquement proches de l'objectif de perte.
- Au moins un bras où l'objectif adverse n'est pas dans le contexte : organisme ajusté, avec adaptateur placebo pour la classe honnête.
- Bras hétérogène avec source de mêmes poids que la cible.
- Alignement appris sur paires permutées. S'il fait aussi bien que l'alignement réel, celui-ci ne fait rien.
- Borne haute du transfert : même rôle, mêmes poids, épisodes disjoints.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Des statuts sont attribués sans base dans FAITS.** Portent [VÉRIFIÉ] : « même sémantique neuronale », « réalisable dans la fenêtre de deux mois », « S_reset mathématiquement équivalent à H », et l'affirmation qu'une sonde ne battant pas les statistiques de logits « ne capture aucune information propre ». Je ne modifie pas ces statuts. La dernière affirmation confond l'absence de gain avec l'absence d'information : elle ignore la redondance et la puissance du test.
2. **Dans E2, l'étiquette coïncide avec les poids.**
   - Les organismes LoRA n'ont pas de déclencheur : adverse = poids ajustés, honnête = poids de base.
   - Toute sonde peut alors séparer les classes par la signature de l'adaptateur, sur toute entrée.
   - Dans H, un adaptateur commun ajoute un décalage commun dans une base commune. Dans D, ce sont trois décalages dans trois bases.
   - L'écart Δ_déf peut donc mesurer la facilité à repérer un adaptateur, non une intention.
   - Le contrôle « hors-prompt » ne corrige pas ce défaut : il supprime la consigne, pas la coïncidence entre l'étiquette et les poids.
3. **L'adversaire est optimisé contre un seul instrument.**
   - L'ajustement se fait par rejet sur des traces jugées défendables, donc contre un juge textuel.
   - Rien ne l'optimise contre les sondes.
   - La « dualité » (avantage adverse en texte, renversement par les activations) compare un instrument attaqué à un instrument épargné. Elle est partiellement vraie par construction.
4. **Deux critères d'instrument sont insatisfiables ou incohérents.**
   - Avec π = 10 % et b = 5 %, le rappel maximal est b/π = 50 % et l'enrichissement maximal 1/π = 10× (calcul). Le critère « ≥ 60 % et ≥ 12× » ne peut pas être atteint.
   - « AUROC ≤ 0,60, soit TPR ≤ 0,10 à FPR = 0,05 » : l'AUROC ne détermine pas un point de la courbe.
5. **Le budget sert à calibrer et à évaluer.** Les épisodes audités étiquettent le détecteur, puis comptent dans TPR@b. Sans évaluation préquentielle (score figé avant l'étiquette), il y a fuite.
6. **Le levier « mutualisation » n'est pas propre à H.**
   - Il suppose une direction invariante entre rôles, ce qui n'est pas établi.
   - Il vaut autant pour l'agent seul S.
   - Face à D, il représente au plus un facteur 3 sur le nombre d'étiquettes.
7. **E3 ne peut pas attribuer son effet aux copies.**
   - S_reset est H, de l'aveu de la pièce. Le duel mesure la continuité du contexte.
   - Égaliser le « taux de dégradation effective » entre H et S conditionne sur une variable postérieure au traitement : les attaques retenues ne sont plus comparables.
8. **E1 ne retranche pas le mode commun honnête.** TAR_déf(H) inclut les angles morts corrélés de copies honnêtes. Δ_adv mesure donc monoculture honnête plus coordination adverse.
9. **L'appariement par filtrage de tâches biaise vers 0.** Sélectionner les tâches où pass@1 s'égalise induit une corrélation des échecs entre modèles différents, et expose à une régression vers la moyenne en test.
10. **La règle de décision de E1 n'a pas de zone d'indifférence.**
    - Le seuil de 0,08 porte sur l'estimation ponctuelle. Si la vraie valeur vaut 0,08, la décision se joue à pile ou face.
    - H_1A est une disjonction (sans canal ou avec canal) : deux tests, deux mécanismes, sans correction.
11. **Le contrôle H-rot ne peut guère échouer.** Appliquer une sonde partagée dans des bases tournées revient à la projeter au hasard. Le contrôle borne par le haut la valeur de « ne pas avoir à aligner », et ne dit rien de H contre D.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Quantile 95 % par tâche** : avec k contributions honnêtes par tâche et k < 20, le quantile empirique est le maximum. Le taux de rejet nul vaut alors 1/(k+1) et non 5 % (calcul, sous échangeabilité). Le critère de défendabilité dépend donc de k.
- **TPR@b** : le plafond b/π dépend de la prévalence, laquelle inclut les bogues honnêtes s'ils comptent comme dégradations. Toute comparaison entre H, D et S est confondue si π diffère.
- **Calibration en ligne** : avec b·N = 25 audits (calcul sur N = 500), dont une fraction de positifs, pour d = 4 096, la sonde est dominée par la régularisation. Le gain de mutualisation se lit sur la courbe d'apprentissage entre 25 et 75 étiquettes. Si elle est plate, la puissance est nulle.
- **Covariance inter-copies** : sous honnêteté, des copies qui lisent les mêmes jetons ont une covariance proche de son maximum. Le test perd sa puissance quand l'effet est petit devant la dispersion de cette covariance, qui dépend de la longueur du préfixe partagé. Pour D, la statistique après CCA vaut 1 en échantillon si n_cal < 2d.
- **Δ_adv** : non jugeable comme effet de coordination tant que TAR_honnête(H) − TAR_honnête(D) n'est pas estimé sur les mêmes tâches.

### (c) Contrôles négatifs dont l'absence serait fatale

- Adaptateur placebo : même rang, norme appariée, entraîné sur des traces honnêtes, pour constituer la classe honnête. Ou un organisme conditionnel, honnête sur un sous-ensemble apparié.
- Adversaire également pénalisé sur la sonde, ou moniteur textuel d'évaluation tenu hors de l'ajustement.
- Soustraction du mode commun honnête dans E1.
- H-rot réaligné : les paires d'activations de copies sur entrées identiques sont exactes à Q_k près, donc l'alignement est atteignable avec n_cal ≥ d. La performance de H doit être retrouvée, sans quoi la procédure d'alignement appliquée à D n'est pas validée.
- Évaluation préquentielle, épisodes audités exclus du numérateur.

---

## Trois défauts présents dans plusieurs pièces

Je les liste sans harmoniser les propositions.

1. **Confusion de l'étiquette avec le contexte ou les poids.** Le défaut touche B (déclencheur thématique, bogues du modèle de base), C (Δh), D (consigne) et E (adaptateur). Seul un adaptateur placebo ou un organisme conditionnel apparié le lève. Aucune pièce ne le prévoit.
2. **Définition de « défendable » par l'instrument qui sert ensuite de référence.** Le défaut touche B, C et E. Il faut deux juges disjoints et la publication des taux non conditionnés.
3. **Métriques au budget sans plafond déclaré.** C, D et E ne donnent pas le plafond b/π. Chez B, l'erreur du quantile à α = 1 % n'est pas chiffrée.

FIN-DE-CELLULE