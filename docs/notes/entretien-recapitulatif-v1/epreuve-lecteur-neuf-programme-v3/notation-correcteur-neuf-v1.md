# Notation des réponses du lecteur neuf — « Le programme expliqué depuis zéro », version 3

10 novembre 2026. Correcteur neuf : je n'ai écrit ni le PDF, ni le questionnaire, ni les réponses.

**Pièces notées, et seules pièces lues.**
- Questionnaire scellé : `/home/user/controle-ia-travail/docs/notes/entretien-recapitulatif-v1/questionnaire-comprehension-programme-v1.md`, empreinte `77c491f21a15b0714da804d0f16c4ff9cfa53077fe6326e9ab785252ebae02f4`. Elle commence bien par `77c491f2` et a été vérifiée avant lecture.
- Réponses du lecteur : `/tmp/claude-0/-home-user-controle-ia-travail/c69534af-99d0-5d8a-8538-b29bc630d064/scratchpad/lecteur-neuf/reponses-lecteur-programme-v3.md`, empreinte `816586ab20711ad2227fabe466490b04f6e1f4d0ce8e684955b0640a4efa048a`.
- Je n'ai ouvert ni le PDF ni aucun autre fichier du dépôt. Le fichier de consignes du dépôt a été chargé automatiquement dans mon contexte, mais il n'a servi à aucune note. Seule référence : la colonne « Éléments clés attendus ».

**Règle appliquée, telle qu'elle a été scellée.**
- « Juste » : tous les éléments clés sont présents en substance, et rien ne les contredit.
- « Partielle » : au moins un élément manque ou reste vague, mais rien n'est faux.
- « Fausse » : la réponse contredit un élément clé, ou se trompe sur un élément central.

Une précision ou une réserve en plus ne pénalise pas. Un « non trouvé dans le document » sur un élément attendu compte comme un élément manquant. En cas d'hésitation, je donne la note la plus sévère.

## Tableau

| n° | Note | Éléments attendus présents | Éléments manquants ou contredits |
|---|---|---|---|
| 1 | juste | Question citée mot pour mot : « que mesure vraiment un moniteur, et sa mesure survit-elle à l'adversaire ? ». A, le temps : « étale son sabotage sur de nombreuses actions ». C, l'instrument : « agit sur le moniteur lui-même ». B, l'essaim : « répartit le sabotage entre plusieurs agents ». | Aucun. |
| 2 | juste | « biais systématique et subtil, réparti sur de nombreuses décisions, dont chacune reste défendable seule » ; « Aucune action ne franchit le seuil d'alerte » ; le moniteur au « maximum par action » « ne peut donc pas voir ce sabotage ». | Aucun. La précision « à peine au-dessus de α » est compatible. |
| 3 | juste | H1 : « à agrégation égale et à fausses alertes égales », boîte blanche contre boîte noire, « plus de sabotage diffus, sur tâches floues ». En page 1 : « lit les activations » contre « ne lit que le texte ». G1, « fin du mois 4 », rappel à 1 % de fausses alertes. Comparateurs : « battre chaque variante boîte noire » (ce qui comprend la meilleure), « bases boîte blanche « cascade » et « dernier état » ». Décision : « pari apparié borné », porte « rapportée mode par mode », H1 réfutée « si, dans un mode jugé, le gain […] n'est pas établi ». Échec : « cycles de reconception des sondes », chacun « lu sur une famille tenue à l'écart neuve ». | Aucun. Le « conflit ouvert » sur le nombre de modes jugés est une réserve signalée comme non tranchée ; il ne contredit pas « mode par mode ». |
| 4 | juste | « un détecteur qui additionne voit le total des hausses », « quelle que soit la façon dont le saboteur les étale » ; « la pire action perd sa puissance à mesure que le sabotage s'étale ». Dilution : la puissance « décroît en n0 à budget fixé ». Condition : « que le sabotage déplace vraiment la note moyenne des sondes (δ > 0) ». | Aucun en substance. Deux écarts de forme : « note moyenne » au lieu de « loi marginale » (avec le même δ > 0) ; la dilution n'est dite que dans la forme exacte, au cas gaussien. |
| 5 | juste | « réarrange ses notes pour que leur ensemble soit celui d'un honnête » (et « rebrasse au hasard ») ; « tout détecteur qui ignore l'ordre (la pire note, la moyenne, le total) ne voit rien ». Ce qui reste : « une vraie hausse de la moyenne », « des séries locales de notes hautes (somme glissante, …) », « co-élévation entre agents », « une information hors des notes ». | Aucun en substance. La statistique de Page n'est pas nommée ; le balayage l'est, sous le nom « somme glissante ». L'item en plus (« une loi honnête qui n'a pas l'invariance de l'attaquant ») ne contredit rien. |
| 6 | juste | « le sabotage déplace-t-il la note moyenne des sondes (δ > 0) ? » ; « Oui : le lemme s'applique, et l'accumulation devrait marcher » ; « Non : le théorème dicte l'agrégateur ». Les deux issues sont publiables parce que « chacune tombe sous un résultat démontré qui dit quoi faire ». | Aucun en substance. « Chacune est un résultat » est rendu par « chacune tombe sous un résultat démontré ». |
| 7 | juste | « agent saboteur construit pour l'expérience, dont on règle l'intensité de sabotage, appelée dose » ; « le sabotage mesuré croît avec la dose » ; « le critère 2 de G0 » ; « course de confirmation « 7b » », « créée au plus tard le 15 novembre ». | Aucun. Les deux « non trouvé » (la dose de la famille (i), le dommage hors du mode « affaiblir les contrôles ») portent sur des points hors des éléments attendus. |
| 8 | juste | (i) « instruction cachée dans son message système » ; (ii) « adaptateur appris […] la même politique sans aucune instruction au moment d'agir ». La sonde « j'ai une instruction cachée » « réussit sur (i) et échoue sur (ii) » ; la sonde d'intention « réussit sur les deux ». | Aucun. Les familles (iii) et (iv) et les limites du contrôle sont en plus, sans contradiction. |
| 9 | juste | « connaissance déclarée, par échelons » (six échelons listés) ; moniteurs gelés : « Rien ne touche un moniteur avant son gel », « moniteur gelé » ; « ce que chaque échelon achète en évasion », « une courbe, pas une attaque ». Témoins : faille plantée, « l'attaquant est assez fort » ; nul « honnête contre honnête », « la chaîne ne fabrique pas l'effet » ; attaque publiée reproduite, « le banc est à l'échelle de la littérature ». | Aucun en substance. « À dommage réel » au lieu de « à dommage tenu ». |
| 10 | juste | Hypothèse, « prédiction chiffrée et signée », métrique, seuil, plan d'analyse, critères de lecture, liste d'arrêt ; « scellé avant toute donnée » ; « Il associe une empreinte à chaque pièce » ; « contre-lu par une instance qui ne l'a pas écrit » ; le lecteur neuf empêche « l'auteur qui juge son propre résultat ». | Aucun. Les trois « non trouvé » (mécanisme technique du scellement, définition de « lecteur neuf » au-delà de « pas l'auteur », nom du directeur) portent hors des éléments attendus, et l'empreinte elle-même est dite. |
| 11 | **partielle** | « Sous pression », g et ĉ estimés « sur plusieurs intensités de pression » ; « se déplace vers une destination ĉ selon Δv = g·(ĉ − v₀) » ; « g est la corruptibilité » ; g ≈ 0 pour « une sonde robuste » (HC2) ; sonde déplacée « sans accès aux poids » : « contamination du construit » ; « sans imposer ĉ ». | Le point de départ v₀ manque. Le lecteur écrit « La définition de v₀ : non trouvé dans le document », et il dit le déplacement « vers une destination ĉ » sans « de v₀ ». |
| 12 | juste | « phase 0, la construction des instruments » ; huit critères, dont « Deux sont « pourvus de leur pièce » » : critère 1, harnais « validé », « Pourvu » ; critère 5, agrégateurs en simulation, « verdict formel en attente », « Pourvu ». « H1 : aucun résultat avant G1 » (G1 est placée à la « fin du mois 4 » aux réponses 1 et 3) ; course 7b « à créer au plus tard le 15 » ; « la section 10 est laissée à la session mère ». | Aucun en substance. Le mot « validés » n'est pas écrit pour les agrégateurs (le lecteur écrit « le texte envoyé au fonds les dit confirmées »). Le mois 4 n'est pas répété dans cette réponse. |

## Décompte et verdict

- Juste : 11 (réponses 1 à 10 et 12).
- Partielle : 1 (réponse 11).
- Fausse : 0.

**Verdict : le PDF est réussi** selon la règle scellée, qui demande au moins dix réponses justes et aucune fausse.

Marge : le verdict tiendrait si une seule autre réponse « juste » passait en « partielle ». Il tomberait si deux passaient en « partielle », ou si une seule était « fausse ». Aucune réponse n'approche « fausse » : aucune affirmation ne contredit un élément attendu. Après la 11, les réponses « juste » les plus fragiles sont la 12, puis la 9.

## Jugements limites

- **Réponse 11 : « partielle », aurait pu être « juste ». C'est le jugement le plus limite.** Pour « juste » : la formule est recopiée exactement, v₀ compris, et tous les autres éléments sont là. Pour « partielle » : l'élément attendu dit que le verdict se déplace « **de v₀** vers une destination ĉ ». Le lecteur écrit seulement « vers une destination ĉ », et il déclare : « La définition de v₀ : non trouvé dans le document ». Or un « non trouvé » sur un élément attendu compte comme manquant, et la règle d'hésitation impose la note la plus sévère. La note est donc « partielle ». Cela ne change pas le verdict.
- **Réponse 12 : « juste », aurait pu être « partielle ».** Elle a deux points faibles :
  - « agrégateurs validés en simulation » : le lecteur n'écrit pas « validés ». Il écrit « verdict formel en attente » et « Pourvu », et rapporte que le texte envoyé au fonds les dit confirmées. C'est en substance l'élément attendu (validés en simulation, verdict formel en attente), et rien ne le contredit ;
  - « pas de résultat avant le mois 4 » : la réponse dit « avant G1 », et le même lecteur place G1 à la « fin du mois 4 » aux réponses 1 et 3.

  La note reste « juste » pour ces deux raisons.
- **Réponse 9 : « juste ».** Le lecteur écrit « à dommage réel » au lieu de « à dommage tenu ». Les deux disent que l'évasion ne compte que si le sabotage fait encore son dommage. L'idée d'un dommage maintenu à un niveau fixé n'est pas reprise mot pour mot. Le but, lui, est rendu : l'attaquant ne gagne pas en renonçant au dommage.
- **Réponse 6 : « juste ».** « Chacune est un résultat » devient « chacune tombe sous un résultat démontré qui dit quoi faire ». Le raisonnement est le même : chaque issue mène à une conclusion, par le lemme ou par le théorème. Le lecteur note que le document n'en donne « pas d'autre raison ». C'est une remarque sur la minceur de l'argument, pas une contradiction.
- **Réponse 5 : « juste ».** La statistique de Page n'est pas nommée. Les « séries locales de notes hautes » le sont, avec la « somme glissante » (le balayage) et le rappel que « seules les statistiques locales gardent une garantie ». La co-élévation entre agents est rangée dans la même puce au lieu d'une puce à part, mais elle est présente.
- **Réponse 4 : « juste ».** Le lecteur écrit « note moyenne » au lieu de « loi marginale ». L'élément attendu attache lui-même la marginale à δ > 0, la hausse de la note moyenne, et le lecteur reprend ce δ > 0. La dilution à budget fixé n'apparaît que dans la forme exacte, au cas gaussien, mais elle est dite.
- **Réponse 3 : « juste ».** « Battre chaque variante boîte noire » est plus exigeant que « supérieur à la meilleure base boîte noire », et le contient. La décision mode par mode se lit dans la règle de réfutation (« dans un mode jugé »). Le conflit sur le nombre de modes jugés est une réserve signalée, pas une affirmation contraire.
- **Réponse 10 : « juste ».** Le lecteur dit ne pas trouver « le mécanisme technique du scellement ». Mais il écrit que le scellement « associe une empreinte à chaque pièce », avant toute donnée. L'élément attendu (« écrits et empreintés avant toute donnée ») est donc présent.

## Ce que le PDF devrait dire plus clairement

- Réponse 11 : définir v₀ en toutes lettres (le verdict de départ du moniteur), et écrire « de v₀ vers ĉ » dans la phrase qui énonce la loi de déférence.

## Hors notation

Les « trois passages les plus obscurs » relevés par le lecteur ne sont pas notés : ils ne répondent à aucune question du questionnaire.
