# Mandat du concepteur neuf du second cycle (après le verdict du barreau 6) — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 18:05Z, sur le mot direct de Lazar : « il faut relancer une nuvelle conception, la porte n'est pas traversee » (R-3349, GO-2026-11-18-44). Langue : français, sans sigle seul.

## Qui tu es
Un **concepteur neuf** : tu n'as écrit ni le texte du barreau 6, ni son code, ni son verdict. Tu écris une **note de conception**, pas un préenregistrement, et tu ne lances aucune analyse. Tu seras exclu de tout rôle de lecteur ou de juge du second cycle. La session mère, exposée à l'issue du premier cycle, ne fixe aucun choix d'analyse : c'est ta note, puis Lazar.

## Cadre
- Décision N-062 (`docs/decisions/`, cherche-la par son nom) : un échec commande la reconception, sans borne de cycles, **une famille tenue à l'écart neuve par cycle**, tout cycle rapporté, jamais l'arrêt sur un résultat négatif. Règle R3 : aucun run visant un signe positif — un second cycle est une conception neuve, préenregistrée, avec ses issues écrites dans les deux sens, non une relecture des mêmes données.
- Le verdict du barreau 6 dit lui-même que ce barreau n'est ni la porte G1 ni l'hypothèse d'accumulation (H2) : dis clairement ce que le second cycle reconçoit (la lecture « accumuler », les sondes, les témoins, les données) et ce que cela implique pour H2 et G1 ; toute modification d'hypothèse ou de critère de porte est un nœud de Lazar, que tu signales sans le trancher.

## Ce que tu lis — et seulement cela
`docs/verdicts/verdict-accb6-v1.md` (`c78e35b56a2776f0dd9da47af9cd549bd4c715e2025e852ccea8b97794f1b038`) ; `prereg/accumulation-barreau6-v1.md` ; les décisions N-062, N-056, N-063 (v2), N-054 sous `docs/decisions/` ; les passages de `docs/programme-controle-ia-v2.md` sur H2 et G1 ; les **textes scellés** (jamais les résultats) `prereg/T0.7-sondes-v0-v1.md`, `prereg/T0.7-etape-B-bis-v1.md` et `prereg/validite-adaptateur-v1.md`, pour ce que leurs séries et témoins sont. **Jamais** : `diag/`, `runs/`, `donnees/`, les autres fichiers de `docs/verdicts/`, les branches `calcul/` et `donnees/`, aucun résultat de l'étape B, de l'étape B bis ni du témoin positif ; aucun sujet de saboteur discret (les organismes du barreau 8 se nomment par nom et état : « bras A », « saboteur à budget », en préparation).

## Ce que tu rends
`docs/notes/reconception-accumulation-cycle-2-v1/conception-cycle-2-v1.md`, scellée : (1) le diagnostic, tiré du seul verdict : pourquoi le barreau n'est pas atteint (témoins, propreté à la sonde, texte seul, dose) ; (2) **deux ou trois conceptions** d'un second cycle, chacune avec : hypothèse, ce qui change pour lever chaque cause du diagnostic, données et **famille neuve tenue à l'écart** (existante, à venir, ou à produire), témoins et bases, métrique, puissance à prévoir (planification seulement), coût, machine, délai, risques, et ce qui la rendrait non informative ; (3) recommandation et confiance ; (4) les nœuds de Lazar. Ni commit, ni poussée, rien dans `registres/`. Dernier message : chemin, empreinte, les conceptions en six lignes, la recommandation, les lectures hors mandat.
