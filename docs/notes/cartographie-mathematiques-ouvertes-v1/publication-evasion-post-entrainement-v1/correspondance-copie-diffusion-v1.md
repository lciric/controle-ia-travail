# Copie de diffusion du manuscrit du papier D, v1 — table de correspondance

- **Date** : 24 novembre 2026. Classe C. Préparée par la session fille 2 du papier D ; tâche du calendrier « copie de diffusion sans trace interne » (programme v3, section 7.2, tâche 5). **Rien n'est diffusé** : la diffusion attend le geste de Lazar, et le correctif de revendication décidé pour après le 1er décembre (GO-2026-11-24-38) devra être porté à cette copie avant toute diffusion.
- **Source** : `manuscrit-arxiv/main-v4-correctif-5-erratum-1.tex`, avec ses trois scripts compagnons et la page de dépôt `github-page/README-v4-correctif-5-erratum-1.md`.

| Copie de diffusion (`copie-diffusion-v1/`) | Source interne |
|---|---|
| `main.tex`, `main.pdf` | `manuscrit-arxiv/main-v4-correctif-5-erratum-1.tex` |
| `verify_examples.py`, `verify_examples_output.json` | `verifier_exemples_papier_v4_correctif_1.py` |
| `verify_reward_normalization.py`, `verify_reward_normalization_output.json` | `verifier_correctif_3_v1.py`, `exemples-verifies-correctif-3-v1.json` |
| `verify_aggregation_traps.py`, `verify_aggregation_traps_output.json` | `verifier_correctif_4_v1.py`, `exemples-verifies-correctif-4-v1.json` |
| `README.md` | `github-page/README-v4-correctif-5-erratum-1.md` |

**Ce qui change** :
- la note d'auteur ne porte plus l'historique des versions ni les noms internes ;
- les scripts sont renommés, et leurs docstrings sont en anglais pour les deux scripts récents ;
- les sorties ont des noms neutres.

Le texte et les formules sont identiques. Aucun commentaire LaTeX n'était présent.

**Vérifié** :
- `main.tex` compile (deux passes, sans référence indéfinie) ;
- aucune occurrence de « correctif » ni de « corrective » dans la copie ;
- les scripts renommés redonnent des sorties identiques à celles des sources, hors empreinte du script (comparaison des JSON pour les deux scripts récents, code de sortie 0 pour le premier).

**Reste** :
- « [Author Name] », `[LINK_PDF]` et `[LINK_LESSWRONG_POST]` à remplir par Lazar ;
- identifiants des sorties JSON encore en français (« affirmations », « defauts ») ;
- correctif de revendication à porter après le 1er décembre.
