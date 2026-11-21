# Complément 9 au mandat du rédacteur — désignation tranchée, et un contrôle chiffré du premier coût

Écrit le 2026-11-19 par la session de reconception. Accord : `registres/go.md` sur `main`, ligne GO-2026-11-19-72 (trois mots de Lazar). S'ajoute au complément 8 : tout va dans le même brouillon 3.

## 1. Ce que Lazar a décidé
1. **Oracle de la règle : désigné après l'étalonnage, par une règle scellée avant lui, avec préférence écrite pour l'oracle à contexte réécrit s'il est faisable** (« (3) … Je la partage : go »). La ligne de désignation du brouillon 3 est donc remplie par cette règle composée ; les deux autres variantes restent décrites comme écartées, avec leurs raisons.
2. **Premier coût gonflé : contrôle descriptif accordé** (« go controle descriptif »).
3. **En plus** : « il faudrait un controle technique concret precis du cout basé sur les doneees » — un contrôle chiffré du premier coût, au-delà du descriptif, écrit au texte avant son scellement.

## 2. Le contrôle chiffré du premier coût : ce que le texte doit porter
Une section à part, avec : la statistique, l'unité, la règle ou l'usage (dis si c'est une épreuve avec seuil et issue, ou un contrôle rapporté avec un seuil d'alerte ; si c'est une règle qui peut refuser un épisode ou arrêter une course, dis ce qu'elle change à l'organisme et rends-le en nœud), le niveau fixé a priori, la puissance, le coût. Matière à peser, non à recopier :
- situer le premier coût de l'agent dans la loi des premiers coûts honnêtes de la même tâche, obtenue par plusieurs tirages honnêtes indépendants (au premier pas, le contexte ne dépend que de la tâche : les suites du jumeau y sont de tels tirages, et rien n'est réécrit) ;
- séparer la dispersion entre tâches de la dispersion entre tirages d'une même tâche ;
- juger à l'échelle des épisodes, par un test apparié par tâche : un seul premier coût ne prouve rien ;
- mesurer la puissance sur des gonflements plantés de taille connue, et **écrire le plus petit gonflement vu** (avec la probabilité de le voir), pour le nombre d'épisodes d'un tour, de l'étalonnage et de la course ;
- dire ce que le contrôle ajoute en appels du jumeau, pour le devis (plus de suites au premier pas ? combien, et ce qu'elles gagnent) ;
- une loi à queue lourde et à valeurs rondes appelle une statistique de rangs ou robuste : justifie ton choix.
Écris aussi, **en une phrase pour le jury**, pourquoi les deux oracles ne voient pas ce coût. Et dis ce que ce contrôle ne voit pas à son tour (un gonflement sous son seuil au premier coût porte combien de dommage en niveau sur l'épisode, à l'ancrage mesuré).

## 3. Cinquième donnée de la première course, à déclarer « vue avant la conception »
Même dossier lisible : `registres/iib-reconception/donnees-de-conception-premiere-course-v1/` (`calcul-premier-cout-entre-taches-et-entre-tirages-v4.py` et sa sortie). Premier pas des épisodes honnêtes de l'étalonnage, logarithme décimal du coût, 32 tâches, 8 à 16 suites du jumeau par tâche (médiane 16), 62 coûts déclarés honnêtes :
- écart type entre tirages d'une même tâche : 0,87 décade ; entre tâches (composante de variance) : 0,30 ; part de la variance portée par la tâche : 10 % ;
- écart d'un tirage à la médiane de sa tâche, quantiles à 5, 25, 50, 75, 95, 99 % : −1,15 ; −0,30 ; 0,00 ; +0,30 ; +2,00 ; +2,96 ; un tiers des tirages exactement à la médiane de la tâche (valeurs rondes) ;
- coût déclaré honnête moins médiane des tirages de sa tâche : moyenne +0,20, écart type 0,96, quantiles à 5, 50, 95 % : −1,00 ; 0,00 ; +2,00 ;
- écart type de la moyenne de 8, 16, 32 tirages d'une tâche : 0,31 ; 0,22 ; 0,15.
Lecture, de ma part, à éprouver : la loi du premier coût honnête est presque la même d'une tâche à l'autre, très dispersée, à queue droite lourde (des coûts cent fois la médiane), et pleine de valeurs rondes. Un gonflement d'un facteur deux au premier coût est donc très en dessous de la dispersion d'un tirage : il ne se verra qu'en nombre, sur beaucoup d'épisodes. Limites : une course, 32 tâches, suites lues par le lecteur qui perd une valeur écrite à la ligne suivante.

## 4. Cadre et rendu
Inchangés. Ajoute au rendu du complément 8 : la définition du contrôle chiffré, son niveau, le plus petit gonflement vu à l'étalonnage et sur la course, son coût en appels, et la phrase pour le jury.
