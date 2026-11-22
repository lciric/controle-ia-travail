# Devis à coût réduit — essaim qui communique — v1

- Cette pièce répond au mot du directeur GO-2026-11-22-26 : « il faut réduire drastiquement les coûts ».
- **Aucune dépense, aucun appel de modèle, aucun réseau.**
- Le calcul se rejoue par `calcul_devis_cout_reduit_v1.py`, qui écrit `calcul-devis-cout-reduit-v1.json`. Il importe `calcul_devis_essaim_v2.py` et `calcul_pilote_essaim_v1.py`.
- Tout nombre sans pièce est marqué **HYPOTHÈSE** ou **PROPOSITION**, dans ce texte comme dans la sortie.
- La pièce sera relue par Fable avant toute dépense.

**Verdict d'abord.**
- **Le levier qui donne un à deux ordres de grandeur est (d)** : faire d'abord le pilote P-std (`pilote-instrument-essaim-v1.md`), et non le programme. Sur Kimi, le pilote coûte **57 à 102 USD** à l'estimation, **204 USD** au vrai pire, contre 2 809 USD pour l'estimation du programme sur la même espèce : un facteur 28 à 49. Par rapport à l'estimation du programme sur la première espèce Claude (4 669 USD), le facteur est de 46 à 82.
- Sur le programme, les autres leviers ne donnent chacun qu'un facteur de 1,1 à 2,5, parce que les tests de mort y dominent ; combinés, environ 3 à 5.
- **Combinaison recommandée pour le pilote** : P-std, Kimi par interface, aucun test de mort, aucun aiguilleur, plafond de sortie de 24 000 jetons. Estimation **57 à 102 USD**, vrai pire **204 USD**. Si une remise par lots existe chez Kimi (non vérifiée), l'estimation tombe à environ 51 USD.

## 1. Leviers, un à un, sur le programme (cas attendu de la v2 ; estimation, relances de 10 % comprises ; USD)

Références v2 : Kimi 2 809 ; première espèce Claude 4 669 ; Fable 8 389 ; seconde espèce Claude 10 249.

### (a) Proposeurs sur un modèle ouvert, servi sur une carte louée (A100 à 1,4 USD/h)

**Hypothèses**, aucune pièce lue ne donnant de débit :
- débit agrégé par vLLM : 400 jetons de sortie et 4 000 jetons d'entrée par seconde à l'estimation ; 100 et 1 000 au pire ;
- utilisation de la carte : 50 % à l'estimation, 25 % au pire, car les générations sont séquentielles et la carte attend le noyau ;
- mise en route : 10 heures sur le programme à l'estimation, 30 au pire.

**Modèle ouvert** : aucune pièce lue pour cette tâche n'en nomme un pour l'organisme. **Le choix revient au directeur.**

| variante | Kimi | première espèce Claude | Fable | seconde espèce Claude | heures de carte |
|---|---|---|---|---|---|
| proposeurs et messages sur le modèle ouvert ; aiguilleur et tests restent sur l'interface | 2 450 (×1,1) | 3 859 (×1,2) | 6 678 (×1,3) | 8 087 (×1,3) | 60 ; pire 426 |
| tout sur le modèle ouvert, sauf le vérificateur, qui reste sur Argon (autre famille, 0,06 USD par test) | 1 250 (×2,2) | 1 250 (×3,7) | 1 250 (×6,7) | 1 250 (×8,2) | 196 ; pire 1 516 |
| pire de la variante « tout » | 3 283 | 3 283 | 3 283 | 3 283 | |

Ce que cela coûte en validité :
- **Comparabilité perdue avec les espèces de frontière** : le résultat ne vaut que pour ce modèle ouvert. Un modèle faible peut ne pas battre B3 pour une raison qui n'a rien à voir avec la communication.
- N-058 n'est pas touchée : la composition reste jugée sur l'oracle et le coût.
- Faire tenir l'expérimentateur des tests de mort par le même modèle ouvert que les proposeurs mêle les rôles. Il faut le dire, ou le garder sur l'interface.
- Le vérificateur, qui doit être d'une autre famille, reste sur Argon : 862 USD sur le programme, soit la plus grosse part du reste.

### (b) Traitement par lots et cache des invites

- **Remise par lots** : **remise rapportée, non vérifiée**. Aucune pièce de tarifs lue ne porte sa valeur. Le calcul v2 (`91f5cf8f…`) mentionne pour Carbon une « commande par lot », avec la mention « remise du lot non comptée » : la remise existe, sa valeur n'est pas écrite. Chiffrée à 50 % : de 1 879 à 5 599 USD (×1,5 à ×1,8). Sans elle : la référence.
- **Cache** : seul le tarif de Fable a une pièce (`relecture_fable_api_v3.py`, `95bea064…`) : lecture du cache 0,20 USD par million de jetons, contre 8,00 pour l'entrée, et facteur d'écriture de 2,0. Avec 2/3 de l'entrée en cache (**HYPOTHÈSE** : consigne et case communes aux appels d'un monde), Fable passe de 8 389 à 6 367 USD (×1,3) ; l'écriture du premier appel n'est pas comptée. Pour les autres espèces, le tarif de cache n'est pas établi.
- **Ce que les lots changent aux générations** : une génération ne part qu'à la fin de la précédente (archive). Chaque génération est donc **un lot**, et le programme compte au moins trois lots successifs, soit plusieurs jours (délai de traitement rapporté, non vérifié). Tous les mondes et tous les bras d'une génération tiennent dans un même lot ; la règle de C.4, qui fait tourner les trois bras dans la même fenêtre, reste tenue si les bras partagent chaque lot.

### (c) Tests de mort et objets de contrôle échantillonnés (PROPOSITION : 20 %)

Sur le programme : de 1 139 à 4 937 USD (×2,1 à ×2,5).

Puissance qui reste : la probabilité de voir au moins un défaut, quand une part q des tests échoue, avec m tests tirés, vaut 1 − (1 − q)^m.

| q | m = 3 | m = 6 | m = 12 | m = 36 |
|---|---|---|---|---|
| 0,05 | 0,14 | 0,27 | 0,46 | 0,84 |
| 0,10 | 0,27 | 0,47 | 0,72 | 0,98 |
| 0,20 | 0,49 | 0,74 | 0,93 | 1,00 |

À 20 %, un monde porte environ 12 tests d'objets de contrôle (3 générations × 2 jeux × 10 × 0,2). Un défaut de chaîne de 10 % se voit avec une probabilité de 0,72 par monde ; sur 32 mondes, presque sûrement. Mais **un témoin manqué isolé passe souvent inaperçu**. L'invalidation par monde de C.7 devient probabiliste : c'est une perte de validité à écrire au préenregistrement. **Dans le pilote, ce levier est sans objet** : on n'y fait aucun test de mort.

### (d) Moins de mondes et de générations : le pilote d'abord

Voir `pilote-instrument-essaim-v1.md`. P-std (12 mondes, (a) et (c), 3 générations) coûte 57 à 102 USD sur Kimi et 115 à 204 USD sur la première espèce Claude, soit un facteur de 23 à 49 par rapport au programme de même espèce. Sa validité : il ne répond qu'à une question, « (a) bat-il B3 ? » ; il ne dit rien des estimandes (a) − (b) et (a) − (c), au-delà d'une lecture descriptive ; sa puissance est d'environ 0,8 à 0,94 pour un gain d'une composante par monde. C'est une **porte**, non une réponse.

### (e) Sorties plus courtes

- **Consigne « deux cartes, sans raisonnement affiché »** (**HYPOTHÈSE** : sortie divisée par deux) : ×1,1 sur le programme, que dominent les tests ; ×1,8 environ sur le pilote (102 → 57 USD sur Kimi, d'une sortie de 12 800 à une sortie de 6 000).
- **Plafond de sortie** : il ne réduit pas l'estimation, seulement le **pire**. Pilote Kimi : 204 USD à 24 000 jetons, 93 USD à 8 000.
- **Risque** : à 8 000 jetons, un appel de Kimi tel que mesuré en v67 (environ 12 800 jetons pour deux cartes) serait **tronqué**. La seconde carte, ou les deux, serait perdue ou malformée, comptée « rien », et la couverture de l'essaim serait biaisée vers le bas contre B3. À 24 000 jetons, la marge est d'environ 1,9. Les troncatures sont à compter et rapporter par bras. Un taux de troncature au-delà d'un seuil à geler, par exemple 5 % des appels, invalide le pilote.

## 2. Combinaisons

| combinaison | Kimi | première espèce Claude | statut |
|---|---|---|---|
| programme : (b) avec remise + (c) + (e) | 582 (×4,8) | 974 (×4,8) | remise non vérifiée |
| programme : (c) + (e), sans remise | 974 (×2,9) | 1 758 (×2,7) | tarifs à pièce |
| programme : (a) tout sur modèle ouvert | 1 250 ; pire 3 283 | idem | débit hypothétique |
| **pilote P-std, interface, sortie 6 000 / 12 800** | **57 / 102 ; pire 204** | 115 / 204 ; pire 408 | **recommandé** |
| pilote P-std, interface, remise par lots | ≈ 51 (sortie 12 800) | ≈ 102 | remise non vérifiée |
| pilote P-std, modèle ouvert sur A100 | 25 ; pire 347 (16,5 h ; pire 214 h) | — | débit hypothétique ; modèle à choisir |

Le pire du pilote sur modèle ouvert (347 USD) dépasse celui de l'interface pour Kimi (204 USD), car un débit inconnu ne se borne pas. Sur l'interface, au contraire, le plafond de jetons borne chaque appel.

## 3. Table de décision

| levier | facteur (estimation) | coût en validité | recommandation |
|---|---|---|---|
| (a) modèle ouvert sur A100 | programme ×1,1 à ×1,3 (proposeurs seuls), ×2,2 à ×8,2 (tout) ; pilote 102 → 25 sur Kimi | aucune comparabilité avec la frontière ; débit et mise en route hypothétiques ; pire non borné par l'interface ; modèle à choisir par le directeur | **à garder en réserve** : seconde espèce bon marché du pilote, si le directeur choisit un modèle et si un débit est mesuré une fois |
| (b) lots, remise | ×1,5 à ×1,8 | aucune sur la mesure ; une génération par lot, plusieurs jours ; **remise non vérifiée** | **oui si une pièce de tarifs la porte** ; sinon devis sans elle |
| (b) cache | ×1,3 (Fable seulement) | aucune | oui, là où le tarif existe |
| (c) tests échantillonnés à 20 % | ×2,1 à ×2,5 (programme) | témoin isolé souvent manqué ; invalidation probabiliste | **oui pour le programme**, avec un taux préenregistré ; sans objet au pilote |
| (d) pilote d'abord | **×23 à ×49** (même espèce) | une seule question ; puissance limitée à un gain d'environ une composante par monde | **oui, en premier** |
| (e) sorties courtes, plafond | estimation ×1,1 à ×1,8 ; pire ×2,2 (24 000 → 8 000) | troncature des cartes au plafond court | **24 000 jetons** au pilote, troncatures rapportées ; refuser 8 000 sur Kimi |

**Recommandation** :
- pilote **P-std sur Kimi par interface**, sans test de mort ni aiguilleur, plafond de 24 000 jetons de sortie ;
- **estimation 57 à 102 USD, vrai pire 204 USD** ;
- (c) et (b) n'entrent qu'au programme, et seulement si le pilote passe la porte ;
- (a) seulement comme seconde espèce, sur choix du directeur.
