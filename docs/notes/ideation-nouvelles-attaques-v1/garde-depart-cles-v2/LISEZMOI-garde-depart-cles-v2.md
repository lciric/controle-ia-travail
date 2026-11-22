# Garde de départ « prêt / manque » — v2, et premier relevé réel (passe X)

- **Version.** La v2 remplace la v1 (`../garde-depart-cles-v1/`, archivée sans changement). Un seul changement, sur la consigne de la mère sous GO-2026-11-22-54 : pour Google, aucun appel ne génère. L'essai Google est `countTokens`, qui est gratuit. Il prouve l'accès au modèle, **pas le crédit**, et rend la raison « prêt, accès seul ». La sortie liste ces clés sous `credit_non_prouve`. Pour le reste, voir le LISEZMOI de la v1.
- **Épreuve (R5).** 40 essais passent (`test-garde-depart-cles-v2-pytest.txt`) : ceux de la v1, plus des artefacts propres à Google et le rapport du crédit non prouvé.
- **Relevé réel**, sous GO-2026-11-22-54, le 2026-11-22 :
  - plan : `plan-garde-depart-passe-x-20261122T121952Z.json` ;
  - journal : `journal-garde-depart-passe-x-20261122T121952Z.jsonl`.

| clé (par son nom) | modèle | verdict | raison | modèle servi |
|---|---|---|---|---|
| RR_ANTHROPIC_API_KEY_LUC | claude-opus-4-6 | prêt | prêt | identique |
| RR_ANTHROPIC_API_KEY_LUC | claude-sonnet-4-6 | prêt | prêt | identique |
| RR_ANTHROPIC_API_KEY_LUC | claude-fable-5-2 | prêt | prêt | identique |
| GEMINI_API_KEY | gemini-4-argon | prêt | prêt, accès seul | — |
| GEMINI_API_KEY | gemini-4-neon | prêt | prêt, accès seul | — |
| OPENAI_API_KEY_2 | gpt-6-astra | prêt | prêt | identique |
| KIMI_API_KEY | kimi-k3.1-pro | prêt | prêt | identique |

- **Coût.** 0,001126 USD au tarif du plan. Le pire de lettre était de 0,002195 USD. GO-54 permet moins de 0,01 USD par clé.
- **Réserves.**
  - (1) Le crédit de Google n'est pas prouvé. C'est un compte payant, dont la carte paie au-delà du crédit (complément v3, § 4).
  - (2) Les identifiants des espèces 3 et 4 de la course ne sont pas dans mes pièces. Je n'ai essayé sur Luc que Opus 4.6, Sonnet 4.6 et Fable 5.2. Mais le crédit est une propriété de la clé, et il est prouvé.
  - (3) OPENAI_API_KEY n'est pas essayée, la mère la disant à sec.
