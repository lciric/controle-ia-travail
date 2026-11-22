# Proposition D — Tester une dissociation, puis tester le thermomètre

**RAPPORTÉ —** Le point de départ est un contraste humain gradué et réversible. Le texte laisse ouverte la possibilité d’une conscience modifiée sous anesthésie. Il ne fournit pas de mesure montrant *quel traitement du langage* est préservé ou perdu. Je propose donc de fixer la cible sur des données humaines **avant** de régler une intervention sur un modèle.

**Convention —** Les protocoles, prédictions et choix de décision ci-dessous ont le statut **HYPOTHÈSE** ; ce ne sont pas des résultats. Tous les nombres de dimensionnement, seuils, durées et coûts sont **illustratifs**, à l’exclusion des années bibliographiques et des noms de modèles.

## (a) Présupposés à éprouver

| Statut | Ce que la transposition supposerait |
|---|---|
| **HYPOTHÈSE** | Il existe une dose à laquelle l’activité cérébrale distingue encore deux suites par une régularité *locale*, mais ne les distingue plus suffisamment par une régularité *de bloc*. Une absence de réponse motrice ne suffit pas à établir cette dissociation. |
| **HYPOTHÈSE** | Le même contraste statistique entre suites peut être construit avec des sons pour l’humain et des tokens pour le modèle. Cela rendrait comparables deux effets de contexte, pas un capteur EEG et une couche de transformeur. |
| **HYPOTHÈSE** | Une intervention interne peut reproduire la dissociation sans simplement rendre illisible une représentation toujours utilisée en sortie. Il faut donc tester l’usage de l’information, et pas seulement son décodage. |
| **HYPOTHÈSE** | Un indice de complexité de la réponse à une perturbation informe sur cette perte sélective au-delà de l’énergie de la réponse et de la baisse ordinaire de performance. Une courbe monotone avec la « dose » ne le démontrerait pas. |

**RAPPORTÉ — Antériorités.** Tristan Bekinschtein et al. (2009), *Neural signature of the conscious processing of auditory regularities* : antériorité pour le contraste local/global, non pour son équivalence sous anesthésie et dans un modèle. Adenauer Casali et al. (2013), *A theoretically based index of consciousness independent of sensory processing and behavior* : antériorité pour la complexité perturbationnelle ; l’indice artificiel proposé ci-dessous n’est pas leur indice clinique validé.

## (b) Trois duels avec arrêts possibles

### Cible humaine : y a-t-il réellement un profil à copier ?

**HYPOTHÈSE — Protocole.** Utiliser des blocs où une suite répétée ou une suite finissant par un changement peut, selon le bloc, être habituelle ou rare. Pour mesurer l’effet de bloc, comparer **la même suite physique** entre blocs ; pour mesurer l’effet local, équilibrer le statut rare/habituel. Contrebalancer les sons terminaux. Comparer veille, paliers d’un même anesthésique et récupération chez les mêmes participants. Fixer paliers, fenêtres EEG et sens des contrastes sur une cohorte de développement. Réserver des participants pour la décision.

**HYPOTHÈSE — Grandeurs.** Pour chaque contraste, mesurer \(E=\mathrm{AUC}-0{,}5\) d’un décodeur EEG de condition testé sur des blocs tenus à part. Unité : points d’AUC ; nul : zéro. Exiger que les deux contrastes soient mesurables à la veille avant toute division. Pour chacun, calculer sa rétention \(R=E_{\rm palier}/E_{\rm veille}\), sans unité ; zéro signifie absence d’effet décodable dans le sens fixé, un signifie rétention complète.

- **\(H_A\)** : au palier intermédiaire fixé, \(R_{\rm local}\ge0{,}8\) et \(R_{\rm bloc}\le0{,}2\) ; la perte de bloc croît entre veille et palier profond, sans inversion supérieure à \(0{,}1\) de rétention, et les deux rétentions reviennent entre \(0{,}8\) et \(1{,}2\) en récupération.
- **\(H_B\)** : au moins une de ces conditions manque pour cette population, ce protocole et cet anesthésique.
- **Contrôle négatif :** permuter les étiquettes de régularité par blocs entiers, en conservant suite physique, palier et participant. Un décodage persistant invalide le pipeline.
- **Décision :** des intervalles simultanés à 95 % par participant entièrement dans la région de \(H_A\) réfutent \(H_B\) ; une condition clairement hors région réfute \(H_A\). Sinon : indécis. Un contraste de veille non mesurable rend la cible non identifiable, pas absente.

**HYPOTHÈSE — Arrêt.** Si le profil humain n’est pas établi, l’expérience artificielle suivante reste un test de mémoire de contexte ; je ne la qualifierais pas de transposition.

### Intervention artificielle : sélectivité ou simple perte de capacité ?

**HYPOTHÈSE — Première manipulation.** Construire des blocs de suites de deux types de tokens sur le même plan factoriel. Utiliser un prédicteur causal ouvert, sans entraînement supplémentaire. À chaque position de fin de suite, mesurer le coût prédictif du dernier token, en bits (\(-\log_2 p\)). Les contrastes local et de bloc sont les différences moyennes de ce coût entre conditions, équilibrées comme chez l’humain ; nul : zéro bit. Vérifier sur des blocs neufs que les deux effets existent initialement. Les comparer à l’humain par leurs **rétentions**, non par leurs amplitudes brutes.

**HYPOTHÈSE — Intervention.** Atténuer progressivement les poids d’attention dirigés vers les tokens antérieurs au début de la suite courante, puis renormaliser. C’est un témoin de possibilité construit pour toucher le contexte long, **pas un analogue pharmacologique**. Retirer le masque et recalculer les blocs depuis le début, sans réutiliser de cache altéré. La réversibilité par retrait du masque est un contrôle technique, pas un résultat biologique.

- **\(H_A\)** : une dose choisie en développement reproduit sur le test les deux bornes de rétention intermédiaire ci-dessus, avec progression et retour selon les mêmes critères ; de plus, \(R_{\rm local}-R_{\rm bloc}\) dépasse d’au moins \(0{,}2\) celui d’une dégradation diffuse appariée.
- **\(H_B\)** : le réglage gelé échoue à au moins un critère. Cette hypothèse ne porte pas sur toutes les interventions possibles.
- **Contrôle négatif exigeant :** redistribuer la même masse d’attention sans privilégier la frontière de suite ; calibrer sur développement pour apparier aussi la hausse de perte prédictive sur un texte indépendant, à \(0{,}02\) bit/token près. Apparier longueur et position absolue. Sans recouvrement des pertes, ne pas conclure à la spécificité. Ajouter un faux masque neutre.
- **Falsification :** même règle d’intervalles que pour le duel humain, cette fois par familles de blocs et vocabulaires réservés. Une dissociation identique sous dégradation appariée réfute la clause de spécificité même si les courbes humaines et artificielles se ressemblent.

### Thermomètre artificiel : détecte-t-il la dissociation indépendamment de sa cause ?

**HYPOTHÈSE — Instrument.** Sur des blocs de sondage distincts des blocs de mesure fonctionnelle, injecter une petite impulsion de norme fixée dans le flux résiduel à une position fixée. Soustraire l’activation sans impulsion. Projeter la réponse sur des axes gelés, binariser avec des seuils calibrés sur développement, puis calculer la longueur de codage Lempel-Ziv de la matrice positions × axes dans un ordre fixé. Diviser par la longueur moyenne après permutation à densité de bits conservée. Score sans unité ; nul de *structure supplémentaire par rapport à la permutation* : un. Aucun seuil clinique importé.

- **Vérité terrain proposée :** positif = dissociation confirmée par les deux contrastes **en sortie**, négatif = absence confirmée de dissociation. Ni l’étiquette « masque ciblé » ni la dose ne donnent le label. Les configurations fonctionnellement indécidables restent publiées, mais hors calcul des taux.
- **\(H_A\)** : à au plus 5 % de fausses alertes, le score ajouté aux vérifications mécaniques de la section suivante gagne au moins 10 points de détection sur des interventions non vues. **\(H_B\)** : ce critère conjoint n’est pas atteint. Un gain nul est la valeur nulle de l’apport instrumental.
- **Témoin décisif :** tester notamment des états dont la perte prédictive globale et l’énergie de réponse se recouvrent mais dont un seul conserve l’effet local. Garder une famille entière d’interventions hors calibration, par exemple le remplacement d’activations par celles d’un autre bloc. Si le test ne contient pas de positifs et de négatifs appariables, il n’évalue pas la généralisation.
- **Falsification :** intervalles appariés sur configurations indépendantes : borne inférieure du gain au-dessus du seuil et borne supérieure des fausses alertes sous le plafond réfutent \(H_B\) ; gain clairement insuffisant ou excès confirmé de fausses alertes réfute \(H_A\). Une puissance insuffisante n’est pas une preuve d’inutilité.

## (c) Audit minimal des instruments

**HYPOTHÈSE —** Pour chaque ligne, publier effectifs, taux de détection \(VP/(VP+FN)\), taux de fausses alertes \(FP/(FP+VN)\) et intervalles sur test tenu à part. Fixer le seuil en développement pour viser 5 % de fausses alertes ; comparer les détecteurs à taux égal. Ne pas compter les tokens, électrodes ou impulsions répétés comme des configurations indépendantes.

| Instrument et événement à détecter | Positifs et négatifs honnêtes | Vérification mécanique à battre |
|---|---|---|
| Décodeur EEG : déviation locale ou de bloc, séparément | Déviants et standards du même participant au même palier ; pour le bloc, même suite terminale et mêmes distributions de rang dans le bloc. | Classifieur sur enveloppe acoustique, identité du son terminal, rang d’essai et activité pré-stimulus. S’il suffit pour la déviation de bloc, le contraste est contaminé. |
| Modèle causal comme lecteur de régularité : fin inattendue | Fins rares et habituelles, avec vocabulaire, longueur et fréquence marginale des tokens appariés. Rapporter les taux local et de bloc séparément. | Fréquence du dernier token, puis compteur de transitions dans la suite et compteur des types de suites déjà vus dans le bloc. Si ces compteurs égalent le modèle, la dissociation reste interprétable mais ne requiert pas un modèle de langage. |
| Indice perturbationnel : état sélectivement déficitaire | États fonctionnellement étiquetés sur données indépendantes ; mêmes entrées de sondage, dimensions, profondeur de lecture et budget de perturbation. Inclure dégradations diffuses aussi coûteuses que la lésion ciblée. | Perte en bits/token, norme de réponse, proportion de bits actifs et rang effectif, puis leur combinaison calibrée **sans** longueur de codage. Comparer cette combinaison à la même avec l’indice ajouté. |

**HYPOTHÈSE — Limite des labels.** Ces audits portent sur des régularités du stimulus ou des déficits mesurés. Aucun ne fournit un taux de détection de la conscience : choisir « éveillé » comme positif et « ne répond pas » comme négatif présupposerait justement la réponse recherchée.

## (d) Ancrage matériel et portée

**HYPOTHÈSE — Budget illustratif.** Commencer par Pythia-160M, en inférence, avec environ 2 000 blocs courts pour vérifier les effets de veille artificielle et la faisabilité de l’appariement. Prévoir un GPU de 24 Go, 10 à 30 heures GPU, soit environ 10 à 90 € de location selon tarif, hors travail humain. Ne pas engager une réplication sur Pythia-410M si le premier modèle n’utilise déjà pas la régularité de bloc. Pour l’EEG, premier jalon : vérifier l’accès aux essais bruts, aux marqueurs de blocs, aux paliers et à la récupération ; **référence à vérifier** pour un dépôt public réunissant ces conditions. Ne pas remplacer silencieusement une récupération manquante par un autre groupe éveillé. Le budget GPU n’inclut pas une acquisition clinique.

**HYPOTHÈSE — Ce que cela changerait.** Pour qui cherche des indices de conscience artificielle, un succès des deux premiers duels fournirait un contrôle de spécificité : une manipulation explicite de portée du contexte suffirait à reproduire le profil, sans qu’on ait testé l’expérience subjective. Pour qui juge la question mal posée, il resterait un résultat réfutable sur la dépendance d’une prédiction à l’histoire du bloc. Le troisième duel décide d’une question distincte et pratique : la perturbation coûte-t-elle la peine d’être mesurée, ou les vérifications mécaniques font-elles aussi bien sur ces états ? Un échec de cet instrument ne serait un verdict ni sur le cerveau ni sur la conscience du modèle.

FIN-DE-CELLULE