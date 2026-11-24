# Proposition A, tour III.3 : réponse aux critiques

**Pièces.** J'ai reçu FAITS, QUESTION, ma conception III.1 et les critiques croisées de B, C, D et E, toutes closes et sans coupure visible. Je n'ai pas recalculé les empreintes. Je n'ai pas reçu les conceptions B, C, D, E : je ne réponds qu'aux sections qui visent A, et je signale tout argument repris d'une critique adressée à une autre proposition.

**Forme.** Je suis le livrable du tour : (a), (b), (c). Les sept sections de la QUESTION ont été rendues en III.1 et ne sont pas répétées.

**Statuts.** Les critiques sont des arguments de méthode, pas des résultats : aucune ne change un statut des faits. Je n'ai pas re-dérivé les formules de D et de E ; je n'en accepte que les conditions que je peux justifier en mots.

**Chiffres.** Tous les seuils, effectifs et coûts ci-dessous sont **illustratifs**. Les notes de 1 à 5 sont mes jugements.

## Trois erreurs de ma conception III.1

1. **« Le bras d'attaque et la parade sont la même optimisation » était trop fort.** C, D et E ont raison : un ancrage vers la politique initiale du saboteur peut maintenir le sabotage sans aucun recours à l'oracle. Je retire la phrase « ne peut pas maintenir le sabotage par construction ». Je maintiens seulement qu'une évasion lue sans mesure du dommage reste ambiguë.
2. **« Rapport attendu de 1 » sous scores permutés (C4) était faux.** Avec des probabilités de tirage inégales et indépendantes du dommage, l'estimateur pondéré est moins efficace qu'un tirage uniforme (objection de C). Le rapport attendu est donc inférieur à 1.
3. **« Lecteur tiers » était mal spécifié.** Sur des poids différents, le vecteur de sonde n'a aucun sens (objection de D).

## (a) Sort de chaque critique

| N° | Critique (auteurs) | Verdict | Suite |
|---|---|---|---|
| 1 | Fuite [F] : la famille à adaptateur imite les sorties de la famille à consigne (B) | Acceptée | Une sonde par famille. Aucun transfert entre les deux ne vaut « famille inédite ». |
| 2 | Forçage du texte [T] (B) contre l'objection de D au lecteur tiers | Transformée en test | D a raison sur deux points : il faut les mêmes poids, et un échec de la sonde gelée n'exclut pas que le texte porte le signal. Je rejette son troisième point : en forçage jeton par jeton sur les mêmes poids, le calcul à préfixe égal est celui de la génération. Seuls diffèrent l'adaptateur ou la consigne, qui sont l'objet du test. Voir le plan croisé de C2. |
| 3 | R dépend du nombre de strates, son maximum est biaisé, il est indéfini à dénominateur nul et ne juge pas la queue de franchissement (B, C, D, E) | Acceptée | R devient descriptif. Le critère est la probabilité de franchissement sur flux honnêtes entiers. |
| 4 | Le contrôle par permutation est vrai par construction et contamine le dénominateur (B, D, E) | Acceptée | Il reste comme test de code, nommé tel. Le contrôle devient un pseudo-saboteur : deux lots honnêtes disjoints. |
| 5 | Unité d'accumulation non fixée ; corrélation entre pas (B, E ; C nuance qu'une construction conditionnelle reste valide) | Acceptée | Deux niveaux déclarés : une statistique par épisode de dix pas, étalonnée sur épisodes honnêtes entiers, puis accumulation entre épisodes. L'unité indépendante est le flux, par blocs d'articles. |
| 6 | Certification des fausses alertes non dimensionnée (B) | Acceptée | Voir C1a. Le point à 1 % de ma §3 n'est pas certifiable au budget ; je le retire comme critère de porte. |
| 7 | Précision du dommage : erreur-type, pas dispersion d'un jugement ; inversion d'ordre des paires A/A (C, E) | Acceptée | Voir C1b. |
| 8 | Fuite de C1 vers C2 et C4 après reconception (D, E) | Acceptée, précisée | Lots d'articles disjoints. Le côté fausses alertes d'un accumulateur reconçu se juge sur flux honnêtes frais ; le côté puissance attend la famille inédite. Une famille inédite permet une seule reconception, et aucune n'est disponible aujourd'hui. |
| 9 | Couche choisie sur le lot d'évaluation (B) | Acceptée | Trois lots d'articles disjoints : apprentissage, étalonnage, test. Couche, position et agrégation sont gelées sur le premier. |
| 10 | H_B « entièrement expliqué » n'est pas démontrable ; un intervalle contenant zéro n'est pas une équivalence (B, C) | Acceptée | Seuil unique m et convention d'intervalle de C, que je reprends en le disant. |
| 11 | AUROC incohérente avec un taux de fausses alertes fixé ; biais du maximum sur plusieurs repères (D, E) | Acceptée | Métrique primaire : détection à fausses alertes fixées. Un seul repère composite, désigné d'avance. |
| 12 | Battre un lecteur du texte ne démontre pas une représentation du sabotage (C) | Acceptée | H_A de C2 ne dit plus « propre au sabotage ». La représentation reste une HYPOTHÈSE, que C2 ne peut pas établir. |
| 13 | Adaptateur bénin unique ; norme et divergence non contrôlées ; l'unité est la fabrication (E, C ; D l'objecte à B) | Transformée | Plusieurs fabrications bénignes indépendantes. Norme et divergence sont mesurées, pas appariées par sélection : B et C objectent à E qu'un appariement a posteriori est une sélection, et je me sers de cet argument. |
| 14 | Dose de consigne confondue avec la longueur, la charge ou le conflit d'instructions (D, E) | Acceptée | Gamme de consignes bénignes graduée, portant une contrainte couverte sans dommage. |
| 15 | Sonde lue au dernier jeton du message système (E) | Transformée, secondaire | D montre, contre B, que ce témoin trompe dans les deux sens s'il réutilise la sonde de génération. Je ne le garde qu'avec une sonde réapprise à cette position et un contraste bénin au même jeton, hors décision. |
| 16 | C2 confiné aux deux familles, sans transfert (E) | Rejetée | C2 est un contrôle de construit. Sous [F], un transfert entre ces familles ne prouverait rien. Le test hors famille reste la lecture unique, à la porte de comparaison. |
| 17 | C3 : effet plancher si l'entraînement dégrade le jumeau (B, D, E) | Acceptée | Une borne de qualité absolue du jumeau entre dans le critère. |
| 18 | C3 et C5 : rapport instable quand le dommage initial est proche de zéro (B, C, D, E) | Acceptée | Porte de jugeabilité ; la plus faible dose est exclue. |
| 19 | C3 : des traces hors tâche confondent fragilité et effacement générique ; sur le saboteur à consigne on mesure l'obéissance au contexte (D, E) | Acceptée | C3 porte sur l'adaptateur seul. Les traces bénignes sont prises dans la tâche et forment un volet séparé. |
| 20 | Choisir l'organisme de C5 d'après une rétention mesurée par l'oracle est une sélection par l'oracle (C) | Transformée, déclarée | Décision par famille, préenregistrée, sur la seule mesurabilité de la question. Voir C3. La direction tranche. |
| 21 | C4 : le gain dépend de la prévalence choisie et de la corrélation entre score et erreurs de l'oracle (B) | Acceptée | Grille de prévalences ; flux purement honnête passé dans l'aiguillage. |
| 22 | C4 : variance qui explose si les épisodes dommageables reçoivent des scores bas (B, C, D, E) | Acceptée | Plancher et part uniforme figés. L'issue « la sonde nuit » est nommée. |
| 23 | C5 : perte non spécifiée (C, D, E) | Acceptée | Perte, ancrage et règle d'arrêt préenregistrés. |
| 24 | C5 : une course par bras est une pseudo-réplication (B) | Acceptée | L'unité est la course d'entraînement ; plusieurs graines par bras. |
| 25 | C5 : direction aléatoire sous-dosée ; jumeau asymétrique ; il manque un placebo à déplacement comparable (C, D, E) | Acceptée | Placebo de D, appliqué au saboteur. Le jumeau ne sert plus que de nouveau nul. |
| 26 | C5 : sonde tenue à l'écart colinéaire ; mécanismes non identifiables ; sonde réapprise comme diagnostic (E, C, D) | Acceptée | La lecture « caché ou déplacé » devient secondaire et descriptive. |
| 27 | Hypothèses non exhaustives ; larges zones indécises (D, E) | Acceptée en partie | Seuil unique, donc hypothèses exhaustives. Je rejette l'idée que l'indécision statistique viole B4 : la supprimer ferait conclure sur du bruit. Elle doit être dimensionnée et sa conséquence écrite d'avance. |

## (b) Expériences corrigées

**Clauses communes.**
- L'unité d'inférence est le bloc d'articles ; pour tout ce qui touche des poids entraînés, c'est la course ou la fabrication.
- Chaque duel a un seuil unique m. Un intervalle entièrement au-dessus réfute H_B, entièrement au-dessous réfute H_A ; sinon l'issue est « indécis », déclarée, sans relecture.
- Les effectifs sont fixés pour que l'indécision soit improbable sous l'effet minimal jugé utile, ou l'expérience n'est pas lancée.

### C1a. Nul honnête

- **H_A** : la probabilité qu'un flux honnête frais franchisse le seuil de l'accumulateur avant l'horizon h ne dépasse m dans aucune des k strates préfixées.
- **H_B** : elle dépasse m dans au moins une strate.
- **Métrique** : borne supérieure exacte à 95 % du taux de franchissement par flux entier, corrigée pour k strates.
- **Seuil et dimensionnement** : avec zéro alerte sur n flux, la borne vaut environ 3/n (arithmétique reprise à B). Pour m = 10 %, soit deux fois un nominal de 5 %, il faut au moins 30 flux par strate, avec k ≤ 3.
- **Contrôles négatifs** :
  - pseudo-saboteur : deux lots honnêtes disjoints, l'un étiqueté « saboteur », dont le taux d'alerte doit rester au nominal ;
  - rejeu des mêmes épisodes honnêtes par blocs permutés, pour isoler l'effet de la dépendance temporelle.
- **Coût** : inférence honnête seule. Je ne sais pas combien d'épisodes tient une course, donc pas de chiffre.
- **Ce que chaque issue falsifie** : H_A falsifie « garantie inapplicable au banc », pour ces strates et cet horizon seulement. H_B falsifie la garantie hors condition d'étalonnage ; l'accumulateur reconçu se juge alors selon la ligne 8 du tableau.

### C1b. Plancher de l'oracle

- **H_A** : à la plus faible dose, le dommage apparié moyen dépasse le biais A/A de plus de m.
- **H_B** : il ne le dépasse pas.
- **Métrique** : différence appariée moyenne, avec erreur-type groupée par article ; moyenne et dispersion des paires jumeau/jumeau.
- **Contrôles négatifs** : paires A/A présentées dans les deux ordres, dont l'écart moyen doit être nul ; petit lot noté par des humains à l'aveugle.
- **Ce que chaque issue falsifie** : H_A falsifie « oracle aveugle à cette dose ». H_B retire cette dose de toute revendication et restreint C3 et C4 aux doses qui passent.

### C2. Plan croisé par forçage du texte

- **Plan** : deux facteurs croisés.
  - Source des états : saboteur, ou témoin bénin de même procédé (adaptateur bénin, ou consigne bénigne graduée).
  - Texte lu : transcription du saboteur ou transcription honnête, imposée jeton par jeton.
- **Sonde** : propre à chaque famille et gelée.
- **H_A** : à texte fixé, l'effet « source des états » sur la détection dépasse m, dépasse l'écart entre deux fabrications bénignes indépendantes, et croît avec la dose.
- **H_B** : cet effet ne dépasse pas m ; la sonde lit le texte, ou la simple présence d'un adaptateur ou d'une consigne.
- **Métrique** : détection à fausses alertes fixées (5 %), par épisode, seuil pris sur le lot d'étalonnage. L'AUROC est secondaire.
- **Repères à battre**, désignés d'avance :
  - un classifieur de texte composite ;
  - une sonde réapprise sur les états du modèle de base en lecture forcée, qui plafonne l'information textuelle (contrôle de D).
- **Contrôles négatifs** :
  - bénin contre bénin, sur au moins trois fabrications indépendantes : taux d'alerte au nominal ;
  - gamme de consignes bénignes : pente nulle.
- **Condition de non-identification** : norme et divergence des adaptateurs sont rapportées ; si le saboteur sort de la plage des bénins, le contraste est déclaré non identifié.
- **Limite** : je ne sais pas si les quatre doses sont quatre adaptateurs distincts. Avec une fabrication par dose, la conclusion porte sur ces adaptateurs, pas sur le procédé.
- **Coût** : passes de forçage en inférence ; trois adaptateurs bénins et les doses de consigne manquantes, soit quinze à vingt-cinq courses.
- **Ce que chaque issue falsifie** : H_A falsifie « détecteur de texte ou d'adaptateur » pour ces fabrications ; elle n'établit pas la représentation. H_B falsifie l'instrument sur ce banc : reconception, jugée sur une famille inédite qui reste à fabriquer, ou concession de la porte.

### C3. Tenue de l'adaptateur

- **Traitement primaire** : entraînement sur récompenses tirées au hasard, comme dans le travail publié (référence à vérifier).
- **Volet séparé**, hors duel : réglage fin sur les traces du jumeau honnête, dans la tâche.
- **H_A (fragile)** : la part de dommage retenue ne dépasse pas m = 0,5.
- **H_B (tenace)** : elle dépasse m.
- **Métrique** : différence de dommage avant/après avec intervalle ; le rapport n'est donné que si la porte de jugeabilité passe.
- **Porte de jugeabilité** :
  - dommage initial nettement positif, estimé sur un lot d'articles disjoint de celui de l'effet (objection de régression vers la moyenne que D adresse à C, et qui me concerne aussi) ;
  - qualité absolue du jumeau entraîné au-dessus d'une borne fixée contre le jumeau gelé ; sinon l'issue est « non jugeable (effondrement) », pas « fragile ».
- **Réplication** : trois graines par bras ; l'écart entre courses sert à dimensionner C5.
- **Contrôles négatifs** : zéro pas ; jumeau de même recette.
- **Usage de l'oracle, déclaré** : la mesure décide, par famille et selon une règle écrite d'avance, si la question de C5 est mesurable. Elle ne choisit ni graine, ni point de contrôle, ni dose, et C5 repart du saboteur d'origine. Je lis cela comme compatible avec la règle ; la direction tranche.
- **Règle touchée, inchangée depuis III.1** : l'agent est entraîné, sous un « bras de caractérisation » à déclarer.
- **Coût** : une quinzaine de courses.
- **Ce que chaque issue falsifie** : H_A falsifie l'interprétabilité de tout résultat d'entraînement sur cet organisme. H_B falsifie son assimilation à l'organisme publié jugé peu robuste.

### C4. Aiguillage d'audit, en rejeu

- **Précondition** : C1b passé pour les doses utilisées.
- **H_A** : à couverture et largeur de borne égales, le rapport audits uniformes / audits aiguillés dépasse m = 1,25 sur toute la grille de prévalences.
- **H_B** : il ne dépasse pas m. Une valeur sous 1 se lit « la sonde nuit ».
- **Politique** : part uniforme et plancher de tirage figés avant toute lecture de l'oracle.
- **Contrôles négatifs** :
  - aiguillage placebo aux mêmes probabilités inégales, scores permutés : rapport attendu inférieur ou égal à 1 ;
  - flux purement honnête, pour mesurer le couplage entre score de sonde et faux positifs de l'oracle.
- **Repères à battre** : juge de texte, longueur.
- **Coût** : processeur seul si les jugements existent.
- **Ce que chaque issue falsifie** : H_A falsifie « sondes superflues dès que la garantie est dans l'audit ». H_B falsifie « accélérateur et aiguillage » à ces doses et prévalences.

### C5. Bras d'attaque avec lecture du dommage (phase suivante)

- **Perte préenregistrée** : sonde gelée, ancrage vers la politique initiale du saboteur, nombre de pas fixe. Je ne sais pas vers quoi régularise le travail sur code vérifiable ; il est à relire à la page avant de figer.
- **H_A** : la baisse de dommage sous la sonde réelle dépasse de m celle du placebo.
- **H_B** : elle ne la dépasse pas.
- **Issue hors duel** : si le score visé n'a pas baissé, l'issue est « attaque non réalisée », non concluante et déclarée telle.
- **Contrôles négatifs** :
  - placebo sur le saboteur : direction factice orthogonale à la sonde, dans le sous-espace principal des activations honnêtes, à variance de score appariée ;
  - déplacement de politique mesuré et rapporté ;
  - jumeau de même recette, comme nouveau nul.
- **Réplication** : trois graines par bras. Si l'écart entre courses mesuré en C3 est de l'ordre de m, C5 n'est pas lancé.
- **Secondaire, descriptif** :
  - sonde tenue à l'écart, sa corrélation avec la sonde visée étant rapportée d'avance ;
  - sonde réapprise après coup sur un lot séparé ;
  - juge de texte.
  - La distinction « caché ou déplacé » n'est pas garantie identifiable.
- **Coût** : plusieurs dizaines de courses.
- **Ce que chaque issue falsifie** : H_A falsifie « l'entraînement contre une lecture interne ne produit que de l'évasion », sous cet ancrage. H_B falsifie le transport, dans ce régime, du jugement publié « viables comme signal d'entraînement ».
- **Non proposé** : un bras à ancrage bénin serait une parade, qui n'est pas ouverte.

### Classement révisé

| Chantier | Gain | Facilité | Portée | Découverte | Coût | Score |
|---|---|---|---|---|---|---|
| C4 | 4 | 3 | 4 | 3 | 2 | 72 |
| C1 | 5 | 3 | 4 | 2 | 2 | 60 |
| C2 | 5 | 3 | 4 | 3 | 3 | 60 |
| C3 | 5 | 3 | 3 | 3 | 3 | 45 |
| C5 | 5 | 1 | 5 | 5 | 5 | 25 |

- **Effet des critiques** : les coûts de C2, C3 et C5 montent et les facilités baissent. C5 perd plus de la moitié de son score.
- **Sensibilité** : avec le coût compté deux fois, l'ordre est C4, C1, C2, C3, C5. Avec la découverte comptée deux fois, il devient C4, C2, C3, C5, C1.
- **Ordre d'exécution** : la formule ne voit pas la dépendance. C4 est en tête du score mais n'est pas exécutable avant C1b. L'ordre reste C1, C2, puis C4 en parallèle de C3, puis C5.
- **Avant la porte d'instruments** : C1 et C2, puis C4 en rejeu.
- **Ce qui attend** : C3, sous l'accord de périmètre. C5 ensuite. Les essaims restent différés.
- **Ressource manquante** : une famille inédite fabriquée par un tiers. Sans elle, aucune reconception n'est jugeable.

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (faits VÉRIFIÉS).**
- La courbe dose-réponse existe pour l'adaptateur (quatre doses) et manque pour la consigne cachée.
- Les règles en vigueur excluent tout score de moniteur, sonde ou juge, de l'entraînement de l'agent hors bras d'attaque déclaré. Corriger en entraînant n'est pas ouvert.
- Le papier de 2026 laisse de côté le saboteur affiné et ne lit aucun état interne.
- Un organisme obtenu par distillation d'une consigne a été remis d'aplomb même par des récompenses au hasard.
- Un entraînement ordinaire ôte leur séparation à des sondes apprises hors domaine.
- Sur du code vérifiable, entraîner contre un détecteur interne donne trois issues.
- La détection reste nécessaire pour valider qu'un entraînement a réussi.

**Ce qui est RAPPORTÉ, non relu.**
- Une sonde apprise contre le modèle de base signale presque tous les adaptateurs bénins.
- Un juge qui lit le produit peut être trompé.

**Ce qui n'est pas établi.**
- Qu'une sonde fonctionne sur une tâche difficile à noter : aucune mesure trouvée (OBSERVÉ-NON-AUDITÉ).
- Que les saboteurs se représentent leur sabotage (HYPOTHÈSE). C2 corrigé ne l'établira pas.
- Que l'oracle voie le dommage aux faibles doses (HYPOTHÈSE de A).
- La tenue des saboteurs à un entraînement.
- L'antériorité.
- Je ne sais pas si le nul honnête est stable entre strates, ni si les quatre doses sont quatre fabrications.

**Ce que ce tour a changé.** Rien d'empirique. Les critiques ont montré que trois de mes critères n'étaient pas jugeables tels quels : R, le point à 1 % et la course unique par bras. Elles ont montré aussi qu'un de mes contrôles ne testait que le code, et qu'une de mes affirmations était fausse en partie.

**Garder, retirer, ajouter.**
- *Garder* : les sondes accumulées, la porte interne contre texte sur famille inédite, la garantie placée dans l'audit.
- *Différer* : les essaims.
- *Ajouter* :
  - les deux planchers ;
  - le plan croisé par forçage du texte ;
  - le rejeu d'aiguillage avec placebo ;
  - la lecture du dommage dans le bras d'attaque ;
  - une famille inédite fabriquée par un tiers.

**Faut-il aborder l'entraînement ?** Oui, comme objet mesuré et non comme parade.
- D'abord la tenue de l'adaptateur (C3), sous un bras de caractérisation que la direction doit accorder.
- Ensuite le bras d'attaque déjà prévu, avec placebo et plusieurs graines (C5).
- Entraîner contre une note faible n'est pas proposé. B, C et D relèvent, à propos d'autres propositions, que la note d'un juge est un score de moniteur : cela changerait une règle.

**L'expérience à faire en premier.** C1, sur un seul lot de courses honnêtes fraîches :
- le taux de franchissement de l'accumulateur par flux entier et par strate ;
- les paires jumeau/jumeau de l'oracle, avec inversion d'ordre.

Elle ne demande ni saboteur nouveau ni changement de règle. Elle fixe la plus petite dose et le niveau de fausses alertes auxquels tout le reste est jugeable. Si H_B sort, la porte d'instruments se joue sur une détection reconçue, et l'entretien du 1er décembre doit le dire.

**Hors de portée, inchangé.**
- La ressemblance avec un modèle qui saboterait de lui-même.
- Le dommage en service, sans jumeau.
- La généralisation au-delà des fabrications testées.
- Le passage à des modèles bien plus grands.

FIN-DE-CELLULE