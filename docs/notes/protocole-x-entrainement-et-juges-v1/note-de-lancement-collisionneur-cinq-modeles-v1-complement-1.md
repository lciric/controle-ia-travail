# Note de lancement du collisionneur à cinq modèles — complément 1 : écart de clé pour Google

Écrite le 2026-11-24T13:29:06Z (`date -u`), avant la relance. Complète `note-de-lancement-collisionneur-cinq-modeles-v1.md`, qui n'est pas réécrite.

- 13:00Z : Astra refusé par `OPENAI_API_KEY` (crédit épuisé) ; relance par `OPENAI_API_KEY_2`, comme l'accord le prévoit.
- 13:27:45Z : critique croisée de Carbon refusée par Google, HTTP 402, crédit prépayé de `GEMINI_API_KEY_2` épuisé ; rien n'est facturé. Faux échec, panne de crédit.
- **Écart consigné** : `GO-2026-11-24-26` nomme `GEMINI_API_KEY_2` pour Carbon. Décision nommée de la mère, reçue à 13:28:50Z : relance sur le même accord avec `GEMINI_API_KEY` (clé par défaut) pour Carbon et Neon ; une reprise unique par cellule après un refus 503 ; garde de Google inchangée ; si une cellule de Google échoue encore, aucune relance, attente du mot de la mère (recharge de `_2` par Lazar, ou fin à trois avec absences déclarées). `GEMINI_API_KEY_3` n'est jamais employée.
- Commande : la même, dans le même dossier `runs/collisionneur-protocole-x-programme-ameliore-entrainement-cinq-modeles-v1-20261124-125147`, avec `--cle-openai OPENAI_API_KEY_2` ; la variable `GEMINI_API_KEY` garde sa propre valeur (aucune substitution).
