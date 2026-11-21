# Comparaison des deux réponses au protocole X « attaquant qui connaît le protocole » : Fable 5.2 (v2) et Opus 5.5 en effort maximal (v1)

- **Date** : 21 novembre 2026. **Auteur** : Claude Opus 5.5, comparateur neuf ; je n'ai écrit aucune des deux réponses. Pièce de classe C. Aucun commit, aucun appel payant.
- **Grille** : `grille-comparaison-attaquant-v1.md` (`611bbaaf0a0cdd9f5abf26d51d376cf14013ed7a52da5330aa2ed60bf8a576d5`), écrite et scellée avant toute lecture. Avant le scellement, je n'avais listé que les noms des fichiers.
- **Pièces lues, empreintes égales aux compagnons** :
  - la réponse du concepteur Fable, v2 : `../reponse-fable-protocole-x-attaquant-v2.md` (`3180e43b…`), en entier ;
  - sa contre-lecture : `../contre-lecture-reponse-fable-protocole-x-attaquant-v1-opus-v1.md`, dont j'ai lu l'en-tête, le verdict et les dix-sept constats ;
  - la vérification des corrections : `../verification-corrections-protocole-x-attaquant-v2-opus-v1.md`, en entier (verdict « conforme ») ;
  - la réponse d'Opus en effort maximal : `reponse-opus-max-attaquant-v1.md` (`4c77dbb5…`), en entier ;
  - les calculs d'Opus (`calculs-opus-max-attaquant-v1.py` et son `.txt`). Je les ai rejoués avec `python3 -I` depuis le bloc-notes de ma session. Seule diffère la ligne de version de numpy (2.4.6 chez moi, 2.5.3 dans la sortie scellée) ; **tous les nombres sont identiques**. Je n'ai pas rejoué les calculs de Fable v2 : le contre-lecteur les a rejoués à l'octet.
- **Cloisonnement** : je n'ai ouvert aucun chemin interdit par le mandat ni aucun résultat d'expérience.

## 1. Chiffres vérifiés à la page

Le texte vient de `pdftotext` ; le rang de page est celui du fichier ; les empreintes sont égales aux compagnons.

| Réponse | Chiffre ou citation | Source, page | Résultat |
|---|---|---|---|
| Fable | 0,46 (« careful on resample »), 0,17 (simulation par recréation, raisonnement caché et invite système retirés), 0,81 (auto-relecture), 0,69 à 0,78 (retour) | Kutasov et al., 2511.02997v1, p. 5, tableau 1 | **exact** |
| Fable | aire sous la courbe de 0,688 à 0,850 ; sûreté de 0,87 vers 0,4 ; « steady background rate » | Loughridge et al., 2511.02823v1 (`anteriorite-P-041-v2/c5/`), p. 4 | **exact** |
| Fable | « does not increase safety at all if the attacker is behaving optimally » ; ρ ≈ 0,19 chez l'honnête | Lucassen et Kaufman, 2605.26047v2, p. 2, et p. 7 et 8 | **exact** |
| Fable | +0,05 ; 7 évaluations sur 8 ; « property of the pool » | Jha, 2608.16190v1, p. 1 | **exact** |
| Fable et Opus | théorème 2.3 (surveillance possible si et seulement si la classe s'apprend en ligne), remarque 2.4 (requêtes tirées au hasard) | Rudoler et al., 2609.36049v1, p. 3 | **exact** |
| Opus | « In a zero-sum game which has a value, leadership has no effect » | Avenhaus, von Stengel et Zamir, p. 31 | **exact** |
| Opus | « inspections are used up […] the inspectee can and will safely violate » | même source, p. 33 | **exact** |
| Opus | 10 % de verdicts faux : le modèle garde 87 % de son ajustement | Lyons Keenan et al., 2609.36490v1, p. 7 | **exact** |
| Opus | de 100 % à 27 % ; rang 1 : 4 % sur des concepts tenus à l'écart | même source, p. 1 | chiffres exacts, **paraphrase imprécise** : « multiplier par huit l'ajustement d'un modèle du commerce » ; la source multiplie par 8 les **modifications d'activation** du modèle (« scaling up these edits by a factor of 8 »), sans aucun affinage |
| Opus | évasion de 0,59 à 0,82 pour les sondes moyennées ; un cas à 1,0 | Gupta et Jenner, 2506.14261v4, p. 7, table 1 | **exact** (0,75 ; 0,82 ; 0,594) |
| Opus | baisse de 88 % sur la sonde « finnois » | McGuinness et al., 2512.11949v1, p. 7 | **exact** |
| Opus | plafond vers 50 % ; « over 70 epochs » | Bailey et al., 2412.09565v2, p. 12, et p. 3 et 11 | **exact** |
| Opus | « Thompson-Horvitz » ; « regardless of the true crime rate » | Ensign et al., 1706.09847v3, p. 7 et p. 1 | **exact** |
| Opus | contre un apprenant « à la moyenne », plus que la valeur de Stackelberg | Deng, Schneider et Sivan, 1909.13861v2, p. 1 | **exact** |

Aucun chiffre faux de part et d'autre. Il y a une seule imprécision, chez Opus, sur Lyons Keenan et al. Elle compte, parce qu'elle fait passer pour un affinage une manipulation faite par les expérimentateurs. Fable écrit juste ce même point à la p. 1 (correction hors constat de sa v2).

## 2. Notes par critère (0 à 5)

| Critère | Fable v2 | Opus max v1 | Justification |
|---|---|---|---|
| 1. Justesse des chiffres à la page | 5 | 4 | Fable : tout est exact ; le texte a été contre-lu, corrigé et vérifié. Opus : tout est exact sauf la paraphrase ci-dessus. Plusieurs pas porteurs restent **de mémoire** : la borne du perceptron (Novikoff) et la dimension de Littlestone infinie des seuils, dont dépend son « si et seulement si ». |
| 2. Profondeur | 5 | 4 | Fable : quatre sens de la convergence, chacun avec sa condition, sa borne et ce qui la casse ; décomposition de la chute publiée par canal ; table des horizons corrigée. Opus : la preuve en trois pas de la borne de la boucle est nette, et les trois asymétries sont traitées avec soin. Mais les questions 5 et 6 du protocole sont à peine touchées. |
| 3. Originalité des solutions | 4 | 4 | Fable : le résidu de la sonde sous sélection d'attaque ; la recapture lue des deux côtés ; les deux horloges ; le prix d'entrée d'un adjudant d* ; la paire ordre et prix de la coupe. Opus : la table des secrets ; l'invariant d'indépendance à la place de « aucun retour » ; les trois conditions du réapprentissage (inverse de la probabilité d'audit, poids du dommage, stationnarité) ; la contrainte débit × délai ; la règle de l'archive rouge contre bleu ; la courbe de prix de l'évasion. Chacune dit ce qu'elle reprend. |
| 4. Honnêteté des limites et de R8 | 5 | 4 | Fable : 15 requêtes d'antériorité ; « non trouvé » posé en question ; ses chances chiffrées ; la liste de ce par quoi la note serait bien jugée sans le mériter. Opus : aucune recherche d'antériorité, ce qu'il dit ; son indépendance partielle est déclarée ; une liste « Ne pas écrire » utile. Mais il écrit « si et seulement si une marge », ce qui est trop fort (contradiction 1). |
| 5. Respect des règles et des nœuds | 4 | 5 | Fable : les défauts sont restreints comme il faut (D-4) et chaque hypothèse est un nœud. Mais D-1 a été écrite avant le retrait de la marge asymétrique (N-077) : sa partie « H6 devient ligne de base » est dépassée. Opus : tout est aligné sur N-077 (descriptif sur nos organismes), N-075, N-062, N-050 et le point 4 de N-060 v3 (la boucle reste sur mondes plantés) ; les nœuds n'ont pas de défaut. |
| 6. Actionnabilité | 4 | 4 | Fable : six décisions au format ; couple neutre v2 prêt pour le collisionneur ; trois mesures défensives d'abord. Opus : six décisions ; cinq premiers pas sur processeur ; il n'écrit pas de question neutre, ce qui est le rôle du concepteur. |
| 7. Coût | 3 | 5 | Fable : quota de Fable consommé (v1, v2) en plus d'une contre-lecture et d'une vérification. La mesure de ρ peut demander des épisodes honnêtes « sur devis ». Opus : tout sur processeur et sur mondes plantés ; zéro dépense ; le script se rejoue. |
| 8. Ce qui manque | 3 | 3 | Fable : les copies à point focal commun, le délai multiplié par le débit, la pondération du réapprentissage, la fuite par quota et la règle de la boucle rouge contre bleu manquent. Ces sujets sont peut-être traités dans la note séparée sur les asymétries, que je n'ai pas lue. Opus : la décomposition de Kutasov et al. manque, alors que c'est la source même du « de 89 % à 17 % » ; manquent aussi la sélection d'attaque (Loughridge et al. ; Lucassen et Kaufman), la question 6 sur la diversité (une seule ligne), le résidu, l'horizon d'expiration, la recapture et le prix d'entrée d'un adjudant. |

Les totaux sont égaux (33 contre 33) ; aucun total ne décide (règle de la grille). **Fable l'emporte** sur la justesse, la profondeur, l'honnêteté et la couverture des six questions. **Opus l'emporte** sur le coût, sur l'alignement avec les décisions les plus récentes et sur les trois asymétries : retour, copies, généralisation de l'évasion.

## 3. Ce que chacune a que l'autre n'a pas

**Seule Fable** :
- la décomposition de la chute publiée (0,46 ; 0,17 ; 0,81 ; Kutasov et al., p. 5) et la borne « à l'aveugle plus fuite » ;
- le résidu de la sonde (A4) ;
- la règle à parts égales, avec sa perte d'au plus un facteur deux ;
- la recapture des deux côtés, avec le cas « mode de dommage par nature moins signalé » ;
- le tirage de ce que l'oracle vérifie ;
- la table des horizons d'expiration en régime d'excès, corrigée de six cases triviales ;
- les deux horloges : ne jamais remettre à zéro celle du dommage ;
- le prix d'entrée d'un adjudant d* ;
- la paire ordre et prix de la coupe pour la diversité effective (H5), et les citations obligatoires (Molnar, Mell et al., Koran et al., Jha) ;
- le couple neutre pour le collisionneur et l'énoncé pour Neon et Carbon.

**Seul Opus** :
- la table des secrets (principe de Kerckhoffs ; Avenhaus et al., p. 31) ;
- la fuite par quota (Avenhaus et al., p. 33 ; bloc F : 9 % du lot sans audit) ;
- le bruit partiel qui ne ferme pas le canal de retour (87 % à 10 % d'erreurs, Lyons Keenan et al., p. 7) ;
- l'invariant d'indépendance, qui permet des corrections dépendant de la seule pièce du plancher ;
- les copies à point focal commun et la contrainte débit × délai (4 800 épisodes pour 100 copies sur 24 heures) ;
- les trois conditions du réapprentissage contre la boucle qui s'emballe (Ensign et al. ; bloc B) ;
- la règle de la boucle rouge contre bleu : archive contre archive, valeur contre une meilleure réponse fraîche ; le dernier coup cycle et la moyenne converge (bloc H) ;
- le gonflement par relecture d'une même famille tenue à l'écart (bloc G, qui appuie N-062) ;
- l'exemple publié d'une évasion payée en dommage (Gupta et Jenner, table 1).

## 4. Contradictions, tranchées à la source

1. **La boucle converge-t-elle pour une sonde lue sur des états que l'attaquant place ?**
   - Fable : « jamais » (table de la question 3, ligne a). Un lecteur à seuil réel subit une erreur par tour ; 1 024 seuils possibles en donnent au plus 10 (C2).
   - Opus : oui, si une marge γ non refermable existe, avec au plus (R/γ)²/(p·q) manques, « si et seulement si » une marge.
   - **À la source** : Rudoler et al., p. 3, théorème 2.3. La surveillance est possible si et seulement si la classe a une dimension de Littlestone finie. Les deux ont donc tort par excès.
   - Le « jamais » de Fable est faux : une classe à marge a une borne d'erreurs (perceptron, de mémoire), même contre un attaquant qui voit la sonde.
   - Le « seulement si une marge » d'Opus est faux : le calcul C2 de Fable montre une classe finie sans marge qui converge.
   - Énoncé juste : la boucle a un total de manques borné si et seulement si la classe de la sonde a une dimension de Littlestone finie, sur ce que l'attaquant peut placer. Une marge non refermable est une façon de l'obtenir ; q et le délai entrent dans la borne.
   - Les deux hypothèses reposent sur la même supposition non mesurée : le pas 8 de Fable, le pas 16 d'Opus.
2. **« La boucle ne converge que si l'agent ne voit pas le moniteur en service » (Fable) contre « la borne tient même s'il voit la sonde » (Opus).** Ce n'est pas une contradiction : les deux ne parlent pas du même sens de la convergence.
   - Fable parle de la stabilité du moniteur réappris (Perdomo et al., p. 8 et 9).
   - Opus parle du total des manques.
   - Les deux s'accordent sur ce point : le dernier coup ne se stabilise pas (Mertikopoulos et al., p. 1).
   - On peut donc écrire les deux : le moniteur peut osciller pendant que ses manques restent bornés.
3. **Le canal de retour.** Fable conditionne H10 à « aucun verdict ni aucune correction ne revient ». Opus montre que le plancher et la borne de la boucle survivent au retour des pièces passées, tant que la pièce est tirée après l'acte et sans quota. Les deux sont compatibles. L'invariant d'Opus est plus fin : ce qui doit rester fermé est ce qui dépend d'une lecture ou d'une trouvaille, non toute correction. Il peut remplacer la condition de H10 sans rien lui retirer, puisque le résidu n'a besoin que du secret de la lecture.
4. **Lyons Keenan et al., p. 1.** Fable a raison. Le facteur 8 porte sur des modifications d'activation, sans affinage. L'affinage de rang 1 donne 4 %, et l'évasion survit au réapprentissage des moniteurs.

## 5. Synthèse recommandée pour Lazar

**Ce qu'il faut retenir.**
- Contre l'attaquant qui connaît le protocole, ce qui tient est un **engagement sur des tirages secrets, faits après l'acte, par épisode, sans quota**. Seuils, quotas et sondes ne sont que des gains mesurés. Les deux réponses s'accordent sur ce point.
- La chute publiée se lit **par canal** : fuite du tirage (0,46), simulation du moniteur (0,17), retour (0,69 à 0,78). C'est Fable qui la donne, et c'est elle qu'il faut citer.
- La convergence de la boucle s'énonce comme au point 1 ci-dessus, **avec délai et débit déclarés** (Opus) et **horloge du dommage jamais remise à zéro, horizon dit** (Fable).

**Décisions qui changent.**
- **L'hypothèse neuve** (D-1 des deux). Ne pas choisir entre H10 et « la marge de lecture que l'évasion ne referme pas » : ce sont deux mesures de la même supposition.
  - Recommandation : une seule hypothèse candidate, non revendiquée, nœud sans défaut.
  - Deux mesures, d'abord sur mondes plantés : le rappel du résidu sous sélection d'attaque (Fable) et la courbe de prix de l'évasion (Opus).
  - La condition de retour serait celle de l'invariant d'indépendance d'Opus.
  - Elle resterait descriptive sur nos organismes (N-077).
  - La partie « H6 devient ligne de base » de la D-1 de Fable est déjà réglée par N-077.
- **Le texte de l'audit** (D-2 de Fable, D-3 d'Opus) : réunir en un seul texte la règle à parts égales, la recapture des deux côtés, le tirage des contrôles de l'oracle, « jamais de quota » et le débit et le délai déclarés. Défaut « écriture seule » acceptable.
- **La garantie d'excès** (D-3 de Fable) : la garder, en corrigeant la phrase sur la convergence par l'énoncé juste du point 1 de la section 4.
- **Le réapprentissage sur verdicts de l'oracle** (D-5 d'Opus) : joindre ses trois conditions à la coupe proposée pour la boucle. C'est le même nœud que le point 4 de N-060 v3.
- **Neuf** : la règle de la boucle rouge contre bleu (D-4 d'Opus), à écrire au montage du bras d'attaque.
- **H5** (D-5 de Fable) : inchangée. D'ici sa décision, appliquer la règle commune aux deux réponses : les lectures internes comptent pour un seul regard tant que la matrice de transfert, mesurée dans les deux sens, ne dit pas mieux.
- **Avant toute inscription** :
  - contre-lire la réponse d'Opus, en particulier sa section 5.3, en mode « garantie qui suppose ce qu'elle prouve » ;
  - corriger sa paraphrase de Lyons Keenan et al. par un erratum ;
  - faire une recherche d'antériorité sur la courbe de prix de l'évasion ;
  - ajouter au couple neutre du collisionneur, après une relecture de neutralité, quatre faits établis par Opus : Avenhaus et al., p. 31 et 33 ; Ensign et al., p. 7 ; Lyons Keenan et al., p. 7.
