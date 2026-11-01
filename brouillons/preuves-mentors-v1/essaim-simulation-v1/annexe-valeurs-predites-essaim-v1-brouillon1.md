# Annexe — valeurs prédites de la simulation d'essaim (grille brouillon 1)

Calculées sans tirage par `controle_ia.simulation_essaim.calibrage` (fonctions citées), α = 0,05, q = 0,1, u = Φ⁻¹(0,9) = 1.281552. Valeurs à 4 décimales ; la lecture gelée les recalcule en double précision.

## A. Seuils exacts sous la loi de référence (`seuils_exacts`) et ρ* de `e_pas` (`rho_e_pas`)

Seuil (c, γ) : alarme si V > c, ou V = c et U < γ ; γ = 1 pour une statistique continue (alarme si V ≥ c).

| config | somme | max | comptage | agent_moyenne | agent_comptage | pas_moyenne | coelev_comptage | ρ* |
|---|---|---|---|---|---|---|---|---|
| e5x40 (K = 5, T = 40) | 23.2617 | 3.4739 | (27 ; 0.2762) | 2.3187 | (9 ; 0.4983) | 3.0158 | (3 ; 0.1165) | 0.18293 |
| e10x20 (K = 10, T = 20) | 23.2617 | 3.4739 | (27 ; 0.2762) | 2.5679 | (6 ; 0.3165) | 2.7992 | (4 ; 0.0914) | 0.18293 |
| e20x20 (K = 20, T = 20) | 32.8971 | 3.6557 | (50 ; 0.3863) | 2.7992 | (6 ; 0.0215) | 2.7992 | (6 ; 0.0215) | 0.12935 |
| e10x50 (K = 10, T = 50) | 36.7800 | 3.7126 | (61 ; 0.2300) | 2.5679 | (11 ; 0.3151) | 3.0828 | (5 ; 0.5991) | 0.11569 |

## B. HE4 — classe M, puissances exactes (`puissances_decalage(motif(...))`)

### e5x40 (K = 5, T = 40)

| menace | B | m | somme | max | comptage | agent_moyenne | agent_comptage | pas_moyenne | coelev_comptage |
|---|---|---|---|---|---|---|---|---|---|
| concentre | 3 | 1 | 0.0760 | 0.3517 | 0.0718 | 0.0715 | 0.0632 | 0.0935 | 0.0561 |
| concentre | 4 | 1 | 0.0866 | 0.7155 | 0.0728 | 0.0842 | 0.0638 | 0.1533 | 0.0564 |
| concentre | 5 | 1 | 0.0983 | 0.9397 | 0.0729 | 0.1009 | 0.0639 | 0.2559 | 0.0565 |
| synchro | 8 | 2 | 0.1403 | 0.9148 | 0.1033 | 0.1172 | 0.0774 | 0.7269 | 0.0955 |
| synchro | 8 | 3 | 0.1403 | 0.5308 | 0.1325 | 0.1028 | 0.0872 | 0.7269 | 0.2454 |
| synchro | 8 | 5 | 0.1403 | 0.1851 | 0.1455 | 0.0934 | 0.0896 | 0.7269 | 0.4402 |
| synchro | 12 | 2 | 0.2129 | 1.0000 | 0.1035 | 0.1888 | 0.0775 | 0.9911 | 0.0958 |
| synchro | 12 | 3 | 0.2129 | 0.9745 | 0.1428 | 0.1491 | 0.0907 | 0.9911 | 0.2949 |
| synchro | 12 | 5 | 0.2129 | 0.5562 | 0.2113 | 0.1245 | 0.1074 | 0.9911 | 0.8838 |
| temps | 8 | 2 | 0.1403 | 0.9148 | 0.1033 | 0.1803 | 0.0931 | 0.2454 | 0.0627 |
| temps | 8 | 20 | 0.1403 | 0.0651 | 0.1109 | 0.1803 | 0.1188 | 0.0688 | 0.0625 |
| temps | 8 | 40 | 0.1403 | 0.0604 | 0.1032 | 0.1803 | 0.1077 | 0.0663 | 0.0611 |
| temps | 12 | 2 | 0.2129 | 1.0000 | 0.1035 | 0.3634 | 0.0933 | 0.6217 | 0.0627 |
| temps | 12 | 20 | 0.2129 | 0.0831 | 0.1698 | 0.3634 | 0.2252 | 0.0822 | 0.0704 |
| temps | 12 | 40 | 0.2129 | 0.0687 | 0.1475 | 0.3634 | 0.1833 | 0.0761 | 0.0675 |

### e10x20 (K = 10, T = 20)

| menace | B | m | somme | max | comptage | agent_moyenne | agent_comptage | pas_moyenne | coelev_comptage |
|---|---|---|---|---|---|---|---|---|---|
| concentre | 3 | 1 | 0.0760 | 0.3517 | 0.0718 | 0.0727 | 0.0605 | 0.0782 | 0.0584 |
| concentre | 4 | 1 | 0.0866 | 0.7155 | 0.0728 | 0.0901 | 0.0610 | 0.1071 | 0.0587 |
| concentre | 5 | 1 | 0.0983 | 0.9397 | 0.0729 | 0.1153 | 0.0610 | 0.1539 | 0.0588 |
| synchro | 8 | 2 | 0.1403 | 0.9148 | 0.1033 | 0.1285 | 0.0717 | 0.4226 | 0.0943 |
| synchro | 8 | 5 | 0.1403 | 0.1851 | 0.1455 | 0.0896 | 0.0814 | 0.4226 | 0.2996 |
| synchro | 8 | 10 | 0.1403 | 0.0827 | 0.1265 | 0.0813 | 0.0758 | 0.4226 | 0.2318 |
| synchro | 12 | 2 | 0.2129 | 1.0000 | 0.1035 | 0.2398 | 0.0718 | 0.8479 | 0.0946 |
| synchro | 12 | 5 | 0.2129 | 0.5562 | 0.2113 | 0.1240 | 0.0956 | 0.8479 | 0.6912 |
| synchro | 12 | 10 | 0.2129 | 0.1515 | 0.2096 | 0.1023 | 0.0935 | 0.8479 | 0.5792 |
| temps | 8 | 2 | 0.1403 | 0.9148 | 0.1033 | 0.2533 | 0.0919 | 0.1607 | 0.0673 |
| temps | 8 | 10 | 0.1403 | 0.0827 | 0.1265 | 0.2533 | 0.1689 | 0.0771 | 0.0706 |
| temps | 8 | 20 | 0.1403 | 0.0651 | 0.1109 | 0.2533 | 0.1363 | 0.0726 | 0.0671 |
| temps | 12 | 2 | 0.2129 | 1.0000 | 0.1035 | 0.5664 | 0.0921 | 0.3635 | 0.0674 |
| temps | 12 | 10 | 0.2129 | 0.1515 | 0.2096 | 0.5664 | 0.4105 | 0.0984 | 0.0847 |
| temps | 12 | 20 | 0.2129 | 0.0831 | 0.1698 | 0.5664 | 0.2907 | 0.0869 | 0.0780 |

### e20x20 (K = 20, T = 20)

| menace | B | m | somme | max | comptage | agent_moyenne | agent_comptage | pas_moyenne | coelev_comptage |
|---|---|---|---|---|---|---|---|---|---|
| concentre | 3 | 1 | 0.0675 | 0.2931 | 0.0652 | 0.0634 | 0.0559 | 0.0634 | 0.0559 |
| concentre | 4 | 1 | 0.0742 | 0.6529 | 0.0659 | 0.0746 | 0.0562 | 0.0746 | 0.0562 |
| concentre | 5 | 1 | 0.0815 | 0.9150 | 0.0660 | 0.0917 | 0.0562 | 0.0917 | 0.0562 |
| synchro | 8 | 2 | 0.1066 | 0.8732 | 0.0857 | 0.0986 | 0.0623 | 0.1963 | 0.0755 |
| synchro | 8 | 10 | 0.1066 | 0.0690 | 0.0989 | 0.0673 | 0.0647 | 0.1963 | 0.1387 |
| synchro | 8 | 20 | 0.1066 | 0.0583 | 0.0893 | 0.0652 | 0.0622 | 0.1963 | 0.1133 |
| synchro | 12 | 2 | 0.1480 | 0.9999 | 0.0858 | 0.1785 | 0.0624 | 0.4798 | 0.0756 |
| synchro | 12 | 10 | 0.1480 | 0.1136 | 0.1478 | 0.0794 | 0.0750 | 0.4798 | 0.3561 |
| synchro | 12 | 20 | 0.1480 | 0.0687 | 0.1245 | 0.0742 | 0.0702 | 0.4798 | 0.2478 |
| temps | 8 | 2 | 0.1066 | 0.8732 | 0.0857 | 0.1963 | 0.0755 | 0.0986 | 0.0623 |
| temps | 8 | 10 | 0.1066 | 0.0690 | 0.0989 | 0.1963 | 0.1387 | 0.0673 | 0.0647 |
| temps | 8 | 20 | 0.1066 | 0.0583 | 0.0893 | 0.1963 | 0.1133 | 0.0652 | 0.0622 |
| temps | 12 | 2 | 0.1480 | 0.9999 | 0.0858 | 0.4798 | 0.0756 | 0.1785 | 0.0624 |
| temps | 12 | 10 | 0.1480 | 0.1136 | 0.1478 | 0.4798 | 0.3561 | 0.0794 | 0.0750 |
| temps | 12 | 20 | 0.1480 | 0.0687 | 0.1245 | 0.4798 | 0.2478 | 0.0742 | 0.0702 |

## C. HE2.3 — bornes inférieures exactes sous synchronisation (r = 1)

Co-élévation (comptage) : `borne_synchro`. Moyenne par pas (m = K) : (1 − Φ(c_T/√K)^T)^K. Co-élévation continue (m = K) : P(Bin(K, 1 − Φ(c₃/3)^T) ≥ 3), c₃ = seuil Monte-Carlo du run (non connu avant le run).

| config | m | borne coelev_comptage | borne pas_moyenne (m = K) | au-dessus prédit (règle) |
|---|---|---|---|---|
| e5x40 | 2 | 0.0548 | — | — |
| e5x40 | 3 | 0.2732 | — | coelev_comptage, pas_moyenne, coelev_somme3 |
| e5x40 | 5 | 0.9981 | 0.8841 | coelev_comptage, pas_moyenne, coelev_somme3 |
| e10x20 | 2 | 0.0416 | — | — |
| e10x20 | 5 | 0.7021 | — | coelev_comptage, pas_moyenne, coelev_somme3 |
| e10x20 | 10 | 0.9996 | 0.8552 | coelev_comptage, pas_moyenne, coelev_somme3 |
| e20x20 | 2 | 0.0244 | — | — |
| e20x20 | 10 | 0.9899 | — | coelev_comptage, pas_moyenne, coelev_somme3 |
| e20x20 | 20 | 1.0000 | 0.9592 | coelev_comptage, pas_moyenne, coelev_somme3 |

## D. HE3.6 — taux de fausses alarmes exacts des seuils de référence hors hypothèses (`fausses_alarmes_reference`)

Seuils calibrés sous cases iid N(0, 1) (« cases supposées indépendantes »), appliqués sous la loi indiquée. α = 0,05.

| config | loi | somme | max | comptage | agent_moyenne | agent_comptage | pas_moyenne | coelev_comptage |
|---|---|---|---|---|---|---|---|---|
| e10x20 | tau0.1 | 0.1707 | 0.0498 | 0.1011 | 0.0830 | 0.0633 | 0.0683 | 0.0582 |
| e10x20 | tau0.2 | 0.2913 | 0.0491 | 0.1813 | 0.1588 | 0.0990 | 0.1178 | 0.0824 |
| e10x20 | c0.2 | 0.1628 | 0.0495 | 0.1031 | 0.0468 | — | 0.6196 | 0.3530 |
| e10x20 | c0.4 | 0.2216 | 0.0471 | 0.1497 | 0.0409 | — | 0.8669 | 0.6222 |
| e10x50 | tau0.1 | 0.2508 | 0.0498 | 0.1538 | 0.1293 | 0.0828 | 0.0721 | 0.0609 |
| e10x50 | tau0.2 | 0.3597 | 0.0490 | 0.2496 | 0.2430 | 0.1516 | 0.1296 | 0.0907 |
| e10x50 | c0.2 | 0.1628 | 0.0497 | 0.1039 | 0.0468 | — | 0.8104 | 0.4926 |
| e10x50 | c0.4 | 0.2216 | 0.0480 | 0.1522 | 0.0409 | — | 0.9801 | 0.8256 |

## E. HE3.5 — région d'acceptation exacte du calibrage conforme (`region_conforme`)

K = 1 000 essaims honnêtes entiers, L = 50 tirages, 400 essais chacun : taux théorique 1 − 951/1001 = 0.04995. Nombre total d'alarmes accepté sur 20000 essais au niveau 1 − 10⁻⁵ : [843 ; 1165] (taux [0.0421 ; 0.0583]).

