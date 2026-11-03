# Groupes de problèmes sous-estimés — piste Kirchner, version 1

Groupeur neuf, aveugle au classement. Lectures : la consigne `piste-kirchner-groupeur-aveugle-v1.md` (empreinte vérifiée), puis le seul fichier d'entrée ci-dessous ; aucun autre fichier lu, aucun appel réseau ni de modèle.

- Entrée : `/home/claude/scratch/kirchner-rapport/piste-kirchner/fiches-a-grouper-v1.json`, sha256 `f157eea6b88b3150ba42750828dacc3673414ecb55021a9339d30033c8686843` (vérifiée avant lecture et revérifiée avant écriture), 14 fiches (KM-01 à KM-15, KM-08 absent).
- Compagnon : `groupes-problemes-v1.json` (même dossier), mêmes groupes et mêmes affectations.

## Chronologie (heures données par `date -u`)

- 2026-11-03T13:12:50Z — début : empreinte de l'entrée vérifiée, fichiers de sortie absents.
- 2026-11-03T13:18:04Z — **définitions des groupes écrites et figées**, après lecture des 14 fiches et avant toute affectation. Empreinte canonique du bloc : `ab95eb63e39daf885a7e784e93b6914d1b0827e5aa643c0db852789ccb5676a2` (sha256 du texte UTF-8 de `json.dumps(groupes, ensure_ascii=False, sort_keys=True, separators=(",", ":"))`, recalculable sur la clé `groupes` du fichier compagnon).
- 2026-11-03T13:21:23Z — affectations terminées ; les deux fichiers écrits, chacun en une seule écriture (création exclusive, rien d'écrasé).

## Définitions (figées à 13:18:04 UTC, inchangées ensuite)

Un groupe est un problème — ce qui, dans la recherche d'alignement automatisée ou sa sélection, fait passer pour un progrès ce qui n'en est pas, ou cache ce qui en est un —, non une méthode de mesure.

### 1. Garde-fous présumés

- **Définition.** Les instruments du harnais (classement, banc tenu à l'écart, garde de capacité, moniteurs de langage) sont crédités d'une valeur jamais mesurée contre un plancher : hasard, base triviale ou vérification mécanique quasi gratuite. Ils peuvent être au plafond, ne mesurer que du bruit ou ne rien ajouter à la vérification mécanique, et une valeur réelle reste cachée faute d'être isolée.
- **Critère.** La question principale de la fiche est de savoir si un instrument mesure quelque chose, ou ajoute quelque chose à un plancher ou à une base bon marché, sans privilégier l'un des mécanismes d'échec propres aux quatre autres groupes.

### 2. Bruit sélectionné

- **Définition.** Retenir le meilleur parmi de nombreuses mesures bruitées, ou laisser resoumettre et consulter de façon adaptative un même ensemble d'évaluation, fait franchir les seuils et monter au sommet par le hasard, le nombre d'essais ou le surapprentissage de l'échantillon. L'erreur ainsi sélectionnée est aléatoire : elle se résorbe quand on remesure le lauréat sur des données fraîches.
- **Critère.** La question principale est de savoir si une promotion, un franchissement de seuil ou un rang de tête s'explique par la variance de la mesure, la multiplicité des essais ou la réutilisation adaptative d'un ensemble réservé, sur des classes que l'instrument couvre et même avec un détecteur parfait des triches connues.

### 3. Trou de couverture

- **Définition.** Une garantie statistique (nulle, banc) ne protège que contre les classes d'échec qu'elle modélise : une classe hors couverture passe sans garantie, quel que soit le soin du protocole (tirages frais, puissance). Déclarer où passe la frontière peut en outre servir de carte à qui cherche à la franchir.
- **Critère.** La question principale porte sur une classe d'échec que la garantie ne couvre pas par construction (passe-t-elle, un remède la referme-t-il, la publication de la frontière aide-t-elle à l'exploiter), l'échec se produisant même sans pression de sélection et sans angle mort partagé entre composants.

### 4. Angles morts partagés

- **Définition.** Deux composants du contrôle qui partagent une famille de modèles ou une source de connaissance (agent et moniteur, deux moniteurs, juge et moniteur) ratent les mêmes cas. L'empilement des contrôles donne alors une illusion de redondance, et un moniteur de la famille de l'agent peut se montrer indulgent.
- **Critère.** La grandeur principale que la fiche estime est une dépendance entre les erreurs de deux composants qui partagent une famille ou une source de connaissance, au-delà de la difficulté propre des cas : co-ratage, interaction même famille contre autre famille, ou baisse du rappel de l'un parmi ce que l'autre laisse passer.

### 5. Sélection sans gradient

- **Définition.** Sans aucun entraînement contre les instruments, classer, recopier entre agents ou choisir une configuration sur un banc reste une optimisation : ce qui est retenu ou propagé s'enrichit en ce que les instruments manquent systématiquement. Une validité établie avant la sélection, ou sur le banc qui a servi à sélectionner (rappel d'un moniteur, gain de surveillabilité), ne vaut alors plus pour ce qui est retenu.
- **Critère.** La question principale est de savoir si un mécanisme non défensif de sélection ou de propagation (classement, forum, choix de configuration) enrichit ce qu'il retient ou propage en ce que les instruments manquent, ou si une validité établie avant ou pendant la sélection vaut encore pour ce qui est retenu ; l'erreur en jeu est systématique et survivrait à une remesure par le même instrument.

## Affectations (une fiche, un seul groupe : celui de son problème principal)

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| KM-01 | Garde-fous présumés | Demande, pour chaque instrument du harnais, s'il mesure quelque chose contre des cas honnêtes appariés et des planchers, sans privilégier un mécanisme d'échec. | Bruit sélectionné |
| KM-02 | Trou de couverture | Une classe hors de la nulle (W2) reste faussement promue à au moins 0,8, et les tirages frais ne la referment pas ; tricheurs scriptés, donc aucune sélection en jeu. | — |
| KM-03 | Sélection sans gradient | Demande si le gain d'une configuration choisie sans gradient sur un banc de surveillabilité vaut encore hors du banc, ou n'est qu'un enrichissement en gains propres au banc. | Trou de couverture |
| KM-04 | Garde-fous présumés | Mesure ce que le moniteur de langage ajoute à la vérification mécanique (apport contre coût, l'oracle mécanique servant d'étiquette) : valeur ajoutée contre une base bon marché. | — |
| KM-05 | Bruit sélectionné | Une méthode réellement en échec franchit la garde de capacité par simple resoumission près du seuil : multiplicité des essais sur une mesure bruitée. | — |
| KM-06 | Garde-fous présumés | Exige que le moniteur de langage batte de 0,15 de rappel, à fausses alertes égales, une vérification mécanique isolée et des planchers aléatoires : valeur ajoutée non établie. | — |
| KM-07 | Angles morts partagés | Baisse du rappel d'un moniteur parmi les lois que le juge statistique promeut, attribuée à une classe que juge et moniteur connaissent tous deux par la description publique. | Sélection sans gradient |
| KM-09 | Angles morts partagés | Interaction même famille contre autre famille entre agent et moniteur, à fausses alertes égalisées : indulgence ou angles morts partagés. | — |
| KM-10 | Sélection sans gradient | Le forum, mécanisme non défensif de propagation, recopierait une classe de triche qui paie davantage que les méthodes honnêtes publiées. | — |
| KM-11 | Angles morts partagés | Excès de co-ratage entre deux moniteurs de même famille, à entrée identique et ratage égalisé, au-delà de la difficulté propre des items. | — |
| KM-12 | Trou de couverture | Rendre visible la frontière de la nulle servirait de carte pour faire promouvoir dès le premier essai de fausses lois hors nulle. | — |
| KM-13 | Bruit sélectionné | Le gagnant du 99e centile serait le maximum d'estimations bruitées ; un arrêt séquentiel calibré sur épisodes honnêtes ferait aussi bien hors banc, pour une fraction du budget. | — |
| KM-14 | Bruit sélectionné | La réutilisation adaptative d'un banc réservé fixe, séparée de la multiplicité des essais, fait promouvoir de fausses méthodes que des tirages frais arrêtent, sur des classes couvertes. | — |
| KM-15 | Sélection sans gradient | Effet de type Berkson : à moniteur figé et sans gradient, la sélection par le score abaisse le rappel parmi les violations que le classement retient. | — |

**Effectifs (14 fiches).** Garde-fous présumés : 3 (KM-01, KM-04, KM-06) ; Bruit sélectionné : 3 (KM-05, KM-13, KM-14) ; Trou de couverture : 2 (KM-02, KM-12) ; Angles morts partagés : 3 (KM-07, KM-09, KM-11) ; Sélection sans gradient : 3 (KM-03, KM-10, KM-15).

**Fiches à second choix (3).** KM-01 → Bruit sélectionné ; KM-03 → Trou de couverture ; KM-07 → Sélection sans gradient.

## Limites

1. **Définitions écrites après lecture.** La consigne impose de les écrire avant toute affectation, non avant lecture : elles sont donc ajustées à ce corpus. Deux formulations reprennent presque une fiche (« quel que soit le soin du protocole (tirages frais, puissance) » pour KM-02 ; « servir de carte » pour KM-12), ce qui rend ces deux affectations quasi automatiques ; un groupeur aveugle aux fiches couperait peut-être autrement.
2. **Angles morts partagés contre Sélection sans gradient.** KM-07 et KM-15 estiment la même forme de grandeur (rappel parmi les retenus moins rappel dans toute la population). La coupure tient au composant qui sélectionne (juge statistique, défensif, pour KM-07 ; classement, non défensif, pour KM-15) et à la cause invoquée (connaissance partagée contre covariance entre gain de score et détectabilité). Un découpage par forme de grandeur les réunirait.
3. **Sélection sans gradient contre Trou de couverture (KM-03).** Le test porte sur des classes absentes du banc, ce qui relève de la couverture ; la cause soupçonnée est la sélection. Fiche affectée par la cause, d'où le second choix.
4. **Bruit sélectionné contre Sélection sans gradient.** La frontière oppose une erreur aléatoire (qui se résorbe sur données fraîches) à une erreur systématique (qui survit à la remesure par le même instrument). KM-13 (surapprentissage possible d'un banc d'environ 200 exemples) et KM-14 (proposeur adaptatif, donc optimiseur sans gradient) ont une part systématique possible ; le critère les range dans le bruit parce que leur remède revendiqué est la donnée fraîche ou l'arrêt séquentiel.
5. **Garde-fous présumés, groupe résiduel.** C'est le groupe le plus proche d'un programme de mesure ; son critère (« sans privilégier l'un des mécanismes d'échec propres aux quatre autres groupes ») dépend des quatre autres définitions. KM-01 est un portefeuille : sa première expérience recouvre Bruit sélectionné (fidélité du classement, banc tenu à l'écart consulté plusieurs fois) et contient en germe les questions de KM-05, KM-13 et KM-14 ; l'affectation unique le masque.
6. **KM-04 et l'effet « même modèle ».** La fiche situe la valeur du moniteur de langage là où « se jouerait l'effet même modèle » (hypothèse d'une version) : lien avec Angles morts partagés jugé secondaire, non compté en second choix.
7. **KM-10 sans rappel.** La fiche n'estime aucun rappel (« ce bras ne sert pas à mesurer le rappel ») ; son rattachement à Sélection sans gradient suppose que la classe plantée qui paie est une classe que les instruments laissent passer, ce que la fiche ne dit qu'implicitement.
8. **Champs tronqués.** `premiere_experience` est coupé net à 900 caractères pour 8 fiches (KM-01, KM-03, KM-04, KM-05, KM-06, KM-09, KM-11, KM-15) ; les affectations reposent d'abord sur `enonce` et `mecanisme`.
9. **KM-08 absent** de l'entrée (numérotation sautée) ; non recherché, aucune autre lecture n'étant permise.
10. **Effectifs inégaux** (Trou de couverture : 2 fiches) : propriété du corpus, pas un critère ; aucune définition n'a été retouchée pour équilibrer.
