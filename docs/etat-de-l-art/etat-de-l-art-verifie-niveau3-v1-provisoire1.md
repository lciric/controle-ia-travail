# État de l'art vérifié sur sources primaires — niveau 3 — v1, version provisoire 1

Date : 2026-11-10, vers 11:15 UTC (heure relevée par `date -u`). Session fille « état de l'art niveau 3 »
(`session_01QPDgKefT7L1TvJMZ4BiBNb`), branche `prep/etat-de-l-art-niveau3-v1`.

**Statut : PROVISOIRE.** Écrite avant la fin des lectures, parce que le quota du compte impose un arrêt possible. Elle
vaut pour les quatorze rapports scellés de cette session et pour les quatre rapports déjà rendus par la session sœur à
réseau ouvert (`prep/etat-de-l-art-niveau3-pieces-v1`, `docs/sources/lecture-pdf-niveau3/`). Les lots encore en lecture
sont listés en section 7 ; la version finale `…-niveau3-v1.md` les intégrera. Complète les niveaux 1 et 2, qu'elle ne
remplace pas.

**Règles de lecture.** « Libre » veut dire « non trouvé dans les pièces lues », jamais « trou du champ » (R8). Tout
verdict « sur PDF » renvoie à un rapport scellé qui donne le PDF empreinté, la page et la citation exacte, contrôlée par
script (R7). Tout ce qui vient d'un moteur de recherche est une **piste non opposable** et est écrit comme tel. Aucune
hypothèse ni revendication n'est modifiée par ce document : les collisions sont des nœuds de Lazar.

Abréviations de renvoi : B1, B2, B3, C1 à C8, D1 à D3 = rapports sous `docs/etat-de-l-art/niveau3-v1/rapports/` ;
S-1, S-5A, S-5B, S-7A = rapports de la session sœur (`rapport-lot1-HC2-mirage-karne-v1.md`,
`rapport-lot5A-sequentiel-multi-agents-v1.md`, `rapport-lot5B-sondes-agents-diffus-v3-v1.md`,
`rapport-lot7A-sondes-agents-H1-H2-v1.md`), repris sans relecture des PDF par cette session.

## 1. Prononcés

1. **Deux collisions partielles sont constatées sur PDF. Ce sont des nœuds de Lazar.**
   - **Organisme d'idéation.** Qu, Chen, Wang, « Propose, Don't Judge », arXiv 2609.27051 v1 (22 septembre 2026 ;
     `docs/sources/pdf/anteriorite-P-041-v2/c8/2609.27051.pdf`, `2a8ded01…`), pièce déjà au dépôt et jamais lue par les
     notes d'antériorité. Elle occupe O1 dans son principe et en revendique la priorité (p. 2) ; deux des quatre
     composantes de O2 tel que N-064 l'a retenu, une troisième dans son principe (C4, contre-lu par C7). D'autres pièces
     du même dossier occupent dans leur principe O3, O10, O17, O19 et réduisent O11 à sa combinaison (C7).
   - **HC2.** MIRAGE, arXiv 2606.10304 v1, occupe en partie la robustesse d'une sonde sous attaque par le contenu
     (S-1 ; p. 1-2, 4, 7, 12, 18-20).
2. **Aucun autre énoncé revendiqué n'est trouvé occupé en entier** dans les pièces lues. La bascule « cœur séquentiel
   sur sondes publié à l'extérieur » n'est pas déclenchée (C1) ; la porte GC non plus (C3).
3. **Plusieurs zones sont plus occupées que ne le disait le niveau 2** : HC1 (trois régressions publiées, une loi
   linéaire empirique en cadre adverse), H1 (un voisin très proche du 8 octobre 2026), H7, H5, HC3, le lemme, H9.
4. **Le texte déjà envoyé au fonds contient deux erreurs de fait et une formulation contestable** (section 5).
5. **La traçabilité des documents du programme est faible dans leur texte** : sur 101 affirmations relevées dans le
   programme v2 et le texte envoyé, une seule porte une page (B1). Les PDF existent ; les renvois manquent.
6. **La partie A (hors archives ouvertes) n'a pas pu être faite par cette session**, privée de réseau ; elle est en
   cours chez la session sœur (section 7).

## 2. Verdict par revendication — papier A

| énoncé | verdict | par qui, où | phrase pour le jury |
|---|---|---|---|
| **H1** gain boîte blanche sur boîte noire, sabotage diffus | **occupée en partie** ; la mesure « diffus, tâches floues, agrégation égale » est libre dans les pièces lues | 2610.12445 « Caught in the Act » (FAR.AI, 8 oct. 2026), p. 7 : sondes contre moniteur de pointe sur sabotage d'agent, pas par pas ; le diffus est écarté du banc, p. 6, 19 (C5). 2512.07810, p. 3 ; 2606.17478 ; 2610.04575 (C1). 2610.17301 n'occupe pas H1 (S-7A) | « Le gain des sondes sur un moniteur de texte est publié pour du sabotage en un pas ; personne, dans ce que nous avons lu, ne le mesure quand le sabotage est étalé, et le banc le plus proche l'exclut par construction. » |
| **H2** accumulation séquentielle toujours valide de scores de sondes de l'agent | **occupée en partie** ; la conjonction de N-007 est libre dans les pièces lues | SafeDream 2604.16824, p. 4-5, 7 : somme de Page sur états cachés, sans garantie à tout instant, menace = l'utilisateur (C1). HELIOS v5 l'annonce p. 3, 18, 19, 26 sans la faire (C1). Boîte noire : E-valuator 2512.03109 ; CURA 2608.27808, p. 1, 3, 4, 16 : somme cumulée, fausse alarme certifiée, variante valable à tout instant, sur trajectoires d'agent, sans activations ni adversaire (C8) ; 2608.02464, p. 4, 5 (C8) ; 2606.20746 (S-5A) ; 2606.04141 (S-5B) | « Chaque morceau existe : la somme cumulée sur états internes, la garantie à tout instant en boîte noire. La conjonction sur les sondes de l'agent, contre un sabotage sous le seuil, n'est pas trouvée ; l'équipe de NARCBench l'annonce comme sa prochaine étape. » |
| **L** lemme d'additivité | **occupé en partie** | borne de puissance : 2608.02698, p. 5 ; critère toujours valide : 2208.07610, p. 2, 6 ; seuil sur épisodes entiers : 2512.03109, p. 4, 8 (C2). Prix de la garantie et coût du report : 2203.03532, p. 8 (C6). Borne de mélange portée sur PDF : 1810.08240, p. 9, 10, 28 ; dichotomie somme contre maximum : 1007.1434, p. 2-3, 6-7, 13 ; aucune des deux n'énonce « la puissance ne dépend que du budget total » (C8) | « Le cœur statistique est classique et cité. Notre apport est l'énoncé à budget total borné et sa mesure sur activations ; il est modeste sur le plan mathématique. » |
| **T** théorème négatif | **occupé en partie** | contraste marginale et corrélation, un agent, boîte noire : 2606.10456, p. 1-4, avec un adversaire adaptatif p. 6-7 ; moitié négative entre agents : 2607.11751, p. 3, 10 (C2). Parade publiée comme outil : 2212.07383 (C6). Voisin fort : 2605.11135, p. 7-9 (S-5A) | « Zhang et Gao l'ont posé avant nous pour un agent, en boîte noire. Ce qui nous sépare : la distinction entre préserver le multi-ensemble et préserver chaque marginale, l'écriture commune du temps et des agents, la mesure sur activations. » |
| **H6** marge asymétrique | libre dans les pièces lues ; rien de neuf depuis N-013 et N-015 | (C5, D1) | « Hypothèse non occupée dans nos lectures ; non prioritaire. » |
| **Tr** transposition jeton → action | libre dans les pièces lues | piste à lever : « What the Monitor Saw » (NeurIPS 2026 ; activations du moniteur, pas de l'agent ; D1, non opposable) | « Angle mort que nous avons nommé ; une pièce voisine reste à lire. » |
| **H8** la validité prédit la robustesse | **occupée en partie pour la prémisse** ; la prédiction est libre dans les pièces lues, sous réserve | 2610.17301 : « voisin fort », lecture dure « occupée en partie », p. 6, 37 (S-7A, **à trancher**) ; 2610.12445, p. 10 (C5) ; socle décrit aussi par 2609.10739, p. 1, 4, et 2607.13346, p. 1, 4, 7 (C8) ; piste 2611.10620 en lecture | « Que les sondes lisent la consigne plutôt que l'intention est maintenant décrit par plusieurs équipes ; prédire la robustesse à partir du construit mesuré ne l'est pas dans nos lectures. » |

## 3. Verdict par revendication — papier C

| énoncé | verdict | par qui, où | phrase pour le jury |
|---|---|---|---|
| **HC1** loi de déférence | **occupée en partie, plus qu'au niveau 2** | forme à destination imposée, loi linéaire ajustée sur six modèles en cadre adverse : 2603.15809, p. 15, 17 ; régressions sur intensités : 2602.13568, p. 3-5 (C3) ; 2608.25869, p. 7 (C5). 2607.08066 lue en entier : aucune loi (C3) | « Nous n'apportons ni la forme ni le phénomène. Nous apportons le test de la destination, par famille d'attaque, dans des moniteurs de contrôle, face à des sondes. » |
| **HC2** robustesse des sondes au contenu | **occupée en partie — collision, nœud** | MIRAGE 2606.10304, p. 1-2, 4, 7, 12, 18-20 (S-1) ; chiffres non opposables (dénominateur réel de 6, p. 20) | « MIRAGE publie une absence d'évasion par le contenu sur une sonde lue pendant la génération. Il reste : la sonde qui lit l'agent lui-même adversaire, le déplacement continu, la comparaison aux juges. » |
| **HC2b** trahison par les activations | libre dans les pièces lues | (S-1, C3) | — |
| **HC3** usurpation | **occupée en partie** | influence sans ordre : Panin, p. 8 ; 2509.16533, p. 7 (C3). Énoncé 1 : 2609.19587, p. 6-7, neutralisation et non détection (C5). Précédent : 2507.08794, p. 4, 7, 15 (S-5B) | « L'influence par le seul style est publiée sur des modèles qui répondent ; pas sur un juge moniteur imitant son instructeur. » |
| **HC4** taxe de déplacement | libre dans les pièces lues | rien de neuf depuis N-013 ; les trois coûts de l'état de l'art v1, l. 140, sont invérifiables au dépôt (B2) | « Prédiction à tester ; nous ne citons aucun coût tant qu'il n'est pas vérifié. » |
| **HC5** contre-mesures | **occupée en partie** | paraphrase par un vérificateur d'une autre famille : 2607.08066, p. 3, 6 (C3). Pistes à lever : 2610.29178, 2609.20211 (D2, en lecture) | « Les ingrédients existent séparément ; le quorum de juges et de sondes et sa matrice de transfert ne sont pas trouvés. » |
| **HC6** le g bénin prédit la robustesse | libre dans les pièces lues | piste à lever : 2608.12645 (D2, en lecture) ; contre-indice faible : 2507.08794, p. 7-9 (S-5B) | « Non trouvé ; une pièce voisine est en lecture. » |

## 4. Verdict par revendication — papier B, H9, organisme d'idéation

| énoncé | verdict | par qui, où | phrase pour le jury |
|---|---|---|---|
| **H3** courbe de sécurité selon le nombre d'agents | boîte noire **occupée** ; boîte blanche **occupée en partie** ; les deux courbes à budget constant libres dans les pièces lues | HELIOS v5, p. 27, 30 : 4 et 8 agents, boîte blanche seule (C1) ; piste 2610.24052 (D3, en lecture) | « La dégradation avec le nombre d'agents est publiée en boîte noire, et HELIOS montre que la boîte blanche se dégrade aussi de 4 à 8 agents. » |
| **Statistique de population** | coupe transversale **occupée** (HELIOS, R-622) ; squelette spatio-temporel **occupé en partie en boîte noire** | 2601.05427, p. 4, 5, 31 ; 2605.11135, p. 2-4 (S-5A) ; pistes 2611.02153 et 2611.10620 (D3, en lecture) | « Le squelette existe sur des signaux externes ; sur les états internes de copies à poids partagés, deux pièces de novembre 2026 sont en cours de lecture. » |
| **H4′** diversification contre coordination | libre dans les pièces lues ; peu cherché | (D3) | — |
| **H5** nombre × diversité des moniteurs | **occupée en partie** | 2608.16190, p. 1 : sur 24 juges, la décorrélation ne prédit pas le gain d'un ensemble (C5) | « Le résultat existe sur des juges ; pas sur un panel de sondes. » |
| **H7** riposte et fuite | **occupée en partie** | 2609.03035 ; 2610.26935, p. 1, signe contraire (C5) ; source du mécanisme : billet de Hopman et collègues, non versé (B2) | « L'effet de l'information rendue à l'attaquant est mesuré ; sa prédiction par l'information mutuelle ne l'est pas. » |
| **H9** survie d'une contrainte à la délégation | **occupée en partie** ; **verdict suspendu** | Cemri 2503.13657, p. 2, 7, 17 ; Hammond 2502.14143, p. 24, 42, 51 (C6) ; cinq pièces en lecture, dont MasDrift 2608.07556 (D3) | « La zone est plus occupée que nous ne l'avions écrit ; nous ne revendiquons rien avant la fin de la lecture. » |

**Organisme d'idéation (O1 à O20), après C4 et C7.** Références de page dans ces deux rapports.

| revendication | verdict |
|---|---|
| O1 qui propose ne juge pas | **occupée dans son principe** (Qu, Chen, Wang, p. 1, 2, 11) |
| O2 juge statistique hors des agents | **occupée en partie, plus largement que N-064** : deux composantes sur quatre, une dans son principe ; le nul des lois connues ne l'est pas |
| O3 prédictions scellées avant les données | occupée dans son principe (Qu et al. ; Masked Erosion 2610.38392, p. 4, 24) ; le tirage semé par l'empreinte non trouvé |
| O4 battre un nul des lois connues | **libre dans les pièces lues — verdict le plus fragile** (littérature de finance non au dépôt) |
| O5, O6, O15 | inchangées, non réexaminées |
| O7, O13, O14, O16, O18 | voisines |
| O8 proposeurs de plusieurs fournisseurs | libre dans les pièces lues |
| O9 mémoire sans verdicts | occupée dans son principe (Dwork et al. ; REUSE 2609.33180) |
| O10 témoins plantés | occupée dans son principe (PROCTOR 2609.02246, p. 2) |
| O11 banc de tricheurs | occupée dans son principe ; il reste la combinaison et l'ampleur |
| O12 attaque de Goodhart | occupée dans son principe ; la forme mesurée reste non trouvée |
| O17 scellement, aucun repli silencieux | occupée dans son principe (Masked Erosion ; SGM 2510.10232) |
| O19 puissance du juge | occupée dans son principe (REUSE, p. 6) |
| O20 juge éprouvé sur vérité plantée | occupée comme méthode (POPPER, p. 7 ; Qu et al., p. 1, 14, 15) |

Phrase pour le jury : « Séparer qui propose de qui juge, juger par e-valeurs avec contrôle de multiplicité, éprouver le
juge sur vérité plantée : tout cela est publié (POPPER 2025 ; Qu, Chen, Wang 2026). Ce que nous n'avons pas trouvé
ailleurs : un juge dont le nul est formé des lois connues, sur des hypothèses libres, mesuré sous l'attaque d'un
proposeur qui en lit la règle. »

## 5. Contre-résultats publiés défavorables, à dire nous-mêmes

1. **Le cadre de référence a écarté la surveillance.** Terekhov et al., 2606.08892, p. 2 : « monitoring and
   incrimination seem theoretically […] and empirically […] less promising for mitigating diffuse threats ». C'est une
   prémisse, pas une conclusion, et elle vise toute surveillance (B3). Le programme parie contre.
2. **Au seuil de la porte G1, des sondes sont à zéro.** 2606.17478, p. 30 : à 1 % de fausses alarmes sur le
   désalignement agentique, boîte noire 0,571, sonde linéaire 0,000 (C1).
3. **Les seuils ne tiennent pas.** 2610.04575, p. 1, 6, 7 : réglé pour 10 %, 18,67 % au test (C1).
4. **Le voisin le plus direct.** 2512.07810, p. 17-18 : sondes muettes sur un modèle dissimulateur agentique ; c'est de
   la sous-performance verrouillée par mot de passe, pas du sabotage ; contre-résultat partiel (les mêmes sondes
   réussissent sur l'autre modèle) ; sondes moyennées sur les jetons (B3, C1).
5. **L'accumulation n'est pas toujours utile.** 2607.02510, p. 1, 3 : un seuil unique calibré égale un test séquentiel
   et alerte plus tôt (C5).
6. **L'échelle.** 2610.12445, p. 8 : sondes à 0,585–0,781 sur un modèle de 2 milliards de paramètres ; le programme
   travaille à 8 milliards (C5).
7. **HELIOS.** p. 18 : rappel de 0,38 à 1 % de fausses alarmes sur le transfert (C1, R-622).
8. **HC1.** Panin, p. 6 : poids du conseil presque binaire dans trois modèles sur cinq ; une loi linéaire en moyenne
   peut n'être qu'un mélange « ignorer ou adopter » ; gain instable jusqu'au signe (C3).
9. **H7.** 2610.26935, p. 1 : après une riposte connue, le sabotage réussi tombe de 77 % à 12 % (C5).
10. **Un classifieur de mots égale la sonde** (S-7A ; 2607.13346, p. 4, 7 : 96,5 % contre 95,1 %, C8 ; piste 2610.40588 en lecture).
11. **L'accumulation pèse peu et les seuils ne se transportent pas, en boîte noire.** 2606.12476, p. 1, 2 : environ un quart du gain vient de l'accumulation ; CURA 2608.27808, p. 1, 7 : rappel de 42,3 % à α = 0,10, fausse alarme triplée sous un autre régime, base triviale de longueur non battue ; 2608.02464, p. 12 : la dérive lente échappe à tous les moniteurs par pas (C8).
12. **Une sonde parfaite en validation peut s'inverser.** 2609.10739, p. 1, 9 : aire de 0,006 sous tromperie (C8).

**Erreurs du texte envoyé au fonds (B1), à dire à l'entretien :**
- l. 199-200 et 261, « quorums across judge families (2605.15377) » : le PDF dit que tous les moniteurs emploient un
  seul modèle (p. 4) et que les familles différentes n'ont pas été essayées (p. 8).
- l. 131-132 : E-valuator n'est pas une accumulation additive.
- l. 87, « synthetic precursor (2606.10456) » : l'article imprime une validation sur traces réelles (p. 8). Mes lecteurs
  B1 et C2 divergent. **Lecture retenue par cette session** : dire « précurseur en boîte noire dont l'attaque est
  construite par simulation ; les auteurs rapportent une validation du modèle de menace sur des traces réelles ».
- l. 87-88, « its central statement does not hold for its own construction » : exact pour la somme (0,074 au point
  phare, 0,254 à 0,9, niveau 0,05, calcul en forme close de C2), faux pour le maximum. À restreindre.
- l. 264, « No claimed statement has been found fully occupied » : littéralement exact, plus un tableau fidèle.

**Corrections du socle de preuves v2 (B3)** : l. 73 (« less promising » n'est pas une conclusion) ; l. 76, 457-458, 539
(2512.07810 : sous-performance, p. 17 et 18, partiel) ; l. 68-69 (« échoue par construction » : ajouter la condition de
2606.10456, proposition 1, p. 3) ; l. 74, 77 (nommer E-valuator).

## 6. Traçabilité (partie B)

- **Programme v2 et texte envoyé** (B1) : 101 affirmations ; 78 tracées après ce passage, dont 4 contredites ; 13 sans
  source désignée (neuf au programme : l. 16, 93, 99, 104, 112, 137, 145, 197, 239).
- **État de l'art v1** (B2) : 60 références à identifiant arXiv, toutes empreintées et lues ; 28 sources sans
  identifiant, dont 24 sans PDF ; 4 venues introuvables au niveau 2, dont trois maintenant attestées par les actes et
  une corrigée (« ACL 2026 » est un atelier tenu avec ACL 2026 ; session sœur) ; 6 chiffres et une date invérifiables au
  dépôt (Meincke et collègues, l. 132 ; coûts de PAIR, GPTFuzzer, NOICE, l. 140 ; date du billet de l'institut
  britannique, l. 37) ; l. 154 contredite par le niveau 2 et jamais corrigée.
- **Socle v2** (B3) : 18 affirmations ; 10 confirmées, 5 avec réserve, 3 corrigées.

## 7. Ce qui reste non vérifié

1. **Lots en lecture à l'heure de cette version** : C9 de cette session (14 pièces neuves des papiers C et B ; C8 est rendu) ; chez la session sœur
   7-B (2611.02153, 2611.10620, 2610.24052), 7-C (2610.29178, 2608.12645, 2609.20211), 7-D (H9), 2-A et 2-B (billets de
   Hopman, de Gasteiger, de l'institut britannique, « The Case for White Box Control », Hebbar), 3-A, lots 8, 9, 10.
   **Tout verdict « libre » ci-dessus touché par une de ces pièces est suspendu** : statistique de population, H3, H8,
   H9, HC5, HC6, O4.
2. **Jamais lu** : codes de HELIOS, d'Orbit et de POPPER (une statistique séquentielle codée sans être dans le papier
   échapperait) ; affiche antérieure de 2607.08066 (non attestée) ; Harvey et Fischer 1997 ; littérature de finance sur
   les facteurs redondants (O4) ; listes arXiv du 1er au 10 novembre et soumissions ICLR 2027 (en cours chez la sœur).
3. **Étendue de lecture** : plusieurs lecteurs n'ont lu ligne à ligne que le corps des pièces ; annexes par mots-clés.
4. **Les rapports D1, D2, D3** sont des pistes de moteur ; une requête a été refusée par un classifieur de l'outil.
5. **H4′, H6, HC2b, HC4** : « libre » y repose sur peu de pièces et peu de requêtes.

## 8. Nœuds à porter à Lazar

1. Organisme d'idéation : resserrer O2 et O11 après Qu, Chen, Wang, et étendre les citations obligatoires de N-064
   (recommandation : oui, confiance 0,8).
2. HC2 après MIRAGE (constat de la session sœur).
3. HC1 : dire que la forme et la régression sont publiées ; ajouter 2603.15809, 2602.13568, 2608.25869 aux sources
   citées.
4. H2 : ajouter SafeDream aux motifs de N-007.
5. H9 : attendre la lecture des cinq pièces ; repli (b) de N-035 à examiner.
6. Texte envoyé : décider comment dire les erreurs de la section 5 à l'entretien.
