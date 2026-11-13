# Témoin de Bailey, troisième série — reprise faite, K′ = 8 ; relance (nœud) — 13 novembre 2026

Session `session_01XJ6MgnEhQMZteN9F8a1BST`. Ne se réécrit pas (R12). Suit `…-0747-decision-lazar-bailey-credit-reprise.md`
(`cc6aba57…`). Aucune note lue : `notes-v3.jsonl` et `technique-v3.jsonl` (champ `valeurs`) non ouverts.

## Reprise (lecture 38)
Poste de reprise v3 (175955746) : `reprendre` lancé à 07:50:55Z, code 0 à 08:01:04Z ; redémarrage de 60417353 le temps
du transfert (145 s) ; **transfert complet** (mise en place, contrôle du juge, règle, pilote, principal) dans
`sortie-conduite-v11/reprise-v10-2/`, empreintes comparées et scellées par la reprise ; **instance 60417353 détruite**
(`detruite: true`, inventaire relu à 08:02Z : absente). Poste v3 détruit à 08:02:44Z. D = 14,386 USD (compte prudent,
B = 75). Crédit Vast relevé à 08:02Z : 23,81 USD.

## Run principal (première exécution) — champs techniques seulement
- `sortie-durees-v3.jsonl` : 8 tours complets (0 à 7), de 1 299 à 1 586 s ; dernier fini à 04:03:36Z ; le tour 8 a été
  coupé (compte Vast sans crédit, ≈ 04:21Z).
- Gardes (`journal/gardes-v3.jsonl`) : toutes « passée » (sonde orientée, juge, dépense ×17, par tour ×8, appariement ×8,
  suffixe appris ×8) ; garde de démarrage « configuration effective » passée (K attendu 72).
- Pas d'état d'exécution final (processus tué).

## Issue de la liste d'arrêt (texte l. 338, 371)
Interruption pendant le tour 8 : run tronqué, **K′ = 8 < 20** : **une seule relance entière**, même graine
(1865327867), dossiers neufs, K recalculé par la même règle sur le budget restant (même B, t du pilote), si ce K est
≥ 20 (attendu : ≈ 60, d'après B − D ≈ 60,6 USD et le taux du pilote ; à calculer par la règle). Les notes de la première
exécution restent scellées sans lecture jusqu'à la fin de la relance et le scellement de ses journaux ; seule la relance
porte le verdict.

## Nœud — ce que la relance demande
1. Le mot exprès de Lazar (instance neuve ; la lecture de la condition 7 a expiré à 08:14Z).
2. Du crédit Vast : ≈ 35 à 45 USD pour la relance au taux observé (≈ 1,34 USD/h, ≈ 22 à 26 min par tour), plus la
   mise en place ; crédit actuel 23,81 USD, insuffisant (une relance coupée par le crédit serait une seconde erreur :
   arrêt, pas de verdict, nœud).
3. Du code de lancement : une conduite qui joue la seule relance (mise en place, contrôle du juge, relance du run
   principal avec le t du pilote déjà mesuré) ; à vérifier dans `lanceur_v17` avant tout devis ; si le code ne le
   permet pas tel quel, un addendum (R1, R2).
Recommandation : relance, après crédit d'au moins 50 USD ; confiance moyenne (le chemin de code est à vérifier).
