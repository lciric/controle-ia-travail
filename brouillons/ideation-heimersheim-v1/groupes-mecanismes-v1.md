# Groupes de mécanismes d'échec — piste Heimersheim, groupeur aveugle (v1)

Direction étudiée : le pilotage des activations contre la conscience d'évaluation (retirer du modèle la croyance « je suis évalué » pour voir ce qu'il ferait en déploiement). Question de groupement : pourquoi ce pilotage ne montrerait-il pas le comportement de déploiement ?

- Consigne : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/piste-heimersheim-groupeur-aveugle-v1.md`, empreinte sha256 (algorithme de hachage sécurisé, 256 bits) `1ce4fdd53005a7b78067eb1fe7bc74e772079d0ff77d2db205dc6ffbc518ba82`, vérifiée.
- Entrée : `/home/claude/scratch/ideation-rapport/piste-heimersheim/fiches-a-grouper-v1.json`, empreinte `6faa03d3885c7c411f4b02d87dd1d540cff862303967196ccd45b112897471ba`, vérifiée à 2026-11-03T12:24:01Z ; 62 fiches, 62 identifiants uniques, 62 affectées. Aucun autre fichier lu.
- Heures (toutes en temps universel coordonné, prises par `date -u`) : définitions écrites et gelées à **2026-11-03T12:30:21Z**, après une lecture des 62 fiches et avant toute affectation (la lecture a pu suggérer des rattachements ; aucune affectation n'a été écrite avant le gel). Passe d'affectation écrite à 2026-11-03T12:35:07Z.
- Empreinte des définitions au gel : `ad9cc5b346eac11e79f94053be279eb8887c17b260f1a6ff42825d79a42cb31e` (sha256 de la liste `groupes` du fichier compagnon `groupes-mecanismes-v1.json`, sérialisée par `json.dumps(groupes, ensure_ascii=False, sort_keys=True, separators=(',', ':'))`, encodage UTF-8). Recalculée et identique au moment d'écrire les fichiers : les définitions n'ont pas changé.

## 1. Groupes (définitions gelées à 2026-11-03T12:30:21Z)

### 1. Cible confondue

- Définition : La direction extraite porte surtout une autre variable que la croyance « je suis évalué » : registre ou style, forme du gabarit, assertion d'un interlocuteur sur le contexte, confiance accordée au contexte. Le pilotage déplace alors cette variable, et le changement de comportement ne dit pas ce que ferait un modèle qui se croit déployé.
- Critère : La fiche avance ou met à l'épreuve, comme raison principale, que l'effet du vecteur passe par une variable distincte de la croyance (registre, gabarit, assertion, certitude contextuelle), ou que la direction n'est qu'un mélange de telles variables sans trait propre à l'évaluation.

### 2. Croyance plurielle

- Définition : « Être évalué » recouvre plusieurs variables ou voies distinctes (familles d'indices, déclaration explicite contre reconnaissance implicite d'un banc d'essai, être noté, observé ou conservé) portées par des représentations différentes. Une direction unique n'en neutralise qu'une part, et le comportement d'évaluation passe par les autres voies ou revient sur les combinaisons nouvelles.
- Critère : La fiche avance ou met à l'épreuve, comme raison principale, la décomposition du concept en composantes ou voies distinctes dont une seule est atteinte par la direction pilotée ; le résidu est une autre composante du concept, non la même information déplacée.

### 3. Croyance non retirée

- Définition : Le pilotage efface un signe visible de la croyance (verbalisation, projection linéaire, comportement à une seule intensité d'indice) sans retirer l'information de statut, qui reste présente ou se reconstitue et continue d'agir. Lieux possibles : sous-espace orthogonal, code non linéaire ou moments d'ordre supérieur, couches aval, cache d'attention, fin de génération, seuil de décision seulement déplacé.
- Critère : La fiche avance ou met à l'épreuve, comme raison principale, la survie, la réinférence depuis le contexte, l'auto-réparation ou le simple masquage de la même information de statut après l'intervention, sans invoquer de décomposition du concept.

### 4. État artificiel

- Définition : Le pilotage amène le modèle dans un état qu'aucun contexte naturel ne produit, ni évaluation ni déploiement : sans avis sur le contexte, au niveau « sans indice », indécis, ou hors de la variété naturelle des activations. Le comportement mesuré est celui de ce troisième état, même quand le marqueur d'évaluation tombe et sans dégât générique.
- Critère : La fiche avance ou met à l'épreuve, comme raison principale, l'écart entre l'état piloté (activations ou comportement) et l'état naturel de déploiement, y compris la déformation que l'intervention induit hors de la coordonnée pilotée, sans que cet écart soit décrit comme porteur du statut d'évaluation.

### 5. Effet non spécifique

- Définition : Le changement de comportement vient de la perturbation elle-même et non du contenu « évaluation » : des perturbations sans ce contenu, de même norme, covariance ou influence, le reproduisent, ou la dose efficace abîme déjà le modèle. À dose utile, on mesure un modèle perturbé ou dégradé, pas un modèle en déploiement.
- Critère : La fiche avance ou met à l'épreuve, comme raison principale, l'absence de marge entre l'effet de la direction et celui de témoins sans contenu « évaluation », ou entre dose efficace et dose de dégât générique (fenêtre de dose effondrée, courbe dose–réponse non monotone).

### 6. Lecture biaisée

- Définition : L'échec vient de la façon d'estimer l'effet, non de ce que l'intervention fait au modèle : retenir le meilleur d'une grille de vecteurs, couches et doses, agréger des effets de signes opposés, ou conclure sans étalon de vérité du déploiement. L'estimation devient extrême, faussement nulle ou invérifiable.
- Critère : La fiche avance ou met à l'épreuve, comme raison principale, un défaut de l'analyse (sélection sur une grille, agrégation entre tâches, absence de référence pour calibrer) plutôt qu'un mécanisme interne du modèle.

### 7. Croyance non décisive

- Définition : Même retirée pour de bon, la croyance « je suis évalué » ne fixerait pas le comportement de déploiement : elle peut être inférée après l'engagement comportemental (corrélat, non cause), ou l'écart entre évaluation et déploiement passe aussi par d'autres causes portées par le contexte. Plusieurs états « non évalué » compatibles avec les mesures peuvent alors mener à des comportements différents.
- Critère : La fiche avance ou met à l'épreuve, comme raison principale, que l'écart de comportement entre évaluation et déploiement ne passe pas seulement par la croyance ciblée, ou pas au moment où l'on intervient.

## 2. Effectifs

| Groupe | Fiches | Identifiants |
|---|---|---|
| Cible confondue | 12 | M-011, M-014, M-023, M-024, M-026, M-031, M-032, M-035, M-049, M-057, M-058, M-075 |
| Croyance plurielle | 3 | M-010, M-030, M-052 |
| Croyance non retirée | 18 | M-004, M-007, M-017, M-020, M-029, M-036, M-039, M-044, M-055, M-061, M-063, M-068, M-069, M-070, M-073, M-074, M-081, M-083 |
| État artificiel | 10 | M-003, M-009, M-016, M-025, M-037, M-038, M-040, M-042, M-050, M-072 |
| Effet non spécifique | 9 | M-019, M-033, M-043, M-048, M-066, M-078, M-079, M-080, M-082 |
| Lecture biaisée | 6 | M-001, M-015, M-021, M-022, M-028, M-067 |
| Croyance non décisive | 4 | M-013, M-027, M-046, M-047 |
| Total | 62 | |

## 3. Affectations

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| M-001 | Lecture biaisée | Des excès de signes opposés selon la tâche s'annuleraient dans la courbe agrégée : l'échec est dans l'agrégation, non dans le modèle. | Cible confondue |
| M-003 | État artificiel | Le pilotage rendrait le modèle indécis (gain écrasé) au lieu de le faire passer à l'état « déployé » ; ce troisième état imite le déploiement en moyenne. | Effet non spécifique |
| M-004 | Croyance non retirée | Le pilotage linéaire ne ferait que translater le seuil, sensibilité intacte, ce qui imite un retrait de croyance à une seule intensité d'indice. | État artificiel |
| M-007 | Croyance non retirée | La posture d'évaluation se reconstituerait au fil d'une génération longue ; l'effet mesuré tôt surestime le retrait. | — |
| M-009 | État artificiel | À dégât générique égal, l'échec du pilotage linéaire viendrait de sa sortie de la variété naturelle des activations. | — |
| M-010 | Croyance plurielle | Chaque famille d'indices aurait sa propre direction, même à registre apparié ; une direction ne couvre qu'une composante. | — |
| M-011 | Cible confondue | La direction porterait une composante de certitude contextuelle, variable distincte de la croyance d'évaluation. | — |
| M-013 | Croyance non décisive | Plusieurs états « non évalué » également plausibles mènent à des comportements différents : le retrait mesuré ne fixe pas le comportement de déploiement. | — |
| M-014 | Cible confondue | Un exposant voisin de 2 dirait que la « conscience d'évaluation » n'est qu'un mélange de registre et de prudence générique, sans trait propre. | — |
| M-015 | Lecture biaisée | Sans étalon de vérité du déploiement, la dose ne peut être calibrée ni le retrait vérifié : défaut de référence dans l'analyse. | Effet non spécifique |
| M-016 | État artificiel | Le décalage de la seule moyenne sortirait de la distribution naturelle, là où un transport qui fixe aussi la covariance y reste. | Effet non spécifique |
| M-017 | Croyance non retirée | La croyance serait réinférée depuis le contexte à chaque jeton : soustraire un vecteur constant ne retire pas l'état. | — |
| M-019 | Effet non spécifique | Une direction spécifique aurait une marge entre dose efficace et dose de dégât plus large que des témoins sans contenu. | — |
| M-020 | Croyance non retirée | La verbalisation tomberait avant la politique d'action : le signe visible disparaît, la croyance continue d'agir. | — |
| M-021 | Lecture biaisée | Le meilleur effet retenu sur la grille serait un gain de sélection que des familles sans rapport atteignent aussi. | Effet non spécifique |
| M-022 | Lecture biaisée | Choisir direction et dose sur le comportement révélé sélectionne un effet et ses erreurs : estimation extrême. | — |
| M-023 | Cible confondue | Teste si la direction d'évaluation est un trait corrigé propre, ce que ne serait pas une direction de registre. | — |
| M-024 | Cible confondue | La direction suivrait la forme du gabarit d'évaluation plutôt qu'une croyance abstraite, d'où l'absence de transfert entre formats. | Croyance plurielle |
| M-025 | État artificiel | La soustraction produirait un état « sans avis sur le contexte », absent de la distribution naturelle, et non l'état déployé. | — |
| M-026 | Cible confondue | Teste, avec un marqueur neutre en registre, si l'effet passe par le registre plutôt que par la croyance. | — |
| M-027 | Croyance non décisive | La croyance serait inférée après l'engagement comportemental : corrélat, non cause ; la piloter avant la décision ne change presque rien. | — |
| M-028 | Lecture biaisée | Des effets de signes opposés selon la tâche s'annuleraient dans une métrique agrégée, d'où une fausse absence d'effet. | — |
| M-029 | Croyance non retirée | La croyance survivrait hors de la direction retirée et serait régénérée aux couches suivantes par relecture du contexte. | — |
| M-030 | Croyance plurielle | Déclaration explicite et reconnaissance implicite d'un banc seraient deux voies distinctes ; piloter la première laisse l'autre intacte. | Cible confondue |
| M-031 | Cible confondue | Instrument interne neutre en registre ; l'échec qu'il sert à détecter est la confusion entre perturbation de registre et retrait de croyance. | — |
| M-032 | Cible confondue | Teste par transfert croisé entre registres, à statut constant, si la direction porte la croyance ou le registre. | — |
| M-033 | Effet non spécifique | Le seuil à franchir dépasserait le seuil de dégradation générique : fenêtre effondrée, on mesure un modèle dégradé. | — |
| M-035 | Cible confondue | Teste si la projection suit la preuve factuelle (croyance) ou la surface stylistique (registre). | — |
| M-036 | Croyance non retirée | Le statut serait recodé de façon non linéaire et encore lu en aval une fois le signal linéaire effacé. | — |
| M-037 | État artificiel | Une part de l'effet viendrait de la déformation des moments hors de la coordonnée pilotée, non du retrait du statut. | Effet non spécifique |
| M-038 | État artificiel | Croise deux raisons presque à égalité ; rattachée à la première énoncée, la sortie de la variété naturelle des activations. | Croyance non décisive |
| M-039 | Croyance non retirée | Le cache d'attention garderait des conséquences de la croyance que le pilotage des activations courantes ne touche pas. | — |
| M-040 | État artificiel | Le marqueur tombe mais comportements et activations restent loin de la distribution naturelle de déploiement : troisième état. | — |
| M-042 | État artificiel | Le sens « déploiement » n'aurait pas de contenu propre : il ramène au niveau « sans indice », non au déploiement. | — |
| M-043 | Effet non spécifique | Sans excès sur le maximum de témoins de même norme et de mêmes libertés, l'effet reste compatible avec une perturbation générique. | Lecture biaisée |
| M-044 | Croyance non retirée | Le pilotage translaterait le seuil sans retirer la sensibilité aux indices : croyance masquée à une intensité, non retirée. | — |
| M-046 | Croyance non décisive | Le contexte porte d'autres causes du comportement (information, utilité, conséquences) que le retrait de la croyance laisse intactes. | — |
| M-047 | Croyance non décisive | Après l'engagement, la croyance reste lisible mais ne décide plus : le calendrier conditionne tout effet du pilotage. | Croyance non retirée |
| M-048 | Effet non spécifique | Au-delà d'une dose optimale, la dégradation ferait remonter le marqueur : courbe dose–réponse non monotone. | État artificiel |
| M-049 | Cible confondue | Double dissociation pour tester si le vecteur déplace le registre plutôt que le statut. | — |
| M-050 | État artificiel | Les activations pilotées resteraient séparables des activations naturelles de déploiement de même contenu : troisième état. | — |
| M-052 | Croyance plurielle | « Être évalué » regrouperait des variables causales distinctes qu'un axe moyen ne neutralise pas une fois dissociées. | — |
| M-055 | Croyance non retirée | La croyance serait portée par la covariance entre positions, laissée intacte par la soustraction d'un vecteur fixe et relue par les têtes aval. | État artificiel |
| M-057 | Cible confondue | Le vecteur explicite porterait l'assertion d'un interlocuteur sur le contexte, non l'inférence propre du modèle. | Croyance plurielle |
| M-058 | Cible confondue | Teste si la composante hors registre est un trait propre à l'évaluation ou seulement du registre plus du bruit. | — |
| M-061 | Croyance non retirée | L'information de statut subsisterait au-delà du premier ordre, lisible par un lecteur non linéaire après projection. | — |
| M-063 | Croyance non retirée | Le cache du préfixe garderait une information de statut active que le pilotage du flux résiduel ne couvre pas. | — |
| M-066 | Effet non spécifique | Une direction moins pure toucherait le statut à une dose plus proche du dégât général : fenêtre étroite. | — |
| M-067 | Lecture biaisée | L'hypothèse adverse tenue pour la plus probable est d'abord un gain de sélection sur la grille, que la loi nulle doit contenir. | Cible confondue |
| M-068 | Croyance non retirée | Les couches tardives réinjecteraient la projection retirée (auto-réparation), ce qui plafonne l'effet. | — |
| M-069 | Croyance non retirée | L'information de statut serait recodée et encore causalement active ; la baisse de l'oracle traduirait une rupture d'étalonnage. | Lecture biaisée |
| M-070 | Croyance non retirée | Le pilotage bloquerait le canal de verbalisation plus facilement qu'il n'efface la représentation amont. | — |
| M-072 | État artificiel | Le pilotage ramènerait au plancher « sans indice », non au déploiement ; le coût croissant en dose relève du second choix. | Effet non spécifique |
| M-073 | Croyance non retirée | Le statut resterait lisible dans le complément orthogonal de l'axe injecté et dans une couche non injectée. | — |
| M-074 | Croyance non retirée | Seuil translaté et résidu lisible hors de l'axe : la croyance serait masquée, non retirée. | — |
| M-075 | Cible confondue | Le vecteur « évaluation contre déploiement » serait pour une large part un vecteur de registre. | — |
| M-078 | Effet non spécifique | L'essentiel de la baisse serait une perturbation générique bien orientée, reproduite par des témoins tirés sous la covariance. | — |
| M-079 | Effet non spécifique | Un témoin apparié à la covariance reproduirait une grande part de la baisse : effet publié en partie générique. | — |
| M-080 | Effet non spécifique | Si la croyance est inférée de plusieurs indices, la dose nécessaire dépasserait la dose de dégât : plus de fenêtre. | — |
| M-081 | Croyance non retirée | Après alignement de la moyenne, le reste de distance porté par les covariances serait encore lu comme « évaluation ». | État artificiel |
| M-082 | Effet non spécifique | Des témoins appariés sur l'influence fonctionnelle réduiraient l'avantage : le vecteur viserait une région influente, non la croyance. | — |
| M-083 | Croyance non retirée | Le statut survivrait aux couches aval et dans le cache du contexte, d'où la reprise du comportement à l'arrêt du pilotage. | — |

## 4. Fiches à second choix (19)

- M-001 : Lecture biaisée → second choix Cible confondue
- M-003 : État artificiel → second choix Effet non spécifique
- M-004 : Croyance non retirée → second choix État artificiel
- M-015 : Lecture biaisée → second choix Effet non spécifique
- M-016 : État artificiel → second choix Effet non spécifique
- M-021 : Lecture biaisée → second choix Effet non spécifique
- M-024 : Cible confondue → second choix Croyance plurielle
- M-030 : Croyance plurielle → second choix Cible confondue
- M-037 : État artificiel → second choix Effet non spécifique
- M-038 : État artificiel → second choix Croyance non décisive
- M-043 : Effet non spécifique → second choix Lecture biaisée
- M-047 : Croyance non décisive → second choix Croyance non retirée
- M-048 : Effet non spécifique → second choix État artificiel
- M-055 : Croyance non retirée → second choix État artificiel
- M-057 : Cible confondue → second choix Croyance plurielle
- M-067 : Lecture biaisée → second choix Cible confondue
- M-069 : Croyance non retirée → second choix Lecture biaisée
- M-072 : État artificiel → second choix Effet non spécifique
- M-081 : Croyance non retirée → second choix État artificiel

## 5. Rubrique « aucun mécanisme d'échec »

Non ouverte : chaque fiche avance ou met à l'épreuve au moins un mécanisme d'échec. La plus proche de cette rubrique est M-031 (voir limite 1).

## 6. Limites (tensions relevées pendant l'affectation ; définitions non réécrites)

1. M-031 est d'abord un instrument de mesure (un marqueur interne neutre en registre) : son champ « mécanisme » explique pourquoi le marqueur marcherait, non pourquoi le pilotage échouerait. Rattachée à « Cible confondue », l'échec qu'elle sert à détecter ; on aurait pu ouvrir pour elle la rubrique « aucun mécanisme d'échec ». Plus largement, plusieurs fiches sont des tests à prédiction positive (par exemple M-019, M-023, M-026, M-032, M-035, M-049, M-058, M-066) : elles sont rangées sous l'échec qu'elles mettent à l'épreuve, ce que permet la formule « avance ou met à l'épreuve » des critères, mais c'est une lecture.
2. Plans croisés : M-038 (géométrie × calendrier), M-047 (calendrier × seuil), M-072 (absence d'indice × dose), M-067 (sélection × registre) et M-004 (seuil × pente) portent deux mécanismes presque à égalité. La règle « un seul groupe » impose un choix, fait sur l'ordre d'énoncé ou sur la conclusion de la fiche ; le second choix garde l'autre mécanisme.
3. Frontière « Croyance non retirée » / « État artificiel » sur la courbe psychométrique : la translation du seuil (M-044, M-074, M-004) est rangée comme masquage d'une croyance dont la sensibilité aux indices reste intacte, la baisse de pente (M-003) comme état indécis. Le critère tient, mais une lecture qui verrait dans toute déformation de la courbe un troisième état regrouperait autrement.
4. Même frontière sur les moments d'ordre supérieur : la clause « sans que cet écart soit décrit comme porteur du statut » sépare M-055 et M-081 (croyance non retirée) de M-016 et M-037 (état artificiel) ; M-055 et M-081 restent à la limite, d'où leur second choix.
5. Frontière « Cible confondue » / « Croyance plurielle » : décider si l'assertion d'un interlocuteur (M-057), la forme du gabarit (M-024) ou la déclaration explicite (M-030) est une autre variable que la croyance ou une composante du concept « être évalué » relève de l'interprétation. « Croyance plurielle » ne garde que 3 fiches ; ce serait le premier groupe à fondre si l'on resserrait à 6.
6. « Lecture biaisée » loge l'échec dans l'analyse et non dans le modèle. C'est une raison d'échec et non une méthode de mesure, mais M-015 (absence d'étalon de vérité) y est une limite de connaissance plus qu'un mécanisme.
7. « Croyance non retirée » rassemble 18 fiches hétérogènes par le lieu du résidu (sous-espace, code non linéaire, couches aval, cache, fin de génération, seuil). La séparation entre masquage et reconstitution n'a pas été faite, pour rester dans 7 groupes et parce que plusieurs fiches (M-070, M-074) joignent les deux.
8. Les chiffres, modèles et attributions cités dans les fiches n'ont pas été vérifiés et n'ont joué aucun rôle dans l'affectation.
