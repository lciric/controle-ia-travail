# Vérification du différentiel v2 → v3 du lot 11 (passe X) — v1

Aucun appel hors 127.0.0.1, aucune clé lue, aucune dépense. Mes essais : `/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad/v3_artefacts.py` (10 essais, tous passent). Rejeu de la pièce : `/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad/rejeu-piece-v2/`.

## Verdict : CONFORME. Aucun point bloquant, aucune réserve nouvelle.

- Essais : 83 passés. Mutations : 44 tuées, T0 survit. Les deux configurations ont leur empreinte égale à leur compagnon (2360513e…, 321c3b38…).
- **Pièce v2** : le programme rejoué rend une sortie identique à `sortie-former-piece-v2.json` ; les quatre fichiers ont les empreintes scellées dans le module (13928f87…, 706c5eb5…, d762d60d…, 19624e22…). Le programme refuse (sortie en erreur) si les 17 premiers corps ne redonnent pas 39fb4e93 ou si la 18e source n'est pas 3b555174 : rc = 0. Chaque morceau (6 pièces) est contenu dans la pièce entière (X7).
- **Morceaux** : la configuration refuse un morceau servi à OpenAI, Claude ou Kimi (X1, X2), à Google en forme « sans découpe » (X3), la pièce entière à Google en forme « découpe » (X4), et un jeu de trois morceaux incomplet ou doublé par espèce (X5).
- **P_X** : sans découpe 102,85 = 72,60 + 18,15 + 6,05 + 6,05 ; découpe 139,15 = 72,60 + 54,45 + 6,05 + 6,05. La somme de plus de 18,15 est refusée (X6). 18,15 = 3 espèces Google × 6,05 ; 54,45 = 9 tentatives × 6,05 ; Luc : 9 tentatives = 54,45 ≤ 72,60.
- **Neon** : `gemini-4-neon`, niveau xhigh, réflexion 49 152, sortie 65 536 ; la garde Google v3 l'accepte à xhigh et le refuse à high (X8) ; pire 1,05 (< 6,05). Tous les pires (le plus haut 5,03) sont sous 6,05 dans les deux formes.
- **Transport** : `transport_simple` refuse la redirection (le serveur local ne reçoit jamais la clé, X9) ; `main` l'utilise pour la garde de départ et l'essai de réglages (X10).
- **Plan** : 9 couples, égaux à ceux des deux configurations.
- **Reste inchangé** : le diff des modules montre seulement les textes servis par nom, la forme et P_X, la ligne d'ouverture (formes, empreintes, écarts), et le transport. Écart à X-2 de la forme « découpe » : déclaré au LISEZMOI, à accorder.
