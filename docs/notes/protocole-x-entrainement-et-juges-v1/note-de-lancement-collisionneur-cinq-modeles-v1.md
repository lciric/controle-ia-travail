# Note de lancement du collisionneur à cinq modèles — « ce qui entre dans un programme amélioré et ambitieux, entraînement compris » — v1

Écrite le 2026-11-24T12:51:47Z (`date -u`), avant le lancement, par la session du protocole X. Classe C.

## Accord

`GO-2026-11-24-26` (30 USD, échéance 2026-11-30), lu au registre des accords de la branche principale (commit `103e0a71`, ligne 904, R-5282) : mot de Lazar vers 12:50Z, « ah non je veux carbon et fable aussi et astra » ; Fable 5.2, Carbon et Astra ajoutés à Opus 5.5 et Neon, même question neutre, voie la moins coûteuse ; départ sans nouveau mot sous 30 USD. Arbitrage de la mère reçu à 12:51:04Z : voie 2 (dossier neuf à cinq modèles), le programme refusant d'ajouter des espèces à une course commencée (composition scellée dans `especes.json`).

## Ce qui part

- Même programme (`collisionneur_v9_v8m.py`, `420394f9…`), mêmes faits (`faits-neutres-demande-1-v3.md`, `c2b9327b…`) et même question (`question-neutre-collisionneur-demande-1-v2.md`, `4494b200…`), étage III.
- Espèces : Fable 5.2, Opus 5.5, Astra, Carbon, Neon.
- Clés, lues par leur nom : Anthropic `RR_ANTHROPIC_API_KEY` ; OpenAI `OPENAI_API_KEY` (puis `OPENAI_API_KEY_2` si la première refuse) ; Google : le programme ne lit que `GEMINI_API_KEY`, qui reçoit pour cette commande la valeur de `GEMINI_API_KEY_2` (jamais `_3`).
- Dossier : `runs/collisionneur-protocole-x-programme-ameliore-entrainement-cinq-modeles-v1-20261124-125147` ; plafond et ligne : 30 USD.
- Devis (fonction de devis du programme, sans réseau) : 15 cellules, 26,94 USD au pire sans relance, dont 12,65 sur la clé Anthropic (Fable 8,39 ; Opus 4,26) ; attendu de 11 à 12,5 USD [extrapolé du rapport attendu/pire d'un devis voisin].

## Conduite

- Une coupure de Carbon ou un refus d'Astra : absence acceptée, sans boucle (décision nommée de la mère, dans `GO-2026-11-24-26`).
- Toute autre panne : arrêt et compte rendu.
- La course à deux espèces en cours (Opus 5.5 et Neon, dossier `runs/collisionneur-protocole-x-programme-ameliore-entrainement-v1-20261124-115219`) est arrêtée par son numéro de processus dès que la conception de Neon est valide ; ses cellules valides deviennent matériau rapporté.
- La note de sortie réunit le collisionneur à cinq modèles et les réponses directes de Fable et de Carbon, en disant ce qui a été soumis aux critiques croisées et ce qui ne l'a pas été.
