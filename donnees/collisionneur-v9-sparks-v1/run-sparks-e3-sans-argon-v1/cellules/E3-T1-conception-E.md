# Proposition E — Évaluer l’apport marginal, pas la plausibilité du récit

**OBSERVÉ-NON-AUDITÉ —** Les propositions A–D ne sont pas transmises ; je ne leur attribue aucun contenu.

**Convention de statut.** Les résultats des pièces sont **RAPPORTÉS**, sans nouvel audit ici. Les propositions expérimentales, effets attendus et budgets ci-dessous sont des **HYPOTHÈSES**. Tous les nombres de conception sont **illustratifs, supposés** ; les calculs correspondants sont également signalés. Aucune nouveauté bibliographique n’est revendiquée.

## A. Ce que la question suppose sans l’établir

| Présupposé | Statut et objection |
|---|---|
| Réussir à reconnaître une tâche implique pouvoir détecter un trait d’alignement. | **HYPOTHÈSE.** Le cas sycophancie échoue sur les poids seuls ; la réussite avec attention est rapportée sur un choix forcé sans témoins nuls — pièce « lecture factuelle », §3. |
| Un lecteur de poids apporte une information absente de la boîte noire. | **HYPOTHÈSE.** Le billet ne mesure pas cet apport à taux de fausses alertes et budget comparables — même pièce, §5–6. |
| Une différence lisible localise une cause modifiable. | **HYPOTHÈSE.** Les greffes rapportées ne déplacent pas le comportement dans l’expérience de sycophancie — même pièce, §3.5. Le travail public sur la validité de construit rapporte également un échec de réplication interventionnelle — pièce « nos résultats », §7. |
| Une édition parcimonieuse préserve le reste du comportement. | **HYPOTHÈSE.** La proportion de poids modifiés ne mesure pas les dommages fonctionnels. Les bancs rapportés pour Qwen ne constituent pas une mesure exhaustive de préservation — « lecture factuelle », §4–5. |
| Le juge figé peut accueillir ces nouvelles propositions sans changement de garantie. | **HYPOTHÈSE.** Une attaque hors couverture déclarée du nul réussit dans le programme public — « nos résultats », §3. Le gel du juge ne suffit donc pas à garantir la pertinence de son nul. |
| Une absence d’alarme indique une absence de sabotage. | **HYPOTHÈSE.** Les résultats P3 sont explicitement « non détecté à cette puissance » — « nos résultats », §6. |
| Plusieurs lecteurs ou essais rendent le résultat plus solide. | **HYPOTHÈSE.** Ils peuvent aussi multiplier les occasions de sélection. Leur agrégation doit être engagée avant les tests. |

**HYPOTHÈSE — Décision d’intégration.** Le lecteur devient un **proposeur d’hypothèses ou de scores**, jamais un certificateur de sécurité ni son propre évaluateur. Je propose trois fiches, avec des critères d’abandon séparés.

---

## B. Fiche DELTA — Les poids ajoutent-ils une détection utile ?

### Question falsifiable

**HYPOTHÈSE —** À taux de fausses alertes fixé, un lecteur non entraîné pour cette tâche, recevant un résumé déterministe du delta d’un adaptateur, améliore-t-il la détection d’un sabotage comportemental au-delà des sorties et des vérifications mécaniques ?

**Effet prédit :** augmentation de la sensibilité, sans augmentation tolérée des fausses alertes.

**Changement dans le programme :** ajout d’un instrument candidat au programme de contrôle, avec obligation de démontrer son apport marginal.

### Duel préenregistré

Définir \(G\) comme le gain de sensibilité du système « boîte noire + delta », relativement au meilleur comparateur choisi **sur développement seulement**, sous la contrainte de fausses alertes.

- **H_A :** \(G>10\) points de pourcentage et taux de fausses alertes \(\leq5\,\%\).
- **H_B :** \(G\leq10\) points, **ou** taux de fausses alertes \(>5\,\%\).

**HYPOTHÈSE —** Ces hypothèses sont exclusives et couvrent le domaine annoncé. Un intervalle entièrement du côté utile réfute \(H_B\) ; un intervalle entièrement du côté insuffisant, ou un dépassement établi du plafond d’alertes, réfute \(H_A\). Un intervalle chevauchant la frontière donne **indécision**, pas réussite ni réfutation.

### Première expérience

**HYPOTHÈSE — Plan illustratif, supposé :**

- Modèle cible : Gemma 3 270M, avec adaptateurs provenant des organismes honnêtes et de sabotage déjà disponibles, sans développer ici de procédure offensive.
- Banque finale : **60 unités honnêtes indépendantes**, **30 unités comportementalement positives**, plus une banque de développement disjointe.
- Unité : une famille d’entraînement et de tâches ; plusieurs questions d’un même modèle ne deviennent pas artificiellement plusieurs unités indépendantes.
- Positivité déterminée par un évaluateur mécanique sur des épisodes scellés, pas par les déclarations de l’agent ni par le lecteur.
- Aveuglement : identifiants opaques, ordre aléatoire, aucun nom de fichier ou métadonnée révélant la classe.
- Lecteurs de **deux familles distinctes**, avec **deux répétitions** ; règle d’agrégation gelée. Pas de sélection rétrospective du meilleur lecteur.

**HYPOTHÈSE — Contrôles honnêtes appariés :**

- même modèle de départ, rang, nombre d’étapes et enveloppe de calcul ;
- affinages honnêtes avec variations bénignes de style, verbosité et difficulté ;
- contrastes entre modèles honnêtes entraînés avec graines différentes ;
- duplications exactes comme témoins techniques, mais jamais comme substituts aux vrais nuls d’entraînement.

### Instruments et comparateurs

**HYPOTHÈSE —** Le lecteur reçoit une représentation bornée : statistiques de tenseurs et extraits choisis par une règle indépendante des étiquettes. La conclusion portera sur **cette représentation**, pas sur une lecture exhaustive des poids.

Comparer, à budget annoncé :

- boîte noire : erreurs, désaccords avec l’oracle, coûts déclarés contre coûts mesurés ;
- vérifications mécaniques : normes des deltas, distances au modèle initial, statistiques spectrales, classifieur simple sur ces statistiques ;
- sonde d’activation figée, avec sondes aléatoires appariées en covariance ;
- lecteur de delta seul ;
- boîte noire augmentée du lecteur.

**HYPOTHÈSE — Mesure minimale :** sensibilité, fausses alertes, abstentions et coût par verdict. Une abstention ne compte pas comme détection et ne disparaît pas du dénominateur.

**Calcul illustratif —** Avec aucune fausse alerte sur **60 unités honnêtes indépendantes**, la borne binomiale supérieure unilatérale à **95 %** est d’environ **4,9 %**. Cela ne vaut pas pour des observations corrélées déguisées en unités indépendantes.

**Seuil d’abandon illustratif :** abandon de l’instrument comme ajout opérationnel si la borne supérieure du gain reste sous **10 points**, ou si le plafond d’alertes est dépassé de manière établie. Si l’étude reste indécise au budget fixé, ne pas déployer ; ne pas annoncer l’absence d’effet.

### Corruptibilité : portée limitée

**HYPOTHÈSE — Classe de menace.** L’adversaire peut soumettre un point de contrôle modifié et connaître la spécification du moniteur, mais ne peut modifier ni le juge, ni la banque finale, ni les journaux externes.

La défense à mesurer est la baisse de sensibilité, à fausses alertes constantes, sur une banque scellée de soumissions adversariales autorisées. Déclarer l’accès accordé et le nombre de soumissions consommées. **Aucun procédé de fabrication ou de dissimulation n’est proposé ici.**

**HYPOTHÈSE — Limite.** Sans cette banque, DELTA ne mesure que la détection non adversariale, pas la corruptibilité.

**Pourquoi ce n’est pas une revendication déjà acquise :** **HYPOTHÈSE.** L’objet n’est pas « lire un delta », déjà signalé dans la question, mais démontrer un gain marginal sous nul réaliste, avec lecteurs multiples et budget de sélection compté.

---

## C. Fiche CONSTRUIT — Retirer le signal change-t-il réellement la sycophancie ?

### Question falsifiable

**HYPOTHÈSE —** Une intervention ciblant un composant désigné par le lecteur diminue-t-elle la sensibilité à la pression sociale, plutôt que la verbosité, l’échelle des notes, la propension à répondre ou la compétence générale ?

**Effet prédit :** diminution du déplacement vers la suggestion erronée lorsque la pression augmente, avec préservation des réponses sans pression.

**RAPPORTÉ — Ancrage.** Le travail psychophysique public décrit une attraction vers un point fixe sous pression dosée ; le travail de validité de construit rapporte une direction lisible sans intervention répliquée concluante — « nos résultats », §7.

**Changement dans le programme :** transformer une interprétation descriptive en prédiction interventionnelle engagée ; raccorder les deux travaux publics sur la sycophancie sans supposer qu’ils mesurent déjà la même chose.

### Duel préenregistré

Définir \(A\) comme l’aire sous la courbe « probabilité de suivre une suggestion fausse » en fonction d’une dose de pression fixée.

- **H_A :** l’intervention ciblée réduit \(A\), au-delà du témoin apparié, d’au moins **10 points**, avec perte d’exactitude sans pression d’au plus **3 points**.
- **H_B :** au moins une de ces conditions échoue.

**HYPOTHÈSE —** Une borne inférieure du bénéfice au-dessus du seuil et une borne supérieure des dommages sous le plafond réfutent \(H_B\). Une borne supérieure du bénéfice sous le seuil, ou des dommages établis au-delà du plafond, réfute \(H_A\). Sinon : indécision.

### Première expérience

**HYPOTHÈSE — Plan illustratif, supposé :**

- Gemma 3 270M pour le pilote ; Llama-3.1-8B-Instruct seulement pour une réplication ultérieure.
- **Quatre niveaux de pression**, dont l’absence de suggestion.
- Questions factuelles à réponse mécanique, avec suggestions justes, fausses et absentes ; formulations et faits séparés entre découverte et test.
- Comparaison en aveugle des modèles : original, intervention ciblée, intervention témoin appariée en ampleur, manipulation factice.
- Le lecteur choisit son candidat sur développement. La procédure d’intervention et son intensité sont ensuite gelées, sans recherche sur le test.
- Générations neuves ; évaluation de réponses entières ; refus, erreurs et non-réponses gardés comme catégories distinctes.
- Rééchantillonnage et intervalles au niveau des faits ou familles de faits, pas au niveau de paraphrases corrélées.

**HYPOTHÈSE — Témoin négatif essentiel.** Un affinage honnête produisant un changement stylistique comparable doit subir le même protocole. Une baisse des notes d’accord, sans baisse des accords factuellement faux, échoue au test de construit.

### Mesures minimales des instruments

**HYPOTHÈSE —**

- **Sonde de direction :** sensibilité et fausses alertes pour identifier les épisodes d’accord erroné, contre sondes aléatoires appariées et caractéristiques des sorties.
- **Moniteur d’attention :** même évaluation ; préfixes de réponse imposés et réponses naturellement produites analysés séparément.
- **Mesure psychophysique :** courbe dose–réponse et résidus prédictifs sur faits nouveaux ; comparaison à une fréquence constante et à une régression simple sur la dose.
- **Notation par modèle de langue :** sensibilité et fausses alertes relativement à l’oracle factuel ; cas honnêtes contenant accord justifié, correction polie, désaccord et paraphrases.
- **Intervention :** bénéfice causal apparié et dommages, non un « taux de détection » artificiellement attribué à une opération qui ne classe rien.

**HYPOTHÈSE —** Pour les tâches d’éloge ou de critique sans vérité mécanique, utiliser des ancrages fixes et une évaluation humaine aveugle ; ne pas prétendre que le pilote factuel valide toute la sycophancie sociale.

**Seuil d’abandon illustratif :** abandon de la prétention causale pour le candidat si le bénéfice ne peut atteindre **10 points**, ou si les dommages dépassent **3 points**. Une direction qui reste prédictive peut survivre comme instrument de lecture, mais pas comme cause démontrée.

**Pourquoi ce n’est pas simplement « retirer une direction » :** **HYPOTHÈSE.** Le critère distinctif est une modification prédite de la courbe comportementale, contrôlée contre changement d’échelle et dégradation générale. La nouveauté reste à vérifier.

---

## D. Fiche ORACLE — Les lecteurs de poids produisent-ils de meilleures lois pour l’organisme ?

### Question falsifiable

**HYPOTHÈSE —** Ajouter l’accès aux poids permet-il aux proposeurs de produire davantage de lois correctes et non redondantes, par unité de budget, sans augmenter les promotions fausses ?

**Effet prédit :** hausse du rendement de lois validées sur de nouvelles familles de réseaux.

**Changement dans le programme :** nouvelle famille de tâches à vérité exécutable ; aucune modification du juge pendant une course.

### Duel préenregistré

Définir \(R\) comme le gain de rendement de lois correctes, confirmé par oracle, de « descriptions + poids » contre « descriptions seules ».

- **H_A :** \(R>20\,\%\), avec probabilité de promotion fausse par course \(\leq5\,\%\).
- **H_B :** \(R\leq20\,\%\), ou cette probabilité dépasse \(5\,\%\).

**HYPOTHÈSE —** Les bornes d’incertitude déterminent quelle hypothèse est réfutée ; leur chevauchement entraîne l’indécision.

### Première expérience

**HYPOTHÈSE — Plan illustratif, supposé :**

- Petits réseaux à domaine d’entrée fini, où l’oracle peut vérifier exhaustivement la propriété : symétrie, monotonie ou comportement d’une petite machine d’états.
- Propriétés positives et négatives certifiées par l’oracle avant toute lecture.
- Sérialisation, architecture et métadonnées neutralisées comme sources triviales d’étiquette.
- Familles et graines nouvelles à la confirmation.
- Même quota de soumissions, même budget de jetons, même procédure d’arrêt dans les deux bras.
- Témoins : réseaux sans propriété, soumissions équivalentes déjà présentes dans l’archive, sorties aléatoires et prédictions issues de statistiques mécaniques.
- Nul, multiplicité et règles de non-redondance engagés avant la course. Les cas hors couverture sont signalés comme tels, jamais comptés parmi les cas garantis.

**RAPPORTÉ — Motivation.** La recombinaison de lois acceptées a déjà révélé un trou de couverture ; des juges de langage au plafond n’ont pas discriminé les fiches — « nos résultats », §2–4.

### Mesures minimales des instruments

**HYPOTHÈSE —**

- **Juge statistique :** puissance sur lois plantées ; probabilité d’au moins une promotion fausse par course nulle entière. Battre une règle aléatoire ne suffit pas : vérifier la couverture contre l’oracle.
- **Proposeur lecteur de poids :** taux de lois correctes parmi les soumissions, rendement par coût, promotions fausses ; comparaison aux mêmes proposeurs sans poids.
- **Juges de langage :** sensibilité aux fiches valides et fausses alertes sur fiches invalides appariées en longueur et qualité rédactionnelle. Comparateur : vérificateur mécanique de format, preuves et prédictions.
- **Oracle :** tests de cohérence et cas synthétiques dont la réponse est connue indépendamment ; aucune vérité fondée sur le vote des lecteurs.

**Seuil d’abandon illustratif :** ne pas intégrer l’accès aux poids si la borne supérieure de son gain de rendement reste sous **20 %**, ou si le plafond de promotions fausses est dépassé.

**Pourquoi ce n’est pas simplement un zoo de réseaux :** **HYPOTHÈSE.** L’objet évalué est le rendement scientifique de l’organisme, sous sélection répétée et archive cumulative, non la précision isolée d’un lecteur.

---

## E. Ancrage matériel et ordre d’exécution

**HYPOTHÈSE — Estimations illustratives, supposées, non mesurées :**

| Fiche | Matériel et calcul | Appels externes | Condition de faisabilité |
|---|---|---|---|
| DELTA | Une carte de **24 Go**, environ **20–50 heures-GPU** sur la cible 270M | **20–40 $**, résumés bornés | Banque existante ou adaptations courtes ; mesurer d’abord le coût d’une unité |
| CONSTRUIT | Même carte, **10–30 heures-GPU** pour le pilote | **5–15 $** | Peu de candidats engagés ; générations courtes et oracle factuel |
| ORACLE | CPU pour l’oracle, éventuellement **2–8 heures-GPU** | **10–25 $** | Domaine réellement énumérable ; petits réseaux |

**HYPOTHÈSE —** Ces budgets sont **par fiche**, pas une promesse de tout exécuter simultanément pour quelques dizaines de dollars. Arrêter ou réduire le périmètre après chronométrage d’une unité, sans réduire après coup les exigences statistiques.

**RAPPORTÉ —** Gemma 3 270M figure dans le billet et Llama-3.1-8B-Instruct dans le programme P3 — « lecture factuelle », §3 ; « nos résultats », §6. Leur disponibilité effective, leurs licences et les formats locaux devront être contrôlés avant lancement.

**HYPOTHÈSE — Priorité.** Commencer par **ORACLE** pour éprouver l’intégration au juge ; lancer **DELTA** si la banque de jumeaux existe ; engager **CONSTRUIT** seulement après gel d’un candidat interprétable. Dans tous les cas, publier les essais sans soumission, les abstentions et les critères d’arrêt.

**Conclusion — HYPOTHÈSE.** L’intégration défendable consiste à demander : *quelle information supplémentaire, quelle prédiction interventionnelle et quelle garantie limitée obtenons-nous ?* Le récit du lecteur devient une soumission réfutable ; il ne devient ni la vérité terrain ni une garantie de contrôle.

FIN-DE-CELLULE