# Collisionneur v2.5, étage III, un seul tour (III.1) — question « allocation d'un budget de calcul entre le choix de la classe d'hypothèses et l'ajustement des paramètres » (v1)

Écrit le 25 octobre 2026 (07:5x UTC) par la lignée « session-depot », sous GO-2026-10-24-07 (« préparatifs », 200 USD),
sur le **mot direct de Lazar dans la session** (« go collisionneur », R-389), pour la question nouvelle qu'il a demandée
(« purement technique et conceptuelle mathématique […], c'est une nouvelle demande », 08:14 heure de Paris, relayé par
« conv-audit », n° 32). Matériau pour le dessin du noyau, jamais une consigne aux organismes. Rien d'opposable (R7).

- Outil : `collisionneur_v2.py` v2.5 (`213b52ef…`, non modifié), appelé pour le seul tour E3-T1 par
  `tour_unique_etage3_v1.py` (`be609dc5…`, le même qu'au tour du 24 octobre) ; entrées versées et scellées, une cellule
  par lettre, plafond (10 USD) vérifié avant chaque appel, une tentative par cellule, refus définitif sans reformulation.
- Pièces : `question-allocation-budget-classes-parametres-v1.md` (`ea904c53…`, figée et versée par « conv-audit ») ;
  aucun fait joint (`faits-aucun-v1.md`, `6aad3b3b…`). Devis au pire cas : 6,13 USD sans relance.
- Lancé à 07:34:56 UTC, fini à 07:45:30 UTC (`lancer-tour-v1.sh`) ; environnement minimal (`ANTHROPIC_API_KEY` = valeur
  de `RR_ANTHROPIC_API_KEY`, en-tête d'espace de travail, `GEMINI_API_KEY` = valeur de `GEMINI_API_KEY_2`, mandataire ;
  `ANTHROPIC_BASE_URL` absente ; aucune valeur écrite : recherche des formes de clés dans ce dossier, aucune trouvée).

## Résultat (`run-allocation-e3t1-v1/etat.md` ; `verifier` : « tout tient »)

| cellule | modèle | statut | caractères | jetons de sortie | coût |
|---|---|---|---|---|---|
| E3-T1-conception-A | claude-fable-5-1 | OK (end_turn) | 29 953 | 17 510 | 0,90 USD |
| E3-T1-conception-B | claude-opus-5-5 | OK (end_turn) | 31 929 | 24 863 | 0,51 USD |
| E3-T1-conception-C | gemini-4-argon | OK (STOP) | 43 050 | 12 934 | 0,66 USD |

Dépense : **2,07 USD** sous GO-2026-10-24-07. Les trois cellules sont valides. Opus n'a pas refusé (la question évite les
sujets sensibles) ; Argon a répondu (la clé Gemini n° 2 a du crédit). Les réponses n'ont pas été lues par
« session-depot » à ce stade ; leurs références sont « à vérifier » (R7 : aucun chiffre ni aucune référence opposable
avant vérification sur pièce).
