# Notation des réponses du lecteur neuf — PDF « le programme depuis zéro » — v1

10 novembre 2026. Correcteur neuf : je n'ai écrit ni le PDF, ni le questionnaire, ni les réponses.

## Pièces lues, et elles seules

- Questionnaire scellé : `/home/user/controle-ia-travail/docs/notes/entretien-recapitulatif-v1/questionnaire-comprehension-programme-v1.md`, empreinte `77c491f21a15b0714da804d0f16c4ff9cfa53077fe6326e9ab785252ebae02f4` (vérifiée avant lecture : elle commence bien par `77c491f2`).
- Réponses du lecteur : `/tmp/claude-0/-home-user-controle-ia-travail/c69534af-99d0-5d8a-8538-b29bc630d064/scratchpad/lecteur-neuf/reponses-lecteur-v1.md`, empreinte `ace52192ccf79c04d2f5d18e4fa6cb4f9a8ab7c99ae4b442cf1532ee46e65cd1`.
- Ni le PDF ni son texte extrait n'ont été ouverts (une liste du dossier en a montré les noms, rien de plus). Seule référence : la colonne « Éléments clés attendus ».
- Réserve : le fichier de consignes du dépôt a été chargé automatiquement dans mon contexte ; je ne m'en suis pas servi pour noter.

Règle appliquée telle quelle : « juste » si tous les éléments attendus sont présents en substance, sans contradiction ; « partielle » si au moins un manque ou reste vague, sans rien de faux ; « fausse » si la réponse contredit un élément attendu ou se trompe sur un élément central ; un « non trouvé dans le document » compte comme manquant ; en cas d'hésitation, la note la plus sévère. Réussite scellée : au moins dix « juste » et aucune « fausse ».

## Notation

| n° | Note | Éléments attendus présents | Éléments manquants ou contredits |
|---|---|---|---|
| 1 | juste | La question (« que mesure vraiment un moniteur, et sa mesure résiste-t-elle à un adversaire ») ; temps, papier A (« étaler son sabotage dans le temps ») ; instrument, papier C (« agir sur le moniteur lui-même ») ; agents, papier B (« répartir le sabotage entre plusieurs agents »). | Aucun. |
| 2 | juste | « Biais systématique et subtil », « réparti sur de nombreuses décisions », « chacune reste défendable prise seule » ; « aucune action ne franchit le seuil d'alerte », donc le moniteur par action ne se déclenche pas. | Aucun. |
| 3 | juste | Revendication entière (agrégation égale, fausses alertes égales, activations contre « ses textes et ses actions », sabotage diffus, tâches floues) ; G1, fin du mois 4 ; rappel à 1 % contre la meilleure base boîte noire et contre « cascade » et « dernier état » ; un « pari apparié borné » décide ; porte « rapportée mode de sabotage par mode », réfutée si le gain manque « dans un mode jugé » ; en cas d'échec, « on reconçoit les sondes, puis on relit » sur « une famille de sabotage tenue à l'écart neuve ». | Aucun. Réserves du lecteur, non pénalisées : « pari apparié borné » non défini ; nombre de modes jugés en conflit (« chaque mode, mode tenu à l'écart compris » contre « deux modes jugés ») ; nombre de cycles non trouvé (hors attendu). |
| 4 | juste | Hausse de la note moyenne par action, et la somme « voit le total de ces hausses, quelle que soit la façon dont le saboteur les étale » ; « la pire action perd […] sa puissance » ; puissance de la somme qui « baisse avec l'horizon quand le budget total est fixé » ; condition : que le sabotage « déplace vraiment la note moyenne des sondes (δ > 0) ». | Aucun. « Note moyenne » au lieu de « loi marginale » : même condition δ > 0, présente en substance. |
| 5 | juste | Réarranger ou rebrasser pour que « leur ensemble soit exactement celui d'un agent honnête », et tout détecteur insensible à l'ordre (pire note, moyenne, total) « ne voit rien » ; il reste « une vraie hausse de la moyenne », « des séries locales de notes hautes » (« une somme glissante »), « la co-élévation des notes entre agents », « une information extérieure aux notes ». | Aucun. La co-élévation est nommée parmi les statistiques qui « gardent une garantie », hors de la liste finale ; « Page » n'est pas nommé dans cette réponse (exemple entre parenthèses, couvert par la somme glissante). |
| 6 | juste | Question pivot : « le sabotage fait-il monter la note moyenne des sondes (δ > 0) ? » ; oui : « le lemme d'additivité s'applique et l'accumulation […] devrait détecter » ; non : « le théorème négatif dicte l'agrégateur » ; publiables car « chacune tombe sous un résultat démontré ». | Aucun (même remarque qu'en 4 sur « moyenne » et « marginale »). |
| 7 | juste | « Agent saboteur construit pour l'expérience », intensité réglable « appelée la dose » ; la courbe « doit montrer que le sabotage mesuré croît avec la dose » ; « critère 2 de la porte de fin de phase G0 » ; course de confirmation « 7b », « au plus tard le 15 novembre », le document disant « part » ou « création » à cette date. | Aucun. Incertitude signalée (résultat connu ou non à cette date), non pénalisée. |
| 8 | juste | (i) « instruction cachée dans son message système » ; (ii) « adaptateur appris […] la même politique sans aucune instruction au moment d'agir » ; sonde « j'ai une instruction cachée » : réussit sur (i), échoue sur (ii) ; sonde d'intention : réussit sur les deux. | Aucun. |
| 9 | juste | Moniteurs éprouvés après leur gel (« rien ne touche un moniteur […] avant son gel ») ; « connaissance déclarée, échelon par échelon » ; « une courbe, pas une attaque », l'évasion achetée « tout en causant un dommage réel » ; les trois témoins avec leur rôle exact. | Aucun. |
| 10 | juste | « Écrit et scellé avant toute donnée », par empreintes ; hypothèse, prédiction chiffrée et signée, métrique, seuil, plan d'analyse, critères de lecture, liste d'arrêt ; « contre-lu par une instance qui ne l'a pas écrit » ; lecteur neuf « pour que l'auteur ne juge jamais son propre résultat ». | Aucun. |
| 11 | partielle | Pression à « plusieurs intensités » ; Δv = g·(ĉ − v₀), le verdict allant de v₀ vers ĉ ; g « s'appelle la corruptibilité » ; g ≈ 0 pour une sonde robuste ; ĉ estimé « sans imposer ĉ ». | Manque la lecture de g > 0 sans accès aux poids comme contamination du construit : la réponse dit seulement « si la sonde se laisse déplacer sans accès aux poids, le papier change de titre ». |
| 12 | partielle | Phase 0, construction des instruments ; « deux des huit critères de G0 sont pourvus de leur pièce » ; harnais (critère 1) validé ; résultats des sondes à la session mère (« la section 10 est réservée à la session mère »). | Second critère pourvu non identifié : « le document ne dit pas lequel est le second » (compté comme manquant) ; absence de résultat de la revendication principale avant le mois 4 non dite ici (dite seulement en 3) ; course 7b vague : « la courbe dose-réponse (course 7b) est attendue au plus tard le 15 novembre » confond la création de la course et la remise de la courbe. |

## Décompte et verdict

- Juste : 10 (n° 1 à 10). Partielle : 2 (n° 11 et 12). Fausse : 0.
- Verdict selon la règle scellée : **PDF réussi** — dix « juste », soit exactement le seuil, et aucune « fausse ».

## Ce que le PDF devrait dire plus clairement (réponses qui ne sont pas « juste »)

- n° 11 : écrire, à côté de la formule, la lecture des valeurs de g — g ≈ 0 : moniteur robuste ; g > 0 obtenu sans accès aux poids : contamination du construit — et pas seulement la conséquence « le papier change de titre ».
- n° 12 : dans l'état au 10 novembre, nommer les deux critères pourvus (harnais validé ; agrégateurs validés en simulation, verdict formel en attente), écrire que la course 7b est à créer (non livrée) au plus tard le 15 novembre, et redire qu'aucun résultat de la revendication principale n'existe avant le mois 4.

## Jugements limites

Le verdict est atteint exactement au seuil : une « juste » de moins le renverse. Là où la formulation du lecteur s'écarte de l'attendu, voici pourquoi je n'ai pas hésité :
- n° 3 : le conflit sur le nombre de modes et le « pari apparié borné » non défini sont des réserves signalées comme incertaines ; l'attendu (« décidé par un pari apparié, mode par mode ») est dans la réponse.
- n° 4 et 6 : « note moyenne » au lieu de « marginale » ; l'attendu lui-même attache le déplacement de la marginale à δ > 0 (question 4), que la réponse donne.
- n° 5 : si l'on comptait chaque exemple entre parenthèses comme un élément à part, l'absence de « Page » ferait passer la réponse à « partielle » et le PDF à « non réussi » ; je ne le fais pas, parce que l'attendu donne « balayage, Page » comme exemples d'un élément (« des séries locales de notes hautes ») que la réponse énonce mot pour mot, avec la « somme glissante ». À l'inverse, en 11, la parenthèse donne le sens de g, et rien qui vaille « contamination du construit » ne figure dans la réponse.
- n° 12, pourquoi pas « fausse » : la réponse n'affirme aucun mauvais second critère (elle dit ne pas le trouver) et donne la bonne course et la bonne date ; « attendue » est imprécis, pas contraire à « à créer ».
