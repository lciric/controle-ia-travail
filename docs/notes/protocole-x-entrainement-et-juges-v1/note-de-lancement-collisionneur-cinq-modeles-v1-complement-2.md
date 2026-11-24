# Note de lancement du collisionneur à cinq modèles — complément 2 : clé de Google du niveau gratuit

Écrite le 2026-11-24T14:00:45Z (`date -u`), avant la relance. Complète la note de lancement et son complément 1, qui ne sont pas réécrits.

- Mot de Lazar vers 13:5xZ, relayé par la mère à 14:00:07Z : « utilise la clé gemini free ».
- **Changement consigné** : pour cette commande seule, la variable `GEMINI_API_KEY` lue par le programme reçoit la valeur de `GEMINI_API_KEY_FREE` (lue par son nom, jamais affichée). Raison : `GEMINI_API_KEY_2` à crédit prépayé épuisé (402 à 13:27:45Z) ; clé par défaut saturée (503 à 13:29:10Z et 13:32:39Z). `GEMINI_API_KEY_3` n'est jamais employée.
- Garde de Google inchangée (celle du programme) : réflexion explicite ; plafond au moins égal à la réflexion plus 16 000 jetons ; MAX_TOKENS, SAFETY, RECITATION ou texte vide : défaut, jamais réponse.
- Une reprise unique par cellule après un refus 503 ou 429 (quota du niveau gratuit). Si le niveau gratuit refuse le modèle (403 ou 404) : arrêt, fin à trois (Fable, Opus, Astra), absences déclarées.
- Dépense : nulle au niveau gratuit en principe ; comptée au pire par le programme. Ligne de 30 USD ; 11,86 USD comptés avant cette relance.
