# Journal des corrections du protocole de veille — de la v1 à la v2

- **Écrit** le 13 novembre 2026 par le rédacteur des deux versions (Claude Opus 5.5), avec la v2.
- **Entrées** : contre-lecture `contre-lecture-protocole-veille-v1.md` (`f76596ca8062e20b…`, R-2574 ; 25 couples « texte actuel →
  texte corrigé », 3 bloquants, 13 majeurs, 14 mineurs) ; décisions de Lazar R-2570, R-2571, R-2573 ; message de la mère
  (exigences B1, M1, B3, M3, M4, M6, R4, M2, M5, M7, B2, M8 à M13, mineurs).
- **Sortie** : `protocole-veille-concurrentielle-v2.md` ; la v1 reste intacte (`37e335d6…`, R12).
- **Règle** : chaque couple est **appliqué**, **appliqué sous une forme adaptée** (le but est tenu, le texte diffère, raison
  donnée) ou **écarté** (raison donnée). Un couple peut être appliqué en partie : chaque partie est dite.

## 1. Les 25 couples

| n° | constat | lieu dans la v1 | sort | lieu dans la v2 | raison ou précision |
|---|---|---|---|---|---|
| 1 | B1 | § 1.4, « Signatures identiques à la section 1.3, sauf » | **appliqué sous une forme adaptée** | § 1.4 ; annexe A ; `annexe-a-signatures-retro-v1.py` | La mère exige une **règle mécanique** : les signatures sont produites par un script à lexique figé sur le seul programme v2, au lieu d'être écrites par un sous-agent qui n'a lu ni la liste ni la synthèse. Le texte « cédé » est la phrase du programme lui-même (aucun identifiant, aucun resserrement). Garde des identifiants `2609.*` à `2611.*` testée sur un cas sain et sur un artefact. **Déclaré** : le lexique est du rédacteur, qui connaît la liste ; un seul changement après le premier passage (règle de coupe, bogue sur « existe » et « établi ») ; aucune décision n'est datée d'avant le 1er octobre (les premières, le 4 octobre), et le programme v2 et l'état de l'art v1 portent le 4 octobre. |
| 2 | B2, fait 1 | § 4.4, « Aucun énoncé du programme n'est envoyé… » | **appliqué sous la forme décidée par Lazar** | § 4.4 ; § 2.0, point 2 | R-2570 tranche la voie (i) : lecteurs sous-agents Claude, rien ne sort. La voie (ii) du couple (lecteurs extérieurs sur consigne accordée mot pour mot) est **retirée**, sans objet. La garde de sortie devient une garde des hôtes : aucun hôte d'un fournisseur de modèles. Le risque des requêtes par auteur est écrit (§ 2.0, point 3). |
| 3 | B2, fait 2 | § 4.1, « Arbitre : un troisième modèle… » | **appliqué** | § 4.1 | Arbitre : sous-agent Claude d'un modèle distinct des deux juges et du rédacteur ; le « juge » des § 1.2, 3.4 et 7.3 est J1 ou J2. |
| 4 | B2, fait 3 | § 10, point 7 (exception du collisionneur) | **appliqué** | § 10, point 3 | Collisionneur retiré (R-2570 : « 3 non ») ; ligne 3 du devis et point 4 de la § 13 retirés. |
| 5 | B3, fait 1 | § 5.3, proximité `g = 0,25 + 1,5 c` | **appliqué sous une forme adaptée** | § 5.5 | Le modèle est refait plutôt que retouché : le taux d'une pièce est la base de volume, répartie entre équipes par des poids qui somment à 1 et relevée au plus du double par les annonces ; plus aucun plancher par équipe, plus d'unités incompatibles ; borne écrite : `h_vol ≤ h_mod ≤ 2 h_vol`. |
| 6 | B3, fait 2 | § 5.3, terme « équipe nouvelle » sur 26 semaines | **appliqué** | § 5.1, 5.2, 5.5 | S = semaines réellement collectées ; la part des équipes nouvelles se mesure sur les histoires d'auteurs de 365 jours, non sur le seul corpus d'un mois. Les fenêtres de prédiction sont bornées par S (13 semaines seulement si S ≥ 13) ; l'horizon H du rétro-test (1,33 fois S) est déclaré comme extrapolation. |
| 7 | B3, fait 3 | § 8.4, critère de niveau | **appliqué en partie ; une partie écartée** | § 8.4, C2 (a) et (b) | Appliqués : calibrage d'ensemble (entre la moitié et le double de la fréquence observée) et Brier inférieur à une base constante qui n'emploie pas l'issue. **Écarté** : l'ajustement d'un facteur d'échelle κ sur le rétro-test si le seul critère de niveau échoue. Raison : un réglage fait sur le test contredit la règle d'un seul passage (M6, exigence de la mère) ; un échec reste un échec. |
| 8 | M1 | § 2.3, exception de l'organisme | **appliqué** | § 1.4 ; § 8.3.2 | Rétro-test principal sans l'organisme ; résultat « à part » sur **toutes** les lignes O1 à O20 (l. 257 à 276) et le rôle 1, sans tri, par le même script. Dénominateurs : **19 pièces** (et non 21 : H9 née le 22 octobre sort ; H6 sort par la règle mécanique, un seul axe), **4 collisions**, **3 pièces de septembre** ; seuils écrits sur eux. |
| 9 | M2 | § 8.3, définition de la liste | **appliqué** | § 8.3 | Dates et sources écrites pour chaque article (fichier, ligne, empreinte, ou mois de l'identifiant) ; vérification datée une fois par `id_list`, scellée par un sous-agent neuf avant la collecte ; règles de strate écrites ; **H = du 1er octobre au 9 novembre** ; seuils en proportion ; seconde lecture de l'issue, une fois (§ 8.7). 2609.17560, absent de la synthèse, est retiré. |
| 10 | M3 | § 8.4, critère 2 | **appliqué** | § 8.4, C2 (c) ; « taux retenu » | Aire sous la courbe avec valeur de permutation par blocs < 0,10 ; base de volume rendue à côté avec intervalle ; le plus simple l'emporte pour les décisions s'il n'est pas battu. Renforcé par les critères de niveau (couple 7). |
| 11 | M4 | § 8.4, critère 3 | **appliqué** | § 8.4, C3 ; § 5.3 | « Au moins 2 sur 4 », strictement au-dessus de la base de volume des équipes et de l'espérance d'un tirage au hasard, sans le flux des citations ; équipes de plus de quinze auteurs scindées, tailles rendues. Ajout : la règle d'équipe exige deux auteurs **et** un Jaccard ≥ 1/3, pour éviter l'enchaînement de laboratoires. |
| 12 | M5, premier couple | § 3.1, fin | **appliqué** | § 3.4 | Échantillon aveugle de 300 écartés ; attribution des termes ; strate 3 mécanique tirée des bibliographies des collisions. La strate 3 entre dans C1 (b) avec la base « tri au hasard à volume égal ». |
| 13 | M5, second couple | § 8.4, critère 1 | **appliqué** | § 8.4, C1 (a) | « Présentes après le préfiltre et retenues à l'étage 1 », puis jugées. Avec la proportion de M2 (5 sur 7 → 3 sur 3), **les 3 pièces de septembre doivent être jugées au moins « occupe en partie »**. |
| 14 | M6, premier couple | § 8.5, « 1 échoue » | **appliqué en partie ; une partie remplacée** | § 8.5 ; § 7.4 | Appliqué : aucun second rétro-test ne vaut validation ; nœud à Lazar si C1 échoue. **Remplacé** : « veille rendue comme description, sans probabilité ni classement » devient « classement et probabilités rendus, dits non validés ; toutes les décisions fragiles, donc rendues tenir ». Raison : exigence de la mère (« le classement est dit non validé ») ; l'effet sur les décisions est le même (aucune décision chiffrée n'est appliquée). |
| 15 | M6, second couple | § 8.5, « Trop beau » | **appliqué** | § 8.6 | Audit symétrique sur cinq déclencheurs ; ajout d'un déclencheur de niveau (calibrage hors d'un facteur 4). |
| 16 | M7 | § 8.2, garde de date | **appliqué** | § 3.1 ; § 4.4 ; § 2.3 ; § 2.6 | Garde sur la première version de chaque article ; titre et résumé de la dernière version antérieure à t0 ; `comment` vidé ; NeurIPS hors du rétro-test ; retard d'indexation de Semantic Scholar dit ; juges hors du dépôt, sans outil de lecture ou audités ; fin de connaissance consignée ; sonde par titre, juges compris. |
| 17 | M8, dates | § 2.0, point 6 | **appliqué** | § 2.0, point 6 ; § 2.1 | Versions suivantes collectées en veille vivante par `lastUpdatedDate`. |
| 18 | M8, catégories | § 2.1 | **appliqué, étendu** | § 2.1 | Huit catégories complémentaires ; elles suivent **le même tri** que les principales (le couple disait métadonnées et préfiltre seulement : un article de statistique ou de finance qui passe le préfiltre doit pouvoir être lu, sinon le flux ne sert à rien) ; décompte à part. |
| 19 | M8, semences | § 2.10 | **appliqué** | § 2.10 | Pièces que la contre-lecture de la synthèse demande de lire, ajoutées ; occupants connus versés à l'étage 2 du corpus vivant, marqués. Rien au rétro-test. |
| 20 | M9 | § 2.3, limite déclarée | **appliqué** | § 2.3 ; § 8.4 | Seuils sans le flux des citations ; jeu de contrôle mécanique (25 identifiants cités au moins deux fois par les documents de lancement, comptés par `grep`) ; justifications des quinze ancrages refaites sur les seuls documents de lancement ; POPPER hors du rétro-test principal. |
| 21 | M10 | § 1.2, appariement | **appliqué ; une partie écartée pour le rétro-test** | § 1.2 ; annexes A et B | Appliqué : signatures en table, code discriminant (règle mécanique : première entrée dans l'ordre ME, TA, AC, GA, OS, CA), échantillon de 60, passage à `c ≥ 0,34` par addendum, phrase libre. « Au moins trois axes » tenu pour la veille vivante (annexe B). **Écarté pour le rétro-test** : exiger trois axes ôterait huit pièces, dont deux touchées (A-H8, B-POP) ; la mère demande de ne sortir que les pièces infaisables ; les pièces à deux axes restent, marquées « signature pauvre », passent par leur code discriminant, et le résultat sur les seules pièces à trois axes est rendu à part. |
| 22 | M11, abandon | § 7.1 | **appliqué, étendu** | § 7.1 | `W_p` propre, `ρ` au même risque de rival ; ajout de `ρ_v` : une capacité rendue ne vaut que si une autre pièce gardée peut l'employer sur la même voie (point (c) du constat). |
| 23 | M11, perturbations | § 7.5 | **appliqué, étendu** | § 7.5 | Perturbations étendues aux constantes du nouveau modèle (0,1 de la base, `ν_F`, poids, annonce) ; fragile → « tenir » ; moins de cinq jalons → toute décision autre que « tenir » fragile. Le point (e) (regret et utilité attendue) est écrit en § 7.2. |
| 24 | M12 | § 11.4, devis | **appliqué sous une forme adaptée** | § 11 | R-2570 : aucune dépense. Lignes payantes, vérification des prix et plafond global en USD : **sans objet**. Gardés : volumes comptant témoins, échantillons et second essai ; capacité des sous-agents chiffrée ; arrêts à 15 000 articles, 600 articles à l'étage 2, 3 000 couples (puis ordre de `c` décroissant si la mère poursuit). |
| 25 | M13 | § 2.0, point 5 | **appliqué** | § 2.0, point 5 | 403 ou vérification humaine : arrêt du flux ; refus de permission ou de classifieur : arrêt de la phase ; hôtes non vérifiés : un premier essai unique sur un mot de la mère. |

## 2. Parties des constats qui n'avaient pas de couple

| constat | sort | lieu dans la v2 |
|---|---|---|
| B1, conséquence : liste « touchées » contredisant les signatures | appliqué : les signatures d'origine ne cèdent que ce que le programme cédait lui-même | annexe A |
| M8 (d) voisins d'avant septembre | appliqué : occupants connus au corpus vivant | § 2.10 |
| M8 (e) sites des équipes | appliqué : réseau ouvert (R-2570) ; hôtes nommés, premier essai sur un mot de la mère ; limite écrite | § 2.0 ; § 2.9 |
| M11 (b) étapes communes | appliqué : `W_p` | § 7.1 |
| M11 (f) point censuré | appliqué : dit, et règle « moins de cinq jalons » | § 6 ; § 7.5 |
| M12 (a) jetons de raisonnement | sans objet (aucun appel facturé) | — |
| M12 (b) deux passes | appliqué : codages de septembre réemployés sauf articles révisés | § 11 |
| Note de la contre-lecture : OpenReview, ateliers de NeurIPS | appliqué : non observés, export possible de Lazar plus tard comme écart déclaré | § 2.5 ; § 2.6 |
| Exigence de la mère : un seul passage | appliqué | § 0.1, point 5 ; § 8.5 |
| Exigence de la mère : GitHub par `git ls-remote` et refspec explicite | appliqué, sans extraction ni exécution | § 2.7 |
| Exigence de la mère : pièces vivantes prises dans N-067 à N-070 retenues | appliqué (HC4 restreinte, « entraîné contre elle », profil de MasDrift cédé pour H9, statuts les plus durs) | § 1.3 ; annexe B |

## 3. Constats mineurs

| n° | sort | lieu |
|---|---|---|
| m1 | appliqué : hypothèse et prédictions chiffrées du rédacteur, avant toute requête (réussite d'ensemble attendue : environ 0,04) | § 8.0 |
| m2 | appliqué : fichiers ajoutés ; lignes du registre citées avec leurs premiers mots | § 0.4 |
| m3 | appliqué : table des graines par usage ; température non réglable, consignée ; un second passage ne remplace jamais le premier | § 12.2 ; § 4.1 |
| m4 | appliqué : nom de la contre-lecture tel que versé ; zip versionné des livrables | en-tête ; § 12.1 |
| m5 | appliqué : variante d'archivage ouvert limitée aux hôtes d'arXiv, date de modification dite, sinon « non disponible » | § 2.1 |
| m6 | appliqué : pagination jusqu'à `totalResults`, une seconde demande | § 2.1 |
| m7 | appliqué : `abstract` demandé dans les histoires d'auteurs | § 2.3 |
| m8 | appliqué : deux formes du nom du congrès ; zéro consigné | § 2.6 |
| m9 | appliqué : 3 secondes partout ; PDF sur `export.arxiv.org` | § 2.0 ; § 2.8 |
| m10 | appliqué : accord positif ; au plus 5 négatifs retenus sur 20 | § 4.5 |
| m11 | appliqué : marques de page gardées et testées | § 3.3 |
| m12 | appliqué : billets retirés du rétro-test | § 2.9 ; § 8.3.1 |
| m13 | **sans objet** : il n'y a plus de lecteur d'une autre famille, donc plus d'analogie avec N-053 à écrire | — |
| m14 | appliqué : voie « décision de Lazar », mesurée sur le registre | § 6 ; § 7.6 |

## 4. Écarts du rédacteur pendant cette version
- Aucun `ls` de `registres/` ; seuls `registres/decisions.md` et les fichiers nommés en § 0.4 de la v2 ont été ouverts.
- Le script de l'annexe A a été joué hors réseau, dans le bloc-notes de la session, puis copié au dépôt et rejoué à
  l'identique (sorties comparées octet par octet).
- Aucune requête réseau, aucune dépense, aucune écriture git.
