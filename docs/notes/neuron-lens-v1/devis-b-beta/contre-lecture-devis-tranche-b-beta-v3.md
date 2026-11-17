# Contre-lecture du devis de la tranche B-β (v3) — lecteur neuf (R2)

Pièce lue : `devis-tranche-b-beta-v3.md` (empreinte vérifiée : `77719c0c…`, conforme au compagnon). Lus aussi : v2 (`abc7b727…`) et sa contre-lecture,
`diff` v2 → v3, relevé `1a7cc32c…` (empreinte conforme), plans v1 et v2, journaux B-α v1 à v3, note `memoire-ablation-lot64-rtx4090-v1.md`,
`02_fit.py` (l. 1-10, 150-180, 213) et `neuron_lens/transport.py` (l. 45-58) et `data/summary/fit_bench_h100_2026-10-28.log` du dépôt voisin
(lecture seule). Rien exécuté du dépôt voisin, aucune commande du loueur, aucune variable d'environnement affichée, aucun fichier existant modifié.

**Verdict : à corriger.** Les 12 points de la v2 sont repris et l'arithmétique est exacte, mais trois défauts de fond restent : l'offre unique
n'est pas vérifiée sous le filtre neuf, le « pire cas sous l'arrêt dur » ne tient qu'à trafic nul (et pas avec le lieu (b) recommandé), la règle
« perte de machine = arrêt » est mal bornée. Aucune bloquante.

## (a) Reprise de la table du § 9, point par point
| point de la v2 | verdict |
|---|---|
| majeure 1 taille | **Corrigé quant au chiffre** : 63 ou 64 emplacements × 2 moitiés × 64 Mio = 7,9 et 8,0 Gio, ≈ 16 Gio (17,2 Go) ; moyennes seules ≈ 8 Gio pour les deux. Deux scories : m-D, m-E. |
| majeure 2 point de sauvegarde, perte de machine | **Corrigé en principe** (perte = arrêt, sauvegardes comptées, copie au lieu (b)) ; **règle incomplète** : voir Majeure 3 ; sauvegardes : m-A. |
| majeure 3 sortie des lentilles | **Corrigé en forme** (`inet_up>=200`, copie comptée à B6, règle « moins d'une heure ») ; **le filtre neuf n'a pas été rejoué** : Majeure 1 ; la règle n'a pas de défaut si la mère ne répond pas : m-F. |
| m-1 A100 80 Go | **Corrigé.** Relevé : 6 SXM4 80 Go (1,1043 à 1,973) + 1 PCIe 80 Go (1,461) ; sous 1,70 : cinq SXM4 + la PCIe = six sur sept. Juste. |
| m-2 lignes citées | **Corrigé** : `02_fit.py` l. 4-5 et 168-177 (la boucle va jusqu'à l. 180 : test de sauvegarde ; sans conséquence) ; `transport.py` l. 49-57 : `class Accumulator`, `sums`, `n_docs`. Juste. |
| m-3 1,5 à 2,3 h | **Corrigé** : B2 (1,0 à 1,5) + B4 (0,5 à 0,8) = 1,5 à 2,3. |
| m-4 lot 64 | **Corrigé** : condition retirée, source citée (la note, § 2, donne 23,53 GiB). Réserve : m-G. |
| m-5 « refusée » | **Corrigé** (§ 5 : « refusé par la minuterie… rien ne part »). |
| m-6 rappel après la minuterie | **Corrigé** : rappel 24,9 h < minuterie 25,7 h (prix exigé) ; aussi avant 28,5 h au prix lu. |
| m-7 recompilations | **Corrigé en forme** : tirage de documents d'au moins 128 jetons ; « mesuré au banc de B0 » ne tient pas : m-H. |
| m-8 options | **Corrigé** : une seule option, 2,38. |
| m-9 | « sans objet » : exact (la contre-lecture disait « rien à corriger »). |
| trafic, `-causal.pt` | **Corrigé** : 3,1 Go (1,04 × 3), 2,6 Go (2,9 × 32/36 = 2,58) ; scories : m-C. |

## (b) Recalculs (tous refaits)
- Taille : 32 × 4 × 64 Mio = 8,0 Gio par lentille ; 63 emplacements (R) = 7,875 Gio, 64 (S) = 8,0 ; total 15,9 Gio = 17,0 à 17,2 Go. Contrôle Qwen3-8B : 71 × 2 × 64 Mio = 9,53 Go ; 72 × 2 × 64 Mio = 9,66 Go : redonne bien 9,5 et 9,7 (mais voir m-D). Juste.
- B1 : 2 000 × 11,22 = 6,23 h ; 2 000 × 11,78 = 6,54 h ; × 0,9 = 5,61 ; × 1,2 = 7,85 ; 2 000 × 23,6 = 13,11 h. Juste. Banc : 11,36 s et 11,56 s (compilé, un document de 128 jetons).
- Heures attendues : bas 0,5 + 5,7 + 1,0 + 0,3 + 0,5 + 0,5 + 0,2 = **8,7** ; haut 1 + 8,2 + 1,5 + 0,5 + 0,8 + 0,8 + 0,4 = **13,2**. Pire : 3 + 13,4 + 2,5 + 1 + 1,5 + 1,5 + 1 + 1 = **24,9**. Écart au plan v2 : 24,9 − 21,2 = 3,7. Juste.
- Carte attendue : 8,7 × 2,145 = 18,7 ; 13,2 × 2,145 = 28,3 (« 19 à 28 ») ; avec 1,7 de trafic : 30,0 (« 19 à 30 »). Juste.
- Pire cas : 24,9 × 2,38 = 59,26 (« 59,3 ») ; + 1,8 = 61,06 (« 61,1 »), sous 61,2 d'une marge de **0,14 USD**. Seuil exact : (61,2 − 1,8) / 24,9 = 2,3855 : « 2,38 » juste.
- Minuterie : 61,2 / 2,38 × 3 600 = 92 571 s = 25,71 h ; 61,2 / 2,15 × 3 600 = 102 474 s ; 61,2 / 36 = 1,70. Juste.
- Copie : 17,2 Go = 137,6 Gbit : 11,5 min à 200 Mbit/s (« ≈ 11 min »), 45,9 min à 50 Mbit/s (« ≈ 45 min »), 57 min à 40 Mbit/s (« 1 h »). Juste.
- Prix avec stockage (200 Go, 730 h) : 2,1076 + 0,0364 = 2,144 ; 4,642 + 0,186 = 4,828 ; 4,843 + 0,182 = 5,025 ; 2,348 + 0,066 = 2,414. Juste. Offres A100 40 Go : 3 SXM4 + 4 PCIe = 7 ; plages de prix et de trafic de toutes les lignes du tableau du § 3 conformes au relevé.
- Perte de machine : 13 h × 2,145 = 27,9 (« ≈ 28 ») : exact **pour ce calcul**, mais ce n'est pas le maximum : Majeure 3.
- Trafic : 25 + 17 = 42 Go × 0,04 = 1,68 (écrit « 1,8 » ; « 0 à 1,7 » à la ligne attendue) : m-C.

## (c) Cohérence de la règle « perte de machine = arrêt »
Cohérente avec : § 2 point 6 (a) (lentilles et point de sauvegarde perdus), § 4 (retrait du pire cas, 24,9 h sans la ligne « machine perdue »), § 5 (ligne « perte de machine », « une seule instance »), § 7 (a) (inconvénient dit). Non cohérente ou incomplète sur trois points (Majeure 3) :
la borne « jusqu'à ≈ 28 USD », la fenêtre de perte qui ne se limite pas à B1, et le § 4 (b) (« reprise sur une nouvelle machine ») face au § 5 (« aucune relance sans mot de Lazar »).

## Bloquantes
Aucune.

## Majeures
**1. Le filtre neuf n'a pas été rejoué : « une seule offre au prix exigé » n'est pas établi** (v3 l. 61-66, 74-75, 123-124, 154-156 ; relevé en-tête et colonnes).
Écrit : relevé « filtre exact » sans débit montant ; carte exigée avec `inet_up>=200` ; « L'unique offre H100 SXM du jour (≈ 2,145 …) y tient ».
Le relevé n'a pas de colonne `inet_up` : on ne sait pas si l'offre 59816181 (Japon, 2,1076, fiabilité 0,9905) passe `inet_up>=200`. Si elle ne passe pas,
la course n'a **aucune** offre aujourd'hui (les deux autres H100 SXM sont à ≈ 4,8 et ≈ 5,0, au-dessus de 2,38) et le devis le présente comme faisable.
Devrait être écrit : soit un relevé refait avec le filtre complet (lecture seule de l'offre, par la mère ou Lazar ; je n'ai pas lancé `vastai`), soit « débit montant de l'offre du jour non relevé ; la condition peut
laisser zéro offre ». Même point : le « filtre exact » de la l. 61 n'est plus celui de la course. Conséquence en (a) : le § 7 (a) « inconvénient : une seule offre » est optimiste ; la condition `inet_up>=200` est inutile si le lieu retenu est (a) « aucun », ce que le texte ne distingue pas (m-E).

**2. « Pire cas entier sous l'arrêt dur » ne tient qu'à trafic nul, et pas avec le lieu (b) que la recommandation retient** (v3 l. 54-56, 108-109, 113-114, 122-124, 154-155, 161).
Écrit : pire cas 61,06 sous 61,2 au prix exigé 2,38, avec 1,8 USD de trafic (« ≈ 42 Go à 0,04 au plus »). Trois fragilités :
(i) la carte exigée borne le prix horaire, **pas le prix du trafic** : une offre H100 SXM à 2,30 USD/h et 0,10 USD/Go passerait la condition et casserait le pire cas ;
(ii) avec le lieu (b), le point de sauvegarde (≈ 8 Gio) est copié « à chaque sauvegarde » : 4 à 7 sauvegardes par lentille à 60 minutes, soit ≈ 70 à 130 Go sortants **en plus** des 17 Go, absents de la ligne « trafic » (sortant ≈ 17 Go) et du temps de B1 (≈ 6 min de débit par copie à 200 Mbit/s) ; à 0,04 USD/Go : + 3 à 5 USD, donc ≈ 64 à 66 USD > 61,2 ;
(iii) la marge est de 0,14 USD : toute somme non comptée (arrondi du prix exigé, trafic, copie) fait basculer vers la troncature que la v3 prétend avoir supprimée.
Devrait être écrit : exiger aussi « trafic ≤ 0,04 USD/Go » (ou « nul ») dans la carte exigée ; compter les copies du point de sauvegarde sous (b) (volume, temps, trafic) ; dire que « sans troncature » vaut à trafic nul et sans (b), ou donner le pire cas du couple (a)+(b).

**3. La règle « perte de machine = arrêt » est mal bornée** (v3 l. 105-109, 155-156, 161, 138).
Écrit : « une machine perdue pendant B1 perd jusqu'à ≈ 13 h (≈ 28 USD) » ; § 7 : « jusqu'à ≈ 28 USD sans résultat ». Défauts :
(i) ce n'est pas un maximum : 13 h est la durée de B1 seule au pire, au prix lu (2,145). Au prix exigé et avec B0 (3 h) : (3 + 13,4) × 2,38 = **39 USD** à la fin de B1 ; la perte est tout aussi sèche **après** B1 (B2 à B5, jusqu'à la copie, avec les options (a) et (c) : les lentilles finies, 8 à 17 Go, n'existent que sur la machine) : jusqu'à ≈ 23 h × 2,38 ≈ 55 USD de dépense perdue, sous l'arrêt dur mais hors des « 28 USD » dits à Lazar ;
(ii) la recommandation « (b) sinon (c) » laisse l'exposition entière sous (c) (aucune copie intermédiaire possible vers une machine de Lazar), sans le dire ;
(iii) § 4 (b) écrit « une reprise sur une nouvelle machine coûte au plus une heure de B1 » et « à chiffrer dans la commande », alors que le § 5 interdit toute relance sans mot de Lazar et que le plafond de 68 USD (ligne unique) ne couvre pas une seconde machine (B0 refait 3 h au pire, + 1 h) : la reprise est un nouveau devis, à dire, et non « à chiffrer dans la commande » ;
(iv) rien ne dit comment une perte est **détectée** (état de l'instance, délai, absence de poussée ?) ni si la destruction et le décompte de la dépense continuent après la perte (la minuterie et la garde tournent dans la session, pas sur la machine ; « course figée » exige deux contrôles de suite).
Devrait être écrit : borne haute chiffrée par étape (B1 : ≤ ≈ 39 USD ; B2 à copie : ≤ ≈ 55 USD à 2,38), dans le § 4 et le § 7 ; critère de détection ; renvoi à un nouveau devis pour toute reprise ; dire que (c) ne protège pas.

## Mineures
**m-A. Sauvegardes : compte et durée** (v3 l. 89-91, 96, 103). « ≈ 4 à 8 sauvegardes de ≈ 8 Gio par lentille » est ambigu (4 à 8 en tout ou par lentille ?). Le calcul : par lentille 2,8 à 4 h attendues → 3 à 4 sauvegardes périodiques + la finale = 4 à 5 ; au pire 6,5 h → 7 ; pour deux lentilles 8 à 10 attendues, jusqu'à ≈ 14 au pire. À 1-2 min : + 0,13 à 0,33 h attendu (écrit 0,1 à 0,3 : acceptable) mais pire cas ≈ 0,47 h (écrit 0,3 : B1 13,4 devrait être ≈ 13,6, total ≈ 25,1 h, soit 59,7 + 1,8 = 61,5 USD > 61,2). Durée de 1 à 2 min non mesurée (copie de ≈ 8 Gio du GPU vers l'hôte, écriture, `os.replace` ; `02_fit.py` l. 161-166) : dire « à mesurer à B0 ». Confirmer aussi que les deux lentilles s'ajustent l'une après l'autre (non écrit).

**m-B. Marge du pire cas et arrondis** : voir Majeure 2 (iii). Si la correction de m-A est prise, le pire cas dépasse l'arrêt dur d'environ 0,3 USD ; le prix exigé exact tombe à (61,2 − 1,8) / 25,1 = 2,366 (« 2,36 »).

**m-C. Trafic** (v3 l. 114, 122). « 1,8 USD (≈ 42 Go à 0,04) » : 42 × 0,04 = 1,68 ; la ligne attendue écrit « 0 à 1,7 ». Harmoniser (1,7 partout, ou 45 Go). Entrant « ≈ 25 Go » = 16 + 3,1 + 5 : le journal B-α v1 donne « ≈ 5 Go » pour une course de 7 minutes (environnement, tokeniseur, trois lentilles, configurations), qui **contient déjà** les ≈ 3,1 Go de lentilles : double compte (≈ 21 Go) ; sans conséquence (prudent), mais la phrase « le journal B-α v1 donne ≈ 5 Go en tout » laisse croire que ce total inclut Llama ; à écrire « hors poids ».

**m-D. Contrôle de la formule sur Qwen3-8B** (v3 l. 46-50). « 32 × 4 × 64 Mio » appliquée à Qwen3 (36 couches) donne 9,66 Go pour chacune, pas « 9,5 » pour R ; le contrôle ne tient qu'avec les emplacements réels (R : 71, S : 72, soit une couche de moins pour la cible « out » de R). À écrire : R 63 emplacements (7,9 Gio), S 64 (8,0 Gio), Qwen3 : 71 et 72 emplacements → 9,5 et 9,7 Go. De plus « ≈ 8 Gio par lentille … moyennes seules ≈ 8 Gio » : la seconde est pour **les deux** lentilles (≈ 4 Gio chacune) ; ajouter « pour les deux ». Mélange de Gio et de Go (« 8 à 17 Go » : 8 Gio = 8,6 Go).

**m-E. Pire cas du débit** (v3 l. 101). « pire cas à ≈ 40 Mbit/s » contredit le filtre `inet_up>=200` sans le dire (débit annoncé et débit réel) ; à écrire comme tel. Le poste « B6 copie » (0,2 à 0,4 h attendu) est compté aussi pour l'option (a) « aucun lieu », où il n'y a pas de copie.

**m-F. Règle de copie** (v3 l. 136). « s'il reste moins d'une heure …, la mère décide » : sans défaut si la mère ne répond pas ; au pire cas (copie à 22,9-23,9 h, minuterie 25,7 h) il reste 0,8 à 1,8 h : la règle se déclenche dans le pire cas lui-même. À écrire : défaut (copier tant que la minuterie n'a pas détruit ; ne rien détruire avant la fin de la copie si le crédit et l'arrêt dur le permettent, ou perdre), et que la destruction attend l'empreinte vérifiée au lieu d'arrivée. La contre-lecture de la v2 demandait cet ordre ; la v3 ne le tranche pas.

**m-G. Pic mémoire du lot 64** (v3 l. 26). « pic estimé ≈ 23,5 GiB » : la note dit « au mieux, sans aucune fragmentation », au point d'échec **à la couche 0** (l'échec a interrompu la mesure) ; c'est un minimum approximatif, non un pic. Le rapport 80/23,5 laisse la marge, mais l'écrire « au moins ≈ 23,5 GiB (note § 2) ».

**m-H. « Mesuré au banc de B0 »** (v3 l. 90-91 ; l. 19 : « banc d'un document par lentille »). Un banc d'un seul document ne mesure pas la part de documents courts ni les recompilations. Ce qui les évite est le filtre « au moins 128 jetons » du tirage de la liste (préalable 3, tokeniseur de Llama) : écrire que B0 **vérifie** que la liste ne contient que des documents de 128 jetons exacts. Le coefficient 0,9 à 1,2 est, lui, bien levé par un banc d'un document.

**m-I. Mise en forme** : l. 75, « Aucun repli** (comme en B-α) » : astérisques orphelins (la v2 écrivait « **Aucun repli** ») ; l. 3-6 : phrase d'en-tête qui enchaîne v3 = v2 puis « v2 = v1 » sans point, difficile à lire ; l. 8 : « ≈ 00:45 UTC » non mis à jour pour la v3 (relevé à 00:22:23Z, v3 postérieure) ; l. 56, le renvoi « (§ 4, perte de machine) » pointe un paragraphe qui ne chiffre pas la copie du point de sauvegarde (Majeure 2).

## Ce qui est sain (à ne pas perdre)
Les 3 majeures et 9 mineures de la v2 sont toutes reprises au fond ou en forme ; la suppression de la ligne « machine perdue » du pire cas est cohérente avec le § 5 ; les chiffres de taille et de durée sont exacts ; la table du § 9 renvoie aux bons paragraphes ; l'empreinte et le relevé joints sont conformes.
