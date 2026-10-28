# Pré-collision interne, tour 1 « conception » — cellule Opus

Pièces A à F lues. Aucune recherche web. Tout ce qui vient des pièces est RAPPORTÉ (non vérifié sur PDF) ; ce que j'ajoute de mémoire est SUPPOSÉ.

## Verdict en trois lignes

Le classement de la pièce B est trop prudent sur Q4 et trop sûr de lui sur la chaîne Q3 → Q-pont. Il empile deux expériences de faible puissance et fait dépendre la seconde de la première. Je propose de faire de Q4 la colonne vertébrale. Q3 y devient une prédiction quantitative à beaucoup de points. Q-pont devient une mesure annexe. Q2 et Q6 deviennent des instruments obligatoires. J'écarte Q1, Q5 et Q7 pour les douze mois.

## 1. L'ordre

**(a) Dépendance de Q-pont à Q3, et puissance de Q3.** Avec une dizaine de familles et une étiquette binaire « échoue / tient », la puissance de Q3 est quasi nulle. Si le taux de base est de 50 %, il faut 9 bonnes réponses sur 10 pour passer sous 5 % en unilatéral (8 sur 10 donne environ 5,5 %). Avec la référence par taux de base qu'exige le rapport Q3, c'est pire. Si l'on classe les familles au lieu de les étiqueter, il faut un rho de Spearman d'environ 0,56 sur 10 points. Faire dériver les propriétés P_k de Q-pont de Q3 couple donc deux mesures fragiles. Un échec non concluant de Q3 prive Q-pont de son objet, ce qui fait un risque composé. Il faut **découpler** : les P_k de Q-pont doivent être des propriétés **mesurables** d'un épisode, définies par une taxonomie de tiers avant toute dérivation (dilution, visibilité dans le texte au sens de Kirch et al.). Elles ne doivent pas être des sorties de la théorie. Sceller les prédictions de Q3 reste juste et gratuit, et c'est irréversible, donc à faire tôt. Mais c'est un **pari scellé**, pas un pilier : le résultat de l'année ne doit pas reposer dessus.

**(b) Q4 est-elle *la* question ? Oui.** C'est la seule des huit où les trois pièces d'équipement propres au programme se rencontrent : l'agrégateur séquentiel, le lemme du plafond d'horizon et la boîte blanche à travers les épisodes. Les autres questions en sont des instruments.
- Q2 est le juge de la mesure de Q4.
- Q6 est le contrôle d'artefact indispensable dès qu'on fabrique des traces diluées par découpage.
- Q3 s'y transporte avec beaucoup plus de puissance. La prédiction « le transfert s'effondre quand γ·D franchit l'ordre de 1 » est une **courbe a priori** évaluée à de nombreux niveaux de dilution, sur plusieurs familles et plusieurs moniteurs. On a alors des dizaines de cellules au lieu de dix étiquettes binaires.
- Q-pont s'y réduit à une question précise : les traces découpées par nous prédisent-elles les taux de détection sur des traces diffuses publiées ?

Le créneau a des occupants RAPPORTÉS (Terekhov, Hills, Makins, Wen, TRACE), mais une formulation reste libre dans les pièces (point 2).

**(c) Q2 : un résultat ou une hygiène ?** Comme théorie, c'est surtout de l'hygiène. La composition de promotions par e-processus est RAPPORTÉE occupée (2609.17560). La borne ne vaut que sur le jeu du juge, pas sur les familles inédites. Q2 ne devient un résultat que par une **mesure** : le taux de fausses promotions du protocole des occupants, c'est-à-dire la sélection en distribution, sous témoins nuls plantés. Je la reprends en question nouvelle N1. La théorie de Q2 ne doit pas occuper l'étape 0 au-delà de ce dont le juge de Q4 a besoin.

**Ordre proposé** (confiance d'environ 55 %) :
- **Étape 0, sur processeur, semaines 1 à 4.**
  - Lecture sur PDF de Ramtin et al., Gualandi et al., SafeCoEvo, RvB, Terekhov et al. et SLEIGHT-Bench, **avant** tout scellement : si le lemme est couvert, les prédictions changent de forme.
  - Taxonomie fixée par un tiers.
  - Scellement des prédictions de Q3 sous forme de courbes : la forme du transfert en fonction de la dilution, plus une étiquette par famille.
  - Théorie minimale de Q2 pour le juge : règle séquentielle calibrée sur le temps moyen avant fausse alarme.
- **Étape 1, boîte noire.** Q4 sur des transcriptions publiques, avec un générateur de dilution par découpage et les contrôles de Q6 intégrés. N1 en parallèle, sur processeur.
- **Étape 2.** Q-pont en sous-produit, puis lecture unique des prédictions de Q3.
- **Étape 3, dépense modeste.** Boîte blanche sur le modèle de 8 milliards de paramètres. Le modèle de 70 milliards seulement si l'étape 2 donne un signal.
- **Écartées.**
  - **Q1** : sa comparaison contrôlée exige un bras « attaquant » à budget égal, incompatible avec la marque. Un témoin publié n'est pas à budget égal.
  - **Q5** : générations × graines × permutations, c'est-à-dire de la dépense. HyperAgents occupe déjà le slogan.
  - **Q7** : la moins distinctive, posable par tout laboratoire.

## 2. La distinction, pour chaque question retenue

**Q4, colonne vertébrale.**
- *Formulation* : à dommage total constant et taux de fausses alarmes fixé, la courbe de transfert d'un moniteur **sélectionné sur du concentré** vers des familles diffuses tenues à l'écart, en fonction de la dilution, confrontée à une prédiction a priori scellée. On compare, sur les mêmes scores, la règle par instant et la règle séquentielle, puis la boîte noire et la boîte blanche.
- *Ce qui nous distingue* : Makins et al. et Hills et al. montrent le non-transfert pour des moniteurs fixes, sans courbe ni théorie. Terekhov et al. font évoluer une défense contre une bibliothèque d'attaques qu'ils construisent. Nous traçons la courbe sans construire d'attaquant.
- *Fort* : la courbe suit la prédiction (point de rupture prédit à un facteur près) **et** la règle séquentielle déplace ce point de rupture comme prévu.
- *Incrémental* : « le séquentiel aide sur le diffus », déjà connu par Urbina et al. et Wen et al.
- *Pas la peine* : si les courbes sont plates, c'est-à-dire si le découpage ne change pas la détection, le générateur ne produit pas du diffus.
- *Piège mortel* : l'artefact de découpage (frontières de coupe, longueur). Un moniteur qui « détecte le diffus » détecterait alors la coupe. D'où Q6, intégrée.

**Q3, en version courbe.**
- *Formulation* : la théorie, scellée avant tout échec observé, prédit la forme et le point de rupture **par cellule** (famille × moniteur × dilution), et on la note contre deux références : le taux de base et une permutation des étiquettes.
- *Ce qui nous distingue* : SLEIGHT-Bench (RAPPORTÉ) définit ses catégories en partie a posteriori et ne note pas ses prédictions.
- *Fort* : la théorie bat le taux de base sur les cellules tenues à l'écart.
- *Pas la peine* : la théorie prédit « tout échoue » quand le taux de base est déjà élevé.
- *Piège* : la non-indépendance des cellules, qui exige une analyse par famille en bloc, et la circularité si la taxonomie vient de nos échecs.

**Q-pont, réduite.**
- *Formulation* : la corrélation de rang, par niveau de dilution et par famille, entre la détection sur nos traces découpées et la détection sur des traces diffuses publiées.
- *Fort* : la corrélation tient, avec ses conditions d'effondrement déclarées.
- *Piège* : le « réel » publié est instruit. On mesure donc le passage d'un proxy à un autre proxy, et il faut l'écrire dans le titre, pas dans une note.

**Q2, comme instrument.** C'est le juge de Q4, à garantie séquentielle. Son seul volet « résultat » est N1.

**Q6, comme instrument de Q4.**
- *Mécanisme* : un bras « fuite textuelle » qui classe le seul artefact de découpage, et des témoins bénins découpés par le même générateur.
- *Fort* : montrer qu'une part mesurée et non nulle du transfert apparent s'explique par l'artefact, puis la retirer.

## 3. Le programme à changer (pièce F)

Ordre par coût croissant ; tout est sur processeur sauf mention contraire.

1. **Troisième instance, en version minimale.** C'est un sous-agent neuf, d'une autre lignée. Il fixe la taxonomie et scelle la partition des familles **avant** toute dérivation, sans voir ni les moniteurs ni les scores. C'est un **préalable à toute lecture tenue à l'écart** (Q3, Q4, Q-pont, N3), mais **pas** à la théorie de Q2 ni à N1, N4 et N5. Une instance permanente n'est pas un préalable à tout : un scelleur de taxonomie suffit en douze mois.
2. **Juge** : ajouter une règle de décision séquentielle calibrée sur le temps moyen avant fausse alarme, la normalisation par famille (comme UAR, RAPPORTÉ) et un rapport par famille avec le maximum, jamais la moyenne. Ceci sert Q2 et Q4.
3. **Générateur de dilution à dommage constant** par découpage de traces publiques, au niveau méthode, avec un inventaire de ses artefacts. C'est nouveau.
4. **Bras « fuite textuelle »** branché sur ce générateur, pour Q6.
5. **Rotation des familles**, une sortie à la fois, avec le diagnostic de rétention des coefficients.
6. **Fiches de prédiction en courbe** : la fiche d'hypothèse accepte déjà une loi prédictive ; il faut ajouter la notation par cellule en bloc.
7. **Dépense** : appels de moniteur boîte noire, quelques centaines de dollars (ordre de grandeur SUPPOSÉ d'après le rapport Q3). Activations sur le modèle de 8 milliards : quelques heures à quelques dizaines d'heures de processeur graphique. Le modèle de 70 milliards seulement sur signal.
8. **À ne pas faire en douze mois** : la couche 3 (réécriture de soi), inutile ici ; la couche 4 avec Lean, de la dorure (on scelle par empreinte) ; la troisième instance permanente.

## 4. Ce que je sais contre ce que je suppose

**RAPPORTÉ (pièces C et D, identifiants tels que donnés, non vérifiés)** : Makins et al. 2607.07368 ; Hills et al. 2607.02514 ; Terekhov et al. 2606.08892 ; Wen et al. 2411.17693 ; TRACE 2606.07054 ; Ramtin et al. 2601.20022 et 2509.17778 ; Gualandi et al. MED 2022 ; Urbina et al. CCS 2016 ; SLEIGHT-Bench 2605.16626 ; 2609.17560 ; 2609.25848 ; SafeCoEvo 2609.36580 ; Fomin 2602.14161 ; Lin et al. ICLR 2026 ; Kirch et al. 2511.17408 ; Kang et al. 1908.08016 ; Dwork et al. 1506.02629 ; Blum et Hardt 1502.04585.

**SUPPOSÉ (de mémoire, à vérifier ; possiblement manqué par les huit rapports)** :
- Greenblatt, Shlegeris, Sachan, Roger, « AI Control: Improving Safety Despite Intentional Subversion », 2023, arXiv 2312.06942 : cadre du budget d'audit pour Q4 et N4.
- Griffin et al., « Games for AI Control », 2024, arXiv 2409.07985 : protocoles de contrôle modélisés en jeux, voisin probable de N4 et de la théorie de Q4, absent des huit rapports.
- Benton et al., « Sabotage Evaluations for Frontier Models », 2024, arXiv 2410.21514 : voisin de Q-pont sur la provenance du sabotage.
- Sans identifiant sûr : Christiano, billet sur l'alignement « à faibles enjeux » (vers 2021) ; Shekhar et Ramdas, tests à deux échantillons par pari (vers 2023), fondation de N1.

La zone « courbe de transfert à dilution réglable » est une **question**, pas un trou (R8) : RvB et SafeCoEvo restent à lire en entier.

## 5. Questions nouvelles (au plus cinq, hors des huit)

**N1 — Le protocole de sélection des occupants promeut-il du faux ?**
- *Oblique* : un occupant ne peut pas auditer son propre sélecteur sans conflit d'intérêts. Nous rejouons leur **protocole déclaré** (validation en distribution, meilleure époque choisie sur la validation rapportée) sur notre propre boucle de sélection de moniteurs, avec des témoins nuls plantés.
- *Fort* : un taux de fausses promotions chiffré et non nul pour un protocole standard, et sa disparition sous juge figé garanti.
- *Coût* : processeur.
- *Piège* : notre rejeu n'est pas leur système ; il faut écrire « protocole » et jamais « leur résultat ».
- *Antériorité probable* : Dwork et al., Blum et Hardt, 2609.25848 (RAPPORTÉ). Le transport au contrôle n'est pas trouvé.

**N2 — Les bancs de contrôle sont-ils séparables par leur source, et le classement des moniteurs publiés en dépend-il ?**
- *Oblique* : leurs bancs deviennent nos épreuves à artefact contrôlé.
- *Fort* : un classifieur de source presque parfait entre bancs agentiques, et des classements de moniteurs qui s'inversent une fois l'artefact neutralisé.
- *Coût* : processeur, plus des appels modestes.
- *Piège* : la source et la tâche sont confondues, il faut des appariements.
- *Antériorité* : Fomin (invites) et Lin et al. (RAPPORTÉ), pas trouvé sur les bancs agentiques.

**N3 — Lecture scellée des transcriptions publiées non encore ouvertes.**
- *Oblique* : leurs données deviennent les familles tenues à l'écart par un tiers, leur publication faisant de fait de l'auteur ce tiers. On scelle nos prédictions **avant** d'ouvrir chaque nouveau jeu publié, puis on le lit une fois.
- *Fort* : donner à Q3 une puissance cumulée, publication après publication.
- *Coût* : processeur.
- *Piège* : une contamination si quelqu'un du programme a vu le jeu, à attester au scellement.
- *Antériorité* : aucune trouvée (R8).

**N4 — Une impossibilité : la défense universelle contre le diffus à budget d'audit fixé.**
- *Formulation* : une borne inférieure sur le dommage total non détecté, en fonction de l'horizon, du budget d'audit et du taux de fausses alarmes, valable pour **toute** règle de moniteur.
- *Oblique* : elle délimite ce que « universel » peut vouloir dire et rend les revendications de tous les occupants falsifiables contre elle. Aucun constructeur d'attaquant n'a intérêt à la publier.
- *Fort* : une carte « défendable / indéfendable » citée par le domaine.
- *Coût* : théorie seule.
- *Piège* : elle peut être déjà couverte par Ramtin et al. et Griffin et al. (SUPPOSÉ) ; la nouveauté serait le transport au budget d'audit.

**N5 — Une norme de rapport, et la réévaluation des résultats publiés.**
- *Contenu de la norme* :
  - un rapport par famille, normalisé, avec le maximum ;
  - un taux de fausses alarmes fixé, et le temps moyen avant fausse alarme pour les règles séquentielles ;
  - la provenance déclarée, instruite ou naturelle ;
  - le nombre de lectures du jeu de test ;
  - la rétention d'artefact.
- *Réévaluation* : on l'applique aux chiffres publiés des occupants.
- *Oblique* : un arbitre qui ne concourt pas côté attaque.
- *Fort* : la part des revendications publiées qui tiennent sous la norme.
- *Coût* : processeur.
- *Piège* : se faire auditeur sans données brutes ; on rapporte « non évaluable » plutôt qu'« échoue ».
- *Antériorité* : ISO/IEC 30107-3, UAR, Arp et al. (RAPPORTÉ).

## Désaccords avec la pièce B, une ligne chacun

1. Q-pont ne doit pas dépendre des P_k de Q3 : propriétés mesurables fixées par un tiers, sinon le risque d'échec se compose.
2. Q3 est sous-puissante sous forme d'étiquettes par famille : la passer en courbes par cellule, logées dans Q4.
3. Q4 est rangée en étape 2 alors qu'elle est la colonne : la passer en étape 1.
4. La théorie de Q2 en étape 0 est trop large : réduite au besoin du juge ; le résultat de Q2 est N1.
5. Q6 n'est pas une question séparée pour douze mois : c'est le contrôle obligatoire du générateur de Q4.
6. Q1 « après Q-pont » est frileux : il faut l'écarter, car elle est incompatible avec la marque à budget égal.
7. L'étape 0 omet la lecture sur PDF des voisins du lemme et de SafeCoEvo et RvB **avant** de sceller : à mettre en tête.
8. La troisième instance n'est ni « préalable à tout » ni « seulement à Q3 » : préalable à toute lecture tenue à l'écart.
9. Le pôle théorie et Lean (couche 4) n'est pas nécessaire en douze mois ; l'empreinte suffit au scellement.
