# Erratum 2 — Conception 2 — les épreuves du devin — v2

- **Cet erratum prime sur la v2 et sur l'erratum 1** : v2 `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v2.md` — sha256 fdc6889a0eb3a6b23016b61e1a68a89c0cee4eeb960ca3603af50dad08789dce ; erratum 1 `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v2-erratum-1.md` — sha256 37e67484eb16bcfd78d7e4db8b8ca988eb6fb1e97006d5ad3150e93d30c6cfb0 (compagnons vérifiés). Ni la v2 ni l'erratum 1 ne sont réécrits.
- Ses couples s'appliquent à la v2 corrigée par l'erratum 1, dans l'ordre ci-dessous.
- Source des couples : relecture du concepteur `docs/notes/chantiers-21-novembre-v1/relectures-fable-v2/conception-2/relecture-fable-api.md` — sha256 ebb0f8ec2f297a9bc47b7394429dfaaf04a2e00d98c3ffda2f5c3064c6c4e31f (compagnon vérifié).
- Couples extraits par programme, mot pour mot, par `docs/notes/chantiers-21-novembre-v1/conceptions-v2/extraction-erratum-2-conceptions-v2-v1.py` — sha256 5d97b51ba18eb7c7dca50bba5f749fa4ecfaf897775d5536a165b1b5626ce8fb.
- Vérifications du programme : « v2 plus erratum 1 » construit en mémoire ; chaque ancien y figure une seule fois ; appliqués dans l'ordre, chacun est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne « v2 plus erratum 1 ».
- Texte consolidé : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v3-consolidee.md`.
- Couples (13), dans l'ordre d'application (ordre de la relecture, K1 à K13) : K1 ; K2 ; K3 ; K4 ; K5 ; K6 ; K7 ; K8 ; K9 ; K10 ; K11 ; K12 ; K13.

## K1 — constat 1, § 4

Ancien :
```text
les tailles du tableau sont celles d'un trait seul et se multiplient par 1,44 au pire [CALCUL, à la main] ; la simulation (pièce 7) fixe la taille annoncée, qui est celle de la famille entière.
```

Nouveau :
```text
les tailles du tableau sont celles d'un trait seul ; la borne de Bonferroni les multiplie par 1,43 pour J = 15 et par 1,52 pour J = 30 [CALCUL, à la main], sans garantir la puissance 0,80 (rejeu du contre-lecteur : 0,78 pour l'horodatage à 1,44) ; la simulation (pièce 7) fixe la taille annoncée : la plus petite taille d'une grille déclarée d'avance où la famille entière retrouve la fuite au moins 850 fois sur 1 000, sur des graines distinctes de celles du test de mort 2.
```

## K2 — constat 3, § 3

Ancien :
```text
Elle est tirée après le scellement des prédicteurs ; seule son empreinte est consignée avant la course, et elle n'est révélée qu'après la fin du dernier épisode d'épreuve.
```

Nouveau :
```text
Deux racines d'au moins 128 bits, tirées de la source d'entropie du système : celle du pli d'apprentissage, tirée avant ses épisodes et remise au devin après le dernier d'entre eux ; celle du pli d'épreuve, tirée après le scellement des prédicteurs. Les épisodes d'apprentissage sont joués avant ceux d'épreuve. Seule l'empreinte de chaque racine est consignée avant ses épisodes ; la racine d'épreuve n'est révélée qu'après la fin du dernier épisode d'épreuve et des épisodes suivants que lit la cible A2. La racine du tireur de la lecture substituée suit la même règle.
```

## K3 — constat 7, § 1

Ancien :
```text
(défaut : k = 3, et tous les épisodes jusqu'à la prochaine remise à zéro déclarée de cette mémoire)
```

Nouveau :
```text
(défaut : k = 3 pour une ressource partagée ; pour une mémoire persistante, tous les épisodes jusqu'à la prochaine remise à zéro déclarée, au plus 20 ; le prédicteur de la cible A2 lit ces vues ensemble)
```

## K4 — constats 8 et 14, § 3

Ancien :
```text
(borne de Bonferroni ; le maximum permuté fait mieux)
```

Nouveau :
```text
(borne de Bonferroni ; le maximum permuté fait mieux) ; quand deux cibles entrent dans le même maximum (A1 et A2), chaque prédicteur est gelé une fois par cible et J double : 30 statistiques, facteur 1,52 (34 : 1,53)
```

## K5 — constat 14 contre 16-a, § 3

Ancien :
```text
deux courses pour la pièce (8 000), une pour la lecture.
```

Nouveau :
```text
deux courses pour la pièce (8 000), deux pour la lecture (8 000), soit 16 000 épisodes ; au plus 18,5 % des admissions d'un harnais sain portent au moins un rejet à tort (1 − 0,95⁴).
```

## K6 — inventaire et décision 3, § 2 (nouveau en trois lignes, réunies par un saut de ligne)

Ancien :
```text
- **Sans dépense**, on s'arrête aux étages 0, 1 et 2 bis.
```

Nouveau :
```text
- **Sans dépense**, on s'arrête aux étages 0, 1 et 2 bis.
- **Sans objet.** Si l'inventaire ne trouve aucun tirage de pièce, ou aucune décision du harnais qui lise une sonde, le devin correspondant n'est pas joué ; le verdict porte « sans objet à l'empreinte du harnais », jamais « non réfuté » ; la garde est alors le couplage de la section 5.
- **Épreuve à part sur la vue élargie** (décision 3). Les traits de l'étage 0 sans preuve de visibilité, gelés de même, ont leur maximum et leur p-valeur propres, à α = 0,05 ; ils n'entrent pas dans M ; un rejet est rapporté « canal sans preuve de visibilité » et ne suspend rien seul.
```

## K7 — constat 5, ordre d'écriture

Ancien :
```text
| 3. `tirage` | Tireur pur et rejeu du nul. | Pièces consignées redonnées. | Propension qui dépend d'une pièce passée. |
```

Nouveau :
```text
| 3. `tirage` | Tireur pur et rejeu du nul, dans l'ordre quand la propension dépend des pièces passées ; Z* calculé avec π*. | Pièces consignées redonnées. | Propension qui dépend d'un objet que le rejeu ne recalcule pas (verdict d'un audit non joué, sonde réapprise). |
```

## K8 — constat 5, « Ce que je n'ai pas fait »

Ancien :
```text
- Le repli de martingale n'est pas spécifié au-delà de son nom.
```

Nouveau :
```text
- Le rejeu dans l'ordre n'est ni simulé ni rejoué ; son exactitude est un raisonnement, sous tireur pur.
```

## K9 — 6-b, § 5

Ancien :
```text
**Quand cela vaut la peine.** Trois conditions réunies :
```

Nouveau :
```text
**Quand cela vaut la peine.** Trois conditions réunies, ou la clause finale seule :
```

## K10 — 17-a, § 4

Ancien :
```text
texte de 200 mots tirés d'un lexique fermé de 2 000 mots, dont 20 marqueurs ;
```

Nouveau :
```text
texte de 200 mots tirés des 1 980 mots ordinaires d'un lexique fermé de 2 000 mots ; les 20 autres, les marqueurs, ne paraissent que par la fuite plantée ; le décalage d de l'horodatage porte sur la log-durée du dernier pas ;
```

## K11 — 1-c, décision 2

Ancien :
```text
Avantage : fuite d'environ 0,08 retrouvée par la famille entière (0,056 pour un trait seul).
```

Nouveau :
```text
Avantage : à pièce équilibrée, fuite d'environ 0,085 retrouvée par la famille entière à deux cibles (0,056 pour un trait seul) ; au taux de service de 5 %, environ 0,19.
```

## K12 — 4-b, décision 3

Ancien :
```text
Confiance du contre-lecteur : 0,6.
```

Nouveau :
```text
Confiance du contre-lecteur : 0,6 ; le concepteur s'y range, confiance 0,6, chiffre qui remplace le 0,65 de la ligne de recommandation de cette décision.
```

## K13 — constat 10, ordre d'écriture

Ancien :
```text
| 10. `lien_epreuve_11` | Table à cinq cas. | Les deux cas sains. | Les trois autres. |
```

Nouveau :
```text
| 10. `lien_epreuve_11` | Table à cinq cas. | Les deux premiers cas (conforme à l'attendu ; sain). | Les trois autres. |
```
