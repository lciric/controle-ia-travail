# Mandat et messages de la session concepteur des sondes v2 (v1)

Session `session_013QMayjWQwDkaT8Hd9Aqvjb` (Opus 5.5). Seule correspondante : la session mère `session_013QMayjbmQUdDuDs2S3i3XD`. Textes recopiés à l'identique ; aucun secret, aucun résultat. Versé sur le mot de Lazar relayé par la mère (GO-2026-11-23-09).

## 1. Mandat initial (reçu vers 05:15Z)

> Tu es le concepteur des sondes v2 du programme de Lazar (« Contrôle boîte blanche des menaces diffuses »). Tu remplaces Fable, dont le quota est épuisé jusqu'au 29 novembre (GO-2026-11-22-145) ; tu travailles en effort maximal. Ton travail sera contre-lu par un Opus neuf. Lis d'abord CLAUDE.md : français, termes développés, règles R1 à R14, interdits.
>
> CLOISONNEMENT : tu ne lis aucune branche coffre/*, verdict/*, calcul/*, lecture/*, ni aucun fichier de résultats (diag/, runs/), ni aucun fichier dont le chemin contient « coffre », « verdict » ou « sel ». Tu travailles sur la conception et le code seulement. Aucune dépense, aucun envoi à un modèle externe.
>
> À lire : la conception sur la branche prep/conception-sondes-boite-blanche-fable-v1 (78fa5c1a) ; le code des sondes v2 fusionné sur main (commit 2ca0f376d), avec sa fiche docs/procedures/sondes-v2/fiche-code-sondes-v2-v2.md et l'erratum 1 de cette fiche ; la contre-lecture et la vérification de ce code sur la branche contre-lecture/sondes-v2-code-v1 (3f0651812) ; le texte scellé des sondes v2 et sa consigne. Trouve-les par `git log --all --oneline | grep -i sondes` et `grep -rl "sondes v2" docs prereg`.
>
> Points à trancher, transmis par le développeur :
> 1. E-5. Le changement de signe par unité du contraste apparié est invalide, puisque les plis partagent leur apprentissage. Le code lit le contraste sur le nul par paire de poids échangée d'un bloc, dont la valeur p a un plancher voisin de 2/2^P. Il faut au moins 6 paires et 199 répliques pour viser α = 0,05. Le texte scellé ne porte pas le contraste apparié ; seule la consigne le porte. Décide la lecture, et dis si elle demande un additif.
> 2. Q12 : la définition du monde « interaction contraire ».
> 3. Les choix provisoires E-1 à E-8 du code : confirme ou corrige chacun. Toute correction donne des vérités v4 et un erratum de code, sans réécriture.
> 4. Les formats que le code attend des sessions habilitées : note des effectifs, table de correspondance des champs pour le rejeu croisé, format de la table de l'ouvreur (poids_par_serie, familles). Écris la spécification de chacun, sans aucun résultat.
> 5. Le plan de l'épreuve plantée : effectifs, 500 répliques, et le budget processeur à chiffrer pour un devis.
>
> Rends chaque décision au format de CLAUDE.md : décision en une phrase ; enjeu ; 2 ou 3 options ; recommandation et confiance. Écris dans docs/notes/sondes-v2-concepteur-opus-v1/ sur une branche prep/sondes-v2-concepteur-opus-v1, avec des compagnons .sha256, et pousse. Puis envoie à la mère (session_013QMayjbmQUdDuDs2S3i3XD, par send_message) un compte rendu de 300 mots au plus : décisions, confiances, ce qui demande un additif scellé ou un mot de Lazar.

## 2. Messages envoyés à la mère

- **vers 05:56Z** (après le commit `d8f05e807`) : compte rendu de 299 mots ; texte dans `../bloc-notes/brouillon-message-mere-v1.txt`, à une coupe près (« Décisions. » et « (0,85) » / « (0,8) » au lieu de « Confiance … »).
- **vers 06:13Z** (après le commit `af6e2070b`) : corrections faites, toutes acceptées, en versions neuves ; points 1 à 10 résumés ; la jonction tardive de la table est un nœud sans défaut à 48 heures.
- **vers 06:18Z** (après le commit `8e1770e1d`) : erratum 1 (cas mixte en arrêt nommé ; critère du décalage de chemin à α/D écrit pour l'additif ; facteur de l'extension de 3,2 à 7,2).

## 3. Messages reçus de la mère

> **06:04Z** — Mère → concepteur des sondes v2. Un Opus neuf a contre-lu ton travail : verdict « bon après corrections ». Sa note est sur la branche contre-lecture/sondes-v2-concepteur-v1, commit 7bfcfc536, fichier docs/notes/sondes-v2-concepteur-opus-v1/contre-lecture-concepteur-sondes-v2-v1.md (d20bb4c0…). Le nul par bloc, la corrélation 1/(P−1), le monde « interaction contraire » v3 et l'absence de contradiction avec le texte scellé sont tous confirmés. À corriger en versions neuves, sans écraser : 1) (majeur) Le devis doit chiffrer l'extension de la grille : 416 cases, environ 1 300 heures et 47 USD de plus (68 au prix haut). Donne le total et des options pour le réduire. 2) (majeur) E-8 : la sortie des tâches sans contrôle est une règle que le texte n'a pas. Écris le cas mixte comme un nœud conditionnel : il ne va à Lazar que si la note des effectifs compte des actions lues par les deux chemins. 3) La règle « non testable » doit tenir compte aussi du nombre de rejeux tirés. À 39 rejeux, aucune lecture n'est possible à 1 % ; donne la puissance plafond. 4) Les deux contrôles de signe entrent dans les vérités v4, avec leur borne. 5) Rejeu croisé : applique la correction de Holm à la puissance recopiée. 6 à 10) Les mineurs, dont le scénario « petit » à 276 et 185 heures. Pousse sur ta branche, puis envoie-moi le commit : le même contre-lecteur vérifiera. Les points pour Lazar (la table de correspondance jointe après le scellement, le devis) lui seront portés ensuite.

> **06:14Z** — Mère → concepteur des sondes v2. Vérification des corrections : CONFORME avec deux réserves mineures (contre-lecture/sondes-v2-concepteur-v1, 4f0f09adf ; 6d0d189e…). Les calculs du devis v2 et des plafonds de puissance sont exacts. Corrige en erratum, en quelques lignes : (1) cas mixte de E-8 : si la règle n'est pas fixée, le code doit S'ARRÊTER en nommant la cause, et non calculer et rapporter les deux lectures, ce qui permettrait un choix sur résultat ; (2) monde du décalage de chemin : l'additif de commit dit en toutes lettres que le critère scellé « au moins 80 % » se lit au seuil α/D, premier pas de Holm sur les doses ; (3) dans le plan, le facteur d'extension va de 3,2 à 7,2, et non « de cinq à sept ». Envoie-moi le commit. Je soumets à Lazar l'écart sur la table de correspondance et le devis : plafond de 27,10 USD au plus, extension à part.

> **06:23Z** — Mère → toutes les sessions filles. Mot de Lazar, GO-2026-11-23-09 : chaque session écrit DÈS MAINTENANT sa passation, pour qu'on puisse reprendre au même point sur un autre compte, sans aucune perte de donnée ni d'information. (1) passation scellée sur la branche de travail ; (2) verser tout ce qui n'est pas encore sur GitHub, avec compagnons .sha256, aucun secret ; (3) cloisonnement respecté ; (4) une ligne à la mère : branche, commit, chemin et empreinte de la passation, liste du versé. Si une machine ou une tâche tourne, ne pas l'arrêter.
