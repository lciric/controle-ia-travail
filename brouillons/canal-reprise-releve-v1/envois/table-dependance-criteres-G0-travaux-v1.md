# Table de dépendance « critères de G0 → travaux du programme » — v1

**Provenance.** Écrite le 29 octobre 2026 par une main neuve, à partir de la seule liste des travaux de la phase 0 (noms et périmètres, jamais les résultats), des huit critères de G0 du programme v2 et de la clause de repli recommandée par l'avis de conv-audit. Elle est écrite **avant tout verdict de G0** et ne dépend d'aucun résultat des critères encore ouverts : elle classe les travaux selon ce dont ils ont besoin, pas selon l'état où se trouve chaque critère.
**À faire avant usage : sceller ce fichier avant le verdict de G0, puis le faire contre-lire (R2) par un sous-agent neuf.** Après scellement, aucun reclassement : un changement passe par une version nouvelle et un nœud de décision, jamais après le verdict.

## 1. Les huit critères de G0

| n° | critère |
|---|---|
| 1 | harnais validé |
| 2 | organismes avec dose-réponse |
| 3 | sondes au-dessus du plancher |
| 4 | base boîte noire opérationnelle |
| 5 | agrégateurs validés en simulation |
| 6 | préenregistrement de G1 scellé et contre-lu |
| 7 | préenregistrement du papier C scellé et contre-lu |
| 8 | état de l'art vérifié |

## 2. Définitions des trois classes

- **Dépend** de k : le travail ne peut pas se faire honnêtement si le critère k n'est pas tenu.
- **Sert** k : le travail contribue à tenir k (il n'en dépend pas pour autant).
- **Continue sous repli** : ne dépend d'aucun critère ; permis sans dépense externe s'il ne sert aucun critère non tenu, **permis sur devis et GO** s'il en sert un.
- **Fermé sous repli** : expérience décisive de G1 ou du papier C, ou tout travail qui lit un résultat de G1.
- **Conditionnel** : continue seulement si **tous** les critères dont il dépend sont tenus au verdict ; sinon fermé. Si, en plus, il sert un critère non tenu, il peut dépenser sur devis et GO tant qu'il reste ouvert.

## 3. Table des travaux

| réf. | travail | dépend | sert | classe |
|---|---|---|---|---|
| W1 | T0.1 socle, gouvernance, registres, passations ; rapport de porte et verdicts de porte | — | transversal | continue |
| W2 | T0.2 : reste de l'état de l'art — documents hors arXiv (Panin, affiche, billets), contrôle de traçabilité par sous-agent neuf | — | 8 | continue |
| W3 | Veille hebdomadaire ; lecture des pistes signalées (dont 2603.02798 pour H2) | — | 8, 6 | continue |
| W4 | Collisionneur (recherche de collisions des revendications avec la littérature) | — | 8 | continue |
| W5 | Moissonneur (voir cas C3) | — | 8 | continue, à confirmer |
| W6 | T0.3 simulation du lemme et du théorème négatif : reprise éventuelle, note mathématique | — | 5 | continue |
| W7 | T0.4 harnais et journalisation des activations | — | 1 | continue |
| W8 | T0.5 environnement (a) v0 : pilote, lecture, verdict | 1 | 2, 4 | conditionnel |
| W9 | T0.6 organismes v0 : code, préenregistrement, runs, dose-réponse | 1 | 2 (3, 4 : fournit leurs données) | conditionnel |
| W10 | T0.7 sondes v0, bras principal sur données génériques, témoins (T7-P9, T7-P10) | 1 | 3 | conditionnel |
| W11 | T0.7 sondes, lectures de généralisation sur activations de T0.6 (T7-P6 à P8) | 1, 2 | — (sans effet sur 3) | conditionnel |
| W12 | T0.8 bases boîte noire v0 : invites, planchers, TRACE-lite, run sur épisodes de T0.6 | 1 | 4 | conditionnel |
| W13 | P3 premier test boîte blanche (i-a) | 1, 3 | — | conditionnel |
| W14 | Préenregistrement de G1 : rédaction, contre-lecture, scellement (sans l'exécuter) | 5 | 6 | conditionnel |
| W15 | Couche 2 : conception, code, banc sur données synthétiques | 5 | 6 | conditionnel |
| W16 | Course d'idéation de l'organisme (sous-agents neufs, texte seul, sans accès aux sondes ni à leurs données) | — | 2 | continue (voir C1) |
| W17 | T0.9 papier C, partie préenregistrement : conception, HC1 à HC3, lecture de Panin, contre-lecture, scellement | — | 7, 8 | continue |
| W18 | T0.9 papier C, pilote (suspendu au scellement) | 1, 7 | — | conditionnel |
| W19 | Papier A : rédaction hors résultats de la phase 1 (cadre, énoncés, antériorité) | 5, 8 | 8 | conditionnel |
| W20 | Papier B : conception et rédaction hors expérience, dont H9 sous réserve d'antériorité | 8 | 8 | conditionnel |
| W21 | Tour (c) (voir cas C4) | non établi | — | fermé par défaut |
| W22 | Couche 2 / G1 : exécution sur organismes réels, porte G1, toute lecture de résultat de G1 | 1 à 6 | — | **fermé** |
| W23 | Phase 1 : E1.1 à E1.7 (organismes finalisés, plan 2 × 2, lemme sur données réelles, théorème négatif semi-synthétique, attaques adaptatives, marge asymétrique, transfert concentré) | 1 à 6 | — | **fermé** |
| W24 | Papier C : expériences décisives (HC1 à HC5, porte GC) | 7 et suivants | — | **fermé** |
| W25 | Papier B : toute expérience | 8, G1 | — | **fermé** |
| W26 | Tout travail absent de cette table | — | — | **fermé** (voir §4, règle 4) |

## 4. Règle de lecture mécanique

Au verdict, soit **N** l'ensemble des critères que le verdict ne déclare pas tenus. « Non franchie » et « non concluante » comptent de la même façon : le critère est dans N.

1. Un travail **fermé** est fermé, quel que soit N.
2. Un travail **conditionnel** est fermé si au moins un de ses critères de la colonne « dépend » est dans N ; sinon il continue.
3. Un travail **continue** continue. Il peut dépenser (devis et GO) seulement s'il sert au moins un critère de N ; sinon, sans dépense externe.
4. Un travail absent de la table est fermé. Aucun reclassement, aucune exception, aucun jugement après le verdict.

Lecture inverse, pour contrôle : travaux conditionnels fermés par un critère de N.

| critère dans N | travaux conditionnels fermés en plus des fermés permanents |
|---|---|
| 1 | W8, W9, W10, W11, W12, W13, W18 |
| 2 | W11 |
| 3 | W13 |
| 4 | aucun |
| 5 | W14, W15, W19 |
| 6 | aucun |
| 7 | W18 |
| 8 | W19, W20 |

Si deux critères sont dans N, on prend l'union des lignes. Les critères 4 et 6 ne ferment rien de plus : leur absence ferme déjà G1 (W22, W23) ; ils ouvrent seulement le droit de dépenser sur devis pour W12 (4) et W14, W15 (6).

## 5. Cas ambigus, avec proposition

| cas | question | proposition | pourquoi |
|---|---|---|---|
| C1 | La course d'idéation dépend-elle du critère 2 ? | Non : continue (W16), texte seul, sans dépense ; son entraînement éventuel appartient à E1.1 (W23, fermé). | Elle produit des idées de stratégie, pas des organismes calibrés. Ne pas la fermer évite de perdre un mois ; la fermer ferait de la dose-réponse une condition d'un travail qui ne la lit pas. Condition : aucune sortie de la course n'entre dans un run avant G0. |
| C2 | La couche 2 dépend-elle de 3 et 4 ? | Séparer : conception, code, banc synthétique (W15) ne dépendent que de 5 ; l'exécution sur organismes réels (W22) dépend de 1 à 6 mais est fermée de toute façon. | Les critères 3 et 4 qualifient des instruments qu'on lit en exécution, pas en conception. |
| C3 | Le moissonneur. | Continue (W5) comme collecte de sources publiques au service du critère 8, sans dépense. **Le terme n'est pas défini dans les trois fichiers lus** : le contre-lecteur doit confirmer sa définition ; sinon la ligne passe à W26 (fermé). | Une collecte de textes ne lit aucun résultat. Mais classer ce qu'on ne sait pas définir serait un jugement. |
| C4 | Le tour (c). | Fermé par défaut (W21), faute de définition dans les trois fichiers lus. Le contre-lecteur qui le définit le reclasse **avant** scellement, jamais après. | Un travail non défini ne peut pas être déclaré indépendant d'avance. |
| C5 | T0.8 : le run sur les épisodes de T0.6 dépend-il du critère 2 ? | Non (W12 dépend de 1 seulement). | Le critère 4 demande une base opérationnelle (elle tourne, calibrée, sans fuite) ; il ne demande pas que les organismes soient calibrés. Si le contre-lecteur juge que « opérationnelle » suppose des organismes calibrés, ajouter 2 à W12. |
| C6 | P3 : dépend-il de 3, et ne préfigure-t-il pas G1 ? | Dépend de 1 et 3 (W13) ; non fermé comme G1, parce que c'est un premier test préenregistré à saboteur instruit, avec témoin, hors porte G1. | Si 3 est dans N, les sondes lues n'ont pas de plancher établi. Risque : lire P3 comme un résultat de G1. Garde : aucun résultat de P3 ne modifie le préenregistrement de G1 une fois scellé. |
| C7 | Pilote du papier C : dépend-il de 7 ou le sert-il ? | Dépend de 7 (W18). | Le fichier des tâches le dit suspendu au scellement ; il ne peut pas aider à sceller ce qu'il attend. |
| C8 | La rédaction des papiers dépend-elle du critère 8 ? | Oui (W19, W20) ; le papier C est couvert par W17. | R7 : aucun chiffre de la littérature sans vérification ; un papier écrit sur un état de l'art non vérifié contrevient à la règle. |
| C9 | Préenregistrement de G1 : dépend-il de 4 ? | Non (W14 dépend de 5 seulement). | On écrit la comparaison sans lire les bases ; le contre-lecteur vérifie que le texte ne suppose aucun résultat de W12. |

## 6. Réserves

- Non contre-lue (R2) ; non scellée à l'écriture.
- Classes établies sur les noms et périmètres de travaux seuls ; « couche 2 », « collisionneur », « moissonneur » et « tour (c) » sont pris au sens de la demande, sans définition vérifiée dans les fichiers lus (cas C3, C4).
- La règle 3 (dépense seulement pour les travaux qui servent un critère de N) reprend la clause recommandée par l'avis ; si la clause scellée dit autre chose, c'est la clause qui prime.
- Constat à signaler : avec seulement les critères 2, 3, 4, 6 ou 7 dans N, la table ferme très peu en plus de G1, de la phase 1 et du papier C (au plus W11, W13 ou W18) ; elle laisse donc le travail courant presque intact. C'est une conséquence de la table, non un choix à corriger après coup.
