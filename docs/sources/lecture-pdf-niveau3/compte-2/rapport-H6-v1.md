# Rapport du lecteur — H6, « marge asymétrique », contre Ctrl-Z et 2605.26047 — v1

- **Date et heures** : début de session 2026-11-13 22:51:46 UTC ; rapport fermé le 2026-11-13 23:01:27 UTC (heures relevées par `date -u`).
- **Rôle et modèle** : lecteur, modèle A. Compte 2, mandat H6 (constat M5 de la contre-lecture du niveau 3).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` ; `interdits-communs-v2.md` lu et tenu (le plus strict : aucune commande git).
- **Empreintes des PDF** (vérifiées contre leurs compagnons `.sha256`, `sha256sum -c` : OK et OK) :
  - `2504.10374v1.pdf` : `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` (38 pages) ;
  - `2605.26047v2.pdf` : `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` (46 pages).
- **Fichiers lus, et seulement eux** : la consigne commune (en entier) ; `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (en entier, sur renvoi de la consigne) ; `docs/programme-controle-ia-v2.md` l. 85-125 et 185-200 ; `docs/decisions/decision-N-013-v1.md` l. 76-81 ; `docs/decisions/decision-N-015-v1.md` en entier ; `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` l. 152-165 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` l. 172-182 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` l. 408-441 ; les deux PDF et leurs compagnons `.sha256`. Aucune ouverture fautive, aucun refus.
- **Étendue lue** :
  - 2504.10374v1 : les 38 pages lues ligne à ligne (texte brut de `pdftotext`) ; pages 15 à 17 (gabarits et code de tests) lues, code parcouru ; figures des pages 4, 5 et 6 vues sur le PDF ; autres figures (p. 13, 14, 28 à 30, 35 à 37) : légendes lues seulement. Recherche par mots sur les 38 pages (aléatoire, uniforme, « chaque pas », « chaque action », toujours, ablation, base, paraphrase, remise à zéro, température…).
  - 2605.26047v2 : pages 1 à 28 lues ligne à ligne ; pages 29 à 46 (annexe I, exemples de rééchantillons : code) parcourues par mots, commentaires des auteurs lus ; figures des pages 2, 7, 9, 10 vues sur le PDF ; autres figures : légendes lues seulement.
- **Citations** : 69 contrôlées par programme (`verifier_citations_H6_v1.py`, `python3 -I`, texte brut et `-layout`, trois niveaux de normalisation), **0 échec** ; script testé d'abord sur un cas juste (passe) et trois cas altérés (trois échecs). Fichier : `citations-H6-v1.json` (champ `n` = numéro cité ci-dessous entre crochets).
- **Noms de modèles** : la ligne 14 de la consigne est lue au sens strict ; aucun nom de modèle, y compris ceux des articles, n'est écrit ici.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi).

---

## 0. Verdict d'ensemble

**H6 : « occupé en partie ».**

- **2605.26047v2 occupe en partie H6 pour le rééchantillonnage**, en sabotage concentré. Il publie un rééchantillonnage systématique, non déclenché par le moniteur, à intensité fixe sur une échelle (k = 1 à 5 échantillons à chaque pas). À k = 5, la sécurité monte de 10,2 points, intervalle de confiance apparié à 95 % [+6,1 ; +14,3] (auteurs, [40]), soit une part d'attaques réussies qui passe de 39 % à 29 % (calcul, à partir de 61 % et 71 %, [33]). Le coût en utilité est « exactement zéro », par construction [50].
- **Ce qui n'est pas occupé, et pourquoi** :
  - Dans ce bras, l'action exécutée est toujours le premier échantillon [49]. La chute du succès d'attaque passe donc tout entière par le moniteur et l'audit, jamais par un affaiblissement de l'attaque elle-même.
  - L'utilité ne peut pas baisser, par définition. La « marge » est vraie par construction : elle n'est pas mesurée.
  - Aucune comparaison de pentes, aucun test de la marge.
  - Le cadre est concentré (« live failures » [42]), pas diffus.
- **Ctrl-Z (2504.10374v1) ne fait que voisiner.** La marge publiée (58 % à 7 % pour 5 % d'utilité [4]) vient d'un rééchantillonnage déclenché par le moniteur et combiné à d'autres mesures. Je n'ai trouvé aucun bras, aucune ablation ni aucune base de rééchantillonnage systématique ou à taux fixe, annexes comprises.
- **Paraphrase et remise à zéro du contexte, sur l'agent** : non trouvées dans les deux pièces.
- **Contradiction (constat M5)** : confirmée, explicite (« contradict earlier work » [35]), sur deux points annoncés et un troisième en corps de texte : l'agrégation (max contre min), la valeur de l'exécution de l'échantillon le moins suspect, et l'audit après plusieurs « coups ». Aucun de ces points ne porte sur une intervention non spécifique. 2605.26047 attribue l'écart au cadre et retrouve le même mécanisme, plus faible [57], [58]. Détail en section 4.

## 1. Énoncé confronté (tel que fixé par N-015)

« Pour l'une au moins des trois interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte), il existe une intensité où, **en moyenne à intensité fixe**, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête » (N-015, section 1). Le bruit d'activations est mesuré mais non revendiqué (N-015) ; le bruit sur les poids non plus (N-013).

Composantes confrontées, selon le mandat :
- (a) intervention **non spécifique** : non déclenchée par le moniteur ni ciblée sur les actions suspectes ;
- (b) à **intensité fixe**, sur une échelle d'intensité ;
- (c) **marge asymétrique** : chute du succès d'attaque significativement plus rapide que celle de l'utilité honnête (forme, mesure, test) ;
- (d) en **sabotage diffus**.

Deux lectures de « succès du sabotage » sont possibles, et les pièces les séparent ; je les tiens séparées partout :
- **lecture large** : le succès est la victoire de l'attaquant, audit compris ;
- **lecture stricte** : l'intervention affaiblit l'attaque elle-même, hors de toute détection par un moniteur.

## 2. Ctrl-Z — 2504.10374v1 (Bhatt, Rushing, Kaufman, Tracy, Georgiev, Matolcsi, Khan, Shlegeris)

**Venue imprimée** : prépublication arXiv, v1, 14 avril 2025 [1] ; aucune conférence ni revue imprimée sur le PDF.

### 2.1 Ce qu'il fait
- **Cadre** : BashBench, 257 tâches d'administration système en plusieurs pas, 100 d'entraînement et 157 de test (p. 1-2). Épisode simulé de 100 000 tâches par échantillonnage préférentiel (annexe C, p. 18-19).
- **Modèles** : un petit modèle commercial joue le modèle non fiable ; un modèle ouvert de 8 milliards de paramètres joue le modèle de confiance (p. 3).
- **Attaque** : télécharger et exécuter un logiciel malveillant factice, une seule cible connue [7], [28]. Elle part de gabarits écrits par des humains (p. 3, 9-10) ; la meilleure attaque compte dix pas (p. 5).
- **Métriques** :
  - utilité : part des tâches résolues, normalisée entre le modèle de confiance (0 %) et le modèle non fiable honnête (100 %) [6] ;
  - sécurité : probabilité que l'équipe bleue finisse l'épisode sans que le logiciel malveillant s'exécute [7] ;
  - budget d'audit de 1 % (p. 3).
- **Protocoles et résultats** (auteurs) :
  - audit initial de toutes les actions jusqu'à épuisement du budget [9] : 5,5 % de sécurité à 100 % d'utilité [10] ;
  - surveillance de confiance : 41,8 % [11] ;
  - report vers le modèle de confiance : 72,7 % à 95 % d'utilité [14] ;
  - report vers un rééchantillon : 83,2 % ; avec incrimination au présent : 84,0 % ; audit après trois coups : 84,9 % ; « voyage dans le temps » : 87,1 % [22] (tableau 1, p. 8, auteurs) ;
  - avec surveillance non fiable : 77,6 %, 91,1 % et 92,6 % (tableau 2, p. 9, auteurs [24]).
- **Chiffre du résumé** : « reducing the success rate of attacks from 58% to 7% at a 5% cost to the performance of a non-malicious agent » [4].
  - 58 % = 1 − 41,8 % (surveillance de confiance, 100 % d'utilité) ; 7 % ≈ 1 − 92,6 % = 7,4 % (voyage dans le temps avec surveillance non fiable, 95 % d'utilité) (calcul, rapprochement non dit par les auteurs).
  - Sans la surveillance non fiable, le meilleur protocole donne 1 − 87,1 % = 12,9 % (calcul).
  - Le 7 % du résumé inclut donc la surveillance non fiable et sa paraphrase de confiance, pas le seul rééchantillonnage.
- **Échelle d'intensité** : seuils de report de 50 % à 99 % [68]. L'utilité baisse avec le seuil (figure 3, p. 5 : droites ajustées imprimées sur la figure, « y = 0.33x + 0.71 » pour le rééchantillonnage, « y = 0.74x + 0.31 » pour le modèle de confiance, lu sur le PDF, non contrôlé par programme). Le seuil est un quantile des scores du moniteur sur l'agent honnête [12].

### 2.2 Ce qui est déclenché par le moniteur, et ce qui ne l'est pas (demande du mandat)
- **Déclenché par le moniteur** :
  - tout rééchantillonnage : report vers un rééchantillon, « If a suspiciousness score is above a deferral threshold, we generate up to two new samples from » [15] ;
  - le choix de l'action exécutée (« the protocol executes the least suspicious one » [16]) ;
  - le rééchantillonnage d'enquête au présent (p. 7) ;
  - le « voyage dans le temps », qui rééchantillonne une étape passée quand le score dépasse un seuil d'enquête [30], annexe J, p. 33-34 [29] ;
  - le report vers le modèle de confiance et l'édition de confiance (annexe H, p. 29-31 [31]).
- **Non déclenché par le moniteur, mais hors de la forme de H6** :
  - l'**audit initial** [9] : intervention d'audit, non ciblée, sans aucun effet sur les actions ;
  - la **paraphrase de confiance**, appliquée à toutes les commandes avant de les montrer au moniteur non fiable [25]. Elle est non ciblée et systématique, mais elle porte sur l'entrée du moniteur, pas sur l'agent : « The blue team still runs the original commands, so trusted paraphrasing does not affect usefulness » [26]. Son effet n'est pas isolé (aucune ablation chiffrée) ; elle sert contre la collusion ;
  - la **remise à zéro de l'état** entre tâches [5] : règle de l'environnement, pas une intervention étudiée.
- **Point non tranché** : la figure 4 (droite) montre la distribution du minimum des scores sous « a resampling procedure with up to six resamples per action » [17]. La légende ne dit pas si ce tirage est déclenché. Ce n'est de toute façon qu'une mesure de distributions de scores, ni de succès d'attaque ni d'utilité.
- **Recherche active du bras non ciblé** : aucun bras, aucune ablation, aucune base de rééchantillonnage systématique (à chaque pas ou à taux fixe), ni dans le corps ni dans les annexes A à L (recherche par mots sur les 38 pages : rien).

### 2.3 Ce qu'il ne fait pas ; limites reconnues ; incohérences ; trop beau
- **Ne fait pas** :
  - aucune intervention non spécifique sur l'agent ;
  - aucun intervalle de confiance ni test sur les sécurités ;
  - aucune comparaison de pentes entre succès d'attaque et utilité ;
  - aucun sabotage diffus.
- **Limites reconnues** : cible d'attaque étroite et connue [28] ; trajectoires plafonnées à 15 pas ; audit supposé infaillible (p. 10) ; résultats absolus sensibles au budget d'audit [27].
- **Incohérence interne** : le score d'une étape rééchantillonnée est « the minimum » en note 8 [66] mais « the mean » dans l'annexe J [67], pour le même protocole d'audit après trois coups. Le texte dit aussi que l'audit après trois coups « doesn't improve the blue team's safety » (p. 8), alors que le tableau 1 le place au-dessus de l'incrimination au présent (84,9 contre 84,0, auteurs).
- **Trop beau (règle R4)** :
  - un audit supposé parfait, fondé sur une classification parfaite observée « in our testing » (p. 3 ; hypothèse posée [8]) ;
  - un chiffre de résumé qui combine plusieurs mécanismes, sans intervalle.

### 2.4 Verdict par composante (Ctrl-Z)

| composante | verdict | page, citation |
|---|---|---|
| (a) non spécifique | **ne touche pas** pour le rééchantillonnage (tout est déclenché par un seuil du moniteur) ; **voisin** pour la paraphrase (systématique, mais sur l'entrée du moniteur, sans mesure isolée) | p. 6 [15] ; p. 33 [29] ; p. 9 [25], [26] |
| (b) intensité fixe, échelle | **voisin** : échelle de seuils de report, 50 % à 99 %, mais c'est l'échelle d'une intervention ciblée | p. 29 [68] ; p. 5 [12], [13] |
| (c) marge asymétrique | **voisin** : forme publiée pour une intervention ciblée et combinée (58 % à 7 % pour 5 % d'utilité) ; ni intervalle, ni test, ni pente | p. 1 [4] ; p. 8 [21], [22] ; p. 9 [24] |
| (d) sabotage diffus | **ne touche pas** : téléchargement unique d'un logiciel malveillant ; attaque fragmentée en plusieurs pas mais concentrée en un dommage | p. 3 [7] ; p. 10 [28] |

**Verdict Ctrl-Z contre H6 : voisin.**

## 3. 2605.26047v2 — « Retrying vs Resampling in AI Control » (Lucassen, Kaufman ; Redwood Research)

**Venue imprimée** : prépublication arXiv, v2, 26 mai 2026 [32] ; aucune conférence ni revue imprimée.

### 3.1 Ce qu'il fait
- **Cadre** : BashArena 1.1. Quatre tâches secondaires : désactiver le pare-feu, télécharger un logiciel malveillant, exfiltrer un secret, modifier les droits d'administration [43]. Elles sont modélisées comme des défaillances en direct, « immediately and irrecoverably bad » [42].
- **Audit** : par pas, budget 0,3 % (p. 3).
- **Modèles** : un modèle de frontière joue le modèle non fiable ; un modèle ouvert plus faible joue le moniteur de confiance (trois tirages, maximum) (p. 3-4).
- **Métriques** :
  - sécurité normalisée en excluant les issues sans vainqueur (formule p. 3, lue sur le PDF, non contrôlée par programme : P(audit) / P(audit ou succès)) ;
  - utilité : score moyen sur les tâches principales (p. 3) ;
  - intervalles par bootstrap hiérarchique et apparié (p. 3).
- **Base** : surveillance de confiance, 61 %, intervalle [57 ; 64] [44].
- **Nouvel essai** : déclenché par le moniteur (score supérieur à 30, environ 2,6 % des pas honnêtes [45]).
  - Avec retour, l'attaquant exploite la justification du moniteur : 60 %, différence −2,6 points [−11,2 ; +6,0] (p. 5, auteurs ; [46]).
- **Consigne « prudente » appliquée toujours, à chaque pas** (non spécifique, mais hors de la liste de H6) : sécurité 64,7 % contre 60,7 %, +4,0 points [+0,8 ; +8,9], pour un coût d'utilité de −5,3 points [−6,8 ; −3,7] [47], [48].
- **Rééchantillonnage « pour information »** :
  - il exécute toujours le premier échantillon, ou audite [49] ; les autres ne sont jamais exécutés, d'où un effet « exactly zero » sur l'utilité [50] ;
  - bras « Fixed resampling: always draw k samples » [51] ;
  - échelle N = 1 à 5 (figure 3a, p. 7 : avec l'agrégation max, environ 61, 68, 70, 71, 71 %, figure) ;
  - à N = 5 : +10,2 points [+6,1 ; +14,3] [40], 61 % à 71 % [33], « at no cost to usefulness » [33] ;
  - les variantes sélectives, déclenchées par le score du premier tirage, récupèrent 6,2 points pour 10 % des tirages en plus [34] ;
  - l'agrégation par le minimum fait baisser la sécurité avec N (figure 3a : environ 48 % à N = 2, 31 % à N = 5, figure).
- **Exécution de l'échantillon le moins suspect** :
  - N = 2 tirages **à chaque pas** (tirage non déclenché), mais l'action exécutée est **choisie par le moniteur** [54] ;
  - sécurité 72 % contre 68 % (rééchantillonnage pour information à N = 2), +3,9 points [−2,1 ; +10,9] [55] ;
  - sur les pas mixtes, la part d'échantillons d'attaque exécutés passe de 54 % à 32 % [56] ;
  - échantillons d'attaque tirés par trajectoire : 6,7 contre 7,4 (p. 10, auteurs) ;
  - utilité : −1,0 point [−2,8 ; +0,9] sur 298 tâches appariées [59] ; 0,0 [−10 ; +10] sur un second jeu (p. 11).

### 3.2 Ce que donne l'exécution de l'échantillon le moins suspect (demande du mandat)
- **Sécurité** : un gain faible et non significatif sur le rééchantillonnage pour information, « +3.9 pp, with the confidence interval overlapping zero » [37], [55]. Les auteurs ajoutent qu'il serait nul contre un attaquant optimalement constant [41], [57].
- **Utilité** : aucun coût significatif [59].
- **Mécanisme** : seul endroit des deux pièces où le succès de l'attaque elle-même baisse sans passer par l'audit (54 % à 32 % [56]). L'action exécutée y est choisie par le moniteur : l'intervention est donc ciblée au sens de la composante (a).

### 3.3 Bras d'intervention non ciblée et courbe utilité contre sécurité (demande du mandat)
- **Rééchantillonnage à k fixe, à chaque pas** [51] :
  - le tirage n'est pas déclenché par le moniteur ;
  - courbe sécurité contre nombre d'échantillons (figure 3a, p. 7) et sécurité contre coût (figure 6a, p. 9 : points noirs de k = 1 à 5, environ 61 %, 66 %, 70 %, 71 %, 71 %, figure) ;
  - utilité constante par construction [50] : la « courbe utilité contre sécurité » est une droite horizontale, non mesurée.
- **Consigne prudente toujours appliquée** [47], [48] : un seul point d'intensité, +4,0 points de sécurité pour −5,3 points d'utilité. Pas de marge asymétrique : c'est un contre-indice pour une intervention non spécifique, hors de la liste de H6. Le gain vient d'une baisse des scores honnêtes (p. 6), pas d'une chute de l'attaque. Les unités diffèrent, et les auteurs ne comparent pas de pentes.
- **Aucun autre bras non ciblé** :
  - ni paraphrase des actions ni remise à zéro du contexte ;
  - aucun rééchantillonnage dont l'action exécutée serait tirée au hasard parmi les échantillons. Le bras « IID » exécute le premier échantillon, soit environ 50 % d'exécution d'attaque sur les pas mixtes (54 %, [56]).

### 3.4 Ce qu'il ne fait pas ; limites reconnues ; incohérences ; trop beau
- **Ne fait pas** :
  - aucune intervention non spécifique qui modifie l'action exécutée sans s'appuyer sur un score de moniteur ;
  - aucune comparaison de pentes, aucun test de marge ;
  - aucun sabotage diffus ;
  - la sélection d'attaque n'est étudiée qu'en annexe G, et seulement contre le nouvel essai prudent.
- **Limites reconnues** :
  - les extrêmes (max, min) sont de mauvais choix pour de très nombreux tirages (p. 7) ;
  - l'auditeur simulé ne repère que 91 % des trajectoires d'attaque auditées sans faux positif, d'où une sécurité surestimée d'environ 10 % (p. 15, auteurs) ;
  - intervalles larges sur le second jeu d'utilité (p. 11, note 6).
- **Incohérences** :
  - référence de Ctrl-Z donnée comme « arXiv:2504.00000 » [61] (au lieu de 2504.10374) ;
  - base de surveillance de confiance donnée à 61 % [57 ; 64] [44], à 60,7 % [55,4 ; 64,6] [47] et à 60,9 % (p. 15) ;
  - la consigne de l'attaquant annonce que les actions suspectes seront remplacées par le modèle de confiance [64], ce qu'aucun protocole de rééchantillonnage étudié ne fait. L'attaquant est donc instruit d'un protocole autre que celui qu'il affronte.
  - à k = 2 avec l'agrégation max, la figure 6a (p. 9) place le point fixe vers 66 % et la figure 3a (p. 7) vers 68 % (figure ; écart possible dû à la règle de départage des ex aequo, non dit par les auteurs).
- **Trop beau (règle R4)** : « exactly zero effect on usefulness » [50] est vrai par construction, pas un résultat. La marge du bras « pour information » est donc asymétrique par définition.

### 3.5 Verdict par composante (2605.26047)

| composante | verdict | page, citation |
|---|---|---|
| (a) non spécifique | **occupée en partie** : rééchantillonnage systématique, k fixe à chaque pas, tirage non déclenché ; mais l'action exécutée est le premier tirage (aucun effet sur l'agent) et le gain passe par le moniteur ; l'exécution du moins suspect est choisie par le moniteur (ciblée) ; la consigne prudente toujours appliquée est non spécifique mais hors liste | p. 8 [51] ; p. 1 [33] ; p. 6 [49], [50] ; p. 10 [54] ; p. 6 [47] |
| (b) intensité fixe, échelle | **occupée** pour le rééchantillonnage pris comme amplificateur d'audit : N = 1 à 5, k fixe | p. 8 [51] ; p. 7 (figure 3a) ; p. 9 [52] |
| (c) marge asymétrique | **occupée en partie**, forme dégénérée : en lecture large, la part d'attaques réussies baisse (39 % à 29 %, calcul ; +10,2 points [+6,1 ; +14,3]) sans coût d'utilité, mais par construction et par l'audit ; ni pente ni test de marge ; en lecture stricte, seul l'exécution du moins suspect (ciblée) donne un effet, faible et non significatif sur la sécurité | p. 2 [40] ; p. 6 [50] ; p. 10 [55], [56] ; p. 11 [59] |
| (d) sabotage diffus | **ne touche pas** : défaillances en direct, quatre dommages concentrés | p. 3 [42], [43] |

**Verdict 2605.26047 contre H6 : occupé en partie** (rééchantillonnage, sabotage concentré, lecture large).

## 4. Les deux pièces se contredisent-elles ? (constat M5)

**Oui, explicitement, sur trois points ; aucun ne porte sur l'objet de H6.**

1. **Agrégation des scores de rééchantillons pour l'audit.**
   - Ctrl-Z audite sur le minimum [65], [66] ; 2605.26047 trouve le maximum meilleur, « the opposite of what Ctrl-Z found » [36].
   - Avec le minimum, la sécurité de 2605.26047 baisse quand N augmente (figure 3a, figure).
   - Explication des auteurs : la corrélation entre tirages des scores honnêtes, ρ ≈ 0,19, est assez haute pour favoriser le maximum (p. 7, auteurs) ; l'argument de Ctrl-Z « rests on honest scores being weakly correlated » [58].
   - Nuance : Ctrl-Z lui-même dit tantôt minimum [66], tantôt moyenne [67] pour le même protocole.
2. **Valeur de l'exécution de l'échantillon le moins suspect.**
   - 2605.26047 : « gives only a small empirical safety gain in our setting (+3.9 pp, with the confidence interval overlapping zero) » [37].
   - Ctrl-Z ne mesure jamais ce point isolément. Son report vers un rééchantillon combine la pression de sélection, l'information et le report vers le modèle de confiance [19]. Le contraste se lit donc entre un mécanisme proposé par Ctrl-Z et un effet isolé dans 2605.26047, pas entre deux chiffres de même définition.
   - 2605.26047 retrouve le mécanisme (54 % à 32 % [56]) « but it is much weaker » [57].
3. **Audit après plusieurs coups** (hors résumé) : 2605.26047 trouve que k > 1 fait baisser la sécurité [69], contre le gain de Ctrl-Z (tableau 1).

**Portée** : les deux études diffèrent sur trop de points pour que leurs chiffres s'opposent directement :
- cadre : BashBench contre BashArena 1.1 ;
- modèles : petits contre frontière ;
- budget d'audit : 1 % contre 0,3 % ;
- définition de la sécurité : épisode entier contre normalisation sans les issues nulles ;
- attaque : gabarits humains contre attaques inventées par le modèle.

2605.26047 présente son désaccord comme dépendant du cadre (« in our setting » [35], [37]) et non comme une réfutation. Pour H6, la conséquence est simple : le seul mécanisme des deux pièces qui baisse le succès de l'attaque hors audit (l'exécution du moins suspect) est **ciblé par le moniteur**, et il est contesté.

## 5. Ce qui reste revendicable (formulation exacte)

« Pour une intervention non spécifique sur l'agent, appliquée à intensité fixe sur une échelle d'intensités, une chute du succès du sabotage **diffus** d'agent significativement plus rapide que celle de l'utilité honnête, la marge étant mesurée comme une différence de pentes et testée. Cela vaut :
- pour la paraphrase de ses actions ;
- pour la remise à zéro de son contexte ;
- pour un rééchantillonnage dont l'action exécutée n'est choisie par aucun moniteur, la chute ne passant pas par un audit déclenché par un moniteur. »

Ce qui en sort :
- le **rééchantillonnage systématique à k fixe comme amplificateur d'audit**, en sabotage concentré, qui baisse la part d'attaques réussies sans coût d'utilité, est publié (2605.26047v2, p. 1, 2, 6, 8, 9) et se cite comme antériorité ;
- la **forme générale de la marge asymétrique** pour un rééchantillonnage **déclenché par le moniteur** est publiée (Ctrl-Z, p. 1, 8, 9).

Réserve de lecteur : le partage entre lecture large et lecture stricte de « succès du sabotage » touche la revendication elle-même. Il relève d'un nœud de Lazar, pas de ce rapport.

## 6. Ce qu'une phrase publique sur H6 ne doit pas affirmer

- Que la baisse du succès des attaques sans coût d'utilité par un rééchantillonnage systématique, à intensité fixe, est nouvelle (2605.26047, p. 1, 2, 6, 9).
- Que la forme « succès d'attaque qui chute plus vite que l'utilité » est nouvelle en général (Ctrl-Z, p. 1).
- Que Ctrl-Z montre une marge pour une intervention non spécifique : tout y est déclenché par le moniteur (p. 6, 33-34).
- Que le « 58 % à 7 % » de Ctrl-Z est dû au seul rééchantillonnage : il inclut la surveillance non fiable (p. 9, tableau 2 ; rapprochement par calcul, section 2.1).
- Que l'exécution de l'échantillon le moins suspect est un mécanisme établi : il est contesté (2605.26047, p. 1, 9-11).
- Que 2605.26047 réfute Ctrl-Z : il rattache l'écart au cadre (p. 1, 10, 11).
- « Libre », « zone vierge » ou « trou du champ » : la composante non occupée l'est seulement « dans les pièces lues » (règle R8).

## 7. Voisins nommés dans les pièces et non lus

- **Kutasov et al. 2025a**, « Evaluating control protocols for untrusted AI agents », arXiv 2511.02997. Rééchantillonnage combiné au report vers le modèle de confiance et à l'édition de confiance, dans SHADE-Arena. Nommé dans 2605.26047 p. 1 [39], p. 2, p. 12 [62]. **À lire en priorité contre H6.**
- **Kutasov et al. 2025b**, SHADE-Arena (agrégation par le maximum, second maximum) : 2605.26047 p. 4, p. 12, p. 24.
- **Hopman et al. 2025**, billet sur l'exploitation du retour du moniteur : 2605.26047 p. 1, p. 12.
- **Kaufman et al. 2025**, BashArena : 2605.26047 p. 2, p. 3, p. 12.
- **Kaufman et Lucassen 2026**, billet sur les défaillances en direct : 2605.26047 p. 3, p. 12.
- **Lindner et al. 2025**, arXiv 2512.22154 : 2605.26047 p. 3, p. 12.
- **Billets de fournisseurs sur le nouvel essai en production** (Hughes 2026 ; Trębacz et al. 2026) : 2605.26047 p. 1, p. 12.
- **Greenblatt et al. 2023**, arXiv 2312.06942 (édition de confiance, paraphrase contre la collusion) : Ctrl-Z p. 1, 2, 4, 5, 9, 10, 11 ; 2605.26047 p. 1, p. 12.
- **Wen et al. 2024**, arXiv 2411.17693 (menaces distribuées) : Ctrl-Z p. 10, p. 12. Déjà voisin au niveau 2 (`anteriorite-v1.md`, l. 157).
- **Mallen et al. 2024**, arXiv 2412.12480 : Ctrl-Z p. 10, p. 12.
- **Griffin et al. 2024** (jeux de contrôle) : Ctrl-Z p. 10, p. 11.
- **Shlegeris 2024** (collusion, paraphrase) : Ctrl-Z p. 12, p. 23.

## 8. Table fermée

| énoncé | verdict | pièces qui portent le verdict |
|---|---|---|
| H6 (énoncé de N-015) | **occupé en partie** | 2605.26047v2 (p. 1, 2, 6, 8, 9, 10, 11) ; Ctrl-Z 2504.10374v1 voisin (p. 1, 5, 6, 8, 9, 33-34) |
