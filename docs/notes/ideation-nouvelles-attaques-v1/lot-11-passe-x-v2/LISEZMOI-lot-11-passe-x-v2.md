# Lot 11 du véhicule NA-1 — exécutant de la passe X — v2

Écrit le 2026-11-22 (`date -u` : 12:41:31Z) par la session de l'organisme.

- **Version.** La v2 remplace la v1 (`../lot-11-passe-x-v1/`, archivée sans changement). Elle suit la vérification `../lot-11-passe-x-v1/verification-v1/verification-lot-11-passe-x-v1.md`, verdict « À corriger ».
  - Points bloquants B1 à B4 : tous portés.
  - Réserves R1 à R8 : toutes portées.
  - Ajout G4b : l'essai de réglages d'effort.
  - Le détail est dans l'en-tête du module.
- **Épreuve.**
  - 73 essais passent (`test-passe-x-na-v2-pytest.txt`).
  - 39 mutations sont toutes tuées, et le témoin T0 survit (`sortie-mutations-passe-x-na-v2.json`).
  - Chaque point de la vérification a son essai et sa mutation.
- **Configuration de lancement** : `lancement/configuration-passe-x-v1.json` (scellée) et `lancement/plan-garde-depart-passe-x-v1.json` (8 couples). Le contrôle à blanc est conforme.

| proposeur | modèle | clé (par son nom) | sortie | réglage |
|---|---|---|---|---|
| espèce 1 | gemini-4-argon | GEMINI_API_KEY | 65 536 | niveau high, réflexion comptée 49 152 |
| espèce 2 | gpt-6-astra | OPENAI_API_KEY_2 | 96 000 | effort essayé : xhigh, puis high |
| espèce 3 | claude-opus-5-5, puis Opus 4.6, puis Sonnet 4.6 | RR_ANTHROPIC_API_KEY_LUC | 96 000 | adaptatif ; effort essayé : max, xhigh, high |
| espèce 4 | claude-fable-5-1, puis Opus 4.6, puis Sonnet 4.6 | RR_ANTHROPIC_API_KEY_LUC | 96 000 | idem |
| espèce 5 | gemini-4-carbon | GEMINI_API_KEY | 65 536 | niveau high, réflexion comptée 49 152 |
| ajout | kimi-k3.1-pro | KIMI_API_KEY | 96 000 | — |
| ajout | claude-opus-4-6, puis Sonnet 4.6 | RR_ANTHROPIC_API_KEY_LUC | 96 000 | adaptatif ; effort essayé |
| ajout | claude-sonnet-4-6 | RR_ANTHROPIC_API_KEY_LUC | 96 000 | adaptatif ; effort essayé |

**Sous-parts** : Luc 72,60 ; GEMINI_API_KEY 12,10 ; OPENAI_API_KEY_2 6,05 ; KIMI_API_KEY 6,05. Total : P_X = 96,80 USD (devis v3 scellé, 83a3f035…).

**Sources.**
- Identifiants des espèces : `runs/20261119-094145-course-auto-conception-v9/configuration-orchestrateur.json` (ce3968e7…).
- Correspondance des numéros : le devis de l'héritage v5 (30c87fa6…), § 1, avec le manifeste de fin (28bc36df…).
- Tarifs et sorties de Claude : page versée `docs/sources/tarifs/anthropic-2026-11-22/platform-claude-com-models-overview-2026-11-22.html`.
- Kimi : TK. Astra et Carbon : bornes du devis.

**Écarts déclarés.**
1. **Google à 65 536** (dont 49 152 de réflexion comptée), sous la garde v3 : accordé par la mère et écrit à la ligne d'ouverture du journal.
2. **Huit proposeurs et non cinq** (X-1, X-10) : c'est la liste de GO-2026-11-22-46, sur le mot de Lazar, et le pire de 96,80 vient du devis v3 scellé.
3. **Noms des classes.** Les classes « erreur de requête » et « injoignable » valent, pour A6, « réponse illisible, cause non établie ».
4. **A5.** La catégorie d'un refus n'est pas lue dans le flux : elle reste dans la quarantaine.
5. **Transport propre** : voir le LISEZMOI de la v1.
6. **Neon n'est pas un proposeur.** C'est en attente de la décision de la mère (signalé à 12:36Z).
