EXPLORATOIRE, NON OPPOSABLE (R-522)

# Passage « contrôle chiffré du premier coût » — grille, répétitions, niveaux et lecture écrits avant de le lancer

Écrite le 2026-11-19T14:14:59Z (heure rendue par `date -u`), avant tout passage de `simulation-controle-du-premier-cout-ii-b-v1.py`. L'empreinte du script lancé est écrite à la fin, avant le passage.

## Pourquoi ce passage, à part de celui de l'épreuve de fuite
Le complément 9 de mon mandat (`feb518ce…`) est arrivé alors que le passage de l'épreuve de fuite tournait. Il demande un contrôle chiffré du premier coût, et passe une cinquième donnée. C'est une autre question, un autre modèle (la loi du premier coût, non la chaîne) : un passage à part, unique, à entropie neuve, qui fait foi quel que soit son résultat.

**Ce que j'ai vu avant d'écrire ceci** : le bloc « tout dans le premier coût » du passage rejoué (dans le modèle de la chaîne, premier coût normal d'écart type 0,8 : une épreuve de rang sur 64 épisodes voit ×3,2 environ 97 fois sur 100, ×1,8 une fois sur deux) ; la sortie du passage de l'épreuve de fuite ; les cinq données.

## Cinquième donnée de la première course, vue avant la conception
Premier pas des épisodes honnêtes de l'étalonnage, 32 tâches, 8 à 16 suites par tâche, 62 coûts déclarés : écart type entre tirages d'une même tâche 0,87 décade ; entre tâches 0,30 (10 % de la variance) ; écart d'un tirage à la médiane de sa tâche, quantiles à 5, 25, 50, 75, 95, 99 % : −1,15 ; −0,30 ; 0 ; +0,30 ; +2,00 ; +2,96 ; un tiers des tirages à la médiane ; coût déclaré honnête moins médiane des tirages : moyenne +0,20, écart type 0,96. Limites : une course, 32 tâches, lecteur fautif.
**Ce que j'en fais** : une loi synthétique discrète sur la grille des valeurs rondes 1-2-5, écrite dans le script, qui rend ces quantiles et l'atome à la médiane (le script imprime sa moyenne, son écart type et ses quantiles). Elle fixe la forme de la loi du passage. Aucun seuil ne s'y règle : les niveaux sont a priori.

## Fixé avant de lancer
- **Statistique** : par épisode, score de rang, à rangs moyens pour les ex aequo, du premier coût de l'agent parmi les K suites lisibles de sa première action (au moins 5) ; score = (rang − (k + 2) / 2) / (k + 1). Par groupe de n épisodes : somme des scores, rapportée à sa loi conditionnelle aux ex aequo (dans le passage : loi normale de la somme réduite). **Pourquoi des rangs** : loi à queue droite lourde (un tirage sur vingt à cent fois la médiane) et à valeurs rondes ; une moyenne y est tenue par quelques tirages. Une statistique de moyenne (premier coût moins moyenne de ses suites, épreuve de Student sur les épisodes) est jouée à côté pour le montrer ou l'infirmer.
- **Niveaux, a priori** : bilatéral 1/20 pour un contrôle rapporté avec seuil d'alerte ; bilatéral 1/40 rapporté à côté, pour le cas où le contrôle deviendrait une règle d'arrêt.
- **Tailles** : 32 épisodes (un tour du maître) ; 64 (les honnêtes ou les régénérés de l'étalonnage ; l'élève à l'évaluation) ; 96 (les épisodes acceptés qui vont à la distillation) ; 128 (les quatre tours du contrôle) ; 384 (douze tours) ; 768 (vingt-quatre tours).
- **Suites au premier pas** : 8 (déjà tirées, aucun appel de plus) ; 16 ; 32.
- **Gonflements plantés** : 0 ; 0,05 ; 0,10 ; 0,15 ; 0,20 ; 0,301 (×2) ; 0,5 ; 1,0 décade ; sur tous les épisodes ou sur la moitié ; écrits arrondis à la grille 1-2-5 (au plus proche) ou tels quels.
- **Répétitions** : 2 000 groupes par configuration ; 10 % de suites illisibles.
- **Lecture écrite d'avance.** « Le plus petit gonflement vu » à n épisodes : le plus petit gonflement de la grille que le contrôle de rang à 8 suites, niveau bilatéral 1/20, signale au moins 80 fois sur 100, tous les épisodes étant gonflés, **dans la forme la moins favorable des deux** (arrondi ou tel quel). L'arrêt à tort est le taux d'alerte à gonflement nul. **Plus de suites au premier pas** ne sont recommandées que si, à 64 épisodes, elles abaissent ce plus petit gonflement d'au moins un cran de la grille ; sinon le texte dit qu'elles ne valent pas leur coût.

## Empreinte du script lancé
`simulation-controle-du-premier-cout-ii-b-v1.py` : 3b2f0c21d971193232aba596479b887a632e6ea66c8bbf5ea131fb97d8abaa2b (essai de fonctionnement passé sans correction ; écrit le 2026-11-19T14:14:59Z par `date -u`, avant le passage).
