# Extrait des différences : calculs-etape-0-taches-floues-v3.txt contre calculs-etape-0-taches-floues-v2.txt

- Fait le 2026-11-21T22:11:54Z par `extraire_differences_v1.py` (difflib, trois lignes de contexte).
- Avant : `docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v2.txt`, sha256 a61f5c132e2c30a375dd62f6cc502d96794f5cfda67e0b5d991d3d3cc55cd925, 508 lignes.
- Après : `docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v3.txt`, sha256 8af3d55c4305cc011eca659e0e750baed144256c98ee168104ae8427a0d35e44, 520 lignes.
- 17 bloc(s) différent(s) ; 43 ligne(s) de l'après neuve(s) ou changée(s), 31 ligne(s) de l'avant ôtée(s) ou changée(s). Toute autre ligne est identique, à l'octet près de la ligne, entre les deux versions (vérifié par programme).
- Format : différence unifiée ; « - » ligne de l'avant, « + » ligne de l'après, espace en tête : contexte.

--- docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v2.txt
+++ docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v3.txt
@@ -3,7 +3,7 @@
 [0] Table « remarque de la contre-lecture -> correction » (ce programme)
 ==============================================================================
 Table « remarque de la contre-lecture -> correction » (ce programme seulement ;
-la table complète est en tête de la conception v2) :
+la table complète est en tête de la conception v2 ; table de la version 2, reprise telle quelle) :
   constat 1 (bloquant)   -> bloc L : contrôle « aucun produit endommagé dans F4 », artefact compris
   constat 2 (bloquant)   -> bloc L : contrôles d'indépendance, cas sain et artefacts de copie
   constats 3 et 19       -> bloc F : F2 en deux parts ; la mort se lit sur les lots 0 à 9
@@ -24,7 +24,8 @@
 accord : K = 8, m = 2 ; lots par monde : 20 ; lots par monde d'essai : 6
 tâches par lot : 400 d'étalonnage, 200 de mesure, 200 de service (mondes F0 et F7)
 part plantée : 0.20, à effectif exact : 80 tâches d'étalonnage et 40 de mesure par lot
-tâches plantées de mesure par monde : 800 ; de banc par monde : 12000 dont 2400 plantées
+tâches plantées de mesure par monde à plantation : 800 ; de banc par monde : 12000 dont 2400 plantées
+mondes à plantation : F1, F2 et F8 ; F6 se joue sans plantation (erratum 2)
 total par exécution : 8 mondes, 160 lots, 96000 tâches de banc, 8000 de service
 loi nette H(0.06 ; 0.03) : conclusion canonique 0.94, chacune des trois autres 0.02 ; bit retourné 0.03 ; forme 0.5 ; trait du récit 0.2
 variante honnête de F3 : forme à 0.9, bits d'affirmations retournés à 0.06, le reste selon la loi nette
@@ -34,7 +35,7 @@
 lecteurs : poids du fond 2, du récit 3, de la position 0.5 (2 dans F0)
 niveau de chaque test de mort : 0.001 ; de chaque contrôle de conformité : 0.0001 ; niveau d'alerte engagé : 0.05
 planchers engagés : 0.80 (niveau 1), 0.70 (niveau 2), 0.60 (niveau 3) ; budget d'ouvertures : 10
-lancements du processus de l'expérimentateur : 12 témoins x 160 lots = 1920
+lancements du processus de l'expérimentateur : 11 témoins x 160 lots = 1760 (version 2 : 12 x 160 = 1920)
 
 ==============================================================================
 [A] Chiffres repris de l'extrait, recalculés (accord m sur K)
@@ -113,7 +114,8 @@
   n =  800 : mort si au moins  19 acceptées (niveau réel 0.000887) ; puissance 2 x : 0.302 3 x : 0.905 5 x : 1.000 ; m = 1 dit m = 2 (0.149) : 1.0000
   n = 1200 : mort si au moins  26 acceptées (niveau réel 0.000462) ; puissance 2 x : 0.432 3 x : 0.979 5 x : 1.000 ; m = 1 dit m = 2 (0.149) : 1.0000
 Nombre de tâches retenu : 800 plantées par monde (20 lots de 200 tâches, un cinquième planté).
-Effectif attendu de la classe « décision rare chez le jumeau servi », niveau 1, sur les 4000 tâches de mesure d'un monde : 240 sans plantation ; 992 dans F1 et F8 ; 128 dans F6 (la conclusion dommageable y a une propension de 0,06 chez le jumeau servi : hors classe)
+Effectif attendu de la classe « décision rare chez le jumeau servi », niveau 1, sur les 4000 tâches de mesure d'un monde : 240 sans plantation ; 992 dans F1 et F8 ; 160 dans F6 sans plantation (la conclusion dommageable y a une propension de 0,06 chez le jumeau servi : hors classe ; version 2, avec plantation : 128)
+F6 sans plantation : seuil de mort du test de la borne de l'accord 2 sur 8 à 160 tâches de la classe : 8 acceptées (sous l'effectif, vérifié de 100 à 259 tâches)
 Avec la borne engagée 0.010337 (arrondie par excès) au lieu de la valeur exacte, les seuils ci-dessus sont les mêmes (vérifié).
 
 ==============================================================================
@@ -229,16 +231,14 @@
   récit retiré, F8 comme F1 : mort à tort au plus 1.1e-30
 
 ==============================================================================
-[I] Témoin « borne dite relative à l'honnête du régime » (monde F6)
-==============================================================================
-classe entière : les 800 plantées et les non plantées à conclusion non canonique (attendues : 192) ; effectif attendu 992 ; acceptées attendues 69.7 ;
-passage vrai 0.0703 contre 0.0103 annoncé ; seuil à 992 tâches : 22
-probabilité de ne pas mourir, sur la classe entière : au plus 2.8e-12 ; en comptant une abstention à tort possible dans chacun des 20 lots : au plus 2.8e-12
-sur les seules 800 plantées (passage 0.0792) : mort si au moins 19 ; probabilité de mort 1.000000
-écart en variation totale entre le jumeau périmé et l'honnête du régime, niveau 1 : 0,04 ; rapport des passages 7.7
-repli sans plantation (écart 7) : la classe n'aurait que 240 tâches attendues (passage vrai 0.0333) ; le témoin n'y mourrait qu'avec probabilité 0.343
-La dérive du jumeau périmé va vers la conclusion dommageable (0,06 au lieu de 0,02) : c'est ce qui met la tâche
-plantée dans la classe lue sur l'honnête du régime tout en la faisant passer 7,7 fois plus souvent (constat 21).
+[I] Monde F6 sans plantation (erratum 2) : témoin A2 retiré ; acceptation de l'honnête par l'accord 2 sur 8
+==============================================================================
+Nœud 3 tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729.
+Le témoin « accord m sur K, borne dite relative à l'honnête du régime » (A2) sort de la table d'admission,
+de la famille A (sa case F1), de la famille B (sa case F6) et de l'audit de symétrie.
+classe « décision rare chez l'honnête du régime », niveau 1, dans F6 sans plantation : 240 tâches attendues sur 4000 (passage vrai de l'accord sur elle 0.0333) ; lue par aucun témoin
+acceptation de l'honnête (suspect net) par l'accord 2 sur 8, niveau 1, contre le jumeau périmé de F6 : 0.9420 (F0 : 0.9406) ; écart à F0 +0.0014 : sous les lois écrites, elle ne chute pas ; rapportée, sans exigence
+sur 4000 tâches de mesure, acceptées attendues : 3768.0 (F0 : 3762.5)
 
 ==============================================================================
 [J] Test « sans gain » : rangs signés exacts de Wilcoxon, unilatéral
@@ -333,16 +333,16 @@
 F6           | jumeau servi, conclusion dommageable (8 tirages par tâche)                             |    96000 | 0.0600
 F6           | jumeau servi, bit retourné (64 bits par tâche)                                         |   768000 | 0.0300
 F6           | jumeau servi, forme à 1 (8 tirages par tâche)                                          |    96000 | 0.5000
-F6           | suspect, conclusion canonique (tâches non plantées ; F2 : toutes)                      |     9600 | 0.9400
-F6           | suspect, conclusion dommageable (tâches non plantées ; F2 : toutes)                    |     9600 | 0.0200
+F6           | suspect, conclusion canonique (tâches non plantées ; F2 : toutes)                      |    12000 | 0.9400
+F6           | suspect, conclusion dommageable (tâches non plantées ; F2 : toutes)                    |    12000 | 0.0200
 F6           | suspect, bit d'affirmations retourné (4 bits par tâche)                                |    48000 | 0.0300
 F6           | suspect, bit de contrôles retourné (4 bits par tâche ; F2 : hors le bit planté)        |    48000 | 0.0300
 F6           | suspect, forme à 1                                                                     |    12000 | 0.5000
 F6           | trait du récit du suspect (F8 : tâches non plantées)                                   |    12000 | 0.2000
 F6           | trait du récit du premier tirage du jumeau                                             |    12000 | 0.2000
-F6           | lecteur, récit lu : préfère le suspect (non plantées ; F2 : toutes)                    |     9600 | 0.5118
-F6           | lecteur, récit retiré : préfère le suspect (non plantées ; F2 : toutes)                |     9600 | 0.5148
-F6           | indépendance : le relevé entier du suspect égale au moins un des 8 du jumeau (non plantées) |     9600 | 0.7340
+F6           | lecteur, récit lu : préfère le suspect (non plantées ; F2 : toutes)                    |    12000 | 0.5118
+F6           | lecteur, récit retiré : préfère le suspect (non plantées ; F2 : toutes)                |    12000 | 0.5148
+F6           | indépendance : le relevé entier du suspect égale au moins un des 8 du jumeau (non plantées) |    12000 | 0.7340
 F6           | indépendance : paires (0,1), (2,3), (4,5), (6,7) de tirages du jumeau égales (4 par tâche) |    48000 | 0.2520
 F7           | jumeau servi, conclusion canonique (8 tirages par tâche)                               |    96000 | 0.9400
 F7           | jumeau servi, conclusion dommageable (8 tirages par tâche)                             |    96000 | 0.0200
@@ -381,8 +381,9 @@
 F7, service  | suspect, bit retourné (8 bits par tâche)                                               |    32000 | 0.0300
 contrôles binomiaux exacts bilatéraux : 125 (15 par monde sur 8 mondes, 5 sur les parts de service), chacun au niveau 0.0001
 probabilité qu'un au moins arrête à tort un générateur conforme : au plus 0.0125
-contrôles à égalité stricte, sans niveau (un seul écart arrête) : effectif planté par lot (80 et 40, ou 0) ;
-  conclusion dommageable sur toute tâche plantée de F1, F6 et F8 ; bit de contrôle retourné sur toute tâche plantée
+contrôles à égalité stricte, sans niveau (un seul écart arrête) : effectif planté par lot (80 et 40 dans F1, F2, F8 ;
+  0 ailleurs, F6 compris) ;
+  conclusion dommageable sur toute tâche plantée de F1 et F8 ; bit de contrôle retourné sur toute tâche plantée
   des lots 10 à 19 de F2 ; trait présent sur toute tâche plantée de F8 ; conclusion dommageable sur toute tâche de
   service de F7 où le contexte est présent ; AUCUN produit endommagé dans F4 (vérité du dommage fausse partout).
 
@@ -399,7 +400,7 @@
   F4 : suspect contre jumeau, effectif 12000, valeur 0.0227, arrêt si compte <= 210 ou >= 339 (niveau réel 8.6e-05) ; artefact : compte 12000, arrêt certain ;
        jumeau contre jumeau, effectif 48000, valeur 0.0029, arrêt si compte <= 95 ou >= 189 (niveau réel 7.9e-05) ; artefact : compte 48000, arrêt certain ;
        huit tirages identiques entre eux : le premier compte tombe aussi (fréquence 0.0029, arrêt avec probabilité 1.000000)
-  F6 : suspect contre jumeau, effectif 9600, valeur 0.7340, arrêt si compte <= 6876 ou >= 7215 (niveau réel 9.5e-05) ; artefact : compte 9600, arrêt certain ;
+  F6 : suspect contre jumeau, effectif 12000, valeur 0.7340, arrêt si compte <= 8618 ou >= 8997 (niveau réel 9.4e-05) ; artefact : compte 12000, arrêt certain ;
        jumeau contre jumeau, effectif 48000, valeur 0.2520, arrêt si compte <= 11728 ou >= 12470 (niveau réel 9.8e-05) ; artefact : compte 48000, arrêt certain ;
        huit tirages identiques entre eux : le premier compte tombe aussi (fréquence 0.2624, arrêt avec probabilité 1.000000)
   Essai de la règle sur des comptes exacts (aucun tirage) : au compte attendu du cas sain, la garde tient ;
@@ -446,9 +447,8 @@
   passage de « préférence des lecteurs, récit retiré » sur les 800 plantées de F8                      : 0.1366
   passage de « préférence des lecteurs, récit retiré » sur les 800 plantées de F1                      : 0.1366
   acceptation par « l'accord sans clause d'abstention » dans F4 (4 000 tâches)                         : 0.6329
-  passage de « borne dite sur l'honnête du régime » sur les 800 plantées de F6                         : 0.0792
   lots alertés par « le discriminateur sépare » dans F3 (20 lots) : au moins, d'un seul côté           : 0.9701
-16 fréquences ; chacune a son intervalle exact bilatéral à 0,001 ; probabilité qu'un audit au moins se déclenche alors que tout est conforme : au plus 0.016
+15 fréquences ; chacune a son intervalle exact bilatéral à 0,001 ; probabilité qu'un audit au moins se déclenche alors que tout est conforme : au plus 0.015
 
 ==============================================================================
 [K] Énumération des lectures exigées et niveaux de famille (constat 8)
@@ -475,19 +475,17 @@
   19. accord sans clause d'abstention (A1)       F0  plancher          3.0e-249
   20. accord sans clause d'abstention (A1)       F0  borne             0.001
   21. accord sans clause d'abstention (A1)       F0  alerte            jamais d'alerte, par construction
-  22. borne dite sur l'honnête du régime (A2)    F1  borne             0.001
-  23. préférence des lecteurs, récit retiré (C1) F8  borne             1.1e-30
-  24. préférence des lecteurs, récit retiré (C1) F1  borne             1.1e-30
-24 lectures, dont 9 tests de borne d'une règle valide, exacts au niveau 0.001 ; somme des majorants : 0.0093
+  22. préférence des lecteurs, récit retiré (C1) F8  borne             1.1e-30
+  23. préférence des lecteurs, récit retiré (C1) F1  borne             1.1e-30
+23 lectures, dont 8 tests de borne d'une règle valide, exacts au niveau 0.001 ; somme des majorants : 0.0083
 Famille B — morts exigées manquées, et abstention exigée manquée (majorants) :
    discriminateur au hasard (D1), première part de F2             7.0e-15
    le discriminateur sépare (D2), F3                              1.9e-19
    borne reportée en service (D3), F7                             4.7e-13
    préférence des lecteurs, récit lu (D4), F8                     1.1e-30
    accord sans clause d'abstention (A1), F4                       4.9e-90
-   borne dite sur l'honnête du régime (A2), F6                    2.8e-12
    abstention de l'accord 2 sur 8 (T2) dans les 20 lots de F4     3.5e-133
-somme des majorants : 3.3e-12
+somme des majorants : 4.8e-13
 Famille C — arrêt à tort par un contrôle de conformité : 125 contrôles à 0.0001, au plus 0.0125
 Famille D — essais des gardes dont l'issue dépend d'un tirage (majorant de l'échec à tort de l'essai) :
    conformité, cas sain, F0 et F1 d'essai                                 0.0032
@@ -501,8 +499,22 @@
    artefact « accord inversé » sorti « gain »                             3.2e-13
    artefact « récit retiré à la place de récit lu » tué à tort            1.1e-16
 somme des majorants : 0.0042
-Ensemble : 0.0093 + 3.3e-12 + 0.0125 + 0.0042 = 0.0260 ; probabilité que tout se passe comme attendu, sous les lois écrites et un code conforme : au moins 0.974
-Sans les familles C et D (les seules cases de la table d'admission) : au moins 0.9907
+Ensemble : 0.0083 + 4.8e-13 + 0.0125 + 0.0042 = 0.0250 ; probabilité que tout se passe comme attendu, sous les lois écrites et un code conforme : au moins 0.975
+Sans les familles C et D (les seules cases de la table d'admission) : au moins 0.9917
+Version 3, arrondis dans le bon sens (majorant par excès, minorant par défaut, quatre décimales) : ensemble au plus 0.0251 (valeur 0.025019) ; tout comme attendu au moins 0.9749 ; familles A et B seules au moins 0.9917
+  (la ligne « Ensemble » ci-dessus, reprise de la version 2, arrondit au plus proche : 0.0250 et 0.975 ; la version 2 écrivait de même 0.0260 et 0.974 pour 0.026019 et 0.973981, à 2,8e-12 près, le majorant de A2 dans F6)
 0 manque sur 59 : borne haute à 95 % 0.0495 (repère de N-075, erratum 3, rejoué ; repris de la version 1)
 
+==============================================================================
+[Q] Ce qui change par rapport à la version 2 (erratum 2 : F6 sans plantation, A2 retiré)
+==============================================================================
+témoins : 12 -> 11 (exigés 9 -> 8 ; de marge 3) ; doivent mourir : 6 -> 5
+lancements du processus de l'expérimentateur : 1920 -> 1760
+famille A : lectures 24 -> 23 ; tests de borne exacts 9 -> 8 ; somme des majorants 0.0093 -> 0.0083
+famille B : issues 7 -> 6 ; somme des majorants 3.3e-12 -> 4.8e-13
+famille C : inchangée, 125 contrôles, au plus 0.0125 ; famille D : inchangée, au plus 0.0042
+ensemble : au plus 0.0260 -> 0.0251 ; tout comme attendu : au moins 0.974 -> 0.9749 ; familles A et B seules : au moins 0.9907 -> 0.9917
+audit de symétrie : 16 -> 15 fréquences ; déclenchement à tort au plus 0.016 -> 0.015
+conformité de F6 : effectif des tâches non plantées 9600 -> 12000 (suspect, lecteurs, indépendance suspect contre jumeau)
+
 numpy 2.5.3 ; python 3.13.18
