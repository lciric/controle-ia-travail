# Note de lancement du collisionneur, dossier 1 — complément 2 : une relance de plus, par la seconde clé de Google

Écrite le 2026-11-24T12:39:03Z (`date -u`), avant la relance. Complète `note-de-lancement-collisionneur-dossier-1-v1.md` et son complément 1, qui ne sont pas réécrits.

- Relances 1 à 3 de la règle R-5272 (12:16:21Z, 12:26:41Z, 12:37:03Z) : Neon refusé chaque fois par Google, 503 « forte demande », avant tout traitement. Course close à 12:37:03Z ; vérification du programme : « tout tient ».
- Message de la mère reçu à 12:36:40Z (décision nommée, R-5272 étendue) : la fille des collisionneurs constate que Neon répond par la clé `GEMINI_API_KEY_2` et rend des 503 par la clé par défaut depuis le matin ; **une** relance de plus est permise avec `GEMINI_API_KEY_2` ; rien d'autre ne change : même ligne de 21 USD, même règle d'arrêt.
- **Changement de clé, consigné ici** : le programme ne lit que la variable `GEMINI_API_KEY` ; pour cette seule commande, elle reçoit la valeur de `GEMINI_API_KEY_2` (lue par son nom, jamais affichée). La clé `GEMINI_API_KEY_3` n'est pas employée. Les cellules de Carbon restent absentes : aucun envoi à Carbon.
- Même commande que le complément 1, au même dossier, avec les trois mêmes absences acceptées. Départ à 12:47:10Z au plus tôt, pour garder dix minutes entre deux relances.
- Dépense comptée sur la ligne avant cette relance : 8,68 USD. Pire cas du reste (Neon conception, puis critiques croisées et réponses d'Opus et de Neon) : 7,44 USD ; total compté au pire : 16,12 USD, sous la ligne.
- Toute panne : arrêt, aucune relance, compte rendu.
