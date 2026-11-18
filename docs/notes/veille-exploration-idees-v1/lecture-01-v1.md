# Lecture 01 sur source — « Can a search hold its own bar? In-loop deflation and its exploits in autonomous strategy discovery » (Eray Gençay, arXiv 2611.14539) — v1

Écrite le 18 novembre 2026 (vers 05:45 UTC) par un sous-agent lecteur. Aucun commit, aucune dépense, aucun résultat sous embargo ouvert, rien dans `registres/`. Lecture entière sur PDF : pages 1 à 19, bibliographie comprise. En plus, lecture sans exécution de l'archive de code et de données que l'article cite (Zenodo), pour vérifier ce qui nous arrange.

## 0. Verdict en trois lignes

1. Le travail place un **seuil statistique de promotion dans la boucle d'une recherche menée par un modèle de langue** (ici : recherche de stratégies de bourse), l'analyse comme **un objet que la recherche peut faire bouger**, et compare ce que change le fait de **montrer ou non au critique la comptabilité du seuil**, sous un protocole dit gelé avant lancement. Cette partie de notre plan à deux bras (bras informé, bras non informé) est **occupée en partie**.
2. Il ne prend **pas** ce qui fait la forme encore revendiquée chez nous : aucun proposeur chargé de tromper, aucune description du juge donnée en texte (quatre nombres seulement), aucun monde où toute promotion est fausse par construction, aucune mesure des fausses promotions du juge face au modèle (zéro promotion dans toutes les cellules où le critique est informé). L'attaque elle-même est dérivée sur le papier et rejouée par un script sans modèle.
3. Pour la règle de promotion (revendications 1 et 2) : **voisin**. Le nul est « la chance de sélection parmi les essais de la recherche elle-même », pas un nul formé des lois connues ; aucune garantie d'erreur n'est revendiquée (l'auteur le dit) ; les candidats sont notés sur des données réutilisées, sans prédiction scellée.

## 1. Source versée

| Pièce | Chemin | Empreinte SHA-256 |
|---|---|---|
| PDF, version 1 (seule version), 19 pages, 901 726 octets | `docs/sources/pdf/veille-exploration-idees-v1/citations-arxiv-2611.14539v1.pdf` (déjà versé et scellé par la voie « citations » ; mon téléchargement de 05:29 UTC a la même empreinte, je n'ai pas versé de seconde copie) | `7d2cc0129c18697fb23ef9e3403e8652b93b0e3b2fe2a996bd9922adcb245fc3` |
| Fichier d'adresse (adresses, dates, versions, relevé de l'archive) | `docs/sources/pdf/veille-exploration-idees-v1/gencay-seuil-dans-la-boucle-arxiv-2611.14539v1/adresse.txt` | voir son compagnon `.sha256` |
| Sept extraits de l'archive Zenodo (version 1.0.1, enregistrement 21739607), non modifiés | `…/gencay-seuil-dans-la-boucle-arxiv-2611.14539v1/extraits-archive-zenodo-21739607/` : `README.md.txt`, `feedback.py.txt`, `p2_e3_full_plain.json`, `p2_e3_deflated_plain.json`, `p2_e3_deflated_hwm.json`, `endpoints.json`, `e0_calibration.json` | un compagnon `.sha256` par fichier |

L'archive entière (`p2-inloop-artifact.zip`, 4 860 437 octets, SHA-256 `4e8c16c459b2fe9b1c62c4c217fc32e6782f07499c8c65fa2926ad8312f77a84`, somme MD5 égale à celle qu'affiche Zenodo) n'est pas versée ; elle se retélécharge à l'adresse notée dans `adresse.txt`. Rien n'a été exécuté. Aucune consigne adressée au lecteur n'a été relevée, ni dans le PDF ni dans les fichiers lus de l'archive.

Dans cette fiche, « p. N » renvoie au PDF ; « archive » renvoie aux extraits versés.

## 2. Ce que le travail fait

- **La boucle** (p. 7, section 4) : un proposeur écrit un candidat (un plan de stratégie déclaratif) ; le plan est rejoué sur une fenêtre de conception (2017–2021) ; son ratio de Sharpe annualisé entre dans un registre des essais ; un critique voit un bloc de retour et oriente la proposition suivante.
- **Le seuil** (p. 5, équation 1) : le maximum attendu sous la seule chance de sélection (Bailey et López de Prado 2014), calculé sur le registre courant des essais de la recherche — dispersion des scores multipliée par un facteur qui croît avec le nombre d'essais. Un candidat est « certifié » s'il le dépasse, et le candidat rendu est revérifié contre le registre final ; sinon la course rend « no certifiable discovery ».
- **L'objet d'attaque** (p. 5-6, section 3.3) : l'article énonce une proposition selon laquelle un seuil ainsi indexé peut être abaissé par des candidats sans intérêt. Contenu non développé ici (hors sujet de cette veille).
- **Deux parades** (p. 6) : un plancher de dispersion fixé d'avance sur les registres du système précédent ; un seuil qui ne peut que monter. Et un choix : garder dans la boucle le compte nominal des essais, le compte effectif n'étant calculé qu'après coup (p. 7, section 3.6).
- **Trois axes d'expérience** (p. 9, tables 1 et 2) : la porte (avec ou sans) ; la règle d'arrêt (budget fixe, arrêt lu sur le seuil, budget adaptatif) ; ce que voit le critique (métriques brutes ; métriques et comptabilité du seuil ; retour quantifié à la manière de Blum et Hardt), croisé avec le mode du seuil.

## 3. Verdicts, revendication par revendication

| Revendication du programme | Verdict | Preuve (page, citation courte) |
|---|---|---|
| **14, plan à deux bras** — un bras qui reçoit les verdicts du juge statistique, un bras qui ne les reçoit pas | **occupé en partie** | p. 7, section 3.5 : « Deflated feedback additionally shows the live accounting: the bar, the excess over it, trials spent, and wealth remaining » ; « We pre-register this as a two-sided prediction ». Archive : les configurations `p2_e3_full_plain.json` et `p2_e3_deflated_plain.json` ne diffèrent que par la ligne `"feedback"`. Le signe de l'excès sur le seuil est un verdict servi à chaque essai. Mais le chercheur n'est pas adverse (ligne suivante). |
| **14, proposeur modèle de langue chargé de tromper le juge, qui lit sa description exacte** | **voisin** (non pris) | Aucun modèle n'a pour mission de tromper : p. 6, « whether a given searcher acts on it is an empirical question ». L'attaque est rejouée par script : p. 13, « The stress test is deterministic… a scripted flood » ; p. 9, table 2, « E4 is deterministic and uses no LLM ». Le critique informé reçoit quatre nombres, pas la règle : archive, `feedback.py.txt`, clés `search_bar`, `search_excess`, `search_trials_spent`, `search_wealth`. |
| **14, mondes où toute promotion est fausse ; mesure des fausses promotions du juge sous attaque** | **voisin** (non pris) | Données de marché réelles, sans vérité plantée : p. 17, « the suite contains no planted true edge, so the false-negative cost of the gate and its defences is not measured here ». Dans les cinq cellules de l'axe « ce que voit le critique », aucune certification (p. 11, table 3, colonne « Certified » à 0.00) : ce qui est mesuré est un comportement (taux de quasi-doublons), pas une erreur du juge. Les promotions sous attaque ne sont comptées que dans le rejeu scripté (p. 13 ; p. 14, table 4 : « 4/1/1 » sur douze trajectoires). |
| **1, juge au nul formé des lois connues** (« rien au-delà de l'archive ») | **voisin** | p. 5 : « 𝐵𝑘 estimates the best Sharpe ratio that selection luck alone would be expected to produce, given how many candidates have been tried and how dispersed their scores are ». Le nul est le bruit de sélection sur les essais de la recherche ; aucune archive de lois ou d'anomalies connues n'entre dans le seuil. Les stratégies de référence (momentum, indice) ne sont que des bras de comparaison (archive, configurations). |
| **2, grille en cinq éléments de la règle de promotion** | **occupé en partie** (deux éléments sur cinq, plus la multiplicité déjà cédée) | (i) propositions écrites par un modèle : pris, p. 7. (v) statistique hors des agents : pris, p. 7-8, « Each entry is a pure function of the recorded ledger state », rejeu exact de chaque décision. (iii) garantie valide à tout instant d'arrêt : **non revendiquée**, p. 4 « we do not claim a false-discovery-rate guarantee from it » ; p. 17 « not a formal error rate for the composite procedure » ; la voie des e-valeurs est renvoyée à plus tard (p. 4, 7, 14). (ii) nul des lois de l'archive : absent. (iv) prédictions scellées avant les données : absent, les candidats sont notés sur la fenêtre de conception réutilisée (p. 5), la fenêtre tenue à l'écart ne sert qu'au critère externe (p. 9). |
| **11 et 15, appui sur Blum et Hardt** (retour quantifié contre l'analyste adaptatif) | **voisin** | p. 3 : « a mechanism our ladder feedback policy adapts for the critic » ; p. 7. Une cellule, trois répétitions, taux de quasi-doublons au niveau de base (p. 12) : mis en œuvre, effet non distingué. |
| **6, mondes plantés comme arbitre** | non touché ; l'article nomme leur absence comme limite | p. 17 (citation ci-dessus). |

Revendication de nouveauté de l'auteur, à connaître : p. 4, « We are not aware of prior work that places the multiplicity correction inside an autonomous search loop, analyses the loop's incentive to game it, defends against that incentive, and measures the result under a pre-registered protocol. That combination is the contribution. » Elle recouvre la forme générale « juge statistique dans la boucle, étudié comme cible, sous protocole gelé », pas notre forme resserrée.

## 4. Ce qui est mesuré, par qui c'est jugé, ce qui est publié

**Mesuré** (chiffres lus sur le PDF ; ceux marqués « archive » recoupés dans `endpoints.json`) :
- 53 courses « auditées » de cent candidats au plus, deux modèles (GPT-4.1 partout, Claude Sonnet 5 sur les cellules de tête), 453 actions américaines, 39 fonds indiciels, et une cellule exploratoire ajoutée après le gel (p. 9, tables 1 et 2). Coût total d'environ 160 dollars (p. 10).
- **Critère principal, indépendant du seuil étudié** (p. 9, section 5.3) : ratio de Sharpe hors échantillon de la stratégie retenue, avec intervalle à 95 % par bootstrap stationnaire, 1000 tirages. Jugé par un script, aucun juge modèle.
- Résultat central : la recherche à porte rend « rien de certifiable » sur 36 courses sur 37, les témoins sans porte rendent une stratégie sur leurs 16 courses, et tous les intervalles contiennent zéro (p. 10 ; p. 11, table 3 ; archive : 37 courses à porte, 36 non certifiées, une certifiée, aucun intervalle n'exclut zéro).
- Axe « ce que voit le critique » : taux médian de quasi-doublons (corrélation d'au moins 0,95 avec un essai antérieur) de 0,69 quand le critique voit la comptabilité contre 0,65 quand il ne voit que les métriques, sous le seuil qui peut baisser ; 0,64 sous le seuil qui ne peut que monter ; 0,64 avec le retour quantifié (p. 12). Trois répétitions par cellule, un seul modèle.
- Arrêt lu sur le seuil : 8 à 9 essais au lieu d'une centaine, sans différence visible hors échantillon ; le budget adaptatif ne s'arrête jamais plus tôt (p. 11-12).
- Rejeu scripté, sans modèle, sur douze trajectoires enregistrées : l'effet et les deux parades sont reproduits (p. 13 ; p. 14, table 4).
- Dépendance entre essais : une centaine d'essais nominaux pour 6 à 8 trajectoires de rendement effectivement indépendantes et 22 à 44 hypothèses distinctes (p. 14).

**Publié** : archive Zenodo (code sous licence MIT, données sous CC BY 4.0) : la couche de comptabilité, les tests, les configurations, les manifestes et traces des 53 courses, les fichiers de résultats, le générateur de figures. **Non publié** : la plateforme de découverte (moteur de rejeu, chaîne de données, bibliothèque de traits), donc les textes servis aux modèles, et les matrices de rendements des candidats, « available from the author on reasonable request » (p. 18 ; archive, `README.md.txt`). Conséquence : les taux de quasi-doublons, qui portent le résultat le plus proche de nous, ne se recalculent pas depuis l'archive ; on ne peut que les relire dans le fichier de résultats.

**Seulement affirmé** :
- Le gel du protocole « by commit before any suite run » (p. 2, p. 8). L'archive ne contient ni l'historique git ni le document de conception gelé. Voir la section 6.
- La leçon générale (« a statistic placed inside a search loop becomes something the search can optimise against », p. 16) : l'auteur la donne comme suggestion, « not as theorems ».
- L'absence de précédent : « to our knowledge » (p. 1, p. 3-4).

## 5. Date de première version

- **Article** : arXiv, version 1 du **14 octobre 2026** (20:21 UTC), seule version (page de résumé, interface d'arXiv et tampon du PDF concordent ; la version 2 n'existe pas).
- **Écart signalé dans la tâche** : l'identifiant commence par 2611 alors que la date est d'octobre. Les identifiants voisins portent le même écart (2611.14538 daté du 14 octobre, 2611.14540 daté du 18 octobre, interface d'arXiv, 18 novembre 2026) : l'écart n'est pas propre à ce travail, et je ne l'explique pas. Le PDF servi a été produit par arXiv le 13 novembre 2026 (métadonnées), ce qui ne date pas la mise en ligne. **Je retiens le 14 octobre 2026 comme date affichée, avec cette réserve** pour tout usage d'antériorité au jour près.
- **Première trace publique du travail** : l'archive de code et de données, qui porte déjà le titre de l'article, version 1.0.0 créée sur Zenodo le **31 juillet 2026** ; version 1.0.1 le 1er août 2026. Les courses sont datées du 17 au 19 juillet 2026 (manifestes de l'archive).
- Dans tous les cas, le travail précède nos décisions N-064 et N-065 (9 novembre 2026) et N-067 (13 novembre 2026).

## 6. Limites — lecture dure de ce qui nous arrange et de ce que l'article avance

Ce qui nous arrange (« la forme resserrée n'est pas prise ») tient, avec trois réserves :
1. **Les textes servis aux modèles ne sont pas publiés.** Le code montre que le bloc de retour ne porte que quatre nombres ; je n'ai pas pu vérifier qu'aucune phrase de la consigne du critique ne décrit le seuil. « Pas de description du juge en texte » est vérifié sur le bloc de retour, pas sur la consigne.
2. **Le signe de l'excès est un verdict.** Un lecteur sévère dira que « comptabilité montrée contre non montrée » est déjà « verdicts servis contre non servis ». Notre différence tient donc au proposeur adverse, à la description exacte du juge, aux mondes négatifs par construction et à la mesure des fausses promotions — pas au plan à deux bras lui-même.
3. **Un seul travail lu.** Ce verdict ne dit rien des travaux qui le citeront ni de la suite annoncée par l'auteur (voie des e-valeurs).

Ce que l'article avance et qui est plus faible qu'il n'y paraît :
- **L'effet de l'information est dans le bruit.** Par répétition (archive, `endpoints.json`, champ `near_duplicate_rate_corr`) : métriques seules 0,70 ; 0,59 ; 0,65 — comptabilité montrée 0,71 ; 0,62 ; 0,69. Les étendues se recouvrent. L'auteur le dit : « we do not attach significance to the differences » (p. 12), « our weakest result » (p. 15), écart de +0,00, +0,04 et +0,01 selon le seuil de corrélation (p. 15 ; table 5, p. 16). Un seul modèle porte la grille (p. 13).
- **Le modèle n'a jamais affronté le seuil naïf.** Dans le texte, « plain bar » désigne le seuil sans plancher (p. 5) ; dans les configurations des cellules à modèle, `bar_mode` vaut `plain` avec le plancher à 0,1204 (archive). Le seuil sans plancher n'est éprouvé que par le script.
- **Les « graines » sont des répétitions à température par défaut**, non rejouables (p. 8 ; archive, descriptions des configurations) ; le modèle Claude rend plusieurs fois la même stratégie (p. 17).
- **Pas de vérité connue** : le coût en vraies découvertes manquées n'est pas mesuré (p. 17) ; les intervalles ont une demi-largeur médiane d'environ 0,9 (p. 17), donc « contient zéro » n'écarte que les très gros effets.
- **Pas de garantie d'erreur** pour la procédure d'ensemble (p. 17).
- **Le gel n'est pas vérifiable depuis l'archive.** Les 53 manifestes portent cinq versions de code différentes, toutes avec le suffixe `-dirty` (dans l'usage de git : arbre de travail modifié et non enregistré ; lecture d'usage, non confirmée par l'auteur). Le fichier de calibration du plancher livré est daté du 30 juillet 2026, après les courses des 17 au 19 juillet ; sa valeur est celle des configurations, ce qui est compatible avec une régénération à l'identique, mais l'ordre « calibré avant toute course » ne se prouve pas avec ce qui est livré. L'article reconnaît des amendements après gel, dont « a feedback-delivery clarification » (p. 8), sur l'axe même qui nous concerne.
- Prépublication d'un auteur seul, sans relecture par les pairs ; les bras partagent données et plans de départ et ne sont pas des répétitions indépendantes (p. 17).

## 7. Idée à prendre

**Une échelle d'information à trois degrés, lue sur l'oracle du monde planté.** Pour notre comparaison « bras informé, bras non informé », ajouter le degré intermédiaire que l'article met en œuvre : un retour quantifié à la manière de Blum et Hardt (« a progressé d'au moins un pas, ou non »), entre « aucun verdict » et « verdicts complets ». Garder de l'article trois choix de protocole : (a) un critère principal qui ne dépend pas du juge étudié (« This avoids grading a system with the very instrument under study », p. 2) — chez nous l'oracle du monde planté, que l'article n'a pas ; (b) une prédiction bilatérale gelée dont le signe dépend du mode du seuil, avec une clause écrite d'avance selon laquelle « aucun effet mesurable » est un résultat recevable (p. 9) ; (c) en critère secondaire, le taux de propositions quasi identiques et le nombre effectif de propositions indépendantes, rapportés à côté du compte nominal et jamais branchés dans la règle (p. 7, p. 14). L'avertissement qui va avec : à trois répétitions par cellule, l'auteur n'a pas pu distinguer un écart de 0,04 du bruit entre répétitions ; notre pilote de bruit doit dimensionner le nombre de répétitions avant de geler quoi que ce soit.

En appui, sur processeur et sans modèle : vérifier par un test de propriété, sur des trajectoires enregistrées, qu'aucune grandeur du seuil de notre juge ne dépend d'une statistique des propositions elles-mêmes (c'est la leçon de conception de la p. 16 : préférer des instruments qui ne peuvent pas être poussés dans le sens favorable).

## 8. Propositions (rien n'est décidé ici ; modifier une revendication est un nœud de Lazar)

1. Ajouter ce travail aux citations obligatoires de tout texte qui présente l'attaque contre le juge statistique et le plan à deux bras.
2. Dire le plan « bras informé, bras non informé » comme pris dans sa forme non adverse par ce travail, et ne garder en propre que : proposeur chargé de tromper, description exacte du juge, mondes où toute promotion est fausse, mesure des fausses promotions.
3. Le prédécesseur du même auteur (« What survives honest evaluation? », Zenodo, DOI 10.5281/zenodo.21559496, page datée du 25 juillet 2026 ; la table de la voie « citations » le donne aussi sous arXiv 2608.27734) n'a pas été lu : il porte la correction après coup, pas dans la boucle.

## 9. Réserves de cette fiche

- Les chiffres viennent du PDF lu en entier, page citée ; ceux recoupés dans l'archive le sont sur le fichier de résultats livré par l'auteur, pas par recalcul depuis les traces (rien n'a été exécuté).
- La lecture de l'archive est partielle : sept fichiers versés, plus un relevé par programme des 53 manifestes et la lecture d'une trace. Les autres modules n'ont pas été lus ligne à ligne.
- Les verdicts « voisin » et « occupé en partie » portent sur ce seul travail (R8) ; « non pris » veut dire « non trouvé dans cette pièce ».
