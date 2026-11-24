# Diagnostic — rejeu de la contre-vérification sur l'échantillon de l'extraction des 96 — v1

Pièce de classe C, 2026-11-24. Il fait suite au bilan d'arrêt (`bilan-arret-extraction-banque-v1.md`, option (a), accordée par la mère comme routine : aucune règle changée, aucune dépense).

## Verdict

**Dérive de l'extracteur, non du juge.** Le contre-vérificateur d'aujourd'hui, avec la même consigne scellée et la même mécanique, a jugé les 16 énoncés de l'échantillon de l'extraction des 96 (sorties scellées d'octobre). Il en accepte 16 sur 16 : 0 échec, comme en octobre. Sur la banque neuve, il en refusait 12 sur 16, tous pour « énoncé qui révèle ce que H.9 interdit ». Le juge ne refuse donc pas l'ancienne banque : les énoncés écrits aujourd'hui sont plus révélateurs que ceux d'octobre.

## Énoncé par énoncé

| papier | rejeu | octobre | cibles défectueuses (rejeu) |
|---|---|---|---|
| 2506.16404v3 | passe | passe | 0 / 12 |
| 2509.03810v2 | passe | passe | 1 / 11 |
| 2509.21513v3 | passe | passe | 0 / 11 |
| 2509.24912v2 | passe | passe | 0 / 10 |
| 2510.02692v3 | passe | passe | 0 / 12 |
| 2510.02779v4 | passe | passe | 1 / 12 |
| 2510.24709v2 | passe | passe | 0 / 11 |
| 2512.00930v1 | passe | passe | 0 / 11 |
| 2512.01199v1 | passe | passe | 0 / 12 |
| 2512.02017v1 | passe | passe | 0 / 12 |
| 2512.11131v1 | passe | passe | 2 / 12 |
| 2602.00987v1 | passe | passe | 0 / 12 |
| 2603.00054v1 | passe | passe | 0 / 11 |
| 2603.11047v1 | passe | passe | 0 / 11 |
| 2604.05112v1 | passe | passe | 1 / 11 |
| 2605.29097v2 | passe | passe | 1 / 10 |

Raison commune : aucun motif d'échec. Énoncé non révélateur, classification juste ou à un cran près, au moins 3 contrôles fondés et observables, au moins une direction féconde fondée. Les raisons détaillées des avis portent du texte des papiers ; elles restent sous `donnees/20261124-133630-rejeu-contre-verification-96/`.

## Pièces

- Manifeste : `runs/20261124-133630-rejeu-contre-verification-96/manifeste.json` ; préparation et lecture : `diag/20261124-133630-rejeu-contre-verification-96/` (lecture `448b3477…`).
- Textes régénérés par la chaîne scellée, empreintes du corpus du 6 octobre vérifiées (16 sur 16).
- Code : `src/controle_ia/environnements/rejeu_contre_verification_banque_v1.py`. Contre-lu par un autre modèle (« utilisable en l'état », `rapport-contre-lecture-rejeu-v1.md`). Errata CL-R4 et CL-R7 portés avant la lecture. CL-R1 est sans effet : 0 retour chariot dans les 16 textes.
- Sous-agents : modèle nommé explicitement à l'appel (demande de la mère). Son identifiant n'est pas écrit dans le dépôt (consigne de la plateforme) ; il est nommé à la mère hors du dépôt.

## Réserves

- **Pas les mêmes papiers.** Le rejeu porte sur les énoncés d'octobre de 16 papiers, la banque neuve sur 16 autres. La différence pourrait tenir en partie aux papiers eux-mêmes. Mais 0 sur 16 contre 12 sur 16 (deux tirages du même vivier) rend une cause « papiers » très improbable.
- **Les modèles ont changé entre octobre et aujourd'hui.** Les énoncés d'octobre ont été écrits par un autre extracteur, et jugés en octobre par un autre contre-vérificateur. Le rejeu tient le juge fixe : la dérive est imputable à l'extracteur d'aujourd'hui, non au juge.
- **Conséquence pour le nœud de Lazar.** L'option (c), extraire avec le modèle d'octobre s'il est encore servi, viserait directement la cause. L'option (b), une version 2 de l'invite de l'énoncé, corrigerait la cause par la règle. Les deux sont des changements de règle ou de modèle, soumis à Lazar.
