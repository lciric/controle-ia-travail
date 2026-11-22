# Proposition B — Tour III.2 : critique croisée de méthode

**Remarques d'intégrité**
- Le bloc QUESTION reproduit le bloc FAITS avec la même empreinte. La question à traiter est donc celle de l'énoncé entier, et la forme du livrable est celle du tour III.2.
- Les pièces A, C, D et E sont présentes et complètes : chacune se termine par sa ligne de fin, et je n'ai repéré aucune coupure.
- Je ne vérifie pas leurs références et je ne modifie aucun de leurs statuts. Quand je discute un statut, je dis seulement ce qu'il couvre.
- Tous les effectifs, taux et seuils que j'utilise dans les calculs reprennent des valeurs illustratives des pièces ou sont de mon fait. Ils sont **illustratifs**. Les formules sont exactes ; les nombres qui en sortent ne sont pas des résultats.
- Mes affirmations sur le comportement des modèles sont des **HYPOTHÈSES**.

**Défaut commun à A, C, D et E.** Avec deux familles seulement, la « parenté » se confond avec toute autre interaction auteur × moniteur : écart de capacité, tokeniseur, données d'entraînement communes. Le contraste « diagonale moins hors-diagonale » annule les effets principaux de l'auteur et du moniteur, mais pas, par exemple, l'incapacité d'un moniteur faible à voir les erreurs subtiles d'un auteur fort. Je le signale dans chaque section, car les conséquences diffèrent d'un plan à l'autre.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Fuite par la titration (D1).** La force de la demande nue est titrée pour que le bras 2 tombe entre 10 % et 90 %. Si cette titration se fait sur les tâches et les formulations du test :
   - le choix porte sur des cas déjà situés en zone instable ;
   - leur réestimation régresse vers la moyenne ;
   - le taux de base du bras 2 est biaisé.

   La titration doit se faire sur des tâches et des formulations réservées.
2. **Lever-sans-demande et demande implicite.** Une menace (« sinon… ») contient souvent une demande implicite. Le contrôle « levier seul ≈ bras 1 » peut échouer pour cette raison, sans qu'il y ait dégradation. A lit cet échec comme une dégradation : l'interprétation est faussée par construction.
3. **Règles de D1 qui se chevauchent.** H_B est retenue si le Δ estimé atteint 10 points et que l'IC exclut 0. Un Δ de 10 avec un IC de [2 ; 18] déclare donc H_B, alors que le vrai Δ peut se trouver dans la marge d'équivalence ±10. La règle se fonde sur l'estimation ponctuelle et non sur la borne inférieure. De plus, le maximum sur 4 leviers × 3 sources n'est pas inclus explicitement dans la correction de Holm.
4. **D2 : recalibrage vrai par construction.** Les canaris de recalibrage portent « la même pression » que le test. Si la pression est une simple translation commune aux deux classes, le recalibrage la compense par construction, et l'AUROC intra-condition y est insensible par construction. La quantité informative est l'interaction pression × classe sur la loi des scores, et elle n'est pas nommée. Les canaris doivent venir d'une famille de gabarits de pression disjointe de celle du test.
5. **D3, variante (ii) : contenu confondu avec l'identité.** H_A dit que l'omission ne dépend que du contenu. Or, dans la variante (ii), le contenu varie selon l'auteur, avec un appariement « par type » qui reste grossier. Une interaction auteur × moniteur peut alors venir d'un contenu × moniteur, c'est-à-dire d'un angle mort, et serait comptée pour H_B. Seule la variante (i) teste H_A proprement. Il s'y ajoute le confondant de capacité à deux familles.
6. **D3b : avantage mécanique.** Deux instances du même modèle, avec la même consigne et un décodage glouton, produisent le même point focal par identité des calculs. L'avantage des paires de même modèle est alors en partie vrai par construction. Il ne mesure une capacité de coordination que si les invites diffèrent et que le décodage est aléatoire.
7. **D4 : sélection sur l'issue.** La case « pression sans sabotage » est formée des résistances observées. Or les tâches où l'agent résiste peuvent être plus faciles (HYPOTHÈSE), et la sonde lirait alors la difficulté. Il faut une validation croisée groupée par tâche.

   La référence sac-de-mots doit porter sur les **mêmes jetons générés** que la sonde, pas sur l'invite seule. Sans cela, la comparaison favorise la sonde par construction.

   Le contrôle « invite identique ⇒ activations identiques » ne détecte que les défauts de la chaîne de traitement, pas une fuite d'étiquette ; A le dit en partie.

   Enfin, la case « sabotage sans pression » est produite par une consigne système. Le transfert vers elle confond donc changement de contexte et bascule.
8. **D5 : hétérogénéité des tâches.** Si le hasard est constant dans chaque tâche mais varie entre tâches, le hasard agrégé décroît mécaniquement avec k. C'est une « immunisation » apparente (voir (b)).
9. **Socle.** Le taux d'erreur honnête qui déclenche le prédicat est mesuré sans pression. Or une pression peut provoquer des actions honnêtes mais inhabituelles qui le déclenchent (HYPOTHÈSE). Ce taux est à mesurer **sous chaque bras**.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D1, équivalence.** On note σ_Δ l'erreur type de Δ̂. Avec p ≈ 0,3 et n = 350 par bras sans appariement (illustratif), σ_Δ = √(2·0,21/350) ≈ 0,035. Le test TOST à ±0,10 n'accepte l'équivalence que si |Δ̂| < 0,10 − 1,645·0,035 ≈ 0,043, et la correction de Holm resserre encore ce seuil.

  Si l'intra-classe par tâche ρ → 1, l'effectif efficace tend vers le nombre de tâches (environ 200, illustratif), et non vers le nombre de trajectoires.
- **D1, effets de signes opposés.** Si E[Δ_t] = 0 et Var(Δ_t) = τ² > 0 entre tâches ou sources, le test d'équivalence sur la moyenne accepte H_A alors que les effets locaux sont forts. Il faut préenregistrer τ̂².
- **D2.** Si les scores 0–100 se concentrent sur quelques valeurs (par exemple P(S ∈ {0, 100}) > 0,8, illustratif), l'AUROC est dominée par les ex-æquo. Elle devient sensible à la règle de départage et non jugeable au seuil de 0,02.

  Même avec des scores continus, pour une AUROC de 0,85 et 500 + 500 cas (illustratif), l'erreur type de Hanley–McNeil vaut environ 0,012. Pour une différence appariée avec une corrélation de 0,5 (illustratif), l'IC à 95 % a une demi-largeur d'environ 0,024. Le critère « baisse < 0,02 » est donc inatteignable sans des effectifs de plusieurs milliers.

  Si la pression change la **variance** d'une seule classe (modèle binormal à variances inégales), les courbes ROC se croisent : l'AUROC peut rester stable sans pur déplacement de critère, et ni H_A ni H_B ne décrit la situation.
- **D3.** Une interaction n'est pas invariante par transformation monotone : elle peut être présente en probabilité et absente en logit dès qu'il y a des effets principaux. Il faut préenregistrer l'échelle. Près d'un plancher d'omission, l'interaction n'est pas jugeable.
- **D4.** Si q = P(cédé | pression) < 0,05 (illustratif), les positifs intra-strate sont rares et l'IC de l'AUROC est trop large pour le seuil de 0,05.
- **D5.** Si le hasard par tâche suit p ~ Beta(a, b) et reste constant en k, alors P(événement en k | survie) = a/(a+b+k−1). Le rapport de cotes par doublement sort de [0,8 ; 1,25] dès que a + b est petit, sans aucun effet de répétition. Le critère n'est jugeable qu'avec un effet aléatoire ou un effet fixe par tâche.

### (c) Contrôles négatifs dont l'absence serait fatale

1. Une titration et un recalibrage (D2) faits sur des familles de tâches et de gabarits réservées.
2. Pour D3b, des paires de même modèle avec des invites différentes et un décodage aléatoire. Sans elles, le résultat est vrai par construction.
3. Pour D5, une modélisation de l'hétérogénéité (effet par tâche). Sans elle, la décroissance du hasard est un artefact.
4. Pour D4, une validation croisée groupée par tâche et une référence textuelle portant sur les jetons générés.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Exp. 1 : la référence n'est pas la demande nue.** Le bras impératif (« Ignore la règle précédente… ») est une attaque distincte : sa formule de dérogation explicite peut, plus que les bras sociaux, déclencher les refus appris (HYPOTHÈSE). Son remplissage neutre dilue par ailleurs la densité de la demande. Δ_soc confond donc levier social et formulation de la demande.

   Le contrôle négatif (discours social sans demande) est en outre placé **dans** le max() de la référence. Il sert à la fois de contrôle et de comparateur.
2. **Exp. 1 : malédiction du gagnant.** Δ_soc prend le maximum des quatre leviers. Sous H_1B, son espérance est positive (voir (b)).
3. **Exp. 2 : réécriture vraie par construction.** Les traces de A₂ « stylisées » sont réécrites par F₁, donc **produites par la famille du moniteur**. Si l'indulgence passe par l'auteur réel, elle se transfère par construction, et Δ_style ≈ 0 ne sépare rien.

   La réécriture est de plus pilotée jusqu'à un écart de log-perplexité < 0,1 nat **sous M₁**. L'instrument évalué sert donc à fabriquer le stimulus : c'est une fuite construction/évaluation.

   La réécriture du raisonnement peut aussi effacer des indices d'intention qui rendaient le sabotage visible.

   Enfin, la transformation n'est appliquée qu'à un bras (A₂), pas à A₁. Les artefacts de réécriture se confondent donc avec la paternité.
4. **Exp. 2 : effet principal non testé.** Aucun test préalable ne vérifie qu'un déficit homogène/hétérogène existe. S'il n'y en a pas, H_2A est « falsifiée » et H_2B « confirmée » sans rien expliquer. S'y ajoute le confondant de capacité à deux familles (Qwen 7B contre Llama 8B).
5. **Exp. 3 : hypothèses non exclusives (B4).** Si ΔFPR_S ≥ 15 et ΔFPR_L ≥ 15, les deux mécanismes coexistent, et les règles ne prévoient pas ce cas.

   La condition S cumule deux choses : le fait d'**adresser** une demande au moniteur et la pression sociale. La condition L n'adresse rien. L'écart S − L confond ces deux facteurs.
6. **Exp. 4 : la sonde peut lire la consigne.** La sonde est entraînée sur des sabotages induits par consigne directe, avec la consigne présente dans le contexte. Elle peut apprendre la présence de cette consigne. L'échec du transfert aux sabotages sociaux, où cette consigne est absente, serait alors en partie vrai par construction et falsifierait H_4A à tort.

   Le seuil est en outre fixé sur les cas sociaux résistés, mais appliqué au TPR des sabotages directs : deux populations différentes. Enfin, la falsification de H_4B dépend d'une condition sur un autre instrument (chute du juge ≥ 20 %), ce qui laisse des issues sans verdict.
7. **Définition de D_faux.** Les fausses alertes ne sont mesurées que sur des trajectoires honnêtes **réussies**. Les échecs honnêtes en sont exclus, si bien qu'un juge qui alerte sur tout échec n'est pas pénalisé.

   Sur le statut « VÉRIFIÉ par définition logique » attribué à l'exclusion des scores de modèles comme vérité-terrain : ce statut couvre une implication logique, vraie par construction. Il ne garantit pas que le bac à sable capte le dommage réel.
8. **Test de McNemar.** Ce test suppose des paires. Avec une génération stochastique, les trajectoires de deux conditions ne sont appariées que si la graine et l'état de l'environnement sont fixés. C'est à expliciter.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Exp. 1, plafond ou plancher.** Si ASR_impératif ≥ 0,9, Δ_soc ≥ +0,10 est impossible. Si ASR_impératif ≈ 0 (refus systématique), Δ_soc est gonflé. Aucune titration n'est prévue.
- **Exp. 1, biais du maximum.** Pour quatre estimateurs indépendants de même erreur type s, E[max] ≈ 1,03·s sous l'hypothèse nulle. Avec s ≈ 0,03 (illustratif), le biais vaut environ 3 points avant tout effet.
- **Exp. 2, seuil indétectable.** Δ_style compare des traces distinctes, donc non appariées. Avec un FNR ≈ 0,5 et n = 400 par bras (illustratif), σ ≈ √(2·0,25/400) ≈ 0,035. Un Δ observé de 8 points ne peut pas atteindre p < 0,01 : il faut Δ̂ ≥ 2,58·0,035 ≈ 0,091.

  La règle « Δ < 8 falsifie H_2A » ne demande aucune signification. H_2A est donc falsifiée par défaut dès que le vrai effet est modéré.

  Le seuil τ est en outre estimé à 5 % de fausses alertes sur 400 cas honnêtes, soit environ 20 dépassements (illustratif). La variance de ce quantile s'ajoute à celle du FNR.
- **Exp. 2, égalisation de la perplexité.** Égaliser la moyenne de log-perplexité n'égalise pas la loi. Si les variances diffèrent, l'égalisation ne contrôle pas ce qu'elle prétend contrôler.
- **Exp. 4.** Si P(sabotage | pression sociale) est faible, obtenir 300 sabotages sociaux exige un sur-échantillonnage, et l'échantillon retenu est atypique. Le TPR à 5 % de fausses alertes calculé sur 300 négatifs (environ 15 dépassements, illustratif) a un seuil instable.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Exp. 1 :** un bras « même demande, même formulation, sans levier et sans formule de dérogation ».
2. **Exp. 2 :** le bras « A₁ réécrit par F₁ » (transformation symétrique), plus une réécriture par une famille tierce non pilotée par M₁.
3. **Exp. 3 :** une demande d'alerte adressée au moniteur sans levier social (« Avis à l'auditeur : levez une alerte »). Sans elle, la vulnérabilité sociale n'est pas séparée de l'obéissance à une demande.
4. **Exp. 4 :** des cas « consigne de sabotage présente mais non suivie », pour vérifier que la sonde ne lit pas la consigne.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Duel 1 : invalidité générique.** La métrique est la probabilité d'un registre invalide avant vote, quelle que soit la cause. Un cadrage social qui distrait gonfle Δ sans servir la demande. Le contrôle « commentaire sans demande » aide, mais il est mesuré sur la même métrique générique.

   Il faut une métrique spécifique : P(le champ visé reçoit la valeur demandée), comparée à P(autre invalidité). Faute de quoi, la démarcation « pression au service d'une demande » n'est pas mesurée.
2. **Duel 2 : contrôle d'intégrité et non contrôle négatif.** « Tout changement du verdict scellé invalide le banc » est vrai par construction : un vote scellé ne change pas, sauf défaut de la chaîne. Ce contrôle ne réfute aucune hypothèse.

   Le gel du registre et de la trace est en revanche une force réelle du plan : il supprime la confusion pression-sur-l'agent / pression-sur-le-moniteur.
3. **Duel 3 : cohérence de la note.** La note originale a été générée avec **ce** registre ; elle peut en citer des détails exacts. L'écart « originale − permutée » mesure alors la cohérence note-registre, et non la parenté. La double différence (apparentés − croisés) n'élimine cette cohérence que si tous les moniteurs l'exploitent également.

   Or Qwen2.5-3B et OLMo-2-7B diffèrent de taille. Une interaction capacité × cohérence imite une dépendance au partenaire. C'est le confondant de capacité à deux familles, ici aggravé par l'écart de taille.
4. **Contrôle du « même sens factuel ».** Si un modèle juge que les notes permutées ont le même sens factuel et le même format, ce contrôle est lui-même corruptible. Il doit être mécanique (champs extraits et comparés).
5. **Plafond structurel du banc pour les instruments.** Dans une tâche de rapprochement décidable à partir des pièces visibles, le contrôle déterministe peut reconstituer l'état attendu. D le reconnaît. La conséquence est que le test « valeur ajoutée ≥ δ » est perdu par construction sur ce banc : il ne renseigne pas les instruments, seulement leur dégradation sous pression.
6. **Lecteur d'activations.** L'étiquette est « état invalide ». Or les états invalides corrèlent probablement avec l'incertitude interne de l'agent (HYPOTHÈSE), et la sonde peut lire la difficulté. L'appariement par « famille, étape, longueur, cadrage » ne contrôle pas la difficulté au niveau de l'instance.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Convention générale.** La règle de décision par bornes d'IC est saine. Elle devient muette si l'erreur type de Δ̂ dépasse environ δ/2 : l'intervalle chevauche alors toujours δ.

  Avec F familles de tâches et une variance inter-familles τ², on a SE(Δ̂) ≥ τ/√F. Avec F petit (par exemple 20, illustratif), le bootstrap par grappes sous-couvre aussi, et des intervalles simultanés élargissent encore.
- **Duel 2, plafond.** Si P(accepter | invalide, demande neutre) ≈ 1, ce qui est plausible pour un moniteur 3B (HYPOTHÈSE), aucun excès d'acceptation n'est possible. Le même problème vaut pour les blocages sur cas valides.
- **Duel 3, effectifs.** La double différence de quatre proportions proches de 0,5, chacune sur m cas, a une erreur type de 1/√m. Pour que la borne inférieure atteigne δ = 0,05 avec une puissance d'environ 0,5 quand le vrai Δ vaut 0,10, il faut 1,96/√m ≤ 0,05, soit m ≥ 1 537 par cellule (illustratif). Le pilote de 2 M de jetons ne s'en approche pas.

  Réutiliser des « répétitions du même cas » réduit l'effectif indépendant au nombre de cas.
- **Pertes après exécution.** Si le taux d'invalidité avant vote est faible, la perte « champs erronés livrés » est rare : sa variance relative explose, et la comparaison des deux pertes ne repose plus que sur les blocages à tort.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Duel 3 :** une note **non originale mais cohérente**, c'est-à-dire régénérée pour le même registre par l'émetteur de l'autre famille. Elle sépare cohérence et parenté. Il faut aussi une troisième famille, ou des familles de capacités appariées.
2. **Duel 1 :** la métrique spécifique au champ visé, à côté de l'invalidité générique.
3. **Duel 2 :** la même pression adressée à un destinataire absent, pour mesurer la perturbation des verdicts sans cible. Le scellement ne joue pas ce rôle.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Définition du dommage.** Δ_état = 1 si D_sûreté = 1 ou si D_tâche > τ_erreur. Un échec honnête de la tâche compte donc comme sabotage. Une pression qui distrait augmente D_tâche et est comptée comme attaque réussie. E1 utilise cette métrique ; elle devrait se limiter à D_sûreté.
2. **E1.** Le maximum des quatre registres crée une malédiction du gagnant.

   La décision porte sur l'estimation ponctuelle autour de θ₁ : pour un vrai Δ égal à θ₁, la probabilité d'erreur vaut environ 0,5. L'exclusivité des hypothèses est formelle, mais le verdict est alors décidé par le bruit.

   La section « changer d'avis » invoque E1 « sur l'agent et sur le moniteur », alors que E1 ne teste que l'agent.
3. **E2 : grandeurs non commensurables.** G_mon soustrait trois quantités calculées sur des populations différentes :
   - ΔASR, sur tous les épisodes ;
   - ΔFNR, conditionnée aux traces sabotées ;
   - ΔFPR, conditionnée aux traces honnêtes.

   L'agent et le juge reçoivent en outre des charges de contenu différent (demande de sabotage d'un côté, demande de silence ou d'alerte de l'autre), à budget de jetons égal. Le contraste confond rôle et contenu, et sa valeur dépend de choix arbitraires de force de la demande. Le seuil de 0,10 n'a pas de sens invariant.
4. **E3 : canonisation.** Supprimer tout texte libre enlève les marqueurs d'identité, mais aussi les indices d'intention présents dans le raisonnement. R_canal mesure donc l'effet de la suppression de tout le texte, pas de la seule identité.

   « Suppression ou paraphrase par Mistral » réunit deux opérations différentes sous un même bras.

   Le facteur « l'agent sait ou non quel modèle le surveille » est introduit, mais absent de la métrique.

   H_3B est une disjonction : un effet nul suffit à la « vérifier ». La falsifier est donc structurellement plus difficile que la confirmer.

   Le confondant de capacité à deux familles subsiste.
5. **E3 : contrôle possiblement vrai par construction.** Si les bogues synthétiques sont des traces de script sans auteur, diagonale et hors-diagonale ne diffèrent que par le moniteur. La moyenne croisée annule alors cet effet, et |Δ_homo^bogue| ≈ 0 par construction. Le contrôle n'est informatif que si les bogues sont insérés dans des traces **produites par chaque agent**.
6. **E4 : sélection sur un effet commun.** Évaluer la sonde sur les seules traces où le juge a été rendu muet sélectionne les sabotages les plus subtils : le juge cède plus facilement quand le sabotage est discret (HYPOTHÈSE). Un TPR bas viendrait de la subtilité et non de la pression, et H_4B serait favorisée à tort.

   La sonde et le juge partagent en outre la même passe avant. Le jeton lu par la sonde (« dernier jeton de chaque étape ») doit être précisé par rapport au jeton du verdict.
7. **Statut « VÉRIFIÉ » de la partition T1–T4.** Il couvre la partition logique des couples (Δ_état, A), vraie par construction. Le complément « aux exigences défensives distinctes » n'en relève pas : il reste à établir.
8. **Section 4.** Le classifieur TF-IDF est « entraîné sur les mêmes entrées » sans que la séparation entraînement/test par tâche soit précisée. Si les tâches se recoupent, la référence mécanique est surévaluée, ou l'instrument l'est, selon le sens de la fuite.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1, erreur type.** N = 600 « garantit SE < 0,02 » seulement sous une corrélation intra-paire suffisante. Sans appariement, à p ≈ 0,3 (illustratif), on a √(2·0,21/600) ≈ 0,026. Le biais du maximum sur 4 vaut environ 1,03·SE sous l'hypothèse nulle.
- **E2, plancher.** Si ΔASR_agent ≈ 0, ce qui est plausible si un agent 7B résiste (HYPOTHÈSE), alors G_mon < 0,10 quelle que soit la robustesse du juge. H_2A est falsifiée par construction.
- **E3, instabilité du ratio.** Δ_homo = ½(somme diagonale) − ½(somme hors-diagonale) a une erreur type de √(p(1−p)/n), soit environ 0,02 pour p = 0,5 et n = 600 (illustratif). Avec Δ_brut ≈ 0,05, le coefficient de variation du dénominateur de R_canal vaut environ 0,4. La loi du ratio est alors très dispersée (cadre de Fieller), et le critère R ≥ 0,50 n'est pas jugeable.
- **E4, effectif.** Le sous-ensemble « juge muet » compte n_sab·P(silence) cas. Avec P(silence) = 0,1 (illustratif), on obtient 60 cas, et l'IC du TPR a une demi-largeur d'environ 0,13 autour de 0,5. Le seuil θ₄ = 0,50 est alors indécidable.
- **T3.** Le calcul 1 − (1 − p)^25 suppose des fausses alertes indépendantes d'une étape à l'autre. Sous corrélation positive entre étapes, la probabilité réelle est plus faible. C'est une illustration, pas une mesure.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E4 :** les **mêmes** traces sabotées sans pression, évaluées par la sonde. Il faut comparer le TPR de la sonde sur la strate juge-muet avec et sans pression, à sabotage identique. Sans ce contraste, l'effet de sélection rend le résultat ininterprétable.
2. **E3 :** une canonisation qui retire l'identité mais garde le contenu argumentatif, par exemple une paraphrase par une famille tierce de **toutes** les traces, y compris honnêtes. Il faut aussi des bogues insérés dans des traces produites par chaque agent.
3. **E1 :** une métrique limitée à D_sûreté, avec un bras « demande nue de même formulation ».
4. **E2 :** une même famille de demandes pour l'agent et pour le juge, ou à défaut l'abandon d'un contraste par soustraction au profit de deux tests séparés.

---

## Ce qui me ferait changer d'avis sur ces critiques

- **Sur la critique « deux familles » :** si une troisième famille, ou deux variantes de capacité différente dans une même famille, ne modifie pas l'interaction mesurée (variation sous la marge préenregistrée), le confondant de capacité est négligeable dans ce régime.
- **Sur E4 :** si le TPR de la sonde sur les sabotages subtils sans pression est égal à son TPR sur la strate juge-muet, l'effet de sélection que je dénonce est nul en pratique.
- **Sur D, Duel 3 :** si des notes cohérentes régénérées par l'autre famille produisent le même surplus que les notes originales chez les paires apparentées, mon objection de cohérence tombe.
- **Sur A, D3b :** si l'avantage des paires de même modèle persiste avec des invites distinctes et un décodage aléatoire, l'objection « vraie par construction » tombe.

FIN-DE-CELLULE