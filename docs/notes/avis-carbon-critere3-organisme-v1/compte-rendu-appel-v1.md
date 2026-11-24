# Compte rendu de l'appel à Carbon sur le critère 3 et l'organisme (v1) — faux échec, « jamais parti »

Sans résultat : la mère peut le lire. Heure (`date -u`) : 2026-11-24T12:12:49Z. Lecteur : `session_01Qi7Gr5f9XYrvY8oLNZQ3wg`.

- Accord : GO-2026-11-24-22 (vérifié sur la branche principale au commit `741b4df8` avant l'envoi ; plafond 3 USD). La ligne d'engagement au registre des dépenses n'était pas inscrite à 12:10Z : à porter par la mère.
- Question : `question-carbon-critere3-organisme-v1.md` (`d256e251…`), recopiée mot pour mot du message de la mère de 12:10Z. Garde commune des appels à Google : réglages conformes avant l'envoi (niveau de réflexion le plus haut, plafond de sortie 65 536 jetons dont 16 384 de texte au-delà de la réflexion, pire cas 2,73 USD).
- Envois : essai 1 à 12:11:54Z, refus HTTP 503 (« This model is currently experiencing high demand », état UNAVAILABLE) ; relance unique à 12:12:26Z, même refus. Les deux avant tout traitement : aucune réponse, aucun jeton facturé. Journal : `journal-appel-carbon-critere3-organisme-v1.txt`.
- **Issue codée : faux échec, « jamais parti ». Dépense : 0 USD.** Arrêt, conformément à l'accord (une seule relance sur refus 503).
- Ce qui existe sur la branche : la question, le script, le journal, et l'avis du lecteur écrit avant toute réponse (`avis-du-lecteur-avant-reponse-v1.md`, pour Lazar seul). La réponse brute et la comparaison n'existent pas.
- Pour repartir : un mot nommé pour une nouvelle relance sous le même accord (le script refuse seulement si un flux de réponse existe ; aucun n'existe), de préférence après quelques minutes, la panne étant une pointe de demande chez Google.
