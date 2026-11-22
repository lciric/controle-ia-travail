# Devis : trois relectures par Fable 5.2, par l'interface d'Anthropic, des lots réduits de la vérité plantée — 22 novembre 2026 (v1)

- Objet : relecture des corrections déjà écrites (errata 1 et 2) des trois étapes 0 du banc à vérité plantée — tâches floues, dommages plantés par un tiers, banc à lois plantées — sur les lots réduits déjà préparés et passés à la garde (commit 41e4d915).
- Outil : `src/controle_ia/relecture_fable_api_v5.py` (empreinte compagnon sur main), modèle `claude-fable-5-2`, effort « max », budget de tâche 96 000, sortie maximale 128 000 ; clé lue par son nom, `RR_ANTHROPIC_API_KEY_MINUIT`. Un journal de dépense par lot, plafond de ligne 6 USD chacun. Les commandes v1 des lots réduits passent de l'outil v2 à l'outil v5 ; pièces, remarques et consignes inchangées.
- Prix lus dans l'outil : 8 USD par million de jetons d'entrée, 40 USD par million de jetons de sortie.
- Entrées estimées (1,76 caractère par jeton, mesure de l'outil ; l'outil compte exactement avant tout envoi et refuse au-delà du plafond) : dommages par un tiers 73 409 ; lois plantées 69 263 ; tâches floues 70 446.
- Pire cas, sortie comptée au maximum : 5,71 + 5,67 + 5,68 = **17,06 USD**. Attendu, d'après les demandes 22A à 22C rendues avec le même réglage (1,05 à 1,16 USD, entrées plus petites) : environ 1,5 à 3 USD par lot, 5 à 9 USD en tout.
- Défaut : toute sortie sans texte, arrêt en `max_tokens`, refus, est un défaut journalisé, jamais une réponse. Sur défaut, **une relance au plus par lot**, en effort « high », dans le même plafond de 6 USD par lot (journal cumulé ; l'outil refuse si le cumul plus le pire cas dépasse).
- Plafond demandé de la ligne : **24 USD** (trois envois et au plus une relance, chacun sous 6 USD). Rappel : 11,68 USD déjà perdus le 21 novembre (deux défauts, réflexion sans texte) sous le plafond de 30 USD de R-4738 ; ce devis n'y puise pas, il demande une ligne neuve.
- Échéance : 2026-11-24.
