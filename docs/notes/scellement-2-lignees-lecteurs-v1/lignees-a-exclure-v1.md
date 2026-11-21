# Lignées de modèles à exclure des deux lecteurs externes du dommage — oracle du cycle 1, scellement 2 du bras d'attaque (famille aveugle de G1) — v1

- Classe C (travail). Écrite le 2026-11-21 vers 17:26 UTC (`date -u`) par un sous-agent Opus 5.5 neuf, qui ne conçoit aucun moniteur, pour le monteur de l'oracle (N-060 v3, point 1 : deux lecteurs « de deux familles de modèles autres que celles des moniteurs évalués »).
- Règle suivie : noms de famille de modèle et rôle seulement ; aucune couche, aucun seuil, aucune invite, aucun trait, aucune valeur ; rien lu sous `donnees/` ni dans le coffre.
- Empreintes (16 premiers signes, compagnons vérifiés pour les quatre premières et la note du bras A) : N-053 `2204256d744288be` ; N-056 `3592c1e977e8c38c` ; N-060 v3 `2b448f696503112c` ; N-029 `084e30523c0a0349` ; N-054 `c8a00b3f885ae3e9` ; N-057 `42180088efb2e101` ; N-061 `b2ae441720665ed4` ; note des familles du bras A `1753a9d94f8a2c40` ; index du scellement 2 `5d0479b437426509` ; règle du bras d'attaque (branche `claude/scellement-2-familles-aveugles-v1`) `88418df09c2e969c` ; rapprochement des trois voix `813f3b305ad52a18`.

## Familles qui servent à un moniteur, un juge ou une base de G1 et du bras d'attaque

| famille (fournisseur) | rôle, en trois mots | source, chemin:ligne |
|---|---|---|
| Llama (Meta) | agent lu, sabotant | `prereg/T0.6-organismes-config-7b-v1.json`:17-18 ; note des familles du bras A, `docs/notes/bras-a-contre-lecture-habilitee-v1/familles-moniteurs-agent-bras-a-v1.md`:16 |
| Llama (Meta) | moniteur boîte noire | `registres/decisions.md`:376 (D1, deux options de la famille) ; `docs/decisions/decision-N-029-v1.md`:20-22 ; `registres/go.md`:456 (GO-2026-11-19-23) |
| Llama (Meta) | sondes lisent l'agent | `docs/decisions/decision-N-056-v1.md`:38-46 et 52-53 (boîte blanche et ses deux bases sur les mêmes sondes, qui lisent l'agent) |
| Qwen (Alibaba) | juge autre lignée | `docs/decisions/decision-N-053-v1.md`:33-34 ; `registres/go.md`:456 ; `docs/notes/couche-2-preparation-v1/verite-dommage-v1/rapprochement-trois-voix-v1.md`:239-240 |
| aucune (sans modèle de langue) | prédicteur traits texte | `docs/decisions/decision-N-029-v1.md`:23-27 |
| non nommée | juge ouvert, plafond | `docs/decisions/decision-N-029-v1.md`:28-30 (non décidé, GO à part, famille non dite) |

Borne écrite : `docs/decisions/decision-N-060-v3.md`:24-25 (« ni Llama ni Qwen ») ; reprise en `docs/notes/bras-a-contre-lecture-habilitee-v1/familles-moniteurs-agent-bras-a-v1.md`:38. Comparateurs de G1 dans chaque mode : `prereg/bras-attaque-regle-v1.md`:131 (branche ci-dessus). Le préenregistrement de la porte G1 n'est pas scellé sous `prereg/` ; seule l'étude par simulation des formulations l'est (`prereg/formulation-g1-simulation-v1.md`, `d04da7903b89d083`), qui ne nomme aucune famille de moniteur.

## Lignée du juge

**Qwen.** Source : `docs/decisions/decision-N-053-v1.md`:33-34 (« Juge d'une autre lignée »), confirmée `registres/go.md`:456 (« Le juge Qwen garde le regard d'une autre lignée »).

## Liste d'exclusion proposée

Llama ; Qwen.

## Incertitudes

1. Le mandat écrit « ni Llama, ni Qwen, ni la lignée du juge » : si « le juge » est celui de G1, c'est Qwen (redondance). S'il désigne le juge du bras d'attaque (lecteur des recettes), aucune pièce lue ne fixe sa famille : sa désignation et celle du second juge sont attendues de Lazar (`prereg/bras-attaque-regle-v1.md`:324-325 et 394-395). À faire préciser par la mère avant le choix.
2. « Juge » au sens du moniteur boîte noire : le juge de la taille de l'agent et le juge plus petit sont tous deux Llama (`registres/decisions.md`:376) ; le rapprochement les dit « juge 8B » et « juge 3B à vérifier » (`…/rapprochement-trois-voix-v1.md`:68-69, 246). Exclus de toute façon par Llama.
3. Claude (Anthropic) n'est exclu par aucune règle lue, mais l'auteur de la famille aveugle du cycle 1 est une instance Claude Fable (pièce 1, `docs/notes/scellement-2-familles-aveugles-v1/piece-1-attestation-aveuglement-v1.md`:3-4, même branche) et N-060 v3 (`docs/decisions/decision-N-060-v3.md`:34-35) veut l'oracle inaccessible à cet auteur ; le rapprochement admet Claude « parenté déclarée » (`…/rapprochement-trois-voix-v1.md`:69). Si un lecteur Claude est retenu : instance distincte, parenté avec l'auteur déclarée ; un lecteur hors Claude l'évite.
4. Gemini (Google) : non exclu ; il a servi côté attaque ailleurs (collisionneur, `docs/decisions/decision-N-057-v1.md`:17 ; mode antérieur du bras d'attaque, `docs/notes/bras-attaque/index-ba002-parametres-modes-v2.md`:10), pas comme moniteur de G1. Au bras A, un modèle Gemini juge les ancres (`docs/decisions/note-neon-dans-l-organisme-v1.md`:11, 32) : siège à ne pas réemployer ici sans le dire.
5. Le juge ouvert de grande taille (N-029, point 3) et Llama Scope (N-061, `docs/decisions/decision-N-061-v1.md`:12, outil de T0.7) n'entrent pas dans la liste scellée de G1 sans nœud à part ; si l'un y entre, sa famille s'ajoute à l'exclusion.
6. La famille exacte de l'attaquant informé n'est établie par aucune pièce lue.
