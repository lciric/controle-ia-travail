# Rapport du lecteur — H6, « marge asymétrique », contre Ctrl-Z et 2605.26047 — v2

**lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B**

- **Date et heures** : reprise de la session le 2026-11-13 23:13:28 UTC ; rapport v2 fermé le 2026-11-13 23:19:24 UTC (heures relevées par `date -u`).
- **Rapport remplacé** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-H6-v1.md`, `86b2d0cdaf90f9c58644d5af89b362f40da825867f69995a9dccf0ce9786f132` (scellé, non modifié) ; archive v1 `fichiers-de-travail-H6-v1.tar`, `ce9479658227355319f85f5f389812de37e26a8194ad051e58961e7e29ae0088`.
- **Contre-lecture intégrée** :
  - `contre-lecture-rapport-H6-v1.md`, `3ce3ac3cf73ea481dd7d04f411d9a30d74f6a0489f531d1cfa24d40f4825666e` (vérifiée) : « tient avec corrections », trois majeurs (A, B, C), sept mineurs (D à J) ;
  - son archive `fichiers-de-travail-contre-lecture-H6-v1.tar`, `2bd48d6668b01576582ca7126056f07a45668c665b4ff566ab48c519a46c4587` (vérifiée), extraite dans un sous-dossier neuf du dossier de travail.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (revérifiée) ; `interdits-communs-v2.md` tenu (aucune commande git).
- **Empreintes des PDF** (vérifiées contre leurs compagnons `.sha256`) :
  - `2504.10374v1.pdf` (Ctrl-Z) : `5f802d679344fe5e15d1edd50e96245f3bdc054e69d1ff0880b077d173549211` (38 pages) ;
  - `2605.26047v2.pdf` : `947724f42324070fd47b1ecaf8c1bf9b2257df0e0c7f8822447241d3ea9a28fa` (46 pages).
- **Fichiers lus** :
  - pour la v1 : la consigne commune ; `interdits-communs-v2.md` ; `docs/programme-controle-ia-v2.md` l. 85-125 et 185-200 ; `docs/decisions/decision-N-013-v1.md` l. 76-81 ; `docs/decisions/decision-N-015-v1.md` en entier ; `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` l. 152-165 (nommé dans le mandat du lecteur ; réponse à la question du constat J) ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` l. 172-182 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` l. 408-441 ; les deux PDF et leurs compagnons ;
  - en plus, pour la v2 : la contre-lecture et son archive ; mon rapport v1. Aucune ouverture fautive, aucun refus.
- **Étendue lue** :
  - lecture v1 (ensemble des deux PDF) : voir la section 9 ;
  - relu ligne à ligne pour la v2 (texte brut de `pdftotext`) :
    - Ctrl-Z : p. 5, 6 (figure 4 et légende), 7-8 (tirage illimité), 10 (limites), 13 (annexe A), 19 (annexe C, définition de la sécurité), 29 à 31 (annexe H) ;
    - 2605.26047 : p. 3 (définition), 4 (note 3), 6, 10, 11, 12 (références), 15, 19 (figure 14 vue sur le PDF), 21.
- **Citations** :
  - `citations-H6-v2.json`, **dans l'archive seulement** : 106 citations (les 69 de la v1, inchangées, puis 37 ajouts, n = 70 à 106) ;
  - contrôlées par `verifier_citations_H6_v2.py` (`python3 -I`, texte brut et `-layout`) : **0 échec** ;
  - le contrôleur a été retesté avant le contrôle final : cas juste, passe ; trois cas altérés, trois échecs.
- **Chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (`calculs_H6_v2.py`, `python3 -I`, sortie `calculs-H6-v2.txt` dans l'archive).
- **Noms de modèles** : aucun n'est écrit, y compris ceux des articles (consigne commune, ligne 14, lue au sens strict).

---

## 0. Verdict

**Le verdict dépend de trois questions de lecture de l'énoncé, qui reviennent à Lazar et que je ne tranche pas** (section 1).

| lecture de l'énoncé | verdict |
|---|---|
| la plus large (succès audit compris ; pas de restriction au diffus ni aux interventions sur l'agent) | **occupé** |
| celle que le texte de N-013 et N-015 rend la plus naturelle (succès hors audit ; aucun moniteur dans le choix de l'action exécutée) | **non trouvé dans les pièces lues** |
| entre les deux | **occupé en partie** |

La table complète est en section 1.3.

- **2605.26047v2** porte toute l'occupation. Deux bras y comptent pour H6 :
  - **rééchantillonnage « pour information »** : k échantillons tirés à chaque pas, sans déclenchement (k = 1 à 5) ; l'action exécutée est toujours le premier échantillon ; le gain passe tout entier par l'audit ; l'utilité est inchangée par construction. À k = 5 : +10,2 points de sécurité, intervalle apparié à 95 % [+6,1 ; +14,3] (auteurs, [40]) ;
  - **exécution de l'échantillon le moins suspect** : deux tirages à chaque pas, sans déclenchement, mais l'action exécutée est choisie par le moniteur (p. 10) :
    - l'attaque elle-même recule hors audit : il lui faut 7,4 échantillons d'attaque par trajectoire au lieu de 6,7, différence appariée +0,66, intervalle [+0,26 ; +1,11] [88], [89] ;
    - l'utilité est mesurée : −1,0 point, intervalle [−2,8 ; +0,9] [59].
- **Ctrl-Z (2504.10374v1)** reste voisin dans toutes les lectures. Tout rééchantillonnage y est déclenché par le moniteur, et le tirage systématique y est nommé puis écarté pour son coût (p. 7-8, [70], [71], [72]).
- **Paraphrase et remise à zéro du contexte comme interventions non déclenchées sur l'agent** : non trouvées dans les deux pièces. Il y a un voisin déclenché : l'édition et la mise en œuvre de confiance de Ctrl-Z (p. 31).
- **Contradiction relevée par la contre-lecture du niveau 3 (constat M5)** : confirmée sur trois points, dont aucun ne porte sur une intervention non spécifique (section 5).

## 1. Verdict selon la lecture de l'énoncé

### 1.1 Les trois questions (nœuds de Lazar, non tranchés ici)

- **Q1, « succès du sabotage »** :
  - **L** : audit compris, c'est-à-dire la victoire de l'attaquant ;
  - **S** : hors audit, c'est-à-dire que l'intervention affaiblit l'attaque elle-même.
- **Q2, « non spécifique »** :
  - **N1** : non déclenché, ce qui admet un tirage systématique dont le moniteur choisit l'action exécutée ;
  - **N2** : aucun moniteur dans l'intervention, ni pour la déclencher ni pour choisir l'action exécutée.
- **Q3, portée** :
  - **U** : énoncé tel qu'écrit, sans restriction ;
  - **R** : restreint au sabotage diffus et aux interventions sur l'agent.

### 1.2 Ce que le texte de N-013 et N-015 rend le plus naturel (lignes)

**Q1 : penche vers S.**
- N-013, l. 80 : le risque de collision nommé est « l'affaiblissement sélectif de l'attaquant ».
- N-013, l. 79 : le bruit sur les poids est retiré parce que « la sous-performance volontaire cède avant la compétence honnête », l'usage en détection étant cité à part (« avec un usage en détection »).
- N-015, l. 18-21 : Poser est retiré pour un effet direct du bruit sur le modèle, l'usage en détection étant là encore cité à part. Le défaut relevé est « sans agent, sans utilité honnête mesurée, sans comparaison de pentes ni test ».
- N-015, l. 25-27 : le retour possible est un « succès du sabotage qui chute plus vite que l'utilité honnête » sous un bruit appliqué à l'agent.
- **Indice contraire** : programme, l. 188, « E1.6 Marge asymétrique (H6). Base : Ctrl-Z ». Le chiffre phare de Ctrl-Z est audit compris.

**Q2 : penche vers N2, sans définition écrite.**
- Programme l. 97, N-013 l. 78 et N-015 l. 15-17 : « non spécifique » n'est défini nulle part.
- Toutes les interventions de la liste (paraphrase, rééchantillonnage, remise à zéro, bruit) se pratiquent sans moniteur. Les deux retraits (N-013 l. 79, N-015 l. 18-21) portent sur des travaux sans moniteur.
- E1.6 prend pour base Ctrl-Z (l. 188), dont le rééchantillonnage est déclenché et choisi par le moniteur. « Non spécifique » s'y oppose le plus naturellement en entier.

**Q3 : partagée.**
- **« Sur l'agent »** est naturel : N-015 l. 16 dit « sabotage d'agent », et Poser est retiré entre autres parce que « sans agent » (l. 21).
- **« Diffus » n'est pas dans l'énoncé** (programme l. 97 ; N-013 l. 78 ; N-015 l. 15-17), alors que H1 le porte en toutes lettres (l. 93). Il n'y entre que par le contexte :
  - H6 est rangée sous « Papier A — le temps » (l. 92), dont l'environnement est « Sabotage diffus » (l. 122) ;
  - E1.6 a une expérience sœur distincte, « E1.7 Transfert concentré » (l. 189).
  - Le contexte suggère donc que l'expérience se fait en diffus ; le texte de la revendication ne le restreint pas.

**Lecture la plus naturelle selon ces lignes : S, N2, sur l'agent, « diffus » non écrit.** Elle donne « non trouvé dans les pièces lues », que « diffus » soit retenu ou non.

### 1.3 Table fermée, par lecture

| lecture | verdict | ce qui porte le verdict |
|---|---|---|
| L, N1, U | **occupé** | 2605.26047, bras « pour information » à k fixe : succès audit compris en baisse significative (+10,2 points de sécurité, [+6,1 ; +14,3], p. 2 [40]), utilité inchangée (p. 6 [50]) ; réserve : marge vraie par construction, sans comparaison de pentes |
| L, N2, U | **occupé** | même bras : l'action exécutée est le premier tirage, aucun moniteur ne la choisit (p. 6 [49], p. 11 [92]) ; même réserve |
| L, N1, R | **occupé en partie** | composantes faites en cadre concentré (« live failures », p. 3 [42]) ; non fait : le diffus ; et, pour le bras « pour information », l'action sur l'agent |
| L, N2, R | **occupé en partie** | idem |
| S, N1, U | **occupé en partie** | 2605.26047, exécution du moins suspect à N = 2 : attaque affaiblie hors audit ([88], [56]), utilité mesurée ([59]), une seule intensité ; non fait : un taux de succès hors audit mesuré qui chute significativement (l'effet sur la sécurité contre la base pour information est +3,9 [−2,1 ; +10,9], [55]), une échelle d'intensités, une comparaison de pentes |
| S, N1, R | **occupé en partie** | idem, en cadre concentré : le diffus n'est pas fait |
| S, N2, U | **non trouvé dans les pièces lues** | aucun bras sans moniteur qui affaiblisse l'attaque hors audit ; voisins : 2605.26047, p. 6, 10 ; Ctrl-Z, p. 6, 31 |
| S, N2, R | **non trouvé dans les pièces lues** | idem |

« Non trouvé » veut dire « non trouvé dans les deux pièces lues », jamais « trou du champ » (règle R8). Deux pièces nommées et non lues pèsent directement sur la lecture S : arXiv 2511.02997 et arXiv 2607.13087 (section 8).

## 2. Énoncé confronté

- **N-015, l. 15-17** : « pour l'une au moins des trois interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte), il existe une intensité où, **en moyenne à intensité fixe**, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête ».
- Le bruit d'activations (N-015) et le bruit sur les poids (N-013) sont mesurés mais non revendiqués.
- **Forme existentielle** : une seule intervention et une seule intensité suffisent à occuper l'énoncé.
- **Composantes confrontées** :
  - (a) intervention non spécifique ;
  - (b) intensité fixe, sur une échelle ;
  - (c) chute du succès d'attaque significativement plus rapide que celle de l'utilité honnête ;
  - (d) sabotage diffus (composante du mandat, absente du texte de l'énoncé : section 1.2, Q3).

## 3. Ctrl-Z — 2504.10374v1 (Bhatt, Rushing, Kaufman, Tracy, Georgiev, Matolcsi, Khan, Shlegeris)

**Venue imprimée** : prépublication arXiv, v1, 14 avril 2025 [1] ; aucune conférence ni revue.

### 3.1 Ce qu'il fait
- **Cadre** : BashBench, 257 tâches d'administration système en plusieurs pas (p. 1-2) ; épisode simulé de 100 000 tâches (annexe C).
- **Modèles** : un petit modèle commercial joue le modèle non fiable ; un modèle ouvert de 8 milliards de paramètres joue le modèle de confiance (p. 3).
- **Attaque** : une seule cible, le téléchargement et l'exécution d'un logiciel malveillant factice ([7], [28]), à partir de gabarits écrits par des humains.
- **Métriques** :
  - utilité normalisée entre le modèle de confiance (0 %) et le modèle non fiable honnête (100 %) [6] ;
  - sécurité : probabilité que l'équipe bleue finisse l'épisode sans exécution du logiciel malveillant [7]. Un épisode sans issue décisive compte comme victoire bleue [84] ; à l'intérieur d'une tranche, une attaque peut échouer en silence [83] ;
  - budget d'audit de 1 % ; courbes à 0,3 % et 3 % en annexe A [85].
- **Résultats** (auteurs) :
  - audit initial : 5,5 % [10] ;
  - surveillance de confiance : 41,8 % [11] ;
  - report vers le modèle de confiance : 72,7 % à 95 % d'utilité [14] ;
  - report vers un rééchantillon : 83,2 % ; voyage dans le temps : 87,1 % [22] ;
  - avec surveillance non fiable : 92,6 % (tableau 2, [24]).
- **Chiffre du résumé** : « 58% to 7% at a 5% cost » [4].
  - 58,2 % = 1 − 41,8 % ; 7,4 % = 1 − 92,6 % (calcul).
  - 92,6 % est la seule cellule des tableaux 1 et 2 dont le complément s'arrondit à 7 % : le rapprochement est le seul possible.
  - Le résumé décrit ce protocole comme « combines resampling with analysis of previous steps » [4], sans nommer la surveillance non fiable. La figure 2 nomme pourtant la courbe « DTR + Time Travel + UM » [86] (report vers un rééchantillon, voyage dans le temps, surveillance non fiable).
  - Sans surveillance non fiable : 12,9 % (calcul).
  - La cellule « 58,3 % » du tableau 1 (report vers le modèle de confiance, 99 % d'utilité, auteurs) est sans rapport avec ce 58 %.
- **Échelle d'intensité** : seuils de report de 50 % à 99 % [68]. Droites d'utilité ajustées sur la figure 3 (« y = 0.33x + 0.71 » et « y = 0.74x + 0.31 », lu sur le PDF, non contrôlé par programme). Le seuil est un quantile des scores du moniteur [12].

### 3.2 Ce qui est déclenché par le moniteur, et ce qui ne l'est pas
- **Déclenché** :
  - tout rééchantillonnage : [15], [29], [30] ;
  - le choix de l'action exécutée : [16] ;
  - le report vers le modèle de confiance : [31] ;
  - l'**édition de confiance** : « Prompt T with U's action and ask T to edit the action to be less suspicious » [87]. Les attaques y survivent « around 14% of the time » [73], pour 1,71 pas de plus jusqu'au succès [76] ;
  - la **mise en œuvre de confiance** (résumé de l'action, puis nouvelle action écrite à partir du résumé, [75]) : elle « never preserves an attack » [74], pour 2,26 pas de plus [77]. Le report simple coûte 2,76 pas [78].
  - Ces deux mesures sont jugées de faible bénéfice (« only provide slight benefits », [79]), sans sécurité ni utilité chiffrée.
  - Ce sont des réécritures **déclenchées**, dont l'action exécutée est écrite par le modèle de confiance, non une paraphrase des actions de l'agent exécutée telle quelle. Elles sont voisines de la branche « paraphrase » en lecture S.
- **Non déclenché, mais hors de la forme de H6** :
  - audit initial [9] ;
  - paraphrase de confiance de l'entrée du moniteur non fiable ([25], [26]), sans mesure isolée ;
  - remise à zéro de l'état entre tâches, règle du cadre [5]. Une limite reconnue sur l'état partagé entre tâches est dite, non mesurée [80].
- **Tirage systématique nommé et écarté** : « If the blue team could use unlimited resampling, they would » [70] « draw many samples at every step, so they can make a more informed decision about auditing » [71] ; puis « we still restrict the blue team to no more than double the queries to » U [72]. Le bras est donc nommé et non fait.
- **Figure 4** :
  - à droite : « up to six resamples per action » [17] ; la légende donne 33,2 % d'attaques repérées sans rééchantillonnage [81] et 70,6 % avec [82] (auteurs). C'est une valeur d'information du rééchantillonnage, mesurée sur des distributions de scores ; la légende ne dit pas si le tirage est déclenché ;
  - au milieu : nombre de pas d'attaque nécessaires pour réussir une fois, sous report vers le modèle de confiance et vers un rééchantillon (figure). C'est une mesure d'affaiblissement de l'attaque hors audit, pour un rééchantillonnage **déclenché** ([20] pour la phrase voisine).

### 3.3 Limites, incohérences, trop beau
- **Limites reconnues** : cible étroite [28] ; état partagé [80] ; audit supposé infaillible (p. 10, [8]) ; résultats absolus sensibles au budget [27].
- **Incohérences** :
  - « minimum » en note 8 [66] contre « mean » en annexe J [67], pour le même protocole ;
  - l'audit après trois coups « doesn't improve » (p. 8), alors que le tableau 1 le place au-dessus de l'incrimination au présent ;
  - le résumé sous-décrit son propre chiffre (section 3.1).
- **Aucun intervalle de confiance.**

### 3.4 Verdict par composante (Ctrl-Z)

| composante | verdict | page, citation |
|---|---|---|
| (a) non spécifique | **ne touche pas** pour le rééchantillonnage (déclenché ; tirage systématique nommé et non fait) ; **voisin** pour la paraphrase (de l'entrée du moniteur) ; **voisin** pour la réécriture des actions (édition et mise en œuvre de confiance, déclenchées) | p. 6 [15] ; p. 7-8 [70]-[72] ; p. 9 [25], [26] ; p. 31 [73]-[75], [87] |
| (b) intensité fixe, échelle | **voisin** : seuils de 50 % à 99 %, échelle d'une intervention déclenchée | p. 29 [68] ; p. 5 [12] |
| (c) marge asymétrique | **voisin** : 58 % à 7 % pour 5 % d'utilité, déclenché et combiné à la surveillance non fiable, sans intervalle | p. 1 [4] ; p. 4 [86] ; p. 9 [24] |
| (d) diffus | **ne touche pas** | p. 3 [7] ; p. 10 [28] |

**Ctrl-Z contre H6 : voisin, dans toutes les lectures.**

## 4. 2605.26047v2 — « Retrying vs Resampling in AI Control » (Lucassen, Kaufman ; Redwood Research)

**Venue imprimée** : prépublication arXiv, v2, 26 mai 2026 [32] ; aucune conférence ni revue.

### 4.1 Ce qu'il fait
- **Cadre** : BashArena 1.1, quatre tâches secondaires [43], défaillances en direct [42], audit par pas à 0,3 %.
- **Modèles** : un modèle de frontière non fiable ; un moniteur ouvert plus faible.
- **Attaquant** : il attaque chaque tâche principale [98] ; aucune sélection d'attaque hors de l'annexe G.
- **Sécurité** : « normalized to ignore no-win outcomes » [99]. Son complément est la part de victoires de l'attaquant parmi les parties décidées, pas un taux de réussite des attaques.
- **Base** : surveillance de confiance, 61 % [57 ; 64] [44] (60,9 % en p. 15 [103]).

### 4.2 Bras 1 — rééchantillonnage « pour information », k fixe à chaque pas
- **Bras** : « Fixed resampling: always draw k samples » [51]. Il exécute toujours le premier échantillon ou audite [49] ; il « does not affect the tool calls that get executed, only which ones are audited » [92]. Utilité « exactly zero effect » [50], par construction, non mesurée.
- **Résultats** :
  - échelle N = 1 à 5 (figure 3a, avec l'agrégation max : environ 61, 68, 70, 71, 71 %, figure) ;
  - à N = 5 : +10,2 points [+6,1 ; +14,3] [40], 61 % à 71 % [33] (70,9 % en p. 15 [104]) ;
  - part de victoires de l'attaquant parmi les parties décidées : de 39 % à 29 % (calcul ; 39,1 % à 29,1 % avec les chiffres de la p. 15).
- **Écart de figures** : à k = 2, la figure 6a donne environ 66 % et la figure 3a environ 68 % (figure).

### 4.3 Bras 2 — exécution de l'échantillon le moins suspect, N = 2 à chaque pas
- **Bras** : il tire N = 2 « per step », exécute le moins suspect et audite sur le maximum [54]. Le tirage n'est pas déclenché ; l'action exécutée est choisie par le moniteur.
- **Sécurité** :
  - 72 %, intervalle [67 ; 77] [90], contre 68 % pour le bras 1 à N = 2 : +3,9 points [−2,1 ; +10,9], l'intervalle couvre zéro [55] ;
  - contre la surveillance de confiance sur le sous-ensemble apparié [91] : environ 62 % (figure 7(i), base en pointillé), soit environ +10 points (calcul sur lecture de figure), sans intervalle apparié imprimé ;
  - la figure 14a (p. 19, vue sur le PDF) trace les trois courbes sur toute la plage de budgets [94] ; le bras 2 reste au-dessus de la base partout (figure).
- **Attaque affaiblie hors audit** :
  - sur les pas mixtes, la part d'échantillons d'attaque exécutés passe de 54 % à 32 % [56] ;
  - échantillons d'attaque tirés par trajectoire : 7,4 contre 6,7 [89], différence appariée +0,66 [+0,26 ; +1,11] [88]. L'intervalle exclut zéro.
  - Ce qui est mesuré est un coût pour l'attaquant, pas un taux de succès hors audit.
- **Utilité mesurée** : −1,0 point [−2,8 ; +0,9], 298 tâches appariées [59] ; second jeu de 50 tâches, 0,0 [−10 ; +10] (p. 11, [100] ; le « n=506 » du texte extrait est « n=50 » suivi de l'appel de note 6).
- **Portée selon les auteurs** : même mécanisme que dans Ctrl-Z, « much weaker », nul contre un attaquant optimalement constant [57], [41].

### 4.4 Consigne « prudente » toujours appliquée (hors liste de H6)
- **Résultats** : +4,0 points de sécurité [+0,8 ; +8,9] [47] pour −5,3 points d'utilité [−6,8 ; −3,7] [48] ; l'utilité passe de 69,0 % à 63,8 % [105] (écart brut 5,2, calcul ; les auteurs donnent −5,3 en apparié).
- **Selon l'échelle** :
  - en points, la sécurité gagne moins que l'utilité ne perd ;
  - en relatif, la part de victoires de l'attaquant baisse de 10,2 % et l'utilité de 7,5 % (calcul).
  - Le signe dépend donc de l'échelle : **ni indice ni contre-indice**.
- **Nature** : un déplacement le long d'une frontière (« Caution protocols move along the Pareto frontier », [95]). La consigne change la politique honnête ; le mécanisme par les scores honnêtes est imprimé pour la variante sélective (p. 6, [106]), pas pour celle-ci.

### 4.5 Ni paraphrase ni remise à zéro du contexte
Le rééchantillonnage tire « from the exact same context » [96].

### 4.6 Limites, incohérences, trop beau
- **Incohérences** :
  - référence de Ctrl-Z « arXiv:2504.00000 » [61] ;
  - base 61 % [57 ; 64] [44], 60,7 % [55,4 ; 64,6] [47], 60,9 % [103] ;
  - consigne d'attaque annonçant un remplacement par le modèle de confiance, absent des protocoles de rééchantillonnage étudiés [64] ;
  - p. 19, l'exécution du moins suspect offre « a small, marginally significant improvement » [93], quand p. 10 l'intervalle « includes 0 » [55] ;
  - deux références « Kutasov » à prénoms différents [101], [102] (forme).
- **Limite reconnue** : auditeur simulé à 91 %, d'où une sécurité surestimée d'environ 10 % (p. 15).
- **Trop beau (règle R4)** : l'utilité du bras 1 est inchangée par définition, pas par mesure.

### 4.7 Verdict par composante (2605.26047), selon la lecture

| composante | verdict | page, citation |
|---|---|---|
| (a) non spécifique | **occupée** sous N1 et N2 pour le bras 1 (tirage à k fixe, aucun moniteur dans le choix) ; sous N1 seulement pour le bras 2 (tirage non déclenché, choix par le moniteur) | p. 8 [51] ; p. 6 [49] ; p. 11 [92] ; p. 10 [54] |
| (b) intensité fixe, échelle | **occupée** pour le bras 1 (N = 1 à 5) ; une seule intensité pour le bras 2 (N = 2) | p. 7, figure 3a ; p. 9 [52] ; p. 10 [54] |
| (c) chute plus rapide que l'utilité | lecture L : **occupée** (bras 1, +10,2 [+6,1 ; +14,3], utilité constante par construction ; ni pente ni test de différence de pentes) ; lecture S : **occupée en partie** sous N1 (bras 2 : attaque affaiblie, +0,66 [+0,26 ; +1,11], utilité −1,0 [−2,8 ; +0,9] ; aucun taux de succès hors audit mesuré, aucune échelle), **non faite** sous N2 | p. 2 [40] ; p. 6 [50] ; p. 10 [55], [56], [88] ; p. 11 [59] |
| (d) diffus | **ne touche pas** (pèse seulement sous R) | p. 3 [42], [43] |

## 5. Les deux pièces se contredisent-elles ? (constat M5)

**Oui, sur trois points ; aucun ne porte sur une intervention non spécifique.**

1. **Agrégation** : minimum chez Ctrl-Z ([65], [66]), maximum chez 2605.26047, « the opposite of what Ctrl-Z found » [36]. Kutasov et collègues 2025b utilisent aussi le maximum [97]. 2605.26047 en donne la raison : une corrélation honnête entre tirages trop forte pour le minimum [58].
2. **Valeur de l'exécution du moins suspect** :
   - 2605.26047 : +3,9 points, intervalle couvrant zéro, contre le bras 1 ([37], [55]) ; environ +10 points contre la base (figure) ;
   - Ctrl-Z n'isole jamais ce point ; son report vers un rééchantillon combine sélection, information et report vers le modèle de confiance [19] ;
   - 2605.26047 retrouve le mécanisme, plus faible [57].
3. **Audit après plusieurs coups** : il fait baisser la sécurité selon 2605.26047 [69], contre un gain chez Ctrl-Z.

**Portée** : les deux études diffèrent sur plusieurs points :
- cadre, modèles et attaquant ;
- budget d'audit : 1 % contre 0,3 % (Ctrl-Z donne aussi 0,3 % en annexe A [85]) ;
- définition de la sécurité. Toutes deux écartent l'attaque qui échoue en silence ([83], [99]), mais Ctrl-Z compte l'épisode sans issue comme une victoire bleue [84].

2605.26047 rattache l'écart au cadre (« in our setting », [35], [37]) : ce n'est pas une réfutation.

## 6. Ce qui reste revendicable, selon chaque lecture

Ces formulations décrivent ce que les deux pièces lues laissent ouvert sous chaque lecture. **Elles ne choisissent pas de lecture et n'ajoutent rien à l'énoncé de N-015.** Toute précision au-delà de son texte (« diffus », « sur l'agent », « différence de pentes testée ») est un resserrement qui relève d'un nœud de Lazar ; je la signale là où elle intervient.

- **Lectures L, U (N1 ou N2)** : pour le rééchantillonnage, l'énoncé est occupé (bras 1). Reste ouvert : l'énoncé pour la paraphrase ou la remise à zéro du contexte, non trouvées dans les pièces lues.
- **Lectures L, R** : l'énoncé en sabotage diffus, pour l'une des trois interventions, rééchantillonnage compris. Sous R, ce qui distingue est le diffus et l'intervention sur l'agent, ajoutés par la lecture R elle-même.
- **Lectures S, N1 (U ou R)** :
  - pour la paraphrase et la remise à zéro du contexte : l'énoncé entier ;
  - pour le rééchantillonnage : la chute significative d'un **taux de succès** de l'attaque hors audit, plus rapide que l'utilité honnête. 2605.26047 ne mesure à N = 2 qu'un coût pour l'attaquant, sans échelle d'intensités ;
  - sous R : en sabotage diffus.
- **Lectures S, N2 (U ou R)** : l'énoncé entier, pour les trois interventions, non trouvé dans les pièces lues. Les voisins se citent : 2605.26047 (bras 1 et 2), Ctrl-Z (rééchantillonnage déclenché, édition et mise en œuvre de confiance).
- **Une précision pèse sous toutes les lectures** : l'énoncé ne demande pas une « différence de pentes testée ». N-015 l. 21 cite pourtant l'absence de « comparaison de pentes ni test » comme défaut de Poser. Les ajouter resserre la revendication et revient à Lazar.

## 7. Ce qu'une phrase publique sur H6 ne doit pas affirmer

- Que la baisse du succès des attaques, audit compris et sans coût d'utilité, par un rééchantillonnage systématique à intensité fixe est nouvelle (2605.26047, p. 1, 2, 6, 8, 9).
- Que nul n'a mesuré l'utilité sous un rééchantillonnage fait à chaque pas (2605.26047, p. 11).
- Qu'aucun rééchantillonnage non déclenché n'affaiblit l'attaque hors audit (2605.26047, p. 10, à N = 2, avec choix par le moniteur).
- Que la forme « succès d'attaque qui chute plus vite que l'utilité » est nouvelle en général (Ctrl-Z, p. 1).
- Que Ctrl-Z montre une marge pour une intervention non spécifique (tout y est déclenché, p. 6, 33-34), ou qu'il n'a pas pensé au tirage systématique (il le nomme et l'écarte, p. 7-8).
- Que le « 58 % à 7 % » est dû au seul rééchantillonnage (il inclut la surveillance non fiable, p. 4, 9).
- Que réécrire les actions de l'agent n'a jamais été montré comme cassant des attaques (Ctrl-Z, p. 31, réécriture déclenchée).
- Que l'exécution du moins suspect est un mécanisme établi (contesté, 2605.26047, p. 1, 9-11), ou que 2605.26047 réfute Ctrl-Z (il rattache l'écart au cadre).
- Que la consigne prudente de 2605.26047 est un contre-exemple, ou un exemple, de marge asymétrique (le signe dépend de l'échelle, p. 6).
- Que le résultat de 2605.26047 vaut contre un attaquant qui choisit ses tâches (il attaque chaque tâche, p. 21).
- Que « sabotage diffus » figure dans l'énoncé de H6 (N-015 l. 15-17).
- « Libre », « zone vierge » ou « trou du champ » (règle R8).

## 8. Voisins nommés et non lus

**Nommés dans les pièces** :
- **Kutasov et collègues 2025a**, « Evaluating control protocols for untrusted AI agents », arXiv 2511.02997 : 2605.26047 p. 1 [39], p. 2, p. 12 [62]. Rééchantillonnage combiné au report et à l'édition de confiance, dans un autre cadre d'agent. **À lire en priorité.**
- **Kutasov et collègues 2025b**, SHADE-Arena (agrégation par le maximum) : 2605.26047 p. 4, p. 6 [97], p. 12 [101], p. 24.
- **Hopman et collègues 2025** (exploitation du retour du moniteur) : 2605.26047 p. 1, 12.
- **Kaufman et collègues 2025** (BashArena) : 2605.26047 p. 2, 3, 12.
- **Kaufman et Lucassen 2026** (défaillances en direct) : 2605.26047 p. 3, 12.
- **Lindner et collègues 2025**, arXiv 2512.22154 : 2605.26047 p. 3, 12.
- **Billets de fournisseurs sur le nouvel essai en production** (Hughes 2026 ; Trębacz et collègues 2026) : 2605.26047 p. 1, 12.
- **Greenblatt et collègues 2023**, arXiv 2312.06942 : Ctrl-Z p. 1, 2, 4, 5, 9, 10, 11 ; 2605.26047 p. 1, 12.
- **Wen et collègues 2024**, arXiv 2411.17693 : Ctrl-Z p. 10, 12 ; déjà voisin au niveau 2.
- **Mallen et collègues 2024**, arXiv 2412.12480 : Ctrl-Z p. 10, 12, 23.
- **Griffin et collègues 2024** : Ctrl-Z p. 10, 11.
- **Shlegeris 2024** : Ctrl-Z p. 12, 23.

**Nommé par l'énoncé, non par les pièces** :
- **arXiv 2607.13087**, « l'affaiblissement sélectif de l'attaquant » (N-013, l. 80). C'est le voisin le plus direct pour la lecture S.

## 9. Étendue de la lecture v1 (pour mémoire)

- **2504.10374v1** : 38 pages lues ligne à ligne en texte brut ; code des pages 15 à 17 parcouru ; figures des pages 4 à 6 vues.
- **2605.26047v2** : pages 1 à 28 lues ligne à ligne ; pages 29 à 46 (exemples de code) parcourues par mots ; figures des pages 2, 7, 9, 10 vues.
- **Session v1** : de 22:51:46 à 23:01:27 UTC (`date -u`), soit moins de dix minutes (constat J). Les pages signalées sont relues pour cette v2 (en-tête) ; le journal v2 est dans l'archive.

## 10. Suite donnée à la contre-lecture

| constat | gravité | décision | où | motif |
|---|---|---|---|---|
| A — exécution du moins suspect : tirage non déclenché, attaque affaiblie hors audit, utilité mesurée | majeur | corrigé | sections 0, 1.3, 4.3, 4.7, 5 | Relu p. 10, 11, 19 et figure 14a : tirage « per step » [54] ; +0,66 [+0,26 ; +1,11] [88] ; utilité −1,0 [−2,8 ; +0,9] [59] ; environ 62 % de base sur la figure 7(i) [91]. Le classement dépend de Q2, d'où la table par lecture. Précision : l'effet mesuré est un coût pour l'attaquant, pas un taux de succès hors audit. |
| B — réécriture déclenchée des actions, avec survie des attaques | majeur | corrigé | sections 0, 3.2, 3.4, 7 | Relu p. 5, 29-31, 10 : 14 % [73], « never preserves » [74], 1,71, 2,26 et 2,76 pas [76]-[78], « slight benefits » [79], état partagé [80]. Nuance : l'action exécutée est écrite par le modèle de confiance ; c'est une réécriture déclenchée, non une paraphrase des actions de l'agent, d'où « voisin » en lecture S. |
| C — « diffus » hors de l'énoncé ; « reste revendicable » resserrait la revendication | majeur | corrigé | sections 1.2, 1.3, 2, 6, 7 | Programme l. 97, N-013 l. 78, N-015 l. 15-17 : ni « diffus » ni « sur l'agent ». La section 6 ne choisit plus de lecture et signale chaque resserrement. Indices de contexte vers le diffus ajoutés (l. 92, 122, 189), sans en faire une restriction. |
| D — la consigne prudente n'est pas un contre-indice | mineur | corrigé | section 4.4 | Relu p. 4 (note 3 [95]) et p. 6 : en relatif, −10,2 % contre −7,5 % (calcul) ; signe dépendant de l'échelle. Mécanisme imprimé pour la variante sélective seulement [106]. |
| E — grandeur « part d'attaques réussies » mal nommée | mineur | corrigé | sections 4.1, 4.2, 5 | Relu p. 3 [99] : renommée « part de victoires de l'attaquant parmi les parties décidées ». Relu Ctrl-Z p. 19 : il écarte aussi l'attaque qui échoue en silence [83], mais compte l'épisode sans issue comme victoire bleue [84]. L'écart de définition est donc plus petit qu'en v1, sans être nul. |
| F — tirage systématique nommé par Ctrl-Z ; chiffres de la figure 4 | mineur | corrigé | section 3.2 | Relu p. 7-8 : [70], [71], [72]. Figure 4 : 33,2 % [81] et 70,6 % [82] ; figure 4 milieu nommée. |
| G — calcul du 7 % juste ; deux précisions | mineur | corrigé | section 3.1 | Figure 2 [86] : le résumé sous-décrit son chiffre. Cellule 58,3 % du tableau 1 distinguée. Unicité du rapprochement vérifiée (calcul). |
| H — indices du texte absents ; 2607.13087 manquant | mineur | corrigé | sections 1.2, 8 | N-013 l. 79-80 ; N-015 l. 18-27 ; programme l. 188 relus avec leurs numéros. 2607.13087 ajouté, « nommé par N-013, non par les pièces ». |
| I — incohérences de 2605.26047 ; budget de Ctrl-Z | mineur | corrigé | sections 4.3, 4.6, 5, 8 | « marginally significant » [93] contre « includes 0 » [55] ; « n=506 » = « n=50 » plus l'appel de note [100] ; prénoms Kutasov [101], [102] ; Ctrl-Z à 0,3 % en annexe A [85] ; Kutasov 2025b aussi p. 6 [97]. |
| J — profondeur et journal | mineur | corrigé | en-tête, section 9 | La durée de la session v1 (moins de dix minutes) est exacte et reste lisible dans le journal v1. Les omissions relevées (p. 7-8 et 31 de Ctrl-Z, figure 7(i), figure 14a, calcul relatif) sont relues ligne à ligne et intégrées ; heures dans le journal v2. `anteriorite-v1.md` l. 152-165 était nommé dans mon mandat. |
