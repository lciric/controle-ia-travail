# Essais de la mémoire, pistes 1 et 2 — lecture (exploratoire, non opposable, lue dans les deux sens)

Lignée conv-audit (instance nouvelle), 27 octobre 2026, écrit à partir de 08:38 UTC (heure lue sur `date -u`). Plan
`plan-essais-memoire-v1.md` (`ac0354ad…`, poussé avant tout lancement, commit `8edfaf7`) ; script `essais_memoire_v1.py`
(commit `c949781`) ; résultats `resultats-v1/conforme/` (conforme au plan, graine 20261028, 2 min 5 s) et
`resultats-v1/variante-B/` (variante déclarée, voir piste 2). Deux essais de fumée avant (2 courses chacun, non retenus).

## Verdict

1. **Une signature prédictive bat de loin le texte** pour reconnaître une redite ; mais **la signature brute** (la piste
   de l'instance sortante) fait aussi bien que ma signature invariante, et mieux sur le mélange aveugle : mon idée
   d'invariance n'apporte rien ici. Je la retire au profit de la signature brute.
2. **Hériter de la preuve vaut mieux que refuser** : mêmes fausses découvertes (0,05 par course), plus de vraies
   (+ 0,06 au plan, + 0,50 quand la première tentative est trop sûre d'elle) ; ne rien faire augmente les fausses
   découvertes de 70 %.

## Piste 1 — redites manquées par famille, à 5 % de fausses fusions (moitié de mesure, 200 paires par famille)

| famille | texte (Jaccard) | signature brute | signature invariante |
|---|---|---|---|
| paraphrase, copie renommée, jargon rare, changement d'échelle | 1,000 chacune | 0,000 chacune | 0,000 chacune |
| biais par issue | 1,000 | 0,025 (5) | 0,000 (0) |
| mélange avec une loi aveugle | 1,000 | **0,035 (7)** | 0,125 (25) |
| fausses fusions réalisées (vraies différences) | 0,000 | 0,060 | 0,050 |
| variante quantitative fusionnée (logits × 2) | 0,000 | 1,000 | 1,000 |

- Le texte simulé est grossier (il ne dit que le sens des effets) : deux lois différentes ont souvent le même texte, si
  bien qu'à 5 % de fausses fusions son seuil monte à 1 et il ne fusionne plus rien. Ce chiffre dit qu'un texte peut être
  identique pour deux hypothèses différentes ; son ampleur est un artefact du générateur.
- Prédictions : tenues pour le texte (il manque tout) et pour la variante quantitative (fusionnée par les deux
  signatures) ; **non tenues** pour la signature brute (je prédisais qu'elle manquerait le mélange et le biais : elle
  n'en manque que 3,5 % et 2,5 %) ; la signature invariante tient sa prédiction (mélange ≤ 0,3) mais elle est **moins
  bonne** que la brute sur le mélange (intervalles de Wilson disjoints) et pas significativement meilleure sur le biais.
  Le critère « ce qui contredirait le brainstorm » du plan est rempli.

## Piste 2 — politiques face aux retentatives (200 courses de 40 hypothèses, environ 4 vraies par course)

| première tentative d'une vraie | politique | fausses par course | vraies par course | tests par course |
|---|---|---|---|---|
| trop faible (× 0,3, plan) | rien | 0,085 | 4,040 | 93,5 |
| | refus | 0,050 | 3,985 | 40,0 |
| | héritage | 0,050 | 4,040 | 93,5 |
| trop sûre d'elle (× 3, variante B) | rien | 0,085 | 3,975 | 94,1 |
| | refus | 0,050 | 3,310 | 40,0 |
| | héritage | 0,050 | 3,810 | 94,3 |

- Rien − refus, fausses : + 0,035 [+ 0,010 ; + 0,060] (les deux variantes) : réessayer jusqu'à la chance gonfle les
  fausses découvertes ; l'essai a des dents (R5).
- Héritage − refus, fausses : 0,000 [0 ; 0] ; vraies : + 0,055 [+ 0,025 ; + 0,090] au plan, + 0,500 [+ 0,400 ; + 0,605]
  en variante B. Prédictions tenues.
- Coût de l'héritage : quand la première tentative est très fausse sur l'effet (trop sûre d'elle), sa classe part de
  très bas ; « rien » retrouve 0,165 vraie de plus par course (+ 0,115 à + 0,220), au prix de fausses découvertes en plus.
- **Variante B, déclarée** : ajoutée après l'essai de fumée, qui montrait qu'à × 0,3 presque toutes les vraies passent dès
  la première tentative (la piste n'aurait pas eu de dents sur les vraies) ; seule l'option de la première tentative change.

## Ce que cela change pour la mémoire

- Identité d'une entrée : la **signature brute** sur une sonde fixe tenue hors de la vue des agents ; seuil réglé sur des
  paires de vraies différences ; la variante quantitative est fusionnée — c'est l'héritage qui lui laisse sa chance.
- Politique : **héritage de la preuve**, pas de refus. Reste à écrire : la classe d'une fille (avec ses parents), et la
  piste 3 (un proposeur qui lit la mémoire, contre mémoire placebo).
- Limites : lois softmax synthétiques, deux traits, textes simulés ; aucune mesure d'effet sur de vrais agents.
