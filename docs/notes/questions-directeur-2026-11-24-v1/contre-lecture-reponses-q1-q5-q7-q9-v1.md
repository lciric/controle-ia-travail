# Contre-lecture des réponses aux questions 1 à 5, 7 et 9 du directeur (v1)

- **Nature** : pièce de travail (classe C). Contre-lecture seule ; aucune pièce modifiée, aucune dépense, aucun appel à un modèle externe.
- **Heure** : `2026-11-24T16:28:39Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, contre-lecteur neuf, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS` ; je n'ai écrit aucune des pièces lues.
- **Fichiers lus** : `CLAUDE.md` ; demandes reformulées (`52d1cc47…`, questions 1 à 7 ; `632c7af2…`, question 9) ; réponses q1 (`2cc29632…`), q2 (`7f4cf73f…`), q3 (`af126ebf…`), q4 (`249c611c…`), q5 (`0bdc9810…`), q7 (`937e3e69…`), q9 (`e981c88c…`) ; scripts `simulation-cinetique-barriere-v1.py` (`57dd7cc9…`), `simulation-emergence-organisme-v1.py` (`4b71ba51…`), `exemple-graphe-meta-mathematique-v1.py` (`16e6bb1e…`) et leurs sorties ; `complement-questions-8-9-et-corrections-note-v1.md` ; `reponse-fable-max-v1.md`, ligne 39 et ligne 45 ; `reponse-carbon-v1.md`, lignes 36 à 40 ; `decision-N-053-v1.md`, `decision-N-060-v3.md`, `decision-N-067-v1.md` (recherches ciblées). PDF du dépôt sous `docs/sources/pdf/` (empreintes vérifiées) : 2405.17044v4, 2405.00492v1, tria-2014, 2604.18005, 2604.24797, 2603.20396 ; PDF du bloc-notes de la session : Diehl et Stroebe 1987, Wiśniewski 2001. Rien d'ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **Calculs refaits** (processeur, bloc-notes, hors dépôt) : borne 1 − 0,05^(1/n) ; dérivées de la forme en série ; condition d'optimum de Fable ; inflation de variance de la barrière sous un préfacteur dépendant de la température ; largeur locale du jouet de la question 9 (transpositions de φ).

## Synthèse

| Pièce | Verdict | Bloquants | Majeurs | Mineurs |
|---|---|---|---|---|
| Q1, quatre étapes comme oracles | tient | 0 | 0 | 3 |
| Q2, profondeur comme surprise retirée | tient | 0 | 0 | 4 |
| Q3, cinétique des collisions | à corriger | 0 | 1 | 4 |
| Q4, émergence | à corriger | 0 | 1 | 2 |
| Q5, Carbon contre Fable, Plan Turing | à corriger | 0 | 1 | 4 |
| Q7, couche des problèmes, hypergraphe | tient | 0 | 0 | 3 |
| Q9, exposé du graphe méta-mathématique | à corriger | 0 | 1 | 3 |

Aucun bloquant. Les quatre majeurs portent sur un chiffre ou une conclusion que le texte présente comme mesuré alors que le calcul ne le soutient pas (Q3, Q4, Q9) et sur une asymétrie du verdict (Q5).

## Q1 — les quatre étapes de procédure lues comme oracles de l'organisme

**Verdict : tient.** Les cinq attendus sont couverts ; l'homonymie « organisme » est signalée et traitée par la forme ; le nœud sur la couverture lue par des lecteurs est posé sans être tranché, au format de décision. Les quatre voisins exigés (POPPER, Dwork et collègues, Blum et Hardt, Co-Scientist) sont cités. La borne 1 − 0,05^(1/n) est juste (0,99 %, 0,30 %, 0,10 % pour 300, 1 000, 3 000) ; « 0 sur 1 000 » est bien dans N-067 (l. 44) ; l'invariant « aucun score de moniteur (sonde, juge) dans la sélection » est bien dans N-053 (l. 42).

**Sondage des références.** Qu, Chen, Wang, arXiv 2609.27051 : titre, auteurs et date (22 septembre 2026) confirmés sur arXiv. Co-Scientist : titre, auteurs, identifiant confirmés ; la page de Nature Asia donne Nature 655(8122), 487-496 (adresse de la notice).

- **Mineur.** Volume et pages de Co-Scientist laissés « à vérifier » alors qu'ils se trouvent. *Correction* : citer 655(8122), 487-496, d'après la notice de Nature Asia, ou garder « à vérifier » sur la page de l'éditeur seule.
- **Mineur.** Le kappa de Cohen simple pour trois issues ordonnées (« absent, altéré, conforme ») ignore l'ordre. *Correction* : kappa pondéré, ou alpha de Krippendorff ordinal, seuil gelé d'avance.
- **Mineur (règle R8).** « Je n'ai pas cherché si la réunion des quatre étapes… est publiée » : honnête, mais la règle demande la recherche. *Correction* : une recherche courte, consignée, ou le mot « question non cherchée » dans le verdict.

## Q2 — la profondeur comme surprise retirée ailleurs

**Verdict : tient.** Fait tranché à la source, propriétés exactes : symétrie de l'information mutuelle ponctuelle, borne W ≤ S(x), décomposition de Myrvold avec le terme U qui manque à la formule de Fable. Trois estimateurs, épreuves avant usage, usage borné, première épreuve avec gardes et réfutation. La demi-largeur 1,96/√2996 ≈ 0,036 est juste.

**Sondage des références.** Gu et Krenn, v4, sur le PDF du dépôt : p. 7, « 4,451 » notes sur « 5,280 » ; p. 8, « 2,996 », ρ = −0,166 (degré), −0,176 (PageRank), −0,223 (distance) : confirmés. Schupbach et Sprenger, *Philosophy of Science* 78(1), 105-127, 2011 : confirmé par Crossref.

- **Mineur (mathématiques).** « Le rapport W/S écarte les deux » (bruit et paraphrase) : faux pour la paraphrase. S petite et W ≈ S donnent un rapport proche de 1. C'est W, borné par S, qui écarte la paraphrase ; le rapport n'écarte que le bruit. *Correction* : « W écarte la paraphrase, W/S écarte le bruit ».
- **Mineur (mathématiques).** Le terme contrastif d'E1, log-cote(vrai contre faux | x) − log-cote(vrai contre faux), vaut W(x ; vrai) − W(x ; faux). C'est une différence de deux informations ponctuelles, non la puissance explicative de Schupbach et Sprenger « à une transformation monotone près ». *Correction* : « apparenté, terme vrai moins terme faux », équivalence limitée au terme vrai.
- **Mineur.** « 13 millions de jetons » pour 3 000 × 100 faits suppose le texte de l'idée mis en cache. Sinon, il faut compter environ un ordre de grandeur de plus. *Correction* : écrire l'hypothèse de cache.
- **Mineur.** Longueur environ 2 570 mots entre le verdict et les références, pour une limite de 2 500. *Correction* : resserrer ou le signaler.

## Q3 — cinétique chimique des collisions d'idées

**Verdict : à corriger.** Le dictionnaire est complet et dit où il redonne le modèle en place. Ce que j'ai refait est juste : le temps moyen `1/λ = 1/k_D + 1/k_r + k_sep/(k_D k_r)`, les deux limites, les élasticités `k_r/(k_D+k_r)`, la dérivée croisée positive (elle reste positive dans la forme générale : un signe négatif réfute toute la famille), le corollaire sur δP, le gain relatif décroissant en Z si β_c < β. La condition de rang 1 pour identifier la barrière dans le corpus est bonne. La simulation reproduit les chiffres cités.

**Sondage des références.** Peeperkorn et collègues, PDF du dépôt, p. 6, tableau 2 : nouveauté « .308±.138 » confirmé. Tria et collègues : l'exposant de Heaps égal à ν/ρ figure p. 3 (légende de la figure 1) ; le numéro « éq. (1) » n'a pas été retrouvé par extraction du texte.

- **Majeur.** La section 3 pose, pour l'organisme, un préfacteur qui dépend de la température (`ln k = ln A + m ln T − E/T`, au moins trois températures). La simulation de la section 4 (partie A) ajuste pourtant `ln A − E/T` sans terme en ln T. Sur les quatre températures 0,4 à 1,3, ln T et 1/T sont corrélés à 0,987. Avec E = 2,5 et 1 600 collisions, l'écart type asymptotique de E passe de 0,56 à 2,96 (mon calcul), soit environ 28 fois plus de collisions pour la même précision. Les ordres de grandeur « 2,63 ± 0,59 » et la puissance du test qui sépare le catalyseur du préfacteur sont donc optimistes pour le modèle que le texte exige. *Correction* : refaire la partie A avec le terme m ln T et une plage de températures plus large, ou dire que les chiffres valent seulement si m = 0.
- **Mineur.** La forme `m ln T` est empruntée à Eyring ; la normalisation du softmax (log Z_T du contexte) n'a pas cette forme. *Correction* : « forme posée, à éprouver », en même temps que la correction précédente.
- **Mineur (mathématiques).** Le premier ordre de la voie catalytique redonne γF « seulement si β_c = β » : il faut aussi que la voie catalytique porte le facteur e^{δP}, sinon le terme garde e^{−δP}. *Correction* : ajouter « et δP sur les deux voies ».
- **Mineur (entre pièces).** Le même κ sert de coefficient catalytique (et κ₀ de constante de rencontre), alors que κ désigne la part des conflits chez Fable, dans la question 7 et dans la question 9. *Correction* : renommer le coefficient catalytique.
- **Mineur.** Le renvoi de Tria « éq. (1), p. 3 » n'est pas retrouvé. *Correction* : « p. 3, légende de la figure 1 ».

## Q4 — tester l'hypothèse d'émergence

**Verdict : à corriger.** Les deux hypothèses sont bien séparées, à leur échelle. Les sources sont lues à la page. Les plans d'observation et par tirage au sort, la réfutation et l'ordre des épreuves sont donnés. Chiffres vérifiés contre la sortie : liaison 0,186 et 0,680 à 16 agents, 0,081 et 0,638 à 64 ; courbes 0,108, 0,353, 0,657 contre 0,056, 0,093, 0,165 ; puissance de 0,853 et 0,862 (K = 24, ρ = 0,05, 60 mondes) ; effet décelable de 12,1 % et 8,4 % ; coûts de 315, 631, 64, 29 et 1 794 USD. Le seuil c·f = 1 et la limite S² sont justes.

**Sondage des références.** Diehl et Stroebe 1987, PDF : « 22 experiments… 18 » (p. 497) ; tableau 5 : 55,67, 37,67, 45,67, 102,67, 106,00 ; « 96% of the variance » : confirmés. Chen et collègues, arXiv 2604.18005 (PDF du dépôt) : « plummets from 1.03 to 0.47 » confirmé.

- **Majeur.** La prédiction de percolation « sans paramètre libre » prend f dans l'épreuve de relais, avec `r(L) = h·f^(L−1)` : un saut sans perte. Le modèle de percolation (parties C2 et C3) dilue pourtant chaque arête par f, voisin direct compris (`c·f/(N−1)`). Le f mesuré n'est donc pas celui de la courbe : décalage d'un saut, qui déplace la dose efficace d'un facteur f. *Correction* : une seule définition du saut dans l'épreuve de relais et dans la percolation (par exemple `r(L) = h·f^L` si chaque arête coûte f), puis refaire les parties C2 et C3.
- **Mineur.** « Prédiction 3 de la question 3 » est l'ordre en porteurs, non la distance entre porteurs dans le graphe des coauteurs. *Correction* : dire que c'est une extension de la prédiction 3.
- **Mineur.** Plusieurs nuances ne reposent que sur des résumés ([8], [13] à [18], [20] à [24]) ; seul [9] est marqué « à vérifier ». *Correction* : l'état de lecture est déjà noté par référence ; ajouter « résumé seul » dans le texte des nuances qui portent la conclusion « le blocage manque chez des agents parallèles ».

## Q5 — Carbon contre Fable ; amender le Plan Turing

**Verdict : à corriger.** Le tableau des écarts couvre les onze thèmes, les cinq désaccords de fait, la table de dépendance et les amendements, avec ce qui ne doit pas changer. La dérivation de l'optimum de Fable est juste : `dI/dS = q[1 − ρ(1−q)(S+W)]`, et `dS*/dZ = −g_Z/g_S > 0` si W ne dépend pas de S (hypothèse bien relevée).

**Sondage des références.** Foster, Rzhetsky, Evans, *American Sociological Review* 80(5), 875-908, 2015 : résumé confirmé par Crossref (la récompense ne compense pas le risque). Wald, recension, *Physics Today* 57(9), 57, 2004 : confirmé par Crossref.

- **Majeur (symétrie, règles R4 et « même sévérité »).** Le verdict dit « Fable vérifie tout ; Carbon ne vérifie rien ». La section 4, point 2, dit pourtant que « contredite » chez Fable dépasse la source (parent pris pour la fille, question 2), et la question 2 relève que Fable cite la v3 sans coefficient. *Correction* : « Fable contrôle ses références et dépasse une fois la source ; Carbon ne contrôle pas les siennes et se trompe au moins trois fois ».
- **Mineur.** Le décompte « trois erreurs » ne colle pas à la section 4, qui en liste au moins quatre (mariage éloigné, Galison, attribution de 2008, jumeaux de Bikard), plus un dépassement partagé. *Correction* : aligner le chiffre.
- **Mineur (entre pièces).** `K = max κ·e^(−γχ)` emploie κ pour la **couverture** de Carbon, l'inverse du κ de Fable (part des conflits), que la question 9 et les corrections du 24 novembre fixent. *Correction* : écrire `κ_C` (couverture chez Carbon) et le dire en note.
- **Mineur (entre pièces).** Ligne « Objets » : « vocabulaire surtout ». La question 7 conclut à des écarts d'expression réels (Carbon l'emporte sur les critères 1 et 5) et recommande une fusion. *Correction* : « fond en partie, voir la question 7 ».
- **Mineur.** Galison : une recension (Wald) qui juge l'argument « less compellingly » ne tranche pas un fait. Elle montre seulement que « démontré » n'est pas acquis. *Correction* : « Carbon surévalue ; la source ne démontre pas », sans « Fable a raison » sur un avis.

## Q7 — la couche des problèmes et le meilleur hypergraphe

**Verdict : tient.** La prémisse est vérifiée : Carbon n'écrit pas « hypergraphe », et cela est vérifiable. Les critères sont fixés avant la comparaison, avec une règle de décision. La fusion est écrite, avec deux épreuves où les modèles divergent. La couche est typée, pondérée et couplée, avec une épreuve et une réfutation. Le couplage `δP` est cohérent avec la question 3 (voie de l'attention ou voie de la serrure) et avec la question 9.

**Sondage des références.** Wiśniewski 2001, PDF : la définition 8 (évocation) est à la page 13 du PDF, soit la p. 17 de la revue si l'article commence p. 5 ; Meheus vient juste après (p. 18) : concordant. Aliberti et collègues 2025, arXiv 2505.21476 : écart de 38(63) × 10⁻¹¹ et « no tension » confirmés sur arXiv.

- **Mineur.** Laudan, « règles de poids (p. 32-40 du livre) » et « p. 68 » : pages du livre non vu, tirées d'une source seconde, sous une forme qui ressemble à une page vérifiée. *Correction* : « pages rapportées par Moser, livre non vu ».
- **Mineur.** Le verdict de tête dit « celui de Fable est meilleur » pour la naissance par mariage. La règle de la section 3 et le tableau donnent pourtant « aucun ne domine », d'où la fusion. *Correction* : ouvrir sur la fusion, et garder « Fable meilleur sur six critères sur sept au premier tour » comme nuance.
- **Mineur.** Environ 2 790 mots entre le verdict et les références, pour une limite de 2 500. *Correction* : resserrer les sections 5 et 7.

## Q9 — exposé du graphe méta-mathématique

**Verdict : à corriger.** La pièce est pédagogique et suit le plan demandé : un fil rouge justifié, les quatre cas, trois graphes démêlés, des données réelles mesurées avec commit et empreintes, trois idées fausses, trois exercices justes (18 sur 36 ; formes (1, 1, 6) et (2, ±1, 3), donc trois classes ; échange sans effet sur le score, vérifié), ce que l'objet ne peut pas faire, et l'homonymie avec la théorie des topos. Les acquis sont repris : κ comme part des conflits, quatre cas, analogie des corrélations canoniques dite comme telle, fusion de la question 7. Le jouet est reproduit : 9! = 362 880, huit bijections au-dessus de φ, 100 à un huitième (2,76 × 10⁻⁴).

**Sondage des références.** Li, Peng, Severini, Shafto, arXiv 2604.24797 (PDF du dépôt) : 308 129 déclarations, 7 563 modules ; information mutuelle normalisée de 0,71 et 0,34, p. 5 : confirmés. Aksenov, Bodnia, Freedman, Mulligan, arXiv 2603.20396, p. 1 : la compression et une analyse de type PageRank sur mathlib « can quantify mathematical interest » : confirmé.

- **Majeur.** « Le puits est étroit » se lit sur la part globale des bijections au hasard proches du maximum, alors que l'acquis définit l'étroitesse par une perturbation locale de la correspondance (changer une ou deux paires). Mesure locale refaite : sur les 36 transpositions de φ, 16 gardent un score à un huitième près de celui de φ, 7 l'égalent ou le battent. Localement, le puits est large. « Deux perturbations… mesurées toutes deux à la section 5 » est donc inexact. *Correction* : mesurer la largeur par transpositions de φ et retirer « étroit », ou dire que la part globale mesure autre chose (la rareté au hasard).
- **Mineur.** La recherche exhaustive porte sur des bijections de neuf nœuds. Elle ne porte ni sur des injections partielles ni sur la contrainte φ(a) = b de la définition de Fable. *Correction* : le dire et préciser que la conclusion (l'absence ne coûte rien) tient aussi pour les injections partielles.
- **Mineur.** Exercice 3 : « les deux propriétés ont le même type de relation avec la composition ». Dans A, elles ont deux types (vérifie, réfute) ; c'est dans B qu'elles ont le même. *Correction* : « dans B, elles portent le même type ; les noms effacés ne les séparent plus ».
- **Mineur.** « Z, l'écart de c − κ à sa moyenne sous recâblage » : chez Fable, Z est centré **et réduit**. *Correction* : « écart réduit ».

## Contradictions entre pièces, en résumé

1. **κ** : part des conflits chez Fable, dans les questions 7 et 9 et dans les corrections du 24 novembre ; couverture de Carbon dans la question 5 ; coefficient catalytique dans la question 3. Rien n'est faux sur le fond, mais c'est le piège déjà signalé au directeur (mineurs Q3 et Q5).
2. **Hypergraphe fusionné** : les questions 7 et 9 concordent ; la question 5 classe l'écart en « vocabulaire surtout » (mineur Q5).
3. **Taux de naissance** : la forme fusionnée `log λ = log p⁰ + βZ + γF + δP` concorde dans les questions 3, 5, 7 et 9 ; la question 3 la réécrit au premier ordre d'une voie catalytique, en le disant ; rien à corriger, hormis le facteur e^{δP} (mineur Q3).
4. **Gu et Krenn, attribution de Bettencourt** : les questions 2, 4 et 5 concordent, et les chiffres sont confirmés sur le PDF.
