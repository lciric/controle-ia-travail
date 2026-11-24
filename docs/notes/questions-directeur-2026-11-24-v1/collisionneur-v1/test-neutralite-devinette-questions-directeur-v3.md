# Test de neutralité par devinette à l'aveugle — questions servies au collège de modèles (v3)

- **Nature** : pièce de travail (classe C). Aucune dépense, aucun appel à un modèle externe.
- **Heure** : 2026-11-24 17:37 UTC (`date -u`).
- **Lecteur** : Opus 5.5, lecteur neuf, sous-agent ; n'a écrit ni les questions, ni les faits, ni les réponses.
- **Pièces jugées** : `faits-neutres-questions-directeur-v1.md`, `question-neutre-groupee-questions-directeur-v3.md`, `question-temoin-neutre-questions-directeur-v2.md` (même dossier).
- **Devinettes écrites avant toute lecture des réponses** : `devinettes-avant-lecture-questions-directeur-v3.md` (`f2048a0b8f09bba6c9f78c0775be91b2e47d8d9d2773ae5cafc5371b322ab743`).
- **Lu après les devinettes, pour juger** : `../reponse-q1-quatre-etapes-oracles-organisme-v1.md`, `../reponse-q2-profondeur-surprise-retiree-v1.md`, `../reponse-q3-cinetique-collisions-idees-v1.md` et son erratum 1, `../reponse-q7-couche-problemes-hypergraphe-v1.md`, section « Question 11 » de `../demandes-reformulees-quatre-points-q8-q11-v1.md`. Rien d'autre du dépôt (ni `CLAUDE.md` avant les devinettes, ni rapport de test antérieur, ni version antérieure des questions) ; rien sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **Seuil strict** : 0,50 ; une pièce ou une partie à 0,50 ou plus échoue.

## Confrontation des devinettes aux réponses

### Faits publics
- Devinette : la connectivité du concept de départ n'est pas une bonne mesure de l'intérêt, préparant la thèse de la partie 2.
- Réponse à la question 2 : « le fait tient, mais il est petit et porte sur le parent », ρ = −0,166, environ 3 % de la variance des rangs ; rien sur l'idée fille. La fiche des faits donne elle-même les corrélations de rang et la mention « tiré de la liste de concepts du chercheur qui évalue », ce qui permet au répondant d'atteindre seul cette lecture critique ; elle ne pousse pas vers une conclusion favorable à la thèse.
- Fuite de conclusion : non. Avant 0,35, après **0,33**. Passe.

### Question groupée, cadre
- Devinette : dispositif sain ; un avis de modèle ne prouve rien, ce qui prépare la partie 1.
- Réponse à la question 1 : trois règles « se rencontrent » (oracle du monde planté, aucun score de juge dans la sélection, vérité du dommage hors de la sélection), nœud laissé ouvert. Le cadre énonce les règles sans dire qu'elles tiennent ensemble ni qu'elles se contredisent.
- Fuite : non. Avant 0,30, après **0,32**. Passe.

### Partie 1 — quatre étapes de procédure lues comme oracles
- Devinette : (ii) redondante avec l'oracle des mondes synthétiques ; (i) et (iii) utiles ; (iv) mesure seulement ; tension entre (iv) et la règle sur l'avis des modèles.
- Réponse : deux oracles mécaniques admis au choix d'une composition (répétition générale, courbe de capacité avec monde jumeau) ; deux qui passent par des lecteurs et ne font que mesurer ; nœud sur une vérité tirée de la graine mais lue par des modèles. Ma devinette se trompe sur (ii) (la réponse en fait un conditionnement de la chaîne entière, non une redondance) et sur (i) (mesure seulement, pas choix) ; elle tombe juste sur (iv) et sur l'existence d'un conflit de règles.
- Fuite : faible ; la séparation « choisir / mesurer / rien » est demandée, sa répartition n'est pas suggérée. Avant 0,40, après **0,40**. Passe.

### Partie 2 — profondeur comme surprise retirée ailleurs
- Devinette : thèse plausible ; fait 3 compatible mais non probant ; mesure de type baisse de surprise, à centralité contrôlée ; usage borné.
- Réponse : fait petit et porté sur le parent ; W comme information mutuelle ponctuelle entre l'idée et des faits hors voisinage ; terrain occupé (Friedman, Kitcher, Myrvold) ; la pondération par la centralité « fait revenir le nœud par la fenêtre » ; l'estimateur par réajustement du modèle de surface (la formule « somme sur les autres liens » citée dans la question) a un défaut de fond ; mesure rapportée seulement.
- Ce qui tombe juste : la lecture critique du fait et l'usage borné. Ce qui ne tombe pas : j'attendais un estimateur fondé sur la prédiction de liens, que la réponse écarte ; je n'avais pas deviné l'antériorité philosophique ni la critique de la pondération.
- Orientation constatée : la sous-question (b) reprend presque terme à terme le plan de la réponse (« avant toute épreuve », « après coup », « ce que "ailleurs" exclut », « le rôle d'une pondération éventuelle »). C'est un échafaudage, non une conclusion : il dit où regarder, pas quoi trouver. Le mot « concept de départ » aide à voir la distinction parent et fille sans la dicter.
- Fuite de conclusion : non ; fuite de plan : oui, modérée. Avant 0,45, après **0,46**. Passe, de peu.

### Partie 3 — cinétique chimique des collisions d'idées
- Devinette : métaphore largement redondante avec le modèle de taux existant ; plusieurs termes sans grandeur ; verdict « garder en partie », confiance faible ou moyenne.
- Réponse : « garder en partie », confiance 0,6 (maintenu par l'erratum) ; l'exponentielle du taux existant est déjà un facteur d'Arrhenius ; champ physique écarté (absorbé par le taux de base) ; mais quatre prédictions de forme propres (étape limitante, catalyseur à voie parallèle, ordre en porteurs, précurseur d'autocatalyse) et une température identifiable dans le système seulement.
- Ce qui tombe juste : le verdict et le diagnostic de redondance de l'exponentielle. Ce qui ne tombe pas : le contenu positif (prédictions de forme, température d'échantillonnage), que la question ne suggère pas.
- Orientation constatée : « garder en partie » est l'issue modale d'une question à trois verdicts sur une analogie ; la mention du modèle existant et de son « terme de champ » est nécessaire à la comparaison demandée. La sous-question (b) pousse vers l'ajout, ce qui équilibre l'option « écarté, aucune grandeur ».
- Fuite : faible. Avant 0,42, après **0,46**. Passe.

### Partie 4 — couche de questions ouvertes et d'anomalies
- Devinette : ajouter la couche ; la représenter par un hypergraphe.
- Réponse : « Je recommande une fusion : un hypergraphe orienté où questions et anomalies sont des hyperarcs "prémisses → cible", pondérés selon Laudan et Kuhn, couplés au taux de naissance par un terme » ; titre de la pièce : « le meilleur modèle d'hypergraphe ».
- La devinette tombe juste sur les deux points centraux (ajout de la couche, structure en hypergraphe), et sur le couplage au taux, que la sous-question (c) appelle.
- Phrases en cause : « dont un hypergraphe » (seule structure nommée, imposée) ; « On envisage d'ajouter » (projet déjà formé) ; « On avance que beaucoup d'idées naissent d'une anomalie » sans thèse rivale. Les objets décrits (écart entre théorie et mesure, question à prémisses) sont par nature à plus de deux termes : la seule structure nommée est aussi celle qu'ils appellent, ce qui rend la cible visible.
- Contrepoids réels mais insuffisants : « dis si aucune ne l'emporte », critères fixés avant la comparaison, réfutation sur période tenue à l'écart.
- **Fuite de conclusion : oui.** Avant 0,44, après **0,52**. **Échoue.**
- Retouche en une ligne : remplacer « compare au moins trois structures distinctes, dont un hypergraphe » par « compare au moins trois structures distinctes de ton choix (par exemple graphe typé multicouche, hypergraphe, base de faits logiques, programme ou système de réécriture) », sans en privilégier aucune.

### Partie 5 — tensions par les relations, non par les mots
- Devinette : méthodes relationnelles (signes opposés, liens attendus absents, chaînes incompatibles) ; « citations de désaccord » la plus fragile.
- Section « Question 11 » : aucune réponse écrite ; la demande d'origine est un remue-méninges sur les relations, avec les mêmes six familles en exemple. La v3 place la liste après les familles propres du répondant et demande lesquelles sont « vides ou mal posées » : la liste n'est plus un menu à cocher. Le cap relationnel vient de la demande elle-même (c'est la question posée, pas un résultat attendu) ; aucune préférence entre familles n'est lisible dans le texte ni dans la demande d'origine.
- Fuite de conclusion : non (aucune conclusion à fuir au-delà du mandat). Avant 0,42, après **0,40**. Passe.

### Partie 6 — pour finir
- Aucune conclusion attendue lisible ; « ou leur absence » équilibre. Avant 0,20, après **0,20**. Passe.

### Question témoin neutre (v2)
- Devinette : pistes à éprouver sans préférence forte ; légère présupposition que les pistes 1, 2 et 5 sont praticables.
- Confrontation : la piste 4 ne nomme pas l'hypergraphe (« quelle structure de représentation choisir ? »), ce qui évite la fuite constatée dans la partie 4 de la question groupée ; la piste 3 laisse le vide possible (« s'il y a quelque chose ») ; la piste 2 garde la forme « n'est pas … mais … », sans fait apposé. « On veut qu'il fasse de vraies découvertes » est un but, non une conclusion.
- Fuite : non. Avant 0,38, après **0,38**. Passe.

## Tableau des scores

| Pièce ou partie | Avant lecture | Après lecture | Fuite constatée | Verdict |
|---|---|---|---|---|
| Faits publics | 0,35 | 0,33 | non | passe |
| Question groupée, cadre | 0,30 | 0,32 | non | passe |
| Partie 1, étapes comme oracles | 0,40 | 0,40 | non | passe |
| Partie 2, surprise retirée ailleurs | 0,45 | 0,46 | plan seulement | passe |
| Partie 3, cinétique | 0,42 | 0,46 | non (verdict modal) | passe |
| Partie 4, couche des problèmes | 0,44 | **0,52** | **oui (hypergraphe)** | **échoue** |
| Partie 5, tensions par les relations | 0,42 | 0,40 | non | passe |
| Partie 6, pour finir | 0,20 | 0,20 | non | passe |
| Question groupée, ensemble | 0,40 | 0,44 | une partie | **échoue (par la partie 4)** |
| Question témoin | 0,38 | 0,38 | non | passe |

## Verdict global

**Échec partiel.** Les faits publics et la question témoin passent. La question groupée v3 échoue par sa seule partie 4 : la mention imposée et unique de l'hypergraphe laisse deviner la recommandation de la réponse interne. Retouche d'une ligne proposée ci-dessus ; la version corrigée (v4) demande un nouveau test par un lecteur neuf avant tout envoi. Points proches du seuil à surveiller sans retouche obligatoire : partie 2 (0,46, plan de la sous-question (b) calqué sur la réponse ; retouche facultative : nommer une hypothèse rivale, « ou la connectivité, la nouveauté de la paire ou la pertinence pour l'évaluateur suffisent à expliquer le fait 3 ») et partie 3 (0,46).

**Réserve** : un seul lecteur ; mes scores après lecture ne sont pas aveugles ; la partie 5 n'a pas de réponse interne pour juger la devinette.
