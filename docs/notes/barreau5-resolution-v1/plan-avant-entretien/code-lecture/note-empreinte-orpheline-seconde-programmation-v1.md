# Note : empreinte orpheline du premier état de la seconde programmation (barreau 5) — v1

Écrite par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026. Pièce de travail.

- Le programmeur Fable de la seconde programmation a scellé `src/controle_ia/barreau5_familles/seconde_programmation_v1.py` dans son premier état (`55c26b8c6896820b155d5bf493cc83182459baa8ef39b731e6650da8fd5d521e`), comme son mandat le lui demandait (« scelle chaque état »), puis l'a modifié. Son second scellement a été refusé par l'outil de scellement (R12) ; il s'est arrêté sans rien contourner.
- Ce premier état n'a jamais été versé : le commit intermédiaire `d05179e38` de la mère a pris le module déjà modifié (`9c6d6253…`) avec le compagnon du premier état. Le contenu `55c26b8c…` est perdu. Erreur de la mère : le mandat demandait de sceller chaque état d'un module de `src/`, ce qui heurte R12.
- Traitement : le module modifié porte désormais le nom `seconde_programmation_v2.py` ; le fichier `seconde_programmation_v1.py` est retiré ; son compagnon `seconde_programmation_v1.py.sha256` est gardé tel quel, **empreinte orpheline connue et voulue** (précédent de R-799). Les essais passent sous le nom `test_barreau5_familles_seconde_programmation_v2.py`.
- Règle pour la suite : un module de `src/` ne se scelle qu'à son état final ; les états intermédiaires sont versés par la mère, marqués « ne pas employer ».
