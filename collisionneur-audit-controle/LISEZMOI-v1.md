# Collisionneur v2.6, étage III à tour III.2 défensif — audit défensif du programme de contrôle (v1)

Tour lancé le 26 octobre 2026 par l'instance qui reprend « session-depot », sur le mot direct de Lazar dans la session (« La partie à plusieurs modèles de l'audit (collisionneur, puis organisme) : go », vers 11:13 UTC, verbatim dans R-509), sous **GO-2026-10-26-04** (partie (1), plafond 10 USD). Matériau pour une décision de Lazar, jamais une consigne. Rien d'opposable (R7).

- Question `question-audit-controle-collisionneur-v1.md` (sha256 `ff7806a94aaf166cc5ed86129b89a13dc2d077d40ef20c3a55d0e692c70df489`), écrite par cette instance : ce que l'audit défensif (R-508) a manqué ou mal jugé ; cadre défensif, aucun procédé de contournement.
- Faits `faits-audit-controle-v1.md` (sha256 `574c6b769b291255a95bf1bba39fef17888dbd85b030b7656c81d48f440583a7`) : F1 le programme v2 (RAPPORTÉ), F2 l'audit `docs/notes/audit-controle-v1/audit-litterature-v1.md` (OBSERVÉ-NON-AUDITÉ), F3 la décision des cinq propositions (numérotée N-047 à l'écriture des faits, devenue N-053 par R-510 ; contenu identique hors numéro).
- Outil : `collisionneur_v2.py` v2.6 (`0e63febd…`, non modifié), appelé par le pilote `tour_audit_defensif_v1.py` (`3c34cb82…`) qui remplace le seul point (b) de la consigne du tour III.2 (« les scénarios d'évasion : comment un agent adverse tromperait chaque instrument… ») par « les hypothèses que la conception suppose sans les tester, chacune avec la mesure qui la testerait ; aucun procédé pour tromper un instrument n'est décrit » ; consigne rétablie à la sortie. Essais : `test_tour_audit_defensif_v1.py` (6, dont le témoin sans pilote, le refus et le plafond) et `test_collisionneur_v2.py` (59) : 65 passés.
- Une tentative par cellule ; refus consignés tels quels (R-468) ; plafond 10 USD vérifié avant chaque cellule (dépense + pire cas de la cellule) ; devis de l'étage III 21,53 USD au pire cas sans relance.
- Lanceur `lancer-tour-v1.sh` → `run-audit-controle-e3-v1` ; clés `RR_ANTHROPIC_API_KEY_LUC` et `GEMINI_API_KEY_2`, jamais écrites. Appel de contrôle par espèce : `appel-controle-especes-v1.json` (trois espèces OK, modèles servis conformes, 0,0015 USD).
- Journal du tour : `journal-etage3-v1.txt`.

| cellule | modèle | statut | jetons de sortie | coût |
|---|---|---|---|---|
| E3-T1-conception-A | claude-fable-5-1 | OK (end_turn) | 21 251 | 1,49 USD |
| E3-T1-conception-B | claude-opus-5-5 | OK (end_turn) | 34 078 | 0,85 USD |
| E3-T1-conception-C | gemini-4-argon | OK (STOP) | 8 820 | 0,75 USD |
| E3-T2-redteam-A | claude-fable-5-1 | OK (end_turn) | 21 098 | 1,74 USD |
| E3-T2-redteam-B | claude-opus-5-5 | OK (end_turn) | 19 384 | 0,66 USD |
| E3-T2-redteam-C | gemini-4-argon | OK (STOP) | 8 783 | 0,90 USD |
| E3-T3-riposte-A à C | — | non lancées : arrêt du plafond (code 4) avant tout appel, « dépense 6,39 + pire cas 3,76 USD > plafond 10,00 USD » | — | — |

Dépense du run : 6,39 USD (plus l'appel de contrôle) ; **aucun refus** ; six cellules valides sur six lancées ; de 2026-10-26T11:18:42Z à 2026-10-26T11:41:32Z. Le III.3 attend une décision de Lazar (plafond).
