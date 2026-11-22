# Lecture de la page officielle des modèles d'Anthropic — v1

Lue le 2026-11-22T11:53Z par la session de l'organisme. Adresse : https://docs.anthropic.com/en/docs/about-claude/models/overview, redirigée (301) vers https://platform.claude.com/docs/en/about-claude/models/overview, page gardée telle quelle : `platform-claude-com-models-overview-2026-11-22.html`. Aucune date n'est affichée sur la page.

| modèle (tableau « All models ») | contexte | sortie maximale | entrée | sortie |
|---|---|---|---|---|
| Claude Opus 4.6 | 1M | **128K jetons** | 5 USD / MTok | 25 USD / MTok |
| Claude Sonnet 4.6 | 1M | **128K jetons** | 3 USD / MTok | 15 USD / MTok |

- La sortie maximale vaut pour l'interface des messages synchrone. Par l'interface des lots, jusqu'à 300K avec un en-tête bêta : ce n'est pas employé ici.
- Les identifiants `claude-opus-4-6` et `claude-sonnet-4-6` ne figurent pas dans ce tableau ; ils sont pris de la référence de l'outil de l'interface.
- **Effet** : le plafond de sortie de 96 000 jetons du devis de la passe X tient sous la sortie maximale des deux modèles. La crainte d'un plafond à 64 000 pour Sonnet 4.6 est levée.
