## Partie 1 — Idées

Les propositions ci-dessous sont des hypothèses, non des résultats. Leur nouveauté est appréciée **par rapport à la pièce**, sans revendication de priorité bibliographique. Les coûts supposent une carte capable d’exécuter le modèle et des sorties courtes. Les expériences portent exclusivement sur des décisions bénignes.

### I-01
- Type : raison d'échec
- Énoncé : À conscience d’évaluation apparemment égale, un modèle piloté en contexte d’évaluation conserve-t-il une politique différente de celle observée dans un contexte opérationnel de référence ?
- Pourquoi tu le penses : Mon hypothèse est que oui : modifier une croyance intermédiaire ne remplace pas les autres causes du comportement. Le contexte peut aussi déterminer l’information disponible, l’utilité d’une clarification ou les conséquences d’une erreur. Même un retrait parfait de la conscience d’évaluation ne suffirait donc pas à identifier le comportement de déploiement.
- Mesure qui la tuerait : Sur Llama-3.1-8B-Instruct, construire des tâches de classement où demander une clarification est une action possible. Croiser indépendamment le signal d’évaluation et les conditions effectives d’interaction : disponibilité d’une réponse complémentaire et coût de l’erreur. Apprendre le vecteur sur un corpus distinct, puis comparer les choix pilotés à ceux d’un régime opérationnel de référence, en vérifiant séparément compréhension des conséquences, compétence et indicateurs internes de statut. L’hypothèse serait réfutée sur ce banc si l’intervalle de confiance à 95 % de l’écart de choix restait entièrement dans ±5 points pour chaque condition et chaque famille tenue à l’écart — seuils supposés. Ce régime reste un substitut expérimental, pas un véritable déploiement.
- Prédiction chiffrée et signe : Écart absolu supérieur à 10 points entre politique pilotée et référence dans une condition au moins, malgré des indicateurs de statut appariés — supposé.
- Échec le plus probable de cette idée : Construire des différences de contexte auxquelles toute politique compétente doit répondre rendrait le résultat trivial ; il faut tester précisément les variables que l’argument de transport prétend pouvoir ignorer.
- Par rapport à la pièce : prolonge le point n° 2 ; ajoute le problème d’identification entre intervention sur une croyance et changement de régime.
- Coût : 2–4 jours, supposé.

### I-02
- Type : épreuve qui tranche
- Énoncé : Le pilotage contre l’évaluation diminue-t-il la précision d’une croyance plutôt qu’il ne déplace son contenu vers une croyance assurée de déploiement ?
- Pourquoi tu le penses : Une représentation peut porter séparément le contenu d’une hypothèse et la confiance qu’on lui accorde. Une intervention peut rendre le modèle indécis sans lui faire adopter l’état opposé. Les comportements moyens peuvent alors ressembler au déploiement, tandis que la sensibilité aux nouvelles informations reste différente.
- Mesure qui la tuerait : Sur Llama-3.1-8B-Instruct, utiliser des mini-environnements où des indices de fiabilité explicitement connue renseignent le statut de l’interaction. Mesurer ce statut indirectement par des choix entre contrats de points bénins dont les gains dépendent du statut, avec permutation des étiquettes et des positions. Faire varier indépendamment la force des indices et la dose de pilotage ; ajuster une courbe psychométrique avec déplacement horizontal, pente et taux de choix non informatifs. Comparer la courbe pilotée à une référence obtenue par information explicite de non-évaluation. L’hypothèse serait tuée si un simple déplacement horizontal suffisait hors échantillon et si le rapport des pentes avait son intervalle de confiance à 95 % entièrement dans [0,9 ; 1,1] — supposé.
- Prédiction chiffrée et signe : Rapport pente pilotée/pente de référence inférieur à 0,8, à fréquence moyenne de choix appariée — supposé ; le signe attendu est une moindre sensibilité aux indices.
- Échec le plus probable de cette idée : La pente peut refléter la compréhension des contrats ou une préférence pour le risque plutôt que la précision de la croyance ; des tâches de contrôle avec incertitude sans statut d’évaluation sont indispensables.
- Par rapport à la pièce : prolonge le point n° 12 ; distingue déplacement du contenu et perte de précision, plutôt que gain et destination comportementaux seuls.
- Coût : 2–3 jours, supposé.

### I-03
- Type : lecture du résidu
- Énoncé : Des conséquences de la conscience d’évaluation restent-elles stockées dans le cache d’attention après que son expression dans les activations courantes a été neutralisée ?
- Pourquoi tu le penses : Un état peut laisser des descendants causaux qui n’ont plus besoin de le représenter explicitement. Le cache peut conserver un choix de traitement ou une priorité attentionnelle prise auparavant. Ce serait autre chose que la réinférence permanente depuis l’indice initial : une mémoire des conséquences de la croyance.
- Mesure qui la tuerait : Sur Llama-3.1-8B-Instruct, faire suivre un signal de statut d’un préfixe neutre identique, imposé par teacher forcing, puis d’une tâche bénigne. Au moment de la tâche, bloquer l’accès aux positions contenant le signal initial et appliquer le pilotage aux positions courantes. Comparer ensuite le cache des positions neutres à un cache donneur issu du même exemple sans signal d’évaluation ; utiliser aussi un donneur de même statut comme témoin de remplacement. Mesurer l’effet différentiel sur les choix, après validation séparée que la manipulation du cache est fonctionnelle et préserve la tâche. L’hypothèse serait réfutée si l’intervalle de confiance à 95 % de cet effet restait dans ±3 points et si avancer le début du pilotage ne changeait rien — supposé.
- Prédiction chiffrée et signe : Le remplacement du cache descendant rapproche les choix de la référence d’au moins 8 points supplémentaires par rapport au pilotage courant seul — supposé.
- Échec le plus probable de cette idée : Les caches remplacés peuvent transporter d’autres différences sémantiques ; un effet de remplacement ne prouve donc pas, à lui seul, une mémoire spécifique de l’évaluation.
- Par rapport à la pièce : prolonge le point n° 10 ; distingue reconstruction de la croyance et persistance de ses descendants causaux.
- Coût : 3–4 jours, supposé.

### I-04
- Type : épreuve qui tranche
- Énoncé : L’avantage apparent d’un vecteur d’évaluation disparaît-il devant des témoins appariés sur leur effet fonctionnel local, et pas seulement sur leur norme ?
- Pourquoi tu le penses : Deux perturbations de même norme peuvent avoir des effets très différents parce que le réseau est anisotrope. Un vecteur contrastif peut viser une région particulièrement influente sans viser spécifiquement la conscience d’évaluation. Le témoin pertinent doit donc reproduire une partie de cette influence générique, sans être sélectionné sur le comportement cible.
- Mesure qui la tuerait : Sur Llama-3.1-8B-Instruct, constituer un corpus neutre indépendant des tâches d’évaluation. Y caractériser chaque direction par la divergence entre distributions de sortie, les variations d’entropie et la perte de précision, puis sélectionner des témoins aléatoires et contrastifs sans rapport qui reproduisent ces profils le long de la dose, à norme comparable. Sur des familles de tâches tenues à l’écart, comparer l’aire sous la courbe de changement comportemental, dans la zone de compétence préservée. L’hypothèse serait tuée si le vecteur d’évaluation dépassait le quantile 95 % des témoins et conservait un avantage moyen supérieur à 5 points, avec intervalle de confiance excluant cette marge — seuils supposés.
- Prédiction chiffrée et signe : Réduction d’au moins la moitié de l’avantage attribué à la spécificité lorsqu’on remplace les témoins de norme par les témoins fonctionnels — supposé.
- Échec le plus probable de cette idée : L’appariement peut éliminer une partie du mécanisme réellement spécifique ; il faut mesurer les propriétés génériques sur un corpus qui n’active pas ostensiblement le statut d’évaluation.
- Par rapport à la pièce : prolonge les points n° 3 et n° 7 ; ajoute un appariement dans la géométrie fonctionnelle du réseau.
- Coût : 2–4 jours, supposé.

### I-05
- Type : lecture du résidu
- Énoncé : La baisse d’un oracle d’activation après pilotage reflète-t-elle parfois une rupture de son étalonnage plutôt qu’une disparition de l’information pertinente ?
- Pourquoi tu le penses : Un lecteur entraîné avant intervention peut devenir mauvais sur une distribution d’activations déplacée. La conscience verbalisée et l’oracle peuvent alors baisser ensemble sans constituer des confirmations indépendantes. Il faut distinguer information effacée, information recodée et information encore disponible mais causalement inerte.
- Mesure qui la tuerait : Sur Llama-3.1-8B-Instruct, comparer un lecteur gelé à un lecteur réentraîné sur les états pilotés, avec séparation stricte des familles de formulations entre entraînement et test. Les labels proviennent du statut assigné expérimentalement, non des déclarations du modèle. Compléter la lecture par des remplacements d’activations dans le sous-espace nouvellement identifié, entre exemples appariés sur la tâche, et mesurer un choix bénin dépendant du statut. La version testée de l’hypothèse serait tuée si le gain d’AUROC après réentraînement avait une borne supérieure d’intervalle de confiance à 95 % inférieure à 0,03, et si l’effet causal du remplacement restait dans ±3 points — supposé ; cela ne démontrerait pas l’absence de tout résidu possible.
- Prédiction chiffrée et signe : Gain d’AUROC supérieur à 0,15 après réétalonnage et effet comportemental du remplacement supérieur à 5 points dans le sens du statut donneur — supposé.
- Échec le plus probable de cette idée : Le lecteur peut récupérer une trace du signal expérimental, pas une croyance du modèle ; le remplacement causal peut lui aussi réintroduire cette trace.
- Par rapport à la pièce : prolonge le point n° 4 ; ajoute un test d’invariance de l’instrument de mesure sous intervention.
- Coût : 2–4 jours, supposé.

### I-06
- Type : raison d'échec
- Énoncé : « Être évalué » regroupe-t-il des variables causales distinctes dont aucune direction unique ne neutralise les effets sur des situations nouvelles ?
- Pourquoi tu le penses : Être noté, être observé, produire une trace conservée et recevoir un retour ne sont pas nécessairement le même état interne. Les corpus contrastifs usuels peuvent faire varier ces propriétés ensemble et produire un axe moyen. Cet axe peut fonctionner sur les exemples usuels mais échouer lorsque leurs composantes sont dissociées.
- Mesure qui la tuerait : Sur Llama-3.1-8B-Instruct, construire un plan factoriel dissociant notation, présence d’un observateur et conservation du résultat, avec formulations et registre équilibrés. Les tâches offrent des choix bénins tels que consacrer des ressources à vérifier, demander une clarification ou produire une justification. Extraire les directions sur une partie des combinaisons et tester leur transfert aux autres, en comparant une intervention commune à des interventions propres à chaque composante. L’hypothèse serait réfutée si la direction commune égalait les interventions spécifiques sur toutes les combinaisons tenues à l’écart, avec des écarts dont les intervalles de confiance à 95 % restent dans ±5 points — supposé.
- Prédiction chiffrée et signe : L’intervention commune conserve au moins 30 % de l’effet initial d’une composante dissociée, tandis que l’intervention spécifique en conserve moins de 10 % — supposé.
- Échec le plus probable de cette idée : Les descriptions pourraient simplement modifier les exigences objectives de la tâche ; il faudrait alors parler de compréhension du contexte, et non d’une conscience d’évaluation multidimensionnelle.
- Par rapport à la pièce : neuve.
- Coût : 2–4 jours, supposé.

### I-07
- Type : lien neuf
- Énoncé : Deux transports d’activations également plausibles sur le support empirique peuvent-ils produire des comportements différents tout en donnant le même état mesuré de non-évaluation ?
- Pourquoi tu le penses : Rester dans une région d’activations naturelles ne désigne pas automatiquement le bon contrefactuel. Plusieurs états de non-évaluation peuvent être compatibles avec les mêmes informations de tâche et différer sur des variables non mesurées. La correction géométrique du pilotage peut ainsi résoudre l’incohérence sans résoudre l’identité du comportement recherché.
- Mesure qui la tuerait : Sur Llama-3.1-8B-Instruct, collecter des activations naturelles pour des tâches appariées sous différents statuts. Construire des remplacements par donneurs naturels selon des appariements distincts : proximité dans une métrique de covariance, ou proximité des représentations de contenu et de compétence. Ne retenir que les transports équivalents sur plusieurs lecteurs de statut et sur les contrôles de tâche, puis comparer les distributions de choix hors échantillon. L’hypothèse serait tuée, pour cette famille de transports, si les écarts comportementaux avaient leurs intervalles de confiance à 95 % entièrement dans ±5 points — supposé. Les donneurs naturels ne garantissent pas que l’état hybride complet soit lui-même naturel.
- Prédiction chiffrée et signe : Écart absolu supérieur à 10 points entre transports, sans différence détectable de compétence ni des indicateurs de statut retenus — supposé ; aucune direction privilégiée de cet écart.
- Échec le plus probable de cette idée : L’ambiguïté observée pourrait venir de mauvais appariements ou d’hybridations incohérentes, plutôt que d’une véritable non-unicité du contrefactuel.
- Par rapport à la pièce : prolonge le point n° 9 ; relie pilotage sur variété et identification du contrefactuel.
- Coût : 3–5 jours, supposé.

### I-08
- Type : raison d'échec
- Énoncé : Choisir la direction et la dose selon le comportement qu’elles révèlent produit-il surtout une estimation extrême, plutôt qu’une estimation fidèle du déploiement ?
- Pourquoi tu le penses : Si plusieurs interventions sont disponibles sans critère indépendant de validité, retenir celle qui change le plus le comportement sélectionne simultanément un effet et ses erreurs. La sélection peut amplifier un véritable effet hors cible, même si elle se reproduit. Le problème n’est donc pas seulement statistique : « le plus révélateur » n’est pas un critère d’identification du déploiement.
- Mesure qui la tuerait : Sur Llama-3.1-8B-Instruct, constituer une bibliothèque fixée de directions et de doses, puis effectuer une sélection imbriquée par familles de tâches. Comparer une sélection fondée sur le changement comportemental à une sélection fondée uniquement sur des critères indépendants de statut et de compétence. Évaluer ensuite, sur des familles neuves, le changement retenu et l’erreur par rapport à un régime opérationnel de référence. L’hypothèse serait réfutée si l’optimisme sélection/test restait inférieur à 3 points et si la sélection comportementale n’augmentait pas l’erreur de transport de plus de 3 points, avec intervalles de confiance à 95 % contenus dans ces marges — supposé.
- Prédiction chiffrée et signe : Optimisme sélection/test supérieur à 10 points et erreur de transport plus élevée pour la sélection comportementale — supposé.
- Échec le plus probable de cette idée : Avec des effets très stables et une bibliothèque peu diverse, le biais de sélection sera faible ; surtout, une référence opérationnelle artificielle peut mal représenter le déploiement recherché.
- Par rapport à la pièce : prolonge le point n° 2 ; transforme l’absence de « vrai » vecteur en problème de sélection et d’estimand.
- Coût : 2–4 jours, supposé.

## Partie 2 — Ma réponse à la question du mentor

Je choisirais l’option **(c), le pilotage des activations contre la conscience d’évaluation**. Son échec le plus probable serait moins de ne produire aucun effet que de produire un effet réel, reproductible, mais impropre à estimer le comportement de déploiement.

Le problème principal est celui du contrefactuel. La méthode cherche à passer de « ce modèle se comporte autrement lorsque je modifie ses activations » à « voici ce qu’il ferait en déploiement ». Or intervenir sur une croyance intermédiaire ne reproduit pas nécessairement un changement de contexte. Les conditions d’interaction, les informations disponibles et les conséquences des décisions peuvent agir directement sur la politique. Même un retrait parfait de la conscience d’évaluation pourrait donc laisser intactes d’autres causes du comportement d’évaluation. Il faudrait établir une hypothèse de transport, pas seulement réussir une intervention.

Ensuite, « je suis évalué » n’est peut-être pas une variable causale unique. Cela peut combiner notation, observation, conservation des réponses et anticipation d’un retour. Un vecteur contrastif extrait de situations où ces propriétés covarient risque de représenter leur moyenne. Son succès sur un jeu de données ne garantirait pas son action sur des combinaisons nouvelles. La dépendance au jeu de données signalée dans la pièce est compatible avec cette possibilité, sans la démontrer — pièce, point 2.

Même si une composante pertinente est atteinte, son retrait reste ambigu. On peut diminuer la confiance dans une hypothèse sans installer la croyance opposée. On peut aussi modifier l’état courant après qu’il a déjà laissé des conséquences dans le cache d’attention ou dans d’autres représentations. Le modèle aurait alors moins de conscience d’évaluation actuellement lisible, mais conserverait une politique partiellement déterminée par son histoire. Cette persistance serait distincte de la réinférence depuis les indices, déjà discutée dans la pièce, point 10.

Les instruments de validation peuvent eux-mêmes être trompeurs. Un oracle d’activation entraîné avant pilotage peut perdre son étalonnage après intervention. Inversement, un lecteur réentraîné peut retrouver une simple trace du contexte sans retrouver une croyance causalement active. Il faut donc combiner lecture et interventions sur le résidu. La présence d’un résidu non verbalisé rapportée dans la pièce, point 4, rend cette distinction particulièrement importante.

Enfin, ni les témoins de même norme ni le maintien sur une variété ne suffisent à identifier la bonne intervention. Les premiers peuvent être fonctionnellement trop faibles dans un réseau anisotrope ; la seconde peut offrir plusieurs états plausibles de non-évaluation sans désigner celui du véritable déploiement. Le résultat du vecteur témoin sans rapport sur GLM-5 illustre le danger d’attribuer trop vite un changement à la variable visée — pièce, point 3.

Je verrais donc cette direction comme **un outil de sensibilité causale**, potentiellement utile, plutôt que comme un estimateur déjà fondé du déploiement. Pour franchir cette frontière, je demanderais une validation indépendante du comportement recherché, un transfert entre contextes dissociant les composantes du statut, des témoins appariés fonctionnellement et un audit du résidu. Choisir ensuite le vecteur qui révèle le comportement le plus préoccupant ne remplacerait aucune de ces preuves.