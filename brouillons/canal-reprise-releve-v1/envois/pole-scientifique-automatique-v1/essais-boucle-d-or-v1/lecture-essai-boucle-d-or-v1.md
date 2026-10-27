# Essai « Boucle d'or » v1 — lecture (exploratoire, non opposable, lue dans les deux sens)

Lignée conv-audit (instance nouvelle), 27 octobre 2026, écrit à partir de 08:37 UTC (heure lue sur `date -u`). Plan
`plan-essai-boucle-d-or-v1.md` (`f2653da3…`, poussé avant tout lancement, commit `de4dbf6`) ; script
`simuler_boucle_d_or_v1.py` (empreinte dans son `.sha256`, commit `c949781`) ; résultats `resultats-v1/` (exécution
conforme au plan : 30 répétitions par monde, budget 40, graine 20261027 ; 9 min 35 s sur un cœur ; 19 191 évaluations
du juge v1). Un seul essai de fumée avant (2 répétitions, budget 10, non conforme, non retenu).

## Verdict (règle du plan) : « à garder sous condition » — pas d'adoption

1. La fenêtre de Gemini ne gagne que dans le monde construit comme elle le suppose : + 0,23 découverte vraie par dollar
   contre le meilleur allocateur appris dans « cloche », mais − 0,34 dans « bords » et − 0,24 dans « croissant ».
2. Un tri par espérance de découvertes, appris en ligne sans rien savoir, bat le hasard dès que la valeur dépend de la
   distance et ne perd jamais gros : c'est le défaut sûr ; la fenêtre ne vaut que si l'on sait d'avance où est la valeur.
3. Le juge v1 n'a promu aucune fausse fille (formes du nul) dans aucun monde : ici, la trivialité est bien écartée par le
   juge, pas par l'allocateur.

## Chiffres (découvertes vraies par dollar, moyenne sur 30 répétitions ; intervalles à 95 % par rééchantillonnage)

| monde | hasard | Thompson | tri | fenêtre | fenêtre − meilleur appris (tri) | fenêtre − hasard |
|---|---|---|---|---|---|---|
| cloche | 0,124 | 0,170 | 0,251 | 0,481 | + 0,230 [+ 0,186 ; + 0,273] gagne | + 0,357 gagne |
| bords | 0,185 | 0,287 | 0,391 | 0,052 | − 0,338 [− 0,373 ; − 0,302] perd | − 0,133 perd |
| croissant | 0,316 | 0,405 | 0,432 | 0,193 | − 0,239 [− 0,283 ; − 0,194] perd | − 0,123 perd |
| décroissant | 0,341 | 0,361 | 0,438 | 0,444 | + 0,007 [− 0,031 ; + 0,043] indistincte | + 0,103 gagne |
| plat | 0,201 | 0,188 | 0,207 | 0,193 | − 0,014 [− 0,045 ; + 0,017] indistincte | − 0,008 indistincte |

## Prédictions (plan) : tenues ou non

- Tenues : « cloche » gagne contre le hasard et contre les appris ; « bords » et « croissant » perdent ; « plat »
  indistinct ; verdict d'ensemble « à garder sous condition ».
- **Non tenue** : « décroissant » (lointains meilleurs) devait perdre ; la fenêtre y est indistincte du tri, parce que
  sa bande (similarité 0,12 à 0,26) est proche de la région la plus riche de ce monde. La fenêtre ne perd que là où la
  valeur est loin d'elle.
- Contrôle de dents : Thompson bat le hasard dans trois des quatre mondes non plats (indistinct dans « décroissant ») ;
  l'essai départage donc quelque chose. Thompson est partout derrière le tri : avec 40 tests et huit cases, explorer
  coûte plus que ce qu'il rapporte.

## Limites

- Mondes synthétiques ; la similarité est une étiquette du monde, pas une mesure sur des fiches ; coût constant par test.
- Les fausses filles sont des formes contenues dans le nul : le trou « parent + loi aveugle » est exclu (dit au plan) ;
  avec lui, les allocateurs appris seraient récompensés par de fausses promotions.
- La fenêtre d'Uzzi sur données réelles reste à tester (citations : OpenAlex avec une clé, décision de Lazar) ; la
  rétrodiction arXiv peut déjà ranger les paires par distance et tester la cloche, sans dépense.
