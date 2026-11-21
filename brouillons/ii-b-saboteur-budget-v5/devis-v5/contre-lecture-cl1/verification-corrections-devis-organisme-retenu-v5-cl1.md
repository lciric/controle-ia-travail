# Vérification des corrections du devis de l'organisme retenu (v5) — contre-lecteur 1

Écrite le 2026-11-21 par le contre-lecteur 1 (Claude Opus 5.5, côté saboteur), sous le même mandat (35860e22e161…). Pièces : `devis-ii-b-v5-brouillon2.md` (e58aa6f0…), `calcul-devis-ii-b-v6.py` (bfe997b1…), `sortie-calcul-devis-ii-b-v6.txt` (228a308d…), `differences-devis-brouillon1-vers-2-v1.md` ; compagnons vérifiés. La copie versée de ma contre-lecture (cfea7cda…) est identique à la mienne.

## Verdict : remettable en l'état, avec deux précisions facultatives

Mes trois majeurs et mes neuf mineurs sont traités. Le script rejoué rend sa sortie à l'octet (`rejeu-v6.txt`). Les durées, les prix et les comptes d'appels sont ceux du calcul v5 (j'ai lu le diff entre les deux scripts : seuls des ajouts, la réserve passée à 10 et la ligne des 6 tours retirée). Il reste deux précisions facultatives (P1, P2), qui ne bloquent pas la remise.

## Remarques traitées

| remarque | traitée ? | contrôle |
|---|---|---|
| M1 dépassement du plafond de tours | oui | le § 6 suit 10.3 (étape 6) et 5.1 à la lettre : [N] passe à [P], [P] mène à « ne part pas », second passage refusé, aucun tour ajouté |
| M2 réserve mince | oui | fichier d'entrées à 45, tolérance chiffrée ; 73 tours, 29 %, k_R ≥ 6 [L41] : mes chiffres retrouvés ; 50 écarté avec sa raison [L44] [L48] |
| M3 pire de la ligne | oui | 59,76 en tête du § 0 ; 53,4 dit « pire d'une course de 24 tours » [L52] |
| m1 six tours | oui | ligne retirée ; au moins 12 tours, au plus le plafond [L51] |
| m2 coût fixe en nombre | oui | 6,33, 7,89, 12,29 et 6,90 [L37] à [L40] ; 6,90 = 3,55 h × 1,38 + 2,00, juste |
| m3 durée de l'oracle | oui | la plus longue des deux durées, renvoyée à l'ordre neuf |
| m4 lecture des marques | oui | [L05] : 543 s et 0,186 s, épisode inchangé |
| m5 coupure de l'étalonnage | oui | règle de la surveillance, pas de code neuf dans la minuterie ; voir P2 |
| m6 échéance | oui | 30 novembre ; voir P1 |
| m7, m8, m9 | oui | commentaires du script ; GO-2026-11-21-66 cité d'après ma lecture |

## Le point neuf du rédacteur : prix scellé à la borne (1,38) et coût fixe de 6,90, ou prix réel écrit à la création

J'ai recalculé : avec le fichier d'entrées à 45, le prix scellé à 1,38 et le coût fixe à 6,90, la course peut aller jusqu'à 63 tours. Si l'offre louée est au prix réel de 1,22, la dépense planifiée est de 40,1 dollars et les tours peuvent être 49 % plus lents que mesuré avant la coupure. Si l'offre louée est à la borne de 1,38, la dépense planifiée est de 45,1 dollars et la tolérance tombe à **29 %**, la même que celle de l'option au prix réel (73 tours). Ce dernier calcul est le mien ; il n'est pas dans la sortie.

**Recommandation : sceller le prix à la borne 1,38 et le coût fixe à 6,90 (63 tours), confiance moyenne.** Trois raisons :
1. La tolérance la plus basse de cette option (29 %, offre à la borne) vaut celle de l'option au prix réel. Elle n'est donc jamais moins sûre.
2. Le fichier d'entrées se scelle avant toute location. Il n'y a pas d'écriture à faire sur la machine après la création, alors qu'un fichier absent mène à l'issue « non calculable » (10.3, étape 1).
3. Le coût est de dix tours au plus et d'un épisode régénéré accepté de plus pour partir (k_R ≥ 7 au lieu de 6).

Les deux options sont conformes à 10.2. La « dépense de l'étalonnage » y est la dépense relevée au prix réel, ce que fait [L49].

## Marge de l'échéance

Le calcul est juste. Une création à 2026-11-28T23:00Z atteint la coupure au plus tard le 30 à 18:26Z au prix réel (43,4 h de carte), 3,6 h avant la minuterie de 22:00Z. La consignation (40 minutes au plus) tient dans cette marge [L53] [L54].

**P1, précision facultative.** « Moins de 48 h d'arrêt » sous-dit le cas. Entre la coupure et la fin de la ligne (2026-12-01T00:00Z), il ne reste que **5,6 h** pour le rapatriement, la lecture du disque et la destruction. Ce n'est pas un risque de dépense : l'arrêt est plus court que celui que le plafond suppose. C'est un risque pour le versement de ce qui est récupérable. Deux façons de le traiter :
- l'écrire en chiffre et demander que le rapatriement soit fini avant 22:00Z le 30 ;
- ou avancer la dernière création au 2026-11-27T00:00Z : la coupure tombe alors au plus tard le 28 à 19:26Z, et il reste 52,6 h avant la fin de la ligne, de quoi garder les 48 h.

Ma recommandation est la seconde si le calendrier le permet. C'est un point pour Lazar.

## Coupure propre de l'étalonnage par une règle de la surveillance

Le point est bien posé : alerte à 12 dollars avant la fin de l'étalonnage, arrêt par identifiant, nœud ; la minuterie garde sa seule coupure de 55.

**P2, précision facultative.** Le § 0 dit « tenu à 16,76 par la règle de surveillance ». Or une règle de la surveillance n'est pas une garde automatique : si la surveillance tombe, la seule borne dure reste 59,76. Il faudrait l'écrire, et demander à l'ordre neuf l'essai de cette règle sur un cas sain et sur un artefact (R5). L'écart entre deux relevés de la surveillance coûte quelques centimes à 1,38 dollar par heure.

## Fichiers rendus

`verification-corrections-devis-organisme-retenu-v5-cl1.md` et `rejeu-v6.txt`, chacun avec son compagnon `.sha256`.
