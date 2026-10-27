# Banc de tricheurs contre le juge de v7 — lecture v2 (exploratoire) : le déni de service avec un effet faible

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 16:36 UTC. **La lecture v1** (`304e1c54…`) **reste
entière** ; cette v2 n'ajoute que la ligne T16f, que la v1 demandait (« T16 mal dimensionné : à rejouer avec un effet
faible »). Même graine, même script (version 2 du banc, en-tête mis à jour avant la course), 200 répétitions (100 à
m = 40), course de 16:34 à 16:35 UTC ; résumé : `resultats-v3-t16f/banc-tricheurs-v7.json` (`b9bc998d…`).

## Verdict

**Le déni de service par inondation existe sous e-BH, et il est modéré** : une fiche vraie d'effet faible (poids de la loi
neuve × 0,3) noyée parmi m − 1 fiches fausses garde une puissance de 0,895 seule, 0,88 parmi 10, **0,80 parmi 40**, contre
0,92 à 0,95 par fiche sans correction dans les mêmes courses : la règle de multiplicité coûte environ 12 points de puissance
à m = 40. Le plafond de propositions par génération borne m ; c'est lui qui borne le déni de service.

| m | puissance par fiche (sans correction) | puissance sous e-BH | écart |
|---|---|---|---|
| 1 | 0,895 | 0,895 | 0 |
| 10 | 0,945 | 0,88 | −0,065 |
| 40 | 0,92 | 0,80 | −0,12 |

(Les puissances par fiche varient d'une ligne à l'autre parce que chaque ligne a ses propres tirages ; la comparaison se
lit dans la ligne.)

## Ce que cela change

- Rien au juge : c'est le prix connu d'une garantie sur le taux de fausses découvertes. À dimensionner : avec 12
  propositions par génération plus les témoins et les rejeux, m reste entre 15 et 25 ; un proposeur qui inonde ne peut pas
  dépasser son plafond.
- La version décisive du banc gardera T16f (effet faible) à 1 000 répétitions, à m ∈ {1, 10, 40}.
