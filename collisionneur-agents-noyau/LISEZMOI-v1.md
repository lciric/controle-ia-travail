# Collisionneur v2.5, étage III, trois tours (III.1 à III.3) — question de conv-audit « faire tester des agents sur le noyau pendant la conception par essais-erreurs » (v1)

Écrit le 26 octobre 2026 (01:2x UTC) par « session-depot », sous GO-2026-10-24-07, sur le mot direct de Lazar (R-466,
« go dépense »). Question de conv-audit `question-agents-noyau-essais-erreurs-collisionneur-v1.md` (`canal/conv-audit-n04`,
`961f87e0`, `6de36af7…`, vérifiée avant le départ). Matériau pour une décision de Lazar, jamais une consigne, servi à aucun
organisme. Rien d'opposable (R7).

- Outil `collisionneur_v2.py` v2.5 (`213b52ef…`), `etage3` (`lancer-tour-v1.sh`), puis, après la porte fermée au III.1
  (refus d'Opus), `suite-etage3-v1.sh` (absence acceptée E3-T1-conception-B, R-468, R-472) ; plafond 10 USD ; une
  tentative par cellule ; aucune cellule refusée relancée. 01:03:17 à 01:27:39 UTC (porte après III.3, code 2). Clés :
  Anthropic n° 3, Gemini n° 2 ; aucune valeur écrite.

| cellule | modèle | statut | jetons de sortie | coût |
|---|---|---|---|---|
| E3-T1-conception-A | claude-fable-5-1 | OK (end_turn) | 16 437 | 0,86 USD |
| E3-T1-conception-B | claude-opus-5-5 | **REFUS** (refusal) | 13 108 | 0,28 USD |
| E3-T1-conception-C | gemini-4-argon | OK (STOP) | 11 680 | 0,61 USD |
| E3-T2-redteam-A | claude-fable-5-1 | OK (end_turn) | 13 391 | 0,89 USD |
| E3-T2-redteam-B | claude-opus-5-5 | OK (end_turn) | 20 886 | 0,55 USD |
| E3-T2-redteam-C | gemini-4-argon | OK (STOP) | 4 897 | 0,34 USD |
| E3-T3-riposte-A | claude-fable-5-1 | OK (end_turn) | 14 815 | 1,04 USD |
| E3-T3-riposte-B | claude-opus-5-5 | **REFUS** (refusal) | 1 384 | 0,11 USD |
| E3-T3-riposte-C | gemini-4-argon | OK (STOP) | 9 115 | 0,71 USD |

Dépense : **5,39 USD**. Sept cellules sur neuf valides. Les refus d'Opus sont reformulés à part (R-468, R-472 : question
« conception itérative », `donnees/collisionneur-agents-noyau-methodo-v1`, réponse valide). Réponses dans
`run-agents-noyau-e3t1-v1/cellules/` (les cellules refusées ne sont pas lues).
