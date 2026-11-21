# Deux relectures par Fable en défaut : la réflexion a mangé toute la sortie — 21 novembre 2026, vers 22:00 UTC

- Banc à lois plantées : arrêt en max_tokens, 128 000 jetons de sortie, tous de réflexion, aucun texte ; 87 096 jetons d'entrée ; coût compté 5,816768 USD.
- Dommages par un tiers : arrêt en max_tokens, 96 000 jetons de sortie, tous de réflexion, aucun texte ; 252 846 jetons d'entrée ; coût compté 5,862768 USD.
- Total dépensé pour rien : 11,679536 USD sur le plafond de 18. Reste 6,32 USD. Journaux : `docs/notes/relecture-plantee-etapes-0-v1/journal-depense-relecture-{lois-plantees,dommages-tiers}-v1.jsonl`. L'outil a bien rangé ces sorties en « défaut » et n'en a fait aucune réponse ; rien n'est à récupérer, il n'y a aucun texte partiel.
- Cause : l'outil envoie l'effort « max » avec une réflexion adaptative sans borne propre. Sur ces lots, la réflexion prend tout le plafond de sortie. C'est un défaut de réglage, du même genre que celui de la règle sur Carbon.
- Arrêt sur ce point : le lot des tâches floues n'est pas envoyé (même réglage, même issue probable).
- Décision pour toi, puis pour Lazar si un dépassement est en jeu. Options :
  (a) une v3 de l'outil, contre-lue, qui borne la réflexion à part (par exemple un budget de réflexion fixe, laissant au moins 16 000 jetons de texte), ou un effort plus bas ; puis les trois relectures relancées. Coût : environ 3 × 5 USD, au-delà du reste de 6,32 USD, donc un devis neuf.
  (b) des lots plus petits : la seule table remarque par remarque et les errata, sans les pièces d'avant. Moins de réflexion probable, mais rien ne la borne.
  (c) renoncer à Fable par l'API et attendre le 24 novembre à 05:00 UTC pour la relecture par Fable dans Claude Code.
  Recommandation : (a) avec un budget de réflexion borné, si l'API le permet pour ce modèle ; sinon (c). Confiance 0,6.
