# Erratum 1 au compte rendu de la course des renvois — relance de l'exploration Opus 5.5

Relance déclarée après troncature, sur décision de la mère (2026-11-22T18:22Z, étage 2 de la chaîne, autonomie GO-2026-11-22-106), sous GO-2026-11-22-103, programme renvois_api_v5.py vérifié conforme par le contre-lecteur Sonnet. Écart déclaré dans la ligne d'ouverture du journal : effort high au lieu de xhigh.

| demande | modèle servi | effort | fin | entrée / sortie (jetons) | coût réel (USD) | issue |
|---|---|---|---|---|---|---|
| exploration (relance) | claude-opus-5-5 | high | end_turn | 963 / 42 554 | 0,854932 | rendue |

- Dépense totale des renvois : 6,271392 + 0,854932 = 7,126324 USD, plus quelques jetons d'essais (garde de départ, essai d'effort), sur 17,50.
- Les quatre réponses sont versées sans lecture sur prep/quarantaine-renvois-api-v1 (4cf6e017) : flux/ (première course) et flux-relance-effort-high/ (relance). La réponse coupée de la première course reste versée (R12).
- Faux échec à inscrire à la veille de cap : exploration Opus 5.5, première course, « non évaluable » (troncature), relancée, issue « verdict valide » à l'effort high.
