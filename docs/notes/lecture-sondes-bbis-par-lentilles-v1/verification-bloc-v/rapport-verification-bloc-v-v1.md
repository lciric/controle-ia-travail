# Rapport de vérification du BLOC-V — brouillon 2 du texte de lecture des sondes par lentille neuronale — v1

- Modèle : Opus 4.6 (`claude-opus-4-6`), lecteur neuf désigné par Lazar (mot « lecteur opus 4.6 », 2026-11-19T11:01:10Z ; GO-2026-11-19-39 et GO-2026-11-19-42).
- Heure UTC : 2026-11-19 11:16 UTC.
- Je n'ai écrit ni le texte de lecture, ni le critère d'identité, ni le verdict de la tranche.

## Empreintes recalculées

| pièce | empreinte attendue | empreinte recalculée | statut |
|---|---|---|---|
| `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon2.md` | `ff121bddca4786c2c981a335c87000c56e947512ab96068a147198d20a2786bb` | `ff121bddca4786c2c981a335c87000c56e947512ab96068a147198d20a2786bb` | conforme |
| `docs/notes/neuron-lens-v1/lecture-b-beta/verdict-b-beta-v1.md` | `3a9b947e0757dd7f5fe7ecb418b047b94fb274fed84672accabc48926660bb78` | `3a9b947e0757dd7f5fe7ecb418b047b94fb274fed84672accabc48926660bb78` | conforme |

## Vérification des valeurs du BLOC-V (lignes 587 à 623 du brouillon 2)

### Tableau principal (lignes 603 à 613)

| mesure du BLOC-V | colonne | valeur du texte | valeur du verdict (V), avec sa ligne | statut |
|---|---|---|---|---|
| stabilité, différence entre moitiés de notre R, cible `out` (seuil « reproduit » ≤ 0,10 par couche) | couche 7 | 0,0652 | 0,0652 (V, § 3, B-1 : série R `out` couches 0 à 30, huitième valeur) | conforme |
| idem | couche 15 | 0,0295 | 0,0295 (V, § 3, B-1 : série R `out`, seizième valeur) | conforme |
| idem | couche 23 | 0,0143 | 0,0143 (V, § 3, B-1 : série R `out`, vingt-quatrième valeur) | conforme |
| idem | « ce qui en suit » | tient aux trois couches ; les couches au-delà de 0,10 sont 0 et 1 (R `out`), 0 à 2 (R `mid`) | V, § 2, B-1 : « R `mid` couches 0, 1, 2 (0,1114 ; 0,1064 ; 0,1005), R `out` couches 0, 1 (0,1059 ; 0,1033) » ; aucune autre couche au-delà de 0,10 pour ces cibles | conforme |
| stabilité de notre S, cible `out` | couches 7, 15, 23 | ≤ 0,10 chacune | V, § 3, B-1 : « (S `out`) de 0,0075 à 0,1046, croissant pour l'essentiel » ; V, § 2, B-1 : seule la couche 31 dépasse 0,10 (0,1046) | conforme |
| idem | parenthèse | « seule la couche 31 dépasse 0,10, à 0,1046 » | V, § 2, B-1 : « S `out` couche 31 (0,1046) », seule de S `out` dans la liste des six couches-cibles au-dessus de 0,10 | conforme |
| idem | parenthèse | « valeurs par couche non citées par V » | V, § 3, B-1 ne donne que la plage (de 0,0075 à 0,1046) pour S `out`, sans valeur individuelle par couche | conforme |
| accord du premier jeton entre moitiés de notre R | 28 672 pôles | 28 672 | V, § 3, B-1 : « 28 672 pôles par couche » | conforme |
| idem | couche 7 | 0,8678 | 0,8678 (V, § 3, B-1 : série « couches 2, 7, 12, 18, 23, 28 », deuxième valeur) | conforme |
| idem | couche 15 | non mesuré (0,9202 à 12 ; 0,9635 à 18) | V, § 3, B-1 : les couches mesurées sont 2, 7, 12, 18, 23, 28 ; la couche 15 n'y figure pas ; 0,9202 à la couche 12 et 0,9635 à la couche 18 | conforme |
| idem | couche 23 | 0,9754 | 0,9754 (V, § 3, B-1 : cinquième valeur de la série) | conforme |
| accord du premier jeton de chaque moitié de notre R avec la lentille R publique | couche 7 | 0,259 et 0,263 | 0,259/0,263 (V, § 3, B-1 : « accord de chaque moitié avec la lentille R publique … 0,259/0,263 », deuxième paire) | conforme |
| idem | couche 15 | non mesuré (0,426/0,429 à 12 ; 0,687/0,690 à 18) | V, § 3, B-1 : mêmes couches que l'accord entre moitiés (2, 7, 12, 18, 23, 28), couche 15 absente ; 0,426/0,429 à 12 et 0,687/0,690 à 18 | conforme |
| idem | couche 23 | 0,777 et 0,778 | 0,777/0,778 (V, § 3, B-1 : cinquième paire) | conforme |
| lecture contre pilotage, notre R (« steer 1x », bande 8 à 27) | couche 7 | hors bande, non mesurée | V, § 3, B-2 : séries données pour les couches 8 à 27 ; la couche 7 est hors de cette bande | conforme |
| idem | couche 15, `r_med` | 0,8205 | 0,8205 (V, § 3, B-2 : série `r_med` 8–27, huitième valeur, couche 15) | conforme |
| idem | couche 15, `pass` | 1,0 | V, § 3, B-2 : « 0,8594 0,9375 0,9219 1,0 0,9844 1,0 0,9688 1,0 puis 1,0 jusqu'à 27 » ; couche 15 est la huitième valeur = 1,0 | conforme |
| idem | couche 23, `r_med` | 0,9523 | 0,9523 (V, § 3, B-2 : série `r_med` 8–27, seizième valeur, couche 23) | conforme |
| idem | couche 23, `pass` | 1,0 | V, § 3, B-2 : « puis 1,0 jusqu'à 27 » ; la couche 23 est dans cette plage | conforme |
| idem | « ce qui en suit » | la seule condition manquée de la tranche est à la couche 8 (`pass` 0,8594) | V, § 2, B-2 : « seule condition manquée : `pass` = **0,8594** à la couche 8 (seuil 0,90, marge **−0,0406**) » | conforme |
| avance sur la lentille des logits (écart de `r_med`, bande 4 à 15) | couche 7 | 0,3524 | 0,3524 (V, § 3, B-3 : série « écarts 4–15 », quatrième valeur, couche 7) | conforme |
| idem | couche 15 | 0,3115 | 0,3115 (V, § 3, B-3 : douzième valeur, couche 15) | conforme |
| idem | couche 23 | hors bande | V, § 3, B-3 : bande 4 à 15 ; couche 23 est hors bande | conforme |
| deux codes : écart absolu de `r_med` entre notre R et la R publique (bande 0 à 27) | couche 7 | 0,0676 | 0,0676 (V, § 3, B-6 : série des écarts absolus 0–27, huitième valeur) | conforme |
| idem | couche 15 | 0,0302 | 0,0302 (V, § 3, B-6 : seizième valeur) | conforme |
| idem | couche 23 | 0,0112 | 0,0112 (V, § 3, B-6 : vingt-quatrième valeur) | conforme |
| idem | « ce qui en suit » | maximum 0,0878 à la couche 6 | V, § 3, B-6 : septième valeur de la série (couche 6) = 0,0878, plus grande de la série | conforme |
| lecture contre ablation par fenêtre, notre R (« ablate win ») | couche 7 | 0,0639 | 0,0639 (V, § 3, B-7 : huitième valeur, couche 7) | conforme |
| idem | couche 15 | 0,3112 | 0,3112 (V, § 3, B-7 : valeur en gras, couche 15) | conforme |
| idem | couche 23 | non citée par V | V, § 3, B-7 : les valeurs individuelles sont données pour les couches 0 à 15, puis une coupure « … », puis 26 à 29 ; la couche 23 n'est pas citée | conforme |
| idem | parenthèse | 0,8104 à 0,8482 aux couches 26 à 29 | V, § 3, B-7 : « 26–29 : 0,8104 0,8441 0,8219 0,8482 » ; le minimum est 0,8104 (couche 26) et le maximum est 0,8482 (couche 29), la plage est exacte | conforme |
| idem | « ce qui en suit » | aux couches 7 et 15, la lecture prédit mal ce qu'une activation fait en contexte | V, § 2, B-7 : « la lecture prédit mal l'effet d'une activation en contexte **jusqu'à la couche 14**, la couche 15 est **intermédiaire** » ; voir note ci-dessous | **nuance** (voir note) |
| lecture côté entrée, notre S, cible `mid`, `read_S` | couche 7 | 0,06 | 0,06 (V, § 3, B-5 : « `read_S` par couche (journal, deux décimales) 0,82 0,87 0,67 0,53 0,37 0,24 0,10 0,06 », huitième valeur, couche 7) | conforme |
| idem | couche 15 | non citée une à une (série « 0,04 … 0,01 » après la couche 8) | V, § 3, B-5 : après la couche 8 (0,04), le verdict écrit « … 0,01 » sans détailler couche par couche | conforme |
| idem | couche 23 | idem | idem | conforme |
| idem | parenthèse | 0,82 à la couche 0 | V, § 3, B-5 : première valeur de `read_S` = 0,82 (couche 0) ; V, § 2, B-5 : valeur non arrondie 0,8167 | conforme |
| idem | « ce qui en suit » | la cible `out` n'a pas de mesure | V, § 3, B-5 ne mentionne aucune valeur de `read_S` pour la cible `out` | conforme |

**Note sur la nuance (lecture contre ablation, « ce qui en suit »)** : le texte du BLOC-V écrit « aux couches 7 et 15, la lecture prédit mal ce qu'une activation fait en contexte ». Le verdict (V, § 2, B-7) dit « la lecture prédit mal l'effet d'une activation en contexte **jusqu'à la couche 14**, la couche 15 est **intermédiaire**, bien tard ». Le verdict distingue la couche 15 (qualifiée d'« intermédiaire », valeur 0,3112, au-dessus du seuil de 0,25) des couches précédentes (qualifiées de « prédit mal »). Le BLOC-V dit « prédit mal » pour les deux, ce qui ne recopie pas la distinction du verdict. La valeur chiffrée elle-même (0,3112) est conforme ; c'est la qualification en mots qui est légèrement élargie. Cet écart ne porte pas sur une valeur chiffrée mais sur l'interprétation dans la colonne « ce qui en suit », qui n'est pas un seuil ni une garde.

### Repères rassemblés (lignes 615 à 621)

| repère du BLOC-V | valeur du texte | valeur du verdict (V), avec sa ligne | statut |
|---|---|---|---|
| attente A-5 : accord des pôles avec la R publique à la couche 23 | 0,78 | V, § 3, B-1 : 0,777/0,778 (arrondi à deux décimales : 0,78) | conforme |
| attente A-5 : accord des pôles avec la R publique à la couche 7 | 0,26 | V, § 3, B-1 : 0,259/0,263 (arrondi à deux décimales : 0,26) | conforme |
| garde du montage (n) : « écart minimal à la lentille R publique 0,069 » | 0,069, « tel qu'écrit » | V, § 4, garde (n) : « écart minimal à la lentille R publique 0,069 (couches 0–27) » | conforme |
| déclencheur d'audit « mêmes vingt premiers jetons à la couche 7 » | accord des pôles sur le premier jeton ≈ 0,26 | V, § 3, B-1 : accord avec la lentille R publique à la couche 7 = 0,259/0,263, soit ≈ 0,26 | conforme |
| noeud N13 : `read_S` à la couche 7 | 0,06 | V, § 3, B-5 : huitième valeur de la série `read_S` (journal, deux décimales) = 0,06 | conforme |

## Vérification des réserves R-a à R-e (lignes 573 à 579)

| réserve | énoncé du texte (résumé) | ce que dit le verdict | statut |
|---|---|---|---|
| R-a | verdict « partiel » ; la stabilité (B-1) et la lecture contre pilotage (B-2) ne sont pas « reproduit » sur l'ensemble des couches, même si leurs conditions tiennent aux couches 15 et 23 (et, pour la stabilité, à la couche 7) | V, § 1 : « verdict d'ensemble : partiel » ; B-1 = « autre », B-2 = « autre » ; aux couches 7, 15 et 23 de R `out`, les différences de B-1 sont 0,0652, 0,0295, 0,0143, toutes sous 0,10 ; à la couche 15, B-2 `r_med` = 0,8205 et `pass` = 1,0 ; à la couche 23, `r_med` = 0,9523 et `pass` = 1,0 | **conforme au verdict** |
| R-b | à la couche 7, aucune lecture contre pilotage, et un faible accord des deux lentilles R sur les pôles | V, § 3 : B-2 bande 8–27, couche 7 hors bande ; accord avec la R publique à la couche 7 = 0,259/0,263 (environ un quart) | **conforme au verdict** |
| R-c | aux couches 7 et 15, la lecture par R prédit mal l'effet en contexte | V, § 3, B-7 : couche 7 = 0,0639 (très bas) ; couche 15 = 0,3112 ; V, § 2, B-7 : « la lecture prédit mal l'effet d'une activation en contexte **jusqu'à la couche 14**, la couche 15 est **intermédiaire** » | **légèrement déformée** : le verdict qualifie la couche 15 d'« intermédiaire », pas de « prédit mal » ; « prédit mal » ne vaut, dans les mots du verdict, que jusqu'à la couche 14 |
| R-d | notre S : fidélité faible à ces couches pour la cible `mid`, inconnue pour la cible `out` | V, § 3, B-5 : `read_S` = 0,06 à la couche 7, « 0,04 … 0,01 » au-delà de la couche 8 (fidélité faible) ; aucune valeur de `read_S` pour la cible `out` dans le verdict | **conforme au verdict** |
| R-e | réserves du lecteur de V : six gardes sans trace complète, carte H100 non consignée, marges de l'ordre de l'effet du matériel | V, § 1, Réserves : « (1) six gardes constatées sur la machine n'ont **pas de trace complète** » ; « (2) carte H100 (registre des GO), non consignée » ; « deux verdicts tiennent à une marge de l'ordre de l'effet du matériel (B-2 : 3 pôles à la couche 8 ; B-6 : une couche de 21) » | **conforme au verdict** |

## Conclusion

**BLOC-V conforme**, avec un seul écart, non chiffré :
- **Écart en mots** : la réserve (R-c) et la colonne « ce qui en suit » de la ligne « lecture contre ablation par fenêtre » qualifient la couche 15 de « prédit mal », alors que le verdict la qualifie d'« intermédiaire ». La valeur chiffrée correspondante (0,3112) est exacte. Cet écart porte sur une qualification en mots dans une colonne d'interprétation ; il ne touche aucune valeur chiffrée, aucun seuil, aucune garde et aucune condition de lecture du texte.

Toutes les valeurs chiffrées du BLOC-V (vingt-six valeurs numériques, quatre mentions « non mesuré » ou « hors bande », quatre mentions « non cité par V ») sont conformes au verdict scellé de la tranche. Les quatre réserves R-a, R-b, R-d et R-e sont conformes au verdict. La réserve R-c est légèrement déformée dans le sens décrit ci-dessus.
