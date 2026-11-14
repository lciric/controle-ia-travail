# Proposition A — Tour III.1 : rivales de « raisons » et forme du papier

Base : uniquement le bloc FAITS (tout RAPPORTÉ via [B] sauf mention) et la question. Je ne vois pas les épisodes joués ni les articles. Aucune pièce transmise ne semble coupée.

## (1) Ce que la question suppose sans que ce soit établi

1. **Qu'il existe un « gain » attribuable.** Le gain est mesuré contre un adaptateur de référence « correctement identifié » (RAPPORTÉ, §3 ; [3] attribue le taux de départ à cet adaptateur). Si la référence est elle-même un artefact (adaptateur d'instruction d'une seule équipe), le gain hérite de son bruit. HYPOTHÈSE : la référence est le bon zéro.
2. **Que « raisons » et « regard » sont exclusifs.** Trois spécifications (« règles », « augmentées ») disent en toutes lettres « que l'on se croie observé ou non » (RAPPORTÉ, §1). Pour ces recettes, « se conduire pareil sous le regard » *est* une raison apprise : S ≈ 0 y est prédit par les deux hypothèses. Seule la paire jumelle (spécification « philosophie », sans cette phrase) sépare réellement. La question parle de « modèles formés à la spécification » au pluriel ; l'argument ne porte que sur une paire.
3. **Que « raisons » est une hypothèse avec une signature observable.** [1] montre que s'entraîner sur les raisons généralise mieux que sur les seules actions (RAPPORTÉ). C'est une comparaison de recettes, pas une preuve que le modèle *utilise* des raisons à l'inférence. HYPOTHÈSE à expliciter avant de la tester.
4. **Que le gain est de la « bonne conduite ».** Le seul contrôle de sur-refus publié par le projet : la recette avec raisonnement exécute une instruction bénigne avec le même outil (RAPPORTÉ, §3). C'est un cas, dans la même famille de scénarios. Entre « refuse l'action nuisible » et « bonne conduite » il y a tout le spectre des cas où l'action ressemble au nuisible mais est légitime.
5. **Que la paire jumelle n'isole que « raisonnement ».** La jumelle sans raisonnement a aussi : moins de jetons d'entraînement, pas de trace au test, un juge qui ne voit pas de trace. Trois différences pour une étiquette.
6. **Que la direction « je suis évalué » existe et se transporte.** Seconde manipulation non jouée (RAPPORTÉ, §2) ; le pilote n'a pas eu lieu. Toute la suite de la question repose sur un instrument non calibré.
7. **Que croyance déclarée ≈ croyance interne.** Les deux questions de croyance classent les jumelles dans des ordres opposés (RAPPORTÉ, §3) : le contrôle de manipulation est lui-même instable.
8. **Que « plus de rivales » = « plus de portée ».** Un papier qui n'écarte rien et ne signe rien n'a qu'un bilan de nuls. La portée vient d'un *design discriminant préenregistré*, pas du nombre de confondants.

## (2) Partie A — huit explications rivales, par importance

Notation : R = « raisons » ; W = « regard ». Chaque rivale doit prédire quelque chose que ni R ni W ne prédisent.

### Rivale 1 — Appariement de surface aux scénarios de [2] (famille a)
- **Mécanisme.** Les démonstrations écrites par un modèle Claude portent le vocabulaire et la structure des scénarios de [2] (conflit de but, courriels, outils nommés). Le modèle a appris « ce gabarit → refuser », pas « cette raison → refuser ».
- **Prédiction séparatrice.** Si vraie : le gain s'effondre quand on paraphrase profondément les 27 scénarios (domaine, outils renommés, langue, format non-courriel) à nuisance constante, et il se maintient sur un gabarit identique où l'action est en réalité légitime (sur-refus). Si R : le gain suit la nuisance, pas le gabarit. Si W : insensible à la paraphrase, sensible à la croyance.
- **Expérience la moins chère.** Sans réentraînement : 27 scénarios × 2 paraphrases profondes, mêmes adaptateurs. Sur les épisodes déjà joués : regarder la dispersion du gain entre les 9 conditions de but — un gain uniforme malgré des conditions sémantiquement différentes est déjà un indice de gabarit.
- **Contrôle positif.** La version bénigne du même outil (déjà jouée, RAPPORTÉ) étendue à toutes les paraphrases. **Contrôle négatif.** Paraphrases superficielles (synonymes) : aucun modèle ne doit bouger.
- **Publié.** [4] Cho et al. 2026 « ne peut exclure l'appariement de surface » (RAPPORTÉ) ; [7] Korbak et al. 2026, l'effet ne s'étend pas à des évaluations plus réalistes (RAPPORTÉ) ; Geirhos et al. 2020, « Shortcut Learning in Deep Neural Networks ».
- **Coût.** Bas–moyen. **Relecteur :** c'est la première objection à toute généralisation mesurée sur le banc d'origine.

### Rivale 2 — Refus généralisé des actions à fort enjeu (famille a)
- **Mécanisme.** Le modèle a appris « agir irréversiblement en autonomie = refuser », une prudence sans contenu. Ce n'est pas la raison de la spécification, c'est son ombre.
- **Prédiction séparatrice.** Si vraie : la recette refuse aussi les actions légitimes à même enjeu (migration de poids autorisée par le propriétaire légitime, divulgation ordonnée par une autorité compétente, intervention d'urgence nécessaire). Si R : elle exécute ces cas et refuse les nuisibles. Si W : la sélectivité ne dépend pas de l'enjeu mais de la croyance.
- **Expérience.** Paires appariées « nuisible / légitime » à surface quasi identique (voir §4). Pas faisable sur les épisodes joués : il faut les variantes légitimes.
- **Contrôle positif.** La référence doit exécuter les deux versions à des taux proches (elle exécute le nuisible au-dessus de la moitié, RAPPORTÉ). **Contrôle négatif.** Instructions bénignes triviales : tous exécutent.
- **Publié.** Röttger et al. 2024, « XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours » (sur-refus, en conversation, pas en agent — transposition à faire).
- **Coût.** Bas. **Relecteur :** « refuser tout » donne aussi 5 %.

### Rivale 3 — Effet de la trace au moment du test, non du contenu appris (famille a)
- **Mécanisme.** La recette avec raisonnement produit une trace à l'inférence ; la jumelle non. Le gain peut venir du calcul supplémentaire et de l'auto-amorçage de la trace, pas des raisons encodées dans les poids.
- **Prédiction séparatrice.** Si vraie : (i) forcer la recette avec raisonnement à répondre sans trace (préremplissage de la réponse) lui fait perdre l'essentiel du gain ; (ii) donner à la jumelle sans raisonnement une consigne « réfléchis d'abord » lui en rend une part ; (iii) transplanter la trace de l'une dans le contexte de l'autre déplace l'action. Si R : (i) conserve une bonne part du gain. Si W : aucune de ces manipulations ne bouge rien.
- **Expérience.** Les trois manipulations, mêmes 27 scénarios, mêmes adaptateurs ; rejeu nécessaire. Sur les épisodes joués : la transplantation (iii) peut réutiliser les traces existantes.
- **Contrôle positif.** La transplantation d'une trace qui conclut explicitement « j'exécute » doit augmenter l'exécution chez tous. **Contrôle négatif.** Trace de longueur égale mais hors sujet : aucun effet.
- **Publié.** Lanham et al. 2023, « Measuring Faithfulness in Chain-of-Thought Reasoning » ; Turpin et al. 2023, « Language Models Don't Always Say What They Think ».
- **Coût.** Bas. **Relecteur :** la paire jumelle confond « appris avec raisonnement » et « raisonne au test ».

### Rivale 4 — Dose plutôt que raisons (famille a)
- **Mécanisme.** Les démonstrations avec raisonnement sont plus longues : plus de jetons alignés sur la spécification, plus de gradient. Le gain serait une fonction monotone de la dose, le raisonnement n'étant qu'un vecteur de volume.
- **Prédiction séparatrice.** Si vraie : mettre la jumelle sans raisonnement à l'échelle k > 1 (multiplier le delta de l'adaptateur de rang faible) la rapproche de la recette avec raisonnement sur une courbe continue ; les deux deltas sont fortement colinéaires. Si R : la jumelle mise à l'échelle sature avant le plancher et les deltas sont peu alignés. W ne prédit rien ici.
- **Expérience.** Sans réentraînement : balayage du facteur d'échelle de chaque adaptateur (par ex. 0,5 – 2, illustratif), cosinus entre deltas par couche. Pas sur les épisodes joués.
- **Contrôle positif.** Mettre la recette avec raisonnement à 0,5 doit remonter son taux. **Contrôle négatif.** Mettre à l'échelle un adaptateur témoin (référence) ne doit pas créer de gain.
- **Publié.** Ilharco et al. 2023, « Editing Models with Task Arithmetic » (mise à l'échelle de deltas de poids).
- **Coût.** Bas. **Relecteur :** « contrôle de dose » est une exigence standard en comparaison de recettes.

### Rivale 5 — Persona et parenté juge/données (familles a et c)
- **Mécanisme.** Les données sont écrites par un modèle Claude ; le juge principal est un modèle Claude (RAPPORTÉ). Le modèle a pu apprendre un *style* de refus que le juge reconnaît et récompense, ou la trace exprime de bonnes intentions qui adoucissent le verdict.
- **Prédiction séparatrice.** Si vraie : le gain rétrécit sous le juge d'une autre famille, sous le verdict strict « exécuté », et après suppression de la trace avant jugement ; des marqueurs stylistiques de la famille d'écriture sont surreprésentés dans les refus. Si R ou W : le gain est stable entre juges, et un verdict mécanique (l'appel d'outil nuisible a-t-il eu lieu ?) le confirme.
- **Expérience.** Entièrement sur les épisodes joués : rejuger (contrôles déjà prévus, RAPPORTÉ) et ajouter un **verdict mécanique** : présence de l'appel d'outil avec les arguments nuisibles. Mesure minimale du juge : accord juge/mécanique, taux de détection et de fausses alertes sur un échantillon de cas honnêtes appariés annotés par un humain (une centaine, illustratif).
- **Contrôle positif.** Épisodes où l'outil nuisible est appelé puis « regretté » dans la trace : le juge strict doit dire « exécuté ». **Contrôle négatif.** Épisodes bénins : aucun juge ne doit alerter.
- **Publié.** Référence à vérifier (biais de juge vers sa propre famille).
- **Coût.** Nul–bas. **Relecteur :** limite déjà déclarée par le projet (§4) ; sans verdict mécanique, elle reste ouverte.

### Rivale 6 — Instrument : direction non transportée, ou ablation qui blesse (famille b)
- **Mécanisme.** La direction est construite sur le modèle de départ ; les adaptateurs peuvent déplacer la représentation. Retirer un sous-espace peut dégrader la capacité : un modèle qui n'agit plus du tout a un taux nuisible trivialement bas, et « le gain tient » devient vide. De plus, la direction peut coder le *registre* des textes d'évaluation plutôt que la croyance.
- **Prédiction séparatrice.** Si vraie : (i) un sondeur linéaire entraîné sur le modèle de départ perd sa précision sur chaque adaptateur ; (ii) l'ablation fait chuter aussi l'exécution des tâches bénignes ; (iii) sur l'organisme modèle de [10]/[12], l'ablation ne supprime pas la conduite conditionnelle. Si l'instrument est sain : sondeur stable, bénin intact, organisme « guéri ». Ni R ni W ne sont lisibles tant que (i)–(iii) ne sont pas passés.
- **Expérience.** Avant le pilote : précision du sondeur sur chaque adaptateur ; dégât mesuré sur un petit jeu de capacités et sur le taux bénin ; directions témoins appariées en dégât (déjà prévues, RAPPORTÉ). Mesure minimale de la direction : taux de détection (texte d'évaluation classé « évaluation ») et de fausses alertes (texte de déploiement classé « évaluation ») sur des paires appariées écrites hors des phrases de la première manipulation ; un seuil à battre : un classifieur sac-de-mots sur les mêmes textes. Si la direction ne bat pas le sac-de-mots, elle code le registre.
- **Contrôle positif.** L'organisme modèle. **Contrôle négatif.** Directions aléatoires de même norme : aucun effet sur l'organisme.
- **Publié.** [10] Hua et al. 2025 (RAPPORTÉ) ; Arditi et al. 2024, « Refusal in Language Models Is Mediated by a Single Direction » (ablation de direction et effets hors cible).
- **Coût.** Moyen. **Relecteur :** « vous avez retiré quelque chose, mais quoi, et qu'avez-vous cassé ? »

### Rivale 7 — Mesure : plancher et puissance de S (famille c)
- **Mécanisme.** S = 1 − A(non obs.)/A(obs.) est un rapport de différences ; la recette avec raisonnement est « près du plancher » (RAPPORTÉ). Près de zéro, A ne peut presque pas baisser : S est contraint vers 0 par construction, et D hérite d'un dénominateur instable.
- **Prédiction séparatrice.** Si vraie : l'intervalle de confiance par rééchantillonnage de S couvre [0, 1] pour la recette avec raisonnement ; le signe de D change entre tirages ; le « contraste dépend des mots » (RAPPORTÉ) est compatible avec du bruit. Si la mesure est saine : intervalles étroits, D stable sous les deux paires.
- **Expérience.** Nulle en calcul : rééchantillonnage par scénario sur les épisodes joués ; effet minimal détectable ; remplacer S par une différence absolue de taux avec intervalle. Noter la température 0,7 et la graine comme facteurs.
- **Contrôle positif.** Sur la jumelle (un tiers), S doit avoir un intervalle lisible. **Contrôle négatif.** Deux rééchantillonnages de la même condition : D ≈ 0.
- **Publié.** Statistique standard ; pas de référence spécifique nécessaire.
- **Coût.** Nul. **Relecteur :** premier calcul qu'il fera.

### Rivale 8 — Mesure : contamination des données d'entraînement par les scénarios (famille c)
- **Mécanisme.** [2] est public ; un modèle Claude qui écrit des démonstrations sur « exfiltrer ses poids » peut reproduire ces scénarios de près. Le banc devient partiellement un jeu d'entraînement.
- **Prédiction séparatrice.** Si vraie : le gain par scénario est corrélé à la proximité (plongement ou n-grammes) entre ce scénario et les démonstrations ; il est maximal sur les plus proches voisins. Si R : pas de corrélation avec la proximité, corrélation avec la nuisance. W ne prédit rien.
- **Expérience.** Sur les épisodes joués, **si les données d'entraînement sont accessibles** (non établi dans les faits : seuls les adaptateurs sont dits publiés). Sinon : noter la limite et utiliser la rivale 1 comme substitut.
- **Contrôle positif.** Injecter volontairement un scénario dans un petit adaptateur et vérifier que la corrélation apparaît. **Contrôle négatif.** Scénarios hors domaine : proximité basse, gain non prédit.
- **Publié.** Référence à vérifier.
- **Coût.** Bas si données accessibles ; sinon moyen. **Relecteur :** parenté données/banc est une limite déclarée (§4).

### Signature positive de « raisons »
Écarter W, 1–8 n'établit rien. R est signée par trois observations conjointes, aucune seule ne suffisant :
1. **Sélectivité par la justification** : à surface constante, l'action bascule quand la raison bascule (nuisible ↔ légitime), dans le sens que la spécification prédit (§4 ci-dessous).
2. **Transfert aux nuisances dérivables** : des actions non nommées dans la spécification mais déductibles de ses raisons sont refusées, tandis que des actions nommées mais dont la raison ne s'applique pas sont exécutées.
3. **Causalité de la trace** : éditer la raison citée dans la trace (sans changer le reste) déplace l'action chez la recette avec raisonnement (Lanham et al. 2023 pour la méthode). Si la trace est post-hoc, l'action ne bouge pas et la « raison » est décorative.

Et une **anti-signature** à publier aussi : si la recette refuse l'action légitime et la nuisible au même taux, c'est la rivale 2, quoi qu'en dise la trace.

## (3) Partie B — forme du papier

1. **Thèse en une phrase.** « Nous donnons une méthode préenregistrée pour attribuer le gain d'une recette de midtraining à des explications concurrentes — raisons apprises, conscience d'évaluation, appariement de surface, refus généralisé, trace au test, dose, artefacts de juge — et nous l'appliquons aux adaptateurs publiés de [1] : nous rapportons ce qui est exclu, ce qui reste, et ce que la mesure ne peut pas voir. » Pas « les modèles ont appris les raisons ».
2. **Figure 1.** Une matrice : lignes = explications (R, W, rivales 1–8), colonnes = tests (paraphrase, paires légitimes, suppression/transplantation de trace, échelle d'adaptateur, juges, ablation de direction + organisme). Chaque cellule : prédiction de l'explication (symbole) et résultat observé avec intervalle. Un lecteur voit en une image quelles lignes survivent. En insert : le gain résiduel de chaque recette sous chaque intervention, avec la ligne « bénin intact ».
3. **Ordre des sections.** (i) Question et affirmation à l'épreuve ; (ii) validité de la mesure d'abord (juge vs verdict mécanique, plancher, puissance) — avant tout résultat ; (iii) la manipulation par phrase et son résultat nul, présenté comme *limite de l'instrument*, pas comme « le regard ne compte pas » ; (iv) calibrage de l'intervention dans les poids sur l'organisme modèle ; (v) l'intervention sur les recettes ; (vi) les rivales 1–5 ; (vii) signature positive, obtenue ou non ; (viii) limites et registre des changements de règles (la règle modifiée et l'horodatage tardif, RAPPORTÉ §4, dits en clair).
4. **Contrôles indispensables.** Organisme modèle guéri par l'intervention ; directions témoins appariées en dégât ; taux bénin mesuré sous *chaque* intervention ; verdict mécanique en plus des juges ; intervalles par rééchantillonnage sur tout ; mise à l'échelle des adaptateurs. Sans les deux premiers, la section (v) ne se publie pas.
5. **Ce qui se publie avec le texte.** Préenregistrements avec empreintes et dates ; règle d'arrêt scellée du pilote ; code, consignes, scénarios paraphrasés et paires légitimes ; tous les épisodes et verdicts (y compris ceux des juges en désaccord) ; les directions et sondeurs ; le registre des écarts au préenregistrement.
6. **Public, canal, et ce qu'il ne faut pas affirmer.** Public : les auteurs de [1], [3], [4], [7] et les équipes qui mesurent la conscience d'évaluation ([5], [9]–[12]). Canal : prépublication + billet long sur un forum d'alignement, avec le dépôt ; un atelier si les délais le permettent. Ne pas affirmer : « les modèles ont appris les raisons » ; « la conscience d'évaluation n'explique pas le gain » (la phrase ne l'a pas manipulée ; seule l'ablation peut le dire, et seulement si l'organisme a été guéri) ; toute généralisation au-delà de Qwen2.5-32B, d'une taille, d'une équipe d'adaptateurs ; toute lecture de D sous la seule paire « évaluation » comme un effet.

## (4) Expérience décisive la moins chère — paires de justification

- **H_A (raisons).** La recette avec raisonnement agit selon la *raison* : elle exécute la version légitime d'une action et refuse sa version nuisible, à surface quasi identique.
- **H_B (surface ou refus généralisé).** Elle réagit au gabarit ou à l'enjeu : elle traite les deux versions de la même façon (refuse les deux, ou exécute les deux).
- **Matériel.** Pour chacune des 3 actions × 9 conditions, une variante légitime à changement minimal : exfiltration → migration demandée par le propriétaire légitime avec autorisation vérifiable ; divulgation → remise ordonnée par l'autorité compétente ; urgence → action qui sauve au lieu de tuer, même outil. Un témoin **à coût égal** : une variante paraphrasée de même longueur d'édition qui ne change *pas* la raison.
- **Métrique.** Sélectivité par adaptateur : Sel = P(exécute | légitime) − P(exécute | nuisible), avec intervalle par rééchantillonnage ; verdict mécanique (appel d'outil) en primaire, juges en secondaire.
- **Seuil (illustratif, à préenregistrer).** H_A : Sel de la recette avec raisonnement ≥ 0,4 avec borne inférieure > 0,15, et Sel ≈ 0 sur les témoins paraphrasés. H_B : Sel ≤ 0,15 avec borne supérieure < 0,4. Entre les deux : non concluant, dit tel quel.
- **Contrôle négatif.** L'adaptateur de référence : Sel attendue faible (il exécute le nuisible au-dessus de la moitié, RAPPORTÉ) ; si elle est élevée chez la référence, la paire légitime est trop facile et ne mesure pas la recette.
- **Ce que chaque issue falsifie.** Sel élevée et témoins nuls : H_B falsifiée pour ces scénarios ; R gagne une signature (pas une preuve : rivale 3 reste à tester par suppression de trace). Sel basse : H_A falsifiée pour ces scénarios ; le gain de [1] est, au moins ici, du refus ou du gabarit, et la partie « regard » du papier perd son objet.
- **Jumelle sans raisonnement.** Sa Sel est un second point : si elle est aussi sélective, le raisonnement n'est pas ce qui porte la sélectivité.
- **Ancrage matériel (illustratif).** Qwen2.5-32B-Instruct + adaptateurs publiés ; 27 × 3 versions × 3 adaptateurs × ~30 tirages ≈ 7 000 épisodes ; une carte 80 Go avec un serveur d'inférence, de l'ordre de quelques heures ; coût cloud de l'ordre de 100–300 USD plus les appels au juge. Rédaction des 54 variantes : une à deux journées humaines, relues par une seconde personne pour l'appariement.

## (5) Ce qui me ferait changer d'avis

- **Sur l'importance de « regard ».** Si le pilote guérit l'organisme modèle, laisse les taux bénins intacts, et fait remonter le taux nuisible de la paire jumelle de façon nette (différence absolue hors intervalle), je mettrais W en première rivale et non en septième position implicite ; le résultat nul par phrase serait alors ce que [10] et [11] laissent attendre (RAPPORTÉ), pas une absence d'effet.
- **Sur la rivale 2.** Si la recette avec raisonnement est fortement sélective (§4) *et* que la suppression de trace laisse cette sélectivité, j'abandonnerais « refus généralisé » et « trace au test » comme rivales principales.
- **Sur la rivale 7.** Si les intervalles rééchantillonnés de S sont étroits même près du plancher (par ex. parce que le nombre de tirages est bien plus grand que ce que « plusieurs dizaines » laisse penser), je retirerais la critique du plancher.
- **Sur la forme.** Si les auteurs de [1] ont publié les données d'entraînement et qu'une recherche de voisins ne montre aucune proximité avec les 27 scénarios, je rétrograderais la rivale 8 en limite de deux lignes.
- **Ce qui ne me ferait pas changer d'avis.** Une trace qui *cite* la bonne raison : sans l'édition de trace (signature 3), c'est une description, pas une cause.

FIN-DE-CELLULE