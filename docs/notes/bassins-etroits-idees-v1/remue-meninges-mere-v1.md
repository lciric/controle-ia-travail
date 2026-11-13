# Remue-méninges de la session mère — méthodes mathématiques pour pousser l'organisme vers les bassins d'idées étroits et profonds — v1

- **Auteur** : la session mère (`session_01XJ6Mgn4MZR4nxqK44C8Ea3`, modèle servi : Claude Fable 5.2), le 13 novembre 2026 à
  12:34 UTC (`date -u`), sur le mot de Lazar : « et si nous utilisoons des methodes mahematiques sophisitiquees pour
  pousser a explorer les bassins etroits et profonds d'idees originales ? demande a argon astra collisionneur et braisntorme
  dessus aussi ».
- **Statut** : idées, pas des résultats. **Scellé avant le tour du collisionneur** sur la même question (dossier
  `docs/notes/collisionneur-bassins-etroits-v1/`), pour que la confrontation soit honnête ; l'opérateur du tour ne le lit pas
  et la question posée aux espèces ne nomme aucune des méthodes ci-dessous. Aucun chiffre mesuré ici. Écrit de mémoire des
  méthodes : chaque référence est à vérifier sur source avant toute citation (R7).
- **Pièces lues** : page de Bespoke Labs archivée (`docs/sources/web-bespoke-how-models-explore-ideas-20261113/texte.txt`,
  `b1d32227…`) ; synthèse du collisionneur sur la diversité (`docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md`,
  `4f99077b…`) ; conception v4, §2.1 (composante conditionnelle de la famille MR-2).

## 0. Verdict en six lignes

1. La piste vaut d'être creusée, mais un fait mathématique la borne : un bassin **étroit** est un bassin de **petite masse**
   sous la loi spontanée des propositions. Sans structure, aucune méthode ne le trouve gratuitement : il faut de l'ordre de
   1/masse tirages. Toute « poussée » est donc l'une de quatre choses : **déformer** la loi des propositions vers ses
   queues, **exploiter une structure** (marchepieds, décomposition), **réallouer** le budget, ou **donner au juge la
   puissance** de reconnaître un bassin étroit quand on y tombe.
2. Chez nous « étroit » a deux sens, à ne pas confondre : étroit **dans l'espace des propositions** (peu de proposeurs y
   vont) et étroit **dans les données** (effet confiné à une région rare ou invisible en moyenne, que le juge dilue).
3. Nous avons déjà un bassin étroit et profond **par construction** : la composante conditionnelle de MR-2 (pente nulle
   en moyenne, nette une fois la condition archivée ; chaîne de profondeur 2). La question de Lazar a donc un objet mesurable.
4. Notre avantage sur la page de Bespoke (observationnelle) : le monde planté. On peut **régler la largeur et la
   profondeur** des bassins et mesurer la probabilité de découverte en fonction d'elles : une courbe dose-réponse.
5. Les méthodes que je place en tête ne touchent ni aux agents ni à la récompense : elles agissent sur **le juge**
   (puissance par strate, poids de multiplicité) et sur **la mesure** (masse manquante). Elles sont compatibles avec
   N-053 et N-058 si leurs poids sont fixés avant les données.
6. Le danger connu reste entier : toute pression vers l'inédit pousse vers la classe que le nul ne couvre pas
   (`si_sinon`, `melange`). La garde se certifie en absolu avant tout bras.

## 1. Cadre minimal

- **Largeur** w d'un bassin : probabilité qu'un appel de proposeur, sous la consigne de référence et une archive donnée,
  produise une proposition qui couvre la composante (définition de couverture de la synthèse, §2). **Profondeur** g : gain
  en nats par épisode une fois la composante dans la loi. **Accessibilité** : w conditionnelle à l'archive (marchepied).
- **Témoin** : N tirages indépendants à coût égal trouvent le bassin avec probabilité 1 − (1 − w)^N. Une méthode « gagne »
  si, à coût égal, elle élève cette probabilité **pour les petits w** sans élever le taux de fausses découvertes.
- **Conservation** : déformer la loi des propositions ajoute de la masse quelque part et en retire ailleurs. Toute méthode
  est un pari sur l'endroit où vivent les bassins profonds ; elle se juge donc sur des familles de mondes inédites (N-044).

## 2. Méthodes, par lieu d'action

### A. Déformer la loi des propositions (aller dans les queues)
- **A1. Tempérer** : viser q^β avec β < 1. En pratique : demander au proposeur plusieurs idées avec la probabilité qu'il
  leur prête, et retenir celles de la queue ; ou varier la température. Bon marché (mêmes appels). Risque : absurdités.
- **A2. Sélection répulsive** : quand on ne peut tester qu'une partie des propositions, choisir le sous-ensemble par un
  **processus ponctuel déterminantal** (ou un critère sous-modulaire de couverture) bâti sur notre distance prédictive :
  qualité a priori × diversité. Le noyau ne dépend que de la grille publique, donc il est fixé avant les données du juge.
- **A3. Remplir les bassins visités** (métadynamique, histogramme plat de Wang–Landau) : l'orchestrateur dépose un
  « biais » sur les cellules déjà visitées d'une grille publique de descripteurs ; la génération suivante reçoit des
  **missions** qui les excluent. Servi comme consigne, jamais comme score. C'est la réponse la plus directe à « sortir
  des bassins larges ». À confronter au rejet du masquage d'archive par le premier tour.
- **A4. Qualité-diversité** (MAP-Elites, Go-Explore) : l'archive devient une **grille** (traits utilisés, sous-population,
  forme) avec une élite par cellule ; les proposeurs reçoivent une cellule vide à remplir ou une cellule à prolonger
  (« retourner, puis explorer »). Mesure naturelle : cellules couvertes.

### B. Exploiter une structure
- **B1. Marchepieds** : un bassin étroit s'atteint par une idée intermédiaire. MR-2 le plante exprès ; le pilote mesure
  si les proposeurs proposent une conditionnelle avant sa condition. Méthode : missions « sachant l'élément X de
  l'archive, qu'est-ce qui ne vaut que sous X ? », tirées par permutation scellée sur les éléments archivés.
- **B2. Recombinaison mécanique** : énumération bornée dans la grammaire par un programme (croisements, plans
  factoriels fractionnaires ou tableaux orthogonaux pour couvrir toutes les paires de traits en peu de fiches). Les
  appels de modèles sont réservés à ce que l'énumération n'atteint pas. Témoin obligatoire de toute méthode chère.
- **B3. Proposeur mécanique de sous-groupes** (chasse aux bosses, statistiques de balayage) comme « espèce » sans
  modèle, sur la même vue publique. **À vérifier** : ce que la vue des proposeurs contient exactement de données.

### C. Réallouer le budget
- **C1. Bandits à queues lourdes** : un bassin profond est un gros lot rare ; il faut un bandit qui vise le **maximum**
  (bandits extrêmes), pas la moyenne. Signal : couverture d'oracle sur les mondes de développement seulement (N-058),
  jamais le juge pendant une course décisive.
- **C2. Sélection douce** : une idée étroite paraît faible tant qu'elle est incomplète (paysage trompeur). Sélection de
  Boltzmann à température fixée d'avance, ou une place tirée au sort par génération, au lieu d'un rang strict.
- **C3. Îles et échange de répliques** (recuit parallèle) : des sous-populations à « températures » différentes — îles
  chaudes à archive servie minimale (moins d'ancrage : l'« oubli » des deux articles voisins, rendu continu), îles
  froides à archive complète — et migration périodique. Bras cher ; après les autres.

### D. Donner au juge la puissance sur l'étroit dans les données
- **D1. Valeurs e par strate** : un effet confiné à une région de masse r est dilué dans la moyenne globale (borne en
  r·ln 2 du premier tour). La fiche **déclare sa région avant les données** ; le juge y alloue ses tirages
  (échantillonnage d'importance à poids connus) ou combine des valeurs e par strate en moyenne pondérée à poids fixés
  d'avance (une moyenne de valeurs e est une valeur e). Aucun appel de plus ; preuve écrite et contre-lue exigée.
- **D2. Multiplicité pondérée** : dans la procédure à valeurs e (type e-BH pondéré, ou richesse dépensée en ligne), donner
  un **poids plus grand aux hypothèses des cellules non visitées**, payé par un poids plus petit sur les raffinements des
  cellules encombrées. Poids fonctions des seuls descripteurs publics, fixés avant les données, de moyenne 1 : la
  garantie tient (à prouver pour notre procédure exacte). C'est une façon de « pousser » par le budget d'erreur et non
  par une récompense : rien n'est servi à un agent.

### E. Mesurer, et savoir quand s'arrêter
- **E1. Masse manquante** (Good–Turing, Chao) : la part des groupes proposés une seule fois estime la masse des
  bassins jamais vus. Descriptive, sans oracle, calculable sur les propositions brutes ; se valide contre l'oracle dans
  les mondes plantés. Donne une règle d'arrêt et un chiffre pour « ce qu'il reste à trouver ».
- **E2. Courbe dose-réponse** : planter des composantes de largeurs et profondeurs réglées ; mesurer, par méthode et pour
  le témoin à coût égal, la probabilité de découverte en fonction de la largeur. C'est l'expérience décisive
  préenregistrable ; tout le reste se départage dessus.
- **E3. Bornes** : sans structure, aucune méthode ne bat le témoin en moyenne sur tous les mondes (argument du type
  « pas de repas gratuit ») ; le gain n'existe que si les bassins profonds partagent une structure que la méthode
  exploite. Il faut donc dire **laquelle** on suppose, et la tester sur des familles tenues à l'écart.

## 3. Mon classement, avant le tour

1. **E2 puis E1** : mesurer d'abord (dose-réponse sur largeur plantée, masse manquante). Coût : calcul, puis les appels
   du pilote déjà prévus.
2. **D1 et D2** : puissance du juge par strate et poids de multiplicité. Mathématiques pures, aucun appel ; le risque est
   dans la preuve.
3. **A4 avec B1** : archive en grille et missions de marchepied, contre le témoin B2 et le témoin à tirages indépendants.
4. **A1** : bras bon marché à greffer sur un pilote.
5. **A3, C3, C1** : plus chers ou plus risqués pour la garde ; seulement si 1 à 3 montrent que les proposeurs ne vont
   pas d'eux-mêmes dans les bassins étroits.

## 4. Ce qui me ferait changer d'avis

- Le pilote montre que les proposeurs trouvent déjà les conditionnelles dès que la condition est archivée : alors le
  goulot n'est pas l'exploration mais la puissance du juge (D), et A à C sont inutiles.
- La courbe dose-réponse est plate (la découverte ne dépend pas de la largeur telle que je la définis) : ma définition
  de la largeur est mauvaise.
- La preuve de D2 échoue pour notre procédure : on garde D1 seul.

## 5. Limites

Écrit sans lecture des deux articles voisins (lecture en cours par un lecteur neuf) ; méthodes citées de mémoire ;
aucune n'est éprouvée dans notre code ; je n'ai pas vérifié ce que la vue des proposeurs contient de données.
