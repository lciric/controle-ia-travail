# Collisionneurs v8d, compte rendu 9 : cause des deux coupures, sans dépense (réponse au mot de 23:07Z)

1. Lignes [agent-proxy] : aucune, ni dans `journal-reprise-v8.txt` (sortie d'erreur jointe par `2>&1`), ni ailleurs dans le dossier. Ces lignes sont ajoutées par l'outil de commande à la fin d'une commande au premier plan qui échoue ; nos courses sont détachées : rien ne nomme l'hôte ni la raison.
2. Durées des flux coupés, de l'envoi à la coupure (`debut`, `fin_utc` du journal) : Argon E3-T2-critique-croisee-C essai 1, 22:45:49 → 22:51:17, 328 s, 12 987 caractères de texte reçus ; Carbon E3-T2-critique-croisee-E essai 1, 23:00:19 → 23:05:19, 300 s, 0 caractère de texte reçu.
3. Flux de Google réussis ce soir, même v8d : 166 s, 269 s, 270 s, 365 s (Argon, essai 2 de la cellule coupée) et **585 s** (Carbon, percée, tour III.3). Une borne fixe de durée du tunnel vers 300 à 330 s ne tient donc pas.
4. Seule piste lisible, non établie : un silence prolongé du flux. Carbon a été coupé sans aucun texte reçu, après cinq minutes de réflexion ; Argon, lui, envoyait du texte. Je ne sais pas si les pensées arrivent par morceaux dans le flux ; je n'ai pas lu les réponses.
5. Lecture : cause non établie, pas de durée bornée visible ; selon ton mot, une seule reprise de plus. Rien n'est parti. Antériorité et fusionnée attendent.
