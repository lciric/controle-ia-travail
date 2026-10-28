# Essais de la mémoire du pôle — pistes 1 et 2 — plan v1 (fixé avant tout lancement)

Lignée conv-audit (instance nouvelle), écrit le 27 octobre 2026 à partir de 08:28 UTC (heure lue sur `date -u`), d'après
`brainstorm-memoire-encodage-v1.md` (`5c67ee38…`). **Exploratoire (R-522), non opposable, lu dans les deux sens.** Poussé
avant tout lancement. La piste 3 (proposeur scripté qui lit la mémoire) viendra avec son propre plan. Graine maîtresse
**20261028** (exploration), dérivation `graine_derivee` (SHA-256). Juge v1 et lois de `../orchestrateur-pole-v2`.

## Piste 1 — détecteurs de redite, à taux de fausses fusions égal

- **Fiches de base** : 400 lois softmax tirées (trois issues, deux traits, force 1,5), chacune avec un texte tiré d'un
  gabarit (issue visée, sens de l'effet de chaque trait, sous-population, vocabulaire courant).
- **Vraies redites** (six familles, 400 chacune, une par fiche de base) : paraphrase (synonymes, ordre) ; copie renommée
  (noms des traits) ; jargon rare (cinq termes rares ajoutés) ; changement d'échelle des traits (prédictions identiques) ;
  mélange avec une loi aveugle (λ uniforme sur [0,2 ; 0,6], loi aveugle de Dirichlet(1, 1, 1)) ; biais par issue
  (log-biais gaussiens d'écart 0,7). Le texte de chaque transformée est réécrit par la même famille.
- **Vraies différences** : même gabarit de texte, autre loi tirée (le texte ne change que par les sens d'effet qu'elle
  implique). **Variante quantitative**, rapportée à part sans étiquette : même loi, logits multipliés par 2.
- **Détecteurs** : (i) Jaccard des 3-grammes du texte (v0) ; (ii) signature brute : divergence de Kullback-Leibler moyenne
  sur une sonde de 256 instances tirée une fois ; (iii) signature invariante : corrélation de rang moyenne, sur la sonde,
  des log-cotes de chaque paire d'issues.
- **Étalonnage puis mesure** : les 400 fiches sont coupées en deux moitiés tirées au hasard ; sur la première, le seuil de
  chaque détecteur est réglé pour que 5 % des paires « vraies différences » soient fusionnées à tort ; sur la seconde, on
  mesure, au même seuil, le taux de redites **manquées** par famille et le taux de fausses fusions réalisé.
- **Lecture** : un détecteur est meilleur qu'un autre sur une famille si son taux de redites manquées est plus bas et
  que les intervalles de Wilson à 95 % ne se recouvrent pas. **Prédictions** : le texte manque la copie renommée, le
  jargon et l'échelle (≥ 0,5 chacune, 0,8) ; la signature brute manque le mélange et le biais (≥ 0,5, 0,7) ; la signature
  invariante manque moins de 0,1 de chaque famille sauf le mélange (≤ 0,3, 0,6) ; elle fusionne la variante quantitative
  (≥ 0,9, 0,9), ce qui est voulu et motive la piste 2. **Ce qui contredirait le brainstorm** : la signature invariante
  pas meilleure que la brute sur le mélange et le biais, ou plus de fausses fusions réalisées que les autres au même seuil.

## Piste 2 — que faire d'une redite : rien, refus, ou héritage de la preuve

- **Par course** : 40 hypothèses de génération 0 (lois softmax) ; 10 % vraies (le monde suit la loi), 90 % fausses (le
  monde est la marginale aveugle de la loi) ; chacune testée par le juge v1 (ordre secret, urne, 200 tirages frais).
- **Retentatives** : chaque éliminée est reproposée, avec une probabilité 0,5 à chaque génération, au plus trois fois,
  sous une forme de la même classe : pour une fausse, une transformée aveugle de sa loi (biais par issue ou mélange) ; pour
  une vraie, une hypothèse vraie engagée d'abord **trop faible** (logits × 0,3) puis reproposée à sa force juste. La classe
  est connue de la simulation (la piste 1 mesure les erreurs des détecteurs ; ici on isole la politique).
- **Politiques**, mêmes tirages pour toutes : **rien** (chaque retentative repart de 1) ; **refus** (toute retentative
  d'une éliminée refusée) ; **héritage** (la retentative repart de la richesse finale cumulée de sa classe ; promue si
  le produit atteint 1/α à un instant quelconque ; la classe garde le produit final).
- **Mesures** : découvertes fausses (classes fausses promues) par course ; découvertes vraies par course ; 200 courses.
- **Lecture** : « héritage » est meilleur que « refus » si ses découvertes fausses par course ne dépassent pas celles de
  « refus » (intervalle de la différence, par rééchantillonnage des courses, qui contient 0 ou est négatif) **et** si ses
  découvertes vraies sont plus nombreuses (intervalle entièrement positif). « rien » doit montrer l'inflation des fausses
  découvertes (sinon l'essai n'a pas de dents, R5). **Prédictions** : fausses par course — rien ≈ 1,5 à 3 fois refus (0,8),
  héritage ≤ refus + 0,02 (0,8) ; vraies par course — héritage > refus (0,8).
