# Choix de Lazar — les deux lecteurs et le juge des ancres du texte neuf du bras A (version 2)

Remplace pour la lecture `choix-de-lazar-deux-lecteurs-v1.md` (`e7cdbdfef4bb6ae5d81206ec24a04d5271af6b5aba01acde473d562c8da6cc91`, gardé, R12) et précise la lecture de `choix-de-lazar-juge-des-ancres-v1.md` (`139af8a159f01f829b14f0bb10a330f4edfb03dfec98d62d4899d3d8bd97c735`, gardé). Transcription : session de relance, 2026-11-19T07:36:10Z.

## Mots de Lazar, directs, dans la session de relance, dans l'ordre

1. 2026-11-19T07:32:48Z, événement `00b48d0d-0a14-4ea9-a206-778cb6611fc7` : « je propose d'utiliser un agent neuf pour juger les ancres ».
2. 2026-11-19T07:34:04Z, événement `2b85afbf-0f46-4fe0-a21f-e44db2d52625` : « on peut utulise gpt6.2 et carbon ».
3. 2026-11-19T07:34:24Z, message tapé pendant un tour de la relance (identifiant de source `bdd859b7-1d75-4cd5-b557-a097c84becfc`, relevé au journal local de la session) : « la ou ca coute le plus de credits on prend claude ou carbon ».
4. 2026-11-19T07:34:36Z, de même (identifiant de source `422449a7-881e-4173-9d35-79420b38c679`) : « car gpt coute cher ».

## Lecture de la relance, déclarée (dite à Lazar, qui peut la corriger ; à confirmer par son GO sur le devis des lectures)

- Les deux lecteurs lisent chacun tous les items (au plus 12 960 appels par lecteur, 15 136 avec la révision bornée de la consigne ; brouillon 3, section 6.11) : c'est là que la dépense est la plus forte, et elle est la même pour chacun des deux. Le juge des ancres fait au plus 152 appels.
- Donc : **les deux lecteurs sont un modèle de la famille Claude et le modèle de la lignée Carbon (`gemini-4-carbon`, famille Google)** ; **`gpt-6.2-astra` (famille OpenAI) juge les ancres**, là où il coûte peu. Trois familles distinctes, toutes hors de Llama et Qwen (`docs/notes/bras-a-contre-lecture-habilitee-v1/familles-moniteurs-agent-bras-a-v1.md`, `1753a9d94f8a2c4004a16ef9cdb0c362936ebab439b6f84404ee40916bff6a06`).
- « Agent neuf » pour les ancres se lit alors : un modèle d'une troisième famille, appelé un item à la fois, qui n'a rien vu du texte ni des réponses des lecteurs — et non un sous-agent Claude, puisqu'un lecteur est de la famille Claude.

## Ce que ces mots ne fixent pas (case « lecteurs », avant scellement)

- **Quel modèle Claude** (plusieurs prix), sa version exacte, la clé qui le sert ; versions exactes de `gemini-4-carbon` et `gpt-6.2-astra` telles que servies ; réglages ; tarifs relevés et datés. Le devis des lectures chiffrera côte à côte les combinaisons, dont celle du mot 2 (GPT et Carbon lecteurs), pour que Lazar tranche sur des prix relevés.
- Aucun appel avant le scellement du texte et de la configuration, et avant la ligne de GO.

## Réserves dites à Lazar

- Un lecteur de la famille Claude est de la même famille que les agents qui ont écrit le texte et la consigne ; aucune pièce du dépôt ne l'exclut (liste des familles, dernière note) ; le texte le déclare.
- La décision N-029 a retiré un juge Claude, mais « pour cette référence » seulement (la référence boîte noire de la comparaison avec la boîte blanche ; `docs/decisions/decision-N-029-v1.md`, lignes 32 et 33) : elle ne vise pas les lecteurs de la vérité du dommage, que la décision N-060 v3 veut de familles autres que celles des moniteurs.
