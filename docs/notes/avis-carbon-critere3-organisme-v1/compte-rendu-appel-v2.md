# Compte rendu du second envoi à Carbon sur le critère 3 et l'organisme (v2) — faux échec, « jamais parti »

Sans résultat : la mère peut le lire. Heure (`date -u`) : 2026-11-24T12:45:43Z. Lecteur : `session_01Qi7Gr5f9XYrvY8oLNZQ3wg`.

- Accord : GO-2026-11-24-22, même accord que le premier envoi (règle des pannes techniques ; mot de la mère de 12:13Z : envoi à partir de 12:35Z, au plus deux tentatives espacées de dix minutes).
- Question envoyée : `question-carbon-critere3-organisme-v2.md` (`09e6d41a…`), une phrase changée par rapport à la v1 (`changement-question-v1-vers-v2.md`, `191d3983…`). Erratum à cette note de changement : la question compte vingt-quatre lignes, non vingt-six ; une seule diffère.
- Garde commune des appels à Google : réglages conformes avant l'envoi (pire cas 2,74 USD sous le plafond de 3).
- Envois : essai 1 à 12:35:07Z, refus HTTP 503 (« This model is currently experiencing high demand », état UNAVAILABLE) ; essai 2 à 12:45:14Z, même refus. Les deux avant tout traitement : aucune réponse, aucun jeton facturé. Journal : `journal-appel-carbon-critere3-organisme-v2.txt`.
- **Issue codée : faux échec, « jamais parti ». Dépense : 0 USD.** Arrêt, comme fixé. Total sur cet accord : quatre refus 503 entre 12:11Z et 12:45Z, 0 USD.
- La réponse brute et la comparaison n'existent toujours pas. Ce matin, un appel au même modèle par la même voie avait abouti à 10:05Z après deux refus 503 : la panne est une pointe de demande chez Google, non un défaut de réglage ou de clé.
- Pour repartir, au choix de Lazar ou de la mère : (a) une nouvelle fenêtre de tentatives plus tard, sous le même accord ; (b) le même envoi par l'appel non diffusé du modèle, dont le plafond de sortie est plus bas — la garde commune l'admet, mais c'est un changement de réglage à nommer ; (c) un autre modèle externe, ce qui est une décision de Lazar. Sans mot neuf, ce lecteur ne renvoie rien.
