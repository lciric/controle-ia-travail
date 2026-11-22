# Garantir la production et la reconnaissance d'objets rares : note de sortie du collisionneur

- **Date** : 2026-11-22, 18:46 UTC.
- **Dossier** : `runs/collisionneur-protocole-x-puits-etroits-abonnement-v1-20261122-142638`.
- **Accord** : GO-2026-11-22-67.
- **Dépense** : 9,03 dollars par l'interface, sur une ligne de 70 (`etat.md` du dossier). Les cellules Claude (Fable 5.2 et Opus 5.5) passent par l'abonnement et ne sont pas facturées.
- **Tours** : dix-huit cellules sur dix-huit, toutes complètes : six conceptions (tour III.1), six critiques croisées (III.2), six réponses (III.3).

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier. Le lecteur est du même modèle qu'une des cellules (lettre B) ; elle est traitée comme les autres.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure. Tout ce qui suit est démonstration, calcul sous hypothèses ou protocole proposé. Les modèles marquent « vérifié » leurs propres calculs. Aucun de ces calculs n'a été refait par un lecteur extérieur au collisionneur. Les seuils, effectifs et coûts sont qualifiés d'illustratifs par leurs auteurs. Aucune référence bibliographique n'a été contrôlée.

## 1. La question

Un générateur aléatoire, dont on ne peut qu'obtenir des tirages, produit des objets écrits dans une grammaire publique. Un vérificateur indépendant et coûteux dit si un objet a la propriété recherchée. La fréquence p des objets qui l'ont est inconnue, faible ou non. La question pose cinq points :

1. ce que « garantir » peut signifier mathématiquement, avec quantificateurs et hypothèses ;
2. les résultats établis et le prix de chaque méthode qui donne une garantie ;
3. comment la réponse dépend de ce qu'on sait du générateur, de la taille de la grammaire, de la corrélation entre tirages et du rapport entre coût de vérification et coût de production ;
4. quelle garantie apporte chaque méthode répandue ;
5. quelle observation, expérience ou preuve trancherait.

Notations des cellules, reprises ici : N tirages, coût c_g d'un tirage, coût c_v d'une vérification, ρ = c_v/c_g, δ le risque d'échec admis.

## 2. En bref

- **Le socle mathématique fait l'unanimité.** Sans plancher connu sur p, aucune garantie de succès ne tient à budget fini. La seule garantie sans hypothèse sur p est disjonctive : ou un positif est reconnu, ou p est certifié inférieur à 1 − δ^(1/N). Les six modèles l'écrivent indépendamment au tour III.1.
- **Le maillon faible est l'indépendance des tirages.** Si les tirages partagent un état caché, la probabilité de découverte plafonne, même à budget infini. Cinq modèles sur six placent en premier une même expérience. Elle compare, sur l'interface réelle, la part de campagnes sans aucun positif en session continue et en sessions réinitialisées, à un horizon de l'ordre de 1/p.
- **Le vérificateur se mesure à part.** Si son taux de fausses acceptations n'est pas très inférieur à p, la plupart des objets « reconnus » sont faux. Ce taux se mesure sur des négatifs, pas par la précision des acceptés.
- **Un filtre ou un juge appris ne garantit rien.** Il a un seuil de rentabilité calculable, mais aucun rappel garanti sur les objets rares.
- **Deux corrections faites en critique ont été adoptées par tous.** La première est une règle de décision à seuil unique, avec une issue « non jugeable » (Astra). La seconde montre que la garantie disjonctive vaut à tout instant d'arrêt, sans surcoût (Astra, démontrée ensuite par Neon).

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (lettre A)

- **Proposition centrale** (A, III.1). Quatre énoncés à faire relire avant toute expérience :
  - P0-1 : sans plancher sur p, aucune garantie uniforme n'existe ;
  - P0-2 : garantie dichotomique, « ou un positif est reconnu, ou p ≤ ε au niveau 1 − δ » ;
  - P0-3 : si les tirages dépendent d'un état latent, la formule des tirages indépendants appliquée à la fréquence moyenne est toujours optimiste ;
  - P0-4 : trier ne crée aucun positif. Un crible n'est rentable qu'au-dessus d'un rappel seuil r* = (1 + κ + s·ρ)/(1 + ρ), avec κ le coût relatif du crible et s son taux de passage.

  Fable relève aussi douze présupposés de la question. Exemples : « la » fréquence p existe ; le vérificateur est un oracle exact ; la grammaire publique permettrait d'énumérer sans passer par le générateur ; l'image de « puits étroits » suppose une géométrie, aiguille isolée ou entonnoir.
- **Plan** (A, III.1). Cinq duels :
  - D1 : la borne (1 − p)^N tient-elle sur le générateur tel qu'il est servi ?
  - D2 : le goulot est-il la production ou la reconnaissance ?
  - D3 : le vote d'accord enrichit-il ou appauvrit-il en régime rare ?
  - D4 : un plancher sur p se transfère-t-il d'une famille de propriétés à une cible nouvelle ?
  - D5 : aiguille ou entonnoir ?

  Trois bancs : synthétique, programmes et preuves sous Lean 4. Coût avancé : 100 à 250 euros de calcul (illustratif). Fable est le seul modèle à ne s'attribuer aucun statut « vérifié ».
- **Après les critiques** (A, III.3). Sur 30 points, Fable en accepte 21, en partage 6, en transforme 2 en test, et n'en retrouve pas 1 (une condition de collision d'Argon). Il supprime l'échantillon de référence de D1, critiqué par quatre modèles. D1′ compare deux régimes sur la même interface, contexte neuf à chaque tirage contre même session, avec une référence obtenue en permutant les verdicts entre campagnes. Le critère de D2 intègre la part du coût de vérification que le crible laisse passer, et P0-4 est étendu aux doublons. Fable propose quatre sens de « garantir », de G1 à G4. G4 est une garantie par campagnes entières échangeables, sans hypothèse sur l'intérieur d'une campagne. Il reprend d'Astra que la disjonction vaut à tout instant. Ordre proposé : relecture de P0, puis D1′.

### Claude Opus 5.5 (lettre B)

- **Proposition centrale** (B, III.1). Huit résultats « tranchés par preuve », de R1 à R8. Trois se distinguent du socle commun :
  - R4, population d'instances. Si la densité des probabilités de succès se comporte comme c·p^(b−1) près de zéro, le budget pour approcher la part insoluble à ε près croît comme ε^(−1/b), et non comme ln(1/ε).
  - R5. La précision des objets acceptés n'atteint ½ que si α ≤ p(1 − β)/(1 − p), avec α le taux de fausses acceptations et β celui de faux rejets.
  - R8. Le décodage contraint par masquage, jeton par jeton, n'échantillonne pas la loi du modèle conditionnée à la grammaire.

  Opus note aussi que la grammaire publique fournit toujours un échantillonneur uniforme de référence. Avec un modèle ouvert, « tirages seuls » est donc un choix de cadrage, pas une contrainte.
- **Plan** (B, III.1). Six duels :
  - D1 : indépendance des tirages ;
  - D2 : part d'instances non résolues, en décroissance exponentielle ou en loi de puissance ;
  - D3 : un filtre bon marché reste-t-il bon sur les puits rares ?
  - D4 : décodage contraint contre rejet ;
  - D5 : l'affinage par renforcement élargit-il ou rétrécit-il le support ?
  - D6 : le vérificateur se laisse-t-il exploiter sous pression de sélection ?

  Bancs : programmes (HumanEval, MBPP, avec EvalPlus comme vérificateur plus fort) et preuves (miniF2F sous Lean 4). Coût avancé : quelques centaines à environ 1 000 dollars.
- **Après les critiques** (B, III.3).
  - Opus reconnaît une erreur dans D6 : il mesurait le taux de fausses découvertes et non α. Désormais, α est estimé sur les candidats que le vérificateur fort rejette.
  - Il sépare la propriété vraie de la fréquence observable des acceptations.
  - Il adopte la règle d'Astra, avec deux lots indépendants : l'un pour sélectionner ou ajuster, l'autre pour décider.
  - D2′ change d'estimande : la part des instances dont le premier succès tombe entre n/2 et n tirages. Les instances insolubles n'y contribuent pas.
  - D5′ suit un plan en deux temps, jugé par un test des signes.
  - Il rejette deux critiques. D4 n'est pas hors cadre : il relève d'un régime déclaré, « accès aux probabilités internes ». Le contrôle par dilution est vrai par construction pour un filtre qui juge chaque objet isolément.
  - Il recalcule un chiffre d'Argon (22 succès requis au lieu de 21), sans changer la conclusion.
  - Première expérience : D1′, environ 3·10⁵ tirages vérifiés à p = 0,01 (illustratif). À p faible, l'indépendance reste une extrapolation.

### Argon (identifiant gemini-4-argon, lettre C)

- **Proposition centrale** (C, III.1). Cinq énoncés formels de garantie : uniforme (impossible), sous plancher, avec filtre, disjonctive, et déterministe par énumération de la grammaire sur un horizon borné. Méthodes à garantie : rejet grammatical exact, regroupement des objets syntaxiquement équivalents, arrêt au premier succès, bandits sur sous-grammaires. Une « loi de bascule » dit quand énumérer la grammaire publique bat le générateur.
- **Plan** (C, III.1). Quatre duels :
  - redondance du générateur ;
  - filtre appris à grand ρ ;
  - indépendance des tirages, par un indice de dispersion ;
  - générateur contre énumération.

  Coût avancé : 5 à 15 dollars.
- **Défauts relevés** (A, B, D, E, F, III.2).
  - Le signe des covariances deux à deux ne fixe pas la probabilité de découverte. Fable donne un contre-exemple chiffré à trois tirages.
  - Une inégalité est inversée en 1.B (Opus, Astra).
  - « Domine strictement » oublie le coût du filtre (Opus).
  - La garantie par bandits est vide avant le premier succès.
  - Des attributions sont marquées « vérifié » sans contrôle : Feller (1968) pour des « axiomes de coût », Knuth (1975) pour une décroissance de p avec la profondeur.
- **Après les critiques** (C, III.3).
  - Argon accepte presque tout : il retire les bandits, corrige 1.B, passe de la covariance à l'association et requalifie les attributions contestées.
  - Il rejette deux points. Évaluer un filtre après déduplication est l'architecture réelle. Énumérer la grammaire est une base de comparaison recevable, contre l'objection de Carbon.
  - Duels corrigés :
    - Duel 1 : gain net de la déduplication, et audit des objets fusionnés pour vérifier que la fusion ne réunit jamais des verdicts opposés ;
    - Duel 2 : estimateur à probabilités d'inclusion connues (Horvitz et Thompson) ;
    - Duel 3 : sessions réinitialisées contre chaîne continue, avec un contrôle de dérive par permutation à rang fixe ;
    - Duel 4 : énumération aléatoire sans remise, appariée en longueur.
  - Première expérience : le Duel 3, couplé à l'audit des objets fusionnés.
  - Sa synthèse finale garde des références en appui de résultats marqués « vérifié » (Feller ; Valiant, 1984).

### Astra (identifiant gpt-6.2-astra, lettre D)

- **Proposition centrale** (D, III.1). La plus courte, centrée sur les quantificateurs. « Pour chaque générateur, il existe un budget » est vrai ; « il existe un budget valable pour tout générateur » est faux. Le contre-exemple le plus simple de dépendance : répéter le premier tirage conserve la fréquence p à chaque appel, mais la probabilité de produire un positif reste p. Condition suffisante : si, après tout historique d'échecs, la chance de succès au tirage suivant reste au moins q, l'échec est borné par (1 − q)^n.
- **Plan** (D, III.1). Trois duels sur bancs finis calculables exactement. Les deux premiers portent sur des énoncés qu'Astra a déjà démontrés. Le troisième compare un score à un contrôle mécanique sur banc gelé, avec un seuil de différence nulle. Ancrage sur processeur seul : expressions arithmétiques bornées.
- **Défauts relevés** (tous, III.2). Les duels 1 et 2 sont des théorèmes, pas des expériences. Avec un seuil zéro sur banc gelé, un score de pur hasard franchit le seuil avec une probabilité proche de ½ (Argon, Carbon, Neon). Le « meilleur » comparateur est choisi sur le banc de test.
- **Apports en critique** (D, III.2). Trois apports ont été repris par d'autres :
  - une règle de décision : paramètre et seuil fixés d'avance, intervalle à cheval sur le seuil déclaré « non jugeable » ;
  - la validité à tout instant, sans surcoût, de la garantie disjonctive à zéro succès ;
  - avec Argon, le constat qu'avant le premier succès, une politique qui ne reçoit que des verdicts binaires suit un calendrier fixé d'avance.

  Astra donne aussi deux lois de mêmes covariances qui n'ont pas la même probabilité de ne rien trouver (contre-exemple de parité).
- **Après les critiques** (D, III.3). Astra retire ses duels 1 et 2, désormais présentés comme preuves. Le signe sur banc gelé devient un intervalle apparié, jugé contre une marge d'utilité que l'arbitre fixe d'avance. Il donne la formule exacte de la probabilité de succès sous quota de vérifications. Première expérience : mesurer directement, sur des sessions indépendantes au plafond réel, la probabilité que l'ordre brut avec cache exact rende un témoin confirmé. Il demande aussi d'auditer les objets produits mais non reconnus, en distinguant quatre causes d'échec.

### Carbon (identifiant gemini-4-carbon, lettre E)

- **Proposition centrale** (E, III.1). Quatre énoncés de garantie, dont un de fidélité à la loi conditionnelle, et trois résultats négatifs, dont la contamination par les fausses alertes quand p ≪ α. Méthodes à garantie :
  - rejet mémoïsé ;
  - certificat après échecs ;
  - énumération directe ;
  - test par groupes de Dorfman ;
  - « triage défensif » : une part γ des vérifications est tirée uniformément, ce qui garantit un plancher quelle que soit la qualité du score.

  Carbon dresse aussi un tableau des méthodes répandues : la calibration conforme est inapplicable tant qu'aucun positif n'est connu, et le vote majoritaire échoue si un mode faux pèse plus que p.
- **Plan** (E, III.1). Quatre duels :
  - générateur contre tirage uniforme dans la grammaire ;
  - tri pur contre triage défensif ;
  - indépendance par un indice de dispersion ;
  - exactitude du vérificateur.

  Coût avancé : environ 55 dollars (50 à 110).
- **Défauts relevés** (III.2).
  - Le test de Fisher teste le mauvais nul.
  - Une clause du duel 2 permet de réfuter les deux hypothèses à la fois.
  - L'indice de dispersion sur une seule séquence est aveugle à un état latent tiré une fois.
  - La valeur prédictive positive dépend de la prévalence.
  - Le score et le générateur sont de la même famille de modèles.
  - 460 acceptations auditées sont hors d'atteinte à p faible.
- **Après les critiques** (E, III.3).
  - Carbon accepte presque tout. Il corrige deux formules : l'appel qui confirme le succès manquait au décompte, et le plancher du triage défensif vaut γ·M/N par candidat produit, non γ.
  - Il écarte Dorfman en pratique, sauf si vérifier un lot coûte nettement moins que vérifier ses éléments.
  - Priorité 1, E3* : sessions continues contre sessions réinitialisées, horizon d'environ 2/p, seuil 0,03 (illustratif).
  - E1* : rapport des taux de découverte par unité de budget, contre une référence uniforme appariée en longueur.
  - E2* : budget égal, coût du score compris, score d'une autre famille de modèles.
  - E4* : audit aveugle de tous les objets acceptés pendant la campagne.
  - Résultat ajouté : certifier α ≤ η·p sur des négatifs coûte de l'ordre de ln(1/δ)/(η·p) appels à un oracle exact, plus que de découvrir un positif.

### Neon (identifiant gemini-4-neon, lettre F)

- **Proposition centrale** (F, III.1). Cinq énoncés, dont une garantie valide à tout instant d'arrêt et une garantie bayésienne. Neon construit le contre-exemple que tous reprendront : un état caché vaut 1 avec probabilité η et 0 sinon. La fréquence moyenne est bien p, mais la probabilité de découverte reste au plus η, même à budget infini.

  Son tableau est le plus large en résultats rapportés : échantillonnage préférentiel, association négative, masse manquante de Good et Turing, méthodes de Monte-Carlo par chaînes ou par particules, découpage multiniveau. Ces dernières méthodes n'ont, selon Neon, aucune garantie sous un verdict purement binaire.
- **Plan** (F, III.1). Quatre expériences :
  - E1 : corrélation, par sur-dispersion ;
  - E2 : mode répété ou attracteurs faux ;
  - E3 : filtre appris hors distribution ;
  - E4 : recherche adaptative sous verdict binaire.

  Coût avancé : 15 à 35 dollars sur banc synthétique, 40 à 120 dollars sur banc réaliste, environ cent fois plus pour p ≈ 10⁻⁵ (illustratif).
- **Défauts relevés** (III.2).
  - E1 ne détecte pas son propre contre-exemple : l'indice vaut environ 1,012 selon Fable et 1,049 selon Argon, sous le seuil 1,10.
  - E1 s'arrête de façon optionnelle.
  - Le gain de déduplication de E2 ne dépend pas des positifs.
  - Le critère « rappel nul par tâche » de E3 est vrai par construction avec un seul positif.
  - E4 bute sur le calendrier fixé d'avance.
  - La masse manquante de Good et Turing donne un certificat dominé par la borne de Clopper et Pearson.
- **Après les critiques** (F, III.3).
  - Neon démontre, par une martingale positive, la correction d'Astra : la disjonction à zéro succès vaut à tout instant sans surcoût. Le prix en logarithme itéré ne porte que sur l'estimation après un succès. Il corrige son tableau en ce sens.
  - Il élève le calendrier fixé d'avance au rang de résultat établi.
  - Il rejette une critique de Fable. Pour une interface distante, des graines indépendantes ne garantissent pas l'indépendance par construction : il en fait un test.
  - E1′ a deux volets, état caché entre sessions et dérive dans une chaîne. Horizon 2/p, seuil 0,05. Puissance calculée sur son contre-exemple : écart d'environ 0,374 pour η = 0,5 et 0,130 pour η = 0,8 (illustratif).
  - E4′ passe dans un régime d'accès étendu, avec un signal gradué.
  - Ordre proposé : audit minimal du vérificateur, puis E1′.

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **Impossibilité uniforme.** Les six l'écrivent : à budget fini, la probabilité de produire un positif est au plus (nombre de tirages) × p, qui tend vers zéro avec p (A P0-1, B R2, C 1.A, D, E N1, F tableau 2).
- **Garantie disjonctive.** Les six l'écrivent : ou un positif est reconnu, ou p ≤ 1 − δ^(1/N), d'après Clopper et Pearson (A P0-2, B R3, C 1.D, D, E énoncé 2, F énoncé 2).
- **Dépendance.** La fréquence moyenne ne suffit pas ; un état caché fait plafonner la découverte (A P0-3, B R4, D répétition du premier tirage, E mélange latent, F contre-exemple en η). Argon est le seul à raisonner par le signe des covariances, raisonnement réfuté ensuite.
- **Seuil de rentabilité d'un filtre.** Même forme algébrique chez Fable, Opus, Argon, Carbon et Neon ; Astra le traite par la probabilité qu'un positif soit parmi les objets vérifiés.
- **Fausses acceptations.** Si α n'est pas très inférieur à p, les objets reconnus sont surtout faux (A, B R5, E N3, F).
- **Grammaire publique.** Elle offre une référence (énumération ou tirage uniforme) à laquelle comparer le générateur (A, B, C, D, E, F), avec un désaccord sur sa légitimité (plus bas).
- **Vote majoritaire.** Aucune garantie en régime rare (A, E, F). Pour Opus, avec un vérificateur exact, il ne fait qu'économiser des appels (B).
- **Contrôle par hachage.** Une propriété définie par une fonction de hachage, sans structure, sert de témoin négatif (B, E, F au III.1 ; repris ensuite par A, C).

### Convergence née des critiques

- **Règle de décision.** Proposée par Astra (D, III.2), reprise nommément par Fable, Opus, Argon, Carbon et Neon au III.3 : un paramètre, un seuil fixé d'avance, deux hypothèses complémentaires, et « non jugeable » quand l'intervalle chevauche le seuil ou qu'un dénominateur est nul.
- **Abandon des indices de dispersion.** Quatre plans testaient l'indépendance par un indice calculé sur une séquence (B, C, E, F). Tous l'abandonnent : un état tiré une fois par session reste invisible, et l'indice n'est sensible qu'à un horizon de l'ordre de 1/p. Ils le remplacent par la comparaison directe de la part de campagnes vides, sessions continues contre sessions réinitialisées.
- **Validité à tout instant.** Remarque d'Astra (D, III.2), démontrée par Neon (F, III.3), adoptée par Fable, Opus et Argon.
- **Coûts conditionnels.** Un filtre qui écarte les rejets rapides concentre la vérification sur des quasi-solutions lentes (E, F, III.2). Fable, Opus, Argon et Neon intègrent le coût moyen de vérification des objets retenus dans leur critère.
- **Mesurer α sur des négatifs.** L'erreur d'Opus (D6) est relevée par les cinq autres ; Opus, Carbon et Fable mesurent désormais α sur des négatifs naturels du générateur, jugés par un oracle indépendant.
- **Avant le premier succès, un verdict binaire n'apprend rien.** Constat d'Argon et d'Astra (III.2), promu en résultat par Neon, qui justifie le retrait des bandits par Argon.

| Modèle | Première expérience proposée au tour III.3 | Seuil (illustratif) | Horizon |
|---|---|---|---|
| Fable (A) | Relecture des quatre énoncés, puis sessions à contexte neuf contre même session | rapport ≤ 1,5 | N = 3/p |
| Opus (B) | Indépendance par campagnes espacées | rapport ≤ 1,25 | N = 3/p |
| Argon (C) | Sessions réinitialisées contre chaîne continue, avec audit des fusions | différence 0 | N·p entre 1 et 3 |
| Astra (D) | Probabilité, par session indépendante, que l'ordre brut rende un témoin confirmé au plafond réel | z ≤ δ | plafond réel |
| Carbon (E) | Sessions continues contre réinitialisées | différence 0,03 | 2/p |
| Neon (F) | Audit minimal du vérificateur, puis état caché et dérive | différence 0,05 | 2/p |

### Désaccords

- **Énumérer la grammaire est-il légitime ?** Argon (C, III.3) maintient que n'appeler jamais le générateur et énumérer la grammaire est une base recevable, contre Carbon (E, III.2). Fable et Neon jugent que l'énumération sort du cadre « tirages seuls » ou n'est valable « si autorisée ». Astra note qu'elle peut trouver un témoin que la source n'a pas produit. Les critiques n'ont pas tranché ; c'est une question de cadrage pour l'arbitre.
- **Quel régime d'accès ?** Opus garde le décodage contraint en le déclarant « accès aux probabilités internes » (B, III.3) ; Argon, Astra et Carbon le jugent hors cadre. Neon fait de même pour son signal gradué (E4′). Les deux positions tiennent si les régimes sont rapportés séparément.
- **Évaluer un filtre après déduplication.** Argon le défend comme l'architecture réelle ; Astra et Neon demandaient des grandeurs pondérées par les tirages. Argon accepte de repondérer.
- **Ce qu'il faut mesurer en premier.** Cinq modèles commencent par l'indépendance ; Neon fait précéder un audit du vérificateur ; Astra mesure directement l'échec par session, sans supposer l'indépendance à l'intérieur d'une session. Les trois choix sont compatibles, l'ordre diffère.
- **Seuils.** Rapports (Fable 1,5, Opus 1,25) contre différences (Argon 0, Carbon 0,03, Neon 0,05) ; horizons 3/p ou 2/p. Aucun modèle ne justifie le niveau de son seuil autrement que par un exemple.
- **Statut « vérifié ».** Fable ne se l'attribue jamais. Opus, Astra, Argon, Carbon et Neon l'attribuent à leurs propres déductions. Opus signale la divergence sans la trancher (B, III.2). Argon et Carbon l'avaient aussi donné à des citations ou à l'intégrité des pièces, et le retirent en partie au III.3.
- **Les chiffres 0,55 et 0,40 de l'en-tête de la question.** Traités comme rapportés par Fable et Carbon, comme observés non audités par Argon (III.2) et Neon (III.1 et III.3). Opus le note comme divergence ; tous s'accordent qu'ils manquent d'échelle, d'effectif et de plan.
- **Rejets motivés au III.3.**
  - Fable maintient que, pour « un positif reconnu », le rappel pondéré par les tirages est la bonne cible (contre Argon). Il refuse de tenir pour apparié un plan que rien ne décrit (contre Neon).
  - Opus juge le contrôle par dilution vrai par construction pour un filtre qui juge objet par objet.
  - Astra maintient que sa formule de coût moyen était correcte dans le cas qu'elle visait.
  - Carbon conteste que l'énoncé de Dorfman soit faux, tout en l'écartant en pratique.
- **Dates.** Wang et al., « Self-Consistency… » : 2022 chez Fable, 2023 chez Opus. miniF2F : 2021 chez Fable, 2022 chez Opus. À vérifier.

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

Aucun modèle ne revendique de nouveauté. Le socle (borne de Clopper et Pearson, impossibilité uniforme, seuil d'un filtre, rôle d'un état caché) est présenté comme élémentaire ou rapporté. Fable note que la littérature traite des cadres voisins et que la transposition au cadre exact reste à écrire (A, III.1, présupposé 10). Pourraient être propres au dossier, sous réserve d'une recherche bibliographique que personne n'a faite :

- la mesure directe, sur l'interface réelle, de l'excès de campagnes vides entre session continue et sessions réinitialisées, comme audit préalable de toute garantie (A, B, C, E, F) ;
- l'estimande d'Opus pour une population d'instances : la part des premiers succès tardifs, qui élimine la part insoluble sans l'estimer (B, III.3) ;
- son plan en deux temps pour compter les instances perdues par l'affinage (B, III.3) ;
- le critère de rentabilité étendu aux doublons et le rapport de coûts d'équilibre (Fable, A, III.3) ;
- le triage défensif appliqué au budget de vérification, avec son plancher corrigé (Carbon, E, III.3) ;
- la distinction de quatre causes d'échec d'une session (rien produit, produit non vérifié à temps, vérifié mais rejeté, annoncé sans témoin) (Astra, D, III.3).

### Fragile

- **Les calculs « vérifiés » n'ont pas de vérificateur extérieur.** Les modèles se contrôlent entre eux, et les petites discordances (21 ou 22 chez Argon et Opus, une condition de collision non retrouvée par Fable) montrent que ce contrôle laisse passer des écarts.
- **Le régime rare est hors de portée des mesures.** Auditer l'indépendance coûte de l'ordre de K·3/p tirages vérifiés (Opus) ; à p faible, elle reste une hypothèse extrapolée. Fable et Neon bornent leurs conclusions à p ≥ 10⁻³ sur objets réels (illustratif).
- **En deçà de 1/n, « p minuscule » et « p nul » sont indiscernables** (B, C, D, E). Une garantie pour un p plus petit ne peut venir que d'une hypothèse sur le générateur, jamais d'une mesure (B, III.3).
- **Un état commun à toutes les campagnes reste invisible** à toutes les expériences proposées (A, B, III.3).
- **Certifier le vérificateur coûte plus que trouver.** Borner α sous une fraction de p demande plus d'appels à un oracle exact que la découverte elle-même (E, III.3) ; Carbon propose comme repli un audit des objets acceptés pendant la campagne.
- **Le vérificateur fort est supposé exact.** Si les tests étendus contiennent ceux du vérificateur, ses propres erreurs sont invisibles (A, F, III.2 ; B, III.3).
- **Coûts.** Les estimations vont de quelques dollars (Argon) à environ 1 000 dollars (Opus) pour des plans comparables ; elles sont toutes illustratives et ne comptent ni l'ingénierie ni l'audit humain.
- **Références en appui de résultats.** Argon garde Feller (1968) et Valiant (1984) en appui de résultats marqués « vérifié », alors que l'attribution de Feller à des « axiomes de coût » a été contestée (A, B, III.2).

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois des références, des auteurs ou des années. Opus marque lui-même Loula et al. (2025) « référence à vérifier ».

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Clopper, Pearson (1934), « The use of confidence or fiducial limits illustrated in the case of the binomial » | les six | Borne après zéro succès |
| Hanley, Lippman-Hand (1983), « If nothing goes wrong, is everything all right? Interpreting zero numerators » | Fable, Opus | Idem |
| Howard, Ramdas, McAuliffe, Sekhon (2021), « Time-uniform, nonparametric, nonasymptotic confidence sequences » | Fable, Opus | Arrêt dépendant des données |
| Ville (1939), « Étude critique de la notion de collectif » | Neon ; Carbon en critique | Validité à tout instant |
| Robbins (1970), « Statistical methods related to the law of the iterated logarithm » | Neon | Prix en logarithme itéré |
| Wald (1945), « Sequential Tests of Statistical Hypotheses » | Argon, Carbon, Neon | Test séquentiel |
| Dagum, Karp, Luby, Ross (2000), « An optimal algorithm for Monte Carlo estimation » | Opus, Argon, Carbon | Coût d'estimer p |
| de Finetti (1937), « La prévision : ses lois logiques, ses sources subjectives » | Fable | Tirages échangeables |
| Esary, Proschan, Walkup (1967), « Association of random variables, with applications » | Opus en critique ; Argon | Association positive |
| Joag-Dev, Proschan (1983), « Negative Association of Random Variables, with Applications » | Neon | Association négative |
| Hoeffding (1963), « Probability inequalities for sums of bounded random variables » | Argon, Carbon, Neon | Concentration |
| Le Cam (1973), « Convergence of estimates under dimensionality restrictions » | Neon ; Carbon en critique | Méthode à deux points |
| Yao (1977), « Probabilistic computations: Toward a unified measure of complexity » | Carbon, Neon | Borne inférieure par principe minimax |
| Wolpert, Macready (1997), « No free lunch theorems for optimization » | Fable, Opus, Carbon | Aucun ordre de recherche ne domine |
| Levin (1973), « Universal sequential search problems » | Fable | Énumération |
| Luby, Sinclair, Zuckerman (1993), « Optimal speedup of Las Vegas algorithms » | Fable | Redémarrages |
| Good (1953), « The population frequencies of species and the estimation of population parameters » | Fable, Opus, Neon | Objets inédits |
| McAllester, Ortiz (2003), « Concentration Inequalities for the Missing Mass and for Histogram Rule Error » | Neon | Masse manquante |
| Flajolet, Zimmermann, Van Cutsem (1994), « A calculus for the random generation of labelled combinatorial structures » | Opus, Carbon | Échantillonneur uniforme |
| Duchon, Flajolet, Louchard, Schaeffer (2004), « Boltzmann samplers for the random generation of combinatorial structures » | Opus | Idem |
| Jerrum, Valiant, Vazirani (1986), « Random generation of combinatorial structures from a uniform distribution » | Carbon | Idem |
| von Neumann (1951), « Various techniques used in connection with random digits » | Carbon | Rejet |
| Owen, Zhou (2000), « Safe and effective importance sampling » | Carbon | Triage défensif |
| Kahn, Marshall (1953), « Methods of Reducing Sample Size in Monte Carlo Computations » | Neon | Échantillonnage préférentiel |
| Chatterjee, Diaconis (2018), « The sample size required in importance sampling » | Neon | Idem, coût exponentiel |
| Horvitz, Thompson (1952), « A Generalization of Sampling Without Replacement from a Finite Universe » | Argon, Neon (III.3) | Audit à inclusion connue |
| Dorfman (1943), « The detection of defective members of large populations » | Carbon | Tests par groupes |
| Aho, Peterson (1972), « A minimum distance error-correcting parser for context-free languages » | Carbon | Correction syntaxique |
| Vovk, Gammerman, Shafer (2005), « Algorithmic Learning in a Random World » | Fable, Carbon, Neon | Prédiction conforme |
| Candès, Lei, Ren (2023), « Conformalized survival analysis » | Fable | Censure |
| Tibshirani, Barber, Candès, Ramdas (2019), « Conformal Prediction Under Covariate Shift » | Fable (III.3) | Décalage de covariable |
| Angelopoulos, Bates, Fannjiang, Jordan, Zrnic (2023), « Prediction-powered inference » | Neon | Estimation assistée |
| Cérou, Guyader (2007), « Adaptive multilevel splitting for rare event analysis » | Fable, Neon | Événements rares |
| Del Moral (2004), « Feynman-Kac Formulae… » ; Asmussen, Glynn (2007), « Stochastic Simulation… » | Neon | Méthodes à particules |
| Rubinstein, Kroese (2004), « The Cross-Entropy Method… » ; Hajek (1988), « Cooling schedules for optimal annealing » | Fable | Entropie croisée, recuit |
| Robbins (1952) ; Auer, Cesa-Bianchi, Fischer (2002) ; Lai, Robbins (1985) ; Berry et al. (1997) | Argon ; Neon | Bandits |
| Srinivas, Krause, Kakade, Seeger (2010), « Gaussian process optimization in the bandit setting… » | Fable | Optimisation bayésienne |
| Feller (1968) ; Valiant (1984) ; Shannon (1948) ; Knuth (1975) ; Brassard, Høyer, Mosca, Tapp (2002) | Argon | Appuis divers ; Feller et Knuth contestés |
| Chen et al. (2021), « Evaluating Large Language Models Trained on Code » | Fable, Opus | Estimateur sans biais, banc de code |
| Austin et al. (2021), « Program Synthesis with Large Language Models » | Opus | Banc de code |
| Liu, Xia, Wang, Zhang (2023), « Is your code generated by ChatGPT really correct?… » | Opus | Tests étendus |
| Zheng, Han, Polu (2021 ou 2022), « MiniF2F… » | Fable, Opus | Banc de preuves |
| Wang et al. (2022 ou 2023), « Self-Consistency Improves Chain of Thought Reasoning… » | Fable, Opus | Vote d'accord |
| Brown et al. (2024), « Large Language Monkeys: Scaling Inference Compute with Repeated Sampling » | Fable, Opus | Couverture croissante avec les tirages |
| Schaeffer et al. (2025), « How Do Large Language Monkeys Get Their Power (Laws)? » | Opus | Loi de puissance par la queue près de zéro |
| Stroebl, Kapoor, Narayanan (2024), « Inference Scaling fLaws… » | Opus | Limite par vérificateur imparfait |
| Yue et al. (2025), « Does Reinforcement Learning Really Incentivize Reasoning Capacity… » | Opus | Perte de couverture après affinage |
| Gao, Schulman, Hilton (2023), « Scaling laws for reward model overoptimization » | Opus | Exploitation d'un juge |
| Park et al. (2024), « Grammar-Aligned Decoding » | Opus | Distorsion du décodage contraint |
| Lew, Zhi-Xuan, Grand, Mansinghka (2023) ; Loula et al. (2025) | Opus | Monte-Carlo séquentiel |
| Kwon et al. (2023), vLLM ; Willard, Louf (2023), Outlines | Opus | Logiciels |
| Romera-Paredes et al. (2024), « Mathematical discoveries from program search with large language models » | Fable | Recherche évolutive guidée |
| McNemar (1947), « Note on the sampling error of the difference between correlated proportions or percentages » | Fable (III.3) | Plan apparié |

## 7. Propositions retenues et non retenues

Critères appliqués : soutien de plusieurs modèles, résistance aux critiques, coût, et ce que la proposition tranche pour la suite.

### Retenues

1. **Mesurer d'abord, sur l'interface réelle, si les tirages se comportent comme indépendants au regard de la propriété.** Il s'agit de comparer la part de campagnes sans aucun positif en session continue et en sessions réinitialisées, à un horizon de 2 à 3/p, avec un seuil unique. Le contrôle positif est un mélange à état caché planté au même p ; le contrôle négatif est un générateur local sans état.
   - *Soutien et résistance.* Cinq modèles la placent en premier au III.3 (A, B, C, E, F). L'expérience d'Astra porte sur le même objet, l'échec par session. C'est la version qui a survécu aux critiques de l'indice de dispersion.
   - *Ce qu'elle tranche.* Toutes les garanties établies supposent l'indépendance. Si elle tombe, seule une garantie par campagnes entières subsiste (Fable G4), et aucun budget ne lève le plafond (Neon).
   - *Points faibles.* Coût en 1/p ; extrapolation aux p plus faibles ; un état commun à toutes les campagnes reste invisible.

2. **N'énoncer que des garanties disjonctives ou conditionnelles à un plancher déclaré, valides à tout instant d'arrêt.** Concrètement : « ou un positif est reconnu, ou p ≤ 1 − δ^(1/N) », et un budget fondé sur un plancher p₀ seulement si p₀ est une hypothèse écrite.
   - *Soutien.* Établi indépendamment par les six ; la correction d'Astra, démontrée par Neon, est acceptée par Fable, Opus et Argon.
   - *Coût.* Nul ; c'est une règle d'écriture.
   - *Point faible.* Elle repose sur la retenue 1.

3. **Mesurer le vérificateur séparément.** α se mesure sur des négatifs naturels du générateur, jugés par un oracle indépendant, et se publie comme borne. Il faut y joindre un audit à l'aveugle de tous les objets acceptés pendant la campagne.
   - *Soutien.* Opus (D6′), Fable (I1′), Carbon (E4*), Neon (audit d'abord), Argon (audit des fusions) ; c'est la critique la plus partagée du dossier.
   - *Ce qu'elle tranche.* Si α n'est pas très inférieur à p, les reconnaissances sont surtout fausses (R5 d'Opus).
   - *Point faible.* Certifier α sous une fraction de p coûte plus que la découverte (Carbon) ; l'audit de campagne est le repli réaliste.

4. **Juger tout filtre, juge ou score par son seuil de rentabilité, à budget égal.** Le seuil doit inclure le coût du filtre et le coût moyen de vérification des objets qu'il retient. L'évaluation se fait sur des propriétés disjointes de celles qui ont servi à le régler, avec un audit des rejetés à probabilité d'inclusion connue. Le triage défensif reste la seule manière nommée de rendre un plancher quand le score se trompe.
   - *Soutien et résistance.* Fable D2′, Opus D3′, Argon Duel 2, Carbon E2*, Neon E3′ convergent après critique ; le biais « aucun positif parmi les rejetés audités, donc rappel parfait » a été démontré par cinq modèles.
   - *Point faible.* Le rappel n'est estimable qu'avec assez de positifs vérifiés, ce qui le rend souvent non jugeable dans le régime le plus étroit.

La règle de décision d'Astra (seuil unique, issue « non jugeable ») est à appliquer à toutes les retenues ; elle a été adoptée par les six.

### À reprendre ensuite

- **Générateur contre référence grammaticale appariée en longueur** (Argon Duel 4 corrigé, Carbon E1*). Elle répond à la partie « taille de la grammaire » du point 3. Elle attend que l'arbitre tranche si l'énumération est admise.
- **Population d'instances et affinage** (Opus D2′ et D5′). Plans propres et peu coûteux une fois les bassins vérifiés constitués ; ils supposent la retenue 1.
- **Signal gradué et décodage contraint** (Fable D5′, Neon E4′, Opus D4′). Ils relèvent d'un régime d'accès plus large que « tirages seuls » et doivent être rapportés à part.

### Non retenues

- **Les indices de dispersion sur une séquence** (Opus, Argon, Carbon, Neon au III.1) : aveugles à un état tiré une fois, insensibles sous 1/p ; abandonnés par leurs auteurs.
- **Les duels déjà démontrés** (Astra, duels 1 et 2) : ce sont des preuves ; retirés par Astra.
- **Le signe exact sur banc gelé** (Astra, duel 3) : un score de pur hasard franchit le seuil une fois sur deux environ ; remplacé par un intervalle apparié.
- **La mesure de l'exploitation du vérificateur par la précision des acceptés** (Opus, D6) : elle mesurait autre chose qu'α ; corrigée.
- **L'extrapolation de la part d'instances non résolues** (Opus, D2) : ajustement et test sur les mêmes comptes ; remplacée.
- **Les bandits sur sous-grammaires** (Argon) : aucune information avant le premier succès ; retirés.
- **Les tests par groupes** (Carbon) : inapplicables à un vérificateur dont le coût croît avec le lot ; écartés.
- **La masse manquante comme certificat sur p** (Neon) : dominée par la borne de Clopper et Pearson ; gardée seulement pour prévoir le coût des objets inédits.
- **La recherche adaptative sous verdict purement binaire** (Neon, E4) : tranchée par le résultat du calendrier fixé d'avance ; déplacée vers le régime à signal gradué.
