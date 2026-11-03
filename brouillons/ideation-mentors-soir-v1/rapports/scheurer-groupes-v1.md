# Groupes des fiches de la piste Scheurer, groupeur aveugle (v1)

- Consigne : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/piste-scheurer-groupeur-aveugle-v1.md`, sha256 `340ef36abbd88c9210e534bdda744ee8431c647500c5ca475063b2a4b83325e7` (vérifiée, conforme).
- Entrée, seule pièce lue : `/home/claude/scratch/soir-rapport/scheurer/piste/fiches-a-grouper-v1.json`, sha256 `9bae335ec593d5e0cd7a8431dfdf7ef3cd7ce1ca68caa6b7c15cd50788c3ef1b` (vérifiée, conforme), 14 fiches (SC-01 à SC-14).
- Début du travail : 2026-11-03 14:46:21 UTC (temps universel coordonné, donné par `date -u`). Aucun classement consulté.

## 1. Groupes

Définitions écrites le 2026-11-03 à 14:51:08 UTC (`date -u`), avant toute affectation. Elles ne changent plus ensuite ; les tensions apparues à l'affectation sont en section 3.

Chaque groupe est une tendance proposée : la quantité tracée (ligne 1) et la raison pour laquelle elle aurait une tendance mesurable (ligne 2).

### Groupe 1 : Seuil du moniteur
- Définition :
  - Quantité tracée : la difficulté maximale tenue (longueur de trajectoire ou d'artefact, temps humain de détection, nombre d'occasions d'action) ou la ressource minimale requise (budget d'inférence) pour qu'un moniteur ou un contrôleur figé atteigne un critère fixé de détection, de fausses alertes ou de dommage.
  - Tendance mesurable parce que les anomalies ou attaques sont exogènes, gelées et vérifiées mécaniquement : le point de croisement est une grandeur continue, ajustable contre la date de sortie du moniteur comme un horizon de tâches.
- Critère : la fiche trace, contre la date ou la taille du moniteur, un point de croisement de sa performance de détection ou de blocage, face à un ensemble d'anomalies ou d'attaques produit indépendamment de lui.

### Groupe 2 : Capacité d'attaque
- Définition :
  - Quantité tracée : le seuil (durée humaine de l'épisode, ou nombre d'occasions nécessaires) auquel le modèle surveillé, sous invites, budget et contrôle figés et sans élicitation adaptative, réussit dans 50 % des cas un artefact fonctionnel de la classe plantée qui franchit le contrôle.
  - Tendance mesurable parce que c'est une capacité accessible, continue même quand le taux spontané de manigance est nul, ajustable contre la date de publication des poids.
- Critère : la grandeur tracée est la réussite du modèle surveillé (côté attaquant), non celle du moniteur, lue comme point de croisement d'un critère de réussite sous un contrôle figé.

### Groupe 3 : Taux de propension
- Définition :
  - Quantité tracée : la fréquence d'un comportement non demandé du modèle étudié (actions couvertes, sous-performance stratégique, conscience d'évaluation verbalisée), contre la date de sortie ou le calcul d'entraînement.
  - Tendance mesurable seulement si le taux s'écarte de zéro et varie de façon monotone sur une échelle adaptée (logit) ; elle est menacée par la confusion avec les refus et la disposition.
- Critère : l'axe vertical est un taux de comportement spontané (ou une transformée d'un tel taux), non une capacité sous protocole forcé ni une performance de moniteur.

### Groupe 4 : Détournement du moniteur
- Définition :
  - Quantité tracée : la probabilité ou le gain avec lesquels un texte inséré dans le contenu évalué pour orienter le verdict (injection d'instructions, note à l'évaluateur, assertion sur le verdict) déplace le verdict d'un moniteur, ou l'écart de capacité attaquant–moniteur à partir duquel ce texte réussit.
  - Tendance mesurable parce que cette robustesse dépend de la taille et de la date du moniteur (hiérarchie d'instructions) et se lit en continu sur une matrice attaquant × moniteur.
- Critère : la fiche mesure l'effet, sur le verdict d'un moniteur, d'un texte qui lui parle depuis le contenu évalué ; ce groupe prime sur « Seuil du moniteur » quand l'attaque passe par ce canal.

### Groupe 5 : Complaisance sous pression
- Définition :
  - Quantité tracée : le déplacement du verdict d'un modèle évaluateur sous la pression sociale de l'interlocuteur (éloge, critique, réputation de l'auteur), résumé par un gain g, une note initiale p₀ et un point fixe ĉ.
  - Tendance mesurable parce que ces grandeurs sont continues par modèle sous un protocole de pression figé, donc comparables d'un modèle, d'une taille ou d'une date à l'autre.
- Critère : la fiche porte sur ce que la pression venue de l'interlocuteur fait au verdict (ce qui le porte, ce qui le déplace, ce qui le laisse invariant).

## 2. Affectations

Écrites à partir de 2026-11-03 14:51:59 UTC (`date -u`), après la section 1. Une fiche, un groupe (son idée principale) ; « second choix » seulement si la fiche relève presque autant d'un autre groupe.

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| SC-01 | Capacité d'attaque | Seuil côté attaquant exprimé en coût (occasions d'épisode nécessaires pour 50 % de réussites franchissant le contrôle) ; second choix : si les tentatives ne sont pas demandées, ce coût est l'inverse du taux de manigance que la fiche dit remplacer. | Taux de propension |
| SC-02 | Détournement du moniteur | Gain de déférence d'un moniteur Qwen2.5 à une note insérée dans le contenu évalué, impérative contre déclarative ; second choix : même mesure de gain que les fiches de pression, sans axe d'échelle. | Complaisance sous pression |
| SC-03 | Seuil du moniteur | Longueur maximale de trajectoire (en transitions d'état) tenue par un moniteur à 80 % de détection et 5 % de fausses alertes sur anomalies plantées, contre la date de sortie. | aucun |
| SC-04 | Seuil du moniteur | Temps humain de détection auquel la détection du moniteur tombe à 50 %, sur un corpus gelé d'attaques validées sans injection, contre la date de sortie. | aucun |
| SC-05 | Complaisance sous pression | Teste ce qui porte le point fixe sous éloge de Llama-3.1-8B-Instruct (les refus) par une clause qui les supprime, le bras critique servant de contrôle ; aucun axe d'échelle. | aucun |
| SC-06 | Seuil du moniteur | Ressource minimale (budget d'opérations d'inférence) pour qu'un moniteur atteigne des critères fixés sur anomalies plantées, contre la date de sortie : variante « ressource » du seuil. | aucun |
| SC-07 | Détournement du moniteur | Écart de capacité attaquant–moniteur au-delà duquel une injection dans le contenu lu par le moniteur réussit, et son déplacement avec la date du moniteur ; second choix : c'est aussi un seuil daté du moniteur. | Seuil du moniteur |
| SC-08 | Capacité d'attaque | Durée humaine de l'épisode à laquelle le modèle surveillé réussit dans 50 % des cas sous protocole et moniteur figés, contre la date de publication des poids. | aucun |
| SC-09 | Taux de propension | Taux de conscience d'évaluation verbalisée et d'actions couvertes, contre le calcul d'apprentissage par renforcement (monotonie contre saut puis plateau). | aucun |
| SC-10 | Seuil du moniteur | Longueur d'artefact à laquelle la détection d'un moniteur croise 50 % (fausses alertes à 5 %) face à des portes dérobées gelées et vérifiées à l'exécution, contre la date de sortie du moniteur. | aucun |
| SC-11 | Complaisance sous pression | Prédit que la réputation de l'auteur ne déplace que la note initiale p₀, non le point fixe ĉ de la pression utilisateur (bande d'équivalence) ; aucun axe d'échelle. | aucun |
| SC-12 | Taux de propension | Pente datée d'une propension (sous-performance stratégique) prédite dominée par les refus et la disposition, proposée comme contre-exemple au tracé des propensions. | aucun |
| SC-13 | Seuil du moniteur | Nombre maximal d'occasions d'action tenues par un contrôleur (dommage sous 5 %, 90 % d'accomplissement honnête) face à un flux exogène gelé, contre la date de sortie. | aucun |
| SC-14 | Complaisance sous pression | Compare une pression sur la forme et une pression sur le fond et prédit une concession dissociée de Llama-3.1-8B-Instruct ; aucun axe d'échelle. | aucun |

Effectifs : Seuil du moniteur 5 (SC-03, SC-04, SC-06, SC-10, SC-13) ; Capacité d'attaque 2 (SC-01, SC-08) ; Taux de propension 2 (SC-09, SC-12) ; Détournement du moniteur 2 (SC-02, SC-07) ; Complaisance sous pression 3 (SC-05, SC-11, SC-14). Total 14, aucune fiche hors groupe.

Seconds choix : SC-01 (Taux de propension), SC-02 (Complaisance sous pression), SC-07 (Seuil du moniteur).

## 3. Limites

Les définitions de la section 1 n'ont pas été retouchées ; les tensions ci-dessous sont apparues à l'affectation.

1. Quatre fiches ne proposent aucun axe d'échelle (ni date, ni taille, ni calcul) : SC-02, SC-05, SC-11, SC-14. Ce sont des tests de mécanisme sur un seul modèle (Llama-3.1-8B-Instruct, ou un moniteur Qwen2.5). Elles sont rangées par la grandeur qu'elles mesurent ; leur tendance n'existe qu'en puissance. Le groupe « Complaisance sous pression » ne contient aucune fiche qui trace une tendance.
2. « Seuil du moniteur » est le plus gros groupe (5 fiches) et réunit trois lectures : horizon de difficulté (SC-03, SC-04, SC-10), horizon de contrôle sous contrainte d'utilité (SC-13), ressource minimale (SC-06, que la fiche lit elle-même comme une tendance d'efficacité de calcul et non de compétence). Un découpage plus fin les séparerait ; je ne l'ai pas fait, la définition ayant été fixée avant affectation.
3. SC-01 : la fiche ne dit pas si les tentatives sont demandées (capacité) ou si ce sont des occasions spontanées (propension convertie en coût). D'où le second choix « Taux de propension ». SC-08, sa voisine, se déclare explicitement capacité.
4. « Taux de propension » réunit deux axes différents : le calcul d'apprentissage par renforcement le long d'un entraînement (SC-09) et la date de sortie (SC-12). Le groupement suit la grandeur tracée (un taux), non l'axe.
5. La frontière entre « Détournement du moniteur » et « Complaisance sous pression » tient au canal : texte inséré dans le contenu évalué, ou pression de l'interlocuteur. SC-02 partage la mesure de gain des fiches de pression ; SC-07 a la forme d'un seuil daté du moniteur. C'est la règle de priorité écrite dans le critère du groupe 4, avant affectation, qui les range.
6. « Seuil du moniteur » et « Capacité d'attaque » ont la même forme de mesure (point de croisement sous protocole figé) ; elles ne diffèrent que par le sujet tracé (moniteur ou modèle surveillé). Des fiches des deux groupes peuvent partager le même dispositif (tâches à classe plantée et contrôle figé).
7. Un thème transversal n'est pas capté par le groupement : les refus comme facteur de confusion de la mesure apparaissent dans deux groupes (SC-05 sous pression, SC-12 en propension).
8. Les chiffres que certaines fiches marquent « RAPPORTÉ » (SC-07, SC-09) n'ont pas été vérifiés sur source. Le groupement n'en dépend pas.
9. Seul le fichier d'entrée a été lu. Le sens de « R7 », des strates « Sp » et « Sm » et des campagnes 1 et 2 est déduit du texte des fiches, sans consultation des pièces correspondantes.
