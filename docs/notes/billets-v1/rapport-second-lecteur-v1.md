# Rapport du second lecteur du tri à la lecture (corpus v2) — v1

Écrit le 2026-11-18 par un sous-agent neuf (Opus 5.5), second lecteur, selon le mandat `mandat-second-lecteur-tri-v1.md` (`e5c238ac…`, compagnon vérifié). Règle appliquée : `regle-tri-a-la-lecture-v2.md` (`8ec15a60…`, compagnon vérifié), sections 2, 3 et 5. Échantillon : `echantillon-second-lecteur-v1.json` (`2dfa7f74…`, compagnon vérifié), 100 billets.

## 1. Ce qui a été fait, dans l'ordre
1. Lecture structurée des 100 billets, en aveugle : titre, mots, images, en-tête (aide `scripts-v2/lire_v2.py`), intertitres, passages à nombres, et, pour une vingtaine de cas serrés, passages choisis du corps sous `/home/user/billets-corpus-v2/tous-textes/` (position des sections, légendes, quelques paragraphes). Aucun commentaire lu, aucune copie de texte. Un petit script de vue (intertitres soulignés, légendes, phrases à nombres) a servi d'aide ; il est resté dans le dossier temporaire de la session, hors dépôt.
2. Journal écrit puis scellé : `journal-second-lecteur-v1.jsonl`, `9e3197cf930e1982c868c4a4ce61ac194b452a6ad40d02dabba7da6aae79c922`. Bilan : 46 « oui », 54 « non », 18 motifs marqués « limite ».
3. Seulement ensuite : comparaison par `scripts-v2/comparer_second_lecteur_v1.py`, sortie scellée `accord-second-lecteur-v1.json`, `0e6f97c1754cfe0cdec634c183b14faa869eda1d57f8014b4290805862929794`. Aucune décision changée après. Puis lecture du journal du premier lecteur pour les seuls 100 identifiants de l'échantillon (aucun doublon parmi eux).

## 2. Accords (source : `accord-second-lecteur-v1.json`, `0e6f97c1…`)
| Groupe | n | Accord brut | Kappa de Cohen | Table premier/second (oui/oui, oui/non, non/oui, non/non) | Désaccords |
|---|---|---|---|---|---|
| Lignes tirées au hasard (hors « limite » du premier lecteur) — seules extrapolables | 72 | 0,972 | 0,941 | 26, 1, 1, 44 | 2 |
| Cas « limite » du premier lecteur | 28 | 0,679 | 0,241 | 15, 5, 4, 4 | 9 |
| Ensemble | 100 | 0,89 | 0,779 | 41, 6, 5, 48 | 11 |

Lecture : hors cas serrés, les deux lecteurs s'accordent presque toujours. Sur les cas que le premier lecteur jugeait serrés, l'accord ne dépasse guère le hasard (kappa 0,24). Les désaccords n'ont pas de sens privilégié (6 « oui » du premier devenus « non », 5 dans l'autre sens). Les 11 désaccords portent tous une mention « limite » chez l'un au moins des deux lecteurs : la mention repère bien les cas fragiles.

## 3. Les onze désaccords
| Identifiant | Premier lecteur | Second lecteur | Clause de la règle qui les sépare |
|---|---|---|---|
| `xtpcJjfWhn3Xn8Pu5` (jetons anormaux de DeepSeek ; tiré au hasard) | oui — « jetons anormaux testés, figures » | non — « limite : catalogue qualitatif de jetons, captures, aucun décompte » | Définition de la « figure de résultat » (section 2) contre « étude de cas qualitative sans mesure… non, sauf décompte » (section 3) : des captures d'écran de sorties de modèle comptent-elles comme figure ? |
| `9FH49ZgJFW4WtbxLi` (lois d'échelle d'un modèle jouet d'apprentissage par renforcement ; tiré au hasard) | non — « modèle jouet théorique » | oui — « limite : simulation du modèle jouet au cœur, lois d'échelle » | « Exposé théorique avec simulation : oui si la simulation est le cœur » contre « exemple jouet : non » (section 3). |
| `bQkp4pi5Ra4SgSSxn` (idées naturelles, programme d'été) | oui — « limite : expériences chiffrées de précision, figures » | non — « limite : petites expériences chiffrées minoritaires dans essai conceptuel » | « Objet principal : plus de la moitié du corps » (section 2) ; la partie expérimentale occupe environ 30 % du texte (position des intertitres), le reste est conceptuel et projets futurs. |
| `3ecs6duLmTfyra3Gp` (leçons de l'étude du circuit d'identification de l'objet indirect) | oui — « limite : leçons tirées d'un circuit mesuré, pourcentages » | non — « limite : leçons méthodologiques, résultats d'article seulement résumés » | « Annonce d'article : oui si chiffres » contre « objet principal » : un billet de leçons adossé à l'article des auteurs, avec quelques chiffres, est-il une annonce d'article ? |
| `TDqvQFks6TWutJEKu` (vers la monosémanticité, billet d'annonce) | non — « limite : annonce d'article, sans résultat chiffré » | oui — « annonce d'article avec figures de résultats des auteurs » | « Annonce d'article : oui si résultats chiffrés **ou figures** » : le billet montre les graphiques d'évaluation (scores humains et automatiques, traits contre neurones) sans nombre dans le texte. |
| `7k3xBdhHb546oLBv4` (organismes modèles trompeurs résistant à l'audit) | non — « limite : exigences de conception, peu de résultats » | oui — « annonce d'article avec figure d'évaluation des auteurs » | « Objet principal » et « annonce d'article » : la section d'évaluation, avec figure de précision d'élicitation, suffit-elle face aux exigences de conception ? |
| `JFw35W7xnsSiZNTnc` (auto-préservation et ambiguïté des consignes) | non — « limite : argument sur expériences d'autrui » | oui — « réplication modifiée des auteurs, figures de taux » | « Réplication : oui si les auteurs rapportent leurs propres chiffres » ; les auteurs disent avoir repris le code public, joué cinq variantes sur cinq modèles, dix tirages chacune, et montrent trois graphiques de taux. Le second lecteur pense que la règle donne « oui » ici. |
| `jfG6vdJZCwTQmG7kb` (la normalisation de couche revisitée) | oui — « limite : mesures sur couche de normalisation, figures » | non — « limite : exposé géométrique illustré, pas d'expérience mesurée centrale » | « Exposé théorique avec simulation » et « schéma conceptuel » : les animations géométriques sont-elles des résultats ou des illustrations ? |
| `s7uD3tzHMvD868ehr` (discriminer des classifieurs de même comportement) | oui — « limite : problème modèle avec résultats chiffrés de sa méthode » | non — « limite : programme de recherche, résultats chiffrés en section minoritaire » | « Essai dont une section centrale rapporte une expérience : oui si plus de la moitié ou résumé en tête » ; la section chiffrée occupe environ 20 % du texte, le résumé en tête annonce un programme. |
| `iQaGXCSQaKYmneZGo` (représentations apprises de maladies du riz) | oui — « limite : rapport d'étape avec courbe de perte » | non — « limite : rapport d'étape surtout plans, une courbe » | « Bilan d'un projet : oui si chiffres ou figures comme objet principal » : une seule courbe de perte, le reste est un plan de travail. |
| `x8BbjZqooS4LFXS8Z` (zoo de petits modèles non interprétés) | non — « limite : présentation de problèmes ouverts » | oui — « limite : publication de modèles, études de cas chiffrées » | « Objet principal » : la publication de modèles et le défi final contre les études de cas chiffrées (précisions, estimations mécanistes) qui occupent la plus grande part du corps. |

Le corpus ne change pas : ces onze billets sont marqués, et la suite rapportera ses résultats avec et sans eux.

## 4. Ce que la règle devrait préciser
1. **Mesure de « plus de la moitié du corps »** : dire comment on la mesure (part du texte en caractères entre intertitres, figures comprises ou non). Trois désaccords (`bQkp…`, `s7uD…`, `x8Bb…`) tiennent à cette proportion estimée à vue.
2. **Ce qu'est une figure de résultat** : dire si des captures d'écran de sorties de modèle comptent (`xtpc…`), et confirmer qu'un graphique de résultat suffit sans nombre dans le texte (`TDqv…`).
3. **Modèle jouet simulé** : départager « exemple jouet : non » et « exposé théorique avec simulation au cœur : oui » quand le billet entier est la simulation d'un modèle jouet avec résultats numériques (`9FH4…`, `jfG6…`).
4. **Billets adossés à un article des auteurs mais centrés ailleurs** (leçons, programme, défi) : dire s'ils relèvent de « annonce d'article » ou de l'essai (`3ecs…`, `s7uD…`, `7k3x…`, `x8Bb…`).
5. **Rapport d'étape** : fixer un seuil (une seule courbe face à un plan de travail suffit-elle ?) (`iQaG…`).
6. **Réplication avec variantes** : rappeler qu'un billet qui rejoue le code d'autrui avec ses propres variantes et ses propres chiffres est une réplication, même si son titre est argumentatif (`JFw3…`).

## 5. Limites
Second lecteur unique, lecture non intégrale, comme le premier. Les proportions de sections citées sont estimées par la position des intertitres dans le texte, pas mesurées finement. Le kappa des cas « limite » repose sur 28 billets et reste très incertain.
