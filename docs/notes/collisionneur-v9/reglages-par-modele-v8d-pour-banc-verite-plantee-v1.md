# Réglages de réflexion et de sortie par modèle dans la v8d, en vue du dossier du banc à vérité plantée

Écrit à 2026-11-22T12:16:27Z (`date -u`). Pièce de travail (classe C), session des collisionneurs. Relevé lu dans le catalogue de `collisionneur_v9_v8d.py` (b7803838…), sans aucun appel. Demande de la mère : tous les modèles en effort maximal, sortie au plus haut admis, aucune réponse coupée (GO-2026-11-22-53). Rien du banc n'est lu ici.

| modèle | identifiant | réflexion envoyée | sortie (relance) | provision de réflexion | texte au-delà de la réflexion | effort maximal ? |
|---|---|---|---|---|---|---|
| Fable 5.2 | claude-fable-5-2 | effort « high », réflexion adaptative | 49 000 (64 000) | 0 | sans objet | **non** : effort « high » codé en dur (`EFFORT`) |
| Opus 5.5 | claude-opus-5-5 | effort « high », réflexion adaptative | 64 000 (64 000) | 0 | sans objet | **non** : même chose |
| Argon | gemini-4-argon | niveau « high » | 65 536 (65 536) | 16 384 | 49 152, au-dessus de 16 000 : conforme | oui pour Argon (« high » est sa profondeur maximale, selon la page citée dans la v8d) |
| Carbon | gemini-4-carbon | niveau « high » | 65 536 (65 536) | 49 152 | 16 384, au-dessus de 16 000 : conforme de justesse | oui (même source) |
| Neon | gemini-4-neon | niveau « xhigh » | 65 536 (65 536) | 32 768 | 32 768 : conforme | oui (« xhigh » est le plus haut ; supposé accepté, jamais envoyé avant le 22 novembre ; il l'a été depuis, sans refus) |
| Astra | gpt-6.2-astra | aucun réglage de raisonnement envoyé | **8 000** (32 000) | 0 | sans objet | **non**, et sortie basse |
| Kimi | kimi-k3.1-pro | aucun | 32 000 (65 536) | 0 | sans objet | relais local absent : inutilisable en l'état |

## Ce que demande « effort maximal, sortie au plus haut admis »
- **Fable et Opus** : effort au niveau le plus haut documenté, et sortie au plafond documenté (64 000 pour Fable, contre 49 000 aujourd'hui).
- **Astra** : réglage de raisonnement au plus haut, et sortie au plafond documenté (8 000 aujourd'hui).
- **Google** : réglages déjà au plus haut de chaque espèce. Si les plafonds montent, la règle de CLAUDE.md (réflexion plus au moins 16 000 jetons de texte) reste à vérifier pour chacun ; Carbon y est tout juste.

Tout cela demande la **v8k** (options `--effort-max` et `--sortie-max`, en préparation), contre-lue puis vérifiée. Les valeurs maximales seront citées depuis les pages des fournisseurs, rien n'est inventé. La table définitive, par modèle, sera écrite avant le départ du dossier.

## Coupure
Dans la v8d, une réponse coupée (fin en MAX_TOKENS, sortie vide) n'est jamais une cellule : relance au plafond relevé, puis dernier recours déclaré chez Google ; code 9 quand il ne reste aucun texte. La règle « une réponse coupée est un défaut, pas une réponse » est donc déjà tenue.
