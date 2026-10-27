# Essais de la mémoire, piste 3 — un proposeur qui lit la mémoire — lecture v1 (exploratoire, non opposable, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 11:26 UTC (heure lue sur `date -u`). Sans
préenregistrement (mot de Lazar, 12:02 heure de Paris) ; plan, lecture et prédictions dans l'en-tête du script
`essais_memoire_piste3_v1.py` (`c8353a5e…`), poussé avant le lancement (commit `b720bdc`). Graine
176238914913698272559241769767042812787 (`numpy.random.SeedSequence().entropy`) ; 60 courses par type de monde ;
exécution de 11:11:56 à 11:25:30 UTC ; résultats `resultats-piste3-v1/` (manifeste poussé avant le calcul, commit
`30c2b37`). Un essai de fumée avant (2 courses, graine 1, non retenu).

## Verdict

1. **Lire la mémoire double les découvertes quand le monde a une structure** : pour le même budget (200 tests), la
   mémoire complète trouve 24,0 vraies associations par course, contre 12,8 avec la mémoire placebo et 11,8 sans
   mémoire (+ 11,2 sur le placebo, intervalle [+ 9,8 ; + 12,5]). Ce qui aide, c'est le **contenu** de la mémoire : la
   même politique nourrie de la mémoire d'une autre course ne fait pas mieux que le hasard (+ 1,0 ; [− 0,2 ; + 2,2]).
2. **L'essai a des dents** : quand la même vérité est dispersée sans structure (monde permuté), l'avantage des
   marchepieds disparaît (+ 0,7 sur « redites seulement », [− 0,3 ; + 1,6]). Seul reste le gain d'éviter les redites
   (+ 2,9 sur « sans mémoire », [+ 2,1 ; + 3,7]) : sans mémoire, 40 tests sur 200 partent en redites.
3. **Le prix** : la lecture structurée concentre les découvertes. Dans le monde permuté, elle couvre moins de régions
   que « redites seulement » (8,6 blocs contre 9,9 ; − 1,3, [− 1,9 ; − 0,7]) ; il faut garder une part d'exploration.
   Les fausses découvertes restent rares pour tous (au plus 0,22 par course) : le registre avec héritage les tient.

## Chiffres (moyennes par course ; 36,5 vraies associations par monde sur 400)

| monde | proposeur | vraies | part trouvée | fausses | redites | blocs | puissance du 1er essai |
|---|---|---|---|---|---|---|---|
| groupé | sans mémoire | 11,8 | 0,32 | 0,07 | 39,8 | 6,7 | 0,80 |
| groupé | mémoire, redites seulement | 14,4 | 0,39 | 0,17 | 0,5 | 7,6 | 0,78 |
| groupé | **mémoire complète** | **24,0** | **0,66** | 0,08 | 0,7 | 7,5 | 0,88 |
| groupé | mémoire placebo | 12,8 | 0,35 | 0,10 | 35,8 | 6,9 | 0,79 |
| permuté | sans mémoire | 11,5 | 0,32 | 0,18 | 39,3 | 8,1 | 0,79 |
| permuté | mémoire, redites seulement | 14,4 | 0,39 | 0,22 | 0,6 | 9,9 | 0,79 |
| permuté | mémoire complète | 15,1 | 0,41 | 0,17 | 0,3 | 8,6 | 0,80 |
| permuté | mémoire placebo | 12,2 | 0,33 | 0,13 | 36,3 | 8,7 | 0,81 |

Différences appariées par course (vraies ; intervalle à 95 % par rééchantillonnage des courses) :

| différence | groupé | permuté |
|---|---|---|
| complète − placebo | + 11,2 [+ 9,8 ; + 12,5] | + 2,9 [+ 1,9 ; + 3,9] |
| complète − redites seulement | + 9,6 [+ 8,7 ; + 10,6] | + 0,7 [− 0,3 ; + 1,6] |
| redites seulement − sans mémoire | + 2,5 [+ 1,7 ; + 3,4] | + 2,9 [+ 2,1 ; + 3,7] |
| placebo − sans mémoire | + 1,0 [− 0,2 ; + 2,2] | + 0,7 [− 0,2 ; + 1,6] |

## Lecture et prédictions (fixées avant le lancement)

- Critères 1 (contenu), 2a (structure, monde groupé), 2b (disparition en monde permuté), 3 (placebo sans apport, deux
  mondes) : remplis ; 5 (trop beau, plus de 95 % trouvées) : non (0,66).
- Prédictions : toutes tenues (complète − placebo ≥ + 5 : + 11,2 ; complète − redites seulement ≥ + 3 : + 9,6 ; permuté,
  écart ≤ 1,5 en valeur absolue : 0,7 ; placebo − sans mémoire dans ± 1,5 : + 1,0 et + 0,7).
- **Pourquoi la mémoire complète gagne en monde groupé**, en deux parts : elle teste les voisines des promues (60 % de
  vraies près d'un foyer, contre 2 % ailleurs) et elle y suppose la force estimée de la promue (forces voisines dans un
  foyer) : sa puissance au premier essai monte à 0,88 contre 0,78. En monde permuté, les deux parts disparaissent
  (0,80) : c'est cohérent.
- **Audit de propreté (R4)** : toutes les prédictions tenues, mais elles suivaient l'essai de fumée (déclaré) ; rien de
  « trop beau » au sens du critère 5. La part de la puissance du premier essai est un mécanisme voulu, pas une fuite :
  la force estimée vient des tirages du test de la promue, jamais du monde.

## Ce que cela dit, et ce que cela ne dit pas

- **Dit** : avec un proposeur qui sait lire, la mémoire améliore les propositions **si et seulement si** les vraies
  associations se regroupent dans l'espace où le proposeur mesure la proximité. Éviter les redites rapporte toujours
  (+ 2,5 à + 2,9 vraies, 20 % du budget récupéré).
- **Ne dit pas** : que la vérité se regroupe dans le monde réel. C'est la condition à vérifier sur données réelles. La
  rétrodiction sur arXiv (2003-2016, `../retrodiction-swanson/`) permet de mesurer si les associations qui ont réussi
  se regroupent dans un espace de concepts : à faire avant de bâtir sur ce résultat.
- **Limites** : proposeur scripté (de vrais agents lisent mal, ou trop) ; voisinage connu exactement (dans la réalité,
  la proximité du proposeur est bruitée : l'essai suivant doit ajouter une part de « fausses voisines ») ; quatre foyers
  seulement ; 200 tests par course.
- **Pour la mémoire du pôle** : signature brute + héritage de la preuve (pistes 1 et 2) + archive lue par marchepieds
  autour des survivantes, avec une part d'exploration réservée (contre la concentration, point 3 du verdict).
