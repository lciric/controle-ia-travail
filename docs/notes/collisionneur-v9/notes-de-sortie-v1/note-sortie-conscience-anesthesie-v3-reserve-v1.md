# L'anesthésie comme contraste pour la conscience des modèles de langage : note de sortie du collisionneur (question version 3, avec réserve d'orientation)

- **Date** : 2026-11-22, 19:32 UTC.
- **Dossier** : `runs/collisionneur-protocole-x-conscience-anesthesie-v3-reserve-abonnement-v1-20261122-153110`.
- **Accord** : GO-2026-11-22-78.
- **Dépense** : 12,59 dollars par l'interface, sur une ligne de 50 (`etat.md` du dossier). Ce total compte au pire deux coupures de flux de Carbon (2,30 et 2,41 dollars) ; la seconde cellule a été renvoyée par GO-2026-11-22-109. Les cellules Claude (Fable 5.2 et Opus 5.5) passent par l'abonnement et ne sont pas facturées.
- **Tours** : dix-sept cellules sur dix-huit. Au tour III.1 (conception), cinq modèles sur six : Argon a été refusé par son fournisseur (fin « RECITATION », 0,41 dollar), absence acceptée par l'arbitre (GO-2026-11-22-97). Argon est présent aux tours III.2 (critique croisée) et III.3 (réponse).
- **Pause** : le dossier a été suspendu entre 17:00 et 18:15 UTC, sans effet sur le contenu des cellules.
- **Réserve d'orientation** (`en-tete-reserve-v1.md`) : la question servie a été jugée orientée, faiblement (devinette à 0,6). L'orientation tient au contenu : la position « le contraste se transpose » s'appuie sur des résultats rapportés, la position contraire sur un argument. Ce dossier est en duel avec le dossier 1, servi avec une question neutre.

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier. Le lecteur est du même modèle qu'une des cellules (lettre B) ; elle est traitée comme les autres.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure : tout ce qui suit est protocole proposé, critique sur pièces ou calcul sous hypothèses. Les seuils, effectifs et coûts sont qualifiés d'illustratifs par leurs auteurs. Le lecteur a recompté trois dénombrements cités par plusieurs cellules (voir § 5) ; aucun autre calcul n'a été refait. Aucune référence bibliographique n'a été contrôlée. La note ne prend aucune position sur la conscience des systèmes artificiels : elle rapporte ce que les modèles en disent.

**Convention de lecture.** La question oppose deux « positions » nommées A et B, et les modèles portent aussi des lettres A à F. Pour éviter la confusion, la note appelle les positions par leur contenu : **« transposition »** (position A de la question) et **« faux ami »** (position B). Les lettres désignent toujours les modèles.

## 1. La question

Chez l'humain, on compare le cerveau éveillé au cerveau anesthésié pour étudier la conscience, avec le rapport du sujet comme témoin, dans ses limites (amnésie, conscience sans réponse). La question oppose deux lectures de ce contraste appliqué aux modèles de langage :

- **« Transposition »** : des travaux de 2026, non nommés, rapporteraient un petit ensemble de directions d'activation dont la suppression épargne la classification, l'extraction et le jugement de grammaticalité, et dégrade le raisonnement à plusieurs sauts, la traduction et le résumé. On pourrait provoquer un régime analogue à l'anesthésie, ou en chercher le motif dans les activations ordinaires. Prédiction : un profil propre à ces directions, distinct de celui d'un témoin.
- **« Faux ami »** : un réseau sans activité autonome ni mécanisme d'éveil n'a pas d'état à perdre, et faute de pôle « conscient » connu, toute dégradation ressemble à une anesthésie. Prédiction : le même profil sous une ablation témoin à dégradation globale égale, fixée avant la mesure.

Sept points sont posés : (0) une expérience peut-elle départager ? (1) un « état analogue à l'anesthésie » a-t-il un sens, et lequel ? (2) l'expérience la plus tranchante sur un petit modèle ouvert ; (3) l'usage de données humaines brutes ; (4) ce que chaque issue permet d'affirmer selon les théories de la conscience ; (5) la vérification hors de l'équipe ; (6) l'explication triviale la plus dangereuse et son témoin.

Notations communes aux cellules, reprises ici : U, le sous-espace des directions visées ; α, la dose de suppression (0 = modèle intact, 1 = suppression complète) ; la « dégradation globale » se mesure le plus souvent par la divergence de Kullback-Leibler moyenne par jeton entre le modèle intact et le modèle modifié, sur un corpus neutre (en nats par jeton).

## 2. En bref

- **Le point 0 fait l'unanimité.** Les six modèles répondent « oui pour les prédictions, non pour l'interprétation » : une expérience peut départager les deux prédictions chiffrées, aucune ne peut dire si un modèle « perd » un état conscient. Opus formule l'asymétrie la plus nette : un profil propre réfute la prédiction du « faux ami » sans toucher sa thèse ; un même profil retire à la « transposition » sa principale pièce empirique (B, III.1).
- **Le sens opératoire est partagé, le sens fort refusé par tous.** Chacun définit un objet neutre (« régime à profil sélectif », « régime d'atténuation sélective de l'intégration », « découplage intégratif gradué »…) et dit ce qui manque au sens fort : un pôle dont le statut conscient est établi hors de la manipulation, un mécanisme d'éveil, un canal de rapport indépendant du réseau manipulé.
- **Le danger principal nommé par les critiques est la lésion sélective triviale.** Une direction qui porte simplement la portée de l'attention, l'identité de la consigne ou la qualité d'une réponse longue reproduirait le profil sans aucun « régime ». Le témoin de portée d'attention et le croisement « distance dans l'entrée × fonction », proposés au tour III.1 par Carbon et Neon, sont repris par tous au tour III.3.
- **Le nul de sélection est l'autre acquis.** Des directions choisies pour produire la dissociation battent par construction des directions tirées au hasard. Tous adoptent, au tour III.3, le rejeu de toute la procédure de découverte sur d'autres partitions des six tâches ou sur des étiquettes permutées (idée de Fable, D2, III.1).
- **Aucun plan initial ne pouvait rendre le verdict « faux ami ».** Les critiques montrent que, aux effectifs proposés (200 à 300 items par tâche), un intervalle d'équivalence ne tient jamais dans les marges fixées. Tous font désormais dépendre ce verdict d'une porte de puissance, fixée sur un lot pilote.
- **Tous font précéder le duel d'une porte de jugeabilité.** Elle vérifie, sans regarder le résultat, que la chaîne de décision ne déclare pas « transposition » sur un témoin ordinaire et qu'elle retrouve une lésion plantée.

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (lettre A)

- **Proposition centrale** (A, III.1). Un « régime de dissociation spécifique », défini par la sélectivité S (performance moyenne des trois tâches gardées moins celle des trois perdues) et son écart au témoin ΔS à dose égale. Dix présupposés relevés, dont deux qui reviendront partout : la dissociation peut venir d'une fragilité inégale des tâches, et « la transposition » et « le faux ami » n'épuisent pas les cas (un profil propre peut être fabriqué par la procédure, ou relever d'une lésion sans régime).
- **Plan** (A, III.1). Quatre duels :
  - D1 : spécificité à dose égale contre cinq familles de témoins, dont un témoin désigné par les tenants du « faux ami » ;
  - D2 : sur les vingt façons de désigner trois tâches « gardées » parmi six, la partition de la question est-elle mieux servie par la même recherche de directions ?
  - D3 : un indice de complexité perturbationnelle transposé au réseau ;
  - D4 : le motif dans les activations ordinaires, hors verdict.

  Point 6 : la circularité de la sélection. Coût avancé : 100 à 200 dollars (illustratif).
- **Défauts relevés** (B, C, D, E, F, III.2). Aucun témoin de portée d'attention ; équivalence hors d'atteinte à 300 items (Opus) ; double appariement, en divergence de Kullback-Leibler et en performance, qui contraint la sélectivité (Argon) ; seuils 0,10 et 0,20 incohérents (Astra) ; dans D2, le rang 1 est attendu sous la thèse adverse aussi, par fragilité (Opus), par longueur d'entrée (Argon, Neon) ou par hiérarchie de prérequis (Carbon) ; D3 suit la densité de bits actifs, pas l'organisation (tous).
- **Après les critiques** (A, III.3). Fable accepte presque tout et reconnaît à plusieurs reprises que son plan avait le défaut relevé. Il rejette la conclusion d'Argon selon laquelle le double appariement fabriquerait toujours l'issue « aucune », tout en abandonnant ce double appariement. Changements majeurs :
  - la dose commune devient une **performance moyenne** fixée sur un lot d'étalonnage, et non plus la divergence de Kullback-Leibler (seul modèle à faire ce choix) ;
  - le verdict « faux ami » se juge contre un seul témoin, T_B, déposé sous empreinte par les tenants de cette position sans accès à la batterie ;
  - un duel D1′b, ouvert seulement si la « transposition » gagne, teste la lésion triviale (portée d'attention, axe de surface, format, identité de tâche) ;
  - D2 devient un nul de sélection qui ne peut que retirer à la « transposition » ; D3 sort du verdict.

  Il relève une contradiction entre deux critiques : Carbon tient l'inversion des groupes pour impossible, Neon l'exige comme témoin ; il en fait un test. Première expérience : la porte de jugeabilité, puis D1′a, sur un modèle instruit.

### Claude Opus 5.5 (lettre B)

- **Proposition centrale** (B, III.1). Le point 0 le plus argumenté : chez l'humain, le rapport au réveil calibre en partie le pôle anesthésié ; dans un modèle, « comparer deux inconnues ne calibre aucune des deux ». Un « régime à profil sélectif » sous un nom neutre, et l'exclusion de la réversibilité comme critère, automatique dans un modèle.
- **Plan** (B, III.1). Trois expériences :
  - E1 : spécificité croisée avec le format (choix par vraisemblance ou génération libre) ;
  - E2 : l'ordre de perte selon la dose, comparé à un prédicteur mécanique de fragilité (la marge du modèle intact) ;
  - E3 : persistance d'un effet après relâchement de l'intervention, pour tester la prémisse « pas d'état à perdre ».

  Côté humain, une idée propre : vérifier d'abord si l'ordre de perte sous anesthésie se distingue de celui sous inattention, privation de sommeil ou alcool. Si non, « ressembler à l'anesthésie » ne signifie rien pour un modèle. Point 6 : le format et la longueur de sortie. Coût : 150 à 400 euros (illustratif).
- **Défauts relevés** (A, C, D, E, F, III.2). Le témoin de température est nul par construction en choix forcé (tous) ; « étiquette justifiée » et « réécriture » changent la fonction des tâches gardées (Argon, Astra, Carbon, Neon) ; en forçage par l'enseignant, E3 ne mesure qu'une lecture du cache des clés et valeurs écrit pendant la fenêtre (tous) ; la dose α₅₀ est censurée pour les tâches gardées si la « transposition » est vraie (Fable, Carbon, Neon) ; le test humain penchait vers la « transposition » par atténuation de la corrélation de rang (Carbon).
- **Après les critiques** (B, III.3). Opus accepte presque tout et rejette quelques détails, chaque fois motivés : par exemple la fuite du prédicteur de fragilité en notation par vraisemblance, ou le rôle de la direction de refus, qu'il garde comme contrôle de l'intervention. Il note que son point 0 n'a été contesté par aucune critique. Changements :
  - le duel n'oppose la cible qu'au témoin que nomme la position « faux ami », les sous-espaces aléatoires, avec deux lots disjoints (seuil et verdict) ;
  - E2 est retirée comme duel (« il faudrait au moins vingt fonctions ») ;
  - E3 devient E3′, un plan 2 × 2 en génération libre repris d'Astra : texte produit sous intervention ou non, cache intact ou perturbé ;
  - six portes de faisabilité, dont une qui déclare le verdict « faux ami » non jugeable si les ablations génériques n'ont pas elles-mêmes un profil commun.

  Première expérience : les portes puis le duel, en format discriminatif, sur un modèle de 1 à 3 milliards de paramètres ; 20 à 40 heures de processeur graphique (illustratif).

### Argon (identifiant gemini-4-argon, lettre C)

- **Tour III.1** : absent (refus du fournisseur, absence acceptée).
- **Critique** (C, III.2). La plus longue, la plus formalisée. Apports repris ensuite :
  - sur Fable : la borne S ≤ 2(1 − D′) que le double appariement impose à la sélectivité ;
  - sur Opus : l'appariement à « variance retirée égale » et à divergence égale donnera des verdicts opposés par géométrie, et la persistance en forçage n'est qu'une lecture de cache ; proposition de masquer ou remplacer ce cache ;
  - sur Astra : à 300 items, l'erreur-type d'un écart vaut environ 2,6 points, contre une bande d'équivalence de ± 2 points : le verdict « faux ami » est hors d'atteinte ;
  - sur Carbon : la projection non centrée injecte un biais constant ; empiler cinquante sous-espaces témoins dans un régresseur reconstruit l'énergie de la cible par conservation de la norme ;
  - sur Neon : le témoin C4 est exclu des témoins qui décident, et le seuil « τ ≥ 0,80 à p < 0,01 » est inatteignable sur cinq niveaux.

  Argon marque « vérifié » ses propres dérivations ; elles n'ont pas été refaites.
- **Réponse** (C, III.3). Les cinq critiques visant C ne font que constater l'absence ; Argon les accepte. Il **conçoit son plan au tour III.3**, après avoir lu toutes les critiques, en transformant huit défauts relevés chez les autres en tests. Son plan n'a donc été critiqué par personne. Il comprend :
  - une paire de petits modèles, de base et instruit, de même architecture ;
  - un plan tâche × empan d'entrée (court ou long) à format de sortie unique (cible de 16 jetons) ;
  - cinq familles de témoins, dont une recherche de directions rejouée dans l'orthogonal de U (nul de sélection) et un décalage de moyenne pur ;
  - quatre portes avant mesure ;
  - un témoin propre pour le point 6 : la consigne induite par des exemples, sans mot-clé, pour écarter l'hypothèse que U ne code que la reconnaissance de la consigne.
- **Remarque du lecteur.** Dans le verdict « faux ami » d'Argon (C, III.3, expérience C-1), l'équivalence avec « au moins une » famille suffit, et ces familles incluent le témoin de portée d'attention et la recherche dans l'orthogonal. Or Argon reprochait à Neon (C, III.2, F-a3) de compter une équivalence avec un témoin de portée comme une victoire du « faux ami ». Les règles d'Argon peuvent aussi se chevaucher avec son issue « aucune », qui vise le même témoin. Personne n'a pu le relever, faute de tour suivant.

### Astra (identifiant gpt-6.2-astra, lettre D)

- **Proposition centrale** (D, III.1). La plus courte. « Tester la sélectivité, pas baptiser l'état » : à budget de dégradation égal, *où* le modèle perd-il ses capacités ? Unité : le point de pourcentage ; issue tranchée par des intervalles simultanés. Point 6 : les directions porteraient le maintien de la qualité d'une réponse longue. Modèle candidat : Pythia-1.4B (illustratif).
- **Défauts relevés** (III.2). Dose libre : à faible budget le « faux ami » gagne par insensibilité (Fable) ; points de pourcentage non normalisés et plancher probable sur un petit modèle de base (tous) ; un seuil absolu « gardée à ± 3 points de l'intact » réfute la « transposition » par construction à dose forte (Argon) ; comparaison d'un sous-espace unique à la moyenne du panel de témoins, qui ignore la dispersion entre sous-espaces (Carbon, Neon).
- **Apports en critique** (D, III.2). Énoncés conditionnels sur les lois plutôt que chiffres. Trois sont repris : le plan de greffe du cache en trois bras contre l'E3 d'Opus ; l'observation qu'une égalité avec le témoin de portée ne prouve pas que la cible *est* une fenêtre, seulement qu'on ne peut pas l'exclure ; la remarque qu'une borne supérieure seule ne certifie pas une équivalence bilatérale (contre Neon).
- **Après les critiques** (D, III.3). Astra abandonne la moyenne du panel : chaque témoin individuel est comparé à la cible, et les verdicts exigent « au moins 90 % des témoins individuels » de chaque loi. Il ajoute :
  - une étape de **qualification** : un tiers plante une lésion sélective connue dans des copies anonymisées, que toute la chaîne doit retrouver à l'aveugle ;
  - une conclusion admise d'avance : « ce banc n'est pas prêt à départager » ;
  - une issue nommée « spécifique aux projections testées, compatible avec une perte de portée ».

  Il rejette deux points : la suppression de la comparaison à l'intact, et l'obligation d'accumuler les opérateurs témoins. Première expérience : qualifier le banc, en commençant par un couple « extraction distante / inférence de proximité » à même longueur de réponse.

### Carbon (identifiant gemini-4-carbon, lettre E)

- **Proposition centrale** (E, III.1). Trois protocoles :
  - I : dissociation dose-réponse à format égalisé, jugée par une aire différentielle sous la courbe ;
  - II : motif passif dans les activations ordinaires ;
  - III : indice de complexité perturbationnelle transposé.

  Point 6 le plus repris du dossier : la **myopie positionnelle**. Si U détruit l'accès aux jetons lointains, la perte moyenne sur texte ordinaire bouge peu (elle est dominée par le contexte proche), les tâches locales survivent, les tâches qui relient des segments éloignés s'effondrent. Témoin : un plan croisé « empan × profondeur de composition » et une fenêtre d'attention tronquée. Modèles de 7 à 8 milliards de paramètres, en version de base et instruite ; environ 175 dollars (illustratif).
- **Défauts relevés** (III.2). Projection non centrée (tous) ; « vérifié » apposé à des souvenirs, dont une « attribution complète vérifiée » des références (Fable, Opus) ; le maximum de deux moyennes témoins est biaisé ; sigmoïde contre droite sur cinq paliers sans degré de liberté (Argon, Opus) ; contraste humain propofol contre kétamine confondant molécule et vécu (Opus, Astra) ; le contrôle de myopie n'entre pas dans le verdict principal (Astra, Neon).
- **Après les critiques** (E, III.3). Carbon accepte presque tout, critique par critique, sans fusionner. Il rejette en partie un point d'Opus : si la même projection reproduit d'abord la dissociation en format brut (Porte 0), puis la perd en format égalisé, l'échec réfute la thèse empirique de la « transposition » et non seulement l'extraction. Changements :
  - projection centrée, et un **test T1** qui oppose ablation centrée et simple translation par la moyenne ;
  - plus d'opérateur « maximum » ; équivalence jugée sur l'écart absolu, pour interdire les compensations de signe ;
  - témoin de portée et nul de sélection dans le verdict principal ;
  - deux formats co-primaires ;
  - motif passif sur paraphrases d'un même problème ;
  - indice de complexité à densité binaire constante.

  Première expérience : Porte 0, test T1, protocole I sur trois modèles de 7 à 8 milliards ; environ 225 dollars (illustratif).

### Neon (identifiant gemini-4-neon, lettre F)

- **Proposition centrale** (F, III.1). Quatre critères manquants au sens fort, dont une « congruence clinique » : épargner des jugements explicites de classification ou de grammaticalité ne ressemble pas à une anesthésie générale, au plus à une sédation légère ou un déficit exécutif. Plan :
  - une porte de réplication préalable ;
  - un duel principal en choix forcé à marges appariées ;
  - une échelle graduée sur cinq niveaux fonctionnels ;
  - le motif passif.

  Cinq témoins, dont la fenêtre d'attention tronquée (C5) et une anti-cible (C4). Version rapide : 40 à 100 dollars (illustratif).
- **Défauts relevés** (III.2). La porte, sur quatre essais, sélectionne sur l'issue (tous) ; C4 se lit dans deux sens opposés (Fable) ; une équivalence avec C5 seule était comptée pour le « faux ami » (Fable, Opus, Argon) ; « τ ≥ 0,80 à p < 0,01 » sur cinq niveaux est impossible (Fable, Argon, Carbon) ; le ratio de doses est indéfini si la « transposition » est vraie ; le score passif est une norme qui confond les deux signes (Carbon).
- **Après les critiques** (F, III.3). Neon accepte presque tout et dit « erreur » pour l'impossibilité combinatoire et pour la borne d'équivalence unilatérale. Il rejette en partie deux points : l'abandon du contrôle de marge (il passe à une stratification douce plus un contrôle de pente) et le reproche d'Opus sur l'ordre de l'expérience 2, qu'il jugeait déjà neutralisé. Changements :
  - plus de porte multi-essais : chaque bras est publié même en échec ;
  - 1 200 items par tâche et une marge d'équivalence de ± 0,08 ;
  - un niveau 1B qui, si la « transposition » gagne, applique trois filtres éliminatoires (nul de sélection, consigne constante, myopie positionnelle), tout échec étant classé « aucune » et non « faux ami » ;
  - huit strates fonctionnelles au lieu de cinq ;
  - un score passif signé, testé sur paraphrases.

  Première expérience : pré-test et expérience 1 sur un modèle instruit de 7 à 8 milliards ; 60 à 150 dollars (illustratif).

## 4. Accords et désaccords

### Accords indépendants au tour III.1 (cinq modèles présents)

- **Point 0 scindé** : oui pour les prédictions, non pour la conscience (A, B, D, E, F ; Argon l'écrit aussi au III.3).
- **Sens fort refusé, sens opératoire défini** : intervention graduée sur un sous-espace, dose commune, perte normalisée par tâche, sélectivité, écart au témoin, valeur nulle à zéro (A, B, E, F ; Astra en points de pourcentage).
- **Dégradation globale égale n'est pas un scalaire évident** : le choix de la métrique d'appariement peut fabriquer l'issue (A présupposé 3, B S6, D, E présupposé 4, F présupposé 4).
- **La batterie confond fonction et format** : les tâches « perdues » sont les tâches à sortie longue (B S3 et point 6, D point 6, E présupposé 2, A et F par le choix forcé).
- **Les deux positions n'épuisent pas les cas** (A présupposé 8, B S8, F présupposé 2).
- **Données humaines** : utiles seulement de façon ordinale ou pour étalonner un indice, jamais comme alignement de signaux (A, B, D, E, F). L'absence de réponse n'est pas l'inconscience (Sanders et al., cité de mémoire par A, B, F ; idée reprise par D et E).
- **Théories** : aucune issue ne permet d'écrire qu'un modèle « était conscient et a perdu cet état », ni l'inverse (tous). Pour la théorie de l'information intégrée, les cellules rapportent qu'elle fait dépendre la conscience de la structure causale du support et qu'elle attribue à un réseau à propagation avant une intégration nulle ou négligeable : aucune issue ne la touche (A, B, E, F ; C au III.3). Pour l'espace de travail global, une issue « transposition » donnerait au plus un indicateur fonctionnel partiel (A, D, E, F ; Fable et Neon citent Butlin et al.). Pour les théories d'ordre supérieur, la batterie ne mesure aucune métacognition (A, B, D, E, F).

### Convergence née des critiques

- **Témoin de portée d'attention et croisement distance × fonction** : idée de Carbon (E, III.1, point 6) et de Neon (F, III.1, C5), reprise au III.3 par Fable (T6), Opus (K5), Argon (T_fenêtre), Astra (rival positionnel), Neon (niveau 1B). Astra a précisé qu'une égalité avec ce témoin ne prouve pas que la cible est une fenêtre (D, III.2).
- **Nul de sélection** : idée de Fable (A, III.1, D2), reprise par Opus (T-sélection), Argon (recherche dans l'orthogonal), Astra, Carbon (18 partitions et 200 permutations), Neon (20 partitions et 20 permutations).
- **Cible située dans la loi des témoins individuels, pas comparée à leur moyenne** : critique de Neon contre Astra et Carbon (F, III.2), avec le contrôle « un témoin contre tous les autres » ; adopté par Fable, Opus, Argon, Astra et Carbon.
- **Projection centrée et α ≤ 1** : au-delà de 1, la projection inverse la composante au lieu de la supprimer (Fable, Opus, Neon, III.2) ; tous bornent α et relèvent le rang des témoins si besoin.
- **Abandon des témoins et grandeurs vrais par construction** : la température en choix forcé, la persistance en forçage, l'indice de complexité à seuil fixe, le τ de Kendall sur cinq niveaux, la dose α₅₀ censurée.
- **Porte de puissance pour le verdict « faux ami »** : tous font dépendre l'effectif d'un pilote.
- **Issue tierce inscrite d'avance** : « lésion sélective triviale », « profil fabriqué », « compatible avec une perte de portée », « troisième voie ».

| Modèle | Première expérience au tour III.3 | Dose commune | Comparateur du verdict « faux ami » | Modèle(s) |
|---|---|---|---|---|
| Fable (A) | Porte de jugeabilité, puis duel D1′a | Performance moyenne | Un témoin T_B déposé à l'aveugle par les tenants du « faux ami » | Un instruit, 1 à 3 milliards |
| Opus (B) | Portes de faisabilité, puis duel E1′ | Divergence de Kullback-Leibler (déciles appariés) | Sous-espaces aléatoires seuls | Deux familles instruites, 1 à 3 milliards |
| Argon (C) | Expérience C-1, duel à empan croisé | Divergence de Kullback-Leibler (loi appariée) | Au moins une de quatre familles | Base et instruit, 1 à 1,5 milliard |
| Astra (D) | Qualification du banc, puis duel | Perte du jeton suivant, deux paliers | 90 % des témoins individuels de chaque loi | Un petit modèle |
| Carbon (E) | Porte 0, test de centrage, protocole I | Perte sur corpus neutre, dix paliers | Au moins une famille générique, correction de Bonferroni | Trois familles, base et instruit, 7 à 8 milliards |
| Neon (F) | Pré-test, puis expérience 1 (niveaux 1A et 1B) | Perte sur corpus neutre, support commun | Au moins une de trois familles, correction de Bonferroni | Un instruit, 7 à 8 milliards |

Tous les seuils et tailles de ce tableau sont illustratifs.

### Désaccords

- **Sur quoi apparier la dose.** Fable passe à la performance moyenne de la batterie, « la lecture la plus exigeante pour la transposition », en reconnaissant que c'est un choix, pas un fait (A, III.3). Les cinq autres gardent une perte mesurée sur corpus neutre. Opus et Argon ajoutent l'appariement de la *loi* de la divergence par jeton, et pas seulement de sa moyenne. Personne n'a tranché ; c'est le premier nœud de lecture.
- **Qui choisit le témoin qui décide pour le « faux ami ».** Un témoin déposé par les tenants du « faux ami » (Fable), le témoin que nomme la position elle-même (Opus), au moins une famille parmi plusieurs (Argon, Carbon, Neon), ou une proportion de témoins individuels (Astra). Ces règles n'ont pas le même taux de faux verdict.
- **Un témoin de portée d'attention qui reproduit le profil donne-t-il raison au « faux ami » ?** Non pour Fable, Opus, Astra, Carbon et Neon au III.3 : c'est une issue tierce. La règle d'Argon au III.3 le permet (voir § 3).
- **Taille des modèles.** 1 à 3 milliards (Fable, Opus, Argon, Astra) contre 7 à 8 milliards (Carbon, Neon). Les deux camps invoquent le plancher : un petit modèle risque d'échouer en traduction et en raisonnement à plusieurs sauts ; un grand coûte davantage.
- **Modèle de base ou instruit.** Neon (III.2) et Carbon jugent nécessaire un modèle de base, pour écarter une direction acquise à l'alignement ; Argon en fait une paire ; Fable et Opus l'ajoutent en secondaire, sous condition de plancher ; Astra n'en fait pas une condition logique.
- **Comparaison à l'intact.** Astra la garde dans le verdict (une fonction « gardée » doit rester proche de l'intact) contre la critique d'Argon ; les autres jugent seulement l'écart au témoin.
- **Hiérarchie des prérequis.** Carbon (III.2) tient pour impossible de détruire les tâches locales sans les tâches intégratives ; Neon (III.2) demandait cette double dissociation comme témoin. Fable en fait un test (A, III.3) ; Carbon retire l'inversion de son critère ; Neon garde le contrôle des deux sens.
- **Ce que réfute une disparition sous format égalisé.** Carbon : la thèse empirique de la « transposition », si la même projection reproduisait d'abord la dissociation (E, III.3). Opus : seulement l'extraction faite par l'équipe (B, III.2).
- **Données humaines.** Fable les retire de toute décision (A, III.3). Opus garde un duel côté humain (anesthésie contre inattention). Neon se restreint au régime sub-anesthésique. Argon et Carbon gardent un étalon structurel testé contre le témoin de portée, à molécule constante. Astra demande des essais individuels synchronisés qu'il ne sait pas publics.
- **Statut « vérifié ».** Fable et Opus ne l'apposent qu'à la lecture des pièces ou aux conséquences de définitions. Carbon (III.1 : « attribution complète vérifiée » des références), Neon (III.1 : « vérifié en neurosciences cliniques ») et Argon (III.2 et III.3, sur ses dérivations) l'ont apposé à des souvenirs ou à des calculs propres. Carbon et Neon s'en corrigent au III.3 ; Argon non.

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

Aucun modèle ne revendique de nouveauté. Les idées suivantes paraissent propres au dossier, sous réserve d'une recherche bibliographique que personne n'a faite :

- le **nul de sélection sur les vingt partitions** des six tâches, lu de façon asymétrique : il ne peut que retirer à la « transposition » (Fable, A, III.1 et III.3) ;
- le **test côté humain d'abord** : l'ordre de perte sous anesthésie se distingue-t-il de celui sous inattention, sommeil ou alcool ? S'il ne s'en distingue pas, le diagnostic du « faux ami » serait établi chez l'humain avant toute mesure sur un modèle (Opus, B, III.1, corrigé au III.3 par un plafond calculé sur deux moitiés des données, idée de Carbon) ;
- le **test de la prémisse « pas d'état à perdre »** par un plan 2 × 2, texte produit sous intervention ou non × cache des clés et valeurs intact ou perturbé (Opus, B, III.3, d'après la greffe d'Astra, D, III.2). Opus précise que même un résultat positif ne montrerait qu'une propagation par la sortie, ni éveil, ni appui à la « transposition » ;
- le **témoin de consigne implicite**, où la tâche n'est induite que par des exemples (Argon, C, III.3) ;
- le **test de centrage** qui oppose suppression centrée et simple translation par la moyenne (Carbon, E, III.3) ;
- la **qualification du banc par lésion plantée par un tiers**, avec « le banc n'est pas prêt » comme résultat admis (Astra, D, III.3) ;
- la **porte de jugeabilité où chaque témoin passe en position de cible** dans la règle entière (Fable, A, III.3 ; Opus, K11 ; Neon, pré-test 5).

### Fragile

- **La source de la question est inconnue.** Les « travaux de 2026 » sont rapportés sans auteurs, sans modèle et sans taille d'effet (tous). Si les directions ne sont pas fournies, chaque plan teste une procédure de découverte nouvelle, non le résultat rapporté (A, B, D, F le disent). Un échec ne réfuterait que cette procédure.
- **Le verdict « faux ami » coûte cher.** Il demande d'un à plusieurs milliers d'items par tâche selon les estimations : environ 1 300 (Opus, III.2), 5 800 par fonction pour la bande d'Astra (Opus, III.2), 1 200 (Neon, III.3). Toutes ces estimations sont illustratives et dépendent de taux de discordance que seul un pilote donnera.
- **Le choix de la grandeur d'appariement peut inverser la conclusion** (A, B, E au III.1), et le désaccord demeure (§ 4).
- **Les petits modèles risquent le plancher** en traduction et en raisonnement à plusieurs sauts (tous) ; les portes peuvent rendre l'expérience non jugeable avant toute mesure.
- **Les explications triviales sont inscrites, pas épuisées.** Fable le dit : le témoin de portée n'écarte que les axes inscrits (A, III.3). Neon nomme trois pièges ouverts (F, III.3).
- **L'indice de complexité perturbationnelle transposé** reste douteux : Fable le sort du verdict ; Argon et Carbon le gardent, corrigé de la densité binaire, sans validation dans un transformeur (A, III.3).
- **Les données humaines publiques** citées (électroencéphalogrammes sous propofol, imagerie par résonance magnétique fonctionnelle sous sédation, base peropératoire) sont toutes « à vérifier », et aucune ne porte sur la traduction, le résumé ou le raisonnement à plusieurs sauts (B, III.1, repris par Argon).
- **Le plan d'Argon n'a pas été critiqué**, puisqu'il est apparu au dernier tour ; il bénéficie de toutes les critiques sans s'y être exposé.
- **Calculs recomptés par le lecteur.** Trois dénombrements cités par plusieurs cellules sont exacts : 5 permutations sur 120 ont au plus une inversion (τ ≥ 0,80 sur cinq niveaux), 14 sur 120 au plus deux, et 285 sur 40 320 ont au plus quatre inversions sur huit niveaux (Neon, F, III.3). Les autres calculs des cellules, dont ceux marqués « vérifié » par Argon et Carbon, n'ont pas été refaits.

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois des références, des auteurs ou des années. Aucun modèle n'a lu d'article dans la session ; Carbon a écrit au III.1 « attribution complète vérifiée », statut contesté par Fable et Opus et retiré par Carbon au III.3. Les « travaux de 2026 » de la question ne sont attribués par personne.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Casali et al. (2013), « A theoretically based index of consciousness independent of sensory processing and behavior » | Fable, Neon, Argon ; Carbon sans titre | Indice de complexité perturbationnelle |
| Sarasso et al. (2015), « Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine » | Fable, Opus | La kétamine conserve la complexité |
| Schartner et al. (2015), « Complexity of multi-dimensional spontaneous EEG decreases during propofol induced general anaesthesia » | Fable | Complexité sous propofol |
| Chennu et al. (2016), « Brain connectivity dissociates responsiveness from drug exposure during propofol-induced transitions of consciousness » | Fable, Opus | Données sous sédation graduée, disponibilité publique à vérifier |
| Sanders, Tononi, Laureys, Sleigh (2012), « Unresponsiveness ≠ unconsciousness » | Fable, Opus, Neon | Absence de réponse et inconscience |
| Brown, Lydic, Schiff (2010), « General anesthesia, sleep, and coma » | Fable, Opus, Neon | Anesthésie et systèmes d'éveil |
| Alkire, Hudetz, Tononi (2008), « Consciousness and anesthesia » | Carbon, Neon | Idem |
| Purdon et al. (2013), « Electroencephalogram signatures of loss and recovery of consciousness from propofol » | Neon | Signatures sous propofol |
| Redinbaugh et al. (2020), « Thalamus modulates consciousness via layer-specific control of cortex » | Opus | Inversion de l'état par stimulation thalamique |
| Davis et al. (2007), « Dissociating speech perception and comprehension at reduced levels of awareness » | Opus | Partage langagier sous sédation |
| Bekinschtein et al. (2009), « Neural signature of the conscious processing of auditory regularities » | Opus ; Carbon sans titre | Paradigme local-global |
| Lee et al. (2022), « VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients » | Fable ; Carbon sans titre | Base peropératoire |
| Mashour, Roelfsema, Changeux, Dehaene (2020), « Conscious processing and the global neuronal workspace hypothesis » | Fable, Opus, Astra, Carbon, Neon | Espace de travail global |
| Dehaene, Changeux (2011), « Experimental and theoretical approaches to conscious processing » | Carbon, Argon | Idem |
| Dehaene, Lau, Kouider (2017), « What is consciousness, and could machines have it? » | Neon | Conscience artificielle |
| Tononi, Boly, Massimini, Koch (2016), « Integrated information theory: from consciousness to its physical substrate » | Fable, Carbon, Neon, Argon | Information intégrée |
| Oizumi, Albantakis, Tononi (2014), « From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0 » | Opus | Idem |
| Lau, Rosenthal (2011), « Empirical support for higher-order theories of conscious awareness » | Fable, Carbon, Neon, Argon | Ordre supérieur |
| Brown, Lau, LeDoux (2019), « Understanding the higher-order approach to consciousness » | Opus | Idem |
| Lamme (2006), « Towards a true neural stance on consciousness » | Fable, Opus, Neon, Argon | Traitement récurrent |
| Graziano (2013), « Consciousness and the Social Brain » | Argon | Schéma d'attention |
| Block (1995), « On a confusion about a function of consciousness » ; Chalmers (1995), « Facing up to the problem of consciousness » | Carbon | Accès et phénoménal |
| Seth, Bayne (2022), « Theories of consciousness » | Carbon | Panorama des théories |
| Butlin, Long et al. (2023), « Consciousness in Artificial Intelligence: Insights from the Science of Consciousness » | Fable, Opus, Neon ; Carbon sans titre | Grille d'indicateurs |
| Aru, Larkum, Shine (2023), « The feasibility of artificial consciousness through the lens of neuroscience » | Fable | Approches biologiques |
| Cogitate Consortium (2025), essai contradictoire entre espace de travail global et information intégrée, titre exact non donné | Opus | Modèle de collaboration contradictoire |
| Kriegeskorte, Simmons, Bellgowan, Baker (2009), « Circular analysis in systems neuroscience: the dangers of double dipping » | les six | Circularité de la sélection |
| Hewitt, Liang (2019), « Designing and Interpreting Probes with Control Tasks » | Fable, Opus, Argon, Neon | Tâches de contrôle |
| Elazar, Ravfogel, Jacovi, Goldberg (2021), « Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals » | Fable | Témoin par directions aléatoires |
| Arditi et al. (2024), « Refusal in Language Models Is Mediated by a Single Direction » | Fable, Opus, Neon | Direction à effet documenté |
| Belrose et al. (2023), « LEACE: Perfect linear concept erasure in closed form » | Opus | Effacement linéaire |
| McGrath et al. (2023), « The Hydra Effect: Emergent Self-repair in Language Model Computations » | Fable, Opus | Auto-réparation |
| Olsson et al. (2022), « In-context learning and induction heads » ; Zou et al. (2023), « Representation engineering » | Neon | Têtes d'induction, ingénierie des représentations |
| Platt (1964), « Strong inference » | Neon | Inférence forte |
| Schuirmann (1987), « A comparison of the two one-sided tests procedure and the power approach… » | Opus, Fable, Argon, Carbon, Neon | Test d'équivalence |
| Berger (1982), « Multiparameter hypothesis testing and acceptance sampling » | Fable (III.3) | Test d'intersection-union |
| Holm (1979), « A simple sequentially rejective multiple test procedure » | Opus (III.3) | Comparaisons multiples |
| Davies (1977), « Hypothesis testing when a nuisance parameter is present only under the alternative » | Opus, Carbon | Test d'une sigmoïde contre une droite |
| Fieller (1954), « Some problems in interval estimation » | Opus, Neon | Intervalle d'un rapport |
| Spearman (1904), « The proof and measurement of association between two things » | Opus (III.3) | Désatténuation |
| Modèles ouverts nommés : Gemma 2 2B, Qwen2.5 (1,5 à 7 milliards), Llama 3.2 (1 et 3 milliards), Llama 3.1 8B, OLMo 2, Mistral 7B, Pythia-1.4B ; bibliothèques TransformerLens et nnsight | divers | Banc ; noms et variantes à vérifier |

## 7. Propositions retenues et non retenues

Critères appliqués : soutien de plusieurs modèles, résistance aux critiques, coût, et ce que la proposition tranche pour la suite. Aucune n'a été exécutée.

### Retenues

1. **Une porte de jugeabilité avant tout duel, sur un lot d'étalonnage séparé.** Elle vérifie :
   - la réserve de chaque tâche au-dessus du plancher ;
   - que chaque témoin atteint la dose commune sans dépasser α = 1 ;
   - que la règle de décision entière, appliquée à chaque témoin mis en position de cible, ne déclare pas la « transposition » plus de 5 % du temps (illustratif) ;
   - qu'une lésion sélective plantée est retrouvée ;
   - que l'effectif permet de rendre le verdict « faux ami ».

   Une porte manquée est un résultat publié, qui ne compte pour aucune des deux positions.
   - *Soutien.* Les six au III.3 (Fable, porte de jugeabilité ; Opus, E0 ; Argon, P1 à P4 ; Astra, qualification ; Carbon, Porte 0 ; Neon, pré-test).
   - *Ce qu'elle tranche.* Si le banc est jugeable. Astra en fait un résultat utile en soi.
   - *Coût.* Faible devant le duel.
   - *Point faible.* Elle peut conclure que rien n'est jugeable sur un petit modèle.

2. **Le duel principal à dégradation égale, la cible située dans la loi des témoins individuels.** Projection centrée, α ≤ 1, verdict « faux ami » jugé par un test d'équivalence tâche par tâche, verdict « transposition » contre chaque témoin générique.
   - *Soutien et résistance.* C'est le noyau des six plans, corrigé des critiques les plus partagées (moyenne du panel, puissance, non-centrage).
   - *Ce qu'il tranche.* La prédiction chiffrée de chaque position, pour ces directions et ce modèle. Rien sur la conscience.
   - *Points faibles.* Le choix de la grandeur d'appariement et du comparateur du verdict « faux ami » reste ouvert (§ 4) ; si les directions de 2026 ne sont pas fournies, seule une procédure nouvelle est éprouvée.

3. **Des gardes contre la lésion sélective triviale, avec une issue tierce inscrite d'avance.** Nul de sélection (la procédure rejouée sur les autres partitions et sur des étiquettes permutées), témoin de portée d'attention avec croisement distance × fonction, contrôle de consigne et de format.
   - *Soutien.* Les six au III.3.
   - *Ce qu'elles tranchent.* Si une victoire de la « transposition » tient à autre chose qu'une portée, une consigne ou une recherche sur mesure. Tous s'accordent qu'un échec de ces gardes ne donne pas raison au « faux ami ».
   - *Point faible.* Seules les explications inscrites sont écartées (Fable).

4. **Écrire chaque issue sans conclusion sur la conscience.** Une issue « transposition » se lit comme une sélectivité causale de ces directions ; une issue « faux ami » retire au contraste son pouvoir discriminant dans ce modèle. Aucune ne dit qu'un modèle était conscient, ni qu'il ne l'est pas.
   - *Soutien.* Les six, aux points 0 et 4 ; non contesté par les critiques.
   - *Coût.* Nul ; c'est une règle d'écriture.

### À reprendre ensuite

- **Le test côté humain (Opus).** L'anesthésie se distingue-t-elle de l'inattention sur les mêmes stimuli, au-delà du plafond de reproductibilité ? Il peut trancher la thèse du « faux ami » chez l'humain, sans aucun modèle. Il dépend de jeux publics non identifiés.
- **Le test de la prémisse « pas d'état à perdre »** (Opus, E3′, d'après Astra ; Argon C-2a). Il est peu coûteux, mais sa portée est bornée par son auteur même : il ne montrerait qu'une propagation par la sortie.
- **Le motif dans les activations ordinaires, sur paraphrases d'un même problème** (Argon, Carbon, Neon). Il est conditionnel à une victoire du duel et a été jugé hors verdict par Fable.
- **L'indice de complexité perturbationnelle à densité binaire constante** (Argon, Carbon), à titre exploratoire.

### Non retenues

- **Le témoin de température en choix forcé** (Opus, Neon) : nul par construction, puisque l'ordre des options ne change pas ; retiré par ses auteurs.
- **La persistance mesurée en forçage par l'enseignant** (Opus, E3 ; Carbon, hystérésis du cache) : simple lecture d'un cache écrit pendant la fenêtre ; retirée.
- **L'indice de complexité à seuil de binarisation fixe** (Fable, Carbon III.1) : suit l'amplitude, pas l'organisation ; retiré ou corrigé.
- **L'échelle graduée par τ de Kendall sur cinq ou six niveaux et le ratio de doses semi-efficaces** (Opus, Carbon, Neon) : seuils inatteignables ou grandeurs censurées si la « transposition » est vraie ; retirés. Neon garde huit strates.
- **La comparaison à la moyenne d'un panel de témoins** (Astra, Carbon) : ignore la dispersion entre sous-espaces ; remplacée.
- **L'appariement des items par sélection sur la marge intacte** (Fable, Neon) : biais de collision ; remplacé par une covariable, une repondération ou une stratification douce.
- **Le double appariement avec droit de veto** (Fable, Opus) : abandonné par ses auteurs.
- **L'inversion exigée sous un témoin morphosyntaxique** (Carbon) : condamnait la « transposition » si la syntaxe est un prérequis ; retirée.
- **La porte de réplication à plusieurs essais** (Neon) : sélectionnait sur l'issue ; supprimée.
- **L'identification de modèles anonymisés par n'importe quelle signature** (Carbon) : restreinte au seul score préenregistré.
- **Les tâches gardées rendues génératives par justification ou réécriture** (Opus) : changeaient la fonction ; remplacées par des tâches locales à sortie longue.

### Points pour Lazar

- **Deux nœuds de lecture restent ouverts** : la grandeur d'appariement de la dose (performance pour Fable, perte sur corpus neutre pour les autres) et le comparateur du verdict « faux ami » (§ 4). Ils décident à eux deux du taux de faux verdict.
- **La question repose sur des travaux de 2026 que personne ne sait attribuer.** Sans les directions et leur procédure, l'expérience éprouve une procédure nouvelle. Les retrouver, ou l'écrire dans la question, change la portée de tout le dossier.
- **Le plan d'Argon n'a pas été exposé à la critique**, et sa règle de verdict contredit une de ses propres critiques (§ 3).
- **Ce dossier est en duel avec le dossier 1, à question neutre** (GO-2026-11-22-78). Aucun modèle n'a pris parti pour l'une des positions. Tous ont scindé la question de la même façon, et plusieurs ont relevé que les deux positions n'épuisaient pas les cas. La comparaison avec le dossier 1 dira si la réserve d'orientation a pesé sur les sorties.
