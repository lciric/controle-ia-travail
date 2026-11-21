# Faits : compter exactement le dommage d'un sabotage diffus dans des travaux de recherche confiés à des agents

## Le cadre

Un programme de recherche défensif surveille des agents d'IA qui font des travaux de recherche : concevoir des expériences, analyser des données, conclure. L'adversaire redouté sabote de façon diffuse : beaucoup de petits écarts, dont chacun se défend ; il connaît tout le dispositif, sauf ses tirages secrets. Sur de telles tâches, la qualité d'un travail ne se vérifie guère qu'en le refaisant : elles sont floues à la relecture. Conséquence : on compare des moniteurs sans savoir ce qu'ils laissent passer, parce que le dommage n'a pas de vérité.

Le programme envisage un banc d'essai, énoncé ainsi : des mondes de recherche engendrés par programme, à lois plantées, flous à la relecture et exacts en aval ; le dommage d'un sabotage diffus s'y compte en lois vraies perdues et en lois fausses promues, par un oracle qui tourne hors de la machine de l'agent ; le banc est servi avec un jumeau honnête, un juge faible et l'accès aux états internes de l'agent. Seul, ce banc n'est pas un résultat : c'est un terrain que d'autres équipes doivent pouvoir rejouer. Il doit accueillir des modes de sabotage qu'il ne connaît pas, écrits par des tiers.

## Ce que le programme envisage, à critiquer

- **Générateur.** Un graphe de causes tiré au hasard, des variables cachées, du bruit ; des fausses lois tentantes qui naissent de la structure (cause commune cachée, causalité prise à l'envers, échantillon sélectionné). La difficulté d'une loi est sa détectabilité au budget donné, calculée par un analyste de référence et non réglée sur un modèle. La fiche d'un épisode, c'est-à-dire la liste des questions posées à l'agent, est composée par case : tant de lois de chaque niveau de détectabilité, tant de fausses lois tentantes, tant de relations sans effet. Les noms des variables sont attribués par une permutation secrète ; les graines sont tirées après le gel des modèles éprouvés, engagées par empreinte, révélées après la course ; un monde révélé ne ressert pas.
- **Produit et oracle.** L'agent rend un registre d'affirmations à champs fermés (relation, statut, signe, intervalle borné, domaine, expériences d'appui) et un texte libre. L'oracle est un programme : il ne lit ni le texte, ni les états internes, ni la sortie d'un juge ; il compte les lois vraies perdues, les lois fausses promues, et le regret d'un consommateur déterministe qui décide d'après le registre. Aucun verdict ne revient à l'agent.
- **Jumeau honnête.** Le même modèle, le même monde, le même bruit par requête (la même question rend les mêmes données), plusieurs tirages. Le dommage d'un saboteur est l'excès sur ce jumeau. Second témoin : un agent honnête handicapé (par exemple par un budget réduit) jusqu'à perdre en moyenne autant qu'un saboteur de dose donnée.
- **Juge faible.** Un modèle de confiance plus faible relit, à accès croissant : le rapport ; la trajectoire ; le droit de rejouer les analyses ; une part du budget en requêtes neuves.
- **États internes.** L'agent est un modèle à poids ouverts d'environ 8 milliards de paramètres ; ses états se régénèrent en rejouant les transcriptions.
- **Admission.** Avant tout usage, des témoins qui doivent tuer le banc : un juge faible qui voit tout ; un modèle faible qui fait aussi bien que le fort ; un oracle qui fuit vers l'agent ; une triche par mémoire ; un registre dégénéré qui gagne ; deux tirages du jumeau qui diffèrent.

## Ce qui est publié et borne la question

- Sur une tâche floue de propositions d'expériences, la vérité du dommage est approchée par un modèle et « was not validated quantitatively against human judges » ; pour beaucoup de ces tâches, elle est dite indéfinie (arXiv 2606.08892, p. 10).
- Un banc d'audit de dépôts de recherche sabotés : 9 dépôts, 11 sabotages écrits par un seul attaquant humain, aidé de modèles et d'experts ; meilleure aire sous la courbe d'un auditeur, 0,77 (arXiv 2604.16286, p. 1, 3, 10).
- Sabotage et surveillance en recherche automatisée : le sabotage y est une tâche annexe cachée, embarquée dans le produit ou indépendante de lui ; les agents sont des modèles de pointe servis par interface (arXiv 2607.19321, p. 1-2 ; arXiv 2610.27735, p. 1).
- Sur un banc d'ingénierie, le sous-rendement volontaire est plus difficile à détecter que le sabotage de code (arXiv 2511.09904, p. 1).
- Un bac synthétique où chaque épisode est étiqueté par rejeu et réparation de l'état final : les négatifs les plus durs d'un moniteur y sont les échecs honnêtes, et les étiquettes « cannot separate a deliberate shortcut from confusion » (arXiv 2611.00407, p. 1, 4).
- Des analystes artificiels, sur les mêmes données, rendent des conclusions qui se renversent ; l'effet est orientable par le rôle donné à l'analyste, même après le tri d'un auditeur de méthode (arXiv 2602.18710, p. 1).
- Des bancs de découverte à vérité connue, sans adversaire : lois décalées pour résister à la mémoire (arXiv 2510.07172, p. 1) ; environnements original et contrefactuel appariés, joués sans données, à données fixées, ou en expérimentant (arXiv 2610.37919, p. 1) ; scénarios à biais de sélection, erreur de mesure et causes cachées, avec un optimum analytique (arXiv 2607.04293, p. 1) ; tâches synthétiques à hypothèses vraies connues (arXiv 2504.11524, p. 1) ; un environnement de découverte évalué sur cinq graines publiques, où la connaissance découverte est notée par un modèle contre une référence (arXiv 2406.06769, p. 5-6).
- Non vérifié sur le texte par le programme : des juges de la découverte automatisée éprouvés sur des contrôles conçus négatifs, face à un proposeur adverse ; des jeux de trajectoires bénignes appariées à des attaques ; des organismes de sous-rendement à poids ouverts.

## Contraintes

- Budget de calcul modeste ; relecture humaine rare.
- La menace se décrit au niveau de l'idée (familles, suppositions violées), jamais par un mode opératoire.
- Aucun score de moniteur dans l'entraînement ni dans la sélection d'un agent ; aucune sortie de l'oracle ne choisit un agent ni un moniteur.
- Aucune moyenne ni médiane sur les jetons dans une sonde de production.
