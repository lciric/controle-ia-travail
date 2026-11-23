# Seconde vérification courte (R1, R2) : relance courte de la machine 61875617 (contre-lecteur 1, classe B)

Contre-lecteur : Claude Opus 5.5, le même que pour les deux pièces précédentes. Heure : 2026-11-22, vers 11:52Z. Aucun appel au vrai loueur.

## Verdict : jouable.

## Empreintes (conformes à l'annonce)

| fichier | sha256 |
|---|---|
| `relance-courte-61875617-v2.sh` | `97f4e627102158a5768d0d795e16c08707f956766ef874805d7f49cc9f85ddeb` |
| `texte-relance-courte-61875617-v1-brouillon3.md` | `f106f712206c18191bbdffa62cb468d733ff715161e968d5350068d81f995132` |
| `essais-blanc-relance-courte-v2.txt` | `9cd18a2ff931aad21e713e4da13d1391c6898dbc13b39e209430d9ea62af83b4` |
| `differences-brouillon2-vers-3.md` | `6c228f5fca9d9eace2817dbdfbb87087723a3e32f8754848f67548ccc801152b` |

Le texte cite le script v2 et son empreinte (l. 6, 78, 80) ; il ne renvoie plus nulle part au script v1.

## Les deux corrections et les changements entre le script v1 et le script v2

Le `diff` entre les deux scripts ne touche que cinq endroits : l'en-tête, `etat()`, le délai de `logs`, le comptage des relevés illisibles et l'ordre de l'arrêt dans la boucle.

- **R1 (arrêt avant la lecture d'état)** : un arrêt décidé par le tri du journal part aussitôt, avant `etat` (l. 83-84 de la v2). L'ancien traitement de l'arrêt à cet endroit est retiré ; seul le cas `DEMARRAGE` reste (l. 89). Le délai de `show instances` est de 30 s dans la boucle et de 120 s ailleurs. Le délai de `logs` passe de 60 à 30 s.
- **R2 (relevés illisibles)** : ils ne sont comptés qu'une fois `RUN_VU` posé, c'est-à-dire une fois la machine vue en marche (l. 79-81).
- **Aucune régression** : l'identifiant, l'absence de `destroy`, le start unique, les deux `stop` au plus, les bornes et la garde des secrets sont inchangés.

## Essais A, B, C et F rejoués sur la v2 avec mon faux outil (`scratchpad/verif-cl1-essais/`)

| essai | cas | résultat | appels | appel juste avant le premier `stop` |
|---|---|---|---|---|
| A | sain | arrêt confirmé sur « poussée faite », code 0 | 1 start, 1 stop | `logs` (R1 tenu) |
| B | tentative 1 refusée, puis poussée | arrêt confirmé sur « poussée faite », au 3e relevé | 1 start, 1 stop | `logs` |
| C | machine en `loading` deux relevés, puis `running` ; relevés illisibles | illisibles non comptés pendant `loading`, comptés ensuite ; arrêt au 3e illisible compté (relevé 6) | 1 start, 1 stop | — |
| F | poussée impossible, arrêt jamais confirmé | arrêt non confirmé, code 1 | exactement 2 stop | — |

Aucun appel interdit sur ces quatre essais.

## Remarque sans effet sur le verdict

Le comptage des relevés illisibles a un tour de retard : `RUN_VU` est posé par la lecture d'état, qui vient après le relevé du journal. Cela fait environ 5 à 10 s de plus avant l'arrêt sur une veille aveugle. C'est acceptable dans la fenêtre d'environ 180 s, à condition que la latence d'arrêt mesurée au préalable P10 tienne sous 90 s.
