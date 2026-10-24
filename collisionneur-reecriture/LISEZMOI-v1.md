# Collisionneur v2.5, étage III, un seul tour (III.1) — question « réécrire sa structure ou apprendre dedans » (v1)

Écrit le 24 octobre 2026 (23:45 UTC) par la lignée « session-depot », sous GO-2026-10-24-07 (« préparatifs », 200 USD),
sur la décision de Lazar du 25 octobre, 00:05 heure de Paris (« lance-le »), relayée par « conv-audit » (message n° 28
§ 1). Matériau pour le dessin du noyau (budgets, primitives), jamais une consigne aux organismes. Rien d'opposable (R7).

- Outil : `collisionneur_v2.py` v2.5 (`213b52ef…`, non modifié ; branche `outils/essaim-m3-refonte-v1-travail`), appelé
  pour le seul tour E3-T1 par `tour_unique_etage3_v1.py` (ce dossier) : l'outil n'a pas d'option « un tour » ; le pilote
  appelle ses fonctions dans l'ordre de `lancer_etage` (entrées versées et scellées, une cellule par lettre, plafond vérifié
  avant chaque appel, relances bornées, refus définitif) ; éprouvé à sec avec les doubles de l'outil avant l'appel réel.
- Pièces : `question-reecriture-vs-apprentissage-v1.md` (`89d8c3db…`, figée par « conv-audit ») ; aucun fait joint
  (`faits-aucun-v1.md`, une ligne, `6aad3b3b…`).
- Lancé à 23:35:25 UTC, fini à 23:40:47 UTC ; environnement minimal (`ANTHROPIC_API_KEY` = valeur de
  `RR_ANTHROPIC_API_KEY`, en-tête d'espace de travail, `GEMINI_API_KEY` ; aucune valeur écrite : recherche des formes de
  clés dans ce dossier, aucune trouvée).

## Résultat (`run-reecriture-e3t1-v1/etat.md`, `verifier` : « tout tient »)

| cellule | modèle | statut | caractères | coût |
|---|---|---|---|---|
| E3-T1-conception-A | claude-fable-5-1 | OK | 21 439 | 0,85 USD |
| E3-T1-conception-B | claude-opus-5-5 | **REFUS** (catégorie « cyber ») | 0 | 0,20 USD |
| E3-T1-conception-C | gemini-4-argon | **ÉCHEC** (HTTP 402 : crédit prépayé épuisé) | 0 | 0,00 USD |

Dépense : **1,05 USD** sous GO-2026-10-24-07. Le refus d'Opus est définitif dans ce run (une seule tentative, aucune
reformulation : procédure du lot 3 et message n° 28). L'échec d'Argon vient du crédit du compte de `GEMINI_API_KEY` :
cellule C non faite ; une reprise demande un crédit rechargé (ou la clé n° 2) et se fait dans ce même dossier (les
cellules valides ne sont pas relancées).
