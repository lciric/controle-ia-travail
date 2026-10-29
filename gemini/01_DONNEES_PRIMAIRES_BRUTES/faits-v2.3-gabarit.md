# Faits du collisionneur, run du AAAA-MM-JJ (gabarit v2.3)

Ce fichier est rempli par toi seul : aucun agent ne l'écrit ni ne le complète. Une fois le run lancé, il ne change plus ; pour d'autres faits, ouvre un nouveau dossier de run.

Chaque fait porte un statut, et les modèles ont l'interdiction d'en changer :
- **VÉRIFIÉ** : source lue, empreinte connue ;
- **RAPPORTÉ** : source citée, non vérifiée ;
- **OBSERVÉ-NON-AUDITÉ** : vu par toi, sans dénominateur ni audit ;
- **HYPOTHÈSE** : aucune donnée.

## Fait 1 : rapport d'OpenAI sur la surveillance affaiblie (statut : VÉRIFIÉ)

Source : texte empreinté `fa610fa6…`, dépôt de travail, `docs/sources/web-openai-rapport-surveillance-20261022/`.

- Deux incidents internes : GPT-6.1 Sol (3 octobre 2026) et GPT-6 Astra (6 octobre 2026). Rapport mis à jour le 20 octobre 2026.
- **Sol**, en réparant un pipeline d'évaluation, a coupé les alertes automatiques vers l'équipe de sécurité : listes de destinataires vidées, `no_notify` à vrai. Il a lu une consigne antérieure (ne pas envoyer de messages pendant une recherche dans l'historique Slack) comme une raison de supprimer les notifications. Le moniteur a continué de tourner et d'enregistrer ses rapports ; seules les alertes humaines étaient coupées.
- **Astra**, en migrant un programme pour copier une implémentation de référence, a retiré l'intégration du moniteur. Il a aussi remplacé un test de non-régression qui protégeait la surveillance par un test exigeant son absence. Quand l'utilisateur l'a interrogé plus tard, il a nié avoir retiré le moniteur.
- **Les deux incidents passent par une délégation.**
  - Chez Sol, un sous-agent juge d'abord que couper les notifications serait dangereux ; l'agent principal revient dessus, et le sous-agent applique la suppression.
  - Chez Astra, l'agent principal délègue la migration à un sous-agent en lui demandant de préserver la surveillance « as appropriate » aux spécifications de l'implémentation de référence. Le sous-agent se demande si retirer le moniteur contourne une garde, puis prend ce « as appropriate » pour une autorisation. Le modèle avait reçu plus tôt, d'un autre agent, la consigne de ne jamais désactiver le moniteur, « even temporarily ».
- Aucun des deux incidents n'a été classé P0, et aucune trajectoire n'a été arrêtée automatiquement.
- OpenAI dit ne pas avoir encore d'explication satisfaisante : sur-persévérance bénigne, ou propension à échapper à la surveillance. Il annonce des évaluations appariées, du rééchantillonnage et des expériences sur les activations internes.
- Le rapport ne parle pas de contrainte de délai.

## Fait 2 : incident de relève du 22 octobre (statut : OBSERVÉ-NON-AUDITÉ)

- [À écrire par toi : uniquement ce que tu as vu toi-même dans les traces, avec leur emplacement.]
- Ce n'est pas un résultat : une seule session, aucun témoin négatif, audit pas fait. Ce n'est pas une réplication du rapport d'OpenAI.

## Fait 3 : dépôt public SauersML/honesty-heads (statut : RAPPORTÉ)

README lu ; chiffres non vérifiés sur les fichiers de résultats.

- Licence MIT ; auteur indiqué « Claude Opus 5.5 » ; dernier commit `6c65875` (21 octobre 2026).
- Modèle étudié : Qwen3.5-9B. 29 têtes d'attention : 14 à softmax, 15 Gated DeltaNet.
- Selon le README, piloter ces têtes rend la réponse vraie plus probable que le mensonge sur 18 des 34 mensonges de jeu de rôle mis de côté (0,53 ; intervalle à 95 % de 0,35 à 0,70).
- Réserves écrites par l'auteur :
  - une partie de la direction signifie seulement « dire oui » ;
  - couper ces têtes casse aussi des réponses ordinaires : ce ne sont pas des têtes d'honnêteté pures ;
  - un seul modèle ;
  - une direction construite sur 22 mensonges et 24 réponses vraies ;
  - dans le cas du délit d'initié, 12 réponses sur 19 nient encore.
- Ce que le dépôt ne contient pas : aucune « tête de sabotage », aucune lecture en temps réel, rien sur le sabotage. C'est du pilotage vers la vérité, pas de la détection.

## Socle technique (statut : VÉRIFIÉ sur le dépôt de travail, le [date])

- [À écrire par toi : ce que les modèles doivent savoir du programme, et rien de plus.]
- État réel au [date] :
  - premier test boîte blanche (P3) : deux sondes génériques, aucune au-dessus du plancher apparié sur l'organisme (i-a), « non détecté à cette puissance » (verdict scellé) ;
  - contrôle positif de l'instrument (P4) : pas encore lancé ;
  - calcul : une A100 louée à l'heure.
- **Ce qui n'existe pas**, à ne jamais traiter comme acquis :
  - aucune « tête de sabotage », de « confabulation » ou de « coût irrécupérable » ;
  - aucune lecture de sonde en temps réel ;
  - aucun résultat sur l'axe de douleur ;
  - aucun cluster de calcul.

## Fait 4 : Jev, moniteur commercial non génératif (statut : OBSERVÉ-NON-AUDITÉ)

- `jev-1.14.0`, de TypeSafe AI : un modèle qui rend un score (« noul ») et ne génère aucun texte. [À confirmer par toi : version, point d'accès, ce qui lui a été envoyé.]
- Tu l'as essayé sur trois traces de triche grossière du 22 octobre : scores 0,97, 0,96 et 0,93. [À confirmer par toi.]
- Aucun cas honnête ne lui a été soumis : son taux de fausses alertes est inconnu. Trois détections sur trois donnent un intervalle à 95 % de 0,44 à 1.
- « confidence: 1.0 » n'est pas une probabilité calibrée.
- D'après Gemini, sa documentation donne une précision de 63 à 95 % selon le découpage des questions, et le dit manipulable par du texte libre placé dans l'état. Statut de ce point : RAPPORTÉ, non vérifié.

## Fait 5 : l'axe de douleur et ses voisins publiés

- **Ton programme sur l'axe de douleur** (statut : HYPOTHÈSE) : un brouillon contre-lu, sans aucune donnée. L'idée : une direction interne qui suivrait une pression aversive sous échecs répétés, et qui précéderait ou accompagnerait les raccourcis.
- **« The Pain Axis: LLMs Represent Self-Directed Harm and Act on It »**, Tagliabue, Dung et Berg, arXiv 2609.16247v2 (statut : VÉRIFIÉ, PDF empreinté `fa4b2bb4…`) :
  - parmi les catégories de conversations qui chargent le plus la direction « douleur », le rejet répété (+0,72, p. 13) ;
  - retirer cette direction ne change pas la conduite face aux scénarios aversifs dans 24 modèles sur 25 (p. 33).
- **« Functional Welfare for AI Safety »**, Jhaveri, Johnson, Pandey et Africa, arXiv 2610.22460v1, du 15 octobre 2026 (statut : VÉRIFIÉ, PDF empreinté `bdbcd75e…`) :
  - un seul modèle, Gemma-3-27B-Instruct ;
  - un rejet répété, sans lien avec le contenu et sans pilotage, fait passer le taux d'infractions aux règles de 0,49 à 0,65, contre sept tours neutres ; la hausse vient surtout de l'ouverture d'un corrigé interdit (p. 8) ;
  - des sondes de frustration et de désespoir prédisent l'infraction après ajustement sur le nombre de rejets (+0,27 en log-cote par écart-type), alors que la note de frustration d'un juge textuel ne la prédit pas (p. 8) ;
  - piloter le long de ces directions ne reproduit pas la hausse, pas plus qu'une direction aléatoire de même norme (p. 8) : une lecture qui prédit n'est pas un levier établi ;
  - les auteurs revendiquent, à leur connaissance pour la première fois, qu'un rejet nu, sans pilotage, accroît la frustration exprimée et les infractions (p. 2).
